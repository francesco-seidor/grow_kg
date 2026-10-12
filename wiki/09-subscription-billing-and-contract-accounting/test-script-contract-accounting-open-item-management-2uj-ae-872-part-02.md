---
id: 09-subscription-billing-and-contract-accounting/test-script-contract-accounting-open-item-management-2uj-ae-872-part-02
title: "Test Script: Contract Accounting – Open Item Management (2UJ_AE) (2UJ_S4CLD2608_BPD_EN_AE) — part 2 of 2"
description: "Step-by-step test script (AE, company code 3310) for SAP S/4HANA Cloud 2608 Contract Accounting 2UJ: factoring, promise to pay, dunning, transfers, APIs."
cluster: 09-subscription-billing-and-contract-accounting
tags: [kb/subscription-billing-and-contract-accounting, topic/fi-ca-open-item-management]
aliases: []
keywords: [Contract Accounting Open Item Management and Collections, factoring, promise to pay, creditworthiness, information container, external system postings, subledger document transfer, dunning, collection strategy, api services]
sources: ["raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/2UJ_S4CLD2608_BPD_EN_AE.docx#lines-3546-5367"]
confidence: low
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-872
topic: 09-subscription-billing-and-contract-accounting/fi-ca-open-item-management
language: EN
part: 2/2
created: 2026-10-12
updated: 2026-10-12
---

# Test Script: Contract Accounting – Open Item Management (2UJ_AE) (2UJ_S4CLD2608_BPD_EN_AE) — part 2 of 2

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/2UJ_S4CLD2608_BPD_EN_AE.docx`, part 2 of 2 (lines 3546–5367 of the extracted text), extracted with `mammoth`. Grouped under **Contract Accounting Open Item Management and Collections** in Subscription Billing and Contract Accounting. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

| 4 | Enter Parameters | Make the following entries and choose Step 2:Job Template: FI-CA Replicate CreditworthinessJob Name: FI-CA Replicate Creditworthiness |  |  |
| 5 | Enter Parameters | Make the following entry and choose Step 3:Start Immediately: Selected |  |  |
| 6 | Enter Parameters | Make the following entries:Run ID Prefix: ID0Business Partner: <Business Partner number>Only Changed Scores: SelectedProblem Class: Additional Information |  |  |
| 5 | Check Job | Choose Check. | System message You can go ahead and schedule the job is displayed. |  |
| 6 | Execute Job | Choose Schedule. | The Application Jobs screen is displayed.One new application job is created with a status. |  |
| 7 | Check Job Status | After the job has been finished, choose the arrow button at the end of the entry to navigate to the job details. | The Job Log screen is displayed. The log should show no errors.For more details about Creditworthiness, see the step Display Creditworthiness - Manage Creditworthiness. |  |

#### Compare Credit Score

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

If the creditworthiness of a business partner changes due to this changed weighting factor at the changeover to a new month, Contract Accounts Receivable and Payable would not record the fact that a change took place. To preclude the necessity of replicating the creditworthiness of all business partners to SAP Credit Management, you could use the mass activity: Compare Replicated Score to identify those business partners as their creditworthiness have changed due to the monthly weighting.

Prerequisite

To change weighting factor, access SSCUI (103523): Define Time-Dependent Creditworthiness Weightings.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Administrator - Accounts Payable and Receivable (FI-CA). |  |  |
| 2 | Access App | Open Compare Credit Score (F4903). | The Application Jobs screen displays. |  |
| 3 | Create New Job | Choose Create. | The New Job view displays. |  |
| 4 | Enter Parameters | Make the following entries and choose Step 2:Job Template: FI-CA Compare Credit ScoreJob Name: FI-CA Compare Credit Score |  |  |
| 5 | Enter Parameters | Make the following entry and choose Step 3:Start Immediately: Selected |  |  |
| 6 | Enter Parameters | Make the following entries:Run ID Prefix: ID0Business Partner: <Business Partner number>Problem Class: Additional Information |  |  |
| 7 | Check Job | Choose Check. | System message You can go ahead and schedule the job is displayed. |  |
| 8 | Execute Job | Choose Schedule. | The Application Jobs screen is displayed.One new application job is created with a status. |  |
| 9 | Check Job Status | After the job has been finished, choose the arrow button at the end of the entry to navigate to the job details. | The Job Log screen is displayed. The log should show no errors.For more details about Creditworthiness, see the chapter Display Creditworthiness - Manage Creditworthiness. |  |

#### Prepare Master Data Change from External System

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Prerequisite

Before you execute Prepare Master Data Change from External System, make sure the following data have been prepared:

1. Business partner with credit segment 1000 (UKM000 role created).
2. Business partner related contract account has been created.

For internal testing purpose, please execute the procedure Prepare Master Data Change from External System in an extensibility testing environment.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result |
| --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Administrator - Accounts Payable and Receivable (FI-CA). |  |
| 2 | Access App | Open Maintain Business Partner (BP). | The Application Jobs screen displays. |
| 3 | Enter Basic Parameters | Make the following entry:Business Partner: <Business Partner number>Press Enter. Double-click Business Partner. |  |
| 4 | Select BP Role | Make the following entry:Select BP role: SAP Credit ManagementPress Enter.Choose the Credit Profile tab. |  |
| 5 | Update BP Master Data Information | Update the Score. (e.g. from 5 to 3)Change the Risk Class. (e.g. from C to B)Choose save. |  |
| 6 | Log On | Log on to the SAP Fiori launchpad as an Administrator - Accounts Payable and Receivable (FI-CA). |  |
| 7 | Access App | Open Prepare Master Data Change from External System (F4902). | The Application Jobs screen displays. |
| 8 | Create New Job | Choose Create. | The New Job view displays. |
| 9 | Enter Parameters | Make the following entries and choose Step 2:Job Template: FI-CA: Prepare Master Data Change from External SystemJob Name: FI-CA: Prepare Master Data Change from External System |  |
| 10 | Enter Parameters | Make the following entry and choose Step 3:Start Immediately: Selected |  |
| 11 | Enter Parameters | Make the following entries:Run ID Prefix: ID0Business Partner: <Business Partner number>Simulation run: UnselectedProblem Class: Additional Information |  |
| 12 | Check Job | Choose Check. | System message You can go ahead and schedule the job is displayed. |
| 13 | Execute Job | Choose Schedule. | The Application Jobs screen is displayed.One new application job is created with a status. |
| 14 | Check Job Status | After the job has been finished, choose the arrow button at the end of the entry to navigate to the job details. | The Job Log screen is displayed. The log should show no errors.Request is successfully transmitted to Credit Management. |

#### Process Master Data Change from External System

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Procedure

| Test Step # | Test Step Name | Instruction | Expect result |
| --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Extensibility Specialist. |  |
| 2 | Access App | Open Custom Logic (F6957). | The Application Jobs screen displays. |
| 3 | Create New Enhancement Implementation | Press + button. | The New Job screen is displayed. |
| 4 | Enter Parameters | Business Context: Contract Accounting: Credit Management IntegrationBAdl Description: FI-CA: Credit Management: Change to Contract Account DataImplementation ID: <e.g. 4506_DBS>Choose the Create button. |  |
| 5 | Implement Logic | Enter the logic and save the draft.e.g.IFCACREDITMGMTMASTERDATARPLCTN-CACREDITMANAGEMENTRISKCLASS = 'B'.contractaccountupdatedata-CAINTERESTCODE = '01'.ENDIF. |  |
| 6 | Save Draft | Choose Save Draft. | Draft is saved |
| 7 | Publish the Implementation | Choose Publish. | New implementation is published. |
| 8 | Log On | Log on to the SAP Fiori Launchpad with your user credentials as Administrator - Accounts Payable and Receivable (FI-CA) role assigned. |  |
| 9 | Access App | Open Process Master Data Change from External System (F4901). | The Application Jobs screen displays. |
| 10 | Create New Job | Choose Create. | The New Job view displays. |
| 11 | Enter Parameters | Make the following entries and choose Step 2:Job Template: Process Master Data Change from External SystemJob Name: Process Master Data Change from External System |  |
| 12 | Enter Parameters | Make the following entry and choose Step 3:Start Immediately: Selected |  |
| 13 | Enter Parameters | Make the following entries:Run ID Prefix: ID0Business Partner: <Business Partner number>Simulation run : UnselectedProblem class: Additional Information |  |
| 14 | Check Job | Choose Check. | System message You can go ahead and schedule the job is displayed. |
| 15 | Execute Job | Choose Schedule. | The Application Jobs screen is displayed.One new application job is created with a status. |
| 16 | Check Job Status | After the job has been finished, choose the arrow button at the end of the entry to navigate to the job details. | The Job Log screen is displayed. The log should show no errors.Partner xxxxxx is updated successfully. |

### Factoring

Purpose

In factoring, a company sells the receivables that it receives from customers to the factoring company (factor) to obtain cash quickly.

#### Post Documents

In this activity, you create customer receivables. For detailed procedures, see the Preliminary Steps - Post Documents section.

#### Offer Receivables for Sale

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Prerequisite

Make sure you have set up communication SAP_COM_0663. For information about the API regarding SAP_COM_0663, please refer to the Set-Up Instruction.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Administrator - Accounts Payable and Receivable (FI-CA). |  |  |
| 2 | Access App | Open Offer Receivables for Sale (F5384). | The Application Jobs screen displays. |  |
| 3 | Create New Job | Choose Create. | The New Job view displays. |  |
| 4 | Enter Parameters | Make the following entries and choose Step 2:Job Template: Offer Receivables for SaleJob Name: Offer Receivables for Sale |  |  |
| 5 | Enter Parameters | Make the following entry and choose Step 3:Start Immediately: Selected |  |  |
| 6 | Enter Parameters | Make the following entries:In the Run Settings section:Run ID Prefix: ID0Simulation: UnselectedIn the Selection Criteria section:Business Partner: <Business Partner number>Contract Account: <Contract Account number>Company Code:3310Factor ID: <for example, F_AE>In the Logs section:Problem Class: Additional Information |  |  |
| 5 | Check Job | Choose Check. | System message You can go ahead and schedule the job is displayed. |  |
| 6 | Execute Job | Choose Schedule. | The Application Jobs screen is displayed.One new application job is created with a status. |  |
| 7 | Check Job Status | After the job has been finished, choose the arrow button at the end of the entry to navigate to the job details. | The Job Log screen is displayed. The log should show no errors. |  |

|  |
| --- |
| Note If the Web service is not sent out, you could use the SAP Fiori app Send Offer Data Again to schedule a job and send offer information again. |

|  |
| --- |
| Note If you have run the Offer Receivables for Sale in Simulation mode, you could use the SAP Fiori app Delete Simulation to delete the simulation data, and after that the data in app Factoring: Monitor Services - tab offer (Simulation), will be cleared. |

##### Reverse Offer

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Prerequisite

Make sure you have set up communication SAP_COM_0663. For information about the API regarding SAP_COM_0663, please refer to the Set-Up Instruction.

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
| 2 | Access App | Open Reverse Offer (F5388). | The Application Jobs screen displays. |  |
| 3 | Create New Job | Choose Create. | The New Job view displays. |  |
| 4 | Enter Parameters | Make the following entries and choose Step 2:Job Template: Reverse OfferJob Name: Reverse Offer |  |  |
| 5 | Enter Parameters | Make the following entry and choose Step 3:Start Immediately: Selected |  |  |
| 6 | Enter Parameters | Make the following entries:In the Run Settings section:Run ID Prefix: ID0Simulation: UnselectedIn the Selection Criteria section:Business Partner: <Business Partner number>Contract Account: <Contract Account number>Company Code: 3310ID of Factoring Company: <for example, F_AE>Reversal Reason: <For example, 0001>In the Logs section:Problem Class: Additional Information |  |  |
| 7 | Check Job | Choose Check. | System message You can go ahead and schedule the job is displayed. |  |
| 8 | Execute Job | Choose Schedule. | The Application Jobs screen is displayed.One new application job is created with a status. |  |
| 9 | Check Job Status | After the job has been finished, choose the arrow button at the end of the entry to navigate to the job details. | The Job Log screen is displayed. The log should show no errors. |  |

|  |
| --- |
| Note If the Web service is not sent out, you could use the SAP Fiori app Send Reversal Information Again to schedule a job and reverse offer again. |

#### Receive the Response of the Factor

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The factor sends response back (normally per offer) in which a confirmation reason is given for each individual receivable.

Alternatively, manual entering of an response is also possible. Please refer to the [Create Answer of Offering Receivables Manually](#unique_139) [page ] 173 section.

Prerequisite

Make sure you have set up communication SAP_COM_0663. For information about the API regarding SAP_COM_0663, please refer to procedure below.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Navigate to SAP API HUB | Open web browser and navigate to [https://api.sap.com](https://api.sap.com/) | The SAP API hub home page is displayed. |  |
| 2 | Search Out SAP S/4HANA Cloud Public Edition API Package | Choose All and make SAP S/4HANA Cloud Public Edition as search key to locate the SAP S/4HANA Cloud Public Edition API package. | The SAP S/4HANA Cloud Public Edition API package is located. |  |
| 3 | Search Out Factoring API | Choose SAP S/4HANA Cloud Public EditionSearch Factoring. | The Factoring API is displayed. |  |

Here's an example code to receive the response of the factor:

|  |
| --- |
| Sample CodeExample Coding: Receive the response of the factor https://{{hostname}}/sap/bc/srt/scs_ext/sap/contractaccountingfactoringans <soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:glob="http://sap.com/xi/FICA/Global2"> <soapenv:Header xmlns:wsa="http://www.w3.org/2005/08/addressing"> <wsa:Action>http://sap.com/xi/FICA/Global2/ContractAccountingFactoringAnswerBulkInformation_In/ContractAccountingFactoringAnswerBulkInformation_InRequest</wsa:Action> <wsa:MessageID>uuid:f0e8c378-9ba2-4781-a105-aa4ee5f99826</wsa:MessageID> <wsa:To>https://{{hostname}}/sap/bc/srt/scs_ext/sap/contractaccountingfactoringans</wsa:To> </soapenv:Header> <soapenv:Body> <glob:ContractAccountingFactoringAnswerBulkInformation> <MessageHeader> <UUID>266d3427-cdd1-4ae5-9e20-c3d3ff5b7498</UUID> <CreationDateTime>2020-12-12T08:17:11.840Z</CreationDateTime> </MessageHeader> <ContractAccountingFactoringAnswerInfoMsg> <MessageHeader> <CreationDateTime>2020-12-12T08:17:11.848Z</CreationDateTime> </MessageHeader> <ContractAccountingFactoringAnswer> <CAFactoringCompany>{{FactorCompany}} </CAFactoringCompany> <CAMassRunDate>2020-12-12</CAMassRunDate> <CAMassRunID>AAA</CAMassRunID> <item> <CADocument>{DocumentNumber}} </CADocument> <CABPItemNumber>001</CABPItemNumber> <CAFactoringItem/> <CAFactoringConfirmationReason>0001</CAFactoringConfirmationReason> <CAFactoringCommissionPctRate>2.00</CAFactoringCommissionPctRate> <CAFactoringImmediatePaytRate>22.0</CAFactoringImmediatePaytRate> </item> </ContractAccountingFactoringAnswer> </ContractAccountingFactoringAnswerInfoMsg> </glob:ContractAccountingFactoringAnswerBulkInformation> </soapenv:Body> </soapenv:Envelope> |

#### Process the Response of the Factor

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
| 2 | Access App | Open Process Response of Factor (F5385). | The Application Jobs screen displays. |  |
| 3 | Create New Job | Choose Create. | The New Job view displays |  |
| 4 | Enter Parameters | Make the following entries and choose Step 2:Job Template: Process Response of FactorJob Name: Process Response of Factor |  |  |
| 5 | Enter Parameters | Make the following entry and choose Step 3:Start Immediately: Selected |  |  |
| 6 | Enter Parameters | Make the following entries:In the Run Settings section:Run ID Prefix: ID0Simulation: UnselectedIn the Selection Criteria section:Business Partner: <Business Partner number>Contract Account: <Contract Account number>Company Code: 3310ID of Factoring Company: <for example, F_AE>In the Logs section:Problem Class: Additional Information |  |  |
| 7 | Check Job | Choose Check. | System message You can go ahead and schedule the job is displayed. |  |
| 8 | Execute Job | Choose Schedule. | The Application Jobs screen is displayed.One new application job is created with a status. |  |
| 9 | Check Job Status | After the job has been finished, choose the arrow button at the end of the entry to navigate to the job details. | The Job Log screen is displayed. The log should show no errors. |  |

#### Buy Back Receivables from Factor (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Prerequisite

Please check and make sure the document type for Setting for Buyback of Receivables has been assigned in SSCUI: 104236.

Purpose

The entity may decide to buy back and notify the factoring company.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Administrator - Accounts Payable and Receivable (FI-CA). |  |  |
| 2 | Access App | Open Buy Back Receivables from Factor (F5975). | The Application Jobs screen is displayed. |  |
| 3 | Create New Job | Choose Create. | The New Job view displays. |  |
| 4 | Enter Parameters | Make the following entries and choose Step 2:Job Template: Buy Back Receivables from FactorJob Name: Buy Back Receivables from Factor |  |  |
| 5 | Enter Parameters | Make the following entry and choose Step 3:Start Immediately: Selected |  |  |
| 6 | Enter Parameters | Make the following entries:In the Run Settings section:Run ID Prefix: ID0Simulation run: UnselectedIn the Selection Criteria section:Company Code: 3310ID of Factoring Company: <for example, F_AE>Business Partner: <Business Partner number>Contract Account: <Contract Account number>Buyback Reason: 0001In the Logs section:Problem Class: Additional Information |  |  |
| 7 | Check Job | Choose Check. | System message You can go ahead and schedule the job is displayed. |  |
| 8 | Execute Job | Choose Schedule. | The Application Jobs screen is displayed.One new application job is created with a status. |  |
| 9 | Check Job Status | After the job has been finished, choose the arrow button at the end of the entry to navigate to the job details. | The Job Log screen is displayed. The log should show no errors. |  |

##### Receive the Response of the Factor

Purpose

The factor sends response back (normally per offer) in which a confirmation reason is given for each individual receivable.

In addition, manual entering of an response is also possible. Please refer to the [Create Answer of Offering Receivables Manually](#unique_139) [page ] 173 section.

Prerequisite

Make sure you have set up communication SAP_COM_0663. For information about the API regarding SAP_COM_0663, please refer to procedure below.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Navigate to SAP API HUB | Open web browser and navigate to [https://api.sap.com](https://api.sap.com/). | The SAP API hub home page is displayed. |  |
| 2 | Search Out SAP S/4HANA Cloud Public Edition API Package | Choose All and make SAP S/4HANA Cloud Public Edition as search key to locate the SAP S/4HANA Cloud Public Edition API package. | The SAP S/4HANA Cloud Public Edition API package is located. |  |
| 3 | Search out Factoring API | Choose SAP S/4HANA Cloud Public EditionSearch Factoring. | The Factoring API is displayed. |  |

#### Send Update to Factor

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Prerequisite

Clearing and clearing resets for sold receivables must be passed on to the factor so that the appropriate transfers can be executed:

- Payments (for example, payment run, payment lot or account maintenance)
- Clearing Reset
- Returns
- Write-Offs
- Reversal

Below is the example for how to write off an item:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Accounts Payable and Receivable Accountant (FI-CA). |  |  |
| 2 | Access App | Open Write Off Items (FP04). | The Write Off Items screen displays. |  |
| 3 | Enter Selection Details | Make the following entries:Business Partner: <Business Partner number with Open Items>Contract Account: <Contract Account number with Open Items>Document Number: <Document with Open Items> |  |  |
| 4 | Enter Specifications for Write-Off | Make the following entries:Posting Date: <Today's date>Currency: AEDClearing Reason: 04Write-Off Reason: Y1Document Type: YAReconciliation Key: <Reconciliation Key generated by system> |  |  |
| 5 | Select Open Items | Choose Select Online. | The Checking reconciliation key screen appears. |  |
| 6 | Create Reconciliation Key | Choose Yes. | A new reconciliation key is created. |  |
| 7 | Continue to Write Off | Choose Continue. | The Write Off: Process Open Items screen displays. |  |
| 8 | Activate Items | Select open items to write off by choosing Activate item button.Alternatively, double-click on the gross amount to activate a specific item for write-off. | The selected open items have been activated. The activated write off amount is displayed in the Gross Clearing field. |  |
| 9 | Post | Choose Post. | The write off documents are posted. |  |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Administrator - Accounts Payable and Receivable (FI-CA). |  |  |
| 2 | Access App | Open Send Update to Factor (F5386). | The Application Jobs screen displays. |  |
| 3 | Create New Job | Choose Create. | The New Job view displays. |  |
| 4 | Enter Parameters | Make the following entries and choose Step 2:Job Template: Send Update to FactorJob Name: Send Update to Factor |  |  |
| 5 | Enter Parameters | Make the following entry and choose Step 3:Start Immediately: Selected |  |  |
| 6 | Enter Parameters | Make the following entries:In the Run Settings section:Run ID Prefix: ID0Simulation: UnselectedIn the Selection Criteria section:Business Partner: <Business Partner number>Contract Account: <Contract Account number>Company Code: 3310ID of Factoring Company: <for example, F_AE>In the Logs section:Problem Class: Additional Information |  |  |
| 7 | Check Job | Choose Check. | System message You can go ahead and schedule the job is displayed. |  |
| 8 | Execute Job | Choose Schedule. | The Application Jobs screen is displayed.One new application job is created with a status. |  |
| 9 | Check Job Status | After the job has been finished, choose the arrow button at the end of the entry to navigate to the job details. | The Job Log screen is displayed. The log should show no errors. |  |

|  |
| --- |
| Note If the Web service is not sent out, you could use the SAP Fiori app Send Clearing Information Again to schedule a job and send clearing information again. |

#### Monitor Factoring Services

All data for business processes for factoring can be displayed in the factoring monitor (via transaction: FPFA_MON).

##### Create Answer of Offering Receivables Manually

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this case, processing of these items (manual entering of an response) is also possible from the monitor.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Administrator - Accounts Payable and Receivable (FI-CA). |  |  |
| 2 | Access App | Open Monitor Factoring Services (FPFA_MON). | The Factoring: Monitor screen displays. |  |
| 3 | Select Tab | Go to the Offer tab. |  |  |
| 4 | Enter Parameters | Create On: <Date>Run ID: <Run ID in the Offer receivables for Sale step>Date ID: <Date in the Offer receivables for Sale step>Press ENTER. | The Documents No. is displayed. |  |
| 5 | Choose Item | Select the item you want to manually enter of an response.Choose manual response. |  |  |
| 6 | Enter Parameters | Scroll to the right side and enter confirmation reason. For example, 0003 purchased.Choose save. | Manual response is saved. |  |

#### Reset Excepted Receivables

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

You could use this SAP Fiori app to reset receivable status.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Administrator - Accounts Payable and Receivable (FI-CA). |  |  |
| 2 | Access App | Open Reset Excepted Receivables (F5389). | The Application Jobs screen displays. |  |
| 3 | Create New Job | Choose Create. | The New Job view displays. |  |
| 4 | Enter Parameters | Make the following entries and choose Step 2:Job Template: Reset Excepted ReceivablesJob Name: Reset Excepted Receivables |  |  |
| 5 | Enter Parameters | Make the following entry and choose Step 3:Start Immediately: Selected |  |  |
| 6 | Enter Parameters | Make the following entries:In the Run Settings section:Run ID Prefix: ID0Simulation: UnselectedIn the Selection Criteria section:Business Partner: <Business Partner number>Contract Account: <Contract Account number>Company Code: 3310In the Logs section:Problem Class: Additional Information |  |  |
| 7 | Check Job | Choose Check. | System message You can go ahead and schedule the job is displayed. |  |
| 8 | Execute Job | Choose Schedule. | The Application Jobs screen is displayed.One new application job is created with a status. |  |
| 9 | Check Job Status | After the job has been finished, choose the arrow button at the end of the entry to navigate to the job details. | The Job Log screen is displayed. The log should show no errors. |  |

### Promise to Pay

#### Create Promise to Pay

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Context

In this process, you create promises to pay based on open items. The promises to pay create installments based on the due open items. The default values of payment dates and number of dates of the installments are defined in the category of promise to pay via configuration activity: 103765.

Prerequisite

Before creating promises to pay, please make sure that there is at least one open item that is overdue for at least one month.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Collections Specialist (FI-CA). |  |  |
| 2 | Access APP Process Promise to Pay | Open Process Promise to Pay (FP2P1). | The screen Promises to Pay of Business Partner displays. |  |
| 3 | Enter Business Partner and Company Code | Business Partner: <the number of the Business Partner that the open items belong to>Company Code: 3310 |  |  |
| 4 | Create Promise | Choose Create Promise. | The screen Create Promise to Pay: Header Data and Dates displays. |  |
| 5 | Enter Header Data | Currency: AEDCategory: 01 Standard EntryReason: 02 Customer CallConfirmation Letter: Not Required |  |  |
| 6 | Assign Open Items | Choose Assign Open Items. | The screen Promise to Pay: Process Open Items displays. |  |
| 7 | Active Open Items | Choose the Selection checkboxes for the open items.Choose Activate item. | The open amount is highlighted. The field Gross Clearing is editable. You can input the total amount or partial amount. |  |
| 8 | Enter Process Dates | Choose Process Dates. | The screen Create Promise to Pay: Header Data and Dates displays. |  |
| 9 | Enter Specification for Payment Dates | First Payment On: <default as the 1st day of next month>Payment Dates: 1 MonthlyNumber of Dates: 4Maximum per Payment: OptionalNote (Optional) You can change the default Payment Dates and Number of Dates proposed on this screen. Once the change is done, the fields Pymt Dates and Amounts get recalculated upon the click of Enter.(Optional) The proposed Pymt Dates and Amounts can be modified by selecting at least one installment and choosing the Individual Installments button. You can also assign interest and charges for the selected installments by choosing the Assign Interest and Charges button. |  |  |
| 10 | Save | Choose Save. | Promise to pay is successfully created with number. |  |

#### Create Promise to Pay for Direct Debit (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Context

In this process, you create promises to pay based on open items. The promises to pay will be paid by direct debit. For more details about the process of direct debit payment, see the [Payment Run Execution (Optional)](#unique_105) [page ] 190 section.

Prerequisite

Before creating promises to pay, please make sure that there is at least one open item that is overdue for at least one month.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Collections Specialist (FI-CA). |  |  |
| 2 | Access APP Process Promise to Pay | Open Process Promise to Pay (FP2P1). | The screen Promises to Pay of Business Partner displays. |  |
| 3 | Enter Business Partner and Company Code | Business Partner: <the number of the Business Partner that the open items belong to>Company Code: 3310 |  |  |
| 4 | Create Promise | Choose Create Promise. | The screen Create Promise to Pay: Header Data and Dates displays. |  |
| 5 | Enter Header Data | Currency: AEDCategory: 01 Standard EntryReason: 02 Customer CallConfirmation Letter: Not Required |  |  |
| 6 | Assign Open Items | Choose Assign Open Items. | The screen Promise to Pay: Process Open Items displays. |  |
| 7 | Active Open Items | Choose the Selection checkboxes for the open items.Choose Activate item. | The open amount is highlighted. The field Gross Clearing is editable. You can input the total amount or partial amount. |  |
| 8 | Enter Process Dates | Choose Process Dates. | The screen Create Promise to Pay: Header Data and Dates displays. |  |
| 9 | Enter Specification for Payment Dates | First Payment On: <The 1st day of next month by default>Payment Dates: 1 MonthlyNumber of Dates: 4Maximum per Payment: OptionalNote (Optional) You can change the default payment dates and number of dates proposed on this screen. Once the change is done, the fields Pymt Dates and Amounts get recalculated upon the click of Enter.(Optional) The proposed Pymt Dates and Amounts can be modified by selecting at least one installment and choosing the Individual Installments button. You can also assign interest and charges for the selected installments by choosing the Assign Interest and Charges button. |  |  |
| 10 | Transfer Direct Debit Payment Method | In the Details for Debit Memossection on the right side of the screen, make the following entries:Contract Account: <the contract account that the open document belongs to>Payment Method: <your direct debit payment method>Select all the installment open items and choose Transfer button.Note To ensure the successful transfer of payment method, the business partner master must be maintained with bank data . The related contract account must have direct debit maintained as incoming payment method and bank details ID correctly assigned in the master data .For European countries, SEPA Mandate needs to be maintained as well. About how to maintain SEPA Mandate, please refer to the Create SEPA Mandate section in the test script of 2DPContract Accounting – Company Initiated Payments.In European countries, Mandate reference also needs to be maintained for contact accounts. |  |  |
| 11 | Save | Choose Save. | Promise to pay is successfully created with number. |  |

|  |
| --- |
| Note Besides entering direct debit data during the creation of promise to pay, you can also add direct debit data for an existing promise to pay. To do this, access SAP Fiori app Process Promise to Pay, select an existing open promise to pay and choose Change Payment Data.To pay the direct debit installment, payment run is to be executed. You may refer to the Execute Payment Run section in the test script of 2DP - Contract Accounting – Company Initiated Payments. |

#### Create Promise to Pay with Credit Card (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this process, you create promises to pay with credit card information.

2 scenarios of promise to pay with credit card are supported:

1. Already registered credit cards with card ID maintained in the master data of the business partner.
2. One-time credit card entered during the creation and maintenance of promise to pay with integration of SAP digital payments add-on.

This section provides you with guidance on how to create promise to pay with one-time credit card.

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Collections Specialist (FI-CA). |  |  |
| 2 | Access APP Process Promise to Pay | Open Process Promise to Pay (FP2P1). | The screen Promises to Pay of Business Partner displays. |  |
| 3 | Enter Business Partner and Company Code | Make the following entries:Business Partner: <the number of the Business Partner that the open items belong to>Company Code: 3310 |  |  |
| 4 | Create Promise | Choose Create Promise. | The screen Create Promise to Pay: Header Data and Dates displays. |  |
| 5 | Enter Header Data | Make the following entries:Currency: AEDCategory: 01 Standard EntryReason: 02 Customer CallConfirmation Letter: Not Required |  |  |
| 6 | Assign Open Items | Choose Assign Open Items. | The screen Promise to Pay: Process Open Items displays. |  |
| 7 | Active Open Items | Choose the Selection checkboxes for the open items.Choose Activate item. | The open amount is highlighted. The field Gross Clearing is editable. You can input the total amount or partial amount. |  |
| 8 | Enter Process Dates | Choose Process Dates. | The screen Create Promise to Pay: Header Data and Dates displays. |  |
| 9 | Enter Specification for Payment Dates | Make the following entries:First Payment On: <default as the 1st day of next month>Payment Dates: 1 MonthlyNumber of Dates: 4Maximum per Payment: OptionalNote (Optional) You can change the default payment dates and number of dates proposed on this screen. Once the change is done, the fields Pymt Dates and Amounts get recalculated upon the click of Enter.(Optional) The proposed Pymt Dates and Amounts can be modified by selecting at least one installment and choosing the Individual Installments button. You can also assign interest and charges for the selected installments by choosing Assign Interest and Charges. |  |  |
| 10 | Enter Card Data | In the Details for Debit Memos section, choose Enter Card Data.Note If you choose the Individual Installments button, you can also register credit card for individual for individual installments. | The screen Enter Payment Data displays. |  |
| 11 | Register Card | Choose the Register Card button. | The screen Credit Card Registration displays. |  |
| 12 | Credit Card Reregistration | Make the following entries:Credit Card Type: <payment card type>Card Number: <card number>Name On Card: <owner name>Valid To: <01/01/2025>CVC: <3-digital number>Choose Submit.Note In testing systems, regarding the card type and card number, please refer to 2AR - Contract Accounting – Master Data and Basic Functions - Test Procedures - Master Data - Create a Business Partner - Procedure - Maintain Payment Data - Note for the card type and card number. | Successful manage shows: Your payment card was successfully registered.You need to close this window and switch back to the original window to continue with the following steps. |  |
| 13 | Transfer Credit Card Payment Data | In the Details for Debit Memos section on the right side of the screen, make the following entries:Contract Account: <the contract account that the open document belongs to>Payment Method: N Credit CardChoose Transfer. | The contract account, payment method and card information is transferred from the right-hand side to the left-hand side of the screen. The open items now carries credit card information. |  |
| 14 | Save | Choose Save. | The promise to pay is created. |  |

|  |
| --- |
| Note Besides entering credit card data during the creation of promise to pay, you can also add credit card data for an existing promise to pay. To do this, acces SAP Fiori app Process Promise to Pay, select an existing open promise to pay and choose Change Payment Data.To pay the credit card installment, payment run is to be executed. You may refer to the Payment Run Execution section in this test script. After the payment, you may refer to the Payment Cards: Authorize section in the test script of 2BI - Contract Accounting – Customer Initiated Payments about the settlement of credit card payment. |

#### Display Promise to Pay

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this process, you display a promises to pay with information of the open document, payment document, business partner and contract account.

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Accounts Payable and Receivable Accountant (FI-CA). |  |  |
| 2 | Access APP Process Promise to Pay | Open Display Promise to Pay (FP2P3). | The screen Display Promise to Pay is displayed. |  |
| 3 | Enter Promise to Pay Number | Make the following entry:Promise to Pay: <the number of the Promise to Pay created in previous step>Press Enter. | The screen Display Promise to Pay: Overview is displayed. |  |
| 4 | Display Header Data | Check the following entry:Promise to Pay: <the number entered in the previous step>Note Status of the promise to pay is displayed after the promise to pay number. If the promise to pay is closed, its status will be displayed as Completed; if the promise to pay is still open, its status will be displayed as Active.Double-click the number of Business Partner or Contract Account. Choose Back to navigate back to the Display Promise to Pay view.To switch to other promises to pay, choose Menu > Promise to Pay > Other Promise . |  |  |
| 5 | Simulate Valuation | Choose Header Data.Enter the following entry:Due By: For example, current date.Press Enter.Note In the valuation, the following factors are considered: how much of the promised amount has actually been paid, and how late the payments were. Please refer to step Mass Valuation Run for more details. | Fields Amount, Payment Amount, Fulfillment and Statuses are recalculated each time you enter Due By and press Enter. |  |
| 6 | Display Payment Information | Choose Payment Deadlines.Check the entries of Payment Date, Amount and Still Open in Payments Promised.Note Double-click the Payt Doc. field in Payments Made, you will drill down to the payment/clearing document. Choose Back to navigate back to the Display Promise to Pay view. |  |  |
| 7 | Display Open Document | Choose Items.Check the entries of Net Due Date and Payment Amount.Choose Acct Bal. button, you will be rerouted to the balance items displayed. This function only works for the promises to pay that are not closed. In the meantime, the list only shows items relevant to this promise to pay.Note Double-click the Document Number field, you will drill down to the original open document, where you can see the promise number in the Promise to Pay field in Basic Data. Choose Back to navigate back to the Display Promise to Pay view.Double-click the Clear. Doc. field in Payments Made, you will drill down to the payment/clearing document. Choose Back to navigate back to Display Promise to Pay view. |  |  |

#### Print Promise to Pay

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this process, you print a promises to pay.

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Administrator - Accounts Payable and Receivable (FI-CA). |  |  |
| 2 | Access APP Process Promise to Pay | Open Display Promise to Pay (FP2P3). | The screen Display Promise to Pay is displayed. |  |
| 3 | Enter Promise to Pay Number | Make the following entry:Promise to Pay: <the number of the Promise to Pay created in previous step>Press Enter. | The screen Display Promise to Pay: Overview is displayed. |  |
| 4 | Enter Print Queue | Select menu More > Promise to Pay > Print (Ctrl+P), or click Print on the upper right corner of this screen.Make the following entries:Output Channel: <Choose Print as an example>Print Queue: <Choose DEFULT as an example>Choose Set in Print Dataset. | The print request is sent to print queue. |  |
| 5 | Access APP Print Correspondence | Open Print Correspondence (F3537). | The Application Jobs screen displays. |  |
| 6 | Create New Print job | Choose Create. | The screen New Job: Print FI-CA Correspondences displays. |  |
| 7 | Enter Parameter for Job Template | Make the following entries and choose Step 2:Job Template: FI-CA: Print CorrespondenceJob Name: FI-CA: Print CorrespondenceStart Immediately: SelectedChoose Step 3.Run ID Prefix: <Enter a value as you want>Business Partner: <the number of the Business Partner in previous steps>Contract Account: <the number of the Contract Account in previous steps>Company Code: 3310Correspondence Type: 0045 Promise to PayPrint Queue: <the print queue you chose in previous test step>Type of Print: Actual PrintSelect Schedule. | Job is scheduled. Job status is Finished. Navigate to job log status, a message Document xxxxxxxxxxxx was printed is displayed. |  |

#### Replace Promise to Pay (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this process, you replace a promises to pay with a new one. By doing so, the previous promise to pay is closed, while a new promise to pay is generated.

Prerequisite

There must be at least one open promise to pay and one open item.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Collections Specialist (FI-CA). |  |  |
| 2 | Access APP Process Promise to Pay | Open Process Promise to Pay (FP2P1). | The screen Promises to Pay of Business Partner is displayed. |  |
| 3 | Enter Business Partner and Company Code | Business Partner: <the number of the Business Partner in previous steps>Company Code: 3310Choose one of the promise to pay listed on the screen. |  |  |
| 4 | Replace Promise to Pay | Choose Replace Promise. | The screen Replace Promise to Pay: Details of Withdrawal displays. |  |
| 5 | Select Reason for Withdrawal | Reason for Withdrawal: 01 Replaced by Other PromiseInitiator of Withdrawal: 5 We Cancel the PromiseChoose For New Promise to Pay . | The screen Replace Promises to Pay: Header Data and Dates is displayed. |  |
| 6 | Enter Header Data for New Promise to Pay | Currency: AEDCategory: 01 Standard EntryReason: 02 Customer CallConfirmation Letter: Not Required |  |  |
| 7 | Assign Open Items | Choose Assign Open Items. | The screen Promise to Pay: Process Open Items displays. |  |
| 8 | Active Open Items | Choose the Selection checkboxes for the open items.Choose Activate item. | The open amount is highlighted. The field Gross Clearing is editable. You can input the total amount or partial amount. |  |
| 9 | Enter Process Dates | Choose Process Dates. | The screen Replace Promises to Pay: Header Data and Dates displays. |  |
| 10 | Enter Specification for Payment Dates | First Payment On: <The 1st day of next month by default>Payment Dates: 1 MonthlyNumber of Dates: 4Maximum per Payment: OptionalNote (Optional) You can change the default payment dates and number of dates proposed on this screen. Once the change is done, the fields Pymt Dates and Amounts get recalculated upon the click of Enter.Note (Optional) The proposed Pymt Dates and Amounts can be modified by selecting at least one installment and choosing the Individual Installments button. You can also assign interest and charges for the selected installments by choosing the Assign Interest and Charges button. |  |  |
| 11 | Save | Choose Save. | The previous promise to pay is closed, while a new promise to pay is generated with new ID. |  |

#### Payment for Promise to Pay

Context

In the Create Promise to Pay section, installments are generated for manual payment. In the Create Promise to Pay for Direct Debit section, you assign direct debit payment method for the installments. In the Create Promise to Pay with Credit Card section, you assign credit card payment method for the installments. This section describes the steps of manual payment by payment lot (to clear the installments created in the Create Promise to Pay section) payment run (to clear the installments created in the Create Promise to Pay for Direct Debit section and the Create Promise to Pay with Credit Card section).

##### Manual Payment by Payment Lot

###### Create Payment Lot

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
| 1 | Log On | Log on to the SAP Fiori launchpad as an Accounts Payable and Receivable Accountant (FI-CA). |  |  |
| 2 | Access App | Open Process Payment Lot (FP05). | Payment Lot: Initial Screen displays. |  |
| 3 | Input Parameters for Payment Lot | Create your payment lot ID and choose Create:Lot: <Your payment lot ID>Make the following entries on the Payment Lot Create: Default Entries and Status screen:Control Information:Lot: <Your payment lot ID>Search Term: <Input your search information>Additional Info: <Input your specific information>Specifications for Posting Documents:Document Type: <by default>Posting Date: <by default>Document Date: <by default>Reconciliation Key: <Generated by the system>Currency: AEDSpecification for Posting Items on Bank Clearing Account:Bank Clearing Account: 11001080Company Code: 3310House Bank: AEBK2Account ID: AEAC2Value Date: <Today's date>Selections for Selecting and Clearing Open Items:Clearing Reason: <01, by default>Selection Category: <by default>Line Layout: SAPClick New Items.On the Payment Lot Create: Payments screen, check and make the following entries:In the Default values and status section: <Values are maintained by default>In the Payments section:Payment Amount: <Input the amount>Selection Category 1: select 0Selection Value 1: <the number of promise to pay created in step Create Promise to Pay >Note G stands for business partner, K stands for contract account, B stands for document, 0 stands for promise to pay.If parameters you input are in accordance with the open items, the payment lot can clear open items of specific business partner, otherwise, it needs further clarification.If you want to create payment lot through payment advice note, you need to create payment advice note with selection category P in advance. Then you can directly input payment advice note with selection category P.Click Save. | Payment lot is created. |  |

###### Post Payment Lot

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
| 1 | Log On | Log on to the SAP Fiori launchpad as an Accounts Payable and Receivable Accountant (FI-CA). |  |  |
| 2 | Access App | Open Process Payment Lot (FP05). | Payment Lot: Initial Screen displays. |  |
| 3 | Post Payment Lot | Input your payment lot ID on the Payment Lot: Initial Screen.Lot: <Your payment lot ID>Choose Close.Note Payment lot must be closed before it can be posted.Choose Yes when message appears: All payment entered in full?Choose Post.In the Schedule Job dialog box, choose Start online and choose OK.Choose Continue when message appears: Posting run is complete, check status.In the Status section, system shows the posting status.Postprocessing is required means the payment needs further clarification. | Payment lot is closed and posted. |  |

##### Payment Run Execution (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Context

In this activity, you can create payment documents by mass run.

Prerequisite

Before you execute payment run, make sure account determination is set up correctly via configuration activities as below.

Depending on your configuration environment for SAP S/4HANA Cloud Public Edition, choose one of the following options:

Configure Your Solution:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. |  |  |
| 2 | Access App Manage Your Solution | Open Manage Your Solution and then choose Configure Your Solution. | The Manage Your Solution screen is displayed. |  |
| 3 | Access App Define Accounts for Payment Program | Search with following criteria:Application Area: FinanceSub Application Area: Contract AccountingChoose the group Company Initiated Payments.Choose the configuration step Define Accounts for Payment Program. | The Maintain Payment Program Bank Accounts: Overview screen is displayed. |  |
| 4 | Check or Add Entries for Account Determination | Choose Create and add an entry for company code.Paying Company Code: <For example, 3310. Do not enter * in this field>House Bank: <For example,AEBK1. Do not enter * in this field>Payment Method: <For example, E. Do not enter * in this field>Currency: <For example, AED. Do not enter * in this field>Account ID: <For example, AEAC1>Tax: <Make sure * is maintained. Only input blank or X for Romania VAT split purpose.>Save the entry. | Account determination entries are saved successfully. |  |

SAP Central Business Configuration:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the project experience in SAP Central Business Configuration. |  |  |
| 2 | Open Define Selection Criteria for Credit Clarification | Go to the Business Processes Configuration app and search for the following activity: Define Accounts for Payment Program.Choose Open Documentation for the found line item to see more details about this configuration activity.Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. | The Change View "Credit Processing: Customizing ID Credit ": Overview screen is displayed. |  |
| 3 | Input Parameters | Choose Create and add an entry for company code.Paying Company Code: <For example, 3310. Do not enter * in this field>House Bank: <For example, AEBK1. Do not enter * in this field>Payment Method: <For example, E. Do not enter * in this field>Currency: <For example, AED. Do not enter * in this field>Account ID: <For example, AEAC1>Tax: <Make sure * is maintained. Only input blank or X for Romania VAT split purpose.>Save the entry. | Account determination entries are saved successfully. |  |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Administrator - Accounts Payable and Receivable (FI-CA). |  |  |
| 2 | Access App | Open Payment Run / Debit Memo Run (F3529). | The Application Jobs screen displays. |  |
| 3 | Create New Job | Choose Create. | The New Job: FICA Payment Run screen displays. |  |
| 4 | Maintain Parameters | Make the following entries and choose Step 2:Job Template: FI-CA Payment RunJob Name: FI-CA Payment Run |  |  |
| 5 | Maintain Parameters | Make the following entry and choose Step 3:Start Immediately: Selected |  |  |
| 6 | Maintain Parameters | Make the following entries:Run ID Prefix: For example, ID0Simulation run.: UnselectedPromise to Pay: SelectedBusiness Partner: <Select Business Partner that the open item belonged to>Contract Account: <Select Contract Account number that the open item belonged to>Company Code: 3310Promise to Pay: <Select the Promise to Pay in step Create Promise to Pay for Direct Debit or step Create Promise to Pay with Credit Card>Due by: <the due date + 1 of the 1st installment of the promise to pay>Payment Method List: <Select payment method list for your country>Country Key: AESelection ID: 3310The Dynamic Date Function is available for parameters of date, you can also use the Dynamic Date Function with the Define Recurrence Pattern to set up the Recurring run for Mass activity for your business needs. For example, you can choose the dynamic date function LASTDAYOFCURRENTMONTH for testing purpose. |  |  |
| 7 | Check Job | Choose Check. | System message You can go ahead and schedule the job is displayed, For credit card outgoing payment, after execute payment run generated clearing document, please follow/refer to step: Payment Card Settlement in 2BI. |  |
| 8 | Execute Job | Choose Schedule. | The Application Jobs screen is displayed. One new application job is created with a status. Payment documents are created from job log details. |  |
| 9 | Check Job Status | After the job has been finished, choose the arrow button at the end of the entry to navigate to the job details.Note In particular cases, if the payment method assigned to the installment is direct debit by payment order, the payment orders are generated after payment run. For details of payment order processing, please refer to the Sample Bank Statement for Payment Order Lot section in the test script of scope item 2DPContract Accounting – Company Initiated Payments. | The Job Log screen is displayed. The log should show no errors.The Run Identification should combine Run ID Prefix + dynamic number (xx).The success message displays: Clearing document xxxxxx posted.Display the promise to pay, on the tab Payment Deadlines, you can find the payment document listed on the right side of the screen. |  |

#### Mass Valuation Run

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Context

During valuation, how late the payments are and how much of the promised amount has actually been paid are taken into consideration. With regard to the delay in payment, in customizing, you can define a number of tolerance days and what reduction in the valuation is made for each day in excess of these tolerance days. You define this for each company code (SSCUI 103809).

The system automatically sets the first check date when a promise to pay is created. It is by default seven days after the due date of the middle installment. During the check, the decision must be made whether a further check is necessary at a later date, and the promise is open until then, or whether the promise is to be closed in its current status. The new check date is seven days after the due date of the last installment. If the date determined in this way is not in the future, the promise to pay is also closed.

In this process, you valuate the promise to pay. Valuation of the promise to pay consists of determining the level of fulfillment of the promise as a percentage between 0.00% and 100.00%. The system derives a status based on this level of fulfillment and your system settings.

Procedure

| ProcedureTest Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Administrator - Accounts Payable and Receivable (FI-CA). |  |  |
| 2 | Access APP Process Promise to Pay | Open Valuate Promise to Pay (F5058). | The screen Application Jobs displays. |  |
| 3 | Create | Choose Create. | The screen New Job: Valuate Promise to Pay displays. |  |
| 4 | Enter Required Parameters | Make the following entries and choose Step 2:Job Template: Valuate Promise to PayJob Name: Valuate Promise to Pay |  |  |
| 5 | Enter Required Parameters | Make the following entries and choose Step 3:Start Immediately: SelectedStart: <Today's Date> |  |  |
| 6 | Enter Required Parameters | Make the following entries:Run ID Prefix: For example, ID0Promise to Pay: <the number of promise to pay created in step Create Promise to Pay>Check Date: <refer to the check date in the header data of the promise to pay>Posting Date: <Today's Date>Business Partner: <the business partner assigned to this promise to pay>Company Code: 3310Document Date: <Today's Date>Simulation Run: Unselected |  |  |
| 7 | Check Job | Choose Check. | System message You can go ahead and schedule the job is displayed. Recon. Key is generated by system automatically. |  |
| 8 | Execute Job | Choose Schedule. | The screen Application Jobs is displayed.One new application job is created with a status. |  |
| 9 | Display Job | After the job has been finished, choose the arrow button at the end of the entry to navigate to the job details. | The screen Job Log is displayed.The Run Identification should combine Run ID Prefix + dynamic number (xx).Check the log and the message type Success is displayed.Display the promise to pay, the next check date is set to 7 days after the last installment. |  |

#### Withdraw Promise to Pay

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Context

By withdrawing a promise to pay, you can determine whether the credit worthiness of the business partner is to be updated or not, or the interst is to be reversed or not. These can be defined in the reasons of withdrawal (SSCUI 103767).

Purpose

In this process, you withdraw the promise to pay. After the withdrawal, the promise to pay is closed. The open items originally belonged to the withdrawn promise to pay become selectable for other new promise to pay.

Prerequisite

There must be at lease one open promise to pay.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as Accounts Payable and Receivable Accountant (FI-CA). |  |  |
| 2 | Access APP Process Promise to Pay | Open Process Promise to Pay (FP2P1). | The screen Promises to Pay of Business Partner is displayed. |  |
| 3 | Enter Business Partner and Company Code | Make the following entry:Business Partner: <the number of the Business Partner in previous step>Company Code: 3310Press Enter. | The list of promises to pay created for the specific business partner is displayed. |  |
| 4 | Withdraw Promise to Pay | Select the promise to pay created in step Create Promise to Pay.Choose Withdraw Promise. | The screen Withdraw Promise to Pay displays. |  |
| 5 | Select Reason for Withdrawal | Make the following entry:Reason for Withdrawal: 2 Withdrawn by CustomerInitiator of Withdrawal: 5 Customer withdraws promise to payChoose Execute Withdrawal. | Success message shows at the button of the screen: Promise to pay XXXXXXXXXXX was withdrawn. |  |

### Handling of Service Provider Bills in Deregulated Market

Purpose

In this section, you can handle the Service Provider Bills in deregulated market.

Prerequisite

Before you start, make sure you have added your Business Partner to be used in following steps to Payment Information Integration in Communication Arrangement (refer to Setting Up Contract Accounting - Open Item Management (2UJ)), and have completed below steps:

|  |
| --- |
| Note Make sure your business partner used in below test steps maintained in communication arrangement (Payment Information Integration), or you have a fixed value * configured for business partner in your communication arrangement ,the system will try to find a communication arrangement specific to a business partner. If not, the system will select the communication arrangement with fixed value * for business partner. |

1. Make Settings for Information Container Categories

Depending on your configuration environment for SAP S/4HANA Cloud Public Edition, choose one of the following options:

Configure Your Solution:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad with your user credentials as Configuration Expert - Business Process Configuration role assigned. | The SAP Fiori Launchpad is displayed. |  |
| 2 | Access App | Open Manage Your Solution (F1241) and then choose Configure Your Solution. | The Manage Your Solution screen is displayed. |  |
| 3 | Input Parameters | Application Area: FinanceSub Application Area: Contract AccountingItem Name: Information ContainerSelect Configuration, choose step Make Settings for Information Container Categories.Choose New entries.InfoCat: <0003>Active: selectedActive From: <today’s date>Active To: <12/31/9999>Send Type: <05 SOAP API>Choose Save. | The settings for Information Container Categories is completed. |  |

SAP Central Business Configuration:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the project experience in SAP Central Business Configuration. |  |  |
| 2 | Open Activi-ty to Make Settings for Information Container Categories | Go to the Business Processes Configuration app and search for the following activity: Make Settings for Information Container Categories.Choose Open Documentation for the found line item to see more details about this configuration activity.Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. | The settings for Information Container Categories is completed. |  |
| 3 | Input Parameters | Choose New entries.InfoCat: <0003>Active: selectedActive From: <today’s date>Active To: <12/31/9999>Send Type: <05 SOAP API>Choose Save. |  |  |

#### Post Documents

In this activity, you create customer receivables. To do so, refer to the chapter Preliminary Steps - Post Documents.

#### Change Document

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Context

Full Clearing and Payment Info can be assigned independently.

When the Full Clearing flag is set, Payment Run should not be able to partially post a partial payment to the document. Also note that no payment transaction else than Payment Run will be able to post a full or partial payment to the document.

When Payment Info flag is set, Payment Run will create a so-called InfoContainer of category 0003, which is the payment information from payment run.

In this activity, you change the document posted in previous step to flag Full Clearing and Payment Info the in document line item.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Accounts Payable and Receivable Accountant (FI-CA). |  |  |
| 2 | Access App | Open Change Document (FPE2). | The Change Document: Initial Screen is displayed. |  |
| 3 | Select Document | Make the following entries and press Enter:Document Number: <Document Number Posted in previous step>BP Item: Y01G/L Item: Y01 | The Change Document: Overview screen is displayed. |  |
| 4 | Select Document Item | Choose Menu > Goto > Business Partner Item list . | The Change Document: Item screen is displayed. |  |
| 5 | Enter Change | Double click the Business Partner item entry.Choose the Payt data tab and make the following entries:Payment Data:Full clearing: SelectedPayment Info:01 |  |  |
| 6 | Save | Choose Save. | Change is saved. |  |

#### Execute Payment Run

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Procedure

In this activity, you can create payment documents by mass run.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Administrator - Accounts Payable and Receivable (FI-CA). |  |  |
| 2 | Access App | Open Payment Run / Debit Memo Run (F3529). | The Application Jobs screen displays. |  |
| 3 | Create | Choose Create. | The New Job screen displays. |  |
| 4 | Maintain Parameters | Make the following entries and choose Step 2:Job Template: FI-CA Payment RunJob Name: FI-CA Payment Run |  |  |
| 5 | Maintain Parameters | Make the following entry and choose Step 3:Start Immediately: Selected |  |  |
| 6 | Maintain Parameters | Make the following entries:Run Settings:Prefix of Run ID: For example, ID0Reconcil. Key: <Reconciliation Key generated by system>Simulation run: UnselectedSelection Criteria:Open Items: SelectedWith repayment requests: SelectedBusiness Partner: <Business Partner>Contract Account: <Contract Account>Company Code: 3310Due by: <Today's Date + 1 Year>Payment Method List: <Select payment method list for your country>Country Key: AEFurther Settings:Posting Date: <Today's date>Selection ID: 3310Note The Dynamic Date Function is available for parameters of date, you can also use the Dynamic Date Function with the Define Recurrence Pattern to set up the recurring run for mass activity for your business needs. For example, you can choose the dynamic date function LASTDAYOFCURRENTMONTH for testing purpose. |  |  |
| 7 | Check Job | Choose Check. | System message You can go ahead and schedule the job is displayed. |  |
| 8 | Execute Job | Choose Schedule. | The Application Jobs screen is displayed. One new application job is created with a status. Payment documents are created from job log details. |  |
| 9 | Check Job Status | After the job has been finished, choose the arrow button at the end of the entry to navigate to the job details. | The Job Log screen is displayed. The log should show no errors.The Run Identification should combine Run ID Prefix + dynamic number (xx). |  |

#### Check Information Container Creation

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
| 2 | Access App | Open Display Information Container (FPINFCO2). | The Display Information Container screen is displayed. |  |
| 3 | Select Information Container | Make the following entries:Master Data:Business Partner: <Business Partner>Contract Account: <Contract Account>AttributesInformation Contain.Cat: <0003>Choose Execute. | The Display of Information Container Entries screen is displayed. |  |

#### Send Data from Information Container

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Prerequisite

Make sure you have completed settings for Communication scenario ID SAP_COM_0682-Contract Accounting - Payment Information Integration.

Before you send data from information Container, refer to Setting Up Contract Accounting - Open Item Management (2UJ).

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Administrator - Accounts Payable and Receivable (FI-CA). |  |  |
| 2 | Access App | Open Forward Data from Information Container (F5792). | The Application Jobs screen displays. |  |
| 3 | Create | Choose Create. | The New Job: Send Data from Infocontainer screen displays. |  |
| 4 | Maintain Parameters | Make the following entries and choose Step 2:Job Template: Send Data to InfocontainerJob Name: Send Data to Infocontainer |  |  |
| 5 | Maintain Parameters | Make the following entry and choose Step 3:Start Immediately: Selected |  |  |
| 6 | Maintain Parameters | Make the following entries:Run Identification:Run ID Prefix: For example, ID0Selection Parameters:Simulation Run: UnselectedBusiness Partner: <Business Partner>Information Contain.Cat: <0003>Contract Account: <Contract Account>Settings for Application Log:Problem Class: Additional Information |  |  |
| 7 | Check Job | Choose Check. | System message You can go ahead and schedule the job is displayed. |  |
| 8 | Execute Job | Choose Schedule. | The Application Jobs screen is displayed. One new application job is created . |  |
| 9 | Check Job Status | After the job has been finished, choose the arrow button at the end of the entry to navigate to the job details. | The Job Log screen is displayed. The log should show no errors.The Run Identification should combine Run ID Prefix + dynamic number (xx). |  |

#### Check the Send Status of Information Container

Procedure

In this activity, you display the information container and verify the send status of information container. To do so, refer to step Check Information Container Creation.

#### Reset the Send Status of Information Container

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you can reset the send status for the information container with failed status.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Administrator - Accounts Payable and Receivable (FI-CA). |  |  |
| 2 | Access App | Open Information Container: Reset Send (FPINFCO3). | The Display Information Containerscreen is displayed. |  |
| 3 | Select Information Container | Make the following entries:Master Data:Business Partner: <Business Partner>Contract Account: <Contract Account>AttributesInformation Contain.Cat: <0003>Choose Execute. | The Display of Information Container Entries screen is displayed. |  |
| 4 | Choose Item | Select the items you want to reset the send status.Choose menu Edit > Reset Send Status .Confirm the information. | The Information Containers should reflect with the new send status. |  |

### Transfer Business Partner Postings to External Systems

Purpose

In this section, you can forward information about business partner postings to external systems.

Prerequisites

1. Communication Setup

Make sure you have set up the Communication Scenario SAP_COM_0361 (Finance - Contract Accounting Open Item Management Integration). For more information on the Communication Scenario SAP_COM_0361, please refer to:

[Link to Set-Up Instructions](https://help.sap.com/docs/SAP_S4HANA_BEST_PRACTICES/b2098e326cb819568df6ca544d204677)

Configuration Activities

-
    1. Define identification for external system:

Depending on your configuration environment for SAP S/4HANA Cloud Public Edition, choose one of the following options:

Configure Your Solution:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad with your user credentials as Configuration Expert - Business Process Configuration role assigned. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access App | Open Manage Your Solution (F1241) and then choose Configure Your Solution. | The Manage Your Solution screen is displayed. |  |
| 3 | Input Parameters | Application Area: FinanceSub Application Area: Contract AccountingItem Name: Transfer of Business Partner Postings to External SystemsChoose Configure for configuration activityDefine Identification for External System.Choose New Entries and input the following entries:ExtSys: <for example, EXS>Name: <for example, external system>Choose Save. | The external system ID is created. |  |

SAP Central Business Configuration:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the project experience in SAP Central Business Configuration. |  |  |
| 2 | Open Make Settings for Information Container Categories | Go to the Business Processes Configuration app and search for the following activity: Make Settings for Information Container Categories.Choose Open Documentation for the found line item to see more details about this configuration activity.Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. |  |  |
| 3 | Input Parameters | Choose New Entries and input the following entries:ExtSys: <for example, EXS>Name: <for example, external system>Choose Save. | Settings for Information Container Categories are completed. |  |

-
    1. Maintain settings for company code:

Depending on your configuration environment for SAP S/4HANA Cloud Public Edition, choose one of the following options:

Configure Your Solution:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad with your user credentials as Configuration Expert - Business Process Configuration role assigned. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access App | Open Manage Your Solution (F1241) and then choose Configure Your Solution. | The Manage Your Solution screen is displayed. |  |
| 3 | Input Parameters | Application Area: FinanceSub Application Area: Contract AccountingItem Name: Transfer of Business Partner Postings to External SystemsChoose Configure for configuration activityMaintain Settings for Company Code.Choose New Entries and input the following entries:Cocd: 3310Open Items: <selected>Clrd Items: <selected>Payments: <selected>Reopened: <selected>Choose Save.Note You can choose different settings per your business requirements. | Settings for your company code are completed. |  |

SAP Central Business Configuration:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the project experience in SAP Central Business Configuration. |  |  |
| 2 | Open Make Settings for Information Container Categories | Go to the Business Processes Configuration app and search for the following activity: Maintain Settings for Company Code.Choose Open Documentation for the found line item to see more details about this configuration activity.Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. |  |  |
| 3 | Input Parameters | Choose New Entries and input the following entries:Cocd: 3310Open Items: <selected>Clrd Items: <selected>Payments: <selected>Reopened: <selected>Choose Save.Note You can choose different settings per your business requirements. | Settings for your company code are completed. |  |

-
    1. Maintain settings for recipient system:

Depending on your configuration environment for SAP S/4HANA Cloud Public Edition, choose one of the following options:

Configure Your Solution:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad with your user credentials as Configuration Expert - Business Process Configuration role assigned. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access App | Open Manage Your Solution (F1241) and then choose Configure Your Solution. | The Manage Your Solution screen is displayed. |  |
| 3 | Input Parameters | Application Area: FinanceSub Application Area: Contract AccountingItem Name: Transfer of Business Partner Postings to External SystemsChoose Configure for configuration activityMaintain Settings for Recipient System.Choose New Entries and input the following entries:ExtSys: <choose external system ID you created in step 2>BPartner: <blank>Cont.Acct: <selected>Contract: <blank>Note You can select exactly one level for transfer between Business Partner, Contract Account and Contract. Contract Account is selected for testing purpose.W/o Contr.: <blank>Open Items: <selected>Clrd Items: <selected>Payments.: <selected>Reopened: <selected>Inst.Plans: <selected>Ext.PtrNo: <selected>Ext.CactNo: <selected>Ext.Ctr: <blank>TimeDelet: <blank>Choose Save.Note You can choose different settings per your business requirements. | Settings for your receiver system are completed. |  |

SAP Central Business Configuration:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the project experience in SAP Central Business Configuration. |  |  |
| 2 | Open Maintain Settings for Recipient System | Go to the Business Processes Configuration app and search for the following activity: Maintain Settings for Recipient System.Choose Open Documentation for the found line item to see more details about this configuration activity.Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. |  |  |
| 3 | Input Parameters | Choose New Entries and input the following entries:ExtSys: <choose external system ID you created in step 2>BPartner: <blank>Cont.Acct: <selected>Contract: <blank>Note You can select exactly one level for transfer between Business Partner, Contract Account and Contract. Contract Account is selected for testing purpose.W/o Contr.: <blank>Open Items: <selected>Clrd Items: <selected>Payments.: <selected>Reopened: <selected>Inst.Plans: <selected>Ext.PtrNo: <selected>Ext.CactNo: <selected>Ext.Ctr: <blank>TimeDelet: <blank>Choose Save.Note You can choose different settings per your business requirements. | Settings for your receiver system are completed. |  |

1. Master Data Preparation (Optional)

Maintain external ID for your business partners, contract accounts or provider contracts.

|  |
| --- |
| Note For performance reasons, you should only set this indicator if you really need the external number for your business partners, contract accounts or provider contracts for your identification. |

-
    1. Maintain external number for business partner master data:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad with your user credentials as an Administrator - Accounts Payable and Receivable (FI-CA). | The SAP Fiori launchpad is displayed. |  |
| 2 | Access App | Open Maintain Business Partner (BP). | The Application Jobs screen displays. |  |
| 3 | Enter Basic Parameters | Make the following entry:Business Partner: <Business Partner number>Press Enter. Double-click Business Partner. |  |  |
| 4 | Select BP Role | Switch to Change mode.Choose the Identification tab and make the following change:External BP Number: <Your external number of business partner>Choose Save. |  |  |

-
    1. Maintain external number for contract account master data:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad with your user credentials as an Administrator - Accounts Payable and Receivable (FI-CA). | The SAP Fiori launchpad is displayed. |  |
| 2 | Access App | Open Maintain Contract Account (CAA3). | The Contract account Display: Initial Screen displays. |  |
| 3 | Enter Contract Account Number | Make the following entry and choose Continue:Contract Acct: <Contract Account number> | The Contract account Display: General Data screen displays. |  |
| 4 | Switch to Change Mode | Choose Change and check the following entry:Contract Acct: <Contract Account number> | The change mode is on. |  |
| 5 | Continue | Choose Continue. | The Contract account Change: General Data screen displays. |  |
| 6 | Make Change | Make the following entry:CAcctLegacySys: <external number of your contract account> |  |  |
| 7 | Save Change | Choose Save. | Change is saved. |  |

-
    1. Maintain external number for provider contract account master data:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad with your user credentials as an Accounts Payable and Receivable Accountant (FI-CA). | The SAP Fiori launchpad is displayed. |  |
| 2 | Access App | Open Maintain Provider Contract (FP_VT3). | The Provider Contract Display: Initial Screen displays. |  |
| 3 | Enter Basic Data | Make the following entry:Provider Contract: <Provider Contract ID>Business Partner: <Business Partner ID> for example, BP_AE_99 |  |  |
| 4 | Execute | Choose Change in Display/Change mode, then choose Continue. | The Provider Contract Display/Change screen is displayed. |  |
| 5 | Make Change | Make the following change:Key in External System: <external number of provider contract account> |  |  |
| 6 | Save Change | Choose Save. | Change is saved. |  |

1. Assign recipients to users:

This process shows you how to assign recipients to users so you can monitor status for documents sent to the external system.

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad with your user credentials as an Configuration Expert - Business Network Integration. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access App | Open Assign Recipients to Users (F2949).Enter CONF_EXPERT_BUS_NET_INT in the filter bar, then select it from the list. | Recipients for User is displayed. |  |
| 3 | Assign Recipient | Choose Assign Recipient.Namespace: /FINCARecipient Name: CA_BLKOI_OUT_RECIPIENTChoose Assign. | Message: Assignment successful displays. |  |

1. Documents preparation for your master data created in steps above.

|  |
| --- |
| Note Based on your selection in Preprereuiste step 2: Configuration Activities settings, you need to prepare the testing documents for open items, cleared items, payment document, reopen documents and installment plan documents. They must be created after you complete the Preprereuiste step 2: Configuration Activities settings. |

#### Transfer Business Partner Postings to External Systems

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Procedure

In this activity, you can transfer business partner postings to external systems.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Accounts Payable and Receivable Accountant (FI-CA). |  |  |
| 2 | Access App | Open Transfer Business Partner Postings to External Systems (F8476). | The Transfer Business Partner Postings to External Systems screen displays. |  |
| 3 | Create New Job | Choose Create. | The new Job: FI-CA: Outbound Interface Notify Business Partner Postings screen displays. |  |
| 4 | Enter Required Parameters | Make the following entries and choose Step 2:Job Template: FI-CA: Outbound Interface Notify Business Partner PostingsJob Name: FI-CA: Outbound Interface Notify Business Partner Postings |  |  |
| 5 | Enter Posting Parameters | Make the following entry and choose Step 3:Start Immediately: Selected |  |  |
| 6 | Enter Posting Parameters | Make the following entries:Run Settings:Prefix of Run ID: For example, ID0Simulation run: UnselectedGeneral Selections:Business Partner.: <your business partner ID>Company Code: 3310External System: <your external system ID defined in prerequisite> |  |  |
| 7 | Check Job | Choose Check. | System message You can go ahead and schedule the job is displayed. |  |
| 8 | Execute Job | Choose Schedule. | The Application Jobs screen is displayed. One new application job is created with a status. Payment documents are created from job log details. |  |
| 9 | Check Job Status | After the job has been finished, choose the arrow button at the end of the entry to navigate to the job details. | The Job Log screen is displayed. The log should show no errors.The Run Identification should combine Run ID Prefix + dynamic number (xx). |  |

#### Monitor Status Tranferred to External Systems

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Procedure

In this activity, you can monitor status for business partner postings transferred to external systems.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Configuration Expert - Business Network Integration. |  |  |
| 2 | Access App | Open Message Dashboard - SAP Application Interface Framework (/AIFX/WDA0005). | The Message Dashboard - SAP Application Interface Framework screen displays. |  |
| 3 | Enter Time Phase | Enter your time phase, then choose Search:From (Date/Time): <from time>To (Date/Time): <to time> |  |  |
| 4 | Check Transfer Status | From the result list, select the interface item of BLKOI_OT, and choose the number in column All Messages. | On the Monitoring and Error Handling screen, data messages are displayed with detailed information. |  |

#### Delete Trigger Data for Data Transfer to External Systems (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Procedure

This activity allows you to delete entries that have been transferred from the trigger tables after a specified number of days.

|  |
| --- |
| Note You can specify the days for your external system in [Transfer Business Partner Postings to External Systems](#unique_142) [page ] 205> Prerequisites > Maintain settings for recipient system. If the field TimeDelet remains blank, it is only the trigger entries that are older than 180 days that have been deleted. |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Accounts Payable and Receivable Accountant (FI-CA). |  |  |
| 2 | Access App | Open Delete Trigger Data for Data Transfer to External Systems (F8475). | The Delete Trigger Data for Data Transfer to External Systems screen displays. |  |
| 3 | Create New Job | Choose Create. | The New Job: FI-CA: Outbound Interface Delete Trigger screen displays. |  |
| 4 | Enter Required Parameters | Make the following entries and choose Step 2:Job Template: FI-CA: Outbound Interface Delete TriggerJob Name: FI-CA: Outbound Interface Delete Trigger |  |  |
| 5 | Enter Posting Parameters | Make the following entry and choose Step 3:Start Immediately: Selected |  |  |
| 6 | Enter Posting Parameters | Make the following entries:Run Settings:Prefix of Run ID: For example, ID0Simulation run: UnselectedGeneral Selections:Business Partner.: <your business partner ID>Company Code: 3310External System: <your external system ID defined in prerequisite> |  |  |
| 7 | Check Job | Choose Check. | System message You can go ahead and schedule the job is displayed. |  |
| 8 | Execute Job | Choose Schedule. | The Application Jobs screen is displayed. One new application job is created with a status. Payment documents are created from job log details. |  |
| 9 | Check Job Status | After the job has been finished, choose the arrow button at the end of the entry to navigate to the job details. | The Job Log screen is displayed. The log should show no errors.The Run Identification should combine Run ID Prefix + dynamic number (xx). |  |

### Transfer Documents to Accounts Payable/Accounts Receivable

Purpose

With this activity, you can transfer documents from Contract Accounting to Accounts Payable/Accounts Receivable.

Prerequisites

Master data:

The business partner must have a customer role (FLCU00).

In this procedure, you can refer to Contract Account CA_AE_23 and create a new contract account for business partner 33100023. Then, assign a subledger to the newly created contract account.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad with your user credentials as Accounts Payable and Receivable Accountant (FI-CA) role assigned. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Maintain Contract Account (CAA3). | The Contract account Display: Initial Screen displays. |  |
| 3 | Create | Choose Create and make the following entry:Contract Acct: <new Contract Account ID, for example, AE_CA_66>Business Partner: <33100023>Cont. Acct Cat.: <Y1>Ref.Account:Contract Acct: <CA_AE_23>Business Partn.: <33100023> | The change mode is on. |  |
| 6 | Continue | Choose Continue. | The Contract account Create: General Data screen displays. |  |
| 7 | Enter Change | Make the following entry:Subledger: <FI> |  |  |
| 8 | Save | Choose Save. | The new contract AE_CA_66 has been created.Note down the new contract account number. |  |

|  |
| --- |
| Note To transfer documents from Contract Accounting to Accounts Payable, ensure that you complete the necessary settings using Configuration Activity before executing the steps.Access Configuration Activity: 101245 - Define and Parameterize External TransactionsAssign the subledger and posting key to main/sub transaction Y600/0110 and Y600/0120.Access Configuration Activity: 101248 - Define CO Account Assignment KeysDefine a new CO account assignment key or adjust an existing one to meet your business requirements.Access Configuration Activity: 102876 - Define Sales/Purchase Tax DeterminationDefine tax determination ID for your input taxes.Access Configuration Activity: 101845 - Define Accounts for Sales/Purchase TaxDefine postings for your input taxes.Access Configuration Activity: 102292 - Define Acct Assmt Data Relevant to Main TransactionsAssign relevant GL account for main/sub transaction Y600/0110 and Y600/0120.Access Configuration Activity: 102293 - Define Account Determination Data Relevant to TransactionsDefine account assignment for main/sub transaction Y600/0110 and Y600/0120.Access Configuration Activity: 106985 - Activate Document Transfer to Accounts Payable/Accounts ReceivableActivate tranfer to Accounts Payable for your company code.Access Configuration Activity: 106986 - Account Determination for Revenues in Another SubledgerMaintain the GL account to be posted in Accounts Payable.Prepare master data of business partner and contract account, the business partner must have a supplier role (FLVN00).Assign subledger to contract account master data. |

#### Post Document

In this activity, you can post documents for business partner and newly created contract account.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Accounts Payable and Receivable Accountant (FI-CA). |  |  |
| 2 | Access App | Open Post Document (FPE1). | Post Document: Initial Screen displays. |  |
| 3 | Enter Data | Make the following entries:Document Date: <today’s date>Posting Date: <today’s date>Document Type: YACurrency: AEDReconcil. Key: <reconciliation key generated by system>Clearing Reason: 01 Incoming PaymentBP Item: Y01G/L Item: Y01Calculate Automatically: selected |  |  |
| 4 | Enter BP Item | Choose New BP Itm. | The Checking reconciliation key screen appears.Note If Reconcil. Key has already been created, the Checking reconciliation key screen won’t be displayed. Please go to step 7 directly |  |
| 5 | Create Reconciliation Key | Choose Yes. | A new reconciliation key is created. |  |
| 6 | Continue to Enter BP Item | Choose Continue. | The Post Document: Enter Item screen displays. |  |
| 7 | Enter Item Data | Make the following entries:In the Account Assignment section:Business partn.: <33100023>Contract Acct: <new contract account created in prerequisites step, for example, AE_CA_66 >Note If the document has contract, you also need to fill in Contract Item.Company Code: 3310Transac.: Y600/0020Note Please use Transaction: Y600/0010 to post credit open items.In the Amounts and Due Date section:Net Due Date: <today’s date>Amount: <any amount value>Tax C/R: <tax country>Note The Tax C/R field is only visible when RITA (Registration for Indirect Taxation Abroad) is activated in your system. |  |  |
| 8 | Post Document | Choose Post. | The FI-CA document is posted. |  |

#### Transfer Documents to Accounts Payable/Accounts Receivable

Purpose

With this activity, you can transfer documents to Accounts Payable/Accounts Receivable.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Accounts Payable and Receivable Accountant (FI-CA). |  |  |
| 2 | Access App | Open Transfer Documents to Accounts Receivable/Payable (F8633). | The CADocument-massTransferToSL screen is displayed. |  |
| 3 | Create New Job | Choose Create. | The New Job: FI-CA: Transfer Documents to Accounts Payable/Accounts Receivable view displays. |  |
| 4 | Enter Required Parameters | Make the following entries and choose Step 2:Job Template: FI-CA: Transfer Documents to Accounts Payable/Accounts ReceivableJob Name: FI-CA: Transfer Documents to Accounts Payable/Accounts Receivable |  |  |
| 5 | Enter Posting Parameters | Make the following entry and choose Step 3:Start Immediately: selected |  |  |
| 6 | Enter Posting Parameters | Make the following entries:Run Identification:Prefix of Run ID: for example, ID0Sim: unselectedGeneral Selections:Company Code: 3310Business Partner.: <your business partner ID>Cont.Account: <your contract account ID>Posting Parameters:Posting date: <optional>DT: <YA>Doc, Type: <Data Transfer FI-CA (UF)>Doc, Type: <Data Transfer FI-CA (UF)> |  |  |
| 7 | Check Job | Choose Check. | System message You can go ahead and schedule the job is displayed. |  |
| 8 | Execute Job | Choose Schedule. | The Application Jobs screen displays.One new application job is created with a status. |  |
| 9 | Check Job Status | After the job has been finished, choose the arrow button at the end of the entry to navigate to the job details. | The Job Log screen is displayed. The log should show no errors.The Run Identification should combine Run ID Prefix + dynamic number (xx).The transferred documents with cleared documents and AP/AR accounting documents should be listed in the log. |  |

#### Display Document

Context

In this activity, you display the contract accounting document and switch to subledger document.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Accounts Payable and Receivable Accountant (FI-CA). |  |  |
| 2 | Access App | Open Display Document (FPE3). | The Display Document: Initial Screen displays. |  |
| 3 | Enter Data | Make the following entry:Document Number: <document number posted in the Post Document step> |  |  |
| 4 | Execute | Press Enter. | Details of the document are listed. |  |
| 5 | Switch to subledger doc | Choose Subledger Document. | Details of the subledger document are listed. |  |

#### Reverse Document (Optional)

Context

In this activity, you can reverse a contract accounting document transferred to subledger.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Accounts Payable and Receivable Accountant (FI-CA). | The SAP Fiori launchpad is displayed. |  |
| 2 | Access App | Open Reverse Documents Run (F3546). | The Application Jobs view is displayed. |  |
| 3 | Choose New | In the Application Jobs view, choose New. | The New Job view is displayed. |  |
| 4 | Enter Required Parameters | Make the following entries and choose Step 2:Job Template: FI-CA: Reverse DocumentsJob Name: FI-CA: Reverse Documents |  |  |
| 5 | Enter Posting Parameters | Make the following entry and choose Step 3:Start Immediately: Selected |  |  |
| 6 | Enter Posting Parameters | Make the following entries:Run Identification:Prefix of Run ID: For example, ID0Sim: UnselectedGeneral Selections:Document Number: <Clearing document of your original contract accounting document>Further Settings:Clearing reason: <default>Document Type: <YA> |  |  |
| 7 | Check Job | Choose Check. | System message You can go ahead and schedule the job is displayed. |  |
| 8 | Execute Job | Choose Schedule. | The Application Jobs screen displays.One new application job is created with a status. |  |
| 9 | Check Job Status | After the job has been finished, choose the arrow button at the end of the entry to navigate to the job details. | The Job Log screen is displayed. The log should show no errors.The Run Identification should combine Run ID Prefix + dynamic number (xx).The reversed document should be listed in the log. |  |

## Appendix

### Process Integration

The processes to be tested in this test script are part of a chain of integrated processes.

#### Reset Cleared Items

Context

You can reset the clearing of line items as well as reverse the clearing entry.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1. | Log On | Log on to the SAP Fiori launchpad as an Accounts Payable and Receivable Accountant (FI-CA). |  |  |
| 2. | Access the SAP Fiori App | Open Reset Clearing (FP07). | The Reset Cleared Items screen is displayed. |  |
| 3. | Search Criteria | Make the following entries:Enter Clearing doc.: <Input clearing document>Setting for Scope of Reset: <Whole clearing>Setting for Posing Clearing Amount: <Create a new open item> |  |  |
| 4. | Execute | Choose post. | The reset document is posted. |  |

#### Reverse of Dunning Notice

Purpose

In this process step you reverse the dunning notice.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Administrator - Accounts Payable and Receivable (FI-CA). |  |  |
| 2 | Access App | Open Reverse Dunning Notices Run (F3528). | The Post Document: Initial Screen is displayed. |  |
| 3 | Create | Choose Create. | The New Job screen is displayed. |  |
| 4 | Enter Basic Parameters | Make the following entries and choose Step 2:Job Template: Reverse FI-CA Dunning Notices (In Parallel)Job Name: Reverse FI-CA Dunning Notices (In Parallel) |  |  |
| 5 | Enter Basic Parameters | Make the following entry and choose Step 3:Start Immediately: Selected |  |  |
| 6 | Enter Selection Parameters | Make the following entries:Run ID Prefix: For example, ID0Run Identification: <select Dunning Proposal ID> |  |  |
| 7 | Check Job | Choose Check. | System message You can go ahead and schedule the job is displayed. |  |
| 8 | Execute Job | Choose Schedule. | The Application Jobs screen is displayed.One new application job is created with a status. |  |
| 9 | Check Job Status | After the job has been finished, choose the arrow button at the end of the entry to navigate to the job details. | The Job Log screen is displayed. The log should show no errors.Note The Run Identification should combine Run ID Prefix + dynamic number (xx). |  |

#### Change Creditworthiness

Purpose

In this process step, you can enter manual creditworthiness and creditworthiness factor to change the creditworthiness manually. The manual creditworthiness is added to the value of the creditworthiness that is calculated automatically. The percentage only refers to the creditworthiness portion that is determined automatically. The manual creditworthiness value is not affected.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1. | Log On | Log on to the SAP Fiori launchpad as an Accounts Payable and Receivable Accountant (FI-CA). |  |  |
| 2. | Access App | Open Manage Creditworthiness (F4408). | The screen Manage Creditworthiness is displayed. |  |
| 3. | Change Creditworthiness | Make the following entry:Business Partner: <the required Business Partner> | The selected Business Partner Creditworthiness is displayed, and you can click the arrow button to view details. |  |
| 4. | Enter | Modify some entries by changing:Manual CreditworthinessCreditworthiness Factor |  |  |
| 5. | Save | Choose Save. | The Creditworthiness is displayed |  |

#### Dunning by Collection Strategy

Purpose

In this process step, the Dunning by Collection Strategy feature utilizes collection strategies to prompt payment for customers' overdue receivables. You can choose to group master data by either contract account or contract level during the dunning process. Subsequently, the dunning activity run regards each group as a single entity. This means that the system executes the required dunning actions separately for each master data group.

Prerequisite

To execute the Dunning by Collection Strategy, you need to create the BRF+ application, FKKCM_SIMPLIFIED_BRFPLUS_APPLK, through the application job. You have to then configure the following two configuration activities. Once these configurations are in place, maintain the master data group and collection strategy either on the contract account or at the contract level. After completing these steps, you can proceed to execute the Dunning Proposal Run and Dunning Activity Run.

1. Creating BRFplus application for Collection Strategy

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad with your user credentials as an Administrator - Accounts Payable and Receivable (FI-CA) role assigned. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access APP | Open Create BRFplus Application for Collection Strategy(F5220). | The screen Application Jobs is displayed. |  |
| 3 | Choose Create | On the Application Jobs screen, choose Create. | The screen New Job: Valuate Promise to Pay is displayed. |  |
| 4 | Enter Required Parameters | Make the following entry:Job Template: Create BRFplus Application for Dunning with Collections StrategyJob Name: Create BRFplus Application for Dunning with Collections StrategyStep 2: selectedStart Immediately: selectedStart: <today's date>Step 3: selectedParameter Section:BRF+ Application Name: FKKCM_SIMPLIFIED_BRFPLUS_APPLK |  |  |
| 5 | Check Job | Choose Check. | System message You can go ahead and schedule the job is displayed. |  |
| 6 | Execute Job | Choose Schedule. | The screen Application Jobs is displayed.One new application job is created with a status. |  |
| 7 | Display Job | Navigate to the new application job by choosing the information icon. | The screen Job Log is displayed.Check the log and the message type Success is displayed.Target application FKKCM_SIMPLIFIED_BRFPLUS_APPLK is created and ready for use in dunning according to collection strategy. |  |

1. Define Collection Strategy

Depending on your configuration environment for SAP S/4HANA Cloud Public Edition, choose one of the following options:

Configure Your Solution:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad with your user credentials as Configuration Expert - Business Process Configuration role assigned. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access App Manage Your Solution | Open Manage Your Solution and then choose Configure Your Solution. | The Manage Your Solution screen is displayed. |  |
| 3 | Access Configuration Step Define Collection Strategy | Search with following criteria:Application Area: FinanceSub Application Area: Contract AccountingChoose the group Dunning by Collection StrategyChoose the configuration step Define Collection Strategy. | The Change View "Change View "Maintain Collection Strategy for BRFplus": Details": Overview screen is displayed. |  |
| 4 | Add Entries | Collection Strategy: <give any name>Name: Dunning by collections strategyBRFplus Application: FKKCM_SIMPLIFIED_BRFPLUS_APPLKBRFplus Function: <select Function>Save the entry. | Check the entries by going again into the configuration activity. |  |

SAP Central Business Configuration:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the project experience in SAP Central Business Configuration. |  |  |
| 2 | Open Define Collection Strategy | Go to the Business Processes Configuration app and search for the following activity: Define Collection Strategy.Choose Open Documentation for the found line item to see more details about this configuration activity.Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. | The Change View "Change View "Maintain Collection Strategy for BRFplus": Details": Overview screen is displayed. |  |
| 3 | Input Parameters | Collection Strategy: <give any name>Name: Dunning by collections strategyBRFplus Application: FKKCM_SIMPLIFIED_BRFPLUS_APPLKBRFplus Function: <select Function>Save the entry. | Check the entries by going again into the configuration activity. |  |

1. Set Up Company Codes for Contract Accounts Receivable and Payable

Depending on your configuration environment for SAP S/4HANA Cloud Public Edition, choose one of the following options:

Configure Your Solution:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad with your user credentials as Configuration Expert - Business Process Configuration role assigned. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access App Manage Your Solution | Open Manage Your Solution and then choose Configure Your Solution. | The Manage Your Solution screen is displayed. |  |
| 3 | Access Configuration Step Set Up Company Codes for Contract Accounts Receivable and Payable | Search with following criteria:Application Area: FinanceSub Application Area: Contract AccountingChoose the group OrganizationChoose the configuration step Set Up Company Codes for Contract Accounts Receivable and Payable. | The Change View " Company Codes in Contract Accounts Receivable and Payable": Overview screen is displayed. |  |
| 4 | Select Entries for Company Codes | Select an entry for company code 3310.Collections Management Grouping Level: <Select Group Level>, for example, Contract Account or ContractSave the entry. | Check the entries by going again into the configuration activity. |  |

SAP Central Business Configuration:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the project experience in SAP Central Business Configuration. |  |  |
| 2 | Open Set Up Company Codes for Contract Accounts Receivable and Payable | Go to the Business Processes Configuration app and search for the following activity: Set Up Company Codes for Contract Accounts Receivable and Payable.Choose Open Documentation for the found line item to see more details about this configuration activity.Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. | The Change View " Company Codes in Contract Accounts Receivable and Payable": Overview screen is displayed. |  |
| 3 | Input Parameters | Select an entry for company code 3310Collections Management Grouping Level: <Select Group Level>, for example, Contract Account or ContractSave the entry. | Check the entries by going again into the configuration activity. |  |

4.1 Dunning by Collection strategy at contract accout level

4.1.1 Configuration Activity 101239: Set Up Company Codes for Contract Accounts Receivable and Payable - Collections Management Grouping Level: <Select Contract Account>

4.1.2 Create contract account and maintain master data group and collection strategy.

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad with your user credentials as Accounts Payable and Receivable Accountant (FI-CA) role assigned. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Maintain Contract Account (CAA3).Alternatively, open Manage Contract Accounts (F5474A). | The Contract account Display: Initial Screen displays. |  |
| 3 | Enter Contract Account Number | Choose ChangeMake the following entry and choose Continue:Contract Acct: <contract account number> | The Contract account Display: General Data screen displays. |  |
| 4 | Enter Parameters | Go to the Dunning/Correspondence tab.Make the following entries in dunning control section:Master Data Group: <Choose master data group>Collection Strategy: <Choose collection strategy> |  |  |
| 5 | Save | Choose Save. | The change has been saved. |  |

4.1.3 Post overdue document with business partner/contract account

4.2 Dunning by Collection strategy on provider contract level

4.2.1 Configuration Activity 101239: Set Up Company Codes for Contract Accounts Receivable and Payable - Collections Management Grouping Level: <Select Provider Contract>

4.2.2 Create provider contract and maintain master data group and collection strategy

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad with your user credentials as Accounts Payable and Receivable Accountant (FI-CA) role assigned. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Maintain Provider Contract (FP_VT3). | The Provider contract Display: Initial Screen displays. |  |
| 3 | Enter Contract Account Number | Choose Change.Make the following entry and choose Continue:Provider Contract: <provider contract number> | The Provider contract Display: General Data screen displays. |  |
| 4 | Enter Parameters | Go to tab Items: Dunning.Make the following entries in Dunning by Collection Strategy section:Master Data Group: <Choose master data group>Collection Strategy: <Choose collection strategy> |  |  |
| 5 | Save | Choose Save. | The change has been saved. |  |

4.2.3 Post overdue document with business partner/contract account/provider contract.

##### Execute Dunning Proposal Run

Purpose

In this activity, you execute the dunning proposal. The dunning proposal run groups overdue items into dunning notices. To do so, refer to the test script of the scope item 2UJContract Accounting – Open Item Management, chapter Execute Dunning Proposal Run.

##### Execute Dunning Activity Run

Purpose

In this activity, step you execute the dunning activity run as a second sub process of the dunning runs. To do so, refer to the test script of the scope item 2UJContract Accounting – Open Item Management, chapter Execute Dunning Activity Run.

##### Display Collection History

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result |
| --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Accounts Payable and Receivable Manager (FI-CA). |  |
| 2 | Access App | Open Display Collection History (FPCOLLHIST) | The Display Collection History screen is displayed. |
| 3 | Enter Basic Parameters | Make the following entries:General Selections:Business Partner: <Business Partner>Contract Account:<Contract Account>Subapplication: <No Contract Reference/Primary Contract>Settings:Variant: <Collection History with Focus on Dunning Notices>Simulation: UnselectedChoose Execute. | The collection history report is displayed. |

##### Valuation Collection Success

Purpose

In this process step, you execute Valuation of Collection Success.

If the customers pay for their dunned items which are collected by collection strategy, this has a positive effect on the collection success. Therefore, make sure you post a payment via payment lot on the dunned items after the dunning run. Please refer to the test script of the scope item Contract Accounting – Customer Initiated Payments (2BI).

A payment within 7 days will be treated as 100% successful. Each further day of delay reduces the success percentage rate by 2.5%.

Prerequisite

Before executing Valuation Collection Success, you have to select Perform Success Valuation and give a value of Payment Deadline for relevant collection steps via SSCUI Define Collection Step (103563).

Procedure

Refer to the test script of the scope item Contract Accounting – Open Item Management (2UJ), chapter Valuation Success of Dunning.

##### Determining the Optimum Collection Strategy

Purpose

In this activity, there are some optional steps for you to maintain the master data groups and assign a collection strategy for your business partners and also provide the functionality to allow you to change the current Collection Strategy (Champion Strategy) with an alternative Collection Strategy (Challenger Strategy). If the Challenger Strategy performs better, it can be updated to the new default Collection Strategy for a Contract Account or Master Data Group.

###### Maintain Master Data Groups

Purpose

In this process step, assign collection strategy to business partner.

| Test Step # | Test Step Name | Instruction | Expected Result |
| --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Collections Specialist (FI-CA). |  |
| 2 | Access App | Open Maintain Master Data Groups (FPCG). | The Maintenance of Master Data Groups of Business Partners screen is displayed. |
| 3 | Enter Basic Parameters | Make the following entry:Business Partner: <Business Partner number> |  |
| 4 | Execute | Press Enter. | The attributes of the business partner are shown in the list. |
| 5 | Enter Basic Parameters | Strategy: <Collection Strategy created in Prerequisite>Group: <S1 for example>Choose Save. | The collection strategy and master data groups are saved. |

###### Maintain Test Series for Collection Strategies

Purpose

In this process step, create a test series with champion strategies, challenger strategies and percentage where a master data group is affected by the replacement of a champion collection strategy by a challenger collection strategy. Test series is to determine which collection strategies achieve the highest success rates during dunning.

| Test Step # | Test Step Name | Instruction | Expected Result |
| --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Accounts Payable and Receivable Manager (FI-CA). |  |
| 2 | Access App | Open Maintain Test Series for Collection Strategies (FPCCT) |  |
| 3 | Create Test Series | Make the following entry:Test Series: <Test Series ID>Choose Create. |  |
| 4 | Enter Basic Parameters | Description: <Description of your Test Series>Valid from: <Today’s date>In the Assignments section:Champ.Str: <Collection Strategy you assigned in the master data groups step>Chall .Str: <A different Collection Strategy created in Prerequisite>Percentage: 100Choose Save. |  |

###### Determine Master Data for Collection Test Series

Purpose

In this process step, it can be used to determine the master data groups that should be assigned to a test series for collection strategy replacement.

| Test Step # | Test Step Name | Instruction | Expected Result |
| --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as Accounts Payable and Receivable Manager (FI-CA). |  |
| 2 | Access App | Open Determine Master Data for Collection Test Series (FPCCMD). | The Determination of Master Data Groups for Challenger Strategies screen is displayed. |
| 3 | Enter Basic Parameters | Make the following entries:Business Partner: <Business partner>Test Series for Strategy: <Test Series ID you create in last step>Simulation: <not selected>Display Detail Log: SelectedChoose Execute. | The Test Series: Create/Change screen is displayed. |

###### Update Collection Strategies

Purpose

In this process step, you can replace old collection strategy by new collection strategy.

| Test Step # | Test Step Name | Instruction | Expected Result |
| --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Accounts Payable and Receivable Manager (FI-CA). |  |
| 2 | Access App | Open Update Collection Strategies (FPCCU). | The Update Run for Collection Strategies screen is displayed. |
| 3 | Enter Basic Parameters | Make the following entries:In the Selection of Master Data section:Business Partner: <Business partner>In the Selection of Collection Strategies section:Replacement per Test Series: SelectedTest Series for Strategy: <Select your Test Series ID>Update Run: SelectedDescription of Update Run: <your description of Update run>Choose Execute. | The Log of Champion/Challenger Update - Overview screen is displayed. |

###### Undo Update of Collection Strategies

Purpose

In this process step, you can revert to old collection strategy.

| Test Step # | Test Step Name | Instruction | Expected Result |
| --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Accounts Payable and Receivable Manager (FI-CA). |  |
| 2 | Access App | Open Update Run for Collection Strategy (FPCCUM). | The Process Update Run for Collection Strategies screen is displayed. |
| 3 | Enter Basic Parameters | Make the following entries:In the Selection for Update Run section:Update Run Description: <Select your description of Champion-Challenger Update Run>In the Mode section:Reverse Run: SelectedSimulation: UnselectedChoose Execute. | The Champion-Challenger Update run is reversed. |

#### Mass Close Dispute Cases

In this step, you can close dispute cases in a mass run.

For internal testing purpose, please execute this section in an extensibility testing environment.

Prerequisites

Before executing Close Dispute Cases, you have to complete Cloud BAdI Implementation for event 1265 and make sure your have open dispute cases can meet your conditions you define in your code logic.

| Test Step # | Test Step Name | Instruction | Expect result |
| --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Extensibility Specialist. |  |
| 2 | Access App | Open Custom Logic(F6957). | The Application Jobs screen displays. |
| 3 | Create New Enhancement Implementation | Choose Create. | The New Job screen is displayed. |
| 4 | Enter Parameters | Business Context: Contract Accounting: Dispute CaseChoose Description:FI-CA Dispute: Close Cases from the ExtensionnPoints list.Choose Step 2.Implementation ID: <e.g. YY1_DisputeCloudBAdI1265>Implementation Description: <e.g. Mass close dispute cases>Choose the Review button. |  |
| 5 | Implement Logic | On the new implementation screen, choose Create.Then choose Publish.Once your implementation is published, choose the Open Code Editor button.Choose Edit on the new screen displayed.Enter the logic.For example:CLEAR: cadisputecasestatus-caseisclosed.IF cadisputecaseattributes-caseplannedclosedate <= '20240402'. "#EC CI_MAGICcadisputecasestatus-caseisclosed = abap_true.cadisputecasestatus-casestatus = '30'.ENDIF. |  |
| 6 | Save Draft | Choose Save. | Draft is saved. |
| 7 | Publish the Implementation | Choose Publish. | New implementation is published. |

Procedure

| Test Step # | Test Step Name | Instruction | Expect result |
| --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Accounts Payable and Receivable Accountant (FI-CA). |  |
| 2 | Access App | Open Close Dispute Cases (F8183). | The Close Dispute Cases screen displays. |
| 3 | Create New Job | Choose Create. | The New Job view displays. |
| 4 | Enter Parameters | Make the following entries and choose Step 2:Job Template: Close Dispute CasesJob Name: Close Dispute Cases |  |
| 5 | Enter Parameters | Make the following entry and choose Step 3:Start Immediately: Selected |  |
| 6 | Enter Parameters | Make the following entries:Run ID Prefix: ID0Business Partner: <Business Partner number>Contract Account: <Contract Account number>Company code: <Company code>Simulation run : UnselectedProblem class: Additional Information |  |
| 7 | Check Job | Choose Check. | System message You can go ahead and schedule the job is displayed. |
| 8 | Execute Job | Choose Schedule. | The Application Jobs screen is displayed.One new application job is created with a status. |
| 9 | Check Job Status | After the job has been finished, choose the arrow button at the end of the entry to navigate to the job details. | The Job Log screen is displayed. The log should show no errors.For example:Dispute case XXXXXDispute case was closed (new status 'Closed'). |

### API Services list

#### API Services for Document Change

Context

You can make changes to some fields of business partner item for a Contract Accounting Document in SAP S/4HANA Cloud Public Edition. In this chapter, we introduce an example of changing the Net due date of a bisiness partner item via SAP API.

Prerequisite

Make sure you have set up the communication SAP_COM_0361.( Finance - Contract Accounting Open Item Management Integration) After that, You can change the business partner items of a Contract Accounting document via API by sending an http request. For more information about the Communication Scenario SAP_COM_0361, please refer to Setting Up Contract Accounting - Open Item Management.

Procedure

In this step, you make changes for a business partner item of a Contract Accounting document by invoking the ODATA API.

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Navigate to SAP API HUB | Open web browser and navigate to [https://api.sap.com](https://api.sap.com) | The SAP API hub home page is displayed. |  |
| 2 | Locate SAP S/4HANA Cloud Public Edition API package | Choose SAP S/4HANA Cloud Public Editionas Source to locate the SAP S/4HANA Cloud Public Edition API package. | The SAP S/4HANA Cloud Public Edition API package is located. |  |
| 3 | Search out Contract Accounting: Document ODATA API | Make [Contract Accounting: Document - Manage](https://api.sap.com/) as search key to locate the API packages that are relevant to Contract Accounting: Document - Manage then choose Contract Accounting: Document - Manage.Note:you can follow the detailed instructions and generate your specific Http request for Document management, below is one example HTTP request for the scenario: Document change of a business partner item. You may exchange variables in curly brackets based on your environment. | The Contract Accounting: Document – Manage ODATA API is displayed. |  |

Example Coding: Document change of a business partner item

PATCH https://{{host}}:{{port}}{{serviceURL}}BPItemLogical(CADocumentNumber='{{DocumentNumber}}',CARepetitionItemNumber='000',CABPItemNumber='0001',CASubItemNumber='000')?sap-client={{client}}

{

"CANetDueDate": "2021-04-18"

}

#### API Services for Creditworthiness

Context

Using the Creditworthiness API, external system can query SAP S/4HANA Cloud Public Edition system in order to retrieved Creditworthiness figures by Business Partner.

Prerequisite

Make sure you have set up the communication SAP_COM_0731. After that, You can retrieve the creditworthiness of business partners via API by sending an http request. For more information about the Communication Scenario SAP_COM_0731, please refer to set up guide of 2UJ -Setting Up Contract Accounting – Open Item Management .

Procedure

In this step, you retrieve the creditworthiness of business partners by invoking the ODATA API for provider contract.

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Navigate to SAP API HUB | Open web browser and navigate to [https://api.sap.com](https://api.sap.com) | The SAP API hub home page is displayed. |  |
| 2 | Locate SAP S/4HANA Cloud Public Edition API package | Choose SAP S/4HANA Cloud Public Editionas Source to locate the SAP S/4HANA Cloud Public Edition API package. | The SAP S/4HANA Cloud Public Edition API package is located. |  |
| 3 | Search out Contract Accounting: Creditworthiness ODATA API | Make Worthiness Information as search key to locate the API packages that are relevant to Contract Accounting: Creditworthiness then choose Contract Accounting: Creditworthiness. | The create Contract Accounting: Creditworthiness ODATA API is displayed. |  |

#### API Services for Installment Plan

Context

In Contract Accounting ,Installment plans can also be created and updated for a given business partner and contract account for existing open receivables via API.

For the installment plan create operation, the customer provides, amongst others, a list of the open receivables which are to be converted to an installment plan.

In the update operation, an existing installment plan can be changed, for example, the due dates for individual installments can be modified, although the total amount must remain the same.

In this chapter, we introduce an example of creating an installment plan for an exiting open receivable via SAP API.

Prerequisite

Make sure you have set up the communication SAP_COM_0361. After that, You can create an installment plan for an existing open receivable via API by sending an http request. For more information about the Communication Scenario SAP_COM_0361, please refer to set up guide of 2UJ -Setting Up Contract Accounting – Open Item Management.

Procedure

In this step, you create an installment plan for an existing open receivable by invoking the SOAP API for Installment Plan.

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Navigate to SAP API HUB | Open web browser and navigate to [https://api.sap.com](https://api.sap.com) | The SAP API hub home page is displayed. |  |
| 2 | Locate SAP S/4HANA Cloud Public Edition API package | Choose SAP S/4HANA Cloud Public Editionas Source to locate the SAP S/4HANA Cloud Public Edition API package. | The SAP S/4HANA Cloud Public Edition API package is located. |  |
| 3 | Search out Installment Plan – Create SOAP API | Make Installment Plan as search key to locate the API packages that are relevant to Installment Plan then choose Installment Plan – Create.Note You can follow the detailed instructions and generate your specific Http request for your Installment Plan creation, below is one example HTTP request for the scenario: Create an Installment Plan for an existing open receivable. You may exchange variables in curly brackets based on your environment. | The Installment Plan – Create SOAP API is displayed. |  |

Example Coding: Installment Plan creation for an Contract Accounting Document

|  |
| --- |
| Sample CodeExample Coding: Installment Plan creation for an Contract Accounting Document <soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:glob="http://something.com/somePath"> <soapenv:Header/> <soapenv:Body> <glob:InstallmentPlanCreateRequest_sync> <MessageHeader> <CreationDateTime>2021-03-01T08:55:54Z</CreationDateTime> </MessageHeader> <InstallmentPlan> <SenderTechnicalID>SOME_SENDER</SenderTechnicalID> <InstallmentPlanHeader> <Currency>{{currency}}</Currency> <CAInstallmentPlanCategory>01</CAInstallmentPlanCategory> <!-- <CAInstallmentPlanType>001</CAInstallmentPlanType> --> <CADocumentType>AB</CADocumentType> <CAPostingDate>2021-02-01</CAPostingDate> <DocumentDate>2021-02-01</DocumentDate> <!-- Interval Value: Applies to Interval Type (below) --> <CAInstallmentIntervalValue>1</CAInstallmentIntervalValue> <!-- <CAInstallmentAmountInTransCrcy currencyCode="AED"></CAInstallmentAmountInTransCrcy> --> <CANumberOfInstallments>10</CANumberOfInstallments> <CAInstallmentPlanStartDate>2021-02-01</CAInstallmentPlanStartDate> <!-- Interval Type 1:Days 2:Weeks 3:Months 4:Every 2 Weeks --> <CAInstallmentPlanIntervalType>3</CAInstallmentPlanIntervalType> <CAInstallmentRoundingAmount currencyCode="AED">1</CAInstallmentRoundingAmount> <ContractAccount> <InternalID>CA_1</InternalID> </ContractAccount> <BusinessPartner> <InternalID>BP_1</InternalID> </BusinessPartner> <CAIntrstAndChargesAreDistrd>true</CAIntrstAndChargesAreDistrd> </InstallmentPlanHeader> <CABusinessPartnerDocumentKey> <CADocument>4711</CADocument> <CABPItemNumber>0001</CABPItemNumber> <CASubItemNumber>000</CASubItemNumber> <CAClearingAmountInTransCrcy currencyCode="AED">100</CAClearingAmountInTransCrcy> </CABusinessPartnerDocumentKey> </InstallmentPlan> </glob:InstallmentPlanCreateRequest_sync> </soapenv:Body> </soapenv:Envelope> |

#### API Services for Dispute Cases

Context

In Contract Accounting, API service for Dispute cases enables you to create dispute cases including a dispute case object and notes. You can use this service to create, read and copy dispute cases. You can retrieve notes and attachments for a dispute case.

In this chapter, we introduce an example of creating an Incorrect Invoice dispute case for an exiting open receivable via SAP API.

Prerequisite

Make sure you have set up the communication SAP_COM_0731. After that, you can create a dispute case via API by sending an http request. For more information about the Communication Scenario SAP_COM_0731, please refer to set up guide of 2UJ - Setting Up Contract Accounting – Open Item Management.

Procedure

In this step, you create a Incorrect Invoice dispute case for an existing open receivable by invoking the ODATA API.

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Navigate to SAP API HUB | Open web browser and navigate to [https://api.sap.com](https://api.sap.com) | The SAP API hub home page is displayed. |  |
| 2 | Locate SAP S/4HANA Cloud Public Edition API package | Choose SAP S/4HANA Cloud Public Editionas Source to locate the SAP S/4HANA Cloud Public Edition API package. | The SAP S/4HANA Cloud Public Edition API package is located. |  |
| 3 | Search out Dispute Case ODATA API | Make dispute as search key to locate the API packages that are relevant to Dispute Cases then choose Contract Accounting: Dispute Case.Note You can follow the detailed instructions and generate your specific Http request for your Dispute Cases creation, below is one example HTTP request for the scenario: Create a dispute case. You may exchange variables in curly brackets based on your environment. | The Dispute Case create ODATA API is displayed. |  |

Http request example

|  |
| --- |
| Sample CodePOST ?sap-client={{client}} HTTP/1.1 Host: {{host}}{{serviceURL}} { "DisputeCaseCurrency": "AED", "CADisputeType": "A001", "BusinessPartner": "BP_XX", "ContractAccount": "CA_XX", "CaseReason": "0002", "CaseCategory": "0002", "DisputedAmount": 50, "CADisputeExternalCallerCode": "EXT", "_CACaseObject": [ { "ObjectType": "CA_DOC", "ObjectClassification": "", "ObjectKey": "000100000010" }, { "ObjectType": "CA_DOC", "ObjectClassification": "", "ObjectKey": "000100000011" } ] } |

#### API Services for Security Deposit

Context

SAP provides various APIs to enable customer management for cash security deposit.

Prerequisite

Make sure you have set up the communication SAP_COM_0380. After that, You can use API tools to call APIs to do like Transfer the data of cash security deposits from an external system to SAP S/4HANA Cloud Public Edition. For more information about the Communication Scenario SAP_COM_0380, please refer to set up guide of 2UJ Open Item Management.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Navigate to SAP API HUB | Open web browser and navigate to [https://api.sap.com](https://api.sap.com) | The SAP API hub home page is displayed. |  |
| 2 | Locate SAP S/4HANA Cloud Public Edition API package | Choose SAP S/4HANA Cloud Public Editionas Source to locate the SAP S/4HANA Cloud Public Edition API package. | The SAP S/4HANA Cloud Public Edition API package is located. |  |
| 3 | Search out Cash Security Deposit ODATA API | Make Security deposit as search key to locate the API packages that are relevant to security deposit then choose Cash Security Deposit.Note You can follow the detailed instructions and generate your specific Http request for managing your security deposit , below is one example HTTP request for the scenario: Create Security Deposit. You may exchange variables in curly brackets based on your environment. | The Transfer the data of cash security API is displayed. |  |

Example Coding: Create Security Deposit

| Http Method | Post |
| --- | --- |
| URL | <host>/sap/opu/odata4/sap/api_casecuritydeposit/srvd_a2x/sap/casecuritydeposit/0002/CASecurityDeposit |
| Content-Type of Request Header | application/json |

Request Body

|  |
| --- |
| Sample Code{ "ContractAccount": "PC_ACC1", "TransactionCurrency": "AED", "CASecurityDepositRequestAmount": 10, "CASecurityDepositRequestReason": "Z001", "CASecurityDepositStartDate": "2022-04-13", "CASecurityDepositReturnDate": "2023-04-13" } |

Example Coding: Create Security Deposit Request

| Http Method | Post |
| --- | --- |
| URL | <host>/sap/opu/odata4/sap/api_casecuritydeposit/srvd_a2x/sap/casecuritydeposit/0002/CASecurityDeposit('100000107304')/_CAScrtyDepRequestDetail |
| Content-Type of Request Header | application/json |

Request Body

|  |
| --- |
| Sample Code{ "CASecurityDeposit": "100000107304", "CAAmountInTransactionCurrency": 10, "TransactionCurrency": "AED", "CASecurityDepositRequestReason": "Z001" } |

#### API Services for Customer Payment Portal

Context

SAP provides various APIs to enable customer payments like PSP (Payment Service Provider) or Payment card.

Prerequisite

Make sure you have set up communication SAP_COM_0361. After that, You can use API tools to call APIs to do the invoices or payment. For more information about Communication Scenario SAP_COM_0361, please refer to Set-Up Instruction of Contract Accounting – Open Item Management (2UJ).

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Navigate to SAP API HUB | Open web browser and navigate to [https://api.sap.com](https://api.sap.com) | The SAP API hub home page is displayed. |  |
| 2 | Locate SAP S/4HANA Cloud Public Edition API Package | Choose SAP S/4HANA Cloud Public Editionas source to locate the SAP S/4HANA Cloud Public Edition API package. | The SAP S/4HANA Cloud Public Edition API package is located. |  |
| 3 | Search Out Customer Payment Portal API | Make Payments of Business Partner as search key to locate the API packages Contract Accounting: Payments of Business Partner that are relevant to Customer Payment Portal then choose it.Note You can follow the detailed instructions and generate your specific HTTP request for payment. Here is one example HTTP request for the scenario: Make Payment using PC (Invoice). You may exchange variables in curly brackets based on your environment. | The payment portal is displayed. |  |

|  |
| --- |
| Sample CodeExample Coding: Make Payment using Payment Card POST /SAP__self.PayByPaymentServiceProvider?sap-client={{client}} HTTP/1.1 Host: {{host}}{{serviceURL}} { "PaymentCurrency": "AED", "CAPaymentAmountInPaytCurrency": 1, "PaymentCardType": "DPVI", "PaytCardByDigitalPaymentSrvc": "x2x2x2x2x2x2x2x2", "PaymentCardSequenceNumber": "", "PaymentCardValidityStartDate": "2020-01-01", "PaymentCardValidityEndDate": "2222-01-01", "PaymentCardHolderName": "John Doe", "CAAuthorizationType": "", "CAAltvBPForPayment": "", "CAAuthznByDigitalPaytSrvc": "12345", "CAAuthorizationByAcquirer": "", "AuthorizationTime": "00:00:00", "AuthorizationDate": "2020-01-01", "AuthorizationCurrency": "AED", "AuthorizedAmountInAuthznCrcy": 2, "AuthorizationExpirationDate": "2222-01-01", "AuthorizationExpirationTime": "00:00:00", "CADocumentContainerInvoiceUUID": "506b4bc3-44e0-1eeb-8882-5d0d770e9c3c", "MerchantByClearingHouse": "", "CAPaymentIDAuthznWithBilling": "", "CADocumentNumber": "", "CARepetitionItemNumber": "000", "CABPItemNumber": "0000", "CASubItemNumber": "000" } |

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
> Flagged while digesting this document, not verified: Initiator of Withdrawal code 5 is described as 'We Cancel the Promise' in Replace Promise to Pay but as 'Customer withdraws promise to pay' in Withdraw Promise to Pay; the same code carries two different meanings within this slice.

## Connections
- part-of :: [[_cluster]]
- related-to :: [[09-subscription-billing-and-contract-accounting/test-script-contract-accounting-open-item-management-2uj-ae-872-part-01]]
- related-to :: [[09-subscription-billing-and-contract-accounting/test-script-sap-s-4hana-cloud-public-edition-sap-fiori-analytical-apps]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/2UJ_S4CLD2608_BPD_EN_AE.docx` — lines 3546–5367 of the extracted text · extracted with `mammoth` · 398,263 chars in the whole document
