---
id: 15-retail-operations/store-connectivity-inbound-3hv-ae-test-script-sap-s-4hana-cloud-public
title: "Store Connectivity – Inbound (3HV_AE) Test Script, SAP S/4HANA Cloud Public Edition (3HV_S4CLD2608_BPD_EN_AE)"
description: "Test script for scope item 3HV: receiving POS sales, returns, payments and finance data via SOAP, scheduling posting jobs, AIF monitoring, sample payloads."
cluster: 15-retail-operations
tags: [kb/retail-operations, topic/store-connectivity]
aliases: [3HV_S4CLD2608_BPD_EN_AE]
keywords: [Store Connectivity (POS Inbound and Outbound), store connectivity inbound, aggregated sales, sales per receipt, sales returns, aggregated payment list, customer order payment, pos financial transactions, pos inbound job scheduling, message monitoring]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/3HV_S4CLD2608_BPD_EN_AE.docx]
confidence: high
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-940
topic: 15-retail-operations/store-connectivity
language: EN
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Store Connectivity – Inbound (3HV_AE) Test Script, SAP S/4HANA Cloud Public Edition (3HV_S4CLD2608_BPD_EN_AE)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/3HV_S4CLD2608_BPD_EN_AE.docx`, extracted with `mammoth`. Grouped under **Store Connectivity (POS Inbound and Outbound)** in Retail Operations. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

|  |  |
| --- | --- |
| Store Connectivity – Inbound (3HV_AE)Purpose PUBLIC 1<!-- image omitted: unnamed --> | Test ScriptSAP S/4HANA Cloud Public Edition - 19-06-26 |
|  | Store Connectivity – Inbound (3HV_AE) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Table of Contents

[1 Purpose 4](#_Toc232852810)

[2 Prerequisites 6](#_Toc232852811)

[2.1 System Access 6](#_Toc232852812)

[2.2 Roles 6](#_Toc232852813)

[2.3 Master Data, Organizational Data, and Other Data 6](#_Toc232852814)

[2.4 Additional Manual Configuration 9](#_Toc232852815)

[2.5 Business Conditions 9](#_Toc232852816)

[2.6 Preliminary Steps 9](#_Toc232852817)

[2.6.1 Schedule Job for Initial Replication 9](#_Toc232852818)

[2.6.2 Schedule Job for Delta Replication 10](#_Toc232852819)

[2.6.3 Monitor Message Summary in SAP Application Interface Framework 12](#_Toc232852820)

[3 Overview Table 13](#_Toc232852821)

[4 Test Procedures 15](#_Toc232852822)

[4.1 Process Aggregated Sales from POS or SAP Omnichannel Sales transfer and Audit 15](#_Toc232852823)

[4.1.1 Receive Aggregated Sales 15](#_Toc232852824)

[4.1.2 Monitor Inbound Queue (Optional) 16](#_Toc232852825)

[4.1.3 Schedule Job for Posting of POS Inbound for Sales 17](#_Toc232852826)

[4.1.4 Monitor Results and Handle Errors (Optional) 18](#_Toc232852827)

[4.2 Process Sales per Receipt from POS 20](#_Toc232852828)

[4.2.1 Receive Sales per Receipt 20](#_Toc232852829)

[4.2.2 Monitor Inbound Queue (Optional) 21](#_Toc232852830)

[4.2.3 Schedule Job for Posting of POS Inbound for Sales 22](#_Toc232852831)

[4.2.4 Manage Results and Error Handling 23](#_Toc232852832)

[4.3 Process Sales per Receipt (Returns) from POS 24](#_Toc232852833)

[4.3.1 Receive Sales per Receipt (Returns) 24](#_Toc232852834)

[4.3.2 Monitor Inbound Queue (Optional) 25](#_Toc232852835)

[4.3.3 Schedule Job for Posting of POS Inbound for Sales 26](#_Toc232852836)

[4.3.4 Manage Message Queue and Errors 27](#_Toc232852837)

[4.4 Process Aggregated Payment List from POS 29](#_Toc232852838)

[4.4.1 Receive Aggregated Payment List 29](#_Toc232852839)

[4.4.2 Monitor Inbound Queue (Optional) 30](#_Toc232852840)

[4.4.3 Schedule Job for Posting of POS Inbound for Sales 31](#_Toc232852841)

[4.4.4 Monitor Results and Handle Errors (Optional) 32](#_Toc232852842)

[4.5 Process Customer Order Payment from POS 34](#_Toc232852843)

[4.5.1 Receive Customer Order Payment 34](#_Toc232852844)

[4.5.2 Monitor Inbound Queue (Optional) 35](#_Toc232852845)

[4.5.3 Schedule Job for Posting of POS Inbound for Sales 36](#_Toc232852846)

[4.5.4 Monitor Results and Handle Errors (Optional) 37](#_Toc232852847)

[4.6 Process Finance Data from POS 39](#_Toc232852848)

[4.6.1 Receive Financial Data 39](#_Toc232852849)

[4.6.2 Monitor Inbound Queue (Optional) 40](#_Toc232852850)

[4.6.3 Schedule Job for Posting of POS Inbound for Financial 41](#_Toc232852851)

[4.6.4 Monitor Results and Handle Errors (Optional) 42](#_Toc232852852)

[5 Appendix 44](#_Toc232852853)

[5.1 Send Transmission With API Client Tools 44](#_Toc232852854)

[5.2 Process Integration 45](#_Toc232852855)

[5.2.1 Preceding Processes 45](#_Toc232852856)

[5.2.2 Succeeding Processes 45](#_Toc232852857)

[5.3 Transmission Example 46](#_Toc232852858)

[5.3.1 Aggregated Sales 46](#_Toc232852859)

[5.3.1.1 Basic Scenario 46](#_Toc232852860)

[5.3.1.2 Implicit listing Scenario 47](#_Toc232852861)

[5.3.1.3 Absolute Tax Scenario 48](#_Toc232852862)

[5.3.2 Sales per Receipt 48](#_Toc232852863)

[5.3.2.1 Basic Scenario 49](#_Toc232852864)

[5.3.2.2 Implicit Listing Scenario 50](#_Toc232852865)

[5.3.2.3 Absolute Tax Scenario 50](#_Toc232852866)

[5.3.2.4 Returns Scenario 52](#_Toc232852867)

[5.3.2.5 On-account Payment Scenario 52](#_Toc232852868)

[5.3.3 Aggregated Payment List 54](#_Toc232852869)

[5.3.4 Customer Order Payment 55](#_Toc232852870)

[5.3.5 Financial Transaction 56](#_Toc232852871)

[5.3.5.1 Pay In 56](#_Toc232852872)

[5.3.5.2 Pay Out 57](#_Toc232852873)

## Purpose

Overview

Business transactions originating from point-of-sale (POS) solutions in the stores are regularly transferred and trigger the posting of relevant documents. Typically, the transactions aren't sent directly from the POS solutions. Most retailers send transactions from the POS first to a solution where all transactions are collected, audited, and aggregated. We recommend using the SAP Omnichannel Sales Transfer and Audit solution for this purpose. From this solution, aggregated transactions (and, in specific use cases, non-aggregated (receipt-level) transactions) are periodically pushed to the back end for further processing.

Relevant transactions include sales, returns, customer order payments, and pure financial transactions. Based on this, documents for goods movements and billing are created, as well as the respective financial postings. The processed sales data are the basis for follow-on processes like replenishment.

This data includes:

- Aggregated sales data: typically, at granular level, such as store, article, or day
- Aggregated payment list: transactions are accumulated based on the payment methods
- Sales per receipt and returns: single sales transaction with relevant details, including means of payment
- Customer order payment: payment for a referenced customer order
- Financial transactions: import of purely financial transactions (that is, transactions that only affect financial accounting)

You can send confirmation messages to the source solution to acknowledge successful processing of the received transactions.

Efficient and user-friendly monitoring and exception handling are ensured via integration into Application Interface Framework (AIF). Technically, the communication is implemented via asynchronous SOAP services.

This document provides a detailed procedure for testing this scope item after solution activation, reflecting the predefined scope of the solution. Each process step, report, or item is covered in its own section, providing the system interactions (test steps) in a table view. Steps that are not in scope of the process but are needed for testing are marked accordingly. Project-specific steps must be added.

|  |
| --- |
| Note Values in this test script (decimal notation, date formats, and so on) are presented in U.S. standard notation. If your test system is set up to use a different notation, enter values as appropriate. |

|  |
| --- |
| Note In the retail industry, specific terms differ from the standard terms used in other lines of business. Therefore, SAP solutions which provide business processes across multiple lines of businesses may use terms for the corresponding business objects, transactions, and user interfaces that deviate from the retail terminology. For integration and reuse reasons, the SAP S/4HANA Cloud Public Edition, retail, fashion, and vertical business business may thus include different terms that refer to the same concept. SAP intends to harmonize the terminology in the future.The following terms are used synonymously in this document:Table 1:Standard Terms in Lines of BusinessSAP S/4HANA Cloud Public Edition, retail, fashion, and vertical business businessMaterial, productArticleMaterial group, product groupMerchandise categoryPlant, locationSite (as superordinate term) - store and distribution center (DC) |

## Prerequisites

This section summarizes all the prerequisites for conducting the test in terms of systems, users, master data, organizational data, other test data and business conditions.

### System Access

|  |  |
| --- | --- |
|  | Details |
| System | Accessible through SAP Fiori launchpad. Your system administrator provides you with the URL to access the various apps assigned to your role. |

### Roles

Create business roles using the following business role templates delivered by SAP and assign them to your individual test users.

Alternatively, if available, you can use the following spaces delivered by SAP. You create a space with pages containing predefined essential apps and assign it to the business role. You then assign this business role to your individual users.

For more information, refer to How to Create a Business Role from a Template in the [product assistance](https://help.sap.com/docs/SAP_S4HANA_CLOUD/53e36b5493804bcdb3f6f14de8b487dd/ec310a8b669a45ca898dc4dd91d97de2.html) for SAP S/4HANA Cloud Public Edition.

| Name (Role Template) | ID (Role Template) | Name (Launchpad Space) | ID (Launchpad Space) | Log On |
| --- | --- | --- | --- | --- |
| Administrator (Retail) | SAP_BR_ADMINISTRATOR_RFM | Administration - Retail | SAP_BR_ADMINISTRATOR_RFM |  |
| Configuration Expert - Business Network Integration | [SAP_BR_CONF_EXPERT_BUS_NET_INT](https://qj5-279.wdf.sap.corp/ui) | Configuration Expert - Business Network Integration | [SAP_CORE_SPT_INT_PC / SAP_CON_SPT_CONCUR_INT_PC / SAP_OC_SPT_INT_PC / SAP_CA_SPT_DATA_REP_PC / SAP_CA_SPT_BUS_NETWORK_INT_PC](https://qj5-279.wdf.sap.corp/ui) |  |

### Master Data, Organizational Data, and Other Data

The organizational structure and master data of your company have been created in your system during activation. The organizational structure reflects the structure of your company. The master data represents materials, customers, and suppliers, for example, depending on the operational focus of your company.

|  |
| --- |
| Caution Update Behavior of Predelivered Demo DataIn non-productive environments (such as starter systems, sandbox systems, or partner demo systems), SAP initially deploys demo data for your selected scope. You can use this data to test and evaluate business processes.In a customer system, you can receive new or updated demo data after initial activation with further scope enhancements, provided the existing demo data wasn't changed in an incompatible way. If activation errors occur due to incompatible changes in demo data, you're responsible for resolving them. If you don't resolve the errors within a specific time frame, SAP reserves the right to deactivate demo data in your systems. In this case, you can continue by creating your own demo data. Alternatively, you can request that your systems be reprovisioned if you want to work with predelivered demo data again.In partner systems, you can use the demo data deployed with the initial activation. No additional demo data will be deployed in the system with scope enhancements. You can only create additional demo data manually. |

Use your own master data or the following sample data to go through the test procedure.

| Data | Sample Value | Details | Comments |
| --- | --- | --- | --- |
| Single Article | R_1006R_1035R_1045R_6110 | My Best Frozen StrawberriesWhite bread small, organicCHIPS Texas StyleMy Best Maccheroni |  |
| Variants of Generic article | R_1003001R_1003002R_1003003R_1003004R_1003005R_1003006R_1003007R_1003008R_1003009R_1003010R_1003011R_1003012R_1003013R_1003014R_1044001R_1044002R_1044003R_1044004R_1044005R_1044006R_1044007R_1044008R_1044009R_1044010R_1044011R_1044012R_1044013R_1044014 | Chocolate, Whole-Milk, DietChocolate, Nuts, DietChocolate, Raisin-Nut, DietChocolate, Christmas Flavor, DietChocolate, Cherry Yoghurt, DietChocolate, Summer-Feeling, DietChocolate, Orange-Punch, DietChocolate, Whole-Milk, NormalChocolate, Nuts, NormalChocolate, Raisin-Nut, NormalChocolate, Christmas Flavor, NormalChocolate, Cherry Yoghurt, NormalChocolate, Summer-Feeling, NormalChocolate, Orange-Punch, NormalCream Yoghurt, Nuts, DietCream Yoghurt, Cherry Yoghurt, DietCream Yoghurt, Strawberry, DietCream Yoghurt, Raspberry, DietCream Yoghurt, Blueberry, DietCream Yoghurt, Blackberry, DietCream Yoghurt, Redcurrant, DietCream Yoghurt, Nuts, NormalCream Yoghurt, Cherry Yoghurt, NormalCream Yoghurt, Strawberry, NormalCream Yoghurt, Raspberry, NormalCream Yoghurt, Blueberry, NormalCream Yoghurt, Blackberry, NormalCream Yoghurt, Redcurrent, Normal |  |
| Structured Articles | Display - R_2007Sales Set - R_1052Empties Article - R_2011, R_2012Full Article – R_2010 | Chocolate Bar DisplayMy Best Blond Shampoo & ConditionerBottle, CrateLemonade |  |
| Store (Site) | 3340 | Store 3340 AE |  |
| Store (Site) | 3341 | Store 3341 AE |  |
| Store (Site) | 3342 | Store 3342 AE |  |
| Store (Site) | 3343 | Store 3343 AE |  |
| Store (Site) | 3344 | Store 3344 AE |  |
| POS Inbound profile | R33I | POS Inb Profile AE |  |
| Pricing Procedure | A10034 | POS Inbound |  |
| Payment Methods | ETCS, ETVO, ETVI, ETAM, ETDI, ETMC, ETCC,ETBL - Invoice Amount | ETCS: Cash paymentETVO: Voucher PaymentETVI: Card - Visa PaymentETAM: Card - American ExpressETDI: Card – Diners CardETMC: Card – Master CardETCC: Card – Credit card |  |
| Profit Center | Y1040 | Template Store |  |
| Financial – Transaction type | RPIN, RPOU | RPIN – Pay InRPOU – Pay Out |  |

### Additional Manual Configuration

Before you can test this scope item, you must have completed the additional configuration steps that are described in the Set-Up Instructions for this scope item. These configuration steps are specific for your implementation and include mandatory settings that are not delivered by SAP and must be created by you. For more information, follow the link to the document:

[Link to Set-Up Instructions](https://help.sap.com/docs/SAP_S4HANA_BEST_PRACTICES/1b70528d7a1e85a17f504bc186d5feaf)

### Business Conditions

Before you can test this scope item, the following business conditions must be met.

| Scope Item ID | Business Condition |
| --- | --- |
| 3I3 - Sites for Retail | Must be run before this test script. |
| 3I1 - Products for Retail | Must be run before this test script. |

|  |
| --- |
| Note For testing full product and empties, you have to activate the scope item 5FK and execute the preliminary steps. |

### Preliminary Steps

Follow the test procedures in preliminary steps if you want to execute Store Connectivity - Inbound (3HV) scope item with SAP Omnichannel Sales Transfer and Audit.

#### Schedule Job for Initial Replication

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this procedure, you can change the communication arrangement to schedule and activate the job for initial replication of master data from SAP S/4HANA Cloud Public Edition system to SAP Omnichannel Sales Transfer and Audit system.

During initial replication, the application replicates all existing instances of business objects. Typically, you perform this activity only once.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log onto the SAP Fiori Launchpad as an Administrator. |  |  |
| 2 | Access the SAP Fiori app | Open Communication Arrangements (F1763) app. | Communication Arrangements (F1763) selection screen is displayed. |  |
| 3 | Select the communication arrangement | Select the arrangement name for the scenario ID SAP_COM_0885 created during initial set up. | Communication Arrangements (F1763) screen is displayed. |  |
| 4 | Schedule a background job | Perform the following for Product and Plant outbound services:Specify your Package Size.Replication Mode: Specify I for initial replication.Select Save. | Communication arrangement is activated to trigger the initial replication of Product and Plant master data. |  |

#### Schedule Job for Delta Replication

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this procedure, you can change the communication arrangement after the stores are initialized. This enables you to replicate delta changes in the master data from SAP S/4HANA Cloud Public Edition system to SAP Omnichannel Sales Transfer and Audit system.

During delta replication, the application replicates all instances of the business objects that have change pointers. For example, organizations typically perform this activity once a day or so. The frequency depends on how often the master data changes and its relevance for the target system.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log onto the SAP Fiori Launchpad as an Administrator |  |  |
| 2 | Access the SAP Fiori app | Open Communication Arrangements (F1763) app. |  |  |
| 3 | Select the communication arrangement | Select the communication arrangement created during initial set up. |  |  |
| 4 | Change the communication arrangement | Perform the following:Select EditUnder Additional Properties for Product and Plant Outbound Services, enter C in Replication ModeEnter P (Pooled) for Output mode |  |  |
| 5 | Schedule a background job | Perform the following Product and Plant Outbound Services:In the Job Execution Details, specify the frequency for job execution by entering a relevant value in Run Every, for instance, if delta changes, must be replicated once every day then set Run Every as 1 Day(s).Note You can set a different interval for job execution based on your preferences. After you activate the job, the system runs the defined job. Wait until the job finishes.Specify your Start Time and Package SizeSelect Save. | Communication arrangement is activated to replicate the delta changes in product master data at the scheduled intervals. |  |

#### Monitor Message Summary in SAP Application Interface Framework

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this procedure, you can monitor the detailed information about the replication logs for a specific date or duration.

|  |
| --- |
| Note To execute this process step, make sure you have waited for the stipulated time for execution of the job defined in the [Schedule Job for Initial Replication](#unique_9) [page ] 9 or [Schedule Job for Delta Replication](#unique_10) [page ] 10 of this document. After the job is executed, logs are generated. |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log onto the SAP Fiori launchpad as a Configuration Expert - Business Network Integration. |  |  |
| 2 | Access the SAP Fiori app | Open Overview Message Monitoring (F4515) app. | The application screen is displayed with result list of existing application logs. |  |
| 3 | Check Persisted Messages | Navigate to Message Monitoring screen by selecting Status available for /LOGIC – Industry Cloud Solutions and CIC_PROD and CIC_PLANT and select messages which the Administrator (Retail) has posted. | Administrator can check for the persisted messages for the payload posted in the previous preliminary steps. |  |

## Overview Table

This scope item consists of several process steps provided in the table below.

|  |
| --- |
| Note If your system administrator has enabled spaces and pages on the SAP Fiori launchpad, the homepage will only contain the essential apps for performing the typical tasks of a business role.You can find all other (searchable) apps not included on the homepage using the search bar ([2434549](https://me.sap.com/notes/2434549)).If you want to personalize the homepage and include the hidden apps, navigate to your user profile and choose App Finder. |

| Process Steps | Business Role | App/Transaction | Expected Results |
| --- | --- | --- | --- |
| Process Aggregated Sales from POS[Receive Aggregated Sales](#unique_13) [page ] 15[Monitor Inbound Queue (Optional)](#unique_14) [page ] 16[Schedule Job for Posting of POS Inbound for Sales](#unique_15) [page ] 17[Monitor Results and Handle Errors (Optional)](#unique_16) [page ] 18 | Configuration Expert - Business Network IntegrationAdministrator (Retail) | Overview Message Monitoring (F4515)Schedule POS Inbound Service (F5236) | You monitor POS inbound aggregated sales transaction.POS inbound aggregated sales transactions are scheduled for processing. |
| Process Sales per Receipt from POS[Receive Sales per Receipt](#unique_17) [page ] 20[Monitor Inbound Queue (Optional)](#unique_18) [page ] 21[Schedule Job for Posting of POS Inbound for Sales](#unique_19) [page ] 22[Manage Results and Error Handling](#unique_20) [page ] 23 | Configuration Expert - Business Network IntegrationAdministrator (Retail) | Overview Message Monitoring (F4515)Schedule POS Inbound Service (F5236) | You monitor POS inbound sales per receipt transaction.POS inbound sales per receipt transactions are scheduled for processing. |
| Process Sales per Receipt (Return) from POS[Receive Sales per Receipt (Returns)](#unique_21) [page ] 24[Monitor Inbound Queue (Optional)](#unique_22) [page ] 25[Schedule Job for Posting of POS Inbound for Sales](#unique_23) [page ] 26[Manage Message Queue and Errors](#unique_24) [page ] 27 | Configuration Expert - Business Network IntegrationAdministrator (Retail) | Overview Message Monitoring (F4515)Schedule POS Inbound Service (F5236) | You monitor POS inbound sales per receipt (Return) transaction.POS inbound sales per receipt (return) transactions are scheduled for processing. |
| Process Aggregated Payment List from[Receive Aggregated Payment List](#unique_25) [page ] 29[Monitor Inbound Queue (Optional)](#unique_26) [page ] 30[Schedule Job for Posting of POS Inbound for Sales](#unique_27) [page ] 31[Monitor Results and Handle Errors (Optional)](#unique_28) [page ] 32 | Configuration Expert - Business Network IntegrationAdministrator (Retail) | Overview Message Monitoring (F4515)Schedule POS Inbound Service (F5236) | You monitor POS inbound aggregated payment list.POS inbound aggregated payment list are scheduled for processing. |
| Process Customer Order Payment from[Receive Customer Order Payment](#unique_29) [page ] 34[Monitor Inbound Queue (Optional)](#unique_30) [page ] 35[Schedule Job for Posting of POS Inbound for Sales](#unique_31) [page ] 36[Monitor Results and Handle Errors (Optional)](#unique_32) [page ] 37 | Configuration Expert - Business Network IntegrationAdministrator (Retail) | Overview Message Monitoring (F4515)Schedule POS Inbound Service (F5236) | You monitor POS inbound sales per receipt transaction.POS inbound sales per receipt transactions are scheduled for processing. |
| Process Finance data from POS[Receive Financial Data](#unique_33) [page ] 39[Monitor Inbound Queue (Optional)](#unique_34) [page ] 40[Schedule Job for Posting of POS Inbound for Financial](#unique_35) [page ] 41[Monitor Results and Handle Errors (Optional)](#unique_36) [page ] 42 | Configuration Expert - Business Network IntegrationAdministrator (Retail) | Overview Message Monitoring (F4515) appSchedule POS Inbound Service (F5236) | You monitor POS inbound financial transaction.POS inbound financial transactions are scheduled for processing. |

## Test Procedures

This chapter describes the test procedures for each process step that belongs to this scope item.

### Process Aggregated Sales from POS or SAP Omnichannel Sales transfer and Audit

#### Receive Aggregated Sales

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this procedure, you transfer aggregated sales information sent from POS or SAP Omnichannel Sales Transfer and Audit system to SAP S/4HANA Cloud Public Edition system.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Receive aggregated sales payload | SAP S/4HANA Cloud Public Edition system receives an inbound payload with the aggregated information on the sales which took place in a point-of-sales (POS) system or via SAP Omnichannel Sales Transfer and Audit.To simulate the above-mentioned behavior, follow the steps mentioned in [Send Transmission With API Client Tools](#unique_38) [page ] 44.Use the below set of master data:Article:R_1006 (Single Article)R_1003001 (Variant of a Generic Article)R_1052 (Sales Set)R_2007 (Display)R_2010 (Full Article) \| R_2011/R_2012(Empties Article)Store: 3340Refer to the Chapter [Basic Scenario](#unique_39) [page ] 46 for Sample Payload and replace the article in the Transmission example to test all kinds of articles listed above. | After successful posting, Administrator (Retail) checks:Status is shown as Accepted.The persisted messages in the Overview Message Monitoring (F4515) app. |  |

#### Monitor Inbound Queue (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this procedure, you monitor the queue for aggregated sales information coming from SAP Omnichannel Sales Transfer and Audit system to SAP S/4HANA Cloud Public Edition system.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori launchpad as a Configuration Expert - Business Network Integration. |  |  |
| 2 | Access the SAP Fiori App | Open Overview Message Monitoring (F4515) app. | The Overview Message Monitoring screen is displayed with result list of existing Application Logs. |  |
| 3 | Check for the persisted messages | Navigate to Message Monitoring screen by selecting Status (In-process) present for the sales transaction (/RFMPI – Sales -2) and select message details which the Administrator (Retail) has posted. | The Message Monitoring screen is displayed.Administrator (Retail) checks for the persisted messages for the payload posted above. |  |

#### Schedule Job for Posting of POS Inbound for Sales

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this procedure, you schedule a job for posting the aggregated sales data coming from SAP Omnichannel Sales Transfer and Audit system to SAP S/4HANA Cloud Public Edition system. Messages from each store are sent to their respective queue, which is then processed in parallel dependent on stores.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Access the SAP Fiori App | Open Schedule POS Inbound Service (F5236) app. |  |  |
| 2 | Create a Job to Schedule the persisted messages above | Select Create | The New Job: Schedule POS inbound Service is displayed with three steps of input.Template SelectionScheduling OptionsParameters |  |
| 3 | Input Template | Select the Job Template ‘Schedule POS Inbound Service’ and enter the Job Name (as Step 1) and select Step 2. |  |  |
| 4 | Input Scheduling Options | Enter the Start date and time to schedule the Job with the recurrence patten (for example, Daily, Monthly or Weekly) and select Step 3 . |  |  |
| 5 | Input Parameters | Enter details in the following sections as the parameters to schedule the job:Service and Message Status (here Administrator (Retail)need to mention which POS inbound service need to be scheduled, which in this case is Sales)Message Creation Date and Time (here Administrator (Retail)can enter the date & time frame or date function of the persisted messages to be processed)Other Attributes (here Administrator (Retail)can specify the Service specific Attributes. For example, Store or Service reference ID.) along with the Processing Control that is timeout. |  |  |
| 6 | Schedule Job | Select Schedule to schedule the job created. | Schedule Job screen with Status, Log, Results, Step, Description and so on. is displayed. |  |

#### Monitor Results and Handle Errors (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this procedure, you monitor the queue and handle error for aggregated sales information coming from SAP Omnichannel Sales Transfer and Audit system to SAP S/4HANA Cloud Public Edition system.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori launchpad as a Configuration Expert - Business Network Integration |  |  |
| 2 | Access the SAP Fiori App | Open Overview Message Monitoring (F4515) app. | The Overview Message Monitoring (F4515) screen is displayed with Result list of existing Application Logs. |  |
| 3 | Check for the persisted messages | Navigate to Message Monitoring screen by selecting on the Status (Success, Error, In-process) present for the Sales transaction (/RFMPI – Sales -2) and select message details which the Administrator (Retail) has posted. | The Message Monitoring screen is displayed.Administrator (Retail) checks for the execution log for the persisted messages posted above.Billing and/or material document number appears for the successful posting and the log appear in green.A confirmation message is triggered from the SAP S/4HANA Cloud Public Edition system to the SAP Omnichannel Sales Transfer and Audit system if there is successful execution and the log is green.This confirmation message is not sent to the SAP Omnichannel Sales Transfer and Audit system directly if the execution is unsuccessful rather the confirmation message is sent whenever the inbound unsuccessful messages are cancelled at the SAP S/4HANA Cloud Public Edition system.The Monitor and Error Handling screen is displayed. |  |
| 4 | Validate Billing and Material DocumentCheck if the article is not listed in Store A and customer wanted to return this article then the SAP S/4HANA Cloud Public Edition system allows to return, and the article gets listed in this new store A.Pass Absolute Tax Amount in the SAP Omnichannel Sales Transfer and Audit InterfaceNote Absolute Taxes are the taxes which are present at the receipt in the SAP Omnichannel Sales Transfer and Audit system and gets considered when the tax condition record (for example TXF1 or tax condition type applicable to your country) is passed with some tax amount. This condition record contains absolute amount and not percent. When absolute tax code is passed through the SAP S/4HANA Cloud Public Edition system tax recalculation do not happen and system consider the tax amount as it is during the billing document creation in the SAP S/4HANA Cloud Public Edition system.When user pass full article with its tied empties, then SAP S/4HANA Cloud Public Edition system should allow to post billing and goods movement.When user try to return full article with its tied empties, then SAP S/4HANA Cloud Public Edition system should allow to post billing and goods movement.When user try to return empties article, then SAP S/4HANA Cloud Public Edition system should allow to post billing and goods movement. | This check can be done in the SAP S/4HANA Cloud Public Edition system using Overview Message Monitoring (F4515) app in the SAP Fiori launchpad.To test Implicit Listing scenario, you need to create a new store and assign the store with the POS inbound profile R10I (refer to scope item 3I1 – Products for Retail for details on article creation). Then use the transmission example in chapter [Implicit listing Scenario](#unique_40) [page ] 47 with the created article information.To test this scenario, use the transmission example mentioned in Chapter [Absolute Tax Scenario](#unique_41) [page ] 48.This check can be done in the SAP S/4HANA Cloud Public Edition system using Message Monitor Overview (F4515) app in the SAP Fiori launchpad. | Check the billing document is posted with details as passed in the payload.Check the material document is posted successfully.Note In this example, the article is not listed in store A, and the SAP Omnichannel Sales Transfer and Audit system attempts to return it, in this case, billing records with the return amount are created, and the system will put the item in this new store A.Validate if the tax amount and tax condition is posted in the billing document with the value passed in the interface instead of calculating in SD billing process.Check the billing document is posted with details as passed in the payload i.e., The billing document should contain Full Article and its BOM, that is empties article.Check the material document is posted successfully. This document should contain full article with exploded BOM components i.e., empties articles. There should be reduction in the stock situation for tied empties and full articles.Check the billing document is posted with details as passed in the payload i.e., The billing document should contain full article and its BOM, that is, empties article. The billing documents posted should have a reversal of payment, that is net amount and taxes. This can be identified by a negative sign.Check if the material document is posted successfully. This document should contain full article with exploded BOM components, that is empties articles. There should be addition in the stock situation for tied empties and unrestricted full articles.Check the billing document is posted with details as passed in the payload i.e., The billing document should contain Empties Article. The billing documents posted should have a reversal of payment, that is net amount and taxes. This can be identified by a negative sign.Check if the material document is posted successfully. This document should contain empties articles. There should be an addition in the stock situation for unrestricted Empties articles. |  |

### Process Sales per Receipt from POS

#### Receive Sales per Receipt

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this procedure, you check the sales information sent from the external system (POS System) to the SAP S/4HANA Cloud Public Edition system. On the sales per receipt basis the system creates sales document (billing)/material document. To achieve this Administrator (Retail), sets up a communication arrangement, so that data can be exchanged between the external and the SAP S/4HANA Cloud Public Edition Systems

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Receive Sales per Receipt | SAP S/4HANA Cloud Public Edition system receives an inbound payload including information on the sales per receipt that occurred in a point-of-sales (POS) system.This payload received from the POS system using the communication arrangements at the SAP S/4HANA Cloud Public Edition systemTo simulate the above-mentioned behavior, follow the steps mentioned in [Send Transmission With API Client Tools](#unique_38) [page ] 44.Use the below set of master data:Article:R_1006 (Single Article)R_1003001 (Variant of a Generic Article)R_1052 (Sales Set)R_2007 (Display)R_2010 (Full Article)R_2011 and R_2012 (Both are empties article tied to the full article)Store: 3340Refer Chapter [Basic Scenario](#unique_42) [page ] 49 for sample Payload and replace the article in the Transmission, for example to test all the kind of articles listed above. | After successful posting, Administrator (Retail) checks:Status is shown as Accepted.The persisted messages in the Overview Message Monitoring (F4515) app. |  |

#### Monitor Inbound Queue (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this procedure, you monitor the queue and handle error for sales per receipt information coming from POS system to SAP S/4HANA Cloud Public Edition system.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori launchpad as a Configuration Expert - Business Network Integration |  |  |
| 2 | Access the SAP Fiori App | Open Overview Message Monitoring (F4515)app. | The Overview Message Monitoring (F4515) screen is displayed with result list of existing Application Logs. |  |
| 3 | Check for the persisted messages | Navigate to Message Monitoring screen by seelcting on the Status (In-process) present for the Sales transaction (/RFMPI – Sales -2) and select the message details which the Administrator (Retail) has posted | The Message Monitoring screen is displayed.Administrator (Retail) checks for the persisted messages for the payload posted above. |  |

#### Schedule Job for Posting of POS Inbound for Sales

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this procedure, you schedule a job for posting the Billing and Inventory data coming from POS system to SAP S/4HANA Cloud Public Edition system. Messages from each store are sent to its own queue which are executed in stores on parallel basis.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Open the SAP Fiori launchpad as an Administrator (Retail). |  |  |
| 2 | Access the SAP Fiori App | Open Schedule POS Inbound Service (F5236) app | The Schedule POS Inbound Service (F5236) screen is displayed. |  |
| 3 | Create a Job to Schedule the persisted messages above | Select Create | The New Job: Schedule POS inbound Service is displayed with three steps of inputTemplate SelectionScheduling OptionsParameters |  |
| 4 | Input Template | Select the Job Template ‘Schedule POS Inbound Service’ and enter the Job Name (as Step 1) and Select Step 2 |  |  |
| 5 | Input Scheduling Options | Enter the Start date and time to schedule the Job with the recurrence patten (for example. Daily, Monthly or Weekly) and select Step 3 |  |  |
| 6 | Input Parameters | Enter the following chapters as the parameters to schedule the job:Service and Message Status (here Administrator (Retail)mentions which POS inbound service to be scheduled, which in this case is sales)Message Creation Date and Time (here Administrator (Retail)enter the date & time frame or date function of the persisted messages to be processed)Other Attributes (here Administrator (Retail)can specify the Service-Specific Attributes, for example, Store or Service Reference ID.) along with the Processing Control which is timeout. |  |  |
| 7 | Schedule Job | Select Schedule to schedule the job created. | Schedule Job screen with Status, Log, Results, Step, Description and so on is displayed. |  |

#### Manage Results and Error Handling

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this procedure, you monitor the message queue and manage errors related to sales per receipt data transmitted from the POS system to the SAP S/4HANA Cloud Public Edition system.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori launchpad as a Configuration Expert - Business Network Integration |  |  |
| 2 | Access the SAP Fiori App | Open Overview Message Monitoring (F4515) app. | The Overview Message Monitoring (F4515) screen is displayed with Result list of existing Application Logs. |  |
| 3 | Check for the Persisted Messages | Navigate to Message Monitoring screen by selecting on the Status (Success, Error, In-process) present for the Sales transaction (/RFMPI – Sales -2) and select the message details. | The Message Monitoring screen is displayed. |  |
| 4 | Validate Billing and Material Document | Check the posted billing and material documents in the Log Messages table. | The billing document and the material document posted with details based on the data passed in the payload are validated.For details on individual scenarios, see [Sales per Receipt](#unique_43) [page ] 48. |  |

### Process Sales per Receipt (Returns) from POS

#### Receive Sales per Receipt (Returns)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this procedure, you check the sales return information sent from the external system (POS System) to the SAP S/4HANA Cloud Public Edition system. On the sales per receipt basis the system creates sales (billing)/material document. To achieve this Administrator (Retail), sets up a communication arrangement, so that data can be exchanged between the external and the SAP S/4HANA Cloud Public Edition Systems

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Receive Sales per Receipt (returns) | SAP S/4HANA Cloud Public Edition system receives an inbound payload including information on the sales per receipt (returns) that occurred in a point-of-sales (POS) system.This payload received from the POS system using the communication arrangements at the SAP S/4HANA Cloud Public Edition systemTo simulate the above-mentioned behavior, follow the steps mentioned in [Send Transmission With API Client Tools](#unique_38) [page ] 44.Use the below set of master data:Article:R_1006 (Single Article)R_1003001 (Variant of a Generic Article)R_1052 (Sales Set)R_2007 (Display)R_2010 (Full Article)R_2011 and R_2012 (Empties Article)Store: 3340Refer Chapter [Returns Scenario](#unique_44) [page ] 52 for sample Payload à and replace the article in the Transmission, for example to test all the kind of articles listed above. | After successful posting, Administrator (Retail) checks:Status is shown as Accepted.The persisted messages in the Overview Message Monitoring (F4515) app. |  |

#### Monitor Inbound Queue (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this procedure, you monitor the queue and handle error for sales per receipt information coming from POS system to SAP S/4HANA Cloud Public Edition system.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori launchpad as a Configuration Expert - Business Network Integration |  |  |
| 2 | Access the SAP Fiori App | Open Overview Message Monitoring (F4515)app. | The Overview Message Monitoring (F4515) screen is displayed with result list of existing Application Logs. |  |
| 3 | Check for the persisted messages | Navigate to Message Monitoring screen by selecting on the Status (In-process) present for the Sales transaction (/RFMPI – Sales -2) and select the message details which the Administrator (Retail) has posted. | The Message Monitoring screen is displayed.Administrator (Retail) checks for the persisted messages for the payload posted above. |  |

#### Schedule Job for Posting of POS Inbound for Sales

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this procedure, you schedule a job for posting the Billing and Inventory data coming from POS system to SAP S/4HANA Cloud Public Edition system. Messages from each store are sent to its own queue which are executed in stores on parallel basis.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Open the SAP Fiori launchpad as an Administrator (Retail). |  |  |
| 2 | Access the SAP Fiori App | Open Schedule POS Inbound Service (F5236) app. | The Schedule POS Inbound Service (F5236) screen is displayed. |  |
| 3 | Create a Job to Schedule the persisted messages above | Select Create | The New Job: Schedule POS inbound Service is displayed with three steps of inputTemplate SelectionScheduling OptionsParameters |  |
| 4 | Input Template | Select the Job Template ‘Schedule POS Inbound Service’ and enter the Job Name (as Step 1) and Select Step 2 |  |  |
| 5 | Input Scheduling Options | Enter the Start date and time to schedule the Job with the recurrence patten (for example, Daily, Monthly or Weekly) and Select Step 3 |  |  |
| 6 | Input Parameters | Enter the following chapters as the parameters to schedule the job:Service and Message Status (here Administrator (Retail) mentions which POS inbound service to be scheduled, which in this case is s ales)Message Creation Date and Time (here Administrator (Retail) can enter the date & time frame or date function of the persisted messages to be processed)Other Attributes (here Administrator (Retail) can specify the Service-Specific Attributes, for example, Store or Service Reference ID.) along with the Processing Control which is timeout. |  |  |
| 7 | Schedule Job | Select Schedule to schedule the job created. | Schedule Job screen with Status, Log, Results, Step, Description and so on is displayed. |  |

#### Manage Message Queue and Errors

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this procedure, you monitor the queue and manage errors related to sales-per-receipt information transferred from the POS system to the SAP S/4HANA Cloud Public Edition system.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori launchpad as a Configuration Expert - Business Network Integration |  |  |
| 2 | Access the SAP Fiori App | Open Overview Message Monitoring (F4515) app. | The Overview Message Monitoring (F4515) screen is displayed with result list of existing Application Logs. |  |
| 3 | Check for the Persisted Messages | Navigate to Message Monitoring screen by selelcting on the Status (Success, Error, In-process) present for the Sales transaction (/RFMPI – Sales -2) and select the message details which the Administrator (Retail) has posted. | The Message Monitoring screen is displayed.Administrator (Retail) checks for the execution log for the persisted messages posted.Billing and/or material document number appears on the successretrieveful execution and the Log appears in green.A confirmation message is triggered from the SAP S/4HANA Cloud Public Edition system to the POS system if there is successful execution and the log is green.This confirmation message is not sent to the POS system directly if the execution is unsuccessful rather the confirmation message is sent whenever the inbound unsuccessful messages are cancelled at the SAP S/4HANA Cloud Public Edition system.A confirmation message is triggered from the SAP S/4HANA Cloud Public Edition system to the POS system if there is successful execution and the log is green.This confirmation message is not sent to the POS system directly if the execution is unsuccessful rather the confirmation message is sent whenever the inbound unsuccessful messages are cancelled at the SAP S/4HANA Cloud Public Edition system. |  |
| 4 | Validate Billing and Material DocumentCheck if the return is posted in the SAP S/4HANA Cloud Public Edition system successfullyWhen user tries to return Full Article with its tied empties, then the SAP S/4HANA Cloud Public Edition system should allow posting Billing and Goods Movement.When user tries to return Empties article, then the SAP S/4HANA Cloud Public Edition system should allow posting Billing and Goods Movement. | This check can be done in the SAP S/4HANA Cloud Public Edition system using Overview Message Monitoring (F4515)app in the SAP Fiori launchpad.To test this scenario, use the transmission example mentioned in Chapter [Returns Scenario](#unique_44) [page ] 52.This check can be done in the SAP S/4HANA Cloud Public Edition system using Message Monitor Overview (F4515) app in the SAP Fiori launchpad. | Check the billing document is posted with details as passed in the payload.Check the material document is posted successfully.Note Billing and material documents are prepared in this scenario. You need to verify that the amount stated in the billing document is negative and that the material document created contains movement type 252, which denotes sales returns.Check the billing document is posted with details as passed in the payload i.e., The billing document should contain Full Article and its BOM i.e., Empties Article.The billing documents posted should have a reversal of payment i.e., net amount and taxes. This can be identified by a negative sign.Check if the material document is posted successfully. This document should contain full article with exploded BOM components i.e., empties articles. There should be addition in the stock situation for tied Empties and unrestricted Full articles.Check the billing document is posted with details as passed in the payload i.e., The billing document should contain Empties Article. The billing documents posted should have a reversal of payment i.e., net amount and taxes. This can be identified by a negative sign.Check if the material document is posted successfully. This document should contain empties articles. There should be an addition in the stock situation for unrestricted empties articles. |  |

### Process Aggregated Payment List from POS

#### Receive Aggregated Payment List

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this procedure, you transfer the amount which is accumulated based on the payment methods and sent as the aggregated payment list to SAP S/4HANA Cloud Public Edition system using SOAP service from a point-of-sale (POS) to SAP S/4HANA Cloud Public Edition system.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Receive Aggregated Payment list | SAP S/4HANA Cloud Public Edition system gets an inbound payload with the aggregated information of payments for the sales took place in the Point-of-sales system.This payload received from the POS system using the communication arrangements at the SAP S/4HANA Cloud Public Edition system.To simulate the above-mentioned behavior, follow the steps mentioned in [Send Transmission With API Client Tools](#unique_38) [page ] 44.Use the below set of master data:Payment Method:ETCS (Cash Payment)ETVO (Voucher Payment)ETVI (Card payment – VISA)Store: 3340Refer Chapter [Aggregated Payment List](#unique_45) [page ] 54 for sample Payload for Cash, Voucher and Card Payment methods | After successful posting, Administrator (Retail) checks:Status is shown as Accepted.The persisted messages in the Overview Message Monitoring (F4515) app. |  |

#### Monitor Inbound Queue (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this procedure, you monitor the queue and handle error for aggregated payment list information coming from POS system to SAP S/4HANA Cloud Public Edition system.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori launchpad as a Configuration Expert - Business Network Integration |  |  |
| 2 | Access the SAP Fiori App | Open Overview Message Monitoring (F4515)app. | The Overview Message Monitoring (F4515) screen is displayed with Result list of existing Application Logs. |  |
| 3 | Check for the persisted messages | Navigate to Message Monitoring screen by selecting the Status (In-process) present for the Sales transaction (/RFMPI – Sales -2) and select the message details which the Administrator (Retail) has posted | The Message Monitoring screen is displayed.Administrator (Retail) checks for the persisted messages for the payload posted above. |  |

#### Schedule Job for Posting of POS Inbound for Sales

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this procedure, you schedule a job for posting the billing data coming from POS system to SAP S/4HANA Cloud Public Edition system. Messages from each store are sent to its own queue which are executed in stores on parallel basis.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Open the SAP Fiori launchpad as an Administrator (Retail). |  |  |
| 2 | Access the SAP Fiori App | Open Schedule POS Inbound Service (F5236) app. | The Schedule POS Inbound Service (F5236) app is displayed. |  |
| 3 | Create a Job to Schedule the persisted messages above | Select Create | The New Job: Schedule POS inbound Service is displayed with three steps of inputTemplate SelectionScheduling OptionsParameters |  |
| 4 | Input Template | Select the Job Template ‘Schedule POS Inbound Service’ and enter the Job Name (as Step 1) and Select Step 2 |  |  |
| 5 | Input Scheduling Options | Enter the Start date and time to schedule the Job with the recurrence patten (for example, Daily, Monthly or Weekly) and Select Step 3 |  |  |
| 6 | Input Parameters | Enter the following chapters as the parameters to schedule the job:Service and Message Status (here Administrator (Retail)mentions which POS inbound service to be scheduled, which in this case is Sales)Message Creation Date and Time (here Administrator (Retail)can enter the date & time frame or date function of the persisted messages to be processed)Other Attributes (here Administrator (Retail)can specify the Service specific Attributes for example, Store) along with the Processing Control that is timeout |  |  |
| 7 | Schedule Job | Select Schedule to schedule the job created | Schedule Job screen with Status, Log, Results, Step, Description and so on. is displayed. |  |

#### Monitor Results and Handle Errors (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this procedure, you monitor the queue and handle error for aggregated payment list information coming from POS system to SAP S/4HANA Cloud Public Edition system.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass/Fail/Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori launchpad as a Configuration Expert - Business Network Integration |  |  |
| 2 | Access the SAP Fiori App | Open Overview Message Monitoring (F4515) app. | The Overview Message Monitoring (F4515) screen is displayed with Result list of existing Application Logs. |  |
| 3 | Check for the persisted messages | Navigate to Message Monitoring screen by selecting the Status (Success, Error, In-process) present for the Sales transaction (/RFMPI – Sales -2) and select the message details which the Administrator (Retail) has posted. | The Message Monitoring screen is displayed.Administrator (Retail) checks for the execution log for the persisted messages posted above.Billing document number appears for the successful execution and the log should appear in green.A confirmation message is triggered from the SAP S/4HANA Cloud Public Edition system to the POS system if there is successful execution and the log is green.This confirmation message is not sent to the POS system directly if the execution is unsuccessful rather the confirmation message is sent whenever the inbound unsuccessful messages are cancelled at the SAP S/4HANA Cloud Public Edition system.A confirmation message is triggered from the SAP S/4HANA Cloud Public Edition system to the POS system if there is successful execution and the log is green.This confirmation message is not sent to the POS system directly if the execution is unsuccessful rather the confirmation message is sent whenever the inbound unsuccessful messages are cancelled at the SAP S/4HANA Cloud Public Edition system |  |
| 4 | Validate Billing DocumentAggregated Payment List with Card, Cash and Voucher Payment | This check can be done in the SAP S/4HANA Cloud Public Edition system using Overview Message Monitoring (F4515) app in the SAP Fiori launchpad.To test this scenario, use the transmission example mentioned in Chapter [Aggregated Payment List](#unique_45) [page ] 54 | Check the billing document is posted with details as passed in the payload.Once the document is created. Administrator (Retail) double-checks to see if the billing document included the dummy article, and you need to navigate to item condition that contains the billing document and Card payment information.(ETVI), Cash payment condition(ETCS), Voucher payment condition(ETVO) with the payment details. |  |

### Process Customer Order Payment from POS

#### Receive Customer Order Payment

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this procedure, you transfer customer order payment information from a POS system to SAP S/4HANA Cloud Public Edition based on the method of payment, such as cash, cheques, payment cards, electronic cash, or electronic wallet using SOAP service.

|  |
| --- |
| Note The customer order payment is done at POS with reference to a billing document. In order to create a billing document in system, follow the steps from test procedure "Sell from store immediate pick up" from the scope item 3HU. |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Receive Costumer Payment list | SAP S/4HANA Cloud Public Edition system gets an inbound payload with the Customer Order payments for the sales took place in the Point-of-sales system with reference to Billing DocumentThis payload received from the POS system using the communication arrangements at the SAP S/4HANA Cloud Public Edition system.To simulate the above-mentioned behavior, follow the steps mentioned in [Send Transmission With API Client Tools](#unique_38) [page ] 44.Use the below set of master data:Payment Method:ETCS (Cash Payment)ETVO (Voucher Payment)ETVI (Card payment – VISA)Store: 3340Refer Chapter [Customer Order Payment](#unique_46) [page ] 55 for sample Payload for Cash, Voucher and Card Payment methods for a Customer Order Payment | After successful posting, Administrator (Retail) checks:Status is shown as Accepted.The persisted messages in the Overview Message Monitoring (F4515) app. |  |

#### Monitor Inbound Queue (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this procedure, you monitor the queue and handle error for aggregated payment list information coming from POS system to SAP S/4HANA Cloud Public Edition system.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori launchpad as a Configuration Expert - Business Network Integration |  |  |
| 2 | Access the SAP Fiori App | Open Overview Message Monitoring (F4515)app. | The Overview Message Monitoring (F4515) screen displayed with Result list of existing Application Logs. |  |
| 3 | Check for the persisted messages | Navigate to Message Monitoring screen by selecting the Status (In-process) present for the Sales transaction (/RFMPI – Sales -2) and select the message details which the Administrator (Retail) has posted | The Message Monitoring screen is displayed.Administrator (Retail) checks for the persisted messages for the payload posted above. |  |

#### Schedule Job for Posting of POS Inbound for Sales

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this procedure, you schedule a job for posting the Billing data coming from POS system to SAP S/4HANA Cloud Public Edition system. Messages from each store are sent to its own queue which are executed in parallel based on stores.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Open the SAP Fiori launchpad as an Administrator (Retail). |  |  |
| 2 | Access the SAP Fiori App | Open Schedule POS Inbound Service (F5236)app. | The Schedule POS Inbound Service (F5236)app is displayed. |  |
| 3 | Create a Job to Schedule the persisted messages above | Select Create | The New Job: Schedule POS inbound Service appeared with three steps of inputTemplate SelectionScheduling OptionsParameters |  |
| 4 | Input Template | Select the Job Template ‘Schedule POS Inbound Service’ and enter the Job Name (as Step 1) and Select Step 2 |  |  |
| 5 | Input Scheduling Options | Enter the Start date and time to schedule the Job with the recurrence patten (for example, Daily, Monthly or Weekly) and Select Step 3 |  |  |
| 6 | Input Parameters | Enter the following chapters as the parameters to schedule the job:Service and Message Status (here Administrator (Retail)mentions which POS inbound service to be scheduled, which in this case is Sales)Message Creation Date and Time (here Administrator (Retail)can enter the date & time frame or date function of the persisted messages to be processed)Other Attributes (here Administrator (Retail)can specify the Service specific Attributes for example. Store) along with the Processing Control that is timeout |  |  |
| 7 | Schedule Job | Select Schedule to schedule the job created | Schedule Job screen with Status, Log, Results, Step, Description and so on. is displayed. |  |

#### Monitor Results and Handle Errors (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this procedure, you monitor the queue and handle error for aggregated payment list information coming from POS system to SAP S/4HANA Cloud Public Edition system.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass/Fail/Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori launchpad as a Configuration Expert - Business Network Integration |  |  |
| 2 | Access the SAP Fiori App | Open Overview Message Monitoring (F4515) app. | The Overview Message Monitoring (F4515) screen is displayed with Result list of existing Application Logs. |  |
| 3 | Check for the persisted messages | Navigate to Message Monitoring screen by selecting the Status (Success, Error, In-process) present for the Sales transaction (/RFMPI – Sales -2) and select the message details which the Administrator (Retail) has posted | The Message Monitoring screen is displayed.Administrator (Retail) checks for the execution log for the persisted messages posted above.Billing document number appears for the successful execution and the log appear in green.A confirmation message is triggered from the SAP S/4HANA Cloud Public Edition system to the POS system if there is successful execution and the log is green.This confirmation message is not sent to the POS system directly if the execution is unsuccessful rather the confirmation message is sent whenever the inbound unsuccessful messages are cancelled at the SAP S/4HANA Cloud Public Edition system.A confirmation message is triggered from the SAP S/4HANA Cloud Public Edition system to the POS system if there is successful execution and the log is green.This confirmation message is not sent to the POS system directly if the execution is unsuccessful rather the confirmation message is sent whenever the inbound unsuccessful messages are cancelled at the SAP S/4HANA Cloud Public Edition system. |  |
| 4 | Validate Billing DocumentTo make customer payment at Store using POS inbound after goods is invoiced (Created with reference to the Billing Document)Note Please Create Sales Order --> Delivery and then Billing document as a prerequisite for this process step. Kindly refer to the Sub Chapter Create Sales Order, Create Outbound Delivery & Create and Print Billing Document of Chapter 4.1 (Sell from Store : immediate Pickup) from Scope Item 3HU. | This check can be done in the SAP S/4HANA Cloud Public Edition system using Overview Message Monitoring (F4515) app in the SAP Fiori launchpad.To test this scenario, use the transmission example mentioned in chapter [Customer Order Payment](#unique_46) [page ] 55.In continuation of above scenario once the good is delivered to customer and invoiced, the down payment made is cleared and remaining amount is paid by customer at POS. POS will trigger the sales transaction service for remaining payment for the customer order passing sales / billing document number with quantity and amount | Check the billing document is posted with details as passed in the payload. |  |

### Process Finance Data from POS

#### Receive Financial Data

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this procedure, you transfer point-of-sale (POS) financial transactions to the SAP S/4HANA Cloud Public Edition system. This inbound service can transfer financial transaction data including:

- Transfer of posting between different accounts within the store
- Settlement of customer outstanding invoices in a store
- Payment of supplier invoice using the cash reserved in a store
- Transfer of other pay-in and pay-out transactions including postage costs taken from the till (cash register) and payments to temporary staff

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
|  | Receive Financial data | SAP S/4HANA Cloud Public Edition system gets an inbound payload with the financial transaction information which do not involve goods movement at the Point-of-sales systemThis payload received from the POS system using the communication arrangements at the SAP S/4HANA Cloud Public Edition systemTo simulate the above-mentioned behavior, follow the steps mentioned in [Send Transmission With API Client Tools](#unique_38) [page ] 44.Use the below set of master data:Transaction type:Pay In: RPINPay Out: RPOUStore: 3340Refer chapter [Customer Order Payment](#unique_46) [page ] 55 for sample Payload for Pay In and Pay out. | After successful posting, Administrator (Retail) checks:Status is shown as Accepted.The persisted messages in the Overview Message Monitoring (F4515) app. |  |

#### Monitor Inbound Queue (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this procedure, you monitor the queue and handle error for financial data coming from POS system to SAP S/4HANA Cloud Public Edition system.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori launchpad as a Configuration Expert - Business Network Integration |  |  |
| 2 | Access the SAP Fiori App | Open Overview Message Monitoring (F4515) app. | The Overview Message Monitoring (F4515) screen is displayed with Result list of existing Application Logs. |  |
| 3 | Check for the persisted messages | Navigate to Message Monitoring screen by selecting the Status (In-process) present for the Financial transactions (/RFMPI – Financial -2) and select the message details which the Administrator (Retail) has posted | The Message Monitoring screen is displayed.Administrator (Retail) checks the persisted messages for the payload posted above |  |

#### Schedule Job for Posting of POS Inbound for Financial

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this procedure, you schedule a job for posting the financial data coming from POS system to SAP S/4HANA Cloud Public Edition system. Messages from each store are sent to its own queue which are executed in stores on parallel basis.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Open the SAP Fiori launchpad as an Administrator (Retail). |  |  |
| 2 | Access the SAP Fiori App | Open Schedule POS Inbound Service (F5236) app. | The Schedule POS Inbound Service (F5236) app is displayed. |  |
| 3 | Create a Job to Schedule the persisted messages above | Select Create | The New Job: Schedule POS inbound Service is displayed with three steps of inputTemplate SelectionScheduling OptionsParameters |  |
| 4 | Input Template | Enter the Job Template ‘Schedule POS Inbound Service’ and the Job Name (as Step 1) and Select Step 2 |  |  |
| 5 | Input Scheduling Options | Enter the Start date and time to schedule the Job with the recurrence patten (for example, Daily, Monthly or Weekly) and Select Step 3 |  |  |
| 6 | Input Parameters | Enter the following chapters as the parameters to schedule the job:Service and Message Status (here Administrator (Retail) need to mention which POS Inbound Service need to be scheduled, which in this case is Financials)Message Creation Date and Time (here Administrator (Retail) can enter the date & time frame or date function of the persisted messages to be processed)Other Attributes (here Administrator (Retail) can specify the Service specific Attributes for example, Store) along with the Processing Control that is timeout |  |  |
| 7 | Schedule Job | Select Schedule to schedule the job created | Schedule Job screen with Status, Log, Results, Step, Description and so on. is displayed. |  |

#### Monitor Results and Handle Errors (Optional)

Purpose

In this procedure, you can monitor the queue and handle error for aggregated payment information coming from POS system to SAP S/4HANA Cloud Public Edition system.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass/Fail/Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori launchpad as a Configuration Expert - Business Network Integration |  |  |
| 2 | Access the SAP Fiori App | Open Overview Message Monitoring (F4515) app. | The Overview Message Monitoring (F4515) screen is displayed with Result list of existing Application Logs. |  |
| 3 | Check for the persisted messages | Navigate to Message Monitoring screen by selecting the Status (Success, Error, In-process) present for the Financial transactions (/RFMPI – Financial -2) and select the message details which the Administrator (Retail) has posted. | The Message Monitoring screen is displayed..Administrator (Retail) checks for the execution log for the persisted messages posted above.Accounting Document number should appear for the successful execution and the Log appear in Green.A confirmation message is triggered from the SAP S/4HANA Cloud Public Edition system to the POS system if there is successful execution and the log is green.This confirmation message is not sent to the POS system directly if the execution is unsuccessful rather the confirmation message is sent whenever the inbound unsuccessful messages are cancelled at the SAP S/4HANA Cloud Public Edition systemA confirmation message is triggered from the SAP S/4HANA Cloud Public Edition system to the POS system if there is successful execution and the log is green.This confirmation message is not sent to the POS system directly if the execution is unsuccessful rather the confirmation message is sent whenever the inbound unsuccessful messages are cancelled at the SAP S/4HANA Cloud Public Edition system |  |
| 4 | Check Accounting DocumentPay-InPay-out | This check can be done in the SAP S/4HANA Cloud Public Edition system using Overview Message Monitoring (F4515) app in the SAP Fiori launchpad.To test this scenario, use the transmission example mentioned in chapter [Pay In](#unique_47) [page ] 56To test this scenario, use the transmission example mentioned in chapter [Pay Out](#unique_48) [page ] 57 | Check the Accounting document is posted with details as passed in the payload..Once the accounting document is created Administrator (Retail) can check for the Pay-in. For example, postage costs taken from the till.Once the accounting document is created Administrator (Retail) can check for the Pay-out. For example, payments to temporary staff. |  |

## Appendix

### Send Transmission With API Client Tools

The process is to simulate sending transmission for testing using any API client tool.

| Test Step # | Test Step Name | Instruction | Expected Results | Comment |
| --- | --- | --- | --- | --- |
| 1 | Get API Client Tool | Refer to Setup Instruction Guide Chapter Download and Install API Client Tools. |  |  |
| 2 | Create Request | Create a new request with the following entry:Request Name: <Enter the name for your identification>Save request (if the tool allows). |  |  |
| 3 | Maintain Request | Choose the request just created and make the following entry for the details:Change the action from GET to POST.Enter request URL:For Sales Transaction ServiceHYPERLINK "https://<Subdomain>/sap/bc/srt/scs_ext/sap/possalestransactionscreaterequ" https://<Subdomain>/sap/bc/srt/scs_ext/sap/possalestransactionscreaterequFor Financial Transaction ServiceHYPERLINK "https://<Subdomain>/sap/bc/srt/scs_ext/sap/posfinancialtransactionscreate" https://<Subdomain>/sap/bc/srt/scs_ext/sap/posfinancialtransactionscreateParams – MessageID for example 989C3E3A-4CD9-21CA-A200-12002B4CA1B4Choose Authorization tab, select TYPE: Basic Auth, maintain Username and Password.Choose Headers tab and add one line entry with the followings:KEY: Content-TypeVALUE: text/xmlSelect Body tab, select the radio button of Raw.Fill in transmission details, as described in the Chapter Transmission Example for each scenario.Choose Save. |  | <POS Service URL> canget after following Set Up Instructions for 3HV.Technical User to be maintained for the basic authorization. Refer to Set Up Instructions for scope item 3HV for how to create technical user Technical User for Transmission Receiver API. |
| 4 | Send the transmission | Choose Send on the upper right of the screen. | After successful posting, Administrator (Retail) checks:Status is shown as Accepted.The persisted messages in the Overview Message Monitoring (F4515) app. |  |

### Process Integration

The process to be tested in this test script is part of a chain of integrated processes.

#### Preceding Processes

The following processes and conditions can continue this process.

| Process | Business Condition |
| --- | --- |
| 3I1 – Products for Retail | Create Article |
| 3I3 – Sites for Retail | Create Site |
| 3I5 – Assortments | Create Listing |

#### Succeeding Processes

After completing the activities in this test script, you can continue testing the following business processes:

| Process | Business Condition |
| --- | --- |
| 3I7 - Replenishment Planning for Stores | Store replenishment |

### Transmission Example

#### Aggregated Sales

##### Basic Scenario

|  |
| --- |
| NoteBefore you execute any payload, make sure you have the unique Service Call Reference ID value. If you use an existing value, then you won't get the expected results. The data in the sample payloads is only for reference. Change it as needed before you execute your test. For example: adjust the dates as appropriate. Update organizational data such as the store information to match the country you are testing.Each country-specific tax condition type must be created or updated and assigned to POS inbound pricing procedure. The tax condition type TXF1 is not available for all countries. |

<?xml version="1.0" encoding="UTF-8" ?>
<soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
<soapenv:Body>
<n0:PosSalesTransactionsCreateRequest xmlns:n0= "http://sap.com/xi/SAPGlobal20/Global">
<MessageHeader>
<CreationDateTime>2021-04-02T12:00:00.1234567Z </CreationDateTime>
<SenderBusinessSystemID><SENDER_SYSID></SenderBusinessSystemID>
<RecipientBusinessSystemID><RECEIVER_SYSID></RecipientBusinessSystemID>
</MessageHeader>
<PosSalesTransactions>
<ServiceCallReferenceID>2021-04-03-00</ServiceCallReferenceID>
<StoreInternalID>3340</StoreInternalID>
<SalesTransactionsDate>2021-03-07</SalesTransactionsDate>
<AggregatedSalesByProduct>
<SequenceNumber>1</SequenceNumber>
<GlobalTradeItemNumber/>
<ProductInternalID>R_1006</ProductInternalID>
<RetailPromotion/>
<TotalAmount currencyCode="AED">167</TotalAmount>
<TotalQuantity unitCode="PCE">1</TotalQuantity>
</AggregatedSalesByProduct>
</PosSalesTransactions>
</n0:PosSalesTransactionsCreateRequest>
</soapenv:Body>
</soapenv:Envelope>

##### Implicit listing Scenario

<?xml version="1.0" encoding="UTF-8" ?>
<soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
<soapenv:Body>
<n0:PosSalesTransactionsCreateRequest xmlns:n0="http://sap.com/xi/SAPGlobal20/Global">
<MessageHeader>
<CreationDateTime>2021-04-02T12:00:00.1234567Z </CreationDateTime>
<SenderBusinessSystemID><SENDER_SYSID ></SenderBusinessSystemID>
<RecipientBusinessSystemID><RECEIVER_SYSID></RecipientBusinessSystemID>
</MessageHeader>
<PosSalesTransactions>
<ServiceCallReferenceID>2021-04-03-01</ServiceCallReferenceID>
<StoreInternalID>3340 </StoreInternalID>
<SalesTransactionsDate>2021-04-02</SalesTransactionsDate>
<AggregatedSalesByProduct>
<SequenceNumber>1</SequenceNumber>
<GlobalTradeItemNumber/>
<ProductInternalID>ARTICLE</ProductInternalID>
<RetailPromotion/>
<TotalAmount currencyCode="AED">167</TotalAmount>
<TotalQuantity unitCode="PCE">1</TotalQuantity>
</AggregatedSalesByProduct>
</PosSalesTransactions>
</n0:PosSalesTransactionsCreateRequest>
</soapenv:Body>
</soapenv:Envelope>

##### Absolute Tax Scenario

<?xml version="1.0" encoding="UTF-8" ?>
<soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
<soapenv:Body>
 <n0:PosSalesTransactionsCreateRequest xmlns:n0="http://sap.com/xi/SAPGlobal20/Global">
<MessageHeader>
<CreationDateTime>2021-04-02T12:00:00.1234567Z </CreationDateTime>
<SenderBusinessSystemID><SENDER_SYSID></SenderBusinessSystemID>
<RecipientBusinessSystemID><RECEIVER_SYSID></RecipientBusinessSystemID>
 </MessageHeader>
<PosSalesTransactions>
<ServiceCallReferenceID>2021-04-07-00</ServiceCallReferenceID>
<StoreInternalID>3340</StoreInternalID>
<SalesTransactionsDate>2021-04-07</SalesTransactionsDate>
<AggregatedSalesByProduct>
<SequenceNumber>1</SequenceNumber>
 <GlobalTradeItemNumber/>
 <ProductInternalID>R_1006</ProductInternalID>
<RetailPromotion/>
<TotalAmount currencyCode="AED">167</TotalAmount>
 <TotalQuantity unitCode="PCE">1</TotalQuantity>
<PriceSpecification>
 <PriceSpecificationElementTypeCode>TXF1</PriceSpecificationElementTypeCode>
 <PriceSpecificationRateValue>5</PriceSpecificationRateValue>
 </PriceSpecification>
</AggregatedSalesByProduct>
 </PosSalesTransactions>
</n0:PosSalesTransactionsCreateRequest>
</soapenv:Body>
</soapenv:Envelope>

#### Sales per Receipt

|  |
| --- |
| Note Before executing any payload for sales per receipt make sure you have the unique Service Call Reference ID and External Reference Document ID value. If you have used an existing value, then you will not get the expected result. |

##### Basic Scenario

The following payload can be used to test the basic sales-per-receipt scenario.

|  |
| --- |
| Note The data in the sample payload is for reference only and must be changed as needed before execution. For example, dates must be changed accordingly. Organizational data, such as the store, must be changed accordingly for the country you are testing. |

<?xml version="1.0" encoding="UTF-8" ?>
<soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
<soapenv:Body>
<n0:PosSalesTransactionsCreateRequest xmlns:n0="http://sap.com/xi/SAPGlobal20/Global">
<MessageHeader>
<CreationDateTime>2021-06-11T12:00:00.1234567Z</CreationDateTime>
<SenderBusinessSystemID>SENDER_SYSID</SenderBusinessSystemID>
<RecipientBusinessSystemID>RECEIVER_SYSID</RecipientBusinessSystemID>
</MessageHeader>
<PosSalesTransactions>
<ServiceCallReferenceID>2021-06-11-18</ServiceCallReferenceID>
<StoreInternalID>3340</StoreInternalID>
<SalesTransactionsDate>2021-06-11</SalesTransactionsDate>
<SalesPerReceipt>
<ExternalReferenceDocumentID>2021-06-11-19</ExternalReferenceDocumentID>
<TransactionInitiatorID>CASHIERUSERID</TransactionInitiatorID>
<PartnerNumber>33113008</PartnerNumber>
<Item>
<ReturnItemIndicator></ReturnItemIndicator>
<GlobalTradeItemNumber></GlobalTradeItemNumber>
<ProductInternalID>R_1006</ProductInternalID>
<TotalAmount currencyCode="AED">120</TotalAmount>
<TotalQuantity unitCode="PCE">10</TotalQuantity>
</Item>
<PaymentList>
<PaymentMethod>ETCS</PaymentMethod>
<Amount currencyCode="AED">120</Amount>
</PaymentList>
</SalesPerReceipt>
</PosSalesTransactions>
</n0:PosSalesTransactionsCreateRequest>
</soapenv:Body>
</soapenv:Envelope>

##### Implicit Listing Scenario

In this scenario, if an article in a sales-per-receipt item is not listed in the store, and a sale or return occurs, the system automatically extends the article to the store during the processing of the POS Inbound scheduling job.

To test the implicit listing scenario, you need to create a new article (for details on article creation, refer to scope item 3I1 – Products for Retail). This article should not be listed in the store. Then use the below transmission example with the article information created.

<?xml version="1.0" encoding="UTF-8" ?>
<soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
<soapenv:Body>
<n0:PosSalesTransactionsCreateRequest xmlns:n0="http://sap.com/xi/SAPGlobal20/Global">
<MessageHeader>
<CreationDateTime>2021-06-11T12:00:00.1234567Z</CreationDateTime>
<SenderBusinessSystemID>SENDER_SYSID</SenderBusinessSystemID>
<RecipientBusinessSystemID>RECEIVER_SYSID</RecipientBusinessSystemID>
</MessageHeader>
<PosSalesTransactions>
<ServiceCallReferenceID>2021-06-11-18</ServiceCallReferenceID>
<StoreInternalID>3340 </StoreInternalID>
<SalesTransactionsDate>2021-06-11</SalesTransactionsDate>
<SalesPerReceipt>
<ExternalReferenceDocumentID>2021-06-11-19</ExternalReferenceDocumentID>
<TransactionInitiatorID>USERID</TransactionInitiatorID>
<PartnerNumber>PARTNERID</PartnerNumber>
<Item>
<ReturnItemIndicator></ReturnItemIndicator>
<GlobalTradeItemNumber></GlobalTradeItemNumber>
<ProductInternalID>ARTICLE</ProductInternalID>
<TotalAmount currencyCode="AED">120</TotalAmount>
<TotalQuantity unitCode="PCE">10</TotalQuantity>
</Item>
</SalesPerReceipt>
</PosSalesTransactions>
</n0:PosSalesTransactionsCreateRequest>
</soapenv:Body>
</soapenv:Envelope>

##### Absolute Tax Scenario

In this scenario, taxes are calculated externally in the POS system and transferred to SAP S/4HANA Cloud Public Edition system using POS inbound service for sales per receipt.

Here, taxes are not calculated in the SAP S/4HANA Cloud Public Edition system, but taken from the values passed in the service interface. For instance, you can pass an absolute tax amount for the country-specific tax condition type (for example TXF1), as shown in the payload below.

|  |
| --- |
| NoteThe data in sample payloads is for reference only. You must update it as needed before execution. For example, change the dates accordingly. Organizational data, such as the store, must be changed according to the country you are testing.The tax condition type TXF1 is not available in all countries. You must first create the country-specific tax condition type and assign it to the POS inbound pricing procedure. Adjust the payloads to use the applicable tax condition types. If a country-specific tax condition type is already available in the pricing procedure, ensure the payload reflects this type. |

<?xml version="1.0" encoding="UTF-8" ?>
<soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
<soapenv:Body>
<n0:PosSalesTransactionsCreateRequest xmlns:n0="http://sap.com/xi/SAPGlobal20/Global">
<MessageHeader>
<CreationDateTime>2021-06-11T12:00:00.1234567Z</CreationDateTime>
<SenderBusinessSystemID>SENDER_SYSID</SenderBusinessSystemID>
<RecipientBusinessSystemID>RECEIVER_SYSID</RecipientBusinessSystemID>
</MessageHeader>
<PosSalesTransactions>
<ServiceCallReferenceID>2021-06-11-18</ServiceCallReferenceID>
<StoreInternalID>3340</StoreInternalID>
<SalesTransactionsDate>2021-06-11</SalesTransactionsDate>
<SalesPerReceipt>
<ExternalReferenceDocumentID>2021-06-11-19</ExternalReferenceDocumentID>
<TransactionInitiatorID>USERID</TransactionInitiatorID>
<PartnerNumber>3340</PartnerNumber>
<Item>
<ReturnItemIndicator></ReturnItemIndicator>
<GlobalTradeItemNumber></GlobalTradeItemNumber>
<ProductInternalID>R_1006</ProductInternalID>
<TotalAmount currencyCode="AED">120</TotalAmount>
<TotalQuantity unitCode="PCE">10</TotalQuantity>
<PriceSpecification>
<PriceSpecificationElementTypeCode>TXF1</PriceSpecificationElementTypeCode>
<PriceSpecificationRateValue>5</PriceSpecificationRateValue>
</PriceSpecification>
</Item>
</SalesPerReceipt>
</PosSalesTransactions>
</n0:PosSalesTransactionsCreateRequest>
</soapenv:Body>
</soapenv:Envelope>

##### Returns Scenario

In this sceanrio, sales return information is sent from external system (POS system) to the SAP S/4HANA Cloud Public Edition system.

On the sales per receipt basis, the system creates billing document with return amount and material document with sales return movement type (252).

<?xml version="1.0" encoding="UTF-8" ?>
<soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
<soapenv:Body>
<n0:PosSalesTransactionsCreateRequest xmlns:n0="http://sap.com/xi/SAPGlobal20/Global">
<MessageHeader>
<CreationDateTime>2021-06-11T12:00:00.1234567Z</CreationDateTime>
<SenderBusinessSystemID>SENDER_SYSID</SenderBusinessSystemID>
<RecipientBusinessSystemID>RECEIVER_SYSID</RecipientBusinessSystemID>
</MessageHeader>
<PosSalesTransactions>
<ServiceCallReferenceID>2021-06-11-18</ServiceCallReferenceID>
<StoreInternalID>3340</StoreInternalID>
<SalesTransactionsDate>2021-06-11</SalesTransactionsDate>
<SalesPerReceipt>
<ExternalReferenceDocumentID>2021-06-11-19</ExternalReferenceDocumentID>
<TransactionInitiatorID>USERID</TransactionInitiatorID>
<PartnerNumber>33113005</PartnerNumber>
<Item>
<ReturnItemIndicator>true</ReturnItemIndicator>
<GlobalTradeItemNumber></GlobalTradeItemNumber>
<ProductInternalID>R_1006</ProductInternalID>
<TotalAmount currencyCode="AED">120</TotalAmount>
<TotalQuantity unitCode="PCE">10</TotalQuantity>
</Item>
</SalesPerReceipt>
</PosSalesTransactions>
</n0:PosSalesTransactionsCreateRequest>
</soapenv:Body>
</soapenv:Envelope>

##### On-account Payment Scenario

In this scenario, the payment is not made immediately at the point of sale but is instead recorded as a credit (or balance) on the customer's account.

Once the billing and accounting documents are posted by the POS system, the remaining balance owed by the customer is displayed in the Display Customer Balances (F0703A) application.

|  |
| --- |
| Note The data in sample payloads is for reference only and must be changed as needed before execution. For example, dates must be changed accordingly. Organizational data, such as the store, must be changed accordingly for the country you are testing. The partner number and currency code must be changed depending on the country. |

<?xml version="1.0" encoding="UTF-8"?>
<soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
<soapenv:Body>
<n0:PosSalesTransactionsCreateRequest xmlns:n0="http://sap.com/xi/SAPGlobal20/Global">
<MessageHeader>
<CreationDateTime>2025-03-17T12:00:00.1234567Z</CreationDateTime>
<SenderBusinessSystemID>OSTA</SenderBusinessSystemID>
<RecipientBusinessSystemID></RecipientBusinessSystemID>
</MessageHeader>
<PosSalesTransactions>
<ServiceCallReferenceID>2025-03-17-003</ServiceCallReferenceID>
<StoreInternalID>1040</StoreInternalID>
<SalesTransactionsDate>2025-03-17</SalesTransactionsDate>
<SalesPerReceipt>
<ExternalReferenceDocumentID>2025-03-17-004</ExternalReferenceDocumentID>
<TransactionInitiatorID>I337206</TransactionInitiatorID>
<PartnerNumber>1000090</PartnerNumber>
<Item>
<ReturnItemIndicator>false</ReturnItemIndicator>
<GlobalTradeItemNumber></GlobalTradeItemNumber>
<ProductInternalID>R_1007</ProductInternalID>
<TIED_EMPTIES_INDICATOR>false</TIED_EMPTIES_INDICATOR>
<TotalAmount currencyCode="EUR">10</TotalAmount>
<TotalQuantity unitCode="PCE">1</TotalQuantity>
</Item>
<PaymentList>
<PaymentMethod>ETBL</PaymentMethod>
<Amount currencyCode="EUR">10</Amount>
</PaymentList>
</SalesPerReceipt>
</PosSalesTransactions>
</n0:PosSalesTransactionsCreateRequest>
</soapenv:Body>
</soapenv:Envelope>

#### Aggregated Payment List

|  |
| --- |
| Note Before Executing any payload for aggregated payment List make sure you have the unique Service Call Reference ID value. If you have used an existing value, then you will not get the expected result. |

<?xml version="1.0" encoding="UTF-8" ?>
<soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
 <soapenv:Body>
 <n0:PosSalesTransactionsCreateRequest xmlns:n0="http://sap.com/xi/SAPGlobal20/Global">
 <MessageHeader>
<CreationDateTime>2021-04-02T12:00:00.1234567Z </CreationDateTime>
<SenderBusinessSystemID>SENDER_SYSID</SenderBusinessSystemID>
<RecipientBusinessSystemID>RECEIVER_SYSID</RecipientBusinessSystemID>
</MessageHeader>
<PosSalesTransactions>
<ServiceCallReferenceID>2021-04-04-00</ServiceCallReferenceID>
<StoreInternalID>3340</StoreInternalID>
<SalesTransactionsDate>2021-04-04</SalesTransactionsDate>
<AggregatedPaymentList>
<PaymentMethod>ETVI</PaymentMethod>
<Amount currencyCode="AED">120</Amount>
<PaytCardByDigitalPaymentSrvc>1234</PaytCardByDigitalPaymentSrvc>
<AuthorizationDateTime>2021-04-04T12:00:00.1234567Z</AuthorizationDateTime>
 </AggregatedPaymentList>
 <AggregatedPaymentList>
<PaymentMethod>ETCS</PaymentMethod>
<Amount currencyCode="AED">100</Amount>
</AggregatedPaymentList>
<AggregatedPaymentList>
<PaymentMethod>ETVO</PaymentMethod>
<Amount currencyCode="AED">200</Amount>
</AggregatedPaymentList>
</PosSalesTransactions>
</n0:PosSalesTransactionsCreateRequest>
</soapenv:Body>
</soapenv:Envelope>

#### Customer Order Payment

<?xml version="1.0" encoding="UTF-8" ?>
<soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
<soapenv:Body>
<n0:PosSalesTransactionsCreateRequest xmlns:n0="http://sap.com/xi/SAPGlobal20/Global">
<MessageHeader>
<CreationDateTime>2021-12-07T12:00:00.1234567Z</CreationDateTime>
</MessageHeader>
<PosSalesTransactions>
<ServiceCallReferenceID>07-12-2021-01</ServiceCallReferenceID>
<StoreInternalID>3340</StoreInternalID>
<SalesTransactionsDate>2021-12-07</SalesTransactionsDate>
<CustomerOrderPaymentList>
<ExternalReferenceDocumentID>07-12-2021-01</ExternalReferenceDocumentID>
<TransactionInitiatorID>USERID</TransactionInitiatorID>
<SalesDocumentDetails>
<SalesDocumentID><BilingDocumentNo.></SalesDocumentID>
<PaymentUseCode>2</PaymentUseCode>
<Amount currencyCode="AED">60</Amount>
</SalesDocumentDetails>
<PaymentList>
<PaymentMethod>ETCS</PaymentMethod>
<Amount currencyCode="AED">20</Amount>
</PaymentList>
<PaymentList>
<PaymentMethod>ETVO</PaymentMethod>
<Amount currencyCode="AED">20</Amount>
</PaymentList>
<PaymentList>
<PaymentMethod>ETVI</PaymentMethod>
<Amount currencyCode="AED">20</Amount>
<PaytCardByDigitalPaymentSrvc>2222</PaytCardByDigitalPaymentSrvc>
<AuthorizationDateTime>2021-12-07T12:00:00.1234567Z</AuthorizationDateTime>
</PaymentList>
</CustomerOrderPaymentList>
</PosSalesTransactions>
</n0:PosSalesTransactionsCreateRequest>
</soapenv:Body>
</soapenv:Envelope>

#### Financial Transaction

|  |
| --- |
| Note Before executing any payload for financial transaction for Pay In/Pay Out make sure you have the unique External Reference Document ID value. If you have used an existing value, then you will not get the expected result. |

##### Pay In

|  |
| --- |
| Note The data in sample payloads is only for reference and has to be changed as per need before executing. For example - Dates have to be appropriately changed. Organizational data like store has to be appropriately changed for country you are testing. |

<?xml version="1.0" encoding="UTF-8" ?><soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"><soapenv:Body><n0:PosFinancialTransactionsCreateRequest xmlns:n0="http://sap.com/xi/SAPGlobal20/Global">
<MessageHeader>
<CreationDateTime>2021-04-02T12:00:00.1234567Z </CreationDateTime>
<SenderBusinessSystemID><SENDER_SYSID ></SenderBusinessSystemID>
<RecipientBusinessSystemID><RECEIVER_SYSID></RecipientBusinessSystemID>
</MessageHeader>
<PosFinancialTransactions>
<StoreInternalID>3340</StoreInternalID>
<PosFinancialTransaction>
<TransactionType>RPIN</TransactionType>
<TransactionDate>2021-04-04</TransactionDate>
<ExternalReferenceDocumentID>2021-04-05-01</ExternalReferenceDocumentID>
<TransactionInitiatorID>USERID</TransactionInitiatorID>
<Item>
<ItemNumber>1</ItemNumber>
<TotalAmount currencyCode="AED">2300</TotalAmount>
<CostCenter>3340</CostCenter>
</Item>
<Item>
<ItemNumber>2</ItemNumber>
<TotalAmount currencyCode="AED">-2300</TotalAmount>
</Item>
</PosFinancialTransaction>
</PosFinancialTransactions>
</n0:PosFinancialTransactionsCreateRequest>
</soapenv:Body>
</soapenv:Envelope>

##### Pay Out

<?xml version="1.0" encoding="UTF-8" ?>
<soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
<soapenv:Body>
<n0:PosFinancialTransactionsCreateRequest xmlns:n0="http://sap.com/xi/SAPGlobal20/Global">
<MessageHeader>
<CreationDateTime>2021-04-02T12:00:00.1234567Y</CreationDateTime>
<SenderBusinessSystemID><SENDER_SYSID></SenderBusinessSystemID>
<RecipientBusinessSystemID><RECIEVER_SYSID></RecipientBusinessSystemID>
</MessageHeader>
<PosFinancialTransactions>
<StoreInternalID>3340</StoreInternalID>
<PosFinancialTransaction>
<TransactionType>RPOU</TransactionType>
<TransactionDate><Date></TransactionDate>
<ExternalReferenceDocumentID>2021-04-05-02</ExternalReferenceDocumentID>
<TransactionInitiatorID>USERID</TransactionInitiatorID>
<Item>
<ItemNumber>1</ItemNumber>
<TotalAmount currencyCode="AED">2300</TotalAmount>
<CostCenter>3340</CostCenter>
</Item>
<Item>
<ItemNumber>2</ItemNumber>
<TotalAmount currencyCode="AED">-2300</TotalAmount>
</Item>
</PosFinancialTransaction>
</PosFinancialTransactions>
</n0:PosFinancialTransactionsCreateRequest>
</soapenv:Body>
</soapenv:Envelope>

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
- related-to :: [[15-retail-operations/test-script-store-connectivity-outbound-3i2-ae-sap-s-4hana-cloud-publi]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/3HV_S4CLD2608_BPD_EN_AE.docx` — full document · extracted with `mammoth` · 103,411 chars in the whole document
