---
id: 10-procurement/sap-ariba-buying-4ai-1009
title: SAP Ariba Buying (4AI) (4AI_S4CLD2608_BPD_EN_XX)
description: "SAP S/4HANA Cloud Public Edition test script for scope item 4AI, SAP Ariba Buying: purchase request through approval, purchase order, goods receipt and supplier invoice."
cluster: 10-procurement
tags: [kb/procurement, topic/ariba-buying]
aliases: [4AI_S4CLD2608_BPD_EN_XX]
keywords: [SAP Ariba Buying Purchase Requests, sap ariba buying, purchase requests, purchase request approval, purchase requisition to order, purchase order approval, goods receipt, supplier invoices, user profile, business roles]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/4AI_S4CLD2608_BPD_EN_XX.docx]
confidence: low
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-1009
topic: 10-procurement/ariba-buying
language: EN
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# SAP Ariba Buying (4AI) (4AI_S4CLD2608_BPD_EN_XX)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/4AI_S4CLD2608_BPD_EN_XX.docx`, extracted with `mammoth`. Grouped under **SAP Ariba Buying Purchase Requests** in Procurement. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

| <!-- image omitted: unnamed --> | Test ScriptSAP S/4HANA Cloud Public Edition - 19-06-26 |
| --- | --- |
|  | SAP Ariba Buying (4AI) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Table of Contents

[1 Purpose 2](#_Toc232840705)

[2 Prerequisites 3](#_Toc232840706)

[2.1 System Access 3](#_Toc232840707)

[2.2 Roles 3](#_Toc232840708)

[2.3 Additional Manual Configuration 4](#_Toc232840709)

[2.4 Preliminary Steps 4](#_Toc232840710)

[2.4.1 Maintain BTP User Profile 4](#_Toc232840711)

[3 Overview Table 6](#_Toc232840712)

[4 Test Procedures 7](#_Toc232840713)

[4.1 Access the Landing Page 7](#_Toc232840714)

[4.2 Create Purchase Request 7](#_Toc232840715)

[4.3 Review Your Purchase Request 9](#_Toc232840716)

[4.4 Approve Purchase Request 11](#_Toc232840717)

[4.5 Convert Purchase Requisitions to Purchase Orders 12](#_Toc232840718)

[4.6 Approve Purchase Order (Optional) 13](#_Toc232840719)

[4.7 Goods Receipt for Purchase Order 14](#_Toc232840720)

[4.8 Create Supplier Invoice 15](#_Toc232840721)

## Purpose

Overview

SAP Ariba Buying creates a simple, smart, and elegant purchasing experience that increases user engagement across all spend areas for indirect material procurement. SAP Ariba Buying serves as a central place where you as a buyer can find items across catalogs and shop goods. All spend contracted through supplier-provided catalogs and punch-out catalogs is available to search. Integration with the SAP S/4HANA Cloud Public Edition system enables a simple and seamless fulfillment experience by providing you with the ability to convert purchasing requests to purchase orders and track the process end to end.

|  |
| --- |
| Note SAP Ariba Buying is only available in a 3-system landscape. |

This document provides a detailed procedure for testing this scope item after solution activation, reflecting the predefined scope of the solution. Each process step, report, or item is covered in its own section, providing the system interactions (test steps) in a table view. Steps that are not in scope of the process but are needed for testing are marked accordingly. Project-specific steps must be added.

## Prerequisites

This section summarizes all prerequisites needed to conduct the test in terms of system, users, master data, organizational data, and other test data and business conditions.

Testing in a 3-System Landscape

In a 3-system landscape (with SAP Central Business Configuration as your configuration environment), changes to software and business configuration are applied to your systems independently of one another. It is therefore your responsibility to manage the active business configuration in your systems and synchronize configuration data in your SAP S/4HANA Cloud Public Edition system landscape. A synchronization is required, for example, after you've enhanced the scope, extended configuration, or adopted new or changed content from content updates or upgrades. For more information, refer to the [product assistance](https://help.sap.com/viewer/b249d650b15e4b3d9fc2077ee921abd0/latest/en-US/6c398c4ae7364af69d3edffe7fdc39f2.html) in the SAP Help Portal.

Before testing, if you want to use all software features described for the process steps, reports, or items in this document, we recommend the Business Process Configuration Expert in your organization has upgraded the configuration content and deployed the configuration data to your system landscape.

### System Access

| System | Details |
| --- | --- |
| System | Accessible via launchpad. Your system administrator provides you with the URL to access the various apps assigned to your role. |

### Roles

Create business roles using the following business role templates delivered by SAP and assign them to your individual test users.

Alternatively, if available, you can use the following spaces delivered by SAP. You create a space with pages containing predefined essential apps and assign it to the business role. You then assign this business role to your individual users.

For more information, refer to How to Create a Business Role from a Template in the [product assistance](https://help.sap.com/docs/SAP_S4HANA_CLOUD/53e36b5493804bcdb3f6f14de8b487dd/ec310a8b669a45ca898dc4dd91d97de2.html) for SAP S/4HANA Cloud Public Edition.

For roles required on SAP S/4HANA Cloud Public Edition for SAP Ariba Buying, see chapter [Assign Roles on SAP S/4HANA Cloud Public Edition for SAP Ariba Buying](https://help.sap.com/docs/SAP_Ariba_Buying/662c2bd15b5940cbaf249c814bedad91/3304058262ed41c38f070d7adfca3887.html) in the SAP Ariba Buying Administration Guide.

For more information on roles supported by SAP Ariba Buying, see chapter [Authorization](https://help.sap.com/docs/SAP_Ariba_Buying/662c2bd15b5940cbaf249c814bedad91/0ccb0ba92d574eb881a48ccbcce9c0ca.html) in the SAP Ariba Buying Administration Guide.

For roles required on SAP S/4HANA Cloud Public Edition for general operation process, see the following table:

| Name (Role Template) | ID (Role Template) | Name (Launchpad Space) | ID (Launchpad Space) | Log On |
| --- | --- | --- | --- | --- |
| Purchaser | SAP_BR_PURCHASER | Purchasing / Sourcing and Contracting | SAP_MM_SPT_PURCHASING_PC / SAP_MM_SPT_SOURCING_PC |  |
| Purchasing Manager | SAP_BR_PURCHASING_MANAGER | My Inbox | SAP_CORE_SPT_MYINBOX_PC |  |
| Warehouse Clerk | SAP_BR_WAREHOUSE_CLERK | Inventory Processing | SAP_BR_WAREHOUSE_CLERK |  |
| Accounts Payable Accountant | SAP_BR_AP_ACCOUNTANT | Accounts Payable / Central Invoice Management - Supplier Invoices / Central Invoicing - Supplier Invoice | SAP_BR_AP_ACCOUNTANT / SAP_MM_SPT_CIM_INV_PC / SAP_MM_SPT_CNTRL_INVOICING_PC |  |

### Additional Manual Configuration

Before you can test this scope item, you must have completed the additional configuration steps that are described in the Set-Up Instructions for this scope item. These configuration steps are specific for your implementation and include mandatory settings that are not delivered by SAP and must be created by you. For more information, follow the link to the document:

[Link to Set-Up Instructions](https://help.sap.com/docs/SAP_S4HANA_BEST_PRACTICES/05a73825df525647f770b987fd97c178)

### Preliminary Steps

#### Maintain BTP User Profile

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This is a mandatory step. The user can proceed with procurement only when the user profile exists.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Employee - Procurement. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open the Create Purchase Request application. |  |  |
| 3 | Access the User Profile | Click on your user icon on the right upper corner and choose the Profile Settings. |  |  |
| 4 | Maintain User Profile | On the Profile Settings screen, add the shipping information. Make the following entries with F4 help:Shipping Address: <Your Shipping Address>Ship To: <Your User>Under Organization and Accounting, make the following entries with F4 help:Company Code: <Your Company Code>, for example, 1010Plant: <Your Plant>, for example, 1010Cost Center: <Your Cost Center>Under Currency, make the following entry with F4 help:Currency: <Your Currency>, for example, EUR |  |  |
| 5 | Save the User Profile | Choose Save.Note For the first time, the user shall not see the cancel button as all these fields are mandatory for PR creation. So, user needs to save these details at least once. If field is missed, the user shall get an error message while saving and would be guided to fill the value. |  |  |

## Overview Table

The scope item consists of several process steps provided in the following table.

If your system administrator has enabled spaces and pages on the SAP Fiori launchpad, the homepage will only contain the essential apps for performing the typical tasks of a business role.

You can find all other apps not included on the homepage using the search bar.

If you want to personalize the homepage and include the hidden apps, navigate to your user profile and choose App Finder.

| Process Step | Business Role | Transaction/App | Expected Results |
| --- | --- | --- | --- |
| [Access the Landing Page](#unique_8) [page ] 7 | Employee - Procurement | Create Purchase Request |  |
| [Create Purchase Request](#unique_9) [page ] 7 | Employee - Procurement | Create Purchase Request |  |
| [Review Your Purchase Request](#unique_10) [page ] 9 | Employee - Procurement | Create Purchase Request |  |
| [Approve Purchase Request](#unique_11) [page ] 11 | Manager - Procurement | My Inbox - Buying |  |
| [Convert Purchase Requisitions to Purchase Orders](#unique_12) [page ] 12 | Purchaser | Process Purchase Requisitions - Deprecated (F1048) |  |
| [Approve Purchase Order (Optional)](#unique_13) [page ] 13 | Purchasing Manager | My Inbox - All Items (F5331) |  |
| [Goods Receipt for Purchase Order](#unique_14) [page ] 14 | Warehouse Clerk | Post Goods Receipt for Purchasing Document (F0843) |  |
| [Create Supplier Invoice](#unique_15) [page ] 15 | Accounts Payable Accountant | Create Supplier Invoice (F0859) |  |

## Test Procedures

### Access the Landing Page

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you open the SAP Ariba Buying application.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Employee - Procurement. | The SAP Fiori launchpad displays. |  |
| 2 | Access the Create Requst App | Open Create Purchase Request application. |  |  |

### Create Purchase Request

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you can create purchase request in SAP Ariba Buying.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Employee - Procurement. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Choose Create Purchase Request App. |  |  |
| 3 | Search for the Item | On the Create Purchase Request screen, enter the search text in the search bar. You can choose any one of the auto suggestions or choose Search to filter search. | The results page containing items matching the search text will come. |  |
| 4 | Add to Cart | On the Search Result screen, choose one of the images to navigate to product details page. You can modify the quantity and choose Add to Cart.If you want to search more items, you can enter search text in search bar at upper left of the screen and then repeat the previous steps.After items are added to cart, choose Cart at the upper right to be navigated to the cart page. |  |  |
| 5 | Review Request | On the checkout page, verify the quantity and other details.For service item request, you need to maintain the following entries:Start Date: <Service start date>End Date: <Service end date>Then choose Submit Request to submit the requisition.Once the requisition is submitted, there will be a pop-up window with PR number to show Requisition Submitted.You can choose View Request to navigate to the request page, the detail of the request will be displayed.You can choose the item to check more detailed information of the request, for example, Approval Workflow. |  |  |
| 6 | Add Comments (Optional) | Choose Edit for the item you want to add comments. On the line item xx screen, choose tab Comments and enter your comments.If you want to share the comments with supplier, please choose the following checkbox:Share with Supplier: <Check>Choose Back to Request. |  |  |
| 7 | Submit Request | Choose Submit Request to submit the requisition.Once the requisition is submitted, there will be a pop-up window Submit Request. You need to make ther following entries:Request Name: For example, ComputerThen choose Submit Request.Once the requisition is submitted, there will be a pop-up window with PR number to show Requisition Submitted.You can choose View Request to navigate to the request page. The detail of the request will be displayed.You can choose the item to check more detailed information of the request, for example, Approval Workflow. |  |  |
| 8 | Review Purchase Request | Choose Back to go back to landing page.On the landing page, you can choose My Requests at upper right of screen to list all your requests.In My Request page, you can choose In Process tab to list your requests. | In tab In progress, all your submitted requests will be listed.If all items of the request are approved, the status of the PR will be Approved.If partial items of the request are approved, the status of the PR will be Partially Approved.If none of the request is approved, the status of the PR will be Submitted. |  |

### Review Your Purchase Request

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

As soon as submission of the cart succeeds, a corresponding PR would be created in the SAP S/4HANA Cloud Public Edition system.

|  |
| --- |
| Note The PR number created in the connected system would not be the same as the Request ID reflected in SAP Ariba Buying. |

In this activity, you can display the newly created purchase requisition in the SAP S/4HANA Cloud Public Edition system.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Employee - Procurement. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open the Create Purchase Request application. |  |  |
| 3 | Search for Your Request | Choose Your Request and click on In Progress to list your PRs. | In the In progress tab, all your submitted requests will be listed.If all items of the request are approved, the status of the PR is Approved.If partial items of the re-quest are approved, the status of the PR is Partially Approved.If none of the request is approved, the status of the PR is Submitted.If the purchase order is created, the status of the request is Ordered. |  |
| 4 | Check Your Purchase Request | Find your Purchase Request and click on the request. You can choose one of the items to display the request details. |  |  |
| 5 | Check Overview Information | Click on Overview tab to check the information of your Request.Note For service items, please check the following information:Start Date: <Service start date>End Date: <Service end date>Product Type: ServiceService ID （Optional）: <Service ID in connected system> |  |  |
| 6 | Check the Approval Status | Click on the Approvals tab to view the approval status of the item. |  |  |
| 7 | Check the Comments | Click on the Comments tab to check the comments for the item. |  |  |
| 8 | Check the Status Flow | Click on the Status Flow tab to see the PR ID and all the follow-on documents that are created for the request.Make a note of the Purchase Requisition ID in connected system. This purchase requisition number will be used in chapter Convert Purchase Requisitions to Purchase Orders. |  |  |

### Approve Purchase Request

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, the approver will log on to SAP Fiori lauchpad and go to My Inbox - Buying to approve the request.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Manager - Procurement.Note In step 5 of chapter Review Your Purchase Request, you can check the approver for the purchase request. | The SAP Fiori launchpad displays. |  |
| 2 | Open Your Approvals | Choose My Inbox - Buying. |  |  |
| 3 | Select Request for Approval | On My Inbox - Buying screen, enter the request number or the part of item text in the search field to find the item for approval. |  |  |
| 4 | Leave Comments for Approval (Optional) | In the Approve request dialog box, enter comments and choose Approve. |  |  |
| 5 | Approve Request | Choose Approve. |  |  |
| 6 | Repeat the Steps | Repeat the steps 1-6 for all the others. | The status of PRXXXX changes from Submitted to Approved or Approved In External System. |  |

### Convert Purchase Requisitions to Purchase Orders

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

You can perform this activity when you want to convert assigned purchase requisitions to purchase orders in the SAP S/4HANA Cloud Public Edition system.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Purchaser. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the App | Open Process Purchase Requisitions ( Version 2 ) (F1048A). | A list of requisitions is displayed. |  |
| 3 | Search for Purchase Requisition | Enter the connected purchase requisition number in the Purchase Requisition Number field and then choose Go.Note You can check the purchase requisition number in the tab Status Flow of Purchase Request. | The purchase requisition is displayed. |  |
| 4 | Select Purchase Requisition | Select the purchase requisition create previously.. | The purchase requisition has been selected for source assignment. |  |
| 5 | Check Purchase Requisition Details | Choose Show More per Row under button Go to diaplay more information of the purchase requisition. |  |  |
| 6 | Create Purchase Order | Go back to screen Process Purchase Requisition, then choose your purchase requisition and choose Create Purchase Order. |  |  |
| 7 | Create the Purchase Order | In the New Purchase Order screen, make the following entry:Purchase Order Type: Standard PO (NB)Choose Order. | The purchase order is created. |  |
| 8 | Back to Manage Purchase Requisition | In the dialog box, choose OK. | The purchase requisition list is displayed again.The Processing Status of purchase requisition has been changed to PO created. |  |

### Approve Purchase Order (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

If the flexible workflow for purchase order is activated, the purchase order needs to be approved before goods receipt.

|  |
| --- |
| Note You can check your purchaser order to find out who is the approver of the purchase order. |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an approver, for example, Purchasing Manager. | The SAP Fiori launchpad is displayed. | The approver is up to the configuration of flexible workflow for purchase order. |
| 2 | Access the App | Open My Inbox - All Items (F5331). | A list of already created purchase orders is displayed. |  |
| 3 | Search for Purchase Order Status | Make the following entry and choose Enter:Search: <Purchase Order Number> | The purchase order is displayed. |  |
| 4 | Approve Purchase Order | Select the purchase order on the left of the screen and choose Approve at the bottom right. | The Submit Decision screen is displayed. |  |
| 5 | Enter Approval Reason | Enter the approval reason if necessary and choose Submit. | The purchase order is approved. |  |

|  |
| --- |
| Note After the purchase order is approved, you will have follow-up steps for different cases:For material item requestsPlease go ahead to the following chapters Goods Receipt for Purchase Order and Create Supplier Invoice to post goods receipt and create supplier invoice.For service item requestsYou can go to Service Procurement with SAP Business Network and SAP Fieldglass (4R2) to execute the follow-up steps. In 4R2, the service fulfillment can be steered and monitored with the supplier side statement of work, supplier time sheets, and service entry sheets. Afterwards, the invoicing process is triggered. |

### Goods Receipt for Purchase Order

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

Goods ordered by a purchase order arrive at warehouse. The goods receipt is to be posted.

In this activity, you post the goods receipt in the SAP S/4HANA Cloud Public Edition system.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Warehouse Clerk. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the App | Open Post Goods Receipt for Purchasing Document (F0843). | The Post Goods Receipt for Purchase Order screen is displayed. |  |
| 3 | Enter Purchase Order | Enter the Purchase Order ID and choose Enter. | The system displays the data for the goods receipt on the Goods Receipt screen. |  |
| 4 | Enter Delivery Note | Make the following entries and choose Enter:Delivery Note: xxxPrinting: Individual slip |  |  |
| 5 | Select Item | From the Items section, select the goods receipt item to be posted. | You can see that the Post button is activated. |  |
| 6 | Post | Choose Post. | The system displays the message Material Document xxx posted. |  |

### Create Supplier Invoice

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Context

In this activity, you perform the invoice verification in the SAP S/4HANA Cloud Public Edition system.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Accounts Payable Accountant. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the App | Open Create Supplier Invoice (F0859). | The New Supplier Invoices screen is displayed. |  |
| 3 | Enter General Data | In case of purchase orders created with local currency in your system, make the following entries:Transaction: <Invoice>Company Code: <Your company>Invoice Date: <Today>Posting Date: <Today>Gross Invoice Amount: <Value in PO Calculate Tax>Invoice Party: <Your supplier number>Reference: <Reference invoice number from invoicing party> | The New Supplier Invoices screen displays. |  |
| 4 | Enter Purchase Order References | In Purchase Order References, make the following entries (use a PO you created previously).References Document Category: <Purchase Order/ Scheduling Agreement>Purchase Order: <PO number> |  |  |
| 5 | Check the Purchase Order Items Data | Check the Amount, the Quantity and the Tax CodeNote If the amount is more than 5.5% of the initial amount, it will trigger supplier invoice workflow, which means you need to do next step – Release Blocked Supplier Invoice and amount changes only work for single account assignment. |  |  |
| 6 | Post Invoice | Choose Post. | The invoice is created. |  |

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
> Flagged while digesting this document, not verified: Overview table lists Process Purchase Requisitions - Deprecated (F1048) while the procedure uses Process Purchase Requisitions (Version 2) (F1048A)

## Connections
- part-of :: [[_cluster]]
- related-to :: [[10-procurement/sap-ariba-buying-base-edition-7ym-test-script-1237]]
- related-to :: [[10-procurement/test-script-sap-ariba-buying-procurement-expansion-package-81y-1244]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/4AI_S4CLD2608_BPD_EN_XX.docx` — full document · extracted with `mammoth` · 27,846 chars in the whole document
