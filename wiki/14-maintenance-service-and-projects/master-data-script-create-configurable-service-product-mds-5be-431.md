---
id: 14-maintenance-service-and-projects/master-data-script-create-configurable-service-product-mds-5be-431
title: "Master Data Script: Create Configurable Service Product - MDS (5BE) (5BE_S4CLD2608_Master_Data_EN_XX)"
description: "SAP S/4HANA Cloud Public Edition 2608 master data script (5BE) for creating configurable service products, classes, profiles, variants and prices for service contracts and orders."
cluster: 14-maintenance-service-and-projects
tags: [kb/maintenance-service-and-projects, topic/configurable-service-products]
aliases: [5BE_S4CLD2608_Master_Data_EN_XX]
keywords: [Configurable Service Products and Advanced Variant…, configurable service product, service contract product, service order product, variant configuration, characteristics and classes, variant pricing, material variant, business roles, organizational units]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/5BE_S4CLD2608_Master_Data_EN_XX.docx]
confidence: low
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-431
topic: 14-maintenance-service-and-projects/configurable-service-products
language: EN
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Master Data Script: Create Configurable Service Product - MDS (5BE) (5BE_S4CLD2608_Master_Data_EN_XX)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/5BE_S4CLD2608_Master_Data_EN_XX.docx`, extracted with `mammoth`. Grouped under **Configurable Service Products and Advanced Variant Configuration** in Maintenance, Service and Projects. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

|  |  |
| --- | --- |
| <!-- image omitted: unnamed --> | Master Data ScriptSAP S/4HANA Cloud Public Edition - 02-07-26 |
|  | Create Configurable Service Product - MDS (5BE) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Table of Contents

[1 Purpose 3](#_Toc233904723)

[2 Prerequisites 4](#_Toc233904724)

[2.1 System Access 4](#_Toc233904725)

[2.2 Roles 4](#_Toc233904726)

[2.3 Required Organizational Units 4](#_Toc233904727)

[2.4 Mandatory and Operational Master Data 5](#_Toc233904728)

[2.5 Preliminary Steps (Mandatory) 5](#_Toc233904729)

[3 Overview Table 7](#_Toc233904730)

[4 Procedures 8](#_Toc233904731)

[4.1 Create Configurable Service Product for Service Contracts 8](#_Toc233904732)

[4.1.1 Create Characteristics 8](#_Toc233904733)

[4.1.2 Create Class 10](#_Toc233904734)

[4.1.3 Create Configurable Service Product for Contracts 11](#_Toc233904735)

[4.1.4 Create Configuration Profile 14](#_Toc233904736)

[4.1.5 Set Prices 15](#_Toc233904737)

[4.2 Create Configurable Service Product for Service Orders 17](#_Toc233904738)

[4.2.1 Create Characteristics 17](#_Toc233904739)

[4.2.2 Create Class 21](#_Toc233904740)

[4.2.3 Create Configurable Service Product for Service Order 22](#_Toc233904741)

[4.2.4 Create Configuration Profile 24](#_Toc233904742)

[4.2.5 Set Prices 25](#_Toc233904743)

[4.3 Create Material Variant for a Service Product 28](#_Toc233904744)

[4.3.1 Set Prices for Material Variant 30](#_Toc233904745)

## Purpose

In this document you find a description of how to create configurable service products for service contracts and service orders, as well as the related prices. The description includes those data segments that are relevant for the master data to work in a "usual" system environment. The reader mainly learns which data segments and fields usually need to be filled with input values. Fields that are not relevant for the scope of the S/4 HANA content delivery by SAP Best Practices are not described in this document although they may appear on the UI.

Configurable service products that are created as described here can be used for service contract processing and service order processing. To make use of the configurable service product, refer to the Service Management with Advanced Variant Configuration (6GS) scope item or the Service Contract Management with Advanced Variant Configuration (6GU).

The functionality of product configuration that can be used in service contracts and service orders is the same as further described in scope item 22T- Setup Configurable Model using Variant Configuration.

## Prerequisites

### System Access

| System | Details |
| --- | --- |
| System | Accessible via SAP Fiori Launchpad. Your system administrator provides you with the URL to access the various apps assigned to your role. |

### Roles

Create business roles using the following business role templates delivered by SAP and assign them to your individual test users.

| Name | ID |
| --- | --- |
| Product Configuration Modeler | SAP_BR_PRODUCT_CONFIG_MODELER |
| Master Data Specialist - Product Data | SAP_BR_PRODMASTER_SPECIALIST |
| Pricing Specialist | SAP_BR_PRICING_SPECIALIST |

In addition, the following role is relevant for the configuration user who takes care of the mandatory Preliminary Steps described below:

| Name | ID |
| --- | --- |
| Configuration Expert - Business Process Configuration | SAP_BR_BPC_EXPERT |

### Required Organizational Units

Some segments of master data are dependent on the organizational units of the company, General (Central) Data does not depend on an organizational unit or the company code. The following table gives an overview of these different data segments and their relevant organizational units:

| Data Segment | Depends On | Organizational Unit to be Used | Comments |
| --- | --- | --- | --- |
| Create Material | Plant | 1710 (Plant 1 US) | For Germany, use 1010 (Plant 1 DE) |
| Create Material | Sales Organization | 1710 (Dom. Sales Org US) | For Germany, use 1010 (Dom. Sales Org DE) |
| Create Material | Distribution Channel | 10 (Direct Sales) | For Germany, use 10 (Direct Sales) |

### Mandatory and Operational Master Data

Material master data records may refer to other master data. The following table gives an overview of optional and mandatory master data objects to be used in a material master data record.

|  |
| --- |
| Note Brazil specific fields are required to get a proper tax calculation.Check Nota Fiscal Brazil - JD0 in Define BR Specific Fields for Master Data chapter for material master data. |

| Master Data Object | Used in Data Segment | Mandatory / Optional | Comments |
| --- | --- | --- | --- |
| Profit Center |  | Mandatory | Assigning a Profit Center to a material (product) master is required for correct valuation processes. |

### Preliminary Steps (Mandatory)

Use

Before creating the configurable service product as described in the following procedure, you must first enable the existing material type SERV (Services) to use classification data.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the App | Open the Manage Your Solution app. | The Manage Your Solution app is displayed. |  |
| 3 | Configure Your Solution | On the Manage Your Solution screen, choose Configure Your Solution. | The Configure Your Solution: Realize Phase screen is displayed. |  |
| 4 | Open the Product Item for Configuration | In the search filters, make the following entries:Application Area: <Database and Data ManagementSub Application Area: ProductChoose the Product record in the search results. | The Configure Your Solution - Product screen is displayed. |  |
| 5 | Configure your solution - Product | In the Configuration Steps section, for Define Attributes of Material Types, choose Configure. | The Define Attributes of Material Types: Change screen is displayed. |  |
| 6 | Open Attributes of the Material Type SERV | Double-click the SERV – Service Product entry. | The Define Attributes of Material Types: Change: Details screen is displayed. |  |
| 7 | Enable Classification | In the User Departments list, select Classification.Caution Before saving the changes in the configuration, ensure that the pre-existing selections in the User Departments list are also selected. |  |  |
| 8 | Save Your Data | Choose Save. |  |  |

Result

When creating products of type SERV – Service Product, the Classification tab page is enabled.

## Overview Table

This master record consists of several segments provided in the table below.

| Segment | Business Role | App/Transaction | Expected Results |
| --- | --- | --- | --- |
| [Create Characteristics](#unique_8) [page ] 8 | SAP_BR_PRODUCT_CONFIG_MODELER | Manage Characteristics | Characteristics for service contract class are created. |
| [Create Class](#unique_9) [page ] 10 | SAP_BR_PRODUCT_CONFIG_MODELER | Manage Classes | A class is created. |
| [Create Configurable Service Product for Contracts](#unique_10) [page ] 11 | SAP_BR_PRODMASTER_SPECIALIST | Create Material | Service product for service contracts is created. |
| [Create Configuration Profile](#unique_11) [page ] 14 | SAP_BR_PRODUCT_CONFIG_MODELER | VC Modeling Environment | Configuration profile is created. |
| [Set Prices](#unique_12) [page ] 15 | SAP_BR_PRICING_SPECIALIST | Set Material Prices | Prices are defined. |
| [Create Characteristics](#unique_13) [page ] 17 | SAP_BR_PRODUCT_CONFIG_MODELER | Manage Characteristics | Characteristics for service contract class are created. |
| [Create Class](#unique_14) [page ] 21 | SAP_BR_PRODUCT_CONFIG_MODELER | Manage Classes | A class is created. |
| [Create Configurable Service Product for Service Order](#unique_15) [page ] 22 | SAP_BR_PRODMASTER_SPECIALIST | Create Material | Service product for service order is created. |
| [Create Configuration Profile](#unique_16) [page ] 24 | SAP_BR_PRODUCT_CONFIG_MODELER | VC Modeling Environment | Configuration profile is created. |
| [Set Prices](#unique_17) [page ] 25 | SAP_BR_PRICING_SPECIALIST | Set Material Prices | Prices for service products are defined. |
| [Create Material Variant for a Service Product](#unique_18) [page ] 28 | SAP_BR_PRODMASTER_SPECIALIST | Create Material | A Material Variant for a configurable service product is created. |
| [Set Prices for Material Variant](#unique_19) [page ] 30 | SAP_BR_PRICING_SPECIALIST | Set Material Prices | Price for a material variant is defined. |

## Procedures

This section describes procedures for each segment or process step that is part of this master record.

### Create Configurable Service Product for Service Contracts

#### Create Characteristics

Purpose

In this activity you create characteristics that shall be available for selection in the configurable service product, and for which you can maintain individual variant prices.

Procedure

Characteristic VARKOND (Variant Condition Key)

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as a Product Configuration Modeler. | The Home page appears. |  |
| 2 | Access the app | Open Manage Characteristics.On the Characteristics screen, maintain Characteristic: VARKONDThen choose Create. | Additional screen areas appear. |  |
| 3 | Enter Basic Data | In the Basic data area, maintain the following data:Description: Variant Condition KeyStatus: ReleasedData Type: Character FormatNumber of Chars: 26Case-Sensitive: SelectedMultiple Values: Selected |  |  |
| 4 | Enter Descriptions | Optionally maintain additional languages on the Maintain Descriptions tab page. |  |  |
| 5 | Enter Additional Data | Navigate to the Addnl Data tab page and maintain the following data:Table Name: SDCOMField Name: VKONDNot Ready for Input: SelectedNo Display: Selected |  |  |
| 6 | Save Characteristic | Choose Save. | The new characteristic is created. |  |

Characteristic SERVICE_CHANNEL (Service Channel)

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as a Product Configuration Modeler. | The Home page appears. |  |
| 2 | Access the app | Open Manage Characteristics.On the Characteristics screen, maintain Characteristic: SERVICE_CHANNELThen choose Create. | Additional screen areas appear. |  |
| 3 | Enter Basic Data | In the Basic data area, maintain the following data:Description: Service ChannelStatus: ReleasedData Type: Character FormatNumber of Chars: 20Multiple Values: SelectedEntry Required: Selected |  |  |
| 4 | Enter Descriptions | Optionally maintain additional languages on the Maintain Descriptions tab page. |  |  |
| 5 | Enter Values | Navigate to the Values tab page and maintain the following data:Char. Value / Description: EMAIL / E-mail SupportChar. Value / Description: TELEPHONE / Telephone Support |  |  |
| 6 | Save Characteristic | Choose Save. | The new characteristic is created. |  |

Characteristic PREVENTIVE_MAINTENANCE (Preventive Maintenance)

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as a Product Configuration Modeler. | The Home page appears. |  |
| 2 | Access the app | Open Manage Characteristics.On the Characteristics screen, maintain Characteristic: PREVENTIVE_MAINTENANCEThen choose Create. | Additional screen areas appear. |  |
| 3 | Enter Basic Data | In the Basic data area, maintain the following data:Description: Preventive MaintenanceStatus : ReleasedData Type: Character FormatNumber of Chars: 20Multiple Values: SelectedEntry Required: Selected |  |  |
| 4 | Enter Descriptions | Optionally maintain additional languages on the Maintain Descriptions tab page. |  |  |
| 5 | Enter Values | Navigate to the Values tab page and maintain the following data:Char. Value / Description: YEARLY / YearlyChar. Value / Description: HALFYEARLY / Half-YearlyChar. Value / Description: QUARTERLY / Quarterly |  |  |
| 6 | Save Characteristic | Choose Save. | The new characteristic is created. |  |

#### Create Class

Purpose

In this activity you create a class to which you assign the characteristics from the previous chapter.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as a Product Configuration Modeler. | The Home page appears. |  |
| 2 | Access the app | Open Manage Classes.On the Class screen, maintain the following data:Class: SERVICE_CONTRACT_CClass Type: 300 (Variants)Then choose Create. | Additional screen areas appear. |  |
| 3 | Enter Basic Data | In the Basic data area, maintain the following data:Description: Service Contract ClassStatus: ReleasedDo not check: Selected |  |  |
| 4 | Enter Characteristics | Navigate to the Char. tab page and maintain the following data:VARKONDSERVICE_CHANNELPREVENTIVE_MAINTENANCE | The relevant characteristics are assigned to the class. |  |
| 5 | Save Class | Choose Save. | The new class is created. |  |

#### Create Configurable Service Product for Contracts

Purpose

In this activity you maintain a configurable service product that you can use in service contracts.

|  |
| --- |
| Note Brazil specific fields are required to get a proper tax calculation. Check Create Master Data for Brazil (JD0_BR) in Define BR Specific Fields for Master Data chapter for Material Master Data. |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as a Master Data Specialist - Product Data | The Home page appears. |  |
| 2 | Access the app | Choose Create Material link below the Manage Product Master Data tile. | The Create Material (Initial Screen) is displayed. |  |
| 3 | Enter Material ID and Type | On the Create Material (Initial Screen) maintain the following entries:Material: SRV_CONTR_CONFIGIndustry sector: MIf the Industry Sector input field is hidden, no entry is required.Material Type: Service ProductThen choose Continue (Enter). |  |  |
| 4 | Choose Basic Data View | On the Select View(s) dialog window, select the Basic Data 1 view, then choose Continue (Enter).On the Organizational Levels dialog box, enter the following:Plant: 1710Sales Organization: 1710Distribution Channel: 10Note For DE, enter Plant/Sales Organization/ Disribution Channel as 1010/1010/10 | The Create Material SRV_CONTR _CONFIG view is displayed. |  |
| 5 | Enter Basic Data | On the Basic data 1 view, maintain the following values:Descr: Configurable Service ContractBase Unit of Measure: AU (Activity Unit)Material Group: P001 (Services)GenItemGroup: SCNP (Serv. Contract Prod.)Material is configurable: SelectedNavigate to Additional Data and maintain the following data:Language: DEMaterial Description: Konfigurierbarer ServicevertragThen choose Save. | The product is created and the Create Material (Initial Screen) view is displayed. |  |
| 6 | Choose Sales Views | On the Create Material (Initial Screen) view, maintain material SRV_CONTR_CONFIG, then choose Continue (Enter).On the Select View(s) dialog window, select the following view:Sales: Sales Org. Data 1Sales: Sales Org. Data 2Sales: General/Plant DataThen choose Continue (Enter). | The Organizational Levels dialog window is displayed. |  |
| 7 | Choose Organizational Levels | On the Organizational Levelsdialog window, maintain the following values:Plant: 1710 (Plant 1 US)Sales Org.: 1710 (Dom. Sales Org US)Distr. Channel: 10 (Direct Sales)Note Note: For DE, maintain 1010/1010/10 respectively.Then choose Continue (Enter). | The Sales: sales org. 1 view is displayed. |  |
| 8 | Enter Sales Organization Data (1) | On the Sales: sales org. 1 view, maintain the following values:General data• Cash Discount: X <selected>Tax data• Tax classification: 1 (Full tax)Then choose Enter. | The Sales: sales org. 2view is displayed. |  |
| 9 | Enter Sales Organization Data (2) | On the Sales: sales org. 2 view, maintain the following entry:Item category group: SCNP (Serv. Contract Prod.)Then choose Enter. | The Sales: General/Plantview is displayed. |  |
| 10 | Enter General Sales Data | On the Sales: General/Plant view, maintain the following values:Base Unit of Measure: AU (Activity Unit)Work Duration: 1 HRThen choose Save.For Poland only: choose Enter instead of Save. | The Create Material (Initial Screen) view is displayed. |  |
| For Poland only | Enter Sales Data | In the International Trade: Export section, enter the following data:Control code.: for example, 41.00.30.0Then choose Save. | The Create Material (Initial Screen) view is displayed. |  |
| 11 | Choose Classification View | On the Create Material (Initial Screen) view, maintain material SRV_CONTR_CONFIG, then choose Continue (Enter).On the Select View(s) dialog window, select the following view:ClassificationThen choose Continue (Enter). | The Classificationview is displayed. |  |
| 12 | Enter Classification | On the Class Typedialog window, select the Variants (300) entry, then choose Copy.On the Classification view, maintain the following data:Class: SERVICE_CONTRACT_CChoose Enter to display the characteristics assigned to the class.In the Values for Class SERVICE_CONTRACT_C screen area, for each characteristic open the value help and select all available values.Then choose Save. | The Create Material (Initial Screen) view is displayed. |  |

#### Create Configuration Profile

Purpose

In this activity you create a configuration profile in the variant configuration modeler.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as a Product Configuration Modeler. | The Home page appears. |  |
| 2 | Access the app | Open VC Modeling Environment.On the Initial Screen of Variant Configuration Modeling Environment screen, maintain the following data:Material: SRV_CONTR_CONFIGClass Type: 300 (Variants)Then choose Enter Model. | The Configuration for SRV_CONTR_CONFIG screen is displayed. |  |
| 3 | Create Configuration Profile | In the Object column, right-click the SRV_CONTR_CONFIG entry and choose Create Configuration Profile.On the Create Configuration Profile dialog window, maintain the following data:Configuration Profile: SRV_CONTR_CONFWithout Change No.: SelectedThen choose Continue (Enter).In the Object pane, double-click the SRV_CONTR_CONFIG material.Open the Variant Pricing tab page, choose Change, and then choose Expand List.Maintain all characteristics assigned to your configurable product except the VARKOND characteristic. Also, make sure to maintain a Variant Cond. and Description to all of them. The variant condition is used in the price condition maintenance.For example, for Characteristic / Char. Value / Variant Cond. / Variant Cond. Description, maintain:SERVICE_CHANNEL / EMAIL / EMAIL /E-mail SupportSERVICE_CHANNEL / TELEPHONE / TELEPHONE / Telephone SupportPREVENTIVE_MAINTENANCE / YEARLY / YEARLY / YearlyPREVENTIVE_MAINTENANCE / HALFYEARLY / HALFYEARLY / Half-YearlyPREVENTIVE_MAINTENANCE / QUARTERLY / QUARTERLY / QuarterlyThen choose Save. | The Configuration for SRV_CONTR_CONFIG screen is displayed. |  |

#### Set Prices

Purpose

In this activity you maintain a standard price condition record for the configurable service product, as well as variant price records for the configurable variants.

Procedure

Condition Type: PSI1 (Price for Service Contract Item)

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori launchpad as Pricing Specialist. | The Home page appears. |  |
| 2 | Access the app | Open Set Material Prices . | The Change Condition Records view is displayed. |  |
| 3 | Enter Condition Type | On the Change Condition Records view, maintain Condition Type: PSI1 (Price f.Srv.Cntr), then choose Enter. | The Key Combination view is displayed. |  |
| 4 | Select Key Combination | In the Key combination view, choose MaterialThen choose Enter. | The Change Price (PSI1): Selection view is displayed. |  |
| 5 | Selection | On the Change Price (PSI1): Selection view, maintain the following information:Sales Org.: 1710 (Dom. Sales Org US)Distr. Channel: 10 (Direct Sales)Material:SRV_CONTRACT (Service Contract Product)Valid On: <Date>, for example, today’s dateThen choose Execute. | The Change Price Condition (PPSI): Overview view is displayed. |  |
| 6 | Enter Price Condition | On the Change Price Condition (PSI1): Overview view, maintain the following data:Material: SRV_CONTR_CONFIG (Configurable Service Contract)Amount: for example, 200.00Unit: for example, USDValid From: <Date> for example, today’s dateChoose Enter.Then choose Save. | A standard price for the service product SRV_CONTR_CONFIG has been maintained. |  |

Condition Type: VASE (Variant Price)

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori launchpad as Pricing Specialist. | The Home page appears. |  |
| 2 | Access the app | Open Set Material Prices . | The Change Condition Records view is displayed. |  |
| 3 | Enter Condition Type | On the Change Condition Records view, maintain Condition Type: VASE (Variant Price), then choose Enter. | The Change Variant Price view is displayed. |  |
| 4 | Enter Sales Data | On the Change Variant Price ( VASE ): Selection view, maintain the following information:Sales Org.: 1710 (Dom. Sales Org US)Distribution Channel: 10 (Direct Sales)Material: SRV_CONTR_CONFIG (Configurable Service Contract)Valid On: <Date> for example, today’s dateThen choose Execute. | The Change Variant Price Condition ( VASE ): Overview view is displayed. |  |
| 5 | Enter Variant Conditions | On the Change Variant Price Condition ( VASE ): Overview view, maintain prices for all variant conditions you maintained in the previous chapter, for example:Variant / Amount / Unit:EMAIL / 30 USDTELEPHONE / 50 USDYEARLY / 250 USDHALFYEARLY / 135 USDQUARTERLY / 90 USDChoose Enter and verify your entries.Then choose Save. | Variant price conditions have been maintained. |  |

### Create Configurable Service Product for Service Orders

#### Create Characteristics

Purpose

In this activity you create characteristics that shall be available for selection in the configurable service product, and for which you can maintain individual variant prices.

Procedure

Characteristic VARKOND (Variant Condition Key)

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as a Product Configuration Modeler. | The Home page appears. |  |
| 2 | Access the App | Open Manage Characteristics.On the Characteristics screen, in the field Characteristic: enter VARKONDThen choose Create. | Additional screen areas appear. |  |
| 3 | Enter Basic Data | In the Basic data area, enter the following data:Description: Variant Condition KeyStatus: ReleasedDate Type: Character FormatNumber of Chars: 26Case-Sensitive: SelectedMultiple Values: Selected |  |  |
| 4 | Enter Descriptions | Optionally, you can enter additional languages on the Maintain Descriptions tab page. |  |  |
| 5 | Enter Additional Data | Navigate to the Addnl Data tab page and enter the following data:Table Name: SDCOMField Name: VKONDNot Ready for Input: SelectedNo Display: Selected |  |  |
| 6 | Save Characteristic | Choose Save. | The new Variant Condition Key is created. |  |

Characteristic CAR_WASH_TYPE (Car Wash Type)

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as a Product Configuration Modeler. | The Home page appears. |  |
| 2 | Access the app | Open Manage Characteristics.On the Characteristics screen, in the field Characteristic: enter CAR_WASH_TYPEThen choose Create. | Additional screen areas appear. |  |
| 3 | Enter Basic Data | In the Basic data area, enter the following data:Description: Car Wash TypeStatus: ReleasedDate Type: Character FormatNumber of Chars: 20Single Values: SelectedEntry Required: Selected |  |  |
| 4 | Enter Descriptions | Optionally, you can enter additional languages on the Maintain Descriptions tab page. |  |  |
| 5 | Enter Values | Navigate to the Values tab page and enter the following data:Char. Value / Description: BASIC / Basic WashChar. Value / Description: STANDARD / Standard WashChar. Value / Description: PREMIUM / Premium Wash |  |  |
| 6 | Save Characteristic | Choose Save. | The new characteristic is created. |  |

Characteristic CAR_SIZE (Car Size)

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as a Product Configuration Modeler. | The Home page appears. |  |
| 2 | Access the app | Open Manage Characteristics.On the Characteristics screen, in the field Characteristic: enter CAR_SIZEThen choose Create. | Additional screen areas appear. |  |
| 3 | Enter Basic Data | In the Basic data area, enter the following data:Description: Car SizeStatus : ReleasedDate Type: Character FormatNumber of Chars: 20Single Values: SelectedEntry Required: Selected |  |  |
| 4 | Enter Descriptions | Optionally, you can enter additional languages on the Maintain Descriptions tab page. |  |  |
| 5 | Enter Values | Navigate to the Values tab page and enter the following data:Char. Value / Description: S / SmallChar. Value / Description: M / MediumChar. Value / Description: L / Large |  |  |
| 6 | Save Characteristic | Choose Save. | The new characteristic is created. |  |

Characteristic EXTRA_POLISH (Extra Polish)

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as a Product Configuration Modeler. | The Home page appears. |  |
| 2 | Access the app | Open Manage Characteristics.On the Characteristics screen, in the field Characteristic: enter EXTRA_POLISHThen choose Create. | Additional screen areas appear. |  |
| 3 | Enter Basic Data | In the Basic data area, enter the following data:Description: Extra PolishStatus : ReleasedDate Type: Character FormatNumber of Chars: 10Single Value: SelectedEntry Required: Selected |  |  |
| 4 | Enter Descriptions | Optionally, you can enter additional languages on the Maintain Descriptions tab page. |  |  |
| 5 | Enter Values | Navigate to the Values tab page and enter the following data:Char. Value / Description: YES / YesChar. Value / Description: NO / No |  |  |
| 6 | Save Characteristic | Choose Save. | The new characteristic is created. |  |

#### Create Class

Purpose

In this activity you create a class to which you assign the characteristics from the previous chapter.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as a Product Configuration Modeler. | The Home page appears. |  |
| 2 | Access the app | Open Manage Classes.On the Class screen, enter the following data:Class: CAR_WASHClass Type: 300 (Variants)Then choose Create. | Additional screen areas appear. |  |
| 3 | Enter the Class Name | On the Class Screen, enter the following data:Class: CAR_WASHClass Type: 300 (Variants)Then choose Create |  |  |
| 4 | Enter Basic Data | In the Basic data area, enter the following data:Description: Car WashStatus: ReleasedDo not check: Selected |  |  |
| 5 | Enter Characteristics | Navigate to the Char. tab page and maintain the following data:VARKONDCAR_WASH_TYPECAR_SIZEEXTRA_POLISH | The relevant characteristics are assigned to the class. |  |
| 6 | Save Class | Choose Save. | The new class is created. |  |

#### Create Configurable Service Product for Service Order

Purpose

In this activity you maintain a configurable service product that you can use in service orders.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as a Master Data Specialist - Product Data | The Home page appears. |  |
| 2 | Access the app | Choose Create Material app. | The Create Material (Initial Screen) is displayed. |  |
| 3 | Enter Material ID and Type | On the Create Material (Initial Screen), enter the following data:Material: CAR-WASH_CONFIf the Industry Sector input field is hidden, no entry is required.Material Type: SERV Service ProductThen choose Continue (Enter). |  |  |
| 4 | Choose Basic Data View | On the Organizational Levels dialog box, enter the following data:Plant: 1710 (Plant 1 US)Sales Org.: 1710 (Dom. Sales Org US)Distr. Channel: 10 (Direct Sales)Note: For DE, enter 1010/1010/10 respectively.Then choose Continue (Enter). | The Create Material CAR-WASH _CONF view is displayed. |  |
| 5 | Enter Basic Data | On the Basic data 1 tab, enter the following data:Descr.: Car Wash ConfigurableBase Unit of Measure: AU (Activity Unit)Material Group: P001 (Services)GenItemCatGroup: SRVP (Service Product)Material is configurable: SelectedNavigate to Additional Data and maintain the following data:Language: DEMaterial Description: Konfigurierbare AutowäscheThen choose Save. | The product is created and theCreate Material (Initial Screen) view is displayed. |  |
| 6 | Choose Sales Views | On the Create Material (Initial Screen) view, in the field Material, enter CAR-WASH_CONF, then choose Continue (Enter).On the Select View(s) dialog box, select the following views:Sales: Sales Org. Data 1Sales: Sales Org. Data 2Sales: General/Plant DataThen choose Continue (Enter). | The Organizational Levels dialog window is displayed. |  |
| 7 | Choose Organizational Levels | On the Organizational Levels dialog box, enter the following data:Plant: 1710 (Plant 1 US)Sales Org.: 1710 (Dom. Sales Org US)Distr. Channel: 10 (Direct Sales)Note: For DE, enter 1010/1010/10 respectively.Then choose Continue (Enter). | The Sales: sales org. 1 view is displayed. |  |
| 8 | Enter Sales Organization Data (1) | On the Sales: sales org. 1 tab, enter the following data:General data• Cash Discount: X <selected>Tax data• Tax classification: 1 (Full tax)Then choose Enter. | The Sales: sales org. 2view is displayed. |  |
| 9 | Enter Sales Organization Data (2) | On the Sales: sales org. 2 tab, enter the following data:Item category group: SRVP (Service Product)Then choose Enter. | The Sales: General/Plantview is displayed. |  |
| 10 | Enter General Sales Data | On the Sales: General/Plant tab, enter the following data:Base Unit of Measure: AU (Activity Unit)Work Duration: 1 HRThen choose Save.For Poland only: choose Enter instead of Save. | The Create Material (Initial Screen) view is displayed. |  |
| For Poland only | Enter Sales Data | On the International Trade: Export tab in the area Foreigen trade date, enter the following data:Control code.: for example, 41.00.30.0Then choose Save. |  |  |
| 11 | Choose Classification View | On the Create Material (Initial Screen) view, in the field Material enter CAR-WASH_CONF, then choose Continue (Enter).On the Select View(s) dialog box, select the following view:ClassificationThen choose Continue (Enter). | The Classification view is displayed. |  |
| 12 | Enter Classification | On the Class Type dialog box, select the Variants (300) entry, then choose Copy.On the Classification view, enter the following data:Class: CAR_WASHChoose Enter to display the characteristics assigned to the class.In the Values for Class CAR_WASH screen area, for each characteristic open the value help and select all available values.Then choose Save. | Characteristics are assigned to the material. |  |

#### Create Configuration Profile

Purpose

In this activity you create a configuration profile in the variant configuration modeler.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as a Product Configuration Modeler. | The Home page appears. |  |
| 2 | Access the app | Open VC Modeling Environment.On the Initial Screen of Variant Configuration Modeling Environment screen, enter the following data:Material: CAR-WASH_CONFClass Type: 300 (Variants)Then choose Enter Model. | The Configuration for CAR_WASH_CONF screen is displayed. |  |
| 3 | Create Configuration Profile | In the Object column, right-click the CAR-WASH_CONF entry and choose Create Configuration Profile.On the Create Configuration Profile dialog box, enter the following data:Configuration Profile: CAR-WASH_CONFWithout Change No.: SelectedThen choose Continue (Enter).In the Object column, double-click the CAR-WASH_CONF entry. Open the Variant Pricing tab page and choose Change. Then choose Expand List.Enter all characteristics assigned to your configurable product except the VARKOND characteristic. Also, make sure to enter a Variant Cond. and Description to all of them. The variant condition is used in the price condition maintenance.For example, for Characteristic / Char. Value / Variant Cond. / Variant Cond. Description, enter:CAR_WASH_TYPE / BASIC / C_W_T_B / BasicCAR_WASH_TYPE / STANDARD / C_W_T_S / StandardCAR_WASH_TYPE / PREMIUM / C_W_T_P / PremiumCAR_SIZE / S / C_S_S / SmallCAR_SIZE / M / C_S_M / MediumCAR_SIZE / L / C_S_L / LargeEXTRA_POLISH / YES / E_P_Y / YesEXTRA_POLISH / NO / E_P_N / NoThen choose Save. | Variant Conditions are created for all characteristics. |  |

#### Set Prices

Purpose

In this activity you maintain a standard price condition record for the configurable service product, as well as variant price records for the configurable variants.

Procedure

Condition Type: PPR0 (Price)

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori launchpad as Pricing Specialist. | The Home page appears. |  |
| 2 | Access the app | Open Set Material Prices . | The Change Condition Records view is displayed. |  |
| 3 | Enter Condition Type | On the Change Condition Records view, in the field Condition Type: enter PPR0 (Price), then choose Enter. | The Key Combination view is displayed. |  |
| 4 | Select Key Combination | In the Key combination view, choose MaterialThen choose Enter. | The Change Price (PPR0): Selection view is displayed. |  |
| 5 | Selection | On the Change Price (PPR0): Selection view, enter the following data:Sales Org.: 1710 (Dom. Sales Org US)Distr. Channel: 10 (Direct Sales)Material: CAR-WASH_CONF (Car Wash Configurable)Valid On: <Date>, for example, today’s dateThen choose Execute. | The Change Price Condition (PPR0): Overview view is displayed. |  |
| 6 | Enter Price Condition | On the Change Price Condition (PPR0): Overview view, enter the following data:Material: CAR-WASH_CONF (Car Wash Configurable)Amount: for example, 10.00Unit: for example, USDValid From: <Date> for example, today’s dateChoose Enter.Then choose Save. | A standard price for the service product is created. |  |

Condition Type: PVA0 (Variant Price)

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori launchpad as Pricing Specialist. | The Home page appears. |  |
| 2 | Access the app | Open Set Material Prices . | The Change Condition Records view is displayed. |  |
| 3 | Enter Condition Type | On the Change Condition Records view, maintain Condition Type: PVA0 (Variant Price), then choose Enter. | The Change Variant Price view is displayed. |  |
| 4 | Enter Sales Data | On the Change Variant Price ( PVA0 ): Selection view, maintain the following information:Sales Org.: 1710 (Dom. Sales Org US)Distribution Channel: 10 (Direct Sales)Material: CAR-WASH_CONF (Configurable Service Contract)Valid On: <Date> for example, today’s dateThen choose Execute. | The Change Variant Price Condition ( PVA0 ): Overview view is displayed. |  |
| 5 | Enter Variant Conditions | On the Create Variant Price Condition ( PVA0): Overview view, enter prices for all variant conditions you created in the previous chapter, for example:Variant / Amount / Unit:C_W_T_B / 5 USDC_W_T_S / 8 USDC_W_T_P / 12 USDC_S_S / 2 USDC_S_M / 4 USDC_S_L / 10 USDChoose Enter and verify your entries.Then choose Save. | Variant price conditions are created. |  |

PVA1 (Variant Price %)

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori launchpad as Pricing Specialist. | The Home page appears. |  |
| 2 | Access the app | Open Set Material Prices . | The Change Condition Records view is displayed. |  |
| 3 | Enter Condition Type | On the Change Condition Records view, in field Condition Type: enter PVA1 Variant Price (%), then choose Enter. | The Change Variant Price (% PVA1) view is displayed. |  |
| 4 | Enter Sales Data | On the Change Variant Price ( % (PVA1 ): Selection view, enter the following data:Sales Org.: 1710 (Dom. Sales Org US)Distribution Channel: 10 (Direct Sales)Material: CAR-WASH_CONFValid On: <Date> for example, today’s dateThen choose Execute. | The Change Variant Price (%) Condition (PVA1): Overview view is displayed. |  |
| 5 | Enter Variant Conditions | On the Create Variant Price (%) Condition (PVA1) : Overview view, enter condition records for all relevant variant conditions, for example:Variant / Amount / Unit:E_P_Y / 20%E_P_N / -10%Choose Enter and verify your entries.Then choose Save. | Variant price conditions are created. |  |

### Create Material Variant for a Service Product

Purpose

In this activity, you create a material variant with a predefined configuration that can be used in a service order. The master record of the variant is linked to a configurable product uses its characteristics.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as a Master Data Specialist - Product Data | The Home page appears. |  |
| 2 | Access the App | Choose the link Create Material below the Manage Product Master Data tile. | The Create Material (Initial Screen) is displayed. |  |
| 3 | Enter Material ID and Type | On the Create Material (Initial Screen) enter the following data:Material: CAR-WASH-VARIndustry sector: Mechanical engineeringIf the Industry Sector input field is hidden, no entry is required.Material Type: SERV Service ProductThen choose Continue (Enter).On the Select View(s) dialog box, choose Basic Data 1Choose Org.Levels |  |  |
| 4 | Select Organizational Levels | On the Organizational Levels dialog box, enter the following data:Plant: 1710 (Plant 1 US)Sales Organization: 1710 (Dom. Sales Org US)Distr. Channel: 10 (Direct Sales)Note For DE, enter 1010/1010/10 respectively.Then choose Continue (Enter). | The Create Material CAR-WASH-VAR view is displayed. |  |
| 5 | Enter Basic Data | On the Basic data 1 tab, enter the following data:Descr.: Car Wash VariantBase Unit of Measure: AU (Activity Unit)Material Group: P001 (Services)GenItemGroup: SRVP (Service Product)Material is configurable: unselectedCross Plant CM: CAR-WASH_CONFChoose Configure VariantOn the view Variant ConfigurationSelect the following characteristics:Car Size: SmallExtra Polish: YesCar Wash Type: Standard Washchoose DoneThen, choose Save. | The product is created and theCreate Material (Initial Screen) view is displayed. |  |
| 6 | Choose Sales Views | On the Create Material (Initial Screen) view, in the field Material, enter CAR-WASH-VAR, then choose Continue (Enter).On the Select View(s) dialog box, select the following views:Sales: Sales Org. Data 1Sales: Sales Org. Data 2Sales: General/Plant DataThen, choose Continue (Enter). | The Organizational Levels dialog window is displayed. |  |
| 7 | Choose Organizational Levels | On the Organizational Levels dialog box, enter the following data:Plant: 1710 (Plant 1 US)Sales Org.: 1710 (Dom. Sales Org US)Distr. Channel: 10 (Direct Sales)Note For DE, enter 1010/1010/10 respectively.Then, choose Continue (Enter). | The Sales: sales org. 1 view is displayed. |  |
| 8 | Enter Sales Organization Data (1) | On the Sales: sales org. 1 tab, enter the following data:General data• Cash Discount: X <selected>• Tax data• Tax classification: 1 (Full tax)Then, choose Enter. | The Sales: sales org. 2 view is displayed. |  |
| 9 | Enter Sales Organization Data (2) | On the Sales: sales org. 2 tab, enter the following data:Item category group: SRVP (Service Product)Then, choose Enter. | The Sales: General/Plantview is displayed. |  |
| 10 | Enter General Sales Data | On the Sales: General/Plant tab, enter the following data:Base Unit of Measure: AU (Activity Unit)Work Duration: 1 HRThen, choose Save. | The Create Material (Initial Screen) view is displayed. |  |

#### Set Prices for Material Variant

Purpose

In this activity you maintain a standard price condition record for the variant.

Procedure

Condition Type: PPR0 (Price)

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori launchpad as Pricing Specialist. | The Home page appears. |  |
| 2 | Access the App | Open Set Material Prices . | The Change Condition Records view is displayed. |  |
| 3 | Enter Condition Type | On the Change Condition Records view, in the field Condition Type: enter PPR0 (Price), then, choose Enter. | The Key Combination view is displayed. |  |
| 4 | Select Key Combination | In the Key combination view, choose Material with release statusThen, choose Enter. | The Change Price (PPR0): Selection view is displayed. |  |
| 5 | Selection | On the Change Price (PPR0): Selection view, enter the following data:Sales Org.: 1710 (Dom. Sales Org US)Distr. Channel: 10 (Direct Sales)Material: CAR-WASH-VAR (Car Wash Variant)Valid On: <Date>, for example, today’s dateThen, choose Execute. | The Change Price Condition (PPR0): Overview view is displayed. |  |
| 6 | Enter Price Condition | On the Change Price Condition (PPR0): Overview view, enter the following data:Material: CAR-WASH-VAR (Car Wash VAR)Amount: for example, 20.00Unit: for example, USDValid From: <Date> for example, today’s dateChoose Enter.Then, choose Save. | A standard price for the variant is created. |  |

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
> Flagged while digesting this document, not verified: Contract price step selects material SRV_CONTRACT but then maintains SRV_CONTR_CONFIG, an internal naming inconsistency.

> [!warning] Conflict
> Flagged while digesting this document, not verified: Service order product material type is given as 'Service Product' in contract section but 'SERV Service Product' elsewhere; item category group differs by design (SCNP for contracts, SRVP for orders).

## Connections
- part-of :: [[_cluster]]
- related-to :: [[14-maintenance-service-and-projects/criar-produto-de-servico-configuravel-mds-5be-script-de-dados-mestre-s]]
- related-to :: [[14-maintenance-service-and-projects/mds-5be-master-data-script-create-configurable-service-products-435]]
- related-to :: [[14-maintenance-service-and-projects/sap-s-4hana-cloud-public-edition-mds-5be-433]]
- related-to :: [[14-maintenance-service-and-projects/script-de-datos-maestros-creacion-de-producto-de-servicio-configurable]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/5BE_S4CLD2608_Master_Data_EN_XX.docx` — full document · extracted with `mammoth` · 45,474 chars in the whole document
