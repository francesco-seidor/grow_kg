---
id: 10-procurement/scheduling-agreements-in-procurement-bmr-ae-test-script-sap-s-4hana-cl
title: "Scheduling Agreements in Procurement (BMR_AE) - Test Script, SAP S/4HANA Cloud Public Edition (BMR_S4CLD2608_BPD_EN_AE)"
description: "SAP S/4HANA Cloud Public Edition 2608 (AE) test script for scheduling agreements in procurement: prerequisites, three test cases, Fiori apps, roles, sample data."
cluster: 10-procurement
tags: [kb/procurement, topic/scheduling-agreements]
aliases: [BMR_S4CLD2608_BPD_EN_AE]
keywords: [Purchase Scheduling Agreements, scheduling agreements, scheduling agreement with release doc, scheduling agreement without release doc, edi supplier integration, delivery schedule, quota arrangement, mrp run, flexible workflow approval, purchasing info record]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/BMR_S4CLD2608_BPD_EN_AE.docx]
confidence: low
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-1291
topic: 10-procurement/scheduling-agreements
language: EN
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Scheduling Agreements in Procurement (BMR_AE) - Test Script, SAP S/4HANA Cloud Public Edition (BMR_S4CLD2608_BPD_EN_AE)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/BMR_S4CLD2608_BPD_EN_AE.docx`, extracted with `mammoth`. Grouped under **Purchase Scheduling Agreements** in Procurement. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

|  |  |
| --- | --- |
| Scheduling Agreements in Procurement (BMR_AE)Purpose PUBLIC 1<!-- image omitted: unnamed --> | Test ScriptSAP S/4HANA Cloud Public Edition - 19-06-26 |
|  | Scheduling Agreements in Procurement (BMR_AE) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Table of Contents

[1 Purpose 3](#_Toc232862390)

[2 Prerequisites 4](#_Toc232862391)

[2.1 System Access 4](#_Toc232862392)

[2.2 Roles 4](#_Toc232862393)

[2.3 Master Data and Organizational Data 5](#_Toc232862394)

[2.4 Additional Manual Configuration 6](#_Toc232862395)

[2.5 Business Conditions 7](#_Toc232862396)

[2.6 Preliminary Steps 7](#_Toc232862397)

[2.6.1 Activate Flexible Workflow for Scheduling Agreement Approval 7](#_Toc232862398)

[2.6.2 Configure Flexible Workflow for Scheduling Agreement 8](#_Toc232862399)

[2.6.3 Create Purchasing Info Record (Optional) 9](#_Toc232862400)

[2.6.4 Create Purchasing Info Record (Optional) 11](#_Toc232862401)

[2.6.5 Edit User-Specific Parameters for Supplier Invoices (Optional) 14](#_Toc232862402)

[2.6.6 Maintain Release Creation Profile for Scheduling Agreement with Release Document (Optional) 15](#_Toc232862403)

[3 Overview Table 17](#_Toc232862404)

[4 Test Procedures 20](#_Toc232862405)

[4.1 Scheduling agreement w/ Release doc for Standard Procurement 20](#_Toc232862406)

[4.1.1 Create Scheduling Agreement w/ Release doc - Standard 20](#_Toc232862407)

[4.1.2 Mass Changes to Scheduling Agreements (Optional) 22](#_Toc232862408)

[4.1.3 Maintain Delivery Schedule 23](#_Toc232862409)

[4.1.4 Quota Arrangement in Scheduling Agreement (Optional) 24](#_Toc232862410)

[4.1.4.1 Create Scheduling Agreement w/ Release doc - Standard 24](#_Toc232862411)

[4.1.4.2 Maintain Quota Arrangement 26](#_Toc232862412)

[4.1.4.3 Create Planned Independent Requirements 27](#_Toc232862413)

[4.1.4.4 MRP Run for One Single Item 28](#_Toc232862414)

[4.1.4.5 Evaluate Stock/Requirements Situation 30](#_Toc232862415)

[4.1.4.6 Display Delivery Schedule 30](#_Toc232862416)

[4.1.4.7 Check the allocated Quantity in Quota Arrangement 31](#_Toc232862417)

[4.1.5 Print Scheduling Agreement 32](#_Toc232862418)

[4.1.6 Release Scheduling Agreement 33](#_Toc232862419)

[4.1.7 Check Scheduling Agreement Release Documentation 34](#_Toc232862420)

[4.1.8 Print Scheduling Agreement Releases 34](#_Toc232862421)

[4.1.9 Evaluate the Stock/Requirement Situation 35](#_Toc232862422)

[4.1.10 Post Goods Receipt 37](#_Toc232862423)

[4.1.11 Create Supplier Invoice with Scheduling Agreement/GR Relation 38](#_Toc232862424)

[4.2 Scheduling Agreement w/o Release doc for Standard Procurement 40](#_Toc232862425)

[4.2.1 Create Scheduling Agreement w/o Release doc - Standard 40](#_Toc232862426)

[4.2.2 Approve Scheduling Agreement (Optional) 41](#_Toc232862427)

[4.2.3 Maintain Delivery Schedule 42](#_Toc232862428)

[4.2.4 Print Scheduling Agreement 43](#_Toc232862429)

[4.2.5 Evaluate the Stock/Requirement Situation 44](#_Toc232862430)

[4.2.6 Post Goods Receipt 45](#_Toc232862431)

[4.2.7 Create Supplier Invoice with Scheduling Agreement/GR Relation 46](#_Toc232862432)

[4.3 Integration of Scheduling Agreement Procurement with External Suppliers 48](#_Toc232862433)

[4.3.1 Create Scheduling Agreement with Release Doc - Standard 48](#_Toc232862434)

[4.3.2 Maintain Delivery Schedule 50](#_Toc232862435)

[4.3.3 Print Scheduling Agreement 51](#_Toc232862436)

[4.3.4 Release Scheduling Agreement 51](#_Toc232862437)

[4.3.5 Check Scheduling Agreement Releases 52](#_Toc232862438)

[4.3.6 Send Forcast & JIT Delivery Schedule – EDI relevant 53](#_Toc232862439)

[4.3.7 Check Forecast and JIT Delivery Schedule in AIF (Message Dashboard) 54](#_Toc232862440)

[4.3.8 Check Incoming Inbound Delivery in AIF (Message Dashboard) 54](#_Toc232862441)

[4.3.9 Review Inbound Delivery Document in Scheduling Agreement Document 55](#_Toc232862442)

[4.3.10 Post Goods Receipt for Inbound Delivery 56](#_Toc232862443)

[4.3.11 Check Incoming Invoice in AIF (Message Dashboard) 57](#_Toc232862444)

[4.3.12 Review Supplier Invoice 58](#_Toc232862445)

[5 Appendix 59](#_Toc232862446)

[5.1 Process Integration 59](#_Toc232862447)

[5.1.1 Succeeding Processes 59](#_Toc232862448)

[5.2 Relevant Features 59](#_Toc232862449)

## Purpose

Overview

The use of scheduling agreements can shorten processing times and reduce the amount of paperwork you are faced with. One delivery schedule can replace many discrete purchase orders or contract release orders.

Delivery of the total quantity of materials specified in a scheduling agreement item is spread over a certain period in a delivery schedule, consisting of lines indicating the individual quantities with their corresponding planned delivery dates.

Inventories can be reduced to a minimum. You can perform your manufacturing operations on the Just-in-Time (JIT) principle.

Your suppliers require shorter lead times. Smaller deliveries are required, which can be spaced out over a longer period. Delivery scheduling enables suppliers to plan and allocate their resources more efficiently.

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

| Name (Role Template) | ID (Role Template) | Name (Launchpad Space) | ID (Launchpad Space) | Log on |
| --- | --- | --- | --- | --- |
| Purchaser | SAP_BR_PURCHASER | Purchasing / Sourcing and Contracting | SAP_MM_SPT_PURCHASING_PC / SAP_MM_SPT_SOURCING_PC |  |
| Purchasing Manager | SAP_BR_PURCHASING_MANAGER | My Inbox | SAP_CORE_SPT_MYINBOX_PC |  |
| Production Planner | SAP_BR_PRODN_PLNR | Production Planning | SAP_BR_PRODN_PLNR |  |
| Warehouse Clerk | SAP_BR_WAREHOUSE_CLERK | Inventory Processing | SAP_BR_WAREHOUSE_CLERK |  |
| Material Planner - External Procurement | SAP_BR_MATL_PLNR_EXT_PROC | Material Planning - External Procurement | SAP_BR_MATL_PLNR_EXT_PROC |  |
| Configuration Expert - Business Process Configuration | SAP_BR_BPC_EXPERT | Business Process Configuration / Business Process Configuration - Finance / Business Process Configuration - Procurement / Manage your Solution / Business Process Configuration - Workflow / Business Configuration - Feature Management / Business Process Configuration - Extensibility Explorer / Business Configuration - Transportation | SAP_BR_BPC_EXPERT / SAP_FIN_SPT_BPC_EXPERT_PC / SAP_MM_SPT_BIZ_PROC_CONFIGN_PC / SAP_CA_SPT_IC_LND_BASE_PC / SAP_CA_SPT_BPC_WORKFLOW_PC / SAP_CA_SPT_BPC_FM_PC / SAP_EI_SPT_BPC_EXT_PC / SAP_TM_SPT_TRANSPCFG_PC |  |
| Receiving Specialist | SAP_BR_RECEIVING_SPECIALIST | Receiving | SAP_BR_RECEIVING_SPECIALIST |  |
| Configuration Expert - Business Network Integration | SAP_BR_CONF_EXPERT_BUS_NET_INT |  |  |  |
| Accounts Payable Accountant | SAP_BR_AP_ACCOUNTANT | Accounts Payable / Central Invoice Management - Supplier Invoices / Central Invoicing - Supplier Invoice | SAP_BR_AP_ACCOUNTANT / SAP_MM_SPT_CIM_INV_PC / SAP_MM_SPT_CNTRL_INVOICING_PC |  |

### Master Data and Organizational Data

The organizational structure and master data of your company has been created in your system during activation. The organizational structure reflects the structure of your company. The master data represents materials, customers, and vendors, for example, depending on the operational focus of your company.

|  |
| --- |
| Caution Update Behavior of Predelivered Demo DataIn non-productive environments (such as starter systems, sandbox systems, or partner demo systems), SAP initially deploys demo data for your selected scope. You can use this data to test and evaluate business processes.In a customer system, you can receive new or updated demo data after initial activation with further scope enhancements, provided the existing demo data wasn't changed in an incompatible way. If activation errors occur due to incompatible changes in demo data, you're responsible for resolving them. If you don't resolve the errors within a specific time frame, SAP reserves the right to deactivate demo data in your systems. In this case, you can continue by creating your own demo data. Alternatively, you can request that your systems be reprovisioned if you want to work with predelivered demo data again.In partner systems, you can use the demo data deployed with the initial activation. No additional demo data will be deployed in the system with scope enhancements. You can only create additional demo data manually. |

Use your own master data or the following sample data to go through the test procedure.

| Data | Sample Value | Details | Comments |
| --- | --- | --- | --- |
| Material | RM129 | RAW129,PD | Update Period Indicator with M (Monthly) in MRP3 view |
| Plant | 3310 | Plant 1 AE |  |
| Storage Location | 331C | Raw mat. stoloc. |  |
| Supplier | 33300001 | Domestic UAE Supplier 1 | Note If you want to send form print outs via e-mail instead of using the print functionality make sure that you have maintained a valid e-mail address in the supplier master data. |
| Supplier | 33300002 | Domestic UAE Supplier 2 | Note If you want to send form print outs via e-mail instead of using the print functionality make sure that you have maintained a valid e-mail address in the supplier master data. |
| Company Code | 3310 | Company Code 3310 |  |
| Purchase Organization | 3310 | Purch. Org. 3310 |  |
| Purchase group | 001 | Group 001 |  |

You can find general information on how to create master data objects in the following [Master Data Scripts (MDS)](https://help.sap.com/docs/s4hana-best-practices/s4cld2608-master-data) :

Table 1: Master Data Script Reference

| MDS | Description |
| --- | --- |
| BNR | Create Product Master of type "Raw Material" - MDS |
| BNE | Create Supplier Master - MDS |
| BHD | Create Purchasing Info Record - MDS |
| BF6 | Create Scheduling Agreement - MDS |

### Additional Manual Configuration

Before you can test this scope item, you must have completed the additional configuration steps that are described in the Set-Up Instructions for this scope item. These configuration steps are specific for your implementation and include mandatory settings that are not delivered by SAP and must be created by you. For more information, follow the link to the document:

[Link to Set-Up Instructions](https://help.sap.com/docs/SAP_S4HANA_BEST_PRACTICES/9940e9f6cac580de173a2ada933ed741)

### Business Conditions

Before this scope item can be tested, the following business conditions must be met.

| Scope Item | Business Condition |
| --- | --- |
| BNZ - Create New Open MM Posting Period - MDS | You have completed the step described in the Create New Open MM Posting Period - MDS (BNZ) master data script. Posting Period is up to date. |

### Preliminary Steps

#### Activate Flexible Workflow for Scheduling Agreement Approval

Purpose

In this procedure, you activate flexible workflow for Scheduling Agreement approval.

If you want to use the flexible workflow to manually approve the Scheduling Agreement, you have to process the steps: Activate Flexible Workflow for Scheduling Agreement Approval and Configure Flexible Workflow for Scheduling Agreement.

Procedure

Depending on your configuration environment for SAP S/4HANA Cloud Public Edition, choose one of the following options:

Configure Your Solution:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log onto the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration . | The SAP Fiori Launch Pad displays. |  |
| 2 | Access the App | Open Manage Your Solution (F1241). | The Manage Your Solution screen displays. |  |
| 3 | Open Configure Your Solution | Choose Configure Your Solution. | The Configure Your Solution screen displays. |  |
| 4 | Open Active Flexible Workflow | On the Configure Your Solution screen, search item Activate Flexible Workflow for Purchase Scheduling Agreements, then click the line Scheduling Agreement Processing.On the Configure Your Solution – Scheduling Agreement Processing screen,In Configuration steps area, choose the Configure button for item Activate Flexible Workflow for Purchase Scheduling Agreements. | The Document Types Scheduling Agreement Change screen displays. |  |
| 5 | Activate Flexible Workflow for PO Approval | Make the following entries and choose Save:Document Type Scenario based workflowLP Scheduling Agreement XLPA SA With Release doc. XNote You may be asked to enter a customizing request number, either choose your own customizing request or create a new one, then click Continue. | The Scenario based workflow is active for Scheduling Agreements with Document Type: LP and LPA. |  |

SAP Central Business Configuration:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Logon | Log on to the project experience in SAP Central Business Configuration. | The SAP Fiori launchpad is displayed. |  |
| 2 | Open Activate Flexible Workflow for Scheduling Agreements | In the Product-Specific Configuration phase, navigate to the Configuration Activities tab. To locate the activity in the tree view, search for the following activity: Activate Flexible Workflow for Purchase Scheduling Agreements.Choose Open Documentation for the found line item to see more details about this configuration activity.Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. | The Document Types Scheduling Agreement Change screen displays. |  |
| 3 | Activate Flexible Workflow for Scheduling Agreements Approval | Make the following entries and choose Save:Document Type Scenario based workflowLP Scheduling Agreement XLPA SA With Release doc. XNote You may be asked to enter a customizing request number, either choose your own customizing request or create a new one, then click Continue. | The Scenario based workflow is active for Scheduling Agreements with Document Type: LP and LPA. |  |

#### Configure Flexible Workflow for Scheduling Agreement

Purpose

In this procedure, you configure your release conditions for scheduling agreement approval.

When you start to process this step, please make sure that the flexible workflow for purchase document type LP has been activated in your system.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log onto the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration role. | The Fiori launchpad is displayed. |  |
| 2 | Access the App | Open Manage Workflows for Purchase Scheduling Agreements (F3044). | The Manage Workflows screen is displayed. |  |
| 3 | Create Manage Workflow | Choose Create and make following entries:Name: Test Workflow for Scheduling AgreementIn the Start Conditions area select Purchasing Group of scheduling agreement is with value: 001Choose Create Alternative Preconditions and make the following entries:Choose Document type of scheduling agreement is with value: LP Scheduling AgreementIn the Header area choose the Create button and make following entry:Step Type: Release of Scheduling AgreementIn Recipients area:Assignment By: UserUser: Select the User ID with Employee ID PURCHASING_MANAGER from F4 helpStep to be completed by: One of the recipientsChoose Create.Choose Save. | The workflow for scheduling agreement is configured. |  |
| 4 | Activate Workflow Item | Select the just created workflow item and choose Activate. | The workflow item is activated. |  |

|  |
| --- |
| Note Please make sure default workflow Automatic Release of Scheduling Agreement has been activated. |

#### Create Purchasing Info Record (Optional)

Purpose

To run through this test script, the info records for the necessary materials must be available as master data. If the Info Record has not been maintained in the system yet, create the required master data. Otherwise you can skip this step.

The purpose of this activity is to create the info records for materials, for example, RM129 and choose a valid supplier (for example, 33300001).

This step is obsolete if the necessary info records are present. Check the info records supplier 33300001, material RM129 and Purchasing Organization 3310. The existing info records for this material are displayed on the screen.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log onto the SAP Fiori launchpad as a Purchaser. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the App | Open Manage Purchasing Info Records (F1982). | The Manage Purchasing Info Records screen is displayed. |  |
| 3 | Open New Purchasing Info Record | Choose Create. | The New Purchasing Info Record Screen is displayed. |  |
| 4 | Enter Header Data | Make the following entries:Purchasing Info Record Category: StandardPurchasing Organization: 3310Supplier: 33300001Material: RM129Plant: 3310Purchasing Group: 001 | Header data is added. |  |
| 5 | Enter General Information | Under General Information section make the following entries:Available From: TodayAvailable To: 12/31/9999 | General Information is added. |  |
| 6 | Enter Purchasing Data | Under the Purchasing Data section, make the following entries:Incoterm: EXWNote Incoterms and their corresponding versions are grouped in the F4 value help. Selecting an incoterm automatically populates its associated version, which can be subsequently modified or removed if needed.Incoterm Location 1: VENDOR | Purchasing Data is added. |  |
| 7 | Enter Delivery and Quantity Data | Under the Delivery and Quantity Data section, make the following entries:Delivery Time in Days: 1Under Delivery Tolerance in %: 10.0Over Delivery Tolerance in %: 10.0Tax Code: <Input Tax Code>Note If time dependent tax (TDT) is activated, and fields Country/Region Key for company code, Validity Periods and Tax Code are maintained via SSCUI 101016 in SAP S/4HANA Cloud Public Edition or the configuration activity Define Tax Codes for Sales and Purchases in Central Business Configuration, you must maintain the Tax Rate Valid From field in the New Purchasing Info Record screen. If you enter the current date, this date will be adjusted to a valid start date for your tax code according to the SSCUI/configuration activity settings.If Registration for Indirect Taxation Abroad (RITA) is activated, and tax registration country and tax code are maintained for company code via SSCUI 103464 in SAP S/4HANA Cloud Public Edition or the configuration activity Activate RITA and Maintain Tax Registration Countries in Central Business Configuration, you must maintain the Tax Country field. The default value of this field is the country ID of company code, but you can change it to a valid country ID that is maintained in the SSCUI/configuration activity accordingly.Order Unit: PCStandard Order Quantity: 1000 | Delivery and Quantity Data is added. |  |
| 8 | Enter Condition Data | In the Conditions section, choose Create.In the General Information area, make the following entries:Valid From: TodayValid To: 12/31/9999Amount: 1755Pricing Unit: 100Currency: AEDChoose Apply. | Condition Data is added |  |
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

The purpose of this activity is to create the info record for materials, for example, RM129 and choose a valid supplier (for example, 33300002).

This step is obsolete if the necessary info records are present. Check the info record supplier 33300002, material RM129 and Purchasing Organization 3310. The existing info record for this material are displayed on the screen.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log onto the SAP Fiori launchpad as a Purchaser . | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the App | Open Manage Purchasing Info Records (F1982) . | The Manage Purchasing Info Records screen is displayed. |  |
| 3 | Open New Purchasing Info Record | Choose Create. | The Purchasing Info Record Screen is displayed. |  |
| 4 | Enter Header Data | Make the following entries:Purchasing Info Record Category: StandardPurchasing Organization: 3310Supplier: 33300002Material: RM129Plant: 3310Purchasing Group: 002 | Header data is added. |  |
| 5 | Enter General Information | Make the following entries:Available From: TodayAvailable To: 12/31/9999 | General Information is added. |  |
| 6 | Enter Purchasing Data | Make the following entries:Incoterm: EXWNote Incoterms and their corresponding versions are grouped in the F4 value help. Selecting an incoterm automatically populates its associated version, which can be subsequently modified or removed if needed.Incoterm Location 1: VENDORConfirmation Control : [blank] | Purchasing Data is added. |  |
| 7 | Enter Delivery and Quantity Data | Make the following entries:Delivery Time in Days: 1Under Delivery Tolerance in %: 0Over Delivery Tolerance in %: 0Tax Code: <Input Tax Code>Note If time dependent tax (TDT) is activated, and fields Country/Region Key for company code, Validity Periods and Tax Code are maintained via SSCUI 101016 in SAP S/4HANA Cloud Public Edition or the configuration activity Define Tax Codes for Sales and Purchases in Central Business Configuration, you must maintain the Tax Rate Valid From field in the New Purchasing Info Record screen. If you enter the current date, this date will be adjusted to a valid start date for your tax code according to the SSCUI/configuration activity settings.If Registration for Indirect Taxation Abroad (RITA) is activated, and tax registration country and tax code are maintained for company code via SSCUI 103464 in SAP S/4HANA Cloud Public Edition or the configuration activity Activate RITA and Maintain Tax Registration Countries in Central Business Configuration, you must maintain the Tax Country field. The default value of this field is the country ID of company code, but you can change it to a valid country ID that is maintained in the SSCUI/configuration activity accordingly.Order Unit: PCStandard Order Quantity: 1 | Delivery and Quantity Data is added. |  |
| 8 | Enter Condition Data | In the Condition section, choose Create.In the General Information area, make the following entries:Valid From: TodayValid To: 12/31/9999Amount: <xxx>Pricing Unit: 100Currency: AEDChoose Apply. | Condition Data is added |  |
| 9 | Enter Reference Data (optional) | You can enter reference data. | Reference data is added. |  |
| 10 | Save your data | Choose Create. | The purchasing info record is saved. |  |

#### Edit User-Specific Parameters for Supplier Invoices (Optional)

Purpose

In this procedure, you will edit User-Specific parameters for supplier invoices.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Accounts Payable Accountant. | The Fiori launchpad is displayed. |  |
| 2 | Access the App | Open Edit Supplier Invoice Settings (F3813) | The Edit Supplier Invoice Settings screen is displayed. |  |
| 3 | Set parameter | Check parameter Display Journal Entry: XNote If parameter is checked, when invoice is created, system message contains invoice and journal entry number.If parameter is unchecked, when invoice is created, system message contains invoice number only.When this parameter is changed, for APP Create Supplier Invoice, it will take effective immediately. For APP Create Supplier Invoice – Advanced, user needs to logout and login again to put it into effect. | Change has been saved successfully. |  |

Result

Parameter Display Journal Entry has been set successfully.

#### Maintain Release Creation Profile for Scheduling Agreement with Release Document (Optional)

Purpose

In this procedure, you can create a new release creation profile for scheduling agreement or make change on an existing one.

If you want to use the creation profile for scheduling agreement which is defined by yourself, you must process this step.

Procedure

Depending on your configuration environment for SAP S/4HANA Cloud Public Edition, choose one of the following options:

Configure Your Solution:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log onto the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration . | The SAP Fiori Launch Pad displays. |  |
| 2 | Access the App | Open Manage Your Solution (F1241). | The Manage Your Solution screen displays. |  |
| 3 | Open Configure Your Solution | Choose Configure Your Solution. | The Configure Your Solution screen displays. |  |
| 4 | Open Maintain Creation profile for Scheduling Agreement w. Rel. Docu. | On the Configure Your Solution screen, search item Release Creation Profile, then click the line Scheduling Agreement Processing.On the Configure Your Solution – Scheduling Agreement Processing screen, in Configuration steps area, choose the Configure button for item Maint. Rel. Creation Profile for Sched. Agmt. w. Rel. Docu.. | The Change View “Release Creation Profile”: Overview screen displays. |  |
| 5 | Create or change Creation profile for Scheduling Agreement w. Rel. Docu. | In the Maint. Rel. Creation Profile for Sched. Agm..: Change screen, you can make a new entry or choose an existing item to maintain it. |  |  |

SAP Central Business Configuration:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the project experience in SAP Central Business Configuration. |  |  |
| 2 | Open the Activity | In the Product-Specific Configuration phase, navigate to the Configuration Activities tab. To locate the activity in the tree view, search for the following activity: Maint. Rel. Creation Profile for Sched. Agmt. w. Rel. Docu..Choose Open Documentation for the found line item to see more details about this configuration activity.Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. | The Change View “Release Creation Profile”: Overview screen displays. |  |
| 3 | Create or change Creation profile for Scheduling Agreement w. Rel. Docu. | In the Maint. Rel. Creation Profile for Sched. Agm..: Change screen, you can make a new entry or choose an existing item to maintain it. |  |  |

## Overview Table

This scope item consists of several process steps that are listed in the following table.

|  |
| --- |
| Note If your system administrator has enabled spaces and pages on the SAP Fiori launchpad, the homepage will only contain the essential apps for performing the typical tasks of a business role.You can find all other (searchable) apps not included on the homepage using the search bar ([2434549](https://me.sap.com/notes/2434549)).If you want to personalize the homepage and include the hidden apps, navigate to your user profile and choose App Finder. |

Table 2: Case 1.Scheduling agreement w/ Release doc for Standard Procurement

| Process Step | Business Role | Transaction/App | Expected Results |
| --- | --- | --- | --- |
| [Create Scheduling Agreement w/ Release doc - Standard](#unique_15) [page ] 20 | Purchaser | Manage Purchase Scheduling Agreements (F2179) | A Schedule Agreement is created. |
| [Mass Changes to Scheduling Agreements (Optional)](#unique_16) [page ] 22 | Purchaser | Mass Changes to Purchase Scheduling Agreements (F2668) | The Scheduling Agreement is changed. |
| [Maintain Delivery Schedule](#unique_17) [page ] 23 | Purchaser | Manage Purchase Scheduling Agreements (F2179) | The Delivery Schedule is created. |
| [Create Scheduling Agreement w/ Release doc - Standard](#unique_18) [page ] 24 | Purchaser | Manage Purchase Scheduling Agreements (F2179) | A Schedule Agreement is created. |
| [Maintain Quota Arrangement](#unique_19) [page ] 26 | Purchaser | Manage Quota Arrangements (F1877) | The Quota Arrangement is created. |
| [Create Planned Independent Requirements](#unique_20) [page ] 27 | Production Planner | Maintain PIRs (F3445) | The PIRs is saved. |
| [MRP Run for One Single Item](#unique_21) [page ] 28 | Material Planner - External Procurement | Schedule MRP Runs (F1339) | The Application Jobs tables is refreshed. |
| [Evaluate Stock/Requirements Situation](#unique_22) [page ] 30 | Material Planner - External Procurement | Monitor Material Coverage - Net / Individual Segments (F2101A) | The MRP has created schedule lines. |
| [Display Delivery Schedule](#unique_23) [page ] 30 | Purchaser | Manage Purchase Scheduling Agreements (F2179) | Scheduling agreement is updated with schedule lines. |
| [Check the allocated Quantity in Quota Arrangement](#unique_24) [page ] 31 | Purchaser | Manage Quota Arrangements (F1877) |  |
| [Print Scheduling Agreement](#unique_25) [page ] 32 | Purchaser | Manage Purchase Scheduling Agreements (F2179) | The Scheduling Agreement is printed. |
| [Release Scheduling Agreement](#unique_26) [page ] 33 | Purchaser | Manage Purchase Scheduling Agreements (F2179) | The Scheduling Agreement is released. |
| [Check Scheduling Agreement Release Documentation](#unique_27) [page ] 34 | Purchaser | Manage Purchase Scheduling Agreements (F2179) |  |
| [Print Scheduling Agreement Releases](#unique_28) [page ] 34 | Purchaser | Manage Purchase Scheduling Agreements (F2179) |  |
| [Evaluate the Stock/Requirement Situation](#unique_29) [page ] 35 | Material Planner - External Procurement | Monitor Material Coverage - Net / Individual Segments (F2101A) | The stock/requirement sitution is displayed. |
| [Post Goods Receipt](#unique_30) [page ] 37 | Warehouse Clerk | Post Goods Receipt for Purchasing Document (F0843) | Goods receipt is posted against the scheduling agreement. |
| [Create Supplier Invoice with Scheduling Agreement/GR Relation](#unique_31) [page ] 38 | Accounts Payable Accountant | Create Supplier Invoice (F0859) | The Supplier Invoice is posted. |

Table 3: Case 2. Scheduling Agreement w/o Release doc for Standard Procurement

| Process Step | Business Role | Transaction/App | Expected Results |
| --- | --- | --- | --- |
| [Create Scheduling Agreement w/o Release doc - Standard](#unique_32) [page ] 40 | Purchaser | Manage Purchase Scheduling Agreements (F2179) | A Schedule Agreement is created. |
| [Approve Scheduling Agreement (Optional)](#unique_33) [page ] 41 | Purchasing Manager | My Inbox - All Items (F0862) | A Schedule Agreement is approved. |
| [Maintain Delivery Schedule](#unique_34) [page ] 42 | Purchaser | Manage Purchase Scheduling Agreements (F2179) | A Delivery Schedule is maintained. |
| [Print Scheduling Agreement](#unique_35) [page ] 43 | Purchaser | Manage Purchase Scheduling Agreements (F2179) | A Schedule Agreement is printed. |
| [Evaluate the Stock/Requirement Situation](#unique_36) [page ] 44 | Material Planner - External Procurement | Monitor Material Coverage - Net / Individual Segments (F2101A) | The stock/requirement sitution is displayed. |
| [Post Goods Receipt](#unique_37) [page ] 45 | Warehouse Clerk | Post Goods Receipt for Purchasing Document (F0843) | Goods receipt is posted against the scheduling agreement. |
| [Create Supplier Invoice with Scheduling Agreement/GR Relation](#unique_38) [page ] 46 | Accounts Payable Accountant | Create Supplier Invoice (F0859) | The Supplier Invoice is posted. |

Table 4: Case 3.Integration of Scheduling agreement Procurement with External Suppliers

| Process Step | Business Role | Transaction/App | Expected Results |
| --- | --- | --- | --- |
| [Create Scheduling Agreement with Release Doc - Standard](#unique_39) [page ] 48 | Purchaser | Manage Purchase Scheduling Agreements (F2179) | A Schedule Agreement is created. |
| [Maintain Delivery Schedule](#unique_40) [page ] 50 | Purchaser | Manage Purchase Scheduling Agreements (F2179) | The Delivery Schedule is created. |
| [Print Scheduling Agreement](#unique_41) [page ] 51 | Purchaser | Manage Purchase Scheduling Agreements (F2179) | The Scheduling Agreement is printed. |
| [Release Scheduling Agreement](#unique_42) [page ] 51 | Purchaser | Manage Purchase Scheduling Agreements (F2179) | The Scheduling Agreement is released. |
| [Check Scheduling Agreement Releases](#unique_43) [page ] 52 | Purchaser | Manage Purchase Scheduling Agreements (F2179) | The Scheduling Agreement is released. |
| [Send Forcast & JIT Delivery Schedule – EDI relevant](#unique_44) [page ] 53 |  |  | Forecast & JIT Delivery Schedule are automati-cally sent to the Buyer system. |
| [Check Forecast and JIT Delivery Schedule in AIF (Message Dashboard)](#unique_45) [page ] 54 | Configuration Expert - Business Network Integration | Message Dashboard | The message is checked in dashborad |
| [Check Incoming Inbound Delivery in AIF (Message Dashboard)](#unique_46) [page ] 54 | Configuration Expert - Business Network Integration | Message Dashboard | The message is checked in dashborad |
| [Review Inbound Delivery Document in Scheduling Agreement Document](#unique_47) [page ] 55 | Purchaser | Display Scheduling Agreement (ME33L) | Incoming Inbound Delivery generated. |
| [Post Goods Receipt for Inbound Delivery](#unique_48) [page ] 56 | Receiving Specialist | Change Inbound Delivery (VL32N) | Goods receipt is posted against the inbound delivery. |
| [Check Incoming Invoice in AIF (Message Dashboard)](#unique_49) [page ] 57 | Configuration Expert - Business Network Integration | Message Dashboard | The message is checked in dashborad |
| [Review Supplier Invoice](#unique_50) [page ] 58 | Accounts Payable Accountant | Supplier Invoices List (F1060A) | The Supplier Invoice is posted. |

## Test Procedures

This section describes test procedures for each process step that belongs to this scope item.

### Scheduling agreement w/ Release doc for Standard Procurement

#### Create Scheduling Agreement w/ Release doc - Standard

Purpose

This activity is used to create the scheduling agreement for the material/supplier combination, for example, material RM129 and supplier 33300001. This activity is used to create the scheduling agreement without release doc for the material/supplier combination if it has not been maintained yet. If the scheduling agreement is already present in the system, you can skip this step.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log onto the SAP Fiori launchpad as a Purchaser. | SAP Fiori launchpad displays |  |
| 2 | Access the SAP Fiori app | Open Manage Purchase Scheduling Agreements (F2179) tile. | The Manage Purchase Scheduling Agreements list page displays. |  |
| 3 | Create Scheduling Agreement | Select Create to create a new scheduling agreement | The New Purchase Scheduling Agreement header view displays. |  |
| 4 | Enter Header Data | Create a new scheduling agreement with the following data:Agreement type: SA With Release doc. (LPA)Supplier: 33300001Validity Start: Default Today.Validity End: MM/DD/YYYY, e.g. today + 720 days.Purchasing Organization: 3310.Purchasing Group: 001In section Delivery and Payment:Target Value : 200000 AED |  |  |
| 5 | Enter Header notes | Navigate to the Notes section, enter some of the Header Notes as below:Header textHeader notePricing typesDeadlinesTerms of deliveryShipping instructionsTerms of paymentWarrantiesPenalty for breach of contractGuaranteesContract riders (clauses)AssetOther contractual stipulationInbound DeliveryVendor memo (general)Vendor memo (pur. org.) |  |  |
| 6 | Add Items to Scheduling Agreement | From the New Purchase Scheduling Agreement view, choose the Items facets and select Create. | The Purchase Scheduling Agreement Item view displays. |  |
| 7 | Enter Item data | On the Items facets view, make the following entries:Plant: 3310Material: RM129Target Quantity: 120000Net Order Price: Defaulted from Info recordTax Code: <Input Tax Code> (Default Value from Info Record)Tax Date: Default TodayNote Field Tax Date is only available for the countries/regions that Time-Dependent Taxes (TDT) is enabled.In the Output Control area, make the following entry:Creation Profile: S001 |  |  |
| 8 | Enter Item notes | Navigate to the Notes section and add the required Notes as below:Item textInfo record PO textMaterial PO textDelivery textInfo record noteES Master Agreements (MA)ES Requests f. Proposals (RFP)Sequence Number LPChoose Apply at the bottom of the view. |  |  |
| 9 | Save | Return to the New Purchase Scheduling Agreement header view and choose Create at the bottom of the view.Make a note of the schedule agreement number. | A schedule agreement is created. |  |

#### Mass Changes to Scheduling Agreements (Optional)

Purpose

In this procedure, you can apply changes to multiple selected Scheduling Agreements in bulk.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log onto Fiori Launchpad | Log onto the SAP Fiori launchpad using the Purchaser role. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Mass Changes to Purchase Scheduling Agreements (F2668) . | The Mass Changes to Scheduling Agreements screen displays. |  |
| 3 | Search for Scheduling Agreements | Set values to some filters to search scheduling agreements. For example:Supplier: 33300001 Domestic UAE Supplier 1Purchasing Group: Group 001Plant: Plant 1 AEThen choose GO. | The search results show the details with the respective filter criteria. |  |
| 4 | Display Scheduling Agreement | Choose Scheduling Agreement Headers tab and click an individual Scheduling Agreement and choose More Links,In the dialog box Define Link List, select Manage Scheduling Agreements, choose OK.Then the link of Manage Scheduling Agreements appears under the scheduling agreement no., click Manage Scheduling Agreements. | The Scheduling Agreement detail screen displays.Verify data displays on the object page.Choose Back. |  |
| 5 | Set new values for selected Scheduling Agreements | Choose Scheduling Agreement Items tab and select the desired Scheduling Agreement(s) for Mass Change operation.Choose Mass Edit. | A dialog box will open displaying fields for Item fields. |  |
| 6 | Apply Mass Changes | Set new values in the given desired fields e.g. Requirement Tracking Number, Short TextChoose <Enter New Values>.Enter new value in the blank field.Choose Apply Mass Changes. | 1.New values will be set to desired fields for selected Scheduling Agreements.2.Confirmation dialog box would appear to confirm mass changes where Job description can also be added.3.After choosing Apply, message Mass Change Job has been scheduled displays. Choose Close. |  |
| 7 | Check Application Jobs | Choose View Job List. | It will navigate to Application Jobs page containing the list of Job IDs for all Scheduling Agreements.Verify if the job is successful for the selected Scheduling Agreements. |  |

#### Maintain Delivery Schedule

Purpose

The purpose of this activity is to create the delivery schedule for the scheduling agreement if it has not been maintained while creating the scheduling agreement.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log onto Fiori launchpad | Log onto the Fiori launchpad using the role Purchaser . | The SAP Fiori Launchpad displays. |  |
| 2 | Access the App | Open Manage Purchase Scheduling Agreements (F2179) . | The Manage Purchase Scheduling Agreements screen displays. |  |
| 3 | Find scheduling agreement number | Find the appropriate newly created scheduling agreement through the search criteria, such as: Supplier: 33300001,Agreement Type: LPA (SA With Release doc.),Purchasing Organization: 3310, then choose Go. Select one item from the search result. | The desired scheduling agreement appears on the list page of Manage Purchase Scheduling Agreements. |  |
| 4 | Select Scheduling Agreement | Navigate to the selected scheduling agreement by clicking on Chevron (>) or by directly clicking on the Scheduling agreement number from the list page. | The Scheduling agreement header object page appears in display mode. |  |
| 5 | Maintain Delivery Schedule | 1. Click on the Edit at the right upper corner on the Manage Scheduling Agreement Header Object page.2. In Items tab, click on the desired item for which delivery schedule needs to be maintained. | The Purchase Scheduling Agreement Item screen displays. |  |
| 6 | Maintain Delivery Schedule | Go to the Schedule Lines section on the Purchase Scheduling Agreement Item screen and choose Create. You will get into the Manage Purchase Scheduling Agreements screen to maintain the schedules for the item, make following entries:Date type: <Day format>Delivery Date: Today's dateDelivery Time: 10:00:00Scheduled Quantity: 10Choose Apply twice at the right bottom to add a schedule line. | You will be navigated back to Scheduling Agreement Header object page. |  |
| 7. | Save | Choose Save from the Scheduling Agreement Header object page. | Scheduling agreement will get updated with schedule lines. |  |

#### Quota Arrangement in Scheduling Agreement (Optional)

##### Create Scheduling Agreement w/ Release doc - Standard

Purpose

This activity is used to create the scheduling agreement for the material/supplier combination, for example, material RM129 and supplier 33300002, if it has not been main-tained yet. If the scheduling agreement is already present in the system you can skip this step.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log onto the SAP Fiori launchpad, as Purchaser . | SAP Fiori launchpad displays |  |
| 2 | Access the SAP Fiori app | Open Manage Purchase Scheduling Agreements (F2179) tile. | The Manage Purchase Scheduling Agreements list page displays |  |
| 3 | Create Scheduling Agreement | Select Create to create a new scheduling agreement. | The New Purchase Scheduling Agreement header view displays. |  |
| 4 | Enter Header Data | Create a new scheduling agreement with the following data:Supplier: 33300002Agreement type: LPA (SA With Release doc.)Validity End: MM/DD/YYYYPurchasing Organization: 3310Purchasing Group: 001Target Value : 200000AED |  |  |
| 5 | Add Items to Scheduling Agreement | From the New Purchase Scheduling Agreement view, choose the Items column and select Create. | The Purchase Scheduling Agreement Item |  |
| 6 | Enter Item Data | On the Items facets view, make the following entries:Plant: 3310Material: RM129Target Quantity: 120000Net Order Price: Defaulted from Info recordIn the Output Control area, make the following entry:Creation Profile: S001Choose Apply at the bottom of the view. |  |  |
| 7 | Save | Return to the New Purchase Scheduling Agreement header view and choose Create at the bottom of the view.Make a note of the schedule agreement number. | A schedule agreement is created. |  |

##### Maintain Quota Arrangement

Purpose

The purpose of this activity is to maintain quota arrangement for the material/supplier combination, for example, material RM129, supplier 33300001and 33300002,if it has not been maintained yet.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on to Fiori launchpad | Logon on to Fiori launchpad as a Purchaser. |  |  |
| 2 | Access the SAP Fiori app | Open Manage Quota Arrangements (F1877) . | The Maintain Quota Arrangements screen displays. |  |
| 3 | Create Quota Arrangement | Select Create to create a new quota arrangement. | The Quota Arrangement screen displays. |  |
| 4 | Enter Header Data | Create a new quota arrangement with the following data:Material: RM129Plant: 3310Valid From: MM/DD/YYYYValid To: MM/DD/YYYY |  |  |
| 5 | Add the first Item to Quota Arrangement | On the Quota Arrangement screen, go to the Items section, and click on Create. | The New Quota Arrangement Item 1 screen displays. |  |
| 6 | Enter Item Data 1 | On the New Quota Arrangement Item 1 screen, make the following entries:Type: External procurementSpecial Procuremnt: 0 Standard external procurementSupplier: 33300001Click on Apply at the right bottom of the screen.On the Quota Arrangement screen, go to the Quota Arrangement Items view, make the following entry for quota arrangement item 1:Quota: e.g, 40Choose Create. | Navigate back to New Quota Arrangement Item with a new item added up in the Items section. |  |
| 7 | Add the second Item to Quota Arrangement | On the Quota Arrangement screen, go to the Quota Arrangement Items view, click on Create. | The New Quota Arrangement Item 2 screen displays. |  |
| 8 | Enter Item Data 2 | On the New Quota Arrangement Item 2 screen, make the following entries:Type: External procurementSpecial Procurement: 0 Standard external procurementSupplier: 33300002Click on Apply.On the Quota Arrangement screen, go to the Quota Arrangement Items view, make the following entry for quota arrangement item 2:Quota: e.g, 60. | Navigate back to New Quota Arrangement Item with a new item added up in the Items section. |  |
| 9 | Save | Choose Save at the right bottom of the screen. | You have created the quota arrangement for the material/supplier combination. |  |

##### Create Planned Independent Requirements

Purpose

Planned independent requirements are used to perform demand management functions. A planned independent requirement contains one planned quantity and one date, or a number of planned independent requirements schedule lines, such as one planned quantity split over time according to dates.

Instead of creating a single requirement, sometimes a requirements plan that includes one or more planned independent requirements can be maintained for mass processing. In this case, the requirements are grouped and maintained under a requirement plan number.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log onto the SAP Fiori Launchpad as a Production Planner . | The SAP Fiori Launchpad displays. |  |
| 2 | Access the App | Open Maintain PIRs (F3445) . |  |  |
| 3 | Check Default Area of Responsibility | Choose the user icon, and select App Settings.In the MRP Settings dialog box, choose Area of Responsibility.On My Area of Responsibility screen, check if the below entry is assigned:Plant 1 AE (3310)MRP Controller 001 (001)Choose AOR Status if the status for the above entry is not yet assigned.Choose AOR Status to unassign the rest of other entries. |  |  |
| 4 | Select Material | On the Maintain PIRs screen,make the following entries:Plant: 3310 (Plant 1 AE)Period Indicator: Monthly (M)Version Active: N/A,Yes and NoMaterial: RM129Note Please make sure you have the same setting in material master data MRP 3 view for 'Period Indicator'. If not, please refer to master data script BNR for adaption. |  |  |
| 5 | Filter Result | Choose Go to execute. | The material item displays. |  |
| 6 | Select Material Item | Select the material item, and choose Edit in the upper right. |  |  |
| 7 | Edit PIRs | In the Maintain PIRs screen, enter quantities per period, for example:PIR: 1000Version is Active: YES |  |  |
| 8 | Save PIRs | Choose Save at the right bottom. | The PIRs are saved. |  |

##### MRP Run for One Single Item

Context

The aim of material requirements planning is to tailor available capacities and receipts on time to suit requirements quantities. You can use MRP or consumption-based planning for this purpose. Single-item multi-level requirement planning is performed for plant 3310.

Prerequisite

The raw material RM129 is planned at plant level. There is now a requirement for the material RM129 in plant 3310.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log onto the SAP Fiori launchpad as a Material Planner - External Procurement . | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Schedule MRP Runs (F1339) . | The Schedule MRP Runs screen displays. |  |
| 3 | Create New Job | Choose Create.On the New Job: Material Requirements Planning (MRP) screen, make the following entries:For 1. Template Selection section:Job Template: Material Requirement Planning (MRP)Job Name: <MRP for RM129>Choose Step 2.For 2. Scheduling Options section:Start Immediately: <select>Choose Define Recurrence Pattern.On the Scheduling Information screen, make the following entries:Start Immediately: XRecurrence Pattern: Single RunChoose OK.Choose Step 3.For 3 Parameters section:Plant: 3310Material: RM129Changed BOM Components: selectPlanning Mode: 1Choose Check at the bottom right.Choose Schedule. | A message appears: You can go ahead and schedule the job. |  |
| 4 | Refresh Application Jobs List | To check the job’s status, enter MRP for RM129 in the search box and choose Go at the top right section of the screen. | The new job is created and is displayed in the Application Jobs table when refreshed. |  |

##### Evaluate Stock/Requirements Situation

Context

After the requirement planning has been performed, you want to display the stock/requirements situation for the raw material RM129 in the stock/requirements list.

Prerequisite

Requirement planning has been carried out.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log onto SAP Fiori Launchpad | Log onto the SAP Fiori launchpad as a Material Planner - External Procurement. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Monitor Material Coverage - Net / Individual Segments (F2101A) . | The Monitor Material Coverage - Net / Individual Segments screen displays. |  |
| 3 | Check Default Setting | Choose the user icon, and select App Settings. In the MRP Settings dialog box, check if toggle button Manage Material Coverage - New Version (F0251A) is switched to ON. Turn it to ON if the toggle button is in status OFF. | If this toggle button is ON, in following steps, you will be navigated to Manage Material Coverage - New Version (F0251A).If this toggle button is OFF, in following steps, you will be navigated to Check Material Coverage - Old Version (F0251). The following steps in this guide describe the scenario when the toggle button is turned to ON. |  |
| 4 | Select Material and Show Shortages | In the Material field, search for RM129, and then choose Go.Choose Manage Materials. | The Manage Material Coverage screen displays. |  |
| 5 | Verify Purchase Requisitions that are Available | In the Stock/Requirements List, to find available schedule lines, look for rows with SchLne items. | The MRP has created schedule lines. |  |

##### Display Delivery Schedule

Purpose

The purpose of this activity is to check the delivery schedule for the scheduling agreement if it has been generated while executing MRP Run.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1. | Log on | Logon on to Fiori launchpad as Purchaser . | The SAP Fiori launchpad displays. |  |
| 2. | Access the App | Open Manage Purchase Scheduling Agreements (F2179) . | You will get into Manage Scheduling Agreements list page. |  |
| 3. | Find scheduling agreement number | Find the appropriate newly created scheduling agreement through the search criteria, such as: Supplier 33300001 or 33300002, Agreement Type LPA (SA With Release doc.), purchase org 3310 , then choose Go button. Select one item from the search result. | The desired scheduling agreement appears on the list page of Manage Purchase Scheduling Agreements. |  |
| 4. | Select Scheduling Agreement | Navigate to the selected scheduling agreement by clicking on cheveron (>) or by directly clicking on the scheduling agreement number from the list page. | The Scheduling agreement header object page appears in display mode. |  |
| 5. | Maintain Delivery Schedule | Under Items section, click on the desired item for which delivery schedule needs to be displayed. | You will get into Scheduling Agreement Item screen. |  |
| 6. | Maintain Delivery Schedule | Go to the Schedule Lines section on the Scheduling Agreement Item screen . You will see the schedule line generated by MRP running.Choose Back. | Scheduling agreement is updated with schedule lines.You will be navigated back to scheduling agreement header object page. |  |

##### Check the allocated Quantity in Quota Arrangement

Purpose

The purpose of this activity is to maintain quota arrangement for the material/supplier combination, for example, material RM129, supplier 33300001 and 33300002,if it has not been maintained yet.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1. | Logon on to Fiori launchpad | Logon on to Fiori launchpad as Purchaser . | The SAP Fiori launchpad displays. |  |
| 2. | Access the App | Open Manage Quota Arrangements (F1877) . | You will get into Maintain Quota Arrangements screen. |  |
| 3. | Search for Quota Arrangement | On the Manage Quota Arrangements screen, make the following entries and choose the Go button.Material: RM129Plant: 3310 | The relevant Quota Arrangements are shown, |  |
| 4. | Display Quota Arrangement | In the list of the Quota Arrangements, select the Quota Arrangement with the valid period by clicking the entire row. | The quota arrangement is displayed. |  |
| 5. | Check Allocated Quantity Details | On the Quota Arrangement screen, the quota-allocated quantities for the two suppliers are shown. | The supplier is assigned by the system. The supplier is determined based on the quota arrangement calculation. |  |

#### Print Scheduling Agreement

Purpose

The purpose of this activity is to print view the scheduling agreement for the material/supplier combination for the new Scheduling agreement or for the one which is already present in the system

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1. | Log onto Fiori launchpad | Log onto the Fiori launchpad as Purchaser . | The SAP Fiori Launchpad displays. |  |
| 2. | Access the App | Open Manage Purchase Scheduling Agreements (F2179) . | The Manage Purchase Scheduling Agreements screen displays. |  |
| 3. | Find scheduling agreement number | Find the appropriate scheduling agreement through the search criteria, such as: Supplier: 33300001,Agreement Type: LPA (SA With Release doc.), Purchasing Organization: 3310, then choose Go. Select one item from the search result. | The desired scheduling agreement appears on the list page of Manage Purchase Scheduling Agreements. |  |
| 4. | Select Scheduling Agreement | Navigate to the selected scheduling agreement by clicking on Chevron (>) or by directly clicking on the Scheduling agreement number from the list page. | The Scheduling agreement header object page appears in display mode. |  |
| 5. | View the output form for scheduling agreement | Go to the Output Control tab and view the output settings maintained for the scheduling agreement. Click on the PDF sign to view the output form of scheduling agreement. | PDF form for scheduling agreement shall open. |  |

#### Release Scheduling Agreement

Purpose

The purpose of this activity is to release the schedules for the respective scheduling agreement at scheduling agreement level or item level.

You can choose release scheduling agreement either at scheduling agreement level or item level.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1. | Log onto Fiori launchpad | Log onon to Fiori launchpad as Purchaser . | The SAP Fiori Launchpad displays. |  |
| 2. | Access the App | Open Manage Purchase Scheduling Agreements (F2179) . | The Manage Purchase Scheduling Agreements screen displays. |  |
| 3. | Find scheduling agreement number | Find the appropriate scheduling agreement through the search criteria, such as: Supplier: 33300001,Agreement Type: LPA (SA With Release doc.),Purchasing Organization: 3310, then choose Go, Select one item from the search result. | The desired scheduling agreement appears on the list page of Manage Purchase Scheduling Agreements. |  |
| 4. | Option 1:Release of schedule at scheduling agreement level | On the Manage Purchase Scheduling Agreements list page, select the schedule agreement and choose Release at the right upper corner.Select Release: Forecast and JIT Schedule. In the Release: Forecast and JIT Schedule dialog box, choose Release.OrSelect Forecast Schedule, in the Release: Forecast Schedule dialog box, choose Release.And select JIT Schedule, in the Release: JIT Schedule dialog box, choose Release.In the Release Result Log dialog box, choose Close. | Release of schedule shall be with green status. |  |
|  | Option 2:Release of schedules at item level | On the Manage Purchase Scheduling Agreements list page, navigate to the selected scheduling agreement by clicking on Cheveron (>) or by directly clicking on the Scheduling agreement number from the list page.Go to the Items tab, select the item, and then choose Release, it will show the option to release FRC and JIT schedules.Select Generate Forecast Schedule and choose Release. Choose OK.Select Generate JIT Schedule and choose Release.Choose OK. | The Scheduling agreement header object page appears in display mode.Success message display for the respective schedule released:Forecast schedule release generated against scheduling agreement.JIT delivery schedule created under scheduling agreement.The release document would be issued immediately to the supplier and releases status would be Transmitted. |  |

#### Check Scheduling Agreement Release Documentation

Purpose

The purpose of this activity is to view the release documentation after releasing the schedules for the respective scheduling agreement at scheduling agreement level and item level.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1. | Log on | Log onto the SAP Fiori launchpad as a Purchaser. | The SAP Fiori launchpad displays. |  |
| 2. | Access the App | Open Manage Purchase Scheduling Agreements (F2179). | The Manage Purchase Scheduling Agreements screen displays. |  |
| 3. | Find scheduling agreement number | Find the appropriate scheduling agreement through the search criteria, for example: Supplier: 33300001,Agreement Type: LPA (SA With Release doc.),Purchasing Organization: 3310, then choose Go, Select one item from the search result. | The desired scheduling agreement appears on the list page of Manage Purchase Scheduling Agreements. |  |
| 4. | Select Scheduling Agreement | Navigate to the selected scheduling agreement by clicking on Cheveron (>) or by directly clicking on the scheduling agreement number from the list page. | The Scheduling agreement header object page appears in display mode. |  |
| 5. | Quick View for Release Information | For the respective scheduling agreement navigate to Item Object page by clicking on the chevron (>) and go to the Release Documents tab. | Quick view shall open up with information related to Last & next Release date & time for FRC/JIT schedules |  |
| 6. | View Release documentation | For the respective scheduling agreement, navigate to Item Object page by clicking on the chevron (>) and go to the Release Documents tab. | It shall display the transmitted or non-transmitted status of the schedules. You can navigate to respective schedules to view the detailed information about the schedule lines released. |  |

#### Print Scheduling Agreement Releases

Purpose

The purpose of this activity is to view and print if needed the release documentation after releasing the schedules for the respective scheduling agreement at item level & scheduling agreement level.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1. | Log onto Fiori Launchpad | Log onto the Fiori Launchpad using the role Purchaser . | The SAP Fiori Launchpad displays. |  |
| 2. | Access the App | Open Manage Purchase Scheduling Agreements (F2179) . | The New Purchase Scheduling Agreement screen displays. |  |
| 3. | Find scheduling agreement number | Find the appropriate newly created scheduling agreement through the search criteria, such as: Supplier: 33300001,Agreement Type: LPA (SA With Release doc.)Purchasing Organization: 3310, then choose Go. Select one item from the search result. | The desired scheduling agreement appears on the list page of New Purchase Scheduling Agreement. |  |
| 4. | Select Scheduling Agreement | Navigate to the selected scheduling agreement by clicking on Cheveron (>) or by directly clicking on the Scheduling agreement number from the list page. | The Scheduling agreement header object page appears in display mode. |  |
| 5. | Select Scheduling Agreement Item | Go to the Items tab, choose the desired item for which delivery schedule has been released. | The Purchase Scheduling Agreement Item screen displays. |  |
| 6. | Display Message for Forecast dlv. Sched. | Go to the Release Documents section on the Purchase Scheduling Agreement Item screen and click the specific Release Number with Release Type (Forecast dlv. Sched.).Go to the OutputControls section on the Scheduling Agreement Release screen, select the specific message with channel PRINT, and then choose Display Document to view the PDF details. You can download this PDF and sent to supplier via Email. | The Scheduling agreement Release screen display.The Scheduling agreement release is opened in PDF format. |  |
| 7. | Display Message for JIT delivery schedule | Go to the Release Documents section on the Scheduling Agreement Item screen and click the specific Release Number with Release Type (JIT delivery schedule).Go to the Output Controls section on the Scheduling Agreement Release screen, select the specific message with channel PRINT, and then choose Display Document to view the PDF details. You can download this PDF and sent to supplier via Email. | The Scheduling agreement Release screen display.The Scheduling agreement release is opened in PDF format. |  |

#### Evaluate the Stock/Requirement Situation

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Prerequisite

Requirements planning has been carried out.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log onto SAP Fiori Launchpad | Log onto the SAP Fiori Launchpad as a Material Planner - External Procurement . | The SAP Fiori Launchpad displays. |  |
| 2 | Access the App | Open Monitor Material Coverage - Net / Individual Segments (F2101A) . | The Monitor Material Coverage screen displays. |  |
| 3 | Check Default Area of Responsibility | On the Monitor Material Coverage screen choose the user icon (on the top right corner), and then choose App Settings.In the MRP Settings dialog box, choose Area of Responsibility.On My Area of Responsibility screen, check if the below entry is assigned:Plant 1 AE 3310MRP Controller 001 (001)Choose AOR Status if the status for the above entry is not yet assigned.Choose AOR Status to unassign the rest of other entries. |  |  |
| 4 | Search for Material | On the Monitor Material Coverage screen, make the following entries and choose the Go button.Material: RM129 | The relevant material is shown. |  |
| 5 | Select Material | Select the checkbox before the materials no., and then choose Manage Materials. | The Materials screen and Material Details screen display. |  |
| 6 | Review Stock/Requirements List | Select the corresponding material on the left Material screen. | The detailed Stock/Requirements List for each material displays. |  |
| 7 | Open Quickview for MRP Element | On the Material Details screen, click the SchLne XXXX in column MRP Element. | The SchLne XXX you clicked will display on the pop-up. |  |
| 8 | Open Scheduling Agreement | On the Pop-up SchLne XXX screen, choose Open…, and then select Scheduling Agreement. | The Display Scheduling Agreement: Item Overview screen displays. |  |
| 9 | Display Delivery Schedule | Select the checkbox before the item no., and then choose More -> Delivery Schedule. | The Display Scheduling Agreement: Delivery Schedule for Item XXX screen displays.The system displays the scheduled quantity and dates. |  |

#### Post Goods Receipt

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Context

In this step, you post the goods receipt for the material against the scheduling agreement.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log onto Fiori Launchpad | Log onto the SAP Fiori launchpad as Warehouse Clerk . | The SAP Fiori Launchpad displays. |  |
| 2 | Access the App | Open Post Goods Receipt for Purchasing Document (F0843). | The Goods Receipt Purchase Order screen appears. |  |
| 3 | Enter Purchase Order | Enter the scheduling agreement number and choose Enter. | The system displays the data for the goods receipt on the Goods Receipt screen. |  |
| 4 | Enter Delivery Note | Make the following entries:Delivery Note: <note number>Printing: Choose Individual slip from the drop-down list.And choose Enter. |  |  |
| 5 | Select Item | Select the items for which a goods receipt is to be posted.Enter the delivered quantity and check storage location 331C to be posted. | The Post button is activated. |  |
| 6 | Post | Choose Post. | The system displays this message:1 document(s) created:Material Document5xxxxxxxxx 2xxx |  |

#### Create Supplier Invoice with Scheduling Agreement/GR Relation

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you create the supplier invoice.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log onto Fiori Launchpad | Open the SAP Fiori launchpad with the Accounts Payable Accountantrole. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Create Supplier Invoice (F0859) . | The Create Supplier Invoices screen displays. |  |
| 3 | Enter General Data | On the Create Supplier Invoice screen, make the following entries.Transaction: InvoiceCompany Code: 3310Gross Invoice Amount : XXXCurrency: AEDInvoice Date: TodayPosting Date: TodayInvoice Party: 33300001Reference: xxx(reference invoice number from invoicing party) | The Create Supplier Invoices screen displays. |  |
| 4 | Enter Purchase Order References | In Purchase Order References area, make the following entries (use a Scheduling agreement you created previously):References Document Category: Purchase Order/ Scheduling AgreementPurchase Order: xxx | The Purchase Order References screen displays. |  |
| 5 | Check the Invoice Items data | Check the Amount, the Quantity, the Tax Code (there may already be a tax code that was copied from the Scheduling Agreement). | The Purchase Order Item's table displays. |  |
| 6 | Check Tax code | In the section Tax check if there is tax code information and enter the tax amount.when the tax code value is greater than zero.If there is no tax, specify the tax code <Input Tax Code>. | In the Tax area, you should see the same tax codes as in the items. |  |
| 7 | Check the balance | Calculate the tax amount from the item amount multiplied by the tax value. Check the balance (difference between the calculated amount and the gross Amount you entered in step 3). | The balance should be zero (or within the defined tolerance). |  |
| 8 | Simulate Supplier Invoice and Check Messages | Choose Simulate.If there are no differences(or if the value is within the defined tolerance), a new screen Simulation appears. You can check the simulation results in Simulation Overview and Simulation Details area. | The supplier Invoice is complete to post. |  |
| 9 | Post Invoice | Choose Post. | The invoice is posted. The system displays the message Documents have been created. Supplier invoice: xxxxxxxxxx/xxxx Journal entries: xxxxxxxxxx/xxxx Do you want to create a new supplier invoice? |  |

### Scheduling Agreement w/o Release doc for Standard Procurement

#### Create Scheduling Agreement w/o Release doc - Standard

Purpose

This activity is used to create the scheduling agreement w/o release doc for the material/supplier combination, for example, material RM129 and supplier 33300001, if it has not been maintained yet. If the scheduling agreement is already present in the system you can skip this step.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log onto the SAP Fiori launchpad, as Purchaser. | SAP Fiori launchpad displays |  |
| 2 | Access App | Open Manage Purchase Scheduling Agreements (F2179). | The Manage Purchase Scheduling Agreements list page displays |  |
| 3 | Create Scheduling Agreement | Select Create to create a new scheduling agreement | The New Purchase Scheduling Agreement header view displays. |  |
| 4 | Enter Header Data | Create a new scheduling agreement with the following data:Supplier: 33300001Agreement type: LP (Scheduling Agreement)Validity Start: <today>Validity End: <MM/DD/YYYY>,for example,today + 720 daysPurchasing Organization: 3310Purchasing Group: 001In section Delivery and Payment:Target Value : 200000 AED |  |  |
| 5 | Add Items to Scheduling Agreement | From the New Purchase Scheduling Agreement view, choose the Items facets and select Create. | The Purchase Scheduling Agreement Item view displays. |  |
| 6 | Enter Item data | On the Items facets view, make the following entries:Plant: 3310Material: RM129Target Quantity: 10000Net Order Price: Defaulted from Info recordTax Code: <Input Tax Code> (Default Value from Info Record)Tax Date: Default TodayChoose Apply at the bottom of the view. |  |  |
| 7 | Save | Return to the New Purchase Scheduling Agreement header view and choose Create at the bottom of the view.Make a note of the schedule agreement number. | A schedule agreement is created. |  |

#### Approve Scheduling Agreement (Optional)

Purpose

In this procedure, you release a Scheduling Agreement. If the document type of scheduling agreement is LP and the purchase group is 001, then the scheduling agreement should be triggered the approval process.

Prerequisite

A Scheduling Agreement must exist for release.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Open the SAP Fiori Launchpad with the Purchasing Manager role. | The SAP Fiori Launchpad is displayed. |  |
| 2 | Open Approve Scheduling Agreement | Open My Inbox - All Items (F0862) . | A list of already created Scheduling Agreement s is displayed. |  |
| 3 | Search for Scheduling Agreement Status | Enter the Scheduling Agreement number in the search area, then choose the Search button. | The Scheduling Agreement s without follow-on documents (w/o status Follow-On Documents) have the status In Approval. |  |
| 4. | Release Scheduling Agreement | Select the Scheduling Agreement in left of the screen and choose Release in bottom right. | The Submit Decision screen displays. |  |
| 4 | Enter Release Reason | Enter the approval reason if needed, then choose Submit. | The Scheduling Agreement is approved. |  |
| 5 | Back to SAP Fiori Launchpad | Choose the Home button to go back to the SAP Fiori launchpad. | The SAP Fiori launchpad is displayed. |  |

#### Maintain Delivery Schedule

Purpose

The purpose of this activity is to create the delivery schedule for the scheduling agreement if it has not been maintained while creating the scheduling agreement.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1. | Log onto Fiori launchpad | Log onto the Fiori launchpad using the role Purchaser . | The SAP Fiori Launchpad displays. |  |
| 2. | Access the App | Open Manage Purchase Scheduling Agreements (F2179) . | The Manage Scheduling Agreements screen displays. |  |
| 3. | Find scheduling agreement number | Find the appropriate newly created scheduling agreement through the search criteria, such as: Supplier: 33300001,Agreement Type: LP,Purchasing Organization: 3310, then choose Go. Select one item from the search result. | The desired scheduling agreement appears on the list page of Manage Scheduling Agreements. |  |
| 4. | Select Scheduling Agreement | Navigate to the selected scheduling agreement by clicking on Cheveron (>) or by directly clicking on the Scheduling agreement number from the list page. | The Scheduling agreement header object page appears in display mode. |  |
| 5. | Maintain Delivery Schedule | 1. Click on the Edit at the right upper corner on the Manage Scheduling Agreement Header Object page.2. In Items tab, click on the desired item for which delivery schedule needs to be maintained. | The Scheduling Agreement Item screen displays. |  |
| 6. | Maintain Delivery Schedule | Go to the Schedule Lines section on the Scheduling Agreement Item screen and choose Create. You will get into the Scheduling agreement Item Schedule Line screen to maintain the schedules for the item, make following entries:Date type: <Day format>Delivery Date: Today's dateDelivery Time: 10:00:00Schedule Quantity: 10Choose Apply twice at the right bottom to add a schedule line. | You will be navigated back to Scheduling Agreement Header object page. |  |
| 7. | Save | Choose Save from the Scheduling Agreement Header object page. | Scheduling agreement will get updated with schedule lines. |  |

#### Print Scheduling Agreement

Purpose

The purpose of this activity is to print view the scheduling agreement for the material/vendor combination for the new Scheduling agreement or for the one which is already present in the system

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1. | Log onto Fiori launchpad | Log onto the Fiori launchpad as Purchaser . | The SAP Fiori Launchpad displays. |  |
| 2. | Access the App | Open Manage Purchase Scheduling Agreements (F2179) . | The Manage Purchase Scheduling Agreements screen displays. |  |
| 3. | Find scheduling agreement number | Find the appropriate scheduling agreement through the search criteria, such as: Supplier:33300001,Agreement Type: LP,Purchasing Organization: 3310, then choose Go. Select one item from the search result. | The desired scheduling agreement appears on the list page of Manage Purchase Scheduling Agreements. |  |
| 4. | Select Scheduling Agreement | Navigate to the selected scheduling agreement by clicking on Cheveron (>) or by directly clicking on the Scheduling agreement number from the list page. | The Scheduling agreement header object page appears in display mode. |  |
| 5. | View the output form for scheduling agreement | Go to the Output Control tab and view the output settings maintained for the scheduling agreement. Click on the PDF sign to view the output form of scheduling agreement. | PDF form for scheduling agreement shall open. |  |

#### Evaluate the Stock/Requirement Situation

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Prerequisite

Requirements planning has been carried out.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log onto SAP Fiori Launchpad | Log onto the SAP Fiori Launchpad as a Material Planner - External Procurement . | The SAP Fiori Launchpad displays. |  |
| 2 | Access the App | Open Monitor Material Coverage - Net / Individual Segments (F2101A) . | The Monitor Material Coverage screen displays. |  |
| 3 | Check Default Area of Responsibility | On the Monitor Material Coverage screen choose the user (on the top right corner), and then choose App Settings.In the MRP Settings dialog box, choose Area of Responsibility.On My Area of Responsibility screen, check if this entry is displayed there: Plant 1 AE | If there is no entry Plant 1 AE in the Area of Responsibility screen, choose Add to select it and then choose OK. For other plant entries in the Area of Responsibility screen, choose Delete to remove the others and then choose OK. |  |
| 4 | Search for Material | On the Monitor Material Coverage - Net and Individual Segments screen, make the following entries and choose the Go button.Material: RM129 | The relevant material is shown. |  |
| 5 | Select Material | Select the checkbox before the materials no., and then choose Manage Materials. | The Materials screen and Material Details screen display. |  |
| 6 | Review Stock/Requirements List | Select the corresponding material on the left Material screen. | The detailed Stock/Requirements List for each material displays. |  |
| 7 | Open Quickview for MRP Element | On the Material Details screen, click the SchLne XXXX in column MRP Element. | The SchLne XXX you clicked will display on the pop-up. |  |
| 8 | Open Scheduling Agreement | On the Pop-up SchLne XXX screen, choose Open…, and then select Scheduling Agreement. | The Display Scheduling Agreement: Item Overview screen displays. |  |
| 9 | Display Delivery Schedule | Mark the checkbox before the item no., and then choose More -> Delivery Schedule. | The Display Scheduling Agreement: Delivery Schedule for Item XXX screen displays.The system displays the scheduled quantity and dates. |  |

#### Post Goods Receipt

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Context

In this step, you post the goods receipt for the material against the scheduling agreement.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log onto Fiori Launchpad | Log onto the SAP Fiori launchpad as Warehouse Clerk . | The SAP Fiori Launchpad displays. |  |
| 2 | Access the App | Open Post Goods Receipt for Purchasing Document (F0843). | The Goods Receipt for Purchasing Document screen appears. |  |
| 3 | Enter Purchasing Document | Enter the scheduling agreement number and choose Enter. | The system displays the data for the goods receipt on the Goods Receipt screen. |  |
| 4 | Enter Delivery Note | Make the following entries:Delivery Note: <note number>Printing: Choose Individual slip from the drop-down list.And choose Enter. |  |  |
| 5 | Select Item | Select the items for which a goods receipt is to be posted.Enter the delivered quantity and check storage location to be posted. | The Post button is activated. |  |
| 6 | Post | Choose Post. | The system is displayed the message 1 material document(s) posted: 5xxxxxxxxx 2xxx. |  |

#### Create Supplier Invoice with Scheduling Agreement/GR Relation

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you create the supplier invoice.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log onto Fiori Launchpad | Open the SAP Fiori launchpad with the Accounts Payable Accountantrole. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Create Supplier Invoice (F0859) . | The Create Supplier Invoices screen displays. |  |
| 3 | Enter General Data | On the Create Supplier Invoice screen, make the following entries.Transaction: InvoiceCompany Code: 3310Gross Invoice Amount : XXXCurrency: AEDInvoice Date: TodayPosting Date: TodayInvoice Party: 33300001Reference: xxx(reference invoice number from invoicing party) | The Create Supplier Invoices screen displays. |  |
| 4 | Enter Purchase Order References | In Purchasing Document References area, make the following entries (use a Scheduling agreement you created previously):Reference Document Category: Purchase Order/ Scheduling AgreementPurchase Order/Scheduling Agreement: xxx | The Purchase Document References screen displays. |  |
| 5 | Check the Invoice Items data | Check the Amount, the Quantity, the Tax Code (there may already be a tax code that was copied from the Scheduling Agreement). | The Purchase Order Item's table displays. |  |
| 6 | Check Tax code | In the section Tax check if there is tax code information and enter the tax amount.when the tax code value is greater than zero.If there is no tax, specify the tax code for zero tax. | In the Tax area, you should see the same tax codes as in the items. |  |
| 7 | Check the balance | Calculate the tax amount from the item amount multiplied by the tax value. Check the balance (difference between the calculated amount and the gross Amount you entered in step 3). | The balance should be zero (or within the defined tolerance). |  |
| 8 | Simulate Supplier Invoice and Check Messages | Choose Simulate.If there are no differences(or if the value is within the defined tolerance), a new screen Simulation appears. You can check the simulation results in Simulation Overview and Simulation Details area. | The supplier Invoice is complete to post. |  |
| 9 | Post Invoice | Choose Post. | The invoice is posted. The system displays the message Documents have been created. Supplier invoice: xxxxxxxxxx/xxxx Journal entries: xxxxxxxxxx/xxxx Do you want to create a new supplier invoice? |  |

### Integration of Scheduling Agreement Procurement with External Suppliers

|  |
| --- |
| Note If the configuration in sections Cloud-to-Cloud Integration under Setting Up Scheduling Agreements in Procurement (BMR) has been done, the EDI integration from purchasing scheduling agreement’s perspective can be executed. |

#### Create Scheduling Agreement with Release Doc - Standard

Purpose

This activity is used to create the scheduling agreement w/ release doc for the material/supplier combination, for example, material RM129 and supplier 33300001, if it has not been maintained yet. If the scheduling agreement is already present in the system you can skip this step.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log onto the SAP Fiori launchpad, as Purchaser. | SAP Fiori launchpad displays |  |
| 2 | Access App | Open Manage Purchase Scheduling Agreements (F2179). | The Manage Purchase Scheduling Agreements list page displays Log onto the SAP Fiori launchpad. |  |
| 3 | Create Scheduling Agreement | Select Create to create a new scheduling agreement | The Manage Purchase Scheduling Agreements header view displays. |  |
| 4 | Enter Header Data | Create a new scheduling agreement with the following data:Supplier: 33300001Agreement type: LPA (SA With Release doc.)Valid End: MM/DD/YYYYPurchasing Organization: 3310Purchasing Group: 001 |  |  |
| 5 | Enter Payement Terms Data | On the Payement Terms facets view, make the following entries:Target Value: 200000 AED |  |  |
| 6 | Add Items to Scheduling Agreement | Choose the Items facets and select Create. | The Purchase Scheduling Agreement Item view displays. |  |
| 7 | Enter Item data | On the Purchase Scheduling Agreement Item facets view, make the following entries:Plant: 3310Material: RM129Target Quantity: 120000Confirmation Control: 0004Net Order Price: Defaulted from Info recordNote Please make sure the purchasing price is the same as the sales price in sales scheduling agreement from supplier system.Tax Code: <Input Tax Code>Tax Date: Default TodayNote Field Tax Date is only available for the countries/regions that Time-Dependent Taxes (TDT) is enabled.In the Output Control area, make the following entry:Creation Profile: S003Choose Apply at the bottom of the view. |  |  |
| 8 | Save | Return to the New Purchase Scheduling Agreement header view and choose Create at the bottom of the view.Make a note of the schedule agreement number. | A schedule agreement is created. |  |

#### Maintain Delivery Schedule

Purpose

The purpose of this activity is to create the delivery schedule for the scheduling agreement if it has not been maintained while creating the scheduling agreement.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1. | Log onto Fiori launchpad | Log onto the Fiori launchpad using the role Purchaser . | The SAP Fiori Launchpad displays. |  |
| 2. | Access the App | Open Manage Purchase Scheduling Agreements (F2179) . | The Manage Scheduling Agreements screen displays. |  |
| 3. | Find scheduling agreement number | Find the appropriate newly created scheduling agreement through the search criteria, such as: Supplier: 33300001,Agreement Type: LPA (SA With Release doc.),Purchasing Organization: 3310, then choose Go. Select one item from the search result. | The desired scheduling agreement appears on the list page of Manage Scheduling Agreements. |  |
| 4. | Select Scheduling Agreement | Navigate to the selected scheduling agreement by clicking on Cheveron (>) or by directly clicking on the Scheduling agreement number from the list page. | The Scheduling agreement header object page appears in display mode. |  |
| 5. | Maintain Delivery Schedule | 1. Click on the Edit at the right upper corner on the Manage Scheduling Agreement Header Object page.2. In Items tab, click on the desired item for which delivery schedule needs to be maintained. | The Scheduling Agreement Item screen displays. |  |
| 6. | Maintain Delivery Schedule | Go to the Schedule Lines section on the Purchase Scheduling Agreement Item screen and choose Create. You will get into the Manage Purchase Scheduling Agreements screen to maintain the schedules for the item, make following entries:Date type: <Day format>Delivery Date: Today's dateDelivery Time: 10:00:00Schedule Quantity: 10Choose Apply twice at the right bottom to add a schedule line. | You will be navigated back to Scheduling Agreement Header object page. |  |
| 7. | Save | Choose Save from the Scheduling Agreement Header object page. | Scheduling agreement will get updated with schedule lines. |  |

#### Print Scheduling Agreement

Purpose

The purpose of this activity is to print view the scheduling agreement for the material/supplier combination for the new Scheduling agreement or for the one which is already present in the system

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1. | Log onto Fiori launchpad | Log onto the Fiori launchpad as Purchaser . | The SAP Fiori Launchpad displays. |  |
| 2. | Access the App | Open Manage Purchase Scheduling Agreements (F2179) . | The Manage Purchase Scheduling Agreements screen displays. |  |
| 3. | Find scheduling agreement number | Find the appropriate scheduling agreement through the search criteria, such as: Supplier: 33300001,Agreement Type: LPA (SA With Release doc.),Purchasing Organization: 3310, then choose Go. Select one item from the search result. | The desired scheduling agreement appears on the list page of Manage Purchase Scheduling Agreements. |  |
| 4. | Select Scheduling Agreement | Navigate to the selected scheduling agreement by clicking on Cheveron (>) or by directly clicking on the Scheduling agreement number from the list page. | The Scheduling agreement header object page appears in display mode. |  |
| 5. | View the output form for scheduling agreement | Go to the Output controls tab and view the output settings maintained for the scheduling agreement. Click on the PDF sign to view the output form of scheduling agreement. | PDF form for scheduling agreement shall open. |  |

#### Release Scheduling Agreement

Purpose

The purpose of this activity is to release the schedules for the respective scheduling agreement at scheduling agreement level or item level.

You can choose release scheduling agreement either at scheduling agreement level or item level.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1. | Log onto Fiori launchpad | Log onon to Fiori launchpad as Purchaser . | The SAP Fiori Launchpad displays. |  |
| 2. | Access the App | Open Manage Purchase Scheduling Agreements (F2179) . | The Manage Purchase Scheduling Agreements screen displays. |  |
| 3. | Find scheduling agreement number | Find the appropriate scheduling agreement through the search criteria, such as: Supplier: 33300001, Agreement Type: LPA (SA With Release doc.), Purchasing Organization: 3310, then choose Go, Select one item from the search result. | The desired scheduling agreement appears on the list page of Manage Purchase Scheduling Agreements. |  |
| 4. | Option 1:Release of schedule at scheduling agreement level | On the Manage Purchase Scheduling Agreements list page, select the schedule agreement and choose Release at the right upper corner.Select Forecast and JIT Schedule. In the Release: Forecast and JIT Schedule dialog box, choose Release.OrSelect Forecast Schedule, in the Release: Forecast Schedule dialog box, choose Release.And select JIT Schedule, in the Release: JIT Schedule dialog box, choose Release.Note If releasing Forecast and JIT separately, please release FRC firstly and then release JIT for the initial release.In the Release Result Log dialog box, choose Close. | Release of schedule shall be with green status. |  |
|  | Option 2:Release of schedules at item level | On the Manage Purchase Scheduling Agreements list page, navigate to the selected scheduling agreement by clicking on Cheveron (>) or by directly clicking on the Scheduling agreement number from the list page.Go to the Items tab, select the item, and then choose Release, it will show the option to release FRC and JIT schedules.Select Release: Forecast and JIT Schedule and choose Release. Choose OK.Choose OK.Note Please release FRC firstly, and then release JIT for the initial release. | The Scheduling agreement header object page appears in display mode.Success message display for the respective schedule released:Forecast schedule release generated against scheduling agreement.JIT delivery schedule created under scheduling agreement.The release document would be issued immediately to the supplier and releases status would be Transmitted. |  |

#### Check Scheduling Agreement Releases

Purpose

The purpose of this activity is to view the release documentation after releasing the schedules for the respective scheduling agreement.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1. | Log onto Fiori launchpad | Log onto the Fiori launchpad as Purchaser . | The SAP Fiori Launchpad displays. |  |
| 2. | Access the App | Open Manage Purchase Scheduling Agreements (F2179) . | The Manage Purchase Scheduling Agreements screen displays. |  |
| 3. | Find scheduling agreement number | Find the appropriate scheduling agreement through the search criteria, such as: Supplier: 33300001,Agreement Type: LPA (SA With Release doc.),Purchasing Organization: 3310, then choose Go, Select one item from the search result. | The desired scheduling agreement appears on the list page of Manage Purchase Scheduling Agreements. |  |
| 4. | Select Scheduling Agreement | Navigate to the selected scheduling agreement by clicking on Cheveron (>) or by directly clicking on the Scheduling agreement number from the list page. | The Scheduling agreement header object page appears in display mode. |  |
| 5. | Select Scheduling Agreement Item | Go to the Items tab, choose the desired item for which delivery schedule has been released. | The Purchase Scheduling Agreement Item screen displays. |  |
| 6. | Display Message for Forecast dlv. Sched. | Go to the Release Documents section on the Scheduling Agreement Item screen and click the specific Release Number with Release Type (Forecast dlv. Sched.).Go to the Output Controls section on the Scheduling Agreement Release screen, you can see the output details for EDI of Forecast Delvery Schedule. | The Scheduling agreement Release screen display. |  |
| 7. | Display Message for JIT delivery schedule | Go to the Release Documents section on the Scheduling Agreement Item screen and click the specific Release Number with Release Type (JIT delivery schedule).Go to the Output Controls section on the Scheduling Agreement Release screen, you can see the output details for EDI of JIT Delivery Schedule. | The Scheduling agreement Release screen display. |  |

#### Send Forcast & JIT Delivery Schedule – EDI relevant

Purpose

Forecast & JIT delivery schedule is automatically sent to the Supplier system.

Prerequisites

Procurement scheduling agreement must have been released, forecast and JIT delivery schedule are genereated in the SAP S/4HANA Cloud Public Edition system (buyer side).

This step is only relevant to EDI relevant delivery schedules.

Procedure

This step is automatically generated.

#### Check Forecast and JIT Delivery Schedule in AIF (Message Dashboard)

Purpose

The forecast and JIT delivery schedule are sent via EDI to the supplier. They are automatically processed if no error occurs. This step can check the message status.

Prerequisites

The procurement scheduling agreement release has been created, forecast and JIT delivery schedule are generated already.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1. | Log onto Fiori launchpad | Log onto the Fiori launchpad as Configuration Expert - Business Network Integration. | The SAP Fiori Launchpad displays. |  |
| 2. | Open Message Dashboard | Open the Message Dashboard tile. |  |  |
| 3. | Choose Date and Namespace/Interface | On the Interface Monitor screen, choose correct time period entries and choose Search.In the Result List, choose the line of /MMSAR and choose All Messages. |  |  |
| 4. | Check detail messages | On the Monitoring and Error Handling screen, Expend the messages in the left side of the screen for outbound scheduling agreement release processing, and choose the corresponding item.Double click the message to see the detal information on the right side of the screen. |  |  |
| 5. | Reprocess messages | Choose Reprocess if needed. |  |  |

#### Check Incoming Inbound Delivery in AIF (Message Dashboard)

Purpose

The outbound delivery has been created, picking has been executed and goods issue has been posted in the SAP S/4HANA Cloud Public Edition system (supplier side). The advanced shipping notification is sent via EDI to the buyer. They are automatically processed if no error occurs. This step can check the message status.

Prerequisites

The outbound delivery has been created and goods issue has been posted from Supplier System.

This step is only relevant to EDI relevant inbound delivery.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1. | Log onto Fiori launchpad | Log onto the Fiori launchpad as Configuration Expert - Business Network Integration. | The SAP Fiori Launchpad displays. |  |
| 2. | Access the App | Open Message Dashboard. |  |  |
| 3. | Choose Date and Namespace/Interface | On the Interface Monitor screen, choose correct time period entries and choose Search.In the Result List, choose the line of /LEEDI and choose All Messages. |  |  |
| 4. | Check detail messages | On the Monitoring and Error Handling screen, Expend the messages in the left side of the screen for outbound scheduling agreement release processing, and choose the corresponding item.Double click the message to see the detal information on the right side of the screen. | Inbound ldelivery 018xxxxxxx createdInbound delivery crea-tion is successful |  |
| 5. | Reprocess messages | Choose Reprocess if needed. |  |  |

#### Review Inbound Delivery Document in Scheduling Agreement Document

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this procedure, you can review the inbound delivery.

|  |
| --- |
| Note The following test steps can be processed ONLY after the corresponding supplier system has sent a shipping notification. |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log onto SAP Fiori Launchpad | Log onto the SAP Fiori Launchpad as a Purchaser . | The SAP Fiori Launchpad displays. |  |
| 2 | Access the App | Open Display Scheduling Agreement (ME33L) .Note If this app is not displayed in the screen, you can click the user icon and then choose the Edit Home Page to add this app accordingly. | The The Display Scheduling Agreement: Initial screen displays. |  |
| 3 | Find scheduling agreement number | Enter the number of the Scheduling Agreement. Or you can search your inbound delivery using input help, such as, in the navigation menu "..." select Purchasing Documents per Supplier tab, enter the following data and choose Find,:such as: Supplier33300001, Agreement TypeLPA (SA With Release doc.), Purchasing Organization3310. Select one item from the search result, choose Copy. | The desired scheduling agreement appears on screen. |  |
| 4 | Display Scheduling Agreement | Choose Overview. | The Display Schedul-ing Agreement: Item Overview displays. |  |
| 5 | View Inbound delivery documentation | Select the desired item, choose More > Item > Confirmations > OverviewWhen the external confirmation from your supplier has been sent, you should see an additional line in the table showing following information:CC (Confirm. Cat.): LADelivery Date: xQuantity: xReference: 8xxxxxxxDelivery: 18xxxxxxx | The Display Scheduling Agreement: Item XXXXX displays. |  |

#### Post Goods Receipt for Inbound Delivery

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you post the goods receipt for the material against the inbound delivery of scheduling agreement.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log onto Fiori Launchpad | Log onto the SAP Fiori launchpad as Receiving Specialist. | The SAP Fiori Launchpad displays. |  |
| 2 | Access the App | Open Change Inbound Delivery (VL32N). | The Change Inbound Delivery screen appears. |  |
| 3 | Enter detail data | On the initial screen, enter the following values then choose Continue:Inbound Delivery Number: Select your inbound delivery using in-put help, such as, in the navigation menu "..." select Inbound Delivery: Not Posted for GR, then enter following data and choose Find,: Supplier33300001,,Delivery Date : Today's date. Select one item from the search result, choose Copy. | The Inbound Delivery xxxxxxxxx Change: Overview screen displays. |  |
| 4 | Confirm Quan-tities for Putaway | In Item Overview tab, input Putaway Qty:xxx,SLoc: 101CNote The putaway quantity should equal to the delivery quantityAnd choose Save. | Back to the Change Inbound Delivery screen and Inbound Delivery xxxxxxxxx has been saved message displays. |  |
| 5 | Post Goods Receipt | Choose Post Goods Receipt. | The system message Goods receipt for inbound delivery xxxxxxxxx posted (material Document 500xxxxxxx) appears. The material is posted to the unrestricted use stock with storage location 101C and plant Plant1DE. You can display the stock overview in APP Display Stock Overview. |  |

#### Check Incoming Invoice in AIF (Message Dashboard)

Purpose

The billing document has been created from supplier system and send via EDI to the buyer. They are automatically processed if no error occurs. This step can check the message status.

Prerequisites

The biliing document has been created from supplier system.

This step is only relevant to EDI relevant invoice.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1. | Log onto Fiori launchpad | Log onto the Fiori launchpad as Configuration Expert - Business Network Integration. | The SAP Fiori Launchpad displays. |  |
| 2. | Open Message Dashboard | Open the Message Dashboard tile. |  |  |
| 3. | Choose Date and Namespace/Interface | On the Interface Monitor screen, choose correct time period entries and choose Search.In the Result List, choose the line of /MMEDI and choose All Messages. |  |  |
| 4. | Check detail messages | On the Monitoring and Error Handling screen, expend the messages in the left side of the screen, and choose the corresponding invoice number in Buyer systemDouble click the message to see the detal information on the right side of the screen. |  |  |
| 5. | Reprocess messages | Choose Reprocess if needed. |  |  |

#### Review Supplier Invoice

Purpose

In this procedure, a supplier invoice is displayed.

The following test steps can be processed ONLY after the corresponding supplier system has sent an invoice.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1. | Log onto Fiori launchpad | Open the SAP Fiori launchpad with the Accounts Payable Accountant role. | The SAP Fiori Launchpad displays. |  |
| 2. | Access the App | Open Supplier Invoices List (F1060A) . | The Supplier Invoices List screen displays. |  |
| 3. | Search for Supplier Invoice | On the Supplier Invoice List, search for your invoice through the search criteria, such as: Invoice Party 33300001, Reference9xxxxxxx (Invoice no. in supplier system) and display it. |  |  |

## Appendix

### Process Integration

The process to be tested in this test script is part of a chain of integrated processes.

#### Succeeding Processes

After completing the activities in this test script, you can continue testing the following business processes:

| Process | Business Condition |
| --- | --- |
| Fiori Overview Pages for Procurement (1JI) | The Procurement Overview Page gives the Purchaser the most important and relevant information at a glance – instead of navigating through many different transactions and reports.The Global Filter helps the Purchaser to focus the entire Procurement Overview Page to view all information according to specific suppliers, material groups, purchasing groups and more.Via contextual navigation the Purchaser can immediately act upon the displayed information by accessing the app or the object instance or get more detailed information in the corresponding KPI Drill-Downs. |

### Relevant Features

Here are listed some important application functionalities related to Scheduling Agreement, which are not covered in the above test procedures.

| Function Area | Function | Detailed Information | Comment |
| --- | --- | --- | --- |
| Purchase Scheduling Agreement | Header/Item notes | Create notes for purchase scheduling agreement document to maintain various details about the document | Header notes are supported to be copied from RFQ/Quotation and Scheduling AgreementItem Notes are supported to be copied from Scheduling Agreement, RFQ/Quotation, Purchase Requisition and Info record |
| Purchase Scheduling Agreement | Output details for scheduling agreements | Output Type/Channel/Form Template/Email Template for Scheduling Agreement (LP) | SCHEDG_AGRMT_INCL_SCHEDULESPRINT/EMAIL/IDOCMM_PUR_SCHD_AGRMT_INCL_SCHEDMM_PUR_SCHD_AGRMT_DEF_TEMPLATE |
| Purchase Scheduling Agreement | Output details for scheduling agreements | Output Type/Channel/Form Template/Email Template for Header of SA With Release doc. (LPA) | SCHEDULING_AGREEMENTPRINT/EMAIL/IDOCMM_PUR_SCHD_AGRMTMM_PUR_SCHD_AGRMT_DEF_TEMPLATE |
| Purchase Scheduling Agreement | Output details for scheduling agreements | Output Type/Channel/Form Template/Email Template for Itemof SA With Release doc. (LPA) | SCHEDULING_AGREEMENT_RELPRINT/EDIMM_PUR_SCHD_AGRMT_REL- |
| Purchase Scheduling Agreement | Add attachments |  | Attachment can be uploaded in the header of purchase scheduling agreement, which will also be shown under the Attachments tabs of purchase scheduling agreement in My Inbox app. |
| Purchase Scheduling Agreement | Enable the Kanban process for purchase scheduling agreement items | At the item level, under the GR/IR Control facet,Kanban Indicator: Scheduling Agreement for Summarized JIT Call | Kanban is a means of signaling the demand status for a certain material. The replenishment or production of a material is not triggered until a certain production level needs the material. The signal for replenishment is issued by an indicator, that is sent by a demand source (consumer) to the supply source (supplier).This functionality is used in test script 1E3. |
| Purchase Scheduling Agreement | Save in Preparation option | Create and save scheduling agreements as a draft using the Save in Preparation option. | The Save in Preparation option is only enabled before a purchase scheduling agreement has been approved and released. |
| Purchase Scheduling Agreement | Withdraw a purchase scheduling agreement from approval | Select the purchase scheduling agreement and choose Withdraw from Approval. | This cancels the approval process for a specific purchase scheduling agreement. You can then make the required changes to the purchase scheduling agreement and submit it again for approval. |
| Purchase Scheduling Agreement | Manage Workflows for Scheduling Agreements | [https://help.sap.com/viewer/0e602d466b99490187fcbb30d1dc897c/latest/en-US/d8967a572d71434bb787fb8ab63aad3b.html](https://help.sap.com/viewer/0e602d466b99490187fcbb30d1dc897c/latest/en-US/d8967a572d71434bb787fb8ab63aad3b.html) |  |
| Purchase Scheduling Agreement | How to Configure the Flexible Workflow for Scheduling Agreements | [https://help.sap.com/viewer/0e602d466b99490187fcbb30d1dc897c/latest/en-US/147ccd5b266042e1896bbb3b34ef2569.html](https://help.sap.com/viewer/0e602d466b99490187fcbb30d1dc897c/latest/en-US/147ccd5b266042e1896bbb3b34ef2569.html) |  |
| Purchase Scheduling Agreement | Purchase Scheduling Agreement related apps | WebGUI: Display Scheduling Agreement (ME33L )WebGUI: Price Change Scheduling Agreements (MEKL )WebGUI: Create Transport Scheduling Agreement (ME37)WebGUI: Monitor Receipt of Order Acknowledgment (ME92L) |  |

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
> Flagged while digesting this document, not verified: The EDI goods receipt step posts to storage location 101C and Plant1DE, while the rest of the script uses plant 3310 (Plant 1 AE) and storage location 331C.

## Connections
- part-of :: [[_cluster]]
- related-to :: [[10-procurement/master-data-script-create-scheduling-agreement-mds-bf6-557]]
- related-to :: [[10-procurement/mds-bf6-559]]
- related-to :: [[10-procurement/mds-bf6-561]]
- related-to :: [[10-procurement/script-de-dados-mestre-criar-programa-de-remessas-mds-bf6-560]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/BMR_S4CLD2608_BPD_EN_AE.docx` — full document · extracted with `mammoth` · 114,027 chars in the whole document
