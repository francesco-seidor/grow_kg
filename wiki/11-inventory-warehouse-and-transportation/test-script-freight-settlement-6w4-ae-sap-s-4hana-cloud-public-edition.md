---
id: 11-inventory-warehouse-and-transportation/test-script-freight-settlement-6w4-ae-sap-s-4hana-cloud-public-edition
title: "Test Script: Freight Settlement (6W4_AE) - SAP S/4HANA Cloud Public Edition (6W4_S4CLD2608_BPD_EN_AE)"
description: "SAP S/4HANA Cloud Public Edition test script for scope item 6W4 Freight Settlement (AE): accrual posting, cost allocation, carrier invoice verification, ERS, SOAP invoices."
cluster: 11-inventory-warehouse-and-transportation
tags: [kb/inventory-warehouse-and-transportation, topic/freight-settlement]
aliases: [6W4_S4CLD2608_BPD_EN_AE]
keywords: [Freight Settlement, freight cost accruals, freight cost allocation, carrier settlement, invoice verification, evaluated receipt settlement, invoice variances, soap carrier invoices, automatic freight cost confirmation, test prerequisites]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/6W4_S4CLD2608_BPD_EN_AE.docx]
confidence: high
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-1196
topic: 11-inventory-warehouse-and-transportation/freight-settlement
language: EN
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Test Script: Freight Settlement (6W4_AE) - SAP S/4HANA Cloud Public Edition (6W4_S4CLD2608_BPD_EN_AE)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/6W4_S4CLD2608_BPD_EN_AE.docx`, extracted with `mammoth`. Grouped under **Freight Settlement** in Inventory, Warehouse and Transportation. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

| <!-- image omitted: unnamed --> | Test ScriptSAP S/4HANA Cloud Public Edition - 19-06-26 |
| --- | --- |
|  | Freight Settlement (6W4_AE) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Table of Contents

[1 Purpose 3](#_Toc232859651)

[2 Prerequisites 4](#_Toc232859652)

[2.1 System Access 4](#_Toc232859653)

[2.2 Roles 4](#_Toc232859654)

[2.3 Master Data, Organizational Data, and Other Data 5](#_Toc232859655)

[2.4 Additional Manual Configuration 6](#_Toc232859656)

[2.5 Business Conditions 7](#_Toc232859657)

[2.6 Preliminary Steps 7](#_Toc232859658)

[2.6.1 Automate Confirmation and Posting of Freight Costs (Optional) 7](#_Toc232859659)

[3 Overview Table 9](#_Toc232859660)

[4 Test Procedures 10](#_Toc232859661)

[4.1 Confirm Freight Costs for Accrual Postings 10](#_Toc232859662)

[4.2 Monitor Freight Cost Allocation Documents 15](#_Toc232859663)

[4.3 Carrier Settlement for Freight Orders and Freight Bookings 17](#_Toc232859664)

[4.3.1 Option A: Invoice Verification 18](#_Toc232859665)

[4.3.1.1 Create Supplier Invoice (Invoice Verification) 18](#_Toc232859666)

[4.3.1.2 Variances in Carrier or Freight Forwarder Invoices (Optional) 20](#_Toc232859667)

[4.3.1.2.1 Variances Between Planned Charges and Charges Received From Carrier or Freight Forwarder Invoice 20](#_Toc232859668)

[4.3.1.2.2 Variances Due to Additional Unplanned Freight Charges 21](#_Toc232859669)

[4.3.2 Option B: Evaluated Receipt Settlement (ERS) 23](#_Toc232859670)

[4.3.2.1 Execute Evaluated Receipt Settlement 24](#_Toc232859671)

[4.3.2.2 Check Supplier Invoice - Generate Credit Memo 25](#_Toc232859672)

[4.3.3 Option C: Carrier Invoice Received via SOAP Message 26](#_Toc232859673)

[5 Appendix 28](#_Toc232859674)

[5.1 Process Integration 28](#_Toc232859675)

[5.1.1 Preceding Processes 28](#_Toc232859676)

[5.1.2 Succeeding Processes 28](#_Toc232859677)

## Purpose

Overview

Freight costs calculated for the freight documents (freight orders and freight bookings) are to be posted in financial accounting to record such costs in accounting as accruals and to pay the carriers or freight forwarders. Once the freight documents are in a status in which the transportation has been initiated or completed, the freight costs can be posted to financial accounting. If there are errors during the posting of accruals, the freight documents can be monitored for such posting errors. The invoice received from the carrier or freight forwarder is verified against the expected costs calculated in the freight document. Depending on the number of invoicing parties involved for a freight document, multiple invoices can be received from different carriers executing the transport. For example, for an ocean freight booking, you can receive invoices from different invoicing carriers to execute different stages of the ocean booking (for example, one for the pick-up, one for the main carriage, and another one for the delivery). During invoice verification, price variances and unplanned freight costs can be captured. Freight cost allocation capabilities are used to manage freight costs that occurred during the transportation processes. The costs are posted to a material valuation in an inbound process, and to an expense account (general ledger) in an outbound process.

This document provides a detailed procedure for testing this scope item after solution activation, reflecting the predefined scope of the solution. Each process step, report, or item is covered in its own section, providing the system interactions (test steps) in a table view. Steps that are not in scope of the process but are needed for testing are marked accordingly. Project-specific steps must be added.

|  |
| --- |
| Note Values in this test script (decimal notation, date formats, and so on) are presented in U.S. standard notation. If your test system is set up to use a different notation, enter values as appropriate. |

## Prerequisites

This section summarizes all the prerequisites for conducting the test in terms of systems, users, master data, organizational data, other test data and business conditions.

|  |
| --- |
| Caution Testing in a 3-System LandscapeIn a 3-system landscape (with SAP Central Business Configuration as your configuration environment), changes to software and business configuration are applied to your systems independently of one another. It is therefore your responsibility to manage the active business configuration in your systems and synchronize configuration data in your SAP S/4HANA Cloud Public Edition system landscape. A synchronization is required, for example, after you've enhanced the scope, extended configuration, or adopted new or changed content from content updates or upgrades. For more information, refer to the [product assistance](https://help.sap.com/docs/SAP_S4HANA_CLOUD/b249d650b15e4b3d9fc2077ee921abd0/6c398c4ae7364af69d3edffe7fdc39f2.html) in the SAP Help Portal.Before testing, if you want to use all software features described for the process steps, reports, or items in this document, we recommend the Business Process Configuration Expert in your organization has upgraded the configuration content and deployed the configuration data to your system landscape.If the decision is not to upgrade the configuration content in your test or production system, you can run regression tests of software changes using the procedures in the previous test script version (see the following [link](https://support.sap.com/content/dam/SAAP/Sol_Pack/S4C/Library/TestScripts/6W4_S4CLD2602_BPD_EN_AE.docx) ). |

### System Access

|  |  |
| --- | --- |
|  | Details |
| System | Accessible via SAP Fiori launchpad. Your system administrator provides you with the URL to access the various apps assigned to your role. |

### Roles

Create business roles using the following business role templates delivered by SAP and assign them to your individual test users.

Alternatively, if available, you can use the following spaces delivered by SAP. You create a space with pages containing predefined essential apps and assign it to the business role. You then assign this business role to your individual users.

For more information, refer to How to Create a Business Role from a Template in the [product assistance](https://help.sap.com/docs/SAP_S4HANA_CLOUD/53e36b5493804bcdb3f6f14de8b487dd/ec310a8b669a45ca898dc4dd91d97de2.html) for SAP S/4HANA Cloud Public Edition.

| Name (Role Template) | ID (Role Template) | Name (Launchpad Space) | ID (Launchpad Space) | Log On |
| --- | --- | --- | --- | --- |
| Transportation Buyer | SAP_BR_TRANSP_BUYER | Transportation Procurement | SAP_TM_SPT_TRANSPBUYER_PC |  |
| Accounts Payable Accountant | SAP_BR_AP_ACCOUNTANT | Accounts Payable / Central Invoice Management - Supplier Invoices / Central Invoicing - Supplier Invoice | SAP_BR_AP_ACCOUNTANT / SAP_MM_SPT_CIM_INV_PC / SAP_MM_SPT_CNTRL_INVOICING_PC |  |
| Configuration Expert - Business Process Configuration | SAP_BR_BPC_EXPERT | Business Process Configuration / Business Process Configuration - Finance / Business Process Configuration - Procurement / Manage your Solution / Business Process Configuration - Workflow / Business Configuration - Feature Management / Business Process Configuration - Extensibility Explorer / Business Configuration - Transportation | SAP_BR_BPC_EXPERT / SAP_FIN_SPT_BPC_EXPERT_PC / SAP_MM_SPT_BIZ_PROC_CONFIGN_PC / SAP_CA_SPT_IC_LND_BASE_PC / SAP_CA_SPT_BPC_WORKFLOW_PC / SAP_CA_SPT_BPC_FM_PC / SAP_EI_SPT_BPC_EXT_PC / SAP_TM_SPT_TRANSPCFG_PC |  |

### Master Data, Organizational Data, and Other Data

The organizational structure and master data of your company have been created in your system during activation. The organizational structure reflects the structure of your company. The master data represents materials, customers, and suppliers, for example, depending on the operational focus of your company.

|  |
| --- |
| Caution Update Behavior of Predelivered Demo DataIn non-productive environments (such as starter systems, sandbox systems, or partner demo systems), SAP initially deploys demo data for your selected scope. You can use this data to test and evaluate business processes.In a customer system, you can receive new or updated demo data after initial activation with further scope enhancements, provided the existing demo data wasn't changed in an incompatible way. If activation errors occur due to incompatible changes in demo data, you're responsible for resolving them. If you don't resolve the errors within a specific time frame, SAP reserves the right to deactivate demo data in your systems. In this case, you can continue by creating your own demo data. Alternatively, you can request that your systems be reprovisioned if you want to work with predelivered demo data again.In partner systems, you can use the demo data deployed with the initial activation. No additional demo data will be deployed in the system with scope enhancements. You can only create additional demo data manually. |

Use your own master data or the following sample data to go through the test procedure.

| Data | Sample Value | Details | Comments |
| --- | --- | --- | --- |
| Company Code | 3310 | Company Code 3310 | In case of the Advanced Intercompany Business Processes, this is the company code of the selling company in Advanced Intercompany Sales and the receiving company in Advanced Intercompany Stock Transfer.It is also used as company code in all other scenarios. |
| Purchasing Organization | 3310 | Purch. Org. 3310 | In case of the Advanced Intercompany Business Processes, this is the purchasing organization of the selling company in Advanced Intercompany Sales and the receiving company in Advanced Intercompany Stock Transfer.It is also used as purchasing organization in all other scenarios. |
| Company Code | 1710 | Company code 1710 (supplying / delivering company) | Company code of the delivering company in Advanced Intercompany Sales and in Advanced Intercompany Stock Transfer. |
| Purchasing Organization | 1710 | Purchasing organization 1710 (supplying / delivering plant) | Purchasing organization of the delivering company in Advanced Intercompany Sales and in Advanced Intercompany Stock Transfer. |
| Plant | 3310 | Plant 1 AE | Plant is used in Evaluated Receipt Settlement. |
| Plant | 1710 | Plant 1 US (supplying plant) | Plant is used in Evaluated Receipt Settlement for the delivering company, in Advanced Intercompany Sales, and in Advanced Intercompany Stock Transfer. |
| Carrier | 33386001 | TM Road Carrier AE 1 | Road carrier AE 1, used for invoice verification. |
| Carrier | 33386002 | TM Road Carrier Self-Billing AE | Road carrier AE 2, used for self-billing (evaluated receipt settlement). |
| Carrier | 33386201 | TM Rail Carrier AE 1 | Rail carrier AE 1, used for invoice verification. |
| Carrier | 33386202 | TM Rail Carrier Self-Billing AE | Rail carrier 2, used for self-billing (evaluated receipt settlement). |
| Carrier | 33386401 | TM Freight Forwarder AE 1 | Freight Forwarder AE 1, used for invoice verification. |
| Carrier | 33386402 | TM Freight Forwarder Self-Billing AE | Freight Forwarder AE 2, used for self-billing (evaluated receipt settlement). |
| Carrier | 17386401 | TM Freight Forwarder US 1 | Freight Forwarder 1, used for invoice verification of the freight booking in Advanced Intercompany Sales and in Advanced Intercompany Stock Transfer. |
| Carrier | 17386402 | TM Freight Forwarder Self-Billing US | Freight Forwarder 2, used for self-billing (evaluated receipt settlement) of the freight booking in Advanced Intercompany Sales and in Advanced Intercompany Stock Transfer. |

### Additional Manual Configuration

Before you can test this scope item, you must have completed the additional configuration steps that are described in the Set-Up Instructions for this scope item. These configuration steps are specific for your implementation and include mandatory settings that are not delivered by SAP and must be created by you. For more information, follow the link to the document:

[Link to Set-Up Instructions](https://help.sap.com/docs/SAP_S4HANA_BEST_PRACTICES/e250ff8ba294f1993a9e60adac121f3d)

### Business Conditions

Before you can test this scope item, the following business conditions must be met.

| Scope Item ID | Business Condition |
| --- | --- |
| 6W3 - Transportation Execution | Complete scope item 6W3 Transportation Execution. |
| 22Z - Procurement of Services | To be able to execute the process step Create a Carrier Invoice for Freight Costs (Option A: Invoice Verification) the scope item 22Z - Procurement of Services must be activated and set up. |
| 2LH - Automated Invoice Settlement | To be able to execute the process step Self-billing for Freight Costs (Option B: Evaluate Receipt Settlement (ERS)) the scope item 2LH- Automated Invoice Settlement must be activated and set up. |
| 2EJ - Integration of Procurement with External Suppliers | To be able to execute the process step Review the Carrier Invoice for Freight Costs(Option C: Carrier Invoice Received via SOAP Message) the scope item 2EJ- Integration of Procurement with External Suppliers must be activated and set up. |

### Preliminary Steps

#### Automate Confirmation and Posting of Freight Costs (Optional)

Use

You can use a combination of carrier/service provider, procuring company code and purchasing organization to set-up the automation of the confirmation and the posting of freight costs. When a freight document matches the defined condition, the system automatically confirms and posts the freight costs for the freight document.

|  |
| --- |
| Note If you skip this step, proceed with the steps described in chapter Confirm Freight Cost for Accrual Postings. |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as a Configuration Expert - Business Process Configuration. | The SAP Fiori launchpad displays. |  |
| 2 | Access App | Open Manage Conditions (F5768). | The Manage Conditions (F5768) app opens. |  |
| 3 | Add new Condition | On the Manage Conditions screen, choose Create. |  |  |
| 4 | Add new Condition information | Enter the following information:Condition: <Condition Name>Description: <Description>Condition Type:/SCMTMS/TOR_FRC_CONF |  |  |
| 5 | Continue | Choose Continue. |  |  |
| 6 | Add Decision Table Entries | For a Decision Table, choose + (Insert new row) and create the following entries with option Direct Input Value:Carrier / service pro: <Carrier / service provider>Procuring Co. Code: 3310 or 1710Purchasing Org.: 3310 or 1710Autom. Cost Conf.: (X)Yes |  |  |
| 7 | Save Condition. | Choose Save. |  |  |

## Overview Table

This scope item consists of several process steps provided in the table below.

|  |
| --- |
| Note If your system administrator has enabled spaces and pages on the SAP Fiori launchpad, the homepage will only contain the essential apps for performing the typical tasks of a business role.You can find all other (searchable) apps not included on the homepage using the search bar ([2434549](https://me.sap.com/notes/2434549)).If you want to personalize the homepage and include the hidden apps, navigate to your user profile and choose App Finder. |

| Process Step | Business Role | App/Transaction | Expected Results |
| --- | --- | --- | --- |
| [Confirm Freight Costs for Accrual Postings](#unique_11) [page ] 10 | Transportation Buyer | Monitor Accrual Postings - Freight Documents (F4329) | Accruals are posted for the freight document. |
| [Monitor Freight Cost Allocation Documents](#unique_12) [page ] 15 | Transportation Buyer | Monitor Freight Cost Allocation Document Items (F5513) | Freight Cost Allocation document is reviewed. |
| [Carrier Settlement for Freight Orders and Freight Bookings](#unique_13) [page ] 17 |  |  |  |
| [Option A: Invoice Verification](#unique_14) [page ] 18 |  |  |  |
| [Create Supplier Invoice (Invoice Verification)](#unique_15) [page ] 18 | Accounts Payable Accountant - Procurement | Create Supplier Invoice - Advanced (MIRO) | The received carrier invoice is verified / posted. |
| [Variances in Carrier or Freight Forwarder Invoices (Optional)](#unique_16) [page ] 20 |  |  |  |
| [Variances Between Planned Charges and Charges Received From Carrier or Freight Forwarder Invoice](#unique_17) [page ] 20 | Accounts Payable Accountant - Procurement | Create Supplier Invoice - Advanced (MIRO) |  |
| [Variances Due to Additional Unplanned Freight Charges](#unique_18) [page ] 21 | Accounts Payable Accountant - Procurement | Create Supplier Invoice - Advanced (MIRO) |  |
| [Option B: Evaluated Receipt Settlement (ERS)](#unique_19) [page ] 23 |  |  |  |
| [Execute Evaluated Receipt Settlement](#unique_20) [page ] 24 | Accounts Payable Accountant | Schedule Supplier Invoice Jobs (F1683) | Evaluated receipt settlement is exececuted and a credit memo posted. |
| [Check Supplier Invoice - Generate Credit Memo](#unique_21) [page ] 25 | Accounts Payable Accountant | Supplier Invoices List (F1060A) | The Credit Memo is displayed and sent to the carrier. |
| [Option C: Carrier Invoice Received via SOAP Message](#unique_22) [page ] 26 | Accounts Payable Accountant | Supplier Invoices List (F1060A) |  |

## Test Procedures

This section describes the test procedures for each process step that belongs to this scope item.

### Confirm Freight Costs for Accrual Postings

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this process step the Transportation Buyer monitors the freight documents (freight orders or freight bookings) and posts accruals.

The Transportation Buyer reviews these freight documents prior to posting the freight cost accruals, to ensure that they correspond to the provided transportation services of the freight forwarder or carrier. This ensures a good data quality for the financial department.

The overall freight costs of the freight documents are allocated to the respective transportation requirements, for example sales order or delivery based on gross weight. On the Cost Distribution tab, it is shown how the freight costs are broken down by sales order item or delivery item reference.

As a final step, the freight document can be confirmed for accrual postings. The system automatically posts the freight costs to financial accounting as accruals and creates a freight cost allocation document, a service purchase order and a service entry sheet. Financial postings are created depending on the business scenario to either expenses for an outbound process or to material accounts for an inbound process.

|  |
| --- |
| Note If the automatic freight cost confirmation and posting is activated as described in chapter Automate Confirmation and Posting of Freight Costs (Optional), the freight order is automatically confirmed for accrual posting. Alternatively, the Transportation Buyer can confirm selected freight orders for accrual posting manually as described below.If you performed Confirm Freight Cost for Accruals Postings in 6W3, you can skip this process and proceed with Monitor Freight Cost Allocation Documents.You only need to perform this process once for each freight document. |

Procedure

Table 1:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1. | Log On | Log on to the SAP Fiori launchpad as a Transportation Buyer. | The SAP Fiori launchpad displays. |  |
| 2. | Access App | Open Monitor Accrual Postings (F4329). | The Monitor Accruals Postings screen appears. |  |
| 3. | Enter Selection Criteria | On the Monitor Accrual Postings screen, make the following entry:Purchasing Organization: 3310Freight Document: Optionally <Enter your freight order or freight booking number>Note Example:For advanced intercompany sales or advanced intercompany stock transfer in case of an ocean freight booking, enter company code 1710.For advanced intercompany sales or advanced intercompany stock transfer in case of the freight order on-carriage, enter company code 3310.For all other scenarios, use company code 3310. |  |  |
| 4. | Choose Go | Choose Go. | The freight documents are displayed in the Monitor Accrual Postings table. |  |
| 5. | Navigate to the For Confirmation Tab | Navigate to the For Confirmation tab. | The freight documents for confirmation are displayed in the Monitor Accrual Postings table. |  |
| 6. | Freight Order / Freight Booking Details | Select the freight document row in the Monitor Accruals Posting table. | The Road Freight Order <your freight order number> - Process Accruals screen appears.orThe Rail Freight Order <your freight order number> - Process Accruals screen appears.orThe Ocean Freight Booking <your freight booking number> - Process Accruals screen appears.orThe Air Freight Booking <your freight booking number> - Process Accruals screen appears. |  |
| 7. | Display General Data (Optional) | Navigate to the General Data tab to review the header information. |  |  |
| 8. | Display Charges (Optional) | Scroll down to the Charges section to review the detailed information. | The charge item for the carrier or freight forwarder is displayed. |  |
| 9. | Display Charges (Optional) | In the Charge Hierarchy expand the node TM Carrier | The charge lines are displayed. |  |
| 10. | Display Charges Details (Optional) | Choose Show/Hide Details.Note Make sure that only one line is selected | The charge line details are displayed. |  |
| 11. | Display Stages (Optional) | Navigate to the Stages tab to review the stage details. |  |  |
| 12. | Display Business Partners (Optional) | Navigate to the Business Partner tab to review the parties involved. |  |  |
| 13. | Display Cost Distribution (Optional) | Navigate to the Cost Distribution tab to review the parties involved. | In the Distribution Hierarchy table it is shown how the freight costs are broken down by a sales order item or delivery item reference. |  |
| 14. | Confirm Freight Order or Confirm Freight Booking | Choose Confirm for Posting. | The following system message appears: Freight document <your freight order or freight booking> for <Your carrier or freight forwarder> confirmed for postingNote After confirming the freight order or freight booking for accruals posting, a service purchase order and a service entry sheet is created automatically in a background process. These documents are the basis for the invoice verification.Additionally, freight cost allocation documents (except for scope item BMY - Subcontracting purchase order with TM integration) are created as follows:Freight Cost Allocation (Expense) in all the legal ledgers for outbound transportation scenario (sell from stock, customer consignment fill-up/pickup, freight costs in the delivering company for ICO stock transport order and ICO intercompany sales process)Freight Cost Allocation (ML-Account) in all legal ledgers for inbound transportation scenario (procurement of material, inbound transport costs related to the ICO Stock transport order by the receiving company)If group valuation is activated, in case of ICO STO, the freight costs in the delivering company, Freight Cost Allocation (ML-Account), are posted in the group valuation ledger.For scope item BMY – Subcontracting purchase order with TM integration, freight cost allocation documents are created as follows:Freight Cost Allocation (ML-Account) in all the legal ledgers for outbound transportation scenario is only created when the goods receipt is performed for the inbound delivery of subcontracting purchase order. In case the confirming of freight document is done after goods receipt, the freight cost allocation (ML-Account) in all legal is created during confirming the freight document itself as done during usual freight cost confirming process.Freight Cost Allocation (ML-Account) in all legal ledgers for inbound transportation scenario.To see the details of the freight cost allocation document, follow the steps mentioned in the Monitor Freight Cost Allocation documents. |  |
| 15. | Navigate Back | Navigate back |  |  |

|  |
| --- |
| Note To confirm multiple freight documents simultaneously, choose multiple freight document checkboxes on the Monitor Accrual Postings overview page (under the For Confirmation tab) and choose Confirm for Posting. |

In case the posting result is an error, follow the steps below to check the error details and repost.

If, for example, the posting date is in a closed period, the posting date needs to be changed prior to posting of the freight document. You need to scroll down to the Charges section, navigate to the Posting Date tab, and change the accrual posting date in column Posting Date.

Table 2:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Access App | Open Monitor Accrual Postings - Freight Documents (F4329). | The Monitor Accruals Postings screen appears. |  |
| 2 | Enter Selection Criteria | On the Monitor Accrual Postings screen, make the following entry:Purchasing Organization: 3310Freight Document: Optionally <Enter your freight order or freight booking number>Note Example:For advanced intercompany sales or advanced intercompany stock transfer in case of an ocean freight booking, enter company code 1710.For advanced intercompany sales or advanced intercompany stock transfer in case of the freight order on-carriage, enter company code 3310.For all other scenarios, use company code 3310. |  |  |
| 3 | Choose Go | Choose Go. | The freight documents are displayed in the Monitor Accrual Posting table. |  |
| 4 | Navigate to the Errors Tab | Navigate to the Errors tab | The freight documents with errors are displayed in the Monitor Accrual Postings table. |  |
| 5 | Show the Error Description | Navigate to the corresponding line and choose Show Errors. | The Application Log appears, containing a detailed description of the errors. |  |
| 6 | Show the Error Details | Select the error details by selecting the error link in the Description column. | The message details are shown containing a diagnosis and guidance on possible solutions. |  |
| 7 | Correct the Errors | Correct the errors according to the message details. |  |  |
| 8 | Select the Freight Order or Freight Booking in the Freight Document Table | Select the Freight Document checkbox. |  |  |
| 9 | Post Accruals | Choose Post. | The following system message appears: Freight document <your freight order or freight booking> for <Your carrier or freight forwarder> confirmed for postingNote After confirming the freight order or freight booking for accruals posting, a service purchase order and a service entry sheet is created automatically in a background process. These documents are the basis for the invoice verification.Additionally, freight cost allocation documents (except for scope item BMY - Subcontracting purchase order with TM integration) are created as follows:Freight Cost Allocation (Expense) in all the legal ledgers for outbound transportation scenario (sell from stock, customer consignment fill-up/pickup, freight costs in the delivering company for ICO stock transport order and ICO intercompany sales process)Freight Cost Allocation (ML-Account) in all legal ledgers for inbound transportation scenario (procurement of material, inbound transport costs related to the ICO Stock transport order by the receiving company)If group valuation is activated, in case of ICO STO, the freight costs in the delivering company, Freight Cost Allocation (ML-Account), are posted in the group valuation ledger.For scope item BMY – Subcontracting purchase order with TM integration, freight cost allocation documents are created as follows:Freight Cost Allocation (ML-Account) in all the legal ledgers for outbound transportation scenario is only created when the goods receipt is performed for the inbound delivery of subcontracting purchase order. In case the confirming of freight document is done after goods receipt the freight cost allocation (ML-Account) in all legal is created during confirming, the freight document itself as done during usual freight cost con-firming process.Freight Cost Allocation (ML-Account) in all legal ledgers for inbound transportation scenario.To see the details of the freight cost allocation document, follow the steps mentioned in the Monitor Freight Cost Allocation documents. |  |

### Monitor Freight Cost Allocation Documents

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this process step the Transportation Buyer reviews the freight cost allocation documents which are created during accrual posting, to ensure that they are successfully posted to accounting.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Transportation Buyer. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Monitor Freight Cost Allocation Document Items (F5513). | The Monitor Freight Cost Allocation Document Items (F5513) screen displays. |  |
| 3 | Adapt Filters | On the Monitor Freight Cost Allocation Document Items screen, make the following entries:Display Currency: <currency>Note Example:Freight Order <your freight order number> orFreight Booking: <your freight booking number> |  |  |
| 4 | Choose Go | Choose Go. | The freight cost allocation document is displayed in table Freight Cost Allocation Document Items. |  |
| 5 | Display Details for the Freight Cost Allocation Document | In table Freight Cost Allocation Document Items choose <freight cost allocation document number> Manage Freight Cost Allocation Documents. | Depending on the selected Freight Cost Allocation Document, the Freight Cost Allocation (Expense) or the Freight Cost Allocation (ML-Account) screen appears.Among others, following details are displayed:Posting Status: Accounting document has been created (C)Posting Date: <Posting Date in your freight document>Company code: <company code of your freight document>Net Amount: <Net Amount>Settlement Document Type: Freight Cost Allocation (Expense) or Freight Cost allocation (ML-Account)In table Freight Cost Allocation Document Items, the system displays the products that were shipped in the freight document and the allocated freight costs per product in the Gross Amount of Item column which is equal to the amount shown in the Cost Distribution tab of the respective freight document in the App Monitor Accrual Postings. |  |
| 6 | Display Item Details | In table Freight Cost Allocation Document Items, choose the entry with the product to display item details. | Among others, following details are displayed:Settlement information, Accounting information such as, Profitability Segment, Profit Center,Reference Document Information (such as the freight order or freight booking number, sales order and item, intercompany sales order number and outbound delivery number and item or the purchase order and item, inbound delivery and item)Plant:<plant from the inbound or outbound delivery item>. |  |

|  |
| --- |
| Note In case of errors in the release of the Freight Cost Allocation Documents to Accounting, you find these Freight Cost Allocation Documents in the Not Released Documents, which must be released after detailed evaluation of the errors. To evaluate the specific error in the Freight Cost Allocation Document, go to the Freight Cost Allocation Document in Error and choose Account Assignment action. |

### Carrier Settlement for Freight Orders and Freight Bookings

Purpose

In this process step the invoice received from the carrier or freight forwarder is verified against the costs calculated in the freight document (freight order or freight booking) as described in option A (use for example 33386001, 33386201, 33386401 or 17386401).

For carriers or freight forwarders that agreed to automated invoice settlement, you use the Evaluated Receipt Settlement (ERS) scenario. A credit memo can be issued as described in option B (use for example 33386002, 33386202 or 33386402).

For carrier or freight forwarder who send invoice using SOAP message (EDI for example) for the freight document. As described in option C (use for example 33386001, 33386201 or 33386401).

#### Option A: Invoice Verification

Purpose

As soon as the invoice of the carrier or freight forwarder is received, the Accounts Payable Accountant can post it with reference to the freight document. The expected freight costs calculated in the freight document are compared with the amounts of the carrier or freight forwarder invoice. Invoices with variances in charges can also be processed and posted

After the carrier invoice is posted, the posting status of the freight document is set to Invoice Verified, the lifecycle status is set to Completed.

##### Create Supplier Invoice (Invoice Verification)

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
| 1 | Log on | Log on to the SAP Fiori launchpad as an Accounts Payable Accountant. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the App | Open Create Supplier Invoice - Advanced (MIRO). | The Create Supplier Invoice screen is displayed. |  |
| 3 | Enter Company Code | On the dialog box Enter Company Code enter the Company Code: 3310Note The dialog box only appears the first time you launch the app. Afterwards you can change the Company Code by choosing Edit > Switch Company CodeNote Example: For advanced intercompany sales or advanced intercompany stock transfer in case of an ocean freight booking, enter company code 1710.For advanced intercompany sales or advanced intercompany stock transfer in case of the freight order on-carriage, enter company code 3310.For all other scenarios, use company code 3310. |  |  |
| 4 | Enter General Data | On the Enter Incoming Invoice: Company Code 3310 screen make the following entries:Transaction : InvoiceGo to the Basic Data area:Invoice date: <Today>Posting Date: <Today>Reference: <Fill the supplier Invoice Number> |  |  |
| 5 | Enter Purchase Order Reference | Go to the PO Reference area and make the following entries:Reference Document Category: Freight OrderFreight Order: Freight Order Number or Freight Booking NumberChoose Enter |  |  |
| 6 | Check Invoice Items | In the PO Reference tab, section Items, check the Amount, Quantity and Tax Code. |  |  |
| 7 | Enter Invoice Amount | Go to the Basic Data area and select the Calculate Tax checkbox.Make the following entry:Amount: <Total amount in PO including Tax> |  |  |
| 8 | Post Invoice | Choose Post. | Once the carrier or freight forwarder invoice is created, the posting status in the freight document changes from Posted to Invoice Verified. |  |

When the invoice is posted with amounts which deviate from the expected value, the following system message appears: Price too high (tolerance limit of XXX exceeded)). Depending on the variance type, proceed as indicated in the section Variances in Carrier or Freight Forwarder Invoices (Optional).

You can check the posting status by using any of the following apps:

Monitor Accrual Postings - Freight Documents (F4329), or Manage Ocean Freight Bookings (F6213), or Manage Air Freight Bookings (F6535). In case the execution status is already Executed, the Life Cycle Status of the freight document is set to Completed.

##### Variances in Carrier or Freight Forwarder Invoices (Optional)

###### Variances Between Planned Charges and Charges Received From Carrier or Freight Forwarder Invoice

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
| 1 | Log on | Log on to the SAP Fiori launchpad as an Accounts Payable Accountant - Procurement. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the App | Open Create Supplier Invoice - Advanced (MIRO). | The Create Supplier Invoice screen is displayed. |  |
| 3 | Enter Company Code | On the dialog box Enter Company Code enter the Company Code: 3310.Note The dialog box only appears the first time you launch the app. Afterwards you can change the Company Code by choosing Edit > Switch Company CodeNote Example:For advanced intercompany sales or advanced inter-company stock transfer in case of an ocean freight booking, enter company code 1710.For advanced intercompany sales or advanced inter-company stock transfer in case of the freight order on-carriage, enter company code 3310.For all other scenarios, use company code 3310. |  |  |
| 4 | Enter General Data | On the Enter Incoming Invoice: Company Code 3310 make the following entries:Transaction : InvoiceGo to the Basic Data area:Invoice Date: <Today>Posting Date: <Today>Reference: <Fill the supplier Invoice Number> |  |  |
| 5 | Enter Purchase Order Reference | Go to the PO Reference area:Reference Document Category: Freight OrderFreight Order: Freight Order Number or Freight Booking NumberChoose Enter |  |  |
| 6 | Adjust the Invoice Items | In the PO Reference tab section Items, enter the Amount:<Variance Amount> and check the, Quantity and Tax Code.Verify that the Tax code determined in the invoice header is the same Tax code as in the invoice items proposed by the system. |  |  |
| 7 | Enter Invoice Amount | Go to the Basic Data area and enter:Amount: <Total amount in PO including Tax> |  |  |
| 8 | Post Invoice | Choose Post. | Once the carrier or freight forwarder invoice is created, the posting status in the freight document changes from Posted to Invoice Verified. |  |

###### Variances Due to Additional Unplanned Freight Charges

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
|  | Log on | Log on to the Fiori launchpad as an Accounts Payable Accountant - Procurement. | The SAP Fiori launchpad is displayed. |  |
|  | Access the App | Open Create Supplier Invoice - Advanced (MIRO). | The Create Supplier Invoice screen is displayed. |  |
|  | Enter Company Code | On the dialog box Enter Company Code enter the Company Code: 3310Note The dialog box only appears the first time you launch the app. Afterwards you can change the Company Code by choosing Edit > Switch Company CodeNote Example: For advanced intercompany sales or advanced intercompany stock transfer in case of an ocean freight booking, enter company code 1710.For advanced intercompany sales or advanced intercompany stock transfer in case of the freight order on-carriage, enter company code 3310.For all other scenarios, use company code 3310. |  |  |
|  | Enter General Data | On the Enter Incoming Invoice: Company Code 3310 make the following entries:Transaction : InvoiceGo to the Basic Data area:Invoice Date: <Today>Posting Date: <Today>Reference: <Fill the supplier Invoice Number> |  |  |
|  | Enter Purchase Order Reference | Go to the PO Reference area:Reference Document Category: Freight OrderFreight Order: Freight Order Number or Freight Booking NumberChoose Enter |  |  |
|  | Add unplanned Invoice Items | In the PO Reference tab section Items, displays the planned charges, to add unplanned charges,Navigate to the G/L Account tab and a new item for each unplanned freight charge. Enter the Charge Type: <Charge Type for the unplanned charge received>Freight Order: <Freight Order> or <Freight Booking Number>Amount in doc.curr: <Amount>and check the Item Tax Code.Verify that the Tax code determined in the invoice header is the same Tax code as in the invoice items proposed by the system. |  |  |
|  | Enter Invoice Amount | Go to the Basic Data area and enter:Amount: <Total amount in PO including Tax> |  |  |
|  | Post Invoice | Choose Post. | Once the carrier or freight forwarder invoice is created, the posting status in the freight document changes from Posted to Invoice Verified. |  |

When the invoice is posted, the price variance creates a new Freight Cost Allocation Document (except for scope item BMY - Subcontracting purchase order with TM integration) for the amount equal to the price variances that have been distributed to the delivered items in the freight document.

For scope item BMY - Subcontracting purchase order with TM integration, the price variance for outbound transport will NOT create a new Freight Cost Allocation Document provided the goods receipt is still not performed. In this case the freight cost allocation for variance amount will be considered during the goods receipt of the inbound delivery of the subcontracting purchase order. For the scenario where the variance amount for outbound transport in invoice is posted after the goods receipt, freight cost allocation document for the price variance will be created as usual.

To monitor the Freight Cost Allocation Documents, proceed as indicated in the section Monitor Freight Allocation Documents, using the following entries in the Adapt Filters dialog box:

Display Currency: <currency>

Freight Order <your freight order number> or Freight Booking:<your freight booking number>

Adjustment Category <Is an Adjustment Document (1)>

The new document is shown as an entry in the Freight Cost Allocation Document Items table.

The variance document can be identified in Adjustment Category field on the General Information tab, as an Adjustment Document (1). Additionally on the Document Flow tab, the Incoming Invoice document indicates the source of the new Freight Cost Allocation Document.

#### Option B: Evaluated Receipt Settlement (ERS)

Purpose

For carriers and freight forwarders that agreed to the automated invoice settlement, the Evaluated Receipt Settlement (ERS) scenario is used. Instead of receiving an invoice from the carrier or freight forwarder a credit memo is submitted and sent to this business partners.

##### Execute Evaluated Receipt Settlement

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this process the Evaluated Receipt Settlement (ERS) is executed for carriers and freight forwarders that agreed to the automated invoice settlement. A job is scheduled to post the appropriated supplier invoices (credit memos). A detailed log can be displayed with the document numbers created.

The scenario can also be used periodically.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Open the SAP Fiori launchpad as an Accounts Payable Accountant - Procurement. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the App | Open Schedule Supplier Invoice Jobs (F1683). | The Application Jobs screen is displayed. |  |
| 3 | Create Application Job | Choose Create. | The New Job screen is displayed. |  |
| 4 | Execute ERS | Make the following entries:For Step 1, in the Template Selection section, from the drop-down box of Job Template, choose Evaluated Receipt Settlement (ERS).Then choose Step 2, in the Scheduling Options section, make sure that Start Immediately checkbox is checked. Or you can also set the start date and start time.Then choose Step 3, in the Parameters section, make the following entries:Company Code: 3310 or 1710Plant: 3310 or 1710Purchasing Document: <enter your procurement document>Note To determine your procurement document, select the value help.In the dialog box, choose the drop-down list for Select Search View and then choose Service Purchasing Documents per Freight Order.In field Freight Order make the following entries::<enter your freight order number> or <enter your freight booking number>.Choose OK.Select your freight document.Choose OK.Document Selection: <1 - Document Selection per Supplier>.Transportation Management: Select the checkbox.Test Run: Select the checkbox.Choose Check. | The system message displays: You can go ahead and schedule the job. |  |
| 5 | Schedule the Job without Test Run | Uncheck Test Run, and then choose Schedule. |  |  |
| 6 | Check the Result | In the Application Jobs screen, find the job you created. You may need to wait several minutes to see the results after the job status becomes finished.Choose Results. | The detailed log is displayed in the Document (ID, XXXXX) screen. You can find the corresponding document number and FI document number created. |  |

##### Check Supplier Invoice - Generate Credit Memo

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step the created credit memos can be reviewed in a supplier invoice list.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Open the Fiori Launchpad tile | Open the SAP Fiori launchpad as an Accounts Payable Accountant | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the App | Open Supplier Invoices List (F1060A) | The Supplier Invoices List screen is displayed. |  |
| 3 | Search for the document | On the Supplier Invoices List screen, enter the following values:Invoicing Party : <your carrier or freight forwarder id from the freight order or freight booking> (for example 33386001)Company Code: 3310Then choose Go. | The invoices list is displayed. |  |
| 4 | Go to the Invoice Detailed Page | Choose the invoice you created, whose Entry Type is ERS | The screen navigates to the Supplier Invoice detailed page. |  |
| 5 | Display the Document | On the Supplier Invoice screen, go to the Output tab. On the Output Details table, find the line with the output type EVALUATED_RECEIPT_SETTLEMENT. Choose Display Document in the Display column. | The document (in this case, Credit Memo) is displayed. |  |
| 6 | Download the Document | Download the document. | The document is downloaded to your local workspace. |  |
| 7 | Send Documents to Supplier | Send the downloaded document to the supplier as printed document, or by fax, e-mail or via the Internet.The step is executed offline. | The document is sent to the supplier. |  |

#### Option C: Carrier Invoice Received via SOAP Message

Purpose

For carriers or freight forwarders who agreed to send the invoices via SOAP message, you can monitor the invoices. The following steps explain how you can review the supplier invoices. They can be processed only after the corresponding supplier system has sent an invoice using B2B communication.

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
| 1 | Log On | Log on to the SAP Fiori launchpad using the Accounts Payable Accountant role. | The SAP Fiori launchpad displays. | The SAP Fiori launchpad displays. |
| 2 | Access App | Choose Supplier Invoices List (F1060A). | The Supplier Invoices List screen appears. |  |
| 3 | Enter Selection Criteria | On the Supplier Invoice List screen, make the following entry:Invoicing Party: 33386001 or 33386201, or 33386401Entry Type: SOA B2BNote To enable the additional search fields, choose Adapt Filters, search for the field, and mark it. Then choose OK. |  |  |
| 4 | Choose Go | Choose Go. | The invoices are displayed in the Invoices table. |  |
| 5 | Select the Item | Select the item with the invoice number. | The Supplier Invoice screen appears. |  |
| 6 | Review the Invoice | Review the invoice. |  |  |
| 7 | Go Back | Go back. |  |  |

## Appendix

### Process Integration

The process to be tested in this test script is part of a chain of integrated processes.

#### Preceding Processes

The following processes and conditions can proceed this process.

| Process | Business Condition |
| --- | --- |
| 6W3 - Transportation Execution | Execution Status (Source) Set to Checked Out |

#### Succeeding Processes

After completing the the Carrier Settlement for Freight Orders and Freight Bookings process step in this test script, you can continue testing the following business processes:

| Process | Business Condition |
| --- | --- |
| BD9 Sell from Stock | Continue with step Create Billing Document.Note The transportation costs are now part of the billing document and can be invoiced to the customer. Details can be checked in the Pricing Elements section while creating the billing document. Locate the condition type, which lists the freights costs. The amount shown there should be equal to the respective amount in the freight booking. (Use the Monitor Accrual Postings - Freight Documents (F4329) app and choose the Cost Distribution tab.) |
| 3NR Sales Scheduling Agreements | Continue with step Create Billing Document. |
| 3BS Warehouse Outbound Processing | Continue with step Create Billing Document. |
| 2TX Direct Procurement with Inbound Delivery | Perform all process steps starting from Confirm Quantities for Putaway. |
| BDD Lean Customer Returns | Perform all process steps starting from Post Goods Receipt. |
| 5D2 Advanced Intercompany Sales | Perform all process steps starting from Create Intercompany Invoice. |
| 5HP Advanced Intercompany Stock Transfer | Perform all process steps starting from Confirm Quantities for Inbound Delivery. |
| BME Stock Transfer with Delivery | Perform all process steps starting from |
| BMY Subcontracting | Perform all process steps starting from . |
| 1IU Customer Consignment | Customer Consignment Fill-UpContinue with the Consignment Issue.Customer Consignment Pick-UpPerform all process steps starting from Receive Returned Goods using the Shipping Point 1710. |

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
- see-also :: [[11-inventory-warehouse-and-transportation/stammdatenskript-lieferplan-anlegen-sds-3tl-sap-s-4hana-cloud-public-e]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/6W4_S4CLD2608_BPD_EN_AE.docx` — full document · extracted with `mammoth` · 54,485 chars in the whole document
