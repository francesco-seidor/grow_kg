---
id: 10-procurement/complementary-procurement-functions-2tw-ae-test-script-sap-s-4hana-clo
title: "Complementary Procurement Functions (2TW_AE) - Test Script, SAP S/4HANA Cloud Public Edition (2TW_S4CLD2608_BPD_EN_AE)"
description: "SAP test script for scope item 2TW_AE: procuring operating supplies, batch- and serial-number-managed materials (PO, goods receipt, supplier invoice), UAE plant 3310."
cluster: 10-procurement
tags: [kb/procurement, topic/complementary-procurement]
aliases: [2TW_S4CLD2608_BPD_EN_AE]
keywords: ["Complementary Procurement for Operating Supplies, Batches…", complementary procurement, operating supply procurement, batch managed materials, serial number management, purchase orders, goods receipt, supplier invoices, purchasing info records, business roles]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/2TW_S4CLD2608_BPD_EN_AE.docx]
confidence: low
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-864
topic: 10-procurement/complementary-procurement
language: EN
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Complementary Procurement Functions (2TW_AE) - Test Script, SAP S/4HANA Cloud Public Edition (2TW_S4CLD2608_BPD_EN_AE)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/2TW_S4CLD2608_BPD_EN_AE.docx`, extracted with `mammoth`. Grouped under **Complementary Procurement for Operating Supplies, Batches and Serial Numbers** in Procurement. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

|  |  |
| --- | --- |
| Complementary Procurement Functions (2TW_AE)Purpose PUBLIC 1<!-- image omitted: unnamed --> | Test ScriptSAP S/4HANA Cloud Public Edition - 19-06-26 |
|  | Complementary Procurement Functions (2TW_AE) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Table of Contents

[1 Purpose 3](#_Toc232850377)

[2 Prerequisites 4](#_Toc232850378)

[2.1 System Access 4](#_Toc232850379)

[2.2 Roles 4](#_Toc232850380)

[2.3 Master Data, Organizational Data, and Other Data 5](#_Toc232850381)

[2.4 Business Conditions 6](#_Toc232850382)

[2.5 Preliminary Steps 6](#_Toc232850383)

[2.5.1 Open New MM Period 6](#_Toc232850384)

[2.5.2 Create Purchasing Info Record (Optional) 7](#_Toc232850385)

[2.5.3 Create Purchasing Info Record (Optional) 9](#_Toc232850386)

[2.5.4 Create Purchasing Info Record (Optional) 11](#_Toc232850387)

[2.5.5 Edit User-Specific Parameters for Supplier Invoices (Optional) 14](#_Toc232850388)

[3 Overview Table 15](#_Toc232850389)

[4 Test Procedures 16](#_Toc232850390)

[4.1 Procurement of Operating Supply Material 16](#_Toc232850391)

[4.1.1 Create Purchase Order 16](#_Toc232850392)

[4.1.2 Post Goods Receipt 18](#_Toc232850393)

[4.1.3 Create Supplier Invoice 19](#_Toc232850394)

[4.2 Procurement of Batch Management Material 20](#_Toc232850395)

[4.2.1 Create Purchase Order 20](#_Toc232850396)

[4.2.2 Post Goods Receipt 22](#_Toc232850397)

[4.2.3 Create Supplier Invoice 23](#_Toc232850398)

[4.3 Procurement of Serial Number Management Material 25](#_Toc232850399)

[4.3.1 Create Purchase Order 25](#_Toc232850400)

[4.3.2 Post Goods Receipt 27](#_Toc232850401)

[4.3.3 Create Supplier Invoice 28](#_Toc232850402)

[5 Appendix 31](#_Toc232850403)

[5.1 Procurement of Manufacture Part Material 31](#_Toc232850404)

[5.1.1 Create Material (Product) Master Data - Purchasing Data 31](#_Toc232850405)

[5.1.1.1 Roles 31](#_Toc232850406)

[5.1.1.2 Required Organizational Units 31](#_Toc232850407)

[5.1.1.3 Mandatory and Operational Master Data 32](#_Toc232850408)

[5.1.1.4 Main Parameters for Data Creation 33](#_Toc232850409)

[5.1.1.4.1 Material Type and Number Ranges 33](#_Toc232850410)

[5.1.1.4.2 Industry Sector 33](#_Toc232850411)

[5.1.1.5 Test Procedures 33](#_Toc232850412)

[5.1.2 Create Purchase Order 36](#_Toc232850413)

## Purpose

Overview

The scope item covers the usage of complementary functions in sourcing and procurement. By enabling a lightweight process, the scope item enables the user to procure operating supplies as well as batch and serial-number-managed materials. Both processes can be summarized by the three following steps: purchase order creation, posting of a goods receipt, and invoice creation. The scope item focuses on the main process steps but can be enhanced by additional optional steps.

Operating supplies are externally procured materials that are used to manufacture products and comprise auxiliary materials and expendable supplies.

The procurement of batch managed materials enables the user to work with homogeneous partial quantities of a material. This can be leveraged for example to meet legal requirements, to track defects, or to ensure procedural requirements throughout the production process.

In alignment with the batch process, you can also procure serial-number-managed materials.

This document provides a detailed procedure for testing this scope item after solution activation, reflecting the predefined scope of the solution. Each process step, report, or item is covered in its own section, providing the system interactions (test steps) in a table view. Steps that are not in scope of the process but are needed for testing are marked accordingly. Project-specific steps must be added.

|  |
| --- |
| Note Values in this test script (decimal notation, date formats, and so on) are presented in U.S. standard notation. If your test system is set up to use a different notation, enter values as appropriate. |

## Prerequisites

This section summarizes all the prerequisites for conducting the test in terms of systems, users, master data, organizational data, other test data and business conditions.

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
| Purchaser | SAP_BR_PURCHASER | Purchasing / Sourcing and Contracting | SAP_MM_SPT_PURCHASING_PC / SAP_MM_SPT_SOURCING_PC |  |
| Warehouse Clerk | SAP_BR_WAREHOUSE_CLERK | Inventory Processing | SAP_BR_WAREHOUSE_CLERK |  |
| Accounts Payable Accountant | SAP_BR_AP_ACCOUNTANT |  |  |  |
| Business Process Specialist | SAP_BR_BUSINESS_PROCESS_SPEC | Business Process Management / Business Process Management | SAP_BR_BUSINESS_PROCESS_SPEC / SAP_CA_SPT_BPS_PC |  |

### Master Data, Organizational Data, and Other Data

The organizational structure and master data of your company have been created in your system during implementation. The organizational structure reflects the structure of your company. The master data represents materials, customers, and suppliers, for example, depending on the operational focus of your company.

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
| Supplier | 33300002 | Domestic UAE Supplier 2 |  |
| Material | TG21 | Trad.Good 21,Reorder Point,Batch-FIFO |  |
| Material | HB01 | Operating Supply 01, Purchasing |  |
| Material | TG0014 | Trading Good 0014,PD,Regular Proc. with Serial no.; no batch |  |

For more information on creating these master data objects, see the following [Master Data Scripts (MDS)](https://help.sap.com/docs/s4hana-best-practices/s4cld2608-master-data)

Table 1: Master Data Script Reference

| Master Data Script ID | Description |
| --- | --- |
| BNF | Create Product Master of type "Trading Good" - MDS |
| BNE | Create Supplier Master - MDS |
| 2SW | Create Tax Condition - MDS |

### Business Conditions

| Scope Item | Business Condition |
| --- | --- |
| BNZ - Create New Open MM Posting Period - MDS | You have completed the step described in the Create New Open MM Posting Period - MDS master data script. Posting Period is up to date. |
|  | When testing time-dependent tax, you need a company code of a country for which the time dependent tax is activated from finance application area. |
|  | Time dependent tax is available for countries that have no tax jurisdiction, for this release Germany is enabled. And the time-dependent tax settings via SSCUI Define Tax Codes for Sales and Purchases in application area Finance must have been completed. |

### Preliminary Steps

#### Open New MM Period

External Process

For this activity, run the following steps from the Create New Open MM Posting Period - MDS (BNZ) to close MM period and open new posting period.

• Closing MM Period and Opening New Posting Period

#### Create Purchasing Info Record (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

To run through this test script, the info records for the necessary materials must be available as master data. If the Info Record has not been maintained in the system yet, create the required master data. Otherwise you can skip this step.

The purpose of this activity is to create the info records for materials, for example, HB01 and choose a valid supplier (for example, 33300001).

This step is obsolete if the necessary info records are present. Check the info records supplier 33300001, material HB01 and Purchasing Organization 3310. The existing info records for this material are displayed on the screen.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log onto the SAP Fiori launchpad as a Purchaser . | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the App | Open Manage Purchasing Info Records (F1982) . | The Manage Purchasing Info Records screen is displayed. |  |
| 3 | Open New Purchasing Info Record | Choose Create. | The Purchasing Info Record Screen is displayed. |  |
| 4 | Enter Header Data | Make the following entries:Purchasing Info Record Category: StandardPurchasing Organization: 3310Supplier: 33300001Material: HB01Plant: 3310Purchasing Group: 002 | Header data is added. |  |
| 5 | Enter General Information | Make the following entries:Available From: TodayAvailable To: 12/31/9999 | General Information is added. |  |
| 6 | Enter Purchasing Data | Make the following entries:Incoterm: EXWIncoterm Location 1: VENDORNote Incoterms and their corresponding versions are grouped in the F4 value help. Selecting an Incoterm automatically populates its associated version, which can be subsequently modified or removed if needed. | Purchasing Data is added. |  |
| 7 | Enter Delivery and Quantity Data | Make the following entries:Delivery Time in Days: 1Under Delivery Tolerance in %: 10.0Over Delivery Tolerance in %: 10.0Tax Code: <Input Tax Code>Note If time dependent tax (TDT) is activated, and fields Country/Region Key for company code, Validity Periods and Tax Code are maintained via SSCUI 101016 in SAP S/4HANA Cloud Public Edition or the configuration activity Define Tax Codes for Sales and Purchases in Central Business Configuration, you must maintain the Tax Rate Valid From field in the New Purchasing Info Record screen. If you enter the current date, this date will be adjusted to a valid start date for your tax code according to the SSCUI/configuration activity settings.If Registration for Indirect Taxation Abroad (RITA) is activated, and tax registration country and tax code are maintained for company code via SSCUI 103464 in SAP S/4HANA Cloud Public Edition or the configuration activity Activate RITA and Maintain Tax Registration Countries in Central Business Configuration, you must maintain the Tax Country field. The default value of this field is the country ID of company code, but you can change it to a valid country ID that is maintained in the SSCUI/configuration activity accordingly.Order Unit: PCStandard Order Quantity: 10 | Delivery and Quantity Data is added. |  |
| 8 | Enter Condition Data | In the Condition section, choose Create.In the General Information area, make the following entries:Valid From: TodayValid To: 12/31/9999Amount: 10Pricing Unit: 1Currency: AEDChoose Apply. | Condition Data is added |  |
| 9 | Enter Reference Data (optional) | You can enter reference data. | Reference data is added. |  |
| 10 | Save your data | Choose Create. | The purchasing info record is saved. |  |

#### Create Purchasing Info Record (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

To run through this test script, the info records for the necessary materials must be available as master data. If the Info Record has not been maintained in the system yet, create the required master data. Otherwise you can skip this step.

The purpose of this activity is to create the info records for materials, for example, TG21 and choose a valid supplier (for example, 33300001).

This step is obsolete if the necessary info records are present. Check the info records supplier 33300001, material TG21 and Purchasing Organization 3310. The existing info records for this material are displayed on the screen.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log onto the SAP Fiori launchpad as a Purchaser . | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the App | Open Manage Purchasing Info Records (F1982) . | The Manage Purchasing Info Records screen is displayed. |  |
| 3 | Open New Purchasing Info Record | Choose Create. | The Purchasing Info Record Screen is displayed. |  |
| 4 | Enter Header Data | Make the following entries:Purchasing Info Record Category: StandardPurchasing Organization: 3310Supplier: 33300001Material: TG21Plant: 3310Purchasing Group: 002 | Header data is added. |  |
| 5 | Enter General Information | Make the following entries:Available From: TodayAvailable To: 12/31/9999 | General Information is added. |  |
| 6 | Enter Purchasing Data | Make the following entries:Incoterm: EXWIncoterm Location 1: VENDORNote Incoterms and their corresponding versions are grouped in the F4 value help. Selecting an Incoterm automatically populates its associated version, which can be subsequently modified or removed if needed. | Purchasing Data is added. |  |
| 7 | Enter Delivery and Quantity Data | Make the following entries:Delivery Time in Days: 10Under Delivery Tolerance in %: 10.0Over Delivery Tolerance in %: 10.0Tax Code: <Input Tax Code>Note If time dependent tax (TDT) is activated, and fields Country/Region Key for company code, Validity Periods and Tax Code are maintained via SSCUI 101016 in SAP S/4HANA Cloud Public Edition or the configuration activity Define Tax Codes for Sales and Purchases in Central Business Configuration, you must maintain the Tax Rate Valid From field in the New Purchasing Info Record screen. If you enter the current date, this date will be adjusted to a valid start date for your tax code according to the SSCUI/configuration activity settings.If Registration for Indirect Taxation Abroad (RITA) is activated, and tax registration country and tax code are maintained for company code via SSCUI 103464 in SAP S/4HANA Cloud Public Edition or the configuration activity Activate RITA and Maintain Tax Registration Countries in Central Business Configuration, you must maintain the Tax Country field. The default value of this field is the country ID of company code, but you can change it to a valid country ID that is maintained in the SSCUI/configuration activity accordingly.Order Unit: PCStandard Order Quantity: 100 | Delivery and Quantity Data is added. |  |
| 8 | Enter Condition Data | In the Condition section, choose Create.In the General Information area, make the following entries:Valid From: TodayValid To: 12/31/9999Amount: 10Pricing Unit: 1Currency: AEDChoose Apply. | Condition Data is added |  |
| 9 | Enter Reference Data (optional) | You can enter reference data. | Reference data is added. |  |
| 10 | Save your data | Choose Create. | The purchasing info record is saved. |  |

|  |
| --- |
| Note Repeat the above steps to create the Infor Record for Material TG21 and Supplier 33300002, the field entries for this Infor Record are the same with TG21 and supplier 33300001. |

#### Create Purchasing Info Record (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

To run through this test script, the info records for the necessary materials must be available as master data. If the Info Record has not been maintained in the system yet, create the required master data. Otherwise you can skip this step.

The purpose of this activity is to create the info records for materials, for example, TG0014 and choose a valid supplier (for example, 33300001).

This step is obsolete if the necessary info records are present. Check the info records supplier 33300001, material TG0014 and Purchasing Organization 3310. The existing info records for this material are displayed on the screen.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log onto the SAP Fiori launchpad as a Purchaser . | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the App | Open Manage Purchasing Info Records (F1982) . | The Manage Purchasing Info Records screen is displayed. |  |
| 3 | Open New Purchasing Info Record | Choose Create. | The Purchasing Info Record Screen is displayed. |  |
| 4 | Enter Header Data | Make the following entries:Purchasing Info Record Category: StandardPurchasing Organization: 3310Supplier: 33300001Material: TG0014Plant: 3310Purchasing Group: 002 | Header data is added. |  |
| 5 | Enter General Information | Make the following entries:Available From: TodayAvailable To: 12/31/9999 | General Information is added. |  |
| 6 | Enter Purchasing Data | Make the following entries:Incoterm: EXWIncoterm Location 1: VENDORNote Incoterms and their corresponding versions are grouped in the F4 value help. Selecting an Incoterm automatically populates its associated version, which can be subsequently modified or removed if needed. | Purchasing Data is added. |  |
| 7 | Enter Delivery and Quantity Data | Make the following entries:Delivery Time in Days: 10Under Delivery Tolerance in %: 10.0Over Delivery Tolerance in %: 10.0Tax Code: <Input Tax Code>Note If time dependent tax (TDT) is activated, and fields Country/Region Key for company code, Validity Periods and Tax Code are maintained via SSCUI 101016 in SAP S/4HANA Cloud Public Edition or the configuration activity Define Tax Codes for Sales and Purchases in Central Business Configuration, you must maintain the Tax Rate Valid From field in the New Purchasing Info Record screen. If you enter the current date, this date will be adjusted to a valid start date for your tax code according to the SSCUI/configuration activity settings.If Registration for Indirect Taxation Abroad (RITA) is activated, and tax registration country and tax code are maintained for company code via SSCUI 103464 in SAP S/4HANA Cloud Public Edition or the configuration activity Activate RITA and Maintain Tax Registration Countries in Central Business Configuration, you must maintain the Tax Country field. The default value of this field is the country ID of company code, but you can change it to a valid country ID that is maintained in the SSCUI/configuration activity accordingly.Order Unit: PCStandard Order Quantity: 10 | Delivery and Quantity Data is added. |  |
| 8 | Enter Condition Data | In the Condition section, choose Create.In the General Information area, make the following entries:Valid From: TodayValid To: 12/31/9999Amount: 10Pricing Unit: 1Currency: AEDChoose Apply. | Condition Data is added |  |
| 9 | Enter Reference Data (optional) | You can enter reference data. | Reference data is added. |  |
| 10 | Save your data | Choose Create. | The purchasing info record is saved. |  |

|  |
| --- |
| Note Repeat the above steps to create the Info Record for Material TG0014 and Supplier 33300002, its net price is 35 AED. |

#### Edit User-Specific Parameters for Supplier Invoices (Optional)

Purpose

In this procedure, you will edit User-Specific parameters for supplier invoices.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Accounts Payable Accountant. | The Fiori launchpad is displayed. |  |
| 2 | Access the App | Open Edit Supplier Invoice Settings (F3813) | The Edit Supplier Invoice Settings screen is displayed. |  |
| 3 | Set parameter | Check parameter Display Journal Entry: XNote If parameter is checked, when invoice is created, system message contains invoice and journal entry number.If parameter is unchecked, when invoice is created, system message contains invoice number only.When this parameter is changed, for APP Create Supplier Invoice, it will take effective immediately. For APP Create Supplier Invoice – Advanced, user needs to logout and login again to make it take effective. | Change has been saved successfully. |  |

Result

Parameter Display Journal Entry has been set successfully.

## Overview Table

This scope item consists of several process steps that are listed in the following table.

|  |
| --- |
| Note If your system administrator has enabled spaces and pages on the SAP Fiori launchpad, the homepage will only contain the essential apps for performing the typical tasks of a business role.You can find all other (searchable) apps not included on the homepage using the search bar ([2434549](https://me.sap.com/notes/2434549)).If you want to personalize the homepage and include the hidden apps, navigate to your user profile and choose App Finder. |

Table 2: Procurement of Stock Material

| Process Step | Business Role | Transaction/App | Expected Results |
| --- | --- | --- | --- |
| [Procurement of Operating Supply Material](#unique_14) [page ] 16 |  |  |  |
| [Create Purchase Order](#unique_15) [page ] 16 | Purchaser | Manage Purchase Orders (F0842A) | The Purchase Order is created. |
| [Post Goods Receipt](#unique_16) [page ] 18 | Warehouse Clerk | Post Goods Receipt for Purchasing Document (F0843) | The Goods Receipt is posted. |
| [Create Supplier Invoice](#unique_17) [page ] 19 | Accounts Payable Accountant | Create Supplier Invoice (F0859) | The Create Supplier Invoices screen is displayed. |
| [Procurement of Batch Management Material](#unique_18) [page ] 20 |  |  |  |
| [Create Purchase Order](#unique_19) [page ] 20 | Purchaser | Manage Purchase Orders (F0842A) | The Purchase Order is created. |
| [Post Goods Receipt](#unique_20) [page ] 22 | Warehouse Clerk | Post Goods Movement (MIGO) | The Goods Receipt is posted. |
| [Create Supplier Invoice](#unique_21) [page ] 23 | Accounts Payable Accountant | Create Supplier Invoice (F0859) | The Create Supplier Invoices screen is displayed. |
| [Procurement of Serial Number Management Material](#unique_22) [page ] 25 |  |  |  |
| [Create Purchase Order](#unique_23) [page ] 25 | Purchaser | Manage Purchase Orders (F0842A) | The Purchase Order is created. |
| [Post Goods Receipt](#unique_24) [page ] 27 | Warehouse Clerk | Post Goods Movement (MIGO) | The Goods Receipt is posted. |
| [Create Supplier Invoice](#unique_25) [page ] 28 | Accounts Payable Accountant | Create Supplier Invoice (F0859) | The Create Supplier Invoices screen is displayed. |

## Test Procedures

### Procurement of Operating Supply Material

#### Create Purchase Order

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this procedure, you create a purchase order for operating supply material.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log onto the SAP Fiori launchpad with the Purchaser role. | The SAP Fiori launchpad is displayed. |  |
| 2 | Open Manage Purchase Order | Open Manage Purchase Orders (F0842A) . | The Manage Purchase Orders screen is displayed. |  |
| 3 | Start Purchase Order creation | Without making any selection, choose Create. | The Purchase Order Screen is shown. |  |
| 4 | Enter Purchase Order data | Enter all of the necessary data.General Information:Purchase Order Type: Standard PO (NB)Supplier: 33300001Company Code: 3310Purchasing Organization:3310Purchasing Group:002Currency: AEDIn Items section, choose Create button.Material: HB01Plant: 3310Order Quantity:xNet Order Price: xNavigate to the selected item by clicking on the Chevron (>) or by directly clicking on the item line.In item section, choose General Information tabStorage Location: 331BIn item section, choose Process Flow tab.The next data will be displayed after the article is enteredGoods Receipt: yesInvoice Receipt: xMake sure Goods-Receipt-Based Invoice Verification has been selected.In Item section, choose Tax tab , check the following entries:Tax Code: <Default Value> ;Tax Date: <Default Value>Note Field Tax Date is only available for the countries/regions that Time-Dependent Taxes (TDT) is enabled.In item section, choose Schedule Lines tabDelivery Date: a date in the futureChoose Apply to go back Purchaser Order screen. | The Purchase Order screen is displayed. |  |
| 5 | Check Purchase Order for completeness and Save Purchase Order | Choose Order to save the Purchase Order. | A new Purchase Order is created if no error is displayed in the dialog box. |  |

#### Post Goods Receipt

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you post the goods receipt for the material HB01 against the purchase order.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log onto Fiori Launchpad | Log onto the SAP Fiori launchpad using the Warehouse Clerk role. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Post Goods Receipt for Purchasing Document (F0843) . | The Goods Receipt screen displays. |  |
| 3 | Enter Purchase Order | Enter the purchase order number and choose Enter. | The system displays the data for the goods receipt on the Goods Receipt screen. |  |
| 4 | Enter Delivery Note | Make the following entries:Delivery Note: <note number>Printing: Choose Individual slip from the drop-down list.And choose Enter. |  |  |
| 5 | Select Item | Select the items for which a goods receipt is to be posted.Enter the delivered quantity and check storage location to be posted. | The Post button is activated. |  |
| 6 | Post | Choose Post. | The system is displayed the message 1 material document(s) posted: 5xxxxxxxxx 2xxx. |  |

#### Create Supplier Invoice

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you perform the invoice verification.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Open the SAP Fiori launchpad with the Accounts Payable Accountant role. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the app | Open Create Supplier Invoice (F0859) . | The New Supplier Invoices screen is displayed. |  |
| 3 | Enter General Data | On the Create Supplier Invoice screen, make the following entries:Transaction: InvoiceCompany Code: 3310Reference: <xxx> (reference invoice number from invoicing party)Gross Invoice Amount : <XXX>Currency: AEDInvoice Date: <Today>Posting Date: <Today>Invoice Party: 33300001 | The New Supplier Invoices screen displays. |  |
| 4 | Enter Purchase Order References | In Purchasing Document References, make the following entries (use a PO you created previously) and choose Enter.Reference Document Category: Purchase Order/ Scheduling AgreementPurchase Order/Scheduling Agreement: <PO number> | The Purchase Document References screen displays. |  |
| 5 | Select Purchase Order Items | Check the selection of the Purchase Order Items.Confirm the warning messages. | All items of the selected Purchase Order are added to the Purchase Order Item table.You should see material items which refer to the entered purchase order document. |  |
| 6 | Check the Invoice Items data | Check the Amount, the Quantity, the Tax Code (there may already be a tax code that was copied from the purchase order). | The Purchase Order Item's table displays. |  |
| 7 | Check Tax code | In the section Tax check if there is tax code information. | In the Tax tab, you should see the same tax codes as in the items.If there is no tax, specify the tax code <Input Tax Code>. |  |
| 8 | Check the balance | Calculate the tax amount from the item amount multiplied by the tax value.. | The balance should be zero (or within the defined tolerance). |  |
| 9 | Simulate Supplier Invoice and Check Messages | Choose Simulate.If there are no differences(or if the value is within the defined tolerance), a new screen Simulation appears. You can check the simulation results in Overview and Details area.The Supplier Invoice is complete to post. Check the Gross Invoice Amount against the items plus tax amount (if tax code is,<Input Tax Code> you do not have any tax amount) | The supplier invoice is complete to post. |  |
| 10 | Post Invoice | Choose Post. | The invoice is posted. |  |

### Procurement of Batch Management Material

#### Create Purchase Order

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this procedure, you create a purchase order for batch management material directly.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log onto the SAP Fiori launchpad with the Purchaser role. | The SAP Fiori launchpad is displayed. |  |
| 2 | Open Manage Purchase Order | Open Manage Purchase Orders (F0842A) . | The Manage Purchase Orders screen is displayed. |  |
| 3 | Start Purchase Order creation | Without making any selection, choose Create. | The Purchase Order Screen is shown. |  |
| 4 | Enter Purchase Order data | Enter all of the necessary data.General Information:Purchase Order Type: Standard PO (NB)Supplier: 33300001Company Code: 3310Purchasing Organization:3310Purchasing Group:002Currency: AEDIn Items section, choose Create button.Material: TG21Plant: 3310Order Quantity:xNet Order Price: xNavigate to the selected item by clicking on the Chevron (>) or by directly clicking on the item line.In item section, choose General Information tabStorage Location: 331AIn item section, choose Process Flow tab.The next data will be displayed after the article is enteredGoods Receipt: yesInvoice Receipt: xMake sure Goods-Receipt-Based Invoice Verification has been selected.In Item section, choose Tax tab , check the following entries:Tax Code: <Default Value> ;Tax Date: <Default Value>Note Field Tax Date is only available for the countries/regions that Time-Dependent Taxes (TDT) is enabled.In item section, choose Schedule Lines tabDelivery Date: a date in the futureChoose Apply to go back Purchaser Order screen. | The Purchase Order screen is displayed. |  |
| 5 | Check Purchase Order for completeness and Save Purchase Order | Choose Order to save the Purchase Order. | A new Purchase Order is created if no error is displayed in the dialog box. |  |

#### Post Goods Receipt

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you post the goods receipt for the material TG21 against the purchase order.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Open the SAP Fiori launchpad with the Warehouse Clerk role. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the App | Open Post Goods Movement (MIGO) . | The Goods Receipt Purchase Order screen is displayed. |  |
| 3 | Select Goods Receipt Order screen | On the Goods Receipt Purchase Order screen, make the following entries and choose Enter.Goods Receipt : <Select>Purchasing Order : <Select>Order number: <Purchase Order number which is created in the previous step>GR goods receipt: 101 | The items of the selected Purchase Order display. |  |
| 4 | Enter Quantity | If required, check the quantity on the Quantity tab. |  |  |
| 5 | Enter storage location | Select the Where tab and check the storage location 331A. |  |  |
| 6 | Input the Batch Number | On the Batch tab, make the following entries and choose Enter.Batch: enter external batch number or leave empty for internal number assignment.Date of Manufacture: Maintain the date when necessary. |  |  |
| 7 | Select Item ok Indicator | Select the Item OK checkbox.Choose Check. Confirm the message Document is O.K.by choosing Enter. |  |  |
| 8 | Post | Choose Post. | The system displays the message: Material document 5xxxxxxxxx posted. |  |

#### Create Supplier Invoice

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you perform the invoice verification.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Open the SAP Fiori launchpad with the Accounts Payable Accountant role. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the app | Open Create Supplier Invoice (F0859) . | The New Supplier Invoices screen is displayed. |  |
| 3 | Enter General Data | On the Create Supplier Invoice screen, make the following entries:Transaction: InvoiceCompany Code: 3310Reference: <xxx> (reference invoice number from invoicing party)Gross Invoice Amount : <XXX>Currency: AEDInvoice Date: <Today>Posting Date: <Today>Invoice Party: 33300001 | The New Supplier Invoices screen displays. |  |
| 4 | Enter Purchase Order References | In Purchasing Document References, make the following entries (use a PO you created previously) and choose Enter.Reference Document Category: Purchase Order/ Scheduling AgreementPurchase Order/Scheduling Agreement: <PO number> | The Purchase Document References screen displays. |  |
| 5 | Select Purchase Order Items | Check the selection of the Purchase Order Items.Confirm the warning messages. | All items of the selected Purchase Order are added to the Purchase Order Item table.You should see material items which refer to the entered purchase order document. |  |
| 6 | Check the Invoice Items data | Check the Amount, the Quantity, the Tax Code (there may already be a tax code that was copied from the purchase order). | The Purchase Order Item's table displays. |  |
| 7 | Check Tax code | In the section Tax check if there is tax code information and enter the tax amount.when the tax code value is greater than zero. | In the Tax tab, you should see the same tax codes as in the items.If there is no tax, specify the tax code <Input Tax Code>. |  |
| 8 | Check the balance | Calculate the tax amount from the item amount multiplied by the tax value.. | The balance should be zero (or within the defined tolerance). |  |
| 9 | Simulate Supplier Invoice and Check Messages | Choose Simulate.If there are no differences(or if the value is within the defined tolerance), a new screen Simulation appears. You can check the simulation results in Overview and Details area.The Supplier Invoice is complete to post. Check the Gross Invoice Amount against the items plus tax amount (if tax code is,<Input Tax Code> you do not have any tax amount) | The supplier invoice is complete to post. |  |
| 10 | Post Invoice | Choose Post. | The invoice is posted. |  |

### Procurement of Serial Number Management Material

#### Create Purchase Order

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this procedure, you create a purchase order for serial number management material directly.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log onto the SAP Fiori launchpad with the Purchaser role. | The SAP Fiori launchpad is displayed. |  |
| 2 | Open Manage Purchase Order | Open Manage Purchase Orders (F0842A) . | The Manage Purchase Orders screen is displayed. |  |
| 3 | Start Purchase Order creation | Without making any selection, choose Create. | The Purchase Order Screen is shown. |  |
| 4 | Enter Purchase Order data | Enter all of the necessary data.General Information:Purchase Order Type: Standard PO (NB)Supplier: 33300001Company Code: 3310Purchasing Organization:3310Purchasing Group:002Currency: AEDIn Items section, choose Create button.Material: TG0014Plant: 3310Order Quantity:xNet Order Price: xNavigate to the selected item by clicking on the Chevron (>) or by directly clicking on the item line.In item section, choose General Information tab.Storage Location: 331AIn item section, choose Process Flow tab.The next data will be displayed after the article is enteredGoods Receipt: yesInvoice Receipt: xMake sure Goods-Receipt-Based Invoice Verification has been selected.In Item section, choose Tax tab , check the following entries:Tax Code: <Default Value> ;Tax Date: <Default Value>Note Field Tax Date is only available for the countries/regions that Time-Dependent Taxes (TDT) is enabled.In item section, choose Schedule Lines tabDelivery date: a date in the futureChoose Apply to go back Purchaser Order screen. | The Purchase Order screen is displayed. |  |
| 5 | Check Purchase Order for completeness and Save Purchase Order | Choose Order to save the Purchase Order. | A new Purchase Order is created if no error is displayed in the dialog box. |  |

#### Post Goods Receipt

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you post the goods receipt for the purchase order. In this step, you have to use purchase order which is created for the material TG0014 with serial number management.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Open the SAP Fiori launchpad with the Warehouse Clerk role. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the App | Open Post Goods Movement (MIGO) . | The Post Goods Receipt for Purchase Order screen is displayed. |  |
| 3 | Select Goods Receipt Order screen | On the Goods Receipt Order screen, make the following entries and choose Enter.Goods Receipt : <Select>Purchasing Order : <Select>Order number: <Purchase Order number which is created in the previous step>GR goods receipt: 101 | The items of the selected Purchase Order display. |  |
| 4 | Enter Quantity If required | Enter Quantity if required, check the quantity on the Quantity tab. |  |  |
| 5 | Enter Storage Location | Select the Where tab and check the storage location 331A. |  |  |
| 6 | Create the Serial Number | On the Serial Numbers tab, make the following entries and choose Enter.Auto-Create Serial Numbers: x |  |  |
| 7 | Select Item ok Indicator | Select the Item OK checkbox. |  |  |
| 8 | Post | Choose Post. | The system displays the message: Material document 5xxxxxxxxxx posted. |  |

#### Create Supplier Invoice

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you perform the invoice verification.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Open the SAP Fiori launchpad with the Accounts Payable Accountant role. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the App | Open Create Supplier Invoice (F0859). | The New Supplier Invoices screen is displayed. |  |
| 3 | Enter General Data | In case of purchase orders created with local currency in your system, make the following entries.Transaction: InvoiceCompany Code: 3310Reference: <xxx> (reference invoice number from invoicing party)Gross Invoice Amount : <XXX>Currency: AEDInvoice Date: <Today>Posting Date: <Today>Invoice Party: 33300007 | The New Supplier Invoices screen displays. |  |
| 4 | Enter Purchase Order References | In Purchasing Document References, make the following entries (use a PO you created previously) and choose Enter.Make the following entries (use a PO you created previously).Reference Document Category: Purchase Order/ Scheduling AgreementPurchase Order/Scheduling Agreement: <PO number> | The Purchase Document References screen displays. |  |
| 5 | Select Purchase Order Items | Check the selection of the Purchase Order Items.Confirm the warning messages. | All items of the selected Purchase Order are added to the Purchase Order Item table.You should see material items which refer to the entered purchase order document. |  |
| 6 | Check the Invoice Items data | Check the Amount, the Quantity, the Tax Code (there may already be a tax code that was copied from the purchase order). | The Purchase Order Item's table displays. |  |
| 7 | Check Tax code | In the section Tax check if there is tax code information. | In the Tax tab, you should see the same tax codes as in the items.If there is no tax, specify the tax code <Input Tax Code>. |  |
| 8 | Check the balance | Calculate the tax amount from the item amount multiplied by the tax value. | The balance should be zero (or within the defined tolerance). |  |
| 9 | Simulate Supplier Invoice and Check Messages | Choose Simulate.If there are no differences(or if the value is within the defined tolerance), a new screen Simulation appears. You can check the simulation results in Simulation Overview and Simulation Details area.The Supplier Invoice is complete to post. Check the Gross Invoice Amount against the items plus tax amount (if tax code is,<Input Tax Code> you do not have any tax amount) | The supplier invoice is complete to post. |  |
| 10 | Post Invoice | Choose Post. | The invoice is posted. |  |

## Appendix

### Procurement of Manufacture Part Material

This section describes test procedures for each process step that belongs to Manufacture Part Material procurement.

#### Create Material (Product) Master Data - Purchasing Data

##### Roles

Create business roles using the following business role templates delivered by SAP and assign them to your individual test users.

Alternatively, if available, you can use the following spaces delivered by SAP. You create a space with pages containing predefined essential apps and assign it to the business role. You then assign this business role to your individual users.

For more information, refer to How to Create a Business Role from a Template in the [product assistance](https://help.sap.com/docs/SAP_S4HANA_CLOUD/53e36b5493804bcdb3f6f14de8b487dd/ec310a8b669a45ca898dc4dd91d97de2.html) for SAP S/4HANA Cloud Public Edition.

| Name (Role Template) | ID (Role Template) | Name (Launchpad Space) | ID (Launchpad Space) | Log On |
| --- | --- | --- | --- | --- |
| Master Data Specialist - Product Data | SAP_BR_PRODMASTER_SPECIALIST | Master Data - Products / Product Governance | SAP_BR_PRODMASTER_SPECIALIST / SAP_CMD_SPT_PR_GOV_PC |  |

##### Required Organizational Units

Some segments of material master data are dependent on the organizational units of the company, General (Central) Data does not depend on an organizational unit or the company code. The following table gives an overview of these different data segments and their relevant organizational units:

| Data Segment | Depends On | Field Examples | Comments | Organizational Unit to be Used |
| --- | --- | --- | --- | --- |
| Basic Data | Independent from organizational units | Material description (short text), Material number, Material Group, Base Unit of Measure, and so on. | Basic Data exists only once for a material master data record. | n/a |
| Sales Data | Plant, Sales Org., Distribution Channel | Tax Data, Item Category Group, Transp. Group, Loading Group, Setup Time, and so on. | Sales data can exist for every Sales Org. of your enterprise structure for which the material master record is used. | Plant:____________Sales Organization:__________Distribution Channel:__________ |
| Purchasing Data | Plant | Purchasing Group, Material Group, GR processing time, and so on. | Purchasing Data can exist for every purchasing organization for which the material shall be used in purchasing processes. | Plant:__________ |
| MRP/Planning Data | Plant, Storage Location | MRP Type, MRP Controller, Lot Size, Planned delivery time, and so on. | Plant data can exist for every Plant ID of your enterprise structure for which the material master record is used.Storage location data (planning context) is optional based on the need to do storage location specific planning | Plant:____________Storage Location:__________ |
| Storage Location Data | Plant, Storage Location | Number of GR slips, Max. Storage Period, Min. Rem. Shelf, and so on. | Plant data can exist for every Plant ID of your enterprise structure for which the material master record is used.Storage location data (planning context) is optional based on the need to do storage location specific planning. | Plant:____________Storage Location:__________ |
| Accounting Data | Valuation area (=Plant), Valuation type | Valuation Class, Per Unit Price, Price Control, and so on. | Valuation area data can exist for every Plant ID of your enterprise structure for which the material master record is used. Every plant represents a valuation area (e.g. different valuation price of a material in different plants) | Plant:____________Valuation type:__________ |

##### Mandatory and Operational Master Data

Material master data records may refer to other master data. The following table gives an overview of optional and mandatory master data objects to be used in a material master data record.

| Master Data Object | Used in Data Segment | Mandatory / Optional | Comments |
| --- | --- | --- | --- |
| Profit Center |  | Mandatory | Assigning a Profit Center to a material (product) master is required for correct valuation processes. |

##### Main Parameters for Data Creation

In this section, we describe some basic parameters that influence the behavior of a master record and are always required to create a material master data record:

###### Material Type and Number Ranges

With the help of material types, the system determines which data segments (views) can be maintained or which fields are mandatory or optional. Based on material types, the system also determines the number ranges for materials. In the SAP standard content, all material types use the same number range definition.

| Number Range | Range / Business Partner ID | Comments |
| --- | --- | --- |
| External alpha-numeric | A – ZZZZZZZZ | This range must start with a character. Overall the ID must not be longer than 40 characters. |
| Internal numeric | 1 – 99999999 | This range is used if the system shall automatically assign a numeric number to a material. |

###### Industry Sector

The standard content only provides one industry sector M. Currently, this is visible in the SAP GUI only.

##### Test Procedures

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The following procedure provides instructions for creating material (product) master data. Apps available to you are dependent upon your assigned role, so two options are provided.

Prerequisite

For a manufacturer part to refer to one of your company's own materials, a manufacturer part profile must be specified.

Please firstly specify one of your company’s own materials and assign a manufacturer part profile to your company's material.

In the standard SAP system, the Manufacturer part profile field appears on the Purchasing screen in the material master.

For example, you can use Operating supplies material HB01 as your company’s own material and assign manufacturer part profile (for example: IMPN) to it. After this testing is done, please remove the manufacturer part profile from your company’s own material HB01 accordingly; otherwise it will affect other testings unexpectedly.

Procedure: Option 1 - Create Material

Use the following procedure when your user access presents you with the Create Material(MM01) app.

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Master Data Specialist - Product Data. | The SAP Fiori launchpad appears. |  |
| 2 | Access the SAP Fiori App | Open Create Material (MM01). | Create Material (Initial Screen) appears. |  |
| 3 | Enter Material Basic Data | In the Create Material (Initial screen) make the following entries:Material: <Material number> for example, HERS-RIndustry sector: M Mechanical engineeringNote If the Industry Sector input field is hidden, no entry is required. When the industry sector is not offered for entry, the field is populated with in the dark.Material type: HERS Manufacturer PartClick on Select View(s). | Select View(s) screen opens. |  |
| 4 | Choose Views | In the Select View(s) window deselect Classification and select Purchasing and choose Continue. | Create Material…(Manufacturer Part) opens. |  |
| 5 | Enter Basic Data | In the Material…(Manufacturer Part) screen, on the Purchasing tab, enter a Material description (short text). |  |  |
| 6 | Enter Purchasing Data | In the Material…(Manufacturer Part) screen, on the Purchasing tab, in the General Data section, make the following entries:Material Group: for example, L002 |  |  |
| 7 | Enter Purchasing Data | In the Other data/manufacturer data section, make the following entry:Int. material number: your firm’s own material, for example, HB01Note Assign a manufacturer part profile (for example: IMPN) to your company's material first.In the standard SAP system, the Manufacturer part profile field appears on the Purchasing screen in the material master.Mfr Part Number: for example, HERS-R-EXManufacturer: for example, 33300001 |  |  |
| 8 | Save Your Data | At the bottom of the screen, choose Save. | Your data is saved. |  |

Procedure: Option 2 - Manage Product Master Data

Use the following procedure when your user access presents you with the Manage Product Master Data (F1602) app.

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Master Data Specialist - Product Data. | The SAP Fiori launchpad appears. |  |
| 2 | Access the SAP Fiori App | Open Manage Product Master Data (F1602). | The Manage Product Master Data(F1602) app is displayed and various search fields are displayed. |  |
| 3 | Choose Create New Product Master | In the Manage Product Master Data(F1602) view, choose Create Product. | The Create Master Data Record screen displays. |  |
| 4 | Enter Data for Mandatory Fields | In the Create Master Data Record screen, make the following entries:Product Number: for example, HERS-RNote You either enter any external alphanumeric ID, and that ID must start with an alphanumeric character, or if you provide no entry, the system automatically assigns a numeric ID.For more information about Product Number, see the previous Material Type and Number Ranges section.Product Type: HERSProduct Group: for example, Raw Materials (L002)Description: <any description> |  |  |
| 5 | Choose OK | In the Create Master Data Record view, choose OK. | The Product view displays. |  |
| 6 | Enter Basic Data | In the Product view, choose Show More in General Information tab, make the following entry:Internal Product Number: your firm’s own material, for example, HB01Note Assign a manufacturer part profile (for example: IMPN) to your company's material first.In the standard SAP system, the Manufacturer part profile field appears on the Purchasing screen in the material master.Manufacturer Part Number: for example, HERS-R-EXManufacturer Number: for example, 33300001 |  |  |
| 7 | Enter Descriptions Data (optional) | In the Descriptions section, choose Create, make the following entries:Language: for example, German(DE)Product: <your description> | Description in default language (for example, English) is already populated. |  |
| 8 | Save Your Data | Choose Create . | System message indicates that the object is saved. |  |

#### Create Purchase Order

Prerequisite

In this case specified in above master data creation, the Manufacturer Part material with Material type HERS (for example, HERS-R) is created, which links the supplier or manufacturer (for example, 33300001), and their material (for example, HERS-R-EX), with your company’s own material (for example, HB01).

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this procedure, you create a purchase order for manufacture part material.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log onto the SAP Fiori launchpad with the Purchaser role. | The SAP Fiori launchpad is displayed. |  |
| 2 | Open Manage Purchase Order | Open Create Purchase Order - Advanced (ME21N).If you want to use the Save Draft feature in this app, you must use a personalized user. | The Manage Purchase Orders screen is displayed.A list of already created Purchase Orders is displayed. |  |
| 3 | Enter Purchase Order Document Type | Enter the following data:Order Type: NB(Standard PO)Then choose Enter. |  |  |
| 4 | Enter Purchase Order data | Enter the following data:Supplier: 33300001On the Org. Data tab:Purchasing Organization:3310Purchasing Group:002Company Code: 3310In the Item Overview area:Material: for example, HBRS-R PO Quantity: xNet Price: xCurrency: AEDDelivery date: a date in the futurePlant: 3310Storage Location: 331BThen choose Enter.In the Item Details area:On the Material Data tab, the following MPN related information are displayed:MPN material: for example, HERS-RMfr Part Number: for example, HERS-R-EXMfr Part Profile: IMPN Manufacturer’s Parts (Inventory-Managed)Manufacture: for example, 33300001 | All data are entered, the item details screen displays. |  |
| 5 | Check Purchase Order for completeness and Save Purchase Order | Choose Save to save the Purchase Order. | A new Purchase Order is created. Purchase order number is displayed, write it down for further use. |  |

After Purchase order creation, you can go ahead for the subsequent process of posting goods receipt and creating supplier invoice accordingly.

In the last, after testing is done, please remove the manufacturer part profile (for example: IMPN ) from your company’s own material HB01 accordingly.

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
> Flagged while digesting this document, not verified: Serial-number invoice step uses Invoice Party 33300007, whereas the other invoice scripts and sample master data use supplier 33300001 (33300007 is not in the listed master data).

## Connections
- part-of :: [[_cluster]]
- see-also :: [[11-inventory-warehouse-and-transportation/batch-derivation-consumer-products-77g-ae-1204]]
- see-also :: [[11-inventory-warehouse-and-transportation/serial-number-management-in-logistics-bll-ae-test-script-1284]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/2TW_S4CLD2608_BPD_EN_AE.docx` — full document · extracted with `mammoth` · 61,425 chars in the whole document
