---
id: 09-subscription-billing-and-contract-accounting/test-script-subscription-management-for-software-5sw-ae-sap-s-4hana-cl-part-01
title: "Test Script: Subscription Management for Software (5SW_AE) - SAP S/4HANA Cloud Public Edition 2608 (5SW_S4CLD2608_BPD_EN_AE) — part 1 of 2"
description: "Test script for scope item 5SW_AE: software subscription master data, solution orders, entitlements, provisioning, billing, revenue recognition, changes."
cluster: 09-subscription-billing-and-contract-accounting
tags: [kb/subscription-billing-and-contract-accounting, topic/subscription-product-master-data]
aliases: []
keywords: [Subscription Products and Rate Plans, subscription billing master data, rate elements, rate plan templates, subscription products, lookup tables, entitlement management setup, offering entitlement mapping, solution orders, provisioning responses]
sources: ["raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/5SW_S4CLD2608_BPD_EN_AE.docx#lines-1-3326"]
confidence: low
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-1122
topic: 09-subscription-billing-and-contract-accounting/subscription-product-master-data
language: EN
part: 1/2
created: 2026-10-12
updated: 2026-10-12
---

# Test Script: Subscription Management for Software (5SW_AE) - SAP S/4HANA Cloud Public Edition 2608 (5SW_S4CLD2608_BPD_EN_AE) — part 1 of 2

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/5SW_S4CLD2608_BPD_EN_AE.docx`, part 1 of 2 (lines 1–3326 of the extracted text), extracted with `mammoth`. Grouped under **Subscription Products and Rate Plans** in Subscription Billing and Contract Accounting. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

| <!-- image omitted: unnamed --> | Test ScriptSAP S/4HANA Cloud Public Edition - 19-06-26 |
| --- | --- |
|  | Subscription Management for Software (5SW_AE) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Table of Contents

[1 Purpose 5](#_Toc232857544)

[2 Prerequisites 6](#_Toc232857545)

[2.1 System Access 6](#_Toc232857546)

[2.2 Roles 6](#_Toc232857547)

[2.3 Master Data, Organizational Data, and Other Data 9](#_Toc232857548)

[2.4 Additional Manual Configuration 13](#_Toc232857549)

[2.5 Preliminary Steps 13](#_Toc232857550)

[2.5.1 Master Data Setup - SAP Subscription Billing 13](#_Toc232857551)

[2.5.1.1 Create Rate Elements 13](#_Toc232857552)

[2.5.1.2 Create Rate Plan Templates 16](#_Toc232857553)

[2.5.1.3 Create Product (SAP Subscription Billing) 22](#_Toc232857554)

[2.5.1.4 Create Lookup Table for Recurring Price Alternative 24](#_Toc232857555)

[2.5.1.5 Create Price Element Specification 25](#_Toc232857556)

[2.5.1.6 Addition of Price Element to Pricing Scheme 26](#_Toc232857557)

[2.5.1.7 Uploading Lookup Tables for Price Determination 27](#_Toc232857558)

[2.5.1.8 Replicate Business Partners from SAP S/4HANA Cloud Public Edition to SAP Subscription Billing 32](#_Toc232857559)

[2.5.1.9 Maintain Standard Master Agreement for Customer in SAP Subscription Billing 33](#_Toc232857560)

[2.5.2 Master Data Setup - SAP S/4HANA Cloud 34](#_Toc232857561)

[2.5.2.1 Maintain Product Groups in SAP S/4HANA Cloud Public Edition 34](#_Toc232857562)

[2.5.2.2 Maintain Master Data S/4HANA Cloud 36](#_Toc232857563)

[2.5.2.2.1 Enhance Subscription Billing Products 36](#_Toc232857564)

[2.5.2.2.2 Maintain Sales Prices for Revenue Split 38](#_Toc232857565)

[2.5.3 Master Data set up – SAP Entitlement Management 40](#_Toc232857566)

[2.5.3.1 Replicate Business Partner from SAP S/4HANA Cloud Public Edition to SAP Entitlement Management 40](#_Toc232857567)

[2.5.3.2 Mark Products in SAP S/4HANA Cloud Public Edition as “Relevant for Entitlement Generation” 41](#_Toc232857568)

[2.5.3.3 Replicate Products from SAP S/4HANA Cloud Public Edition to SAP Entitlement Management 42](#_Toc232857569)

[2.5.3.4 Maintain Offering – Entitlements Mapping for Entitlement Model Master Agreement 43](#_Toc232857570)

[2.5.3.5 Maintain Offering – Entitlements Mapping for Entitlement Model Tenant 44](#_Toc232857571)

[2.5.3.6 Maintain Offering – Entitlements Mapping for Entitlement Model Tenant Phase 45](#_Toc232857572)

[2.5.3.7 Maintain Offering – Entitlements Mapping for Entitlement Model License 46](#_Toc232857573)

[2.5.3.8 Maintain Specific Views for “Maintain Customer Entitlements” App 48](#_Toc232857574)

[2.5.4 Prepare SAP Business Accelerator Hub to test the SAP Entitlement Management Provisioning Response 51](#_Toc232857575)

[2.5.5 Prepare SoapUI to test the SAP Entitlement Management Provisioning Response (Optional) 53](#_Toc232857576)

[3 Overview Table 55](#_Toc232857577)

[4 Test Procedures 61](#_Toc232857578)

[4.1 Create Solution Order 61](#_Toc232857579)

[4.2 Manage Subscription Billing - Display Pending Subscription in SAP Subscription Billing 63](#_Toc232857580)

[4.3 Manage Entitlements - Display Entitlements in SAP Entitlement Management 65](#_Toc232857581)

[4.4 Entitlement Management 66](#_Toc232857582)

[4.4.1 Background Job to Trigger Provisioning 66](#_Toc232857583)

[4.4.2 Send Response for the Tenant Provisioning Requests 67](#_Toc232857584)

[4.4.3 Send Response for the License Provisioning Requests 69](#_Toc232857585)

[4.4.4 Check Event for Subscription Activation in SAP Entitlement Management 73](#_Toc232857586)

[4.4.5 Send Tenant Capability Update 74](#_Toc232857587)

[4.5 Enter License Consumption in SAP Entitlement Management 77](#_Toc232857588)

[4.6 Enter Software Usage and Adoption in SAP Entitlement Management 78](#_Toc232857589)

[4.7 Manage Subscription Billing 80](#_Toc232857590)

[4.7.1 Display Active Subscription in SAP Subscription Billing 80](#_Toc232857591)

[4.7.2 Display Provider Contract 82](#_Toc232857592)

[4.7.3 Monitor Revenue Recognition (Event-Based): Provider Contracts 83](#_Toc232857593)

[4.7.4 Manage Usage Records in SAP Subscription Billing 84](#_Toc232857594)

[4.7.5 Display Pre-Bill in SAP Subscription Billing 86](#_Toc232857595)

[4.8 Manage Billing Document in SAP S/4HANA Cloud 87](#_Toc232857596)

[4.8.1 Create Billing Document 87](#_Toc232857597)

[4.8.2 Display Billing Document 88](#_Toc232857598)

[4.8.3 Display Journal Entry Analyzer 89](#_Toc232857599)

[4.9 Manage Revenue Recognition 91](#_Toc232857600)

[4.9.1 Monitor Revenue Recognition (Event-Based): Provider Contracts 91](#_Toc232857601)

[4.9.2 Run Revenue Recognition: Provider Contracts (Period-End Activity) 92](#_Toc232857602)

[4.9.3 Manage Real-Time Revenue Recognition Issues – Provider Contracts 93](#_Toc232857603)

[4.10 Change Processes 94](#_Toc232857604)

[4.10.1 Separate CAD Subscription for a the Commercial Division of the Customer 94](#_Toc232857605)

[4.10.1.1 Create Solution Order 94](#_Toc232857606)

[4.10.1.2 Display Pending Subscription in SAP Subscription Billing 96](#_Toc232857607)

[4.10.1.3 Display Entitlements in SAP Entitlement Management 98](#_Toc232857608)

[4.10.1.4 Background Job to Trigger Provisioning 99](#_Toc232857609)

[4.10.1.5 Send Response for the Tenant Provisioning Requests 100](#_Toc232857610)

[4.10.1.6 Send Response for the License Provisioning Requests 104](#_Toc232857611)

[4.10.1.7 Display Active Subscription in SAP Subscription Billing 107](#_Toc232857612)

[4.10.1.8 Send Tenant Capability Update 109](#_Toc232857613)

[4.10.2 Change Subscription – Number of Users 112](#_Toc232857614)

[4.10.2.1 Change Number of Users in SAP Subscription Billing 112](#_Toc232857615)

[4.10.2.2 Display Entitlements in SAP Entitlement Management 113](#_Toc232857616)

[4.10.2.3 Background Job to Trigger Provisioning 113](#_Toc232857617)

[4.10.2.4 Send Response for the License Provisioning Requests 114](#_Toc232857618)

[4.10.3 Change Subscription – Extend Subscription Duration 117](#_Toc232857619)

[4.10.3.1 Extend Subscription End Date in SAP Subscription Billing 117](#_Toc232857620)

[4.10.3.2 Display Entitlements in SAP Entitlement Management 118](#_Toc232857621)

[4.10.3.3 Background Job to Trigger Provisioning 119](#_Toc232857622)

[4.10.3.4 Send Response for the License Provisioning Requests 120](#_Toc232857623)

[4.10.4 Add Additional Subscriptions for Users, Documents, Test Tenant, Trial CAD 3D 123](#_Toc232857624)

[4.10.4.1 Extend Solution Order with Additional Subscriptions 123](#_Toc232857625)

[4.10.4.2 Display Pending Subscriptions in SAP Subscription Billing 126](#_Toc232857626)

[4.10.4.3 Display Entitlements in SAP Entitlement Management 128](#_Toc232857627)

[4.10.4.4 Background Job to Trigger Provisioning 129](#_Toc232857628)

[4.10.4.5 Send Response for the Tenant Provisioning Request 129](#_Toc232857629)

[4.10.4.6 Send Response for the License Provisioning Requests 132](#_Toc232857630)

[4.10.4.7 Display Active Subscription in SAP Subscription Billing 136](#_Toc232857631)

[4.10.4.8 Send Tenant Capability Update 138](#_Toc232857632)

[4.10.5 Perform Decommissioning for Capability “CAD 3D” 140](#_Toc232857633)

[4.10.5.1 Background Job to Set Entitlement Status to Expired 140](#_Toc232857634)

[4.10.5.2 Display Entitlements in SAP Entitlement Management 141](#_Toc232857635)

[4.10.5.3 Group Event for Licenses Expired 142](#_Toc232857636)

[4.10.5.4 Send Tenant Capability Update based on License Capability Decommissioning 143](#_Toc232857637)

[4.10.6 Replace Subscription with New Contract 145](#_Toc232857638)

[4.10.6.1 Terminate Subscription early in SAP Subscription Billing 145](#_Toc232857639)

[4.10.6.2 Display Entitlements in SAP Entitlement Management 146](#_Toc232857640)

[4.10.6.3 Background Job to Trigger Provisioning 146](#_Toc232857641)

[4.10.6.4 Send Response for the License Provisioning Requests 147](#_Toc232857642)

[4.10.6.5 Create SAP S/4HANA Solution Order Replacement Contract 152](#_Toc232857643)

[4.10.6.6 Display Pending Subscriptions in SAP Subscription Billing 154](#_Toc232857644)

[4.10.6.7 Display Entitlements in SAP Entitlement Management 156](#_Toc232857645)

[4.10.6.8 Run Job in SAP Entitlement Management to Set Status to Expired 157](#_Toc232857646)

[4.10.6.9 Display Entitlements in SAP Entitlement Management 158](#_Toc232857647)

[4.10.6.10 Run Job in SAP Entitlement Management to Create License Decommissioning Process 158](#_Toc232857648)

[4.10.6.11 Background Job to Trigger Provisioning 159](#_Toc232857649)

[4.10.6.12 Send Response for the License Decommissioning Requests 160](#_Toc232857650)

[4.10.6.13 Background Job to Trigger Provisioning 164](#_Toc232857651)

[4.10.6.14 Send Response for the Tenant Provisioning Requests 165](#_Toc232857652)

[4.10.6.15 Send Response for the License Provisioning Requests 168](#_Toc232857653)

[4.10.6.16 Display Active Subscription in SAP Subscription Billing 172](#_Toc232857654)

[4.10.7 End of Contract for Test Tenant 174](#_Toc232857655)

[4.10.7.1 Terminate Subscription early in SAP Subscription Billing 174](#_Toc232857656)

[4.10.7.2 Display Entitlements in SAP Entitlement Management 175](#_Toc232857657)

[4.10.7.3 Run Job in SAP Entitlement Management to Set Status to Expired 176](#_Toc232857658)

[4.10.7.4 Display Entitlements in SAP Entitlement Management 177](#_Toc232857659)

[4.10.7.5 Run Job in SAP Entitlement Management to Trigger Tenant Decommissioning 178](#_Toc232857660)

[4.10.7.6 Background Job to Trigger Provisioning 179](#_Toc232857661)

[4.10.7.7 Send Response for the Tenant Decommissioning Requests 179](#_Toc232857662)

## Purpose

Overview

This scope item enables an integrated end-to-end process across SAP S/4HANA Cloud Public Edition, SAP Subscription Billing, and SAP Entitlement Management.

The process covers software subscription modeling and pricing, selling, fulfillment, provisioning, license and software usage, billing, and revenue recognition. It describes the end-to-end process for a new subscription contract, as well as various change processes for subscriptions and the respective fulfillment and provisioning, including license and tenant decommissioning at the end of a subscription contract.

The scope item combines the existing scope items Subscription Management with Sales Billing (57Z), the subscription product part of scope item Solution Order Management (4GT), and scope item Event-Based Revenue Recognition – Subscription Billing (5DQ), extended with processes in SAP Entitlement Management.

The test script is intended for you to manually test the scope item. In a productive implementation, most processes run automatically, monitoring for exceptions. In such an implementation, you can manually create or extend the SAP S/4HANA Cloud solution order and changes in the SAP subscription billing subscription. The SAP Entitlement Management processes run fully automated, assuming license usage and software usage and adoption postings are also automated.

This document provides a detailed procedure for testing this scope item after solution activation, reflecting the predefined scope of the solution. Each process step, report, or item is covered in its own section, providing the system interactions (test steps) in a table view. Steps that are not in scope of the process but are needed for testing are marked accordingly. Project-specific steps must be added.

|  |
| --- |
| Note Values in this test script (decimal notation, date formats, and so on) are presented in U.S. standard notation. If your test system is set up to use a different notation, enter values as appropriate. |

## Prerequisites

### System Access

The test should be conducted with the following system:

|  |
| --- |
| Note For system details, you must contact your system administrator. |

| System | Details |
| --- | --- |
| SAP S/4HANA Cloud Public Edition System | Accessible via SAP Fiori launchpad. Your system administrator provides you with the URL to access the various apps assigned to your role. |
| SAP Cloud Platform | Your system administrator should provide you with a URL and the login details. |
| SAP Subscription Billing Tenant | Your system administrator should provide you with a URL and the login details. |
| Entitlement Management System | Your system administrator should provide you with a URL and the login details. |
| SAP Business Technology Platform (SAP BTP) | Your system administrator should provide you with a URL and the login details. |
| SAP Cloud integration tenant | Your system administrator should provide you with a URL and the login details. |

### Roles

Create business roles using the following business role templates delivered by SAP and assign them to your individual test users.

Alternatively, if available, you can use the following spaces delivered by SAP. You create a space with pages containing predefined essential apps and assign it to the business role. You then assign this business role to your individual users.

For more information, refer to How to Create a Business Role from a Template in the [product assistance](https://help.sap.com/docs/SAP_S4HANA_CLOUD/53e36b5493804bcdb3f6f14de8b487dd/ec310a8b669a45ca898dc4dd91d97de2.html) for SAP S/4HANA Cloud Public Edition.

| Name (Role Template) | ID (Role Template) | Name (Launchpad Space) | ID (Launchpad Space) | Log On |
| --- | --- | --- | --- | --- |
| Roles for Test Procedures |  |  |  |  |
| Solution Order Specialist | SAP_BR_SOLN_ORDER_SPCLST | Solution Order Management | SAP_BR_SOLN_ORDER_SPCLST | Your system administrator provides the user and password information. |
| Administrator | SAP_BR_ADMINISTRATOR | Administration / Administration - Workforce Master Data / Administration - License Compliance / Administration - Data Management / Administration - Output Control | SAP_BR_ADMINISTRATOR / SAP_BUM_SPT_ADMINISTRATION_PC / SAP_EI_SPT_ADM_LC_PC / SAP_CA_SPT_TDR_PC / SAP_OC_SPT_ADMINISTRATION_PC |  |
| Billing Clerk | SAP_BR_BILLING_CLERK | Billing | SAP_BR_BILLING_CLERK | Your system administrator provides the user and password information. |
| General Ledger Accountant | SAP_BR_GL_ACCOUNTANT | General Ledger | SAP_BR_GL_ACCOUNTANT |  |
| Cost Accountant - Sales | SAP_BR_SALES_ACCOUNTANT | Sales Accounting | SAP_BR_SALES_ACCOUNTANT |  |
| Subscription Specialist - Subscription Billing | SAP_BR_SUBSCR_BILLG_SPCLST | Subscription Billing | SAP_CEC_SPT_SUBSCR_BILLG_SPCLST_PC | Your system administrator provides the user and password information. |
| Roles for Master Data Setup |  |  |  |  |
| Master Data Specialist - Product Data | SAP_BR_PRODMASTER_SPECIALIST | Master Data - Products / Product Governance | SAP_BR_PRODMASTER_SPECIALIST / SAP_CMD_SPT_PR_GOV_PC |  |
| Master Data Specialist - Business Partner Data | SAP_BR_BUPA_MASTER_SPECIALIST | Master Data - Business Partners / Business Partner Governance / Business Partner Governance / Business Partner Governance | SAP_BR_BUPA_MASTER_SPECIALIST / SAP_CA_SPT_MDG_BP_GOV_PC / SAP_CMD_SPT_BP_GOV_PC / SAP_CA_SPT_MDG_BP_WFUSR_PC |  |
| Administrator - Data Replication | SAP_BR_ADMINISTRATOR_DATA_REPL |  |  | Your system administrator provides the user and password information. |
| Pricing Specialist | SAP_BR_PRICING_SPECIALIST | Price Management | SAP_BR_PRICING_SPECIALIST |  |
| Pricing Specialist - Subscription Billing | SAP_BR_PRICING_SPCLST_SBL | Subscription Products | SAP_CEC_SPT_PRICING_SPCLST_PC |  |
| Roles for System Setup |  |  |  |  |
| Configuration Expert - Business Process Configuration | SAP_BR_BPC_EXPERT | Business Process Configuration / Business Process Configuration - Finance / Business Process Configuration - Procurement / Manage your Solution / Business Process Configuration - Workflow / Business Configuration - Feature Management / Business Process Configuration - Extensibility Explorer / Business Configuration - Transportation | SAP_BR_BPC_EXPERT / SAP_FIN_SPT_BPC_EXPERT_PC / SAP_MM_SPT_BIZ_PROC_CONFIGN_PC / SAP_CA_SPT_IC_LND_BASE_PC / SAP_CA_SPT_BPC_WORKFLOW_PC / SAP_CA_SPT_BPC_FM_PC / SAP_EI_SPT_BPC_EXT_PC / SAP_TM_SPT_TRANSPCFG_PC | Your system administrator provides the user and password information. |
| Configuration Expert - Subscription Billing | SAP_BR_CONFIG_EXPERT_SBL | Subscription Pricing | SAP_CEC_SPT_CONFIG_EXPERT_PC | Your system administrator provides the user and password information. |
| Extensibility Specialist | SAP_BR_EXTENSIBILITY_SPEC | Extensibility / Extensibility | SAP_BR_EXTENSIBILITY_SPEC / SAP_CA_SPT_EXT_PC |  |
| Configuration Expert - Business Network Integration | SAP_BR_CONF_EXPERT_BUS_NET_INT | Business Network Integration / Business Network Integration - Concur Integration / Business Network Integration - Output Control / Business Network Integration - Data Replication / Configuration Expert - Business Network Integration Cross Applications | SAP_CORE_SPT_INT_PC / SAP_CON_SPT_CONCUR_INT_PC / SAP_OC_SPT_INT_PC / SAP_CA_SPT_DATA_REP_PC / SAP_CA_SPT_BUS_NETWORK_INT_PC |  |
| Cost Accountant - Overhead | SAP_BR_OVERHEAD_ACCOUNTANT | Overhead Accounting | SAP_BR_OVERHEAD_ACCOUNTANT |  |
| Subscription Specialist - Subscription Billing | SAP_BR_SUBSCR_BILLG_SPCLST | Subscription Billing | SAP_CEC_SPT_SUBSCR_BILLG_SPCLST_PC |  |
| Configuration Expert - Subscription Billing | SAP_BR_CONFIG_EXPERT_SBL | Subscription Pricing | SAP_CEC_SPT_CONFIG_EXPERT_PC |  |
| Pricing Specialist - Subscription Billing | SAP_BR_PRICING_SPCLST_SBL | Subscription Products | SAP_CEC_SPT_PRICING_SPCLST_PC |  |
| Admin ( Entitlement Management System) | EM-ADMIN |  |  |  |

### Master Data, Organizational Data, and Other Data

SAP Subscription Billing

Create the organizational data and master data for SAP Subscription Billing manually and use them to test the scope item:

| Data | Sample Value | Details | Comments |
| --- | --- | --- | --- |
| Customer | 33100001 | Domestic UAE Customer 1 | Replicated from SAP S/4HANA Cloud Public Edition |
| Subscription Products |  |  |  |
| Subscription Product (PCS Products) | P-CAD-BRONZE | CAD Bronze Edition |  |
| Subscription Product (PCS Products) | P-CAD-SILVER | CAD Silver Edition |  |
| Subscription Product (PCS Products) | P-CAD-GOLD | CAD Gold Edition |  |
| Subscription Product (PCS Products) | P-CAD-ADD-DOC | CAD Documents | Buy more CAD documents per month |
| Subscription Product (PCS Products) | P-CAD-TRIAL-3D | CAD Free Trial 3D | Free trail for capability 3D |
| Subscription Product (PCS Products) | P-CAD-TST-TENANT | CAD Test Tenant | Additional test tenant of the CAD system |
| Subscription Product (PCS Products) | P-CAD-API | CAD API Access | API access post and get for external users |
| Rate Element Products |  |  |  |
| Rate Elements Products | R-AF | One-Time Activation Fee | One-time activation fee |
| Rate Elements Products | R-LICENSE | License | Recurring license based on quantity |
| Rate Elements Products | R-RECURRING | Recurring Fixed Fee | Recurring fixed licenses without quantity |
| Rate Elements Products | R-API | API Calls | Usage-based |
| Pricing Scheme |  |  |  |
| Pricing Scheme | Initial |  |  |
| Rate Plan Templates |  |  |  |
| Rate Plan Template for Main Products | RPT for CAD Software Editions |  | One-time activation and recurring license based on quantity |
| Rate Plan Template for API Add-On | RPT for CAD Software - API Add-On |  | Usage-based |
| Rate Plan Template for Document Add-On | RPT for CAD Software Addtl. Documents |  | Recurring license based on quantity |
| Rate Plan Template for other Add-Ons | RPT for CAD Software Add-Ons |  | Recurring fixed licenses without quantity |
| Organization Data |  |  |  |
| Market |  |  | Data Mapping:Sales Organization: 3310Distribution Channel: 10Division: 00 |

You can find general information on how to create master data objects in the following [Master Data Scripts (MDS)](https://help.sap.com/docs/s4hana-best-practices/s4cld2608-master-data) .

Master Data Script Reference

| Master Data ID | Description |
| --- | --- |
| 5BD | Create Subscription Product Sales Billing - MDS |

SAP S/4HANA Cloud Public Edition

The organizational structure and business partner for this scope item have been created in your system during activation.

The product master data needs to be replicated from SAP Subscription Billing, and then extended manually based on the test script chapters below.

This results in the following organization data and master data in SAP S/4HANA Cloud Public Edition, to be used for the test of the scope item:

| Data | Sample Value | Details | Comments |
| --- | --- | --- | --- |
| Customer | 33100001 | Domestic UAE Customer 1 | Make sure that the customer you use for this process has either assigned the customer pricing procedure 01 (Procedure 01) or no procedure.To check the assignment, use Business Role SAP_BR_BUPA_MASTER_SPECIALIST - tile Manage Customer Master Data in the Sales Area Data.Replicate Business Partner from SAP S/4HANA Cloud Public Edition to SAP Subscription Billing and SAP Entitlement Management |
| Products |  |  |  |
| Product | P-CAD-BRONZE | CAD Bronze Edition | Replicate from SAP Subscription Billing and extend in SAP S/4HANA Cloud Public Edition |
| Product | P-CAD-SILVER | CAD Silver Edition | Replicate from SAP Subscription Billing and extend in SAP S/4HANA Cloud Public Edition |
| Product | P-CAD-GOLD | CAD Gold Edition | Replicate from SAP Subscription Billing and extend in SAP S/4HANA Cloud Public Edition |
| Product | P-CAD-ADD-DOC | CAD Documents | Replicate from SAP Subscription Billing and extend in SAP S/4HANA Cloud Public Edition |
| Product | P-CAD-TRIAL-3D | CAD Free Trial 3D | Replicate from SAP Subscription Billing and extend in SAP S/4HANA Cloud Public Edition |
| Product | P-CAD-TST-TENANT | CAD Test Tenant | Replicate from SAP Subscription Billing and extend in SAP S/4HANA Cloud Public Edition |
| Product | P-CAD-API | CAD API Access | Replicate from SAP Subscription Billing and extend in SAP S/4HANA Cloud Public Edition |
| Product | R-AF | One-Time Activation Fee | Replicate from SAP Subscription Billing and extend in SAP S/4HANA Cloud Public Edition |
| Product | R-LICENSE | License | Replicate from SAP Subscription Billing and extend in SAP S/4HANA Cloud Public Edition |
| Product | R-RECURRING | Recurring Fixed Fee | Replicate from SAP Subscription Billing and extend in SAP S/4HANA Cloud Public Edition |
| Product | R-API | API-Calls | Replicate from SAP Subscription Billing and extend in SAP S/4HANA Cloud Public Edition |
| Organization Data |  |  |  |
| Sales Organization | 3310 | Dom. Sales Org |  |
| Company Code | 3310 | Company Code 3310 |  |

SAP Entitlement Management

The customer and the offerings needs to be replicated from SAP S/4HANA Cloud Public Edition to SAP Entitlement Management.

The offering to entitlement mapping needs to be done manually, based on the respective chapter below.

This results in the following master data in SAP Entitlement Management, to be used for the test of the scope item:

| Data | Sample Value | Details | Comments |
| --- | --- | --- | --- |
| Customer | 33100001 | Domestic UAE Customer 1 | Replicate Business Partner from SAP S/4HANA Cloud Public Edition to SAP Entitlement |
| Offering | P-CAD-BRONZE | CAD Bronze Edition | Replicate Product from SAP S/4HANA Cloud Public Edition to SAP Entitlement Management |
| Offering | P-CAD-SILVER | CAD Silver Edition | Replicate Product from SAP S/4HANA Cloud Public Edition to SAP Entitlement Management |
| Offering | P-CAD-GOLD | CAD Gold Edition | Replicate Product from SAP S/4HANA Cloud Public Edition to SAP Entitlement Management |
| Offering | P-CAD-ADD-DOC | CAD Documents | Replicate Product from SAP S/4HANA Cloud Public Edition to SAP Entitlement Management |
| Offering | P-CAD-TRIAL-3D | CAD Free Trial 3D | Replicate Product from SAP S/4HANA Cloud Public Edition to SAP Entitlement Management |
| Offering | P-CAD-TST-TENANT | CAD Test Tenant | Replicate Product from SAP S/4HANA Cloud Public Edition to SAP Entitlement Management |
| Offering | P-CAD-API | CAD API Access | Replicate Product from SAP S/4HANA Cloud Public Edition to SAP Entitlement Management |

### Additional Manual Configuration

Before you can test this scope item, you must have completed the additional configuration steps that are described in the Set-Up Instructions for this scope item. These configuration steps are specific for your implementation and include mandatory settings that are not delivered by SAP and must be created by you. For more information, follow the link to the document:

[Link to Set-Up Instructions](https://help.sap.com/docs/SAP_S4HANA_BEST_PRACTICES/8f74439b9b050e0d7cc71998a6b8438e)

### Preliminary Steps

#### Master Data Setup - SAP Subscription Billing

##### Create Rate Elements

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you create rate elements in SAP Subscription Billing. The rate elements will be replicated to SAP S/4HANA Cloud Public Edition products of type SBRE:

| Rate ID | Rate Type | Description |
| --- | --- | --- |
| R-AF | One-Time | One-Time Activation Fee |
| R-LICENSE | Recurring | License |
| R-API | Usage-based | API Calls |
| R-RECURRING | Recurring | Recurring Fixed Fee |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to SAP Subscription Billing as Configuration Expert - Subscription Billing. | The Home page appears. |  |
| 2 | Access the App | Open Manage Business Configuration - Subscription Billing (F6808).Choose Rate Elements from left pane. | The Rate Elements view is displayed. |  |
| 3 | Create Rate Element R-AF | Choose Create and select One-Time from the drop downNavigate to General Info section and enter the following data.ID: R-AFLabel: One-Time Activation FeeDescription: One-Time Activation FeeUnit: EACH (EA)Active: EnabledNavigate to One -Time section and enter the following data:Data Source: NoneOne-Time Type: Initial FeeBilling Type: ChargeChoose Save.Note Confirm Saving pop up will appear: The items cannot be removed after saving. Do you really want to save the items?Click on Save. |  |  |
| 4 | Create Rate Element: R-LICENSE | Choose Create and select Recurring from the drop downNavigate to General Info section and enter the following data.ID: R-LICENSELabel: LicenseDescription: Recurring fee for the number of licenses for software.Unit: EACH (EA)Active: EnabledNavigate to Recurring section and enter the following data:Data Source: SubscriptionBilling Type: ChargeChoose Save.Note Confirm Saving pop up will appear: The items cannot be removed after saving. Do you really want to save the items?Click on Save. |  |  |
| 5 | Create Rate Element: R-RECURRING | Choose Create and select Recurring from the drop downNavigate to General Info section and enter the following data.ID: R-RECURRINGLabel: Recurring Fixed FeeDescription: Recurring fixed fee without quantity.Unit: EACH (EA)Active: EnabledNavigate to Recurring section and enter the following data:Data Source: NoneBilling Type: ChargeChoose Save.Note Confirm Saving pop up will appear: The items cannot be removed after saving. Do you really want to save the items?Click on Save. |  |  |
| 6 | Create Rate Element: Usage-Based | Choose Create and select Usage-Based from the drop downNavigate to General Info section and enter the following data.ID: R-APILabel: API CallsDescription: API CallsUnit: EACH (EA)Active: EnabledNavigate to Usage-Based section and enter the following data:Data Source: UsageUsage Rating Variant: AggregatedType of Technical Resource ID: Original Software IDAuto generate Technical Resource: EnabledBilling Type: ChargeUse Rate Subelements: EnabledChoose Save.Note Confirm Saving pop up will appear: The items cannot be removed after saving. Do you really want to save the items?Click on Save. |  |  |

##### Create Rate Plan Templates

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity you create a rate plan templates in SAP Subscription Billing.

Procedure

1: RPT for CAD Software (no usage charge)

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to SAP Subscription Billing as Configuration Expert - Subscription Billing. | The Home page appears. |  |
| 2 | Access the App | Open Manage Rate Plan Templates (F6809). | The available rate plan templates are displayed. |  |
| 3 | Create Rate Plan Template | Choose Create and select With Pricing Scheme from the drop down.Navigate to General Info section and maintain the following data:Description: RPT for CAD Software EditionsTags: Best Practice; SoftwareUnder Pricing:Currency: Choose Parameter and maintain description as Currency.Pricing Scheme: Initial pricing schemeUnder Billing:Billing Cycle: Choose Parameter and maintain description as Billing CycleEnd-of-Month Rule: Choose Value and select Bill from next month from the drop downBilling Profile: Choose Value and select Initial Settings from the drop down | The basic data for the template is defined. |  |
| 4 | Maintain Charges/Credits | Create a one-time charge.In Charges / Credits section:Click on Create and select One-Time from the drop down.Rate Element: R-AFClick on Add Under Assigned Overridable Fields tab.Select the following Price Element Specification Code :OneTimePriceDiscount1Click on Select and Apply.Create a Recurring charge.In Charges / Credits section:Click on Create and select Recurring from the drop down.Rate Element: R-LICENSEEnter the following in the Value field:Apply Changes with Next Cycle: NoBilling in Advance: YesProrate First Cycle: YesClick on Add Under Assigned Overridable Fields Table.Select the following Price Element Specification Code :RecurringPriceDiscount1Click on Select and Apply. | Charges are created under Charges/Credits section. |  |
| 5 | Save Rate Template | Click on Create and Publish.Note Confirm Publishing pop up will appear: After publishing, you can only edit the template's tags and description.Choose Publish. | Rate plan template XX (RPT for CAD Software Editions) createdRate plan template XX (RPT for CAD Software Editions) published. |  |

2: RPT for CAD Software - API Add-On

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to SAP Subscription Billing as Configuration Expert - Subscription Billing. | The Home page appears. |  |
| 2 | Access the App | Open Manage Rate Plan Templates (F6809). | The available rate plan templates are displayed. |  |
| 3 | Create Rate Plan Template | Choose Create and select With Pricing Scheme from the drop down.Navigate to General Info section and maintain the following data:Description: RPT for CAD Software Add-On: API UsageTags: Best Practice ; SoftwareUnder PricingCurrency: Choose Parameter and maintain description as CurrencyPricing Scheme: Initial pricing schemeUnder BillingBilling Cycle: Choose Parameter and maintain description as Billing CycleEnd of Month Rule: Choose Value and choose Bill from Next MonthBilling Profile: Choose Value and choose Initial Settings | The basic data for the template is defined. |  |
| 4 | Maintain Charges/Credits | Create a Usage-Based charge.In Charges / Credits section:Click on Create and select Usage-Based from the drop down and maintain the following data:Rate Element: R-API.Rate Subelements: Post ; Get.Click on Add Under Assigned Overridable Fields tab.Select the following Price Element Specification Code :UsagePriceDiscount1Click on Select and Apply. | Charges are created under Charges/Credits section. |  |
| 5 | Save Rate Template | Click on Create and Publish.Note Confirm Publishing pop up will appear: After publishing, you can only edit the template's tags and description.Choose Publish. | Rate plan template XX (RPT for CAD Software Add-On: API Usage) created.Rate plan template XX (RPT for CAD Software Add-On: API Usage) published. |  |

3: RPT for CAD Software Addtl. Documents

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to SAP Subscription Billing as Configuration Expert - Subscription Billing. | The Home page appears. |  |
| 2 | Access the App | Open Manage Rate Plan Templates (F6809). | The available rate plan templates are displayed. |  |
| 3 | Create Rate Plan Template | Choose Create and select With Pricing Scheme from the drop down.Navigate to General Info section and maintain the following data:Description: RPT for CAD Software Add-On:LicenseTags: Best Practice; SoftwareUnder PricingCurrency: Choose Parameter and maintain description as CurrencyPricing Scheme: Initial pricing schemeUnder BillingBilling Cycle: Choose Parameter and maintain description as Billing CycleEnd of Month Rule: Choose Value and choose Bill from Next MonthBilling Profile: Choose Value and choose Initial Settings | The basic data for the template is defined. |  |
| 4 | Maintain Charges/Credits | Create a recurring charge.In Charges / Credits section:Click on Create and select Recurring from the drop down and maintain the following data:Rate Element: R-LICENSE.Enter the following in Value field:Apply Changes with Next Cycle: NoBilling Advance: YesProrate First Cycle: YesClick Apply. | Charges are created under Charges/Credits section. |  |
| 5 | Save Rate Template | Click on Create and Publish.Note Confirm Publishing pop up will appear: After publishing, you can only edit the template's tags and description.Choose Publish. | Rate plan template XX (RPT for CAD Software Add-On:License) created.Rate plan template XX (RPT for CAD Software Add-On:License) published. |  |

4: RPT for CAD Software Add-Ons

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to SAP Subscription Billing as Configuration Expert - Subscription Billing. | The Home page appears. |  |
| 2 | Access the App | Open Manage Rate Plan Templates (F6809). | The available rate plan templates are displayed. |  |
| 3 | Create Rate Plan Template | Choose Create and select With Pricing Scheme from the drop down.Navigate to General Info section and maintain the following data:Description: RPT for CAD Software Add-On: No QuantityTags: Best Practice; SoftwareUnder PricingCurrency: Select Parameter and maintain description as CurrencyPricing Scheme: Initial pricing schemeUnder BillingBilling Cycle: Choose Parameter and maintain description as Billing CycleEnd of Month Rule: Choose Value and choose Bill from Next MonthBilling Profile: Choose Value and choose Initial Settings | The basic data for the template is defined. |  |
| 4 | Maintain Charges/Credits | Create a recurring charge.In Charges / Credits section:Click on Create and select Recurring from the drop down and maintain the following data:Rate Element: R-RECURRING.Enter the following in Value field:Apply Changes with Next Cycle: NoBilling Advance: YesProrate First Cycle: YesClick on Apply | Charges are created under Charges/Credits section. |  |
| 5 | Save Rate Template | Click on Create and Publish.Note Confirm Publishing pop up will appear: After publishing, you can only edit the template's tags and description.Choose Publish. | Rate plan template XX (RPT for CAD Software Add-On: No Quantity) created.Rate plan template XX (RPT for CAD Software Add-On: No Quantity) published. |  |

##### Create Product (SAP Subscription Billing)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity you create a product P-CAD-BRONZE , P-CAD-SILVER , P-CAD-GOLD, P-CAD-ADD-DOC, P-CAD-TRIAL-3D, P-CAD-TST-TENANT, P-CAD-API in SAP Subscription Billing. The rate elements will be replicated to SAP S/4HANA Cloud Public Edition products of type SBPD:

|  |
| --- |
| Note For all products, set flag “Create Subscription as Pending”. |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to SAP Subscription Billing as Master Data Specialist – Product Data | The Home page appears. |  |
| 2 | Access the App | Under Master Data and Configuration, open the Manage Products app. | The available products are displayed. |  |
| 3 | Maintain General Product Information | Choose Create and maintain the following data under General Info area:Product Name: CAD Bronze EditionID: P-CAD-BRONZESubscription Type: CommercialDescription: CAD Bronze EditionCreate Subscriptions as Pending: SelectedSubscription Profile: S/4 Integration | General information has been maintained. |  |
| 4 | Maintain Rate Plan for Product | Under Rate Plans, choose Create > With Pricing Scheme and maintain the following data:.Market:Rate Plan Template: RPT for CAD Software EditionsDescription: AE Rate Plan for CAD Bronze EditionTags: Best Practice; SoftwareBilling Cycle: Every month on Reference DateChoose Create.Add Technical Resources and Subscription Parameters pop up will appear, click on Add Selected Items button. | The rate plan has been maintained for the product. |  |
| 5 | Maintain Subscription Terms | Under Subscription Terms, maintain the following:Term of Notice: 30 daysInitial Fixed Term: 12 monthsExpected term: 12 months | Subscription terms are maintained. |  |
| 6 | Maintain Subscription Parameters | Under Subscription Parameters, maintain the following:Subscription Parameter: License (R-LICENSE)Click on Add and maintain the above Subscription Parameter, if it is not available. |  |  |
| 7 | Create Product | For the entire product, choose Create and PublishWarning pop up appears with the following message: There are pricing errors, or the pricing check could not be executed, or rate plans have mismatched market. Do you really want to publish this product?Choose OK. | The P-CAD-BRONZE product is created in SAP Subscription Billing, and replicated to SAP S/4HANA Cloud Public Edition. |  |
| 8 | Repeat Steps | Repeat steps from 3 to 6 to create the following Products from the table below. | Products are created in SAP Subscription Billing, and replicated to SAP S/4HANA Cloud Public Edition |  |

| Product ID | Product Name | Description | Rate Plan Template | Rate Plan Description | Subscription Parameter | Term of Notice | Minimum term | Initial Fixed Term | Expected Term | Expected Term Extension |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| P-CAD-SILVER | CAD Silver Edition | CAD Silver Edition | RPT for CAD Software Editions | AE Rate Plan for CAD Silver Edition | R-LICENSE | 30 days |  | 12 months | 12 months | 12 months |
| P-CAD-GOLD | CAD Gold Edition | CAD Gold Edition | RPT for CAD Software Editions | AE Rate Plan for CAD Silver Edition | R-LICENSE | 30 days |  | 12 months | 12 months | 12 months |
| P-CAD-ADD-DOC | CAD Documents | CAD Documents | RPT for CAD Software Add-On: License | AE Rate Plan for CAD Silver Edition | R-LICENSE | 30 days |  | 12 months | 12 months | 12 months |
| P-CAD-TRIAL-3D | CAD Free Trial 3D | CAD Free Trial 3D | RPT for CAD Software Add-on: No Quantity | AE Rate Plan for CAD Silver Edition |  | 30 days | 3 months | 3 months | 3 months |  |
| P-CAD-TST-TENANT | CAD Test Tenant | CAD Test Tenant | RPT for CAD Software Add-on: No Quantity | AE Rate Plan for CAD Silver Edition |  | 30 days |  | 12 months | 12 months | 12 months |
| P-CAD-API | CAD API Access | CAD API Access | RPT for CAD Software Add-On: API Usage | AE Rate Plan for CAD Silver Edition | R-API | 30 days |  | 12 months | 12 months | 12 months |

##### Create Lookup Table for Recurring Price Alternative

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This step is to create Lookup Table for Recurring Price Alternative.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Subscription Billing as Configuration Expert (Price Calculation). | The Home page appears. |  |
| 2 | Navigate to Lookup Tables app | Open Manage Lookup Tables - Subscription Billing (F7133). | The available Lookup Tables are displayed. |  |
| 3 | Create Lookup Table | Click on CreateNavigate to Header section and maintain the following data:Code: Recurring Price AlternativeDescription: Alternative Recurring prices for products | General information has been maintained. |  |
| 4 | Maintain the Inputs | Navigate to Inputs section and maintain the following data:Code: productCode, marketId and rateElement | Inputs for Lookup table are maintained. |  |
| 5 | Maintain the Output and Save | Navigate to Lookup Table Outputs section and maintain the following data:Code: priceClick on Create. | Lookup Table created. |  |

##### Create Price Element Specification

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This step is to create the Recurring Price Alternative Price Element Specification.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Subscription Billing as Configuration Expert (Price Calculation). | The Home page appears. |  |
| 2 | Navigate to Manage Price Element Specification app | Open Manage Price Element Specifications - Subscription Billing (F7134). | The available Lookup Tables are displayed. |  |
| 3 | Create Price Element Specification | Click on CreateNavigate to Header section and maintain the following data:Code: Recurring Price AlternativeDescription: Alternative Recurring price | Header Information is maintained. |  |
| 4 | Maintain Pricing Tree | Navigate to Pricing Tree section and enter the following data:Under Component, choose from the drop down.Component: Table LookupLookup Table: Recurring Price AlternativeReference Date: Pricing DateClick on New Component in Line 2 (IF) and select the values:Component: Calculate Price ElementPrice Condition: priceScale Value: quantityQuantity: quantityRatio: prorataScroll down and select New Component of Else as Skip Price Element. | Pricing data is maintained. |  |
| 5 | Maintain Overridable Fields | Navigate to Overridable Fields section and enter the following data:Code: price | Overridable fields are maintained. |  |
| 6 | Maintain Custom Output Attributes | Navigate to Custom Output Attributes section and enter the following data:Code: Subscription BillingNavigate to Values:field: conditionTypeOrigin: ConstantValue: ZMP2 | Overridable fields are maintained. |  |
| 7 | Create the Price Element Specification | Click on Create. | Price element specification created. |  |

##### Addition of Price Element to Pricing Scheme

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This step is to add the price element to the pricing scheme (Initial).

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Subscription Billing as Configuration Expert (Price Calculation). | The Home page appears. |  |
| 2 | Navigate to Manage Pricing Schemes | Open Manage Pricing Schemes - Subscription Billing (F7131). | The available Pricing Schemes are displayed. |  |
| 3 | Edit Pricing Scheme and save | Select Initial Pricing Scheme and click to get the detailsClick on EditUnder Items table enter the following data:Step: 101 (Below the Recurring Price)Adjust the step numbers accordingly.Price Element Specification: Recurring Price AlternativeName: Alternative Recurring PriceSign: +Click on Save. | Object saved. |  |

##### Uploading Lookup Tables for Price Determination

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

You can upload your lookup tables for one-time, recurring, and usage-based fees and for the discount, using the following procedure. The data in the following table is used to find the relevant prices during price determination as part of the rating process.

Procedure

Table 1: Table 1: Upload One-Time Table

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to SAP Subscription Billing as Configuration Expert (Price Calculation) | The Home page appears. |  |
| 2 | Navigate to App | Under Master Data Management, open the Manage Lookup Table Data - Subscription Billing (F7135) app. | The lookup tables are displayed. |  |
| 3 | Choose OneTimePrice | Choose the lookup table OneTimePrice.Download the empty table and store it locally as a CSV file.Tip If the format of the downloaded file is not column separated, you must change the format of the spreadsheet to a US format. |  |  |
| 4 | Update the downloaded file | Enter the following values and save the file:productCodemarketIdrateElementprice(Price Condition Type)price (Price Type)price (Amount Value or Multiplier)price (Amount Currency)P-CAD-BRONZER-AFSingleFixed99AEDP-CAD-SILVERR-AFSingleFixed129AEDP-CAD-GOLDR-AFSingleFixed149AED |  |  |
| 5 | Upload the CSV file | Choose the lookup table OneTimePrice and go to Import > Browse to upload the saved file from the previous step.Note There are two types of imports. Choose Merge to keep the existing data intact.Click on Import. | The lookup table OneTimePrice is updated. |  |

Table 2: Table 2: Upload Recurring Table

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to SAP Subscription Billing as Configuration Expert (Price Calculation) | The Home page appears. |  |
| 2 | Navigate to App | Under Master Data Management, open the Manage Lookup Table Data - Subscription Billing (F7135) app. | The lookup tables are displayed. |  |
| 3 | Choose RecurringPrice | Choose the lookup table RecurringPrice.Download the empty table and store it locally as a CSV file.Tip If the format of the downloaded file is not column separated, you must change the format of the spreadsheet to a US format. |  |  |
| 4 | Update the downloaded file | Enter the following values and save the file:productCodemarketIdrateElementprice(Price Condition Type)price (Price Type)price (Amount Value or Multiplier)price (Amount Currency)price (Pricing Unit Value)price (Pricing Unit UoM or Currency)P-CAD-ADD-DOCR-LICENSESingleLinear100AED100EAP-CAD-TST-TENANTR-RECURRINGSingleFixed150AEDP-CAD-TRIAL-3DR-RECURRINGSingleFixed0AED |  |  |
| 5 | Upload the CSV file | Choose the lookup table RecurringPrice and go to Import > Browse to upload the saved file from the previous step.Note There are two types of imports. Choose Merge to keep the existing data intact.Click on Import. | The lookup table RecurringPrice is updated. |  |

Table 3: Table 3: Upload Usage Table

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to SAP Subscription Billing as Configuration Expert (Price Calculation) | The Home page appears. |  |
| 2 | Navigate to App | Under Master Data Management, open the Manage Lookup Table Data - Subscription Billing (F7135) app. | The lookup tables are displayed. |  |
| 3 | Choose UsagePrice | Choose the lookup table UsagePrice.Download the empty table and store it locally as a CSV file.Tip If the format of the downloaded file is not column separated, you must change the format of the spreadsheet to a US format. |  |  |
| 4 | Update the downloaded file | Enter the following values and save the file:productCodemarketIdrateElementrateSubElementprice(Price Condition Type)price (Range Value)price (Range UoM or Currency)price (Price Type)price (Amount Value or Multiplier)price (Amount Currency)price (Pricing Unit Value)price (Pricing Unit UoM or Currency)P-CAD-APIR-APIGetTier50EALinear0AED1EAP-CAD-APIR-APIGetTierEALinear0.1AED1EAP-CAD-APIR-APIPostTier50EALinear0AED1EAP-CAD-APIR-APIPostTierEALinear0.2AED1EA |  |  |
| 5 | Upload the CSV file | Choose the lookup table UsagePrice and go to Import > Browse to upload the saved file from the previous step.Note There are two types of imports. Choose Merge to keep the existing data intact.Click on Import. | The lookup table UsagePrice is updated. |  |

Table 4: Table 4: Upload Alternative Recurring PriceTable

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to SAP Subscription Billing as Configuration Expert (Price Calculation) | The Home page appears. |  |
| 2 | Navigate to App | Under Master Data Management, open the Manage Lookup Table Data - Subscription Billing (F7135) app. | The lookup tables are displayed. |  |
| 3 | Choose RecurringPriceAlternative | Choose the lookup table RecurringPriceAlternative.Download the empty table and store it locally as a CSV file.Tip If the format of the downloaded file is not column separated, you must change the format of the spreadsheet to a US format. |  |  |
| 4 | Update the downloaded file | Enter the following values and save the file:productCodemarketIdrateElementprice(Price Condition Type)price (Range Value)price (Range UoM or Currency)price (Price Type)price (Amount Value or Multiplier)price (Amount Currency)price (Pricing Unit Value)price (Pricing Unit UoM or Currency)P-CAD-BRONZER-LICENSETier30EALinear100AED1EAP-CAD-BRONZER-LICENSETier50EALinear90AED1EAP-CAD-BRONZER-LICENSETier80EALinear80AED1EAP-CAD-BRONZER-LICENSETier100EALinear70AED1EAP-CAD-BRONZER-LICENSETierEALinear50AED1EAP-CAD-SILVERR-LICENSETier30EALinear160AED1EAP-CAD-SILVERR-LICENSETier50EALinear140AED1EAP-CAD-SILVERR-LICENSETier80EALinear120AED1EAP-CAD-SILVERR-LICENSETier100EALinear110AED1EAP-CAD-SILVERR-LICENSETierEALinear100AED1EAP-CAD-GOLDR-LICENSETier30EALinear200AED1EAP-CAD-GOLDR-LICENSETier50EALinear180AED1EAP-CAD-GOLDR-LICENSETier80EALinear160AED1EAP-CAD-GOLDR-LICENSETier100EALinear140AED1EAP-CAD-GOLDR-LICENSETierEALinear100AED1EA |  |  |
| 5 | Upload the CSV file | Choose the lookup table RecurringPriceAlternative and go to Import > Browse to upload the saved file from the previous step.Note There are two types of imports. Choose Merge to keep the existing data intact.Click on Import. | The lookup table RecurringPriceAlternative is updated. |  |

##### Replicate Business Partners from SAP S/4HANA Cloud Public Edition to SAP Subscription Billing

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity you replicate business partner from SAP S/4HANA Cloud Public Edition to SAP Subscription Billing.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to SAP S/4HANA Cloud Public Edition as Administrator - Data Replication. | The Home page appears. |  |
| 2 | Navigate to Replicate by Object Selection | Open Replicate by Object Selection (DRF_MANUAL_REPLICATION). | Replicate by Object Selection screen appears. |  |
| 3 | Enter the selection parameters | Select Business Object Type: CustomerIn the table Business Objects to be Replicated, enter the valueCustomer: 33100001Test Run Only: UncheckedTarget System Selection : checked, Example: BS_5SWClick on Replicate. | Selected objects replicated. |  |
| 4 | Display Logs | Click on Display Logs for the details of replication. | Log is displayed. |  |

##### Maintain Standard Master Agreement for Customer in SAP Subscription Billing

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step , you maintain Master Agreement: RES for the residential division of the customer.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Subscription Billing as Configuration Expert (Price Calculation). | The Home page appears. |  |
| 2 | Navigate to App | Under Master Data and Configuration, open Customer Overview - Subscription Billing (F6800). | The available customers are displayed. |  |
| 3 | Search for Customer | Enter the following and click Go.Customer ID: 33100001Select Customer and click on the Navigation chevron. | Search required Customer. |  |
| 4 | Navigate to Customer References | Click on Customer Info area and Navigate to Customer References section.Click Create and enter the following the data:Reference Type: Master AgreementID: RESClick on Save. | Customer Reference is maintained. |  |

#### Master Data Setup - SAP S/4HANA Cloud

##### Maintain Product Groups in SAP S/4HANA Cloud Public Edition

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

Depending on your configuration environment for SAP S/4HANA Cloud Public Edition, choose one of the following options:

Configure Your Solution:

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori launchpad using the role Configuration Expert - Business Process Configuration. |  |  |
| 2 | Access the App | Open Manage Your Solution (F1241).Note If required, choose Set Local Version to set the desired local version. | The Manage Your Solution screen displays. |  |
| 3 | Open Configure Your Solution | Choose Configure Your Solution. | The Configure Your Solution screen displays. |  |
| 4 | Open Configuration Item for Material Group creation | Enter the following filters:Application Area: Database and Data ManagementSub-Application Area: ProductItem Name: ProductClick on Navigation Chevron for details. |  |  |
| 5 | Go to Define Material Groups | Choose Configure on the right of Define Material Groups. | The Define Material Groups: Change screen displays. |  |
| 6 | Maintain New Entries | Click on New Entries and maintain the following:Material GroupMaterial Group Description01_CADCAD02_CAD2CAD Add-on03_COLLABCollaboration04_ANALYTAnalytics | The New Entries: Added Entries screen displays. |  |
| 7 | Save your data | Choose Save. | Material Groups are created. |  |

##### Maintain Master Data S/4HANA Cloud

###### Enhance Subscription Billing Products

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you enhance the subscription billing products in SAP S/4HANA. This product is created in Subscription Billing, replicated to SAP S/4HANA, and is available once the replication of products is set up as part of the Setup Guide. For more information about replication of products, refer to [Configure IFlow Package for Replication of Products and Rate Elements](https://help.sap.com/docs/CLOUD_TO_CASH_OD/a78a4be305be4dbc903bd826a1aba456/93e79ab9ec8e4dc49bc1710e396608ed.html)

|  |
| --- |
| Note Brazil-specific fields require a proper tax calculation. For more information about this, refer to Material Master Data > Define BR Specific Fields for Master Data > Create Master Data for Brazil (JD0_BR) . |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori launchpad using the role Master Data Specialist - Product Data. | The Home page appears. |  |
| 2 | Access the SAP Fiori app | Open Manage Product Master Data (F1602). | The Manage Product Master Data screen appears. |  |
| 3 | Find the Product | In the search area on the top, enterProduct: P-CAD-BRONZEChoose Go.Click on Navigation Chevron to get details. | Your product is displayed in the report list. |  |
| 4 | Update Product Group | Click on Edit, Choose Edit Header.In the pop-up window, maintain the followingProduct Group: 01_CADClick OK. | Product Group updated. |  |
| 5 | Maintain Distribution Chains: General Information | On the Product view, in the Distribution Chains area, choose Create and maintain the following data:Sales Organization: 3310Distribution Channel: 10Note The distribution chain is not required for the SBPD product type if you are using MDI. They are only required if you are using Cloud Integration. | Sales Org and distribution channel maintained. |  |
| 6 | Maintain Distribution Chains: Grouping Terms | Navigate to the Grouping Terms area and maintain the following data:Item Category Group: SBPD (Sub. Billing Product)Account Assignment Group: X5 (SP-Licenses)Only if your system is set up to be tested with tax, Navigate to the Sales Tax area and maintain the following data:Departure Ctry/Reg.:Tax Classification: 1 (Full Tax)Then choose Apply. | Grouping terms are maintained and the product is saved. |  |
| 7 | Maintain Plants | Navigate to Plants, click on Create and maintain the following data:Plant: 3310Choose Apply and Save. | Plant data is maintained. |  |
| 8 | Repeat Steps 3 to 7 for other products | Repeat from Step 3 to 7 with the following table data for the products.ProductProduct GroupItem Category GroupP-CAD-SILVER01_CADSBPDP-CAD-GOLD01_CADSBPDP-CAD-ADD-DOC02_CAD2SBPDP-CAD-TRIAL-3D02_CAD2SBPDP-CAD-TST-TENANT02_CAD2SBPDP-CAD-API02_CAD2SBPDR-AF01_CADSBRER-LICENSE01_CADSBRER-API01_CADSBRER-RECURRING01_CADSBRE | Products are enhanced for subscription billing. |  |

###### Maintain Sales Prices for Revenue Split

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you maintain sales price condition records.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori launchpad using the role Pricing Specialist (Price Calculation). | The Home page appears. |  |
| 2 | Access the SAP Fiori app | Open Set Material Prices - Sales (VK12). | The Change Condition Records page appears. |  |
| 3 | Access condition type | Enter Condition Type: ZP21 and select Sales Org/Distr. Chl/YY1_PRODUC in the Key Combination pop-up.Click on Choose. |  |  |
| 4 | Enter the filter values | Enter the following values:Sales Organization: 3310Distribution Channel: 10Click on Execute. |  |  |
| 5 | Enter the values | Maintain the following values:Product SoAmountUnitP-CAD-BRONZE20%P-CAD-GOLD20%P-CAD-ADD-SILVER20% |  |  |
| 6 | Save | Choose Save. | Condition Records saved. |  |
| 7 | Access Condition Type | Enter Condition Type: ZP22Follow the same steps mentioned 3 to 6 with the following data:Product SoAmountUnitP-CAD-GOLD10% |  |  |
| 8 | Access Condition Type | Enter Condition Type: ZP2B.Follow the same steps mentioned 3 to 6 with the following data:Product SoAmountUnitP-CAD-BRONZE<empty>%P-CAD-GOLD<empty>%P-CAD-ADD-SILVER<empty>% |  |  |
| 9 | Repeat these steps mentioned for ZP2B | Enter Condition Type: ZP2B and select Material with release status in the Key Combination pop-up.Click on Choose |  |  |
| 10 | Enter the filter values | Enter the following values:Sales Organization: 3310Distribution Channel: 10Click on Execute. |  |  |
| 11 | Enter the values | Maintain the following values:Product SoAmountUnitR-LICENSE100%Choose Save. |  |  |

#### Master Data set up – SAP Entitlement Management

##### Replicate Business Partner from SAP S/4HANA Cloud Public Edition to SAP Entitlement Management

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you replicate business partners from SAP S/4HANA Cloud Public Edition to SAP EMS.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to SAP S/4HANA Cloud Public Edition as Administrator - Data Replication. | The Home page appears. |  |
| 2 | Open the app | Open Replicate by Replication Model (DRF_ADHOC_REPLICATION) app. | The Replicate by Replication Model screen appears. |  |
| 3 | Choose Replication Model | Choose the replication model created in Create Communication arrangement for Business Partner Integration (SAP_COM_0008)Example: BPREP_5SW | Replication model is selected. |  |
| 4 | Choose Filter | Choose Display Filter CriteriaIn the new window, choose Edit and select MDG_BP_SFT filter object under Main Filters, then create a filter as per your requirements.Business Partner Number: 33100001Choose Apply and Save. | Business Partner is selected. |  |
| 5 | Replicate BP | Choose Replicate. | Business Partner including Relationships is replicated. |  |

##### Mark Products in SAP S/4HANA Cloud Public Edition as “Relevant for Entitlement Generation”

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you enable products relevant for entitlement generation.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to SAP S/4HANA Cloud Public Edition as Master Data Specialist - Product Data. | The Home page appears. |  |
| 2 | Open the app | Open Manage Product Master Data (F1602) app. | The Manage Product Master Data app opens. |  |
| 3 | Search for Product | In the Product Description search field, enter CAD* and click on Go. | The list of products are displayed. |  |
| 4 | Access Product | Click on > to access the product P-CAD-BRONZE. | General Information is displayed. |  |
| 5 | Navigate to Distribute Chains | Navigate to Distribution Chains and click on Edit. Then, click on >. | Distribution Chain is displayed. |  |
| 6 | Set Checkmark | Set the checkbox Relevant for Entitlement Generation. | Checkbox is set. |  |
| 7 | Apply and Save Changes | Click on Apply and Save it. | Changes are saved. |  |
| 8 | Repeat Steps for Other Products | Repeat the steps 3 to 7 for the following products.P-CAD-SILVERP-CAD-GOLDP-CAD-ADD-DOCP-CAD-TRIAL-3DP-CAD-TST-TENANTP-CAD-API | Relevant for Entitlement Generation set for products. |  |

##### Replicate Products from SAP S/4HANA Cloud Public Edition to SAP Entitlement Management

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity you replicate products from SAP S/4HANA Cloud Public Edition to SAP EMS.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to SAP S/4HANA Cloud Public Edition as Administrator - Data Replication. | The Home page appears. |  |
| 2 | Open the app | Open Replicate by Object Selection (DRF_MANUAL_REPLICATION). | The Replicate by Object Selection screen appears. |  |
| 3 | Choose Product | Select the Business Object Type as Product from the drop down menu.Enter the materials below Business Objects to be Replicated section.Example: P-CAD-BRONZE, P-CAD-SILVER, P-CAD-GOLD, P-CAD-ADD-DOC, P-CAD-TRIAL-3D, P-CAD-TST-TENANT, P-CAD-API | Products are selected. |  |
| 4 | Select Target System | Choose your target system. | Target System is selected. |  |
| 5 | Replicate Product | Click on Replicate. | Product is replicated. |  |

##### Maintain Offering – Entitlements Mapping for Entitlement Model Master Agreement

1. Log on to Entitlement Management System.
2. Open Configure Entitlement Master Data app and open Assign Entitlements to Offerings – Offering-to-Entitlement Mapping.
3. Create the first mapping based on the table below.
4. For the 2nd entry, choose Copy, select the mapping just created, choose Confirm, select the category to copy to, choose Confirm.
5. Adjust the settings in the copied mapping based on the table below.

Table 5: General Settings and Value Assignments

| Category or Offering | Name | Entitlement Model ID | Conditional | Status | Execution Batch | Conditions Field | Conditions Operator | Quantity | Valid From | Valid To | Master Agreement |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  |  |  |  |  |  |  |  | Static | Static | Static | Map |
| 01_CAD | Master Agreement 01_CAD | SI_5SW_MA | X | Active | 10 | Item.Master Agreement | Is Not Empty | 1 | 01/01/0001 | 12/31/9999 | Item.Master Agreement |
| 02_CAD | Master Agreement 02_CAD | SI_5SW_MA | X | Active | 11 | Item.Master Agreement | Is Not Empty | 1 | 01/01/0001 | 12/31/9999 | Item.Master Agreement |

##### Maintain Offering – Entitlements Mapping for Entitlement Model Tenant

1. Log on to Entitlement Management System.
2. Open Configure Entitlement Master Data app and open Assign Entitlements to Offerings – Offering-to-Entitlement Mapping.
3. Create the first mapping, using the first table with field settings for all mappings, and the first row in the 2nd table.
4. For the other entries in the 2nd table, choose Copy, select the mapping created first, choose Confirm, select the category to copy to, choose Confirm.
5. Adjust the settings in the copied mapping based on the table below.

Table 6: General Settings and Value Assignments which are the same for all mappings

| Entitlement Model ID | Conditional | Status | Conditions Field | Conditions Operator | Quantity | Valid From | Valid To | Master Agreement |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  |  |  |  |  | Static | Static | Static | Map |
| SI_5SW_Tenant | X | Active | Item.Master Agreement | Is Not Empty | 1 | 01/01/0001 | 12/31/9999 | Item.Master Agreement |

Table 7: General Settings and Value Assignment which are different for each mapping

| Category or Offering | Name | Execution Batch | Application | System Type | Unique Per |
| --- | --- | --- | --- | --- | --- |
|  |  | Static | Static | Static | Static |
| 01_CAD | CAD PRD Tenant | 50 | CAD Application | Productive System | L1 |
| 01_CAD | CAD TST Tenant | 51 | CAD Application | Test System | L1 |
| 01_CAD | COLLAB PRD Tenant | 52 | Collaboration Application | Productive System | L1 |
| 01_CAD | COLLAB TST Tenant | 53 | Collaboration Application | Test System | L1 |
| P-CAD-GOLD | Analytics PRD Tenant | 54 | Analytics Application | Productive System | L1 |
| P-CAD-GOLD | Analytics TST Tenant | 55 | Analytics Application | Test System | L1 |
| P-CAD-TST-TENANT | CAD ADD TST Tenant | 56 | CAD Application | Test System | L3 |

##### Maintain Offering – Entitlements Mapping for Entitlement Model Tenant Phase

1. Log on to Entitlement Management System.
2. Open Configure Entitlement Master Data app and open Assign Entitlements to Offerings – Offering-to-Entitlement Mapping.
3. Create the first mapping, using the first table with field settings for all mappings, and the first row in the 2nd table.
4. For the other entries in the 2nd table, choose Copy, select the mapping created first, choose Confirm, select the category to copy to, choose Confirm.
5. Adjust the settings in the copied mapping based on the table below.

Table 8: General Settings and Value Assignments which are the same for all mappings

| Entitlement Model ID | Conditional | Status | Conditions Field | Conditions Operator | Quantity | Valid From | Valid To | Master Agreement |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  |  |  |  |  | Static | Static | Static | Map |
| SI_5SW_Tenant_Phase | X | Active | Item.Master Agreement | Is Not Empty | 1 | 01/01/0001 | 12/31/9999 | Item.Master Agreement |

Table 9: General Settings and Value Assignment which are different for each mapping

| Category or Offering | Name | Execution Batch | Application | System Type | Unique Per |
| --- | --- | --- | --- | --- | --- |
|  |  | Static | Static | Static | Static |
| 01_CAD | CAD PRD Tenant Phase | 70 | CAD Application | Productive System | L1 |
| 01_CAD | CAD TST Tenant Phase | 71 | CAD Application | Test System | L1 |
| 01_CAD | COLLAB PRD Tenant Phase | 72 | Collaboration Application | Productive System | L1 |
| 01_CAD | COLLAB TST Tenant Phase | 73 | Collaboration Application | Test System | L1 |
| P-CAD-GOLD | Analytics PRD Tenant Phase | 74 | Analytics Application | Productive System | L1 |
| P-CAD-GOLD | Analytics TST Tenant Phase | 75 | Analytics Application | Test System | L1 |
| P-CAD-TST-TENANT | CAD ADD TST Tenant Phase | 76 | CAD Application | Test System | L3 |

##### Maintain Offering – Entitlements Mapping for Entitlement Model License

1. Log on to Entitlement Management System.
2. Open Configure Entitlement Master Data app and open Assign Entitlements to Offerings – Offering-to-Entitlement Mapping.
3. Create the first mapping, using the first table with field settings for all mappings, and the first row in the 2nd table.
4. For the other entries in the 2nd table, choose Copy, select the mapping created first, choose Confirm, select the category to copy to, choose Confirm.
5. Adjust the settings in the copied mapping based on the table below.

Table 10: General Settings and Value Assignments which are the same for all mappings

| Entitlement Model ID | Conditional | Status | Conditions Field | Conditions Operator | Valid From | Valid To | Master Agreement | Unique Per |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  |  |  |  |  | Mapping | Mapping + Calculate | Map | Static |
| SI_5SW_License | X | Active | Item.Master Agreement | Is Not Empty | Item.ValidFrom | Item.ValidTo – 1 day | Item.MasterAgreement | L3 |

Table 11: General Settings and Value Assignment which are different for each mapping

| Category or Offering | Name | Execution Batch | Quantity | Mapping field | Calculate | Operator | Value | Metric | Application | Capability |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  |  | Static Value |  |  |  |  |  | Static Value | Static Value | Static Value |
| 01_CAD | License User | 20 | Map | Item.License |  |  |  | Users | CAD Application |  |
| 01_CAD | License CAD 2D Essentials | 21 | Static Value |  |  |  | 1 |  | CAD Application | CAD 2D Essentials |
| 01_CAD | COLLAB_Basic | 22 | Static Value |  |  |  | 1 |  | Collaboration Application | Collaboration Basic |
| P-CAD-BRONZE | License Documents | 23 | Map | Item.License | X | * | 3 | Documents | CAD Application |  |
| P-CAD-SILVER | COLLAB Advanced Silver | 24 | Static Value |  |  |  | 1 |  | Collaboration Application | Collaboration Advanced |
| P-CAD-SILVER | CAD 2D Advanced - Silver | 25 | Static Value |  |  |  | 1 |  | CAD Application | CAD 2D Advanced |
| P-CAD-SILVER | License Documents | 26 | Map | Item.License | X | * | 10 | Documents | CAD Application |  |
| P-CAD-GOLD | CAD 2D Advanced Gold | 27 | Static Value |  |  |  | 1 |  | CAD Application | CAD 2D Advanced |
| P-CAD-GOLD | COLLAB Realtime Gold | 28 | Static Value |  |  |  | 1 |  | Collaboration Application | Collaboration Realtime |
| P-CAD-GOLD | COLLAB Advanced Gold | 29 | Static Value |  |  |  | 1 |  | Collaboration Application | Collaboration Advanced |
| P-CAD-GOLD | CAD 3D Gold | 30 | Static Value |  |  |  | 1 |  | CAD Application | CAD 3D |
| P-CAD-TRIAL-3D | CAD Free Trial 3D | 31 | Static Value |  |  |  | 1 |  | CAD Application | CAD 3D |
| P-CAD-ADD-DOC | CAD Addl Docs | 32 | Map | Item.License |  |  |  | Documents | CAD Application |  |
| P-CAD-API | CAD API Post | 33 | Static Value |  |  |  | 50 | API Calls | CAD Application | CAD API Calls Post |
| P-CAD-API | CAD API Get | 34 | Static Value |  |  |  | 50 | API Calls | CAD Application | CAD API Calls Get |

##### Maintain Specific Views for “Maintain Customer Entitlements” App

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity you set up specific views for entitlements, for the master agreements RES and COM representing the residential division and the commercial division of the customer, subscribing to different license and tenants, for each of the divisions. If you are using different master agreements in your testing, you can adjust the views accordingly, or overwrite the filter Master Agreement on a specific view.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to Entitlement Management System as Admin. | The Home page appears. | The Entitlement Management Home page appears. |
| 2 | Open the app | Open Maintain Customer Entitlements App | The Maintain Customer Entitlements screen appears. |  |
| 3 | Create Filter Residential All | Activate Filter:Choose Adapt FiltersAdd the following filters: Master Agreement, Application, System Type, Entitlement ModelClick on OK.Choose Setting to adapt the layout of the listIn the View Settings pop up, select the following fields, and use the arrow buttons to sort the added fields, then choose OK.Fields to add: Master Agreement, Reference Document Number, Reference Item Number, Application, System Type, Metric, Tenant ID, CapabilityCustomer: 33100001Master Agreement: RESClick on the drop down arrow next to Entitlements in the top left cornerChoose Save AsEnter the View: Residential AllChoose Save | Filter Residential All was created. |  |
| 4 | Create Filter Residential Tenants | Activate Filter:Choose Adapt FiltersAdd the following filters: Master Agreement, Application, System Type, Entitlement ModelClick on OK.Choose Setting to adapt the layout of the listIn the View Settings pop up, select the following fields, and use the arrow buttons to sort the added fields, then choose OK.Fields to add:Add the following filters: Master Agreement, Reference Document Number, Reference Item Number, Application, System Type, Metric, Tenant ID, Tenant URL, Tenant Name, CapabilityChoose filter:Customer: 33100001Master Agreement: RESEntitlement Model: Master Agreement, Tenant, Tenant PhaseClick on the drop down arrow next to Entitlements in the top left cornerChoose Save AsEnter the View: Residential TenantsChoose Save | Filter Residential Tenants was created. |  |
| 5 | Create Filter Residential Licenses | Activate Filter:Choose Adapt FiltersAdd the following filters: Master Agreement, Application, System Type, Entitlement ModelClick on OK.Choose Setting to adapt the layout of the listIn the View Settings pop up, select the following fields, and use the arrow buttons to sort the added fields, then choose OK.Fields to add: Master Agreement, Reference Document Number, Reference Item Number,Application, Metric, Capability.Customer: 33100001Master Agreement: RESEntitlement Model: LicenseClick on the drop down arrow next to Entitlements in the top left cornerChoose Save AsEnter the View: Residential LicensesChoose Save. | Filter Residential Licenses was created. |  |
| 6 | Create Filter Commercial All | Activate Filter:Choose Adapt FiltersAdd the following filters: Master Agreement, Application, System Type, Entitlement ModelClick on OK.Choose Setting to adapt the layout of the listIn the View Settings pop up, select the following fields, and use the arrow buttons to sort the added fields, then choose OK.Fields to add: Master Agreement, Reference Document Number, Reference Item Number, System Type, Application, Metric,Tenant ID, Capability.Customer: 33100001Master Agreement: COMClick on the drop down arrow next to Entitlements in the top left cornerChoose Save AsEnter the View: Commercial AllChoose Save. | Filter Commercial All was created. |  |
| 7 | Create Filter Commercial Tenants | Activate Filter:Choose Adapt FiltersAdd the following filters: Master Agreement, Application, System Type, Entitlement ModelClick on OK.Choose Setting to adapt the layout of the listIn the View Settings pop up, select the following fields, and use the arrow buttons to sort the added fields, then choose OK.Fields to add: Master Agreement, Reference Document Number, Reference Item Number, Application, System Type, Metric, Tenant ID, Tenant URL, Tenant Name, Capability.Customer: 33100001Master Agreement: COMEntitlement Model: Master Agreement, Tenant, Tenant PhaseClick on the drop down arrow next to Entitlements in the top left cornerChoose Save AsEnter the View: Commercial TenantsChoose Save. | Filter Commercial Tenants was created. |  |
| 8 | Create Filter Commercial Licenses | Activate Filter:Choose Adapt FiltersAdd the following filters: Master Agreement, Application, System Type, Entitlement ModelClick on OK.Choose Setting to adapt the layout of the listIn the View Settings pop up, select the following fields, and use the arrow buttons to sort the added fields, then choose OK.Fields to add: Master Agreement, Reference Document Number, Reference Item Number, Application, Metric, Capability.Customer: 33100001Master Agreement: COMEntitlement Model: LicenseClick on the drop down arrow next to Entitlements in the top left cornerChoose Save AsEnter the View: Commercial LicensesChoose Save. | Filter Commercial Licenses was created. |  |

#### Prepare SAP Business Accelerator Hub to test the SAP Entitlement Management Provisioning Response

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to SAP Entitlement Management as Admin | The Home page appears. |  |
| 2 | Determine sub domain and region to use in subsequent steps | From the standard URL for SAP Entitlement Management, after logging on, extract <identityzone>For example : https://<identityzone>.<region>.entlms.cloud.sap/cp.portal/site?sap-language=en#Shell-home |  |  |
| 3 | Access the App | Open the Explore APIs app |  |  |
| 4 | Search for API | Interface: Inbound_Interface_Provisioning_Async_Request_CallbackClick on Go. |  |  |
| 5 | Determine sub domain and region to use in subsequent steps | From the URL shown, note down subdomain (e.g. live-test) and region (e.g. us10 or eu10):https://ems-api-<subdomain>.<region>.entlms.cloud.sap/provisioning-process/request-task/callback |  |  |
| 6 | API access | Click on the API ID “Inbound_Interface_Provisioning_Async_Request_Callback” to access the API documentation on SAP Business Accelerator hub.Afterward the relevant help page will be opened in a new window |  |  |
| 7 | Try out the API | Click on Try Out. |  |  |
| 8 | Select Environment | Click Select Environment, then + Add New Environment |  |  |
| 9 | Add new Environment and enter parameters | The Configure New Environment pop up window will be displayed.Enter the following parameters:Under Basic Information:Display Name: <Display Name for Environment>, e.g. “Provisioning Callback”Starting URL: In the drop down menu, choose the URL pattern that reflects the URL from stepSubdomain: <Subdomain>Under Resulting URL:Resulting URL: <Choose the correct URL>Under Authentication:Authentication Type: OAuth 2.0 Application FlowClient ID: <Client ID>Client Secret: <Client Secret>Identityzone: <Identityzone>Region: <Region>Under Environment Scope:Apply this environment to all APIs in this package that are not yet configured: CheckedSave this environment for future sessions: X (Selected)Click on Configure. |  |  |
| 10 | Repeat the same for quick update api | Repeat steps 3 to 8 with API Inbound_Interface_Entitlement_Process_Quick_Update with Display Name: quick update |  |  |

#### Prepare SoapUI to test the SAP Entitlement Management Provisioning Response (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This step helps to test the provisioning responses and response through the SoapUI and the steps required to configure and test the APIs.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Get the test tool SoapUI | Download SoapUI from the following location: https://www.soapui.org/downloads/soapui/Install the package.Choose a suitable version based on your operating system, Windows 32-bit or Windows 64-bit.Note If you already have SoapUI installed, please skip this step. |  |  |
| 2 | Create Project | Choose File >Create Empty Project at the top left of the screen and make the following entry:Proptery Name: <Enter the name for your Project> |  |  |
| 3 | Create Endpoint | Choose Endpoint Explorer | Endpoint Explorer screen is displayed |  |
| 4 | Maintain Endpoint | Change the method from GET to POST.Enter Endpoint : <URL can be found in EMS Explore APIs, search for Inbound_Interface_Provisioning_Async_Request_Callback >Choose Save Request.Choose Authorization tab, SelectTYPE: OAuth 2.0 Application FlowClient ID: <Client ID>Client Secret: <Client Secret>Access Token URI: <Token URI>Choose Get Token.Save the profile.Choose Headers tab and add one line entry with the following:Host: ems-api-live-test.cfapps.eu10.hana.ondemand.comMedia-Type: application/jsonChoose Body tab, select the radio button of Raw.Choose Save. |  | Service URL/Service Interface is the end point URLe.g. [https://ems-api-live-test.eu10.entlms.cloud.sap/provisioning-process/request-task/callback](https://ems-api-live-test.eu10.entlms.cloud.sap/provisioning-process/request-task/callback) |
| 5 | Repeat the same for quick update api | Repeat steps 3 to 5 with API Inbound_Interface_Entitlement_Process_Quick_Update with Display Name: quick update |  | Endpoint URL e.g. [https://ems-api-live-test.eu10.entlms.cloud.sap/v2/entitlement-process-quick](https://ems-api-live-test.eu10.entlms.cloud.sap/v2/entitlement-process-quick) |

## Overview Table

This scope item consists of several process steps provided in the table below.

If your system administrator has enabled spaces and pages on the SAP Fiori launchpad, the home page will only contain the essential apps for performing the typical tasks of a business role.

You can find all other apps not included on the home page using the search bar.

If you want to personalize the home page and include the hidden apps, navigate to your user profile and choose Settings > App Finder.

| Process Step | Business Role | Transaction/App | Expected Output |
| --- | --- | --- | --- |
| [Create Solution Order](#unique_30) [page ] 61 | Solution Order Specialist | Manage Solution Orders (F4615) | New Solution Order is created. |
| [Manage Subscription Billing - Display Pending Subscription in SAP Subscription Billing](#unique_31) [page ] 63 | Solution Order Specialist | Manage Solution Orders (F4615) | Subscription details are displayed. |
| [Manage Entitlements - Display Entitlements in SAP Entitlement Management](#unique_32) [page ] 65 | EM-Admin | Maintain Customer Entitlements | Tenant and License Entitlements are viewed. |
| Entitlement Management |  |  |  |
| [Background Job to Trigger Provisioning](#unique_33) [page ] 66 | EM-Admin | Monitor Background Job Logs | Provisioning Request job is triggered to send message from provisioning process to the Provisioning System. |
| [Send Response for the Tenant Provisioning Requests](#unique_34) [page ] 67 | EM-Admin | Maintain Customer Entitlements | Tenant provisioning response is tested. |
| [Send Response for the License Provisioning Requests](#unique_35) [page ] 69 | EM-Admin | Maintain Customer Entitlements | License provisioning response is tested. |
| [Check Event for Subscription Activation in SAP Entitlement Management](#unique_36) [page ] 73 | EM-Admin | Monitor Event Logs | Subscription Activation event is checked. |
| [Send Tenant Capability Update](#unique_37) [page ] 74 | EM-Admin | Maintain Customer Entitlements | Tenant capability update is sent. |
| [Enter License Consumption in SAP Entitlement Management](#unique_38) [page ] 77 | EM-Admin | Maintain Customer Entitlements | License consumption is entered. |
| [Enter Software Usage and Adoption in SAP Entitlement Management](#unique_39) [page ] 78 | EM-Admin | Maintain Customer Entitlements | Software Usage and Adoption are entered. |
| Manage Subscription Billing |  |  |  |
| [Display Active Subscription in SAP Subscription Billing](#unique_40) [page ] 80 | Solution Order Specialist | Manage Solution Orders (F4615) | Active subscription details are viewed. |
| [Display Provider Contract](#unique_41) [page ] 82 | Solution Order Specialist | Display Provider Contract for Sales Billing (FP_PC3) | Provider Contract details are viewed. |
| [Monitor Revenue Recognition (Event-Based): Provider Contracts](#unique_42) [page ] 83 | Cost Accountant - Sales | Event-Based Revenue Recognition - Provider Contracts (F5406) | Revenue Recognition is monitored. |
| [Manage Usage Records in SAP Subscription Billing](#unique_43) [page ] 84 | Subscription Specialist - Subscription Billing | Manage Usage Records - Deprecated (F6802) | Usage of APIs at the end of billing period is recorded. |
| [Display Pre-Bill in SAP Subscription Billing](#unique_44) [page ] 86 | Subscription Specialist - Subscription Billing | Manage Billing Data - Subscription Billing (F6803) | Pre-Bill details are viewed. |
| Manage Billing Document in SAP S/4HANA Cloud Public Edition |  |  |  |
| [Create Billing Document](#unique_45) [page ] 87 | Billing Clerk | Create Billing Documents (F0798) | Billing Document is created. |
| [Display Billing Document](#unique_46) [page ] 88 | Billing Clerk | Manage Billing Documents (F0797) | Sales Order billing document is displayed. |
| [Display Journal Entry Analyzer](#unique_47) [page ] 89 | General Ledger Accountant | Journal Entry Analyzer (FIS_FPM_OVP_JEANA (FIS_FPM_OVP_JEANA)) | Journal Entry document is displayed. |
| Manage Revenue Recognition |  |  |  |
| [Monitor Revenue Recognition (Event-Based): Provider Contracts](#unique_48) [page ] 91 | Cost Accountant - Sales | Event-Based Revenue Recognition - Provider Contracts (F5406) | Provider Contract Revenue is reviewed. |
| [Run Revenue Recognition: Provider Contracts (Period-End Activity)](#unique_49) [page ] 92 | Cost Accountant - Sales | Event-Based Revenue Recognition - Provider Contracts (F5406) | Event-based revenue recognition for provider contracts is executed. |
| [Manage Real-Time Revenue Recognition Issues – Provider Contracts](#unique_50) [page ] 93 | Cost Accountant - Sales | Event-Based Revenue Recognition - Provider Contracts (F5406) | Posting entries are reviewed. |
| [Change Processes](#unique_51) [page ] 94 |  |  |  |
| Separate CAD Subscription for a the Commercial Division of the Customer |  |  |  |
| [Create Solution Order](#unique_52) [page ] 94 | Solution Order Specialist | Manage Solution Orders (F4615) | Solution Order is created. |
| [Display Pending Subscription in SAP Subscription Billing](#unique_53) [page ] 96 | Solution Order Specialist | Manage Solution Orders (F4615) | Subscription details are displayed. |
| [Display Entitlements in SAP Entitlement Management](#unique_54) [page ] 98 | EM-Admin | Maintain Customer Entitlements | Tenant and License Entitlements are viewed. |
| [Background Job to Trigger Provisioning](#unique_55) [page ] 129 | EM-Admin | Monitor Background Job Logs | Provisioning Request job is triggered to send message from provisioning process to the Provisioning System. |
| [Send Response for the Tenant Provisioning Request](#unique_56) [page ] 129 | EM-Admin | Maintain Customer Entitlements | Tenant provisioning response is tested. |
| [Send Response for the License Provisioning Requests](#unique_57) [page ] 132 | EM-Admin | Maintain Customer Entitlements | License provisioning response is tested. |
| [Display Active Subscription in SAP Subscription Billing](#unique_58) [page ] 136 | Solution Order Specialist | Manage Solution Orders (F4615) | Active subscription details are viewed. |
| [Send Tenant Capability Update](#unique_59) [page ] 109 | EM-Admin | Maintain Customer Entitlements | Tenant capability update is sent. |
| Change Subscription – Number of Users |  |  |  |
| [Change Number of Users in SAP Subscription Billing](#unique_60) [page ] 112 | Subscription Specialist - Subscription Billing | Manage Subscriptions (F6801) | Number of users in subscription is increased. |
| [Display Entitlements in SAP Entitlement Management](#unique_61) [page ] 113 | EM-Admin | Maintain Customer Entitlements | Tenant and License Entitlement are displayed. |
| [Background Job to Trigger Provisioning](#unique_62) [page ] 113 | EM-Admin | Monitor Background Job Logs | Send Provisioning Request job is triggered. |
| [Send Response for the License Provisioning Requests](#unique_63) [page ] 114 | EM-Admin | Maintain Customer Entitlements | Response of License Provisioning completion is sent. |
| Change Subscription – Extend Subscription Duration |  |  |  |
| [Extend Subscription End Date in SAP Subscription Billing](#unique_64) [page ] 117 | Subscription Specialist - Subscription Billing | Manage Subscriptions (F6801) | Subscription is extended. |
| [Display Entitlements in SAP Entitlement Management](#unique_65) [page ] 118 | EM-Admin | Maintain Customer Entitlements | Tenant and License Entitlement are displayed. |
| [Background Job to Trigger Provisioning](#unique_66) [page ] 119 | EM-Admin | Monitor Background Job Logs | Send Provisioning Request job is triggered. |
| [Send Response for the License Provisioning Requests](#unique_67) [page ] 120 | EM-Admin | Maintain Customer Entitlements | Response of License Provisioning completion is sent. |
| Add Additional Subscriptions for Users, Documents, Test Tenant, Trial CAD 3D |  |  |  |
| [Extend Solution Order with Additional Subscriptions](#unique_68) [page ] 123 | Solution Order Specialist | Manage Solution Orders (F4615) | Solution Order is extended. |
| [Display Pending Subscriptions in SAP Subscription Billing](#unique_69) [page ] 126 | Solution Order Specialist | Manage Solution Orders (F4615) | Pending subscription is viewed. |
| [Display Entitlements in SAP Entitlement Management](#unique_70) [page ] 128 | EM-Admin | Maintain Customer Entitlements | Tenant and License Entitlement are displayed. |
| [Background Job to Trigger Provisioning](#unique_55) [page ] 129 | EM-Admin | Monitor Background Job Logs | Send Provisioning request job is triggered. |
| [Send Response for the Tenant Provisioning Request](#unique_56) [page ] 129 | EM-Admin | Maintain Customer Entitlements | Tenant Provisioning Request response is sent. |
| [Send Response for the License Provisioning Requests](#unique_57) [page ] 132 | EM-Admin | Maintain Customer Entitlements | License Provisioning Request response is sent. |
| [Display Active Subscription in SAP Subscription Billing](#unique_58) [page ] 136 | Solution Order Specialist | Manage Solution Orders (F4615) | Active subscription is viewed. |
| [Send Tenant Capability Update](#unique_71) [page ] 138 | EM-Admin | Maintain Customer Entitlements | Tenant capability update is sent. |
| Perform Decommissioning for Capability “CAD 3D” |  |  |  |
| [Background Job to Set Entitlement Status to Expired](#unique_72) [page ] 140 | EM-Admin | Monitor Background Job Logs | Job to set Expired status is triggered. |
| [Display Entitlements in SAP Entitlement Management](#unique_73) [page ] 141 | EM-Admin | Maintain Customer Entitlements | Commercial license entitlement is displayed. |
| [Group Event for Licenses Expired](#unique_74) [page ] 142 | EM-Admin | Maintain Customer Entitlements | Capability is decommissioned. |
| [Send Tenant Capability Update based on License Capability Decommissioning](#unique_75) [page ] 143 | EM-Admin | Maintain Customer Entitlements | Tenant Capability update is sent. |
| [Replace Subscription with New Contract](#unique_76) [page ] 145 |  |  |  |
| [Terminate Subscription early in SAP Subscription Billing](#unique_77) [page ] 145 | Subscription Specialist - Subscription Billing | Manage Subscriptions (F6801) | Subscription is terminated and status set to Expired. |
| [Display Entitlements in SAP Entitlement Management](#unique_78) [page ] 146 | EM-Admin | Maintain Customer Entitlements | Tenant and License Entitlement are displayed. |
| [Background Job to Trigger Provisioning](#unique_79) [page ] 146 | EM-Admin | Monitor Background Job Logs | Send Provisioning request job is triggered. |
| [Send Response for the License Provisioning Requests](#unique_80) [page ] 147 | EM-Admin | Maintain Customer Entitlements | Tenant Provisioning Request response is sent. |
| [Create SAP S/4HANA Solution Order Replacement Contract](#unique_81) [page ] 152 | Solution Order Specialist | Manage Solution Orders (F4615) | Subscription licenses are updated as per customer request. |
| [Display Pending Subscriptions in SAP Subscription Billing](#unique_82) [page ] 154 | Solution Order Specialist | Manage Solution Orders (F4615) | Pending subscription is viewed. |
| [Display Entitlements in SAP Entitlement Management](#unique_83) [page ] 156 | EM-Admin | Maintain Customer Entitlements | Tenant and License Entitlement are displayed. |
| [Run Job in SAP Entitlement Management to Set Status to Expired](#unique_84) [page ] 157 | EM-Admin | Monitor Background Job Logs | Set status to Expired job is triggered. |
| [Display Entitlements in SAP Entitlement Management](#unique_85) [page ] 158 | EM-Admin | Maintain Customer Entitlements | Tenant and License Entitlement are displayed. |
| [Run Job in SAP Entitlement Management to Create License Decommissioning Process](#unique_86) [page ] 158 | EM-Admin | Monitor Background Job Logs | License Decommissioning job is triggered. |
| [Background Job to Trigger Provisioning](#unique_87) [page ] 159 | EM-Admin | Monitor Background Job Logs | Send Provisioning Request job is triggered. |
| [Send Response for the License Decommissioning Requests](#unique_88) [page ] 160 | EM-Admin | Maintain Customer Entitlements | License decommissioning response is tested. |
| [Background Job to Trigger Provisioning](#unique_89) [page ] 164 | EM-Admin | Monitor Background Job Logs | Send Provisioning Request job is triggered. |
| [Send Response for the Tenant Provisioning Requests](#unique_90) [page ] 165 | EM-Admin | Maintain Customer Entitlements | Tenant provisioning response is tested. |
| [Send Response for the License Provisioning Requests](#unique_91) [page ] 168 | EM-Admin | Maintain Customer Entitlements | License provisioning response is tested. |
| [Display Active Subscription in SAP Subscription Billing](#unique_92) [page ] 172 | Solution Order Specialist | Manage Solution Orders (F4615) | Active subscription is viewed. |
| End of Contract for Test Tenant |  |  |  |
| [Terminate Subscription early in SAP Subscription Billing](#unique_93) [page ] 174 | Subscription Specialist - Subscription Billing | Manage Subscriptions (F6801) | Subscription is terminated. |
| [Display Entitlements in SAP Entitlement Management](#unique_94) [page ] 175 | EM-Admin | Maintain Customer Entitlements | Commercial Tenants detail is viewed. |
| [Run Job in SAP Entitlement Management to Set Status to Expired](#unique_95) [page ] 176 | EM-Admin | Monitor Background Job Logs | Background job to set Expired status is triggered. |
| [Display Entitlements in SAP Entitlement Management](#unique_96) [page ] 177 | EM-Admin | Maintain Customer Entitlements | Commercial Tenants detail is viewed. |
| [Run Job in SAP Entitlement Management to Trigger Tenant Decommissioning](#unique_97) [page ] 178 | EM-Admin | Monitor Background Job Logs | Tenant Decommissioning Job is created. |
| [Background Job to Trigger Provisioning](#unique_98) [page ] 179 | EM-Admin | Monitor Background Job Logs | Decommissioning request job is triggered. |
| [Send Response for the Tenant Decommissioning Requests](#unique_99) [page ] 179 | EM-Admin | Maintain Customer Entitlements | Tenant Decommissioning response is tested. |

## Test Procedures

### Create Solution Order

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This step describes how to create a new solution order and add line items (for example, sales items, service items and service contract items) to solution order.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad using the role Solution Order Specialist. | The Fiori Launchpad with access to the Manage Solution Orders application is displayed. |  |
| 2 | Open Manage Solution Orders application | Open Manage Solution Orders (F4615). | The Manage Solution Orders screen is displayed. |  |
| 3 | Create Solution Order | Choose Create from the solution order list page. | Create Solution Order window is displayed. |  |
| 4 | Maintain Solution Order data | Enter the following data to create a solution order:Description: <your description>External Reference: <your reference>Sold-To Party: for example, 33100001 for AE (Domestic UAE Customer 1)Note Select the sales organization (for example, 3310) and Contact person from the pop-up appears. | Required header data for the Solution order has been maintained. |  |
| 5 | Maintain Master Agreement | Under Solution Order Details – Additional Data, maintain master agreement: for example, RESNote Make sure that all entitlements for that master agreement have been deleted from previous tests in SAP Entitlement Management.Note If no master agreement is entered either here in the solution order header, or in the solution order item in section Subscription Billing Item Details, the master agreement maintained in chapter [Maintain Standard Master Agreement for Customer in SAP Subscription Billing](#unique_15) [page ] 33 will be added in SAP Cloud Integration as the master agreement to use. |  |  |
| 6 | Add Item P-CAD-BRONZE | Maintain the following Item in the solution order under Items:Product ID: P-CAD-BRONZEQuantity: 1Choose Enter.Click on Action(Edit) icon.Under Subscription Parameters, enter the following:Parameter ID: R-LICENSEValue: 20In the Subscription Terms section enter the following details:Contract Start: < First Day of Current Month >Click on Simulate to simulate the pricing.Click on Apply.Check the Net Value of line item 10. |  |  |
| 7 | Add Item P-CAD API | Maintain the following Item in the solution order under Items:Product ID: P-CAD-APIQuantity: 1Choose Enter.Click on Action(Edit) icon.In the Subscription Terms section enter the following details:Contract Start Date: < First Day of Current Month >Click on Simulate.Click on Apply.Check the Net Value of line item 20 | The subscription item is now added to Solution Order. |  |
| 8 | Release Items and Save Solution Order | Click on Release All Items under Items and Click on Save.Click on Refresh.Navigate to Transaction History.On clicking on the Transaction number, you can directly navigate to SAP Subscription Billing.Note User can navigate to the subscription billing via the transaction history in Solution Order. Alternatively, log on to Subscription Billing > Manage Subscriptions and search for the created subscriptions using the Subscription ID.Check in the Contract ItemCheck one-time price, Recurring Net Charge/ Month, Usage Based Net Charges / Month | On release the items are replicated as Subscription Contract to SAP Subscription Billing and also different entitlements in SAP Entitlement Management will be created. |  |

### Manage Subscription Billing - Display Pending Subscription in SAP Subscription Billing

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The purpose of this step is to view the subscription in the Subscription Billing tenant and to verify the details.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad using the role Solution Order Specialist, if the subscription is created via a Solution Order. | The Fiori Launchpad is displayed. |  |
| 2 | Navigate to Manage Solution Orders | Open Manage Solution Orders (F4615). | The Manage Solution Orders page is displayed. |  |
| 3 | Search for Solution Order | In the search area enter the Solution Order ID in the Solution Order field.Choose Go. | The solution order is displayed in the search result. |  |
| 4 | Open Solution Order | Choose the solution order from the result list. | Solution Order details are displayed. |  |
| 5 | View Progress | In the Solution Order screen, choose View Progress. | Solution Order Progress is displayed. |  |
| 6 | Navigate to Subscription | In the Solution Order Progress screen, go to section Solution Order Progress.Choose the box with the Subscription.Choose icon Navigate to Transaction.Choose the subscription ID to navigate to the Subscription in SAP Subscription Billing.Note User can navigate to the subscription billing via the transaction history in Solution Order.Alternatively, log on to Subscription Billing > Manage Subscriptions and search for the created subscriptions using the Subscription ID. |  |  |
| 7 | Check Subscription Header Details | Check the following subscription header details at the top:Customer : 33100001Status: PendingValid From: XXX XX, XXXXExpires On: XXX XX, XXXX | All the details are rightly available in Subscription Billing. |  |
| 8 | Check Subscription item details | In the Processing Data , check for the details like:Subscription ProfileRelated DocumentsSubscription DatesSnapshot DataIn the Item List, choose Subscription Item, to view the complete details of the transaction.Details like Billing, Subscription Parameters, Pricing can be viewed. | All the item details of the Subscription Item can be viewed. |  |

### Manage Entitlements - Display Entitlements in SAP Entitlement Management

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

Use the Maintain Customer Entitlements app to view and manage entitlements. Using this app, you can create, view, edit, split, change status, reassign (move) folders of entitlement records, or export a filtered Entitlements List.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to SAP Entitlement Management. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Maintain Customer Entitlements app. | APP is displayed. |  |
| 3 | Select the tenant and the license entitlement | Select the views Residential Tenants and then Residential Licenses.Click on Go. | Tenant and license entitlements are shown, as well as the underlying master agreement entitlement. |  |
| 4 | Capability and Quantity Check | Check the details of the respective entitlements. |  |  |
| 5 | Check related subscription | If desired, to navigate to the subscription for a specific entitlement, click on the highlighted number for column “reference document”. | The subscription is shown. |  |

### Entitlement Management

#### Background Job to Trigger Provisioning

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

To send the message from the provisioning process to the provisioning system, the background job “5SW Send Provisioning Request” has to be triggered, as described below.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to SAP Entitlement Management. | The SAP Fiori Launchpad displays. |  |
| 2 | Access the App | Open Monitor Background Job Logs app |  |  |
| 3 | Execution of the job | Choose job name 5SW Send Provisioning Request.Choose Execute and choose Confirm. | Job is selected and executed. Wait for message: “Job has been executed, please go to the “JOB LOGS” section to refresh and see the latest job logs”. |  |
| 4 | Refresh | Refresh and look at the provisioning requests. | Check the sent provisioning request to the provisioning system. |  |

#### Send Response for the Tenant Provisioning Requests

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

After the different provisioning request has been sent to the provisioning system, the provisioning of the tenants is performed by the provisioning system. After completion, the provisioning system sends a response to SAP Entitlement Management. The test description below describes how to manually test that response, using SAP Business Accelerator Hub (aka API Hub) / SoapUI.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to SAP Entitlement Management. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Maintain Customer Entitlements app. |  |  |
| 3 | Select the Tenant Entitlement | Select the view Residential Tenants. | Tenant entitlements are shown, as well as the underlying master agreement entitlement. |  |
| 4 | View Provisioning Process and copy TaskExecutionLogGuid | Choose the entitlement number withEntitlement Model: Tenant PhaseApplication: CAD ApplicationSystem Type: Productive SystemUnder Phase section, choose View Phase Detail.Choose tab Provision.Choose Expand/Collapse Node.Note down the Process Log ID.Choose the Process Log ID.Select Send Provisioning Request and choose the View Log icon in the middle .On pop-up window Send Provisioning Request, choose the Message Log ID.On window Communication Messages, choose the icon under Payload column.On pop-up Payload, click anywhere in the window, then press CTRL-F.In the search window, enter the Process Log ID noted down earlier and click on Enter.Double click on the field behind TaskExecutionLogGuid above your process log ID, and press CTRL-C to copy it. |  |  |
| 5 | Prepare the provisioning response on SAP Business Accelerator Hub / SoapUI | Launch:[https://api.sap.com/api/SAP_CF_EMS_Provisioning_Process/tryout](https://api.sap.com/api/SAP_CF_EMS_Provisioning_Process/tryout), and select the environment you created in chapter Prepare SAP Business Accelerator Hub to test the SAP Entitlement Management Provisioning Response.For SoapUI, select the project you created in chapter Prepare SoapUI to test the SAP Entitlement Management Provisioning Response (Optional)Choose the Body tab.Click in the area below the example payload, click Enter, and click CTRL+V to insert the copied TaskExecutionLogGuid.Replace the example payload with the payload below, for the application and system type.Double click on the TaskExecutionLogGuid, click CTRL+X, then double click on GUID, then click CTRL+V to insert the Guid.Note Workaround for specific URL:If the URL provided in SAP Entitlement Management starts with [https://ems-api-ext.cfapps.eu10-005.hana.ondemand.com/](https://ems-api-ext.cfapps.eu10-005.hana.ondemand.com/), then do the following:Choose the Headers tab.Choose Add New Header.In the drop down box, select Host.In field value, Enter: ems-api-live-test.cfapps.eu10.hana.ondemand.com |  |  |
| 6 | Send Provisioning Response | Choose Run/ Choose Send for SoapUI. | The response body outlines that the response was sent successfully. |  |
| 7 | Return to app Maintain Customer Entitlements | On pop up Payload, choose Close and choose Back. | The tenant provisioning process has status Completed. |  |
| 8 | Return to Entitlements Tenants Overview | Choose Back.Choose Back.In Maintain Customer Entitlements, choose View Residential Tenants. | The entitlement for tenant phases and tenants for application CAD and system type Productive System have status Active.The tenant entitlement shows the Tenant ID, Tenant Name, Tenant URL based on the provisioning feedback. |  |
| 9 | Repeat for other licenses | Repeat steps 4 to 8 using the payload belowApplicationSystem TypeCAD ApplicationTest SystemCollaboration ApplicationProductive SystemCollaboration ApplicationTest System |  |  |

#### Send Response for the License Provisioning Requests

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

After the different provisioning requests for tenants has been sent to the provisioning system, the provisioning of the licenses for the new contract is performed by the provisioning system. After completion, the provisioning system sends a response to SAP Entitlement Management. The test description below describes how to manually test that response, using SAP Business Accelerator Hub (aka API Hub) / SoapUI.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to SAP Entitlement Management. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Maintain Customer Entitlements app. |  |  |
| 3 | Select the License Entitlement | Select the view Residential Licenses. | License entitlements are shown, as well as the underlying master agreement entitlement. |  |
| 4 | View Provisioning Process and copy TaskExecutionLogGuid | Choose the entitlement number withEntitlement Model: LicenseApplication: CAD ApplicationMetric: UsersChoose tab Provision.Choose Expand for SI 5SW License DecommissioningNote down the Process Log ID.Choose the Process Log ID.Choose License Provisioning Request.Choose the icon in the middle, View Log.On pop-up window License Provisioning Request, choose the Message Log ID.On window Communication Messages, choose the icon under Payload.On pop-up Payload, click anywhere in the window, then press CTRL-F.In the search window, enter the Process Log ID noted down earlier and click on Enter.Double click on the field behind TaskExecutionLogGuid above your process log ID, and press CTRL-C to copy it. |  |  |
| 5 | Prepare the provisioning response on SAP Business Accelerator Hub / SoapUI | Launch:[https://api.sap.com/api/SAP_CF_EMS_Provisioning_Process/tryout](https://api.sap.com/api/SAP_CF_EMS_Provisioning_Process/tryout), and select the environment you created in chapter Prepare SAP Business Accelerator Hub to test the SAP Entitlement Management Provisioning Response.For SoapUI, select the project you created in chapter Prepare SoapUI to test the SAP Entitlement Management Provisioning Response (Optional)Choose the Body tab.Click in the area below the example payload, click Enter, and click CTRL+V to insert the copied TaskExecutionLogGuid.Replace the example payload with the payload below, for the application and system type.Double click on the TaskExecutionLogGuid, click CTRL+X, then double click on GUID, then click CTRL+V to insert the GuidNote Workaround for specific URL:If the URL provided in SAP Entitlement Management starts with https://ems-api-ext.cfapps.eu10-005.hana.ondemand.com/ then do the following:Choose the Headers tab.Choose Add New Header.In the drop down box, select Host.In field value, Enter: ems-api-live-test.cfapps.eu10.hana.ondemand.com |  |  |
| 6 | Send Provisioning Response | Choose Run / Send for SoapUI. | The response body outlines that the response was sent successfully. |  |
| 7 | Return to app Maintain Customer Entitlements | On pop up Payload, choose Close and choose Back. | The license provisioning process has status Completed. |  |
| 8 | Return to Entitlements License Overview | Choose Back.In Maintain Customer Entitlements, choose View Residential Licenses. | The entitlement for license with application CAD Application and metric Users has status Active. |  |
| 9 | Repeat for other licenses | Repeat steps 4 to 8 using the payload belowApplicationCapabilityMetricQuantityCAD ApplicationDocumentsCAD ApplicationCAD 2D EssentialsCAD ApplicationCAD API Calls PostAPI CallsCAD ApplicationCAD API Calls GetAPI CallsCollaboration ApplicationCollaboration Basic |  |  |

Payload for CAD Users License

[ {
"taskExecutionLogGuid" : "GUID",
"response" : {
"Capability_ID" : "",
"Capability_Active" : true,
"Application" : "CAD",
"Quantity" : 20
}
} ]

Payload for CAD Documents Licenses

[ {
"taskExecutionLogGuid" : "GUID",
"response" : {
"Capability_ID" : "",
"Capability_Active" : true,
"Application" : "CAD",
"Quantity" : 60
}
} ]

Payload for CAD 2D Essentials

[ {
"taskExecutionLogGuid" : "GUID",
"response" : {
"Capability_ID" : "CAD_2D_ES",
"Capability_Active" : true,
"Application" : "CAD",
"Quantity" : 1
}
} ]

Payload for CAD API Post License

[ {
"taskExecutionLogGuid" : "GUID",
"response" : {
"Capability_ID" : "CAD_API_POST",
"Capability_Active" : true,
"Application" : "CAD",
"Quantity" : 50
}
} ]

Payload for CAD API Get License

[ {
"taskExecutionLogGuid" : "GUID",
"response" : {
"Capability_ID" : "CAD_API_GET",
"Capability_Active" : true,
"Application" : "CAD",
"Quantity" : 50
}
} ]

Payload for Collaboration Basic

[ {
"taskExecutionLogGuid" : "GUID",
"response" : {
"Capability_ID" : "COLLAB_BAS",
"Capability_Active" : true,
"Application" : "COLLAB",
"Quantity" : 1
}
} ]

#### Check Event for Subscription Activation in SAP Entitlement Management

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

After the provisioning of all tenants and licenses for the subscription contract have been completed, an event has been created in SAP Entitlement Management, which sets the subscription contract from “Pending” to “Active”. Check that the event has been successfully triggered in SAP Entitlement Management.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to SAP Entitlement Management. | The SAP Fiori Launchpad displays. |  |
| 2 | Access the App | Open Monitor Event Logs app |  |  |
| 3 | Execution of the job name | Select Send Notification.For the last event with Event Name 5SW Activate Subscription Contract with Notification Status Sent, Choose the Notification Log ID and then choose the icon under Payload on the Communication Messages screen. | The message sent to SAP Cloud Integration to trigger the contract activation is shown. The contract number to be activated can be found with tag SI_5SW_Contract. |  |

#### Send Tenant Capability Update

Procedure

After completing license provisioning, which activated a specific capability, the provisioning system sends a call to SAP Entitlement Management, to updated the enabled license capabilities in the tenant entitlement.

Based on that, the tenant entitlement acts as the “Digital Twin” of the real system tenant, showing in a table attribute of the tenant entitlement for a specific tenant, which capabilities have been licensed and are currently enabled in that tenant.

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Prepare the entitlement update on SAP Business Accelerator Hub / SoapUI | Launch:[https://api.sap.com/api/SAP_CF_EMS_Entitlement_Process_Quick_Update/tryout](https://api.sap.com/api/SAP_CF_EMS_Entitlement_Process_Quick_Update/tryout) and select the environment you created in chapter Prepare SAP Business Accelerator Hub to test the SAP Entitlement Management Provisioning Response.For SoapUI, select the project you created in chapter Prepare SoapUI to test the SAP Entitlement Management Provisioning Response (Optional)Choose the Body tab.Replace the example payload with the payload below.Note Workaround for specific URLIf the URL provided in SAP Entitlement Management starts with [https://ems-api-ext.cfapps.eu10-005.hana.ondemand.com/](https://ems-api-ext.cfapps.eu10-005.hana.ondemand.com/), Choose the Headers tab. Choose Add New Header. In the dropdown box, select Host. In field value, enter: ems-api-live-test.cfapps.eu10.hana.ondemand.com | The SAP Fiori launchpad displays. |  |
| 2 | Send Tenant Update | Choose Run / Send for SoapUI..Note The response will search for a unique tenant ID of the used Application with entitlement model Tenants. In case you get an error since you have multiple times the same tenant ID for the used application in different tenants, delete the other tenant entitlements still in the system from earlier tests, to be able to post the response successfully. |  |  |
| 3 | Log On | Log on to SAP Entitlement Management. | The SAP Fiori launchpad displays. |  |
| 4 | Access the App | Open Maintain Customer Entitlements app. |  |  |
| 5 | Select the Tenant Entitlement | Select the view Residential Tenants. | Tenant entitlements are shown, as well as the underlying master agreement entitlement. |  |
| 6 | View Tenant Capabilities Table | Choose the entitlement number for withEntitlement Model: TenantApplication: CAD ApplicationSystem Type: Productive SystemUnder General Data, review the Capability Table for an entry with Active status. |  |  |
| 7 | Repeat for other licenses for capabilities | Repeat steps 1 to 6 for below filters:Entitlement Model: TenantApplication: Collaboration ApplicationSystem Type: Productive System |  |  |

Productive System, CAD Application, Capability 2D Essentials

{
"processCode" : "5SW_Quick_Create_Update_Tenant_Capabilities_JS",
"businessEvent" : "NOS",
"refDocNo" : "",
"processParameter" : {
"Application" : "CAD",
"TenantID" : "CAD_10001_PRD",
"Operation" : "Append",
"CapabilityTable" : [ {
"Capability" : "CAD_2D_ES",
"Status" : "ACTIVE",
"Licensed" : true
} ]
}
}

Productive System, Collaboration Application, Capability Collaboration Basic

{
"processCode" : "5SW_Quick_Create_Update_Tenant_Capabilities_JS",
"businessEvent" : "NOS",
"refDocNo" : "",
"processParameter" : {
"Application" : "COLLAB",
"TenantID" : "COL_10001_PRD",
"Operation" : "Append",
"CapabilityTable" : [ {
"Capability" : "COLLAB_BAS",
"Status" : "ACTIVE",
"Licensed" : true
} ]
}
}

### Enter License Consumption in SAP Entitlement Management

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

For the licensed metrics, and application capabilities, the license consumption is entered in the productive system, to determine the balances between total licensed quantity, used quantity, and remaining quantity for each month.

For non cumulative licenses, like users, or licenses of specific capabilities, the consumption should be entered only once, after the last day of the month, using the last day of that month. For cumulative metrics, like documents, the usage could also be entered for the last day of the month, or for each day of the month, separately.

The consumption in this test case is entered manually, but in reality it would be entered by API by the underlying usage measurement system.

For licenses for specific capabilities, the entitlement quantity is 1, meaning that the capability has been licensed and can be used in the productive system. The respective consumption should be entered with 1 indicating that the capability has been used, or with 0 indicating that the capability has not been used, in the productive tenant.

If multiple subscription contracts for e.g. users or documents have been created adding entitlement quantities to a total entitlement quantity for a specific month, the total usage could just be entered for one of the valid entitlements of that day. In that case, the license balance would be determined by adding total licensed quantity, used quantity, and remaining quantity for that application, capability and metric, across all entitlements under that master agreement, e.g. using View Consumption Balance report downloaded to CSV, and then aggregated accordingly.

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to SAP Entitlement Management. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Maintain Customer Entitlements app. | The app is opened. |  |
| 3 | Select the license entitlement | Select the views Residential All | Tenant and license entitlements are shown, as well as the underlying master agreement entitlement. |  |
| 4 | Select entitlement | Choose the license entitlement withApplication: CAD ApplicationMetric: Users |  |  |
| 5 | Enter consumption | Choose tab Consumption.Choose Create.Enter consumed date, quantity, and metric, based on the table below.Choose Create.Choose Consumption Recalculate Period. | View for the current month, the calculated balance showing total amount, total consumed, and remaining. |  |
| 6 | Repeat | Repeat step 1 to 5 using the table below. |  |  |

| Application | Capability | Consumed Date | Quantity | Metric |
| --- | --- | --- | --- | --- |
| CAD Application |  | <Last day of this month> | 15 | Users |
| CAD Application |  | <Last day of this month> | 30 | Documents |
| CAD Application | CAD API Calls Get | <Last day of this month> | 60 | API Calls |
| CAD Application | CAD API Calls Post | <Last day of this month> | 40 | API Calls |
| CAD Application | CAD 2D Essentials | <Last day of this month> | 1 |  |
| Collaboration Application | Collaboration Basic | <Last day of this month> | 1 |  |

### Enter Software Usage and Adoption in SAP Entitlement Management

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

Software usage and adoptions enables entering usage and adoption data for each application tenant, in addition to the license usage data recorded earlier in the section license usage. For the application tenant overall, or for the licensed, or more detailed capabilities, for the licensed metrics, or additional metrics, the usage to be aggregated for a specific month can be entered into consumption records.

Below are the records for active users in the application tenant, including data for specific capabilities, the number of documents created per capability, and the frequency with which each capability was used within the application tenant. The test script outlines an example for productive tenants, but the same data can also be recorded in test tenants. This provides insights into live usage as well as usage in test systems for implementation across different software applications, tenants, and capabilities.

The consumption in this test case is entered manually, but in reality it would be entered by API by the underlying usage measurement system.

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to SAP Entitlement Management. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Maintain Customer Entitlements app. | The app is opened. |  |
| 3 | Select the license entitlement | Select the views Residential Tenants | Tenant entitlements are shown, as well as the underlying master agreement entitlement. |  |
| 4 | Select entitlement | Choose the entitlement withEntitlement Model: TenantApplication: CAD ApplicationSystem Type: Productive System |  |  |
| 5 | Enter consumption | Choose tab Consumption.Choose Create.Enter consumed date, quantity, and metric, based on the table below.Choose Create. |  |  |
| 6 | Repeat | Repeat step 1 to 5 using the table below. |  |  |

| Consumed Date | Capability | Metric | Quantity |
| --- | --- | --- | --- |
| <Last day of this month> |  | Active Users | 10 |
| <Last day of this month> | CAD_2D_ES | Active Users | 10 |
| <Last day of this month> | CAD_3D | Active Users | 2 |
| <Last day of this month> | CAD_2D_ES | Documents | 25 |
| <Last day of this month> | CAD_3D | Documents | 5 |
| <Last day of this month> | CAD_2D_ES | Count | 500 |
| <Last day of this month> | CAD_3D | Count | 80 |

Table 12: Entitlement with Type: Tenant, Application: Collaboration Application, System type: Productive System

| Consumed Date | Capability | Metric | Quantity |
| --- | --- | --- | --- |
| <Last day of this month> |  | Active Users | 5 |
| <Last day of this month> | COLLAB_BAS | Active Users | 5 |
| <Last day of this month> | COLLAB_BAS | Documents | 10 |
| <Last day of this month> | COLLAB_BAS | Count | 80 |

### Manage Subscription Billing

#### Display Active Subscription in SAP Subscription Billing

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The purpose of this step is to view the subscription in the Subscription Billing tenant and to verify the details.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad using the role Solution Order Specialist, if the subscription is created via a Solution Order. | The Fiori Launchpad is displayed. |  |
| 2 | Navigate to Manage Solution Orders | Open Manage Solution Orders (F4615) under Subscriptions and Billing catalog. | The Manage Solution Orders page is displayed. |  |
| 3 | Search for Solution Order | In the search area enter the Solution Order ID in the Solution Order field.Choose Go. | The solution order is displayed in the search result. |  |
| 4 | Open Solution Order | Choose the Solution Order from the result list. | Solution Order details are displayed on the Solution Order Page |  |
| 5 | View Progress | In the Solution Order, choose View Progress. | Solution Order Progress is displayed. |  |
| 6 | Navigate to Subscription | In the Solution Order Progress page, go to section Solution Order Progress.Choose the box with the Subscription.Choose icon Navigate to Transaction.Choose the subscription ID to navigate to the Subscription in SAP Subscription Billing.Note User can navigate to the subscription billing via the transaction history in Solution Order.Alternatively, log on to Subscription Billing > Manage Subscriptions and search for the created subscriptions using the Subscription ID. |  |  |
| 7 | Check Subscription Header Details | Check the following subscription header details at the top:Customer : 33100001Status: ActiveValid From: XXX XX, XXXXNote Note down the provider contract ID mentioned in the Processing data tab for further steps. | All the details are rightly available in Subscription Billing. |  |
| 8 | Check Provider Contract | Choose tab Processing Data.Choose the Provider Contract ID under Related Documents.Review the provider contract under General Data.Choose Items: General Data.Choose Item 1 – License.Double click the linked Billing Plan.Choose Plan Items.Choose Item 2 – Activation Fee.Double click the linked Billing Plan.Choose Plan Items.Choose Back.Choose Back.Choose Back. | Review the billing plan items for one time charge for the first month.Review the billing plan items for recurring charge, with monthly entries for the duration of the contract. |  |
| 9 | Check Subscription item details | In the Processing Data, check for the details like:Subscription ProfileRelated DocumentsSubscription DatesSnapshot DataIn the Item List, choose Subscription Item, to view the complete details of the transaction.Details like Billing, Subscription Parameters, Pricing can be viewed. | All the item details of the Subscription Item can be viewed. |  |

#### Display Provider Contract

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The purpose of this step is to view the provider contract created by Subscription and to verify the details.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad using the role Solution Order Specialist. | The Fiori Launchpad is displayed. |  |
| 2 | Navigate to Display Provider Contract for Sales Billing | Open Display Provider Contract for Sales Billing (FP_PC3) under Subscriptions and Billing catalog. | Provider Contract Display: Initial Screen is displayed. |  |
| 3 | Display Provider Contract | In Sales Billing Provider Contract enter the Provider Contract ID.Choose Continue.NoteProvider Contract can also be viewed from Subscription node in Solution Order Progress as described in Subscription Billing section.Provider Contract can also be viewed under Processing Data of each Subscription item created. | Details of the Provider Contract is displayed. |  |

#### Monitor Revenue Recognition (Event-Based): Provider Contracts

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The provider contract revenue can be reviewed, revenue recognition and be simulated, explained, and posted. Instead of posting revenue recognition here, revenue recognition posting can also be done by a batch job instead, as described in the next test process.

|  |
| --- |
| Note RA key assigned to provider contract for charge type recurring is PPCA-Provider Contracts 365 Days Calendar Yr-No cost deferred. So to view any data in this app, there must either be billing done for the contract and that would post deferred revenue, or execute the Run Revenue Recognition: Provider Contracts (Period-End Activity) step to accrue revenue if no billing is done. For charge type One time with RA key PPCN, there is no rev recognition. |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Cost Accountant - Sales. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Event-Based Revenue Recognition - Provider Contracts (F5406). | The Event Based Revenue Recognition - Provider Contracts screen displays. |  |
| 3 | Enter Selection Criteria | Make the following entries :Company Code: 3310Provider Contract: <Created in step Manage Subscription Billing>Contract Item: <leave this field blank>Revenue Recognition Key: PPCA, PPCN |  |  |
| 4 | Execute | Choose Go. | The provider contract items 1 (License) and 2 (One-Time Activation Fee) are shown. |  |
| 5 | View Details | Click on icon Navigation for Contract Item 1 (License) | The item has billed revenue, recognized revenue, and accrued revenue. |  |
| 6 | Revalue | Click on Revalue.Click on Simulate. | The simulation shows only recognized revenue. |  |
| 7 | Post | Click on Post. | Revenue recognition for the billing plan item was posted, and shows the revenue adjustment, recognized revenue, and accrued revenue. |  |
| 8 | Repeat | Repeat steps 5 to 7 for Item 2 (One-Time Activation Fee) | There is no accrued revenue, recognized revenue, or adjustment, since there is no forecast or billing plan available for One-Time Activation Fee. |  |

#### Manage Usage Records in SAP Subscription Billing

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The purpose of this step is to record the usage of APIs in Subscription Billing at the end of the Billing Period.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Subscription Specialist - Subscription Billing. | The Subscription Home page is displayed. |  |
| 2 | Access the SAP Fiori App | Open Manage Usage Records - Subscription Billing (F6802A) under Subscriptions and Billing catalog. | The list of available measured usage records are displayed. |  |
| 3 | Create Usage Records | Click on CreateNavigate to Header Info and enter the following data.Technical Resource Type: R-APITechnical Resource ID: XXX (Search for Technical Resource ID from the subscription created in earlier steps from Search help) |  |  |
| 4 | Record Usage | Navigate to General Info and enter the following data.Period Start: <first day of current month, 12:00:00 AM>Period End: <last day of current month, 12:00:00 AM>Quantity: <quantity> e.g. 60 EARate Subelement: Get |  |  |
| 5 | Save Usage Record | Click on Create |  |  |
| 6 | Repeat for Rate subelement Post | Repeat the same steps from Step 3 to 5 with the following data:Quantity: <quantity> e.g. 60 EARate Subelement: Post |  |  |

#### Display Pre-Bill in SAP Subscription Billing

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The purpose of this step is to view the Pre-Bill which gets generated in Subscription Billing at the end of the Billing Period.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad using the role Subscription Specialist - Subscription Billing. | Subscription Home page is displayed. |  |
| 2 | Open Bills | Open Manage Billing Data - Subscription Billing (F6803) under Subscriptions and Billing catalog. | The list of available bills is displayed. |  |
| 3 | Search for Bill Corresponding to Subscription | Enter the following search criteria and Choose Go:Transfer Status: Not TransferredCustomer: 33100001Markets: | The bill corresponding to the subscription is displayed. |  |
| 4 | View the Bill details | In the Bills (XX) table the following details can be viewed:Bill Status: X days until closedTransfer Status: Not Transferred | Bill details are displayed. |  |
| 5 | Check Bill Items and Charge Details of the Bill Item | Choose Bill Item under Item List to view the details of the Bill List Item.Bill Item and Charge Details can be viewed:Product ID: P-CAD-BRONZE/ P-CAD-API product for Pricing SchemesNet Bill Amount: example 2100 AED | Bill Item and Charge Details are displayed. |  |
| 6 | Close Bill to prepare for transfer | Choose Change Status and Choose Close Bill Immediately.Choose Close Bill in the Warning dialog box.Bill Status changes to Manually Closed. | Bill Status changed to Manually Closed. |  |
| 7 | Display and Verify Billing Doc Request | Verify if the Transfer Status is changed to Transferred and the Billing Document request ID is created under the Transfer tab as Successor Documents.In the Billing Doc Request section, Choose Node Details to view the Document ID.Note Make a note of Document ID. User can also navigate to S4 HANA via the Subscription Billing Document Request under Transfer (Successor Documents). | Billing Document request ID is displayed. |  |

### Manage Billing Document in SAP S/4HANA Cloud

#### Create Billing Document

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity the billing clerk creates an invoice for the solution order items that was released for billing in the previous step. The billing document is created by the billing clerk.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Billing Clerk. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Create Billing Documents (F0798). | The Create Billing Documents screen displays. |  |
| 3 | Define Billing Settings | Choose Billing Settings in the bottom bar, you can make the following settings as below and Choose OK:Set billing date and type before billing: ONCreate separate billing document for each item of billing due list: OFFAutomatically post billing documents: ONDisplay billing documents after creation: ON | The Billing Settings dialog window is displayed.You have maintained the required settings for billing. |  |
| 4 | Search for billing due list | In search filters , provide the Document ID in SD Document field.Choose Go. | All billing due list items belonging to Solution order should be displayed. |  |
| 5 | Select item(s) for billing | Select row(s) of SD Document created previously and choose button Create Billing Documents.Note It is possible to combine all the items in the solution order and create a single invoice, at the same time individual invoice can be created for different items in solution order by choosing the individual billing due list items. | The Create Billing Document pop up is displayed. |  |
| 6 | Maintain Billing Date | Choose Billing Type Invoice (F2) and maintain Billing Date, for example current date, then press button OK. | The draft billing document with ID TMPxxxxxxx displays. |  |
| 7 | Save Billing Document | On the Manage Billing Documents screen, choose Save.Invoice ID xxxxxxxx is displayed , make a note of Invoice ID.Note In case the Billing Due List cannot be combined into a single invoice a Split Analysis button will be displayed. In that case you will have to create individual billing documents. | The system generates an invoice for billing. Billing status of the individual items in the Solution order is updated. |  |

#### Display Billing Document

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step displays the sales order billing document.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Billing Clerk. | The Fiori Launchpad is displayed. |  |
| 2 | Access the App | Open Manage Billing Documents (F0797). | The Manage Billing Documents screen is displayed. |  |
| 3 | Search the Billing Document Created in Previous Step | Enter <the Billing document number recorded in Create Billing Document step>.Choose Go.Select the line with the billing document and click on Display. | The billing document is displayed.The items section shows the lines for “One-Time Activation Fee” and “License”. |  |
| 4 | Display Pricing Data | Click on tab Pricing Elements. | Condition type PMP1 shows the one time activation fee.Condition type ZMP2 shows the total recurring fee (statistical).Condition type ZP21 shows the percentage and condition value split to a different accountCondition type ZP2B shows the delta of ZMP2 and ZP21, remaining on the standard account. |  |
| 5 | Display the Process Flow | Click on tab Process Flow.Copy the Journal Entry ID for the next test process. |  |  |

#### Display Journal Entry Analyzer

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step displays the Journal Entry document.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a General Ledger Accountant. | The Fiori Launchpad is displayed. |  |
| 2 | Access the App | Open Journal Entry Analyzer (FIS_FPM_OVP_JEANA (FIS_FPM_OVP_JEANA)). | The Journal Entry Analyzer screen is displayed. |  |
| 3 | Search the Journal Entry Document created in previous step | Enter the following :Ledger: 0LCompany Code: 3310Journal Entry: <Number noted from previous stepChoose Go. | The billing document is displayed.The items section shows the lines for “Activation” and “License”. |  |
| 4 | Display the Product Area in the Journal Entry | In the navigation panel, enter Product Area in the entry field Search Dimensions, Enter.Under Available Fields, select the icon (Add field Product Area to rows axis) available next to Product Area.In the navigation panel, enter Product Sold in the entry field Search Dimensions, Enter.Under Available Fields, select the icon (Add field Product Sold to rows axis) available next to Product Sold. | The journal entry analyzer that the revenue for account 41910000 (Billed Revenue Domestic) was assigned to Product Area 01_CAD, and that the revenue split to account 41910001 (Rev Licenses Split 1), was assigned to Product Area 02_COLLAB. |  |

### Manage Revenue Recognition

#### Monitor Revenue Recognition (Event-Based): Provider Contracts

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The provider contract revenue can be reviewed, revenue recognition and be simulated, explained, and posted. Instead of posting revenue recognition here, revenue recognition posting can also be done by a batch job instead, as described in the next test process.

|  |
| --- |
| Note RA key assigned to provider contract for charge type recurring is PPCA-Provider Contracts 365 Days Calendar Yr-No cost deferred. So to view any data in this app, there must either be billing done for the contract and that would post deferred revenue, or execute the Run Revenue Recognition: Provider Contracts (Period-End Activity) step to accrue revenue if no billing is done. For charge type One time with RA key PPCN, there is no rev recognition. |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Cost Accountant - Sales. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Event-Based Revenue Recognition - Provider Contracts (F5406). | The Event Based Revenue Recognition - Provider Contracts screen displays. |  |
| 3 | Enter Selection Criteria | Make the following entries :Company Code: 3310Provider Contract: <Created in step Manage Subscription Billing>Contract Item: <leave this field blank>Recognition Key: PPCA, PPCN |  |  |
| 4 | Execute | Choose Go. | The provider contract items 1 (License) and 2 (One-Time Activation Fee) are shown. |  |
| 5 | View Details | Click on icon Navigation for contract item 1 (License) | The item has billed revenue, recognized revenue, and accrued revenue. |  |
| 6 | Revalue | Click on Revalue.Click on Simulate. | The simulation shows only recognized revenue, |  |
| 7 | Explain Simulation (Optional) | Click on Explain Simulation. | The detailed steps of the revenue recognition simulation are shown. |  |

#### Run Revenue Recognition: Provider Contracts (Period-End Activity)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you run the event-based revenue recognition for provider contracts.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Cost Accountant - Sales. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Run Revenue Recognition - Provider Contracts (F5405). | The Application Jobs view displays. |  |
| 3 | New Job | Choose the Create button. | The New Job view displays. |  |
| 4 | Enter Selection Criteria | Make the following entries and choose the Schedule button:Job Template: Run Revenue Recognition – Provider ContractsJob Name: <Enter a description or leave the default description>Choose Step 2.Start Immediately: <checked>Choose Step 3.To Fiscal Period/Year: <mm.yyyy>Company Code: 3310Ledger: 0LProvider Contract: <Created in step Manage Subscription Billing>Contract Item: <leave this field blank>Sales Organization: 3310Division: <leave this field blank>Distribution Channel: <leave this field blank>Simulation: <deselect the checkbox> | The new job is executed. |  |
| 5 | Show Results | Click on icon Navigate to the Job Log.Click on icon Results. |  |  |

#### Manage Real-Time Revenue Recognition Issues – Provider Contracts

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

During cost or revenue posting on the cost object, errors that stop real time revenue postings can occur. This activity allows you to review these posting entries where no corresponding real time revenue recognition posting exists and make the necessary corrections. All errors must be addressed prior to the month end revenue recognition month end process.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Cost Accountant - Sales. |  |  |
| 2 | Access the App | Open Manage Revenue Recognition Issues - Provider Contracts (F5407) . |  |  |
| 3 | Enter Selection Criteria | Make the following entries and choose Go:To Fiscal Period/Year: <PPP.YYYY>Company Code: 3310Ledger: 0LNote Choose the Adapt Filters button for any additional filter criteria choose Go. | No data found indicates that there are no issues. If issues are shown, review and process corrections.Tip To download the issue list, make your filter selections and select Show Error Summary. From the list, you can choose the Download button. |  |

### Change Processes

This section describes test procedures for each process step that belongs to this scope item. In this chapter, the focus is on change processes from SAP S/4HANA Cloud Public Edition solution order, to subscription contracts in SAP subscription billing, and the related entitlement provisioning and decommissioning in SAP Entitlement Management without describing the test flow creating billing documents from SAP Subscription Billing to SAP S/4HANA Cloud.

#### Separate CAD Subscription for a the Commercial Division of the Customer

##### Create Solution Order

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This step describes how to create a new solution order for a “Commercial” division of the architecture customer using Master Agreement “COM”, so that the commercial division has a separate solution order, subscription contract, entitlements for tenants and licenses from the residential division using Master Agreement “RES” from the previous chapters.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad using the role Solution Order Specialist. | The Fiori Launchpad with access to the Manage Solution Orders application is displayed. |  |
| 2 | Open Manage Solution Orders application | Open Manage Solution Orders (F4615). | The Manage Solution Orders screen is displayed. |  |
| 3 | Create Solution Order | Choose Create from the solution order list page. | Create Solution Order window is displayed. |  |
| 4 | Maintain Solution Order data | Enter the following data to create a solution order:Description: <your description>External Reference: <your reference>Sold-To Party: for example, 33100001 for AE (Domestic UAE Customer 1)Note Select the sales organization (for example, 3310) and Contact person from the pop-up appears. | Required header data for the Solution order has been maintained. |  |
| 5 | Maintain Master Agreement | Under Solution Order Details – Additional Data, maintain master agreement: for example, COMNote Make sure that all entitlements for that master agreement have been deleted from previous tests in SAP Entitlement Management.Note If no master agreement is entered either here in the solution order header, or in the solution order item in section Subscription Billing Item Details, the master agreement maintained in chapter Maintain Standard Master Agreement for Customer in SAP Subscription Billing will be added in SAP Cloud Integration as the master agreement to use. |  |  |
| 6 | Add Item P-CAD-BRONZE | Maintain the following Item in the solution order under Items tab:Product ID: P-CAD-BRONZEQuantity: 1Choose Enter.Click on Action(Edit) icon.Under Subscription Parameters, enter the following:Parameter ID: R-LICENSEValue: 10In the Subscription Terms section enter the following:Contract Start Date: <First Day of Current Month minus 9 months> | The subscription item is now added to Solution Order. |  |
| 7 | Adjust Contract Standard Duration | Activate check box Overwrite Default Terms.Set Fixed Term to 11 months.Click on Simulate to simulate the Pricing and Contract Duration.Click on Apply.Check the Net Value of line item 10. | The subscription item is now added to Solution Order. |  |
| 8 | Release Items and Save Solution Order | Click on Release All Items under Items and Click on Save.Click on Refresh.Navigate to Transaction History.On clicking on the Transaction number, you can directly navigate to SAP Subscription Billing.Note User can navigate to the subscription billing via the transaction history in Solution Order. Alternatively, log on to Subscription Billing > Manage Subscriptions and search for the created subscriptions using the Subscription ID.Check in the Contract ItemCheck one-time price, Recurring Net Charge/ Month, Usage Based Net Charges / Month | On release the items are replicated as Subscription Contract to SAP Subscription Billing and also different entitlements in SAP Entitlement Management will be created. |  |

##### Display Pending Subscription in SAP Subscription Billing

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The purpose of this step is to view the subscription in the Subscription Billing tenant and to verify the details.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad using the role Solution Order Specialist, if the subscription is created via a Solution Order. | The Fiori Launchpad is displayed. |  |
| 2 | Navigate to Manage Solution Orders | Open Manage Solution Orders (F4615). | The Manage Solution Orders screen is displayed. |  |
| 3 | Search for Solution Order | In the search area enter the Solution Order ID in the Solution Order field.Choose Go. | The solution order is displayed in the search result. |  |
| 4 | Open Solution Order | Choose the solution order from the result list. | Solution Order details is displayed in the Display Solution Order Page. |  |
| 5 | View Progress | In the Solution Order, choose View Progress. | The Solution Order Progress screen is displayed. |  |
| 6 | Navigate to Subscription | In the Solution Order Progress. go to section Solution Order Progress.Choose the box with the Subscription.Choose icon Navigate to Transaction.Choose the Subscription ID to navigate to the Subscription in SAP Subscription BillingNote User can navigate to the subscription billing via the transaction history in Solution Order.Alternatively, log on to Subscription Billing > Subscriptions and search for the created subscriptions using the Subscription ID. |  |  |
| 7 | Check Subscription Header Details | Check the following subscription header details at the top:Customer: 33100001Status: PendingValid From: XXX XX, XXXXExpires On: XXX XX, XXXX | All the details are rightly available in Subscription Billing. |  |
| 8 | Check Subscription item details | In the Processing Data, check for the details like:Subscription ProfileRelated DocumentsSubscription DatesSnapshot DataIn the Item List, choose Subscription Item, to view the complete details of the transaction.Details like Billing, Subscription Parameters, Pricing can be viewed. | All the item details of the Subscription Item can be viewed. |  |

##### Display Entitlements in SAP Entitlement Management

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

Use the Maintain Customer Entitlements app to view and manage entitlements. Using this app, you can create, view, edit, split, change status, reassign (move) folders of entitlement records, or export a filtered Entitlements List.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to SAP Entitlement Management. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Maintain Customer Entitlements app. | APP is opened. |  |
| 3 | Select the Tenant and the License Entitlement | Select the views Commercial Tenants and then Commercial Licenses.Click on Go. | Tenant and license entitlements are shown, as well as the underlying master agreement entitlement. |  |
| 4 | Capability and Quantity Check | Check the details of the respective entitlements. |  |  |
| 5 | Check related subscription | If desired, to navigate to the subscription for a specific entitlement, click on the highlighted number for column “reference document”. | The subscription is shown. |  |

##### Background Job to Trigger Provisioning

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

To send the message from the provisioning process to the provisioning system, the background job “5SW Send Provisioning Request” has to be triggered, as described below.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to SAP Entitlement Management. | The SAP Fiori Launchpad displays. |  |
| 2 | Access the App | Open Monitor Background Job Logs app |  |  |
| 3 | Execution of the job | Choose job name 5SW Send Provisioning Request.Choose Execute and choose Confirm. | Job is selected and executed. Wait for message: “Job has been executed, please go to the “JOB LOGS” section to refresh and see the latest job logs”. |  |
| 4 | Refresh | Refresh JOB LOGS and look at the provisioning requests. | Check the sent provisioning request to the provisioning system. |  |

##### Send Response for the Tenant Provisioning Requests

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

After the different provisioning request has been sent to the provisioning system, the provisioning of the tenants is performed by the provisioning system. After completion, the provisioning system sends a response to SAP Entitlement Management. The test description below describes how to manually test that response, using SAP Business Accelerator Hub (aka API Hub) / SoapUI.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to SAP Entitlement Management. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Maintain Customer Entitlements app. |  |  |
| 3 | Select the Tenant Entitlement | Select the view Commercial Tenants. | Tenant entitlements are shown, as well as the underlying master agreement entitlement. |  |
| 4 | View Provisioning Process and copy TaskExecutionLogGuid | Choose the entitlement number withEntitlement Model: Tenant PhaseApplication: CAD ApplicationSystem Type: Productive SystemChoose View Phase Detail under Phase section.Choose tab Provision.Choose Expand.Note down the Process Log ID.Choose the Process Log ID.Choose Send Provisioning Request.Choose the icon in the middle, View Log.On pop-up window Send Provisioning Request, choose the Message Log ID.On window Communication Messages, choose the icon under Payload.On pop-up Payload, click anywhere in the window, then press CTRL-F.In the search window, enter the Process Log ID noted down earlier and click on Enter.Double click on the field behind TaskExecutionLogGuid above your process log ID, and press CTRL-C to copy it. |  |  |
| 5 | Prepare the provisioning response on SAP Business Accelerator Hub / SoapUI | Launch:[https://api.sap.com/api/SAP_CF_EMS_Provisioning_Process/tryout](https://api.sap.com/api/SAP_CF_EMS_Provisioning_Process/tryout), and select the environment you created in chapter Prepare SAP Business Accelerator Hub to test the SAP Entitlement Management Provisioning Response.For SoapUI, select the project you created in chapter Prepare SoapUI to test the SAP Entitlement Management Provisioning Response (Optional)Choose the Body tab.Click in the area below the example payload, click Enter, and click CTRL+V to insert the copied TaskExecutionLogGuid.Replace the example payload with the payload below, for the application and system type.Double click on the TaskExecutionLogGuid, click CTRL+X, then double click on GUID, then click CTRL+V to insert the Guid.Note Workaround for specific URL:If the URL provided in SAP Entitlement Management starts with [https://ems-api-ext.cfapps.eu10-005.hana.ondemand.com/](https://ems-api-ext.cfapps.eu10-005.hana.ondemand.com/), then do the following:Choose the Headers tab.Choose Add New Header.In the drop down box, select Host.In field value, Enter: ems-api-live-test.cfapps.eu10.hana.ondemand.com |  |  |
| 6 | Send Provisioning Response | Choose Run/ Choose Send for SoapUI.. | The response body outlines that the response was sent successfully. |  |
| 7 | Return to app Maintain Customer Entitlements | On pop up Payload, choose Close and choose Back. | The tenant provisioning process has status Completed. |  |
| 8 | Return to Entitlements Tenants Overview | Choose Back.Choose Back.In Maintain Customer Entitlements, choose View Commercial Tenants. | The entitlement for tenant phases and tenants for application CAD and system type Productive System have status Active.The tenant entitlement shows the Tenant ID, Tenant Name, Tenant URL based on the provisioning feedback. |  |
| 9 | Repeat for other licenses | Repeat steps 4 to 8 using the payload belowApplicationSystem TypeCAD ApplicationTest SystemCollaboration ApplicationProductive SystemCollaboration ApplicationTest System |  |  |

Payload for CAD Productive Tenant

[ {
"taskExecutionLogGuid" : "GUID",
"response" : {
"Tenant_URL" : "http://fivestar.prod.cad.com",
"Tenant_ID" : "CAD_10003_PRD",
"Tenant_Status" : "ACTIVE",
"Tenant_Name" : "AE1 COM CAD PROD"
}
} ]

Payload for CAD Test Tenant

[ {
"taskExecutionLogGuid" : "GUID",
"response" : {
"Tenant_URL" : "http://fivestar.test.cad.com",
"Tenant_ID" : "CAD_10004_TST",
"Tenant_Status" : "ACTIVE",
"Tenant_Name" : "AE1 COM CAD TEST"
}
} ]

Payload for Collaboration Productive Tenant

[ {
"taskExecutionLogGuid" : "GUID",
"response" : {
"Tenant_URL" : "http://fivestar.prod.collab.com ",
"Tenant_ID" : "COL_10003_PRD",
"Tenant_Status" : "ACTIVE",
"Tenant_Name" : "AE1 COM COLLAB PROD"
}
} ]

Payload for Collaboration Test Tenant

[ {
"taskExecutionLogGuid" : "GUID",
"response" : {
"Tenant_URL" : "http://fivestar.test.collab.com ",
"Tenant_ID" : "COL_10004_TST",
"Tenant_Status" : "ACTIVE",
"Tenant_Name" : "AE1 COM COLLAB TEST"
}
} ]

##### Send Response for the License Provisioning Requests

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

After the different provisioning requests for tenants has been sent to the provisioning system, the provisioning of the licenses for the new contract is performed by the provisioning system. After completion, the provisioning system sends a response to SAP Entitlement Management. The test description below describes how to manually test that response, using SAP Business Accelerator Hub (aka API Hub) / SoapUI.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to SAP Entitlement Management. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Maintain Customer Entitlements app. |  |  |
| 3 | Select the License Entitlement | Select the view Commercial Licenses. | License entitlements are shown, as well as the underlying master agreement entitlement. |  |
| 4 | View Provisioning Process and copy TaskExecutionLogGuid | Choose the entitlement number withEntitlement Model: LicenseApplication: CAD ApplicationMetric: UsersChoose tab Provision.Choose Expand for SI 5SW License ProvisioningNote down the Process Log ID.Choose the Process Log ID.Choose License Provisioning Request.Choose the icon in the middle, View Log.On pop-up window License Provisioning Request, choose the Message Log ID.On window Communication Messages, choose the icon under Payload.On pop-up Payload, click anywhere in the window, then press CTRL-F.In the search window, enter the Process Log ID noted down earlier and click on Enter.Double click on the field behind TaskExecutionLogGuid above your process log ID, and press CTRL-C to copy it. |  |  |
| 5 | Prepare the provisioning response on SAP Business Accelerator Hub / SoapUI | Launch:[https://api.sap.com/api/SAP_CF_EMS_Provisioning_Process/tryout](https://api.sap.com/api/SAP_CF_EMS_Provisioning_Process/tryout), and select the environment you created in chapter Prepare SAP Business Accelerator Hub to test the SAP Entitlement Management Provisioning Response.For SoapUI, select the project you created in chapter Prepare SoapUI to test the SAP Entitlement Management Provisioning Response (Optional)Choose the Body tab.Click in the area below the example payload, click Enter, and click CTRL+V to insert the copied TaskExecutionLogGuid.Replace the example payload with the payload below, for the application and system type.Double click on the TaskExecutionLogGuid, click CTRL+X, then double click on GUID, then click CTRL+V to insert the GuidNote Workaround for specific URL:If the URL provided in SAP Entitlement Management starts with [https://ems-api-ext.cfapps.eu10-005.hana.ondemand.com/](https://ems-api-ext.cfapps.eu10-005.hana.ondemand.com/), then do the following:Choose the Headers tab.Choose Add New Header.In the drop down box, select Host.In field value, Enter: ems-api-live-test.cfapps.eu10.hana.ondemand.com |  |  |
| 6 | Send Provisioning Response | Choose Run / Send for SoapUI. | The response body outlines that the response was sent successfully. |  |
| 7 | Return to app Maintain Customer Entitlements | On pop up Payload, choose Close and choose Back. | The license provisioning process has status Completed. |  |
| 8 | Return to Entitlements License Overview | Choose Back.In Maintain Customer Entitlements, choose View Commercial Licenses. | The entitlement for license with application CAD Application and metric Users has status Active. |  |
| 9 | Repeat for other licenses | Repeat steps 4 to 8 using the payload belowApplicationCapabilityMetricQuantityCAD ApplicationDocumentsCAD ApplicationCAD 2D EssentialsCollaboration ApplicationCollaboration Basic |  |  |

Payload for CAD Users License

[ {
"taskExecutionLogGuid" : "GUID",
"response" : {
"Capability_ID" : "",
"Capability_Active" : true,
"Application" : "CAD",
"Quantity" : 10
}
} ]

Payload for CAD Documents Licenses

[ {
"taskExecutionLogGuid" : "GUID",
"response" : {
"Capability_ID" : "",
"Capability_Active" : true,
"Application" : "CAD",
"Quantity" : 30
}
} ]

Payload for CAD 2D Essentials

[ {
"taskExecutionLogGuid" : "GUID",
"response" : {
"Capability_ID" : "CAD_2D_ES",
"Capability_Active" : true,
"Application" : "CAD",
"Quantity" : 1
}
} ]

Payload for Collaboration Basic

[ {
"taskExecutionLogGuid" : "GUID",
"response" : {
"Capability_ID" : "COLLAB_BAS",
"Capability_Active" : true,
"Application" : "COLLAB",
"Quantity" : 1
}
} ]

##### Display Active Subscription in SAP Subscription Billing

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The purpose of this step is to view the subscription in the Subscription Billing tenant and to verify the details.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad using the role Solution Order Specialist, if the subscription is created via a Solution Order. | The Fiori Launchpad is displayed. |  |
| 2 | Navigate to Manage Solution Orders | Open Manage Solution Orders (F4615) under Subscriptions and Billing catalog. | The Manage Solution Orders page is displayed. |  |
| 3 | Search for Solution Order | In the search area enter the Solution Order ID in the Solution Order field.Choose Go. | The solution order is displayed in the search result. |  |
| 4 | Open Solution Order | Choose the solution order from the result list. | Solution Order details are displayed on the Display Solution Order Page |  |
| 5 | View Progress | In the Solution Order, choose View Progress. | Solution Order Progress is displayed. |  |
| 6 | Navigate to Subscription | In the Solution Order Progress. go to section Solution Order Progress.Choose the box with the Subscription.Choose icon Navigate to Transaction.Choose the subscription ID to navigate to the Subscription in SAP Subscription Billing.Note User can navigate to the subscription billing via the transaction history in Solution Order.Alternatively, log on to Subscription Billing > Manage Subscriptions and search for the created subscriptions using the Subscription ID. |  |  |
| 7 | Check Subscription Header Details | Check the following subscription header details at the top:Customer : 33100001Status: ActiveValid From: XXX XX, XXXXNote Note down the provider contract ID mentioned in the Processing data tab for further steps. | All the details are rightly available in Subscription Billing. |  |
| 8 | Check Provider Contract | Choose tab Processing Data.Choose the Provider Contract ID under Related Documents.Review the provider contract General Data.Choose Items: General Data.Choose Item 1 – License.Double click the linked Billing Plan.Choose Plan Items.Choose Item 2 – Activation Fee.Double click the linked Billing Plan.Choose Plan Items.Choose Back.Choose Back.Choose Back. |  |  |
| 9 | Check Subscription item details | In the Processing Data , check for the details like:Subscription ProfileRelated DocumentsSubscription DatesSnapshot DataIn the Item List, choose Subscription Item, to view the complete details of the transaction.Details like Billing, Subscription Parameters, Pricing can be viewed. | All the item details of the Subscription Item can be viewed. |  |

##### Send Tenant Capability Update

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

After completing license provisioning, which activated a specific capability, the provisioning system sends a call to SAP Entitlement Management, to updated the enabled license capabilities in the tenant entitlement.

Based on that, the tenant entitlement acts as the “Digital Twin” of the real system tenant, showing in a table attribute of the tenant entitlement for a specific tenant, which capabilities have been licensed and are currently enabled in that tenant.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Prepare the entitlement update on SAP Business Accelerator Hub/ SoapUI | Launch: [https://api.sap.com/api/SAP_CF_EMS_Entitlement_Process_Quick_Update/tryout](https://api.sap.com/api/SAP_CF_EMS_Entitlement_Process_Quick_Update/tryout) and select the environment you created in chapter Prepare SAP Business Accelerator Hub to test the SAP Entitlement Management Provisioning Response.For SoapUI, select the project you created in chapter Prepare SoapUI to test the SAP Entitlement Management Provisioning Response (Optional)Choose the Body tab.Replace the example payload with the payload below.Note Workaround for specific URL:If the URL provided in SAP Entitlement Management starts with [https://ems-api-ext.cfapps.eu10-005.hana.ondemand.com/](https://ems-api-ext.cfapps.eu10-005.hana.ondemand.com/): Choose the Headers tab and choose Add New Header. In the drop down box, select Host. In field value, enter: ems-api-live-test.cfapps.eu10.hana.ondemand.com |  |  |
| 2 | Send Tenant Update | Choose Run / Choose Send for SoapUI.Note The response will search for a unique tenant ID of the used Application with entitlement model Tenants. In case you get an error since you have multiple times the same tenant ID for the used application in different tenants, delete the other tenant entitlements still in the system from earlier tests, to be able to post the response successfully. |  |  |
| 3 | Log on | Log on to SAP Entitlement Management. |  |  |
| 4 | Access the app | Open Maintain Customer Entitlements app. |  |  |
| 5 | Select the Tenant Entitlement | Select the view Commercial Tenants. |  |  |
| 6 | View Tenant Capabilities Table | Choose the entitlement with the following details:Entitlement Model: TenantApplication: CAD ApplicationSystem Type: Productive SystemUnder General Data, review the capability table with activated and licensed capabilities in the productive tenant is shown. |  |  |
| 7 | Repeat for other licenses for capabilities. | Repeat steps 1 to 6 for the below filters:Entitlement Model: TenantApplication: Collaboration ApplicationSystem Type: Productive SystemCapability: Collaboration Basic |  |  |

Productive System, Tenant, CAD Application, Capability 2D Essentials

{
"processCode" : "5SW_Quick_Create_Update_Tenant_Capabilities_JS",
"businessEvent" : "NOS",
"refDocNo" : " ADD_CAP_001",
"processParameter" : {
"Application" : "CAD",
"TenantID" : "CAD_10003_PRD",
"Operation" : "Append",
"CapabilityTable" : [ {
"Capability" : "CAD_2D_ES",
"Status" : "ACTIVE",
"Licensed" : true
} ]
}
}

Productive System, Tenant, Collaboration Application, Capability Collaboration Basic

{
"processCode" : "5SW_Quick_Create_Update_Tenant_Capabilities_JS",
"businessEvent" : "NOS",
"refDocNo" : " ADD_CAP_001",
"processParameter" : {
"Application" : "COLLAB",
"TenantID" : "COL_10003_PRD",
"Operation" : "Append",
"CapabilityTable" : [ {
"Capability" : "COLLAB_BAS",
"Status" : "ACTIVE",
"Licensed" : true
} ]
}
}

#### Change Subscription – Number of Users

##### Change Number of Users in SAP Subscription Billing

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The customer wants to increase the number of users in the subscription after the initial contract was booked.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad using the role Subscription Specialist - Subscription Billing. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Subscriptions (F6801). |  |  |
| 3 | Execution of the job name | Choose the subscription from the previous chapter.Navigate to Item List tab and choose Edit Items.In Effective From, enter <First Day of Current Month minus 9 months>.Choose Confirm.Choose Navigate to display the Item Details.Under Subscription Parameters, change the quantity under R-License from 10 to 20.Choose Apply.Choose Save. |  |  |

##### Display Entitlements in SAP Entitlement Management

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

Use the Maintain Customer Entitlements app to view and manage entitlements. Using this app, you can create, view, edit, split, change status, reassign (move) folders of entitlement records, or export a filtered Entitlements List.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to SAP Entitlement Management. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Maintain Customer Entitlements app. | APP is opened. |  |
| 3 | Select the Tenant and the License Entitlement | Select the views Commercial Tenants and then Commercial Licenses.Click on Go. | Tenant and license entitlements are shown, as well as the underlying master agreement entitlement. |  |
| 4 | Capability and Quantity Check | Check the details of the respective entitlements. |  |  |
| 5 | Check related subscription | If desired, to navigate to the subscription for a specific entitlement, click on the highlighted number for column “reference document”. | The subscription is shown. |  |

##### Background Job to Trigger Provisioning

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

To send the message from the provisioning process to the provisioning system, the background job “5SW Send Provisioning Request” has to be triggered, as described below.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to SAP Entitlement Management. | The SAP Fiori Launchpad displays. |  |
| 2 | Access the App | Open Monitor Background Job Logs app |  |  |
| 3 | Execution of the job | Choose job name 5SW Send Provisioning Request.Choose Execute and choose Confirm. | Job is selected and executed. Wait for message: “Job has been executed, please go to the “JOB LOGS” section to refresh and see the latest job logs”. |  |
| 4 | Refresh | Refresh and look at the provisioning requests. | Check the sent provisioning request to the provisioning system. |  |

##### Send Response for the License Provisioning Requests

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

After the different provisioning requests for tenants has been sent to the provisioning system, the provisioning of the licenses for the new contract is performed by the provisioning system. After completion, the provisioning system sends a response to SAP Entitlement Management. The test description below describes how to manually test that response, using SAP Business Accelerator Hub (aka API Hub) / SoapUI.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to SAP Entitlement Management. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Maintain Customer Entitlements app. |  |  |
| 3 | Select the License Entitlement | Select the view Commercial Licenses. | License entitlements are shown, as well as the underlying master agreement entitlement. |  |
| 4 | View Provisioning Process and copy TaskExecutionLogGuid | Choose the entitlement number withEntitlement Model: LicenseApplication: CAD ApplicationMetric: UsersChoose tab Provision.Choose Expand for SI 5SW License ProvisioningNote down the Process Log ID.Choose the Process Log ID.Choose License Provisioning Request.Choose the icon in the middle, View Log.On pop-up window License Provisioning Request, choose the Message Log ID.On window Communication Messages, choose the icon under Payload.On pop-up Payload, click anywhere in the window, then press CTRL-F.In the search window, enter the Process Log ID noted down earlier and click on Enter.Double click on the field behind TaskExecutionLogGuid above your process log ID, and press CTRL-C to copy it. |  |  |
| 5 | Prepare the provisioning response on SAP Business Accelerator Hub / SoapUI | Launch:[https://api.sap.com/api/SAP_CF_EMS_Provisioning_Process/tryout](https://api.sap.com/api/SAP_CF_EMS_Provisioning_Process/tryout), and select the environment you created in chapter Prepare SAP Business Accelerator Hub to test the SAP Entitlement Management Provisioning Response.For SoapUI, select the project you created in chapter Prepare SoapUI to test the SAP Entitlement Management Provisioning Response (Optional)Choose the Body tab.Click in the area below the example payload, click Enter, and click CTRL+V to insert the copied TaskExecutionLogGuid.Replace the example payload with the payload below, for the application and system type.Double click on the TaskExecutionLogGuid, click CTRL+X, then double click on GUID, then click CTRL+V to insert the GuidNote Workaround for specific URL:If the URL provided in SAP Entitlement Management starts with [https://ems-api-ext.cfapps.eu10-005.hana.ondemand.com/](https://ems-api-ext.cfapps.eu10-005.hana.ondemand.com/), then do the following:Choose the Headers tab.Choose Add New Header.In the drop down box, select Host.In field value, Enter: ems-api-live-test.cfapps.eu10.hana.ondemand.com |  |  |
| 6 | Send Provisioning Response | Choose Run / Send for SoapUI. | The response body outlines that the response was sent successfully. |  |
| 7 | Return to app Maintain Customer Entitlements | On pop up Payload, choose Close and choose Back. | The license provisioning process has status Completed. |  |
| 8 | Return to Entitlements License Overview | Choose Back.In Maintain Customer Entitlements, choose View Commercial Licenses. | The entitlement for license with application CAD Application and metric Users has status Active. |  |
| 9 | Repeat for other licenses | Repeat steps 4 to 8 using the payload belowApplicationCapabilityMetricCAD ApplicationDocuments |  |  |

Payload for CAD Users License

[ {
"taskExecutionLogGuid" : "GUID",
"response" : {
"Capability_ID" : "",
"Capability_Active" : true,
"Application" : "CAD",
"Quantity" : 20
}
} ]

Payload for CAD Documents Licenses

[ {
"taskExecutionLogGuid" : "GUID",
"response" : {
"Capability_ID" : "",
"Capability_Active" : true,
"Application" : "CAD",
"Quantity" : 60
}
} ]

#### Change Subscription – Extend Subscription Duration

##### Extend Subscription End Date in SAP Subscription Billing

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The customer wants to extend the subscription, initially booked for 11 months, by 1 month to 12 months.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad using the role Subscription Specialist - Subscription Billing. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Subscriptions (F6801). | App is displayed. |  |
| 3 | Execution of the job name | Activate the check box on the left side of the Subscription list for the Subscription from the previous chapter.Choose Mass Changes, then Extend.Under Extension, enter 1 MonthsChoose Extend Subscriptions. | Subscriptions changed. |  |

##### Display Entitlements in SAP Entitlement Management

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

Use the Maintain Customer Entitlements app to view and manage entitlements. Using this app, you can create, view, edit, split, change status, reassign (move) folders of entitlement records, or export a filtered Entitlements List.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to SAP Entitlement Management. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Maintain Customer Entitlements app. | APP is opened. |  |
| 3 | Select the Tenant and the License Entitlement | Select the views Commercial Tenants and then Commercial Licenses.Click on Go. | The tenant and tenant phase entitlements are still Active. All license entitlements have now status In Preparation, since the end date of all of them has changed. |  |
| 4 | Capability and Quantity Check | Check the details of the respective entitlements. |  |  |
| 5 | Check related subscription | If desired, to navigate to the subscription for a specific entitlement, click on the highlighted number for column “reference document”. | The subscription is shown. |  |

##### Background Job to Trigger Provisioning

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

To send the message from the provisioning process to the provisioning system, the background job “5SW Send Provisioning Request” has to be triggered, as described below.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to SAP Entitlement Management. | The SAP Fiori Launchpad displays. |  |
| 2 | Access the App | Open Monitor Background Job Logs app |  |  |
| 3 | Execution of the job | Choose job name 5SW Send Provisioning Request.Choose Execute and choose Confirm. | Job is selected and executed. Wait for message: “Job has been executed, please go to the “JOB LOGS” section to refresh and see the latest job logs”. |  |
| 4 | Refresh | Refresh and look at the provisioning requests. | Check the sent provisioning request to the provisioning system. |  |

##### Send Response for the License Provisioning Requests

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

After the different provisioning requests for tenants has been sent to the provisioning system, the provisioning of the licenses for the new contract is performed by the provisioning system. After completion, the provisioning system sends a response to SAP Entitlement Management. The test description below describes how to manually test that response, using SAP Business Accelerator Hub (aka API Hub) / SoapUI.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to SAP Entitlement Management. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Maintain Customer Entitlements app. |  |  |
| 3 | Select the License Entitlement | Select the view Commercial Licenses. | License entitlements are shown, as well as the underlying master agreement entitlement. |  |
| 4 | View Provisioning Process and copy TaskExecutionLogGuid | Choose the entitlement number withEntitlement Model: LicenseApplication: CAD ApplicationMetric: UsersChoose tab Provision.Choose Expand for SI 5SW License ProvisioningNote down the Process Log ID.Choose the Process Log ID.Choose License Provisioning Request.Choose the icon in the middle, View Log.On pop-up window License Provisioning Request, choose the Message Log ID.On window Communication Messages, choose the icon under Payload.On pop-up Payload, click anywhere in the window, then press CTRL-F.In the search window, enter the Process Log ID noted down earlier and click on Enter.Double click on the field behind TaskExecutionLogGuid above your process log ID, and press CTRL-C to copy it. |  |  |
| 5 | Prepare the provisioning response on SAP Business Accelerator Hub / SoapUI | Launch:[https://api.sap.com/api/SAP_CF_EMS_Provisioning_Process/tryout](https://api.sap.com/api/SAP_CF_EMS_Provisioning_Process/tryout), and select the environment you created in chapter Prepare SAP Business Accelerator Hub to test the SAP Entitlement Management Provisioning Response.For SoapUI, select the project you created in chapter Prepare SoapUI to test the SAP Entitlement Management Provisioning Response (Optional)Choose the Body tab.Click in the area below the example payload, click Enter, and click CTRL+V to insert the copied TaskExecutionLogGuid.Replace the example payload with the payload below, for the application and system type.Double click on the TaskExecutionLogGuid, click CTRL+X, then double click on GUID, then click CTRL+V to insert the GuidNote Workaround for specific URL:If the URL provided in SAP Entitlement Management starts with [https://ems-api-ext.cfapps.eu10-005.hana.ondemand.com/](https://ems-api-ext.cfapps.eu10-005.hana.ondemand.com/), then do the following:Choose the Headers tab.Choose Add New Header.In the drop down box, select Host.In field value, Enter: ems-api-live-test.cfapps.eu10.hana.ondemand.com |  |  |
| 6 | Send Provisioning Response | Choose Run / Send for SoapUI. | The response body outlines that the response was sent successfully. |  |
| 7 | Return to app Maintain Customer Entitlements | On pop up Payload, choose Close and choose Back. | The license provisioning process has status Completed. |  |
| 8 | Return to Entitlements License Overview | Choose Back.In Maintain Customer Entitlements, choose View Commercial Licenses. | The entitlement for license with application CAD Application and metric Users has status Active. |  |
| 9 | Repeat for other licenses | Repeat steps 4 to 8 using the payload belowApplicationCapabilityMetricCAD ApplicationDocumentsCAD ApplicationCAD 2D EssentialsCollaboration ApplicationCollaboration Basic |  |  |

Payload for CAD Users License

[ {
"taskExecutionLogGuid" : "GUID",
"response" : {
"Capability_ID" : "",
"Capability_Active" : true,
"Application" : "CAD",
"Quantity" : 20
}
} ]

Payload for CAD Documents Licenses

[ {
"taskExecutionLogGuid" : "GUID",
"response" : {
"Capability_ID" : "",
"Capability_Active" : true,
"Application" : "CAD",
"Quantity" : 60
}
} ]

Payload for CAD 2D Essentials

[ {
"taskExecutionLogGuid" : "GUID",
"response" : {
"Capability_ID" : "CAD_2D_ES",
"Capability_Active" : true,
"Application" : "CAD",
"Quantity" : 1
}
} ]

Payload for Collaboration Basic

[ {
"taskExecutionLogGuid" : "GUID",
"response" : {
"Capability_ID" : "COLLAB_BAS",
"Capability_Active" : true,
"Application" : "COLLAB",
"Quantity" : 1
}
} ]

#### Add Additional Subscriptions for Users, Documents, Test Tenant, Trial CAD 3D

##### Extend Solution Order with Additional Subscriptions

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This step describes how to create a new solution order and add line items (for example, sales items, service items and service contract items) to solution order.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad using the role Solution Order Specialist. | The Fiori Launchpad with access to the Manage Solution Orders application is displayed. |  |
| 2 | Open Manage Solution Orders application | Open Manage Solution Orders (F4615). | The Manage Solution Orders screen is displayed. |  |
| 3 | Search for Solution Order | In the search area enter the Solution Order ID in the Solution Order field.Choose Go. | The solution order is displayed in the search result. |  |
| 4 | Open Solution Order | Choose the solution order from the result list. | Solution Order details are displayed on the Display Solution Order Page. |  |
| 5 | Add Item P-CAD-BRONZE | Choose Edit.Add the following Item in the solution order:Under ItemsProduct ID: P-CAD-BRONZEQuantity: 1Choose Enter.Click on Action(Edit) icon.Under Subscription ParametersParameter ID: R-LICENSEValue: 30In the Subscription Terms section enter the following details:Contract Start Date: <First Day of Current Month minus 6 months> |  |  |
| 6 | Adjust Contract Standard Duration | Activate check box Overwrite Default Terms.Set Fixed Term to 9 months.Click on Simulate to simulate the Pricing and Contract Duration and click Apply.Check the Net Value of the added line item. | The subscription item is now added to Solution Order. |  |
| 7 | Add Item P-CAD-ADD-DOC | Add the following Item in the solution order:Under ItemsProduct ID: P-CAD-ADD-DOCQuantity: 1Choose Enter.Click on Action(Edit) icon.Under Subscription ParametersParameter ID: R-LICENSEValue: 100In the Subscription Terms section enter the following details:Contract Start Date: <First Day of Current Month minus 6 months> |  |  |
| 8 | Adjust Contract Standard Duration | Activate check box Overwrite Default Terms.Set Fixed Term to 9 months.Click on Simulate to simulate the Pricing and Contract Duration and click Apply.Check the Net Value of the added line item. | The subscription item is now added to Solution Order. |  |
| 9 | Add Item P-CAD-TST-TENANT | Add the following Item in the solution order:Under ItemsProduct ID: P-CAD-TST-TENANTQuantity: 1Choose Enter.Click on Action(Edit) icon.In the Subscription Terms section enter the following details:Contract Start Date: <First Day of Current Month minus 6 months> |  |  |
| 10 | Adjust Contract Standard Duration | Activate check box Overwrite Default Terms.Set Fixed Term to 9 months.Click on Simulate to simulate the Pricing and Contract Duration and click Apply.Check the Net Value of the added line item. | The subscription item is now added to Solution Order. |  |
| 11 | Add Item P-CAD-TRIAL-3D | Add the following Item in the solution order:Under ItemsProduct ID: P-CAD-TRIAL-3DQuantity: 1Choose Enter.Click on Action(Edit) icon.In the Subscription Terms section enter the following details:Contract Start Date: <First Day of Current Month minus 6 months>Click on Apply. |  |  |
| 12 | Release Items and Save Solution Order | Click on Release All Items under Items and Click on Save.Click on Refresh.Navigate to Transaction History.On clicking on the Transaction number, you can directly navigate to SAP Subscription Billing.Note User can navigate to the subscription billing via the transaction history in Solution Order. Alternatively, log on to Subscription Billing > Subscriptions and search for the created subscriptions using the Subscription ID.Check in the Contract ItemCheck one-time price, Recurring Net Charge/ Month, Usage Based Net Charges / Month | On release the items are replicated as Subscription Contracts to SAP Subscription Billing and also different entitlements in SAP Entitlement Management will be created. |  |

##### Display Pending Subscriptions in SAP Subscription Billing

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The purpose of this step is to view the subscription in the Subscription Billing tenant and to verify the details.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad using the role Solution Order Specialist, if the subscription is created via a Solution Order. | The Fiori Launchpad is displayed. |  |
| 2 | Navigate to Manage Solution Orders | Open Manage Solution Orders (F4615). | The Manage Solution Orders screen is displayed. |  |
| 3 | Search for Solution Order | In the search area enter the Solution Order ID in the Solution Order field.Choose Go. | The solution order is displayed in the search result. |  |
| 4 | Open Solution Order | Choose the solution order from the result list. | Solution Order details is displayed in the Display Solution Order Page. |  |
| 5 | View Progress | In the Solution Order, choose View Progress. | Solution Order Progress is displayed. |  |
| 6 | Navigate to Subscription | In the Solution Order Progress. go to section Solution Order Progress.Choose the box with the Subscription.Choose icon Navigate to Transaction.Choose the Subscription ID to navigate to the Subscription in SAP Subscription BillingNote User can navigate to the subscription billing via the transaction history in Solution Order.Alternatively, log on to Subscription Billing > Subscriptions and search for the created subscriptions using the Subscription ID. |  |  |
| 7 | Check Subscription Header Details | Check the following subscription header details at the top:Customer: 33100001Status: PendingValid From: XXX XX, XXXX | All the details are rightly available in Subscription Billing. |  |
| 8 | Check Subscription item details | In the Processing Data , check for the details like:Subscription ProfileRelated DocumentsSubscription DatesSnapshot DataIn the Item List, choose Subscription Item, to view the complete details of the transaction.Details like Billing, Subscription Parameters, Pricing can be viewed. | All the item details of the Subscription Item can be viewed. |  |

##### Display Entitlements in SAP Entitlement Management

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

Use the Maintain Customer Entitlements app to view and manage entitlements. Using this app, you can create, view, edit, split, change status, reassign (move) folders of entitlement records, or export a filtered Entitlements List.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to SAP Entitlement Management. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Maintain Customer Entitlements app. | APP is opened. |  |
| 3 | Select the Tenant and the License Entitlement | Select the views Commercial Tenants and then Commercial Licenses.Click on Go. | The previously created tenant and tenant phase entitlements and license entitlements are still active.A new tenant and tenant phase entitlement has been created for the additional test tenant license.Additional license entitlements for the added subscriptions have been created and have status In Preparation, awaiting provisioning. |  |
| 4 | Capability and Quantity Check | Check the details of the respective entitlements. |  |  |
| 5 | Check related subscription | If desired, to navigate to the subscription for a specific entitlement, click on the highlighted number for column “reference document”. | The subscription is shown. |  |

##### Background Job to Trigger Provisioning

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

To send the message from the provisioning process to the provisioning system, the background job “5SW Send Provisioning Request” has to be triggered, as described below.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to SAP Entitlement Management. | The SAP Fiori Launchpad displays. |  |
| 2 | Access the App | Open Monitor Background Job Logs app |  |  |
| 3 | Execution of the job | Choose job name 5SW Send Provisioning Request.Choose Execute and choose Confirm. | Job is selected and executed. Wait for message: “Job has been executed, please go to the “JOB LOGS” section to refresh and see the latest job logs”. |  |
| 4 | Refresh | Refresh and look at the provisioning requests. | Check the sent provisioning request to the provisioning system. |  |

##### Send Response for the Tenant Provisioning Request

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

After the different provisioning requests for tenants has been sent to the provisioning system, the provisioning of the licenses for the new contract is performed by the provisioning system. After completion, the provisioning system sends a response to SAP Entitlement Management. The test description below describes how to manually test that response, using SAP Business Accelerator Hub (aka API Hub) / SoapUI.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to SAP Entitlement Management. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Maintain Customer Entitlements app. |  |  |
| 3 | Select the Tenant Entitlement | Select the view Commercial Tenants. | Tenant entitlements are shown, as well as the underlying master agreement entitlement. |  |
| 4 | View Provisioning Process and copy TaskExecutionLogGuid | Choose the entitlement number withEntitlement Model: Tenant PhaseApplication: CAD ApplicationSystem Type: Test SystemChoose View Phase Detail under Phase section.Choose tab Provision.Choose Expand for SI 5SW License ProvisioningNote down the Process Log ID.Choose the Process Log ID.Choose Send Provisioning Request.Choose the icon in the middle, View Log.On pop-up window Send Provisioning Request, choose the Message Log ID.On window Communication Messages, choose the icon under Payload.On pop-up Payload, click anywhere in the window, then press CTRL-F.In the search window, enter the Process Log ID noted down earlier and click on Enter.Double click on the field behind TaskExecutionLogGuid above your process log ID, and press CTRL-C to copy it. |  |  |
| 5 | Prepare the provisioning response on SAP Business Accelerator Hub / SoapUI | Launch:[https://api.sap.com/api/SAP_CF_EMS_Provisioning_Process/tryout](https://api.sap.com/api/SAP_CF_EMS_Provisioning_Process/tryout), and select the environment you created in chapter Prepare SAP Business Accelerator Hub to test the SAP Entitlement Management Provisioning Response.For SoapUI, select the project you created in chapter Prepare SoapUI to test the SAP Entitlement Management Provisioning Response (Optional)Choose the Body tab.Click in the area below the example payload, click Enter, and click CTRL+V to insert the copied TaskExecutionLogGuid.Replace the example payload with the payload below, for the application and system type.Double click on the TaskExecutionLogGuid, click CTRL+X, then double click on GUID, then click CTRL+V to insert the GuidNote Workaround for specific URL:If the URL provided in SAP Entitlement Management starts with [https://ems-api-ext.cfapps.eu10-005.hana.ondemand.com/](https://ems-api-ext.cfapps.eu10-005.hana.ondemand.com/), then do the following:Choose the Headers tab.Choose Add New Header.In the drop down box, select Host.In field value, Enter: ems-api-live-test.cfapps.eu10.hana.ondemand.com |  |  |
| 6 | Send Provisioning Response | Choose Run / Send for SoapUI. | The response body outlines that the response was sent successfully. |  |
| 7 | Return to app Maintain Customer Entitlements | On pop up Payload, choose Close and choose Back. | The tenant provisioning process has status Completed. |  |
| 8 | Return to Entitlements Tenants Overview | Choose Back.Choose Back.In Maintain Customer Entitlements, choose View Commercial Tenants. | The entitlement for Tenant Phases and Tenants for application CAD and system type Test have status Active.The tenant entitlement shows the Tenant ID, Tenant Name, Tenant URL based on the provisioning feedback. |  |

Payload for CAD Additional Test Tenant

[ {
"taskExecutionLogGuid" : "GUID",
"response" : {
"Tenant_URL" : "http://fivestar.test2.cad.com",
"Tenant_ID" : "CAD_10005_TST",
"Tenant_Status" : "ACTIVE",
"Tenant_Name" : "AE1 COM CAD TEST 2"
}
} ]

##### Send Response for the License Provisioning Requests

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

After the different provisioning requests for tenants has been sent to the provisioning system, the provisioning of the licenses for the new contract is performed by the provisioning system. After completion, the provisioning system sends a response to SAP Entitlement Management. The test description below describes how to manually test that response, using SAP Business Accelerator Hub (aka API Hub) / SoapUI.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to SAP Entitlement Management. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Maintain Customer Entitlements app. |  |  |
| 3 | Select the License Entitlement | Select the view Commercial Licenses. | License entitlements are shown, as well as the underlying master agreement entitlement. |  |
| 4 | View Provisioning Process and copy TaskExecutionLogGuid | Choose the entitlement number withEntitlement Model: LicenseApplication: CAD ApplicationMetric: UsersChoose tab Provision.Choose Expand for SI 5SW License ProvisioningNote down the Process Log ID.Choose the Process Log ID.Choose License Provisioning Request.Choose the icon in the middle, View Log.On pop-up window License Provisioning Request, choose the Message Log ID.On window Communication Messages, choose the icon under Payload.On pop-up Payload, click anywhere in the window, then press CTRL-F.In the search window, enter the Process Log ID noted down earlier and click on Enter.Double click on the field behind TaskExecutionLogGuid above your process log ID, and press CTRL-C to copy it. |  |  |
| 5 | Prepare the provisioning response on SAP Business Accelerator Hub / SoapUI | Launch:[https://api.sap.com/api/SAP_CF_EMS_Provisioning_Process/tryout](https://api.sap.com/api/SAP_CF_EMS_Provisioning_Process/tryout), and select the environment you created in chapter Prepare SAP Business Accelerator Hub to test the SAP Entitlement Management Provisioning Response.For SoapUI, select the project you created in chapter Prepare SoapUI to test the SAP Entitlement Management Provisioning Response (Optional)Choose the Body tab.Click in the area below the example payload, click Enter, and click CTRL+V to insert the copied TaskExecutionLogGuid.Replace the example payload with the payload below, for the application and system type.Double click on the TaskExecutionLogGuid, click CTRL+X, then double click on GUID, then click CTRL+V to insert the GuidNote Workaround for specific URL:If the URL provided in SAP Entitlement Management starts with [https://ems-api-ext.cfapps.eu10-005.hana.ondemand.com/](https://ems-api-ext.cfapps.eu10-005.hana.ondemand.com/), then do the following:Choose the Headers tab.Choose Add New Header.In the drop down box, select Host.In field value, Enter: ems-api-live-test.cfapps.eu10.hana.ondemand.com |  |  |
| 6 | Send Provisioning Response | Choose Run / Send for SoapUI. | The response body outlines that the response was sent successfully. |  |
| 7 | Return to app Maintain Customer Entitlements | On pop up Payload, choose Close and choose Back. | The license provisioning process has status Completed. |  |
| 8 | Return to Entitlements License Overview | Choose Back.In Maintain Customer Entitlements, choose View Commercial Licenses. | The entitlement for license with application CAD Application and metric Users has status Active. |  |
| 9 | Repeat for other licenses | Repeat steps 4 to 8 using the payload belowApplicationCapabilityMetricOfferingCAD ApplicationDocumentsCAD Bronze EditionCAD ApplicationCAD 2D EssentialsCollaboration ApplicationCollaboration BasicCAD ApplicationDocumentsCAD DocumentsCAD ApplicationCAD 3D |  |  |

Payload for CAD Users License

[ {
"taskExecutionLogGuid" : "GUID",
"response" : {
"Capability_ID" : "",
"Capability_Active" : true,
"Application" : "CAD",
"Quantity" : 30
}
} ]

Payload for CAD Documents Licenses

[ {
"taskExecutionLogGuid" : "GUID",
"response" : {
"Capability_ID" : "",
"Capability_Active" : true,
"Application" : "CAD",
"Quantity" : 90
}
} ]

Payload for CAD 2D Essentials

[ {
"taskExecutionLogGuid" : "GUID",
"response" : {
"Capability_ID" : "CAD_2D_ES",
"Capability_Active" : true,
"Application" : "CAD",
"Quantity" : 1
}
} ]

Payload for Collaboration Basic

[ {
"taskExecutionLogGuid" : "GUID",
"response" : {
"Capability_ID" : "COLLAB_BAS",
"Capability_Active" : true,
"Application" : "COLLAB",
"Quantity" : 1
}
} ]

Payload for Document License from CAD Documents

[ {
"taskExecutionLogGuid" : "GUID",
"response" : {
"Capability_ID" : "",
"Capability_Active" : true,
"Application" : "CAD",
"Quantity" : 100
}
} ]

Payload for CAD 3D

[ {
"taskExecutionLogGuid" : "GUID",
"response" : {
"Capability_ID" : " CAD_3D",
"Capability_Active" : true,
"Application" : "CAD",
"Quantity" : 1
}
} ]

##### Display Active Subscription in SAP Subscription Billing

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The purpose of this step is to view the subscription in the Subscription Billing tenant and to verify the details.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad using the role Solution Order Specialist, if the subscription is created via a Solution Order. | The Fiori Launchpad is displayed. |  |
| 2 | Navigate to Manage Solution Orders | Open Manage Solution Orders (F4615) under Subscriptions and Billing catalog. | The Manage Solution Orders page is displayed. |  |
| 3 | Search for Solution Order | In the search area enter the Solution Order ID in the Solution Order field.Choose Go. | The solution order is displayed in the search result. |  |
| 4 | Open Solution Order | Choose the solution order from the result list. | Solution Order details are displayed on the Display Solution Order Page |  |
| 5 | View Progress | In the Solution Order, choose View Progress. | Solution Order Progress is displayed. |  |
| 6 | Navigate to Subscription | In the Solution Order Progress. go to section Solution Order Progress.Choose the box with the Subscription.Choose icon Navigate to Transaction.Choose the subscription ID to navigate to the Subscription in SAP Subscription Billing.Note User can navigate to the subscription billing via the transaction history in Solution Order.Alternatively, log on to Subscription Billing > Manage Subscriptions and search for the created subscriptions using the Subscription ID. |  |  |
| 7 | Check Subscription Header Details | Check the following subscription header details at the top:Customer: 33100001Status: ActiveValid From: XXX XX, XXXXNote Note down the provider contract ID mentioned in the Processing data tab for further steps. | All the details are rightly available in Subscription Billing. |  |
| 8 | Check Provider Contract | Choose tab Processing Data.Choose the Provider Contract ID under Related Documents.Review the provider contract under General Data.Choose Items: General Data.Choose Item 1 – License.Double click the linked Billing Plan.Choose Plan Items.Choose Item 2 – Activation Fee.Double click the linked Billing Plan.Choose Plan Items.Choose Back.Choose Back.Choose Back. |  |  |
| 9 | Check Subscription item details | In the Processing Data , check for the details like:Subscription ProfileRelated DocumentsSubscription DatesSnapshot DataIn the Item List, choose Subscription Item, to view the complete details of the transaction.Details like Billing, Subscription Parameters, Pricing can be viewed. | All the item details of the Subscription Item can be viewed. |  |

##### Send Tenant Capability Update

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

After completing license provisioning, which activated a specific capability, the provisioning system sends a call to SAP Entitlement Management, to updated the enabled license capabilities in the tenant entitlement.

Based on that, the tenant entitlement acts as the “Digital Twin” of the real system tenant, showing in a table attribute of the tenant entitlement for a specific tenant, which capabilities have been licensed and are currently enabled in that tenant.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Prepare the entitlement update on SAP Business Accelerator Hub / SoapUI | Launch: [https://api.sap.com/api/SAP_CF_EMS_Entitlement_Process_Quick_Update/tryout](https://api.sap.com/api/SAP_CF_EMS_Entitlement_Process_Quick_Update/tryout) and select the environment you created in chapter Prepare SAP Business Accelerator Hub to test the SAP Entitlement Management Provisioning Response.For SoapUI, select the project you created in chapter Prepare SoapUI to test the SAP Entitlement Management Provisioning Response (Optional)Choose the Body tab.Replace the example payload with the payload below.Note Workaround for specific URL:If the URL provided in SAP Entitlement Management starts with [https://ems-api-ext.cfapps.eu10-005.hana.ondemand.com/](https://ems-api-ext.cfapps.eu10-005.hana.ondemand.com/):Choose the Headers tab and choose Add New Header. In the drop down box, select Host. In field value, enter: ems-api-live-test.cfapps.eu10.hana.ondemand.com |  |  |
| 2 | Send Tenant Update | Choose Run / Send for SoapUI.Note The response will search for a unique tenant ID of the used Application with entitlement model Tenants. In case you get an error since you have multiple times the same tenant ID for the used application in different tenants, delete the other tenant entitlements still in the system from earlier tests, to be able to post the response successfully. |  |  |
| 3 | Log on | Log on to SAP Entitlement Management. |  |  |
| 4 | Access the app | Open Maintain Customer Entitlements app. |  |  |
| 5 | Select the Tenant Entitlement | Select the view Commercial Tenants. |  |  |
| 6 | View Tenant Capabilities Table | Choose the entitlement with the following details:Entitlement Model: TenantApplication: CAD ApplicationSystem Type: Productive SystemUnder General Data, review the capability table with activated and licensed capabilities in the productive tenant is shown. |  |  |

Productive System, Tenant, CAD Application, Capability 3D

{
"processCode" : "5SW_Quick_Create_Update_Tenant_Capabilities_JS",
"businessEvent" : "NOS",
"refDocNo" : " ADD_CAP_001",
"processParameter" : {
"Application" : "CAD",
"TenantID" : "CAD_10003_PRD",
"Operation" : "Append",
"CapabilityTable" : [ {
"Capability" : "CAD_3D",
"Status" : "ACTIVE",
"Licensed" : true
} ]
}
}

#### Perform Decommissioning for Capability “CAD 3D”

##### Background Job to Set Entitlement Status to Expired

Procedure

This background job will move any entitlement, for which the end date has been passed, to Expired.

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to SAP Entitlement Management. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Monitor Background Job Logs app |  |  |
| 3 | Execution of the job name | Choose job name 5SW Set Status to Expired Job.Choose Execute and choose Confirm. | Job is selected and executed. Wait for message: “Job has been executed, please go to the “JOB LOGS” section to refresh and see the latest job logs”. |  |
| 4 | Refresh and look at the job log | Refresh and look at the provisioning requests. | Check the job lock to see that one status was set to expired. |  |

##### Display Entitlements in SAP Entitlement Management

Procedure

Use the Maintain Customer Entitlements app to view and manage entitlements. Using this app, you can create, view, edit, split, change status, reassign (move) folders of entitlement records, or export a filtered Entitlements List.

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to SAP Entitlement Management. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Maintain Customer Entitlements app. | APP is opened. |  |
| 3 | Select the License Entitlement | Select the views Commercial Licenses.Click on Go. | The license for Capability CAD 3D has now status Expired. |  |
| 4 | Capability and Quantity Check | Check the details of the respective entitlements. |  |  |
| 5 | Check related subscription | If desired, to navigate to the subscription for a specific entitlement, click on the highlighted number for column “reference document”. | The subscription is shown. |  |

##### Group Event for Licenses Expired

Procedure

This event will be triggered, once the last event for a specific capability has been set to expired, because then, that capability has to be de-comissioned in the productive tenant.

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to SAP Entitlement Management. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Monitor Event Logs app.Choose Send Notification. |  |  |
| 3 | Execution of the job name | View event 5SW License Expired (Group Event) with status Sent. | The event has sent a message to the provisioning system to decommission the respective capability in the productive tenant. |  |

##### Send Tenant Capability Update based on License Capability Decommissioning

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

After completing license provisioning, which activated a specific capability, the provisioning system sends a call to SAP Entitlement Management, to updated the enabled license capabilities in the tenant entitlement.

Based on that, the tenant entitlement acts as the “Digital Twin” of the real system tenant, showing in a table attribute of the tenant entitlement for a specific tenant, which capabilities have been licensed and are currently enabled in that tenant.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Prepare the entitlement update on SAP Business Accelerator Hub / SoapUI | Launch:[https://api.sap.com/api/SAP_CF_EMS_Entitlement_Process_Quick_Update/tryout](https://api.sap.com/api/SAP_CF_EMS_Entitlement_Process_Quick_Update/tryout) and select the environment you created in chapter Prepare SAP Business Accelerator Hub to test the SAP Entitlement Management Provisioning Response.For SoapUI, select the project you created in chapter Prepare SoapUI to test the SAP Entitlement Management Provisioning Response (Optional)Choose the Body tab.Replace the example payload with the payload below.Note Workaround for specific URLIf the URL provided in SAP Entitlement Management starts with [https://ems-api-ext.cfapps.eu10-005.hana.ondemand.com/](https://ems-api-ext.cfapps.eu10-005.hana.ondemand.com/), Choose the Headers tab. Choose Add New Header. In the dropdown box, select Host. In field value, enter: ems-api-live-test.cfapps.eu10.hana.ondemand.com | The SAP Fiori launchpad displays. |  |
| 2 | Send tenant update | Choose Run / Send for SoapUI.Note The response will search for a unique tenant ID of the used Application with entitlement model Tenants. In case you get an error since you have multiple times the same tenant ID for the used application in different tenants, delete the other tenant entitlements still in the system from earlier tests, to be able to post the response successfully. |  |  |
| 3 | Log On | Log on to SAP Entitlement Management. | The SAP Fiori launchpad displays. |  |
| 4 | Access the App | Open Maintain Customer Entitlements app. |  |  |
| 5 | Select the Tenant Entitlement | Select the view Commercial Tenants. | Tenant entitlements are shown, as well as the underlying master agreement entitlement. |  |
| 6 | View Tenant Capabilities Table | Choose the entitlement number withEntitlement Model: TenantApplication: CAD ApplicationSystem Type: Productive SystemUnder General Data, review the Capability Table with Inactive. | Licensed capabilities in the productive tenant is no longer shown. |  |

Productive System, Tenant, CAD Application, Capability CAD 3D

{
"processCode" : "5SW_Quick_Create_Update_Tenant_Capabilities_JS",
"businessEvent" : "NOS",
"refDocNo" : " ADD_CAP_001",
"processParameter" : {
"Application" : "CAD",
"TenantID" : "CAD_10003_PRD",
"Operation" : "Append",
"CapabilityTable" : [ {
"Capability" : "CAD_3D",
"Status" : "INACTIVE",
"Licensed" : false
} ]
}
}

#### Replace Subscription with New Contract

The customer wants to move from the existing CAD Bronze Edition subscription and add-on, and do an early replacement with the CAD Gold Edition.

##### Terminate Subscription early in SAP Subscription Billing

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad using the role Subscription Specialist - Subscription Billing. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Subscriptions (F6801). |  |  |
| 3 | Execution of the job name | Activate the check box on the left side of the subscription list for all subscriptions which were created for P-CAD-BRONZE, P-CAD-TST-TENANT, P-CAD-ADD-DOCChoose Mass Changes and then Cancel.Under Desired Expiration Date, enter the first day of the current month minus 2 months.Under Cancellation Notice Date, enter the same date.Under Cancellation Reason, enter Early Contract Replacement.Activate the check box for Overrule Subscription Terms.Choose Cancel Subscriptions. | The subscriptions do now have status Expired. |  |

##### Display Entitlements in SAP Entitlement Management

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Procedure

Use the Maintain Customer Entitlements app to view and manage entitlements. Using this app, you can create, view, edit, split, change status, reassign (move) folders of entitlement records, or export a filtered Entitlements List.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to SAP Entitlement Management. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Maintain Customer Entitlements app. | APP is opened. |  |
| 3 | Select the Tenant and the License Entitlement | Select the views Commercial Tenants and then Commercial Licenses.Click on Go. | The previously created Tenant and Tenant Phase and License entitlements are still Active, but the end date of the Tenant Phase entitlements has been reduced.The Licenses which were terminated early have now status In Preparation, since the reduced end date has to be communicated to the provisioning system. |  |
| 4 | Capability and Quantity Check | Check the details of the respective entitlements. |  |  |

##### Background Job to Trigger Provisioning

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

To send the message from the decommissioning processes to the provisioning system, the background job “5SW Send Provisioning Request” has to be triggered, as described below.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to SAP Entitlement Management. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Monitor Background Job Logs app. |  |  |
| 3 | Execution of the job name | Choose job name 5SW Send Provisioning Request.Choose Execute and choose Confirm. | Job is selected and executed.Wait for message: “Job has been executed, please go to the “JOB LOGS” section to refresh and see the latest job logs”. |  |
| 4 | Refresh the job | Refresh and look at the provisioning requests. | Check the sent provisioning requests to the provisioning system. |  |

##### Send Response for the License Provisioning Requests

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

After the different provisioning requests for tenants has been sent to the provisioning system, the provisioning of the licenses for the new contract is performed by the provisioning system. After completion, the provisioning system sends a response to SAP Entitlement Management. The test description below describes how to manually test that response, using SAP Business Accelerator Hub (aka API Hub) / SoapUI.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to SAP Entitlement Management. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Maintain Customer Entitlements app. |  |  |
| 3 | Select the License Entitlement | Select the view Commercial Licenses. | License Entitlements are shown, as well as the underlying master agreement entitlement. |  |
| 4 | View Provisioning Process and copy TaskExecutionLogGuid | Choose the entitlement number withEntitlement Model: LicenseApplication: CAD ApplicationMetric: UsersChoose tab Provision.Choose Expand for SI 5SW License ProvisioningNote down the Process Log ID.Choose the Process Log ID.Choose License Provisioning Request.Choose the icon in the middle, View Log.On pop-up window Send Provisioning Request, choose the Message Log ID.On window Communication Messages, choose the icon under Payload.On pop-up Payload, click anywhere in the window, then press CTRL-F.In the search window, enter the Process Log ID noted down earlier and click on Enter.Double click on the field behind TaskExecutionLogGuid above your process log ID, and press CTRL-C to copy it. |  |  |
| 5 | Prepare the provisioning response on SAP Business Accelerator Hub / SoapUI | Launch:[https://api.sap.com/api/SAP_CF_EMS_Provisioning_Process/tryout](https://api.sap.com/api/SAP_CF_EMS_Provisioning_Process/tryout), and select the environment you created in chapter Prepare SAP Business Accelerator Hub to test the SAP Entitlement Management Provisioning Response.For SoapUI, select the project you created in chapter Prepare SoapUI to test the SAP Entitlement Management Provisioning Response (Optional)Choose the Body tab.Click in the area below the example payload, click Enter, and click CTRL+V to insert the copied TaskExecutionLogGuid.Replace the example payload with the payload below, for the application and system type.Double click on the TaskExecutionLogGuid, click CTRL+X, then double click on GUID, then click CTRL+V to insert the Guid.Note Workaround for specific URL:If the URL provided in SAP Entitlement Management starts with https://ems-api-ext.cfapps.eu10-005.hana.ondemand.com/ then do the following:Choose the Headers tab.Choose Add New Header.In the drop down box, select Host.In field value, Enter: ems-api-live-test.cfapps.eu10.hana.ondemand.com |  |  |
| 6 | Send Provisioning Response | Choose Run / Send for SoapUI. | The response body outlines that the response was sent successfully. |  |
| 7 | Return to app Maintain Customer Entitlements | On pop up Payload, choose Close and choose Back. | The license decommissioning process has status Completed. |  |
| 8 | Return to Entitlements License Overview | Choose Back.In Maintain Customer Entitlements, choose View Commercial Licenses. | The entitlement has status Active. |  |
| 9 | Repeat for other licenses | Repeat steps 4 to 8 using the payload belowApplicationCapabilityMetricQuantityCAD ApplicationUsers20CAD ApplicationUsers30CAD ApplicationDocuments60CAD ApplicationDocuments90CAD ApplicationDocuments100CAD ApplicationCAD 2D Essentials1CAD ApplicationCAD 2D Essentials1Collaboration ApplicationCollaboration Basic1Collaboration ApplicationCollaboration Basic1 |  |  |

Payload for CAD Users Licenses

[ {
"taskExecutionLogGuid" : "GUID",
"response" : {
"Capability_ID" : "",
"Capability_Active" : true,
"Application" : "CAD",
"Quantity" : 20
}
} ]

[ {
"taskExecutionLogGuid" : "GUID",
"response" : {
"Capability_ID" : "",
"Capability_Active" : true,
"Application" : "CAD",
"Quantity" : 30
}
} ]

Payload for CAD Documents Licenses

[ {
"taskExecutionLogGuid" : "GUID",
"response" : {
"Capability_ID" : "",
"Capability_Active" : true,
"Application" : "CAD",
"Quantity" : 60
}
} ]

[ {
"taskExecutionLogGuid" : "GUID",
"response" : {
"Capability_ID" : "",
"Capability_Active" : true,
"Application" : "CAD",
"Quantity" : 90
}
} ]

Payload for Document License from CAD Documents

[ {
"taskExecutionLogGuid" : "GUID",
"response" : {
"Capability_ID" : "",
"Capability_Active" : true,
"Application" : "CAD",
"Quantity" : 100
}
} ]

Payload for CAD 2D Essentials

[ {
"taskExecutionLogGuid" : "GUID",
"response" : {
"Capability_ID" : "CAD_2D_ES",
"Capability_Active" : true,
"Application" : "CAD",
"Quantity" : 1
}
} ]

Payload for Collaboration Basic

[ {
"taskExecutionLogGuid" : "GUID",
"response" : {
"Capability_ID" : "COLLAB_BAS",
"Capability_Active" : true,
"Application" : "COLLAB",
"Quantity" : 1
}
} ]

##### Create SAP S/4HANA Solution Order Replacement Contract

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The existing solution order, for which the subscriptions have been canceled in the last step, is copied to the new solution order, where the subscription licenses are updated based on the customer’s request, to move to the CAD Gold Edition with 100 users, and continue the subscription for the additional test tenant.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad using the role Solution Order Specialist. | The Fiori Launchpad with access to the Manage Solution Orders application is displayed. |  |
| 2 | Open Manage Solution Orders application | Open Manage Solution Orders (F4615). | The Manage Solution Orders screen is displayed. |  |
| 3 | Search for Solution Order | In the Search area enter the Solution Order ID created in the previous test process in the Solution Order field and choose Go. | The solution order is displayed in the search result. |  |
| 4 | Open Solution Order | Choose the solution order from the result list. | Solution Order details is displayed on the Display Solution Order Page. |  |
| 5 | Copy Solution Order | Choose Copy. | A copy of the solution order is created, still with the master agreement COM, so that the existing tenants can be re-used by the replacement contracts. |  |
| 6 | Delete Items | Choose action Delete for the items in the copied solution order, not required any longer:2nd Item with product P-CAD-BRONZEItem with product P-CAD-ADD-DOCItem with product P-CAD-TRIAL-3D | Additional documents are removed, since the CAD Gold Edition does not have a document limit.CAD Trial 3D is removed, since CAD Gold Edition does include CAD 3D. |  |
| 7 | Change item with P-CAD-BRONZE | Change the item with product P-CAD-BRONZE to product P-CAD-GOLD.Click on Action(Edit) icon for that item.Under Subscription ParametersParameter ID: R-LICENSEValue: 100In the Subscriptions Terms section enter the following details:Contract Start Date: <first day of the current month minus 3 months>Choose Simulate to simulate the Pricing and Contract Duration.Choose Apply .Check the Net Value of the added line item. |  |  |
| 8 | Look up existing contract and item for P-CAD-TST-TENANT | Log on to SAP Entitlement Management in a separate browser tab.Open Maintain Customer Entitlements app.Select the views Commercial Tenants.Choose Go.Note down contract and contract item for Entitlement with,Entitlement Model: Tenant PhaseOffering: CAD Test Tenant |  |  |
| 9 | Update Item P-CAD-TST-TENANT | Return to the browser tab with SAP S/4HANA Solution Order.Click on Action(Edit) icon for the item with product P-CAD-TST-TENANT.In the Dates section enter the following details:Contract Start Date: <first day of the current month minus 3 months>In the Subscription Billing Item Details - Additional Data section enter the following details:Reference Contract: <Enter the contract number you looked up in the last step (without SB prefix)>.Reference Contract Item: <Enter the contract item you looked up in the last step>.Choose Simulate to simulate the Pricing and Contract Duration.Choose Apply .Check the Net Value of the added line item. | By providing the reference to the old contract and item for the new item for P-CAD-TST-TENANT, SAP Entitlement Management will re-use the existing additional test tenant, and will not trigger the provisioning of a new tenant. |  |
| 10 | Release Items and Save Solution Order | Click on Release All Items under Items and Click on Save.Click on Refresh.Navigate to Transaction History.On clicking on the Transaction number, you can directly navigate to SAP Subscription Billing.Note User can navigate to the subscription billing via the transaction history in Solution Order. Alternatively, log on to Subscription Billing > Manage Subscriptions and search for the created subscriptions using the Subscription ID.Check in the Contract ItemCheck one-time price, Recurring Net Charge/ Month, Usage Based Net Charges / Month | On release the items are replicated as Subscription Contracts to SAP Subscription Billing and also different entitlements in SAP Entitlement Management will be created. |  |

##### Display Pending Subscriptions in SAP Subscription Billing

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The purpose of this step is to view the subscription in the Subscription Billing tenant and to verify the details.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad using the role Solution Order Specialist, if the subscription is created via a Solution Order. | The Fiori Launchpad is displayed. |  |
| 2 | Navigate to Manage Solution Orders | Open Manage Solution Orders (F4615). | The Manage Solution Orders page is displayed. |  |
| 3 | Search for Solution Order | In the search area enter the Solution Order ID in the Solution Order field.Choose Go. | The solution order is displayed in the search result. |  |
| 4 | Open Solution Order | Choose the solution order from the result list. | Solution Order details are displayed on the Display Solution Order Page |  |
| 5 | View Progress | In the Solution Order, choose View Progress. | Solution Order Progress is displayed. |  |
| 6 | Navigate to Subscription | In the Solution Order Progress. go to section Solution Order Progress.In the Subscription section, choose Subscription Billing.Note User can navigate to the subscription billing via the transaction history in Solution Order.Alternatively, log on to Subscription Billing > Manage Subscriptions and search for the created subscriptions using the Subscription ID. |  |  |
| 7 | Check Subscription Header Details | Check the following subscription header details at the top:Customer : 33100001Status: PendingValid From: XXX XX, XXXXExpires On: XXX XX, XXXX | All the details are rightly available in Subscription Billing. |  |
| 8 | Check Subscription item details | In the Processing Data, check for the details like:Subscription ProfileRelated DocumentsSubscription DatesSnapshot DataIn the Item List, choose Subscription Item, to view the complete details of the transaction. | All the item details of the Subscription Item can be viewed. |  |

##### Display Entitlements in SAP Entitlement Management

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

Use the Maintain Customer Entitlements app to view and manage entitlements. Using this app, you can create, view, edit, split, change status, reassign (move) folders of entitlement records, or export a filtered Entitlements List.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to SAP Entitlement Management. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Maintain Customer Entitlements app. | APP is opened. |  |
| 3 | Select the Tenant and the License Entitlement | Select the views Commercial Tenants and then Commercial Licenses.Click on Go. | For Offering CAD Test Tenant, we still have the existing tenant entitlement, and we now have two Tenant Phase entitlements, one for the old contract, and one for the new contract, both linked to the physical tenant entitlement through the first, leading phase. Those Tenants and Tenant Phases are all Active.For Offering CAD Bronze Edition and CAD Gold Edition, we can see Tenant entitlements for the Productive CAD, Test CAD, Productive Collaboration, and Test Collaboration Tenant, each with 2 old Tenant Phases, and one new Tenant Phase, from the new contract. Those Tenants and Tenant Phases are all Active.For Offering CAD Gold Edition, we also see now a Tenant and Tenant Phase for an Analytics Test and Analytics Productive Tenant, which are coming with the switch from Bronze to Gold Edition. Those new Tenants and Tenant Phases have status In Preparation, since they have not been provisioned yet.For the licenses, we see the licenses from the old contract still Active, and we see new licenses for the CAD Gold Edition with status In Preparation, which will be provisioned as soon as the contract starts. |  |
| 4 | Capability and Quantity Check | Check the details of the respective entitlements. |  |  |
| 5 | Check related subscription | If desired, to navigate to the subscription for a specific entitlement, click on the highlighted number for column “reference document”. | The subscription is shown. |  |

##### Run Job in SAP Entitlement Management to Set Status to Expired

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This background job will move any entitlement, for which the end date has been passed, to Expired. For the current test process, by running this job, we are simulating that the day, where the contract for the test tenant expires, has arrived, so that tenant phase entitlement is set to status Expired.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to SAP Entitlement Management. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Monitor Background Job Logs app |  |  |
| 3 | Execution of the job name | Choose job name 5SW Set Status to Expired Job.Choose Execute and choose Confirm. | Job is selected and executed.Wait for message: “Job has been executed, please go to the “JOB LOGS” section to refresh and see the latest job logs.” |  |
| 4 | Refresh the job | Refresh and look at the JOB LOGS. | Check the job log to see that one status were set to Expired. |  |

## Suspected conflicts

> [!warning] Conflict
> Flagged while digesting this document, not verified: Usage records app is named 'Manage Usage Records - Deprecated (F6802)' in the Overview Table but 'Manage Usage Records - Subscription Billing (F6802A)' in the test procedure.

> [!warning] Conflict
> Flagged while digesting this document, not verified: Journal Entry Analyzer step says the split revenue is assigned to Product Area 02_COLLAB, while the material groups defined earlier are 02_CAD2 (CAD Add-on) and 03_COLLAB (Collaboration).

## Connections
- part-of :: [[_cluster]]
- related-to :: [[09-subscription-billing-and-contract-accounting/test-script-subscription-management-for-software-5sw-ae-sap-s-4hana-cl-part-02]]
- related-to :: [[09-subscription-billing-and-contract-accounting/master-data-script-create-subscription-product-convergent-invoicing-md]]
- related-to :: [[09-subscription-billing-and-contract-accounting/master-data-script-create-subscription-product-sales-billing-mds-5bd-4]]
- related-to :: [[09-subscription-billing-and-contract-accounting/mds-5bd-429]]
- related-to :: [[09-subscription-billing-and-contract-accounting/mds-5lp-451]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/5SW_S4CLD2608_BPD_EN_AE.docx` — lines 1–3326 of the extracted text · extracted with `mammoth` · 288,298 chars in the whole document
