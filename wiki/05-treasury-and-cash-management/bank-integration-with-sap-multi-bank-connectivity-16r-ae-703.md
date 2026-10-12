---
id: 05-treasury-and-cash-management/bank-integration-with-sap-multi-bank-connectivity-16r-ae-703
title: Bank Integration with SAP Multi-Bank Connectivity (16R_AE) (16R_S4CLD2608_BPD_EN_AE)
description: "S/4HANA Cloud 2608 test script (16R_AE): simulating MBC outgoing payments, CAMT.053/MT940 bank statements, fee files, situations and message monitoring."
cluster: 05-treasury-and-cash-management
tags: [kb/treasury-and-cash-management, topic/bank-integration-mbc-and-file-interface]
aliases: [16R_S4CLD2608_BPD_EN_AE]
keywords: [Bank Integration via Multi-Bank Connectivity and File…, multi-bank connectivity, bank integration, bank statements, camt.053 format, mt940 format, electronic bank statement import, payment instructions, situation handling, mbc message monitor]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/16R_S4CLD2608_BPD_EN_AE.docx]
confidence: high
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-703
topic: 05-treasury-and-cash-management/bank-integration-mbc-and-file-interface
language: EN
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Bank Integration with SAP Multi-Bank Connectivity (16R_AE) (16R_S4CLD2608_BPD_EN_AE)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/16R_S4CLD2608_BPD_EN_AE.docx`, extracted with `mammoth`. Grouped under **Bank Integration via Multi-Bank Connectivity and File Interface** in Treasury and Cash Management. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

|  |  |
| --- | --- |
| Bank Integration with SAP Multi-Bank Connectivity (16R_AE)Purpose PUBLIC 1<!-- image omitted: unnamed --> | Test ScriptSAP S/4HANA Cloud Public Edition - 19-06-26 |
|  | Bank Integration with SAP Multi-Bank Connectivity (16R_AE) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Table of Contents

[1 Purpose 3](#_Toc232865145)

[2 Prerequisites 4](#_Toc232865146)

[2.1 System Access 4](#_Toc232865147)

[2.2 Roles 4](#_Toc232865148)

[2.3 Master Data, Organizational Data, and Other Data 5](#_Toc232865149)

[2.4 Business Conditions 6](#_Toc232865150)

[2.5 Preliminary Steps 7](#_Toc232865151)

[2.5.1 Create pain.002.001.03_I071234_01.xml 7](#_Toc232865152)

[2.5.2 Create camt.053.001.02_I071234_01.xml 8](#_Toc232865153)

[2.5.3 Check Alternative Format Type 11](#_Toc232865154)

[2.5.4 Adapt Payment Medium File Structure for Supplier Financing (Optional) 13](#_Toc232865155)

[2.5.5 Enable Situation Framework 18](#_Toc232865156)

[2.5.5.1 Manage Teams and Responsibilities 18](#_Toc232865157)

[2.5.5.2 Create Situation Type 18](#_Toc232865158)

[3 Overview Table 21](#_Toc232865159)

[4 Test Procedures 23](#_Toc232865160)

[4.1 Outgoing Integration 23](#_Toc232865161)

[4.1.1 Create Payment Medium 23](#_Toc232865162)

[4.1.2 Send Payment Instruction to MBC (Optional) 24](#_Toc232865163)

[4.1.3 Monitor Situations 25](#_Toc232865164)

[4.1.4 Check Notification 26](#_Toc232865165)

[4.2 Incoming Integration 26](#_Toc232865166)

[4.2.1 Pull Bank Statement from MBC 26](#_Toc232865167)

[4.2.1.1 ISO CAMT.053 Format 26](#_Toc232865168)

[4.2.1.2 MT940 Format 31](#_Toc232865169)

[4.2.2 Import Electronic Bank Statement 34](#_Toc232865170)

[4.2.3 Pull Bank Services Billing Files from MBC 36](#_Toc232865171)

[4.2.4 Route Payment Files and Payment Transaction Messages 37](#_Toc232865172)

[4.2.4.1 Route Payment Transaction Messages Initiated by SAP Systems 37](#_Toc232865173)

[4.2.4.2 Route Payment Files Initiated by non-SAP Systems 38](#_Toc232865174)

[4.2.5 Monitor Situations 39](#_Toc232865175)

[4.2.6 Check Notification 39](#_Toc232865176)

[4.3 MBC Message Monitor 40](#_Toc232865177)

[5 Appendix 42](#_Toc232865178)

[5.1 Process Integration 42](#_Toc232865179)

[5.2 Succeeding Processes 42](#_Toc232865180)

## Purpose

Overview

With SAP Multi-Bank Connectivity (MBC), SAP establishes connections with your banks to automatically send payment instructions, receive status notifications, receive bank statements, and receive lockbox messages. Leveraging the monitoring capabilities, you can supervise the status of all payment instructions and see which bank statements are received and which expected bank statements are still missing. The monitoring is only available in combination with Advanced Cash Management (J78).

This test script describes an example of the end-to-end process using manual steps to test the setup without needing to connect to an actual real bank. In an actual productive implementation, this process is fully automated.

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
| Cash Management Specialist | SAP_BR_CASH_SPECIALIST | Cash Management | SAP_BR_CASH_SPECIALIST |  |
| Business Integration Specialist - Bank Integration | SAP_BR_BANK_INT_SPECIALIST | Bank Integration | SAP_BR_BANK_INT_SPECIALIST |  |
| Configuration Expert - Business Process Configuration | SAP_BR_BPC_EXPERT | Business Process Configuration / Business Process Configuration - Finance / Business Process Configuration - Procurement / Manage your Solution / Business Process Configuration - Workflow / Business Configuration - Feature Management / Business Process Configuration - Extensibility Explorer / Business Configuration - Transportation | SAP_BR_BPC_EXPERT / SAP_FIN_SPT_BPC_EXPERT_PC / SAP_MM_SPT_BIZ_PROC_CONFIGN_PC / SAP_CA_SPT_IC_LND_BASE_PC / SAP_CA_SPT_BPC_WORKFLOW_PC / SAP_CA_SPT_BPC_FM_PC / SAP_EI_SPT_BPC_EXT_PC / SAP_TM_SPT_TRANSPCFG_PC |  |
| Administrator | SAP_BR_ADMINISTRATOR | Administration / Administration - Workforce Master Data / Administration - License Compliance / Administration - Data Management / Administration - Output Control | SAP_BR_ADMINISTRATOR / SAP_BUM_SPT_ADMINISTRATION_PC / SAP_EI_SPT_ADM_LC_PC / SAP_CA_SPT_TDR_PC / SAP_OC_SPT_ADMINISTRATION_PC |  |
| Business Process Specialist | SAP_BR_BUSINESS_PROCESS_SPEC | Business Process Management / Business Process Management | SAP_BR_BUSINESS_PROCESS_SPEC / SAP_CA_SPT_BPS_PC |  |

### Master Data, Organizational Data, and Other Data

The organizational structure and master data of your company have been created in your system during activation. The organizational structure reflects the structure of your company. The master data represents materials, customers, and vendors, for example, depending on the operational focus of your company.

|  |
| --- |
| Caution Update Behavior of Predelivered Demo DataIn non-productive environments (such as starter systems, sandbox systems, or partner demo systems), SAP initially deploys demo data for your selected scope. You can use this data to test and evaluate business processes.In a customer system, you can receive new or updated demo data after initial activation with further scope enhancements, provided the existing demo data wasn't changed in an incompatible way. If activation errors occur due to incompatible changes in demo data, you're responsible for resolving them. If you don't resolve the errors within a specific time frame, SAP reserves the right to deactivate demo data in your systems. In this case, you can continue by creating your own demo data. Alternatively, you can request that your systems be reprovisioned if you want to work with predelivered demo data again.In partner systems, you can use the demo data deployed with the initial activation. No additional demo data will be deployed in the system with scope enhancements. You can only create additional demo data manually. |

| Data | Sample Value | Details | Comments |
| --- | --- | --- | --- |
| Bank | 18121976 1812198618121986 |  |  |
| House Bank | AEBK1 AEBK2AEBK2 |  |  |
| House Bank Account ID | AEAC1AEAC2 |  |  |
| Bank Account Number | 000000069312345600000006931234560000000693123456 |  |  |
| Country | AE |  |  |
| Company Code | 3310 |  |  |
| SWIFT/BIC |  |  |  |
| Currency | AED |  |  |

### Business Conditions

Before this scope item can be tested, the following business conditions must be met.

| Scope Item | Business Condition |
| --- | --- |
| J60 - Accounts Payable and/orJ78 - Advanced Cash Operations andBFB - Basic Cash Operations | If the Full (Extended) Cash Management is implemented, before the test step Outgoing Integration ensure that either:The payment run has been executed and the paying house bank uses the payment medium format for MBC connectivity in test script Accounts Payable (J60), and the BCM batch has been approved the step Approval and Bank Integration in the Advanced Cash Operations (J78) test script.A bank transfer is made and the paying house bank uses the payment medium format for MBC connectivity and the BCM batch has been approved in the Advanced Cash Operations (J78) test script. |
| J60 - Accounts Payable and/orBFB - Basic Cash Operations | If the Basic (Core) Cash Management is implemented, before the test step Outgoing Integration ensure that: The payment run has been executed and the paying house bank uses the payment medium format for MBC connectivity in test script Accounts Payable (J60), the process is linked to current test script Bank Integration with SAP Multi-Bank Connectivity (16R) via a process interface mentioned in the Accounts Payable Bank Integration procedure in the Basic Cash Operations (BFB) test script, because no approval is needed (no BCM approval function is provided) when using Basic (Core) Cash Management. |
| BD9 - Sell from Stock (for SAP S/4HANA Enterprise Management or SAP S/4HANA Enterprise Management Cloud) orJ14 - Sales Order Processing – Project-Based Services (for SAP S/4HANA Enterprise Management Cloud or SAP S/4HANA Professional Services Cloud)or any other scope items creating customer invoice | Before the test step Incoming Integration ensure that either:Another tester has created a billing document, and its customer item is open (uncleared). You can find open customer items in the app Manage Customer Line Items; in order to run this app, add accounts receivable related roles to your user, you may find these roles in the Accounts Receivable (J59) test script.If you cannot find an existing open customer item, create a billing document by yourself. You can use test script Sell from Stock (BD9) or Sales Order Processing – Project-Based Services (J14) to create a billing document.Make a note of the amount and reference (XBLNR in the header) of the FI document of billing document. This information is needed to simulate the incoming payment (credit) item in an electronic bank statement. In the bank statement, a credit item can be reconciled with customer invoice. |
| J59 - Accounts Receivable | Before the test step Incoming Integration ensure that either:Another tester has created a customer invoice, and its customer item is open (uncleared). You can find open customer items in the app Manage Customer Line Items; in order to run this app, add accounts receivable related roles to your user, you may find these roles in the Accounts Receivable (J59) test script.If you cannot find an existing open customer item, create a customer invoice document by yourself. You can use test script Accounts Receivable (J59).Make a note of the amount and reference (XBLNR in the header) of the FI document of billing document. This information is needed to simulate the incoming payment (credit) item in an electronic bank statement. In the bank statement, a credit item can be reconciled with customer invoice. |
| 2O0 - Bank Fee Management | Before you execute the Pull Bank Services Billing Files from MBC step, ensure that you:Execute the preliminary steps of the Bank Fee Management (2O0) test script. The Cash Scope of General Setting for Cash Management is set as Full Scope.Create a Camt_086 Bank Fee file for bank account 0000000693123456 and save it locally on your PC. Make sure the file used in MBC has a different name and report ID (for example Camt_086_DE_0000000693123456_00002.xml). The report ID is maintained in the <RptId> tag (for example RPT_20170816_DE_50070010_1010_0002). |
| 2DP - Contract Accounting – Company Initiated Payments | Before the test step Route Payment Transaction Messages Initiated by SAP Systems ensure that you:The payment run is conducted, payment media file is generated.The mandatory manual configuration is conducted to integrate Contract Accounting with Multi-Bank Connectivity. |
| 4MT - Advanced Payment Management | Before the test step Route Payment Files and Payment Transaction Messages ensure that all the preliminary steps of the Advanced Payment Management (4MT) test script are executed. |
| 31N - Situation Handling | You install this scope item for the situation handling steps. |

### Preliminary Steps

#### Create pain.002.001.03_I071234_01.xml

Context

This file is required for a later process step.

The xml file name must contain the string ‘pain.002.001.03’ (for example, pain.002.001.03_I071234_01.xml). Because MBC does not accept files with the same name, and more than one tester is testing this scenario, always use a different file name each time you test this step, and replace I071234 with a different ID you specified.

Procedure

In a text editor, paste the following code:

|  |
| --- |
| Sample Code<?xml version="1.0" encoding="UTF-8"?> <Document xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns="urn:iso:std:iso:20022:tech:xsd:pain.002.001.03"> <CstmrPmtStsRpt> <GrpHdr> <MsgId>BBBB/100928-PSR/00120141222054500</MsgId> <CreDtTm>2014-12-22T05:45:00</CreDtTm> <InitgPty> <Nm>Tools Inc. America</Nm> <PstlAdr> <StrtNm>Times Square</StrtNm> <BldgNb>7</BldgNb> <PstCd>NY 10036</PstCd> <TwnNm>New York</TwnNm> <Ctry>US</Ctry> </PstlAdr> </InitgPty> <DbtrAgt> <FinInstnId> <BIC>BOFAUS3M</BIC> </FinInstnId> </DbtrAgt> </GrpHdr> <OrgnlGrpInfAndSts> <OrgnlMsgId>1000004611</OrgnlMsgId> <OrgnlMsgNmId>pain.001.001.03</OrgnlMsgNmId> <OrgnlCreDtTm>2014-12-21T20:38:42</OrgnlCreDtTm> <OrgnlNbOfTxs>1</OrgnlNbOfTxs> <OrgnlCtrlSum>1191.72</OrgnlCtrlSum> </OrgnlGrpInfAndSts> <OrgnlPmtInfAndSts> <OrgnlPmtInfId>1000004611</OrgnlPmtInfId> <OrgnlNbOfTxs>000000001</OrgnlNbOfTxs> <OrgnlCtrlSum>1191.72</OrgnlCtrlSum> <PmtInfSts>ACSP</PmtInfSts> <TxInfAndSts> <OrgnlEndToEndId>33102000000125</OrgnlEndToEndId> <TxSts>ACSP</TxSts> <OrgnlTxRef> <Amt> <InstdAmt Ccy="AED">1191.72</InstdAmt> </Amt> <ReqdExctnDt>2014-12-23</ReqdExctnDt> <PmtMtd>TRF</PmtMtd> <RmtInf> <Ustrd>PREF:TEST FOR PAIN.002</Ustrd> </RmtInf> <Cdtr> <Nm>TEST SE</Nm> </Cdtr> </OrgnlTxRef> </TxInfAndSts> </OrgnlPmtInfAndSts> </CstmrPmtStsRpt> </Document> |

Save the file to a folder on your PC as pain.002.001.03_I071234_01.xml.

#### Create camt.053.001.02_I071234_01.xml

Context

This file is required for a later process step.

The xml file name must contain the string ‘camt.053.001.02’ (for example, camt.053.001.02_I071234_01.xml). Because MBC does not accept files with the same name, and more than one tester is testing this scenario, always use a different file name each time you test this step, and replace I071234 with a different ID you specified.

Procedure

1. In a text editor, paste the following code:

|  |
| --- |
| Sample Code<?xml version="1.0" encoding="utf-8"?> <Document xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns="urn:iso:std:iso:20022:tech:xsd:camt.053.001.02"> <BkToCstmrStmt> <GrpHdr> <MsgId>20141222102146</MsgId> <CreDtTm>2014-12-22T00:00:00</CreDtTm> <MsgPgntn> <PgNb>00001</PgNb> <LastPgInd>false</LastPgInd> </MsgPgntn> </GrpHdr> <Stmt> <Id>CAMSLINK01000249</Id> <ElctrncSeqNb>00006</ElctrncSeqNb> <CreDtTm>2014-12-22T00:00:00</CreDtTm> <Acct> <Id> <Othr> <Id>0000000693123456</Id> </Othr> </Id> <Svcr> <FinInstnId> <BIC>BOFAUS3M</BIC> </FinInstnId> </Svcr> </Acct> <Bal> <Tp> <CdOrPrtry> <Cd>PRCD</Cd> </CdOrPrtry> </Tp> <Amt Ccy="AED">5002.30</Amt> <CdtDbtInd>CRDT</CdtDbtInd> <Dt> <Dt>2014-12-22</Dt> </Dt> </Bal> <Bal> <Tp> <CdOrPrtry> <Cd>CLBD</Cd> </CdOrPrtry> </Tp> <Amt Ccy="AED">4018.83</Amt> <CdtDbtInd>CRDT</CdtDbtInd> <Dt> <Dt>2014-12-22</Dt> </Dt> </Bal> <Ntry> <Amt Ccy="AED">208.25</Amt> <CdtDbtInd>CRDT</CdtDbtInd> <Sts>BOOK</Sts> <BookgDt> <Dt>2014-12-22</Dt> </BookgDt> <ValDt> <Dt>2014-12-22</Dt> </ValDt> <AcctSvcrRef>MBC TEST AcctSvcrRef Item 1</AcctSvcrRef> <BkTxCd> <Prtry> <Cd>PMNTRCDTDMCT</Cd> </Prtry> </BkTxCd> <NtryDtls> <TxDtls> <Refs> <ChqNb>MMTEST</ChqNb> </Refs> <AddtlTxInf>4711</AddtlTxInf> </TxDtls> </NtryDtls> <AddtlNtryInf>4711</AddtlNtryInf> </Ntry> <Ntry> <Amt Ccy="AED">1191.72</Amt> <CdtDbtInd>DBIT</CdtDbtInd> <Sts>BOOK</Sts> <BookgDt> <Dt>2014-12-22</Dt> </BookgDt> <ValDt> <Dt>2014-12-22</Dt> </ValDt> <AcctSvcrRef>MBC TEST AcctSvcrRef Item 1</AcctSvcrRef> <BkTxCd> <Prtry> <Cd>PMNTICDTDMCT</Cd> </Prtry> </BkTxCd> <NtryDtls> <TxDtls> <Refs> <ChqNb>1000004611</ChqNb> </Refs> <AddtlTxInf>4712</AddtlTxInf> </TxDtls> </NtryDtls> <AddtlNtryInf>4712</AddtlNtryInf> </Ntry> <AddtlStmtInf>MBC Test AddtlSmtInf</AddtlStmtInf> </Stmt> </BkToCstmrStmt> </Document> |

2. Save the file to a folder on your PC as camt.053.001.02_I071234_01.xml.

#### Check Alternative Format Type

Use

In this activity, you check the alternative format type. Alternative format type determines how the payment medium file is transmitted to banks or a payment service provider.

Procedure

Depending on your configuration environment for SAP S/4HANA Cloud Public Edition, choose one of the following options:

Configure Your Solution:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. |  |  |
| 2 | Access App | Open Manage Your Solution (F1241). |  |  |
| 3 | Configure | Choose Configure Your Solution. | The Configure Your Solution: Realize Phase view is displayed. |  |
| 4 | Select Filter Criteria | In the filters area, make the following selections:Application Area: FinanceSub Application Area: Account Payable | A filtered list of Configuration Items is displayed. |  |
| 5 | Select Item | At the right side of the Automatic Payments row, choose the arrow button. | The Configure Your Solution - Automatic Payments view is displayed. |  |
| 6 | Choose Configuration Step | For the Set Up Payment Methods for Each Country/Region for Payment Transactions step, choose Configure. | The "Set Up Payment Methods for Each Country/Reg..": Change view is displayed. |  |
| 7 | Select Payment Method | Double click the payment method (for example, Country AE + Pmt MethodT). | The Change View "Set Up Payment Methods for Each Country/Reg..": Details view is displayed. |  |
| 8 | Check Alternative Format | Choose Format in Company Code. | The Change View “PMW Format”: Overview view is displayed.The alternative format type determines in which way the payment medium file is transmitted to banks or payment service provider. Ensure that the alternative format type is set SAP Multi-Bank Connectivity.The other integration option is blank value. Refer to the test procedure in Bank Integration with File Interface(1EG). |  |

SAP Central Business Configuration:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the project experience in SAP Central Business Configuration. |  |  |
| 2 | Open Set Up Payment Methods per Country for Payment Transactions | Go to the Business Processes Configuration app. To locate the activity in the tree view, search for the following activity: Set Up Payment Methods for Each Country/Region for Payment Transactions.Choose Open Documentation for the found line item to see more details about this configuration activity.Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. | The Change View “Payment Method/Country”: Overview screen displays. |  |
| 3 | Select Payment Method | Double click the payment method (for example, Country AE + Pmt MethodT). | The Change View “Payment Method/Country”: Details view is displayed. |  |
| 4 | Check Alternative Format | Choose Format in Company Code. | The Change View “PMW Format”: Overview view is displayed.The alternative format type determines in which way the payment medium file is transmitted to banks or payment service provider. Ensure that the alternative format type is set SAP Multi-Bank Connectivity.The other integration option is blank value. Refer to the test procedure in Bank Integration with File Interface(1EG). |  |

#### Adapt Payment Medium File Structure for Supplier Financing (Optional)

Use

In this activity, you adapt the payment medium file structure to match bank’s standard. The payment medium file used for supplier financing is based on PAIN.001.001.03 format.

Procedure

Depending on your configuration environment for SAP S/4HANA Cloud Public Edition, choose one of the following options:

Configure Your Solution:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. |  |  |
| 2 | Access App | Open Manage Your Solution (F1241). |  |  |
| 3 | Configure | Choose Configure Your Solution. | The Configure Your Solution: Realize Phase view is displayed. |  |
| 4 | Select Filter Criteria | In the filters area, make the following selections:Application Area: FinanceSub Application Area: Account Payable | A filtered list of Configuration Items is displayed. |  |
| 5 | Select Item | At the right side of the Payment Medium Formats row, choose the arrow button. | The Configure Your Solution - Payment Medium Formats view is displayed. |  |
| 6 | Choose Configuration Step | For the Map Payment Format Data step, choose Configure. | The Map Payment Format Data view is displayed. |  |
| 7 | Copy Format Mapping | Choose > Expand Node of Format Mapping CGI_CT, select a PAIN.001.001.03 Format Mapping, for example, AE_CGI_XML_CT | The Copy Format MappingAE_CGI_XML_CT pop-up window is displayed. |  |
| 8 | Confirm New Format Mapping | In the pop-up window, make the following selections:New Format Mapping Name: AE_CGI_XML_CT, choose OK. | A new Format Mapping is created. |  |
| 9 | Edit Format Mapping | Select the new Format Mapping AE_CGI_XML_CT, choose > Displays the format mapping. | The maintenance view of Map Payment Format Data view is displayed. |  |
| 10 | Adapt Format Structure | Expand the structure tree in the Format Mapping Properties subscreen, choose Edit and select node Nm under PmtInf->CdtTrfTxInf->Cdtr. Choose + Create Note from the toolbar on the top left-hand.Name the new node as Id. Make the following entries and press Enter:Name: IdShort Description: Internal Supplier IdStatus: StandardLevel: 3Length: 0Type: CharacterConversion Function: Character string: left-justified, replace leading 0 (CL R0)Mapping Procedure: Structure FieldStructure Field: FPAYH-GPA1RAdapt the change for other node as below:Remove the conditions of node PmtTplnf under PmtInf.Select the node RltdDt under RmtInf->Strd->RfrdDocInf->RltdDt, choose + Create Note from the toolbar on the top left-hand side, choose Create Atom > As Subnode to create following elements on at the lower level.Node YYYY:Name: YYYYStatus: StandardLength: 4Target Offset: 0Type: CharacterConversion Function: Character string: left-justified (CL)Mapping Procedure: Structure FieldStructure Field: FPAYP-BLDATNode MM:Name: MMStatus: StandardLength: 2Target Offset: 5Type: CharacterConversion Function: Character string: left-justified (CL)Mapping Procedure: Structure FieldStructure Field: FPAYP-BLDAT+004Node DD:Name: DDStatus: StandardLength: 2Target Offset: 8Type: CharacterConversion Function: Character string: left-justified (CL)Mapping Procedure: Structure FieldStructure Field: FPAYP-BLDAT+006Node -:Name: -Status: StandardLength: 1Type: CharacterConversion Function: Character string: left-justified (CL)Mapping Procedure: ConstantConstant: - | The format mapping is successfully adapted. |  |
| 11 | Release Format Mapping | Choose Release to activate the format mapping. | The format mapping is successfully released. |  |

SAP Central Business Configuration:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the project experience in SAP Central Business Configuration. |  |  |
| 2 | Open Map Payment Format Data | Go to the Business Processes Configuration app. To locate the activity in the tree view, search for the following activity: Map Payment Format Data.Choose Open Documentation for the found line item to see more details about this configuration activity.Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. | The Map Payment Format Data screen displays. |  |
| 3 | Copy Format Mapping | The Copy Format MappingAE_CGI_XML_CT pop-up window is displayed. | The Copy Format MappingAE_CGI_XML_CT pop-up window is displayed. |  |
| 4 | Confirm New Format Mapping | The Copy Format MappingAE_CGI_XML_CT pop-up window is displayed. | A new Format Mapping is created. |  |
| 5 | Edit Format Mapping | The Copy Format MappingAE_CGI_XML_CT pop-up window is displayed. | The maintenance view of Map Payment Format Data view is displayed. |  |
| 6 | Adapt Format Structure | Expand the structure tree in the Format Mapping Properties subscreen, choose Edit and select node Nm under PmtInf->CdtTrfTxInf->Cdtr. Choose + Create Note from the toolbar on the top left-hand.Name the new node as Id. Make the following entries and press Enter:Name: IdShort Description: Internal Supplier IdStatus: StandardLevel : 3Length: 0Type: CharacterConversion Function: Character string: left-justified, replace leading 0 (CL R0)Mapping Procedure: Structure FieldStructure Field: FPAYH-GPA1RAdapt the change for other node as below:Remove the conditions of node PmtTplnf under PmtInf.Modify the node Cd under PmtInf->PmtTpInf->CtgyPurpMapping Procedure: ConstantConstant: TRADSelect the node RltdDt under RmtInf->Strd->RfrdDocInf->RltdDt, choose + Create Note from the toolbar on the top left-hand side, choose Create Atom > As Subnode to create following elements on at the lower level.Node YYYY:Name: YYYYStatus: StandardLength: 4Target Offset: 0Type: CharacterConversion Function: Character string: left-justified (CL)Mapping Procedure: Structure FieldStructure Field: FPAYP-BLDATNode MM:Name: MMStatus: StandardLength: 2Target Offset: 5Type: CharacterConversion Function: Character string: left-justified (CL)Mapping Procedure: Structure FieldStructure Field: FPAYP-BLDAT+004Node DD:Name: DDStatus: StandardLength: 2Target Offset: 8Type: CharacterConversion Function: Character string: left-justified (CL)Mapping Procedure: Structure FieldStructure Field: FPAYP-BLDAT+006Node -:Name: -Status: StandardLength: 1Type: CharacterConversion Function: Character string: left-justified (CL)Mapping Procedure: ConstantConstant: - | The format mapping is successfully adapted. |  |
| 7 | Release Format Mapping | Choose Release to activate the format mapping. | The format mapping is successfully released. |  |

#### Enable Situation Framework

##### Manage Teams and Responsibilities

Use

In this activity, you create a team to specify responsibilities for MBC messages.

Procedure

Execute the Manage Teams and Responsibilities steps in the Responsibility Management (1NJ) test script with the following information:

Name: MBC Monitor Team

Global ID: TeamMBC01

Type: SMBC

Status: Enabled

ReceiverId: for example, <blank>

SenderId: for example, <blank>

|  |
| --- |
| Note If the last two fields are left blank, the team is responsible for all MBC messages. |

Team Owners tab:

Business Partner: <user ID>, for example, Business Process Specialist

Team Members tab:

Business Partner: <user ID>, for example, Bank Integration Specialist

Functions: S_MBCMON_F

|  |
| --- |
| Note To display the connection between the business partner, cash manager, and user ID, see the search help. Generic users are described in the Last Name field. |

##### Create Situation Type

Use

In this activity, you create situation types for Multi-Bank Connectivity Situation Handling.

There are situation templates available for Multi-Bank Connectivity:

- Bank Message still in status Created: This situation is triggered when an outgoing message is still in status Create after a few minutes.
- Bank Message entering Error status: This situation is triggered when an incoming message goes into Error status.
- Bank Message requires manual processing: This situation is triggered when an incoming message goes into Error status.
- No MBC status received for Bank Message: This situation is triggered when for an outgoing message no MBC Status has been received.
- Bank Message still in status received: This situation is triggered when an incoming message remains in status received for some time.

You can use the above described situations as templates.

|  |
| --- |
| Note Please make sure 31N is activated if you want to execute this step. |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Business Process Specialist. |  |  |
| 2 | Access App | Open Manage Situation Types (F2947). |  |  |
| 3 | Select Filter Criteria | In the filters area, make the following selections:ID: for example, FIN_MBC_BANK_MESSAGE_ERROR | A situation template is displayed. |  |
| 4 | Copy Situation Type | Choose the situation template item and choose Copy. | A new situation type is to be created in the Situation Type view. |  |
| 5 | Create a Situation Type | In the Situation Type view, make the following entries and choose Create.ID: for example, ZFIN_MBC_MESSAGE_ERRORName: for example, keep default name Bank Message Entering Error StatusIn the Situation Monitoring area, Monitor Instances: <Selected> |  |  |
| 6 | Add Team Category | In the Recipients area, choose Add Team Category.In the dialog box, select Multi-Bank Connectivity Connector and choose Select. |  |  |
| 7 | Confirm Creation | Choose Create.Choose Yes to confirm the message Enable Situation Type. | A new situation type is created and enabled. |  |
| 8 | Create Situation Types | Repeat step 3 -7 to create situation types based on following situation templates:FIN_MBC_BANK_MESSAGE_CREATEDFIN_MBC_BANK_MESSAGE_MANPROCFIN_MBC_BANK_MESSAGE_NO_MBCSTATFIN_MBC_BANK_MESSAGE_RECEIVED | Situation types ZFIN_MBC_MESSAGE_CREATED , ZFIN_MBC_MESSAGE_MANPROC, ZFIN_MBC_MESSAGE_NO_MBCSTAT , ZFIN_MBC_MESSAGE_RECEIVERED are created. |  |

## Overview Table

This scope item consists of several process steps provided in the table below.

|  |
| --- |
| Note If your system administrator has enabled spaces and pages on the SAP Fiori launchpad, the homepage will only contain the essential apps for performing the typical tasks of a business role.You can find all other (searchable) apps not included on the homepage using the search bar ([2434549](https://me.sap.com/notes/2434549)).If you want to personalize the homepage and include the hidden apps, navigate to your user profile and choose App Finder. |

| Process Step, Report or Item | Business Role | Transaction/App | Expected Results |
| --- | --- | --- | --- |
| Outgoing Integration |  |  |  |
| [Create Payment Medium](#unique_14) [page ] 23 | Cash Management Specialist |  | The procedure is completed automatically. |
| [Send Payment Instruction to MBC (Optional)](#unique_15) [page ] 24 | Cash Management Specialist |  | The payment medium file is automatically sent to Multi-Bank Connectivity (MBC) and you verify that the file displays in the correct folder of the SFTP server. |
| [Monitor Situations](#unique_16) [page ] 25 | Business Process Specialist | Monitor Situations (F3264) | Situations can be monitored and instance details can be checked. |
| [Check Notification](#unique_17) [page ] 26 | Recipient (for example, Business Integration Specialist - Bank Integration) |  | The notification is checked by the recipient. |
| Incoming Integration |  |  |  |
| [Pull Bank Statement from MBC](#unique_18) [page ] 26 | Cash Management Specialist | Manage Bank Statements (F1564) | MBC maps the local bank statement format to correct format and SAP S/4HANA pulls that bank statement from MBC. |
| [ISO CAMT.053 Format](#unique_19) [page ] 26 | Cash Management Specialist | Manage Bank Statements (F1564) | An ISO CAMT.053 bank statement is simulated. |
| [MT940 Format](#unique_20) [page ] 31 | Cash Management Specialist | Manage Bank Statements (F1564) | An MT940 bank statement is simulated. |
| [Import Electronic Bank Statement](#unique_21) [page ] 34 | Cash Management Specialist | Manage Bank Statements (F1564)Check Cash Flow Items (F0735) | After the CAMT.053 bank statement is pulled from MBC, the electronic bank statement is imported automatically and the postings in bank accounting and subledger accounting are then carried out. |
| [Pull Bank Services Billing Files from MBC](#unique_22) [page ] 36 | Cash Management Specialist |  | The file is placed in the SFTP folder. |
| [Route Payment Transaction Messages Initiated by SAP Systems](#unique_23) [page ] 37 |  |  |  |
| [Route Payment Transaction Messages Initiated by SAP Systems](#unique_23) [page ] 37 |  |  | You simulate a FICA ISO PAIN.001 credit transfer payment message import from MBC. |
| [Route Payment Files Initiated by non-SAP Systems](#unique_24) [page ] 38 |  |  | A CSV payment file which imported from MBC is simulated. |
| [Monitor Situations](#unique_25) [page ] 39 | Business Process Specialist | Monitor Situations (F3264) | You monitor situations and check instance details. |
| [Check Notification](#unique_26) [page ] 39 | Business Integration Specialist - Bank Integration |  | The notification is checked by the recipient. |
| [MBC Message Monitor](#unique_27) [page ] 40 | Business Integration Specialist - Bank Integration | Manage Bank Messages (F4385) | The message content is displayed. |

## Test Procedures

This section describes test procedures for each process step that belongs to this scope item.

### Outgoing Integration

#### Create Payment Medium

Context

In this process step, the payment medium file (DME file) for the payment medium format of Multi-Bank Connectivity (MBC) is created automatically.

Prerequisite

If the Full (Extended) Cash Management is implemented with BCM (Bank Communication Management), after the outgoing payment is executed (whether through the payment run for vendor in Accounts Payable([J60](https://me.sap.com/processnavigator/SolS/SolS-013/2608/SolP/J60)) test script, or making bank transfer in Advanced Cash Operations (([J78](https://me.sap.com/processnavigator/SolS/SolS-013/2608/SolP/J78))) test script), and the BCM batch of this outgoing payment is approved (described in step Approval and Bank Integration in Advanced Cash Operations (J78) test script), the payment medium file is created automatically.

If the Basic (Core) Cash Management is implemented, after the payment run is executed (described in Accounts Payable (J60) test script, the payment medium file is created automatically if the payment method is using the payment medium workbench (PMW) format.

|  |
| --- |
| Note Because Basic and Full Cash Management cannot be tested in the same client at the same time, contact your test organizer to ensure the version of Cash Management to be tested in the current testing client.Test scripts relevant to Basic Cash Operations are:Basic Cash Operations [BFB](https://me.sap.com/processnavigator/SolS/SolS-013/2608/SolP/BFB))Test scripts relevant to Full Cash Operations are:Advanced Cash Operations (J78) |

If in customizing, the PMW medium format for MBC connectivity is assigned to the payment method as the default format. The payment medium file is sent to MBC automatically when SAP S/4HANA is connected to MBC, which will be described in next procedure.

Procedure

This step is done automatically.

#### Send Payment Instruction to MBC (Optional)

Context

If SAP S/4HANA is integrated with Multi-Bank Connectivity (MBC), and a payment medium workbench (PMW) format for MBC connectivity is created, the payment medium file is sent to MBC automatically via the MBC connector. This payment medium file displays in the Secure File Transfer Protocol (SFTP) folder if it has no error.

In this activity, you verify if the payment medium file reaches the SFTP server successfully. The following internal optional test step is the simulation of communication between S/4HANA and SFTP server. You can skip the step if the connection is not running Instead, check whether the outgoing message is displayed in the MBC Connector Monitor step.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Access the SFTP Folder | Access the SFTP folder.For example: /home/S4HTESTHCI/simbank/inbox/s4hana/v0115/BankConnectivity/Bank_ModelS/QE4212/PAIN.001.001.03/BOFAUS3MNote The path of the SFTP server folder depends on testing system, tenant, payment medium format, SWIFT/BIC of house bank.The path provided in this test script is only an example. To get the specific path in the SFTP folder for your specific testing system and client and to get the information about how to access the SFTP folder, contact your test organizer.In the example, this path stores the payment files with format ISO PAIN001 Credit Transfer (format depends which payment method and paying house bank you used), which are sent out from system QE4 client 212 to MBC tenant v0115, and the paying house bank’s SWIFT/BIC is BOFAUS3M (the SWIFT/BIC of house bank AEBK1). |  |  |
| 2 | Verify File | Verify that the payment medium file appears in the SFTP server folder. A new file, for example, DTA150925051453_0279.xml displays in the folder. |  |  |
| 3 | Review File | Open and review the XML file to determine if the information (such as amount or bank information) is consistent with the outgoing payment from a house bank account you approved. |  |  |
| 4 | Note Message Number | Make a note of the values of the following fields in the XML file:<MsgId>Message ID</MsgId>. For example, 1000004611<PmtInfId>Payment Information ID</PmtInfId> for example, 1000004611<CtrlSum>Amount</CtrlSum> for example, 1191.72<EndToEndId>Payment Document Number</EndToEndId> for example: 33102000000125For example:Message ID: 1000004611Payment information ID: 1000004611Amount: 1191.72Payment document number: 33102000000125Note An XML file may contain several payment documents. In this example, there is only one payment document in the XML file.Caution For the non-pain.001 payment medium formats (formats other than CGI credit transfer or SEPA credit transfer), you may not find the information listed previously. For these payment media, skip the current test step and proceed to the Pull Bank Statement from MBC procedure.Use payment method with name such as ISO PAIN.001 Credit Transfer or SEPA CT Credit Transfer for simplicity. The setting is country specific and you can check the payment media format assigned via SSCUI 101972 Set Up Payment Methods per Country for Payment Transactions. |  |  |

#### Monitor Situations

Purpose

In this activity, you monitor situations and check instance details.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Business Process Specialist. |  |  |
| 2 | Access App | Open Monitor Situations (F3264). |  |  |
| 3 | Enter Selection Criteria | In the upper area, make the following entries and press Enter:Situation Type ID: ZFIN_MBC_MESSAGE_CREATEDZFIN_MBC_MESSAGE_NO_MBCSTATYear: for example, <current year> | A chart and a list with instances that are displayed for outgoing payment situations:ZFIN_MBC_MESSAGE_CREATED: Shows all outgoing messages still in status Message Created after a few minutesZFIN_MBC_MESSAGE_NO_MBCSTAT: Shows all outgoing messages with no MBC status received |  |
| 4 | Check Instance | Expand the hierarchy by respective situation ID, you can check the instance triggered by each message. In this case, the Anchor Object Key is the MBC message ID.Note If you can not find the Anchor Object Key, you can choose Settings and select the columns to be visible in the list. | The MBC message ID which triggered the situation is displayed. You can check more details in the App Manage Bank Messages (F4385). For more details, you can refer to test step MBC Message Monitor. |  |

#### Check Notification

Purpose

In this activity, the notification is checked by the recipient who is assigned to team members in preliminary step.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a recipient (for example, Bank Integration Specialist). |  |  |
| 2 | Check Notification | On the home page, choose Notifications in the upper right corner.Choose By Type, under type Bank Message Still in Created Status or No MBC Status Received for Bank Message has been identified, choose Expand Group. |  |  |

### Incoming Integration

#### Pull Bank Statement from MBC

Purpose

For banks with a Multi-Bank Connectivity (MBC) connection, for example, AEBK1, bank statements are handled by MBC. You can check whether MBC is enabled for a specific combination of company code, payment method house bank and payment media format in the preliminary step Check Alternative Format Type. SAP S/4HANA pulls the supported bank statement messages from MBC and then imports it automatically.

A transaction type must be maintained in the field transaction type on the tab of Bank Relationship. You can refer to test script BFA or J77 change bank account section.

You can also define new transaction types in configuration activity 101024 Manage Global Settings for Electronic Bank Statement.

##### ISO CAMT.053 Format

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

In the Preliminary Steps of the Prerequisites section, you created an xml file and saved it to a folder of your PC.

The XML file name must contain the string camt.053.001.02, for example, camt.053.001.02_AB12345_01.xml. Because MBC does not accept files with the same name, and more than one tester is testing this scenario, use a different file name every time when you test this step, and replace AB12345 by a different ID you specified.camt.053.001.02_AB12345_01.xml is for integration with other business process for simplicity.

Access that XML file and using a text editor, edit the file. Because MBC does not accept files with the same name, name each file if more than one tester uses the same XML values.

| XML Text | Example | Comment |
| --- | --- | --- |
| <MsgId>Message ID</MsgId> | <MsgId>20141222102146</MsgId> | 20141222102146 is the real system data and time YYYYMMDDHHMMSS |
| <ElctrncSeqNb>Bank Statement Number</ElctrncSeqNb> | <ElctrncSeqNb>00006</ElctrncSeqNb> | The next bank statement number |
| <Id>Account Number</Id> in <Othr></Othr> | <Id>0000000693123456</Id> | The account number of house bank/account ID AEBK1/AEAC1 |
| find a customer invoice<BIC>BIC</BIC> | <BIC>BOFAUS3M</BIC> |  |
| <Amt Ccy="AED">Opening Balance</Amt> in the first <Bal></Bal> | <Amt Ccy="AED">5002.30</Amt> | Opening balance = closing balance of latest imported bank statement |
| <Dt>Opening Balance Date</Dt> in the first <Bal></Bal> | <Dt>2014-12-22</Dt> |  |
| <Amt Ccy="AED">Closing Balance</Amt> in the second <Bal></Bal> | <Amt Ccy="AED">4018.83</Amt> | Closing balance = opening balance - debit amount + credit amount; For example, 4018.83=5002.30+208.25-1191.72 |
| <Dt>Closing Balance Date</Dt> in the second <Bal></Bal> | <Dt>2014-12-22</Dt> |  |
| <Amt Ccy="AED">Item Amount</Amt> in the first <Ntry></ Ntry> | <Amt Ccy="AED">208.25</Amt> | Customer invoice amount |
| <BookgDt><Dt>Booking Date</Dt></BookgDt> in the first <Ntry></ Ntry> | <BookgDt><Dt>2014-12-22</Dt></BookgDt> |  |
| <ValDt><Dt>Value date</Dt></ValDt> in the first <Ntry></ Ntry> | <ValDt><Dt>2014-12-22</Dt></ValDt> |  |
| <ChqNb>Reference</ChqNb> in the first <Ntry></ Ntry>. | <ChqNb>MMTEST</ChqNb> which is the reference of customer invoice. | Customer invoice reference |
| <Amt Ccy="AED">Item Amount</Amt> in the second <Ntry></ Ntry> | <Amt Ccy="AED">1191.72</Amt> | The payment amount in the [Send Payment Instruction to MBC (Optional)](#unique_15) [page ] 24 step |
| <BookgDt><Dt>Booking Date</Dt></BookgDt> in the second <Ntry></ Ntry> | <BookgDt><Dt>2014-12-22</Dt></BookgDt> |  |
| <ValDt><Dt>Value date</Dt></ValDt> in the second <Ntry> | <ValDt><Dt>2014-12-22</Dt></ValDt></ Ntry> |  |
| <ChqNb>Reference</ChqNb> in the second <Ntry></ Ntry> | <ChqNb>1000004611</ChqNb> | The payment information ID in the [Send Payment Instruction to MBC (Optional)](#unique_15) [page ] 24 step |

| XML Text | Example | Comment |
| --- | --- | --- |
| <MsgId>Message ID</MsgId> | <MsgId>20190726074500</MsgId> | 201907260745 is the real system data and time YYYYMMDDHHMM |
| <ElctrncSeqNb>Bank Statement Number</ElctrncSeqNb> | <ElctrncSeqNb>138</ElctrncSeqNb> | The next bank statement number |
| <Id>Account Number</Id> in <Othr></Othr> | <Id>33333</Id> | The account number of house bank/account ID USBK1/USAC1 |
| find a customer invoice<BIC>BIC</BIC> | <BIC>BOFAUS3M</BIC> | You can find the BIC of house bank USBK1 using the Manage Banks (F6437) SAP Fiori app. |
| <Amt Ccy="USD">Opening Balance</Amt> in the first <Bal></Bal> | <Amt Ccy="USD">1000.00</Amt> | Opening balance = closing balance of latest imported bank statement |
| <Dt>Opening Balance Date</Dt> in the first <Bal></Bal> | <Dt>2019-07-26</Dt> |  |
| <Amt Ccy="USD">Closing Balance</Amt> in the second <Bal></Bal> | <Amt Ccy="USD">400.00</Amt> | Closing balance = opening balance - debit amount + credit amount; For example, 400.00=1000.00-600.00 |
| <Dt>Closing Balance Date</Dt> in the second <Bal></Bal> | <Dt>2019-07-26</Dt> |  |
| <Amt Ccy="USD">Item Amount</Amt> in the first <Ntry></ Ntry> | <Amt Ccy="USD">600.00</Amt> | Total amount of Bank to Customer Debit Notification. The amount should be the same as the total amount maintained in last step. |
| <BookgDt><Dt>Booking Date</Dt></BookgDt> in the first <Ntry></ Ntry> | <BookgDt><Dt>2019-07-26</Dt></BookgDt> |  |
| <ValDt><Dt>Value date</Dt></ValDt> in the first <Ntry></ Ntry> | <ValDt><Dt>2019-07-26</Dt></ValDt> |  |
| <Cd>Code</Cd> in <Ntry><BkTxCd><Prtry></Prtry></BkTxCd></ Ntry> | <Cd>ZSF053</Cd> | The transaction code is always ZSF053 in the Supplier Financing scenario. |

Prerequisite

Per the Business Conditions section in this document, you must execute the Enter Invoice without Sales Order procedure in Accounts Receivable(J59), Sell from Stock (BD9), or Sales Order Processing – Project-Based Services (J14) to create a customer invoice. Make a note of the amount and reference (XBLNR in the header) of the customer invoice document. You use this information when simulating an electronic bank statement.

Procedure

Perform the following steps to simulate an ISO CAMT.053 bank statement for house bank/account ID AEBK1 /AEAC1 directly. MBC gets it from the SFTP server and the SAP S/4HANA system pulls the ISO CAMT.053 bank statements from MBC.

|  |
| --- |
| Note Provided that it is for testing purpose, for simplicity, before you maintain the transaction type, you can change the Bank Account Control Mode to simplify the bank account change process.Go to configuration activity 101025 Define Basic Settings as a Configuration Expert - Business Process Configuration, note down value of field Bank Account Control Mode, change it to 01 Direct Change. As mentioned in Pull Bank Statement from MBC, maintain the Payment Transaction Type Group of corresponding bank account with value CAMT053, and change the Bank Account Control Mode to the original value. |

|  |
| --- |
| Note In this example, the simulated bank statement contains two line items:First item: a credit item which should be reconciled with an existing customer invoice (created as per Prerequisites above).Second item: a debit item that should be reconciled with the payment document created in the [Send Payment Instruction to MBC (Optional)](#unique_15) [page ] 24 step. |

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log onto the SAP Fiori launchpad as a Cash Management Specialist. |  |  |
| 2 | Access the SAP Fiori App | Open Manage Bank Statements (F1564). |  |  |
| 3 | Enter Criteria | To get the latest imported bank statement number, make the following entries and choose Go:Company Code: 3310House Bank: AEBK1House Bank Account: AEAC1Latest Statement: Latest only | The latest bank statement number of the specified bank account displays on the Manage Bank Statements (F1564) view.The next bank statement number is one greater than the latest bank statement number. For example, if the latest bank statement number is 00005, the next number is 00006. If no latest bank statement was found, the next number should be 00001. |  |
| 4 | Closing Balance of Latest Bank Statement | Make a note of the closing balance of the specified bank account. It can be found on the Manage Bank Statements (F1564) view. | The closing balance of the latest bank statement should be the opening balance of the next bank statement.If no latest bank statement was found, the opening balance of the next bank statement should be zero. |  |
| 5 | Access the XML File | Open the camt.053 xml file with a text editor, for example, camt.053.001.02_AB12345_01.xml. Because MBC does not accept files with the same name, and if more than one tester is testing this scenario, use a different file name every time when you test this step, and replace AB12345 by a different ID you specified. |  |  |
| 6 | Edit the XML File | Modify the XML file as previously described in the Prerequisites.Note In the ISO CAMT.053 bank statement file, always use ‘.’ as decimal point (don't use ‘,’). The date format should be YYYY-MM-DD. |  |  |
| 7 | Upload XML File | Upload the XML file you edited to the SFTP server folder.For example, copy to the folder /home/S4HTESTHCI/simbank/outbox/s4hana/v0115/QE421 2/AE/BANK1The internal test step is the simulation of communication between S/4HANA and SFTP server. You can run test program /BSNAGT/TEST_INBOUND_MSG2 via transaction code SA38 if the connection is not running. Populate CAMT.053.001.02 in the message type field and C:\Users\AB12345\Desktop\camt.053.001.02_AB12345_01.xml. in the file name field via search help. After execution, check whether incoming message is displayed in the MBC Connector Monitor.Note The path of the SFTP server folder for bank statements depends on testing system, tenant, country, and house bank.If you want to get sufficient information on how to access the MBC bank tenants or SFTP server, please contact test organizer for help.In this example, a CAMT.053 file for house bank/account ID AEBK1/AEAC1 in country AE is pulled from MBC. | The xml file is removed from the SFTP server folder in several seconds. A background job is scheduled to pull the bank statement from MBC to the S/4HANA system every 10 minutes. |  |

##### MT940 Format

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Prerequisite

As already described in section Business Condition, find a customer invoice created by another tester (the customer item must be uncleared), or perform step Enter Invoice without Sales Order in Accounts Receivable (J59), or Sell from Stock (BD9), Sales Order Processing – Project-Based Services (J14) to create a customer invoice. Make a note of the amount and reference (XBLNR in the header) of the customer invoice document. You need this information when simulating an electronic bank statement.

Perform step Bank Transfer Actions in test script J78: make a bank transfer with a payment method using payment medium format for MBC connectivity from bank account 0000000693123456 of bank 18121976 to bank account 0000000693123456 of bank 18121986 , amount AED 1191,72, please note down the information described in the Pull Status Message from MBC procedure.

Create a new text file and name it MT940_AE_AEBK1_00006.txt. Enter the following text into it and save it locally on your PC:

{1:F01[type 12 spaces here]0000000000}{2:O9401829041029LRLRXXXX4A0500004554351306031829N}{4:

:20:20141222173000

:25:BOFAUS3M/0000000693123456

:28C:00006/1

:60F:C141212AED5002,30

:61:141212C208,25NMSC0815

:86:051?00TestSAP?200090000008?32SCOTT

:61:141212D1191,72NMSC1000004612

:86:020?00TestSAP?204712?32SMITH

:62F:C141212AED4018,83

-}

|  |
| --- |
| Note Replace [type 12 spaces here] in the first line with the real 12 spaces in your MT940.txt file. |

|  |
| --- |
| Note If incoming MT940 bank statement file is split across multiple physical files with one page per file, it is supported in MBC to merge multiple files. The following prerequisites must be met to support this feature.Scenario is just applicable for the channel SWIFTIt is only available for customers who have an MBC connection to their bank.Time limit:If all multiple files in a statement sequence are not delivered within an MBC defined period of time, the incomplete MT940 file is forwarded anyway, as the statement aggregation assumes that a bank always sends all part-MT940s and MBC will not hold a partial MT940 without notifying the customer. |

Procedure

Perform the following steps to simulate a MT940 bank statement for house bank/account AEBK1/AEAC1. MBC maps the MT940 statement format to an ISO CAMT.053 format automatically, and the SAP S/4HANA system pulls the ISO CAMT.053 bank statement from MBC.

|  |
| --- |
| Note Provided that it is for testing purpose, for simplicity, before you maintain the transaction type, you can change the Bank Account Control Mode to simplify the bank account change process.Go to configuration activity 101025 Define Basic Settings as a Configuration Expert - Business Process Configuration, note down value of field Bank Account Control Mode, change it to 01 Direct Change. As mentioned in Pull Bank Statement from MBC, maintain the Payment Transaction Type Group of corresponding bank account with value MT940, and change the Bank Account Control Mode to the original value. |

|  |
| --- |
| Note In this example, the simulated bank statement contains two line items:First item: a credit item that is reconciled with an existing customer invoice. The customer invoice has been created (see the Prerequisites).Second item: a debit item that is reconciled with the payment document that was previously created in the Send Payment Instruction to MBC procedure. |

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Cash Management Specialist. |  |  |
| 2 | Access the SAP Fiori App | Open Manage Bank Statements (F1564). | The Manage Bank Statements (F1564) view displays. |  |
| 3 | Get Latest Bank Statement Number | To get the latest imported bank statement number, choose Show Filter Bar if search criteria are hidden, and make the following entries:Company Code: 3310House Bank: AEBK1House Bank Account: AEAC1Latest Statement: Latest onlyand choose Go. | The latest bank statement number of the specified bank account displays on the Manage Bank Statements view.The next bank statement number is one greater than the latest bank statement number. For example, if the latest bank statement number is 00005, the next number is 00006. If no latest bank statement was found, the next number should be 00001. |  |
| 4 | Get Closing Balance | Make a note of the closing balance of the specified bank account. It can be found on the Manage Bank Statements view. | The closing balance of the latest bank statement should be the opening balance of the next bank statement.If no latest bank statement was found, the opening balance of the next bank statement should be zero. |  |
| 5 | Save File | Refer to the text file MT940_AE_AEBK1_00006.txt you previously created in the Prerequisite section. The txt file name must contain the string MT940, for example, MT940_AE_AEBK1_00006.txt.Note MBC does not accept files with the same name. If more than one tester is testing this scenario, use a different file name every time when you test this step. |  |  |
| 6 | Open File | Using a text editor, open this txt file. |  |  |
| 7 | Edit File | Modify the txt file.Note In the MT940 bank statement file, always use ‘,’ as decimal point (don't use ‘.’). And the date format should be YYMMDD.Edit the following values in the MT940 file:Tag :20: (Bank Statement Reference): use current time as the bank statement reference during testing, format YYYYMMDDHHMMSS, for example 20141222173000.Tag :25: (Account definition): SWIFT code of bank/account number, for example, BOFAUS3M/0000000693123456, BOFAUS3M is the SWFIT code of AEBK1, 0000000693123456 is the account number of AEBK1. Edit tag :25: if you are not using AEBK1 during testing.Tag :28C: Statement number/page number, for example, 00006/1, statement number should be incremented by 1 for a new bank statement.Tag :60F: (Opening balance information): for example, C141212AED5002,30. Replace 141212 by the current date, format YYMMDD; replace 5002,30 by the closing balance of latest imported bank statement, or 0,00 for the first bank statement.First tag :61: in this example, 141212 is the value date (format YYMMDD), replace it by the current date; 208,25 is the amount of the incoming payment from customer, it should be equal to the receivables of customer invoice mentioned in Prerequisites.First tag :86: in this example, 0090000008 (after indicator ?20) is the reference of customer invoice (XBLNR), replace it by the reference of the customer invoice mentioned in Prerequisites.Second tag :61: in this example, 141212 is the value date (format YYMMDD), replace it by the current date; 1191,72 is the amount of an outgoing payment transaction, it should be equal to the amount of the payment document of bank transfer, which is described in Prerequisites; 1000004612 is the reference number, replace it by the Payment information ID you noted down previously from the Send Payment Instruction to MBC procedure:Tag :62F: (Closing balance information): for example, C141212AED4018,83. Replace 141212 by the current date, format YYMMDD; replace 4018,83 by the calculated closing balance, for example, closing balance = 5002,30 + 208,25 - 1191,72 = 4018,83. |  |  |
| 8 | Upload File | Upload the txt file you edited to the SFTP server folder.For example, upload to the folder /home/S4HTESTHCI/simbank/outbox/s4hana/v0115/QE4212/AEAEBK1The internal test step is the simulation of communication between S/4HANA and SFTP server. You can run test program /BSNAGT/TEST_INBOUND_MSG2 via transaction code SA38 if the connection is not running. Populate MT940 in the message type field and C:\Users\I071234\Desktop\MT940_DE_DEBK1_00006.txt. in the file name field via search help. After execution, check whether incoming message is displayed in the MBC Connector Monitor.Note The path of SFTP server folder for bank statements depends on the testing system, tenant, country, and house bank. If you want to get sufficient information on how to access the MBC bank tenants or SFTP server, please contact your test organizer for help.In this example, a MT940 bank statement file for house bank/account IDAEBK1/AEAC1 in country AE is pulled from SFTP by MBC. | The txt file vanishes from the SFTP server folder in several seconds.A background job is scheduled to pull the bank statement from MBC to the SAP S/4HANA system every 10 minutes. |  |

#### Import Electronic Bank Statement

Purpose

After the bank statement is pulled from Multi-Bank Connectivity (MBC), SAP S/4HANA imports the electronic bank statement automatically. The postings in bank accounting and subledger accounting should be performed.

The following posting rules are available for bank statement processing:

| Transactions | Text |
| --- | --- |
| F001 | Cash receipt via interim account |
| F002 | Checks In |
| F003 | Checks Out |
| F004 | Transfer Domestic/SEPA/Foreign |
| F005 | Other Disbursements |
| F006 | Other Receipts |
| F007 | Cash Payment |
| F008 | Cash Receipt |
| F009 | Direct Debit / Collection |
| F010 | Vendor Direct Debit |
| F011 | Bank Fee |
| F012 | Interest Received |
| F013 | Interest Paid |
| F014 | Returns Collection / Direct debit |
| F015 | Returns vendor direct debit |
| F016 | Unallocated Credit |
| F017 | Unallocated Debit |
| FCD1 | Direct Check Deposit |
| FCD2 | Check Deposit via interim Account |

Procedure

After the background job pulls the bank statement from MBC, SAP S/4HANA imports the bank statement automatically. You can monitor the imported electronic bank statements in the Fiori App Manage Bank Statements.

|  |
| --- |
| Note There is a column Manual Bank Statement to indicate if the bank statement is a manual bank statement or an imported electronic bank statement. |

If the Cash Management Full (Extended) version is implemented in the system, then you review the relevant payment document using the Check Cash Flow Items (F0735), to review the status. The status of the batch item should now be Stmt. Received.

|  |
| --- |
| Restriction The Check Cash Flow Items (F0735) app is not available in the Cash Management Basic (Core) version. |

#### Pull Bank Services Billing Files from MBC

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you simulate an ISO CAMT.086 bank fee file for bank 0000000693123456 import from MBC. SAP S/4HANA pulls the ISO CAMT.086 bank fee file from MBC and imports it automatically.

You can either upload the bank fee file manually via the Import Bank Services Billing Files app or import it via Multi-Bank Connectivity. For the manual upload process, see the Bank Fee Management ([2O0](https://me.sap.com/processnavigator/SolS/SolS-013/2608/SolP/2O0)) test script.

|  |
| --- |
| Note The CAMT.086 bank fee management is in the scope of Bank Fee Management (2O0), which requires an Advanced Cash Management license. |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Upload File | Upload the TXT file you edited to the SFTP server folder.For example, upload to the folder /home/S4HTESTHCI/simbank/outbox/s4hana/v0115/QE4212/DEDEBK1The internal test step is the simulation of communication between S/4HANA and SFTP server. You can run test program /BSNAGT/TEST_INBOUND_MSG2 via transaction code SA38 if the connection is not running. Populate camt.086.001.01 in the message type field and C:\Users\I071234\Desktop\Camt_086_DE_1133698_00001.xml. in the file name field via search help. After execution, check whether incoming message is displayed in the MBC Connector Monitor.Note The path of SFTP server folder for bank statements depends on the testing system, tenant, country, and house bank. If you want to get sufficient information on how to access the MBC bank tenants or SFTP server, contact your test organizer for assistance. | The TXT file disappears from the SFTP server folder in several seconds. A background job is scheduled to pull the bank statement from MBC to the SAP S/4HANA system every 10 minutes. |  |

#### Route Payment Files and Payment Transaction Messages

Purpose

In this activity, you simulate payment message and payment file import from MBC. SAP S/4HANA pulls the message and the file from MBC, then imports them automatically.

After import, the messages are routed into Advanced Payment Management for payment monitoring and approval.

|  |
| --- |
| Note The payment processing is in the scope of Advanced Payment Management ([4MT](https://me.sap.com/processnavigator/SolS/SolS-013/2608/SolP/4MT)), which requires an additional license. |

##### Route Payment Transaction Messages Initiated by SAP Systems

Purpose

In this activity, you simulate a FICA ISO PAIN.001 credit transfer payment message import from MBC. You can either download the payment media file manually via the Manage Payment Media app or import it via Multi-Bank Connectivity. For the manual download process, see the Contract Accounting – Company Initiated Payments ([2DP](https://me.sap.com/processnavigator/SolS/SolS-013/2608/SolP/2DP)) test script.

|  |
| --- |
| Note The supported FICA PAIN.001 message routing integration is in the scope of Contract Accounting – Company Initiated Payments (2DP), which requires an additional license. |

Procedure

This test step is automatically conducted. The payment message will be converted into APM metaformat and the following test step is described in test step Receive Payment Transaction Messages initiated by SAP Systems of test script Advanced Payment Management ([4MT](https://me.sap.com/processnavigator/SolS/SolS-013/2608/SolP/4MT)).

If automation is not supported in some cases such as payment on short notice, payment from subsidiaries, manual upload is also supported in test step Upload Bank Statement of test script Bank Integration with File Interface ([1EG](https://me.sap.com/processnavigator/SolS/SolS-013/2608/SolP/1EG)). The import file type is Payment File for Advanced Payment Management and the convert ID is ISO inbound MBC.

##### Route Payment Files Initiated by non-SAP Systems

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you simulate a CSV payment file imported from MBC.

|  |
| --- |
| Note The CSV payment template can be found in test step Receive Payment Files Initiated by non-SAP Systems of test script Advanced Payment Management ([4MT](https://me.sap.com/processnavigator/SolS/SolS-013/2608/SolP/4MT)). |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Upload File | Upload the CSV file you edited to the SFTP server folder.For example, upload to the folder /home/S4HTESTHCI/simbank/outbox/s4hana/v0115/QE4212/DEDEBK1. The internal test step is the simulation of communication between S/4HANA and SFTP server. You can run test program /BSNAGT/TEST_INBOUND_MSG2 via transaction code SA38 if the connection is not running. Populate SAP_APM_DEMO_CSV_CT in the message type field and C:\Users\IAB1234\Desktop\IFME_TESTFILE_P1.csv. in the file name field via search help. After execution, check whether incoming message is displayed in the MBC Connector Monitor.Note The path of SFTP server folder for bank statements depends on the testing system, tenant, country, and house bank. If you want to get sufficient information on how to access the MBC bank tenants or SFTP server, contact your test organizer for assistance. | The CSV file disappears from the SFTP server folder in several seconds. A background job is scheduled to pull the bank statement from MBC to the SAP S/4HANA system every 10 minutes. |  |

#### Monitor Situations

Purpose

In this activity, you monitor situations and check instance details.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Business Process Specialist. |  |  |
| 2 | Access App | Open Monitor Situations (F3264). |  |  |
| 3 | Enter Selection Criteria | In the upper area, make the following entries and press Enter:Situation Type ID: ZFIN_MBC_MESSAGE_ERRORZFIN_MBC_MESSAGE_NO_MANPROCZFIN_MBC_MESSAGE_NO_RECEIVEDYear: for example, <current year> | A chart and a list with instances that are displayed for outgoing payment situations:ZFIN_MBC_MESSAGE_ERROR: Shows all incoming messages with Error statusZFIN_MBC_MESSAGE_MANPROC: Shows all incoming messages with Manual Processing Required statusZFIN_MBC_MESSAGE_RECEIVED: Shows all incoming messages with Received status |  |
| 4 | Check Instance | Expand the hierarchy by respective situation ID, you can check the instance triggered by each message. In this case, the Anchor Object Key is the MBC message ID.Note If you can not find the Anchor Object Key, you can choose Settings and select the columns to be visible in the list. | The MBC message ID which triggered the situation is displayed. You can check more details in the App Manage Bank Messages (F4385). For more details, you can refer to test step MBC Message Monitor. |  |

#### Check Notification

Purpose

In this activity, the notification is checked by the recipient who is assigned to team members in preliminary step.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a recipient (for example, Bank Integration Specialist). |  |  |
| 2 | Check Notification | On the home page, choose Notifications in the upper right corner.Choose By Type, under type Bank Message Entering Error Status, Bank Message Requires Manual Processing or Bank Message Still in Status Received has been identified, choose Expand Group. |  |  |

### MBC Message Monitor

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you monitor all the messages transmitted out of S/4HANA via MBC and messages transmitted into S/4HANA via MBC.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Business Integration Specialist - Bank Integration. |  |  |
| 2 | Access App | Open Manage Bank Messages (F4385). |  |  |
| 3 | Enter Selection Criteria | In the upper area, make the following entries and press Enter:Message Type: CAMT.053.001.02Creation Date: For example, <today’s date> | The MBC messages are displayed in respective tabs:Outgoing Messages tab: Shows all the payment media files transmitted from SAP S/4HANAIncoming Messages tab: Shows all bank statements and lockbox files transmitted from MBCFor Manual Processing tab: Show all messages received with message types that are unknown to the MBC Connector.Error: Show all messages with error status.Created: Show all messages with issues of sending messages. |  |
| 4 | Display Message Content | Select a message and choose View Payload in the detail screen of message. | The message content is displayed. |  |
| 5 | Navigation to Application Log | Select a message and choose Log in the detail screen of message. | The detail log of the message processing is listed. |  |

## Appendix

### Process Integration

The process to be tested in this test script is part of a chain of integrated processes.

### Succeeding Processes

After completing the activities in this test script, you can continue testing the following business processes:

| Process | Business Condition |
| --- | --- |
| Basic Cash Operations (BFB)andAdvanced Cash Operations (J78) | If the Full (Extended) Cash Management is implemented:After the payment status message is pulled from MBC, check the status change in app Check Cash Flow Items and app Monitor Payments.After the bank statement is imported via MBC, check the status in app Bank Statement Monitor. |

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
- related-to :: [[05-treasury-and-cash-management/test-script-bank-integration-with-file-interface-1eg-ae-sap-s-4hana-cl]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/16R_S4CLD2608_BPD_EN_AE.docx` — full document · extracted with `mammoth` · 75,742 chars in the whole document
