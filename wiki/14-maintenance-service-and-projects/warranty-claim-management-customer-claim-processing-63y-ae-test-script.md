---
id: 14-maintenance-service-and-projects/warranty-claim-management-customer-claim-processing-63y-ae-test-script
title: "Warranty Claim Management – Customer Claim Processing (63Y_AE) – Test Script, SAP S/4HANA Cloud Public Edition (63Y_S4CLD2608_BPD_EN_AE)"
description: "SAP S/4HANA Cloud Public Edition 2608 (UAE) test script for scope item 63Y: customer warranty claim lifecycle in Manage Customer Claims (F6204), with prerequisites and sample data."
cluster: 14-maintenance-service-and-projects
tags: [kb/maintenance-service-and-projects, topic/warranty-claim-management]
aliases: [63Y_S4CLD2608_BPD_EN_AE]
keywords: [Warranty Claim Management, customer warranty claims, claim creation, claim validation, claim status transitions, master warranty, claim posting and reversal, claim rejection and closure, equipment warranty assignment, pricing condition records]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/63Y_S4CLD2608_BPD_EN_AE.docx]
confidence: low
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-1147
topic: 14-maintenance-service-and-projects/warranty-claim-management
language: EN
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Warranty Claim Management – Customer Claim Processing (63Y_AE) – Test Script, SAP S/4HANA Cloud Public Edition (63Y_S4CLD2608_BPD_EN_AE)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/63Y_S4CLD2608_BPD_EN_AE.docx`, extracted with `mammoth`. Grouped under **Warranty Claim Management** in Maintenance, Service and Projects. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

| <!-- image omitted: unnamed --> | Test ScriptSAP S/4HANA Cloud Public Edition - 19-06-26 |
| --- | --- |
|  | Warranty Claim Management – Customer Claim Processing (63Y_AE) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Table of Contents

[1 Purpose 3](#_Toc232858010)

[2 Prerequisites 4](#_Toc232858011)

[2.1 System Access 4](#_Toc232858012)

[2.2 Roles 4](#_Toc232858013)

[2.3 Master Data, Organizational Data, and Other Data 5](#_Toc232858014)

[2.4 Business Conditions 7](#_Toc232858015)

[3 Preliminary Steps 8](#_Toc232858016)

[3.1 Create Master Warranty 8](#_Toc232858017)

[3.2 Maintain Equipment Data and Assign Master Warranty 9](#_Toc232858018)

[3.3 Check Assignment of Pricing Procedure to Claim Type/Company Code 10](#_Toc232858019)

[3.4 Check Pricing Condition Records 11](#_Toc232858020)

[3.5 Check General Ledger (GL) Account Assignment 12](#_Toc232858021)

[3.6 Manage Default Account Assignment 12](#_Toc232858022)

[4 Starting Supplier Recovery Process from Customer Claim 14](#_Toc232858023)

[5 Overview Table 15](#_Toc232858024)

[6 Test Procedures 17](#_Toc232858025)

[6.1 Create Customer Claim 17](#_Toc232858026)

[6.2 Discard Customer Claim 19](#_Toc232858027)

[6.3 Validate Customer Claim 20](#_Toc232858028)

[6.4 Adjust Customer Claim 22](#_Toc232858029)

[6.5 Request Customer Return Parts 23](#_Toc232858030)

[6.6 Request Additional Information from Customer 24](#_Toc232858031)

[6.7 Information Provided 24](#_Toc232858032)

[6.8 Start Supplier Process from Customer 25](#_Toc232858033)

[6.9 Accept Customer Claim 26](#_Toc232858034)

[6.10 Post Customer Claim 27](#_Toc232858035)

[6.11 Reverse Posting of Claim 28](#_Toc232858036)

[6.12 Reject Customer Claim 29](#_Toc232858037)

[6.13 Close Customer Claim 30](#_Toc232858038)

[6.14 Reopen Customer Claim 31](#_Toc232858039)

[6.15 Reprocess Customer Claim 32](#_Toc232858040)

## Purpose

Overview

This scenario enables you to create a warranty claim for a reimbursement request of a supplier (based on a performed repair).

In this scenario, you create a claim, validate it for completeness and eligibility for reimbursement, and determine the correct prices for material, labor activities, and so on.

Based on the validation support of the system, the claim analyst can make a transparent decision on the claim and perform the financial reimbursement to the customer.

This document provides a detailed procedure for testing this scope item after solution activation, reflecting the predefined scope of the solution. Each process step, report, or item is covered in its own section, providing the system interactions (test steps) in a table view. Steps that are not in scope of the process but are needed for testing are marked accordingly. Project-specific steps must be added.

|  |
| --- |
| Note Values in this test script (decimal notation, date formats, and so on) are presented in U.S. standard notation. If your test system is set up to use a different notation, enter values as appropriate. |

## Prerequisites

This section summarizes all prerequisites to conducting the test in terms of systems, users, master data, organizational data, other test data and business conditions.

- [System Access](#unique_3) [page ] 4
- [Roles](#unique_4) [page ] 4
- [Master Data, Organizational Data, and Other Data](#unique_5) [page ] 5
- [Business Conditions](#unique_6) [page ] 7

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
| SAP_BR_BUPA_MASTER_SPECIALIST | CustomerSupplier | Manage Customer Master DataManage Supplier Master Data |
| SAP_BR_CLAIMS_ANALYST_COMPL | Claim | Manage Customer Claims |
| SAP_BR_MD_SPECIALIST_WRNTY | Warranty Master Data | Manage Master WarrantiesCreate Pricing Condition RecordsChange Pricing Condition RecordsDisplay Pricing Condition Records |
| SAP_BR_PRODMASTER_SPECIALIST | Material | Manage Product Master Data |
| SAP_BR_PRICING_SPECIALIST | Pricing Condition | Set Material Prices - Sales |

|  |
| --- |
| Note You need to maintain master data (equipment/functional location/supplier/customer or material) used within the customer warranty claims while navigating to the individual applications with the relevant test user in the cloud system. |

### Master Data, Organizational Data, and Other Data

The organizational structure and master data of your company has been created in your system during activation. The organizational structure reflects the structure of your company. The master data represents materials, customers, and suppliers, for example, depending on the operational focus of your company.

|  |
| --- |
| Caution Update Behavior of Predelivered Demo DataIn non-productive environments (such as starter systems, sandbox systems, or partner demo systems), SAP initially deploys demo data for your selected scope. You can use this data to test and evaluate business processes.In a customer system, you can receive new or updated demo data after initial activation with further scope enhancements, provided the existing demo data wasn't changed in an incompatible way. If activation errors occur due to incompatible changes in demo data, you're responsible for resolving them. If you don't resolve the errors within a specific time frame, SAP reserves the right to deactivate demo data in your systems. In this case, you can continue by creating your own demo data. Alternatively, you can request that your systems be reprovisioned if you want to work with predelivered demo data again.In partner systems, you can use the demo data deployed with the initial activation. No additional demo data will be deployed in the system with scope enhancements. You can only create additional demo data manually. |

Use your own master data or the following sample data to go through the test procedure.

For more information on creating master data objects, see the following [Master Data Scripts (MDS)](https://help.sap.com/docs/s4hana-best-practices/s4cld2608-master-data) .

Business Partner

| Data | Sample Value | Details |
| --- | --- | --- |
| Customer | 33100001 | Domestic UAE Customer 1 |

Organizational Unit

| Data | Sample Value | Details | Comments |
| --- | --- | --- | --- |
| Company Code | 3310 | Company Code 3310 | Appropriate Master Data Script (MDS): J56, J57, J47 |
| Sales Organization | 3310 | Dom. Sales Org |  |
| Distribution Channel | 10 | Direct Sales |  |
| Division | 00 | Product Division 00 |  |
| Plant | 3310 | Plant 1 AE | Appropriate Master Data Script (MDS): BFL |
| Person Responsible |  | < Use your own employee ID that is assigned to your user ID.> | How Employee Master Data can be maintained in SAP S/4HANA Cloud Public Edition: [https://s4hanacloud.community.sap/blogs/show/ONDHRzuhvLKHJFO1KmxKhB](https://s4hanacloud.community.sap/blogs/show/ONDHRzuhvLKHJFO1KmxKhB) |
| Currency | AED | UAE Dirham |  |

Master Data

| Data | Product Sample | Details | Comments |
| --- | --- | --- | --- |
| Material | TG0011 | Trading Good 0011,PD,Regular Proc. | Appropriate Master Data Script (MDS): BNF |
| EquipmentNote If you choose Functional Location as the object type, the number will be different. But, the procedure or steps to be performed remains the same. | 233100001 | Manual Isolation Valve | Refer [Create and Maintain Technical Objects (Equipment) (Optional)](https://help.sap.com/viewer/DRAFT/43f8e55f80e127ec4c48649b4186bde5/2108_DEV/en-US/e20dab5c98cd4895b0e866a457de5a6f.html) |
| General Ledger (GL) Accounts | 65008600 | Warranty Claim Processing | Refer [Check General Ledger (GL) Account Assignment](#unique_7) [page ] 12 |
| Master Warranty |  | To be created | Refer [Maintain Equipment Data and Assign Master Warranty](#unique_8) [page ] 9 |

|  |
| --- |
| Note Some of the values mentioned in the configuration steps, for example 1710 represent values that are available if you have implemented the SAP Best Practices content of the US version for this scope item. If you have activated another country version, your system will show different values, for example 1010 for Germany. To set up the system according to your own customer-specific needs, you may use your own values according to the structure of your company. |

For more information on creating master data scripts, see the following Master Data Scripts (MDS):

Table 2: Master Data Script Reference

| Master Data ID | Description |
| --- | --- |
| 3KV | Create Service Product for Service Processes |
| 2J7 | Create Product Master of Type "Spare Parts" |
| 31X | Create Product Master of Type "Services" |
| BND | Create Customer Master |
| 5MF | Create Equipment |
| 5LM | Create Functional Location |
| BNF | Create Product Master of Type "Trading Good" |
| 31Y | Create Product Master of Type "Non-stock Material" |

### Business Conditions

Before you test this scope item, the following business condition should be met.

| Scope Item ID | Business Condition |
| --- | --- |
| 1LQ - Output Management | This scope item provides best practice information for SAP S/4HANA output management that can be used to implement business scenarios that include output-related tasks. For details, refer to scope item [1LQ](https://me.sap.com/processnavigator/SolS/SolS-013/2608/SolP/1LQ) in the SAP Signavio Process Navigator.Note The settings for warranty claim management (application object types: WARRANTY_CLAIM and WARRANTY_CLAIM_CUSTOMER) must be done. |

## Preliminary Steps

Refer the below topics:

- [Create Master Warranty](#unique_10) [page ] 8
- [Maintain Equipment Data and Assign Master Warranty](#unique_8) [page ] 9
- [Check Assignment of Pricing Procedure to Claim Type/Company Code](#unique_11) [page ] 10
- [Check Pricing Condition Records](#unique_12) [page ] 11
- [Check General Ledger (GL) Account Assignment](#unique_7) [page ] 12

### Create Master Warranty

A warranty is a commitment from a manufacturer, vendor, or salesperson to a customer that a product has no defects, and that the services such as repairs or complete exchange of defective parts are guaranteed for a particular period of time. Repairs or exchanges are made if the product does not function as described or intended, without the customer being billed. Vendor warranty is a commitment made by the vendor or supplier to your company.

Prerequisites

- Relevant master data which are organizationl details, supplier, equipment, and material should exist
- Role SAP_BR_MD_SPECIALIST_WRNTY should be assigned
- Below counters should exist:
    - WARRANTY_DISTANCE_KM (Counter for distance in kilometer)
    - WARRANTY_DISTANCE_MI (Counter for distance in miles)
    - WARRANTY_OPERATING_HOURS (Counter for operating hours)
    - WARRANTY_PERIOD (Counter for time period)

Procedure

1. Log into the application as a warranty specialist.
2. Open the Manage Master Warranties application.
3. Choose Create.
4. On the Header tab, enter values for the following fields:
    - Description: for example, CW Isolation Valve 24 Months
    - Warranty Type: Customer Warranty
5. On the Terms and Conditions tab, choose Create to create a new item.
6. Enter values in the following fields:
    - Description: for example, Isolation Valve 24 Months
7. On the Warranty Counter, choose Add Counter and enter values for following fields:
    - Counter: WARRANTY_PERIOD
    - Counter Value: 24 (Mon)

Choose Add.

1. On the Warranty Counter, choose Add Counter and enter values for following fields:
    - Counter: WARRANTY_OPERATING_HOURS
    - Counter Value: 3200 (H)

Choose Add.

1. Ensure that the counter link is set .
2. Choose and then .

### Maintain Equipment Data and Assign Master Warranty

A warranty is a commitment from a manufacturer, vendor, or salesperson to a customer that a product has no defects, and that services such as repairs and partial or complete exchange of defective parts are guaranteed for a particular period of time, without the customer being billed.

Maintain Equipment Data

Use the below steps to maintain equipment data within the warranty claims:

1. Log onto the SAP Fiori launchpad with the role, .
2. Navigate to the Change Technical Object application.
3. Enter equipment number as the technical object and choose Continue.
4. Verify the acquisition date that displays as registration date within the Manage Customer Claims application.
5. Verify the customer warranty start date and assign master warranty for validating the customer claim.

|  |
| --- |
| Note These dates should be maintained so that the respective equipment can be used in the warranty claim. If the equipment is not maintained with valid master warranty and acquisition date, then the claim validation fails. |

Maintain Customer Warranty

The warranty claim process supports and integrates warranties that are based on dates (warranty period).

- Customer warranty: A commitment, that is made by your company to the customer.

If you have entered the start date and assign master warranty of an equipment, the system checks the validity of the claim. Before you use the warranty for individual objects within your claim process, you need to enter the warranty start date and assign master warranty in the equipment master data.

To create and/or maintain equipment, perform the steps from the master data scripts (MDS) 3U3. For more information on creating master data objects, see the following [Master Data Scripts (3U3)](https://help.sap.com/viewer/aab12ac0de280902b406e6242a66b51c/2202_DEV/en-US/504fdd228e71476e997e41979aa418ab.html).

Maintain Vendor Warranty

- Vendor warranty: A commitment, that is made by the vendor or supplier to your company.

If you have entered the start date and assign master warranty of an equipment, the system checks the validity of the claim. Before you use the warranty for individual objects within your claim process, you need to enter the warranty start date and assign master warranty in the equipment master data.

1. Log onto the SAP Fiori launchpad with the role, .
2. Navigate to the Change Technical Object application.
3. Enter your equipment number (for example,233100001) as the technical object and choose Continue.
4. Verify the acquisition date that displays as registration date within the Manage Supplier Claims application.
5. Verify the vendor warranty start date and assign master warranty for validating the supplier claim.

|  |
| --- |
| Note These dates should be maintained so that the respective equipment can be used in the warranty claim. If the equipment is not maintained with valid master warranty and acquisition date, then the claim validation fails. |

### Check Assignment of Pricing Procedure to Claim Type/Company Code

As a key user, you can determine the pricing procedure based on the country of claimant or reimburser.

The pricing procedure is assigned to the claim type, warranty process (claimant or reimburser), and the company code. For this, the company code should be defined and there should be valid claim type.

| Test Step # | Test Step Name | Instruction |
| --- | --- | --- |
| 1 | Log On | Log on to Fiori Launchpad. |
| 2 | Access the customizing activity | Navigate to Manage Your Solution application → Configure Your Solution → choose application area as Logistics.Sub application area : WarrantyWithin the configuration step → Assign Pricing Procedure to Claim Type/Company Code. |
| 3 | Check data | Check the following entries:Warranty Claim Type: 1C01Warranty Process: C ClaimantCompany Code:3310Procedure:A33A01Validity: Valid |

### Check Pricing Condition Records

Determining the correct prices is a central element within the warranty claim processing. To ensure that the appropriate amount can be claimed from the supplier, the correct prices need to be set up in the system. Each of the different item types (material, labor, sublet) has its own condition to ensure proper maintenance and relationship to the already existing pricing records.

Procedure - For Material

1. Log onto the SAP Fiori launchpad with the role, as a warranty specialist.
2. Open application.

The Display Conditions Record page displays.

1. Enter condition type: and press enter.
2. Choose key combination and choose Choose.
3. Enter:
    - Sales Organization:3310
    - Distribution Channel: 10
    - Material: TG0011

Ensure that the flag or field Cond.marked for deletion is not set.

-
    - Choose Execute.

1. Verify the condition record for the material.

Procedure - For Labor

1. Log onto the SAP Fiori launchpad with the role, , as a warranty specialist.
2. Open application. The page displays.
3. Enter condition type and press enter.
4. Choose key combination and choose Choose.
5. Enter:
    - Sales Organisation: 3310
    - Distribution Channel: 10
    - Material: SRV_01

Ensure that the flag for field Cond.marked for deletion is not set.

Choose Execute.

1. Verify the condition record for the service material.

|  |
| --- |
| NoteThe sublet items are always manually entered in the claim. Therefore, no pricing records need to be set up as preliminary step. |

### Check General Ledger (GL) Account Assignment

As a claim analyst, you can use the below procedure to set up the general ledger (GL) accounts.

Prerequisites

- Claim analyst must have the role, SAP_BR_BPC_EXPERT assigned.

| Test Step # | Test Step Name | Instruction |
| --- | --- | --- |
| 1 | Log On | Log on to Fiori Launchpad. |
| 2 | Access | Navigate to Manage Your Solution application and click Configure Your Solution. Choose the following values:Application Area: FinanceSub Application Area : General LedgerItem Name: Chart of AccountsWithin the Configuration Steps, choose step name Automatic Account Determination (100297). |
| 3 | Choose Area | Select Warranty in the Area field and choose Step 2. |
| 4 | Enter Parameters | Check the follwing entries and choose Step 3:Application: RWChart of Accounts: YCOACondition Table: 005 |
| 5 | Account Assignments | Check if the G/L Account is assigned. For example:Condition Type: KOFISales Organization: 3310Account Key: ERL (selected)G/L Account: 65008600If not assigned, maintain the item. Select the item you have just maintained and choose Review and then choose Save. |

### Manage Default Account Assignment

As a claim analyst, you can use the below procedure to set up default general ledger (GL) accounts.

Prerequisites

- Claim analyst must have the role, SAP_BR_BPC_EXPERT assigned.

| Test Step # | Test Step Name | Instruction |
| --- | --- | --- |
| 1 | Log On | Log on to Fiori Launchpad. |
| 2 | Access | Navigate to Manage Your Solution (F1241) application and click Configure Your Solution. Choose the following values:Application Area: FinanceSub Application Area : General SettingsItem Name: Journal EntriesWithin the Configuration Steps, choose step name Manage Default Account Assignment (102639). |
| 3 | Click New Entries | Click New Entries. |
| 4 | Enter Values | Enter Values:CoCd: 3310Cost Elem.: 65008600Cost Ctr: 33101101Click Save. |

## Starting Supplier Recovery Process from Customer Claim

In case you want to test the steps of chapter Start Supplier Process from Customer, you have to perform the preliminary step of test script of 5HR Supplier Recovery Processing.

## Overview Table

This scope item consists of several process steps that are listed in the following table:

|  |
| --- |
| Note If your system administrator has enabled spaces and pages on the SAP Fiori launchpad, the homepage will only contain the essential apps for performing the typical tasks of a business role.You can find all other (searchable) apps not included on the homepage using the search bar ([2434549](https://me.sap.com/notes/2434549)).If you want to personalize the homepage and include the hidden apps, navigate to your user profile and choose App Finder. |

Table 3: Overview Table

| Process Step | Business Role | App/Transaction | Expected Results |
| --- | --- | --- | --- |
| Create Claim | Claims Analyst | Manage Customer Claims (F6204) | Warranty claim is created. |
| Discard Claim | Claims Analyst | Manage Customer Claims (F6204) | Claim is discarded. |
| Validate Claim | Claims Analyst | Manage Customer Claims (F6204) | Claim is validated. |
| Adjust Claim | Claims Analyst | Manage Customer Claims (F6204) | Claim is reset to created status. |
| Request Customer Return Parts | Claims Analyst | Manage Customer Claims (F6204) | Claim is set to parts have to be returned. |
| Request Additional Information from Customer | Claims Analyst | Manage Customer Claims (F6204) | Claim is set to additional info requested. |
| Information Provided | Claims Analyst | Manage Customer Claims (F6204) | Claim is set to submitted. |
| Accept Claim | Claims Analyst | Manage Customer Claims (F6204) | Claim is accepted. |
| Start Supplier Process from Customer | Claims Analyst | Manage Customer Claims (F6204) | Supplier process is initiated. |
| Post Claim | Claims Analyst | Manage Customer Claims (F6204) | Claim is posted to finance. |
| Post Reversal | Claims Analyst | Manage Customer Claims (F6204) | Finance posting is reversed. |
| Reject Claim | Claims Analyst | Manage Customer Claims (F6204) | Claim is rejected. |
| Close Claim | Claims Analyst | Manage Customer Claims (F6204) | Claim is closed. |
| Reopen Claim | Claims Analyst | Manage Customer Claims (F6204) | Claim is reopened. |
| Reprocess Claim | Claims Analyst | Manage Customer Claims (F6204) | Claim is set to supplier response received. |

## Test Procedures

This section describes test procedures for each process step that belongs to this scope item.

|  |
| --- |
| Note Please note that the descriptions specifically explain what is done or happens in the individual process steps.The scope item, in total, is set up to support process automation. This means that when a process step is successfully executed, the succeeding process step is directly initiated or performed. |

|  |
| --- |
| Note The processes described in the below topics do not expect any tax calculations for Brazil. |

- [Create Customer Claim](#unique_17) [page ] 17
- [Discard Customer Claim](#unique_18) [page ] 19
- [Validate Customer Claim](#unique_19) [page ] 20
- [Request Customer Return Parts](#unique_20) [page ] 23
- [Request Additional Information from Customer](#unique_21) [page ] 24
- [Information Provided](#unique_22) [page ] 24
- [Adjust Customer Claim](#unique_23) [page ] 22
- [Accept Customer Claim](#unique_24) [page ] 26
- [Start Supplier Process from Customer](#unique_25) [page ] 25
- [Post Customer Claim](#unique_26) [page ] 27
- [Reverse Posting of Claim](#unique_27) [page ] 28
- [Reject Customer Claim](#unique_28) [page ] 29
- [Close Customer Claim](#unique_29) [page ] 30
- [Reopen Customer Claim](#unique_30) [page ] 31
- [Reprocess Customer Claim](#unique_31) [page ] 32

### Create Customer Claim

In this process step you can create a customer warranty claim.

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
| 2 | Access the App | Open Manage Customer Claims (F6204). | The Manage Customer Claims screen is displayed. |
| 3 | Open Create Claim | Choose Create → Pre-Credit Process Claim on Manage Customer Claims screen. | The Claim screen is displayed. |
| 4 | Enter Claim Data | On the General Information tab, enter the following details:Customer:33100001Object Type: Equipment (EQUI)Object: 233100001Registration Date: values are automatically populatedDamage Date: for example, date of last weeks MondayRepair Date: for example, date of last weeks WednesdayRepair End Date: for example, date of last weeks WednesdayOperating Hours: 120Plant: 3310Sales Organization:3310Distribution Channel: 10Division: 00Currency:AEDPerson Responsible: for example Barbara Lee (SERV_EMPL)Header Notes: this field is optionalVersion Notes: this field is optional | A warranty claim is created. |
| 5 | Create Items | On the Item Information tab, choose Add and select Labor Value from the dropdown list:On the Claim Item screen, enter the following details, and choose Apply:Material: CSSRV_01Quantity: for example, 2Unit: HRNotes: OptionalChoose Apply.On the Item Information tab, choose Add and select Spare Part, Material from the dropdown list.On the Claim Item screen, enter the following details, and choose Apply:Material: TG0011Quantity: for example, 1Unit: PCNotes: OptionalPart Causing Damage: XOnly the item type Material (MAT) has this optionOnly one item can be selected as part causing damageChoose Apply. |  |
| 6 | Save Document | Choose Create. |  |

### Discard Customer Claim

Purpose

In this process step, you can discard a customer warranty claim.

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
| 2 | Access the App | Open Manage Customer Claims (F6204). | The Manage Customer Claims screen is displayed. |  |
| 3 | Open Create Claim | Choose Create → Pre-credit Process Claim on Manage Customer Claims screen. | The Claim screen is displayed. |  |
| 4 | Create Claim | Create a claim. | A warranty claim is created |  |
| 5 | Discard Claim | Choose Process Actions → Discard Claim. | Claim status is set to Discarded. |  |

### Validate Customer Claim

Purpose

In this process step, you can validate a customer warranty claim.

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
| 2 | Access the App | Open Manage Customer Claims (F6204). | The Manage Customer Claims screen is displayed. |  |
| 3 | Open Create Claim | Choose Create → Pre-Credit Process Claim on Manage Customer Claims screen. | The Claim screen is displayed. |  |
| 4 | Create Claim | Create a claim following the steps provided in [Create Customer Claim](#unique_17) [page ] 17. | A warranty claim is created. |  |
| 5 | Validate Claim | Choose Process Actions → Validate on Submit. | The claim is set to Submitted.Note To proceed, the following steps are possible:Request Additional InformationRequest Return PartsFormal ValidationIf there are errors in this step of validation, for example, person responsible value not entered, respective messages display on clicking View Alerts and View Messages buttons. |  |
| 6 |  | Choose Process Actions → Formal Validation. | The claim status is set to Claim Posted.Note When all the entered details are correct, the claim is posted to finance. The following actions are processed automatically according to the action matrix:Complete Inbound ProcessContent ValidationPost to FinanceNote If there are any errors in validation in this step, the processing status is set to Errors in Formal Validation. Once the errors are fixed, you need to validate the claim again and perform steps 7 and 8.For details on the validations done, refer [Validate a Customer Claim](https://help.sap.com/viewer/adbae5bcd5994f159bf2847a11397b61/2202.500/en-US/7e5aaec6b8244f748e7d8c02cb6dba46.html).Errors are visible on clicking the View Alerts and View Messages buttons. |  |
| 7 |  | Choose Process Actions → Complete Inbound Process. | The claim is set to Ready for Content Validation.Note New outgoing claimant version (OC) is created. In addition, if there are any errors in validation in this step, you can still accept the claim using the respective option. |  |
| 8 |  | Choose Process Actions → Content Validation. | The claim is set to Content Validation Successful.Note If there are any errors in validation in this step, the processing status is set to Errors in Content Validation. Once the errors are fixed, you need to validate the claim again. |  |

### Adjust Customer Claim

Purpose

Once a customer claim is validated, the edit option limits the number of fields to be edited to ensure consistency. In this process step, you can reset the claim to Created status, in order to adjust the fields.

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
| 2 | Access the App | Open Manage Customer Claims (F6204). | The Manage Customer Claims screen is displayed. |  |
| 3 | Open Create Claim | Choose claims with the status Create → Pre -Credit Process Claim on Manage Customer Claims screen. | TheClaim screen is displayed. |  |
| 4 | Create Claim | Create a claim. Enter Sales Organization:3310. | A warranty claim is created. |  |
| 5 | Submit Claim | Choose Process Actions → Validate on Submit. | The claim is validated and its status is set to Submitted. |  |
| 6 | Validate Claim | Choose Process Actions → Formal Validation. | Processing status is set to Errors in Formal Validation. An error message Specified partner (xx) is not setup in sales organization (xx) displays as validation message. To resolve this issue, you need to adjust the claim. |  |
| 7 | Adjust Claim | Choose Process Actions → Adjust Claim and then choose Edit. Change the sales organization and choose Save. | Claim status is set to Submitted and correct data is maintained. |  |
| 8 | Validate Claim | Choose Process Actions →Formal Validation. | Claim status is set to Claim Posted. |  |

### Request Customer Return Parts

Purpose

Request is sent to the customer for parts to be returned. For this purpose, PDFs are generated and sent to the customer either through email or print.

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
| 2 | Access the App | Open Manage Customer Claims (F6204). | The Manage Customer Claims screen is displayed. |  |
| 3 | Open Claim | Choose claims in status Submitted. | Select one of the claims. |  |
| 4 | Check Returns Part Status | Go to Item Information to open the item. | The customer returns part status should be Parts have to be returned. |  |
| 5 | Request Return Parts | Choose Process Actions → Request Returns Parts. | The statement is generated and visible within the Output Management tab. |  |
| 6 | Check Output | Navigate to Output Management tab. | The statement is visible for print and for emailing. |  |

### Request Additional Information from Customer

Purpose

While validating a claim, the claim analyst can request addition information from the customer, for example, operating hour, mileage, clarifications in terms of notes, attachments, and so on. The claim is set to status, Additional Info Requested. Once the customer provides the requested information and saves the claim, the status is set to Submitted.

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
| 2 | Access the App | Open Manage Customer Claims (F6204). | The Manage Customer Claims screen is displayed. |  |
| 3 | Open Claim | Choose claims in status Submitted or Error in Formal Validation. | Select one of the claims. |  |
| 4 | Request Additional Information | Choose Process Actions → Request Additional Info. | The claim is saved with the processing status Additional Info Requested. |  |

### Information Provided

Purpose

In this process step, the customer provides the additional information requested by the claim analyst. Once done, the claim status is set to Submitted.

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
| 2 | Access the App | Open Manage Customer Claims (F6204). | The Manage Customer Claims screen is displayed. |  |
| 3 | Open Claim | Choose claims with status Additional Info Requested. | Select one of the claims. |  |
| 4 | Information Provided | Choose Process Actions → Information Provided. | The claim is saved with the processing status Submitted. |  |

### Start Supplier Process from Customer

Purpose

This action is to initiate supplier recovery process and displays after completing the inbound process of customer claims (OC version).

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
| 2 | Access the App | Open Manage Customer Claims (F6204). | The Manage Customer Claims screen is displayed. |  |
| 3 | Open Claim | Choose claim with the status Ready for Content Validation, Error in Content Validation, Claim Posted, and Claim Closed. | Select one of the claims. |  |
| 4 |  | Execute the action Initiate Supplier Process. Enter the following details:Partner (Supplier):33300010Purchase Organization: Purchase Organization 3310Sales Organization:3310 (copied from customer claim)Distribution Channel: 10 (copied from customer claim)Division: 00 (copied from customer claim)Currency:AED(copied from customer claim)PersnRespSuplr: for example, Barbara Lee (SERV_EMPL) | A pop up titled Initiate Supplier Process displays. Add values in all mandatory fields such as the supplier, purchase organization, and supplier person responsible. |  |
| 5 |  | Choose Initiate Supplier Process option in the pop up. | On executing this action successfully, the supplier process is initiated. Errors display in case it exist. |  |
| 6 |  | Open Manage Supplier Claims application. | The application displays. Proceed with the steps as mentioned in [Warranty Claim Management - Supplier Recovery Processing (5HR)](https://help.sap.com/docs/SAP_S4HANA_BEST_PRACTICES/6bc7c77e92098fa64708720e7742739d/21101f1a142d4f1bbcf7544fb7fa9141.html?state=DRAFT). |  |
| 7 |  | Search for the claim with the same claim number as customer claim. | The claim displays with the same claim number and new outgoing version. |  |

### Accept Customer Claim

Purpose

In this process step, you can accept a customer claim, irrespective of whether validation errors exist or not.

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
| 2 | Access the App | Open Manage Customer Claims (F6204). | The Manage Customer Claims screen is displayed. |  |
| 3 | Open Create Claim | Choose Create → Pre-Credit Process Claim on Manage Customer Claims screen. | The Claim screen is displayed. |  |
| 4 | Create Claim | Create a claim following the steps provided in [Create Customer Claim](#unique_17) [page ] 17. Enter Operating Hours as 4000 instead of 120. | A warranty claim is created. |  |
| 5 | Submit Claim | Choose Process Actions → Validate on Submit | The claim is validated and its status is set to Submitted. |  |
| 6 | Validate Claim | Choose Process Actions → Formal Validation. | Processing status is set to Errors in Formal Validation. An error message Operating hours have crossed the threshold is displayed as validation message. The customer warranty master has 3200 operating as maximum coverage. Although the maximum operating hours exceeds, the customer warranty claim is accepted. |  |
| 7 | Accept Claim | Choose Process Actions → Accept Claim. | The claim is set to Claim Posted.Note The decision code is automatically set to Approved and can be edited. |  |

### Post Customer Claim

Purpose

In this process step, you can carry out a financial posting for the approved customer claim.

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
| 2 | Access the App | Open Manage Customer Claims (F6204). | The Manage Customer Claims screen is displayed. |  |
| 3 | Open Claim | Choose claim with status Content Validation Successful. You can select the one reversed in the previous chapter. | Select one of the claims. |  |
| 4 | Approve Claim | Choose Edit. Set Decision to Approved and choose Save. | Claim is approved. |  |
| 5 | Post Claim | Choose Process Actions → Post to Finance. | Claim status is set to Claim Posted. |  |

### Reverse Posting of Claim

Purpose

In this process step, you can reverse the financial posting for the customer claim in case of wrong posting.

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
| 2 | Access the App | Open Manage Customer Claims (F6204). | The Manage Customer Claims screen is displayed. |  |
| 3 | Open claim | Choose claim with status Claim Posted. | Select one of the claims. |  |
| 4 | Post Reversal | Choose Process Actions → Reverse Posting. | Claim status is set to Content Validation Successful.Note Two new outgoing claimant version (OC) is created. The latest active version is available for posting. |  |

### Reject Customer Claim

Purpose

In this process step, you can reject the customer claim.

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
| 2 | Access the App | Open Manage Customer Claims (F6204). | The Manage Customer Claims screen is displayed. |  |
| 3 | Create Claim | Create a claim. Enter object:217100002 instead of 233100001. | A warranty claim is created. |  |
| 4 | Submit Claim | Choose Process Actions → Validate on Submit. | The claim is validated and set to Submitted. |  |
| 5 | Validate Claim | Choose Process Actions → Formal Validation | Processing status is set to Errors in Formal Validation. An error message displays as validation message. Equipment 217100002 has no customer warranty master assigned. In this case, the customer warranty claim is rejected. |  |
| 6 | Accept Claim | Choose Process Actions → Reject Claim. | The claim is set to Claim Rejected.Note The decision code is automatically set to Rejected - Formal Validation Error and can be edited. |  |

### Close Customer Claim

Purpose

In this process step, you can close the customer claim after successful financial posting.

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
| 2 | Access the App | Open Manage Customer Claims (F6204). | The Manage Supplier Claims screen is displayed. |  |
| 3 | Open Claim | Choose claim with status Claim Rejected or Claim Posted. | Select one of the claim. |  |
| 4 | Close Claim | Choose Process Actions → Close Claim. | Claim status is set to Claim Posted and Closed.Note In addition, a claim can be closed once it is rejected. If the claim selected is Rejected, then the status is set to Claim Rejected and Closed. |  |

### Reopen Customer Claim

Purpose

In this process step, you can reopen a closed customer claim.

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
| 2 | Access the App | Open Manage Customer Claims (F6204). | The Manage Customer Claims screen is displayed. |
| 3 | Open Claim | Choose claim with status Claim Posted and Closed or Claim Rejected and Closed. | Select one of the claims. |
| 4 | Reopen Claim | Choose Process Actions → Reopen Claim. | If the claim selected is Posted and Closed, then the status is set to Claim Posted.If the claim selected is Rejected and Closed, then the status is set to Claim Rejected. |

### Reprocess Customer Claim

Purpose

In this process step, you can reprocess a customer claim.

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
| 2 | Access the App | Open Manage Customer Claims (F6204). | The Manage Customer Claims screen is displayed. |  |
| 3 | Open Claim | Choose claims with the status Claim Rejected. | Choose one of the claims. |  |
| 4 | Reprocess Claim | Choose Process Actions → Reprocess Claim. | The claim status is set to Error in Content Validation. |  |

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
> Flagged while digesting this document, not verified: Labor pricing condition is checked for material SRV_01, but the claim labor item is created with material CSSRV_01; the sample data may be inconsistent.

> [!warning] Conflict
> Flagged while digesting this document, not verified: Validate Customer Claim says Formal Validation automatically runs Complete Inbound Process, Content Validation and Post to Finance and sets Claim Posted, yet steps 7 and 8 then run Complete Inbound Process and Content Validation manually, expecting Ready for Content Validation and Content Validation Successful; the status sequence is unclear.

## Connections
- part-of :: [[_cluster]]
- related-to :: [[14-maintenance-service-and-projects/test-script-warranty-claim-management-supplier-recovery-processing-5hr]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/63Y_S4CLD2608_BPD_EN_AE.docx` — full document · extracted with `mammoth` · 49,394 chars in the whole document
