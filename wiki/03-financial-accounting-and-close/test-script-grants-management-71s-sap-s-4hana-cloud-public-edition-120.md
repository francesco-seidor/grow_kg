---
id: 03-financial-accounting-and-close/test-script-grants-management-71s-sap-s-4hana-cloud-public-edition-120
title: "Test Script: Grants Management (71S) - SAP S/4HANA Cloud Public Edition (71S_S4CLD2608_BPD_EN_XX)"
description: "SAP S/4HANA Cloud Public Edition test script for scope item 71S Grants Management: master data setup, grant creation, budget upload, PO/invoice postings, IDC, billing, monitoring."
cluster: 03-financial-accounting-and-close
tags: [kb/financial-accounting-and-close, topic/public-sector-grants-management]
aliases: [71S_S4CLD2608_BPD_EN_XX]
keywords: [Public Sector Grants Management, grants management, grant master data, sponsored classes, sponsored programs, grants budget upload, substitution rules, cost share distribution, indirect cost posting, grants billing]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/71S_S4CLD2608_BPD_EN_XX.docx]
confidence: high
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-1202
topic: 03-financial-accounting-and-close/public-sector-grants-management
language: EN
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Test Script: Grants Management (71S) - SAP S/4HANA Cloud Public Edition (71S_S4CLD2608_BPD_EN_XX)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/71S_S4CLD2608_BPD_EN_XX.docx`, extracted with `mammoth`. Grouped under **Public Sector Grants Management** in Financial Accounting and Close. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

| <!-- image omitted: unnamed --> | Test ScriptSAP S/4HANA Cloud Public Edition - 19-06-26 |
| --- | --- |
|  | Grants Management (71S) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Table of Contents

[1 Purpose 3](#_Toc232841806)

[2 Prerequisites 4](#_Toc232841807)

[2.1 System Access 4](#_Toc232841808)

[2.2 Roles 4](#_Toc232841809)

[2.3 Master Data, Organizational Data, and Other Data 5](#_Toc232841810)

[2.4 Additional Manual Configuration 7](#_Toc232841811)

[2.5 Business Conditions 7](#_Toc232841812)

[2.6 Main Parameters for Data Creation 7](#_Toc232841813)

[2.6.1 Grant Type 7](#_Toc232841814)

[2.6.2 Authorization Groups 8](#_Toc232841815)

[2.6.3 Splitting Rule 8](#_Toc232841816)

[3 Preliminary Steps 9](#_Toc232841817)

[3.1 Create a Sponsored Program 9](#_Toc232841818)

[3.2 Add Sponsor Business Role to the Business Partner 9](#_Toc232841819)

[3.3 Create Sponsored Classes 10](#_Toc232841820)

[3.4 Create Substitution Rule for Sponsored Classes and Cost Share Split Rules 12](#_Toc232841821)

[3.5 Assign Sponsored Classes to G/L Accounts 13](#_Toc232841822)

[3.6 Create Automatic Account Assignment Distribution Rule 16](#_Toc232841823)

[3.7 Create a Grant 17](#_Toc232841824)

[3.8 Upload Grants Budget 19](#_Toc232841825)

[3.9 Create a WBS Element 20](#_Toc232841826)

[4 Overview Table 23](#_Toc232841827)

[5 Test Procedures 24](#_Toc232841828)

[5.1 Create a Purchase Order with a WBS 24](#_Toc232841829)

[5.2 Create Vendor Invoice with Reference to the Purchase Order 26](#_Toc232841830)

[5.3 Charge an Indirect Cost to a Grant 27](#_Toc232841831)

[5.4 Create Resource-Related Billing Document 29](#_Toc232841832)

[5.5 Grants Overview 30](#_Toc232841833)

[5.6 Monitor Grants 32](#_Toc232841834)

## Purpose

Overview

The Grants Management component provides public sector organizations with an integrated tool. Grants Management is a method used to record external financing sources in which the usage is restricted by sponsors. The current process showcases the master data objects and the relationship to general ledger accounts and controlling objects. The following functions are currently available:

- Perform, record and identify the activities related to the execution of sponsored programs
- Report all costs, revenues, and the required statistical information related to a grant
- Differentiate between eligible and ineligible costs

The Grants Management component is designed to provide public sector organizations with an integrated tool they can use to do the following:

- Plan, budget, identify, obtain, and record all funding related to received grants
- Plan, budget, identify, schedule, perform, and record the tasks and activities related to managing the sponsored programs and furthering the sponsor’s and organization’s objectives
- Differentiate between eligible and ineligible costs
- Bill and record sponsor amounts
- Record and report all related costs, revenues, and required statistical information

The current test script includes creating the relevant master data and posting both a commitment document including GM master data and account receivable/ account payable documents.

Other functionalities will follow with a later release.

This document provides a detailed procedure for testing this scope item after solution activation, reflecting the predefined scope of the solution. Each process step, report, or item is covered in its own section, providing the system interactions (test steps) in a table view. Steps that are not in scope of the process but are needed for testing are marked accordingly. Project-specific steps must be added.

|  |
| --- |
| Note Values in this test script (decimal notation, date formats, and so on) are presented in U.S. standard notation. If your test system is set up to use a different notation, enter values as appropriate. |

## Prerequisites

### System Access

The test should be conducted in the following system:

| System | Details |
| --- | --- |
| System | Accessible from the SAP Fiori launchpad. Your system administrator provides you with the URL required to access the various apps assigned to your role. |

### Roles

Create business roles using the following business role templates delivered by SAP and assign them to your individual test users.

Alternatively, if available, you can use the following spaces delivered by SAP. You create a space with pages containing predefined essential apps and assign it to the business role. You then assign this business role to your individual users.

For more information, refer to How to Create a Business Role from a Template in the [product assistance](https://help.sap.com/docs/SAP_S4HANA_CLOUD/53e36b5493804bcdb3f6f14de8b487dd/ec310a8b669a45ca898dc4dd91d97de2.html) for SAP S/4HANA Cloud Public Edition.

| Name (Role Template) | ID (Role Template) | Name (Launchpad Space) | ID (Launchpad Space) | Log On |
| --- | --- | --- | --- | --- |
| Grant Specialist | SAP_BR_GRANT_SPECIALIST | Grants Management | SAP_BR_GRANT_SPECIALIST |  |
| Project Financial Controller | SAP_BR_PROJ_FIN_CONTROLLER | Project Control - Finance | SAP_BR_PROJ_FIN_CONTROLLER |  |
| Purchaser | SAP_BR_PURCHASER | Purchasing / Sourcing and Contracting | SAP_MM_SPT_PURCHASING_PC / SAP_MM_SPT_SOURCING_PC |  |
| Accounts Payable Accountant | SAP_BR_AP_ACCOUNTANT | Accounts Payable / Central Invoice Management - Supplier Invoices / Central Invoicing - Supplier Invoice | SAP_BR_AP_ACCOUNTANT / SAP_MM_SPT_CIM_INV_PC / SAP_MM_SPT_CNTRL_INVOICING_PC |  |
| Accounts Receivable Accountant | SAP_BR_AR_ACCOUNTANT | Accounts Receivable | SAP_BR_AR_ACCOUNTANT |  |
| Master Data Specialist - Business Partner Data | SAP_BR_BUPA_MASTER_SPEC_TEST | Master Data - Business Partners / Business Partner Governance / Business Partner Governance / Business Partner Governance | SAP_BR_BUPA_MASTER_SPECIALIST / SAP_CA_SPT_MDG_BP_GOV_PC / SAP_CMD_SPT_BP_GOV_PC / SAP_CA_SPT_MDG_BP_WFUSR_PC |  |
| Billing Clerk | SAP_BR_BILLING_CLERK | Billing | SAP_BR_BILLING_CLERK |  |
| Configuration Expert - Business Process Configuration | SAP_BR_BPC_EXPERT | Business Process Configuration / Business Process Configuration - Finance / Business Process Configuration - Procurement / Manage your Solution / Business Process Configuration - Workflow / Business Configuration - Feature Management / Business Process Configuration - Extensibility Explorer / Business Configuration - Transportation | SAP_BR_BPC_EXPERT / SAP_FIN_SPT_BPC_EXPERT_PC / SAP_MM_SPT_BIZ_PROC_CONFIGN_PC / SAP_CA_SPT_IC_LND_BASE_PC / SAP_CA_SPT_BPC_WORKFLOW_PC / SAP_CA_SPT_BPC_FM_PC / SAP_EI_SPT_BPC_EXT_PC / SAP_TM_SPT_TRANSPCFG_PC |  |

Implementation Type

The following section is only relevant for SAP S/4HANA Cloud Public Edition.

### Master Data, Organizational Data, and Other Data

The organizational structure and master data for your company have been created in your system during activation. The organizational structure reflects the structure of your company. The master data represents materials, customers, and suppliers, for example, according to the operational focus of your company.

|  |
| --- |
| Caution Update Behavior of Predelivered Demo DataIn non-productive environments (such as starter systems, sandbox systems, or partner demo systems), SAP initially deploys demo data for your selected scope. You can use this data to test and evaluate business processes.In a customer system, you can receive new or updated demo data after initial activation with further scope enhancements, provided the existing demo data wasn't changed in an incompatible way. If activation errors occur due to incompatible changes in demo data, you're responsible for resolving them. If you don't resolve the errors within a specific time frame, SAP reserves the right to deactivate demo data in your systems. In this case, you can continue by creating your own demo data. Alternatively, you can request that your systems be reprovisioned if you want to work with predelivered demo data again.In partner systems, you can use the demo data deployed with the initial activation. No additional demo data will be deployed in the system with scope enhancements. You can only create additional demo data manually. |

Use your own master data or the following sample data to go through the test procedure.

| Data | Sample Value | Details | Comments |
| --- | --- | --- | --- |
| Fund | fund, for example, G6100> | Mandatory | Derived automatically |
| Functional Area | <functional area, for example, 1000> | Mandatory |  |
| Budget Period | <No Entry> | Mandatory |  |
| Cost Center | <cost center, for example, 17101302> | Optional | Replace with the cost center in your company code, such as xxxx1202 and xxxx1801 |
| Account Number | <account number, for example, 61100000> | Mandatory |  |
| Budget Account | <budget account, for example, 61100000> | Mandatory | Entered in the account number field. |
| Grant | <Grant created> | NRG | Delivered |
| Sponsored Class | <SUPPLIES> | Mandatory | Derived automatically |
| Profit Center | <YB600 (Shared Services)> | Optional | Derived automatically |
| Segment |  | Optional | Derived automatically |

You can find general information about creating master data objects in the following [Master Data Scripts (MDS)](https://help.sap.com/docs/s4hana-best-practices/s4cld2608-master-data) :

| MDS | Description |
| --- | --- |
| BND | Create Customer Master - MDS |
| BNE | Create Supplier Master - MDS |
| BNG | Create G/L Account and Cost Element - MDS |
| BNH | Create Profit Center - MDS |
| 47C | Create Fund - MDS |
| 47D | Create Budget Period - MDS |
| 47E | Create Functional Area - MDS |
| 4TA | Create Sponsored Class - MDS |

### Additional Manual Configuration

Before you can test this scope item, you must have completed the additional configuration steps that are described in the Set-Up Instructions for this scope item. These configuration steps are specific for your implementation and include mandatory settings that are not delivered by SAP and must be created by you. For more information, follow the link to the document:

[Link to Set-Up Instructions](https://help.sap.com/docs/SAP_S4HANA_BEST_PRACTICES/fdd617d6987f45297d6ac7a763b06800)

### Business Conditions

Before you can test this scope item, the following business conditions must be met.

| Scope Item ID | Business Condition |
| --- | --- |
| 6YU - Government Budget Management | The steps executed by the budget specialist to consume budget. |
| 1NT - Project Control – Finance | The steps executed by the project controller to create WBS elements. |
| BNX - Consumable Purchasing | The steps executed by the purchaser to consume budget using purchase orders. |
| J59 – Accounts Receivable | The steps executed by the accounts receivable accountant to create customer invoices used in Revenues Increasing the Budget (RIB). |
| J60 – Accounts Payable | The steps executed by the accounts payable accountant to consume budget using supplier invoices. |

### Main Parameters for Data Creation

In this section, we describe some basic parameters that influence the behavior of a master record and are always required to create this master data record:

#### Grant Type

Grant types are used to classify and group grant master data. The corresponding grant type is assigned during master data maintenance for each grant.

| Fund Type | Fund Type Description |
| --- | --- |
| G1 | Governmental |
| G2 | Non-Governmental |

#### Authorization Groups

Authorization groups are mandatory. They can be used if they have been customized:

| Grant Auth. Group | GrantAuthGrpDescr |
| --- | --- |
| S_ALL | ALL |

#### Splitting Rule

The following budget time slice splitting rules for budget validity can be used:

| Splitting Rule | Description |
| --- | --- |
| 0001 | Sponsor Fiscal Year |
| 0002 | Grant Validity |
| 0003 | Biannual based on Sponsor FY |

## Preliminary Steps

This section describes the procedures that apply to each process step associated with this scope item. You can also use these procedures to test the creation of master data.

### Create a Sponsored Program

This chapter describes how to create a sponsored program master data record for your SAP S/4HANA Cloud Public Edition system. A sponsored program master record can be used to process budget documents (in a later release), budget consumption and related reports.

Procedure: SAP Fiori

Access the activity as follows:

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as Grant Specialist. | The SAP Fiori launchpad appears. |  |
| 2 | Open Manage Sponsored Programs | Front end SAP Fiori App:Open Manage Sponsored Programs (F4545). |  |  |
| 3 | Create a Sponsored Program | On the Manage Sponsored Programs (F4545) screen, choose Create. | The Sponsored Program opens in the editing mode. |  |
| 4 | Enter Sponsored Program Data | Enter the following manually:Sponsored Program ID <PROGxx>Sponsored Program Name <Program xxx>Sponsored Program Description <Program xxx> | Sponsored Program data is set. |  |
| 5 | Save Sponsored Program | Click on Create. | A system message appears informing you that the object has been created.No errors occur and the application displays the new sponsored program master. |  |

### Add Sponsor Business Role to the Business Partner

This chapter describes how to add the sponsor business role to a business partner in your S/4 HAHNA Cloud system. Only business partners assigned to the sponsor business role can be used as a sponsor in a grant. This activity only needs to be executed once. If the sponsor role is already assigned, you do not need to do anything here.

Procedure: SAP Fiori

Access the activity as follows:

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1. | Log On | Log on to the SAP Fiori launchpad as Grant Specialist. | The SAP Fiori launchpad appears. |  |
| 2. | Open Maintain Business Partner | Front end SAP Fiori app:Open Maintain Business Partner (Transaction BP). | The Maintain Business Partner screen appears. |  |
| 3. | Start editing Business Partner | Click Open BP in the menu area. | A pop up to enter the business partner appears. |  |
| 4. | Edit Business Partner | Enter a business partner manually <for example, 17100001>.Click Enter. | The business partner detail screen appears. |  |
| 5. | Check if Sponsor Role is Already Assigned | Click the dropdown field Display in BP Role.Check whether the Sponsor role is found in the dropdown list.If the role is already found in the list, subsequent steps do not need to be executed. | The dropdown list appears. |  |
| 6. | Change Business Partner | Click Switch Between Display and Change in the menu area. | Fields on the screen are ready for input. |  |
| 7. | Add Role Assignment | Click the dropdown field Change in BP Role.Scroll down to find the Sponsor role and select this Sponsor role. | The Change in BP Role field contains the <Sponsor (new)> entry. |  |
| 8. | Save Business Partner | Click Save. | A message appears informing you that the changes have been saved. |  |

### Create Sponsored Classes

This chapter describes how to create a sponsored class master data record for your SAP S/4HANA Cloud Public Edition system. A sponsored class can be used to process budget documents (in a subsequent release), budget consumption and related reports. The sponsored classes only need to be created once. If they already exist, this step does not need to be executed.

Procedure: SAP Fiori

Access the activity as follows:

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as Grant Specialist. | The SAP Fiori launchpad appears. |  |
| 2 | Open Manage Sponsored Class | Front end SAP Fiori app:Manage Sponsored Classes (F4445). | The Manage Sponsored Classes (F4445) screen appears. |  |
| 3 | Check Whether Sponsored Classes Already Exist | Click Go. Use the search field to check whether the sponsored classes SUPPLIES, BENEFITS, GRANT_REVENUE, INDIRECT_CHARGES and GRANT_IDC_REVENUE already exist. If this is the case, no further steps need to be executed. If not, follow the subsequent steps to create the sponsored classes.Note It does not matter whether the Account for Budget is different in the existing class. | A list of existing sponsored classes appears. |  |
| 4 | Create a Sponsored Class | On the Manage Sponsored Classes (F4445) screen, choose Create. | The Manage Sponsored Classes (F4445) opens in the editing mode. |  |
| 5 | Enter Sponsored Class Data | Enter the following manually:Sponsored Class ID: <SUPPLIES>Sponsored Class Name: <Supplies>Sponsored Class Description: <Supplies>Choose the Class Type Expense.Account for Budget: <budget account, for example, 65100000>Set the Billable indicator. | The sponsored class data has been defined. |  |
| 6 | Save Sponsored Class | Click Save. | A system message appears informing you that the object has been created.No errors occur and the application displays the new sponsored class master. |  |
| 7 | Repeat Steps 4 – 6 with the following information | Sponsored Class ID: <BENEFITS>Sponsored Class Name: <Benefits>Sponsored Class Description: <Benefits>Choose the Class Type: ExpenseAccount for Budget: 61061000Set the Billable indicator. | The sponsored class <BENEFITS> is created. |  |
| 8 | Repeat Steps 4 – 6 with the following information | Sponsored Class ID: <GRANT_REVENUE>Sponsored Class Name: <Grant Revenue>Sponsored Class Description: <Grant Revenue>Choose the Class Type RevenueAccount for Budget: 41080000Do NOT set the Billable indicator. | The sponsored class <Grant Revenue> is created. |  |
| 9 | Repeat Steps 4 – 6 with the following information | Sponsored Class ID: <INDIRECT_CHARGES>Sponsored Class Name: <Indirect Charges>Choose the Class Type ExpensesAccount for Budget: 69999200Set the Billable indicator. | The sponsored class <Grant Revenue> is created. |  |
| 10 | Repeat Steps 4 – 6 with the following information | Sponsored Class ID: <GRANT_IDC_REVENUE>Sponsored Class Name: <IDC Revenue>Choose the Class Type RevenueAccount for Budget: 49999200Set the Billable indicator. | The sponsored class <Grant Revenue> is created. |  |

### Create Substitution Rule for Sponsored Classes and Cost Share Split Rules

|  |
| --- |
| Note The substitution rules only need to be created once. If such rules already exist, this step does not need to be executed. |

This chapter describes how to create two types of substitution rules:

1. Substitution rules to determine a sponsored class from the general ledger account in your SAP S/4HANA Cloud Public Edition system. A substitution rule is required to determine the sponsored class during consumption postings, such as purchase orders or invoices.
2. A substitution rule to determine the cost share split rule

Procedure: SAP Fiori

Access the activity as follows:

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori launchpad as Configuration Expert - Business Process Configuration | The SAP Fiori launchpad appears. |  |
| 2 | Manage substitution/validation | Frontend SAP Fiori app:Open Manage Substitution and Validation Rules (F7603). | The Manage Substitution and Validation for Public Sector (F7603) screen appears. |  |
| 3 | Start creation of the substitution rule | Choose Create Rule | The dialog box Create Rule appears. |  |
| 4 | Enter values on the dialog box | Choose Public Sector Automatic Account Assignment Distribution Rule in the drop-down list for the Business Context.The event is filled automatically.Choose the rule type Substitution Rule.Choose Create. | The dialog box disappears and the rule maintenance screen appears. |  |
| 5 | Enter the required information for the rule | Enter the following manually:Rule Name: <GRANT_COSTSHARE>Description: <Grant Cost Share>In the section Precondition:Position the cursor in the field Field. A dialog box appears to select the field. Expand the node PSM_S4C_SPLIT_SUBSTN_RULE, scroll down and expand the node _grant. Choose the field <GranteeMgmtCostSharingRule>.Choose <Is not empty> as the operator in the dropdown list for that field.In the section Substitution:Position the cursor in the field Target Field. A dialog box appears to select the field. Choose the field <SplitRule>.Choose <Substitution with constant> as the Substitution Type in the drop-down list for that field.Enter <GRANT> in the Source field.Click Save. | The rule is saved, and the rule maintenance screen appears in the display mode. |  |
| 6 | Activate the rule | Choose Activate. | The message Rule Activated appears. |  |

### Assign Sponsored Classes to G/L Accounts

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

|  |
| --- |
| Note The assignment of sponsored classes to the G/L account only needs to be done once. If the sponsored classes are already assigned to the G/L accounts, this step does not need to be executed. |

Table with G/L account – Sponsored Class Assignments

| G/L Account ID | Short Text | Sponsored Class |
| --- | --- | --- |
| 41000000 | Rev Domestic Prod | GRANT_REVENUE |
| 41080000 | Grant Revenue | GRANT_REVENUE |
| 49999200 | GM IDC Recovery | GRANT_IDC_REVENUE |
| 51100000 | Consptn Raw Mat | SUPPLIES |
| 51600000 | Consptn Trde Gds | SUPPLIES |
| 61002000 | 3rd party material | SUPPLIES |
| 65008300 | Services - General | SERVICES |
| 65100000 | Office Supplies | SUPPLIES |
| 69999200 | GM Indirect Cost | INDIRECT_CHARGES |

|  |
| --- |
| Note If you receive the message “Posting to grant xxx and G/L account yyy requires a sponsored class” during your testing you can assign a suitable sponsored class to the G/L account missing the assignment as described in the following procedure. |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori launchpad as Configuration Expert - Business Process Configuration Test | The SAP Fiori launchpad appears. |  |
| 2 | Check/Create Customizing Transport | Frontend SAP Fiori app:Open Export Customizing Transports (F5069) . | The Export Customizing Transports (F5069)screen appears. |  |
| 3 | Check if Customizing Transport for User Example BpcExpert Exists | Look for transport request with Example BpcExpert in owner column and status Modifiable | If transport exist continue with step 6 |  |
| 4 | Create Transport for User Example BpcExpert | Choose Create. | The transport request detail screen appears. |  |
| 5 | Enter the Required Information for the Transport and Create Transport | Enter the following manually:Description: <Test Customizing>Technical Type: <Customizing Request>Target: Pick one with search help. For example, </YGDK_CUS/>Click Create. | The transport is created and the list with transports is displayed. |  |
| 6 | Open Manage G/L Account Master Data (F0731A) | In the address area of your browser enter GLAccount-manage behind the hashtag (#) symbol. The URL should look like this https://XXXX.XX.XXX.XXX/ui?sap-language=#GLAccount-manageThe XXX represent the address of your test system.Press ENTER. | The Manage G/L Account Master Data (F0731A) app opens. |  |
| 7 | Add Sponsored Class as Column | Open settings for table (little cogwheel in table header area). Set the checkbox in front of field Sponsored Class.Click OK | G/L accounts list screen appears again with Sponsored Class added as column |  |
| 8 | Enter Selection Data | Enter the following manually:Chart of Accounts: <YCOA>G/L Account: All G/L account ID’s given in the table above.Choose Go | List of selected G/L accounts with assigned Sponsored Classes is displayed.If assigned sponsored classes match assignments in table above the following steps do not need to be executed. |  |
| 9 | Start MassChange | Mark all selected lines.Press Mass Change and choose Other Attributes | Mass Replacement screen is displayed. |  |

### Create Automatic Account Assignment Distribution Rule

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This chapter describes how to create an automatic account assignment distribution rule for your SAP S/4HANA Cloud Public Edition system. An automatic account assignment distribution rule is required to automatically split purchase order or earmarked fund lines into the sponsor and cost share contribution.

The rule only needs to be created once. If it already exists, this step does not need to be executed.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori launchpad as a Grant Specialist. | The SAP Fiori launchpad appears. |  |
| 2 | Access the SAP Fiori App | Open Manage Automatic Account Assignment Distribution Rule (F5600). | The Manage Automatic Account Assignment Distribution Rule (F5600) list screen appears. |  |
| 3 | Check whether the rule already exists | Click Go. Use the search field to check whether the rule GRANT already exists. If this is the case, no further steps need to be executed. If not, follow the subsequent steps to create the rule. | A list of existing rules appears. |  |
| 4 | Create the distribution rule | On the Manage Automatic Account Assignment Distribution Rule (F5600) screen, choose Create. | A dialog box appears on which you can enter the rule name |  |
| 5 | Enter the rule name | Enter the following manually on the dialog box:Distribution Rule: <GRANT>Choose Continue. | The Rule detail screen appears. |  |
| 6 | Enter the detail data | Choose or enter the following manually:Rule Group: <SGM1>Rule Name: <Grant Cost Share>Field Profile: <Fund (SFPGM00002)>Rule Type: <GM Cost Sharing Rule>>Remainder Handling: <Allocate to Original Account Assignment>Choose Create. | The rule is created and Object Created message appears |  |

### Create a Grant

This chapter describes how to create a grant master data record for your SAP S/4HANA Cloud Public Edition system.

A grant master record can be used to process budget documents (in a later release), budget consumption and related reports.

Procedure: SAP Fiori

Access the activity as follows:

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as the SAP_BR_GRANT_SPECIALIST . | The SAP Fiori launchpad appears. |  |
| 2 | Open Manage Grants | Frontend SAP Fiori App:Open Manage Grants (F4182). | The Manage Grants (F4182) screen appears. |  |
| 3 | Create a Grant | On the Manage Grants (F4182) screen, choose Create. | The Grant opens in the editing mode. |  |
| 4 | Enter General Information | Select the following values:Grant Type : <G2>Sponsor : <17100001>Cost Center: <cost center, for example, 17101302>Grant Type: <G2>Authorization Group : <S_ALL>Name : <inventory funding>Valid From Date : <01.01.20xx>Valid To Date : <31.12.20xx +3>Grant Fiscal Year Variant: <V6>Time Slice Split Rule: <0002>Choose Reset using the splitting rule | The general data is entered manually. | The value help opens a calendar where you can choose the date. |
| 5 | New Dimensions | In the section dimensions, table Funds related to Grant choose Add. Enter Fund <fund, for example, G6100>.Repeat with the fund <fund, for example, G1100>. Set the IDC Recovery and Cost Sharing Flag for this fund.In the section dimensions, table Grant related Sponsored Programs choose Add. Enter the sponsored program created earlier.In the section dimensions, table Grant related Sponsored Classes choose Add. Enter the sponsored class created earlier SUPPLIES. Repeat to add the sponsored classes BENEFITS, INDIRECT_CHARGES, GRANT_IDC_REVENUE and GRANT_REVENUE.Set the IDC Relevant and Cost Sharing flag for the sponsored class SUPPLIES |  |  |
| 6 | Enter Billing Information | Select the following value:Billing Rule: <2 (Res. Rel. Billing - Expenses)> |  |  |
| 7 | Enter Cost Share Details | Select the following values:Cost Share Rule: 1In the Cost Sharing Details table, enter the following in the line with the sponsored class SUPPLIES:Cost Share Rate%: 10Note You might need to choose Enter for the table to be filled. |  |  |
| 8 | Enter Indirect Cost Details | Select the following values:ICD Rule: 1In the Indirect Cost Rates table, enter the following in the line with the sponsored class SUPPLIES:ICD Rate: 20Note You might need to choose Enter for the table to be filled. |  |  |
| 9 | Save Grant | Click Save. | A system message appears informing you that the object has been saved.No errors occur and the application displays the new grant master. |  |

### Upload Grants Budget

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Procedure: SAP Fiori

Access the activity as follows:

| Test Step | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1. | Log On | Log on to the SAP Fiori launchpad as the grants specialist. | The SAP Fiori launchpad appears. |  |
| 2. | Open Import Financial Plan Data (F1711). | Frontend Fiori App:Open Import Financial Plan Data (F1711). | The Import Financial Plan Data (F1711) screen appears. |  |
| 3. | Download Template | Choose Download Templatesand download the template Public Sector Budgeting to enter budget. | Excel template downloaded with the file format CSV (file extension <*.csv>). |  |
| 4. | Create Excel File for PSM Budget | Create an Excel file including your public sector budget data.Note Do not delete the existing line that contains an X for each column.Make sure that there is an X in the Grant column to avoid overwriting the budgetThe Public Sector Budgeting Excel template provides the following fields:Category: <BUDGET03>General Ledger Fiscal Year: <current year>Posting Period: 1Company Code: <company code, for example, 1710>Cost Center: <cost center, for example, 17101302>WBS Element External Number: <No Entry>Account Number (Budget Account for PSM): <budget account, for example, 65100000>Functional Area: <No Entry>Fund: <fund, for example, G6100>Budget Period: <No Entry>Sponsored Program: <Sponsored Program created earlier>Sponsored Class: <SUPPLIES>Budget Validity Number: <’010> (note apostrophe at beginning)Budget Process: ENTRBudget Subcategory: S_SCAT1Grant: <Grant created earlier>Global Currency: <currency code, for example, USD>Global Currency Amount: 10000Copy line and change fund to <fund, for example, G1100>.Make sure you save your Excel file in the file format CSV (File extension <*.csv>). | Excel list created.(SUPL & RETN is also supported by the Excel upload) |  |
| 5. | Browse a CSV File | On the Import Financial Plan Data (F1711) screen, chooseBrowse .csv Files and select the file that includes your budget. | The selected data is proposed in the Source File field. |  |
| 6. | Import Data | Click Import Source File. | The data from the file is imported. |  |
| 7. | Check Financial Plan Data | Click on Check Financial Plan Data. | The report for PlanAmountInGlobalCurrency (Plan Amount in Global Crcy) appears. |  |

### Create a WBS Element

Postings in this document include a WBS element. With reference to the ONT scope item (see previous chapter), you should create a WBS element and also include an actual grant and a sponsored program. This grant and sponsored program are then derived automatically from a WBS element in postings.

Purpose

In this activity, you can create projects of the following type based on the business requirement with the project definition and WBS element using the Fiori app Project Control - Enterprise Projects (F3215):

Projects with Revenue Allows revenue G/L journal entry postings to be made following release. The profitability segment characteristics can be maintained in the settlement rule. However, you no longer need to perform settlement due to cost postings being attributed directly.

Procedure: SAP Fiori

Access the activity as follows:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as a PROJ_FIN_CONTROLLER. |  |  |
| 2 | Access App | Open Project Control - Enterprise Projects (F3215). | The Project Control screen appears. |  |
| 3 | Create Project: Definition | Choose Create.Make entries as shown in the following example in the Header and General Information sections:HeaderProject Name: Project with RevenueProject ID: Rev.0001Project Profile: Project with RevenuePlanned Start: Today (MM/dd/yyyy)Planned Finish: Today + 3 months (MM/dd/yyyy)General information:Responsible Cost Center: <Example: <cost center, for example, 17101501> (R&D)>Profit Center: <YB600 (Shared Services)>Project Currency: <currency code, for example, USD> (Automatically filled based on the cost center)Project Manager: the Project Manager IDPriority: the priority suitable for projectChoose Create.A success message tells you that the project has been saved. | A project is created with the definition parameters provided.A WBS element, as shown in the following example, is created under the project :WBS Element ID: <O.000001>Project Name: <Project with Revenue>Note The PSM fields are only visible once the project has been saved. You can add values in the next step. |  |
| 4 | Add Values to the Project Summary Task WBS Element | Once the project is created, from the header section, choose Edit.Make the following entries:General InformationPlant: <plant, for example, 1710>Fund: <fund, for example, G6100>Functional Area: <functional area, for example, 1000> (General Government)Grant: < the one created above>Sponsored Program: < the one created above>Costing Sheet: <costing sheet, for example, 1710PI>Choose Save. | The WBS element is updated with all the parameters provided.A system message tells you that the project has been saved. |  |
| 5 | Release Project | Select the project and in the header section choose Processing Status > Release |  |  |
| 6 | Save Project with WBS Element | Choose Save. | The project is saved with the WBS element. |  |

## Overview Table

This scope item consists of several process steps that are listed in the following table:

|  |
| --- |
| Note If your system administrator has enabled spaces and pages on the SAP Fiori launchpad, the homepage will only contain the essential apps for performing the typical tasks of a business role.You can find all other (searchable) apps not included on the homepage using the search bar ([2434549](https://me.sap.com/notes/2434549)).If you want to personalize the homepage and include the hidden apps, navigate to your user profile and choose App Finder. |

| ID (Role Template) | Name (Role Template) | App/Transaction | Expected Results |
| --- | --- | --- | --- |
| Create grants budget | Grant Specialist | Maintain Budget | Budgeting created |
| Purchase order with WBS/ grant(Example for commitment documents with grant) | Purchaser | Manage Purchase Orders | PO created. |
| Create vendor invoice with PO reference(Example for actuals with grant) | AP_Accountant | Create Supplier Invoice | Vendor invoice created with reference to a PO. |
| Check AVC | Grant Specialist | Available in a subsequent release | Budgeting consumption checked. |

## Test Procedures

This section describes the procedures that apply to each process step associated with this scope item. You can also use these procedures to test the creation of master data.

### Create a Purchase Order with a WBS

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

Create a purchase order, which is recorded for a grant.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori launchpad as a Purchaser. | The SAP Fiori launchpad appears. |  |
| 2 | Access app | Open Manage Purchase Orders (F0842A). | The Manage Purchase Orders screen appears. |  |
| 3 | Start purchase order creation | Without making any selection, choose Create. | The New Purchase Order screen appears. |  |
| 4 | Enter purchase order data | Make the following entries:In the Basic Data area:PO Type: Standard PO (NB)Supplier: <supplier, for example, 17300001> in plant <plant, for example, 1710>Currency: <currency code, for example, USD>Purchasing Group: purchasing group, for example, 001>Purchasing Organization: <purchasing organization, for example, 1710>Company Code: <company code, for example, 1710>Choose the Notes tab at header level. Choose > or < to search for header text. In the Header text column, enter the free text: xxx for testing. |  |  |
| 5 | Purchase material without a material number | In the Items area:Choose Create and enter the following values:Item Category: StandardShort Text: Enter an appropriate description, for example, <office supplies>Material Group: YBMM01Plant: <plant, for example, 1710>Order Quantity: <XX PC >Net Order Price: <XX>Acct Assignment Cat.: project(P)Go to the Purchase Order item view.Go to the Process Control section: Goods Receipt <empty> (no flag)Go to the Tax section and enter:Tax Code: <tax code, for example, I0>Go to the Account Assignment section and enter:G/L Account >G/L account, for example, 51600000> for a material without a material number. (The G/L account is determined automatically.)WBS: <the one created above>on the screen that appears.This master data should be derived from the WBS (if not, please enter it manually).Fund: <fund, for example, G6100>Grant: <the one created above>Functional Area: <functional area, for example, 1000>Budget Period: <Overall> |  |  |
| 6 | Apply entered data | Choose Apply. | The account assignment is split according to the grant cost share setting. |  |
| 7 | Save purchase order | Choose Apply to return to the purchase order screen. Choose Order to save the purchase order. | The purchase order is created. |  |
| 8 | Grant Specialist | “Comm/act line item display” Fiori App (W0151)Enter Grant: <the one created above> | The PO was posted to the correct GM account assignments. |  |

### Create Vendor Invoice with Reference to the Purchase Order

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you create a vendor invoice, which is recorded for a grant.

Prerequisities

The supplier master record has been created.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a SAP_BR_AP_ACCOUNTANT |  |  |
| 2 | Access the SAP Fiori App | Open Create Supplier Invoice (F0859). | The Manage Supplier Invoices (F0859) view appears. |  |
| 3 | Dialog Box | If the Data from Previous Invoice Entry Exist dialog box appears, choose No. |  |  |
| 4 | General Information | In the Basic Data section, enter the following data:Transaction: InvoicePurchase OrderCompany Code: <company code, for example, 1710>Invoicing Party: <invoicing party, for example, 17300001>Gross Invoice Amount: <the amount of the PO above>Currency: <currency code, for example, USD>Invoice Date: <Today's date>Posting Date: <Today's date>Reference: <any> |  |  |
| 5 | PO Reference | In the PO References section,Reference Document Category: <company code, for example, 1710>Purchase 1710>Purchase Order: <Purchase Order from above> |  |  |
| 6 | Grant Specialist | “Comm/act line item display” Fiori App (W0151)Enter: Grant: | The invoice was posted to the correct GM account assignments.The PO commitment was reduced by the invoice amount. |  |

### Charge an Indirect Cost to a Grant

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you charge an indirect cost to a grant according to the IDC settings in the grant.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori launchpad as a Grant Specialist. |  |  |
| 2 | Access the SAP Fiori App | Open Application Jobs - Grants Management (F6218). | The Application Jobs (F6218) view appears. |  |
| 3 | Create job | Choose Create. | The job creation guided procedure appears. |  |
| 4 | Choose template | Choose the Job Template: <Grants Management Indirect cost Posting>Choose Step 2. | The scheduling options section appears. |  |
| 5 | Set scheduling option | Leave the Start immediately option selectedChoose Step 3. | The parameter section appears. |  |
| 6 | Set run parameters | Enter manually:Company Code: <company code, for example, 1710>Grant: Grant created previouslyCuttoff Date: todayDocument Type: SAText: anyDocument Date:<todayPosting Date: todayPosting Period: today's posting periodDeselect the test run flag. | The invoice was posted to the correct GM account assignments.The PO commitment was reduced by the invoice amount. |  |
| 7 | Schedule job | Choose Schedule. | A message that the job was scheduled and a list of jobs appear. |  |
| 8 | Check | Wait a short amount of time and then reload the job list by choosing Go.Once the job is finished, check the Results document. | The indirect cost was calculated according to the settings in the grant and the indirect cost was posted. |  |

### Create Resource-Related Billing Document

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you automatically create a billing document request for incurred expenses.

Prerequisities

Expenses are posted to the grant.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori launchpad as a Grant Specialist. |  |  |
| 2 | Access the SAP Fiori App | Open Manage Grants Billing Proposal (F5523). | A list of billing elements appears. |  |
| 3 | Search for billing elements with your grant | Enter the grant created previously in the grant search field and choose Go. |  |  |
| 4 | Choose billing element and prepare billing | Set the checkbox next to the billing element and choose Prepare Billing. |  |  |
| 5 | Submit a billing proposal | Choose Submit. | A message informing you that the billing document request was created appears.Make a note of the billing request number. |  |
| 6 | Log on | Log on to the SAP Fiori launchpad as Billing Clerk. |  |  |
| 7 | Access the SAP Fiori App | Open Create Billing Documents (F0798) app. | A list of billing items appears. |  |
| 8 | Post the billing document | Select the billing document request created previously.Choose Create Billing Documents. |  |  |
| 9 | Save the document | Choose Save. | The document has an actual number. |  |
| 10 | Post the document | Choose Post Billing Document. | A message informing you that the billing document was created appears. |  |
| 11 | Check Document | Log on as Grant Specialist.Use Commitment / Actual Line Item Analyzer (W0151) to check correct posting. |  |  |

### Grants Overview

Purpose

The Grants Overview includes analytic tabs from different perspectives for the Grant Specialist and Grant Responsible users.

| Tab# | Tab Name |
| --- | --- |
| 1 | Sponsors |
| 2 | Grants |
| 3 | Budget Consumption |
| 4 | Status |
| 5 | Sponsor Locations |
| 6 | Sponsored Assets |

Implementation Type

The following section is only relevant for SAP S/4HANA Cloud Public Edition.

Procedure: SAP Fiori

Access the activity as follows:

Procedure

| Test Step | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori launchpad as a Grant Specialist or a Grant Responsible user. | The SAP Fiori launchpad appears. |  |
| 2 | Access the app Grants Overview | Frontend: Fiori App:Open Grants Overview - (Obsolete) (F6174). | The Grants Overview appears. In the story, the Sponsors tab is displayed as a default. |  |
| 3 | Set the prompt for the charts on this tab | Edit Story Prompt.On the Set Variables dialog box, enter the prompt values and choose Set.For example:Valid From DateValid To DateNote Grants with the status Closed are not displayed. | The charts are refreshed with the data you have selected. |  |
| 4 | Access the tab | Based on the tab you want to view, you can choose from one of the following on the tab:SponsorsGrantsBudget ConsumptionStatusSponsor LocationsSponsored Assets | The respective tab page appears and the charts are loaded with the data you have selected.Note The standard longitude and latitude details for the Sponsored Location Details page can be customized using the SSCUI ID 180099. |  |

### Monitor Grants

Purpose

Monitor Grants (F7716) includes cards from different perspectives for the Grant Specialist and Grant Responsible users.

Implementation Type

The following section is only relevant for SAP S/4HANA Cloud Public Edition.

Procedure: SAP Fiori

Access the activity as follows:

Procedure

| Test Step | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori launchpad as a Grant Specialist or a Grant Responsible user. | The SAP Fiori launchpad appears. |  |
| 2 | Access the app Monitor Grants | Frontend: Fiori Overview page AppOpen Monitor Grants ( Monitor Grants (F7716). | The Monitor Grants appears. In the app, all the cards are displayed. |  |
| 3 | Set the filter from the filter criteria for the cards | Enter the filter criteria values and choose Go.For example:GrantGrant TypeStatusSponsor | The cards are refreshed with the data you have selected. |  |

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
- see-also :: [[03-financial-accounting-and-close/test-script-fund-accounting-7au-sap-s-4hana-cloud-public-edition-1206]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/71S_S4CLD2608_BPD_EN_XX.docx` — full document · extracted with `mammoth` · 50,196 chars in the whole document
