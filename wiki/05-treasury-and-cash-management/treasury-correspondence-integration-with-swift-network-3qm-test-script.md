---
id: 05-treasury-and-cash-management/treasury-correspondence-integration-with-swift-network-3qm-test-script
title: "Treasury Correspondence Integration with SWIFT Network (3QM) - Test Script, SAP S/4HANA Cloud Public Edition (3QM_S4CLD2608_BPD_EN_XX)"
description: "SAP test script for scope item 3QM: set up and test treasury SWIFT correspondence (MT300/MT320) via SAP Multi-Bank Connectivity, from BP settings to settlement."
cluster: 05-treasury-and-cash-management
tags: [kb/treasury-and-cash-management, topic/treasury-trading-platforms-and-swift]
aliases: [3QM_S4CLD2608_BPD_EN_XX]
keywords: [Treasury Trading Platforms and SWIFT Correspondence, swift integration, treasury correspondence, multi-bank connectivity, swift messages, correspondence settings, bic assignment, inbound correspondence, outbound correspondence, correspondence monitoring]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/3QM_S4CLD2608_BPD_EN_XX.docx]
confidence: low
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-968
topic: 05-treasury-and-cash-management/treasury-trading-platforms-and-swift
language: EN
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Treasury Correspondence Integration with SWIFT Network (3QM) - Test Script, SAP S/4HANA Cloud Public Edition (3QM_S4CLD2608_BPD_EN_XX)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/3QM_S4CLD2608_BPD_EN_XX.docx`, extracted with `mammoth`. Grouped under **Treasury Trading Platforms and SWIFT Correspondence** in Treasury and Cash Management. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

| <!-- image omitted: unnamed --> | Test ScriptSAP S/4HANA Cloud Public Edition - 19-06-26 |
| --- | --- |
|  | Treasury Correspondence Integration with SWIFT Network (3QM) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Table of Contents

[1 Purpose 3](#_Toc232832452)

[2 Prerequisites 4](#_Toc232832453)

[2.1 System Access 4](#_Toc232832454)

[2.2 Roles 4](#_Toc232832455)

[2.3 Master Data, Organizational Data, and Other Data 4](#_Toc232832456)

[2.4 Preliminary Steps 5](#_Toc232832457)

[2.4.1 Setup the Communication Integration 5](#_Toc232832458)

[2.4.2 Maintain Correspondence Setting for Business Partner 6](#_Toc232832459)

[2.4.2.1 Maintain Profile and BP Group Assignments to External Recipient 6](#_Toc232832460)

[2.4.2.2 Assign BC or External Security Account ID to Business Partner 9](#_Toc232832461)

[2.4.2.3 Assign Correspondence Class for Inbound 10](#_Toc232832462)

[2.4.2.4 Assign Business Partner Group for Inbound Correspondence 11](#_Toc232832463)

[2.4.2.5 Assign Business Partner Group to Depository Bank for Inbound Process 13](#_Toc232832464)

[2.4.2.6 Update BIC of Payment Bank 14](#_Toc232832465)

[2.4.3 Maintain Additional Settings 15](#_Toc232832466)

[3 Overview Table 17](#_Toc232832467)

[4 Test Procedures 19](#_Toc232832468)

[4.1 Create Financial Instruments Transaction 19](#_Toc232832469)

[4.1.1 Create IR Instrument 19](#_Toc232832470)

[4.1.2 Create FX Forward 21](#_Toc232832471)

[4.2 Create Outgoing Correspondence Object and Outbound SWIFT Message 22](#_Toc232832472)

[4.3 Check Outbound Correspondence Object Status 23](#_Toc232832473)

[4.4 Send Outbound SWIFT Message to MBC 24](#_Toc232832474)

[4.5 Pull Acknowledgment Message from MBC 25](#_Toc232832475)

[4.6 Check Outbound Correspondence Object Status 25](#_Toc232832476)

[4.7 Pull Inbound SWIFT Message from MBC 26](#_Toc232832477)

[4.8 Create Incoming Correspondence Object and Match with Outgoing Object 26](#_Toc232832478)

[4.9 Check Matching of Correspondence Objects 27](#_Toc232832479)

[4.10 Check Transaction Status 27](#_Toc232832480)

## Purpose

Overview

This scope item uses SAP Multi-Bank Connectivity to integrate treasury correspondence with the SWIFT network.

SWIFT messages for treasury OTC transactions can be delivered to the counterparty's SWIFT code using SAP Multi-Bank Connectivity. SAP Multi-Bank Connectivity acts as a hub and forwards the message to the SWIFT network.

Meanwhile, the SWIFT messages can be sent back from their counterparty via SAP Multi-Bank Connectivity, and relevant incoming correspondence objects are generated automatically in the SAP client. Once the incoming correspondence object is matched with the outgoing correspondence object with confirmation, the OTC transaction is settled accordingly. This function currently covers MT300 for Foreign Exchange instruments and MT320 for Debt and Investment instruments.

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
| Treasury Specialist - Back Office | SAP_BR_TREASURY_SPECIALIST_BOE | Treasury Back Office | SAP_BR_TREASURY_SPECIALIST_BOE |  |
| Treasury Specialist - Front Office | SAP_BR_TREASURY_SPECIALIST_FOE | Treasury Front Office | SAP_BR_TREASURY_SPECIALIST_FOE |  |
| Cash Management Specialist | SAP_BR_CASH_SPECIALIST | Cash Management | SAP_BR_CASH_SPECIALIST |  |

### Master Data, Organizational Data, and Other Data

The organizational structure and master data of your company has been created in your system during activation. The organizational structure reflects the structure of your company. The master data represents materials, customers, and vendors, for example, depending on the operational focus of your company.

|  |
| --- |
| Caution Update Behavior of Predelivered Demo DataIn non-productive environments (such as starter systems, sandbox systems, or partner demo systems), SAP initially deploys demo data for your selected scope. You can use this data to test and evaluate business processes.In a customer system, you can receive new or updated demo data after initial activation with further scope enhancements, provided the existing demo data wasn't changed in an incompatible way. If activation errors occur due to incompatible changes in demo data, you're responsible for resolving them. If you don't resolve the errors within a specific time frame, SAP reserves the right to deactivate demo data in your systems. In this case, you can continue by creating your own demo data. Alternatively, you can request that your systems be reprovisioned if you want to work with predelivered demo data again.In partner systems, you can use the demo data deployed with the initial activation. No additional demo data will be deployed in the system with scope enhancements. You can only create additional demo data manually. |

|  |
| --- |
| Caution Sample values for master data values are country-specific and the values provided in the following table are for DE. Substitute the country-specific values provided by the Best Practices for SAP S/4HANA or use master data values you have created for this purpose. |

| Data | Sample Value | Details | Comments |
| --- | --- | --- | --- |
| Company Code | 1010 |  |  |
| Currency | EUR and USD |  |  |
| Business Partner | 10537001 |  |  |
| Bank Number | 50070010 |  |  |
| Bank Country | DE |  |  |

Table 1: Master Data Script Reference

| MDS | Description |
| --- | --- |
| 22G | Create Business Partner for Treasury and Risk Management - MDS |

### Preliminary Steps

#### Setup the Communication Integration

Purpose

This step enables the SWIFT Message communication between the registered SAP S/4HANA tenant and the SAP Multi-Bank Connectivity (MBC), which is formerly known as Financial Services Network (FSN).

Procedure

Please contact your on-boarding trainer for the SAP MBC (Multi-bank connectivity) tenant registration and the communication scenario SAP_COM_ 1002 setup.

During testing, the message communication will be simulated with special SWIFT self-test server. The dummy acknowledge response and inbound message will be sent from self-test server, triggered automatically by outbound message.

#### Maintain Correspondence Setting for Business Partner

Purpose

SAP TRM provides the standard correspondence functionality. With this correspondence functionality, whenever a TRM transaction is saved, SAP sends an SWIFT message to the SWIFT Code of the business partner via MBC component.

To use this correspondence functionality, the following data needs to be assigned to the Business Partner:

- Business Partner Profile
- Business Partner group
- Swift/BIC code

##### Maintain Profile and BP Group Assignments to External Recipient

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

Business partner profiles and business partner groups control the correspondence activities in SAP TRM.

SAP has predefined the following Business Partner profile:

- PR_MBC

SAP has predefined the following Business Partner group:

- BPG_SWIFT

You can assign this business partner group to your business partner. You can also use configuration step Define Business Partner Group to add your own business partner group and assign appropriate attributes according to your specific requirement. Different business partner profiles and BP groups could be assigned to the same business partner.

|  |
| --- |
| Note Depending on your configuration environment, configuration steps can be accessed under Configure Your Solution in the SAP Fiori launchpad or in the Business Processes Configuration app in the project experience of SAP Central Business Configuration. |

This step describes how to assign business partner profile and BP group to an external business partner.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as Treasury Specialist - Back Office. | The SAP Fiori Launchpad displays. |  |
| 2 | Access the SAP Fiori app | Open Assign Profile and BP Group - External Recipients (FTR_EXT_ASSIGN). | The Assignment of Profiles and BP Groups to External Recipients screen displays. |  |
| 3 | Enter Business partner data on the screen | On the left side of Assignment of Profiles and BP Groups to External Recipientsscreen, choose Insert Row and enter the following data, and choose Modify Row.BusPartner: for example, 10537001CoCd: for example, 1010Recpt/Send Type: for example, COUNTERPARTYCheckbox: <select>Note When testing other country, use the related company code and business partner instead, for example, for US, company code is 1710, and business partner is 17537001. | The Business Partner information is entered. |  |
| 4 | Assign Business profile and BP group to the Business Partner | On the top-right side of Assignment of Profiles and BP Groups to External Recipients screen, choose Expand Node to expand BP:0010537001 /CoCd: 1010 / Rec/SendType: COUNTERPARTY -> Money Market -> Interest rate instrument -> 51A Fixed-Term Deposit/Borrowing -> 100 Investment, select 10 Contract.On the bottom-right side of Assignment of Profiles and BP Groups to External Recipients screen, choose Delete Row to delete all existing items, then choose Insert Row, and enter the following data:Profile: for example, PR_MBCBP Group: for example, BPG_SWIFTChoose Insert Row again and add another entry as following and choose Save.Note For the automatic settlement, there should be only one profile to a product type/transaction type/activity category, you need to remove other existing profile, such as 'PR_EMAIL' or 'PR_PRINT'.. | Business partner profiles and BP groups are assigned for the Product type/Transaction type/Activity category. |  |
| 5 | Repeat the previous step to assign BP profiles and BP groups to the rest of Product type/Transaction Type/Activity category | Repeat the above step for following product types and transactions:Product TypeTransaction TypeAct. Category51A1001051A2001055A1001055A2001060A1012060A1022060A1032060A1042060A1052060A1072060B1032060B1035560B1042060B1045560B1052060B1055560B1102060B11055 | For all the listed Product Types/Transaction Types/Activity Categories, BP profiles and BP groups are assigned. |  |

##### Assign BC or External Security Account ID to Business Partner

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The SWIFT Code and Business Identifier Codes (BIC) are used to uniquely identify banks and financial institutions globally. For each business partner, a SWIFT/BIC code can be assigned for different combination of Recipient Type/Sender Type.

This step describes how to assign SWIFT/BIC code to a business partner.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as Treasury Specialist - Back Office. | The SAP Fiori Launchpad displays. |  |
| 2 | Access the SAP Fiori app | Open Assign BIC to Business Partners (FTR_BP_BIC) | The "Assign BIC to Business Partners": Changescreen displays. |  |
| 3 | Enter Swift/BIC data for one correspondence class | On the "Assign BIC to Business Partners": Change screen, choose New Entries. On the New Entries: Details of Added Entries screen, enter the following data and choose Save:Item 1BusPartner: for example, 10537001Note This business partner value is DE-specific. Replace this with master data value you created or pre-delivered by Best Practices for SAP S/4HANA, for example, use 17537001 for US.Valid From: for example, <January 1st of Previous Year>Recpt/Send Type: select COUNTERPARTYCorrespondClass: select DEAL_MMSWIFT/BIC: for example, DEUTDEFFItem 2BusPartner: for example, 10537001Note This business partner value is DE-specific. Replace this with master data value you created or pre-delivered by Best Practices for SAP S/4HANA, for example, use 17537001 for US.Valid From: for example, <January 1st of Previous Year>Recpt/Send Type: select COUNTERPARTYCorrespondClass: select, DEAL_FXSWIFT/BIC: for example, DEUTDEFF | The Swift/BIC code information of the business partner is maintained for the correspondence class. |  |

##### Assign Correspondence Class for Inbound

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

For each Business partner, assign correspondence class for inbound process dependent on recipient.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log onto the SAP Fiori Launchpad as Treasury Specialist - Back Office. | The SAP Fiori Launchpad displays. |  |
| 2 | Access the SAP Fiori app | Open Assign Correspondence Class - Inbound Process (FTR_INB_FUNC). | The "Inbound Process: Correspondence Class Assig..": Change screen displays. |  |
| 3 | Enter Assignment for Correspondence class | On the "Inbound Process: Correspondence Class Assig..": Change screen, choose New Entries. On the New Entries: Details of Added Entries screen, enter the following data and choose Save:Item 1Format: for example, MT300BPartner: for example, 10537001Recipient/SendType: select COUNTERPARTYCorrespondence Class: for example, DEAL_FXItem 2Format: for example, MT320BPartner: for example, 10537001Recipient/SendType: select COUNTERPARTYCorrespondence Class: for example, DEAL_MMNote For US, use Business Partner 17537001 instead. | The Swift/BIC code information of the business partner is maintained for the correspondence class. |  |

##### Assign Business Partner Group for Inbound Correspondence

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you assign business partner group for inbound correspondence.

|  |
| --- |
| Note The values for company code and business partner are DE specific. Replace the values withthe master data value you created or those pre-delivered by Best Practices for SAP S/4HANA, for example, use 1710 and 17537001 respectively for US. |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori Launchpad as Treasury Specialist - Back Office. | The SAP Fiori Launchpad displays. |  |
| 2 | Access the SAP Fiori app | Open Assign Business Partner Group - Inbound Process (FTR_INB_ASSIGN). | The "BP Group Assignment for Inbound Corresponde..": Change screen displays. |  |
| 3 | Enter Assignment for Correspondence class | On the "BP Group Assignment for Inbound Corresponde..": Change screen, choose New Entries, on the New Entries: Details of Added Entries screen, enter the following data and choose Save:Item 1BPartner: for example, 10537001CoCd: for example, 1010Recipient/SendType: select COUNTERPARTYCorrespondence Class: for example, DEAL_FXBusiness Partner Group: for example, BPG_SWIFTItem 2BPartner: for example, 10537001CoCd: for example, 1010Recipient/SendType: select COUNTERPARTYCorrespondence Class: for example, DEAL_MMBusiness Partner Group: for example, BPG_SWIFTItem 3BPartner: for example, 10537001CoCd: for example, 1010Recipient/SendType: select COUNTERPARTYCorrespondence Class: for example, <Blank>Business Partner Group: for example, BPG_SWIFT | The Swift/BIC code information of the business partner is maintained for the correspondence class. |  |

##### Assign Business Partner Group to Depository Bank for Inbound Process

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you assign the business partner group to depository bank for the inbound process.

The step is required to support receiving MT535 message via MBC channel. The external securities account statement can be imported automatically. Refer to Reconciliation of External Securities Account Statements in the Appendix section for more details.

Prerequisite

A Business Partner with TR0152 Depository Bank is created with ID 10537001. Refer to Create Security Account for Investment in test script Bond Management 3WY for maintenance.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Treasury Specialist - Back Office. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori app | Open Assign Business Partner Group - Inbound Process (FTR_INB_ASSIGN). | The "BP Group Assignment for Inbound Correspondence" Change screen is displayed. |  |
| 3 | Switch to Change Mode | On the "BP Group Assignment for Inbound Correspondence" Change screen, choose New Entries in the new screen and enter the following data:BPartner: for example, 10537001CoCd: for example, 1010Recipient/Send Type: for example, DEPOSITORYBANKCorrespondence Class: for example, SEC_STMNT_HOLDBusiness Partner Group: for example, BPG_DEPOBANKChoose Enter and then choose Save. | The New Entres: Added Entries screen is displayed. |  |

##### Update BIC of Payment Bank

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, update BIC for payment bank.

|  |
| --- |
| Caution Sample values for master data values are country/region-specific and the values provided in the following table are for Germany (DE). Substitute the country/region-specific values provided by the Best Practices for SAP S/4HANA or use master data values you have created for this purpose. |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as Cash Management Specialist | The SAP Fiori Launchpad displays. |  |
| 2 | Access the SAP Fiori app | Open Manage Banks - Master Data (F6437). | The Manage Banks - Master Data screen displays. |  |
| 3 | Display Bank data on the screen | On the top plane of Manage Banks - Master Data screen, enter following data, and choose Go.Bank Country/Region: for example, DEBank Number: for example, 50070010Note This bank master data values above are DE-specific. Replace them with master data value you created or pre-delivered by Best Practices for SAP S/4HANA, for example, use US and 011000390 respectively for US.Choose Bank name to display. | The information of Bank 50070010 information is displayed. |  |
| 4 | Edit Bank data | On the Edit screen, choose Edit, enter the following data and choose Save:Bank Name: Bank 1 SAMPLE BANKSWIFT/BIC: for example, DEUTDEFFStreet: for example, Franklinstra 46-48City: for example, FrankfurtNote If a warning message is displayed, skip it. | SWIFT BIC is updated. |  |

#### Maintain Additional Settings

You need to maintain additional settings by the following SSCUI's in Configure Your Solution or SAP Central Business Configuration depending on which configuration environment you are in：

- Define Company Code Additional Data

In this configuration step, you assign bank identifier code (BIC) for company codes, which are regarded as sender ID in the SWIFT message.

Activities

-
    1. Enter company code and choose Details, for example, enter company code 1010 for DE, or other country-specific value you defined or pre-delivered by Best Practices for SAP S/4HANA, for example, 1710 for US.
    2. Enter the BIC in the SWIFT/BIC field of the General Settings area, for example, enter SWIFT/BIC ASPXDEF0
    3. Save your entries.
- Assign SWIFT Parameters for Outbound Messages

In this configuration step, maintain SWIFT parameters for receiver ID.

Table 2: Sample Data

| Receiver ID | Message Type | Parameter Name | Parameter Value |
| --- | --- | --- | --- |
| DEUTDEFF | MT300 | Service | swift.fin |
| DEUTDEFF | MT300 | RequestType | fin.300 |
| DEUTDEFF | MT300 | Responder | o=swift |
| DEUTDEFF | MT300 | SenderBIC | ASPXDEF0AXXX |
| DEUTDEFF | MT300 | ReceiverBIC | ASPXDEF0XXXX |
| DEUTDEFF | MT300 | SenderDN | o=ASPXDEFF,o=swift |
| DEUTDEFF | MT320 | SenderDN | o=ASPXDEFF,o=swift |
| DEUTDEFF | MT320 | SenderBIC | ASPXDEF0AXXX |
| DEUTDEFF | MT320 | ReceiverBIC | ASPXDEF0XXXX |
| DEUTDEFF | MT320 | Service | swift.fin |
| DEUTDEFF | MT320 | RequestType | fin.320 |
| DEUTDEFF | MT320 | Responder | o=swift |

## Overview Table

The scope item consists of several process steps in the table below.

|  |
| --- |
| Note If your system administrator has enabled spaces and pages on the SAP Fiori launchpad, the homepage will only contain the essential apps for performing the typical tasks of a business role.You can find all other (searchable) apps not included on the homepage using the search bar ([2434549](https://me.sap.com/notes/2434549)).If you want to personalize the homepage and include the hidden apps, navigate to your user profile and choose App Finder. |

| Process | Business Role | Transaction /APP | Expected Results |
| --- | --- | --- | --- |
| [Create IR Instrument](#unique_16) [page ] 19 | Treasury Specialist - Front Office | Create IR Instrument (TM_51) | An interest rate instrument is created. |
| [Create FX Forward](#unique_17) [page ] 21 | Treasury Specialist - Front Office | Create FX Spot/Forward (TX01) | A FX Forward instrument is created. |
| [Create Outgoing Correspondence Object and Outbound SWIFT Message](#unique_18) [page ] 22 |  |  |  |
| [Check Outbound Correspondence Object Status](#unique_19) [page ] 23 | Treasury Specialist - Back Office | Process Correspondence - Monitor (FTR_COMONI) | The status of correspondence objects are Acknowledgement awaited. |
| [Send Outbound SWIFT Message to MBC](#unique_20) [page ] 24 |  |  | The SWIFT message is automatically sent to Multi-Bank Connectivity (MBC). |
| [Pull Acknowledgment Message from MBC](#unique_21) [page ] 25 |  |  | SAP S/4HANA pulls the acknowledgement message from MBC. |
| [Check Outbound Correspondence Object Status](#unique_22) [page ] 25 | Treasury Specialist - Back Office | Process Correspondence - Monitor (FTR_COMONI) | The status of correspondence objects is Delivery. |
| [Pull Inbound SWIFT Message from MBC](#unique_23) [page ] 26 |  |  | SAP S/4HANA pulls the Inbound SWIFT message from MBC. |
| [Create Incoming Correspondence Object and Match with Outgoing Object](#unique_24) [page ] 26 |  |  |  |
| [Check Matching of Correspondence Objects](#unique_25) [page ] 27 | Treasury Specialist - Back Office | Process Correspondence - Monitor (FTR_COMONI) | The status of correspondence objects is Match. |
| [Check Transaction Status](#unique_26) [page ] 27 | Treasury Specialist - Back Office | Process Correspondence - Monitor (FTR_COMONI) | The transaction is settled |

## Test Procedures

This section describes test procedures for each process step that belongs to this scope item.

### Create Financial Instruments Transaction

Purpose

Currently, SWIFT Message communication supports foreign exchange instruments and debt and investment instruments. In this section, you will create an interest rate instrument transaction and a FX spot/forward transaction.

#### Create IR Instrument

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you create an interest rate instrument transaction as an example for testing purpose. For creation of other types of debt and investment instruments, please refer to the 1WV: Debt and Investment Management test script.

|  |
| --- |
| Note The outbound SWIFT message is generated and sent to the MBC tenant after a deal is created. |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Treasury Specialist - Front Office | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the SAP Fiori app | Open Create IR Instrument (TM_51). | The Create Interest Rate Instrument screen is displayed. |  |
| 3 | Create A New Deal | On the Create Interest Rate Instrument screen, enter the following data and press Enter:Company Code: for example, 1010Product Type: 55ATransaction Type: for example, 200Partner: for example, 10537001Note When testing other country, use the related company code and business partner instead; such as for US, company code is 1710, business partner is 17537001. | The Create Interest Rate Instrument: Structure screen is displayed. |  |
| 4 | Maintain Structure of New Deal | On the Create Interest Rate Instrument: Structure screen, enter the following data:Nominal Amount: for example, 10MStart: for example, <Current Date>End: for example, <Current Date + 3 years>Interest Cat.: for example, FixedPercentage Rate: for example, 3.0000000Int. Calc. Method: for example, act/360Frequency: for example, MonthlyContract Date: for example, <Current Date>/<Current Time> |  |  |
| 5 | Maintain Administration of New Deal | On the Administr. tab, enter following data:Portfolio: for example, Y000Gen. Valn Class: For example, Long term debt(non-current liability |  |  |
| 6 | Maintain Payment Details of New Deal | On the Payment Details tab, you can find the incoming line with direction of flow "+" and outgoing row with direction of flow "-". Double click on the outgoing row, and maintain the following data:Payment Request With: <select this checkbox>House Bank: for example, DEBK1Account ID: for example, DEAC1Payer/Payee: for example, 10537001Partner Bank: for example, EUR1Payment Methods: for example, TNote The data above is Germany-specific. Replace the values with other country-specific ones you defined or pre-delivered by Best Practices for SAP S/4HANA. |  |  |
| 7 | Save the New Deal | Choose Check to verify the input data. If no error message is displayed, choose Save | Interest rate instrument was created. Note down the transaction number for consequent steps. |  |

#### Create FX Forward

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you create a foreign exchange forward transaction as an example for the testing purpose. For creation of other types of foreign exchange transactions, please refer to the 1X1: Foreign Currency Risk Management test script.

|  |
| --- |
| Note The outbound SWIFT message is generated and sent to the outbox folder when a deal is created. The message will be eliminated in the outbox in 10 minutes. You can process the [Send Outbound SWIFT Message to MBC](#unique_20) [page ] 24 step first to download the message. |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Treasury Specialist - Front Office | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the SAP Fiori app | Open Create FX Spot/Forward (TX01). | The Spot/Forward Transaction Entry: Initial screen is displayed. |  |
| 3 | Enter Selection Criteria | Enter the following data and press Enter:Company Code: for example, 1010Product Type: 60ATransaction Type: for example, 102Partner: for example, 10537001Note When testing other country, use the related company code and business partner instead, for example, for US, company code is 1710, business partner is 17537001. | The Spot/Forward Transaction Entry: Structure screen is displayed. |  |
| 4 | Enter Structure Data | On the Spot/Forward Transaction Entry: Structure screen, enter the following data:Rate: for example, EUR/USD 1.2Buy/Sell: for example, B BuyTraded Amt: for example, USD 1MValue Date: ++2 | The Administr. tab displays. |  |
| 5 | Enter Data in Administration tab | On the Administr. tab, enter the following data and choose Save:Hdg Classific.: for example, Y0Risk Mitigation: for example, CheckNote Check the Risk Mitigation field if this transaction is intended for risk mitigation purpose, in which case this transaction will be excluded from Clearing Threshold Report calculation. | Transaction is saved and a transaction number is generated.Note Note down the transaction number for consequent steps. |  |

### Create Outgoing Correspondence Object and Outbound SWIFT Message

Purpose

In this step, the correspondence object and relevant outbound SWIFT Message are generated automatically. SWIFT Message is sent to MBC automatically when SAP S/4HANA is connected to MBC.

Procedure

This step is done automatically.

### Check Outbound Correspondence Object Status

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you will check the status of the correspondence objects.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log onto the SAP Fiori Launchpad as a Treasury Specialist - Back Office. | The SAP Fiori Launchpad displays. |  |
| 2 | Access the SAP Fiori app | Open Process Correspondence - Monitor (FTR_COMONI) | The Correspondence Monitor screen displays. |  |
| 3 | Enter selection criteria on the initial screen | On the Correspondence Monitor screen, enter following data and choose Execute:Under group Correspondence,Company Code: for example, 1010Under the deal tab,Company Code: for example, 1010Deal Number: for example, <Noted Transaction Number>Note When testing other country, use the related company code instead; such as for US, company code is 1710. | The Correspondence monitor - Standard View screen displays.Note Note down the Correspondence Reference ID in the Corr. Internal Ref column for later use. |  |
| 4 | Check the correspondence status | On the Correspondence monitor - Standard View screen, all the correspondence objects are displayed in the status column.Note One financial transaction could have one or more correspondence objects depending on the BP profiles and BP groups assignment.For the channel MBC, the Acknowledgement awaited status means SAP MBC has tried to send the SWIFT message to the SWIFT Code of the business partner, but the acknowledge response hasn't been received; if the acknowledgeresponse is received, the correspondence object status is Delivery. | The status of correspondence objects is in Acknowledgement awaited. |  |
| 5 | Display the transaction details | On the Correspondence monitor - Standard View screen, select the checkbox for the line with following data and choose Show Underlying.Recpt/Send TypeChannelCOUNTERPARTYMBCChoose Back to return to the Correspondence monitor - Standard View screen. | The transaction details display.Note Note down the Correspondence Internal Reference number in the Corr.Internal Ref for later use. |  |
| 6 | Display the Message detail of the correspondence object | On the Correspondence monitor - Standard View screen, select the checkbox for the line with following data and choose View Message.Recpt/Send TypeChannelCOUNTERPARTYMBCA message displays. Choose Continue to close the dialog box. | The SWIFT Message of the correspondence object displays. |  |

### Send Outbound SWIFT Message to MBC

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The SWIFT message is automatically sent to Multi-Bank Connectivity (MBC).

However, if you use configuration step Define Business Partner Group and create new business partner group and don't assign the autosend attribute, you may need to send those correspondence objects manually via the Send Correspondence (FTR_COSEND) app.

|  |
| --- |
| Note Depending on your configuration environment, configuration steps can be accessed under Configure Your Solution in the SAP Fiori launchpad or in the Business Processes Configuration app in the project experience of SAP Central Business Configuration. |

### Pull Acknowledgment Message from MBC

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

When the counterparty receives the outbound message, the acknowledge response is pulled automatically from MBC to the SAP client. The system matches the response to the outgoing correspondence object, then update the outgoing correspondence object status to Delivery.

In testing, the SWIFT message communication will be simulated with specific a SWIFT self-test server. The acknowledge should be received via MBC automatically.

|  |
| --- |
| Note The acknowledge is received after several minutes. |

### Check Outbound Correspondence Object Status

Purpose

In this step, you review the status of the correspondence object. If the acknowledge file is captured and matched correctly, the status of the correspondence object is changed to Delivery.

Procedure

Reprocess the [Check Outbound Correspondence Object Status](#unique_19) [page ] 23 step to check the updated correspondence object status.

### Pull Inbound SWIFT Message from MBC

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

Once the inbound SWIFT Message is arrived, the message is pulled from MBC automatically. The SAP S/4HANA system then imports the inbound SWIFT Message and the generated relevant incoming correspondence object.

In testing, the SWIFT Message exchange will be simulated with specific SWIFT self-test server, the inbound message is received from MBC component automatically.

|  |
| --- |
| Note It would take several minutes. |

### Create Incoming Correspondence Object and Match with Outgoing Object

Purpose

The Incoming correspondence object is generated for the inbound SWIFT Message, and matched with the outgoing correspondence object automatically.

Procedure

This step is done automatically.

### Check Matching of Correspondence Objects

Purpose

If the correspondence objects are matched correctly, the status of the outing and incoming correspondence objects should be changed to Completed according to the system setting.

Procedure

Reprocess step [Check Outbound Correspondence Object Status](#unique_19) [page ] 23 to check the updated correspondence object status.

### Check Transaction Status

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

Once the incoming correspondence object is matched with the outgoing correspondence object with confirmation, the relevant transaction should be settled automatically.

In this step, you will check if the transaction has been settled automatically.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori launchpad as a Treasury Specialist - Back Office. | The SAP Fiori Launchpad displays. |  |
| 2 | Access the SAP Fiori app | Open Process Correspondence - Monitor (FTR_COMONI) | The Correspondence Monitor screen displays. |  |
| 3 | Enter selection criteria on the initial screen | On the Correspondence Monitor screen, enter following data and choose Execute:Under group Correspondence,Company Code: for example, 1010Under tab deal,Company Code: for example, 1010Company Code: for example, <Noted Transaction Number>Note When testing other country, use the related company code instead; such as for US, company code is 1710. | The Correspondence monitor - Standard View screen displays. |  |
| 4 | Display the transaction history | On the Correspondence monitor - Standard View screen, select the checkbox of the incoming correspondence object, choose Show Underlying. Now the transaction detail screen displays. | Activity 2 Contract Settlement displaysin second line. |  |

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
> Flagged while digesting this document, not verified: Final correspondence status after matching is named inconsistently: the Overview Table expects status 'Match', while the Check Matching of Correspondence Objects section says outgoing and incoming objects change to 'Completed according to the system setting'.

## Connections
- part-of :: [[_cluster]]
- related-to :: [[05-treasury-and-cash-management/test-script-treasury-trading-via-trading-platforms-2f5-sap-s-4hana-clo-part-01]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/3QM_S4CLD2608_BPD_EN_XX.docx` — full document · extracted with `mammoth` · 42,909 chars in the whole document
