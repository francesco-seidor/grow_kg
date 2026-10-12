---
id: 14-maintenance-service-and-projects/service-management-with-advanced-variant-configuration-6gs-ae-test-scr
title: Service Management with Advanced Variant Configuration (6GS_AE) - Test Script (6GS_S4CLD2608_BPD_EN_AE)
description: "SAP S/4HANA Cloud Public Edition test script for scope item 6GS_AE: configurable service products via advanced variant configuration, from quotation to invoice."
cluster: 14-maintenance-service-and-projects
tags: [kb/maintenance-service-and-projects, topic/configurable-service-products]
aliases: [6GS_S4CLD2608_BPD_EN_AE]
keywords: [Configurable Service Products and Advanced Variant…, advanced variant configuration, service quotations, service orders, service confirmation, release for billing, billing documents, configurable service products, business roles, master data]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/6GS_S4CLD2608_BPD_EN_AE.docx]
confidence: high
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-1168
topic: 14-maintenance-service-and-projects/configurable-service-products
language: EN
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Service Management with Advanced Variant Configuration (6GS_AE) - Test Script (6GS_S4CLD2608_BPD_EN_AE)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/6GS_S4CLD2608_BPD_EN_AE.docx`, extracted with `mammoth`. Grouped under **Configurable Service Products and Advanced Variant Configuration** in Maintenance, Service and Projects. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

|  |  |
| --- | --- |
| Service Management with Advanced Variant Configuration (6GS_AE)Purpose PUBLIC 1<!-- image omitted: unnamed --> | Test ScriptSAP S/4HANA Cloud Public Edition - 19-06-26 |
|  | Service Management with Advanced Variant Configuration (6GS_AE) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Table of Contents

[1 Purpose 2](#_Toc232858706)

[2 Prerequisites 3](#_Toc232858707)

[2.1 System Access 3](#_Toc232858708)

[2.2 Roles 3](#_Toc232858709)

[2.3 Master Data, Organizational Data, and Other Data 4](#_Toc232858710)

[2.4 Business Conditions 5](#_Toc232858711)

[3 Overview Table 6](#_Toc232858712)

[4 Test Procedures 7](#_Toc232858713)

[4.1 Create Service Order Quotation with Configurable Service Product Item 7](#_Toc232858714)

[4.2 Create Service Order with Configurable Service Product 9](#_Toc232858715)

[4.2.1 Release Service Order Item 11](#_Toc232858716)

[4.3 Create Service Confirmation and Change Product Configuration 12](#_Toc232858717)

[4.3.1 Release Confirmation for Billing 13](#_Toc232858718)

[4.4 Create Billing Document (Invoice) 14](#_Toc232858719)

[5 Appendix 16](#_Toc232858720)

[5.1 Process Integration 16](#_Toc232858721)

[5.1.1 Preceding Processes 16](#_Toc232858722)

[5.1.2 Succeeding Processes 16](#_Toc232858723)

## Purpose

Overview

With this scope item, customers can configure specific products and materials in service orders, service order templates, and service quotations. Configurable products allow users to select options for the service order item. The options are predefined as characteristics in the product master data before usage.

Prices can vary for different options. The configured options and their prices are visible to the user.

Before you can maintain configurable items, the service order or service order template must be in place. The results of the configuration and the pricing are transferred back to the service order.

This scope item uses advanced variant configuration (AVC).

This document provides a detailed procedure for testing this scope item after solution activation, reflecting the predefined scope of the solution. Each process step, report, or item is covered in its own section, providing the system interactions (test steps) in a table view. Steps that are not in scope of the process but are needed for testing are marked accordingly. Project-specific steps must be added.

|  |
| --- |
| Note Values in this test script (decimal notation, date formats, and so on) are presented in U.S. standard notation. If your test system is set up to use a different notation, enter values as appropriate. |

## Prerequisites

This section summarizes all the prerequisites for conducting the test in terms of systems, users, master data, organizational data, other test data and business conditions.

Testing in a 3-System Landscape

In a 3-system landscape (with SAP Central Business Configuration as your configuration environment), changes to software and business configuration are applied to your systems independently of one another. It is therefore your responsibility to manage the active business configuration in your systems and synchronize configuration data in your SAP S/4HANA Cloud Public Edition system landscape.

For example, synchronization is required after you've enhanced the scope, extended configuration, or adopted new or changed content from content updates or upgrades. For more information, refer to the [product assistance](https://help.sap.com/viewer/b249d650b15e4b3d9fc2077ee921abd0/latest/en-US/6c398c4ae7364af69d3edffe7fdc39f2.html) in the SAP Help Portal.

If you want to use all software features described for the process steps, reports, or items in this document, we recommend the business process configuration expert in your organization has upgraded the configuration content and deployed the configuration data to your system landscape.

You have activated the scope item Service Order Management and Monitoring (3D2) and Service Quotation4GA.

### System Access

|  |  |
| --- | --- |
|  | Details |
| System | Accessible via SAP Fiori launchpad. Your system administrator provides you with the URL to access the various apps assigned to your role. |

### Roles

Create business roles using the following business role templates delivered by SAP and assign them to your individual test users.

Alternatively, if available, you can use the following spaces delivered by SAP. You create a space with pages containing predefined essential apps and assign it to the business role. You then assign this business role to your individual users.

For more information, refer to How to Create a Business Role from a Template in the [product assistance](https://help.sap.com/docs/SAP_S4HANA_CLOUD/53e36b5493804bcdb3f6f14de8b487dd/ec310a8b669a45ca898dc4dd91d97de2.html) for SAP S/4HANA Cloud Public Edition.

| Name (Role Template) | ID (Role Template) | Name (Launchpad Space) | ID (Launchpad Space) | Log On |
| --- | --- | --- | --- | --- |
| Customer Service Manager | SAP_BR_CUSTOMER_SRVC_MGR | Service Management / Service Management – SAP Field Service and Asset Management | SAP_BR_CUSTOMER_SRVC_MGR / SAP_S4CRM_SPT_FSM_PC |  |
| Service Technician - Customer Service | SAP_BR_CUSTOMER_SRVC_TEC | Service Processing | SAP_BR_CUSTOMER_SRVC_TEC |  |
| Billing Clerk | SAP_BR_BILLING_CLERK | Billing | SAP_BR_BILLING_CLERK |  |

### Master Data, Organizational Data, and Other Data

The organizational structure and master data of your company have been created in your system during activation. The organizational structure reflects the structure of your company. Depending on the operational focus of your company, the master data represents materials, customers, and suppliers, for example.

|  |
| --- |
| Caution Update Behavior of Predelivered Demo DataIn non-productive environments (such as starter systems, sandbox systems, or partner demo systems), SAP initially deploys demo data for your selected scope. You can use this data to test and evaluate business processes.In a customer system, you can receive new or updated demo data after initial activation with further scope enhancements, provided the existing demo data wasn't changed in an incompatible way. If activation errors occur due to incompatible changes in demo data, you're responsible for resolving them. If you don't resolve the errors within a specific time frame, SAP reserves the right to deactivate demo data in your systems. In this case, you can continue by creating your own demo data. Alternatively, you can request that your systems be reprovisioned if you want to work with predelivered demo data again.In partner systems, you can use the demo data deployed with the initial activation. No additional demo data will be deployed in the system with scope enhancements. You can only create additional demo data manually. |

Use your own master data or the following sample data to go through the test procedure.

| ID (Role Template) | Sample Value | Details | Comments |
| --- | --- | --- | --- |
| Customer | 33100001 | Domestic UAE Customer 1You must either assign the customer pricing procedure 01 (Procedure 01) or ensure that the customer is not assigned to a pricing procedure.To check the assignment, use business role SAP_BR_BUPA_MASTER_SPECIALIST and access Manage Customer Master Data (F0850A). |  |
| Employee | <employee> | Use the employee ID that is assigned to your user. |  |
| Service product (service) | SRV_01 | Services |  |
| Configurable Service product | CAR-WASH_CONF | Car Wash ConfigurableService product with several characteristics that can be configured in the service order |  |
| Material Variant for configurable Service Product | CAR-WASH_VAR | Car Wash VariantA material variant with a predefined configuration of the configurable product CAR-WASH_CONF |  |
| Sales Org | 3310 | Dom. Sales Org |  |

You can find general information on how to create master data objects in the following [Master Data Scripts (MDS)](https://help.sap.com/docs/s4hana-best-practices/s4cld2608-master-data) .

Table 1: Master Data Script Reference

| MDS | Description |
| --- | --- |
| 3KV | Create Service Product for Service Processes - MDS |
| 5BE | Create Configurable Service Product - MDS |

### Business Conditions

Before you can activate and test scope item Service Management with Advanced Variant Configuration (6GS), the following business conditions must be met.

| Scope Item ID | Business Condition |
| --- | --- |
| 4GA - Service Quotation | Must be activated. |
| 3D2 - Service Order Management and Monitoring | Must be activated. |

## Overview Table

This scope item consists of several process steps. For more information, see the table below.

|  |
| --- |
| Note If your system administrator has enabled spaces and pages on the SAP Fiori launchpad, the homepage will only contain the essential apps for performing the typical tasks of a business role.You can find all other (searchable) apps not included on the homepage using the search bar ([2434549](https://me.sap.com/notes/2434549)).If you want to personalize the homepage and include the hidden apps, navigate to your user profile and choose App Finder. |

Service Order:

| Process Step | Business Role | App/Transaction | Expected Results |
| --- | --- | --- | --- |
| [Create Service Order Quotation with Configurable Service Product Item](#unique_8) [page ] 7 | Customer Service Manager | Manage Service Quotations - Overview (F4251) | A service order template has been created. |
| [Create Service Order with Configurable Service Product](#unique_9) [page ] 9 | Customer Service Manager | Manage Service Orders - To-Do List (F3571A) | A service order has been created. |
| [Release Service Order Item](#unique_10) [page ] 11 | Customer Service Manager | Manage Service Orders - To-Do List (F3571A) | The service order has been released. |
| [Create Service Confirmation and Change Product Configuration](#unique_11) [page ] 12 | Customer Service Manager | Manage Service Orders - To-Do List (F3571A) | A follow-up service confirmation has been created. |
| [Release Confirmation for Billing](#unique_12) [page ] 13 | Customer Service Manager | Release For Billing (F3573) | The confirmation has been released for billing. |
| [Create Billing Document (Invoice)](#unique_13) [page ] 14 | Billing Clerk | Create Billing Documents (F0798) | An invoice (billing document) is created. |

## Test Procedures

This section describes test procedures for each process step that belongs to this scope item.

### Create Service Order Quotation with Configurable Service Product Item

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The customer service manager creates a service quotation with an item for a service product that is configurable and assigns the corresponding variants for the item. Pric-ing is determined dependent on the selected variants.

Prerequisite steps for configuration and the creation of configurable service products are described in Master Data Script 5BE.

Service quotations are used to provide legally binding offers with fixed conditions made to a customer for the performance of services.

Customer Service managers may use quotations to provide cost estimates before placing an order. Both Time and Material (T&M) and Fixed Price cost estimates are sup-ported with validity period. The validity period of the service quotation can be changed by the customer service manager with an option to carry out repricing as per the new validity.

Upon finalizing the service quote with required services and price offered, the customer service manager can either print or generate the quote as a PDF, then attach it to an email to be sent to customer for negotiation.

The service quote can then be set to Accepted or Rejected. Finally, the service quote acceptance triggers the automatic creation of service orders as a follow-on process.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Customer Service Manager. |  |  |
| 2 | Access App | Open Manage Service Quotations - Overview (F4251). | The Manage Service Quotations screen displays. |  |
| 3 | Create Service Quotation | Choose Create Service Quotation > Quick Create . | A Create Service Quotation window displays. |  |
| 4 | Maintain Data | Make the following entries:Service Quotation Type: Service QuotationSold-To Party: for example, 33100003Description:Requested Start Date - End Date: <your description><<date range>Product ID: for example, CAR-WASH_CONFQuantity: for example, 1Unit: for example, AUPress Enter.Choose Save and Edit.Note If you have created a material variant with predefined configuration like CAR-WASH-VAR for this configurable product CAR-WASH_CONF, you can skip the following configuration steps. Material variants are helpful when the same variant of the configurable product is frequently requested. | A new service quotation will be created with a configurable product and status will be set to Open. |  |
| 5 | Adjust the Product Characteristics | On the Items tab in the Actions column, choose Configure Product to navigate to the Variant Configuration.In the Default Group section, select the following variants using the input help:CAR SIZE: LargeCAR WASH TYPE : Premium WashEXTRA POLISH: YesChoose Done. | All variants for the characteristics are maintained. The Net Value field is automatically calculated according to the prices for the selected variants.The configuration status is set to Released. |  |
| 6 | Save | Choose Save. | A new service quotation is created.Your new service quotation is displayed in the Manage Service Quotations - Overview (F4251) app. |  |
| 7 | Accept Service Quotation | Choose Accept. | The service quotation is accepted.Note The accepted service quote will automatically create a service order internally. Note down the service order number. |  |

### Create Service Order with Configurable Service Product

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The customer service manager creates a service order with an item for a service product that is configurable and assigns the corresponding variants for the item. Pricing is determined dependent on the selected variants.

Prerequisite steps for configuration and the creation of configurable service products are described in Master Data Script 5BE.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Customer Service Manager. |  |  |
| 2 | Access App | Open Manage Service Orders - To-Do List (F3571A). | The Manage Service Orders screen displays. |  |
| 3 | Create Service Order | Choose Create Service Order > Create .In the Service Order Type dialog box, choose Service Order from the service order type list. | The Service Order : New view displays. |  |
| 4 | Maintain Data | Make the following entries:Description: <your description>Sold-To Party: for example, 33100001 forChoose Enter.If contact persons are displayed in a Partner Selection Document Header dialog box, select one of them.If teams are displayed in a Select Service Team for Header dialog box, select the relevant service team.If your sold-to-party is associated with one or more service contracts, a dialog box Contract Assignment will be displayed for selecting a contract per item. Select No Assignment.Product ID: for example, CAR-WASH_CONFQuantity: for example, 1Unit: for example, AUPress Enter.Note If you have created a material variant with predefined configuration like CAR-WASH_VAR for this configurable product CAR-WASH_CONF, you skip the following configuration steps. Material variants are helpful when the same variant of the configurable product is frequently requested. | A message is displayed:Item 10: configure product CAR-WASH_CONF |  |
| 5 | Adjust the Product Characteristics | In the Actions column, choose Configure Product to navigate to the Service Order New Variant Configuration view.In the Default Group section, select the following variants using the input help:CAR SIZE: LargeCAR WASH TYPE : Premium WashEXTRA POLISH: YesChoose Done. | All variants for the characteristics are maintained. The Net Value field is automatically calculated according to the prices for the selected variants.The configuration is set to Released. |  |
| 6 | Check Price Details. | In the Service Order : New view, choose Price – Details.Check the End Value for the Price Element for the following variants:CAR SIZE: LargeCAR WASH TYPE: PremiumEXTRA POLISH: YesNote If you have created a Fixed Price Service Order, choose the action Add to insert a new Price Element:Select Price Element Manual Doc. Amount (Price Element ID = PMV0)Enter a Price value for this Price Element, for example, 80AED.Choose Enter. | The end values for all price elements are calculated and displayed. |  |
| 7 | Save | Choose Save. | A service order has been created.Take a note of the service order ID.Your service order is displayed in the Manage Service Orders - To-Do List (F3571A) app. |  |

#### Release Service Order Item

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, the configured service item of the previously created service order is released, as a prerequisite for the follow-up confirmation.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Customer Service Manager. |  |  |
| 2 | Access App | Open Manage Service Orders - To-Do List (F3571A). | The Manage Service Orders screen displays. |  |
| 3 | Find Service Order | Make the following entires and choose Go:Description: <descritpion>Alternatively, search for the ID of your service order. | Your service order is displayed. |  |
| 4 | Open Service Order | Choose Edit for the service order. | The view Service Order:<Description> is displays. |  |
| 5 | Release Service Item. | Choose the Items tab, or scroll down to the Items area.Choose Release All Items.In the Status column, the status value of the CAR_WASH_CONFIG service item changes from Open to Released.Choose Save. | The service item is released. |  |

### Create Service Confirmation and Change Product Configuration

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, a follow-up service confirmation is created. It includes changing a configurable product using the advanced variant configuration, setting the confirmation to completed, and defining the confirmation as the final confirmation for the service order.

Choosing the Final Confirmation checkbox sets the service confirmation to completed, which is the prerequisite for triggering the billing document request.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Customer Service Manager or as a Service Technician - Customer Service. |  |  |
| 2 | Access App | Open Manage Service Orders - To-Do List (F3571A) or Process Service Orders - To-Do List (F4230), depending on the role you are using. | The list report page is displayed. |  |
| 3 | Find Service Order | Make the following entires and choose Go:Description: <descritpion>Alternatively, search for the ID of your service order. | Your service order is displayed. |  |
| 4 | Display Service Order Details | Choose the service order ID in the report list. | The service order is displayed. |  |
| 5 | Create Service Confirmation | Choose Created Follow-up > Create Service Confirmation. | The Create Service Confirmation view is displayed. |  |
| 6 | Maintain Data | Make the following entries:Enter a description.Final Confirmation Selected.(Final Confirmation: Yes)Choose theExec. Service Employee, for example, 9980000xxx.In the service confirmation, select the products from your service order and enter the quantity for each service order item:Product ID: for example, CAR-WASH_CONF.Quantity: for example, 1Choose Save and Edit. | The edit view of the service confirmation is displayed.The configurable products can be selected. |  |
| 7 | View Details | Choose the Items tab or scroll down to the Items area.Choose Edit.In the Actual Duration field, enter a duration, for example 1 Hour.Choose Back. | The details view of the service item is displayed. |  |
| 8 | Adjust Characteristics | Choose Configure Product.The Service Confirmation: XXXXXX - Variant Configuration view is displayed. You can change the product characteristics as required.Choose Done. | The service item price has changed, depending on the product configuration changes. |  |
| 9 | Complete Service Confirmation | Change the Life Cycle Status to Completed.Ensure that the Final Confirmation checkbox has been selected and choose Save. | The service confirmation is set to completed. Changing the service confirmation is no longer possible. If required, you can cancel the service confirmation.In addition, the life-cycle status of the related service order is automatically set to completed . Setting the service order to completed is the prerequisite for releasing the service items for billing. |  |

#### Release Confirmation for Billing

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The Service manager releases the items of the confirmation for billing.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Customer Service Manager. |  |  |
| 2 | Access App | Open Release For Billing (F3573). | The Release For Billing screen displays. |  |
| 3 | Find Service Confirmation | Enter the ID of your service confirmation in the Search field and choose Go. | All items of the respective service confirmation that have been confirmed and completed in the service order, are displayed in the result list.If you've created a fixed price service order (SVO2), the invoice has been created for the service order. In this case, search for the relevant service order and release for billing. |  |
| 4 | Release Service Item | Select the corresponding service item and choose Release for Billing. | The service item containing the configurable product is released for billing.If an error occurs, a popup containing an error list is returned.The billing document request is been created. |  |

### Create Billing Document (Invoice)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, the billing clerk creates an invoice for the service confirmation items that have been released for billing in the previous step. The invoice or billing document is created by the billing clerk.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment. |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to The SAP Fiori launchpad as a Billing Clerk. |  |  |
| 2 | Access App | Open Create Billing Documents (F0798). | The Create Billing Documents (F0798) view with the Billing Due List Items list is displayed. |  |
| 3 | Define the Billing Settings | In the Create Billing Documents (F0798) view, choose Billing Settings in the bottom bar (next to the Create button).On the Billing Settings dialog window, maintain the following settings:Set billing date and type before billing: ON.Create separate billing document for each item of billing due list: OFF.Automatically post billing documents: ON.Display billing documents after creation: ONChoose OK. | The Billing Settings dialog window is displayed.You have maintained the required settings for billing. |  |
| 4 | Select Items for Billing | Maintain the following search criteria:SD Document Category: <Billing Document Request>In order to better find your items to be billed, choose the Settings icon.In View Settings select the BDR Source Document field for display.Choose OK and search for your items in the list by identifying your service confirmation in the BDR Source Document field.In the Billing Due List Items list, select the row(s) of billing document requests created for your service confirmation items. Then choose Create Billing Documents.Note If you don’t want to display all billing due list items, you can restrict the list display by applying search criteria such as Sold-to-Party or Billing Date. | The Create Billing Documents dialog box is displayed. |  |
| 5 | Select Billing Type and Date | In the Create Billing Documents dialog box, choose the following values:Billing Type: F2 Invoice (F2)Billing Date: <today’s date>Then choose OK. | The Invoice view is displayed. |  |
| 6 | Save | In the Invoice screen, choose Save.The billing document with ID xxxxxxxx is created. Make a note of the billing document number for further reference. | A billing document has been created. |  |

## Appendix

### Process Integration

The process to be tested in this test script is part of a chain of integrated processes.

#### Preceding Processes

The following processes and conditions can precede this process.

| Scope Item | Business Condition |
| --- | --- |
| 4GT - Solution Order Management | Optional |

#### Succeeding Processes

After completing the activities in this test script, you can continue testing the following business processes:

| Process | Business Condition |
| --- | --- |
| 43B - Service Monitoring and Analytics | Optional |
| 4GG - Credit and Debit Memo Processing for Service Management | Optional |
| J59 - Accounts Receivable |  |
| 3M3 - Event-Based Revenue Recognition – Service Documents |  |
| 3M4 - Event-Based Revenue Recognition – Service Documents – IFRS |  |
| 3M5 -Event-Based Revenue Recognition – Service Documents – US GAAP |  |

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
- related-to :: [[14-maintenance-service-and-projects/criar-produto-de-servico-configuravel-mds-5be-script-de-dados-mestre-s]]
- related-to :: [[14-maintenance-service-and-projects/master-data-script-create-configurable-service-product-mds-5be-431]]
- related-to :: [[14-maintenance-service-and-projects/mds-5be-master-data-script-create-configurable-service-products-435]]
- related-to :: [[14-maintenance-service-and-projects/sap-s-4hana-cloud-public-edition-mds-5be-433]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/6GS_S4CLD2608_BPD_EN_AE.docx` — full document · extracted with `mammoth` · 30,082 chars in the whole document
