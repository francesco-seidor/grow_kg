---
id: 01-solution-foundation-and-platform/test-script-exception-based-core-hr-with-sap-successfactors-employee-c
title: "Test Script: Exception-Based Core HR with SAP SuccessFactors Employee Central (JB1_AE) (JB1_S4CLD2608_BPD_EN_AE)"
description: "S/4HANA Cloud 2608 test script for JB1 (UAE): replicating banks, company codes, cost centers, workers and photos with SuccessFactors Employee Central."
cluster: 01-solution-foundation-and-platform
tags: [kb/solution-foundation-and-platform, topic/successfactors-employee-central-and-user-provisioning, topic/payroll-posting-integration]
aliases: [JB1_S4CLD2608_BPD_EN_AE]
keywords: [SuccessFactors Employee Central Integration and User…, employee central integration, test scripts, bank data replication, company code replication, cost center replication, employee data replication, contingent workers, replication monitoring, address information]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/JB1_S4CLD2608_BPD_EN_AE.docx]
confidence: low
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-1311
topic: 01-solution-foundation-and-platform/successfactors-employee-central-and-user-provisioning
language: EN
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Test Script: Exception-Based Core HR with SAP SuccessFactors Employee Central (JB1_AE) (JB1_S4CLD2608_BPD_EN_AE)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/JB1_S4CLD2608_BPD_EN_AE.docx`, extracted with `mammoth`. Grouped under **SuccessFactors Employee Central Integration and User Provisioning** in Solution Foundation and Platform. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

| <!-- image omitted: unnamed --> | Test ScriptSAP S/4HANA Cloud Public Edition - 19-06-26 |
| --- | --- |
|  | Exception-Based Core HR with SAP SuccessFactors Employee Central (JB1_AE) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Table of Contents

[1 Purpose 3](#_Toc232863908)

[2 Prerequisites 4](#_Toc232863909)

[2.1 Additional Manual Configuration 4](#_Toc232863910)

[2.2 System Access 4](#_Toc232863911)

[2.3 Roles 4](#_Toc232863912)

[2.4 Master Data, Organizational Data, and Other Data 6](#_Toc232863913)

[2.5 Business Conditions 7](#_Toc232863914)

[3 Overview Table 8](#_Toc232863915)

[4 Test Procedures 10](#_Toc232863916)

[4.1 Bank Data Replication 10](#_Toc232863917)

[4.1.1 View Bank Data 10](#_Toc232863918)

[4.2 Company Code Replication 11](#_Toc232863919)

[4.2.1 Check Company Code 11](#_Toc232863920)

[4.2.2 View Legal Entity Data 12](#_Toc232863921)

[4.3 Cost Center Replication 14](#_Toc232863922)

[4.3.1 Maintain Cost Center 14](#_Toc232863923)

[4.3.2 View Cost Center Data 16](#_Toc232863924)

[4.4 Employee Workforce Data Replication 18](#_Toc232863925)

[4.4.1 Hire New Employee 19](#_Toc232863926)

[4.4.1.1 Monitor Employee Data Replication 23](#_Toc232863927)

[4.4.1.2 View Employee Basic Data 24](#_Toc232863928)

[4.4.2 Hire New Contingent Worker 26](#_Toc232863929)

[4.4.2.1 Monitor Contingent Worker Data Replication 31](#_Toc232863930)

[4.4.2.2 View Contingent Worker Data 32](#_Toc232863931)

[4.4.3 Maintain Additional Information (Optional) 34](#_Toc232863932)

[4.4.3.1 Maintain Address Information 35](#_Toc232863933)

[4.4.3.2 View Address Information 37](#_Toc232863934)

[4.4.3.3 Maintain Payment Information 38](#_Toc232863935)

[4.4.3.4 View Payment Information 40](#_Toc232863936)

[4.4.3.5 Maintain Service Cost Level 41](#_Toc232863937)

[4.4.4 Employee Photo Replication 43](#_Toc232863938)

[4.4.4.1 Maintain Employee Photo 43](#_Toc232863939)

[4.4.4.2 View Employee Photo 45](#_Toc232863940)

[5 Appendix 47](#_Toc232863941)

[5.1 Process Integration 47](#_Toc232863942)

[5.1.1 Succeeding Processes 47](#_Toc232863943)

## Purpose

Overview

The integration between SAP S/4HANA Cloud Public Edition and SAP SuccessFactors Employee Central enables the transfer of worker data for both internal employees and contingent workers. This includes basic data, such as worker name, ID, and job information, as well as contact details, such as private address, email, and telephone information. This scope item also covers the replication of key financial objects such as cost centers from SAP S/4HANA Cloud Public Edition to SAP SuccessFactors Employee Central.

|  |
| --- |
| Note The standard method to integrate SAP S/4HANA Cloud Public Edition and SAP SuccessFactors Employee Central is through SAP Master Data Integration. For more information, see the SAP Help Portal for SAP S/4HANA Cloud Public Edition under [Master Data Replication Using SAP Master Data Integration](https://help.sap.com/docs/SAP_S4HANA_CLOUD/0f69f8fb28ac4bf48d2b57b9637e81fa/34ee350171bf41bb8d015f8061a5a918.html). Activation of this scope item is recommended only when the standard integration option isn't available for your country or for specific use cases. |

This document provides a detailed procedure for testing this scope item after solution activation, reflecting the predefined scope of the solution. Each process step, report, or item is covered in its own section, providing the system interactions (test steps) in a table view. Steps that are not in scope of the process but are needed for testing are marked accordingly. Project-specific steps must be added.

|  |
| --- |
| Note Values in this test script (decimal notation, date formats, and so on) are presented in U.S. standard notation. If your test system is set up to use a different notation, enter values as appropriate. |

## Prerequisites

This section summarizes all the prerequisites for conducting the test in terms of systems, users, master data, organizational data, other test data and business conditions.

### Additional Manual Configuration

Before you can test this scope item, you must have completed the additional configuration steps that are described in the Set-Up Instructions for this scope item. These configuration steps are specific for your implementation and include mandatory settings that are not delivered by SAP and must be created by you. For more information, follow the link to the document:

[Link to Set-Up Instructions](https://help.sap.com/docs/SAP_S4HANA_BEST_PRACTICES/371f9bb55ec2e74d5e64d8dfab6101b2)

### System Access

The test takes place in the following systems:

| System | Details |
| --- | --- |
| SAP SuccessFactors Employee Central | Accessible via SAP SuccessFactors Employee Central web-based portal. Your system administrator provides you with the URL to access the various apps assigned to your role. |
| SAP S/4HANA Cloud Public Edition | Accessible via SAP Fiori launchpad. Your system administrator provides you with the URL to access the various apps assigned to your role. |

### Roles

Create business roles using the following business role templates delivered by SAP and assign them to your individual test users.

Alternatively, if available, you can use the following spaces delivered by SAP. You create a space with pages containing predefined essential apps and assign it to the business role. You then assign this business role to your individual users.

For more information, refer to How to Create a Business Role from a Template in the [product assistance](https://help.sap.com/docs/SAP_S4HANA_CLOUD/53e36b5493804bcdb3f6f14de8b487dd/ec310a8b669a45ca898dc4dd91d97de2.html) for SAP S/4HANA Cloud Public Edition.

| Name (Role Template) | ID (Role Template) | Name (Launchpad Space) | ID (Launchpad Space) | Log On |
| --- | --- | --- | --- | --- |
| Configuration Expert - Business Process Configuration | SAP_BR_BPC_EXPERT | Business Process Configuration / Business Process Configuration - Finance / Business Process Configuration - Procurement / Manage your Solution / Business Process Configuration - Workflow / Business Configuration - Feature Management / Business Process Configuration - Extensibility Explorer / Business Configuration - Transportation | SAP_BR_BPC_EXPERT / SAP_FIN_SPT_BPC_EXPERT_PC / SAP_MM_SPT_BIZ_PROC_CONFIGN_PC / SAP_CA_SPT_IC_LND_BASE_PC / SAP_CA_SPT_BPC_WORKFLOW_PC / SAP_CA_SPT_BPC_FM_PC / SAP_EI_SPT_BPC_EXT_PC / SAP_TM_SPT_TRANSPCFG_PC |  |
| Cost Accountant - Overhead | SAP_BR_OVERHEAD_ACCOUNTANT | Overhead Accounting | SAP_BR_OVERHEAD_ACCOUNTANT |  |
| Cash Management Specialist | SAP_BR_CASH_SPECIALIST | Cash Management | SAP_BR_CASH_SPECIALIST |  |
| Master Data Specialist - Business Partner Data | SAP_BR_BUPA_MASTER_SPECIALIST | Master Data - Business Partners / Business Partner Governance / Business Partner Governance / Business Partner Governance | SAP_BR_BUPA_MASTER_SPECIALIST / SAP_CA_SPT_MDG_BP_GOV_PC / SAP_CMD_SPT_BP_GOV_PC / SAP_CA_SPT_MDG_BP_WFUSR_PC |  |
| Administrator - Data Replication | SAP_BR_ADMINISTRATOR_DATA_REPL |  |  |  |
| Administrator - HR Info | SAP_BR_ADMINISTRATOR_HRINFO | Administration - HR Info | SAP_BR_ADMINISTRATOR_HRINFO |  |
| Administrator | SAP_BR_ADMINISTRATOR | Administration / Administration - Workforce Master Data / Administration - License Compliance / Administration - Data Management / Administration - Output Control | SAP_BR_ADMINISTRATOR / SAP_BUM_SPT_ADMINISTRATION_PC / SAP_EI_SPT_ADM_LC_PC / SAP_CA_SPT_TDR_PC / SAP_OC_SPT_ADMINISTRATION_PC |  |
| Employee | SAP_BR_EMPLOYEE | Self Services / Self Services / Employee Overview Space | SAP_BR_EMPLOYEE / SAP_CA_SPT_EMPLOYEE_CROSS_PC / SAP_EAM_SPT_EMPLOYEE_PC | Test user: <Person Id from EC>; Password: <password>Note Log on as ADMINISTRATOR / <password> and add the employee role to the user, as shortly sketched below:Go to the Maintain Business Users appSearch for user name <Person Id from EC>. In the result list, flag the checkbox in the row containing this user name. Select Edit in the lower part of the screen.On the Business Users screen, select Add Business Roles in the lower part of the screen. The Add Business Roles dialog box opens. Search for the business role ID SAP_BR_EMPLOYEE. In the result list, flag the checkbox next to this role and choose OK, then select Save. |

Employee Central System

| Business User | Name | Log On |
| --- | --- | --- |
| HR Manager | As defined under role-based permissions in SAP SuccessFactors Employee Central; for testing purpose, use the superuser role. | Test user: <superuser>, Password: <password> |

### Master Data, Organizational Data, and Other Data

The organizational structure and master data of your company have been created in your system during activation. The organizational structure reflects the structure of your company. The master data represents materials, customers, and suppliers, for example, depending on the operational focus of your company.

|  |
| --- |
| Caution Update Behavior of Predelivered Demo DataIn non-productive environments (such as starter systems, sandbox systems, or partner demo systems), SAP initially deploys demo data for your selected scope. You can use this data to test and evaluate business processes.In a customer system, you can receive new or updated demo data after initial activation with further scope enhancements, provided the existing demo data wasn't changed in an incompatible way. If activation errors occur due to incompatible changes in demo data, you're responsible for resolving them. If you don't resolve the errors within a specific time frame, SAP reserves the right to deactivate demo data in your systems. In this case, you can continue by creating your own demo data. Alternatively, you can request that your systems be reprovisioned if you want to work with predelivered demo data again.In partner systems, you can use the demo data deployed with the initial activation. No additional demo data will be deployed in the system with scope enhancements. You can only create additional demo data manually. |

Use your own master data or the following sample data to go through the test procedure.

| Master Data | Value | Details | Comments |
| --- | --- | --- | --- |
| SAP S/4HANA: Company Code | 3310 | Company code AE | SAP SuccessFactors Employee Central: value is mapped to legal entity ID. |

### Business Conditions

Before you can test this scope item, the following business conditions must be met.

|  |  |
| --- | --- |
|  | Business Condition |
| 1 | Company codes have been defined in the SAP S/4HANA Cloud Public Edition system and replicated to SAP SuccessFactors Employee Central. That means that the four-character ID value of a legal entity in SAP SuccessFactors Employee Central and the corresponding company code must be equal. If you want to replicate a cost center to Employee Central, a legal entity for the corresponding company code must already exist in SAP SuccessFactors Employee Central. Likewise, to replicate an employee to SAP S/4HANA Cloud Public Edition, a company code for the corresponding legal entity must exist in SAP S/4HANA Cloud Public Edition. |
| 2 | Cost centers have been defined in the SAP S/4HANA Cloud Public Edition system and replicated to SAP SuccessFactors Employee Central. |
| 3 | Bank master data have been defined in the SAP S/4HANA Cloud Public Edition system and replicated to SAP SuccessFactors Employee Central. |
| 4 | Legal entities, cost centers, and bank data must be replicated from SAP S/4HANA Cloud Public Edition to SAP SuccessFactors Employee Central before hiring an employee. |
| 5 | Employee master data must be replicated to SAP S/4HANA Cloud Public Edition, so that employee time data replication works. |

## Overview Table

The scope item Exception-Based Core HR with SAP SuccessFactors Employee Central (JB1) consists of several process steps provided in the table below.

Bank Data Replication

| Process Step | Business Role | Transaction/App | Expected Results |
| --- | --- | --- | --- |
| [View Bank Data](#unique_9) [page ] 10 | HR Manager | SAP SuccessFactors Employee Central | The data of the new bank is displayed. |

Legal Entity Replication

| Process Step | Business Role | Transaction/App | Expected Results |
| --- | --- | --- | --- |
| [Check Company Code](#unique_10) [page ] 11 | Configuration Expert - Business Process Configuration | SAP Fiori launchpad | You've created a company code. |
| [View Legal Entity Data](#unique_11) [page ] 12 | HR Manager | SAP SuccessFactors Employee Central | The data of the new legal entity is displayed. |

Cost Center Replication

| Process Step | Business Role | Transaction/App | Expected Results |
| --- | --- | --- | --- |
| [Maintain Cost Center](#unique_12) [page ] 14 | Cost Accountant - Overhead | SAP Fiori launchpad | You've created a cost center or you've updated an existing one. |
| [View Cost Center Data](#unique_13) [page ] 16 | HR Manager | SAP SuccessFactors Employee Central | The data of the new cost center and the updated cost centers is displayed. |

Employee Data Replication

| Process Step | Business Role | Transaction/App | Expected Results |
| --- | --- | --- | --- |
| [Hire New Employee](#unique_14) [page ] 19 | HR Manager | Company Instance URL | A new employee has been added and has the status Active as of the hiring date. |
| [Monitor Employee Data Replication](#unique_15) [page ] 23 | HR Manager | Company Instance URL | The HR Manager has verified successful replication and possibly identified failed replication requests. Their correction leads to a delta replication of the changes to SAP S/4HANA Cloud Public Edition. |
| [View Employee Basic Data](#unique_16) [page ] 24 | Administrator - HR Info | SAP Fiori launchpad | The basic data of the employee has been viewed after initial replication. |

Contingent Worker Data Replication

| Process Step | Business Role | Transaction/App | Expected Results |
| --- | --- | --- | --- |
| [Hire New Contingent Worker](#unique_17) [page ] 26 | HR Manager | Company Instance URL | The data for a newly hired contingent worker has been entered into the system and the status is Active as of the hiring date. |
| [Monitor Contingent Worker Data Replication](#unique_18) [page ] 31 | HR Manager | Company Instance URL | Possibly existing unsuccessfully processed replication requests have been identified. After the errors have been corrected, a new delta replication of the changes in the contingent worker data is triggered. |
| [View Contingent Worker Data](#unique_19) [page ] 32 | Administrator - HR Info | SAP Fiori launchpad | The data of the contingent worker has been viewed. |

Additional Information

| Process Step | Business Role | Transaction/App | Expected Results |
| --- | --- | --- | --- |
| [Maintain Address Information](#unique_20) [page ] 35 | HR Manager | Company Instance URL | The home address of an employee has been maintained. |
| [View Address Information](#unique_21) [page ] 37 | Master Data Specialist - Business Partner Data | SAP Fiori launchpad | The updated home address of the employee has been viewed. |
| [Maintain Payment Information](#unique_22) [page ] 38 | HR Manager | Company Instance URL | An employee's payment information has been maintained. |
| [View Payment Information](#unique_23) [page ] 40 | Administrator - HR InfoMaster Data Specialist - Business Partner Data | SAP Fiori launchpad | The payment information of the employee has been viewed after initial replication. |

## Test Procedures

This section describes the test procedures for each process step that belongs to this scope item.

### Bank Data Replication

When you create a bank in SAP S/4HANA Cloud Public Edition, it is replicated automatically to SAP SuccessFactors Employee Central. This section describes how to check a newly created bank in SAP SuccessFactors Employee Central for correctness.

#### View Bank Data

Purpose

The Administrator checks if the bank has been created correctly in SAP SuccessFactors Employee Central. Only initial replication of bank master data is supported. There are editable fields on SAP S/4HANA Cloud Public Edition for which this replication scenario would replicate value changes to banks in SAP SuccessFactors Employee Central.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to SAP SuccessFactors Employee Central as an HR Manager. |  |  |
| 2 | Go to Administration Center | From the Home dropdown in the upper left corner, choose Admin Center. |  |  |
| 3 | Go to Manage Data | On the Admin Center screen, go in the Company Processes & Cycles portlet to Employee Files and choose Manage Data. |  |  |
| 4 | Search New Bank | On the Manage Data screen, in the Search field, select Bank from the dropdown list. In the blank field next to the search field, search and select the new bank you've created in SAP S/4HANA Cloud Public Edition and which has been replicated to SAP SuccessFactors Employee Central. | The result is displayed beneath the Search portlet. |  |
| 5 | Check New Bank Data | Check if the new bank has been replicated correctly from SAP S/4HANA Cloud Public Edition. For details on the field mapping between SAP S/4HANA Cloud Public Edition and Employee Central, refer to the table below. |  |  |

|  |
| --- |
| Note The replication scenario fills only five fields of the SAP SuccessFactors Employee Central bank object, as listed in the mapping table below. All other fields in the SAP SuccessFactors Employee Central bank object can be maintained manually in SAP SuccessFactors Employee Central without being overwritten or impacted in any way by the replication scenario. |

|  |
| --- |
| Note Once all banks have been replicated successfully to the SAP SuccessFactors Employee Central system, you can validate the replicated bank data to make sure it is synchronized between SAP SuccessFactors Employee Central and SAP S/4HANA Cloud Public Edition. For this, check the list of banks in SAP SuccessFactors Employee Central and compare it with the list of banks in SAP S/4HANA Cloud Public Edition. |

The replicated bank object fields map to the SAP S/4HANA Cloud Public Edition bank API fields as follows:

| Fields in SAP S/4HANA Cloud Public Edition API | Fields in SAP SuccessFactors Employee Central | Description/Comment |
| --- | --- | --- |
| BankCountry | bankCountry | BANKS |
| BankName | bankName |  |
| BankInteralID | routingNumber | SuccessFactors Employee Central validations shall be switched off. |
| NA | effectiveStatus | There is no source value. The replication writes the hard-coded target value A. |
| NA | externalCode | Combination of BANKS and BANKL (routing number is not mandatory for replication). |

### Company Code Replication

In the following sections, the procedures for executing the company code replication from SAP S/4HANA Cloud Public Edition to SAP SuccessFactors Employee Central are described. The high-level process is as follows: a company code is created in SAP S/4HANA Cloud Public Edition. The new company code is then replicated automatically to SAP SuccessFactors Employee Central, where the corresponding legal entity is created and can be checked for correctness.

#### Check Company Code

Purpose

The Configuration Expert - Business Process Configuration checks one or several company codes. The company code(s) are transferred to SAP SuccessFactors Employee Central.

|  |
| --- |
| Note The replication of a company code fails if a legal entity for the same company code has been created manually in SAP SuccessFactors Employee Central with a different start date than 01/01/1900. |

Procedure

Depending on your configuration environment for SAP S/4HANA Cloud Public Edition, choose one of the following options:

Configure Your Solution

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. | The page containing the SAP Fiori apps associated with your role is displayed. |  |
| 2 | Access SAP Fiori App | Open the Manage Your Solution (F1241) app. Check that you have selected the local version for which you want to create a company code. Then, open the Configure Your Solution app. |  |  |
| 3 | Access Configuration Item | In the Configure Your Solution app, under application area Organization and subapplication area Organization, open the Organization configuration item. | The Configuration Steps for setting up an organizational structure are displayed. |  |
| 4 | Access Configuration Step | Open Configuration Step Organizational Structure with SSCUI ID 100066. |  |  |
| 5 | Add a Company Code | On the left-hand side pane, navigate to Country. Check the already configured company codes. This is the source for the data replication. New company codes can get configured here - please consult the SAP Help documentation for further details (it is expected that the company codes are already configured properly to be used in this integration.) | Company codes that are the basis for the data replication are displayed. |  |

SAP Central Business Configuration:

For the required steps with SAP Central Business Configuration, refer to [Setting Up Organizational Structure](https://help.sap.com/docs/CENTRAL_BUSINESS_CONFIGURATION/55c9333eed324cd284f6c4e5dab8462f/16d75cc2236c4c918ecce3196544acc3.html).

#### View Legal Entity Data

Purpose

The Administrator checks if the legal entities have been created correctly in SAP SuccessFactors Employee Central. Only initial replication of company code master data is supported. There are no editable fields in SAP S/4HANA Cloud Public Edition for which this replication scenario would replicate value changes to legal entities in SAP SuccessFactors Employee Central.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to SAP SuccessFactors Employee Central as an HR Manager. |  |  |
| 2 | Go to Administration Center | From the Home dropdown in the upper left corner, choose Admin Center. |  |  |
| 3 | Go to Manage Data | On the Admin Center screen, go in the Company Processes & Cycles portlet to Employee Files and choose Manage Data. |  |  |
| 4 | Search New Legal Entity | On the Manage Data screen, in the Search field, select Legal Entity from the dropdown list. In the blank field next to the search field, search and select the new legal entity you have created in SAP S/4HANA Cloud Public Edition and just replicated to SAP SuccessFactors Employee Central. | The result is displayed beneath the Search portlet. |  |
| 5 | Check New Legal Entity Data | Check if the new legal entity has been replicated correctly from SAP S/4HANA Cloud Public Edition. For details on the field mapping between SAP S/4HANA Cloud Public Edition and SAP SuccessFactors Employee Central, refer to the table below. |  |  |

|  |
| --- |
| Note The replication scenario fills only five fields in the Employee Central legal entity object, as listed in the mapping table below. All other fields in the SAP SuccessFactors Employee Central legal entity object can be maintained manually in SAP SuccessFactors Employee Central without being overwritten or impacted in any way by the replication scenario. |

Once all company codes have been replicated successfully to the SAP SuccessFactors Employee Central system, you can validate the replicated company code data to make sure it is synchronized between SAP SuccessFactors Employee Central and SAP S/4HANA Cloud Public Edition. For this, check the list of legal entities in SAP SuccessFactors Employee Central and compare it with the list of company codes in SAP S/4HANA Cloud Public Edition.

The replicated legal entity object fields maps to the SAP S/4HANA Cloud Public Edition company code API fields as follows:

| Fields in SAP S/4HANA Cloud Public Edition API | Fields in SAP SuccessFactors Employee Central | Description/Comment |
| --- | --- | --- |
| NA | startDate | There is no source value. The replication defaults this date to 01/01/1900. It is a business key field. |
| CompanyCode | Legal Entity ID | It is a business key field. |
| CompanyCodeName | Legal Entity Name | This field is not translatable in SAP S/4HANA Cloud Public Edition. |
| NA | Status | There is no source value. The replication writes the hard coded target value A. |
| Country | Country |  |

### Cost Center Replication

In the following section, the procedures for executing the cost center data replication from SAP S/4HANA Cloud Public Edition to SAP SuccessFactors Employee Central are described. The high-level process is as follows: once the initial replication is completed, you can change the existing cost center data in SAP S/4HANA Cloud Public Edition. The changes are then replicated automatically to SAP SuccessFactors Employee Central, where they can be checked for correctness.

|  |
| --- |
| Note Whenever there are multiple SAP S/4HANA Cloud Public Edition systems, you need to make sure that the cost center IDs delivered to Employee Central are unique across your system landscape. |

#### Maintain Cost Center

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The Cost Accountant - Overhead maintains one or several cost centers by performing one of the following activities:

- creating a new cost center in an already replicated cost center hierarchy
- updating an already replicated cost center, including name and description in different languages.

|  |
| --- |
| Note In both cases, a delta replication is triggered. The newly created cost center within the hierarchy or the updates of an existing cost center are transferred to SAP SuccessFactors Employee Central. |

Procedure

|  |
| --- |
| Note In this procedure, the assumption is that the new and the changed cost centers belong to the same controlling area. |

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Cost Accountant - Overhead. | The page containing the SAP Fiori apps associated with your role is displayed. |  |
| 2 | Access SAP Fiori App | Choose the Manage Cost Centers - Old Version (F1443A) tile. |  |  |
| 3 | Create New Cost Center | Choose Create located in the upper right corner of the screen. | A new screen, New Cost Center, opens in addition to the cost center search screen. |  |
| 4 | Enter Basic Information of New Cost Center | In the New Cost Center section of the screen, make the following entries:Cost Center: <cost center ID>.Valid From: <validity start date>.Valid To: defaults to system high date; adapt if appropriate, else leave as is.Name: Enter a cost center name.Description: Enter a cost center description.Person Responsible: Enter the cost center manager.Cost Center Category: Select from value help. |  |  |
| 5 | Enter Organizational Unit Data of New Cost Center | In the Organizational Units section, make the following entries:Standard Hierarchy Node: Select from value help.Company Code: 3310Functional Area: Select from value help.Profit Center: Select from value help. |  |  |
| 6 | Save New Cost Center | Choose Save. |  |  |
| 7 | Exit the Opened Cost Center | Close the opened cost center panel. | You return to the cost center search screen. |  |
| 8 | Search Cost Center to be Changed | On the cost center search screen, in the Standard section, enter search criteria and choose Go. | All cost centers matching your search criteria are listed in the results section of the cost center search screen. In case no search criterion is entered, all cost centers are listed. |  |
| 9 | Select Cost Center to be Changed | In the list of results, open the cost center you want to change. | A new screen with the cost center master data opens in addition to the cost center search screen. |  |
| 10 | Update Cost Center Data | Select Edit in the upper part of the cost center panel. Modify, for example, the description and choose Save. |  |  |
| 11 | Exit Cost Center Edit Screen | Close the open cost center panel. | You return to the cost center search screen. |  |
| 12 | Search Cost Center for Multiple Language Maintenance | On the cost center search screen, in the Standard section, enter search criteria and choose Go. | All cost centers matching your search criteria are listed in the results section of the cost center search screen. If no search criterion is entered, all cost centers are listed. |  |
| 13 | Select Cost Center for Multiple Language Maintenance | In the list of results, open the cost center you want to change. | A new screen with the cost center master data opens in addition to the cost center search screen. |  |
| 14 | Expand Translation and Long Text Section | In the open cost center, go to the Translation section. | A table is displayed containing the languages in which the name, description, and possibly, long text description of the chosen cost center are listed. |  |
| 15 | Maintain Cost Center Name and Description in Multiple Languages | Choose Edit in the upper part of the cost center panel and make the following entries:Language Key: For example, DECost Center Name: enter the translated name as appropriate.Cost Center Description: add as appropriate.Optionally, you can add a Long Description via the corresponding button.Repeat this for other languages as required, for example Chinese, French, Spanish, and Portuguese. When done, choose Save. | The system confirms that data has been saved. The data maintained in multiple languages is visible in the Translation section. |  |
| 16 | Exit Cost Center Edit Screen | Close the open cost center panel. | You return to the cost center search screen. |  |

#### View Cost Center Data

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The Administrator checks if the cost center updates have been replicated correctly to SAP SuccessFactors Employee Central.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to SAP SuccessFactors Employee Central as an HR Manager. |  |  |
| 2 | Go to Administration Center | From the Home dropdown in the upper left corner, choose Admin Center. |  |  |
| 3 | Go to Manage Data | On the Admin Center screen, go in the Company Processes & Cycles portlet to Employee Files and choose Manage Data.Note You can add this link to your favorites if you right-click it. You can then choose the link from the My Admin Favorites portlet on the Home page, or from the My Favorites portlet on the Admin Center screen. |  |  |
| 4 | Search New Cost Center | On the Manage Data screen, in the Search field, select Cost Center from the dropdown list. In the blank field next to the Search field, search and select the new cost center you have created in SAP S/4HANA Cloud Public Edition and just replicated to SAP SuccessFactors Employee Central. | The result is displayed below the Search portlet: on the right part of the screen, a portlet with the current details of the chosen cost center is displayed. On the left part of the screen, the History portlet for this cost center is displayed. |  |
| 5 | Check New Cost Center Data | Check if the new cost center has been replicated correctly from SAP S/4HANA Cloud Public Edition. |  |  |
| 6 | Search Updated Cost Center | On the Manage Data screen, in the Search field, select Cost Center from the dropdown list. From the blank field next to the Search field, search and select the cost center you have changed in SAP S/4HANA Cloud Public Edition and just replicated to SAP SuccessFactors Employee Central. | The result is displayed below the Search portlet: on the right part of the screen, a portlet with the current details of the chosen cost center is displayed; on the left part of the screen, the History portlet for this cost center is displayed. |  |
| 7 | Check Updated Cost Center Data | Check if the changed data, for example, the description, has been replicated correctly from SAP S/4HANA Cloud Public Edition. |  |  |
| 8 | Search Cost Center Updated with Multiple Language Description | On the Manage Data screen, in the Search field, select Cost Center from the dropdown list. From the blank field next to the Search field, search and select the cost center for which you have maintained the description in multiple languages in SAP S/4HANA Cloud Public Edition and just replicated to SAP SuccessFactors Employee Central. | The result is displayed below the Search portlet: on the right part of the screen, a portlet with the current details of the chosen cost center is displayed, on the left part of the screen, the History portlet for this cost center is displayed. |  |
| 9 | Check Multiple Language Description of Cost Center | Select the View Translations icon <!-- image omitted: unnamed -->next to the Description field.In the dialog box, verify that the translations of the cost center description you performed in SAP S/4HANA Cloud Public Edition have been replicated correctly. When done, choose Done. |  |  |

### Employee Workforce Data Replication

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

The following sections deal with employee workforce-related data replication from SAP SuccessFactors Employee Central to SAP S/4HANA Cloud Public Edition. You find details on how to enter hiring data for a newly hired employee, how to verify that data replication was processed successfully, and how to proceed if the replication fails.

One section is dedicated to contingent workers. Companies can hire contingent workers to deliver services on a non-permanent basis. The contingent workers are often known as independent professionals, temporary-contract workers, or labor hires. After the work order, to which the contingent worker is assigned, has ended, the status of the contingent worker turns inactive in the system. Nevertheless, the contingent worker can be reactivated by assigning him or her to other work orders.

At high level, this process is as follows: hiring data of new employees and contingent workers is entered into the SAP SuccessFactors Employee Central system. This data is then replicated automatically to SAP S/4HANA Cloud Public Edition, where it can be checked for correctness. As the employee and contingent worker data must always be up-to-date, changes of employee's master data records can be performed in SAP SuccessFactors Employee Central. These changes are then replicated automatically as delta changes to SAP S/4HANA Cloud Public Edition, where they can be checked for correctness.

During his or her life cycle at the company, the employee or contingent worker might be terminated. For this, termination-specific data is entered SAP SuccessFactors Employee Central. This data is then replicated automatically to SAP S/4HANA Cloud Public Edition, where it can be checked for correctness. It might occur that a terminated employee returns to the company. In this case, rehiring data of the rehired employee is entered into the SAP SuccessFactors Employee Central system. This data is then replicated automatically to SAP S/4HANA Cloud Public Edition, where it can be checked for correctness. Similarly, every change in the employee data including changes in personal information, job classifications, or organizational information are replicated as delta load. That means that only employee data that has changed in SAP SuccessFactors Employee Central since the last synchronization is replicated to SAP S/4HANA Cloud Public Edition.

For more details on hiring and terminating employees and contingent workers, please refer to the documentation on SAP Help Portal. Go to [SAP Help Portal](https://help.sap.com/viewer/index) and search for SAP SuccessFactors Employee Central. Once you've arrived at the product page, enter a search term, for example, Managing Employment in Employee Central.

|  |
| --- |
| Note The batch job, which has been scheduled in SAP S/4HANA Cloud Public Edition on a regular basis, extracts and replicates the employee master data from SAP SuccessFactors Employee Central to SAP S/4HANA Cloud Public Edition. |

#### Hire New Employee

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The HR manager enters hiring data for a newly hired employee. This data includes legally mandated, company-specific, and personal data for the employee.

Prerequisites

Before you start hiring any employee, make sure that the following information has been replicated.

- Company codes are replicated from SAP S/4HANA Cloud Public Edition to SAP SuccessFactors Employee Central legal entities.
- Cost centers are replicated from SAP S/4HANA Cloud Public Edition to SAP SuccessFactors Employee Central.
- Bank master data from SAP S/4HANA Cloud Public Edition is replicated to SAP SuccessFactors Employee central banks.
- Generic objects from SAP SuccessFactors Employee Central are replicated to SAP S/4HANA Cloud Public Edition organizational objects.
- New Hire Employee Manager is replicated from SAP SuccessFactors Employee Central to SAP S/4HANA Cloud Public Edition.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to SAP SuccessFactors Employee Central as an HR Manager. |  |  |
| 2 | Go to Admin Center Screen | From the Home dropdown, select Admin Center. |  |  |
| 3 | Add New Employee | In the Manage Employees portlet of the Admin Center screen, choose Update User Information > Add New Employee.Note You can add Add New Employee to My Favorites and start the process from there. | You are directed to the My Employee File - Add New Employee screen. |  |
| 4 | Enter Identity Information for New Employee | On the Identity section, make the following entries:Hire Date: select from calendar helpCompany: Company Code 3310Event Reason: New Hire (HIRNEW)In the Name Information block, make the following entries:First Name: enter as appropriate, for example, AlanMiddle Name: enter as appropriateLast Name: enter as appropriate, for example, MustermannSuffix: select from the dropdown list, if appropriateSalutation: enter as appropriate, for example, Mr.Birth Name: enter as appropriateIn the Biographical Information block, make the following entries:Date Of Birth: select from calendar helpCountry Of Birth: select from dropdown if appropriateIn the Employee Information block, make the following entries:Person ID: enter as appropriate, should not be longer than 20 characters and letters should be capitalNote It is recommended to use a number range having as prefix EC in order to easily find the employee after replication to SAP S/4HANA Cloud Public Edition.Note Person ID is an external field, which is used to identify the employee as a person. The internal Person ID field is used to identify the employee in technical communication from Employee Central to SAP S/4HANA Cloud Public Edition. Both the internal and external Person IDs are forwarded to SAP S/4HANA Cloud Public Edition. The external Person ID is used as the ID of the employee for display and search in SAP S/4HANA Cloud Public Edition. |  |  |
| 5 | Continue | Choose Continue. | The Personal Information section in the Add New Employee screen is expanded. |  |
| 6 | Enter Personal Information for New Employee | In the Personal Information section, make the following entries:Gender: select from dropdown, for example, MaleMarital Status: select from dropdownTitle: select from dropdown if appropriatePreferred Name: enter if appropriateNationality: select from dropdownNote Only stable information, such as gender, title, and preferred name are made available in SAP S/4HANA Cloud Public Edition. Therefore, the personal information stored in SAP S/4HANA Cloud Public Edition is not time-dependent, since relevant changes in the future are not expected. |  |  |
| 7 | Enter Contact Information for New Employee | In the Email Information block, select the (+) Add link. The editable fields show up and you can enter following information:Email Type: select Business from dropdownEmail Address: enter as appropriateNote For testing purposes, we recommend that you add your own valid email address as email address, in order to receive an email from the system with the logon data to the SAP SuccessFactors Employee Central instance.Is Primary: defaults to Yes; adapt if appropriate.Note The other available email types are not relevant for integration with SAP S/4HANA Cloud Public Edition.In the Phone Information block, select the (+) Add link. The editable fields show up and you can enter following information:Phone Type: select Business from dropdownCountry Code: enter +65Area Code: enter as appropriate, for example, (0)9Phone Number: enter as appropriateExtension: enter if appropriateIs Primary: defaults to Yes; adapt if appropriate.Note Phone information relevant for SAP S/4HANA Cloud Public Edition is Business and Cell. These two phone types are replicated to SAP S/4HANA Cloud Public Edition and made available there as part of the employee workplace address together with the email of type Business. |  |  |
| 8 | Continue | Choose Continue. | The Job Information section in the Add New Employee screen is expanded. |  |
| 9 | Enter Organizational Information for New Employee | In the Organizational Information block, make the following entries:Company: value Company Code 3310 is defaulted; leave as isBusiness Unit: select from dropdownDivision: select from dropdownDepartment: select from dropdownLocation: select from dropdownCost Center: select from dropdownCaution The Cost Center field must be filled! It will be required in order to staff the employee on a project in SAP S/4HANA Cloud Public Edition. It is also needed by the employee for recording times in timesheet, especially for non-project related tasks.Timezone: defaulted based on the value entered in the Location field. |  |  |
| 10 | Enter Job Information for New Employee | In the Job Information block, make the following entries:Supervisor: select name of supervisor of new employee from dropdownNote In case of the first employee in the instance, select No Manager.Job Classification: select from dropdownStandard Weekly Hours: defaulted based on the value entered in the Location fieldWorking Days Per Week: enter as appropriate, for example, 5Select the Show <#> more fields link and make the following entries:Cost Level: Enter value 1Note Cost Level is a custom field and you must choose the value that is configured. | Depending on the propagation rule configured in your instance, the following fields will be auto-populated from the value you have chosen for the Job Classification: Job Title, Local Job Title, Pay Grade, Regular/Temporary, and FTE. |  |
| 11 | View Employment Details of New Employee | In the Employment Details block, note that original start, seniority start, and service dates default to the hire date entered in the Identity section.Note The Is Contingent Worker field is set to No and is read-only. |  |  |
| 12 | Continue | Choose Continue. | The Compensation Information section in the Add New Employee screen is expanded. |  |
| 13 | Enter Compensation Information for New Employee | In the Compensation Information block, make the following entries:Pay Group: select from dropdown |  |  |
| 14 | Submit Data | Choose Submit or Continue. | The system generates a success message, informing you about the hire date of the new employee. You may choose to view the employee’s profile, add hiring data of another new employee, or simply return to the home page.The system automatically sends a welcome-email from your email account to the new employee, containing logon information for the same. |  |
| 15 | View Employee Profile | Choose the View profile of <new employee name> link. | You are directed to My Employee File > new <employee name> > Personal Information section. |  |
| 16 | Verify Data | Verify the data displayed in the employee profile. For example, in the Job Information subsection, check value of the Employee Status field. | The new employee has the Employee StatusActive. |  |

##### Monitor Employee Data Replication

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The HR Manager monitors the success or failure of the creation of the master data record as well as employee workforce assignment of the newly hired employee in the SAP S/4HANA Cloud Public Edition system. Therefore, check the replication status for each employee to see if there are any failed replications.

|  |
| --- |
| Note To access the AIF interfaces, you need to create a role and assign the corresponding business catalog to this role. See SAP Note [2942866](https://me.sap.com/notes/2942866). |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a user with the role that you've created as described in in SAP Note [2942866](https://me.sap.com/notes/2942866). |  |  |
| 2 | Go to Message Dashboard | Choose from the dropdown menu Message Monitoring.Open the Overview Message Monitoring (F4515) app. |  |  |
| 3 | Select the Monitoring Data | In the Interface Monitor, select values for From (Date/Time) and To (Date/Time) in order to limit the time range for the monitoring records.Choose Go to obtain the messages corresponding to this time range.In the Result List card, select Worker Integration - /WFD - WFD_WORKER-1 in the Namespace / Interface and choose Error or Success. |  |  |
| 4 | Check Status of Worker Data Replication | In the Message Monitoring screen, in the Log Messages panel, you see now all worker replication log messages for your selected time range. Error messages and success messages are included.Filter for the Log Messages belonging to the worker you’ve hired. These messages can be displayed by selecting the corresponding message line.You can filter based on the External Person ID. This corresponds to the person ID entered when hiring the employee in your source system. Filter for the Log Messages belonging to the worker you’ve hired.Choose the corresponding Log Message for this data message in the Log Message. Resolve any errors you find. | You’ve checked the correctness of the replication of your employee and were able to resolve any errors which have occurred along the way. |  |

##### View Employee Basic Data

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The Administrator - HR Info views the basic data of the employee that has been replicated from SAP SuccessFactors Employee Central. This data includes name information, organizational information, and communication information.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as Administrator - HR Info. |  |  |
| 2 | Search for Employee | In the upper right corner of the screen, select the Search (magnifying glass) icon.From the dropdown menu, choose Apps and select Worker.Search In: Worker: enter <full name> or <*full name parts*> or <Person ID> of the employee and choose the Search Icon. |  |  |
| 3 | Select Employee | On the Search Results screen, choose the Person ID of the employee whose data you want to view. | You’re directed to the employee's fact sheet. |  |
| 4 | View Identity and Personal Information | In the page header, check that the identity and personal information are correctly transferred. For example, check the employee's first name, last name, and person ID as maintained in the source system. |  |  |
| 5 | View Communication Details | In the Personal Information section, in the Contact Data subsection, verify the correctness of the following replicated data:Check that the phone information of type Business has been correctly transferred. This is visible in the Phone field.Check that email address of type Business has been correctly transferred. This is visible in the Email field. |  |  |
| 6 | View Work Agreements Details | In the Work Agreements section, verify the correctness of the following replicated data:Company CodeStart Date/End Date: hire date/system high date.Choose the triangle next to the Company Code and navigate to the Work Assignment Information. Check the following data:Job TitleManager: (this field has to contain the value of the field Supervisor from the source system).Cost CenterVerify that the Employment Status is Active.Note The fields displayed in the table sections can be adjusted. To do so, choose the Settings icon on top of the tables, flag the appropriate checkbox, and choose OK. |  |  |
| 7 | View Service Cost Level | Scroll down to the Service Cost Level area. | Check that the Service Cost Level and Description as maintained in the source system have been correctly replicated. |  |
| 8 | View Payment Details | Go to the Payment Information tab. | The Payment Information tab is displayed, containing several sections. |  |
| 9 | View Detailed Payment Information | Check that the routing number, bank, and account number as maintained in the source system have been correctly replicated into the fields Bank Key, Bank Name, and Bank Account. If necessary, check also other fields if they were replicated. Check the validity period. Dependent on the payment method and country/region chosen, different fact sheet fields may have been filled with values.The Payment Methods field contains the value T, meaning bank transfer.The Payment Methods field contains the value C, meaning bank check.Note The Payment Information Tab is only displayed once payment information is maintained for this employee. |  |  |

#### Hire New Contingent Worker

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The HR manager enters master data for a new contingent worker. This data includes personal data, company-specific data, and work-order-related data for the contingent worker.

Prerequisites

Before you start hiring any contingent worker, make sure the following information has been replicated or created in relevant systems.

- Company codes are replicated from SAP S/4HANA Cloud Public Edition to SAP SuccessFactors Employee Central legal entities.
- Cost centers are replicated from SAP S/4HANA Cloud Public Edition to SAP SuccessFactors Employee Central.
- Generic objects from SAP SuccessFactors Employee Central are replicated to SAP S/4HANA Cloud Public Edition organizational objects.
- Suppliers in SAP S/4HANA Cloud Public Edition are created and available in SAP SuccessFactors Employee Central as vendors. See below for instructions on how to create a vendor in SAP SuccessFactors Employee Central.
- New hire contingent worker manager is replicated to SAP S/4HANA Cloud Public Edition.

Create Vendor in SAP SuccessFactors Employee Central

For the work-order information of the contingent worker, it is a prerequisite to have a vendor in SAP S/4HANA Cloud Public Edition. Otherwise, the replication of the contingent worker data from SAP SuccessFactors Employee Central to SAP S/4HANA Cloud Public Edition will fail. To create a vendor in SAP SuccessFactors Employee Central, proceed as follows:

1. Log on to the SAP Fiori launchpad as Master Data Specialist - Business Partner Data.
2. Open Manage Business Partner Master Data (F3163).
3. On the left part of the screen, select the Find tab and make following entries in the search fields:

Find: select Organizations from dropdown.

By: select Supplier Number from dropdown.

Select Start.

1. In the search result list, double-click on the supplier of interest. To ensure it is a supplier, check that the dropdown menu Display in BP role contains at least one of the roles Supplier or Supplier (Fin.Accounting). Take note of the supplier ID (visible in the read-only field Business Partner on top of the screen), and name (visible in the Name section of the Address tab), and validity start date (visible for example in Address tab > Communication > Address Valid From) of the supplier; you will need them in order to create the appropriate vendor in the SAP SuccessFactors Employee Central system, if not already maintained there.

|  |
| --- |
| Note The vendor information can be created in SAP SuccessFactors Employee Central as follows:Log on to Employee Central and navigate to Home > Admin Center.In the Company Processes & Cycles portlet of the Admin Center screen, select Employee Files > Manage Data.From the Create New dropdown, select VendorInfo. Fill the upcoming fields with the same data as the vendor created in SAP S/4HANA Cloud Public Edition . Choose Save. |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to Employee Central as an Administrator - HR Info. |  |  |
| 2 | Go to Admin Center Screen | From the Home dropdown, select Admin Center. |  |  |
| 3 | Add Contingent Employee | In the Manage Employees block of the Admin Center screen, choose Update User Information > Add Contingent Worker.Note You can add Add Contingent Worker to My Favorites and start the process from there. |  |  |
| 4 | Enter Identity Information for Contingent Employee | In the Identity Information section, make the following entries:Start Date: select from calendar helpCompany: Company Code 3310In the Name Information block, make the appropriate entries for following fields:First Name: enter as appropriateMiddle Name: enter as appropriateLast Name: enter as appropriateSalutation: select from dropdownIn the Employee Information block, make the following entry:Person Id: enter as applicable; should not be longer than 20 characters and letters should be capital. |  |  |
| 5 | Continue | Choose Continue. | The Personal Information section in the Add Contingent Worker screen is expanded. |  |
| 6 | Enter Contact Information for Contingent Worker | In the Contact Information block of the Personal Information section, select the (+) Add link below the email table header. The editable fields show up and you can enter following information:Email Type: select Business from dropdownEmail Address: enter as appropriateIs Primary: defaults to Yes; adapt if appropriateNote The other available email types are not relevant for integration with SAP S/4HANA Cloud Public Edition. |  |  |
| 7 | Continue | Choose Continue. | The Contingent Worker Assignment Information section in the Add Contingent Worker screen is expanded. |  |
| 8 | Enter Organizational Information for Contingent Employee | In the Organizational Information block, make the following entries:Company: value Company Code 3310 is defaulted; leave as isMake entries as appropriate for the following fields:Business Unit: select from dropdownDivision: select from dropdownDepartment: select from dropdownLocation: select from dropdownCost Center: select from dropdownCaution The Cost Center field must be filled in order to be able to staff the contingent worker on a project in SAP S/4HANA Cloud Public Edition.Timezone: defaulted based on value entered in the Location field. |  |  |
| 9 | Enter Job Information for Contingent Worker | In the Job Information block, make the following entries:Supervisor: For example, enter the manager of the business unit, or simply No Manager.Job Classification: select from dropdownStandard Weekly Hours: defaulted based on value entered in field LocationWorking Days Per Week: enter as appropriate, for example 5Select the Show <#> more fields link and make the appropriate entries. | Dependent on the propagation rule configured in your instance, some fields will be auto-populated from the value you have chosen for the Job Classification. |  |
| 10 | Continue | Choose Continue. | The Work Order Information section in the Add Contingent Worker screen is expanded. |  |
| 11 | Enter Work Order Information for Contingent Worker | In the Work Order block, make the following entries:Work Order ID: enter as appropriateWork Order Name: enter as appropriateOwner ID: enter name partsNote The individual responsible for work orders. This can be a procurement specialist, supervisor, or a manager.Supplier: select from dropdown, the vendor as existing in SAP S/4HANA Cloud Public Edition.Caution For the employee class Freelancer, the value contained in the Supplier field is not transferred to SAP S/4HANA Cloud Public Edition!End Date: select from calendar help the date on which the engagement of the contingent worker ends in the work order.Note Starting one day after this date the work order turns inactive and the contingent worker will no longer be active in the system. |  |  |
| 12 | Submit Data | Choose Submit or Continue. | The system generates a success message, informing you about the hire date of the new contingent worker. You may choose to view the profile of the contingent worker, add data of another employee, or simply return to the home page.The external person ID has been generated automatically by the system. |  |
| 13 | View Contingent Worker Profile | Choose View profile of <contingent worker name>. | You are directed to My Employee File > new contingent worker name>page, containing two sections: Personal Information and Employment Information. In the Header, above the name, the Contingent Worker symbol is displayed. |  |
| 14 | Verify Data | Verify the data displayed in the different sections:In the Job Information subsection of the Employment Information section, check that value of field Employee Status is Active.In the Organizational Information subsection of the Employment section, select the pending future change in the Job Information (<Date>) link. In the upcoming Change History: Organizational Information Changes dialog box, view the details of the two records created with appropriate events and event reasons: Start Contingent Worker and End Contingent Worker. In the record related to event End Contingent Worker, check that value of field Employee Status is Terminated and the effective date of that change is one day after the date maintained in field End Date in the Work Order block.Note Alternatively, you can select the Pending future change in Job Information (<Date>) link in the Job Information subsection of the Employment Information section, and check above mentioned details. | The contingent worker has Employee StatusActive. |  |

##### Monitor Contingent Worker Data Replication

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The HR Manager monitors the success or failure of the creation of the master data record as well as employee workforce assignment of the newly hired contingent worker in the SAP S/4HANA Cloud Public Edition system. Therefore, check the replication status for each contingent worker to see if there are any failed replications.

|  |
| --- |
| Note To access the AIF interfaces, you need to create a role and assign the corresponding business catalog to this role. See SAP Note [2942866](https://me.sap.com/notes/2942866). |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a user with the role that you've created as described in in SAP Note [2942866](https://me.sap.com/notes/2942866). |  |  |
| 2 | Go to Message Dashboard | Choose from the dropdown menu Message Monitoring.Open the Overview Message Monitoring (F4515) app. |  |  |
| 3 | Select the Monitoring Data | In the Interface Monitor, select values for From (Date/Time) and To (Date/Time) in order to limit the time range for the monitoring records.Choose Go to obtain the messages corresponding to this time range.In the Result List card, select Worker Integration - /WFD - WFD_WORKER-1 in the Namespace / Interface and choose Error or Success. |  |  |
| 4 | Check Status of Worker Data Replication | In the Message Monitoring screen, in the Log Messages panel, you see now all worker replication log messages for your selected time range. Error messages and success messages are included.Filter for the Log Messages belonging to the worker you’ve hired. These messages can be displayed by selecting the corresponding message line.You can filter based on the External Person ID. This corresponds to the person ID entered when hiring the employee in your source system. Filter for the Log Messages belonging to the worker you’ve hired.Choose the corresponding Log Message for this data message in the Log Message. Resolve any errors you find. | You’ve checked the correctness of the replication of your employee and were able to resolve any errors which have occurred along the way. |  |

##### View Contingent Worker Data

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The Administrator - HR Info views the data of the contingent worker as replicated from the source system. This data includes information related to name, communication, organization, and vendor, if applicable.

For each contingent worker replicated from the source system, a business partner of role Service Performer is created in SAP S/4HANA Cloud Public Edition. In addition, a relationship between the contingent worker and the vendor maintained in the work order in the source system is automatically created in SAP S/4HANA Cloud Public Edition.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as Administrator - HR Info. | The page containing the Fiori apps associated with your role is displayed. |  |
| 2 | Search Contingent Worker | On the top-right corner of the screen, select the Search (magnifying glass) icon. In the two editable search fields on top of the screen, make following entries:All: select Worker from the dropdown listSearch In: Worker: enter <full name> or <*full name parts*> of the contingent worker and choose Enter. | In the Search Results screen, the system proposes a list of employees matching your search criteria. For each employee, a short overview of organizational details is given, like company code, cost center, and organizational unit to which they’re assigned. Also the job title, person ID as entered in the source system, and manager, if entered. The contingent workers are marked accordingly. |  |
| 3 | Select Contingent Worker | In the Search Results screen, choose the <ID number> of the employee whose data you want to view. | You’re directed to the factsheet. |  |
| 4 | View Identity and Personal Information | In the page header, check that the identity and personal information attributes are correctly transferred. For example, check the contingent worker's first name and last name, and their external person ID as generated and replicated from the source system. |  |  |
| 5 | View Communication Details | In the Contact Information subsection of the Personal Information section, check that:The email address of type Business has been correctly transferred. This is visible in the Email fieldThe phone information of type Business has been correctly transferred. This is visible in the Phone field. |  |  |
| 6 | View Work Agreements Details | In the Work Agreements section, verify the correctness of the following replicated data:Company CodeStart Date/End Date: hire date/system high date.Choose the triangle next to the Company Code and navigate to the Work Assignment Information. Check the following data:Job TitleManager: (this field has to contain the value of the field Supervisor from the source system).Cost CenterVerify that the Employment Status is Active.Note The fields displayed in the table sections can be adjusted. To do so, choose the Settings icon on top of the tables, flag the appropriate checkbox, and choose OK. |  |  |
| 7 | View Service Cost Level | Scroll down to the Service Cost Level area. | Check that the Service Cost Level and Description as maintained in the source system have been correctly replicated. |  |
| 8 | View Vendor Information | In the Worker Types subsection of the Personal Information section, the potential relationship of the contingent worker to a vendor is visible.In case the contingent worker is a ServicePerformer, a relationship between the contingent worker and the vendor entered in the work order in the source system is automatically created in SAP S/4HANA Cloud Public Edition. Verify that the Vendor field contains the appropriate supplier as maintained in the work order in the source system. |  |  |

#### Maintain Additional Information (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The information contained in the employee file must be up-to-date, so the HR Manager creates new records and adapts existing ones as appropriate in SAP SuccessFactors Employee Central. The following sections describe the maintenance procedure for several types of employee data.

|  |
| --- |
| Note The additional information can also be maintained during the hiring process of an employee. |

|  |
| --- |
| Caution Maintenance of employee data is relevant only for active employees! |

|  |
| --- |
| Note Every change in the employee data is replicated as a delta load, that is, only employee data that has changed in SAP SuccessFactors Employee Central since the last synchronization is replicated to SAP S/4HANA Cloud Public Edition. The frequency of these replications depends on the schedule that has been set for the batch job in SAP S/4HANA Cloud Public Edition. |

Procedure for selecting an employee

For maintaining employee information, the HR Manager needs to select the employee first. In order not to overload the procedure for each step with details to searching and selecting the employee, we describe it in detail below:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to SAP SuccessFactors Employee Central as an HR Manager. |  |  |
| 2 | Search for Employee | In the People Search field on the upper right corner of the screen, enter the name (or name parts) of the employee whose data you want to maintain. For example, AlanMustermann | The system proposes a list of employees matching your search criteria. |  |
| 3 | Select Employee | Choose in the list of employees the appropriate employee. | You are directed to the Employee Files page, on which the employee's existing data record is divided into several sections: Personal Information, Employment Information, and Payment Information. The default view is the Personal Information section.In addition, if Time Off is enabled in your SAP SuccessFactors Employee Central instance, the Time Off section is also visible. |  |
| 4 | Continue | Continue with the procedure as described in:[Maintain Address Information](#unique_20) [page ] 35 |  |  |

##### Maintain Address Information

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The HR Manager maintains the address information of the employee as necessary. He or she updates the existing home address data for a specified employee.

The employee home address is replicated to the SAP S/4HANA Cloud Public Edition system and made available in the vendor created for the employee. The home address can be maintained time-dependently in SAP SuccessFactors, but only the current address is shown at the vendor. This is achieved through a scheduled job in SAP S/4HANA Cloud Public Edition handling maintenance of addresses into the future in SAP SuccessFactors.

|  |
| --- |
| Note If granted the appropriate edit permissions, employees can maintain their own address information. |

|  |
| --- |
| Note The home address is country-specific. Depending on the country selected, different fields are to be filled. |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Edit Address Information | In the Address Information subsection of the Personal Information section, select the Pencil icon next to the Addresses block. | The Home Address dialog box is displayed. |  |
| 2 | Enter Effective Change Date | In the Home Address dialog box, enter an effective date of change.When would you like your changes to take effect: select using the calendar icon. |  |  |
| 3 | Create New Home Address Record | In the Home Address block, make the following entries:Note The home address is country-specific. Depending on the country selected, different fields are to be filled.Country: United Arab Emirates, leave as isCare Of: enter if appropriateStreet: enter as appropriateHouse Number: enter as appropriateApartment: enter if appropriateExtra Address Line: enter if appropriatePostal Code: enter as appropriate, for example, 118353City: enter as appropriate, for example, DubaiDistrict: enter as appropriateRegion: select from dropdown |  |  |
| 4 | Save Data | Choose Save. | A system message confirms that the data has been saved. The data is visible in the employee’s file. If the changes are effective on a future date, select the Pending future change in Home Address (mm/dd/yy) link to view the changes. |  |

|  |
| --- |
| Note If you need to correct an existing home address rather than entering a new effective dated home address, proceed as follows:In the Address Information subsection of the Personal Information section, select the Clock icon next to the Addresses block.In the Change History part of the upcoming dialog box, select the record you want to correct and choose Edit.In the Edit History of Home Address on <effective start date> dialog box, leave the date as is and make the appropriate correction. When done, choose Save. |

##### View Address Information

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
| Note This information isn’t relevant for terminated employees. |

For each employee replicated from the source system, a business partner is created in SAP S/4HANA Cloud Public Edition.

The Master Data Specialist - Business Partner Data views the address information of the employee as replicated from the source system. The factsheet of the created business partner is used.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Master Data Specialist - Business Partner Data. |  |  |
| 2 | Open the App | In the Business Partner Master section, choose the Manage Business Partner Master Data (F3163) tile. |  |  |
| 3 | Search Employee | In the search screen, select values for the business partners to be selected, for example:Last Name: enter the <last name> of the employee.First Name: enter the <first name> of the employee.Choose Go. | In the search results panel, the system proposes a list of Business Partners matching your search criteria. |  |
| 4 | Select Employee | In the search results panel, choose the record of the business partner whose data you want to view. | The details of the selected business partner are shown in a fact sheet. |  |
| 5 | Go to Address | Go to the Address tab. Select the Address Details section there. |  |  |
| 6 | View Detailed Address Information | Choose the Address Details record with the validity data range you want to display. |  |  |
| 7 | View Address Information | Go to the Address tab and choose See More. The the data maintained in Employee Central for the Home Address is displayed. Check the correctness of the replicated data. |  |  |

##### Maintain Payment Information

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The HR Manager maintains payment information of the employee. This data is then replicated to the SAP S/4HANA Cloud Public Edition system where it is required for controlling payout of expenses.

In the following, the maintenance of pay type Main with payment method Bank Transfer is described.

|  |
| --- |
| Note To ensure that the entered payment information is sent to your SAP S/4HANA Cloud Public Edition system, you first have to enter the Home Address of an employee. If granted the appropriate edit permissions, employees can maintain their own payment information. |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Edit Payment Information | Go to the Payment Information section and select the Pencil icon next to the Payment Information block. |  |  |
| 2 | Enter Effective Date | Enter effective date of changeWhen do you want your changes to take effect?: select using calendar icon |  |  |
| 3 | Add New Record | Select the Add link in the lower left corner of the Payment Information dialog box. | The fields for adding new data become editable below the already existing record. |  |
| 4 | Create New Payment Information Record | In the Payment Information block, select the (+) icon. The editable fields show up and you can enter the following information:Pay Type: select Main Payment Method from the dropdown listPayment Method: select Bank Transfer (05) from the dropdown list.Note Dependent on the payment method chosen, different editable fields will be displayed for entering values.Purpose: enter the purpose of the transfer, if appropriateBank Country: select United Arab Emirates (AE) from dropdown if not defaulted upon entering Payment Method field.For maintaining the other relevant fields, you have three options:Option 1:Bank: select from dropdown list.Note Make sure to select a bank which exists also in the SAP S/4HANA Cloud Public Edition system, otherwise the replication of payment data will fail. See the note at the beginning of this section.Account Owner: enter the employee’s nameRouting Number: defaulted from the bank chosen in the Bank field.Account Number: enter as appropriate.Business Identifier Code: defaulted from the bank chosen in the Bank field.Option 2:Account Owner: enter employee’s nameBusiness Identifier Code: enter as appropriate, for example, NBADAEAADIR.IBAN: enter as appropriate, for example, AE54500700100113369800.Option 3:Account Owner: enter employee’s nameIBAN: enter as appropriate, for example AE28820800000258006100For all three options:Currency: select UAE Dirham (AED) from dropdown if not defaulted; currency and country should be aligned. |  |  |
| 5 | Save Data | Choose Save. | The system displays a success message. |  |
| 6 | View Payment Information Record | If the newly added payment information is effective starting today, select in the Payment Information block the See more link and check if the data is visible as expected. |  |  |
| 7 | View New Future Dated Payment Information Record (Optional) | If the newly added payment information is effective on a future date, select in the Payment Information block the Clock icon.In the Change History part of the upcoming Payment Information: Changes dialog box, select the appropriate record and check if the newly added payment information is displayed as expected. |  |  |

##### View Payment Information

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
| Note This information is not relevant for terminated employees. |

Procedure to view payment information in SAP Fiori launchpad

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Administrator - HR Info. | The page containing the SAP Fiori apps associated with your role is displayed. |  |
| 2 | Search Employee | Select the search (  ) icon.From the dropdown menu, select Worker.Search in: Worker: enter <full name> or <*full name parts*> or <Person ID> of the employee and choose the Search Icon (  ). |  |  |
| 3 | Select Employee | In the Description section, double-click the <employee name> link of the employee whose data you want to view, for example, Alan Mustermann. |  |  |
| 4 | Work Agreements | Choose the Work Agreements tab.Choose the Triangle next to the Worker Type to see the details of the Work Agreements. |  |  |
| 5 | View Payment | Go to the Payment Information tab.Note The Payment Information tab will only show up if valid payment information is maintained for this employee. |  |  |
| 6 | View Detailed Payment Information | Check that the routing number, bank, and account number as maintained in SAP SuccessFactors Employee Central have been correctly replicated into the fields Payment Method, Bank Key, and Bank acct.Check the validity period. |  |  |
| 7 | Check Payment Method | Check that the Payment methods field contains the value I (ISO PAIN001: Credit Transfer). |  |  |

##### Maintain Service Cost Level

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In the Customer Factsheet, you can review the controlling information for the active employments along with the validity dates. You can also view the Service Cost Level information along with the validity start date.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to SAP S/4HANA Cloud Public Edition via the SAP Fiori Launchpad as Administrator HR Info. | The page containing the Fiori apps associated with your role is displayed. |  |
| 2 | Access the Search | Choose the magnifier icon to access the Search in the SAP Fiori Launchpad. | The Search environment is expanded. |  |
| 3 | Open Dropdown Menu | From the dropdown menu next to the free text search field, choose Worker. |  |  |
| 4 | Search for an Employee | Enter a valid ID of a worker and choose the magnifier icon to start the search. | The search results are displayed in a list view. |  |
| 5 | Select an Employee | Choose an employee from the result list by selecting the highlighted ID. | The Employee Fact Sheet is displayed. |  |
| 6 | Open Manage Workforce App | Choose Manage Workforce. | The Manage Workforce app opens. |  |
| 7 | Choose Edit | Choose Edit. |  |  |
| 8 | Switch to Work Agreements | Choose the Work Agreements tab and select a Work Agreement to access the Work Agreement details. | The Work Agreement details are displayed. |  |
| 9 | Maintain Service Cost Level | In the Service Cost Level section, choose Create.Maintain Start -and End Data. Choose the Service Cost Level from the Value Help.Choose Apply.Choose Save. |  |  |
| 10 | Navigate Back to Factsheet | Navigate back to the Worker Factsheet. | The factsheet is displayed. |  |
| 11 | Choose Details for Work Agreements | On the Work Agreements tab, choose the triangle to see the Work Agreement details. | The Work Agreement details are displayed. |  |
| 12 | Check Service Cost Level | The maintained Service Cost Level is displayed in the factsheet. | The created Service Cost Level is displayed in the factsheet. |  |

Result

You’ve assigned a Service Cost Level to an Employee.

#### Employee Photo Replication

In the following sections, you find details on how to execute the employee (or contingent worker) photo replication from SAP SuccessFactors Employee Central to SAP S/4HANA Cloud Public Edition. The high-level process is as follows: after executing the initial replication, all photos are replicated to SAP S/4HANA Cloud Public Edition. If any changes are applied to the existing photos in SAP SuccessFactors Employee Central, the changes are replicated automatically to SAP S/4HANA Cloud Public Edition, where they can be checked for correctness.

|  |
| --- |
| Note The process steps described in this chapter are also relevant for contingent workers.The process steps described in this chapter are not relevant for terminated employees. |

##### Maintain Employee Photo

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The HR Manager maintains photos of employee and contingent workers. This may refer to:

- adding a photo for an employee or contingent worker who does not have any photo yet
- exchanging an already replicated photo

|  |
| --- |
| Note In all these cases, a delta replication is triggered. |

Prerequisites

- The employee must have been replicated to SAP S/4HANA Cloud Public Edition before photos can be replicated.

Procedure

|  |
| --- |
| Note Even though in the following only "employee" is mentioned, the procedure is valid for contingent workers, too! |

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to SAP SuccessFactors Employee Central as an HR Manager. |  |  |
| 2 | Search Employee without Photo | In the People: Search field in the top right corner of the page, enter the name (or name parts) of the employee for whom you want to add a photo. |  |  |
| 3 | Select Employee | Choose an employee from the list, for example, AlanMustermann. | You are directed to the Employee Files page in the employee's existing data record is divided into several sections. The default view is the Personal Information section. |  |
| 4 | Go to Header Edit Mode | Select the Header button (Pencil icon) in the right upper corner of the screen. | A callout containing the Edit Profile Picture button is displayed. |  |
| 5 | Edit Photo | Choose the Edit Profile Picture button. |  |  |
| 6 | Add Photo | Continue with one of the two options below:Option 1: Select the Select image file link, select the file with the appropriate photo, and upload it.Option 2: Open the folder containing the photo you want to upload, and move the photo from the folder into the pictogram.For both options, use the Zoom in or Zoom Out icons to adjust the photo into the pictogram. When done, choose Save. | The uploaded photo is visible in the Profile Header of the employee or contingent worker. |  |
| 7 | Search Employee with Photo | In the People: Search field in the top right corner of the page, enter the name (or name parts) of the employee for whom you want to exchange a photo. |  |  |
| 8 | Select Employee | Choose an employee from the list. | You are directed to the Employee Files page, in which the employee's existing data record is divided into several sections. The default view is the Personal Information section. |  |
| 9 | Go to Header Edit Mode | Select the Header button (Pencil icon) in the right top corner of the screen. | A callout containing the Edit Profile Picture button is displayed. |  |
| 10 | Edit Photo | Choose the Edit Profile Picture button. | The Edit Profile Picture dialog box is displayed, where you have the options to upload a new picture or delete the existing one.Note Deletion of a photo is not supported by the middleware. Therefore, if you remove the employee's photo in SAP SuccessFactors Employee Central, his or her last photo transferred to SAP S/4HANA Cloud Public Edition is still visible in the factsheet. |  |
| 11 | Exchange Photo | Select the Upload New Picture button, select the file with the appropriate photo, and upload it.Use the Zoom In or Zoom Out icons to adjust the photo into the pictogram. When done, choose the Save button. | The new photo is visible in the Profile Header of the employee or contingent worker. |  |

##### View Employee Photo

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The Administrator - HR Info views the employee (or contingent worker) photo as replicated from SAP SuccessFactors Employee Central.

Procedure

|  |
| --- |
| Note Even though in the following only "employee" is mentioned, the procedure is valid for contingent workers, too. |

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Administrator - HR Info. | The page containing the Fiori apps associated with your role is displayed. |  |
| 2 | Search Employee | In the upper right corner of the screen, select the Search (magnifying glass) icon. In the two editable search fields, make the following entries:All: WorkerSearch In: Worker: enter <full name> or <*full name parts*> of the employee and press Enter. | On the Search Results screen, the system proposes a list of employees matching your search criteria.For employees with a photo, this photo is visible as a small icon in the search result list. |  |
| 3 | Select Employee with New Photo | In the Search Results screen, choose the <employee name> link of the employee whose initial photo has been uploaded, for example, Alan Mustermann. |  |  |
| 4 | View Newly Uploaded Photo | Check that the photo is displayed below the employee's name in the page header. |  |  |
| 5 | Select Employee with Updated Photo | Search and select the employee whose photo has been updated in SAP SuccessFactors Employee Central. |  |  |
| 6 | View Exchanged Photo | Check that the photo is displayed below the employee's name in the page header. |  |  |

## Appendix

### Process Integration

The process to be tested in this test script is part of a chain of integrated processes.

#### Succeeding Processes

After completing the activities in this test script, you can continue testing the following business processes:

| Process | Business Condition |
| --- | --- |
| Customer Project Management – Project-Based Services (J11) | For Professional Services organizations, after the data of the employee and/or contingent worker has been replicated successfully to SAP S/4HANA Cloud Public Edition, the employee/contingent worker can be staffed on customer projects. |
| Time Recording – Project-Based Services (J12) | For Professional Services organizations, the employee can record the time he or she has worked on different tasks. |

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
> Flagged while digesting this document, not verified: View Bank Data purpose says only initial replication of bank master data is supported yet also says there are editable fields in S/4HANA Cloud for which replication would replicate value changes; the sibling legal entity section says there are no such editable fields.

> [!warning] Conflict
> Flagged while digesting this document, not verified: Payment method values differ between sections: View Employee Basic Data expects Payment Methods T (bank transfer) or C (bank check), while View Payment Information expects I (ISO PAIN001: Credit Transfer).

> [!warning] Conflict
> Flagged while digesting this document, not verified: Hire New Contingent Worker is assigned to role HR Manager in the Overview Table, but its procedure step 1 says to log on to Employee Central as an Administrator - HR Info.

## Connections
- part-of :: [[_cluster]]
- related-to :: [[01-solution-foundation-and-platform/test-script-automated-provisioning-via-sap-cloud-identity-access-gover]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/JB1_S4CLD2608_BPD_EN_AE.docx` — full document · extracted with `mammoth` · 93,050 chars in the whole document
