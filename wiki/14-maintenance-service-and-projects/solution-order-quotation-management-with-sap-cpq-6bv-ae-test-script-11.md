---
id: 14-maintenance-service-and-projects/solution-order-quotation-management-with-sap-cpq-6bv-ae-test-script-11
title: Solution Order Quotation Management with SAP CPQ (6BV_AE) - Test Script (6BV_S4CLD2608_BPD_EN_AE)
description: "SAP S/4HANA Cloud Public Edition 2608 test script for scope item 6BV: create a quotation in SAP CPQ and display the resulting solution order."
cluster: 14-maintenance-service-and-projects
tags: [kb/maintenance-service-and-projects, topic/solution-orders-and-cpq]
aliases: [6BV_S4CLD2608_BPD_EN_AE]
keywords: [Solution Orders and SAP CPQ Quotations, sap cpq quotation, solution order management, test scripts, business roles, master data, configurable products, service contracts, business conditions, three-system landscape]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/6BV_S4CLD2608_BPD_EN_AE.docx]
confidence: high
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-1164
topic: 14-maintenance-service-and-projects/solution-orders-and-cpq
language: EN
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Solution Order Quotation Management with SAP CPQ (6BV_AE) - Test Script (6BV_S4CLD2608_BPD_EN_AE)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/6BV_S4CLD2608_BPD_EN_AE.docx`, extracted with `mammoth`. Grouped under **Solution Orders and SAP CPQ Quotations** in Maintenance, Service and Projects. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

|  |  |
| --- | --- |
| Solution Order Quotation Management with SAP CPQ (6BV_AE)Purpose PUBLIC 1<!-- image omitted: unnamed --> | Test ScriptSAP S/4HANA Cloud Public Edition - 19-06-26 |
|  | Solution Order Quotation Management with SAP CPQ (6BV_AE) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Table of Contents

[1 Purpose 2](#_Toc232858512)

[2 Prerequisites 3](#_Toc232858513)

[2.1 System Access 3](#_Toc232858514)

[2.2 Roles 3](#_Toc232858515)

[2.3 Master Data, Organizational Data, and Other Data 4](#_Toc232858516)

[2.3.1 Additional Manual Configuration 5](#_Toc232858517)

[2.4 Business Conditions 6](#_Toc232858518)

[3 Preliminary Steps 7](#_Toc232858519)

[4 Overview Table 8](#_Toc232858520)

[5 Test Procedures 9](#_Toc232858521)

[5.1 Create Quotation in SAP CPQ 9](#_Toc232858522)

[5.2 Display Solution Order in SAP S/4HANA Cloud Public Edition 11](#_Toc232858523)

## Purpose

Overview

This scope item enables seamless data integration between SAP S/4HANA Cloud Public Edition and SAP CPQ. You can create customer and product master data in SAP S/4HANA Cloud Public Edition (including pricing). You can then use this data in SAP CPQ to create a quotation for physical products (including single-level configurable products) and service contract products (including configurable service contract products). After the customer accepts the quote, you can send it to SAP S/4HANA Cloud Public Edition. A solution order is created to capture the order. Follow-up documents such as a sales order and service contract are automatically triggered from the solution order creation.

This document provides a detailed procedure for testing this scope item after solution activation, reflecting the predefined scope of the solution. Each process step, report, or item is covered in its own section, providing the system interactions (test steps) in a table view. Steps that are not in scope of the process but are needed for testing are marked accordingly. Project-specific steps must be added.

|  |
| --- |
| Note Values in this test script (decimal notation, date formats, and so on) are presented in U.S. standard notation. If your test system is set up to use a different notation, enter values as appropriate. |

## Prerequisites

This section summarizes all the prerequisites for conducting the test in terms of systems, users, master data, organizational data, other test data and business conditions.

Testing in a 3-System Landscape

In a 3-system landscape (with SAP Central Business Configuration as your configuration environment), changes to software and business configuration are applied to your systems independently of one another. It is therefore your responsibility to manage the active business configuration in your systems and synchronize configuration data in your SAP S/4HANA Cloud Public Edition system landscape. A synchronization is required, for example, after you've enhanced the scope, extended configuration, or adopted new or changed content from content updates or upgrades. For more information, refer to [Settings via SAP Central Business Configuration](https://help.sap.com/docs/SAP_S4HANA_CLOUD/b249d650b15e4b3d9fc2077ee921abd0/6c398c4ae7364af69d3edffe7fdc39f2.html).

Before testing, if you want to use all software features described for the process steps, reports, or items in this document, we recommend the Business Process Configuration Expert in your organization has upgraded the configuration content and deployed the configuration data to your system landscape.

If the decision is not to upgrade the configuration content in your test or production system, you can run regression tests of software changes using the procedures in the previous test script version (see the following link ).

### System Access

The test should be conducted with the following system:

| System | Details |
| --- | --- |
| SAP S/4HANA Cloud Public Edition | Accessible via SAP Fiori Launchpad. Your system administrator provides you with the URL to access the various apps assigned to your role. |
| SAP CPQ | Your system administrator provides you with the URL and related credentials for the user type, Sales. |

|  |
| --- |
| Note For system details, contact your system administrator. |

### Roles

Create business roles using the following business role templates delivered by SAP and assign them to your individual test users.

Alternatively, if available, you can use the following spaces delivered by SAP. You create a space with pages containing predefined essential apps and assign it to the business role. You then assign this business role to your individual users.

For more information, refer to How to Create a Business Role from a Template in the [product assistance](https://help.sap.com/docs/SAP_S4HANA_CLOUD/53e36b5493804bcdb3f6f14de8b487dd/ec310a8b669a45ca898dc4dd91d97de2.html) for SAP S/4HANA Cloud Public Edition.

For more information, refer to [How to Create a Business Role for the Administrator](https://help.sap.com/viewer/a630d57fc5004c6383e7a81efee7a8bb/latest/en-US/8fa28e0107984d42a99b9eea67856cea.html) for SAP S/4HANA Cloud Public Edition.

| Name (Role Template) | ID (Role Template) | Name (Launchpad Space) | ID (Launchpad Space) | Log On |
| --- | --- | --- | --- | --- |
| Solution Order Specialist | SAP_BR_SOLN_ORDER_SPCLST | Solution Order Management | SAP_BR_SOLN_ORDER_SPCLST | Your system administrator provides the user and password information. |
| Internal Sales Representative | SAP_BR_INTERNAL_SALES_REP | Internal Sales / Customer Returns / Billing | SAP_BR_INTERNAL_SALES_REP | Your system administrator provides the user and password information. |
| Shipping Specialist | SAP_BR_SHIPPING_SPECIALIST | Shipping | SAP_BR_SHIPPING_SPECIALIST | Your system administrator provides the user and password information. |
| Customer Service Manager | SAP_BR_CUSTOMER_SRVC_MGR | Service Management / Service Management – SAP Field Service and Asset Management | SAP_BR_CUSTOMER_SRVC_MGR | Your system administrator provides the user and password information. |
| Billing Clerk | SAP_BR_BILLING_CLERK | Billing | SAP_BR_BILLING_CLERK | Your system administrator provides the user and password information. |

### Master Data, Organizational Data, and Other Data

The organizational structure and master data of your company has been created in your system during activation. The organizational structure reflects the structure of your company. The master data represents materials, customers, and vendors, for example, depending on the operational focus of your company.

Use your own master data or the following sample data to go through the test procedure.

| Data | Sample Value | Details | Comments |
| --- | --- | --- | --- |
| Customer | 17100066 for US | Domestic US Customer 66 | Ensure that the customer you use for this process has either assigned the customer pricing procedure ZR (Pricing procedure used in the determination).To check the assignment, use the business role SAP_BR_BUPA_MASTER_SPEC and go to Sales Area Data > Manage Customer Master Data . |
| Customer | 10100066 for DE | Domestic DE Customer 66 | Ensure that the customer you use for this process has either assigned the customer pricing procedure ZR (Pricing procedure used in the determination).To check the assignment, use the business role SAP_BR_BUPA_MASTER_SPEC and go to Sales Area Data > Manage Customer Master Data . |
| Employee | - | <Use your own employee ID assigned to your User ID.> |  |
| Material | TG11 | Sales Product |  |
| Material | SRV_CONTRACT | Service Contract Product | SRV_CONTRACT is also used for price adaption. When creating service contracts with SRV_CONTRACT for price adaption, you must switch the item category from service contract product to Pri. Adptn. |
| Material | CM-FL-V00 | Confiurable Sales Prod-uct | Configuration of this product is explained in scope item 1YT. |
| Material | SRV_CONTR_CONFIG | Configurable Service Product for Contracts | Configuration of this product is explained in scope item 5BE. |
| Sales Organization | 1710 for US and 1010 for DE | Dom. Sales Org |  |
| Company Code | 1710 for US and 1010 for DE | Company Code 1710 for US and Company Code 1710 for DE |  |
| Plant | 1710 for US and 1010 for DE | Plant 1 US for US and Plant 1 DE for DE |  |

For more information on creating master data objects, see the following [Master Data Scripts (MDS)](https://help.sap.com/docs/s4hana-best-practices/s4cld2608-master-data) .

Table 1: Master Data Script Reference

| Master Data ID | Description |
| --- | --- |
| 3KV | Create Service Product for Service Processes - MDS |
| BNF | Create Product Master of type "Trading Good" - MDS |
| BND | Create Customer Master - MDS |
| 1YT | Make-to-Order Production with Variant Configuration |
| 5BE | Create Configurable Service Product - MDS |

#### Additional Manual Configuration

Before you can test this scope item, you must have completed the additional configuration steps that are described in the Set-Up Instructions for this scope item. These configuration steps are specific for your implementation and include mandatory settings that are not delivered by SAP and must be created by you. For more information, follow the link to the document:

[Link to Set-Up Instructions](https://help.sap.com/docs/SAP_S4HANA_BEST_PRACTICES/ff412ebded75a07eecbb0c4c731bd8b8)

### Business Conditions

Before this test script can be tested, the following business conditions must be met:

| Scope Item | Business Condition |
| --- | --- |
| 4GT - Solution Order Management | To run through this test script, the solution order process has to be in place in the SAP S/4HANA Cloud Public Edition system. |
| 6HY - Solution Order Management with Advanced Variant Configuration | To run through this test script, the solution order process with Advanced Variant Configuration has to be in place in the SAP S/4HANA Cloud Public Edition system. |

## Preliminary Steps

N/A

## Overview Table

This process variant starts with the creation of a quotation in SAP CPQ. IF your system administrator has enabled spaces and pages on the SAP Fiori Launchpad, the homepage will only contain the essential apps for performing the typical tasks of a business role.

You can find all other apps, not included on the homepage, using the search bar. If you want to personalize the homepage and include the hidden apps, navigate to your user profile and choose App Finder.

| Process Step | Business Role | App/Transaction | Expected Results |
| --- | --- | --- | --- |
| [Create Quotation in SAP CPQ](#unique_10) [page ] 9 | User type - Sales in SAP CPQ | - | SAP CPQ quote is created |
| [Display Solution Order in SAP S/4HANA Cloud Public Edition](#unique_11) [page ] 11 | Solution Order Specialist | Manage Solution Order | Solution order is validated |

## Test Procedures

This section describes test procedures for each process step that belongs to this scope item.

### Create Quotation in SAP CPQ

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This step describes how to create a new SAP CPQ Quote and add items (sales, configurable sales, service contract and configurable service contract items) to it.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On to SAP CPQ | Logon to SAP CPQ with user created with User Type Sales. | SAP CPQ is launched with Catalog open. |  |
| 2 | Create a Quotation in SAP CPQ | Choose New Project/Quotation icon. | Create Quotation window is displayed. |  |
| 3 | Maintain Quote Info Data | Ensure that the following details are entered in the Quote Info section under the Quotation tab:Status: PreparingMarket: Market created in SAP CPQ that corresponds to the sales organisation of SAP S/4HANA Cloud Public Edition, for example <Dom. Sales Org US>Pricebook: Pricebook created in SAP CPQ that corresponds to a distribution channel of SAP S/4HANA Cloud Public Edition, for example, <Dom Sales Org US Pricebook>Effective Date: <today>Revision: Master(Active) | Required Quote Info details are maintained. |  |
| 4 | Add PO Number | Navigate to Additional Info tab and enter a value, for example <12345> in PO Number.Choose Save. | PO Number is added. |  |
| 5 | Add Involved Parties | Navigate to Involved Parties tab and choose a Business partner for Sold-to party, for example, <Domestic US Customer 1>Choose Save.NoteIf Sold-to party is not listed under Involved Parties, Choose Add Existing Business Partner., select Partner Function, as <Sold-to party> and add a Business partnerUse the Business Partner ID, for example, <17100001> from SAP S/4HANA Cloud Public Edition in External ID to search for Business Partners. | Involved Parties are added. |  |
| 6 | Add Sales Item to Quotation | Navigate to Quotation tab, in Products section, enter Sales Item TG11 in Add Items.Once the product is displayed, maintain quantity, for example, <1> and choose Add. | Sales Item is added to the SAP CPQ Quotation. |  |
| 7 | Add Service Contract Items | Navigate to Quotation tab,in Products section, enter Service Contract Item, SRV_CONTRACT in Add Items.Once the product is displayed, maintain quantity, for example, <1> and choose Configure.Maintain the following details to configure the product:Select Service Profile: For example, <Mo-Fr: 7-17h>Select Response Profile: For example, <First Level Response Time>Select Service Contract Duration:For example, <1 Year>Select Settlement Period: For example, <Monthly>Select Billing Date: For example, <First of the Month>Choose Add to Quote. | Service Contract Item is added to the SAP CPQ Quotation. |  |
| 8 | Add Configurable Items | Navigate to Quotation tab,in Products section, enter Configurable Item, CM-FL-V00 in Add Items.Once the product is displayed, maintain quantity, for example, <1> and choose Configure.Maintain the following details to configure the product:Select Lifter Model For example, <Heavy>Select Power Source: For example, <Combustion>Select Wheel Type:For example, <Cushion Tyres>Select Counterweight: For example, <1.000>Select Fork Size: For example, <Small>Choose Add to Quote. | Configurable Item is added to the SAP CPQ Quotation. |  |
| 9 | Add Configurable Service Product for Contracts | Navigate to Quotation tab, in Products section, enter Configurable Service Product for Contracts, SRV_CONTR_CONFIG in Add Items.Once the product is displayed, maintain quantity, for example, <1> and choose Configure.Maintain the following details to configure the product:Select Service Profile: For example, <Mo-Fr: 7-17h>Select Response Profile: For example, <First Level Response Time>Select Service Contract Duration:For example, <1 Year>Select Settlement Period: For example, <Monthly>Select Billing Date: For example, <First of the Month>Select Service Channel: For example, <E-mail Support>Select Preventive Maintenance: For example, <Yearly>Choose Add to Quote. | Configurable Service Product for Contracts is added to the SAP CPQ Quotation. |  |
| 10 | Add Discount | In the Products section of Quotation tab, enter Discount Percent under One-Time for Sales or Configurable products, for example as <-10>In the Products section of Quotation, enter Discount Percent under Recurring for Service Contracts or Configurable Service Product for Contracts, for example, <-10>. | Discount is added. |  |
| 11 | Place Quotation | Navigate to Quotation > Actions > Place Order.Choose Yeson the ConfirmationStatus under Quote Info section changes to Order Confirmation Pending. The Status changes to Order Placed.Note the Quote# and Sales Order IDNote The change of Status might take 15-30 seconds.Refresh the page for the updated Status. | The Order is Placed. |  |

### Display Solution Order in SAP S/4HANA Cloud Public Edition

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This step describes how to display the new solution order created with line items (sales, configurable sales, service contract, configurable service contract items).

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad using the role Solution Order Specialist. | The Fiori Launchpad with access to the Manage Solution Orders application is displayed. |  |
| 2 | Open the Manage Solution Orders App | Choose the Manage Solution Orders app. | The list report page is displayed. |  |
| 3 | Open the Solution Order Window | Search for the Sales Order ID noted from SAP CPQ in the Solution Order field. Choose Go and select the solution order. | Solution Order window is displayed. |  |
| 4 | Display Solution Order Data | Check the following data in the created solution order:Description: Quote# from SAP CPQSold-To Party: for example, <Domestic US Customer 1>External Reference: The value maintained as PO Number in SAP CPQ for example, <12345> | Header data is displayed. |  |
| 5 | Display Sales Item Details | Check the following Sales Item details in the solution order as maintained in SAP CPQ.Product ID: for example, <TG11>(Trading Good 11)Quantity: for example, <1>Unit: for example, <PC>Net Value: for example, <18.50> (Amount from CPQ, Quotation > Products > TG11 > Extended Amount > One-Time)Note Refer to topics from Release Solution Order Line Items for Sales Item in Solution Order Management (4GT) test script for further details. | Sales Item details are displayed. |  |
| 6 | Display Configurable Sales Item Details | Check the following Configurable Sales Item details in the solution order as maintained in SAP CPQ.Product ID: for example, <CM-FL-V00>(Forklift)Quantity: for example, <1>Unit: for example, <PC>Net Value: for example, <8,000.00> (Amount from CPQ, Quotation > Products > CM-FL-V00 > Extended Amount > One-Time)Note Refer to topics from Release Solution Order Line Items for Configurable Sales Item in Solution Order Management (4GT) test script for further details. | The Configurable Sales Item details are displayed. |  |
| 7 | Display Service Contract Items | Check the following Service Contract Items in the solution order as maintained in SAP CPQ:Product ID: for example, SRV_Contract (Service Contract Item)Quantity: for example, <1>Unit: for example, <AU>Net Value: for example, <8,000.00> (Amount from CPQ, Quotation > Products > SRV_CONTRACT > Extended Amount > Recurring multiplied by duration in months)Note Refer to topics from Release Solution Order Line Items for Service Contract Item in Solution Order Management (4GT) test script for further details. | The Service Contract Item details are displayed. |  |
| 8 | Display Configurable Service Product for Contracts | Check the following Configurable Service Contract Item in the solution order as maintained in SAP CPQ:Product ID: for example, SRV_CONTR_CONF (Configurable Service Contract)Quantity: for example, <1>Unit: for example, <AU>Net Value: for example, <8,000.00> (Amount from Quotation > Products > SRV_CONTR_CONF > Extended Amount > Recurring multiplied by duration in months)Note Refer to topics from Release Solution Order Line Items for Configurable Service Contract Items in Solution Order Management with Advanced Variant Configuration (6HY) test script for further details. | The Configurable Service Contract Item details are displayed. |  |
| 9 | Display Discount | Choose the product for which the discounts are maintained in SAP CPQ. Go to Price Details and check for the percentage discount maintained under the correct Price element ID. | Discounts are displayed. |  |

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
- related-to :: [[14-maintenance-service-and-projects/creacion-de-producto-de-servicio-para-proyecto-mds-5to-486]]
- related-to :: [[14-maintenance-service-and-projects/criar-produto-de-servico-para-projeto-mds-5to-488]]
- related-to :: [[14-maintenance-service-and-projects/master-data-script-create-service-product-for-project-5to-485]]
- related-to :: [[14-maintenance-service-and-projects/mds-5to-487]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/6BV_S4CLD2608_BPD_EN_AE.docx` — full document · extracted with `mammoth` · 22,717 chars in the whole document
