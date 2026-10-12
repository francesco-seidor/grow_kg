---
id: 02-business-partner-and-product-master-data/master-data-script-create-customer-master-mds-bnd-sap-s-4hana-cloud-pu
title: "Master Data Script - Create Customer Master - MDS (BND), SAP S/4HANA Cloud Public Edition (BND_S4CLD2608_Master_Data_EN_XX)"
description: "SAP S/4HANA Cloud Public Edition 2608 test script for creating customer master data (general, company code, sales area) via Maintain Business Partner or F0850A."
cluster: 02-business-partner-and-product-master-data
tags: [kb/business-partner-and-product-master-data, topic/customer-master]
aliases: [BND_S4CLD2608_Master_Data_EN_XX]
keywords: [Customer Master Data, business partner creation, company code data, sales area data, number ranges, partner functions, account groups, business roles, tax numbers, country-specific fields]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/BND_S4CLD2608_Master_Data_EN_XX.docx]
confidence: high
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-581
topic: 02-business-partner-and-product-master-data/customer-master
language: EN
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Master Data Script - Create Customer Master - MDS (BND), SAP S/4HANA Cloud Public Edition (BND_S4CLD2608_Master_Data_EN_XX)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/BND_S4CLD2608_Master_Data_EN_XX.docx`, extracted with `mammoth`. Grouped under **Customer Master Data** in Business Partner and Product Master Data. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

|  |  |
| --- | --- |
| <!-- image omitted: unnamed --> | Master Data ScriptSAP S/4HANA Cloud Public Edition - 02-07-26 |
|  | Create Customer Master - MDS (BND) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Table of Contents

[1 Purpose 2](#_Toc233904941)

[2 Prerequisites 3](#_Toc233904942)

[2.1 System Access 3](#_Toc233904943)

[2.2 Roles 3](#_Toc233904944)

[2.3 Preliminary Steps 3](#_Toc233904945)

[2.4 Required Organizational Units 4](#_Toc233904946)

[2.5 Main Parameters for Data Creation 5](#_Toc233904947)

[2.5.1 Business Partner Grouping and Number Ranges 5](#_Toc233904948)

[2.5.2 Business Partner ID 5](#_Toc233904949)

[2.5.3 Business Partner Function 6](#_Toc233904950)

[2.5.4 Account Group 6](#_Toc233904951)

[3 Overview Table 7](#_Toc233904952)

[4 Test Procedures 8](#_Toc233904953)

[4.1 Creating Customer Master Data - General Data 8](#_Toc233904954)

[4.2 Creating Customer Master Data - Company Code Data 15](#_Toc233904955)

[4.3 Creating Customer Master Data - Sales Area Data 20](#_Toc233904956)

## Purpose

A customer is a business partner to which goods and services are sold and delivered. A business partner can be a customer and a supplier at the same time if, for example, your customer also supplies goods to you.

A customer master holds information about the customer such as their name, address, bank details, tax details and delivery and billing preferences. This customer information is used and stored in transactions such as sales orders, deliveries and invoices.

Some customer information is specific to a particular company (known as company code) or sales unit (known as sales area) within your organization.

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

Some segments of customer master data are dependent on the organizational units of the company, General (Central) Data does not depend on an organizational unit or the company code. The following table gives an overview of these different data segments and their relevant organizational units:

| Data Segment | Depends On | Field Examples | Comments | Organizational Unit to be Used |
| --- | --- | --- | --- | --- |
| General / Central Data | Independent from organizational units | ID, Name, Address, Bank Account, Tax Number, Industry Classification | Central data exists only once for a customer master data record. | n/a |
| Company Code Data | Company Code | Reconciliation Account, Payment terms, Accounting Clerk responsible, Account Number at Customer | Company code data can exist for every company code ID of your enterprise structure for which the customer master record is used. | Company Code: ____________ |
| Sales Area Data | Sales Organization, Distribution Channel, and Division(The Sales Area is a combination of these three org. units) | Standard Ordering Currency, Default Delivering Plant, Payment terms, Tax Classification | Sales Data can exist for every sales area for which the customer master record is used. | Sales Organization: __________Distribution Channel: __________Division: __________ |

|  |
| --- |
| Note Brazil specific fields are required to get a proper tax calculation.Check Nota Fiscal Brazil - JD0 in Define BR Specific Fields for Master Data chapter for customer master data. |

### Main Parameters for Data Creation

In this section, we describe some basic parameters that influence the behavior of a master record and are always required to create a customer master data record:

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

Examples for partner functions in Sales and Distribution are: Sold-to party, Ship-to party, and so on.

#### Account Group

Account Groups are leading control parameters for creating the ERP data segments of a customer master record. Currently, the only supported account group for customer master data is CUST.

## Overview Table

This scope item consists of several process steps that are listed in the following table:

|  |
| --- |
| Note If your system administrator has enabled spaces and pages on the SAP Fiori launchpad, the homepage will only contain the essential apps for performing the typical tasks of a business role.You can find all other (searchable) apps not included on the homepage using the search bar ([2434549](https://me.sap.com/notes/2434549)).If you want to personalize the homepage and include the hidden apps, navigate to your user profile and choose App Finder. |

| Process Step | Business Role | App/Transaction | Expected Results |
| --- | --- | --- | --- |
| [Creating Customer Master Data - General Data](#unique_13) [page ] 8 | Master Data Specialist - Business Partner Data | Maintain Business Partner (BP) or Manage Customer Master Data (F0850A) | Customer Master - General Data is created. |
| [Creating Customer Master Data - Company Code Data](#unique_14) [page ] 15 | Master Data Specialist - Business Partner Data | Maintain Business Partner (BP) or Manage Customer Master Data (F0850A) | Customer Master - Company Code Data is created. |
| [Creating Customer Master Data - Sales Area Data](#unique_15) [page ] 20 | Master Data Specialist - Business Partner Data | Maintain Business Partner (BP) or Manage Customer Master Data (F0850A) | Customer Master - Sales Area Data is created. |

## Test Procedures

This section describes test procedures for each process step that belongs to this scope item.

### Creating Customer Master Data - General Data

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The following procedure provides instructions for creating customer master data. Apps available to you are dependent upon your assigned role. Therefore, two options are provided.

The following note is for Saudi Arabia only.

|  |
| --- |
| Note To comply with ZATCA e-invoice regulations, ensure that all required fields, such as Street 2, Street 3, District, etc., are correctly entered in the business partner forms before generating e-documents. This is necessary for the successful validation of e-invoices before submitting them to the tax authority portal.This information is used to populate the appropriate XML tags as required by ZATCA, depending on the type of e-document. For more information on the guidelines from ZATCA, please refer to the Electronic Invoice XML Implementation Standard Guidelines. |

Procedure: Option 1 - Maintain Business Partner

Follow this procedure when your user access presents you with the Maintain Business Partner (BP) app.

| Test Step # | Test Step Name | Instruction | Expected Result | Pass/Fail/Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Master Data Specialist - Business Partner Data. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Maintain Business Partner (BP). | The app opens. |  |
| 3 | Create a Business Partner Organization | Choose Organization. | The Create Organization screen displays. |  |
| 4 | Enter General Data | Make the following entries:Business Partner: <Enter a Business Partner ID that starts with a letter>Grouping: Select, for example, External alpha-numeric numbering.The Create in BP role field is filled by the system with the Business Partner (Gen.) role. Keep this setting.Press Enter.Note For more information about General Data details, see the [Prerequisites](#unique_2) [page ] 3 section. |  |  |
| 5 | Enter Address Data | On the Address tab in the Name section, enter the following data:Title: <Select a title>Name: <Name> |  |  |
| 6 | Enter Address Data | In the Standard Address section, enter the address. |  |  |
| 7 | Enter Time Zone and Transportation Zone | In the Street Address section, choose More fields. Enter the following data:Time Zone: <Time zone>Transportation Zone: <Transportation zone> |  |  |
| For Thailand Only | Enter Additional Address Data (for Thailand Only) | In the Street Address section, choose More and enter the following data:Building code: <Building>Room: <Room no>Floor: <Floor no>Street 2: <Moo>Street 3: <Soi/Lane>Street: <Road>House Number: <no>Different City: <Sub-District>District: <District/Section>City: <Province>Postal code: <Postal code>Telephone: <Telephone number> |  |  |
| 8 | Enter Search Terms | On the Address tab, in the Search Terms section, enter one or two search terms for the business partner. |  |  |
| 9 | Enter Communication Data | In the Communication section, in the Language field, enter the preferred language of the business partner. |  |  |
| For Japan Only | Enter Industry Data (for Japan Only) | On the Identification tab, in the Industries section, choose All Industry Systems. Enter the following data:Industry System: Select Bank of Japan.Industry: <Select an industry number>Standard Industry: <Not selected> |  |  |
| 10 | Enter Tax Numbers | On the Identification tab, in the Tax Numbers section, enter the following data:Category: <Category>Tax Number: <Tax number>Note Choose the correct category applicable for the business partner's country/region. For example, for a German business partner, you maintain a value for the Category DE1, which represents the commonly-used VAT tax number (Umsatzsteuer-Identifikationsnummer). |  |  |
| 11 | Enter Bank Accounts | On the Payment Transactions tab, in the Bank Details section, enter the following data:Bank Key: <Bank key>Bank acct.: <Bank account>Caution Bank keys must be defined beforehand. Use the value help for more information on allowed entries in this field. |  |  |
| 12 | Save Your Data | Save your entries. | Your data is saved. |  |

Procedure: Option 2 - Manage Customer Master Data

Follow this procedure when your user access presents you with the Manage Customer Master Data (F0850A) app.

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori launchpad as a Master Data Specialist - Business Partner Data. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Manage Customer Master Data (F0850A). | The app opens. |  |
| 3 | Create New Organization | On the Customer Master screen, choose Create > Organization. | The Create Organization screen displays in edit mode. |  |
| 4 | Enter Basic Data | On the Create Organization screen, make the following entries:General InformationBusiness Partner: For example, Z … (that is, any external alphanumeric ID, as this must start with a letter).Grouping: For example, BPAB.You must assign each business partner to a grouping when you create the business partner record. The grouping determines the number range. You cannot change the assignment afterwards.Business Partner Role: Select a role, for example, FLCU01 - Customer.Note A Customer must be created either with the business partner role FLCU00 - Customer (Financial Accounting) or with the business partner role FLCU01 - Customer, or with both roles. The business partner role FLCU00 - Customer (Financial Accounting) is used in Financial Accounting, and the business partner role FLCU01 - Customer is used in Sales.Organization Title: For example, Company (0003).Name 1: <Enter a name>Standard AddressCountry/Region: For example, US.Language: For example, EN. |  |  |
| 5 | Close the Create Organization Screen | On the Create Organization screen, choose OK. | The Create Organization screen is closed. The New Customer screen displays. |  |
| 6 | Choose Roles | On the New Customer screen, choose Roles. | You are navigated to the Roles section. |  |
| 7 | Choose Create | In the Roles section, choose Create. |  |  |
| 8 | Enter Additional Roles Data | In the Roles section, choose Create and make the following entry:Business Partner Role: Select the additional role, for example, FLCU00 - Customer (Financial Accounting)Note A Customer must be created either with the business partner role FLCU00 - Customer (Financial Accounting) or with the business partner role FLCU01 - Customer, or with both roles. The business partner role FLCU00 - Customer (Financial Accounting) is used in Financial Accounting, and the business partner role FLCU01 - Customer is used in Sales. | After you complete maintaining all the business partner roles, they display in the Roles section on the New Customer screen. |  |
| 9 | Choose Basic Data | On the New Customer screen, choose Basic Data and go to the Customer Information section. | You are navigated to the Customer Information section. |  |
| 10 | Enter Customer Information | In the Customer Information section, make the following entries:Customer Classification: For example, A - Customer.Customer Account Group: <Customer account group>Note When the Business Partner Grouping allows for a flexible account group assignment, you can choose the account group to be used and deviate from the proposed value. For more details on Business Partner Grouping and how it is related to ID numbering, see the Business Partner Grouping and Number Ranges section in this document. |  |  |
| 11 | Choose Additional Information | On the New Customer screen, choose Basic Data and go the Additional Information section. | You are navigated to the Additional Information section. |  |
| 12 | Enter Additional Information | In the Additional Information section, make the following entries:Express Station: <Express station name>Plant: <Select a Plant>Industry Code 1: <Select an Industry code>Condition Group 1: <Select a Condition group> |  |  |
| 13 | Choose Address | On the New Customer screen, choose Address and go the Standard Address section. | You are navigated to the Standard Address section. |  |
| 14 | Enter Address Data | In the Standard Address section, make the following entries:Street: For example, Augusta Ave SE.Select the country/region if you have not done so in Step 4.House Number: For example, 200.Postal Code: For example, 30315-1402.City: For example, Atlanta.Region: For example, GA.Note When you create a Business Partner located in the United States, the Tax Jurisdiction code is automatically determined. However, you must enter the correct and complete address, as the jurisdiction is derived based on the entries of Region and Postal Code.Standard CommunicationSelect the language if you have not done so in Step 4.Cell Phone: <Cell phone>Email: Add an email address, for example,contact@Z.com. |  |  |
| 15 | Choose Bank Accounts | On the New Customer screen, choose Bank Accounts. | You are navigated to the Bank Accounts section. |  |
| 16 | Choose Create | In the Bank Accounts section, choose Create. | An entry for the Bank Account displays in edit mode. |  |
| 17 | Enter Bank Data | On the New Bank Account screen, make the following entries and choose Apply:ID: For example, BNK1Bank Country: For example, US.Bank Key: For example, 011000390 - Bank 1 SAMPLE BANK.Account Number: For example, 102030.Make entries for all other fields for Bank Data based on your requirements. | You are navigated back to the New Customer screen. |  |
| 18 | Choose Identification Numbers | On the New Customer screen, choose Identification Numbers and go to the Tax Numbers section. | You are navigated to the Tax Numbers section. |  |
| 19 | Choose Create | In the Tax Numbers section, choose Create. |  |  |
| 20 | Enter Tax Number Data | In the Tax Numbers section, make the following entries:Tax Category: <Select a tax category>Tax Number: <Tax number>The Tax Numbers entering depends on the specific country/region requirements.Note Choose the correct category that applies for the customer's country/region. For example, for a German business partner, you maintain a value for the Category DE1, representing the commonly-used VAT tax number (Umsatzsteuer-Identifikationsnummer).Only make entries for the fields that you require, otherwise choose Delete to remove the (empty) data set. |  |  |
| 21 | Choose Tax Categories | On the New Customer screen, choose Tax Categories. | You are navigated to the Tax Categories section. |  |
| 22 | Choose Create | In the Tax Categories section, choose Create. |  |  |
| 23 | Enter Tax Categories Data (Optional) | In the Tax Categories section, make the following entries:Tax Code: For example, COC chamber of commerce.Exemption Certificate Number: <Exemption certificate number>Exemption Certificate Rate: For example, 800.Exemption Start Date: <Exemption start date>.Exemption End Date: <Exemption end date> |  |  |
| 24 | Choose Texts | On the New Customer screen, choose Texts. | You are navigated to the Texts section. |  |
| 25 | Create Texts | In the Texts section, choose Create and make the following entries:Language: For example, EN.ID: For example, 01.Long Text: <Enter a long text> |  |  |
| 26 | Choose Basic Data | Choose Basic Data > Additional Customers. | You are navigated to the Additional Customers section. |  |
| 27 | Add Additional Customer Data | In the Additional Customers section, choose Create.Add the required data as described in the steps above.Note This scenario is for multiple assignments of customers to the same business partners and hence the same master data as described in the steps above applies.If additional data such as Sales data and Company Code data is required, refer to the preceding sections which describe, for example, how to add Sales data and Company Code data. |  |  |
| 28 | Save Your Data | Choose Create. | System message displays that the object has been saved. |  |

### Creating Customer Master Data - Company Code Data

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The following procedure provides instructions for creating customer master data. Apps available to you are dependent upon your assigned role. Therefore, two options are provided.

Prerequisite

You must complete the previous chapter, [Creating Customer Master Data - General Data](#unique_13) [page ] 8, before you proceed with this chapter.

Follow the procedure after you have saved the General Data entries, as described in the previous chapter.

Procedure: Option 1 - Maintain Business Partner

Follow this procedure when your user access presents you with the Maintain Business Partner (BP) app.

| Test Step # | Test Step Name | Instruction | Expected Result | Pass/Fail/ Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Master Data Specialist - Business Partner Data. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Maintain Business Partner (BP). | The app opens. |  |
| 3 | Search and Open | Search and open the Business Partner (Customer) that you created in the previous chapter: [Creating Customer Master Data - General Data](#unique_13) [page ] 8. | The Business Partner displays in the search list. |  |
| 4 | Switch to Change Mode | Choose Switch Between Display and Change (F6) to switch to change mode. |  |  |
| 5 | Change Business Partner Role | In the Change in BP role field, choose the following value:Customer (Financial Accounting)Note The technical key of this Business Partner role is FLCU00. |  |  |
| 6 | Open Company Code Data | Choose Company Code. | The Company Code screen displays. |  |
| 7 | Enter Company Code | Enter the Company Code. |  |  |
| 8 | Enter Customer Accounting Data | On the Customer: Account Management tab, in the Account Management section, make the following entries:Reconciliation Account: 140000 (Customers - Domestic Receivables)Sort key: <Sort key> |  |  |
| 9 | Enter Customer Payment Data | On the Customer: Payment Transactions tab, in the Payment Data section, make an entry for the following field:Terms of Payment: <Terms of payment> |  |  |
| 10 | Enter Customer Payment Data | On the Customer: Payment Transactions tab, in the Automatic Payment Transactions section, make entries for the following fields:Payment Methods: <Payment methods>House Bank: <House bank>Note Press F4 to open the selection in the Field Payment methods. |  |  |
| 11 | Enter Customer Correspondence Data | On the Customer: Correspondence tab, in the Correspondence section, make the following entries:Accounting Clerk: <Accounting clerk>Account at Customer: <Account at customer> |  |  |
| For Thailand Only | Branch Code (for Thailand Only) | Open general data, on the Ctry-Spec.Enh. tab, maintain the Branch Code data along with address and the default Branch Code for this Business Partner.For the Branch Code address, choose Address and enter the following data:Name (First two lines): <Name of tax payer>Country: THBuilding code: <Bldg name/Village>Room: <Room no>Floor: <Floor>Street 2: <Moo>Street 3: <Trok/Soi>Street: <Road>House Number: <no>Other City: <Tumbol/Subsection>District: <District/Section>City: <Province>Postal code: <Postal code>Telephone: <Telephone number>Note When there are more than one Branch Codes for a Business Partner, you should maintain each Branch Code along with the address for each Branch Code. You should also set a Branch Code that is commonly used by the Business Partner as the default one. |  |  |
| For Japan Only | Invoice Summary (for Japan Only) | On the Ctry-Spec.Enh. tab, if this customer is relevant to Invoice Summary, make the following entries according to your requirements:In the Japan: Invoice Summary - Role section:IS Role: <IS Role>In case that IS Role is P: Invoice Summary Payer, in the Japan: Invoice Summary - Invoice section:Number Rang: MI: <Number Rang: MI>Calculation Tax in MI: <Calculation Tax in MI>Move Due Date: <Move Due Date>Rule Payment Term: <Rule Payment Term>Valid From: <Valid From>Payment Term: <Payment Term>In the Japan: Invoice Summary - Payment section:Number Rang: PI: <Number Rang: PI>Bank Charge Payee: <Bank Charge Payee>Bank Charge Pattern ID: <Bank Charge Pattern ID>Relevant for Special Cases: <DO NOT Select>Bank Country: <Bank Country>Bank Key: <Bank Key>Virtual Account Number: <Virtual Account Number>Sequential Number: <Sequential Number>Alternative Payee Name: <Alternative Payee Name>Counter Bank Name: <Counter Bank Name>Counter Bank Branch Name: <Counter Bank Branch Name>In case that IS Role is M: Monthly Invoice Recipients in the Japan: Invoice Summary - Role section:Invoice Summary Payer: <Invoice Summary Payer>In the Japan: Invoice Summary - Invoice section:Number Rang: MI: <Number Rang: MI>Calculation Tax in MI: <Calculation Tax in MI>In case that IS Role is C: (Invoice Summary) Customer in the Japan: Invoice Summary - Role section:Invoice Summary Recipient: <Invoice Summary Recipient> |  |  |
| 12 | Save Your Data | Save your entries. | The entry in the Change in BP role field changes from FI Customer (New) to FI Customer (defined). |  |

Procedure: Option 2 - Manage Customer Master Data

Follow this procedure when your user access presents you with the Manage Customer Master Data (F0850A) app.

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Master Data Specialist - Business Partner Data. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Manage Customer Master Data (F0850A). | The app opens. |  |
| 3 | Search and Open | Search and open the Business Partner (Customer) that you created in the previous chapter: [Creating Customer Master Data - General Data](#unique_13) [page ] 8. |  |  |
| 4 | Choose Edit | Choose Edit. | The Customer Master screen displays in edit mode (fields are ready for your input). |  |
| 5 | Choose Company Code | On the Customer Master screen, choose the Company Codes tab. | You are navigated to the Company Codes section. |  |
| 6 | Choose Create | In the Company Codes section, choose Create. | The New Company Code screen displays in edit mode. |  |
| 7 | Enter Company Code Data | On the New Company Code screen, make the following entries:Company Code: Enter the company code, for example, 1710.On the Correspondence tab:Accounting Clerk: For example: 01 Mrs. Smith.On the Finance tab:Finance - AccountingReconciliation Account: For example, 12100000 - Receivables Foreign.Sort key: For example, 009 External Doc. Number.Finance - Payment DataPayment Terms: For example, 0001.Finance - Automatic Payment TransactionsPayment Methods: For example, C (Check, for example, for US)On the Dunning Data tab:Dunning Area: Organizational unit that you use to process the dunning program, for example, by division, or sales organization.Dunning Procedure, Dunning Block, Dunning Recipient, Dunning Clerk: Choose from the value help.Dunning Level: For example, 0.Last Dunned: For example, 10.02.2020.Legal Dunning Procedure From: For example, 11.02.2020.On the Texts tab:In the Texts section, choose Create and make the following entries:.Language: For example, EN.ID: For example, 01.Long Text: <Enter a long text> |  |  |
| 8 | Return to Main Screen | Choose Apply. |  |  |
| 9 | Save Your Data | Choose Save. | System message displays that the object is saved. |  |

### Creating Customer Master Data - Sales Area Data

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The following procedure provides instructions for creating customer master data. Apps available to you are dependent upon your assigned role. Therefore, two options are provided.

Prerequisite

You must complete the previous chapter, [Creating Customer Master Data - General Data](#unique_13) [page ] 8, before you proceed with this chapter.

Follow the procedure after you have saved the General Data entries, as described in the previous chapter, on the Display Organization: Customer Name screen.

Procedure: Option 1 - Maintain Business Partner

Follow this procedure when your user access presents you with the Maintain Business Partner (BP) app.

| Test Step # | Test Step Name | Instruction | Expected Result | Pass/Fail/Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Master Data Specialist - Business Partner Data. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Maintain Business Partner (BP). | The app opens. |  |
| 3 | Switch to Change Mode | Choose Switch Between Display and Change (F6) to switch to change mode. |  |  |
| 4 | Change Business Partner Role | In the Change in BP role field, choose the following value:CustomerNote The technical key of this Business Partner role is FLCU01. |  |  |
| 5 | Open Sales Area | Choose Sales and Distribution on the screen. | The Sales Area screen displays. |  |
| 6 | Enter Sales Area Data | Make the following entries:Sales Org.: <Sales organization>Distr. Channel: <Distribution channel>Division: <Division>Note These three entries (Sales Organization, Distribution Channel, and Division) form the sales area. In many cases, the sales area sets the purpose for sales processing, for example, within the sales order or pricing. |  |  |
| 7 | Enter Sales Orders Data | On the Orders tab, in the Order section, make the following entry:Currency: <Currency> |  |  |
| 8 | Enter Shipping Data | On the Shipping tab, in the Shipping section, make the following entries:Delivery Priority: <Delivery priority>Delivering Plant: <Delivering plant>Shipping Conditions: <Shipping conditions> |  |  |
| 9 | Enter Billing Data | On the Billing tab, in the Delivery and Payment Terms section, make the following entries:Incoterms: EXW (Ex Works)You can maintain the incoterm value and provide its description.Note The fields for incoterms are interdependent. For example, if you maintain the value for the Incoterms field, you need to provide information for the Incoterm Loc. 1 ID and Incoterm Location 1 fields as well.Terms of Payment: <Select the terms of payment>Note The terms of payment defined here are copied into a sales order and are used instead of the terms of payment defined on the company code level. |  |  |
| 10 | Enter Accounting Data | In the Accounting section, make the following entry:Acct Assmt Grp Cust.: <Select the account assignment group for the customer>For example, domestic customers may be assigned to account assignment group 01, and foreign customers may be assigned to account assignment group 02. Go to the value help to see more options. |  |  |
| 11 | Enter Tax Data | In the Output Tax section, select the following value for the existing entry in the table:Tax Classific: <1>For example, value <1> means that this customer is fully taxable. |  |  |
| 12 | Modify Partner Functions Data | On the Partner Functions tab, the following 4 standard partner functions are available for the customer. You can create the 4 partner functions:SP - Sold-to PartyBP - Bill-To PartyPY - PayerSH - Ship-to PartyNote The 4 partner functions mentioned above are the minimum set of partner functions that must be assigned to a customer master data record to work in a standard sale and distribution process. |  |  |
| 13 | Enter Long Text | In the Customer Text field, enter the details of the sales data. Note that this is a read-only field. Use the Edit Text option to modify the long text. |  |  |
| 14 | Open General Data | Choose General Data on the screen. |  |  |
| 15 | Enter Organization Data | On the Customer: General Data tab, in the Marketing section, make the following entry:Customer Classific.: <Select a customer classification> |  |  |
| 16 | Save Your Data | Save your entries. |  |  |

Procedure: Option 2 - Manage Customer Master Data

Follow this procedure when your user access presents you with the Manage Customer Master Data (F0850A) app.

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Master Data Specialist - Business Partner Data. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Manage Customer Master Data (F0850A). | The app opens. |  |
| 3 | Search and Open | Search and open the Business Partner (Customer) that you created in the previous chapter: [Creating Customer Master Data - General Data](#unique_13) [page ] 8. |  |  |
| 4 | Choose Edit | Choose Edit. | The Customer Master screen displays in edit mode (fields are ready for your input). |  |
| 5 | Choose Sales Area | On the Customer Master screen, choose Sales Areas.Note The Sales Areas tab is only available if the Business Partner has the role FLCU01 (Customer). | The Sales Areas section displays. |  |
| 6 | Choose Create | In the Sales Areas section, choose Create. | The New Sales Area screen displays in edit mode. |  |
| 7 | Enter Sales Area Data | On the New Sales Area screen, make the following entries:General DataSales Organization: For example, 1710.Note If you select the sales organization from the value help, the following fields (Distribution channel and Division) are entered automatically.Distribution channel: For example, 10.Division: For example, 00.Sales Area DetailsSales Area Details - Sales Orders:Account at Customer: <Enter your account at the customer>Currency: For example, USD.Sales Area Details - Billing:Incoterms: For example, EXW.Incoterms Location 1: For example, Palo Alto.Payment Terms: For example, 0001.Sales Area Details - Shipping:Delivery Priority: For example, Normal.Delivery Plant: For example, 1710.Shipping Conditions: For example, Immediately.Sales Area Details - Accounting:Account assignment group: For example, Domestic Revenues.Sales Area Details - Pricing and Statistics:Customer Pricing Procedure: For example, Procedure 01. |  |  |
| 8 | Choose Texts | On the New Sales Area screen, choose Texts. |  |  |
| 9 | Choose Create | In the Texts section, choose Create and make the following entries:Language: For example, EN.ID: Select an ID number or enter an ID number manually, for example, 01.Long Text: <enter a long text> |  |  |
| 10 | Choose Taxes | On the New Sales Area screen, choose Taxes. | The Taxes section displays. |  |
| 11 | Choose Country/Region and Tax Category | In the Taxes section, choose the entry for a country/region, for example, USA (US).Note The Tax Category entry is dependent upon the Customer location. For example, UTXJ is the tax category for creating a US Customer, and TTXJ is the tax category for creating a DE Customer. | The Sales Area Taxes screen displays in edit mode. |  |
| 12 | Enter Tax Classification | On the Tax tab, make the following entry:Tax Classification: Select, for example, Liable for Taxes (1). |  |  |
| 13 | Choose Apply | Choose Apply. | You return to the main view. |  |
| 14 | Choose Partner Functions | On the New Sales Area screen, choose Partner Funtions. | The Partner Funtions section displays. |  |
| 15 | Choose Create | In the Partner Functions section, choose Create. | The Partner Functions section displays in edit mode. |  |
| 16 | Enter Partner Function Data | Select a partner role , for example, Sold-to Party (SP).Choose the entry for the partner role, and on the General Data screen, select a partner number and enter a partner description. |  |  |
| 17 | Return to Main View | Choose Apply. | The added Partner Function displays in the main view. |  |
| 18 | Enter Partner Function Data | Repeat step 15 to step 17 (for adding a Partner Function) to include additional Partner Function data. Add the following Partner Roles:Note Two-character Partner Role keys are language-dependent. The keys documented here are valid for logon language English.In other languages, these keys may be different. For example, the two-character Partner Role keys in German are:AG for Sold-to (Auftraggeber)WE for Ship-to (Warenempfänger)RE for Bill-to (Rechnungsempfänger)RG for Payer (Regulierer)Partner Role: Ship-to Party:Partner Role: SH Ship-to PartyPartner Role: Bill-to Party:Partner Role: BP Bill-To PartyPartner Role: PY Payer:Partner Role: PY Payer |  |  |
| 19 | Return to Main View | Choose Apply.Note Make sure that the system message Draft updated displays at the bottom of the view before you return to the main view. |  |  |
| 20 | Save Your Data | Choose Save. | System message displays that the object is saved. |  |

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
- related-to :: [[02-business-partner-and-product-master-data/mds-bnd-583]]
- related-to :: [[02-business-partner-and-product-master-data/mds-bnd-585]]
- related-to :: [[02-business-partner-and-product-master-data/script-de-dados-mestre-criar-mestre-de-clientes-bnd-sap-s-4hana-cloud]]
- related-to :: [[02-business-partner-and-product-master-data/script-de-datos-maestros-creacion-de-maestro-de-clientes-mds-bnd-582]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/BND_S4CLD2608_Master_Data_EN_XX.docx` — full document · extracted with `mammoth` · 42,107 chars in the whole document
