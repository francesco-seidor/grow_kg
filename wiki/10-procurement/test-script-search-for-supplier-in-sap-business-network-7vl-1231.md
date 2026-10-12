---
id: 10-procurement/test-script-search-for-supplier-in-sap-business-network-7vl-1231
title: "Test Script: Search for Supplier in SAP Business Network (7VL) (7VL_S4CLD2608_BPD_EN_XX)"
description: "Test script for scope item 7VL: searching suppliers in SAP Business Network from S/4HANA Cloud, requesting supplier creation, and informing the buyer."
cluster: 10-procurement
tags: [kb/procurement, topic/business-network-purchase-to-pay]
aliases: [7VL_S4CLD2608_BPD_EN_XX]
keywords: [Purchase-to-Pay Automation with SAP Business Network, supplier search, sap business network, supplier creation request, supplier profile, discovery postings, supplier master data, business roles, test scripts, additional manual configuration]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/7VL_S4CLD2608_BPD_EN_XX.docx]
confidence: high
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-1231
topic: 10-procurement/business-network-purchase-to-pay
language: EN
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Test Script: Search for Supplier in SAP Business Network (7VL) (7VL_S4CLD2608_BPD_EN_XX)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/7VL_S4CLD2608_BPD_EN_XX.docx`, extracted with `mammoth`. Grouped under **Purchase-to-Pay Automation with SAP Business Network** in Procurement. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

| <!-- image omitted: unnamed --> | Test ScriptSAP S/4HANA Cloud Public Edition - 19-06-26 |
| --- | --- |
|  | Search for Supplier in SAP Business Network (7VL) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Table of Contents

[1 Purpose 2](#_Toc232828694)

[2 Prerequisites 3](#_Toc232828695)

[2.1 System Access 3](#_Toc232828696)

[2.2 Roles 3](#_Toc232828697)

[2.3 Additional Manual Configuration 3](#_Toc232828698)

[3 Overview Table 4](#_Toc232828699)

[4 Test Procedure 5](#_Toc232828700)

[4.1 Launch SAP Business Network Supplier Search 5](#_Toc232828701)

[4.2 Search Supplier 5](#_Toc232828702)

[4.3 View Profile Details 6](#_Toc232828703)

[4.4 Create Discovery Posting for Additional Information (Optional) 7](#_Toc232828704)

[4.5 Request Supplier Creation 8](#_Toc232828705)

[4.6 Review Supplier 8](#_Toc232828706)

[4.7 Create Supplier (Optional) 9](#_Toc232828707)

[4.8 Inform Buyer 10](#_Toc232828708)

## Purpose

Overview

The Supplier Search functionality in SAP S/4HANA Cloud Public Edition - enabled through integration with the SAP Business Network - helps users identify and select suitable suppliers using general search criteria. It supports supplier discovery and evaluation by providing access to a broad network of suppliers and their basic profiles, enabling better sourcing decisions and improving procurement efficiency.

This document provides a detailed procedure for testing this scope item after solution activation, reflecting the predefined scope of the solution. Each process step, report, or item is covered in its own section, providing the system interactions (test steps) in a table view. Steps that are not in scope of the process but are needed for testing are marked accordingly. Project-specific steps must be added.

|  |
| --- |
| Note Values in this test script (decimal notation, date formats, and so on) are presented in U.S. standard notation. If your test system is set up to use a different notation, enter values as appropriate. |

## Prerequisites

This section summarizes all the prerequisites for conducting the test in terms of systems, users, master data, organizational data, other test data and business conditions.

### System Access

| System | Details |
| --- | --- |
| SAP S/4HANA Cloud Public Edition | Accessible via the SAP Fiori launchpad. Your system administrator provides you with the URL to access the various apps assigned to your role. |
| SAP Business Network | Accessible via SAP Business Network. Your system administrator provides you with the URL and logon data to access SAP Business Network. |

### Roles

Create business roles using the following business role templates delivered by SAP and assign them to your individual test users.

Alternatively, if available, you can use the following spaces delivered by SAP. You create a space with pages containing predefined essential apps and assign it to the business role. You then assign this business role to your individual users.

For more information, refer to How to Create a Business Role from a Template in the [product assistance](https://help.sap.com/docs/SAP_S4HANA_CLOUD/53e36b5493804bcdb3f6f14de8b487dd/ec310a8b669a45ca898dc4dd91d97de2.html) for SAP S/4HANA Cloud Public Edition.

| Name (Role Template) | ID (Role Template) | Name (Launchpad Space) | ID (Launchpad Space) |
| --- | --- | --- | --- |
| Purchaser | SAP_BR_PURCHASER | Purchasing / Sourcing and Contracting | SAP_MM_SPT_PURCHASING_PC / SAP_MM_SPT_SOURCING_PC |
| Master Data Specialist - Business Partner Data | SAP_BR_BUPA_MASTER_SPECIALIST | Master Data - Business Partners / Business Partner Governance / Business Partner Governance / Business Partner Governance | SAP_BR_BUPA_MASTER_SPECIALIST / SAP_CA_SPT_MDG_BP_GOV_PC / SAP_CMD_SPT_BP_GOV_PC / SAP_CA_SPT_MDG_BP_WFUSR_PC |

### Additional Manual Configuration

Before you can test this scope item, you must have completed the additional configuration steps that are described in the Set-Up Instructions for this scope item. These configuration steps are specific for your implementation and include mandatory settings that are not delivered by SAP and must be created by you. For more information, follow the link to the document:

[Link to Set-Up Instructions](https://help.sap.com/docs/SAP_S4HANA_BEST_PRACTICES/74e2c75b80f6ffb2c1ed62cc7965dfef)

## Overview Table

This scope item consists of several process steps provided in the following table.

|  |
| --- |
| Note If your system administrator has enabled spaces and pages on the SAP Fiori launchpad, the homepage will only contain the essential apps for performing the typical tasks of a business role.You can find all other (searchable) apps not included on the homepage using the search bar ([2434549](https://me.sap.com/notes/2434549)).If you want to personalize the homepage and include the hidden apps, navigate to your user profile and choose App Finder. |

| Process Step | Business Role | App/Transaction | Expected Results |
| --- | --- | --- | --- |
| [Launch SAP Business Network Supplier Search](#unique_7) [page ] 5 | Purchaser | Search Suppliers in SAP Business Network | You are directed to SAP Business Network. |
| [Search Supplier](#unique_8) [page ] 5 | User in SAP Business Network | SAP Business Network | You can search suppliers. |
| [View Profile Details](#unique_9) [page ] 6 | User in SAP Business Network | SAP Business Network | You can view details of the company profile. |
| [Create Discovery Posting for Additional Information (Optional)](#unique_10) [page ] 7 | User in SAP Business Network | SAP Business Network | You can request more information. |
| [Request Supplier Creation](#unique_11) [page ] 8 | User in SAP Business Network | SAP Business Network | Master data specialist in SAP S/4HANA Cloud Public Edition receives an email. |
| [Review Supplier](#unique_12) [page ] 8 | Master Data Specialist - Business Partner Data | Link in request email from SAP Business Network | Master data specialist checks supplier details via the link attached in the email. |
| [Create Supplier (Optional)](#unique_13) [page ] 9 | Master Data Specialist - Business Partner Data | Maintain Business Partner (BP) or Manage Supplier Master Data (F1053A) | Supplier master data is created. |
| [Inform Buyer](#unique_14) [page ] 10 | Master Data Specialist - Business Partner Data | Email | Master data specialist replies the email and inform buyer about the supplier creation process. |

## Test Procedure

### Launch SAP Business Network Supplier Search

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you can navigate to SAP Business Network from SAP S/4HANA Cloud Public Edition.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori launchpad using business role Purchaser. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the App | Go to Sourcing and Contracting - Source of Supplier Management, and find app Search Suppliers in SAP Business Network. | The app is displayed. |  |
| 3 | Access SAP Business Network | Click the app tile. | You will be navigated to SAP Business Network. |  |

### Search Supplier

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you can search for suppliers in SAP Business Network.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Business Network using a business role with adequate authorization. | The SAP Business Network interface displays. |  |
| 2 | Search Supplier | In the trading partner search bar, search for the supplier you want to find by typing in the category, product, company or location keywords, for example, computer. Press Enter.In section Filters, you can further narrow down the search results by entering your cretiria in the filter fields, for example,Categories: <Computer programmers>Service Locations: <North America> | Your search results are displayed. |  |

### View Profile Details

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you can view profile details of selected suppliers.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Business Network using a business role with adequate authorization. | The SAP Business Network interface displays. |  |
| 2 | View Profile Details | Choose the supplier you are interested in.On Company Profile screen, a detailed company profile is displayed. You can check the company’s overview, credentials, organization structure and other information. | Profile details of selected suppliers are displayed. |  |

### Create Discovery Posting for Additional Information (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you can request more information regarding certain suppliers.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Business Network using a business role with adequate authorization. | The SAP Business Network interface displays. |  |
| 2 | Request for Information | On screen Company Profile, choose the Request for Information botton.A Request for Information form displays. The mandatory fields are Title, Description, and Response Deadline.In section Description, enter a detailed description of your buying needs, and specify the information supplier should provide.Choose Send. | Your information request will be sent. |  |
| 3 | View Exchange History (Optional) | If you want to find previous information requests, choose Discovery. |  |  |

### Request Supplier Creation

In this step, you can send an email to master data specialist to create a new supplier in SAP S/4HANA Cloud Public Edition.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Business Network using a business role with adequate authorization. | The SAP Business Network interface displays. |  |
| 2 | Trigger Email | Choose Send Supplier Request to request the master data specialist to create a new supplier in SAP S/4HANA Cloud Public Edition. The message Supplier request sent successfully will display.Users with administrator role can go to Notifications > Master Data Management Notifications and edit the recipient email address. | Master data specialist will receive the email requesting to add a new supplier. |  |

### Review Supplier

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, master data specialist will review information of the suggested supplier.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Check Email | The master data specialist checks the email sent by SAP Business Network. | The email sent by SAP Business Network displays. |  |
| 2 | Review supplier | There is a link in the email that directs to the supplier’s public profile in SAP Business Network. Choose this link to complete supplier review.Alternatively, the master data specialist can also go to SAP S/4HANA Cloud Public Edition to check if the suggested supplier exists. | The master data specialist can review information about the suggested supplier. |  |

### Create Supplier (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

If the suggested supplier does not exist in SAP S/4HANA Cloud Public Edition, the master data specialist can find general information on how to create supplier master data in the following [Master Data Scripts (MDS)](https://help.sap.com/docs/s4hana-best-practices/s4cld2608-master-data) :

| MDS | Description |
| --- | --- |
| BNE | Create Supplier Master - MDS |

### Inform Buyer

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, master data specialist informs purchaser the supplier creation status via email.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Reply Email | The requester email address is included in the email sent by SAP Business Network.The master data specialist can write to the email address, and inform purchaser about the supplier creation process. | The purchaser learns about the latest status. |  |

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
- related-to :: [[10-procurement/test-script-automated-purchase-to-pay-with-sap-ariba-commerce-automati]]
- related-to :: [[10-procurement/test-script-automation-of-central-procurement-quote-with-sap-business]]
- related-to :: [[08-sales-order-management/test-script-automation-of-order-to-invoice-with-sap-business-network-4]]
- related-to :: [[10-procurement/test-script-automation-of-source-to-pay-with-sap-business-network-42k]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/7VL_S4CLD2608_BPD_EN_XX.docx` — full document · extracted with `mammoth` · 17,036 chars in the whole document
