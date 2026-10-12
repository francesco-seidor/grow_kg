---
id: 10-procurement/direct-procurement-with-inbound-delivery-2tx-ae-test-script-sap-s-4han
title: "Direct Procurement with Inbound Delivery (2TX_AE) - Test Script, SAP S/4HANA Cloud Public Edition (2TX_S4CLD2608_BPD_EN_AE)"
description: "SAP S/4HANA Cloud Public Edition test script for scope item 2TX_AE (UAE): PO, supplier confirmation, inbound delivery, goods receipt and supplier invoice, with roles, sample data and Fiori apps."
cluster: 10-procurement
tags: [kb/procurement, topic/direct-material-procurement]
aliases: [2TX_S4CLD2608_BPD_EN_AE]
keywords: [Direct Material Procurement, direct procurement test script, purchase order creation, supplier confirmation, situation handling, order acknowledgement, inbound delivery, goods receipt, two step goods receipt, supplier invoice]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/2TX_S4CLD2608_BPD_EN_AE.docx]
confidence: low
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-865
topic: 10-procurement/direct-material-procurement
language: EN
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Direct Procurement with Inbound Delivery (2TX_AE) - Test Script, SAP S/4HANA Cloud Public Edition (2TX_S4CLD2608_BPD_EN_AE)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/2TX_S4CLD2608_BPD_EN_AE.docx`, extracted with `mammoth`. Grouped under **Direct Material Procurement** in Procurement. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

|  |  |
| --- | --- |
| Direct Procurement with Inbound Delivery (2TX_AE)Purpose PUBLIC 1<!-- image omitted: unnamed --> | Test ScriptSAP S/4HANA Cloud Public Edition - 19-06-26 |
|  | Direct Procurement with Inbound Delivery (2TX_AE) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Table of Contents

[1 Purpose 4](#_Toc232850256)

[2 Prerequisites 5](#_Toc232850257)

[2.1 System Access 5](#_Toc232850258)

[2.2 Roles 5](#_Toc232850259)

[2.3 Master Data, Organizational Data, and Other Data 6](#_Toc232850260)

[2.4 Business Conditions 7](#_Toc232850261)

[2.5 Preliminary Steps 8](#_Toc232850262)

[2.5.1 Open New MM Period 8](#_Toc232850263)

[2.5.2 Create Manage Team and Responsibilities 8](#_Toc232850264)

[2.5.3 Create Situation Template 9](#_Toc232850265)

[2.5.4 Monitor Situations 11](#_Toc232850266)

[2.5.5 Create Purchasing Info Record (Optional) 12](#_Toc232850267)

[2.5.6 Set up Confirmation Control 14](#_Toc232850268)

[2.5.7 Output Parameter Determination for Order Acknowlegement 15](#_Toc232850269)

[2.5.8 Create Purchase Order for Order Acknowledgement 18](#_Toc232850270)

[2.5.9 Confirmation for Purchase Order 19](#_Toc232850271)

[2.5.10 Schedule Order Acknowledgement output for Purchase Orders (Optional) 20](#_Toc232850272)

[2.5.11 Order Acknowledge on Purchase Orders 21](#_Toc232850273)

[2.5.12 Supplier Confirmation Workflow (Optional) 22](#_Toc232850274)

[2.5.12.1 Activate Flexible Workflows for Supplier Confirmation (Optional) 22](#_Toc232850275)

[2.5.12.2 Manage Workflows for Supplier Confirmations (Optional) 24](#_Toc232850276)

[3 Overview Table 26](#_Toc232850277)

[4 Test Procedures 27](#_Toc232850278)

[4.1 Create Purchase Order Manually 27](#_Toc232850279)

[4.1.1 Option A: Create Purchase Order with Confirmation 27](#_Toc232850280)

[4.1.2 Option B: Create Purchase Order with Inbound Delivery 28](#_Toc232850281)

[4.2 Supplier Confirmation (Optional) 30](#_Toc232850282)

[4.2.1 Create Supplier Confirmation (Optional) 30](#_Toc232850283)

[4.2.2 Approve Supplier Confirmation (Optional) 31](#_Toc232850284)

[4.2.3 Manage Supplier Confirmation (Optional) 32](#_Toc232850285)

[4.3 Monitor Confirmation/Situation 33](#_Toc232850286)

[4.3.1 Option A: Monitor Supplier Confirmations (Optional) 34](#_Toc232850287)

[4.3.1.1 Monitor Supplier Confirmations (Optional) 34](#_Toc232850288)

[4.3.1.2 Confirm Purchase Order (Optional) 35](#_Toc232850289)

[4.3.1.3 Monitor Supplier Confirmations (Optional) 36](#_Toc232850290)

[4.3.2 Option B: Detect and React to Situation 37](#_Toc232850291)

[4.3.2.1 Detect Critical Supply Situations(Optional) 37](#_Toc232850292)

[4.3.2.2 React to Critical Supply Situations (Optional) 37](#_Toc232850293)

[4.3.2.3 Monitor the Supplier Delivery Deficit (Optional) 38](#_Toc232850294)

[4.4 Create Inbound Deliveries 39](#_Toc232850295)

[4.4.1 Option A: Create Inbound Delivery 39](#_Toc232850296)

[4.4.2 Option B: Schedule Job for Inbound Delivery 40](#_Toc232850297)

[4.4.3 Handling Unit Management (Optional) 41](#_Toc232850298)

[4.5 Confirm Quantities for Putaway 42](#_Toc232850299)

[4.6 Post Goods Receipt for Inbound Delivery 43](#_Toc232850300)

[4.6.1 Option A: Post Goods Receipt 43](#_Toc232850301)

[4.6.2 Option B: Schedule Job for Goods Receipt 44](#_Toc232850302)

[4.7 Reverse Goods Receipt (Optional) 45](#_Toc232850303)

[4.8 Create Supplier Invoice 46](#_Toc232850304)

[4.8.1 Create Supplier Invoice with PO/GR Relation 46](#_Toc232850305)

[4.8.2 Post Supplier Invoice 47](#_Toc232850306)

[4.9 Approve Supplier Invoice (Optional) 48](#_Toc232850307)

[5 Appendix 50](#_Toc232850308)

[5.1 Process Integration 50](#_Toc232850309)

[5.1.1 Succeeding Processes 50](#_Toc232850310)

[5.2 Create Purchase Order (Enhanced Limit) 50](#_Toc232850311)

[5.3 Two Step Goods Receipt Process 51](#_Toc232850312)

[5.3.1 Create Inbound Delivery 52](#_Toc232850313)

[5.3.2 Post Goods Receipt Financially 52](#_Toc232850314)

[5.3.3 Confirm Quantities for Putaway (Optional) 54](#_Toc232850315)

[5.3.4 Post Goods Receipt Physically 54](#_Toc232850316)

## Purpose

Overview

Starting with the creation of a purchase order, the actual supply situation can be monitored and planned. The subsequent creation of an inbound delivery enables the user to process enhanced procurement processes including the goods receipt and the putaway. The procurement process is enclosed with the creation of a supplier invoice.

This document provides a detailed procedure for testing this scope item after solution activation, reflecting the predefined scope of the solution. Each process step, report, or item is covered in its own section, providing the system interactions (test steps) in a table view. Steps that are not in scope of the process but are needed for testing are marked accordingly. Project-specific steps must be added.

|  |
| --- |
| Note Values in this test script (decimal notation, date formats, and so on) are presented in U.S. standard notation. If your test system is set up to use a different notation, enter values as appropriate. |

## Prerequisites

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
| Master Data Specialist - Product Data | SAP_BR_PRODMASTER_SPECIALIST | Master Data - Products / Product Governance | SAP_BR_PRODMASTER_SPECIALIST / SAP_CMD_SPT_PR_GOV_PC |  |
| Purchaser | SAP_BR_PURCHASER | Purchasing / Sourcing and Contracting | SAP_MM_SPT_PURCHASING_PC / SAP_MM_SPT_SOURCING_PC |  |
| Inventory Manager | SAP_BR_INVENTORY_MANAGER | Inventory Management | SAP_BR_INVENTORY_MANAGER |  |
| Warehouse Clerk | SAP_BR_WAREHOUSE_CLERK | Inventory Processing | SAP_BR_WAREHOUSE_CLERK |  |
| Accounts Payable Accountant | SAP_BR_AP_ACCOUNTANT | Accounts Payable / Central Invoice Management - Supplier Invoices / Central Invoicing - Supplier Invoice | SAP_BR_AP_ACCOUNTANT / SAP_MM_SPT_CIM_INV_PC / SAP_MM_SPT_CNTRL_INVOICING_PC |  |
| Configuration Expert - Business Process Configuration | SAP_BR_BPC_EXPERT | Business Process Configuration / Business Process Configuration - Finance / Business Process Configuration - Procurement / Manage your Solution / Business Process Configuration - Workflow / Business Configuration - Feature Management / Business Process Configuration - Extensibility Explorer / Business Configuration - Transportation | SAP_BR_BPC_EXPERT / SAP_FIN_SPT_BPC_EXPERT_PC / SAP_MM_SPT_BIZ_PROC_CONFIGN_PC / SAP_CA_SPT_IC_LND_BASE_PC / SAP_CA_SPT_BPC_WORKFLOW_PC / SAP_CA_SPT_BPC_FM_PC / SAP_EI_SPT_BPC_EXT_PC / SAP_TM_SPT_TRANSPCFG_PC |  |
| Business Process Specialist | SAP_BR_BUSINESS_PROCESS_SPEC | Business Process Management / Business Process Management | SAP_BR_BUSINESS_PROCESS_SPEC / SAP_CA_SPT_BPS_PC |  |
| Receiving Specialist | SAP_BR_RECEIVING_SPECIALIST | Receiving | SAP_BR_RECEIVING_SPECIALIST |  |
| Administrator | SAP_BR_ADMINISTRATOR | Administration / Administration - Workforce Master Data / Administration - License Compliance / Administration - Data Management / Administration - Output Control | SAP_BR_ADMINISTRATOR / SAP_BUM_SPT_ADMINISTRATION_PC / SAP_EI_SPT_ADM_LC_PC / SAP_CA_SPT_TDR_PC / SAP_OC_SPT_ADMINISTRATION_PC |  |

### Master Data, Organizational Data, and Other Data

The organizational structure and master data of your company have been created in your system during implementation. The organizational structure reflects the structure of your company. The master data represents materials, customers, and vendors, for example, depending on the operational focus of your company.

|  |
| --- |
| Caution Update Behavior of Predelivered Demo DataIn non-productive environments (such as starter systems, sandbox systems, or partner demo systems), SAP initially deploys demo data for your selected scope. You can use this data to test and evaluate business processes.In a customer system, you can receive new or updated demo data after initial activation with further scope enhancements, provided the existing demo data wasn't changed in an incompatible way. If activation errors occur due to incompatible changes in demo data, you're responsible for resolving them. If you don't resolve the errors within a specific time frame, SAP reserves the right to deactivate demo data in your systems. In this case, you can continue by creating your own demo data. Alternatively, you can request that your systems be reprovisioned if you want to work with predelivered demo data again.In partner systems, you can use the demo data deployed with the initial activation. No additional demo data will be deployed in the system with scope enhancements. You can only create additional demo data manually. |

Use your own master data or the following sample data to go through the test procedure:

| Master data | Value | Master. data details | Comments |
| --- | --- | --- | --- |
| Plant | 3310 | Plant 1 AE |  |
| Storage Location | 331A | Standard storage 1 | Shop floor w/o lean WM |
| Storage Location | 331B | Standard storage 2 | Shop floor w/o lean WM |
| Company Code | 3310 | Company Code 3310 |  |
| Purchase Organization | 3310 | Purch. Org. 3310 |  |
| Purchasing group | 002 | Group 002 | depending on material |
| Supplier | 33300001 | Domestic UAE Supplier 1 |  |
| Supplier | 33300003 | Domestic UAE Supplier 3 |  |
| Material | TG0011 | Trading Good for Regular Procurement (PD planning)no Serial no.; no batch |  |
| Material | TG0013 | Trad. Good 0013,PD,Regular Proc.no Serial no.; no batch |  |

For more information on creating these master data objects, see the following [Master Data Scripts (MDS)](https://help.sap.com/docs/s4hana-best-practices/s4cld2608-master-data)

Table 1: Master Data Script Reference

| Master Data Script ID | Description |
| --- | --- |
| BNF | Create Product Master of type "Trading Good" - MDS |
| BNE | Create Supplier Master - MDS |

### Business Conditions

| Scope Item | Business Condition |
| --- | --- |
| BNZ - Create New Open MM Posting Period - MDS | You have completed the step described in the Create New Open MM Posting Period - MDS master data script. Posting Period is up to date. |
| 31N - Situation Handling | This scope item must be installed for situation handling steps. |

### Preliminary Steps

#### Open New MM Period

External Process

For this activity, run the following steps from the Create New Open MM Posting Period - MDS (BNZ) to close MM period and open new posting period.

• Closing MM Period and Opening New Posting Period

#### Create Manage Team and Responsibilities

Context

In this procedure, you create manage team and responsibilities for the supplier confirmation.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log onto Fiori Launchpad | Log onto the SAP Fiori launchpad using the Configuration Expert - Business Process Configuration role. | The Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Teams and Responsibilities - Procurement (F2412). | The Team screen displays. |  |
| 3 | Create manage team and responsibilities | Choose Create and make the following entries:Name:Z_SUPPLIER_CONFIRMATIONDescription: for supplier confirmationGlobal ID: Team_SCStatus: EnableType:OPPURGo to the Responsibility Definitions area, and make the following entries:Material: TG0011Go to the Team Members area, and choose Create , then make the following entries on the next screen:Business Partner: Select from F4 For example: search Last Name for *Purchaser*to get the user ID.Functions: OP_PURCH (Operational Purchasing) |  |  |
| 4 | Save Team | Choose Create. | The team has been created. |  |

#### Create Situation Template

Context

In this procedure, you can create situation type for the supplier confirmation.

|  |
| --- |
| Note 31N - Situation Handling is required to execute this step. |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log onto Fiori Launchpad | Log onto the SAP Fiori launchpad using the Business Process Specialist role. | The Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Situation Types (F2947). | The Manage Situation Types screen displays. |  |
| 3 | Copy standard situation template | On the Manage Situation Types screen, There are two tabs Situation Templates and Situation Types.Choose Situation Templates tab. Enter PROC_PENDINGSUPPLIERCONF_V2 in the ID field and choose Go to search the Standard Situation Templates.Choose standard situation template: PROC_PENDINGSUPPLIERCONF_V2 (for example) and choose Copy. |  |  |
| 4 | Create Custom Situation template | It will create a ready-to-use situation type.On the Situation Type screen, make the following entries:ID: Z_ST_SUPPLIER_CONFIRMATION (for example)This field is the unique identifier of a ready-to-use situation type. The ID of a ready-to-use situation type should start with 'Z' or 'Y'. ID is a mandatory field and cannot be left blank.Name: SUPPLIER CONFIRMATION FOR TESTING (for example)This field is the name of the ready-to-use situation type.Click the Situation Display tab, and go to the Notification tab.Resend Notifications: XIn the Condition section, make following entries:Purchasing Group:002(for example)Supplier: 33300001(for example)The Condition Range is based on the Order with two flags Create/Keep Instance and Send Notification and corresponding to each order there are list of Attributes coming from Trigger Object View. Here the values can be maintained corresponding to each attribute. The evaluation of the condition can be triggered by an Event or by a Batch Report which would be triggered Daily or Hourly.Once the Condition is met, the Situation Engine would be triggered with a Set of Anchor Object keys which is returned from Trigger Object CDS when queried with the set of Condition Attribute Value pairs maintained here corresponding to each Order. If the same Anchor Object Key is returned from the query of different order attributes then the flag of Create Instance and Send Notification will be from the higher rank.Go to section Recipients and make the following entries:Team Category: ProcurementFilter by Member Function: Operational Purchasing(for example) | The team has been created. |  |
| 5 |  | Go to section Situation Monitoring and choose Monitor Instances. | Monitoring of Situation Instances has been activated. |  |
| 6 |  | Go to the section Batch Job Scheduling: choose one time zone in the field: Time Zone and maintain the time for the field: Start Batch Job At. |  |  |
| 7 | Save situation template | Choose Create. | The situation template has been saved. |  |
| 8 | Enable situation template | One the popup window, choose Yes. |  |  |
| 9 | Repeat the above steps | Choose Situation Templates tab and choose Go to search the Standard Situation Templates: PROC_POITEMCONFQTYDEFICITChoose standard situation template: PROC_POITEMCONFQTYDEFICIT and choose Copy.On Situation Template screen, make the following entries:ID: Z_ Z_Supplier_Delivery_Deficit (for example)Name: Supplier Delivery Deficit (for example)Go to section Recipients and make the following entries:Member Function: Operational PurchasingGo to section Situation Monitoring and choose Monitor Instance from Check Box.Go to section Batch Job Scheduling and choose one time zone and set the time for the filed Start Batch Job At.Choose Create.One the popup window, choose Yes. |  |  |

#### Monitor Situations

Context

Here you can monitor activities of Situation Instances with respect to their Situation Types, e.g. instance created or set to done.

To allow an analysis of monitored data a Situation type (see previous section) must have been created and Situation Instances should have been generated (e.g. by a daily job).

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log onto SAP Fiori Launchpad | Log onto the SAP Fiori launchpad using the Configuration Expert - Business Process Configuration role. | The Fiori Launch Pad is displayed. |  |
| 2 | Access the App | Open Monitor Situations (F3264). | The Monitor Situations screen displays. |  |
| 3 | Monitor Situation Instance Activities | On the Monitor Situations screen, use the following system default values:Year: current year, default value, mandatorySituation Type ID: Z_ST_SUPPLIER_CONFIRMATION (for example) | The activities of the Situation Instances can be monitored. |  |
| 4 | Search for Anchor Object Key | Search for the Anchor Object Key which contains the Business Object. Purchase Order/Item/Schedule Line for example | The activities of the of a single Anchor Object can be monitored. |  |
| 5 | Choose Go | Choose Go to check the instance details. | The situation can be monitored. |  |

#### Create Purchasing Info Record (Optional)

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
| 1 | Log on | Log onto the SAP Fiori launchpad as a Purchaser . | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the App | Open Manage Purchasing Info Records (F1982). | The Manage Purchasing Info Records screen is displayed. |  |
| 3 | Open New Purchasing Info Record | Choose Create. | The Purchasing Info Record Screen is displayed. |  |
| 4 | Enter Header Data | Make the following entries:Purchasing Info Record Category: <Standard>Purchasing Organization: 3310Supplier: 33300001Material: TG0011 /TG0013Plant: 3310Purchasing Group: 002 | Header data is added. |  |
| 5 | Enter General Information | Make the following entries:Available From: TodayAvailable To: Today + 1 year | General Information is added. |  |
| 6 | Enter Purchasing Data | Make the following entries:Incoterm: for example, EXWNote Incoterms and their corresponding versions are grouped in the F4 value help. Selecting an incoterm automatically populates its associated version, which can be subsequently modified or removed if needed.Incoterm Location 1: Incoterm location1 | Purchasing Data is added. |  |
| 7 | Enter Delivery and Quantity Data | Make the following entries:Delivery Time in Days: 10 DaysUnder Delivery Tolerance in %: 10.0Over Delivery Tolerance in %: 10.0Tax Code: <Input Tax Code>Note If time dependent tax (TDT) is activated, and fields Country/Region Key for company code, Validity Periods and Tax Code are maintained via SSCUI 101016 in SAP S/4HANA Cloud Public Edition or the configuration activity Define Tax Codes for Sales and Purchases in Central Business Configuration, you must maintain the Tax Rate Valid From field in the New Purchasing Info Record screen. If you enter the current date, this date will be adjusted to a valid start date for your tax code according to the SSCUI/configuration activity settings.If Registration for Indirect Taxation Abroad (RITA) is activated, and tax registration country and tax code are maintained for company code via SSCUI 103464 in SAP S/4HANA Cloud Public Edition or the configuration activity Activate RITA and Maintain Tax Registration Countries in Central Business Configuration, you must maintain the Tax Country field. The default value of this field is the country ID of company code, but you can change it to a valid country ID that is maintained in the SSCUI/configuration activity accordingly.Order Unit: PCStandard Order Quantity: 1Select the following entries if required:Goods-Receipt-Based Invoice VerificationNo Evaluated Receipt Settlement | Delivery and Quantity Data is added. |  |
| 8 | Enter Condition Data | In the Condition section, choose Create.In the General Information area, make the following entries:Valid From: TodayValid To: Today+1yearAmount: 10Pricing Unit: 1Currency: AEDChoose Apply. | Condition Data is added |  |
| 9 | Enter Reference Data (optional) | Optionally, you can enter reference data. | Reference data is added. |  |
| 10 | Save your data | Choose Create. | The purchasing info record is saved. |  |

#### Set up Confirmation Control

Purpose

This is the perquisition step for setting confirmation control.

Procedure

Depending on your configuration environment for SAP S/4HANA Cloud Public Edition, choose one of the following options:

Configure Your Solution:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as a Configuration Expert - Business Process Configuration. | The SAP Fiori Launchpad is displayed. |  |
| 2 | Access App | Open Manage Your Solution (F1241). | The Manage Your Solution screen is displayed. |  |
| 3 | Open Configure Your Solution | Choose Configure Your Solution.Note To create country-/region-dependent settings for the intended local version, choose Set Local Version. | The Configure Your Solution screen is displayed. |  |
| 4 | Set the confirmation control | Input the Set Up Confirmation Control, then click the Search.When the SSCUI appear, choose Configure.On the Set Up Confirmation Control: Change screen, choose 0001 Confirmations.Then double click the Confirmation sequence, and make bellow entries:For the Confirmation Category: LA Inbound DeliveryReference Date: 2 Delivery date minus monitoring timeSubject to reminder (Sbj.to Rem.): Enable | Update the setting for for confirmation control. |  |
| 5 | Save the setting | Choose Save. |  |  |

SAP Central Business Configuration:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the project experience in SAP Central Business Configuration. | The SAP Fiori Launchpad displays. |  |
| 2 | Open Set Up Confirmation Control | Go to the Configuration app. You can search for a configuration activity and navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori Launchpad as a Configuration Expert - Business Process Configuration (SAP_BR_BPC_EXPERT).Search for Set Up Confirmation Control. |  |  |
| 3 | Set the confirmation control | On the Set Up Confirmation Control: Change screen, choose 0001 Confirmations.Then double click the Confirmation sequence, and make bellow entries:For the Confirmation Category: LA Inbound DeliveryReference Date: 2 Delivery date minus monitoring timeSubject to reminder (Sbj.to Rem.): Enable | Update the setting for for confirmation control. |  |
| 4 | Save the setting | Choose Save. |  |  |

#### Output Parameter Determination for Order Acknowlegement

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This is the perquisition step for the purchase order acknowledgement steps.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log onto Fiori Launchpad | Log onto the SAP Fiori launchpad using the Administrator role. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Output Parameter Determination. | The Output Parameter Determination screen displays. |  |
| 3 | Create Output Type for Order Acknowledgement | On the Output Parameter Determination screen, choose Show Rules for: Purchase Order, and Determination Step :Output Type.On section Maintain Business Rules, choose Edit and choose Insert New Row (+), then make bellow entries:Output Type: PURCHASE_ORDER_ACKNOWLEDGMENT (Purchase Order Output type for Order Acknowledgement)Dispatch Time : 1 (Immediately)Choose Activate | Output type Purchase Order Acknowledgement is created. |  |
| 4 | Create Receiver for Order Acknowledgement | On the Output Parameter Determination screen, choose Show Rules for: Purchase Order, and Determination Step :Receiver.On section Maintain Business Rules, choose Edit and choose Insert New Row (+), then make bellow entries:Output Type: PURCHASE_ORDER_ACKNOWLEDGMENT (Purchase Order Output type for Order Acknowledgement)Role : LFExclusive Indicator: -(false)Choose Activate | The Receiver for Order Acknowledgement is created. |  |
| 5 | Create Channel for Order Acknowledgement | On the Output Parameter Determination screen, choose Show Rules for: Purchase Order, and Determination Step :Channel.On section Maintain Business Rules, choose Edit and choose Insert New Row (+), then make bellow entries:Output Type: PURCHASE_ORDER_ACKNOWLEDGMENT (Purchase Order Output type for Order Acknowledgement)Role : LFChannel : PRINT (Printout)Exclusive Indicator: -(false)Choose Activate | The Channel for Order Acknowledgement is created. |  |
| 6 | Create Printer Settings for Order Acknowledgement | On the Output Parameter Determination screen, choose Show Rules for: Purchase Order, and Determination Step :Printer Settings.On section Maintain Business Rules, choose Edit and choose Insert New Row (+), then make bellow entries:Output Type: PURCHASE_ORDER_ACKNOWLEDGMENT (Purchase Order Output type for Order Acknowledgement)Role : LFPurchasing Org . :Print Queue : DEFAULTNumber of Copies: 1Choose Activate. | The Printer Settings for Order Acknowledgement is created. |  |
| 7 | Create Form Template for Order Acknowledgement | On the Output Parameter Determination screen, choose Show Rules for: Purchase Order, and Determination Step :Form Template.On section Maintain Business Rules, choose Edit and choose Insert New Row (+), then make bellow entries:Role : LFOutput Type: PURCHASE_ORDER_ACKNOWLEDGMENT (Purchase Order Output type for Order Acknowledgement)Channel : PRINT(Printout)Form Template: MM_PUR_ORDER_ORDACK_REMChoose Activate | The Form Template for Order Acknowledgement is created. |  |
| 8 | Create Output Relevance for Order Acknowledgement | On the Output Parameter Determination screen, choose Show Rules for: Purchase Order, and Determination Step :Output Relevance.On section Maintain Business Rules, choose Edit and choose Insert New Row (+), then make bellow entries:Output Type: PURCHASE_ORDER_ACKNOWLEDGMENT (Purchase Order Output type for Order Acknowledgement)Relevance Indicator : X(true)Choose Activate | The Output Relevance for Order Acknowledgement is created. |  |

#### Create Purchase Order for Order Acknowledgement

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
| 1 | Log On | Log on to the SAP Fiori launchpad as a Purchaser. |  |  |
| 2 | Access the App | Open Create Purchase Order - Advanced (ME21N). | The Create Purchase Order screen is displayed. |  |
| 3 | Enter Purchase Order Data | Enter all of the necessary data.Order Type: NB Standard POSupplier: 33300001In Header section, on the Org. Data tab, make the following entries:Purch.Org.: 3310Purchasing Group:002Company Code: 3310In Items section,Material: TG0011Plant: 3310Storage Location: 331AQuantity: 10Deliv.Date: TodayNet Price: XAEDInvoice Receipt: <selected>Verify if Goods-Receipt-Based Invoice Verification is selected.Go to Invoice tab, and make the following entry:Tax Code: for example, <Input Tax Code>Tax Date: <Default Value>Go to Confirmation Tab:Conf. Control: ConfirmationsAcknowl.Reqd: Enable | The Create Purchase Order screen is displayed. |  |
| 4 | Save Purchase Order | Choose Save and when the purchase order number is displayed, write it down for further use. | A new Purchase Order is created.Purchase Order Number is displayed. |  |

#### Confirmation for Purchase Order

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
| 1 | Log On | Log on to the SAP Fiori Launchpad as a Purchaser. |  |  |
| 2 | Access App | Open Change Purchase Order - Advanced (ME22N) . | The Change Purchase Order - Advanced (ME22N)screen is displayed. |  |
| 3 | Enter Purchase Order data | Open the Purchase order in last step. Choose Display/Change button to change the Purchase Order.Go to Confirmation Tab:Maintain the entry:CC:ABDeliver Date: Today + 5Quantity: 5 PCMaintain the entries in the next line:CC:LADeliver Date: Today + 5Quantity: 5 PCChoose Enter to confirm the warning message. | The Create Purchase Order screen is displayed. |  |
| 4 | Save Purchase Order | Choose Save and when the purchase order number is displayed, write it down for further use. | A new Purchase Order is created.Purchase Order Number is displayed. |  |

#### Schedule Order Acknowledgement output for Purchase Orders (Optional)

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
| 1 | Log On | Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. | The SAP Fiori launchpad displays. |  |
| 2 | Access App | Open Schedule Order Acknowledgement output for Purchase Orders (F7082) | The Application Jobs screen displays |  |
| 3 | Create Job | Choose Create. | The New Job screen displays. |  |
| 4 | Define a Job | On the New Job: Schedule Order Acknowledgement output for Purchase Orders screen,go to 1. Template Selection area, make the following entries:Job Template: <Job Template>, for example, Schedule Order Acknowledgement output for Purchase OrdersJob Name: <Job Name>, for example, Schedule Order Acknowledgement output for Purchase OrdersChoose Step 2 and go to 2. Scheduling Options area and make the following entries:Start Immediately : <selected>Job Start: <Current Time>Choose Step 3 and go to 3. Parameters area and make the following entries:Purchasing document: <use a PO you created previously>Document Type: <NB>Set Parameter settings according to your needs.Choose Schedule. | The job is created. |  |
| 5 | Order Acknowledgement output for Purchase Orders created | On the Application Jobs screen.Go to Jobs (X) area and check the status until it changes to Finished. |  |  |
| 6 | Check Result | Click on Logs to navigate to the job log. |  |  |

#### Order Acknowledge on Purchase Orders

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
| 1 | Log On | Log on to the SAP Fiori Launchpad as a Purchaser. | The SAP Fiori launchpad displays. |  |
| 2 | Access App | Open Order Acknowledgement on Purchase Order - Advanced (ME92FF) | The Order Acknowledge on Purchase Order Advanced screen displays. |  |
| 3 | Define Purchasing Document Data | On the Monitor Receipt of Order Acknowledgments: S/4HANA Output Management screen, make the following entries:Purchasing document: <use a PO you created previously>Generate and Save Messages: SelectedChoose Execute (F8). | The Purchasing Document Data has been defined. |  |
| 4 | Check the log | It will appear one message of Successful processing, if there is no error in the PO. | Message saved. |  |

#### Supplier Confirmation Workflow (Optional)

##### Activate Flexible Workflows for Supplier Confirmation (Optional)

Purpose

In this procedure, you check the flexible workflow for Supplier Confirmation approval.

When you use the flexible workflow to approve the supplier confirmation, make sure Flexible Workflow for Supplier confirmation is activated, and Flexible Workflow for Supplier Confirmation Approval is configured.

Procedure

Depending on your configuration environment for SAP S/4HANA Cloud Public Edition, choose one of the following options:

Configure Your Solution:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as a Configuration Expert - Business Process Configuration. | The SAP Fiori Launchpad is displayed. |  |
| 2 | Access App | Open Manage Your Solution(F1241). | The Manage Your Solution screen is displayed. |  |
| 3 | Open Configure Your Solution | Choose Configure Your Solution.Note To create country-/region-dependent settings for the intended local version, choose Set Local Version. | The Configure Your Solution screen is displayed. |  |
| 4 | Open Active Flexible Workflow | On the Configure Your Solution: Realize Phase screen, search Activate Flexible Workflows for Supplier Confirmations, then choose Search.Select the line of the item and go to the next screen.On the Configure Your Solution - Purchase Order Processing screen, choose Configure on the line of configuration step with name Activate Flexible Workflows for Supplier Confirmation . | The Activate Flexible Workflows for Supplier Confirmation screen is displayed. |  |
| 5 | Check Flexible Workflows for Supplier Confirmation | Make the following entries:Purchasing Doc. Type: NBConf. WF: <Selected> | The supplier confirmation workflow is active for Purchase Orders with Document Type: NB. |  |
| 6 | Save | Choose Save. |  |  |

SAP Central Business Configuration:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the project experience in SAP Central Business Configuration. | The SAP Fiori Launchpad displays. |  |
| 2 | Open Active Flexible Workflow | In the Product-Specific Configuration phase, navigate to the Configuration Activities tab. To locate the activity in the tree view, search for the following activity: Activate Flexible Workflows for Supplier Confirmation.Choose Open Documentation for the found line item to see more details about this configuration activity.Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. |  |  |
| 3 | Open Active Flexible Workflows | On the Configure Your Solution: Realize Phase screen, search Activate Flexible Workflows for Supplier Confirmations, then choose Search.Select the line of the item and go to the next screen.On the Configure Your Solution - Purchase Order Processing screen, choose Configure on the line of configuration step with name Activate Flexible Workflows for Supplier Confirmation . | The Activate Flexible Workflows for Supplier Confirmation screen is displayed. |  |
| 4 | Check Flexible Workflows for Supplier Confirmation | Make the following entries:Purchasing Doc. Type: NBConf. WF: <Selected> | The supplier confirmation workflow is active for Purchase Orders with Document Type: NB. |  |
| 5 | Save | Choose Save. |  |  |

Result

The supplier confirmation workflow is active for Purchase Orders with Document Type: NB.

##### Manage Workflows for Supplier Confirmations (Optional)

Purpose

In this procedure, you configure the release conditions for Supplier Confirmations.

|  |
| --- |
| Note Note When you start to process this step, please make sure that the flexible workflow for supplier confirmation has been activated in your system. |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Workflows for Supplier Confirmations(F6194). | The Manage Workflows screen displays. |  |
| 3 | Create Manage Workflow | Choose Create, and make the following entry:Workflow Name: Test Workflow for Supplier ConfirmationFrom the Start Conditions section, add the following preconditions:Purchasing group of purchase order: SelectedPurchasing Group: 003Choose Create another condition, and make the following entries:Supplier for confirmation is: SelectedSupplier: For example, 10300003In the Steps area, choose Create and make the following entries:Step Type: Release of Supplier ConfirmationIn the Recipients area, make the following entries:Assignment By: UserUser: Select User from value help (with Employee ID PURCHASING_MANAGER) Choose OK.Step to be completed by: One of the recipients.Choose Create.Choose Save. | The Workflow for Supplier Confirmation is configured. |  |
| 4 | Activate Workflow Item | Select the Workflow Item just created, and choose Activate. | The Workflow Item is activated. |  |

|  |
| --- |
| Note Note Please make sure default workflow Automatic Release of Supplier Confirmation has been activated. |

## Overview Table

|  |
| --- |
| Note If your system administrator has enabled spaces and pages on the SAP Fiori launchpad, the homepage will only contain the essential apps for performing the typical tasks of a business role.You can find all other (searchable) apps not included on the homepage using the search bar ([2434549](https://me.sap.com/notes/2434549)).If you want to personalize the homepage and include the hidden apps, navigate to your user profile and choose App Finder. |

| Process Step | Business Role | Transaction/App | Expected Results |
| --- | --- | --- | --- |
| [Create Purchase Order Manually](#unique_23) [page ] 27 | Purchaser | Manage Purchase Orders (F0842A) | The Purchase Order is created. |
| [Monitor Confirmation/Situation](#unique_24) [page ] 33 | Purchaser | Monitor Supplier Confirmations (F2359) | The Monitor Supplier Confirmations (F2359) screen is displayed. |
| [Create Inbound Deliveries](#unique_25) [page ] 39 |  |  |  |
| [Option A: Create Inbound Delivery](#unique_26) [page ] 39 | Receiving Specialist | Inbound Deliveries for Purchase Orders (VL34) | The Generation of Inbound Delivery screen appears. |
| [Option B: Schedule Job for Inbound Delivery](#unique_27) [page ] 40 | Receiving Specialist | Schedule Inbound Delivery Creation (F2798) | A delivery creation job is scheduled. |
| [Handling Unit Management (Optional)](#unique_28) [page ] 41 |  |  |  |
| [Confirm Quantities for Putaway](#unique_29) [page ] 42 | Receiving Specialist | Inbound Deliveries for Putaway (VL06IP) | The Inbound Deliveries for Putaway (VL06IP) Screen appears. |
| [Post Goods Receipt for Inbound Delivery](#unique_30) [page ] 43 |  |  |  |
| [Option A: Post Goods Receipt](#unique_31) [page ] 43 | Receiving Specialist | Post Goods Receipt for Inbound Delivery (F2502) | Goods receipt is posted. |
| [Option B: Schedule Job for Goods Receipt](#unique_32) [page ] 44 | Receiving Specialist | Schedule Goods Receipt For Inbound Deliveries (F2776) | A schedule goods issue for deliveries job is scheduled. |
| [Reverse Goods Receipt (Optional)](#unique_33) [page ] 45 | Receiving Specialist | Reverse Goods Receipt for Inbound Delivery (VL09) | The Reverse Goods Movement screen appears. |
| [Create Supplier Invoice](#unique_34) [page ] 46 |  |  |  |
| [Create Supplier Invoice with PO/GR Relation](#unique_35) [page ] 46 | Accounts Payable Accountant | Create Supplier Invoice (F0859) | The Supplier Invoice is posted. |
| [Post Supplier Invoice](#unique_36) [page ] 47 | Accounts Payable Accountant | Supplier Invoices List (F1060A) | The Supplier Invoice is posted. |
| [Approve Supplier Invoice (Optional)](#unique_37) [page ] 48 | Accounts Payable Accountant | Supplier Invoices List (F1060A) | The Supplier Invoices is approved. |

## Test Procedures

This section describes test procedures for each process step that belongs to this scope item.

### Create Purchase Order Manually

In this activity, you create the purchase order. You have two options

Option A: Create Purchase Order with Confirmation

Option B: Create Purchase Order with Inbound Delivery

#### Option A: Create Purchase Order with Confirmation

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this procedure, you create a purchase order for stock material directly.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log onto the SAP Fiori Launchpad as Purchaser. |  |  |
| 2 | Access the App | Open Manage Purchase Orders (F0842A) . | The Manage Purchase Order screen is displayed. |  |
| 3 | Enter Purchase Order data | Choose Create, and enter all of the necessary data.In General Information section:Supplier: 33300001Currency: AEDPurchasing Organization:3310Purchasing Group:002Company Code: 3310In Items section, choose Create button and make the following entries:Material: TG0011Plant: 3310Storage Location: 331AQuantity: xNet Price: xClick this item, then choose Supplier Confirmation Control tab:Confirmation Control: ConfirmationsChoose Schedule Lines tab:Delivery Date: <Today>Choose Apply. | The Create Purchase Order screen is displayed. |  |
| 4 | Save Purchase Order | Choose Order and when the purchase order number is displayed, write it down and record the delivery date for further use. | A new Purchase Order is created. Purchase Order Number is displayed. |  |

#### Option B: Create Purchase Order with Inbound Delivery

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

You perform this activity when you want to display your Purchase Requisitions and assign them to a Source of Supply.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log onto the SAP Fiori Launchpad as Purchaser . |  |  |
| 2 | Access the App | Open Manage Purchase Orders (F0842A) . | The Manage Purchase Order screen is displayed. |  |
| 3 | Enter Purchase Order data | Choose Create, and enter all of the necessary data.In General Information section:Supplier: 33300001Currency: AEDPurchasing Organization:3310Purchasing Group:002Company Code: 3310In Items section, choose Create button and make the following entries:Material: TG0011Plant: 3310Storage Location: 331AQuantity: xNet Price: xClick this item, then choose Supplier Confirmation Control tab:Confirmation Control: Inbound DeliveryChoose Schedule Lines tab:Delivery Date: TodayChoose Apply. | The Create Purchase Order screen is displayed. |  |
| 4 | Save Purchase Order | Choose Order and when the purchase order number is displayed, write it down and record the delivery date for further use. | A new Purchase Order is created.Purchase Order Number is displayed.Note If the Purchaser Order needs to be approved, please refer the step Approve Purchase Order (Optional) in scope item J45 Procurement of Direct Materials. |  |

### Supplier Confirmation (Optional)

#### Create Supplier Confirmation (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this procedure, you create a supplier confirmation for stock material directly. Before processing this step, you must first complete the "Create Purchase Order with Confirmation" step.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log onto SAP Fiori Launchpad | Log onto the SAP Fiori Launchpad using the Role Purchaser. | The Fiori Launchpad is displayed. |  |
| 2 | Access the App | Open Manage Supplier Confirmations(F5039). | The Manage Supplier Confirmation screen is displayed |  |
| 3 | Choose Create | Choose Create. | The Supplier Confirmation screen is displayed. |  |
| 4 | Enter Reference Purchase Order | Enter Reference Purchase Order that was created on step (Option A: Create Purchase Order with Confirmation) | The purchase order number is entered. |  |
| 5 | Enter Supplier Reference | Enter Supplier Reference: 33300001 | The Supplier is entered. |  |
| 6 | Choose Create | Choose Create in Confirmation Item |  |  |
| 7 | Create Supplier Confirmation Item | Enter all of the necessary data in screen Supplier Confirmation Item.Supplier Reference: 33300001Item: 10Confirmed Net Order Price: <Default Value>Note If you want to enter the confirmed Net Order price, you can use the SSCUI 101718 (Set Up Confirmation Control) to click the Price for confirmation Category AB.Confirmed Price Unit: <Default Value> | The Supplier Confirmation Item is entered. |  |
| 8 | Create Confirmation Line Data | Choose Create to enter the following values in tab: Confirmation LineDelivery Date: TodayConfirmed Quantity: <same as PO quantity> | The Confirmation Line Data is entered. |  |
| 9 | Choose Apply | Choose Apply. |  |  |
| 10 | Create Supplier Comments | Go to the Section Item Notes, and click Create to drop down and select Supplier Comments in Supplier Confirmation Item. Enter some comments （For Example: Test for Supplier Confirmation）in the popup screen. Choose Create in the popup screen. | Supplier Comments are now created and visible. |  |
| 11 | Choose Create | Choose Create. |  |  |
| 12 | Choose Save | Choose Save to confirm the warning message. | The Supplier Confirmation is created. |  |

#### Approve Supplier Confirmation (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

If the supplier is 10300003 and purchase group is 003, then supplier confirmation should be approved. To decide which supplier confirmation need approval, please refer to Manage Workflows for Supplier Confirmations.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log onto SAP Fiori Launchpad | Log onto the SAP Fiori Launchpad using the Role Purchasing Manager. | The Fiori Launchpad is displayed. |  |
| 2 | Access the App | Open My Inbox - All Items(F0862). | A list of existing Purchase Documents are displayed. |  |
| 3 | Search for Supplier Confirmation Status | Make the following entry and choose Enter.Search: <Supplier Confirmation number> | The Supplier Confirmation is displayed. |  |
| 4 | Approve Supplier Confirmation | Select the Supplier Confirmation on the left side of the screen and choose Approve at the bottom right. | The Submit Decision screen is displayed. |  |
| 5 | Enter Approval Reason | Enter the approval reason if necessary and then choose Submit. | The Supplier Confirmation is approved. |  |

#### Manage Supplier Confirmation (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

Manage Supplier Confirmation is used in the procurement process to track and manage responses from suppliers regarding purchase orders.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log onto SAP Fiori Launchpad | Log onto the SAP Fiori Launchpad using the Role Purchaser. | The Fiori Launchpad is displayed. |  |
| 2 | Access the App | Open Manage Supplier Confirmations(F5039). | The Manage Supplier Confirmation screen is displayed |  |
| 3 | Search for Supplier Confirmations | The basic filters are displayed.Purchase Order, Supplier, Created By, and so on.Make the above entries accordingly, then choose Go. | The Supplier Confirmation screen is displayed. |  |
| 4 | Check the Supplier Confirmation Processing Status | Select the supplier confirmation and check its Processing Status. | The purchase order number is entered. |  |
| 5 | Click the navigation to view Confirmation details | Click the navigation icon (>) to view the supplier confirmation’s General information. |  |  |
| 6 | Go to Confirmation Item | Go to the tab Confirmation Item and choose the Confirmation Item and click the navigation icon (>) |  |  |
| 7 | Review Confirmation Item | On the Supplier Confirmation Item screen, you can review the following entries:Delivery Date: <Default Value>Confirmed Quantity: <Default Value> | You have reviewed the supplier confirmation item. |  |

### Monitor Confirmation/Situation

Please use the the purchase order created in the step: [Option A: Create Purchase Order with Confirmation](#unique_39) [page ] 27

#### Option A: Monitor Supplier Confirmations (Optional)

##### Monitor Supplier Confirmations (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This activity you can monitor purchase documents awaiting supplier confirmations.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Open the Fiori Launch Pad with the Purchaser role. | The Fiori Launch Pad is displayed. |  |
| 2 | Access the App | Open Monitor Supplier Confirmations (F2359) . | The Monitor Supplier Confirmations screen is displayed. |  |
| 3 | Search for Purchase Orders | Make the following filters in top filter bar then choose Go:Display Currency: AEDConfirmation Category: INBOUND DELIVERY(LA)/Order Acknowledgment (AB) | The Purchase Document is displayed mentioning Scheduled date, Scheduled Quantity and Committed Quantity. |  |
| 4 | Display Purchase Order Item Details | Choose the individual line item of the Purchase Document where you want to display the PO details. | The Purchase Order Item screen is displayed. |  |
| 5 | Verify data displayed on the object page | Verify data displayed on the object page. | The data should be logically in sync with Purchase Order. |  |

##### Confirm Purchase Order (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

You perform this activity to confirm purchase order relative delivery information.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Open the Fiori Launch Pad with the Purchaser role. | The Fiori Launch Pad is displayed. |  |
| 2 | Access the App | Open Change Purchase Order - Advanced (ME22N) . | The Change Purchase Order - Advanced screen is displayed. |  |
| 3 | Enter Purchase Order data | Choose Other Purchase Order, then enter all of the necessary data.Pur. Order: the Purchase order number in step Create Purchase Order with ConfirmationChoose the Display/Change button to change the purchase order.Choose Other Document, then choose the Confirmations tab, and make below entries:CC: ABD: DDelivery Date: choose date:Time: choose timeQuantity: the same as PO Quantity in the PO item | The Create Purchase Order screen is displayed. |  |
| 4 | Save Purchase Order | Choose Save. | The confirmation of Purchase Order is done |  |

##### Monitor Supplier Confirmations (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

You can monitor purchase documents awaiting supplier confirmations in this activity.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Open the Fiori Launch Pad with the Purchaser role. | The Fiori Launch Pad is displayed. |  |
| 2 | Access the App | Open Manage Purchase Orders (F0842A) . | The Manage Purchase Order screen is displayed. |  |
| 3 | Choose the Purchase Order | Make the following filters in top filter bar then choose Go:Enter the Purchase Order number: the Purchase order number in step Create Purchase Order with Confirmation.Click the right arrow of PO item, then choose Supplier Confirmations tab. | The Purchase order detail is displayed. |  |
| 4 | Verify data displayed on the object page | You can see this confirmation detail information. |  |  |

#### Option B: Detect and React to Situation

##### Detect Critical Supply Situations(Optional)

Detect Critical Supply Situations

|  |
| --- |
| Note The system automatically detects critical supply situations, which refer to missing order acknowledgements. The detection process is automatically triggered by the system on a regular basis and indicates critical situations to the purchaser, using the notification functionality on the home screen. This enables the purchaser to proactively react to potential supply shortages and avoid negative implications to the business processes of the company. |

##### React to Critical Supply Situations (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This activity you can monitor purchase documents awaiting supplier confirmations through the notification.

|  |
| --- |
| Note There is daily job which has been setup in the system, and this job is running every day. If you do not receive any notifications in this step, you should wait for the whole day for the notification generation. |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Open the Fiori Launch Pad with the Purchaser role. | The Fiori Launch Pad is displayed. |  |
| 2 | Choose the notifications | Choose the Notifications icon which is at the top right of the Home screen.Choose the notifications: pending supplier confirmations (for example) which is generated by the system batch daily job. | The Monitor Supplier Confirmations screen is displayed. |  |
| 3 | Monitor Supplier Confirmations | On the Monitor Supplier Confirmations screen, use the following system default values:Display Currency: AEDSupplier Confirmation Category: Order Acknowledgement(AB) default valuePurchasing Group:002Supplier: 33300001Purchasing Document: default value | The purchase order can monitor the supplier confirmation. |  |
| 4 | Search PO | Choose Go to search for the PO which is created in the previous step. |  |  |

##### Monitor the Supplier Delivery Deficit (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This activity you can monitor purchase documents awaiting supplier confirmations through the notification.

|  |
| --- |
| Note There is daily job which has been setup in the system, and this job is running every day. If you do not receive any notifications in this step, you should wait for the whole day for the notification generation. |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Open the Fiori Launch Pad with the Purchaser role. | The Fiori Launch Pad is displayed. |  |
| 2 | Choose the notifications | Choose the Notifications icon which is at the top right of the Home screen.Choose the notifications: Supplier Delivery Deficit (for example) which is generated by the system batch daily job. | The Monitor Supplier Confirmations screen is displayed. |  |
| 3 | Check Supplier Delivery Deficit | On the Manage Purchase Order screen, you can check the detail of delivery of the purchase order. | The purchase order can monitor the supplier delivery detail information. |  |

### Create Inbound Deliveries

In this activity, you create the inbound deliveries. Please use the the purchase order created in the step: [Option B: Create Purchase Order with Inbound Delivery](#unique_40) [page ] 28

You have two options to create the inbound deliveries.

Option A: Create Inbound Delivery

Option B: Job Scheduling for Inbound Delivery Creation

You can choose either option A or option B to execute the inbound delivery creation. For more information, see the next two tasks.

|  |
| --- |
| Note Only choose option A or B (not both). |

#### Option A: Create Inbound Delivery

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
| 1 | Log on | Log onto the SAP Fiori Launchpad using the Role Receiving Specialist . | The Fiori Launchpad is displayed. |  |
| 2 | Access the App | Open Inbound Deliveries for Purchase Orders (VL34) . | The Generation of Inbound Deliveries screen displays. |  |
| 3 | Create Inbound Delivery | Make the following entries then choose Execute:Document Number: XXX (Enter the purchase order number created in previous step)Delivery Date: XXX Delete the default date and enter the delivery date in purchase order.Test Run: uncheckedThe Inbound Delivery Number is displayed, write it down for further use. | A new Inbound Delivery is created.The Inbound Delivery Number is displayed. |  |

#### Option B: Schedule Job for Inbound Delivery

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this process step, you can schedule a background job for creating inbound deliveries.

This app can be used as an alternative instead of the manual creation of inbound deliveries.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1. | Log on | Log onto the SAP Fiori Launchpad using Role Receiving Specialist . | The SAP Fiori Launchpad displays. |  |
| 2. | Access the App | Open Schedule Inbound Delivery Creation (F2798) . | The Application Jobs screen is displayed. The app automatically shows the history of application jobs. |  |
| 3. | Create Delivery Creation Schedule | Choose Create to define a new job. | The New Job screen displays. Job Template should default as Schedule Inbound Delivery Creation. |  |
| 4. | Job Parameters | Define scheduling options and parameters for the batch job if necessary, then choose Step 2.Start Immediately: SelectedChoose Step 3.Document Number: XXX Enter the purchase order numberDelivery Date to: XXX Delete the default date and enter the delivery date in purchase orderTest Run: Deselected | The system displays the message You can go ahead and schedule the job. |  |
| 5. | Schedule | Choose Schedule. | A delivery creation job is scheduled. Screen back to Application Jobs. |  |
| 6. | Check Delivery Creation Job Log | In screen Application Jobs, after job item’s status turned to Finished, choose Status symbol in column Log.Note Click Magnifier, the job list will refresh. | Screen goes to job log details. |  |

#### Handling Unit Management (Optional)

Purpose

You can execute packing for delivery items right in an inbound delivery.

Procedure

Complete all the activities related to inbound delivery described in the test script of 4MM - Handling Unit Management.

### Confirm Quantities for Putaway

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This activity confirms that all the materials have been put away in the correct quantities.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log onto the SAP Fiori Launchpad using the Role Receiving Specialist . | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Inbound Deliveries for Putaway (VL06IP) . | The Inbound Deliveries for Putaway screen displays. |  |
| 3 | Enter inbound delivery number | Make the following entries then choose Execute:Delivery Date: Delete the default dateInbound Delivery: XXX | The selected Inbound Delivery displays. |  |
| 4 | Change the inbound delivery | Select Inbound deliveries and click Change Inbound Deliveries. | The Inbound Delivery XXX Change: Overview screen displays. |  |
| 5 | Confirm Quantities for Putaway | In Item Overview tab, input the Putaway Qty: XXXNote The put away quantity should equal to the delivery QtyAnd choose Save. | Back to the Inbound Deliveries for Putaway screen and Inbound Delivery XXX has been saved message displays. |  |

### Post Goods Receipt for Inbound Delivery

In this activity, you post goods receipt for inbound deliveries. You have two options to post goods receipt for inbound deliveries:

Option A: Post Goods Receipt

Option B: Scheduling Job for Goods Receipt for Inbound Deliveries

You can choose either option A or option B to execute the inbound delivery creation. For more information, see the next two tasks.

#### Option A: Post Goods Receipt

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
| 1 | Log on | Log onto the SAP Fiori Launchpad using the Role Receiving Specialist . | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the App | Open Post Goods Receipt for Inbound Delivery (F2502). | The Goods Receipt screen displays. |  |
| 3 | Enter inbound delivery number | Make the following entries then choose Enter:Enter Inbound Delivery Number: XXX | The Goods Receipt screen displays.The selected Inbound Deliveries are shown. |  |
| 4 | Change the inbound delivery | Select the item for this inbound delivery. Choose Post. | The goods receipt is posted.A success message is shown. |  |

#### Option B: Schedule Job for Goods Receipt

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this process step, you can schedule a background job for goods receipt posting with reference to inbound deliveries.

This app can be used as an alternative instead of the manual goods receipt posting for inbound deliveries.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1. | Log on | Log onto the SAP Fiori Launchpad using Role Receiving Specialist . | The SAP Fiori Launchpad displays. |  |
| 2. | Access the App | Open Schedule Goods Receipt For Inbound Deliveries (F2776) . | The Application Jobs screen is displayed. The app automatically shows the history of application jobs. |  |
| 3. | Create Goods Issue Deliveries Schedule | Choose New to define a new job. | The New Job screen displays. Job Template should default as Schedule Goods Receipt for Inbound Deliveries. |  |
| 4. | Job Parameters | Choose Step 2 and make the following entries:Start Immediately: SelectedChoose Step 3.Inbound Delivery: XXX Enter the inbound delivery numberDelivery Date: Enter the delivery date in Inbound delivery | The system displays the message You can go ahead and schedule the job. |  |
| 5. | Schedule | Choose Schedule. | A schedule goods issue for deliveries job is scheduled. Screen back to Application Jobs. |  |
| 6. | Check Goods Issue Deliveries Job Log | In screen Application Jobs, after job item’s status turned to Finished, choose Status symbol in column Log.Note Click Magnifier, the job list will refresh. | Screen goes to job log details. |  |

### Reverse Goods Receipt (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

Goods ordered by a purchase order arrive at warehouse. The goods receipt is to be posted regarding the inbound delivery.

|  |
| --- |
| Note Reverse goods receipt is an optional step. But if you process this step, then you have to proceed with step: [Post Goods Receipt for Inbound Delivery](#unique_30) [page ] 43. |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log onto the SAP Fiori Launchpad using the Role Receiving Specialist . | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the App | Open Reverse Goods Receipt for Inbound Delivery (VL09) . | The Reverse Goods Movement Screen appears. |  |
| 3 | Enter inbound delivery number | Make the following entries then choose Execute:Inbound/Outbound Delivery: XXX | The selected Inbound Delivery is shown. |  |
| 4 | Reverse the Inbound Delivery | Select the inbound delivery and choose Reverse.A confirmation prompt is shown and choose Continue. | The selected Inbound Delivery is reversed. A successful error log is shown up. |  |

### Create Supplier Invoice

#### Create Supplier Invoice with PO/GR Relation

Purpose

In this activity, you perform the invoice verification.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Open the SAP Fiori launchpad with the Accounts Payable Accountant role. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the App | Open Create Supplier Invoice (F0859). | The New Supplier Invoice screen displays. |  |
| 3 | Enter General Data | In case of purchase orders created with local currency in your system, make the following entries.Transaction: InvoiceCompany Code: 3310Reference: Enter the reference document number of the supplier for example: 33300001Gross Invoice Amount : XXXCurrency: AEDInvoice Date: TodayPosting Date TodayBaseline Date: : Today (in Payment tab)Invoice Party: 33300001 |  |  |
| 4 | Enter Purchase Order References | In Purchasing Document References, make the following entries (use a PO you created previously) and Press Enter key.Make the following entries (use a PO you created previously).References Document Category: Purchase Order/ Scheduling AgreementPurchase Order: PO number | The Purchase Order References screen displays. |  |
| 5 | Select Purchase Order Items | Check the selection of the Purchase Order Items.Confirm the warning messages. | All items of the selected Purchase Order are added to the Purchase Order Item table. |  |
| 6 | Check the Purchase Order Items data | Check the Amount, the Quantity, the Tax Code (there may already be a tax code that was copied from the purchase order). | The Purchase Order Item's table displays. |  |
| 7 | Check Tax code | In the section Tax check if there is tax code information and enter the tax amount.when the tax code value is greater than zero | In the Tax tab, you should see the same tax codes as in the items.If there is no tax, specify the tax code <Input Tax Code>. |  |
| 8 | Check the balance | Calculate the tax amount from the item amount multiplied by the tax value. Check the balance (difference between the calculated amount and the gross Amount you entered in step 3). | The balance should be zero (or within the defined tolerance). |  |
| 9 | Simulate Supplier Invoice and Check Messages | Choose the Simulate button.You can check the simulation results in Simulation Overview and Simulation Details area. Choose Back. | The supplier invoice is simulated. |  |
| 10 | Save as Completed Invoice | Choose the Save as Completed.Note You can choose Park to park the invoice first. After that, you can edit the created supplier invoice to choose Save as Completed. |  |  |

#### Post Supplier Invoice

Purpose

In this step, a supplier invoice is posted

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Open the SAP Fiori launchpad with the Accounts Payable Accountant role. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the App | Open Supplier Invoices List (F1060A) . | The Supplier Invoices list screen is displayed. |  |
| 3 | Filter Supplier Invoice List | Fill in search criteria fields, and click on Go button.Invoicing Party: 33300001Invoice Document No.created in previous step | The Supplier Invoices list is displayed. |  |
| 4 | Check Supplier Invoice Detail | In the list of the Supplier Invoices, select an Invoice Document by clicking the entire row, which is blocked for payment. | The invoice document is displayed. |  |
| 5 | Post the invoice | Choose Post. | The invoice is posted. |  |
| 6 | Back to SAP Fiori Launch Pad | Choose the Home button to go back to the SAP Fiori launchpad. | The SAP Fiori launchpad is displayed. |  |

### Approve Supplier Invoice (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, a supplier invoice is approved.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Open the SAP Fiori launchpad with the Accounts Payable Accountant role. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the App | Open Supplier Invoices List (F1060A) . | The Supplier Invoices list screen is displayed. |  |
| 3 | Filter Supplier Invoice List | Fill in search criteria fields or leave them blank, and choose Go. | The Supplier Invoices list is displayed. |  |
| 4 | Check Supplier Invoice Detail | In the list of the Supplier Invoices, select an Invoice Document by clicking the entire row, which is blocked for payment. | The invoice document is displayed. |  |
| 5 | Release the Invoice | Choose Release. | The invoice is released. |  |
| 6 | Back to SAP Fiori Launch Pad | Choose Home to go back to the SAP Fiori launchpad. | The SAP Fiori launchpad is displayed. |  |

## Appendix

### Process Integration

The process to be test in this test script is part of a chain of integrated processes.

#### Succeeding Processes

After completing the activities in this test script, you can continue testing the following business processes:

| Process | Business Description |
| --- | --- |
| Accounts Payable-(J60) | Outgoing Payment |

### Create Purchase Order (Enhanced Limit)

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log onto the SAP Fiori Launchpad as Purchaser . |  |  |
| 2 | Access the App | Open Create Purchase Order - Advanced (ME21N) . | The Create Purchase Order screen is displayed. |  |
| 3 | Enter Purchase Order data | Enter all of the necessary data.Order type: NB Standard POSupplier: 33300001In Header section, on the Org. Data tab:Purchasing Org.: 3310Purchasing Group:001Company Code: 3310In Items Overview section,Account Assignment: UItem Category: EShort Text: Enhanced Limit TestPlant: 3310End Date: +10 days from current dateIn Items Details section, on Enhanced Limits tab:Expected Value: 200Overall Limit: 300In Items Details section, onConfirmations tab:Conf. Control: Confirmations.Note The Origin Accept checkbox is disabled for enhanced limit item in the purchase order. After processing this step, skip step [Two Step Goods Receipt Process](#unique_57) [page ] 51. The enhanced limit item doesn't support the two step goods receipt process. This behavior is expected in the system. | The Create Purchase Order screen is displayed. |  |
| 4 | Save Purchase Order | Choose Save and click on save in the pop-up screen. | A new Purchase Order is created.Purchase Order Number is displayed. |  |

### Two Step Goods Receipt Process

Purpose

This process enables the acceptance and ownership of goods to be transferred financially, even before the physical arrival of the goods.

|  |
| --- |
| Note If you have executed the previous step [Create Purchase Order (Enhanced Limit)](#unique_56) [page ] 50, the system will not support to execute the current step Two Step Goods Receipt Process. |

|  |
| --- |
| Note When creating purchase orders, select the Origin Accept checkbox under tab Delivery for the purchase order item.You can only proceed with the two post goods receipt steps below after selecting the Origin Accept box. |

#### Create Inbound Delivery

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you create an inbound delivery for purchase order for two step goods receipt which has the Orgin Accept. indicator checked.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log onto SAP Fiori Launchpad | Log onto the SAP Fiori Launchpad using the Role Receiving Specialist. | The Fiori Launchpad is displayed. |  |
| 2 | Access the App | Open Inbound Deliveries for Purchase Orders (VL34). | The Generation of Inbound Deliveries screen displays. |  |
| 3 | Create Inbound Delivery | Make the following entries then choose Execute:Document Number: XXX (Enter the purchase order number created in previous step)Delivery Date: XXX Delete the default date and enter the delivery date in purchase orderTest Run: unchecked | The Inbound Delivery Number is displayed.Note down the Inbound Delivery number for further use. ________ |  |

#### Post Goods Receipt Financially

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In the first step, the goods are accepted before physically arriving. The purchasing entity posts the goods receipt under 'Stock in Transit', and the financial accounting is recorded.

At this point, the financial ownership of the goods is transferred to the purchasing entity.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Warehouse Clerk.Note User Warehouse Clerk used here is due to simplified user setup in demo company. In real business, this step shall not be executed by a warehouse clerk as there’s no physical goods arrived at the warehouse at this moment. You shall setup a dedicated role to access the app Post Goods Movement (MIGO) restricted with movement type 107. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Post Goods Movement (MIGO). It only displays this way if it was your last transaction. | The Goods Receipt screen displays. |  |
| 3 | Enter Purchase Order | Make the following entry and choose Execute.Executable Action in Transaction MIGO: Goods ReceiptReference Document for MIGO Transaction: Inbound Delivery or Purchase OrderDocument Number : <Inbound Delivery Number> or < Purchase Order Number>Note You can choose post against inbound delivery or purchase order to post goods receipt in this step. | The Goods Receipt Inbound Delivery displays. |  |
| 4 | Edit Movement Type | Make the following entry, and choose Enter:GR to Val. Bl. Stock : 107 |  |  |
| 5 | Save your entry | Check Item Ok check box and choose Post. | The posted material document displays.Note down the material document number. ________Check the financial posting. |  |

#### Confirm Quantities for Putaway (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, the goods physically arrive.

This activity confirms that all the materials have been put away in the correct quantities.

Put away needs to be done for inbound delivery according to the system configuration.

Procedure

For putaway procedure of two step goods receipt please refer to the section Confirm Quantities for Putaway of Direct Procurement with Inbound Delivery-(2TX).

#### Post Goods Receipt Physically

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, the goods physically arrive, and the final goods receipt is posted.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Receiving Specialist. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Inbound Deliveries (VL06I). | The Manage Inbound Deliveries - VL06I screen displays. |  |
| 3 | Open the Goods Receipt | Choose For Goods Receipt. Make the following entry and choose Execute. | The Goods Receipt for Inbound Deliveries to be Posted screen displays |  |
| 4 | Search Inbound Deliveries | Purchasing Document: <Purchase Order Number>Clear Delivery DateInbound Delivery: <Inbound Delivery Number> | The list of relevant inbound deliveries displays. |  |
| 5 | Change Inbound Deliveries | Select the relevant delivery and choose Change Inbound Deliveries. | The Change Inbound Delivery screen displays. |  |
| 6 | Post Goods Receipt | On Goods Movement Data tab,Check the following entry:Movement Type: 109Choose Post Goods Receipt. | The posted material document displays.Note down the material document number. ________In this step, there is no financial posting. |  |

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
> Flagged while digesting this document, not verified: The supplier-confirmation approval workflow and its approval test step use supplier 10300003 and purchasing group 003, but the sample master data and every test step use suppliers 33300001/33300003 and purchasing group 002, so the approval workflow would not trigger on the script's own data.

## Connections
- part-of :: [[_cluster]]
- related-to :: [[10-procurement/test-script-cross-company-purchasing-organization-2r3-ae-854]]
- related-to :: [[10-procurement/test-script-procurement-of-production-components-consumer-products-5w3]]
- related-to :: [[10-procurement/test-script-sap-s-4hana-cloud-public-edition-procurement-of-direct-mat]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/2TX_S4CLD2608_BPD_EN_AE.docx` — full document · extracted with `mammoth` · 85,643 chars in the whole document
