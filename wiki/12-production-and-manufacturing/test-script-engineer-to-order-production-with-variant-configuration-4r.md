---
id: 12-production-and-manufacturing/test-script-engineer-to-order-production-with-variant-configuration-4r
title: "Test Script: Engineer-to-Order Production with Variant Configuration (4R8_AE) (4R8_S4CLD2608_BPD_EN_AE)"
description: "SAP S/4HANA Cloud Public Edition 2608 test script for scope item 4R8 (AE): ETO sales order, Order BOM creation and acceptance of engineering changes."
cluster: 12-production-and-manufacturing
tags: [kb/production-and-manufacturing, topic/engineer-to-order-variant-configuration]
aliases: [4R8_S4CLD2608_BPD_EN_AE]
keywords: [Engineer-to-Order with Variant Configuration, engineer-to-order, variant configuration, order bom, sales order creation, engineering changes acceptance, configuration profile, sample master data, business roles, demo data update behavior]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/4R8_S4CLD2608_BPD_EN_AE.docx]
confidence: high
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-1047
topic: 12-production-and-manufacturing/engineer-to-order-variant-configuration
language: EN
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Test Script: Engineer-to-Order Production with Variant Configuration (4R8_AE) (4R8_S4CLD2608_BPD_EN_AE)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/4R8_S4CLD2608_BPD_EN_AE.docx`, extracted with `mammoth`. Grouped under **Engineer-to-Order with Variant Configuration** in Production and Manufacturing. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

| <!-- image omitted: unnamed --> | Test ScriptSAP S/4HANA Cloud Public Edition - 19-06-26 |
| --- | --- |
|  | Engineer-to-Order Production with Variant Configuration (4R8_AE) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Table of Contents

[1 Purpose 2](#_Toc232855478)

[2 Prerequisites 3](#_Toc232855479)

[2.1 System Access 3](#_Toc232855480)

[2.2 Roles 3](#_Toc232855481)

[2.3 Master Data, Organizational Data, and Other Data 4](#_Toc232855482)

[2.4 Business Conditions 7](#_Toc232855483)

[2.5 Preliminary Steps 7](#_Toc232855484)

[2.5.1 Change Configuration Profile to Assign Characteristic Group 7](#_Toc232855485)

[3 Overview Table 10](#_Toc232855486)

[4 Test Procedures 11](#_Toc232855487)

[4.1 Create Sales Order 11](#_Toc232855488)

[4.2 Creation of Order BOM 13](#_Toc232855489)

[4.3 Accept Changes of Engineering and Save Sales Order 15](#_Toc232855490)

## Purpose

Overview

The scenario enables the Order BOM processing type, which is used to make customer-specific changes to the BOM of a material that you configure in the sales order. The process supports a handover between sales order creation, order BOM preparation, and acceptance of those changes within the sales order.

This document provides a detailed procedure for testing this scope item after solution activation, reflecting the predefined scope of the solution. Each process step, report, or item is covered in its own section, providing the system interactions (test steps) in a table view. Steps that are not in scope of the process but are needed for testing are marked accordingly. Project-specific steps must be added.

|  |
| --- |
| Note Values in this test script (decimal notation, date formats, and so on) are presented in U.S. standard notation. If your test system is set up to use a different notation, enter values as appropriate. |

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
| Product Configuration ModelerMaintains the variant-configuration-specific master data such as classes, characteristics, variant conditions, dependencies, configuration profiles, and so on.Collaborates with PLM department, production supervisors, and others relevant to manufacturing. | SAP_BR_PRODUCT_CONFIG_MODELER | Variant Configuration | SAP_BR_PRODUCT_CONFIG_MODELER |  |
| Internal Sales RepresentativeInternal Sales | SAP_BR_INTERNAL_SALES_REP | Internal Sales / Customer Returns / Billing | SAP_BR_INTERNAL_SALES_REP / SAP_SD_SPT_RETURNS_INT_SALES_PC / SAP_SD_SPT_BILLING_INT_SALES_PC |  |
| BOM Engineer - Customer Order | SAP_BR_BOM_ENG_CUST_ORDER | Bills of Material - Customer Orders | SAP_BR_BOM_ENG_CUST_ORDER |  |

### Master Data, Organizational Data, and Other Data

The organizational structure and master data of your company is created in the system during activation. The organizational structure reflects the structure of your company. The master data represents materials, customers, and vendors, for example, depending on the operational focus of your company.

|  |
| --- |
| Caution Update Behavior of Predelivered Demo DataIn non-productive environments (such as starter systems, sandbox systems, or partner demo systems), SAP initially deploys demo data for your selected scope. You can use this data to test and evaluate business processes.In a customer system, you can receive new or updated demo data after initial activation with further scope enhancements, provided the existing demo data wasn't changed in an incompatible way. If activation errors occur due to incompatible changes in demo data, you're responsible for resolving them. If you don't resolve the errors within a specific time frame, SAP reserves the right to deactivate demo data in your systems. In this case, you can continue by creating your own demo data. Alternatively, you can request that your systems be reprovisioned if you want to work with predelivered demo data again.In partner systems, you can use the demo data deployed with the initial activation. No additional demo data will be deployed in the system with scope enhancements. You can only create additional demo data manually. |

Use your own master data or the following sample data to go through the test procedures.

Table 1: Multi-Level Configurable BOM

| Data | Sample Value | Details | Comments |
| --- | --- | --- | --- |
| Plant | 3310 | Plant 1 AE |  |
| Material | AVC_RBT_ROBOT2 | Robot Multi-Level | Configurable Material |
| Material | AVC_RBT_LINKARM | Link Arm (Configurable) | Configurable Material |
| Material | AVC_RBT_CONTROL | Control Unit (Configurable) | Configurable Material |
| Material | AVC_RBT_MOTOR_2XX | Motor 2XX | Semi-finished Material |
| Material | AVC_RBT_BRD_PAINT | Painting Unit | Semi-finished Material |
| Material | AVC_RBT_BRD_SEAL | Sealing Unit | Semi-finished Material |
| Characteristic | AVC_RBT_MOTOR_GRP | Motor Group |  |
| Characteristic | AVC_RBT_SPEED_GRP | Speed |  |
| Characteristic | AVC_RBT_SPEED_1 | Speed Motor 1 |  |
| Characteristic | AVC_RBT_SPEED_2 | Speed Motor 2 |  |
| Characteristic | AVC_RBT_SPEED_3 | Speed Motor 3 |  |
| Characteristic | AVC_RBT_SPEED_4 | Speed Motor 4 |  |
| Characteristic | AVC_RBT_SPEED_5 | Speed Motor 5 |  |
| Characteristic | AVC_RBT_SPEED_6 | Speed Motor 6 |  |
| Characteristic | AVC_RBT_LEN_DRIVEARM | Length of Drive Arm |  |
| Characteristic | AVC_RBT_LEN_LINKARM | Length of Link Arm |  |
| Characteristic | AVC_RBT_RMAX_REQ | Reach(Maximum) - Requested |  |
| Characteristic | AVC_RBT_RMAX_TECH | Reach(Maximum) -Technical |  |
| Class | AVC_RBT_SALES | Robot Sales Data | Class of Type 300 |
| Class | AVC_RBT_ROBOT_REQ | Robot Sales Requirement Data | Class of Type 300 |
| Class | AVC_RBT_ROBOT_ENG | Robot Technical Data | Class of Type 300 |
| Class | AVC_RBT_CN_L_ARM | Link Arm | Class of Type 300 |
| Class | AVC_RBT_CONTROL | Control Data | Class of Type 300 |
| Class | AVC_RBT_CN_MOTOR | Motor | Class of Type 200 |
| Dependencies | AVC_RBT_DEF_LEN_ARM_CTO | Set default values for arm len |  |
| Dependencies | AVC_RBT_DEF_LEN_ARM_ETO | Set default values for arm len |  |
| Dependencies | AVC_RBT_TECH_REACH_ETO | Set Technical Reach |  |
| Dependencies | AVC_RBT_PRICING_SLA | Pricing SLA |  |
| Dependencies | AVC_RBT_PRICING_REACH_CTO | Pricing Conditions for Robot |  |
| Dependencies | AVC_RBT_PRICING_REACH_ETO | Pricing Conditions for Robot |  |
| Dependencies | AVC_RBT_PR_CN_MOTOR1 | Set values for class node |  |
| Dependencies | AVC_RBT_PR_CN_MOTOR2 | Set values for class node |  |
| Dependencies | AVC_RBT_PR_CN_MOTOR3 | Set values for class node |  |
| Dependencies | AVC_RBT_PR_CN_MOTOR4 | Set values for class node |  |
| Dependencies | AVC_RBT_PR_CN_MOTOR5 | Set values for class node |  |
| Dependencies | AVC_RBT_PR_CN_MOTOR6 | Set values for class node |  |
| Dependencies | AVC_RBT_SC_PAINT | Select for Painting |  |
| Dependencies | AVC_RBT_SC_SEAL | Select for Sealing |  |
| Variant Table | AVC_RBT_SPEED | Speed |  |
| BOM | AVC_RBT_ROBOT2 | Robot Multi-Level |  |
| BOM | AVC_RBT_LINK_ARM | Link Arm (Configurable) |  |
| BOM | VC_RBT_CONTROL | Control Unit (Configurable) |  |
| Configuration Profile | ETO | ETO |  |
| Configuration Profile | CTO | CTO |  |
| Characteristic Group | AVC_ROBOT_BASIC | Basic |  |
| Characteristic Group | AVC_RBT_REACH | Reach |  |
|  |  |  |  |

Table 2: Sales Center

| Data | Sample Value | Details | Comments |
| --- | --- | --- | --- |
| Sales Organization | 3310 |  | National |
| Distribution Channel | 10 |  | Direct Sales |
| Customer | 33100001 |  |  |

For more information on creating master data objects, see the following [Master Data Scripts (MDS)](https://help.sap.com/docs/s4hana-best-practices/s4cld2608-master-data)

Table 3: Master Data Script Reference

| Master Data ID | Description |
| --- | --- |
| BNS | Create Product Master of type "Semi-Finished Good" - MDS |
| 2T7 | Create Product Master of Type "Configurable Material" - MDS |

### Business Conditions

Before this scope item can be tested, the following business conditions must be met.

| Scope Item ID | Business Condition |
| --- | --- |
| 22T - Set Up Configurable Model Using Variant Configuration | To simulate configurable materials, the 22T - Set Up Configurable Model Using Variant Configuration scope item must be activated in the system. |

### Preliminary Steps

#### Change Configuration Profile to Assign Characteristic Group

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this process step, you assign characteristic group to configuration profile.

Procedure

| Test Step # | Test Step Name | Instructions | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori launchpad as Product Configuration Modeler. | The SAP Fiori launchpad displays. |  |
| 2 | Access the app | Open the VC Modeling Environment (PMEVC) app. | The Initial Screen of Variant Configuration Modeling Environment screen displays. |  |
| 3 | Enter the configuration model data | On the initial screen, make the following entries, and choose Enter Model.Material: AVC_RBT_ROBOT2Class Type: 300 (Default)Plant: 3310BOM Application: PP01 | The configuration screen displays. |  |
| 4 | Assign characteristic group to profile | In the Object section, expand the root node and double-click the configuration profile CTO node.The Configuration Profile screen displays in the right pane.Select the User Interface tab.Choose Assign Characteristic Groups.A dialog box to confirm whether to leave the page with unsaved data might be displayed.Choose Edit. | The Configuration Profile screen displays in a new browser tab. |  |
| 5 | Assign group to configuration profile | Choose Edit.Choose Assign Group.In Select: Characteristic Groups screen, search for AVC_ROBOT_BASIC, and choose Go.Select the item displayed under the Items section, and choose Ok. On the Configuration Profile screen, the selected characteristic is displayed under the Characteristic Groups section.Maintain the sorting order for the characteristic group as 1.Choose Save.Repeat the steps 1 and 5 for the following characteristic group .Sorting Order: 2Characteristic Group: AVC_RBT_REACHChoose Close. | Characteristics group is assigned to the configuration profile. |  |
| 6 | Repeat Steps for ETO | Repeat steps 2 to 6 for the following configuration profile:Configuration profile: ETO |  |  |

## Overview Table

This scope item consists of several process steps provided in the table below:

|  |
| --- |
| Note If your system administrator has enabled spaces and pages on the SAP Fiori launchpad, the homepage will only contain the essential apps for performing the typical tasks of a business role.You can find all other (searchable) apps not included on the homepage using the search bar ([2434549](https://me.sap.com/notes/2434549)).If you want to personalize the homepage and include the hidden apps, navigate to your user profile and choose App Finder. |

| Process Step | Business Role | App/Transaction | Expected Results |
| --- | --- | --- | --- |
| [Create Sales Order](#unique_9) [page ] 11 | Internal Sales Representative | Create Sales Orders - VA01 (VA01) | Sales order is created and released to Engineering |
| [Creation of Order BOM](#unique_10) [page ] 13 | BOM Engineer - Customer Order | Order Engineering Worklist (F4770) | The BOM Engineer creates an Order BOM, marks the Order BOM as Engineering finished and hands over back to sales. |
| [Accept Changes of Engineering and Save Sales Order](#unique_11) [page ] 15 | BOM Engineer - Customer Order | Change Sales Orders - VA02 (VA02) | The BOM Engineer either accepts the Engineering changes or sends it back to Engineering |

## Test Procedures

This section describes test procedures for each process step that belongs to this scope item.

### Create Sales Order

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you create a Sales Order and set values to the characteristics in both ETO and CTO profiles and handover it to Engineering for evaluating the changes.

Procedure

| Test Step # | Test Step Name | Instructions | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori launchpad as Internal Sales Representative |  |  |
| 2 | Access the App | Open the Create Sales Orders - VA01 (VA01) app. | The Create Sales Order - VA01 screen is displayed. |  |
| 3 | Create Sales Document | On the Create Sales Document screen, make the following entries and choose Continue.Order Type: OR (Standard Order)Sales Organization: 3310Sales Office:330Sales Group: 330Distribution Channel: 10Division: 00 | The Create Standard Order: Overview screen is displayed. |  |
| 4 | Enter Header Data | On the Create Standard Order: Overview screen, enter the following Header values:Sold-To-Party: 33100001Cust.Reference: TESTVC01Cust.Ref.Date: <Current date>Req. Deliv. Date: <As per requirement> |  |  |
| 5 | Enter Header Data | On the Create Standard Order: Overview screen, enter the following Item values and choose Enter:Item: 1Material: AVC_RBT_ROBOT2Order Quantity:10 | The valuation screen Variant Configuration loads automatically. |  |
| 6 | Start Multi-Level Valuation | On the Variant Configuration screen, choose the basic tab and provide the following Item values.Service Level Agreement: 8h at 5 days a weekRobot Application :SealingSpeed: Standard SpeedChoose the Reach tab and provide the following Item values.Reach(Minimum) Requested : 50 |  | The Reach(maximum) Requested is not sufficient for the Customer. |
| 7 | Switch to ETO profile | Choose Switch to ETO and Confirm.. | The valuation screen Variant Configuration for ETO profile is displayed. |  |
| 8 | Check Multi-Level Configuration | Ensure that previously entered values for the characteristics are intact:Service Level Agreement: 8h at 5 days a weekRobot Application:SealingSpeed: Standard SpeedReach(Minimum) Requested : 50 | The values entered for the characteristics should remain unchanged and the value range for Reach(Maximum) Requested should change to 50-380 from 50-190. |  |
| 9 | Finish Multi Level Valuation | On the Variant Configuration for ETO profile, provide the following values and choose Enter :Reach(Maximum) Requested : 230 | The following fields should get populated:Reach(Maximum) Technical : 230Reach(Minimum) Technical : 50Length of Link Arm : 60Length of Drive Arm: 110 | The values for the fields Length of Link Arm and Length of Drive Arm are the default values which are to be confirmed by choosing the Check button present against each field. |
| 10 | Release Order for Engineering | Choose Handover to Engineering.After choosing Handover to Engineering, if order quantity entered in step 5 is less than available quantity in the system, the Review Availability Check Result screen appears. It is to provide upfront information to the Internal Sales Representative regarding availability of material.Choose Handover. | The Create Standard Order: Overview screen is displayed and the Save button is enabled. |  |
| 11 | (Optional) Release Order for Engineering | After choosing Handover to Engineering, if Order Quantity entered in step 5 is less than the available quantity in the system, theReview Availability Check Result screen is displayed.Note You can choose to proceed or cancel the creation of sales order.If you want to still proceed even with lesser Order Quantity, choose Apply. | The Create Standard Order: Overview screen is displayed. |  |
| 12 | Save Sales Order | Choose Save to save the Sales Order. | The sales order is created. |  |

### Creation of Order BOM

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this process step, the BOM Engineer creates an Order BOM, marks the Order BOM as engineering finished and hands over back to sales.

.

Procedure

| Test Step # | Test Step Name | Instructions | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori launchpad as BOM Engineer - Customer Order. |  |  |
| 2 | Access the App | Open the Order Engineering Worklist (F4770) app. | The Manage Order Engineering items screen is displayed. |  |
| 3 | Select the Sales Order | Choose Ready for Engineering.Select the sales order created from the section [Create Sales Order](#unique_9) [page ] 11. | The Order Engineering Item Details screen is displayed. |  |
| 4 | Confirm the Default Values for Link and Drive Arm. | Go to Edit mode and check that the default values of Link Arm and Drive Arm are displayed.Length of Link Arm : 60Length of Drive Arm: 110 |  |  |
| 5 | Choose Bill Of Material in Header | From the Select View dropdown menu (next to Configurable Items ), select Bill of Material | The structure tree of the Bill Of Material is displayed. |  |
| 6 | Create Order Bill Of Material | Choose Fixate at the item level. The button ‘+’ on the same Header below Bill Of Material gets activated. Choose it to add the following component and then choose OK.Note If the Fixate button is not available, enlarge the Bill Of Material section.CategoryStock ItemProductAVC_RBT_D_ARM_110Position002DQuantity1 PCCheck the structure tree to see if the component is added. | The component gets added to the structure tree of Bill Of Material. |  |
| 7 | Handback to Sales | Choose Finish Engineering to release the Order.A dialog box, Confirmation is displayed, choose OK to confirm. | The document is handed over to Sales for review. |  |

### Accept Changes of Engineering and Save Sales Order

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this process step an Internal Sales Representative accepts the Engineering changes or sends back to Engineering.

Procedure

| Test Step # | Test Step Name | Instructions | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori launchpad as Internal Sales Representative. |  |  |
| 2 | Access the App | Open the Change Sales Orders - VA02 (VA02)app. | The Sales Order screen is displayed. |  |
| 3 | Open Sales Order | Search for the Sales Order created in the section [Create Sales Order](#unique_9) [page ] 11. | The Sales Order details are displayed in the Change Order Overview screen. |  |
| 5 | Open Configuration | Select the material and choose the button Item Details: Configuration. | The Variant Configuration screen is displayed. |  |
| 6 | Accept Changes of Engineering | Choose Accept Engineering Changes .A dialog box, Accept Engineering changes is displayed, choose Accept to confirm.On the Review Availability Check Result screen choose Apply. | The Engineering Changes are accepted and Change Order Overview screen is displayed. |  |
| 7 | Calculate Sales Order | In the Change Standard Order screen, select the line item and go to Menu > Extras > Costing .Choose EnterChoose Product Costing and check the details under Costing Data. If costing data is correct, then choose the Green circle to mark the estimate and then choose Save. For any errors, a red circle will appear instead of a green one. Upon hovering over this button, either a success message or an error message will be displayed. | The Sales Order Costing screen loads; costing details are accepted and saved. |  |
| 8 | Save Sales Order | Choose Save . | The Sales Order gets saved. |  |

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
- see-also :: [[02-business-partner-and-product-master-data/anwendungsgruppe-und-merkmalsanzeige-anlegen-sds-2ni-268]]
- see-also :: [[14-maintenance-service-and-projects/test-script-sap-s-4hana-cloud-public-edition-engineer-products-and-sys]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/4R8_S4CLD2608_BPD_EN_AE.docx` — full document · extracted with `mammoth` · 24,042 chars in the whole document
