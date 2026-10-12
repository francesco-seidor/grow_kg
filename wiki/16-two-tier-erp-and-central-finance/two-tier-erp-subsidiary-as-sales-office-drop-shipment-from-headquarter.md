---
id: 16-two-tier-erp-and-central-finance/two-tier-erp-subsidiary-as-sales-office-drop-shipment-from-headquarter
title: "Two-Tier ERP: Subsidiary as Sales Office, Drop-shipment from Headquarter - Customer Guide (S4CLD2608_2T_ Drop Shipment_User_Guide)"
description: "SAP Cloud ERP two-tier guide: subsidiary sales office with drop shipment from headquarters; prerequisites, EDI/IDoc setup, master data, and test script (scope BD3/2EJ)."
cluster: 16-two-tier-erp-and-central-finance
tags: [kb/two-tier-erp-and-central-finance, topic/subsidiary-sales-office-drop-shipment]
aliases: [S4CLD2608_2T_ Drop Shipment_User_Guide]
keywords: [Subsidiary as Sales Office with HQ Drop Shipment, drop shipment, two-tier erp, idoc integration, master data, third-party sales order, billing documents, communication arrangement, tax code mapping, integration with buyer]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/General/Two-Tier_ERP_Assets_User_Guides/Two-Tier_ERP_Assets_User_Guides/Sales & Service/S4CLD2608_2T_ Drop Shipment_User_Guide.docx]
confidence: low
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-247
topic: 16-two-tier-erp-and-central-finance/subsidiary-sales-office-drop-shipment
language: ""
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Two-Tier ERP: Subsidiary as Sales Office, Drop-shipment from Headquarter - Customer Guide (S4CLD2608_2T_ Drop Shipment_User_Guide)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/General/Two-Tier_ERP_Assets_User_Guides/Two-Tier_ERP_Assets_User_Guides/Sales & Service/S4CLD2608_2T_ Drop Shipment_User_Guide.docx`, extracted with `mammoth`. Grouped under **Subsidiary as Sales Office with HQ Drop Shipment** in Two-Tier ERP and Central Finance. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

|  |  |
| --- | --- |
| SAP Cloud ERP June 2026English |  |
|  | Two-Tier ERP: Subsidiary as Sales Office, Drop-shipment from Headquarter |
|  | Customer Guide |

Copyright

© 2020 SAP SE or an SAP affiliate company. All rights reserved.

No part of this publication may be reproduced or transmitted in any form or for any purpose without the express permission of SAP SE. The information contained herein may be changed without prior notice.

Some software products marketed by SAP SE and its distributors contain proprietary software components of other software vendors.

National product specifications may vary.

These materials are provided by SAP SE and its affiliated companies ("SAP Group") for informational purposes only, without representation or warranty of any kind, and SAP Group shall not be liable for errors or omissions with respect to the materials. The only warranties for SAP Group products and services are those that are set forth in the express warranty statements accompanying such products and services, if any. Nothing herein should be construed as constituting an additional warranty.

SAP and other SAP products and services mentioned herein as well as their respective logos are trademarks or registered trademarks of SAP SE in Germany and other countries. Please see http://www.sap.com/corporate-en/legal/copyright/index.epx#trademark for additional trademark information and notices.

| Revision | Change Date | Description |
| --- | --- | --- |
| 0 | 01.03.2018 | Initial version of document |
| 1 | 01.06.2020 | Validation of document |
| 2 | 31.03.2021 | Review of Document |

Icons

| Icon | Meaning |
| --- | --- |
| <!-- image omitted: unnamed --> | Caution |
| <!-- image omitted: unnamed --> | Example |
| <!-- image omitted: unnamed --> | Note |
| <!-- image omitted: unnamed --> | Recommendation |
| <!-- image omitted: unnamed --> | Syntax |

Typographic Conventions

| Type Style | Description |
| --- | --- |
| Example text | Words or characters that appear on the screen. These include field names, screen titles, pushbuttons as well as menu names, paths and options.Cross-references to other documentation. |
| Example text | Emphasized words or phrases in body text, titles of graphics and tables. |
| EXAMPLE TEXT | Names of elements in the system. These include report names, program names, transaction codes, table names, and individual key words of a programming language, when surrounded by body text, for example, SELECT and INCLUDE. |
| Example text | Screen output. This includes file and directory names and their paths, messages, source code, names of variables and parameters as well as names of installation, upgrade and database tools. |
| EXAMPLE TEXT | Keys on the keyboard, for example, function keys (such as F2) or the ENTER key. |
| Example text | Exact user entry. These are words or characters that you enter in the system exactly as they appear in the documentation. |
| <Example text> | Variable user entry. Pointed brackets indicate that you replace these words and characters with appropriate entries. |

Contents

[1 Purpose 7](#_Toc43385806)

[2 Value Proposition 7](#_Toc43385807)

[2.1 Business Requirements 7](#_Toc43385808)

[2.2 Two-Tier Solution 7](#_Toc43385809)

[3 Business Process Details 7](#_Toc43385810)

[3.1 Prerequisites 8](#_Toc43385811)

[3.2 Process Flow with Technical Details 9](#_Toc43385812)

[4 Technical Requirement 9](#_Toc43385813)

[4.1 Integration Requirements by using API 9](#_Toc43385814)

[4.2 Integration Requirements by using EDI/IDOC 9](#_Toc43385815)

[4.3 Reporting Requirements by using Analytical CDS Views 10](#_Toc43385816)

[4.4 Reporting Requirements by using Analytical API 10](#_Toc43385817)

[5 Configurations 10](#_Toc43385818)

[5.1 Configuration for SAP Cloud ERP Public Edition 10](#_Toc43385819)

[5.1.1 Communication Arrangement in SAP Cloud ERP Public Edition (Subsidiary) 10](#_Toc43385820)

[5.1.2 Tax Codes in SAP Cloud ERP Public Edition (Subsidiary) 10](#_Toc43385821)

[5.1.3 Company Code determination in SAP Cloud ERP Public Edition (Subsidiary) 11](#_Toc43385822)

[5.1.4 Integration with Buyer in SAP Cloud ERP Public Edition (Subsidiary) 11](#_Toc43385823)

[5.2 Configuration for SAP S/4HANA On premise/ Cloud ERP Private 12](#_Toc43385824)

[5.2.1 IDOC Configs at the On-Premise System (Headquarters) 12](#_Toc43385825)

[6 Master Data 13](#_Toc43385826)

[6.1 Master Data for SAP Cloud ERP 13](#_Toc43385827)

[6.1.1 Vendor Master 13](#_Toc43385828)

[6.1.2 Condition Master 13](#_Toc43385829)

[6.1.3 Purchase Info Record 14](#_Toc43385830)

[6.2 Master Data for SAP S/4HANA On premise/ Cloud ERP Private 14](#_Toc43385831)

[6.2.1 Material Master 14](#_Toc43385832)

[6.2.2 Customer Master 15](#_Toc43385833)

[6.2.3 Condition Master 17](#_Toc43385834)

[6.2.4 Sales org determination at Headquarters 17](#_Toc43385835)

[7 Test Script 17](#_Toc43385836)

[7.1 Prerequisites 17](#_Toc43385837)

[7.2 System Access at Subsidiary 17](#_Toc43385838)

[7.3 Role at Subsidiary 18](#_Toc43385839)

[7.4 Role at Headquarters 18](#_Toc43385840)

[7.5 Master Data, Organizational Data, and Other Data 18](#_Toc43385841)

[7.6 Business Conditions in Subsidiary 20](#_Toc43385842)

[7.7 Preliminary Steps 20](#_Toc43385843)

[7.7.1 Assigning Release Processor for PO Approval at Subsidiary 20](#_Toc43385844)

[7.7.2 Change Purchasing Info Record at Subsidiary 21](#_Toc43385845)

[7.7.3 Create Purchasing Info Record at Subsidiary 22](#_Toc43385846)

[7.7.4 Activate Flexible Workflow for Purchase Order Approval at Subsidiary 23](#_Toc43385847)

[7.7.5 Configure Flexible Workflow for Purchase Order at Subsidiary 25](#_Toc43385848)

[7.8 Overview Table 27](#_Toc43385849)

[7.9 Test Procedures 30](#_Toc43385850)

[7.9.1 Sales Inquiry at Subsidiary (1IQ) (Optional) 30](#_Toc43385851)

[7.9.2 Sales Contract Management at Subsidiary (I9I) (Optional) 31](#_Toc43385852)

[7.9.3 Sales Quotation at Subsidiary (BDG) (Optional) 31](#_Toc43385853)

[7.9.4 Create Third-Party Sales Order at Subsidiary 32](#_Toc43385854)

[7.9.5 Create Attachment for Sales Order at Subsidiary (Optional) 34](#_Toc43385855)

[7.9.6 Change Order Quantity at Subsidiary (Optional) 35](#_Toc43385856)

[7.9.7 Display List of Purchase Requisitions to be Assigned at Subsidiary 36](#_Toc43385857)

[7.9.8 Convert Assigned Requisitions into Purchase Orders at Subsidiary 37](#_Toc43385858)

[7.9.9 Approve Purchase Orders (Optional) at Subsidiary 38](#_Toc43385859)

[7.9.10 Review Purchase Order Message at Subsidiary 40](#_Toc43385860)

[7.9.11 Review Order Confirmation at Subsidiary 41](#_Toc43385861)

[7.9.12 Send Order Confirmation (Update) to Customer at Subsidiary 42](#_Toc43385862)

[7.9.13 Create Delivery at Headquarters 42](#_Toc43385863)

[7.9.14 Create Attachment for Delivery at Headquarters (Optional) 42](#_Toc43385864)

[7.9.15 Execute Picking at Headquarters 43](#_Toc43385865)

[7.9.16 Check Batches at Headquarters (Optional) 43](#_Toc43385866)

[7.9.17 Split Outbound Delivery at Headquarters (optional) 43](#_Toc43385867)

[7.9.18 Add Freight Costs at Headquarters (Optional) 44](#_Toc43385868)

[7.9.19 Post Goods Issue at Headquarters 44](#_Toc43385869)

[7.9.20 Review Shipping Notification at Subsidiary 45](#_Toc43385870)

[7.9.21 Post Statistical Goods Receipt at Subsidiary 46](#_Toc43385871)

[7.9.22 Create Billing Document at Subsidiary 48](#_Toc43385872)

[7.9.23 Create Attachment for Billing at Subsidiary (Optional) 50](#_Toc43385873)

[7.9.24 Create Pro Forma Invoice – for Free or Charge Items at Subsidiary (Optional) 51](#_Toc43385874)

[7.9.25 Create Billing Document at Headquarters 53](#_Toc43385875)

[7.9.26 Create Attachment for Billing at Headquarters (Optional) 53](#_Toc43385876)

[7.9.27 Check Vendor Invoice at Subsidiary 54](#_Toc43385877)

[7.10 Appendix 56](#_Toc43385878)

[7.10.1 Process Integration 56](#_Toc43385879)

[7.10.2 Succeeding Processes 56](#_Toc43385880)

[7.10.3 Scheduling Job (alternative) 56](#_Toc43385889)

[7.10.3.1 Job Scheduling for Billing Creation (Alternative) 56](#_Toc43385890)

**Two-Tier- Subsidiary as Sales Office, Drop-shipment from Headquarters**

## Purpose

This document will provide the detailed process on Two-Tier ERP solution for process where “Subsidiary is a Local Sales Office – Drop Shipment from Headquarters” with process flow, technical requirements and followed with testing procedure.

## Value Proposition

### Business Requirements

The Subsidiary process the customer's order and Shipment details are communicated as sales orders to headquarters, who then dispatches goods to the customer directly from Headquarters with seamless processes Integration between headquarters and subsidiary.

### Two-Tier Solution

Through Two-Tier ERP solutions, seamless orchestration of process between headquarters and subsidiary along with below Integration points.

1. Purchase order at subsidiary will be automatically transformed to sales order at headquarters.
2. Headquarters confirms the sales order and subsequently the Purchase order at the subsidiary is updated.
3. Once the Goods issue is done at the headquarters, the advance shipping notification is sent to subsidiary.
4. Headquarters creates billing documents; corresponding supplier invoice will be created at Subsidiary.

## Business Process Details

The Two-Tier ERP solution for Subsidiary as a Local Sales Office – Drop Shipment from Headquarters is depicted in this document.

The process starts where customer places order at subsidiary. The internal sales representative at the subsidiary creates the sales order of customer, where purchase requisition is automatically created against the sales order. The purchase requisites is converted to purchase order from the displayed list of purchase requisition. Once the purchase order is approved EDI based approach is used to automatically transfer the purchase order information, for creation of sales order at Headquarters.

Internal Sales representatives will receive the automatically generated sales order at Headquarters with sold-to as subsidiary and ship-to as the end customer. Once the sales order is confirmed, EDI based approach is used to confirm the purchase order at subsidiary

As soon as the sales order is confirmed the shipping specialist at headquarters release goods for delivery to shipment office at headquarters. The shipment specialist creates delivery document, Post goods issue at headquarters which triggers an advance shipping notification to subsidiary through EDI based approach.

Once the shipping notification is received, the warehouse clerk at subsidiary posts statistical goods receipt and billing clerks creates billing document which is billed to customers.

Post goods has been issued from the shipping specialist, billing clerk at headquarters creates billing documents and bill to subsidiary, corresponding Supplier invoice will be created automatically at Subsidiary.

### Prerequisites

The following list of prerequisites are to be in place to realize the business process

- Subsidiary should be running on SAP Cloud ERP system and Headquarters should run on SAP S/4HANA On premise/ Cloud ERP Private or ECC
- Activate the Scope ID 2EJ and BD3 at the Subsidiary’s SAP Cloud ERP system
- In case Headquarters is on:
- SAP S/4HANA On premise/ Cloud ERP Private activate the scope ID BD9
- SAP ERP follow standard sell from stock process.
- The Headquarters and Subsidiary should have business partner and product master data aligned for this business process to work.
- Headquarters will be represented as a Supplier in Subsidiary and Subsidiary will be represented as a Customer in Headquarters.

### Process Flow with Technical Details

<!-- image omitted: unnamed -->

The following integration points are depicted in the process flow diagram:

1. Purchase order at subsidiary will be automatically transformed to sales order at headquarters.
2. Headquarters confirms delivery date to the subsidiary sales office.
3. Post goods issue at headquarters will send advance shipping notification resulting in automatic inbound delivery creation.
4. Headquarters create billing documents correspondingly supplier invoice will be created at Subsidiary.

## Technical Requirement

### Integration Requirements by using API

None

### Integration Requirements by using EDI/IDOC

**In SAP Cloud ERP:**

Use Communication System Scenario SAP_COM_0224 the details of setting up this scenario instruction will be found in set up instruction document for scope ID 2EJ from SAP Best Practices Explorer.

**In SAP S/4HANA On premise/ Cloud ERP Private:**

The On premise/ Cloud ERP Private will use the following IDOCS

1. ORDERS05: For creating sales order
2. ORDRSP: For order confirmation
3. DELVRY07: For sending ASN
4. INVOIC2: For sending billing document

Mapping between the IDOC and SOHA service fields in the I-flow will be provided by SAP.

### Reporting Requirements by using Analytical CDS Views

None

### Reporting Requirements by using Analytical API

None.

## Configurations

### Configuration for SAP Cloud ERP

#### Communication Arrangement in SAP Cloud ERP (Subsidiary)

To be setup as per SAP Cloud ERP Best Practice scope id 2EJ.

#### Tax Codes in SAP Cloud ERP (Subsidiary)

Tax codes between the HQ and subsidiary must be mapped for Supplier Invoice posting sat subsidiary from Billing document at HQ.

1. Log on to the SAP Fiori launchpad in the SAP Cloud ERP system.

2. Navigate to Implementation Cockpit > Manage Your Solution > Configure Your Solution

3. On the Configure Your Solution: Realize Phase screen, select the values as shown below:

- Application Area: Sourcing and Procurement
- Sub-application area: Integration

4. In the Configure Item area, choose the entry with above values and Name: Integration with Supplier

5. In the Configure Your Solution: Integration with Suppliers screen, choose the Configuration Steps tab.

6. Search for Assign Tax Codes and select Configure.

7. Choose New Entries.

8. Enter the Headquarter’s ID as Invoicing Party, e.g. 10300089

9. Enter the type of tax (for example A1) under Tax Type.

10. Enter the country of the subsidiary under Country.

11. Under Tax Code enter the respective tax code of your SAP Cloud ERP system.

For example, V1.

12. Choose Save.

13. One line item has to be created for each tax code mapping.

#### Company Code determination in SAP Cloud ERP (Subsidiary)

1. Log on to the SAP Fiori launchpad in the SAP Cloud ERP system.

2. Navigate to Implementation Cockpit > Manage Your Solution > Configure Your Solution.

3. On the Configure Your Solution: Realize Phase screen, select the values as shown below:

- Application Area: Sourcing and Procurement
- Sub-application area: Integration

4. In the Configure Item area, choose the entry with above values and Name: Integration with Supplier

5. On the Configure Your Solution: Integration with Suppliers screen, choose the Configuration Steps tab.

6. Search for Assign Company Code and select Configure.

7. Choose New Entries.

8. Enter the Headquarters’ ID as Invoicing Party, e.g. 10300089

9. Enter the name or the account number which Headquarters uses in invoices for Subsidiary’s company as Company Code Name, e.g. 10101000

10. Enter the Company Code used in subsidiary’s SAP Cloud ERP system, e.g. 1010

11. Choose Save.

One line item should be created for each company code mapping

#### Integration with Buyer in SAP Cloud ERP (Subsidiary)

1. Log on to the SAP Fiori launchpad in the SAP Cloud ERP system.

2. Navigate to Implementation Cockpit > Manage Your Solution > Configure Your

Solution.

3. On the Configure Your Solution: Realize Phase screen, select the values as shown below:

- Application Area: Sales
- Sub-application area: Integration

4. On the Configure Your Solution: Integration with Buyer screen, choose the

Configuration Steps tab

5. Select Step Name Assign Customer/Supplier to Sales Organization Data step Select

Configure

6. Choose New Entries

Enter Customer: 10100001

Enter Supplier: 10300089

Enter Sales Organization: 1710

Enter Distribution Channel: 10

Enter Division: 00

Enter Sales Document Type: OR

7. Select Step Name Convert External to Internal Partner Numbers Step Select Configure

Choose New Entries

Customer: 10100001

Function Partner Function: SP

External Partner: 10300089

Internal Partner: 10100001

8. Select Step Name Define Mapping for Inbound Texts for Integration with Buyers Step Select

Configure

Choose New Entries

| XMLMessage Type | TextObj | XML Text Type | TxPrc | ID |
| --- | --- | --- | --- | --- |
| OrderRequest | Header | PickPackInstructions | T3 | Tx07 |
| OrderRequest | Header | SalesNote | T3 | Tx02 |
| OrderRequest | Header | ShippingInstructions | T3 | Tx03 |
| OrderRequest | Item | PickPackInstructions | T3 | Tx07 |
| OrderRequest | Item | MaterialText | T3 | 0001 |
| OrderRequest | Item | ShippingInstructions | T3 | Tx04 |

Maintain corresponding values in OnPrem system for the following Text IDs available in

Note: In case, a TextID which is not maintained in Value Mapping table is received, Text node will not be created and corresponding text will not be passed to the receiver system.

### Configuration for SAP S/4HANA On premise/ Cloud ERP Private

#### IDOC Configs at the On-Premise System (Headquarters)

Configure the Partner profiles and message control for incoming IDOCS for Sales Order creation and Change and outbound IDOCS for Order Confirmation, Advance Shipping

Notification and Billing Document.

The following IDOCS are to be used:

| **Message Type** | **Direction** | **Use** |
| --- | --- | --- |
| ORDERS05 | Inbound | Sales Order Creation/Change |
| ORDRSP | Outbound | Sales Order Confirmation |
| DESADV | Outbound | Advance Shipping Notification |
| INVOIC02 | Outbound | Billing document |

## Master Data

### Master Data for SAP Cloud ERP

#### Vendor Master

HQ to be maintained as a supplier in subsidiary. The customer number maintained against subsidiary at the HQ has also to be specified here. If the HQ has multiple sales areas with which the subsidiary does business, then each sales area of the HQ must be a supplier at the subsidiary. The same is true for HQ having multiple company codes.

<!-- image omitted: unnamed -->

Subsidiary’s Customer number at HQ

#### Condition Master

Condition master can be managed centrally at Headquarters with the buying price for the subsidiary and selling price for HQ being same by using release accelerators on ‘Centralised Pricing’. In parallel you can also use whitelisted API’s in API Hub.

#### Purchase Info Record

The condition group must set as ‘0001’ in the Purchasing info record against the HQ for the material. ‘0001’ corresponds to purchase orders requiring confirmations and advance shipping notifications. The receipt of advance shipping notification will automatically create the inbound delivery.

<!-- image omitted: unnamed -->

### Master Data for SAP S/4HANA On premise/ Cloud ERP Private

#### Material Master

The material number of subsidiary has to be mapped with the material number of the headquarters using customer info record.

<!-- image omitted: unnamed -->

Material number at Subsidiary

Material number at HQ

#### Customer Master

The subsidiary has to be maintained a customer in HQ. The supplier number of the HQ at the subsidiary has to be provided here. If the subsidiary has multiple company codes, then each company code has to be maintained as customer in the subsidiary. The practice at subsidiary should be one unique purchasing org per company code.

<!-- image omitted: unnamed -->

HQ’s Supplier number at Subsidiary

Subsidiary’s customers relevant for drop-shipment have to be maintained as ship-to-party roles in the partner function for the subsidiary.

<!-- image omitted: unnamed -->

Subsidiary’s Customer for drop-shipment

The subsidiary’s end customer has to be created at HQ with ship-to-party role only. The sold-to-party, payer and bill-to-party will be the subsidiary.

<!-- image omitted: unnamed -->

Partner functions assignment

Subsidiary’s end customer

If the numbering of the customer at subsidiary and HQ is same, then the value mapping has to be maintained in SAP Cloud Integration as described in section 5.3.

#### Condition Master

Condition master can be managed centrally at Headquarters with the buying price for the subsidiary and selling price for HQ being same by using release accelerators on ‘Centralised Pricing’. In parallel you can also use whitelisted API’s in API Hub.

#### Sales org determination at Headquarters

In the EDSDC table (Transaction code VOE2), maintain the sales area determination for subsidiary’s sales orders at HQ.

<!-- image omitted: unnamed -->

Preferred Sales Area at HQ

Supplier Number for HQ at Subsidiary

Customer Number for Subsidiary at HQ

## Test Script

### Prerequisites

This section summarizes all prerequisites needed to conduct the test in terms of system, users, master data, organizational data, and other test data and business conditions.

Integration to Headquarters system needs to be established first. For that, please activate Integration Scope Item 2EJ. For details refer to the corresponding Setup Guide.

### System Access at Subsidiary

The test should be conducted with the following system:

| System | Details |
| --- | --- |
| System | Accessible via the SAP Fiori Launchpad. Your system administrator provides you with the URL to access the various apps assigned to your role. |

### 7.3 Role at Subsidiary

Assign the following business roles to your individual test users at Subsidiary.

Note The following roles are provided as example roles from SAP. You can use these as templates to create your own roles.

| Business Role | Business Role ID as Delivered by SAP | Log On |
| --- | --- | --- |
| Internal Sales Representative | SAP_BR_INTERNAL_SALES_REP |  |
| Purchaser | SAP_BR_PURCHASER |  |
| Purchasing Manager | SAP_BR_PURCHASING_MANAGER |  |
| Accounts Payable Accountant | SAP_BR_AP_ACCOUNTANT |  |
| Billing Clerk | SAP_BR_BILLING_CLERK |  |
| Warehouse Clerk | SAP_BR_WAREHOUSE_CLERK |  |
| Receiving Specialist | SAP_BR_RECEIVING_SPECIALIST |  |

Assign the following business roles to your individual test users.

### 7.4 Role at Headquarters

The following roles are provided as example roles from SAP. You can use these as templates for your own roles.

| Business Role |
| --- |
| Internal Sales Representative |
| Shipping Specialist |
| Warehouse Clerk |
| Billing Clerk |
| Credit Controller |
| Customer Master Specialist |

For more information about business roles, refer to Assigning business roles to a user in the [Administration Guide for the Implementation of SAP S/4HANA](https://help.sap.com/viewer/S4HANA1709_AdminGuide).

### 7.5 Master Data, Organizational Data, and Other Data

SAP Best Practices Standard Values based on new global template will be used once available. In the table you still see the master data used for the current baseline.

Essential master and organizational data was created in your S/4 HANA system in the implementation phase, such as the data that reflects the organizational structure of your company and master data that suits its operational focus, for example, master data for materials, vendors, and customers.

This master data usually consists of standardized SAP Best Practices default values, and enables you to go through the process steps of this scope item.

Note Additional Master Data (Default Values)

You can test the scope item with other SAP Best Practices default values that have the same characteristics.

Check your SAP system to find out which other material master data exists.

Note Using Your Own Master Data

You can also use customized values for any material or organizational data for which you have created master data.

The organizational structure and master data of your company has been created in your system during activation. The organizational structure reflects the structure of your company. The master data represents materials, customers, and vendors, for example, depending on the operational focus of your company.

Use your own master data or the following sample data to go through the test procedure. Below is the Master data maintained at SAP S4 HANA cloud system.

| Data | Sample Value | Details | Comments |
| --- | --- | --- | --- |
| Material | TG10 | Trad. Good 10, PD, Third PartyTrading Good for regular Trading (MRP planning) with item category group CBORno Serial no.; no batch. | See sections Preliminary Steps. |
| Sold-to party | 10100001 | Customer domestic 01 | You can test the scope item using another domestic customer. |
| Ship-to party | 10100001 | Domestic DE Customer 1 |  |
| Payer | 10100001 | Domestic DE Customer 1 |  |
| Vendor | 10300084 | Domestic DE Supplier 84 |  |
| Plant | 1010 | Plant 1 DE |  |
| Storage Location | 101A | Std. storage 1 |  |
| Shipping Point | 1010 | Shipping Point 1010 |  |
| Sales organization | 1010 | Dom. Sales Org |  |
| Distribution channel | 10 | Direct Sales |  |
| Division | 00 | Product Division 00 |  |
| Company Code | 1010 | Company Code 1010 |  |

For more information on creating master data objects, see the following Master Data Scripts (MDS):

Table 1: Master Data Script Reference

| Master Data ID | Description |
| --- | --- |
| BNF | Create Product Master of Type "Trading Good" |
| BND | Create Customer Master |

Master Data maintained in Headquarters On premise/ Cloud ERP Private System

| Data | Sample Value | Details | Comments |
| --- | --- | --- | --- |
| Material | TG10 or as per Headquarters nomenclature | Trad. Good 10, PD, Third PartyTrading Good for regular Trading (MRP planning) with item category group CBORno Serial no.; no batch. | Customer Info record of the material number in the Headquarters |
| Sold-to party | XXXXXXX | Customer no. subsidiary |  |
| Ship-to party | 10100001 | Domestic DE subsidiary | In Headquarters On premise/ Cloud ERP Private end customer to be maintained as Ship to Party and correspondingly Sold to party should be subsidiary |
| Payer | XXXXXXX |  |  |

### 7.6 Business Conditions in Subsidiary

The business process described in this Test Script is part of a bigger chain of integrated business processes or scope items. As a consequence, you must have completed the following processes and fulfilled the following business conditions before you are able to start going through this scope item:

| Scope Item | Business Condition |
| --- | --- |
| 2EJ - Integration of SAP Cloud ERP Procurement with Headquarters | In case you want to exchange messages with Headquarters you have to activate Scope Item 2EJ. |

### Preliminary Steps

#### Assigning Release Processor for PO Approval at Subsidiary

External Process

For this activity, run the following steps from the Procurement of Direct Materials (J45) test script to configure your release conditions for PO approval:

- Configure Your Release Conditions for PO Approval

#### Change Purchasing Info Record at Subsidiary

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| Test Case ID | <X.XX> | Tester Name |  | Testing Date | Enter a test date. |
| Business Role(s) |  |  |  |  |  |
| Responsibility | <State Service Provider, Customer or Joint Service Provider and Customer> | Duration | Enter a duration. |  |  |

Context

In this activity, you change the existing Purchase Info Record.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log onto the SAP Fiori launchpad as a Purchaser. | The SAP Fiori launchpad displays. |  |
| 3 | Access the SAP Fiori App | Open Change Purchasing Info Record. | The Change Info Record: Initial Screen screen displays. |  |
| 4 | Enter Data | Make the following entries:Supplier: 10300084Material: TG10Purchasing Organization: 1010Plant: 1010Press Enter. | The Chanege Info Record: General Data screen displays. |  |
| 6 | Enter Purchasing Data | Make the following entries:Conf. Ctrl : 0001 [Confirmations] | Purchasing Data is added. |  |
| 7 | Save your data | Choose Save. | A purchasing info record is saved. |  |

#### Create Purchasing Info Record at Subsidiary

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| Test Case ID | <X.XX> | Tester Name |  | Testing Date | Enter a test date. |
| Business Role(s) |  |  |  |  |  |
| Responsibility | <State Service Provider, Customer or Joint Service Provider and Customer> | Duration | Enter a duration. |  |  |

Context

In this activity, you create a Purchase Info Record.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log onto the SAP Fiori launchpad as a Purchaser. | The SAP Fiori launchpad displays. |  |
| 3 | Access the SAP Fiori App | Open Create Purchasing Info Record. | The Create Info Record: Initial Screen displays. |  |
| 4 | Enter Data | Make the following entries:Supplier: 10300084Material: TG10Purchasing Organization: 1010Plant: 1010Press Enter. | The Create Info Record: General Data screen displays. |  |
| 5 | Enter General Information | Make the following entries:Supp. Mat. No: TG12Choose Purch.Org. Data 1. | The Create Info Record: Purch. Organization Data 1 screen displays. |  |
| 6 | Enter Purchasing Data | Make the following entries:Delivery Time in Days: 2 DaysPurchasing Group: 002Standard Quantity: 10Tol. Underdl.: 10Tol. Overdl: 10Conf. Ctrl: 0001 [Confirmations]Tax Code: V1Net Price: 12.35Incoterm: EXWIncoterm Location 1: VENDORSelect the following entries if necessary:UnlimitedGR-Bsd IVNo ERSAckn.Rqd | Purchasing Data is added. |  |
| 7 | Save your data | Choose Save. | A purchasing info record is saved. |  |

#### Activate Flexible Workflow for Purchase Order Approval at Subsidiary

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| Test Case ID | <X.XX> | Tester Name |  | Testing Date | Enter a test date. |
| Business Role(s) |  |  |  |  |  |
| Responsibility | <State Service Provider, Customer or Joint Service Provider and Customer> | Duration | Enter a duration. |  |  |

Context

In this procedure, you activate flexible workflow for purchase order approval.

If you want to use the flexible workflow to approve the purchase order, you have to process the steps: Activate Flexible Workflow for Purchase Order Approval and Configure Flexible Workflow for Purchase Order.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log onto the SAP Fiori launchpad as a Configuration Expert. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Manage Your Solution. | The Manage Your Solution screen displays. |  |
| 3 | Open Configure Your Solution | Choose Configure Your Solution.Note If country version needs to be added, choose Set Country Version. | The Configure Your Solution screen displays. |  |
| 4 | Open Active Flexible Workflow | On the Configure Your Solution screen, search Activate Flexible Workflow for Purchase Orders, and then choose Go.Select the line of the item and go to next screen.On the Configure Your Solution – Purchase Order Processing screen, choose Configure on the line of configuration step with name Activate Flexible Workflow for Purchase Orders. | The Document Types Purchase order Change screen displays. |  |
| 5 | Activate Flexible Workflow for PO Approval | Make the following entries and choose Save:Document Type: NBScenario based workflow:XNote You may be asked to enter a customizing request number, either choose your own customizing request or create a new one, and then choose Continue. | The Scenario based workflow is active for Purchase Orders with Document Type: NB. |  |

Result

The Scenario based workflow is active for Document Type: NB.

#### Configure Flexible Workflow for Purchase Order at Subsidiary

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| Test Case ID | <X.XX> | Tester Name |  | Testing Date | Enter a test date. |
| Business Role(s) |  |  |  |  |  |
| Responsibility | <State Service Provider, Customer or Joint Service Provider and Customer> | Duration | Enter a duration. |  |  |

Purpose

In this procedure, you configure your release conditions for Purchase Order Approval.

Note When you start to process this step, please make sure that the flexible workflow for purchase document type NB has been activated in your system.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori launchpad as a Purchaser. | The SAP Fiori launchpad displays. |  |
| 2 | Open Manage Workflow for Purchase Order | Open Manage Workflows for Purchase Order. | The Manage Workflows screen displays. |  |
| 3 | Create Manage Workflow | Choose Add and make following entries:Name: Test Workflow for Purchase OrderIn the Preconditions area select Purchasing group of purchase order is with 003 value:Choose Add another condition and make the following entries:Choose Total net amount of purchase order is greater thanPrice: 500.Currency: USDIn Step Sequence area choose the Add and make following entries:Type: Release Purchase OrderRole: Manager of Workflow InitiatorStep to be completed by: One of the recipients.Choose Add.Choose Save. | The Workflow for Purchase Order is configured. |  |
| 4 | Activate Workflow Item | Select the just created Workflow Item and choose Activate. | The Workflow Item is activated. |  |

Note Please make sure default workflow Automatic Release of Purchase Order has been activated.

## 7.8 Overview Table

This scope item consists of several process steps provided in the table below.

| Process Step | Business Role | Transaction/App | Expected Results |
| --- | --- | --- | --- |
| Sales Inquiry at Subsidiary (1IQ) (Optional) [page] 30 | Internal Sales Representative | See scope item no. 1IQ |  |
| Sales Contract Management at Subsidiary (I9I) (Optional) [page] 31 | Internal Sales Representative | See scope item no. I9I |  |
| Sales Quotation at Subsidiary (BDG) (Optional) [page] 31 | Internal Sales Representative | See scope item no. BDG |  |
| [Create Third-Party Sales Order](#unique_13) at Subsidiary [page] 32 | Internal Sales Representative | Manage Sales Orders | The Manage Sales Orders screen displays. |
| [Create Attachment for Sales Order at Subsidiary (Optional)](#unique_14) [page] 34 | Internal Sales Representative | Display Sales Orders | The Display Sales document screen displays. |
| [Change Order Quantity at Subsidiary (Optional)](#unique_15) [page] 35 | Internal Sales Representative | Manage Sales Orders | The Manage Sales Orders screen displays. |
| [Display List of Purchase Requisitions to be Assigned](#unique_16) at Subsidiary [page] 36 | Purchaser | Manage Purchase Requisitions | The Manage Purchase Requisitions screen displays. |
| [Convert Assigned Requisitions into Purchase Orders](#unique_17) at Subsidiary [page] 37 | Purchaser | Manage Purchase Requisitions | The Manage Purchase Requisitions screen displays. |
| [Approve Purchase Orders at Subsidiary (Optional)](#unique_18) [page] 39 | Purchasing Manager | Approve Purchase Orders |  |
| [Review Purchase Order Message](#unique_19)at Subsidiary [page] 40 | Purchaser | Manage Purchase Orders | Purchase Order Message created successfully |
| [Review Order Confirmation](#unique_20) at Subsidiary [page] 41 | Purchaser | Manage Purchase Orders | Order Confirmation received from Headquarters |
| Send Order Confirmation (Update) to Customer [page] 43 | Internal Sales Represen-tatice | Manage Sales Orders | Order Confirmation (Update) Send to Customer |
| [Create Delivery](#unique_16) at Headquarters [page] 43 | Shipping Specialist | Create Outbound Deliveries | The Create Outbound Deliveries screen displays. |
| [Create Attachment for Delivery at Headquarters (Optional)](#unique_17) [page] 43 | Shipping Specialist | Display Outbound Delivery | The Display Outbound Delivery: Initial Screen displays |
| [Execute Picking](#unique_18)at Headquarters [page] 43 | Shipping Specialist | My Outbound Delivery Monitor |  |
| [Check Batches at Headquarters (Optional)](#unique_19) [page] 44 | Shipping Specialist | Change Outbound Delivery | Batch numbers are checked |
| [Split Outbound Delivery at Headquarters (optional)](#unique_20) [page] 44 | Shipping Specialist | Split Outbound Delivery |  |
| [Add Freight Costs at Headquarters (Optional)](#unique_21) [page] 44 | Shipping Specialist | Change Outbound Delivery |  |
| [Post Goods Issue](#unique_22) at Headquarters [page] 45 | Shipping Specialist | My Outbound Delivery Monitor | The goods issue is posted. |
| [Review Shipping Notification](#unique_22) at Subsidiary [page] 45 | Purchaser | Manage Purchase Orders | Inbound Delivery created successfully |
| [Post Statistical Goods Receipt](#unique_25) at Subsidiary [page] 46 | Warehouse Clerk | Post Goods Movement | The Post Goods Receipt for Purchase Order screen displays. |
| [Create Billing Document](#unique_26) at Subsidiary [page] 48 | Billing Clerk | Create Billing Documents (Work List) | The Create Billing Document screen displays. |
| [Create Attachment for Billing at Subsidiary (Optional)](#unique_27) [page] 51 | Billing Clerk | Display Billing Documents | The Display Billing Document screen displays. |
| [Create Pro Forma Invoice – for Free or Charge Items at Subsidiary (Optional)](#unique_28) [page] 52 | Billing Clerk | Create Billing Documents | Pro Forma invoice is created. |
| [Create Billing Document](#unique_24) at Headquarters [page] 54 | Billing Clerk | Create Billing Documents | The Create Billing Document screen displays. |
| [Create Attachment for Billing at Headquarters (Optional)](#unique_25) [page] 54 | Billing Clerk | Display Billing Document | The Display Billing Document screen displays. |
| Check [Vendor Invoice](#unique_29) at Subsidiary [page] 54 | Accounts Payable Accountant | Create Supplier Invoice(Advanced) |  |

### 7.9 Test Procedures

This section describes procedures for each process step that belongs to this scope item.

The Enterprise search function provides a central entry point for finding business objects in your company from different sources using a single search request, you can search for objects such as: Apps, factsheets for business objects. From the data found, you can go directly to the respective apps and factsheets to display, edit the data or find related objects.

How to access and check a factsheet:

- Log onto the SAP Fiori Launchpad using the respective user, for example, Internal Sales Representative.
- Access the Enterprise Search Bar and choose the magnifying glass button in the upper right corner.
- The Enterprise Search bar is displayed, two filter fields appear left to the search button. Enter your Search Criteria and choose the business object type, for example, Sales orders from drop-down menu in 1st field, enter sales order number in 2nd field and choose Search, the sales order is listed.
- Choose the sales order number link: the system navigates to the factsheet screen and sales order related information is integrated and summarized in one Fiori page, you can get detailed data via choosing the corresponding links.

There are factsheets available for the following objects: (Visible depending on the assigned role)

- Sales order
- Quotation
- Billing document
- Credit Memo
- Debit Memo
- Customer 360 Fact sheet

### 7.9.1 Sales Inquiry at Subsidiary (1IQ) (Optional)

Note Sales Inquiry (1IQ)

Context

This scope item describes the process for a standard Sales Inquiry.

Procedure

Complete all the activities described in the test script of the scope item: Sales Inquiry (1IQ).

Note If you want to use the optional link between scope item Sales Inquiry (1IQ) and Sales Processing using Third-Party with Shipping Notification (BD3) this reference only works if you use consistent master data (such as Business Partner for the customer inquiry and the customer sales order).

### 7.9.2 Sales Contract Management at Subsidiary (I9I) (Optional)

Note Sales Contract Management (I9I)

Context

This scope item describes the process for Sales Quantity contract.

Procedure

Complete all the activities described in the test script of the scope item: Sales Contract Management (I9I).

Note If you want to use the optional link between scope item Sales Contract Management (I9I) and Sales Processing using Third-Party with Shipping Notification (BD3) this reference only works if you use consistent master data (such as Business Partner for the customer quotation and the customer sales order).

### 7.9.3 Sales Quotation at Subsidiary (BDG) (Optional)

Note Sales Quotation (BDG)

Context

This scope item describes the process for a standard sales quotation.

Procedure

Complete all the activities described in the test script of the scope item: Sales Quotation (BDG).

Note If you want to use the optional link between scope item Sales Quotation (BDG) and Sales Processing using Third-Party with Shipping Notification (BD3) this reference only works if you use consistent master data (such as Business Partner for the customer quotation and the customer sales order).

### 7.9.4 Create Third-Party Sales Order at Subsidiary

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| Test Case ID | <X.XX> | Tester Name |  | Testing Date | Enter a test date. |
| Business Role(s) |  |  |  |  |  |
| Responsibility | <State Service Provider, Customer or Joint Service Provider and Customer> | Duration | Enter a duration. |  |  |

Context

In this activity, you create a third-party sales order.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log onto the SAP Fiori launchpad as an Internal Sales Representative. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Manage Sales Orders. | The Manage Sales Orders screen displays. |  |
| 3 | Navigate to Create Sales Order Screen | Choose Create Sales Order. |  |  |
| 4 | Enter Sales Document Type | Make the following entries and press Enter:Order Type: ORSales Organization: 1010Distribution Channel: 10Division: 00 |  |  |
| 5 | Enter Order Details | Make the following entries and press Enter:Sold-To Party: 10100001Cust. Reference: PO numberReq.Deliv Date: <Date>Material: <Material Number>, for example TG10Order Quantity: <quantity>, for example, 10Item Category: CB1.Note You can manually change the item category to CB3 if the item is free of charge for 3rd party sales order with shipping notification. |  |  |
| 6 | Save | Choose Save.If pop-up screen Standard Order: Purchase Order Scheduling displays, choose Complete dlv. and then choose Save. | The third-party sales order is created. A Purchase Requisition is created automatically. The order confirmation is only processed when the purchase requisition is converted into a purchase order.Make a note of the sales order number:You can find the purchase requisition number on the Schedule Lines tab at item level. |  |

Printing Form

The print-out of the order confirmation is executed automatically, or manually only after the purchase requisition has been transferred to a purchase order.

For instructions on manually printing the output, see Manual Printing below.

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log onto the SAP Fiori launchpad as an Internal Sales Representative. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Manage Sales Orders. | The Manage Sales Orders screen displays. |  |
| 3 | Search For Sales Order | Enter search terms (such as a sales order number) in the filter bar and choose Go. | The sales order is displayed in the result list. |  |
| 4 | Navigate to Sales Order Screen | Select the sales order number and choose Display Sales order. | The Display Sales Order xxx: Overview screen displays. |  |
| 5 | Check Output Condition | Choose More > Extras > Output > Header > Edit . | The Display Standard Order xxx: Output screen displays. |  |
| 6 | Display Print Preview | Mark the Output line, then choose Display PDF Document. | Preview for PDF document displays. |  |

In the Manage Sales Orders app, you can navigate to a fact sheet:

- On the Manage Sales Orders screen, enter search terms in the filter bar and choose Go.
- In the search result, select your sales order number and choose Sales Order Number.

### 7.9.5 Create Attachment for Sales Order at Subsidiary (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| Test Case ID | <X.XX> | Tester Name |  | Testing Date | Enter a test date. |
| Business Role(s) |  |  |  |  |  |
| Responsibility | <State Service Provider, Customer or Joint Service Provider and Customer> | Duration | Enter a duration. |  |  |

Context

In this activity, you will upload an attachment for the sales order.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log onto the SAP Fiori launchpad as an Internal sales Representative. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Display Sales Orders. | The Display Sales Documents view displays. |  |
| 3 | Enter sales Order number | Enter the respective order number created in previous step and press Enter. | The Display Standard Order XXX: Overview view displays. |  |
| 4 | Create Attachment for sales Order | Choose Services for Object on top right corner of view. Choose Create Attachment. | Import file view displays. |  |
| 5 | Import File | Choose Import from native file system.In the Open view, choose local path and file, and choose Open.Choose OK.Navigate Back to Import file view, select file item, and select Choose. | The attachment is successfully created. |  |
| 6 | Check Attachment | Choose Services for Object on top right corner of view, and choose Attachment list. | Attachment brings up in the Service: Attachment list view. |  |

### 7.9.6 Change Order Quantity at Subsidiary (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| Test Case ID | <X.XX> | Tester Name |  | Testing Date | Enter a test date. |
| Business Role(s) |  |  |  |  |  |
| Responsibility | <State Service Provider, Customer or Joint Service Provider and Customer> | Duration | Enter a duration. |  |  |

Context

In this activity, you change the order quantity. This step is optional.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log onto the SAP Fiori launchpad as an Internal Sales Representative. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Manage Sales Orders. | The Manage Sales Orders screen displays. |  |
| 3 | Select Order Number to Change | In Manage Sales Orders, choose on the sales order number and choose Change Sales Order. |  |  |
| 4 | Change Document | Change the quantity as needed. |  |  |
| 5 | Save Document | Save your entries. | The sales order quantity has been changed. If a PO existed, you have changed the PO quantity. Otherwise, you have changed the requisition quantity. |  |

### 7.9.7 Display List of Purchase Requisitions to be Assigned at Subsidiary

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| Test Case ID | <X.XX> | Tester Name |  | Testing Date | Enter a test date. |
| Business Role(s) |  |  |  |  |  |
| Responsibility | <State Service Provider, Customer or Joint Service Provider and Customer> | Duration | Enter a duration. |  |  |

Context

This activity is performed when you want to review your Purchase Requisitions and assign them to a vendor.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log onto the SAP Fiori launchpad as a Purchaser. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Manage Purchase Requisitions.If you want to use the Save Draft feature in this app, you have to use a personalized user. | The Manage Purchase Requisitions screen displays. |  |
| 3 | Find Relevant Purchase Requisition | Input selection criteria in the Filter Bar and choose Go if necessary:Plant: <Plant>, for example, 1010 | You can find the purchase requisition number in the create sales order steps. |  |
| 4 | Choose Sources of Supply | Click X Source in the row of your purchase requisition, and choose a source by clicking on it.For EDI, choose vendor 10300084. | The Source of Supply is assigned. |  |

### 7.9.8 Convert Assigned Requisitions into Purchase Orders at Subsidiary

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| Test Case ID | <X.XX> | Tester Name |  | Testing Date | Enter a test date. |
| Business Role(s) |  |  |  |  |  |
| Responsibility | <State Service Provider, Customer or Joint Service Provider and Customer> | Duration | Enter a duration. |  |  |

Context

You perform this activity when you want to convert the assigned requisitions into purchase orders.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log onto the SAP Fiori launchpad as a Purchaser. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Manage Purchase Requisitions. | The Manage Purchase Requisitions screen displays. |  |
| 3 | Find Purchase Requisition | Enter selection criteria in the Filter Bar and choose Go if necessary:Plant: <Plant>, for example, 1010. |  |  |
| 4 | Create Purchase Order | Choose the purchase requisition and click Create Purchase Order above the result list.Note If any warning message appears, choose OK to skip it. | The Purchase Orders Preview screen displays. |  |
| 5 | Confirm Purchase Order Creation | Select the purchase order type Standard PO and choose OK.Note If any warning message displays, choose OK. |  |  |
| 6 | Submit Purchase Order | Choose the purchase order and choose Submit in the bottom of the screen.The purchase order number shows in the screen. | The purchase order is created in the SAP system. The system creates a message for the purchase order, so that the information from the purchase order can be transmitted to the vendor.Note The print-out of the order confirmation is executed after the Purchase Order is created automatically and immediately. For printing handling and the processing of purchase orders, see Procurement of Direct Materials, the Review Purchase Order step. |  |

### 7.9.9 Approve Purchase Orders (Optional) at Subsidiary

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| Test Case ID | <X.XX> | Tester Name |  | Testing Date | Enter a test date. |
| Business Role(s) |  |  |  |  |  |
| Responsibility | <State Service Provider, Customer or Joint Service Provider and Customer> | Duration | Enter a duration. |  |  |

Context

In this procedure, you release a purchase order. If the total amount of PO >= 500 EUR and purchase group is 003. then the PO should do the approval.

Prerequisite

A purchase order must exist for release.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log onto the SAP Fiori launchpad as a Purchasing Manager. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open My Inbox. | The My Inbox view displays. |  |
| 3 | Input Release Code | Search for Purchase Order with In Approval status. | The Purchase Orders without follow-on documents (w/o status Follow-On Documents) and a net value of 500 EUR or more have the In Approval status. |  |
| 4 | Select purchase order | Select the Purchase order in left of the screen and choose Approve at the right of the bottom. | The Submit Decision dialog box displays. |  |
| 5 | Release documents | Input the approved reason if needed.Choose Submit. | The Purchase Order is approved. The sales order will be automatically created at headquarters SAP system. |  |

Note For printing handling and the processing of purchase orders, see scope item Procurement of Direct Materials, the Review Purchase Order chapter.

### 7.9.10 Review Purchase Order Message at Subsidiary

For details refer to Scope Item 2EJ Integration of SAP Cloud ERP Procurement with Headquarters, the Review Purchase Order chapter.

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| Test Case ID | <X.XX> | Tester Name |  | Testing Date | Enter a test date. |
| Business Role(s) |  |  |  |  |  |
| Responsibility | <State Service Provider, Customer or Joint Service Provider and Customer> | Duration | Enter a duration. |  |  |

Use

In this procedure, you can preview an existing purchase order.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad using the Purchaser role. | The SAP Fiori Launchpad is displayed. |  |
| 2 | Open Manage Purchase Orders App | Open Manage Purchase Orders. | The Manage Purchase Orders screen is displayed.A list of already created purchase orders is displayed. |  |
| 3 | Select Purchase Order | Search for purchase order xxx and choose Go.Select the row with the purchase order you want to display and review the purchase order. |  |  |

### 7.9.11 Review Order Confirmation at Subsidiary

In case you have received the Order Confirmation from you Headquarters, you can check it by opening the Manage Purchase Orders App. Choose the Purchase Order details and go to the Confirmations tab. See also Scope Item 2EJ Integration of SAP Cloud ERP Procurement with Headquarters, the Review Order Confirmation chapter 2EJ below.

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| Test Case ID | <X.XX> | Tester Name |  | Testing Date | Enter a test date. |
| Business Role(s) |  |  |  |  |  |
| Responsibility | <State Service Provider, Customer or Joint Service Provider and Customer> | Duration | Enter a duration. |  |  |

Use

In this procedure, you can review the order confirmation.

Note You will be able to process this test steps ONLY after the corresponding Headquarters SAP system has sent an order confirmation.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad using the Purchaser role. | The SAP Fiori Launchpad is displayed. |  |
| 2 | Open Manage Purchase Orders App | Open Manage Purchase Orders. | The Manage Purchase Orders screen is displayed.A list of already created Purchase Orders is displayed. |  |
| 3 | Select Purchase Order | Search for purchase order xxx and choose Go.Select the row with purchase order xxx. | Purchase Order xxx is displayed. |  |
| 4 | Review Order Confirmation | In Item Detail section, choose Confirmation tab.When the external confirmation from your Headquarters has been sent, you should see an additional line in the table showing following information:CC (Confirm. Cat.): ABQuantity: xDelivery Date: x | Order Confirmation is displayed. |  |

### 7.9.12 Send Order Confirmation (Update) to Customer at Subsidiary

In case the Vendor confirmed a different Delivery Date, this Date is populated into the Sales Order. The changed date might be communicated to the Customer as well using an Order Confirmation. For details please refer to the Printing Form section in the Create Sales Orders step.

### 7.9.13 Create Delivery at Headquarters

Purpose

In this activity, you create the delivery

Procedure

Once the goods have been released for delivery the shipping specialist will create delivery against sale orders in the SAP system at headquarters.

### 7.9.14 Create Attachment for Delivery at Headquarters (Optional)

Choose the suitable documents/files that will be attach to delivery from SAP System at Headquarters this is optional.

### 7.9.15 Execute Picking at Headquarters

Purpose

The picking process involves taking goods from a storage location and staging the right quantity in a picking area where the goods are prepared for shipping.

Procedure

Execute picking of goods is done by warehouse management system. It is done via a transfer order, which is used for picking list and to withdraw the goods from the stock at Headquarters and dropped at the required shipping point.

### 7.9.16 Check Batches at Headquarters (Optional)

Purpose

In this activity, you check the batch number assignment to the material.

Procedure

This is an optional step you can attach batch numbers to materials with a dedicated quantity, expiry date and other warranty information and the batch is then tracked throughout your shipping point that is from Headquarters all the way to the customer.

### 7.9.17 Split Outbound Delivery at Headquarters (optional)

Purpose

In this process step, the user can split up single or multiple items from an existing, completely picked Outbound Delivery and move them to a new delivery document before posting Goods Issue.

Procedure

Once you have completely picked an outbound delivery order in Extended Warehouse Management (EWM). You find that you cannot load the complete quantity. That time you can create an outbound delivery for individual delivery items and therefore perform an outbound delivery split. You can select Items from the SAP system at Headquarters and split an outbound delivery order or an outbound delivery.

### 7.9.18 Add Freight Costs at Headquarters (Optional)

Purpose

You might want to add the actual freight costs to the Outbound Delivery after picking where you know the exact weights and freight charges.

Procedure

The freight is part of an asset’s cost, it is to be considered an extension of the asset’s overall value. Enter the freight-in amount in the Unit price field. Dates on forms for the purchase and freight-in do not need to match. Average costs will be correctly adjusted as of the transaction date in SAP system for the freight-in charge.

### 7.9.19 Post Goods Issue at Headquarters

Purpose

In this activity, you post the goods issue.

Procedure

The post goods issue is made once the delivery is created. When a post goods issue is made in SAP system at Headquarters, the ownership of the materials is transferred to the final customer. On post goods issue, stock gets reduced from the inventory. Similarly, stock figures also get updated in General Ledger. This increases the *Cost of Goods Sold* and reduces the inventory figure.

### 7.9.20 Review Shipping Notification at Subsidiary

In case your Headquarters have sent Advanced shipping notification, you can review it in the purchase order in item detail under confirmation tag. Refer below Scope Item 2EJ Integration of SAP Cloud ERP Procurement with Headquarters, the *Review Shipping Notification* chapter.

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| Test Case ID | <X.XX> | Tester Name |  | Testing Date | Enter a test date. |
| Business Role(s) |  |  |  |  |  |
| Responsibility | <State Service Provider, Customer or Joint Service Provider and Customer> | Duration | Enter a duration. |  |  |

Use

In this procedure, you can review the shipping notification.

Note You will be able to process this test steps ONLY after the corresponding Headquarters SAP system has sent a shipping notification.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad using the Purchaser role. | The SAP Fiori Launchpad is displayed. |  |
| 2 | Open Manage Purchase Orders App | Open Manage Purchase Orders. | The Manage Purchase Orders screen is displayed.A list of already created Purchase Orders is displayed. |  |
| 3 | Select Purchase Order | Search for purchase order xxx and choose Go.Select the row with purchase order xxx. | Purchase Order xxx is displayed. |  |
| 4 | Review Shipping Notification | In Item Detail section, choose Confirmation tab.When the external shipping notification from your Headquarters has been sent, you should see an additional line in the table showing following information:CC (Confirm. Cat.): LAQuantity: xDelivery Date: xInbound Delivery: xxx | Shipping Notification is displayed. Note the inbound delivery number. |  |

### 7.9.21 Post Statistical Goods Receipt at Subsidiary

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| Test Case ID | <X.XX> | Tester Name |  | Testing Date | Enter a test date. |
| Business Role(s) |  |  |  |  |  |
| Responsibility | <State Service Provider, Customer or Joint Service Provider and Customer> | Duration | Enter a duration. |  |  |

Context

After the vendor has sent the shipping notification, you post a statistical goods receipt

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log onto the SAP Fiori launchpad as a Warehouse Clerk. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Post Goods Movement. | The Post Goods Receipt for Purchase Order / Inbound Delivery screen displays. |  |
| 3 | Choose Good Receipt | Make the following entry and press Enter:Executable Action in Transaction MIGO: Goods ReceiptReference Document for MIGO Transaction: Inbound Delivry |  |  |
| 4 | Choose GR goods receipt and enter purchase order | Make the following entrie, and press Enter.Field next to Inbound Delibvery: <Inbound Delivery Number> |  |  |
| 5 | Change the quantity if necessary | If necessary, change the quantity in Item details, Quantity tab. |  |  |
| 6 | Enter Goods Recipient | In Detail data, navigate to the Where tab.Make the following entries, and press Enter.Goods Recipient: for example 101A |  |  |
| 7 | Select Item OK | Select Item OK or Item overview checkbox at the bottom of the screen. |  |  |
| 8 | Save the documents | Choose Post. | The system generates a material document.You may record down the posted material document number at the bottom. |  |

Note To view the material document in FLP, open Display Material Documents List.

Financial postings

| Material | Debited Accounts | Credited Accounts | Cost Element / CO Object |
| --- | --- | --- | --- |
| Trading Good (HAWA) | 51600000 Consumption - Trading Goods | 21120000 GR/IR | none |

### 7.9.22 Create Billing Document at Subsidiary

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| Test Case ID | <X.XX> | Tester Name |  | Testing Date | Enter a test date. |
| Business Role(s) |  |  |  |  |  |
| Responsibility | <State Service Provider, Customer or Joint Service Provider and Customer> | Duration | Enter a duration. |  |  |

Context

In this activity, you handle billing.

Procedure

Table 2: Create Billing Document

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log onto the SAP Fiori launchpad as a Billing Clerk. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Create Billing Documents. | The Create Billing Document screen displays. |  |
| 3 | Define billing setting | Choose Billing Settings at the right bottom of the screen.There are four settings. You should turn all of these settings into ON.Enter Billing Data before billingSeparate Billing Documents for Each Billing Due List ItemAutomatically Post Billing DocumentsDisplay Billing Document after creation |  |  |
| 4 | Search for billing list | In the search condition, use criteria if necessary. | Sales document(s) will display in the result. |  |
| 5 | Choose Individual Billing Document | Select the row of sales document created previously and choose Create. | The Create Billing Documents window displays. |  |
| 6 | Maintain Billing Date | Choose billing type Invoice (F2) and maintain billing date, such as the current date.Choose OK. | The new billing document will be created. |  |
| 7 | Save the Billing Document | Choose Save. |  |  |
| 8 | Display Billing Document after Creation | The billing document displays automatically. Make a note of the billing document number: __________. | The system generates an invoice for billing. |  |

Table 3: Manage billing documents

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Access the SAP Fiori App | Open Manage Billing Documents． | The Manage Billing Document screen displays. |  |
| 2 | Search the billing document created in previous step | Input the billing document number recorded in previous step.Press Enter. | The billing document created in the previous step displays. |  |
| 3 | Display the billing document | Select the billing document item and choose Display. | The billing document displays. |  |
| 4 | Check Output Condition | On the Billing Document screen, choose the last assignment block - Output Items. | There is one entry in the item and the output type is BILLING_DOCUMENT. |  |
| 5 | Display Print Preview | On the Billing Document screen choose Preview. | Preview for PDF document displays. |  |
| 6 | Cancel Billing Document (Optional) | Select certain billing document and choose Cancel billing Docs. | A log displays: Billing Document Canceled. |  |
| 7 | Update new Attachment (Optional) | In the Edit mode, you can add, delete and update the attachments. Save your changes by choosing Save in the footer bar. |  |  |
| 8 | Update new Text (optional) | In the Edit mode, you can add, delete and update these texts. Save your changes by choosing Save in the footer bar. |  |  |

Financial postings

| Material | Debited Accounts | Credited Accounts | Cost Element / CO Object |
| --- | --- | --- | --- |
| Trading Good (HAWA) | 12100000 G/L (for Item category CB1)44002000 G/L (for Item category CB3) | 41000000 Rev Domestic Prod22000000 (only for CB1) Output tax (MWS) | None |

### 7.9.23 Create Attachment for Billing at Subsidiary (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| Test Case ID | <X.XX> | Tester Name |  | Testing Date | Enter a test date. |
| Business Role(s) |  |  |  |  |  |
| Responsibility | <State Service Provider, Customer or Joint Service Provider and Customer> | Duration | Enter a duration. |  |  |

Context

In this activity, you will upload the attachment in billing document.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log onto the SAP Fiori launchpad as a Billing Clerk. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Display Billing Documents. | The Display Billing Documents screen displays. |  |
| 3 | Enter the Billing number | On the Display Billing Documents screen, enter the respective invoice number created in the previous step and choose Continue. | The F2 Invoice xxx(F2) Display: Overview of Billing Items screen displays. |  |
| 4 | Create Attachment for Delivery | Choose Services for Object on top right corner of the screen. Choose Create Attachment. | The Import file screen displays. |  |
| 5 | Import File | Choose Import from native file system.In the Open window, select a local path or file, and choose Open.Choose OK in pop up screen that shows import finished.Navigate back to the Import file screen and select a file item.Choose Choose. | The attachment is successfully created. |  |
| 6 | Check Attachment | Choose Services for Object on top right corner of the screen. Choose Attachment list. | Attachment brings up on theService: Attachment list screen. |  |

### 7.9.24 Create Pro Forma Invoice – for Free or Charge Items at Subsidiary (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| Test Case ID | <X.XX> | Tester Name |  | Testing Date | Enter a test date. |
| Business Role(s) |  |  |  |  |  |
| Responsibility | <State Service Provider, Customer or Joint Service Provider and Customer> | Duration | Enter a duration. |  |  |

Context

In this activity, you handle Pro Forma invoice only when you are using item category CB3 in the previous steps.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log onto the SAP Fiori launchpad as a Billing Clerk. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Create Billing Documents. | The Create Billing Documents screen displays. |  |
| 3 | Define billing setting | Choose Billing Settings at the right bottom of the screen.There are four settings. You should turn all of these settings into ON.Enter Billing Data before billingSeparate Billing Documents for Each Billing Due List Item.Automatically Post Billing DocumentsDisplay Billing Document after creation. |  |  |
| 4 | Search for billing list | In the search condition, use criteria if necessary. | Sales document(s) displays in the result. |  |
| 5 | Choose Individual Billing Document | Select the row of delivery document created previously and choose Create. | The Create Billing Documents window displays. |  |
| 6 | Maintain Billing Date | Choose billing type Pro Forma for Order (F5) and maintain billing date, such as the current date.Choose OK. | The new billing document will be created. |  |
| 7 | Display Billing document after creation | The billing document displays automatically. Make a note of the billing document number: __________. | The system generates an invoice for billing. |  |

Table 4: Manage billing documents

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Access APP | Open APP Manage Billing Documents under Sales Billing Document. | The screen Manage Billing Document displays. |  |
| 2 | Search the billing document created in previous step | Input the billing document number recorded in the previous step. Press Enter. | The billing document created in the previous step displays. |  |
| 3 | Display the billing document | Select the billing document item and choose Display. | The billing document displays. |  |
| 4 | Check Output Condition | On the Billing Document screen, choose the last assignment block - Output Items. | There is one entry in the item and the output type is BILLING_DOCUMENT. |  |
| 5 | Display Print Preview | On the Billing Document screen choose Preview. | Preview for PDF document displays. |  |
| 6 | Cancel Billing Document (Optional) | Select certain Billing document and choose Cancel billing Docs. | A log displays: Billing Document Canceled. |  |
| 7 | Update new Attachment (Optional) | In the Edit mode, you can add, delete and update the attachments. Save your changes by choosing Save in the footer bar. |  |  |
| 8 | Update new Text (optional) | In the Edit mode, you can add, delete and update these texts. Save your changes by choosing Save in the footer bar. |  |  |

### 7.9.25 Create Billing Document at Headquarters

This **billing document** number is **created** at the end of this post goods issue process at Headquarters. Once the goods have been delivered to the customers the headquarter must bill it to the subsidiary. As soon as the headquarters create the billing documents the invoice will be automatically generated to subsidiary.

### 7.9.26 Create Attachment for Billing at Headquarters (Optional)

In standard SAP system, you can see help documents stating that proof of delivery can be used for confirming material delivery to the customer and its quantity. This is done by creating attachment for billing at Headquarters by entering the respective invoice number generated in the previous step.

### 7.9.27 Check Vendor Invoice at Subsidiary

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| Test Case ID | <X.XX> | Tester Name |  | Testing Date | Enter a test date. |
| Business Role(s) |  |  |  |  |  |
| Responsibility | <State Service Provider, Customer or Joint Service Provider and Customer> | Duration | Enter a duration. |  |  |

Use

In this procedure, a supplier invoice is displayed.

You will be able to process this test steps ONLY after the corresponding Headquarters system has sent an invoice.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad using the Accounts Payable Accountant role. | The SAP Fiori Launchpad is displayed. |  |
| 2 | Open Supplier Invoice List | Open Supplier Invoice List. | The Supplier Invoice List screen is displayed. |  |
| 3 | Search for Supplier Invoice | On the Supplier Invoice List, search for your invoice and display it. | The Billing document number from the Headquarters will be populated in the Reference field of the Supplier Invoice at the Subsidiary. |  |

Context

In this activity, you enter an invoice.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log onto the SAP Fiori launchpad as an Accounts Payable Accountant. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Create Supplier Invoice(Advanced). |  |  |
| 3 | Select Company Code | Make the following entries and press Enter.Company Code: 1010 | The Enter Incoming Invoice: Company Code 1010 screen displays. |  |
| 4 | Find Reference Document | Make the following entries and press Enter.Transaction: InvoiceReference: <input reference information>Invoice Date: <mm.dd.yyyy>.PO number: <purchase order number from previous steps> on the PO reference tab in lower screen area. |  |  |
| 5 | Enter Tax Information | Enter the invoice amount including taxes and select the Calculate Tax checkbox. Choose the appropriate tax code. | The amount can be checked from the Balance field. |  |
| 6 | Post Invoice | Choose Menu > More > Invoice Document > Post . | The system generates a logistics invoice and an accounting document. |  |

Financial postings

| Material | Debited Accounts | Credited Accounts | Cost Element / CO Object |
| --- | --- | --- | --- |
| Trading Good (HAWA) | 12600000 Input Tax (VST)21120000 GR/IR | Vendor Account (21100000 G/L) | none |

### Appendix

### 7.10.1 Process Integration

The process to be tested in this test script is part of a chain of integrated processes.

#### 7.10.2 Succeeding Processes

After completing the activities in this test script, you can continue testing the following business processes:

| Process | Business Condition |
| --- | --- |
| Accounts Payable (J60) | Post the outgoing payment.Using the master data from this document, complete the following activities described in the test script:Post Payments Using the Payment ProgramPost Manual Outgoing payment |
| Accounts Receivable (J59) | Posting a Customer Invoice in Accounting, etc.Using the master data from this document, complete the following activities described in the test script:Posting a Customer Invoice in AccountingOverdue Receivables, Display Customer BalancesManage Customer Line Items |
| Sales Order Fulfilment Monitoring(BKK) (optional) | This scope item describes the collection of periodic activities such as day ending activities, or reporting.Using the master data from this document, complete all the activities described in the Test Script of the scope item:Review Incomplete SD Documents (deliveries),Review Sales Documents blocked for billingReview Log of collective invoice creation |

#### Scheduling Job (alternative)

#### 7.10.3.1 Job Scheduling for Billing Creation (Alternative)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| Test Case ID | <X.XX> | Tester Name |  | Testing Date | Enter a test date. |
| Business Role(s) |  |  |  |  |  |
| Responsibility | <State Service Provider, Customer or Joint Service Provider and Customer> | Duration | Enter a duration. |  |  |

Context

In this process step, you can schedule a background job for creation billing documents.

This app can be used as an alternative instead of the manual creation of billing documents.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log onto the SAP Fiori launchpad as a Billing Clerk. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Schedule Billing Creation. | The Application Jobs screen displays. The app automatically shows the history of application jobs. |  |
| 3 | Create Billing Creation Schedule | Choose New to define a new job for billing creation. | The New Job screen displays. Job Template should default as Schedule Billing Creation. |  |
| 4 | Job Parameters | Define scheduling options and parameters for the batch job if necessary.Choose Check. | The system displays the message Go ahead and schedule the job. |  |
| 5 | Schedule | Choose Schedule. | A billing creation job is scheduled. Screen goes back to Application Jobs. |  |
| 6 | Check Billing Creation Job Log | On the Application Jobs screen, after job item’s status turned to Finish, choose Job Log.Note Choose the Magnifier, and the job list will refresh. | The log details display. |  |

##### 7.10.3.2 Job Scheduling for Billing Release (Alternative)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| Test Case ID | <X.XX> | Tester Name |  | Testing Date | Enter a test date. |
| Business Role(s) |  |  |  |  |  |
| Responsibility | <State Service Provider, Customer or Joint Service Provider and Customer> | Duration | Enter a duration. |  |  |

Context

In this process step, you can schedule a background job for release billing documents to accounting.

This app can be used as an alternative instead of the manual release to accounting for billing documents.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log onto the SAP Fiori launchpad as a Billing Clerk. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Schedule Billing Release. | The Application Jobs screen displays. The app automatically shows the history of application jobs. |  |
| 3 | Create Billing Release Schedule | Choose New to define a new job for billing creation. | The New Job screen displays. Job Template default should be Schedule Billing Release. |  |
| 4 | Job Parameters | Define scheduling options and parameters for the batch job if necessary.Choose Check. | The system displays the message Go ahead and schedule the job. |  |
| 5 | Schedule | Choose Schedule. | A billing release job is scheduled. Return to Application Jobs. |  |
| 6 | Check Billing Release Job Log | On the Application Jobs screen, after job item’s status turned to Finish, choose Job Log.Note Choose the Magnifier, and the job list will refresh. | The log details display. |  |

##### 7.10.3.3 Job Scheduling for Billing Output (Alternative)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| Test Case ID | <X.XX> | Tester Name |  | Testing Date | Enter a test date. |
| Business Role(s) |  |  |  |  |  |
| Responsibility | <State Service Provider, Customer or Joint Service Provider and Customer> | Duration | Enter a duration. |  |  |

Context

In this process step, you can schedule a background job for when and how billing documents are sent to customer.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log onto the SAP Fiori launchpad as a Billing Clerk. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Schedule Billing Output. | The Application Jobs screen displays. The app automatically shows the history of application jobs. |  |
| 3 | Create Billing Output Schedule | Choose New to define a new job for billing creation. | The New Job screen displays. Job Template should default as Schedule Billing Output. |  |
| 4 | Job Parameters | Define scheduling options and parameters for the batch job if necessary.Choose Check. | The system displays the message Go ahead and schedule the job. |  |
| 5 | Schedule | Choose Schedule. | A billing release job is scheduled. Return to Application Jobs. |  |
|  | Check Billing Output Job Log | On the Application Jobs screen, after job item’s status turned to Finish, choose Job Log.Note Choose Magnifier, and the job list will refresh. | The log details display. |  |

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

## Suspected conflicts

> [!warning] Conflict
> Flagged while digesting this document, not verified: Section 4.2 lists IDocs DELVRY07 and INVOIC2, but section 5.2.1 lists DESADV and INVOIC02 for the same ASN and billing messages.

> [!warning] Conflict
> Flagged while digesting this document, not verified: Approval threshold stated as 500 USD in workflow configuration but 500 EUR in the approval step.

> [!warning] Conflict
> Flagged while digesting this document, not verified: Cover says June 2026 while copyright says 2020 and last revision is 2021.

> [!warning] Conflict
> Flagged while digesting this document, not verified: Master data text refers to 'section 5.3' which does not exist; sample vendor 10300084 vs HQ ID 10300089 in config examples.

## Connections
- part-of :: [[_cluster]]
- see-also :: [[16-two-tier-erp-and-central-finance/two-tier-erp-procurement-by-subsidiary-from-headquarters-replenishment]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/General/Two-Tier_ERP_Assets_User_Guides/Two-Tier_ERP_Assets_User_Guides/Sales & Service/S4CLD2608_2T_ Drop Shipment_User_Guide.docx` — full document · extracted with `mammoth` · 83,440 chars in the whole document
