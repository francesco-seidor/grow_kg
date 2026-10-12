---
id: 10-procurement/test-script-request-for-price-1xf-ae-780
title: Test Script - Request for Price (1XF_AE) (1XF_S4CLD2608_BPD_EN_AE)
description: "SAP S/4HANA Cloud 2608 test script for scope item 1XF_AE (UAE): RFQ creation, supplier quotations, award, purchase contract follow-on, low-quotation situation handling."
cluster: 10-procurement
tags: [kb/procurement, topic/request-for-quotation]
aliases: [1XF_S4CLD2608_BPD_EN_AE]
keywords: [Request for Price and Quotation Comparison, request for quotation, supplier quotation, quotation award, situation handling, procurement test scripts, follow-on documents, flexible workflow, teams and responsibilities, business roles]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/1XF_S4CLD2608_BPD_EN_AE.docx]
confidence: high
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-780
topic: 10-procurement/request-for-quotation
language: EN
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Test Script - Request for Price (1XF_AE) (1XF_S4CLD2608_BPD_EN_AE)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/1XF_S4CLD2608_BPD_EN_AE.docx`, extracted with `mammoth`. Grouped under **Request for Price and Quotation Comparison** in Procurement. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

| <!-- image omitted: unnamed --> | Test ScriptSAP S/4HANA Cloud Public Edition - 19-06-26 |
| --- | --- |
|  | Request for Price (1XF_AE) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Table of Contents

[1 Purpose 3](#_Toc232848499)

[2 Prerequisites 4](#_Toc232848500)

[2.1 System Access 4](#_Toc232848501)

[2.2 Role 4](#_Toc232848502)

[2.3 Master Data, Organizational Data, and Other Data 5](#_Toc232848503)

[2.4 Business Conditions 6](#_Toc232848504)

[2.5 Preliminary Steps 6](#_Toc232848505)

[2.5.1 Configure Flexible Workflow for RFQs 6](#_Toc232848506)

[2.5.2 Configure Flexible Workflow for Supplier Quotation 6](#_Toc232848507)

[2.5.3 Manage Teams and Responsibilities 7](#_Toc232848508)

[2.5.4 Create Situation Type for Low Number of Received Quotations 8](#_Toc232848509)

[3 Overview Table 10](#_Toc232848510)

[4 Test Procedures 11](#_Toc232848511)

[4.1 Create Price Request 11](#_Toc232848512)

[4.2 Create Supplier Quotation 12](#_Toc232848513)

[4.3 Display Supplier Quotation (Optional) 14](#_Toc232848514)

[4.4 Compare and Award Supplier Quotation 15](#_Toc232848515)

[4.5 Create Follow-on Documents 16](#_Toc232848516)

[4.6 Detect and React to Situation (Optional) 17](#_Toc232848517)

[4.6.1 Detect Critical Low Number of Received Quotations Situation 17](#_Toc232848518)

[4.6.2 React to Critical Low Number of Received Quotations Situation 17](#_Toc232848519)

## Purpose

Overview

With this scope item, you can create requests for quotations in the SAP S/4HANA Cloud Public Edition system and send them to a supplier via e-mail or as a printed version by mail. The suppliers provide their quotations via e-mail or by mail as well. You can manually create a quotation in the SAP S/4HANA Cloud Public Edition system using the Manage Supplier Quotations app. By default, a new quotation has the status In Preparation. You select a quotation that you want to award and submit it for approval. After awarding the quotation, the follow-on documents are created in SAP S/4HANA Cloud Public Edition. The quotations that do not meet your requirements must be manually set to Rejected/Completed.

This document provides a detailed procedure for testing this scope item after solution activation, reflecting the predefined scope of the solution. Each process step, report, or item is covered in its own section, providing the system interactions (test steps) in a table view. Steps that are not in scope of the process but are needed for testing are marked accordingly. Project-specific steps must be added.

|  |
| --- |
| Note Values in this test script (decimal notation, date formats, and so on) are presented in U.S. standard notation. If your test system is set up to use a different notation, enter values as appropriate. |

## Prerequisites

This section summarizes all prerequisites needed to conduct the test in terms of system, users, master data, organizational data, and other test data and business conditions.

### System Access

| System | Details |
| --- | --- |
| System | Accessible via SAP Fiori launchpad. Your system administrator provides you with the URL to access the various apps assigned to your role. |

### Role

Create business roles using the following business role templates delivered by SAP and assign them to your individual test users.

Alternatively, if available, you can use the following spaces delivered by SAP. You create a space with pages containing predefined essential apps and assign it to the business role. You then assign this business role to your individual users.

For more information, refer to How to Create a Business Role from a Template in the [product assistance](https://help.sap.com/docs/SAP_S4HANA_CLOUD/53e36b5493804bcdb3f6f14de8b487dd/ec310a8b669a45ca898dc4dd91d97de2.html) for SAP S/4HANA Cloud Public Edition.

| Name (Role Template) | ID (Role Template) | Name (Launchpad Space) | ID (Launchpad Space) | Log On |
| --- | --- | --- | --- | --- |
| Purchaser | SAP_BR_PURCHASER | Purchasing / Sourcing and Contracting | SAP_MM_SPT_PURCHASING_PC / SAP_MM_SPT_SOURCING_PC |  |
| Business Process Specialist | SAP_BR_BUSINESS_PROCESS_SPEC | Business Process Management / Business Process Management | SAP_BR_BUSINESS_PROCESS_SPEC / SAP_CA_SPT_BPS_PC |  |
| Administrator | SAP_BR_ADMINISTRATOR | Administration / Administration - Workforce Master Data / Administration - License Compliance / Administration - Data Management / Administration - Output Control | SAP_BR_ADMINISTRATOR / SAP_BUM_SPT_ADMINISTRATION_PC / SAP_EI_SPT_ADM_LC_PC / SAP_CA_SPT_TDR_PC / SAP_OC_SPT_ADMINISTRATION_PC |  |
| Business Process Specialist | SAP_BR_BUSINESS_PROCESS_SPEC | Business Process Management / Business Process Management | SAP_BR_BUSINESS_PROCESS_SPEC / SAP_CA_SPT_BPS_PC |  |

### Master Data, Organizational Data, and Other Data

The organizational structure and master data of your company has been created in your system during activation. The organizational structure reflects the structure of your company. The master data represents materials, customers, and vendors, for example, depending on the operational focus of your company.

|  |
| --- |
| Caution Update Behavior of Predelivered Demo DataIn non-productive environments (such as starter systems, sandbox systems, or partner demo systems), SAP initially deploys demo data for your selected scope. You can use this data to test and evaluate business processes.In a customer system, you can receive new or updated demo data after initial activation with further scope enhancements, provided the existing demo data wasn't changed in an incompatible way. If activation errors occur due to incompatible changes in demo data, you're responsible for resolving them. If you don't resolve the errors within a specific time frame, SAP reserves the right to deactivate demo data in your systems. In this case, you can continue by creating your own demo data. Alternatively, you can request that your systems be reprovisioned if you want to work with predelivered demo data again.In partner systems, you can use the demo data deployed with the initial activation. No additional demo data will be deployed in the system with scope enhancements. You can only create additional demo data manually. |

Use your own master data or the following sample data to go through the test procedure.

| Data | Sample Value | Details | Comments |
| --- | --- | --- | --- |
| Plant | 3310 | Plant 1 AE |  |
| Company Code | 3310 | Company Code 3310 |  |
| Purchase Organization | 3310 | Purch. Org. 3310 |  |
| Purchasing Group | 001 | Group 001 |  |
| Vendor | 33300001 | Domestic UAE Supplier 1 |  |
| Vendor | 33300002 | Domestic UAE Supplier 2 |  |
| Material | TG0011 | Trading Good 0011,PD,Regular Proc.no Serial no.; no batch |  |

You can find general information on how to create master data objects in the following Master Data Scripts (MDS):

| MDS | Description |
| --- | --- |
| BNF | Create Product Master of type "Trading Good" - MDS |

### Business Conditions

To run through this scope item, the materials must be available in stock. You can create stock using the Manage Stock or Transfer Stock apps

| Scope Item | Business Condition |
| --- | --- |
| 31N - Situation Handling | This scope item must be installed for situation handling steps. |

### Preliminary Steps

#### Configure Flexible Workflow for RFQs

Purpose

In this activity, you configure automatic approval workflow for RFQs.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1. | Log on | Log on to the Fiori Launch Pad as a Configuration Expert - Business Process Configuration . | The Fiori Launchpad is displayed. |  |
| 2. | Open Manage Workflows for RFQs | Open Manage Workflows for RFQs (F3232). | The Manage Workflows screen is displayed. |  |
| 3. | Check and Activate Automatic Release of RFQ Workflow | Check Status of workflow Automatic Release of RFQ.If status is Inactive, select the workflow Automatic Release of RFQ and choose Activate. | The automatic approval workflow for RFQ is configured. |  |

#### Configure Flexible Workflow for Supplier Quotation

Purpose

In this activity, you configure automatic approval workflow for Supplier Quotation.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1. | Log on | Log on to the Fiori Launch Pad as a Configuration Expert - Business Process Configuration . | The Fiori Launchpad is displayed. |  |
| 2. | Open Manage Workflows for Supplier Quotations | Open Manage Workflows for Supplier Quotations (F2704). | The Manage Workflows screen is displayed. |  |
| 3. | Check and Activate Automatic Release of Supplier Quote Workflow | Check Status of workflow Automatic Release of Supplier Quote.If status is Inactive, select the workflow Automatic Release of Supplier Quote and choose Activate. | The automatic approval workflow for Supplier Quotation is configured. |  |

#### Manage Teams and Responsibilities

Purpose

In this activity, you create teams and responsibilities for RFQs.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori Launchpad using the Configuration Expert - Business Process Configuration role. | The SAP Fiori Launchpad is displayed. |  |
| 2 | Access the App | Open Manage Teams and Responsibilities - Procurement (F2412). | The Manage Teams and Responsibilities screen is displayed. |  |
| 3 | Create team and responsibilities | Choose Create and make following entries:Name: PROC_RFQ_TEAMGlobal ID: PROC_RFQ_TEAMDescription: Procurement RFQ TeamStatus: EnabledType: OPPURIn the Responsibility Definitions section, make the following entries:Purchasing Group:001Purchasing Organization: 3310In the Team Members area, choose Create and make the following entries:Business Partner: use the search function to find the business partner of PurchaserFunctions: Operational Purchasing |  |  |
| 4 | Save Team | Choose Create. | The team is created. |  |

#### Create Situation Type for Low Number of Received Quotations

Purpose

In this activity, you create situation type for low number of received quotations.

When a purchaser logs into the SAP Fiori launchpad, the notification RFQ XXX is close to the submission deadline XXX – Low number of received quotations will appear. The submitted quotation criteria can be maintained in custom situation types. The framework checks the quotation information of the RFQ. If it meets the criteria defined in custom situation types, a situation is then triggered, and notification is sent. The purchaser can then navigate from the SAP Fiori launchpad notification to RFQ object. The purchaser can then choose to dismiss the situation and take corrective actions. Dismissing a situation will ensure that no further situation messaging is triggered for the same situation type and RFQ number. The purchaser can choose one of the following reasons to dismiss the situation message:

- Obsolete
- Resolve
- Invalid

|  |
| --- |
| Note 31N -Situation Handling is required to execute this step. |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori launchpad using the Business Process Specialist role. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the App | Open Manage Situation Types (F2947). | The Manage Situation Types screen is displayed. |  |
| 3 | Copy Standard Situation Template | On the Manage Situation Types screen, choose Go.Choose standard situation template PROC_RFQLOWNUMBEROFQTN.Low number of received quotations and choose Copy. |  |  |
| 4 | Create Ready-to-Use Situation Type | It will create a ready-to-use situation type.On the Situation Type screen, make the following entry:ID: ZPROC_RFQLOWNUMBEROFQTN (for example)This field is the unique identifier of a ready-to-use situation type. The ID of a ready-to-use situation type should start with 'Z' or 'Y'. ID is a mandatory field and cannot be left blank.Name: Low number of received quotations (for example)This field is the name of the ready-to-use situation type.Go to section Condition:Choose Process Order 1 Instance StatusOpen and make the following entries:Bidding Ratio in %: less than 50 (for example)Days to Quotation Deadline: less than 30 (for example)Go to section Recipients and make the following entries:Filter by Responsibility Definition: Purchasing Group, Purchasing OrganizationFilter by Member Functions: Operational PurchasingGo to section Situation Monitoring:Check Monitor Instances.Go to the section Batch Job Scheduling:Choose one time zone in the field Time Zone and maintain the time for the field Start Batch Job At.Choose Save. | The ready-to-use situation type has been saved. |  |
| 5 | Enable Ready-to-Use Situation Type | On the Do you want to enable the situation type? pop up screen, choose Yes. | The ready-to-use situation type is enabled. |  |

## Overview Table

This scope item consists of several process steps provided in the table below.

|  |
| --- |
| Note If your system administrator has enabled spaces and pages on the SAP Fiori launchpad, the homepage will only contain the essential apps for performing the typical tasks of a business role.You can find all other (searchable) apps not included on the homepage using the search bar ([2434549](https://me.sap.com/notes/2434549)).If you want to personalize the homepage and include the hidden apps, navigate to your user profile and choose App Finder. |

| Process Step | Business Role | App/Transaction | Expected Results |
| --- | --- | --- | --- |
| [Create Price Request](#unique_13) [page ] 11 | Purchaser | Manage RFQs (F2049) |  |
| [Create Supplier Quotation](#unique_14) [page ] 12 | Purchaser | Manage RFQs (F2049) |  |
| [Display Supplier Quotation (Optional)](#unique_15) [page ] 14 | Purchaser | Manage RFQs (F2049) |  |
| [Compare and Award Supplier Quotation](#unique_16) [page ] 15 | Purchaser | Compare Supplier Quotations (F2324) |  |
| [Create Follow-on Documents](#unique_17) [page ] 16 | Purchaser | Manage Supplier Quotations (F1991) |  |
| Detect and React to Situation | Purchaser |  |  |

## Test Procedures

This section describes test procedures for each process step that belongs to this scope item.

### Create Price Request

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you create a Price Request (from an existing Purchase Requisition).

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the Fiori Launch Pad as a Purchaser. | The Fiori Launchpad is displayed. |  |
| 2 | Open Manage RFQs | Open Manage RFQs (F2049). | The Manage RFQs screen is displayed. |  |
| 3 | Create Price Request | Choose Create (on the right top of the screen), and select Int. Sourcing Req.On the Request for Quotation screen make the following entries:Tab General Information:RFQ Description: Request for Price (1XF)Quotation Deadline: today + 7 daysPurchasing Group: 001Purchasing Organization: 3310Company Code: 3310Follow-On Document Type: MKValidity Per. Start: todayValidity Period End: today + 1 monthTab Delivery and Payment Terms:Target Value: 3500.00Currency: AEDTab Items:Make the following entries:Material: TG0011Plant: 3310Requested Quantity: 100Delivery Date: today + 2 monthTab Bidders:Add one or more bidder, for example:Supplier: 33300001 and 33300002Choose Create. | A new Request for Quotation is created with a new ID xxx |  |
| 4 | Publish Request for Quotation | Click Publish button at the top right of the screen. | The Request for Quotation is in approval.Workflow is triggered with automatic approval.The Request for Quotation is published. |  |

### Create Supplier Quotation

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you create a Supplier Quotation.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the Fiori Launch Pad as a Purchaser. | The Fiori Launchpad is displayed. |  |
| 2 | Open Manage RFQ | Open Manage RFQs (F2049). | The Manage RFQs is displayed with a list of existing RFQ Document items. |  |
| 3 | Search for RFQ | Make the following entries and choose Go:Company Code: 3310RFQ Type: Int. Sourcing Req.Status: PublishedPurchasing Organization: 3310Purchasing Group: 001 | You search for the previous created RFQ. |  |
| 4 | Open Request for Quotation | Select the previous created RFQ xxx and open it. |  |  |
| 5 | Create First Supplier Quotation | Select supplier 33300001 in the Bidders Facet and click on Create Quotation.On the Supplier Quotation screen, make the following entries:Tab General Information:Quotation Submission Date: todayTab Items:Net Order Price: 30.00Choose Create.ou can ignore message If you have selected a value contract, please enter a target value. | The supplier quotation xxx was created. |  |
| 6 | Submit First Supplier Quotation | On the Supplier Quotation screen choose Submit. | The supplier quotation was submitted. |  |
| 7 | Back to Manage RFQ | Go back. |  |  |
| 8 | Create Second Supplier Quotation | Select supplier 33300002 in the Bidders Facet and click on Create Quotation.On the Supplier Quotation screen, make the following entries:Tab General Information:Quotation Submission Date: todayTab Items:Net Order Price: 35.00Choose Create.You can ignore message If you have selected a value contract, please enter a target value. | The supplier quotation xxx was created. |  |
| 9 | Submit Second Supplier Quotation | On the Supplier Quotation screen choose Submit. | The supplier quotation was submitted. |  |

### Display Supplier Quotation (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you log in to the SAP S/4HANA system and display the automatically created supplier quotation.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the Fiori Launch Pad as a Purchaser. | The Fiori Launchpad is displayed. |  |
| 2 | Open Mange RFQs | Open Manage RFQs (F2049). | The Manage RFQs screen is displayed with a list of existing Request for Quotations items. |  |
| 3 | Search for Request for Quotation | Make the following entries and choose Go:Company Code: 3310RFQ Type: Int. Sourcing Req.Purchasing Organization: 3310Purchasing Group: 001 | You search for the previous created RFQ. |  |
| 4 | Open Request for Quotation | Select previous created RFQ xxx and open it. |  |  |
| 5 | Display Supplier Quotation | Go to the Quotations tab and view the created Quotation with IDxxx | The Quotation xxx is displayed in the column Supplier Quotation. |  |

### Compare and Award Supplier Quotation

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you log in to the SAP S/4HANA system and award the automatically created supplier quotation.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the Fiori Launch Pad as a Purchaser. | The Fiori Launchpad is displayed. |  |
| 2 | Open Compare Supplier Quotation | Open Compare Supplier Quotations (F2324). | The Compare Supplier Quotations screen is displayed. |  |
| 3 | Search Request for Quotation | Input or select previous created RFQ xxx. | You select the created Request for Quotation. |  |
| 4 | Compare Supplier Quotation | Check and compare quotations from different Supplier. |  |  |
| 5 | Award Supplier Quotation | Select one quotation with Best-Priced Items and choose Award. | Quotation XXX is in approval.Workflow is triggered with automatic approval. |  |

### Create Follow-on Documents

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you log in to the SAP S/4HANA system and display the automatically created purchase order.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1. | Log on | Log on to the Fiori Launch Pad as a Purchaser. | The Fiori Launchpad is displayed. |  |
| 2. | Open Manage Supplier Quotations | Open Manage Supplier Quotations (F1991). | The Manage Supplier Quotations screen is displayed. |  |
| 3. | Search for Supplier Quotation | Make the following entries and choose Go:RFQ Type: Int. Sourcing Req.Company Code: 3310Status: AwardedPurchasing Organization: 3310Purchasing Group: 001 | You search for the previous awarded Supplier Quotation. |  |
| 4. | Open Supplier Quotation | Select previous awarded Supplier Quotation xxx and click on the arrow > at the end of the row. |  |  |
| 5. | Create Follow-on Documents | On the Supplier Quotation screen, choose Follow-On Documents and then choose Create Purchase Contract. | The Purchase Contract screen is displayed. |  |
| 6. | Save Follow-on Documents | Choose Create to save the Purchase Contract. | A new Purchase Contract is created. |  |

### Detect and React to Situation (Optional)

#### Detect Critical Low Number of Received Quotations Situation

The system automatically detects critical situations, which refer to the RFQ is close to submission deadline and has not sufficient number of quotations. The detection process is automatically triggered by the system on a regular basis and indicates critical Low Number of Received Quotations situations to the purchaser, using the notification functionality on the home screen. This enables the purchaser to proactively react to situations and avoid negative implications to the business of the company.

#### React to Critical Low Number of Received Quotations Situation

Purpose

In this activity, you can monitor Low Number of Received Quotations situation through the notification.

Situation and Notification will be triggered according to criteria set in preliminary steps. System automatically detects Low Number of Received Quotations situations by daily job, and indicates critical situations using the notification functionality on the home screen. This enables Team Member to proactively react and avoid negative implications to the business processes of the company.

|  |
| --- |
| Note You must perform step [Create Situation Type for Low Number of Received Quotations](#unique_11) [page ] 8 and [Manage Teams and Responsibilities](#unique_10) [page ] 7 before testing this step. |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori Launchpad using the Purchaser role. | The SAP Fiori Launchpad is displayed. |  |
| 2 | Choose the notifications | Choose the Notifications icon which is at the top right of the Home screen.Choose the notifications: RFQ XXX is close to the submission deadline XXX – Low number of received quotations which is generated by the system batch daily job. | The RFQ Item screen is displayed. |  |
| 3 | Check and React Situation Message | On the Request for Quotation screen, detail situation message is displayed in Situations tab.You can choose Dismiss and pick a reason for dismissing the situation. | Situation Message is shown and dismissed. |  |

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
- related-to :: [[10-procurement/request-for-quotation-customer-specification-en-de-255]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/1XF_S4CLD2608_BPD_EN_AE.docx` — full document · extracted with `mammoth` · 27,445 chars in the whole document
