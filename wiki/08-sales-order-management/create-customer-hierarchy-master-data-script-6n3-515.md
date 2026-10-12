---
id: 08-sales-order-management/create-customer-hierarchy-master-data-script-6n3-515
title: Create Customer Hierarchy Master Data Script (6N3) (6N3_S4CLD2608_Master_Data_EN_XX)
description: "SAP S/4HANA Cloud Public Edition 2608 test script (6N3): create customer master data (general, company code, sales area) and customer hierarchies in Fiori."
cluster: 08-sales-order-management
tags: [kb/sales-order-management, topic/customer-hierarchies]
aliases: [6N3_S4CLD2608_Master_Data_EN_XX]
keywords: [Customer Hierarchies, customer master data, company code data, sales area data, business partner roles, partner functions, organizational units, country-specific requirements, test procedures, tax data]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/6N3_S4CLD2608_Master_Data_EN_XX.docx]
confidence: high
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-515
topic: 08-sales-order-management/customer-hierarchies
language: EN
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Create Customer Hierarchy Master Data Script (6N3) (6N3_S4CLD2608_Master_Data_EN_XX)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/6N3_S4CLD2608_Master_Data_EN_XX.docx`, extracted with `mammoth`. Grouped under **Customer Hierarchies** in Sales Order Management. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

|  |  |
| --- | --- |
| <!-- image omitted: unnamed --> | Master Data ScriptSAP S/4HANA Cloud Public Edition - 02-07-26 |
|  | Create Customer Hierarchy Master Data Script (6N3) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Table of Contents

[1 Purpose 2](#_Toc233904847)

[2 Prerequisites 3](#_Toc233904848)

[2.1 System Access 3](#_Toc233904849)

[2.2 Roles 3](#_Toc233904850)

[2.3 Required Organizational Units 3](#_Toc233904851)

[2.4 Mandatory and Optional Master Data 4](#_Toc233904852)

[3 Overview Table 5](#_Toc233904853)

[4 Test Procedures 6](#_Toc233904854)

[4.1 Creating Customer Master Data - General Data 6](#_Toc233904855)

[4.2 Creating Customer Master Data - Company Code Data 13](#_Toc233904856)

[4.3 Creating Customer Master Data - Sales Area Data 18](#_Toc233904857)

[4.4 Creating Customer Hierarchies 23](#_Toc233904858)

## Purpose

The Manage Customer Hierarchies app helps you to create, copy, edit, and delete customer hierarchies and assign multiple levels of hierarchy nodes. You can also manage the validity time frames of the hierarchies, and a hierarchy will be considered for processes only during this specified time frame.

Customer Hierarchy - Analytics: You use this hierarchy type in sales analytics to project transactional data and gain insightful information.

Customer Hierarchy - Sales: You use this hierarchy type for price determination in sales documents and billing documents. This hierarchy contains customer information belonging to the same sales area. The system allows you to add text nodes, which can denote any sort of information such as state, district, and so on that helps you organize the hierarchy better. Furthermore, these text nodes can be maintained as pricing relevant. The hierarchy also contains business partner nodes which must have a customer sales area associated.

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

### Required Organizational Units

The required organizational units are listed below:

| Data Segment | Depends On | Field Examples | Comments | Organizational Unit to be Used |
| --- | --- | --- | --- | --- |
| Basic Data | Independent from organizational units | Business Partner Description, Customer Number, Pricing Relevant, and so on. | Basic data exists only once for a business partner master data record. | N/A |
| Sales Data | Sales Organization, Distribution Channel, and Division | Tax Data, Pricing Relevant, and so on. | Sales data can exist for every Sales Organization of your enterprise structure for which the business partner master data record is used. | Sales OrganizationDistribution ChannelDivision |

### Mandatory and Optional Master Data

Business partner master data records may refer to other master data. The following table provides an overview of mandatory and optional master data objects to be used in a business partner master data record.

| Master Data Object | Used in Data Segment | Mandatory / Optional | Comments |
| --- | --- | --- | --- |
| Sales Area |  | Mandatory | Assigning a sales area to business partner master data is mandatory for customer hierarchy. |

## Overview Table

This scope item consists of several process steps that are listed in the following table:

|  |
| --- |
| Note If your system administrator has enabled spaces and pages on the SAP Fiori launchpad, the homepage will only contain the essential apps for performing the typical tasks of a business role.You can find all other (searchable) apps not included on the homepage using the search bar ([2434549](https://me.sap.com/notes/2434549)).If you want to personalize the homepage and include the hidden apps, navigate to your user profile and choose App Finder. |

| Process Step | Business Role | App/Transaction | Expected Results |
| --- | --- | --- | --- |
| [Creating Customer Master Data - General Data](#unique_8) [page ] 6 | Master Data Specialist - Business Partner Data | Maintain Business Partner (BP) or Manage Customer Master Data (F0850A) | Customer Master - General Data is created. |
| [Creating Customer Master Data - Company Code Data](#unique_9) [page ] 13 | Master Data Specialist - Business Partner Data | Maintain Business Partner (BP) or Manage Customer Master Data (F0850A) | Customer Master - Company Code Data is created. |
| [Creating Customer Master Data - Sales Area Data](#unique_10) [page ] 18 | Master Data Specialist - Business Partner Data | Maintain Business Partner (BP) or Manage Customer Master Data (F0850A) | Customer Master - Sales Area Data is created. |
| [Creating Customer Hierarchies](#unique_11) [page ] 23 | Master Data Specialist - Business Partner Data | Manage Customer Hierarchies (F5794) | Customer Hierarchies are created. |

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

You must complete the previous chapter, [Creating Customer Master Data - General Data](#unique_8) [page ] 6, before you proceed with this chapter.

Follow the procedure after you have saved the General Data entries, as described in the previous chapter.

Procedure: Option 1 - Maintain Business Partner

Follow this procedure when your user access presents you with the Maintain Business Partner (BP) app.

| Test Step # | Test Step Name | Instruction | Expected Result | Pass/Fail/ Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Master Data Specialist - Business Partner Data. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Maintain Business Partner (BP). | The app opens. |  |
| 3 | Search and Open | Search and open the Business Partner (Customer) that you created in the previous chapter: [Creating Customer Master Data - General Data](#unique_8) [page ] 6. | The Business Partner displays in the search list. |  |
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
| 3 | Search and Open | Search and open the Business Partner (Customer) that you created in the previous chapter: [Creating Customer Master Data - General Data](#unique_8) [page ] 6. |  |  |
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

You must complete the previous chapter, [Creating Customer Master Data - General Data](#unique_8) [page ] 6, before you proceed with this chapter.

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
| 3 | Search and Open | Search and open the Business Partner (Customer) that you created in the previous chapter: [Creating Customer Master Data - General Data](#unique_8) [page ] 6. |  |  |
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

### Creating Customer Hierarchies

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The following procedure provides instructions for customer hierarchy of type sales and analytics using the Manage Customer Hierarchies (F5794) app.

Prerequisite

You must complete the previous chapter, [Creating Customer Master Data - General Data](#unique_8) [page ] 6, before you proceed with this chapter.

Follow the procedure after you have saved the General Data entries, as described in the previous chapter.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Master Data Specialist - Business Partner Data. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Manage Customer Hierarchies (F5794). | The app opens. |  |
| 3 | Create New Hierarchy | On the Manage Customer Hierarchies screen, choose Create. |  |  |
| 4 | Choose Hierarchy Type | Choose the hierarchy type from the following options:Customer Hierarchy - SalesCustomer Hierarchy - Analytics |  |  |
| 5 | Enter Hierarchy Related Data | In the Create New Hierarchies dialog box, provide the hierarchy ID and enter other required data. |  |  |
| 6 | Edit Subnode | Once the parent node with the hierarchy ID provided in the previous step is created, add subnodes to this parent node. You will be able to perform the following actions:Change the hierarchy name.Change validities and other details such as sales, distribution, division, and so on.Simulate option as on/off.Delete the subnodes mapped to the hierarchy. |  |  |
| 7 | Subnode Options | Choose the parent node defined in the previous step.Choose the option to define the subnode. Below are the three types of subnodes that can be added:Subnode: This is a text node that can be customized based on your business needs. It can contain multiple subnodes.Subnode - Business Partner: This is a business partner node, which can contain multiple subnodes. The system auto-checks that the business partner added to the hierarchy belongs to the same sales area.Business Partner: This is a business partner node, however, it is a leaf node and cannot contain any further nodes. The system auto-checks that the business partner added to the hierarchy belongs to the same sales area. | The Master Data - Product screen displays.Your data is saved. |  |
| 8 | Create Subnode | Choose the parent node.Choose Edit. Choose + to add a subnode.Choose the relevant customer master records that already exist in the system.If the hierarchy type is Sales, select whether the subode is pricing relevant.Note The subnodes can also be created in fast entry mode which helps to create multiple subnodes in one go. | Ensure that the subnode is created and displayed under the root node.Note If the sales area/division/distribution values are not matched with the relevant customer added before, the subnode cannot be added, and an error message customer doesn't have relevant sales/division/distribution displays. |  |
| 9 | Activate Hierarchy | Choose Activate. | The customer hierarchy is activated. |  |
| 10 | Delete Hierarchy | Choose Delete if you want to delete a hierarchy. |  |  |
| 11 | Export/Import | Choose Export/Import if you want to export or import a hierarchy. | You can export or import a hierarchy structure. |  |

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
- related-to :: [[08-sales-order-management/6n3-517]]
- related-to :: [[08-sales-order-management/6n3-519]]
- related-to :: [[08-sales-order-management/script-de-dados-mestre-criar-script-de-dados-mestre-de-hierarquia-de-c]]
- related-to :: [[08-sales-order-management/script-de-datos-maestros-crear-script-de-datos-maestros-de-jerarquia-d]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/6N3_S4CLD2608_Master_Data_EN_XX.docx` — full document · extracted with `mammoth` · 41,847 chars in the whole document
