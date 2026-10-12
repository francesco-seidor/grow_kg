---
id: 09-subscription-billing-and-contract-accounting/master-data-script-create-subscription-product-convergent-invoicing-md
title: "Master Data Script: Create Subscription Product Convergent Invoicing - MDS (5LP) (5LP_S4CLD2608_Master_Data_EN_XX)"
description: "Step-by-step master data script (5LP) for S/4HANA Cloud Public Edition 2608: FI-CA business partner, contract account, SAP Subscription Billing products and SBPD/SBRE enrichment."
cluster: 09-subscription-billing-and-contract-accounting
tags: [kb/subscription-billing-and-contract-accounting, topic/subscription-product-master-data]
aliases: [5LP_S4CLD2608_Master_Data_EN_XX]
keywords: [Subscription Products and Rate Plans, subscription products, business partner, customer master data, contract account, rate elements, rate plan templates, price calculation, lookup tables, product master data]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/5LP_S4CLD2608_Master_Data_EN_XX.docx]
confidence: low
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-449
topic: 09-subscription-billing-and-contract-accounting/subscription-product-master-data
language: EN
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Master Data Script: Create Subscription Product Convergent Invoicing - MDS (5LP) (5LP_S4CLD2608_Master_Data_EN_XX)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/5LP_S4CLD2608_Master_Data_EN_XX.docx`, extracted with `mammoth`. Grouped under **Subscription Products and Rate Plans** in Subscription Billing and Contract Accounting. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

|  |  |
| --- | --- |
| <!-- image omitted: unnamed --> | Master Data ScriptSAP S/4HANA Cloud Public Edition - 02-07-26 |
|  | Create Subscription Product Convergent Invoicing - MDS (5LP) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Table of Contents

[1 Purpose 3](#_Toc233904752)

[2 Prerequisites 4](#_Toc233904753)

[2.1 System Access 4](#_Toc233904754)

[2.2 Roles 4](#_Toc233904755)

[2.3 Required Organization Units (SAP S/4HANA) 4](#_Toc233904756)

[3 Overview Table 6](#_Toc233904757)

[4 Procedures 7](#_Toc233904758)

[4.1 Create Business Partner 7](#_Toc233904759)

[4.1.1 Create Customer Master Data 8](#_Toc233904760)

[4.1.2 Create a Contract Account 10](#_Toc233904761)

[4.2 Create Subscription Product (SAP Subscription Billing) 12](#_Toc233904762)

[4.2.1 Create Rate Elements 12](#_Toc233904763)

[4.2.2 Create Rate Plan Template 13](#_Toc233904764)

[4.2.3 Create Product (SAP Subscription Billing) 15](#_Toc233904765)

[4.2.4 Create a Product for Price Calculation Services 16](#_Toc233904766)

[4.2.5 Uploading Lookup Tables for Price Determination 19](#_Toc233904767)

[4.3 Enrich Subscription Billing Products 24](#_Toc233904768)

[4.3.1 Enhance Subscription Product of Type SBPD 24](#_Toc233904769)

[4.3.2 Enhance Subscription Products of Type SBRE 27](#_Toc233904770)

[5 Appendix 31](#_Toc233904771)

## Purpose

In this document, you find a description of how to create subscription product master data. The description includes those data segments that are relevant for the master data to work in a "usual" system environment. Here, the reader mainly learns about the data segments and fields that need to be filled with input values. Fields that are not relevant for the scope are not described in this document, although they may appear on the UI.

A subscription master record that is created as per this document can be used for subscription billing.

| Subscription Product ID | Description | Usage |
| --- | --- | --- |
| P-CLOUD_COMM | Subscription product | Represents the subscription product |
| P-CLOUD_SUPPORT | Subscription product | Represents the subscription product |

## Prerequisites

### System Access

The following table discusses the system access requirements.

| System | Details |
| --- | --- |
| SAP S/4HANA System | Accessible via SAP Fiori Launchpad.Your system administrator provides you with the URL to access the various apps assigned to your role. |
| SAP Subscription Billing | Accessible via URL.Your system administrator provides you with the URL to access the application. |

### Roles

You can create business roles using the following business role templates delivered by SAP and assign them to your individual test users.

SAP S/4HANA

| Name (Role Template) | ID (Role Template) | Name (Launchpad Space) | ID (Launchpad Space) | Log On |
| --- | --- | --- | --- | --- |
| Master Data Specialist - Product Data | SAP_BR_PRODMASTER_SPECIALIST | Master Data Specialist - Product Data | SAP_BR_PRODMASTER_SPECIALIST |  |
| Accounts Payable and Receivable Accountant (FI-CA) | SAP_BR_APR_ACCOUNTANT_FICA | Accounts Payable and Receivable Accountant (FI-CA) | SAP_BR_APR_ACCOUNTANT_FICA |  |

SAP Subscription Billing

You must contact your system administrator for setting up the required authorizations.

### Required Organization Units (SAP S/4HANA)

While some segments of master data are dependent on the organizational units of the company, the General (Central) Data does not depend on either an organizational unit or the company code. The following table gives an overview of these different data segments and their relevant organizational units:

| Data Segment | Depends On | Organizational Unit to be Used | Comments |
| --- | --- | --- | --- |
| Create Master Data Record | Sales Organization | 1710 (Dom. Sales Org US) | For Germany, use 1010 (Dom. Sales Org DE) |
| Create Master Data Record | Distribution Channel | 10 (Direct Sales) |  |

## Overview Table

This master record consists of several segments provided in the table below.

| Segment | Business Role | App/Transaction | Expected Results |
| --- | --- | --- | --- |
| Create Subscription Product (SAP Subscription Billing) | N/A | N/A | Subscription products are created. |
| Enrich Subscription Products (SAP S/4HANA) | SAP_BR_PRODMASTER_SPECIALIST | Manage Product Master Data | Subscription products are created. |

## Procedures

This section describes procedures for each segment or process step that is part of this master record.

### Create Business Partner

Context

In this activity, you create a business partner for a new FI-CA customer in S/4HANA Cloud.

Procedure

| Test Step Number | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as an Accounts Payable and Receivable Accountant (FI-CA). | The SAP Fiori Launchpad is displayed. |  |
| 2 | Access the SAP Fiori App | Open Maintain Business Partner (BP). | The Maintain Business Partner view is displayed. |  |
| 3 | Create a Business Partner | Choose Person or select More > Business Partner > Create > Person . | The Create Person view is displayed. |  |
| 4 | Select the BP Role | Make the following entry:Create in BP role: Contract Partner | The Change to Another BP Role view is displayed in create mode. |  |
| 5 | Create | Choose Create | Select Role Contract Partner on the Create Person dialog box.Contract Partner (New) is selected for Create in BP Role. |  |
| 6 | Enter Basic Data | Make the following entries:Business Partner: <Enter a specific ID>, for example, BP_US_97Grouping: External alpha-numeric numbering |  |  |
| 7 | Enter Address Data | Make the following entry in Address tab:First Name/Last name: John/MillerStreet/House Number: Hillview Ave/3410Postal Code/City: 94304/PALO ALTOCountry: USRegion: CATax Jurisdiction: CA00000000Tip If Tax Jurisdiction is not visible, click on + to expand the options. |  |  |
| 8 | Maintain Payment Data | Add bank details using the Manage Business Partner app, and register payment card using the Manage Business Partner Master Data app.Make the following entry in the Payment Transactions tab:In Bank Details section enter:ID: 01Ctry: USBank Key: 011000390Bank Acct: <Bank Account>Swift Code (SWIFT/BIC): CITIUS33XXXChoose Submit. | The Checking Reconciliation Key view pops up. |  |
| 9 | Save | Choose Save. | A new business partner is created. |  |

#### Create Customer Master Data

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Context

In this activity, you extend a FI-CA business partner with BP role FLCU01 and MKK with sales area master data.

Procedures

| Test Step Number | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad with your user credentials as SAP_BR_APR_ACCOUNTANT_FICA | The SAP Fiori Launchpad is displayed. |  |
| 2 | Access the SAP Fiori App | Open Maintain Business Partner(BP). | The Maintain Business Partner screen is displayed. |  |
| 3 | Select Business Partner | Enter the Business Partner number |  |  |
| 4 | Open Business Partner | Choose Enter |  |  |
| 5 | Switch to Change Mode | Choose Switch Between Display and Change |  |  |
| 6 | Change in BP Role | In the Change in BP Role field, choose the following value: CustomerThe technical key of this BP role is FLCU01. |  |  |
| 7 | Input information for Address | Correspondence lang: <EN> |  |  |
| 8 | Open Sales Area | Choose Sales and Distribution at the top of the view. | The Sales Area view is displayed. |  |
| 9 | Enter Sales Area Data | Enter the following data:Sales Org: 1710Distr. Channel: 10Division: 00Choose Enter and then Save.Note The above three entries form the sales area. In many cases, the sales area sets the Purpose for sales processing, for example, within the sales order or pricing. | The changes are saved for the business partner. |  |
| 10 | Enter Shipping Data | On the Shipping tab in the Shipping section, enter the following data:Delivering Plant: 1710 |  |  |
| 11 | Enter Tax Data | On the Billing tab in the Output Tax section, enter the following data:Tax Classification: <1>For example, value <1> means that this customer is fully taxable. |  |  |
| 12 | Save Your Data | Save your entries. |  |  |
| 13 | Change in BP Role | In the Change in BP Role field, choose the following value: Contract PartnerThe technical key of this BP role is MKK. |  |  |
| 14 | Input Information for Address | Correspondence Lang: <EN> |  |  |
| 15 | Enter Shipping Data | On the Shipping tab page in the Shipping section, enter the following data:Delivering Plant: 1710 |  |  |
| 16 | Enter Tax Data | On the Billing tab page in the Output Tax section, enter the following data:Tax Classification: <1>For example, value <1> means that this customer is fully taxable. |  |  |
| 17 | Save Your Data | Save your entries. |  |  |

#### Create a Contract Account

Context

In this activity, you create a contract account master data for an FI-CA customer in SAP S/4HANA Cloud Public Edition.

Procedure

| Test Step Number | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad with your user credentials, using the Accounts Payable and Receivable Accountant (FI-CA) business role. | The SAP Fiori Launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Maintain Contract Account(CAA3). | The Contract Account Display: Initial Screen is displayed. |  |
| 3 | Create a Contract Account | Choose Create or select More > Contract Account > Create. | The Contract Account Create: Initial Screen is displayed. |  |
| 4 | Enter Basic Data | Make the following entry:Contract Acct: <Enter a specific ID>, for example, CA_US_97Business Partner: <Select Business Partner number created in Step Create a Business Partner>Cont. Acct. Cat.: Y1Valid From: <Today's Date> |  |  |
| 5 | Maintain Contract Account details | Choose Continue. | The Contract Account Create: General Data screen is displayed. |  |
| 6 | Enter General Data | Make the following entry in the General tab:Cont. Acct Name: <Contract Account name>Acct. Relation.: Account HolderTolerance Group: Y001 Tolerance not permittedPlanning Group: Domestic customersPayment cond.: YN01Act Determ. ID: Y1 |  |  |
| 7 | Enter Payments/Taxes Data | Make the following entry in the Payments/Taxes tab:Company Code Gp: 1710Standard CoCode: 1710 |  |  |
| 8 | Enter Dunning/Correspondence | Make the following entry in Dunning/Correspondence tab:Corresp. Variant: <only printout, immediately> |  |  |
| 9 | Save | Choose Save. | A new contract account is created. |  |

### Create Subscription Product (SAP Subscription Billing)

#### Create Rate Elements

Purpose

In this activity, you create rate elements in SAP Subscription Billing. The rate IDs must correspond with the relevant S/4HANA products of type SBRE:

| Rate ID | Rate Type | Description |
| --- | --- | --- |
| R-ONETIME | One-Time | One-Time Activation Fee |
| R-SEATS | Recurring | Seat-Based Monthly Fee |
| R-TICKETS | Usage-Based | Ticket-Based Usage Fee |

Procedure

| Test Step Number | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to SAP Subscription Billing. | The Home page appears. |  |
| 2 | Navigate to Rate Elements | Under Master Data and Configuration, choose Business Configuration > Rate Elements . | The Rate Elements view is displayed. |  |
| 3 | Create Rate Element: One-Time | Choose Create, then maintain the following data:Type: One-TimeID: R-ONETIMEUnit: Each (EA)Label: One-Time Activation FeeData Source: NoneOne-Time Type: Initial FeeBilling Type: ChargeDescription: Maintain a description, for example, One-Time Activation FeeActive: SelectedChoose Save. | The R-One-Time rate element is created. |  |
| 4 | Create Rate Element: R-SEATS | Choose Create, then maintain the following data:Type: RecurringID: R-SEATSUnit: Each (EA)Label: Seat-Based Monthly FeeData Source: SubscriptionBilling Type: ChargeDescription: Maintain a description, for example, Seat-Based Monthly FeeActive: SelectedChoose Save. | The R-SEATS rate element is created. |  |
| 5 | Create Rate Element: R-TICKETS | Choose Create, then maintain the following data:Type: Usage-BasedID: R-TICKETSUnit: Gigabyte(GB)/Each(EA)Label: Ticket-Based Usage FeeData Source: UsageBilling Type: ChargeUsage Rating Variant: AggregatedType of Technical Resource ID: Cloud Storage Space IDDescription: Maintain a description, for example, Upload/Download Traffic in GBActive: SelectedChoose Save. | The R-TICKETS rate element is created. |  |

#### Create Rate Plan Template

Purpose

In this activity you create a rate plan template in SAP Subscription Billing.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to SAP Subscription Billing. | The Home page appears. |  |
| 2 | Navigate to Rate Plan Templates | Under Pricing, open the Rate Plan Templates app. | The available rate plan templates are displayed. |  |
| 3 | Create Rate Plan Template: SEATS | Choose Create > Without Pricing Scheme , and maintain the following data in General Info:Description: Seat-Based Plan TemplateBilling Cycle: Value - Monthly on first day of monthCurrency: Value – USD (for country version US)Choose Add | The basic data for the template is defined. |  |
| 4 | Maintain Charges/Credits for SEATS | Create a one-time charge in the Charges/Credits section by choosing Add > One Time . Maintain the following data:Rate Element: R-ONETIMEPrice: Value - 9.99 USD (for country version US)Create a recurring charge in the Charges / Credits section by choosing Add > Recurring > Percentage Pricing . Maintain the following data:Rate Element: R-SEATSApply Changes with Next Cycle: SelectedBilling Advance: SelectedProrate First Cycle: SelectedPrice Per Unit : 1 USDRatio : 100Create a usage-based charge in the Charges / Credits section by choosing Add > Usage-Based > Block Pricing . Maintain the following data:Rate Element:R-TICKETSApply Changes with Next Cycle: Not SelectedIncluded Quantity: Value – 1Block Size: Value – 1Price per Block: Value – 1 USD (for country version US)Choose Save and Publish. | The Charges/Credits are created. |  |

#### Create Product (SAP Subscription Billing)

Purpose

In this activity you create products P-CLOUD_COMM and P-CLOUD_SUPPORT in SAP Subscription Billing. The ID of the product in SAP Subscription Billing must correspond to the relevant product ID in SAP S/4HANA

Procedure

Product: P-CLOUD_COMM

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to SAP Subscription Billing. | The Home page appears. |  |
| 2 | Navigate to Products | Under the Master Data and Configuration catalog, choose Business Configuration > Products . | The available products are displayed. |  |
| 3 | Maintain General Product Information | Choose Create, then maintain the following data in the General Info area:Product Name: Cloud CommunicationProduct ID: P-CLOUD_COMMSubscription Type: CommercialCreate Subscriptions as Pending: De-selectedSold Electronically: Selected | General information has been maintained. |  |
| 4 | Maintain Rate Plan for Product | In the Rate Plans area, choose Create Rate Plan from Template.On the Create Rate Plan view, maintain the following data:Market: US East (for country version US)Rate Plan Template: Seat-Based Plan TemplateDescription: Recurring Rate Plan (Seat-Based) | The product’s rate plan has been maintained. |  |
| 5 | Maintain Subscription Terms | Maintain the following subscription parameters details:Expected term: for example,12Minimum term: 12Renewal term: 12Withdrawal period: 14 | Subscription terms are maintained. |  |
| 6 | Create Product | On the Create Rate Plan view, choose Create.On the Product view, choose Save.Then choose Publish. | The P-CLOUD_COMM product is created. |  |

Product: P-CLOUD_SUPPORT

| Test Step Number | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to SAP Subscription Billing. | The Home page appears. |  |
| 2 | Navigate to Products | In the left-hand navigation area, choose Products. | The available products are displayed. |  |
| 3 | Maintain General Product Information | Choose Create, then maintain the following data in the General Info area:Product Name: Cloud SupportProduct ID: P-CLOUD_SUPPORTSubscription Type: CommercialCreate Subscriptions as Pending: De-selectedSold Electronically: Selected | General information has been maintained. |  |
| 4 | Maintain Rate Plan for Product | In the Rate Plans area, choose Create Rate Plan from Template.On the Create Rate Plan view, maintain the following data:Market: US East (for country version US)Rate Plan Template: Seat-Based Plan TemplateDescription: Recurring Rate Plan (Seat-Based) | The product’s rate plan has been maintained. |  |
| 5 | Maintain Subscription Terms | Maintain Subscription parameters details:Expected term: for example, 12Minimum term: 12Renewal term: 12Withdrawal period: 14 | Subscription terms are maintained. |  |
| 6 | Create Product | On the Create Rate Plan view, choose Create.On the Product view, choose Save.Then choose Publish. | The P-CLOUD_SUPPORT product is created. |  |

#### Create a Product for Price Calculation Services

When going through a sample use case, you can either use the sample values to create data from scratch, or you can use the predefined configuration that is delivered with every new tenant. You must execute the following steps in price calculation before creating a product for PCS.

Procedure

1. Manage Field Catalog

If you are using the sample data, a predefined field catalog is used in the Manage Field Catalog app. Thus, you need not make any additional settings here. The Manage Field Catalog app allows you to create fields that are later used for defining the lookup tables and input properties for price element specifications.

2. Create Lookup Tables

In the Manage Lookup Tables app, you can create lookup tables by mapping a set of input fields to a set of output fields. These lookup tables are then used in a later step to create price element specifications. The goal of this step is to create the following lookup tables for one-time, recurring, and usage fees:

- OneTimePrice
- RecurringPrice
- UsagePrice
- Discount1

These tables are part of the predefined content. Thus, you need not make any additional settings in this step.

3. Price Element Specifications

In the Manage Price Element Specifications app, you define your pricing configuration by creating price element specifications. This includes setting up the pricing logic and overridable fields:

- OneTimePrice
- RecurringPrice
- UsagePrice
- Discount1

These price element specifications are part of the predefined content. Thus, you need not make any additional settings in this step.

4. Pricing Scheme

In the Manage Pricing Scheme app, you create and maintain pricing schemes. A pricing scheme is a procedure that defines the usage and relationship of the price element specifications for a given priceable document. It also determines the sequence for executing these specifications to generate an overall amount in a priced document.

The pricing scheme 'Initial' is part of the predefined content. Thus, you need not make any additional settings in this step.

5. Create Rate Plan Template

| Test Step # | Test Step Name | Instructions | Expected Results | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to SAP Subscription Billing. | The Home page appears. |  |
| 2 | Navigate to the Rate Plan Templates app | Go to Pricing > Rate Plan Templates | The rate plan templates are displayed. |  |
| 3 | Choose Create | Choose Create - With Pricing Scheme and maintain the following data in General Info:Description: RPT for Price CalculationTags: PCS (Optional)Pricing Scheme: InitialBilling Cycle: Monthly on first day of the monthCurrency: USD | General information has been maintained. |  |
| 4 | Maintain Charges/Credits for rate elements | For one-time , choose Charges/Credits > Add > One Time and enter Rate Element = R-ONETIME.For recurring, choose Charges/Credits > Add > Recurring and enter Rate Element = R-SEATS.For usage, choose Charges/Credits > Add > Usage-Block Pricing and enter Rate Element = R-TRAFFIC.Choose Save and then Publish. |  |  |

6. Create Product

You create a product P-CLOUD_STORAGE_PC in SAP Subscription Billing. The ID of the product in SAP Subscription Billing must correspond to the relevant product ID in SAP S/4HANA. You can use the following procedure:

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to SAP Subscription Billing. | The Home page appears. |  |
| 2 | Navigate to Products | Under Master Data and Configuration, open the Products app. | The available products are displayed. |  |
| 3 | Maintain general product information | Choose Create and maintain the following data in the General Info area:Product Name: Cloud Storage Price CalculationProduct ID: P-CLOUD_STORAGE_PCSubscription Type: CommercialCreate Subscriptions as Pending: De-selected | General information has been maintained. |  |
| 4 | Maintain rate plan for product | On the Rate Plans tab, choose Create - With Pricing Scheme.Note For more information about price calculation products, refer to [SAP Subscription Billing with Pricing Schemes](https://help.sap.com/docs/CLOUD_TO_CASH_OD/3da4082dc5094e3489b7c98e9113cf6c/3542ae740bb046b9bf422e193f3e0526.html)Navigate to Create Rate Plan from Template > Create Rate Plan With Pricing Scheme and maintain the following data:Market: US East (for country version US)Rate Plan Template: RPT for Price CalculationDescription: RPT for Price CalculationBilling Cycle: Monthly on the first day of the monthChoose Create. | The rate plan has been maintained for the product. |  |
| 5 | Maintain Subscription Terms | Maintain the following data in the Subscription Terms area:Expected Term: for example, 12Minimum Term: 12Renewal Term: 12Withdrawal Period: 14 | Subscription terms are maintained. |  |
| 6 | Create product | On the Create Rate Plan view, choose Create.On the Product view, choose Save.Choose Publish. | The P-CLOUD_STORAGE_PC product is created. |  |

7. Upload Lookup Tables for Price Determination

For more information about uploading lookup tables, refer to Uploading Lookup Tables for Price Determination.

For more information about price calculation products, refer to [SAP Subscription Billing with Pricing Schemes](https://help.sap.com/docs/CLOUD_TO_CASH_OD/3da4082dc5094e3489b7c98e9113cf6c/3542ae740bb046b9bf422e193f3e0526.html)

#### Uploading Lookup Tables for Price Determination

You can upload your lookup tables for one-time, recurring, and usage-based fees and for the discount, using the following procedure. The data in the following table is used to find the relevant prices during price determination as part of the rating process.

Table 1: Upload One-Time Table

| Test Step # | Test Step Name | Instructions | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to SAP Price Calculation | The Home page appears. |  |
| 2 | Navigate to Rate Plan Templates | Under Master Data Management, open the Manage Lookup Table Data app. | The lookup tables are displayed. |  |
| 3 | Choose OneTimePrice | Choose the lookup table OneTimePrice.Download the empty table and store it locally as a CSV file.Tip If the format of the downloaded file is not column separated, you must change the format of the spreadsheet to a US format. |  |  |
| 4 | Update the downloaded file | Enter the following values and save the file:productCode: P-CLOUD_STORAGE_PCmarketId: A1rateElement: R-ONETIMEprice: Singleprice (Price Type): Fixedprice (Value): 5000price (Value Currency): USD |  |  |
| 5 | Upload the CSV file | Choose the lookup table OneTimePrice and go to Import > Browse to upload the saved file from the previous step.Note There are two types of imports. Choose Merge to keep the existing data intact.Click on Import. | The lookup table OneTimePrice is updated. |  |

Table 2: Upload Recurring Table

| Test Step # | Test Step Name | Instructions | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to SAP Price Calculation | The Home page appears. |  |
| 2 | Navigate to Rate Plan Templates | Under Master Data Management, open the Manage Lookup Table Data app. | The lookup tables are displayed. |  |
| 3 | Choose RecurringPrice | Choose the lookup table RecurringPrice.Download the empty table and store it locally as a CSV file.Tip If the format of the downloaded file is not column separated, you must change the format of the spreadsheet to a US format. |  |  |
| 4 | Update the downloaded file | Enter the following values and save the file:productCode: P-CLOUD_STORAGE_PCmarketId: A1rateElement: R-SEATSprice: Singleprice (Price Type): Linearprice (Value): 50price (Value Currency): USDprice (Quantity Value): 1price (Quantity Unit): EA |  |  |
| 5 | Upload the CSV file | Choose the lookup table RecurringPrice and go to Import > Browse to upload the saved file from the previous step.Note There are two types of imports. Choose Merge to keep the existing data intact.Click on Import. | The lookup table RecurringPrice is updated. |  |

Table 3: Upload Usage Table

| Test Step # | Test Step Name | Instructions | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to SAP Price Calculation | The Home page appears. |  |
| 2 | Navigate to Rate Plan Templates | Under Master Data Management, open the Manage Lookup Table Data app. | The lookup tables are displayed. |  |
| 3 | Choose UsagePrice | Choose the lookup table OneTimePrice.Download the empty table and store it locally as a CSV file.Tip If the format of the downloaded file is not column separated, you must change the format of the spreadsheet to a US format. |  |  |
| 4 | Update the downloaded file | Enter the following values and save the file:productCode: P-CLOUD_STORAGE_PCmarketId: A1rateElement: R-TRAFFICprice: Volumeprice (Price Type): LinearThe following specific values are available for each tier for a high-rate sub element:rateSubElement: Highprice (Range): 500price (Range Unit): EAprice (Value): 30price (Value Currency): USDprice (Quantity Value): 1price (Quantity Unit): EAThe following specific values are available for each tier:rateSubElement: Highprice (Range): 1000price (Range Unit): EAprice (Value): 25price (Value Currency): USDprice (Quantity Value): 1price (Quantity Unit): EAThe following specific values are available for each tier:rateSubElement: Highprice (Range):price (Range Unit): EAprice (Value): 20price (Value Currency): USDprice (Quantity Value): 1price (Quantity Unit): EAThe following specific values are available for each tier for a low-rate sub element:rateSubElement: Lowprice (Range): 500price (Range Unit): EAprice (Value): 15price (Value Currency): USDprice (Quantity Value): 1price (Quantity Unit): EAThe following specific values are available for each tier for a low-rate sub element:rateSubElement: Lowprice (Range): 1000price (Range Unit): EAprice (Value): 10price (Value Currency): USDprice (Quantity Value): 1price (Quantity Unit): EAThe following specific values are available for each tier for a low-rate sub element:rateSubElement: Lowprice (Range):price (Range Unit): EAprice (Value): 5price (Value Currency): USDprice (Quantity Value): 1price (Quantity Unit): EA |  |  |
| 5 | Upload the CSV file | Choose the lookup table OneTimePrice and go to Import > Browse to upload the saved file from the previous step.Note There are two types of imports. Choose Merge to keep the existing data intact.Click on Import.. | The lookup table OneTimePrice is updated. |  |

Table 4: Upload Discount Table

| Test Step # | Test Step Name | Instructions | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to SAP Price Calculation | The Home page appears. |  |
| 2 | Navigate to Rate Plan Templates | Under Master Data Management, open the Manage Lookup Table Data app. | The lookup tables are displayed. |  |
| 3 | Choose Discount1 | Choose the lookup table Discount1.Download the empty table and store it locally as a CSV file.Tip If the format of the downloaded file is not column separated, you must change the format of the spreadsheet to a US format. |  |  |
| 4 | Update the downloaded file | Enter the following values and save the file:marketId: A1discount: Singlediscount (Price Type): Percentagediscount (value): 0.1 |  |  |
| 5 | Upload the CSV file | Choose the lookup table Discount1 and go to Import > Browse to upload the saved file from the previous step.Note There are two types of imports. Choose Merge to keep the existing data intact.Click on Import.. | The lookup table Discount1 is updated. |  |

### Enrich Subscription Billing Products

#### Enhance Subscription Product of Type SBPD

Purpose

In this activity, you enhance the subscription products P-CLOUD_COMM and P-CLOUD_SUPPORT in SAP S/4HANA. These products are created in SAP Subscription Billing and replicated to SAP S/4HANA.

Procedure

Product: P-CLOUD_COMM

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as a Master Data Specialist - Product Data. | The Home page appears. |  |
| 2 | Access the SAP Fiori app | Choose the Manage Product Master Data tile. | The Manage Product Master Data app appears. |  |
| 3 | Find Product P-CLOUD_COMM | In the search area on the top,enter the Product:P-CLOUD_COMM.Press the button Go. | Your product is displayed in the report list. |  |
| 4 | Open Product and Maintain Distribution Chains: General Information | Choose the Product from the report list,Product Number: P-CLOUD_COMMBase Unit: EAProduct Type: SBPD (Sub. Billing Product)Then choose OK.Note In Description provide the Language and Product details for specific region, for example, Language: English and Product: Subscription Billing Product. | The product should be open and general information is maintained. |  |
| 5 | Maintain Distribution Chains: General Information | On the Product view, in the Distribution Chains area, choose Create and maintain the following data:Sales Organization: 1710 (Dom. Sales Org US)Distribution Channel: 10 (Direct Sales)Note Distribution Chain is not required for SBPD product type if you are using MDI. Only required if you are using Cloud Integration. | Grouping terms are maintained and the product is saved. | For country version Germany, maintain the following value instead of 1 (Full Tax):Tax Classification: 6 (Full Tax (Services))The other entries are the same for both countries. |
| 6 | Maintain Distribution Chains: Grouping Terms | Navigate to the Grouping Terms area and maintain the following data:Item Category Group: SBPD (Sub. Billing Product)Account Assignment Group: X9 (Periodic Service)Tax Classification: 1 (Full Tax)Then choose Apply and then Create.Note Item category group is required only if you are using Cloud Integration and not Master Data Integration for replication |  |  |
| 7 | Maintain Plants | Navigate to the Plants area, choose Create and maintain the following data:Plant: 1710 (Plant US)Then choose Apply and then Save | Plant data is maintained. |  |

Product: P-CLOUD_SUPPORT

| Test Step Number | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as a Master Data Specialist - Product Data. | The Home page appears. |  |
| 2 | Access the SAP Fiori app | Choose the Manage Product Master Data tile. | The Manage Product Master Data app appears. |  |
| 3 | Find Product P-CLOUD_SUPPORT | In the search area on the top,enter the Product: P-CLOUD_SUPPORTPress the button Go. | Your product is displayed in the report list. |  |
| 4 | Open Product and Maintain Distribution Chains: General Information | Choose the Product from the report list,Product Number: P-CLOUD_COMMBase Unit: EAProduct Type: SBPD (Sub. Billing Product)Then choose OK.Note In Description provide the Language and Product details for specific region, for example, Language: English and Product: Subscription Billing Product. | The product should be open and general information is maintained. |  |
| 5 | Maintain Distribution Chains: General Information | On the Product view, in the Distribution Chains area, choose Create and maintain the following data:Sales Organization: 1710 (Dom. Sales Org US)Distribution Channel: 10 (Direct Sales)Note Distribution Chain is not required for SBPD product type if you are using Master Data Integration. Only required if you are using Cloud Integration. | Grouping terms are maintained and the product is saved. | For country version Germany, maintain the following value instead of 1 (Full Tax):Tax Classification: 6 (Full Tax (Services))The other entries are the same for both countries. |
| 6 | Maintain Distribution Chains: Grouping Terms | Navigate to the Grouping Terms area and maintain the following data:Item Category Group: SBPD (Sub. Billing Product)Account Assignment Group: X9 (Periodic Service)Tax Classification: 1 (Full Tax)Then choose Apply and then Create.Note Distribution Chain is not required for SBPD product type if you are using Master Data Integration and Only required if you are using Cloud Integration. |  |  |
| 7 | Maintain Plants | Navigate to the Plants area, choose Create and maintain the following data:Plant: 1710 (Plant US)Then choose Apply and then Save | Plant data is maintained. |  |

#### Enhance Subscription Products of Type SBRE

Purpose

In this activity, you enhance the following subscription products in SAP S/4HANA. These products are created in SAP Subscription Billing and replicated to SAP S/4HANA.

| Product ID | Product Type | Description |
| --- | --- | --- |
| R-ONETIME | SBRE | One-Time Activation Fee |
| R-SEATS | SBRE | Seat-based monthly fee |
| R-TICKETS | SBRE | Ticket-Based Usage Fee |

Procedure

Product: R_ONETIME

| Test Step Number | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as a Master Data Specialist - Product Data. | The Home page appears. |  |
| 2 | Access the SAP Fiori app | Choose the Manage Product Master Data tile. | The Manage Product Master Data app appears. |  |
| 3 | Find Product R_ONETIME | In the search area, enter the Product:R-ONETIMEClick on Go. | Your product is displayed in the report list. |  |
| 4 | Open Product and Maintain Distribution Chains: General Information | On the Product view, in the Distribution Chains area, choose Create and maintain the following data:Sales Organization: 1710 (Dom. Sales Org US)Distribution Channel: 10 (Direct Sales)Cash Discount: YesNote In Description provide the Language and Product details for specific region, for example, Language: English and Product: Subscription Billing Product. | The product should be open and general information is maintained. | For country version Germany, maintain the following value instead of 1710:Sales Organization: 1010 (Dom. Sales Org DE)The other entries are the same for both countries. |
| 5 | Maintain Distribution Chains: Grouping Terms | Navigate to the Grouping Terms area and maintain the following data:Account Assignment Group: X9 (Periodic Service)Tax Classification: 1 (Full Tax)Then choose Apply. | Grouping terms are maintained and the product is saved. | For country version Germany, maintain the following value instead of 1 (Full Tax):Tax Classification: 6 (Full Tax (Services))The other entries are the same for both countries. |
| 6 | Maintain Plants | Navigate to the Plants area, choose Create and maintain the following data:Plant: 1710 (Plant US)Then choose Apply and then Create. | Plant data is maintained. |  |

Product: R_SEATS

| Test Step Number | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as a Master Data Specialist - Product Data. | The Home page appears. |  |
| 2 | Access the SAP Fiori app | Choose the Manage Product Master Data tile. | The Manage Product Master Data app appears. |  |
| 3 | Find Product R_SEATS | In the search area, enter the Product:R-SEATSClick on Go. | Your product is displayed in the report list. |  |
| 4 | Open Product and Maintain Distribution Chains: General Information | Choose the product from the report list.On the Product view, click on Edit.In the Distribution Chains area, choose Create and maintain the following data:Sales Organization: 1710 (Dom. Sales Org US)Distribution Channel: 10 (Direct Sales)Note In Description provide the Language and Product details for specific region, for example, Language: English and Product: Subscription Billing Product. | The product should be open and general information is maintained. | For country version Germany, maintain the following value instead of 1710:Sales Organization: 1010 (Dom. Sales Org DE)The other entries are the same for both countries. |
| 5 | Maintain Distribution Chains: Grouping Terms | Navigate to the Grouping Terms area and maintain the following data:Item Category Group: SBRE (Sub. Billing Rate Element)Account Assignment Group: X9 (Periodic Service)Tax Classification: 1 (Full Tax)Then choose Apply. | Grouping terms are maintained and the product is saved. | For country version Germany, maintain the following value instead of 1 (Full Tax):Tax Classification: 6 (Full Tax (Services))The other entries are the same for both countries. |
| 6 | Maintain Plants | Navigate to the Plants area, choose Create and maintain the following data:Plant: 1710 (Plant US)Then choose Apply and Save. | Plant data is maintained. |  |

Product: R_TICKETS

| Test Step Number | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as a Master Data Specialist - Product Data. | The Home page appears. |  |
| 2 | Access the SAP Fiori app | Choose the Manage Product Master Data tile. | The Manage Product Master Data app appears. |  |
| 3 | Find Product R_TICKETS | In the search area, enter the Product:R-TICKETSClick on Go. | Your product is displayed in the report list. |  |
| 4 | Open Product and Maintain Distribution Chains: General Information | Choose the product from the report list.On the Product view, click on Edit.In the Distribution Chains area, choose Create and maintain the following data:Sales Organization: 1710 (Dom. Sales Org US)Distribution Channel: 10 (Direct Sales)Note In Description provide the Language and Product details for specific region, for example, Language: English and Product: Subscription Billing Product. | The product should be open and general information is maintained. | For country version Germany, maintain the following value instead of 1710:Sales Organization: 1010 (Dom. Sales Org DE)The other entries are the same for both countries. |
| 5 | Maintain Distribution Chains: Grouping Terms | Navigate to the Grouping Terms area and maintain the following data:Account Assignment Group: X9 (Periodic Service)Tax Classification: 1 (Full Tax)Then choose Apply. | Grouping terms are maintained and the product is saved. | For country version Germany, maintain the following value instead of 1 (Full Tax):Tax Classification: 6 (Full Tax (Services))The other entries are the same for both countries. |
| 6 | Maintain Plants | Navigate to the Plants area, choose Create and maintain the following data:Plant: 1710 (Plant US)Then choose Apply and Save. | Plant data is maintained. |  |

## Appendix

Table 5: Typographic Conventions

| Type Style | Description |
| --- | --- |
| Example | Words or characters quoted from the screen.These include field names, screen titles, pushbuttons labels, menu names, menu paths, and menu options.Textual cross references to other documents. |
| Example | Emphasized words or expressions. |
| Example | Technical names of system objects.These include report names, program names, transaction codes, table names, and key concepts of a programming language when they are surrounded by body text, for example, SELECT and INCLUDE. |
| Example | Output on the screen.This includes file and directory names and their paths, messages, names of variables and parameters, source text, and names off installation, upgrade, and database tools. |
| Example | Exact user entry.These are words or characters that you enter in the system exactly as they appear in the documentation. |
| <Example> | Variable user entry.Angle brackets indicate that you replace these words and characters with appropriate entries to make entries in the system. |
| Example | Keys on the keyboard, for example, F2 or ENTER. |

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
> Flagged while digesting this document, not verified: Internal inconsistencies: the usage rate element is R-TICKETS but the price calculation template and UsagePrice lookup use R-TRAFFIC; P-CLOUD_SUPPORT enrichment step 4 names Product Number P-CLOUD_COMM; SBRE procedure headings use R_ONETIME/R_SEATS/R_TICKETS versus R-... IDs.

## Connections
- part-of :: [[_cluster]]
- related-to :: [[09-subscription-billing-and-contract-accounting/mds-5lp-451]]
- related-to :: [[09-subscription-billing-and-contract-accounting/sap-s-4hana-cloud-public-edition-convergent-invoicing-mds-5lp-453]]
- related-to :: [[09-subscription-billing-and-contract-accounting/script-de-dados-mestre-criar-faturamento-convergente-de-produto-de-ass]]
- related-to :: [[09-subscription-billing-and-contract-accounting/script-de-datos-maestros-creacion-de-facturacion-convergente-de-produc]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/5LP_S4CLD2608_Master_Data_EN_XX.docx` — full document · extracted with `mammoth` · 44,041 chars in the whole document
