---
id: 15-retail-operations/test-script-store-connectivity-outbound-3i2-ae-sap-s-4hana-cloud-publi
title: "Test Script: Store Connectivity – Outbound (3I2_AE), SAP S/4HANA Cloud Public Edition (3I2_S4CLD2608_BPD_EN_AE)"
description: "SAP S/4HANA Cloud Public Edition test script for scope item 3I2 (AE): replicating retail article master data and sales prices to store POS, initial and delta, with monitoring."
cluster: 15-retail-operations
tags: [kb/retail-operations, topic/store-connectivity]
aliases: [3I2_S4CLD2608_BPD_EN_AE]
keywords: [Store Connectivity (POS Inbound and Outbound), store connectivity outbound, pos master data replication, initial replication, delta replication, communication arrangements, replication logs, application interface framework, manual replication, replication filters]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/3I2_S4CLD2608_BPD_EN_AE.docx]
confidence: high
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-942
topic: 15-retail-operations/store-connectivity
language: EN
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Test Script: Store Connectivity – Outbound (3I2_AE), SAP S/4HANA Cloud Public Edition (3I2_S4CLD2608_BPD_EN_AE)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/3I2_S4CLD2608_BPD_EN_AE.docx`, extracted with `mammoth`. Grouped under **Store Connectivity (POS Inbound and Outbound)** in Retail Operations. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

| <!-- image omitted: unnamed --> | Test ScriptSAP S/4HANA Cloud Public Edition - 19-06-26 |
| --- | --- |
|  | Store Connectivity – Outbound (3I2_AE) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Table of Contents

[1 Purpose 3](#_Toc232852831)

[2 Prerequisites 4](#_Toc232852832)

[2.1 System Access 4](#_Toc232852833)

[2.2 Roles 4](#_Toc232852834)

[2.3 Master Data, Organizational Data, and Other Data 5](#_Toc232852835)

[2.4 Business Conditions 6](#_Toc232852836)

[2.5 Additional Manual Configuration 6](#_Toc232852837)

[3 Overview Table 7](#_Toc232852838)

[4 Test Procedures 9](#_Toc232852839)

[4.1 Schedule Job for Initial Replication 9](#_Toc232852840)

[4.2 Monitor Message Summary in SAP Application Interface Framework 10](#_Toc232852841)

[4.3 Replicate with Global Filter (Optional) 11](#_Toc232852842)

[4.4 Replicate with Manual Selection (Optional) 13](#_Toc232852843)

[4.5 Analyze Replication Logs 15](#_Toc232852844)

[4.6 Change Product Master Data 16](#_Toc232852845)

[4.6.1 Change Sales Price of Product 16](#_Toc232852846)

[4.6.2 Change Other Product Attributes (Optional) 17](#_Toc232852847)

[4.7 Schedule Job for Delta Replication 18](#_Toc232852848)

[4.8 Replicate Specific Data by Using Replication Model (Optional) 19](#_Toc232852849)

[4.9 Display Replication Status 20](#_Toc232852850)

[4.10 Monitor Message Summary in SAP Application Interface Framework 21](#_Toc232852851)

[5 Appendix 23](#_Toc232852852)

[5.1 Process Integration 23](#_Toc232852853)

[5.1.1 Preceding Processes 23](#_Toc232852854)

[5.1.2 Succeeding Processes 23](#_Toc232852855)

## Purpose

Overview

Point-of-sale (POS) systems in the stores must be provided with the data necessary to enable selling articles to consumers, such as sales prices and article master data (including article description, tax information, and Global Trade Item Number (GTIN) for scanning). You can configure messages such that only needed information is gathered (for example, supplier and purchase price). Obviously, it's of major importance that information in the POS solutions is always up to date. This can be ensured via the following process variants:

- Supply the POS with all needed master data via an initial load, for example when a new store is opened
- Automatically update the POS with the changed article data in regular intervals
- In exceptional cases, you can manually start an immediate supply of the POS, such as for short-term sales price changes

Technically, the communication is implemented as an asynchronous SOAP service.

This document provides a detailed procedure for testing this scope item after solution activation, reflecting the predefined scope of the solution. Each process step, report, or item is covered in its own section, providing the system interactions (test steps) in a table view. Steps that are not in scope of the process but are needed for testing are marked accordingly. Project-specific steps must be added.

|  |
| --- |
| Note Values in this test script (decimal notation, date formats, and so on) are presented in U.S. standard notation. If your test system is set up to use a different notation, enter values as appropriate. |

|  |
| --- |
| Note In the retail industry, specific terms differ from the standard terms used in other lines of business. Therefore, SAP solutions which provide business processes across multiple lines of businesses may use terms for the corresponding business objects, transactions, and user interfaces that deviate from the retail terminology. For integration and reuse reasons, the SAP S/4HANA Cloud Public Edition, retail, fashion, and vertical business business may thus include different terms that refer to the same concept. SAP intends to harmonize the terminology in the future.The following terms are used synonymously in this document:Table 1:Standard Terms in Lines of BusinessSAP S/4HANA Cloud Public Edition, retail, fashion, and vertical business businessMaterial, productArticleMaterial group, product groupMerchandise categoryPlant, locationSite (as superordinate term) - store and distribution center (DC) |

## Prerequisites

This chapter summarizes all the prerequisites for conducting the test in terms of systems, users, master data, organizational data, other test data, and business conditions.

### System Access

|  |  |
| --- | --- |
|  | Details |
| System | Accessible through SAP Fiori launchpad. Your system administrator provides you with the URL to access the various apps assigned to your role. |

### Roles

Create business roles using the following business role templates delivered by SAP and assign them to your individual test users.

Alternatively, if available, you can use the following spaces delivered by SAP. You create a space with pages containing predefined essential apps and assign it to the business role. You then assign this business role to your individual users.

For more information, refer to How to Create a Business Role from a Template in the [product assistance](https://help.sap.com/docs/SAP_S4HANA_CLOUD/53e36b5493804bcdb3f6f14de8b487dd/ec310a8b669a45ca898dc4dd91d97de2.html) for SAP S/4HANA Cloud Public Edition.

| Name (Role Template) | ID (Role Template) | Name (Launchpad Space) | ID (Launchpad Space) | Log On |
| --- | --- | --- | --- | --- |
| Administrator | SAP_BR_ADMINISTRATOR | Communication Management | SAP_BR_ADMINISTRATOR / SAP_BUM_SPT_ADMINISTRATION_PC / SAP_EI_SPT_ADM_LC_PC / SAP_CA_SPT_TDR_PC / SAP_OC_SPT_ADMINISTRATION_PC |  |
| Configuration Expert - Business Network Integration | SAP_BR_CONF_EXPERT_BUS_NET_INT | Message Monitoring | SAP_BR_CONF_EXPERT_BUS_NET_INT |  |
| Pricing Specialist (Retail) | SAP_BR_PRICING_SPCLST_RFM | Retail Pricing - Price Calculation | SAP_BR_PRICING_SPCLST_RFM |  |
| Purchaser (Retail) | SAP_BR_PURCHASER_RFM | Retail Purchasing | SAP_BR_PURCHASER_RFM |  |
| Master Data Specialist - Product Data | SAP_BR_PRODMASTER_SPECIALIST | Product Master | SAP_BR_PRODMASTER_SPECIALIST / SAP_CMD_SPT_PR_GOV_PC |  |

### Master Data, Organizational Data, and Other Data

The organizational structure and master data of your company have been created in your system during activation. The organizational structure reflects the structure of your company. The master data represents materials, customers, and suppliers, for example, depending on the operational focus of your company.

Use your own master data or the following sample data to go through the test procedure.

|  |
| --- |
| Note In the following table, sample values for master data are provided for the country/region US. You can either use the country-dependent sample master data or create and use your own master data while executing the test procedure. |

| Data | Sample Value | Details | Comments |
| --- | --- | --- | --- |
| Single Article (Material or Product) | R_2004 | Relax Body Lotion, 200 ml |  |
| Single Article (Material or Product) | R_2005 | Showergel with caffeine, 200 ml |  |
| Single Article (Material or Product) | R_2003 | Organic Low fat milk, 1,5 % |  |
| Generic Article (Material or Product) | R_1080 | Cycling Jersey Longsleeve |  |
| Sales set Article (Material or Product) | R_2020 | Gift Set Shower Gel & Body Lotion |  |
| Store (Site) | 3340 | Store 3340 AE |  |
| Store (Site) | 3341 | Store 3341 AE |  |
| Store (Site) | 3342 | Store 3342 AE |  |
| Store (Site) | 3343 | Store 3343 AE |  |
| Store (Site) | 3344 | Store 3344 AE |  |
| Sales organization | 3310 | Dom. Sales Org |  |
| Distribution channel | 40 | Store Sales |  |
| Division | 00 | Product Division 00 |  |
| Product Group (Material Group or Merchandise Category) | R2121001 | Body Care |  |
| Product Group (Material Group or Merchandise Category) | R2121002 | Hair Care |  |
| Product Group (Material Group or Merchandise Category) | R1182002 | Milk |  |
| Product Group (Material Group or Merchandise Category) | R5121001 | T-shirts |  |
| Product Group (Material Group or Merchandise Category) | R1161002 | Soft Drinks |  |

### Business Conditions

The business process described in this test script is part of a bigger chain of integrated business processes or scope items. As a consequence, the following business conditions must be met before you can test this scope item,

| Scope Item ID | Business Condition |
| --- | --- |
| 3I1 - Products for Retail | Must be run before this test script. |
| 3I4 - Sales Pricing for Retail | Must be run before this test script. |

### Additional Manual Configuration

Before you can test this scope item, you must have completed the additional configuration steps that are described in the Set-Up Instructions for this scope item. These configuration steps are specific for your implementation and include mandatory settings that are not delivered by SAP and must be created by you. For more information, follow the link to the document:

[Link to Set-Up Instructions](https://help.sap.com/docs/SAP_S4HANA_BEST_PRACTICES/f9d241ab1c9262a7f7d344882f0a6da5)

## Overview Table

This scope item consists of several process steps provided in the table below.

|  |
| --- |
| Note If your system administrator has enabled spaces and pages on the SAP Fiori launchpad, the homepage will only contain the essential apps for performing the typical tasks of a business role.You can find all other (searchable) apps not included on the homepage using the search bar ([2434549](https://me.sap.com/notes/2434549)).If you want to personalize the homepage and include the hidden apps, navigate to your user profile and choose App Finder. |

| Process Step | Business Role | App/Transaction | Expected Results |
| --- | --- | --- | --- |
| Initial Replication by Scheduling Job |  |  |  |
| [Schedule Job for Initial Replication](#unique_9) [page ] 9 | Administrator | Communication Arrangements (F1763) | You have schedule jobs for initial replication of product master data. |
| [Monitor Message Summary in SAP Application Interface Framework](#unique_10) [page ] 21 | Configuration Expert - Business Network Integration | Message Dashboard (/AIFX/WDA_MSG_MONITOR) | You can view the message summary in Application Interface Framework. |
| Initial Replication (Manual) using Fiori Apps |  |  |  |
| [Replicate with Global Filter (Optional)](#unique_11) [page ] 11 | Configuration Expert - Business Network Integration | Replicate by Replication Model (DRF_ADHOC_REPLICATION) | The system reads and sends product master data including sales prices. |
| [Replicate with Manual Selection (Optional)](#unique_12) [page ] 13 | Configuration Expert - Business Network Integration | Replicate by Object Selection (DRF_MANUAL_REPLICATION) | The system reads and sends product master data including sales prices. |
| [Analyze Replication Logs](#unique_13) [page ] 15 | Configuration Expert - Business Network Integration | Monitor Replication (DRF_FPM_OIF_MONITORING) | You can view log including success/ error messages. |
| Delta Replication by Scheduling Job |  |  |  |
| [Change Sales Price of Product](#unique_14) [page ] 16[Change Other Product Attributes (Optional)](#unique_15) [page ] 17 | Pricing Specialist (Retail)Master Data Specialist - Product Data | Maintain Sales Price Calculation (VKP1)Manage Product Master Data (F1602) | You have changed product master data. |
| [Schedule Job for Delta Replication](#unique_16) [page ] 18 | Administrator | Communication Arrangements (F1763) | You have schedule jobs for delta replication of product master data. |
| Delta Replication (Manual) using Fiori Apps |  |  |  |
| [Replicate Specific Data by Using Replication Model (Optional)](#unique_17) [page ] 19 | Configuration Expert - Business Network Integration | Replicate by Replication Model (DRF_ADHOC_REPLICATION) | The system reads and sends delta information in the form of messages for product master data including sales prices. |
| [Display Replication Status](#unique_18) [page ] 20 | Configuration Expert - Business Network Integration | Display Replication Status (MDG_BS_WD_RSI_DISPLAY) | You can view the status of replication. |
| [Monitor Message Summary in SAP Application Interface Framework](#unique_10) [page ] 21 | Configuration Expert - Business Network Integration | Message Dashboard (/AIFX/WDA_MSG_MONITOR) | You can view the message summary in Application Interface Framework. |

## Test Procedures

This chapter describes the test procedures for each process step that belongs to this scope item.

### Schedule Job for Initial Replication

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this procedure, you can change the communication arrangement to schedule and activate the job for initial replication of master data.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log onto the SAP Fiori Launchpad as an Administrator. |  |  |
| 2 | Access the SAP Fiori app | Open Communication Arrangements (F1763) app. | Communication Arrangements (F1763) selection screen is displayed. |  |
| 3 | Select the communication arrangement | Select the arrangement name for the scenario ID SAP_COM_0640 created during initial set up. | Communication Arrangements (F1763) screen is displayed. |  |
| 4 | Schedule a background job | Perform the following:In the Job Execution Details, specify the frequency for job execution by entering a relevant value in Run Every, for instance, if initial replication must be done after an hour, then set Run Every as 01 Hour(s).Note You can choose to set a different interval for job execution based on your convenience. After job activation, system takes an hour to run the defined job. Wait for stipulated time for the job to finish.Specify your Package Size.Select Save. |  |  |

### Monitor Message Summary in SAP Application Interface Framework

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this procedure, you can monitor the detailed information about the replication logs for a specific date.

|  |
| --- |
| Note To execute this process step, make sure you have waited for the stipulated time for execution of the job defined in the [Schedule Job for Initial Replication](#unique_9) [page ] 9 of this document. After the job is executed, logs are generated. |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log onto the SAP Fiori launchpad as a Configuration Expert - Business Network Integration. |  |  |
| 2 | Access the SAP Fiori app | Open Message Dashboard (/AIFX/WDA_MSG_MONITOR) app. | The Interface Monitor selection screen is displayed. |  |
| 3 | Select the dates | Perform the following:Select From (Date/Time), To (Date/Time)Select Search | The replication log for the selected dates is displayed. |  |
| 4 | Expand the result list and select the messages link | Perform the following:Expand the Namespace/Interface For example, /RFMPO to view ProductMerchandiseViewReplicationBulkRequest_Out - PMVRBR_OUT/1Select the messages link text under All Messages | Monitor and Error Handling screen is displayed. |  |
| 6 | Download XML to view message detailsOrSelect node to check its content | Follow one of the following ways to check the message details:In the Data Messages on the left split screen, select Expand All and select the data message of the specific date and time whose details you want to investigate. Resize to expand the split screen and find the Download and select it.In the Data Messages on the left split screen, select Expand All and select the data message of the specific date and time whose details you want to investigate. Select the node whose content needs to be viewed under the Data Structure on the right split screen, then scroll down to find the contents of the selected node under the Data Content on the right split screen. | The message Downloading the payload of message /RFMPO/PMVRBR_OUT/1/<Message ID> displays on right side of the screen. Simultaneously, XML file for the selected message ID is downloaded in your system to open and view the details.Node value/content is displayed. |  |

### Replicate with Global Filter (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The POS must be supplied with all required master data through an initial load, for example, when a new store is opened. In this procedure, you can manually replicate initial set of data with respect to the global filter criteria.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log onto the SAP Fiori launchpad as Configuration Expert - Business Network Integration. |  |  |
| 2 | Access the SAP Fiori App | Open Replicate by Replication Model (DRF_ADHOC_REPLICATION) app. | Replicate by Replication Model (DRF_ADHOC_REPLICATION) screen is displayed. |  |
| 3 | Select Replication Scope | Perform the following:Select the replication model, which was defined in the Communication Arrangement chapter of the Set Up Instructions.Note Please refer to the Define Filter Criteria in Set Up Instructions (3I2) if the earlier Defined filter criteria need to be changed or redefined before replication. For instance, to include a new store.Select target system in the Select Target System section to which data must be replicated.Select Product Merchandise as the business object under Select Business Objects to be Replicated section.Select Initialization under Replication Mode section. |  |  |
| 4 | Replicate | Select Replicate. | Replication begins for the target system. All articles which adhere to the filter criteria for example, sales org: for example 3310 and distribution channel 40, are replicated and sent to the target system.Note If reference and recipient site is maintained as described in the Maintain Reference and Recipient Sites (Optional) chapter of the Set-Up Instructions (3I2), then:Replication will take place for each reference store if the recipient store/stores given in the replication model filter criteria belongs to different reference stores.The sales price and purchase price information will correspond to that maintained for the reference store irrespective of the filter criteria.Note If Language Profile is defined and assigned to organizational units as per Define Language Profile for POS and Include Languages (Optional) in Set Up Instructions (3I2) and Assign POS Language Profile to Organizational Units (Optional) in Set Up Instructions (3I2) chapters, then:Description node and MeasureUnitCodeSpecificDescription have information in all the languages which are maintained in the language profile provided the article master data also have them maintained.Note If error category for any of the message number of language profile application area - RFM_DRF_PRD is maintained as Error or Warning in the Maintain Message Category for POS Outbound in Set Up Instructions (3I2) chapter, then:The respective logs would be displayed, if any of the article/receipt text description is missing.If an article contains a language-related error, no XML will be sent. |  |

### Replicate with Manual Selection (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this procedure, you can do manual replication by specifying individual objects only or by including the already defined filters along with specification of the individual objects.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log onto the SAP Fiori launchpad as Configuration Expert - Business Network Integration |  |  |
| 2 | Access the SAP Fiori app | Open Replicate by Object Selection (DRF_MANUAL_REPLICATION) app. |  |  |
| 3 | Enter selection criteria values | Perform the following:Select the Business Object Type as Product MerchandiseSelect the target system to which data must be replicated under Target System Selection. Specify the filter criteria manually. For example, Rec. store: 3340 Product: R_2003. |  |  |
| 4 | Apply object filter criteria (Optional) | Select the Apply Object Filter Criteria to filter data based on the corresponding global filters.Apply Object Filter Criteria includes the global filter criteria, for the replication model linked with the target system.Note <Business System> is displayed under Target System Selection for selection. Refer to the Communication Arrangement in Set-Up Instructions(3I2) to check the Business System specified for the communication system linked to your communication arrangement. | Note Set of the articles pertaining to both the global filter and the specified manual filter gets replicated to the selected target systems. |  |
| 5 | Replicate | Select Replicate. | Data is replicated to the target system. |  |
| 6 | Check the logs | Select Display Log. Select the log under Replication Logs and view the related log message under Replication Log Messages. | Replication Log for Manual Replication pop-up displays the selected log message details.Note To find the detailed data content of the replication messages, navigate to the Message Dashboard (/AIFX/WDA_MSG_MONITOR) app. refer to [Monitor Message Summary in SAP Application Interface Framework](#unique_10) [page ] 21 of this document for more details. |  |

### Analyze Replication Logs

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this procedure, you can view the replication logs message summary for the initial replication that was supposed to be triggered through scheduled job while setting up the communication arrangement. Optionally the replication logs message summary of prior optional step can also be analyzed.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log onto the SAP Fiori launchpad as Configuration Expert - Business Network Integration |  |  |
| 2 | Access the App | Open Monitor Replication (DRF_FPM_OIF_MONITORING) app. |  |  |
| 3 | Select Monitoring Scope | Perform the following:Select your Replication Model,which was defined in the Communication Arrangement in Set-Up Instructions (3I2)The system populates default values for the following fields:Replication Model: <Select your replication model>Business Object : Product Merchandise Date From/Time From Date To/Time ToLog Class : All LogsUser : *Replication Mode : All ModesYou can change the values as required.Select Continue. | The replication log for the selection criteria is displayed.Following outcomes are expected based on the status of replication:Replication logs with Green LED will be displayed if replication happened successfully for the selected replication model.Replication logs with Yellow LED will be displayed if replication happened successfully but there are some warnings associated with replication of few or more products for the selected replication model.Replication logs with Red LED will be displayed if replication fails for the selected replication model.Note To find the detailed data content of the replication messages, navigate to the Message Dashboard (/AIFX/WDA_MSG_MONITOR) app. Refer to [Monitor Message Summary in SAP Application Interface Framework](#unique_10) [page ] 21 of this document for more details. |  |

### Change Product Master Data

#### Change Sales Price of Product

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

You can perform this activity to change the data in the price calculations suggested by the system based on the various default settings (calculation schemas, planned markups, price points, and so on.), so that it can be replicated through the delta replication.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Pricing Specialist (Retail). |  |  |
| 2 | Access App | Open Maintain Sales Price Calculation (VKP1) app. |  |  |
| 3 | Enter values for Price Calculation fields | Make the following entries and choose Execute:Material: R_2004Sales Organization: for example 3310Distribution Channel: 40Plant: for example 1740Valid on: <Current Date>Purchase price determination seq: 01Sales price determination seq: 01List group: CList variant: 01 |  |  |
| 4 | Change values for price calculation | Change the final price value to any new value.Note If price changes are done at store level as described above, then for the changes to be replicated it is necessary to have the store defined in the filter. Please refer to the Define Filter Criteria in Set-Up Instructions (3I2) if the earlier defined filter criteria need to be changed or redefined before replication. | Final price is changed to new value. |  |
| 5 | Save Document | Choose all and select Save. | Changes made to existing pricing calculation is saved. |  |

#### Change Other Product Attributes (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this procedure, you can change the product master data so that it can be replicated through the delta replication.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log onto the SAP Fiori launchpad as a Master Data Specialist - Product Data |  |  |
| 2 | Access the SAP Fiori app | Open Manage Product Master Data (F1602) app. |  |  |
| 3 | Change product master data | The change pointers are generated for delta replication of changed master data in the following scenarios:If any of the following fields is changed for an article,General Information > DescriptionsGeneral Information > Unit of Measure > Receipt TextsDistribution Chains > Point of Sale data > No Repeat KeyDistribution Chains > Point of Sale data > Price RequiredDistribution Chains > Point of Sale data > Discount AllowedDistribution Chains > Listing Parameters > Sales Store > Sales Period End DateGeneral Information > Base Unit of Measure > GTINGeneral Information > Unit of Measure > Conversion Factor > Units/Quantity -Alternative Unit of MeasureGeneral Information > Unit of Measure > Conversion Factor > Units/Quantity -Base Unit of MeasureGeneral Information > Base Unit of Measure > Base Unit of Measure > GTIN CategoryChange Sales Period End Date field in article with lead time consideration, that is the date is as much in the future as the set lead time for the D-Chain/Site.Note XML with action code – 05 (Deletion), is generated to imply article record deletion as article sale validity approaches, considering the lead time.Refer to Products for Retail (3I1), to know the process of changing the product master. |  |  |

### Schedule Job for Delta Replication

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this procedure, you can change the communication arrangement after the stores are initialized. This enables you to replicate delta changes in the master data.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log onto the SAP Fiori Launchpad as an Administrator |  |  |
| 2 | Access the SAP Fiori app | Open Communication Arrangements (F1763) app. |  |  |
| 3 | Select the communication arrangement | Select the communication arrangement created during initial set up. |  |  |
| 4 | Change the communication arrangement | Perform the following:Select EditUnder Additional Properties, enter C in Replication Mode |  |  |
| 5 | Schedule a background job | Perform the following:In the Job Execution Details, specify the frequency for job execution by entering a relevant value in Run Every, for instance, if delta changes, must be replicated once every day then set Run Every as 1 Day(s).Note You can choose to set a different interval for job execution based on your convenience. After job activation, system takes an hour to run the defined job. Wait for stipulated time for the job to finish.Specify your Start Time and Package SizeSelect Save. |  |  |

### Replicate Specific Data by Using Replication Model (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this procedure, you can manually trigger replication of the specific data which is changed or modified.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log onto the SAP Fiori launchpad as Configuration Expert - Business Network Integration |  |  |
| 2 | Access the SAP Fiori app | Open Replicate by Replication Model (DRF_ADHOC_REPLICATION) app. |  |  |
| 3 | Select replication scope and other details | Perform the following:Select your replication model, which was defined in the Communication Arrangement in Set-Up Instructions(3I2) in Replication Model.Select your target system in Select Target System to which data must be replicated.Note <Business System> is displayed under Select Target System section for selection. Refer to the Communication Arrangement in Set-Up Instructions(3I2) of the Set-Up Instructions to check the Business System specified for the communication system linked to your communication arrangement.Select Product Merchandise as the Business Object.Select Changes in Replication Mode section. |  |  |
| 4 | Replicate the data | Select Replicate. | The specific data which is changed or modified is replicated. |  |

### Display Replication Status

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this procedure, you can check the replication status whether it is in error, warning, or success state.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log onto the SAP Fiori launchpad as Configuration Expert - Business Network Integration |  |  |
| 2 | Access the SAP Fiori app | Open Display Replication Status (MDG_BS_WD_RSI_DISPLAY) app. |  |  |
| 3 | Enter selection details and search | Select Business Object Type as Product MerchandiseSelect Receiving Store and Product.Select Search. | The replication status information is displayed along with detailed log. |  |

### Monitor Message Summary in SAP Application Interface Framework

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this procedure, you can monitor the detailed information about the replication logs for a specific date.

|  |
| --- |
| Note To execute this process step, make sure you have waited for the stipulated time for execution of the job defined in the [Schedule Job for Initial Replication](#unique_9) [page ] 9 of this document. After the job is executed, logs are generated. |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log onto the SAP Fiori launchpad as a Configuration Expert - Business Network Integration. |  |  |
| 2 | Access the SAP Fiori app | Open Message Dashboard (/AIFX/WDA_MSG_MONITOR) app. | The Interface Monitor selection screen is displayed. |  |
| 3 | Select the dates | Perform the following:Select From (Date/Time), To (Date/Time)Select Search | The replication log for the selected dates is displayed. |  |
| 4 | Expand the result list and select the messages link | Perform the following:Expand the Namespace/Interface For example, /RFMPO to view ProductMerchandiseViewReplicationBulkRequest_Out - PMVRBR_OUT/1Select the messages link text under All Messages | Monitor and Error Handling screen is displayed. |  |
| 6 | Download XML to view message detailsOrSelect node to check its content | Follow one of the following ways to check the message details:In the Data Messages on the left split screen, select Expand All and select the data message of the specific date and time whose details you want to investigate. Resize to expand the split screen and find the Download and select it.In the Data Messages on the left split screen, select Expand All and select the data message of the specific date and time whose details you want to investigate. Select the node whose content needs to be viewed under the Data Structure on the right split screen, then scroll down to find the contents of the selected node under the Data Content on the right split screen. | The message Downloading the payload of message /RFMPO/PMVRBR_OUT/1/<Message ID> displays on right side of the screen. Simultaneously, XML file for the selected message ID is downloaded in your system to open and view the details.Node value/content is displayed. |  |

## Appendix

### Process Integration

The process to be tested in this test script is part of a chain of integrated processes.

#### Preceding Processes

The following processes and conditions can proceed this process.

| Process | Business Condition |
| --- | --- |
| Not applicable |  |

#### Succeeding Processes

After completing the activities in this test script, you can continue testing the following business processes:

| Process | Business Condition |
| --- | --- |
| 3HV - Store Connectivity – Inbound | This scope item covers posting of article purchase and return information along with financial transactions from POS to the SAP S/4HANA Cloud Public Edition system. |

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
- related-to :: [[15-retail-operations/store-connectivity-inbound-3hv-ae-test-script-sap-s-4hana-cloud-public]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/3I2_S4CLD2608_BPD_EN_AE.docx` — full document · extracted with `mammoth` · 38,849 chars in the whole document
