---
id: 08-sales-order-management/self-billing-4h2-ae-test-script-sap-s-4hana-cloud-public-edition-1028
title: Self-Billing (4H2_AE) Test Script - SAP S/4HANA Cloud Public Edition (4H2_S4CLD2608_BPD_EN_AE)
description: "SAP test script for scope item 4H2_AE Self-Billing (UAE): prerequisites, tolerance and sender setup, API transmission, simulation and execution of self-billing."
cluster: 08-sales-order-management
tags: [kb/sales-order-management, topic/invoice-lists-collective-billing-self-billing]
aliases: [4H2_S4CLD2608_BPD_EN_AE]
keywords: ["Invoice Lists, Collective Billing and Self-Billing", self-billing, self-billing with invoice creation, self-billing cockpit, scope item testing, tolerance groups, sold-to party parameters, sender parameters, self-billing transmission, action codes]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/4H2_S4CLD2608_BPD_EN_AE.docx]
confidence: low
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-1028
topic: 08-sales-order-management/invoice-lists-collective-billing-self-billing
language: EN
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Self-Billing (4H2_AE) Test Script - SAP S/4HANA Cloud Public Edition (4H2_S4CLD2608_BPD_EN_AE)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/4H2_S4CLD2608_BPD_EN_AE.docx`, extracted with `mammoth`. Grouped under **Invoice Lists, Collective Billing and Self-Billing** in Sales Order Management. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

|  |  |
| --- | --- |
| Self-Billing (4H2_AE)Purpose PUBLIC 1<!-- image omitted: unnamed --> | Test ScriptSAP S/4HANA Cloud Public Edition - 28-08-26 |
|  | Self-Billing (4H2_AE) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Table of Contents

[1 Purpose 3](#_Toc239510216)

[2 Prerequisites 4](#_Toc239510217)

[2.1 System Access 4](#_Toc239510218)

[2.2 Roles 4](#_Toc239510219)

[2.3 Master Data, Organizational Data, and Other Data 4](#_Toc239510220)

[2.4 Additional Manual Configuration 6](#_Toc239510221)

[2.5 Business Conditions 6](#_Toc239510222)

[2.6 Preliminary Steps 6](#_Toc239510223)

[2.6.1 Create Delivery at SAP S/4HANA Cloud Public Edition 6](#_Toc239510224)

[2.6.2 Manage Tolerance Group 7](#_Toc239510225)

[2.6.3 Define Sold-to Party Parameters 8](#_Toc239510226)

[2.6.4 Define Sender Parameters 9](#_Toc239510227)

[2.6.5 Format Transmission 9](#_Toc239510228)

[2.6.6 Manage Master Data, Organizational Data, and Other Data 10](#_Toc239510229)

[3 Overview Table 12](#_Toc239510230)

[4 Test Procedures 13](#_Toc239510231)

[4.1 Processing Introduction 13](#_Toc239510232)

[4.1.1 Processing Flows 13](#_Toc239510233)

[4.1.2 Action Codes for Controlling the Processing Flow 14](#_Toc239510234)

[4.2 Check Auto Processing Result 14](#_Toc239510235)

[4.3 Check Simulation Result 15](#_Toc239510236)

[4.4 Execute Self-Billing Document 16](#_Toc239510237)

[4.5 Check Execution Result (Optional) 17](#_Toc239510238)

[5 Appendix 19](#_Toc239510239)

[5.1 Process Integration 19](#_Toc239510240)

[5.2 Succeeding Processes 19](#_Toc239510241)

[5.3 Transmission Example 19](#_Toc239510242)

[5.4 Send Transmission with Postman 21](#_Toc239510243)

[5.5 Resources 22](#_Toc239510244)

## Purpose

Overview

In many sell-from-stock processes (for example, the Sell from Stock (BD9) and Sales Scheduling Agreements (3NR) scope items), the financial settlement is handled with a self-billing process with the customer. Instead of issuing an invoice to the customer, the supplier receives self-billing information from the customer, containing the reference document number, received quantity, and value to be credited to the supplier (as well as other information).

This scope item focuses on the sales-related supplier's side of the self-billing processes. The supplier validates the self-billing message received from the customer and simulates results. If there are differences, credit and debit memos are created respectively to settle the account. If the differences exceed the defined tolerances, credit and debit memos are created to show the open amounts. The existing invoices and accounting documents are updated with the transferred self-billing reference number. This ensures that the financial settlement can be automated once payment advice from the customer is received.

As legal requirements differ across regions, SAP provides two main self-billing applications:

- Self-Billing with Automatic Posting (SBWAP): used in countries where billing documents are automatically created at goods issue.
- Self-Billing with Invoice Creation (SBINV): used where suppliers must generate an invoice identical to the buyer’s self-billing document.

In Self-Billing with Invoice Creation, an initial invoice does not exist. Instead, it is simulated and created.

To use the processes covered by this scope item, activate the scope item and integrate your SAP S/4HANA Cloud Public Edition system with SAP Self-Billing Cockpit. SAP Self-Billing Cockpit is available as a licensed product through the SAP Store. You can find it by searching for SAP Self-Billing Cockpit in the store. You can find additional information about the product and its features on the SAP Help Portal on the [SAP Self-Billing Cockpit](https://help.sap.com/docs/CP_SELF_BILLING) product page.

This document provides a detailed procedure for testing this scope item after solution activation, reflecting the predefined scope of the solution. Each process step, report, or item is covered in its own section, providing the system interactions (test steps) in a table view. Steps that are not in scope of the process but are needed for testing are marked accordingly. Project-specific steps must be added.

|  |
| --- |
| Note Values in this test script (decimal notation, date formats, and so on) are presented in U.S. standard notation. If your test system is set up to use a different notation, enter values as appropriate. |

## Prerequisites

This section summarizes all the prerequisites for conducting the test in terms of systems, users, master data, organizational data, other test data and business conditions.

### System Access

Table 1:

| System | Details |
| --- | --- |
| System | Accessible via SAP Fiori Launchpad. Your system administrator provides you with the URL to access various apps assigned to your role. |

### Roles

Full authorization for self-billing process needs to be provided to the user applied. This is mentioned in 4H2 Scope Item setup instruction [Create Business User for SAP Self-Billing Cockpit](https://help.sap.com/docs/btp/sap-business-technology-platform/create-users?locale=en-US).

Note:

For integrated process with SAP S/4HANA Cloud Public Edition:

Create business roles using the following business role templates delivered by SAP and assign them to your individual test users.

Alternatively, if available, you can use the following spaces delivered by SAP. You create a space with pages containing predefined essential apps and assign it to the business role. You then assign this business role to your individual users.

For more information, refer to How to Create a Business Role from a Template in the [product assistance](https://help.sap.com/docs/SAP_S4HANA_CLOUD/53e36b5493804bcdb3f6f14de8b487dd/ec310a8b669a45ca898dc4dd91d97de2.html) for SAP S/4HANA Cloud Public Edition.

For information about business roles, refer to Assigning Business Roles to a User in the [Administration Guide to Implementation of SAP S/4HANA with SAP Best Practices](https://help.sap.com/docs/SAP_S4HANA_ON-PREMISE/4cef93946a0b48ec89533b3c34443b85/17d958a88d244ee293aed687f9bfe37f.html?version=2025).

Table 2:

| Name (Role Template) | ID (Role Template) | Name (Launchpad Space) | ID (Launchpad Space) | System |
| --- | --- | --- | --- | --- |
| Billing Clerk | SAP_BR_BILLING_CLERK | Billing | SAP_BR_BILLING_CLERK | SAP S/4HANA Cloud Public Edition |

### Master Data, Organizational Data, and Other Data

The master data and organizational data needed is based on these data set up at SAP S/4HANA Cloud Public Edition system.

Regarding SAP S/4HANA Cloud Public Edition, the organizational structure and master data of your company have been created in your system during activation. The organizational structure reflects the structure of your company. The master data represents products, customers, and vendors, for example, depending on the operational focus of your company.

|  |
| --- |
| Caution Update Behavior of Predelivered Demo DataIn non-productive environments (such as starter systems, sandbox systems, or partner demo systems), SAP initially deploys demo data for your selected scope. You can use this data to test and evaluate business processes.In a customer system, you can receive new or updated demo data after initial activation with further scope enhancements, provided the existing demo data wasn't changed in an incompatible way. If activation errors occur due to incompatible changes in demo data, you're responsible for resolving them. If you don't resolve the errors within a specific time frame, SAP reserves the right to deactivate demo data in your systems. In this case, you can continue by creating your own demo data. Alternatively, you can request that your systems be reprovisioned if you want to work with predelivered demo data again.In partner systems, you can use the demo data deployed with the initial activation. No additional demo data will be deployed in the system with scope enhancements. You can only create additional demo data manually. |

Use your own master data or the following sample data to go through the test procedure.

| Data | Sample Value | Details | Comments |
| --- | --- | --- | --- |
| Product | TG11 | Trading Good for Reg. Trading (MRP planning) No serial number; no batch | See sections [Business Conditions](#unique_6) [page ] 6 and [Preliminary Steps](#unique_7) [page ] 6. |
| Product | TG12 | Trad.Good 12,Reorder Point,Reg.Trad. No serial number, no batch | See sections [Business Conditions](#unique_6) [page ] 6 and [Preliminary Steps](#unique_7) [page ] 6. |
| Sold-to Party | 33100003 | Domestic UAE Customer 3 |  |
| Ship-to Party | 33100003 | Domestic UAE Customer 3 |  |
| Payer | 33100003 | Customer domestic 03 |  |
| Plant | 3310 | Plant 1 AE |  |
| Storage Location | 331A | Std. storage 1 |  |
| Shipping Point | 3310 |  |  |
| Sales Organization | 3310 |  |  |
| Distribution Channel | 10 |  |  |
| Division | 00 | Product Division 00 |  |

### Additional Manual Configuration

Before you can test this scope item, you must have completed the additional configuration steps that are described in the Set-Up Instructions for this scope item. These configuration steps are specific for your implementation and include mandatory settings that are not delivered by SAP and must be created by you. For more information, follow the link to the document:

[Link to Set-Up Instructions](https://help.sap.com/docs/SAP_S4HANA_BEST_PRACTICES/37f44029280f91e8a0782108f349698f)

For more information, refer to the [Administration Guide to Implementation of SAP S/4HANA with SAP Best Practices](https://help.sap.com/docs/SAP_S4HANA_ON-PREMISE/4cef93946a0b48ec89533b3c34443b85/5a3861e6e0a64295b8b436f1466cd4b7.html?version=2025).

### Business Conditions

Before you can test this scope item, test script of the proceding scope item 3NR needs to be completed.

| Scope Item | Business Condition |
| --- | --- |
| 3NR - Sales Scheduling Agreements | You have completed the steps described in the 3NR- Sales Scheduling Agreements test script. Additionally, ensure that there are valid delivery, billing created. |

### Preliminary Steps

#### Create Delivery at SAP S/4HANA Cloud Public Edition

Purpose

This process shows you how to create delivery at SAP S/4HANA Cloud Public Edition to run through this scope item.

Below procedure takes scope item 3NR as a prerequisite process. Delivery should be created following 3NR - Sales Scheduling Agreements test script, but do not create billing document.

Procedure

Before create scheduling agreement, product price needs to be maintained for scope item 3NR at SAP S/4HANA Cloud Public Edition system by using Fiori App Set Material Prices.

| Sold-to Party | Product | Condition Value of PPR0 | Currency |
| --- | --- | --- | --- |
| 33100003 | TG11 | 17.55 | AED |
| 33100003 | TG12 | 17.55 | AED |

Two scheduling agreements are needed for testing scenario of this scope item. Item category need to be set to LZSN.

Expected result examples are listed as below:

| Sold-to Party | Scheduling Agreement | Product | Customer Material | Unit of Measure | Currency | Item Category |
| --- | --- | --- | --- | --- | --- | --- |
| 33100003 | 30000001 | TG11 | RM129 | PC | AED | LZSN |
| 33100001 | 30000002 | TG12 | RM128 | PC | AED | LZSN |

Two deliveries are needed for testing scenario of this scope item. Deliveries are created under each scheduling agreement.

Expected result examples are listed as below:

| Sold-to Party | Scheduling Agreement | Delivery | Product | Customer Material | Billed Quantity | Unit of Measure | Billing Net Value | Currency | Item Category |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 33100003 | 30000001 | 80000001 | TG11 | RM129 | 6 | PC | 105.3 | AED | LZSN |
| 33100001 | 30000002 | 80000002 | TG12 | RM128 | 8 | PC | 140.4 | AED | LZSN |

Example delivery 80000001 has one line item which can be created by Scheduling Agreement with one line item of product TG11. The test result regarding to Billing Net Value might be different from the value shown in above table which is based on PPR0 condition value delivered by SAP.

#### Manage Tolerance Group

Purpose

This process shows you how to maintain the tolerance groups.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to SAP Self-Billing Cockpit Launchpad. | SAP Self-Billing Cockpit Launchpad is displayed. |  |
| 2 | Access the App | Open Manage Tolerance Groups. |  |  |
| 3 | Create Tolerance Group | Choose Create. Make the following entries:Tolerance Group: TESTDescription: Absolute 20Sales Organization: 3310Choose Create. | Tolerance group TEST created. |  |
| 4 | Create Absolute Limit | Choose tab Absolute Limits. Choose Create and make the following entries:Currency:AEDLower Limit per Product:20Lower Limit per Product-Check Limit: YesChoose Create. | Tolerance group TEST saved with absolute limit maintained.The tolerance group will check the lower limit per product item of 20 AED. |  |

#### Define Sold-to Party Parameters

Purpose

This process shows you how to define sold-to party parameters.

Procedure

Table 3:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to SAP Self-Billing Cockpit Launchpad | SAP Self-Billing Cockpit launchpad is displayed. |  |
| 2 | Access the App | Open Define Sold-to Party Parameters. |  |  |
| 3 | Define Sold-to Party Parameters | Choose Create.Switch on Configuration - Invoice Creation.Make the following entries:Sold to Party: 33100003Tolerance Group: TEST <Created in previous step>Choose Create. | Sold-to Party 33100003 related parameters are defined. | It is a mandatoy maintenance step. |

#### Define Sender Parameters

Purpose

This process shows you how to define sender parameters.

Procedure

Table 4:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to SAP Self-Billing Cockpit Launchpad | SAP Self-Billing Cockpit launchpad displays. |  |
| 2 | Access the App | Open Define Sender Parameters. |  |  |
| 3 | Define Sender Parameters | Choose Create. Make the following entries:Sender ID: AMOTORSender: Alpha MotorChoose Create. | Sender Alpha Motor parameters are defined.Note Sender ID is corresponding to the field <senderId> received from transmission.Sender will display on the App Manage Self-Billing - Automatic Posting |  |

|  |
| --- |
| Note Section [Define Sender Parameters](#unique_12) [page ] 9, [Define Sold-to Party Parameters](#unique_11) [page ] 8 and [Define Sender Parameters](#unique_12) [page ] 9 needs to be carried out only once for the same sold-to party and sender. |

#### Format Transmission

Purpose

This process shows you how to format and simulate sending the transmission for testing.

Procedure

The self-billing process is triggered by receiving the transimission of self-billing documents from the customer. SOAP API Self-Billing Document - Receive is provided to send transmissions and published in the SAP API Hub with detail introduction and implementation information. You can use general SOAP API testing tool like Postman, SoapUI etc to call the API and send test transmission.

The below example is formating the transmission based on the three preceeding deliveries created in previous step ( [Create Delivery at SAP S/4HANA Cloud Public Edition](#unique_9) [page ] 6 ).

The designed scenario and corresponding key received fields are as below.

| External Billing Document | Delivery | Product | Customer Material | Delivered Quantity | UoM | Billing Net Value | Currency | Transmitted Quantity | Transmitted UoM ISO | Transmitted Net Value | Transmitted Currency ISO | Expected Processing and Simulation Result |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 70000001 | 80000001 | TG11 | RM129 | 6 | PC | 105.3 | AED | 6 | PCE | 105.3 | AED | No difference and this item will be fully billed. |
|  | 80000002 | TG12 | RM128 | 8 | PC | 140.4 | AED | 7 | PCE | 122.85 | AED | No difference and this item will be partially billed. |

|  |
| --- |
| Note The example transmission is provided in [Transmission Example](#unique_14) [page ] 19 with all mandatory fields maintained based on scenarios listed above.To test receiving transmission for testing, take Postman to call the API as the example, detail steps are listed in [Send Transmission with Postman](#unique_15) [page ] 21 .If the Billing Net Value is different from the value shown in above table, please adjust Transmitted Net Value accordingly in order to fulfil the value differences shown in Expected Processing and Simulation Result column.Sold-to party determination needs to be maintained for scope item 3NR in the SAP S/4HANA Cloud Public Edition system by using the SAP Fiori app Assign Sold-to Parties (F3894). Please refer to the set-up instructions for scope item 3NR in Convert External to Internal Partner Number. Enter details as follows:Supplier: 33300001Partner Description: 3310Unloading Point: <empty>Sold-to Party: 33100003 |

#### Manage Master Data, Organizational Data, and Other Data

Purpose

The required master data and organizational data must be uploaded and maintained using the relevant object from Manage Master Data apps in the SAP Self-Billing Cockpit. This app is used to create, display and manage master data according to your company’s organizational structure and business requirements.

In SAP S/4HANA Public Cloud Edition, the organizational structure reflects your company setup, and master data represents business objects such as sold-to-party, products, company code, and Plant. Depending on the test scope, use your own master data maintained in the system through the appropriate Manage Master Data apps.

Use your own master data or the sample data in the chapter [Master Data, Organizational Data, and Other Data](#unique_5) [page ] 4 to go through the test procedure.

Procedure

1. Open the Manage Master Data app.
2. Select the required master data object, such as Sold-To Party or Sales Organization.
3. Choose Download Template and save the template to your local system.
4. Enter the required master data in the template according to the field requirements.
5. Choose Upload File and select the completed template.
6. Select a destination if required for the selected object.
7. Choose the required operation:
    - Add Records to create new entries.
    - Delete Records to remove existing entries.
8. Choose Save to start the upload.
9. The system validates the file for issues such as missing fields, incorrect formats, duplicate records, and invalid values.
10. If validation is successful, the system processes the records. If some records fail backend validation, the upload may be partially successful.
11. Choose View Application Logs to check processing results, failed records, and error messages.
12. Choose Download File to review the current master data and verify the uploaded records.

## Overview Table

This scope item consists of several process steps provided in the following table.

Table 5:

| Process Step | Transaction/App | Expected Results |
| --- | --- | --- |
| [Check Auto Processing Result](#unique_18) [page ] 14 | Manage Self-Billing – Invoice Creation | Self-billing document has been auto processed either to simulation status in orange or stopped in red with error |
| [Check Simulation Result](#unique_19) [page ] 15 | Manage Self-Billing - Automatic PostingManage Self-Billing – Invoice Creation | Simulation result presented. |
| [Execute Self-Billing Document](#unique_20) [page ] 16 | Manage Self-Billing – Invoice Creation | Execution completed and document processing completed. |
| [Check Execution Result (Optional)](#unique_21) [page ] 17 | Manage Self-Billing – Invoice Creation | Execution result presented. |

|  |
| --- |
| Note The error correction provided in this test script is regarding the editable field Transmitted ISO UoM. There are other editable fields for error handling. |

## Test Procedures

This section describes procedures for each process step that belongs to this scope item.

### Processing Introduction

#### Processing Flows

The system can interpret received transmissions in various ways before determining the processing logic. How it interprets them depends on the header action codes and item action codes carried in the respective transmission.

For details about possible combinations of action codes, see [Action Codes for Controlling the Processing Flow](#unique_24) [page ] 14.

The following processing flows exist for self-billing with invoice creation:

|  |  |
| --- | --- |
| Initial Invoice Creation | This type of processing deals with initial invoice creation. After receiving self-billing documents from the buyer, the system determines the corresponding delivery document for reference, and compares the received data with the reference data.Based on the comparison results, the system proceeds in one of the following ways:It executes self-billing to trigger the creation of invoices (billing type CIXS) for billing items where there is no difference.It executes self-billing to create a clearing line, in addition to an invoice, for billing items where the transmitted net value differs from the reference net value.It executes self-billing to create a clearing line and an open line, in addition to an invoice, if the difference exceeds the predefined tolerance limits.Note Clearing lines and open lines are used to keep track of the value difference and open value, respectively. Created only in SAP Self-Billing Cockpit, clearing lines and open lines are not posted to financial accounting. |
| Credit or Debit Memos for Quantity Corrections | This type of processing deals with quantity corrections (such as damaged goods during the transport) claimed by the buyer, by referring to a transaction that has already been processed and settled. Therefore, the buyer sends a credit or debit memo for quantity corrections with reference to one or more existing invoices.During the process, the system compares the claimed net value change against the internal net value change, both of which are calculated based on input such as quantity changes of the settled transaction.If they match, the system executes self-billing to trigger the creation of a credit memo (billing type CIXG) or debit memo (billing type CIXL) exactly as the buyer has prepared it.If they don't match, the system creates a credit or debit memo and a clearing line, as well as an open line if the difference exceeds the predefined tolerance limit. |
| Credit or Debit Memos for Retroactive Price Changes | This type of processing is similar to the previous one except that it deals with retroactive price changes. Therefore, the system compares the claimed net value change against the internal retroactive billing value, which is calculated in your system based on input such as price changes of the settled transaction. |

#### Action Codes for Controlling the Processing Flow

The following table lists the possible combinations of header action codes, item action codes, and the corresponding processing flow.

| Header Action Code | Item Action Code | Processing Flow |
| --- | --- | --- |
| 000 (indicates self-billing invoice) | 001 or 091 (indicates goods receipt) | Initial invoice creation |
|  | 002 or 092 (indicates goods receipt correction)005 or 095 (indicates transport damages) | Credit or debit memos for quantity corrections |
| 001 (indicates retroactive price changes) | 002 or 092 (indicates goods receipt correction)005 or 095 (indicates transport damages) | Credit or debit memos for quantity corrections |
|  | 009 or 099 (indicates value-based clearing invoice with retroactive billing) | Credit or debit memos for retroactive price changes |

### Check Auto Processing Result

Purpose

This process step shows you how to check self-billing auto processing result.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to SAP Self-Billing Cockpit Launchpad. | SAP Self-Billing Cockpit Launchpad is displayed. |  |
| 2 | Access the App | Open Manage Self-Billing - Invoice Creation. |  |  |
| 3 | Choose the transmission | On the self-billing list view, add filter External Transmission and make the following entry:External Transmission: 100001 | Transmission 100001 is displayed. Entry of external billing document 7000001 is simulated in orange status.Note External Transmission is corresponding to the field <transmissionId> received from transmission. Same external ID from same sender will trigger corresponding duplication check. Please use different External Transmission ID for your multiple testing.Overall Status:Error occur during processing and stopped from further processing.Simulated. The comparison result and tolerance check result provided.Confirmed. Successfully executed. Process completed.Processing. It is in processing or pending for processing due to sequence control. |  |

### Check Simulation Result

Purpose

This process step shows you how to check the detail simulation result.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass/ Fail/ Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to SAP Self-Billing Cockpit Launchpad. | SAP Self-Billing Cockpit launchpad is displayed. |  |
| 2 | Access the App | Open Manage Self-Billing– Invoice Creation. |  |  |
| 3 | Choose the transmission | Add filter External Transmission and make the following entry: External Transmission: 100001 | Transmission 100001 displayed which contains three entries in orange simulation status.External billing document 7000001 has the issue type Quantity Difference. |  |
| 4 | Check Simulation Result Detail | Choose the navigation arrow on the right of External Billing Document 7000001 entry.Checking the document detail.Choose the arrow upperleft to go back after. | Detail page displayed for the three document.External Billing Document 7000001Net Value Difference and Tax Amount Difference are displayed.. |  |
| 5 | Check Simulation Result Detail | Choose the navigation arrow on the right ofExternal Billing Document 7000001 entry.Check the document detail.Choose the arrow upperleft to go back after | Detail page displayed for the document.External Billing Document 7000001 headerNet Value Difference: 0 AED Not RelevantTax Amount Difference: 0 AEDProduct Item TG11Quantity Difference: 0Net Value Difference: 0.00 AEDTolerance Check Result: Not RelevantProduct Item TG12:Quantity Difference: -1.000 PCNet Value Difference: 0.00 AEDTolerance Check Result: Not Relevant |  |

|  |
| --- |
| Note The simulation results need to be validated to decide if applicable for further execution. |

### Execute Self-Billing Document

Purpose

This process step shows you how to execute the simulated document.

Prerequisites

The execution can only be performed to the document with simulation result in Orange with active status.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass/ Fail/ Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to SAP Self-Billing Cockpit Launchpad | SAP Self-Billing Cockpit launchpad displays. |  |
| 2 | Access the App | Open Manage Self-Billing– Invoice Creation. |  |  |
| 3 | Choose the transmission | Add filter External Transmission and make the following entry: External Transmission: 100001 |  | Using filter function to find out the transmission is because this step is for executing specific transmission. |
| 4 | Execute | Flag the check box of Select all, choose Execute. | The execution for transmission 100001 is triggered.Selected documents completed execution and turned to Confirmed status in green. | As the execution including multiple updates and creation actions in the SAP S/4HANA Cloud Public Edition system, it may take some time to get confirmed after execution triggered. |

### Check Execution Result (Optional)

Purpose

This process step shows you how to check the detail execution result.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass/ Fail/ Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to SAP Self-Billing Cockpit Launchpad. | SAP Self-Billing Cockpit launchpad is displayed. |  |
| 2 | Access the App | Open Manage Self-Billing– Invoice Creation. |  |  |
| 3 | Choose the transmission | Add filter External Transmission and make the following entry: External Transmission: 100001 | External Transmission 100001 displayed and all three entries are with Green - Confirmed-status.Note Using filter function to find out the transmission is because this step is for executing specific transmission. |  |
| 4 | Check Execution Result Detail | Choose the navigation arrow on the right of referenced delivery 70000001 entry.Choose the arrow on the right of the item to navigate to item history page.Choose the arrow upperleft to go back after checking history details.Choose the arrow upperleft to go back. | History page displayed with execution results.Initial Invoice I00001 created.No any Clearing line nor Open line.Note Clicking Billing Document Number in blue can navigate to the corresponding billing document display screen in S/4 HANA Cloud. |  |

|  |
| --- |
| Note The simulation results need to be validated to decide if applicable for further execution. |

## Appendix

### Process Integration

The process to be tested in this test script is part of a chain of integrated processes, follow each of the process of 3NR, and BD9.

### Succeeding Processes

After completing the activities in this test script, you can continue testing the following business processes:

Table 6:

| Scope Item | Business Condition |
| --- | --- |
| J59 - Accounts Receivable | Posting a Customer Invoice in Accounting, etc.Using the master data from this document, complete the following activities described in the test script:Account Receivable (Sections Incoming Payments, Overdue Receivables, Display Customer Balances, Manage Customer Line Items.) |

### Transmission Example

As described in [Format Transmission](#unique_13) [page ] 9, the example transmission filling with the data for designed scenario is as below.

|  |
| --- |
| Sample Code<soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:tran="http://sap.com/sb/transmission"> <soapenv:Header/> <soapenv:Body> <tran:SelfBillingInvTransmissionMessage> <transmission> <transmissionId>T100001</transmissionId> <senderId>AMOTOR</senderId> <transmissionDate>20210916</transmissionDate> <billingDocument> <headerActionCode>000</headerActionCode> <externalBilling>7000001</externalBilling> <isoCurrency>AED</isoCurrency> <paymentKeyTerm></paymentKeyTerm> <customerVatNumber></customerVatNumber> <supplierVatNumber></supplierVatNumber> <netValue></netValue> <grossAmount></grossAmount> <taxAmount></taxAmount> <surcharges></surcharges> <cashDiscountAmount>1</cashDiscountAmount> <fixedValueDate></fixedValueDate> <documentDate>20210916</documentDate> <deliveryHeader> <!--deliveryHeader 1--> <delivery>80000001</delivery> <customerPlant></customerPlant> <customerUnloadingPoint></customerUnloadingPoint> <customerSupplier></customerSupplier> <soldToParty>33100003</soldToParty> <goodsReceiptDate></goodsReceiptDate> <serviceRenderedDate></serviceRenderedDate> <shippingDate></shippingDate> <deliveryTaxAmount></deliveryTaxAmount> <deliveryGrossAmount></deliveryGrossAmount> <billingItem> <itemActionCode>01</itemActionCode> <quantity>6</quantity> <isoUnitOfMeasure>PCE</isoUnitOfMeasure> <netValue>105.3</netValue> <grossAmount></grossAmount> <price></price> <priceUnit></priceUnit> <priceIsoUoM>EA</priceIsoUoM> <taxAmount>22.11</taxAmount> <taxRate></taxRate> <externalInvoiceNumber></externalInvoiceNumber> <product>TG11</product> <customerMaterial></customerMaterial> <newPrice></newPrice> <newPriceUnit></newPriceUnit> <priceDifference></priceDifference> <priceValidFromDate></priceValidFromDate> </billingItem> </deliveryHeader> <deliveryHeader> <!--deliveryHeader 1--> <delivery>80000002</delivery> <customerPlant></customerPlant> <customerUnloadingPoint></customerUnloadingPoint> <customerSupplier></customerSupplier> <soldToParty>33100003</soldToParty> <goodsReceiptDate></goodsReceiptDate> <serviceRenderedDate></serviceRenderedDate> <shippingDate></shippingDate> <deliveryTaxAmount></deliveryTaxAmount> <deliveryGrossAmount></deliveryGrossAmount> <billingItem> <itemActionCode>01</itemActionCode> <quantity>7</quantity> <isoUnitOfMeasure>PCE</isoUnitOfMeasure> <netValue>122.85</netValue> <grossAmount></grossAmount> <price></price> <priceUnit></priceUnit> <priceIsoUoM>EA</priceIsoUoM> <taxAmount>25.80</taxAmount> <taxRate></taxRate> <externalInvoiceNumber></externalInvoiceNumber> <product>TG12</product> <customerMaterial></customerMaterial> <newPrice></newPrice> <newPriceUnit></newPriceUnit> <priceDifference></priceDifference> <priceValidFromDate></priceValidFromDate> </billingItem> </deliveryHeader> </billingDocument> </transmission> </tran:SelfBillingInvTransmissionMessage> </soapenv:Body> </soapenv:Envelope> |

### Send Transmission with Postman

The process is to simulate sending transmission for testing. Here use Postman as the example.

Table 7:

| Test Step # | Test Step Name | Instruction | Comment |
| --- | --- | --- | --- |
| 1 | Get the test tool Postman | Download Postman via below link: [https://www.getpostman.com/downloads/](https://www.getpostman.com/downloads/)Install the package. | Choose suitable version based on your operation system, Windows 32-bit or Windows 64-bit.If you already have Postman installed, please skip this step. |
| 2 | Create Collection | Choose New > Collection at the top left of the screen and make the following entry:Name: <Enter the name for your identification>Choose Create. |  |
| 3 | Create Request | Find the collection just created on the leftside of the screen. Choose View more actions.Choose Add Request from the drop down list and make the following entry:Request Name: <Enter the name for your identification>Choose Save to <collection name defined in previous step>. |  |
| 4 | Maintain Request | Choose the request just created on the leftside of the screen under the collection and make the following entry for the details display on the right side of the screen.Change the action from GET to POST.Enter request URL: <Self-Billing Tenant URL>/api-password/selfbilling-transmission-receiver-service/v1/api/Transmission_InChoose Authorization tab, select TYPE: Basic Auth, maintain Username and Password.Choose Headers tab and add one line entry with the followings:KEY: Content-TypeVALUE: text/xmlChoose Body tab, select the radio button of Raw.Fill in transmission details, example provided in previous [Transmission Example](#unique_14) [page ] 19.Choose Save. | <Self-Billing Tenant URL> can get after sub-scribing Self-Billing service with referring to Subscribe to Self-Billing in 4H2 setting up instructions,Techincal User should be maintained for the Basic Auth. Please refere to setting up scope item 4H2 for how to create technical user Technical User for Transmission Recevier API. |
| 5 | Send the transmission | Choose Send on the upper right of the screen. | Whether the transmission has been successfully received will be displayed at the button after choosing Send. |

### Resources

- [SAP Self-Billing Cockpit](https://help.sap.com/docs/CP_SELF_BILLING?ai=true)
- [Administration Guide](https://help.sap.com/docs/CP_SELF_BILLING/ed6677e050b142a1b99d068c813d6ac6/52b2d78b3bf7415cb72ab3c0723ba013.html?ai=true)
- [Creating Business Users and technical Users](https://help.sap.com/docs/CP_SELF_BILLING/86e3607c4c1d43eca25d4c9433799c08/b553ccab42504e978efd3609de4d4ffa.html?q=Create+Business+User&ai=true)
- [Connecting to SAP S/4HANA Cloud](https://help.sap.com/docs/CP_SELF_BILLING/ed6677e050b142a1b99d068c813d6ac6/26bc9cb8b1c349b4849a275a8ce08a33.html?ai=true)
- [Connecting to SAP S/4HANA](https://help.sap.com/docs/CP_SELF_BILLING/ed6677e050b142a1b99d068c813d6ac6/7932c1ec391c42fd8d186a397c286c83.html?ai=true)
- [API reference Documentation](https://help.sap.com/docs/CP_SELF_BILLING/3c59c5f3dc1c46f7872ae6124561ece8/2064331eb4b943c78b0007a82a3016c6.html?ai=true)

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
> Flagged while digesting this document, not verified: Business Conditions require the 3NR script completed with 'valid delivery, billing created', while Create Delivery says deliveries follow 3NR 'but do not create billing document'.

> [!warning] Conflict
> Flagged while digesting this document, not verified: Format Transmission refers to 'three preceding deliveries' and the check steps expect three entries, but only two deliveries (80000001, 80000002) and two delivery headers appear in the scenario and example transmission.

> [!warning] Conflict
> Flagged while digesting this document, not verified: Scenario table states TG12 (delivered 8, transmitted 7 PCE) gives 'No difference ... partially billed', while Check Simulation Result expects Quantity Difference -1.000 PC and issue type Quantity Difference for the same item.

> [!warning] Conflict
> Flagged while digesting this document, not verified: Second scheduling agreement (30000002) is listed under sold-to party 33100001, whereas sample data, parameters, transmission and sold-to determination use only 33100003.

## Connections
- part-of :: [[_cluster]]
- related-to :: [[08-sales-order-management/test-script-sales-order-processing-with-invoice-list-and-collective-bi]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/4H2_S4CLD2608_BPD_EN_AE.docx` — full document · extracted with `mammoth` · 39,059 chars in the whole document
