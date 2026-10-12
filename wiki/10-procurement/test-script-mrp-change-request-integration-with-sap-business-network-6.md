---
id: 10-procurement/test-script-mrp-change-request-integration-with-sap-business-network-6
title: "Test Script: MRP Change Request Integration with SAP Business Network (65D_AE) (65D_S4CLD2608_BPD_EN_AE)"
description: "S/4HANA Cloud test script (scope 65D_AE) for MRP change requests negotiated with suppliers via SAP Business Network: prerequisites and test steps."
cluster: 10-procurement
tags: [kb/procurement, topic/business-network-supply-chain-collaboration]
aliases: [65D_S4CLD2608_BPD_EN_AE]
keywords: [Supply Chain Collaboration with SAP Business Network, mrp change requests, sap business network, mrp rescheduling check, supplier response, change request confirmation, planned independent requirements, purchasing info records, purchase orders, application jobs]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/65D_S4CLD2608_BPD_EN_AE.docx]
confidence: low
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-1151
topic: 10-procurement/business-network-supply-chain-collaboration
language: EN
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Test Script: MRP Change Request Integration with SAP Business Network (65D_AE) (65D_S4CLD2608_BPD_EN_AE)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/65D_S4CLD2608_BPD_EN_AE.docx`, extracted with `mammoth`. Grouped under **Supply Chain Collaboration with SAP Business Network** in Procurement. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

| <!-- image omitted: unnamed --> | Test ScriptSAP S/4HANA Cloud Public Edition - 19-06-26 |
| --- | --- |
|  | MRP Change Request Integration with SAP Business Network (65D_AE) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Table of Contents

[1 Purpose 3](#_Toc232858071)

[2 Prerequisites 4](#_Toc232858072)

[2.1 Additional Manual Configuration 4](#_Toc232858073)

[2.2 System Access 4](#_Toc232858074)

[2.3 Roles 4](#_Toc232858075)

[2.4 Master Data, Organizational Data, and Other Data 5](#_Toc232858076)

[2.5 Business Conditions 6](#_Toc232858077)

[2.6 Preliminary Steps 6](#_Toc232858078)

[2.6.1 Prerequisite for Material Requirements Planning (MRP) Change Request 7](#_Toc232858079)

[2.6.1.1 Assign Business User 7](#_Toc232858080)

[2.6.1.2 Create Purchasing Info Record 8](#_Toc232858081)

[2.6.1.3 Clear Planned Independent Requirements (PIRs) for Material TG0011 10](#_Toc232858082)

[2.6.1.4 Clear Purchase Requestions and Purchase Orders for Material TG0011 11](#_Toc232858083)

[3 Overview Table 13](#_Toc232858084)

[4 Test Procedure 15](#_Toc232858085)

[4.1 Material Requirements Planning (MRP) Change Request 15](#_Toc232858086)

[4.1.1 Create Purchase Order 15](#_Toc232858087)

[4.1.2 Manage Planned Independent Requirements (PIRs) for Material TG0011 16](#_Toc232858088)

[4.1.3 Schedule Material Requirements Planning (MRP) Rescheduling Check 18](#_Toc232858089)

[4.1.4 Create Material Requirements Planning (MRP) Change Requests 19](#_Toc232858090)

[4.1.5 Send Material Requirements Planning (MRP) Change Requests 20](#_Toc232858091)

[4.2 Manage Material Requirements Planning (MRP) Change Request in SAP Business Network 21](#_Toc232858092)

[4.3 Review Material Requirements Planning (MRP) Change Requests Based on Vendor’s Response 22](#_Toc232858093)

[4.4 Send Confirmation for Material Requirements Planning (MRP) Change Requests to Vendor 23](#_Toc232858094)

[4.5 Review Material Requirements Planning (MRP) Change Request Confirmation in SAP Business Network 25](#_Toc232858095)

## Purpose

Overview

In times of changing customer demands, the material planner must react regularly to changes suggested by the MRP situation (for example, already ordered purchase orders should be updated by changing the requested date or quantity). Because of the high number of orders per day addressed to many different suppliers, an automated solution is provided to negotiate the changes with the suppliers.

With the Create MRP Change Requests app, you can reschedule proposals coming from MRP, create MRP change requests, and transfer these change requests from SAP S/4HANA Cloud Public Edition to SAP Business Network for Supply Chain, which connects suppliers with the buying organization. The supplier can decide about an answer to the request (accept, reject, or new proposal), and can send the change request answer back to SAP S/4HANA Cloud Public Edition. The requests can finally be either applied or discarded. The supplier is also informed about the decision. If the requests are applied, the corresponding purchase order is automatically changed.

This document provides a detailed procedure for testing this scope item after solution activation, reflecting the predefined scope of the solution. Each process step, report, or item is covered in its own section, providing the system interactions (test steps) in a table view. Steps that are not in scope of the process but are needed for testing are marked accordingly. Project-specific steps must be added.

|  |
| --- |
| Note Values in this test script (decimal notation, date formats, and so on) are presented in U.S. standard notation. If your test system is set up to use a different notation, enter values as appropriate. |

## Prerequisites

This section summarizes all the prerequisites for conducting the test in terms of systems, users, master data, organizational data, other test data and business conditions.

### Additional Manual Configuration

Before you can test this scope item, you must have completed the additional configuration steps that are described in the Set-Up Instructions for this scope item. These configuration steps are specific for your implementation and include mandatory settings that are not delivered by SAP and must be created by you. For more information, follow the link to the document:

[Link to Set-Up Instructions](https://help.sap.com/docs/SAP_S4HANA_BEST_PRACTICES/3307a18fa7c78088e2b726500c7aff72)

### System Access

| System | Details |
| --- | --- |
| SAP S/4HANA Cloud Public Edition | Accessible via SAP Fiori launchpad. Your system administrator provides you with the URL to access the various apps assigned to your role. |
| SAP Business Network | Access your SAP Business Network supplier account on [supplier.ariba.com](https://supplier.ariba.com). Your system administrator provides you with logon data. |

### Roles

Create business roles using the following business role templates delivered by SAP and assign them to your individual test users.

Alternatively, if available, you can use the following spaces delivered by SAP. You create a space with pages containing predefined essential apps and assign it to the business role. You then assign this business role to your individual users.

For more information, refer to How to Create a Business Role from a Template in the [product assistance](https://help.sap.com/docs/SAP_S4HANA_CLOUD/53e36b5493804bcdb3f6f14de8b487dd/ec310a8b669a45ca898dc4dd91d97de2.html) for SAP S/4HANA Cloud Public Edition.

| Name (Role Template) | ID (Role Template) | Name (Launchpad Space) | ID (Launchpad Space) | Log On |
| --- | --- | --- | --- | --- |
| Material Planner - External Procurement | SAP_BR_MATL_PLNR_EXT_PROC | Material Planning - External Procurement | SAP_BR_MATL_PLNR_EXT_PROC |  |
| Master Data Specialist - Product Data | SAP_BR_PRODMASTER_SPECIALIST | Master Data - Products / Product Governance | SAP_BR_PRODMASTER_SPECIALIST / SAP_CMD_SPT_PR_GOV_PC |  |
| Purchaser | SAP_BR_PURCHASER | Purchasing / Sourcing and Contracting | SAP_MM_SPT_PURCHASING_PC / SAP_MM_SPT_SOURCING_PC |  |
| Administrator | SAP_BR_ADMINISTRATOR | Administration / Administration - Workforce Master Data / Administration - License Compliance / Administration - Data Management / Administration - Output Control | SAP_BR_ADMINISTRATOR / SAP_BUM_SPT_ADMINISTRATION_PC / SAP_EI_SPT_ADM_LC_PC / SAP_CA_SPT_TDR_PC / SAP_OC_SPT_ADMINISTRATION_PC |  |

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

Org. Data

| Master | Value | Details | Comments |
| --- | --- | --- | --- |
| Plant | 3310 | Plant 1 AE |  |
| Vendor | 33300002 | Domestic UAE Supplier 2 |  |
| Company Code | 3310 | Company Code 3310 |  |
| Purchasing Organization | 3310 | Purch. Org. 3310 |  |

For more information on creating these master data objects, see the following [Master Data Scripts (MDS)](https://help.sap.com/docs/s4hana-best-practices/s4cld2608-master-data)

Table 1: Master Data Script Reference

| Master Data ID | Description |
| --- | --- |
| BNF | Create Product Master of type "Trading Good" - MDS |

### Business Conditions

After completing the activities in this test case, you can continue testing the following business processes:

| Scope Item | Business Condition |
| --- | --- |
| J45 - Procurement of Direct Materials | A purchase requisition is created as part of the Procurement of Direct Materials (J44) test script. This purchase requisition is converted into a purchase order in the Procurement of Direct Materials (J45) process. |

### Preliminary Steps

In this section, you are provided a detailed step-by-step description of technical or other prerequisites.

#### Prerequisite for Material Requirements Planning (MRP) Change Request

##### Assign Business User

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This procedure describes how to assign a business user.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Logon | Log on to SAP Fiori launchpad as an Administrator. |  |  |
| 2 | Access App | Open the Maintain Business Users (F1303) app. | The Maintain Business Users screen is displayed. |  |
| 3 | Search for Business User | In the Search field, enter MATL_PLNR_EXT_PROC. Choose Go. | In the Business Users section, the MATL_PLNR_EXT_PROC user name is displayed. |  |
| 4 | Select Business User | Select the MATL_PLNR_EXT_PROC user name and choose Edit. | The Maintain Business User screen is displayed. |  |
| 5 | Check Assigned Business Role | In the Assigned Business Roles section, check whether the SAP_BR_PURCHASER business role is assigned. |  |  |
| 6 | Assign Business Role | In the Assigned Business Roles section, choose Add.In the Add Business Role dialog box, search for the SAP_BR_PURCHASER business role. From the search results list, select the SAP_BR_PURCHASER business role and choose OK.Choose Save. | The SAP_BR_PURCHASER business role is assigned to the MATL_PLNR_EXT_PROC user. |  |

##### Create Purchasing Info Record

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This procedure describes how to create the purchasing info record for the material/supplier combination.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Logon | Log on to SAP Fiori launchpad as an Purchaser. |  |  |
| 2 | Access App | Open the Manage Purchasing Info Records (F1982) app. | The Manage Purchasing Info Records screen is displayed. |  |
| 3 | Check Existing Purchasing Info Record | In the Material field, enter TG0011 and choose Go.If a purchasing info record for material TG0011 and supplier 33300002 is displayed in the search results list, select the purchasing info record.On the General Information tab, review the Available From: and Available to: fields. If you confirm this purchasing info record to be valid, you completed this procedure already. |  |  |
| 4 | Create New Purchasing Info Record | Note The following step are only required, if no purchasing info record for material TG0011 and supplier 33300002 exists.On the Manage Purchasing Info Records screen, choose Create. | The Purchasing Info Record screen is displayed. |  |
| 5 | Enter Purchasing Info Record Information | On the Header tab, enter the following data:Purchasing Info Record Category: Select Standard from the dropdown list.Purchasing Organization: 3310Supplier: 33300002Material: TG0011Plant: 3310Purchasing Group: 001On the General Information tab, enter the following data according to your business requirements:ExampleAvailable From: <Today>Available To: 31.12.9999On the Purchasing Data tab, enter the following data:Incoterm: EXWIncoterm Location 1: VENDOROn the Delivery and Quantity tab, enter the following data according to your business requirements:ExampleDelivery Time in Days: <Delivery Time in Days>Under Delivery Tolerance in %: 10.0Over Delivery Tolerance in %: 10.0Tax Code: <Input Tax Code>Tax Rate Valid From (if necessary): <Date>Note When the TDT (time dependent tax) is activated via SSCUI 101016 (Define Tax Codes for Sales and Purchases) for the country of the company code and the tax code that were entered, it's mandatory to enter a value in the Tax Rate Valid From field. If you enter the current date, it's adjusted to the validity start date of the tax code according to the settings of the SSCUI.Tax Country/Region (if necessary): <Country/Region>Order Unit: PCStandard Order Quantity: 10Goods-Receipt-Based Invoice Verification: Select the checkbox.No Evaluated Receipt Settlement: Select the checkbox.On the Conditions tab, choose Create. On the New Condition screen, enter the following data according to your business requirements:ExampleValid From: <Today>Valid To: 12.31.9999Amount: 30.00Pricing Unit: 1Currency: AEDChoose Apply. |  |  |
| 6 |  | Choose Create. | The purchasing info record is created. |  |

##### Clear Planned Independent Requirements (PIRs) for Material TG0011

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This procedure describes how to clear the planned independent requirements directly for material TG0011.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Logon | Log on to SAP Fiori launchpad as a Material Planner - External Procurement. |  |  |
| 2 | Access App | Open the Maintain PIRs (F3445) app. | The Maintain PIRs screen is displayed. |  |
| 3 | Check Default Area of Responsibility | Select the user icon or photo and choose App Settings. In the MRP Settings dialog box, choose Area of Responsibility.Ensure that only the plant/MRP controller combination with the following data is assigned:Plant Name: 3310 Plant 1 AEMRP Controller: 001MRP Controller Name: MRP Controller 001If this plant/MRP controller combination isn't assigned, enable this assignment in the AOR Status column. Disable the assignment of any other plant/MRP controller combination.Choose Back. |  |  |
| 4 | Search for Material TG0011 | On the Maintain PIRs screen, enter the following search criteria:Plant: 3310Period Indicator: Select Monthly(M) from the dropdown list.Version Active: Select all options from the dropdown list.In the search field, enter TG0011 and choose Go. | A search results list with materials is displayed. |  |
| 5 | Select Material TG0011 | Select material TG0011. Check whether a PIR already exists. Depending on your check, choose one of the following options:If a PIR exists, you completed this procedure already.If no PIR exists, continue with the following steps. |  |  |
| 6 | Clear PIRs | Choose Edit. In the Planning Data table, set the value in the PIRs column to 0. | For future periods the PIRs are cleared. |  |
| 7 | Save Your Entries | To save your changes, choose Save. | The cleared PIRs for material TG0011 are saved. |  |

##### Clear Purchase Requestions and Purchase Orders for Material TG0011

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This procedure describes how to clear purchase requisitions and purchase orders for material TG0011.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Logon | Log on to SAP Fiori launchpad as a Material Planner - External Procurement. |  |  |
| 2 | Access App | Open the Manage Material Coverage - New Version (F0251A) app. | The Find Material dialog box is displayed. |  |
| 3 | Select Material and Show Shortages | In the Find Material dialog box, enter the following data:ExampleMaterial: TG0011Tip You can use the Value Help (  ) to select a value.Plant: 3310From the dropdown list, select a plant.Shortage Definition: MRP StandardFrom the dropdown list, select a plant.Choose OK. | The Material Details screen is displayed. |  |
| 4 | Clear Existing MRP Element | On the Stock / Requirements List tab, navigate to the existing MRP element and select Delete from the dropdown list in the Actions column to clear it. | The selected MRP element is cleared. |  |

## Overview Table

|  |
| --- |
| Note If your system administrator has enabled spaces and pages on the SAP Fiori launchpad, the homepage will only contain the essential apps for performing the typical tasks of a business role.You can find all other (searchable) apps not included on the homepage using the search bar ([2434549](https://me.sap.com/notes/2434549)).If you want to personalize the homepage and include the hidden apps, navigate to your user profile and choose App Finder. |

| Process Step | Business Role | Transaction/App | Expected Results |
| --- | --- | --- | --- |
| [Create Purchase Order](#unique_14) [page ] 15 | Material Planner - External Procurement | Manage Material Coverage - New Version (F0251A) | You've created a purchase order for material TG0011. |
| [Manage Planned Independent Requirements (PIRs) for Material TG0011](#unique_15) [page ] 16 | Material Planner - External Procurement | Maintain PIRs (F3445) | You've created the planned independent requirements directly for material TG0011. |
| [Schedule Material Requirements Planning (MRP) Rescheduling Check](#unique_16) [page ] 18 | Material Planner - External Procurement | Schedule MRP Rescheduling Checks (F5417) | You've identified the MRP exceptions and how to schedule the MRP rescheduling check to collect MRP rescheduling information. |
| [Create Material Requirements Planning (MRP) Change Requests](#unique_17) [page ] 19 | Material Planner - External Procurement | Create MRP Change Requests (F5416) | You've created MRP change requests for material TG0011. |
| [Send Material Requirements Planning (MRP) Change Requests](#unique_18) [page ] 20 | Material Planner - External Procurement | Create MRP Change Requests (F5416) | You've manually set the MRP change requests status to Requested and how to review the detailed requested MRP change requests for material TG0011. |
| [Manage Material Requirements Planning (MRP) Change Request in SAP Business Network](#unique_19) [page ] 21 | Supplier | SAP Business Network on [supplier.ariba.com](https://supplier.ariba.com) | You've manually managed the MRP change requests from SAP S/4HANA Cloud Public Edition in SAP Business Network and how to review the detailed requested MRP change requests for material TG0011. |
| [Review Material Requirements Planning (MRP) Change Requests Based on Vendor’s Response](#unique_20) [page ] 22 | Material Planner - External Procurement | Create MRP Change Requests (F5416) | You've reviewed the vendor's response to your MRP change request for material TG0011. |
| [Send Confirmation for Material Requirements Planning (MRP) Change Requests to Vendor](#unique_21) [page ] 23 | Material Planner - External Procurement | Schedule Sending MRP Change Requests (F5418) | You've scheduled the Sending of MRP Change Request application job for material TG0011 to send the confirmation to the vendor. |
| [Review Material Requirements Planning (MRP) Change Request Confirmation in SAP Business Network](#unique_22) [page ] 25 | Supplier | SAP Business Network on [supplier.ariba.com](https://supplier.ariba.com) | You've reviewed the vendor's response to your material requirements planning (MRP) change request. |
| [Send Confirmation for Material Requirements Planning (MRP) Change Requests to Vendor](#unique_21) [page ] 23 | Material Planner - External Procurement | Schedule Sending MRP Change Requests (F5418) | The status of your application job is refreshed. The Sending of MRP Change Request application job is in status Finished. |
| [Review Material Requirements Planning (MRP) Change Request Confirmation in SAP Business Network](#unique_22) [page ] 25 | Supplier | SAP Business Network on [supplier.ariba.com](https://supplier.ariba.com) | In the Customer Response column, the customers response is displayed. |

## Test Procedure

The test procedure covers the MRP procedure for material (TG0011) without scheduling agreement.

### Material Requirements Planning (MRP) Change Request

#### Create Purchase Order

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This procedure describes how to create a purchase order for material TG0011.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Logon | Log on to SAP Fiori launchpad as a Material Planner - External Procurement. |  |  |
| 2 | Access App | Open the Manage Material Coverage - New Version (F0251A) app. | The Find Material dialog box is displayed. |  |
| 3 | Select Material TG0011 | In the Find Material dialog box, enter the following data:Material: TG0011Plant: 3310Shortage Definition: Select MRP Standard from the dropdown list.Choose OK. | The Material Details screen is displayed. |  |
| 4 | Create Purchase Requisition | In the Material Details section , choose Create Order.In the Create Order dialog box, enter the following data according to your business requirements:ExampleReceipt Quantity: <Receipt Quantity> PCAvailability Date: <Current + 2 Month>Source of Supply: Info Record <Info Record Number>Note You can use the Value Help to select the source of supplier for order.Choose Create. | The purchase requisition is created. |  |
| 5 | Convert Purchase Requisition into Purchase Order | In the Stock/Requirements List table, purchase requisitions are labeled as PurReqs in the MRP Element column. For each PurReqs MRP element, select the Dropdown (  ) icon in the Actions column and choose Convert.In the Change Purchase Requisition XXXXXXXX-XX dialog box, review the information and choose OK. Note down the purchase order number. | The purchase requisition is converted to a purchase order. |  |

#### Manage Planned Independent Requirements (PIRs) for Material TG0011

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This procedure describes how to create the planned independent requirements directly for material TG0011.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Logon | Log on to SAP Fiori launchpad as a Material Planner - External Procurement. |  |  |
| 2 | Access App | Open the Maintain PIRs (F3445) app. | The Maintain PIRs screen is displayed. |  |
| 3 | Check Default Area of Responsibility | Select the user icon or photo and choose App Settings. In the MRP Settings dialog box, choose Area of Responsibility.Ensure that only the plant/MRP controller combination with the following data is assigned:Plant Name: 3310 Plant 1 AEMRP Controller: 001MRP Controller Name: MRP Controller 001If this plant/MRP controller combination isn't assigned, enable this assignment in the AOR Status column. Disable the assignment of any other plant/MRP controller combination.Choose Back. |  |  |
| 4 | Search for Material TG0011 | On the Maintain PIRs screen, enter the following search criteria:Plant: TG0011Period Indicator: Select Monthly(M) from the dropdown list.Version Active: Select all options from the dropdown list.In the search field, enter TG0011 and choose Go. | A search results list with materials is displayed. |  |
| 5 | Select Material TG0011 | Select material TG0011 and choose Edit. |  |  |
| 6 | Edit PIRs for Material TG0011 | In the Maintain Quantities per Period table, enter the following data according to your business requirements:Tip To enter data for several periods, choose Mass Maintenance.ExampleVersion is Active: YES<Time Period>: 200 (as proposed quantity)Choose Save. | The purchasing info records (PIRs) are saved. |  |

#### Schedule Material Requirements Planning (MRP) Rescheduling Check

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This procedure describes how to identify the MRP exceptions and how to schedule the MRP rescheduling check to collect MRP rescheduling information.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Logon | Log on to SAP Fiori launchpad as a Material Planner - External Procurement. |  |  |
| 2 | Access App | Open the Schedule MRP Rescheduling Checks (F5417) app. | The Application Jobs screen is displayed. |  |
| 3 | Create New Job | On the Application Jobs screen, choose Create. The New Job: MRP Rescheduling Checks screen is displayed.In the 1. Template Selection section, enter the following data:Job Template: Select MRP Rescheduling Checks from the dropdown list.Job Name: <MRP Rescheduling Checks for TG0011>Choose Step 2.In the 2. Scheduling Options section, enter the following data:Start Immediately: Select the checkbox.Choose Define Recurrence Pattern.In the Scheduling Information, enter the following data:Start Immediately: Select the checkbox.Recurrence Pattern: Select Single Run from the dropdown list.Choose OK.Choose Step 3.In the 3. Parameters section, enter the following data:MRP Plant: 3310MRP Controller: 001Material: TG0011Choose Check > Schedule . | The Job MRP Rescheduling Check has been scheduled is displayed.You're forwarded to the Application Jobs screen. In the Jobs table, the application job that you've created is displayed in status In Process. |  |
| 4 | Refresh Application Jobs List | To refresh and check the status of the application job that you've created, choose Go. | In the Jobs table, the status of your application job is changed to Finished. |  |
| 5 | Verify Application Job Results | To review and verify the results of your application job, choose the Job Results (  ) icon in the Results column. | The Document (<ID>) screen is displayed. For the item with material TG0011 the Reschedule in exception message is displayed. |  |

#### Create Material Requirements Planning (MRP) Change Requests

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This procedure describes how to create MRP change requests for material TG0011.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Logon | Log on to SAP Fiori launchpad as a Material Planner - External Procurement. |  |  |
| 2 | Access App | Open the Create MRP Change Requests (F5416) app. | The Create MRP Change Requests screen is displayed. |  |
| 3 | Select Material and Show Purchase Order Schedule Lines | In the Material field, enter TG0011. Choose Go. | The Purchase Order Schedule Lines table is displayed. For the material TG0011 related purchase order item, the Requested Date/Requested Quantity column and the Request Status column are empty. |  |
| 4 | Create Change Requests | Select the purchase order schedule line and choose Create Change Requests. | The Change requests for the record created successfully. system message is displayed.The Requested Date/Requested Quantity column and the Request Status column are updated. In the Request Status column, the status changes to New. |  |

#### Send Material Requirements Planning (MRP) Change Requests

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This procedure describes how to manually set the MRP change requests status to Requested and how to review the detailed requested MRP change requests for material TG0011.

|  |
| --- |
| Note If you've already set up the Manufacturing - MRP Change Request Integration (SAP_COM_0667) communication scenario, this procedure can also be done automatically using the Create MRP Change Requests (F5416) app. |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Logon | Log on to SAP Fiori launchpad as a Material Planner - External Procurement. |  |  |
| 2 | Access App | Open the Create MRP Change Requests (F5416) app. | The Create MRP Change Requests screen is displayed. |  |
| 3 | Search for Created MRP Change Request | On the Create MRP Change Requests screen, enter the required search criteria to search for the MRP change request that you've created in [Create Material Requirements Planning (MRP) Change Requests](#unique_17) [page ] 19. | In the Purchase Order Schedule Lines table, the newly created MRP change requests are displayed. |  |
| 4 | Send Change Request | Select a purchase order schedule line and choose Send Change Requests. | The Change request send successfully system message is displayed. |  |

### Manage Material Requirements Planning (MRP) Change Request in SAP Business Network

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This procedure describes how to manually manage the MRP change requests from SAP S/4HANA Cloud Public Edition in SAP Business Network and how to review the detailed requested MRP change requests for material TG0011.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Logon | Log on to SAP Business Network as a Supplier on [supplier.ariba.com](https://supplier.ariba.com). | The Home screen is displayed. |  |
| 2 | Select MRP Change Request | In the search bar, select the Orders and Releases from the dropdown list. | The Ariba Network Workbench screen is displayed. |  |
| 3 | Search for Order Number | On the Workbench screen, select the first order change request. | The List Order Change Requests is displayed. |  |
| 4 | Select Order Change Request | Select the order that was sent from the SAP S/4HANA Cloud Public Edition system and review all the details.Choose either Accept, Reject, or Propose.If you chose Propose, enter the following data:Supplier Proposed Delivery Date: <Delivery Date>Supplier Proposed Quantity: <Quantity>Comment: Optionally, enter a comment and choose Apply.Other: Select Estimated Amount and enter a value. |  |  |
| 5 | Review and Submit Change Request | On the Review Change Request screen, add a comment and choose Submit. | The change request is submitted by the supplier.If you chose Reject, enter the rejection code. |  |

### Review Material Requirements Planning (MRP) Change Requests Based on Vendor’s Response

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This procedure describes how to review the vendor's response to your MRP change request for material TG0011.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Logon | Log on to SAP Fiori launchpad as a Material Planner - External Procurement. |  |  |
| 2 | Access App | Open the Create MRP Change Requests (F5416) app. | The Create MRP Change Requests screen is displayed. |  |
| 3 | Select Material and Show Purchase Order Schedule Lines | In the Material field, enter TG0011. Choose Go. | The Purchase Order Schedule Lines table is displayed for material TG0011. |  |
| 4 | Select the Request Status field | In the Request Status field, choose Answered from the drop-down. | The Purchase Order Schedule Lines table with the request answers is displayed for material TG0011. |  |
| 5 | React to Vendor’s Response | On the Purchase Order Schedule Lines tab, choose one of the following options depending on the vendor's response:Accepted: Choose Apply Change Requests.Rejected: Choose Discard Change Requests.New Proposal: Choose Answered.On the Change Request Detail screen, review the proposal. Choose Back and review the supplier's new proposal in the New Proposal quick view. Choose Apply Change Request. | Based on your action, the status of the change request is Applied, Discarded. |  |

### Send Confirmation for Material Requirements Planning (MRP) Change Requests to Vendor

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This procedure describes how to schedule an application job to send the confirmation for the MRP change request to the vendor.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Logon | Log on to SAP Fiori launchpad as a Material Planner - External Procurement. |  |  |
| 2 | Access App | Open the Schedule Sending MRP Change Requests (F5418) app. | The Application Jobs screen is displayed. |  |
| 3 | Create a New Job | On the Application Jobs screen, choose Create.The New Job: Sending of MRP Change Requests screen is displayed.In the 1. Template Selection section, enter the following data:Job Template: Sending of MRP Change RequestsJob Name: <Sending of MRP Change Requests>Choose Step 2.In the 2. Scheduling Options section, enter the following data:Start Immediately: Select the checkbox.Choose Define Recurrence Pattern.In the Scheduling Information dialog box, enter the following data:Start Immediately: Select the checkbox.Recurrence Pattern: Select Single Run from the dropdown list.Choose OK.Choose Step 3.In the 3. Parameters section, select the Confirmations radio button and enter the following data according to your business requirements:MRP Plant: <MRP Plant>MRP Area: <MRP Area>Material: <Material>Purchase Order: <Purchase Order>Purchase Order Item: <Purchase Order Item>In the Sending Status field, use the Value Help (  ) to select the U (Unprocessed) option.Choose Check > Schedule . | Your application job has been scheduled.On the Application Jobs screen, the application job that you've created is displayed in status In Process. |  |
| 4 | Check the Status | On the Application Jobs screen, choose Go. | The status of your application job is refreshed. The Sending of MRP Change Request application job is in status Finished. |  |

### Review Material Requirements Planning (MRP) Change Request Confirmation in SAP Business Network

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This procedure describes how to review the MRP change request confirmation in SAP Business Network.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Logon | Log on to SAP Business Network as a Supplier on [supplier.ariba.com](https://supplier.ariba.com). | The Home screen is displayed. |  |
| 2 | Select MRP Change Request | In the search bar, select Order Change Request from the dropdown list. | The Ariba Network Workbench screen is displayed. |  |
| 3 | Search for Order Number | On the Workbench screen, select the first order change request. | The List Order Change Requests is displayed. |  |
| 4 | Select Order Change Request | Select the order that was sent from the SAP S/4HANA Cloud Public Edition system and review all the details. | In the Customer Response column, the customers response is displayed. |  |

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
> Flagged while digesting this document, not verified: The Clear PIRs procedure says 'If a PIR exists, you completed this procedure already' and only continues to clear PIRs (set to 0) when no PIR exists, which inverts the stated purpose of clearing existing PIRs.

## Connections
- part-of :: [[_cluster]]
- related-to :: [[10-procurement/test-script-supply-chain-automation-with-sap-business-network-5i2-ae-1]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/65D_S4CLD2608_BPD_EN_AE.docx` — full document · extracted with `mammoth` · 41,398 chars in the whole document
