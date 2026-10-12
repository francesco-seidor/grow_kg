---
id: 16-two-tier-erp-and-central-finance/two-tier-erp-procurement-by-subsidiary-from-headquarters-replenishment
title: "Two-Tier ERP: Procurement by Subsidiary from Headquarters (Replenishments) (S4CLD2608_2T_Replenishment_Guide)"
description: "SAP Two-Tier ERP customer guide: subsidiary replenishment from HQ via EDI/IDoc (PO to sales order, ASN, billing), with configuration, master data and test script."
cluster: 16-two-tier-erp-and-central-finance
tags: [kb/two-tier-erp-and-central-finance, topic/subsidiary-replenishment-from-hq]
aliases: [S4CLD2608_2T_Replenishment_Guide]
keywords: [Subsidiary Procurement from Headquarters, two-tier replenishment, idoc integration, process prerequisites, vendor and customer master, material requirements planning, test script, tax code mapping, company code determination, buyer integration]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/General/Two-Tier_ERP_Assets_User_Guides/Two-Tier_ERP_Assets_User_Guides/Procurement/S4CLD2608_2T_Replenishment_Guide.docx]
confidence: low
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-246
topic: 16-two-tier-erp-and-central-finance/subsidiary-replenishment-from-hq
language: ""
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Two-Tier ERP: Procurement by Subsidiary from Headquarters (Replenishments) (S4CLD2608_2T_Replenishment_Guide)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/General/Two-Tier_ERP_Assets_User_Guides/Two-Tier_ERP_Assets_User_Guides/Procurement/S4CLD2608_2T_Replenishment_Guide.docx`, extracted with `mammoth`. Grouped under **Subsidiary Procurement from Headquarters** in Two-Tier ERP and Central Finance. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

|  |  |
| --- | --- |
| S/4HANA June 2026English |  |
|  | Two-Tier ERP: Procurement by Subsidiary from Headquarters (Replenishments) |
| SAP SE Dietmar-Hopp-Allee 16 69190 Walldorf Germany | Customer Guide |

Copyright

© 2025 SAP SE or an SAP affiliate company. All rights reserved.

No part of this publication may be reproduced or transmitted in any form or for any purpose without the express permission of SAP SE. The information contained herein may be changed without prior notice.

Some software products marketed by SAP SE and its distributors contain proprietary software components of other software vendors.

National product specifications may vary.

These materials are provided by SAP SE and its affiliated companies ("SAP Group") for informational purposes only, without representation or warranty of any kind, and SAP Group shall not be liable for errors or omissions with respect to the materials. The only warranties for SAP Group products and services are those that are set forth in the express warranty statements accompanying such products and services, if any. Nothing herein should be construed as constituting an additional warranty.

SAP and other SAP products and services mentioned herein as well as their respective logos are trademarks or registered trademarks of SAP SE in Germany and other countries. Please see http://www.sap.com/corporate-en/legal/copyright/index.epx#trademark for additional trademark information and notices.

| Revision | Change Date | Description |
| --- | --- | --- |
| 0 | 01.03.2018 | Initial version of document |
| 1 | 01.06.2020 | Review of the document |
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

[1 Purpose 8](#_Toc510514547)

[2 Value Proposition 8](#_Toc510514548)

[2.1 Business Requirements 8](#_Toc510514549)

[2.2 Two-Tier Solution 8](#_Toc510514550)

[3 Business Process Details 8](#_Toc510514551)

[3.1 Prerequisites 8](#_Toc510514552)

[3.2 Process Flow with Technical Details 9](#_Toc510514553)

[4 Technical Requirement 9](#_Toc510514554)

[4.1 Integration Requirements by using API 9](#_Toc510514555)

[4.2 Integration Requirements by using EDI/IDOC 10](#_Toc510514556)

[4.3 Reporting Requirements by using Analytical CDS Views 10](#_Toc510514557)

[4.4 Reporting Requirements by using Analytical API 10](#_Toc510514558)

[5 Configurations 10](#_Toc510514559)

[5.1 Configuration for SAP Cloud ERP 10](#_Toc510514560)

[5.1.1 Communication Arrangement in SAP Cloud ERP (Subsidiary) 10](#_Toc510514561)

[5.1.2 Tax Codes in SAP Cloud ERP (Subsidiary) 10](#_Toc510514562)

[5.1.3 Company Code determination in SAP Cloud ERP (Subsidiary) 11](#_Toc510514563)

[5.2 Configuration for SAP S/4HANA On Premise 11](#_Toc510514564)

[5.2.1 IDOC Configs at the On-Premise System (Headquarters) 11](#_Toc510514565)

[5.3 Configuration for SAP Cloud Integration 12](#_Toc510514566)

[6 Master Data 13](#_Toc510514567)

[6.1 Master Data for SAP Cloud ERP 13](#_Toc510514568)

[6.1.1 Vendor Master 13](#_Toc510514569)

[6.1.2 Condition Master 13](#_Toc510514570)

[6.1.3 Purchase Info Record 13](#_Toc510514571)

[6.2 Master Data for SAP S/4HANA On Premise 14](#_Toc510514572)

[6.2.1 Material Master 14](#_Toc510514573)

[6.2.2 Customer Master 14](#_Toc510514574)

[6.2.3 Condition Master 16](#_Toc510514575)

[6.2.4 Ship-to-Party determination at Headquarters against Subsidiary’s Plant 17](#_Toc510514576)

[6.2.5 Sales org determination at Headquarters 17](#_Toc510514577)

[7 Test Script 18](#_Toc510514578)

[7.1 Prerequisites 18](#_Toc510514579)

[7.2 System Access at Subsidiary 18](#_Toc510514580)

[7.3 Roles at Subsidiary 18](#_Toc510514581)

[7.4 Role at Headquarters 18](#_Toc510514582)

[7.5 Master Data, Organizational Data, and Other Data 19](#_Toc510514583)

[7.6 Preliminary Steps 20](#_Toc510514584)

[7.6.1 Create Scheduling Agreement 20](#_Toc510514585)

[7.6.2 Maintain Consumption Values 22](#_Toc510514586)

[7.6.3 OPTIONAL - Adjust Historical Requirements – to prerequisites 23](#_Toc510514587)

[7.7 Overview Table 26](#_Toc510514588)

[7.8 Test Procedure 28](#_Toc510514589)

[7.8.1 Manage PIRs for Material TG0011 at Subsidiary 28](#_Toc510514590)

[7.8.2 Option 2 - Manage PIRs Directly at Subsidiary 35](#_Toc510514591)

[7.9 Monitor Material Coverage at Subsidiary 36](#_Toc510514592)

[7.9.1 Run Material Requirements Planning(MRP) at Subsidiary 36](#_Toc510514593)

[7.9.2 Evaluate MRP result at Subsidiary 38](#_Toc510514594)

[7.10 Display MRP Run Master Data Issues at Subsidiary 39](#_Toc510514595)

[7.11 Display MRP Run Key Figures at Subsidiary 40](#_Toc510514596)

[7.12 Convert Assigned Requisitions into Purchase Orders at Subsidiary 41](#_Toc510514597)

[7.13 Approve Purchase Orders (Optional) at Subsidiary 43](#_Toc510514598)

[7.14 Review Purchase Order Message at Subsidiary 44](#_Toc510514599)

[7.15 Review Order Confirmation at Subsidiary 45](#_Toc510514600)

[7.16 Create Delivery at Headquarters 46](#_Toc510514601)

[7.17 Create Attachment for Delivery at Headquarters (Optional) 47](#_Toc510514602)

[7.18 Execute Picking at Headquarters 47](#_Toc510514603)

[7.19 Check Batches at Headquarters (Optional) 47](#_Toc510514604)

[7.20 Split Outbound Delivery at Headquarters (optional) 47](#_Toc510514605)

[7.21 Add Freight Costs at Headquarters (Optional) 48](#_Toc510514606)

[7.22 Post Goods Issue at Headquarters 48](#_Toc510514607)

[7.23 Review Shipping Notification at Subsidiary 48](#_Toc510514608)

[7.24 Confirm Quantities for Putaway at Subsidiary 50](#_Toc510514609)

[7.25 Option A: Post Goods Receipt at subsidiary 51](#_Toc510514610)

[7.26 Option B: Schedule Job for Goods Receipt at Subsidiary 52](#_Toc510514611)

[7.27 Create Billing Document at Headquarters 53](#_Toc510514612)

[7.28 Create Attachment for Billing at Headquarters (Optional) 53](#_Toc510514613)

[7.29 Check Vendor Invoice at Subsidiary 53](#_Toc510514614)

[8 Appendix 56](#_Toc510514615)

[8.1 Process Chains 56](#_Toc510514616)

[8.1.1 Preceding Processes 56](#_Toc510514617)

[8.1.2 Succeeding Processes 56](#_Toc510514618)

**Procurement by Subsidiary from Headquarters (Replenishments)**

## Purpose

This document will provide the detailed process on Two-Tier ERP solution for the process “Procurement by Subsidiary from Headquarters (Replenishments)” with process flow, technical requirements and followed with testing procedure.

## Value Proposition

### Business Requirements

The streamlined procurement and sales process between headquarters to subsidiary. The purpose of replenishment is to keep inventory flowing through the supply chain by maintaining efficient order and line item fill rates. The process helps prevent costly inventory overstocking.

### Two-Tier Solution

Through Two-Tier ERP solutions, there will be seamless orchestration between headquarters and subsidiary along with the following integration points.

1. Purchase order at subsidiary will be automatically transformed to sales order at headquarters.
2. Once the order in conformed at headquarters, subsidiary will receive order confirmation message.
3. Post goods issue at headquarters, in the subsidiary will automatically create inbound delivery of goods.
4. Headquarters create billing documents; corresponding supplier invoice will be created at Subsidiary

## Business Process Details

The Two-Tier ERP solution for Procurement by Subsidiary from Headquarters (Replenishments) is depicted in this document.

The process starts where material planner receives independent requirements for goods, then he runs material requirement planning and evaluates MRP result. Then purchase requisitions will be converted to purchase order on headquarters as the vendor. Once the purchase order is approved EDI based approach is used to automatically transform the purchase order information for sales order creation at Headquarters. Once the order in confirmed at headquarters, subsidiary will receive order confirmation message and purchase order in confirmed.

The shipping clerk creates delivery and sends it for shipment team at headquarters. Posting goods issue at the headquarters will send advance shipping notification to subsidiary through EDI based approach to create inbound delivery. Once the goods receipts are confirmed the subsidiary will create post supplier invoice. In headquarters the billing team will create billing document and the subsidiary will automatically receive supplier invoice message.

### Prerequisites

The following list of prerequisites are to be in place to realize the business process

- Subsidiary’s should be running on SAP Cloud ERP system and Headquarters should run on SAP S/4HANA On Premise / SAP Cloud ERP (Private) or ECC
- Activate the Scope ID 2EJ and J44 at the Subsidiary’s SAP Cloud ERP system
- In case Headquarters is on:
- SAP S/4HANA On Premise / SAP Cloud ERP (Private) activate the scope ID BD9
- SAP ERP follow standard sell from stock process.
- The Headquarters and Subsidiary should have business partner and product master data aligned for this business process to work.’
- Headquarters will be represented as a Supplier in Subsidiary and Subsidiary will be represented as a Customer in Headquarters.

### Process Flow with Technical Details

<!-- image omitted: unnamed -->

The following integration points are depicted in the process flow diagram:

1. Purchase order at subsidiary will be automatically transformed to sales order at headquarters.
2. Once the order in conformed at headquarters, subsidiary will receive order confirmation message.
3. Post goods issue at headquarters, subsidiary will automatically create inbound delivery of goods.
4. Headquarters create billing documents correspondingly supplier invoice will be created at Subsidiary

## Technical Requirement

### Integration Requirements by using API

None

### Integration Requirements by using EDI/IDOC

**In SAP Cloud ERP:**

Use Communication System Scenario SAP_COM_0224 the details of setting up this scenario instruction will be found in set up instruction document for scope ID 2EJ from SAP Best Practices Explorer.

**In SAP S/4HANA On Premise or**/ **SAP Cloud ERP (Private):**

The On-Premise / / SAP Cloud ERP (Private) will use the following IDOCS

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

To be setup as per SAP Cloud ERP Best Practice scope id 2EJ for drop-shipment from HQ.

#### Tax Codes in SAP Cloud ERP (Subsidiary)

Tax codes between the HQ and subsidiary must be mapped for Supplier Invoice posting sat subsidiary from Billing document at HQ.

1. Log on to the SAP Fiori Launchpad in the SAP Cloud ERP system.

2. Navigate to Implementation Cockpit > Manage Your Solution > Configure Your Solution .

3. On the Configure Your Solution: Realize Phase screen, select the values as shown below:

- Application Area: Sourcing and Procurement
- Sub-application area: Integration

4. In the Configure Item area, choose the entry with above values and Name: Integration with Supplier

5. In the Configure Your Solution: Integration with Suppliers screen, choose the Configuration Steps tab.

A16. Search for Assign Tax Codes and select Configure.

7. Choose New Entries.

8. Enter the Headquarter’s ID as Invoicing Party, e.g. 10300089

9. Enter the type of tax (for example A1) under Tax Type.

10. Enter the country of the subsidiary under Country.

11. Under Tax Code enter the respective tax code of your SAP Cloud ERP system.

For example, V1.

12. Choose Save.

13. One-line item has to be created for each tax code mapping.

#### Company Code determination in SAP Cloud ERP (Subsidiary)

1. Log on to the SAP Fiori Launchpad in the SAP Cloud ERP system.

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

Enter Customer, eg. 10100001

Enter Supplier, eg. 10300089

Enter Sales Organization, eg. 1710

Enter Distribution Channel, eg. 10

Enter Division, eg. 00

Enter Sales Document Type, eg. OR

7. Select Step Name Convert External to Internal Partner Numbers Step Select Configure

Choose New Entries

Customer, eg. 10100001

Function Partner Function: SP

External Partner, eg. 10300089

Internal Partner, eg. 10100001

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

Note: In case, a TextID which is not maintained in Value Mapping table is received, Text node will not be created, and corresponding text will not be passed to the receiver system.

### Configuration for SAP S/4HANA On Premise

#### IDOC Configs at the On-Premise System (Headquarters)

Configure the Partner profiles and message control for incoming IDOCS for Sales Order creation and Change and outbound IDOCS for Order Confirmation, Advance Shipping Notification and Billing Document.

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

Condition master can be managed centrally at HQ or maintained manually with the buying price for the subsidiary and selling price for HQ being same.

#### Purchase Info Record

The condition group must set as ‘0001’ in the Purchasing info record against the HQ for the material. ‘0001’ corresponds to purchase orders requiring confirmations and advance shipping notifications. The receipt of advance shipping notification will automatically create the inbound delivery.

<!-- image omitted: unnamed -->

### Master Data for SAP S/4HANA On Premise

#### Material Master

The material number of subsidiary must be mapped with the material number of the headquarters using customer info record.

<!-- image omitted: unnamed -->

Material number at Subsidiary

Material number at HQ

#### Customer Master

The subsidiary must be maintained as a customer in HQ. The supplier number of the HQ at the subsidiary should be provided here. If the subsidiary has multiple company codes, then each company code must be maintained as customer in the subsidiary. The practice at subsidiary should be one unique purchasing org per company code.

<!-- image omitted: unnamed -->

HQ’s Supplier number at Subsidiary

Subsidiary’s plant must be created as a Ship-to-Party in HQ.

<!-- image omitted: unnamed -->

Subsidiary’s Plant should be modelled as Customer in HQ

<!-- image omitted: unnamed -->

Subsidiary Plant should be modelled as Customer in HQ

Partner functions assignment

#### Condition Master

Condition master can be managed centrally at HQ or maintained manually with the buying price for the subsidiary and selling price for HQ being same.

#### Ship-to-Party determination at Headquarters against Subsidiary’s Plant

In the EDSDC table (Transaction code VOE4), Ship-to-Party determination at Headquarters against Subsidiary’s Plant

Customer Number for Subsidiary at HQ

Plant Number at Subsidiary

Customer Number for Subsidiary at HQ

<!-- image omitted: unnamed -->

#### Sales org determination at Headquarters

In the EDSDC table (Transaction code VOE2), maintain the sales area determination for subsidiary’s sales orders at HQ.

<!-- image omitted: unnamed -->

Preferred Sales Area at HQ

Supplier Number for HQ at Subsidiary

Customer Number for Subsidiary at HQ

## Test Script

### Prerequisites

This section summarizes all prerequisites needed to conduct the test in terms of system, users, master data, organizational data, and other test data and business conditions.

### System Access at Subsidiary

The test should be conducted with the following system:

| System | Details |
| --- | --- |
| System | Accessible via the SAP Fiori launchpad. Your system administrator provides you with the URL to access the various apps assigned to your role. |

### Roles at Subsidiary

Assign the following business roles to your individual test users.

Note The following roles are provided as example roles from SAP. You can use these as templates for your own roles.

| Business Role | Business Role ID as Delivered by SAP | Log On |
| --- | --- | --- |
| Material Planner - External Procurement | SAP_BR_MATL_PLNR_EXT_PROC |  |
| Product Master Data Specialist | SAP_BR_PRODMASTER_SPECIALIST |  |
| Purchaser | SAP_BR_PURCHASER |  |
| Purchasing Manager | SAP_BR_PURCHASING_MANAGER |  |
| Accounts Payable Accountant | SAP_BR_AP_ACCOUNTANT |  |
| Receiving Specialist | SAP_BR_RECEIVING_SPECIALIST |  |

### Role at Headquarters

The following roles are provided as example roles from SAP. You can use these as templates for your own roles.

| Business Role |
| --- |
| Internal Sales Representative |
| Shipping Specialist |
| Warehouse Clerk |
| Billing Clerk |
| Credit Controller |
| Customer Master Specialist |

For more information about business roles, refer to Assigning business roles to a user in the Administration Guide for the Implementation of SAP S/4HANA

### Master Data, Organizational Data, and Other Data

The organizational structure and master data of your company has been created in your system during implementation. The organizational structure reflects the structure of your company. The master data represents materials, customers, and vendors, for example, depending on the operational focus of your company.

Use your own master data to go through the test procedure. If you have installed an SAP Best Practices Baseline Package, you can use the following Baseline Package scenario data:

Material

| Master data | Value | Master. data details | Comments |
| --- | --- | --- | --- |
| Material | TG0011 | Trading Good 0011,PD,Regular Proc. | Used for MRP procedure without scheduling agreement |

Org Data

| Master data | Value | Master. data details | Comments |
| --- | --- | --- | --- |
| Plant | 1010 | Plant 1 DE |  |
| Vendor | 10300001 | Domestic 10 Supplier 1 |  |
| Vendor | 10300002 | Domestic 10 Supplier 2 |  |
| Company Code | 1010 | Company Code 1010 |  |
| Purchasing Organization | 1010 | Purch. Org. 1010 |  |

For more information on creating these master data objects, see the following Master Data Scripts (MDS):

Table 1: Master Data Script Reference

| Master Data Script ID | Description |
| --- | --- |
| BNF | Create Product Master of Type "Trading Good" |

**Master Data maintained in Headquarters On Premise System**

| Data | Sample Value | Details | Comments |
| --- | --- | --- | --- |
| Material | TG10 or as per Headquarters nomenclature | Trad. Good 10, PD, Third PartyTrading Good for regular Trading (MRP planning) with item category group CBORno Serial no.; no batch. | Customer Info record of the material number in the Headquarters |
| Sold-to party | XXXXXXX | Customer no. subsidiary |  |
| Ship-to party | 10100001 | Domestic DE subsidiary | In Headquarters On Premise end customer to be maintained as Ship to Party and correspondingly Sold to party should be subsidiary |
| Payer | XXXXXXX |  |  |

### Preliminary Steps

In this section, you are provided a detailed step-by-step description of technical or other prerequisites.

The following steps are engaged if you choose option 1 - forecasting to manage planned independent requirements for material TG0011.

#### Create Scheduling Agreement

Purpose

This activity is used to create the scheduling agreement for the material/supplier combination, for example, material TG0011 and supplier 10300001, if it has not been maintained yet. If the scheduling agreement is already present in the system you can skip this step.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log onto the SAP Fiori launchpad, as Purchaser. | SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori app | Open Manage Scheduling Agreements tile. | The Manage Scheduling Agreements list page displays |  |
| 3 | Create Scheduling Agreement | Select Create Object (+) to create a new scheduling agreement | The New Scheduling Agreement header view displays. |  |
| 4 | Enter Header Data | Create a new scheduling agreement with the following data:Supplier: 10300001Agreement type: LPA (SA With Release doc.)Valid To: MM/DD/YYYYPurchasing Organization: 1010Purchasing Group: 001Target Value |  |  |
| 5 | Enter Header notes | Navigate to the Notes section, enter some of the Header Notes as below:Header textHeader notePricing typesDeadlinesTerms of deliveryShipping instructionsTerms of paymentWarrantiesPenalty for breach of contractGuaranteesContract riders (clauses)AssetOther contractual stipulationInbound DeliveryVendor memo (general)Vendor memo (pur. org.) |  |  |
| 6 | Add Items to Scheduling Agreement | From the New Scheduling Agreement view, choose the Items facets and select Add (+) | The New Scheduling Agreement Item view displays. |  |
| 7 | Enter Item data | On the Items facets view, make the following entries:Plant: 1010Target Quantity Material: 120 000Net Order Price: Defaulted from Info recordIn the Output Control area, make the following entry:Creation Profile: 0001Choose Apply at the bottom of the view. |  |  |
| 8 | Enter Item notes | Navigate to the Notes section and add the required Notes as below:Item textInfo record PO textMaterial PO textDelivery textInfo record noteES Master Agreements (MA)ES Requests f. Proposals (RFP)Sequence Number LPChoose Apply at the bottom of the view. |  |  |
| 9 | Save | Return to the New Scheduling Agreement header view and choose Save at the bottom of the view.Make a note of the schedule agreement number. | A schedule agreement is created. |  |

#### Maintain Consumption Values

Purpose

This activity maintains the consumption values for material TG0011.

If you do not change consumption values, the forecasting results could show without change.

Important note: Typically maintaining Consumption Data of Inventory for a material starts initially before you want to work with this material the first time.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori launchpad as a Product Master Data Specialist. | The SAP Fiori launchpad displays. |  |
| 2 | Access the Fiori App | Open Change Material. | The Change Material (Initial Screen) screen displays. |  |
| 3 | Select Material | Enter the material details and choose Enter.Material: TG0011Select the Forecasting view and choose Continue icon.Enter the plant details and choose Continue icon.Plant: 1010 | The Change Material TG0011 (Material general) screen displays. |  |
| 4 | Enter General data & Control data | In the Forecasting view, check the following data.Forecast model: DInitialization: X | The Initialization flag could be removed automatically if app Schedule Material Demand Forecast Runs is executed for material.If the Initialization flag is not set available, please re-mark it. |  |
| 5 | Choose Consumption values button | In the Forecasting view, choose Consumption vals to maintain historical consumption values for material TG0011. | The Consumption tab displays. |  |
| 6 | Enter Consumption values | For the past twelve periods, maintain the following data and choose Save.Total consumption: 20Corrected value: 20 | The notification ‘Material TG011 changed’ displays.The first time the Corrected values will be filled automatically.The total consumption could only be maintained at the first time, and corrected value could be always maintained. |  |

#### OPTIONAL - Adjust Historical Requirements – to prerequisites

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| Test Case ID | <X.XX> | Tester Name |  | Testing Date | Enter a test date. |
| Business Role(s) |  |  |  |  |  |
| Responsibility | <State Service Provider, Customer or Joint Service Provider and Customer> | Duration | Enter a duration. |  |  |

Context

This activity could adjust the historical requirements of material TG0011.

With the reorganization function, you can delete planned independent requirements for which there are no sales orders in the database.

The planned independent requirement quantities that have not been assigned before the specified reorganization key date (this date can also be in future) are set to zero and are flagged for reorganization. In this step, you can also set the system in that way that it deletes all inactive planned independent requirements.

There are two other jobs available which are not described in this test script.

Delete History and Ind. Requirements - Reorganization of schedule lines

The system checks which planned independent requirements were set to zero – either by reduction or consumption or by “requirement adjustment”. Schedule lines that have a quantity of zero before key date are deleted from database.

Delete old Requirement Records - Deleting history

Once the reorganization process is completed, the history can also be deleted by determining a key date. The key date for deleting histories can differ from the key date of reorganization.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori launchpad as a Material Planner - External Procurement. | The SAP Fiori launchpad displays. |  |
| 2 | Access the Fiori App | Open Schedule PIR Reorganizing Runs . | The Application Jobs screen displays. |  |
| 3 | Create new job | Choose New to create a new application job. | The New Job screen displays. |  |
| 4 | Enter job details | Enter the application job details.Job Template: Indep. Requirements Reorganizing - Adjusting RequirementsJob Name: Indep. Requirements Reorganizing - Adjusting RequirementsStart Immediately: X |  |  |
| 5 | Enter Parameters | In the Parameter Section area, make the following entries and choose Schedule.Plant: 1010Material: TG0011Version:00Key date: Enter Today's Date.Write history: XDelete Inactive Versions before Key Date: XResult List: XNo database changes (simulation): blank | The new job of reorganizing PIRs is created and scheduled.The Application job screen displays again, the new job displays in the Appliction Jobs table |  |
| 6 | Navigate to Job Results | Figure out the newly create job row and click the icon Navigate to the job results. | The Document (ID XXX) screen displays. |  |
| 7 | Check Job Results | In the Document (ID XXX) screen, check the requirement quantities during historical forecasting period have been adjusted to zero. |  |  |

## 7.7 Overview Table

The scope item Material Requirements Planning consists of several process steps provided in the following table.

| Process Step | Business Role | Transaction/App | Expected Results |
| --- | --- | --- | --- |
| Manage PIRs for Material TG0011 at subsidiary [page] 28 | Material Planner - External Procurement | Manage PIRs | Upon first run of the app, the Welcome! screen displays. |
| [Run Material Requirements Planning(MRP)](#unique_12) at subsidiary [page] 36Monitor Material Coverage Net/Individual segments | Material Planner - External Procurement | Monitor Material Coverage Net/Individual segments | The Monitor Material Coverage - Net and Individual Segments screen displays. MRP Run completed notification pop-out |
| [Evaluate MRP result (Purchase requisitions)](#unique_13)[at subsidiary](#unique_13)[page] 38 | Material Planner - External Procurement | Monitor Material Coverage Net/Individual segments | The Monitor Material Coverage - Net and Individual Segments screen displays. |
| [Display MRP Run Master Data Issues](#unique_15) at subsidiary [page] 39 | Material Planner - External Procurement | Display MRP Master Data Issues | The Display MRP Master Data Issues list displays |
| [Display MRP Run Key Figures](#unique_16)[at subsidiary](#unique_16) [page] 40 | Material Planner - External Procurement | Display MRP Key Figures. | The Display MRP Key Figures list displays. |
| [Convert Assigned Requisitions into Purchase Orders](#unique_17) at Subsidiary [page] 41 | Purchaser | Manage Purchase Requisitions | The Manage Purchase Requisitions screen displays. |
| [Approve Purchase Orders at Subsidiary (Optional)](#unique_18) [page] 43 | Purchasing Manager | Approve Purchase Orders |  |
| [Review Purchase Order Message](#unique_19)at Subsidiary [page] 44 | Purchaser | Manage Purchase Orders | Purchase Order Message created successfully |
| [Review Order Confirmation](#unique_20) at Subsidiary [page] 45 | Purchaser | Manage Purchase Orders | Order Confirmation received from Headquarters |
| [Create Delivery](#unique_16) at Headquarters [page] 46 | Shipping Specialist | Create Outbound Deliveries | The Create Outbound Deliveries screen displays. |
| [Create Attachment for Delivery at Headquarters (Optional)](#unique_17) [page] 47 | Shipping Specialist | Display Outbound Delivery | The Display Outbound Delivery: Initial Screen displays |
| [Execute Picking](#unique_18)at Headquarters [page] 47 | Shipping Specialist | My Outbound Delivery Monitor |  |
| [Check Batches at Headquarters (Optional)](#unique_19) [page] 47 | Shipping Specialist | Change Outbound Delivery | Batch numbers are checked |
| [Split Outbound Delivery at Headquarters (optional)](#unique_20) [page] 47 | Shipping Specialist | Split Outbound Delivery |  |
| [Add Freight Costs at Headquarters (Optional)](#unique_21) [page] 48 | Shipping Specialist | Change Outbound Delivery |  |
| [Post Goods Issue](#unique_22) at Headquarters [page] 48 | Shipping Specialist | My Outbound Delivery Monitor | The goods issue is posted. |
| [Review Shipping Notification](#unique_22) at Subsidiary [page] 48 | Purchaser | Manage Purchase Orders | Inbound Delivery created successfully |
| Confirm Quantities for Putaway at Subsidiary [page] 50 | Receiving Specialist | Inbound Deliveries for Putaway | The Inbound Deliveries for Putaway Screen appears. |
| Option A: Post Goods Receipt at Subsidiary [page] 51 | Receiving Specialist | Inbound Deliveries for Goods Receipt | The Inbound Deliveries for Goods Receipt Screen appears. |
| Option B: Schedule Job for Goods Receipt at Subsidiary [page] 52 | Receiving Specialist | Schedule Goods Receipt for Inbound Deliveries | A schedule goods issue for deliveries job is scheduled. |
| [Create Billing Document](#unique_24) at Headquarters [page] 53 | Billing Clerk | Create Billing Documents | The Create Billing Document screen displays. |
| [Create Attachment for Billing at Headquarters (Optional)](#unique_25) [page] 53 | Billing Clerk | Display Billing Document | The Display Billing Document screen displays. |
| Check [Vendor Invoice](#unique_29) at Subsidiary [page] 53 | Accounts Payable Accountant | Create Supplier Invoice(Advanced) |  |

### Test Procedure

In this procedure, 2 MRP procedures are covered. One MRP procedure is for material(TG0011) without scheduling agreement. Please follow the steps to test both sub-senarios independently.

#### Manage PIRs for Material TG0011 at Subsidiary

Purpose

Planned independent requirements of material could be managed either from forecasting results or directly creation. Please follow the steps to test only one option at a time.

Option 1: Execute forecasting for material TG0011

Option 2: Manage PIRs directly for material TG0011

##### Option 1 – Forecast at Subsidiary

The following steps execute forecasting for material TG0011.

In this activity, system could calculate and manage material demand forecast and PIRs based on consumption data of Inventory.

##### 7.8.1.1A Calculate Material Demand Forecast at Subsidiary

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| Test Case ID | <X.XX> | Tester Name |  | Testing Date | Enter a test date. |
| Business Role(s) |  |  |  |  |  |
| Responsibility | <State Service Provider, Customer or Joint Service Provider and Customer> | Duration | Enter a duration. |  |  |

Purpose

This activity executes forecasting for material TG0011.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori launchpad as a Material Planner - External Procurement. | The SAP Fiori launchpad displays. |  |
| 2 | Access the Fiori App | Open Schedule Material Demand Forecast Runs. | The Application Jobs screen displays. |  |
| 3 | Create new job | Choose New to create a new application job. | The New Job screen displays. |  |
| 4 | Enter job details | Enter the application job details.Job Template: Schedule Material Demand ForecastingJob Name: Enter a Job Name, for example, Schedule Material Demand ForecastingStart Immediately: X |  |  |
| 5 | Enter Parameters | In the Parameter section, make the following entries and choose Schedule.Plant: 1010Material: TG0011Period Indicator: MForecast execution: F | The new job of Schedule Material Demand Forecasting is created and scheduled.The Application Jobs screen displays again, and the new job displays in the Appliction Jobs table. |  |
| 6 | Navigate to Job Results | Figure out the newly create job row and click the icon Navigate to the job results. | The Document (ID XXX) screen displays. |  |
| 7 | Check Job Results | In the Document (ID XXX) screen, check details of Basic data, Control data, No. of values, Historical data and Forecast results section.Check the forecast values for the next twelve periods display in Forecast results section. | The expected original & corrected values column are expected to be the same constant with the consumption value, 20.If the forecast results display without change and Number of material forecasts carried out is zero, please confirm whether you execute preliminary steps Maintain Consumption Values and change consumption values from last forecasting executed and confirm the Initialization flag for material TG0011 is marked as X. |  |

##### 7.8.1.1B Check Material Coverage at Subsidiary

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| Test Case ID | <X.XX> | Tester Name |  | Testing Date | Enter a test date. |
| Business Role(s) |  |  |  |  |  |
| Responsibility | <State Service Provider, Customer or Joint Service Provider and Customer> | Duration | Enter a duration. |  |  |

Purpose

This activity checks initial status of material coverage.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori launchpad as a Material Planner - External Procurement. | The SAP Fiori launchpad displays. |  |
| 2 | Access the Fiori App | Open Check Material Coverage. | The Find Material screen displays. |  |
| 3 | Select Material | Enter following data and choose Enter.Material: TG0011Plant: 1010Storage Definition: MRP Standard | The Manage Material Coverage screen displays. |  |
| 4 | Check Stock/Requirements List | In the Stock/Requirements List, look for rows with IndReq VSF items and check status of current planned independent requirements. | If there is any IndReq VSF items during the historial forecasting period, you could refer preliminary steps to adjust historical requirements. |  |

##### 7.8.1.1C Transfer the resulting forecast to PIRs at Subsidiary

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| Test Case ID | <X.XX> | Tester Name |  | Testing Date | Enter a test date. |
| Business Role(s) |  |  |  |  |  |
| Responsibility | <State Service Provider, Customer or Joint Service Provider and Customer> | Duration | Enter a duration. |  |  |

Purpose

This activity copies total forecast jobs into PIRs for material TG0011.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori launchpad as a Material Planner - External Procurement. | The SAP Fiori launchpad displays. |  |
| 2 | Access the Fiori App | Open Schedule Copying Total Forecast Runs. | The Application Jobs screen displays. |  |
| 3 | Create new job | Choose New to create a new application job. | The New Job screen displays. |  |
| 4 | Enter job details | Enter the application job details.Job Template: Copy Total ForecastJob Name: Enter a Job Name, for example, Copy Total ForecastStart Immediately: X |  |  |
| 5 | Enter Parameters | In the Parameter Section area, make the following entries and choose Schedule.Plant: 1010Material: TG0011Version: 00Requirement Active: XWrite History: XNo database changes(simulation): blankResult List: XIncorrect Items Only: blankDisplay Detailed Lists: X | The new job of Schedule Material Demand Forecasting is created and scheduled.The Application job screen displays again, the new job displays in the Appliction Jobs table. |  |
| 6 | Navigate to Job Results | Figure out the newly create job row and click the icon Navigate to the job results. | The Document (ID XXX) screen displays. |  |
| 7 | Check Job Results | In the Document (ID XXX) screen, the detailed lists of Copy Total Forecast job displays.Check the planned quantity column, the values shall be consistent with the forecast results. |  |  |

##### 7.8.1.1D Check Material Coverage at Subsidiary

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| Test Case ID | <X.XX> | Tester Name |  | Testing Date | Enter a test date. |
| Business Role(s) |  |  |  |  |  |
| Responsibility | <State Service Provider, Customer or Joint Service Provider and Customer> | Duration | Enter a duration. |  |  |

Purpose

This activity checks material coverage after forecast results copied.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori launchpad as a Material Planner - External Procurement. | The SAP Fiori launchpad displays. |  |
| 2 | Access the Fiori App | Open Check Material Coverage. | The Find Material screen displays. |  |
| 3 | Select Material | Enter following data and choose Enter.Material: TG0011Plant: 1010Storage Definition: MRP Standard | The Manage Material Coverage screen displays. |  |
| 4 | Check Stock/Requirements List | In the Stock/Requirements List, look for rows with In-dReq VSF items.Confirm the quantity of planned independent require-ments is consistent with forecast results. | The PIRs for next twelve period are updated with the same quantity of forecast results, like 20. |  |

##### 7.8.1.1E Check Planned Independent Requirements at Subsidiary

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| Test Case ID | <X.XX> | Tester Name |  | Testing Date | Enter a test date. |
| Business Role(s) |  |  |  |  |  |
| Responsibility | <State Service Provider, Customer or Joint Service Provider and Customer> | Duration | Enter a duration. |  |  |

Purpose

This activity creates the planned independent requirements directly for material TG0011.

Please choose either option 1 or option 2.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori launchpad as a Material Planner - External Procurement. | The SAP Fiori launchpad displays. |  |
| 2 | Access the Fiori App | Open Manage PIRs. | Upon first run of the app, the Welcome! screen displays. |  |
| 3 | Skip Welcome! screen | Choose OK. |  |  |
| 4 | Choose your plant and MRP controller | Select the following data and choose Go.Material Planner/ MRP Controller: 001Plant: 1010Please first check default Area of Responsibility. On the Manage PIRs screen, click your user name, then choose Area of Responsibility. Check if the specific plant/controller is present in Area of Responsibility screen, if not, click + icon to make assignment.If the Plant field is not offered, choose Filters in the top right section of the screen (next to the Go button). A Filters dialog box displays. Choose More Filters (2). The Select Filters dialog box displays. Select Plant and choose OK. On the Filters dialog box, select the checkbox to the right of Plant and choose Go. | The MRP controller 001 in plant 1010 is assigned to your user. |  |
| 5 | Filter Material | In the Manage PIRs material list, filter by material and choose Go.Material: TG0011 | In the Manage PIRs materials list, the materialTG0011 displays. |  |
| 6 | Select Material | In the Manage PIRs materials list, select material TG0011 and choose the arrow (>) on the right side of the table. | The forecast demand for material TG0011 displays. |  |
| 7 | Check PIR status | For the next twelve periods, check Released PIRs displaying 20 PC. | The PIRs for next twelve peri-od display with the same quantity of forecast results, like 20. |  |

#### Option 2 - Manage PIRs Directly at Subsidiary

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| Test Case ID | <X.XX> | Tester Name |  | Testing Date | Enter a test date. |
| Business Role(s) |  |  |  |  |  |
| Responsibility | <State Service Provider, Customer or Joint Service Provider and Customer> | Duration | Enter a duration. |  |  |

Purpose

This activity creates the planned independent requirements directly for material TG0011.

Please choose either option 1 or option 2.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori launchpad as a Material Planner - External Procurement. | The SAP Fiori launchpad displays. |  |
| 2 | Access the Fiori App | Open Manage PIRs. | Upon first run of the app, the Welcome! screen displays. |  |
| 3 | Skip Welcome! screen | Choose OK. |  |  |
| 4 | Choose your plant and MRP controller | Select the following data and choose Go.Material Planner/ MRP Controller: 001Plant: 1010Please first check default Area of Responsibility. On the Manage PIRs screen, click your user name, then choose Area of Responsibility. Check if the specific plant/controller is present in Area of Responsibility screen, if not, click + icon to make assignment.If the Plant field is not offered, choose Filters in the top right section of the screen (next to the Go button). A Filters dialog box displays. Choose More Filters (2). The Select Filters dialog box displays. Select Plant and choose OK. On the Filters dialog box, select the checkbox to the right of Plant and choose Go. | The MRP controller 001 in plant 1010 is assigned to your user. |  |
| 5 | Filter Material | In the Manage PIRs material list, filter by material and choose Go.Material: TG0011 | In the Manage PIRs materials list, the material TG0011 displays. |  |
| 6 | Select Material | In the Manage PIRs materials list, select material TG0011 and choose the arrow (>) on the right side of the table. | The forecast demand for material TG0011 displays. |  |
| 7 | Check PIR status | For the next twelve periods, make the following entries:Draft PIRs: 200 | The draft forecast is entered. |  |
| 7 | Release Fore-cast | Choose Release PIRS. | The forecast of 200 PC for the next 12 periods is released.Check if the values are shown in the Released PIRs column. |  |

### Monitor Material Coverage at Subsidiary

#### Run Material Requirements Planning(MRP) at Subsidiary

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| Test Case ID | <X.XX> | Tester Name |  | Testing Date | Enter a test date. |
| Business Role(s) |  |  |  |  |  |
| Responsibility | <State Service Provider, Customer or Joint Service Provider and Customer> | Duration | Enter a duration. |  |  |

Context

The purpose of this activity is to start MRP run for both material with scheduling agreement and material without scheduling agreement.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori launchpad as the Material Planner – External Procurement. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Monitor Material Coverage Net/Individual segments. | The Monitor Material Coverage – Net and Individual Segments screen displays. |  |
| 3 | Select Material and Show Shortages | In the Materials tab, enter the following entries and choose Go.Material: TG0011Select 2 filtered rows and choose Manage Materials. | The Material Details screen displays. |  |
| 4 | Start MRP run for material without scheduling agreement | Choose Material TG0011 on left Materials screen.On the screen Material Details, choose Start MRP Run | The MRP run in progress notification pop-out first, then MRP Run completed notification pop-out. |  |

#### Evaluate MRP result at Subsidiary

##### Evaluate MRP result (Purchase requisitions) at Subsidiary

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| Test Case ID | <X.XX> | Tester Name |  | Testing Date | Enter a test date. |
| Business Role(s) |  |  |  |  |  |
| Responsibility | <State Service Provider, Customer or Joint Service Provider and Customer> | Duration | Enter a duration. |  |  |

Context

The purpose of this activity is to evaluate MRP results for material without scheduling agreement.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori launchpad as the Material Planner – External Procurement. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Monitor Material Coverage Net/Individual segments. | The Monitor Material Coverage – Net and Individual Segments screen displays. |  |
| 3 | Select Material and Show Shortages | In the Materials tab, enter the following entry and choose Go.Material: TG0011Select the filtered row and choose Manage Materials. | The Material Details screen displays. |  |
| 4 | Verify Purchase Requisitions that are available | In the Stock/Requirements List, purchase requisitions are shown as MRP results.Look for rows with PurRqs items to check more details. | The MRP has created purchase requisitions that can be used for the Procurement of Direct Materials test script.You could click PurRqs item, choose Open… button and click Purchase Requisition to display more details for PR. |  |
| 5 | Check planning details (optional) | In the Shortage Definition dropdown menu, choose MRP Standard, then select the Table View button. In the Available column, select an exception highlighted with a red statusShortage Definition: MRP StandardView Button: Table View | The Material Shortage screen displays.View buttons are located in the upper right of the Stock/Requirements List |  |
| 6 | Change style and version of the Material Detail List | On the Material Shortage screen, explore the display options (Table view/Chart view) by selecting an icon located in the upper right. | Go back twice to Monitor Material Coverage – Net and Individual Segments screen, navigate to row of material: TG0011, click against red/green charts in Stock Availability column.The Projected Stock screen displays the Availability per date. You can click Check Material Coverage button to go to the same Material Details list like in the previous step. |  |

### Display MRP Run Master Data Issues at Subsidiary

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| Test Case ID | <X.XX> | Tester Name |  | Testing Date | Enter a test date. |
| Business Role(s) |  |  |  |  |  |
| Responsibility | <State Service Provider, Customer or Joint Service Provider and Customer> | Duration | Enter a duration. |  |  |

Purpose

The purpose of this activity is to check MRP Run Master Data Issues.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori launchpad as a Material Planner - External Procurement. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Display MRP Master Data Issues. | The Display MRP Master Data Issues list displays. |  |
| 3 | Check the issues | Select the issue to display the details. | If there are any issues, choose the issue to display the details of the error. |  |

### Display MRP Run Key Figures at Subsidiary

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| Test Case ID | <X.XX> | Tester Name |  | Testing Date | Enter a test date. |
| Business Role(s) |  |  |  |  |  |
| Responsibility | <State Service Provider, Customer or Joint Service Provider and Customer> | Duration | Enter a duration. |  |  |

Purpose

The purpose of this activity is to check the key figures of the MRP run.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori launchpad as a Material Planner - External Procurement. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Display MRP Key Figures. | The MRP Key Figures list displays. |  |
| 3 | Select MRP run | Open the log with name Material Requirements Planning (MRP).Select the row with your user and the specific log name, i. e. Material Requirements Planning (MRP) job description. | The details of MRP run displays. |  |

### Convert Assigned Requisitions into Purchase Orders at Subsidiary

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

### Approve Purchase Orders (Optional) at Subsidiary

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

### Review Purchase Order Message at Subsidiary

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

### Review Order Confirmation at Subsidiary

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

### Create Delivery at Headquarters

Purpose

In this activity, you create the delivery

Procedure

Once the goods have been released for delivery the shipping specialist will create delivery against sale orders in the SAP system at headquarters.

### Create Attachment for Delivery at Headquarters (Optional)

Choose the suitable documents/files that will be attach to delivery from SAP System at Headquarters this is optional.

### Execute Picking at Headquarters

Purpose

The picking process involves taking goods from a storage location and staging the right quantity in a picking area where the goods are prepared for shipping.

Procedure

Execute picking of goods is done by warehouse management system. It is done via a transfer order, which is used for picking list and to withdraw the goods from the stock at Headquarters and dropped at the required shipping point.

### Check Batches at Headquarters (Optional)

Purpose

In this activity, you check the batch number assignment to the material.

Procedure

This is an optional step you can attach batch numbers to materials with a dedicated quantity, expiry date and other warranty information and the batch is then tracked throughout your shipping point that is from Headquarters all the way to the customer.

### Split Outbound Delivery at Headquarters (optional)

Purpose

In this process step, the user can split up single or multiple items from an existing, completely picked Outbound Delivery and move them to a new delivery document before posting Goods Issue.

Procedure

Once you have completely picked an outbound delivery order in Extended Warehouse Management (EWM). You find that you cannot load the complete quantity. That time you can create an outbound delivery for individual delivery items and therefore perform an outbound delivery split. You can select Items from the SAP system at Headquarters and split an outbound delivery order or an outbound delivery.

### Add Freight Costs at Headquarters (Optional)

Purpose

You might want to add the actual freight costs to the Outbound Delivery after picking where you know the exact weights and freight charges.

Procedure

The freight is part of an asset’s cost, it is to be considered an extension of the asset’s overall value. Enter the freight-in amount in the Unit price field. Dates on forms for the purchase and freight-in do not need to match. Average costs will be correctly adjusted as of the transaction date in SAP system for the freight-in charge.

### Post Goods Issue at Headquarters

Purpose

In this activity, you post the goods issue.

Procedure

The post goods issue is made once the delivery is created. When a post goods issue is made in SAP system at Headquarters, the ownership of the materials is transferred to the final customer. On post goods issue, stock gets reduced from the inventory. Similarly, stock figures also get updated in General Ledger. This increases the *Cost of Goods Sold* and reduces the inventory figure.

### Review Shipping Notification at Subsidiary

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

### Confirm Quantities for Putaway at Subsidiary

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| Test Case ID | <X.XX> | Tester Name |  | Testing Date | Enter a test date. |
| Business Role(s) |  |  |  |  |  |
| Responsibility | <State Service Provider, Customer or Joint Service Provider and Customer> | Duration | Enter a duration. |  |  |

Purpose

This activity confirms that all the materials have been put away in the correct quantities

Procedure

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Test Step # | Test Step Name | Instruction | Expected Result |  |
| 1 | Log onto SAP Fiori Launchpad | Log onto the SAP Fiori Launchpad using the Role Receiving Specialist. | The SAP Fiori Launchpad displays. |  |
| 2 | Access the App | Open Inbound Deliveries for Putaway. | The Inbound Deliveries for Putaway screen displays. |  |
| 3 | Enter inbound delivery number | Make the following entries then choose Execute:Delivery Date: Delete the default dateInbound Delivery: XXX | The selected Inbound Delivery displays. |  |
| 4 | Change the inbound delivery | Check the selected Inbound deliveries and click Change Inbound Deliveries. | The Inbound Delivery XXX Change: Overview screen displays. |  |
| 5 | Confirm Quantities for Putaway | In Item Overview tab, input the Putaway Qty: XXXNoteThe put away quantity should equal to the delivery QtyAnd choose Save. | Back to the Inbound Deliveries for Putaway screen and Inbound Delivery XXX has been saved message displays. |  |

### Option A: Post Goods Receipt at subsidiary

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| Test Case ID | <X.XX> | Tester Name |  | Testing Date | Enter a test date. |
| Business Role(s) |  |  |  |  |  |
| Responsibility | <State Service Provider, Customer or Joint Service Provider and Customer> | Duration | Enter a duration. |  |  |

Purpose

In this activity, you post goods receipt for inbound deliveries. You have two options to post goods receipt for inbound deliveries:

Option A: Post Goods Receipt

Option B: Scheduling Job for Goods Receipt for Inbound Deliveries

You can choose either option A or option B to execute the inbound delivery creation. For more information, see the next two tasks.

Procedure

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Test Step # | Test Step Name | Instruction | Expected Result |  |
| 1 | Log onto SAP Fiori Launchpad | Log onto the SAP Fiori Launchpad using the Role Receiving Specialist. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the App | Open Post Goods Receipt for Inbound Delivery. | The Goods Receipt screen displays. |  |
| 3 | Enter inbound delivery number | Make the following entries then choose Enter:Enter Inbound Delivery Number: XXX | The Goods Receipt screen displays.The selected Inbound Deliveries are shown. |  |
| 4 | Change the inbound delivery | Select item for this inbound delivery. Choose Post. | The Goods Receipt is posted.A success message is shown. |  |

### Option B: Schedule Job for Goods Receipt at Subsidiary

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| Test Case ID | <X.XX> | Tester Name |  | Testing Date | Enter a test date. |
| Business Role(s) |  |  |  |  |  |
| Responsibility | <State Service Provider, Customer or Joint Service Provider and Customer> | Duration | Enter a duration. |  |  |

Purpose

In this process step, you can schedule a background job for goods receipt posting regarding inbound deliveries.

This app can be used as an alternative instead of the manual goods receipt posting for inbound deliveries

Procedure

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Test Step # | Test Step Name | Instruction | Expected Result |  |
| 1. | Log on | Log onto the SAP Fiori Launchpad using Role Receiving Specialist. | The SAP Fiori Launchpad displays. |  |
| 2. | Access the App | Open Schedule Goods Receipt For Inbound Deliveries. | The Application Jobs screen is displayed. The app automatically shows the history of application jobs. |  |
| 3. | Create Goods Issue Deliveries Schedule | Choose New to define a new job. | The New Job screen displays. Job Template should default as Schedule Goods Receipt for Inbound Deliveries. |  |
| 4. | Job Parameters | Define scheduling options and parameters for the batch job if necessary, then choose Check.Start Immediately: SelectedInbound Delivery: **XXX** Enter the inbound delivery numberDelivery Date: Enter the delivery date in Inbound delivery | The system displays the message You can go ahead and schedule the job |  |
| 5. | Schedule | Choose Schedule. | A schedule goods issue for deliveries job is scheduled. Screen back to Application Jobs. |  |
| 6. | Check Goods Issue Deliveries Job Log | In screen Application Jobs, after job item’s status turned to Finished, choose Status symbol in column Log.NoteClick Magnifier, the job list will refresh. | Screen goes to the job log on details |  |

### Create Billing Document at Headquarters

This billing document number is created at the end of this post goods issue process at Headquarters. Once the goods have been delivered to the customers the headquarter must bill it to the subsidiary. As soon as the headquarters create the billing documents the invoice will be automatically generated to subsidiary.

### Create Attachment for Billing at Headquarters (Optional)

In standard SAP system, you can see help documents stating that proof of delivery can be used for confirming material delivery to the customer and its quantity. This is done by creating attachment for billing at Headquarters by entering the respective invoice number generated in the previous step.

### Check Vendor Invoice at Subsidiary

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

## Appendix

### Process Chains

The process to be tested in this test case is part of a chain of integrated processes.

#### Preceding Processes

Complete the following business processes and conditions before you start with the test steps:

| Process | Business Condition |
| --- | --- |
| Master Data Maintenance |  |

#### Succeeding Processes

After completing the activities in this test case, you can continue testing the following business processes:

| Process | Business Condition |
| --- | --- |
| Procurement of Direct Materials | A purchase requisition is created as part of the Material Requirements Planning test script. This purchase requisition is converted into a purchase order in the Procurement of Direct Materials process. |

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
| © 2019 SAP SE or an SAP affiliate company. All rights reserved.No part of this publication may be reproduced or transmitted in any form or for any purpose without the express permission of SAP SE or an SAP affiliate company.SAP and other SAP products and services mentioned herein as well as their respective logos are trademarks or registered trademarks of SAP SE (or an SAP affiliate company) in Germany and other countries. Please see [http://global.sap.com/corporate-en/legal/copyright/index.epx#trademark](http://global.sap.com/corporate-en/legal/copyright/index.epx#trademark) for additional trademark information and notices.Some software products marketed by SAP SE and its distributors contain proprietary software components of other software vendors.National product specifications may vary.These materials are provided by SAP SE or an SAP affiliate company for informational purposes only, without representation or warranty of any kind, and SAP SE or its affiliated companies shall not be liable for errors or omissions with respect to the materials. The only warranties for SAP SE or SAP affiliate company products and services are those that are set forth in the express warranty statements accompanying such products and services, if any. Nothing herein should be construed as constituting an additional warranty. In particular, SAP SE or its affiliated companies have no obligation to pursue any course of business outlined in this document or any related presentation, or to develop or release any functionality mentioned therein. This document, or any related presentation, and SAP SE’s or its affiliated companies’ strategy and possible future developments, products, and/or platform directions and functionality are all subject to change and may be changed by SAP SE or its affiliated companies at any time for any reason without notice. The information in this document is not a commitment, promise, or legal obligation to deliver any material, code, or functionality. All forward-looking statements are subject to various risks and uncertainties that could cause actual results to differ materially from expectations. Readers are cautioned not to place undue reliance on these forward-looking statements, which speak only as of their dates, and they should not be relied upon in making purchasing decisions. |

<!-- image omitted: unnamed -->

## Suspected conflicts

> [!warning] Conflict
> Flagged while digesting this document, not verified: IDoc names inconsistent within document: DELVRY07/INVOIC2 in technical requirements vs DESADV/INVOIC02 in HQ configuration

> [!warning] Conflict
> Flagged while digesting this document, not verified: Document is dated revision 2 (2021) and copyright 2019/2025 but labelled June 2026; may be stale

> [!warning] Conflict
> Flagged while digesting this document, not verified: Test script section partly reuses Materials Requirements Planning content (e.g. 'TG011' typo, 'Goods Issue' wording for goods receipt job)

## Connections
- part-of :: [[_cluster]]
- related-to :: [[16-two-tier-erp-and-central-finance/two-tier-erp-billing-document-to-supplier-invoice-integration-using-cl]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/General/Two-Tier_ERP_Assets_User_Guides/Two-Tier_ERP_Assets_User_Guides/Procurement/S4CLD2608_2T_Replenishment_Guide.docx` — full document · extracted with `mammoth` · 78,767 chars in the whole document
