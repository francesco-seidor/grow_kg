---
id: 13-quality-ehs-and-compliance/test-script-safety-data-sheets-in-the-value-chain-3vq-ae-974
title: "Test Script: Safety Data Sheets in the Value Chain (3VQ_AE) (3VQ_S4CLD2608_BPD_EN_AE)"
description: "SAP S/4HANA Cloud Public Edition test script for scope item 3VQ_AE: safety data sheet checks blocking sales orders and outbound deliveries, UAE (AE) localization."
cluster: 13-quality-ehs-and-compliance
tags: [kb/quality-ehs-and-compliance, topic/safety-data-sheets]
aliases: [3VQ_S4CLD2608_BPD_EN_AE]
keywords: [Safety Data Sheets in the Value Chain, safety data sheets, product compliance, sales order fulfillment, outbound delivery, compliance requests, test scripts, business roles, master data, unpackaged products]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/3VQ_S4CLD2608_BPD_EN_AE.docx]
confidence: high
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-974
topic: 13-quality-ehs-and-compliance/safety-data-sheets
language: EN
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Test Script: Safety Data Sheets in the Value Chain (3VQ_AE) (3VQ_S4CLD2608_BPD_EN_AE)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/3VQ_S4CLD2608_BPD_EN_AE.docx`, extracted with `mammoth`. Grouped under **Safety Data Sheets in the Value Chain** in Quality, EHS and Compliance. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

| <!-- image omitted: unnamed --> | Test ScriptSAP S/4HANA Cloud Public Edition - 19-06-26 |
| --- | --- |
|  | Safety Data Sheets in the Value Chain (3VQ_AE) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Table of Contents

[1 Purpose 2](#_Toc232853733)

[2 Prerequisites 3](#_Toc232853734)

[2.1 System Access 3](#_Toc232853735)

[2.2 Roles 3](#_Toc232853736)

[2.3 Master Data, Organizational Data, and Other Data 4](#_Toc232853737)

[2.4 Business Conditions 5](#_Toc232853738)

[2.5 Additional Configuration 5](#_Toc232853739)

[2.6 Preliminary Steps 5](#_Toc232853740)

[2.6.1 Create Product Master Record and Set Compliance Relevance 5](#_Toc232853741)

[2.6.2 Fill Inventory with Stock 7](#_Toc232853742)

[2.6.3 Create Unpackaged Product 8](#_Toc232853743)

[3 Overview Table 10](#_Toc232853744)

[4 Test Procedures 11](#_Toc232853745)

[4.1 Create Sales Order with a Warning for the Safety Data Sheet Check 11](#_Toc232853746)

[4.1.1 Create Sales Order for a Product Without Prepared Safety Data Sheets 11](#_Toc232853747)

[4.1.2 Optional: Analyze Sales Order Fulfillment Monitor 13](#_Toc232853748)

[4.1.3 Process Request from Sales Order for Safety Data Sheet 14](#_Toc232853749)

[4.2 Create Outbound Delivery with a Warning for the Safety Data Sheet Check 16](#_Toc232853750)

[4.2.1 Create Outbound Delivery for a Non-Compliant Product 16](#_Toc232853751)

[4.2.2 Process Request from Outbound Delivery for Safety Data Sheet 17](#_Toc232853752)

## Purpose

Overview

This scope item covers the main process steps for the maintenance of safety data sheets for products during sales processes.

Products flagged as relevant for compliance must have a completed safety data sheet assessment by the product steward. A missing assessment results in a country-specific automatic block of sales order fulfillment that can be resolved by the product steward, typically by assigning a relevant safety data sheet to the products.

This document provides a detailed procedure for testing this scope item after solution activation, reflecting the predefined scope of the solution. Each process step, report, or item is covered in its own section, providing the system interactions (test steps) in a table view. Steps that are not in scope of the process but are needed for testing are marked accordingly. Project-specific steps must be added.

|  |
| --- |
| Note Values in this test script (decimal notation, date formats, and so on) are presented in U.S. standard notation. If your test system is set up to use a different notation, enter values as appropriate. |

## Prerequisites

This section summarizes all the prerequisites for conducting the test in terms of systems, users, master data, organizational data, other test data and business conditions.

### System Access

| System | Details |
| --- | --- |
| System | Available via SAP Fiori launchpad. Your system administrator provides you with the URL to access the various apps assigned to your role. |

### Roles

Create business roles using the following business role templates delivered by SAP and assign them to your individual test users.

Alternatively, if available, you can use the following spaces delivered by SAP. You create a space with pages containing predefined essential apps and assign it to the business role. You then assign this business role to your individual users.

For more information, refer to How to Create a Business Role from a Template in the [product assistance](https://help.sap.com/docs/SAP_S4HANA_CLOUD/53e36b5493804bcdb3f6f14de8b487dd/ec310a8b669a45ca898dc4dd91d97de2.html) for SAP S/4HANA Cloud Public Edition.

| Name (Role Template) | ID (Role Template) | Name (Launchpad Space) | ID (Launchpad Space) | Log On |
| --- | --- | --- | --- | --- |
| Internal Sales Representative | SAP_BR_INTERNAL_SALES_REP | Internal Sales / Customer Returns / Billing | SAP_BR_INTERNAL_SALES_REP / SAP_SD_SPT_RETURNS_INT_SALES_PC / SAP_SD_SPT_BILLING_INT_SALES_PC |  |
| Product Stewardship Specialist - Product Compliance | SAP_BR_PRODSTWRD_SPLST_PCL | Product Compliance | SAP_BR_PRODSTWRD_SPLST_PCL |  |
| Shipping Specialist | SAP_BR_SHIPPING_SPECIALIST | Shipping | SAP_BR_SHIPPING_SPECIALIST |  |
| Warehouse Clerk | SAP_BR_WAREHOUSE_CLERK | Inventory Processing | SAP_BR_WAREHOUSE_CLERK |  |
| Master Data Specialist - Product Data | SAP_BR_PRODMASTER_SPECIALIST | Master Data - Products / Product Governance | SAP_BR_PRODMASTER_SPECIALIST / SAP_CMD_SPT_PR_GOV_PC |  |

### Master Data, Organizational Data, and Other Data

The organizational structure and master data of your company has been created in your system during activation. The organizational structure reflects the structure of your company. The master data represents materials, customers, and suppliers, for example, depending on the operational focus of your company.

|  |
| --- |
| Caution Update Behavior of Predelivered Demo DataIn non-productive environments (such as starter systems, sandbox systems, or partner demo systems), SAP initially deploys demo data for your selected scope. You can use this data to test and evaluate business processes.In a customer system, you can receive new or updated demo data after initial activation with further scope enhancements, provided the existing demo data wasn't changed in an incompatible way. If activation errors occur due to incompatible changes in demo data, you're responsible for resolving them. If you don't resolve the errors within a specific time frame, SAP reserves the right to deactivate demo data in your systems. In this case, you can continue by creating your own demo data. Alternatively, you can request that your systems be reprovisioned if you want to work with predelivered demo data again.In partner systems, you can use the demo data deployed with the initial activation. No additional demo data will be deployed in the system with scope enhancements. You can only create additional demo data manually. |

| Data | Sample Value | Details | Comments |
| --- | --- | --- | --- |
| Product | FGPC01 | Product Number: FGPC01Product Type: FERTProduct Description: Product Compliance Finished GoodCompliance Relevant: Yes | Used for sales order |

| Data | Sample Value | Details | Comments |
| --- | --- | --- | --- |
| Sold-to Party (Customer) | 33100003 | Domestic UAE Customer 3 | Used in sales order and outbound delivery |
| Ship-to Party (Customer) | 33100003 | Domestic UAE Customer 3 | Used in sales order and outbound delivery |
| Payer (Customer) | 33100003 | Customer domestic 03 | Used in sales order and outbound delivery |
| Plant | 3310 | Plant 1 AE | Used in to fill inventory with stock |
| Storage Location | 331A | Std. storage 1 | Used in to fill inventory with stock |

You can find general information on how to create master data objects in the following [Master Data Scripts (MDS)](https://help.sap.com/docs/s4hana-best-practices/s4cld2608-master-data) :

Table 1: Master Data Script Reference

| MDS | Description |
| --- | --- |
| BNT | Create Product Master of Type “Finished Good” |
| BND | Create Customer Master |

### Business Conditions

Before this scope item can be tested, the following business conditions must be met.

| Scope Item ID | Business Condition |
| --- | --- |
| BD9 - Sell from Stock | The scope item of this document is an extension of the BD9 scope item. Therefore, BD9 must be implemented and tested first. |

### Additional Configuration

To use the final safety data sheet generation service, you must establish the connection between the SAP S/4HANA Cloud Public Edition tenant and the central final safety data sheet generation service that is located on the SAP HANA Cloud platform. The communication scenario SAP_COM_1083 must be active.

If the communication scenario SAP_COM_1083 is not active, you have to request the activation. For more information, see SAP Note [2844426](https://me.sap.com/notes/2844426).

### Preliminary Steps

#### Create Product Master Record and Set Compliance Relevance

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

To run through this scope item, you need a unique product master record.

Procedure

| Test Step | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as Master Data Specialist - Product Data. | The SAP Fiori launchpad with the sections and tiles for the role Master Data Specialist - Product Data is displayed. |  |
| 2 | Access App | Open the Manage Product Master Data (F1602) app. | The Manage Product Master Data screen is displayed. |  |
| 3 | Search | Enter the product FGPC01 into the Search field and choose Go to start the search. | Product Compliance Finished Good (FGPC01) is displayed in the hitlist. |  |
| 4 | Select and Copy | Select the entry for Product Compliance Finished Good (FGPC01)and choose Copy. | The Select Organizational Data to Copy dialog is displayed. |  |
| 5 | Select Organizational Data to Copy | Keep the selection for plants and distribution chains and choose OK. | The Create Master Record dialog is displayed. |  |
| 6 | Create Master Record | Change the <Description>, leave all other fields with default values and choose OK. | The Product screen is displayed. |  |
| 7 | Translation | In Descriptions change the translation of field <Product> in the language which is relevant for your scenario. |  |  |
| 8 | Product Compliance Relevance | In Product Compliance verify if Compliance Relevant is set to Yes.If it has a different value change to Yes. | Compliance Relevant is set to Yes. |  |
| 9 | Create | Choose Create.In case a potential duplicate warning appears, choose Create to confirm. | The product master record was created. Your <Description> and the <Product Number> are shown in the header. Note down both:Product Description: _______________Product Number: ______________ |  |

#### Fill Inventory with Stock

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

To run through this scope item, your product needs to be in stock.

Procedure

| Test Step | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad using the role Warehouse Clerk. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access App | Open the app Post Goods Movement (MIGO). | The app opens and the Goods Receipt Purchase Order screen is displayed. |  |
| 3 | Input Movement Type | Make the following entries and choose Enter:First dropdown list: Goods ReceiptSecond dropdown list: Other | The Goods Receipt Other screen is displayed. |  |
| 4 | Input on the Goods Receipt Other Screen: Material Tab | On the Goods Receipt Other screen: Material tab, make the following entry and choose Enter:Material: <Product Number> that you have created in chapter [Create Product Master Record and Set Compliance Relevance](#unique_9) [page ] 5 under Preliminary Steps. |  |  |
| 5 | Input on the Goods Receipt Other Screen: Quantity Tab | On the Goods Receipt Other screen: Quantity tab, make the following entry and choose Enter:Qty in Unit of Entry: <Qty in unit of entry>Unit of Entry: BTNote Make sure to add enough stock to process the sales order and delivery in this scope item. |  |  |
| 6 | Input on the Goods Receipt Other screen: Where Tab | On the Goods Receipt Other screen: Where tab, make the following entries and choose Enter:Goods Movement Type: 561 - Receipt per initial entry of stock balances into unrestricted usePlant: 3310Storage Location: 331A |  |  |
| 7 | Save Your Entries | Choose Post. | A message confirms that the material document has been posted. |  |

#### Create Unpackaged Product

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The Product Stewardship Specialist - Product Compliance creates an unpackaged product.

Procedure

| Test Step | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as Product Stewardship Specialist - Product Compliance. | The SAP Fiori launchpad with the sections and tiles for the role Product Stewardship Specialist - Product Compliance is displayed. |  |
| 2 | Access App | Open Manage Basic Compliance Data - Unpackaged Products (F2641). | The Manage Basic Data – Unpackaged Products screen is displayed. |  |
| 3 | Create | Choose Create. | The New Product dialog is displayed. |  |
| 4 | New Product | Enter <Internal Name>: ______________Select Mixture in the Product Categorization field.Leave all other fields with default values. | The Unpackaged Product - Basic Compliance Data screen is displayed. |  |
| 5 | Save | Choose Save. | Data is saved and the Manage Basic Data – Unpackaged Products screen is shown in display mode. |  |

## Overview Table

This scope item consists of several process steps provided in the table.

|  |
| --- |
| Note If your system administrator has enabled spaces and pages on the SAP Fiori launchpad, the homepage will only contain the essential apps for performing the typical tasks of a business role.You can find all other (searchable) apps not included on the homepage using the search bar ([2434549](https://me.sap.com/notes/2434549)).If you want to personalize the homepage and include the hidden apps, navigate to your user profile and choose App Finder. |

| Process Step | Business Role | App/Transaction | Expected Results |
| --- | --- | --- | --- |
| [Create Sales Order for a Product Without Prepared Safety Data Sheets](#unique_13) [page ] 11 | Internal Sales Representative | Manage Sales Orders (F1873) | The sales order is created. |
| [Optional: Analyze Sales Order Fulfillment Monitor](#unique_14) [page ] 13 | Internal Sales Representative | Sales Order Fulfillment - Analyze and Resolve Issues (F0029A) | The outbound delivery is created. |
| [Process Request from Sales Order for Safety Data Sheet](#unique_15) [page ] 14 | Shipping Specialist | Process Requests from Logistics (F3342) | The delivery is picked. |
| [Create Outbound Delivery for a Non-Compliant Product](#unique_16) [page ] 16 | Shipping Specialist | Create Outbound Delivery - Without Order Reference (VL01NO) | The outbound delivery is created. |
| [Process Request from Outbound Delivery for Safety Data Sheet](#unique_17) [page ] 17 | Product Stewardship Specialist - Product Compliance | Process Requests from Logistics (F3342) | A safety data sheet document exists for each language. The delivery is no longer blocked. |

## Test Procedures

This section describes test procedures for each process step that belongs to this scope item.

### Create Sales Order with a Warning for the Safety Data Sheet Check

#### Create Sales Order for a Product Without Prepared Safety Data Sheets

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The Internal Sales Representative creates a sales order for a finished good. The safety data sheet check verifies for the ship-to country/region if selling is possible.

Procedure

| Test Step | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Internal Sales Representative. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access App | Open Manage Sales Orders (F1873). | The Manage Sales Orders screen is displayed. |  |
| 3 | Create Sales Order | Choose Create then choose Create Sales Order - VA01 . | The screen to create a sales order is displayed. |  |
| 4 | Enter the Order | On the Create Sales Documents screen, make the following entries and choose Continue:Order Type: ORSales Organization: 3310Distribution Channel: 10Division: 00 | The Create Sales Documents screen is displayed. |  |
| 5 | Enter Order Details | On the Create Standard Order: Overview screen, make the following entries:Sold-To Party: 33100003Ship-To Party: 33100003Cust. Reference: <Any customer reference text>Cust. Ref. Date: <Today’s date>Deliver. Plant: 3310 | The screen to maintain the standard order attributes is displayed. |  |
| 6 | Enter Order Item | On the Create Standard Order: Overview screen, make the following entries for the first sales order item:Material: <Product Number> which you have created in chapter [Create Product Master Record and Set Compliance Relevance](#unique_9) [page ] 5 under Preliminary StepsOrder Quantity: 1Un (Sales Unit): BTDouble-click in the row for the sales order item. On the Country/Region tab, if available, enter 00 as the tax code. If there’s no Country/Region tab, navigate back to Create Standard Order: Overview. | The item is added to the standard order. |  |
| 7 | Item Data – mandatory pricing condition | Double-click in the row for the sales order item. On the Condition tab, add a row:CnTy: PPR0Choose Enter.Add an arbitrary numerical amount in the Amount column.Navigate back to Create Standard Order: Overview. | Pricing error resolved and condition type maintained. |  |
| 8 | Save Order | Choose Save. | The order is saved and the order number is shown in the footer.Messages are shown that the safety data sheet is missing for the product and a compliance request has been initiated and the Product Stewardship Specialist will work on this request in chapter [Process Request from Sales Order for Safety Data Sheet](#unique_15) [page ] 14. |  |
| 9 | Display | If you missed to see the standard order number in the footer, choose Display.Make a note of the sales order number: _____________ | The standard order No. is displayed in the field Standard Order. |  |

#### Optional: Analyze Sales Order Fulfillment Monitor

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The Internal Sales Representative analyzes sales documents based on the given issue types. Safety data sheet issues are visualized in the Delivery Issue in Sales Orders issue type.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Internal Sales Representative. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access App | Under Internal Sales - Insights, open the Sales Order Fulfillment - Analyze and Resolve Issues (F0029A) app. | The Sales Order Fulfillment Issues screen is displayed. |  |
| 3 | Search for Safety Data Sheet Issues | Switch the header filter view by choosing the <!-- image omitted: unnamed -->(Compact Filter) icon.Choose Adapt Filters. Select the Safety Data Sheet Status filter attribute, and then choose OK.For the Safety Data Sheet Status filter, select Warning.For the Sales Document filter, enter the sales order ID of the sales order that you have created in [Create Sales Order for a Product Without Prepared Safety Data Sheets](#unique_13) [page ] 11.Confirm the new filter settings by choosing Go. | The list is filtered accordingly. |  |
| 4 | Select the Status Value for Display | Choose the <!-- image omitted: unnamed -->(Settings) icon for the table Sales Documents with Issues.In the Columns tab, select Safety Data Sheet Status if it isn’t already selected, and then choose OK. | The table shows the safety data sheet status for the sales documents.If you can't see the Safety Data Sheet Status column, scroll right. |  |
| 5 | Select the Sales Order | Find the sales order with Delivery Issue in Sales Orders in the Issue column and the sales document number that you have created in step Create Sales Order for a Product Without Prepared Safety Data Sheets, and navigate to the details of this sales order by choosing the <!-- image omitted: unnamed -->(Details) icon. | The Track Sales Orders (F2577) app is displayed. |  |
| 6 | Select Delivery Issue | If there are multiple items in the Fulfillment table, select the Delivery Issue in Sales Orders row. | The sub page of the app visualizes details about the sales order with a delivery issue. |  |
| 7 | Select the Item Status Value for Display | In the Items with Delivery Issues table, choose the <!-- image omitted: unnamed -->(Settings) icon and select Safety Data Sheet Status.If the safety data sheet status isn't displayed, choose Show More per Row. | The table shows the safety data sheet status for the sales item. |  |

#### Process Request from Sales Order for Safety Data Sheet

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The Product Stewardship Specialist - Product Compliance receives the compliance request because the product referenced in the request is not assigned to a compliance view. The specialist processes the request by creating a compliance view for the product and checking if the assigned purpose is sufficient for the sales country.

Procedure

| Test Step | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Product Stewardship Specialist - Product Compliance. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access App | Open the Process Requests from Logistics (F3342) app. | The Process Requests from Logistics screen is displayed. |  |
| 3 | Search for Request | Search the request for the <Product Number> that you have created in chapter [Create Product Master Record and Set Compliance Relevance](#unique_9) [page ] 5 under Preliminary Steps by using the filters. | The list is filtered and only the request for <Product Number> is displayed. |  |
| 4 | Select Request | Choose the request with Sales Order as Source of Request and Safety Data Sheet Management as Request Initiator for processing.Note If the Request Initiator column is not displayed, add it by choosing the Settings button above the list. | A new column opens that displays details for the request and the steps that you need to process to resolve the compliance issue. |  |
| 5 | Create Compliance View | In the Edit Compliance View Assignments step, choose Edit Assignments. | The Manage Basic Compliance Data - Unpackaged Products (F2641) app opens. |  |
| 6 | Assign to Unpackaged Product | In the Manage Basic Compliance Data - Unpackaged Products (F2641) app, search for the <Internal Name> unpackaged product that you have created in chapter [Create Unpackaged Product](#unique_11) [page ] 8 under Preliminary Steps.On the Unpackaged Products tab, choose the <Internal Name> product from the lists.On the Unpackaged Product - Basic Compliance Data screen that opens, choose Edit.In the Assigned Products section, enter the product referenced in the compliance request as Related Products in Product Master.Choose Save. | On the Unpackaged Product - Basic Compliance Data screen, the product referenced in the compliance request is shown as Related Products in Product Master. |  |
| 7 | Compliance Purposes to Verify | In the Assigned Compliance Purposes section, verify that the Product Default Compliance Purpose compliance purpose is assigned. | The Area in the header of the request is derived from the sales order. Based on this information the Product Stewardship Specialist is able to decide if any further purposes need to be assigned to be able to perform an assessment. |  |
| 8 | Navigate Back | After you have saved your entries, navigate back to the Process Requests from Logistics (F3342) app. | The compliance request with its steps is displayed again. |  |

### Create Outbound Delivery with a Warning for the Safety Data Sheet Check

#### Create Outbound Delivery for a Non-Compliant Product

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The Shipping Specialist created a delivery for a finished good. The safety data sheet check verifies for the ship-to country/region if a delivery of this finished good is allowed.

Procedure

| Test Step | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Shipping Specialist. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access App | Open the Create Outbound Delivery - Without Order Reference (VL01NO) app. | The Create Outbound Delivery Without Order Reference screen is displayed. |  |
| 3 | Enter the Order | On the Create Outbound Delivery Without Order Reference screen, make the following entries and choose Continue:Shipping Point: 3310Delivery Type: LOSales Organization: 3310Distribution Channel: 10Division: 00 | The Delivery w/o Ref. Create: Overview screen is displayed. |  |
| 4 | Enter Delivery Details | On the Delivery w/o Ref. Create: Overview screen, make the following entries:Ship-To Party: 33100003Planned GI: <Today’s date> |  |  |
| 5 | Enter Delivery Item | On the Delivery w/o Ref. Create: Overview screen, make the following entry for the first delivery item:Material: <Product Number> that you have created in chapter [Create Product Master Record and Set Compliance Relevance](#unique_9) [page ] 5 under Preliminary StepsDeliv. Qty: 1Un (Sales Unit): BT | The item is added to the delivery.You may receive an error or warning message due to missing assessments, for example, for dangerous goods. |  |
| 6 | Save Delivery | Choose Save.Make a note of the Delivery: _____________ | The delivery is saved and the delivery number is shown in the footer.Messages are shown that the product compliance check was not successful and the document is blocked from further processing.In addition, a compliance request has been initiated and the Product Stewardship Specialist will work on this request in chapter [Process Request from Outbound Delivery for Safety Data Sheet](#unique_17) [page ] 17. |  |

#### Process Request from Outbound Delivery for Safety Data Sheet

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The Product Stewardship Specialist - Product Compliance receives the compliance request because no safety data sheet assessment is released for the product referenced in the request.

Procedure

| Test Step | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Product Stewardship Specialist - Product Compliance. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access App | Open the Process Requests from Logistics (F3342) app. | The Process Requests from Logistics screen is displayed. |  |
| 3 | Search for Request | Search the request for product <Product Number> that you have created in chapter [Create Product Master Record and Set Compliance Relevance](#unique_9) [page ] 5 under Preliminary Steps by using the filters. | The list is filtered and only the requests for <Product Number> are displayed. |  |
| 4 | Select Request | Choose the request with Outbound Delivery as Source of Request and Safety Data Sheet Management as Request Initiator for processing.Note If the Request Initiator column is not displayed, add it by choosing the Settings button above the list. | A new column opens that displays details for the request and the steps that you need to process if you want to resolve the compliance issue. |  |

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
- see-also :: [[13-quality-ehs-and-compliance/assess-dangerous-goods-for-a-product-3fc-ae-test-script-933]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/3VQ_S4CLD2608_BPD_EN_AE.docx` — full document · extracted with `mammoth` · 31,775 chars in the whole document
