---
id: 16-two-tier-erp-and-central-finance/two-tier-project-based-services-procurement-between-headquarter-and-su
title: Two Tier - Project Based Services Procurement between Headquarter and Subsidiary (S4CLD2608_2T_Proj_ServiceProcurement)
description: "SAP S/4HANA Cloud Public Edition customer guide and test script for two-tier project-based services procurement: HQ on-premise/ECC buys services from a Cloud ERP subsidiary."
cluster: 16-two-tier-erp-and-central-finance
tags: [kb/two-tier-erp-and-central-finance, topic/two-tier-professional-services-projects]
aliases: [S4CLD2608_2T_Proj_ServiceProcurement]
keywords: [Two-Tier Professional Services Projects, two-tier erp, project based services procurement, customer project management, customer project billing, billing proposals, timesheet recording, integration apis, contingent workers, work package staffing]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/General/Two-Tier_ERP_Assets_User_Guides/Two-Tier_ERP_Assets_User_Guides/Procurement/S4CLD2608_2T_Proj_ServiceProcurement.docx]
confidence: low
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-245
topic: 16-two-tier-erp-and-central-finance/two-tier-professional-services-projects
language: ""
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Two Tier - Project Based Services Procurement between Headquarter and Subsidiary (S4CLD2608_2T_Proj_ServiceProcurement)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/General/Two-Tier_ERP_Assets_User_Guides/Two-Tier_ERP_Assets_User_Guides/Procurement/S4CLD2608_2T_Proj_ServiceProcurement.docx`, extracted with `mammoth`. Grouped under **Two-Tier Professional Services Projects** in Two-Tier ERP and Central Finance. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

|  |  |
| --- | --- |
| S/4HANA CloudPublic Edition June 2026English |  |
|  | Project Based Services Procurement between Headquarters and Subsidiary |
| SAP SEDietmar-Hopp-Allee 1669190 WalldorfGermany | Customer Guide |

Copyright

© 2020 SAP SE or an SAP affiliate company. All rights reserved.

No part of this publication may be reproduced or transmitted in any form or for any purpose without the express permission of SAP SE. The information contained herein may be changed without prior notice.

Some software products marketed by SAP SE and its distributors contain proprietary software components of other software vendors.

National product specifications may vary.

These materials are provided by SAP SE and its affiliated companies ("SAP Group") for informational purposes only, without representation or warranty of any kind, and SAP Group shall not be liable for errors or omissions with respect to the materials. The only warranties for SAP Group products and services are those that are set forth in the express warranty statements accompanying such products and services, if any. Nothing herein should be construed as constituting an additional warranty.

SAP and other SAP products and services mentioned herein as well as their respective logos are trademarks or registered trademarks of SAP SE in Germany and other countries. Please see http://www.sap.com/corporate-en/legal/copyright/index.epx#trademark for additional trademark information and notices.

| Revision | Change Date | Description |
| --- | --- | --- |
| 0 | 22.05.2018 | Initial version of document |
| 1 | 10.05.2020 | Validation of earlier version |

Icons

| Icon | Meaning |
| --- | --- |
| <!-- image omitted: unnamed --> | Caution |
| <!-- image omitted: unnamed --> | Example |
| <!-- image omitted: unnamed --> | Note |
| <!-- image omitted: unnamed --> | Recommendation |
| <!-- image omitted: unnamed --> | Syntax |

Typographic Conventions

| Type Style | Description |
| --- | --- |
| Example text | Words or characters that appear on the screen. These include field names, screen titles, pushbuttons as well as menu names, paths and options.Cross-references to other documentation. |
| Example text | Emphasized words or phrases in body text, titles of graphics and tables. |
| EXAMPLE TEXT | Names of elements in the system. These include report names, program names, transaction codes, table names, and individual key words of a programming language, when surrounded by body text, for example, SELECT and INCLUDE. |
| Example text | Screen output. This includes file and directory names and their paths, messages, source code, names of variables and parameters as well as names of installation, upgrade and database tools. |
| EXAMPLE TEXT | Keys on the keyboard, for example, function keys (such as F2) or the ENTER key. |
| Example text | Exact user entry. These are words or characters that you enter in the system exactly as they appear in the documentation. |
| <Example text> | Variable user entry. Pointed brackets indicate that you replace these words and characters with appropriate entries. |

Content

[1. Purpose 7](#_Toc515286994)

[2. Value Proposition 7](#_Toc515286995)

[2.1 Business Requirement 7](#_Toc515286996)

[2.2 Two-Tier Solution 7](#_Toc515286997)

[3. Business Process Details 7](#_Toc515286998)

[4. Prerequisites 8](#_Toc515286999)

[5. Process Flow with Technical Details 9](#_Toc515287000)

[6. Technical Requirement 9](#_Toc515287001)

[6.1 Integration Requirements by using API 9](#_Toc515287002)

[6.2 Integration Requirements by using EDI/IDOC 10](#_Toc515287003)

[6.3 Reporting Requirements by using Analytical CDS Views 10](#_Toc515287004)

[6.4 Reporting Requirements by using Analytical API 10](#_Toc515287005)

[7. Master Data 11](#_Toc515287006)

[7.1 Master Data for SAP S/4HANA On Premise or ECC 11](#_Toc515287007)

[Vendor Master 11](#_Toc515287008)

[7.2 Master Data for SAP Cloud ERP 11](#_Toc515287009)

[Customer Master 11](#_Toc515287010)

[8. Test Script 12](#_Toc515287011)

[8.1 Roles 12](#_Toc515287012)

[Role at subsidiary: 12](#_Toc515287013)

[Role at Headquarter: 12](#_Toc515287014)

[8.2 Master Data, Organizational Data, and Other Data 13](#_Toc515287015)

[8.3 Preliminary Steps 15](#_Toc515287016)

[8.3.1 Check and Maintain the Service Cost Level for Employees 15](#_Toc515287017)

[8.3.2 Check and Maintain Cost Rates 17](#_Toc515287018)

[8.3.3 Check Sales Price 18](#_Toc515287019)

[8.3.4 Check and Maintain Service Organizations 19](#_Toc515287020)

[8.3.5 Manage Teams and Responsibilities 21](#_Toc515287021)

[8.3.6 Set up Threshold and Agent Rules 22](#_Toc515287022)

[8.4 Test Procedure 25](#_Toc515287023)

[8.4.1 Creation of Purchase Order at Headquarter 25](#_Toc515287024)

[8.4.2 Read Purchase Order (Visibility Scenario) 25](#_Toc515287025)

[8.4.3 Create a New Customer Project 26](#_Toc515287026)

[8.4.4 Copy a Project as Basis for New Project 27](#_Toc515287027)

[8.4.5 Maintain Work Packages and Time-Based Planning 28](#_Toc515287028)

[8.4.6 Maintain Work Package Staffing 31](#_Toc515287029)

[8.4.7 Maintain Customer Project Billing 34](#_Toc515287030)

[8.4.8 Capture Service Units (optional) 40](#_Toc515287031)

[8.4.9 Time Recording through Manage My Timesheet 41](#_Toc515287032)

[8.4.10 Time Recording for Contingent Worker 46](#_Toc515287033)

[8.4.10.1 Optional: Create Task through Manage My Timesheet 46](#_Toc515287034)

[8.4.10.2 Time Recording through Manage My Timesheet 47](#_Toc515287035)

[8.4.11 Approval of Working Times 51](#_Toc515287036)

[8.4.12 Maintain Customer Project Billing Proposal 52](#_Toc515287037)

[8.4.13 Release Customer Project Billing Proposal 55](#_Toc515287038)

[8.4.14 Billing 56](#_Toc515287039)

[8.4.14.1 Processing of Existing Debit Memo Requests 57](#_Toc515287040)

[8.4.14.1.1 Create Customer Invoices 57](#_Toc515287041)

[8.4.14.1.2 Creation of Supplier invoice at headquarter 58](#_Toc515287042)

[8.4.14.1.3 Manage Customer Invoices (Optional) 59](#_Toc515287043)

[8.4.15 Review Customer Project 60](#_Toc515287044)

[8.4.16 Headquarter visibility of the project status 61](#_Toc515287045)

[8.4.17 Headquarter visibility of the Credit Memos and Debit Memo Requests (created at the subsidiary) 61](#_Toc515287046)

[8.4.18 Set Project Status (Completed) 62](#_Toc515287047)

[8.4.19 Close Customer Projects 63](#_Toc515287048)

Two Tier - Project Based Services Procurement between Headquarter and Subsidiary

## **Purpose**

This document provides detailed Two-Tier approach for procurement of Project based Services between Headquarter and Subsidiaries, including process flow, technical requirements and Test script.

## **Value Proposition**

### **Business Requirement**

Even though the End customer signs a deal/contract with the Headquarter (HQ), the HQ can take the support of Subsidiaries for the implementation of the project (full or partial). Also, subsidiaries implement projects for their HQ. The subsidiary then bills HQ for the services provided. During the project, HQ needs visibility on the progress of the Project, Credit and Debit Memos created.

### **Two-Tier Solution**

With Two-Tier approach, SAP Cloud ERP solution will be deployed on Subsidiary and integrates with Headquarters which runs on SAP S/4HANA On-Premise / SAP ERP solution.

The following business benefits will be achieved with the procurement of project-based services from subsidiary:

- Headquarter to implement their Projects effectively.
- Headquarter to have a visibility of the projects, managed in the subsidiary system (SAP Cloud ERP)
- Reduces manual intervention in the business process between HQ and Subsidiary
- Real time automation of the invoicing process between Subsidiary and Headquarter.

## **Business Process Details**

The process starts with creation of the Purchase Order at the Headquarter. The delivery schedule (project deliverable-based) should be maintained in the Purchase Order. This sets the expectation for the subsidiary.

Subsidiary is maintained as the Vendor/Supplier in the Purchase Order. Hence, the subsidiary can filter and view the Purchase Orders created at the Headquarters, based on the vendor/supplier. This is done via the visibility application on the SAP Cloud Platform.

The subsidiary identifies the Project Manager, who in turn creates the Customer Project. Work Packages and Work Items are defined based on the deliverables. Also, roles are identified for the execution of the project. In case, the Project Manager requires a specific resource for the execution, he/she can mention at the “Roles”. The resource manager will check the availability of the specific resource during the staffing process.

The project manager raises Purchase Orders in case contingent workers or materials are required for the project execution.

To define the billing contract type, including the detailed billing plan, the project status is set to “Contract Preparation”. The Sales Order is auto-generated after the maintenance of the billing plan. The project manager can maintain project-specific service rates, if required. The Purchase Order number (from the HQ) should be maintained in the Project.

Once the project is in “In Execution” status, the consultants can start work and book time against the Project.

The Project Manager tracks the project progress in SAP Cloud ERP. The Headquarter can also view the project progress via visibility application on the SAP Cloud Platform.

Based on the billing plan, the subsidiary creates customer invoice. This in turn leads to the creation of Supplier Invoice (auto-generation based on integration) in the Headquarters’ system. The Headquarter settles the subsidiary invoice and the project is closed.

## **Prerequisites**

The following list of prerequisites are to be in place to realize the business process:

- Subsidiary should be running on SAP Cloud ERP system and Headquarters on SAP S/4HANA On Premise or ECC
- Activate the Scope ID J11, J12, J13, J14 and 2EL at the Subsidiary’s SAP Cloud ERP system. The customer can choose to activate Advanced Resource Management functionality (Scope ID 1KC) or use 2MV. Also, the scope items relevant for finance such as J59, J55 etc. should be activated.
- Create the required Apps/Reports for extracting information at the Headquarters’ On-Premise ERP or Subsidiary’s S/4HANA Cloud system on SAP Cloud Platform (Visibility Scenarios)
- Headquarters will be represented as a customer in Subsidiary and Subsidiary will be represented as a supplier in Headquarters.

## **Process Flow with Technical Details**

**Subsidiary**

**Headquarter**

<!-- image omitted: unnamed -->

The following integration points are depicted above:

1. Subsidiary’s visibility over the Purchase Orders created by the Headquarters
2. Headquarters’ visibility over the Engagement Project status, run by Subsidiary
3. Creation of Supplier Invoice at Headquarter based on the generation of customer invoice at the Subsidiary.
4. Headquarters’ visibility over the Credit Memo Requests and Debit Memo requests created at the Subsidiary.

## **Technical Requirement**

### **Integration Requirements by using API**

The following APIs are suggested for running the end-to-end process:

| **API Name** | **API Description** |
| --- | --- |
| /CPD/SC_EXTERNAL_SERVICES_SRV | Read Commercial Project Details from SAP Cloud ERP |
| API_CREDIT_MEMO_REQUEST_SRV | Read Credit Memo Request |
| API_DEBIT_MEMO_REQUEST_SRV | Read Debit Memo Request |

The above APIs can be used for realizing the visibility scenarios (via SAP Cloud Platform).

### **Integration Requirements by using EDI/IDOC**

**In SAP Cloud ERP:**

Use Communication Scenario **SAP_COM_0223**. The details of setting up this scenario will be found in Set-up instruction guide for scope ID **2EL** in the SAP Best Practices Explorer.

In this scenario, we would be integrating the SAP Cloud ERP (supplier system creating the billing document) with On-Premise (Buyer system where supplier invoice is generated). Check the section “Deployment and Configuration of Invoice Request Integration Flow”. You also need to do the relevant set-up mentioned in the document.

**In SAP S/4HANA On Premise:**

The On-Premise will use the IDOC, INVOIC02 to create the supplier invoice.

Mapping between the IDOC and SOA service fields in the I-flow is provided by SAP. This is part of standard deliverable " Integration of SAP Cloud ERP for Sales with SAP S/4HANA or SAP ERP àReceive supplier invoice” ([https://api.sap.com](https://api.sap.com)).

### **Reporting Requirements by using Analytical CDS Views**

The following CDS views can be used to extract information about Engagement Project and Credit and Debit memo requests from Subsidiary’s SAP Cloud ERP to Headquarter:

| CDS View Name | Description |
| --- | --- |
| [I_ENGAGEMENTPROJECT](https://my300163.s4hana.ondemand.com/ui#CDSView-browse?View=I_ENGAGEMENTPROJECT) | Engagement Project |
| [I_SALESDOCUMENT](https://my300163.s4hana.ondemand.com/ui#CDSView-browse?View=I_SALESDOCUMENT) | Sales: Sales Document |

### **Reporting Requirements by using Analytical API**

None.

## **Master Data**

### **Master Data for SAP S/4HANA On Premise or ECC**

#### Vendor Master

Subsidiary is maintained as the supplier at the headquarter. The customer number maintained against the headquarters in the subsidiary should be specified in the field “Account with supplier”.

<!-- image omitted: unnamed -->

HQ’s Customer number at Subsidiary should be maintained here

### **Master Data for SAP Cloud ERP**

#### Customer Master

The headquarter should be maintained as a customer in subsidiary. The supplier number of the subsidiary at the headquarter should be provided in the field “Account at customer”

<!-- image omitted: unnamed -->

Subsidiary’s supplier # at the HQ should be maintained here

## **Test Script**

### **Roles**

#### Role at subsidiary:

| **Business Role** | **Business Role as Delivered by SAP** |
| --- | --- |
| Project Manager - Commercial Services | SAP_BR_PROJ_MANAGE_COMM |
| Employee | SAP_BR_EMPLOYEE |
| Overhead Accountant | SAP_BR_OVERHEAD_ACCOUNTANT |
| Billing Clerk | SAP_BR_BILLING_CLERK |
| Internal Sales Representative - Professional Services | SAP_BR_INTERNAL_SALES_REP_PRSV |
| Business Process Specialist | SAP_BR_BUSINESS_PROCESS_SPEC |
| Configuration Expert - Business Process Configuration | SAP_BR_BPC_EXPERT |

#### Role at Headquarter:

| **Business Role** | **Business Role as Delivered by SAP** |
| --- | --- |
| Purchaser | SAP_BR_PURCHASER |
| Purchasing Manager | SAP_BR_PURCHASING_MANAGER |
| Accounts Payable Accountant | SAP_BR_AP_ACCOUNTANT |

### **Master Data, Organizational Data, and Other Data**

The organizational structure and master data of your company is created in your system during implementation. The organizational structure reflects the structure of your company. The master data depends on the operational focus of your company and represents, for example, materials, customers, and vendors.

Use your own master data to go through the test procedure. If you have installed an SAP Best Practices package, you can use the following scenario data.

Below Master data is maintained at SAP Cloud ERP system.

| Data | Sample Value | Details | Comments |
| --- | --- | --- | --- |
| Service Organization / Delivery Organization | Service Organization – Company DE | The following Enterprise Structures are assigned to the Service Organization:Controlling Area A000Company Code 1010Cost Centre 10101902, 10101903, 10101904Plant 1 DEDistribution Channel 10Division 00Sales Organization 1010 | The service organization Service Organization – Company DE is also defined as delivery organization. |
| Cost Centre | Csltg Unit ACsltg Unit BCustomer Dev | 101019021010190310101904 |  |
| Profit Centre | Consulting Unit AConsulting Unit BCustomer Development | YB101YB102YB103 |  |
| Customer/Sold to Party/Ship to Party/Payer | Domestic Customer DE 2 | 10100002 | The customer refers to the Headquarters’ business partner (mentioned in the section for “Master Data”) |
| Activity Types | T001 Junior ConsultantT002 Senior ConsultantT003 Platinum ConsultantT004 TrainerT005 Project ManagerT006 $ Time / Fee type 6 |  | If you need to create new activity types, use the placeholders already available in the system. |
| Cost Rate | Actual and planned cost rates are maintained for the following combination of cost centres / activity types:Cost centres: 10101902, 10101903, 10101904Activity types: T001 - T006 |  |  |
| Pricing Condition Records | Pricing condition records are maintained for the following materials:T001 - T006 | Only the following key combinations are visible in the service price list:For standard prices: Material with release statusFor project-specific prices: Cust Proj/Material | Pricing condition records are used in the Service Price list to calculate Project Planned Revenues.If you use other key combinations, the system can use them for pricing but you cannot display or change them in the service price list. |
| Material | P001 | Project Based Service: Fixed Price | Material which will be used in order to describe different services being provided to the customer |
| Material | P002 | Project Based Service: Time &amp; Expenses | Material which will be used in order to describe different services being provided to the customer |
| Material | P003 | Periodic Service | Material which will be used in order to describe different services being provided to the customer |
| Material | H001 | Hardware 01 |  |
| Material | H002 | Hardware 02 |  |
| Material | T001 | Junior Consultant |  |
| Material | T002 | Senior Consultant |  |
| Materials | T003 to T020 | Time Recording: Rate Type 03 to 20 |  |
| Material | E001 | Accommodation |  |
| Material | E002 | Airfare |  |
| Material | E003 | Ground Transportation |  |
| Material | E004 | Miscellaneous |  |
| Materials | E005 to E040 | Billable Expenses 05 to 40 |  |
| Materials | L001 | Licences 001 |  |
| Material | U001 | Cloud Sales Licences |  |
| Material | U002 | Service Centre Tickets |  |
| Material | U003 to U010 | Incidents Monitoring |  |

Allowed changes to the above listed service-related materials are limited to descriptions and some attributes, since they are provided with DIP-Profile, a technical object necessary for selling of project-based services.

For more information on creating master data objects, see the following Master Data Scripts (MDS):

Table 1: Master Data Script Reference

| Master Data ID | Description |
| --- | --- |
| BNM | Create Cost Centre and Cost Centre Group |
| BND | Create Customer |
| BNN | Create Activity Type and Activity Type Group |

### **Preliminary Steps**

You should complete the below set of steps to execute the customer project in SAP Cloud ERP.

#### Check and Maintain the Service Cost Level for Employees

Context

Controller can assign a cost level to an employee to determine the usual standard cost rate of the employee.

**Note**: To be able to search for Employees and maintain the Service Cost Level, make sure that the business role SAP_BR_EMPLOYEE is assigned to the user Overhead Accountant.

Procedure

| **Test Step #** | **Test Step Name** | **Instruction** | **Expected Result** | **Pass/Fail/Comment** |
| --- | --- | --- | --- | --- |
| 1 | Logon | Logon to the SAP Fiori launchpad as Overhead Accountant. | The Home page appears. | OK |
| 2 | Search for Employee | Choose the Search button on the toolbar. Filter for Employees and search for an Employee. |  | OK |
| 3 | View Employee Fact Sheet | Select the Employee to view the employee fact sheet. | The Employee Fact Sheet with the Employee information is displayed: cost centre, contacts, employments details, service cost level and project history are available for detailed analysis.Note To be able to display Payment information for the employee, the Business Catalog SAP_HCM_BC_EMP_PI_DSP_PC need to be manually assigned to the Business Role. | OK |
| 4 | Assign the Service Cost Level | Choose Controlling Information tab, and choose Edit.Assign the relevant Service Cost level to the employee (on the Service Cost Level dialog box, choose Go to display the service cost levels) and the Start Date.For example:Service Cost Level: 4 (SENIOR CONSULTANT (K4))Start Date: TodaySave and go back. | The Service Cost Level is assigned to the employee. | OK |

#### Check and Maintain Cost Rates

Context

This step describes how to check and maintain the actual and planned cost rates.

Procedure

| **Test Step #** | **Test Step Name** | **Instruction** | **Expected Result** | **Pass/Fail/Comment** |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori launchpad as Overhead Accountant. | The Home page appears. | OK |
| 2 | Access the SAP Fiori App | Open Manage Cost Rates -Professional Services. | The Manage Service Cost Rates screen displays. | OK |
| 3 | Check Cost Rate with Selection Criteria | Make the following entries:Company Code: Company for which you want to enter ratesValid On: Current Date or start of a period |  | Company code of the subsidiary is maintained hereOK |
| 4 | Maintain Additional Cost Rates | Select Add. | Pop-up of Create Cost Rate(s)-Company Code e.g. 1010 | OK |
| 5 | Enter Cost Rates | Make the following entries:Company Code: Company for which you want to enter ratesCost Centre: example 10101902Activity Type: example T002Service Cost Levels: optionalWork item ID: optionalPersonal Number: optionalWBS Element: optionalFrom Fiscal Year: Current YearFrom Period: Current PeriodVariable Amount: e.g. 100Currency: e.g. your company code currency EURPer: 1Activity Unit: example H | Cost rates have to be as per customer business requirement.This step is using content sample master data Few Hints:At least one of the fields: Activity Type, Service Cost Levels or Personnel Number - must be filled.Personnel Number and Cost Centre exclude each other as key fields for one price.Personnel Number and Service Cost Levels exclude each other as key fields for one price.Company Code to be billed shall be filled when WBS Element is filled. | You would maintain the company code of the Headquarter as the “Receiving company code”OK |
| 6 | Save | Click Save. | Additional cost rates are created. | OK |

#### Check Sales Price

Context

This step describes how to check the sales price.

Procedure

| **Test Step #** | **Test Step Name** | **Instruction** | **Expected Result** | **Pass/Fail/Comment** |
| --- | --- | --- | --- | --- |
| 1 | Logon | Log on to the SAP Fiori launchpad as a Project Manager - Commercial Services. | The Home page appears. | OK |
| 2 | Access the SAP Fiori App | Select Set Service Prices. | The Change Condition Record screen displays. | OK |
| 3 | Check Sales Price | Select the Condition Type PSP0 and choose Enter.Choose the combination Key Material with release status and choose Enter.Make the following entries and choose Execute:Sales Org.: 1010Distribution Channel: 10Material: From T001 to T005Choose Save. | Sales Prices are maintained for the five materials/roles.Project Planned Revenues for the different roles are calculated based on these values. | OK |

#### Check and Maintain Service Organizations

Context

This step describes how to check and maintain the existing service organization, and how to create new service organizations.

The following organization units are assigned to the Service Organization:

- Controlling Area
- Company Code
- Sales Organization
- Distribution Channel
- Division
- Plant
- Cost Center

If you have created your own organization units, you can create new Service Organizations to be used in the project.

Procedure

| **Test Step #** | **Test Step Name** | **Instruction** | **Expected Result** | **Pass/Fail/Comment** |
| --- | --- | --- | --- | --- |
| 1 | Logon | Log on to the SAP Fiori launchpad as a Project Manager - Commercial Services. | The Home page appears. | OK |
| 2 | Access the SAP Fiori App | Open Maintain Service Organizations. | The Service Organization screen displays. | OK |
| 3 | Check a Service Organization | On the Service Organization screen, the Customer Project Manager can view the existing service organizations. | The existing service organizations are displayed. | OK |
| 4 | Check a Service Organization | On the Service Organization screen, select a service organization and choose the Edit button.Change for example, the name of the Service Organization or update the organization units or assign the missing ones.Save the entries and go back. | The service organization is updated. | OK |
| 5 | Create a new Service Organization (optional) | On the Service Organization screen, choose the Create button. Make the following entries:ID: Z001Name: New Serv.Org Z001Select the two fields: Sales Organization and Delivery Organization. Assign your own organization units.Save the entries and go back. | The new service organization with your own organization units is created.It is only possible to assign a cost centre once to a Service Organization. In order to use the newly created Service Organization, make sure:To maintain the cost rates for your own cost centre (see chapter 2.4.2 Check and Update Cost Rates)To assign the cost centre to the employees to be staffed on the project. | OK |

If you need to activate workflow for credit memo, then follow the sections 7.3.5 and 7.3.6.

#### Manage Teams and Responsibilities

Context

In this activity, you maintain the teams and responsibilities for credit memo workflow.

Procedure

| **Test Step #** | **Test Step Name** | **Instruction** | **Expected Result** | **Pass / Fail / Comment** |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori Launchpad using the Business Process Specialist role. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Teams and Responsibilities. | The Manage Teams and Responsibilitiesscreen displays. |  |
| 3 | Create A New Team | Choose the Create Team button to create a new team. | Navigates to the window of new team. |  |
| 4 | Input Team | Make the following entries and choose Enter:Name: credit memo workflowDescription: credit memo workflowStatus: Ready to UseType: SALES | Users created a new team and appropriate function(s) have been assigned to the business user(s) to be configured as approver(s). |  |
| 5 | Add Team Members | In Team Members, Choose Create.Choose Select button, in the Select: Business Partner window, fill in the following entry and choose Enter.Last Name: PROJ_MANAGE_COMMAfter you choose the workflow approver as project manager, you need to assign business catalog SAP_SD_BC_DMR_CMR_DISPL_PC into the business role SAP_BR_PROJ_MANAGE_COMM of project manager. This action is required for the following approval process by project manager. | Team is saved. | Last Name: PROJ_MANAGE_COMMNot setup |
| 6 | Add Function to Team Members | In Function field, Choose Select, and in the Select: Functions window, choose the following functions, and choose OK.CMR1LVLA: Credit Memo Request first level ApprovalCMR2LVLA: Credit Memo Request second level ApprovalChoose Save to save the team. |  |  |
| 7 | Check Team Status | Navigate to the Manage Teams and Responsibilities worklist and verify the status of the team.The status should be Ready to Use. | Team status is ready to use. |  |

#### Set up Threshold and Agent Rules

Context

In this activity, you set up threshold and agent rules.

Procedure

| **Test Step #** | **Test Step Name** | **Instruction** | **Expected Result** | **Pass / Fail / Comment** |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori Launchpad using Configuration Expert – Business Process Configuration role. | The SAP Fiori launchpad displays. | No specific user ID? |
| 2 | Access the App | Open Manage Credit Memo Request Workflow. | The Manage Workflowsscreen displays. | Could not find APP Manage Credit Memo Request Workflow. |
| 3 | Create Workflows | Choose Add to create new workflows:First Approver- Net Value over 500 USDSecond Approver- Net Value over 1000 USDAutomatic ReleaseIf the workflows have been already defined, please skip step 4 to 7 | The new workflow window appears. |  |
| 4 | Set Preconditions for New Workflow | Make the following entries and choose Enter:Name: First Approver- Net Value over 500 USDPreconditions: Is credit memo request blocked and Net Amount greater thanAmount: 500Currency: USD | Set preconditions |  |
| 5 | Add Steps for Defining the Workflow | Choose Add in Steps, in the new window of Handling of the credit memo request, input the entries below.Header Type: Handling of the credit memo requestAssignment By: Credit Memo Request first level ApprovalIn the Exception Handling section:Name: Rework Credit Memo RequestRequired Action: Change Credit Memo RequestAction Result: Restart workflowThen choose Add to append this step to the workflow and choose Save. | The new workflow is saved |  |
| 6 | Create 2nd Workflow | Choose Back to the screen Manage workflows, Choose Add to create the second workflow.In the New Workflow screen, make the following entries:Name: Second Approver- Net Value over 1000 USDPreconditions: Is credit memo request blocked and Net Amount greater thanAmount: 1000Currency: USDChoose Add in Steps, in the new window of Handling of the credit memo request, input the entries below.Header Type: Handling of the credit memo requestAssignment By: Credit Memo Request second level ApprovalIn the Exception Handling section:Name: Rework Credit Memo RequestRequired Action: Change Credit Memo RequestAction Result: Restart workflowThen choose Add to append this step to the workflow and choose Save. |  |  |
| 7 | Create Automatic Release Workflow | Choose Back to the screen Manage Workflows, Choose Add to create the next workflow.In the New Workflow screen, make the following entries:Name: Automatic ReleasePreconditions: Is credit memo request blockedChoose Add in Steps, in the new window of Handling of the credit memo request, put the entries below.Header Type: Handling of the credit memo requestThen choose Add to append this step to the workflow and choose Save. |  |  |
| 8 | Create the Workflow Order | Choose Back to the Manage Workflows and choose Define Order, adjust the order as below:Automatic Release: Order 3Second Approver-Net value over 1000 USD: Order 2First Approver-Net value over 500 USD: Order 1And choose Activate to active the workflow. |  |  |

### Test Procedure

### Creation of Purchase Order at Headquarter

Context

As headquarter, you need to implement the project for your customer. However, you would like to implement this project via your subsidiary. Hence, you need to create the purchase order in your ECC or S/4HANA On-premise system.

Procedure

As a purchaser, you create the purchase order, with detailed delivery schedule in the on-premise system. The subsidiary is maintained as the vendor in the PO.

### Read Purchase Order (Visibility Scenario)

Context

The project manager at the subsidiary should have the visibility of the purchase order created at the headquarter.

Procedure

The end user of this guide should create a visibility application on SAP Cloud Platform. This Fiori application will utilize the API available on the ECC or S/4HANA on-premise to populate the purchase order relevant data (including Delivery Schedule). The Project manager at the subsidiary can filter the Purchase orders based on the vendor (subsidiary would be listed as the vendor in the PO).

### Create a New Customer Project

Context

In this step, you create a new customer project. This is based on the purchase order created at the headquarter for the implementation of the Project at the subsidiary.

Procedure

| **Test Step #** | **Test Step Name** | **Instruction** | **Expected Result** | **Pass / Fail / Comment** |
| --- | --- | --- | --- | --- |
| 1 | Logon | Log on to the SAP Fiori launchpad as a Project Manager - Commercial Services. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Create Customer Projects. | The Create Customer Project app displays. |  |
| 3 | Maintain Customer Project Information | Make the following entries, starting from the right-hand side:Service Organization: Service Organization – Company DECost Centre: Csltg Unit AProfit Centre: Consulting Unit ACustomer: Domestic Customer DE 2Project Name: XXXXProject ID: XXXXXStage: In PlanningDuration: Start Date: Today’s Date - 2End Date: today + 4 monthsCurrency: EUR - EuroDescription: XXXXXX | Note: The Profit Centre is changeable until the first posting is done.Maintain the project name, ID and description. |  |
| 4 | Save your entries | Choose the Save button. | The system displays the message Project created and saved. |  |
| 5 | Maintain Project Roles | Choose the Edit button. To add a new Project Roles, choose the + (plus) button. Make the following entries in the Project Roles fields:Project Partner: Enter a valueProject Controller: Enter a valueProject Accountant: Enter a value |  |  |
| 6 | Attach Documents on Project Header Level | Choose the Attachments view.To add a new document, choose the + (plus) button. Select the document and choose the Open button to attach the document. | Attached documents are listed.New documents are added as attachments to the project. |  |
| 7 | Save your entries | Choose the Save button. | Project is saved. |  |

### Copy a Project as Basis for New Project

Context

You can make a copy of an existing customer project to create a new customer project.

Procedure

| **Test Step #** | **Test Step Name** | **Instruction** | **Expected Result** | **Pass / Fail / Comment** |
| --- | --- | --- | --- | --- |
| 1 | Start to Create Customer Projects | Open Plan Customer Projects. | The Customer Project sub-screen is displayed. |  |
| 2 | Choose Template Project | Choose a Customer Project to use as a template. | You have marked the template for the copying process. |  |
| 3 | Filter My Projects List | To filter the Customer Project section, in the Search field, enter some text to start searching and choose the Search button.You can also use the following search parameters:Project manager nameCustomer nameIn addition, you can filter the search result to display projects defined as Favorite or projects in a defined state.Enter some text to search. | The Search Result section displays the filtered results. |  |
| 4 | Copy Customer Project | Select a project to use as a template and choose the Copy button.In the dialog box, select the options for what to copy (Work Packages or Work Packages and Roles) . To change the proposed start date, select the option New Start Date. Choose OK. | The new project information screen is populated automatically. |  |
| 5 | Save Project | Maintain or change any relevant information for the new project and save it when done (see [Maintain Work Packages and Time-Based Planning](#unique_15) ) | The system displays the message:Project copied. |  |

### Maintain Work Packages and Time-Based Planning

Context

Once the project is created, you need to detail with work packages and time-based planning information.

Procedure

| **Test Step #** | **Test Step Name** | **Instruction** | **Expected Result** | **Pass / Fail / Comment** |
| --- | --- | --- | --- | --- |
| 1 | Logon | Logon to the SAP Fiori launchpad as a Project Manager - Commercial Services. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Plan Customer Projects. | The Customer Project screen displays. |  |
| 3 | Choose a Customer Project to Edit | On the Customer Project screen, the Customer Project Manager can view the assigned customer projects.The Customer Project Manager can search the project using the Search field or filter the list using the Filter button.To start work on staffing and work packages, choose the project XXXX (created in the last step).The project information is displayed.To edit the project, choose the Edit button. | Project XXXX is available for further editing. |  |
| 4 | Choose Work Packages View | Choose Work Packages. | The Work Package details page displays. |  |
| 5 | Update the First Work Package | The first work package is proposed by default.Replace the proposed entries with the following entries:Name: <Maintain the details as per the Project requirement>Start Date: <enter the start date>End Date: <Enter the end date for the work package>Description: <Maintain suitable descrition>Save the entries. | The new work package is updated and displayed on the details screen. |  |
| 6 | Create Further Work Packages | To create a new work package, choose the + (Add) button.Make the following entries and choose the OK button.NameStart DateEnd DateDescription: Save the entries. | The messageWork Package update successfulis displayed. |  |
| 7 | Assign Work Items to the Work Package | To assign work items to an existing work package, choose the Select button.Assign the work item, for e.g. Wok Items ID P001 Documentation, to the work package.Choose the OK button and save the entries.Repeat this step to assign work items to the relevant work packages.Assign existing work items to the work package. | Work Items are assigned to the work package.You can review the assigned work items by choosing the Assigned button. A dialog box appears. Choose Edit to add additional work items. |  |
| 8 | Add Roles to First Work Packages | Select the work package to display the Details screen.To add a new role, choose the + (Add) button in the top right corner for Team section.Make the following entries and choose the OK button.Work PackageRole: for e.g. Project ManagerDelivery Organization: Service Organization – Company DEWork Item: <Enter a value based on the work items selected at the work package>Effort (Hours): <# of hours required for completion of the work package>Repeat the steps if you want to maintain further roles required for the realization of the work packagesChoose Save and go Back.For each planned role, you can also select whether the effort is billable or not. Non-billable effort is not considered during the calculation of planned revenue, and not charged to the customer during the billing process. Please Click the Settings button to display the Billing Control Category in the table.The Recalculate button is available to distribute planned effort across the periods of the work package. By default, total effort is distributed equally. Readjustment of distribution is allowed across all periods of the work package. When there is a change in the dates of the work package, a message inform to review effort distribution (by default the planned efforts are kept as is for the existing plan periods; the new plan periods are planned with 0 efforts). | Assigned roles are listed for the work package.Planned Costs are automatically calculated from the Planned Effort.Planned Revenues are calculated based on the Service Price List.If you choose a different service organization, for example, Service Organization - Company US, an intercompany resource from company code 1710 is staffed and the business process Intercompany Processes - Project-Based Services (16T) is triggered. For more information, refer to the related test script. |  |
| 9 | Specify required skills | Choose the Skills button near the role to add the required skills.Enter the required skills in the text input box (for example: ABAP, HANA ..) and choose the Add button. | The required skills for the role are defined in addition to the location (delivery org) and the required effort.Note The type-ahead input field helps to select the already defined skills. A maximum of 5 skills can be assigned to each role. |  |
| 10 | Add Expense Type to the Work Package | Select the Work Package to display the Details screen. UseWork Package: <Select the work package created in the previous steps>To add a new expense, choose the + (Add) button in the right corner for Expense section.Make the following entries and choose the Save button.Expense Type: for e.g. AccommodationCosts: Enter a value (for example 2000)Revenue: Enter a value (for example, 2500) | Expenses are added to the work package.Planned costs and revenue are recalculated.You can maintain Expense Type by SSCUI with Fiori app Manage Your Solution. Search Define Resources. After it is selected, click the row to get information. . |  |
| 11 | Navigate to Details of Work Packages | Choose the Work Package to display the Details screen. | The staffed roles, planned effort, planned costs and planned revenues are displayed. |  |
| 12 | Attach Documents to Work Package | On the Work Package details screen, scroll to the Documents section. To add a new document, choose the + (Add) button. Select the document and choose the Open button to attach the document. | Attached documents are listed.New documents are added as attachments to the work package. |  |

### Maintain Work Package Staffing

Context

Once the roles have been assigned to the work packages, the project team can be staffed to specific work packages. These steps are performed by the Resource manager, in case 1KC is activated and the setting to assign resources by Resource Manager is activated.

Procedure

| **Test Step #** | **Test Step Name** | **Instruction** | **Expected Result** | **Pass / Fail / Comment** |
| --- | --- | --- | --- | --- |
| 1 | Logon | Logon to the SAP Fiori launchpad as a Project Manager - Commercial Services. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Plan Customer Projects. | The Customer Project screen is displayed. |  |
| 3 | View My Projects Header Data and Choose a Customer Project to Edit | On the Customer Projects screen, the Customer Project Manager sees all of the assigned Customer Projects.Choose the Project XXXX (created in an earlier step). Customer Project Information is displayed.Choose the Edit button. | Project XXXX is chosen and available for further editing. |  |
| 4 | Choose Work Packages View | Choose the Work Packages button. | The Work Package Overview screen is displayed. |  |
| 5 | Employee Staffing – Add Employee Assignment to Role in Work Package | Choose a work package to display the Details screen.For each role, to staff an employee, choose the Add Resource link.The system displays a list of employees already staffed in the selected role. Only the employees who belong to the delivery organization are displayed and can be staffed to a project.Select the Employee, select the checkbox, and choose Add to Role.Make the following entries and choose Save.You should do the steps for every role defined within the Work Package | A list of employees already staffed in the selected role is shown. If there are no names on the list, search for an employee as explained in the next step.The role is staffed. |  |
| 6 | Employee Staffing – Search for Employee | Choose a work package to display the Details screen.For each role, to staff an employee, choose the Add Resource button.In the Add Resource dialog, search for the relevant employee by name or role.Select the option Include Contingent Worker to include external/ freelance resources in the search. Also remove the role filter by selecting the X below the Include Contingent Worker option. This displays all employees.Select the employee, select the checkbox, and choose Add to Role.Save | Employees are staffed. |  |
| 7 | Employee Staffing – Availability | Choose a work package to display the Details screen.For each role, to staff an employee, choose the Add Resource button.In the Add Resource dialog, search for the relevant employee.Choose the See Availability link to display the monthly availability of the employee.Select the employee, select the checkbox, and choose Add to Role.Make the entries and choose Save. | The monthly availability of the employee is displayed:Availability is calculated by month based on weekly working hours of the employee.Number of working days in a month is calculated based on company code calendar of the employee.Already staffed days are deducted. |  |
| 8 | Employee Staffing – View Employee Fact Sheet | Choose a Work Package to display the Details screen.For each role, to staff an employee, choose the Add Resource button.In the Add Resource dialog, search for the relevant employee.Choose the selected employee to view the Employee Fact Sheet.Close the fact sheet in the new window, select the checkbox, and choose Add to Role.Make the entries and choose Save. | The Employee Fact Sheet with the Employee information is displayed: cost centre, contacts, employments details, service cost level, and project history are available for detailed analysis.From the Employee Fact Sheet, you can select the Project ID to navigate to the Project Fact Sheet or the Customer to navigate to the Customer Fact Sheet. |  |
| 10 | Employee Staffing – Remove Employee Assignment to Role in Work Package | Choose a Work Package to display the Details screen.To remove an employee, choose the X button next to the Role and choose Remove the employee but leave the role to staff it later in the dialog.Choose the Save button. | The staffed employee is removed. |  |
| 11 | Choose Team View | Go back and choose the Team button. | The team details page is displayed. You can use this view to add roles, staff employees, or adjust the already planned effort. |  |

### Maintain Customer Project Billing

Context

In this process step, the Customer Project Manager maintains the Project Billing information.

Procedure

| **Test Step #** | **Test Step Name** | **Instruction** | **Expected Result** | **Pass / Fail / Comment** |
| --- | --- | --- | --- | --- |
| 1 | Logon | Logon to the SAP Fiori launchpad as a Project Manager - Commercial Services. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Plan Customer Projects. | The Customer Project screen is displayed.Projects that are assigned to the Customer Project Manager are displayed. |  |
| 3 | View Projects Header Data and Choose a Customer Project to Edit | To start billing, choose the project XXXX (created in the previous step). | Project XXXX is displayed. |  |
| 4 | Edit Project | Choose the Edit button to edit project information. | You can now make changes to the project. |  |
| 5 | Change the Project Status | Make the following entry:Stage: Contract PreparationChoose Save. | The system displays the message: Project updated.The billing is now available for editing. |  |
| 6 | Choose Billing View | Choose the Billing button.Maintain the Purchase order number (from the headquarter) in the field “Customer Reference” | The billing details page is displayed.The PO # maintained in the “Customer Reference” flows down till the billing document. |  |
| 7 | Create Billing Item for Fixed Price | Make the following entries and choose Save.Contract Type: Fixed PriceAssigned Work Packages: <Select the work package>Profit Centre: Select profit centre by your requirementAmount to be billed: <Enter the amount>Description: Enter a description.The amount to be billed is based on the planned revenues of the assigned work-packages.OPTIONAL: To test the bundling functionality in context of IFRS15 use material ID PIF1 and enter a value for the stand alone selling price (Total SSP).Note For information regarding the bundling functionality in context of IFRS15, please refer to SAP note[2524569](https://service.sap.com/sap/support/notes/%0a%09%09%09%09%09%09%09%09%092524569). | The Billing Item for Fixed Price is created.The Material ID is editable on Billing tab for all contract types as long as the sales order item is created. Different sales materials can be used in the Billing tab. If those materials belong to different categories such as maintenance and service, this would have an impact in profitability analysis. P001 is used as the default material ID for fixed price. If not changed, the profit centre chosen when creating a new customer project in information level will be shown as default. In addition, if the profit centre is changed in information level, it will not update the ones in billing item automatically. |  |
| 8 | Create Billing Item for Time and Expenses | To create another billing item, choose the + (Add) button.Make the following entries and choose Enter.Contract Type: Time and ExpensesAssigned Work Packages: <Select the work packages>Profit Centre: Select profit centre by your requirementAmount to be billed: <Enter the amount>Description: Enter a description.The amount to be billed is based on the planned revenues of the assigned work-packages. | The Billing Item for Time and Expenses is created.If not changed, P002 is used as the default material ID for Time and Expenses. If not changed, the profit centre chosen when creating a new customer project in information level will be shown as default. In addition, if the profit centre is changed in information level, it will not update the ones in billing item automatically.Note The non-billable service assigned in work-pages is relevant for contract type Time and Expense and will not contribute to the calculation for planned revenues. |  |
| 9 | Create Billing Item for Periodic Services | To create another billing item, choose the + (Add) button.Make the following entries and choose Enter.Contract Type: Periodic ServiceAssigned Work Packages: (Select the work packages>Profit Centre: Select profit centre by your requirementAmount to be billed: <Enter the amount>Description: Enter a descriptionThe amount to be billed is based on the planned revenues of the assigned work-packages.OPTIONAL: To test the bundling functionality in context of IFRS15 use material ID PIF3 and enter a value for the stand alone selling price (Total SSP) | The Billing Item for Periodic Services is created.E.g. The fixed maintenance fee.If not changed, P003 is used as the default material ID for Periodic Services. If not changed, the profit centre chosen when creating a new customer project in information level will be shown as default. In addition, if the profit centre is changed in information level, it will not update the ones in billing item automatically. |  |
| 10 | Create Billing Item for Usage-based billing | To create another billing item, choose the + (Add) button. Make the following entries and choose Enter.Contract Type: Periodic ServiceMaterial ID: U001Assigned Work Packages: <Select the work package>Profit Centre: Select profit centre by your requirementAmount to be billed: <Enter amount>Description: Enter a descriptionThe amount to be billed is based on the planned revenues of the assigned work-packages. | The Billing Item for Periodic Services is created. This Periodic Services item will be used for usage based billing such as the number of licenses sold to the customer. In this scenario, Material ID U001 (instead of P003) is used. If not changed, the profit centre chosen when creating a new customer project in information level will be shown as default. In addition, if the profit centre is changed in information level, it will not update the ones in billing item automatically. |  |
| 11 | Save | Choose the Save button.Close the message and go back. | A Sales Order is created with the billing plan. Selected work packages are assigned to the Billing Item for Fixed Price; Time and Expenses, Periodic Services.On the General session, the sales order number is displayed. The Amount “To Be Billed (Total)” is the sum of the Amount to be billed for the different Contract types. This value is the value of the Sales order (contracted revenue) and can differ from the project planned revenues. |  |
| 12 | Create Billing Plan for Fixed Price | Select the Fixed Price Item. |  |  |
| 13 | Enter Billing Plan Details | Choose the + (Add) button to create billing items. Make the following entries and go back.Billing due date: <Enter the date>Note: <Maintain a description>Amount: <Enter amount> | A billing plan is created for Fixed Price.Another row is added automatically when previous row has been filled with no errors.You can maintain as many rows as required. |  |
| 14 | Create Billing Plan for Time and Expenses | Select the Time and Expenses Item. |  |  |
| 15 | Enter Billing Plan Details | Choose the + (Add) button to create billing items. Make the following entries and go back.Billing due date: <Enter the date>Item Usage: Payment on AccountAmount: <Specify the amount>Billing due date: <Enter the date>Item Usage: Time and ExpensesBilling due date: <Enter the date>Item Usage: Time and Expenses | A billing plan is created for Time and Expenses. |  |
| 16 | Create Billing Plan for Periodic Services | Select the Periodic Service item (Maintenance). |  |  |
| 17 | Enter Billing Plan Details | Choose the + button to create billing items. Make the following entries:Billing due date: <Enter the date>Item usage: Periodic ServiceAmount: <Specify the amount>Service start date: (maintain the start date for the service>Service end date: <maintain the end date of the service>Go back and save. | A billing plan is created for the fixed maintenance fee (Periodic Services).You can also use the copy function to create the billing plan.Select the billing date, select copy, and enter the periodicity (for example, every month) and the start/end dates. |  |
| 18 | Create Billing Plan for Usage-Based Billing | Select the Periodic Service item (Licenses). |  |  |
| 19 | Enter Billing Plan Details | Choose the + (Add) button to create billing items. Make the following entries and go back.Billing due date: todayItem Usage: Usage-Based BillingBilling due date: today + 1 monthItem Usage: Usage-Based Billing | This billing plan is used to collect the number of licenses sold to the customer in a certain period. |  |
| 20 | Maintain Project-Specific Price per Hours for Services (Service Price List) | Choose the corresponding Service Price List button. |  |  |
| 21 | Enter Prices | Maintain the Project specific value for the roles.e.g. Trainer: 90,00 EURChoose Enter.To save your entries, go to the previous screen by choosing < button on the top of the screen and choose Save. | The Service Price List shows all services with the standard price per hour. This price is used to calculate the planned revenue.The project-specific price per hour can be defined in this view. Planned revenues are recalculated based on these new prices. |  |
| 22 | Change the Project Status | Go back to the Information view to change the Project status.Make the following entry:Stage: In ExecutionChoose Save. | The system displays the messages:Project updatedBaseline version createdThe project is in execution phase now. A baseline version is automatically created. All the initial planned data including the cost details will be pushed to Finance ACDOCP automatically. |  |
| 23 | Choose Versions View | Choose the Versions button. | The Version details page is displayed. The baseline version can be compared with the Actual version.The Project Manager can always update the baseline version using the Update Baseline button. All the current updated planned data including the cost will be pushed to Finance ACDOCP again.During the update, only the version of those work packages that are selected will be updated. The versions of work packages that are not selected will be kept unchanged. |  |
| 24 | Confirm the Staffing | Go back and choose the Work Packages button.Choose a work package to display the Details screen.The list of staffed employees is displayed.Switch to On in the Confirmed column to confirm the staffing.Save the entries. Otherwise, you can switch to On in the Confirmed column directly from the Team tab. | Once all Employees are successfully staffed to a work package, the Staffing Status for the work package changes to Staffed (green) or Partially Staffed (yellow).In case, Advanced Resource Management - Project-Based Services (1KC) is activated, the Staff confirmation in the Staffed Resource column will be switched off. In addition, if the multiple resources were assigned to one role, the multiple resources will be shown in Staffed Resource column. Please refer to Advanced Resource Management - Project-Based Services (1KC) to perform the staffing. |  |

### Capture Service Units (optional)

Context

In this optional step, the usage-based services are captured in a project as a base for billing.

The possible use cases are:

- Billing of licenses over a time period
- Billing of support tickets raised by the customer
- Billing of calls to a support hotline

The calls and tickets might be related to a maintenance contract with a base amount of support services. Services exceeding the base amount are additionally billed to the customer.

Procedure

| **Test Step #** | **Test Step Name** | **Instruction** | **Expected Result** | **Pass / Fail / Comment** |
| --- | --- | --- | --- | --- |
| 1 | Logon | Log on to the SAP Fiori launchpad as Overhead Accountant. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Enter Activity Allocation. | The Enter Direct Activity Allocation screen displays. |  |
| 3 | Capture Service nit | On the Enter Direct Activity Allocation screen, select Scrn Var. (screen variant) = WBS element/order and Input Type = List Entry.Make the following entries.Doc. Date: TodayPostg Date: TodaySend. CCtr: 10101902SAty Typ: U001Receiver WBS element: <For example, I1000.1.4(Licenses)>Total Quantity: 10 PCSend. CCtr: 10101902SAty Typ: U002Receiver WBS element: <For example, I1000.1.4(Licenses)Total Quantity: 5 PCIgnore the following warning message:Pricing error: Mandatory condition CACT is missing.Choose Post and go back. | The Receiver WBS element is the work-package for which a Billing Plan for Usage-Based Billing has been created (in this example: the work package Licenses). Document is posted. Service units (that is number of licenses sold to the customer in a certain period) are captured. |  |

### Time Recording through Manage My Timesheet

Context

In this activity, you perform the time recording process through the Manage My Timesheet.

Procedure

| **Test Step #** | **Test Step Name** | **Instruction** | **Expected Result** | **Pass / Fail / Comment** |
| --- | --- | --- | --- | --- |
| 1 | Log on and open My Timesheet | Option 1: Log on to the SAP Fiori launchpad with the user for whom timesheet is to be recorded, then open Fiori App Manage My Timesheet.In case users can't record time for themselves, line manager and project manager can record timesheet on behalf.Option 2: Timesheet on behalf by Line manager.Log on to SAP Fiori Launchpad as a line manager and open Fiori App Team Utilization. Select the user for whom timesheet is to be recorded and press button Edit Timesheet.Option 3: Timesheet on behalf by project manager.Log on to SAP Fiori Launchpad as a project manager and open Fiori App Monitor Missing Time Notifications. Select the user for whom timesheet is to be recorded and press button Edit Timesheet. | The My Timesheet screen displays.Note Field extensibility is enabled. you may transfer additional customer field like JIRA ticket. Please refer to 1N9 for more details. | OKFiori App Team Utilization not found. |
| 2 | Select Date Range | By default, the timesheet shows the current week.If you want to record times in a different week, select the date range line on the top of the screen under My Timesheet. | A calendar entry dialog box displays allowing you to choose the week you wish to display.The button Calendar Settings allows you to set Show Work Week (if no, Saturday and Sunday are shown), Start Week From (e.g. Monday), and Time Format (12:30 or 12.5).There are also two items Minimum Time Slot and Intervals for Time Recording (in Minutes). If you are in Custom Settings (choose Custom Settings button), you can change Intervals for Time Recording (in Minutes) in Calendar Settings. If you are in Default Settings, you will use the values defined in SSCUI. |  |
| 3 | Explore your tasks |  | The tasks (labelled by combination of: Customer Name, work packages, Activity Type, work items) assigned to you are displayed in the right side of the screen under My Tasks with the description of the projects, work packages, Activity Type, and work items.They are automatically prefilled in the My Tasks list if the employee is staffed to a work package of commercial projects. The automatically created tasks cannot be deleted.On the top-right corner of each task, you would see the hours already recorded for that task.Task Type for non-project related activities are also shown. |  |
| 4 | Search your tasks (optional) | In the right side of the screen, insert a text in the search box just below My Tasks.The text search can be performed through three attributes: project title description, work package title description/work item title description, role description | The task(s) assigned to you are filtered according to the text inserted in the search box. |  |
| 5 | Select a task | In the right side of the screen, under My Tasks, the tasks assigned to you are shown.By default, the five most recently used tasks are shown. choose a task. | You have selected a task on which you can record times. The selected task is shown in a different color. |  |
| 6 | Record working time - Create new time entry | Enter the working times per days, hours and tasks <registered in hh:mm format>.Choose a task from the list of the available tasks. To enter the working times, click on the number of hours you want to record. A rectangular area just below the date range, shows all the days of the chosen week on the top horizontal axis, the working hours for each day on the left vertical axis, and the total hours recorded per day in the bottom horizontal axis. The left vertical axis is labelled with a number that helps you in understanding how many hours to record.The minimum time slot is by default 30 minutes, which means if you maintain an entry less than 30 minutes, system will initially provide a time block of 30 minutes. For entries less than 15 minutes, there is no task label or description in the time block. If there are multiple entries that are less than 15 minutes, they will be grouped together. By clicking the time block, you will get an entry list, each entry with a task label and description. You can choose an entry for editing.To create a new time entry, click on the cell corresponding to the day and the number of hours that you want to record. For example, if you want to record 5 hours, click on the cell just below the number 5 on the day on which you want to record the hours.Interval for Time Recording is by default 30 minute. You can change Interval for Time Recording (in Minutes) in Calendar Setting. For example, if the time interval is set to 5 minutes, when mouse across calendar, time will jump from e.g. 2:55 h to 3:00 h. | The new time entry is visualized on the day you have chosen as a rectangular box. The height of this box fits the number of hours you have inserted. The entry shows the task title descriptions and the number of hours recorded in hh:mm format. The system calculates total hours automatically per day and can be viewed on the bottom bar per day and on the bottom left corner as total per week. |  |
| 7 | Record working time – Create additional time entries | Repeat steps 5 and 6 for any additional time entry you want to record taking into account the already existing entries. For example, if 2 hours are already registered on a day, and you want to record 5 hours, click on the cell just below the number 7 on the day on which you want to record the hours. If you want to record additional time entries on a day on which you have already recorded, all the times allowed on the grid, just click on the top row and the grid will enlarge. | The new time entries are visualized on the days you have chosen as rectangular boxes. The height of each box fits the number of hours you have inserted. Each entry shows the task title descriptions and the number of hours recorded in hh:mm format. The left vertical axis shrinks up showing more hours if the total hours on a day exceeds the hours currently visualized. A vertical scroll bar appears on the right side of the screen, so that you can scroll up and down for a better visualization. If recording a time entry on a day the total would exceed 24 hours, the system prompts an error message and prevents you from recording that time entry. The system calculates total hours automatically per day and can be viewed on the bottom bar per day and on the bottom left corner as total per week. |  |
| 8 | Record working time – Modify existing entries | Choose an existing entry, and in the Details dialog box, adapt the Duration field by inserting the number of hours in hh:mm format.If you want to create an entry which is less than 30 minutes, say 4 minutes, you need to change Minimum Time Slot to less than 4 minutes by SSCUI. Then you can adapt the Duration to 4 minutes.Save your entry. | The time entry is adapted. The height of the time entry is adapted according to the new recorded hours. |  |
| 9 | Record working time – Delete existing entries | Choose the Delete button that is on the cross icon on the top-right corner of an entry. | The selected entry disappears. |  |
| 10 | Enter a description for an activity (optional) | To enter an optional description or note for an activity, just choose the entry, enter a description in the Note field and save. | A dialog box is displayed. The description of the activity is saved. |  |
| 11 | Record time | Save your entries. | The times are saved. The filter/display settings are also saved, and will display the next time this app is launched.There are a UI adaptation for lower right button Save and Submit which are controlled by SSCUI. You may refer to SSCUI documents on how to configure it:For details please refer to SAP Product Assistance: [https://help.sap.com/viewer/p/SAP_S4HANA_CLOUD](https://help.sap.com/viewer/p/SAP_S4HANA_CLOUD): Choose a specific language version of Product Assistance and navigate by: Configuration Apps → Configuration Apps for Professional Services.Under Configuration Apps for Professional Services - Data Entry Profiles for Timesheet. |  |

### Time Recording for Contingent Worker

#### Optional: Create Task through Manage My Timesheet

Prerequisites

The following business process must be run before this step:

- Create external service Purchase Orders in Service and Material Procurement - Project-Based Services (J13). The service performer is specified with this contingent worker. When creating PO for external service, please use the right Service Material item for example: T001 in order to record the timesheet.
- Maintain the Staffing work package in Customer Project Management (J11). This contingent worker is selected in the project staffing.

Procedure

| **Test Step #** | **Test Step Name** | **Instruction** | **Expected Result** | **Pass / Fail / Comment** |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori launchpad as a contingent worker (e.g. EXTSERVPERF1010 for DE Company). | The SAP Fiori launchpad displays. |  |
| 2 | Access the Fiori App | Open Manage My Timesheet. | My Timesheet displays. |  |
| 3 | Manage my task | At the right top, choose the  icon in the right side of My Tasks, then open the list item Manage My Tasks. | My task list displays. |  |
| 4 | Create a task | In the lower right-hand corner, choose the Create Task button. | The New Task window displays. |  |
| 5 | Enter field values | Choose the assigned work package.Choose the Purchase Order (the one created in J13 for the contingent worker).Go back to the My Timesheet screen.Note When creating a task, please don't choose Activity Type. | The work package is staffed with this contingent worker (log-in ID), and the staffing status is Confirmed.The external service purchase order is specified with this contingent worker as the service performer. |  |
| 6 | Save the Entry | The new task is saved. | If the new task is duplicated with task created by system, an error message will appear. |  |

#### Time Recording through Manage My Timesheet

Procedure

| **Test Step #** | **Test Step Name** | **Instruction** | **Expected Result** | **Pass / Fail / Comment** |
| --- | --- | --- | --- | --- |
| 1 | Log on and Open Manage My Timesheet | Option 1: Log on to the SAP Fiori launchpad as a contingent worker (e.g. EXTSERVPERF1010 for DE Company) and open Fiori App Manage My Timesheet.In case the contingent workers can't record time for themselves, line manager and project manager can record timesheet on-behalf.Option 2: Timesheet on-behalf by Line manager.Log on to SAP Fiori Launchpad as a line manager and open Fiori App Team Utilization Select the contingent worker for whom time is to be recorded and press button Edit Timesheet.Option 3: Timesheet on behalf by project manager.Log on to SAP Fiori Launchpad as a project manager and open Fiori App Missing Time Notification. Select the contingent worker for whom time is to be recorded and press button Edit Timesheet. | My Timesheet screen displays. | OKFiori App Team Utilization not found. |
| 2 | Select a Task | On the top-right corner of each task, you would see the hours already recorded for that task.Choose a task. | You have selected a task on which you can record time. The selected task is shown in a different color.The tasks assigned to a contingent worker are prefilled in the My Tasks list on the right side. The automatically created tasks cannot be deleted. Only the purchase orders with account assignment type Cost Center and Project will be shown in the task list. Only if a service performer is assigned during the purchase order creation, those tasks will be shown in the My Task list.In the right side of the screen under My Tasks, tasks are labelled with the description of the Projects, Work Packages, Customer, Activity Type, Purchase Order, Work Items.On the top-right corner of each task, you would see the hours already recorded for that task. |  |
| 3 | Record Working Time – Create New Time Entry | To create a new time entry, choose the cell corresponding to the day and the number of hours that you want to record. For example, if you want to record 5 hours, choose the cell just below the number 5 on the day on which you want to record the hours.Interval for Time Recording is by default 30 minutes.You can change Interval for Time Recording (in Minutes) in Calendar Settings, for example, if the time interval is set to 5 minutes, and you move your mouse across calendar, time will jump from e.g. 2:55 h to 3:00 h.The minimum time slot is pre-set as 30 minutes, which means if you maintain an entry less than 30 minutes, system will initially provide a time block of 30 minutes. |  |  |
| 4 | Record Working Time – Create Additional Time Entries | Repeat steps 6 and 7 for any additional time entry you want to record taking into account the already existing entries. For example, if 2 hours are already registered on a day, and you want to record 5 hours, choose on the cell just below the number 7 on the day on which you want to record the hours. | The new time entries are visualized on the days you have chosen as rectangular boxes. The height of each box fits the number of hours you have inserted. Each entry shows the task title descriptions and the number of hours recorded in hh:mm format. The left vertical axis shrinks up showing more hours if the total hours on a day exceeds the hours currently visualized. A vertical scroll bar appears on the right side of the screen, so that you can scroll up and down for a better visualization. If recording a time entry on a day the total would exceed 24 hours, the system prompts an error message and prevents you from recording that time entry. The system calculates total hours automatically per day and can be viewed on the bottom bar per day and on the bottom left corner as total per week. |  |
| 5 | Record working time – Modify existing entries | Choose an existing entry, and in the Details, adapt the Duration field by inserting the number of hours in hh:mm format. Save your entry. | The time entry is adapted. The height of the time entry is adapted according to the new recorded hours. |  |
| 6 | Record Working Time – Delete Existing Entries | Choose the Delete button that is on the cross icon on the top-right corner of an entry. | The selected entry disappears.Until approved Service Entry Sheet, delete approved time recording is possible. You need to:Purchaser uses app Manage Service Entry Sheet to Revoke Approval for approved service entry sheet and delete the service entry sheet item, then Send for Approval to Project Manager.Project Manager approves the SES via My Inbox app.Consultant deletes the entries in Manage My Timesheet app.Project Manager approves the time entry deletion in app Approve Timesheets. |  |
| 7 | Enter A Description for An Activity (optional) | To enter an optional description or note for an activity, just choose the entry, enter a description in the Note field and save. | A dialog box is displayed. The description of the activity is saved. |  |
| 8 | Record Time | Save your entries. | The times are saved. The filter/display settings are also saved, and display the next time this app is launched. |  |
| 9 | Submit for Approval | Choose the Submit button. | The time is ready for approval.After approval, the left side of the time-block turns to green. |  |

Note Skip the following Approval of Working Times step if the left side of the time-block turns green. This would mean that “approval from manager” is not activated in the SSCUI.

### Approval of Working Times

Context

The recorded time of the contingent worker in the previous steps need further approval from the project manager. The approved data is transferred to the target components for further processing through a background job. The roadmap contains the approval of working times by an appropriate responsible person.

You can configure your solution by SSCUI with Fiori app Manage Your Solution to Maintain Data Entry Profiles.

You can:

- Switch on or off the approval process. By default, approval is required for contingent workers.
- Select the accounting objects that is used by the customer for their processes like Cost Center, Activity Type, and Receiver Order.
- Enable Extensibility Mode to transfer additional customer field.
- Define the period for which you want to get the missing time entries (like 60 days or 120 days).

For details please refer to SAP Product Assistance: [https://help.sap.com/viewer/p/SAP_S4HANA_CLOUD](https://help.sap.com/viewer/p/SAP_S4HANA_CLOUD):

Choose a specific language version of Product Assistance and navigate by: Configuration Apps → Configuration Apps for Professional Services.

Under Configuration Apps for Professional Services - Data Entry Profiles for Timesheet.

Procedure

| **Test Step #** | **Test Step Name** | **Instruction** | **Expected Result** | **Pass / Fail / Comment** |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori launchpad as a Project Manager – Commercial. | The SAP Fiori launchpad displays. |  |
| 2 | Access the Fiori App | Option 1: Open Approve Timesheets.Option 2. Open My Inbox, in the left part of the screen, choose task Approval of Working Times, then choose button Open Task in the bottom right. | The Approve Timesheets screen displays. |  |
| 3 | Approve the Timesheet | At the left part of the screen, there’s the employee list.Select one and read the request at right part of the screen.Choose item(s) that need to be approved by clicking the checkbox, then press the Approve button in lower right part. | The selected timesheet is approved. |  |
| 4 | Reject the Timesheet | Choose the checkbox for items that need to be rejected, then press Reject button in lower right part.A dialogue box is shown for you to select a rejection reason and a Confirmation screen pops out for your confirmation.Note You can define own Rejection Reasons by SSCUI with app Manage Your Solution. For details please refer to SAP Product Assistance: [https://help.sap.com/viewer/p/SAP_S4HANA_CLOUD](https://help.sap.com/viewer/p/SAP_S4HANA_CLOUD): Choose a specific language version of Product Assistance and navigate by: Configuration Apps → Configuration Apps for Professional Services. Under Configuration Apps for Professional Services - Rejection Codes for Timesheet. | The selected timesheet is rejected. |  |

### Maintain Customer Project Billing Proposal

Context

In this step, the customer project billing proposals can be maintained.

Prerequisites

The following Business Processes must be run before this step:

- Time Recording - Project-Based Services (J12)
- Service and Material Procurement - Project-Based Services (J13)
- Consumable Purchasing (BNX) (Optional)

Procedure

| **Test Step #** | **Test Step Name** | **Instruction** | **Expected Result** | **Pass / Fail / Comment** |
| --- | --- | --- | --- | --- |
| 1 | Logon | Logon to the SAP Fiori launchpad as a Project Manager - Commercial Services. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Release Billing Proposals. | The system provides the customer project billing proposals filtered by due date (default filter). |  |
| 3 | Show details of Customer Project Billing Proposal | A list of Billing Proposals is displayed based on the default filter: Billing Dates = TodayTo display more information, choose the Project Name.Note Project ID, Project name, Customer, Billing Type and/or Billing Item can be used as filters. | The system displays a dialog box with the following information:Project NameCustomerDescriptionStart/End DateService OrganizationCost CentreSales StageChoose the Project Name in the dialog box to navigate to the Project Fact Sheet. |  |
| 4 | Postpone Customer Project Billing Proposal – optional | Choose one or more Customer Project Billing Proposals.Choose the Postpone button. | A dialog box is displayed. |  |
| 5 | Enter Data | Maintain the data and choose the OK button.New billing date: tomorrowReason: ex. Rework necessary | The postponed Billing Proposal is removed from the filtered list. |  |
| 6 | Preview Customer Project Billing Proposal | Choose one or more Customer Project Billing Proposals.Choose the Edit button. | The Billing Proposal details are displayed.Note If incompatible proposals are chosen, a dialog box displays an error message explaining that the selected billing proposals cannot be billed together. |  |
| 7 | Display Data | According to the different billing item usage (fixed price, time and expenses, periodic service, payment on an account, usage-based billing), different fields are displayed. The setting button can be used to personalize the layout of the screen. | For the fixed price, periodic service and payment on account billing items, the billing amount is the value of the sales order billing plan (see the section on Maintain Customer Project Billing).For the usage-based billing, the billing amount is the quantity posted in the Enter Activity Allocation app, multiplied for the sales price (see the section on Capture Service Unit).For the Time and Expense billing item, the Billing Amount is calculated based on the actual costs posted on the project. A list of service/expense items is displayed with costs coming from the following business processes: Time Recording - Project-Based Services (J12) and/or Service and Material Procurement - Project-Based Services (J13) and/or Consumable Purchasing (BNX).Note For the Time and Expense billing item, the non billable service will be indicated via a new column and the amount to be billed will be automatically written off for the same. This will not be changeable by the project manager |  |
| 8 | Postpone selected items – optional | For the Time and Expense billing types only:Choose one of the customer project billing proposals. Actual amount/quantity can be modified or postponed. Enter the amount to be written off/amount to be postponed or the quantity to be written off/quantity to be postponed to change the actual amount to be billed.These changes are not automatically saved. The Approximate Amount icon is shown near the Amount to be billed.Click on the Update button to save the changes. | The Billing Amount is changed.For the Time and Expense billing types or Usage-based billing types, if the billing proposal has not been totally released as some amount/quantity was postponed, the amount/quantity to be written off can be viewed via clicking the button View Written-off Items. |  |
| 9 | Defer after date | Choose one of the customer project billing proposals. You can use the Defer after Date button to postpone all the items after a specified service date. | Only the items before the specified service date are taken into account and billed to the customer. |  |

### Release Customer Project Billing Proposal

Context

In this step, the customer project billing proposal can be released. This leads to the creation of Debit Memo Request (DMR).

Procedure

| **Test Step #** | **Test Step Name** | **Instruction** | **Expected Result** | **Pass / Fail / Comment** |
| --- | --- | --- | --- | --- |
| 1 | Logon | Logon to the SAP Fiori launchpad as a Project Manager - Commercial Services. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Release Billing Proposals. | The system provides the customer project billing proposals filtered by due date (default filter). |  |
| 3 | Release Customer Project Billing Proposal | Select the relevant Customer Project Billing Proposal and choose the Edit button. You can click on the Billing Item to display the billing instructions.Note In addition, you can add a note. This note will be visible in the Customer Invoice printout.Check the values. Then choose the Release button. |  |  |
| 4 | Check the Debit Memo Request | When the dialog box appears, choose OK.Optionally, you can choose the Open Editor to maintain the billing request (debit memo request) (see the section Finalize and Release Billing Request in the test script for J11). | The Customer Project Billing Proposal is released.A billing request (debit memo request) is created.The business process Sales Order Processing - Project-Based Services (J14) is triggered. The billing process is started, and bills are created and sent to the customer.For more information, refer to the related test script. |  |
| 5 | Optional: Create the debit memo request in the blocked status | Select the relevant Customer Project Billing Proposal and choose the Edit button. You have the possibility to decide whether you want to create the Debit Memo Request with or without billing block. Choose Create as blocked to create the Debit Memo Request with a billing block, then use the Fiori App Release Billing Request to take out the billing block. | The Customer Project Billing Proposal is released. A billing request (debit memo request) is created in the blocked status. |  |

### Billing

In billing, we have 3 possibilities:

-
    1. Processing of the existing Debit Memo Requests (DMR), where the DMR created as a part of the previous steps is processed to create invoice
    2. Processing of Manual Credit Memo Requests, where the Internal Sales Representative creates a manual credit memo request (without reference to any preceding document)
    3. Processing of Manual Credit Memo Requests, where the Internal Sales Representative creates a manual credit memo request (without reference to any preceding document).

In this document, we will consider the processing of DMR, created as a part of the customer project management (J11).

For steps on processing of manual credit memo requests and/or debit memo request, please refer the test script for scope item J14 (Section 4.2.2 and 4.2.3 are relevant)

### Processing of Existing Debit Memo Requests

### Create Customer Invoices

Context

In this activity, the Billing Clerk creates invoices for services which have been executed. The invoice is printed and can be sent to the customer. A journal entry is created in finance which is then the basis for incoming payments which clear the open items in customer accounts.

Procedure

| **Test Step #** | **Test Step Name** | **Instruction** | **Expected Result** | **Pass / Fail / Comment** |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori launchpad using the role Billing Clerk. | The SAP Fiori launchpad is displayed. |  |
| 2 | Open App | Open Create Billing Documents. | The Billing Due List Items is displayed. |  |
| 3 | Define Billing Settings | Choose Billing Settings on the right bottom of the screen.There are four settings, turn these settings to ON.Set billing date and type before billing.Create separate billing document for each item of billing due list.Automatically post billing documents.Display billing document after creation. |  |  |
| 4 | Search for Billing Due Items | In the search condition, use criteria if necessary. | Sales document(s) will display in the result. |  |
| Note Before doing the next step, the customer billing proposal must be maintained and the billing request must be released. This is part of the Customer Project Management - Project-Based Services (J11) scope item. After you released the billing proposal from scope item J11, you can also test the convergent billing scenario in scope item 1MC (4.1 Create a Billing Document with External Data and 4.2 Creating a Billing Document Combining External Billing Data and Data from Professional Services). |  |  |  |  |
| 5 | Create Customer Invoice | Select the document and choose Create. | The Create Billing Documents screen is displayed. |  |
| 6 | Enter Billing Details | Choose billing type Invoice (CI01) and maintain Billing Date, for example current date, then press button OK. | The draft billing document with ID Sxxxxxxxx will be displayed. |  |
| 7 | Save Billing Document | In the Billing Document screen, choose the Save button.The draft version billing document with ID Sxxxxxxxx turns into a saved billing document with ID xxxxxxxx, make a note of the billing document number: __________. | The system generates an invoice for billing. |  |

### Creation of Supplier invoice at headquarter

Context

The creation of billing document at subsidiary should lead to the automatic generation of the supplier invoice at the Headquarters.

Procedure

Follow the set-up document for scope item 2EL and the integration flow mentioned in the API hub. More details mentioned in the section “Integration Requirements by using EDI/IDOC”

### Manage Customer Invoices (Optional)

Context

In this activity, the Billing Clerk lists the customer invoices which have been created. From this list, invoices can be canceled or posted to accounting. Depending on system configuration, billing documents are automatically transferred to accounting or they are blocked for automatic posting and will be manually released to accounting.

Procedure

| **Test Step #** | **Test Step Name** | **Instruction** | **Expected Result** | **Pass / Fail / Comment** |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori launchpad using the role Billing Clerk. | The SAP Fiori launchpad displays. |  |
| 2 | Open App | Open Manage Billing Documents. |  |  |
| 3 | Select Document | Make the following entries:Billing Document: <Previously created billing document> | The relevant invoice document is selected. |  |
| 4 | Display Invoice Details | Select the row of your billing document and choose the Display button. | Invoice document details are displayed. |  |
| 5 | Preview Output | Choose the Preview button. | A PDF document of the invoice printout is displayed. |  |
| 6 |  | Go back to the Billing Document screen. |  |  |
| 7 | Post Invoice (Optional) | Depending on system configuration, billing documents are automatically transferred to accounting or they are blocked for automatic posting and will be manually released to accounting. In case the billing document has not yet been posted to accounting, choose the Post Billing Document button to create journal entry. | The invoice is transferred to Accounting. The system displaysBilling documents postedmessage. |  |

##### You can also create a credit memo with reference to invoice generated above. Refer the test script for J14 (Section 4.2.1.3 “Create Credit Memo with Reference to Invoice (Optional)”)

### Review Customer Project

Context

In this step, the customer project KPIs are analyzed. As a project manager, you can see the Percentage of Completion and set the project status based on the Overall Status, Budget, Staffing and Execution.

Procedure

| **Test Step #** | **Test Step Name** | **Instruction** | **Expected Result** | **Pass / Fail / Comment** |
| --- | --- | --- | --- | --- |
| 1 | Logon | Logon to the SAP Fiori launchpad as a Project Manager - Commercial Services. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Review Customer Projects. | The system provides the list of customer projects. Only projects with status In Execution are displayed. |  |
| 3 | Check Customer Projects | On the Customer Projects list, check the relevant information for your project. | You can analyse the current situation of the customer projects.You can select a specific project to start to monitor it in detail. |  |
| 4 | Choose a Customer Project and view Monitoring Details | Check the Forecast Month for your project. If necessary, use the Set Forecast Month button to set the review period to the current month, then select the > button to start monitoring this project.On the Review Customer Projects screen, the core KPIs for project monitoring are available for detailed analysis.The analysis per work package is available; the remaining effort for Work Item and Resource and/or the remaining costs for Expense types can be updated.When saving, the PoC is recalculated.Once the review is completed, set the Forecast Status to Completed and Save. | The core KPIs for project monitoring are displayed. |  |
| 5 | Maintain Project Status for the Customer Project | On the Review Customer Project screen, select the Project Status folder.To maintain the status, choose the + button, enter the status and save.Enter today's status for the following KPIs: Overall Status, Budget, Staffing, Execution. | The status is maintained. |  |
| 6 | Compare Versions | On the Review Customer Project screen select the Version Folder . | The comparison between the Actual version and the Baseline version is available. |  |

### Headquarter visibility of the project status

Context

The headquarter can view the current state of the customer project at subsidiary’s SAP Cloud ERP system

Procedure

Using the API listed at the start of this document (“SC_EXTERNAL_SERVICES_SRV - Read Commercial Project Details” in API Hub), you can create custom application on SAP Cloud Platform. The project specific data is read from SAP Cloud ERP and consumed in SCP for the benefit of On-Premise users.

### Headquarter visibility of the Credit Memos and Debit Memo Requests (created at the subsidiary)

Context

Headquarter should have the visibility to the debit memo requests and credit memo requests created by the subsidiary, before the final billing is done. This removes the possibility of re-work and lets the subsidiary and headquarter to be on the same page.

Procedure

Using the APIs API_CREDIT_MEMO_REQUEST_SRV and API_DEBIT_MEMO_REQUEST_SRV, customer can build application on SAP Cloud Platform. The application will consume the data from these APIs and provide the visibility on the credit and debit memo requests to the headquarter.

### Set Project Status (Completed)

Context

In this step, the status of the customer project is set to Completed.

Procedure

| **Test Step #** | **Test Step Name** | **Instruction** | **Expected Result** | **Pass / Fail / Comment** |
| --- | --- | --- | --- | --- |
| 1 | Log on | Logon to the SAP Fiori launchpad as a Project Manager - Commercial Services. | The SAP Fiori launchpad displays. | OK |
| 2 | Access the SAP Fiori App | Choose Plan Customer Projects. | The Customer Project screen is displayed.Projects assigned to the Customer Project Manager are displayed. | OK |
| 3 | View Projects Header Data and Choose a Customer Project to Edit | Choose project XXXX ( Created in the start of the script) | Project XXXX is displayed. | OK |
| 4 | Edit Project | Choose the Edit button to edit project information. | You can now make changes to the project. | OK |
| 5 | Change the Project Status | Make the following entry and choose Save.Stage: Completed | This stage indicates that work has been completed and delivered, but financial settlements (customer/supplier invoices) are still pending. | OK |

### Close Customer Projects

Context

In this step, the customer project is closed.

The following Business Processes must run before this step:

- Event-Based Revenue Recognition - Project-Based Services (1IL)
- Profitability and Cost Analysis (J55)

Procedure

| **Test Step #** | **Test Step Name** | **Instruction** | **Expected Result** | **Pass / Fail / Comment** |
| --- | --- | --- | --- | --- |
| 1 | Logon | Logon to the SAP Fiori launchpad as a Project Manager - Commercial Services. | The SAP Fiori launchpad displays. | OK |
| 2 | Access the SAP Fiori App | Open Plan Customer Projects. | The Customer Project screen is displayed.Projects assigned to the Customer Project Manager are displayed. | OK |
| 3 | View Projects Header Data and Choose a Customer Project to Edit | Choose project XXXX(Created in the beginning of the test script). | Project XXXX is displayed. | OK |
| 4 | Edit Project | Choose the Edit button to edit project information. | You can now make changes to the project. | OK |
| 5 | Change the Project Status | Make the following entry and choose Save.Stage: Closed | When a project is closed, financial postings are no longer possible. | OK |

You can also reset the status of the project to “Completed” and do necessary changes (like customer billing etc.)

## Suspected conflicts

> [!warning] Conflict
> Flagged while digesting this document, not verified: Cover says June 2026 / 2608 but copyright is 2020 and last revision 10.05.2020, so content may be stale

> [!warning] Conflict
> Flagged while digesting this document, not verified: Test script contains leftover tester comments (e.g. 'Could not find APP Manage Credit Memo Request Workflow', 'Fiori App Team Utilization not found', 'No specific user ID?') suggesting some apps/steps may not be available

> [!warning] Conflict
> Flagged while digesting this document, not verified: Billing section lists three possibilities but items 2 and 3 are identical text

> [!warning] Conflict
> Flagged while digesting this document, not verified: Cross-references to chapters 7.3.5/7.3.6 and 2.4.2 do not match this document's numbering

## Connections
- part-of :: [[_cluster]]
- related-to :: [[16-two-tier-erp-and-central-finance/two-tier-scenario-managing-intercompany-professional-services-projects]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/General/Two-Tier_ERP_Assets_User_Guides/Two-Tier_ERP_Assets_User_Guides/Procurement/S4CLD2608_2T_Proj_ServiceProcurement.docx` — full document · extracted with `mammoth` · 94,115 chars in the whole document
