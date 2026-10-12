---
id: 09-subscription-billing-and-contract-accounting/master-data-script-create-subscription-product-sales-billing-mds-5bd-4
title: "Master Data Script: Create Subscription Product Sales Billing - MDS (5BD) (5BD_S4CLD2608_Master_Data_EN_XX)"
description: "SAP S/4HANA Cloud Public Edition 2608 master data script (5BD): create subscription products and rate elements in SAP Subscription Billing, then enrich them in S/4HANA."
cluster: 09-subscription-billing-and-contract-accounting
tags: [kb/subscription-billing-and-contract-accounting, topic/subscription-product-master-data]
aliases: [5BD_S4CLD2608_Master_Data_EN_XX]
keywords: [Subscription Products and Rate Plans, subscription products, rate elements, rate plan templates, pricing schemes, lookup tables, product master data, sbpd products, sbre products, organizational units]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/5BD_S4CLD2608_Master_Data_EN_XX.docx]
confidence: low
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-425
topic: 09-subscription-billing-and-contract-accounting/subscription-product-master-data
language: EN
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Master Data Script: Create Subscription Product Sales Billing - MDS (5BD) (5BD_S4CLD2608_Master_Data_EN_XX)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/5BD_S4CLD2608_Master_Data_EN_XX.docx`, extracted with `mammoth`. Grouped under **Subscription Products and Rate Plans** in Subscription Billing and Contract Accounting. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

|  |  |
| --- | --- |
| <!-- image omitted: unnamed --> | Master Data ScriptSAP S/4HANA Cloud Public Edition - 02-07-26 |
|  | Create Subscription Product Sales Billing - MDS (5BD) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Table of Contents

[1 Purpose 2](#_Toc233904746)

[2 Prerequisites 3](#_Toc233904747)

[2.1 System Access 3](#_Toc233904748)

[2.2 Roles 3](#_Toc233904749)

[2.3 Required Organizational Units (SAP S/4HANA) 3](#_Toc233904750)

[3 Overview Table 4](#_Toc233904751)

[4 Procedures 5](#_Toc233904752)

[4.1 Create Subscription Product (SAP Subscription Billing) 5](#_Toc233904753)

[4.1.1 Create Rate Elements 5](#_Toc233904754)

[4.1.2 Create Rate Plan Template 7](#_Toc233904755)

[4.1.3 Create a Product 8](#_Toc233904756)

[4.1.4 Create a Product with a Pricing Scheme 9](#_Toc233904757)

[4.1.5 Uploading Lookup Tables for Price Determination 12](#_Toc233904758)

[4.2 Enrich Subscription Products (SAP S/4HANA) 17](#_Toc233904759)

[4.2.1 Enhance Subscription Billing Products of Type SBPD 17](#_Toc233904760)

[4.2.2 Enhance Subscription Billing Products of Type SBRE 19](#_Toc233904761)

## Purpose

In this document you find a description of how to create subscription product master data. The description includes those data segments that are relevant for the master data to work in a "usual" system environment. The reader mainly learns which data segments and fields usually need to be filled with input values. Fields that are not relevant for the scope are not described in this document although they may appear on the UI.

A subscription master record that is created as described here can be used for subscription billing.

| Subscription Product ID | Description | Usage |
| --- | --- | --- |
| P-CLOUD_STORAGE | Subscription product | Represents the subscription billing product |
| P-CLD_STORAGE_PCS | Price Calculation Services product | Represents the price calculation product |

## Prerequisites

### System Access

| System | Details |
| --- | --- |
| SAP S/4HANA System | Accessible via SAP Fiori Launchpad. Your system administrator provides you with the URL to access the various apps assigned to your role. |
| SAP Subscription Billing | Accessible via URL. Your system administrator provides you with the URL to access the application. |
| Price Calculation Service | Accessible via SAP Fiori Launchpad. Your system administrator provides you with the URL to access the various apps assigned to your role. |

### Roles

Create business roles using the following business role templates delivered by SAP and assign them to your individual test users.

SAP S/4HANA

| Name | ID |
| --- | --- |
| Master Data Specialist - Product Data | SAP_BR_PRODMASTER_SPECIALIST |

SAP Subscription Billing

Contact your system administrator for authorization set-up.

### Required Organizational Units (SAP S/4HANA)

Some segments of master data are dependent on the organizational units of the company, General (Central) Data does not depend on an organizational unit or the company code. The following table gives an overview of these different data segments and their relevant organizational units:

| Data Segment | Depends On | Organizational Unit to be Used | Organizational Unit to be Used |
| --- | --- | --- | --- |
| Create Master Data Record | Sales Organization | 1710 (Dom. Sales Org US) | For Germany, use 1010 (Dom. Sales Org DE) |
| Create Master Data Record | Distribution Channel | 10 (Direct Sales) | 10 (Direct Sales) |

## Overview Table

This master record consists of several segments provided in the table below.

| Segment | Business Role | App/Transaction | Expected Results |
| --- | --- | --- | --- |
| Create Subscription Product (SAP Subscription Billing) | N/A | N/A | Subscription products are created. |
| Create Subscription Products (SAP S/4HANA) | SAP_BR_PRODMASTER_SPECIALIST | Manage Product Master Data | Subscription products are created. |

## Procedures

This section describes procedures for each segment or process step that is part of this master record.

### Create Subscription Product (SAP Subscription Billing)

#### Create Rate Elements

Purpose

In this activity you create rate elements in SAP Subscription Billing. The rate IDs must correspond with the relevant S/4HANA products of type SBRE:

| Rate ID | Rate Type | Description |
| --- | --- | --- |
| R-ONETIME | One-Time | One-Time Activation Fee |
| R-SEATS | Recurring | Seat-Based Monthly Fee |
| R-TRAFFIC | Usage-Based | Traffic-Based Usage Fee |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to SAP Subscription Billing Launchpad. | The Home page appears. |  |
| 2 | Navigate to Rate Elements | Under Master Data and Configuration , Choose Manage Business Configuration > Rate Elements . | The Rate Elements view is displayed. |  |
| 3 | Create Rate Element: R-ONETIME | Choose Create > One-Time and then maintain the following data:ID: R-ONETIMEUnit: Each (EA)Label: One-Time Activation FeeData Source: NoneOne-Time Type: Initial FeeBilling Type: ChargeDescription: Maintain a description, for example, One-Time Activation FeeActive: SelectedChoose Save. | The R-ONETIME rate element is created. |  |
| 4 | Create Rate Element: R-SEATS | Choose Create, then maintain the following data:Type: RecurringID: R-SEATSUnit: Each (EA)Label: Seat-Based Monthly FeeData Source: SubscriptionBilling Type: ChargeDescription: Maintain a description, for example, Seat-Based Monthly FeeActive: SelectedChoose Save. | The R-SEATS rate element is created. |  |
| 5 | Create Rate Element: R-TRAFFIC | Choose Create, then maintain the following data:Type: Usage-BasedID: R-TRAFFICUnit: EACH (EA)Label: Traffic-Based Usage FeeData Source: UsageBilling Type: ChargeUse Rate Subelements: Selected (only for PCS products)Usage Rating Variant: AggregatedType of Technical Resource ID: Cloud Storage Space IDDescription: Maintain a description, for example, Upload/Download TrafficActive: SelectedChoose Save. | The R-TRAFFIC rate element is created. |  |

|  |
| --- |
| Note Technical resources identify the subscriber and the subscribed service in a technical system. They are needed when you bill your customers based on the usage of your service. For example, measuring electricity consumption, Here, the Type of Technical Resource ID: could be defined as the ‘Electricity Meter ID’, which is the unique ID (for example, EM392734-A) against which the usage is posted. In a scenario where mileage is being measured, the Type of Technical Resource ID: could be defined as the ‘Car License Number’.This is a user input field and is defined according to the service/scenario. |

#### Create Rate Plan Template

Purpose

In this activity you create a rate plan template in SAP Subscription Billing.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to SAP Subscription Billing. | The Home page appears. |  |
| 2 | Navigate to Rate Plan Templates | Under Pricing, choose Manage Rate Plan Templates app. | The available rate plan templates are displayed. |  |
| 3 | Create Rate Plan Template: | Choose Create > Without Pricing Scheme and maintain the following data in General Info:Description: Seat-Based Plan TemplateBilling Cycle: Monthly on first day of monthCurrency: Value – USD (for country version US) | The Rate Plan Template screen is displayed. |  |
| 4 | Maintain Charges / Credits for Rate Elements | In the Charges / Credits section, choose Charges / Credits, choose Add and choose One-Time.Then maintain the following data:Rate Element: R-ONETIMEPrice Value: 100 USDFor Charges / Credits, choose Create and choose Recurringand then choose, Percentage Pricing Charge.Then maintain the following data:Rate Element: R-SEATSApply Changes with Next Cycle: SelectedBilling Advance: SelectedProrate First Cycle: SelectedPrice Per Unit : 10 USDRatio : 100For Charges / Credits, choose Add and then choose UsageBlock Pricing.Then maintain the following data:Rate Element: R-TRAFFICRate Subelement: Maintain Rate Subelementif the Use Rate Subelements option is enabled in the [Create Rate Elements](#unique_7) [page ] 5 step.Note Rate Subelementis a mandatory field if the Use Rate Subelements option is enabled.Apply Changes with Next Cycle: Not SelectedIncluded Quantity: Value – 1Block Size: Value – 1Price per Block: Value – 1 USD (for country version US)Choose Create.Then choose Publish. | The Charges / Credits are created. |  |

#### Create a Product

Purpose

In this activity you create a product P-CLOUD_STORAGE in SAP Subscription Billing. The ID of the product in SAP Subscription Billing must correspond to the relevant product ID in SAP S/4HANA.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to SAP Subscription Billing. | The Home page appears. |  |
| 2 | Navigate to Products | Under Master Data and Configuration, open the Manage Products app. | The available products are displayed. |  |
| 3 | Maintain General Product Information | Choose Create and maintain the following data under General Info area:Product Name: Cloud StorageProduct ID: P-CLOUD_STORAGESubscription Type: CommercialCreate Subscriptions as Pending: De-selectedSubscription Profile: S/4 Integration | General information has been maintained. |  |
| 4 | Maintain Rate Plan for Product | Under Rate Plans, choose Create > Without Pricing Scheme and maintain the following data:.Note If you are using products that require a pricing scheme, you must choose With Pricing Scheme. For an overview of pricing with and without pricing schemes, see [Pricing](https://help.sap.com/docs/subscription-billing/feature-overview/pricing) in the SAP Subscription Billing documentation.Market: US East (for country version US)Rate Plan Template: Seat-Based Plan TemplateDescription: Recurring Rate Plan (Seat-Based)Billing Cycle : Monthly on first day of monthChoose Create. | The rate plan has been maintained for the product. |  |
| 5 | Maintain Subscription Terms | Under Subscription Terms, maintain the following:Expected term: for example, 12Minimum term: 12Renewal term: 12Withdrawal period: 14 | Subscription terms are maintained. |  |
| 6 | Create Product | For the entire product, choose Create.Then choose Publish. | The P-CLOUD_STORAGE product is created. |  |

#### Create a Product with a Pricing Scheme

When going through a sample use case, you can either use the sample values to create data from scratch, or you can use the predefined configuration that is delivered with every new tenant. You must execute the following steps in Price Calculation service before creating a product with a pricing scheme.

You can find a detailed description of how to set up pricing with pricing schemes (using an example) in the [Pricing with Pricing Schemes Configuration Guide](https://help.sap.com/docs/subscription-billing/pricing-configuration/pricing-with-pricing-schemes-configuration-guide).

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

|  |
| --- |
| Note If the price element specifications for the above elements are not maintained, you must maintain them in the Manage Price Element Specifications app by choosing the individual elements Overridable Fields > Add/Create > Price/Discount > Save . |

4. Pricing Scheme

In the Manage Pricing Schemes app, you create and maintain pricing schemes. A pricing scheme is a procedure that defines the usage and relationship of the price element specifications for a given priceable document. It also determines the sequence for executing these specifications to generate an overall amount in a priced document.

The pricing scheme 'Initial' is part of the predefined content. Thus, you need not make any additional settings in this step.

5. Create Rate Plan Template

| Test Step # | Test Step Name | Instructions | Expected Results | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to SAP Subscription Billing. | The Home page appears. |  |
| 2 | Navigate to the Rate Plan Templates app | Go to Pricing > Manage Rate Plan Templates | The rate plan templates are displayed. |  |
| 3 | Choose Create | Choose Create > With Pricing Scheme and maintain the following data in General Info:Description: RPT for Price CalculationTags: PCS (Optional)Pricing Scheme: InitialBilling Cycle: Monthly on first day of the monthBilling Profile: Initial SettingsCurrency: USD | General information has been maintained. |  |
| 4 | Maintain Charges/Credits for rate elements | For one-time, choose Charges/Credits > Create > One-Time and enter Rate Element = R-ONETIME.Choose Overridable Fields Details > Create > Discount 1 and enter One-Time Price = Select. Choose Apply.For recurring, choose Charges/Credits > Create > Recurring and enter Rate Element = R-SEATS.Choose Overridable Fields Details > Create > Discount 1 and enter Recurring Price = Select. Choose Apply.For usage, choose Charges/Credits > Create > Usage-Block Pricing and enter Rate Element = R-TRAFFICand Rate Subelement.Note Rate Subelementis a mandatory field if the Use Rate Subelements option is enabled in the [Create Rate Elements](#unique_7) [page ] 5 step.Choose Overridable Fields Details > Create > Discount 1 and enter Usage-Based Price = Select. Choose Apply.Choose Create and then Publish. |  |  |

6. Create Product

You create a product P-CLOUD_STORAGE_PC in SAP Subscription Billing. The ID of the product in SAP Subscription Billing must correspond to the relevant product ID in SAP S/4HANA. You can use the following procedure:

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to SAP Subscription Billing. | The Home page appears. |  |
| 2 | Navigate to Products | Under Master Data and Configuration, open the Manage Products app. | The available products are displayed. |  |
| 3 | Maintain general product information | Choose Create and maintain the following data in the General Info area:Product Name: Cloud Storage Price CalculationProduct ID: P-CLOUD_STORAGE_PCSubscription Type: CommercialCreate Subscriptions as Pending: De-selected | General information has been maintained. |  |
| 4 | Maintain rate plan for product | On the Rate Plans tab, choose Create - > With Pricing SchemeNavigate to Create Template and maintain the following data:Market: US East (for country version US)Rate Plan Template: RPT for Price CalculationDescription: RPT for Price CalculationBilling Cycle: Monthly on the first day of the monthChoose Create. | The rate plan has been maintained for the product. |  |
| 5 | Maintain Subscription Terms | Under Subscription Parameters, maintain the following data in the Subscription Terms area:Expected Term: for example, 12Minimum Term: 12Renewal Term: 12Withdrawal Period: 14 | Subscription terms are maintained. |  |
| 6 | Create product | On the Product view, choose Create.Choose Publish. | The P-CLOUD_STORAGE_PC product is created. |  |

7. Upload Lookup Tables for Price Determination

For more information about uploading lookup tables, refer to [Uploading Lookup Tables for Price Determination](#unique_11) [page ] 12.

#### Uploading Lookup Tables for Price Determination

You can upload your lookup tables for one-time, recurring, and usage-based fees and for the discount, using the following procedure. The data in the resulting table is used to find the relevant prices during price determination as part of the rating process.

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
| 3 | Choose UsagePrice | Choose the lookup table UsagePrice.Download the empty table and store it locally as a CSV file.Tip If the format of the downloaded file is not column separated, you must change the format of the spreadsheet to a US format. |  |  |
| 4 | Update the downloaded file | Enter the following values and save the file:productCode: P-CLOUD_STORAGE_PCmarketId: A1rateElement: R-TRAFFICprice: Volumeprice (Price Type): LinearThe following specific values are available for each tier for a high-rate sub element:rateSubElement: Highprice (Range): 500price (Range Unit): EAprice (Value): 30price (Value Currency): USDprice (Quantity Value): 1price (Quantity Unit): EAThe following specific values are available for each tier:rateSubElement: Highprice (Range): 1000price (Range Unit): EAprice (Value): 25price (Value Currency): USDprice (Quantity Value): 1price (Quantity Unit): EAThe following specific values are available for each tier:rateSubElement: Highprice (Range):price (Range Unit): EAprice (Value): 20price (Value Currency): USDprice (Quantity Value): 1price (Quantity Unit): EAThe following specific values are available for each tier for a low-rate sub element:rateSubElement: Lowprice (Range): 500price (Range Unit): EAprice (Value): 15price (Value Currency): USDprice (Quantity Value): 1price (Quantity Unit): EAThe following specific values are available for each tier for a low-rate sub element:rateSubElement: Lowprice (Range): 1000price (Range Unit): EAprice (Value): 10price (Value Currency): USDprice (Quantity Value): 1price (Quantity Unit): EAThe following specific values are available for each tier for a low-rate sub element:rateSubElement: Lowprice (Range):price (Range Unit): EAprice (Value): 5price (Value Currency): USDprice (Quantity Value): 1price (Quantity Unit): EA |  |  |
| 5 | Upload the CSV file | Choose the lookup table UsagePrice and go to Import > Browse to upload the saved file from the previous step.Note There are two types of imports. Choose Merge to keep the existing data intact.Click on Import. | The lookup table UsagePrice is updated. |  |

Table 4: Upload Discount Table

| Test Step # | Test Step Name | Instructions | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to SAP Price Calculation | The Home page appears. |  |
| 2 | Navigate to Rate Plan Templates | Under Master Data Management, open the Manage Lookup Table Data app. | The lookup tables are displayed. |  |
| 3 | Choose Discount1 | Choose the lookup table Discount1.Download the empty table and store it locally as a CSV file.Tip If the format of the downloaded file is not column separated, you must change the format of the spreadsheet to a US format. |  |  |
| 4 | Update the downloaded file | Enter the following values and save the file:marketId: A1discount: Singlediscount (Price Type): Percentagediscount (value): 0.1 |  |  |
| 5 | Upload the CSV file | Choose the lookup table Discount1 and go to Import > Browse to upload the saved file from the previous step.Note There are two types of imports. Choose Merge to keep the existing data intact.Click on Import. | The lookup table Discount1 is updated. |  |

### Enrich Subscription Products (SAP S/4HANA)

#### Enhance Subscription Billing Products of Type SBPD

Purpose

In this activity, you enhance the subscription billing product P-CLOUD_STORAGE in SAP S/4HANA. This product is created in Subscription Billing, replicated to SAP S/4HANA, and is available once the replication of products is set up as part of the scope item 57Z. For more information about replication of products, refer to [Configure IFlow Package for Replication of Products and Rate Elements](https://help.sap.com/docs/CLOUD_TO_CASH_OD/a78a4be305be4dbc903bd826a1aba456/93e79ab9ec8e4dc49bc1710e396608ed.html).

|  |
| --- |
| Note Brazil-specific fields require a proper tax calculation. For more information about this, refer to Material Master Data > Define BR Specific Fields for Master Data > Create Master Data for Brazil (JD0_BR) . |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as a Master Data Specialist - Product Data. | The Home page appears. |  |
| 2 | Access the SAP Fiori app | Choose the Manage Product Master Data tile. | The Manage Product Master Data app appears. |  |
| 3 | Find the Product | In the search area on the top, enter the Product: P-CLOUD_ STORAGE and P-CLOUD_ STORAGE_PC.Choose Go. | Your product is displayed in the report list. |  |
| 4 | Open Product and Maintain Distribution Chains: General Information | Choose the product from the report list,Product Number: P-CLOUD_STORAGEBase Unit: EAProduct Type: SBPD (Sub. Billing Product)Description: Cloud StorageThen choose OK.Note In Description provide the Language and Product details for specific region, for example, Language: English and Product: Subscription Billing Product. | The product should be open and general information is maintained. |  |
| 5 | Maintain Distribution Chains: General Information | On the Product view, in the Distribution Chains area, choose Create and maintain the following data:Sales Organization: 1710 (Dom. Sales Org US)Distribution Channel: 10 (Direct Sales)Note The distribution chain is not required for the SBPD product type if you are using MDI. They are only required if you are using Cloud Integration. |  | For country version Germany, maintain the following value instead of 1710:Sales Organization: 1010 (Dom. Sales Org DE)The other entries are the same for both countries |
| 6 | Maintain Distribution Chains: Grouping Terms | Navigate to the Grouping Terms area and maintain the following data:Item Category Group: SBPD (Sub. Billing Product)Account Assignment Group: X9 (Periodic Service)Tax Classification: 1 (Full Tax)Then choose Apply > Create .Note The item category group is not required for the SBPD product type if you are using MDI. This is only required if you are using Cloud Integration. | Grouping terms are maintained and the product is saved. | For country version Germany, maintain the following value instead of 1 (Full Tax):Tax Classification: 6 (Full Tax (Services))The other entries are the same for both countries. |
| 7 | Maintain Plants | Navigate to Plants > Create and maintain the following data:Plant: 1710 (Plant US)Choose Apply > Save . | Plant data is maintained. |  |

#### Enhance Subscription Billing Products of Type SBRE

Purpose

In this activity you enhance the following subscription products in SAP S/4HANA that correspond to rate elements in SAP Subscription Billing: The products are created in Subscription Billing and replicated to SAP S/4HANA. The Rate Elements will be available once the Replication of Products is set up as mentioned in 57Z scope item set up guide or refer to [Product and Rate Element Replication](https://help.sap.com/docs/CLOUD_TO_CASH_OD/a78a4be305be4dbc903bd826a1aba456/9dbec8b5ce1841a6a39f0af5571ed63b.html?version=latest).

|  |
| --- |
| Note Brazil-specific fields require a proper tax calculation. For more information about this, refer to Material Master Data > Define BR Specific Fields for Master Data > Check Create Master Data for Brazil (JD0_BR) . |

| Product ID | Product Type | Description |
| --- | --- | --- |
| R-ONETIME | SBRE | One-time activation fee |
| R-SEATS | SBRE | Seat-based monthly fee |
| R-TRAFFIC | SBRE | Traffic-based usage fee |

Procedure

Product: R-ONETIME

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as a Master Data Specialist - Product Data. | The Home page appears. |  |
| 2 | Access the SAP Fiori app | Choose the Manage Product Master Data tile. | The Manage Product Master Data app appears. |  |
| 3 | Find Product | In the search area on the top, enter the Product: R-ONETIME.Choose Go. | Your product is displayed in the report list. |  |
| 4 | Open Product and Maintain Distribution Chains: General Information | On the Product view, in the Distribution Chains area, choose Create and maintain the following data:Sales Organization: 1710 (Dom. Sales Org US)Distribution Channel: 10 (Direct Sales)Note In Description provide the Language and Product details for specific region, for example, Language: English and Product: Subscription Billing Product. | The product should be open and general information is maintained. | For Country version Germany, maintain the following value instead of 1710:Sales Organization: 1010 (Dom. Sales Org DE)The other entries are the same for both countries. |
| 5 | Maintain Distribution Chains: Grouping Terms | Navigate to the Grouping Terms area and maintain the following data:Account Assignment Group: X9 (Periodic Service)Tax Classification: 1 (Full Tax)Then choose Apply and then Create.Note The item category group is not needed for the product type SBRE if you are using MDI. | Grouping terms are maintained and the product is saved. | For country version Germany, maintain the following value instead of 1 (Full Tax):Tax Classification: 6 (Full Tax (Services))The other entries are the same for both versions. |
| 6 | Maintain Plants | Navigate to the Plants area, choose Create and maintain the following data:Plant: 1710 (Plant US)Choose Apply and Save. | Plant data is maintained. | For country version Germany, maintain the following value:Plant: Plant 10101 (Plant DE) |

Product: R-SEATS

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as a Master Data Specialist - Product Data. | The Home page appears. |  |
| 2 | Access the SAP Fiori app | Choose the Manage Product Master Data tile. | The Manage Product Master Data app appears. |  |
| 3 | Find Product | In the search area on the top,enter the Product: R-SEATSPress the button Go. | Your product is displayed in the report list. |  |
| 4 | Open Product and Maintain Distribution Chains: General Information | On the Product view, in the Distribution Chains area, choose Create and maintain the following data:Sales Organization: 1710 (Dom. Sales Org US)Distribution Channel: 10 (Direct Sales)Note In Description provide the Language and Product details for specific region, for example, Language: English and Product: Subscription Billing Product. | The product should be open and general information is maintained. | For country version Germany, maintain the following value instead of 1710:Sales Organization: 1010 (Dom. Sales Org DE)The other entries are the same for both countries |
| 5 | Maintain Distribution Chains: Grouping Terms | Navigate to the Grouping Terms area and maintain the following data:Account Assignment Group: X9 (Periodic Service)Tax Classification: 1 (Full Tax)Then choose Apply . | Grouping terms are maintained and the product is saved. | For Country version Germany, maintain the following value instead of 1 (Full Tax):Tax Classification: 6 (Full Tax (Services))The other entries are the same for both versions. |
| 6 | Maintain Plants | Navigate to the Plants area, choose Create and maintain the following data:Plant: 1710 (Plant US)Choose Apply and Save. | Plant data is maintained. | For country version Germany, maintain the following value:Plant: PLant 1010 (Plant DE) |

Product: R-TRAFFIC

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as a Master Data Specialist - Product Data. | The Home page appears. |  |
| 2 | Access the SAP Fiori app | Choose the Manage Product Master Data tile. | The Manage Product Master Data app appears. |  |
| 3 | Find Product | In the search area on the top,enter the Product: R-TrafficPress the button Go. | Your product is displayed in the report list. |  |
| 4 | Open Product and Maintain Distribution Chains: General Information | On the Product view, in the Distribution Chains area, choose Create and maintain the following data:Sales Organization: 1710 (Dom. Sales Org US)Distribution Channel: 10 (Direct Sales)Note In Description provide the Language and Product details for specific region, for example, Language: English and Product: Subscription Billing Product. | The product should be open and general information is maintained. | For country version Germany, maintain the following value instead of 1710:Sales Organization: 1010 (Dom. Sales Org DE)The other entries are the same for both countries |
| 5 | Maintain Distribution Chains: Grouping Terms | Navigate to the Grouping Terms area and maintain the following data:Item Category Group: SBRE (Sub. Billing Rate Element)Account Assignment Group: X9 (Periodic Service)Tax Classification: 1 (Full Tax)Choose Apply and then Save .Note The item category group is not required for the product SBRE if you are using MDI. | The product is saved. | For local version Germany, maintain the following value instead of 1 (Full Tax):Tax Classification: 6 (Full Tax (Services))The other entries are the same for both versions. |
| 6 | Maintain Plants | Navigate to the Plants area, choose Create and maintain the following data:Plant: 1710 (Plant US)Choose Apply and then Save. | Plant data is maintained. | For country version Germany, maintain the following value:Plant: Plant 10101 (Plant DE) |

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
> Flagged while digesting this document, not verified: German plant for R-SEATS is given as 'Plant 1010' while R-ONETIME and R-TRAFFIC use 'Plant 10101' (Plant DE); internal inconsistency.

## Connections
- part-of :: [[_cluster]]
- related-to :: [[09-subscription-billing-and-contract-accounting/mds-5bd-429]]
- related-to :: [[09-subscription-billing-and-contract-accounting/sap-s-4hana-cloud-public-edition-mds-5bd-427]]
- related-to :: [[09-subscription-billing-and-contract-accounting/script-de-dados-mestre-criar-faturamento-de-vendas-de-produto-de-assin]]
- related-to :: [[09-subscription-billing-and-contract-accounting/script-de-datos-maestros-crear-facturacion-de-ventas-de-productos-de-s]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/5BD_S4CLD2608_Master_Data_EN_XX.docx` — full document · extracted with `mammoth` · 35,453 chars in the whole document
