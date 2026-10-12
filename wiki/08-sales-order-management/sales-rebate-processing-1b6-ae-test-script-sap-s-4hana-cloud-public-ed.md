---
id: 08-sales-order-management/sales-rebate-processing-1b6-ae-test-script-sap-s-4hana-cloud-public-ed
title: "Sales Rebate Processing (1B6_AE) - Test Script, SAP S/4HANA Cloud Public Edition (1B6_S4CLD2608_BPD_EN_AE)"
description: "SAP test script for scope item 1B6 (UAE) Sales Rebate Processing: condition contracts, process variants, settlement runs, workflow, fixed amounts, reversals; release 2608."
cluster: 08-sales-order-management
tags: [kb/sales-order-management, topic/condition-contract-settlement]
aliases: [1B6_S4CLD2608_BPD_EN_AE]
keywords: ["Rebates, Commissions and Royalties Settlement", sales rebate processing, condition contracts, condition contract process variants, rebate settlement, delta accruals settlement, two-step settlement, approval workflow, fixed amount agreements, multiple company codes]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/1B6_S4CLD2608_BPD_EN_AE.docx]
confidence: high
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-709
topic: 08-sales-order-management/condition-contract-settlement
language: EN
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Sales Rebate Processing (1B6_AE) - Test Script, SAP S/4HANA Cloud Public Edition (1B6_S4CLD2608_BPD_EN_AE)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/1B6_S4CLD2608_BPD_EN_AE.docx`, extracted with `mammoth`. Grouped under **Rebates, Commissions and Royalties Settlement** in Sales Order Management. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

|  |  |
| --- | --- |
| Sales Rebate Processing (1B6_AE)Purpose PUBLIC 1<!-- image omitted: unnamed --> | Test ScriptSAP S/4HANA Cloud Public Edition - 19-06-26 |
|  | Sales Rebate Processing (1B6_AE) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Table of Contents

[1 Purpose 4](#_Toc232846551)

[2 Prerequisites 5](#_Toc232846552)

[2.1 System Access 5](#_Toc232846553)

[2.2 Roles 5](#_Toc232846554)

[2.3 Master Data, Organizational Data, and Other Data 6](#_Toc232846555)

[2.4 Preliminary Steps 9](#_Toc232846556)

[2.4.1 Posting of Accruals with Transactional Documents (Optional) 9](#_Toc232846557)

[2.4.2 Prepare Transactional Data (Optional) 11](#_Toc232846558)

[2.4.3 Activate Condition Contract Types (Optional) 12](#_Toc232846559)

[2.4.4 Define Condition Contract Process Variants (Optional) 14](#_Toc232846560)

[2.4.4.1 Define Process Variant for Using the Workflow 14](#_Toc232846561)

[2.4.4.2 Define Process Variant for Tax Free Goods 17](#_Toc232846562)

[2.4.4.3 Define Process Variant for Split Criteria Usage in Settlement 19](#_Toc232846563)

[2.4.4.4 Define Process Variant for Business Volume Selection Criteria Usage 22](#_Toc232846564)

[2.4.4.5 Define Process Variant to Configure Material Groups as Condition Level 24](#_Toc232846565)

[2.4.4.6 Define Process Variant to Configure Settings for Fixed Amount Agreements 27](#_Toc232846566)

[2.4.4.7 Define Process Variant for Contract Determination 30](#_Toc232846567)

[2.4.4.8 Define Process Variant for Rebates on Paid Invoices 32](#_Toc232846568)

[2.4.4.9 Define Process Variant for Different Bases for Rebate Calculation and Scale Determination 35](#_Toc232846569)

[2.4.4.10 Define Process Variant to Activate Condition Table for Product Hierarchy 38](#_Toc232846570)

[2.4.4.11 Define Process Variant to Activate Business Volume Selection by Service Rendered Date 41](#_Toc232846571)

[2.4.4.12 Maintain Automatic Account Determination 44](#_Toc232846572)

[2.4.5 Configure Approval Workflow (Optional) 47](#_Toc232846573)

[2.4.5.1 Manage Teams and Responsibilities 47](#_Toc232846574)

[2.4.5.2 Manage Workflow for Condition Contracts - Release Contract 49](#_Toc232846575)

[2.4.5.3 Manage Workflow for Condition Contracts - Release Settlement 50](#_Toc232846576)

[2.4.5.4 Manage Workflow for Settlement Documents 52](#_Toc232846577)

[3 Overview Table 54](#_Toc232846578)

[4 Test Procedures 58](#_Toc232846579)

[4.1 Sales Rebate Processing – One Customer 59](#_Toc232846580)

[4.1.1 Create Condition Contract 59](#_Toc232846581)

[4.1.2 Check Business Volume (Optional) 63](#_Toc232846582)

[4.1.3 Delta Accruals Settlement (Optional) 65](#_Toc232846583)

[4.1.4 Check Settlement Document for Delta Accruals Settlement (Optional) 66](#_Toc232846584)

[4.1.5 Partial Settlement (Optional) 67](#_Toc232846585)

[4.1.6 Check Settlement Document for Partial Settlement (Optional) 68](#_Toc232846586)

[4.1.7 Final Settlement 71](#_Toc232846587)

[4.1.8 Check Settlement Document for Final Settlement (Optional) 72](#_Toc232846588)

[4.2 Sales Rebate Processing – Multiple Customers 72](#_Toc232846589)

[4.2.1 Create Condition Contract 73](#_Toc232846590)

[4.2.2 Check Business Volume (Optional) 76](#_Toc232846591)

[4.2.3 Delta Accruals Settlement (Optional) 76](#_Toc232846592)

[4.2.4 Partial Settlement (Optional) 77](#_Toc232846593)

[4.2.5 Final Settlement 77](#_Toc232846594)

[4.3 Sales Rebate Processing – Two-Step Settlement 77](#_Toc232846595)

[4.3.1 Create Condition Contract 77](#_Toc232846596)

[4.3.2 Check Business Volume (Optional) 81](#_Toc232846597)

[4.3.3 Delta Accruals Settlement (Optional) 81](#_Toc232846598)

[4.3.4 Partial Settlement (Optional) 82](#_Toc232846599)

[4.3.5 Collect Parked Settlement Documents from Partial Settlement (Optional) 82](#_Toc232846600)

[4.3.6 Final Settlement 83](#_Toc232846601)

[4.3.7 Collect Parked Settlement Documents from Final Settlement 83](#_Toc232846602)

[4.4 Goods Related Sales Rebate Processing 84](#_Toc232846603)

[4.5 Sales Rebate Processing – Multiple Company Codes 84](#_Toc232846604)

[4.5.1 Create Condition Contracts 85](#_Toc232846605)

[4.5.2 Check Business Volume 85](#_Toc232846606)

[4.5.3 Create Settlement Documents 86](#_Toc232846607)

[4.5.4 Check Settlement Documents 86](#_Toc232846608)

[4.5.5 Collect Parked Settlement Documents 86](#_Toc232846609)

[4.5.6 Check Collective Settlement Documents 86](#_Toc232846610)

[4.6 Sales Rebate Processing with Approval Workflow 87](#_Toc232846611)

[4.6.1 Create Condition Contract 87](#_Toc232846612)

[4.6.2 Request Approval to Release Condition Contract 91](#_Toc232846613)

[4.6.3 Trigger Rework of Condition Contract (Optional) 92](#_Toc232846614)

[4.6.4 Rework Condition Contract (Optional) 93](#_Toc232846615)

[4.6.5 Release Condition Contract 94](#_Toc232846616)

[4.6.6 Delta Accruals Settlement (Optional) 95](#_Toc232846617)

[4.6.7 Request Release of Condition Contract for Settlement 95](#_Toc232846618)

[4.6.8 Release Condition Contract for Settlement 96](#_Toc232846619)

[4.6.9 Partial Settlement (Optional) 97](#_Toc232846620)

[4.6.10 Approve Release of Partial Settlement Document to Accounting (Optional) 97](#_Toc232846621)

[4.6.11 Final Settlement 98](#_Toc232846622)

[4.6.12 Approve Release of Final Settlement Document to Accounting 98](#_Toc232846623)

[4.7 Sales Rebate Processing with Different Bases for Rebate Calculation and Scale Determination 98](#_Toc232846624)

[4.7.1 Create Condition Contract 99](#_Toc232846625)

[4.8 Sales Rebate Processing with Graduated Scales 100](#_Toc232846626)

[4.9 Sales Rebate Processing with Conditions Maintained for Product Hierarchy Nodes 101](#_Toc232846627)

[4.10 Sales Rebate Processing Using Service Rendered Date for Business Volume Selection 102](#_Toc232846628)

[4.11 Final Settlement with Adjustments (Optional) 103](#_Toc232846629)

[4.12 Rebate Unlikelihood (Optional) 105](#_Toc232846630)

[4.13 Sales Rebate Processing – Fixed Amount Agreements 106](#_Toc232846631)

[4.13.1 Basic Processing 106](#_Toc232846632)

[4.13.2 Cost Recognition for Fiscal Periods 109](#_Toc232846633)

[4.13.3 Fixed Amount Settlement Proportionally Across Fiscal Periods 110](#_Toc232846634)

[4.13.4 Fixed Amount Distribution to Business Objects 111](#_Toc232846635)

[4.13.5 Fixed Amount Settlement on Multiple Products 112](#_Toc232846636)

[4.14 Reverse Settlement Document (Optional) 112](#_Toc232846637)

[5 Follow-Up Processes 114](#_Toc232846638)

[5.1 Analytical Content: Order-to-Cash (Optional) 114](#_Toc232846639)

[5.2 General Ledger Reporting and CO-PA Reporting (Optional) 114](#_Toc232846640)

[6 Appendix 115](#_Toc232846641)

[6.1 Time-Dependent Tax 115](#_Toc232846642)

## Purpose

Overview

This scope item covers the subsequent settlement of rebate conditions agreed upon with customers. You use condition contracts to enter the rebate conditions, together with the process control parameters, business volume selection criteria, and settlement dates for partial and final settlement. You can create condition contracts for one customer or multiple customers.

Customer invoices are used to determine the business volume. In the case of multiple customers, the individual revenue of each customer assigned is used to calculate the settlement values. To pay out rebates to customers, you create settlement documents.

Settlement documents are usually immediately released to accounting. You can also create a condition contract for a two-step settlement procedure to collect and post settlement documents of different condition contracts in one journal entry to accounting.

Furthermore, you can choose how the system determines the taxation for the settlement items.

This document provides a detailed procedure for testing this scope item after solution activation, reflecting the predefined scope of the solution. Each process step, report, or item is covered in its own section, providing the system interactions (test steps) in a table view. Steps that are not in scope of the process but are needed for testing are marked accordingly. Project-specific steps must be added.

|  |
| --- |
| Note Values in this test script (decimal notation, date formats, and so on) are presented in U.S. standard notation. If your test system is set up to use a different notation, enter values as appropriate. |

## Prerequisites

This section summarizes all the prerequisites for conducting the test in terms of systems, users, master data, organizational data, other test data and business conditions.

|  |
| --- |
| Caution Testing in a 3-System LandscapeIn a 3-system landscape (with SAP Central Business Configuration as your configuration environment), changes to software and business configuration are applied to your systems independently of one another. It is therefore your responsibility to manage the active business configuration in your systems and synchronize configuration data in your SAP S/4HANA Cloud Public Edition system landscape. A synchronization is required, for example, after you've enhanced the scope, extended configuration, or adopted new or changed content from content updates or upgrades. For more information, refer to the [product assistance](https://help.sap.com/docs/SAP_S4HANA_CLOUD/b249d650b15e4b3d9fc2077ee921abd0/6c398c4ae7364af69d3edffe7fdc39f2.html) in the SAP Help Portal.Before testing, if you want to use all software features described for the process steps, reports, or items in this document, we recommend the Business Process Configuration Expert in your organization has upgraded the configuration content and deployed the configuration data to your system landscape.If the decision is not to upgrade the configuration content in your test or production system, you can run regression tests of software changes using the procedures in the previous test script version (see the following [link](https://support.sap.com/content/dam/SAAP/Sol_Pack/S4C/Library/TestScripts/1B6_S4CLD2602_BPD_EN_AE.docx) ). |

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
| Sales Manager | SAP_BR_SALES_MANAGER | Sales Management / Internal Sales / Billing for Sales Manager / Customer Returns for Sales Manager | SAP_BR_SALES_MANAGER / SAP_SD_SPT_INT_SALES_SALES_MGR_PC / SAP_SD_SPT_BILLING_SALES_MGR_PC / SAP_SD_SPT_RETURNS_SALES_MGR_PC |  |
| Internal Sales Representative | SAP_BR_INTERNAL_SALES_REP | Internal Sales / Customer Returns / Billing | SAP_BR_INTERNAL_SALES_REP / SAP_SD_SPT_RETURNS_INT_SALES_PC / SAP_SD_SPT_BILLING_INT_SALES_PC |  |
| Shipping Specialist | SAP_BR_SHIPPING_SPECIALIST | Shipping | SAP_BR_SHIPPING_SPECIALIST |  |
| Returns and Refund Clerk | SAP_BR_WAREHOUSE_CLERK | Customer Returns | SAP_BR_RETURNS_REFUND_CLERK |  |
| Billing Clerk | SAP_BR_BILLING_CLERK | Billing | SAP_BR_BILLING_CLERK |  |
| Business Process Specialist | SAP_BR_BUSINESS_PROCESS_SPEC | Business Process Management / Business Process Management | SAP_BR_BUSINESS_PROCESS_SPEC / SAP_CA_SPT_BPS_PC |  |
| Credit Controller | SAP_BR_CREDIT_CONTROLLER | Credit Management | SAP_BR_CREDIT_CONTROLLER |  |
| Configuration Expert - Business Process Configuration | SAP_BR_BPC_EXPERT | Business Process Configuration / Business Process Configuration - Finance / Business Process Configuration - Procurement / Manage your Solution / Business Process Configuration - Workflow / Business Configuration - Feature Management / Business Process Configuration - Extensibility Explorer / Business Configuration - Transportation | SAP_BR_BPC_EXPERT / SAP_FIN_SPT_BPC_EXPERT_PC / SAP_MM_SPT_BIZ_PROC_CONFIGN_PC / SAP_CA_SPT_IC_LND_BASE_PC / SAP_CA_SPT_BPC_WORKFLOW_PC / SAP_CA_SPT_BPC_FM_PC / SAP_EI_SPT_BPC_EXT_PC / SAP_TM_SPT_TRANSPCFG_PC |  |

### Master Data, Organizational Data, and Other Data

SAP Best Practices Standard Values based on new global template will be used once available. In the table you still see the master data used for the current baseline.

Essential master and organizational data was created in your SAP S/4HANA system in the implementation phase, such as the data that reflects the organizational structure of your company and master data that suits its operational focus, for example, master data for materials, vendors, and customers.

This master data usually consists of standardized SAP Best Practices default values, and enables you to go through the process steps of this scope item.

|  |
| --- |
| Caution Update Behavior of Predelivered Demo DataIn non-productive environments (such as starter systems, sandbox systems, or partner demo systems), SAP initially deploys demo data for your selected scope. You can use this data to test and evaluate business processes.In a customer system, you can receive new or updated demo data after initial activation with further scope enhancements, provided the existing demo data wasn't changed in an incompatible way. If activation errors occur due to incompatible changes in demo data, you're responsible for resolving them. If you don't resolve the errors within a specific time frame, SAP reserves the right to deactivate demo data in your systems. In this case, you can continue by creating your own demo data. Alternatively, you can request that your systems be reprovisioned if you want to work with predelivered demo data again.In partner systems, you can use the demo data deployed with the initial activation. No additional demo data will be deployed in the system with scope enhancements. You can only create additional demo data manually. |

|  |
| --- |
| Note Additional Master Data (Default Values)You can test the scope item with other SAP Best Practices default values that have the same characteristics. |

Check your SAP system to find out which other material master data exists.

|  |
| --- |
| Note Using Your Own Master DataYou can also use customized values for any material or organizational data for which you have created master data. For more information about creating master data, see the Master Data Procedures documentation. |

The organizational structure and master data of your company has been created in your system during activation. The organizational structure reflects the structure of your company. The master data represents materials, customers, and vendors, for example, depending on the operational focus of your company.

Use your own master data or the following sample data to go through the test procedure.

| Data | Sample Value | Details | Comments |
| --- | --- | --- | --- |
| Material | TG11 | Trading Good for Reg. Trading (MRP planning)No batch. |  |
| Material | TG12 | Trad.Good 12,Reorder Point,Reg.Trad.No batch. |  |
| Material | TG21 | Trad.Good 21,Reorder Point,Batch-FIFONo serial number, batch-controlled (FIFO strategy). |  |
| Material | TG22 | Trad.Good 22,Reorder Point,Batch-ExpDNo serial number, batch- controlled (Exp. Date). |  |
| Material | TG0015 | Trading Good 0015,PD,Regular Proc.Tax classification for reduced output tax. |  |
| Material | CM-FL-V00 | Forklift | Only use if you have activated the scope item Make-to-Order Production with Variant Configuration (1YT). |
| Sold-to Party | 3310000333100008 | Domestic UAE Customer 3Domestic UAE Customer 8 | You can test the scope item using another domestic customer.33100005 is for credit management.33100008 is for material listing/exclusion. 33100009 is for customer material record and POD (Proof-of-Delivery). |
| Ship-to party | 3310000333100008 | Domestic UAE Customer 3Domestic UAE Customer 8 |  |
| Payer | 3310000333100008 | Customer domestic 03Domestic UAE Customer 8 |  |
| Plant | 3310 |  |  |
| Storage Location | 331A |  |  |
| Shipping Point | 3310 |  |  |
| Sales organization | 3310 |  |  |
| Distribution channel | 10 |  |  |
| Division | 00 |  |  |

For more information on creating master data objects, see the following [Master Data Scripts (MDS)](https://help.sap.com/docs/s4hana-best-practices/s4cld2608-master-data)

Table 1: Master Data Script Reference

| MDS | Description |
| --- | --- |
| BNF | Create Product Master of type "Trading Good" - MDS |
| BND | Create Customer Master - MDS |

If you want to test the Sales Rebate Processing – Multiple Company Codes process variant, you must prepare business partners accordingly. Extend existing business partners in a way that you maintain the Customer View for the desired sales areas or create new business partners with required master data. Check test scripts for other countries for relevant logistics data (plant, storage location, shipping point, and sales area). When you use own materials, make sure that all views for involved organizational levels are maintained.

### Preliminary Steps

#### Posting of Accruals with Transactional Documents (Optional)

Purpose

Accruals can be created when you post transactional documents ‒ billing documents released to accounting in this scope item ‒ or you can post accruals in an accumulated form with a specific settlement run called Delta Accruals Settlement as described in the test procedures. You can also combine the procedures, for instance, to determine a more accurate accruals amount in a weekly delta accruals run by considering all transactional documents.

To post accruals with released billing documents, you must include the accruals condition type in the pricing procedure of the sales order in an appropriate manner. As usual, this pricing element will be copied to the billing document. Below we describe the best practice approach that you include the condition type at the bottom of the pricing procedure. Note that you can similarly post accruals for other scope items (sales commissions, royalties) in parallel when you include the corresponding accruals condition types in the same way.

Posting accruals with transactional documents requires that you create the condition contract with the accruals condition before you create rebate relevant sales orders, so that the accruals condition is found during pricing of a sales order item. Relevant condition contracts are determined by matching sales order and condition contract data. If the system finds more than one relevant condition contract, you will accordingly get several lines for the accruals condition types in the pricing elements. When you create a condition contract with a validity period starting in the past, you can schedule a delta accruals settlement to post accruals for already created billing documents. Then you continue to post accruals with the transactional documents. When you want to create a new condition contract without specifying a customer as the business volume selection criterion, usually the case in the multiple customer business process variant, define a condition contract process variant as described in chapter Define Process Variant for Contract Determination and enter it for the condition contract.

Procedure

Depending on your configuration environment for SAP S/4HANA Cloud Public Edition, choose one of the following options:

Configure Your Solution:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Your Solution (F1241).Note If required, choose Set Local Version to set the desired local version. | The Manage Your Solution screen displays. |  |
| 3 | Open Configure Your Solution | Choose Configure Your Solution. | The Configure Your Solution: Realize Phase screen displays. |  |
| 4 | Open Configuration Item for Pricing | Enter the following filters:Application Area: SalesSub Application Area: Price ManagementIn the items table, select the item with item name: Pricing. | The Configure Your Solution - Pricing screen displays. |  |
| 5 | Go to Pricing Procedures Overview | Choose Configure on the right to Set Pricing Procedures configuration step. | The Set Pricing Procedures: Change screen displays. |  |
| 6 | Go to Control Data | Select the relevant pricing procedure and choose Procedures – Control Data in Dialog Structure. | The control data for the pricing procedure with the Reference Step Overview table is displayed in the working area. |  |
| 7 | Add Accruals Condition Type | Choose New Entries and make the following entries:Step Number: <number higher than maximum hitherto>Condition Type: REA1Alt. Cndn Base Value: 213Accruals: 0S1Choose Save. | Accruals condition type has been added to pricing procedure. |  |

SAP Central Business Configuration:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the project experience in SAP Central Business Configuration. | The SAP Fiori launchpad displays. |  |
| 2 | Go to Pricing Procedures Overview | In the Product-Specific Configuration phase, navigate to the Configuration Activities tab. To locate the activity in the tree view, search for the following activity: Set Pricing Procedures.Choose Open Documentation for the found line item to see more details about this configuration activity.Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. | The Set Pricing Procedures: Change screen displays. |  |
| 3 | Go to Control Data | Select the relevant pricing procedure and choose Procedures – Control Data in Dialog Structure. | The control data for the pricing procedure with the Reference Step Overview table is displayed in the working area. |  |
| 4 | Add Accruals Condition Type | Choose New Entries and make the following entries:Step Number: <number higher than maximum hitherto>Condition Type: REA1Alt. Cndn Base Value: 213Accruals: 0S1Choose Save. | Accruals condition type has been added to pricing procedure. |  |

Routine 213 for the alternative calculation of condition base value has the following function: When you enter a condition contract, you can set the amount fields group on the Settlement Data tab page. This parameter controls for which amount field from the business volume data the system transfers data to the pricing procedure of the settlement document. As default, the net amount is used, but you can also specify a subtotal of the pricing procedure. As mentioned, during pricing the system determines the relevant condition contracts for the accruals condition types, and formula 213 reads the corresponding amounts field group and sets the condition base value accordingly. Therefore, there is no need to specify the From Step in the line with accruals condition type.

#### Prepare Transactional Data (Optional)

Purpose

The business volume for sales rebate settlement is determined from billing documents for most cases. To prepare transactional test data, you can follow the Sell from Stock (BD9) scope item, which describes the sales process from a standard sales order to a billing document.

For sales rebate settlement based on paid billing documents, the business volume is determined from paid billing documents, which means the related accounting documents need to be cleared. To prepare transactional test data, you can follow the steps described in the scope items Sell from Stock (BD9) and Accounts Receivable (J59).

Preparing transactional data is a required step. You can perform this step before or after creating the condition contract, or after each settlement run.

Procedure

Perform necessary preliminary steps, as for instance an initial stock set up for materials, and test activities for sales order, delivery, and billing document creation as described in the Sell from Stock (BD9) scope item's test script using the master data from this document.

Case 1: One Customer as Condition Contract Partner

For the sales rebate processing using one customer as condition contract partner, select a customer from the [Master Data, Organizational Data, and Other Data](#unique_5) [page ] 6 chapter and execute Sell from Stock (BD9) scope item for this customer. Then follow the [Create Condition Contract](#unique_8) [page ] 59 section to create a condition contract for the selected customer.

Case 2: Multiple Customers as Condition Contract Partner

For the sales rebate processing using multiple customers as settlement recipients, select at least two different customers from the [Master Data, Organizational Data, and Other Data](#unique_5) [page ] 6 chapter and execute Sell from Stock (BD9) scope item for each of the customers. Then follow the [Create Condition Contract](#unique_9) [page ] 73 section to create a condition contract with the selected customers as business volume selection criteria.

#### Activate Condition Contract Types (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you activate the condition contract types for multiple company codes process variant and for fixed amount agreements.

|  |
| --- |
| Note Representing a new business scenario, the condition contract types for fixed amount agreements and for multiple company codes process variant are blocked in the delivered business content in accordance with the guideline that UI changes should be avoided after a release upgrade. Without block these condition contract types would appear on the pop-up window for condition contract selection when you create a new condition contract. |

|  |
| --- |
| Note You must also create a condition contract process variant for the profit center determination for fixed amount agreements. For more information, see chapter [Define Process Variant to Configure Settings for Fixed Amount Agreements](#unique_11) [page ] 27. |

Procedure

Depending on your configuration environment for SAP S/4HANA Cloud Public Edition, choose one of the following options:

Configure Your Solution:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. |  |  |
| 2 | Access the App | Open Manage Your Solution (F1241).Note To create country-/region-dependent settings for the intended local version, choose Set Local Version. | The Manage Your Solution screen displays. |  |
| 3 | Open Configure Your Solution | Choose Configure Your Solution. | The Configure Your Solution: Realize Phase screen displays. |  |
| 4 | Open Configuration Item for Sales Rebate Settlement | Enter the following filters:Application Area: SalesSub Application Area: Sales Rebate ManagementIn the items table, select the item with item name: Sales Rebate Settlement. | The Configure Your Solution - Sales Rebate Settlement screen displays. |  |
| 5 | Go to Configuration Details | Choose Configure on the right to Configure Condition Contract Types for Customer Condition Contracts. | The Configure Condition Contract Types for Cust..: Change screen displays. |  |
| 6 | Remove Block | In column Block, choose Not Blocked – Can be Used for condition contract type you use in the test procedures:For multiple company codes process variant:0S05 Sales Rebate - MultOrgData 2Step0S06 Sales Rebate - MultCustomersOrg- 2Step0SG5 Sales Rebate Goods Rel MultOrg - 2Step0SG6 Sales Rebate GoodsRel MultCustOrg- 2StepFor fixed amount agreements:0SF1 Sales Rebate Fixed Amount0SF3 Sales Rebate Fixed Amount - 2StepChoose Save. | The condition contract types are no longer blocked. |  |

SAP Central Business Configuration:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the project experience in SAP Central Business Configuration. |  |  |
| 2 | Access the App | Go to the Business Processes Configuration app. To locate the activity in the tree view, search for the following activity: Configure Condition Contract Types for Customer Condition Contracts.Choose Open Documentation for the found line item to see more details about this configuration activity.Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. | The Configure Condition Contract Types for Cust..: Change screen displays. |  |
| 3 | Remove Block | In column Block, choose Not Blocked – Can be Used for condition contract type you use in the test procedures:For multiple company codes process variant:0S05 Sales Rebate - MultOrgData 2Step0S06 Sales Rebate - MultCustomersOrg- 2Step0SG5 Sales Rebate Goods Rel MultOrg - 2Step0SG6 Sales Rebate GoodsRel MultCustOrg- 2StepFor fixed amount agreements:0SF1 Sales Rebate Fixed Amount0SF3 Sales Rebate Fixed Amount - 2StepChoose Save. | The condition contract types are no longer blocked. |  |

#### Define Condition Contract Process Variants (Optional)

This chapter describes the definition of condition contract process variants to also test variations of the core process. A process variant is used to define limited variations for condition contract maintenance and settlement that are configured for a condition contract type without changing the overall character of the process defined by a condition contract type. In this chapter, we describe process variants for different purposes. Note that you can also combine settings from these process variants.

For the use of condition contract process variant, you must also enhance the account determination settings. The process variant is a key field in the relevant condition table. We describe how you maintain account determination settings for the first process variant for approval workflow. Proceed in the same way for all other process variants that you want to test.

When you create a new condition contract and you want to apply the process variations of a condition contract process variant, enter the condition contract process variant on the Basic Data tab page.

##### Define Process Variant for Using the Workflow

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you create a condition contract process variant to activate the workflow for sales rebate processing.

Procedure

Depending on your configuration environment for SAP S/4HANA Cloud Public Edition, choose one of the following options:

Configure Your Solution:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. |  |  |
| 2 | Access the App | Open Manage Your Solution (F1241).Note To create country-/region-dependent settings for the intended local version, choose Set Local Version. | The Manage Your Solution screen displays. |  |
| 3 | Open Configure Your Solution | Choose Configure Your Solution. | The Configure Your Solution: Realize Phase screen displays. |  |
| 4 | Open Configuration Item for Sales Rebate | Enter the following filters:Application Area: SalesSub Application Area: Sales Rebate ManagementIn the items table, select the item with item name: Sales Rebate Settlement. | The Configure Your Solution - Sales Rebate Settlement screen displays. |  |
| 5 | Go to Configuration Details | Choose Configure on the right to Define Condition Contract Process Variants configuration steps. | The "Define Condition Contract Process Variants": Change screen displays. |  |
| 6 | Create Process Variant | Choose New Entries and make the following entries:Condition Contract Process Variant: ZS01 Sales Rebates with WorkflowSettlement Management Status Group: Sales RebateDefault Application Status for Settlement Documents: Workflow Release RequiredApproval Process: 1 Approval Process Is ActiveChoose Save. | The process variant is created. |  |
| 7 | Assign Contract Types to the Process Variant | Double-click Condition Contract Types on the left of the screen.Choose New Entries and make the following entry:Contract Type: 0S01Choose Save.Note Add further condition contract types if you want to test the process variant for other sales rebate scenarios. | The relevant condition contract type is assigned to newly-created process variant. |  |

SAP Central Business Configuration:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the project experience in SAP Central Business Configuration. |  |  |
| 2 | Access the App | Go to the Business Processes Configuration app. To locate the activity in the tree view, search for the following activity: Define Condition Contract Process Variants.Choose Open Documentation for the found line item to see more details about this configuration activity.Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. | The Configure Your Solution - Sales Rebate Settlement screen displays. |  |
| 3 | Create Process Variant | Choose New Entries and make the following entries:Condition Contract Process Variant: ZS01 Sales Rebates with WorkflowSettlement Management Status Group: Sales RebateDefault Application Status for Settlement Documents: Workflow Release RequiredApproval Process: 1 Approval Process Is ActiveChoose Save. | The process variant is created. |  |
| 4 | Assign Contract Types to the Process Variant | Double-click Condition Contract Types on the left of the screen.Choose New Entries and make the following entry:Contract Type: 0S01Choose Save.Note Add further condition contract types if you want to test the process variant for other sales rebate scenarios. | The relevant condition contract type is assigned to newly-created process variant. |  |

##### Define Process Variant for Tax Free Goods

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you create a condition contract process variant which controls that sales rebate is treated tax-free.

Some countries, like the USA, do not offer tax services. When sales rebate is regarded as a service, taxation will be set to zero for the sales rebate amount. Tax-free sales rebate is achieved with this process variant in which you set the tax indicator for materials to zero. This tax indicator setting is transferred to pricing of a settlement run by a configured transfer rule.

If you want to treat sales rebate tax-free, make sure that you assign the condition contract process variant when you create a new condition contract.

Procedure

Depending on your configuration environment for SAP S/4HANA Cloud Public Edition, choose one of the following options:

Configure Your Solution:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. |  |  |
| 2 | Access the App | Open Manage Your Solution (F1241).Note To create country-/region-dependent settings for the intended local version, choose Set Local Version. | The Manage Your Solution screen displays. |  |
| 3 | Open Configure Your Solution | Choose Configure Your Solution. | The Configure Your Solution: Realize Phase screen displays. |  |
| 4 | Open Configuration Item for Sales Rebate Settlement | Enter the following filters:Application Area: SalesSub Application Area: Sales Rebate ManagementIn the items table, select the item with item name: Sales Rebate Settlement. | The Configure Your Solution - Sales Rebate Settlement screen displays. |  |
| 5 | Go to Configuration Details | Choose Configure on the right to Define Condition Contract Process Variants configuration step. | The "Define Condition Contract Process Variants": Change screen displays. |  |
| 6 | Create Process Variant | Choose New Entries and make the following entry:Condition Contract Process Variant: ZS02 Sales Rebates with Tax Free GoodsChoose Save. | The process variant is created. |  |
| 7 | Assign Contract Types to the Process Variant | Double-click Condition Contract Types on the left of the screen.Choose New Entries and make the following entry:Contract Type: 0S01Choose Save.Note Add further condition contract types if you want to test the process variant for other sales rebate scenarios. | The relevant condition contract type is assigned to newly-created process variant. |  |
| 8 | Define Company Code Specific Settings | Double-click Company Code Specific Settings on the left of the screen.Choose New Entries and make the following entries:Company Code: 3310Tax Indicator for Material: 0Choose Save. |  |  |

SAP Central Business Configuration:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the project experience in SAP Central Business Configuration. |  |  |
| 2 | Access the App | Go to the Business Processes Configuration app. To locate the activity in the tree view, search for the following activity: Define Condition Contract Process Variants.Choose Open Documentation for the found line item to see more details about this configuration activity.Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. | The Configure Your Solution - Sales Rebate Settlement screen displays. |  |
| 3 | Create Process Variant | Choose New Entries and make the following entry:Condition Contract Process Variant: ZS02 Sales Rebates with Tax Free GoodsChoose Save. | The process variant is created. |  |
| 4 | Assign Contract Types to the Process Variant | Double-click Condition Contract Types on the left of the screen.Choose New Entries and make the following entry:Contract Type: 0S01Choose Save.Note Add further condition contract types if you want to test the process variant for other sales rebate scenarios. | The relevant condition contract type is assigned to newly-created process variant. |  |
| 5 | Define Company Code Specific Settings | Double-click Company Code Specific Settings on the left of the screen.Choose New Entries and make the following entries:Company Code: 3310Tax Indicator for Material: 0Choose Save. |  |  |

##### Define Process Variant for Split Criteria Usage in Settlement

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you create a condition contract process variant to activate further split criteria defined in the profiles for business volume determination.

Split criteria for condition contract settlement – defined in Customizing in the profiles for business volume determination – are used to point up the contribution of different business objects to the overall sales rebate amount. In the profile for business volume determination relevant for sales rebate settlement, some split criteria, such as material or profit center, are defined as always active. The usage of these split criteria cannot be influenced with a condition contract process variant. But there are other split criteria which are defined as inactive until activated by a process variant. Note that for the test of an additionally activated split criterion you also have to prepare the business volume data accordingly with different values for the split criterion.

Procedure

Depending on your configuration environment for SAP S/4HANA Cloud Public Edition, choose one of the following options:

Configure Your Solution:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. |  |  |
| 2 | Access the App | Open Manage Your Solution (F1241).Note To create country-/region-dependent settings for the intended local version, choose Set Local Version. | The Manage Your Solution screen displays. |  |
| 3 | Open Configure Your Solution | Choose Configure Your Solution. | The Configure Your Solution: Realize Phase screen displays. |  |
| 4 | Open Configuration Item for Sales Rebate Settlement | Enter the following filters:Application Area: SalesSub Application Area: Sales Rebate ManagementIn the items table, select the item with item name: Sales Rebate Settlement. | The Configure Your Solution - Sales Rebate Settlement screen displays. |  |
| 5 | Go to Configuration Details | Choose Configure on the right to Define Condition Contract Process Variants configuration steps. | The "Define Condition Contract Process Variants": Change screen displays. |  |
| 6 | Create Process Variant | Choose New Entries and make the following entry:Condition Contract Process Variant: ZS03 Split Criteria AdaptationChoose Save. | The process variant is created. |  |
| 7 | Assign Contract Types to the Process Variant | Double-click Condition Contract Types on the left of the screen.Choose New Entries and make the following entry:Contract Type: 0S01Note Add further condition contract types if you want to test the process variant for other sales rebate scenarios. | The relevant condition contract type is assigned to newly-created process variant. |  |
| 8 | Activate/Deactivate Split Criteria for Settlement | Double-click on Split Criteria for Settlement on the left of the screen.Choose New Entries and make the following entries:Profile: Sales RebateField Name: criteria from field help list, for example, AUFNRUsage as Split Criterion: select from the dropdown list, for example, Use as Split CriterionClick Enter and choose Save. | The split criteria usage is changed with the process variant. |  |

SAP Central Business Configuration:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the project experience in SAP Central Business Configuration. |  |  |
| 2 | Access the App | Go to the Business Processes Configuration app. To locate the activity in the tree view, search for the following activity: Define Condition Contract Process Variants.Choose Open Documentation for the found line item to see more details about this configuration activity.Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. | The Configure Your Solution - Sales Rebate Settlement screen displays. |  |
| 3 | Create Process Variant | Choose New Entries and make the following entries:Condition Contract Process Variant: ZS03 Split Criteria AdaptationChoose Save. | The process variant is created. |  |
| 4 | Assign Contract Types to the Process Variant | Double-click Condition Contract Types on the left of the screen.Choose New Entries and make the following entry:Contract Type: 0S01Note Add further condition contract types if you want to test the process variant for other sales rebate scenarios. | The relevant condition contract type is assigned to newly-created process variant. |  |
| 5 | Activate/Deactivate Split Criteria for Settlement | Double-click Split Criteria for Settlement on the left of the screen.Choose New Entries and make the following entries:Profile: Sales RebateField Name: criteria from field help list, for example, AUFNRUsage as Split Criterion: select from the dropdown list, for example, Use as Split CriterionClick Enter and choose Save. | The split criteria usage is changed with the process variant. |  |

##### Define Process Variant for Business Volume Selection Criteria Usage

Purpose

In this activity, you create a condition contract process variant to change the usage of business volume selection criteria defined in the relevant set of field combinations.

To allow high flexibility in the business volume selection, the set of field combinations for sales rebate settlement provides many business volume selection criteria. However, this larger number can complicate the maintenance of business volume selection criteria in the condition contract as the user needs to find the desired field combination in a long list when he wants to enter a new line. With a suitable condition contract process variant, you can reduce the scope of business volume selection criteria to the relevant ones.

Procedure

Depending on your configuration environment for SAP S/4HANA Cloud Public Edition, choose one of the following options:

Configure Your Solution:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. |  |  |
| 2 | Access the App | Open Manage Your Solution (F1241).Note To create country-/region-dependent settings for the intended local version, choose Set Local Version. | The Manage Your Solution screen displays. |  |
| 3 | Open Configure Your Solution | Choose Configure Your Solution. | The Configure Your Solution: Realize Phase screen displays. |  |
| 4 | Open Configuration Item for Sales Rebate Settlement | Enter the following filters:Application Area: SalesSub Application Area: Sales Rebate ManagementIn the items table, select the item with item name: Sales Rebate Settlement. | The Configure Your Solution - Sales Rebate Settlement screen displays. |  |
| 5 | Go to Configuration Details | Choose Configure on the right to Define Condition Contract Process Variants configuration steps. | The "Define Condition Contract Process Variants": Change screen displays. |  |
| 6 | Create Process Variant | Choose New Entries and make the following entries:Condition Contract Process Variant: ZS04 Selection Criteria AdaptationChoose Save. | The process variant is created. |  |
| 7 | Assign Contract Types to the Process Variant | Double-click Condition Contract Types on the left of the screen.Choose New Entries and make the following entry:Contract Type: 0S01Note Add further condition contract types if you want to test the process variant for other sales rebate scenarios. | The relevant condition contract type is assigned to newly-created process variant. |  |
| 8 | Change the Usage of Selection Criteria for Business Volume Determination | Double-click Business Volume Selection Criteria on the left of the screen.Choose New Entries and make the following entries:Set of Field Combinations: Sales RebateField Combination: select from field help list, for example, 0035Note You can choose 0069 for Customer Hierarchy.Usage of Field Combination: select from the dropdown list as used or not usedChoose Save. | The usage of field combination is changed with the process variant. |  |

SAP Central Business Configuration:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the project experience in SAP Central Business Configuration. |  |  |
| 2 | Access the App | Go to the Business Processes Configuration app. To locate the activity in the tree view, search for the following activity: Define Condition Contract Process Variants.Choose Open Documentation for the found line item to see more details about this configuration activity.Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. | The Configure Your Solution - Sales Rebate Settlement screen displays. |  |
| 3 | Create Process Variant | Choose New Entries and make the following entries:Condition Contract Process Variant: ZS04 Selection Criteria AdaptationChoose Save. | The process variant is created. |  |
| 4 | Assign Contract Types to the Process Variant | Double-click Condition Contract Types on the left of the screen.Choose New Entries and make the following entry:Contract Type: 0S01Note Add further condition contract types if you want to test the process variant for other sales rebate scenarios. | The relevant condition contract type is assigned to newly-created process variant. |  |
| 5 | Change the Usage of Selection Criteria for Business Volume Determination | Double-click Business Volume Selection Criteria on the left of the screen.Choose New Entries and make the following entries:Set of Field Combinations: Sales RebateField Combination: select from field help list, for example, 0035Note You can choose 0069 for Customer Hierarchy.Usage of Field Combination: select from the dropdown list as used or not usedChoose Save. | The usage of field combination is changed with the process variant. |  |

##### Define Process Variant to Configure Material Groups as Condition Level

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you create a condition contract process variant to change the usage of condition levels for condition records.

Procedure

Depending on your configuration environment for SAP S/4HANA Cloud Public Edition, choose one of the following options:

Configure Your Solution:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. |  |  |
| 2 | Access the App | Open Manage Your Solution (F1241).Note To create country-/region-dependent settings for the intended local version, choose Set Local Version. | The Manage Your Solution screen displays. |  |
| 3 | Open Configure Your Solution | Choose Configure Your Solution. | The Configure Your Solution: Realize Phase screen displays. |  |
| 4 | Open Configuration Item for Sales Rebate Settlement | Enter the following filters:Application Area: SalesSub Application Area: Sales Rebate ManagementIn the items table, select the item with item name: Sales Rebate Settlement. | The Configure Your Solution - Sales Rebate Settlement screen displays. |  |
| 5 | Go to Configuration Details | Choose Configure on the right to Define Condition Contract Process Variants configuration steps. | The "Define Condition Contract Process Variants": Change screen displays. |  |
| 6 | Create Process Variant | Choose New Entries and make the following entry:Condition Contract Process Variant: ZS05 Condition Level AdaptationChoose Save. | The process variant is created. |  |
| 7 | Assign Contract Types to the Process Variant | Double-click Condition Contract Types on the left of the screen.Choose New Entries and make the following entry:Contract Type: 0S01Note Add further condition contract types if you want to test the process variant for other sales rebate scenarios. | The relevant condition contract type is assigned to newly-created process variant. |  |
| 8 | Change the Usage of Condition Level | Double-click Condition Types / Tables on the left of the screen.Choose New Entries and make the following entries:Application: VCond.Type Group: 0S01Condition Type: RES1Table Number: 4ANUsage of Condition Level: ActiveClick Enter and choose Save. | The usage of condition level is changed with the process variant. |  |

SAP Central Business Configuration:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the project experience in SAP Central Business Configuration. |  |  |
| 2 | Access the App | Go to the Business Processes Configuration app. You can search for a configuration activity and navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration.Search for Define Condition Contract Process Variants and create the following settings. | The Configure Your Solution - Sales Rebate Settlement screen displays. |  |
| 3 | Create Process Variant | Choose New Entries and make the following entry:Condition Contract Process Variant: ZS05 Condition Level AdaptationChoose Save. | The process variant is created. |  |
| 4 | Assign Contract Types to the Process Variant | Double-click Condition Contract Types on the left of the screen.Choose New Entries and make the following entry:Contract Type: 0S01Note Add further condition contract types if you want to test the process variant for other sales rebate scenarios. | The relevant condition contract type is assigned to newly-created process variant. |  |
| 5 | Change the Usage of Condition Level | Double-click Condition Types / Tables on the left of the screen.Choose New Entries and make the following entries:Application: VCond.Type Group: 0S01Condition Type: RES1Table Number: 4ANUsage of Condition Level: ActiveClick Enter and choose Save. | The usage of condition level is changed with the process variant. |  |

##### Define Process Variant to Configure Settings for Fixed Amount Agreements

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you create a condition contract process variant to specify settings for fixed amount agreements.

Procedure

Depending on your configuration environment for SAP S/4HANA Cloud Public Edition, choose one of the following options:

Configure Your Solution:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. |  |  |
| 2 | Access the App | Open Manage Your Solution (F1241).Note To create country-/region-dependent settings for the intended local version, choose Set Local Version. | The Manage Your Solution screen displays. |  |
| 3 | Open Configure Your Solution | Choose Configure Your Solution. | The Configure Your Solution: Realize Phase screen displays. |  |
| 4 | Open Configuration Item for Sales Rebate Settlement | Enter the following filters:Application Area: SalesSub Application Area: Sales Rebate ManagementIn the items table, select the item with item name: Sales Rebate Settlement. | The Configure Your Solution - Sales Rebate Settlement screen displays. |  |
| 5 | Go to Configuration Details | Choose Configure on the right to Define Condition Contract Process Variants configuration steps. | The "Define Condition Contract Process Variants": Change screen displays. |  |
| 6 | Create Process Variant | Choose New Entries and make the following entries:Condition Contract Process Variant: ZS06 Fixed Amount AgreementAmount Split Across Periods: StandardIf you want to carry out cost recognition for fiscal periods, select the following two entries:No Accruals Reversal at Partial Settlement: <selected>Recognition Adjustment Active: <selected>Choose Save. | The process variant is created. |  |
| 7 | Assign Contract Types to the Process Variant | Double-click Condition Contract Types on the left of the screen.Choose New Entries and make the following entry:Contract Type: 0SF1, 0SF3 | The relevant condition contract type is assigned to newly-created process variant. |  |
| 8 | Activate Fixed Amount Settlement Proportionally Across Fiscal Periods (Optional) | If you want to settle the fixed amount proportionally across fiscal periods, you can activate the amount split function in the general settings.Double-click Condition Contract Types on the left of the screen.In the General Settings section, set the field Amount Split Periods Partial Settlement to Yes from the dropdown list. |  |  |
| 9 | Specify Plant | Double-click Company Code Specific Settings on the left of the screen.Choose New Entries and make the following entries:Company Code: according to test data, for example, 3310Plant for CO Data: according to test data, for example, 3310Click Enter and choose Save. | The plant is specified for profit center. |  |

SAP Central Business Configuration:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the project experience in SAP Central Business Configuration. |  |  |
| 2 | Access the App | Go to the Business Processes Configuration app. You can search for a configuration activity and navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration.Search for Define Condition Contract Process Variants and create the following settings. | The Configure Your Solution - Sales Rebate Settlement screen displays. |  |
| 3 | Create Process Variant | Choose New Entries and make the following entries:Condition Contract Process Variant: ZS06 Fixed Amount AgreementAmount Split Across Periods: StandardIf you want to carry out cost recognition for fiscal periods, select the following two entries:No Accruals Reversal at Partial Settlement: <selected>Recognition Adjustment Active: <selected>Choose Save. | The process variant is created. |  |
| 4 | Assign Contract Types to the Process Variant | Double-click Condition Contract Types on the left of the screen.Choose New Entries and make the following entry:Contract Type: 0SF1, 0SF3 | The relevant condition contract type is assigned to newly-created process variant. |  |
| 5 | Activate Fixed Amount Settlement Proportionally Across Fiscal Periods (Optional) | If you want to settle the fixed amount proportionally across fiscal periods, you can activate the amount split function in the general settings.Double-click Condition Contract Types on the left of the screen.In the General Settings section, set the field Amount Split Periods Partial Settlement to Yes from the dropdown list. |  |  |
| 6 | Specify Plant | Double-click Company Code Specific Settings on the left of the screen.Choose New Entries and make the following entries:Company Code: according to test data, for example, 3310Plant for CO Data: according to test data, for example, 3310Click Enter and choose Save. | The plant is specified for profit center. |  |

##### Define Process Variant for Contract Determination

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you create a condition contract process variant to adapt the condition contract determination in the pricing of a sales order which is required when you do not specify a customer as business volume selection criterion.

Procedure

Depending on your configuration environment for SAP S/4HANA Cloud Public Edition, choose one of the following options:

Configure Your Solution:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. |  |  |
| 2 | Access the App | Open Manage Your Solution (F1241).Note To create country-/region-dependent settings for the intended local version, choose Set Local Version. | The Manage Your Solution screen displays. |  |
| 3 | Open Configure Your Solution | Choose Configure Your Solution. | The Configure Your Solution: Realize Phase screen displays. |  |
| 4 | Open Configuration Item for Sales Rebate Settlement | Enter the following filters:Application Area: SalesSub Application Area: Sales Rebate ManagementIn the items table, select the item with item name: Sales Rebate Settlement. | The Configure Your Solution - Sales Rebate Settlement screen displays. |  |
| 5 | Go to Configuration Details | Choose Configure on the right to Define Condition Contract Process Variants configuration step. | The "Define Condition Contract Process Variants": Change screen displays. |  |
| 6 | Create Process Variant | Choose New Entries and make the following entry:Condition Contract Process Variant: ZS07 Contract DeterminationChoose Save. | The process variant is created. |  |
| 7 | Assign Contract Types to the Process Variant | Double-click Condition Contract Types on the left of the screen.Choose New Entries and make the following entries:Contract Type: 0S01Relevant for Contract Determination: All CustomersChoose Save. | The relevant condition contract type is assigned to newly-created process variant. |  |

SAP Central Business Configuration:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the project experience in SAP Central Business Configuration. |  |  |
| 2 | Access the App | Go to the Business Processes Configuration app. To locate the activity in the tree view, search for the following activity: Define Condition Contract Process Variants.Choose Open Documentation for the found line item to see more details about this configuration activity.Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. | The Configure Your Solution - Sales Rebate Settlement screen displays. |  |
| 3 | Create Process Variant | Choose New Entries and make the following entry:Condition Contract Process Variant: ZS07 Contract DeterminationChoose Save. | The process variant is created. |  |
| 4 | Assign Contract Types to the Process Variant | Double-click Condition Contract Types on the left of the screen.Choose New Entries and make the following entries:Contract Type: 0S01Relevant for Contract Determination: All CustomersChoose Save. | The relevant condition contract type is assigned to newly-created process variant. |  |

##### Define Process Variant for Rebates on Paid Invoices

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you create a condition contract process variant to activate the usage of business volume table groups for the business volume determination. This enables that the rebate amount calculation only considers paid invoices.

Procedure

Depending on your configuration environment for SAP S/4HANA Cloud Public Edition, choose one of the following options:

Configure Your Solution:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. |  |  |
| 2 | Access the App | Open Manage Your Solution (F1241).Note To create country-/region-dependent settings for the intended local version, choose Set Local Version. | The Manage Your Solution screen displays. |  |
| 3 | Open Configure Your Solution | Choose Configure Your Solution. | The Configure Your Solution: Realize Phase screen displays. |  |
| 4 | Open Configuration Item for Sales Rebate Settlement | Enter the following filters:Application Area: SalesSub Application Area: Sales Rebate ManagementIn the items table, select the item with item name: Sales Rebate Settlement. | The Configure Your Solution - Sales Rebate Settlement screen displays. |  |
| 5 | Go to Configuration Details | Choose Configure on the right to Define Condition Contract Process Variants configuration steps. | The "Define Condition Contract Process Variants": Change screen displays. |  |
| 6 | Create Process Variant | Choose New Entries and make the following entry:Condition Contract Process Variant: ZS08 Sales Rebate on Paid InvoicesChoose Save. | The process variant is created. |  |
| 7 | Assign Contract Types to the Process Variant | Double-click Condition Contract Types on the left of the screen.Choose New Entries and make the following entry:Contract Type: 0S01Note Add further condition contract types if you want to test the process variant for other sales rebate scenarios. | The relevant condition contract type is assigned to newly-created process variant. |  |
| 8 | Activate Usage of Business Volume Table Group | Double-click on Business Volume Table Group on the left of the screen.Choose New Entries and make the following entries:Profile: 0S01BVTab Grp.: 0S01Usage: select from the dropdown list, Use in Condition Contract SettlementClick Enter and choose Save. | The split criteria usage is changed with the process variant. |  |

SAP Central Business Configuration:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the project experience in SAP Central Business Configuration. |  |  |
| 2 | Access the App | Go to the Business Processes Configuration app. To locate the activity in the tree view, search for the following activity: Define Condition Contract Process Variants.Choose Open Documentation for the found line item to see more details about this configuration activity.Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. | The Configure Your Solution - Sales Rebate Settlement screen displays. |  |
| 3 | Create Process Variant | Choose New Entries and make the following entries:Condition Contract Process Variant: ZS08 Sales Rebate on Paid InvoicesChoose Save. | The process variant is created. |  |
| 4 | Assign Contract Types to the Process Variant | Double-click Condition Contract Types on the left of the screen.Choose New Entries and make the following entry:Contract Type: 0S01Note Add further condition contract types if you want to test the process variant for other sales rebate scenarios. | The relevant condition contract type is assigned to newly-created process variant. |  |
| 5 | Activate Usage of Business Volume Table Group | Double-click on Business Volume Table Group on the left of the screen.Choose New Entries and make the following entries:Profile: 0S01BVTab Grp.: 0S01Usage: select from the dropdown list, Use in Condition Contract SettlementClick Enter and choose Save. | The split criteria usage is changed with the process variant. |  |

##### Define Process Variant for Different Bases for Rebate Calculation and Scale Determination

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you define a condition contract process variant that allows you to specify the business volume used for rebates separately from the business volume used to determine the rebate scale. For example, if you have a range of products and need to establish that the rebate scale is determined using transactional data from the entire range, but the rebate itself is applicable only to a selected subset of those products, you can achieve it by creating this process variant and using it within the condition contract.

Procedure

Depending on your configuration environment for SAP S/4HANA Cloud Public Edition, choose one of the following options:

Configure Your Solution:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. |  |  |
| 2 | Access the App | Open Manage Your Solution (F1241).Note To create country-/region-dependent settings for the intended local version, choose Set Local Version. | The Manage Your Solution screen displays. |  |
| 3 | Open Configure Your Solution | Choose Configure Your Solution. | The Configure Your Solution: Realize Phase screen displays. |  |
| 4 | Open Configuration Item for Sales Rebate Settlement | Enter the following filters:Application Area: SalesSub Application Area: Sales Rebate ManagementIn the items table, select the item with item name: Sales Rebate Settlement. | The Configure Your Solution - Sales Rebate Settlement screen displays. |  |
| 5 | Go to Configuration Details | Choose Configure on the right to Define Condition Contract Process Variants configuration steps. | The "Define Condition Contract Process Variants": Change screen displays. |  |
| 6 | Create Process Variant | Choose New Entries and make the following entry:Condition Contract Process Variant: ZS09 Sales Rebates with Different BasesChoose Save. | The process variant is created. |  |
| 7 | Assign Contract Types to the Process Variant | Double-click Condition Contract Types on the left of the screen.Choose New Entries and make the following entry:Contract Type: 0S01Note Add further condition contract types if you want to test the process variant for other sales rebate scenarios. | The relevant condition contract type is assigned to newly-created process variant. |  |
| 8 | Define Selection Groups | Double-click Selection Groups on the left of the screen.Choose New Entries and make the following entries:Profile: for example, 0S01Group: 0SRBUsage: 2 Use in Condition Contract SettlementMake the following entries for line 2:Profile: for example, 0S01Group: 0SSBUsage: 2 Use in Condition Contract SettlementIf you create new entries in step 7 for other contract types, then you need to create entries for the corresponding profiles in this step.Note See the following list to find the correct Profile required for each Condition Contract Type (CC Type).CC Type 0S01, 0S03 - Selection Group for profile 0S01CC Type 0S02, 0S04 - Selection Group for profile 0S02CC Type 0S05 - Selection Group for profile 0S03CC Type 0S06 - Selection Group for profile 0S04CC Type 0SG1, 0SG3 - Selection Group for profile 0SG1CC Type 0SG2, 0SG4 - Selection Group for profile 0SG2CC Type 0SG5 - Selection Group for profile 0SG3CC Type 0SG6 - Selection Group for profile 0SG4Click Enter and choose Save. |  |  |

SAP Central Business Configuration:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the project experience in SAP Central Business Configuration. |  |  |
| 2 | Access the App | Go to the Business Processes Configuration app. To locate the activity in the tree view, search for the following activity: Define Condition Contract Process Variants.Choose Open Documentation for the found line item to see more details about this configuration activity.Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. | The Configure Your Solution - Sales Rebate Settlement screen displays. |  |
| 3 | Create Process Variant | Choose New Entries and make the following entries:Condition Contract Process Variant: ZS09 Sales Rebates with Different BasesChoose Save. | The process variant is created. |  |
| 4 | Assign Contract Types to the Process Variant | Double-click Condition Contract Types on the left of the screen.Choose New Entries and make the following entry:Contract Type: 0S01Note Add further condition contract types if you want to test the process variant for other sales rebate scenarios. | The relevant condition contract type is assigned to newly-created process variant. |  |
| 5 | Define Selection Groups | Double-click Selection Groups on the left of the screen.Choose New Entries and make the following entries:Profile: for example, 0S01Group: 0SRBUsage: 2 Use in Condition Contract SettlementMake the following entries for line 2:Profile: for example, 0S01Group: 0SSBUsage: 2 Use in Condition Contract SettlementIf you create new entries in step 7 for other contract types, then you need to create entries for the corresponding profiles in this step.Note See the following list to find the correct Profile required for each Condition Contract Type (CC Type).CC Type 0S01, 0S03 - Selection Group for profile 0S01CC Type 0S02, 0S04 - Selection Group for profile 0S02CC Type 0S05 - Selection Group for profile 0S03CC Type 0S06 - Selection Group for profile 0S04CC Type 0SG1, 0SG3 - Selection Group for profile 0SG1CC Type 0SG2, 0SG4 - Selection Group for profile 0SG2CC Type 0SG5 - Selection Group for profile 0SG3CC Type 0SG6 - Selection Group for profile 0SG4Click Enter and choose Save. |  |  |

##### Define Process Variant to Activate Condition Table for Product Hierarchy

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you define a condition contract process variant that allows you to activate condition table for product hierarchy.

Procedure

Depending on your configuration environment for SAP S/4HANA Cloud Public Edition, choose one of the following options:

Configure Your Solution:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. |  |  |
| 2 | Access the App | Open Manage Your Solution (F1241).Note To create country-/region-dependent settings for the intended local version, choose Set Local Version. | The Manage Your Solution screen displays. |  |
| 3 | Open Configure Your Solution | Choose Configure Your Solution. | The Configure Your Solution: Realize Phase screen displays. |  |
| 4 | Open Configuration Item for Sales Rebate Settlement | Enter the following filters:Application Area: SalesSub Application Area: Sales Rebate ManagementIn the items table, select the item with item name: Sales Rebate Settlement. | The Configure Your Solution - Sales Rebate Settlement screen displays. |  |
| 5 | Go to Configuration Details | Choose Configure on the right to Define Condition Contract Process Variants configuration steps. | The "Define Condition Contract Process Variants": Change screen displays. |  |
| 6 | Create Process Variant | Choose New Entries and make the following entry:Condition Contract Process Variant: ZS10 Activate Condition for Product HierarchyChoose Save. | The process variant is created. |  |
| 7 | Assign Contract Types to the Process Variant | Double-click Condition Contract Types on the left of the screen.Choose New Entries and make the following entry:Contract Type: 0S01Note Add further condition contract types if you want to test the process variant for other sales rebate scenarios. | The relevant condition contract type is assigned to newly-created process variant. |  |
| 8 | Enter Condition Types / Tables | Double-click Condition Types / Tables on the left of the screen.Choose New Entries and make the following entries:Application: V Sales/DistributionCond.Type Group: 0S01Condition Type: RES1Table Number: 4CVUsage of Condition Level: 2 ActiveRepeat the current step if you need to active more condition types such as REA1.Click Enter and choose Save.Optionally, you can set product hierarchy as a split criterion by selecting Field Name: PRODH_UNIV_SALES_PARNT_NODID in step 8 in chapter [Define Process Variant for Split Criteria Usage in Settlement](#unique_15) [page ] 19. |  |  |

SAP Central Business Configuration:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the project experience in SAP Central Business Configuration. |  |  |
| 2 | Access the App | Go to the Business Processes Configuration app. To locate the activity in the tree view, search for the following activity: Define Condition Contract Process Variants.Choose Open Documentation for the found line item to see more details about this configuration activity.Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. | The Configure Your Solution - Sales Rebate Settlement screen displays. |  |
| 3 | Create Process Variant | Choose New Entries and make the following entries:Condition Contract Process Variant: ZS10 Activate Condition for Product HierarchyChoose Save. | The process variant is created. |  |
| 4 | Assign Contract Types to the Process Variant | Double-click Condition Contract Types on the left of the screen.Choose New Entries and make the following entry:Contract Type: 0S01Note Add further condition contract types if you want to test the process variant for other sales rebate scenarios. | The relevant condition contract type is assigned to newly-created process variant. |  |
| 5 | Enter Condition Types / Tables | Double-click Condition Types / Tables on the left of the screen.Choose New Entries and make the following entries:Application: V Sales/DistributionCond.Type Group: 0S01Condition Type: RES1Table Number: 4CVUsage of Condition Level: 2 ActiveRepeat the current step if you need to active more condition types such as REA1.Click Enter and choose Save.Optionally, you can set product hierarchy as a split criterion by selecting Field Name: PRODH_UNIV_SALES_PARNT_NODID in step 8 in chapter [Define Process Variant for Split Criteria Usage in Settlement](#unique_15) [page ] 19. |  |  |

##### Define Process Variant to Activate Business Volume Selection by Service Rendered Date

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you define a condition contract process variant that enables you to use service rendered date instead of billing date for the selection of billing documents to determine the business volume.

Procedure

Depending on your configuration environment for SAP S/4HANA Cloud Public Edition, choose one of the following options:

Configure Your Solution:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. |  |  |
| 2 | Access the App | Open Manage Your Solution (F1241).Note To create country-/region-dependent settings for the intended local version, choose Set Local Version. | The Manage Your Solution screen displays. |  |
| 3 | Open Configure Your Solution | Choose Configure Your Solution. | The Configure Your Solution: Realize Phase screen displays. |  |
| 4 | Open Configuration Item for Sales Rebate Settlement | Enter the following filters:Application Area: SalesSub Application Area: Sales Rebate ManagementIn the items table, select the item with item name: Sales Rebate Settlement. | The Configure Your Solution - Sales Rebate Settlement screen displays. |  |
| 5 | Go to Configuration Details | Choose Configure on the right to Define Condition Contract Process Variants configuration steps. | The "Define Condition Contract Process Variants": Change screen displays. |  |
| 6 | Create Process Variant | Choose New Entries and make the following entry:Condition Contract Process Variant: ZS11 BusVol Selection by Service Rendered DateChoose Save. | The process variant is created. |  |
| 7 | Assign Contract Types to the Process Variant | Double-click Condition Contract Types on the left of the screen.Choose New Entries and make the following entry:Contract Type: 0S01Business Volume Selection Date Type: 0001 Service Rendered DateNote Add further condition contract types if you want to test the process variant for other sales rebate scenarios. | The relevant condition contract type is assigned to newly-created process variant. |  |
| 8 | Enter Condition Types / Tables | This step is to ensure that only that accrual condition type which works with Service Rendered Date is selectable when creating your condition contract with this process variant.Double-click Condition Types / Tables on the left of the screen.Choose New Entries and make the following entries to set the condition type REA1 to inactive:Application: V Sales/DistributionCond.Type Group: 0S01Condition Type: REA1Usage of Condition Level: 1 InactiveRepeat the current step. Make the following entries to activate condition type REAA:Application: V Sales/DistributionCond.Type Group: 0S01Condition Type: REAAUsage of Condition Level: 2 ActiveClick Enter and choose Save. |  |  |

SAP Central Business Configuration:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the project experience in SAP Central Business Configuration. |  |  |
| 2 | Access the App | Go to the Business Processes Configuration app. To locate the activity in the tree view, search for the following activity: Define Condition Contract Process Variants.Choose Open Documentation for the found line item to see more details about this configuration activity.Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. | The Configure Your Solution - Sales Rebate Settlement screen displays. |  |
| 3 | Create Process Variant | Choose New Entries and make the following entries:Condition Contract Process Variant: ZS11 BusVol Selection by Service Rendered DateChoose Save. | The process variant is created. |  |
| 4 | Assign Contract Types to the Process Variant | This step is to ensure that only that accrual condition type which works with Service Rendered Date is selectable when creating your condition contract with this process variant.Double-click Condition Contract Types on the left of the screen.Choose New Entries and make the following entry:Contract Type: 0S01Business Volume Selection Date Type: 0001 Service Rendered DateNote Add further condition contract types if you want to test the process variant for other sales rebate scenarios. | The relevant condition contract type is assigned to newly-created process variant. |  |
| 5 | Enter Condition Types / Tables | Double-click Condition Types / Tables on the left of the screen.Choose New Entries and make the following entries to set the condition type REA1 to inactive:Application: V Sales/DistributionCond.Type Group: 0S01Condition Type: REA1Usage of Condition Level: 1 InactiveRepeat the current step. Make the following entries to activate condition type REAA:Application: V Sales/DistributionCond.Type Group: 0S01Condition Type: REAAUsage of Condition Level: 2 ActiveClick Enter and choose Save. |  |  |

##### Maintain Automatic Account Determination

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you specify G/L accounts for sales rebate processing.

If you assign a condition contract process variant to a new condition contract you can enhance the account determination settings. The process variant is a key field in the relevant condition table.

Procedure

Depending on your configuration environment for SAP S/4HANA Cloud Public Edition, choose one of the following options:

In the following steps, we show how to create the necessary entry for the first defined process variant ZS01 Sales Rebates with Workflow.

Configure Your Solution:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. |  |  |
| 2 | Access the App | Open Manage Your Solution (F1241).Note If required, choose Set Local Version to set the desired local version. | The Manage Your Solution screen displays. |  |
| 3 | Open Configure Your Solution | Choose Configure Your Solution. | The Configure Your Solution: Realize Phase screen displays. |  |
| 4 | Open Configuration Item for Chart of Accounts | Enter the following filters:Application Area: FinanceSub Application Area: General LedgerIn the items table, select the item with item name: Chart of Accounts. | The Configure Your Solution – Chart of Accounts screen displays. |  |
| 5 | Go to Configuration Details | Choose Configure on the right to Automatic Account Determination configuration step. | The Automatic Account Determination 1. Area screen displays. |  |
| 6 | Fill in Basic Information | Make the following entries:Area: SalesSubarea: Sales BillingProcess: Assign G/L AccountsChoose Step 2. | The Automatic Account Determination 2. Parameters screen displays. |  |
| 7 | Fill in Relevant Information | Make the following entries:Chart of Accounts: YCOAApplication: VCondition Table: 016Choose Step 3. | The Automatic Account Determination 3. Account Assignments screen displays. |  |
| 8 | Maintain G/L Account Assignment | Choose Add and scroll down to the bottom.Make the following entries:Condition Type: KORS Sales RebateCompany Code: 3310Process Variant: ZS01Account Key: 0S1 Rebate SalesG/L Account: 44001000Accruals Acc.: 21770000Choose Review. | The Automatic Account Determination screen displays with relevant information. |  |
| 9 | Review in the Information and Save | Choose Save. | The G/L account assignment is saved. |  |

SAP Central Business Configuration:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the project experience in SAP Central Business Configuration. |  |  |
| 2 | Open Automatic Account Determination | Go to the Business Processes Configuration app. To locate the activity in the tree view, search for the following activity: Automatic Account Determination.Choose Open Documentation for the found line item to see more details about this configuration activity.Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. | The Automatic Account Determination 1. Area screen displays. |  |
| 3 | Fill in Basic Information | Make the following entries:Area: SalesSubarea: Sales BillingProcess: Assign G/L AccountsChoose Step 2. | The Automatic Account Determination 2. Parameters screen displays. |  |
| 4 | Fill in Relevant Information | Make the following entries:Chart of Accounts: YCOAApplication: VCondition Table: 016Choose Step 3. | The Automatic Account Determination 3. Account Assignments screen displays. |  |
| 5 | Maintain G/L Account Assignment | Choose Add and scroll down to the bottom.Make the following entries:Condition Type: KORS Sales RebateCompany Code: 3310Process Variant: ZS01Account Key: 0S1 Rebate SalesG/L Account: 44001000Accruals Acc.: 21770000Choose Review. | The Automatic Account Determination screen displays with relevant information. |  |
| 6 | Review in the Information and Save | Choose Save. | The G/L account assignment is saved. |  |

#### Configure Approval Workflow (Optional)

##### Manage Teams and Responsibilities

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you maintain the teams and responsibilities for sales rebate workflow.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Business Process Specialist. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Teams and Responsibilities (F2412). |  |  |
| 3 | Create a New Team | Choose Create. |  |  |
| 4 | Enter General Information | In the General Information section, make the following entries and choose Enter:Name: for example, <CCM_TEST_TEAM_SD_(Country Code)>Description: for example, <Condition Contract Management Team Sales (Country Name)>Status: EnabledType: SCMTV Sales Condition Contract Team TypeIn the Responsibility Definitions section, make the following entry.Condition Contract Category: 0S | The team is created. |  |
| 5 | Add Team Members | In the Team Members section, choose Create.From the Items section, select a business partner check box and choose OK.Business Partner: for example, <Salesmanager> | The Select: Business Partner screen displays. |  |
| 6 | Add Functions to Team Members | Select a team member and choose Manage Functions.On the following dialog screen, mark SCCM_F1 Condition Contract Release Approval and the team member and choose OK.Repeat this step to select function SCCM_F2 Condition Contract Settlement Release Approval.Choose Create to create the team. | The team is saved. |  |
| 7 | Create a New Team | Go back and choose Create. | The Team screen displays. |  |
| 8 | Enter General Information | Make the following entries and choose Enter.Name: for example, <STLMT_TEST_TEAM_SD_(Country Code)>Description: for example, <Settlement Management Team Sales (Country Name)>Status: EnabledType: SMT Settlement Management Team TypeIn the Responsibility Definitions section, make the following entry.SettlmtDocType: 0S12 | The team is created. |  |
| 9 | Add Team Members | In the Team Members section, choose Create.From the Items section, select a business partner check box and choose OK.Business Partner: for example, <Salesmanager> | The Select: Business Partner screen displays. |  |
| 10 | Add Functions to Team Members | Select a team member and choose Manage Functions.On the following dialog screen, mark STLMTAPR Settlement Document Approver and the team member and choose OK.Choose Create to create the team. | The team is saved. |  |
| 11 | Check Team Status | Navigate to the Manage Teams and Responsibilities worklist and verify the status of the team by selecting Go.The status should be Enabled. | The team is ready to use. |  |

##### Manage Workflow for Condition Contracts - Release Contract

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you maintain workflow settings for the release of condition contracts.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Workflows for Condition Contracts (F3680). | The Manage Workflow screen displays. |  |
| 3 | Select Relevant Workflow | Select Release Condition Contract in the top left dropdown list.Choose Create. | The New Workflow screen displays. |  |
| 4 | Enter General Information | Make the following entries:Workflow Name: Workflow for Release of Condition Contract - Single Step Level ApprovalUnder Steps, choose Create. | The New Step screen displays. |  |
| 5 | Enter Details | Make the following entries:Step Type: Release of Condition ContractRole: Condition Contract Release ApprovalIn the Exception Handling section, make the following settings for Rework Condition Contract:Required Action: Rework of Condition ContractAction Result: Restart WorkflowChoose Create. | The New Workflow screen displays. |  |
| 6 | Save Workflow | Choose Save. | The Workflow Details screen displays. |  |
| 7 | Activate Workflow | Choose Activate. | The workflow is activated. |  |

##### Manage Workflow for Condition Contracts - Release Settlement

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you maintain workflow settings for the release of condition contract settlements.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Workflows for Condition Contracts (F3680). | The Manage Workflows screen displays. |  |
| 3 | Select Relevant Workflow | Select Settlement Release of Condition Contract in the top left dropdown list.Choose Create. | The New Workflow screen displays. |  |
| 4 | Enter General Information | Make the following entry:Workflow Name: Workflow for Settlement Release of Cond. Contract - Single StepChoose Create under Steps. | The New Step screen displays. |  |
| 5 | Input Details for the Workflow | Make the following entries:Step Type: Release of Condition Contract for SettlementRole: Condition Contract Settlement Release ApprovalIn the Exception Handling section, make the following settings for Rework Condition Contract:Required Action: Rework of Condition Contract for Settlement ReleaseAction Result: Restart WorkflowChoose Create. | The New Workflow screen displays. |  |
| 6 | Save Workflow Settings | Choose Save. | The Workflow Details screen displays. |  |
| 7 | Activate Workflow | Choose Activate. | The workflow is activated. |  |

##### Manage Workflow for Settlement Documents

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you maintain workflow settings for the approval of settlement documents.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Workflows for Settlement Documents (F3681). | The Manage Workflows screen displays. |  |
| 3 | Create New Workflow | Choose Create. | The New Workflow screen displays. |  |
| 4 | Enter General Information | Make the following entry:Workflow Name: Workflow for the approval of Settlement Document (To Accounting)Under Steps, choose Create. | The New Step screen displays. |  |
| 5 | Input Details | Make the following entries:Step Type: Release of Settlement DocumentRole: Settlement Document ApproverChoose Create. | The New Workflow screen displays. |  |
| 6 | Create New Step | Under Steps, choose Create. | The New Step screen displays. |  |
| 7 | Input Details | Make the following entry:Step Type: Automatic Change of Settlement Document StatusChoose Create. | The New Workflow screen displays. |  |
| 8 | Save the Workflow Settings | Click Save. | The Workflow Details screen displays. |  |
| 9 | Activate Workflow | Click Activate. | The workflow is activated. |  |

## Overview Table

This scope item consists of several process steps provided in the table below.

|  |
| --- |
| Note If your system administrator has enabled spaces and pages on the SAP Fiori launchpad, the homepage will only contain the essential apps for performing the typical tasks of a business role.You can find all other (searchable) apps not included on the homepage using the search bar ([2434549](https://me.sap.com/notes/2434549)).If you want to personalize the homepage and include the hidden apps, navigate to your user profile and choose App Finder. |

| Process Step | Business Role | Transaction/App | Expected Results |
| --- | --- | --- | --- |
| [Sales Rebate Processing – One Customer](#unique_29) [page ] 59 |  |  |  |
| [Create Condition Contract](#unique_8) [page ] 59 | Internal Sales Representative | Manage Condition Contracts - Sales Rebates (F6739) |  |
| [Check Business Volume (Optional)](#unique_30) [page ] 63 | Billing Clerk | Display Business Volume - Condition Contracts (WB2R_BUSVOL) |  |
| [Delta Accruals Settlement (Optional)](#unique_31) [page ] 65 | Billing Clerk | Settle Condition Contracts (WB2R_SC_SLSR) |  |
| [Check Settlement Document for Delta Accruals Settlement (Optional)](#unique_32) [page ] 66 | Billing Clerk | Manage Settlement Documents (F3254) |  |
| [Partial Settlement (Optional)](#unique_33) [page ] 67 | Billing Clerk | Settle Condition Contracts (WB2R_SC_SLSR) |  |
| [Check Settlement Document for Partial Settlement (Optional)](#unique_34) [page ] 68 | Billing Clerk | Manage Settlement Documents (F3254) |  |
| [Final Settlement](#unique_35) [page ] 71 | Billing Clerk | Settle Condition Contracts (WB2R_SC_SLSR) |  |
| [Check Settlement Document for Final Settlement (Optional)](#unique_36) [page ] 72 | Billing Clerk | Manage Settlement Documents (F3254) |  |
| [Sales Rebate Processing – Multiple Customers](#unique_37) [page ] 72 |  |  |  |
| [Create Condition Contract](#unique_9) [page ] 73 | Internal Sales Representative | Manage Condition Contracts - Sales Rebates (F6739) |  |
| [Check Business Volume (Optional)](#unique_38) [page ] 76 | Billing Clerk | Display Business Volume - Condition Contracts (WB2R_BUSVOL) |  |
| [Delta Accruals Settlement (Optional)](#unique_39) [page ] 76 | Billing Clerk | Settle Condition Contracts (WB2R_SC_SLSR) |  |
| [Partial Settlement (Optional)](#unique_40) [page ] 97 | Billing Clerk | Settle Condition Contracts (WB2R_SC_SLSR) |  |
| [Final Settlement](#unique_41) [page ] 98 | Billing Clerk | Settle Condition Contracts (WB2R_SC_SLSR) |  |
| [Sales Rebate Processing – Two-Step Settlement](#unique_42) [page ] 77 |  |  |  |
| [Create Condition Contract](#unique_43) [page ] 77 | Internal Sales Representative | Manage Condition Contracts - Sales Rebates (F6739) |  |
| [Check Business Volume (Optional)](#unique_44) [page ] 81 | Billing Clerk | Display Business Volume - Condition Contracts (WB2R_BUSVOL) |  |
| [Delta Accruals Settlement (Optional)](#unique_39) [page ] 76 | Billing Clerk | Settle Condition Contracts (WB2R_SC_SLSR) |  |
| [Partial Settlement (Optional)](#unique_40) [page ] 97 | Billing Clerk | Settle Condition Contracts (WB2R_SC_SLSR) |  |
| [Collect Parked Settlement Documents from Partial Settlement (Optional)](#unique_45) [page ] 82 | Billing Clerk | Collect Settlement Documents (WZRC) |  |
| [Final Settlement](#unique_41) [page ] 98 | Billing Clerk | Settle Condition Contracts (WB2R_SC_SLSR) |  |
| [Collect Parked Settlement Documents from Final Settlement](#unique_46) [page ] 83 | Billing Clerk | Collect Settlement Documents (WZRC) |  |
| [Goods Related Sales Rebate Processing](#unique_47) [page ] 84 | Internal Sales Representative/ Billing Clerk |  |  |
| [Sales Rebate Processing – Multiple Company Codes](#unique_48) [page ] 84 |  |  |  |
| [Create Condition Contracts](#unique_49) [page ] 85 | Internal Sales Representative | Manage Condition Contracts - Sales Rebates (F6739) |  |
| [Check Business Volume](#unique_50) [page ] 85 | Billing Clerk | Display Business Volume - Condition Contracts (WB2R_BUSVOL) |  |
| [Create Settlement Documents](#unique_51) [page ] 86 | Billing Clerk | Settle Condition Contracts (WB2R_SC_SLSR) |  |
| [Check Settlement Documents](#unique_52) [page ] 86 | Billing Clerk | Manage Settlement Documents (F3254) |  |
| [Collect Parked Settlement Documents](#unique_53) [page ] 86 | Billing Clerk | Collect Settlement Documents (WZRC) |  |
| [Check Collective Settlement Documents](#unique_54) [page ] 86 | Billing Clerk | Manage Settlement Documents (F3254) |  |
| [Sales Rebate Processing with Approval Workflow](#unique_55) [page ] 87 |  |  |  |
| [Create Condition Contract](#unique_56) [page ] 87 | Internal Sales Representative | Manage Condition Contracts - Sales Rebates (F6739) |  |
| [Request Approval to Release Condition Contract](#unique_57) [page ] 91 | Internal Sales Representative | Manage Condition Contracts - Sales Rebates (F6739) |  |
| [Trigger Rework of Condition Contract (Optional)](#unique_58) [page ] 92 | Sales Manager | My Inbox - All Items (F0862) |  |
| [Rework Condition Contract (Optional)](#unique_59) [page ] 93 | Sales Manager | My Inbox - All Items (F0862) |  |
| [Release Condition Contract](#unique_60) [page ] 94 | Sales Manager | My Inbox - All Items (F0862) |  |
| [Delta Accruals Settlement (Optional)](#unique_39) [page ] 76 | Billing Clerk | Settle Condition Contracts (WB2R_SC_SLSR) |  |
| [Request Release of Condition Contract for Settlement](#unique_61) [page ] 95 | Internal Sales Representative | Manage Condition Contracts - Sales Rebates (F6739) |  |
| [Release Condition Contract for Settlement](#unique_62) [page ] 96 | Sales Manager | My Inbox - All Items (F0862) |  |
| [Partial Settlement (Optional)](#unique_40) [page ] 97 | Billing Clerk | Settle Condition Contracts (WB2R_SC_SLSR) |  |
| [Approve Release of Partial Settlement Document to Accounting (Optional)](#unique_63) [page ] 97 | Sales Manager | My Inbox - All Items (F0862) |  |
| [Final Settlement](#unique_41) [page ] 98 | Billing Clerk | Settle Condition Contracts (WB2R_SC_SLSR) |  |
| [Approve Release of Final Settlement Document to Accounting](#unique_64) [page ] 98 | Sales Manager | My Inbox - All Items (F0862) |  |
| [Sales Rebate Processing with Different Bases for Rebate Calculation and Scale Determination](#unique_65) [page ] 98 | Internal Sales Representative | Manage Condition Contracts - Sales Rebates (F6739) |  |
| [Create Condition Contract](#unique_66) [page ] 99 | Internal Sales Representative | Manage Condition Contracts - Sales Rebates (F6739) |  |
| [Sales Rebate Processing with Graduated Scales](#unique_67) [page ] 100 | Internal Sales Representative | Manage Condition Contracts - Sales Rebates (F6739) |  |
| [Sales Rebate Processing with Conditions Maintained for Product Hierarchy Nodes](#unique_68) [page ] 101 | Internal Sales Representative | Manage Condition Contracts - Sales Rebates (F6739) |  |
| [Final Settlement with Adjustments (Optional)](#unique_69) [page ] 103 | Internal Sales Representative | Manage Condition Contracts - Sales Rebates (F6739) |  |
| [Rebate Unlikelihood (Optional)](#unique_70) [page ] 105 | Internal Sales Representative |  |  |
| [Sales Rebate Processing – Fixed Amount Agreements](#unique_71) [page ] 106 | Internal Sales Representative/ Billing Clerk |  |  |
| [Basic Processing](#unique_72) [page ] 106 | Internal Sales Representative | Manage Condition Contracts - Sales Rebates (F6739) |  |
| [Cost Recognition for Fiscal Periods](#unique_73) [page ] 109 | Billing Clerk |  |  |
| [Fixed Amount Settlement Proportionally Across Fiscal Periods](#unique_74) [page ] 110 | Internal Sales Representative | Manage Condition Contracts - Sales Rebates (F6739) |  |
| [Fixed Amount Distribution to Business Objects](#unique_75) [page ] 111 | Billing Clerk |  |  |
| [Fixed Amount Settlement on Multiple Products](#unique_76) [page ] 112 | Internal Sales Representative | Manage Condition Contracts - Sales Rebates (F6739) |  |
| [Reverse Settlement Document (Optional)](#unique_77) [page ] 112 | Billing Clerk | Reverse Settlement Documents - Condition Contracts (WB2R_CANCEL_DOCS) |  |

## Test Procedures

This chapter comprises the test procedures for different sales rebates processing variants covered by this scope item.

The variant differentiation results from the differentiation of agreements for one or multiple customers, from two basic types of the rebate agreements, and two ways for the settlement procedure.

In an agreement with one customer, you specify the customer in the condition contract header, and in a settlement run only one settlement document is created for this customer. In an agreement for multiple customers, the condition contract header does not contain an entry field for the business partner. Instead, customers are derived from the specified business volume, and separate settlement documents are created for each customer.

In the first type of rebate agreement, you regard sales rebates as a service for the customer. Under this perspective, you apply the usual value added tax for services. Alternatively, you can regard subsequent sales rebates as normal revenue reductions. Then you must apply the tax valid for the sales of a material (goods-related taxation).

Another process variation concerns the transfer of settlement documents to accounting. Usually, you create settlement documents that are immediately released to accounting. But you can also apply an alternative, two-step settlement procedure when you have several sales rebate agreements with the same customer. In the partial settlements and in the final settlement for the different condition contracts, you first create so called parked settlement documents that are not transferred to accounting. In a second step, you collect the parked settlement documents to create a collective settlement document, which is then transferred in one journal entry to accounting. Thus, you reduce the workload for the accounting module and have the information for the sales rebates settlement with a customer in one journal entry.

The two-step settlement procedure is also used for the following scenario: You want to settle a rebate agreement for a customer with a business volume generated in different company codes and for different sales areas in a way that you create separate settlement documents for the involved company codes and sales areas whereas for the determination of the scale level of the rebate condition, the business volume from all company codes and sales areas is considered. Company code and sales area serve as additional split criteria on item level for the parked settlement documents and as header split criteria in the creation of the collective settlement documents, so that actually the parked settlement documents are split by company code and sales area.

You can also use a customer hierarchy node in combination with condition contract types for single customers or multiple customers. Only hierarchies of type Customer Hierarchy – Sales can be used. When using a customer hierarchy node in condition contract types that apply to single customers (e.g. 0S01, 0S03), the application will check for business volume data corresponding to the customers belonging to the customer hierarchy node. If a customer hierarchy node is used with condition contract types for multiple customers (e.g. 0S02, 0S04), the application will check for business volume data corresponding to the customers belonging to the customer hierarchy node, and use the same set of customers as rebate recipients.

The test procedure for the different variants is very similar. To avoid unnecessary recurrences of identical test sequences, we therefore decided for the following approach.

In the first section Sales Rebate Processing - One Customer, we describe the test sequence for the basic process variant – service related sales rebates for one customer with direct release of settlement document to accounting – in detail. This process variant is represented by condition contract type 0S01. The description comprises the creation of the corresponding condition contract, the business volume control, the execution of the delta accruals, partial and final settlement, and guidelines for checking settlement results.

In the following sections, we only describe the differences, and when test sequences are identical, we refer to the first section. The second section Sales Rebate Processing - Multiple Customers deals with rebate agreements for multiple customers. The corresponding condition contract type is 0S02. The third section, Sales Rebate Processing – Two-Step Settlement, is about the two-step settlement procedure for the two variants mentioned before. Related condition contract types are 0S03 and 0S04. We describe the specific step for the creation of the collective settlement document only once for one customer. This step has to be executed similarly for the multiple customer variant. In section Goods Related Sales Rebate Processing, we look at sales rebate agreements representing a subsequent discount on the sales price. Related condition contract types are 0SG1 to 0SG4. As the operative processing is identical to the variants before, we only look at the different taxation within the settlement document.

For each of these process variants, you can configure a workflow process. This is subject matter of section Sales Rebate Processing with Approval Workflow. Again, we only describe the specific steps in detail, for other test sequences we refer to the first section. And we only describe the procedure for the basic process variant, the workflow steps for the other seven process variants are identical.

Finally, we describe some special aspects with chapters Final Settlement with Adjustments, Rebate Unlikelihood, Sales Rebate Processing – Fixed Amount Agreements, and Reverse Settlement Documents – Condition Contracts.

### Sales Rebate Processing – One Customer

This section describes the test sequence for the basic variant for sales rebates processing – service related sales rebates for one customer with direct release of settlement document to accounting. This process variant is represented by condition contract type 0S01. In this process variant, you regard rebates as a service for a customer. In the corresponding settlement as accounts receivable, you create a credit memo for the customer and you apply the usual value added tax for services to the rebate amount.

The detailed description comprises the creation of the condition contract for one customer, the business volume control, the execution of the delta accruals, partial and final settlement, and guidelines for checking settlement results.

As known, the sales rebates process runs in parallel to the regular sales process. Accordingly, we recommend creating new customer invoices (see chapter Preparation of Transactional Data) between the different settlement runs to check the evolution of accruals and rebate amounts. For this, you can also repeat the delta accruals settlement and partial settlement processing step as described.

#### Create Condition Contract

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this process step, you create a sales rebate condition contract for one customer as condition contract partner.

|  |
| --- |
| Note You can control several aspects for the maintenance of condition contracts with user settings. To check and change user settings, choose User Settings from the toolbar when you maintain or display a condition contract. You will see for instance in the Default Values for Conditions section that as default the validity of the condition contract will be copied when you enter a new condition record. But a subsequent adaptation is possible.Furthermore, the system processes several checks when you want to save a condition contract. For instance, it’s required that you have maintained a settlement date for the valid-to date of the condition contract. Similarly, you must maintain a settlement date for the valid-to date of condition records if you do not specify a condition contract process variant which enables a split by condition validity. |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Internal Sales Representative. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Condition Contracts - Sales Rebates (F6739). | The Manage Condition Contracts - Sales Rebates screen displays. |  |
| 3 | Select Condition Contract Type | On the Manage Condition Contracts - Sales Rebates screen, choose Create.On the following Select Condition Contract Type pop-up window, select condition contract type:0S01 Sales Rebate | The Create Sales Rebate screen displays. |  |
| 4 | Enter Contract Details | On the Create Sales Rebate screen, make the following entries and choose Enter:Customer: 33100003From: for example, <today's date>To: for example, <end of current year> |  |  |
| 5 | Enter Process Variant (Optional) | On the Basic Data tab, enter one of the condition contract process variants, each of which varies the basic scenario. Then choose Enter:Option A:Process Variant: ZS02 Sales Rebate with Tax Free GoodsOption B:Process Variant: ZS03 Split Criteria AdaptationOption C:Process Variant: ZS04 Selection Criteria AdaptationOption D:Process Variant: ZS05 Condition Level AdaptationOption E:Process Variant: ZS07 Contract DeterminationOption F:Process Variant: ZS08 Sales Rebate on Paid InvoicesNote When you enter process variant ZS08 to enable the process variation for sales rebates on paid invoices, you must also specify business volume table group 0S01 Sales Rebate Only Paid Invoices on the Settlement Data tab.The application does not differentiate between partially and fully paid invoices, and always takes the full amount in either case. |  |  |
| 6 | Enter Sales Data | On the Sales tab page, make and check the following entries:Sales Organization: 3310Distribution Channel: 10Division: 00Sales Office: 330Note This is a mandatory field to be input or there will be no accounting document created with business place missing when doing settlement |  |  |
| 7 | Enter Header Text | On the Header Texts tab page, make and check the following entries:Text Type: Text for Settlement DocumentLanguage: EnglishChoose Create Header Text and enter the header text. | The header text will be shown in the corresponding settlement documents.Note Choose language German if communication language of business partner is German. If the language of the text box deviates from the communication language of the business partner then the header text will not appear in the output form. |  |
| 8 | Enter Business Volume Base | On the Business Volume Selection Criteria tab page, select New Line. Make the following entries and choose Enter:Field Combination: 0001 CustomerInclusion Indicator (Incl/Excl): InclusiveCustomer: 33100003Select New Line. Make the following entries and choose Enter:Field Combination: 0009 MaterialInclusion Indicator (Incl/Excl): InclusiveMaterial: TG11 |  |  |
| 9 | Enter Settlement Data | On the Settlement Data tab page, make the following entries and choose Enter.Settlement Material: TG11Settlement Type Customer: As Accounts ReceivableNote The settlement material is optional. The settlement material is only needed if no business volume is available or no invoice documents are created for a defined settlement date.When you want to enable the process variation for sales rebates on paid invoices, make the following entry and choose Enter:Business Volume Table Group: 0S01 Sales Rebate Only Paid Invoices |  |  |
| 10 | Enter Settlement Calendar | On the Settlement Calendar tab page, select New Line.Make the following entries and choose Enter.Settlement Date: for example, <end of current year>Settlement Date Type: Final SettlementOptionally, enter settlement calendar dates for delta accruals and partial settlement.Select New Line.Make the following entries and choose Enter.Settlement Date: for example, <tomorrow's date>Settlement Date Type: Partial SettlementSelect New Line.Make the following entries and choose Enter.Settlement Date: for example, <today's date>Settlement Date Type: Delta Accruals |  |  |
| 11 | Enter Condition Record for Rebate | In the Conditions area, select the following entry:Condition Table: Condition ContractSelect New Condition.Make the following entries and choose Enter.Condition Type: RES1 RebateCondition Rate: for example, <1%>Valid From: for example, <today's date>Valid To: for example, <end of validity period>Scale Base Type: Value scale |  |  |
| 12 | Enter Scale Data | Select the condition line.Choose New Scale Level.Make the following entries and choose Enter.Scales: for example, <1000>Unit: AEDCondition Rate: for example, <1%>Select the first created condition line.Choose New Scale Level.Make the following entries and choose Enter.Scales: for example, <2000>Unit: AEDCondition Rate: for example, <2%> |  |  |
| 13 | Enter Condition Record for Accruals | In the Conditions area, select New Condition.Make the following entries and choose Enter.Condition Type: REA1 Rebate AccrualsCondition Rate: for example, <2%>Valid From: for example, <today's date>Valid To: for example, <end of validity period> |  |  |
| 14 | Release Condition Contract | Choose Release. |  |  |
| 15 | Save Condition Contract | Choose Save.Make a note of the condition contract number: __________. |  |  |

#### Check Business Volume (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this process step, you check the business volume for the condition contract.

Prerequisite

Use this step if you have prepared transactional data for the customer condition contract.

If you are using the process variant for paid invoices in the condition contract, then you need to post incoming payments for the billing documents that you want to consider for your test. The steps are explained in the scope item Accounts Receivable (J59).

Note

You can repeat this process step at every point in time in the test procedure. It’s recommendable to check the business volume before you start a settlement run to enable a control of the business volume determined for a settlement document.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Billing Clerk. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Display Business Volume - Condition Contracts (WB2R_BUSVOL). | The Business Volume for Condition Contracts screen displays. |  |
| 3 | Select Condition Contract | On the Business Volume for Condition Contracts screen, make the following entries:Condition Contract: <number of condition contract created before>Business Volume Base: From ContractOutput Level Business Volume: Settlement Date and Split Criteria |  |  |
| 4 | Check Business Volume for Condition Contracts | Choose Execute. | Business volume value REBV is determined based on the existing customer invoices. |  |
| 5 | Change Output Level (Optional) | Choose function Output Level Business Volume and Single Record on the Business Volume Selection Level dialog screen. | The system displays relevant billing document items for a settlement date of a condition contract. |  |

|  |
| --- |
| Note When you have enabled the process variation for sales rebates on paid invoices, you also see unpaid customer invoices in the business volume display with output level Single Record but with quantity and net amount 0. Unpaid customer invoices are displayed as potential candidates for a settlement. |

#### Delta Accruals Settlement (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this process step, you create a delta accruals settlement for the condition contract. With this delta accruals settlement, you post accruals for the billing documents related to the condition contract.

Prerequisite

Use this step if you have prepared transactional data for the customer condition contract.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori launchpad as a Billing Clerk. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Settle Condition Contracts (WB2R_SC_SLSR). | The Settlement of Customer Condition Contracts screen displays. |  |
| 3 | Select Condition Contract | On the Settlement of Customer Condition Contracts screen, make the following entries and choose Execute.Settlement Date: for example, <today's date>Settlement Date Type: 3 Delta AccrualsCondition Contract: <number of condition contract created before>Posting Date: for example, <today's date>Document Date: for example, <today's date>Run Type: Live RunList Range: Message LogSave Application Log: Only in Productive RunMessage Log Filter: No Filter | Settlement document for posting delta accruals is saved. |  |

#### Check Settlement Document for Delta Accruals Settlement (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this process step, you check the settlement document and accounting document for the delta accruals settlement.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Billing Clerk. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Settlement Documents (F3254). | The Manage Settlement Documents screen displays. |  |
| 3 | Display Document Data | In the Settlement Documents table, find the settlement document for the delta accruals settlement and choose the corresponding line. | The Settlement Document screen displays. |  |
| 4 | Check FI Posting Status | In the header area, check the posting status for the data transferred to Accounting. | The posting status is Accounting document has been created (C). |  |
| 5 | Check Reference Information | Under General Information > Basic Settlement Data, check the reference information. | Under Reference Information, field Reference contains the number of the settlement document, and field Assignment contains the number of the condition contract. |  |
| 6 | Check Document Items | Under Items, check the items of the settlement documents. | The system has created the items according to the split criteria. |  |
| 7 | Check Pricing of Items | Click an item in the table. On the following Settlement Document Item screen, under Pricing Elements, check the pricing elements of the settlement document item.Repeat this step for all items. | The system has determined the relevant business volume and displays it for condition type REBV Rebate Business Vol.The system has calculated the accruals amount with the relevant conditions maintained in the condition contract. |  |
| 8 | Check Document Flow | Go back to the Settlement Document screen.Under Document Flow, check that the delta accruals settlement document is displayed as follow-on document of the condition contract. Optionally, use the Expand function of nodes to display the complete flow. | The document flow with condition contract, settlement documents, and journal entry is displayed. |  |
| 9 | Check Journal Entries | Choose the Main Customer Journal Entries node. Click the icon right to the box and select Display Journal Entries from the pop-up window. | You see the financial posting as below. |  |

|  |
| --- |
| Note Also in case that you have enabled the process variation for sales rebates on paid invoices, the system posts accruals for unpaid customer invoices. These are still candidates for a settlement after an incoming payment so that you have to consider them as potential future payment obligations. |

Financial Posting

| G/L Account | Debit | Credit |
| --- | --- | --- |
| 44001000 (Sales Rebates) | <Accruals amount> | 0 |
| 21770000 (Accrd Volume Rebate) | 0 | <Accruals amount> |

#### Partial Settlement (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this process step, you create a partial settlement for the condition contract. In this step, you also reverse the accruals posted before.

Prerequisite

Use this step if you have prepared transactional data for the customer condition contract.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Billing Clerk. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Settle Condition Contracts (WB2R_SC_SLSR). | The Settlement of Customer Condition Contracts screen displays. |  |
| 3 | Select Condition Contract | On the Settlement of Customer Condition Contracts screen make the following entries and choose Execute.Settlement Date: for example, <tomorrow's date>Settlement Date Type: 1 Partial SettlementCondition Contract: <number of condition contract created before>Posting Date: for example, <tomorrow's date>Document Date: for example, <tomorrow's date>Run Type: Live RunList Range: Message LogSave Application Log: Only in Productive RunMessage Log Filter: No FilterTake a note of the number of the credit memo created. | The Log for Customer Condition Contract Settlement screen displays. Customer Credit memo is created. Accruals are reversed. |  |

#### Check Settlement Document for Partial Settlement (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this process step, you check the settlement document and accounting document for partial settlement.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Billing Clerk. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Settlement Documents (F3254). | The Manage Settlement Documents screen displays. |  |
| 3 | Display Document Data | In the Settlement Documents table, find the settlement document for the partial settlement and choose the corresponding line. | The Settlement Document screen displays. |  |
| 4 | Check FI Posting Status | In the header area, check the posting status for the data transferred to Accounting. | The posting status is Accounting document has been created (C). |  |
| 5 | Check Reference Information | Under General Information > Basic Settlement Data, check the reference information. | Under Reference Information, field Reference contains the number of the settlement document, and field Assignment contains the number of the condition contract. |  |
| 6 | Check Partner Data | Under Partner Data, check the partner information. | You see the partner data maintained in the master data. |  |
| 7 | Check Document Items | Under Items, check the items of the settlement documents. | The system has created the items according to the split criteria. |  |
| 8 | Check Pricing of Items | Click an item in the Settlement Document Items table. On the following Settlement Document Item screen, under Pricing Elements, check the pricing elements of the settlement document item.Repeat this step for all the items. | The system has determined the relevant business volume and displays it for condition type REBV Rebate Business Vol. The system has calculated the rebate amount with condition type RES1 maintained in the condition contract and the output tax with the percentage for full tax. The system shows the amount of reversed accruals for condition type REA2 and the amount for excess accruals for condition type REA5. |  |
| 9 | Check Output | Go back to the Settlement Document screen, under Output Items, check the output items.Find the item with Channel: Print and choose Open File under Display. | You see the output print form. |  |
| 10 | Check Document Flow | Go back to the Settlement Document screen.Under Document Flow, check that the settlement document for partial settlement is displayed as follow-on document of the condition contract. Optionally, use the Expand function of nodes to display the complete flow. | The document flow with condition contract, settlement documents, and journal entry is displayed. |  |
| 11 | Check Journal Entries | Choose the Main Customer Journal Entries node. Click the icon right to the box and select Display Journal Entries from the pop-up window. | You see the financial posting as below.The accruals reversal amount is the difference between the amount of reversed accruals and the excess accruals as mentioned in step 8. |  |
| 12 | Check Texts | Go back to the Manage Settlement Documents screen.In the Settlement Documents table, click the settlement document number and select Display Settlement Document from the pop-up window.Choose Header Texts. Under Texts, check the text information. | For text type Contract Text for Output/Forms, you see the text maintained in the condition contract for text type Text for Settlement Document. |  |

|  |
| --- |
| Note In case that you have enabled the process variation for sales rebates on paid invoices, the system considers accruals for unpaid customer invoices when writing back the excess accruals amount to the accruals index table with condition type REA5. |

Financial Posting

| G/L Account | Debit | Credit |
| --- | --- | --- |
| 12100000 (Receivables Domestic) | 0 | <Sales rebate amount + Output tax> |
| 44001000 (Sales Rebates) | <Sales rebate amount> | 0 |
| 22000000 (Output Tax (MWS)) | <Output tax> | 0 |
| 44001000 (Sales Rebates) | 0 | <Accruals reversal amount> |
| 21770000 (Accrued Volume Rebate) | <Accruals reversal amount> | 0 |

#### Final Settlement

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this process step, you create a final settlement for the condition contract. In this step, you also reverse the accruals posted before.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Billing Clerk. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Settle Condition Contracts (WB2R_SC_SLSR). | The Settlement of Customer Condition Contracts screen displays. |  |
| 3 | Select Condition Contract | On the Settlement of Customer Condition Contracts screen, make the following entries and choose Execute.Settlement Date: for example, <end of current year date>Settlement Date Type: Final SettlementCondition Contract: <Number of condition contract created before>Posting Date: for example, <today's date>Document Date: for example, <today's date>Run Type: Live RunList Range: Message LogSave Application Log: Only in Productive runMessage Log Filter: No FilterTake a note of the number of the credit memo created. | The Log for Customer Condition Contract Settlement screen displays. Customer credit memo is created. Accruals are reversed. |  |
| 4 | Optional: Check | Note If the workflow is activated, in this step, you will see the following messages including:Contract XXXXXXXXXXX locked after final settlementDocument XXXXXXXXXXX with document status Workflow Release Required is blocked for follow-on documentsDocument XXXXXXXXXXX saved (no accounting document generated)Document XXXXXXXXXXX is processed with reference XXXXXXXXXXX | Now the credit memo for the condition contract is created but the journal entry is not yet created. |  |

#### Check Settlement Document for Final Settlement (Optional)

Please follow process steps of chapter Check Settlement Document for Partial Settlement (Optional) in section Sales Rebate Processing – One Customer.

Note the following difference: for the pricing elements of the settlement document items, check that all accruals are reversed. That means the amount for excess accruals for condition type REA5 is zero.

### Sales Rebate Processing – Multiple Customers

This section deals with the first process variant for sales rebates processing – service related sales rebates for multiple customers with direct release of settlement document to accounting. This process variant is represented by condition contract type 0S02. This process variant is very similar to the basic processing. You do not enter a customer in the header, instead customers are derived from the specified business volume. For the different settlement runs, separate settlement documents are created for relevant customers.

#### Create Condition Contract

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this process step, you create a sales rebate condition contract for multiple customers.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Internal Sales Representative. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Condition Contracts - Sales Rebates (F6739). | The Manage Condition Contracts - Sales Rebates screen displays. |  |
| 3 | Select Condition Contract Type | On the Manage Condition Contracts - Sales Rebates screen, choose Create.On the following Select Condition Contract Type pop-up window, select condition contract type:0S02 Sales Rebate - Multiple Customers |  |  |
| 4 | Enter Contract Details | On the Create Sales Rebate – Multiple Customers screen, make the following entries and choose Enter:From: for example, <today's date>To: for example, <end of the current year> |  |  |
| 5 | Enter Sales Data | On the Sales tab page, make the following entries:Sales Organization: 3310Distribution Channel: 10Division: 00Sales Office: 330 (This is a mandatory field to be input or there will be no accounting document created with business place missing when doing settlement) |  |  |
| 6 | Enter Header Text | On the Header Texts tab page, make and check the following entries:Text Type: Text for Settlement DocumentLanguage: EnglishChoose Create Header Text and enter the header text. | The header text will be shown in the corresponding settlement documents.Note Choose language German if the communication language of the business partner is German. If the language of the text box deviates from the communication language of the business partner then the header text will not appear in the output form. |  |
| 7 | Enter Business Volume Base | On the Business Volume Selection Criteria tab page, select New Line. Make the following entries and choose Enter:Field Combination: 0001 CustomerInclusion Indicator (Incl/Excl): InclusiveCustomer: 33100003Select New Line. Make the following entries and choose Enter:Field Combination: 0001 CustomerInclusion Indicator (Incl/Excl): InclusiveCustomer: 33100008Select New Line. Make the following entries and choose Enter:Field Combination: 0009 MaterialInclusion Indicator (Incl/Excl): InclusiveMaterial: TG11Optionally, you can also limit the business volume to certain customers using field combination 0001 Customer.Note In case you have processed the optional Sell from Stock (BD9) scope item for sales orders created for more than one customer (multiple customers), use these customers here to create the condition contract. Each customer listed in the business volume selection criteria will receive settlement documents based on its individual revenue. |  |  |
| 8 | Enter Settlement Data | On the Settlement Data tab page, make the following entries and choose Enter:Settlement Material: TG11Settlement Type Customer: As Accounts ReceivableNote The settlement material is optional. The settlement material is only needed if no business volume is available or no invoice documents are created for a defined settlement date. |  |  |
| 9 | Enter Settlement Calendar | On the Settlement Calendar tab page, select New Line. Make the following entries and choose Enter:Settlement Date: for example, <end of the current year>Settlement Date Type: Final SettlementSelect New Line. Make the following entries and choose Enter:Settlement Date: for example, <tomorrow's date>Settlement Date Type: Partial SettlementSelect New Line. Make the following entries and choose Enter:Settlement Date: for example, <today's date>Settlement Date Type: Delta accrualsNote The creation of the line with Settlement Date Type: Delta accruals is optional.The creation of the line with Settlement Date Type: Partial settlement is optional. |  |  |
| 10 | Enter Condition Record for Rebate | In the Conditions area, select the following entry:Condition Table: Condition ContractSelect New Condition, make the following entries and choose Enter.Condition Type: RES1 RebateCondition Rate: for example, <1%>Valid From: for example, <today's date>Valid To: for example, <end of the current year>Scale Base Type: Value scaleNote This condition is used to calculate the base volume for payment.In case the Valid From date and the Valid To date are already there, you can check and change it. |  |  |
| 11 | Enter Scale Data | Select the condition line, choose New Scale Level. Make the following entries and choose Enter:Scales: for example, <1000>Unit: AEDCondition Rate: for example, <1%>Select the first created condition line.Choose New Scale Level.Make the following entries and choose Enter:Scales: for example, <2000>Unit: AEDCondition Rate: for example, <2%> |  |  |
| 12 | Enter Condition Record for Accruals | In the Conditions Area, select New Condition. Make the following entries and choose Enter:Condition Type: REA1 Rebate AccrualsCondition Rate: for example, <2%>Valid From: for example, <today's date>Valid To: for example, <end of the current year>Note This condition is used to calculate the amount for accruals.In case the Valid From date and the Valid To date are already there, you can check and change it. |  |  |
| 13 | Release Condition Contract | Choose Release. |  |  |
| 14 | Save Condition Contract | Choose Save. Make a note of the condition contract number: __________. |  |  |

#### Check Business Volume (Optional)

As described for the basic processing variant, also check the business volume in this test procedure before you start a settlement run to enable a control of the business volume determined for a settlement document.

Please follow process steps in Check Business Volume (Optional) in section Sales Rebate Processing – One Customer.

#### Delta Accruals Settlement (Optional)

Please follow process steps in Delta Accruals Settlement (Optional) in section Sales Rebate Processing – One Customer.

On the selection screen, enter the different condition contracts belonging to this test.

Delta accrual documents are created for each customer with contract relevant business volume for a condition contract with multiple customers as contract partners.

After you have processed the delta accruals settlement you can optionally check the created settlement documents as described in chapter Check Settlement Document for Delta Accruals Settlement (Optional) in section Sales Rebate Processing – One Customer.

#### Partial Settlement (Optional)

Please follow process steps in Partial Settlement (Optional) in section Sales Rebate Processing – One Customer.

On the selection screen, enter the different condition contracts belonging to this test.

After you have processed the partial settlement, you can optionally check the created settlement documents as described in chapter Check Settlement Document for Partial Settlement (Optional) in section Sales Rebate Processing – One Customer.

Partial settlement documents are created for each customer with contract relevant business volume for a condition contract with multiple customers as contract partners.

#### Final Settlement

Please follow process steps in Final Settlement in section Sales Rebate Processing – One Customer.

On the selection screen, enter the different condition contracts belonging to this test.

After you have processed the final settlement, you can optionally check the created settlement documents as described in chapter Check Settlement Document for Final Settlement (Optional) in section Sales Rebate Processing – One Customer.

### Sales Rebate Processing – Two-Step Settlement

The sales rebate processing – two-step settlement describes an alternative settlement procedure when you have several sales rebate agreements (condition contracts) with the same customer. In the partial settlements and in the final settlement for the different condition contracts, you first create so called parked settlement documents that are not transferred to accounting. In a second step, you collect the parked settlement documents to create a collective settlement document, which is then transferred in one journal entry to accounting. Thus, you reduce the workload for the accounting module and have the information for the sales rebate processing with a customer in one journal entry.

In the following, we describe the process variant for two-step settlement for a sales rebate agreement with one customer represented by condition contract type 0S03. The two-step settlement processing for the multiple customers variant runs in a similar way.

#### Create Condition Contract

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this process step, you create a condition contract for sales rebate processing involving two settlement steps. Here take condition contract type 0S03 Sales Rebate - 2Step as the two-step process example for one customer as condition contract partner. You can use condition contract type 0S04 Sales Rebate - Mult. Customers - 2Step for the two-step settlement process and multiple customers.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Internal Sales Representative. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Condition Contracts - Sales Rebates (F6739). | The Manage Condition Contracts - Sales Rebates screen displays. |  |
| 3 | Select Condition Contract Type | On the Manage Condition Contracts - Sales Rebates screen, choose Create.On the following Select Condition Contract Type pop-up window, select condition type:0S03 Sales Rebate – 2StepNote You can optionally choose Sales Rebate – Mult. Customers - 2step condition contract type if you want to collect and post settlement documents of different condition contracts in one journal entry to accounting. In that case, the reversal of the accruals together with the customer revenues is not posted until the creation of the collective settlement document. |  |  |
| 4 | Enter Contract Details | On the Create Sales Rebate - 2Step screen, make the following entries and choose Enter:Customer: 33100003From: for example, <today's date>To: for example, <end of the current year> |  |  |
| 5 | Enter Sales Data | On the Sales tab page, make the following entries:Sales Organization: 3310Distribution Channel: 10Division: 00Sales Office: 330 (This is a mandatory field to be input or there will be no accounting document created with business place missing when doing settlement) |  |  |
| 6 | Enter Header Text | On the Header Texts tab page, make and check the following entries:Text Type: Text for Settlement DocumentLanguage: EnglishChoose Create Header Text and enter the header text. | The header text will be shown in the corresponding settlement documents.Note Choose language German if the communication language of the business partner is German. If the language of the text box deviates from the communication language of the business partner then the header text will not appear in the output form. |  |
| 7 | Enter Business Volume Base | On the Business Volume Selection Criteria tab page, select New Line. Make the following entries and choose Enter:Field Combination: 0001 CustomerInclusion Indicator (Incl/Excl): InclusiveCustomer: 33100003Select New Line. Make the following entries and choose Enter:Field Combination: 0009 MaterialInclusion Indicator (Incl/Excl): InclusiveMaterial: TG11Optionally, you can also limit the business volume to certain customers using field combination 0001 Customer.Note In case you have processed the optional Sell from Stock (BD9) scope item for sales orders created for more than one customer (multiple customers), use these customers here to create the condition contract. Each customer listed in the business volume selection criteria will receive settlement documents based on its individual revenue. |  |  |
| 8 | Enter Settlement Data | On the Settlement Data tab page, make the following entries and choose Enter:Settlement Material: TG11Settlement Type Customer: As Accounts ReceivableNote The settlement material is optional. The settlement material is only needed if no business volume is available or no invoice documents are created for a defined settlement date. |  |  |
| 9 | Enter Settlement Calendar | On the Settlement Calendar tab page, select New Line. Make the following entries and choose Enter:Settlement Date: for example, <end of the current year>Settlement Date Type: Final SettlementSelect New Line. Make the following entries and choose Enter:Settlement Date: for example, <tomorrow's date>Settlement Date Type: Partial SettlementSelect New Line. Make the following entries and choose Enter:Settlement Date: for example, <today's date>Settlement Date Type: Delta accrualsNote The creation of the line with Settlement Date Type: Delta accruals is optional.The creation of the line with Settlement Date Type: Partial settlement is optional. |  |  |
| 10 | Enter Condition Record for Rebate | In the Conditions area, select the following entry:Condition Table: Condition ContractSelect New Condition, make the following entries and choose Enter.Condition Type: RES1 RebateCondition Rate: for example, <1%>Valid From: for example, <today's date>Valid To: for example, <end of the current year>Scale Base Type: Value scaleNote This condition is used to calculate the base volume for payment.In case the Valid From date and the Valid To date are already there, you can check and change it. |  |  |
| 11 | Enter Scale Data | Select the condition line, choose New Scale Level. Make the following entries and choose Enter:Scales: for example, <1000>Unit: AEDCondition Rate: for example, <1%>Select the first created condition line.Choose New Scale Level.Make the following entries and choose Enter:Scales: for example, <2000>Unit: AEDCondition Rate: for example, <2%> |  |  |
| 12 | Enter Condition Record for Accruals | In the Conditions area, select New Condition. Make the following entries and choose Enter:Condition Type: REA1 Rebate AccrualsCondition Rate: for example, <2%>Valid From: for example, <today's date>Valid To: for example, <end of the current year>Note This condition is used to calculate the amount for accruals.In case the Valid From date and the Valid To date are already there, you can check and change it. |  |  |
| 13 | Release Condition Contract | Choose Release. |  |  |
| 14 | Save Condition Contract | Choose Save. Make a note of the condition contract number: __________. |  |  |

#### Check Business Volume (Optional)

As described for the basic processing variant, also check the business volume in this test procedure before you start a settlement run to enable a control of the business volume determined for a settlement document.

Please follow process steps in Check Business Volume (Optional) in section Sales Rebate Processing – One Customer.

#### Delta Accruals Settlement (Optional)

Please follow process steps in Delta Accruals Settlement (Optional) in section Sales Rebate Processing – One Customer.

On the selection screen, enter the different condition contracts belonging to this test.

After you have processed the delta accruals settlement you can optionally check the created settlement documents as described in chapter Check Settlement Document for Delta Accruals Settlement (Optional) in section Sales Rebate Processing – One Customer.

#### Partial Settlement (Optional)

Please follow process steps in Partial Settlement in section Sales Rebate Processing – One Customer.

On the selection screen, enter the different condition contracts belonging to this test.

After you have processed the partial settlement, you can optionally check the created parked settlement documents as described in chapter Check Settlement Document for Partial Settlement (Optional) in section Sales Rebate Processing – One Customer.

Note the following differences: The posting status is Blocked for Accounting. Accordingly, there is not journal entry related to a parked settlement document. In addition, there is also no output related to a parked settlement document.

#### Collect Parked Settlement Documents from Partial Settlement (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this process step, you collect parked settlement documents from partial settlement in order to create a collective settlement document for transfer to accounting.

Prerequisite

As prerequisite for this process step, you have created several two-step condition contracts and you have performed the partial settlement for these condition contracts as described in chapter [Partial Settlement (Optional)](#unique_82) [page ] 82.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Billing Clerk. | The SAP Fiori launchpad displays. |  |
| 2 | Access Collect Settlement Documents | Open Collect Settlement Documents.On the Create Collective Documents from Settlement Documents screen, make the following entries and choose Execute.Document Numbers: <numbers of settlement documents for partial settlements created before>Check Run Only: <do not select> | The Create Collective Documents from Settlement Documents screen displays. |  |

#### Final Settlement

Please follow process steps of chapter Final Settlement in section Sales Rebate Processing – One Customer.

On the selection screen, enter the different condition contracts belonging to this test.

After you have processed the final settlement, you can optionally check the created parked settlement documents as described in chapter Check Settlement Document for Final Settlement (Optional) in section Sales Rebate Processing – One Customer.

Note the following differences: The posting status is Blocked for Accounting. Accordingly, there is not journal entry related to a parked settlement document. In addition, there is also no output related to a parked settlement document.

#### Collect Parked Settlement Documents from Final Settlement

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this process step, you collect parked settlement documents from final settlement in order to create a collective settlement document for transfer to accounting.

Prerequisite

As prerequisite for this process step, you have created several two-step condition contracts and you have performed the final settlement for these condition contracts as described in chapter [Final Settlement](#unique_83) [page ] 83.

Procedure

Process the steps described in the chapter [Collect Parked Settlement Documents from Partial Settlement (Optional)](#unique_45) [page ] 82.

|  |
| --- |
| Note After you have processed this step you can optionally check the created collective settlement document as described in chapter Check Settlement Document for Final Settlement (Optional) in section Sales Rebate Processing – One Customer. |

### Goods Related Sales Rebate Processing

In goods related sales rebate processing, you regard subsequent sales rebates as normal revenue reductions. This subsequent net sales price adaptation also means that you change the tax base used for former billing documents. Accordingly, in condition contract settlement, you must apply the same taxation for materials in settlement items as in related billing items. This makes up the name of these sales rebate process variants. To ensure same taxation, the system automatically considers tax related parameters, such as the tax code or different tax percentage rates as split criteria. You cannot influence this with a condition contract process variant. When you prepare transactional test data, you best use materials with different tax classifications.

SAP provides four condition contract types for goods related sales rebate processing similar to the process variants described above. Accordingly, follow the test steps of the corresponding sections.

Condition contract type 0SG1 Sales Rebate Goods Related for the goods related sales rebate processing with one customer and with direct release of settlement document to accounting.

Condition contract type 0SG2 Sales Rebate Goods Rel.- Mult. Customers, for the goods related sales rebate processing with multiple customers and with direct release of settlement document to accounting

Condition contract type 0SG3 Sales Rebate Goods Related - 2Step, and condition contract type 0SG4 Sales Rebate Goods Rel- MultCust - 2Step, for the goods related sales rebate processing applying a two-step settlement procedure and with one or multiple customers, respectively.

As only difference, we describe how you check the different taxation of materials in settlement documents for partial and final settlement. Follow the procedure described in Check Settlement Document for Partial Settlement (Optional). When you check the pricing of settlement document items on the Pricing Elements tab page, click on condition type MWAS and check that the tax code displayed in the Accounting section corresponds to the tax classification of the material.

### Sales Rebate Processing – Multiple Company Codes

Purpose

In the sales rebate processing – multiple company codes process variant, you want to settle a rebate agreement for a customer with a business volume generated in different company codes. In the settlement, you want to create separate settlement documents for the involved company codes whereas for the determination of the scale level of the rebate condition the business volume from all company codes is considered.

This business objective is achieved with a two-step settlement procedure. In the first step, you create a parked settlement document for which the company code is an additional item split criterion. For the second step, the creation of the collective settlement document, the company code is configured as a header split criterion so that actually the parked settlement document is split by company code. As usual for the collective settlement document, the transfer to accounting now happens for each company code separately. When you perform the second step for parked settlement documents from different rebate agreements, the system combines the parts for a certain company code into the collective settlement document as described in chapter Sales Rebate Processing - Two-Step Settlement.

This two-step procedure can also be applied to the multiple customer process variant in the following way: similar to the company code, the customer is an additional split criterion on item level for the parked settlement document in the first step and also a header split criterion for the creation of the collective settlement document. This means, you now split the parked settlement document by company code and customer.

Taking furthermore into account the differentiation between sales rebate as a service and goods related sales rebate, the following four condition contract types are provided:

- Condition contract type 0S05 Sales Rebate - MultOrgData 2Step for sales rebate as a service and business volume for a customer generated in different company codes.
- Condition contract type 0S06 Sales Rebate - MultCustomersOrg- 2Step for sales rebate as a service and business volume for multiple customers generated in different company codes.
- Condition contract type 0SG5 Sales Rebate Goods Rel MultOrg - 2Step for goods related sales rebate and business volume for a customer generated in different company codes.
- Condition contract type 0SG6 Sales Rebate GoodsRel MultCustOrg- 2Step for goods related sales rebate and business volume for multiple customers generated in different company codes.

Prerequisite

You have activated desired condition contract types for this process variant as described in chapter Activate Condition Contract Types (Optional).

#### Create Condition Contracts

Please refer to chapter [Create Condition Contract](#unique_8) [page ] 59 for the basic processing variant to create the condition contract. Data entry for condition contract types 0S05, 0S06, 0SG5, and 0SG6 is similar to condition contract types for the usual two-step settlement process variant, that are 0S03, 0S04, 0SG3, and 0SG4 respectively.

#### Check Business Volume

As described for the basic processing variant, also check the business volume in this test procedure before you start a settlement run to enable a control of the business volume determined for a settlement document.

Please follow process steps of [Check Business Volume (Optional)](#unique_30) [page ] 63.

Verify that the company code and sales area are applied as split criteria for condition contracts with condition contract types 0S05 or 0SG5, and company code, sales area, and customer for condition contracts with condition contract types 0S06 or 0SG6.

#### Create Settlement Documents

You perform the delta accruals settlement, partial settlement, and final settlement as described in corresponding chapters for the basic processing variant.

#### Check Settlement Documents

Check the parked settlement document for delta accruals settlement, partial settlement, and final settlement as described in corresponding chapters of the basic processing variant with view on the following specifics.

When checking the FI posting status, verify that – in contrast to the usual two-step settlement process variant – the settlement document for delta accruals is also a parked settlement document. Posting of accruals happens with the collective settlement document in the second step for the different company codes.

Verify that the company code and sales area are applied as split criteria for condition contracts with condition contract types 0S05 or 0SG5, and company code, sales area, and customer for condition contracts with condition contract types 0S06 or 0SG6.

When checking pricing for items in parked settlement documents for partial settlement, and final settlement, note that the system does not perform a taxation. Taxation happens with the collective settlement document in the second step according to taxation settings for the different company codes.

When displaying the document flow, check that the parked settlement documents for delta accruals, partial settlement, and final settlement are displayed as follow-on document of the condition contract.

Note that there are no output items for parked settlement document for partial and final settlement.

#### Collect Parked Settlement Documents

Perform the creation of collective settlement documents for parked settlement documents from delta accruals, partial settlement and final settlement using the Collect Settlement Documents app as described for the usual two-step settlement process variant.

#### Check Collective Settlement Documents

Check the collective settlement documents for delta accruals settlement, partial settlement, and final settlement similar to the check for parked settlement documents.

Verify that the system has created separate collective settlement documents for different company codes and sales areas, and additionally for different customers in case of conditions contracts with condition contract type 0S06 or 0SG6. For this check, you can use the document flow display on settlement document header level for parked settlement documents in combination with the journal entry display for collective settlement documents. In the Document Flow display of the collective settlement document, choose Expand or Expand all Entries to display the preceding parked settlement document and then Expand all Entries for the parked settlement document.

When checking pricing for items in collective settlement documents for partial and final settlement, control that the system has performed taxation according to settings for the different company codes.

Check that the usual output items are available for collective settlement documents for partial and final settlement.

### Sales Rebate Processing with Approval Workflow

For all process variants described in previous chapters, you can configure an approval workflow for three events: release of a (newly created) condition contract, release a condition contract for settlement, release a settlement document to accounting.

In the following we describe the test procedure with workflow for the basic process variant.

#### Create Condition Contract

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In the following steps, we show how to create a Sales Rebate 0S01 condition contract with approval process active.

Prerequisite

As prerequisite for this process step, you have completed steps mentioned in preliminary steps for creating a process variant with approval process active and performed chapters for configuring approval workflow in Configure Approval Workflow (Optional).

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Internal Sales Representative. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Condition Contracts - Sales Rebates (F6739). | The Manage Condition Contracts - Sales Rebates screen displays. |  |
| 3 | Select Condition Contract Type | On the Manage Condition Contracts - Sales Rebates screen, choose Create.On the following Select Condition Contract Type pop-up window, select condition contract type:0S01 Sales Rebate |  |  |
| 4 | Enter Contract Details | On the Create Sales Rebate screen, make the following entries and choose Enter:Customer: 33100003From: for example, <today's date>To: for example, <end of current year> |  |  |
| 5 | Enter Process Variant | On the Basic Data tab, make the following entries and choose Enter:Process Variant: ZS01 Sales Rebate with Workflow |  |  |
| 6 | Enter Sales Data | On the Sales tab, make and check the following entries:Sales Organization: 3310Distribution Channel: 10Division: 00Sales Office: 330Note This is a mandatory field to be input or there will be no accounting document created with business place missing when doing settlement |  |  |
| 7 | Enter Header Text | On the Header Texts tab, make and check the following entries:Text Type: Text for Settlement DocumentLanguage: EnglishChoose Create Header Text and enter the header text. | The header text will be shown in the corresponding settlement documents.Note Choose language German if communication language of business partner is German. If the language of the text box deviates from the communication language of the business partner then the header text will not appear in the output form. |  |
| 8 | Enter Business Volume Selection Criteria | On the Business Volume Selection Criteria tab, select New Line.Make the following entries and choose Enter.Field Combination: 0001 CustomerInclusion Indicator (Incl/Excl): InclusiveCustomer: 33100003Select New Line.Make the following entries and choose Enter.Field Combination: 0009 MaterialInclusion Indicator (Incl/Excl): InclusiveMaterial: TG11Optionally, you can also limit the business volume to certain customers using field combination 0001 Customer.Note In case you processed the steps from Prepare Transactional Data (Optional) chapter, enter the customer number you used to create the sales order here. |  |  |
| 9 | Check / Enter Settlement Data | On the Settlement Data tab, make the following entries and choose Enter.Settlement Material: TG11Settlement Type Customer: As Accounts ReceivableNote The settlement material is optional. The settlement material is only needed if no business volume is available or no invoice documents are created for a defined settlement date. |  |  |
| 10 | Enter Settlement Calendar | On the Settlement Calendar tab, select New Line.Make the following entries and choose Enter.Settlement Date: for example, <end of current year>Settlement Date Type: Final SettlementSelect New Line.Make the following entries and choose Enter.Settlement Date: for example, <tomorrow's date>Settlement Date Type: Partial SettlementSelect New Line.Make the following entries and choose Enter.Settlement Date: for example, <today's date>Settlement Date Type: Delta AccrualsNote The creation of the line with Settlement Date Type: Delta Accruals is optional.The creation of the line with Settlement Date Type: Partial Settlement is optional. |  |  |
| 11 | Enter Condition Record for Rebate | In the Conditions area, select the following entry:Condition Table: Condition ContractSelect New Condition.Make the following entries and choose Enter.Condition Type: RES1 RebateCalculation Type: for example, PercentageCondition Rate: for example, <1>Valid From: for example, <today's date>Valid To: for example, <end of current year>Scale Base Type: Value scaleNote This condition is used to calculate the base volume for payment value scale.In case the Valid From date and the Valid To date are already there, you can check and change it. |  |  |
| 12 | Enter Scale Data | Select the condition line.Choose New Scale Level.Make the following entries and choose Enter.Scales: for example, <1000>Unit: AEDCondition Rate: for example, <1%>Select the first created condition line.Choose New Scale Level.Make the following entries and choose Enter.Scales: for example, <2000>Unit: AEDCondition Rate: for example, <2%> |  |  |
| 13 | Enter Condition Record for Accruals | In the Conditions area, select New Condition.Make the following entries and choose Enter.Condition Type: REA1 Rebate AccrualsCalculation Type: for example, PercentageCondition Rate: for example, <2>Valid From: for example, <today's date>Valid To: for example, <end of current year>Note This condition is used to calculate the amount for accruals.In case the Valid From date and the Valid To date are already there, you can check and change it. |  |  |
| 14 | Save Condition Contract | Choose Save.Make a note of the condition contract number: __________. |  |  |

#### Request Approval to Release Condition Contract

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this process step, you request a rebate condition contract for release.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Internal Sales Representative. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Condition Contracts - Sales Rebates (F6739). | The Manage Condition Contracts - Sales Rebates screen displays. |  |
| 3 | Request Release of Condition Contract | Find the condition contract that you want to put into approval for release process, and choose Change Condition Contract after clicking on condition contract number.Choose Menu > Edit > Request Approval .Choose Save. | On the Status tab page, the system displays the following system status entries:NewApproval RequestedNow the request to release the condition contract goes to Sales Manager's Inbox. |  |

#### Trigger Rework of Condition Contract (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this process step, you check the status of a rebate condition contract and trigger a rework of the condition contract as a Sales Manager.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Sales Manager. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open My Inbox - All Items (F0862). | The My Inbox screen displays. |  |
| 3 | Display the Relevant Condition Contract | Find the condition contract that Internal Sales Representative has just requested for release: Release Condition Contract XXXXXXXXXXX. | The details of the condition contract display on the right of the screen. |  |
| 4 | Check Condition Contract Data and Send Back for Rework | Check the Settlement Lock Status and Status of the condition contract.Now the settlement lock status is Not Locked and the status is New.As the Internal Sales Representative has not set the status to Locked for Settlement, click Rework.On the Submit Decision pop-up window, enter a decision note: for example, please set the condition contract to Locked for Settlement.Choose Submit. | The condition contract is sent back to Internal Sales Representative. |  |

#### Rework Condition Contract (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this process step, you rework on a rebate condition contract in order to set the status to Locked for Settlement.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Internal Sales Representative. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open My Inbox - All Items (F0862). | The My Inbox screen displays. |  |
| 3 | Check the Condition Contract and Go to Change Mode | Open the notification: Rework Condition Contract XXXXXXXXXXX.Choose Show Details at the bottom and check the comments on the right side of the screen. Under the Comments tab, there is a message from the Sales Manager: please set the condition contract to Locked for Settlement.Choose Hide Details at the bottom and choose More Details on the upper right of the screen.On the Display Sales Rebate screen, choose Menu > Condition Contract > Change. | You check the comment from the Sales Manager and go to the change mode for condition contract. |  |
| 4 | Set Condition Contract to Locked for Settlement | On the Change Sales Rebate screen, choose Menu > Edit > Lock Settlement.Choose Save.Choose Continue in the pop-up window. | The settlement lock status is changed to Locked and the status for condition contract is New. |  |
| 5 | Complete Rework for the Condition Contract | Choose Rework Completed at the bottom.On the Submit Decision pop-up window, enter a decision note: for example, the condition contract is set to Locked for Settlement.Choose Submit. | The condition contract is sent to Sales Manager for release approval again. |  |

#### Release Condition Contract

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this process step, you release a rebate condition contract in an approval workflow.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Sales Manager. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open My Inbox - All Items (F0862). | The My Inbox screen displays. |  |
| 3 | Release Condition Contract | Find the condition contract that Internal Sales Representative has just requested for release: Release Condition Contract XXXXXXXXXXX.Choose Release at the bottom.Choose Submit in the pop-up window. | The condition contract is released now. |  |

#### Delta Accruals Settlement (Optional)

Please follow process steps in Delta Accruals Settlement (Optional) in section Sales Rebate Processing – One Customer.

On the selection screen, enter the different condition contracts belonging to this test.

After you have processed the delta accruals settlement you can optionally check the created settlement documents as described in chapter Check Settlement Document for Delta Accruals Settlement (Optional) in section Sales Rebate Processing – One Customer.

#### Request Release of Condition Contract for Settlement

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this process step, you request an approval for the settlement of a condition contract.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Internal Sales Representative. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Condition Contracts - Sales Rebates (F6739). | The Manage Condition Contracts - Sales Rebates screen displays. |  |
| 3 | Send Condition Contract for Release of Settlement | Find the condition contract for which you want to request the approval to release it for settlement. Choose Change Condition Contract via More Links when choosing condition contract number.Click Menu > Edit > Request Settlement Approval .Choose Save.Note Please click Menu > Edit > Lock Settlement before clicking Request Settlement Approval if you haven't executed steps in chapter Rework Condition Contract (Optional). | The status for condition contract now should be:ReleasedLocked for SettlementSettlement Approval Requested |  |

#### Release Condition Contract for Settlement

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this process step, you release a rebate condition contract for settlement.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Sales Manager. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open My Inbox - All Items (F0862). | The My Inbox screen displays. |  |
| 3 | Release Condition Contract for Settlement | Find the condition contract for that Internal Sales Representative has just requested for release for settlement.Position the notification: Release Condition Contract XXXXXXXXXXX for Settlement in the inbox.Choose Release.Choose Submit in the pop-up window. | The condition contract is released now for settlement. |  |

#### Partial Settlement (Optional)

Please follow process steps in Partial Settlement in section Sales Rebate Processing – One Customer.

#### Approve Release of Partial Settlement Document to Accounting (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this process step, you approve the release of the settlement document - created in partial settlement - to Accounting.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Sales Manager. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open My Inbox - All Items (F0862). | The My Inbox screen displays. |  |
| 3 | Approve Release to Accounting | Find the settlement document for which the release to accounting has to be approved. The approval request was triggered automatically after the settlement has been processed by the Billing Clerk.Position the notification: Approve Settlement XXXXXXXXXXX in the inbox.Choose Approve.Choose Submit in the dialog box. | The settlement document is released to accounting. |  |

#### Final Settlement

Please follow process steps in Final Settlement in section Sales Rebate Processing – One Customer.

#### Approve Release of Final Settlement Document to Accounting

Purpose

In this process step, you approve the release of the settlement document - created in final settlement - to Accounting.

Procedure

Process the steps described in the chapter [Approve Release of Partial Settlement Document to Accounting (Optional)](#unique_63) [page ] 97.

### Sales Rebate Processing with Different Bases for Rebate Calculation and Scale Determination

This section describes different bases for rebate calculation and scale determination using materials selection as an example.

When multiple materials are involved in the business volume selection criteria, the selection group specified for each material will determine the involvement of business volume of the material in either scale determination, rebate determination, or both.

The following is a detailed example.

Example:

Consider there being 4 materials M1, M2, M3 and M4.

Business Volume is to be determined from Materials M1, M2, M3, M4 for deriving the scale for rebate, but rebate is applicable only for M1, M2, M3.

Scales:

- If Business Volume > 20000, rebate rate = 2%
- If Business Volume > 30000, rebate rate = 3%

At the time of Settlement:

- Total Sales = $ 31,000

=> Rebate Scale = 3%

- Total Sales excl M4 = $ 27,000

Rebate = $ 27,000 x 3% = $ 810

Based on this example, during the condition contract creation, you will have to set the Selection Group for M1, M2 and M3 as blank, while for M4, you would need to set it as 0SSB.

In the following, we explain how to create the condition contract using the process variant ZS09 described in chapter Define Process Variant for Different Bases for Rebate Calculation and Scale Determination to specify different bases for rebate calculation and scale determination. The test procedure is very similar to the basic process variant, so we only describe the differences to the basic scenario.

#### Create Condition Contract

Please refer to the step Create Condition Contract in the section Sales Rebate Processing – One Customer, except for the following differences:

1. Process Variant.

In step 5, choose Process Variant ZS09.

1. Business Volume Base.

In step 8, add the following before the entry for Material: TG11.

-
    - Selection Group: 0SSB Scale Base

Select New Line. Make the following entries and choose Enter.

-
    - Field Combination: 0009 Material
    - Inclusion Indicator (Incl/Excl): Inclusive
    - Selection Group: Blank
    - Material: TG12

|  |
| --- |
| Note With regards to the business volume corresponding to each selection criterion,Selection Group: Blank => Relevant for both rebate and scale determinationSelection Group: 0SRB => Relevant for rebate onlySelection Group: 0SSB => Relevant for scale determination only |

All the other steps, such as checking business volume and carrying out settlement, remain the same as explained in the section Sales Rebate Processing – One Customer.

### Sales Rebate Processing with Graduated Scales

The default calculation of the scales that are set up in the condition table in condition contracts works like volume pricing. This means that on the execution of settlements, the application would apply the rate of the tier that it finds when looking for the business volume, on the entire amount and not only the delta amount:

If you set up the conditions as for example:

| Business Volume | Rebate Percentage |
| --- | --- |
| (From) 1,000 EUR | 10% |
| (From) 6,000 EUR | 20% |
| (From) 10,000 EUR | 30% |

Then the settlement run would calculate the rebates as follows:

| Business Volume found at the time of settlement | Total Effective Rebate at the time of settlement |
| --- | --- |
| 999 EUR | 0 EUR |
| 6,000 EUR | 1,200 EUR |
| 11,000 EUR | 3,300 EUR |

However, if you would like to set up graduated scales that work like tiered pricing instead of volume pricing, then you need to set up the condition contract slightly differently.

Follow the steps as in the chapter [Create Condition Contract](#unique_8) [page ] 59. In step 9, choose the value of the field Settlement Calculation Method as Graduated-To-Scale. Then in step 12, maintain the scales with scale type as To-scale.

Thereafter, if you set up the conditions as for example:

| Business Volume | Rebate Percentage |
| --- | --- |
| (To-scale) 1,000 EUR | 0% |
| (To-scale) 5,000 EUR | 10% |
| (To-scale) 11,000 EUR | 20% |
| (To-scale) 999,999 EUR | 30% |

Then the settlement run would calculate the rebates as follows:

| Business Volume found at the time of settlement | Total Effective Rebate at the time of settlement |
| --- | --- |
| 1,000 EUR | 0 EUR |
| 5,000 EUR | 400 EUR |
| 11,000 EUR | 1,600 EUR (= 400 EUR +1,200 EUR) |

In the example above, the calculation works in the following manner.

When business volume is found to be 1,000 EUR, then the first tier with 0% rebate is applicable. Hence, the rebate is 0 EUR.

When business volume is found to be 5,000 EUR, then the second condition rate with 10% rebate is applicable on the difference of business volumes between the first and second scales. Hence, the rebate is calculated as 400 EUR.

When business volume is found to be 11,000 EUR, then three condition rates would be applicable. This means that the rebate would be calculated at the rate of 0% for 1,000 EUR, 10% for 4,000 EUR and 20% for the remaining 6,000 EUR, resulting in 0, 400 and 1,200 EUR, respectively. Hence, the total rebate value comes to 1,600 EUR.

### Sales Rebate Processing with Conditions Maintained for Product Hierarchy Nodes

In condition contracts, another condition table V 4CV Condition Contract/Product Hierarchy enables you to maintain different condition rates for several product hierarchy nodes in a single contract for sales rebate.

One good practice is to include the same hierarchy nodes also in the business volume selection criteria, to make the selection of transactional documents as precise as possible. By doing this, you will see the business volumes only for those products which are part of the hierarchy nodes in your condition tables and subsequently, the products which were not part of the hierarchy will not be considered during the settlement run. If you don’t maintain the condition contract in this manner, then even the products which are not part of the hierarchy will be part of the settlement but with 0 values, because no condition rate will be found for them, unless you have maintained conditions for those products additionally.

Please note that you will need to select the sub-nodes of the product hierarchy and not the root node, in the condition maintenance.

Follow the steps as in the chapter [Create Condition Contract](#unique_8) [page ] 59. In step 5, enter process variant ZS10 Activate Condition for Product Hierarchy as explained in chapter [Define Process Variant to Activate Condition Table for Product Hierarchy](#unique_21) [page ] 38. Then in step 11, select V 4CV Condition Contract/Product Hierarchy in the condition table dropdown and maintain the condition lines for the product hierarchy nodes as you need.

Split Criterion Usage in Process Variant

If your business need is to consider the product hierarchy information stored in the transactional data during the lifetime of the condition contract, even if the product hierarchy has been modified during that period, then in the process variant you should set the product hierarchy as a split criterion and include the same hierarchy nodes also in the business volume selection criteria. The impact of this is explained with an example below.

Product Hierarchy

| Hierarchy Node | Type | Product | Valid From | Valid To |
| --- | --- | --- | --- | --- |
| PH1 | Root |  | January 1st of the current year | December 31st of the current year |
| PH1-1 | Sub-node |  |  |  |
|  |  | TG11 |  |  |
|  |  | TG12 |  |  |
| PH1-2 | Sub-node |  |  |  |
|  |  | TG15 |  |  |

In this example, let's assume that on the March 31st of the current year, product TG11 is removed from the hierarchy.

Condition Contract Validity – January 1st of the current year – December 31st of the current year

Condition Rate – 10% for PH1-1

Partial Settlement Date – October 30th of the current year

The billing documents generated for the period January 1st of the current year to March 31st of the current year for product TG11, will include the hierarchy information PH1-1. The ones generated after that time, will not include the hierarchy information in them. At the time of settlement, the application will look at the data maintained in the billing documents and the ones having the hierarchy node in them will be considered for the business volume.

However, if your business need is to consider the product hierarchy only as it is at the time of settlement, then you should not set the split criterion for product hierarchy in the process variant. In that case, for the same example above, at the time of settlement, the application will find that TG11 is not part of the sub-node PH1-1 and therefore, it will not consider the business volume from the billing documents for TG11. But please note that if you have added new products to the hierarchy after the billing documents had been generated, then those billing documents will not have the information of the hierarchy stored in them and hence, will not be considered.

### Sales Rebate Processing Using Service Rendered Date for Business Volume Selection

In the standard scenario, the system uses the billing date to determine the business volume and the corresponding rates for settlement. However, there are some business scenarios where the business volume impacted by subsequent debit or credit memos (for example, price corrections or customer returns) needs to be considered for the same period as the original sales. One example of such a scenario is when rates vary across multiple periods within a condition contract’s validity duration. To handle these scenarios, you can use the service rendered date for business volume selection instead of the standard billing date, provided that the service rendered date of the subsequent billing document is the same as the service rendered date of the original billing document. This ensures that subsequent billing documents are processed using the rate from the original transaction period.

Example

Consider an agreement with different monthly rates. If you use the billing date:

| Transaction | Period | Amount | Rate | Calculation | Settlement Amount |
| --- | --- | --- | --- | --- | --- |
| Sale | January | $ 100 | 10% | $ 100 * 10% | $ 10 |
| Return | March | -$ 50 | 15% | -$ 50 * 15% | -$ 7.5 |

The business volume for the return is considered at 15%, which is higher than the 10% rate granted in January prior to the return.

If you use the service rendered date:

| Transaction | Period | Amount | Rate | Calculation | Settlement Amount |
| --- | --- | --- | --- | --- | --- |
| Sale | January | $ 100 | 10% | $ 100 * 10% | $ 10 |
| Return | March | -$ 50 | 15% | -$ 50 * 10% (January) | -$ 5 |

The business volume for the return is considered at the January rate of 10%, reflecting the rate originally granted.

To enable this feature, follow the steps described in the chapter [Create Condition Contract](#unique_8) [page ] 59 with the following differences:

- In step 5, choose Process Variant ZS11 as explained in chapter [Define Process Variant to Activate Business Volume Selection by Service Rendered Date](#unique_22) [page ] 41.
- In step 13, select condition type REAA Rebate Accruals.

|  |
| --- |
| Caution In case of returns, the service rendered date can differ based on the type of return. For further details about how the service rendered date is filled, consult your Sales and Distribution experts. |

|  |
| --- |
| Note If you have different rates for different periods, then you need to create the settlement calendar with Final Settlement dates for each period for those rates to be correctly applied. Using the service rendered date for business volume selection can cause subsequent billing documents posted after a contract's final settlement to be excluded from settlement. For example, if the original billing document is created in December, final settlement runs in January, and a subsequent billing document is posted in February with a service rendered date in December, the subsequent billing document may not be considered in the final settlement because the contract has already been settled. To capture such late billing documents, you can use delta settlements in subsequent settlement runs. |

### Final Settlement with Adjustments (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this process step, you enter conditions in the condition contract to adjust the final rebate amount before you process the final settlement.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log onto SAP Fiori Launchpad | Log onto the SAP Fiori Launchpad as an Internal Sales Representative. | The SAP Fiori Launchpad displays. |  |
| 2 | Access the App | Open Manage Condition Contracts - Sales Rebates (F6739). | The Manage Condition Contracts - Sales Rebates screen displays. |  |
| 3 | Create New Condition Contract | On the Manage Condition Contracts - Sales Rebates screen, select the relevant condition contract and choose Change Contract. | The Select Condition Contract Type dialog screen displays. |  |
| 4 | Enter Condition Data for Rebate Condition | In the Conditions Area, select the following entry:Condition Table: Condition ContractSelect New Condition.Make one of the following entries and choose Enter.Adjustment of business volumeCondition Type: REBD Rebate BusVol DeltaValid From: for example, <today's date>Valid to: for example, <end of current year>Calculation Type: Fixed amountCondition Rate: for example, <100> AEDAdjustment of rebate valueCondition Type: REJ1 Rebate AdjustmentValid From: for example, <today's date>Valid to: for example, <end of current year>Calculation Type: for example, Fixed amountCondition Rate: for example, <20> AEDEntry of a fixed settlement amountCondition Type: REV1 Rebate VerifiedValid From: for example, <today's date>Valid to: for example, <end of current year>Calculation Type: for example, Fixed amountCondition Rate: for example, <1000> AEDThe conditions entered here are used to adjust the rebate amount. You can also choose Condition Contract / Material as condition level. You then also specify the material for a condition record. In case the Valid From and Valid To date are copied from the condition contract validity according to user settings, you can check and change these dates if necessary. | The conditions entered here are used to adjust the rebate amount.You can also choose Condition Contract / Material as condition level. You then also specify the material for a condition record.If the Valid From and Valid To date is copied from the condition contract validity according to user settings, you can check and change these dates if required. |  |
| 5 | Save Condition Contract | Choose Save. |  |  |

After you have maintained the conditions to adjust the rebate amount, you perform the final settlement as described in the chapter Final Settlement in section Sales Rebate Processing – One Customer. Then check the created settlement document as described in Check Settlement Document for Final Settlement (Optional) in section Sales Rebate Processing – One Customer. In the pricing elements, particularly check that the system has determined the rebate amount using the conditions for adjustment.

### Rebate Unlikelihood (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

During the creation of the condition contract (Chapter Create Condition Contract) when entering the conditions, you have the option to use the condition: rebate unlikelihood. You use condition type rebate unlikelihood in case the minimum sales turnover will not be reached and therefore no accruals should be created or existing accruals should be reversed.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Enter Condition Data (Optional) | In the Conditions area, select New Condition.Make the following entries and choose Enter.Condition Type: REU1 Rebate UnlikelihoodCondition Rate: for example, <100%>Valid From: for example, <today's date>Valid To: for example, <end of current year> |  |  |

### Sales Rebate Processing – Fixed Amount Agreements

This section deals with fixed amount agreements as a special process variant for sales rebate processing. The characteristic feature for this sales rebate process variant is that you enter a fixed amount for the rebate condition in the condition contract. You can again distinguish several scenarios which we describe in the following subchapters.

In the basic scenario, you just enter one or several fixed amount(s) that you pay out to the customer with a final settlement. As for other sales rebate process variants, you can also perform a two-step settlement when there are several fixed amount agreements with a customer. When you want to distribute the fixed amount to the different fiscal periods within the condition contract validity, you schedule additional delta accruals settlement runs. This distribution can happen before or after the payout of the fixed amount. Additionally, you can also involve business volume data to distribute the fixed amount to business objects.

For the basic scenario and for the scenario with fixed amount distribution to fiscal periods, you use condition contract types 0SF1 Sales Rebate Fixed Amount and 0SF3 Sales Rebate Fixed Amount - 2Step. For the scenario with business volume data, you can use for instance condition contract type 0S01.

#### Basic Processing

Purpose

In this section, you execute the sales rebate process for fixed amount agreements. You first create the condition contract with one or several condition record(s) for fixed amounts. Then you run the corresponding final settlement(s).

Procedure

Enter a condition contract with one fixed amount condition record as follows:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Internal Sales Representative. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Condition Contracts - Sales Rebates (F6739). | The Manage Condition Contracts - Sales Rebates screen displays. |  |
| 3 | Select Condition Contract Type | On the Manage Condition Contracts - Sales Rebates screen, choose Create.On the following Select Condition Contract Type pop-up window, select condition contract type:0SF1 Sales Rebate Fixed Amount |  |  |
| 4 | Enter Contract Details | On the Create Sales Rebate Fixed Amount screen, make the following entries and choose Enter:Customer: 33100003From: for example, <today's date>To: for example, <end of current year> |  |  |
| 5 | Enter Process Variant | On the Basic Data tab, make the following entry and choose Enter:Process Variant: ZS06 Fixed Amount Agreement |  |  |
| 6 | Enter Sales Data | On the Sales tab, make and check the following entries:Sales Organization: 3310Distribution Channel: 10Division: 00Sales Office: 330Note This is a mandatory field to be input or there will be no accounting document created with business place missing when doing settlement |  |  |
| 7 | Enter Header Text | On the Header Texts tab, make and check the following entries:Text Type: Text for Settlement DocumentLanguage: EnglishChoose Create Header Text and enter the header text. | The header text will be shown in the corresponding settlement documents.Note Choose language German if communication language of business partner is German. If the language of the text box deviates from the communication language of the business partner then the header text will not appear in the output form. |  |
| 8 | Enter Settlement Data | On the Settlement Data tab, make the following entries and choose Enter:Settlement Material: TG11Settlement Type Customer: As Accounts Receivable |  |  |
| 9 | Enter Settlement Calendar | On the Settlement Calendar tab, select New Line.Make the following entries and choose Enter.Settlement Date: for example, <end of current year>Settlement Date Type: Final Settlement |  |  |
| 10 | Enter Condition Record for Rebate | In the Conditions area, select the following entry:Condition Table: Condition ContractSelect New Condition.Make the following entries and choose Enter.Condition Type: RES1 RebateCalculation Type: Fixed AmountCondition Rate: <any amount>Condition Currency: <any currency, best company code currency>Valid From: for example, <today's date>Valid To: for example, <end of validity period> |  |  |
| 11 | Release Condition Contract | Choose Release. |  |  |
| 12 | Save Condition Contract | Choose Save.Make a note of the condition contract number: __________. |  |  |

To create a condition contract with several fixed amount condition records, you must align the settlement dates in the settlement calendar with the validity period of condition records. If you want to pay out a fixed amount at the end of January and end of February, create corresponding settlement dates for final settlement in the settlement calendar and conditions record with a validity Jan 1st – Jan 31st and Feb 1st – Feb 28th.

After you have maintained the condition contract, you perform the final settlement(s) as described in the chapter Final Settlement in section Sales Rebate Processing – One Customer. Then check the created settlement document as described in Check Settlement Document for Final Settlement (Optional) in section Sales Rebate Processing – One Customer. In the pricing elements, particularly check that the system has determined the fixed rebate amount.

When you test the process variant with two-step settlement, prepare at least two condition contracts as described, perform the final settlement, check the parked settlement documents, create the collective settlement document as described in the chapter Collect Parked Settlement Documents from Final Settlement in section Sales Rebate Processing – Two-Step Settlement, and then check the collective settlement document.

#### Cost Recognition for Fiscal Periods

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this section, you execute the sales rebate process for fixed amount agreements in combination with a cost recognition of the fixed amount for the different fiscal periods within the condition contract validity. For this cost recognition adjustment, you schedule an additional delta accruals settlement run for each fiscal period.

In a first process variant, we describe a cost recognition adjustment before the payout of the fixed amount. Here the accruals amount is successively built up with the delta accruals settlements. For the test we have chosen data that make settlement postings comprehensible. Afterwards, we describe a distribution subsequent to an immediate payout. Here, the fixed amount is used to activate a positive accruals amount reflecting a claim. In the following delta accruals settlements, you reduce the accruals amount and assign the monthly share to the sales rebate P/L account.

Procedure Variant 1

Enter a condition contract with one fixed amount condition record as described in the previous section. The validity of the condition contract is one year starting on the first day of the current month and ending on the last day of the previous month in the next year. The fixed amount is 1200 AED.

In the settlement calendar, enter additional 12 settlement dates for delta accruals settlement for each month’s end within the condition contract validity. That means the first delta accruals settlement is at the end of the current month, the last coincides with the final settlement date at the end of the condition contract validity.

Perform the delta accruals settlements for each settlement date and check the created settlement documents as described in section Sales Rebate Processing – One Customer. Be aware that the correct cost recognition adjustment for fiscal periods only happens when the delta accruals settlement runs at the specified settlement date. However, this procedure is required to illustrate the settlement postings.

First, check the accounting document related to a delta accruals settlement document. You will see that the accruals amount is 100 AED for each month. Then check the pricing for the settlement document items. You see, that condition type REBV Rebate Business Vol. does not appear as business volume determination does not play a role for condition contract type 0SF1 (and 0SF3). The initial accruals amount 1200 AED set by condition type RES1 corresponds to the entered fixed amount. In the next line, you see condition type RED5 Cost Recogn. Adjust which controls the cost recognition adjustment. In the first settlement document the initial accruals amount 1200 is reduced by 11/12 (= 1100 AED), in the second settlement document by 10/12 (= 1000 AED) and so on. In the last settlement document the amount for RED5 is zero. Starting with the second settlement document you also see the already posted accruals amount in the line of condition type RED2 Rebate Accr Total which further reduces the actual accruals amount in the calculation. In the second settlement document this amount is 100 AED, in the third settlement document 200 AED and so on. As a result of the calculation the amount for each delta accruals settlement is 100 AED. When you check the settlement document of the final settlement, you see a revenue posting for the customer with the fixed amount increased by the corresponding tax and the reversal of the total accruals amount of 1200 AED.

Procedure Variant 2

Enter a condition contract with one fixed amount condition record as described in the previous section. The validity of the condition contract is one year starting on the first day of the current month and ending on the last day of the previous month in the next year. The fixed amount is 1200 AED.

In the settlement calendar, enter additional 12 settlement dates for delta accruals settlement for each month’s end within the condition contract validity. That means the first delta accruals settlement is at the end of the current month, the last coincides with the final settlement date at the end of the condition contract validity. Additionally, enter a partial settlement within the current month for instance for the current day.

Perform the partial settlement and then the delta accruals settlements and check the created settlement documents as described in section Sales Rebate Processing – One Customer. Be aware that the correct cost recognition adjustment for fiscal periods only happens when the delta accruals settlement runs at the specified settlement date. However, this procedure is required to illustrate the settlement postings.

First, check the settlement document for the partial settlement. In the pricing elements of the item, you see the fixed amount 1200 AED as rebate for condition type RES1 Rebate in the first line of the pricing procedure. In the line with condition type for Rebate Tax, you calculate the corresponding VAT tax. The following line shows the resulting gross amount. Relevant for the cost recognition adjustment in this document is the line for condition type REA5 Rebate AccrualsSettl which shows the fixed amount with a negative sign similar to an accruals reversal. Now check the accounting document. First, you see the usual posting for a partial settlement, the credit entry for the customer for the gross amount and debit entries for the fixed amount (net value) on the Sales Rebate P/L account and the output tax on the corresponding tax account. In the following lines you see the consequence of the negative value for condition type REA5 from the pricing elements. You see a credit posting for the Sales Rebate P/L account and a debit posting for the Accrd Volume Rebate accruals account. This is typical for a ‘payment first, cost activation later’ scenario. These lines balance the cost account – which is the Sales Rebate P/L account in this case – and transfer the costs to a clearing account, i.e. the Accrd Volume Rebate accruals account. With the following delta accruals settlements, you reduce the proportionate amount on the clearing account and activate (transfer back) the costs on the P/L account.

Now, check the settlement documents for the delta accruals settlement to control this cost activation. First, you see that the settlement amount for each month is 100 AED. When you look at the pricing elements, you see how this net amount is derived from the fixed amount for condition type RES1, a negative amount for condition type RED5 Cost Recogn. Adjust controlling the cost recognition adjustment, the negative fixed amount for condition type RES2 Rebate PartSettl Rev representing the partial settlement reversal, and the – now positive – amount for the condition type RED2 Rebate Accr Total for posted accruals. The (absolute) amount for RED5 and RED2 is decreased by 100 AED month by month. In the accounting document for a delta accruals settlement document, you see the cost activation by a debit entry for the Sales Rebate P/L account and a credit posting for the Accrd Volume Rebate accruals account. The final settlement has a settlement amount of zero, it only locks the condition contract.

#### Fixed Amount Settlement Proportionally Across Fiscal Periods

For condition contract types 0SF1 Sales Rebate Fixed Amount and 0SF3 Sales Rebate Fixed Amount - 2Step, the default behavior is that a condition contract with a fixed amount is settled in a manner where the total allocation is settled upon the first partial settlement, regardless of the delta accrual distribution across periods.

To ensure that the fixed amount is distributed across partial settlements, make sure that you complete the step 8 in the [Define Process Variant to Configure Settings for Fixed Amount Agreements](#unique_11) [page ] 27 before using the process variant ZS06 Fixed Amount Agreement in the condition contract.

Example

A condition contract has a fixed amount of 12,000 AED. Settlement dates include monthly delta accruals of 1,000 AED and quarterly partial settlements. During the settlement run, the default partial settlement for March would be 12,000 AED. However, if you use the defined process variant for the condition contract, the partial settlement for March would be 3,000 AED.

The table below provides a detailed comparison of the calculations for the two methods:

| Default | Process Variant Used |
| --- | --- |
| Delta accruals for January = 1,000 AED | Delta accruals for January = 1,000 AED |
| Delta accruals for February = 2,000 – 1,000 = 1,000 AED | Delta accruals for February = 2,000 – 1,000 = 1,000 AED |
| Delta accruals for March = 3,000 – 2,000 = 1,000 AED | Delta accruals for March = 3,000 – 2,000 = 1,000 AED |
| Partial settlement for March = 12,000 AED | Partial settlement for March = 1,000 * 3 = 3,000 AED |
| Accruals released = 3,000 AED | Accruals released = 3,000 AED |

#### Fixed Amount Distribution to Business Objects

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this section, you execute the sales rebate process for fixed amount agreements in combination with the assignment of the fixed amount to business objects according to their contribution to the overall business volume.

Prerequisite

We recommend preparing transactional in a way that the assignment becomes comprehensible. For instance, prepare business volume of two material with a 2:1 relationship. In the condition contract, enter business volume selection criteria accordingly and use a fixed amount that can be divided by 3.

Procedure

Use condition contract type 0S01 to enter a condition contract with one fixed amount condition record as described in the section Basic Processing. In addition, specify business volume selection criteria.

Perform the final settlement and check the created settlement document. Control that the fixed rebate amount has been distributed to the settlement document items according to the contribution of each item to the overall business volume. When you have prepared business volume data according to the recommendation above, you see two items in the settlement document with a rebate amount of 200 AED and 100 AED, respectively.

#### Fixed Amount Settlement on Multiple Products

Follow the steps described in the [Basic Processing](#unique_72) [page ] 106 chapter in the Sales Rebate Processing – Fixed Amount Agreements section.

To specify multiple products and the fixed amount for each of them, in step 10, you can select Condition Contract / Material in the Condition Table dropdown and maintain materials and the corresponding fixed amounts as you need.

If you do this, the settlement material maintained in the header will not be considered but will remain as a fallback.

### Reverse Settlement Document (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this process step, you reverse settlement document for the condition contract.

Prerequisite

You have processed the settlement run to the condition contract(s).

Procedure

The steps below are using Reverse Settlement Documents Condition Contracts (WB2R_CANCEL_DOCS) for reversing settlement documents for the selected condition contract(s). You can use Reverse Settlement Document (WZR4) to reverse a single settlement document. You can also use Reverse Settlement Documents (WAB_CANCEL_B) to reverse several settlement documents together.

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Billing Clerk. | The SAP Fiori launchpad displays. |  |
| 2 | Access Reverse Settlement Documents | Open Reverse Settlement Documents - Condition Contracts (WB2R_CANCEL_DOCS). | The Reverse Settlement Documents for Condition Contracts screen displays. |  |
| 3 | Reverse Settlement Documents for Condition Contracts | On the Reverse Settlement Documents for Condition Contracts screen, make the following entries:Condition Contract: <number of condition contract(s) created in this test>Check Run Only: <unselect this checkbox>Choose Execute.Choose Continue in the pop-up window. | The Log for Reversal of Settlement Documents - Live Run screen displays. All settlement documents for the selected condition contract(s) are reversed. |  |

## Follow-Up Processes

You have finished all the activities that are part of the business process described in this document.

To accomplish the subsequent activities of this business process, use the master data from this document and carry out the process steps described in one or more of the following scope items.

### Analytical Content: Order-to-Cash (Optional)

Purpose

This scope item describes the detailed procedure for testing the scope item Analytical Content: Order-to-Cash after solution activation.

Procedure

Using the reports from this document, complete all the activities described in the Test script of the scope item.

### General Ledger Reporting and CO-PA Reporting (Optional)

Purpose

After completing the activities in this test script, it is possible to run General Ledger Reporting and CO-PA Reporting connected with the accounts which were used in this sales rebate process. Log on as General Ledger Accountant or Sales Accountant and run the reports which apply to your needs and check the postings on your accounts. Please refer to scope item Accounting and Financial Close (J58) to Manage G/L Account Master Data and Manage Financial Statement Versions.

## Appendix

### Time-Dependent Tax

Purpose

With the new Time-Dependent Tax feature you can enter different tax rates for a tax code for different validity periods. So it is no longer necessary to introduce a new tax code when a tax rate is changed.

For more details concerning the activation of the Time-Dependent Tax feature and the maintenance of time dependent tax rates, see [Time-Dependent Taxes (TDT)](https://help.sap.com/docs/SAP_S4HANA_CLOUD/0fa84c9d9c634132b7c4abb9ffdd8f06/8fd78f3974b84e478dc99ae1ae1afc16.html).

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
- related-to :: [[08-sales-order-management/margin-optimization-sap-solution-extensions-by-vistex-7uq-test-script]]
- related-to :: [[08-sales-order-management/royalties-settlement-for-sales-55i-ae-test-script-sap-s-4hana-cloud-pu]]
- related-to :: [[08-sales-order-management/test-script-condition-contract-with-customer-hierarchy-consumer-produc]]
- related-to :: [[08-sales-order-management/test-script-sales-commissions-external-sales-representative-2tt-ae-863]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/1B6_S4CLD2608_BPD_EN_AE.docx` — full document · extracted with `mammoth` · 223,726 chars in the whole document
