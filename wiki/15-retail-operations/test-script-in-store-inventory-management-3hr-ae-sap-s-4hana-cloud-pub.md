---
id: 15-retail-operations/test-script-in-store-inventory-management-3hr-ae-sap-s-4hana-cloud-pub
title: "Test Script: In-Store Inventory Management (3HR_AE) - SAP S/4HANA Cloud Public Edition (3HR_S4CLD2608_BPD_EN_AE)"
description: "SAP S/4HANA Cloud Public Edition test script (3HR_AE, dated 19-06-26) for in-store inventory: physical inventory, ad hoc count, mass stock adjustment, transfers, clean-up."
cluster: 15-retail-operations
tags: [kb/retail-operations, topic/in-store-inventory]
aliases: [3HR_S4CLD2608_BPD_EN_AE]
keywords: [In-Store Inventory Management, physical inventory, count stock ad hoc, adjust mass stock, product transfer, in-store data clean-up, cycle counting, business roles, test master data, stock overview]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/3HR_S4CLD2608_BPD_EN_AE.docx]
confidence: high
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-937
topic: 15-retail-operations/in-store-inventory
language: EN
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Test Script: In-Store Inventory Management (3HR_AE) - SAP S/4HANA Cloud Public Edition (3HR_S4CLD2608_BPD_EN_AE)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/3HR_S4CLD2608_BPD_EN_AE.docx`, extracted with `mammoth`. Grouped under **In-Store Inventory Management** in Retail Operations. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

| <!-- image omitted: unnamed --> | Test ScriptSAP S/4HANA Cloud Public Edition - 19-06-26 |
| --- | --- |
|  | In-Store Inventory Management (3HR_AE) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Table of Contents

[1 Purpose 3](#_Toc232852529)

[2 Prerequisites 4](#_Toc232852530)

[2.1 System Access 4](#_Toc232852531)

[2.2 Roles 4](#_Toc232852532)

[2.3 Master Data, Organizational Data, and Other Data 5](#_Toc232852533)

[2.4 Additional Manual Configuration 5](#_Toc232852534)

[2.5 Preliminary Steps 6](#_Toc232852535)

[2.5.1 Configure Define Basic Settings for Count Stock Ad hoc 6](#_Toc232852536)

[2.5.2 Assign Store Associate (User) to a Store 6](#_Toc232852537)

[2.5.3 Display Physical Inventory Document 7](#_Toc232852538)

[2.5.4 Delete Active Physical Inventory Document (Optional) 9](#_Toc232852539)

[2.5.5 Overview of Stock– Single Material 9](#_Toc232852540)

[2.5.6 Set Initial Stock for Article (Optional – Only if Stock not Available) 10](#_Toc232852541)

[2.5.7 Define Cycle Counting Indicator 12](#_Toc232852542)

[2.5.8 Define Cycle Counting Classification 13](#_Toc232852543)

[2.5.9 Set up the Printer 14](#_Toc232852544)

[3 Overview Table 15](#_Toc232852545)

[4 Test Procedures 17](#_Toc232852546)

[4.1 Perform Physical Inventory 17](#_Toc232852547)

[4.1.1 Create Physical Inventory Document 17](#_Toc232852548)

[4.1.2 Display Physical Inventory Document 18](#_Toc232852549)

[4.1.3 Perform Physical Inventory Count 19](#_Toc232852550)

[4.1.4 Approve or Reschedule Stock Counts 21](#_Toc232852551)

[4.1.5 Post Inventory Count Differences 22](#_Toc232852552)

[4.1.6 Overview of Stock– Single Material 22](#_Toc232852553)

[4.2 Count Stock Ad hoc 23](#_Toc232852554)

[4.2.1 Overview of Stock– Single Material 25](#_Toc232852555)

[4.3 Adjust Mass Stock - Options 26](#_Toc232852556)

[4.3.1 Adjust Mass Stock (Option 1) 26](#_Toc232852557)

[4.3.2 Adjust Mass Stock with Add Claim (Option 2) 28](#_Toc232852558)

[4.4 Transfer of Product 30](#_Toc232852559)

[4.5 Schedule Clean Up of Operational In-Store Data (Optional) 31](#_Toc232852560)

[4.5.1 Schedule Clean Up of Operational In-Store Data - Count Stock Ad hoc 31](#_Toc232852561)

[4.5.2 Schedule Clean Up of Operational In-Store Data – Adjust Mass Stock 33](#_Toc232852562)

[4.5.3 Schedule Clean Up of Operational In-Store Data – Transfer Products 34](#_Toc232852563)

## Purpose

Overview

In-Store Inventory Management aims to ensure an accurate and rebalanced stock, providing, for example, a sound basis for replenishment.

It enables store associates to:

- Transfer articles from one store to another or to a distribution center using handling units that enable efficient logistics processes within the store.
- Create a physical inventory document and make it visible to the count stock application
- Perform a physical inventory count of all articles in the store, or a cycle count of selected articles
- Use the Manage Stock Counting app as a store manager to review counts submitted by store associates
- Perform an ad-hoc physical inventory count for selected articles at a given point of time by the retail associate
- Adjust the stock quantity for different reasons such as shrinkage, damage, or spoilage, and subtract the article quantity from the current on-hand stock

This document provides a detailed procedure for testing this scope item after solution activation, reflecting the predefined scope of the solution. Each process step, report, or item is covered in its own section, providing the system interactions (test steps) in a table view. Steps that are not in scope of the process but are needed for testing are marked accordingly. Project-specific steps must be added.

|  |
| --- |
| Note Values in this test script (decimal notation, date formats, and so on) are presented in U.S. standard notation. If your test system is set up to use a different notation, enter values as appropriate. |

|  |
| --- |
| Note In the retail industry, specific terms differ from the standard terms used in other lines of business. Therefore, SAP solutions which provide business processes across multiple lines of businesses may use terms for the corresponding business objects, transactions, and user interfaces that deviate from the retail terminology. For integration and reuse reasons, the SAP S/4HANA Cloud Public Edition, retail, fashion, and vertical business business may thus include different terms that refer to the same concept. SAP intends to harmonize the terminology in the future.The following terms are used synonymously in this document:Table 1:Standard Terms in Lines of BusinessSAP S/4HANA Cloud Public Edition, retail, fashion, and vertical business businessMaterial, productArticleMaterial group, product groupMerchandise categoryPlant, locationSite (as superordinate term) - store and distribution center (DC) |

## Prerequisites

This section summarizes all the prerequisites for conducting the test in terms of systems, users, master data, organizational data, other test data and business conditions.

### System Access

|  |  |
| --- | --- |
|  | Details |
| System | Accessible through SAP Fiori launchpad. Your system administrator provides you with the URL to access the various apps assigned to your role. |

### Roles

Create business roles using the following business role templates delivered by SAP and assign them to your individual test users.

Alternatively, if available, you can use the following spaces delivered by SAP. You create a space with pages containing predefined essential apps and assign it to the business role. You then assign this business role to your individual users.

For more information, refer to How to Create a Business Role from a Template in the [product assistance](https://help.sap.com/docs/SAP_S4HANA_CLOUD/53e36b5493804bcdb3f6f14de8b487dd/ec310a8b669a45ca898dc4dd91d97de2.html) for SAP S/4HANA Cloud Public Edition.

| Name (Role Template) | ID (Role Template) | Name (Launchpad Space) | ID (Launchpad Space) |
| --- | --- | --- | --- |
| Allocator (Retail) | SAP_BR_ALLOCATOR_RETAIL | Allocator (Retail) | SAP_BR_ALLOCATOR_RETAIL |
| Retail Store Associate | SAP_BR_RFM_STORE_ASSOCIATE | Retail Store Associate | SAP_BR_RFM_STORE_ASSOCIATE |
| Retail Store Manager | SAP_BR_RFM_STORE_MANAGER | Retail Store Manager | SAP_BR_RFM_STORE_MANAGER |
| Warehouse Clerk (Retail) | SAP_BR_WAREHOUSE_CLERK_RFM | Retail Inventory Processing | SAP_BR_WAREHOUSE_CLERK_RFM |
| Inventory Manager (Retail) | SAP_BR_INVENTORY_MGR_RFM | Retail Inventory Management | SAP_BR_INVENTORY_MGR_RFM |
| Administrator (Retail) | SAP_BR_ADMINISTRATOR_RFM | Administrator (Retail) | SAP_BR_ADMINISTRATOR_RFM |

### Master Data, Organizational Data, and Other Data

The organizational structure and master data of your company have been created in your system during activation. The organizational structure reflects the structure of your company. The master data represents Articles, customers, and suppliers, for example, depending on the operational focus of your company.

Use your own master data or the following sample data to go through the test procedure.

|  |
| --- |
| Note In the following table, sample values for master data are provided for the country/region US. You can either use the country-dependent sample master data or create and use your own master data while executing the test procedure. |

| Data | Sample Value | Details | Comments |
| --- | --- | --- | --- |
| Store (Site) | 3340 | Store 3340 AE |  |
| Store (Site) | 3341 | Store 3341 AE |  |
| Article | R_1006 | My Best Frozen Strawberries |  |
| Article | R_1038 | My Best bread roll - grain |  |
| Article | R_1003005 | Chocolate, Cherry Yoghurt, Diet |  |
| Article | R_1037 | White bread large, organic |  |
| Cost Center | 3340 | Template Store |  |
| Material Group | R1171001 | Bread |  |
| Storage Location | 994A | St.Loc.Neg.Stock |  |

### Additional Manual Configuration

Before you can test this scope item, you must have completed the additional configuration steps that are described in the Set-Up Instructions for this scope item. These configuration steps are specific for your implementation and include mandatory settings that are not delivered by SAP and must be created by you. For more information, follow the link to the document:

[Link to Set-Up Instructions](https://help.sap.com/docs/SAP_S4HANA_BEST_PRACTICES/57a4f4e6cf2d3186a4268edae0b77020)

### Preliminary Steps

#### Configure Define Basic Settings for Count Stock Ad hoc

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the project experience in SAP Central Business Configuration as Configuration Expert - Business Process Configuration |  |  |
| 2 | Open Active Flexible Workflow | Go to the Business Processes Configuration app. To locate the activity in the tree view, search for the following activity: Define Basic Settings for Count Stock Ad hoc.Choose Open Documentation for the found line item to see more details about this configuration activity.Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. | The Define Basic Settings for Count Stock Ad hoc screen is displayed. |  |
| 3 | Configure Define Basic Settings for Count Stock Ad hoc | Create the following settings:Check ON Enable Automatic Posting |  |  |
| 4 | Save the configuration | Select Save | The configuration is saved successfully. |  |

#### Assign Store Associate (User) to a Store

Use

To filter the data provided in the SAP Fiori in-store merchandising apps, the store associate needs to be assigned to a certain store (site).

|  |
| --- |
| Note The store assignment can be changed at any point in time in case a store associate is helping in another store or if this is required for testing purposes. |

Procedure

| Step # | Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori launchpad as a Retail Store Associate. |  |  |
| 2 | Open my store assignment app | Open My Store Assignment (F4334) app.Note If you are already assigned to Store (for example 3340), you can skip the entire Procedure. |  |  |
| 3 | Search store | Search for the stores ID/ Name/ Postal Code and City combination:Store ID : for example 3340 orName: for example Store Atlanta orPostal Code : for example 30326 orCity : for example City AtlantaSelect the magnifying glass or select Go |  |  |
| 4 | Select store | Select the store you want the user to be assigned by clicking radio button of the store on the left. | Store is selected. |  |
| 5. | Assign store | Save the new assignment by selecting Assign Me on the top right above the list of stores. | The message pops up “You were assigned to store <Store created by you>.” is momentarily displayed. The assigned store above the list is updated accordingly. |  |
| 6. | Exit screen | Select Back | The SAP Fiori Launchpad is displayed containing all relevant apps for the Retail Store Associates |  |

Result

When assigned to a store, store associate has access to relevant information of the assigned store, increasing the efficiency of the day-to-day work.

#### Display Physical Inventory Document

Use

This preliminary step is to check if there is an existing PI document for the combination of an article, site, and storage location.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori launchpad as a Inventory Manager (Retail). |  |  |
| 2 | Access the app | Open Physical Inventory Analysis (W0058) app. |  |  |
| 3 | Adopt filters | Choose Adapt Filters and select the below options under AdditionalMaterial :Plant :Storage Location :Choose OK |  |  |
| 4. | Enter details | Enter the below details in Standard SectionMaterial :Plant :Storage Location :Is Difference Posted: <Delete if any default value is selected in this field>Choose GO |  |  |
| 5. | Check the Physical Inventory Document | In Navigation Panel, under Available Fields:Add Physical Inventory Document either for row or for column by selecting below options:Select this option for row axis Add field Physical Inventory Document to row axis orSelect this option for column axis Add field Physical Inventory Document to column axis.Physical Inventory DocumentMaterialAll the details of the physical inventory displays under Data Analysis tabSelect Physical Inventory Document field and choose Drill Down > Add Drill DownSelect "Is Deleted" option under Available Fields.Choose OK | PI document number for the combination of an article, site, and storage location is displayed. |  |
| 6 | Note Active PI | Search for the PI Document number havingIs Deleted : #(No)Note the PI document number.In case of no active PI document, proceed to step Overview of Stock– Single Material | Active PI document number noted |  |

Result

Active PI document checked for the combination of an article, site, and storage location.

#### Delete Active Physical Inventory Document (Optional)

Use

This process step is in continuation to the previous step [Display Physical Inventory Document](#unique_9) [page ] 7 to delete the active Physical Inventory (PI) document. This step is only applicable when there is an active PI document for the combination of an article, site, and storage location.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori launchpad as Inventory Manager (Retail) |  |  |
| 2 | Access App | Open Manage Physical Inventory Documents (F0379A) app. |  |  |
| 3 | Manage Physical Inventory | Enter the Physical Inventory Document: XXXX ([Display Physical Inventory Document](#unique_9) [page ] 7) and select Go. | Physical inventory document is displayed. |  |
| 4 | Display the Physical Inventory Document | Select the arrow on right hand side to display the physical inventory document details. | Physical inventory document is displayed. |  |
| 5 | Delete Physical Inventory Document | Select Delete.Popup window is displayed for the confirmation as below:Do you want to delete physical inventory document XXXXXXXXX XXXX?.Note: The document is deleted and disappears from your list.In the popup screen, select Delete. | A message is displayed as physical inventory document XXXXXXXXX XXXX Deleted |  |

Result

Active PI document for the combination of an article, site, and storage location deleted.

#### Overview of Stock– Single Material

Use

To execute this scope item, the article has stock available in unrestricted use stock. The following preliminary steps must be executed to ensure the stock availability for all the process steps in this scope item.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log onto the SAP Fiori launchpad as a Inventory Manager (Retail). |  |  |
| 2 | Access the app | Open Stock - Single Material (F1076) app. |  |  |
| 3 | Enter Material | Make the following entries:Material: R_1037Select Enter | The Stock – Single Material screen is displayed with stock of material R_1037 in all the sites and storage locations. |  |
| 4 | Enter Material | Make the following entries:Material: R_1038Select Enter | The Stock – Single Materials creen is displayed with stock of material R_1038 in all the sites and storage locations. |  |
| 5 | Enter Material | Make the following entries:Material: R_1003005Select Enter | The Stock – Single Material screen is displayed with stock of material R_1003005 in all the sites and storage locations. |  |

Result

Unrestricted stock is checked for the material.

#### Set Initial Stock for Article (Optional – Only if Stock not Available)

Use

To execute this scope item, the article must have stock available. The following preliminary steps must be executed only if there is no unrestricted use stock available for any of the 3 materials used in the test script. This step is to ensure the stock availability for all the process steps in this scope item.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori launchpad as a Warehouse Clerk (Retail). |  |  |
| 2 | Access the app | Open Post Goods Movement (MIGO) app.The Transaction/Event and reference document will be updated automatically based on your last activity in MIGO transaction. |  |  |
| 3 | Input movement type | Make the following entry below and select ENTER:Trans./Event : Goods ReceiptReference Document: OtherInit.entry of StBalance : 561 | Entry accepted. |  |
| 4 | Enter article | In the detail data section : Material tab, Make the following entry:Material : R_2010And select ENTERNote Enter the articles without unrestricted use stock. | Article accepted. |  |
| 5 | Enter quantity data | In the detail data section: Quantity tab, Make the following entry:Qty in Unit of Entry : 10/ CRTExt. Amount LC: 1000Select ENTER | Qty and unit accepted. |  |
| 6 | Input on the goods receipt other screen: where tab | In the detail data section: Where tab, Make the following entries:Goods Movement Type: 561 (Receipt per initial entry of stock balances into unrestricted use)Plant: for example 3340Storage Location: 994ASelect ENTER | Values are accepted and shows check and post below screen. |  |
| 7 | Check your entries | Select CheckIf there is no errors in the data entered, a confirmation message Document Is O.K. is displayed. | Material document is checked. |  |
| 8 | Save your entries | Select PostNote Repeat the steps in case there are more than one article without unrestricted use stock (as per the quantities mentioned in the respective test procedure). | Material document is created. |  |

Result

Stock is created for the material.

#### Define Cycle Counting Indicator

Use

A cycle-counting indicator is a configuration setting used to control how and how often items are physically counted in a store.

The following procedure provides instructions for creating cycle counting indicator.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the project experience in SAP Central Business Configuration. |  |  |
| 2 | Open Active Flexible Workflow | Go to the Business Processes Configuration app. To locate the activity in the tree view, search for the following activity: Cycle Counting.Choose Open Documentation for the found line item to see more details about this configuration activity.Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. | The Cycle Counting: Change screen is displayed. |  |
| 3 | Set Cycle Counting Indicator | Create the following settings:Choose New Entries to create 3 new entries with the following data:First Entry:Plnt: 3340CC Phys. Inv. Ind.: <A>No. of phys. invtories: <12>Float time: <5>Validity: ValidSecond Entry:Plnt: 3340CC Phys. Inv. Ind.: <B>No. of phys. invtories: <6>Float time: <3>Validity: ValidThird Entry:Plnt: 3340CC Phys. Inv. Ind.: <C>No. of phys. invtories: <5>Float time: <2>Validity: Valid |  |  |
| 4 | Save Your Entries | Choose Save. | The cycle counting indicator is saved. |  |

#### Define Cycle Counting Classification

Use

It is used to categorize retail articles by their sales value or turnover. It determines how often each item should be counted (monthly for high-value items and annually for low-value stock) to ensure inventory accuracy without closing the entire store by using the Cycle Counting - Classification (F4486) app.

The following procedure provides instructions for defining cycle counting indicator.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Inventory Manager (Retail) |  |  |
| 2 | Access the App | Open the Cycle Counting - Classification (F4486) app. | Cycle Counting - Classification screen is displayed. |  |
| 3 | Enter Parameters | Enter the following data:Analytics Start Date: <First Day in This Year>Analytics End Date: <Today>Inventory Consumption Group: 000(STANDARD CONSUMPTION GROUP)Plant: 3340Product: R_1006Choose Go. |  |  |
| 4 | Maintain Physical Inventory Indicator | Select products under the Unclassified tab and choose Classify.In the Classify dialog box, enter below details:Cycle Counting Indicator : Replace Field Values and ACycle Counting Indicator Fixed: YesChoose Save. | A classify dialogue box displays.Classification is assigned to product XXX. |  |

#### Set up the Printer

Use

To execute this scope item, the printer set up must be completed. The following preliminary steps must be executed to ensure the printer setup for transfer products process.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori launchpad as a Retail Store Associate. |  |  |
| 2 | Access the app | Open Transfer Products (F2449) app. |  |  |
| 3 | Setup printer | Printer needs to be set by navigating through User profile - Application Setting and select the required printer from the dropdown list and select Close. | Printer needs to be displayed in the dropdown list to be selected. |  |

Result

Printer is assigned.

## Overview Table

This scope item consists of several process steps provided in the table below.

|  |
| --- |
| Note If your system administrator has enabled spaces and pages on the SAP Fiori launchpad, the homepage will only contain the essential apps for performing the typical tasks of a business role.You can find all other (searchable) apps not included on the homepage using the search bar ([2434549](https://me.sap.com/notes/2434549)).If you want to personalize the homepage and include the hidden apps, navigate to your user profile and choose App Finder. |

|  |  |  |  |
| --- | --- | --- | --- |
| <Choose the appropriate entity: Process Step, Report, or Item> | Business Role | App/Transaction | Expected Results |
| [Create Physical Inventory Document](#unique_17) [page ] 17 | Inventory Manager (Retail) | Create Documents - Physical Inventory (WV31) | Physical Inventory Document is created for Store. |
| [Display Physical Inventory Document](#unique_18) [page ] 18 | Inventory Manager (Retail) | Manage Physical Inventory Documents (F0379A) | Physical Inventory Document is displayed |
| [Perform Physical Inventory Count](#unique_19) [page ] 19 | Retail Store Associate | Count Stock (F1512) | A before planned physical inventory is executed by the store associate by entering the quantity for the to be counted articles. |
| [Approve or Reschedule Stock Counts](#unique_20) [page ] 21 | Retail Store Manager | Manage Stock Counting (F1512) | The store manager is monitoring the counts and can approve them or request a recount in case of high deviations. |
| [Post Inventory Count Differences](#unique_21) [page ] 22 | Inventory Manager (Retail) | Manage Physical Inventory Documents (F0379A) | The inventory manager can review and post the count difference |
| [Overview of Stock– Single Material](#unique_22) [page ] 22 | Inventory Manager (Retail) | Stock - Single Material (F1076) | Updated count is displayed in stock overview |
| [Count Stock Ad hoc](#unique_23) [page ] 23 | Retail Store Associate |  |  |
| [Adjust Mass Stock (Option 1)](#unique_24) [page ] 26 | Retail Store Associate | Adjust Mass Stock (F4959) | The store associate adjusts the stock as example an item was discovered in the shelf unaccounted for. |
| [Adjust Mass Stock with Add Claim (Option 2)](#unique_25) [page ] 28 | Retail Store Associate | Adjust Mass Stock (F4959) | The store associate is adjusting stack and creating a claim for another cost centre. |
| [Transfer of Product](#unique_26) [page ] 30 | Retail Store Associate | Transfer Products (F2449) | A stock transfer order is created, containing the scanned articles. |
| [Schedule Clean Up of Operational In-Store Data (Optional)](#unique_27) [page ] 31 | Administrator (Retail) | Count Stock Ad hoc (F5563), Adjust Mass Stock (F4959), Transfer Products (F2449) apps. | Operational In store app data will be deleted |

## Test Procedures

This chapter describes the test procedures for each process step that belongs to this scope item.

### Perform Physical Inventory

#### Create Physical Inventory Document

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

A Physical Inventory (PI) document is prepared before the actual counting of the stock for the Article. It contains a list of articles which need to be counted in a store.

This process step shows you how you can create a physical inventory document for a store.

|  |
| --- |
| Note You can only have one active PI document for the combination of an article, site, and storage location. Execute preliminary step [Display Physical Inventory Document](#unique_9) [page ] 7 to check if there is an existing PI document for the combination of an article, site, and storage location. If yes, then follow preliminary step [Delete Active Physical Inventory Document (Optional)](#unique_10) [page ] 9 to delete the existing PI document before executing this step. |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori launchpad as Inventory Manager (Retail). |  |  |
| 2 | Access app | Open Create Documents - Physical Inventory (WV31) app. | Create Physical Inventory Docs for Unrestricted -Use stock (Retail) app is accessed. |  |
| 3 | Maintain basic information | Maintain the below entries in the selection screen:Under Database Selection section enter:Plant: for example 3340Storage location: 994AMaterial Group: R1171001Under Data in Phys, Inv, Docmt Header section enter:Planned count date : Today’s DateSelect ON the flag for issue log in control data sectionIssue log: X | The inputs provided are accepted. |  |
| 4 | Create physical inventory document (PID) | Select Execute to create the physical inventory document. | Physical Inventory documents generated |  |
| 5 | Pick the physical inventory document | On the table under Message text column, we can see Physical Inventory Document xxxxxxxxxx is created. Keep note of the physical inventory document number.Note Multiple physical inventory documents can be created depending upon the number of articles available for physical inventory. |  |  |

Result

A physical inventory document has been created and is shown in the count products app.

#### Display Physical Inventory Document

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

|  |
| --- |
| Note Because the system can only have one open physical inventory document for the same material, it is necessary to check open physical inventory document before any testing procedures. |

Purpose

This process step shows, how you can display the physical inventory document created in the previous step.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori launchpad as a Inventory Manager (Retail). |  |  |
| 2 | Access the app | Open Manage Physical Inventory Documents (F0379A) app. |  |  |
| 3 | Enter Data | Make the following entries and choose Go:Plant:Physical Inventory Document: (Enter PI Doc number noted in the previous procedure)Choose Adapt Filters and select the below option:Adjustment Status: Select items Not Posted and Partially Posted. |  |  |
| 4 | Choose an Item | Choose the item displayed in the Physical Inventory Documents List and verify the physical inventory documents detailsNote In case of multiple physical inventory documents, repeat 3 & 4 steps for each physical inventory document.Note down the physical inventory document number and the articles associated with it which needs to be counted in further steps. |  |  |

#### Perform Physical Inventory Count

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how in this application, store associates can perform a physical inventory count of all products in the store, or a cycle count of selected products. The count can be performed region (or zone wise) of the store. This process step can be used to:

- Perform annual inventory count of all products in the store
- Perform periodic inventory counts of selected products in the store
- Respond to recount requests received from head office

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori launchpad as a Retail Store Associate. |  |  |
| 2 | Access app | Open Count Stock (F1512) app. | The list of open physical inventory documents for the store are displayed. |  |
| 3 | Start counting | Select a physical inventory document (created in step [Create Physical Inventory Document](#unique_17) [page ] 17) XXXXXXXXX from the list and select Start Count.Note In case of multiple physical inventory documents, select the physical inventory document created for material R_1038 by following the preliminary step [Display Physical Inventory Document](#unique_9) [page ] 7. | It pops up the Enter Zone screen. |  |
| 4 | Enter zone | Select Scan and either scan the barcode of the zone or enter it manually if scanner is not available.Bar code: XXXXXXX (Material - R_1038) | Scans or accepts the EAN number of the material. |  |
| 5 | Add product | Select More (…) and Add Product to Count In the Search enter the article (picked from physical inventory document in step [Display Physical Inventory Document](#unique_18) [page ] 18).Select the Article to add it to count list. | The product is added to the count list. |  |
| 6 | Enter quantity | Enter the count of the product 10.Select +, we can increase the count and select – we can decrease the count. | Count of the product gets updated. |  |
| 7 | Submit count | Select More (…) and then on submit and OK in the submit count pop up. | Count submitted. A confirmation message is displayed.Zone count updated. displayed in the screen near to the physical inventory document number. |  |

#### Approve or Reschedule Stock Counts

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how as a store manager, you can approve or request for recount, of the count submitted by the store associate. Once the count is approved, the stocks are updated with the count.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori launchpad as a Retail Store Manager. |  |  |
| 2 | Access app | Open Manage Stock Counting (F1512) app. | A list of physical inventory documents is displayed. |  |
| 3 | Select physical inventory document | Select the Physical Inventory Document XXXXXXXXXX submitted by store associate in step [Perform Physical Inventory Count](#unique_19) [page ] 19 | Stock counting results are displayed in a product-centric/zone-centric or associate-centric view |  |
| 4 | Request recount | Flag Recount, as the counting difference is too high and select Submit.Select Complete This Inventory Count and select OK to submit selection popup. | A confirmation message is shown Count Submitted.The physical inventory document in the list of documents is labelled as local recount.And the same physical inventory document gets updated into Completed tab, as the Store manager activity is done. |  |
| 5 | Select physical inventory document after recount | Once the store associate recounts the physical inventory document with Local Recount status (as in step [Perform Physical Inventory Count](#unique_19) [page ] 19)Select the recounted physical inventory document | Stock counting results are displayed in a product-centric/zone-centric or associate-centric view |  |
| 6 | Approve count | Flag Count OK and Submit the physical inventory documentCheck Complete this Inventory Count and select OK for submit selection popup. | A confirmation message Count Submitted is displayed.And the physical inventory document gets updated into Completed tab, as the Store manager activity is done. |  |

#### Post Inventory Count Differences

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to post the results of the physical inventory. Once the count is reviewed and approved, the store manager can post the inventory count differences.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori launchpad as an Inventory Manager (Retail) |  |  |
| 2 | Access the app | Open Manage Physical Inventory Documents (F0379A) app. | Manage Physical Inventory Documents: Initial screen is displayed. |  |
| 3 | Enter inventory document data | Make the following entries:Select the arrow on right hand side to view the physical inventory document details.Physical Inventory Document: XXXXXXXXXX (Enter the physical inventory document completed in step [Approve or Reschedule Stock Counts](#unique_20) [page ] 21). | Physical Inventory document is fetched |  |
| 4 | Post Differences | Select the Material and choose Post.Enter the Posting Date: for example < Today's Date>.Choose Post. | Physical inventory is posted successfully. |  |

#### Overview of Stock– Single Material

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how you can display the stock overview of a material for a particular plant.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log onto the SAP Fiori launchpad as a Inventory Manager (Retail). |  |  |
| 2 | Access the app | Open Stock - Single Material (F1076) app. | In tile group Warehouse Stock Monitoring,The Stock - Single Material (F1076) screen is displayed. |  |
| 3 | Enter Material | Make the following entries:Material: R_1038Select Enter | The Stock – Single Material screen shows the stock of material R_1038 in all the sites and storage locations |  |

### Count Stock Ad hoc

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

Store associates need to keep a track of the stock count for the products on need basis for each storage location available in the store. This process helps to increase the efficiency of the store replenishment process.

You can only have one active PI document for the combination of an article, site, and storage location. Execute preliminary step [Display Physical Inventory Document](#unique_9) [page ] 7 to check if there is an existing PI document for the combination of an article, site, and storage location. If yes, then follow preliminary step [Delete Active Physical Inventory Document (Optional)](#unique_10) [page ] 9 to delete the existing PI document before executing this step.

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori launchpad as a Retail Store Associate. |  |  |
| 2 | Access app | Open Count Stock Ad hoc - TODAY (F5563) app. | The Count Stock Ad hoc - TODAY (F5563) app is displayed. |  |
| 3 | Create count stock document | Select Create on the upper right corner. | A new stock document is created for the store. The location of the store is displayed in the dropdown list and prefilled with the values selected for the last created stock document.The list of products is empty. |  |
| 4 | Maintain basic information | Change Location: 994A |  |  |
| 5 | Add product by search | Select on 'Search Product' and select the required product R_1006 by searching in the search tab available. Select Add. | Once the product is added "Success" pop up message is displayed and the product is added to in process Tab. |  |
| 6 | Add product by GTIN | Select 'Scan Bar code', enter the EAN/GTIN <xxxxxxxxxxx> of another product in the Bar code field and select OK.Note Repeat step 5 to get the GTIN number for a product (displayed between product description and UOM). | The product is added to the list of products. In case the product was already contained in the list, the number increase by one. |  |
| 7 | Add product by scanning of GTIN (Optional) | Only possible on mobile device:Select scan and scan a barcode with the camera of the mobile device. | The product is added to the list of products. In case the product was already contained in the list, the number increase by one. |  |
| 8 | Add product using hardware scan (Optional) | Only possible on MDE or ruggedized devices with an extension of the Custom SAP Fiori client.Select (hardware) scan of the MDE and scan a barcode. | The product is added to the list of products. In case the product was already contained in the list, the number increase by one. |  |
| 9 | Navigate to product list | Select the product to navigate to product list screen. | The product details are displayed. |  |
| 10 | Change the stock type | Change the stock type as per requirement to Unrestricted useQuality Inspection or Blocked |  |  |
| 11 | Create new placement | Select Add, select the Quantity unit from the dropdown list and select Add. | New placement is created with the selected quantity unit and quantity as 0. |  |
| 12 | Adjust the quantity | Either enter the quantity field directly in the quantity field for the new placement created or select Additional Unit, enter the quantity: 20 and Quantity unit: CAR and select Add. | Quantity updated message is displayed and quantity is successfully updated in the new placement |  |
| 13 | Back to overview | Select Back to Overview. | Navigation to the main screen. |  |
| 14 | Document Posting | Select Submit | The status of the stock document is changed from ‘In Process' to ‘Posted'.Verify if the posting was successful in step [Overview of Stock– Single Material](#unique_29) [page ] 25. |  |
| 15 | Print and submit | Execute steps from 1 to 13 and select Print and Submit. | The status of the stock document is changed from ‘In Process’ to ‘Posted’.Print document is sent to the cloud print manager.Verify if the posting was successful in step [Overview of Stock– Single Material](#unique_29) [page ] 25. |  |

#### Overview of Stock– Single Material

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows, how you can display the stock overview of a material for a particular plant.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log onto the SAP Fiori launchpad as a Warehouse Clerk (Retail). |  |  |
| 2 | Access the app | Open Stock - Single Material (F1076) app. | In tile group Warehouse Stock MonitoringThe Stock - Single Material (F1076) screen is displayed. |  |
| 3 | Enter Material | Make the following entries:Material: R_1006Select Enter | The Stock - Single Material (F1076)shows the stock of material R_1006 in all the sites and storage locations.Verify if the stock has been updated, based on the quantity which was entered in the posted document, in test procedure [Count Stock Ad hoc](#unique_23) [page ] 23. |  |

### Adjust Mass Stock - Options

#### Adjust Mass Stock (Option 1)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The app Adjust Mass Stock (F4959) can be used to adjust the stock for different reasons such as damaged, stolen, own consumption, etc. “Mass” means scanning and posting the adjustment for several products at once. A typical use case would be: As a store associate, you take a shopping cart in the morning, you walk in the store and collect all products that are for some reason not sellable. Then, you open this app, you scan the products and post the adjustment in the S/4 system. Therewith, you correct the stock quantity. As a result, your store replenishment will be more accurate. And, when you look up the product for customer service, you will have an accurate stock info.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori launchpad as a Retail Store Associate . |  |  |
| 2 | Access app | Open Adjust Mass Stock - TODAY (F4959) app. | The Adjust Mass Stock (F4959) app is displayed. |  |
| 3 | Create stock adjustment | Select Create on the upper right corner. | A new stock adjustment in in process status gets created for the store.If the user is new to the app, the reason and the Location of the store adjustment will be blank, which needs to be filled.If the user is not login for first-time, then the Reason and Storage location is prefilled with the values selected for the last created stock adjustment.The list of products is empty. |  |
| 4 | Maintain basic information | Maintain the following entries:Reason : Goods receipt unplanned (3)Location : 994ANote The goods movement type for adjustment posting is linked to the reason.Reason: Goods receipt unplanned (0003) is linked to movement type 501 (Receipt w/o PO) | Values are accepted. |  |
| 5 | Add product by search | Select + and select the required product R_1038 by searching in the search tab available.Select the product available in the list. Selected products will be updated in the product list.Select Add to add the product to the list. | product added message is displayed and the product added. |  |
| 6 | Add product by GTIN | Select Scan Bar Code and enter the EAN/GTIN XXXXXXX of another product in the Bar Code field and select OK. | The product is added to the list of products with message product added.In case the product was already in the list, the quantity should increase by 1 with a message product added. |  |
| 7 | Optional: add product by scanning of GTIN | Only possible on mobile device:Select Scan to scan a barcode with the camera of the mobile device. | The product is added to the list of products with message product added.In case the product was already in the list, the quantity should increase by 1 with a message product added. |  |
| 8 | Optional: Add product using hardware scan | Only possible on MDE or ruggedized devices with an extension of the Custom SAP Fiori clientSelect (hardware) scan of the MDE and scan a barcode | The product is added to the list of products with message product added.In case the product was already in the list, the quantity should increase by 1 with a message product added. |  |
| 9 | Adjust quantity | Enter the required Quantity: 29 to be adjusted either in the Quantity field directly or select + and enter the Quantity and select Quantity Unit from the dropdown list. | The price is updated accordingly to the entered quantity. |  |
| 10 | Submit stock adjustment | Select SubmitMessage Stock Adjustment is Submitted is displayed. | Navigate to Completed tab and refresh the adjustments.Validate the status of the stock adjustment is changed from In Process to Posted. |  |
| 11 | Print and submit | Follow the test steps from 1 to 9 and select Print and submit.It displays message Print and submit request completed. | Navigate to Completed tab and refresh the adjustments.Validate the status of the stock adjustment is changed from In Process to Posted. |  |

#### Adjust Mass Stock with Add Claim (Option 2)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

While performing goods receiving, you notice that a product was arrived damaged. In such case, you adjust the stock because the product is not sellable, and at the same time you file a claim against the shipping company as per your contract. The adjustment including the claim can be printed out for handing to a responsible person or it can be emailed.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori launchpad as a Retail Store Associate. |  |  |
| 2 | Access app | Open Adjust Mass Stock - TODAY (F4959) app. | The Adjust Mass Stock - TODAY (F4959) app is displayed. |  |
| 3 | Create stock adjustment | Select Create from the top right corner. | A new stock adjustment in in process status gets created for the store.If the user is new to the app, the Reason and the location of the store adjustment will be blank, which needs to be filled.If the user is not login for first-time, then the Reason and Storage location is prefilled with the values selected for the last created stock adjustment.The list of products is empty. |  |
| 4 | Maintain basic information | Change theReason : Breakage/Spoilage of stock Article (1)Location : for example 994ANote The goods movement type for adjustment posting is linked to the reason.Reason: Breakage/spoilage of stock material (0001) is linked to movement type 551 (GI scrapping) | Values are accepted. |  |
| 5 | Add product by search | Select + and select the required product R_1038 by searching in the search tab available.Select ON available near to product “Selected 1” gets updated above the product.Select Add to add the product to list. | product added message is displayed and the product is added. |  |
| 6 | Adjust quantity | Enter the required Quantity: 29 to be adjusted either in the Quantity field directly or by Selecting on the + icon and by entering the Quantity and selecting the Quantity Unit from the dropdown list. | The price is updated accordingly to the entered quantity. |  |
| 7 | Add a claim | Select Add Claim and enter the mandatory field Cost Center: for example 3340Select Add | claim added message is displayed and View claim option visible below the product GTIN |  |
| 8 | Submit stock adjustment | Select SubmitMessage Stock adjustment is submitted is displayed. | Navigate to Completed tab and refresh the adjustments.Validate the status of the stock adjustment is changed from In Process to Posted. |  |
| 9 | Display claim | Select the Posted document and select Claim Info link. | Claim details is displayed. |  |

### Transfer of Product

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows, how you can process transfers of products from one store to another store or from a store to a distribution centre. All documents relevant for a transfer are created and filled automatically. The SAP Fiori app transfer products covers and simplifies all steps involved in a product transfer and enables store associates to transfer products more efficiently.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori launchpad as a Retail Store Associate. |  |  |
| 2 | Access app | Open Transfer Products (F2449) app. | Transfer Product app is displayed. |  |
| 3 | Create transfer | Select create transfer and enter the following fields:Receiving Site Category : StoreReceiving Site : 3341Reason for Transfer : Too much deliveredSelect CreateShows message Your Transfer was created. The detail screen is displayed containing 0 items. | Entry is updated. |  |
| 4 | Add product | Select Add Product (+) , enter the Product: R_1037 in search and select Magnifying Glass icon.Select ON near to the product and select Select .(Optional: add product by Scan Product and enter the GTIN : XXXXXXXXXXX). | 1 Item added to the box message is displayed. |  |
| 5 | Adjust the quantity | Change the Quantity: 2 of the products and ENTER | The quantity is updated accordingly. |  |
| 6 | Add additional product | Select Add Product (+) , Enter the P roduct: R_1003005 in search and select magnifying glass icon.Select ON near to the product and select Select.(Optional: add product by Scan Product and enter the GTIN : XXXXXXXX). | 1 Item added to the box message is displayed. |  |
| 7 | Adjust the quantity | Change the Quantity: 3 of the products | The quantity is updated accordingly. |  |
| 8 | Print shipping and content labels | In More (…) Select Print | The labels will be printed. |  |
| 9 | Submit transfer | Select Submit to submit the transfer and Select OKNote If you haven't set up your printer yet, a notification will appear You have not selected a printer yet. Your documents will not be printed automatically.Submit this transfer? is displayed. | A popup with status Submitting will appear. The system constantly update the status of transfer to following status:In – Transit: Transfer Boxes are In Transit (After the goods issue posting with the movement type 641 - the TF to stock in trans). |  |

### Schedule Clean Up of Operational In-Store Data (Optional)

#### Schedule Clean Up of Operational In-Store Data - Count Stock Ad hoc

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to clean up the unused operational data from Count Stock Ad hoc (F5563) app.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori launchpad as an Administrator (Retail) |  |  |
| 2 | Access app | Open Schedule Clean Up of Operational In-Store Data (F5594) app. | The Application Jobs screen is displayed |  |
| 3 | Provide input values | On the initial screen, select Create:Job Template: Clean-up of Operational In-Store DataJob Name: Clean-up of Operational In-Store DataSelect Step2Select Step3Select Parameters for selection criteria:Under Count Stock Ad hoc section:Ensure Delete Data check box is selected.Enter F4 Help at Processing Status and choose In Process status for deleting the documents which are in In Process status and select Create.Note As we are testing for Count Stock Ad hoc, we uncheck the Delete Data check box under Adjust Mass Stock, Transfer Products and Notifications.Note In Count Stock Adhoc app, scheduling clean-up activity for operational in-store data is only eligible after the validation period of more than 48 hours as per the Configuration Settings. | Entry is updated. |  |
| 4 | Check | Select Check for validating. | A message is displayed as You can go ahead and schedule the job. |  |
| 5 | Schedule Job | Select Schedule and following message is displayed as Job Clean Up of Operational In-Store Data has been scheduled. |  |  |
| 6 | Check Job Results | On the Application Jobs screen, after job item status turned to Finished, choose Navigate to the job results in the Results column.Note Repeat the same steps to perform deletion for other statuses also. | Document (ID XXXXXX) is displayed with job results. |  |

Result

Documents which are under selected status are deleted.

#### Schedule Clean Up of Operational In-Store Data – Adjust Mass Stock

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to clean up the unused operational data from Adjust Mass Stock (F4959) app.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori launchpad as an Administrator (Retail). |  |  |
| 2 | Access app | Open Schedule Clean Up of Operational In-Store Data (F5594) app.. | The Application Jobs screen is displayed. |  |
| 3 | Provide input values | On the initial screen, select CreateJob Template: Clean-up of Operational In-Store DataJob Name: Clean-up of Operational In-Store DataSelect Step2Select Step3Select Parameters for selection criteria:Under Adjust Mass Stock section:Ensure Delete Data check box is selected.Select F4 Help at Processing Status and choose In Process status for deleting the documents which are in In Process status and select Create.Note As you are testing for Adjust Mass Stock, you uncheck the Delete Data check box under Count Stock Ad hoc, Transfer Products and Notifications.Note In Adjust Mass Stock app, scheduling clean-up activity for operational in-store data is only eligible after the validation period of more than 24 hours as per the Configuration Settings. | Entry should be updated. |  |
| 4 | Check | Select Check for validating. | A message is displayed as You can go ahead and schedule the job. |  |
| 5 | Schedule Job | Select Schedule and following message appears Job Clean Up of Operational In-Store Data has been scheduled. |  |  |
| 6 | Check Job Results | On the Application Jobs screen, after job item status turned to Finished, choose Navigate to the job results in the Results column.Note Repeat the same steps to perform deletion for other statuses as well. | Document (ID XXXXXX) is displayed with job results.. |  |

Result

Documents which are under selected status are deleted.

#### Schedule Clean Up of Operational In-Store Data – Transfer Products

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to clean up the unused operational data from Transfer Products (F2449) app.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori launchpad as an Administrator (Retail). |  |  |
| 2 | Access app | Open Schedule Clean Up of Operational In-Store Data (F5594) app.. | The Application Jobs screen is displayed. |  |
| 3 | Provide input values | On the initial screen, select CreateJob Template: Clean-up of Operational In-Store DataJob Name: Clean-up of Operational In-Store DataSelect Step2Select Step3Select Parameters for selection criteria:Under Transfer Products section:Ensure Delete Data check box is selected.Maintain 0 days under Number of DaysSelect F4 Help at Processing Status of Count Stock Ad Hoc documents to Be Deleted and choose In Process status for deleting the documents which are in In Process status and select Create.Note As you are testing for Transfer Products, you uncheck the Delete Data check box under Count Stock Ad hoc, Adjust Mass Stock and Notifications. | Entry is updated. |  |
| 4 | Check | Select Check for validating. | A message is displayed as You can go ahead and schedule the job. |  |
| 5 | Schedule Job | Select Schedule and following message is dislayed Job Clean Up of Operational In-Store Data has been scheduled. |  |  |
| 6 | Check Job Results | On the Application Jobs screen, after job item status turned to Finished, choose Navigate to the job results in the Results column.Note Repeat the same steps to perform deletion for other statuses as well. | Document (ID XXXXXX) is displayed with job results.. |  |

Result

Documents which are under selected status are deleted.

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
- see-also :: [[11-inventory-warehouse-and-transportation/physical-inventory-cycle-counting-4lu-ae-test-script-sap-s-4hana-cloud]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/3HR_S4CLD2608_BPD_EN_AE.docx` — full document · extracted with `mammoth` · 61,467 chars in the whole document
