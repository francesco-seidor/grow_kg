---
id: 08-sales-order-management/test-script-digital-payments-sales-1z1-ae-sap-s-4hana-cloud-public-edi
title: "Test Script: Digital Payments – Sales (1Z1_AE), SAP S/4HANA Cloud Public Edition (1Z1_S4CLD2608_BPD_EN_AE)"
description: "SAP S/4HANA Cloud Public Edition 2608 (UAE) test script for Digital Payments – Sales (1Z1): credit card authorization, cancellation, reauthorization and billing checks."
cluster: 08-sales-order-management
tags: [kb/sales-order-management, topic/digital-payments]
aliases: [1Z1_S4CLD2608_BPD_EN_AE]
keywords: [Digital Payments and Card Payments in Sales, digital payments, credit card authorization, payment card registration, one-time payment card, authorization cancellation, payment card reauthorization, sales order rejection, sales order creation, billing document check]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/1Z1_S4CLD2608_BPD_EN_AE.docx]
confidence: high
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-790
topic: 08-sales-order-management/digital-payments
language: EN
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Test Script: Digital Payments – Sales (1Z1_AE), SAP S/4HANA Cloud Public Edition (1Z1_S4CLD2608_BPD_EN_AE)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/1Z1_S4CLD2608_BPD_EN_AE.docx`, extracted with `mammoth`. Grouped under **Digital Payments and Card Payments in Sales** in Sales Order Management. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

| <!-- image omitted: unnamed --> | Test ScriptSAP S/4HANA Cloud Public Edition - 19-06-26 |
| --- | --- |
|  | Digital Payments – Sales (1Z1_AE) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Table of Contents

[1 Purpose 3](#_Toc232848603)

[2 Prerequisites 4](#_Toc232848604)

[2.1 System Access 4](#_Toc232848605)

[2.2 Roles 4](#_Toc232848606)

[2.3 Master Data, Organizational Data, and Other Data 4](#_Toc232848607)

[2.4 Business Conditions 6](#_Toc232848608)

[2.5 Preliminary Steps 7](#_Toc232848609)

[2.5.1 Create Condition Records (Optional) 7](#_Toc232848610)

[3 Overview Table 8](#_Toc232848611)

[4 Test Procedures 10](#_Toc232848612)

[4.1 Using Credit Card Data Maintained in Business Partner in Sales Document 10](#_Toc232848613)

[4.1.1 Add & Register Credit Card Data in Business Partner 10](#_Toc232848614)

[4.1.2 Create Sales Documents 13](#_Toc232848615)

[4.1.3 Check Credit Card Data in Sales Documents 16](#_Toc232848616)

[4.1.4 Cancellation of Credit Card Authorization and Reauthorizations (Optional) 17](#_Toc232848617)

[4.1.5 Check Payment Card Status (Optional) 18](#_Toc232848618)

[4.1.6 Reauthorize Sales Documents with Payment Card 19](#_Toc232848619)

[4.1.7 Proceed with All Succeeding Steps Until Billing Document Created 20](#_Toc232848620)

[4.1.8 Check Credit Card Data in Billing Document 21](#_Toc232848621)

[4.2 Using One-time Credit Card Data in Sales Document 22](#_Toc232848622)

[4.2.1 Create Sales Documents 22](#_Toc232848623)

[4.2.2 Check Credit Card Data in Sales Documents 25](#_Toc232848624)

[4.2.3 Cancellation of Credit Card Authorization and Reauthorizations (Optional) 26](#_Toc232848625)

[4.2.4 Check Payment Card Status (Optional) 27](#_Toc232848626)

[4.2.5 Release Sales Documents with Payment Card 28](#_Toc232848627)

[4.2.6 Proceed with All Succeeding Steps Until Billing Document Created 30](#_Toc232848628)

[4.2.7 Check Credit Card Data in Billing Document 30](#_Toc232848629)

[4.3 Reject Sales Order and Check Deleted Credit Card Authorization 31](#_Toc232848630)

[4.3.1 Create Sales Documents 31](#_Toc232848631)

[4.3.2 Reject Sales Order and Cancelation of Credit Card Authorization 34](#_Toc232848632)

[4.3.3 Check Deleted Credit Card Authorization 35](#_Toc232848633)

[5 Appendix 37](#_Toc232848634)

[5.1 Process Integration 37](#_Toc232848635)

[5.1.1 Succeeding Processes 37](#_Toc232848636)

## Purpose

Overview

SAP digital payments is a payment capability for payment service providers and SAP components, solutions, or applications that process incoming credit card payments.

Payment card information available in the business partner master data can be used when creating the sales order or new payment card data (one-time payment card) can be used in the sales order. When you save the sales order, the authorization of the payment card is executed through the payment provider service.

The credit card authorization can be cancelled by deleting the authorized amount in the sales order. Then a re-authorization can be done after changing the order quantity.

Furthermore, the credit card authorization can be cancelled by rejecting the sales order which has an amount authorized for credit card payment.

This document provides a detailed procedure for testing this scope item after solution activation, reflecting the predefined scope of the solution. Each process step, report, or item is covered in its own section, providing the system interactions (test steps) in a table view. Steps that are not in scope of the process but are needed for testing are marked accordingly. Project-specific steps must be added.

|  |
| --- |
| Note Values in this test script (decimal notation, date formats, and so on) are presented in U.S. standard notation. If your test system is set up to use a different notation, enter values as appropriate. |

## Prerequisites

Cloud: Integration to the payment Hub has to be set up. Refer to the corresponding Instruction Guide

### System Access

| System | Details |
| --- | --- |
| System | Accessible via SAP Fiori launchpad. Your system administrator provides you with the URL to access the various apps assigned to your role. |

### Roles

Create business roles using the following business role templates delivered by SAP and assign them to your individual test users.

Alternatively, if available, you can use the following spaces delivered by SAP. You create a space with pages containing predefined essential apps and assign it to the business role. You then assign this business role to your individual users.

For more information, refer to How to Create a Business Role from a Template in the [product assistance](https://help.sap.com/docs/SAP_S4HANA_CLOUD/53e36b5493804bcdb3f6f14de8b487dd/ec310a8b669a45ca898dc4dd91d97de2.html) for SAP S/4HANA Cloud Public Edition.

| Name (Role Template) | ID (Role Template) | Name (Launchpad Space) | ID (Launchpad Space) |
| --- | --- | --- | --- |
| Master Data Specialist - Business Partner Data | SAP_BR_BUPA_MASTER_SPECIALIST | Master Data - Business Partners / Business Partner Governance / Business Partner Governance / Business Partner Governance | SAP_BR_BUPA_MASTER_SPECIALIST / SAP_CA_SPT_MDG_BP_GOV_PC / SAP_CMD_SPT_BP_GOV_PC / SAP_CA_SPT_MDG_BP_WFUSR_PC |
| Internal Sales Representative | SAP_BR_INTERNAL_SALES_REP | Internal Sales / Customer Returns / Billing | SAP_BR_INTERNAL_SALES_REP / SAP_SD_SPT_RETURNS_INT_SALES_PC / SAP_SD_SPT_BILLING_INT_SALES_PC |
| Billing Clerk | SAP_BR_BILLING_CLERK | Billing | SAP_BR_BILLING_CLERK |

### Master Data, Organizational Data, and Other Data

The organizational structure and master data of your company have been created in your system during activation. The organizational structure reflects the structure of your company. The master data represents materials, customers, and suppliers, for example, depending on the operational focus of your company.

|  |
| --- |
| Caution Update Behavior of Predelivered Demo DataIn non-productive environments (such as starter systems, sandbox systems, or partner demo systems), SAP initially deploys demo data for your selected scope. You can use this data to test and evaluate business processes.In a customer system, you can receive new or updated demo data after initial activation with further scope enhancements, provided the existing demo data wasn't changed in an incompatible way. If activation errors occur due to incompatible changes in demo data, you're responsible for resolving them. If you don't resolve the errors within a specific time frame, SAP reserves the right to deactivate demo data in your systems. In this case, you can continue by creating your own demo data. Alternatively, you can request that your systems be reprovisioned if you want to work with predelivered demo data again.In partner systems, you can use the demo data deployed with the initial activation. No additional demo data will be deployed in the system with scope enhancements. You can only create additional demo data manually. |

Use your own master data or the following sample data to go through the test procedure.

| Master / Org. Data | Value | Master / Org. Data Details | Comments |
| --- | --- | --- | --- |
| Material | TG11 | Trading Good for Reg. Trading (MRP planning)no Serial no.; no batch | See sections Business Conditions and Preliminary Steps. |
| Material | TG12 | Trad.Good 12,Reorder Point,Reg.Trad.no Serial no.; no batch | See sections Business Conditions and Preliminary Steps. |
| Material | TG20 | Trading Good for Reg. Trading (reorder point planning) | See sections Business Conditions and Preliminary Steps. |
| Material | CM-FL-V00 | Forklift | Only use if you have activated the scope item Make-to-Order Production with Variant Configuration (1YT). |
| Material | SM0001 | Service Material 01 |  |
| Material | NS0002 | Non-Stock Material 02 (No MRP planning)no Serial no.; no batch |  |
| Sold-to party | 3310000133100005 | Domestic UAE Customer 1Domestic UAE Customer 5 | Payment Card Data in Business Partner.One-time payment card customer. |
| Ship-to party | 3310000133100005 | Domestic UAE Customer 1Domestic UAE Customer 5 |  |
| Payer | 3310000133100005 | Domestic UAE Customer 1Customer domestic 05 |  |
| Plant | 3310 | Plant 1 AE |  |
| Storage Location | 331A |  |  |
| Shipping Point | 3310 |  |  |
| Sales Organization | 3310 |  |  |
| Distribution Channel | 10 |  |  |
| Division | 00 |  |  |

|  |
| --- |
| Note Additional Master Data (Default Values)You can test the scope item with other SAP Best Practices default values that have the same characteristics.Check your SAP system to find out which other material master data exists.Using Your Own Master DataYou can also use customized values for any material or organizational data for which you have created master data. |

Table 1: Master Data Script Reference

| MDS | Description |
| --- | --- |
| BNF | Create Product Master of type "Trading Good" - MDS |
| BND | Create Customer Master - MDS |
| 2YX | Create Customer-Material Info Record - MDS |

### Business Conditions

Before this scope item can be tested, the following business conditions must be met.

| Scope Item ID | Business Condition |
| --- | --- |
| BD9 - Sell from Stock | After order creation, Complete the following steps and final the Billing document created |
| BD3 - Sales Processing using Third-Party with Shipping Notification | After order creation, Complete the following steps and final the Billing document created |
| BKZ - Sales Order Processing with Invoice List and Collective Billing | After order creation, Complete the following steps and final the Billing document created |
| BDK - Sales Processing Using Third-Party Without Shipping Notification | After order creation, Complete the following steps and final the Billing document created |

### Preliminary Steps

#### Create Condition Records (Optional)

Purpose

In case you have finetuned the access sequence of SAP pre-shipped condition types, the relative condition records should be created accordingly.

You can find general information on how to create your own master data in the following: [Master Data Scripts (MDS)](https://help.sap.com/docs/s4hana-best-practices/s4cld2608-master-data)

Table 2: Master Data Script Reference

| Master Data ID | Description |
| --- | --- |
| BEW | Create Free Goods Condition - MDS |

## Overview Table

This scope item consists of several process steps provided in the table below.

|  |
| --- |
| Note If your system administrator has enabled spaces and pages on the SAP Fiori launchpad, the homepage will only contain the essential apps for performing the typical tasks of a business role.You can find all other (searchable) apps not included on the homepage using the search bar ([2434549](https://me.sap.com/notes/2434549)).If you want to personalize the homepage and include the hidden apps, navigate to your user profile and choose App Finder. |

| Process Step | Business Role | Transaction/App | Expected Results |
| --- | --- | --- | --- |
| Using Credit Card Data Maintained in Business Partner in Sales Document |  |  |  |
| [Add & Register Credit Card Data in Business Partner](#unique_9) [page ] 10 | Master Data Specialist - Business Partner Data | Manage Customer Master Data (F0850A) |  |
| [Create Sales Documents](#unique_10) [page ] 13 | Internal Sales Representative | Manage Sales Orders (F1873) |  |
| [Check Credit Card Data in Sales Documents](#unique_11) [page ] 16 | Internal Sales Representative | Manage Sales Orders (F1873) |  |
| [Cancellation of Credit Card Authorization and Reauthorizations (Optional)](#unique_12) [page ] 17 | Internal Sales Representative | Manage Sales Orders (F1873) |  |
| [Check Payment Card Status (Optional)](#unique_13) [page ] 18 | Internal Sales Representative | Resolve Payment Card Issues - Reauthorizations (F4793) |  |
| [Reauthorize Sales Documents with Payment Card](#unique_14) [page ] 19 | Internal Sales Representative | Resolve Payment Card Issues - Schedule Job (F2758) |  |
| [Proceed with All Succeeding Steps Until Billing Document Created](#unique_15) [page ] 20 |  |  |  |
| [Check Credit Card Data in Billing Document](#unique_16) [page ] 21 | Billing Clerk | Manage Billing Documents (F0797) |  |
| Using One-time Credit Card Data in Sales Document |  |  |  |
| [Create Sales Documents](#unique_17) [page ] 22 | Internal Sales Representative | Manage Sales Orders (F1873) |  |
| [Check Credit Card Data in Sales Documents](#unique_18) [page ] 25 | Internal Sales Representative | Manage Sales Orders (F1873) |  |
| [Cancellation of Credit Card Authorization and Reauthorizations (Optional)](#unique_19) [page ] 26 | Internal Sales Representative | Manage Sales Orders (F1873) |  |
| [Check Payment Card Status (Optional)](#unique_20) [page ] 27 | Internal Sales Representative | Resolve Payment Card Issues - Reauthorizations (F4793) |  |
| [Release Sales Documents with Payment Card](#unique_21) [page ] 28 | Internal Sales Representative | Resolve Payment Card Issues - Schedule Job (F2758) |  |
| [Proceed with All Succeeding Steps Until Billing Document Created](#unique_22) [page ] 30 |  |  |  |
| [Check Credit Card Data in Billing Document](#unique_23) [page ] 30 | Billing Clerk | Manage Billing Documents (F0797) |  |
| Reject Sales Order and Check Deleted Credit Card Authorization |  |  |  |
| [Create Sales Documents](#unique_24) [page ] 31 | Internal Sales Representative | Manage Sales Orders (F1873) |  |
| [Reject Sales Order and Cancelation of Credit Card Authorization](#unique_25) [page ] 34 | Internal Sales Representative | Manage Sales Orders (F1873) |  |
| [Check Deleted Credit Card Authorization](#unique_26) [page ] 35 | Internal Sales Representative | Manage Sales Orders (F1873) |  |

## Test Procedures

This section describes test procedures for each process step that belongs to this scope item.

### Using Credit Card Data Maintained in Business Partner in Sales Document

#### Add & Register Credit Card Data in Business Partner

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to add and register credit card data in business partner.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Master Data Specialist - Business Partner Data. |  |  |
| 2 | Access the App | Open Manage Customer Master Data (F0850A). | The Customer Master search screen displays. |  |
| 3 | Create New Person | Choose Create and Person.A dialog box displays. Choose OK.Last Name: Domestic CustomerAE 99Grouping: Internal Numbering for Standard UseBP Role: FLCU01Currency: AEDSales Organization: 3310Distribution Channel: 10Division: 00Company Code: 3310Reconciliation Account: 12100000 |  |  |
| 4 | Add Role for Financial | Choose Roles on the navigation bar. And choose Create.Make the following entry:Business Partner Role: FLCU00 |  |  |
| 5 | Add Address Information | Choose Addres > Standard Address on the navigation bar.Make the following entry:Street: <Street>Country: AERegion: <Region>Postal Code: 33803Language: ENTelephone: <Telphone>E-mail: info@33100001.comCity: <City> |  |  |
| 6 | Input the Currency and Tax | Choose Sales Areas on the navigation bar.Choose Sales Org. (>).The system will navigate to another screen, and make the following entries as below,Customer Group: 01Delivery Plant: 3310Shipping Conditions: StandardIncoterms: EXWIncoterms Location 1: <Incoterms Location 1>Payment Terms: 0004Payment Guarantee Procedure: 0002Account assignment group: Domestic RevenuesCountry: AETax Classification for TTX1 : 1And choose Apply. |  |  |
| 7 | Check the Company Code data | Choose Company Codes on the navigation bar.Choose Company Code. (>).Make the following entry:Payment Terms: 0004Sort Key: 009And choose Apply. |  |  |
| 8 | Navigate to the Payment Card | Choose Payment Cards on the navigation bar. | The Payment Cards screen displays. |  |
| 9 | Register New Payment Card | Choose Create.A dialog box displays for entering the basic details of card which should be added to customer master.make the following entries:Card ID: XXXXXAnd choose Register. |  |  |
| 10 | Input the Detail Information for the Payment Card | URL opens UI to enter credit card data, make the following entries:Credit Card Type: XXXXXCard Number: XXXXXXXXXXXXXName on Card: XXXXXXXXXXXXXValid to: XX YYYYCard Security Code: XXXXThen Submit. | Payment hub verifies the validity of the card details provided via 3rd party payment service providers (PSP).After verification, in case data is provided correctly, Card details are added to the Customer Master. | Tokenization of Payment Card via 3rd party payment service provider.Digital payments provide a tokenized reference to cardSample credit card:American Express: 378282246310005Visa: 4012888888881881 |
| 11 | Verify the Payment Card | Verify the details added in the Payment Card. | Details displayed should be correct and as per the details entered by user.If this is the first valid card added, then Default flag should be set for this card.If there are more than one card, then user should be able to set the Default flag for any one of the cards available. |  |
| 12 | Save | Choose Save Customer. |  |  |

|  |
| --- |
| Note Follow from the step 8–12, you can assign the credit card data to an existing business partner in Customer Master APP. |

#### Create Sales Documents

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to create sales documents.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Internal Sales Representative. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Sales Orders (F1873). | The Create Sales Order: Initial screen displays. | From the menu, choose catalog Sales-Sales Order Processing > Manage Sales Orders. |
| 3 | Navigate to Create Sales Order Screen | On the Manage Sales Orders screen, choose Create, and choose Create Sales Orders - VA01. |  |  |
| 4 | Enter the Order type OR (Standard Order) | On the Create Sales Order: Initial Screen, make the following entries:Order Type: ORSales Organization: 3310Distribution Channel: 10Division: 00 |  |  |
| 5 | Enter Order Details | If you would like to use listing and exclusion, continue with test step Enter listed / excluded Material Numbers.If you would like to use customer material record information, continue with test step Enter Customer Material Number.On the Create Sales Order: Overview screen, make the following entries:Sold to party: for example, 33100001 (Created in the step [Add & Register Credit Card Data in Business Partner](#unique_9) [page ] 10)Ship to party: for example, 33100001Customer Reference: <Customer Reference>Material Number: TG11Quantity: <Quantity>If you would like to use item proposal, continue with test step Copy Item Proposal to Sales Order. |  | Cust. Reference:<Enter a customer purchase order number as reference>PO number: <Enter a customer purchase order number as reference>Order reason: for example, Excellent priceQuantity: for example, 10 PC |
| 6 | Electronic Payments | On the Create Standard Order: Overview screen, choose Menu > Goto > Header > Electronic Payments. In the Card Number / Transaction ID field, select F4 help and select credit card. | The payment card information will be taken over from the business partner master data.The status has been returned as green if the authorization check is passed. | Tokenization of Payment Card via the third party Payment service.Digital payments get a tokenized reference to card.The test credit card accounts have amount limitation of 1000 AED. |
| 7 | Save Document | Choose Save Document. Make a note of the sales order number: __________.Note If you’ve installed the scope item Free Goods Processing in your system and you use material TG11 and customer 33100001, the following warning may appear: Minimum quantity 1.000 PC of free goods has not been reached. To skip this warning, choose Enter.Note You can now display the created order on the Customer Cockpit screen. In the Number of Last Documents field, select the number of last documents you would like to display. Choose Refresh. The latest order is the one that has just been created.Note The printout of the order confirmation is executed automatically and immediately (see settings in SAP GUI transaction VV13 for output type BA00 and defaults in your user settings in transaction SU3); however, only in the case when the sales order is not blocked (see next section Credit Management Review blocked Sales Orders). | The order is saved and the order confirmation is printed out. |  |

Printing Form - Output Management

Cloud and On-premise

|  |
| --- |
| Note If you implement the note 2298826 - Switch for enabling NAST condition based output for On Premise for activating the Output Management function, please process the output procedure steps in Printing From- Output Management. |

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Internal Sales Representative. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Sales Orders (F1873). | The Manage Sales Orders screen displays. |  |
| 3 | Search for Sales Order | Enter search term(s) in filter bar and choose Go:For example, enter sales order number in the Sales Order field. | Sales order displays in result list. |  |
| 4 | Navigate to Sales Order Screen | Choose > on the right side of the Sales Order item and navigate to Display Standard Orders xxx: Overview screen. | The Display Standard Order xxx: Overview displays. |  |
| 5 | Check Output Condition | On the Display Standard Order xxx: Overview screen, choose Extras > Output > Header > Edit. |  |  |
| 6 | Display Print Preview | On the Display Standard Order xxx: Output screen, select the line already created for the print output and choose Display Document. | Preview for PDF document displays. |  |

|  |
| --- |
| Note It can also be navigated to a factsheet screen in Manage Sales Orders app: On the Manage Sales Orders screen, enter search terms in filter bar and choose Go. In search result, choose your sales order number and choose Display Fact sheet. |

#### Check Credit Card Data in Sales Documents

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

Navigate to the tile in the Fiori launchpad navigate to the Electronic Payments tab.

During saving of the sales documents an authorization is executed. The status can be checked in the Electronic Payments tab.

Procedure - Cloud Edition

Example: Sell from Stock (BD9)

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Internal Sales Representative. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Sales Orders (F1873),Enter search term(s) in filter bar and choose Go: for example, enter sales order number XXX in the Sales Order field. | Sales Order XXX displays in result list. |  |
| 3 | Navigate to the Sales Order | Choose sales order number XXX and choose Display Sales Orders - VA03 (VA03). | The Display Sales Order XXX: Overview screen displays. |  |
| 4 | Navigate to the Electronic Payments Tab | On the Display Sales Order XXX: Overview screen, choose Goto > Header > Electronic Payments | The Payment card information displays.Credit Card details are stored:Card typeCard token (not displayed)Card Number / Transaction IDPayer NameValid-toPayment card is charged via payment hub, Not every card number is valid. |  |

#### Cancellation of Credit Card Authorization and Reauthorizations (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

SAP digital payments add-on offers a service for the cancellation of credit card authorizations, which is now called in the sales order.

If the authorization in sales order is canceled, the service is called so that the corresponding authorizations of the payment service provider are canceled as well.

The benefit for the end user and retailer is that the canceled amount will not block the credit card.

The employee can check the authorization history within the order to see the current status of the authorizations and the response from the SAP digital payments add-on.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Internal Sales Representative. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Sales Orders (F1873),Enter search term(s) in filter bar and choose Go: for example, enter sales order number XXX in the Sales Order field. | Sales Order XXX displays in result list. |  |
| 3 | Navigate to the Sales Order | Choose sales order number XXX and choose Change Sales order. | The Change Sales Order XXX: Overview screen displays. |  |
| 4 | Change Sales Order’s Quantity and Reauthorizations | Change the Order Quantity: <Quantity>. | Change the sales order quantity (For example, from 10 PC to 8 PC) |  |
| 5 | Navigate to the Payment Cards Tab | On the Change Sales Order XXX: Overview screen, choose More > Goto > Header > Electronic Payments . | The payment card information displays. |  |
| 6 | Delete Authorized Credit Card Amount in Sales Document | Choose the line with authorized amount and choose the delete row button. | The authorization amount will be cancelled in the payment Hub when saving order. |  |
| 7 | Save Document and Reauthorizations | Choose Back and Save. | After the sales order is saved, the sales order will be authorized with the new amount.The cancellation of credit card and reauthorizations log have been stored after saving order.It can be displayed by choosing Authorization Log. |  |

#### Check Payment Card Status (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to check your sales order’s payment card status.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Internal Sales Representative. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Resolve Payment Card Issues - Reauthorizations (F4793) | The Resolve Payment Card Issues – Reauthoirzations screen displays. |  |
| 3 | Change View Settings | Choose Settings. |  |  |
| 4 | Choose Payment Card Status | Choose Payment Card Status and Choose OK. |  |  |
| 5 | Navigate to the Sales Order | Enter sales order number XXX in the Sales Order field and Choose Go. | Sales Order XXX is displayed in the screen. |  |

|  |
| --- |
| Note In case of a credit block due to authorization issues, you can also navigate to the credit case. From there you can execute a credit recheck (which triggers a reauthorizations) or alternatively, if you do not want to cover the sales order by credit card anymore, you can also perform a credit release as described. For detail, please follow step Management of Blocked Orders from scope item Basic Credit Management (BD6) to reauthorize sales order. |

#### Reauthorize Sales Documents with Payment Card

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to release sales documents with payment card.

Procedure

Option A: You can use Resolve Payment Card Issues - Schedule Job to release sales document with payment card.

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Internal Sales Representative. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Resolve Payment Card Issues - Schedule Job (F2758). | The Application Jobs screen displays. |  |
| 3 | Create A New Job | Choose Create. | The New Job screen displays. |  |
| 4 | Enter Job Data | On the New Jobs screen, make the following entries as below:Job Template: Resolve Payment Card IssuesJob Name: Resolve Payment Card IssuesStart Immediately: selectedSD document: XXX. (Enter your sales order which created in step [Create Sales Documents](#unique_10) [page ] 13)Choose Schedule. | The job is created and starts immediately. |  |
| 5 | Review Job Status | The Application Job screen displays after the job completes. Navigate to the Job detail. | The Job detail displays. When the status is Finished, the sales order is released. |  |

Option B: You can use Resolve Payment Card Issues – Reauthoirzations to release sales document with payment card.

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Internal Sales Representative. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Resolve Payment Card Issues - Reauthorizations (F4793) | The Resolve Payment Card Issues – Reauthoirzations screen displays. |  |
| 3 | Navigate to the Sales Order | Enter sales order number XXX in the Sales Order field and Choose Go. | Sales Order XXX is displayed in the screen. |  |
| 4 | Reauthoirze the Sales Order | Choose Sales Order XXX and choose Reauthoirze. | Reauthorizations has been triggered for order XXX.. |  |

#### Proceed with All Succeeding Steps Until Billing Document Created

Proceed with following steps: Create Delivery, Execute Picking, Post Goods Issue and Create Billing Document from scope item Sell from Stock (BD9).

|  |
| --- |
| Note If the outbound delivery is blocked by payment card, please follow step: from scope item Basic Credit Management (BD6) to execute a recheck on the outbound delivery. You can enter the delivery note number into field Document Number to Search your credit case. From the credit case, besides a recheck, there is also the option to perform a credit release if needed. Check Credit Card Data in Billing Document. |

#### Check Credit Card Data in Billing Document

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to check credit card data in billing documents.

Procedure

After the creation of the billing document check the payment card data in the billing document:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as a Billing Clerk. |  |  |
| 2 | Access the App | Open Manage Billing Documents (F0797), enter search term(s) in filter bar and choose Go:for example, enter Billing Document number in field Billing Document. |  |  |
| 3 | Navigate to the Billing Document | Choose Billing Document Number XXX and choose Display Billing Document. | The Display billing document xxx: Overview screen displays. |  |
| 4 | Navigate to the payment Cards Tab | On the Display billing document xxx: Overview screen, choose Menu > Goto > Header > Electronic Payments | The Payment card information displays.Credit Card details are stored:Card typeCard token (not be displayed)Mask numberCard holderValid-to |  |

### Using One-time Credit Card Data in Sales Document

Purpose

This section shows the use of one-time payment cards in the sales documents and the authorization via the payment hub.

#### Create Sales Documents

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to create sales documents.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Internal Sales Representative. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Sales Orders (F1873). | The Manage Sales Orders screen displays. | From the menu, choose catalog Sales-Sales Order Processing > Manage Sales Orders. |
| 3 | Navigate to Create Sales Order Screen | On the Manage Sales Orders screen, choose Create, and choose Create Sales Orders - VA01. |  |  |
| 4 | Enter the Order type OR (Standard Order) | On the Create Sales Order: Initial Screen, make the following entries:Order Type: ORSales Organization: 3310Distribution Channel: 10Division: 00 |  |  |
| 5 | Enter Order Details | If you would like to use listing & exclusion, continue with test step Enter listed / excluded Material Numbers.If you would like to use customer material record information, continue with test step Enter Customer Material Number.On the Create Sales Order: Overview screen, make the following entries:Sold to party: for example, 33100005Ship to party: for example, 33100005Cust. Reference: 33100005Material Number: TG11Quantity: QuantityIf you would like to use item proposal, continue with test step Copy Item Proposal to Sales Order. |  | Cust. Reference: Enter a customer purchase order number as referenceOrder reason: for example, Excellent priceQuantity: for example, 1 PC |
| 6 | Assign Electronic Payments | On the Create Standard Order: Overview screen, choose Goto > Header > Electronic Payments. Choose Assign Payment Card.URL opens UI to enter credit card data, make the following entries:Card Type:Card Number:Name on Card:Valid to:Then choose Submit. | The credit card data has been submitted to the Digital payment system for registration.The status has been returned as green if the authorization check is passed | Tokenization of Payment Card via the third-party Payment service.Digital payments get a tokenized reference to card.Sample credit card:American Express: 378282246310005Visa: 4012888888881881The test credit card accounts have amount limitation of 1000 AED. |
| 7 | Assign Payment Guarantee Proc. | Choose Billing DocumentMake the following entries:Paymt Guarant. Proc. 000002 |  |  |
| 8 | Save Document | Choose Save Document. Make a note of the sales order number: __________.Note If you have installed the scope item Free Goods Processing in your system and you use material TG11 and customer 33100001, the following warning may appear: Minimum quantity 1.000 PC of free goods has not been reached. To skip this warning, choose Enter.Note You can now display the created order on the Customer Cockpit screen. In the Number of Last Documents field, select the number of last documents you would like to display. Choose Refresh. The latest order is the one that has just been created.Note The printout of the order confirmation is executed automatically and immediately (see settings in SAP GUI transaction VV13 for output type BA00 and defaults in your user settings in transaction SU3); however, only in the case when the sales order is not blocked (see next section Credit Management Review blocked Sales Orders). | The order is saved and the order confirmation is printed out. |  |

Printing Form - Output Management

Cloud and On-premise

|  |
| --- |
| Note If you implement the note 2298826 - Switch for enabling NAST condition based output for On Premise for activate the Output Management function, please process the output procedure steps in Printing From- Output Management. |

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Internal Sales Representative. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Sales Orders (F1873). | The Manage Sales Orders screen displays. |  |
| 3 | Search for Sales Order | Enter search term(s) in filter bar and choose Go:for example: enter sales order number in field Sales Order. | Sales order displays in result list. |  |
| 4 | Navigate to Sales Order Screen | Choose > on the right side of the Sales Order item and navigate to Display Standard Orders xxx: Overview screen. | The Display Standard Order xxx: Overview displays. |  |
| 5 | Check Output Condition | On the Display Standard Order xxx: Overview screen, choose Menu > Extras > Output > Header > Edit. |  |  |
| 6 | Display Print Preview | On the Display Standard Order xxx: Output screen, select the line already created for the print output and choose Display PDF Document. | Preview for PDF document displays. |  |

|  |
| --- |
| Note It can also be navigated to a factsheet screen in Manage Sales Orders app: On the Manage Sales Orders screen, enter search terms in filter bar and choose Go. In search result, choose your sales order number and choose Display Fact sheet. |

#### Check Credit Card Data in Sales Documents

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

Navigate to the tile in the Fiori Launchpad navigate to the Electronic Payments tab.

During saving of the sales documents an authorization is executed. The status can be checked on the Electronic Payments tab.

Procedure - Cloud Edition

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Internal Sales Representative. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Sales Orders (F1873).Enter search term(s) in filter bar and choose Go: for example, enter sales order number XXX in the Sales Order field. | Sales order number XXX displays in result list. |  |
| 3 | Navigate to the Sales Order | Choose sales order number XXX and choose Display Sales Orders - VA03 (VA03). | The Display Sales Order xxx: Overview screen displays. |  |
| 4 | Navigate to the Payment Cards Tab | On the Display Sales Order xxx: Overview screen, choose Menu > Goto > Header > Electronic Payments. | The Payment card information displays.Credit Card details are stored:Card typeCard token (not be displayed)Card Number / Transaction IDPayer NameValid-to | The Payment card is debited via the payment hub. Not every card number is valid. |

#### Cancellation of Credit Card Authorization and Reauthorizations (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

SAP digital payments add-on offers a service for the cancellation of credit card authorizations, which is now called in the sales order.

If the authorization in sales order is canceled, the service is called so that the corresponding authorizations of the payment service provider are canceled as well.

The benefit for the end user and retailer is that the canceled amount will not block the credit card.

The employee can check the authorization history within the order to see the current status of the authorizations and the response from the SAP digital payments add-on.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Internal Sales Representative. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Sales Orders (F1873),Enter search term(s) in filter bar and choose Go: for example, enter sales order number XXX in the Sales Order field. | Sales Order XXX displays in result list. |  |
| 3 | Navigate to the Sales Order | Choose sales order number XXX and choose Change Sales order. | The Change Sales Order XXX: Overview screen displays. |  |
| 4 | Change Sales Order’s Quantity and Reauthorizations | Change the Order Quantity: <Quantity>. | Change the sales order quantity (For example, from 10 PC to 8 PC) |  |
| 5 | Navigate to the Electronic Payments Tab | On the Change Sales Order XXX: Overview screen, choose More > Goto > Header > Electronic Payments . | The payment card information displays. |  |
| 6 | Delete Authorized Credit Card Amount in Sales Document | Choose the line with authorized amount and choose the delete row button. | The authorization amount will be cancelled in the payment Hub when saving order. |  |
| 7 | Save Document and Reauthorizations | Choose Back and Save. | After the sales order is saved, the sales order will be authorized with the new amount.The cancellation of credit card and reauthorizations log have been storedafter saving order.It can be displayed by choosing Authorization Log. |  |

#### Check Payment Card Status (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to check your sales order’s payment card status.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Internal Sales Representative. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Resolve Payment Card Issues - Reauthorizations (F4793) | The Resolve Payment Card Issues – Reauthoirzations screen displays. |  |
| 3 | Change View Settings | Choose Settings. |  |  |
| 4 | Choose Payment Card Status | Choose Payment Card Status and Choose OK. |  |  |
| 5 | Navigate to the Sales Order | Enter sales order number XXX in the Sales Order field and Choose Go. | Sales Order XXX is displayed in the screen. |  |

|  |
| --- |
| Note In case of a credit block due to authorization issues, you can also navigate to the credit case. From there you can execute a credit recheck (which triggers a reauthorizations) or alternatively, if you do not want to cover the sales order by credit card anymore, you can also perform a credit release as described. For detail, please follow step Management of Blocked Orders from scope item Basic Credit Management (BD6) to reauthorize sales order. |

#### Release Sales Documents with Payment Card

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to release sales documents with payment card.

Procedure

Option A: You can use Resolve Payment Card Issues - Schedule Job to release sales document with payment card.

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Internal Sales Representative. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Resolve Payment Card Issues - Schedule Job (F2758). | The Application Jobs screen displays. |  |
| 3 | Create A New Job | Choose Create. | The New Job screen displays. |  |
| 4 | Enter Job Data | On the New Jobs screen, make the following entries as below:Job Template: Resolve Payment Card IssuesJob Name: Resolve Payment Card IssuesStart Immediately: selectedSD document: XXX. (Enter your sales order which created in step [Create Sales Documents](#unique_17) [page ] 22)Choose Schedule. | The job is created and starts immediately. |  |
| 5 | Review Job Status | The Application Job screen displays after the job completes. Navigate to the Job detail. | The Job detail displays. When the status is Finished, the sales order is released. |  |

Option B: You can use Resolve Payment Card Issues – Reauthoirzations to release sales document with payment card.

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Internal Sales Representative. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Resolve Payment Card Issues - Reauthorizations (F4793) | The Resolve Payment Card Issues – Reauthoirzations screen displays. |  |
| 3 | Navigate to the Sales Order | Enter sales order number XXX in the Sales Order field and Choose Go. | Sales Order XXX is displayed in the screen. |  |
| 4 | Reauthoirze the Sales Order | Choose Sales Order XXX and choose Reauthoirze. | Reauthorizations has been triggered for order XXX.. |  |

#### Proceed with All Succeeding Steps Until Billing Document Created

Proceed with following steps: Create Delivery, Execute Picking, Post Goods Issue and Create Billing Document from scope item Sell from Stock (BD9).

|  |
| --- |
| Note If the outbound delivery is blocked by payment card, please follow step: from scope item Basic Credit Management (BD6) to execute a recheck on the outbound delivery. You can enter the delivery note number into field Document Number to Search your credit case. From the credit case, besides a recheck, there is also the option to perform a credit release if needed. Check Credit Card Data in Billing Document. |

#### Check Credit Card Data in Billing Document

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to check credit card data in billing documents.

Procedure

After the creation of the billing document check the Electronic Payments data in the billing document:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Billing Clerk . |  |  |
| 2 | Access the App | Open Manage Billing Documents (F0797), Enter search term(s) in filter bar and choose Go: for example, enter billing document number in the Billing Document field. |  |  |
| 3 | Navigate to the Billing Document | Choose billing document number XXX and choose Display Billing Document. | The Display billing document xxx: Overview screen displays. |  |
| 4 | Navigate to the Electronic Payments Tab | On the Display billing document xxx: Overview screen, choose Menu > Goto > Header > Electronic Payments | The Payment card information displays.Credit Card details are stored:Card typeCard token (not be displayed)Mask numberCard holderValid-to |  |

### Reject Sales Order and Check Deleted Credit Card Authorization

Purpose

This process step shows you how to reject the sales order.

The credit card authorization will be cancelled and the corresponding authorizations of the payment service provider are canceled as well.

#### Create Sales Documents

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to create sales documents.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Internal Sales Representative. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Sales Orders (F1873). | The Manage Sales Orders screen displays. | From the menu, choose catalog Sales-Sales Order Processing > Manage Sales Orders . |
| 3 | Navigate to Create Sales Order Screen | On the Manage Sales Orders screen, choose Create, and choose Create Sales Orders - VA01. |  |  |
| 4 | Enter the Order type OR (Standard Order) | On the Create Sales Order: Initial Screen, make the following entries:Order Type: ORSales Organization: 3310Distribution Channel: 10Division: 00 |  |  |
| 5 | Enter Order Details | If you would like to use listing & exclusion, continue with test step Enter listed / excluded Material Numbers.If you would like to use customer material record information, continue with test step Enter Customer Material Number.On the Create Sales Order: Overview screen, make the following entries:Sold to party: for example, 33100005Ship to party: for example, 33100005Cust. Reference: 33100005Material Number: TG11Quantity: QuantityIf you would like to use item proposal, continue with test step Copy Item Proposal to Sales Order. |  | Cust. Reference: <Enter a customer purchase order number as reference>Order reason: for example, Excellent priceQuantity: for example, 1 PC |
| 6 | Assign Electronic Payments | On the Create Standard Order: Overview screen, choose more > Goto > Header > Electronic Payments . Choose Assign Payment Card.URL opens UI to enter credit card data, make the following entries:Credit Card Type:Card Number:Name on Card:Valid to:CVC:Then Submit. | The credit card data has been submitted to the Digital payment system for registration.The status has been returned as green if the authorization check is passed | Tokenization of Payment Card via 3rd party Payment service.Digital payments get a tokenized reference to card.Sample credit card:American Express: 378282246310005Visa: 4012888888881881The test credit card accounts have amount limitation of 1000 AED. |
| 7 | Assign Payment Guarantee Proc. | Choose Billing DocumentMake the following entries:Paymt Guarant. Proc. 000002 |  |  |
| 8 | Save Document | Choose Save Document. Make a note of the sales order number: __________.Note If you have installed the scope item Free Goods Processing in your system and you use material TG11 and customer 33100001, the following warning may appear: Minimum quantity 1.000 PC of free goods has not been reached. To skip this warning, choose Enter.Note You can now display the created order on the Customer Cockpit screen. In the Number of Last Documents field, select the number of last documents you would like to display. Choose Refresh. The latest order is the one that has just been created.Note The printout of the order confirmation is executed automatically and immediately (see settings in SAP GUI transaction VV13 for output type BA00 and defaults in your user settings in transaction SU3); however, only in the case when the sales order is not blocked (see next section Credit Management Review blocked Sales Orders). | The order is saved and the order confirmation is printed out. |  |

Printing Form - Output Management

|  |
| --- |
| Note If you implement the note 2298826 - Switch for enabling NAST condition based output for On Premise for activate the Output Management function, please process the output procedure steps in Printing From- Output Management. |

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Internal Sales Representative. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Sales Orders (F1873). | The Manage Sales Orders screen displays. |  |
| 3 | Search for Sales Order | Enter search term(s) in filter bar and choose Go: for example: enter sales order number in the Sales Order field. | Sales order displays in result list. |  |
| 4 | Navigate to Sales Order Screen | Choose > on the right side of the Sales Order item and navigate to Display Standard Orders xxx: Overview screen. | The Display Standard Order xxx: Overview displays. |  |
| 5 | Check Output Condition | On the Display Standard Order xxx: Overview screen, choose Menu > Extra > Output > Header > Edit . |  |  |
| 6 | Display Print Preview | On the Display Standard Order xxx: Output screen, select the line already created for the print output and choose Display PDF Document. | Preview for PDF document displays. |  |

|  |
| --- |
| Note It can also be navigated to a factsheet screen in the Manage Sales Orders app: On the Manage Sales Orders screen, enter search terms in filter bar and choose Go. In search result, choose your sales order number and choose Display Fact sheet. |

#### Reject Sales Order and Cancelation of Credit Card Authorization

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to reject the sales document and cancel the Electronic Payments authorization.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Internal Sales Representative. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Sales Orders (F1873),Enter search term(s) in filter bar and choose Go: for example, enter sales order number XXX in field Sales Order. | Sales Order XXX displays in result list. |  |
| 3 | Navigate to the Sales Order | Select sales order number XXX and choose Change Sales Order. | The Change Sales Order xxx: Overview screen displays. |  |
| 4 | Reject the Sales Document | Choose Reject All Items. | The Reject All Items dialog dialog box displays. |  |
| 5 | Select Reason | Select Reason for Rejection.Reason for Rejection: Due to Invoice ErrorAnd choose Reject All Items. | The sales order updates with a reason for the rejection. And payment authorization has been cancelled . |  |

#### Check Deleted Credit Card Authorization

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to check the Electronic Payments authorization log.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Internal Sales Representative. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Sales Orders (F1873),Enter search term(s) in filter bar and choose Go: for example, enter sales order number XXX in the Sales Order field. | Sales Order XXX displays in result list. |  |
| 3 | Navigate to the Sales Order | Select sales order number XXX and choose Display Sales Orders - VA03 (VA03). | The Display Sales Order xxx: Overview screen displays. |  |
| 4 | Navigate to the Electronic Payments Tab | On the Display Sales Order XXX: Overview screen, choose Menu > Goto > Header > Electronic Payments. | The Payment card information dis­ plays.Credit Card details are stored:Card typeCard token (not displayed)Card Number / Transaction IDPayer NameValid-to |  |
| 5 | Check Authorization Log | Choose Authorization Log. | The cancellation of credit card log has been stored in the authorization log. |  |

## Appendix

### Process Integration

The process to be tested in this test script is part of a chain of integrated processes.

#### Succeeding Processes

After completing the activities in this test script, you can continue testing the following business processes:

| Process | Business Condition |
| --- | --- |
| 1S2 - Digital Payments | Check the credit card data in the corresponding accounting documents. |

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
- related-to :: [[08-sales-order-management/external-digital-payments-2lz-ae-test-script-833]]
- related-to :: [[08-sales-order-management/test-script-digital-payments-foundation-53v-1062]]
- related-to :: [[08-sales-order-management/test-script-sap-s-4hana-cloud-public-edition-digital-payments-1s2-ae-7]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/1Z1_S4CLD2608_BPD_EN_AE.docx` — full document · extracted with `mammoth` · 60,779 chars in the whole document
