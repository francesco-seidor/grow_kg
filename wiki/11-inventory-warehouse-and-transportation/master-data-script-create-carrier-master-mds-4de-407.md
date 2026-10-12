---
id: 11-inventory-warehouse-and-transportation/master-data-script-create-carrier-master-mds-4de-407
title: "Master Data Script: Create Carrier Master - MDS (4DE) (4DE_S4CLD2608_Master_Data_EN_XX)"
description: "SAP S/4HANA Cloud Public Edition 2608 master data script (4DE) for creating Business Partner Carriers (road, rail, ocean, forwarder, air) for invoice verification and ERS."
cluster: 11-inventory-warehouse-and-transportation
tags: [kb/inventory-warehouse-and-transportation, topic/carrier-master-data]
aliases: [4DE_S4CLD2608_Master_Data_EN_XX]
keywords: [Carrier Business Partners, carrier master data, business partner creation, invoice verification, evaluated receipt settlement, freight forwarder, business roles, bp groupings, organizational units, supplier roles]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/4DE_S4CLD2608_Master_Data_EN_XX.docx]
confidence: low
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-407
topic: 11-inventory-warehouse-and-transportation/carrier-master-data
language: EN
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Master Data Script: Create Carrier Master - MDS (4DE) (4DE_S4CLD2608_Master_Data_EN_XX)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/4DE_S4CLD2608_Master_Data_EN_XX.docx`, extracted with `mammoth`. Grouped under **Carrier Business Partners** in Inventory, Warehouse and Transportation. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

|  |  |
| --- | --- |
| <!-- image omitted: unnamed --> | Master Data ScriptSAP S/4HANA Cloud Public Edition - 02-07-26 |
|  | Create Carrier Master - MDS (4DE) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Table of Contents

[1 Purpose 3](#_Toc233904719)

[2 Prerequisites 4](#_Toc233904720)

[2.1 System Access 4](#_Toc233904721)

[2.2 Roles 4](#_Toc233904722)

[2.3 Required Organizational Units 4](#_Toc233904723)

[2.4 Main Parameters for Data Creation 5](#_Toc233904724)

[2.4.1 Groupings 5](#_Toc233904725)

[3 Overview Table 6](#_Toc233904726)

[4 Procedures 7](#_Toc233904727)

[4.1 Create Business Partner Carrier (Road) for Invoice Verification Process 7](#_Toc233904728)

[4.2 Create Business Partner Carrier (Road) for Evaluated Receipt Settlement (ERS) Process 11](#_Toc233904729)

[4.3 Create Business Partner Carrier (Rail) for Invoice Verification Process 15](#_Toc233904730)

[4.4 Create Business Partner Carrier (Rail) for Evaluated Receipt Settlement (ERS) Process 18](#_Toc233904731)

[4.5 Create Business Partner Carrier (Ocean) for Invoice Verification Process 22](#_Toc233904732)

[4.6 Create Business Partner Carrier (Ocean) for Evaluated Receipt Settlement (ERS) Process 25](#_Toc233904733)

[4.7 Create Business Partner Carrier (Freight Forwarder) for Invoice Verification Process 29](#_Toc233904734)

[4.8 Create Business Partner Carrier (Freight Forwarder) for Evaluated Receipt Settlement (ERS) Process 33](#_Toc233904735)

[4.9 Create Business Partner Carrier (Air) for Invoice Verification Process 36](#_Toc233904736)

[4.10 Create Business Partner Carrier (Air) for Evaluated Receipt Settlement (ERS) Process 40](#_Toc233904737)

[5 Appendix 44](#_Toc233904738)

## Purpose

This document provides a description for creating a Business Partner - Carrier for your SAP S/4HANA system. The description includes those data segments that are relevant for the SAP S/4HANA appliance, such as Business Partner roles and other relevant fields. Fields that are not relevant for the scope of the SAP S/4HANA content as delivered by SAP Best Practices are not described in this document.

A carrier is a business partner responsible for transporting goods. A carrier can offer services to shippers or freight forwarders.

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
| Master Data Specialist - Business Partner Data | SAP_BR_BUPA_MASTER_SPECIALIST | Master Data - Business Partners / Business Partner Governance / Business Partner Governance / Business Partner Governance | SAP_BR_BUPA_MASTER_SPECIALIST / SAP_CA_SPT_MDG_BP_GOV_PC / SAP_CMD_SPT_BP_GOV_PC / SAP_CA_SPT_MDG_BP_WFUSR_PC |

### Required Organizational Units

Some segments of master data are dependent on the organizational units of the company. General (central) data does not depend on an organizational unit or the company code. The following table gives an overview of these different data segments and their relevant organizational units:

| Data Segment | Depends On | Field Examples | Comments | Organizational Unit to be Used |
| --- | --- | --- | --- | --- |
| Purchasing Data (Materials Management) | Purchasing Organization |  |  |  |
| Company Code | Company Code |  |  |  |

### Main Parameters for Data Creation

In this section, we describe some basic parameters that influence the behavior of a master record and are always required to create a business partner carrier master data record.

#### Groupings

The following groupings are defined for Business Partner Carrier:

| Grouping | Range / IDs | Comments |
| --- | --- | --- |
| External numeric numbering (higher range) | BP03 |  |

## Overview Table

This master record consists of several segments provided in the table below.

|  |
| --- |
| Note If your system administrator has enabled spaces and pages on the SAP Fiori launchpad, the homepage will only contain the essential apps for performing the typical tasks of a business role.You can find all other (searchable) apps not included on the homepage using the search bar ([2434549](https://me.sap.com/notes/2434549)).If you want to personalize the homepage and include the hidden apps, navigate to your user profile and choose App Finder. |

| Segment | Business Role | App/Transaction | Expected Results |
| --- | --- | --- | --- |
| [Create Business Partner Carrier (Road) for Invoice Verification Process](#unique_8) [page ] 7 | Master Data Specialist - Business Partner Data | Maintain Business Partner (BP) | The business partner carrier is created. |

## Procedures

This section describes procedures for each segment or process step that is used for different business processes: Invoice Verification Process and Self-Billing Process.

### Create Business Partner Carrier (Road) for Invoice Verification Process

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

Create a business partner carrier to enable transportation execution. The carrier is assigned to a transportation order (freight order). This carrier is primarily used in the invoice verification process, where the amounts of the carrier invoice are compared with the expected transportation costs calculated in the freight order.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Master Data Specialist - Business Partner Data. | The Start page appears. |  |
| 2 | Access the SAP Fiori App | Maintain Business Partner (BP) | A new window opens, displaying the Maintain Business Partner (BP) screen. |  |
| 3 | Create a BP Organization | Choose Organization. | The Create Organization screen appears. |  |
| 4 | Enter General Data | Make the following entries:Business Partner: <Enter a Business Partner ID that starts with a character>Grouping: <External alpha-numeric numbering>The Create in BP role field is filled by the system with the Business Partner (Gen.) role. Keep this setting. On the Address tab, enter the following information:Name: <Name of organization>Search Term: <Search term for business partner>Note Example values with US localization for the above fields:Business Partner:<17386001>Grouping:<External numeric numbering (higher range) (BP03)>Name: <TM Road Carrier US 1>Search Term:<TMROADCARRUS> |  |  |
| 5 | Enter Identification Data | On the Identification tab for the Business Partner role, enter the following information:Legal form: <Legal form of organization>Example values for the above field: Legal form: <01 (Corporation)>Save your entries. |  |  |
| 6 | Assign New Role Carrier and Enter Address Data | Choose Switch between Display and Change to ensure that you are in change mode. Assign a new BP role Carrier (CRM010) by selecting the role via the dropdown list Change in BP Role.On the Address tab for the BP role enter a carrier with the following information:Street: <Streetname>City postal code: <PostalCode of City>City:<City name>Country:<Country name>Region (State, Province, County):<Region name>Time Zone: <TimeZone>Language: <Languagename>Telephone (dialing code + number):<Telephone number with dialing code>Email: <Emailaddress>Note Example values with US localization for the above fields:Street:<WindgapAve>City postal code:<95206>City:<Pittsburgh>Country: <US>Region (State, Province, County):<PA>Time Zone:<EST>Language: <EN>Telephone (dialing code + number): <412-264-5632>Email : <info@17386001.com> |  |  |
| 7 | Enter Payment Transactions Data for Carrier role | On the Payment Transactions tab for the BP role Carrier, enter the following information:Ctry: <Bank key>Bank key: <Bank key>Bank Account: <Bank account number>Save your entries.Note Example values with US localizations for the above fields:Ctry: <US>Bank key: <150350300>Bank Account: <790133> |  |  |
| 8 | Assign New Role Supplier and Enter Business Partner Data | Assign the new BP role Supplier (FLVN01) by selecting it via the dropdown list Change in BP Role. Then perform the following steps:Choose Purchasing.Enter the following value in the Purch. Organization field: <Purchasing Organization>Choose Enter .Enter the following information on the Purchasing Data tab:Order Currency: <Currency name>Terms of Payment: <Terms of payment>Shipping Conditions: <Shipping Condition name>Purchasing Group: <Purchasing group value>Schema Grp Supp: <value>Save your entries.Note Example values with US localization for the above fields:Order Currency: <USD>Terms of Payment: <0004>Shipping Conditions: <01>Purchasing Group: <005>Schema Grp Supp: <03> |  |  |
| 9 | Assign New Role Supplier FI and enter Business Partner Data | Assign the new BP role Supplier (Fin.Accounting) (FLVN00) by selecting it via the dropdown list.Change in BP RoleChoose Company Code.Enter the Company code: <Company Code>Choose Enter.Enter the following information on the respective tab:Vendor: Account Management.Reconciliation Account: <Account number>Sort key: <Value>Note Example values with US localization for the above fields:Company Code: <1710>Reconciliation Account: <21100000>Sort key: <009> |  |  |
| 10 | Enter Vendor Correspondence Data | Enter the following information on the Vendor Correnspondence tab:Clerk Abbrev.: <Value>Account with vendor: <Value>Note Example values with US localization for the above fields:Clerk Abbrev.: <01>Account with vendor: <1710-CARR1> |  |  |
| 11 | Save Your Data | Choose Save. | The system displays a message that the object is saved. |  |

### Create Business Partner Carrier (Road) for Evaluated Receipt Settlement (ERS) Process

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

Create a business partner carrier to enable transportation execution. The carrier is assigned to a transportation order (freight order). This carrier is primarily used for the Evaluated Receipt Settlement (ERS) scenario, where automated invoice settlement is done, without waiting for a carrier invoice.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as a Master Data Specialist - Business Partner Data. | The Start page appears. |  |
| 2 | Access the SAP Fiori App | Choose Maintain Business Partner (BP). | The Maintain Business Partner (BP) screen is displayed. |  |
| 3 | Create a BP Organization | Choose Organization. | The Create Organization screen appears. |  |
| 4 | Enter General Data | Make the following entries:Business Partner: <Enter a Business Partner ID that starts with a character>Grouping: <External alpha-numeric numbering>The Create in BP role field is filled by the system with the Business Partner (Gen.) role. Keep this setting.On the Address tab, enter the following information:Name: <Name of organization>Search Term: <Search term for business partner>Note Refer to section Master Data, Organizational Data, and Other Data in scenario 3EP - Order-Based Transportation Consolidation to choose the right values.Example values for the above fields:Business Partner: <17386002>Grouping: <External numeric numbering (higher range) (BP03)>Name: TM Road Carrier Self-Billing USSearch Term: <TMROADCARRSBUS> |  |  |
| 5 | Enter Identification Data | On the Identification tab for the Business Partner role, enter the following information:Legal form: <Legal form of organization>Example values for the above field:Legal form: <01 (Corporation)>Save your entries. |  |  |
| 6 | Assign New Role Carrier and enter Address Data | Use the switch between Display and Change to ensure you are in change mode. Assign the new BP Role Carrier(CRM010) by selecting the role via the dropdown list change in BP Role.On the Address tab, enter the following information:Street: <Street name>City postal code: <Postal Code of City>City: <City name>Country: <Country name>Region (State, Province, County): <Region name>Time Zone: <Time Zone>Language: <Language name>Telephone (dialing code + number): <Telephone number with dialing code>Email: <Email address>Note Example values for the above fields:Street: <E Sweet Ave>City postal code: <58504>City: <Bismarck>Country: <US>Region (State, Province, County): <ND>Time Zone: <MST>Language: <EN>Telephone (dialing code + number): <999 254 3623>Email: <info@17386002.com> | The Business Partners role Carrier gets added. |  |
| 7 | Enter Payment Transactions Data for Carrier Role | On the Payment Transactions tab, enter the following information:Ctry: <Bank key>Bank key: <Bank key>Bank Account: <Bank account number>Save your entries.Note Example values for the above fields:Ctry: <US>Bank key: <150350300>Bank Account: <102610> |  |  |
| 8 | Assign New Role Supplier and enter Business Partner Data | Assign the new BP Role Supplier (FLVN01) by selecting the role via the dropdown list change in BP Role.Choose Purchasing.Enter the value in the Purch. Organization: <Purchasing Organization> field.Choose Enter.Enter the following information on the Purchasing Data tab:Order Currency: <Currency name>Terms of Payment: <Terms of payment>Shipping Conditions: <Shipping Condition name>Purchasing Group: <value>Schema Grp Supp: <value>AutoEvalGRSetmt Del: <select>Save your entries.Note Example values for the above fields:Purch. Organization: <1710>Order Currency: <USD>Terms of Payment: <0004>Shipping Conditions: <01>Purchasing Group: <005>Schema Grp Supp: <03>AutoEvalGRSetmt Del: <select> |  |  |
| 9 | Assign New Role Supplier FI and Enter Business Partner Data | Assign the new BP Role Supplier (Fin.Accounting) (FLVN00) by selecting the role via the dropdown list change in BP Role.Choose Company Code.Enter the Company code: <Company Code>Choose Enter.Enter the following information on the Vendor: Account Management tab:Reconciliation Account: <Account number>Sort key: <Value>Note Example values for the above fields:Company Code: <1710>Reconciliation Account: <21100000>Sort key: <009> |  |  |
| 10 | Enter Vendor Correspondence Data | Enter the following information on the Vendor: Correspondence tab:Clerk Abbrev: <Value>Account with vendor: <Value>Note Example values for the above fields:Clerk Abbrev: <01>Account with vendor: <1710-CARR2>. |  |  |
| 11 | Save Your Data | Choose Save. | The system displays a message that the object is saved. |  |

### Create Business Partner Carrier (Rail) for Invoice Verification Process

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

Create a business partner carrier to enable transportation execution. The carrier is assigned to a transportation order (freight order). This carrier is primarily used in the invoice verification process, where the amounts of the carrier invoice are compared with the expected transportation costs calculated in the freight order.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Master Data Specialist - Business Partner Data. | The Start page appears. |  |
| 2 | Access the SAP Fiori App | Maintain Business Partner (BP) | A new window opens, displaying the Maintain Business Partner (BP) screen. |  |
| 3 | Create a BP Organization | Choose Organization. | The Create Organization screen appears. |  |
| 4 | Enter General Data | Make the following entries:Business Partner: <Enter a Business Partner ID that starts with a character>Grouping: <External alpha-numeric numbering>The Create in BP role field is filled by the system with the Business Partner (Gen.) role. Keep this setting. On the Addresstab, enter the following information:Name: <Name of organization>Search Term: <Search term for business partner>Example values with US localization for the above fields:Business Partner:<17386201>Grouping:<External numeric numbering (higher range) (BP03)>Name: <TM Rail Carrier US 1>Search Term:<TMRAILCARRUS1> |  |  |
| 5 | Enter Identification Data | On the Identification tab for the Business Partner role, enter the following information:Legal form: <Legal form of organization>Example values for the above field: Legal form: <01 (Corporation)>Save your entries. |  |  |
| 6 | Assign New Role Carrier and Enter Address Data | Choose Switch between Display and Change to ensure that you are in change mode. Assign a new BP role Carrier (CRM010) by selecting the role via the dropdown list Change in BP Role.On the Address tab for the BP role enter a carrier with the following information:Street: <Streetname>City postal code: <PostalCode of City>City:<City name>Country:<Country name>Region (State, Province, County):<Region name>Time Zone: <TimeZone>Language: <Languagename>Telephone (dialing code + number):<Telephone number with dialing code>Email: <Emailaddress>Example values with US localization for the above fields:Street:<WindgapAve>City postal code:<95206>City:<Pittsburgh>Country: <US>Region (State, Province, County):<PA>Time Zone:<EST>Language: <EN>Telephone (dialing code + number): <412-264-5632>Email : <info@17386201.com> |  |  |
| 7 | Enter Payment Transactions Data for Carrier role | On the Payment Transactions tab for the BP role Carrier, enter the following information:Ctry: <Bank key>Bank key: <Bank key>Bank Account: <Bank account number>Save your entries.Example values with US localizations for the above fields:Ctry: <US>Bank key: <150350300>Bank Account: <790133> |  |  |
| 8 | Assign New Role Supplier and Enter Business Partner Data | Assign the new BP role Supplier (FLVN01) by selecting it via the dropdown list Change in BP Role. Then perform the following steps:Choose Purchasing.Enter the following value in the Purch. Organization field: <Purchasing Organization>Choose Enter .Enter the following information on the Purchasing Data tab:Order Currency: <Currency name>Terms of Payment: <Terms of payment>Shipping Conditions: <Shipping Condition name>Purchasing Group: <Purchasing group value>Schema Grp Supp: <value>Save your entries.Example values with US localization for the above fields:Order Currency: <USD>Terms of Payment: <0004>Shipping Conditions: <01>Purchasing Group: <005>Schema Grp Supp: <03> |  |  |
| 9 | Assign New Role Supplier FI and enter Business Partner Data | Assign the new BP role Supplier (Fin.Accounting) (FLVN00) by selecting it via the dropdown list.Change in BP RoleChoose Company Code.Enter the Company code: <Company Code>Choose Enter.Enter the following information on the respective tab:Vendor: Account Management.Reconciliation Account: <Account number>Sort key: <Value>Example values with US localization for the above fields:Company Code: <1710>Reconciliation Account: <21100000>Sort key: <009> |  |  |
| 10 | Enter Vendor Correspondence Data | Enter the following information on the Vendor Correnspondence tab:Clerk Abbrev.: <Value>Account with vendor: <Value>Example values with US localization for the above fields:Clerk Abbrev.: <01>Account with vendor: <1710-CARR201> |  |  |
| 11 | Save Your Data | Choose Save. | The system displays a message that the object is saved. |  |

### Create Business Partner Carrier (Rail) for Evaluated Receipt Settlement (ERS) Process

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

Create a business partner carrier to enable transportation execution. The carrier is assigned to a transportation order (freight order). This carrier is primarily used for the Evaluated Receipt Settlement (ERS) scenario, where automated invoice settlement is done, without waiting for a carrier invoice.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as a Master Data Specialist - Business Partner Data. | The Start page appears. |  |
| 2 | Access the SAP Fiori App | Choose Maintain Business Partner(BP). | The Maintain Business Partner(BP) screen is displayed. |  |
| 3 | Create a BP Organization | Choose Organization. | The Create Organization screen appears. |  |
| 4 | Enter General Data | Make the following entries:Business Partner: <Enter a Business Partner ID that starts with a character>Grouping: <External alpha-numeric numbering>The Create in BP role field is filled by the system with the Business Partner (Gen.) role. Keep this setting.On the Address tab, enter the following information:Name: <Name of organization>Search Term: <Search term for business partner>Refer to section Master Data, Organizational Data, and Other Data in scenario 3EP - Order-Based Transportation Consolidation to choose the right values.Example values for the above fields:Business Partner: <17386202>Grouping: <External numeric numbering (higher range) (BP03)>Name: <TM Rail Carrier Self-Billing US>Search Term: <TMRAILCARRSBUS> |  |  |
| 5 | Enter Identification Data | On the Identification tab for the Business Partner role, enter the following information:Legal form: <Legal form of organization>Example values for the above field:Legal form: <01 (Corporation)>Save your entries. |  |  |
| 6 | Assign New Role Carrier and enter Address Data | Use the switch between Display and Change to ensure you are in change mode. Assign the new BP Role Carrier(CRM010) by selecting the role via the dropdown list change in BP Role.On the Address tab, enter the following information:Street: <Street name>City postal code: <Postal Code of City>City: <City name>Country: <Country name>Region (State, Province, County): <Region name>Time Zone: <Time Zone>Language: <Language name>Telephone (dialing code + number): <Telephone number with dialing code>Email: <Email address>Example values for the above fields:Street: <E Sweet Ave>City postal code: <58504>City: <Bismarck>Country: <US>Region (State, Province, County): <ND>Time Zone: <MST>Language: <EN>Telephone (dialing code + number): <999 254 3623>Email: <info@17386202.com> | The Business Partners role Carrier gets added. |  |
| 7 | Enter Payment Transactions Data for Carrier Role | On the Payment Transactions tab, enter the following information:Ctry: <Bank key>Bank key: <Bank key>Bank Account: <Bank account number>Save your entries.Example values for the above fields:Ctry: <US>Bank key: <150350300>Bank Account: <102610> |  |  |
| 8 | Assign New Role Supplier and enter Business Partner Data | Assign the new BP Role Supplier (FLVN01) by selecting the role via the dropdown list change in BP Role.Choose Purchasing.Enter the value in the Purch. Organization: <Purchasing Organization> field.Choose Enter.Enter the following information on the Purchasing Data tab:Order Currency: <Currency name>Terms of Payment: <Terms of payment>Shipping Conditions: <Shipping Condition name>Purchasing Group: <value>Schema Grp Supp: <value>AutoEvalGRSetmt Del to Eval. Receipt Settlement: <select>Save your entries.Example values for the above fields:Purch. Organization: <1710>Order Currency: <USD>Terms of Payment: <0004>Shipping Conditions: <01>Purchasing Group: <005>Schema Grp Supp: <03>AutoEvalGRSetmt Del to Eval. Receipt Settlement: <select> |  |  |
| 9 | Assign New Role Supplier FI and Enter Business Partner Data | Assign the new BP Role Supplier (Fin.Accounting) (FLVN00) by selecting the role via the dropdown list change in BP Role.Choose Company Code.Enter the Company code: <Company Code>Choose Enter.Enter the following information on the Vendor: Account Management tab:Reconciliation Account: <Account number>Sort key: <Value>Example values for the above fields:Company Code: <1710>Reconciliation Account: <21100000>Sort key: <009> |  |  |
| 10 | Enter Vendor Correspondence Data | Enter the following information on the Vendor: Correspondence tab:Clerk Abbrev: <Value>Account with vendor: <Value>Example values for the above fields:Clerk Abbrev: <01>Account with vendor: <1710-CARR202>. |  |  |
| 11 | Save Your Data | Choose Save. | The system displays a message that the object is saved. |  |

### Create Business Partner Carrier (Ocean) for Invoice Verification Process

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

Create a business partner carrier to enable transportation execution. The carrier is assigned to a transportation order (freight booking) as executing/invoicing carrier on stage level. This carrier is primarily used in the invoice verification process, where the amounts of the carrier invoice are compared with the expected transportation costs calculated in the freight booking.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Master Data Specialist - Business Partner Data. | The Start page appears. |  |
| 2 | Access the SAP Fiori App | Maintain Business Partner (BP) | A new window opens, displaying the Maintain Business Partner (BP) screen. |  |
| 3 | Create a BP Organization | Choose Organization. | The Create Organization screen appears. |  |
| 4 | Enter General Data | Make the following entries:Business Partner: <Enter a Business Partner ID that starts with a character>Grouping: <External alpha-numeric numbering>The Create in BP role field is filled by the system with the Business Partner (Gen.) role. Keep this setting. On the Addresstab, enter the following information:Name: <Name of organization>Search Term: <Search term for business partner>Example values with US localization for the above fields:Business Partner:<17386301>Grouping:<External numeric numbering (higher range) (BP03)>Name: <TM Ocean Carrier US 1>Search Term:<TMOCEANCARRUS1> |  |  |
| 5 | Enter Identification Data | On the Identification tab for the Business Partner role, enter the following information:Legal form: <Legal form of organization>Example values for the above field: Legal form: <01 (Corporation)>Save your entries. |  |  |
| 6 | Assign New Role Carrier and Enter Address Data | Choose Switch between Display and Change to ensure that you are in change mode. Assign a new BP role Carrier (CRM010) by selecting the role via the dropdown list Change in BP Role.On the Address tab for the BP role enter a carrier with the following information:Street: <Streetname>City postal code: <PostalCode of City>City:<City name>Country:<Country name>Region (State, Province, County):<Region name>Time Zone: <TimeZone>Language: <Languagename>Telephone (dialing code + number):<Telephone number with dialing code>Email: <Emailaddress>Example values with US localization for the above fields:Street:<5301 Waterford at Blue Lagoon>City postal code:<33126>City:<Miami>Country: <US>Region (State, Province, County):<FL>Time Zone:<EST>Language: <EN>Telephone (dialing code + number): <412-264-5632>Email : <info@17386301.com> |  |  |
| 7 | Enter Payment Transactions Data for Carrier role | On the Payment Transactions tab for the BP role Carrier, enter the following information:Ctry: <Bank key>Bank key: <Bank key>Bank Account: <Bank account number>Save your entries.Example values with US localizations for the above fields:Ctry: <US>Bank key: <150350300>Bank Account: <790133> |  |  |
| 8 | Assign New Role Supplier and Enter Business Partner Data | Assign the new BP role Supplier (FLVN01) by selecting it via the dropdown list Change in BP Role. Then perform the following steps:Choose Purchasing.Enter the following value in the Purch. Organization field: <Purchasing Organization>Choose Enter .Enter the following information on the Purchasing Data tab:Order Currency: <Currency name>Terms of Payment: <Terms of payment>Shipping Conditions: <Shipping Condition name>Purchasing Group: <Purchasing group value>Schema Grp Supp: <value>Save your entries.Example values with US localization for the above fields:Order Currency: <USD>Terms of Payment: <0004>Shipping Conditions: <01>Purchasing Group: <005>Schema Grp Supp: <03> |  |  |
| 9 | Assign New Role Supplier FI and enter Business Partner Data | Assign the new BP role Supplier (Fin.Accounting) (FLVN00) by selecting it via the dropdown list.Change in BP RoleChoose Company Code.Enter the Company code: <Company Code>Choose Enter.Enter the following information on the respective tab:Vendor: Account Management.Reconciliation Account: <Account number>Sort key: <Value>Example values with US localization for the above fields:Company Code: <1710>Reconciliation Account: <21100000>Sort key: <009> |  |  |
| 10 | Enter Vendor Correspondence Data | Enter the following information on the Vendor Correnspondence tab:Clerk Abbrev.: <Value>Account with vendor: <Value>Example values with US localization for the above fields:Clerk Abbrev.: <01>Account with vendor: <1710-CARR301> |  |  |
| 11 | Save Your Data | Choose Save. | The system displays a message that the object is saved. |  |

### Create Business Partner Carrier (Ocean) for Evaluated Receipt Settlement (ERS) Process

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

Create a business partner carrier to enable transportation execution. The carrier is assigned to a transportation order (freight booking) as executing/invoicing carrier on stage level. This carrier is primarily used for the Evaluated Receipt Settlement (ERS) scenario, where automated invoice settlement is done, without waiting for a carrier invoice.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as a Master Data Specialist - Business Partner Data. | The Start page appears. |  |
| 2 | Access the SAP Fiori App | Choose Maintain Business Partner(BP). | The Maintain Business Partner(BP) screen is displayed. |  |
| 3 | Create a BP Organization | Choose Organization. | The Create Organization screen appears. |  |
| 4 | Enter General Data | Make the following entries:Business Partner: <Enter a Business Partner ID that starts with a character>Grouping: <External alpha-numeric numbering>The Create in BP role field is filled by the system with the Business Partner (Gen.) role. Keep this setting.On the Address tab, enter the following information:Name: <Name of organization>Search Term: <Search term for business partner>Refer to section Master Data, Organizational Data, and Other Data in scenario 3EP - Order-Based Transportation Consolidation to choose the right values.Example values for the above fields:Business Partner: <17386302>Grouping: <External numeric numbering (higher range) (BP03)>Name: <TM Ocean Carrier Self-Billing US 2>Search Term: <TMOCEANCARRSBUS2> |  |  |
| 5 | Enter Identification Data | On the Identification tab for the Business Partner role, enter the following information:Legal form: <Legal form of organization>Example values for the above field:Legal form: <01 (Corporation)>Save your entries. |  |  |
| 6 | Assign New Role Carrier and enter Address Data | Use the switch between Display and Change to ensure you are in change mode. Assign the new BP Role Carrier(CRM010) by selecting the role via the dropdown list change in BP Role.On the Address tab, enter the following information:Street: <Street name>City postal code: <Postal Code of City>City: <City name>Country: <Country name>Region (State, Province, County): <Region name>Time Zone: <Time Zone>Language: <Language name>Telephone (dialing code + number): <Telephone number with dialing code>Email: <Email address>Example values for the above fields:Street: <888 Brannan Street>City postal code: <94103>City: <San Francisco>Country: <US>Region (State, Province, County): <CA>Time Zone: <PST>Language: <EN>Telephone (dialing code + number): <999 254 3623>Email: <info@17386302.com> | The Business Partners role Carrier gets added. |  |
| 7 | Enter Payment Transactions Data for Carrier Role | On the Payment Transactions tab, enter the following information:Ctry: <Bank key>Bank key: <Bank key>Bank Account: <Bank account number>Save your entries.Example values for the above fields:Ctry: <US>Bank key: <150350300>Bank Account: <102610> |  |  |
| 8 | Assign New Role Supplier and enter Business Partner Data | Assign the new BP Role Supplier (FLVN01) by selecting the role via the dropdown list change in BP Role.Choose Purchasing.Enter the value in the Purch. Organization: <Purchasing Organization> field.Choose Enter.Enter the following information on the Purchasing Data tab:Order Currency: <Currency name>Terms of Payment: <Terms of payment>Shipping Conditions: <Shipping Condition name>Purchasing Group: <value>Schema Grp Supp: <value>AutoEvalGRSetmt Del to Eval. Receipt Settlement: <select>Save your entries.Example values for the above fields:Purch. Organization: <1710>Order Currency: <USD>Terms of Payment: <0004>Shipping Conditions: <01>Purchasing Group: <005>Schema Grp Supp: <03>AutoEvalGRSetmt Del to Eval. Receipt Settlement: <select> |  |  |
| 9 | Assign New Role Supplier FI and Enter Business Partner Data | Assign the new BP Role Supplier (Fin.Accounting) (FLVN00) by selecting the role via the dropdown list change in BP Role.Choose Company Code.Enter the Company code: <Company Code>Choose Enter.Enter the following information on the Vendor: Account Management tab:Reconciliation Account: <Account number>Sort key: <Value>Example values for the above fields:Company Code: <1710>Reconciliation Account: <21100000>Sort key: <009> |  |  |
| 10 | Enter Vendor Correspondence Data | Enter the following information on the Vendor: Correspondence tab:Clerk Abbrev: <Value>Account with vendor: <Value>Example values for the above fields:Clerk Abbrev: <01>Account with vendor: <1710-CARR302>. |  |  |
| 11 | Save Your Data | Choose Save. | The system displays a message that the object is saved. |  |

### Create Business Partner Carrier (Freight Forwarder) for Invoice Verification Process

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

Create a business partner carrier to enable the organization of transport execution. The freight forwarder is assigned to a transportation order (freight booking). This freight forwarder is primarily used for the subcontracting process and the organization of transport execution. The freight forwarder is paid for his service to organize the transport.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Master Data Specialist - Business Partner Data. | The Start page appears. |  |
| 2 | Access the SAP Fiori App | Maintain Business Partner (BP) | A new window opens, displaying the Maintain Business Partner (BP) screen. |  |
| 3 | Create a BP Organization | Choose Organization. | The Create Organization screen appears. |  |
| 4 | Enter General Data | Make the following entries:Business Partner: <Enter a Business Partner ID that starts with a character>Grouping: <External alpha-numeric numbering>The Create in BP role field is filled by the system with the Business Partner (Gen.) role. Keep this setting. On the Addresstab, enter the following information:Name: <Name of organization>Search Term: <Search term for business partner>Example values with US localization for the above fields:Business Partner:<17386401>Grouping:<External numeric numbering (higher range) (BP03)>Name: <TM Freight Forwarder US>Search Term:<TMOCEANFORWUS1> |  |  |
| 5 | Enter Identification Data | On the Identification tab for the Business Partner role, enter the following information:Legal form: <Legal form of organization>Example values for the above field: Legal form: <01 (Corporation)>Save your entries. |  |  |
| 6 | Assign New Role Carrier and Enter Address Data | Choose Switch between Display and Change to ensure that you are in change mode. Assign a new BP role Carrier (CRM010) by selecting the role via the dropdown list Change in BP Role.On the Address tab for the BP role enter a carrier with the following information:Street: <Streetname>City postal code: <PostalCode of City>City:<City name>Country:<Country name>Region (State, Province, County):<Region name>Time Zone: <TimeZone>Language: <Languagename>Telephone (dialing code + number):<Telephone number with dialing code>Email: <Emailaddress>Example values with US localization for the above fields:Street:<131 Aberdeen Dr.>City postal code:<92007>City:<CARDIFF BY THE SEA>Country: <US>Region (State, Province, County):<CA>Time Zone:<PST>Language: <EN>Telephone (dialing code + number): <412-264-5632>Email : <info@17386401.com> |  |  |
| 7 | Enter Payment Transactions Data for Carrier role | On the Payment Transactions tab for the BP role Carrier, enter the following information:Ctry: <Bank key>Bank key: <Bank key>Bank Account: <Bank account number>Save your entries.Example values with US localizations for the above fields:Ctry: <US>Bank key: <150350300>Bank Account: <790133> |  |  |
| 8 | Assign New Role Supplier and Enter Business Partner Data | Assign the new BP role Supplier (FLVN01) by selecting it via the dropdown list Change in BP Role. Then perform the following steps:Choose Purchasing.Enter the following value in the Purch. Organization field: <Purchasing Organization>Choose Enter .Enter the following information on the Purchasing Data tab:Order Currency: <Currency name>Terms of Payment: <Terms of payment>Shipping Conditions: <Shipping Condition name>Purchasing Group: <Purchasing group value>Schema Grp Supp: <value>Save your entries.Example values with US localization for the above fields:Order Currency: <USD>Terms of Payment: <0004>Shipping Conditions: <01>Purchasing Group: <005>Schema Grp Supp: <03> |  |  |
| 9 | Assign New Role Supplier FI and enter Business Partner Data | Assign the new BP role Supplier (Fin.Accounting) (FLVN00) by selecting it via the dropdown list.Change in BP RoleChoose Company Code.Enter the Company code: <Company Code>Choose Enter.Enter the following information on the respective tab:Vendor: Account Management.Reconciliation Account: <Account number>Sort key: <Value>Example values with US localization for the above fields:Company Code: <1710>Reconciliation Account: <21100000>Sort key: <009> |  |  |
| 10 | Enter Vendor Correspondence Data | Enter the following information on the Vendor Correnspondence tab:Clerk Abbrev.: <Value>Account with vendor: <Value>Example values with US localization for the above fields:Clerk Abbrev.: <01>Account with vendor: <1710-CARR401> |  |  |
| 11 | Save Your Data | Choose Save. | The system displays a message that the object is saved. |  |

### Create Business Partner Carrier (Freight Forwarder) for Evaluated Receipt Settlement (ERS) Process

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

Create a business partner carrier to enable the organization of transport execution. The freight forwarder is assigned to a transportation order (freight booking). This freight forwarder is primarily used for the subcontracting process and the organization of transport execution. The freight forwarder is paid for his service to organize the transport.This freight forwarder is primarily used for the Evaluated Receipt Settlement (ERS) scenario, where automated invoice settlement is done, without waiting for a carrier invoice.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as a Master Data Specialist - Business Partner Data. | The Start page appears. |  |
| 2 | Access the SAP Fiori App | Choose Maintain Business Partner(BP). | The Maintain Business Partner(BP) screen is displayed. |  |
| 3 | Create a BP Organization | Choose Organization. | The Create Organization screen appears. |  |
| 4 | Enter General Data | Make the following entries:Business Partner: <Enter a Business Partner ID that starts with a character>Grouping: <External alpha-numeric numbering>The Create in BP role field is filled by the system with the Business Partner (Gen.) role. Keep this setting.On the Address tab, enter the following information:Name: <Name of organization>Search Term: <Search term for business partner>Refer to section Master Data, Organizational Data, and Other Data in scenario 3EP - Order-Based Transportation Consolidation to choose the right values.Example values for the above fields:Business Partner: <17386402>Grouping: <External numeric numbering (higher range) (BP03)>Name: <TM Freight Forwarder Self-Billing US>Search Term: <TMOCEANFORWSBUS1> |  |  |
| 5 | Enter Identification Data | On the Identification tab for the Business Partner role, enter the following information:Legal form: <Legal form of organization>Example values for the above field:Legal form: <01 (Corporation)>Save your entries. |  |  |
| 6 | Assign New Role Carrier and enter Address Data | Use the switch between Display and Change to ensure you are in change mode. Assign the new BP Role Carrier(CRM010) by selecting the role via the dropdown list change in BP Role.On the Address tab, enter the following information:Street: <Street name>City postal code: <Postal Code of City>City: <City name>Country: <Country name>Region (State, Province, County): <Region name>Time Zone: <Time Zone>Language: <Language name>Telephone (dialing code + number): <Telephone number with dialing code>Email: <Email address>Example values for the above fields:Street: <2601 Westheimer Road>City postal code: <77098>City: <Houston>Country: <US>Region (State, Province, County): <TX>Time Zone: <CST>Language: <EN>Telephone (dialing code + number): <999 254 3623>Email: <info@17386402.com> | The Business Partners role Carrier gets added. |  |
| 7 | Enter Payment Transactions Data for Carrier Role | On the Payment Transactions tab, enter the following information:Ctry: <Bank key>Bank key: <Bank key>Bank Account: <Bank account number>Save your entries.Example values for the above fields:Ctry: <US>Bank key: <150350300>Bank Account: <102610> |  |  |
| 8 | Assign New Role Supplier and enter Business Partner Data | Assign the new BP Role Supplier (FLVN01) by selecting the role via the dropdown list change in BP Role.Choose Purchasing.Enter the value in the Purch. Organization: <Purchasing Organization> field.Choose Enter.Enter the following information on the Purchasing Data tab:Order Currency: <Currency name>Terms of Payment: <Terms of payment>Shipping Conditions: <Shipping Condition name>Purchasing Group: <value>Schema Grp Supp: <value>AutoEvalGRSetmt Del to Eval. Receipt Settlement: <select>Save your entries.Example values for the above fields:Purch. Organization: <1710>Order Currency: <USD>Terms of Payment: <0004>Shipping Conditions: <01>Purchasing Group: <005>Schema Grp Supp: <03>AutoEvalGRSetmt Del to Eval. Receipt Settlement: <select> |  |  |
| 9 | Assign New Role Supplier FI and Enter Business Partner Data | Assign the new BP Role Supplier (Fin.Accounting) (FLVN00) by selecting the role via the dropdown list change in BP Role.Choose Company Code.Enter the Company code: <Company Code>Choose Enter.Enter the following information on the Vendor: Account Management tab:Reconciliation Account: <Account number>Sort key: <Value>Example values for the above fields:Company Code: <1710>Reconciliation Account: <21100000>Sort key: <009> |  |  |
| 10 | Enter Vendor Correspondence Data | Enter the following information on the Vendor: Correspondence tab:Clerk Abbrev: <Value>Account with vendor: <Value>Example values for the above fields:Clerk Abbrev: <01>Account with vendor: <1710-CARR402>. |  |  |
| 11 | Save Your Data | Choose Save. | The system displays a message that the object is saved. |  |

### Create Business Partner Carrier (Air) for Invoice Verification Process

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

Create a business partner carrier to enable transportation execution. The carrier is assigned to a transportation order (freight booking) as executing/invoicing carrier on stage level. This carrier is primarily used in the invoice verification process, where the amounts of the carrier invoice are compared with the expected transportation costs calculated in the freight booking.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Master Data Specialist - Business Partner Data. | The Start page appears. |  |
| 2 | Access the SAP Fiori App | Maintain Business Partner (BP) | A new window opens, displaying the Maintain Business Partner (BP) screen. |  |
| 3 | Create a BP Organization | Choose Organization. | The Create Organization screen appears. |  |
| 4 | Enter General Data | Make the following entries:Business Partner: <Enter a Business Partner ID that starts with a character>Grouping: <External alpha-numeric numbering>The Create in BP role field is filled by the system with the Business Partner (Gen.) role. Keep this setting. On the Addresstab, enter the following information:Name: <Name of organization>Search Term: <Search term for business partner>Example values with US localization for the above fields:Business Partner:<17386501>Grouping:<External numeric numbering (higher range) (BP03)>Name: <TM Airline US 1>Search Term:<TMAIRLINEUS1> |  |  |
| 5 | Enter Identification Data | On the Identification tab for the Business Partner role, enter the following information:Legal form: <Legal form of organization>Example values for the above field: Legal form: <01 (Corporation)>Save your entries. |  |  |
| 6 | Assign New Role Carrier and Enter Address Data | Choose Switch between Display and Change to ensure that you are in change mode. Assign a new BP role Carrier (CRM010) by selecting the role via the dropdown list Change in BP Role.On the Address tab for the BP role enter a carrier with the following information:Street: <Streetname>City postal code: <PostalCode of City>City:<City name>Country:<Country name>Region (State, Province, County):<Region name>Time Zone: <TimeZone>Language: <Languagename>Telephone (dialing code + number):<Telephone number with dialing code>Email: <Emailaddress>Example values with US localization for the above fields:Street:<5301 Waterford at Blue Lagoon>City postal code:<33126>City:<Miami>Country: <US>Region (State, Province, County ):<FL>Time Zone:<EST>Language: <EN>Telephone (dialing code + number): <412-264-5632>Email : <info@17386501.com> |  |  |
| 7 | Enter Payment Transactions Data for Carrier role | On the Payment Transactions tab for the BP role Carrier, enter the following information:Ctry: <Bank key>Bank key: <Bank key>Bank Account: <Bank account number>Save your entries.Example values with US localizations for the above fields:Ctry: <US>Bank key: <150350300>Bank Account: <790133> |  |  |
| 8 | Assign New Role Supplier and Enter Business Partner Data | Assign the new BP role Supplier (FLVN01) by selecting it via the dropdown list Change in BP Role. Then perform the following steps:Choose Purchasing.Enter the following value in the Purch. Organization field: <Purchasing Organization>Choose Enter .Enter the following information on the Purchasing Data tab:Order Currency: <Currency name>Terms of Payment: <Terms of payment>Shipping Conditions: <Shipping Condition name>Purchasing Group: <Purchasing group value>Schema Grp Supp: <value>Save your entries.Example values with US localization for the above fields:Order Currency: <USD>Terms of Payment: <0004>Shipping Conditions: <01>Purchasing Group: <005>Schema Grp Supp: <03> |  |  |
| 9 | Assign New Role Supplier FI and enter Business Partner Data | Assign the new BP role Supplier (Fin.Accounting) (FLVN00) by selecting it via the dropdown list.Change in BP RoleChoose Company Code.Enter the Company code: <Company Code>Choose Enter.Enter the following information on the respective tab:Vendor: Account Management.Reconciliation Account: <Account number>Sort key: <Value>Example values with US localization for the above fields:Company Code: <1710>Reconciliation Account: <21100000>Sort key: <009> |  |  |
| 10 | Enter Vendor Correspondence Data | Enter the following information on the Vendor Correnspondence tab:Clerk Abbrev.: <Value>Account with vendor: <Value>Example values with US localization for the above fields:Clerk Abbrev.: <01>Account with vendor: <1710-CARR501> |  |  |
| 11 | Save Your Data | Choose Save. | The system displays a message that the object is saved. |  |

### Create Business Partner Carrier (Air) for Evaluated Receipt Settlement (ERS) Process

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

Create a business partner carrier to enable transportation execution. The carrier is assigned to a transportation order (freight booking) as executing/invoicing carrier on stage level. This carrier is primarily used for the Evaluated Receipt Settlement (ERS) scenario, where automated invoice settlement is done, without waiting for a carrier invoice.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as a Master Data Specialist - Business Partner Data. | The Start page appears. |  |
| 2 | Access the SAP Fiori App | Choose Maintain Business Partner(BP). | The Maintain Business Partner(BP) screen is displayed. |  |
| 3 | Create a BP Organization | Choose Organization. | The Create Organization screen appears. |  |
| 4 | Enter General Data | Make the following entries:Business Partner: <Enter a Business Partner ID that starts with a character>Grouping: <External alpha-numeric numbering>The Create in BP role field is filled by the system with the Business Partner (Gen.) role. Keep this setting.On the Address tab, enter the following information:Name: <Name of organization>Search Term: <Search term for business partner>Refer to section Master Data, Organizational Data, and Other Data in scenario 3EP - Order-Based Transportation Consolidation to choose the right values.Example values for the above fields:Business Partner: <17386502>Grouping: <External numeric numbering (higher range) (BP03)>Name: <TM Airline Self-Billing US 2>Search Term: <TMAIRLINESBUS2> |  |  |
| 5 | Enter Identification Data | On the Identification tab for the Business Partner role, enter the following information:Legal form: <Legal form of organization>Example values for the above field:Legal form: <01 (Corporation)>Save your entries. |  |  |
| 6 | Assign New Role Carrier and enter Address Data | Use the switch between Display and Change to ensure you are in change mode. Assign the new BP Role Carrier(CRM010) by selecting the role via the dropdown list change in BP Role.On the Address tab, enter the following information:Street: <Street name>City postal code: <Postal Code of City>City: <City name>Country: <Country name>Region (State, Province, County): <Region name>Time Zone: <Time Zone>Language: <Language name>Telephone (dialing code + number): <Telephone number with dialing code>Email: <Email address>Example values for the above fields:Street: <888 Brannan Street>City postal code: <94103>City: <San Francisco>Country: <US>Region (State, Province, County): <CA>Time Zone: <PST>Language: <EN>Telephone (dialing code + number): <999 254 3623>Email: <info@17386502.com> | The Business Partners role Carrier gets added. |  |
| 7 | Enter Payment Transactions Data for Carrier Role | On the Payment Transactions tab, enter the following information:Ctry: <Bank key>Bank key: <Bank key>Bank Account: <Bank account number>Save your entries.Example values for the above fields:Ctry: <US>Bank key: <150350300>Bank Account: <102610> |  |  |
| 8 | Assign New Role Supplier and enter Business Partner Data | Assign the new BP Role Supplier (FLVN01) by selecting the role via the dropdown list change in BP Role.Choose Purchasing.Enter the value in the Purch. Organization: <Purchasing Organization> field.Choose Enter.Enter the following information on the Purchasing Data tab:Order Currency: <Currency name>Terms of Payment: <Terms of payment>Shipping Conditions: <Shipping Condition name>Purchasing Group: <value>Schema Grp Supp: <value>Eval Receipt Settlement: <select>Save your entries.Example values for the above fields:Purch. Organization: <1710>Order Currency: <USD>Terms of Payment: <0004>Shipping Conditions: <01>Purchasing Group: <005>Schema Grp Supp: <03>Eval Receipt Settlement: <select> |  |  |
| 9 | Assign New Role Supplier FI and Enter Business Partner Data | Assign the new BP Role Supplier (Fin.Accounting) (FLVN00) by selecting the role via the dropdown list change in BP Role.Choose Company Code.Enter the Company code: <Company Code>Choose Enter.Enter the following information on the Vendor: Account Management tab:Reconciliation Account: <Account number>Sort key: <Value>Example values for the above fields:Company Code: <1710>Reconciliation Account: <21100000>Sort key: <009> |  |  |
| 10 | Enter Vendor Correspondence Data | Enter the following information on the Vendor: Correspondence tab:Clerk Abbrev: <Value>Account with vendor: <Value>Example values for the above fields:Clerk Abbrev: <01>Account with vendor: <1710-CARR502>. |  |  |
| 11 | Save Your Data | Choose Save. | The system displays a message that the object is saved. |  |

## Appendix

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
> Flagged while digesting this document, not verified: Overview Table lists only the Road invoice verification segment although ten procedures exist; the introduction mentions a Self-Billing Process while sections are titled ERS

> [!warning] Conflict
> Flagged while digesting this document, not verified: Step 4 instructs a grouping of 'External alpha-numeric numbering' but the example uses External numeric numbering (BP03) with numeric IDs

> [!warning] Conflict
> Flagged while digesting this document, not verified: Purchasing Data field is named differently across variants (AutoEvalGRSetmt Del, AutoEvalGRSetmt Del to Eval. Receipt Settlement, Eval Receipt Settlement)

## Connections
- part-of :: [[_cluster]]
- related-to :: [[11-inventory-warehouse-and-transportation/mds-4de-411]]
- related-to :: [[11-inventory-warehouse-and-transportation/mds-4de-master-data-script-create-carrier-master-409]]
- related-to :: [[11-inventory-warehouse-and-transportation/script-de-dados-mestre-criar-mestre-de-transportadoras-mds-4de-410]]
- related-to :: [[11-inventory-warehouse-and-transportation/script-de-datos-maestros-creacion-de-maestro-de-transportistas-mds-4de]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/4DE_S4CLD2608_Master_Data_EN_XX.docx` — full document · extracted with `mammoth` · 59,123 chars in the whole document
