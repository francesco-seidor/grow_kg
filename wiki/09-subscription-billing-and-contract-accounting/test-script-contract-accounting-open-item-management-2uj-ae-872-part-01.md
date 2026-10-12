---
id: 09-subscription-billing-and-contract-accounting/test-script-contract-accounting-open-item-management-2uj-ae-872-part-01
title: "Test Script: Contract Accounting – Open Item Management (2UJ_AE) (2UJ_S4CLD2608_BPD_EN_AE) — part 1 of 2"
description: "S/4HANA Cloud test script, Contract Accounting Open Item Management (2UJ_AE): dunning, installment plans, interest, credits, deposits, disputes, collections."
cluster: 09-subscription-billing-and-contract-accounting
tags: [kb/subscription-billing-and-contract-accounting, topic/fi-ca-open-item-management]
aliases: []
keywords: [Contract Accounting Open Item Management and Collections, contract accounting, dunning, installment plans, flexible workflow, interest calculation, interest calculation on clearing, credit clarification, creditworthiness, security deposit]
sources: ["raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/2UJ_S4CLD2608_BPD_EN_AE.docx#lines-1-3545"]
confidence: high
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-872
topic: 09-subscription-billing-and-contract-accounting/fi-ca-open-item-management
language: EN
part: 1/2
created: 2026-10-12
updated: 2026-10-12
---

# Test Script: Contract Accounting – Open Item Management (2UJ_AE) (2UJ_S4CLD2608_BPD_EN_AE) — part 1 of 2

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/2UJ_S4CLD2608_BPD_EN_AE.docx`, part 1 of 2 (lines 1–3545 of the extracted text), extracted with `mammoth`. Grouped under **Contract Accounting Open Item Management and Collections** in Subscription Billing and Contract Accounting. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

| <!-- image omitted: unnamed --> | Test ScriptSAP S/4HANA Cloud Public Edition - 19-06-26 |
| --- | --- |
|  | Contract Accounting – Open Item Management (2UJ_AE) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Table of Contents

[1 Purpose 6](#_Toc232850450)

[2 Prerequisites 8](#_Toc232850451)

[2.1 Additional Manual Configuration 8](#_Toc232850452)

[2.2 System Access 8](#_Toc232850453)

[2.3 Roles 8](#_Toc232850454)

[2.4 Master Data, Organizational Data, and Other Data 10](#_Toc232850455)

[2.5 Business Conditions 11](#_Toc232850456)

[2.6 Preliminary Steps 12](#_Toc232850457)

[2.6.1 Post Documents 12](#_Toc232850458)

[2.6.2 Maintain Contract Account 15](#_Toc232850459)

[3 Overview Table 17](#_Toc232850460)

[4 Test Procedures 26](#_Toc232850461)

[4.1 Account Maintenance 26](#_Toc232850462)

[4.1.1 Account Maintenance: Process Open Items 26](#_Toc232850463)

[4.2 Dunning 27](#_Toc232850464)

[4.2.1 Execute Dunning Proposal Run 29](#_Toc232850465)

[4.2.2 Delete Dunning Proposal Run 30](#_Toc232850466)

[4.2.3 Execute Dunning Activity Run 32](#_Toc232850467)

[4.2.4 Print Dunning Notices 33](#_Toc232850468)

[4.2.4.1 Print Correspondence 33](#_Toc232850469)

[4.2.4.2 Display Correspondence History 35](#_Toc232850470)

[4.2.5 Display Dunning History 35](#_Toc232850471)

[4.2.6 Maintain Dunning Notice 36](#_Toc232850472)

[4.2.7 Valuate Success of Dunning 37](#_Toc232850473)

[4.2.8 Dunning Exceptions 41](#_Toc232850474)

[4.2.8.1 Display Dunning Exception List 41](#_Toc232850475)

[4.2.8.2 Delete Dunning Exception 42](#_Toc232850476)

[4.3 Installment Plans 43](#_Toc232850477)

[4.3.1 Create Installment Plan 43](#_Toc232850478)

[4.3.2 Print Installment Plan 45](#_Toc232850479)

[4.3.2.1 Print Correspondence 45](#_Toc232850480)

[4.3.2.2 Display Correspondence History 46](#_Toc232850481)

[4.3.3 Display Installment Plan History 47](#_Toc232850482)

[4.3.4 Change Installment Plan 48](#_Toc232850483)

[4.3.5 Display Installment Plan 48](#_Toc232850484)

[4.3.6 Automatic Interest Run for Installment Plan 49](#_Toc232850485)

[4.4 Flexible Workflow for Installment Plan Creation (Optional) 52](#_Toc232850486)

[4.4.1 Post Installment Plan 59](#_Toc232850487)

[4.4.2 Verify Installment Plan Document 60](#_Toc232850488)

[4.4.3 Approve Installment Plan Document (for Processor - Inbox) 61](#_Toc232850489)

[4.4.4 Reject Installmen Plan Document (for Processor - Inbox) 62](#_Toc232850490)

[4.4.5 Deactivate a Rejected Installment Plan Document (Requester) 63](#_Toc232850491)

[4.4.6 Resend a Rejected Installment Plan Document (Requester) 64](#_Toc232850492)

[4.5 Interest Calculation 65](#_Toc232850493)

[4.5.1 Post Interest 65](#_Toc232850494)

[4.5.2 Print Interest Notification 67](#_Toc232850495)

[4.5.2.1 Print Correspondence 67](#_Toc232850496)

[4.5.2.2 Display Correspondence History 69](#_Toc232850497)

[4.5.3 Display Interest Calculation 69](#_Toc232850498)

[4.5.4 Execute Interest Run 70](#_Toc232850499)

[4.6 Interest Calculation on Clearing 72](#_Toc232850500)

[4.6.1 Interest Calculation on Clearing 72](#_Toc232850501)

[4.6.2 Display Interest Supplement 75](#_Toc232850502)

[4.7 Credit Clarification 76](#_Toc232850503)

[4.7.1 Create Credit List 76](#_Toc232850504)

[4.7.2 Clarify Credits 79](#_Toc232850505)

[4.7.3 Process Credits 80](#_Toc232850506)

[4.7.3.1 Transfer Credits 81](#_Toc232850507)

[4.7.3.2 Pay Out Credits 82](#_Toc232850508)

[4.7.3.3 Clear Credits with Open Items 83](#_Toc232850509)

[4.8 Creditworthiness 84](#_Toc232850510)

[4.8.1 Display Creditworthiness 84](#_Toc232850511)

[4.9 Security Deposit 89](#_Toc232850512)

[4.9.1 Create Cash Deposit Request 89](#_Toc232850513)

[4.9.2 Print Security Deposit 91](#_Toc232850514)

[4.9.2.1 Print Correspondence 91](#_Toc232850515)

[4.9.2.2 Display Correspondence 92](#_Toc232850516)

[4.9.3 Receive Cash Security Deposit Payment 93](#_Toc232850517)

[4.9.4 Release Security Deposit 96](#_Toc232850518)

[4.9.5 Return Security Deposit 96](#_Toc232850519)

[4.9.6 Cash Security Deposit Interest Calculation (Optional) 99](#_Toc232850520)

[4.10 Transfer Business Partner Items 100](#_Toc232850521)

[4.10.1 Transfer Business Partner Items 100](#_Toc232850522)

[4.11 Dispute Case Management 109](#_Toc232850523)

[4.11.1 Incorrect Invoice Processing 112](#_Toc232850524)

[4.11.1.1 Create a Dispute Case of Incorrect Invoice 112](#_Toc232850525)

[4.11.1.2 Modify the Dispute Case Status 114](#_Toc232850526)

[4.11.1.3 Process the Incorrect Invoice Dispute Case 115](#_Toc232850527)

[4.11.1.4 Close the Dispute Case 117](#_Toc232850528)

[4.11.2 Missing Payment Processing 119](#_Toc232850529)

[4.11.2.1 Create a Dispute Case of Missing Payment 119](#_Toc232850530)

[4.11.2.2 Modify the Dispute Case Status 120](#_Toc232850531)

[4.11.2.3 Reset Payment Assignment 121](#_Toc232850532)

[4.11.2.4 Assign Payments to Dispute Case (Optional) 122](#_Toc232850533)

[4.11.2.5 Close the Dispute Case 123](#_Toc232850534)

[4.11.3 Send Email (Optional) 124](#_Toc232850535)

[4.12 Disconnection and Reconnection 126](#_Toc232850536)

[4.12.1 Create Disconnection Request 126](#_Toc232850537)

[4.12.1.1 Execute Dunning Proposal Run 127](#_Toc232850538)

[4.12.1.2 Execute Dunning Activity Run 129](#_Toc232850539)

[4.12.2 Send Disconnection and Reconnection Requests 129](#_Toc232850540)

[4.12.3 Payment Lot Processing 131](#_Toc232850541)

[4.12.4 Create Reconnection Requests 133](#_Toc232850542)

[4.12.5 Send Disconnection and Reconnection Requests 134](#_Toc232850543)

[4.12.6 Monitor Disconnection Requests 135](#_Toc232850544)

[4.13 Collection Agency 136](#_Toc232850545)

[4.13.1 Post Documents 136](#_Toc232850546)

[4.13.2 Release to Collection Agency 136](#_Toc232850547)

[4.13.2.1 Automatic Release to Collection Agency (Optional) 137](#_Toc232850548)

[4.13.3 Submit to Collection Agency 140](#_Toc232850549)

[4.13.3.1 Automatic Recall Receivables from Collection Agency during Dunning (Optional) 141](#_Toc232850550)

[4.13.4 Post Collection Agency Information via Inbound Service 144](#_Toc232850551)

[4.13.5 Process Information from Collection Agency 147](#_Toc232850552)

[4.13.6 Post Receivables for Collection Agency 148](#_Toc232850553)

[4.13.7 Monitor Collection Services 149](#_Toc232850554)

[4.13.8 Display History of Collection Items 150](#_Toc232850555)

[4.13.9 Create List of Collection Items 151](#_Toc232850556)

[4.14 Integration with Credit Management 152](#_Toc232850557)

[4.14.1 Transfer Credit Data 152](#_Toc232850558)

[4.14.2 Replicate Creditworthiness 154](#_Toc232850559)

[4.14.3 Compare Credit Score 155](#_Toc232850560)

[4.14.4 Prepare Master Data Change from External System 157](#_Toc232850561)

[4.14.5 Process Master Data Change from External System 159](#_Toc232850562)

[4.15 Factoring 161](#_Toc232850563)

[4.15.1 Post Documents 161](#_Toc232850564)

[4.15.2 Offer Receivables for Sale 161](#_Toc232850565)

[4.15.2.1 Reverse Offer 163](#_Toc232850566)

[4.15.3 Receive the Response of the Factor 164](#_Toc232850567)

[4.15.4 Process the Response of the Factor 166](#_Toc232850568)

[4.15.5 Buy Back Receivables from Factor (Optional) 167](#_Toc232850569)

[4.15.5.1 Receive the Response of the Factor 169](#_Toc232850570)

[4.15.6 Send Update to Factor 170](#_Toc232850571)

[4.15.7 Monitor Factoring Services 172](#_Toc232850572)

[4.15.7.1 Create Answer of Offering Receivables Manually 173](#_Toc232850573)

[4.15.8 Reset Excepted Receivables 174](#_Toc232850574)

[4.16 Promise to Pay 175](#_Toc232850575)

[4.16.1 Create Promise to Pay 175](#_Toc232850576)

[4.16.2 Create Promise to Pay for Direct Debit (Optional) 177](#_Toc232850577)

[4.16.3 Create Promise to Pay with Credit Card (Optional) 179](#_Toc232850578)

[4.16.4 Display Promise to Pay 182](#_Toc232850579)

[4.16.5 Print Promise to Pay 184](#_Toc232850580)

[4.16.6 Replace Promise to Pay (Optional) 185](#_Toc232850581)

[4.16.7 Payment for Promise to Pay 187](#_Toc232850582)

[4.16.7.1 Manual Payment by Payment Lot 187](#_Toc232850583)

[4.16.7.1.1 Create Payment Lot 187](#_Toc232850584)

[4.16.7.1.2 Post Payment Lot 189](#_Toc232850585)

[4.16.7.2 Payment Run Execution (Optional) 190](#_Toc232850586)

[4.16.8 Mass Valuation Run 193](#_Toc232850587)

[4.16.9 Withdraw Promise to Pay 195](#_Toc232850588)

[4.17 Handling of Service Provider Bills in Deregulated Market 196](#_Toc232850589)

[4.17.1 Post Documents 198](#_Toc232850590)

[4.17.2 Change Document 198](#_Toc232850591)

[4.17.3 Execute Payment Run 199](#_Toc232850592)

[4.17.4 Check Information Container Creation 201](#_Toc232850593)

[4.17.5 Send Data from Information Container 202](#_Toc232850594)

[4.17.6 Check the Send Status of Information Container 204](#_Toc232850595)

[4.17.7 Reset the Send Status of Information Container 204](#_Toc232850596)

[4.18 Transfer Business Partner Postings to External Systems 205](#_Toc232850597)

[4.18.1 Transfer Business Partner Postings to External Systems 213](#_Toc232850598)

[4.18.2 Monitor Status Tranferred to External Systems 214](#_Toc232850599)

[4.18.3 Delete Trigger Data for Data Transfer to External Systems (Optional) 215](#_Toc232850600)

[4.19 Transfer Documents to Accounts Payable/Accounts Receivable 217](#_Toc232850601)

[4.19.1 Post Document 218](#_Toc232850602)

[4.19.2 Transfer Documents to Accounts Payable/Accounts Receivable 220](#_Toc232850603)

[4.19.3 Display Document 221](#_Toc232850604)

[4.19.4 Reverse Document (Optional) 222](#_Toc232850605)

[5 Appendix 224](#_Toc232850606)

[5.1 Process Integration 224](#_Toc232850607)

[5.1.1 Reset Cleared Items 224](#_Toc232850608)

[5.1.2 Reverse of Dunning Notice 224](#_Toc232850609)

[5.1.3 Change Creditworthiness 226](#_Toc232850610)

[5.1.4 Dunning by Collection Strategy 226](#_Toc232850611)

[5.1.4.1 Execute Dunning Proposal Run 231](#_Toc232850612)

[5.1.4.2 Execute Dunning Activity Run 232](#_Toc232850613)

[5.1.4.3 Display Collection History 232](#_Toc232850614)

[5.1.4.4 Valuation Collection Success 232](#_Toc232850615)

[5.1.4.5 Determining the Optimum Collection Strategy 233](#_Toc232850616)

[5.1.4.5.1 Maintain Master Data Groups 233](#_Toc232850617)

[5.1.4.5.2 Maintain Test Series for Collection Strategies 234](#_Toc232850618)

[5.1.4.5.3 Determine Master Data for Collection Test Series 234](#_Toc232850619)

[5.1.4.5.4 Update Collection Strategies 235](#_Toc232850620)

[5.1.4.5.5 Undo Update of Collection Strategies 236](#_Toc232850621)

[5.1.5 Mass Close Dispute Cases 236](#_Toc232850622)

[5.2 API Services list 239](#_Toc232850623)

[5.2.1 API Services for Document Change 239](#_Toc232850624)

[5.2.2 API Services for Creditworthiness 240](#_Toc232850625)

[5.2.3 API Services for Installment Plan 240](#_Toc232850626)

[5.2.4 API Services for Dispute Cases 242](#_Toc232850627)

[5.2.5 API Services for Security Deposit 245](#_Toc232850628)

[5.2.6 API Services for Customer Payment Portal 246](#_Toc232850629)

## Purpose

Overview

In this process, you handle open item management for contract accounting. This includes dunning, installment plans, interest calculation, and credit clarification.

This scope item consists of the following processes:

- Dunning

With Dunning, you can create and send payment reminders or dunning letters to your business partners to remind them of overdue payables and to request payment.

- Installment Plans

With an installment plan, you divide source items into several installment receivables that have a due date in the future. Once an installment plan has been posted, the items of the installment plan and not the source items are referred to when a bank collection is made, or when a dunning run is carried out.

- Flexible Workflow for Installment Plan Creation

Flexible Workflow for Installment Plan Creation in Contract Accounting enables the approval processing of creating Installment Plan.

- Interest Calculation

With Interest Calculation, you can determine and post interest receivables and payables.

- Interest Calculation on Clearing

With Interest Calculation on Clearing, the interest is calculated and posted automatically during the clearing process.

- Credit Clarification

With Credit Clarification, you can systematically process existing credits in accounts for your business partners.

- Creditworthiness

With Creditworthiness, system automatically determines the creditworthiness of a business partner can via various business transactions, such as dunning, write-offs, returns and installment plans.

- Disconnection and Reconnection

With Disconnection and Reconnection functionality, you can:

Create disconnection requests during FI-CA dunning under configurable pre-conditions;

Send disconnection requests to a remote system;

Analyze of payments to items involved in disconnection requests and create reconnection requests if configured conditions are met;

Send reconnection requests to a remote system.

- Security Deposit

With Security Deposit functionality, you can request cash security deposits from your business partners and manage them in the system.

Meanwhile you can assign security deposits to contract accounts or contracts.

- Transfer Business Partner Items

You can transfer business partner items if you come across such cases as receivables from different contract accounts shall be transferred to a joint contract account or a payment was assigned to the wrong contract account and need to be transferred to another contract account, etc.

- Dispute Case Management

With Dispute Case Management,you can create and manage complaints (disputes) from your business partner about incorrect invoices and credits or missing payments and credits as dispute cases.

- Submit to Collection Agency

With external collection agencies, you can manage postings connected to submitting receivables to a collection agency and the exchange of information with those collection agencies in Contract Accounting.

- Integration with Credit Management

SAP Credit Management enables your company to operate centralized credit management. The business systems connected (for example, Contract Accounts Receivable and Payable , CRM, or SD) report the commitment of a business partner to SAP Credit Management via XML. SAP Credit Management consolidates these reports to a credit exposure and checks this against the current credit limit of the business partner.

- Promise to Pay

You use a promise to pay to record a business partner's agreement to pay receivables that are on his or her account. You can create, withdraw, replace and valuate a promise to pay.

- Factoring

In factoring, a company sells the receivables that he/she receives from his customers to the factoring company (factor) to obtain cash quickly. This increases the liquidity and improves the equity ratio.

- Handling of Service Provider Bills in Deregulated Market

With the Handling of Service Provider Bills in Deregulated Market, you can:

Set your Contract Accounting document with full payment and/or the inform about payment flags and send your payment information to the InfoContainer.

This document provides a detailed procedure for testing this scope item after solution activation, reflecting the predefined scope of the solution. Each process step, report, or item is covered in its own section, providing the system interactions (test steps) in a table view. Steps that are not in scope of the process but are needed for testing are marked accordingly. Project-specific steps must be added.

|  |
| --- |
| Note Values in this test script (decimal notation, date formats, and so on) are presented in U.S. standard notation. If your test system is set up to use a different notation, enter values as appropriate. |

## Prerequisites

This section summarizes all the prerequisites for conducting the test in terms of systems, users, master data, organizational data, other test data and business conditions.

|  |
| --- |
| Caution Testing in a 3-System LandscapeIn a 3-system landscape (with SAP Central Business Configuration as your configuration environment), changes to software and business configuration are applied to your systems independently of one another. It is therefore your responsibility to manage the active business configuration in your systems and synchronize configuration data in your SAP S/4HANA Cloud Public Edition system landscape. A synchronization is required, for example, after you've enhanced the scope, extended configuration, or adopted new or changed content from content updates or upgrades. For more information, refer to the [product assistance](https://help.sap.com/docs/SAP_S4HANA_CLOUD/b249d650b15e4b3d9fc2077ee921abd0/6c398c4ae7364af69d3edffe7fdc39f2.html) in the SAP Help Portal.Before testing, if you want to use all software features described for the process steps, reports, or items in this document, we recommend the Business Process Configuration Expert in your organization has upgraded the configuration content and deployed the configuration data to your system landscape.If the decision is not to upgrade the configuration content in your test or production system, you can run regression tests of software changes using the procedures in the previous test script version (see the following [link](https://support.sap.com/content/dam/SAAP/Sol_Pack/S4C/Library/TestScripts/2UJ_S4CLD2602_BPD_EN_AE.docx) ). |

### Additional Manual Configuration

Before you can test this scope item, you must have completed the additional configuration steps that are described in the Set-Up Instructions for this scope item. These configuration steps are specific for your implementation and include mandatory settings that are not delivered by SAP and must be created by you. For more information, follow the link to the document:

[Link to Set-Up Instructions](https://help.sap.com/docs/SAP_S4HANA_BEST_PRACTICES/b2098e326cb819568df6ca544d204677)

Regarding Settings for RITA, Activate Registration for Indirect Taxation Abroad, you could do manual modification for FICA. Please refer to chapter Addition Manual Configuration in Contract Accounting – Company Initiated Payments (2DP).

### System Access

| System | Details |
| --- | --- |
| System | Accessible via SAP Fiori Launchpad. Your system administrator provides you with the URL to access the various apps assigned to your role. |

### Roles

Create business roles using the following business role templates delivered by SAP and assign them to your individual test users.

Alternatively, if available, you can use the following spaces delivered by SAP. You create a space with pages containing predefined essential apps and assign it to the business role. You then assign this business role to your individual users.

For more information, refer to How to Create a Business Role from a Template in the [product assistance](https://help.sap.com/docs/SAP_S4HANA_CLOUD/53e36b5493804bcdb3f6f14de8b487dd/ec310a8b669a45ca898dc4dd91d97de2.html) for SAP S/4HANA Cloud Public Edition.

| Name (Role Template) | ID (Role Template) | Name (Launchpad Space) | ID (Launchpad Space) | Log On |
| --- | --- | --- | --- | --- |
| Administrator - Accounts Payable and Receivable (FI-CA) | SAP_BR_ADMIN_APR_FICA | Contract Accounting - Jobs | SAP_BR_ADMIN_APR_FICA |  |
| Collections Specialist (FI-CA) | SAP_BR_COLL_SPECIALIST_FICA | Contract Accounting - Collections | SAP_BR_COLL_SPECIALIST_FICA |  |
| Accounts Payable and Receivable Accountant (FI-CA) | SAP_BR_APR_ACCOUNTANT_FICA | Contract Accounting | SAP_BR_APR_ACCOUNTANT_FICA |  |
| Configuration Expert - Business Process Configuration | SAP_BR_BPC_EXPERT | Business Process Configuration / Business Process Configuration - Finance / Business Process Configuration - Procurement / Manage your Solution / Business Process Configuration - Workflow / Business Configuration - Feature Management / Business Process Configuration - Extensibility Explorer / Business Configuration - Transportation | SAP_BR_BPC_EXPERT / SAP_FIN_SPT_BPC_EXPERT_PC / SAP_MM_SPT_BIZ_PROC_CONFIGN_PC / SAP_CA_SPT_IC_LND_BASE_PC / SAP_CA_SPT_BPC_WORKFLOW_PC / SAP_CA_SPT_BPC_FM_PC / SAP_EI_SPT_BPC_EXT_PC / SAP_TM_SPT_TRANSPCFG_PC |  |
| Accounts Payable and Receivable Manager (FI-CA) | SAP_BR_APR_MANAGER_FICA | Contract Accounting - Analytics | SAP_BR_APR_MANAGER_FICA |  |
| Administrator | SAP_BR_ADMINISTRATOR | Administration / Administration - Workforce Master Data / Administration - License Compliance / Administration - Data Management / Administration - Output Control | SAP_BR_ADMINISTRATOR / SAP_BUM_SPT_ADMINISTRATION_PC / SAP_EI_SPT_ADM_LC_PC / SAP_CA_SPT_TDR_PC / SAP_OC_SPT_ADMINISTRATION_PC |  |
| Master Data Specialist - Product Data | SAP_BR_PRODMASTER_SPECIALIST | Product Master Specialist | SAP_BR_PRODMASTER_SPECIALIST / SAP_CMD_SPT_PR_GOV_PC |  |
| Product Configuration Modeler | SAP_BR_PRODUCT_CONFIG_MODELER | Product Configuration Modeler | SAP_BR_PRODUCT_CONFIG_MODELER |  |
| Pricing Specialist | SAP_BR_PRICING_SPECIALIST | Price Management | SAP_BR_PRICING_SPECIALIST |  |
| Internal Sales Representative | SAP_BR_INTERNAL_SALES_REP | Internal Sales / Customer Returns / Billing | SAP_BR_INTERNAL_SALES_REP / SAP_SD_SPT_RETURNS_INT_SALES_PC / SAP_SD_SPT_BILLING_INT_SALES_PC |  |
| Billing Clerk | SAP_BR_BILLING_CLERK | Billing | SAP_BR_BILLING_CLERK |  |
| Cash Management Specialist | SAP_BR_CASH_SPECIALIST | Cash Management | SAP_BR_CASH_SPECIALIST |  |
| Extensibility Specialist | SAP_BR_EXTENSIBILITY_SPEC | Extensibility / Extensibility | SAP_BR_EXTENSIBILITY_SPEC / SAP_CA_SPT_EXT_PC |  |
| Configuration Expert - Business Network Integration | SAP_BR_CONF_EXPERT_BUS_NET_INT | Business Network Integration / Business Network Integration - Concur Integration / Business Network Integration - Output Control / Business Network Integration - Data Replication / Configuration Expert - Business Network Integration Cross Applications | SAP_CORE_SPT_INT_PC / SAP_CON_SPT_CONCUR_INT_PC / SAP_OC_SPT_INT_PC / SAP_CA_SPT_DATA_REP_PC / SAP_CA_SPT_BUS_NETWORK_INT_PC |  |

### Master Data, Organizational Data, and Other Data

The organizational structure and master data of your company has been created in your system during activation. The organizational structure reflects the structure of your company. The master data represents materials, customers, and vendors, for example, depending on the operational focus of your company.

|  |
| --- |
| Caution Update Behavior of Predelivered Demo DataIn non-productive environments (such as starter systems, sandbox systems, or partner demo systems), SAP initially deploys demo data for your selected scope. You can use this data to test and evaluate business processes.In a customer system, you can receive new or updated demo data after initial activation with further scope enhancements, provided the existing demo data wasn't changed in an incompatible way. If activation errors occur due to incompatible changes in demo data, you're responsible for resolving them. If you don't resolve the errors within a specific time frame, SAP reserves the right to deactivate demo data in your systems. In this case, you can continue by creating your own demo data. Alternatively, you can request that your systems be reprovisioned if you want to work with predelivered demo data again.In partner systems, you can use the demo data deployed with the initial activation. No additional demo data will be deployed in the system with scope enhancements. You can only create additional demo data manually. |

Use your own master data or the following sample data to go through the test procedure.

Organizational Data

| Data | Sample Value | Details | Comments |
| --- | --- | --- | --- |
| Company Code | 3310 |  |  |
| Currency | AED |  |  |

Table 1: Other Data

|  |  |  |  |
| --- | --- | --- | --- |
|  | Sample Value | Details | Comments |
| Business Partner | BP_AE_99 |  |  |
| Contract Account | CA_AE_99 |  |  |

For more information on creating these master data objects, see the following [Master Data Scripts (MDS)](https://help.sap.com/docs/s4hana-best-practices/s4cld2608-master-data) Scripts (MDS):

Table 2: Master Data Script Reference

| Master Data Script ID | Description |
| --- | --- |
| 31X | Create Product Master of type "Service Product" - MDS |
| BET | Create Sales Pricing Condition - MDS |

### Business Conditions

Before this scope item can be tested, the following business conditions must be met.

| Scope Item ID | Business Condition |
| --- | --- |
| 2AR - Contract Accounting – Master Data and Basic Functions | Must be run before this test script. Contract partner and contract account have been created for posting. |
| 2BI - Contract Accounting – Customer Initiated Payments | During the testing procedure, you need to be able to post customer initiated payments via payment lot. |
| BD6 - Basic Credit Management | Must be activated before this test script. BP role - UKM000 Sap Credit Management has been activated in the system. |
| 22T - Set Up Configurable Model Using Variant Configuration | Must be activated before you run this test script. Business Catalog - SAP_LO_BC_VC_MODELING_PC has been activated for Manage Characteristics. |

### Preliminary Steps

#### Post Documents

Prerequisite

|  |
| --- |
| Note If you have activated RITA in your system, the Tax Country field is visible in the app.If you have not activated RITA, the field is not visible in the app. In this case, you can disregard the Tax Country field in the Procedure table below.For more information on activating RITA, please refer to J58 - Accounting and Financial Close - Preliminary Steps - Activate Registration for Indirect Taxation Abroad (Optional). |

Use

For account maintenance, you need to ensure the open items have been posted. (for example, both debit and credit open items under one BP)

For reset clearing, you need to ensure the clearing has been done.

For further processes, you need to post FI-CA documents.

For dunning, you need to ensure that the due date is in the past.

For credit clarification, you need to post credits upfront.

For liquidity forecast of cash management, you need to maintain planning group (for example, Domestic Customer) on contract account first, then post FI-CA documents.

Then you can access SAP Fiori app Check Cash Flow Items (F0735) and Cash Flow Analyzer (F2332) with role Cash Manager to see cash flow changes.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Accounts Payable and Receivable Accountant (FI-CA). |  |  |
| 2 | Access App | Open Post Document (FPE1). | Post Document: Initial Screen displays. |  |
| 3 | Enter Data | Make the following entries:Document Date: <Today’s date>Posting Date: <Today’s date>Document Type: YACurrency: AEDReconcil. Key: <Reconciliation key generated by system>Clearing Reason: 01 Incoming PaymentBP Item: Y01G/L Item: Y01Calculate Automatically: <Select> |  |  |
| 4 | Enter BP Item | Choose New BP Itm. | The Checking reconciliation key screen appears.Note If Reconcil. Key has already been created, the Checking reconciliation key screen won’t be displayed. Please go to step 7 directly. |  |
| 5 | Create Reconciliation Key | Choose Yes. | A new reconciliation key is created. |  |
| 6 | Continue to Enter BP Item | Choose Continue. | The Post Document: Enter Item screen displays. |  |
| 7 | Enter Item Data | Make the following entries:In the Account Assignment section:Bus. Partner: <Business partner number with MKK BP role>Contract Acct: <Contract account number related to the selected BP>Contract: <Provider contract number, which is optional>Note If the document has contract, you also need to fill in Contract Item.Company Code: 3310Transac.: Y600/0020Note Please use Transaction: Y600/0010 to post credit open items.In the Amounts and Due Date section:Net Due Date: <Three weeks in the past>Amount: <Any amount value>Tax C/R: <Tax country>Note The Tax C/R field is only visible when RITA is activated in your system. |  |  |
| 8 | Post Document | Choose Post. | The FI-CA document is posted. |  |

Alternatively, you can post documents via the SAP Fiori app Import Documents.

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as an Accounts Payable and Receivable Accountant (FI-CA). |  |  |
| 2 | Access App | Open Import Documents (FPB1X). | The Transfer Document from File screen displays. |  |
| 3 | Create Template | Choose Create CSV Template. |  |  |
| 4 | Save Template | Make the following entries:File Name: <Name of the file>Save as type: All Files (*.*)Click Choose.Then choose OK. | The template is stored to the WebGui File Browser. |  |
| 5 | Change File | Choose Menu > SAP GUI for HTML File Browser.Select the file and choose Export to Native File System. | The file is downloaded to your computer. |  |
| 6 | Enter Data | Open the file and enter the following data:WAERS: AEDBLART: YABLDAT: <Today’s date> (in format YYYYMMDD)BUDAT: <Today’s date> (in format YYYYMMDD)BUKRS: 3310OPUPK : 1GPART: <Business partner number with MKK BP role>VKONT: <Contract account number related to the selected BP>HVORG: Y600TVORG: 0020 (leading zeros need to be contained)BETRW: <Any amount value>Enter several parameters and save the file. |  |  |
| 7 | Select File | Go back to the app and choose the value help in the field File Path for Import. Select the file and choose Import from native file system. Select the file from your computer. Choose Open. In the next dialog choose OK to overwrite the old file.Then click on Choose. | The Transfer Document from File Screen is displayed again. |  |
| 8 | Execute | Make the following entry and choose Execute:Reconciliation Key: <Reconciliation key generated by system> | The system displays a list with all the items you have entered. The column Message shows the text Document not yet checked. |  |
| 9 | Check and Post | Choose Check and Post. | The dialog box Post Documents appears. |  |
| 10 | Confirm | Choose Yes. | The text in the column Message changes to Document was posted. |  |

#### Maintain Contract Account

Use

In this activity, you enter the relevant dunning parameters in the contract account that should be dunned. You need to ensure that no payment method is maintained and appropriate parameters for the dunning are set.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Accounts Payable and Receivable Accountant (FI-CA). |  |  |
| 2 | Access App | Open Maintain Contract Account (CAA3). | Contract Account Display: Initial Screen displays. |  |
| 3 | Select Change Mode | Choose Change. | Contract Account Change: Initial Screen displays. |  |
| 4 | Open Contract Account | Make the following entry and choose Continue:Contract Acct: <Select contract account related to business partner> | The Contract Account Change: General Data screen displays. |  |
| 5 | Maintain General Data | Choose the General Data tab and make the following entry:Interest Key: <Standard Interest Key> |  |  |
| 6 | Maintain Payment/Taxes | Choose the Payment/Taxes tab:Inc. Payt.Method: <must be empty> |  |  |
| 7 | Maintain Dunning/Correspondence | Choose the Dunning/Correspondence tab and make the following entries:Grouping: Dunning GroupingDunning Proc.: Standard Dunning ProcedureCorresp.Variant.: only printout, immediately |  |  |
| 8 | Save | Choose Save. | Changes to the contract account are saved. |  |

## Overview Table

This scope item consists of several process steps provided in the table below.

|  |
| --- |
| Note If your system administrator has enabled spaces and pages on the SAP Fiori launchpad, the homepage will only contain the essential apps for performing the typical tasks of a business role.You can find all other (searchable) apps not included on the homepage using the search bar ([2434549](https://me.sap.com/notes/2434549)).If you want to personalize the homepage and include the hidden apps, navigate to your user profile and choose App Finder. |

Table 3: Account Maintenance

| Process Step | Business Role | App/Transaction | Expected Results |
| --- | --- | --- | --- |
| [Account Maintenance: Process Open Items](#unique_12) [page ] 26 | Administrator - Accounts Payable and Receivable (FI-CA) | Maintain Accounts (FP06) | Open items are cleared. |

Table 4: Dunning

| Process Step | Business Role | App/Transaction | Expected Results |
| --- | --- | --- | --- |
| [Execute Dunning Proposal Run](#unique_13) [page ] 29 | Administrator - Accounts Payable and Receivable (FI-CA) | Dunning Runs (F3545) | Dunning proposal run groups overdue items into dunning notices. |
| [Delete Dunning Proposal Run](#unique_14) [page ] 30 | Administrator - Accounts Payable and Receivable (FI-CA) | Dunning Runs (F3545) | The unexpected dunning proposal is deleted. |
| [Execute Dunning Activity Run](#unique_15) [page ] 32 | Administrator - Accounts Payable and Receivable (FI-CA) | Dunning Runs (F3545) | Execute the dunning activity run as a second sub process of the dunning runs. |
| [Print Dunning Notices](#unique_16) [page ] 33 |  |  |  |
| [Print Correspondence](#unique_17) [page ] 33 | Administrator - Accounts Payable and Receivable (FI-CA) | Print Correspondence (F3537) | Print the dunning letters. |
| [Display Correspondence History](#unique_18) [page ] 35 | Accounts Payable and Receivable Accountant (FI-CA) | Display Correspondences (F3693) | Display the correspondence history. |
| [Display Dunning History](#unique_19) [page ] 35 | Administrator - Accounts Payable and Receivable (FI-CA) | Display Dunning History (FPM3) | Display the dunning history for the business partner you have just dunned. |
| [Maintain Dunning Notice](#unique_20) [page ] 36 | Collections Specialist (FI-CA) | Maintain Dunning Notices (F3678) | The Dunning Notices are shown in the list. |
| [Valuate Success of Dunning](#unique_21) [page ] 37 | Administrator - Accounts Payable and Receivable (FI-CA) | Dunning Runs (F3545) | Execute the valuation of your dunning success. |
| [Dunning Exceptions](#unique_22) [page ] 41 |  |  |  |
| [Display Dunning Exception List](#unique_23) [page ] 41 | Administrator - Accounts Payable and Receivable (FI-CA) | Display Dunning Run Exceptions (F7575) | Display the dunning exception list. |
| [Delete Dunning Exception](#unique_24) [page ] 42 | Administrator - Accounts Payable and Receivable (FI-CA) | Delete Dunning Exception (FPMXC) | Display the dunning exception list. |

Table 5: Installment Plans

| Process Step | Business Role | App/Transaction | Expected Results |
| --- | --- | --- | --- |
| [Create Installment Plan](#unique_25) [page ] 43 | Collections Specialist (FI-CA) | Maintain Installment Plan (FPR3) | Create an installment plan. |
| [Print Installment Plan](#unique_26) [page ] 45 |  |  |  |
| [Print Correspondence](#unique_27) [page ] 45 | Administrator - Accounts Payable and Receivable (FI-CA) | Print Correspondence (F3537) | Print the installment plan correspondence. |
| [Display Correspondence History](#unique_28) [page ] 46 | Accounts Payable and Receivable Accountant (FI-CA) | Display Correspondences (F3693) | Display the overview of the installment plans. |
| [Display Installment Plan History](#unique_29) [page ] 47 | Collections Specialist (FI-CA) | Display Installment Plan History (FPRH) | Display the overview of the installment plans. |
| [Change Installment Plan](#unique_30) [page ] 48 | Collections Specialist (FI-CA) | Maintain Installment Plan (FPR3) | Change an installment plan. |
| [Display Installment Plan](#unique_31) [page ] 48 | Collections Specialist (FI-CA) | Maintain Installment Plan (FPR3) | Display an installment plan. |
| [Automatic Interest Run for Installment Plan](#unique_32) [page ] 49 | Collections Specialist (FI-CA) | Interest Run for Installment Plan (F6289) Maintain Installment Plan (FPR3) | Calculate and post interest of installment plans automatically. |

Table 6: Flexible Workflow for Installment Plan Creation (Option)

| Process Step | Business Role | App/Transaction | Expected Results |
| --- | --- | --- | --- |
| [Post Installment Plan](#unique_33) [page ] 59 | Collections Specialist (FI-CA) | Maintain Installment Plan (FPR3) | Create an installment plan. |
| [Verify Installment Plan Document](#unique_34) [page ] 60 | Collections Specialist (FI-CA) | Maintain Installment Plan (FPR3) | Change an installment plan. |
| [Approve Installment Plan Document (for Processor - Inbox)](#unique_35) [page ] 61 | Accounts Payable and Receivable Manager (FI-CA) | My Inbox for Contract Accounting - All Items (F5136) | Approve the installment plan document. |
| [Reject Installmen Plan Document (for Processor - Inbox)](#unique_36) [page ] 62 | Accounts Payable and Receivable Manager (FI-CA) | My Inbox for Contract Accounting - All Items (F5136) | Reject the installment plan document. |
| [Deactivate a Rejected Installment Plan Document (Requester)](#unique_37) [page ] 63 | Collections Specialist (FI-CA) | My Inbox for Contract Accounting - All Items (F5136) | Deactive the installment plan document. |
| [Resend a Rejected Installment Plan Document (Requester)](#unique_38) [page ] 64 | Collections Specialist (FI-CA) | My Inbox for Contract Accounting - All Items (F5136) | Resent the installment plan to approver. |

Table 7: Interest Calculation

| Process Step | Business Role | App/Transaction | Expected Results |
| --- | --- | --- | --- |
| [Post Interest](#unique_39) [page ] 65 | Collections Specialist (FI-CA) | Post Interest (FPI1) | Calculate interests manually. |
| Print Interest Notification |  |  |  |
| [Print Correspondence](#unique_40) [page ] 67 | Administrator - Accounts Payable and Receivable (FI-CA) | Print Correspondence (F3537) | Print the interest Notification correspondence. |
| [Display Correspondence History](#unique_41) [page ] 69 | Accounts Payable and Receivable Accountant (FI-CA) | Display Correspondences (F3693) | The Correspondence History displayed. |
| [Display Interest Calculation](#unique_42) [page ] 69 | Accounts Payable and Receivable Accountant (FI-CA) | Display Interest Calculations (F4761) | Display the interest calculation for an interest document. |
| [Execute Interest Run](#unique_43) [page ] 70 | Administrator - Accounts Payable and Receivable (FI-CA) | Interest Run (F3527) | Post interests automatically by executing the interest run. |

Table 8: Interest Calculation on Clearing

| Process Step | Business Role | App/Transaction | Expected Results |
| --- | --- | --- | --- |
| [Interest Calculation on Clearing](#unique_44) [page ] 72 | Accounts Payable and Receivable Accountant (FI-CA) | Maintain Accounts Run (F3531) | Interest Calculation on Automatic Clearing |
| [Display Interest Supplement](#unique_45) [page ] 75 | Accounts Payable and Receivable Accountant (FI-CA) | Display Document (FPE3) | The interest supplement can be displayed. |

Table 9: Credit Clarification

| Process Step | Business Role | App/Transaction | Expected Results |
| --- | --- | --- | --- |
| [Create Credit List](#unique_46) [page ] 76 | Administrator - Accounts Payable and Receivable (FI-CA) | Create Credit List (F3526) | Place the credits in clarification processing using the function Create Credit List |
| [Clarify Credits](#unique_47) [page ] 79 | Collections Specialist (FI-CA) | Clarify Credits (FPCRPO) | Clarify existing the credits which are part of the credit list created in the step before. |
| [Process Credits](#unique_48) [page ] 80 | Collections Specialist (FI-CA) | Process Credits (FPTCRPO) | Process individual credits that have not been placed in credit processing by the credit list |

Table 10: Creditworthiness

| Process Step | Business Role | App/Transaction | Expected Results |
| --- | --- | --- | --- |
| [Display Creditworthiness](#unique_49) [page ] 84 | Configuration Expert - Business Process Configuration | Manage Creditworthiness (F4408) | Creditworthiness is set. |

Table 11: Security Deposit

| Process Step | Business Role | App/Transaction | Expected Results |
| --- | --- | --- | --- |
| [Create Cash Deposit Request](#unique_50) [page ] 89 | Accounts Payable and Receivable Accountant (FI-CA) | Manage Security Deposits (F4415) | A Cash Deposit Request is created |
| Print Security Deposit | Accounts Payable and Receivable Accountant (FI-CA) | Manage Security Deposits (F4415) | The Cash Deposit Request is Printed |
| [Receive Cash Security Deposit Payment](#unique_51) [page ] 93 | Accounts Payable and Receivable Accountant (FI-CA) | Process Payment Lot (FP05) | Payment lot processed successfully |
| [Release Security Deposit](#unique_52) [page ] 96 | Accounts Payable and Receivable Accountant (FI-CA) | Manage Security Deposits (F4415) | Security deposits released successfully |
| [Return Security Deposit](#unique_53) [page ] 96 | Administrator - Accounts Payable and Receivable (FI-CA) | Payment Run / Debit Memo Run (F3529) | Payment run successfully |
| [Cash Security Deposit Interest Calculation (Optional)](#unique_54) [page ] 99 | Administrator - Accounts Payable and Receivable (FI-CA) | Interest Run for Security Deposits (F4547) | The Interest Run for Security Deposit is displayed. |

Table 12: Transfer Business Partner Items

| Process Step | Business Role | App/Transaction | Expected Results |
| --- | --- | --- | --- |
| [Transfer Business Partner Items](#unique_55) [page ] 100 | Accounts Payable and Receivable Accountant (FI-CA) | Transfer Business Partner Items (F4398) | Get the transfer document number successfully |

Table 13: Dispute Case Management

| Process Step | Business Role | App/Transaction | Expected Results |
| --- | --- | --- | --- |
| Incorrect Invoice Processing |  |  |  |
| [Create a Dispute Case of Incorrect Invoice](#unique_56) [page ] 112 | Accounts Payable and Receivable Accountant (FI-CA) | Manage Dispute Cases (F4443) | A dispute case of Incorrect Invoice is created. |
| [Modify the Dispute Case Status](#unique_57) [page ] 114 | Accounts Payable and Receivable Accountant (FI-CA) | Manage Dispute Cases (F4443) | The status of dispute case is changed. |
| [Process the Incorrect Invoice Dispute Case](#unique_58) [page ] 115 | Accounts Payable and Receivable Accountant (FI-CA) | Post Document (FPE1) | The dispute case is processed. |
| [Close the Dispute Case](#unique_59) [page ] 117 | Accounts Payable and Receivable Accountant (FI-CA) | Manage Dispute Cases (F4443) | The dispute case is closed. |
| Missing Payment Processing |  |  |  |
| [Create a Dispute Case of Missing Payment](#unique_60) [page ] 119 | Accounts Payable and Receivable Accountant (FI-CA) | Manage Dispute Cases (F4443) | A dispute case of missing payment is created.The status of dispute case is changed. |
| [Modify the Dispute Case Status](#unique_61) [page ] 120 | Accounts Payable and Receivable Accountant (FI-CA) | Manage Dispute Cases (F4443) | The Payment assignment is reset. |
| [Reset Payment Assignment](#unique_62) [page ] 121 | Accounts Payable and Receivable Accountant (FI-CA) | Process Payment Lot (FP05) | The Payment document is assigned to the dispute case. |
| [Assign Payments to Dispute Case (Optional)](#unique_63) [page ] 122 | Accounts Payable and Receivable Accountant (FI-CA) | Manage Dispute Cases (F4443) | The dispute case is closed. |
| [Close the Dispute Case](#unique_64) [page ] 123 | Accounts Payable and Receivable Accountant (FI-CA) | Manage Dispute Cases (F4443) | The email is sent to the recipient. |
| [Send Email (Optional)](#unique_65) [page ] 124 | Accounts Payable and Receivable Accountant (FI-CA) | Manage Dispute Cases (F4443) | The email is sent to the recipient. |

Table 14: Disconnection and Reconnection

| Process Step | Business Role | App/Transaction | Expected Results |
| --- | --- | --- | --- |
| [Create Disconnection Request](#unique_66) [page ] 126 |  |  |  |
| [Execute Dunning Proposal Run](#unique_67) [page ] 127 | Administrator - Accounts Payable and Receivable (FI-CA) | Dunning Runs (F3545) | Dunning proposal run groups overdue items into dunning notices. |
| [Execute Dunning Activity Run](#unique_68) [page ] 129 | Administrator - Accounts Payable and Receivable (FI-CA) | Dunning Runs (F3545) | Disconnection Requests created for Overdue Open items during dunning run under configurable pre-conditions. |
| [Send Disconnection and Reconnection Requests](#unique_69) [page ] 129 | Administrator - Accounts Payable and Receivable (FI-CA) | Send Disconnection and Reconnection Requests (F4658) | Analyze and send out the Disconnection requests |
| [Payment Lot Processing](#unique_70) [page ] 131 | Accounts Payable and Receivable Accountant (FI-CA) | Process Payment Lot (FP05) | The overdue open items will be partial or completely cleared. |
| [Create Reconnection Requests](#unique_71) [page ] 133 | Administrator - Accounts Payable and Receivable (FI-CA) | Create Reconnection Requests (F4654) | Analyze and create the Reconnection requests |
| [Send Disconnection and Reconnection Requests](#unique_72) [page ] 134 | Administrator - Accounts Payable and Receivable (FI-CA) | Send Disconnection and Reconnection Requests (F4658) | Analyze and send out the Reconnection requests |
| [Monitor Disconnection Requests](#unique_73) [page ] 135 | Administrator - Accounts Payable and Receivable (FI-CA) | Monitor Disconnection Requests (F4943) |  |

Table 15: Collection Agency

| Process Step | Business Role | App/Transaction | Expected Results |
| --- | --- | --- | --- |
| [Post Documents](#unique_74) [page ] 136 | Accounts Payable and Receivable Accountant (FI-CA) | Post Document (FPE1) | Document post successfully. |
| [Release to Collection Agency](#unique_75) [page ] 136 | Collections Specialist (FI-CA) | Release Items for Collection (FP03E) | Submission status of receivable documents is updated. |
| [Submit to Collection Agency](#unique_76) [page ] 140 | Collections Specialist (FI-CA) | Manage Submitted Items (FP03) | Submission status of the item is updated. |
| [Post Collection Agency Information via Inbound Service](#unique_77) [page ] 144 |  | Use API tool (e.g. postman) | API execute without error. |
| [Process Information from Collection Agency](#unique_78) [page ] 147 | Administrator - Accounts Payable and Receivable (FI-CA) | Process Information from Collection Agency (F4924) | Collection Agency collected payment from customer processed. |
| [Post Receivables for Collection Agency](#unique_79) [page ] 148 | Administrator - Accounts Payable and Receivable (FI-CA) | Post Receivables for Collection Agency (F4923) | Payment posted for received from collection Agency |
| [Monitor Collection Services](#unique_80) [page ] 149 | Administrator - Accounts Payable and Receivable (FI-CA) | Monitor Collection Services (FKKCOLL_MONI) | Collection Services displayed |
| [Display History of Collection Items](#unique_81) [page ] 150 | Collections Specialist (FI-CA) | Display Collection Item History (FP03H) | Collection items displayed . |
| [Create List of Collection Items](#unique_82) [page ] 151 | Collections Specialist (FI-CA) | Create List with Collection Items (FP03L) | Collection items displayed . |

Table 16: Integration with Credit Management

| Process Step | Business Role | App/Transaction | Expected Results |
| --- | --- | --- | --- |
| [Transfer Credit Data](#unique_83) [page ] 152 | Administrator - Accounts Payable and Receivable (FI-CA) | Transfer Credit Data (F4905) | Credit exposure transferred. |
| [Replicate Creditworthiness](#unique_84) [page ] 154 | Administrator - Accounts Payable and Receivable (FI-CA) | Replicate Creditworthiness (F4904) | Creditworthiness updated and returned to Contract Accounts Receivable and Payable. |
| [Compare Credit Score](#unique_85) [page ] 155 | Administrator - Accounts Payable and Receivable (FI-CA) | Compare Credit Score (F4903) | marks the business partners where there was a change to their creditworthiness |
| [Prepare Master Data Change from External System](#unique_86) [page ] 157 | Administrator - Accounts Payable and Receivable (FI-CA) | Maintain Business Partner (BP) |  |
| [Process Master Data Change from External System](#unique_87) [page ] 159 | Extensibility Specialist | Custom Logic (F6957) |  |

Table 17: Factoring

| Process Step | Business Role | App/Transaction | Expected Results |
| --- | --- | --- | --- |
| [Post Documents](#unique_88) [page ] 161 | Accounts Payable and Receivable Accountant (FI-CA) | Post Document (FPE1) | The FI-CA document is posted. |
| [Offer Receivables for Sale](#unique_89) [page ] 161 | Administrator - Accounts Payable and Receivable (FI-CA) | Offer Receivables for Sale (F5384) Offer Receivables for Sale | The log should show no errors. |
| [Receive the Response of the Factor](#unique_90) [page ] 164 |  |  | Confirmation reason update. |
| [Process the Response of the Factor](#unique_91) [page ] 166 | Administrator - Accounts Payable and Receivable (FI-CA) | Process Response of Factor (F5385) | Process Response of Factor run without error. |
| [Buy Back Receivables from Factor (Optional)](#unique_92) [page ] 167 | Administrator - Accounts Payable and Receivable (FI-CA) | Buy Back Receivables from Factor |  |
| [Send Update to Factor](#unique_93) [page ] 170 | Administrator - Accounts Payable and Receivable (FI-CA) | Send Update to Factor (F5386) Send Update to Factor | Send Update to Factor run without error. |
| [Monitor Factoring Services](#unique_94) [page ] 172 | Administrator - Accounts Payable and Receivable (FI-CA) | Monitor Factoring Services (FPFA_MON) | Factoring information can be displayed in the factoring monitor. |
| [Reset Excepted Receivables](#unique_95) [page ] 174 | Administrator - Accounts Payable and Receivable (FI-CA) | Reset Excepted Receivables (F5389) |  |

Table 18: Promise to Pay

| Process Step | Business Role | App/Transaction | Expected Results |
| --- | --- | --- | --- |
| [Create Promise to Pay](#unique_96) [page ] 175 | Collections Specialist (FI-CA) | Process Promise to Pay (FP2P1) | Promise to pay is successfully created with number. |
| [Create Promise to Pay for Direct Debit (Optional)](#unique_97) [page ] 177 | Collections Specialist (FI-CA) | Process Promise to Pay (FP2P1) | Promise to pay is successfully created with number. |
| [Create Promise to Pay with Credit Card (Optional)](#unique_98) [page ] 179 | Collections Specialist (FI-CA) | Process Promise to Pay (FP2P1) | Promise to pay is successfully created with number. |
| [Display Promise to Pay](#unique_99) [page ] 182 | Accounts Payable and Receivable Accountant (FI-CA) | Display Promise to Pay (FP2P3) |  |
| [Print Promise to Pay](#unique_100) [page ] 184 | Administrator - Accounts Payable and Receivable (FI-CA) | Display Promise to Pay (FP2P3) |  |
| [Replace Promise to Pay (Optional)](#unique_101) [page ] 185 | Collections Specialist (FI-CA) | Process Promise to Pay (FP2P1) | The “old” promise to pay will be closed, while a new promise to pay is generated with new ID. |
| [Payment for Promise to Pay](#unique_102) [page ] 187 |  |  |  |
| Manual Payment by Payment Lot |  |  |  |
| [Create Payment Lot](#unique_103) [page ] 187 | Accounts Payable and Receivable Accountant (FI-CA) | Process Payment Lot (FP05) | Installments, payment documents and open items are displayed. You can also simulate the valuation of the promise to pay. |
| [Post Payment Lot](#unique_104) [page ] 189 | Accounts Payable and Receivable Accountant (FI-CA) | Process Payment Lot (FP05) | The old promise to pay is withdrawn and instead, a new promise to pay is created. |
| [Payment Run Execution (Optional)](#unique_105) [page ] 190 | Administrator - Accounts Payable and Receivable (FI-CA) | Payment Run / Debit Memo Run (F3529) | The open items relevant to the promise to pay are cleared by payment documents. |
| [Mass Valuation Run](#unique_106) [page ] 193 | Administrator - Accounts Payable and Receivable (FI-CA) | Valuate Promise to Pay (F5058) | The promise to pay is valuated with fulfillment rate, open/closed status is set, and the next check date is determined. |
| [Withdraw Promise to Pay](#unique_107) [page ] 195 | Collections Specialist (FI-CA) | Process Promise to Pay (FP2P1) | The promise to pay is withdrawn, its status is closed. |

Table 19: Handling of Service Provider Bills in Deregulated Market

| Process Step | Business Role | App/Transaction | Expected Results |
| --- | --- | --- | --- |
| [Post Documents](#unique_108) [page ] 198 | Accounts Payable and Receivable Accountant (FI-CA) | Post Document (FPE1) | The FI-CA document is posted. |
| [Change Document](#unique_109) [page ] 198 | Accounts Payable and Receivable Accountant (FI-CA) | Change Document (FPE2) | The FI-CA document is changed. |
| [Execute Payment Run](#unique_110) [page ] 199 | Administrator - Accounts Payable and Receivable (FI-CA) | Payment Run / Debit Memo Run (F3529) | Open items are cleared successfully. |
| [Check Information Container Creation](#unique_111) [page ] 201 | Administrator - Accounts Payable and Receivable (FI-CA) | Display Information Container (FPINFCO2) | The Information Container is created. |
| [Send Data from Information Container](#unique_112) [page ] 202 | Administrator - Accounts Payable and Receivable (FI-CA) | Forward Data from Information Container (F5792) Information Container: Forward Data | The Data from Information Container is send. |
| [Check the Send Status of Information Container](#unique_113) [page ] 204 | Administrator - Accounts Payable and Receivable (FI-CA) | Display Information Container (FPINFCO2) | The status of sending Information Container is sent. |
| [Reset the Send Status of Information Container](#unique_114) [page ] 204 | Administrator - Accounts Payable and Receivable (FI-CA) | Information Container: Reset Send (FPINFCO3) | The status of sending Information Container is reset. |

Table 20: Transfer Business Partner Postings to External Systems

| Process Step | Business Role | App/Transaction | Expected Results |
| --- | --- | --- | --- |
| [Transfer Business Partner Postings to External Systems](#unique_115) [page ] 213 | Accounts Payable and Receivable Accountant (FI-CA) | Transfer Business Partner Postings to External Systems (F8476) | The FI-CA documents are transferred to external system. |
| [Monitor Status Tranferred to External Systems](#unique_116) [page ] 214 | Configuration Expert - Business Network Integration | Message Dashboard - SAP Application Interface Framework (/AIFX/WDA0005) | You can monitor the status of transferred documents. |
| [Delete Trigger Data for Data Transfer to External Systems (Optional)](#unique_117) [page ] 215 | Accounts Payable and Receivable Accountant (FI-CA) | Delete Trigger Data for Data Transfer to External Systems (F8475) | Open items are cleared successfully. |

Table 21: Transfer Documents to Accounts Payable/Accounts Receivable

| Process Step | Business Role | App/Transaction | Expected Results |
| --- | --- | --- | --- |
| [Post Document](#unique_118) [page ] 218 | Accounts Payable and Receivable Accountant (FI-CA) | Post Document (FPE1) | Document is posted in contract accounting. |
| [Transfer Documents to Accounts Payable/Accounts Receivable](#unique_119) [page ] 220 | Accounts Payable and Receivable Accountant (FI-CA) | Transfer Documents to Accounts Receivable/Payable (F8633) | You transfer the documents to subledger. |
| [Display Document](#unique_120) [page ] 221 | Accounts Payable and Receivable Accountant (FI-CA) | Display Document (FPE3) | You can display the document and switch to posted subleger document. |
| [Reverse Document (Optional)](#unique_121) [page ] 222 | Accounts Payable and Receivable Accountant (FI-CA) | Reverse Documents Run (F3546) | Your document is reversed in contract accounting and subledger. |

## Test Procedures

This section describes test procedures for each process step that belongs to this scope item.

### Account Maintenance

#### Account Maintenance: Process Open Items

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you process open items for the business partner.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Accounts Payable and Receivable Accountant (FI-CA). |  |  |
| 2 | Access App | Open Maintain Accounts (FP06). | The Account maintenance: Select Account screen displays. |  |
| 3 | Enter Basic Parameters | Make the following entries:In the Selection Details area:Business Partner: <Business Partner number>Contract Account: <Contract Account number>Company Code: 3310In the Posting Parameters area:Currency: AEDChoose Open items.Note | The Account maintenance: Process Open Items screen displays. |  |
| 4 | Choose Items to Be Cleared | Choose the open items of the business partner to be cleared.For example,A receivable in the amount of 100 AEDA payable in the amount of 100 AEDChoose Activate item, check and make sure the Difference amount is 0 AED.Choose Post.Note Note down the clearing document. |  |  |

### Dunning

Prerequisite

|  |
| --- |
| Note Activate Dunning letter with QR code if you want to use this option, then business partner can pay invoice by scanning QR code. |

Depending on your configuration environment for SAP S/4HANA Cloud Public Edition, choose one of the following options:

Configure Your Solution:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Configuration Expert - Business Process Configuration. |  |  |
| 2 | Access App Manage Your Solution | Open Manage Your Solution and then choose Configure Your Solution. | The Manage Your Solution screen is displayed. |  |
| 3 | Access App Define Selection Criteria for Credit Clarification | Search with following criteria:Application Area: FinanceSub Application Area: Contract AccountingChoose the group Organization.Choose the configuration step Set Up Company Codes for Contract Accounts Receivable and Payable. | The Change View " Company Codes in Contract Accounts Receivable and Payable": Overview screen is displayed. |  |
| 4 | Select Entries for Company Codes | Select an entry for company code 3310For Dunning Notices: SelectedSave the entry. | Check the entries by accessing the configuration activity again. |  |

SAP Central Business Configuration:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the project experience in SAP Central Business Configuration. |  |  |
| 2 | Open Set Up Company Codes for Contract Accounts Receivable and Payable | Go to the Business Processes Configuration app and search for the following activity: Set Up Company Codes for Contract Accounts Receivable and Payable.Choose Open Documentation for the found line item to see more details about this configuration activity.Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. | The Change View " Company Codes in Contract Accounts Receivable and Payable": Overview screen is displayed. |  |
| 3 | Input Parameters | Select an entry for company code 3310For Dunning Notices: SelectedSave the entry. | Check the entries by accessing the configuration activity again. |  |

#### Execute Dunning Proposal Run

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this process step, you execute the dunning proposal. The dunning proposal run groups overdue items into dunning notices.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Administrator - Accounts Payable and Receivable (FI-CA). |  |  |
| 2 | Access App | Open Dunning Runs (F3545). | The Application Jobs screen displays. |  |
| 3 | Create New Job | Choose Create. | The New Job view displays. |  |
| 4 | Enter Posting Parameters | Make the following entries and choose Step 2:Job Template: FI-CA Dunning ProposalJob Name: FI-CA Dunning Proposal |  |  |
| 5 | Enter Posting Parameters | Make the following entry and choose Step 3:Start Immediately: Selected |  |  |
| 6 | Enter Posting Parameters | Make the following entries:In the Run Identification area:Run ID Prefix: For example, ID0In the General Selections area:Business Partner: <Business partner number>Contract Account: <Contract account number>Company Code: 3310In the Dunning Parameters area:Date of Issue: <Today's date>Dunning Procedure: 01 Standard Dunning ProcedureNote The Dynamic Date Function is available for parameters of date, you can also use the Dynamic Date Function with the Define Recurrence Pattern to set up the recurring run for mass activity to meet your business needs. For example, you can choose the dynamic date function TODAY for testing purpose. |  |  |
| 7 | Check Job | Choose Check. | System message You can go ahead and schedule the job is displayed. |  |
| 8 | Execute Job | Choose Schedule. | The Application Jobs screen appears.One new application job is created with a status. |  |
| 9 | Check Job Status | After the job has been finished, choose the arrow button at the end of the entry to navigate to the job details. | The Job Log screen is displayed. The log should show no errors.Note The Run Identification should combine Run ID Prefix + dynamic number (xx). |  |

#### Delete Dunning Proposal Run

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this process step, you can delete the unexpected dunning proposal.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Administrator - Accounts Payable and Receivable (FI-CA). |  |  |
| 2 | Access App | Open Dunning Runs (F3545). | The Application Jobs screen displays. |  |
| 3 | Create New Job | Choose Create. | The New Job view displays. |  |
| 4 | Enter Posting Parameters | Make the following entries and choose Step 2:Job Template: FI-CA Delete Dunning Proposal RunJob Name: FI-CA Delete Dunning Proposal Run |  |  |
| 5 | Enter Posting Parameters | Make the following entry and choose Step 3:Start Immediately: Selected |  |  |
| 6 | Enter Posting Parameters | Make the following entries:In the Run Identification area:Date ID: <Today's date>Run ID: <run ID on previous step> |  |  |
| 7 | Check Job | Choose Check. | System message You can go ahead and schedule the job is displayed. |  |
| 8 | Execute Job | Choose Schedule. | The Application Jobs screen appears.One new application job is created with a status. |  |
| 9 | Check Job Status | After the job has been finished, choose the arrow button at the end of the entry to navigate to the job details. | The Job Log screen is displayed. The log should show no errors. |  |

#### Execute Dunning Activity Run

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you execute the dunning activity run as a second sub process of the dunning runs.

Procedure

The dunning run stores the correspondence data in the Correspondence Container.

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Administrator - Accounts Payable and Receivable (FI-CA). |  |  |
| 2 | Access App | Open Dunning Runs (F3545). | The Application Jobs screen displays. |  |
| 3 | Create New Job | Choose Create. | The New Job view displays. |  |
| 4 | Enter Parameters | Make the following entries and choose Step 2:Job Template: FI-CA Dunning Activity RunJob Name: FI-CA Dunning Activity Run |  |  |
| 5 | Enter Parameters | Make the following entry and choose Step 3:Start Immediately: Selected |  |  |
| 6 | Enter Parameters | Make the following entries:In the Run Identification area:Run ID Prefix: For example, ID0Simulation run: UnselectedIn the General Selections area:Run Identification: <Select Run Identification from previous executed Dunning Proposal> |  |  |
| 7 | Check Job | Choose Check. | System message You can go ahead and schedule the job is displayed. |  |
| 8 | Execute Job | Choose Schedule. | The Application Jobs screen appears.One new application job is created with a status. |  |
| 9 | Check Job Status | After the job has been finished, choose the arrow button at the end of the entry to navigate to the job details. | The Job Log screen is displayed. The log should show no errors.Note The Run Identification should combine Run ID Prefix + dynamic number (xx). |  |

#### Print Dunning Notices

##### Print Correspondence

Purpose

In this activity, you print the dunning notice.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Administrator - Accounts Payable and Receivable (FI-CA). |  |  |
| 2 | Access App | Open Print Correspondence (F3537). | The Application Jobs screen displays. |  |
| 3 | Create New Job | Choose Create. | The New Job view displays. |  |
| 4 | Enter Required Parameters | Make the following entries and choose Step 2:Job Template: FI-CA: Print CorrespondenceJob Name: FI-CA: Print Correspondence |  |  |
| 5 | Enter Required Parameters | Make the following entry:Start Immediately: SelectedChoose Define Recurrence Pattern.Recurrence Pattern: <Select Single Run>Note For recurrence setting, select recurrence time cycle.Choose Step 3. |  |  |
| 6 | Enter Required Parameters | Make the following entries:In the Run Settings area:Run ID Prefix: For example, ID0In the Selection Criteria area:Business Partner: <Select business partner number>Contract Account: <Select contract account number>Company Code: 3310Correspondence Type: <Select 0003 Dunning Notice>In the Print Parameters area:Actual Print: Selected |  |  |
| 7 | Check Job | Choose Check. | System message You can go ahead and schedule the job displays. |  |
| 8 | Execute Job | Choose Schedule. | The Application Jobs screen displays.One new application job is created with a status. |  |
| 9 | Display Job Details | After the job has been finished, choose the arrow button at the end of the entry to navigate to the job details. | The Job Log screen displays. The log should show no errors.Note The Run Identification should combine Run ID Prefix + dynamic number (xx). |  |

##### Display Correspondence History

Purpose

In this activity, you display the correspondence history.

|  |
| --- |
| Note Business partner can make payment by scanning the QR code, if dunning letter with a QR code is activated. For detailed procedures, refer to the test script of the scope item 2BI Contract Accounting – Customer Initiated Payments, chapter Process Payments Paid via Link. |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Accounts Payable and Receivable Accountant (FI-CA). |  |  |
| 2 | Access App | Open Display Correspondences (F3693). | The Display Correspondences screen displays. |  |
| 3 | Search Criteria | Enter required parameters for search criteria. |  |  |
| 4 | Execute | Choose Go. | The correspondence details are listed. |  |
| 5 | Display Correspondence History | Select an entry to display. | Details of this entry are shown and you can see the QR code on the PDF file either via download or in the embedded mode. |  |

#### Display Dunning History

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you display the dunning history for the business partner you have just dunned.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Administrator - Accounts Payable and Receivable (FI-CA). |  |  |
| 2 | Access App | Open Display Dunning History (FPM3). | The Display Dunning History screen displays. |  |
| 3 | Display Dunning History | On the Display Dunning History screen, make the following entry and choose Execute.Business Partner: <Required Business Partner> | The dunning history is shown in a list. |  |

#### Maintain Dunning Notice

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you display details of the dunning notice for the business partner you have just dunned.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Collections Specialist (FI-CA). |  |  |
| 2 | Access App | Open Maintain Dunning Notices (F3678). | The Maintain Dunning Notices screen displays. |  |
| 3 | Enter Basic Parameters | Make the following entries:Business Partner: <Business Partner number>Contract Account: <Contract Account number> |  |  |
| 4 | Execute | Choose Go. | The Dunning Notices are shown in the list. |  |
| 5 | Display Details | Choose the right arrow button to the right of the dunning notice line item. | Generic details of the dunning notice are displayed:Dunning run dateChargeInterestDunning items are displayedDunning notice documentDunning amountDunning levelsSet next dunning levelShow dunning runDunning activities are displayed:Dunning activities descriptionCorrespondence |  |

#### Valuate Success of Dunning

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you can valuate your dunning success.

If the customers pay for their dunned items after the dunning run, it will have a positive effect on the dunning success. Therefore, make sure you post a payment via payment lot on the dunned items after the dunning run.

|  |
| --- |
| Note A payment within 7 days will be treated as 100% successful; each further day of delay reduces the success percentage rate by 2.5%. |

Procedure

1. Customers pay for dunned items:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Accounts Payable and Receivable Accountant (FI-CA). |  |  |
| 2 | Access App | Open Process Payment Lot (FP05). | Payment Lot initial Screen displays. |  |
| 3 | Input Parameters for Payment Lot | Create your payment lot ID and choose Create:Lot: <Your payment lot ID>Make the following entries on the Payment Lot Create: Default Entries and Status screen:Control Information:Lot: <Your payment lot ID>Search Term: <Input your search information>Additional Info: <Input your specific information>Specifications for Posting Documents:Document Type: <by default>Posting Date: <by default>Document Date: <by default>Reconciliation Key: <Generated by the system>Currency: AEDSpecification for Posting Items on Bank Clearing Account:Bank Clearing Account: 11001080Company Code: 3310House Bank: AEBK2Account ID: AEAC2Value Date: <Today's date>Selections for Selecting and Clearing Open Items:Clearing Reason: <01, by default>Selection Category: <by default>Line Layout: SAPClick New Items.On the Payment Lot Create: Payments screen, check and make the following entries:In the Default values and status section: <Values are maintained by default>In the Payments section:Payment Amount: <Input the amount>Selection Category: BCategory B stands for Document.If parameters you input are in accordance with the open items, the payment lot can clear open items of specific business partner, otherwise, it needs further clarification.Choose Save. | Payment lot is created. |  |
| 4 | Post Payment Lot | Input your payment lot ID on the Payment Lot: Initial Screen.Lot: <Your payment lot ID>Choose Close.Note Payment lot must be closed before it can be posted.Choose Yes when message appears: All payment entered in full?Choose Post.In the Schedule Job dialog box, choose Start online and choose OK.Choose Continue when message appears: Posting run is complete, check status.In the Status section, system shows the posting status.Postprocessing is required means the payment needs further clarification. | Payment lot is closed and posted. |  |

2. Execute valuation of dunning:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Administrator - Accounts Payable and Receivable (FI-CA). |  |  |
| 2 | Access App | Open Dunning Runs (F3545). | The Application Jobs screen displays. |  |
| 3 | Create New Job | Choose Create. | The New Job screen displays. |  |
| 4 | Enter Parameters | Make the following entries and choose Step 2:Job Template: FI-CA: Valuate DunningsJob Name: FI-CA: Valuate Dunnings |  |  |
| 5 | Enter Parameters | Make the following entry and choose Step 3:Start Immediately: SelectedRecurrence Pattern: Single Run |  |  |
| 6 | Enter Parameters | Make the following entries:Run IdentificationRun ID Prefix: For example, ID0Simulation: <Unselected>General SelectionsBusiness Partner: <Business Partner number>Company Code: 3310Date ID: <Select Date ID>Identification: <Select Identification>Check Date: <Choose date after Dunning and Payments>Note The check date of the dunning evaluation run must not be earlier than 14 days after the issue date of the dunning proposal run. |  |  |
| 7 | Check Job | Choose Check. | System message You can go ahead and schedule the job is displayed. |  |
| 8 | Execute Job | Choose Schedule. | The Application Jobs screen displays.One new application job is created with a status. |  |
| 9 | Check Job Status | After the job has been finished, choose the arrow button at the end of the entry to navigate to the job details. | The Job Log screen displays. The log should show no errors.Note The Run Identification should combine Run ID Prefix + dynamic number (xx). |  |

To check the result of the evaluation, you can use the SAP Fiori app Analyze Dunning Success. To do so, please refer to the test script of the scope item SAP Fiori Analytical Apps for Contract Accounting Manager (2KH).

#### Dunning Exceptions

Prerequisite

To create dunning exceptions, proceed as follows:

- To delete the dunning procedure in the contract account, see the Maintain Contract Account step.
- To process a dunning proposal again, see the Execute Dunning Proposal step.

##### Display Dunning Exception List

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you display the dunning exception list.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Administrator - Accounts Payable and Receivable (FI-CA). |  |  |
| 2 | Access App | Open Display Dunning Run Exceptions (F7575). | The Display Dunning Exceptions screen displays. |  |
| 3 | Maintain Display Dunning Exception Parameters | Make the following entries:Business Partner: <Required Business Partner>Contract Acct: <Required Contract Account> |  |  |
| 4 | Execute | Choose Go. | Details of dunning exception are listed. |  |
| 5 | Display | Select an entry to display. | Details of this entry are shown. |  |

##### Delete Dunning Exception

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you delete the dunning exception.

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Administrator - Accounts Payable and Receivable (FI-CA). |  |  |
| 2 | Access App | Open Delete Dunning Exception (FPMXC). |  |  |
| 3 | Maintain Delete Dunning Exception Parameters | Make the following entries:Date ID: <Running date>Identification: <Identification code of your choice>Simulation: Unselected |  |  |
| 4 | Enter | Choose Execute. | The dunning exceptions are deleted from the database. |  |

### Installment Plans

#### Create Installment Plan

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you create an installment plan.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Collections Specialist (FI-CA). |  |  |
| 2 | Access App | Open Maintain Installment Plan (FPR3).Note You can also use the App Manage Installment Plans (F5720) to create, change or display installment plan history. | Display Installment Plan: Initial Screen displays. |  |
| 3 | Create Installment Plan | Choose Create. | Create Installment Plan: Initial Screen displays. |  |
| 4 | Maintain Parameters | Make the following entries:Business Partner: <Required Business Partner>Contract Account: <Required Business Partner>Currency: AEDPosting Date: <Today's date>Document Date: <Today's date>Doc Type: Inst Plan: YADoc. Type: Charges: YAReconciliation Key: <Reconciliation Key generated by system> |  |  |
| 5 | Save | Choose Continue. | Create Installment Plan: Select Items and Enter Parameters Initial Screen is displayed. |  |
| 6 | Select Item | In the Item Selection section, select the items for the installment plan. |  |  |
| 7 | Maintain Installment Plan Parameters | In the Installment Plan Parameters section, make the following entries:Inst. Plan Type: SAEStart Date: <Today's date> |  |  |
| 8 | Propose | Choose Propose. | The Create Installment Plan: Define Installments screen displays. |  |
| 9 | Save | Choose Save. | The installment plan is created. |  |

#### Print Installment Plan

##### Print Correspondence

Purpose

In this activity, you print the installment plan. The correspondence printing run determines the correspondence data that has been stored in the Correspondence Container.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Administrator - Accounts Payable and Receivable (FI-CA). |  |  |
| 2 | Access App | Open Print Correspondence (F3537). | The Application Jobs screen displays. |  |
| 3 | Create New Job | Choose Create. |  |  |
| 4 | Enter Required Parameters | Make the following entries and choose Step 2:Job Template: FI-CA: Print CorrespondenceJob Name: FI-CA: Print Correspondence |  |  |
| 5 | Enter Required Parameters | Make the following entry:Start Immediately: SelectedChoose Define Recurrence Pattern.Recurrence Pattern: <Select Single Run>Note For recurrence setting, select recurrence time cycle.Choose Step 3. |  |  |
| 6 | Enter Required Parameters | Make the following entries:In the Run Settings area:Run ID Prefix: For example, ID0In the Selection Criteria area:Business Partner: <Select business partner number>Contract Account: <Select contract account number>Company Code: 3310Correspondence Type: <Select 0005 Installment Plan>In the Print Parameters area:Actual Print: Selected |  |  |
| 7 | Check Job | Choose Check. | System message You can go ahead and schedule the job displays. |  |
| 8 | Execute Job | Choose Schedule. | The Application Jobs screen displays.One new application job is created with a status. |  |
| 9 | Display Job Details | After the job has been finished, choose the arrow button at the end of the entry to navigate to the job details. | The Job Log screen displays. The log should show no errors.Note The Run Identification should combine Run ID Prefix + dynamic number (xx). |  |

##### Display Correspondence History

Purpose

In this activity, you display the correspondence history.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Accounts Payable and Receivable Accountant (FI-CA). |  |  |
| 2 | Access App | Open Display Correspondences (F3693). | The Display Correspondences screen displays. |  |
| 3 | Search Criteria | Enter required parameters for search criteria. |  |  |
| 4 | Execute | Choose Go. | The correspondence details are listed. |  |
| 5 | Display Correspondence History | Select an entry to display. | Details of this entry are shown. |  |

#### Display Installment Plan History

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you display the overview of the installment plans.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Collections Specialist (FI-CA). |  |  |
| 2 | Access App | Open Display Installment Plan History (FPRH). | The Overview of Installment Plans screen displays. |  |
| 3 | Input Business Partner | Make the following entry:Business Partner: <Required Business Partner> |  |  |
| 4 | Display Installment Plan | Choose Run. | The Installment Plan History screen displays.Selected business partner is listed on the left side of the screen. View details by expanding the structure and choosing the installment plan. |  |

#### Change Installment Plan

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you can change an installment plan.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Collections Specialist (FI-CA). |  |  |
| 2 | Access App | Open Maintain Installment Plan (FPR3). | Create Installment Plan: Initial Screen displays. |  |
| 3 | Select Installment Plan | Make the following entry and choose Continue:Install. Plan No.: <Required Installment Plan> |  |  |
| 4 | Switch to Change Mode | Choose Edit. | Change Installment Plan: Initial Screen displays. |  |
| 5 | Change Installment Plan | Modify installments by changing:Installment AmountDue |  |  |
| 6 | Save | Choose Save. | The changed installment plan is saved. |  |

#### Display Installment Plan

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you can display an installment plan.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Collections Specialist (FI-CA). |  |  |
| 2 | Access App | Open Maintain Installment Plan (FPR3). | Display Installment Plan: Initial Screen displays. |  |
| 3 | Display Installment Plan | Make the following entry and choose Continue:Install. Plan No.: <Required Installment Plan> | The installment plan is displayed. |  |

#### Automatic Interest Run for Installment Plan

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this process step, you calculate and post interest of installment plans automatically by executing the interest run.

Context

Automatic Interest Run for Installment Plan in Contract Accounting enables the automatic interest calculation and posting against mass installment plans.

You've activated Interest Calculated from Original Items via SSCUI (102198) and completed all the prerequisite procedure in the Create Installment Plan step. Follow the procedure in the Change Installment Plan step to change the due date of open items of installment plans. Choose the Update Interest Document button to trigger the interest update based on the new due date but without posting in the SAP Fiori app Maintain Installment Plan (FPR3). Then, you execute the job via Interest Run for Installment Plan (F6289) to trigger the interest calculation and posting. After the job is executed, you can check the posted interesting document in the SAP Fiori app Maintain Installment Plan (FPR3).

Prerequisites

Make sure you have completed procedure below to activate Interest Calculated from Original Items in Contract Accounting.

1. Define Default Values for Interest on Installment Plans via SSCUI (102198):

Depending on your configuration environment for SAP S/4HANA Cloud Public Edition, choose one of the following options:

Configure Your Solution:

| Step # | Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. |  |  |
| 2 | Access App | Open Manage Your Solution and choose Configure Your Solution. | The Manage Your Solution screen is displayed. |  |
| 3 | Input Parameters | Search with following criteria:Application Area: FinanceSub Application: Contract AccountingItem Name: Installment PlanClick Configure in the Define Default Values for Interest on Installment Plans row.Int. fm Orig.Items: XChoose Save. | Interest Calculated from Original Items is saved. |  |

SAP Central Business Configuration:

| Step # | Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the project experience in SAP Central Business Configuration. | The SAP Fiori launchpad is displayed. |  |
| 2 | Open Define Default Values for Installment Plan Charge | Go to the Business Processes Configuration app and search for the following activity: Define Default Values for Interest on Installment Plans.Choose Open Documentation for the found line item to see more details about this configuration activity.Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. | The Maintian Installment Plan Interest: Specifications: Detail scr screen is displayed. |  |
| 3 | Input Parameters | Int. fm Orig.Items: XChoose Save. | Interest Calculated from from Original Items is saved. |  |

1. Define Interest Calculation Rules via SSCUI (102065):

Please refer to the chapter Preliminary Steps - Post Interest.

Procedure

1. Run FPINTM3 to post interest:

| Step # | Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Administrator - Accounts Payable and Receivable (FI-CA). |  |  |
| 2 | Access App | Open Interest Run for Installment Plan (F6289). | The Application Jobs screen displays. |  |
| 3 | Create New Job | Choose Create. | The New Job view displays. |  |
| 4 | Enter Required Parameters | Make the following entries and choose Step 2:Job Template: FI-CA: Interest Run for Installment PlansJob Name: FI-CA: Interest Run for Installment Plans |  |  |
| 5 | Enter Posting Parameters | Make the following entry and choose Step 3:Start Immediately: Selected |  |  |
| 6 | Enter Posting Parameters | Make the following entries:Run IdentificationPrefix of Run ID: For example, ID0Simulation Run: UnselectedGeneral SelectionsInstall.Plan No.: <Your Installment plan>PostingPosting Date: <Today's date>Interest Doc. Type: YAInterest Key: Standard Interest KeyInt. fm Orig. Items: Selected |  |  |
| 7 | Check Job | Choose Check. | System message You can go ahead and schedule the job is displayed. |  |
| 8 | Execute Job | Choose Schedule. | The Application Jobs screen displays.One new application job is created with a status. |  |
| 9 | Check Job Status | After the job has been finished, choose the arrow button at the end of the entry to navigate to the job details. | The Job Log screen is displayed. The log should show no errors.The Run Identification should combine Run ID Prefix + dynamic number (xx). |  |

1. Display interest documents of installment plan:

| Step # | Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Collections Specialist (FI-CA). |  |  |
| 2 | Access App | Open Maintain Installment Plan (FPR3). | The Display Installment Plan screen is displayed. |  |
| 3 | Select Installment Plan | Make the following entry and choose Continue:Install. Plan No.: <Required Installment Plan> |  |  |
| 4 | Display Interest Document | Choose Menu > Environment > Interest Documents. | Interest Document is displayed. |  |

### Flexible Workflow for Installment Plan Creation (Optional)

Context

Flexible Workflow for Installment Plan Creation in Contract Accouting enables the approval processing of creating installment plan. If an installment plan meets conditions set in Manage Workflows for Contract Accounting (F5135), it is automatically blocked and routed to approver for action (release/rejection).

During the workflow:

- Approvers receive workflows in Inbox for Contract Accounting and can release/reject the installment plans.
- After the installment plans are released, they are unblocked and can go for further processing.
- If the installment plan is rejected, there is an option to send the installment plan back to the requestor’s Inbox. Requestor can accept the rejection event of the document or resend it for approval.
- If the document is resent to approver, the approval cycle will restart.

It is important to know that the document will always be posted no matter a workflow is triggered or not. The only difference is that the document which has a workflow involved is currently ‘blocked’ for certain business process(es) according to SSCUI (103740-Define Check Reasons). In this case, check reason 03 for Installment Plan Creation with settings below is used in this test script.

| Check Reason | No Payment | No Clearing | No Dunning | No Interest | No Changes |
| --- | --- | --- | --- | --- | --- |
| 03 |  |  |  |  | X |

Prerequisites

Make sure you have completed below steps to activate the Flexible Workflow for Installment Plan Creation in Contract Accounting.

1. Define Default Values for Installment Plan Charge via SSCUI (102197)

Depending on your configuration environment for SAP S/4HANA Cloud Public Edition, choose one of the following options:

Configure Your Solution:

| Step # | Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. |  |  |
| 2 | Access App | Open Manage Your Solution and choose Configure Your Solution. | The Manage Your Solution screen displays. |  |
| 3 | Input Parameters | Application Area: FinanceSub Application: Contract AccountingItem Name: Installment PlanSelect Configuration, choose step Define Default Values for Installment Plan Charge.Temp.Charges:DocType: YAChoose Save. | Default values for installment plan charge is saved. |  |

SAP Central Business Configuration:

| Step # | Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the project experience in SAP Central Business Configuration. |  |  |
| 2 | Open Define Default Values for Installment Plan Charge | Go to the Business Processes Configuration app and search for the following activity: Define Default Values for Installment Plan Charge.Choose Open Documentation for the found line item to see more details about this configuration activity.Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. | The Default Values for Installment Plan Charge screen is displayed. |  |
| 3 | Input Parameters | Temp.Charges:DocType: YASave it. |  |  |

1. Define Check Reason via SSCUI (103740)

It is recommended to create your own check reason for your workflow. If you decide to use standard check reason 03, you can skip this step.

Depending on your configuration environment for SAP S/4HANA Cloud Public Edition, choose one of the following options:

Configure Your Solution:

| Step # | Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. |  |  |
| 2 | Access App | Open Manage Your Solution and choose Configure Your Solution. | The Manage Your Solution screen displays. |  |
| 3 | Input Parameters | Application Area: FinanceSub Application: Contract AccountingItem Name: Postings and DocumentsSelect Configuration, choose step Define Check Reasons.Choose the standard check reason 03, copy it to create your check reason code and adapt the setting for your business needs. | The Change View "Check Reasons for Dual Control Principle": Overview screen displays. |  |

SAP Central Business Configuration:

| Step # | Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the project experience in SAP Central Business Configuration. |  |  |
| 2 | Open Define Check Reasons | Go to the Business Processes Configuration app and search for the following activity: Define Check Reasons.Choose Open Documentation for the found line item to see more details about this configuration activity.Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. | The Change View "Check Reasons for Dual Control Principle": Overview screen displays. |  |
| 3 | Input Parameters | Choose the standard check reason 03, copy it to create your check reason code and adapt the setting for your business needs. |  |  |

1. Activate Flexible Workflow for Posting Document

There are two ways to activate the flexible workflow in Cloud, you can choose either of them to activate your flexible workflow:

-
    1. Via SSCUI (103769) - Define Default Check Reason for Workflow

Depending on your configuration environment for SAP S/4HANA Cloud Public Edition, choose one of the following options:

Configure Your Solution:

| Step # | Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. |  |  |
| 2 | Access App | Open Manage Your Solution and choose Configure Your Solution. | The Manage Your Solution screen displays. |  |
| 3 | Input Parameters | Application Area: FinanceSub Application: Contract AccountingItem Name: Postings and DocumentsSelect Configuration, choose step Define Default Check Reason for Workflow.Choose Create.Scenario: WS02400077Check Reason: 03Save it. | The Maintain C003:Overview screen displays.The default check reason is assigned to workflow scenario ID.The workflow for Installment Plan creation is enabled in this client. |  |

SAP Central Business Configuration:

| Step # | Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the project experience in SAP Central Business Configuration. |  |  |
| 2 | Open Define Default Check Reason for Workflow | Go to the Business Processes Configuration app and search for the following activity: Define Default Check Reason for Workflow.Choose Open Documentation for the found line item to see more details about this configuration activity.Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. | The Maintain C003:Overviewscreen displays. |  |
| 3 | Input Parameters | Choose Create.Scenario: WS02400077Check Reason: 03Save it. |  |  |

-
    1. Implement Cloud BAdI: FI-CA Dual Control Principle: New Installment Plan (FKK_EVENT_5506) and assign the check reason into the BAdI.

If you need more conditions to trigger your workflow and SSCUI could not meet your business requirement, you could implement Cloud BAdI: FI-CA Dual Control Principle: New Installment Plan (FKK_EVENT_5506) .There is a certain priority for deriving the check reason. If you have implemented the check reason in the Cloud BAdI 5500, the configuration in the SSCUI (103769) - Define Default Check Reason for Workflow will be ignored.

1. Define Responsibility for Rules Used in Workflow Steps and Assign Users to Responsibilities

|  |
| --- |
| Note The approver(s) and requester(s) must be different business users. |

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on on to the SAP Fiori launchpad as Configuration Expert - Business Process Configuration . |  |  |
| 2 | Access App | Open Manage Teams and Responsibilities - Contract Accounting (F5134). | The Manage Teams and Responsibilities view displays. |  |
| 3 | Create Team | Choose Create. | The Team view displays. |  |
| 4 | Enter Team Details | Choose the Team Information tab and make the following entries:Name: <For example, Approver of Installment Plan>Global ID: <For example, Installment Plan Posting approver>Type: SFICAIPWF (Installment Plan Workflow Approval)Description: <Optional>Status: Enabled |  |  |
| 5 | Enter Team Details | Choose the Team Members tab. |  |  |
| 6 | Enter Team Details | Choose Create. | A blank field displays under Business Partner. |  |
| 7 | Enter Team Details | Make the following entries and choose Save:Business Partner: <For example, Example Accounts Payable and Receivable Manager>Function: Function for Approving - Level 1 | The Responsibility for the contract document posting workflow is defined. |  |

1. Define and Activate Your Approval Workflows

You can create a new workflow by copying the standard template or create a new entry directly. In this activity, you create a new workflow by copying the standard template.

|  |
| --- |
| Note You can have multiple active workflows and can define or sort the order. The system will go through all the active workflows in order from the first to the last until the workflow process could be started. If the system determines a workflow that starts a workflow process, others would be ignored. |

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. |  |  |
| 2 | Access App | Open Manage Workflows for Contract Accounting (F5135). | The Manage Workflows view displays. |  |
| 3 | Select Workflow | Select Workflow for Installment Plan from the Workflows drop-down list. |  |  |
| 4 | Choose Template | Choose Workflow Template. |  |  |
| 5 | Copy Workflow | Choose Copy. | The Copy of Workflow screen displays. |  |
| 6 | Enter Workflow Details | Make the following entries and choose Save:Choose the Header tab:Name: for example, Installment Plan creation workflowChoose the Properties tab:Description: for example, Installment Plan creation workflowValid from: <Today’s date>Valid to: 12/31/9999Choose the Start Conditions tab:Only start the workflow if all of the following preconditions are met:For example, Installment Plan category is 01.Choose the Add button to add another condition.For example, Number of installment plans is greater than 10.Create Alternative Preconditions tab: (Optional)Choose the Steps tab.Choose the first sequence and modify:Step Name: for example, Installment Plan: Posting ApprovalStep Type: Installment Plan: Posting ApprovalChoose the Recipients tab:Assignment By: Team (For example)Team: Select the team you create in previous stepChoose the Step Conditions tab: (Optional)Choose the Exception Handling tab:Name: Installment Plan was rejectedRequired Action: Installment Plan: Rejection NotificationAction result: Cancel workflow | You saved the workflow. |  |
| 7 | Activate Rule | Choose Apply, then choose Save and Activate.Note The template workflow is delivered by default as active with no preconditions defined, which means this workflow will always start. Make sure you've deactivated the standard template if you don’t want to use it before you start to post your Installment Plan. | The workflow of installment plan posting is activated. |  |

#### Post Installment Plan

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Context

After completing all the prerequisite steps and setting the start conditions with Installment Plan category set as 01 and number of installment plans is greater than 10 in the Define and Activate Your Approval Workflows step, you can post an installment plan to start the workflow. Once the start conditions of posting installment plan are met, the workflow starts, the system automatically sets the check reason in document header and a new item is sent to recipient’s Inbox as well as the notification list for actions. To post the installment plan document, confirmation from approver is required for further processing (change, etc) according to your check reason settings in SSCUI (103740). If the installment plan document is released by approver, the check reason is automatically removed from the document header and the installment plan can go for further processing.

Procedure

In this activity, to trigger the workflow, you post an installment plan document with installment plan category set as 01 and number of installment plans is greater than 10.

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Collections Specialist (FI-CA). |  |  |
| 2 | Access App | Open Maintain Installment Plan (FPR3). | Display Installment Plan: Initial Screen displays. |  |
| 3 | Create Installment Plan | Choose Create. | Create Installment Plan: Initial Screen displays. |  |
| 4 | Maintain Parameters | Make the following entries:Business Partner: <Required Business Partner>Contract Account: <Required Business Partner>Currency: AEDPosting Date: <Today's date>Document Date: <Today's date>Doc Type: Inst Plan: YADoc. Type: Charges: YAReconciliation Key: <Reconciliation Key generated by system> |  |  |
| 5 | Save | Choose Continue. | Create Installment Plan: Select Items and Enter Parameters Initial Screen displays. |  |
| 6 | Select Items | In the Item Selection section, select the items for the installment plan. |  |  |
| 7 | Maintain Installment Plan Parameters | In the Installment Plan Parameters section, make the following entries:Inst. Plan Type: SAEStart Date: <Today's date> |  |  |
| 8 | Propose | Choose Propose. | Create Installment Plan: Define Installments screen display. |  |
| 9 | Save | Choose Save. | The installment plan is created. |  |

#### Verify Installment Plan Document

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you can verify a document blocked by installment plan workflow.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Collections Specialist (FI-CA). |  |  |
| 2 | Access App | Open Maintain Installment Plan (FPR3). | Create Installment Plan: Initial Screen displays. |  |
| 3 | Select Installment Plan | Make the following entry and choose Continue:Install. Plan No.: <Installment plan document posted in previous step> |  |  |
| 4 | Switch to Change Mode | Choose Edit and Continue. | The message Installment plan XXX is in workflow; only display is possible is displayed.Note You have this message because you've selected No Changes in your check reason 03. |  |

#### Approve Installment Plan Document (for Processor - Inbox)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Context

You receive installment plan documents that need to be checked. After checking the installment plan detailed information, you can either release or reject the document with a comment or reason. Once the work item has been selected and released, it disappears from the list. If a document is released or approved, the released or approved installment plan can go for further processing.

|  |
| --- |
| Note You can set a substitute when you are absent and could not access your Inbox. To do so, go to My Inbox and find the Substitute function from your profile. |

Purpose

In this activity, you access Inbox as an approver and release the document.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Accounts Payable and Receivable Manager (FI-CA). |  |  |
| 2 | Access App | Open My Inbox for Contract Accounting - All Items (F5136). |  |  |
| 3 | Approve Documents | Select the document to be released.Choose Approve. | The document is released.Note All released documents are displayed in the My Outbox - Outbox items app.Message Confirm Installment Plan with Check Reason Installment Plan approve disappears. |  |

#### Reject Installmen Plan Document (for Processor - Inbox)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Context

You receive posted installment plan documents that need to be checked. After checking the detailed information of installment plan documents, you can either approve or reject the document with a comment or reason. Once an installment plan has been selected and rejected, it disappears from the list and goes back to the requester.

Purpose

In this activity, you access Inbox as an approver and reject the document.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Accounts Payable and Receivable Manager (FI-CA). |  |  |
| 2 | Access App | Open My Inbox for Contract Accounting - All Items (F5136). | The My Inbox view displays. |  |
| 3 | Reject Installment Plan | Select the installment plan item to be rejected.Choose Reject and enter the reason for rejection.For example: The amount is not correct, please deactivate the Installment Plan. | The installment plan is rejected. |  |

#### Deactivate a Rejected Installment Plan Document (Requester)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Context

The installment plan document must be approved before final release. If the document you submitted is rejected, you can choose one of below steps to complete your workflow item so that it can be deactivated or resent back for approval.

Purpose

In this activity, you access Inbox as a requester and deactivate the rejected installment plan document.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Collections Specialist (FI-CA). |  |  |
| 2 | Access App | Open My Inbox for Contract Accounting - All Items (F5136). | The My Inbox view displays. |  |
| 3 | Reverse Documents | Select the document to be deactivated.Choose Deactivate.Note The installment plan document status is changed to Deactivated automatically. | The rejected installment plan document is deactivated. |  |

#### Resend a Rejected Installment Plan Document (Requester)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you access Inbox as a requester, make a note and resend it to approver.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Collections Specialist (FI-CA). |  |  |
| 2 | Access App | Open My Inbox for Contract Accounting - All Items (F5136). | The My Inbox view displays. |  |
| 3 | Repeat Approval | Select the document to be resent.Choose Restart.In the Submit Decision view:Decision Note: <Your reason for repeat approval>Choose Submit. | The installment plan document is submitted for approval again.Note Once the document is submitted, approval cycle will restart. |  |

### Interest Calculation

#### Post Interest

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this process step, you calculate interests manually.

Prerequisite

Depending on your configuration environment for SAP S/4HANA Cloud, choose one of the following options:

Configure Your Solution:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. |  |  |
| 2 | Access App Manage Your Solution | Open Manage Your Solution and choose Configure Your Solution. | The Manage Your Solution screen is displayed. |  |
| 3 | Access Define Interest Calculation Rules | Search with following criteria:Application Area: FinanceSub Application Area: Contract AccountingChoose Interest.Choose the configuration step: Define Interest Calculation Rules.Choose Configure. | The Change View "Define Interest Calculation Rules: Change: Details": screen is displayed. |  |
| 4 | Double-click Interest Conditions | Select an entry:Currency: AEDDebit: S |  |  |
| 5 | Double-click Time-dependent Interest Terms | Valid from: 01/01/2000Surcharge: 5Choose Save. |  |  |

SAP Central Business Configuration:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the project experience in SAP Central Business Configuration. | The SAP Fiori launchpad is displayed. |  |
| 2 | Open Set Up Company Codes for Contract Accounts Receivable and Payable | Go to the Business Processes Configuration app and search for the following activity: Define Interest Calculation Rules.Choose Open Documentation for the found line item to see more details about this configuration activity.Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. | The Change View "Define Interest Calculation Rules: Change: Details": screen is displayed. |  |
| 3 | Double-click Interest Conditions | Select an entry:Currency: AEDDebit: S |  |  |
| 4 | Double-click Time-dependent Interest Terms | Valid from: 01/01/2000Surcharge: 5Choose Save. |  |  |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Collections Specialist (FI-CA). |  |  |
| 2 | Access App | Open Post Interest (FPI1). | The Calculate Interest Individually screen displays. |  |
| 3 | Maintain Parameters | Make the following entries in the Line Item Selection section:Business Partner: <Required Business Partner>Contract Acct: <Required Contract Account>Currency: AED |  |  |
| 4 | Enter | Choose the Debit and Credit Items radio button.Choose the Line Items button. |  |  |
| 5 | Select | Choose at least one line item. |  |  |
| 6 | Choose the Item for Interest Calculation | Choose More in the menu and select Save + Create Letter or choose Post. | Choose Save Create Letter, interest document is posted and interest notification is created.Choose Post, interest document is posted. |  |

#### Print Interest Notification

##### Print Correspondence

Purpose

In this activity, you print the interest notification correspondence.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Administrator - Accounts Payable and Receivable (FI-CA). |  |  |
| 2 | Access App | Open Print Correspondence (F3537). | The Application Jobs screen displays. |  |
| 3 | Create New Job | Choose Create. |  |  |
| 4 | Enter Required Parameters | Make the following entries and choose Step 2:Job Template: FI-CA: Print CorrespondenceJob Name: FI-CA: Print Correspondence |  |  |
| 5 | Enter Required Parameters | Make the following entry:Start Immediately: SelectedChoose Define Recurrence Pattern.Recurrence Pattern: <Select Single Run>Note For recurrence setting, select recurrence time cycle.Choose Step 3. |  |  |
| 6 | Enter Required Parameters | Make the following entries:Run SettingsRun ID Prefix: For example, ID0Selection CriteriaBusiness Partner: <Select business partner number>Contract Account: <Select contract account number>Company Code: 3310Correspondence Type: <Select 0007 Interest Notification>Print ParametersActual Print: Selected |  |  |
| 7 | Check Job | Choose Check. | System message You can go ahead and schedule the job displays. |  |
| 8 | Execute Job | Choose Schedule. | The Application Jobs screen displays.One new application job is created with a status. |  |
| 9 | Display Job Details | After the job has been finished, choose the arrow button at the end of the entry to navigate to the job details. | The Job Log screen displays. The log should show no errors.Note The Run Identification should combine Run ID Prefix + dynamic number (xx). |  |

##### Display Correspondence History

Purpose

In this activity, you display the correspondence history.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Accounts Payable and Receivable Accountant (FI-CA). |  |  |
| 2 | Access App | Open Display Correspondences (F3693). | The Display Correspondences screen displays. |  |
| 3 | Search Criteria | Enter required parameters for search criteria. |  |  |
| 4 | Execute | Choose Go. | The correspondence details are listed. |  |
| 5 | Display | Select an entry to display. | Details of this entry are shown. |  |

#### Display Interest Calculation

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this process step, you display the interest calculation for an interest document.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Accounts Payable and Receivable Accountant (FI-CA). |  |  |
| 2 | Access App | Open Display Interest Calculations (F4761). | The Display Interest Calculations screen displays. |  |
| 3 | Enter Search Criteria | Make any of the following search criteria and choose Go:Document: <Select Interest Document>Business Partner: <Select Business Partner>Interest Run ID: <Select Contract Account> | The relevant interest document is displayed in the Interest documents section. |  |
| 4 | View Interest Document Details | To view interest document details, select the interest document and choose the arrow button to the right of its row. | Brief information of interest document is shown on the left panel and details are shown on the right panel. |  |

#### Execute Interest Run

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this process step, you post interests automatically by executing the interest run.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Administrator - Accounts Payable and Receivable (FI-CA). |  |  |
| 2 | Access App | Open Interest Run (F3527). | The Application Jobs screen displays. |  |
| 3 | Create New Job | Choose Create. |  |  |
| 4 | Enter Basic Parameters | Make the following entries and choose Step 2:Job Template: FI-CA Interest RunJob Name: FI-CA Interest Run |  |  |
| 5 | Enter Basic Parameters | Make the following entry and choose Step 3:Start Immediately: Selected |  |  |
| 6 | Enter Basic Parameters | Make the following entries:Run SettingsRun ID Prefix: For example, ID0Simulation run: UnselectedSelection CriteriaBusiness Partner: <Select Business Partner>Contract Account: <Select Contract Account>Currency: AEDParametersCalc.Int. on Dr/Cr Items: SelectedAll Items: SelectedCreate Correspondence: Selected |  |  |
| 7 | Check Job | Choose Check. | Message You can go ahead and schedule the job displays. |  |
| 8 | Execute Job | Choose Schedule. | The Application Jobs screen displays.One new application job is created with a status. |  |
| 9 | Display Job | Choose the arrow button at the end of the entry to navigate to the job details. | The Job Log screen displays.The Run Identification should combine Run ID Prefix + dynamic number (xx). |  |

### Interest Calculation on Clearing

#### Interest Calculation on Clearing

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The system can check open items and calculate interest during clearing as needed, offering two interest calculation options. One option calculates interest on the full open receivable amount during clearing, which is available only with SAP Fiori Apps: Process Payment Lot (FP05), Maintain Accounts (FP06), and Maintain Accounts Run (F3531), and requires that the IntCalc. of Receivable on Clearing indicator is enabled in the configuration activity for setting up company codes for contract accounts receivable and payable.

In this activity, you activate the Interest Calculation on Clearing function for the company code. Once activated, interest can be calculated and posted automatically during the clearing process.

Prerequisite

1. Complete the prerequisite settings described in the Interest Calculation chapter.
2. Assign the interest key to the contract account master data.
3. Ensure that overdue open receivable documents are available.
4. Activate the Interest Calculation of Receivable Amount on Clearing setting for your company code.

Depending on your configuration environment for SAP S/4HANA Cloud Public Edition, choose one of the following options:

Configure Your Solution:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access App Manage Your Solution | Open Manage Your Solution and choose Configure Your Solution. | The Manage Your Solution screen is displayed. |  |
| 3 | Open Set Up Company Codes for Contract Accounts Receivable and Payable | Search with following criteria:Application Area: FinanceSub Application Area: Contract AccountingChoose Organization.Search for the configuration step: Set Up Company Codes for Contract Accounts Receivable and Payable, and choose Configure. | The Change View "Company Codes in Contract Accounts Receivable and Payable": Overview screen is displayed. |  |
| 4 | Select Entries for Company Codes | Select an entry for company code 3310.In the Settings for Further Business Proceses section, make the following entry:IntCalc.of Reveivable on Clearing: <select>Save the entry.Note If the Interest on Receivables for Clearing indicator is set in the customizing activity 101239 –Set Up Company Codes for Contract Accounts Receivable and Payable, ensure the Interest on Clearing Amount for Clearing indicator is not set in the customizing activity 102218 – Maintain Central Settings for Posting, and vice versa. | Check the entries by going again into the configuration activity. |  |

SAP Central Business Configuration:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the project experience in SAP Central Business Configuration. | The SAP Fiori launchpad is displayed. |  |
| 2 | Open Set Up Company Codes for Contract Ac-counts Receivable and Payable | Go to the Business Processes Configuration app and search for the following activity: Set Up Company Codes for Contract Accounts Receivable and Payable.Choose Open Documentation for the found line item to see more details about this configuration activity.Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. | The Change View "Company Codes in Contract Accounts Receivable and Payable": Overview screen is displayed. |  |
| 3 | Select Entries for Company Codes | Select an entry for company code 3310.In the Settings for Further Business Proceses section, make the following entry:IntCalc.of Reveivable on Clearing: <select>Save the entry.Note If the Interest on Receivables for Clearing indicator is set in the customizing activity 101239 –Set Up Company Codes for Contract Accounts Receivable and Payable, ensure the Interest on Clearing Amount for Clearing indicator is not set in the customizing activity 102218 – Maintain Central Settings for Posting, and vice versa. | Check the entries by going again into the configuration activity. |  |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Accounts Payable and Receivable Accountant (FI-CA). |  |  |
| 2 | Access App | Open Maintain Accounts Run (F3531). | The Application Jobs screen displays. |  |
| 3 | Create New Job | Choose Create. |  |  |
| 4 | Enter Basic Parameters | Make the following entries and choose Step 2:Job Template: FI-CA: Automatic ClearingJob Name: FI-CA: Automatic Clearing |  |  |
| 5 | Enter Basic Parameters | Make the following entry and choose Step 3:Start Immediately: Selected |  |  |
| 6 | Enter Basic Parameters | Make the following entries:Run IdentificationRun ID Prefix: For example, ID0General SelectionsBusiness Partner: <Select Business Partner>Contract Account: <Select Contract Account>Company Code: 3310To Net Due Date: <Today’s date>Posting Parameters:Clearing Reason: Automatic Clearing (15)Document Type: YAPosting Date: <Today’s date>Document Date: <Today’s date> |  |  |
| 7 | Check Job | Choose Check. | Message You can go ahead and schedule the job displays. |  |
| 8 | Execute Job | Choose Schedule. | The Application Jobs screen displays.One new application job is created with a status. |  |
| 9 | Display Job | Choose the arrow button at the end of the entry to navigate to the job details. | The Job Log view is displayed. The log should show detailed information about the interest posting.Note down the clearing document number, as it will be used in the next step.Note The Run Identification should combine Run ID Prefix + dynamic number (xx). |  |

#### Display Interest Supplement

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you display the interest supplement in the clearing document.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Accounts Payable and Receivable Accountant (FI-CA). |  |  |
| 2 | Access App | Open Display Document (FPE3). | The Display Document: Initial Screen screen displays. |  |
| 3 | Enter Data | Make the following entry:Document Number: <Use the clearing document number from the previous step> |  |  |
| 4 | Execute | Press Enter. | Details of the document are listed. |  |
| 5 | Navigate to Details | Select Extras > Interest Supplement .On the new screen appears, the detailed information for the interest supplement is displayed. |  |  |

### Credit Clarification

#### Create Credit List

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you place the credits in clarification processing via the SAP Fiori app Create Credit List (F3526). Then you are able to clarify existing credits systematically.

Prerequisite

Before you execute Create Credit List and Process Credits, maintain Define Selection Criteria for Credit Clarification via SSCUI as below, then do Post Document.

1. Define Selection Criteria for Credit Clarification

Depending on your configuration environment for SAP S/4HANA Cloud Public Edition, choose one of the following options:

Configure Your Solution:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. |  |  |
| 2 | Access App Manage Your Solution | Open Manage Your Solution and then choose Configure Your Solution. | The Manage Your Solution screen is displayed. |  |
| 3 | Access App Define Selection Criteria for Credit Clarification | Search with following criteria:Application Area: FinanceSub Application Area: Contract AccountingChoose the group Credit.Choose the configuration step Define Selection Criteria for Credit Clarification and choose Configure. | The Change View "Credit Processing: Customizing ID Credit ": Overview screen is displayed. |  |
| 4 | Add Entries for Company Codes | Choose New Entries and add an entry for company code.Company Code: 3310Main Transaction: <Main Transaction, for example, Y600>Sub Transaction: <Sub Transaction, for example, 0010>Currency: AEDSave the entry. | Check the entries by accessing the SSCUI again. |  |

SAP Central Business Configuration:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the project experience in SAP Central Business Configuration. |  |  |
| 2 | Open Define Selection Criteria for Credit Clarification | Go to the Business Processes Configuration app and search for the following activity: Define Selection Criteria for Credit Clarification.Choose Open Documentation for the found line item to see more details about this configuration activity.Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. | The Change View "Credit Processing: Customizing ID Credit ": Overview screen is displayed. |  |
| 3 | Input Parameters | Choose New Entries and add an entry for company code.Company code: 3310Main Transaction: <Main Transaction, for example, Y600>Main Transaction: <Sub Transaction, for example, 0010>Currency: AEDSave the entry. | Entries for company codes added. |  |

2. To post open credits (Transaction.: Y600/0010), see the Process Credits step.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Administrator - Accounts Payable and Receivable (FI-CA). |  |  |
| 2 | Access App | Open Create Credit List (F3526). | The Application Jobs view displays. |  |
| 3 | Create New Job | Choose Create. |  |  |
| 4 | Enter Basic Parameters | Make the following entries and choose Step 2:Job Template: FI-CA: Create Credit ListJob Name: FI-CA: Create Credit List |  |  |
| 5 | Enter Basic Parameters | Make the following entry and choose Step 3:Start Immediately: Selected |  |  |
| 6 | Enter Basic Parameters | Make the following entries:Run IdentificationRun ID Prefix: For example, ID0General SelectionsBusiness Partner: <Select Business Partner>Contract Account: <Select Contract Account>Company Code: 3310 |  |  |
| 7 | Check Job | Choose Check. | System message You can go ahead and schedule the job displays. |  |
| 8 | Execute Job | Choose Schedule. | The Application Jobs view displays.One new application job is created with a status. |  |
| 9 | Check Job Status | Choose the arrow button at the end of the entry to navigate to the job details. | The Job Log view displays. The log should show no errors.Note The Run Identification should combine Run ID Prefix + dynamic number (xx). |  |

#### Clarify Credits

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you systematically clarify the existing credits that are part of the credit list created in the previous step.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Collections Specialist (FI-CA). |  |  |
| 2 | Access App | Open Clarify Credits (FPCRPO). | The Select. Screen: Credit view displays. |  |
| 3 | Enter Selection Parameter | Make the following entry in the Clarification Worklist Credit section:Business Partner: <Required Business Partner> |  |  |
| 4 | Enter | Choose Execute. | The Worklist: Credit screen displays. |  |
| 5 | Select Credit | Select one entry from the Clarification Cases list and choose Clarify. | The Detailed Information on Application Item screen displays. |  |
| 6 | Process Credits | Process credits by one of the following ways:TransferPayRemainClearingBusiness Partner TransferG/L TransferWriting OffReturn to ClarificationTo executing transfer, pay, clearing, you could refer to next step Process Credit. |  |  |

#### Process Credits

SAP Fiori app Process Credits (FPTCRPO) is recommended to manually process individual credits that are not entered by the credit list. It offers the following functions:

Transfer: You can transfer the credit in full or part of it to any bank account, even if the master data of this account does not exist in your system, that is, the owner of the bank account is not a business partner.

Pay: You can pay out in full or in part of the credit to another business partner.

Writing Off: You can write off the credit in full to a G/L account.

Clearing: You can clear the credit in full or as a partial amount with another item from the same business partner, contract account, or provider contract (account maintenance).

Business Partner Transfer: You can transfer the credit in full or in part to another business partner, another contract account or another provider contract.

General Ledger Transfer: If the credit is to be assigned to a different department, you can clear the credit and make a transfer posting to a different G/L account.

In this test script, only the most important functions are displayed, which are Transfer, Pay and Clearing.

Prerequisite

Make sure you have posted open credits for a business partner, please refer to the Post Documents step.

##### Transfer Credits

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

You can transfer the entire credit or a portion of it to any bank account, regardless of whether the account's master data exists in your system. This applies even if the bank account owner is not a business partner. Once the transfer is initiated, a repayment request will be generated. To process these repayment requests, use the payment run feature by selecting the Repayment Requests indicator.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Collections Specialist (FI-CA). |  |  |
| 2 | Access App | Open Process Credits (FPTCRPO). | Credit: Initial Screen displays. |  |
| 3 | Enter Selection Parameter | Make the following entry and choose Continue:Business Partner.: <Required Business Partner> | The list shows the existing credit items. |  |
| 4 | Select Credit | Select one entry and double-click it. | The Credit: Processing screen displays. |  |
| 5 | Enter Parameter | On the Transfer tab, make the following entries:Payment Method: <For example, T>Bank Number: <Required Bank Number>Bank Account: <Required Bank Account>Bank Country: <Required Country>Account Holder: <Bank account holder>IBAN: <Required IBAN>Note Fill in IBAN or choose Generate IBAN from Bank Data to generate IBAN automatically.Press Enter to refresh if Generate IBAN from Bank Data is grayed out after you input all the information above.SWIFT/BIC: <Required SWIFT/BIC> |  |  |
| 6 | Enter | Choose the Pay button. | The Credit: Processing screen displays. |  |
| 7 | Enter Parameter | In the Details of Recipient of Repayments dialog box, make the following entries:First Name: <Required First Name>Last Name: <Required Last Name>House No: <Required House No.>Street: <Required Street>Post Code: <Required Post Code>City: <Required City>Country: <Required Country> |  |  |
| 8 | Enter Continues | Choose Continue. |  |  |

##### Pay Out Credits

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this process step, you manually pay the credit(s) back to the business partner.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Collections Specialist (FI-CA). |  |  |
| 2 | Access App | Open Process Credits (FPTCRPO). | The screen Credit: Initial Screen displays. |  |
| 3 | Enter Selection Parameter | Make the following entry and choose Continue:Business Partner.: <the required Business Partner> | The list shows the existing credit items. |  |
| 4 | Select Credit | Select one entry and double-click it. |  |  |
| 5 | Enter Parameter | On the Pay tab, make the following entries:Payment Method: <Choose Payment Method>Partner: <Choose the required Business Partner>Bank Detail: <Choose the required Bank Detail> |  |  |
| 6 | Enter | Choose Pay. |  |  |

##### Clear Credits with Open Items

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this process step, you manually clear the entered (partial) amounts of all selected items against the open items of the business partner.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Collections Specialist (FI-CA). |  |  |
| 2 | Access App | Open Process Credits (FPTCRPO). | The screen Credit: Initial Screen displays. |  |
| 3 | Enter Selection Parameter | Make the following entry and choose Continue:Business Partner.: <Required Business Partner> | The list shows the existing credit items. |  |
| 4 | Select Credit | Select one entry and double click it. | The screen Credit:Processing displays. |  |
| 5 | Enter | On the clearing tab, choose Partner. | The screen Credit Processing: Process Open Items displays. |  |
| 6 | Select Clearing Item | Select one offset item and click the Active Item icon. Check or maintain the Gross Clearing field to make sure amount difference is 0. If required, you could also choose the icon Select Further Item to narrow down your selection of open items. |  |  |
| 7 | Enter | Choose Post. |  |  |

### Creditworthiness

#### Display Creditworthiness

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this process step, creditworthiness of a business partner provides information on the business partner’s payment history. A creditworthiness of zero means that the business partner has an excellent payment history and the maximum value is 9999. Once you have maintained one of the following prerequisites, you can implement relevant business transactions, such as dunning, write-offs, returns and installment plans. After that, creditworthiness will be updated in the system automatically.

Prerequisite

Before you execute Manage Creditworthiness, execute at least one of the following prerequisites as below.

Case 1: Update creditworthiness score by dunning

To do so, refer to the Execute Dunning Proposal Run step and Execute Dunning Activity Run step.

Case 2: Update creditworthiness score by write-offs

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Accounts Payable and Receivable Accountant (FI-CA). | The SAP Fiori launchpad is displayed. |  |
| 2 | Access App | Open Write Off Items (FP04). | The Write Off Items screen is displayed. |  |
| 3 | Enter Selection Details | Make the following entries:Business Partner: <Business Partner Number with Open Items>Contract Account: <Contract Account Number with Open Items>Document Number: <Document with Open Items> |  |  |
| 4 | Enter Specifications for Write-Off | Make the following entries:Posting Date: <Today's Date>Currency: AEDClearing Reason: 04Write-Off Reason: Y1Document Type: YAReconciliation Key: <Reconciliation Key generated by system> |  |  |
| 5 | Select Open Items | Choose Select Online. | The Checking reconciliation key screen appears. |  |
| 6 | Create Reconciliation Key | Choose Yes. | A new Reconciliation Key is created. |  |
| 7 | Continue to Write Off | Choose Continue. | The Write Off: Process Open Items screen is displayed. |  |
| 8 | Activate Items | Select open items to write off by choosing the Activate item button.Alternatively, double-click on the gross amount to activate a specific item for write-off. | The selected open items have been activated. The activated write off amount is displayed in the Gross Clearing field. |  |
| 9 | Post | Choose Post. | The write off documents are posted. |  |

Case 3: Update creditworthiness score by returns

1. Make a payment for receivable

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Accounts Payable and Receivable Accountant (FI-CA). |  |  |
| 2 | Access App | Open Process Payment Lot (FP05). | Payment Lot: Initial Screen displays. |  |
| 3 | Input Parameters for Payment Lot | Create your payment lot ID and choose Create:Lot: <Your payment lot ID>Make the following entries on the Payment Lot Create: Default Entries and Status screen:Control Information:Lot: <Your payment lot ID>Search Term: <Input your search information>Additional Info: <Input your specific information>Specifications for Posting Documents:Document Type: <by default>Posting Date: <by default>Document Date: <by default>Reconciliation Key: <Generated by the system>Currency: AEDSpecification for Posting Items on Bank Clearing Account:Bank Clearing Account: 11001080Company Code: 3310House Bank: AEBK2Account ID: AEAC2Value Date: <Today's date>Selections for Selecting and Clearing Open Items:Clearing Reason: <01, by default>Selection Category: <by default>Line Layout: SAPClick New Items.On the Payment Lot Create: Payments screen, check and make the following entries:In the Default Value and Status section: <Values are maintained by default>In the Payments section:Payment Amount: <Input the amount>Selection Category: BNote Category B stands for Document.If parameters you input are in accordance with the open items, the payment lot can clear open items of specific business partner, otherwise, it needs further clarification.Selection Value 1: <Input your document generated in the Create Cash Deposit Request step>Click Save. | Payment lot is created. |  |
| 4 | Post Payment Lot | Input your payment lot ID on the Payment Lot: Initial Screen.Lot: <Your payment lot ID>Choose Close.Note Payment lot must be closed before it can be posted.Choose Yes when message appears: All payment entered in full?Choose Post.In the Schedule Job dialog box, choose Start online and choose OK.Choose Continue when message appears: Posting run is complete, check status.In the Status section, system shows the posting status.Postprocessing is required means the payment needs further clarification. | Payment lot is closed and posted. |  |

1. Return payment

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Accounts Payable and Receivable Accountant (FI-CA). | The SAP Fiori launchpad is displayed. |  |
| 2 | Access App | Open Process Returns Lot (FP09) | Returns: Request Screen is displayed. |  |
| 3 | Enter Return Lot ID | Make the following entry:Returns Lot: Example: ReturnLot001 |  |  |
| 4 | Create | Choose More > Return lot > Create . | The Returns: Specification and Status Display screen is displayed. |  |
| 5 | Maintain Specifications and Status | Company Code: 3310Currency: AEDChoose New Items. |  |  |
| 6 | Input Items | Selection Value: payment document number generated in payment run and check the Returns amount with the payment document.Return reason: Y02Bank Clrg Acct: <Choose bank clearing account>Choose Save.If you want to check the Clarifications of Returns Lot, you could input * in Selection Value. | The Returns: Display line items screen is displayed. |  |
| 7 | Close Returns Lot | Go back to Return Lot: Specification and Status display screen.Choose Close. | The Close lot screen appears. |  |
| 8 | Confirm | Choose Yes. | The return lot is closed.The Returns: Request Screen is displayed again. |  |
| 9 | Post Returns Lot | Choose Post. | The Schedule Job screen is displayed. |  |
| 10 | Start Online | Choose Start online. | The return lot is posted successfully. |  |

Case 4: Update creditworthiness score by installment plan

To do so, refer to the Create Installment Plan step.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Accounts Payable and Receivable Accountant (FI-CA). |  |  |
| 2 | Access App | Open Manage Creditworthiness (F4408). | The Manage Creditworthiness screen displays. |  |
| 3 | Display Creditworthiness | Make the following entry:Business Partner: <the required Business Partner> | The selected Business Partner Creditworthiness is displayed, click right arrow to view details. |  |
| 4 | Enter | Choose Go. | The Creditworthiness is displayed |  |

### Security Deposit

#### Create Cash Deposit Request

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this process step, you manually create a cash security deposit request.

Prerequisite

Make sure you have maintained necessary reasons for requesting a security deposit by implementing following steps before you create cash deposit request:

Depending on your configuration environment for SAP S/4HANA Cloud Public Edition, choose one of the following options:

Configure Your Solution:

Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration.

Open Manage your solution APP, search for Define Request Reasons for Securities (SSCUI ID: 103395), and add reason needed:

| Reason | Text |
| --- | --- |
| Z001 (example) | New Customer |

You could also create necessary Reversal Reasons for Security Deposits through configuration activity: Define Reversal Reasons for Security Deposits (SSCUI ID: 103396).

| Reason | Text |
| --- | --- |
| Z001 (example) | Created in Error |

SAP Central Business Configuration:

Log on to the project experience in SAP Central Business Configuration.

Go to the Business Processes Configuration app. You can search for Define Request Reasons for Securities and navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration (SAP_BR_BPC_EXPERT).

Add reason needed:

| Reason | Text |
| --- | --- |
| Z001 (example) | New Customer |

You could also create necessary Reversal Reasons for Security Deposits through configuration activity: Define Reversal Reasons for Security Deposits.

| Reason | Text |
| --- | --- |
| Z001 (example) | Created in Error |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Accounts Payable and Receivable Accountant (FI-CA). |  |  |
| 2 | Access App | Open Manage Security Deposits (F4415). | The Manage Security Deposit screen displays. |  |
| 3 | Create Security Deposit | Choose Create. |  |  |
| 4 | Enter Selection Parameter | Make the following entries:Contract Account: <Contract Account>Request Reason: <Choose the reason for request>, please refer to the Prerequisite section.Request Amount: <Amount>Note You could input interest key, for example, 01, if interest needs to be calculated. |  |  |
| 5 | Save | Choose Create.Note As long as the request document has not yet been cleared, you can reverse the security deposit. A deposit that has been reversed cannot be used again.On the Manage Security Deposits screen, choose Reverse.Note You can create a similar security deposit request based on a existing one by choosing Copy. | The created security deposit is displayed. |  |

#### Print Security Deposit

##### Print Correspondence

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

If you want to print the security deposit, please make sure the status is requested. The correspondence printing run determines the correspondence data that has been stored in the Correspondence.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Accounts Payable and Receivable Accountant (FI-CA). |  |  |
| 2 | Access App | Open Manage Security Deposits (F4415). | The screen Manage Security Deposits is displayed. |  |
| 3 | Print Security Deposit | Select the security deposit to be printed.Click Create Correspondence.In the Create Single Correspondence dialog box, choose the Dispatch Control you want, for example, only printout.In the Unique ID e.Queue field, select the DEFAULT Print Queue via the value help icon.Then choose Create and Print. |  |  |

##### Display Correspondence

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Context

In this activity, you display correspondence details.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Accounts Payable and Receivable Accountant (FI-CA). |  |  |
| 2 | Access App | Open Manage Security Deposits (F4415). | The screen Manage Security Deposit Screen is displayed. |  |
| 3 | Print Security Deposit | Choose the security deposit that has been printed in previous step and go to the detailed page.Click Correspondence.Choose Display Correspondence. |  |  |

#### Receive Cash Security Deposit Payment

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

If you receive a (partial) cash security deposit payment and this clears the request document either completely or partially, the status changes to (Partially) Paid.

If the security deposit is partially paid, you could select the security deposit and choose Clear to reverse the rest not yet received.

Procedure

1. Process payment lot:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Accounts Payable and Receivable Accountant (FI-CA). |  |  |
| 2 | Access App | Open Process Payment Lot (FP05). | Payment Lot: Initial Screen displays. |  |
| 3 | Input Parameters for Payment Lot | Create your payment lot ID and choose Create:Lot: <Your payment lot ID>Make the following entries on the Payment Lot Create: Default Entries and Status screen:Control Information:Lot: <Your payment lot ID>Search Term: <Input your search information>Additional Info: <Input your specific information>Specifications for Posting Documents:Document Type: <by default>Posting Date: <by default>Document Date: <by default>Reconciliation Key: <Generated by the system>Currency: AEDSpecification for Posting Items on Bank Clearing Account:Bank Clearing Account: 11001080Company Code: 3310House Bank: AEBK2Account ID: AEAC2Value Date: <Today's date>Selections for Selecting and Clearing Open Items:Clearing Reason: <01, by default>Selection Category: <by default>Line Layout: SAPClick New Items.On the Payment Lot Create: Payments screen, check and make the following entries:In the Default values and status section: <Values are maintained by default>In the Payments section:Payment Amount: <Input the amount>Selection Category: <Select B>Note Category B stands for Document.If parameters you input are in accordance with the open items, the payment lot can clear open items of specific business partner, otherwise, it needs further clarification.Selection value1: <Input your document generated in the Create Cash Deposit Request step>Click Save. | Payment lot is created. |  |

1. Post payment lot:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Accounts Payable and Receivable Accountant (FI-CA). |  |  |
| 2 | Access App | Open Process Payment Lot (FP05). | Payment Lot: Initial Screen displays. |  |
| 3 | Post Payment Lot | Input your payment lot ID on the Payment Lot: Initial Screen.Lot: <Your payment lot ID>Choose Close.Note Payment lot must be closed before it can be posted.Choose Yes when message appears: All payment entered in full?Choose Post.In the Schedule Job dialog box, choose Start online and choose OK.Choose Continue when message appears: Posting run is complete, check status.In the Status section, system shows the posting status.Postprocessing is required means the payment needs further clarification. | Payment lot is closed and posted. |  |

#### Release Security Deposit

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

When the return date is reached, or when an early manual release occurs, the system changes the status to Released.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Accounts Payable and Receivable Accountant (FI-CA). |  |  |
| 2 | Access App | Open Manage Security Deposits (F4415). | The screen Manage Security Deposit Screen is displayed. |  |
| 3 | Enter Selection Parameter | Make the following entry:Contract Account.: <Contract Account>Choose Go. | The existing security deposits are displayed. |  |
| 4 | Release | Select the security deposit and select Partially Release or Fully Release the amount you want. If needed, you may select Reset Release to revert the release.You could click the security deposit and check the document flow for more details about the status. | The security deposits status updated to Released. |  |

#### Return Security Deposit

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

If the cash security deposit payment is cleared by repayment or settlement against open receivables, the end status Returned is reached.

For how to do a repayment/outgoing payment to business partner, refer to the Contract Accounting – Company Initiated Payments (2DP) test script, step Execute Payment Run to do outgoing payment for the security deposit.

You could also use account maintenance to manually clear by executing the Account Maintenance: Process Open Items step in this test script.

|  |
| --- |
| Note Security Deposit status will be updated to Returned. |

Here is an example for outgoing payment to business partner.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Administrator - Accounts Payable and Receivable (FI-CA). |  |  |
| 2 | Access App | Open Payment Run / Debit Memo Run (F3529). | The Application Jobs screen displays. |  |
| 3 | Create New Job | Choose Create. | The New Job view displays. |  |
| 4 | Maintain Parameters | Make the following entries and choose Step 2:Job Template: FI-CA Payment RunJob Name: FI-CA Payment Run |  |  |
| 5 | Maintain Parameters | Make the following entry and choose Step 3:Start Immediately: Selected |  |  |
| 6 | Maintain Parameters | Make the following entries:Post Date: <Today's Date>Run SettingsRun ID Prefix: For example, ID0Simulation run.: UnselectedSelection CriteriaOpen Items: SelectedBusiness Partner: <Select Business Partner>Contract Account: <Select Contract Account>Company Code: 3310Due by: <Today's Date + 1 Year>Payment Method List: 0001Country Key: AEFurther SettingsSelection ID: 3310 |  |  |
| 7 | Check Job | Choose Check.Note The Dynamic Date Function is available for parameters of date, you can also use the Dynamic Date Function with the Define Recurrence Pattern to set up the recurring run for mass activity to meet your business needs. For example, you can choose the dynamic date function TODAY for testing purpose. | System message You can go ahead and schedule the job is displayed. For credit card outgoing payment, after execute payment run generated clearing document, please refer to the Payment Card Settlement step in the Contract Accounting – Customer Initiated Payments(2BI) test script. |  |
| 8 | Execute Job | Choose Schedule. | The Application Jobs screen is displayed. One new application job is created with a status. Payment documents are created from job log details. |  |
| 9 | Check Job Status | After the job has been finished, choose the arrow button at the end of the entry to navigate to the job details. | The Job Log screen is displayed. The log should show no errors.The Run Identification should combine Run ID Prefix + dynamic number (xx). |  |

#### Cash Security Deposit Interest Calculation (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you can post cash security deposit interest document. Note that if you want to post the interest of one cash security deposit, you need to maintain the interest key in the Create Cash Deposit Request step and complete procedures in the Receive Cash Security Deposit Payment step.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Administrator - Accounts Payable and Receivable (FI-CA). |  |  |
| 2 | Access App | Open Interest Run for Security Deposits (F4547). | The Application Jobs screen displays. |  |
| 3 | Create | Choose Create. | The New Job view displays. |  |
| 4 | Enter Basic Parameters | Make the following entries and choose Step 2:Job Template: FI-CA: Security Deposit Interest RunJob Name: FI-CA: Security Deposit Interest Run |  |  |
| 5 | Enter Basic Parameters | Make the following entry and choose Step 3:Start Immediately: Selected |  |  |
| 6 | Enter Posting Parameters | Make the following entries:Run Identification:Prefix of Run ID: For example, Z01General Selections:Business Partner: <Business Partner number>Contract Account: <Contract Account number>Company Code: 3310Currency: AEDCorrespondence:Create Correspondence: SelectedSettings for Application Log:Problem Class: Additional InformationNote The Dynamic Date Function is available for parameters of date, you can also use the Dynamic Date Function with the Define Recurrence Pattern to set up the recurring run for mass activity to meet your business needs. For example, you can choose the dynamic date function TODAY for testing purpose. |  |  |
| 7 | Check Job | Choose Check. | System message You can go ahead and schedule the job is displayed. |  |
| 8 | Execute Job | Choose Schedule. | The Application Jobs screen is displayed.One new application job is created with a status. |  |
| 9 | Check Job Status | After the job has been finished, choose the arrow button at the end of the entry to navigate to the job details. | The Job Log screen is displayed. The log should show no errors.You could also see the interest document posted. |  |

### Transfer Business Partner Items

#### Transfer Business Partner Items

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this process step, you can transfer business partner items if you come across such cases as receivables from different contract accounts shall be transferred to a joint contract account or a payment has been assigned to a wrong contract account and need to be transferred to another contract account, an so on.

Prerequisite

1. Check or Define Your Transfer Reason

Depending on your configuration environment for SAP S/4HANA Cloud Public Edition, choose one of the following options:

Configure Your Solution:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad with as a Configuration Expert. |  |  |
| 2 | Access App Make Your Solution | Open Manage Your Solution (F1241) | The Manage Your Solution screen displays. |  |
| 3 | Access App Transfer | Search with following criteria:Application Area: financeSub application: Contract AccountingItem Name: Transfer |  |  |
| 4 | Access App Define Transfer Reasons to Check or Define the Transfer Reason | Open Define Transfer Reasons and check the transfer reasons.Note Select the Payment of a transfer reason if you want transfers with this transfer reason to be displayed as payments in the account balance payment list. Meanwhile, please check Prerequisite 5 and Prerequisite 6 as well. | The Change View “Transfer Reasons”: Overview displays. |  |

SAP Central Business Configuration:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the project experience in SAP Central Business Configuration. |  |  |
| 2 | Open Define Transfer Reasons | Go to the Business Processes Configuration app and search for the following activity: Define Transfer Reasons.Choose Open Documentation for the found line item to see more details about this configuration activity.Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. | The Change View “Transfer Reasons”: Overview screen is displayed. |  |
| 3 | Configure Define Transfer Reason | Input necessary parameters.Note Select the Payment of a transfer reason if you want transfers with this transfer reason to be displayed as payments in the account balance payment list. Meanwhile, please check Prerequisite 5 and Prerequisite 6 as well. |  |  |

2. Check or Define the Default Value for Transfer Reason

Depending on your configuration environment for SAP S/4HANA Cloud Public Edition, choose one of the following options:

Configure Your Solution:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad with as a Configuration Expert. |  |  |
| 2 | Access App Make Your Solution | Open Manage Your Solution (F1241) | The Manage Your Solution screen displays. |  |
| 3 | Access App Transfer | Search with following criteria:Application Area: FinanceSub application: Contract AccountingItem Name: Transfer |  |  |
| 4 | Access App Define Default Value for Transfer Reason to Check or Define the Default Value for Transfer Reason | Open Define Default Value for Transfer Reason, check or define the default transfer reasons to be proposed when you post a transfer.Transfer Reason: 01 | The screen Maintain Transfer Item: Additional Specifications displays. |  |

SAP Central Business Configuration:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the project experience in SAP Central Business Configuration. |  |  |
| 2 | Open Define Default Value for Transfer Reason | Go to the Business Processes Configuration app and search for the following activity: Define Default Value for Transfer Reason.Choose Open Documentation for the found line item to see more details about this configuration activity.Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. | The Maintain Transfer Item: Additional Specifications screen is displayed. |  |
| 3 | Check or Define Transfer Reason | Check or define the default transfer reasons to be proposed when you post a transfer.Transfer Reason: 01 |  |  |

3. Check or Define Specifications and Default Values for Transfer

Depending on your configuration environment for SAP S/4HANA Cloud Public Edition, choose one of the following options:

Configure Your Solution:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Configuration Expert. |  |  |
| 2 | Access App Make Your Solution | Open Manage Your Solution (F1241) | The Manage Your Solution screen displays. |  |
| 3 | Access App Transfer | Search with following criteria:Application Area: FinanceSub application: Contract AccountingItem Name: Transfer |  |  |
| 4 | Access App Define Specifications and Default Values for Transfer | Open Define Specifications and Default Values for Transfer, you define the clearing reason and default values for the document type and the transfer currency that are used when posting a transfer document.Currency: <the currency of the business partner item>Document Type: YATransfer Credit: selected | The screen Maintain Transfer Item: Specifications: Detail scr displays. |  |

SAP Central Business Configuration:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the project experience in SAP Central Business Configuration. |  |  |
| 2 | Open Define Specifications and Default Values for Transfer | Go to the Business Processes Configuration app and search for the following activity: Define Specifications and Default Values for Transfer.Choose Open Documentation for the found line item to see more details about this configuration activity.Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. | The Maintain Transfer Item: Specifications: Detail scr screen is displayed. |  |
| 3 | Input Parameters | Currency: <the currency of the business partner item>Document Type: YATransfer Credit: selected |  |  |

4. Check or Define Specifications Dependent on Transfer Reason

Depending on your configuration environment for SAP S/4HANA Cloud Public Edition, choose one of the following options:

Configure Your Solution:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Configuration Expert. |  |  |
| 2 | Access App Make Your Solution | Open Manage Your Solution (F1241) | The Manage Your Solution screen displays. |  |
| 3 | Access App Transfer | Search with following criteria:Application Area: FinanceSub application: Contract AccountingItem Name: Transfer |  |  |
| 4 | Access App Define Specifications Dependent on Transfer Reason | Open Define Specifications Dependent on Transfer Reason, check or define the parameters of the transfer reasons such as whether credit can be transferred, whether a partial transfer is allowed, etc. | The screen Maintain Transfer Items, Specifications by Transfer Reason: Overview displays. |  |

SAP Central Business Configuration:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the project experience in SAP Central Business Configuration. |  |  |
| 2 | Open Define Specifications Dependent on Transfer Reason | Go to the Business Processes Configuration app and search for the following activity: Define Specifications Dependent on Transfer Reason.Choose Open Documentation for the found line item to see more details about this configuration activity.Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. | The Maintain Transfer Items, Specifications by Transfer Reason: Overview screen is displayed. |  |
| 3 | Check or Define Parameters | Check or define the parameters of the transfer reasons such as whether credit can be transferred, whether a partial transfer is allowed, etc. |  |  |

5. Check or Define Transactions for the Transfer of Items and Requests

Depending on your configuration environment for SAP S/4HANA Cloud Public Edition, choose one of the following options:

Configure Your Solution:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Configuration Expert. |  |  |
| 2 | Access App Make Your Solution | Open Manage Your Solution (F1241) | The Manage Your Solution screen displays. |  |
| 3 | Access App Transfer | Search with following criteria:Application Area: FinanceSub application: Contract AccountingItem Name: Transfer |  |  |
| 4 | Access App Define Transactions for the Transfer of Items and Requests | Open Define Transactions for the Transfer of Items and Requests, check or define the transactions for the items and requests transferred.Note Please check or define the external transactions specified in this SSCUI by following Prerequisite 6. | The screen Maintain Transfer Items: Transaction Determination: Overview displays. |  |

SAP Central Business Configuration:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the project experience in SAP Central Business Configuration. |  |  |
| 2 | Open Define Transactions for the Transfer of Items and Requests | Go to the Business Processes Configuration app and search for the following activity: Define Transactions for the Transfer of Items and Requests.Choose Open Documentation for the found line item to see more details about this configuration activity.Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. | The Maintain Transfer Items: Transaction Determination: Overview screen is displayed. |  |
| 3 | Configure Define Transactions for the Transfer of Items and Requests | Open Define Transactions for the Transfer of Items and Requests, check or define the transactions for the items and requests transferred.Note Please check or define the external transactions specified in this SSCUI by following Prerequisite 6. |  |  |

6. Check or Define the External Transactions Relate to Transfer

Depending on your configuration environment for SAP S/4HANA Cloud Public Edition, choose one of the following options:

Configure Your Solution:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Configuration Expert. |  |  |
| 2 | Access App Make Your Solution | Open Manage Your Solution (F1241) | The Manage Your Solution screen displays. |  |
| 3 | Access App Postings and Documents | Search with following criteria:Application Area: FinanceSub application: Contract AccountingItem Name: Postings and Documents |  |  |
| 4 | Access App Define and Parameterize External Transactions | Open Define and Parameterize External Transactions, check or define the parameters of the external transactions related to transfer, especially the ones configured in Prerequisite 5.Note If you want to display the transferred items in the payment list in the SAP Fiori app Display Account Balance, please make sure the Payment of transfer reason in Prerequisite 1 and Payment trans. of the Debit main trans. and Debit subtrans. in Prerequisite 5 are both selected. | The screen Maintain Transfer Item: Additional Specifications displays. |  |

SAP Central Business Configuration:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the project experience in SAP Central Business Configuration. |  |  |
| 2 | Open Define Transactions for the Transfer of Items and Requests | Go to the Business Processes Configuration app and search for the following activity: Define Transactions for the Transfer of Items and Requests.Choose Open Documentation for the found line item to see more details about this configuration activity.Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. | The Maintain Transfer Item: Additional Specifications screen is displayed. |  |
| 3 | Configure Define and Parameterize External Transactions | Open Define and Parameterize External Transactions, check or define the parameters of the external transactions related to transfer, especially the ones configured in Prerequisite 5.Note If you want to display the transferred items in the payment list in the SAP Fiori app Display Account Balance, please make sure the Payment of transfer reason in Prerequisite 1 and Payment trans. of the Debit main trans. and Debit subtrans. in Prerequisite 5 are both selected. |  |  |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Accounts Payable and Receivable Accountant (FI-CA). |  |  |
| 2 | Access App | Open Transfer Business Partner Items (F4398). | The Transfer Business Partner Items screen displays. |  |
| 3 | Enter Filters | Make the following entries to select the business partner items you want to transfer.Note You can choose the Adapt Filters button to select various fields for transferable items selection, such as Dunning Lock Reason, Payment Lock Reason, and Subapplication.Document Number: <Document number of the business partner item to be transferred>Business Partner: <Business partner number>Contract Account: <Contract account number>Contract: <Provider Contract Number>Note Among fields of Document Number, Business Partner, Contract Account and Contract, you need to enter at least one of them to select the transferable business partner items.Currency: <Currency of the business partner item to be transferred>Click Go. | Transferable items are listed. |  |
| 4 | Transfer Items | Select items from transferable items list, choose Transfer.In the Transfer dialog box, make the following entries:Business Partner: <Target business partner number>Contract Account: <Target contract account number>Posting Date: <Today’s date>Transfer Reason: <Select the transfer reason>Document Type: YAReconciliation Key: <Enter the reconciliation key>Text: <Enter the text>Choose Transfer.In the Confirmation dialog box, choose OK.The Success window appears with the transfer document number. Choose Close to close the dialog box. | Get the transfer document number successfully. If you click the transfer document number in the Success dialog box, you could navigate to the app to display the document. |  |

### Dispute Case Management

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

With Dispute Case Management, you can create and manage complaints (disputes) from your business partner about incorrect invoices and credits or missing payments and credits as dispute cases. In this test script, incorrect invoice and missing payment are displayed.

Prerequisite

Make sure you have activated Dispute Case Management for your company codes before you open dispute cases in Contract Accounting.

1. Activate Dispute Management in Contract Accounting

Depending on your configuration environment for SAP S/4HANA Cloud Public Edition, choose one of the following options:

Configure Your Solution:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. |  |  |
| 2 | Access App Manage Your Solution | Open Manage Your Solution and then choose Configure Your Solution | The Manage Your Solution screen displays. |  |
| 3 | Access App Make Specifications | Search with following criteria:Application Area: FinanceSub Application Area: Contract AccountingChoose the Dispute Management group.Choose the configuration step: Make Basic Settings for Dispute Management.Choose Configure. | The Change View "Dispute Management: General Settings": Details screen displays. |  |
| 4 | Choose | In the Activation of SAP Dispute Management section:Active: SelectedChoose Save. | Dispute Case Management is activated in Contract Accounting. |  |

SAP Central Business Configuration:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the project experience in SAP Central Business Configuration. |  |  |
| 2 | Open Make Basic Settings for Dispute Management | Go to the Business Processes Configuration app and search for the following activity: Make Basic Settings for Dispute Management.Choose Open Documentation for the found line item to see more details about this configuration activity.Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. | The Configure your Solution-Organization screen is displayed. |  |
| 3 | Input Parameters | On the Change View "Dispute Management: General Settings": Details screen:Active: SelectedChoose Save. | The Dispute Case Management is active in Contract Accounting. |  |

1. Activate Dispute Management for Your Company Codes in Contract Accounting

Depending on your configuration environment for SAP S/4HANA Cloud Public Edition, choose one of the following options:

Configure Your Solution:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. |  |  |
| 2 | Access App Manage Your Solution | Open Manage Your Solution and then choose Configure Your Solution. | The Manage Your Solution screen displays. |  |
| 3 | Access App Make Specifications | Search with following criteria:Application Area: FinanceSub Application Area: Contract AccountingChoose the Organization group.Choose the configuration step: Set Up Company Codes for Contract Accounts Receivable and Payable.Choose Configure. | The Configure your Solution-Organization screen displays. |  |
| 4 | Choose | Choose your companies:Settings for further Business Process:Dispute Cases in Dispute Management: SelectedSave. | Dispute Case Management is activated for your companies. |  |

SAP Central Business Configuration:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the project experience in SAP Central Business Configuration. |  |  |
| 2 | Open Set Up Company Codes for Contract Accounts Receivable and Payable | Go to the Business Processes Configuration app and search for the following activity: Set Up Company Codes for Contract Accounts Receivable and Payable.Choose Open Documentation for the found line item to see more details about this configuration activity.Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. | The Configure your Solution-Organization screen is displayed. |  |
| 3 | Input Parameters | Choose your companies:Settings for further Business Process:Dispute Cases in Dispute Management: SelectedSave. | The Dispute Case Management is active for your companies. |  |

#### Incorrect Invoice Processing

##### Create a Dispute Case of Incorrect Invoice

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Context

In this activity, you create an incorrect invoice dispute case for open or cleared invoices.

Prerequisite

An open or cleared contract accounting invoice document exists.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Accounts Payable and Receivable Accountant (FI-CA). |  |  |
| 2 | Access App | Open Manage Dispute Cases (FI-CA) (F4443) . | The Manage Dispute Cases screen displays. |  |
| 3 | Create | Choose Create. | The Create Dispute Case dialog box displays. |  |
| 4 | Enter Parameters | Make the following entries:Dispute Case Type: Incorrect InvoiceBusiness Partner: <Business Partner number>Contract Account: <Contract Account number> (Optional)Document: <Document number>Choose Create. | The New Dispute Case screen displays. |  |
| 5 | Enter Parameters | Choose the Case Overview tab and make the following entries:Basic Data:Title: <Optional>Company Code: 3310Status: NewAdditional information: <Optional>External Reference: <Optional>Detail Data:Category: <Invoice amount too high (0001) as an example>Priority: <Medium as an example>Reason: <Invoice amount not correct (0001) as an example>Amounts:Disputed Amount: <Disputed Amount of the Invoice>Contact:Contact Person: <Optional>E-mail Address: <Optional>Telephone: <Optional>Fax: <Optional>Country/Reg: <Optional>Choose the Documents tab.You can include more documents into this dispute case.Choose Add, search and select the documents and choose Include.Choose the Attachments tab and choose Upload.Select the documents from your folder and choose Open.Choose the Notes tab and make the following entry:Notes: <any comment>Choose Create. | An incorrect invoice dispute case is created. |  |

##### Modify the Dispute Case Status

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Context

In this process step, you could change the dispute case status and give the deadline date and plan closed date for the dispute case.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Accounts Payable and Receivable Accountant (FI-CA). |  |  |
| 2 | Access App | Open Manage Dispute Cases (FI-CA) (F4443) | The Manage Dispute Cases screen displays. |  |
| 3 | Execute Query | You can filter the dispute cases by:Case IDStatusDispute typeCategoryPriorityBusiness PartnerContract AccountProcessorEditing statusChoose Go.Note You can choose the Adapt Filters icon on the right side of the view to add more fields to the filters. | Dispute cases are listed. |  |
| 4 | Choose Items to Be Modified | Find the dispute case you've created in the previous step.Click the dispute case. | The dispute case screen displays. |  |
| 5 | Edit Dispute Case | Choose Edit.Status: Being ProcessedProcessing Deadline: <Today's date or a future date>Planned Close Date: <Today's date or a future date>Choose save. | Changes to dispute case are saved. |  |

##### Process the Incorrect Invoice Dispute Case

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Context

In this process step, you can post following documents for this dispute case.

|  |
| --- |
| Note After investigating the dispute case, what can be carried out next depends on the results of the investigation. For incorrect invoice dispute cases, we provide the following options as the optional follow-on documents:Option 1: Post a credit document for the same business partner and contract accountOption 2: Reverse the document included in the dispute caseOption 3: Write-off the document included in the dispute caseHere we take option 1 as an example. |

In this activity, you create credit memo document for the same business partner and contract in dispute case, the amount for the credit memo document should be the same with the disputed amount in dispute case.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Accounts Payable and Receivable Accountant (FI-CA). |  |  |
| 2 | Access App | Open Post Document (FPE1). | The Post Document: Initial Screen displays. |  |
| 3 | Enter Data | Make the following entries:Document Date: <Today's Date>Posting Date: <Today's Date>Document Type: YACurrency: <Same currency with the disputed amount>Reconcil. Key: <Reconciliation Key generated by system>Case ID : <Your case ID created in previous step>Note The icon for the Case ID is not a value help option, you can navigate to the SAP Fiori app Manage Dispute Cases by clicking on it.You can navigate to the Post Document app from Manage Dispute Cases app by choosing Create Correction in the Dispute Case view, and the Case ID will be automatically filled by system. Otherwise, please input the Case ID manually.BP Item: Y01G/L Item: Y01Taxes Calculate Automatically: Selected |  |  |
| 4 | Enter BP Item | Choose New BP Itm. | The Checking reconciliation key screen appears.Note If Reconcil. Key has already been created, the Checking reconciliation key screen won’t be displayed. Please go to step 7 directly. |  |
| 5 | Create Reconciliation Key | Choose Yes. | A new reconciliation key is created. |  |
| 6 | Continue to Enter BP Item | Choose Continue. | The Post Document: Enter Item screen displays. |  |
| 7 | Enter Item Data | Make the following entries:In the Account Assignment section,Business partner: <Business Partner Number within dispute case>Contract Acct: <Contract Account Number within dispute case if any>Company Code: 3310Transaction: Y600/0010In the Amounts and Due Dates section,Amount: <Same with disputed amount> |  |  |
| 8 | Post | Choose Post. | The credit document is posted. |  |

##### Close the Dispute Case

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Context

In previous step, you issue a credit memo that refers to the dispute case and the credit memo document is automatically assigned to the dispute case. When the remaining disputed amount is zero, you determine that the customer's complaint is justified, and now the disputed case can be closed.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Accounts Payable and Receivable Accountant (FI-CA). |  |  |
| 2 | Access App | Open Manage Dispute Cases (FI-CA) (F4443). | The Manage Dispute Cases screen displays. |  |
| 3 | Execute Query | You can filter the dispute cases by:Case IDStatusDispute typeCategoryPriorityBusiness PartnerContract AccountProcessorEditing statusChoose Go.Note You can choose the Adapt Filters icon on the right side of the view to add more fields to the filters. | Dispute cases are listed. |  |
| 4 | Choose Items to Be Modified | Find the dispute case you've created in the previous step.Click the dispute case. | The dispute case screen displays. |  |
| 5 | Edit Dispute Case | Edit: SelectedStatus: ClosedRoot Cause reason: <Wrong Invoicing, for example>Choose save.Note Once a dispute case is closed, you can no longer change it. However, you can start processing the dispute case again via button Resume in the navigator list. Then the status of dispute case is changed to In process automatically.If you have confirmed the dispute case, you cannot start processing the dispute case again. | Changes to dispute case are saved. |  |

#### Missing Payment Processing

##### Create a Dispute Case of Missing Payment

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Context

In this activity, you create a dispute case of missing payment. Here we use payment that is wrongly allocated to other business partner as a use case.

For example, you receive a call from customer A, complaining that the invoice has been paid already, but is still dunned. After investigating the dispute case, you find the payment has been wrongly allocated to other business partner (for example, business partner B). Thus you have to reset the wrongly allocated payment lot of customer B and create a correct payment lot for customer A.

Prerequisite

An overdue open invoice document exists for business partner A, and a cleared document created by payment lot exists for business partner B.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Accounts Payable and Receivable Accountant (FI-CA). |  |  |
| 2 | Access App | Open Manage Dispute Cases (FI-CA) (F4443) . | The Manage Dispute Cases screen displays. |  |
| 3 | Create | Choose Create. | The Create Dispute Case dialog box displays. |  |
| 4 | Enter Parameters | Make the following entries:Dispute Case Type: Missing PaymentBusiness Partner: <Business Partner number>Contract Account: <Contract Account number> (Optional)Choose Create. | The New Dispute Case screen displays. |  |
| 5 | Enter Further Parameters | Choose the Case Overview tab and make the following entries:Basic Data:Title: <Optional>Company Code: 3310Status: NewAdditional information: <Optional>External Reference: <Optional>Detail Data:Category: <Payment is missing as an example>Priority: <Medium as an example>Reason: <Invoice amount too high as an example>Amounts:Disputed Amount: <Disputed Amount>Currency: AEDContact:Contact Person: <Optional>E-mail Address: <Optional>Telephone: <Optional>Fax: <Optional>Country/Reg: <Optional>Choose the Attachments tab and choose Upload.Select the documents from your folder and choose Open.Choose the Notes tab and make the following entry:Notes: <any comment>Choose Create. | The incorrect invoice dispute case is created. |  |

##### Modify the Dispute Case Status

In this process step you can change the dispute case status and give the deadline date and plan closed date for the dispute case. To do so, refer to the [Modify the Dispute Case Status](#unique_57) [page ] 114 step.

##### Reset Payment Assignment

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Context

In this activity, you reset the payment assignment that is wrongly allocated to another business partner, for example, business partner B.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Accounts Payable and Receivable Accountant (FI-CA). |  |  |
| 2 | Access App | Open Process Payment Lot (FP05) | The Payment Lot: Initial Screen displays. |  |
| 3 | Enter Parameter | Lot: <Input Payment Lot ID that has been wrongly processed for business partner B>Choose List. | The Payment Lot: Payment Search screen displays. |  |
| 4 | Choose Items to Be Modified | Double-click the payment lot item.New screen Item Display: Details and Selections displays.Choose reset payment assignment.New screen Reverse document displays.Reversal date: <Today’s date as example>Document Type: <YA>Clearing Reason: <05>Reversal Method: <Clear Business Partner Items/Clearing Reset>Reconciliation Key: <generated automatically>Choose Post.Note If Generate Reconciliation Key screen appears, choose yes and continue.Choose clarify payment.Note If you have the error message Clarification case has been reserved for Machine Learning. when you choose Clarify Payment, that means you already activate the Machine Learning for your company code, please refer to the test script of the scope item 47I Contract Accounting – Cash Application.Close the information.New screen Item Clarify: Details and Selections displays.In the selection proposal section, maintain the following entries:Business partner: <Change the business partner B to business partner A>Add.Specification: <Change the document to overdue open document in Prerequisite>Choose Post. | The clearing document is reset and reversed.The overdue open invoice is cleared. |  |

##### Assign Payments to Dispute Case (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Context

In this process step, you can manually assign payments to dispute case. If your payments have already been assigned to dispute case automatically, please skip this step.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Accounts Payable and Receivable Accountant (FI-CA). |  |  |
| 2 | Access App | Open Manage Dispute Cases (FI-CA) (F4443). | The Manage Dispute Cases screen displays. |  |
| 3 | Execute Query | You can filter the dispute cases by:Case IDStatusDispute typeCategoryPriorityBusiness PartnerContract AccountProcessorEditing statusChoose Go.Note You can choose the Adapt Filters icon on the right side of the view to add more fields to the filters. | Dispute cases are listed. |  |
| 4 | Choose Items to be Modified | Find the dispute case you need to modify.Click the dispute case. | The Manage Dispute Case screen displays. |  |
| 5 | Edit Dispute Case | Choose Edit.Choose Assign payments.Select the documents from the list.Choose Assign.Choose save. | Payments are assigned to dispute case . |  |

##### Close the Dispute Case

You have assigned the correct payments to the dispute case, and now you can close the dispute case. To do so, refer to the [Close the Dispute Case](#unique_59) [page ] 117 step.

#### Send Email (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Context

When creating a dispute case in Contract Accounting, you can send email to notify customer the newly created dispute case. Meanwhile, the data of a contact person becomes the correspondence recipient. This is then included in the dispute case as an attribute and used for customer correspondence. You can use different predefined templates to send your email to customers.

Purpose

In this activity, you send an email after creating a dispute case.

Prerequisite

Make sure you maintain the email domain address as default sender domain Name in this step before you send email to your customers. The email domain address should be the same email domain address as your log on user ID, in this example it is [apr_accountant_fica@example.com](mailto:apr_accountant_fica@example.com).

Depending on your configuration environment for SAP S/4HANA Cloud Public Edition, choose one of the following options:

Configure Your Solution:

| Step # | Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. |  |  |
| 2 | Access App | Open Manage Your Solutionand choose Configure Your Solution. | The Manage Your Solution screen displays. |  |
| 3 | Input Parameters | Application Area: Application Platform and InfrastructureSub Application Area: Output ManagementItem Name: System AdministrationSelect Configuration, choose step Define Allowed Sender Domains For Email Outbound.Choose New Entries.Sender Domain Name: example.comChoose Save. | The Sender Domain Name is saved. |  |

SAP Central Business Configuration:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the project experience in SAP Central Business Configuration. |  |  |
| 2 | Open Define Email Sender Domain | Go to the Business Processes Configuration app and search for the following activity: Define Allowed Sender Domains For Email Outbound.Choose Open Documentation for the found line item to see more details about this configuration activity.Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. |  |  |
| 3 | Input Parameters | Choose New Entries.Sender Domain Name: example.comChoose Save. | The Sender Domain Name is saved. |  |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Accounts Payable and Receivable Accountant (FI-CA). |  |  |
| 2 | Access App | Open Manage Dispute Cases (FI-CA) (F4443) . | The Manage Dispute Cases screen displays. |  |
| 3 | Create Email | Choose Go to get the list of dispute cases.Choose your dispute case to navigate to the detailed page of it.Choose Send Email. | The Dispute Case screen displays. |  |
| 4 | Enter Parameters | In the Send Email dialog box, make the following entries:To: <The recipient is driven from contact data or manually input>CC: <Optional>Subject: <System automatically created>Template: <Message to Customer - Dispute Case Created> <English> as an exampleAdditional Text: <Optional>Choose Send E-Mail. | The Email is created and sent. |  |

### Disconnection and Reconnection

#### Create Disconnection Request

Purpose

In this process step, you create disconnection requests during FI-CA dunning run under configurable preconditions.

Prerequisite

Make sure you have maintained necessary master data and completed necessary steps before you create disconnection requests during FI-CA dunning run.

1. Before you use the Disconnection and Reconnection service, make sure you have activated this functionality for your companies by following steps below.

Depending on your configuration environment for SAP S/4HANA Cloud Public Edition, choose one of the following options:

Configure Your Solution:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. |  |  |
| 2 | Access App Manage Your Solution | Open Manage Your Solution and then choose Configure Your Solution. | The Manage Your Solution screen is displayed. |  |
| 3 | Access App Make Specifications | Search with following criteria:Application Area: FinanceSub Application Area: Contract AccountingChoose the Disconnection / Reconnection group.Choose the configuration step: Configure Disconnection and Reconnection of Services. | The Change View "General Settings for Service Disconnection and Reconnection screen is displayed. |  |
| 4 | Choose | Make the following entries for your companies:Disconnection Active: SelectedSave. | The Disconnection and Reconnection service is activated for your companies. |  |

SAP Central Business Configuration:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the project experience in SAP Central Business Configuration. |  |  |
| 2 | Open Configure Disconnection and Reconnection of Services | Go to the Business Processes Configuration app and search for the following activity: Configure Disconnection and Reconnection of Services.Choose Open Documentation for the found line item to see more details about this configuration activity.Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. | The Change View "General Settings for Service Disconnection and Reconnection screen is displayed. |  |
| 3 | Input Parameters | Make the following entries for your companies:Disconnection Active: SelectedSave. | The Disconnection Reconnection service is active for your companies. |  |

1. Make sure you have the provider contract master for your business partner and contract account and assign dunning Procedure 03- Standard Dunning Procedure for Disconnection provider contract at the item level or contract account level. Refer to Contract Accounting – Master Data and Basic Functions (2AR) test script, step Create Provider Contract to create your provider contract.
2. Make sure you already have the overdue open items for your business partners, contract account and provider contract and those overdue open items can meet the criteria to trigger Dunning level 01, the disconnection request will be triggered at dunning Procedure 03.

##### Execute Dunning Proposal Run

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
| 1 | Log On | Log on to the SAP Fiori launchpad as an Administrator - Accounts Payable and Receivable (FI-CA) role assigned. |  |  |
| 2 | Access App | Open Dunning Runs (F3545). | The Application Jobs screen displays. |  |
| 3 | Create New Job | Choose Create. | The New Job view displays. |  |
| 4 | Enter Parameters | Make the following entries and choose Step 2:Job Template: FI-CA Dunning ProposalJob Name: FI-CA Dunning Proposal |  |  |
| 5 | Enter Parameters | Make the following entry and choose Step 3:Start Immediately: Selected |  |  |
| 6 | Enter Parameters | Make the following entries in the corresponding sections:Run Identification:Run ID Prefix: For example, ID0Selection Criteria:Business Partner: <Business Partner number>Contract Account: <Contract Account number>Contract: <Provider Contract number>Company Code: 3310Dunning Parameters:Issue Date: <Today's date>Dunning Procedure: 03 Standard Dunning Procedure for DisconnectionThe Dynamic Date Function is available for parameters of date, you can also use the Dynamic Date Function with the Define Recurrence Pattern to set up the recurring run for mass activity to meet your business needs. For example, you can choose the dynamic date function TODAY for testing purpose. |  |  |
| 7 | Check Job | Choose Check. | System message You can go ahead and schedule the job is displayed. |  |
| 8 | Execute Job | Choose Schedule. | The Application Jobs screen is displayed.One new application job is created with a status. |  |
| 9 | Check Job Status | After the job has been finished, choose the arrow button at the end of the entry to navigate to the job details. | The Job Log screen is displayed. The log should show no errors.The Run Identification should combine Run ID Prefix + dynamic number (xx). |  |

##### Execute Dunning Activity Run

In this activity, you can execute Dunning Activity Run and create the disconnection requests for the documents up to dunning level 01. To do so, refer to the Execute Dunning Activity Run step.

#### Send Disconnection and Reconnection Requests

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
| 1 | Log On | Log on to the SAP Fiori launchpad as an Administrator - Accounts Payable and Receivable (FI-CA). |  |  |
| 2 | Access App | Open Send Disconnection and Reconnection Requests (F4658) | The Application Jobs screen displays. |  |
| 3 | Create | Choose Create. | The New Job view displays. |  |
| 4 | Enter Parameters | Make the following entries and choose Step 2:Job Template: FI-CA: Send Disconnection and Reconnection Requests to External SystemJob Name: FI-CA: Send Disconnection and Reconnection Requests to External System |  |  |
| 5 | Enter Parameters | Make the following entry and choose Step 3:Start Immediately: Selected |  |  |
| 6 | Enter Parameters | Make the following entries:Selection Parameters:Company Code: 3310Reconnection request number: <Blank>Disconnection request number : <Blank>Business Partner: <Business Partner number>Contract Account: <Contract Account number>Processing Parameters:Block size: <Default 100 or Manual input number>Simulation: Unselected |  |  |
| 7 | Check Job | Choose Check. | System message You can go ahead and schedule the job is displayed. |  |
| 8 | Execute Job | Choose Schedule. | The Application Jobs screen is displayed.One new application job is created with a status. |  |
| 9 | Check Job Status | After the job has been finished, choose the arrow button at the end of the entry to navigate to the job details. | The Job Log screen is displayed. The log should show no errors.The disconnection number should be listed in log . |  |

#### Payment Lot Processing

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Context

In this activity, you receive the payment from customer for the overdue open items and clear them.

|  |
| --- |
| Note In order to trigger the reconnection request in next step, please make sure the total overdue amount of the documents involved in the disconnection request is less then 10 AED. (access SSCUI Configure Disconnection and Reconnection of Services (103535) to check your control table and find the reconnection trigger amount) |

Payments initiated from business partners can be processed by payment lot and go to clear the open invoices automatically. If you post a payment lot but could not clear the open invoice, its items will be posted to an interim account defined in customizing and included in a clarification worklist. Then you can process the clarification worklist by correcting the payment items, creating repayment requests, posting on account, posting on G/L account, and so on.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Accounts Payable and Receivable Accountant (FI-CA). |  |  |
| 2 | Access App | Open Process Payment Lot (FP05). | Payment Lot: Initial Screen displays. |  |
| 3 | Input Parameters for Payment Lot | Create your payment lot ID and choose Create:Lot: <Your payment lot ID>Make the following entries on the Payment Lot Create: Default Entries and Status screen:Control Information:Lot: <Your payment lot ID>Search Term: <Input your search information>Additional Info: <Input your specific information>Specifications for Posting Documents:Document Type: <by default>Posting Date: <by default>Document Date: <by default>Reconciliation Key: <Generated by the system>Currency: AEDSpecification for Posting Items on Bank Clearing Account:Bank Clearing Account: 11001080Company Code: 3310House Bank: AEBK2Account ID: AEAC2Value Date: <Today's date>Selections for Selecting and Clearing Open Items:Clearing Reason: <01, by default>Selection Category: <by default>Line Layout: SAPClick New Items.On the Payment Lot Create: Payments screen, check and make the following entries:In the Default values and status section: <Values are maintained by default>In the Payments section:Payment Amount: <Input the amount>Selection Category: <Select G/K/B/P>Note G stands for Business Partner, K stands for Contract Account and B stands for Document.If parameters you input are in accordance with the open items, the payment lot can clear open items of specific business partner, otherwise, it needs further clarification.If you want to create payment lot through payment advice note, you need to create payment advice note with selection category P in advance. Then you can directly input payment advice note with selection category P.Click Save. | Payment lot is created. |  |
| 4 | Post Payment Lot | Input your payment lot ID on the Payment Lot: Initial Screen.Lot: <Your payment lot ID>Choose Close.Note Payment lot must be closed before it can be posted.Choose Yes when message appears: All payment entered in full?Choose Post.In the Schedule Job dialog box, choose Start online and choose OK.Choose Continue when message appears: Posting run is complete, check status.In the Status section, system shows the posting status.Postprocessing is required means the payment needs further clarification. | Payment lot is closed and posted. |  |

#### Create Reconnection Requests

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
| 1 | Log On | Log on to the SAP Fiori launchpad as an Administrator - Accounts Payable and Receivable (FI-CA). |  |
| 2 | Access App | Open Create Reconnection Requests (F4654) | The Application Jobs screen displays. |
| 3 | Create | Choose Create. | The New Job view displays. |
| 4 | Enter Parameters | Make the following entries and choose Step 2:Job Template: FI-CA: Analyze and Create Reconnection RequestsJob Name: FI-CA: Analyze and Create Reconnection Requests |  |
| 5 | Enter Parameters | Make the following entry and choose Step 3:Start Immediately: Selected |  |
| 6 | Enter Parameters | Make the following entries:Company Code: 3310Creation date: <Today's date>Disconnection request number : <Disconnection Number or Blank>Business Partner: <Business Partner number>Division: <Blank>Contract Account: <Contract Account number>Provider contract number: <Provider Contract number>Simulation: Unselected |  |
| 7 | Check Job | Choose Check. | System message You can go ahead and schedule the job is displayed. |
| 8 | Execute Job | Choose Schedule. | The Application Jobs screen is displayed.One new application job is created with a status. |
| 9 | Check Job Status | After the job has been finished, choose the arrow button at the end of the entry to navigate to the job details. | The Job Log screen is displayed. The log should show no errors.Under log information, you can see the reconnection request is created. |

#### Send Disconnection and Reconnection Requests

In this activity, you send out the Reconnection Requests. To do so, refer to the Send Disconnection and Reconnection Requests step.

#### Monitor Disconnection Requests

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
| 1 | Log On | Log on to the SAP Fiori launchpad as an Administrator - Accounts Payable and Receivable (FI-CA). |  |
| 2 | Access App | Open Monitor Disconnection Requests (F4943). | The Monitor Disconnection Requests screen displays. |
| 3 | Enter Selection Criteria | On the Monitor Disconnection Requests screen, you can filter the report by using a set of fields at the top of the view:Business PartnerContract AccountContactCompany codeCreated onFill in the selection fields according to your requirements.Note Choose the Adapt Filters icon on the right side of the view to add more fields in the selection filter. |  |
| 4 | Execute | Choose GO. | A report of disconnection requests is displayed.You can navigate to the detailed information page to see the disconnection request. |

### Collection Agency

Purpose

Contract Accounts Receivable and Payable enables you to manage postings connected to submitting receivables to a collection agency and the exchange of information with those collection agencies.

#### Post Documents

In this activity, you create customer receivables. To do so, refer to the Post Documents step in Prerequisites section.

#### Release to Collection Agency

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Prerequisite

Please check whether a default collection agency has been assigned via SSCUI: 103662.

Purpose

In this step, you release the open item to collection agency.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Collections Specialist (FI-CA). |  |  |
| 2 | Access App Make Your Solution | Open Release Items for Collection (FP03E). | The Application Jobs screen displays. |  |
| 3 | Enter Data | Company Code: 3310Business Partner: <Business Partner Number used in the Post Documents step>Press Enter.Select open item to be released to collection agency and click flag for collection order. |  |  |
| 4 | Select and Confirm | In the Determine Collection Agency dialog box, choose Manual.Select the Collection Agency: <BP_AE_99> (example)Note You can also process this step via SAP Fiori app: Release Run to Collection Agency. | After collection agency is selected, the log submission status of receivable documents is updated. |  |

##### Automatic Release to Collection Agency (Optional)

Purpose

If you make the relevant system settings, items that have reached a specific dunning level are automatically released for collection. The release of receivables for collection is integrated in the following business processes:

- Dunning
- Write-off
- Write-off in mass run

Prerequisite

Before you activate Automatic Release to Collection Agency, please complete the steps below:

1. Check whether dunning procedure for automatic release to collection agency has been created (SSCUI ID:102469).

Depending on your configuration environment for SAP S/4HANA Cloud Public Edition, choose one of the following options:

Configure Your Solution:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. |  |  |
| 2 | Access App Manage Your Solution | Open Manage Your Solution (F1241) and then choose Configure Your Solution. | The Manage Your Solution screen is displayed. |  |
| 3 | Access App Configure Dunning Procedure | Search with following criteria:Application Area: FinanceSub Application Area: Contract AccountingChoose the group Dunning.Choose the configuration step Configure Dunning Procedure. | The Change View "Dunning Procedure": Overview screen is displayed. |  |
| 4 | Check Dunning Procedure | Check whether automatic release to collection agency procedure is available in the system:For example:08 Dunning Proc. for Rel. to Coll. Agency (FKKMAKT)06 Dunning Proc. Rel for Submit.to Ext. Coll. Agency |  |  |

SAP Central Business Configuration:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the project experience in SAP Central Business Configuration. |  |  |
| 2 | Open Activate Configure Dunning Procedure | Go to the Business Processes Configuration app and search for the following activity: Configure Dunning Procedure.Choose Open Documentation for the found line item to see more details about this configuration activity.Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. | The Change View "Configure Dunning Procedure": Overview screen is displayed. |  |
| 3 | Check Dunning Procedure | Check whether automatic release to collection agency procedure is available in the system:For example:08 Dunning Proc. for Rel. to Coll. Agency (FKKMAKT)06 Dunning Proc. Rel for Submit.to Ext. Coll. Agency |  |  |

1. Make sure you have executed 2AR - Contract Accounting – Master Data and Basic Functions, and business partner and contract account master data have been created.

Follow procedures below to update contract account:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Accounts Payable and Receivable Accountant (FI-CA). |  |  |
| 2 | Access App | Open Maintain Contract Account (CAA3). | The Contract Account Display: Initial screen is displayed. |  |
| 3 | Select Change Mode | Choose Change. | The Contract Account Change: Initial screen is displayed. |  |
| 4 | Select Contract Account | Make the following entry:Contract Acct: <Select Contract Account related to Business Partner> |  |  |
| 5 | Open Contract Account | Choose Continue. | The Contract Account Change: General Data screen is displayed. |  |
| 6 | Maintain Dunning/Correspondence | Make the following entries in Dunning/Correspondence:Grouping: 01 Dunning GroupingDunning Proc.: <for example, Standard Dunning Procedure 08> |  |  |
| 7 | Save | Choose Save. | Changes to the contract account are saved. |  |

1. Post an open item under the contract account in step 2. For more information, please refer to the Post Documents step in Prerequisites section.

Make sure the open items are overdue for testing the dunning case.

1. Execute Dunning Proposal Run, please refer to the Execute Dunning Proposal Run chapter.
2. Execute Dunning Activity Run, please refer to the Execute Dunning Activity Run chapter.
3. You could check open item released to collection agency by following below steps:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Collections Specialist (FI-CA). |  |  |
| 2 | Access App Make Your Solution | Open Release Items for Collection (FP03E). | The Manage Your Solution screen is displayed. |  |
| 3 | Enter Data | Search with following criteria:Company Code:3310Business Partner:<Business Partner Number used in the Post Documents step>Deselect the Items for subm.only checkbox.Press Enter. | The status of the open item should be released. |  |

#### Submit to Collection Agency

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Prerequisite

Make sure you have set up Communication SAP_COM_0639. For more information about Communication Scenario SAP_COM_0639, please refer to the Set-Up Instruction or SAP API HUB.

Purpose

In this step, you submit the open item to collection agency.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Collections Specialist (FI-CA). |  |  |
| 2 | Access App Make Your Solution | Open Manage Submitted Items (FP03). | The Application Jobs screen displays. |  |
| 3 | Enter Data | Search with following criteria:Company Code: 3310Business Partner: <Business Partner Number used in post documents step>Press Enter.Select the open item with released status and choose submit . |  |  |
| 4 | Select and Execute | On the Process Opts tab, choose Submit items.Choose Execute. | Information Subapplication is only used if a contract is also entered appears and submit receivables to collection agency is done.Log information Processing successful; the enterprise service was triggered appears. |  |
| 5 | Check Status | Choose the back button, on the Manage Submitted Items screen, the item status is updated.Note You can also process this step via SAP Fiori app: Submission Run to Collection Agency. | The submission status of the item is updated. |  |

##### Automatic Recall Receivables from Collection Agency during Dunning (Optional)

Purpose

You can call back items from a collection agency automatically in other business transactions:

- Dunning

Prerequisite

Before you activate Automatic Recall Receivables from Collection Agency during Dunning, please complete the steps below:

1. Check whether dunning procedure for automatic recall receivables from collection agency has been created (SSCUI ID: 102469)

Depending on your configuration environment for SAP S/4HANA Cloud Public Edition, choose one of the following options:

Configure Your Solution:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. |  |  |
| 2 | Access App Manage Your Solution | Open Manage Your Solution (F1241) and then choose Configure Your Solution. | The Manage Your Solution screen is displayed. |  |
| 3 | Access App Configure Dunning Procedure | Search with following criteria:Application Area: FinanceSub Application Area: Contract AccountingChoose the group Dunning.Choose the configuration step Configure Dunning Procedure. | The Change View "Dunning Procedure": Overview screen is displayed. |  |
| 4 | Check Dunning Procedure | Check whether automatic release to collection agency procedure is available in the system:For example:07 Standard Dunning Procedure for Recall Receivables |  |  |

SAP Central Business Configuration:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the project experience in SAP Central Business Configuration. |  |  |
| 2 | Open Activate Configure Dunning Procedure | Go to the Business Processes Configuration app and search for the following activity: Configure Dunning Procedure.Choose Open Documentation for the found line item to see more details about this configuration activity.Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. | The Change View "Configure Dunning Procedure": Overview screen is displayed. |  |
| 3 | Check Dunning Procedure | Check whether automatic release to collection agency procedure is available in the system:For example:07 Standard Dunning Procedure for Recall Receivables |  |  |

1. Make sure you have executed 2AR - Contract Accounting – Master Data and Basic Functions, and business partner and contract account master data have been created.

Follow procedures below to update contract account:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Accounts Payable and Receivable Accountant (FI-CA). |  |  |
| 2 | Access App | Open Maintain Contract Account (CAA3). | The Contract Account Display: Initial screen is displayed. |  |
| 3 | Select Change Mode | Choose Change. | The Contract Account Change: Initial screen is displayed. |  |
| 4 | Select Contract Account | Make the following entry:Contract Acct: <Select Contract Account related to Business Partner> |  |  |
| 5 | Open Contract Account | Choose Continue. | The Contract Account Change: General Data screen is displayed. |  |
| 6 | Maintain Dunning/Correspondence | Make the following entries in Dunning/Correspondence:Grouping: 01 Dunning GroupingDunning Proc.: <for example, Standard Dunning Procedure 07> |  |  |
| 7 | Save | Choose Save. | Changes to the contract account are saved. |  |

1. Make sure the open items you submitted to collection agency are overdue for testing the dunning case.
2. Execute Dunning Proposal Run, please refer to the Execute Dunning Proposal Run chapter.
3. Execute Dunning Activity Run, please refer to the Execute Dunning Activity Run chapter.
4. You could check the status of submitted open item to collection agency by following below steps:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Collections Specialist (FI-CA). |  |  |
| 2 | Access App Make Your Solution | Open Manage Submitted Items (FP03). | The Manage Your Solution screen is displayed. |  |
| 3 | Enter Data | Search with following criteria:Company Code:3310Business Partner:<Business Partner Number used in the Post Documents step>Press Enter. |  |  |
| 4 | Check Status | Choose the back button, and check whether the item status has been updated. | The submission status of the item is updated as Undo. |  |

#### Post Collection Agency Information via Inbound Service

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

A collection agency has completed a collection request and informed you either by electronic data media, by letter, by phone, or by enterprise services about the money it is able to collect (fully, partially, or not at all).

Prerequisite

Make sure you have set up the communication SAP_COM_0639. After that you can use API tool (for example: postman) to call APIs and transfer the incoming information from the collection agency to your system and process it accordingly. For more information about the Communication Scenario SAP_COM_0639, please refer to the set up guide or SAP API HUB.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Navigate to SAP API HUB | Open web browser and navigate to [https://api.sap.com](https://api.sap.com/) | The SAP API hub home page is displayed |  |
| 2 | Search Out Collection Agency API | Choose SAP S/4HANA Cloud Public Edition.Search for collection agency. | The collection agency API is displayed |  |

Here's an example code to post collection agency information via inbound service:

|  |
| --- |
| Sample CodeExample Coding: Post Collection Agency information via inbound service https://{{hostname}}/sap/bc/srt/xip/sap/commissionedoutstandingcollect <soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:glob="http://sap.com/xi/FICA/Global2"> <soapenv:Header xmlns:wsa="http://www.w3.org/2005/08/addressing"> <wsa:Action>http://sap.com/xi/FICA/Global2/CommissionedOutstandingCollectionsERPBulkConfirmation_In/CommissionedOutstandingCollectionsERPBulkConfirmation_InRequest</wsa:Action> <wsa:MessageID>uuid:cbd5b349-e88c-4032-8463-75f75931e104</wsa:MessageID> <wsa:To> https://{{hostname}}/sap/bc/srt/scs_ext/sap/commissionedoutstandingcollect</wsa:To> </soapenv:Header> <soapenv:Body> <glob:CommissionedOutstandingCollectionsERPBulkConfirmation> <MessageHeader> <CreationDateTime>2020-05-14T12:00:00.1234567Z</CreationDateTime> </MessageHeader> <CommissionedOutstandingCollectionsERPConfirmationMessage> <MessageHeader> <CreationDateTime>2020-05-14T12:00:00.1234567Z</CreationDateTime> </MessageHeader> <CommissionedOutstandingCollections> <ID>COLL_AGCY BUSI_PTNER</ID> <DebtorParty> <DebtorID>BUSI_PTNER</DebtorID> </DebtorParty> <Item> <ID>000400101755001</ID> <GroupingCode>01</GroupingCode> <StatusCode>02</StatusCode> <FeeAmount currencyCode="AED" 5.00< FeeAmount> <InterestAmount currencyCode="AED">8.00</InterestAmount> </Item> <Payment> <CollectionAgencyCommissionedOutstandingCollectionsPaymentID>Pay01</CollectionAgencyCommissionedOutstandingCollectionsPaymentID> <!-- 22 == 5 + 8 + 9 --> <Amount currencyCode="AED">22.00</Amount> <GroupID>GRP01</GroupID> <ItemAssignment> <CommissionedOutstandingCollectionsItemID>000400101755001</CommissionedOutstandingCollectionsItemID> <CommissionedOutstandingCollectionsItemGroupingCode>01</CommissionedOutstandingCollectionsItemGroupingCode> <PaymentAmount currencyCode="AED">9.00</PaymentAmount> <PaymentDate>2020-05-14</PaymentDate> </ItemAssignment> </Payment> </CommissionedOutstandingCollections> </CommissionedOutstandingCollectionsERPConfirmationMessage> </glob:CommissionedOutstandingCollectionsERPBulkConfirmation> </soapenv:Body> </soapenv:Envelope> |

#### Process Information from Collection Agency

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you can process and post inbound collection agency information.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Administrator - Accounts Payable and Receivable (FI-CA). |  |  |
| 2 | Access App | Open Process Information from Collection Agency (F4924). | The Application Jobs screen displays. |  |
| 3 | Create New Job | Choose Create. | The New Job view displays. |  |
| 4 | Enter Parameters | Make the following entries and choose Step 2:Job Template: FI-CA: Process Information from Collection AgencyJob Name: FI-CA: Process Information from Collection Agency |  |  |
| 5 | Enter Parameters | Make the following entry and choose Step 3:Start Immediately: Selected |  |  |
| 6 | Enter Parameters | Make the following entries:Simulation Run: UnselectedSelection CriteriaBusiness Partner: <Business Partner number>Collection Agency: <Collection Agency number>Date Received: <Specify the date received>Posting ParametersCompany Code: 3310 |  |  |
| 7 | Check Job | Choose Check. | System message You can go ahead and schedule the job displays. |  |
| 8 | Execute Job | Choose Schedule. | The Application Jobs screen displays.One new application job is created with a status. |  |
| 9 | Check Job Status | After the job has been finished, choose the arrow button at the end of the entry to navigate to the job details. | The Job Log screen is displayed. The log should show no errors.Details about the payment collection agency collected from customer are displayed. |  |

#### Post Receivables for Collection Agency

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

You post collected payments reported by collection agencies as summarized receivables to the contract account of the collection agency.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Administrator - Accounts Payable and Receivable (FI-CA). |  |  |
| 2 | Access App | Open Post Receivables for Collection Agency (F4923). | The Application Jobs screen displays. |  |
| 3 | Create New Job | Choose Create. | The New Job view displays. |  |
| 4 | Enter Parameters | Make the following entries and choose Step 2:Job Template: FI-CA: Post Receivables for Collection AgencyJob Name: FI-CA: Post Receivables for Collection Agency |  |  |
| 5 | Enter Parameters | Make the following entry and choose Step 3:Start Immediately: Selected |  |  |
| 6 | Enter Parameters | Make the following entries:Selection CriteriaCollection Agency: <Collection Agency number>Simulation: Unselected |  |  |
| 7 | Check Job | Choose Check. | System message You can go ahead and schedule the job displays. |  |
| 8 | Execute Job | Choose Schedule. | The Application Jobs screen displays.One new application job is created with a status. |  |
| 9 | Check Job Status | After the job has been finished, choose the arrow button at the end of the entry to navigate to the job details. | The Job Log screen is displayed. The log should show no errors. |  |

#### Monitor Collection Services

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

You can monitor collection services for the outbound and inbound information that you send or receive using enterprise services.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad with your user credentials as Administrator - Accounts Payable and Receivable (FI-CA) role assigned. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access App | Open Monitor Collection Services (FKKCOLL_MONI). | The Application Jobs screen is displayed. |  |
| 3 | Enter Parameters | Choose tab Collection Payments.Select Collection Agency on the left screen.Enter Business Partner: <Business Partner number>Press Enter. |  |  |
| 4 | Check Items | Check the status of the collection item. | The collection item status is displayed. |  |
| 5 | Display Message | Choose Item > Msg Display . | The Application Jobs screen is displayed.One new application job is created with a status. |  |
| 6 | Maintain Parameter | On the Application-Specific Selection tab, maintain the following data:Namespace: /FINCAInterface Name: BLKCOLL_INOn the Generic Selection tab:Choose Today.Message GUID: <Blank>On the Status Selection tab:Choose Select all.Choose Execute. | Details about the Inbound information of collection services are displayed . |  |

#### Display History of Collection Items

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

You can check the history of collection items.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Collections Specialist (FI-CA). |  |  |
| 2 | Access App | Open Display Collection Item History (FP03H). | The Application Jobs screen displays. |  |
| 3 | Enter Basic Parameters | Make the following entries:Company Code: 3310Business Partner: <Business Partner Number>Choose Execute. | Details of the collection items are displayed. |  |

#### Create List of Collection Items

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

You can create list of collection items.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Collections Specialist (FI-CA). |  |  |
| 2 | Access App | Open Create List with Collection Items (FP03L). | The Application Jobs screen displays. |  |
| 3 | Enter Basic Parameters | Make the following entries:Company Code: 3310Business Partner: <Business Partner Number>Choose Execute. | List of collection items is created. |  |

### Integration with Credit Management

#### Transfer Credit Data

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

You can transfer credit exposure from Contract Accounts Receivable and Payable to SAP Credit Management.

Prerequisite

Before you execute Transfer Credit Data, make sure the following data have been prepared:

1. Maintain business partner with role UKM000 Sap Credit Management. Click on the Credit Profile tab and choose role SAP_FICA FI-CA Rule. Choose Credit Segment Data and choose Credit Segment 1000.
2. Access SSCUI (103596): Activate Credit Management, select the Active checkbox for the C Convergent FI-CA application area and choose Save.
3. Create open document. See Prerequisite step - Post Documents.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Administrator - Accounts Payable and Receivable (FI-CA). |  |  |
| 2 | Access App | Open Transfer Credit Data (F4905). | The Application Jobs screen displays. |  |
| 3 | Create New Job | Choose Create. | The New Job view displays. |  |
| 4 | Enter Parameters | Make the following entries and choose Step 2:Job Template: FI-CA Transfer Credit DataJob Name: FI-CA Transfer Credit Data |  |  |
| 5 | Enter Parameters | Make the following entry and choose Step 3:Start Immediately: Selected |  |  |
| 6 | Enter Parameters | Make the following entries:In the Run Identification section:Run ID Prefix: ID0Credit Segment: 1000Business Partner: <Business Partner number>In the Selection Criteria section:Liability Category: 200Percentage Rate: 100Transfer of Credit Data: SelectedSpecial Attentn: SelectedUpdate Credit Data: SelectedIn the Logs section:Problem Class: Additional Information |  |  |
| 7 | Check Job | Choose Check. | System message You can go ahead and schedule the job is displayed. |  |
| 8 | Execute Job | Choose Schedule. | The Application Jobs screen is displayed.A new application job is created with a status. |  |
| 9 | Check Job Status | After the job has been finished, choose the arrow button at the end of the entry to navigate to the job details. | The Job Log screen is displayed. The log should show no errors.You can check the credit exposure transferred in BP (role UKM000, segment 1000) . |  |

#### Replicate Creditworthiness

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

When you transfer FI-CA creditworthiness to SAP Credit Management using transaction Replication of Creditworthiness, the updated score in SAP Credit Management is automatically returned to Contract Accounts Receivable and Payable.

|  |
| --- |
| Note Scope Item 1QM Advanced Credit Management provides the function to automatically determine the risk class of a business partner from the business partner's score. Related content is available via SSCUI (102105) Create Risk Classes and SSCUI (102279) Define Events and Follow-On Processes (EVL_RISK_C Determine Risk Class). If you don't have 1QM activated, risk class cannot be determined automatically. |

Prerequisite

For detailed procedures, see the Display Creditworthiness step, Prerequisite Case 2: Update Creditworthiness Score by Write-offs.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Administrator - Accounts Payable and Receivable (FI-CA). |  |  |
| 2 | Access App | Open Replicate Creditworthiness (F4904). | The Application Jobs screen displays. |  |
| 3 | Create New Job | Choose Create. | The New Job view displays. |  |

## Connections
- part-of :: [[_cluster]]
- related-to :: [[09-subscription-billing-and-contract-accounting/test-script-contract-accounting-open-item-management-2uj-ae-872-part-02]]
- related-to :: [[09-subscription-billing-and-contract-accounting/test-script-sap-s-4hana-cloud-public-edition-sap-fiori-analytical-apps]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/2UJ_S4CLD2608_BPD_EN_AE.docx` — lines 1–3545 of the extracted text · extracted with `mammoth` · 398,263 chars in the whole document
