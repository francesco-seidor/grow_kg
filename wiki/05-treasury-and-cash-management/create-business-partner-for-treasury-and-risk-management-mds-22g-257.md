---
id: 05-treasury-and-cash-management/create-business-partner-for-treasury-and-risk-management-mds-22g-257
title: Create Business Partner for Treasury and Risk Management - MDS (22G) (22G_S4CLD2608_Master_Data_EN_XX)
description: "SAP S/4HANA Cloud Public Edition master data script (22G): manual test steps to create treasury business partners, roles, payment, correspondence data."
cluster: 05-treasury-and-cash-management
tags: [kb/treasury-and-cash-management, topic/treasury-business-partners]
aliases: [22G_S4CLD2608_Master_Data_EN_XX]
keywords: [Business Partners for Treasury and Risk Management, treasury business partner, business partner general data, payment details, business partner authorizations, treasury correspondence, securities partner roles, derived flows, company code reporting data, letter of credit bank role]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/22G_S4CLD2608_Master_Data_EN_XX.docx]
confidence: high
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-257
topic: 05-treasury-and-cash-management/treasury-business-partners
language: EN
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Create Business Partner for Treasury and Risk Management - MDS (22G) (22G_S4CLD2608_Master_Data_EN_XX)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/22G_S4CLD2608_Master_Data_EN_XX.docx`, extracted with `mammoth`. Grouped under **Business Partners for Treasury and Risk Management** in Treasury and Cash Management. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

|  |  |
| --- | --- |
| <!-- image omitted: unnamed --> | Master Data ScriptSAP S/4HANA Cloud Public Edition - 02-07-26 |
|  | Create Business Partner for Treasury and Risk Management - MDS (22G) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Table of Contents

[1 Purpose 3](#_Toc233904538)

[2 Prerequisites 4](#_Toc233904539)

[2.1 System Access 4](#_Toc233904540)

[2.2 Roles 4](#_Toc233904541)

[2.3 Master Data, Organizational Data, and Other Data 5](#_Toc233904542)

[3 Overview Table 6](#_Toc233904543)

[4 Test Procedures 8](#_Toc233904544)

[4.1 Maintain General Data for Business Partner 8](#_Toc233904545)

[4.2 Maintain Company Code Data for Business Partner 10](#_Toc233904546)

[4.2.1 Maintain Payment Details for Business Partner 10](#_Toc233904547)

[4.2.2 Maintain Authorizations for Business Partner 13](#_Toc233904548)

[4.2.3 Maintain Derived Flows for Business Partner (Optional) 14](#_Toc233904549)

[4.2.4 Maintain Reporting Data in Company Code for Business Partner 16](#_Toc233904550)

[4.3 Maintain Correspondence Data for Business Partner 17](#_Toc233904551)

[4.3.1 Maintain Profile and BP Group Assignments to External Recipient 18](#_Toc233904552)

[4.3.2 Maintain Profile and BP Group Assignments to Internal Recipient 21](#_Toc233904553)

[4.4 Maintain Business Partner Master Data for Securities 25](#_Toc233904554)

[4.4.1 Create Issuer Role for Business Partner 26](#_Toc233904555)

[4.4.2 Create Depository Bank Role for Business Partner 27](#_Toc233904556)

[4.5 Maintain Business Partner Master Data for Letter of Credit 28](#_Toc233904557)

[4.5.1 Create Bank Role for Business Partner 28](#_Toc233904558)

## Purpose

This building block provides the basic manual steps to create Business Partners for Treasury and Risk Management.

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
| Treasury Specialist - Back Office | SAP_BR_TREASURY_SPECIALIST_BOE | Treasury Back Office | SAP_BR_TREASURY_SPECIALIST_BOE |  |
| Master Data Specialist - Business Partner Data | SAP_BR_BUPA_MASTER_SPECIALIST | Master Data - Business Partners / Business Partner Governance / Business Partner Governance / Business Partner Governance | SAP_BR_BUPA_MASTER_SPECIALIST / SAP_CA_SPT_MDG_BP_GOV_PC / SAP_CMD_SPT_BP_GOV_PC / SAP_CA_SPT_MDG_BP_WFUSR_PC |  |
| Configuration Expert - Business Process Configuration | SAP_BR_BPC_EXPERT | Business Process Configuration / Business Process Configuration - Finance / Business Process Configuration - Procurement / Manage your Solution / Business Process Configuration - Workflow / Business Configuration - Feature Management / Business Process Configuration - Extensibility Explorer / Business Configuration - Transportation | SAP_BR_BPC_EXPERT / SAP_FIN_SPT_BPC_EXPERT_PC / SAP_MM_SPT_BIZ_PROC_CONFIGN_PC / SAP_CA_SPT_IC_LND_BASE_PC / SAP_CA_SPT_BPC_WORKFLOW_PC / SAP_CA_SPT_BPC_FM_PC / SAP_EI_SPT_BPC_EXT_PC / SAP_TM_SPT_TRANSPCFG_PC |  |

### Master Data, Organizational Data, and Other Data

The organizational structure and master data of your company has been created in your system during activation. The organizational structure reflects the structure of your company. The master data represents materials, customers, and vendors, for example, depending on the operational focus of your company.

Use your own master data to go through the test procedure. If you have installed an SAP Best Practices baseline package, you can use the following baseline package sample data.

|  |
| --- |
| Caution Sample values for master data values are country/region-specific and the values provided in the following table are for Germany. Substitute the country/region-specific values provided by SAP Best Practices for SAP S/4HANA Cloud Public Edition or use master data values you have created for this purpose. |

| Data | Sample Value | Details | Comments |
| --- | --- | --- | --- |
| COMPANY CODE | For example, 1010 |  |  |
| CURRENCY | For example, EUR |  |  |
| FOREIGN CURRENCY 1 | For example,USD |  |  |
| HOUSE BANK | For example,DEBK1 |  |  |
| HOUSE BANK ACCOUNT ID 1 | For example, DEAC1 |  |  |
| HOUSE BANK ACCOUNT ID 2 | For example,USAC2 |  |  |
| BUSINESS PARTNER | 10537001 |  |  |

## Overview Table

Create Business Partner for Treasury and Risk Management - MDS (22G) consists of several process steps provided in the following tables:

|  |
| --- |
| Note If your system administrator has enabled spaces and pages on the SAP Fiori launchpad, the homepage will only contain the essential apps for performing the typical tasks of a business role.You can find all other (searchable) apps not included on the homepage using the search bar ([2434549](https://me.sap.com/notes/2434549)).If you want to personalize the homepage and include the hidden apps, navigate to your user profile and choose App Finder. |

Table 1: Maintain Data for Normal Business Partner

| Process Step, Report or Item | Business Role | Transaction/APP | Expected Results |
| --- | --- | --- | --- |
| [Maintain General Data for Business Partner](#unique_7) [page ] 8 | Master Data Specialist - Business Partner Data | Maintain Business Partner (BP) | The general data for the business partner is maintained. |
| Maintain Company Code Data for Business Partner |  |  |  |
| [Maintain Payment Details for Business Partner](#unique_8) [page ] 10 | Master Data Specialist - Business Partner Data | Maintain Business Partner (BP) | The payment details data for the business partner is maintained. |
| [Maintain Authorizations for Business Partner](#unique_9) [page ] 13 | Master Data Specialist - Business Partner Data | Maintain Business Partner (BP) | The authorizations data for the business partner is maintained. |
| [Maintain Derived Flows for Business Partner (Optional)](#unique_10) [page ] 14 | Master Data Specialist - Business Partner Data | Maintain Business Partner (BP) | The derived flows data for the business partner is maintained. |
| [Maintain Reporting Data in Company Code for Business Partner](#unique_11) [page ] 16 | Master Data Specialist - Business Partner Data | Maintain Business Partner (BP) | The reporting data for the business partner is maintained. |
| Maintain Correspondence Data for Business Partners |  |  |  |
| [Maintain Profile and BP Group Assignments to External Recipient](#unique_12) [page ] 18 | Master Data Specialist - Business Partner Data | Assign Profile and BP Group - External Recipients (FTR_EXT_ASSIGN) | BP profiles and BP groups are maintained for the external recipient. |
| [Maintain Profile and BP Group Assignments to Internal Recipient](#unique_13) [page ] 21 | Master Data Specialist - Business Partner Data | Assign Profile and BP Group - Internal Recipients (FTR_INT_ASSIGN) | BP profiles and BP groups and user IDs are maintained for the internal recipient. |
| Maintain Business Partner Master Data for Securities |  |  |  |
| [Create Issuer Role for Business Partner](#unique_14) [page ] 26 | Master Data Specialist - Business Partner Data | Maintain Business Partner (BP) | Role Issuer is created. |
| [Create Depository Bank Role for Business Partner](#unique_15) [page ] 27 | Master Data Specialist - Business Partner Data | Maintain Business Partner (BP) | Role Depository Bank is created. |
| Maintain Business Partner Master Data for Letter of Credit |  |  |  |
| [Create Bank Role for Business Partner](#unique_16) [page ] 28 | Master Data Specialist - Business Partner Data | Maintain Business Partner (BP) | Role Bank is created. |

## Test Procedures

This section describes test procedures for each process step that belongs to this scope item.

### Maintain General Data for Business Partner

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This section describes the process of maintaining general data for business partner.

|  |
| --- |
| Remember Sample values for master data values are country/region-specific and the values provided in the following table are for Gemany. Substitute the country/region-specific values provided by SAP Best Practices for SAP S/4HANA Cloud Public Edition or use master data values you have created for this purpose. |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Master Data Specialist - Business Partner Data. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Maintain Business Partner (BP). | The app opens. |  |
| 3 | Enter Data on Initial Screen | On the Maintain Business Partner screen, choose Organization. | The Create Organization screen displays. |  |
| 4 | Enter Address Data | On the Create Organization screen, enter the following data:Business Partner: For example, 10537001.Grouping: Select TR02 Treasury partner (external).Create in BP role: Select 000000 Business Partner (Gen.).Title: Select 0003 Company.Name: For example, Bank 1 – SAMPLE BANK.Salutation: For example, Bank 1.Search Term 1/2: For example, Bank 1.Street/House number: <Street address>Postal Code/City: <Postal code and city>Country/Reg.: Select <Country/Region code>.Language: Select <Language code>.E-Mail: <E-mail address>Address Valid From: For example, <Current date in the previous year>.Address Valid To: For example, Dec 31 of the year 9999.Choose Save.Note Stay on the screen for the subsequent steps.Note If you only see Business Partner (Gen.) without the key 000000, then you may go to Menu > Settings - Interaction Design > Visualization > Dropdown List > Show dropdown lists with keys and turn it on. | The Business Partner is created successfully. |  |
| 5 | Switch to Change Mode | On the Display Organization: 10537001 screen, choose Switch Between Display and Change and enter the following data:Change in BP role: Select TR0151 Counterparty. | More counterparty related tabs such as Legal Data and Rating display. |  |
| 6 | Enter Legal Data | On the Change Organization: 10537001 , new role Counterparty screen, choose Navigation Menu.Note The Navigation Menu is on the very right side of the screen. It displays as …, which is right next to the > symbol.From the dropdown list, choose Legal Data and enter the following data:Country/Region: For example, select DE.Choose Save.Note Stay on the screen for the subsequent steps. | The Legal Data is entered and saved.The Change Organization: 10537001, new role Counterparty screen displays. |  |
| 7 | Enter Payment Transaction Data | On the Change Organization: 10537001, role Counterparty screen, choose Navigation Menu.From the dropdown list, choose Payment Transactions and enter the following data for two rows:Row 1:ID: Currency Code + 1, for example, EUR1.C/R: <Country/Region code>Bank Key: <Bank key>Bank Account: <Bank account>IBAN: Choose IBAN and choose Continue in the IBAN dialog box.Row 2:ID: Foreign Currency Code + 1, for example, USD1.C/R: <Country/Region code>Bank Key: <Bank key>Bank account: <Bank account>IBAN: Choose IBAN and choose Continue in the IBAN dialog box.Choose Save.Note If an Information dialog box displays when you choose IBAN, choose Continue.Note IBAN is mainly used in EU countries. For US, please skip the IBAN-related steps. | The Payment Transaction data is entered and the Business Partner is saved. |  |

### Maintain Company Code Data for Business Partner

#### Maintain Payment Details for Business Partner

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This section describes the steps for maintaining payment details data for a business partner.

|  |
| --- |
| Remember Sample values for master data values are country/region-specific and the values provided in the following table are for Germany. Substitute the country/region-specific values provided by SAP Best Practices for SAP S/4HANA Cloud Public Edition or use master data values you have created for this purpose. |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Master Data Specialist - Business Partner Data. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Maintain Business Partner (BP). | The Maintain Business Partner screen displays. |  |
| 3 | Switch to Change Mode | On the Maintain Business Partner screen, choose Open BP. In the dialog box, enter following data:Business Partner: 10537001Choose Enter.Choose Switch Between Display and Change, and enter following data:Change in BP Role: select TR0151 Counterparty | The Change Organization: 10537001, role Counterparty screen displays. |  |
| 4 | Enter SI: Payment Details Data | On Change Organization: 10537001 , role Counterparty, choose Company code, and enter following data:Company code: for example, 1010Choose ENTER and choose SI: Payment Details to enter the following four rows of data:Row 1Currency: for example, EURPay.Det.ID: for example, EURIHouse Bank: for example, DEBK1Account ID: for example, DEAC1Payer/ee: for example, leave blankPartner Bank: for example, leave blankPayment request: for example, DeselectPayment methods: for example, leave blankRow 2Currency: for example, EURPay.Det.ID: for example, EUROHouse Bank: for example, DEBK1Account ID: for example, DEAC1Payer/ee: for example, 10537001Partner Bank: for example, EUR1Payment request: for example, selectPayment methods: for example, TRow 3Currency: for example, USDPay.Det.ID: for example, USDIHouse Bank: for example, DEBK1Account ID: for example, USDACPayer/ee: for example, leave blankPartner Bank: for example, leave blankPayment request: for example, DeselectPayment methods: for example, leave blankRow 4Currency: for example, USDPay.Det.ID: for example, USDOHouse Bank: for example, DEBK1Account ID: for example, USDACPayer/ee: for example, 10537001Partner Bank: for example, USD1Payment request: for example, SelectPayment methods: for example, FNote Stay on this screen for subsequent steps.Note Make sure you enter the payment method into the field Payment Methods instead of field Payment Method.Note If a warning window displays with the following message: Business partner proposed as payer/payee (see long text)Display this message for this business partner again?Choose No. | The SI: Payment Details data is entered. |  |
| 5 | Assign Payment Details | From the screen of the previous step, assign payment details. For example, for EUR, select the EUR EURI row.Choose Assign, in the Counterparty Change: Payment Details Assignment dialog box.Choose Select All Incoming. The result is that EURI displays under PmntID-Inc.Choose Continue to close the dialog box.Select the EUR EURO row.Choose Assign, in the Counterparty Change: Payment Details Assignment dialog box.Choose Select All Outgoing. The result is that EURO displays under P-ID Outg.Choose Continue to close the dialog box.Repeat the step for USD:USDI: PmntID-IncUSDO: P-ID Outg.On the Change Organization: 10537001, role Counterparty screen, choose Save. | Payment details and the assignments are saved. |  |

#### Maintain Authorizations for Business Partner

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This section describes the steps for maintaining the authorization data for a business partner for SAP Treasury and Risk Management.

|  |
| --- |
| Remember Sample values for master data values are country/region-specific and the values provided in the following table are for Germany. Substitute the country/region-specific values provided by SAP Best Practices for SAP S/4HANA Cloud Public Edition or use master data values you have created for this purpose. |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log onto the SAP Fiori launchpad as a Master Data Specialist - Business Partner Data. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Maintain Business Partner (BP). | The Maintain Business Partner screen displays. |  |
| 3 | Switch to Change Mode | On the Maintain Business Partner screen, choose Open BP. In the dialog box, enter following data:Business Partner: 10537001Choose Enter.Choose Switch Between Display and Change, and enter the following data:Change in BP Role: select TR0151 Counterparty | The Change Organization: 10537001 , role Counterparty screen displays. |  |
| 4 | Enter SI: Authorizations Data | On the Change Organization: 10537001 , role Counterparty screen, choose Company Code, choose SI: Authorizations.Select the Auth. checkbox for all of the entries and choose Save.Note You can also give authorization to a specific product type and transaction type by expanding the folders. For testing purpose, we provide all authorizations to all kinds of product types and transaction types. | The authorizations data is saved. |  |

#### Maintain Derived Flows for Business Partner (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This section describes the steps for maintaining Derived Flow data for a business partner. Some countries tax interest rate income is what creates a special kind of tax you must include for a business partner. In this procedure, you set any country/region-specific interest income tax for Product type and Transaction type. This step is optional.

|  |
| --- |
| Remember Sample values for master data values are country/region-specific and the values provided in the following table are for Gemany. Substitute the country/region-specific values provided by SAP Best Practices for SAP S/4HANA Cloud Public Edition or use master data values you have created for this purpose. |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Master Data Specialist - Business Partner Data. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Maintain Business Partner (BP). | The app opens. |  |
| 3 | Switch to Change Mode | On the Maintain Business Partner screen, choose Open BP. In the dialog box, enter the following data:Business Partner: 10537001Press Enter.Choose Switch Between Display and Change and enter the following data:Change in BP Role: Select TR0151 Counterparty. | The Change Organization: 10537001 , role Counterparty screen displays. |  |
| 4 | Enter SI: Derived Flows Data | On the Change Organization: 10537001 , role Counterparty screen, choose Company Code, choose SI: Derived Flows, and expand: Money Market > Interest rate instrument > 51A Fixed-Term Deposit/Borrowing > 100 Investment .ChooseSelect/Deselect Incoming line.In the Procedure to Generate Derived Flows 1 Entry dialog box, choose INTDE.Choose OK.The results are what the INTDE displays in the Procedure column.Choose Save. | The Derived Flows data is entered and saved. |  |
| 5 | Repeat for Additional Product and Transaction Types | Repeat the previous step for each of the following product types and transaction types:Product Type.…..Transaction Type52B.…..10053A.…..10053A.…..10153A.…..10254A.…..10055A.…..10058A.…..300Tip The locations of the product types are as follows:52B is under Money Market > Deposit at notice.53A is under Money Market > Commercial Paper.54A is under Money Market > Cash flow transaction.55A is under Money Market > Interest rate instructment.58A is under Money Market > Current Acct-Style Instrument. |  |  |

#### Maintain Reporting Data in Company Code for Business Partner

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This section describes the steps for maintaining company relationship for a business partner.

|  |
| --- |
| Remember Sample values for master data values are country/region-specific and the values provided in the following table are for Germany. Substitute the country/region-specific values provided by SAP Best Practices for SAP S/4HANA Cloud Public Edition or use master data values you have created for this purpose. |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log onto the SAP Fiori launchpad as a Master Data Specialist - Business Partner Data. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Maintain Business Partner (BP). | The Maintain Business Partner screen displays. |  |
| 3 | Switch to Change Mode | On the Maintain Business Partner screen, choose Open BP. In the dialog box, enter following data:Business Partner: 10537001Choose Enter.Choose Switch Between Display and Change, and enter following data:Change in BP Role: choose TR0151 Counterparty | The Change Organization: 10537001 , role Counterparty screen displays. |  |
| 4 | Enter Reporting Data in Company Code | On the Change Organization: 10537001 , role Counterparty screen, choose Company Code, choose Reporting Data in Company Code,Note If you don't see Reporting Data in Company Code on the screen, then choose Navigation Menu and select from the dropdown menu.Enter following data,Comp. Rel.: for example, 3 OtherChoose Save.Note Comp.Rel. reflects your relationship to the counterparty:1 affiliated and consolidated2 affiliated but not consolidated3 unaffiliated4 Do not use itThese are used to derive the correct G/L accounts. | The reporting data is entered and saved. |  |

### Maintain Correspondence Data for Business Partner

SAP Treasury Risk Management provides standard correspondence functionality. With this correspondence functionality, whenever a treasury risk management transaction is saved, the system either sends an e-mail to the business partner or automatically prints out a form to the designated print machine.

To use this correspondence functionality, the following data needs to be assigned to a business partner:

- Business Partner Profile
- Business Partner group

#### Maintain Profile and BP Group Assignments to External Recipient

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This procedure describes assigning business partner profiles and BP groups to an external business partner.

Business partner profiles and business partner groups controls the correspondence activities in SAP Treasury Risk Management.

The following predefined business partner profiles are provided:

- PR_EMAIL
- PR_PRINT

These predefined business partner profiles can be assigned to your business partner. For example, if the communication with your business partner is by e-mail, then you assign PR_EMAIL to the business partner. If the communication is by sending a printed document, then you assign PR_PRINT to the business partner.

The following business partner group has been predefined:

- BPG_DEFAULT

You assign this business partner group to your business partner or use Configuration Steps Define Business Partner Group and Assign Attributes for Business Partner Groups to add your own business partner group and then assign appropriate attributes according to your specific requirements. Different business partner profiles and BP groups can be assigned to the same business partner.

|  |
| --- |
| Remember Sample values for master data values are country/region-specific and the values provided in the following table are for Germany. Substitute the country/region-specific values provided by SAP Best Practices for SAP S/4HANA Cloud Public Edition or use master data values you have created for this purpose. |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log onto the SAP Fiori launchpad as a Treasury Specialist - Back Office. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Assign Profile and BP Group - External Recipients (FTR_EXT_ASSIGN). | The Assign Profile and BP Groups to External Recipients screen displays. |  |
| 3 | Enter Business Partner Data | On the left side of Assign Profile and BP Groups to External Recipients screen, choose Insert Row and enter the following data,BusPartner: for example, 10537001CoCd: for example, 1010Recpt/Send Type: for example, select the COUNTERPARTY row,Press Enter. | The business partner information is entered. |  |
| 4 | Assign Business Profile and BP Group to the Business Partner | On the upper right part of the Assignment of Profiles and BP Groups to External Recipients screen, choose Expand Node and expand:BP:0010537001 /CoCd: 1010 / Rec/SendType: COUNTERPARTY > Money Market > Interest rate instrument > 51A Fixed-Term Deposit/Borrowing > 100 Investment .Select 10 Contract.On the lower right of the Assignment of Profiles and BP Groups to External Recipients screen, choose Insert Row and either add the e-mail or the print profile:Note Typically, only only one Profile is assigned to a Product type/Transaction type/Activity Category. If both profiles are to be assigned, then after you complete the first profile, choose Insert Row again to add the other profile.Either when the profile is e-mail:Profile: for example, PR_EMAILBP Group: for example, BPG_DEFAULTChoose Save.Or when the profile is print:Profile: for example, PR_PRINTBP Group: for example, BPG_DEFAULTChoose Save. | Business partner profiles and BP groups are assigned for the Product type/Transaction type/Activity category. |  |
| 5 | Repeat for Additional Product Type/Transaction Type/Activity Category | Choose Modify Row on the upper left part of the screen and repeat the previous step to assign BP profiles and BP groups for the following product types and transactions:Product TypeTransaction TypeAct. Category51A1001051A2001052B1001052B1001153A1001053A1011053A1021053A2001053A2011053A2021054A1001054A2001055A1001055A2001055A1001155A2001156A1001056A2001058A3001058A3001160A1012060A1022060A1032060A1042060A1052060A1072060B1032060B1035560B1042060B1045560B1052060B1055560B1102060B1105562A3002062A3012062A3022062B3002062B3012062B3022076A1002076A20020 | For all the listed Product Types/Transaction Types/ Activity Categories, BP profiles and BP groups are assigned. |  |

#### Maintain Profile and BP Group Assignments to Internal Recipient

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

Internal Recipient ID is predefined by SAP. It could be linked to SAP User ID(s). Once it's linked to an SAP user ID, whenever an internal correspondence object is generated, SAP TRM will try to send correspondence information to the address of the SAP User ID. Depending on the different profiles (PR_EMAIL /PR_PRINT), Email could be sent to the user's email address, or a form is printout.

This step describes how to assign Business partner profiles and BP groups to an internal business partner.

|  |
| --- |
| Remember Sample values for master data values are country/region-specific and the values provided in the following table are for Germany. Substitute the country/region-specific values provided by SAP Best Practices for SAP S/4HANA Cloud Public Edition or use master data values you have created for this purpose. |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log onto the SAP Fiori launchpad as a Treasury Specialist - Back Office. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Assign Profile and BP Group - Internal Recipients (FTR_INT_ASSIGN). | The Assignment of Profiles and BP Groups to Internal Recipients screen displays. |  |
| 3 | Enter Business Partner Data | On the left side of the Assignment of Profiles and BP Groups to Internal Recipients screen, choose Insert Row and enter the following data,Remember Sample values for master data values are country/region-specific and the following example values are for Germany. Substitute your country/region-specific values provided by SAP Best Practices for SAP S/4HANA Cloud Public Edition or use master data values you have created for this purpose.IntRec: for example, INT.RECPCoCd: for example, 1010Recpt/Send Type: for example, select the INTERNAL checkbox.Press Enter. | The business partner information is entered. |  |
| 4 | Assign Business Profile and BP Group to the Business Partner | On the upper right side of theAssignment of Profiles and BP Groups to Internal Recipients screen, expand:BP:INT. RECP /CoCd: 1010 / Rec/SendType: INTERNAL > Money Market > Interest rate instrument > 51A Fixed-Term Deposit/Borrowing > 100 Investment .Select 10 Contract.On the lower right part of the Assignment of Profiles and BP Groups to Internal Recipients screen, choose Insert Row.Enter the profile information for either e-mail or print:Profile: for example for e-mail, PR_EMAILBP Group: for example, BPG_DEFAULTUser Name: select a <User ID>.Choose Save.Choose Insert Row again and add another entry for print:Profile: for example, for print option, PR_PRINTBP Group: for example, BPG_DEFAULTUser Name: select a <User ID>.Note The <User ID> is a backend user ID.Choose Save. | Business partner profile and BP group and user ID are assigned for the Product type/Transaction type/Activity category. |  |
| 5 | Repeat for Additional Product Type/Transaction Type/Activity Category | Choose Modify Row on the upper left part of the screen and repeat the previous step to assign BP profiles and BP groups for the following product types and transactions:Product TypeTransaction TypeAct. Category51A1001051A2001052B1001052B1001153A1001053A1011053A1021053A2001053A2011053A2021054A1001054A2001055A1001055A2001055A1001155A2001156A1001056A2001058A3001058A3001160A1012060A1015560A1022060A1025560A1032060A1035560A1042060A1045560A1052060A1055560A1072060A1075560B1032060B1035560B1042060B1045560B1052060B1055560B1102060B1105562A3002062A3012062A3022062B3002062B3012062B3022076A1002076A20020 | BP profiles, BP groups, and user IDs are assigned to all the listed Product Types/Transaction Types/ Activity Categories. |  |

### Maintain Business Partner Master Data for Securities

Purpose

For securities related financial instruments, for example, Money Market Fund, to record the basic information of the issuer and Depository Bank, create the following business partner roles:

- TR0150 Issuer
- TR0152 Depository Bank

#### Create Issuer Role for Business Partner

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This step describes the processes to create the Issuer role for a business partner.

|  |
| --- |
| Remember Sample values for master data values are country/region-specific. Substitute the country/region-specific values provided by SAP Best Practices for SAP S/4HANA Cloud Public Edition or use master data values you have created for this purpose. |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Master Data Specialist - Business Partner Data. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access App | Open Maintain Business Partner (BP). | The Maintain Business Partner: screen displays. |  |
| 3 | Create Issuer role | Choose Open BP. In the dialog box, enter following data:Business Partner: 10537001Choose Enter.Choose Switch Between Display and Change, and enter following data:Change in BP Role: select TR0150 Issuerand choose Save. | On the Change Organization: 10537001, role Issuer screen, the following notification displays:Changes have been saved. |  |

#### Create Depository Bank Role for Business Partner

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This step describes the processes to create the Depository Bank role for a business partner.

|  |
| --- |
| Remember Sample values for master data values are country/region-specific and the following example values provided are for Germany. Substitute the country/region-specific values provided by SAP Best Practices for SAP S/4HANA Cloud Public Edition or use master data values you have created for this purpose. |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Master Data Specialist - Business Partner Data. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the SAP Fiori App | Open Maintain Business Partner (BP). | The Maintain Business Partner screen displays. |  |
| 3 | Create Depository Bank Role | Choose Open BP. In the dialog box, enter following data:Business Partner: 10537001Choose Enter.Choose Switch Between Display and Change, and enter following data:Change in BP Role: select TR0152 Depository Bankand choose Save. | On the Change Organization: 10537001, role Depository Bank screen, the following notification displays:Changes have been saved. |  |

### Maintain Business Partner Master Data for Letter of Credit

#### Create Bank Role for Business Partner

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
| 1 | Log onto SAP Fiori Launchpad | Log on to the SAP Fiori launchpad as a Master Data Specialist - Business Partner Data. | The SAP Fiori Launchpad displays. |  |
| 2 | Access App | Open Maintain Business Partner (BP). | The Maintain Business Partner screen displays. |  |
| 3 | Create Bank Role | Choose Open BP. In the dialog box, enter following data:Business Partner: 10537001Choose Enter.Choose Switch Between Display and Change, and enter following data:Change in BP Role: select TR0703 Bankand choose Save. | On the Change Organization: 10537001 role Bank screen, the following notification displays:Changes have been saved. |  |

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
- related-to :: [[05-treasury-and-cash-management/geschaftspartner-fur-treasury-and-risk-management-anlegen-mds-22g-256]]
- related-to :: [[05-treasury-and-cash-management/mds-22g-259]]
- related-to :: [[05-treasury-and-cash-management/mds-22g-261]]
- related-to :: [[05-treasury-and-cash-management/script-de-dados-mestre-criar-parceiro-de-negocios-para-o-treasury-and]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/22G_S4CLD2608_Master_Data_EN_XX.docx` — full document · extracted with `mammoth` · 40,109 chars in the whole document
