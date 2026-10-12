---
id: 16-two-tier-erp-and-central-finance/two-tier-erp-integrated-financial-planning-with-sap-analytics-cloud-22
title: "Two-Tier ERP: Integrated Financial Planning with SAP Analytics Cloud (S4CLD2608_2T_Integrated Financial Planning)"
description: "Customer guide for hybrid two-tier headquarter/subsidiary integrated financial planning with SAP Analytics Cloud and S/4HANA: prerequisites, connections, test steps (scope 4RC, 1YB)."
cluster: 16-two-tier-erp-and-central-finance
tags: [kb/two-tier-erp-and-central-finance, topic/financial-planning-hq-and-subsidiary]
aliases: [S4CLD2608_2T_Integrated Financial Planning]
keywords: [Two-Tier Financial Planning, integrated financial planning, two-tier erp, sap analytics cloud, data connections, master and actual data import, planning stories, planning data export, system prerequisites, scope items]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/General/Two-Tier_ERP_Assets_User_Guides/Two-Tier_ERP_Assets_User_Guides/Finance/S4CLD2608_2T_Integrated Financial Planning.docx]
confidence: low
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-227
topic: 16-two-tier-erp-and-central-finance/financial-planning-hq-and-subsidiary
language: ""
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Two-Tier ERP: Integrated Financial Planning with SAP Analytics Cloud (S4CLD2608_2T_Integrated Financial Planning)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/General/Two-Tier_ERP_Assets_User_Guides/Two-Tier_ERP_Assets_User_Guides/Finance/S4CLD2608_2T_Integrated Financial Planning.docx`, extracted with `mammoth`. Grouped under **Two-Tier Financial Planning** in Two-Tier ERP and Central Finance. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

|  |  |
| --- | --- |
| SAP Cloud ERP June 2026English |  |
|  | Two-Tier ERP: Integrated Financial Planning with SAP Analytics Cloud |
|  | Customer Guide |

Copyright

© 2021 SAP SE or an SAP affiliate company. All rights reserved.

No part of this publication may be reproduced or transmitted in any form or for any purpose without the express permission of SAP SE. The information contained herein may be changed without prior notice.

Some software products marketed by SAP SE and its distributors contain proprietary software components of other software vendors.

National product specifications may vary.

These materials are provided by SAP SE and its affiliated companies ("SAP Group") for informational purposes only, without representation or warranty of any kind, and SAP Group shall not be liable for errors or omissions with respect to the materials. The only warranties for SAP Group products and services are those that are set forth in the express warranty statements accompanying such products and services, if any. Nothing herein should be construed as constituting an additional warranty.

SAP and other SAP products and services mentioned herein as well as their respective logos are trademarks or registered trademarks of SAP SE in Germany and other countries. Please see http://www.sap.com/corporate-en/legal/copyright/index.epx#trademark for additional trademark information and notices.

| Revision | Change Date | Description |
| --- | --- | --- |
| 0 | 05-01-2021 | Initial version of document |

Icons

| Icon | Meaning |
| --- | --- |
| <!-- image omitted: unnamed --> | Caution |
| <!-- image omitted: unnamed --> | Example |
| <!-- image omitted: unnamed --> | Note |
| <!-- image omitted: unnamed --> | Recommendation |
| <!-- image omitted: unnamed --> | Syntax |

Typographic Conventions

| Type Style | Description |
| --- | --- |
| Example text | Words or characters that appear on the screen. These include field names, screen titles, pushbuttons as well as menu names, paths and options.Cross-references to other documentation. |
| Example text | Emphasized words or phrases in body text, titles of graphics and tables. |
| EXAMPLE TEXT | Names of elements in the system. These include report names, program names, transaction codes, table names, and individual key words of a programming language, when surrounded by body text, for example, SELECT and INCLUDE. |
| Example text | Screen output. This includes file and directory names and their paths, messages, source code, names of variables and parameters as well as names of installation, upgrade and database tools. |
| EXAMPLE TEXT | Keys on the keyboard, for example, function keys (such as F2) or the ENTER key. |
| Example text | Exact user entry. These are words or characters that you enter in the system exactly as they appear in the documentation. |
| <Example text> | Variable user entry. Pointed brackets indicate that you replace these words and characters with appropriate entries. |

Content

[1 Purpose 6](#_Toc60926355)

[2 Value Proposition 6](#_Toc60926356)

[2.1 Business Requirements 6](#_Toc60926357)

[2.2 Two-Tier Solution 6](#_Toc60926358)

[3 Business Process Details 6](#_Toc60926359)

[3.1 Prerequisites 6](#_Toc60926360)

[3.2 Process Flow with Technical Details 7](#_Toc60926364)

[4 Technical Requirement 7](#_Toc60926365)

[4.1 Import Data Connection from On-Premise Systems 7](#_Toc60926366)

[4.2 Import Data Connection from SAP S4/HANA Cloud System 8](#_Toc60926367)

[5 Test Procedure 8](#_Toc60926368)

[5.1 Prerequisites 8](#_Toc60926369)

[5.1.1 System Details 9](#_Toc60926370)

[5.2 Overview Table 9](#_Toc60926371)

[5.2.1 Load Master and Actual Data from SAP S/4HANA Cloud 9](#_Toc60926372)

[5.2.2 Perform Planning 11](#_Toc60926373)

[5.2.3 Export Planning Data to SAP S/4HANA Cloud 12](#_Toc60926374)

[6 Appendix 13](#_Toc60926375)

[6.1 Relevant Scope ID’s 13](#_Toc60926376)

[6.2 Integration Example 13](#_Toc60926377)

**Hybrid Cloud-Integrated Financial Planning with SAP Analytics Cloud**

## Purpose

This document provides a conceptual overview of performing Integrated Financial Planning in a Hybrid Cloud Headquarter Subsidiary deployment model with SAP Analytics Cloud.

## Value Proposition

### Business Requirements

The need to have standardized Integrated Financial Planning process in a Headquarter Subsidiary model where both entities can participate in the Planning process by taking the actuals as reference and can prepare the planning data for future periods for better monitoring, controlling the business operations and taking corrective measures.

### Two-Tier Solution

SAP Analytics Cloud is fully integrated with SAP S/4HANA. Integrated Financial Planning for SAP S/4HANA business content comes with demo data and allows you to import your own data from SAP S/4HANA and to export your planning results back to SAP S/4HANA. The complete integration is part of the content delivery and is available out of the box.

## Business Process Details

SAP Analytics Cloud is fully integrated with SAP S/4HANA and enables integrated financial planning and budgeting processes. Extract actual results from the Universal Journal in SAP Cloud ERP and populate a planning model in SAP Analytics Cloud for Planning.

Use extracted data in the SAP Analytics Cloud for Planning model as seed data for planning future periods as well as to report Actual versus Plan results. Export your planning results back to SAP S/4HANA.

Headquarter & Subsidiary can use SAP Analytics Cloud system for –

• Cost and activity planning to determine cost flows and activity rates

• Sales and Profitability planning to determine volume and price targets, expected discounts, and cost of goods sold

• Product cost simulation to determine raw material prices and activity usage

• Project planning to provide a baseline for revenue recognition and for capital expense projects

• Financial statement planning, including profit and loss, balance sheet, and cash flow

### Prerequisites

Hybrid ERP systems requiring SAP Analytics Cloud for their Financial Planning solution should meet the technical prerequisites as stated [here](https://help.sap.com/viewer/00f68c2e08b941f081002fd3691d86a7/release/en-US/11b4e5ff76eb4747bc255d7037be1f01.html?q=System%20Requirements%20and%20Technical%20Prerequisites).

For SAP S/4HANA Systems -

4. Business Content Activation and Integration Setup -

You must perform the following **Getting Started** activities for SAP Analytics Cloud:

For SAP S/4HANA Cloud Public Edition: [Getting Started with SAP Analytics Cloud](https://help.sap.com/docs/PRODUCT_ID/7532c8913c5342b7af98936276667f48/17428a92983b4261980511ee781b8cc4.html?state=PRODUCTION&version=Latest&locale=en-US" \o "https://help.sap.com/viewer/1cbcff7ccd35405ab445b223c1ab1588/latest/en-US/74b2bfa963214757b0746993603762be.html" \t "_blank)

For SAP S/4HANA: [Getting Started with SAP Analytics Cloud](https://help.sap.com/docs/SAP_SPORTS_ONE/7532c8913c5342b7af98936276667f48/17428a92983b4261980511ee781b8cc4.html" \o "https://help.sap.com/viewer/48f4b4785b8e45938ac44a67be8032d9/latest/en-US/74b2bfa963214757b0746993603762be.html" \t "_blank)

1. System access to SAP Analytics Cloud with Role of Planning Modeler.
2. The organizational structure and master data of your company have been created in SAP S/4HANA systems
3. Additional Manual Configuration as detailed in Set-Up instruction of [4RC](https://rapid.sap.com/bp/#/browse/scopeitems/4rc) & [1YB](https://support.sap.com/content/dam/SAAP/Sol_Pack/Library/Setup/1YB_Set-Up_EN_XX.pdf) scope item in Best Practice Explorer.

### Process Flow with Technical Details

<!-- image omitted: unnamed -->

## Technical Requirement

As a rule of thumb, the starting point for setting up a data connection from SAP Analytics Cloud is the [Data Connection Guide](https://saphanajourney.com/sap-analytics-cloud/data-connections/)

Additionally, the following guides can be followed for setting up the connections for the following connection types

Hybrid ERP systems requiring SAP Analytics Cloud for their Financial Planning solution should meet the technical prerequisites as stated [here](https://help.sap.com/viewer/00f68c2e08b941f081002fd3691d86a7/release/en-US/11b4e5ff76eb4747bc255d7037be1f01.html?q=System%20Requirements%20and%20Technical%20Prerequisites)

### Import Data Connection from On-Premise Systems

- [Enable SAP Analytics Cloud for data acquisition from On-Premise Systems](https://blogs.sap.com/2016/05/11/enable-sap-cloud-for-analytics-for-data-acquistion-from-on-premise-systems/)
- [Import Data connection to an SAP ERP System](https://help.sap.com/viewer/00f68c2e08b941f081002fd3691d86a7/release/en-US/f1f537fecf6e425bbd21b36bdd2a3fe3.html)
- [Troubleshoot Guide](https://blogs.sap.com/2016/08/26/troubleshooting-guide-sap-businessobjects-cloud-agent/)

You can refer to the following data connection matrix for more information on importing data connection from On Premise systems or SAP Cloud ERP Private

<!-- image omitted: unnamed -->

### Import Data Connection from SAP Cloud ERP

-
    - [Setting Up Import Connection setup with SAP Analytics Cloud for SAP S/4HANA Cloud](https://support.sap.com/content/dam/SAAP/Sol_Pack/Library/Setup/1YB_Set-Up_EN_XX.pdf) (Scope item 1YB) or refer to [Blog](https://blogs.sap.com/2020/12/14/setting-up-an-import-connection-setup-between-sap-s-4hana-cloud-and-sap-analytics-cloud-for-planning-integration/?update=publish) post.
    - The SAP Analytics Cloud agent doesn't need to be installed during the configuration process as compared to the steps explained previously.

## Test Procedure

### Prerequisites

This section summarizes all prerequisites to conduct the test in terms of systems, users, master data, organizational data, and other test data and business conditions. For details refer Best Practices Scope item [4RC](https://rapid.sap.com/bp/#/browse/scopeitems/4rc) and [1YB](https://rapid.sap.com/bp/#/browse/categories/sap_s%254hana/areas/cloud/packageversions/BP_CLD_ENTPR/S4CLD/2011/US/22/EN/scopeitems/1YB).

1. Business Content Activation and Integration Setup -

You must perform the following **Getting Started** activities for SAP Analytics Cloud:

For SAP Cloud ERP: [Getting Started with SAP Analytics Cloud](https://help.sap.com/docs/SAP_SPORTS_ONE/7532c8913c5342b7af98936276667f48/17428a92983b4261980511ee781b8cc4.html)

For SAP S/4HANA: [Getting Started with SAP Analytics Cloud](https://help.sap.com/docs/SAP_SPORTS_ONE/7532c8913c5342b7af98936276667f48/17428a92983b4261980511ee781b8cc4.html)

1. System access to SAP Analytics Cloud with Role of Planning Modeler.
2. The organizational structure and master data of your company have been created in S/4Hana systems
3. Additional Manual Configuration as detailed in Set-Up instruction of [4RC](https://rapid.sap.com/bp/#/browse/scopeitems/4rc) & [1YB](https://support.sap.com/content/dam/SAAP/Sol_Pack/Library/Setup/1YB_Set-Up_EN_XX.pdf) scope items.

#### System Details

The test is conducted in the following systems:

| System | Details |
| --- | --- |
| On-Premise System - Headquarters | SAP S/4HANA 1709 or higher |
| SAP Cloud ERP - Subsidiary | Release 2005 or higher |
| SAP Analytics Cloud | Latest Release |

### Overview Table

Reference Test Script - Scope [4RC](https://rapid.sap.com/bp/#/browse/scopeitems/4rc) and [1YB](https://rapid.sap.com/bp/#/browse/categories/sap_s%254hana/areas/cloud/packageversions/BP_CLD_ENTPR/S4CLD/2011/US/22/EN/scopeitems/1YB).

#### Load Master and Actual Data from SAP S/4HANA Cloud Public Edition

After you have familiarized yourself with the Demo data of the Integrated Financial Planning for SAP S/4HANA business content, you can now import your own master and transaction data from your SAP S/4HANA system to SAP Analytics Cloud.

For details on Planning Models, Stories, Data Actions in SAP Analytics Cloud refer to Test Script for Scope [4RC](https://rapid.sap.com/bp/#/browse/scopeitems/4rc) for Data Import Testing steps.

1. Delete Demo Data
2. Import your **Master data** to the public dimensions of the following models:

- SAP__FI_BPL_IM_COSTCENTER
- SAP__FI_BPL_IM_PRODUCTCOST
- SAP__FI_BPL_IM_PROFITABILITY
- SAP__FI_BPL_IM_PROJECT
- SAP__FI_BPL_IM_INTERNAL_ORDER
- SAP__FI_BPL_IM_CAPEX
- SAP__FI_BPL_IM_FINANCIAL_STATEMENT

Test Steps details in [1YB](https://rapid.sap.com/bp/#/browse/categories/sap_s%254hana/areas/cloud/packageversions/BP_CLD_ENTPR/S4CLD/2011/US/22/EN/scopeitems/1YB) Scope item in Best Practices Explorer -

| Test Step # | Test Step Name | Instruction | Expected Result |
| --- | --- | --- | --- |
| 1. | Log on to SAP Analytics Cloud | Log on to SAP Analytics Cloud. | The Home screen is displayed. |
| 2. | Access Browse Dimension | Open Main Menu > Browse > Dimensions . | The Public Dimensions screen is displayed. |
| 3. | Access Import Data | Select your public dimension and choose Import Data > Datasource .On the Select a Datasource screen, choose SAP S/4HANA. Under Connection, select a name, for example S4HODATACON. | The Connection is set. |
| 4. | Create New Query | Choose Create New Query and then choose Next.On the New Query for SAP S/4HANA screen, enter a name for the query.Select your entity type (for example, A_ProfitCenter) and choose Next.On the Build SAP S/4HANA Query screen, drag the fields that you need for the public dimension (for example, Profit Center and Name) into the Selected Data area.Choose Create.A data preview is displayed. Adjust the proposed mapping of the OData columns to the columns of the public dimensions.Choose Finish Mapping and then choose Finish. | Master data is imported into public dimension. |

1. Importing Your**Actual Data**(transaction data) to the following models:

- SAP__FI_BPL_IM_COSTCENTER
- SAP__FI_BPL_IM_PRODUCTCOST
- SAP__FI_BPL_IM_PROFITABILITY
- SAP__FI_BPL_IM_FINANCIAL_STATEMENT
- SAP__FI_BPL_IM_PROJECT
- SAP__FI_BPL_IM_INTERNAL_ORDER
- SAP__FI_BPL_IM_CAPEX

| Test Step # | Test Step Name | Instruction | Expected Result |
| --- | --- | --- | --- |
| 1 | Open SAP Analytics Cloud | Use the URL and credentials provided by the system administrator. | The Home - Welcome to SAP Analytics Cloud screen is displayed. |
| 2 | Planning Model | From the main menu, choose Browse > Files Search for and open Model. Eg.SAP__FI_BPL_IM_COSTCENTER. | The model is displayed. |
| 3 | Dimension | Choose dimensions of Model eg. SAP_FI_BPL_GLACCOUNT. | Dimension displayed |
| 4 | Data Management | Choose the Data Management tab. | The Data Management tab is displayed. |
| 5 | Refresh the Job | Choose the Refresh button to the right of the job. | The system displays a message stating number of rows imported. |
| 6 | Repeat | Repeat steps 3 to 5 for the all dimensions in the model. | The system displays a message stating number of rows imported. |
| 7 | Data Management | Choose the Data Management tab. | The Data Management tab is displayed. |
| 8 | Refresh the Job to Load Actual Data | Under Import Jobs, choose Refresh to the right of the job [Actual Data] A_JournalEntryItemBasicQuery. | The system displays a message stating number of rows imported. |

#### Perform Planning

Integrated Financial Planning can be performed in SAP Analytics Cloud System by performing Data actions on the Stories for Cost Center Planning and Budgeting, Product Cost Planning, Sales and Profitability Planning, Product Cost Planning, Project Planning and Financial Statement Planning. Refer to [link](https://help.sap.com/viewer/21868089d6ae4c5ab55f599c691726be/release/en-US/7b8caa06f850453fab8d570be92f4c99.html) for Integrated Financial Planning details in SAP Analytics Cloud in current release.

Each story can be used separately or in a specific order to simulate the end-to-end process.

| Process Step | Business Role | App/Transaction | Expected Results |
| --- | --- | --- | --- |
| Cost Center Planning and Budgeting | Admin, Planner | SAP Analytics Cloud | Expense planning, allocations, activity quantity planning, activity cost rate planning, and activity cost rate calculations. |
| Product Cost Planning | Admin, Planner | SAP Analytics Cloud | Calculation and simulation of product costs based on raw material prices and activity cost rates. |
| Sales and Profitability Planning | Admin, Planner | SAP Analytics Cloud | Sales and quantity planning and simulation, revenue, deductions, and cost of goods sold calculations. |
| Project Planning | Admin, Planner | SAP Analytics Cloud | Planning of costs associated with a project or program. |
| Internal Order Planning | Admin, Planner | SAP Analytics Cloud | Internal order costs on G/L account basis. |
| Investment Planning | Admin, Planner | SAP Analytics Cloud | Profit center expenses for acquiring, maintaining, or improving fixed assets such as buildings, vehicles, equipment, or land. |
| Financial Statement Planning | Admin, Planner | SAP Analytics Cloud | Profit and loss planning with trading partner allocation and balance sheet planning. |

Run Planning Admin Task Story before performing the Planning Story. Refer to Test Script Scope Id [4RC](https://rapid.sap.com/bp/#/browse/scopeitems/4rc).

Perform Planning Story

| Test Step # | Test Step Name | Instruction | Expected Result |
| --- | --- | --- | --- |
| 1 | Access the Story Page | From the main menu, open Browse > Files > Public > SAP Content > SAP_FI_BPL_Budgeting_and_Planning | The Files page is displayed. |
| 2 | Access the Story | Find and display the story | The Story is displayed. |
| 3 | Copy actuals | Use data action - Actual based. | Actual data is displayed |
| 4 | Maintain planning | Maintain planning values | Planning Values are maintained |
| 10 | Run | Use data action to Execute/Calculate. | Check calculated amounts. |
| 11 | Reporting | Go to Reporting tab | Check plan data. |

<!-- image omitted: unnamed -->

#### Export Planning Data to SAP Cloud ERP

| Test Step # | Test Step Name | Instruction | Expected Result |
| --- | --- | --- | --- |
| 1 | Access the Model Page | From the main menu, open Browse > Files . | The Files page is displayed. |
| 2 | Access the Model | Find and display the model | The Model is displayed. |
| 3 | Open Data Management | Choose Data Management. | Import and Export jobs are displayed |
| 4 | Create Export | On the Export Jobs section, choose Export Data to SAP S/4HANA. | Follow the wizard as described in the documentation |

We can Export the planning data back to ACDOCP (Planning Table), Activity Type Plan Cost Rates to ACCOSTRATE or Statistical Key Figures to FINSSKF.

Follow the instructions in [Exporting Data from SAP Analytics Cloud to SAP S/4HANA Cloud](https://help.sap.com/docs/SAP_S4HANA_CLOUD/1cbcff7ccd35405ab445b223c1ab1588/15447e5bda934be28f3b16cfb456fb23.html).

The data that is loaded into ACDOCP should be available in Analytical reports for comparison with the actuals (Apps like Cost Center – Plan/Actuals, Cost Center – Plan/Actuals YTD, Internal Order – Plan/Actuals, Internal Order – Plan/Actuals YTD).

## Appendix

### Relevant Scope ID’s

Import Connection setup with SAP Analytics Cloud (1YB)

[1YB -Import Connection Setup with SAP Analytics Cloud](https://rapid.sap.com/bp/#/browse/categories/sap_s%254hana/areas/cloud/packageversions/BP_CLD_ENTPR/S4CLD/2011/US/22/EN/scopeitems/1YB)

[4RC -Integrated Financial Planning](https://rapid.sap.com/bp/#/browse/scopeitems/4rc)

### Integration Example

[Integrated Financial Planning for Hybrid ERP with SAP Analytics Cloud](https://blogs.sap.com/2020/12/21/integrated-financial-planning-for-hybrid-erp-with-sap-analytics-cloud/)

## Suspected conflicts

> [!warning] Conflict
> Flagged while digesting this document, not verified: Cover says June 2026 release but revision history and copyright date from 2021; content may be dated

## Connections
- part-of :: [[_cluster]]
- related-to :: [[16-two-tier-erp-and-central-finance/two-tier-subsidiary-as-financial-planning-and-upload-of-plan-data-from]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/General/Two-Tier_ERP_Assets_User_Guides/Two-Tier_ERP_Assets_User_Guides/Finance/S4CLD2608_2T_Integrated Financial Planning.docx` — full document · extracted with `mammoth` · 19,564 chars in the whole document
