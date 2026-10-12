---
id: 05-treasury-and-cash-management/test-script-bank-fee-management-2o0-ae-sap-s-4hana-cloud-public-editio
title: "Test Script: Bank Fee Management (2O0_AE), SAP S/4HANA Cloud Public Edition (2O0_S4CLD2608_BPD_EN_AE)"
description: "SAP test script for scope item 2O0 (AE): importing bank billing files, managing bank fee and interest conditions, monitoring and validating bank fees; dated 19-06-26."
cluster: 05-treasury-and-cash-management
tags: [kb/treasury-and-cash-management, topic/bank-fee-management]
aliases: [2O0_S4CLD2608_BPD_EN_AE]
keywords: [Bank Fee Management, bank services billing files, bank fee conditions, bank fee monitoring, pricing validation status, bank service mapping, bank account interest, camt.086 xml mapping, field value codes, business roles]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/2O0_S4CLD2608_BPD_EN_AE.docx]
confidence: high
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-840
topic: 05-treasury-and-cash-management/bank-fee-management
language: EN
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Test Script: Bank Fee Management (2O0_AE), SAP S/4HANA Cloud Public Edition (2O0_S4CLD2608_BPD_EN_AE)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/2O0_S4CLD2608_BPD_EN_AE.docx`, extracted with `mammoth`. Grouped under **Bank Fee Management** in Treasury and Cash Management. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

| <!-- image omitted: unnamed --> | Test ScriptSAP S/4HANA Cloud Public Edition - 19-06-26 |
| --- | --- |
|  | Bank Fee Management (2O0_AE) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Table of Contents

[1 Purpose 3](#_Toc232849646)

[2 Prerequisites 4](#_Toc232849647)

[2.1 System Access 4](#_Toc232849648)

[2.2 Roles 4](#_Toc232849649)

[2.3 Master Data, Organizational Data, and Other Data 4](#_Toc232849650)

[2.4 Preliminary Steps 5](#_Toc232849651)

[2.4.1 Define Authorization Group for Interest Condition 6](#_Toc232849652)

[3 Overview Table 8](#_Toc232849653)

[4 Test Procedures 10](#_Toc232849654)

[4.1 Import Bank Services Billing Files 10](#_Toc232849655)

[4.2 Manage Bank Fee Conditions 20](#_Toc232849656)

[4.2.1 General Check of Bank Fee Conditions 20](#_Toc232849657)

[4.2.2 Create Bank Fee Conditions 21](#_Toc232849658)

[4.2.3 Edit Bank Fee Conditions 23](#_Toc232849659)

[4.2.4 Delete Bank Fee Conditions 25](#_Toc232849660)

[4.2.5 Import Bank Fee Conditions 26](#_Toc232849661)

[4.2.6 Maintain Bank Fee Condition Deletion and Downloads 27](#_Toc232849662)

[4.3 Monitor Bank Fees 28](#_Toc232849663)

[4.3.1 Bank Fees General Check 29](#_Toc232849664)

[4.3.2 Assign Validation Condition 31](#_Toc232849665)

[4.3.3 Change Pricing Validation Status 32](#_Toc232849666)

[4.3.4 Bank Service Mapping 33](#_Toc232849667)

[4.4 Manage Interest Condition 34](#_Toc232849668)

[4.4.1 Create Interest Condition 34](#_Toc232849669)

[4.4.2 Bank Account Interest Calculation 36](#_Toc232849670)

[4.4.3 Monitor Bank Account Interests 37](#_Toc232849671)

[5 Appendix 38](#_Toc232849672)

[5.1 Field Mapping - Monitor Bank Frees to XML Category 38](#_Toc232849673)

[5.2 Field Mapping - Service Details to XML Category 39](#_Toc232849674)

[5.3 Field Value Descriptions 40](#_Toc232849675)

## Purpose

Overview

This scope item provides comprehensive functionalities in bank fee management, such as the maintenance of the bank fee conditions and monitoring and validation of the bank fees.

You start by importing the bank service billing files into the SAP S/4HANA Cloud Public Edition system. You then create, edit, or delete the bank fee calculation conditions in the SAP S/4HANA Cloud Public Edition system per the agreements you have with the banks and assign them to the corresponding bank fee items. You check the bank fees in different views or dimensions and with different detail levels. You can also validate them based on the assigned conditions and set the validation status accordingly.

This document provides a detailed procedure for testing this scope item after solution activation, reflecting the predefined scope of the solution. Each process step, report, or item is covered in its own section, providing the system interactions (test steps) in a table view. Steps that are not in scope of the process but are needed for testing are marked accordingly. Project-specific steps must be added.

|  |
| --- |
| Note Values in this test script (decimal notation, date formats, and so on) are presented in U.S. standard notation. If your test system is set up to use a different notation, enter values as appropriate. |

|  |
| --- |
| Remember After each system upgrade or improvement, you must review the settings in the configuration activity Define Basic Settings before continuing any business operation in the system. You must correct any differences you find compared to the state prior to activation. |

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

| Name (Role Template) | ID (Role Template) | Name (Launchpad Space) | ID (Launchpad Space) | Log on |
| --- | --- | --- | --- | --- |
| Cash Management Specialist | SAP_BR_CASH_SPECIALIST | Cash Management | SAP_BR_CASH_SPECIALIST |  |
| Cash Manager | SAP_BR_CASH_MANAGER | Cash Management | SAP_BR_CASH_MANAGER |  |

### Master Data, Organizational Data, and Other Data

Default Values

The organizational structure and master data of your company have been created in your system during activation. The organizational structure reflects the structure of your company. These master data represent materials, customers, and vendors, for example, depending on the operational focus of your company.

|  |
| --- |
| Caution Update Behavior of Predelivered Demo DataIn non-productive environments (such as starter systems, sandbox systems, or partner demo systems), SAP initially deploys demo data for your selected scope. You can use this data to test and evaluate business processes.In a customer system, you can receive new or updated demo data after initial activation with further scope enhancements, provided the existing demo data wasn't changed in an incompatible way. If activation errors occur due to incompatible changes in demo data, you're responsible for resolving them. If you don't resolve the errors within a specific time frame, SAP reserves the right to deactivate demo data in your systems. In this case, you can continue by creating your own demo data. Alternatively, you can request that your systems be reprovisioned if you want to work with predelivered demo data again.In partner systems, you can use the demo data deployed with the initial activation. No additional demo data will be deployed in the system with scope enhancements. You can only create additional demo data manually. |

Use your own master data or the following sample data to go through the test procedure.

The business process is enabled with this organization-specific master data, examples are provided in the next section.

Operational Focus

SAP Best Practices delivers standard values for more than one operational focus area, such as Services, Manufacturing, or Trade. This means that you may find more than one master data table below. Use the master data that matches the operational focus of your company (Services, Manufacturing, or Trade).

|  |
| --- |
| Note Additional Default Values You can test the scope item with other SAP Best Practices default values that have the same characteristics. Review your SAP ECC system to find out which other material master data exists. |

|  |
| --- |
| Note Using Your Own Master Data You can also use customized values for any material or organizational data for which you have created master data. For more information about creating master data, see the Master Data Procedures documentation. |

Use the following master data in the process steps described in this document:

|  |
| --- |
| Caution The following Sample Values assume that you are only implementing one of the three Maintain Signatory in Multiple Accountswith Full Cash Procedures Management and … procedure steps. If you are implementing and testing more than one, especially in a single environment, you cannot use the same Master Data values for more than one procedure type. You must create additional Master Data values, for example G/L Accounts, and then use these different values in each procedure type. |

### Preliminary Steps

To use the function of Bank Fee Management, the Cash Scope of General Setting for Cash Management must be set as Full Scope.

Procedure

Depending on your configuration environment for SAP S/4HANA Cloud Public Edition, choose one of the following options:Full Scope

Manage Your Solution:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log onto the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. |  |  |
| 2 | FullAccess the SAP Fiori app for Cloud systems | Open Manage Your Solution > Configure Your Solution > Basic Settings. | The Basic Settings screen displays. |  |
| 3 | Define Basic Settings | Choose Full Scope in the Cash Scope field. |  |  |

SAP Central Business Configuration:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the project experience in SAP Central Business Configuration. |  |  |
| 2 | Access Basic Settings | Go to the Business Processes Configuration app. To locate the activity in the tree view, search for the following activity: Basic Settings.Choose Open Documentation for the found line item to see more details about this configuration activity.Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. | The Basic Settings screen displays. |  |
| 3 | Basic Settings | Choose Full Scope in the Cash Scope field. |  |  |

|  |
| --- |
| Remember Basic Settings must be reviewed following any system upgrade or improvement before continuing any business operation in the system. When differences are found from previous activations, you must correct in the SSCUI Basic Settings, using the generic user Configuration Expert - Business Process Configuration in the Manage Your Solution app. |

#### Define Authorization Group for Interest Condition

Purpose

This activity describes the approach to define authorization groups to restrict access to different bank account interest conditions. You use this configuration activity to define authorization groups for bank account interest conditions. For each bank account interest condition, you can assign an authorization group so that only authorized users can access the bank account interest condition.

Procedure

Depending on your configuration environment for SAP S/4HANA Cloud Public Edition, choose one of the following options:

Configure Your Solution:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. | The SAP Fiori launchpad displays |  |
| 2 | Access the SAP Fiori App | Open Manage Your Solution (F1241).Choose Configure Your Solution.Search for Define Authorization Groups for Interest Conditions or Configuration Activity ID: 107208 via the search filter.Choose the Configure button in the Define Authorization Groups for Interest Conditions step. | The Define Settings for Bank Account Master Data screen is displayed. |  |
| 3 | Maintain Authorization Group | Choose New Entries.Make the following entries and choose Save:Authorization Group: ZAGFIRDescription: Authorization Group for Interest Condition |  |  |

SAP Central Business Configuration:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the project experience in SAP Central Business Configuration. | The SAP Fiori launchpad displays |  |
| 2 | Open Define Settings for Bank Account Master Data | Go to the Business Processes Configuration app. To locate the activity in the tree view, search for the following activity: Define Authorization Groups for Interest Conditions.Choose Open Documentation for the found line item to see more details about this configuration activity.Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. | The Define Settings for Bank Account Master Data screen displays. |  |
| 3 | Maintain Authorization Group | Choose New Entries.Make the following entries and choose Save:Authorization Group: ZAGFIRDescription: Authorization Group for Interest Condition |  |  |

## Overview Table

The Bank Fee Management (2O0) scope item consists of several process steps described in the following tables.

|  |
| --- |
| Note If your system administrator has enabled spaces and pages on the SAP Fiori launchpad, the homepage will only contain the essential apps for performing the typical tasks of a business role.You can find all other (searchable) apps not included on the homepage using the search bar ([2434549](https://me.sap.com/notes/2434549)).If you want to personalize the homepage and include the hidden apps, navigate to your user profile and choose App Finder. |

| Process Step, Report or Item | Business Role | Transaction/APP | Expected Results |
| --- | --- | --- | --- |
| [Import Bank Services Billing Files](#unique_9) [page ] 10 | Cash Management Specialist |  | Bank Service Billing Files are imported. |
| Manage Bank Fee Conditions |  |  |  |
| [General Check of Bank Fee Conditions](#unique_10) [page ] 20 | Cash Management Specialist | Manage Bank Fee Conditions (F3185) | Bank Fee Conditions are checked. |
| [Create Bank Fee Conditions](#unique_11) [page ] 21 | Cash Manager | Manage Bank Fee Conditions (F3185) | Bank Fee Conditions are created. |
| [Edit Bank Fee Conditions](#unique_12) [page ] 23 | Cash Manager | Manage Bank Fee Conditions (F3185) | Bank Fee Conditions are updated. |
| [Delete Bank Fee Conditions](#unique_13) [page ] 25 | Cash Manager | Manage Bank Fee Conditions (F3185) | Bank Fee Conditions are deleted. |
| [Import Bank Fee Conditions](#unique_14) [page ] 26 | Cash Manager | Manage Bank Fee Conditions (F3185) | Bank Fee Conditions are imported. |
| [Maintain Bank Fee Condition Deletion and Downloads](#unique_15) [page ] 27 | Cash Manager | Manage Bank Fee Conditions (F3185) | Bank Fee Conditions are maintained. |
| Monitor Bank Fees |  |  |  |
| [Bank Fees General Check](#unique_16) [page ] 29 | Cash Management Specialist | Monitor Bank Fees (F3001) | Bank Fees are displayed. |
| [Assign Validation Condition](#unique_17) [page ] 31 | Cash Management Specialist | Monitor Bank Fees (F3001) | Validation Condition is assigned. |
| [Change Pricing Validation Status](#unique_18) [page ] 32 | Cash Management Specialist | Monitor Bank Fees (F3001) | Pricing Validation Status are changed. |
| [Bank Service Mapping](#unique_19) [page ] 33 | Cash Management Specialist | Manage Banks - Cash Management (F1574A) | Banks are updated. |
| Manage Interest Condition |  |  |  |
| [Create Interest Condition](#unique_20) [page ] 34 | Cash Management Specialist | Manage Bank Account Interest Conditions (F9017) | You can create interest condition. |
| [Bank Account Interest Calculation](#unique_21) [page ] 36 | Cash Management Specialist | Schedule Jobs for Bank Account Interest Calculation (F9016) | You can calculate bank account interest. |
| [Monitor Bank Account Interests](#unique_22) [page ] 37 | Cash Management Specialist | Monitor Bank Account Interests (F9015) | You can monitor bank account interest. |

## Test Procedures

This section describes test procedures for each process step that belongs to this scope item.

### Import Bank Services Billing Files

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you import a Camt_086 Bank Fee file for the 0000000693123456 bank account. If you implemented Multi-Bank Connectivity Connector, the import process is automatically triggered.

Prerequisite

Create a new xml file with the name: Camt_086_AE_0000000693123456_00001.xml.

Open the file in a text editor and enter the following code into it, then save it locally on your PC:

<?xml version="1.0" encoding="utf-8"?>
<Document xmlns="urn:iso:std:iso:20022:tech:xsd:camt.086.001.01" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
 <BkSvcsBllgStmt>
 <RptHdr>
 <RptId>RPT_20170816_AE_18121976_3310_0001</RptId>
 </RptHdr>
 <BllgStmtGrp>
 <GrpId>GRP_20170816_0001</GrpId>
 <Sndr>
 <Nm>Bank 1 - SAMPLE BANK</Nm>
 <Id>
 <FIId>
 <BICFI>BOFAUS3M</BICFI>
 </FIId>
 </Id>
 <CtryOfRes>AE</CtryOfRes>
 </Sndr>
 <Rcvr>
 <Nm>Company Code 3310</Nm>
 <Id>
 <OrgId>
 <AnyBIC>3310</AnyBIC>
 </OrgId>
 </Id>
 <CtryOfRes>AE</CtryOfRes>
 </Rcvr>
 <BllgStmt>
 <StmtId>GRP_AE_18121976_3310_1</StmtId>
 <FrToDt>
 <FrDt>2017-08-01</FrDt>
 <ToDt>2017-08-31</ToDt>
 </FrToDt>
 <CreDtTm>2017-08-31T00:00:00</CreDtTm>
 <Sts>ORGN</Sts>
 <AcctChrtcs>
 <AcctLvl>SMRY</AcctLvl>
 <CshAcct>
 <Id>
 <Othr>
 <Id>0000000693123456</Id>
 </Othr>
 </Id>
 <Ccy>AED</Ccy>
 </CshAcct>
 <CompstnMtd>DDBT</CompstnMtd>
 <DbtAcct>
 <Othr>
 <Id>0000000693123456</Id>
 </Othr>
 </DbtAcct>
 <DelydDbtDt>2017-08-01</DelydDbtDt>
 <SttlmAdvc>Settlement Advice</SttlmAdvc>
 <AcctBalCcyCd>AED</AcctBalCcyCd>
 <SttlmCcyCd>AED</SttlmCcyCd>
 <HstCcyCd>AED</HstCcyCd>
 <Tax>
 <ClctnMtd>MTDC</ClctnMtd>
 <Rgn>AED</Rgn>
 <NonResCtry>
 <Ctry>AE</Ctry>
 </NonResCtry>
 </Tax>
 </AcctChrtcs>
 <RateData>
 <Id>
 <Cd>RATE1</Cd>
 </Id>
 <Val>10.6800</Val>
 <DaysInPrd>30</DaysInPrd>
 <DaysInYr>365</DaysInYr>
 </RateData>
 <RateData>
 <Id>
 <Cd>RATE2</Cd>
 </Id>
 <Val>37.9300</Val>
 <DaysInPrd>30</DaysInPrd>
 <DaysInYr>365</DaysInYr>
 </RateData>
 <RateData>
 <Id>
 <Cd>RATE3</Cd>
 </Id>
 <Val>4.9500</Val>
 <DaysInPrd>30</DaysInPrd>
 <DaysInYr>365</DaysInYr>
 </RateData>
 <CcyXchg>
 <SrcCcy>USD</SrcCcy>
 <TrgtCcy>EUR</TrgtCcy>
 <XchgRate>1.1434</XchgRate>
 <Desc>Desc-USD-EUR</Desc>
 <UnitCcy>EUR</UnitCcy>
 <Cmnts>Cmnts_USD_EUR</Cmnts>
 <QtnDt>2017-08-01T00:00:00</QtnDt>
 </CcyXchg>
 <CcyXchg>
 <SrcCcy>GBP</SrcCcy>
 <TrgtCcy>EUR</TrgtCcy>
 <XchgRate>2.00000</XchgRate>
 <Desc>Desc-GBP-EUR</Desc>
 <UnitCcy>EUR</UnitCcy>
 <Cmnts>Cmnts_GBP_EUR</Cmnts>
 <QtnDt>2017-08-01T00:00:00</QtnDt>
 </CcyXchg>
 <CcyXchg>
 <SrcCcy>JPY</SrcCcy>
 <TrgtCcy>EUR</TrgtCcy>
 <XchgRate>2.00000</XchgRate>
 <Desc>Desc-JPY-EUR</Desc>
 <UnitCcy>EUR</UnitCcy>
 <Cmnts>Cmnts_JPY_EUR</Cmnts>
 <QtnDt>2017-08-01T00:00:00</QtnDt>
 </CcyXchg>
 <CcyXchg>
 <SrcCcy>CNY</SrcCcy>
 <TrgtCcy>EUR</TrgtCcy>
 <XchgRate>2.00000</XchgRate>
 <Desc>Desc-CNY-EUR</Desc>
 <UnitCcy>EUR</UnitCcy>
 <Cmnts>Cmnts_CNY_EUR</Cmnts>
 <QtnDt>2017-08-01T00:00:00</QtnDt>
 </CcyXchg>
 <Bal>
 <Tp>
 <Cd>LBME</Cd>
 </Tp>
 <Val>
 <Amt Ccy="EUR">8821093.180000</Amt>
 <Sgn>false</Sgn>
 </Val>
 <CcyTp>ACCT</CcyTp>
 </Bal>
 <Bal>
 <Tp>
 <Cd>CABN</Cd>
 </Tp>
 <Val>
 <Amt Ccy="EUR">1664820.670000</Amt>
 <Sgn>false</Sgn>
 </Val>
 <CcyTp>ACCT</CcyTp>
 </Bal>
 <Compstn>
 <Tp>
 <Cd>SCBT</Cd>
 </Tp>
 <Val>
 <Amt Ccy="AED">336.600000</Amt>
 <Sgn>true</Sgn>
 </Val>
 <CcyTp>STLM</CcyTp>
 </Compstn>
 <Compstn>
 <Tp>
 <Cd>TXTS</Cd>
 </Tp>
 <Val>
 <Amt Ccy="AED">124.542000</Amt>
 <Sgn>true</Sgn>
 </Val>
 <CcyTp>STLM</CcyTp>
 </Compstn>
 <Compstn>
 <Tp>
 <Cd>CTND</Cd>
 </Tp>
 <Val>
 <Amt Ccy="AED">461.142000</Amt>
 <Sgn>true</Sgn>
 </Val>
 <CcyTp>STLM</CcyTp>
 </Compstn>
 <Compstn>
 <Tp>
 <Cd>FESS</Cd>
 </Tp>
 <Val>
 <Amt Ccy="AED">461.142000</Amt>
 <Sgn>true</Sgn>
 </Val>
 <CcyTp>STLM</CcyTp>
 </Compstn>
 <Svc>
 <SvcDtl>
 <BkSvc>
 <Id>1044</Id>
 <Desc>SVC_1044</Desc>
 <SubSvc>
 <Issr>
 <Cd>AFP</Cd>
 </Issr>
 <Id>1606</Id>
 </SubSvc>
 <CmonCd>
 <Issr>AFP</Issr>
 <Id>2000</Id>
 </CmonCd>
 </BkSvc>
 <Vol>306</Vol>
 </SvcDtl>
 <Pric>
 <UnitPric>
 <Amt Ccy="AED">1.100000</Amt>
 <Sgn>true</Sgn>
 </UnitPric>
 </Pric>
 <PmtMtd>FLAT</PmtMtd>
 <OrgnlChrgPric>
 <Amt Ccy="AED">336.600000</Amt>
 <Sgn>true</Sgn>
 </OrgnlChrgPric>
 <OrgnlChrgSttlmAmt>
 <Amt Ccy="EUR">336.600000</Amt>
 <Sgn>true</Sgn>
 </OrgnlChrgSttlmAmt>
 <TaxDsgnt>
 <Cd>ZERO</Cd>
 <Rgn>AE</Rgn>
 </TaxDsgnt>
 <TaxClctn/>
 </Svc>
 <TaxRgn>
 <RgnNb>AE</RgnNb>
 <RgnNm>AE</RgnNm>
 <CstmrTaxId>3310</CstmrTaxId>
 <PtDt>2017-08-31</PtDt>
 <InvcNb>2017-08-31</InvcNb>
 <MtdC>
 <SvcDtl>
 <BkSvc>
 <Id>1044</Id>
 <SubSvc>
 <Issr>
 <Cd>AFP</Cd>
 <Id>1606</Id>
 </Issr>
 </SubSvc>
 <Desc>SVC_1044</Desc>
 </BkSvc>
 <Vol>306</Vol>
 <UnitPric>
 <Amt Ccy="AED">1.100000</Amt>
 <Sgn>true</Sgn>
 </UnitPric>
 <SvcChrgAmt>
 <Amt Ccy="AED">336.600000</Amt>
 <Sgn>true</Sgn>
 </SvcChrgAmt>
 </SvcDtl>
 <TaxClctn>
 <HstCcy>EUR</HstCcy>
 <TaxblSvcChrgConvs>
 <SrcAmt>
 <Amt Ccy="EUR">336.600000</Amt>
 <Sgn>true</Sgn>
 </SrcAmt>
 <HstAmt>
 <Amt Ccy="EUR">336.600000</Amt>
 <Sgn>true</Sgn>
 </HstAmt>
 </TaxblSvcChrgConvs>
 <TtlTaxblSvcChrgHstAmt>
 <Amt Ccy="EUR">336.600000</Amt>
 <Sgn>true</Sgn>
 </TtlTaxblSvcChrgHstAmt>
 <TaxId>
 <Nb>100180</Nb>
 <Desc>Tax100180</Desc>
 <Rate>11.0000</Rate>
 <TtlTaxAmt>
 <Amt Ccy="EUR">37.026000</Amt>
 <Sgn>true</Sgn>
 </TtlTaxAmt>
 </TaxId>
 <TaxId>
 <Nb>100190</Nb>
 <Desc>Tax100190</Desc>
 <Rate>11.5000</Rate>
 <TtlTaxAmt>
 <Amt Ccy="EUR">38.709000</Amt>
 <Sgn>true</Sgn>
 </TtlTaxAmt>
 </TaxId>
 <TaxId>
 <Nb>100250</Nb>
 <Desc>Tax100250</Desc>
 <Rate>14.5000</Rate>
 <TtlTaxAmt>
 <Amt Ccy="EUR">48.807000</Amt>
 <Sgn>true</Sgn>
 </TtlTaxAmt>
 </TaxId>
 <TtlTax>
 <Amt Ccy="AED">124.542000</Amt>
 <Sgn>true</Sgn>
 </TtlTax>
 </TaxClctn>
 </MtdC>
 <SttlmAmt>
 <Amt Ccy="EUR">124.542000</Amt>
 <Sgn>true</Sgn>
 </SttlmAmt>
 <TaxDueToRgn>
 <Amt Ccy="EUR">124.542000</Amt>
 <Sgn>true</Sgn>
 </TaxDueToRgn>
 </TaxRgn>
 <BalAdjstmnt>
 <Type>FLOT</Type>
 <Desc>Adjustment</Desc>
 <BalAmt>
 <Amt Ccy="EUR">8257653.760000</Amt>
 <Sgn>false</Sgn>
 </BalAmt>
 <AvrgAmt>
 <Amt Ccy="EUR">1436195.140000</Amt>
 <Sgn>true</Sgn>
 </AvrgAmt>
 <ErrDt>2017-07-15</ErrDt>
 <PstngDt>2017-08-15</PstngDt>
 <Days>30</Days>
 <EarngsAdjstmntAmt>
 <Amt Ccy="EUR">1116008.040000</Amt>
 <Sgn>false</Sgn>
 </EarngsAdjstmntAmt>
 </BalAdjstmnt>
 <SvcAdjstmnt>
 <Type>COMP</Type>
 <Desc>Error Correction</Desc>
 <Amt>
 <Amt Ccy="EUR">575.630000</Amt>
 <Sgn>false</Sgn>
 </Amt>
 <BalReqrdAmt>
 <Amt Ccy="EUR">3990198.320000</Amt>
 <Sgn>true</Sgn>
 </BalReqrdAmt>
 <ErrDt>2017-07-15</ErrDt>
 <AdjstmntId>1044</AdjstmntId>
 <SubSvc>
 <Issr>
 <Cd>AFP</Cd>
 </Issr>
 <Id>1606</Id>
 </SubSvc>
 <PricChng>
 <Amt Ccy="EUR">10.000000</Amt>
 <Sgn>true</Sgn>
 </PricChng>
 <OrgnlPric>
 <Amt Ccy="EUR">1.100000</Amt>
 <Sgn>true</Sgn>
 </OrgnlPric>
 <NewPric>
 <Amt Ccy="EUR">11.100000</Amt>
 <Sgn>true</Sgn>
 </NewPric>
 <VolChng>10</VolChng>
 <OrgnlVol>306</OrgnlVol>
 <NewVol>316</NewVol>
 <OrgnlChrgAmt>
 <Amt Ccy="EUR">336.600000</Amt>
 <Sgn>true</Sgn>
 </OrgnlChrgAmt>
 <NewChrgAmt>
 <Amt Ccy="EUR">3507.600000</Amt>
 <Sgn>true</Sgn>
 </NewChrgAmt>
 </SvcAdjstmnt>
 </BllgStmt>
 </BllgStmtGrp>
 </BkSvcsBllgStmt>
</Document>

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as Cash Management Specialist. |  |  |
| 2 | Access the SAP Fiori App | Open Import Bank Services Billing Files (F3002). |  |  |
| 3 | Open XML File | Use a text editor to open the XML file you created in the prerequisites.Note Ensure that a valid exchange rate between source currency/bank account currency and target currency in the file is already maintained. For more information, see the Maintain Exchange Rate procedure in the Accounting and Financial Close (J58) test script. |  |  |
| 4 | Edit XML file | Modify the values in the XML file as described below.Edit these values in Camt086 file:<RptId>RPT_20170816_AE_18121976_3310_0001</RptId>:RPT_20170816_AE_18121976_3310_0001 is the report ID, use the different report ID each time you import bank fee, for example, RPT_20170816_AE_18121976_3310_0002, because it overwrites the bank fee report having the same report ID.<Nm>Bank 1 - SAMPLE BANK</Nm>: the name of bank key 18121976, for example, Bank 1 - SAMPLE BANK<BICFI>BOFAUS3M</BICFI>: The BIC of the bank account 0000000693123456, for example, BOFAUS3M.<Nm>Company Code 3310</Nm>: The description of company code 3310, for example,Company Code 3310.<AnyBIC>3310</AnyBIC>: The company code number, for example, 3310.<StmtId>GRP_AE_18121976_3310_1</StmtId>: The statement ID for the bank fee report, for example, GRP_ AE_18121976_3310_1.<FrDt>2017-08-01</FrDt> and <ToDt>2017-08-31</ToDt>: The date range for bank fee import, for example, from start day to end day of current month.<Id>0000000693123456</Id>: It indicates the bank account number used in the bank fee report, for example, 0000000693123456.Remember<Tp> <Cd>SCBT</Cd> </Tp> <Val> <Amt Ccy="USD">336.600000</Amt>: <Cd>SCBT</Cd> indicates Service Total Amount. <Tp> <Cd>TXTS</Cd> </Tp> <Val> <Amt Ccy="USD">124.542000</Amt>: <Cd>TXTS</Cd> indicates Tax Total Amount. <Tp> <Cd>CTND</Cd> </Tp> <Val> <Amt Ccy="USD">461.142000</Amt>: <Cd>CTND</Cd>This code block indicates the Total Amount of both the Service Amount and the Tax Amount. For example, 461.142000=336.600000+124.542000. |  |  |
| 5 | Save | Save the modified XML file with the name Camt_086_0000000693123456_00001.xml to your local PC. |  |  |
| 6 | Upload | Locate the Select Source File field.Choose the file picker icon on the right of the Select Source File field to select your XML file.In the file browser dialog, select the XML file and choose Open.Choose Import.Caution If the system displays the warning Report IDAE_18121976_3310_00001 was imported. Do you want to overwrite the last import?, the report ID is already used in the previous bank fee reports. To continue import, choose OK. This overwrites the bank fee report. To stop the import, choose Cancel, and then modify the report ID for your XML file and try again. | The message File imported. displays. |  |
| 7 | Manage Source File | To delete a bank fee report, select the checkbox for a bank fee report and choose Delete. A dialog box displays the message By deleting a source file, you delete the data that was imported from the file. Do you still want to delete the source file?. Choose Delete to confirm. |  |  |

### Manage Bank Fee Conditions

In this section, you review, create, edit, and delete bank fee conditions using the Manage Bank Fee Conditions features.

#### General Check of Bank Fee Conditions

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you review bank fee conditions.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Cash Management Specialist. |  |  |
| 2 | Access the SAP Fiori App | Open Manage Bank Fee Conditions (F3185). |  |  |
| 3 | Display Conditions | Choose Go. | Bank fee conditions are displayed. |  |
| 4 | Review Conditions | Choose Settings. | The View Settings dialog box displays all available fields for bank fee conditions.Note Select and deselect fields as required. You can also change sorting, filtering, and grouping settings. |  |
| 5 | Close Settings | Choose Cancel. |  |  |
| 6 | Display | Enter any desired search conditions and choose Go. | Bank accounts are listed based on search criteria. |  |

#### Create Bank Fee Conditions

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you create bank fee conditions.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Cash Manager. |  |  |
| 2 | Access the SAP Fiori app | Open Manage Bank Fee Conditions (F3185). |  |  |
| 3 | Create Conditions | Choose the Create icon. | The Bank Fee Conditions view displays. |  |
| 4 | Enter Data | Make the following entries and choose Save:Condition ID:20180216EUValid From: <current date>Pricing Type: 01 (Unit Pricing (Standard)); see Note belowCondition Currency: AEDUnit Price: 1Base Charge: 2Minimum Charge: 1Maximum Charge: 3Note Five pricing types are supported:Unit Pricing (Standard)Editable fields for this include:Unit PriceBase ChargeMinimum ChargeMaximum ChargeFlat PricingEditable fields for this include:Unit PriceBalance based pricingEditable fields for this include:Annual RateTier pricingEditable fields for this include:Threshold VolumeUnit PriceThreshold PricingEditable fields for this include:Threshold VolumeUnit PriceCustom Pricing Enable fields for this include:Unit PRICEBase ChargeMinimum ChargeMaximum ChargeThreshold VolumeAnnual Rate |  |  |

#### Edit Bank Fee Conditions

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you edit bank fee conditions.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Cash Manager. |  |  |
| 2 | Access the SAP Fiori App | Open Manage Bank Fee Conditions (F3185). |  |  |
| 3 | Display Conditions | Choose Go. | All conditions are listed. |  |
| 4 | Select a Condition | For a bank fee condition, choose the arrow icon at the right side of the row. | A detailed view of the bank fee condition displays. |  |
| 5 | Edit | Choose Edit. Per your requirements, edit the following fields:Condition DescriptionPricing TypeCondition ItemsThe following fields are for display only:Condition IDLast Changed ByLast Changed On |  |  |
| 6 | Add Selections | Go to the Bank Account and Fee Service Selections tab.Input the selections, for example:Field Name: Bank Accounnt TypeSelection Option: EqualValue: 04Field Name: Service IDSelection Option: EqualValue: 1040Field Name: Company CodeSelection Option: EqualValue: 3310Choose Determine Accounts and Services. | The Bank Account and Services match the conditions are listed in Determined Account and Services tab. |  |
| 7 | Save | Choose Save. |  |  |

#### Delete Bank Fee Conditions

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you delete bank fee conditions.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Cash Manager. |  |  |
| 2 | Access the SAP Fiori App | Open Manage Bank Fee Conditions (F3185). | The Bank Fees Conditions view displays. |  |
| 3 | Display Conditions | Choose Go. | All conditions are listed. |  |
| 4 | Delete | Select the checkbox for a bank fee condition and choose Delete. | The Delete dialog box displays. |  |
| 5 | Confirm Deletion | Choose Delete.Note If the bank fee condition has been assigned to bank fee, it can’t be deleted. | The bank fee condition is deleted. |  |

#### Import Bank Fee Conditions

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you can import bank fee conditions.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Cash Manager. |  |  |
| 2 | Access the SAP Fiori App | Open Manage Bank Fee Conditions (F3185). | The Bank Fees Conditions view displays. |  |
| 3 | Display Conditions | Choose Import. | All conditions are listed. |  |
| 4 | Import Bank Fee Conditions | Select the checkbox for a bank fee condition and choose Import. |  |  |
| 5 | Check Bank Fee Condition Import Log | Navigate to app Schedule Jobs for Bank Fee Condition Update.Choose Go. | All jobs and statuses for the bank fee conditions import are listed.You can select the log icon to view details of failed jobs. Additionally, choose the results icon to preview log details or download results in PDF or Text with Tabs. |  |

#### Maintain Bank Fee Condition Deletion and Downloads

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you delete bank fee conditions.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Cash Manager. |  |  |
| 2 | Access the SAP Fiori App | Open Manage Bank Fee Conditions (F3185). | The Bank Fees Conditions view displays. |  |
| 3 | Display Conditions | Choose Go. | All conditions are listed. |  |
| 4 | Delete Bank Fee Conditions | Select the checkbox for bank fee conditions and choose Delete. | The Delete dialog box displays. |  |
| 5 | Confirm Deletion | Choose Delete.Note If the bank fee condition has been assigned to bank fee, it can’t be deleted. | The Bank Fee Conditions are deleted. |  |
| 6 | Download Bank Fee Conditions | Select the checkbox for bank fee conditions and choose Download Conditions.In the window appears, choose the local path and choose Save. | The Bank Fee Conditions are downloaded. |  |
| 7 | Download Template | Choose Download Template.In the window appears, choose the local path and choose Save. | The Bank Fee Condition template is downloaded. |  |

### Monitor Bank Fees

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you analyze the bank fee reports from different dimensions.

Prerequisite

Previously imported bank fee reports are available, otherwise no data is displayed.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Cash Management Specialist. |  |  |
| 2 | Access the SAP Fiori App | Open Monitor Bank Fees (F3001).Caution If a Display Currency dialog box displays, enter a value, for example, AED. A display currency is a mandatory requirement for performing this activity.Note You can also change the Display Currency manually, as necessary, in Default Values by choosing Settings at the upper left of the view.Remember Ensure that a valid exchange rate between the display currency and the bank account currency is maintained. For more information, see the Maintain Exchange Rate procedure in the Accounting and Financial Close (J58), test script. | The Bank Fees Analysis view displays. |  |
| 3 | Analyze Bank Fee | You can switch the view by choosing Compact Filter or Visual Filter on the upper right of the header section. Analyze the bank fee report from different dimensions, such as, by bank key, by company, by country, and so on. For example, with the Visual Filter, select doughnut chart of Bank Country and choose the AE area. Then, all visual charts update their data based on your selected conditions.On the Bank Fee Analysis section, choose Drill Down to analyze the bank fee from other dimensions, such as Account Level, Account Number, and so on. Switch between Chart View and Table View by selecting the toggle button. It is also possible to change the chart type, category, and series of each option by choosing Settings, then the chart is adapted according to your settings.On the Bank Fee Analysis Table View section, navigate to service details of the bank fee items by choosing the arrow icons.Note Additional display fields are available by choosing and modifying Settings. | The Results List displays. |  |

#### Bank Fees General Check

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you analyze the bank fee reports from different dimensions.

Prerequisite

You must have previously imported bank fee reports. If there are no such reports, no data is displayed.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Cash Management Specialist. |  |  |
| 2 | Access the SAP Fiori App | Open Monitor Bank Fees (F3001). | The Adapt Filters dialog box displays. |  |
| 3 | Browse Filters | At the top right of the dialog box, you see the Visual Filter and Compact Filter buttons.To view a standard list of filters in text format, choose Compact Filter.To view the filters in graphical form, choose Visual Filter.Enter some filter values and choose Go.Note If you exited the dialog box, you can choose Adapt Filters from the Monitor Bank Fees view to get back to it and adapt your filters. | The Monitor Bank Fees screen displays. |  |
| 4 | Browse Views | Slightly down from the top of the screen on the right, you see the Chart View, Table View, and Chart and Table view buttons.Choose the view for your requirements.To add or remove fields from the table and chart views, you can choose the Settings button.Choose Adapt Filters. |  |  |
| 5 | Enter Search Criteria | Make the following entries and choose Go:Display Currency: for example, AEDExchange Rate Date: <current date>Exchange Rate Type: For example, MNote To save the search criteria, on the Monitor Bank Fees view, choose the down-facing arrow next to Standard in the upper left corner of the screen.Remember Ensure that a valid exchange is maintained. For more information, see the Maintain Exchange Rate procedure in the Accounting and Financial Close (J58) test script. |  |  |
| 6 | Navigate Chart View | Select several columns from the Chart View and choose Details. |  |  |
| 7 | Navigate Table View | Drag the scroll bar to view more fields in the Table View.If Bank Service Mapping haven't been done, the fields Payment Transaction Type Group & External Transaction will be empty. The value in fields Billed Service Volume and Calculated Volume will be the same. You go into the detail you will find the value of field Charge Difference in Display Currency is marked as red.For field Billed Service Volume, its source comes from Banks Service Billing File.For field Calculated Volume, its source comes from End of Day Bank Statement.The difference between Billed Service Volume and Calculated Volume will be displayed in field Volume Difference. |  |  |
| 8 | Navigate Object Page | Choose the triangle button on the right to navigate into the detail. | You will find detail information, such as Calculated Service Charge, Bank Service Billing Charges, Bank Service Billing File, Bank Accountant. |  |

#### Assign Validation Condition

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you analyze the bank fee reports by different dimensions.

Procedure

Perform the following steps to change pricing validation status.

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Cash Management Specialist. |  |  |
| 2 | Access the SAP Fiori App | Open Monitor Bank Fees (F3001). | The Adapt Filters dialog box displays. |  |
| 3 | Enter Search Criteria | Make the following entries and choose Go:Display Currency: for example, AEDExchange Rate Date: <A date earlier than the Service Valid-to date>Exchange Rate Type: for example, M.Choose Go.Note To save the search criteria, on the Monitor Bank Fees view, choose the down-facing arrow next to Standard in the upper left corner of the screen.Remember Ensure that a valid exchange is maintained. For more information, see the Maintain Exchange Rate procedure in the Accounting and Financial Close (J58) test script. |  |  |
| 4 | Assign Condition to Service | Select the item with Item Type Service and choose Assign Condition.Note Conditions cannot be assigned to either Tax or Compensation. The Assign Conditon and Overwriter Status buttons are disabled when these item type are selected.Please ensure the condition's valid from date is within the validity date range of the bank fee. | The condition is assigned to selected services. |  |

#### Change Pricing Validation Status

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you analyze the bank fee reports from different dimensions. You change the pricing validation status in the following steps.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Cash Management Specialist. |  |  |
| 2 | Access the SAP Fiori App | Open Monitor Bank Fees (F3001). | The Adapt Filters dialog box displays. |  |
| 3 | Enter Search Criteria | Make the following entries and choose Go:Display Currency: AED.Key Date: <current date>.Exchange Rate Type: For example, M.Note To save the search criteria, on the Monitor Bank Fees view, choose the down-facing arrow next to Standard in the upper left corner of the screen.Remember Ensure that a valid exchange is maintained. For more information, see the Maintain Exchange Rate procedure in the Accounting and Financial Close (J58) test script. |  |  |
| 4 | Change Status | Select a service and choose Overwrite Status. | The Overwrite Status dialog box displays. |  |
| 5 | Change Status | Make the following entries and choose OK:Validation status: <validation status> | The validation status pricing for the selected service is changed. |  |

#### Bank Service Mapping

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you can map the bank service ID with the external transaction type and External Transaction.

Procedure

Bank Service ID is a unique ID to identify the bank service billing file. You can find the service ID from app Monitor Bank Fee after the bank service billing files are imported. External transaction type and External Transaction come from bank statement, you can find it through app Manage Bank Statements after bank statement imported.

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Cash Management Specialist. |  |  |
| 2 | Access the SAP Fiori App | Open Manage Banks - Cash Management (F1574A). |  |  |
| 3 | Enter Search Criteria | Make the following entries and choose Go:Bank Number: for example, 18121976 |  |  |
| 4 | Bank Service Mapping | Choose the bank number you filtered in previous step.Choose Edit.Choose Bank Service Mapping tab.Choose Create.Make the following entries and choose Save.Service ID: for example, 1043Transaction Type: for example, CAMT053External Transaction: for example, PMNTRCHQCCHQ |  |  |

### Manage Interest Condition

In this section, you can set up interest conditions, calculate interest by scheduling jobs, and monitor the interest on your bank account.

#### Create Interest Condition

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you can create interest condition.

Prerequisite

Perform the preliminary step [Define Authorization Group for Interest Condition](#unique_7) [page ] 6, if you want to restrict access to different bank account interest conditions by users.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Cash Management Specialist. |  |  |
| 2 | Access the SAP Fiori App | Open Manage Bank Account Interest Conditions (F9017). |  |  |
| 3 | Create Conditions | Choose Create. |  |  |
| 4 | Enter Data | Make the following entries and choose Save.ID: BAIC01Valid From: Current DateBalance Type: Closing Available Balance (EoD)Authorization Group: ZAGFIRDescription: Bank Account Interest ConditionInterest Calculation Method: ACT/365Rounding: Round to the NearestCurrency: AEDDebit Interest Percentage Rate (%): 2Credit Interest Percentage Rate (%): 3Quick Set Up: Manual InputCalculation Frequency / Unit: 1 MonthsCalculation Date: Current DateDue Date: Current Date + 6 MonthsSelection Group: 1Selection Field: Company CodeSelection Option: EqualValue: 3310On the Assigned Bank Account tab, choose Retrieve Bank Accounts. | The updated interest condition display. |  |

#### Bank Account Interest Calculation

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you can calculate the bank account interest.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Cash Management Specialist. |  |  |
| 2 | Access the SAP Fiori App | Open Schedule Jobs for Bank Account Interest Calculation (F9016). |  |  |
| 3 | Template Selection | Choose Create.Make the following entries and choose Step 2:Job Template: Bank Account Interest CalculationJob Name: Bank Account Interest Calculation |  |  |
| 4 | Scheduling Options | Start Immediately: <Select the check box>Choose Step 3. | The updated interest condition display. |  |
| 5 | Input Parameters | Make the following entries:Company Code: 3310Due Date From: <10 Months before current date>Due Date To: <Current date> |  |  |
| 6 | Schedule Job | Choose Schedule. |  |  |

#### Monitor Bank Account Interests

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you can monitor the bank account interest.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Cash Management Specialist. |  |  |
| 2 | Access the SAP Fiori App | Open Monitor Bank Account Interests (F9015). |  |  |
| 3 | Enter Filter Data | Make the following entries and choose Go:Display Currency: AEDExchange Rate Type: MExchange Rate Date: <Today> |  |  |
| 4 | Navigate to Details | Choose the triangle button on the right of one Bank Account from Bank Account Interest. | Navigate to the detailed bank account interest page. |  |

## Appendix

### Field Mapping - Monitor Bank Frees to XML Category

| Field Name in "Monitor Bank Fees" table view | Category in XML File |
| --- | --- |
| Sender ID | BllgStmtGrp/Sndr/Id/FIId/BICFI orBllgStmtGrp/Sndr/Id/FIId/Othr/Id orBllgStmtGrp/Sndr/Id/OrgId/AnyBIC orBllgStmtGrp/Sndr/Id/OrgId/Othr/Id |
| Bank Key | Bank Key of the account |
| Receiver ID | BllgStmtGrp/Rcvr/Id/OrgId/AnyBIC |
| Report ID | Generated when importing the report |
| Company Code | System data |
| Account Number | BllgStmtGrp/Rcvr/Id/FIId/BICFI orBllgStmtGrp/Rcvr/Id/FIId/Othr/Id orBllgStmtGrp/Rcvr/Id/OrgId/AnyBIC orBllgStmtGrp/Rcvr/Id/OrgId/Othr/Id |
| Account Level | BllgStmtGrp/BllgStmt/AcctChrtcs/AcctLvl |
| IBAN | IBAN in the account |
| Service Total | IfBllgStmtGrp/BllgStmt/Compstn/Tp/Cd = ‘SCBT’ThenBllgStmtGrp/BllgStmt/Compstn/Val/Amt = Service TotalElse IfBllgStmtGrp/BllgStmt/Compstn/Tp/Cd = ‘SCCP’ThenBllgStmtGrp/BllgStmt/Compstn/Val/Amt = Service TotalElseService Total= Total Amount – Total Tax |
| Tax Total | IfBllgStmtGrp/BllgStmt/Compstn/Tp/Cd = ‘TXTS’ThenBllgStmtGrp/BllgStmt/Compstn/Val/Amt = Tax Total |
| Total Amount in Settlement Currency | IfBllgStmtGrp/BllgStmt/Compstn/Tp/Cd = ‘CTND’ThenBllgStmtGrp/BllgStmt/Compstn/Val/Amt = Total Amount in Settlement CurrencyElse IfBllgStmtGrp/BllgStmt/Compstn/Tp/Cd = ‘SCDB’ThenBllgStmtGrp/BllgStmt/Compstn/Val/Amt = Total Amount in Settlement CurrencyElseTotal Amount in Settlement Currency = Service Total + Tax Total |
| Total Amount in Display Currency | Convert Total Amount in Settlement Currency into the amount in display currency |

### Field Mapping - Service Details to XML Category

| Field Name in Service Details table view | Category in XML File |
| --- | --- |
| Service ID | BllgStmtGrp/BllgStmt/Svc/SvcDtl/BkSvc/Id |
| Subservice Code | BllgStmtGrp/BllgStmt/Svc/SvcDtl/BkSvc/SubSvc/Issr/Cd or BllgStmt-Grp/BllgStmt/Svc/SvcDtl/BkSvc/SubSvc/Issr/Prtry |
| Subservice ID | BllgStmtGrp/BllgStmt/Svc/SvcDtl/BkSvc/SubSvc/Id |
| Volume | BllgStmtGrp/BllgStmt/Svc/SvcDtl/Vol |
| Unit Price | BllgStmtGrp/BllgStmt/Svc/Pric/UnitPric/Amt and BllgStmtGrp/BllgStmt/Svc/Pric/UnitPric/Sgn |
| Service total | BllgStmtGrp/BllgStmt/Svc/OrgnlChrgPric/Amt |
| Tax Total | Method A: BllgStmt/Svc/TaxClctn/MtdA/SvcTax/HstAmt/AmtMethod B: BllgStmt/Svc/TaxClctn/MtdB/SvcTax/HstAmt/AmtMethod C: BllgStmtGrp/BllgStmt/Compstn/Tp/Cd = ‘TXTS’BllgStmtGrp/BllgStmt/Compstn/Val/Amt = Tax TotalMethod D: BllgStmt/Svc/TaxClctn/MtdD/SvcTaxPricAmt/Amt |
| Payment Method | BllgStmtGrp/BllgStmt/Svc/PmtMtd |
| Tax Designation code | BllgStmtGrp/BllgStmt/Svc/TaxDsgnt/Cd |

Method A/B/C/D: BllgStmtGrp/BllgStmt/AcctChrtcs/Tax/ClctnMtd/

### Field Value Descriptions

1. Status (BllgStmtGrp/BllgStmt/Sts)

| Status | Description |
| --- | --- |
| ORGN Original | The statement uniquely identified by the Account Level, Account Number, Statement Start Date, and Statement End Date is the original statement. |
| RPLC Replace | This statement replaces a previously transmitted statement. The statement to be replaced is identified by the Account Level, Account Number, and Statement End Date. |
| TEST Test | This is a test statement and does not represent real events. |

1. Account level (BllgStmtGrp/BllgStmt/AcctChrtcs/AcctLvl)

| Account Level | Description |
| --- | --- |
| DETL Detail | The account is a real deposit/current account. It is either not a member of a hierarchy or it is at the lowest level in a hierarchy. If the account is a member of a hierarchy, the Parent Qualifier and Parent Account Number elements are required. |
| INTM Intermediate | The account exists at an intermediate level within a hierarchy. It can be a real deposit/current account or a fictitious account used exclusively to total information from lower levels in the hierarchy. Intermediate level accounts require the Parent Level and Parent Account Number elements. |
| SMRY Summary | The account is at the highest level in a hierarchy. It can be a real deposit account or a fictitious account used exclusively to total information from lower levels in the hierarchy. The Parent Level and Parent Account Number elements must not be present. |

1. Compensation method (BllgStmtGrp/BllgStmt/AcctChrtcs/CompstnMtd)

| Compensation Method | Description |
| --- | --- |
| NOCP No | The account does not pay any charges due. Some other account in the hierarchy is debited or invoiced for charges and taxes due. |
| DBTD Debited | This account was debited for any charges or taxes due |
| INVD Invoiced | The account or summary was invoiced for charges and taxes due |
| DDBT DelayedDebit |  |

1. Tax calculation method (BllgStmtGrp/BllgStmt/AcctChrtcs/Tax/ClctnMtd)

| Tax Calculation Method | Description |
| --- | --- |
| NTAX NoTaxes | No taxes are calculated or due on this statement. There is no Tax Section. |
| MTDA BSBMethodA | Line-by-line per service calculation and settlement currency translation. |
| MTDB BSBMethodB | Line by line per service calculation with settlement currency translation performed on the statement tax total. |
| MTDC BSBMethodC | Group tax calculation with group settlement currency translation. |
| MTDD BSBMethodD | Line-by-line per service calculation with all charges and taxes in the Pricing currency. |
| UDFD Undefined | The tax calculation method is not identified. |

1. Payment method (BllgStmtGrp/BllgStmt/Svc/PmtMtd)

| Payment Method | Description |
| --- | --- |
| BCMP BalanceCompensable | This code is used in the USA and allows the bank to offset a service charge with interest earned on the deposit account balance. The actual charges arising from Balance Compensable services are always calculated and charged at month end. |
| FLAT HardCharge | The charge is not balance compensable and is due. In the absence of balance compensable charges in Europe, this would be the most commonly used code for services that are billed at month end. |
| PVCH PreviouslyCharged | The charge was previously assessed and is not part of the amount due as of this statement. This code is used for charges that were debited as the chargeable event took place. |
| INVS InvoicedSeparately | The charge was previously invoiced and is not part of the amount due as of this statement. This code is used for charges that were invoiced as the chargeable event took place. |
| WVED Waived | The charge is waived and not due. The waived amount must be placed in Original Charge. |
| FREE Free | The service is free, no charge, to the customer. |

1. Tax designation code (BllgStmtGrp/BllgStmt/Svc/TaxDsgnt/Cd)

| Tax Designation Code | Description |
| --- | --- |
| XMPT Exempt | No taxes are due. This service is not repeated in the TaxRegion section. |
| ZERO Zero Rated | The tax is due but at zero percent and a zero charge. This service is not repeated in the TaxRegion section. |
| TAXE Taxable | One or more taxes are due on this service. The basic elements of this service are repeated in the TaxRegion Section if the account tax calculation method is "C". |

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
- see-also :: [[05-treasury-and-cash-management/test-script-advanced-bank-statement-automation-4x8-1056]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/2O0_S4CLD2608_BPD_EN_AE.docx` — full document · extracted with `mammoth` · 59,194 chars in the whole document
