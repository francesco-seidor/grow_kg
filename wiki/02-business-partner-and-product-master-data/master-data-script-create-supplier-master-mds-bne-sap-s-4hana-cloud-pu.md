---
id: 02-business-partner-and-product-master-data/master-data-script-create-supplier-master-mds-bne-sap-s-4hana-cloud-pu
title: "Master Data Script: Create Supplier Master - MDS (BNE), SAP S/4HANA Cloud Public Edition (BNE_S4CLD2608_Master_Data_EN_XX)"
description: "SAP S/4HANA Cloud Public Edition 2608 test script for creating supplier master data (general, company code, purchasing org) via Maintain Business Partner or F1053A."
cluster: 02-business-partner-and-product-master-data
tags: [kb/business-partner-and-product-master-data, topic/supplier-master]
aliases: [BNE_S4CLD2608_Master_Data_EN_XX]
keywords: [Supplier Master Data, general data, company code data, purchasing organization data, business partner grouping, business partner roles, account groups, organizational units, withholding tax, bank accounts]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/BNE_S4CLD2608_Master_Data_EN_XX.docx]
confidence: low
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-587
topic: 02-business-partner-and-product-master-data/supplier-master
language: EN
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Master Data Script: Create Supplier Master - MDS (BNE), SAP S/4HANA Cloud Public Edition (BNE_S4CLD2608_Master_Data_EN_XX)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/BNE_S4CLD2608_Master_Data_EN_XX.docx`, extracted with `mammoth`. Grouped under **Supplier Master Data** in Business Partner and Product Master Data. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

|  |  |
| --- | --- |
| <!-- image omitted: unnamed --> | Master Data ScriptSAP S/4HANA Cloud Public Edition - 02-07-26 |
|  | Create Supplier Master - MDS (BNE) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Table of Contents

[1 Purpose 2](#_Toc233904931)

[2 Prerequisites 3](#_Toc233904932)

[2.1 System Access 3](#_Toc233904933)

[2.2 Roles 3](#_Toc233904934)

[2.3 Preliminary Steps 3](#_Toc233904935)

[2.4 Required Organizational Units 4](#_Toc233904936)

[2.5 Mandatory and Optional Master Data 5](#_Toc233904937)

[2.6 Main Parameters for Data Creation 5](#_Toc233904938)

[2.6.1 Business Partner Grouping and Number Ranges 5](#_Toc233904939)

[2.6.2 Business Partner ID 6](#_Toc233904940)

[2.6.3 Business Partner Function 6](#_Toc233904941)

[2.6.4 Account Group 6](#_Toc233904942)

[3 Overview Table 7](#_Toc233904943)

[4 Test Procedures 8](#_Toc233904944)

[4.1 Creating Supplier Master Data - General Data 8](#_Toc233904945)

[4.2 Creating Supplier Master Data - Company Code Data 14](#_Toc233904946)

[4.3 Creating Supplier Master Data - Purchasing Organization Data 21](#_Toc233904947)

## Purpose

Business Context

A supplier or vendor is a business partner which delivers and sells goods and services to your organization. A business partner can be a supplier and a customer at the same time if, for example, your supplier also buys goods from you.

A supplier master holds information about the supplier such as their name, address, bank details, tax details and billing preferences. This supplier information is used and stored in transactions such as purchase orders, goods receipts and supplier invoices.

Some supplier information is specific to a particular company (known as company code) or purchasing unit (known as purchasing organization) within your organization.

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
| Master Data Specialist - Business Partner Data | SAP_BR_BUPA_MASTER_SPECIALIST | Master Data - Business Partners / Business Partner Governance / Business Partner Governance / Business Partner Governance | SAP_BR_BUPA_MASTER_SPECIALIST / SAP_CA_SPT_MDG_BP_GOV_PC / SAP_CMD_SPT_BP_GOV_PC / SAP_CA_SPT_MDG_BP_WFUSR_PC |  |

### Preliminary Steps

Context

In this step, you assign the roles of chapter Roles to the test user that are necessary for data replication. Prior to executing this step ensure you have created and added the necessary roles for the specific object for data replication.

| Test Step # | Test Step Name | Instruction | Expected Result | Pass/Fail/Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log onto the SAP Fiori launchpad using your user credentials. | The Home screen displays. |  |
| 2 | Access the SAP Fiori App | Choose Maintain Business Users. |  |  |
| 3 | Enter User Name | Enter the User name given by your System Administrator then choose Go. |  |  |
| 4 | Select User | Select the User from the list. |  |  |
| 5 | Edit | Choose Edit. |  |  |
| 6 | Add Business Roles | Choose Add Business Roles, enter the required Business role into the Search field and choose Enter. |  |  |
| 7 | Select Business Roles | Select the required Business roles and choose OK. |  |  |
| 8 | Save | Choose Save. | Business roles are saved. |  |
| 9 | Home Screen | Go back to the SAP Home screen. | Home screen displays. |  |

### Required Organizational Units

Some segments of Supplier master data are dependent on the organizational units of the company, General (Central) Data does not depend on an organizational unit or the company code. The following table gives an overview of these different data segments and their relevant organizational units:

| Data Segment | Depends On | Field Examples | Comments | Organizational Unit to be Used |
| --- | --- | --- | --- | --- |
| General / Central Data | Independent from organizational units | ID, Name, Address, Bank Account, Tax Number, and so on. | Central data exists only once for a Supplier master data record. | n/a |
| Company Code Data | Company Code | Reconciliation Account, Payment terms, Accounting Clerk responsible, and so on. | Company code data can exist for every company code ID of your enterprise structure for which the Supplier master data record is used. | Company Code:____________ |
| Purchasing Data | Purchasing Organization | Order Currency, Payment terms, Purchasing Group, Shipping conditions | Purchasing Data can exist for every purchasing organization for which the Supplier master data record is used. | Purchasing Organization:__________ |

### Mandatory and Optional Master Data

Supplier master data records may refer to other master data. The following table gives an overview of optional and mandatory master data objects to be used in a Supplier master data record.

|  |
| --- |
| Note Check Nota Fiscal Brazil - JD0 in Define BR Specific Fields for Master Data chapter for Supplier master data. |

| Master Data Object | Used in Data Segment | Mandatory / Optional | Comments |
| --- | --- | --- | --- |
| Bank Master | In the Business Partner UI, you find the entry of bank account data in the Payment Transactions section. | Optional | If you want to maintain the bank accounts of supplier, you must have created the bank master of the corresponding bank. In the customer master records, you can then enter the actual account number together with the bank master data. |
| Reconciliation Account | In the Business Partner UI, you find the entry of the reconciliation account data Company Code > Vendor Account Management | Mandatory | For the reconciliation account, you enter the General Ledger (G/L) account number from the AR (Accounts Receivable) sub ledger.The G/L account you enter must have been created before you can use it in the Supplier master record. |

### Main Parameters for Data Creation

In this section, we describe some basic parameters that influence the behavior of a master record and are always required to create a Supplier master data record:

#### Business Partner Grouping and Number Ranges

Business Partner Groupings determine the number ranges for the Business Partner IDs. You cannot change the assignment or IDs afterwards. If a Business Partner Grouping is assigned to an internal number range, you cannot enter the Business Partner ID manually. In this case, leave the field blank as the system automatically chooses a number from the assigned numeric number range.

The following business partner groupings and corresponding number ranges are defined for business partners (customers, suppliers, contacts, employees, and so on):

| Business Partner Grouping | Range / Business Partner ID | Comments |
| --- | --- | --- |
| BP01 | External numeric number range (low):1 – 999999 | Use this grouping, for example, to migrate numeric master data records |
| BP02 | Internal numeric number range for standard use:1000000 – 9999999 | If no Business Partner Group is entered, this number range is used per default. |
| BP03 | External numeric number range (high):10000000 – 999999999 | Reserved for SAP sample master data objects. |
| BPAB | External alpha-numeric number range:A – ZZZZZZZZZZ | This range must start with a character. |
| BPEE | Internal numeric number range:9980000000 – 9999999999 | Reserved for business partners used as Employees. |

#### Business Partner ID

Business Partner ID

The following options for assigning the Business partner identifier (ID) are available:

- Enter an ID along with a Business Partner Grouping for external numbering. For example

| Business Partner Grouping | Possible Entries for the Business Partner ID |
| --- | --- |
| BP01 | Any number within the corresponding interval 1 – 999999 |
| BPAB | Any alpha-numeric combination up to 10 characters, provided you start with a character, for example, Z-TEST01 |

If you have not specified the Business Partner Grouping and leave the business partner ID blank, the system takes the next free number from the Business Partner Grouping BP02. This grouping is defined as the standard grouping for internal numeric business partner IDs.

#### Business Partner Function

Business Partner Function

The business partner function determines the rights and responsibilities of each partner in a business transaction.

Examples for partner functions in Purchasing are: Vendor, Invoicing Party, Goods supplier, and so on.

#### Account Group

Account Groups are leading control parameters for creating the ERP data segments of a Supplier master record. Currently, the only supported account group for Supplier master data is SUPL.

## Overview Table

This scope item consists of several process steps that are listed in the following table:

|  |
| --- |
| Note If your system administrator has enabled spaces and pages on the SAP Fiori launchpad, the homepage will only contain the essential apps for performing the typical tasks of a business role.You can find all other (searchable) apps not included on the homepage using the search bar ([2434549](https://me.sap.com/notes/2434549)).If you want to personalize the homepage and include the hidden apps, navigate to your user profile and choose App Finder. |

| Process Step | Business Role | App/Transaction | Expected Results |
| --- | --- | --- | --- |
| [Creating Supplier Master Data - General Data](#unique_14) [page ] 8 | Master Data Specialist - Business Partner Data | Maintain Business Partner (BP) or Manage Supplier Master Data (F1053A) | Supplier Master – General Data is created. |
| [Creating Supplier Master Data - Company Code Data](#unique_15) [page ] 14 | Master Data Specialist - Business Partner Data | Maintain Business Partner (BP) or Manage Supplier Master Data (F1053A) | Supplier Master – Company Code Data is created. |
| [Creating Supplier Master Data - Purchasing Organization Data](#unique_16) [page ] 21 | Master Data Specialist - Business Partner Data | Maintain Business Partner (BP) or Manage Supplier Master Data (F1053A) | Supplier Master – Purchasing Data is created. |

## Test Procedures

This section describes test procedures for each process step that belongs to this scope item.

### Creating Supplier Master Data - General Data

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The following procedure provides instructions for creating supplier master data. Apps available to you are dependent upon your assigned role. Therefore, two options are provided.

Procedure: Option 1 - Maintain Business Partner

Follow this procedure when your user access presents you with the Maintain Business Partner (BP) app.

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Master Data Specialist - Business Partner Data. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Maintain Business Partner (BP). | The app opens. |  |
| 3 | Create a Business Partner Organization | Choose Organization. | The Create Organization screen displays. |  |
| 4 | Enter General Data | Make the following entries and choose OK:Business Partner: <Enter a Business Partner ID that starts with a letter>Grouping: Select, for example, External alpha-numeric numbering.The Create in BP role field is filled by the system with the Business Partner (Gen.) role. Keep this setting.Note For more information, see the previous [Business Partner Grouping and Number Ranges](#unique_9) [page ] 5 chapter. |  |  |
| 5 | Enter Address Data | On the Address tab, in the Name section, enter the following data:Title: <Company>Name: <Name> |  |  |
| 6 | Enter Search Term | On the Address tab, in the Search Term section, enter one or more search terms for the Supplier. |  |  |
| 7 | Enter Address Data | In the Standard Address section, in the Street Address sub-section, enter the address. |  |  |
| 8 | Enter Time Zone and Transportation Zone | In the Street Address section, choose More fields. Enter the following data:Time Zone: <Time zone>Transportation Zone: <Transportation zone> |  |  |
| For Thailand Only | Enter Address Data (for Thailand Only) | In the Street Address section, choose More and enter the following data:Building code: <Building>Room: <Room no>Floor: <Floor no>Street 2: <Moo>Street 3: <Soi/Lane>Street: <Road>House Number: <no>Different City: <Sub-District>District: <District/Section>City: <Province>Postal code: <Postal code> |  |  |
| 9 | Enter Communication Data | On the Address tab, in the Communication section, enter the following data:Language: <Select the preferred language of the Supplier>Telephone: <Telephone number>E-Mail: <E-mail address> |  |  |
| 10 | Enter Identification Data | On the Identification tab, in the Organizational Data section, enter the following data for the supplier:Legal form: <Legal form> |  |  |
| For Japan Only | Enter Industry Data (for Japan Only) | On the Identification tab, in the Industries section, choose All Industry Systems. Enter the following data:Industry System: Select Bank of Japan.Industry: <Select an industry number>Standard Industry: <Not selected> |  |  |
| For Japan Only | Enter Tax Number Data (for Japan Only) | Press Enter for confirmation.Caution If you choose the wrong setting, you will not be able to maintain Japan: My Number data. |  |  |
| For Japan Only | Enter Tax Number Long Data (for Japan Only) | On the Identification tab, in the Tax Numbers Long section, enter the following data:Category: JP4 Japan VAT Registration NumberTax Number Long: <Business partner's corporate number> |  |  |
| 11 | Enter Bank Accounts | On the Payment Transactions tab, in the Bank Details section, enter the following data for the supplier:Country/Region: <Country/Region>Bank Key: <Bank key>Bank Account: <Bank account>Caution Bank keys must be defined beforehand. Use the value help for more information on allowed entries in this field. |  |  |
| 12 | Save Your Data | Save your entries. |  |  |

Procedure: Option 2 - Manage Supplier Master Data

Follow this procedure when your user access presents you with the Manage Supplier Master Data (F1053A) app.

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Master Data Specialist - Business Partner Data. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Manage Supplier Master Data (F1053A). | The app opens. |  |
| 3 | Choose Create | In the Suppliers section, choose, choose Create > Organization. | The Create Organization screen displays. |  |
| 4 | Enter General Data | In the General Data section, enter the following data and choose OK:Business Partner: For example, Z … (that is, any external alphanumeric ID, as this must start with a letter).Grouping: For example, <External alpha-numeric numbering>.Title: For example, Company (0003)Name 1: <Enter a Name> | The New Supplier screen displays. |  |
| 5 | Enter Basic Data | On the New Supplier screen, on the Basic Data tab, make the following entries:In the Supplier Information section, enter the following data:Reference Account Group, Supplier Authorization Group, etc.: Select from the value help.In the Organizational Data section, enter the following data:VAT Liability, Tax Split, Payment Block, etc.: Select the relevant indicators.Note For more information about BP-Groupings and how they are related to ID numbering, see the previous [Business Partner Grouping and Number Ranges](#unique_9) [page ] 5 chapter.In the Additional Information section, enter the following data:Block Function: Select from the value help.Plant: Select from the value help.Instruction Key: Select from the value help. |  |  |
| 6 | Choose Roles | On the New Supplier screen, choose the Roles tab. | You are navigated to the Roles section. |  |
| 7 | Choose Create | In the Roles section, choose Create and select a role from the value help:Business Partner Role: For example, FLVN01.A Supplier Master must be created either with the business partner role FLVN00 (FI Supplier) or with the business partner role FLVN01 (Supplier with purchasing data), or with both roles. The business partner role FLVN00 (FI Supplier) is used in Financial Accounting, and the business partner role FLVN01 (Supplier with purchasing data) is used in Sales.Note Make sure that the system message Draft saved displays at the bottom of the screen before you return to the main screen. | The Role is added. |  |
| 8 | Enter Additional Roles (Optional) | Repeat Step 6 and Step 7 to add an additional role.Business Partner Role: For example, FLVN00. | After you have entered all the Business Partner roles, they display in the Roles section of the New Master screen. |  |
| 9 | Choose Standard Address | On the Supplier Master - New Supplier screen, choose the Address tab and go to the Standard Address section. | You are navigated to the Standard Address section. |  |
| 10 | Enter Address Data | In the Address - Standard Address section, make entries for all the relevant fields according to your requirements. For example:Street: <Street name>House Number: <Number for the address>Postal Code: <Postal code for the address>City: <City>Country/Region: <Country/Region code>Note (Only applies to the United States) When you create a Business Partner located in the United States, the Tax Jurisdiction code is automatically determined. However, you must enter the correct and complete address, as the jurisdiction is derived based on the entries of Country (US), State, and Postal Code.In the Address - Standard Communication section, make the following entries:Language: <Language>Telephone: <Enter the field as required>Email: For example, contact@Z.com.Choose Create.In the Address - Address Details section, select the address entry.On the New Address screen, on the Address Usages tab, verify that the following information is displayed:Address Type: XXDEFAULT |  |  |
| 11 | Return to Main Screen | Choose Apply.Note Make sure that the system message Draft saved displays at the bottom of the screen before you return to the main screen. |  |  |
| 12 | Choose Bank Accounts | On the Supplier Master - New Supplier … screen, choose the Bank Accounts tab. | You are navigated to the Bank Accounts section. |  |
| 13 | Choose Create | On the Supplier Master - Bank Accounts … screen, choose Create. | A new bank account is added. |  |
| 14 | Enter Bank Data | Enter the following data for the new bank account:ID: For example, BNK1.Bank Country/Region: <Country/Region code>Bank Key: <Bank key>Account Number: <Account number>Make entries for all other fields according to your requirements. |  |  |
| 15 | Return to Main Screen | Choose Apply.Note Make sure that the system message Draft saved displays at the bottom of the screen before you return to the main screen. |  |  |
| 16 | Choose Tax Number (Optional) | On the Supplier Master - New Supplier screen, on the Identification tab, choose TAX NUMBERS. | You are navigated to the TAX NUMBERS section. |  |
| 17 | Choose Create (Optional) | In the Supplier Master - New Supplier Master - TAX NUMBER … section, choose Create. |  |  |
| 18 | Enter Tax Number Data (Optional) | In the Tax Numbers section, make the following entries:Tax Category: <Tax code>Tax Number: <Tax number>Note The Tax Numbers entering depends on the specific country/region requirements.Choose the correct category that applies for the customer's country/region. For example, for a German business partner, you maintain a value for the Category DE1, representing the commonly-used VAT tax number (Umsatzsteuer-Identifikationsnummer).Only make entries for the fields that you require, otherwise choose Delete to remove the (empty) data set. |  |  |
| 19 | Return to Main Screen | Choose the back arrow.Note Make sure that the system message Draft saved displays at the bottom of the screen before you return to the main screen. |  |  |
| 20 | Choose Create | In the Supplier Master - New Supplier - Tax Categories section, choose Create. | The Tax Categories screen displays. |  |
| 21 | Enter Tax Categories Data (Optional) | Make the following entries:Tax Code: For example, IVA Purchase VAT .Collection Authorization From: <Date>Collection Authorization To : <Date> |  |  |
| 22 | Enter Texts (Optional) | On the Texts screen, make the following entries:Language: For example, EN.ID: For example, 01.Long Text: <Enter a long text> |  |  |
| 23 | Enter Additional Supplier Data (Optional) | Go to Basic Data > Additional Supplier Data, and choose Create.Add the required data as described in the steps above.Note This scenario is for multiple assignments of suppliers to the same business partners and hence the same master data as described in the steps above applies.If additional data such as Purchase data and Company Code data is required, refer to the preceding sections which describe the same. |  |  |
| 24 | Save Your Data | Choose Create. | System message displays that the object is saved. |  |

### Creating Supplier Master Data - Company Code Data

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The following procedure provides instructions for creating supplier master data. Apps available to you are dependent upon your assigned role. Therefore, two options are provided.

Prerequisite

You must complete the previous chapter, [Creating Supplier Master Data - General Data](#unique_14) [page ] 8, before you proceed with this chapter.

Follow the procedure after you have saved the General Data entries, as described in the previous chapter, on the Display Organization: <Supplier Name> screen.

Procedure: Option 1 - Maintain Business Partner

Follow this procedure when your user access presents you with the Maintain Business Partner (BP) app.

| Test Step # | Test Step Name | Instruction | Expected Result | Pass/Fail/Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Master Data Specialist - Business Partner Data. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Maintain Business Partner (BP). | The app opens. |  |
| 3 | Switch to Change Mode | Choose Switch Between Display and Change (F6) to switch to change mode. |  |  |
| 4 | Change Business Partner Role | In the Change in BP role field, choose the following value:Supplier (Financial Accounting)Note The technical key of this Business Partner role is FLVN00. |  |  |
| 5 | Open Company Code Data | Choose Company Code on the screen. | The Company Code screen displays. |  |
| 6 | Enter Company Code | Enter the Company Code. For example, 1010. |  |  |
| For Russia Only | Enter Vendor Accounting Data - Head Office (for Russia Only) | On the Vendor: Account Management tab, in the Account Management section, enter one of the following:163107701 as a head office for VAT BP 163117701163107701 as a head office for VAT BP 163117701163107701 as a head office for Property Tax BP 163127701163107702 as a head office for Property Tax BP 163127702 |  |  |
| 7 | Enter Vendor Accounting Data | On the Vendor: Account Management tab, in the Account Management section, enter the following data:Reconciliation Account: <21100000> (Payables Domestic)Sort key: <Sort key>Minority Indicator: <Minority indicator> (The minority indicator values are defined using the Configuration Step: Define Minority Indicators)Note There might be other G/L reconciliation accounts for foreign Suppliers or affiliates. |  |  |
| For Japan Only | Enter Vendor Accounting Data - Withholding Tax (for Japan Only) | On the Vendor: Account Management tab, in the Withholding Tax section, enter the following data, if this Supplier is relevant to withholding tax:WTax C/R Key: <JP> (Japan) |  |  |
| For Poland Only | Enter Vendor: Withholding Tax (for Poland Only) | On the Vendor: Withholding Tax tab, in the Withholding Tax Types section, make the following entries:Assign the Withholding Tax Type and Withholding Tax Code information to Business Partner.Enter Exemption Reason (DT), Exemption Percentage (for example, 100%), Exemption Number, and Validity Range for the Withholding Tax Codes that are relevant to Double Taxation Treaty/Double Taxation Agreement. |  |  |
| 8 | Enter Vendor Payment Data | On the Vendor: Payment Transactions tab, in the Payment Data section, make the following entry:Terms of Payment: <Terms of Payment>Note The terms of payment defined in this step can be overruled by the terms of payment defined on the Purchasing level. |  |  |
| 9 | Enter Supplier Payment Data | On the Vendor: Payment Transactions tab, in the Automatic Payment Transactions section, enter the following data:Payment Methods: <Payment methods>House Bank: <House bank>Note Press F4 to open the selection in the Field Payment methods. |  |  |
| 10 | Enter Supplier Correspondence Data | On the Vendor: Correspondence tab, in the Correspondence section, enter the following data:Account with vendor: <Account with vendor> |  |  |
| For Japan Only | Withholding Tax (for Japan Only) | On the Withholding Tax tab, make the following entry, if this Supplier is relevant to withholding tax:Withholding Tax Type: <Withholding tax type>Withholding Tax Code: <Withholding tax code>Subject: <selected> |  |  |
| For Japan Only | Japan: My Number (for Japan Only) | Choose General Data. On the Country-Spec. Enh. tab, make the following entry, if this Business Partner is not a natural person:Corporate Number: <Corporate number>On the Country-Spec. Enh. tab, make the following entries, if this Supplier is a natural person:Choose Valid From and Valid To, and then choose Display.Status: <Status>Evidence for Identity: <Evidence for identity>Evidence for Number: <Evidence for number>Retention Until: <Retention until>Choose Unmask to enter the Individual Number. |  |  |
| For Thailand Only | Branch Code (for Thailand Only) | Open general data, on the Country-Spec. Enh. tab, maintain the Branch Code data along with address and the default Branch Code for this Business Partner.For the Branch Code address, choose Address and enter the following data:Name (First two lines): <Name of tax payer>Country: THBuilding code: <Bldg name/Village>Room: <Room no>Floor: <Floor>Street 2: <Moo>Street 3: <Trok/Soi>Street: <Road>House Number: <no>Other City: <Tumbol/Subsection>District: <District/Section>City: <Province>Postal code: <Postal code>Telephone: <Telephone number>Note When there are more than one Branch Codes for a Business Partner, you should maintain each Branch Code along with the address for each Branch Code. You should also set a Branch Code that is commonly used by the Business Partner as the default one. |  |  |
| For Russia Only | Tax Payment Attributes (for Russia Only) | On the Country-Spec. Enh. tab, make the following entries for the Business Partner.For Property Tax BP 163107701 and 163107702, enter the following values:Type of Payment: Payments to BudgetPayer Status: 01Budget code: 182 1 06 02010 02 1000 110For Payroll Payment BP 163107703, enter the following value:Type of Payment: Payments to BudgetFor VAT BP 163117701 and 163117702, enter the following values:Type of Payment: Payments to BudgetPayer Status: 01Budget code: 18210301000011000110For Property Tax BP 163127701 and 163127702, enter the following values:Type of Payment: Payments to BudgetPayer Status: 01Budget code: 18210602010021000110 |  |  |
| For Saudi Arabia Only | Vendor: Country-Spec. Enh. (for Saudi Arabia Only) | On the Vendor: Country-Spec. Enh. tab, choose Insert Row to add the Supplier Certificates. |  |  |
| 11 | Save Your Data | Save your entries. | The entry in the Change in BP role field changes from FI Vendor (New) to FI Vendor (defined). |  |

Withholding Tax Information (Brazil only)

Use the following table to determine the withholding tax entries in the previous step for Brazil only.

For Company Organization:

| WHT T. Type | W. Tax Code | subject | Comments |
| --- | --- | --- | --- |
| GA | GA | X | for 4,65% |
| PA | PA | X | for PIS only |
| CA | CA | X | for COFINS only |
| SA | SA | X | for CSSL only |
| RA | RA | X | for IRPJ only (via TAXBRA) |
| IR | R1 to R3 | X | for IRPJ only (via FI) |
| IW | IW | X | for ISS |
| IJ | I1 to I2 | X | for INSS PJ |

For Natural Person:

| WHT T. Type | W. Tax Code | subject | Comments |
| --- | --- | --- | --- |
| ID | R0 to R5 | X | for INSS PF |
| IN | N1 | X | for INSS PR |

Procedure: Option 2 - Manage Supplier Master Data

Follow this procedure when your user access presents you with the Manage Supplier Master Data (F1053A) app.

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Master Data Specialist - Business Partner Data. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Manage Supplier Master Data (F1053A). | The app opens. |  |
| 3 | Enter Supplier Details | From the value help, select Business Partner. Additionally, you can select more details such as Street.Choose Go. |  |  |
| 4 | Select Supplier | From the results list, select a Supplier. | The Supplier screen displays. |  |
| 5 | Choose Edit | Choose Edit.Note This step assumes that you are continuing from the previous step and are already navigated to Master Data - Supplier Master > Manage Supplier Master. After you have saved your general data from the previous section, the system is in display mode. To continue, you must be in edit mode. | The Manage Supplier Master screen displays in edit mode (fields are ready for your input). |  |
| 6 | Choose Company Codes | On the Manage Supplier screen, choose Company Codes. |  |  |
| 7 | Choose Create | In the Company Codes section, choose Create. | A details view displays in edit mode. |  |
| 8 | Enter Company Code Data | In the Company Codes section, choose an entry to open a details view. Make the following entries:On the General Data tab:Company Code: Enter the company code, for example, 1710.On the Correspondence tab:Accounting Clerk: For example: 01 Mrs. Smith.Account at Supplier: <Account at Supplier>On the Finance tab:Finance - AccountingReconciliation Account: For example, 21100000 - Payables Domestic.Sort key: For example, 009 External Doc. Number.Minority Group: <Minority group> (This is only valid for the FLVN00 - Supplier (Financial Accounting) role. The minority group values are defined using the configuration step: Define Minority Indicators.)Finance - Payment DataPayment Terms: For example, 0001.Finance - Automatic Payment TransactionsPayment Methods: For example, E Direct Debit.On the Dunning Data tab:Dunning Procedure, Dunning Block, Dunning Recipient, Dunning Clerk: Choose from the value help.Dunning Level: For example, 0.Last Dunned: For example, 10.02.2020.Legal Dunning Procedure From: For example, 11.02.2020.On the Texts tab:In the Texts section, choose Create and make the following entries:.Language: For example, EN.ID: For example, 01.Long Text: <Enter a long text> |  |  |
| 9 | Return to Main Screen | Choose Create, and then choose Apply.Note Make sure that the system message Draft saved displays at the bottom of the screen before you return to the main screen. |  |  |
| 10 | Save Your Data | Choose Save. | System message displays that the object is saved. |  |

### Creating Supplier Master Data - Purchasing Organization Data

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The following procedure provides instructions for creating supplier master data. Apps available to you are dependent upon your assigned role. Therefore, two options are provided.

Prerequisite

You must complete the previous chapter, [Creating Supplier Master Data - General Data](#unique_14) [page ] 8, before you proceed with this chapter.

Follow the procedure after you have saved the General Data entries, as described in the previous chapter, on the Display Organization: <Supplier Name> screen.

Procedure: Option 1 - Maintain Business Partner

Follow this procedure when your user access presents you with the Maintain Business Partner (BP) app.

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Master Data Specialist - Business Partner Data. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Maintain Business Partner (BP). | The app opens. |  |
| 3 | Switch to Change Mode | Choose Switch Between Display and Change (F6) to switch to change mode. |  |  |
| 4 | Change Business Partner Role | In the Change in BP role field, choose the following value:SupplierNote The technical key of this Business Partner role is FLVN01. |  |  |
| 5 | Open Purchasing Organization Data | Choose Purchasing on the screen. | The Purchasing Organization screen displays. |  |
| 6 | Enter Purchasing Data | Enter the following data and press Enter:Purchasing Organization: <Purchasing organization> |  |  |
| 7 | Enter Purchasing Data | On the Purchasing Data tab, in the Conditions section, enter the following data:Order Currency: <Order currency>Payment Terms: <Payment terms> |  |  |
| 8 | Enter Purchasing Data | On the Purchasing Data tab, in the Control Data section, enter the following data:Shipping Conditions: <Shipping conditions>GR-Based Inv. Verif.: <GR-based invoice verification> |  |  |
| 9 | Enter Purchasing Data | On the Purchasing Data tab, in the Default Values for Material section, enter the following data:Purchasing Group: <Purchasing group>Planned Deliv. Time: <Planned delivery time> |  |  |
| 10 | Enter Partner Functions Data | On the Partner Functions tab, in the Partner Functions section, verify that the LF entry (or the VN entry when the logon language is English) exists. |  |  |
| 11 | Save Your Data | Save your entries. |  |  |

Procedure: Option 2 - Supplier Master

Follow this procedure when your user access presents you with the Manage Supplier Master Data (F1053A) app.

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Master Data Specialist - Business Partner Data. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Manage Supplier Master Data (F1053A). | The app opens. |  |
| 3 | Choose Edit | Choose Edit.Note This step assumes that you are continuing from the previous step and are already navigated to Master Data - Supplier Master > Supplier Master. After you have saved your data from the previous section, the system is in display mode. To continue, you must be in edit mode. | The Supplier Master screen displays in edit mode (fields are ready for your input). |  |
| 4 | Choose Purchasing Organizations | In the Supplier Master … screen, choose PURCHASING ORGANIZATIONS. | The Supplier Master - PURCHASING section displays. |  |
| 5 | Choose Create | In the Supplier Master - PURCHASING section, choose Create. | The New Purchasing Organization … screen displays in edit mode. |  |
| 6 | Enter Purchasing Organization Data | On the New Purchasing Organization screen, make the following entries:On the General Data tab:Purchasing Organization: <Purchasing organization code>Purchasing Group: For example, 001.On the PURCHASING tab:For the Conditions column:Order Currency: <Currency code>Minimum Order Value: <Minimum order value>Payment terms: For example, 0001.Pricing Data Control: For example, <Current date>.For the Control Data column:Shipping Condition: For example, 01.Automatic Purchasing Order: <Automatic purchasing order>Goods Receipt-Based Invoice Verification (checkbox) |  |  |
| 7 | Enter Partner Functions Data | Note Some Partner Functions are predetermined based on the customization for selected Account Groups and Purchasing Organizations.To add more Partner Functions, on the Partner Functions tab, choose Create. You can select from the following functions:VN - SupplierGS - Good SupplierMN - Manufacturing Plant |  |  |
| 8 | Enter Purchasing Organization Details | On the Text tab, choose Create and enter the details of Purchasing Organization. |  |  |
| 9 | Return to Main Screen | Choose Apply.Note Make sure that the system message Draft saved displays at the bottom of the screen before you return to the main screen. |  |  |
| 10 | Save Your Data | Choose Save. | System message displays that the object is saved. |  |

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
> Flagged while digesting this document, not verified: Reconciliation account text says to enter the G/L account from the AR sub ledger for a supplier (payables expected), and FLVN01 is said to be used in Sales rather than Purchasing; internally inconsistent wording.

## Connections
- part-of :: [[_cluster]]
- related-to :: [[02-business-partner-and-product-master-data/mds-bne-591]]
- related-to :: [[02-business-partner-and-product-master-data/sap-s-4hana-cloud-public-edition-mds-bne-589]]
- related-to :: [[02-business-partner-and-product-master-data/script-de-dados-mestre-criar-mestre-de-fornecedores-mds-bne-590]]
- related-to :: [[02-business-partner-and-product-master-data/script-de-datos-maestros-creacion-de-maestro-de-proveedores-bne-588]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/BNE_S4CLD2608_Master_Data_EN_XX.docx` — full document · extracted with `mammoth` · 40,886 chars in the whole document
