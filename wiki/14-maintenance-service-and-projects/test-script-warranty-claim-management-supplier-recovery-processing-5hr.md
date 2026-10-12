---
id: 14-maintenance-service-and-projects/test-script-warranty-claim-management-supplier-recovery-processing-5hr
title: "Test Script: Warranty Claim Management – Supplier Recovery Processing (5HR_AE) (5HR_S4CLD2608_BPD_EN_AE)"
description: "SAP S/4HANA Cloud Public Edition 2608 (AE) test script for scope item 5HR: supplier warranty claims from creation to posting, rejection, closing and reopening."
cluster: 14-maintenance-service-and-projects
tags: [kb/maintenance-service-and-projects, topic/warranty-claim-management]
aliases: [5HR_S4CLD2608_BPD_EN_AE]
keywords: [Warranty Claim Management, supplier claims, supplier recovery, master warranty, vendor warranty, claim validation, supplier response, claim posting, claim lifecycle, return parts status]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/5HR_S4CLD2608_BPD_EN_AE.docx]
confidence: low
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-1101
topic: 14-maintenance-service-and-projects/warranty-claim-management
language: EN
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Test Script: Warranty Claim Management – Supplier Recovery Processing (5HR_AE) (5HR_S4CLD2608_BPD_EN_AE)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/5HR_S4CLD2608_BPD_EN_AE.docx`, extracted with `mammoth`. Grouped under **Warranty Claim Management** in Maintenance, Service and Projects. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

|  |  |
| --- | --- |
| Warranty Claim Management – Supplier Recovery Processing (5HR_AE)Purpose PUBLIC 1<!-- image omitted: unnamed --> | Test ScriptSAP S/4HANA Cloud Public Edition - 19-06-26 |
|  | Warranty Claim Management – Supplier Recovery Processing (5HR_AE) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Table of Contents

[1 Purpose 3](#_Toc232857194)

[2 Prerequisites 4](#_Toc232857195)

[2.1 System Access 4](#_Toc232857196)

[2.2 Roles 4](#_Toc232857197)

[2.3 Master Data, Organizational Data, and Other Data 5](#_Toc232857198)

[2.4 Business Conditions 7](#_Toc232857199)

[2.5 Preliminary Steps 7](#_Toc232857200)

[2.5.1 Create Master Warranty 8](#_Toc232857201)

[2.5.2 Maintain Equipment Data and Assign Vendor Warranty 9](#_Toc232857202)

[2.5.3 Maintain Supplier Data (Optional) 10](#_Toc232857203)

[2.5.4 Check Price Condition Records 10](#_Toc232857204)

[2.5.5 Check General Ledger (GL) Account Assignment 12](#_Toc232857205)

[2.5.6 Manage Default Account Assignment 12](#_Toc232857206)

[3 Overview Table 14](#_Toc232857207)

[4 Test Procedures 15](#_Toc232857208)

[4.1 Create Supplier Claim 15](#_Toc232857209)

[4.2 Validate Supplier Claim 17](#_Toc232857210)

[4.3 Adjust Supplier Claim 18](#_Toc232857211)

[4.4 Send to Supplier 19](#_Toc232857212)

[4.5 Maintain Supplier Response 21](#_Toc232857213)

[4.6 Post Supplier Claim 22](#_Toc232857214)

[4.7 Reverse Claim Posting 23](#_Toc232857215)

[4.8 Reject Supplier Claim 24](#_Toc232857216)

[4.9 Cancel Supplier Claim 25](#_Toc232857217)

[4.10 Close Supplier Claim 26](#_Toc232857218)

[4.11 Reprocess Rejected Supplier Claim 27](#_Toc232857219)

[4.12 Reopen Supplier Claim 28](#_Toc232857220)

## Purpose

Overview

This scenario enables you to create a warranty claim that can then be forwarded to the respective supplier for a reimbursement. The scenario covers the relevant steps starting with the creation of a claim (based on a performed repair), continuing with the validation for completeness, eligibility for reimbursement, and the finding of the correct prices for material, labor activities, and so on.

Once the information is sent to the supplier and their response is received, the scenario supports the transparent maintenance of values and the posting of the negotiated amount.

This document provides a detailed procedure for testing this scope item after solution activation, reflecting the predefined scope of the solution. Each process step, report, or item is covered in its own section, providing the system interactions (test steps) in a table view. Steps that are not in scope of the process but are needed for testing are marked accordingly. Project-specific steps must be added.

|  |
| --- |
| Note Values in this test script (decimal notation, date formats, and so on) are presented in U.S. standard notation. If your test system is set up to use a different notation, enter values as appropriate. |

## Prerequisites

This section summarizes all prerequisites to conducting the test in terms of systems, users, master data, organizational data, other test data and business conditions.

### System Access

| System | Details |
| --- | --- |
| System | Accessible via SAP Fiori launchpad. Your system administrator provides you with the URL to access the various apps assigned to your role. |

### Roles

Assign the following business roles to your individual test users.

|  |
| --- |
| Note The following roles are provided as example roles from SAP. You can use these as templates to create your own roles. |

For more information on business roles, refer [How to Create a Business Role for the Administrator](https://help.sap.com/viewer/a630d57fc5004c6383e7a81efee7a8bb/2105.500/en-US/8fa28e0107984d42a99b9eea67856cea.html) and Assigning Roles to a User in the [Administration Guide](https://help.sap.com/viewer/S4HANA2020_AdminGuide).

Table 1: Roles

| Business Role | Object | Application Name |
| --- | --- | --- |
| SAP_BR_MAINTENANCE_PLANNER | EquipmentFunctional Location | Create/Change and Display Technical Objects |
| SAP_BR_BUPA_MASTER_SPECIALIST | SupplierCustomer | Manage Supplier Master DataManage Customer Master Data |
| SAP_BR_CLAIMS_ANALYST_COMPL | Claim | Manage Supplier Claims |
| SAP_BR_PRODMASTER_SPECIALIST | Material | Manage Product Master Data |
| SAP_BR_MD_SPECIALIST_WRNTY | Warranty Master Data | Manage Master WarrantiesCreate Pricing Condition RecordsChange Pricing Condition RecordsDisplay Pricing Condition Records |
| SAP_BR_PRICING_SPECIALIST | Pricing Condition | Set Material Prices - Sales |

|  |
| --- |
| Note You need to maintain master data (equipment/functional location/supplier/material and pricing condition records) used within the warranty claims while navigating to the individual applications with the relevant business user in the cloud system. |

### Master Data, Organizational Data, and Other Data

The organizational structure and master data of your company has been created in your system during activation. The organizational structure reflects the structure of your company. The master data represents materials, customers, and suppliers, for example, depending on the operational focus of your company.

|  |
| --- |
| Caution Update Behavior of Predelivered Demo DataIn non-productive environments (such as starter systems, sandbox systems, or partner demo systems), SAP initially deploys demo data for your selected scope. You can use this data to test and evaluate business processes.In a customer system, you can receive new or updated demo data after initial activation with further scope enhancements, provided the existing demo data wasn't changed in an incompatible way. If activation errors occur due to incompatible changes in demo data, you're responsible for resolving them. If you don't resolve the errors within a specific time frame, SAP reserves the right to deactivate demo data in your systems. In this case, you can continue by creating your own demo data. Alternatively, you can request that your systems be reprovisioned if you want to work with predelivered demo data again.In partner systems, you can use the demo data deployed with the initial activation. No additional demo data will be deployed in the system with scope enhancements. You can only create additional demo data manually. |

Use your own master data or the following sample data to go through the test procedure.

For more information on creating master data objects, see the following [Master Data Scripts (MDS)](https://help.sap.com/docs/s4hana-best-practices/s4cld2608-master-data) .

Business Partner

Table 2:

| Data | Sample Value | Details |
| --- | --- | --- |
| Supplier | 33300010. (For Public Sector Management (PSM), use 33300001) | Local Supplier |

Organizational Unit

Table 3:

| Data | Sample Value | Details | Comments |
| --- | --- | --- | --- |
| Company Code | 3310 | Company Code 3310 | Appropriate Master Data Script (MDS): J56, J57, J47 |
| Sales Organization | 3310 | Dom. Sales Org |  |
| Distribution Channel | 10 | Direct Sales |  |
| Division | 00 | Product Division 00 |  |
| Purchasing Organization | 3310 | Purch. Org. 3310 |  |
| Plant | 3310 | Plant 1 AE | Appropriate Master Data Script (MDS): BFL |
| Person Responsible |  | Authorized business user who is responsible for claims.Note The email address of receipt needs to be maintained within the Output Parameter Determination page. If not, the email address is retrieved from the business partner address data. | How Employee Master Data can be maintained in SAP S/4HANA Cloud Public Edition: Master data script 47Y Create Employee Master Data for Service [https://s4hanacloud.community.sap/blogs/show/ONDHRzuhvLKHJFO1KmxKhB](https://s4hanacloud.community.sap/blogs/show/ONDHRzuhvLKHJFO1KmxKhB). |
| Currency | AED | UAE Dirham |  |

Master Data

| Data | Product Sample | Details | Comments |
| --- | --- | --- | --- |
| Product | TG0011SRV_01 (Optional) | Trading Good 0011,PD,Regular Proc.Service | Appropriate Master Data Script (MDS): BNF |
| EquipmentNote If you choose Functional Location as the object type, the number will be different. But, the procedure or steps to be performed remains the same. | 233100001(For Public Sector Management, use 217100001)217100002 | Manual Isolation ValveControl Valve | Refer [Create and Maintain Technical Objects (Equipment) (Optional)](https://help.sap.com/viewer/DRAFT/43f8e55f80e127ec4c48649b4186bde5/2108_DEV/en-US/e20dab5c98cd4895b0e866a457de5a6f.html). |

For more information on creating master data scripts, see the following Master Data Scripts (MDS):

Table 4: Master Data Script Reference

| Master Data ID | Description |
| --- | --- |
| 3KV | Create Service Product of Type |
| 2J7 | Create Product Master of Type |
| 31X | Create Product Master of Type |
| BNE | Create Supplier Master |
| 5MF | Create Equipment |
| 5LM | Create Functional Location |
| BNF | Create Product Master of Type |
| 31Y | Create Product Master of Type |

### Business Conditions

Before you test this scope item, the following business condition must be met.

| Scope Item ID | Business Condition |
| --- | --- |
| 1LQ - Output Management | This scope item provides best practice information for SAP S/4HANA output management that can be used to implement business scenarios that include output-related tasks.Note The settings for warranty claim management, that is, application object types WARRANTY_CLAIM and WARRANTY_CLAIM_CUSTOMER must be maintained. |

### Preliminary Steps

Create Master Warranty

Prerequisites

- Relevant master data: Organizational details, Supplier, Equipment and Material
- A valid claim should exist
- The role SAP_BR_MD_SPECIALIST_WRNTY should be assigned

Procedure

1. Log into the application with a registered user.
2. Open the application.
3. Create a master warranty without entering any values in the mandatory field.
4. Enter values in the following fields:
    - Description
    - Master Warranty
    - Warranty Type
    - Customer Warranty
    - Vendor/Customer Warranty
5. Validate item creation, warranty creation without adding the item, match ALL/ANY option, and warranty counter without entering warranty counter, counter description, counter value, and counter unit of measure.

#### Create Master Warranty

A warranty is a commitment from a manufacturer, vendor, or salesperson to a customer that a product has no defects, and that services such as repairs and partial or com-plete exchange of defective parts are guaranteed for a particular period of time. Repairs or exchanges will be made if the product does not function as originally described or intended, without the customer being billed. A vendor warranty is a commitment that is made by the vendor or supplier to your company.

Prerequisites

- Relevant master data which is valid organizational details, supplier, equipment, and material
- Roles SAP_BR_MD_SPECIALIST_WRNTY should be assigned
- Below counters should exist:
    - WARRANTY_DISTANCE_KM (Counter for distance in kilometer)
    - WARRANTY_DISTANCE_MI (Counter for distance in miles)
    - WARRANTY_OPERATING_HOURS (Counter for operating hours)
    - WARRANTY_PERIOD (Counter for time period)

Procedure

1. Log on to the SAP Fiori launchpad as a warranty specialist.
2. Open the Manage Master Warranties application.
3. Choose Create.
4. On the Header tab, enter values in the following fields:
    - Description: for example, <VW Isolation Valve 24 Months>
    - Warranty Type: Vendor/Manufacturer Warranty
5. On the , choose Create to create a new item.
6. On the Header tab, enter values in the below field:
    - Description: for example, <Isolation Valve 24 Months>
7. On the Warranty Counter, choose Add Counter and enter values in the following fields:
    - Counter: WARRANTY_PERIOD
    - Counter Value: 24(MON)

Choose Add.

1. Choose Apply and Create.

#### Maintain Equipment Data and Assign Vendor Warranty

A warranty is a commitment from a manufacturer, vendor, or salesperson to a customer that a product has no defects, and that services such as repairs and partial or complete exchange of defective parts are guaranteed for a particular period of time, without the customer being billed.

The warranty claim process supports and integrates warranties that are based on dates (warranty period).

To create and/or maintain equipment, perform the steps from the master data scripts (MDS) 3U3. For more information on creating master data objects, see the following [Master Data Scripts (MDS)](https://help.sap.com/docs/s4hana-best-practices/s4cld2608-master-data) .

Maintain Equipment Data

Use the below steps to maintain equipment data within the warranty claim.

1. Log onto the SAP Fiori launchpad with the role, .
2. Navigate to the Change Technical Object application.
3. Enter equipment number as the technical object and choose Continue.
4. Verify the acquisition date that displays as registration date within the Manage Supplier Claims application.
5. Verify the vendor warranty start date and assign master warranty.

|  |
| --- |
| Note These dates should be maintained so that the respective equipment can be used in the warranty claim. If the equipment is not maintained, the claim validation fails.To Manage Supplier Claims application, Log on to the SAP Fiori launchpad as a Claims Analyst. |

Maintain Vendor Warranty

Vendor warranty: A commitment, that is made by the vendor or supplier to your company.

If you have entered the start date and assign master warranty of an equipment, the system checks the validity of the claim. Before you use the warranty for individual objects within your claim process, you need to enter the warranty start date and assign master warranty in the equipment master data.

1. Log onto the SAP Fiori launchpad with the role, MAINTENANCE_PLANNER.
2. Navigate to the Change Technical Object application.
3. Enter your equipment number (for example,233100001) as the technical object and choose Continue.
4. Verify the acquisition date that displays as registration date within the Manage Supplier Claims application.
5. Verify the vendor warranty start date and assign master warranty for validating the supplier claim.

These dates should be maintained so that the respective equipment can be maintained in the warranty claim. If the equipment is not maintained with valid master warranty and acquisition date, then the claim validation fails.

#### Maintain Supplier Data (Optional)

In the warranty claim process, a partner is used to derive the correct prices, post the amount to accounting, and identify where the claim statement should be send to. The claim analyst can use the below steps to maintain the customer and supplier (vendor) data.

Prerequisites

Below are the relevant business partner roles for the supplier to be used within the Manage Claims application:

- Customer role (sales view)
- Customer role F1 (Company code view)
- Vendor role
- Vendor role F1 (Company code view)

Procedure

Maintain Customer Data

1. Log onto the SAP Fiori launchpad with the role as a Business Partner Master Data Specialist.
2. Open Maintain Business Partner application.
3. Enter the business partner and choose Start.
4. In the result list, double click the business partner 33300010.
5. Select from the Display in BP Role dropdown.
6. Notice that for the business partner roles are assigned and created to maintain supplier data.

#### Check Price Condition Records

Determining the correct prices is a central element within the warranty claim processing. To ensure that the appropriate amount can be claimed from the supplier, the correct prices need to be set up in the system. Each of the different item types (material, labor, sublet) has its own condition to ensure proper maintenance and relationship to the already existing pricing records.

Procedure - For Material

1. Log onto the SAP Fiori launchpad with the role, SAP_BR_PURCHASER as a Purchaser.
2. Open Create Price Conditions - Purchasing (MEK1).
3. Enter condition Type, PPR0 (Gross Price) and press Enter.
4. Choose key combination and choose Choose.
5. Enter values:
    - Supplier: 33300010
    - Purch. Organization:3310
    - Material:TG0011

Ensure that the flag for field Cond. marked for deletion is deselcted.

1. Choose Execute and verify the condition record for the material.
2. Continue with the following steps only when the message shows No Condition records exist for this selection.
3. Choose Condition > Create.
4. Enter values and press Enter.
    - Infotype: 0
    - Amount: <any amount>
    - Unit: <enter a currency>, for example, AED
5. Choose Save.

Procedure - For Labor (Optional)

|  |
| --- |
| Note Follow these steps only when you have a service material, such as SRV_01 |

1. Log onto the SAP Fiori launchpad with the role, SAP_BR_MD_SPECIALIST_WRNTY, as a Master Data Specialist - Warranty Management.
2. Open Display Pricing Condition Records - Warranty Claim Processing (WYP3).
3. Enter condition type PBF0 (Labor Rate) and press Enter.
4. Choose key combination and choose Choose.
5. Enter values:
    - Plant: 3310
    - Material: SRV_01

Ensure that the flag for field Cond.marked for deletion is not set.

1. Choose Execute and verify the condition record for the service material.
2. Continue with the following steps only when the message shows No Condition records exist for this selection.
3. Choose Menu > Condition > Create.
4. Enter values and press Enter.
    - Material: SRV_01
    - Amount: <any amount>
    - Unit: <enter a currency>, for example, AED
5. Choose Save.

|  |
| --- |
| NotePPRO is the reference condition type of PBF0 (Purchasing Price) which is used in the pricing procedure of the supplier warranty claim.The sublet items are always manually entered in the claim. Therefore, no pricing records need to be set up as preliminary step. |

#### Check General Ledger (GL) Account Assignment

As a claim analyst, you can use the below procedure to set up the general ledger (GL) accounts.

Procedure

1. Log onto the SAP Fiori Launchpad with the role SAP_BR_BPC_EXPERT.
2. Navigate to the Manage Your Solution (F1241) application.
3. Click Configure Your Solution.
4. Select from the Application Area and from the Sub Application area.
5. Select from the list provided below.
6. Within the configuration steps, click Configure against .
7. Choose the following:
    - Area: warranty from the dropdown
    - Chart of Accounts: YCOA
    - Condition Tables: 021 and 022
8. Click Step to move to Account Assignment tab.

For example:

-
    - Condition type: KOFS
    - Company Code: 3310
    - Account Key: ERL
    - GL Account: 41090000
    - Accruals Account: 11008030

1. Choose the item and click Review and then save.

#### Manage Default Account Assignment

As a claim analyst, you can use the below procedure to set up default general ledger (GL) accounts.

Procedure

1. Log on to the SAP Fiori Launchpad with role SAP_BR_BPC_EXPERT.
2. Navigate to the Manage Your Solution (F1241) application.
3. Click Configure Your Solution.
4. Select Finance from the Application Area and General Settings from the Sub Application area.
5. Select Journal Entries from the list provided below.
6. Within the configuration steps, click Configure against Manage Default Account Assignment (102639).
7. Click New Entries and enter values:
    - CoCd: 3310
    - Cost Elem.: 65008600
    - Cost Ctr: 33101101
8. Click Save.

## Overview Table

This scope item consists of several process steps that are listed in the following table:

|  |
| --- |
| Note If your system administrator has enabled spaces and pages on the SAP Fiori launchpad, the homepage will only contain the essential apps for performing the typical tasks of a business role.You can find all other (searchable) apps not included on the homepage using the search bar ([2434549](https://me.sap.com/notes/2434549)).If you want to personalize the homepage and include the hidden apps, navigate to your user profile and choose App Finder. |

Table 5: Overview Table

| Process Step | Business Role | App/Transaction | Expected Results |
| --- | --- | --- | --- |
| Create Claim | Claims Analyst | Manage Supplier Claims - Manage Supplier Claims (F5227) | Warranty claim is created |
| Validate Claim | Claims Analyst | Manage Supplier Claims - Manage Supplier Claims (F5227) | Claim is validated |
| Adjust Claim | Claims Analyst | Manage Supplier Claims - Manage Supplier Claims (F5227) | Claim is reset to created status |
| Send Claim to Supplier | Claims Analyst | Manage Supplier Claims - Manage Supplier Claims (F5227) | Claim document is sent to supplier |
| Maintain Supplier Response | Claims Analyst | Manage Supplier Claims - Manage Supplier Claims (F5227) | Supplier response is recorded in claim |
| Post Claim | Claims Analyst | Manage Supplier Claims - Manage Supplier Claims (F5227) | Claim is posted to Finance |
| Post Reversal | Claims Analyst | Manage Supplier Claims - Manage Supplier Claims (F5227) | Finance posting is reversed |
| Reject Claim | Claims Analyst | Manage Supplier Claims - Manage Supplier Claims (F5227) | Claim is rejected |
| Cancel Claim | Claims Analyst | Manage Supplier Claims - Manage Supplier Claims (F5227) | Claim is cancelled |
| Close Claim | Claims Analyst | Manage Supplier Claims - Manage Supplier Claims (F5227) | Claim is closed |
| Reopen Claim | Claims Analyst | Manage Supplier Claims - Manage Supplier Claims (F5227) | Claim is reopened |
| Reprocess Rejected Claim | Claims Analyst | Manage Supplier Claims - Manage Supplier Claims (F5227) | Claim is set to supplier response received |

## Test Procedures

This section describes test procedures for each process step that belongs to this scope item.

|  |
| --- |
| Note Please note that the descriptions specifically explain what is done or happens in the individual process steps. The scope item, in total, is set up to support process automation. This means that when a process step is successfully executed, the succeeding process step is directly initiated or performed. |

|  |
| --- |
| Note The processes described in the below topics do not expect any tax calculations for Brazil. |

### Create Supplier Claim

In this process step you can create a warranty claim.

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result |
| --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Claims Analyst. | The SAP Fiori launchpad is displayed. |
| 2 | Access the App | Open Manage Supplier Claims - Manage Supplier Claims (F5227). | The Manage Supplier Claims screen is displayed. |
| 3 | Open Create Claim | Choose Create → Supplier Facing Claim on Manage Supplier Claims screen. | The Claim screen is displayed. |
| 4 | Enter Claim Data | On the General Information within the Claim screen, enter following details:Supplier:33300010Object Type: Equipment (EQUI)Object:233100001Registration Date: value is automatically populatedDamage Date: for example, date of last weeks MondayRepair Date: for example, date of last weeks WednesdayRepair End Date: for example, date of last weeks WednesdayPlant:3310Purchase Organization: 3310Sales Organization:3310Distribution Channel: 10Division: 00Currency: AEDPerson Responsible: for example, Barbara Lee (SERV_EMPL)Header Notes: Optional fieldVersion Notes: Optional field | A warranty claim is created |
| 5 | Create Items (Optional) | Note Follow this step only when you have a service material, such as SRV_01On the tab, choose Add and select Labor Value from the dropdown list.On the Claim Item screen, enter the following details, and then choose Apply:Material: SRV_01Quantity: for example 2Unit: HRNotes: optionalChoose Apply. | Items are created |
| 6 | Create Items | On the Item Information tab, choose Add and select Spare Part, Material from the dropdown list.On the Claim Item screen, enter the following details, and choose Apply:Material: TG0011Quantity: for example 1Unit: PCNotes: optionalPart Causing Damage: XOnly the item type Material (MAT)has this optionOnly one item can be selected as part causing damageReturn Parts StatusIn case a part needs to be returned, the respective parts return status is automatically set. The status is set manually or set to shipped in case the shipment is already done.To get the status set to Parts have to be Returned automatically, the field Product Attribute 10 must be flagged in the material master. Material → Sales: Sales Organization → Product attribute 10 is flagged.Choose Apply. |  |
| 7 | Save Document | Choose Create. |  |

### Validate Supplier Claim

Purpose

In this process step, you can validate a warranty claim.

|  |
| --- |
| Note Please note that the descriptions specifically explain what is done / happens in the individual process steps. The scope item, in total is set up to support process automation. This indicates that when a process step is successfully executed, the succeeding process step is directly initiated or performed. |

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
| 1 | Log On | Log on to the SAP Fiori launchpad as a Claims Analyst. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the App | Open Manage Supplier Claims - Manage Supplier Claims (F5227). | The Manage Supplier Claims screen is displayed. |  |
| 3 | Open Create Claim | Choose Create → Supplier Facing Claim on Manage Supplier Claims screen. | The Claim screen is displayed. |  |
| 4 | Create Claim | Create a claim following the steps provided in [Create Supplier Claim](#unique_16) [page ] 15. | A warranty claim is created. |  |
| 5 | Validate Claim | Choose Process Actions → Validate. | The claim is validated and its status is set to Waiting for Supplier Response.Note When all the provided data are correct, the claim status is set to waiting for supplier response. The following actions are processed automatically according to the action matrix:Validate ClaimSend to SupplierNote If there are any errors in validation, the processing status is set to Error in Validation. Once the errors are fixed, you need to validate the claim again before sending to the supplier.For details on the validations done, refer [Validate a claim](https://help.sap.com/viewer/adbae5bcd5994f159bf2847a11397b61/2108.501/en-US/c467b5add2e1453ab8bcce25ef980f88.html).Errors are visible on clicking the View Alerts tab. |  |

### Adjust Supplier Claim

Once claim is validated, the edit option limits the number of fields to be edited to ensure consistency. In this process step, you can reset the claim to Created status, in order to adjust the fields.

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result |
| --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Claims Analyst. | The SAP Fiori launchpad is displayed. |
| 2 | Access the App | Open Manage Supplier Claims - Manage Supplier Claims (F5227). | The Manage Supplier Claims screen is displayed. |
| 3 | Open Claim | Choose Create → Supplier Facing Claim on Manage Supplier Claims screen. | The Claim screen is displayed. |
| 4 | Create Claim | Create a claim. Enter object:217100002 instead of 233100001. | A warranty claim is created. |
| 5 | Validate Claim | Choose Process Actions → Validate. | The claim status is set to Errors in Validation.An error message Maintain warranty start date for object EQUI 217100002 displays as the validation message. Equipment 217100002 has no customer warranty master assigned.Note If there are any errors in this validation step, the processing status is set to Errors in validation. |
| 6 | Adjust Claim | Choose Process Actions → Adjust Claim and then choose Edit. Change object: 217100002 to 233100001. Choose Save. | Claim status gets set to Created once the adjust claim is chosen. |

### Send to Supplier

Purpose

In this process step, you can send the claim statement to the supplier.

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
| 1 | Log On | Log on to the SAP Fiori launchpad as a Claims Analyst. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the App | Open Manage Supplier Claims - Manage Supplier Claims (F5227). | The Manage Suppler Claims screen is displayed. |  |
| 3 | Open Create Claim | Choose Create → Supplier Facing Claim on Manage Supplier Claims screen. | The Claim screen is displayed. |  |
| 4 | Create Claim | Create a claim following the steps provided in [Create Supplier Claim](#unique_16) [page ] 15.Set the return part status for item type Spare Part, Material to 1(Parts have to be returned). | A warranty claim is created. |  |
| 5 | Validate Claim | Choose Process Actions → Validate Claim.Set the return parts status to 3. | The claim is validated and its status is set to Successfully Validated An alert Damaged part TG0011 must be Returned with the claim is displayed.Note Use the Return Parts Status option in a scenario wherein you want to return a damaged part. The status must be maintained as Parts shipped or no parts to be returned. If you maintain the status as parts to be returned, then an error message is displayed. This is only possible when the item type is Mat (Material). |  |
| 6 | Set Return Parts Status | Choose Edit. Set the return part status for item type to 3 (Part shipped). | Once the return part status is set to 3 (Parts Shipped), the claim can be send to the supplier.Choose Save. |  |
| 7 | Send to Supplier | Choose Process Actions → Send to Supplier. | Claim status is set to Waiting for Supplier Response. In the Output Management section of version 1, a new entry is created with the details of output, which is sent to supplier.In case a part is set to be returned, the claim document cannot be sent to the supplier. Only once the part is shipped and the respective return parts status is updated in the claim, the system allows to send the claim to the supplier. |  |

### Maintain Supplier Response

Purpose

In this process step, you maintain the response received from the supplier.

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
| 1 | Log On | Log on to the SAP Fiori launchpad as a Claims Analyst. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the App | Open Manage Supplier Claims - Manage Supplier Claims (F5227). | The Manage Supplier Claims screen is displayed. |  |
| 3 | Open Create Claim | Choose Create → Supplier Facing Claim on Manage Supplier Claims screen. | The Claim screen is displayed. |  |
| 4 | Create Claim | Create a supplier claim following the steps provided in [Create Supplier Claim](#unique_16) [page ] 15 chapter. | A warranty claim is created. |  |
| 5 | Validate Claim | Choose Process Actions → Validate Claim. | Claim status is set to Waiting for Supplier Response. In the section, a new entry is created with the details of output, which is sent to supplier. |  |
| 6 | Supplier Response Received | Choose Process Actions → Maintain Supplier Response and then Edit.In the General Information, enter the following details, then choose Save:Decision:Approved: If a supplier fully approves a claim, set the decision to Approved. The approved net amount is set to same amount as the requested net amount. No additional steps is required at the items level.Partially Approved: If a supplier partly approves a claim, set the decision to Partially Approved. You can now either maintain the suppliers' response at the overall claim level by creating a condition within the Pricing Element section or by adjusting each of the items.For an overall maintenanceNavigate to the Pricing Information section and click Create at the table Pricing Elements to add a new conditionSelect condition PBTS and enter an amount that the supplier is accepting to pay and choose CreateFor maintenance on individual itemsSelect an itemIn the Claim Item page, select the decision code:Approved, if the supplier is accepting the item, fully. The value remains the same as requestedRejected, if the supplier is not accepting the item. A new condition PBRJ will be automatically created in the Pricing Elements that sets the overall item value to zeroPartially Approved, if the supplier is only paying a part of the requested amount. Also enter the amount the supplier is accepting to pay into the field, Amount. A new condition will be automatically created in the Pricing Elements that adjust the value accordinglyNote Condition types are different depending on the item type:PBRS: materialPBFS: laborPBSS: subletRejected: If a supplier rejects a claim, set the decision to Rejected. The approved net amount is set to zero. No additional steps is required at the items level. |  |  |

### Post Supplier Claim

Purpose

In this process step, you can carry out a financial posting for the approved supplier claim.

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
| 1 | Log On | Log on to the SAP Fiori launchpad as a Claims Analyst. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the App | Open Manage Supplier Claims - Manage Supplier Claims (F5227). | The Manage Supplier Claims screen is displayed. |  |
| 3 | Open Claim | Choose claims with the status Supplier Response Received and navigate to the document details. | A claim with status Supplier Response Received is opened. |  |
| 4 | Post Claim | Choose Process Actions → Post to Finance. | Claim status is set to Posted to Finance. |  |

### Reverse Claim Posting

Purpose

In this process step, you can reverse the financial posting for the supplier claim in case of wrong posting.

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
| 1 | Log On | Log on to the SAP Fiori launchpad as a Claims Analyst. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the App | Open Manage Supplier Claims - Manage Supplier Claims (F5227). | The Manage Supplier Claims screen is displayed. |  |
| 3 | Open Claim | Choose claims with the status Posted to Financeand navigate to the document details. | A claim with status Posted to Finance is opened. |  |
| 4 | Post Reversal | Choose Process Actions → Reverse Posting. | Claim status is set to Supplier Response Received. |  |

### Reject Supplier Claim

Purpose

In this process step, you can reject the supplier claim in case the claim is rejected by the supplier.

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
| 1 | Log On | Log on to the SAP Fiori launchpad as a Claims Analyst. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the App | Open Manage Supplier Claims - Manage Supplier Claims (F5227). | The Manage Supplier Claims screen is displayed. |  |
| 3 | Open Create Claim | Choose Create → Supplier Facing Claim on the Manage Supplier Claim screen. | The Claim screen is displayed. |  |
| 4 | Create Claim | Create a supplier claim following the steps provided in [Create Supplier Claim](#unique_16) [page ] 15. | A warranty claim is created. |  |
| 5 | Validate Claim | Choose Process Actions → Validate Claim. | Claim status is set to Succesfully Validated. |  |
| 6 | Send to Supplier | Choose Process Actions → Send to Supplier. | Claim status is set to Waiting for Supplier Response In the Output Management section of version 1, a new entry is created of output, which is sent to supplier. |  |
| 7 | Supplier Response Received | Choose Process Actions → Maintain Supplier Response and then Edit. In the General Information, enter the following detail, and choose Save:Decision : Rejected | Claim status is set to Supplier Response Received. |  |
| 8 | Reject Claim | Choose Process Actions → Reject Claim. | Claim status is set to Claim Rejected. |  |

### Cancel Supplier Claim

Purpose

In this process step, you can cancel the supplier claim.

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
| 1 | Log On | Log on to the SAP Fiori launchpad as a Claims Analyst. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the App | Open Manage Supplier Claims - Manage Supplier Claims (F5227). | The Manage Supplier Claims screen is displayed. |  |
| 3 | Open Create Claim | Choose Create → Supplier Facing Claim on Manage Supplier Claims screen. | The Claim screen is displayed. |  |
| 4 | Create Claim | Create a supplier claim following the steps provided in [Create Supplier Claim](#unique_16) [page ] 15. | A warranty claim is created. |  |
| 5 | Cancel Claim | Choose Process Actions → Cancel Claim. | The supplier claim is validated and its status is set to Cancelled.Note You can cancel a claim until it is sent to the supplier. This applies for claims that are created and validated but errors occurred during the validation process. |  |

### Close Supplier Claim

Purpose

In this process step, you can close the supplier claim after successful financial posting.

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
| 1 | Log On | Log on to the SAP Fiori launchpad as a Claims Analyst. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the App | Open Manage Supplier Claims - Manage Supplier Claims (F5227). | The Manage Supplier Claims screen is displayed. |  |
| 3 | Open Claim | Choose claims with the status Posted to Finance or Claim Rejected. | Choose one of the claims. |  |
| 4 | Close Claim | Choose Process Actions → Close Claim. | Claim status is set to Claim Posted and Closed or Claim Rejected and Closed.Note In addition, a claim can be closed once it is rejected. |  |

### Reprocess Rejected Supplier Claim

Purpose

In this reprocess step, you can reprocess a supplier claim after reopening a claim.

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
| 1 | Log On | Log on to the SAP Fiori launchpad as a Claims Analyst. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the App | Open Manage Supplier Claims - Manage Supplier Claims (F5227). | The Manage Supplier Claims screen is displayed. |  |
| 3 | Open Claim | Choose claims with the status Claim Rejected and navigate to the document details. | Choose one of the claims. |  |
| 4 | Reprocess Claim | Choose Process Actions → Reprocess Claim. | Reprocessing a rejected claim sets the claim status to the previous status. The claim status is set to Supplier Response Received. |  |

### Reopen Supplier Claim

Purpose

In this process step, you can reopen a closed supplier claim.

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
| 1 | Log On | Log on to the SAP Fiori launchpad as a Claims Analyst. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the App | Open Manage Supplier Claims - Manage Supplier Claims (F5227). | The Manage Supplier Claims screen is displayed. |  |
| 3 | Open Claim | Choose claims with the status Claim Closed and Posted or Claim Rejected and Closed and navigate to the document. | Choose one of the claims. |  |
| 4 | Reopen Claim | Choose Process Actions → Reopen Claim. | Reopening of the claim sets the claim status to the previous status. If claim status is Claim Rejected and Closed, the status is set to Claim Rejected. If claim is Claim Posted and Closed, the claim status is set to Posted to Finance. |  |

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
> Flagged while digesting this document, not verified: Validate Supplier Claim and Maintain Supplier Response say a validated claim goes straight to Waiting for Supplier Response (Send to Supplier runs automatically), but the Reject Supplier Claim steps show validation ending at Successfully Validated and then a separate manual Send to Supplier step.

## Connections
- part-of :: [[_cluster]]
- related-to :: [[14-maintenance-service-and-projects/warranty-claim-management-customer-claim-processing-63y-ae-test-script]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/5HR_S4CLD2608_BPD_EN_AE.docx` — full document · extracted with `mammoth` · 46,096 chars in the whole document
