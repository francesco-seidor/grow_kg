---
id: 14-maintenance-service-and-projects/master-data-script-create-service-product-for-service-processes-mds-3k
title: "Master Data Script: Create Service Product for Service Processes - MDS (3KV) (3KV_S4CLD2608_Master_Data_EN_XX)"
description: "SAP S/4HANA Cloud Public Edition 2608 master data script (3KV): step-by-step creation of service products (SRV_*, FSM expenses) and their sales prices, overtime and accounting indicator conditions."
cluster: 14-maintenance-service-and-projects
tags: [kb/maintenance-service-and-projects, topic/service-products-for-service-processes]
aliases: [3KV_S4CLD2608_Master_Data_EN_XX]
keywords: [Service Products and Service Prices, service products, service product master data, material pricing, overtime pricing, accounting indicator, service bundles, service contract products, field service management expenses, stock service parts]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/3KV_S4CLD2608_Master_Data_EN_XX.docx]
confidence: low
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-347
topic: 14-maintenance-service-and-projects/service-products-for-service-processes
language: EN
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Master Data Script: Create Service Product for Service Processes - MDS (3KV) (3KV_S4CLD2608_Master_Data_EN_XX)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/3KV_S4CLD2608_Master_Data_EN_XX.docx`, extracted with `mammoth`. Grouped under **Service Products and Service Prices** in Maintenance, Service and Projects. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

|  |  |
| --- | --- |
| <!-- image omitted: unnamed --> | Master Data ScriptSAP S/4HANA Cloud Public Edition - 02-07-26 |
|  | Create Service Product for Service Processes - MDS (3KV) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Table of Contents

[1 Purpose 3](#_Toc233904648)

[2 Prerequisites 4](#_Toc233904649)

[2.1 System Access 4](#_Toc233904650)

[2.2 Roles 4](#_Toc233904651)

[2.3 Required Organizational Units 4](#_Toc233904652)

[3 Overview Table 5](#_Toc233904653)

[4 Procedures 6](#_Toc233904654)

[4.1 Create Service Products 6](#_Toc233904655)

[4.1.1 SRV_01 6](#_Toc233904656)

[4.1.2 SRV_CONTRACT 8](#_Toc233904657)

[4.1.3 SRV_CTR_RENEWAL 10](#_Toc233904658)

[4.1.4 SRV_02 11](#_Toc233904659)

[4.1.5 FSM – Expense Item 13](#_Toc233904660)

[4.1.6 SRV_03 15](#_Toc233904661)

[4.1.7 SRV_04 17](#_Toc233904662)

[4.1.8 SRV_BUNDLE_01 19](#_Toc233904663)

[4.1.9 SRV_BUNDLE_02 20](#_Toc233904664)

[4.1.10 SRV_05 22](#_Toc233904665)

[4.1.10.1 Create Basic Data 22](#_Toc233904666)

[4.1.10.2 Create Sales Data 23](#_Toc233904667)

[4.1.10.3 Create Purchasing Data 25](#_Toc233904668)

[4.1.10.4 Create MRP/Planning Data 26](#_Toc233904669)

[4.1.10.5 Create Storage Location Data 28](#_Toc233904670)

[4.1.10.6 Create Accounting Data 29](#_Toc233904671)

[4.2 Set Prices for Materials 31](#_Toc233904672)

[4.2.1 Price for SRV_01 31](#_Toc233904673)

[4.2.2 Price for SRV_CONTRACT 32](#_Toc233904674)

[4.2.3 Price for SRV_CTR_RENEWAL 33](#_Toc233904675)

[4.2.4 Price for SRV_02 34](#_Toc233904676)

[4.2.5 Price for SRV_04 35](#_Toc233904677)

[4.2.6 Price for SRV_BUNDLE_01 36](#_Toc233904678)

[4.2.7 Price for SRV_05 37](#_Toc233904679)

[4.2.8 Price for FSM - Expense EXP_FSM_MILEAGE 39](#_Toc233904680)

[4.3 Set Prices for Overtime 40](#_Toc233904681)

[4.4 Creating Condition Record for Accounting Indicator 41](#_Toc233904682)

## Purpose

In this document you find a description of how to create service productmaster data records including prices. The description includes those data segments that are relevant for the master data to work in a "usual" system environment. The reader mainly learns which data segments and fields usually need to be filled with input values. Fields that are not relevant for the scope are not described in this document although they may appear on the UI.

A service product master record that is created as described here can be used for service order and service confirmation processing.

| Service product ID | Description | Usage |
| --- | --- | --- |
| SRV_01 | Service | represents the service itself, for example, an installation, a repair, a maintenance |
| SRV_CONTRACT | Contract Product | represents the service itself within the contract |
| SRV_CTR_RENEWAL | Service Contract Renewal Product | represents the service contract product within the contract with preset alues for auto-renewal |
| SRV_02 | Service Expense | reflects the expense which could occur due to the service, for example, travel cost, fuel |
| SRV_03 | Service Part (Undefined) | reflects a material required for the service and allows free text descriptionthis non-stock material can only be procured |
| SRV_04 | Service Part (Defined) | reflects the material as the non-stock with minimal/no logistic integrationthis non-stock material can only be procured |
| SRV_05 | Stock Service Part | reflects a material which will be taken from stock (pick from stock scenario) |
| SRV_06 | Stock Service Part with Serial Number Profile | reflects a material with an assigned serial number profile which will be taken from stock (pick from stock scenario) |
| SRV_BUNDLE_01 | Service Bundle 01 | represents a complex service as a bundle with sub items |
| SRV_BUNDLE_02 | Service Bundle 02 | represents a complex service as a bundle with sub items (service Item and fixed price items) |
| EXP_FSM_TRAVELEXP_FSM_MEALSEXP_FSM_OTHEREXP_FSM_MILEAGE | Service Expense | reflects the expense, for example, travel cost or meals, in case of integration with SAP Field Service Management. |

## Prerequisites

### System Access

| System | Details |
| --- | --- |
| System | Accessible via SAP Fiori Launchpad. Your system administrator provides you with the URL to access the various apps assigned to your role. |

### Roles

Create business roles using the following business role templates delivered by SAP and assign them to your individual test users.

Alternatively, if available, you can use the following spaces delivered by SAP. You create a space with pages containing predefined essential apps and assign it to the business role. You then assign this business role to your individual users.

For more information, refer to How to Create a Business Role from a Template in the [product assistance](https://help.sap.com/docs/SAP_S4HANA_CLOUD/53e36b5493804bcdb3f6f14de8b487dd/ec310a8b669a45ca898dc4dd91d97de2.html) for SAP S/4HANA Cloud Public Edition.

| Name (Role Template) | ID (Role Template) | Name (Launchpad Space) | ID (Launchpad Space) |
| --- | --- | --- | --- |
| Master Data Specialist - Product Data | SAP_BR_PRODMASTER_SPECIALIST | Master Data - Products / Product Governance | SAP_BR_PRODMASTER_SPECIALIST / SAP_CMD_SPT_PR_GOV_PC |
| Pricing Specialist | SAP_BR_PRICING_SPECIALIST | Price Management | SAP_BR_PRICING_SPECIALIST |

### Required Organizational Units

Some segments of master data are dependent on the organizational units of the company, General (Central) Data does not depend on an organizational unit or the company code. The following table gives an overview of these different data segments and their relevant organizational units:

| Data Segment | Depends On | Organizational Unit to be Used for US | Organizational Unit to be Used for DE |
| --- | --- | --- | --- |
| Create Material | Plant | 1710 (Plant 1 US) | 1010 (Plant 1 DE) |
| Create Material | Sales Organization | 1710 (Dom. Sales Org US) | 1010 (Dom. Sales Org DE) |
| Create Material | Distribution Channel | 10 (Direct Sales) | 10 (Direct Sales) |

## Overview Table

This master record consists of several segments provided in the table below.

|  |
| --- |
| Note If your system administrator has enabled spaces and pages on the SAP Fiori launchpad, the homepage will only contain the essential apps for performing the typical tasks of a business role.You can find all other (searchable) apps not included on the homepage using the search bar ([2434549](https://me.sap.com/notes/2434549)).If you want to personalize the homepage and include the hidden apps, navigate to your user profile and choose App Finder. |

| Segment | Business Role | App/Transaction | Expected Results |
| --- | --- | --- | --- |
| Create Service Products | SAP_BR_PRODMASTER_SPECIALIST | Create Material (MM01) | Service products are created. |
| Set Prices for materials (Create Condition Records) | SAP_BR_PRICING_SPECIALIST | Set Material Prices - Sales (VK12) | Prices for service products are defined. |
| Set Prices for Overtime (Create Condition Records) | SAP_BR_PRICING_SPECIALIST | Set Material Prices - Sales (VK12) | Price for overtime has been defined. |

## Procedures

This section describes procedures for each segment or process step that is part of this master record.

### Create Service Products

#### SRV_01

Purpose

This material is relevant for cloud edition only.

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as a Master Data Specialist - Product Data (MDG). | The Home page appears. |  |
| 2 | Access the SAP Fiori app | Choose Create Material app. | The Create Material screen is displayed. |  |
| 3 | Maintain Material Basic Data (for Service Product Service) | On the Create Material (Initial Screen) make the following entries: dialog window, select theMaterial: SRV_01Industry sector MIf the Industry Sector input field is hidden, no entry is required. When the industry sector is not offered for entry, the field is populated in the dark. Currently only one entry exists for industry (M = Mechanical engineering).Material Type: Service ProductThen choose Continue (Enter). | You have maintained basic information for the new service product.The Select View(s) dialog window is displayed. |  |
| 4 | Choose Views | On the Select View(s) dialog window, select the following views:Basic data 1Sales: Sales Org. Data 1Sales: Sales Org. Data 2Sales: General/Plant DataPurchasingAccounting1Then choose Continue (Enter). | The Organizational Level screen is displayed. |  |
| 5 | Choose Organizational Levels | On the Organizational Levels window, maintain the following values:Plant: 1710 (Plant 1 US)Sales Org.: 1710 (Dom. Sales Org US)Distr. Channel: 10 (Direct Sales)Then choose Continue (Enter). | Organizational data has been selected.The Create Material SRV_01 (Services) view is displayed. |  |
| 6 | Maintain Basic Data | On the Basic data 1 view, maintain the following values:Descr.: ServiceBase Unit of Measure: HR (Hours)Material Group: P001 (Services)GenItemGroup: SRVP (Service Product)Then choose Continue (Enter). | Basic data is maintained and Sales: sales org. 1 tab page is displayed.Note For every different language used in your company the corresponding description for the product has to be maintained per language code! |  |
| 7 | Maintain Sales Organization Data (1) | On the Sales: sales org. 1 view, maintain the following values:General dataCash Discount: X <selected>Tax dataTax classification: 1 (Full tax)Then choose Enter. | Sales organizational data is maintained. The Sales: sales org. 2 tab page is displayed. |  |
| 8 | Maintain Sales Organization Data (2) | On the Sales: sales org. 2 view, maintain the following entry:Item category group: SRVP (Service Product)Then choose Enter. | Sales organizational data is maintained. The Sales: General/Plant tab page is displayed. |  |
| 9 | Maintain General Sales Data | On the Sales: General/Plant view, maintain the following values:Base Unit of Measure: HR (Hours)Work Duration: 1 HRService Profile: 5x10 (Mo-Fr: 7-17h)Response Prof.: FIRST (First Level Response Time)Then choose Enter. | General sales data is maintained. |  |
| 10 | Maintain Purchasing Data | On the Purchasing view, in the General Data section, make the following entries:Base Unit of Measure: for example, HRMaterial Group: for example, P001Purchase Group: for example, 001Tax ind. f. material: for example,1Then choose Continue (Enter). | Purchasing Data is maintained. |  |
| 11 | Maintain Accounting Data | On the Accounting 1 view, in the Current Valuation Data section, make the following entry:Base Unit of Measure: for example, HRValuation Class: for example, 3200Then choose Save. | Accounting data is maintained.The service product is saved. The system displays the Create Material (Initial Screen) view. |  |

#### SRV_CONTRACT

Purpose

This material is relevant for cloud edition and on-premise.

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as a Master Data Specialist - Product Data (MDG). | The Home page appears. |  |
| 2 | Access the SAP Fiori app | Choose Create Material app. | The Create Material (Initial Screen) is displayed. |  |
| 3 | Maintain Material Basic Data (for Service Product Service) | On the Create Material (Initial Screen) make the following entries:● Material: SRV_CONTRACT● Industry sector MIf the Industry Sector input field is hidden, no entry is required. When the industry sector is not offered for entry, the field is populated in the dark. Currently only one entry exists for industry (M = Mechanical engineering).● Material Type: Service ProductThen choose Continue (Enter). | You have maintained basic information for the new service product.The Select View(s) dialog window is displayed. |  |
| 4 | Choose Views | On the Select View(s) dialog window, select the following views:Basic data 1Sales: Sales Org. Data 1Sales: Sales Org. Data 2Sales: General/Plant DataThen choose Continue (Enter). | The Organizational Levels screen is displayed. |  |
| 5 | Choose Organizational Levels | On the Organizational Levels window, maintain the following values:• Plant: 1710 (Plant 1 US)• Sales Org.: 1710 (Dom. Sales Org US)• Distr. Channel: 10 (Direct Sales)Then choose Continue (Enter). | Organizational data has been selected.The Create Material SRV_CONTRACT (Service Product) view is displayed. |  |
| 6 | Maintain Basic Data | On the Basic data 1 view, maintain the following values:• Descr.: Service Contract Product• Base Unit of Measure: AU (Activity Unit)• Material Group: P001 (Services)• GenItemGroup: SCNP Serv. Contract Prod.Then choose Continue (Enter). | Basic data is maintained, and Sales: sales org. 1 tab is displayed. |  |
| 7 | Maintain Sales Organization Data (1) | On the Sales: sales org. 1 view, maintain the following values:General data• Cash Discount: X <selected>Tax data• Tax classification: 1 (Full tax)Then choose Continue (Enter). | Sales organizational data is maintained. The Sales: sales org. 2 tab page is displayed. |  |
| 8 | Maintain Sales Organization Data (2) | On the Sales: sales org. 2 view, maintain the following entry:Item category group: SNCP - Serv. Contract Prod.Then choose Continue (Enter). | Sales organizational data is maintained. The Sales: General/Plant tab page is displayed. |  |
| 9 | Maintain General Sales Data | On the Sales: General/Plant view, maintain the following values:• Base Unit of Measure: AU (Activity Unit)• Work Duration: 1 Day (Days)• Service Profile: 5x10 (Mo-Fr: 7-17h)• Response Prof.: FIRST (First Level Response Time)Then choose Save. | General sales data is maintained. |  |

#### SRV_CTR_RENEWAL

Purpose

This material is relevant for cloud edition and on-premise.

This material has auto renewal values defaulted.

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as a Master Data Specialist - Product Data (MDG). | The Home page appears. |  |
| 2 | Access the SAP Fiori app | Choose Create Material app. | The Create Material (Initial Screen) is displayed. |  |
| 3 | Maintain Material Basic Data (for Service Product Service) | On the Create Material (Initial Screen) make the following entries:● Material: SRV_CTR_RENEWAL● Industry sector MIf the Industry Sector input field is hidden, no entry is required. When the industry sector is not offered for entry, the field is populated in the dark. Currently only one entry exists for industry (M = Mechanical engineering).● Material Type: Service ProductThen choose Continue (Enter). | You have maintained basic information for the new service product.You have maintained basic information for the new service product. |  |
| 4 | Choose Views | On the Select View(s) dialog window, select the following views:Basic data 1Sales: Sales Org. Data 1Sales: Sales Org. Data 2Sales: General/Plant DataThen choose Continue (Enter). | The Organizational Levels screen is displayed. |  |
| 5 | Choose Organizational Levels | On the Organizational Levels window, maintain the following values:• Plant: 1710 (Plant 1 US)• Sales Org.: 1710 (Dom. Sales Org US)• Distr. Channel: 10 (Direct Sales)Then choose Continue (Enter). | Organizational data has been selected.The Create Material SRV_CTR_RENEWAL (Service Product) view is displayed. |  |
| 6 | Maintain Basic Data | On the Basic data 1 view, maintain the following values:• Descr.: Service Contract Renewal Product• Base Unit of Measure: AU (Activity Unit)• Material Group: P001 (Services)• GenItemGroup: SCNP Serv. Contract Prod.• Contract Auto Renewal Indicator: 1Then choose Continue (Enter). | Basic data is maintained, and Sales: sales org. 1 tab is displayed. |  |
| 7 | Maintain Sales Organization Data (1) | On the Sales: sales org. 1 view, maintain the following values:General data• Cash Discount: X <selected>Tax data• Tax classification: 1 (Full tax)Then choose Continue (Enter). | Sales organizational data is maintained. The Sales: sales org. 2 tab page is displayed. |  |
| 8 | Maintain Sales Organization Data (2) | On the Sales: sales org. 2 view, maintain the following entry:Grouping Terms• Item category group: SRVP (Service Product)Auto Renewal Extension Period• Default Extension Period: 1• Unit for Extension: Year Then choose Continue (Enter). | Sales organizational data is maintained. The Sales: General/Plant tab page is displayed. |  |
| 9 | Maintain General Sales Data | On the Sales: General/Plant view, maintain the following values:• Base Unit of Measure: AU (Activity Unit)• Work Duration: 1 Day (Days)• Service Profile: 5x10 (Mo-Fr: 7-17h)• Response Prof.: FIRST (First Level Response Time)Then choose Save. | General sales data is maintained.The service product is saved. The system displays the Create Material (Initial Screen) view. |  |

#### SRV_02

Purpose

This material is relevant for cloud edition only.

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as a Master Data Specialist - Product Data (MDG). | The Home page appears. |  |
| 2 | Access the SAP Fiori app | Choose Create Material app. | The Create Material (Initial Screen) is displayed. |  |
| 3 | Maintain Material Basic Data (for Service Product Service Expense) | On the Create Material (Initial Screen) make the following entries:Material: SRV_02Industry sector MIf the Industry Sector input field is hidden, no entry is required. When the industry sector is not offered for entry, the field is populated in the dark. Currently only one entry exists for industry (M = Mechanical engineering).Material Type: Service ProductThen choose Continue (Enter). | You have maintained basic information for the new service product.The Select View(s) dialog window is displayed. |  |
| 4 | Choose Views | On the Select View(s) dialog window, select the following views:Basic data 1Sales: Sales Org. Data 1Sales: Sales Org. Data 2Sales: General/Plant DataInternational Trade: ExportThen choose Continue (Enter). | The Organizational Levels screen is displayed. |  |
| 5 | Choose Organizational Levels | On the Organizational Levels window, maintain the following values:Plant: 1710 (Plant 1 US)Sales Org.: 1710 (Dom. Sales Org US)Distr. Channel: 10 (Direct Sales)Then choose Continue (Enter). | Organizational data has been selected.The Create Material SRV_02 (Service Expenses) view is displayed. |  |
| 6 | Maintain Basic Data | On the Basic data 1 view, maintain the following values:Descr.: Service ExpenseBase Unit of Measure: EA (each)Material Group: P002 (Expenses)GenItemGroup: SRVE (Expense Item)Then choose Continue (Enter). | Basic data has been maintained and Sales: sales org. 1 tab is displayed.Note For every different language used in your company the corresponding description for the product has to be maintained per language code! |  |
| 7 | Maintain Sales Organization Data (1) | On the Sales: sales org. 1 view, maintain the following values:General dataCash Discount: <selected>Tax dataTax classification: 1 (Full tax)Then choose Continue (Enter). | Sales organizational data is maintained. The Sales: sales org. 2 tab page is displayed. |  |
| 8 | Maintain Sales Organization Data (2) | On the Sales: sales org. 2 view, maintain the following entry:Item category group: SRVE (Expense Item)Then choose Continue (Enter). | Sales organizational data is maintained. The service product is saved. |  |

#### FSM – Expense Item

Purpose

This material is relevant for cloud edition only.

Apply service items for FSM (Service Order Processing with SAP Field Service Management) like SRV_02, for example “Expense Item for Accommodation”.

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as Master Data Specialist - Product Data. | The Home page appears. |  |
| 2 | Access the SAP Fiori app | Choose Create Material app. | The Create Material (Initial Screen) is displayed. |  |
| 3 | Maintain Material Basic Data (for Service Product Service Expense) | On the Create Material (Initial Screen) make the following entries:Material: EXP_FSM_ACCOMIndustry sector MIf the Industry Sector input field is hidden, no entry is required. When the industry sector is not offered for entry, the field is populated in the dark. Currently only one entry exists for industry (M = Mechanical engineering).Material Type: Service ProductThen choose Continue (Enter). | You have maintained basic information for the new service product.You also can create as expense material, for example:EXP_FSM_MEALSEXP_FSM_OTHEREXP_FSM_TRAVELEXP_FSM_MILEAGEThe Select View(s) dialog window is displayed. |  |
| 4 | Choose Views | On the Select View(s) dialog window, select the following views:Basic data 1Sales: Sales Org. Data 1Sales: Sales Org. Data 2Sales: General/Plant DataAccounting 1 (only for EXP_FSM_MILEAGE)Then choose Continue (Enter). | The Organizational Levels screen is displayed. |  |
| 5 | Choose Organizational Levels | On the Organizational Levels window, maintain the following values:Plant: 1710 (Plant 1 US)Sales Org.: 1710 (Dom. Sales Org US)Distr. Channel: 10 (Direct Sales)Then choose Continue (Enter). | Organizational data has been selected.The Create Material SRV_02 (Service Expenses) view is displayed. |  |
| 6 | Maintain Basic Data | On the Basic data 1 view, maintain the following values:Description: Service ExpenseFor all expense except EXP_FSM_MILEAGEBase Unit of Measure: EA (each)For expense EXP_FSM_MILEAGEBase Unit of Measure: KM (Kilometer)Material Group: P002 (Expenses)GenItemGroup: SRVE (Expense Item)Then choose Save. | Basic data has been maintained and Sales: sales org. 1 tab is displayed. |  |
| 7 | Maintain Sales Organization Data (1) | On the Sales: sales org. 1 view, maintain the following values:General dataCash Discount: <selected>Tax dataTax classification: 1 (Full tax)Then choose Save. | Sales organizational data is maintained. The Sales: sales org. 2 tab page is displayed. |  |
| 8 | Maintain Sales Organization Data (2) | On the Sales: sales org. 2 view, maintain the following entry:Item category group: SRVE (Expense Item)Then choose Save.For Poland or EXP_FSM_MILEAGE: choose Enter instead of Save. | Sales organizational data is maintained. The expense product is saved. |  |
| 9 | Maintain Accounting 1(only for EXP_FSM_MILEAGE) | On the Accounting 1 view, maintain the following values:Current valuation- Value Class: for example, 3300- Standard Price: for example, 1.50Then choose Save. | Accounting 1 data is maintained. The expense product is saved. |  |

#### SRV_03

Purpose

This material is relevant for cloud edition only.

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as a Master Data Specialist - Product Data (MDG). | The Home page appears. |  |
| 2 | Access the SAP Fiori app | Choose Create Material app. | The Create Material (Initial Screen) is displayed. |  |
| 3 | Maintain Material Basic Data (for Service Product Spare Part) | On the Create Material (Initial Screen) make the following entries:Material: SRV_03Industry sector MIf the Industry Sector input field is hidden, no entry is required. When the industry sector is not offered for entry, the field is populated in the dark. Currently only one entry exists for industry (M = Mechanical engineering).Material Type: Non-Stock MaterialThen choose Continue (Enter). | You have maintained basic information for the new service product.The Select View(s) dialog window is displayed. |  |
| 4 | Choose Views | On the Select View(s) dialog window, select the following views:Basic data 1Sales: Sales Org. Data 1Sales: Sales Org. Data 2Sales: General/Plant DataPurchasingAccounting 1Then choose Continue (Enter). | The Organizational Levels screen is displayed. |  |
| 5 | Choose Organizational Levels | On the Organizational Levels window, maintain the following values:Plant: 1710 (Plant 1 US)Sales Org.: 1710 (Dom. Sales Org US)Distr. Channel: 10 (Direct Sales)Then choose Continue (Enter). | Organizational data has been selected.The Create Material SRV_03 (Spare Part) view is displayed. |  |
| 6 | Maintain Basic Data | On the Basic data 1 view, maintain the following values:Descr.: Spare PartBase Unit of Measure: EA (each)Material Group: YBMM00 (Non-Stock Material without ID)GenItemGroup: SRVM (Service Material)Then choose Continue (Enter). | Basic data is maintained and Sales: sales org. 1 tab is displayed.Note For every different language used in your company the corresponding description for the product has to be maintained per language code! |  |
| 7 | Maintain Sales Organization Data (1) | On the Sales: sales org. 1 view, maintain the following values:General dataCash Discount: <selected>Tax dataTax classification: 1 (Full tax)Then choose Enter. | Sales organizational data is maintained. The Sales: sales org. 2 tab page is displayed. |  |
| 8 | Maintain Sales Organization Data (2) | On the Sales: sales org. 2 view, maintain the following entry:Item category group: SRVM (Service Material) | Sales organizational data is maintained. |  |
| 9 | Maintain Purchasing Data | on the Purchasing view, in the General Data section, make the following entries:Base Unit of Measure : for example, EAMaterial Group : for example, YBM00Purchase Group : for example, 001Tax ind. f. material: for example, 1Then choose Continue (Enter). | Purchasing Data is maintained. |  |
| 10 | Maintain Accounting Data | on the Accounting 1 view, in the Current Valuation Data section, make the following entry:Valuation Class: for example, YB01Price Control: for example, SStandard Price: for example, 1Price Unit: for example, 1Then choose Save. | Accounting data is maintained.The service product is saved. The system displaysCreate Material (Initial Screen) view. |  |

#### SRV_04

Purpose

This material is relevant for cloud edition only.

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as a Master Data Specialist - Product Data (MDG). | The Home page appears. |  |
| 2 | Access the SAP Fiori app | Choose Create Material app. | The Create Material (Initial Screen) is displayed. |  |
| 3 | Maintain Material Basic Data (for Service Product managed Spare Part) | On the Create Material (Initial Screen) make the following entries:● Material: SRV_04● Industry sector MIf the Industry Sector input field is hidden, no entry is required. When the industry sector is not offered for entry, the field is populated in the dark. Currently only one entry exists for industry (M = Mechanical engineering).● Material Type: Non-Stock MaterialThen choose Continue (Enter). | You have maintained basic information for the new service product.The Select View(s) dialog window is displayed. |  |
| 4 | Choose Views | On the Select View(s) dialog window, select the following views:Basic data 1Sales: Sales Org. Data 1Sales: Sales Org. Data 2Sales: General/Plant DataInternational Trade: ExportPurchasingAccounting 1Then choose Continue (Enter). | The Organizational Levelsscreen is displayed. |  |
| 5 | Choose Organizational Levels | On the Organizational Levels window, maintain the following values:● Plant: 1710 (Plant 1 US)● Sales Org.: 1710 (Dom. Sales Org US)● Distr. Channel: 10 (Direct Sales)Then choose Continue (Enter). | Organizational data is selected.The Create Material SRV_04 (managed Spare Part (Non-stock)) view is displayed. |  |
| 6 | Maintain Basic Data | On the Basic data 1 view, maintain the following values:● Descr: Managed Spare Part (Non-stock)● Base Unit of Measure: EA (each)● Material Group: YBMM01 (Non-Stock Material with ID)●GenItemGroup: SRVM (Service Material)Then choose Continue (Enter). | Basic data is maintained and Sales: sales org. 1 tab is displayed.Note For every different language used in your company the corresponding description for the product has to be maintained per language code! |  |
| 7 | Maintain Sales Organization Data (1) | On the Sales: sales org. 1 view, maintain the following values:General data• Cash Discount: <selected>Tax data• Tax classification: 1 (Full tax)Then choose Enter. | Sales organizational data is maintained. The Sales: sales org. 2 tab page is displayed. |  |
| 8 | Maintain Sales Organization Data (2) | On the Sales: sales org. 2 view, maintain the following entry:Item category group: SRVM (Service Material)Then choose Continue (Enter). | Sales organizational data is maintained. |  |
| 9 | Spare PartMaintain Purchasing Data | On the Purchasing view, in the General Data section, make the following entries:• Base Unit of Measure: for example, EA• Material Group: for example, YBMM01• Purchase Group: for example, 001Tax ind. f. material: for example, 1Then choose Continue (Enter). | Purchasing Data is maintained. |  |
| 10 | Maintain Accounting Data | On the Accounting 1 view, in the Current Valuation Data section, make the following entry:• Valuation Class: for example, YB01• Price Control: for example, S• Standard Price: for example, 1• Price Unit: for example, 1Then choose Save. | Accounting data is maintained.The service product is saved.The system displays the Create Material (Initial Screen) view. |  |

#### SRV_BUNDLE_01

Purpose

This material is relevant for cloud edition only.

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as a Master Data Specialist - Product Data (MDG). | The Home page appears. |  |
| 2 | Access the SAP Fiori app | Choose Create Material app. | The Create Material (Initial Screen) is displayed. |  |
| 3 | Maintain Material Basic Data (for Service Product Service) | On the Create Material (Initial Screen) make the following entries:● Material: SRV_BUNDLE_01● Industry sector MIf the Industry Sector input field is hidden, no entry is required. When the industry sector is not offered for entry, the field is populated in the dark. Currently only one entry exists for industry (M = Mechanical engineering).● Material Type: Service ProductThen choose Continue (Enter). | You have maintained basic information for the new service product.The Select View(s) dialog window is displayed. |  |
| 4 | Choose Views | On the Select View(s) dialog window, select the following views:Basic data 1Sales: Sales Org. Data 1Sales: Sales Org. Data 2Sales: General/Plant DataInternational Trade: ExportThen choose Continue (Enter). | The Organizational Levels screen is displayed. |  |
| 5 | Choose Organizational Levels | On the Organizational Levels window, maintain the following values:● Plant: 1710 (Plant 1 US)● Sales Org.: 1710 (Dom. Sales Org US)● Distr. Channel: 10 (Direct Sales)Then choose Continue (Enter). | Organizational data is selected.The Create Material SRV_BUNDLE_01 (Services) view is displayed. |  |
| 6 | Maintain Basic Data | On the Basic data 1 view, maintain the following values:● Descr: Service Bundle Fixed Price● Base Unit of Measure: EA (each)● Material Group: p001 (Services)●GenItemGroup: SVBL (Service Bundle FP)Then choose Continue (Enter). | Basic data is maintained and Sales: sales org. 1 tab is displayed.Note For every different language used in your company the corresponding description for the product has to be maintained per language code! |  |
| 7 | Maintain Sales Organization Data (1) | On the Sales: sales org. 1 view, maintain the following values:General data• Cash Discount:X <selected>Tax data• Tax classification: 1 (Full tax)Then choose Enter. | Sales organizational data is maintained. The Sales: sales org. 2 tab page is displayed. |  |
| 8 | Maintain Sales Organization Data (2) | On the Sales: sales org. 2 view, maintain the following entry:Item category group: SVBL (Service Bundle FP)Then choose Continue (Enter). | Sales organizational data is maintained. The Sales: General/Plant tab page is displayed. |  |
| 9 | Maintain General Sales Data | On the Sales: General/Plant , maintain the following entries:• Base Unit of Measure: EA (Each)• Work Duration: for example, 2 HR (Hours)Then choose Continue (Enter). | General sales Data is maintained. |  |

#### SRV_BUNDLE_02

Purpose

This material is relevant for cloud edition only.

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as a Master Data Specialist - Product Data. | The Home page appears. |  |
| 2 | Access the SAP Fiori app | Choose Create Material app. | The Create Material (Initial Screen) is displayed. |  |
| 3 | Maintain Material Basic Data (for Service Product Service) | On the Create Material (Initial Screen), make the following entries:Material: SRV_BUNDLE_02Industry sectorMIf the Industry Sector input field is hidden, no entry is required. When the industry sector is not offered for entry, the field is populated in the dark. Currently only one entry exists for industry (M = Mechanical engineering).Material Type: Service ProductThen choose Continue (Enter). | You have maintained basic information for the new service product.The Select View(s) dialog window is displayed. |  |
| 4 | Choose Views | On the Select View(s) dialog window, select the following views:Basic data 1Sales: Sales Org. Data 1Sales: Sales Org. Data 2Sales: General/Plant DataThen choose Continue (Enter). | The Organizational Levels screen is displayed. |  |
| 5 | Choose Organizational Levels | On the Organizational Levels window, maintain the following values:Plant: 1710 (Plant 1 US)Sales Org.: 1710 (Dom. Sales Org US)Distr. Channel: 10 (Direct Sales)Then choose Continue (Enter). | Organizational data is selected.The Create Material SRV_BUNDLE_02 (Services) view is displayed. |  |
| 6 | Maintain Basic Data | On the Basic data 1 view, maintain the following values:Descr: Service BundleBase Unit of Measure: EA (each)Material Group: p001 (Services)GenItemGroup: SVBV (Service Bundle T&M)Then choose Continue (Enter). | Basic data is maintained andSales: sales org. 1 tab is displayed.Note For every different language used in your company the corresponding description for the product has to be maintained per language code! |  |
| 7 | Maintain Sales Organization Data (1) | On the Sales: sales org. 1 view, maintain the following values:General dataCash Discount: X <selected>Tax dataTax classification: 1 (Full tax)Then choose Enter. | Sales organizational data is maintained. The Sales: sales org. 2 tab page is displayed. |  |
| 8 | Maintain Sales Organization Data (2) | On the Sales: sales org. 2 view, maintain the following entry:Item category group: SVBV (Service Bundle)Then choose Continue (Enter). | Sales organizational data is maintained. The Sales: General/Plant tab page is displayed. |  |
| 9 | Maintain General Sales Data | On the Sales: General/Plant , maintain the following entries:Base Unit of Measure: EA (Each)Work Duration: for example, 2 HR (Hours)Then choose Save. | General sales Data is maintained. |  |

#### SRV_05

##### Create Basic Data

Purpose

This material is relevant for cloud edition only.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Master Data Specialist - Product Data (MDG). | The SAP Fiori launchpad appears. |  |
| 2 | Access the SAP Fiori App | Choose Create Material app. | The Create Material (Initial Screen) appears. |  |
| 3 | Enter Material Basic Data | In the Create Material (Initial screen)Material: SRV_05Industry sector: MNote If the Industry Sector input field is hidden, no entry is required. When the industry sector is not offered for entry, the field is populated with in the dark.Material type: Trading GoodsChoose Select View(s). | A new window appears, Select View(s). |  |
| 4 | Choose Views | In Select View(s), select Basic data 1 and make the following entries: | Create Material SRV_05 (Trading Goods) opens. |  |
| 5 | Enter Basic Data | Enter:Description: Stock Service PartIn the General Data section, enter the following:Base Unit: PCProduct Group: L001Division: 00GenItemCatGroup: SVST or NORMIn the Dimensions/EANs section, enter the following:Gross Weight: 2Unit of Weight: KGNet Weight: 1 | Note For every different language used in your company the corresponding description for the product has to be maintained per language code! |  |
| 6 | Complete Basic Data | No entries are required for Basic Data 2 you don´t have to make any entries. |  |  |
| 7 | Save Your Data | At the bottom right of the display, choose Save to save your data. | The Create Material (Initial Screen) appears.The Basic Data is created and saved. |  |

##### Create Sales Data

Purpose

This material is relevant for cloud edition only.

Prerequisite

You must complete the previous section, Create Basic Data, before you proceed with this section.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Access the SAP Fiori App | Choose Create Material app. | Create Material (Initial view)is displayed. |  |
| 2 | Enter Material Basic Data | In the Create Material screen, make the following entries:Material: SRV_05Material type: Trading GoodsChoose Select View(s). | After completing entries, a new window opens, Select View(s). |  |
| 3 | Choose Views | In the Select View(s) window select Sales: Sales Org. Data 1, Sales: Sales Org. Data 2 and Sales: General/Plant Data and choose Continue. | A window with Organizational Levels is displayed. |  |
| 4 | Enter Organizational Levels Data | In Organizational Levels, in the Organizational level section, enter descriptions for the following:Plant: 1710Sales Org.: 1710Distr. Channel: 10Choose Continue.Note Information appears at the bottom of the view: The material already exists and will be extended. | Create Material SRV_05 (Trading Goods) view is displayed. |  |
| 5 | Enter Sales Data | In Material SRV_05 (Trading Goods), from the Sales: sales org. 1 tab, in the General data section, make the following entry:Delivering Plant: 1710 |  |  |
| 6 | Enter Sales Data | In Material SRV_05 (Trading Goods), from the Sales: sales org. 1 tab, in the Tax Data section, make the following entriesTax classification: 1Choose the tab Sales: sales org 2. | The next tab Sales: sales org. 2 is displayed. |  |
| 7 | Enter Sales Data | On the Sales: sales org 2 tab, in the Grouping terms section, make the following entries:Acct Assmt Grp Mat.: 01Item category group: SVST or NORMChoose the tab Sales: General/Plant. | The next tab Sales: General/Plant is displayed. |  |
| 8 | Enter Sales Data | On the Sales: General/Plant tab, in the General data section, enter following data:Availability check: SP |  |  |
| 9 | Enter Sales Data | On the Sales: General/Plant tab, in the Shipping data (times in days) section, enter following data:Transp. Grp: 0001Loading Grp: 0001 |  |  |
| 10 | Enter Sales Data | In the General Plant parameters section, enter the following dataProfit Center: <YB700> |  |  |
| For Poland only | Enter Sales Data | In the International Trade: Export section, enter the following data:Control code.: for example, 41.00.30.0 | PKWiU code for Poland is maintained. |  |
| 11 | Save your data | At the bottom of the screen, choose Save. | Your data is saved. |  |

##### Create Purchasing Data

Purpose

This material is relevant for cloud edition only.

Prerequisite

You must complete the previous procedures, before you proceed with this section.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Access the SAP Fiori App | Choose Create Material app tile. | Create Material (Initial Screen) appears. |  |
| 2 | Enter Material Basic Data | In the Create Material screen, make the following entries:Material: SRV_05Material type:Trading Goods (HAWA)Choose Select View(s). | Select View(s) screen opens. |  |
| 3 | Choose Views | In the Select View(s) window select Purchasing and choose Continue. | Organizational Levels is displayed. |  |
| 4 | Enter Organizational Levels Data | In the Organizational Levels screen, in the Organizational level section, make following entry:Plant: 1710Choose Continue.Note A message appears at the bottom of the screen: The material already exists and will be extended. | Create Material SRV_05 (Trading Goods) opens. |  |
| 5 | Enter Purchasing Data | In the Material SRV_05 (Trading Goods) screen, on the Purchasing tab, in the General Data section, make the following entries:Purchasing Group: 001Material Group: L001 |  |  |
| 6 | Enter Purchasing Data | In the Other data/manufacturer data section, make the following entry:GR processing time: for example, 1 |  |  |
| 7 | Save Your Data | At the bottom of the screen, choose Save. | Your data is saved. |  |

##### Create MRP/Planning Data

Purpose

This material is relevant for cloud edition only.

Prerequisite

You must complete the previous procedures, before you proceed with this section.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Access the SAP Fiori App | Choose Create Material app. | Create Material (Initial Screen) opens. |  |
| 2 | Enter Material Basic Data | In the Create Material screen, make the following entries:Material: SRV_05Material type: Trading GoodsChoose Select View(s). | Select View(s) screen opens. |  |
| 3 | Choose Views | In the Select View(s) window select MRP1, MRP2, MRP3, and MRP4 and choose Continue. | Organizational Levels appears. |  |
| 4 | Enter Organizational Levels Data | In the Organizational Levels screen, in the Organizational level section, make following entries:Plant: 1710Storage Location: 171ANote Information appears at the bottom of the screen: The material already exists and will be extended. | The Create Material SRV_05 (Trading Goods) screen opens. |  |
| 5 | Enter MRP/Planning Data | In the Material SRV_05 (Trading Goods) screen, on the MRP1 tab, in the General Data section, make the following entries:MRP Type: NDMRP Controller : <001> |  |  |
| 6 | Enter MRP/Planning Data | In the Lot size data section make the following entry:Lot Sizing Procedure: <EX>Select the next tab MRP 2 | The next tab, MRP 2 opens. |  |
| 7 | Enter MRP/Planning Data | In the Create Material SRV_05 (Trading Goods) screen, on the MRP 2 tab, in the Procurement section, make the following entries:Procurement Type: XIn the Scheduling section, make the following entries:Planned delivery time: for example, 3GR processing time: for example, 1SchedMargin key: for example, 000Select the next tab MRP 3. | The next tab, MRP 3 opens. |  |
| 8 | Enter MRP/Planning Data | In the Create Material SRV_05 (Trading Goods) screen, on the MRP 3 tab, in the Planning section, make the following entries:Strategy Group: for example, 40 |  |  |
| 9 | Enter MRP/Planning Data | In the Availability check section, make the following entries:Availability check: NCTot. repl. Lead time: for example, 3Select the next tab MRP 4 | The next tab, MRP 4 opens. |  |
| 10 | Enter MRP/Planning Data | In the Create Material SRV_05 (Trading Goods) screen, on the MRP 4 tab, in the BOM explosion/dependent requirements section make the following entries:Individual/coll.: <empty> |  |  |
| 11 | Save Your Data | At the bottom of the screen, choose Save. | Your data is saved. |  |

##### Create Storage Location Data

Purpose

This material is relevant for cloud edition only.

Prerequisite

You must complete the previous procedures, before you proceed with this section.

|  |
| --- |
| Note First you create a view for storage location 171A, afterwards you create the very same for storage location 171B. |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Access the SAP Fiori App | Choose Create Material app tile. | Create Material (Initial Screen) opens. |  |
| 2 | Enter Material Basic Data | In the Create Material screen, make the following entries:Material: SRV_05Material type: Trading GoodsChoose Select View(s). | Select View(s) opens. |  |
| 3 | Choose Views | In the Select View(s) window select the following views:General Plant Data/Storage 1General Plant Data/Storage 2Choose Continue. | Organizational Levels is displayed. |  |
| 4 | Enter Organizational Levels Data | In Organizational Levels, in the Organizational level section, make following entries:Plant: 1710Storage Location:171ANote Information appears at the bottom of the screen: The material already exists and will be extended. | Create Material SRV_05 (Trading Goods) opens. |  |
| 5 | Enter Storage Location Data | In the Create Material SRV_05 (Trading Goods) screen, on the Plant data/stor. 1 tab, in the General Data section, make the following entry:Number of GR slips: for example, 1 | The next tab, Plant data/stor.2 opens. |  |
| 6 | Enter Storage Location Data | In the Create Material SRV_05 (Trading Goods) screen, on the Plant data/stor. 2 tab, in the General Data section, make the following entry:Profit Center: YB700 |  |  |
| 7 | Save Your Data | From the bottom of the display, choose Save. | Master Data-Product appears.Your data is saved. |  |

##### Create Accounting Data

Purpose

This material is relevant for cloud edition only.

Prerequisite

You must complete the previous procedures, before you proceed with this section.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Access the SAP Fiori App | Choose Create Material app. | A new window opens, showing the Create Material (Initial Screen). |  |
| 2 | Enter Material Basic Data | In the Create Material (Initial screen) make the following entries:Material: SRV_05Material type: HAWA Trading GoodsChoose Select View(s). | Select View(s) opens. |  |
| 3 | Choose Views | In Select View(s), select the following views:Accounting 1Choose Continue. | Organizational Levels opens. |  |
| 4 | Enter Organizational Levels Data | In the Organizational Levels screen, in the Organizational level section, make following entries:Plant: 1710Note Information appears at the bottom of the screen: The material already exists and will be extended. | Create Material SRV_05 (Trading Goods) opens. |  |
| 5 | Enter Accounting Data | In the Create Material SRV_05 (Trading Goods) screen, on the Accounting 1 tab, in the General Valuation Data section, make the following entry:Valuation Class: 3100Price Determ.: 2 (Transaction-Based) |  |  |
| 6 | Enter Accounting Data | In the Prices and values section, make the following entries:Standard Price: for example, 13.50Price Control: S |  |  |
| 7 | Save Your Data | From the bottom of the display, choose Save. | The Master Data-Product window appears.Your data is saved. |  |

### Set Prices for Materials

#### Price for SRV_01

Purpose

This material is relevant for cloud edition only.

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori launchpad as Pricing Specialist. | The SAP Fiori launchpad opens. |  |
| 2 | Access the SAP Fiori App | Choose Set Material Prices-Sales. | The Change Condition Records view is displayed. |  |
| 3 | Pricing condition type | In the Change Condition Records view, enter the following information:Condition Type: PPR0Then choose Enter. | The Key Combination view is displayed. |  |
| 4 | Key Combination | In the Key combination view, choose the Material with release status option.Then choose Choose (Enter). | The Change Price (PPR0): Selection view is displayed. |  |
| 5 | Selection | In the Change Price (PPR0): Selection view, maintain the following information:Sales Org.: 1710 (Dom. Sales Org US)Distr. Channel: 10 (Direct Sales)Material:SRV_01 (Service Product)Valid On: <Date> for example, today’s dateThen choose Execute. | The Change Price Condition (PPR0): Overview view is displayed. |  |
| 6 | Change price condition | In the Change Price Condition (PPR0): Overview view, maintain the following data for material SRV_01:Material: for example, SRV_01 (Service Product)Amount : for example, 35.00Unit : USDValid From: <Date> for example, today’s dateChoose Enter. | Price conditions for service products SRV_01 has been maintained. |  |
| 7 | Save | Choose Save. | The prices for the service products have been defined. |  |

#### Price for SRV_CONTRACT

Purpose

This material is relevant for cloud edition and on-premise.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori launchpad as Pricing Specialist. | The SAP Fiori launchpad opens. |  |
| 2 | Access the SAP Fiori App | Choose Set Material Prices - Sales . | The Change Condition Records view is displayed. |  |
| 3 | Pricing condition type | In the Change Condition Records view, enter the following information:Condition Type: PSI1Then choose Enter. | The Key Combination view is displayed. |  |
| 4 | Key Combination | In the Key combination view, choose Material .Then choose Enter. | The Change Price (PSI1): Selection view is displayed. |  |
| 5 | Selection | In the Change Price (PSI1): Selection view, maintain the following information:Sales Org.: 1710 (Dom. Sales Org US)Distr. Channel: 10 (Direct Sales)Material:SRV_CONTRACT (Service Contract Product)Valid On: <Date> for example, today’s dateThen choose Execute. | The Change Price Condition (PPSI): Overview view is displayed. |  |
| 6 | Change price condition | In the Change Price Condition (PSI1): Overview view, maintain the following data for material SRV_CONTRACT:Material : for example, SRV_CONTRACT (Service Contract Product)Amount : for example, 100.00Unit : for example, USDValid From: <Date> for example, today’s dateChoose Enter. | Price conditions for the service contract product SRV_CONTRACT is maintained. |  |
| 7 | Save | Choose Save. | The price for the service contract product is saved. |  |

#### Price for SRV_CTR_RENEWAL

Purpose

This material is relevant for cloud edition and on-premise.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori launchpad as Pricing Specialist. | The SAP Fiori launchpad opens. |  |
| 2 | Access the SAP Fiori App | Choose Set Material Prices - Sales. | The Change Condition Records view is displayed. |  |
| 3 | Pricing condition type | In the Change Condition Records view, enter the following information:Condition Type: PSI1Then choose Enter. | The Key Combination view is displayed. |  |
| 4 | Key Combination | In the Key combination view, choose Material .Then choose Enter. | The Change Price (PSI1): Selection view is displayed. |  |
| 5 | Selection | In the Change Price (PSI1): Selection view, maintain the following information:Sales Org.: 1710 (Dom. Sales Org US)Distr. Channel: 10 (Direct Sales)Material:SRV_CTR_RENEWAL (Service Contract Renewal Product)Valid On: <Date> for example, today’s dateThen choose Execute. | The Change Price Condition (PPSI): Overview view is displayed. |  |
| 6 | Change price condition | In the Change Price Condition (PSI1): Overview view, maintain the following data for material SRV_CTR_RENEWAL:Material : for example, SRV_CTR_RENEWAL (Service Contract Renewal Product)Amount : for example, 90.00Unit : for example, USDValid From: <Date> for example, today’s dateChoose Enter. | Price conditions for service contract products SRV_CTR_RENEWAL is maintained. |  |
| 7 | Save | Choose Save. | The prices for the service contract products have been defined. |  |

#### Price for SRV_02

Purpose

This material is relevant for cloud edition and on-premise.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori launchpad as Pricing Specialist. | The SAP Fiori launchpad opens. |  |
| 2 | Access the SAP Fiori App | Choose Set Material Prices - Sales . | The Change Condition Records view is displayed. |  |
| 3 | Pricing condition type | In the Change Condition Records view, enter the following information:Condition Type: PPR0Then choose Enter. | The Key Combination view is displayed. |  |
| 4 | Key Combination | In the Key combination view, choose Material with release status .Then choose Enter. | The Change Price (PPR0): Selection view is displayed. |  |
| 5 | Selection | In the Change Price (PPR0): Selection view, maintain the following information:Sales Org.: 1710 (Dom. Sales Org US)Distr. Channel: 10 (Direct Sales)Material:SRV_02 (Service Expenses)Valid On: <Date> for example, today’s dateThen choose Execute. | The Change Price Condition (PPR0): Overview view is displayed. |  |
| 6 | Change price condition | In the Change Price Condition (PPR0): Overview view, maintain the following data for material SRV_02:Material : for example, SRV_02 (Services)Amount : for example, 15.00Unit : for example, USDValid From: <Date> for example, today’s dateChoose Enter. | Price conditions for service products SRV_02 is maintained. |  |
| 7 | Save | Choose Save. | The prices for the service products have been defined. |  |

#### Price for SRV_04

Purpose

This material is relevant for cloud edition only.

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori launchpad as Pricing Specialist. | The SAP Fiori launchpad opens. |  |
| 2 | Access the SAP Fiori App | Choose Set Material Prices - Sales. | The Change Condition Records view is displayed. |  |
| 3 | Pricing condition type | In the Change Condition Records view, enter the following information:Condition Type: PPR0Then choose Enter. | The Key Combination view is displayed. |  |
| 4 | Key Combination | In the Key combination view, choose Material with release status .Then choose Enter. | The Change Price (PPR0): Selection view is displayed. |  |
| 5 | Selection | In the Change Price (PPR0): Selection view, maintain the following information:Sales Org.: 1710 (Dom. Sales Org US)Distr. Channel: 10 (Direct Sales)Material:SRV_04 (Managed Spare Part (Non-stock))Valid On: <Date> for example, today’s dateThen choose Execute. | The Change Price Condition (PPR0): Overview view is displayed. |  |
| 6 | Change price condition | In the Change Price Condition (PPR0): Overview view, maintain the following data for material SRV_04:Material : SRV_04 (Managed Spare Part (Non-stock))Amount : for example, 15.00Unit: USDValid From: <Date> for example, today’s dateChoose Enter. | Price conditions for service products SRV_04 is maintained. |  |
| 7 | Save | Choose Save. | The prices for the service products have been defined. |  |

#### Price for SRV_BUNDLE_01

Purpose

This material is relevant for cloud edition only.

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori launchpad as Pricing Specialist. | The SAP Fiori launchpad opens. |  |
| 2 | Access the SAP Fiori App | Choose Set Material Prices - Sales . | The Change Condition Records view is displayed. |  |
| 3 | Pricing condition type | In the Change Condition Records view, enter the following information:Condition Type: PPR0Then choose Enter. | The Key Combination view is displayed. |  |
| 4 | Key Combination | In the Key combination view, choose Material with release status .Then choose Enter. | The Change Price (PPR0): Selection view is displayed. |  |
| 5 | Selection | In the Change Price (PPR0): Selection view, maintain the following information:Sales Org.: 1710 (Dom. Sales Org US)Distr. Channel: 10 (Direct Sales)Material:SRV_BUNDLE_01 (Service Bundle 01)Valid On: <Date> for example, today’s dateThen choose Execute. | The Change Price Condition (PPR0): Overview view is displayed. |  |
| 6 | Change price condition | In the Change Price Condition (PPR0): Overview view, maintain the following data for material SRV_01:Material : SRV_BUNDLE_01 (Service Bundle 01)Amount : for example, 200.00Unit: USDValid From: <Date> for example, today’s dateChoose Enter. | Price conditions for service products SRV_BUNDLE_01 is maintained. |  |
| 7 | Save | Choose Save. | The prices for the service products have been defined. |  |

#### Price for SRV_05

Purpose

This material price is relevant for cloud edition only.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as Pricing Specialist. | The SAP Fiori launchpad opens. |  |
| 2 | Access the SAP Fiori App | Choose Set Material Prices - Sales. | The Change Condition Records view is displayed. |  |
| 3 | Pricing condition type | In the Change Condition Records view, enter the following information:Condition Type: PPR0Then choose Enter. | The Key Combination view is displayed. |  |
| 4 | Key Combination | In the Key combination view, choose the Material with release status option.Then choose Choose (Enter). | The Change Price (PPR0): Selection view is displayed. |  |
| 5 | Selection | In the Change Price (PPR0): Selection view, maintain the following information:Sales Org.: 1710 (Dom. Sales Org US)Distr. Channel: 10 (Direct Sales)Material: SRV_05 (Stock Service Part)Valid On: <Date> for example, today’s dateThen choose Execute. | The Change Price Condition (PPR0): Overview view is displayed. |  |
| 6 | Change price condition | In the Change Price Condition (PPR0): Overview view, maintain the following data for material SRV_01:Material: SRV_05 (Stock Service Part)Amount: for example, 14.50Unit: USDValid From: <Date> for example, today’s dateChoose Enter. | PriceCorrection condition for service product SRV_01 has been maintained. |  |
| 7 | Save | Choose Save. | The prices for the service products have been defined. |  |

#### Price for FSM - Expense EXP_FSM_MILEAGE

Purpose

This material is relevant for cloud edition and on-premise.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori launchpad as Pricing Specialist. | The SAP Fiori launchpad opens. |  |
| 2 | Access the SAP Fiori App | Open Set Material Prices - Sales . | The Change Condition Records view is displayed. |  |
| 3 | Pricing condition type | In the Change Condition Records view, enter the following information:Condition Type: PCO4Then choose Enter. | The Key Combination view is displayed. |  |
| 4 | Key Combination | In the Key combination view, choose Material with release status .Then choose Enter. | The Change Price (PCO4): Selection view is displayed. |  |
| 5 | Selection | In the Change Price (PCO4): Selection view, maintain the following information:Sales Org.: 1710 (Dom. Sales Org US)Distr. Channel: 10 (Direct Sales)Material:EXP_FSM_MILEAGEValid On: <Date> for example, today’s dateThen choose Execute. | The Change Price Condition (PCO4): Overview view is displayed. |  |
| 6 | Change price condition | In the Change Price Condition (PCO4): Overview view, maintain the following data for material EXP_FSM_MILEAGE:Material : for example, EXP_FSM_MILEAGEAmount : for example, 1,50 (Price per Unit)Unit : for example, USDValid From: <Date> for example, today’s dateChoose Enter. | Price conditions for service product EXP_FSM_MILEAGE is maintained. |  |
| 7 | Save | Choose Save. | The prices for the service products have been defined. |  |

### Set Prices for Overtime

Purpose

This procedure describes how to set prices for overtime. This chapter is only relevant for 3D2 (cloud edition).

|  |
| --- |
| Note Before you maintain the prices for overtime, you have to create the “Overtime Categories” first.You will find the description in Test Script 3D2, chapter ‘2.5.6 Maintain Overtime Category’! |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori launchpad as Pricing Specialist. | The SAP Fiori launchpad opens. |  |
| 2 | Access the SAP Fiori App | Choose Set Material Prices Sales. | The Change Condition Records view is displayed. |  |
| 3 | Pricing condition type | In the Change Condition Records view, enter the following information:Condition Type: SOV1 or SOV2Then choose Enter. | The screen Change Overtime (SOV1): Selection or Change Overtime (SOV 2 ): Selection opens.Info:Has SOV1 been selected as condition record, you will be able to maintain an absolute value as price.Has SOV2 been selected as condition record, you will be able to maintain a percentage value for price calculation. |  |
| 4 | Selection | In the Change Overtime (SOV1): Selection or Change Overtime (SOV 2 ): Selection view, maintain the following information:Sales Org.: 1710 (Dom. Sales Org US)Distr . Channel: 10 (Direct Sales)Valid On: <Date> for example, today’s dateThen choose Execute. | The Change Overtime (SOV1): Overview or Change Overtime (SOV 2 ): Overview view is displayed. |  |
| 5 | Change price condition | In the Change Overtime (SOV1): Selection or Change Overtime (SOV 2 ): Selection view, maintain one or more price conditions for overtime:Overtime: for example, OV01, OV02, OV03Amount: for example, 30 or 50Unit: for example, USD or %UoM: for example, HRValid From: <Date> for example, today’s dateChoose Enter. |  |  |
| 6 | Save | Choose Save. | Price conditions for overtime calculation have been created |  |

### Creating Condition Record for Accounting Indicator

Purpose

In this step, you define condition records for accounting indicators. This condition can be used in service orders to differentiate between billable, non-billable, and partially billable items for pricing and controlling purposes. Non-billable and partially billable services are, for example, those provided under warranty or in goodwill. Condition record for accounting indicator is optional and only for cloud edition.

Procedure (using Fiori Launchpad)

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log onto the SAP Fiori launchpad as Pricing Specialist. | The SAP Fiori launchpad opens. |  |
| 2 | Access the SAP Fiori App | Choose Set Material Prices - Sales | The Change Condition Records view is displayed. |  |
| 3 | Pricing condition type | In the Change Condition Records view, enter the following information:Condition Type: DAI2Then choose Enter. | The Change Accounting Ind. (DAI2): Selection view is displayed. |  |
| 4 | Selection | In the Change Accounting Ind. (DAI2): Selection view, maintain the following information:Sales Org.: for example, 1710 (Dom. Sales Org US)Distr. Channel: for example, 10 (Direct Sales)Valid On: <Date> for example, today’s dateThen choose Execute. | The Change Accounting Ind. (%) Condition (DAI2): Overview view is displayed. |  |
| 5 | Create condition record | In the Change Accounting Ind. (%) Condition (DAI2) : Overview view, create the following condition for SRV_01:Sales Org: for example, 1710 (Dom. Sales Org US)Distr. Channel: for example, <10> (Direct Sales)Material: for example, <SRV_01>AcctIndic: S1Amount: for example, <-100>Calculat.Type: AValid From: <Date> for example, today’s dateValid To: <Date> for example, today’s date.Choose Enter. | Price condition has been maintained. |  |
| 6 | Save | Choose Save. | Condition records for accounting indicator for the service product is created. |  |

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
> Flagged while digesting this document, not verified: SRV_CONTRACT item category group written SNCP while GenItemGroup is SCNP, possible typo

> [!warning] Conflict
> Flagged while digesting this document, not verified: SRV_CTR_RENEWAL uses item category group SRVP whereas SRV_CONTRACT uses SNCP

> [!warning] Conflict
> Flagged while digesting this document, not verified: Several price steps for SRV_BUNDLE_01 and SRV_05 refer to material SRV_01 in the text (copy-paste)

> [!warning] Conflict
> Flagged while digesting this document, not verified: SRV_06 is listed in the overview table but has no creation procedure

## Connections
- part-of :: [[_cluster]]
- related-to :: [[14-maintenance-service-and-projects/sap-s-4hana-cloud-public-edition-3kv-349]]
- related-to :: [[14-maintenance-service-and-projects/sap-s-4hana-cloud-public-edition-mds-3kv-351]]
- related-to :: [[14-maintenance-service-and-projects/script-de-dados-mestre-criar-produto-de-servicos-para-operacao-de-serv]]
- related-to :: [[14-maintenance-service-and-projects/script-de-datos-maestros-creacion-de-producto-de-servicio-para-proceso]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/3KV_S4CLD2608_Master_Data_EN_XX.docx` — full document · extracted with `mammoth` · 66,532 chars in the whole document
