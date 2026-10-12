---
id: 05-treasury-and-cash-management/test-script-sap-s-4hana-cloud-public-edition-treasury-workstation-paym
title: Test Script SAP S/4HANA Cloud Public Edition - Treasury Workstation Payment Integration (3NA) (3NA_S4CLD2608_BPD_EN_XX)
description: "SAP S/4HANA Cloud 2608 test script for scope item 3NA: Treasury payment requests sent by IDoc to a receiving FI system, with reversal, roles and test steps."
cluster: 05-treasury-and-cash-management
tags: [kb/treasury-and-cash-management, topic/treasury-accounting-integration]
aliases: [3NA_S4CLD2608_BPD_EN_XX]
keywords: [Treasury Workstation Accounting Integration, treasury payment integration, payment request generation, idoc monitoring, message dashboard, payment request reversal, receiving system mapping, communication connection setup, business roles, test scripts]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/3NA_S4CLD2608_BPD_EN_XX.docx]
confidence: high
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-963
topic: 05-treasury-and-cash-management/treasury-accounting-integration
language: EN
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Test Script SAP S/4HANA Cloud Public Edition - Treasury Workstation Payment Integration (3NA) (3NA_S4CLD2608_BPD_EN_XX)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/3NA_S4CLD2608_BPD_EN_XX.docx`, extracted with `mammoth`. Grouped under **Treasury Workstation Accounting Integration** in Treasury and Cash Management. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

| <!-- image omitted: unnamed --> | Test ScriptSAP S/4HANA Cloud Public Edition - 19-06-26 |
| --- | --- |
|  | Treasury Workstation Payment Integration (3NA) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Table of Contents

[1 Purpose 2](#_Toc232832923)

[2 Prerequisites 3](#_Toc232832924)

[2.1 System Access 3](#_Toc232832925)

[2.2 Roles 3](#_Toc232832926)

[2.3 Master Data, Organizational Data, and Other Data 4](#_Toc232832927)

[2.4 Additional Manual Configuration 4](#_Toc232832928)

[2.5 Preliminary Steps 5](#_Toc232832929)

[2.5.1 Set up the Communication Connection 5](#_Toc232832930)

[2.5.2 Maintain Mapping Rule in Receiving System 5](#_Toc232832931)

[3 Overview Table 7](#_Toc232832932)

[4 Test Procedures 8](#_Toc232832933)

[4.1 Process TRM Transactions and Post Flow to Generate Payment Request 8](#_Toc232832934)

[4.2 Monitor IDoc in Sending System 12](#_Toc232832935)

[4.3 Monitor IDoc in Receiving System 13](#_Toc232832936)

[4.4 Check and Process Payment Request in Receiving System 14](#_Toc232832937)

[4.5 Set the Transaction Related Posting Flow for Reverse 15](#_Toc232832938)

[4.6 Reverse Transaction 16](#_Toc232832939)

[4.7 Monitor IDoc in Sending System 17](#_Toc232832940)

[4.8 Monitor IDoc in Receiving System 18](#_Toc232832941)

[4.9 Check and Process the Payment Request 19](#_Toc232832942)

## Purpose

Overview

This scenario fulfills the requirements for deploying Treasury and Risk Management in SAP S/4HANA Cloud Public Edition, while keeping the payment in an existing central Financial Accounting system. In such cases, the Treasury and Risk Management component of SAP S/4HANA Cloud Public Edition can trigger the payment request creation or cancellation. Requests are then generated in an SAP S/4HANA Cloud Public Edition or SAP ERP system.

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
| Configuration Expert - Business Network Integration | SAP_BR_CONF_EXPERT_BUS_NET_INT | Business Network Integration / Business Network Integration - Concur Integration / Business Network Integration - Output Control / Business Network Integration - Data Replication / Configuration Expert - Business Network Integration Cross Applications | SAP_CORE_SPT_INT_PC / SAP_CON_SPT_CONCUR_INT_PC / SAP_OC_SPT_INT_PC / SAP_CA_SPT_DATA_REP_PC / SAP_CA_SPT_BUS_NETWORK_INT_PC |  |
| Administrator | SAP_BR_ADMINISTRATOR | Administration / Administration - Workforce Master Data / Administration - License Compliance / Administration - Data Management / Administration - Output Control | SAP_BR_ADMINISTRATOR / SAP_BUM_SPT_ADMINISTRATION_PC / SAP_EI_SPT_ADM_LC_PC / SAP_CA_SPT_TDR_PC / SAP_OC_SPT_ADMINISTRATION_PC |  |
| Treasury Specialist - Back Office | SAP_BR_TREASURY_SPECIALIST_BOE | Treasury Back Office | SAP_BR_TREASURY_SPECIALIST_BOE |  |
| Treasury Specialist - Front Office | SAP_BR_TREASURY_SPECIALIST_FOE | Treasury Front Office | SAP_BR_TREASURY_SPECIALIST_FOE |  |
| Treasury Specialist - Middle Office | SAP_BR_TREASURY_SPECIALIST_MOE | Treasury Middle Office | SAP_BR_TREASURY_SPECIALIST_MOE |  |
| Treasury Accountant | SAP_BR_TREASURY_ACCOUNTANT | Treasury Accounting | SAP_BR_TREASURY_ACCOUNTANT |  |
| Treasury Risk Manager | SAP_BR_TREASURY_RISK_MANAGER | Treasury Analytics | SAP_BR_TREASURY_RISK_MANAGER |  |

### Master Data, Organizational Data, and Other Data

The organizational structure and master data of your company have been created in your system during activation. The organizational structure reflects the structure of your company. The master data represents materials, customers, and vendors, for example, depending on the operational focus of your company.

Use your own master data or the following sample data to go through the test procedure.

| Data | Sample Value | Details | Comments |
| --- | --- | --- | --- |
| Company Code | 1010 |  |  |

Table 1: Master Data Script Reference

| MDS | Description |
| --- | --- |
| 22G | Create Business Partner for Treasury and Risk Management - MDS |

### Additional Manual Configuration

Before you can test this scope item, you must have completed the additional configuration steps that are described in the Set-Up Instructions for this scope item. These configuration steps are specific for your implementation and include mandatory settings that are not delivered by SAP and must be created by you. For more information, follow the link to the document:

[Link to Set-Up Instructions](https://help.sap.com/docs/SAP_S4HANA_BEST_PRACTICES/698b58449f48e1bd6f868927337ed29f)

### Preliminary Steps

#### Set up the Communication Connection

Purpose

You need to set up the connection between SAP S/4HANA Cloud Public Edition system and the Receiving system.

Procedure

Please follow the steps in the Set-up instructions of communication scenario SAP_COM_0442 to enable the connectivity in SAP S/4HANA Cloud Public Edition system. Correspondingly, SAP Business Suite or SAP S/4HANA Cloud Private Edition system (FI system) needs to be configured for inbound message by customers.

Result

You have setup the communication connection between SAP S/4HANA Cloud Public Edition system and Receiving system.

#### Maintain Mapping Rule in Receiving System

Purpose

In this step, you set up the field mapping for payment request generated in the receiving system if necessary.

By default, the system will look for the exactly same master data in the receiving system, however, master data like Business Partner, House Bank ID, Account ID, G/L Account, Payment Method in the sending system may not exist in the receiving system. You need to specify how the fields in the sender structure are mapped to those in the receiver structure.

Procedure

SAP delivers the Converting Data Between Sender and Receiver tool, which enables you to convert and map field content from the sender fields to the receiver fields. In this way, you can map organizational units, units of measurement, or yours and the customer-specific field content from one system to another. Please initialize and maintain the mapping rule for payment request according to customer requirements.

You can find this tool using transaction: SPRO via following IMG path: SAP Customizing Implementation Guide > SAP NetWeaver > Application Server > IDoc Interface / Application Link Enabling (ALE) > Modelling and Implementing Business Processes > Converting Data Between Sender and Receiver

|  |
| --- |
| Note The IMG path may vary in different systems, you can find it by searching for the IMG of IDoc Interface/Application Link Enabling (ALE). |

Then please perform the following steps in receiving system.

1. Create Rule: The rules are defined by IDOC segment name.
2. Maintain Rules: When you maintain rules, the conversion at the field level is determined according to defined rules.
3. Assign Rule to Message Type: The assignment defines when the rule is used. This can be sender, receiver, and Segment type Conversion rule for following Message Types.

PAYMENTREQUEST_CREATE

PAYMENTREQUEST_CANCEL

Result

All the fields mappings between the SAP S/4HANA Cloud Public Edition system and the receiving system are maintained.

## Overview Table

The scope item consists of several process steps in the table below.

|  |
| --- |
| Note If your system administrator has enabled spaces and pages on the SAP Fiori launchpad, the homepage will only contain the essential apps for performing the typical tasks of a business role.You can find all other (searchable) apps not included on the homepage using the search bar ([2434549](https://me.sap.com/notes/2434549)).If you want to personalize the homepage and include the hidden apps, navigate to your user profile and choose App Finder. |

| Process Step, Report or Item | Business Role | App/Transaction | Expected Results |
| --- | --- | --- | --- |
| [Process TRM Transactions and Post Flow to Generate Payment Request](#unique_10) [page ] 8 | Treasury Specialist - Back Office | Fix, Pay and Post Flows (TBB1)Fix and Pay Flows (TBB1_PAY) | Payment Requests are generated. |
| [Monitor IDoc in Sending System](#unique_11) [page ] 12 | Configuration Expert - Business Network Integration/Configuration Expert - Business Network Integration | Assign Recipients to Users (F2949)/Message Dashboard | You can monitor and analyze outbound messages in the Message Dashboard app. |
| [Monitor IDoc in Receiving System](#unique_12) [page ] 13 | n/a | WE02 | You can check the transferred inbound message in the receiving system. |
| [Check and Process Payment Request in Receiving System](#unique_13) [page ] 14 | n/a | F8BT | You can check the details of payment request in the receiving system. |
| [Set the Transaction Related Posting Flow for Reverse](#unique_14) [page ] 15 | Treasury Specialist - Back Office | Process Spots/Forwards - Collective Processing (TX06) | You can flag the posting flow or transactions for reverse in the SAP S/4HANA Cloud Public Edition system. |
| [Reverse Transaction](#unique_15) [page ] 16 | Treasury Accountant | Process Business Transactions (TPM10) | You can execute the reverse for the posting flows or transactions you marked as reverse in the SAP S/4HANA Cloud Public Edition system. |
| [Monitor IDoc in Sending System](#unique_16) [page ] 17 | Configuration Expert - Business Network Integration | Message Dashboard | You can check and reprocess outbound messages in the sending system |
| [Monitor IDoc in Receiving System](#unique_17) [page ] 18 | n/a | WE02 | You can check the transferred inbound message in the receiving system. |
| [Check and Process the Payment Request](#unique_18) [page ] 19 | n/a | F8BT | You can check the reversed payment request in the receiving system. |

## Test Procedures

This section describes test procedures for each process step that belongs to this scope item.

### Process TRM Transactions and Post Flow to Generate Payment Request

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you create the TRM financial transactions and trigger post flows in the SAP S/4HANA Cloud Public Edition system, then the system will generate the payment requests in the Receiving system automatically.

Procedure

Please refer the following test scripts for detailed steps about how to create and settle TRM financial transactions.

- 1WV: Debt and Investment Management
- 1X1: Foreign Currency Risk Management
- 1X3: Interest Rate Derivatives Management
- 2NZ: Bank Guarantee Management
- 2UN: Money Market Mutual Fund Management

To trigger the generation of payment requests in the receiving system, you can process the following steps in the above test scripts:

- Create TRM contract
- Settle the TRM contract
- Generate the payment request using the Fix, Pay and Post Flows (TBB1)/Fix and Pay Flows(TBB1_PAY) app

The test script will take Foreign Exchange forward transaction as an example

Option 1: Generate Payment Request with Fix, Pay and Post Flows (TBB1) App

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Treasury Specialist - Front Office. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori app | Open Create FX Spot/Forward (TX01). | The Spot/Forward Transaction Entry: Initial Screen displays. |  |
| 3 | Enter Selection Criteria | Enter selection criteria and choose Enter:Company Code: for example, 1010Product Type: 60ATransaction Type: For example, 102Partner: For example, 10537001 | The Spot/Forward Transaction Entry: Structure screen displays. |  |
| 4 | Enter Data | Enter the following data and choose Save.Rate: For example, EUR/USD 1.3Buy/Sell: For example, B BuyTraded Amt: For example, EUR 1MValue Date: <current date> | Transaction is saved and a transaction number is generated. |  |
| 5 | Log On | Log on to the SAP Fiori launchpad as Treasury Specialist - Back Office. |  |  |
| 6 | Access the SAP Fiori App | Open Process Spots/Forwards - Collective Processing (TX06). |  |  |
| 7 | Enter Selection Criteria | Enter the following data and choose Execute:Company Code: for example, 1010Transaction: <transaction number created in the previous step> |  |  |
| 8 | Settle the Transaction | Select the checkbox at the beginning of the transaction line and choose Settle. |  |  |
| 9 | Save | Choose Save. | The transaction is settled and saved. |  |
| 10 | Back | Go Back to the Home page. |  |  |
| 11 | Access the SAP Fiori app | Open Fix, Pay and Post Flows (TBB1). |  |  |
| 12 | Generate Payment Request | Enter the following data and choose Execute:Foreign Exchange: <select>Company code: for example, 1010Transaction: <transaction number with outflows you created the in previous steps>Up to and Including Due Date: <current date + 1 year>Test Run: <deselect>Pay Only: <select> | There will be a screen for Information Overview where you can find Payment log and Messages. |  |
| 13 | Check Payment log | Double click on Payment Log to find the details. | The Payment Logs screen displays and the key is blank in the Payment Log. |  |

|  |
| --- |
| Note Please note down the TRM financial transaction number which you created in the previous procedure. |

Option 2: Generate Payment Request with Fix and Pay Flows (TBB1_PAY) App

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Treasury Specialist - Front Office. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Create FX Spot/Forward (TX01). | The Spot/Forward Transaction Entry: Initial Screen displays. |  |
| 3 | Enter Selection Criteria | Enter selection criteria and choose Enter:Company Code: for example, 1010Product Type: 60ATransaction Type: For example, 102Partner: For example, 10537001 | The Spot/Forward Transaction Entry: Structure screen displays. |  |
| 4 | Enter Data | Enter the following data and choose SaveRate: For example, EUR/USD 1.3Buy/Sell: For example, B BuyTraded Amt: For example, EUR 1MValue Date: <current date> | Transaction is saved and a transaction number is generated. |  |
| 5 | Log On | Log on to the SAP Fiori launchpad as a Treasury Specialist - Back Office |  |  |
| 6 | Access the SAP Fiori App | Open Process Spots/Forwards - Collective Processing (TX06). |  |  |
| 7 | Enter Selection Criteria | Enter the following data and choose Execute:Company Code: for example, 1010Transaction: <transaction number created in the previous step> |  |  |
| 8 | Settle the Transaction | Select the checkbox at the beginning of the transaction line and choose Settle. |  |  |
| 9 | Save | Choose Save. | The transaction is settled and saved. |  |
| 10 | Back | Go Back to the Home page. |  |  |
| 11 | Access the SAP Fiori App | Open Fix and Pay Flows (TBB1_PAY). |  |  |
| 12 | Generate Payment Request | Enter the following data, and choose Execute:Foreign Exchange: <select>Company Code: for example, 1010Transaction: <transaction number with outflows you created the in previous steps>Up to and Including Due Date: <current date + 1 year>Test Run: <deselect> | There will be a screen for Information Overview where you can find Payment log and Messages. |  |
| 13 | Check Payment Log | Double click on Payment Log to find the details. | The Payment Logs screen displays and the key is blank in the Payment Log. |  |

|  |
| --- |
| Note Please note down the TRM financial transaction number which you created in the previous procedure. |

### Monitor IDoc in Sending System

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, after assigning recipients to your user, you can use the Message Dashboard to monitor messages from related interface, and analyze the causes of errors.

Procedure

Step 1: Assign Recipients to You User

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as a Configuration Expert - Business Network Integration | The SAP Fiori Launchpad is displayed. |  |
| 2 | Access the SAP Fiori app | Open Assign Recipients to Users (F2949). | The Assign Recipients to User screen is displayed. |  |
| 3 | Assign Recipients to User | On the Assign Recipients to User screen, on the left pane Users assigned to recipients, choose icon +, then enter the following data in the pop-up search bar and choose Add.Name/ID: for example, CONF_EXPERT_BUS_NET_INTThen enter the following data in the Assign Recipients dialog box, and choose Assign:Namespace: for example, /FINACRecipient Name: for example, FINAC_RECT_TRPR_OUTMessage Type: for example, Application Error and Technical ErrorOverview: <select>Technical User: <select> | The recipient is assigned to user. |  |

Step 2: Message Monitor through Message Dashboard

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as a Configuration Expert - Business Network Integration | The SAP Fiori Launchpad is displayed. |  |
| 2 | Access the SAP Fiori app | Open Message Dashboard (/AIFX/WDA_MSG_MONITOR). | The Interface Monitor screen is displayed. |  |
| 3 | Select Interface | On the Interface Monitor screen, under Calendar Monitor, enter the date information in the search bar, and choose SearchThen under Result List, you can find the line item AIF for Accounting -/FINAC namespace | The figures representing message in related status in the All Messages, Warnings, Errors, and Successfully Processed columns.There are messageTreasury Payment Request Creation - PAYRQ.CREA/00001 under the Namespace/ Interface AIF for Accounting -/FINAC. |  |
| 4 | Check Message Summary and Details | Double click on the aggregate number in order to investigate one kind of message. | The Monitoring and Error Handling screen is displayed. You can check the message detail and reprocess the message there. |  |

### Monitor IDoc in Receiving System

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you check the transferred inbound message in the receiving system. If the message is sent out successfully and the relevant configurations are maintained correctly, you should find the inbound message carrying payment request detail information in the message list.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the Receiving system via SAP Logon with user with necessary authorization. | You can log on to the system. |  |
| 2 | Access the IDoc list | Enter the transaction code WE02 in the Command field and choose Enter. | The IDoc List screen displays. |  |
| 3 | Enter Selection Criteria and Execute | On the IDoc List screen, enter the following data and choose Execute:Created On: <The message creation date in the previous step> | The IDoc List is displayed. |  |
| 4 | Display the Message Details | Double click on the IDocs/ Selected IDocs /Inbound IDocs/PAYMENTREQUEST_CREATE | You can find all the IDocs sending from S/4HANA Cloud system. |  |
| 5 | Check the Message Details | Double Click on the IDoc. Go to the Status Records node to investigate the the detailed information of the IDoc status. | Make sure thePAYMENTREQUEST_CREATE IDoc is successfully procced by the receiving system . |  |

### Check and Process Payment Request in Receiving System

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you check the payment request generated in the receiving system, and ensure it is correctly generated in the receiving system. If the mapping rule is maintained, check if the details are correctly derived.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the Receiving System via SAP Logon via user with necessary authorization. |  |  |
| 2 | Access the IDoc list | Enter transaction code F8BT in the command field, and choose Enter. | The Display Payment Requests screen displays. |  |
| 3 | Enter Selection Criteria and Execute | On the Display Payment Requests screen, enter the following data and choose Execute:Company Code: <the company code mapping in the receiving system, for example,1010>Paying Company Code : <the company code mapping in the receiving system, for example,1010>Selection of Payment Request: <Select Open>On the Administration Data tab, enter the following data:Origin: TR-TMCreated On: <the current date>Note For different receiving systems, the UI may vary. Please input necessary search criteria and make sure you can find the right one. | You can see the payment request generated in the receiving system |  |
| 4 | Display the payment request details | Double click the payment request key number.Note It is not possible for sending system to knows about the payment request key number in receiving system when sending the IDoc to receiving system, please find out whether there is any newly created payment request after you execute above test procedures. | The details of payment request are displayed. |  |

### Set the Transaction Related Posting Flow for Reverse

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you can flag the posting flow or flag the transaction for reverse in the SAP S/4HANA Cloud Public Edition system if you want to reverse the posting.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Treasury Specialist - Back Office |  |  |
| 2 | Access App | Open Process Spots/Forwards - Collective Processing (TX06).Note For different transaction types, you need to use different Collective Processing app. | The Forex: Collective Processing screen displays. |  |
| 3 | Search the Financial Instrument | Enter the following search criteria and choose Execute:Company Code: 1010Transaction: <enter the transaction number you created in the previous step> |  |  |
| 4 | Select the Transaction | Select the transaction, and choose Reverse. | The Reverse Activity: Initial screen displays, and the Activity already has posted flows displays. |  |
| 5 | Reverse | Choose Enter. | The Reverse Activity: Payment Details screen displays. |  |
| 6 | Enter Reverse Reason | Select following Reversal Reason, and choose Save.Reversal Reason: 01 | The financial transaction is saved. |  |

### Reverse Transaction

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you can execute the reverse the transaction in the SAP S/4HANA Cloud Public Edition system after you have flagged the transaction for reverse.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Treasury Accountant |  |  |
| 2 | Access App | Open Process Business Transactions (TPM10). | The Fix, Post or Reverse Transactions screen displays. |  |
| 3 | Search the Financial Instrument | Enter the following search criteria and choose Execute:OTC Transactions: <select>Company Code: 1010OTC Transactions:Transaction: <enter the transaction number you settled in previous step>TRM Reversal Reason: 01Test Run: <deselect> | The Update Run: Post/Reverse Business Transactions screen displays.The transactions you want to reverse is listed, and all the posted flows are displayed. |  |
| 4 | Execute Reverse | Select the flows for reverse and choose Execute. | You will get a successful update message. |  |

### Monitor IDoc in Sending System

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, after assigning recipients to your user, you can use the Message Dashboard to monitor messages from related interface, analyze the causes of errors, and restart outbound messages.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as a Configuration Expert - Business Network Integration | The SAP Fiori Launchpad is displayed. |  |
| 2 | Access the SAP Fiori app | Open Message Dashboard. | The Interface Monitor screen is displayed. |  |
| 3 | Select Interface Monitor | On the Interface Monitor screen, under Calendar Monitor, enter the date information in the search bar, and choose Search. | The figures representing message in related status in the All Messages, Warnings, Errors, and Successfully Processed columns.There are messageTreasury Payment Request Cancellation - PAYRQ.CANC/00001 under the Namespace/ Interface AIF for Accounting -/FINAC. |  |
| 4 | Check Message Summary and Details | Double click on the aggregate number in order to investigate one kind of message. | The Monitoring and Error Handling screen is displayed. You can check the message detail and reprocess the message if necessary. |  |

### Monitor IDoc in Receiving System

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you check the transferred inbound message in the receiving system. If the message is sent out successfully and the relevant configurations are maintained correctly, you should find the inbound message carrying payment request detail information in the message list.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the Receiving system via SAP Logon with user with necessary authorization. |  |  |
| 2 | Access the IDoc list | Enter the transaction code WE02 in the Command field and choose Enter. | The IDoc List screen displays. |  |
| 3 | Enter Selection Criteria and Execute | On the IDoc List screen, enter the following data and choose Execute:Created On: <The message creation date in the previous step> | The IDoc List is displayed. |  |
| 4 | Display the Message Details | Double click on the IDocs/Selected IDocs/Inbound IDocs/PAYMENTREQUEST_CANCEL | You can find all the IDocs sending from the SAP S/4HANA Cloud Public Edition system. |  |
| 5 | Check In Bound IDoc Detail | Double click on the IDoc you want to check. | The IDoc Display: 000000000000XXXX screen displays. |  |
| 6 | Check the payment request ID for cancel | Go to the node under IDoc display/IDoc 0000000000XXXXXX/Data records/E1PAYMENTREQUEST_CANCEL | Go to the Content of Selected segment.You can find the REQUESTID. Please note down the Value of REQUESTID which you need to use later. |  |

### Check and Process the Payment Request

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you can reverse the posting in the SAP S/4HANA system if you have flagged the posting for reverse.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the Receiving System via sap log on with user has necessary authorization. | System cloud logon. |  |
| 2 | Access the IDoc list | Enter transaction code F8BT in the command field, and choose Enter. | The Display Payment Requests screen displays. |  |
| 3 | Enter Selection Criteria and Execute | On the Display Payment Requests screen, enter the following data and choose Execute:Company Code: <the company code mapping in the receiving system,for example,1010Selection of Payment Request:Open : <Deselected>Cleared: <Selected>Origin: TR-TMKey Number: <the REQUESTID you noted down in previous step> |  |  |
| 4 | Display the payment request details | Double click the payment request key number | The details of payment request are displayed.Check the details of payment request.The Revrse column is marked with X.The Reversal Reason column is marked with 01 |  |

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
- related-to :: [[05-treasury-and-cash-management/test-script-treasury-workstation-accounting-integration-33e-ae-897]]
- related-to :: [[05-treasury-and-cash-management/test-script-treasury-workstation-cash-integration-34p-ae-sap-s-4hana-c]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/3NA_S4CLD2608_BPD_EN_XX.docx` — full document · extracted with `mammoth` · 34,657 chars in the whole document
