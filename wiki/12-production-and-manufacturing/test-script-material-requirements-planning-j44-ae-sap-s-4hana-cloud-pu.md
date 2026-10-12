---
id: 12-production-and-manufacturing/test-script-material-requirements-planning-j44-ae-sap-s-4hana-cloud-pu
title: "Test Script: Material Requirements Planning (J44_AE) - SAP S/4HANA Cloud Public Edition (J44_S4CLD2608_BPD_EN_AE)"
description: "Step-by-step Fiori test script for scope item J44_AE (MRP, UAE plant 3310): PIRs, MRP run, safety stock/days of supply, material exceptions, MRP change requests"
cluster: 12-production-and-manufacturing
tags: [kb/production-and-manufacturing, topic/mrp-and-predictive-mrp]
aliases: [J44_S4CLD2608_BPD_EN_AE]
keywords: [Material Requirements Planning and Predictive MRP, material requirements planning, mrp run, planned independent requirements, purchase requisitions, scheduling agreements, material coverage, time-dependent safety stock, days of supply, material exceptions]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/J44_S4CLD2608_BPD_EN_AE.docx]
confidence: low
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-1300
topic: 12-production-and-manufacturing/mrp-and-predictive-mrp
language: EN
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Test Script: Material Requirements Planning (J44_AE) - SAP S/4HANA Cloud Public Edition (J44_S4CLD2608_BPD_EN_AE)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/J44_S4CLD2608_BPD_EN_AE.docx`, extracted with `mammoth`. Grouped under **Material Requirements Planning and Predictive MRP** in Production and Manufacturing. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

| <!-- image omitted: unnamed --> | Test ScriptSAP S/4HANA Cloud Public Edition - 19-06-26 |
| --- | --- |
|  | Material Requirements Planning (J44_AE) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Table of Contents

[1 Purpose 3](#_Toc232862851)

[2 Prerequisites 4](#_Toc232862852)

[2.1 System Access 4](#_Toc232862853)

[2.2 Roles 4](#_Toc232862854)

[2.3 Master Data, Organizational Data, and Other Data 5](#_Toc232862855)

[2.4 Business Conditions 6](#_Toc232862856)

[2.5 Preliminary Steps 6](#_Toc232862857)

[2.5.1 Create Scheduling Agreement 6](#_Toc232862858)

[2.5.2 Prerequisite for Material Exception (Optional) 8](#_Toc232862859)

[2.5.2.1 Manage Teams and Responsibilities 8](#_Toc232862860)

[2.5.2.2 Manage Situation Types 10](#_Toc232862861)

[2.5.3 Prerequisite for Handover of Purchase Requisition (Optional) 11](#_Toc232862862)

[2.5.3.1 Assign MRP Group 0011 to TG0011 11](#_Toc232862863)

[2.5.4 Prerequisite for MRP Change Request (Optional) 12](#_Toc232862864)

[2.5.4.1 Assign Business User 12](#_Toc232862865)

[2.5.4.2 Create Purchasing Info Record 13](#_Toc232862866)

[2.5.4.3 Clear PIRs for Material TG0099 15](#_Toc232862867)

[2.5.4.4 Clear Purchase Requestions & Purchase Orders for Material TG0099 17](#_Toc232862868)

[3 Overview Table 18](#_Toc232862869)

[4 Test Procedure 21](#_Toc232862870)

[4.1 Manage PIRs for Material **TG0011** & **TG0012** 21](#_Toc232862871)

[4.2 Monitor Material Coverage 22](#_Toc232862872)

[4.2.1 Run Material Requirements Planning (MRP) 22](#_Toc232862873)

[4.2.2 Evaluate MRP Result 23](#_Toc232862874)

[4.2.2.1 Evaluate MRP Result (Purchase Requisitions) 23](#_Toc232862875)

[4.2.2.2 Evaluate MRP Result (Delivery Schedule) 26](#_Toc232862876)

[4.3 Display MRP Run Master Data Issues 28](#_Toc232862877)

[4.4 Display MRP Run Key Figures 29](#_Toc232862878)

[4.5 Time-Dependent Safety Stock Levels 30](#_Toc232862879)

[4.5.1 Time-Dependent Safety Stock 30](#_Toc232862880)

[4.5.1.1 Maintain MRP Safety Stock Method in Material 30](#_Toc232862881)

[4.5.1.2 Maintain Time-Dependent Safety Stock 31](#_Toc232862882)

[4.5.1.3 Manage Material Coverage 32](#_Toc232862883)

[4.5.2 Time-Dependent Days of Supply 33](#_Toc232862884)

[4.5.2.1 Maintain MRP Safety Stock Method in Material 33](#_Toc232862885)

[4.5.2.2 Maintain Time-Dependent Days of Supply 34](#_Toc232862886)

[4.5.2.3 Manage PIRs for Material TG0099 35](#_Toc232862887)

[4.5.2.4 Manage Material Coverage 37](#_Toc232862888)

[4.5.2.5 Reset Material Master Data 38](#_Toc232862889)

[4.6 Material Exception (Optional) 39](#_Toc232862890)

[4.6.1 Clear Initial Stock 39](#_Toc232862891)

[4.6.2 Clear Existing Purchase Requisitions 40](#_Toc232862892)

[4.6.3 Manage PIRs for Material TG0099 41](#_Toc232862893)

[4.6.4 Run Material Requirements Planning (MRP) and Firm Purchase Requisition 42](#_Toc232862894)

[4.6.5 Increase Stock for TG0099 43](#_Toc232862895)

[4.6.6 Detect MRP Situations 44](#_Toc232862896)

[4.6.7 Check and React to Material Exception 46](#_Toc232862897)

[4.6.8 Reduce Stock for TG0099 47](#_Toc232862898)

[4.7 MRP Change Request (Optional) 48](#_Toc232862899)

[4.7.1 Create Purchase Order 48](#_Toc232862900)

[4.7.2 Manage PIRs for Material TG0099 49](#_Toc232862901)

[4.7.3 MRP Rescheduling Check 50](#_Toc232862902)

[4.7.4 Create and Send MRP Change Requests 52](#_Toc232862903)

[4.7.5 Manage Change Requests 53](#_Toc232862904)

[4.7.6 React to MRP Change Requests based on Vendor’s Response 54](#_Toc232862905)

[5 Appendix 56](#_Toc232862906)

[5.1 Process Chains 56](#_Toc232862907)

[5.1.1 Preceding Processes 56](#_Toc232862908)

[5.1.2 Succeeding Processes 56](#_Toc232862909)

[5.2 Additional Functional Information 56](#_Toc232862910)

## Purpose

Overview

This process enables your material requirements planning (MRP) department to automate the procurement planning. The main function of MRP is to guarantee material availability and to avoid delays in order fulfillment. The planning run checks availability of each material and, in case of shortages, creates purchase requisitions, or delivery schedules if a scheduling agreement exists. Remaining shortages are displayed in the MRP app where the material planner can analyze the situation.

Procurement lead time can be longer than the time available to fulfill a demand. For this reason, you must procure the material in advance and cover your demand from stock. This process starts by creating forecast demands that are interpreted as expected customer demand. The MRP schedule runs. The system creates purchase requisitions or scheduling lines that trigger external procurement.

Optionally, you can handle time-dependent stock levels, purchase requisition handover and MRP material exceptions.

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
| Material Planner - External Procurement | SAP_BR_MATL_PLNR_EXT_PROC | Material Planning - External Procurement | SAP_BR_MATL_PLNR_EXT_PROC |  |
| Master Data Specialist - Product Data | SAP_BR_PRODMASTER_SPECIALIST | Master Data - Products / Product Governance | SAP_BR_PRODMASTER_SPECIALIST / SAP_CMD_SPT_PR_GOV_PC |  |
| Purchaser | SAP_BR_PURCHASER | Purchasing / Sourcing and Contracting | SAP_MM_SPT_PURCHASING_PC / SAP_MM_SPT_SOURCING_PC |  |
| Business Process Specialist | SAP_BR_BUSINESS_PROCESS_SPEC | Business Process Management / Business Process Management | SAP_BR_BUSINESS_PROCESS_SPEC / SAP_CA_SPT_BPS_PC |  |
| Inventory Manager | SAP_BR_INVENTORY_MANAGER | Inventory Management | SAP_BR_INVENTORY_MANAGER |  |

### Master Data, Organizational Data, and Other Data

The organizational structure and master data of your company have been created in your system during activation. The organizational structure reflects the structure of your company. The master data represents materials, customers, and vendors, for example, depending on the operational focus of your company.

|  |
| --- |
| Caution Update Behavior of Predelivered Demo DataIn non-productive environments (such as starter systems, sandbox systems, or partner demo systems), SAP initially deploys demo data for your selected scope. You can use this data to test and evaluate business processes.In a customer system, you can receive new or updated demo data after initial activation with further scope enhancements, provided the existing demo data wasn't changed in an incompatible way. If activation errors occur due to incompatible changes in demo data, you're responsible for resolving them. If you don't resolve the errors within a specific time frame, SAP reserves the right to deactivate demo data in your systems. In this case, you can continue by creating your own demo data. Alternatively, you can request that your systems be reprovisioned if you want to work with predelivered demo data again.In partner systems, you can use the demo data deployed with the initial activation. No additional demo data will be deployed in the system with scope enhancements. You can only create additional demo data manually. |

Use your own master data or the following sample data to go through the test procedure.

Material

| Master | Value | Details | Comments |
| --- | --- | --- | --- |
| Material | TG0011 | Trading Good 0011,PD,Regular Proc. | Used for MRP procedure without scheduling agreement |
| Material | TG0012 | Trad. Good 0012,Reord. Pt.,Regular Proc. | Used for MRP procedure with scheduling agreement |
| Material | TG0099 | Trading Good 0099,PD,Regular Proc. | Used for Material Situation Handling |

Org. Data

| Master | Value | Details | Comments |
| --- | --- | --- | --- |
| Plant | 3310 | Plant 1 AE |  |
| Vendor | 33300001 | Domestic UAE Supplier 1 |  |
| Vendor | 33300002 | Domestic UAE Supplier 2 |  |
| Company Code | 3310 | Company Code 3310 |  |
| Purchasing Organization | 3310 | Purch. Org. 3310 |  |

For more information on creating these master data objects, see the following [Master Data Scripts (MDS)](https://help.sap.com/docs/s4hana-best-practices/s4cld2608-master-data)

Table 1: Master Data Script Reference

| Master Data ID | Description |
| --- | --- |
| BNF | Create Product Master of type "Trading Good" - MDS |

### Business Conditions

Before this scope item can be tested, the following business conditions must be met.

| Scope Item | Business Condition |
| --- | --- |
| 31N - Situation Handling | Install this scope item for the situation handling steps. |

### Preliminary Steps

In this section, you are provided a detailed step-by-step description of technical or other prerequisites.

#### Create Scheduling Agreement

Purpose

This process step shows you how to create the scheduling agreement for the material/supplier combination, if it has not been maintained yet. If the scheduling agreement is already present in the system you can skip this step.

Procedure

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |  |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Purchaser. | The SAP Fiori launchpad displays. |  |  |
| 2 | Access the App | Open Manage Purchase Scheduling Agreements (F2179). |  |  |  |
| 3 | Create Scheduling Agreement | Select Create to create a scheduling agreement. | The Purchase Scheduling Agreement screen displays. |  |  |
| 4 | Enter Header Data | Under General Information tab, create a scheduling agreement with the following data:Supplier: 33300001Agreement type: SA With Release docValid To: dd.mm.yyyy (for example: 01.01.2099)Purchasing Organization: 3310Purchasing Group: 001Target Value: <For example, 200000 EUR> |  |  |  |
| 5 | Enter Header Notes | Navigate to the Notes tab, enter notes in some or all of the of the Header Notes elements for the ones mentioned below:Header textHeader notePricing typesDeadlinesTerms of deliveryShipping instructionsTerms of paymentWarrantiesPenalty for breach of contractGuaranteesContract riders (clauses)AssetOther contractual stipulationInbound DeliveryVendor memo (general)Vendor memo (pur. org.) |  |  |  |
| 6 | Add Items to Scheduling Agreement | Choose the Items tab and choose Create. | The Purchase Scheduling Agreement Item screen displays. |  |  |
| 7 | Enter Item Data | Make the following entries under General Information tab:Plant: 3310Material: TG0012In Quantity and Price tab, enter the following data:Target Quantity: 120 PCNet Order Price: 40Order Price Unit: PC or <defaulted value>In Output Control tab, make the following entry:Creation Profile: S001 |  |  |  |
| 8 | Enter Item Notes | Enter notes in some or all of the of the Header Notes elements for the ones mentioned below:Item textInfo record PO textMaterial PO textDelivery textInfo record noteES Master Agreements (MA)ES Requests f. Proposals (RFP)Sequence Number LPChoose Apply at the bottom of the view. |  |  |  |
| 9 | Save | Return to the New Purchase Scheduling Agreement header view and choose Create at the bottom of the view.Make a note of the schedule agreement number. | A schedule agreement is created. |  |  |

#### Prerequisite for Material Exception (Optional)

##### Manage Teams and Responsibilities

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to link the list of users who are supposed to receive material exception notifications.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Business Process Specialist. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Teams and Responsibilities (F2412). | The Manage Teams and Responsibilities screen displays. |  |
| 3 | Check Existing Teams | Make following entries and choose Go:Type: SMRPTIn Teams area, choose again the row of the filtered teams, check if MRPMaterial= TG0099 is maintained on Teams screen. If so, then the team is created already and please skip the following steps; if not maintained, then continue the following steps.Note If no filtered teams display in Teams area, please continue the following steps to create it. | If there is no entry for Plant 1 AE on the Area of Responsibility screen, choose Add to select it and then choose OK.For other plant entries on the Area of Responsibility screen, choose Delete to remove them and then choose OK. |  |
| 4 | Create Teams | Choose Create and make the following entries:Name: MRP MAT EXCEPTIONS TEAMStatus: EnabledType: SMRPTGo to the Responsibility Definitions section, and make the following entries:MRP Controller: 001MRP Material: TG0099MRP Plant: 3310Go to the Team Members area, and choose Create.On the Select: Business Partner screen, search by Last Name: : Material Planner - External Procurement, select the searched item and choose OK. | Then user MatlPlnrExtProc can receive the notification to handle the critical situation. |  |
| 5 | Save Team | Choose Create. | The team has been created. |  |

##### Manage Situation Types

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to configure the situation type by using template.

|  |
| --- |
| Note Please make sure 31N is activated if you want to execute this step. |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Business Process Specialist. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Situation Types (F2947). | The Manage Situation Types (F2947) screen displays. |  |
| 3 | Check Existing Situation Types | Choose the Situation Types tab. Make the following entries and choose Go:Name (In search box): MRP Material ExceptionsChoose the row of the filtered Situation Types and check whether types related to MRP Material Exceptions already exist. If so, skip step 4 and only maintain Start Batch Job in step 5; if not, continue the following steps.Note If no filtered teams are displayed, continue the following steps to create it. |  |  |
| 4 | Copy Situation Template | On the Manage Situation Types screen, there are two tabs: Situation Templates and Situation Types.Choose the Situation Templates tab and choose Go to search for the situation template: SAP_PP_MRP_MATERIAL_EXCEPTIONCheck the box before the situation template: SAP_PP_MRP_MATERIAL_EXCEPTION and choose Copy. |  |  |
| 5 | Create Custom Situation Template | In this step you create a situation type.On the Situation Type screen, make the following entries:ID: ZTEST_MRP_EXCEPTIONSThis field is the Unique Identifier of a situation type. The ID of a situation type should start with 'Z'. ID is a mandatory field and can't be left blank.Name: MRP Material ExceptionsIn the Recipients field, make the following entry:Filter by Member Function: MRP PlanningIn the Situation Monitoring field, make the following entry:Monitor Instances: SelectedIn the Batch Job Scheduling field, make the following entries:Time Zone: UTCStart Batch Job At: <Time you want your team members to get notification> (For example, if you want to let your team members receive the notification at UTC 8:00, then enter UTC 8:00. But due to system clock settings issue, there may be a 30-minute lag, so they get the notification around UTC 8:30.)Choose Create. | The situation has been created. |  |
| 6 | Enable Situation Template | Choose Yes for the pop-up message: Do you want to enable situation type? | The situation is enabled. |  |

#### Prerequisite for Handover of Purchase Requisition (Optional)

##### Assign MRP Group 0011 to TG0011

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to assign MRP group to TG0011.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Master Data Specialist - Product Data. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Change Material (MM02). |  |  |
| 3 | Specify Material | On the Change Material (Initial Screen), enter following data and choose Continue:Material: TG0011In the Select View(s) dialog box, choose MRP 1, and press Enter.In the Organization Levels dialog box, make the following data and press Enter:Plant: 3310 | The Change Material TGXXXX (Material general) screen displays. |  |
| 4 | Assign MRP Group | On the General Data tab, make the following entry and choose Save:MRP Group:0011 External procurement (PReq Handover) | The material change is saved. |  |

#### Prerequisite for MRP Change Request (Optional)

##### Assign Business User

Purpose

Create MRP Change Requests process needs an additional Purchaser role. This process step shows you how to assign business user if it has not been assigned yet.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Administrator. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Maintain Business Users (F1303). | The Maintain Business Users screen displays. |  |
| 3 | Search for Business User | On the Maintain Business Users screen, search for MATL_PLNR_EXT_PROC, then choose Go. | Line with MATL_PLNR_EXT_PROC displays. |  |
| 4 | Display Business User Screen | Tick the checkbox in front of the line and choose Edit. | The Maintain Business User screen displays |  |
| 5 | Check Business Role | In the Assigned Business Roles section, check whether SAP_BR_PURCHASER exists. If the role already exists, you can skip the next step. |  |  |
| 6 | Assign Business Role | On Assigned Business Roles section, choose Add.Search for SAP_BR_PURCHASER, tick the checkbox in front of the line and choose OK.Then choose Save. | Business Role SAP_BR_PURCHASER was assigned. |  |

##### Create Purchasing Info Record

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to create the purchasing info record for the material/supplier combination, if it has not been maintained yet.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Purchaser. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Purchasing Info Records (F1982). | The Manage Purchasing Info Records screen displays. |  |
| 3 | Check Existing Info Record | On the Manage Purchasing Info Records screen, search for Material: TG0099, and then choose Go.If an info record for material TG0099 with supplier 33300001 already exists, choose against the info record and check the General Information: Available From: and Available to. If you confirm this info record is valid, skip the following step 4 to 10. |  |  |
| 4 | Open New Purchasing Info Record | Choose Create. | The Purchasing Info Record Screen is displayed. |  |
| 5 | Enter Header Data | Make the following entries:Purchasing Info Record Category: StandardPurchasing Organization: 3310Supplier: 33300001Material: TG0099Plant: 3310Purchasing Group: 002 | Header data is added. |  |
| 6 | Enter General Information | Make the following entries:Available From: TodayAvailable To: 31.12.9999 | General Information is added. |  |
| 7 | Enter Purchasing Data | Make the following entries:Incoterm: EXWIncoterm Location 1: VENDOR | Purchasing Data is added. |  |
| 8 | Enter Delivery and Quantity Data | Make the following entries:Delivery Time in Days: 1Under Delivery Tolerance in %: 10.0Over Delivery Tolerance in %: 10.0Tax Code: <Input Tax Code>Tax Rate Valid From (If required): Select value from F4 helpTax Country/Region (If required): Select value from F4 helpNote When the TDT (time dependent tax) is activated via SSCUI 101016 (Define Tax Codes for Sales and Purchases) for country of company code and the tax code is given, the field Tax Rate Valid From is mandatory. You can enter current date, which will be adjusted to validity start date of tax code according to the settings in SSCUI.Order Unit: PCStandard Order Quantity: 10Goods-Receipt-Based Invoice Verification: selectNo Evaluated Receipt Settlement: select | Delivery and Quantity Data are added. |  |
| 9 | Enter Condition Data | In the Conditions section, choose Create.In the General Information area, make the following entries:Valid From: TodayValid To: 12.31.9999Amount: 30.00Pricing Unit: 1Currency: AEDChoose Apply. | Condition Data is added. |  |
| 10 | Create Your Data | Choose Create. | The purchasing info record is created. |  |

##### Clear PIRs for Material TG0099

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to clear the planned independent requirements directly for material TG0099.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Material Planner - External Procurement. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Maintain PIRs (F3445). | The Maintain PIRs screen displays. |  |
| 3 | Check Default Setting | Choose the user icon, and select App Settings.In the MRP Settings dialog box, choose Area of Responsibility.On the My Area of Responsibility screen, check if the below entry is assigned:Plant 1 AE (3310)MRP Controller 001 (001)Choose AOR Status if the status for the above entry is not yet assigned.Choose AOR Status to unassign the rest of other entries. Then choose Back.Please note that you need to maintain this AOR Status correctly when you go through the whole test script. |  |  |
| 4 | Select Material Items | On the Maintain PIRs screen, make the following entries:Plant: 3310Period Indicator: Monthly(M)Version Active: Select all optionsMaterial: TG0099 |  |  |
| 5 | Filter Result | Choose Go to execute. | Material item displays. |  |
| 6 | Check Material Item | Select the line with TG0099.Check the material item, if a PIR for a future data already exists, skip the following steps. If not, continue with the steps. |  |  |
| 7 | Clear PIRs | Choose Edit in the upper right. On the screen, clear the existing PIRs. | PIR for a data in the future is zero. |  |
| 8 | Save PIRs Draft | Choose Save at bottom right. | The PIRs are saved. |  |

##### Clear Purchase Requestions & Purchase Orders for Material TG0099

Purpose

This process step shows you how to clear a Purchase Order for material TG0099.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Material Planner - External Procurement. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Material Coverage - New Version (F0251A). | The Manage Material Coverage screen displays. |  |
| 3 | Select Material and Show Shortages | Make the following entries and choose Go:Material: TG0099Plant: 3310Shortage Definition: MRP Standard | The material item displays. |  |
| 4 | Display Stock / Requirements List | Choose the corresponding material item in the Materials list. | The detailed stock / requirements list for each material displays. |  |
| 5 | Clear Existing MRP Element | Under Stock / Requirements List, clear the existing MRP Element.In column Actions, select Delete from dropdown list. | MRP Elements have been cleared. |  |

## Overview Table

The Material Requirements Planning (J44) scope item consists of several process steps provided in the following table.

|  |
| --- |
| Note If your system administrator has enabled spaces and pages on the SAP Fiori launchpad, the homepage will only contain the essential apps for performing the typical tasks of a business role.You can find all other (searchable) apps not included on the homepage using the search bar ([2434549](https://me.sap.com/notes/2434549)).If you want to personalize the homepage and include the hidden apps, navigate to your user profile and choose App Finder. |

| Process Step | Business Role | Transaction/App | Expected Results |
| --- | --- | --- | --- |
| [Manage PIRs for Material TG0011 & TG0012](#unique_17) [page ] 21 | Material Planner - External Procurement | Maintain PIRs (F3445) | PIRs for TG0011 & TG0012 are created. |
| Monitor Material Coverage |  |  |  |
| [Run Material Requirements Planning (MRP)](#unique_18) [page ] 22 | Material Planner - External Procurement | Monitor Material Coverage - Net / Individual Segments (F2101A) | MRP runs for TG0011 and TG0012. |
| Evaluate MRP Result |  |  |  |
| [Evaluate MRP Result (Purchase Requisitions)](#unique_19) [page ] 23 | Material Planner - External Procurement | Monitor Material Coverage - Net / Individual Segments (F2101A) | MRP results are reviewed for material without scheduling agreement (TG0011). |
| [Evaluate MRP Result (Delivery Schedule)](#unique_20) [page ] 26 | Material Planner - External Procurement | Monitor Material Coverage - Net / Individual Segments (F2101A) | MRP results are reviewed for material with scheduling agreement (TG0012). |
| [Display MRP Run Master Data Issues](#unique_21) [page ] 28 | Material Planner - External Procurement | Display MRP Master Data Issues (F1425A) | The Display MRP Master Data Issues list displays. |
| [Display MRP Run Key Figures](#unique_22) [page ] 29 | Material Planner - External Procurement | Display MRP Key Figures (F1426) | The Display MRP Key Figures list displays. |
| Time-Dependent Safety Stock Levels |  |  |  |
| Time-Dependent Safety Stock |  |  |  |
| [Maintain MRP Safety Stock Method in Material](#unique_23) [page ] 30 | Master Data Specialist - Product Data | Manage Product Master Data (F1602) |  |
| [Maintain Time-Dependent Safety Stock](#unique_24) [page ] 31 | Material Planner - External Procurement | Maintain Time-Dependent Stock Levels (F5726) |  |
| [Manage Material Coverage](#unique_25) [page ] 32 | Material Planner - External Procurement | Manage Material Coverage - New Version (F0251A) |  |
| Time-Dependent Days of Supply |  |  |  |
| [Maintain MRP Safety Stock Method in Material](#unique_26) [page ] 33 | Master Data Specialist - Product Data | Manage Product Master Data (F1602) |  |
| [Maintain Time-Dependent Days of Supply](#unique_27) [page ] 34 | Material Planner - External Procurement | Maintain Time-Dependent Stock Levels (F5726) |  |
| [Manage PIRs for Material TG0099](#unique_28) [page ] 35 | Material Planner - External Procurement | Maintain PIRs (F3445) |  |
| [Manage Material Coverage](#unique_29) [page ] 37 | Material Planner - External Procurement | Manage Material Coverage - New Version (F0251A) |  |
| [Reset Material Master Data](#unique_30) [page ] 38 | Master Data Specialist - Product Data | Manage Product Master Data (F1602) |  |
| Material Exception (Optional) |  |  |  |
| [Clear Initial Stock](#unique_31) [page ] 39 | Inventory Manager | Manage Stock (F1062). |  |
| [Clear Existing Purchase Requisitions](#unique_32) [page ] 40 | Material Planner - External Procurement | Manage Material Coverage - New Version (F0251A) |  |
| [Manage PIRs for Material TG0099](#unique_33) [page ] 41 | Material Planner - External Procurement | Maintain PIRs (F3445) |  |
| [Run Material Requirements Planning (MRP) and Firm Purchase Requisition](#unique_34) [page ] 42 | Material Planner - External Procurement | Manage Material Coverage - New Version (F0251A) |  |
| [Increase Stock for TG0099](#unique_35) [page ] 43 | Inventory Manager | Manage Stock (F1062). |  |
| [Detect MRP Situations](#unique_36) [page ] 44 | Material Planner - External Procurement | Detect MRP Situations (F3853) |  |
| [Check and React to Material Exception](#unique_37) [page ] 46 | Material Planner - External Procurement | Notification |  |
| [Reduce Stock for TG0099](#unique_38) [page ] 47 | Inventory Manager | Manage Stock (F1062). |  |
| MRP Change Request (Optional) |  |  |  |
| [Create Purchase Order](#unique_39) [page ] 48 | Material Planner - External Procurement | Manage Material Coverage - New Version (F0251A) |  |
| [Manage PIRs for Material TG0099](#unique_40) [page ] 49 | Material Planner - External Procurement | Maintain PIRs (F3445) |  |
| [MRP Rescheduling Check](#unique_41) [page ] 50 | Material Planner - External Procurement | Schedule MRP Rescheduling Checks (F5417) |  |
| [Create and Send MRP Change Requests](#unique_42) [page ] 52 | Material Planner - External Procurement | Create MRP Change Requests (F5416) |  |
| [Manage Change Requests](#unique_43) [page ] 53 | Material Planner - External Procurement | Manage Change Requests (F0670) |  |
| [React to MRP Change Requests based on Vendor’s Response](#unique_44) [page ] 54 | Material Planner - External Procurement | Create MRP Change Requests (F5416) |  |

## Test Procedure

In this procedure, two MRP procedures are covered. One MRP procedure is for material(TG0011) without scheduling agreement, the other MRP procedure is for material (TG0012) with schedule agreement. Please follow the steps to test both subscenarios independently.

### Manage PIRs for Material TG0011 & TG0012

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to create the planned independent requirements directly for material TG0011 and TG0012.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Material Planner - External Procurement. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Maintain PIRs (F3445). | The Maintain PIRs screen displays. |  |
| 3 | Check Default Setting | Choose the user icon, and select App Settings.In the MRP Settings dialog box, choose Area of Responsibility.On the My Area of Responsibility screen, check if the below entry is assigned:Plant 1 AE (3310)MRP Controller 001 (001)Choose AOR Status if the status for the above entry is not yet assigned.Choose AOR Status to unassign the rest of other entries. Then choose Back.Please note that you need to maintain this AOR Status correctly when you go through the whole test script. |  |  |
| 4 | Select Material Items | On the Maintain PIRs screen, make the following entries:Plant: 3310Period Indicator: Monthly(M)Version Active: Select all optionsSearch: TG0011 |  |  |
| 5 | Filter Result | Choose Go to execute. | Material item displays. |  |
| 6 | Edit PIRs | Select the material item and choose Edit in the upper-right corner of the screen.On the screen, enter quantities per period, for example:PIR: 200 for all periodsMake sure the version is active.Version Active: Yes |  |  |
| 7 | Save PIRs Draft | Choose Save at bottom right. | The PIRs are saved. |  |
| 8 | Repeat Steps | Go back and repeat steps 4–7 for TG0012. In step 6, enter quantities per period, for example: PIR: 1000 for all periods |  |  |

### Monitor Material Coverage

#### Run Material Requirements Planning (MRP)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to start MRP run for both material with scheduling agreement and material without scheduling agreement.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Material Planner - External Procurement. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Monitor Material Coverage - Net / Individual Segments (F2101A). | The Monitor Material Coverage - Net / Individual Segments screen displays. |  |
| 3 | Check Default Setting | Choose the user icon, and select App Settings.In the MRP Settings dialog box, check if the toggle button of Manage Material Coverage - New Version (F0251A) is on.Turn it on if the toggle button is off. | If the toggle button is on, continue with following steps to navigate to Manage Material Coverage - New Version (F0251A).If the toggle button is off, you will be navigated to Check Material Coverage - Old Version (F0251).The following steps are described with the toggle button on. |  |
| 4 | Select Material and Show Shortages | In the search area, make the following entries and choose Go.Material: TG0011Material: TG0012Select the filtered rows and choose Manage Materials. | The Manage Material Coverage screen displays. |  |
| 5 | Start MRP Run for Material without Scheduling Agreement | Choose TG0011 in the Materials list on the left side.On the right screen, choose Start MRP Run. | The MRP run in progress notification displays first, and then MRP Run completed notification displays. |  |
| 6 | Start MRP Run for Material with Scheduling Agreement | Repeat step 5 for TG0012. | The MRP run in progress notification displays first, and then MRP run was completed notification displays. |  |

#### Evaluate MRP Result

##### Evaluate MRP Result (Purchase Requisitions)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to evaluate MRP results for material without scheduling agreement.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Material Planner - External Procurement. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Monitor Material Coverage - Net / Individual Segments (F2101A). |  |  |
| 3 | Rescheduling Columns and Last MRP Run Column (Optional) | Choose the Settings icon in the upper-right corner to add the following columns and choose OK:The rescheduling columns:Reschedule InReschedule OutCancel ProcessRescheduling ProposalsThe last MRP run column:Last MRP Run | The rescheduling columns display the number of the rescheduling proposals by category respectively. The Rescheduling Proposals column displays the total number of the rescheduling proposals.The Last MRP Run column displays the date and the time when the last MRP run was performed for a material.You can also choose Adapt Filters to add these filters to help filter the materials with specific rescheduling proposals or the materials with MRP run performed on a specific date/period. |  |
| 4 | Check Default Setting | Choose the user icon, and select App Settings.In the MRP Settings dialog box, check if the toggle button of Manage Material Coverage - New Version (F0251A) is on.Turn it on if the toggle button is off. | If the toggle button is on, continue with following steps to navigate to Manage Material Coverage - New Version (F0251A).If the toggle button is off, you will be navigated to Check Material Coverage - Old Version (F0251).The following steps are described with the toggle button on. |  |
| 5 | Select Material and Show Shortages | In the search area, make the following entries and choose Go.Material: TG0011Select the filtered rows and choose Manage Materials. | The Manage Material Coverage screen displays.On the left side of the screen, you could choose Adapt Filters and the Settings icon to configure column Last MRP Run to help filter materials. The last MRP run information is also available on the material header and the Material Information section. |  |
| 6 | Verify Purchase Requisitions that are Available | In the Stock/Requirements List, purchase requisitions are shown as MRP results.Look for rows with PurRqs items to check more details. | The MRP has created purchase requisitions that can be used for the Procurement of Direct Materials test script.You could click the PurRqs item, choose Document Info, and the Purchase Requisition screen displays where you can find more details about existing PR. |  |
| 7 | Handover of Purchase Requisition (Optional) | Check the PurRqs items with Handover Pending icon and choose Hand Over. Then choose Yes in the dialog box.Note If you want to handover more than one purchase requisition at a time, you could use Hand Over Purchase Requisitions (F4795) app. Refer to relevant steps at the end of this section. | The icon turns to Handover Completed. |  |
| 8 | Rescheduling Check (Optional) | In the Stock/Requirements List, the Rescheduling column displays the rescheduling status of the following MRP Elements.PurReqPurchase OrdersPlanned OrdersProduction OrdersProcess OrdersIf necessary actions can be performed, below icons in the Rescheduling column are displayed via pushing buttons. Push the buttons and corresponding actions perform directly.Reschedule in (Bring operation forward if the receipt element lies after the requirement date)Reschedule out (Postpone operation, if the receipt element lies before the requirement date)Plan Process according to scheduleCancel ProcessExcess StockExcess in individual segment | Corresponding actions perform. |  |
| 9 | Restore MRP Group for TG0011 (Optional) | Log on to the SAP Fiori launchpad as a Master Data Specialist - Product Data.Open Change Material (MM02).Make the following entry and press Enter:Material: TG0011On the Change Material (Initial Screen), in the Select View(s) dialog box, choose MRP 1 and choose Continue (Enter) icon.In the Organization Levels dialog box, make the following entry, and choose Continue (Enter) icon:Plant: 3310On the General Data tab, make the following entry and choose Save:MRP Group: <blank> | Material TG0011 MRP group is restored. |  |

Hand Over Purchase Requisitions (Optional)

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Material Planner - External Procurement. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Hand Over Purchase Requisitions (F4795). |  |  |
| 3 | Filter Result | Choose following entries as filter, and choose Go:Status Description: Handover PendingMaterial: TG0011 |  |  |
| 4 | Mass Handover | Select the Purchase Requisitions you want, choose Hand Over. Then choose Yes in the dialog box. | A message appears: Handover was successful |  |

##### Evaluate MRP Result (Delivery Schedule)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to evaluate MRP results for materials with scheduling agreements.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Material Planner - External Procurement. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Monitor Material Coverage - Net / Individual Segments (F2101A). |  |  |
| 3 | Check Default Setting | Choose the user icon, and select App Settings.In the MRP Settings dialog box, check if the toggle button of Manage Material Coverage - New Version (F0251A) is on.Turn it off if the toggle button is on. | If the toggle button is off, continue with following steps to navigate to Check Material Coverage - Old Version (F0251).The following steps are described with the toggle button off. |  |
| 4 | Select Material and Show Shortages | In the search area, make the following entry and choose Go.Material: TG0012Select the filtered row and choose Manage Materials. | The Manage Material Coverage screen displays. |  |
| 5 | Verify Schedule Lines that are Available | In the Stock/Requirements List, the MRP results show as schedule lines.Look for rows with SchLne items to show more details. | The MRP created schedule lines.You can click the SchLne item, choose Open…, and choose Delivery Schedule or Scheduling Agreement to display more details.If you choose Delivery Schedule, the screen Display Sch. Agmt Schedule: Item Overview shows. Choose the schedule agreement item and then choose Delivery Schedule to display delivery schedule information.If you choose Scheduling Agreement, the Display Scheduling Agreement: Item Overview screen shows. |  |
| 6 | Check Delivery Schedule Button | Choose Delivery Schedule at the top of the screen to view the delivery schedule. | The Scheduling Agreement Delivery Schedule screen displays.The SchLne items display with a deviation chart and quantity.Choose Back. |  |
| 7 | Check Planning Details (Optional) | In the Shortage Definition dropdown list, select MRP Standard, then select the Table View button. In the Available column, select an exception highlighted with a red statusShortage Definition: MRP StandardView Button: Table View | The Material Shortage screen displays.The View buttons are located in the upper right of the Stock/Requirements List. |  |
| 8 | Change Style and Version of the Material Detail List | On the Material Shortage screen, explore the display options (table view/chart view) by selecting an icon located in the upper right. | Go back twice to the Monitor Material Coverage - Net and Individual Segments screen, and navigate to the row of material: TG0012, click against red/green charts in the Stock Availability column.The Projected Stock screen displays the Availability per date. In the button line, you can click Check Material Coverage. You would go to the same Material Details list as in the previous step.Note The app Check Material Coverage - Old Version (F0251) will be replaced by Manage Material Coverage - New Version (F0251A) in future releases. When you open Check Material Coverage - Old Version (F0251), a popover guides you through this transition, and a toggle button on the Fiori launchpad shell bar allows you to switch between the two versions.The feature parity is not yet fully achieved. Therefore, you should continue using Check Material Coverage - Old Version (F0251) for scenarios that are not yet supported in Manage Material Coverage - New Version (F0251A), including scheduling agreement scenarios. |  |

### Display MRP Run Master Data Issues

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to check MRP Run Master Data Issues.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Material Planner - External Procurement. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Display MRP Master Data Issues (F1425A) |  |  |
| 3 | Check the Issues | Select the issue to display the details. | If there are any issues, choose the issue to display the details of the error. |  |

### Display MRP Run Key Figures

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to check the key figures of the MRP run.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Material Planner - External Procurement. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Display MRP Key Figures (F1426). | The Display MRP Key Figures list displays. |  |
| 3 | Select MRP Run | Open the log with name Material Requirements Planning (MRP).Select the row with your user and the specific log name, for example, the Material Requirements Planning (MRP) job description. | The details of MRP run displays. |  |

### Time-Dependent Safety Stock Levels

#### Time-Dependent Safety Stock

##### Maintain MRP Safety Stock Method in Material

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to maintain MRP safety stock method in material master data.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Master Data Specialist - Product Data. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Product Master Data (F1602). | The Manage Product Master Data standard selection screen displays. |  |
| 3 | Select Material | In the search area, make the following entries and choose Go:Material: TG0099In the Products list, choose the line of the material TG0099. | The product details screen displays. |  |
| 4 | Select Plant | In the TG0099 details view, choose the menu Plants.On the Plants tab, choose the line of the plant 3310. | The material in Plant 3310 details displays. |  |
| 5 | Maintain MRP Safety Stock Method | Choose Edit to switch to the edit mode. Then go to menu MRP Data > Lot-Size Data .On the Lot-Size Data tab, assign Time-Dependent Safety Stock in the drop-down list of MRP Safety Stock Method.Choose Apply, and choose Save. | The MRP safety stock method is assigned in material master data. |  |

##### Maintain Time-Dependent Safety Stock

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to maintain time-dependent safety stock for material TG0099, which is assigned MRP safety stock method Time-Dependent Safety Stock.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Material Planner - External Procurement. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Maintain Time-Dependent Stock Levels (F5726). | The Maintain Time-Dependent Stock Levels screen displays. |  |
| 3 | Select Material | In the search area, make the following entries and choose Go:Material Number: TG0099In the Materials list, choose the line of material TG0099. | The material details display on the right side of the screen. |  |
| 4 | Maintain Validity Intervals | In the Validity Intervals view, choose Add Interval for the first interval:In the Add New Validity Interval dialog that pops up, enter today’s date in the field Start Date. Then choose Add and confirm any information. (Note that the first interval must be today).Choose Add Interval for the second interval:In the Add New Validity Interval dialog that pops up, enter beginning of next month in the field Start Date; enter 100 in the field Safety Stock. Then choose Add and confirm any information.Choose Add Interval for the third interval:In the Add New Validity Interval dialog that pops up: enter beginning of the month after next month in the field Start Date; enter 150 in the field Safety Stock. Then choose Add and confirm any information. | Time-dependent safety stock intervals are maintained. |  |

##### Manage Material Coverage

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you the Stock/Requirement List of TG0099 before and after running MRP, so that the functionality of Time-dependent safety stock is demonstrated.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Material Planner - External Procurement. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Material Coverage - New Version (F0251A). | The Manage Material Coverage screen displays. |  |
| 3 | Select a Material | In the search area, make the following entries and choose Go.Shortage Definition: MRP StandardMaterial: TG0099Plant: 3310 | The material item displays. |  |
| 4 | Check the Stock/Requirement List before Running MRP | Choose the material item. As a result of safety stock you input 2 validity intervals, and then you can see 2 requirements with MRP element SfyReq: The quantity of the first SfyReq is 100. The quantity of the second SfyReq is 50. In this case, the total safety stock in the second interval is 100+50=150. This number matches the input in the second interval. | MRP element for Safety stock displays. |  |
| 5 | Run MRP to Create Purchase Requisition | Choose Start MRP Run at the upper right. | The MRP run in progress notification first pops up, and then MRP run was completed notification pops up. |  |
| 6 | Evaluate the Purchase Requisition and delete them | If supply cannot cover requirement, MRP will generate purchase requisition. You can evaluate the MRP proposed purchase requisition regarding scheduling and quantity.For testing purpose, you can choose the Edit button and delete them. As till now the sub-process for method Time-dependent safety stock is completed, and TG0099 can be reused in other sub-process. | MRP result is evaluated and testing environment is cleaned up. |  |

#### Time-Dependent Days of Supply

##### Maintain MRP Safety Stock Method in Material

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to maintain MRP safety stock method in material master data.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Master Data Specialist - Product Data. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Product Master Data (F1602). | The Manage Product Master Data standard selection screen displays. |  |
| 3 | Select Material | In the search area, make the following entries and choose Go:Material: TG0099In the Products list, choose the line of the material TG0099. | The product details screen displays. |  |
| 4 | Select Plant | In the TG0099 details view, choose the menu Plants.On the Plants tab, choose the line of the plant 3310. | The material in Plant 3310 details displays. |  |
| 5 | Maintain MRP Safety Stock Method | Choose Edit to switch to the edit mode. Then go to menu MRP Data > Lot-Size Data .On the Lot-Size Data tab, assign Time-Dependent Safety Stock in the drop-down list of MRP Safety Stock Method.Choose Apply, and choose Save. | The MRP safety stock method is assigned in material master data. |  |

##### Maintain Time-Dependent Days of Supply

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to maintain Time-Dependent Days of Supply for material TG0099, which has assigned MRP safety stock method Time-dependent safety stock.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Material Planner - External Procurement. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Maintain Time-Dependent Stock Levels (F5726). | The Maintain Time-Dependent Stock Levels screen displays. |  |
| 3 | Select Material | In the Standard (selection) section, make the following entries and choose Go:Material: TG0099In the Materials section, choose the line of the material TG0099. | The details screen displays on the right side. |  |
| 4 | Maintain Validity Intervals | In the Validity Intervals view, you can see the intervals created in step [Manage Material Coverage](#unique_25) [page ] 32, which can be reused.Choose Edit to switch to the Edit mode. Remove the safety stock quantity. Because the safety stock Method is changed to Days of Supply, the safety stock does not take effect here.For the first interval:Keep all fields blank.For the second interval:Input 1 in the field Safety Dos. Input 2 in the field Target Dos.For the third interval:Input 1 in the field Safety Dos. Input 3 in the field Target Dos.Choose Save. | The time-dependent intervals are maintained:*In MRP, the PIR quantity in one interval is considered as Daily consumption.Safety stock level = daily consumption * Safety DOSTarget stock level = daily consumption * Target DOSIn one interval, only if net supply (target stock level in last interval – PIR in current interval) < safety stock level, MRP will trigger replenishment to build up target stock level. |  |

##### Manage PIRs for Material TG0099

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to create the planned independent requirements directly for material TG0099.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Material Planner - External Procurement. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Maintain PIRs (F3445). | The Maintain PIRs screen displays. |  |
| 3 | Check Default Setting | Choose the user icon, and select App Settings.In the MRP Settings dialog box, choose Area of Responsibility.On the My Area of Responsibility screen, check if the below entry is assigned:Plant 1 AE (3310)MRP Controller 002 (002)Choose AOR Status if the status for the above entry is not yet assigned.Choose AOR Status to unassign the rest of other entries. Then choose Back.Please note that you need to maintain this AOR Status correctly when you go through the whole test script. |  |  |
| 4 | Select | On the Maintain PIRs screen, make the following entries:Plant: 3310Period Indicator: Monthly(M)Version Active: Select all optionsMaterial: TG0099 |  |  |
| 5 | Filter Result | Choose Go to execute. | Material item displays. |  |
| 6 | Check Material Item | Select the line with TG0099.Check the material item, if a PIR for a future data already exists, clear it. |  |  |
| 7 | Edit PIRs | Choose Edit in the upper-right corner. On the screen, enter quantities per period, for example:PIR: 100 for next period in the futurePIR: 200 for the period afterMake sure the version is active.Version Active: Yes | PIR for a data in the future is entered. The PIRs period should match the interval you maintained in previous step. |  |
| 8 | Save PIRs Draft | Choose Save on bottom right. | The PIRs are saved. |  |

##### Manage Material Coverage

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you the Stock/Requirement List of TG0099 before and after running MRP, so that the functionality of Time-dependent Days of supply is demonstrated.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Material Planner - External Procurement. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Material Coverage - New Version (F0251A). | The Manage Material Coverage screen displays. |  |
| 3 | Select Material | In the search area, make the following entries and choose Go.Material: TG0099Plant: 3310 | The material item displays. |  |
| 4 | Check the Stock/Requirement List before Run MRP | Choose the corresponding material in the Materials list.The PIRs you input in the previous step are displayed as requirements in stock/requirement list. |  |  |
| 5 | Run MRP to Create Purchase Requisition | Choose Start MRP Run at the upper right. | The MRP run in progress notification first pops up, and then MRP run was completed notification pops up. |  |
| 6 | Evaluate the Purchase Requisition and Delete Them | Regarding the data input in previous steps:In interval next month: target stock level 100*2= 200 is built up.In interval the month after next month: net supply = 200-200=0 < stock level 1*200=200 MRP, which proposes replenishment to build up target stock level 200*3=600 |  |  |

##### Reset Material Master Data

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to reset material master data to set up a clean environment for the succeeding testing.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Master Data Specialist - Product Data. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | On the Home screen, click the menu Master data – Products, then choose the tile Manage Product Master Data (F1602). | The Manage Product Master Data screen displays. |  |
| 3 | Select Material | In the Standard (selection) tab, enter the following entries and choose Go:Material: TG0099On the Products tab, choose the row of the material TG0099. | The Material details screen displays. |  |
| 4 | Select Plant | In the TG0099 details view, click the menu plant.On the Plants tab, choose the row of the plant 3310 | The Material in Plant 3310 details displays. |  |
| 5 | Maintain MRP safety stock method | Choose Edit to switch to the edit mode. Then go to menu MRP Data > Lot size Data .On the Lot size data tab, in the field MRP safety stock Method, assign Time-dependent Safety stock.Choose Apply, and choose Save. | Once MRP safety stock method is removed from material master data, the interval maintained in the previous steps will not be considered in MRP. |  |

### Material Exception (Optional)

#### Clear Initial Stock

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to ensure TG0099's stock is empty.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Inventory Manager. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Stock (F1062). | The Manage Stock screen displays. |  |
| 3 | Specify Material | Make the following entries and press Enter:Material: TG0099Plant: 3310 | The stock overview for the product displays. |  |
| 4 | Clear Stock | If the current stock of TG0099 is zero, skip this step.On the screen, you can check Storage Location, Unrestricted-Use Stock, Blocked Stock, and Stock in Quality Inspection.Choose the Unrestricted-Use Stock icon, and make the following entries:Stock Change: ScrappingQuantity: <=“Current Quantity“>Cost Center: <Cost Center>, for example, 33101301Choose Post. | Unrestricted-Use Stock is 0.000 PC. |  |

#### Clear Existing Purchase Requisitions

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to ensure TG0099’s purchase requisitions is empty.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Material Planner - External Procurement. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Material Coverage - New Version (F0251A) | The Manage Material Coverage screen displays. |  |
| 3 | Select Material and Show Shortages | Make the following entries and choose Go.Material: TG0099Plant: 3310Shortage Definition: MRP Standard | The material items display. |  |
| 4 | Clear Purchase Requisitions | Check the material item.Under Stock / Requirements List, clear the existing PurRqs.In column Actions, select Delete from the dropdown list. | There is no purchase requisition. |  |

#### Manage PIRs for Material TG0099

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to create the planned independent requirements directly for material TG0099.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Material Planner - External Procurement. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Maintain PIRs (F3445). | The Maintain PIRs screen displays. |  |
| 3 | Check Default Setting | Choose the user icon, and select App Settings.In the MRP Settings dialog box, choose Area of Responsibility.On the My Area of Responsibility screen, check if the below entry is assigned:Plant 1 AE (3310)MRP Controller 001 (001)Choose AOR Status if the status for the above entry is not yet assigned.Choose AOR Status to unassign the rest of other entries. Then choose Back.Please note that you need to maintain this AOR Status correctly when you go through the whole test script. |  |  |
| 4 | Select Material Items | On the Maintain PIRs screen, make the following entries:Plant: 3310Period Indicator: Monthly(M)Version Active: Select all optionsMaterial: TG0099 |  |  |
| 5 | Filter Result | Choose Go to execute. | Material item displays. |  |
| 6 | Check Material Item | Select the line with TG0099.Check the material item. If a PIR for a future data already exists, skip the following steps. If not, continue with the steps. |  |  |
| 7 | Edit PIRs | Choose Edit in the upper right. On the screen, enter quantities per period, for example:PIR: 100 for next period in the futureMake sure the version is active.Version Active: Yes | PIR for a data in the future is entered. |  |
| 8 | Save PIRs Draft | Choose Save at bottom right. | The PIRs are saved. |  |

#### Run Material Requirements Planning (MRP) and Firm Purchase Requisition

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to start MRP run for material with scheduling agreement.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Material Planner - External Procurement. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Material Coverage - New Version (F0251A). | The Manage Material Coverage screen displays. |  |
| 3 | Select Material AND | Make the following entries and choose Go.Material: TG0099Plant: 3310Shortage definition: MRP Standard | The material item displays. |  |
| 4 | Run MRP to Create Purchase Requisition | Choose the material item. On the right screen, choose Start MRP Run. | The MRP run in progress notification displays first, and then MRP run was completed notification displays. |  |
| 5 | Firm Purchase Requisition | Check the generated PurRqs. Select Edit from Action dropdown list, and change the delivery date to firm it. Choose OK. | The Purchase requisition was changed notification displays first, then the PurRqs are locked. |  |

#### Increase Stock for TG0099

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to increase stock and make it more than PIR.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Inventory Manager. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Stock (F1062). | The Manage Stock (F1062). screen displays. |  |
| 3 | Specify Material | Make the following entries and press Enter:Material: TG0099Plant: 3310 | The Stock overview for the product displays. |  |
| 4 | Increase Stock | Choose the icon beside Unrestricted - Use Stock to add the initial stock for your chosen storage location (For example, Raw mat. stoloc 331A), and choose Post.Quantity: <For example, 200>Document Data: TodayPosting Date: Today | Unrestricted-Use Stock is greater than PIR. |  |

#### Detect MRP Situations

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to run job for MRP material exception.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Material Planner - External Procurement. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Detect MRP Situations (F3853)Note If the App is not available by default, please use the App finder to add it to the SAP Fiori launchpad. | The Application Jobs screen displays. |  |
| 3 | Enter Basic Parameters for New Job | On the Application Jobs screen, choose Create and make the following entries:For 1. Template Selection section: Job Template: MRP Situation Handling TemplateJob Name: <: MRP Situation Handling for TG0099>Choose Step 2.For 2. Scheduling Options section: Start Immediately: <select>Choose Define Recurrence Pattern.On the Scheduling Information screen, make the following entries: Start Immediately: XRecurrence Pattern: Single RunChoose OK.Choose Step 3.For 3. Parameters section: Material: TG0099MRP Controller: 001Plant: 3310Choose Check at the bottom right, then choose Schedule. |  |  |
| 4 | Refresh Application Jobs List | To check the status of the job you created, choose Go on the top right section of the screen. | The Application Jobs table is refreshed. |  |
| 5 | Verify the Job Results | To see the outcome of the job, choose the icon in Results column. | A Documents screen should list the purchase requisition created in chapter [Run Material Requirements Planning (MRP) and Firm Purchase Requisition](#unique_34) [page ] 42 for cancellation. |  |

#### Check and React to Material Exception

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

By the prerequisite step, notification will be automatically sent to responsible team members. The detection process is automatically triggered by the system on a regular basis based on the Batch Job Scheduling parameters maintained in section Create Situation Types and indicates material exception situations to the material planner (usually within one hour). This process step shows you how to check and react to material exception.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Material Planner - External Procurement. | The SAP Fiori launchpad displays. |  |
| 2 | Check Notifications | On the home screen, choose the Notifications icon in the upper right corner. | The following notification displays:Cancel process: PurchReq 1xxxxxx-000010 Material TG0099 Plant 3310.It enables the material planner to proactively take further action. |  |
| 3 | Navigate to Manage Material Coverage App | Choose the detailed notification line Cancel process: PurchReq 1xxxxxx-000010 MaterialTG0099Plant3310., it navigates to Manage Material Coverage screen. | The Manage Material Coverage screen for discontinued product displays. |  |
| 4 | Delete Purchase Requisition | On the Manage Material Coverage screen, select Delete from Action dropdown list. Then choose Delete in the dialog box. | The purchase requisition detected by the MRP Material Exception job disappears. |  |
| 5 | Dismiss the MRP Material Exception | Choose Close Situation in the yellow notification box and pick a reason for dismissing the situation. Choose Confirm. | The situation has been dismissed. |  |
| 6 | Close the Notification Message | On the home screen, choose the Notifications icon in the upper right corner and choose the cross sign in the upper right corner to close the notification message.(You may need to repeat this step for notifications on the same purchase requisition and material issued for days earlier than today.) | The notification for the resolved MRP Material Exception disappears from the list. |  |

#### Reduce Stock for TG0099

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to decrease stock and make it less than PIR.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Inventory Manager. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Stock (F1062). | The Manage Stock screen displays. |  |
| 3 | Specify Material | Make the following entries and press Enter:Material: TG0099Plant: 3310 | The stock overview for the product displays. |  |
| 4 | Reduce Stock | On the screen, you can check Storage Location, Unrestricted-Use Stock, Blocked Stock, and Stock in Quality Inspection.Choose the Unrestricted-Use Stock icon, and make the following entries:Stock Change: ScrappingQuantity: <= "Current Quantity"> (make it less than PIR)Cost Center: <Cost Center>, for example, 33101301Choose Post. | Unrestricted-Use Stock is less than PIR. |  |

### MRP Change Request (Optional)

#### Create Purchase Order

Purpose

This process step shows you how to create a purchase order for TG0099.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Material Planner - External Procurement. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Material Coverage - New Version (F0251A). | The Manage Material Coverage screen displays. |  |
| 3 | Select Material and Show Shortages | Make the following entries and choose Go:Material: TG0099Plant: 3310Shortage Definition: MRP Standard | The material item displays. |  |
| 4 | Create a Purchase Requisition | Choose the material item. On the right screen, choose Create Order, make the following entries, and choose Create.Receipt Quantity: 100 PCAvailability Date: <Current + 2 Month>Source of Supply for Order: <Info Record with supplier 33300001> | Purchase requisition has been created. |  |
| 5 | Convert the Purchase Requisition into Purchase Order | Check the PurRqs items and select Convert in the dropdown list from the Actions column. Check the information, then choose Convert in the pop-up dialog: Purchase Requisition was converted. Note down this purchase order number. | Purchase requisition has been converted. |  |

#### Manage PIRs for Material TG0099

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to create the planned independent requirements directly for material TG0099.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Material Planner - External Procurement. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Maintain PIRs (F3445). | The Maintain PIRs screen displays. |  |
| 3 | Check Default Setting | Choose the user icon, and select App Settings.In the MRP Settings dialog box, choose Area of Responsibility.On the My Area of Responsibility screen, check if the below entry is assigned:Plant 1 AE (3310)MRP Controller 001 (001)Choose AOR Status if the status for the above entry is not yet assigned.Choose AOR Status to unassign the rest of other entries. Then choose Back.Please note that you need to maintain this AOR Status correctly when you go through the whole test script. |  |  |
| 4 | Select Material Items | On the Maintain PIRs screen, make the following entries:Plant: 3310Period Indicator: Monthly(M)Version Active: Select all optionsMaterial: TG0099 |  |  |
| 5 | Filter Result | Choose Go to execute. | Material item displays. |  |
| 6 | Check Material Item | Select the line with TG0099.Check the material item. If a PIR for a future data already exists, skip the following steps. If not, continue with the steps. |  |  |
| 7 | Edit PIRs | Choose Edit in the upper-right corner. On the screen, clear the existing PIRs and enter:PIR: 100 <for current + 1 Month>Version Active: YES | PIR for a data in the future is entered. |  |
| 8 | Save PIRs Draft | Choose Save on bottom right. | The PIRs are saved. |  |

#### MRP Rescheduling Check

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process helps you to identify the MRP exceptions, and shows you how to schedule MRP rescheduling check to collect MRP rescheduling information.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Material Planner - External Procurement. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Schedule MRP Rescheduling Checks (F5417) | The Application Jobs screen displays. |  |
| 3 | Enter Parameters for New Job | On the Application Jobs screen, choose Create and make the following entries:For 1. Template Selection section: Job Template: MRP Rescheduling ChecksJob Name: MRP Rescheduling Checks for TG0099Choose Step 2.For 2. Scheduling Options section: Start Immediately: <select>Recurrence Pattern: Single RunChoose Step 3.For 3. Parameters section: MRP Plant: 3310MRP Controller: 001Material: TG0099Choose Check at the bottom right, then choose Schedule. |  |  |
| 4 | Check Result | Choose Go to refresh the page. When the Status shows Finished, click the icon in the column Results to see the result. | On the Document (ID xxxxxxxxx) screen, item with Material: TG0099, Exception Message: Reschedule in appears. |  |

|  |
| --- |
| Note Related APIs and Communication ArrangementsIf you want to verify that the filtering of the SOAP outbound service MRP Change Request Message Outbound is working as intended, or to verify that one SOAP message does contain the MRP change requests for one supplier of one company code, please utilize API for integration scenario. To set up relevant communication arrangement, refer to APIs and Communication Arrangements for Scope Items in SAP S/4HANA Cloud Public Edition.For details regarding the interfaces, please access the SAP Process Navigator for SAP S/4HANA Cloud Public Edition cloud and navigate to Accelerators > Implementation > APIs.Integration ScenarioIntegration Scenario NameSAP_COM_0667Communication arrangement for MRP Change Request Outbound |

#### Create and Send MRP Change Requests

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to create and send MRP Change Requests for TG0099.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Material Planner - External Procurement. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Create MRP Change Requests (F5416) | The Create MRP Change Requests screen displays. |  |
| 3 | Select Material and Show Purchase Order Schedule Lines | In the Create MRP Change Requests screen, enter the following entry and choose Go.Material: TG0099 | Purchase Order Schedule Line for TG0099 displays. The Requested Date, Quantity and Request Status are empty. |  |
| 4 | Create Change Requests | Tick the checkbox in front of the Purchase Order which was created in pervious step and choose Create Change Requests. | Change requests for the record created successfully.The Requested Date and Quantity were updated, and Request Status become New. |  |

#### Manage Change Requests

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to manually set the MRP Change Request status to "Requested", and how to review the detailed requested MRP Change Requests for TG0099.

If you have already built the communication scenario "SAP_COM_0667: Manufacturing - MRP Change Request Integration", this step can also be done automatically with the app Create MRP Change Requests (F5416).

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Material Planner - External Procurement. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Change Requests (F0670). | The Manage Change Requests screen displays. |  |
| 3 | Search for the Vendor | In My Vendors / Contacts list, search for Vendor (Supplier)<33300001>. | Change requests under Vendor<33300001> were listed. |  |
| 4 | Set to Requested | Tick the checkbox in front of the Order which was created in pervious step and choose Set to Requested. | The Order Item was set to REQUESTED. |  |
| 5 | Review the requested change Requests | On the Change Requests table, choose the tab: REQUESTED. Click against the item that you requested in last step and review the change request detail. | Change Request Details are listed. |  |

|  |
| --- |
| Note Related APIs and Communication ArrangementsIf you want to verify that the filtering of the SOAP outbound service MRP Change Request Message Outbound is working as intended, or to verify that one SOAP message does contain the MRP change requests for one supplier of one company code, please utilize API for integration scenario. To set up relevant communication arrangement, refer to APIs and Communication Arrangements for Scope Items in SAP S/4HANA Cloud Public Edition.For details regarding the interfaces, please access the SAP Signavio Process Navigator, choose the solution scenario for SAP S/4HANA Cloud Public Edition and navigate to Accelerators > Implementation > APIs.Integration ScenarioIntegration Scenario NameSAP_COM_0667Communication arrangement for MRP Change Request Outbound |

#### React to MRP Change Requests based on Vendor’s Response

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

Suppose you already got the vendor’s response from Ariba. This process step shows you how to react to MRP Change Requests for TG0099 based on vendor’s response.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Material Planner - External Procurement. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Create MRP Change Requests (F5416) | The Create MRP Change Requests screen displays. |  |
| 3 | Select Material and Show Purchase Order Schedule Lines | In the Create MRP Change Requests screen, enter the following entry and choose Go.Material: TG0099 | The Purchase Order Schedule Line for TG0099 displays. The Requested Date, Quantity, and Request Status are empty. |  |
| 4 | Navigates to Manage Change Requests | Click against the Request Status for the purchase order.Navigates to the Manage Change Requests screen. | The Manage Change Requests screen displays. |  |
| 5 | React to Vendor’s Responses | In the RECEIPT/REQUIREMENT ITEMS list, select one of the following vendor's responses:Pending/ Accepted/ Rejected/ New Proposal.Assume you got vendor’s response as Accepted. Choose tab Accepted and then choose Apply Changes.If you got vendor’s response as Rejected, choose tab Rejected and then choose Discard.You can also enter a New Proposal based on vendor’s response and then choose Apply Changes.Choose OK in the pop-up dialog: Purchase Order XXXXXXXX-XX will be changed. | The change request status becomes: Applied or Discarded. |  |

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
| J45 - Procurement of Direct Materials | A purchase requisition is created as part of the Material Requirements Planning (J44) test script. This purchase requisition is converted into a purchase order in the Procurement of Direct Materials (J45) process. |

### Additional Functional Information

If you want to know functional information for Discrete and Process Manufacturing beyond what is described in the test scripts of the best practice scope items for SAP S/4HANA Cloud Public Edition, you could check SAP Note [3441318](https://me.sap.com/notes/3441318).

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
> Flagged while digesting this document, not verified: Internal: the Days of Supply section's 'Maintain MRP Safety Stock Method in Material' step assigns Time-Dependent Safety Stock, yet the next step says the safety stock method 'is changed to Days of Supply'; the Reset Material Master Data step also says to assign Time-dependent Safety stock while its expected result says the method is removed.

> [!warning] Conflict
> Flagged while digesting this document, not verified: Internal: material TG0099 uses MRP Controller 001 in every other step (team definition, PIR steps, Detect MRP Situations, rescheduling check), but the Days of Supply 'Manage PIRs for Material TG0099' step requires MRP Controller 002 in the area of responsibility.

## Connections
- part-of :: [[_cluster]]
- related-to :: [[12-production-and-manufacturing/test-script-planning-and-production-in-other-plant-consumer-products-7]]
- related-to :: [[12-production-and-manufacturing/test-script-sap-s-4hana-cloud-public-edition-predictive-material-and-r]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/J44_S4CLD2608_BPD_EN_AE.docx` — full document · extracted with `mammoth` · 92,400 chars in the whole document
