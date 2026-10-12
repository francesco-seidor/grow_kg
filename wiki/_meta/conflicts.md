---
title: Conflicts
description: "Suspected disagreements and data errors flagged while digesting source documents, all unverified and awaiting a human decision."
tags: [kb/meta]
created: 2026-10-09
updated: 2026-10-12
---

# Conflicts

**709 open conflict callouts** across **439 pages**. Every one was flagged by a digest reading (unverified) and is carried verbatim on its page as a `> [!warning] Conflict` callout. None has been resolved; the register exists so someone with authority can.

| Cluster | Open conflicts |
| --- | --- |
| 01-solution-foundation-and-platform | 59 |
| 02-business-partner-and-product-master-data | 50 |
| 03-financial-accounting-and-close | 46 |
| 04-tax-and-statutory-reporting | 10 |
| 05-treasury-and-cash-management | 44 |
| 06-management-accounting | 30 |
| 07-group-reporting-and-consolidation | 43 |
| 08-sales-order-management | 63 |
| 09-subscription-billing-and-contract-accounting | 32 |
| 10-procurement | 55 |
| 11-inventory-warehouse-and-transportation | 73 |
| 12-production-and-manufacturing | 45 |
| 13-quality-ehs-and-compliance | 30 |
| 14-maintenance-service-and-projects | 66 |
| 15-retail-operations | 19 |
| 16-two-tier-erp-and-central-finance | 36 |
| 17-leasing-and-real-estate | 8 |

## C001 — availability-dependencies-en-xx-131-part-01

Page: [[01-solution-foundation-and-platform/availability-dependencies-en-xx-131-part-01]]

Scope items 2OO (External Tax Audit) and 5IM (Product Footprint Management) list themselves as their own Required Scope Item, which looks like a data error in the dependency column.

**Status:** open — needs a human decision

## C002 — availability-dependencies-en-xx-131-part-01

Page: [[01-solution-foundation-and-platform/availability-dependencies-en-xx-131-part-01]]

Contract Accounting and Convergent Invoicing items (e.g. 2DP, 3L3, 2BI, 2BK, 2AR, 2UJ, 2BE, 2BG) show 'Yes' instead of a release number in the CA, GB, IE and IN country columns, so the first-available release for those countries is not stated.

**Status:** open — needs a human decision

## C003 — availability-dependencies-en-xx-131-part-03

Page: [[01-solution-foundation-and-platform/availability-dependencies-en-xx-131-part-03]]

1JI Real-Time Reporting and Monitoring for Procurement lists 19C as a required scope item, but 19C Activity Management in Procurement is on the Retired Scope Items sheet.

**Status:** open — needs a human decision

## C004 — availability-dependencies-en-xx-131-part-03

Page: [[01-solution-foundation-and-platform/availability-dependencies-en-xx-131-part-03]]

5HP Advanced Intercompany Stock Transfer lists [2RP]* among required scope items, but 2RP Electronic Documents is on the Retired Scope Items sheet.

**Status:** open — needs a human decision

## C005 — availability-dependencies-en-xx-131-part-03

Page: [[01-solution-foundation-and-platform/availability-dependencies-en-xx-131-part-03]]

5FM, 5FO, 5FR, 5FS, 5FU, 5FV are provisioned 'Optional (only with SAP Central Business Configuration)' yet show Selectable in Scoping = No, whereas 69L, 69M, 83S, 5RP with the same provisioning show Yes.

**Status:** open — needs a human decision

## C006 — bp-cld-entpr-2608-process-steps-en-xx-135-part-03

Page: [[01-solution-foundation-and-platform/bp-cld-entpr-2608-process-steps-en-xx-135-part-03]]

Venezuela withholding tax and VAT WHT certificate rows (lines 1187, 1193, 1195, 1196) and Korea 'Generate Withholding Tax Reporting' (line 1142) have no app or role and an X in nearly every availability column, while other country-specific 1J2 rows, including the Korea WHT rows at lines 1144-1145, are flagged in a single column; the flag pattern looks inconsistent (column headers are outside this slice).

**Status:** open — needs a human decision

## C007 — bp-cld-entpr-2608-process-steps-en-xx-135-part-08

Page: [[01-solution-foundation-and-platform/bp-cld-entpr-2608-process-steps-en-xx-135-part-08]]

The same app is assigned different business roles across scope items: Execute Billing - Mass Run (F3525) and Execute Invoicing - Mass Run (F3524) use SAP_BR_ADMINISTRATOR in 2BE but SAP_BR_INVOICING_ADMIN_CINV in 2BG; Print Correspondence (F3537) uses SAP_BR_ADMIN_APR_FICA, SAP_BR_ADMINISTRATOR or SAP_BR_INVOICING_ADMIN_CINV depending on scope item.

**Status:** open — needs a human decision

## C008 — bp-cld-entpr-2608-process-steps-en-xx-135-part-12

Page: [[01-solution-foundation-and-platform/bp-cld-entpr-2608-process-steps-en-xx-135-part-12]]

The app 'My Inbox - All Items' is F0862 (object WorkflowTask) in 2WL, 2XT, 2VB, but F5331 (object LegalTask) in 2XU Approve Purchase Order and F6012 for 2XT Approve Central Supplier Confirmation - same title, different app IDs.

**Status:** open — needs a human decision

## C009 — bp-cld-entpr-2608-process-steps-en-xx-135-part-12

Page: [[01-solution-foundation-and-platform/bp-cld-entpr-2608-process-steps-en-xx-135-part-12]]

Billing Clerk role for the same VF01 / J1B3N Brazil steps is 'Billing Clerk (<country>)' SAP_BR_BILLING_CLERK_<country> in 2UV but 'Billing Clerk' SAP_BR_BILLING_CLERK in 2UW.

**Status:** open — needs a human decision

## C010 — bp-cld-entpr-2608-process-steps-en-xx-135-part-15

Page: [[01-solution-foundation-and-platform/bp-cld-entpr-2608-process-steps-en-xx-135-part-15]]

In 3M5 (Event-Based Revenue Recognition - Service Documents - US GAAP) the step 'Manage Revenue Recognition Issues - Service Document' is mapped to Manage Real-Time Revenue Recognition Issues (F4101), whereas the same-named step in 3M3 and 3M4 is mapped to Manage Revenue Recognition Issues - Service Documents (F4186).

**Status:** open — needs a human decision

## C011 — bp-cld-entpr-2608-process-steps-en-xx-135-part-17

Page: [[01-solution-foundation-and-platform/bp-cld-entpr-2608-process-steps-en-xx-135-part-17]]

Scope item 3X2 (Hedge Accounting for FX Option - Local GAAP): scope-level summary rows are flagged for RU, but none of its app-level step rows are flagged for RU (they carry RS instead); in sibling 3X1 the 29-country block includes RU, so RU availability for 3X2 is ambiguous.

**Status:** open — needs a human decision

## C012 — bp-cld-entpr-2608-process-steps-en-xx-135-part-18

Page: [[01-solution-foundation-and-platform/bp-cld-entpr-2608-process-steps-en-xx-135-part-18]]

The same step 'Approve Purchase Order (Optional)' uses My Inbox F0862 (WorkflowTask) with role Sales Manager (SAP_BR_SALES_MANAGER) in scope items 4A1 and 4AH, but F5331 (LegalTask) with Purchasing Manager (SAP_BR_PURCHASING_MANAGER) in 4AI; the approver role for purchase orders is inconsistent across scope items.

**Status:** open — needs a human decision

## C013 — bp-cld-entpr-2608-process-steps-en-xx-135-part-20

Page: [[01-solution-foundation-and-platform/bp-cld-entpr-2608-process-steps-en-xx-135-part-20]]

The step Approve Purchase Order(s) via My Inbox - All Items (F0862) is assigned to Purchasing Manager SAP_BR_PURCHASING_MANAGER in 4R2 but to Internal Sales Representative SAP_BR_INTERNAL_SALES_REP in 54U.

**Status:** open — needs a human decision

## C014 — bp-cld-entpr-2608-process-steps-en-xx-135-part-20

Page: [[01-solution-foundation-and-platform/bp-cld-entpr-2608-process-steps-en-xx-135-part-20]]

4RF converts purchase requisitions with the app labelled Process Purchase Requisitions - Deprecated (F1048), while 4VT, 4WM, 54U and 54V use Process Purchase Requisitions (F1048A).

**Status:** open — needs a human decision

## C015 — bp-cld-entpr-2608-process-steps-en-xx-135-part-21

Page: [[01-solution-foundation-and-platform/bp-cld-entpr-2608-process-steps-en-xx-135-part-21]]

Scope item 5FO Returns to Supplier for Retail: 5 of its 10 steps (e.g. Monitor Returns Purchase Order, Receive Replacement Material, Post Goods Receipt, Check Invoice Document) are blank in availability columns 7 and 61 while the other 5 steps (e.g. Create Returns Purchase Order, Create Outbound Delivery, Pick and Post Goods Issue) are marked there, so a single process is available in a column only for some of its steps; column headers are outside this slice and this may be intentional.

**Status:** open — needs a human decision

## C016 — bp-cld-entpr-2608-process-steps-en-xx-135-part-26

Page: [[01-solution-foundation-and-platform/bp-cld-entpr-2608-process-steps-en-xx-135-part-26]]

Scope item 6GD lists 'Approve Purchase Order (Optional)' with My Inbox - All Items as F0862 (WorkflowTask) in two places but as F5331 (LegalTask) in a third; same app name, different app ID and business object.

**Status:** open — needs a human decision

## C017 — bp-cld-entpr-2608-process-steps-en-xx-135-part-26

Page: [[01-solution-foundation-and-platform/bp-cld-entpr-2608-process-steps-en-xx-135-part-26]]

Scope item 6JN lists 'My Collaborative Projects' as F3145 for most steps but as F5671 for 'Create Project Plan'; same app name under two app IDs.

**Status:** open — needs a human decision

## C018 — bp-cld-entpr-2608-process-steps-en-xx-135-part-29

Page: [[01-solution-foundation-and-platform/bp-cld-entpr-2608-process-steps-en-xx-135-part-29]]

App 'My Inbox - All Items' is listed with ID F0862 (object WorkflowTask) in 7TZ, 7Z2 and 7Z4, but with ID F5331 (object LegalTask) in 7YM and 81Y; worth checking whether these are the same app.

**Status:** open — needs a human decision

## C019 — bp-cld-entpr-2608-process-steps-en-xx-135-part-35

Page: [[01-solution-foundation-and-platform/bp-cld-entpr-2608-process-steps-en-xx-135-part-35]]

In J77 the same step 'Update Bank G/L Account' using Manage G/L Account Master Data (F0731A) is assigned to General Ledger Accountant (SAP_BR_GL_ACCOUNTANT) in some blocks and to Configuration Expert - Business Process Configuration (SAP_BR_BPC_EXPERT) in others.

**Status:** open — needs a human decision

## C020 — data-protection-and-privacy-data-controller-and-purpose-6n9-ae-1180

Page: [[01-solution-foundation-and-platform/data-protection-and-privacy-data-controller-and-purpose-6n9-ae-1180]]

Internal inconsistency: the test step 'Check Purpose Assignments for Application Objects' says purpose PURP01 and data controller DC01 should be displayed for the purchase order, but Table 2 gives PURP02 as the purpose with data category PURCHASEORDER (PURP01 has no data category) and the later business partner check expects PURP02.

**Status:** open — needs a human decision

## C021 — import-connection-setup-with-sap-analytics-cloud-1yb-786

Page: [[01-solution-foundation-and-platform/import-connection-setup-with-sap-analytics-cloud-1yb-786]]

Document describes SAP S/4HANA Cloud Public Edition integration, but the test steps select the datasource 'SAP S/4HANA Cloud Private Edition'.

**Status:** open — needs a human decision

## C022 — s4c-2608-ae-links-1313

Page: [[01-solution-foundation-and-platform/s4c-2608-ae-links-1313]]

Scope item 5I9 and 53V list product assistance URLs that are identical for S.1 and S.2 rows, possible duplicate entries.

**Status:** open — needs a human decision

## C023 — s4c-2608-ae-links-1313

Page: [[01-solution-foundation-and-platform/s4c-2608-ae-links-1313]]

Duplicate set-up instruction URL pattern fragments (e.g. 1N7 and 6BP) look near-identical to other links, may be copy errors.

**Status:** open — needs a human decision

## C024 — sscui-list-en-xx-sap-s-4hana-cloud-2608-configuration-2-part-04

Page: [[01-solution-foundation-and-platform/sscui-list-en-xx-sap-s-4hana-cloud-2608-configuration-2-part-04]]

Configuration Item ID 500428 is used for two different configuration items: 'Disconnection / Reconnection' (Finance, Contract Accounting, lines 876-877) and 'Advanced Payment Management' (Finance, Payments and Bank Communications, lines 878-879).

**Status:** open — needs a human decision

## C025 — sscui-list-en-xx-sap-s-4hana-cloud-2608-configuration-2-part-04

Page: [[01-solution-foundation-and-platform/sscui-list-en-xx-sap-s-4hana-cloud-2608-configuration-2-part-04]]

Configuration Item ID 106891 is used for both 'Payables Financing' (Finance, Accounts Payable, lines 854-855) and 'Dispute Resolution in Collections and Dispute Automation' (line 935).

**Status:** open — needs a human decision

## C026 — sscui-list-en-xx-sap-s-4hana-cloud-2608-configuration-2-part-04

Page: [[01-solution-foundation-and-platform/sscui-list-en-xx-sap-s-4hana-cloud-2608-configuration-2-part-04]]

Line 880 shows availability 'N#A' alongside the approach 'Use Configuration Step in Configure Your Solution', while Additional Information says 'Available only in Central Business Configuration'.

**Status:** open — needs a human decision

## C027 — sscui-list-en-xx-sap-s-4hana-cloud-2608-configuration-2-part-04

Page: [[01-solution-foundation-and-platform/sscui-list-en-xx-sap-s-4hana-cloud-2608-configuration-2-part-04]]

Define Number Range Intervals for Payables Financing Orders (106893, line 855) is classed 'Global' although its country column is restricted to DE, whereas the sibling activity 106892 (line 854) is 'Country/Region Dependent' with DE.

**Status:** open — needs a human decision

## C028 — sscui-list-en-xx-sap-s-4hana-cloud-2608-configuration-2-part-05

Page: [[01-solution-foundation-and-platform/sscui-list-en-xx-sap-s-4hana-cloud-2608-configuration-2-part-05]]

Configuration item ID 500075 is named 'Blocking Reasons' under Sales / Basic Functions but 'Deliveries' under Supply Chain / Delivery Management; ID 500113 is 'Royalties Settlement' under Sales / Royalties Settlement for Sales and 'Sales Rebate Settlement' under Sales / Sales Rebate Management, so item ID to item name is not one-to-one.

**Status:** open — needs a human decision

## C029 — sscui-list-en-xx-sap-s-4hana-cloud-2608-configuration-2-part-05

Page: [[01-solution-foundation-and-platform/sscui-list-en-xx-sap-s-4hana-cloud-2608-configuration-2-part-05]]

The five Sales Billing activities flagged 'Obsolete' (102401, 102358, 102762, 102763, 102764) are still listed with category Optional and availability in Configure Your Solution = Yes; their status may differ from other sections or releases of the list.

**Status:** open — needs a human decision

## C030 — sscui-list-en-xx-sap-s-4hana-cloud-2608-configuration-2-part-06

Page: [[01-solution-foundation-and-platform/sscui-list-en-xx-sap-s-4hana-cloud-2608-configuration-2-part-06]]

Scope tag and country column are used inconsistently: Define Tax on Sales/Purchases Groups (102526) is tagged 'Global' yet lists specific countries (AT,AU,BE,...), its sibling Assign Company Codes to Tax on Sales/Purchases Groups (102521) is 'Country/Region Dependent' with a near-identical list, and Create/Assign Selection Variants (102238) is 'Country/Region Dependent' with country XX.

**Status:** open — needs a human decision

## C031 — sscui-list-en-xx-sap-s-4hana-cloud-2608-configuration-2-part-07

Page: [[01-solution-foundation-and-platform/sscui-list-en-xx-sap-s-4hana-cloud-2608-configuration-2-part-07]]

Configuration Item IDs are reused for different items in this slice: 500199 is both Organization / Organization (Assign company code to company, 101631) and Supply Chain / Warehouse Management / Master Data (Define Warehouse Numbers, 102399); 500013 is both Finance / Accounts Receivable / Automatic Incoming/Outgoing Payment and Accounts Payable / General Payment Settings (Define Terms of Payment for Installment Payments, 102335), while another Accounts Payable / General Payment Settings row uses 500137; 500032 is used for both Contract Accounting Customer Initiated Payments (102551) and…

**Status:** open — needs a human decision

## C032 — sscui-list-en-xx-sap-s-4hana-cloud-2608-configuration-2-part-07

Page: [[01-solution-foundation-and-platform/sscui-list-en-xx-sap-s-4hana-cloud-2608-configuration-2-part-07]]

Item 500400 (Intercompany Matching and Reconciliation) is filed under Application Subarea 'Closing Operations' for activity 103380 but under 'Corporate Close' for activity 103381.

**Status:** open — needs a human decision

## C033 — sscui-list-en-xx-sap-s-4hana-cloud-2608-configuration-2-part-08

Page: [[01-solution-foundation-and-platform/sscui-list-en-xx-sap-s-4hana-cloud-2608-configuration-2-part-08]]

Configuration Item ID is reused for differently named items: 500199 (Contract Accounting > Organization; Supply Chain > Decentralized Warehouse Management System Integration; Organization > Organization), 500486 (Warehouse Management > Cross-Process Settings; Handling Unit Identification), 500008 (R&D/Engineering and Application Platform and Infrastructure > Product Development Foundation), 500012 (Accounts Payable > Automatic Payments; Accounts Receivable > Automatic Incoming/Outgoing Payment), 500281 (Cash Flow Statement; Localization > Cross Country).

**Status:** open — needs a human decision

## C034 — sscui-list-en-xx-sap-s-4hana-cloud-2608-configuration-2-part-08

Page: [[01-solution-foundation-and-platform/sscui-list-en-xx-sap-s-4hana-cloud-2608-configuration-2-part-08]]

Item name 'Decentralized Warehouse Management System Integration' carries Configuration Item ID 500199 on 'Assign Warehouse Number to Plant and Storage Location' but 500074 on 'Consistency Check'.

**Status:** open — needs a human decision

## C035 — sscui-list-en-xx-sap-s-4hana-cloud-2608-configuration-2-part-08

Page: [[01-solution-foundation-and-platform/sscui-list-en-xx-sap-s-4hana-cloud-2608-configuration-2-part-08]]

Country and component disagree on some rows: 'Maintain Number Groups' (101863) is Country/Region Dependent AR but uses activity V_1ANUMGR1_ID and component FI-LOC-FI-ID (Indonesia); 'Use Non-Leading Ledger for Offsetting Account Determination' (101075) is specialized for CN but uses activity J3RKNGLL and component FI-LOC-FI-RU.

**Status:** open — needs a human decision

## C036 — sscui-list-en-xx-sap-s-4hana-cloud-2608-configuration-2-part-09

Page: [[01-solution-foundation-and-platform/sscui-list-en-xx-sap-s-4hana-cloud-2608-configuration-2-part-09]]

Configuration Item ID 570006 is used for two differently named items (Public Sector > Budget Execution > Public Sector Budget Management, and Public Sector > Grants Management > Grants Management), while the item name 'Public Sector Budget Management' carries both 570006 (180094, 180095) and 570004 (180090).

**Status:** open — needs a human decision

## C037 — sscui-list-en-xx-sap-s-4hana-cloud-2608-configuration-2-part-09

Page: [[01-solution-foundation-and-platform/sscui-list-en-xx-sap-s-4hana-cloud-2608-configuration-2-part-09]]

'Maintain Document Classes' (101872) is labelled Localized with 24 specialized countries (AE,AR,BE,DK,EG,ES,FI,HU,ID,IN,IT,NL,NO,OM,PE,PH,PT,RO,SA,SE,TH,TR,TW,VE) but its table V_DOCCLS_IN and component FI-LOC-LO-IN are India-specific.

**Status:** open — needs a human decision

## C038 — sscui-list-en-xx-sap-s-4hana-cloud-2608-configuration-2-part-10

Page: [[01-solution-foundation-and-platform/sscui-list-en-xx-sap-s-4hana-cloud-2608-configuration-2-part-10]]

Configuration Item ID 500110 is used for two differently named items: 'Pricing' (Sales > Price Management, activity 107178) and 'Omnichannel Sales Promotions' (Sales > Basic Functions, activity 107177), while other Omnichannel Sales Promotions rows (107179, 107197) use item ID 500735.

**Status:** open — needs a human decision

## C039 — sscui-list-en-xx-sap-s-4hana-cloud-2608-configuration-2-part-10

Page: [[01-solution-foundation-and-platform/sscui-list-en-xx-sap-s-4hana-cloud-2608-configuration-2-part-10]]

Nine rows are labelled Global in the 'Global, Country Dependent, or Localized' column yet list specific countries in 'Specialized for Certain Countries' (e.g. 106351 Define Tax Box Structure Type, 106490, 106348, 106305, 106347, 106200, 106199, 106429, 106259).

**Status:** open — needs a human decision

## C040 — sscui-list-en-xx-sap-s-4hana-cloud-2608-configuration-2-part-10

Page: [[01-solution-foundation-and-platform/sscui-list-en-xx-sap-s-4hana-cloud-2608-configuration-2-part-10]]

Several Localized rows have scope inconsistent with their country-specific table/component: 'Define Business Places for Indonesia' (106106, FI-LOC-FI-ID) is specialized for 83 country codes; 106517 and 106468 (FI-LOC-FI-QA), 106454 (FI-LOC-FI-EG) and 106353 (FI-LOC-FI-JP) are Localized but specialized for XX.

**Status:** open — needs a human decision

## C041 — sscui-list-en-xx-sap-s-4hana-cloud-2608-configuration-2-part-10

Page: [[01-solution-foundation-and-platform/sscui-list-en-xx-sap-s-4hana-cloud-2608-configuration-2-part-10]]

Configure Matching and Duplicate Check (100274) and Maintain Units of Measurement (102179) are flagged 'Obsolete' in Additional Information yet remain marked available in Configure Your Solution with approach 'Use Configuration Step in Configure Your Solution'.

**Status:** open — needs a human decision

## C042 — sscui-list-en-xx-sap-s-4hana-cloud-2608-configuration-2-part-12

Page: [[01-solution-foundation-and-platform/sscui-list-en-xx-sap-s-4hana-cloud-2608-configuration-2-part-12]]

Some Localized rows list a country that does not match the component or object suffix: SSCUI 101883 lists VE but uses V_T003_B_I_PH and FI-LOC-FI-PH; SSCUI 101991 lists LU but uses FI-LOC-FI-BE.

**Status:** open — needs a human decision

## C043 — sscui-list-en-xx-sap-s-4hana-cloud-2608-configuration-2-part-13

Page: [[01-solution-foundation-and-platform/sscui-list-en-xx-sap-s-4hana-cloud-2608-configuration-2-part-13]]

Group id 500592 is filed under two different parents: 'Real Estate, Facilities, and Equipment > Property and Lease Management > Integration Settings' (e.g. 105392) and 'Finance > Contract and Lease Management > Generic Rental Objects' (105395 Define Total Measurements).

**Status:** open — needs a human decision

## C044 — sscui-list-en-xx-sap-s-4hana-cloud-2608-configuration-2-part-13

Page: [[01-solution-foundation-and-platform/sscui-list-en-xx-sap-s-4hana-cloud-2608-configuration-2-part-13]]

Scope and country columns are inconsistent on some rows: 106646 is 'Localized' with country XX (component FI-LOC-FI-EG), 106637 has an empty scope, and several rows marked 'Global' carry explicit country lists (e.g. 102323, 102814, 103168, 104084).

**Status:** open — needs a human decision

## C045 — sscui-list-en-xx-sap-s-4hana-cloud-2608-configuration-2-part-14

Page: [[01-solution-foundation-and-platform/sscui-list-en-xx-sap-s-4hana-cloud-2608-configuration-2-part-14]]

Country scope looks inconsistent for localized rows: Define Business Places for Philippines (105727, Localized, PH-specific table OFFDOCNO_PH_01) and Define Settings for CU Reporting (101307, IT_WTX_MODELLO770) list about 90 countries, while the Thailand (TH) and South Korea (KR) business place rows list only their own country.

**Status:** open — needs a human decision

## C046 — sscui-list-en-xx-sap-s-4hana-cloud-2608-configuration-2-part-15

Page: [[01-solution-foundation-and-platform/sscui-list-en-xx-sap-s-4hana-cloud-2608-configuration-2-part-15]]

Configuration Item ID 500417 is used for two different items: Logistics > Handling Unit Management > General Settings (Specify Unit of Measure for Packing Consistency Check, 105741) and Supply Chain > Warehouse Management > Cross-Process Settings (Define Material Group for Packaging Materials, 103927, component LO-HU), while 'Cross-Process Settings' elsewhere carries ID 500511.

**Status:** open — needs a human decision

## C047 — sscui-list-en-xx-sap-s-4hana-cloud-2608-configuration-2-part-15

Page: [[01-solution-foundation-and-platform/sscui-list-en-xx-sap-s-4hana-cloud-2608-configuration-2-part-15]]

'Define Turnover Types' (104250, table V_J_3RM_TURNTYP, component FI-LOC-LO-RU) is Country/Region Dependent with a list of 83 countries, whereas sibling Russia-localization rows (104251, 104252) list only KZ,RU,UA,VN.

**Status:** open — needs a human decision

## C048 — sscui-list-en-xx-sap-s-4hana-cloud-2608-configuration-2-part-15

Page: [[01-solution-foundation-and-platform/sscui-list-en-xx-sap-s-4hana-cloud-2608-configuration-2-part-15]]

'Maintain Profile For POS Outbound' (104673) sits under Store Connectivity > POS Outbound but carries component LO-RFM-IFC-IN, while other POS Outbound rows (105576, 105594) use LO-RFM-IFC-OUT.

**Status:** open — needs a human decision

## C049 — sscui-list-en-xx-sap-s-4hana-cloud-2608-configuration-2-part-35

Page: [[01-solution-foundation-and-platform/sscui-list-en-xx-sap-s-4hana-cloud-2608-configuration-2-part-35]]

Transaction code S_ALR_87000248_2 maps to 'Define Priorities' (SIMG_CFMENUOLIAOIO1, SSCUI 102583) under Plant Maintenance General Setting but to 'Define Priority Types for Notifications' (CFMENUOLQNOQNM2_1, SSCUI 105528) under Quality Management.

**Status:** open — needs a human decision

## C050 — sscui-list-en-xx-sap-s-4hana-cloud-2608-configuration-2-part-37

Page: [[01-solution-foundation-and-platform/sscui-list-en-xx-sap-s-4hana-cloud-2608-configuration-2-part-37]]

Numeric ID 100297 is attached to three different activities: 'Automatic Account Determination' (FAC_ACC_DET_SSCUI, FI-GL), 'Define Retained Earnings Account' (OB53) and 'Assign G/L Accounts' (VKOA, SD-SLS).

**Status:** open — needs a human decision

## C051 — test-script-automated-provisioning-via-sap-cloud-identity-access-gover

Page: [[01-solution-foundation-and-platform/test-script-automated-provisioning-via-sap-cloud-identity-access-gover]]

App naming inconsistency inside the document: Employee Recruitment > View Employee Basic Data step 'Go to the Manage Workforce' says to open 'Manage Service Level Agreements (F6183A)', while the Overview Table lists 'Manage Workforce' and the JB1 section names 'Manage Workforce (F6097A)'.

**Status:** open — needs a human decision

## C052 — test-script-exception-based-core-hr-with-sap-successfactors-employee-c

Page: [[01-solution-foundation-and-platform/test-script-exception-based-core-hr-with-sap-successfactors-employee-c]]

View Bank Data purpose says only initial replication of bank master data is supported yet also says there are editable fields in S/4HANA Cloud for which replication would replicate value changes; the sibling legal entity section says there are no such editable fields.

**Status:** open — needs a human decision

## C053 — test-script-exception-based-core-hr-with-sap-successfactors-employee-c

Page: [[01-solution-foundation-and-platform/test-script-exception-based-core-hr-with-sap-successfactors-employee-c]]

Payment method values differ between sections: View Employee Basic Data expects Payment Methods T (bank transfer) or C (bank check), while View Payment Information expects I (ISO PAIN001: Credit Transfer).

**Status:** open — needs a human decision

## C054 — test-script-exception-based-core-hr-with-sap-successfactors-employee-c

Page: [[01-solution-foundation-and-platform/test-script-exception-based-core-hr-with-sap-successfactors-employee-c]]

Hire New Contingent Worker is assigned to role HR Manager in the Overview Table, but its procedure step 1 says to log on to Employee Central as an Administrator - HR Info.

**Status:** open — needs a human decision

## C055 — test-script-integration-to-icertis-for-contract-assembly-6v2-sap-s-4ha

Page: [[01-solution-foundation-and-platform/test-script-integration-to-icertis-for-contract-assembly-6v2-sap-s-4ha]]

The Overview Table lists only Create Legal Documents and Manage Legal Documents, while the table of contents and Test Procedure also include a third process step, Send Legal Document for Signature.

**Status:** open — needs a human decision

## C056 — test-script-integration-with-sap-document-ai-7tc-1225

Page: [[01-solution-foundation-and-platform/test-script-integration-with-sap-document-ai-7tc-1225]]

Purpose text refers to the 'Manage Document AI Workspace' app while the test case and app are named Manage Document AI Schema Registration Subscriptions (F8996)

**Status:** open — needs a human decision

## C057 — test-script-sap-archiving-and-document-access-core-by-opentext-integra

Page: [[01-solution-foundation-and-platform/test-script-sap-archiving-and-document-access-core-by-opentext-integra]]

Near-identical to the 7XY test script; differs only in the integration (OpenText vs SAP Document Management service) and set-up link.

**Status:** open — needs a human decision

## C058 — test-script-sap-document-management-service-integration-7xy-1234

Page: [[01-solution-foundation-and-platform/test-script-sap-document-management-service-integration-7xy-1234]]

Near-identical to the 7W6 OpenText test script; differs only in the integration and set-up link.

**Status:** open — needs a human decision

## C059 — test-script-sap-s-4hana-cloud-public-edition-sap-s-4hana-for-enterpris

Page: [[01-solution-foundation-and-platform/test-script-sap-s-4hana-cloud-public-edition-sap-s-4hana-for-enterpris]]

The same app, My Inbox - All Items, is given as F5331 in the Overview Table but as F0862 in the Approve Legal Transactions procedure.

**Status:** open — needs a human decision

## C060 — 2608-master-data-overview-en-xx-120-part-01

Page: [[02-business-partner-and-product-master-data/2608-master-data-overview-en-xx-120-part-01]]

Material ID RM30 is listed twice in the sLog OP raw materials block with different attributes: 'RAW30, VB, FIFO Charge' (MRP type PD, base unit PC) and 'RAW30,VB,Batch-Fifo' (MRP type VB, base unit L).

**Status:** open — needs a human decision

## C061 — 2608-master-data-overview-en-xx-120-part-02

Page: [[02-business-partner-and-product-master-data/2608-master-data-overview-en-xx-120-part-02]]

ID SRV_03 appears twice with different definitions: 'Spare Part Service Product' (material type NLAG) and 'Spare Part' (material type SERV).

**Status:** open — needs a human decision

## C062 — 2608-master-data-overview-en-xx-120-part-02

Page: [[02-business-partner-and-product-master-data/2608-master-data-overview-en-xx-120-part-02]]

Several rows use material types SEMI and RAW (e.g. S-201, R-302) although the Intro material type list shows HALB/ROH; some IDs also deviate from the Intro naming convention (VERP materials such as PMPALLET instead of PK prefix, SM0001 for SERV instead of SV).

**Status:** open — needs a human decision

## C063 — 2608-master-data-overview-en-xx-120-part-04

Page: [[02-business-partner-and-product-master-data/2608-master-data-overview-en-xx-120-part-04]]

Work Centers sheet, row WORK ('Work for machine / Person'): capacity-category column shows 0008 (Cap 001/002) while the Work Center Category column shows 0001, unlike other rows where the two agree.

**Status:** open — needs a human decision

## C064 — anwendungsgruppe-und-merkmalsanzeige-anlegen-sds-2ni-268

Page: [[02-business-partner-and-product-master-data/anwendungsgruppe-und-merkmalsanzeige-anlegen-sds-2ni-268]]

The overview table gives the same expected result (Anwendungsgruppe wird angelegt) for both steps, and the text cites edition 1711 although the document is release 2608; possibly outdated wording.

**Status:** open — needs a human decision

## C065 — create-application-group-and-characteristic-display-mds-2ni-269

Page: [[02-business-partner-and-product-master-data/create-application-group-and-characteristic-display-mds-2ni-269]]

Text says only Sales and Distribution Document is supported (1711 edition) yet lists other transaction types; the overview table gives the same 'Application Group is created' result for both steps

**Status:** open — needs a human decision

## C066 — master-data-script-create-product-master-of-type-configurable-material

Page: [[02-business-partner-and-product-master-data/master-data-script-create-product-master-of-type-configurable-material]]

Costing step 3 carries a stray 'Field is not available.' comment in the result column, which is unclear

**Status:** open — needs a human decision

## C067 — master-data-script-create-product-master-of-type-configurable-material

Page: [[02-business-partner-and-product-master-data/master-data-script-create-product-master-of-type-configurable-material]]

Sales/Basic Data steps reference Plant 1010 in purchasing but 1710 elsewhere (example values only)

**Status:** open — needs a human decision

## C068 — master-data-script-create-product-master-of-type-finished-good-sap-s-4

Page: [[02-business-partner-and-product-master-data/master-data-script-create-product-master-of-type-finished-good-sap-s-4]]

Repetitive manufacturing Option 1 step 4 expects a 'Trading Goods' screen although the script is for Finished Good (FERT)

**Status:** open — needs a human decision

## C069 — master-data-script-create-product-master-of-type-finished-good-sap-s-4

Page: [[02-business-partner-and-product-master-data/master-data-script-create-product-master-of-type-finished-good-sap-s-4]]

Create Product Master Data - Basic Data step 3 text differs slightly from other chapters on hidden Industry Sector field (greyed out vs garbled wording)

**Status:** open — needs a human decision

## C070 — master-data-script-create-product-master-of-type-raw-material-mds-bnr

Page: [[02-business-partner-and-product-master-data/master-data-script-create-product-master-of-type-raw-material-mds-bnr]]

Mandatory/optional master data table is empty (placeholder rows only); Plant Sales section step numbering skips step 7; Create Material app step is hidden in some roles (Industry Sector field may be hidden)

**Status:** open — needs a human decision

## C071 — master-data-script-create-product-master-of-type-semi-finished-good-md

Page: [[02-business-partner-and-product-master-data/master-data-script-create-product-master-of-type-semi-finished-good-md]]

Some steps in plant sales and repetitive manufacturing procedures mention 'Trading Goods' screens and the attachment procedure mentions 'Finished Product' although material type is HALB; wording inconsistent inside the script.

**Status:** open — needs a human decision

## C072 — master-data-script-create-product-master-of-type-trading-good-mds-bnf

Page: [[02-business-partner-and-product-master-data/master-data-script-create-product-master-of-type-trading-good-mds-bnf]]

Sales Data row in the organizational units table lists Plant, Sales Org., Distribution Channel, while Option 2 steps use Distribution Chains tab without plant; minor wording inconsistency only

**Status:** open — needs a human decision

## C073 — master-data-script-create-supplier-master-mds-bne-sap-s-4hana-cloud-pu

Page: [[02-business-partner-and-product-master-data/master-data-script-create-supplier-master-mds-bne-sap-s-4hana-cloud-pu]]

Reconciliation account text says to enter the G/L account from the AR sub ledger for a supplier (payables expected), and FLVN01 is said to be used in Sales rather than Purchasing; internally inconsistent wording.

**Status:** open — needs a human decision

## C074 — mds-2j7-265

Page: [[02-business-partner-and-product-master-data/mds-2j7-265]]

External alphanumeric material ID length limited to 8 here, whereas the Chinese sibling script (65B) says up to 40 characters.

**Status:** open — needs a human decision

## C075 — mds-2j7-267

Page: [[02-business-partner-and-product-master-data/mds-2j7-267]]

Maximum external alphanumeric material identifier length is given as 8 characters here, but as 40 characters in the service-product script (31X); one may be inaccurate.

**Status:** open — needs a human decision

## C076 — mds-2ni-271

Page: [[02-business-partner-and-product-master-data/mds-2ni-271]]

1711-edition limitation (only sales documents supported) is stated in a 2608 document alongside other transactions; may be outdated

**Status:** open — needs a human decision

## C077 — mds-2ni-273

Page: [[02-business-partner-and-product-master-data/mds-2ni-273]]

事务表称仅销售和分销凭证支持（1711 版本），但同表列出多种事务，可能与 2608 版现状不符

**Status:** open — needs a human decision

## C078 — mds-31x-309

Page: [[02-business-partner-and-product-master-data/mds-31x-309]]

Maximum external alphanumeric material identifier length is given as 40 characters here, but as 8 characters in the spare-parts script (2J7); one may be inaccurate.

**Status:** open — needs a human decision

## C079 — mds-65b-501

Page: [[02-business-partner-and-product-master-data/mds-65b-501]]

External alphanumeric material ID length limit stated as 40 characters here, but the Japanese sibling script (2J7) states not longer than 8 characters.

**Status:** open — needs a human decision

## C080 — script-de-dados-mestre-criar-grupo-de-aplicacao-e-exibicao-de-caracter

Page: [[02-business-partner-and-product-master-data/script-de-dados-mestre-criar-grupo-de-aplicacao-e-exibicao-de-caracter]]

Overview table gives the same expected result ('application group is created') for both create application group and create characteristic display; the 1711-only restriction may be outdated in a 2608 document.

**Status:** open — needs a human decision

## C081 — script-de-dados-mestre-criar-mestre-de-fornecedores-mds-bne-590

Page: [[02-business-partner-and-product-master-data/script-de-dados-mestre-criar-mestre-de-fornecedores-mds-bne-590]]

Note refers to Brazil nota fiscal JD0 'for customer master data' and the option 2 headings say 'Administrar dados mestre de cliente' although the content concerns suppliers; FLVN01 is described as used in 'sales' rather than purchasing.

**Status:** open — needs a human decision

## C082 — script-de-dados-mestre-criar-mestre-de-produtos-do-tipo-materia-prima

Page: [[02-business-partner-and-product-master-data/script-de-dados-mestre-criar-mestre-de-produtos-do-tipo-materia-prima]]

Internal inconsistencies: step numbering skips 7 in the plant sales Option 1 table; the mandatory/optional master data table is empty; the storage data row text refers to 'registro mestre de cliente' instead of material.

**Status:** open — needs a human decision

## C083 — script-de-dados-mestre-criar-mestre-de-produtos-do-tipo-material-confi

Page: [[02-business-partner-and-product-master-data/script-de-dados-mestre-criar-mestre-de-produtos-do-tipo-material-confi]]

Extracted title was 'Objetivo' (first H1), real title is on the cover table

**Status:** open — needs a human decision

## C084 — script-de-dados-mestre-criar-mestre-de-produtos-do-tipo-material-confi

Page: [[02-business-partner-and-product-master-data/script-de-dados-mestre-criar-mestre-de-produtos-do-tipo-material-confi]]

Test steps are examples (plant 1710, profit centers YB110/YB111) and may differ from customer configuration

**Status:** open — needs a human decision

## C085 — script-de-dados-mestre-criar-mestre-de-produtos-do-tipo-produto-acabad

Page: [[02-business-partner-and-product-master-data/script-de-dados-mestre-criar-mestre-de-produtos-do-tipo-produto-acabad]]

Extracted title 'Objetivo' is only the first heading; real title is the cover 'Script de dados mestre'. Steps differ slightly between sections on whether the 'sem entrada' industry-sector field is 'no escuro' vs 'esmaecido' (translation inconsistency).

**Status:** open — needs a human decision

## C086 — script-de-dados-mestre-criar-mestre-de-produtos-do-tipo-produto-comerc

Page: [[02-business-partner-and-product-master-data/script-de-dados-mestre-criar-mestre-de-produtos-do-tipo-produto-comerc]]

Document title in extraction is 'Objetivo'; real title is the cover line. Setor industrial M in MM01 steps vs example sector 00 in F1602 step, a minor inconsistency in examples.

**Status:** open — needs a human decision

## C087 — script-de-dados-mestre-criar-mestre-de-produtos-do-tipo-produto-semiac

Page: [[02-business-partner-and-product-master-data/script-de-dados-mestre-criar-mestre-de-produtos-do-tipo-produto-semiac]]

Document title in metadata is 'Objetivo' while the cover title is the master data script; the step sections contain template placeholders (<X.XX>) and some typos (e.g. 'Material (produto acabado)' used for HALB semi-finished product).

**Status:** open — needs a human decision

## C088 — script-de-datos-maestros-creacion-de-maestro-de-productos-de-tipo-mate

Page: [[02-business-partner-and-product-master-data/script-de-datos-maestros-creacion-de-maestro-de-productos-de-tipo-mate-2]]

Machine-translated Spanish text, unreviewed; terminology may differ from other-language versions of the same script.

**Status:** open — needs a human decision

## C089 — script-de-datos-maestros-creacion-de-maestro-de-productos-de-tipo-mate

Page: [[02-business-partner-and-product-master-data/script-de-datos-maestros-creacion-de-maestro-de-productos-de-tipo-mate-2]]

Plant sales and repetitive manufacturing Option 1 tables skip a step number (7) and some fields are blank; table of mandatory/optional master data objects is empty.

**Status:** open — needs a human decision

## C090 — script-de-datos-maestros-creacion-de-maestro-de-productos-de-tipo-mate

Page: [[02-business-partner-and-product-master-data/script-de-datos-maestros-creacion-de-maestro-de-productos-de-tipo-mate-3]]

Text is machine-translated and may contain errors (e.g. 'Categoría de valoración' used for valuation class); 'Ramo' vs 'Sector' terminology varies.

**Status:** open — needs a human decision

## C091 — script-de-datos-maestros-creacion-de-maestro-de-productos-de-tipo-mate

Page: [[02-business-partner-and-product-master-data/script-de-datos-maestros-creacion-de-maestro-de-productos-de-tipo-mate-3]]

Procedure steps assume MM01 exists, while it is described in Fiori; some Brazil tax/field details refer to other scope items.

**Status:** open — needs a human decision

## C092 — script-de-datos-maestros-creacion-de-maestro-de-productos-de-tipo-prod

Page: [[02-business-partner-and-product-master-data/script-de-datos-maestros-creacion-de-maestro-de-productos-de-tipo-prod-2]]

Machine-translated text has errors (e.g. 'Pos también', 'En la oscuridad' for dimmed/greyed out field); some steps say field is filled/dimmed inconsistently

**Status:** open — needs a human decision

## C093 — script-de-datos-maestros-creacion-de-maestro-de-productos-de-tipo-prod

Page: [[02-business-partner-and-product-master-data/script-de-datos-maestros-creacion-de-maestro-de-productos-de-tipo-prod-2]]

Document title in batch metadata is 'Objetivo' (a heading), real title taken from cover

**Status:** open — needs a human decision

## C094 — script-de-datos-maestros-creacion-de-maestro-de-productos-de-tipo-prod

Page: [[02-business-partner-and-product-master-data/script-de-datos-maestros-creacion-de-maestro-de-productos-de-tipo-prod]]

Machine-translated Spanish text with some garbled phrases (e.g. 'En la oscuridad' for 'dark/blank'); sections 4.6/4.7 mention 'producto terminado' despite semi-finished scope; sample valuation class differs between options (7900 vs 3100).

**Status:** open — needs a human decision

## C095 — script-de-datos-maestros-crear-maestro-de-productos-de-tipo-mercaderia

Page: [[02-business-partner-and-product-master-data/script-de-datos-maestros-crear-maestro-de-productos-de-tipo-mercaderia]]

Machine-translated and unreviewed; terminology may differ from other SAP documents or the English original

**Status:** open — needs a human decision

## C096 — script-de-datos-maestros-crear-maestro-de-productos-de-tipo-mercaderia

Page: [[02-business-partner-and-product-master-data/script-de-datos-maestros-crear-maestro-de-productos-de-tipo-mercaderia]]

Document title extracted as 'Objetivo' (first heading) rather than real title

**Status:** open — needs a human decision

## C097 — set-up-configurable-model-using-variant-configuration-22t-ae-test-scri

Page: [[02-business-partner-and-product-master-data/set-up-configurable-model-using-variant-configuration-22t-ae-test-scri]]

Preliminary step 'Assign Routing for CM-FL-V01' enters Material CM-MLFL-KM-VXX on the Change Routing initial screen, while its purpose and later steps concern CM-FL-V01; the material may be mismatched.

**Status:** open — needs a human decision

## C098 — stammdatenskript-produktstamm-fur-materialart-konfigurierbares-materia

Page: [[02-business-partner-and-product-master-data/stammdatenskript-produktstamm-fur-materialart-konfigurierbares-materia]]

Brazil-specific tax fields are required for correct tax calculation (refers to Nota Fiscal JD0), not detailed here

**Status:** open — needs a human decision

## C099 — stammdatenskript-produktstamm-fur-materialart-konfigurierbares-materia

Page: [[02-business-partner-and-product-master-data/stammdatenskript-produktstamm-fur-materialart-konfigurierbares-materia]]

Sample plant values vary between sections (purchasing uses plant 1010, others 1710), possibly inconsistent example data

**Status:** open — needs a human decision

## C100 — stammdatenskript-produktstamm-vom-typ-halbfabrikat-anlegen-sds-bns-664

Page: [[02-business-partner-and-product-master-data/stammdatenskript-produktstamm-vom-typ-halbfabrikat-anlegen-sds-bns-664]]

Section titles for plant sales and repetitive manufacturing steps mention material types Handelswaren/Fertigerzeugnis in screen names although material type HALB is used; the Werksverkauf and Serienfertigung overview rows have empty expected results.

**Status:** open — needs a human decision

## C101 — stammdatenskript-produktstamm-vom-typ-handelsware-anlegen-sds-bnf-592

Page: [[02-business-partner-and-product-master-data/stammdatenskript-produktstamm-vom-typ-handelsware-anlegen-sds-bnf-592]]

Section titles say Handelsware but some steps reference Fertigerzeugnis screens (configurable product, attachments); Option 1 sections also use Materialart Handelsware throughout.

**Status:** open — needs a human decision

## C102 — stammdatenskript-produktstamm-vom-typ-handelsware-anlegen-sds-bnf-592

Page: [[02-business-partner-and-product-master-data/stammdatenskript-produktstamm-vom-typ-handelsware-anlegen-sds-bnf-592]]

Last two sections (Werksverkauf, Serienfertigung) have empty expected results in the overview table.

**Status:** open — needs a human decision

## C103 — stammdatenskript-produktstamm-vom-typ-rohstoff-anlegen-sds-bnr-658

Page: [[02-business-partner-and-product-master-data/stammdatenskript-produktstamm-vom-typ-rohstoff-anlegen-sds-bnr-658]]

Table of mandatory/optional master data objects is empty in extraction; the purchasing data row lists dependency on Werk while the comment mentions purchasing organization; step 7 is missing in the plant-sales Option 1 table (numbering jumps 6 to 8). Likely overlaps with other language versions/variants of the same master data script.

**Status:** open — needs a human decision

## C104 — stammdatenskript-sap-s-4hana-cloud-public-edition-lieferantenstamm-anl

Page: [[02-business-partner-and-product-master-data/stammdatenskript-sap-s-4hana-cloud-public-edition-lieferantenstamm-anl]]

Text says FLVN01 (supplier with purchasing data) is used in 'Verkauf' (sales), which seems inconsistent with its purchasing use elsewhere in the document.

**Status:** open — needs a human decision

## C105 — stammdatenskript-sap-s-4hana-cloud-public-edition-lieferantenstamm-anl

Page: [[02-business-partner-and-product-master-data/stammdatenskript-sap-s-4hana-cloud-public-edition-lieferantenstamm-anl]]

Reconciliation account is described as a G/L account from the 'Debitorennebenbuch' (customer subledger) although it is for suppliers (21100000 Verbindlichkeiten Inland).

**Status:** open — needs a human decision

## C106 — stammdatenskript-sap-s-4hana-cloud-public-edition-produktstamm-vom-typ

Page: [[02-business-partner-and-product-master-data/stammdatenskript-sap-s-4hana-cloud-public-edition-produktstamm-vom-typ]]

Basic data steps contradict slightly on missing industry field handling (one says 'nicht bekannt', others 'ausgegraut')

**Status:** open — needs a human decision

## C107 — stammdatenskript-sap-s-4hana-cloud-public-edition-produktstamm-vom-typ

Page: [[02-business-partner-and-product-master-data/stammdatenskript-sap-s-4hana-cloud-public-edition-produktstamm-vom-typ]]

Last two sections (Werksverkauf, Werk/Serienfertigung) leave expected results empty in the overview table and use 'Handelswaren' screen title despite FERT

**Status:** open — needs a human decision

## C108 — stammdatenskript-sap-s-4hana-cloud-public-edition-produktstamm-vom-typ

Page: [[02-business-partner-and-product-master-data/stammdatenskript-sap-s-4hana-cloud-public-edition-produktstamm-vom-typ]]

Tax classification text for Brazil/US is ambiguous in step listing (Steuerklassifikation listed twice)

**Status:** open — needs a human decision

## C109 — test-script-central-governance-for-product-1n5-sap-s-4hana-cloud-publi

Page: [[02-business-partner-and-product-master-data/test-script-central-governance-for-product-1n5-sap-s-4hana-cloud-publi]]

App naming differs inside the document: the Overview Table lists Manage Mass Processes - Products (F8321) for the mass-processing steps, but the Create Process and Derivation procedures instruct opening Manage Governance Processes - Products (F8466).

**Status:** open — needs a human decision

## C110 — 2508-journal-entry-template-xxxx-pu1010-98

Page: [[03-financial-accounting-and-close/2508-journal-entry-template-xxxx-pu1010-98]]

G/L account 12550000 is labelled 'Unbilled Revenue' in batches 1-5 but 'Allowance for Doubtful Receivables' in batch 8, while batch 7 uses 12401100 for the same label.

**Status:** open — needs a human decision

## C111 — advanced-credit-management-1qm-ae-test-script-sap-s-4hana-cloud-public

Page: [[03-financial-accounting-and-close/advanced-credit-management-1qm-ae-test-script-sap-s-4hana-cloud-public]]

Test data is inconsistent within the script: credit master data is set up only for customer 33100011 (company code 3310), but the service order and service contract prerequisites name customer 10100011, and the Reject step searches business partner 33100005, neither of which is created in this script.

**Status:** open — needs a human decision

## C112 — asset-under-construction-additional-depreciation-area-5kf-ae-test-scri

Page: [[03-financial-accounting-and-close/asset-under-construction-additional-depreciation-area-5kf-ae-test-scri]]

Takeover date section says the date is usually the prior year-end, yet its example says fiscal year 2025 implies loading legacy assets as of year end 2023 (prior year-end would be 2024).

**Status:** open — needs a human decision

## C113 — bp-cld-entpr-2608-account-master-data-for-ycoa-132-part-01

Page: [[03-financial-accounting-and-close/bp-cld-entpr-2608-account-master-data-for-ycoa-132-part-01]]

Some 'Account Purpose' notes name fewer countries than the X-matrix marks: 12609000 says only FR, HU but is marked for AT, FR, HU, IT, KR, MX, RO, RU, TH; 12610100 says only BE, LU but is also marked for DK, FI, NO, SE; 21501100 says only BE, LU but is marked for BE, IT, NO, RU, SE; 12606000 and 22006011 say only CN but are also marked for RU; 21613000 says only MY, PH but is also marked for IT, TH, VE.

**Status:** open — needs a human decision

## C114 — bp-cld-entpr-2608-account-master-data-for-ycoa-132-part-01

Page: [[03-financial-accounting-and-close/bp-cld-entpr-2608-account-master-data-for-ycoa-132-part-01]]

22005900 GST/HST Self-Assess (CA) and 22005910 PST Self-Assess (CA) are described as 'Tax account only used in the country BR' but are named (CA) and marked only in the CA (2910) column.

**Status:** open — needs a human decision

## C115 — bp-cld-entpr-2608-account-master-data-for-ycoa-132-part-02

Page: [[03-financial-accounting-and-close/bp-cld-entpr-2608-account-master-data-for-ycoa-132-part-02]]

61022030 is named 'Long Service Leave (CN)' but its description says 'Account only used in the country AU' - country scope disagrees between name and description.

**Status:** open — needs a human decision

## C116 — bp-cld-entpr-2608-account-master-data-for-ycoa-132-part-02

Page: [[03-financial-accounting-and-close/bp-cld-entpr-2608-account-master-data-for-ycoa-132-part-02]]

22140000 Output Tax (ICZ) is described as 'Tax account used in tax code settings' with Tax account determination (2BA), yet its financial statement hierarchy is 'ACCOUNTS NOT IN USE'.

**Status:** open — needs a human decision

## C117 — bp-cld-entpr-2608-account-master-data-for-ycoa-132-part-02

Page: [[03-financial-accounting-and-close/bp-cld-entpr-2608-account-master-data-for-ycoa-132-part-02]]

Some descriptions do not match the account they sit on, so the stated purpose is unreliable for these rows: 24031000 Pension Provision is described as 'Provision for Tax'; 52053000 Loss Consumption of Consign. Mat (SF & F.Goods) as 'loss from freight differences'; 52070500 and 52570500 (Inventory Value Adjustment Own Prod.) as 'external products'.

**Status:** open — needs a human decision

## C118 — bp-cld-entpr-2608-account-master-data-for-ycoa-132-part-03

Page: [[03-financial-accounting-and-close/bp-cld-entpr-2608-account-master-data-for-ycoa-132-part-03]]

94310000 QM Control carries the note 'Mapped in cost component structure but not used functionally' yet is classed SECONDARY ACCOUNTS | INTERNAL ACTIVITY ALLOCATION, unlike sibling accounts 94304000-94307000 and 94309000 with the same note, which are classed ACCOUNTS NOT IN USE.

**Status:** open — needs a human decision

## C119 — bp-cld-entpr-2608-account-master-data-for-ycoa-132-part-03

Page: [[03-financial-accounting-and-close/bp-cld-entpr-2608-account-master-data-for-ycoa-132-part-03]]

21191100 and 21191200 (contract liability for down payments) are classified under CURRENT LIABILITIES but with sub-level 'Residual maturity > 5 years'.

**Status:** open — needs a human decision

## C120 — bp-cld-entpr-2608-account-master-data-for-ycoa-132-part-04

Page: [[03-financial-accounting-and-close/bp-cld-entpr-2608-account-master-data-for-ycoa-132-part-04]]

T030H maps 11002045 (Bank 2 - Returns) to balance-sheet adjustment account 11001099 (a Bank 1 account) whereas every other Bank 2 sub-account maps to 11002099.

**Status:** open — needs a human decision

## C121 — bp-cld-entpr-2608-account-master-data-for-ycoa-132-part-04

Page: [[03-financial-accounting-and-close/bp-cld-entpr-2608-account-master-data-for-ycoa-132-part-04]]

Acct Structure Overview places liability-type tax accounts (22000000 Output Tax (MWS), 22090000 Withholding Tax Payable, 22100000 Acquisition Tax) under ASSETS > CURRENT ASSETS > ASSETS FOR CURRENT TAXES, and labels equity groups with the path 'EQUITY | CURRENT ASSETS'; T030K uses 22000000 and 22100000 for output and acquisition tax postings.

**Status:** open — needs a human decision

## C122 — bp-cld-entpr-2608-account-master-data-for-ycoa-132-part-06

Page: [[03-financial-accounting-and-close/bp-cld-entpr-2608-account-master-data-for-ycoa-132-part-06]]

T030 rows use valuation classes 3030 and 3031 (e.g. BSX, GBB, PRD, EIN, EKG) but these classes are not listed on the Valuation Classes sheet.

**Status:** open — needs a human decision

## C123 — bp-cld-entpr-2608-account-master-data-for-ycoa-132-part-06

Page: [[03-financial-accounting-and-close/bp-cld-entpr-2608-account-master-data-for-ycoa-132-part-06]]

Transactions I says WRY is not used from Release 4.0 onwards, yet T030 still carries a WRY row (GR/IR clearing acct (mat. ledger) (old) -> 21121000).

**Status:** open — needs a human decision

## C124 — government-budget-management-6yu-test-script-sap-s-4hana-cloud-public

Page: [[03-financial-accounting-and-close/government-budget-management-6yu-test-script-sap-s-4hana-cloud-public]]

Create Revenue Posting (Actuals): the Overview Table assigns business role Accounts Payable / Central Invoice Management - Supplier Invoices / Central Invoicing - Supplier Invoice, but the procedure logs on as an Accounts Receivable Accountant (and refers to Accounts Receivable J59).

**Status:** open — needs a human decision

## C125 — integration-of-payment-advice-with-buyers-and-suppliers-2mb-ae-test-sc

Page: [[03-financial-accounting-and-close/integration-of-payment-advice-with-buyers-and-suppliers-2mb-ae-test-sc]]

Receive Payment Advice step uses company code 1710 for the receiver system, while other steps use company code 3310; the Delete Payment Advice step checks company code 3310 for receiver entries.

**Status:** open — needs a human decision

## C126 — intercompany-billing-for-cross-company-cost-accounting-postings-4an-ae

Page: [[03-financial-accounting-and-close/intercompany-billing-for-cross-company-cost-accounting-postings-4an-ae]]

Financial Posting note describes FI document types W1/W2/W3 for Italy/EU/non-EU destinations (Italian localisation), which does not fit the DE/US-only scenario described elsewhere in the same document.

**Status:** open — needs a human decision

## C127 — lease-out-for-sublease-accounting-group-ledger-ifrs-2sa-ae-858

Page: [[03-financial-accounting-and-close/lease-out-for-sublease-accounting-group-ledger-ifrs-2sa-ae-858]]

Overview Table lists Accounts Payable Accountant - Leasing for periodic posting, reverse contract postings and several accounting reports, while the test procedures and Roles table use Accounts Receivable Accountant - Leasing (no Accounts Payable role is defined in Roles).

**Status:** open — needs a human decision

## C128 — mds-bni-613

Page: [[03-financial-accounting-and-close/mds-bni-613]]

Asset class 3100 (vehicles) number range 50000000-59999999 and 3300 sharing 30000000-39999999 with 3000 may differ from other country versions of this script; 8300/9000 ranges use dot notation

**Status:** open — needs a human decision

## C129 — payroll-processing-with-sap-successfactors-employee-central-payroll-1n

Page: [[03-financial-accounting-and-close/payroll-processing-with-sap-successfactors-employee-central-payroll-1n]]

Portugal withholding tax return prerequisites refer to the company code for Spain, apparently copied from the Spain section

**Status:** open — needs a human decision

## C130 — psm-preparation-guide-254

Page: [[03-financial-accounting-and-close/psm-preparation-guide-254]]

Guide is labelled release 2402 (January 2024) although it sits in the 2608 best-practices bundle; may be outdated versus 2608 content.

**Status:** open — needs a human decision

## C131 — psm-preparation-guide-254

Page: [[03-financial-accounting-and-close/psm-preparation-guide-254]]

Section on skipping J54 Commitment Management and Cost Center Budgeting lists project-budget/WBS items (project budget, availability control profile, WBS master data), apparently copied from the project section.

**Status:** open — needs a human decision

## C132 — test-script-advanced-payment-management-4mt-sap-s-4hana-cloud-public-e

Page: [[03-financial-accounting-and-close/test-script-advanced-payment-management-4mt-sap-s-4hana-cloud-public-e]]

The Purpose note says 2DP Contract Accounting integration supports DE but not US, yet 'Set Up Outgoing Payment in Contract Accounting' states payment method I is used for US for testing.

**Status:** open — needs a human decision

## C133 — test-script-advanced-payment-management-4mt-sap-s-4hana-cloud-public-e

Page: [[03-financial-accounting-and-close/test-script-advanced-payment-management-4mt-sap-s-4hana-cloud-public-e]]

The automatic-reject response type is called RJC_01 in the Assign Exception Handling Reaction note but REJ_01 in the Process Payment test step.

**Status:** open — needs a human decision

## C134 — test-script-asset-accounting-additional-depreciation-area-5hg-ae-1095

Page: [[03-financial-accounting-and-close/test-script-asset-accounting-additional-depreciation-area-5hg-ae-1095]]

The takeover date note says the date is usually the prior year-end day, but its example says that in fiscal year 2025 legacy assets are loaded as of year end 2023 (not 2024); the example looks inconsistent with the rule.

**Status:** open — needs a human decision

## C135 — test-script-asset-accounting-group-ledger-ifrs-1gb-ae-719

Page: [[03-financial-accounting-and-close/test-script-asset-accounting-group-ledger-ifrs-1gb-ae-719]]

Ledger mapping is described inconsistently: the Purpose note says IFRS is on 0L (local on 2L) after a ledger switch, while sample data and the revaluation section treat 2L as IFRS and 3L as USGP; may differ from other test scripts in the set.

**Status:** open — needs a human decision

## C136 — test-script-asset-under-construction-bfh-ae-sap-s-4hana-cloud-public-e

Page: [[03-financial-accounting-and-close/test-script-asset-under-construction-bfh-ae-sap-s-4hana-cloud-public-e]]

Legacy AuC asset class is stated inconsistently: creation step and sample data say class 4000 only, the open-items transfer step says 4000 or 4010, and the final-settlement sample row excludes only 4000 and 4001.

**Status:** open — needs a human decision

## C137 — test-script-asset-under-construction-bfh-ae-sap-s-4hana-cloud-public-e

Page: [[03-financial-accounting-and-close/test-script-asset-under-construction-bfh-ae-sap-s-4hana-cloud-public-e]]

Takeover date guidance says it is usually the prior year-end, but the example says that in fiscal year 2025 legacy assets are loaded as of year end 2023 rather than 2024.

**Status:** open — needs a human decision

## C138 — test-script-asset-under-construction-group-ledger-us-gaap-33g-ae-899

Page: [[03-financial-accounting-and-close/test-script-asset-under-construction-group-ledger-us-gaap-33g-ae-899]]

Takeover date note says the date is usually the prior year-end day but then gives the example that in fiscal year 2025 legacy assets are loaded as of year end 2023 (rule implies year end 2024).

**Status:** open — needs a human decision

## C139 — test-script-earmarked-funds-for-real-estate-contracts-6r3-sap-s-4hana

Page: [[03-financial-accounting-and-close/test-script-earmarked-funds-for-real-estate-contracts-6r3-sap-s-4hana]]

Earmarked funds document type is inconsistent: Define Document Types sets Document Type CL under Configure Your Solution but RE under SAP Central Business Configuration (same description, number range and settings), while later steps (CLM contract type activation, workflow start condition) use CL and the Manage Earmarked Funds report filters on document type SC.

**Status:** open — needs a human decision

## C140 — test-script-earmarked-funds-for-real-estate-contracts-6r3-sap-s-4hana

Page: [[03-financial-accounting-and-close/test-script-earmarked-funds-for-real-estate-contracts-6r3-sap-s-4hana]]

Create Contract says Valuation relevance 'No-Leasing Valuation', yet the Overview Table says the valuated contract is created and a separate procedure adds valuation parameters (valuation rule such as US_UGSF_FL).

**Status:** open — needs a human decision

## C141 — test-script-government-budget-planning-6uc-sap-s-4hana-cloud-public-ed

Page: [[03-financial-accounting-and-close/test-script-government-budget-planning-6uc-sap-s-4hana-cloud-public-ed]]

The overview table lists SAP_ALL_GRANT among the Project Planning master data loads, but the Project Planning load procedure (step 6) repeats only SAP_ALL_BUDGETPERIOD, FUNCTIONALAREA, BUDGETACCOUNT, PROFITCENTER, COSTCENTER and PROJECT_WBSELEMENT, with no SAP_ALL_GRANT step.

**Status:** open — needs a human decision

## C142 — test-script-lease-out-accounting-21q-ae-sap-s-4hana-cloud-public-editi

Page: [[03-financial-accounting-and-close/test-script-lease-out-accounting-21q-ae-sap-s-4hana-cloud-public-editi]]

Overview table assigns Periodic Posting and Reverse Contract Postings to 'Accounts Payable Accountant - Leasing', but the test procedures log on as 'Accounts Receivable Accountant - Leasing' (the roles table lists only the AR role).

**Status:** open — needs a human decision

## C143 — test-script-lease-out-for-sublease-accounting-2sb-ae-859

Page: [[03-financial-accounting-and-close/test-script-lease-out-for-sublease-accounting-2sb-ae-859]]

Overview Table lists Accounts Payable Accountant - Leasing as the role for periodic posting, reverse contract postings and several accounting reports, while the test steps and the Roles table use Accounts Receivable Accountant - Leasing.

**Status:** open — needs a human decision

## C144 — test-script-lease-out-for-sublease-accounting-group-ledger-us-gaap-34o

Page: [[03-financial-accounting-and-close/test-script-lease-out-for-sublease-accounting-group-ledger-us-gaap-34o]]

Periodic Posting (F4607) and Reverse Contract Postings (F6275) are assigned to 'Accounts Payable Accountant - Leasing' in the Overview Table, but the test procedures log on as 'Accounts Receivable Accountant - Leasing', and the Roles table lists only the AR role.

**Status:** open — needs a human decision

## C145 — test-script-lease-out-for-sublease-accounting-group-ledger-us-gaap-34o

Page: [[03-financial-accounting-and-close/test-script-lease-out-for-sublease-accounting-group-ledger-us-gaap-34o]]

Overview Table lists Item Overview, Contract Cashflow Report and Periodic Posting Previous Period Comparison under Accounts Payable Accountant - Leasing, while the procedures use Accounts Receivable Accountant - Leasing.

**Status:** open — needs a human decision

## C146 — test-script-payables-financing-with-taulia-7mg-ae-1219

Page: [[03-financial-accounting-and-close/test-script-payables-financing-with-taulia-7mg-ae-1219]]

The Overview Table names the business role for Create Supplier Invoice (F0859) as a personalized role based on SAP_BR_AR_ACCOUNTANT, while the procedure steps say to create a personalized user based on SAP_BR_AP_ACCOUNTANT.

**Status:** open — needs a human decision

## C147 — test-script-payroll-processing-with-sap-erp-hcm-payroll-3up-sap-s-4han

Page: [[03-financial-accounting-and-close/test-script-payroll-processing-with-sap-erp-hcm-payroll-3up-sap-s-4han]]

Portugal section reuses Spain content (prerequisites reference Spain company code, Spain app and US payroll area), so it may not reflect Portugal-specific requirements.

**Status:** open — needs a human decision

## C148 — test-script-sales-based-rent-3f4-ae-sap-s-4hana-cloud-public-edition-9

Page: [[03-financial-accounting-and-close/test-script-sales-based-rent-3f4-ae-sap-s-4hana-cloud-public-edition-9]]

Overview table assigns periodic posting and reverse posting steps to 'Accounts Payable Accountant - Leasing', but the test procedures log on as 'Accounts Receivable Accountant - Leasing'; the roles table lists only the AR role. Likewise 'Contract Valuation Specialist - Leasing' appears in the overview but not in the roles table.

**Status:** open — needs a human decision

## C149 — test-script-sap-s-4hana-cloud-public-edition-accounting-and-financial-

Page: [[03-financial-accounting-and-close/test-script-sap-s-4hana-cloud-public-edition-accounting-and-financial-part-01]]

Aging SGLOBRCL is listed with Months values 1 (CURRENT) and 2 (NONCURRENT) but descriptions 'Current up to 12 Months' and 'Non-current more than 12 Months'; the Months column and the descriptions do not match.

**Status:** open — needs a human decision

## C150 — test-script-sap-s-4hana-cloud-public-edition-accounts-receivable-j59-a

Page: [[03-financial-accounting-and-close/test-script-sap-s-4hana-cloud-public-edition-accounts-receivable-j59-a]]

Overview table lists Manage Payment Advices - Deprecated (F2550) while the appendix documents newer F2550A; both appear in the same script

**Status:** open — needs a human decision

## C151 — test-script-sap-s-4hana-cloud-public-edition-accounts-receivable-j59-a

Page: [[03-financial-accounting-and-close/test-script-sap-s-4hana-cloud-public-edition-accounts-receivable-j59-a]]

Sample customer is given as 3310000133100002 in the master data table but 33100001 in the test procedures

**Status:** open — needs a human decision

## C152 — test-script-sap-s-4hana-cloud-public-edition-earmarked-funds-78s-1205

Page: [[03-financial-accounting-and-close/test-script-sap-s-4hana-cloud-public-edition-earmarked-funds-78s-1205]]

Internal inconsistency: in the Funds Commitment test, the commitment Total Amount is 80 but the expected budget consumption shows a Reduction (REDU) of Funds Precommitment (82) of 90; the same amounts are not otherwise reconciled.

**Status:** open — needs a human decision

## C153 — test-script-sap-s-4hana-cloud-public-edition-earmarked-funds-78s-1205

Page: [[03-financial-accounting-and-close/test-script-sap-s-4hana-cloud-public-edition-earmarked-funds-78s-1205]]

Internal inconsistency: the Funds Precommitment item step says cost center 17301101 (stated to default from the reservation), while the reservation and every consumption check use cost center 17101101.

**Status:** open — needs a human decision

## C154 — test-script-travel-expense-processing-with-sap-concur-1m1-734

Page: [[03-financial-accounting-and-close/test-script-travel-expense-processing-with-sap-concur-1m1-734]]

Overview Table and procedures disagree on resulting statuses: Create Expense Report Obligation via Transport Request is listed as 'Submitted & Pending approval' but its procedure gives 'Pending External Validation'; Check Payment Status is listed as 'changed to paid' but its procedure gives 'Payment Confirmed'.

**Status:** open — needs a human decision

## C155 — test-script-travel-expense-processing-with-sap-concur-1m1-734

Page: [[03-financial-accounting-and-close/test-script-travel-expense-processing-with-sap-concur-1m1-734]]

Pay the Invoice procedure describes the invoice as 'transferred from the SAP Fieldglass system', although the rest of this script has invoices originating from SAP Concur expense reports.

**Status:** open — needs a human decision

## C156 — 2608-pre-configured-tax-codes-en-ae-702

Page: [[04-tax-and-statutory-reporting/2608-pre-configured-tax-codes-en-ae-702]]

Glossary lists condition type MWVZ as 'MWVN is connected to Transaction key NVV' - internal inconsistency in naming

**Status:** open — needs a human decision

## C157 — compliance-formats-support-preparation-for-south-africa-5z5-test-scrip

Page: [[04-tax-and-statutory-reporting/compliance-formats-support-preparation-for-south-africa-5z5-test-scrip]]

The Overview Table lists Accounts Payable Manager for South Africa as the business role for the VAT201 Declaration and VAT 201 Supporting Data File steps, but the Test Procedures for both log on as General Ledger Accountant for South Africa.

**Status:** open — needs a human decision

## C158 — master-data-script-sap-s-4hana-cloud-public-edition-nota-fiscal-brazil

Page: [[04-tax-and-statutory-reporting/master-data-script-sap-s-4hana-cloud-public-edition-nota-fiscal-brazil]]

ICMS Tax Law step labels the key as 'ICMS Law: 3 digit key which will identify the ISS Tax Law' (likely copy error).

**Status:** open — needs a human decision

## C159 — master-data-script-sap-s-4hana-cloud-public-edition-nota-fiscal-brazil

Page: [[04-tax-and-statutory-reporting/master-data-script-sap-s-4hana-cloud-public-edition-nota-fiscal-brazil]]

Incoming service types procedure instructs choosing 'Define Official Brazilian Service Types for Outgoing Notas Fiscais' (likely copy error from outgoing section).

**Status:** open — needs a human decision

## C160 — master-data-script-sap-s-4hana-cloud-public-edition-nota-fiscal-brazil

Page: [[04-tax-and-statutory-reporting/master-data-script-sap-s-4hana-cloud-public-edition-nota-fiscal-brazil]]

Several CPRB steps label Company Code field as '<Supplier code/number>' and Purchase CPRB titles differ slightly from app names (Sales Material vs Materials).

**Status:** open — needs a human decision

## C161 — master-data-script-sap-s-4hana-cloud-public-edition-nota-fiscal-brazil

Page: [[04-tax-and-statutory-reporting/master-data-script-sap-s-4hana-cloud-public-edition-nota-fiscal-brazil]]

Withholding tax code lists for customers/suppliers vary (e.g. IW/IW described as ISS in sales and INSS in financial list; RF/RF vs RF/1R, NS/1N), possibly inconsistent.

**Status:** open — needs a human decision

## C162 — test-script-contract-accounting-external-tax-audit-and-compliance-repo

Page: [[04-tax-and-statutory-reporting/test-script-contract-accounting-external-tax-audit-and-compliance-repo]]

Indirect system access is described inconsistently: Purpose says the administrator exports productive data into reduced-field short-tables that the auditor displays, while Overview Table and Test Procedures say the auditor requests analyses and an employee provides data as a file or paper; no test steps are given for it.

**Status:** open — needs a human decision

## C163 — test-script-enablement-of-sap-excise-tax-management-by-vistex-7z8-ae-s

Page: [[04-tax-and-statutory-reporting/test-script-enablement-of-sap-excise-tax-management-by-vistex-7z8-ae-s]]

Internal inconsistencies in sample data: company code 3310 is described as 'AE Company Code' (country AE, AED) but plant/posting tables use 'US Company Code', USA and USD, and the tax rate rate is labelled EUR per 1 LA while the document currency is USD

**Status:** open — needs a human decision

## C164 — test-script-enablement-of-sap-excise-tax-management-by-vistex-7z8-ae-s

Page: [[04-tax-and-statutory-reporting/test-script-enablement-of-sap-excise-tax-management-by-vistex-7z8-ae-s]]

Calculate step cites example tax rate document '56 (Alcohol - Germany)' while the created document is 'Alcohol - United States'

**Status:** open — needs a human decision

## C165 — test-script-intrastat-processing-for-germany-5ol-sap-s-4hana-cloud-pub

Page: [[04-tax-and-statutory-reporting/test-script-intrastat-processing-for-germany-5ol-sap-s-4hana-cloud-pub]]

Purchasing default step lists Trans. Type Receipts 12 for LP/L/2, while the reference table lists 32 for the same combination (LP, L, item category 2).

**Status:** open — needs a human decision

## C166 — advanced-cash-operations-j78-ae-test-script-sap-s-4hana-cloud-public-e

Page: [[05-treasury-and-cash-management/advanced-cash-operations-j78-ae-test-script-sap-s-4hana-cloud-public-e-part-01]]

Derive Liquidity Item Online is stated to work only with Deferred liquidity analysis update mode, yet the example for company code 3310 sets Liquidity Analysis Update Mode to Close to Real Time while also using Derive Liquidity Item Online for 3310.

**Status:** open — needs a human decision

## C167 — advanced-cash-operations-j78-ae-test-script-sap-s-4hana-cloud-public-e

Page: [[05-treasury-and-cash-management/advanced-cash-operations-j78-ae-test-script-sap-s-4hana-cloud-public-e-part-01]]

Flow Builder runtime parameters still define a Chain Step maximum (1-12, default 6), while the Stop Condition section says the technical concept for chain step is removed in Flow Builder.

**Status:** open — needs a human decision

## C168 — advanced-cash-operations-j78-ae-test-script-sap-s-4hana-cloud-public-e

Page: [[05-treasury-and-cash-management/advanced-cash-operations-j78-ae-test-script-sap-s-4hana-cloud-public-e-part-02]]

Check Notification under 'Situation Handling: Bank Account Balance Threshold Exceeded' tells the recipient to expand type 'Situation Date Difference Warning for FI Flows has been identified', but step 3 then expects an item 'Balance Threshold Alert for Bank Account' - the notification type looks copied from the date difference situation.

**Status:** open — needs a human decision

## C169 — advanced-cash-operations-j78-ae-test-script-sap-s-4hana-cloud-public-e

Page: [[05-treasury-and-cash-management/advanced-cash-operations-j78-ae-test-script-sap-s-4hana-cloud-public-e-part-02]]

Short Term Cash Positioning purpose says hierarchy source 03 shows accounts assigned to cash pools of service provider 'Bank - Time Dependent' and 'In-House Bank - Time - Dependent', while the step 11 note mentions only 'Bank - Time Dependent'.

**Status:** open — needs a human decision

## C170 — bond-management-3wy-ae-test-script-sap-s-4hana-cloud-public-edition-26

Page: [[05-treasury-and-cash-management/bond-management-3wy-ae-test-script-sap-s-4hana-cloud-public-edition-26-part-01]]

Overview table lists Create Security Class for Invested Index-Linked Bond using Manage Securities Classes (FWZZ), while other classes use Manage Security Classes (F8717) - app naming differs by section.

**Status:** open — needs a human decision

## C171 — bond-management-3wy-ae-test-script-sap-s-4hana-cloud-public-edition-26

Page: [[05-treasury-and-cash-management/bond-management-3wy-ae-test-script-sap-s-4hana-cloud-public-edition-26-part-01]]

Intro says process covers fixed-rate, floating-rate and zero-coupon bonds, but the script also tests unit-quoted and index-linked bonds.

**Status:** open — needs a human decision

## C172 — bond-management-3wy-ae-test-script-sap-s-4hana-cloud-public-edition-26

Page: [[05-treasury-and-cash-management/bond-management-3wy-ae-test-script-sap-s-4hana-cloud-public-edition-26-part-01]]

Correspondence section refers to BP_DEFAULT/BP_GROUP while elsewhere the group is named BPG_DEFAULT.

**Status:** open — needs a human decision

## C173 — bond-management-3wy-ae-test-script-sap-s-4hana-cloud-public-edition-26

Page: [[05-treasury-and-cash-management/bond-management-3wy-ae-test-script-sap-s-4hana-cloud-public-edition-26-part-01]]

Section 'Scheduled Repayment Date' purpose text says it describes Interest Rate Adjustment, apparently copied from another section.

**Status:** open — needs a human decision

## C174 — bond-management-3wy-ae-test-script-sap-s-4hana-cloud-public-edition-26

Page: [[05-treasury-and-cash-management/bond-management-3wy-ae-test-script-sap-s-4hana-cloud-public-edition-26-part-02]]

Import Price Index Values purpose text duplicates the reference interest rate wording (apparent copy-paste in source).

**Status:** open — needs a human decision

## C175 — bond-management-3wy-ae-test-script-sap-s-4hana-cloud-public-edition-26

Page: [[05-treasury-and-cash-management/bond-management-3wy-ae-test-script-sap-s-4hana-cloud-public-edition-26-part-02]]

Maintain Email Template step uses app F1306 labelled Deprecated, while Output Parameter Determination refers to a Maintain Email Template app.

**Status:** open — needs a human decision

## C176 — bond-management-3wy-ae-test-script-sap-s-4hana-cloud-public-edition-26

Page: [[05-treasury-and-cash-management/bond-management-3wy-ae-test-script-sap-s-4hana-cloud-public-edition-26-part-02]]

Payment-run examples use differing identifiers (BD_AE3, BD_AE 3, BD_04) across steps, possibly inconsistent example data.

**Status:** open — needs a human decision

## C177 — hedge-accounting-for-fx-option-group-ledger-us-gaap-3x4-ae-test-script

Page: [[05-treasury-and-cash-management/hedge-accounting-for-fx-option-group-ledger-us-gaap-3x4-ae-test-script]]

Simulated Valuation steps say results can be checked for IFRS (valuation area 003), while elsewhere in the same script valuation area 003 is US GAAP.

**Status:** open — needs a human decision

## C178 — intercompany-foreign-exchange-group-ledger-ifrs-2hu-ae-test-script-826

Page: [[05-treasury-and-cash-management/intercompany-foreign-exchange-group-ledger-ifrs-2hu-ae-test-script-826]]

The final step (Post Realized Profit and Loss, production run) says an accounting document is created 'in the US GAAP ledger in financial accounting', while the rest of the script, including that step's own purpose and test-run result, concerns IFRS valuation area 002 (the local GAAP area being AE0).

**Status:** open — needs a human decision

## C179 — interest-rate-derivatives-management-group-ledger-us-gaap-34e-ae-test

Page: [[05-treasury-and-cash-management/interest-rate-derivatives-management-group-ledger-us-gaap-34e-ae-test]]

Run Accrual prerequisite refers to local GAAP valuation area 001, while other sections of the same script use AE0 as the local GAAP valuation area

**Status:** open — needs a human decision

## C180 — letter-of-credit-management-group-ledger-us-gaap-49f-ae-1004

Page: [[05-treasury-and-cash-management/letter-of-credit-management-group-ledger-us-gaap-49f-ae-1004]]

Internal inconsistency: procedure sections say flows are posted in valuation area 003 for US GAAP, while the overview table and some section purposes say area 002 for the IFRS ledger (sample data lists 002); area/GAAP naming is unclear.

**Status:** open — needs a human decision

## C181 — money-market-mutual-fund-management-group-ledger-ifrs-2uo-ae-874

Page: [[05-treasury-and-cash-management/money-market-mutual-fund-management-group-ledger-ifrs-2uo-ae-874]]

Key date valuation test step 6 says the accounting document is created in local GAAP (AE0) although the script is about IFRS area 002; possible internal inconsistency.

**Status:** open — needs a human decision

## C182 — shareholding-management-group-ledger-ifrs-5wg-ae-test-script-1127

Page: [[05-treasury-and-cash-management/shareholding-management-group-ledger-ifrs-5wg-ae-test-script-1127]]

Key date valuation production-run result refers to 'valuation area AE0' while the rest of the script uses valuation area 002 for local GAAP

**Status:** open — needs a human decision

## C183 — test-script-advanced-bank-account-management-j77-ae-sap-s-4hana-cloud-

Page: [[05-treasury-and-cash-management/test-script-advanced-bank-account-management-j77-ae-sap-s-4hana-cloud-part-01]]

Enable Bank Account Contract Type: the Configure Your Solution note says contract types support full cash management with Activate Directly, Two-Person Verification and Activate via Workflow, but the SAP Central Business Configuration note lists only Activate Directly and Activate via Workflow.

**Status:** open — needs a human decision

## C184 — test-script-advanced-bank-account-management-j77-ae-sap-s-4hana-cloud-

Page: [[05-treasury-and-cash-management/test-script-advanced-bank-account-management-j77-ae-sap-s-4hana-cloud-part-01]]

Request grouping value 01 means Group into a Single Change Request in Define Basic Settings (workflow procedure), but the Manage Workflows team note says 01 applies when only Company Code is restricted (00 none, 02 account type only, 03 both).

**Status:** open — needs a human decision

## C185 — test-script-advanced-bank-account-management-j77-ae-sap-s-4hana-cloud-

Page: [[05-treasury-and-cash-management/test-script-advanced-bank-account-management-j77-ae-sap-s-4hana-cloud-part-01]]

Dual control closing section: status Closing Request Sent to Bank is described as showing as To be Closed in the status table and step 6, while later steps and the lifecycle list use Closing Request Sent to Bank.

**Status:** open — needs a human decision

## C186 — test-script-advanced-bank-account-management-j77-ae-sap-s-4hana-cloud-

Page: [[05-treasury-and-cash-management/test-script-advanced-bank-account-management-j77-ae-sap-s-4hana-cloud-part-02]]

In the Two-Person Verification closing path the status after initial closing is called 'To Be Closed' (and the status table description mentions it), whereas the Workflow closing path calls the same state 'Closing Request Sent to Bank'; the status names for the same step differ within the document.

**Status:** open — needs a human decision

## C187 — test-script-bank-integration-with-file-interface-1eg-ae-sap-s-4hana-cl

Page: [[05-treasury-and-cash-management/test-script-bank-integration-with-file-interface-1eg-ae-sap-s-4hana-cl]]

Internal: master data lists SWIFT/BIC BKMEKWKW for house bank AEBK2, but the MT942 and camt.052/camt.053 samples and explanations use DRESDEFF827 and call it the SWIFT/BIC of AEBK2; camt.052 explanation also cites account Id 0000000693123456 and IBAN AE28820800000258006100 while the sample XML contains Id 2580061 and IBAN DE28820800000258006100.

**Status:** open — needs a human decision

## C188 — test-script-bank-integration-with-file-interface-1eg-ae-sap-s-4hana-cl

Page: [[05-treasury-and-cash-management/test-script-bank-integration-with-file-interface-1eg-ae-sap-s-4hana-cl]]

Internal: camt.052 sample XML uses namespace camt.052.001.02, but the import step says Recognized Format CAMT.052.001.08.

**Status:** open — needs a human decision

## C189 — test-script-bank-integration-with-file-interface-1eg-ae-sap-s-4hana-cl

Page: [[05-treasury-and-cash-management/test-script-bank-integration-with-file-interface-1eg-ae-sap-s-4hana-cl]]

Internal: intraday statements are described as not posted ('they are not be posted' in the ZCAMT052 parameter set note) while the same step's expected result and the Purpose say the intraday statement will/can be posted when Posting Category (Intraday) is configured.

**Status:** open — needs a human decision

## C190 — test-script-bank-integration-with-file-interface-1eg-ae-sap-s-4hana-cl

Page: [[05-treasury-and-cash-management/test-script-bank-integration-with-file-interface-1eg-ae-sap-s-4hana-cl]]

Internal: Display Bank Statement test step filters on House Bank AEBK1 / Account AEAC1, whereas all other steps and the sample master data use AEBK2 / AEAC2.

**Status:** open — needs a human decision

## C191 — test-script-basic-bank-account-management-bfa-ae-sap-s-4hana-cloud-pub

Page: [[05-treasury-and-cash-management/test-script-basic-bank-account-management-bfa-ae-sap-s-4hana-cloud-pub]]

Define Settings for Bank Statements: the Configure Your Solution variant sets Transfer Mode (Intraday) to Bank Statement Items Only, while the SAP Central Business Configuration variant of the same step sets Balance and Bank Statement Items.

**Status:** open — needs a human decision

## C192 — test-script-basic-bank-account-management-bfa-ae-sap-s-4hana-cloud-pub

Page: [[05-treasury-and-cash-management/test-script-basic-bank-account-management-bfa-ae-sap-s-4hana-cloud-pub]]

Export/Import Bank Accounts: the Overview Table says accounts are exported from the production system and imported into development and consolidation systems, while the Export purpose says configuration is done in the development system and accounts are exported from that system, and the Import step reports success 'into development system'.

**Status:** open — needs a human decision

## C193 — test-script-basic-bank-account-management-bfa-ae-sap-s-4hana-cloud-pub

Page: [[05-treasury-and-cash-management/test-script-basic-bank-account-management-bfa-ae-sap-s-4hana-cloud-pub]]

Overview Table gives 'GL Accounts are reduced and migrated' as the expected result for Delete Bank Account, but the GL Account Reduction section states the Public Edition supports G/L reduction but not G/L migration.

**Status:** open — needs a human decision

## C194 — test-script-bond-management-group-ledger-us-gaap-3x0-ae-983

Page: [[05-treasury-and-cash-management/test-script-bond-management-group-ledger-us-gaap-3x0-ae-983]]

Operative valuation area for local GAAP is given inconsistently as AE0 and DE0 within the same script (e.g. accrual and Bond Investment TBB1/TPM10 steps mention DE0, while prerequisites and the rest say AE0).

**Status:** open — needs a human decision

## C195 — test-script-bond-management-group-ledger-us-gaap-3x0-ae-983

Page: [[05-treasury-and-cash-management/test-script-bond-management-group-ledger-us-gaap-3x0-ae-983]]

The Production Run steps of the accrual sections say 'Test Run: <select this checkbox>', which contradicts a production run (the valuation and posting sections say to deselect it).

**Status:** open — needs a human decision

## C196 — test-script-debt-and-investment-management-1wv-ae-sap-s-4hana-cloud-pu

Page: [[05-treasury-and-cash-management/test-script-debt-and-investment-management-1wv-ae-sap-s-4hana-cloud-pu-part-01]]

Overview Table assigns Give Notice to Deposit at Notice to Treasury Specialist - Back Office and Adjust Nominal Amount to Front Office, both via Process MM Transactions - Collective Processing (TM00); the test procedures use Front Office for Give Notice, Back Office for Adjust Nominal Amount, and Manage Financial Transactions (F6157) as the app. Manual settlement likewise lists TM00 in the table but F6157 in the procedure.

**Status:** open — needs a human decision

## C197 — test-script-foreign-currency-risk-management-1x1-ae-sap-s-4hana-cloud-

Page: [[05-treasury-and-cash-management/test-script-foreign-currency-risk-management-1x1-ae-sap-s-4hana-cloud-part-01]]

Overview Table (Without Options) lists the app for Take Snapshot for Balance Sheet FX Risk as FXM_REQUEST, while the test procedure uses Take Snapshot - Balance Sheet FX Risk (FXM_SNAP).

**Status:** open — needs a human decision

## C198 — test-script-interest-rate-derivatives-management-1x3-ae-sap-s-4hana-cl

Page: [[05-treasury-and-cash-management/test-script-interest-rate-derivatives-management-1x3-ae-sap-s-4hana-cl-part-01]]

Prerequisites maintain credit limit types Y01 and Y07 only, but the CCS Check Limit Utilization Report step selects limit type 'Y01 or Y09' (the IRS version says 'Y01 or Y07').

**Status:** open — needs a human decision

## C199 — test-script-interest-rate-derivatives-management-1x3-ae-sap-s-4hana-cl

Page: [[05-treasury-and-cash-management/test-script-interest-rate-derivatives-management-1x3-ae-sap-s-4hana-cl-part-01]]

Fair-value description differs between sections: IRS describes two NPV options and only the difference method for CVA/DVA, while the CCS section describes three options (adds basis spread curve) and two CVA/DVA methods (Based on Expected Exposures and Difference); the reference-rate list also differs (IRS lists SORA and HONIA, CCS stops at CORRA).

**Status:** open — needs a human decision

## C200 — test-script-letter-of-credit-management-49d-ae-sap-s-4hana-cloud-publi

Page: [[05-treasury-and-cash-management/test-script-letter-of-credit-management-49d-ae-sap-s-4hana-cloud-publi-part-01]]

Process Payment Request steps send readers to the 'Advanced Cash Operations (J78)' test script for BCM batch approvals in the issue LC and standby LC sections, but to the 'Basic Cash Operations (BFB)' test script in the rollover LC and rollover standby LC sections.

**Status:** open — needs a human decision

## C201 — test-script-sap-s-4hana-cloud-public-edition-money-market-mutual-fund-

Page: [[05-treasury-and-cash-management/test-script-sap-s-4hana-cloud-public-edition-money-market-mutual-fund-part-01]]

Recognize Dividend Distribution states the user has to run dividend accrual at least once before capitalizing it, but Accrue Dividend is stated as only applicable to product type 02B and the 02A and 02C capitalization sections are described as dividend capitalized 'without accrual'.

**Status:** open — needs a human decision

## C202 — test-script-sap-s-4hana-cloud-public-edition-money-market-mutual-fund-

Page: [[05-treasury-and-cash-management/test-script-sap-s-4hana-cloud-public-edition-money-market-mutual-fund-part-01]]

Overview Table says Enter Dividend Factor 'is outside of SAP system', whereas the Enter Dividend Factor procedure directs the tester to the Enter Securities Factor Values step of test script 1XN (app Enter Factor Values TMDFACTORVAL).

**Status:** open — needs a human decision

## C203 — test-script-securities-option-management-6nd-ae-sap-s-4hana-cloud-publ

Page: [[05-treasury-and-cash-management/test-script-securities-option-management-6nd-ae-sap-s-4hana-cloud-publ]]

Post Derived Business Transactions production run expected result mentions posting information for valuation area US0 while creating the accounting document in AE0 (all other steps use AE0 only).

**Status:** open — needs a human decision

## C204 — test-script-shareholding-management-5wf-ae-sap-s-4hana-cloud-public-ed

Page: [[05-treasury-and-cash-management/test-script-shareholding-management-5wf-ae-sap-s-4hana-cloud-public-ed]]

Associate or Joint Venture purchase section purpose says purchased ratio is under 20%, while the document defines associate/JV as 20% to 50%.

**Status:** open — needs a human decision

## C205 — test-script-shareholding-management-5wf-ae-sap-s-4hana-cloud-public-ed

Page: [[05-treasury-and-cash-management/test-script-shareholding-management-5wf-ae-sap-s-4hana-cloud-public-ed]]

Correspondence section refers to BP group BP_DEFAULT / BP_GROUP, whereas elsewhere the predefined group is BPG_DEFAULT.

**Status:** open — needs a human decision

## C206 — test-script-shareholding-management-group-ledger-us-gaap-5wh-ae-1128

Page: [[05-treasury-and-cash-management/test-script-shareholding-management-group-ledger-us-gaap-5wh-ae-1128]]

Valuation area references are inconsistent within the script: the Overview Table says flows post in valuation area 002 for ledger of IFRS and step text mentions local GAAP as 002 or 003, while Purpose states 003 for US GAAP and the prerequisite names operative valuation AE0 for local GAAP.

**Status:** open — needs a human decision

## C207 — test-script-treasury-trading-via-trading-platforms-2f5-sap-s-4hana-clo

Page: [[05-treasury-and-cash-management/test-script-treasury-trading-via-trading-platforms-2f5-sap-s-4hana-clo-part-01]]

The Roles prerequisite table lists only Treasury Specialist Front Office, Middle Office, Cash Management Specialist and Cash Manager, yet the Overview Table and MM test steps use the role Treasury Specialist - Back Office (TM00 Process MM Transactions).

**Status:** open — needs a human decision

## C208 — test-script-treasury-trading-via-trading-platforms-2f5-sap-s-4hana-clo

Page: [[05-treasury-and-cash-management/test-script-treasury-trading-via-trading-platforms-2f5-sap-s-4hana-clo-part-02]]

In the Back-End Format (Intercompany) inbound mapping, TRANSACTION_TYPE for FX_NDS_NDF is 102, while the same key maps to 110 in the external Back-End Format inbound mapping, and FX_NDS_FX_NDF maps to 110 within the intercompany table itself.

**Status:** open — needs a human decision

## C209 — treasury-correspondence-integration-with-swift-network-3qm-test-script

Page: [[05-treasury-and-cash-management/treasury-correspondence-integration-with-swift-network-3qm-test-script]]

Final correspondence status after matching is named inconsistently: the Overview Table expects status 'Match', while the Check Matching of Correspondence Objects section says outgoing and incoming objects change to 'Completed according to the system setting'.

**Status:** open — needs a human decision

## C210 — 2608-master-data-co-en-xx-118

Page: [[06-management-accounting/2608-master-data-co-en-xx-118]]

Cost centers 17101101 etc. appear twice in the Cost Centers sheet with different names and functional areas (e.g. Financials (US) YB40 vs 1000; 17101601 Marketing vs Transportation), so the same ID has two definitions.

**Status:** open — needs a human decision

## C211 — 2608-master-data-co-en-xx-118

Page: [[06-management-accounting/2608-master-data-co-en-xx-118]]

Secondary cost element 63009000 'Leasing Expense' and 64000000 are listed alongside a different ID range for the same account types, and cost element category values '#1' and '#01' are both used.

**Status:** open — needs a human decision

## C212 — 7r8-537

Page: [[06-management-accounting/7r8-537]]

Material ID spelled URR_SRVCON1 in creation step 3 but URR_SRVCONT1 elsewhere in the same document; also description of URR_FPPRJ_1 is 'URR 测试物料 1 SERV' while the overview table lists 'URR 测试物料固定价格客户项目'

**Status:** open — needs a human decision

## C213 — event-based-revenue-recognition-project-based-services-us-gaap-33o-ae

Page: [[06-management-accounting/event-based-revenue-recognition-project-based-services-us-gaap-33o-ae]]

In the Overview Table the Expected Results of Manage Real-Time Revenue Recognition Issues (F4101: values are posted) and Run Revenue Recognition - Projects (F4277: posting issues are reviewed and corrected) appear swapped relative to the Purpose of their own test procedures (4.3 reviews/corrects posting errors; 4.4 runs revenue recognition).

**Status:** open — needs a human decision

## C214 — event-based-revenue-recognition-service-documents-us-gaap-3m5-ae-960

Page: [[06-management-accounting/event-based-revenue-recognition-service-documents-us-gaap-3m5-ae-960]]

Section 4.4 (Manage Revenue Recognition Issues – Service Document) is listed in the Overview Table with app F4186 (Manage Revenue Recognition Issues - Service Documents), but its test step 2 instructs to open Manage Real-Time Revenue Recognition Issues (F4101), the same app used in section 4.2.

**Status:** open — needs a human decision

## C215 — kostenartengruppe-anlegen-sds-bnp-646

Page: [[06-management-accounting/kostenartengruppe-anlegen-sds-bnp-646]]

Prerequisite text refers to entering basic material data, which seems inconsistent with a cost element group procedure

**Status:** open — needs a human decision

## C216 — master-data-script-create-material-master-for-universal-revenue-recogn

Page: [[06-management-accounting/master-data-script-create-material-master-for-universal-revenue-recogn]]

Service contract step 3 uses product number URR_SRVCON1 while the rest of the document uses URR_SRVCONT1

**Status:** open — needs a human decision

## C217 — master-data-script-create-material-master-for-universal-revenue-recogn

Page: [[06-management-accounting/master-data-script-create-material-master-for-universal-revenue-recogn]]

URR_FPPRJ_1 description given as 'URR Test Material1 SERV', same as URR_MAT1_SERV, though the overview table names it 'URR Test Material Fix Price Customer Proj.'

**Status:** open — needs a human decision

## C218 — master-data-script-item-master-for-universal-revenue-recognition-7r8-j

Page: [[06-management-accounting/master-data-script-item-master-for-universal-revenue-recognition-7r8-j]]

The doc says item URR_SRVCONT1 but step 3 enters product number URR_SRVCON1; the URR_FPPRJ_1 item text is URR テスト品目 1 SERV, same as URR_MAT1_SERV's text.

**Status:** open — needs a human decision

## C219 — period-end-closing-projects-bna-ae-test-script-sap-s-4hana-cloud-publi

Page: [[06-management-accounting/period-end-closing-projects-bna-ae-test-script-sap-s-4hana-cloud-publi]]

Statistical project profile is identified as YNS in the Project Profile to Settlement Profile Mapping table but as YP04 in the Project Financial Booklet sections; the document does not reconcile the two IDs.

**Status:** open — needs a human decision

## C220 — script-de-datos-maestros-crear-maestro-de-materiales-para-el-reconocim

Page: [[06-management-accounting/script-de-datos-maestros-crear-maestro-de-materiales-para-el-reconocim]]

Document mentions CE 2502 demo data although it is the 2608 release; step 3 of service contract uses product number URR_SRVCON1 while the rest uses URR_SRVCONT1

**Status:** open — needs a human decision

## C221 — stammdatenskript-materialstamm-fur-universelle-erlosrealisierung-anleg

Page: [[06-management-accounting/stammdatenskript-materialstamm-fur-universelle-erlosrealisierung-anleg]]

Step 3 of the URR_SRVCONT1 section uses product number UER_SRVCON1, whereas the rest of the document uses URR_SRVCONT1.

**Status:** open — needs a human decision

## C222 — stammdatenskript-materialstamm-fur-universelle-erlosrealisierung-anleg

Page: [[06-management-accounting/stammdatenskript-materialstamm-fur-universelle-erlosrealisierung-anleg]]

URR_MAT1_SERV is listed in the purpose table as used in the stock sales scenario, while its section is titled one-time service product; URR_FPPRJ_1 step 6 gives description 'UER-Testmaterial1 SERV' instead of a fixed-price description.

**Status:** open — needs a human decision

## C223 — test-script-event-based-production-cost-posting-3f0-ae-sap-s-4hana-clo

Page: [[06-management-accounting/test-script-event-based-production-cost-posting-3f0-ae-sap-s-4hana-clo]]

Purpose lists six supported variance categories including output price variance, but the Analyze Event-Based Order Costs note lists only five (input quantity, input price, resource usage, lot size, remaining) with SLA line types 9130, 9131, 9132, 9139, 9140 and no output price type.

**Status:** open — needs a human decision

## C224 — test-script-event-based-revenue-recognition-sell-from-stock-ifrs-33m-a

Page: [[06-management-accounting/test-script-event-based-revenue-recognition-sell-from-stock-ifrs-33m-a]]

App ID for Sales Order Actual Data Reporting differs inside the document: the Overview Table gives Sales Orders - Actuals (F1035) while the test procedure opens Sales Orders - Actuals (F1582A).

**Status:** open — needs a human decision

## C225 — test-script-financial-plan-data-upload-from-file-1hb-ae-sap-s-4hana-cl

Page: [[06-management-accounting/test-script-financial-plan-data-upload-from-file-1hb-ae-sap-s-4hana-cl]]

The Purpose note refers to Delete Financial Plan Data (F4074), but later sections name F4074 as Delete Financial Plan Data - with Timestamp and F4851 as Delete Financial Plan Data, so the app ID for the corrective-deletion app is inconsistent within the document.

**Status:** open — needs a human decision

## C226 — test-script-financial-plan-data-upload-from-file-1hb-ae-sap-s-4hana-cl

Page: [[06-management-accounting/test-script-financial-plan-data-upload-from-file-1hb-ae-sap-s-4hana-cl]]

Sample plan data years are inconsistent: the base cost center and market segment files use fiscal year 2022, while the follow-up update files and the statistical key figure table use 2017 and the statistical key figure CSV sample uses 2018 (with cost center 10101101 and company code 1010 versus 33101101 and 3310 in the table), although the verification steps use the current fiscal year.

**Status:** open — needs a human decision

## C227 — test-script-organizational-flexibility-in-financial-accounting-4pg-sap

Page: [[06-management-accounting/test-script-organizational-flexibility-in-financial-accounting-4pg-sap]]

Process and Complete: the purpose says the status becomes Complete if no errors occurred (Processed only if errors), but test step 5 expects the status to be Processed after the run.

**Status:** open — needs a human decision

## C228 — test-script-organizational-flexibility-in-financial-accounting-4pg-sap

Page: [[06-management-accounting/test-script-organizational-flexibility-in-financial-accounting-4pg-sap]]

Last process step (Analyze Profit Center Balances, after processing): the Overview Table says the report shows changes in the standard ledger, but the procedure and purpose use the extension ledger and simulated transfer postings.

**Status:** open — needs a human decision

## C229 — test-script-predictive-commitments-management-2i3-ae-sap-s-4hana-cloud

Page: [[06-management-accounting/test-script-predictive-commitments-management-2i3-ae-sap-s-4hana-cloud]]

Project Budget Report app is given as F3378 in the Overview Table but F3377 in the test procedure.

**Status:** open — needs a human decision

## C230 — test-script-predictive-commitments-management-2i3-ae-sap-s-4hana-cloud

Page: [[06-management-accounting/test-script-predictive-commitments-management-2i3-ae-sap-s-4hana-cloud]]

Overview Table lists the Cost Accountant - Sales role for Import Financial Plan Data (F1711) steps while the template step uses Cost Accountant - Overhead; the exclude step names Manage Cost Centers - Old Version (F1443A) in overview but New Version (F1443B) in procedure.

**Status:** open — needs a human decision

## C231 — test-script-project-control-capital-projects-35f-ae-sap-s-4hana-cloud

Page: [[06-management-accounting/test-script-project-control-capital-projects-35f-ae-sap-s-4hana-cloud]]

Internal contradiction on project coding mask deletion: the note says a coding mask once created can be deleted if no project with the same key exists, while the configuration step notes say once the coding mask is created, deletion is not possible.

**Status:** open — needs a human decision

## C232 — test-script-project-control-capital-projects-35f-ae-sap-s-4hana-cloud

Page: [[06-management-accounting/test-script-project-control-capital-projects-35f-ae-sap-s-4hana-cloud]]

Internal sample-data inconsistency: master data lists cost rates for cost centers 33101301 and 33101101 with activity type 11, but the Maintain Cost Rates steps use cost centers 33101321 and 33101101 with activity type 8.

**Status:** open — needs a human decision

## C233 — test-script-project-control-finance-1nt-ae-sap-s-4hana-cloud-public-ed

Page: [[06-management-accounting/test-script-project-control-finance-1nt-ae-sap-s-4hana-cloud-public-ed]]

Internal contradiction on project coding masks: the Create Project Coding Mask note says a mask once created can be deleted if no project with the same key exists, while the step notes say that once the coding mask is created, deletion is not possible.

**Status:** open — needs a human decision

## C234 — test-script-project-control-research-and-development-projects-35e-ae-9

Page: [[06-management-accounting/test-script-project-control-research-and-development-projects-35e-ae-9]]

Functional area YB75 is described as 'Research & Development' in the master data table but as 'Other expenses' in the Create R&D Project step.

**Status:** open — needs a human decision

## C235 — test-script-project-control-resourcing-and-procurement-4rf-ae-1049

Page: [[06-management-accounting/test-script-project-control-resourcing-and-procurement-4rf-ae-1049]]

The Reservation section's purpose says reservations 'are taken into account by Material Requirements Planning (MRP)', while the Request steps' expected results say 'MRP does not read this reservation and would not create requirements'.

**Status:** open — needs a human decision

## C236 — test-script-project-control-resourcing-and-procurement-4rf-ae-1049

Page: [[06-management-accounting/test-script-project-control-resourcing-and-procurement-4rf-ae-1049]]

Project-stock demands are said to need project profile 'Investment project' only (In CE2108) under Direct Procurement and Check and Return Extra Project Stock, but 'Investment Project and Project with Revenue' under Preliminary Procurement and 'Investment and Revenue' under Reservation.

**Status:** open — needs a human decision

## C237 — test-script-project-control-resourcing-and-procurement-4rf-ae-1049

Page: [[06-management-accounting/test-script-project-control-resourcing-and-procurement-4rf-ae-1049]]

Sample plant differs within the same flows: preliminary procurement and reservation demands use example plant 1710, while the reservation goods issue uses Plant 3310 / storage location 331A for the same WBS element and material FG0611.

**Status:** open — needs a human decision

## C238 — test-script-project-control-sales-4i9-ae-sap-s-4hana-cloud-public-edit

Page: [[06-management-accounting/test-script-project-control-sales-4i9-ae-sap-s-4hana-cloud-public-edit]]

Internal sample-data inconsistency: master data and revenue recognition checks use Company Code 3310 (plant 3310, functional area YB25, Activity Type 8), but the Project Financial Booklet step uses Company Code 1010, the profitability segment step uses Plant 1010 / Functional Area YB10, and the Time Recording note says Activity Type 18.

**Status:** open — needs a human decision

## C239 — test-script-sap-s-4hana-cloud-public-edition-integrated-financial-plan

Page: [[06-management-accounting/test-script-sap-s-4hana-cloud-public-edition-integrated-financial-plan]]

The final section 'Load Master and Actual Data from SAP S/4HANA Cloud Public Edition' carries a Caution that the add-on package is not applicable for SAP S/4HANA Cloud Public Edition source systems, contradicting its own title and purpose.

**Status:** open — needs a human decision

## C240 — 2308-cgaxx-j20-mje-2019-02-pl-10-31

Page: [[07-group-reporting-and-consolidation/2308-cgaxx-j20-mje-2019-02-pl-10-31]]

Sheet name references Z10_Z20 while data uses version J20

**Status:** open — needs a human decision

## C241 — 2308-cgaxx-j20-mje-2019-02-pl-10-31

Page: [[07-group-reporting-and-consolidation/2308-cgaxx-j20-mje-2019-02-pl-10-31]]

Near-duplicate of the CGRXX J20 MJE templates for 2022, 2024 and 2026; line item format differs (1 vs 000001)

**Status:** open — needs a human decision

## C242 — 2308-cgrxx-j20-mje-2022-02-pl-10-53

Page: [[07-group-reporting-and-consolidation/2308-cgrxx-j20-mje-2022-02-pl-10-53]]

Near-duplicate of the CGRXX J20 MJE templates for 2019, 2024 and 2026; only fiscal year differs

**Status:** open — needs a human decision

## C243 — 2308-mcrxx-a10-upload-2023-01-srd2-dt-00-58

Page: [[07-group-reporting-and-consolidation/2308-mcrxx-a10-upload-2023-01-srd2-dt-00-58]]

Sibling upload file differs only in fiscal year (2023 vs 2026) with identical amounts; possible duplicate/stale copy

**Status:** open — needs a human decision

## C244 — 2308-mcrxx-a10-upload-2023-02-srd2-dt-00-59

Page: [[07-group-reporting-and-consolidation/2308-mcrxx-a10-upload-2023-02-srd2-dt-00-59]]

Near-duplicate of the other MCRXX A10 upload template (2023 vs 2026); differs in fiscal year and in quantity/base unit on 172100 rows.

**Status:** open — needs a human decision

## C245 — 2308-outcome-rule-base-1sg-62

Page: [[07-group-reporting-and-consolidation/2308-outcome-rule-base-1sg-62]]

File name says 2308 while the containing folder is release 2608; version relationship is unclear.

**Status:** open — needs a human decision

## C246 — 2402-brd-consolidation-profit-center-72

Page: [[07-group-reporting-and-consolidation/2402-brd-consolidation-profit-center-72]]

Visible header Valid From is 2021-12-31 but the hidden Validation sheet still records VER_VLDFM 20160101.

**Status:** open — needs a human decision

## C247 — 2402-lob-consolidation-profit-center-76

Page: [[07-group-reporting-and-consolidation/2402-lob-consolidation-profit-center-76]]

Visible header Valid From is 2021-12-31 but the hidden Validation sheet still records VER_VLDFM 20160101 (the 2308 version shows 01/01/2016 in both places).

**Status:** open — needs a human decision

## C248 — 2402-seg-consolidation-segment-83

Page: [[07-group-reporting-and-consolidation/2402-seg-consolidation-segment-83]]

Visible Valid From is 2021-12-31 but the hidden Validation sheet metadata in the same file has VER_VLDFM 20160101; the hierarchy structure itself is identical to the 2308 and 2502 variants, which carry different Valid From dates.

**Status:** open — needs a human decision

## C249 — 2402-xxxx-y10-mje-2016-11-pl-0c-85

Page: [[07-group-reporting-and-consolidation/2402-xxxx-y10-mje-2016-11-pl-0c-85]]

Near-duplicate of the XXXX Y10 MJE templates for 2021 and 2023; only fiscal year differs

**Status:** open — needs a human decision

## C250 — 2502-brd-consolidation-profit-center-86

Page: [[07-group-reporting-and-consolidation/2502-brd-consolidation-profit-center-86]]

Visible header Valid From is 2023-12-31 but the hidden Validation sheet still records VER_VLDFM 20160101.

**Status:** open — needs a human decision

## C251 — 2502-lob-consolidation-profit-center-92

Page: [[07-group-reporting-and-consolidation/2502-lob-consolidation-profit-center-92]]

Visible header Valid From is 2023-12-31 but the hidden Validation sheet still records VER_VLDFM 20160101 (the 2308 version shows 01/01/2016 in both places).

**Status:** open — needs a human decision

## C252 — 2502-seg-consolidation-segment-95

Page: [[07-group-reporting-and-consolidation/2502-seg-consolidation-segment-95]]

Visible Valid From is 2023-12-31 but the hidden Validation sheet metadata in the same file has VER_VLDFM 20160101; the hierarchy structure itself is identical to the 2308 and 2402 variants, which carry different Valid From dates.

**Status:** open — needs a human decision

## C253 — 2502-xxxx-y10-mje-2021-11-pl-0c-97

Page: [[07-group-reporting-and-consolidation/2502-xxxx-y10-mje-2021-11-pl-0c-97]]

Near-duplicate of the XXXX Y10 MJE templates for 2016 and 2023; only fiscal year differs

**Status:** open — needs a human decision

## C254 — 2602-outputs-mgc-2023-12-104

Page: [[07-group-reporting-and-consolidation/2602-outputs-mgc-2023-12-104]]

In Balance Sheet 2023.12, J2R Assets (112,005,717.86) does not equal J2R Liabilities & Equity (111,992,665.55), and J1R Total equity differs from J10 slightly; sample data may be intentionally unbalanced.

**Status:** open — needs a human decision

## C255 — 2602-template-financial-statement-item-mapping-109

Page: [[07-group-reporting-and-consolidation/2602-template-financial-statement-item-mapping-109]]

Internal inconsistency: the same FS item ID carries different descriptions in different rows. 585000 is 'Oth Op.Expenses' for 71 accounts but 'Warranty Provision, Current' for 65008600 Warranty Claims Processing; 412200 is 'Cost Serv/Mat' on some rows and 'Cost of Purchased Services and Materials' on others; 214100 is 'Def Inc L.,NC' for 12562000 and 'Deferred Income' for 13811100/13815600.

**Status:** open — needs a human decision

## C256 — 2608-consolidation-units-rule-based-j1s-113

Page: [[07-group-reporting-and-consolidation/2608-consolidation-units-rule-based-j1s-113]]

Version J1S is the filter value but does not appear in the hidden value-help list of consolidation versions.

**Status:** open — needs a human decision

## C257 — 2608-consolidation-units-rule-based-j1s-113

Page: [[07-group-reporting-and-consolidation/2608-consolidation-units-rule-based-j1s-113]]

Value help lists Company 1010 for both 1010 and 1012, and company 1210 for FR00 and FR10; labels look duplicated.

**Status:** open — needs a human decision

## C258 — 2608-consolidation-units-rule-based-j1s-113

Page: [[07-group-reporting-and-consolidation/2608-consolidation-units-rule-based-j1s-113]]

Release is 2608 while effective period is 2025/012, which may be stale or inconsistent with other 2608 content.

**Status:** open — needs a human decision

## C259 — 2608-outcome-rule-base-1sg-123

Page: [[07-group-reporting-and-consolidation/2608-outcome-rule-base-1sg-123]]

The Balance sheet lists 'Net income' 317000 and retained earnings 316000 with a sign change between 012.2025 and 001.2026 (retained earnings 808,208.30 vs -28,970,047.44), a possible inconsistency in sample data.

**Status:** open — needs a human decision

## C260 — 2608-outcome-rule-base-1sg-123

Page: [[07-group-reporting-and-consolidation/2608-outcome-rule-base-1sg-123]]

SCF 2026-01 closing cash (30,117,781.65) differs from balance sheet cash and cash equivalents for 001.2026 (31,334,887.81).

**Status:** open — needs a human decision

## C261 — cgrxx-j10-j1r-j2r-upload-2025-12-srd2-dt-00-155-part-02

Page: [[07-group-reporting-and-consolidation/cgrxx-j10-j1r-j2r-upload-2025-12-srd2-dt-00-155-part-02]]

Version J10 appears twice in the sheet: a main block and a 17-row closing block (lines 3712-3728) whose unit/item/sub-item keys repeat keys of the main J10 block with different amounts (e.g. MXX00 121100/915: -10000 vs 11853 and 88707 in the main block); how repeated keys are treated is not stated in this slice.

**Status:** open — needs a human decision

## C262 — cgrxx-j10-j20-mje-2024-01-pl-30-158

Page: [[07-group-reporting-and-consolidation/cgrxx-j10-j20-mje-2024-01-pl-30-158]]

Sibling file with identical content but fiscal year 2026; the two sample files differ only in year.

**Status:** open — needs a human decision

## C263 — cgrxx-j10-j20-mje-2026-01-pl-30-161

Page: [[07-group-reporting-and-consolidation/cgrxx-j10-j20-mje-2026-01-pl-30-161]]

Sibling file with identical content but fiscal year 2024; the two sample files differ only in year.

**Status:** open — needs a human decision

## C264 — cgrxx-j20-mje-2024-02-pl-10-178

Page: [[07-group-reporting-and-consolidation/cgrxx-j20-mje-2024-02-pl-10-178]]

Near-duplicate of the CGRXX J20 MJE templates for 2019, 2022 and 2026; only fiscal year differs

**Status:** open — needs a human decision

## C265 — cgrxx-j20-mje-2026-02-pl-10-179

Page: [[07-group-reporting-and-consolidation/cgrxx-j20-mje-2026-02-pl-10-179]]

Near-duplicate of the CGRXX J20 MJE templates for 2019, 2022 and 2024; only fiscal year differs

**Status:** open — needs a human decision

## C266 — mcrxx-a10-upload-2026-01-srd2-dt-00-199

Page: [[07-group-reporting-and-consolidation/mcrxx-a10-upload-2026-01-srd2-dt-00-199]]

Sibling upload file differs only in fiscal year (2023 vs 2026) with identical amounts; possible duplicate/stale copy

**Status:** open — needs a human decision

## C267 — mcrxx-a10-upload-2026-02-srd2-dt-00-200

Page: [[07-group-reporting-and-consolidation/mcrxx-a10-upload-2026-02-srd2-dt-00-200]]

Near-duplicate of the other MCRXX A10 upload template (2023 vs 2026); differs in fiscal year and in quantity/base unit on 172100 rows.

**Status:** open — needs a human decision

## C268 — outcome-rule-base-1sg-202

Page: [[07-group-reporting-and-consolidation/outcome-rule-base-1sg-202]]

Hidden text table repeats some item codes (21100D, 21110D, 21170D) with slightly different texts, and code PL appears twice ('Profit and loss' and 'BS and PL').

**Status:** open — needs a human decision

## C269 — outcome-rule-base-1sg-202

Page: [[07-group-reporting-and-consolidation/outcome-rule-base-1sg-202]]

Some translations look inconsistent with the English text, e.g. 511100 'Gains on disposal of investment property' has German text 'Verluste aus Abgang von Beteiligung' (losses), and TSCE10/SCE100 Portuguese 'Demonstração do resultado'.

**Status:** open — needs a human decision

## C270 — test-script-group-reporting-environmental-social-and-governance-data-4

Page: [[07-group-reporting-and-consolidation/test-script-group-reporting-environmental-social-and-governance-data-4]]

Create Version G10 step uses template version Y10 but its expected result says the target version is created with template version Y20.

**Status:** open — needs a human decision

## C271 — test-script-group-reporting-plan-consolidation-28b-sap-s-4hana-cloud-p

Page: [[07-group-reporting-and-consolidation/test-script-group-reporting-plan-consolidation-28b-sap-s-4hana-cloud-p]]

Version descriptions differ between the two configuration paths: Configure Your Solution step 8 sets ZB2 to 'Budget (2024)' and ZB4 to 'Budget (2026)', while the SAP Central Business Configuration path sets ZB2 to 'Budget (2026)' and ZB4 to 'Budget (2028)'; the Overview Table also labels ZB2 as 'Budget 2024' while section 4.2 says 2026.

**Status:** open — needs a human decision

## C272 — test-script-group-reporting-plan-consolidation-28b-sap-s-4hana-cloud-p

Page: [[07-group-reporting-and-consolidation/test-script-group-reporting-plan-consolidation-28b-sap-s-4hana-cloud-p]]

In the Configure Your Solution version setup, step 13 sets global parameters to version ZB2 before 'Assign Process Period Cycle to ZF2' (step 14), whereas the Central Business Configuration path sets version ZF2 for the same step.

**Status:** open — needs a human decision

## C273 — test-script-group-reporting-plan-consolidation-28b-sap-s-4hana-cloud-p

Page: [[07-group-reporting-and-consolidation/test-script-group-reporting-plan-consolidation-28b-sap-s-4hana-cloud-p]]

Pull scenario filter is 'Version Equal public.Actual Bottom Up' for pulling plan data into ZB4, while the push export filters use 'Plan Bottom Up' (balance sheet) and 'Plan' (P&L); it is unclear whether the pull filter is intended to differ.

**Status:** open — needs a human decision

## C274 — test-script-intercompany-reconciliation-process-40y-sap-s-4hana-cloud

Page: [[07-group-reporting-and-consolidation/test-script-intercompany-reconciliation-process-40y-sap-s-4hana-cloud]]

App references are inconsistent within the document: the Overview Table lists Manage Global Hierarchies (F2918) but the procedure opens Manage Consolidation Hierarchies (F7995); Overview lists Schedule Matching Run Jobs (F5011) but the procedure uses Schedule Matching Run Jobs - By Company (F7669); F3865 is given to both Reconciliation Status Overview and Reconciliation Balances.

**Status:** open — needs a human decision

## C275 — test-script-sap-s-4hana-cloud-public-edition-group-reporting-financial

Page: [[07-group-reporting-and-consolidation/test-script-sap-s-4hana-cloud-public-edition-group-reporting-financial-part-01]]

Rule Based COI 2025.12 Initial Consolidation, SAP Central Business Configuration path step 9 (unit level) assigns task S2980 to SBV_RG1 while the Configure Your Solution path assigns S1080 for the same unit-level step and then repeats for S1180.

**Status:** open — needs a human decision

## C276 — test-script-sap-s-4hana-cloud-public-edition-group-reporting-financial

Page: [[07-group-reporting-and-consolidation/test-script-sap-s-4hana-cloud-public-edition-group-reporting-financial-part-01]]

Partial divestiture of MXX07 is described as 'capital decrease' (and MXX08 'capital increase') in the Rule Based COI scenario but as 'no capital decrease' / 'no capital increase' in the MGC scenario; MXX07 share goes 90%->70% in Tables 9 and 11 but 90%->80% in J1S (Table 12).

**Status:** open — needs a human decision

## C277 — test-script-sap-s-4hana-cloud-public-edition-group-reporting-financial

Page: [[07-group-reporting-and-consolidation/test-script-sap-s-4hana-cloud-public-edition-group-reporting-financial-part-01]]

Integrated intercompany Configure Your Solution journal entry template uses transaction currency USD for company 1710 (local currency USD per the unit table) although the note requires a transaction currency different from local currency; the Central Business Configuration path uses EUR.

**Status:** open — needs a human decision

## C278 — test-script-sap-s-4hana-cloud-public-edition-group-reporting-financial

Page: [[07-group-reporting-and-consolidation/test-script-sap-s-4hana-cloud-public-edition-group-reporting-financial-part-01]]

MXX04 Start of Assignment is 2026/001 in the Rule Based COI group structure but 2025/012 in the MGC group structures (Tables 15 and 16), with First Consolidation 2026/001 in both.

**Status:** open — needs a human decision

## C279 — test-script-sap-s-4hana-cloud-public-edition-group-reporting-financial

Page: [[07-group-reporting-and-consolidation/test-script-sap-s-4hana-cloud-public-edition-group-reporting-financial-part-02]]

P&L by Nature of Expense test uses Fiscal Year Period 012.2025 with Key Date 31.12.2024, whereas the Balance Sheet test for the same period uses Key Date 31/12/2025.

**Status:** open — needs a human decision

## C280 — upload-zb2-2024-cgrxx-srd2-209

Page: [[07-group-reporting-and-consolidation/upload-zb2-2024-cgrxx-srd2-209]]

sheet name says UPLOAD_ZB4 while title/version is ZB2

**Status:** open — needs a human decision

## C281 — upload-zb2-2026-cgrxx-srd2-211

Page: [[07-group-reporting-and-consolidation/upload-zb2-2026-cgrxx-srd2-211]]

Sheet is named UPLOAD_ZB4_2026_SRD2 and the file ZB2, while version column is ZB2; possible naming mismatch with a ZB4 version

**Status:** open — needs a human decision

## C282 — xxxx-y10-mje-2023-11-pl-0c-221

Page: [[07-group-reporting-and-consolidation/xxxx-y10-mje-2023-11-pl-0c-221]]

Near-duplicate of the XXXX Y10 MJE templates for 2016 and 2021; only fiscal year differs

**Status:** open — needs a human decision

## C283 — customer-returns-bkp-ae-test-script-sap-s-4hana-cloud-public-edition-1

Page: [[08-sales-order-management/customer-returns-bkp-ae-test-script-sap-s-4hana-cloud-public-edition-1]]

Determine Refund prerequisite refers to second plant 1020/shipping point 1020/storage location 102A, while the sample data and refund steps use second plant 3320 (storage location 332A).

**Status:** open — needs a human decision

## C284 — customer-returns-management-consumer-products-61v-ae-test-script-sap-s

Page: [[08-sales-order-management/customer-returns-management-consumer-products-61v-ae-test-script-sap-s]]

Overview Table lists Determine Refund under Manage Customer Returns (F1708), but the Determine Refund procedure uses Manage Customer Returns - Version 2 (F4832).

**Status:** open — needs a human decision

## C285 — extended-intercompany-processes-for-sales-1wo-ae-test-script-sap-s-4ha

Page: [[08-sales-order-management/extended-intercompany-processes-for-sales-1wo-ae-test-script-sap-s-4ha]]

Business condition says to open posting periods in company codes 1010, 1020, 1710 and 1720, while the procedures use company codes 3310/3320/3330 (AE) for domestic and plant 1710 for international.

**Status:** open — needs a human decision

## C286 — extended-intercompany-processes-for-sales-1wo-ae-test-script-sap-s-4ha

Page: [[08-sales-order-management/extended-intercompany-processes-for-sales-1wo-ae-test-script-sap-s-4ha]]

Domestic 'Create Down Payment Request' says there are five billing settings but lists four; international version says four.

**Status:** open — needs a human decision

## C287 — integration-of-sales-with-external-buyers-2el-ae-test-script-sap-s-4ha

Page: [[08-sales-order-management/integration-of-sales-with-external-buyers-2el-ae-test-script-sap-s-4ha]]

The Overview Table names the app for Manage Sales Documents with Customer Expected Price as 'Manage Sales Orders (F1873)', while the test procedure opens 'Manage Sales Docs with Customer-Expected Price (F2713)'.

**Status:** open — needs a human decision

## C288 — integration-of-sales-with-external-buyers-2el-ae-test-script-sap-s-4ha

Page: [[08-sales-order-management/integration-of-sales-with-external-buyers-2el-ae-test-script-sap-s-4ha]]

Post Goods Issue purpose says 'post the goods receipt in the SAP S/4HANA Buyer system', but the steps are performed by the Shipping Specialist in VL06O_CLOUD on the supplier side and post a goods issue.

**Status:** open — needs a human decision

## C289 — invoice-correction-process-with-credit-memo-bkl-ae-test-script-sap-s-4

Page: [[08-sales-order-management/invoice-correction-process-with-credit-memo-bkl-ae-test-script-sap-s-4]]

Document is the UAE (AE) script, but the Define Identification Types and Maintain Company Code Data steps tell the user to set local version to Malaysia, and the optional BP step refers to a Malaysia participant ID, while the Process Communication step sets United Arab Emirates.

**Status:** open — needs a human decision

## C290 — mds-5nh-481

Page: [[08-sales-order-management/mds-5nh-481]]

The plant substitution control section's purpose text refers to storage location substitution/exclusion controls rather than plant, an internal inconsistency.

**Status:** open — needs a human decision

## C291 — sales-processing-using-third-party-with-shipping-notification-bd3-ae-t

Page: [[08-sales-order-management/sales-processing-using-third-party-with-shipping-notification-bd3-ae-t]]

Workflow configuration example uses a total net amount threshold greater than 10 AED, while the approval step states POs of 500 AED or more with purchasing group 003 require approval; thresholds differ.

**Status:** open — needs a human decision

## C292 — sales-processing-using-third-party-with-shipping-notification-bd3-ae-t

Page: [[08-sales-order-management/sales-processing-using-third-party-with-shipping-notification-bd3-ae-t]]

Item category determination is described as 'three options' in one section, and as 3 standard ways plus a NEW fourth (Advanced ATP) in the 1JW integration section.

**Status:** open — needs a human decision

## C293 — sales-processing-using-third-party-without-shipping-notification-bdk-a

Page: [[08-sales-order-management/sales-processing-using-third-party-without-shipping-notification-bdk-a]]

Approval threshold is inconsistent within the document: the workflow configuration example uses total net amount greater than 10 AED, while the release section states approval is needed for PO >= 500 AED with purchasing group 003.

**Status:** open — needs a human decision

## C294 — self-billing-4h2-ae-test-script-sap-s-4hana-cloud-public-edition-1028

Page: [[08-sales-order-management/self-billing-4h2-ae-test-script-sap-s-4hana-cloud-public-edition-1028]]

Business Conditions require the 3NR script completed with 'valid delivery, billing created', while Create Delivery says deliveries follow 3NR 'but do not create billing document'.

**Status:** open — needs a human decision

## C295 — self-billing-4h2-ae-test-script-sap-s-4hana-cloud-public-edition-1028

Page: [[08-sales-order-management/self-billing-4h2-ae-test-script-sap-s-4hana-cloud-public-edition-1028]]

Format Transmission refers to 'three preceding deliveries' and the check steps expect three entries, but only two deliveries (80000001, 80000002) and two delivery headers appear in the scenario and example transmission.

**Status:** open — needs a human decision

## C296 — self-billing-4h2-ae-test-script-sap-s-4hana-cloud-public-edition-1028

Page: [[08-sales-order-management/self-billing-4h2-ae-test-script-sap-s-4hana-cloud-public-edition-1028]]

Scenario table states TG12 (delivered 8, transmitted 7 PCE) gives 'No difference ... partially billed', while Check Simulation Result expects Quantity Difference -1.000 PC and issue type Quantity Difference for the same item.

**Status:** open — needs a human decision

## C297 — self-billing-4h2-ae-test-script-sap-s-4hana-cloud-public-edition-1028

Page: [[08-sales-order-management/self-billing-4h2-ae-test-script-sap-s-4hana-cloud-public-edition-1028]]

Second scheduling agreement (30000002) is listed under sold-to party 33100001, whereas sample data, parameters, transmission and sold-to determination use only 33100003.

**Status:** open — needs a human decision

## C298 — sell-from-stock-with-invoice-creation-before-goods-issue-7ua-ae-test-s

Page: [[08-sales-order-management/sell-from-stock-with-invoice-creation-before-goods-issue-7ua-ae-test-s]]

App names differ between the Overview Table and the step procedures: billing creation is 'Create Billing Documents (F0798)' in the overview but 'Create Billing Documents - VF01 (VF01)' in the procedure; billing attachment is 'Display Billing Documents (VF03)' in the overview but 'Manage Billing Documents (F0797)' in the procedure.

**Status:** open — needs a human decision

## C299 — statistical-sales-conditions-34b-ae-test-script-906

Page: [[08-sales-order-management/statistical-sales-conditions-34b-ae-test-script-906]]

Master data table lists sold-to/ship-to/payer 33100001 but the sales order test step uses customer 33100002 (and mentions 33100009 for customer material).

**Status:** open — needs a human decision

## C300 — test-script-advanced-intercompany-sales-5d2-ae-sap-s-4hana-cloud-publi

Page: [[08-sales-order-management/test-script-advanced-intercompany-sales-5d2-ae-sap-s-4hana-cloud-publi]]

Script is for the AE (UAE) localization with company 3310, but financial posting guidance refers to Italian FI document types W1/W2/W3, Part 2 sales order example uses sales org 1010/DE, and invoice form template SDBIL_INVOICE_RU is a Russian template; may disagree with other localized versions of 5D2.

**Status:** open — needs a human decision

## C301 — test-script-advanced-intercompany-sales-make-to-order-and-variant-conf

Page: [[08-sales-order-management/test-script-advanced-intercompany-sales-make-to-order-and-variant-conf]]

Purpose lists only 5D2 and 1YT as required business conditions, but the Business Conditions table also requires scope item BJE (Make-to-Order Production - Finished Goods Sales and Final Assembly) to be activated.

**Status:** open — needs a human decision

## C302 — test-script-advanced-intercompany-sales-make-to-order-and-variant-conf

Page: [[08-sales-order-management/test-script-advanced-intercompany-sales-make-to-order-and-variant-conf]]

Post Goods Issue expected result says goods issue is posted to Stock in Transit of the delivering company, 'for example, 3310', although 3310 is the selling company and the delivering company is 1710.

**Status:** open — needs a human decision

## C303 — test-script-automation-of-order-to-invoice-with-sap-business-network-4

Page: [[08-sales-order-management/test-script-automation-of-order-to-invoice-with-sap-business-network-4]]

PO approval threshold: the Approve Purchase Order section says POs of 500 USD or more (purchasing groups 001 and 003) require approval, while the flexible workflow configured in the preliminary steps triggers on purchasing group 001 with net amount greater than 100 AED; the two thresholds differ.

**Status:** open — needs a human decision

## C304 — test-script-automation-of-order-to-invoice-with-sap-business-network-4

Page: [[08-sales-order-management/test-script-automation-of-order-to-invoice-with-sap-business-network-4]]

App identifiers differ within the document: the Overview Table lists My Inbox - All Items as F5331 while the Approve Purchase Order procedure uses F0862; the Overview lists Create Purchase Order - Advanced (ME21N) while the procedure uses Manage Purchase Orders (F0842A).

**Status:** open — needs a human decision

## C305 — test-script-automation-of-order-to-invoice-with-sap-business-network-4

Page: [[08-sales-order-management/test-script-automation-of-order-to-invoice-with-sap-business-network-4]]

Example prices do not match although the script requires sales and purchase prices to correspond: PO net order price is 17.55 AED while the sales pricing condition PPR0 is set to 20.05 AED.

**Status:** open — needs a human decision

## C306 — test-script-automation-of-order-to-invoice-with-sap-business-network-4

Page: [[08-sales-order-management/test-script-automation-of-order-to-invoice-with-sap-business-network-4]]

Check Inbound Delivery for Purchase Order Confirmations is titled (Optional) but its prerequisite note calls it a necessary step before continuing to test this scope item.

**Status:** open — needs a human decision

## C307 — test-script-credit-and-debit-memo-processing-with-variant-configuratio

Page: [[08-sales-order-management/test-script-credit-and-debit-memo-processing-with-variant-configuratio]]

Workflow example names the level-1 workflow 'First Approver - No conditions' and 'Net Value over AED 500', while the text says under AED 500 needs no approval; exact handling at 500/1000 boundaries is unspecified.

**Status:** open — needs a human decision

## C308 — test-script-credit-memo-processing-1ez-ae-sap-s-4hana-cloud-public-edi

Page: [[08-sales-order-management/test-script-credit-memo-processing-1ez-ae-sap-s-4hana-cloud-public-edi]]

UAE (AE) script gives Malaysia-specific instructions in the PEPPOL preliminary steps: local version is set to Malaysia for 'Define Identification Types' and 'Maintain Company Code Data', and the BP step refers to a 'Malaysia participant ID', while the process-communication step sets United Arab Emirates.

**Status:** open — needs a human decision

## C309 — test-script-credit-memo-processing-1ez-ae-sap-s-4hana-cloud-public-edi

Page: [[08-sales-order-management/test-script-credit-memo-processing-1ez-ae-sap-s-4hana-cloud-public-edi]]

Optional step 'Remove Billing Block from Order Type' removes entry Y8 for sales document type CR, yet the credit memo request step expects a billing block to be assigned on save, and the Purpose describes the request as placed on billing block for review before release.

**Status:** open — needs a human decision

## C310 — test-script-customer-consignment-1iu-ae-sap-s-4hana-cloud-public-editi

Page: [[08-sales-order-management/test-script-customer-consignment-1iu-ae-sap-s-4hana-cloud-public-editi]]

Internal inconsistency in the Consignment Pick-Up Check Stock Overview step: it says goods are 'transferred again to customer's consignment stock' and expects the quantity 'posted into the consignment stock', while the Overview Table and the Post Goods Receipt step say pick-up posts goods from consignment stock directly into free stock.

**Status:** open — needs a human decision

## C311 — test-script-customer-consignment-1iu-ae-sap-s-4hana-cloud-public-editi

Page: [[08-sales-order-management/test-script-customer-consignment-1iu-ae-sap-s-4hana-cloud-public-editi]]

Internal inconsistency in the Consignment Return Check Stock Overview step: it says goods are 'transferred from the customer's consignment stock and no longer owned by the company', while the Overview Table and the Post Goods Receipt step say the received quantity is added to the customer consignment stock.

**Status:** open — needs a human decision

## C312 — test-script-lean-customer-returns-bdd-ae-sap-s-4hana-cloud-public-edit

Page: [[08-sales-order-management/test-script-lean-customer-returns-bdd-ae-sap-s-4hana-cloud-public-edit]]

Create Attachment for Delivery is listed in the Overview Table with app Display Outbound Delivery (VL03N), but the test procedure opens Change Outbound Delivery (VL02N).

**Status:** open — needs a human decision

## C313 — test-script-lean-customer-returns-bdd-ae-sap-s-4hana-cloud-public-edit

Page: [[08-sales-order-management/test-script-lean-customer-returns-bdd-ae-sap-s-4hana-cloud-public-edit]]

Purpose says the returns order is created optionally with reference to the original sales order or invoice, and the Create Returns Order step notes it can be created without reference, yet that step's Prerequisites say you must have a reference invoice number and a billing document from BD9.

**Status:** open — needs a human decision

## C314 — test-script-omnichannel-convergent-billing-1mc-ae-sap-s-4hana-cloud-pu

Page: [[08-sales-order-management/test-script-omnichannel-convergent-billing-1mc-ae-sap-s-4hana-cloud-pu]]

Invoice List note says 'Automatically post billing documents - ON' must be set in the earlier billing steps, but the Billing Settings in all preceding test procedures (4.1-4.5) specify 'Automatically Post Billing Documents - OFF'.

**Status:** open — needs a human decision

## C315 — test-script-returnables-processing-bdw-ae-sap-s-4hana-cloud-public-edi

Page: [[08-sales-order-management/test-script-returnables-processing-bdw-ae-sap-s-4hana-cloud-public-edi]]

The Purpose says unreturned pallets are handled with debit memo requests, debit memos and a manual goods issue after consignment stock synchronization, but the procedure uses a CCLN pallets issue order, VL02N goods issue and an F2 invoice, with no debit memo or consignment sync step.

**Status:** open — needs a human decision

## C316 — test-script-returnables-processing-bdw-ae-sap-s-4hana-cloud-public-edi

Page: [[08-sales-order-management/test-script-returnables-processing-bdw-ae-sap-s-4hana-cloud-public-edi]]

Receivables account differs between the two billing sections: 12100000 Rcvbls Domestic in Create Billing Documents versus 10100001 Rcvbls Domestic DE 1 in the unreturned-pallets Create Billing Document, a German-named account in a UAE script; the 'separate billing document per item' setting is also ON in one and OFF in the other.

**Status:** open — needs a human decision

## C317 — test-script-returnables-processing-bdw-ae-sap-s-4hana-cloud-public-edi

Page: [[08-sales-order-management/test-script-returnables-processing-bdw-ae-sap-s-4hana-cloud-public-edi]]

The Overview Table names different apps than the procedures for some steps: sales order attachment lists Manage Sales Orders (F1873) but the procedure uses F3893, and the pallets return sales order lists F1873 but the procedure uses Create Sales Orders - VA01.

**Status:** open — needs a human decision

## C318 — test-script-sales-contract-management-i9i-ae-sap-s-4hana-cloud-public

Page: [[08-sales-order-management/test-script-sales-contract-management-i9i-ae-sap-s-4hana-cloud-public]]

Overview Table role/app assignments disagree with the procedures: 'Create Down Payment Request Part II' is listed as Accounts Payable Accountant / Post Incoming Payments (F1345) but the procedure uses Billing Clerk / Create Billing Documents (F0798); 'Post Incoming Payment' is listed as Billing Clerk / F0798 but the procedure uses Accounts Receivable Accountant / F1345 (the Roles table has no Accounts Payable Accountant); 'Print Form - Output Management' is listed under Manage Sales Orders (F1873) but the procedure uses Manage Sales Contracts (F1851).

**Status:** open — needs a human decision

## C319 — test-script-sales-contract-management-i9i-ae-sap-s-4hana-cloud-public

Page: [[08-sales-order-management/test-script-sales-contract-management-i9i-ae-sap-s-4hana-cloud-public]]

Material TG11 is entered in the Scenario 2 to 5 contract and order steps, but the sample data table lists TG12, TG10, TG13, TG14 and no TG11 (Scenario 1 enters TG12, while the Customer Material note in Scenarios 2 to 5 refers to TG12).

**Status:** open — needs a human decision

## C320 — test-script-sales-contract-management-i9i-ae-sap-s-4hana-cloud-public

Page: [[08-sales-order-management/test-script-sales-contract-management-i9i-ae-sap-s-4hana-cloud-public]]

Price agreement condition type is DPA1 when maintained in the contract and checked at billing, but the sales order checks in Scenarios 3 to 5 expect condition type DAP1.

**Status:** open — needs a human decision

## C321 — test-script-sales-of-non-stock-item-with-order-specific-procurement-bd

Page: [[08-sales-order-management/test-script-sales-of-non-stock-item-with-order-specific-procurement-bd]]

PO approval threshold is stated inconsistently: Purpose says '>= 500 USD' with purchase group 003, step 3 says net value of '500 AED or more', step 4 says '500 USD or more', and the workflow configuration example uses 'greater than 10' in AED.

**Status:** open — needs a human decision

## C322 — test-script-sales-of-non-stock-item-with-order-specific-procurement-bd

Page: [[08-sales-order-management/test-script-sales-of-non-stock-item-with-order-specific-procurement-bd]]

Sold-to party: sample master data lists 33100003 (Domestic UAE Customer 3), but the Create Sales Order step enters Sold-to Party 33100005.

**Status:** open — needs a human decision

## C323 — test-script-sales-of-non-stock-item-with-order-specific-procurement-bd

Page: [[08-sales-order-management/test-script-sales-of-non-stock-item-with-order-specific-procurement-bd]]

Purchasing group: the purchasing info record is created with purchasing group 002 (repeat with 001), whereas the PO approval workflow and rule require purchasing group 003.

**Status:** open — needs a human decision

## C324 — test-script-sales-of-non-stock-item-with-order-specific-procurement-bd

Page: [[08-sales-order-management/test-script-sales-of-non-stock-item-with-order-specific-procurement-bd]]

Info record price: step 8 enters condition amount 300 AED, while the following notes state net prices of 35 AED and 25 AED for the same material.

**Status:** open — needs a human decision

## C325 — test-script-sales-of-non-stock-item-with-order-specific-procurement-bd

Page: [[08-sales-order-management/test-script-sales-of-non-stock-item-with-order-specific-procurement-bd]]

Overview Table app names differ from the procedures: Create Delivery lists VL01N but the procedure opens F0869A; sales order attachment lists F1873 but the procedure opens F3893; Approve and Release PO lists 'Approve Purchase Orders' but the procedure opens My Inbox (F2097).

**Status:** open — needs a human decision

## C326 — test-script-sales-order-entry-with-one-time-customer-bdh-ae-1254

Page: [[08-sales-order-management/test-script-sales-order-entry-with-one-time-customer-bdh-ae-1254]]

Account group of one-time customer 33100273 is stated as CPD in the Purpose section but as CFD in the Create Sales Order step note.

**Status:** open — needs a human decision

## C327 — test-script-sales-order-entry-with-one-time-customer-bdh-ae-1254

Page: [[08-sales-order-management/test-script-sales-order-entry-with-one-time-customer-bdh-ae-1254]]

Billing postings refer to a customer ID 'created in chapter 4.2', but 4.2 only changes the sales order address and creates no customer.

**Status:** open — needs a human decision

## C328 — test-script-sales-order-fulfillment-monitoring-and-operations-bkk-ae-1

Page: [[08-sales-order-management/test-script-sales-order-fulfillment-monitoring-and-operations-bkk-ae-1]]

Billing due list app is identified as Create Billing Documents (F0798) in the Overview Table but as Create Billing Documents - VF04 (VF04) in the procedure for the same step.

**Status:** open — needs a human decision

## C329 — test-script-sales-order-processing-for-sales-kits-31q-ae-896

Page: [[08-sales-order-management/test-script-sales-order-processing-for-sales-kits-31q-ae-896]]

Process code BKK is used for two different scope items in the same document: 'Sales Period End Closing Operations (BKK)' under Succeeding Processes and 'BKK-Sales Order Processing - SEPA Direct Debit Handling' under Relevant Processes.

**Status:** open — needs a human decision

## C330 — test-script-sales-order-processing-with-customer-down-payment-bkj-ae-1

Page: [[08-sales-order-management/test-script-sales-order-processing-with-customer-down-payment-bkj-ae-1]]

The UAE (AE) script tells the user to set the local/country version to Malaysia when defining identification types for business partners and maintaining company code data, and describes a Malaysia participant ID for the business partner, while the process communication step selects United Arab Emirates; the intended country version is inconsistent within the document.

**Status:** open — needs a human decision

## C331 — test-script-sales-order-processing-with-invoice-list-and-collective-bi

Page: [[08-sales-order-management/test-script-sales-order-processing-with-invoice-list-and-collective-bi]]

Master data table says Order combination is switched off in the customer master for both 33100001 and 33100002, but the Overview Table and the collective-billing Create Delivery step say the Order Combination checkbox is switched on for 33100002 (its orders merge into one delivery).

**Status:** open — needs a human decision

## C332 — test-script-sales-order-processing-with-invoice-list-and-collective-bi

Page: [[08-sales-order-management/test-script-sales-order-processing-with-invoice-list-and-collective-bi]]

Goods issue debit account differs between the two processes: 51600000 Consptn Trde Gds in the invoice list section versus 54083000 Consptn Trde Gds in the collective billing section, for the same Trading Good (HAWA) posting.

**Status:** open — needs a human decision

## C333 — test-script-sales-scheduling-agreement-with-consignment-4lz-ae-sap-s-4

Page: [[08-sales-order-management/test-script-sales-scheduling-agreement-with-consignment-4lz-ae-sap-s-4]]

Stock overview expected results are inconsistent within the script: the Overview Table says consignment pick-up posts the quantity from consignment stock into free available stock (and 4.3.4 says the same), but 4.3.5 Check Stock Overview says the goods are transferred again to the customer's consignment stock.

**Status:** open — needs a human decision

## C334 — test-script-sales-scheduling-agreement-with-consignment-4lz-ae-sap-s-4

Page: [[08-sales-order-management/test-script-sales-scheduling-agreement-with-consignment-4lz-ae-sap-s-4]]

Consignment issue stock check: the Overview Table says customer consignment stock is reduced by the goods issue, while step 4.2.6 states the expected result as the delivered quantity being posted into the consignment stock; for consignment return, 4.4.5 purpose says goods are transferred from consignment stock and no longer owned, while the Overview Table says the received quantity is added to customer consignment stock.

**Status:** open — needs a human decision

## C335 — test-script-sales-scheduling-agreement-with-consignment-4lz-ae-sap-s-4

Page: [[08-sales-order-management/test-script-sales-scheduling-agreement-with-consignment-4lz-ae-sap-s-4]]

Financial postings for the consignment return goods receipt (Option 1, Without Scheduling) show debit 51600000 Consptn Trde Gds / credit 13600000 Inventory TradingGd, identical to the consignment issue goods issue, whereas the consignment pick-up goods receipt states no accounting document is created because ownership does not change.

**Status:** open — needs a human decision

## C336 — test-script-sap-returnable-packaging-management-7ho-ae-1215

Page: [[08-sales-order-management/test-script-sap-returnable-packaging-management-7ho-ae-1215]]

The prerequisites state material masters are to be created for both US (1710) and DE (1010) plants, while all sample data and steps in the script use plant 3310 (Plant 1 AE).

**Status:** open — needs a human decision

## C337 — test-script-sap-s-4hana-cloud-public-edition-complaint-handling-7bg-12

Page: [[08-sales-order-management/test-script-sap-s-4hana-cloud-public-edition-complaint-handling-7bg-12]]

Approve-with-reference procedure only clicks Submit (status SUBM) rather than Approve, unlike the without-reference approval; Overview Table roles (Complaint Approver, Configuration Admin) differ from the single role listed in Roles (SAP_BR_CMH_CLAIM_ANALYST)

**Status:** open — needs a human decision

## C338 — test-script-sap-s-4hana-cloud-public-edition-internal-commissions-sett

Page: [[08-sales-order-management/test-script-sap-s-4hana-cloud-public-edition-internal-commissions-sett]]

Prepare Transactional Data is headed (Optional) but its text says 'Preparing transactional data is a required step'.

**Status:** open — needs a human decision

## C339 — test-script-sap-s-4hana-cloud-public-edition-just-in-time-supply-to-cu

Page: [[08-sales-order-management/test-script-sap-s-4hana-cloud-public-edition-just-in-time-supply-to-cu]]

Summarized JIT (supply from stock) scheduling agreement uses sold-to/ship-to 33154802, material FGJIT02, customer material CFGJIT02 and type LKJ, while the supply control and JIT call for this scenario use customer 33154801, material FGJIT01 and CFGJIT01 (type LZJ elsewhere).

**Status:** open — needs a human decision

## C340 — test-script-sap-s-4hana-cloud-public-edition-just-in-time-supply-to-cu

Page: [[08-sales-order-management/test-script-sap-s-4hana-cloud-public-edition-just-in-time-supply-to-cu]]

Sequenced supply-from-stock scheduling agreement uses sold-to 33154801 and customer material CFGJIT01, while its supply control, delivery sequence group and JIT call use customer 33154802 and CFGJIT02; its packing group job uses SGJIT02/PSA_04 instead of FGJIT02/PSA_03.

**Status:** open — needs a human decision

## C341 — test-script-sap-s-4hana-cloud-public-edition-just-in-time-supply-to-cu

Page: [[08-sales-order-management/test-script-sap-s-4hana-cloud-public-edition-just-in-time-supply-to-cu]]

JIT production confirmation profile for summarized production is set to 'Asynchronous execution of Backflush' in preliminary steps, but a Note in Confirm Production says it must be 'Execution of Custom Specific Logic'.

**Status:** open — needs a human decision

## C342 — test-script-sap-s-4hana-cloud-public-edition-sell-from-stock-bd9-ae-12

Page: [[08-sales-order-management/test-script-sap-s-4hana-cloud-public-edition-sell-from-stock-bd9-ae-12]]

Sales order approval thresholds are inconsistent: the workflow purpose text says 1000 USD, the configuration step uses currency AED 1000, and the change-sales-order step refers to amount >500 USD.

**Status:** open — needs a human decision

## C343 — test-script-sap-s-4hana-cloud-public-edition-sell-from-stock-bd9-ae-12

Page: [[08-sales-order-management/test-script-sap-s-4hana-cloud-public-edition-sell-from-stock-bd9-ae-12]]

Preliminary billing approval note says total amount not less than 500 USD, while the workflow example and rework step use EUR 500/1000.

**Status:** open — needs a human decision

## C344 — test-script-sell-from-stock-consumer-products-5hl-ae-sap-s-4hana-cloud

Page: [[08-sales-order-management/test-script-sell-from-stock-consumer-products-5hl-ae-sap-s-4hana-cloud]]

The VSIT section (Post Goods Issue) lists COGS/inventory postings (54083000 / 13400000, 51600000 / 13600000) identical to the standard flow, while the Purpose says goods issue to the delivery only moves stock into VSIT and revenue and COGS are recognized at the later goods issue from VSIT.

**Status:** open — needs a human decision

## C345 — test-script-sell-from-stock-consumer-products-5hl-ae-sap-s-4hana-cloud

Page: [[08-sales-order-management/test-script-sell-from-stock-consumer-products-5hl-ae-sap-s-4hana-cloud]]

The VSIT section says 'create three sales orders', 'three deliveries' and 'three billing documents', but its steps and the overview table cover only one order (customer 33105001) and the goods issue expected result is '1 successful and 0 incorrect goods movements'.

**Status:** open — needs a human decision

## C346 — convergent-invoicing-invoice-correction-processing-2be-ae-test-script

Page: [[09-subscription-billing-and-contract-accounting/convergent-invoicing-invoice-correction-processing-2be-ae-test-script]]

Example approval threshold is inconsistent within the document: the BAdI sample code triggers the workflow when total amount is greater than 100, while the example workflow start condition is greater than or equal to 100 (differs at exactly 100).

**Status:** open — needs a human decision

## C347 — master-data-script-create-subscription-product-convergent-invoicing-md

Page: [[09-subscription-billing-and-contract-accounting/master-data-script-create-subscription-product-convergent-invoicing-md]]

Internal inconsistencies: the usage rate element is R-TICKETS but the price calculation template and UsagePrice lookup use R-TRAFFIC; P-CLOUD_SUPPORT enrichment step 4 names Product Number P-CLOUD_COMM; SBRE procedure headings use R_ONETIME/R_SEATS/R_TICKETS versus R-... IDs.

**Status:** open — needs a human decision

## C348 — master-data-script-create-subscription-product-sales-billing-mds-5bd-4

Page: [[09-subscription-billing-and-contract-accounting/master-data-script-create-subscription-product-sales-billing-mds-5bd-4]]

German plant for R-SEATS is given as 'Plant 1010' while R-ONETIME and R-TRAFFIC use 'Plant 10101' (Plant DE); internal inconsistency.

**Status:** open — needs a human decision

## C349 — mds-5bd-429

Page: [[09-subscription-billing-and-contract-accounting/mds-5bd-429]]

Plant for Germany R-SEATS given as 1010 while R-ONETIME and R-TRAFFIC give 10101 (internal inconsistency)

**Status:** open — needs a human decision

## C350 — mds-5bd-429

Page: [[09-subscription-billing-and-contract-accounting/mds-5bd-429]]

Product ID P-CLD_STORAGE_PCS in overview table differs from P-CLOUD_STORAGE_PC created in procedure

**Status:** open — needs a human decision

## C351 — mds-5lp-451

Page: [[09-subscription-billing-and-contract-accounting/mds-5lp-451]]

Usage rate element is R-TICKETS in the rate element/template sections but R-TRAFFIC in price calculation rate plan template and UsagePrice upload; product IDs written R-ONETIME vs R_ONETIME in headings.

**Status:** open — needs a human decision

## C352 — mds-5lp-451

Page: [[09-subscription-billing-and-contract-accounting/mds-5lp-451]]

Table 3 and 'Table 1' UsagePrice/OneTimePrice upload steps reference lookup table OneTimePrice where UsagePrice is intended.

**Status:** open — needs a human decision

## C353 — sap-s-4hana-cloud-public-edition-convergent-invoicing-mds-5lp-453

Page: [[09-subscription-billing-and-contract-accounting/sap-s-4hana-cloud-public-edition-convergent-invoicing-mds-5lp-453]]

Usage rate element named R-TICKETS in rate element section but R-TRAFFIC in the price calculation template and usage lookup table steps

**Status:** open — needs a human decision

## C354 — sap-s-4hana-cloud-public-edition-convergent-invoicing-mds-5lp-453

Page: [[09-subscription-billing-and-contract-accounting/sap-s-4hana-cloud-public-edition-convergent-invoicing-mds-5lp-453]]

P-CLOUD_SUPPORT enrichment step opens product number P-CLOUD_COMM

**Status:** open — needs a human decision

## C355 — sap-s-4hana-cloud-public-edition-mds-5bd-427

Page: [[09-subscription-billing-and-contract-accounting/sap-s-4hana-cloud-public-edition-mds-5bd-427]]

Plant for R-SEATS in Germany given as 1010 while R-ONETIME and R-TRAFFIC use 10101; possible inconsistency within the document

**Status:** open — needs a human decision

## C356 — sap-s-4hana-cloud-public-edition-mds-5bd-427

Page: [[09-subscription-billing-and-contract-accounting/sap-s-4hana-cloud-public-edition-mds-5bd-427]]

Product ID for the pricing-scheme product appears as P-CLD_STORAGE_PCS in the overview table but P-CLOUD_STORAGE_PC in the procedures

**Status:** open — needs a human decision

## C357 — script-de-dados-mestre-criar-faturamento-convergente-de-produto-de-ass

Page: [[09-subscription-billing-and-contract-accounting/script-de-dados-mestre-criar-faturamento-convergente-de-produto-de-ass]]

Rate element R-TICKETS is created, but the price-calculation rate plan template and UsagePrice table refer to R-TRAFFIC

**Status:** open — needs a human decision

## C358 — script-de-dados-mestre-criar-faturamento-convergente-de-produto-de-ass

Page: [[09-subscription-billing-and-contract-accounting/script-de-dados-mestre-criar-faturamento-convergente-de-produto-de-ass]]

Product IDs written R_ONETIME/R_SEATS/R_TICKETS in headings but R-ONETIME/R-SEATS/R-TICKETS elsewhere

**Status:** open — needs a human decision

## C359 — script-de-dados-mestre-criar-faturamento-convergente-de-produto-de-ass

Page: [[09-subscription-billing-and-contract-accounting/script-de-dados-mestre-criar-faturamento-convergente-de-produto-de-ass]]

P-CLOUD_SUPPORT enrichment step 4 gives product number P-CLOUD_COMM

**Status:** open — needs a human decision

## C360 — script-de-dados-mestre-criar-faturamento-de-vendas-de-produto-de-assin

Page: [[09-subscription-billing-and-contract-accounting/script-de-dados-mestre-criar-faturamento-de-vendas-de-produto-de-assin]]

German plant for SBRE products is inconsistent inside the document: 10101 for R-ONETIME and R-TRAFFIC versus 1010 for R-SEATS.

**Status:** open — needs a human decision

## C361 — script-de-datos-maestros-creacion-de-facturacion-convergente-de-produc

Page: [[09-subscription-billing-and-contract-accounting/script-de-datos-maestros-creacion-de-facturacion-convergente-de-produc]]

Inconsistent IDs: rate element R-TICKETS is created but the price calculation plan template and usage lookup use R-TRAFFIC; headings use R_ONETIME/R_SEATS/R_TICKETS vs R-ONETIME.

**Status:** open — needs a human decision

## C362 — script-de-datos-maestros-creacion-de-facturacion-convergente-de-produc

Page: [[09-subscription-billing-and-contract-accounting/script-de-datos-maestros-creacion-de-facturacion-convergente-de-produc]]

P-CLOUD_SUPPORT SBPD step 4 enters product number P-CLOUD_COMM (likely copy error).

**Status:** open — needs a human decision

## C363 — script-de-datos-maestros-creacion-de-facturacion-convergente-de-produc

Page: [[09-subscription-billing-and-contract-accounting/script-de-datos-maestros-creacion-de-facturacion-convergente-de-produc]]

Usage lookup table steps select OneTimePrice instead of UsagePrice in step 3 and import.

**Status:** open — needs a human decision

## C364 — script-de-datos-maestros-creacion-de-facturacion-convergente-de-produc

Page: [[09-subscription-billing-and-contract-accounting/script-de-datos-maestros-creacion-de-facturacion-convergente-de-produc]]

Machine-translated text, tax classification note says 1 is full tax and 6 for Germany.

**Status:** open — needs a human decision

## C365 — script-de-datos-maestros-crear-facturacion-de-ventas-de-productos-de-s

Page: [[09-subscription-billing-and-contract-accounting/script-de-datos-maestros-crear-facturacion-de-ventas-de-productos-de-s]]

Germany plant for R-SEATS is given as 1010 whereas R-ONETIME and R-TRAFFIC use 10101

**Status:** open — needs a human decision

## C366 — stammdatenskript-abonnementprodukt-anlegen-convergent-invoicing-sds-5l

Page: [[09-subscription-billing-and-contract-accounting/stammdatenskript-abonnementprodukt-anlegen-convergent-invoicing-sds-5l]]

Product ID spellings differ within the document: R-ONETIME/R-SEATS/R-TICKETS vs R_ONETIME/R_SEATS/R_TICKETS, and R-TRAFFIC used in the PCS rate plan template and usage table where R-TICKETS is defined elsewhere.

**Status:** open — needs a human decision

## C367 — stammdatenskript-abonnementprodukt-anlegen-convergent-invoicing-sds-5l

Page: [[09-subscription-billing-and-contract-accounting/stammdatenskript-abonnementprodukt-anlegen-convergent-invoicing-sds-5l]]

P-CLOUD_SUPPORT enrichment steps instruct entering product number P-CLOUD_COMM; and the UsagePrice upload step selects OneTimePrice table instead of UsagePrice.

**Status:** open — needs a human decision

## C368 — stammdatenskript-abonnementprodukt-anlegen-convergent-invoicing-sds-5l

Page: [[09-subscription-billing-and-contract-accounting/stammdatenskript-abonnementprodukt-anlegen-convergent-invoicing-sds-5l]]

Rate plan template recurring fee priced in EUR while US country version uses USD elsewhere.

**Status:** open — needs a human decision

## C369 — stammdatenskript-abonnementprodukt-anlegen-sales-billing-sds-5bd-424

Page: [[09-subscription-billing-and-contract-accounting/stammdatenskript-abonnementprodukt-anlegen-sales-billing-sds-5bd-424]]

DE plant for R-ONETIME and R-TRAFFIC is given as 10101, but for R-SEATS as 1010; the document is internally inconsistent.

**Status:** open — needs a human decision

## C370 — stammdatenskript-abonnementprodukt-anlegen-sales-billing-sds-5bd-424

Page: [[09-subscription-billing-and-contract-accounting/stammdatenskript-abonnementprodukt-anlegen-sales-billing-sds-5bd-424]]

Intro table lists price calculation product P-CLD_STORAGE_PCS, but procedures create P-CLOUD_STORAGE_PC.

**Status:** open — needs a human decision

## C371 — stammdatenskript-abonnementprodukt-anlegen-sales-billing-sds-5bd-424

Page: [[09-subscription-billing-and-contract-accounting/stammdatenskript-abonnementprodukt-anlegen-sales-billing-sds-5bd-424]]

Rate plan template uses USD currency for the US version while the price for R-ONETIME is stated as 100 EUR.

**Status:** open — needs a human decision

## C372 — test-script-contract-accounting-daily-and-monthly-closing-2bk-ae-812

Page: [[09-subscription-billing-and-contract-accounting/test-script-contract-accounting-daily-and-monthly-closing-2bk-ae-812]]

Write-off workflow start condition is stated as write-off balance >= 2,000 AED, but the test activity says to post a write-off of a document total >= 3,000 AED to trigger it.

**Status:** open — needs a human decision

## C373 — test-script-contract-accounting-open-item-management-2uj-ae-872-part-0

Page: [[09-subscription-billing-and-contract-accounting/test-script-contract-accounting-open-item-management-2uj-ae-872-part-02]]

Initiator of Withdrawal code 5 is described as 'We Cancel the Promise' in Replace Promise to Pay but as 'Customer withdraws promise to pay' in Withdraw Promise to Pay; the same code carries two different meanings within this slice.

**Status:** open — needs a human decision

## C374 — test-script-sap-s-4hana-cloud-public-edition-contract-accounting-custo

Page: [[09-subscription-billing-and-contract-accounting/test-script-sap-s-4hana-cloud-public-edition-contract-accounting-custo-part-01]]

Document-change and document-reversal workflow sections contain wording copied from an Installment Plan workflow (e.g. 'workflow for Installment Plan creation is enabled', 'Confirm Installment Plan with Check Reason Installment Plan approve', 'Reject Installment Plan'), which does not match the document-change/reversal scenarios they describe.

**Status:** open — needs a human decision

## C375 — test-script-sap-s-4hana-cloud-public-edition-contract-accounting-custo

Page: [[09-subscription-billing-and-contract-accounting/test-script-sap-s-4hana-cloud-public-edition-contract-accounting-custo-part-01]]

Document-posting workflow threshold is stated as 'greater than or equal to = 30000 AED' in the step conditions but as 'Amount > 30000 AED' in the Post Document context.

**Status:** open — needs a human decision

## C376 — test-script-subscription-management-for-software-5sw-ae-sap-s-4hana-cl

Page: [[09-subscription-billing-and-contract-accounting/test-script-subscription-management-for-software-5sw-ae-sap-s-4hana-cl-part-01]]

Usage records app is named 'Manage Usage Records - Deprecated (F6802)' in the Overview Table but 'Manage Usage Records - Subscription Billing (F6802A)' in the test procedure.

**Status:** open — needs a human decision

## C377 — test-script-subscription-management-for-software-5sw-ae-sap-s-4hana-cl

Page: [[09-subscription-billing-and-contract-accounting/test-script-subscription-management-for-software-5sw-ae-sap-s-4hana-cl-part-01]]

Journal Entry Analyzer step says the split revenue is assigned to Product Area 02_COLLAB, while the material groups defined earlier are 02_CAD2 (CAD Add-on) and 03_COLLAB (Collaboration).

**Status:** open — needs a human decision

## C378 — central-procurement-with-sap-ariba-sourcing-4qn-test-script-sap-s-4han

Page: [[10-procurement/central-procurement-with-sap-ariba-sourcing-4qn-test-script-sap-s-4han]]

System Access row describes the hub as an SAP S/4HANA Cloud Public Edition system (1905 or higher) but the next sentence says an SAP S/4HANA Cloud Private Edition system acts as a hub when connected to multiple connected systems; the hub edition is stated inconsistently.

**Status:** open — needs a human decision

## C379 — complementary-procurement-functions-2tw-ae-test-script-sap-s-4hana-clo

Page: [[10-procurement/complementary-procurement-functions-2tw-ae-test-script-sap-s-4hana-clo]]

Serial-number invoice step uses Invoice Party 33300007, whereas the other invoice scripts and sample master data use supplier 33300001 (33300007 is not in the listed master data).

**Status:** open — needs a human decision

## C380 — consumable-purchasing-bnx-ae-test-script-sap-s-4hana-cloud-public-edit

Page: [[10-procurement/consumable-purchasing-bnx-ae-test-script-sap-s-4hana-cloud-public-edit]]

PO approval threshold: the flexible workflow configuration example uses total net amount greater than 10 AED for purchasing group 003, while the Create PO, Change PO and Approve PO steps say approval applies above 500 AED for purchasing group 003.

**Status:** open — needs a human decision

## C381 — consumable-purchasing-bnx-ae-test-script-sap-s-4hana-cloud-public-edit

Page: [[10-procurement/consumable-purchasing-bnx-ae-test-script-sap-s-4hana-cloud-public-edit]]

Option A/B labels are overloaded: in Create Supplier Invoice step 11, 'Optional A' (Post) leads to Release Blocked Invoice and 'Optional B' (Save as Completed) leads to 'Option A: Release Completed Supplier Invoice', while the invoice creation options A/B mean without/with invoice reduction and the release tables use Option A/B for two workflow sequences.

**Status:** open — needs a human decision

## C382 — direct-procurement-with-inbound-delivery-2tx-ae-test-script-sap-s-4han

Page: [[10-procurement/direct-procurement-with-inbound-delivery-2tx-ae-test-script-sap-s-4han]]

The supplier-confirmation approval workflow and its approval test step use supplier 10300003 and purchasing group 003, but the sample master data and every test step use suppliers 33300001/33300003 and purchasing group 002, so the approval workflow would not trigger on the script's own data.

**Status:** open — needs a human decision

## C383 — external-workforce-procurement-via-sap-fieldglass-22k-test-script-sap

Page: [[10-procurement/external-workforce-procurement-via-sap-fieldglass-22k-test-script-sap]]

Invite Supplier step searches supplier 10300090 while the master data table and other steps use supplier 10300080.

**Status:** open — needs a human decision

## C384 — external-workforce-procurement-via-sap-fieldglass-22k-test-script-sap

Page: [[10-procurement/external-workforce-procurement-via-sap-fieldglass-22k-test-script-sap]]

Invoice adjustment type is V0 in the master data table but the Accept Work Order step selects V1 (Invoice).

**Status:** open — needs a human decision

## C385 — procurement-of-materials-with-variant-configuration-2xu-ae-test-script

Page: [[10-procurement/procurement-of-materials-with-variant-configuration-2xu-ae-test-script]]

PO approval threshold is stated as total amount above 500 AED for purchasing group 003 in the PO and approval sections, but the configured test workflow uses total net amount greater than 5000 AED.

**Status:** open — needs a human decision

## C386 — procurement-of-materials-with-variant-configuration-2xu-ae-test-script

Page: [[10-procurement/procurement-of-materials-with-variant-configuration-2xu-ae-test-script]]

Variant condition PVA1 is created with absolute amounts 200 and 300 in the info record, but the PO step says PVA1 applies 20% and 30% added to the standard price.

**Status:** open — needs a human decision

## C387 — procurement-of-pipeline-materials-41f-ae-993

Page: [[10-procurement/procurement-of-pipeline-materials-41f-ae-993]]

Record Consumption purpose text says 'create an opportunity without a preceding document', which does not match the goods issue steps.

**Status:** open — needs a human decision

## C388 — purchasing-rebate-processing-2r7-ae-test-script-sap-s-4hana-cloud-publ

Page: [[10-procurement/purchasing-rebate-processing-2r7-ae-test-script-sap-s-4hana-cloud-publ]]

Process variant for different bases is created as ZP07 in the configuration chapter but later referred to as ZS09 in the Different Bases test procedure.

**Status:** open — needs a human decision

## C389 — sap-ariba-buying-4ai-1009

Page: [[10-procurement/sap-ariba-buying-4ai-1009]]

Overview table lists Process Purchase Requisitions - Deprecated (F1048) while the procedure uses Process Purchase Requisitions (Version 2) (F1048A)

**Status:** open — needs a human decision

## C390 — scheduling-agreements-in-procurement-bmr-ae-test-script-sap-s-4hana-cl

Page: [[10-procurement/scheduling-agreements-in-procurement-bmr-ae-test-script-sap-s-4hana-cl]]

The EDI goods receipt step posts to storage location 101C and Plant1DE, while the rest of the script uses plant 3310 (Plant 1 AE) and storage location 331C.

**Status:** open — needs a human decision

## C391 — test-script-automated-purchase-to-pay-with-sap-ariba-commerce-automati

Page: [[10-procurement/test-script-automated-purchase-to-pay-with-sap-ariba-commerce-automati]]

Approval threshold appears inconsistent within the document: the Approve Purchase Order section says POs of 500 USD or more require approval (Purchasing Groups 001 and 003), while the Configure Flexible Workflow step sets the release condition at total net amount greater than 100 AED for purchasing group 001.

**Status:** open — needs a human decision

## C392 — test-script-central-procurement-with-sap-business-network-for-procurem

Page: [[10-procurement/test-script-central-procurement-with-sap-business-network-for-procurem]]

Overview Table lists 'Approve Central Supplier Confirmation (Optional)' as role Warehouse Clerk with app Post Goods Receipt for Inbound Delivery (F2502), while the test procedure for that step uses the Purchasing Manager role and My Inbox - All Items (F6012).

**Status:** open — needs a human decision

## C393 — test-script-central-procurement-with-sap-business-network-for-procurem

Page: [[10-procurement/test-script-central-procurement-with-sap-business-network-for-procurem]]

Purchase order approval threshold differs: the Approve Purchase Order note says orders of 500 USD or more need approval (purchasing groups 001 and 003), while the sample flexible workflow starts for purchasing group 001 with total net amount greater than 100 EUR.

**Status:** open — needs a human decision

## C394 — test-script-central-procurement-with-sap-business-network-for-procurem

Page: [[10-procurement/test-script-central-procurement-with-sap-business-network-for-procurem]]

Sample master data lists material TG001, but the Create Purchase Order step enters material SP001, which is not in the master data table.

**Status:** open — needs a human decision

## C395 — test-script-central-requisitioning-1xi-sap-s-4hana-cloud-public-editio

Page: [[10-procurement/test-script-central-requisitioning-1xi-sap-s-4hana-cloud-public-editio]]

Post Goods Issue for Reservation, Case 1 (SAP ERP): step 1 names role Accounts Payable Accountant and step 2 is titled 'Create Credit Memo' with expected result 'Credit Memo is created', although the step is a MIGO goods issue; Overview Table 4 and Case 2 give the role as Warehouse Clerk.

**Status:** open — needs a human decision

## C396 — test-script-central-requisitioning-1xi-sap-s-4hana-cloud-public-editio

Page: [[10-procurement/test-script-central-requisitioning-1xi-sap-s-4hana-cloud-public-editio]]

Overview Tables 3 and 4 list apps 'Create Purchase Requisition - Deprecated (F1643)' and 'My Purchase Requisitions - Deprecated (F1639)', while the procedures use My Purchase Requisitions (F1643A); My Inbox - All Items is F0862 in the approval chapter but F5331 in the rework chapter.

**Status:** open — needs a human decision

## C397 — test-script-central-requisitioning-1xi-sap-s-4hana-cloud-public-editio

Page: [[10-procurement/test-script-central-requisitioning-1xi-sap-s-4hana-cloud-public-editio]]

Rework Purchase Requisition step 3 (Request Rework) gives expected result 'The Purchase Requisition is approved', whereas the text after the table says the status becomes 'Awaiting Approval-Rework Required'.

**Status:** open — needs a human decision

## C398 — test-script-central-sourcing-3zf-sap-s-4hana-cloud-public-edition-990

Page: [[10-procurement/test-script-central-sourcing-3zf-sap-s-4hana-cloud-public-edition-990]]

Scenario 2 enters Purchasing Organization 1000 whereas the RFQ and contract steps and sample data use organization 1010

**Status:** open — needs a human decision

## C399 — test-script-contract-management-with-sap-ariba-contracts-4az-ae-1014

Page: [[10-procurement/test-script-contract-management-with-sap-ariba-contracts-4az-ae-1014]]

Step 3 and 4 name the supplier/template 'SAP S/4HANA Cloud Private Edition' within a Public Edition script; the doc says the name is example/configuration dependent

**Status:** open — needs a human decision

## C400 — test-script-cross-company-purchasing-organization-2r3-ae-854

Page: [[10-procurement/test-script-cross-company-purchasing-organization-2r3-ae-854]]

Purchase order value limit is 'less than 500 AED' in the within-country scenario but 'less than 500 USD' in the across-countries scenario, although the PO currency is AED in both.

**Status:** open — needs a human decision

## C401 — test-script-mrp-change-request-integration-with-sap-business-network-6

Page: [[10-procurement/test-script-mrp-change-request-integration-with-sap-business-network-6]]

The Clear PIRs procedure says 'If a PIR exists, you completed this procedure already' and only continues to clear PIRs (set to 0) when no PIR exists, which inverts the stated purpose of clearing existing PIRs.

**Status:** open — needs a human decision

## C402 — test-script-procurement-for-service-management-3ni-ae-964

Page: [[10-procurement/test-script-procurement-for-service-management-3ni-ae-964]]

Option C (external workforce PO conversion) uses Supplier 10300001 and Purch. Org. 1010, whereas the stated master data and all other steps use supplier 33300001 and org 3310.

**Status:** open — needs a human decision

## C403 — test-script-procurement-of-production-components-consumer-products-5w3

Page: [[10-procurement/test-script-procurement-of-production-components-consumer-products-5w3]]

Approve Purchase Requisition says PRs need approval when total > 500 AED and purchase group 002, but the PR workflow is configured with net amount >= 10 AED.

**Status:** open — needs a human decision

## C404 — test-script-procurement-of-production-components-consumer-products-5w3

Page: [[10-procurement/test-script-procurement-of-production-components-consumer-products-5w3]]

Approve Purchase Order says POs need approval when total > 500 AED and purchase group is 001, but the PO workflow and manual PO note use purchasing group 002.

**Status:** open — needs a human decision

## C405 — test-script-procurement-of-production-components-consumer-products-5w3

Page: [[10-procurement/test-script-procurement-of-production-components-consumer-products-5w3]]

Storage location 331C is used in PO, goods receipt and stock steps but the organization data lists only 331A, 331B and 331R.

**Status:** open — needs a human decision

## C406 — test-script-procurement-of-services-22z-ae-sap-s-4hana-cloud-public-ed

Page: [[10-procurement/test-script-procurement-of-services-22z-ae-sap-s-4hana-cloud-public-ed]]

Prelim step Configure Flexible Workflow for Purchase Order sets condition total net amount greater than 10 AED for group 003, while later PO approval steps state 500 AED or more requires approval.

**Status:** open — needs a human decision

## C407 — test-script-procurement-of-services-22z-ae-sap-s-4hana-cloud-public-ed

Page: [[10-procurement/test-script-procurement-of-services-22z-ae-sap-s-4hana-cloud-public-ed]]

Prelim step Configure Flexible Workflow for Service Entry Sheets enters Amount 10 AED (and expected result says greater than 10), while workflow name and later approval tables state 1000 AED.

**Status:** open — needs a human decision

## C408 — test-script-procurement-of-services-22z-ae-sap-s-4hana-cloud-public-ed

Page: [[10-procurement/test-script-procurement-of-services-22z-ae-sap-s-4hana-cloud-public-ed]]

Case 4 convert PR to PO uses Supplier 10300001 and Purchasing Organization 1010, differing from sample data (supplier 33300001, org 3310).

**Status:** open — needs a human decision

## C409 — test-script-purchase-contract-bmd-ae-sap-s-4hana-cloud-public-edition

Page: [[10-procurement/test-script-purchase-contract-bmd-ae-sap-s-4hana-cloud-public-edition]]

Approval threshold currency differs inside the document: the example flexible workflow start condition is 'greater than 2000 EUR' while the approval procedure says 'greater than 2000 AED'.

**Status:** open — needs a human decision

## C410 — test-script-purchase-contract-bmd-ae-sap-s-4hana-cloud-public-edition

Page: [[10-procurement/test-script-purchase-contract-bmd-ae-sap-s-4hana-cloud-public-edition]]

Reference purchasing organization example values are inconsistent: the mapping step maps 3310 to a reference org (example 1410), the supplier extension step uses 1710, yet the Create Reference Purchase Contract and hierarchy-contract steps give the reference purchase organization as 'for example 3310'.

**Status:** open — needs a human decision

## C411 — test-script-purchase-contract-bmd-ae-sap-s-4hana-cloud-public-edition

Page: [[10-procurement/test-script-purchase-contract-bmd-ae-sap-s-4hana-cloud-public-edition]]

The Overview Table lists 'Process Purchase Requisitions - Deprecated (F1048)' for creating a contract from a requisition while the procedure uses Process Purchase Requisitions (F1048A); it also lists the Purchaser as role for the versioning Approve Purchase Contract steps whereas the referenced procedure is performed by the Purchasing Manager.

**Status:** open — needs a human decision

## C412 — test-script-real-time-reporting-and-monitoring-for-procurement-1ji-729

Page: [[10-procurement/test-script-real-time-reporting-and-monitoring-for-procurement-1ji-729]]

Procurement Overview Page Hide Cards steps place the user icon at the top left in Table 1 but at the top right in Table 3 of the same document.

**Status:** open — needs a human decision

## C413 — test-script-requisitioning-18j-ae-sap-s-4hana-cloud-public-edition-705

Page: [[10-procurement/test-script-requisitioning-18j-ae-sap-s-4hana-cloud-public-edition-705]]

Rework Purchase Requisition step 3 (Request Rework) lists the expected result as 'The Purchase Requisition is approved', which contradicts the rework action.

**Status:** open — needs a human decision

## C414 — test-script-requisitioning-18j-ae-sap-s-4hana-cloud-public-edition-705

Page: [[10-procurement/test-script-requisitioning-18j-ae-sap-s-4hana-cloud-public-edition-705]]

Multiple account assignment test uses cost center 33101401, which is not in the sample master data list (33101101 and 33101501) nor in the cost center update step (33101101, 33101501).

**Status:** open — needs a human decision

## C415 — test-script-sap-s-4hana-cloud-public-edition-central-purchase-contract

Page: [[10-procurement/test-script-sap-s-4hana-cloud-public-edition-central-purchase-contract]]

Scenario titles say 'central quantity contract' (Table 5 Scenario 4 material unknown; Table 9 Scenario 1 free text) but their step 4 enters Contract Type: Value Contract.

**Status:** open — needs a human decision

## C416 — test-script-sap-s-4hana-cloud-public-edition-central-purchase-contract

Page: [[10-procurement/test-script-sap-s-4hana-cloud-public-edition-central-purchase-contract]]

Flexible Distribution is described as allowing 'more or less than 100%' distribution in the first scenario but 'more than 100%' in the later scenarios and hierarchy creation.

**Status:** open — needs a human decision

## C417 — test-script-sap-s-4hana-cloud-public-edition-procurement-of-direct-mat

Page: [[10-procurement/test-script-sap-s-4hana-cloud-public-edition-procurement-of-direct-mat]]

Workflow start-condition amounts differ across sections (example 10 AED, 50,000 AED, 500,00 AED) while the PO approval step states approval applies above 500 AED for purchasing group 003; they are examples but may be inconsistent.

**Status:** open — needs a human decision

## C418 — test-script-scheduling-agreement-for-consignment-procurement-2ny-ae-sa

Page: [[10-procurement/test-script-scheduling-agreement-for-consignment-procurement-2ny-ae-sa]]

The Overview Table's Expected Results appear offset from the procedures: Approve Scheduling Agreement shows 'Schedule Agreements are changed', Maintain Delivery Schedule shows 'A Scheduling Agreement is approved' and Print Scheduling Agreement shows 'A Delivery Schedule is created', which do not match those procedure sections.

**Status:** open — needs a human decision

## C419 — test-script-scheduling-agreement-for-consignment-procurement-2ny-ae-sa

Page: [[10-procurement/test-script-scheduling-agreement-for-consignment-procurement-2ny-ae-sa]]

Evaluate the Stock/Requirement Situation step 4 states both the ON and OFF positions of the Check Material Coverage - Old Version (F0251) toggle navigate to F0251, so the ON/OFF distinction is contradictory.

**Status:** open — needs a human decision

## C420 — test-script-scheduling-agreement-for-subcontracting-procurement-2nx-ae

Page: [[10-procurement/test-script-scheduling-agreement-for-subcontracting-procurement-2nx-ae]]

Overview Table lists Part 1 Create Supplier Invoice as 'Create Supplier Invoice - Advanced (MIRO)', but the test procedure uses Create Supplier Invoice (F0859).

**Status:** open — needs a human decision

## C421 — test-script-scheduling-agreement-for-subcontracting-procurement-2nx-ae

Page: [[10-procurement/test-script-scheduling-agreement-for-subcontracting-procurement-2nx-ae]]

Overview Table assigns Evaluate Stock Requirement Situation to app Manage Material Coverage - New Version (F0251A), but the procedure opens Monitor Material Coverage - Net / Individual Segments (F2101A) and then navigates to F0251A or F0251 depending on a toggle.

**Status:** open — needs a human decision

## C422 — test-script-scheduling-agreement-for-subcontracting-procurement-2nx-ae

Page: [[10-procurement/test-script-scheduling-agreement-for-subcontracting-procurement-2nx-ae]]

Overview Table gives the Production Planner role for Print Scheduling Agreement, but the procedure logs on as Purchaser.

**Status:** open — needs a human decision

## C423 — test-script-service-procurement-with-sap-business-network-and-sap-fiel

Page: [[10-procurement/test-script-service-procurement-with-sap-business-network-and-sap-fiel]]

PO approval threshold is inconsistent within the document: workflow set-up uses total net amount greater than 100 EUR, while the approval step states POs of 500 USD or more require approval (purchasing groups 001 and 003).

**Status:** open — needs a human decision

## C424 — test-script-sourcing-with-sap-ariba-sourcing-4bl-ae-sap-s-4hana-cloud

Page: [[10-procurement/test-script-sourcing-with-sap-ariba-sourcing-4bl-ae-sap-s-4hana-cloud]]

Overview Table lists Manage RFQs (F2049) as the app for displaying the automatically created supplier quotation, but the test procedure for that step uses Manage Supplier Quotations (F1991).

**Status:** open — needs a human decision

## C425 — test-script-subcontracting-bmy-ae-sap-s-4hana-cloud-public-edition-129

Page: [[10-procurement/test-script-subcontracting-bmy-ae-sap-s-4hana-cloud-public-edition-129]]

Overview Table app names differ from the procedures: it lists 'Process Purchase Requisitions - Deprecated (F1048)' (procedure uses F1048A), ME2ON for Part 1 Create Outbound Delivery (procedure uses Subcontracting Cockpit F2948), and 'Create Supplier Invoice - Advanced (MIRO)' for Part 1 (procedure uses Create Supplier Invoice F0859).

**Status:** open — needs a human decision

## C426 — test-script-subcontracting-bmy-ae-sap-s-4hana-cloud-public-edition-129

Page: [[10-procurement/test-script-subcontracting-bmy-ae-sap-s-4hana-cloud-public-edition-129]]

Approval threshold wording is inconsistent: the note says only POs 'higher than 500.00 AED' can be released, while the expected result says POs with a net value of '500 AED or more' have status In Approval.

**Status:** open — needs a human decision

## C427 — test-script-subcontracting-consumer-products-5w4-ae-sap-s-4hana-cloud

Page: [[10-procurement/test-script-subcontracting-consumer-products-5w4-ae-sap-s-4hana-cloud]]

Purchase order approval threshold is worded inconsistently: 'higher than 500.00 AED' in the note versus 'net value of 500 AED or more' in the expected result of the approval step.

**Status:** open — needs a human decision

## C428 — test-script-supplier-consignment-2lg-ae-sap-s-4hana-cloud-public-editi

Page: [[10-procurement/test-script-supplier-consignment-2lg-ae-sap-s-4hana-cloud-public-editi]]

Approve Purchase Order step cites app My Inbox - All Items as F5331 in the Overview Table but F0862 in the test procedure.

**Status:** open — needs a human decision

## C429 — test-script-supplier-evaluation-and-performance-monitoring-sl4-ae-sap

Page: [[10-procurement/test-script-supplier-evaluation-and-performance-monitoring-sl4-ae-sap]]

Create Supplier Evaluation Weighting and Scoring step 3 says total weighting should be 100%, but its example values (Inspection Lot 10, Quantity 20, Time 20, Price 20, Questionnaire 10, Quality Notification 10, Return Delivery 4, Reasonable Discounts 5, PPM 5) add up to 104%.

**Status:** open — needs a human decision

## C430 — test-script-supply-chain-automation-with-sap-business-network-5i2-ae-1

Page: [[10-procurement/test-script-supply-chain-automation-with-sap-business-network-5i2-ae-1]]

Multi-tier overview table lists Approve Purchase Order under role Purchaser, while the procedure and the other scenarios use Purchasing Manager.

**Status:** open — needs a human decision

## C431 — test-script-supply-chain-automation-with-sap-business-network-5i2-ae-1

Page: [[10-procurement/test-script-supply-chain-automation-with-sap-business-network-5i2-ae-1]]

Multi-tier overview table lists Create Purchase Order via ME21N, but the detailed procedure creates the PO in Manage Purchase Orders (F0842A) and uses ME21N only for an optional step.

**Status:** open — needs a human decision

## C432 — test-script-supply-chain-automation-with-sap-business-network-5i2-ae-1

Page: [[10-procurement/test-script-supply-chain-automation-with-sap-business-network-5i2-ae-1]]

Subcontracting without serial numbers overview table omits several procedure steps (create/change outbound delivery) and references inconsistent page numbers, so overview and detailed procedures may differ in scope.

**Status:** open — needs a human decision

## C433 — manual-transportation-planning-6w2-ae-test-script-sap-s-4hana-cloud-pu

Page: [[11-inventory-warehouse-and-transportation/manual-transportation-planning-6w2-ae-test-script-sap-s-4hana-cloud-pu]]

The AE script's rail and ocean planning sections use US sample data (source SP_1710, carriers 17386xxx, purchasing org 1710) while road and air use AE data (SP_3310, 33386xxx, org 3310); air main carriage lists carrier 10386502 versus 33386502 in the master data table.

**Status:** open — needs a human decision

## C434 — master-data-script-create-carrier-master-mds-4de-407

Page: [[11-inventory-warehouse-and-transportation/master-data-script-create-carrier-master-mds-4de-407]]

Overview Table lists only the Road invoice verification segment although ten procedures exist; the introduction mentions a Self-Billing Process while sections are titled ERS

**Status:** open — needs a human decision

## C435 — master-data-script-create-carrier-master-mds-4de-407

Page: [[11-inventory-warehouse-and-transportation/master-data-script-create-carrier-master-mds-4de-407]]

Step 4 instructs a grouping of 'External alpha-numeric numbering' but the example uses External numeric numbering (BP03) with numeric IDs

**Status:** open — needs a human decision

## C436 — master-data-script-create-carrier-master-mds-4de-407

Page: [[11-inventory-warehouse-and-transportation/master-data-script-create-carrier-master-mds-4de-407]]

Purchasing Data field is named differently across variants (AutoEvalGRSetmt Del, AutoEvalGRSetmt Del to Eval. Receipt Settlement, Eval Receipt Settlement)

**Status:** open — needs a human decision

## C437 — master-data-script-create-freight-agreement-mds-3tl-sap-s-4hana-cloud

Page: [[11-inventory-warehouse-and-transportation/master-data-script-create-freight-agreement-mds-3tl-sap-s-4hana-cloud]]

Some table and step references are inconsistent inside the doc (duplicate table numbering, 'S005'/'S003' vs 'SO05'/'SO03', 'see tables 8, 9 in Step 12').

**Status:** open — needs a human decision

## C438 — master-data-script-create-freight-agreement-mds-3tl-sap-s-4hana-cloud

Page: [[11-inventory-warehouse-and-transportation/master-data-script-create-freight-agreement-mds-3tl-sap-s-4hana-cloud]]

Step 12 of the road script mentions switching to role Transportation Manager for Manage Rate Tables, while the rest uses Freight Contract Specialist.

**Status:** open — needs a human decision

## C439 — master-data-script-create-freight-agreement-mds-3tl-sap-s-4hana-cloud

Page: [[11-inventory-warehouse-and-transportation/master-data-script-create-freight-agreement-mds-3tl-sap-s-4hana-cloud]]

Section 3 Overview names role 'Freight Contract Specialist' whereas role template table lists 'Contract Specialist - Freight Management'.

**Status:** open — needs a human decision

## C440 — master-data-script-create-freight-agreement-mds-3tl-sap-s-4hana-cloud

Page: [[11-inventory-warehouse-and-transportation/master-data-script-create-freight-agreement-mds-3tl-sap-s-4hana-cloud]]

Some rate values in rail Carrier4 return-to-supplier and consignment tables repeat road values (STR vehicle types) rather than rail values.

**Status:** open — needs a human decision

## C441 — mds-4de-master-data-script-create-carrier-master-409

Page: [[11-inventory-warehouse-and-transportation/mds-4de-master-data-script-create-carrier-master-409]]

Step 9 supplier FI role is FLVN01 in invoice verification procedures but FLVN00 in ERS procedures; may be an inconsistency within the document.

**Status:** open — needs a human decision

## C442 — sap-ewm-integration-delivery-based-production-integration-2vm-ae-test

Page: [[11-inventory-warehouse-and-transportation/sap-ewm-integration-delivery-based-production-integration-2vm-ae-test]]

Check Stock Situation tells the tester to check stock in storage location 331B, while every other step (control cycle, release, staging, goods issue check) uses storage location 333S as the production supply location.

**Status:** open — needs a human decision

## C443 — sap-ewm-integration-delivery-based-production-integration-2vm-ae-test

Page: [[11-inventory-warehouse-and-transportation/sap-ewm-integration-delivery-based-production-integration-2vm-ae-test]]

The Overview Table assigns Confirm Production Order Operation (CO11N) to Production Operator - Discrete Manufacturing, but the procedure section logs on as Production Supervisor - Discrete Manufacturing and opens Confirm Production Operation (F3069).

**Status:** open — needs a human decision

## C444 — sap-ewm-integration-delivery-based-production-integration-2vm-ae-test

Page: [[11-inventory-warehouse-and-transportation/sap-ewm-integration-delivery-based-production-integration-2vm-ae-test]]

The Overview Table lists Maintain PIRs (F3445) for creating planned independent requirements, while the procedure opens Manage PIRs (Obsolete) - Replaced by Maintain PIRs (F1079).

**Status:** open — needs a human decision

## C445 — sap-ewm-integration-inbound-processing-from-supplier-2vj-ae-test-scrip

Page: [[11-inventory-warehouse-and-transportation/sap-ewm-integration-inbound-processing-from-supplier-2vj-ae-test-scrip]]

The Overview Table expects the material document Storage Location to be 'EWM Int ROD 103D', while the Check Material Document procedure expects Receiving Storage Location 'EWM Int AFS 333S' (and the sample data lists 333D and 333S, not 103D).

**Status:** open — needs a human decision

## C446 — sap-s-4hana-cloud-public-edition-mds-3tl-367

Page: [[11-inventory-warehouse-and-transportation/sap-s-4hana-cloud-public-edition-mds-3tl-367]]

SF00 rate tables are concatenated in the extraction, so individual rate values are hard to read; verify against the source before citing them.

**Status:** open — needs a human decision

## C447 — sap-s-4hana-cloud-public-edition-mds-3tl-367

Page: [[11-inventory-warehouse-and-transportation/sap-s-4hana-cloud-public-edition-mds-3tl-367]]

Document has some internal numbering inconsistencies (e.g. step numbers missing, table numbering 42-65 in rail section, S005 vs SO05 naming, SG02 referenced twice for SG04, SG110 vs SG11).

**Status:** open — needs a human decision

## C448 — sap-s-4hana-cloud-public-edition-mds-3tl-367

Page: [[11-inventory-warehouse-and-transportation/sap-s-4hana-cloud-public-edition-mds-3tl-367]]

Carrier 1 for air uses 17386401 (same ID as sea carrier 1) and carrier 2 for air uses 17386402 (same as sea carrier 2), which may be intentional reuse or a copy error.

**Status:** open — needs a human decision

## C449 — sap-s-4hana-cloud-public-edition-mds-3tl-369

Page: [[11-inventory-warehouse-and-transportation/sap-s-4hana-cloud-public-edition-mds-3tl-369]]

Document is an unreviewed machine translation into Chinese; terminology and some table fragments are garbled or inconsistent (e.g. SO05/S005, SG02 referenced twice for SG04, table numbering restarts).

**Status:** open — needs a human decision

## C450 — sap-s-4hana-cloud-public-edition-mds-3tl-369

Page: [[11-inventory-warehouse-and-transportation/sap-s-4hana-cloud-public-edition-mds-3tl-369]]

Rate values and charge-type example amounts differ between Carrier1 and Carrier2 variants by design; other-language versions of the same script may differ in details.

**Status:** open — needs a human decision

## C451 — script-de-dados-mestre-criar-acordo-de-frete-mds-3tl-368

Page: [[11-inventory-warehouse-and-transportation/script-de-dados-mestre-criar-acordo-de-frete-mds-3tl-368]]

Internal inconsistencies: some step descriptions reference wrong table numbers and the document says rail/air agents sometimes as 'transportadora' vs 'agente de frete'; carrier ID 17386401 is used for both sea FA 1 and air FA 1, and 17386402 for both sea FA 2 and air FA 2.

**Status:** open — needs a human decision

## C452 — script-de-dados-mestre-criar-acordo-de-frete-mds-3tl-368

Page: [[11-inventory-warehouse-and-transportation/script-de-dados-mestre-criar-acordo-de-frete-mds-3tl-368]]

Document is Portuguese (PT) translation and contains untranslated or inconsistent step numbering (many steps unnumbered).

**Status:** open — needs a human decision

## C453 — script-de-dados-mestre-criar-mestre-de-transportadoras-mds-4de-410

Page: [[11-inventory-warehouse-and-transportation/script-de-dados-mestre-criar-mestre-de-transportadoras-mds-4de-410]]

Last air carrier section is titled FAEM but its objective and variants refer to LAEM; naming LAEM vs FAEM is inconsistent across sections.

**Status:** open — needs a human decision

## C454 — script-de-dados-mestre-criar-mestre-de-transportadoras-mds-4de-410

Page: [[11-inventory-warehouse-and-transportation/script-de-dados-mestre-criar-mestre-de-transportadoras-mds-4de-410]]

Example data uses US localisation inside a Portuguese-language script; section 4.1 mentions BP numbering 'alfanumérica externa' while the example uses numeric BP03.

**Status:** open — needs a human decision

## C455 — script-de-dados-mestre-criar-mestre-de-transportadoras-mds-4de-410

Page: [[11-inventory-warehouse-and-transportation/script-de-dados-mestre-criar-mestre-de-transportadoras-mds-4de-410]]

Overview table lists only the first segment (road, invoice review) while ten procedures exist.

**Status:** open — needs a human decision

## C456 — script-de-datos-maestros-creacion-de-acuerdo-de-flete-mds-3tl-366

Page: [[11-inventory-warehouse-and-transportation/script-de-datos-maestros-creacion-de-acuerdo-de-flete-mds-3tl-366]]

Carrier ID 17386401 is given both for sea carrier 1 and for air carrier 1, and 17386402 for sea carrier 2 and air carrier 2; possible copy/paste error or intentional reuse.

**Status:** open — needs a human decision

## C457 — script-de-datos-maestros-creacion-de-acuerdo-de-flete-mds-3tl-366

Page: [[11-inventory-warehouse-and-transportation/script-de-datos-maestros-creacion-de-acuerdo-de-flete-mds-3tl-366]]

Automatic translation warning: wording may be inaccurate; some charge type codes appear inconsistently (SO05 vs S005, S003 vs SO03) and table numbering is inconsistent.

**Status:** open — needs a human decision

## C458 — script-de-datos-maestros-creacion-de-acuerdo-de-flete-mds-3tl-366

Page: [[11-inventory-warehouse-and-transportation/script-de-datos-maestros-creacion-de-acuerdo-de-flete-mds-3tl-366]]

Road/rail sections state some steps refer to 'step 12 tables 8 and 9' which do not match the actual table numbering; step numbers are blank in several sections.

**Status:** open — needs a human decision

## C459 — script-de-datos-maestros-creacion-de-maestro-de-transportistas-mds-4de

Page: [[11-inventory-warehouse-and-transportation/script-de-datos-maestros-creacion-de-maestro-de-transportistas-mds-4de]]

Machine-translated text has inconsistencies (e.g., 'Interlocutor comercial' vs 'socio comercial', untranslated 'Change in BP Role'); step 4 says alphanumeric external numbering while examples use numeric BP03.

**Status:** open — needs a human decision

## C460 — script-de-datos-maestros-creacion-de-maestro-de-transportistas-mds-4de

Page: [[11-inventory-warehouse-and-transportation/script-de-datos-maestros-creacion-de-maestro-de-transportistas-mds-4de]]

Org-unit table in prerequisites is empty and summary table lists only the first procedure.

**Status:** open — needs a human decision

## C461 — stammdatenskript-lieferplan-anlegen-sds-3tl-sap-s-4hana-cloud-public-e

Page: [[11-inventory-warehouse-and-transportation/stammdatenskript-lieferplan-anlegen-sds-3tl-sap-s-4hana-cloud-public-e]]

Document is in German; the title extracted as 'Zweck' but the real title is 'Lieferplan anlegen – SDS (3TL)' while content actually describes freight agreements (Frachtvereinbarungen), so the title looks mismatched.

**Status:** open — needs a human decision

## C462 — stammdatenskript-lieferplan-anlegen-sds-3tl-sap-s-4hana-cloud-public-e

Page: [[11-inventory-warehouse-and-transportation/stammdatenskript-lieferplan-anlegen-sds-3tl-sap-s-4hana-cloud-public-e]]

Internal inconsistencies: carrier labelling alternates between Spediteur and Frachtführer; some sections refer to an SG04/SG02 table numbering that does not match; table numbering is duplicated; the cross-company sea section refers to a road chapter 'Spediteur1 - Straße' for post-carriage.

**Status:** open — needs a human decision

## C463 — stammdatenskript-lieferplan-anlegen-sds-3tl-sap-s-4hana-cloud-public-e

Page: [[11-inventory-warehouse-and-transportation/stammdatenskript-lieferplan-anlegen-sds-3tl-sap-s-4hana-cloud-public-e]]

Tariff values for carrier 2 differ by small increments from carrier 1; the road SO05 table is labelled S005/SOS005 in places (likely typo for SO05).

**Status:** open — needs a human decision

## C464 — stammdatenskript-spediteurstamm-anlegen-sds-4de-406

Page: [[11-inventory-warehouse-and-transportation/stammdatenskript-spediteurstamm-anlegen-sds-4de-406]]

Step 4 of the road invoice-verification script says grouping 'externe alphanumerische Nummerierung' but samples use BP03 (external numeric).

**Status:** open — needs a human decision

## C465 — stammdatenskript-spediteurstamm-anlegen-sds-4de-406

Page: [[11-inventory-warehouse-and-transportation/stammdatenskript-spediteurstamm-anlegen-sds-4de-406]]

Step 6 expected-result wording is inconsistent: ERS scripts say Rolle 'Spediteur' wird hinzugefügt vs 'Frachtführer' in the road ERS script; the ERS checkbox label also varies across scripts.

**Status:** open — needs a human decision

## C466 — stammdatenskript-spediteurstamm-anlegen-sds-4de-406

Page: [[11-inventory-warehouse-and-transportation/stammdatenskript-spediteurstamm-anlegen-sds-4de-406]]

Overview table lists only the road invoice-verification segment although 10 segments are described; Zweck mentions only Frachtführer.

**Status:** open — needs a human decision

## C467 — stammdatenskript-spediteurstamm-anlegen-sds-4de-406

Page: [[11-inventory-warehouse-and-transportation/stammdatenskript-spediteurstamm-anlegen-sds-4de-406]]

Document title 'Zweck' in the extraction is a heading, not the real title; also the German text mentions a 'Materialstammdatensatz' for a business partner.

**Status:** open — needs a human decision

## C468 — test-script-intercompany-stock-transfer-1p9-ae-sap-s-4hana-cloud-publi

Page: [[11-inventory-warehouse-and-transportation/test-script-intercompany-stock-transfer-1p9-ae-sap-s-4hana-cloud-publi]]

Appendix scheduled delivery job uses Shipping Point 3320, while the master data and the manual delivery creation (VL10B) for the domestic supplying side use Shipping Point 3330 (3320 is listed only as a company code).

**Status:** open — needs a human decision

## C469 — test-script-intercompany-stock-transfer-1p9-ae-sap-s-4hana-cloud-publi

Page: [[11-inventory-warehouse-and-transportation/test-script-intercompany-stock-transfer-1p9-ae-sap-s-4hana-cloud-publi]]

The International 'Post Goods Receipt for Inbound Delivery' step uses app F0843 in the test steps and overview table, while the same step in the Domestic flow uses VL06IG.

**Status:** open — needs a human decision

## C470 — test-script-intercompany-stock-transfer-returns-2ts-ae-sap-s-4hana-clo

Page: [[11-inventory-warehouse-and-transportation/test-script-intercompany-stock-transfer-returns-2ts-ae-sap-s-4hana-clo]]

Appendix job scheduling uses Shipping Point 3320, while the main procedure uses Shipping Point 3310 (and the master data lists shipping points 3310331R and 3330333R, none being 3320; 3320 is a company code).

**Status:** open — needs a human decision

## C471 — test-script-intercompany-stock-transfer-returns-2ts-ae-sap-s-4hana-clo

Page: [[11-inventory-warehouse-and-transportation/test-script-intercompany-stock-transfer-returns-2ts-ae-sap-s-4hana-clo]]

Purpose says the process returns material 'within the same country', yet the document also has an International section (US company code 1710); the Domestic master data is described as 'within Germany' and uses German tax code V1 as an example, while the org units are labelled AE and the currency is AED.

**Status:** open — needs a human decision

## C472 — test-script-intercompany-stock-transfer-returns-2ts-ae-sap-s-4hana-clo

Page: [[11-inventory-warehouse-and-transportation/test-script-intercompany-stock-transfer-returns-2ts-ae-sap-s-4hana-clo]]

The optional flexible workflow example uses purchasing group 003 as precondition, while the test returns STO is created with purchasing group 002, so the example workflow would not apply to the test order.

**Status:** open — needs a human decision

## C473 — test-script-quality-management-in-warehousing-3m0-ae-sap-s-4hana-cloud

Page: [[11-inventory-warehouse-and-transportation/test-script-quality-management-in-warehousing-3m0-ae-sap-s-4hana-cloud]]

Warehouse number in RF steps differs: production-flow RF steps use Whse No 1750, supplier-flow RF steps use 3350, and the sample data lists EWM warehouse 3350 (ERP warehouse 335).

**Status:** open — needs a human decision

## C474 — test-script-quality-management-in-warehousing-3m0-ae-sap-s-4hana-cloud

Page: [[11-inventory-warehouse-and-transportation/test-script-quality-management-in-warehousing-3m0-ae-sap-s-4hana-cloud]]

Storage location differs: sample data and business conditions use 335W, but the synchronous goods receipt (MIGO) steps tell the tester to check storage location 105W (and optional 105I).

**Status:** open — needs a human decision

## C475 — test-script-quality-management-in-warehousing-3m0-ae-sap-s-4hana-cloud

Page: [[11-inventory-warehouse-and-transportation/test-script-quality-management-in-warehousing-3m0-ae-sap-s-4hana-cloud]]

Production-flow handling unit steps refer to materials SG124 and FG228, while the sample data table lists SG29 for the production flow and the supplier flow uses TG21 although sample data lists QM001.

**Status:** open — needs a human decision

## C476 — test-script-sap-ewm-integration-batch-management-2vn-ae-sap-s-4hana-cl

Page: [[11-inventory-warehouse-and-transportation/test-script-sap-ewm-integration-batch-management-2vn-ae-sap-s-4hana-cl]]

Post Goods Receipt in SAP EWM (both options) uses Warehouse No. 1730, Goods Receipt Office YWAREHOUSE-1730 and Ent. to Dispose 17411710, whereas the sample data and the Option 2 batch-creation step use EWM warehouse 3330 (YWAREHOUSE-3310, 33413310) and the stock checks use 3330.

**Status:** open — needs a human decision

## C477 — test-script-sap-ewm-integration-batch-management-2vn-ae-sap-s-4hana-cl

Page: [[11-inventory-warehouse-and-transportation/test-script-sap-ewm-integration-batch-management-2vn-ae-sap-s-4hana-cl]]

Sample data gives Purchasing Group 001, but the Create Purchase Order steps enter Purch. Group 002.

**Status:** open — needs a human decision

## C478 — test-script-sap-ewm-integration-batch-management-2vn-ae-sap-s-4hana-cl

Page: [[11-inventory-warehouse-and-transportation/test-script-sap-ewm-integration-batch-management-2vn-ae-sap-s-4hana-cl]]

The Overview Table names the delivery app 'Inbound Deliveries for Purchase Orders (VL34)' while the procedure uses Create Inbound Delivery (VL31N).

**Status:** open — needs a human decision

## C479 — test-script-sap-ewm-integration-stock-transport-orders-2vl-ae-sap-s-4h

Page: [[11-inventory-warehouse-and-transportation/test-script-sap-ewm-integration-stock-transport-orders-2vl-ae-sap-s-4h]]

The Overview Table disagrees with the test procedures on several apps: for 8.1 it lists VL02N for 'Check Outbound Delivery Orders' while the procedure uses /SCWM/PRDO; for 8.2 it lists /SCWM/PRDO for 'Pick and Post Goods Issue' while the procedure uses VL02N; for 8.3 it lists VL33N (Display Inbound Delivery) and F0843 while the procedures use VL32N (Change Inbound Delivery) and F2502.

**Status:** open — needs a human decision

## C480 — test-script-sap-ewm-integration-stock-transport-orders-2vl-ae-sap-s-4h

Page: [[11-inventory-warehouse-and-transportation/test-script-sap-ewm-integration-stock-transport-orders-2vl-ae-sap-s-4h]]

The Overview Table for the 8.2 scenario lists EWM outbound steps (Create Warehouse Tasks Manually, Pick Warehouse Orders, Post Goods Issue, pointing to pages 42-44) that have no matching procedure in section 8.2 and belong to section 8.3.

**Status:** open — needs a human decision

## C481 — test-script-sap-ewm-integration-warehouse-stock-handling-2yl-ae-889

Page: [[11-inventory-warehouse-and-transportation/test-script-sap-ewm-integration-warehouse-stock-handling-2yl-ae-889]]

Storage Location is 333D in the master data table but 333S in the Material Documents Overview selection steps (initial stock upload, physical inventory and scrapping checks).

**Status:** open — needs a human decision

## C482 — test-script-sap-ewm-integration-warehouse-stock-handling-2yl-ae-889

Page: [[11-inventory-warehouse-and-transportation/test-script-sap-ewm-integration-warehouse-stock-handling-2yl-ae-889]]

The Stock Overview After Initial Stock Upload table refers to isu_SN01.csv and storage type SN01 (bins 001.01.01.01 to .03) while the Data Files section and master data name isu_TG11.csv and storage types Y001/Y002.

**Status:** open — needs a human decision

## C483 — test-script-sap-ewm-integration-warehouse-stock-handling-2yl-ae-889

Page: [[11-inventory-warehouse-and-transportation/test-script-sap-ewm-integration-warehouse-stock-handling-2yl-ae-889]]

The Purpose text of the Check Material Documents steps under Physical Inventory and Scrapping states movement type 561 (initial stock upload), but their test steps check movement types 711/712 and 344/551 respectively.

**Status:** open — needs a human decision

## C484 — test-script-sap-ewm-integration-warehouse-stock-handling-2yl-ae-889

Page: [[11-inventory-warehouse-and-transportation/test-script-sap-ewm-integration-warehouse-stock-handling-2yl-ae-889]]

The /SCWM/ADPROD access step expects a screen for Warehouse Number 1730 while all other steps and the master data use warehouse 3330.

**Status:** open — needs a human decision

## C485 — test-script-sap-s-4hana-cloud-public-edition-core-inventory-management

Page: [[11-inventory-warehouse-and-transportation/test-script-sap-s-4hana-cloud-public-edition-core-inventory-management]]

Goods Movement Analysis is marked Obsolete in the overview table but has a test procedure with a different app ID (MMIM_FPM_OVP_GDSMVT)

**Status:** open — needs a human decision

## C486 — test-script-sap-s-4hana-cloud-public-edition-core-inventory-management

Page: [[11-inventory-warehouse-and-transportation/test-script-sap-s-4hana-cloud-public-edition-core-inventory-management]]

Customer returns scrapping uses MIGO while other scrapping uses Manage Stock; may differ from other inventory documents

**Status:** open — needs a human decision

## C487 — test-script-stock-transfer-with-delivery-bme-ae-sap-s-4hana-cloud-publ

Page: [[11-inventory-warehouse-and-transportation/test-script-stock-transfer-with-delivery-bme-ae-sap-s-4hana-cloud-publ]]

Approval step states purchasing group is 003 (and 0003 in expected result) while the flexible workflow configuration uses purchasing group 002; the script is internally inconsistent.

**Status:** open — needs a human decision

## C488 — test-script-stock-transfer-without-delivery-bmh-ae-sap-s-4hana-cloud-p

Page: [[11-inventory-warehouse-and-transportation/test-script-stock-transfer-without-delivery-bmh-ae-sap-s-4hana-cloud-p]]

Approval section mentions purchasing group 003 and 0003 inconsistently, and the Purpose says stock transfer POs are not subject to approval while the optional section says all UB orders require approval.

**Status:** open — needs a human decision

## C489 — test-script-transportation-execution-6w3-ae-sap-s-4hana-cloud-public-e

Page: [[11-inventory-warehouse-and-transportation/test-script-transportation-execution-6w3-ae-sap-s-4hana-cloud-public-e-part-01]]

Overview Table lists a different app for Post Goods Issue than the procedures use: Road outbound shows Monitor Accrual Postings (F4329), Rail outbound shows Manage Ocean Freight Bookings (F6213), Rail stock transfer shows F4329, Ocean outbound shows Manage Outbound Deliveries (F0867A); the procedures use VL06O (VL06O_CLOUD), F6498 or VL02N.

**Status:** open — needs a human decision

## C490 — test-script-transportation-execution-6w3-ae-sap-s-4hana-cloud-public-e

Page: [[11-inventory-warehouse-and-transportation/test-script-transportation-execution-6w3-ae-sap-s-4hana-cloud-public-e-part-01]]

Ocean outbound 'Arrival of Truck at Port of Loading (Pick-Up)' step 9 expects the message 'Departure at stop PORT_AEYAS was reported' although the Overview Table expects 'Arrival at port of loading was reported'.

**Status:** open — needs a human decision

## C491 — test-script-transportation-execution-6w3-ae-sap-s-4hana-cloud-public-e

Page: [[11-inventory-warehouse-and-transportation/test-script-transportation-execution-6w3-ae-sap-s-4hana-cloud-public-e-part-02]]

Future-dated internal transfer of control: Advanced Intercompany Sales says the goods movement posts one day later than the planned/actual date and time, while Advanced Intercompany Stock Transfer says it posts when that date and time is reached.

**Status:** open — needs a human decision

## C492 — test-script-transportation-execution-6w3-ae-sap-s-4hana-cloud-public-e

Page: [[11-inventory-warehouse-and-transportation/test-script-transportation-execution-6w3-ae-sap-s-4hana-cloud-public-e-part-02]]

Advanced Intercompany scenarios: Post Goods Issue says the shipping point should be 1710, but the transfer-of-control display steps filter Shipping Point/Receiving Pt on 1010.

**Status:** open — needs a human decision

## C493 — test-script-warehouse-ad-hoc-goods-issue-3bt-ae-sap-s-4hana-cloud-publ

Page: [[11-inventory-warehouse-and-transportation/test-script-warehouse-ad-hoc-goods-issue-3bt-ae-sap-s-4hana-cloud-publ]]

Internal inconsistency: the scrapping synchronous goods movement (movement type 551) Where-tab step lists 'Plant: TG11', but TG11 is a material in the sample data and the plant is 3310 everywhere else in the script.

**Status:** open — needs a human decision

## C494 — test-script-warehouse-inbound-processing-3br-ae-sap-s-4hana-cloud-publ

Page: [[11-inventory-warehouse-and-transportation/test-script-warehouse-inbound-processing-3br-ae-sap-s-4hana-cloud-publ]]

RF test steps log on with Whse No 1750, while the master data table and default-value steps use warehouse 3350 (ERP warehouse 335, plant 3310).

**Status:** open — needs a human decision

## C495 — test-script-warehouse-inbound-processing-3br-ae-sap-s-4hana-cloud-publ

Page: [[11-inventory-warehouse-and-transportation/test-script-warehouse-inbound-processing-3br-ae-sap-s-4hana-cloud-publ]]

The optional two-storage-location note names 335I as the additional storage location in Business Conditions, but the same note in Preceding Processes says 'additional storage location 335W' compared to the single 335W setup.

**Status:** open — needs a human decision

## C496 — test-script-warehouse-inbound-processing-3br-ae-sap-s-4hana-cloud-publ

Page: [[11-inventory-warehouse-and-transportation/test-script-warehouse-inbound-processing-3br-ae-sap-s-4hana-cloud-publ]]

Create Handling Unit RF 'Check Delivery Status' shows GR Posted: X although it precedes goods receipt posting, while Post Goods Receipt RF shows GR Posted: Empty before posting.

**Status:** open — needs a human decision

## C497 — test-script-warehouse-production-integration-with-synchronous-goods-re

Page: [[11-inventory-warehouse-and-transportation/test-script-warehouse-production-integration-with-synchronous-goods-re]]

Create Control Cycle expected result reads 'Control cycle RM124 1010 PSA_02 is created' although the entries specify Plant 3310; the message shows plant 1010.

**Status:** open — needs a human decision

## C498 — test-script-warehouse-production-integration-with-synchronous-goods-re

Page: [[11-inventory-warehouse-and-transportation/test-script-warehouse-production-integration-with-synchronous-goods-re]]

Initial Stock Posting section refers to BoM materials of FG228 and FG227 (with SG224, SG21, RM20) and storage location 331B, and a putaway step filters Product FG012, none of which are in the sample data table (FG426, SG424, FG626, SG624, FG328).

**Status:** open — needs a human decision

## C499 — warehouse-advanced-production-integration-6ni-ae-test-script-sap-s-4ha

Page: [[11-inventory-warehouse-and-transportation/warehouse-advanced-production-integration-6ni-ae-test-script-sap-s-4ha]]

Sample organizational data (company code 3310, plant 3310, storage location 335W, warehouse number 335, warehouse 3350) disagrees with the values used in the test steps (plant 1710, warehouse number 1750, storage location 175W, PSA_03 / 1710).

**Status:** open — needs a human decision

## C500 — warehouse-advanced-production-integration-6ni-ae-test-script-sap-s-4ha

Page: [[11-inventory-warehouse-and-transportation/warehouse-advanced-production-integration-6ni-ae-test-script-sap-s-4ha]]

RM124 staging warehouse process type is S220 in the Assign Bins to PSA overview table, but the procedure step for RM124 enters Staging WPT S320 (S320 is described as the Cross-Order Staging type while RM124 is Single-Order Staging).

**Status:** open — needs a human decision

## C501 — warehouse-advanced-production-integration-6ni-ae-test-script-sap-s-4ha

Page: [[11-inventory-warehouse-and-transportation/warehouse-advanced-production-integration-6ni-ae-test-script-sap-s-4ha]]

Replenishment quantity for RM424/RM524/RM124 is 4 in the Assign Bins to PSA table, yet the Post Consumption note says the replenishment quantity is set at 2 per iteration.

**Status:** open — needs a human decision

## C502 — warehouse-kanban-supply-into-production-3vt-ae-test-script-977

Page: [[11-inventory-warehouse-and-transportation/warehouse-kanban-supply-into-production-3vt-ae-test-script-977]]

Variant 1 step 4 says goods issue posts to production storage location 171B, while the rest of the document uses 331B.

**Status:** open — needs a human decision

## C503 — warehouse-physical-inventory-3bx-ae-test-script-sap-s-4hana-cloud-publ

Page: [[11-inventory-warehouse-and-transportation/warehouse-physical-inventory-3bx-ae-test-script-sap-s-4hana-cloud-publ]]

Internal inconsistency in warehouse number: sample data, default values, Fiori counting and cycle counting steps use warehouse 3350, but the RF steps (Whse No: 1750), Confirm Inventory Count Results (Warehouse No.: 1750) and Analyze Differences (Warehouse No.: 1750) use 1750.

**Status:** open — needs a human decision

## C504 — warehouse-posting-changes-3bu-ae-test-script-sap-s-4hana-cloud-public

Page: [[11-inventory-warehouse-and-transportation/warehouse-posting-changes-3bu-ae-test-script-sap-s-4hana-cloud-public]]

Sample data lists warehouse 3350, plant 3310 and storage location 335W, but test steps use warehouse 1750, plant 1710 and storage location 175W.

**Status:** open — needs a human decision

## C505 — warehouse-production-integration-3dv-ae-test-script-sap-s-4hana-cloud

Page: [[11-inventory-warehouse-and-transportation/warehouse-production-integration-3dv-ae-test-script-sap-s-4hana-cloud]]

Warehouse number is 3350 in sample data and in most steps, but the RF steps in Create Handling Unit (Variant 3), Post Goods Receipt (Variant 2) and Confirm Putaway Warehouse Tasks (Variant 2) enter Whse No 1750 (the packing instruction determination example uses 1050); the RF putaway-creation variant uses 3350.

**Status:** open — needs a human decision

## C506 — arbeitsplan-anlegen-sds-bnl-628

Page: [[12-production-and-manufacturing/arbeitsplan-anlegen-sds-bnl-628]]

Control key list in step 6 names YBP5 in the entry options while describing YBP4; internal inconsistency

**Status:** open — needs a human decision

## C507 — creacion-de-hoja-de-ruta-mds-bnl-630

Page: [[12-production-and-manufacturing/creacion-de-hoja-de-ruta-mds-bnl-630]]

Control key list in step 6 names YBP1/YBP2/YBP3/YBP5 but the explanation lists YBP4 (process manufacturing milestone) and no YBP5; the step 7 text also says the purchasing info record is mandatory for internal operations, contradicting the prerequisite table (external operations).

**Status:** open — needs a human decision

## C508 — criar-roteiro-mds-bnl-632

Page: [[12-production-and-manufacturing/criar-roteiro-mds-bnl-632]]

Step 7 (external operation setup) says the purchasing info record is required for internal operations and blank for external ones, contradicting section 2.4 and the step title, which tie the purchasing info record to external operations.

**Status:** open — needs a human decision

## C509 — master-data-script-create-production-resources-tools-mds-5cp-437

Page: [[12-production-and-manufacturing/master-data-script-create-production-resources-tools-mds-5cp-437]]

Purpose text says 'SAP S/4HANA Cloud Private Edition system' while the document is for Public Edition

**Status:** open — needs a human decision

## C510 — master-data-script-create-reference-operation-set-mds-ble-575

Page: [[12-production-and-manufacturing/master-data-script-create-reference-operation-set-mds-ble-575]]

Work center row of the master data table refers to the script 'Create Reference Operation Set - MDS (BLE)' (itself) rather than a work center script; BOM row refers to BNK

**Status:** open — needs a human decision

## C511 — master-data-script-create-routing-mds-bnl-629

Page: [[12-production-and-manufacturing/master-data-script-create-routing-mds-bnl-629]]

Step 7 says purchasing info record is 'required for internal operations, blank for external', while prerequisites table says it is used for external operations; internal inconsistency.

**Status:** open — needs a human decision

## C512 — master-data-script-mds-5cp-japanese-439

Page: [[12-production-and-manufacturing/master-data-script-mds-5cp-japanese-439]]

The purpose text says the script covers 'SAP S/4HANA Cloud Private Edition' while the title and cover say Public Edition.

**Status:** open — needs a human decision

## C513 — mds-ble-577

Page: [[12-production-and-manufacturing/mds-ble-577]]

Control key description lists YBP1 twice (with and without automatic goods receipt); YBP3 not explained

**Status:** open — needs a human decision

## C514 — mds-bnl-631

Page: [[12-production-and-manufacturing/mds-bnl-631]]

Control key list in step 6 assigns YBP1 to both internal operation without and with auto goods receipt (YBP3 not described), internally inconsistent

**Status:** open — needs a human decision

## C515 — mds-bnl-633

Page: [[12-production-and-manufacturing/mds-bnl-633]]

控制代码说明中 YBP5 在列表中出现而说明列出 YBP4，疑似内部不一致

**Status:** open — needs a human decision

## C516 — produce-and-sell-standard-products-warehouse-managed-54v-ae-test-scrip

Page: [[12-production-and-manufacturing/produce-and-sell-standard-products-warehouse-managed-54v-ae-test-scrip]]

Assign Bins to PSA step uses Warehouse Number 1750 while all other steps and org data use warehouse 3350.

**Status:** open — needs a human decision

## C517 — produce-and-sell-standard-products-warehouse-managed-54v-ae-test-scrip

Page: [[12-production-and-manufacturing/produce-and-sell-standard-products-warehouse-managed-54v-ae-test-scrip]]

Create Control Cycle (IM-managed PSA) for RM021 uses supply area PSA_01 and warehouse no 335, while org data lists only PSA_03 and warehouse 3350.

**Status:** open — needs a human decision

## C518 — script-de-dados-mestre-criar-meio-auxiliar-de-producao-mds-5cp-440

Page: [[12-production-and-manufacturing/script-de-dados-mestre-criar-meio-auxiliar-de-producao-mds-5cp-440]]

Purpose text refers to 'SAP S/4HANA Cloud Private Edition' while the title and rest of the document say Public Edition

**Status:** open — needs a human decision

## C519 — script-de-datos-maestros-creacion-de-medios-auxiliares-de-fabricacion

Page: [[12-production-and-manufacturing/script-de-datos-maestros-creacion-de-medios-auxiliares-de-fabricacion]]

Objetivo refers to SAP S/4HANA Cloud Private Edition while the document is for Public Edition

**Status:** open — needs a human decision

## C520 — stammdatenskript-fertigungshilfsmittel-anlegen-sds-5cp-436

Page: [[12-production-and-manufacturing/stammdatenskript-fertigungshilfsmittel-anlegen-sds-5cp-436]]

Purpose section says the system is SAP S/4HANA Cloud Private Edition, while the title/footers and role links refer to Public Edition.

**Status:** open — needs a human decision

## C521 — stammdatenskript-fertigungshilfsmittel-anlegen-sds-5cp-436

Page: [[12-production-and-manufacturing/stammdatenskript-fertigungshilfsmittel-anlegen-sds-5cp-436]]

Material FHM example number is FHM_01 but the expected result says material number PRT_01 is created; later steps use PRT_01.

**Status:** open — needs a human decision

## C522 — test-script-bill-of-material-management-64f-ae-sap-s-4hana-cloud-publi

Page: [[12-production-and-manufacturing/test-script-bill-of-material-management-64f-ae-sap-s-4hana-cloud-publi]]

Internal: the Overview Table lists the Release Change steps of the three mass-maintenance sections under apps F6578/F6862/F6863 (expected result 'Change master is released'), while the detailed procedures release the change master in Manage Change Masters (F2212).

**Status:** open — needs a human decision

## C523 — test-script-capacity-planning-evaluation-scope-item-31l-sap-s-4hana-cl

Page: [[12-production-and-manufacturing/test-script-capacity-planning-evaluation-scope-item-31l-sap-s-4hana-cl]]

Check Capacity Situation (discrete) step 3 assigns work center group 05_COFFEE for plant 3310, but the sample work center groups defined in this script are TURN_ALT and CP_SG1 (created via BNJ).

**Status:** open — needs a human decision

## C524 — test-script-demand-driven-buffer-level-management-1y2-ae-sap-s-4hana-c

Page: [[12-production-and-manufacturing/test-script-demand-driven-buffer-level-management-1y2-ae-sap-s-4hana-c]]

Schedule Buffer Proposal Calculation step 7 says Fixed Interval ADU mode is chosen 'for product S-202 and R-401', but step 6 selects S-201 and R-401 and step 9 and the later Manage Buffer Levels note say S-202 alone uses Rolling Interval (S-201 and R-401 fixed).

**Status:** open — needs a human decision

## C525 — test-script-demand-driven-buffer-level-management-1y2-ae-sap-s-4hana-c

Page: [[12-production-and-manufacturing/test-script-demand-driven-buffer-level-management-1y2-ae-sap-s-4hana-c]]

Mass Maintenance of Products step 3 lists S-201, S-202, S-203 and R-401 as buffered products by default, while Buffer Positioning and the preliminary steps name only three buffered products (S-201, S-202, R-401) and the BOM table describes S-203 as a stock transfer material.

**Status:** open — needs a human decision

## C526 — test-script-demand-driven-replenishment-planning-and-execution-2qi-ae

Page: [[12-production-and-manufacturing/test-script-demand-driven-replenishment-planning-and-execution-2qi-ae]]

Final check in Replenishment Planning says the resulting priority is 100.00% in green or above 100% in blue, while its expected result says the status turns black above 100% of max stock.

**Status:** open — needs a human decision

## C527 — test-script-demand-driven-replenishment-planning-and-execution-2qi-ae

Page: [[12-production-and-manufacturing/test-script-demand-driven-replenishment-planning-and-execution-2qi-ae]]

Create Demand for Finished Goods says to skip the whole chapter when S-201 is MRP type D2, yet Option 1 contains the D2-only step 'Firm Planned Order' and Option 2 the D2-only 'Create Firmed Planned Order', which the same text routes D2 users to.

**Status:** open — needs a human decision

## C528 — test-script-make-to-stock-production-discrete-manufacturing-bj5-ae-sap

Page: [[12-production-and-manufacturing/test-script-make-to-stock-production-discrete-manufacturing-bj5-ae-sap]]

Internal inconsistency: the Release Production Order for Final Assembly step (FG126) says to assign only AOR entry 'MTO w/o VC - Val.(YB4)', whereas every other supervisor AOR check in the script (including the FG126 availability review) assigns 'MTS DI - Valuated (YB1)'.

**Status:** open — needs a human decision

## C529 — test-script-make-to-stock-production-discrete-manufacturing-bj5-ae-sap

Page: [[12-production-and-manufacturing/test-script-make-to-stock-production-discrete-manufacturing-bj5-ae-sap]]

Internal inconsistency: the Overview Table lists Manage Production Orders (F2336) for the Review Production Order step, but the procedure itself opens Manage Production Operations (F2335).

**Status:** open — needs a human decision

## C530 — test-script-make-to-stock-production-repetitive-manufacturing-bjh-ae-s

Page: [[12-production-and-manufacturing/test-script-make-to-stock-production-repetitive-manufacturing-bjh-ae-s]]

Overview Table lists Production Supervisor - Repetitive Manufacturing as the role for Material Staging (MF60) and Confirm Repetitive Manufacturing (MFBF), but the test procedures for both steps say to log on as Production Operator - Repetitive Manufacturing.

**Status:** open — needs a human decision

## C531 — test-script-make-to-stock-production-repetitive-manufacturing-bjh-ae-s

Page: [[12-production-and-manufacturing/test-script-make-to-stock-production-repetitive-manufacturing-bjh-ae-s]]

Planning table capacity example is internally inconsistent: text computes 2000 PC as 3.5 H (210 min) at 43.75% load, but the planning table shows Requirement - Default Capacity of 4 H at 43.75%; the quantity change is also dated 04/17/17 in step 4 but 04/18/17 in the later description, while the table shows the quantity in the 04/17/17 column.

**Status:** open — needs a human decision

## C532 — test-script-make-to-stock-production-with-variant-configuration-21d-ae

Page: [[12-production-and-manufacturing/test-script-make-to-stock-production-with-variant-configuration-21d-ae]]

Material SF-FL-COMB is described as 'FORKLIFTER BASE MODEL ELECTRICAL' in the master data table, but as the combustion base model in the BoM table (where SF-FL-ELECTRIC is the electrical one) and as 'Power source = SF-FL-COMB (Combustion)' in the planned order check.

**Status:** open — needs a human decision

## C533 — test-script-make-to-stock-with-co-and-by-products-process-manufacturin

Page: [[12-production-and-manufacturing/test-script-make-to-stock-with-co-and-by-products-process-manufacturin]]

Overview Table lists the Review Scrap Report (Optional) step under role 'Production Supervisor - Discrete Manufacturing', while the procedure logs on as 'Production Supervisor - Process Manufacturing'; the Roles table does not list a Discrete Manufacturing supervisor.

**Status:** open — needs a human decision

## C534 — test-script-material-replenishment-with-kanban-in-house-production-4b3

Page: [[12-production-and-manufacturing/test-script-material-replenishment-with-kanban-in-house-production-4b3]]

Monitor Replenishment Situation step searches Plant 1010 while the rest of the script and master data use Plant 3310 (Plant 1 AE).

**Status:** open — needs a human decision

## C535 — test-script-material-replenishment-with-kanban-stock-transfer-4b4-ae-s

Page: [[12-production-and-manufacturing/test-script-material-replenishment-with-kanban-stock-transfer-4b4-ae-s]]

Withdraw Quantity note says it can be 50 or less 'based on the demo data', but the RM233-1 control cycle defined in the same script has Container quantity 100, so the limit would be 100 or less.

**Status:** open — needs a human decision

## C536 — test-script-material-replenishment-with-kanban-stock-transfer-4b4-ae-s

Page: [[12-production-and-manufacturing/test-script-material-replenishment-with-kanban-stock-transfer-4b4-ae-s]]

One-card Kanban overview says the second container is set to Empty when remaining material 'reaches or exceeds' the trigger quantity, whereas the step purpose and example (15 in container, trigger 5, withdraw 10 or more) say it triggers when remaining quantity reaches or falls below the trigger quantity.

**Status:** open — needs a human decision

## C537 — test-script-material-requirements-planning-j44-ae-sap-s-4hana-cloud-pu

Page: [[12-production-and-manufacturing/test-script-material-requirements-planning-j44-ae-sap-s-4hana-cloud-pu]]

Internal: the Days of Supply section's 'Maintain MRP Safety Stock Method in Material' step assigns Time-Dependent Safety Stock, yet the next step says the safety stock method 'is changed to Days of Supply'; the Reset Material Master Data step also says to assign Time-dependent Safety stock while its expected result says the method is removed.

**Status:** open — needs a human decision

## C538 — test-script-material-requirements-planning-j44-ae-sap-s-4hana-cloud-pu

Page: [[12-production-and-manufacturing/test-script-material-requirements-planning-j44-ae-sap-s-4hana-cloud-pu]]

Internal: material TG0099 uses MRP Controller 001 in every other step (team definition, PIR steps, Detect MRP Situations, rescheduling check), but the Days of Supply 'Manage PIRs for Material TG0099' step requires MRP Controller 002 in the area of responsibility.

**Status:** open — needs a human decision

## C539 — test-script-planning-and-production-in-other-plant-consumer-products-7

Page: [[12-production-and-manufacturing/test-script-planning-and-production-in-other-plant-consumer-products-7]]

Internal inconsistency on batch management of PK0515 (Foil): the master data table lists it as 'Packaging material, no batch, external procurement' while the plant 3310 BOM table lists it as 'Packaging material, batch managed, external procured' (component quantity 40 M).

**Status:** open — needs a human decision

## C540 — test-script-produce-and-sell-standard-products-inventory-management-54

Page: [[12-production-and-manufacturing/test-script-produce-and-sell-standard-products-inventory-management-54-part-01]]

Approve Purchase Orders: the note says only POs with a value higher than 500.00 AED are released, while the expected result says a net value of 500 AED or more has status In Approval, so the boundary at exactly 500 AED is ambiguous.

**Status:** open — needs a human decision

## C541 — test-script-produce-and-sell-standard-products-inventory-management-54

Page: [[12-production-and-manufacturing/test-script-produce-and-sell-standard-products-inventory-management-54-part-01]]

The Overview Table lists Record Inspection Results (F1685A) for the repetitive-manufacturing inspection step and Production Operator - Lean Manufacturing with Display Kanbans: Demand View (PK13N) for Create Event-Driven Kanban, but the procedures use Record Inspection Results - Hierarchical Worklist (QE51N) and Production Planner - Lean Manufacturing with Kanban Board (F4630).

**Status:** open — needs a human decision

## C542 — test-script-produce-and-sell-standard-products-inventory-management-54

Page: [[12-production-and-manufacturing/test-script-produce-and-sell-standard-products-inventory-management-54-part-01]]

Create Outbound Delivery (subcontracting) names components provided as RM33 and RM34, whereas the master data and the surrounding steps use RM023, RM024, RM025 and RM026.

**Status:** open — needs a human decision

## C543 — test-script-produce-and-sell-standard-products-inventory-management-54

Page: [[12-production-and-manufacturing/test-script-produce-and-sell-standard-products-inventory-management-54-part-02]]

Post Outgoing Payment step 6 expected result cites 'company code1010' although the same procedure uses Company Code 3310.

**Status:** open — needs a human decision

## C544 — test-script-produce-and-sell-standard-products-inventory-management-54

Page: [[12-production-and-manufacturing/test-script-produce-and-sell-standard-products-inventory-management-54-part-02]]

Post Outgoing Payment step 10 pays invoices for RM012, RM017 and RM018 but the Create Supplier Invoice steps in this part cover RM011, RM012, RM013, RM018 and SG022 only (no RM017); RM017 may be invoiced in the earlier part of the document.

**Status:** open — needs a human decision

## C545 — test-script-product-change-management-with-change-records-64e-ae-sap-s

Page: [[12-production-and-manufacturing/test-script-product-change-management-with-change-records-64e-ae-sap-s]]

The Overview Table's Expected Results do not match the Test Procedures: e.g. Submit Change Request and Approve Change Request both list 'Change Master Status is set to Inactive', Release Change lists 'Bill of Material is discarded', while the procedures state statuses Change Request in Review, Change Request Approved and Change Released.

**Status:** open — needs a human decision

## C546 — test-script-production-capacity-leveling-3lq-ae-sap-s-4hana-cloud-publ

Page: [[12-production-and-manufacturing/test-script-production-capacity-leveling-3lq-ae-sap-s-4hana-cloud-publ]]

Preceding-process list differs between sections: Business Conditions (2.4) lists Create Planned Independent Requirements, Material Requirement Planning and Evaluate Capacity Situation from 31L, while Appendix 5.1.1 Preceding Processes lists Conversion to Production Orders, Material Requirement Planning and Evaluate Capacity Situation.

**Status:** open — needs a human decision

## C547 — test-script-sap-s-4hana-cloud-public-edition-from-planning-to-fulfillm

Page: [[12-production-and-manufacturing/test-script-sap-s-4hana-cloud-public-edition-from-planning-to-fulfillm-part-01]]

Purchase order approval threshold for purchasing group 002 appears inconsistent: the 5W3 workflow configuration example uses total net amount greater than 10 AED, while the 5W3 manual purchase order note says an approver is assigned above 500 AED (for Purchase Groups = 002); 5W4 uses group 001 with 500 AED.

**Status:** open — needs a human decision

## C548 — test-script-sap-s-4hana-cloud-public-edition-from-planning-to-fulfillm

Page: [[12-production-and-manufacturing/test-script-sap-s-4hana-cloud-public-edition-from-planning-to-fulfillm-part-02]]

Approve Purchase Orders in the subcontracting section: the note says only POs with a value higher than 500.00 AED need release, but step 3 says POs with a net value of 500 AED or more have status In Approval (boundary differs).

**Status:** open — needs a human decision

## C549 — test-script-sap-s-4hana-cloud-public-edition-from-planning-to-fulfillm

Page: [[12-production-and-manufacturing/test-script-sap-s-4hana-cloud-public-edition-from-planning-to-fulfillm-part-02]]

Check Default Setting for Manage Material Coverage: the first Evaluate Stock/Requirements Situation says toggle OFF navigates to the old version (F0251), while the one after goods receipt for FG0511 says OFF also navigates to F0251A.

**Status:** open — needs a human decision

## C550 — test-script-sap-s-4hana-cloud-public-edition-from-planning-to-fulfillm

Page: [[12-production-and-manufacturing/test-script-sap-s-4hana-cloud-public-edition-from-planning-to-fulfillm-part-03]]

Record Inspection Results step 6 lists the Positive Result with Visual Pack Check assigned to class NOK and the Negative Result with Visual Pack Check assigned to class OK, while Label Check is the reverse; the positive/negative class assignments look internally inconsistent.

**Status:** open — needs a human decision

## C551 — ehs-produkt-anlegen-sds-660-508

Page: [[13-quality-ehs-and-compliance/ehs-produkt-anlegen-sds-660-508]]

Section 4.1 heading says 'EHS-Lokationsstammdaten anlegen' (EHS location) while content creates an EHS product; may differ from other language versions of script 660

**Status:** open — needs a human decision

## C552 — health-and-safety-management-54a-ae-test-script-sap-s-4hana-cloud-publ

Page: [[13-quality-ehs-and-compliance/health-and-safety-management-54a-ae-test-script-sap-s-4hana-cloud-publ]]

The Release and Print safety-instruction steps log on as 'Plant Manager - EHS Info', which is not in the Roles table (Industrial Hygienist, Employee - EHS Info, Hazardous Materials Manager). The Overview Tables 5 and 6 name Industrial Hygienist as the business role for those same release steps.

**Status:** open — needs a human decision

## C553 — health-and-safety-management-54a-ae-test-script-sap-s-4hana-cloud-publ

Page: [[13-quality-ehs-and-compliance/health-and-safety-management-54a-ae-test-script-sap-s-4hana-cloud-publ]]

The Workplace Safety Overview card 'Number of Risks' expects a risk assessment 'Job: Welding for Production Line B', but the script only creates the job hazard analysis for Production Line A.

**Status:** open — needs a human decision

## C554 — master-data-script-create-quality-inspection-plan-mds-bnq-653

Page: [[13-quality-ehs-and-compliance/master-data-script-create-quality-inspection-plan-mds-bnq-653]]

Quantitative characteristic step 10 describes both Complete and Incomplete Copy Model with near-identical wording, which may be a copy error

**Status:** open — needs a human decision

## C555 — master-data-script-create-quality-inspection-plan-mds-bnq-653

Page: [[13-quality-ehs-and-compliance/master-data-script-create-quality-inspection-plan-mds-bnq-653]]

Section 4.13 Display Open Inspection Lots is listed in the TOC but missing from the Overview Table process steps

**Status:** open — needs a human decision

## C556 — nonconformance-management-2qn-ae-test-script-sap-s-4hana-cloud-public

Page: [[13-quality-ehs-and-compliance/nonconformance-management-2qn-ae-test-script-sap-s-4hana-cloud-public]]

Record Inspection Results purpose says the quality engineer records results, but the overview table and test step 1 use the Quality Technician role.

**Status:** open — needs a human decision

## C557 — nonconformance-management-2qn-ae-test-script-sap-s-4hana-cloud-public

Page: [[13-quality-ehs-and-compliance/nonconformance-management-2qn-ae-test-script-sap-s-4hana-cloud-public]]

Purpose says the quality technician executes the defined actions and sets the status, but the Execute Quality Task steps and the overview table assign this to the Quality Engineer (Process Quality Tasks F3250).

**Status:** open — needs a human decision

## C558 — quality-management-in-procurement-1fm-ae-test-script-sap-s-4hana-cloud

Page: [[13-quality-ehs-and-compliance/quality-management-in-procurement-1fm-ae-test-script-sap-s-4hana-cloud]]

Supplier return support is stated inconsistently: some PO steps say 33300006 supports return with delivery while 33300001 only without delivery; the Create Second Purchase Order step says 33300006 supports with delivery and 33300006 only without delivery.

**Status:** open — needs a human decision

## C559 — quality-management-in-procurement-1fm-ae-test-script-sap-s-4hana-cloud

Page: [[13-quality-ehs-and-compliance/quality-management-in-procurement-1fm-ae-test-script-sap-s-4hana-cloud]]

Storage location for goods receipt/quality stock is 331A in master data and most steps, but the stock-before-GR step and one GR step reference 331C, which is not listed in master data.

**Status:** open — needs a human decision

## C560 — script-de-dados-mestre-criar-plano-de-controle-de-qualidade-mds-bnq-65

Page: [[13-quality-ehs-and-compliance/script-de-dados-mestre-criar-plano-de-controle-de-qualidade-mds-bnq-65]]

Quantitative characteristic step text on 'modelo de cópia completo' vs 'incompleto' is near-identical for both, and differs from the qualitative description; possible text inconsistency

**Status:** open — needs a human decision

## C561 — script-de-dados-mestre-criar-plano-de-controle-de-qualidade-mds-bnq-65

Page: [[13-quality-ehs-and-compliance/script-de-dados-mestre-criar-plano-de-controle-de-qualidade-mds-bnq-65]]

Test-case metadata (ID, dates, executor) is left as template placeholders

**Status:** open — needs a human decision

## C562 — script-de-datos-maestros-creacion-de-plan-de-inspeccion-de-calidad-mds

Page: [[13-quality-ehs-and-compliance/script-de-datos-maestros-creacion-de-plan-de-inspeccion-de-calidad-mds]]

Document is flagged as machine-translated and not reviewed for accuracy; wording may be unreliable.

**Status:** open — needs a human decision

## C563 — script-de-datos-maestros-creacion-de-plan-de-inspeccion-de-calidad-mds

Page: [[13-quality-ehs-and-compliance/script-de-datos-maestros-creacion-de-plan-de-inspeccion-de-calidad-mds]]

Filename says 'Master_Data' ES while the extracted title heading is 'Objetivo'; real title taken from cover table.

**Status:** open — needs a human decision

## C564 — stammdatenskript-qualitatsprufplan-anlegen-sds-bnq-652

Page: [[13-quality-ehs-and-compliance/stammdatenskript-qualitatsprufplan-anlegen-sds-bnq-652]]

Source title extracted as 'Verwendungszweck' (first heading) rather than the real title; document is in German.

**Status:** open — needs a human decision

## C565 — stammdatenskript-qualitatsprufplan-anlegen-sds-bnq-652

Page: [[13-quality-ehs-and-compliance/stammdatenskript-qualitatsprufplan-anlegen-sds-bnq-652]]

Unfilled placeholders (<X.XX>, test case fields) are template content, not data.

**Status:** open — needs a human decision

## C566 — stammdatenskript-qualitatsprufplan-anlegen-sds-bnq-652

Page: [[13-quality-ehs-and-compliance/stammdatenskript-qualitatsprufplan-anlegen-sds-bnq-652]]

Description of Vollständige/Unvollständige Kopiervorlage differs between qualitative (step 4) and quantitative (step 10) sections, possibly a template inconsistency.

**Status:** open — needs a human decision

## C567 — substance-volume-tracking-4ol-ae-test-script-sap-s-4hana-cloud-public

Page: [[13-quality-ehs-and-compliance/substance-volume-tracking-4ol-ae-test-script-sap-s-4hana-cloud-public]]

The 'Classify a Packaged Product as No Dangerous Good' procedure adds the compliance purpose 'Transport in North America' (and links to the 4OL US / 2308_DEV procedure), although the sample customer 33100050 is in DE and the market assessment is added for Germany; the appendix may have been carried over from the US version of this script.

**Status:** open — needs a human decision

## C568 — test-script-assess-marketability-of-a-product-31h-ae-sap-s-4hana-cloud

Page: [[13-quality-ehs-and-compliance/test-script-assess-marketability-of-a-product-31h-ae-sap-s-4hana-cloud]]

The Create Analytical Composition purpose says the unpackaged product consists of only one substance, m-xylene, but the test steps and expected results use DEHP (CAS 117-81-7) as that single substance.

**Status:** open — needs a human decision

## C569 — test-script-chemical-compliance-in-the-value-chain-31j-ae-sap-s-4hana

Page: [[13-quality-ehs-and-compliance/test-script-chemical-compliance-in-the-value-chain-31j-ae-sap-s-4hana]]

Sample master data names customer 33100003 as 'Domestic UAE Customer 3' (UAE) but expected results in the status-check procedures describe it as 'Domestic US Customer 3' (US), so the customer's country/region is stated inconsistently.

**Status:** open — needs a human decision

## C570 — test-script-chemical-compliance-in-the-value-chain-31j-ae-sap-s-4hana

Page: [[13-quality-ehs-and-compliance/test-script-chemical-compliance-in-the-value-chain-31j-ae-sap-s-4hana]]

In 'Process Compliance Request from Logistics and Assess Marketability Requirements' the request is for FG<your name>02, yet the expected data lists packaged FG<your name>03, unpackaged '<your name> UP 2' and a Product in Product Master of FG<your name>05, which do not match the three products created in the preliminary steps.

**Status:** open — needs a human decision

## C571 — test-script-compliance-management-for-environment-health-and-safety-4c

Page: [[13-quality-ehs-and-compliance/test-script-compliance-management-for-environment-health-and-safety-4c]]

The My Inbox - Environment Management app is given as F0862 in the Overview Table but as F8329 in the Execute Tasks and Monitor Compliance Tasks procedures.

**Status:** open — needs a human decision

## C572 — test-script-label-management-6mt-ae-sap-s-4hana-cloud-public-edition-1

Page: [[13-quality-ehs-and-compliance/test-script-label-management-6mt-ae-sap-s-4hana-cloud-public-edition-1]]

Delivery-scenario Validate and Print step expects Country/Region USA, while the ship-to party 33100003 is 'Domestic UAE Customer 3' and the Sell In country is meant to be that business partner's country; the compliance requirement validity in the generic scenario is US.

**Status:** open — needs a human decision

## C573 — test-script-occupational-health-for-environment-health-and-safety-7za

Page: [[13-quality-ehs-and-compliance/test-script-occupational-health-for-environment-health-and-safety-7za]]

The Create Health Centers Result says the center has two medical physicians, one psychologist and one receptionist, but the steps assign two OH Physicians, one OH Nurse and one OH Receptionist (no psychologist role).

**Status:** open — needs a human decision

## C574 — test-script-preference-management-with-sap-global-trade-services-3jx-a

Page: [[13-quality-ehs-and-compliance/test-script-preference-management-with-sap-global-trade-services-3jx-a]]

Display Worklist of Configurable Materials: the Overview Table expects the configurable material 'displayed with the status Calculated', while the procedure's expected result says 'displayed with the status transferred'.

**Status:** open — needs a human decision

## C575 — test-script-preference-management-with-sap-global-trade-services-3jx-a

Page: [[13-quality-ehs-and-compliance/test-script-preference-management-with-sap-global-trade-services-3jx-a]]

Overview Table lists 'Schedule Transfer of Material Documents - Global Trade Services (F3741)' for the billing document transfer step, whereas the procedure uses 'Schedule Transfer of Billing Documents - Global Trade Services (F3740)' and F3741 is the material documents app.

**Status:** open — needs a human decision

## C576 — test-script-preference-management-with-sap-global-trade-services-3jx-a

Page: [[13-quality-ehs-and-compliance/test-script-preference-management-with-sap-global-trade-services-3jx-a]]

Notes state the master-data change-point background jobs are scheduled hourly and the rhythm cannot be changed, yet 'Schedule Transfer of Changed Master Data' (F6041) has the tester schedule daily (Every 1 Day) jobs for the same change pointers.

**Status:** open — needs a human decision

## C577 — test-script-quality-management-for-complaints-against-suppliers-2f9-ae

Page: [[13-quality-ehs-and-compliance/test-script-quality-management-for-complaints-against-suppliers-2f9-ae]]

Overview Table lists 'Display a List of Quality Notifications (optional)' under app QM13 (Display Quality Notification Tasks - Worklist), but the procedure for that step opens QM11 (Display Quality Notifications - Worklist).

**Status:** open — needs a human decision

## C578 — test-script-quality-management-in-sales-1mp-ae-sap-s-4hana-cloud-publi

Page: [[13-quality-ehs-and-compliance/test-script-quality-management-in-sales-1mp-ae-sap-s-4hana-cloud-publi]]

Internal app inconsistency: the Overview Table lists Manage Outbound Deliveries (F0867A) for Execute Picking and Manage Usage Decisions (F2345) for Make Usage Decision, but the Test Procedures use Manage Outbound Deliveries - VL06O (VL06O_CLOUD) and Record Usage Decision (QA11) respectively.

**Status:** open — needs a human decision

## C579 — test-script-request-regulatory-documentation-from-service-provider-6av

Page: [[13-quality-ehs-and-compliance/test-script-request-regulatory-documentation-from-service-provider-6av]]

Internal inconsistency in launchpad space IDs: the Roles table gives the space 'Master Data - Product Compliance' the ID SAP_BR_MD_SPECIALIST_PCL, but the Overview Table row for Create Private Substance Request lists the same space name with ID SAP_BR_PRODSTWRD_SPLST_PCL (the Product Stewardship role's ID).

**Status:** open — needs a human decision

## C580 — test-script-supplier-compliance-in-the-value-chain-5oj-ae-1115

Page: [[13-quality-ehs-and-compliance/test-script-supplier-compliance-in-the-value-chain-5oj-ae-1115]]

Posting period step references company code 1710 while sample data and PO use company code 3310 (AE)

**Status:** open — needs a human decision

## C581 — bom-mds-63j-493

Page: [[14-maintenance-service-and-projects/bom-mds-63j-493]]

Step 8 for SRV_BOM_02_02 labels item category group SRVP as 'プロジェクト' (project) whereas the other two service products label SRVP as 'サービス製品'.

**Status:** open — needs a human decision

## C582 — collaborative-project-management-6jn-test-script-sap-s-4hana-cloud-pub

Page: [[14-maintenance-service-and-projects/collaborative-project-management-6jn-test-script-sap-s-4hana-cloud-pub]]

Business role for several steps differs between the Overview Table and the procedure: Identify & Capture Risks (table: Project Manager, procedure logs on as Project Team Member), Document Issues (table: Project Manager, procedure: Project Team Member), Monitor and Mitigate Risks (table: Project Team Member, but Purpose says the Project Manager monitors risks).

**Status:** open — needs a human decision

## C583 — criar-produto-de-servico-configuravel-mds-5be-script-de-dados-mestre-s

Page: [[14-maintenance-service-and-projects/criar-produto-de-servico-configuravel-mds-5be-script-de-dados-mestre-s]]

Contract PSI1 price step uses material SRV_CONTRACT while the product is created as SRV_CONTR_CONFIG, likely a typo within the document

**Status:** open — needs a human decision

## C584 — criar-produto-de-servico-configuravel-mds-5be-script-de-dados-mestre-s

Page: [[14-maintenance-service-and-projects/criar-produto-de-servico-configuravel-mds-5be-script-de-dados-mestre-s]]

PVA0 example list omits an amount for C_W_T_S (standard wash)

**Status:** open — needs a human decision

## C585 — criar-produto-de-servico-configuravel-mds-5be-script-de-dados-mestre-s

Page: [[14-maintenance-service-and-projects/criar-produto-de-servico-configuravel-mds-5be-script-de-dados-mestre-s]]

Contract product step lists material type as 'Produto de serviços' while order product uses SERV; PVA0 step for CAR-WASH_CONF labels it 'contrato de prestação de serviços configurável'

**Status:** open — needs a human decision

## C586 — criar-produto-de-servico-configuravel-mds-5be-script-de-dados-mestre-s

Page: [[14-maintenance-service-and-projects/criar-produto-de-servico-configuravel-mds-5be-script-de-dados-mestre-s]]

Order class creation repeats the create-class step twice (steps 2 and 3); control code format differs (41.00.30.0 vs 41,00.30,0)

**Status:** open — needs a human decision

## C587 — internal-project-management-project-based-services-1a8-ae-test-script

Page: [[14-maintenance-service-and-projects/internal-project-management-project-based-services-1a8-ae-test-script]]

Master data and prerequisites describe Service Organization – Company AE (company code 3310, currency AED), but the work package, baseline and finance sync steps use Service Organization - Company DE (1010) and EUR amounts; project IDs also vary between INT1000, INT10002 and INT3300 across steps.

**Status:** open — needs a human decision

## C588 — internal-project-management-project-based-services-1a8-ae-test-script

Page: [[14-maintenance-service-and-projects/internal-project-management-project-based-services-1a8-ae-test-script]]

The section 'Reset Project Status to Completed (Optional)' states its purpose is to reset the project to Completed but its only change step says to choose Set Stage and select Closed.

**Status:** open — needs a human decision

## C589 — maintenance-order-processing-with-sap-field-service-management-7z2-ae

Page: [[14-maintenance-service-and-projects/maintenance-order-processing-with-sap-field-service-management-7z2-ae]]

Phase codelist mapping: the Configure Your Solution table lists the last entry (phase 09/0085, status -5) under S/4 Cmp. ID 00002, while the Central Business Configuration table lists it under 00001.

**Status:** open — needs a human decision

## C590 — master-data-script-create-configurable-service-product-mds-5be-431

Page: [[14-maintenance-service-and-projects/master-data-script-create-configurable-service-product-mds-5be-431]]

Contract price step selects material SRV_CONTRACT but then maintains SRV_CONTR_CONFIG, an internal naming inconsistency.

**Status:** open — needs a human decision

## C591 — master-data-script-create-configurable-service-product-mds-5be-431

Page: [[14-maintenance-service-and-projects/master-data-script-create-configurable-service-product-mds-5be-431]]

Service order product material type is given as 'Service Product' in contract section but 'SERV Service Product' elsewhere; item category group differs by design (SCNP for contracts, SRVP for orders).

**Status:** open — needs a human decision

## C592 — master-data-script-create-material-and-equipment-bom-for-service-mds-6

Page: [[14-maintenance-service-and-projects/master-data-script-create-material-and-equipment-bom-for-service-mds-6]]

Step 8 of SRV_BOM_02_02 gives Item Category Group SRVP labelled (Project) whereas the other two products label SRVP as (Service Product)

**Status:** open — needs a human decision

## C593 — master-data-script-create-service-product-for-service-processes-mds-3k

Page: [[14-maintenance-service-and-projects/master-data-script-create-service-product-for-service-processes-mds-3k]]

SRV_CONTRACT item category group written SNCP while GenItemGroup is SCNP, possible typo

**Status:** open — needs a human decision

## C594 — master-data-script-create-service-product-for-service-processes-mds-3k

Page: [[14-maintenance-service-and-projects/master-data-script-create-service-product-for-service-processes-mds-3k]]

SRV_CTR_RENEWAL uses item category group SRVP whereas SRV_CONTRACT uses SNCP

**Status:** open — needs a human decision

## C595 — master-data-script-create-service-product-for-service-processes-mds-3k

Page: [[14-maintenance-service-and-projects/master-data-script-create-service-product-for-service-processes-mds-3k]]

Several price steps for SRV_BUNDLE_01 and SRV_05 refer to material SRV_01 in the text (copy-paste)

**Status:** open — needs a human decision

## C596 — master-data-script-create-service-product-for-service-processes-mds-3k

Page: [[14-maintenance-service-and-projects/master-data-script-create-service-product-for-service-processes-mds-3k]]

SRV_06 is listed in the overview table but has no creation procedure

**Status:** open — needs a human decision

## C597 — material-und-equipmentstuckliste-fur-service-anlegen-sds-63j-490

Page: [[14-maintenance-service-and-projects/material-und-equipmentstuckliste-fur-service-anlegen-sds-63j-490]]

SRV_BOM_02_02 step 8 sets item category group SRVP as '(Projekt)' whereas the other service products label SRVP '(Serviceprodukt)'; step 5 refers to material SRV_BUNDLE_02 instead of SRV_BOM_02_02

**Status:** open — needs a human decision

## C598 — mds-5be-master-data-script-create-configurable-service-products-435

Page: [[14-maintenance-service-and-projects/mds-5be-master-data-script-create-configurable-service-products-435]]

PSI1 selection step uses material SRV_CONTRACT while the price condition entry uses SRV_CONTR_CONFIG

**Status:** open — needs a human decision

## C599 — mds-5be-master-data-script-create-configurable-service-products-435

Page: [[14-maintenance-service-and-projects/mds-5be-master-data-script-create-configurable-service-products-435]]

Contract product uses material type 'Service Product' while the service order product uses SERV; item category group SCNP vs SRVP

**Status:** open — needs a human decision

## C600 — operational-and-overhead-maintenance-4wm-ae-test-script-sap-s-4hana-cl

Page: [[14-maintenance-service-and-projects/operational-and-overhead-maintenance-4wm-ae-test-script-sap-s-4hana-cl]]

Complete Main Work step 3 filters on Technical object 217100091, while the sample data and all other steps use equipment 233100091 (233100093 also listed); 217100091 is not in the sample data.

**Status:** open — needs a human decision

## C601 — operational-and-overhead-maintenance-4wm-ae-test-script-sap-s-4hana-cl

Page: [[14-maintenance-service-and-projects/operational-and-overhead-maintenance-4wm-ae-test-script-sap-s-4hana-cl]]

Manage Output purpose says the maintenance planner creates work packs, but the Overview Table and the test steps assign the step to the Maintenance Supervisor.

**Status:** open — needs a human decision

## C602 — reactive-maintenance-4hh-ae-test-script-sap-s-4hana-cloud-public-editi

Page: [[14-maintenance-service-and-projects/reactive-maintenance-4hh-ae-test-script-sap-s-4hana-cloud-public-editi]]

Sample equipment is 233100091 in prerequisites and most steps, but notification creation steps (create notification, emergency, minor work) use technical object 217100091 labelled Cooling Water Circulation Pump.

**Status:** open — needs a human decision

## C603 — sap-s-4hana-cloud-public-edition-3kv-349

Page: [[14-maintenance-service-and-projects/sap-s-4hana-cloud-public-edition-3kv-349]]

SRV_BUNDLE_01 and SRV_05 price steps say they update item SRV_01 in the instruction text, inconsistent with their own item selection.

**Status:** open — needs a human decision

## C604 — sap-s-4hana-cloud-public-edition-3kv-349

Page: [[14-maintenance-service-and-projects/sap-s-4hana-cloud-public-edition-3kv-349]]

SRV_06 (serialized stock spare part) is listed in the overview table but has no creation procedure.

**Status:** open — needs a human decision

## C605 — sap-s-4hana-cloud-public-edition-mds-5be-433

Page: [[14-maintenance-service-and-projects/sap-s-4hana-cloud-public-edition-mds-5be-433]]

Contract price step uses item SRV_CONTRACT in selection but SRV_CONTR_CONFIG in price entry; tax classification described as 1 (全課税) for contract/variant but 1 (正規税) for service order item

**Status:** open — needs a human decision

## C606 — script-de-dados-mestre-criar-lista-tecnica-de-material-e-equipamento-p

Page: [[14-maintenance-service-and-projects/script-de-dados-mestre-criar-lista-tecnica-de-material-e-equipamento-p]]

SRV_BOM_02_02 step 8 lists item category group SRVP as '(projeto)' whereas the other products label SRVP as 'produto de serviços'

**Status:** open — needs a human decision

## C607 — script-de-dados-mestre-criar-produto-de-servicos-para-operacao-de-serv

Page: [[14-maintenance-service-and-projects/script-de-dados-mestre-criar-produto-de-servicos-para-operacao-de-serv]]

SRV_06 is listed in the overview table but has no creation procedure in the document

**Status:** open — needs a human decision

## C608 — script-de-dados-mestre-criar-produto-de-servicos-para-operacao-de-serv

Page: [[14-maintenance-service-and-projects/script-de-dados-mestre-criar-produto-de-servicos-para-operacao-de-serv]]

Some price steps for SRV_BUNDLE_01 and SRV_05 refer to material SRV_01 in instructions/results (copy-paste inconsistency)

**Status:** open — needs a human decision

## C609 — script-de-dados-mestre-criar-produto-de-servicos-para-operacao-de-serv

Page: [[14-maintenance-service-and-projects/script-de-dados-mestre-criar-produto-de-servicos-para-operacao-de-serv]]

Overview says SRV_03/SRV_04 are 'only supplied' non-stock, while the SRV_03 outline label says undefined and SRV_04 defined spare part; SRV_05 item group given as 'SVST or NORM' alternatives

**Status:** open — needs a human decision

## C610 — script-de-datos-maestros-creacion-de-producto-de-servicio-configurable

Page: [[14-maintenance-service-and-projects/script-de-datos-maestros-creacion-de-producto-de-servicio-configurable]]

Document is machine-translated and unreviewed; some values inconsistent: condition TELETELÉFONO, 'TRIMESTRAL' vs QUARTERLY, 'AÑO' vs YEARLY, contract price material SRV_CONTRACT vs SRV_CONTR_CONFIG, CAR-WASH_CONF vs CAR_WASH_CONF.

**Status:** open — needs a human decision

## C611 — script-de-datos-maestros-creacion-de-producto-de-servicio-configurable

Page: [[14-maintenance-service-and-projects/script-de-datos-maestros-creacion-de-producto-de-servicio-configurable]]

Contract-order characteristics use 'Valores múltiples' while service-order ones use single values; the service-order class section says the characteristics belong to the 'service contract class' in the summary table.

**Status:** open — needs a human decision

## C612 — script-de-datos-maestros-creacion-de-producto-de-servicio-para-proceso

Page: [[14-maintenance-service-and-projects/script-de-datos-maestros-creacion-de-producto-de-servicio-para-proceso]]

Machine-translated and unreviewed; some inconsistencies inside: SRV_BUNDLE_01 and SRV_05 price steps refer to 'material SRV_01'; SRV_06 listed in the ID table but has no procedure

**Status:** open — needs a human decision

## C613 — script-de-datos-maestros-creacion-de-producto-de-servicio-para-proceso

Page: [[14-maintenance-service-and-projects/script-de-datos-maestros-creacion-de-producto-de-servicio-para-proceso]]

Some products flagged cloud-only, others cloud and on-premise; may differ from other scope item scripts

**Status:** open — needs a human decision

## C614 — script-de-datos-maestros-crear-lista-de-materiales-para-material-y-equ

Page: [[14-maintenance-service-and-projects/script-de-datos-maestros-crear-lista-de-materiales-para-material-y-equ]]

Step 8 of SRV_BOM_02_02 labels item category group SRVP as '(proyecto)' while the other products label it '(producto de servicio)'

**Status:** open — needs a human decision

## C615 — service-order-processing-with-sap-field-service-management-49x-ae-test

Page: [[14-maintenance-service-and-projects/service-order-processing-with-sap-field-service-management-49x-ae-test]]

Overview Table says the key characteristic of this process variant is that total billed amount is calculated on time and material, while the service order test procedures create a 'Fixed Price Order' with items billed on a fixed price basis.

**Status:** open — needs a human decision

## C616 — solution-order-advanced-product-bundling-6bu-ae-1163

Page: [[14-maintenance-service-and-projects/solution-order-advanced-product-bundling-6bu-ae-1163]]

The bought-in info record (CBAB) step enters condition Amount 300 AED, while the following note says the net price for material TG14 and supplier 33300001 is 35 AED (and a repeat at 25 AED).

**Status:** open — needs a human decision

## C617 — solution-order-advanced-product-bundling-6bu-ae-1163

Page: [[14-maintenance-service-and-projects/solution-order-advanced-product-bundling-6bu-ae-1163]]

Master data and order steps use sales organization 3310 and customer 33100001/33100003, but the bundle-specific price condition steps and the PSP0 condition record use sales organization 1710, customer 10100001 and USD/EUR currency, while the AE info record uses AED.

**Status:** open — needs a human decision

## C618 — stammdatenskript-sap-s-4hana-cloud-public-edition-serviceprodukt-fur-s

Page: [[14-maintenance-service-and-projects/stammdatenskript-sap-s-4hana-cloud-public-edition-serviceprodukt-fur-s]]

SRV_06 is listed in the overview table but has no creation procedure in the document

**Status:** open — needs a human decision

## C619 — stammdatenskript-sap-s-4hana-cloud-public-edition-serviceprodukt-fur-s

Page: [[14-maintenance-service-and-projects/stammdatenskript-sap-s-4hana-cloud-public-edition-serviceprodukt-fur-s]]

Minor internal inconsistencies: SRV_03 purchasing example material group YBM00 vs YBMM00 in basic data; SRV_BUNDLE_01 and SRV_05 price steps mention material SRV_01 in text; SRV_05 price result text mentions SRV_01

**Status:** open — needs a human decision

## C620 — stammdatenskript-sap-s-4hana-cloud-public-edition-serviceprodukt-fur-s

Page: [[14-maintenance-service-and-projects/stammdatenskript-sap-s-4hana-cloud-public-edition-serviceprodukt-fur-s]]

Item group field labelled GenItemGroup in some steps and AllgPosGrp in others

**Status:** open — needs a human decision

## C621 — test-script-credit-and-debit-memo-processing-for-service-management-4g

Page: [[14-maintenance-service-and-projects/test-script-credit-and-debit-memo-processing-for-service-management-4g]]

Debit memo request for corrected and actual amount, step 10 is titled 'Adjust the Amount for PPR0' but the instruction says to adjust the amount for condition PSI1; unclear which pricing condition type is intended.

**Status:** open — needs a human decision

## C622 — test-script-field-logistics-planning-and-execution-40g-ae-sap-s-4hana-

Page: [[14-maintenance-service-and-projects/test-script-field-logistics-planning-and-execution-40g-ae-sap-s-4hana-part-01]]

Create Technical Object enters company code 1710, while the sample data table lists company code 3310 for the plants used in the test.

**Status:** open — needs a human decision

## C623 — test-script-field-logistics-planning-and-execution-40g-ae-sap-s-4hana-

Page: [[14-maintenance-service-and-projects/test-script-field-logistics-planning-and-execution-40g-ae-sap-s-4hana-part-01]]

The Overview Table assigns Post Goods Receipt at Remote plant to Warehouse Clerk (EWM) with app F0843 and Post Goods Issue from Base plant to MIGO_GI, whereas the procedures use Receiving Specialist (IOG) with Process Receipts (F5316) and Warehouse Clerk (EWM) with Manage Outbound Delivery Orders (F6498).

**Status:** open — needs a human decision

## C624 — test-script-field-logistics-planning-and-execution-40g-ae-sap-s-4hana-

Page: [[14-maintenance-service-and-projects/test-script-field-logistics-planning-and-execution-40g-ae-sap-s-4hana-part-01]]

Single Plant Setup intro says the SP14 sequence runs from Convert Purchase Requisition to Purchase Order through Record Inspection Results, while section Direct Purchase for Single Plant says it runs through Post Goods Issue for Maintenance Order.

**Status:** open — needs a human decision

## C625 — test-script-field-logistics-planning-and-execution-supplier-items-4ah

Page: [[14-maintenance-service-and-projects/test-script-field-logistics-planning-and-execution-supplier-items-4ah]]

Limit PR values differ between sections: Overall Limit 10 / Expected Value 10 in 'Create Limit PR for Rental / Renewal Extension' versus Overall Limit 1000 / Expected Value 100 in 'Renew Rentals'.

**Status:** open — needs a human decision

## C626 — test-script-field-logistics-planning-and-execution-supplier-items-4ah

Page: [[14-maintenance-service-and-projects/test-script-field-logistics-planning-and-execution-supplier-items-4ah]]

Remote warehouse task destination bin is GENERAL-AREA in 'Receive Supplier Item at Remote > Process Receipt' but GEN-AREA in the following 'Complete Open Warehouse Tasks' purpose text.

**Status:** open — needs a human decision

## C627 — test-script-improvement-maintenance-4vt-ae-sap-s-4hana-cloud-public-ed

Page: [[14-maintenance-service-and-projects/test-script-improvement-maintenance-4vt-ae-sap-s-4hana-cloud-public-ed]]

Role for Manage Output differs inside the document: its Purpose says 'the maintenance planner can search and apply filters ... and create work pack', while the Overview Table and the test steps assign the step to the Maintenance Supervisor.

**Status:** open — needs a human decision

## C628 — test-script-maintenance-resource-scheduling-43r-ae-sap-s-4hana-cloud-p

Page: [[14-maintenance-service-and-projects/test-script-maintenance-resource-scheduling-43r-ae-sap-s-4hana-cloud-p]]

Internal inconsistency on prerequisite scope items: Business Conditions lists BH1, BH2, 4HH, 4HI, 4VT, 4WM (no BJ2), while Preceding Processes lists BH1, BH2, BJ2, 4HH, 4HI (no 4VT or 4WM); Succeeding Processes lists all seven including BJ2, 4VT and 4WM.

**Status:** open — needs a human decision

## C629 — test-script-sap-maintenance-assistant-4rv-sap-s-4hana-cloud-public-edi

Page: [[14-maintenance-service-and-projects/test-script-sap-maintenance-assistant-4rv-sap-s-4hana-cloud-public-edi]]

The overview table lists the 'Set Assignment Type for Service Orders' step under Configuration Expert (Maintenance Assistant) and again as 'Setting the Assignment Type for Service Orders' under Service Technician - Customer Service, while the procedure itself is performed by the Configuration Expert (SAP_BR_MAIF_CONFIG_EXPERT).

**Status:** open — needs a human decision

## C630 — test-script-sap-s-4hana-cloud-public-edition-engineer-products-and-sys

Page: [[14-maintenance-service-and-projects/test-script-sap-s-4hana-cloud-public-edition-engineer-products-and-sys]]

Approve Purchase Order step in the long lead components section states approval is needed for purchase group 003 and PO > 500 AED, while the same step elsewhere and the workflow configuration use purchase group 001.

**Status:** open — needs a human decision

## C631 — test-script-sap-s-4hana-cloud-public-edition-engineer-products-and-sys

Page: [[14-maintenance-service-and-projects/test-script-sap-s-4hana-cloud-public-edition-engineer-products-and-sys]]

Re-upload of planned costs sample template uses company code 1010 while the initial upload and the rest of the script use company code 3310.

**Status:** open — needs a human decision

## C632 — test-script-sap-s-4hana-cloud-public-edition-engineer-products-and-sys

Page: [[14-maintenance-service-and-projects/test-script-sap-s-4hana-cloud-public-edition-engineer-products-and-sys]]

Approval step references app My Inbox - All Items as F5331 in the first procurement block but F0862 in later blocks.

**Status:** open — needs a human decision

## C633 — test-script-sap-s-4hana-cloud-public-edition-engineer-products-and-sys

Page: [[14-maintenance-service-and-projects/test-script-sap-s-4hana-cloud-public-edition-engineer-products-and-sys]]

Document says Business Role 'Project Manager - Commercial Services' in the overview table while the Roles section lists Project Manager (SAP_BR_PROJECTMANAGER).

**Status:** open — needs a human decision

## C634 — test-script-sap-s-4hana-cloud-public-edition-engineer-products-and-sys

Page: [[14-maintenance-service-and-projects/test-script-sap-s-4hana-cloud-public-edition-engineer-products-and-sys]]

Release Production Order step lists area of responsibility 'MTO w/o VC Val. (YB9)' for FG0611 but 'ETO w/o VC Val. (YB9)' for FG0612 with the same code YB9.

**Status:** open — needs a human decision

## C635 — test-script-sap-s-4hana-cloud-public-edition-field-logistics-planning

Page: [[14-maintenance-service-and-projects/test-script-sap-s-4hana-cloud-public-edition-field-logistics-planning]]

Remote receipt is tested with Process Receipts (F5316), and the overview table also lists F5316 for Receive at remote, but the same section says F5316 does not support remote receipt in the intercompany code scenario (F4713 recommended) and the return section assumes items were received at remote using F4713.

**Status:** open — needs a human decision

## C636 — test-script-sap-s-4hana-cloud-public-edition-in-house-repair-3xk-ae-98

Page: [[14-maintenance-service-and-projects/test-script-sap-s-4hana-cloud-public-edition-in-house-repair-3xk-ae-98]]

Outbound delivery availability prerequisite is worded inconsistently: 'Received by Repair Center', 'Received by Customer Repair Center' and 'Received In Repair Center' appear in different sections.

**Status:** open — needs a human decision

## C637 — test-script-sap-s-4hana-cloud-public-edition-in-house-repair-3xk-ae-98

Page: [[14-maintenance-service-and-projects/test-script-sap-s-4hana-cloud-public-edition-in-house-repair-3xk-ae-98]]

Sample org data conflicts within the script: configuration/master data use plant/shipping point 3310/331R while customer returns steps use 1010/101R and customer 10100001.

**Status:** open — needs a human decision

## C638 — test-script-sap-s-4hana-cloud-public-edition-solution-order-management

Page: [[14-maintenance-service-and-projects/test-script-sap-s-4hana-cloud-public-edition-solution-order-management]]

Bought-in purchasing info record (TG14, supplier 33300001) is created with condition Amount 300 AED and purchasing group 002, but follow-on notes say net price is 35 AED, then repeat with purchasing group 001 and net price 25 AED; values are not clearly reconciled.

**Status:** open — needs a human decision

## C639 — test-script-sap-s-4hana-cloud-public-edition-solution-order-management

Page: [[14-maintenance-service-and-projects/test-script-sap-s-4hana-cloud-public-edition-solution-order-management]]

Create Billing Document (Project Item) expected result lists Unbilled 400 EUR, Written Off 300 EUR, Billed 300 EUR, which does not obviously match the planned billing amounts of 500.00 (fixed price) and 1000.00 (time and expense) in Plan Customer Project.

**Status:** open — needs a human decision

## C640 — test-script-sap-s-4hana-cloud-public-edition-time-recording-1q4-ae-754

Page: [[14-maintenance-service-and-projects/test-script-sap-s-4hana-cloud-public-edition-time-recording-1q4-ae-754]]

Validation BAdI is named HCM_CATS_V1_TS_VALIDATION in the preliminary steps but HCM_CATS_V1_B_TS_VALIDATION in the test step 7 note.

**Status:** open — needs a human decision

## C641 — test-script-service-contract-management-3mo-ae-sap-s-4hana-cloud-publi

Page: [[14-maintenance-service-and-projects/test-script-service-contract-management-3mo-ae-sap-s-4hana-cloud-publi]]

Internal contradiction in Schedule Billing Document Request Creation: steps say leave both BDR Creation Horizon (in days) and Service Contract IDs empty to schedule all contracts, but a note says either field must be specified and both cannot be empty.

**Status:** open — needs a human decision

## C642 — test-script-service-contract-management-3mo-ae-sap-s-4hana-cloud-publi

Page: [[14-maintenance-service-and-projects/test-script-service-contract-management-3mo-ae-sap-s-4hana-cloud-publi]]

Sample data lists Sales Organization 3310 (with UAE customer 33100001), but the renewal procedures instruct entering Sales Organization 1010 for the same customer.

**Status:** open — needs a human decision

## C643 — test-script-service-quotation-4ga-ae-sap-s-4hana-cloud-public-edition

Page: [[14-maintenance-service-and-projects/test-script-service-quotation-4ga-ae-sap-s-4hana-cloud-public-edition]]

Overview table for Service Bundle lists Accept and Reject expected results swapped (Accept says rejected, Reject says accepted); several overview sections reuse the same time-and-material description and links for different variants.

**Status:** open — needs a human decision

## C644 — test-script-warranty-claim-management-supplier-recovery-processing-5hr

Page: [[14-maintenance-service-and-projects/test-script-warranty-claim-management-supplier-recovery-processing-5hr]]

Validate Supplier Claim and Maintain Supplier Response say a validated claim goes straight to Waiting for Supplier Response (Send to Supplier runs automatically), but the Reject Supplier Claim steps show validation ending at Successfully Validated and then a separate manual Send to Supplier step.

**Status:** open — needs a human decision

## C645 — warranty-claim-management-customer-claim-processing-63y-ae-test-script

Page: [[14-maintenance-service-and-projects/warranty-claim-management-customer-claim-processing-63y-ae-test-script]]

Labor pricing condition is checked for material SRV_01, but the claim labor item is created with material CSSRV_01; the sample data may be inconsistent.

**Status:** open — needs a human decision

## C646 — warranty-claim-management-customer-claim-processing-63y-ae-test-script

Page: [[14-maintenance-service-and-projects/warranty-claim-management-customer-claim-processing-63y-ae-test-script]]

Validate Customer Claim says Formal Validation automatically runs Complete Inbound Process, Content Validation and Post to Finance and sets Claim Posted, yet steps 7 and 8 then run Complete Inbound Process and Content Validation manually, expecting Ready for Content Validation and Content Validation Successful; the status sequence is unclear.

**Status:** open — needs a human decision

## C647 — empties-for-retail-5fk-ae-test-script-sap-s-4hana-cloud-public-edition

Page: [[15-retail-operations/empties-for-retail-5fk-ae-test-script-sap-s-4hana-cloud-public-edition-part-01]]

Post Inventory Count Differences purpose says the store manager posts differences, but the steps and Overview Table assign posting to the Inventory Manager (Retail) in F0379A.

**Status:** open — needs a human decision

## C648 — empties-for-retail-5fk-ae-test-script-sap-s-4hana-cloud-public-edition

Page: [[15-retail-operations/empties-for-retail-5fk-ae-test-script-sap-s-4hana-cloud-public-edition-part-02]]

Step 9 uses Reservation Hand Over, which the same step says is for Not Paid orders only, inside a section titled Click-and-Collect (Pre-Paid Order); pre-paid orders would use Hand Over instead.

**Status:** open — needs a human decision

## C649 — in-store-customer-order-management-3hu-ae-test-script-sap-s-4hana-clou

Page: [[15-retail-operations/in-store-customer-order-management-3hu-ae-test-script-sap-s-4hana-clou]]

Schedule Delivery Creation (F2228) is assigned to the Purchaser (Retail) role in the Overview Table but the test procedure logs on as Shipping Specialist.

**Status:** open — needs a human decision

## C650 — invoice-verification-for-retail-5fn-ae-test-script-sap-s-4hana-cloud-p

Page: [[15-retail-operations/invoice-verification-for-retail-5fn-ae-test-script-sap-s-4hana-cloud-p]]

Internal data inconsistency: master data and UI steps use company code 3310 and currency EUR (F0859 step), while the sample API payload uses CompanyCode 1010 and DocumentCurrency AED; plant 3350 and supplier 33213002 are the same in both.

**Status:** open — needs a human decision

## C651 — outbound-logistics-for-distribution-centers-5fv-ae-test-script-1090

Page: [[15-retail-operations/outbound-logistics-for-distribution-centers-5fv-ae-test-script-1090]]

Initial stock is posted to storage location 995A while the sample data and the STO use storage location 994A for the supplying side, which may be an internal inconsistency.

**Status:** open — needs a human decision

## C652 — retail-logistics-with-third-party-warehouse-management-69m-ae-test-scr

Page: [[15-retail-operations/retail-logistics-with-third-party-warehouse-management-69m-ae-test-scr]]

Config step 'Define default values for deliveries' sets Shipping Point 3310, while the master data table and later steps use shipping point 3350 for plant 3350 (3310 is the sales and purchasing org); possibly inconsistent with the sample data.

**Status:** open — needs a human decision

## C653 — returns-from-store-5fr-ae-1086

Page: [[15-retail-operations/returns-from-store-5fr-ae-1086]]

Preliminary steps name 3HQ both as 'In-Store Merchandise Management' and 'Ordering, Receiving and Customer Inquiry in Store'

**Status:** open — needs a human decision

## C654 — sales-from-distribution-center-3hs-ae-test-script-sap-s-4hana-cloud-pu

Page: [[15-retail-operations/sales-from-distribution-center-3hs-ae-test-script-sap-s-4hana-cloud-pu]]

Advanced intercompany Part 2 example mentions Sales Organization 1010, Tax Departure DE, transit plant 1010 and plant 1710, inconsistent with the 3310/AE/3350 sample data; and the Financial Posting rule cites Italian FI types (W1/W2/W3) and an invoice form template SDBIL_INVOICE_RU, inconsistent with the UAE scope.

**Status:** open — needs a human decision

## C655 — test-script-merchandise-allocation-5fl-ae-sap-s-4hana-cloud-public-edi

Page: [[15-retail-operations/test-script-merchandise-allocation-5fl-ae-sap-s-4hana-cloud-public-edi]]

Change Returns Purchase Order: purpose says to change the PO item storage location to the returns storage location, but the step enters 995A (listed in sample data as 'Storage Loc. DC'); 995R is the listed 'St.Loc.Return'.

**Status:** open — needs a human decision

## C656 — test-script-omnichannel-order-fulfillment-for-retail-5fz-ae-sap-s-4han

Page: [[15-retail-operations/test-script-omnichannel-order-fulfillment-for-retail-5fz-ae-sap-s-4han]]

The BAdI for click-and-collect sales order payment status is named RFM_STR_PICK_ORD_PAYT_STS_MOD in the Business Conditions note but RFM_STORE_PICK_ORD_PAYT_STS in the Appendix Create Sales Order purpose; the two names differ within the same document.

**Status:** open — needs a human decision

## C657 — test-script-omnichannel-sales-promotion-opps-consumer-products-7t7-ae

Page: [[15-retail-operations/test-script-omnichannel-sales-promotion-opps-consumer-products-7t7-ae]]

Role naming is inconsistent inside the document: the Overview Table lists 'Configuration Specialist' as the business role for Maintain Promotion Rule steps, while the Roles prerequisite table and the step instructions use 'Promotion Planner' (Maintain_OPPS_Promotions); 'Configuration Specialist' (used for OPPS number ranges, configurations and identifier formats) is not defined in the Roles table.

**Status:** open — needs a human decision

## C658 — test-script-procurement-for-retail-5fm-ae-sap-s-4hana-cloud-public-edi

Page: [[15-retail-operations/test-script-procurement-for-retail-5fm-ae-sap-s-4hana-cloud-public-edi]]

Overview Table gives the Expected Results for 'Output from a Purchase Order' as 'output via EDI is enabled' and for 'Purchase Order EDI Output' as 'Message output is generated to print', which looks swapped relative to the test procedures (the print procedure displays the PRINT channel preview, the EDI procedure verifies the EDI channel line).

**Status:** open — needs a human decision

## C659 — test-script-retail-logistics-with-embedded-warehouse-management-69l-ae

Page: [[15-retail-operations/test-script-retail-logistics-with-embedded-warehouse-management-69l-ae]]

Sample data and preliminary steps use warehouse 3350, plant 3350, storage location 995W and articles R_7000/R_7003, but Confirm Inventory Count Results, Analyze Differences and Create Posting Changes use warehouse number 1750, and Transfer Stock - In-Plant uses plant 1710, storage location 175W and material TG11.

**Status:** open — needs a human decision

## C660 — test-script-retail-logistics-with-embedded-warehouse-management-69l-ae

Page: [[15-retail-operations/test-script-retail-logistics-with-embedded-warehouse-management-69l-ae]]

Define Default Values for Deliveries sets Shipping Point 3310, while the sample master data lists Shipping Point 3350 (SP DC 3350).

**Status:** open — needs a human decision

## C661 — test-script-retail-logistics-with-embedded-warehouse-management-69l-ae

Page: [[15-retail-operations/test-script-retail-logistics-with-embedded-warehouse-management-69l-ae]]

Maintain Warehouse Product Attributes says Putaway and Stock Removal Control Indicators must be maintained differently for the replenishment process, yet the step enters SG01 for both.

**Status:** open — needs a human decision

## C662 — test-script-sales-pricing-for-retail-3i4-ae-sap-s-4hana-cloud-public-e

Page: [[15-retail-operations/test-script-sales-pricing-for-retail-3i4-ae-sap-s-4hana-cloud-public-e]]

Business role mismatch: the Overview Table lists 'Master Data Specialist - Product Data (Retail)' for Maintain Price List Type for Site and Merchandise Category (WB30N), but the test procedure's log-on step uses 'Master Data Specialist - Location Data (Retail)'.

**Status:** open — needs a human decision

## C663 — test-script-seasons-for-retail-6di-ae-sap-s-4hana-cloud-public-edition

Page: [[15-retail-operations/test-script-seasons-for-retail-6di-ae-sap-s-4hana-cloud-public-edition]]

Test data sets sales, purchase and stock transfer periods from <Current Date> to a fixed 31.12.2024, while the script is dated 19-06-26 and (c) 2026; following the steps literally would give a period ending before the current date.

**Status:** open — needs a human decision

## C664 — test-script-supplier-consignment-for-retail-71p-ae-sap-s-4hana-cloud-p

Page: [[15-retail-operations/test-script-supplier-consignment-for-retail-71p-ae-sap-s-4hana-cloud-p]]

Purchasing group is 002 in the article master and consignment PO steps but 001 in the optional manual STO steps (DC to store).

**Status:** open — needs a human decision

## C665 — test-script-supplier-consignment-for-retail-71p-ae-sap-s-4hana-cloud-p

Page: [[15-retail-operations/test-script-supplier-consignment-for-retail-71p-ae-sap-s-4hana-cloud-p]]

Display Customer step uses customer 33113008 in one scenario but 10113008 in the later-pickup scenario, while the sample data lists 33113008.

**Status:** open — needs a human decision

## C666 — test-script-process-integration-of-sap-s-4hana-finance-with-central-fi

Page: [[16-two-tier-erp-and-central-finance/test-script-process-integration-of-sap-s-4hana-finance-with-central-fi]]

Template placeholders remain (e.g. 'To Author' notes, <choose the appropriate entity>); roles table lists role template names only, and system access lists customer-specific test systems.

**Status:** open — needs a human decision

## C667 — two-tier-central-financial-compliance-management-225

Page: [[16-two-tier-erp-and-central-finance/two-tier-central-financial-compliance-management-225]]

Cover says SAP Cloud ERP June 2026 but revision history shows only 05.04.2021 initial version and copyright 2024; currency unclear

**Status:** open — needs a human decision

## C668 — two-tier-consolidation-of-autonomous-subsidiaries-via-central-finance

Page: [[16-two-tier-erp-and-central-finance/two-tier-consolidation-of-autonomous-subsidiaries-via-central-finance]]

Overview table lists AP_ACCOUNTANT for Create Outgoing Invoice and Post Incoming Payments, while test procedures use AR_ACCOUNTANT

**Status:** open — needs a human decision

## C669 — two-tier-consolidation-of-autonomous-subsidiaries-via-central-finance

Page: [[16-two-tier-erp-and-central-finance/two-tier-consolidation-of-autonomous-subsidiaries-via-central-finance]]

Document header says SAP Cloud ERP June 2026 but revision history ends 2020 and copyright says 2024

**Status:** open — needs a human decision

## C670 — two-tier-erp-integrated-financial-planning-with-sap-analytics-cloud-22

Page: [[16-two-tier-erp-and-central-finance/two-tier-erp-integrated-financial-planning-with-sap-analytics-cloud-22]]

Cover says June 2026 release but revision history and copyright date from 2021; content may be dated

**Status:** open — needs a human decision

## C671 — two-tier-erp-integration-setup-document-230

Page: [[16-two-tier-erp-and-central-finance/two-tier-erp-integration-setup-document-230]]

Cover says SAP Cloud ERP June 2026 but the last revision is dated 31.03.2021 and the copyright 2020, so content may be outdated relative to release 2608.

**Status:** open — needs a human decision

## C672 — two-tier-erp-procurement-by-subsidiary-from-headquarters-replenishment

Page: [[16-two-tier-erp-and-central-finance/two-tier-erp-procurement-by-subsidiary-from-headquarters-replenishment]]

IDoc names inconsistent within document: DELVRY07/INVOIC2 in technical requirements vs DESADV/INVOIC02 in HQ configuration

**Status:** open — needs a human decision

## C673 — two-tier-erp-procurement-by-subsidiary-from-headquarters-replenishment

Page: [[16-two-tier-erp-and-central-finance/two-tier-erp-procurement-by-subsidiary-from-headquarters-replenishment]]

Document is dated revision 2 (2021) and copyright 2019/2025 but labelled June 2026; may be stale

**Status:** open — needs a human decision

## C674 — two-tier-erp-procurement-by-subsidiary-from-headquarters-replenishment

Page: [[16-two-tier-erp-and-central-finance/two-tier-erp-procurement-by-subsidiary-from-headquarters-replenishment]]

Test script section partly reuses Materials Requirements Planning content (e.g. 'TG011' typo, 'Goods Issue' wording for goods receipt job)

**Status:** open — needs a human decision

## C675 — two-tier-erp-scenario-integrated-multiple-specification-inspection-in

Page: [[16-two-tier-erp-and-central-finance/two-tier-erp-scenario-integrated-multiple-specification-inspection-in]]

Header says SAP Cloud ERP June 2026 but copyright and revision date are 2023; scope item links reference 2302 package

**Status:** open — needs a human decision

## C676 — two-tier-erp-service-order-management-in-headquarter-subsidiary-model

Page: [[16-two-tier-erp-and-central-finance/two-tier-erp-service-order-management-in-headquarter-subsidiary-model]]

Integration point 2 is described as 'Subsidiary confirms delivery date' in one list and as 'confirms the service order, PO updated' in another

**Status:** open — needs a human decision

## C677 — two-tier-erp-subsidiary-as-sales-office-drop-shipment-from-headquarter

Page: [[16-two-tier-erp-and-central-finance/two-tier-erp-subsidiary-as-sales-office-drop-shipment-from-headquarter]]

Section 4.2 lists IDocs DELVRY07 and INVOIC2, but section 5.2.1 lists DESADV and INVOIC02 for the same ASN and billing messages.

**Status:** open — needs a human decision

## C678 — two-tier-erp-subsidiary-as-sales-office-drop-shipment-from-headquarter

Page: [[16-two-tier-erp-and-central-finance/two-tier-erp-subsidiary-as-sales-office-drop-shipment-from-headquarter]]

Approval threshold stated as 500 USD in workflow configuration but 500 EUR in the approval step.

**Status:** open — needs a human decision

## C679 — two-tier-erp-subsidiary-as-sales-office-drop-shipment-from-headquarter

Page: [[16-two-tier-erp-and-central-finance/two-tier-erp-subsidiary-as-sales-office-drop-shipment-from-headquarter]]

Cover says June 2026 while copyright says 2020 and last revision is 2021.

**Status:** open — needs a human decision

## C680 — two-tier-erp-subsidiary-as-sales-office-drop-shipment-from-headquarter

Page: [[16-two-tier-erp-and-central-finance/two-tier-erp-subsidiary-as-sales-office-drop-shipment-from-headquarter]]

Master data text refers to 'section 5.3' which does not exist; sample vendor 10300084 vs HQ ID 10300089 in config examples.

**Status:** open — needs a human decision

## C681 — two-tier-master-data-replication-business-partner-master-customer-233

Page: [[16-two-tier-erp-and-central-finance/two-tier-master-data-replication-business-partner-master-customer-233]]

Cover says June 2026 but test systems are S/4HANA 2021 and release 2102 with revision dated 2020; possibly stale

**Status:** open — needs a human decision

## C682 — two-tier-master-data-replication-business-partner-master-customer-233

Page: [[16-two-tier-erp-and-central-finance/two-tier-master-data-replication-business-partner-master-customer-233]]

Terminology differs from sibling supplier guide (SAP Cloud ERP vs SAP S/4HANA Cloud Public Edition for the subsidiary system)

**Status:** open — needs a human decision

## C683 — two-tier-master-data-replication-product-master-customer-guide-234

Page: [[16-two-tier-erp-and-central-finance/two-tier-master-data-replication-product-master-customer-guide-234]]

Test systems listed (S4HANA 1909, release 2005) and 2017-2021 revision history look outdated versus the 2608/June 2026 library release

**Status:** open — needs a human decision

## C684 — two-tier-master-data-replication-product-master-customer-guide-234

Page: [[16-two-tier-erp-and-central-finance/two-tier-master-data-replication-product-master-customer-guide-234]]

Test step 3 refers to material number 'created in Step 5.4.1' while the change check refers to 'Step 4.1' - internal reference inconsistency

**Status:** open — needs a human decision

## C685 — two-tier-master-data-replication-supplier-master-235

Page: [[16-two-tier-erp-and-central-finance/two-tier-master-data-replication-supplier-master-235]]

Cover says June 2026 / 2608 but test systems listed are S/4HANA 2021 and Public Edition release 2102 with revision dated 2021; possibly stale content

**Status:** open — needs a human decision

## C686 — two-tier-master-data-replication-supplier-master-235

Page: [[16-two-tier-erp-and-central-finance/two-tier-master-data-replication-supplier-master-235]]

Contains a test user with a hard-coded example password

**Status:** open — needs a human decision

## C687 — two-tier-multi-level-project-scenario-eppm-customer-guide-243

Page: [[16-two-tier-erp-and-central-finance/two-tier-multi-level-project-scenario-eppm-customer-guide-243]]

Title page says SAP Cloud ERP June 2026 but revision history ends 2020 and copyright reads 2025

**Status:** open — needs a human decision

## C688 — two-tier-procurement-directly-by-subsidiary-with-visibility-to-headqua

Page: [[16-two-tier-erp-and-central-finance/two-tier-procurement-directly-by-subsidiary-with-visibility-to-headqua]]

Create delivery document section says 'create the return delivery' and billing uses Credit Memo for Returns (CBRE), which seems inconsistent with the outbound sales flow described in Purpose.

**Status:** open — needs a human decision

## C689 — two-tier-procurement-directly-by-subsidiary-with-visibility-to-headqua

Page: [[16-two-tier-erp-and-central-finance/two-tier-procurement-directly-by-subsidiary-with-visibility-to-headqua]]

Test script uses sales org 1710 and customer 17100001 in the sales order step while the master data table lists sales org 3010 and customer 30100001.

**Status:** open — needs a human decision

## C690 — two-tier-project-based-services-procurement-between-headquarter-and-su

Page: [[16-two-tier-erp-and-central-finance/two-tier-project-based-services-procurement-between-headquarter-and-su]]

Cover says June 2026 / 2608 but copyright is 2020 and last revision 10.05.2020, so content may be stale

**Status:** open — needs a human decision

## C691 — two-tier-project-based-services-procurement-between-headquarter-and-su

Page: [[16-two-tier-erp-and-central-finance/two-tier-project-based-services-procurement-between-headquarter-and-su]]

Test script contains leftover tester comments (e.g. 'Could not find APP Manage Credit Memo Request Workflow', 'Fiori App Team Utilization not found', 'No specific user ID?') suggesting some apps/steps may not be available

**Status:** open — needs a human decision

## C692 — two-tier-project-based-services-procurement-between-headquarter-and-su

Page: [[16-two-tier-erp-and-central-finance/two-tier-project-based-services-procurement-between-headquarter-and-su]]

Billing section lists three possibilities but items 2 and 3 are identical text

**Status:** open — needs a human decision

## C693 — two-tier-project-based-services-procurement-between-headquarter-and-su

Page: [[16-two-tier-erp-and-central-finance/two-tier-project-based-services-procurement-between-headquarter-and-su]]

Cross-references to chapters 7.3.5/7.3.6 and 2.4.2 do not match this document's numbering

**Status:** open — needs a human decision

## C694 — two-tier-sale-from-local-stock-by-subsidiary-249

Page: [[16-two-tier-erp-and-central-finance/two-tier-sale-from-local-stock-by-subsidiary-249]]

Payment Information at Headquarter purpose says it views 'Stock information' though it concerns receivables (copy/paste error)

**Status:** open — needs a human decision

## C695 — two-tier-sale-from-local-stock-by-subsidiary-249

Page: [[16-two-tier-erp-and-central-finance/two-tier-sale-from-local-stock-by-subsidiary-249]]

Cover says June 2026 while copyright says 2020 and last revision is 2021

**Status:** open — needs a human decision

## C696 — two-tier-sale-from-local-stock-by-subsidiary-249

Page: [[16-two-tier-erp-and-central-finance/two-tier-sale-from-local-stock-by-subsidiary-249]]

Intro calls the process a 'subcontracting process' though it is sale from local stock

**Status:** open — needs a human decision

## C697 — two-tier-sale-from-local-stock-by-subsidiary-249

Page: [[16-two-tier-erp-and-central-finance/two-tier-sale-from-local-stock-by-subsidiary-249]]

Overview table says Check Batches on page 28 while the TOC says 29

**Status:** open — needs a human decision

## C698 — two-tier-scenario-managing-intercompany-professional-services-projects

Page: [[16-two-tier-erp-and-central-finance/two-tier-scenario-managing-intercompany-professional-services-projects]]

Process flow case labelling in the Technical Details section (case 1 HQ Private / subsidiary Cloud) differs from case 2 description in text where subsidiary is described as S/4HANA On-Premise versus SAP Cloud ERP (Private).

**Status:** open — needs a human decision

## C699 — two-tier-scenario-project-based-engineer-to-order-customer-guide-241

Page: [[16-two-tier-erp-and-central-finance/two-tier-scenario-project-based-engineer-to-order-customer-guide-241]]

Copyright line says 2025 while the revision table shows a 25-05-2026 update and the cover says June 2026

**Status:** open — needs a human decision

## C700 — two-tier-subsidiary-as-financial-planning-and-upload-of-plan-data-from

Page: [[16-two-tier-erp-and-central-finance/two-tier-subsidiary-as-financial-planning-and-upload-of-plan-data-from]]

Guide says plan file is 'semicolon separated' in one place and 'comma separated values (CSV)' in another, while listing four supported separators.

**Status:** open — needs a human decision

## C701 — two-tier-subsidiary-as-financial-planning-and-upload-of-plan-data-from

Page: [[16-two-tier-erp-and-central-finance/two-tier-subsidiary-as-financial-planning-and-upload-of-plan-data-from]]

System access table lists both Fiori launchpad and 'On-Premise SAP S/4HANA' for a Cloud Public Edition subsidiary scenario.

**Status:** open — needs a human decision

## C702 — lease-out-for-sublease-accounting-group-ledger-ifrs-2sa-ae-858

Page: [[17-leasing-and-real-estate/lease-out-for-sublease-accounting-group-ledger-ifrs-2sa-ae-858]]

Overview Table lists Accounts Payable Accountant - Leasing for periodic posting, reverse contract postings and several accounting reports, while the test procedures and Roles table use Accounts Receivable Accountant - Leasing (no Accounts Payable role is defined in Roles).

**Status:** open — needs a human decision

## C703 — test-script-earmarked-funds-for-real-estate-contracts-6r3-sap-s-4hana

Page: [[17-leasing-and-real-estate/test-script-earmarked-funds-for-real-estate-contracts-6r3-sap-s-4hana]]

Earmarked funds document type is inconsistent: Define Document Types sets Document Type CL under Configure Your Solution but RE under SAP Central Business Configuration (same description, number range and settings), while later steps (CLM contract type activation, workflow start condition) use CL and the Manage Earmarked Funds report filters on document type SC.

**Status:** open — needs a human decision

## C704 — test-script-earmarked-funds-for-real-estate-contracts-6r3-sap-s-4hana

Page: [[17-leasing-and-real-estate/test-script-earmarked-funds-for-real-estate-contracts-6r3-sap-s-4hana]]

Create Contract says Valuation relevance 'No-Leasing Valuation', yet the Overview Table says the valuated contract is created and a separate procedure adds valuation parameters (valuation rule such as US_UGSF_FL).

**Status:** open — needs a human decision

## C705 — test-script-lease-out-accounting-21q-ae-sap-s-4hana-cloud-public-editi

Page: [[17-leasing-and-real-estate/test-script-lease-out-accounting-21q-ae-sap-s-4hana-cloud-public-editi]]

Overview table assigns Periodic Posting and Reverse Contract Postings to 'Accounts Payable Accountant - Leasing', but the test procedures log on as 'Accounts Receivable Accountant - Leasing' (the roles table lists only the AR role).

**Status:** open — needs a human decision

## C706 — test-script-lease-out-for-sublease-accounting-2sb-ae-859

Page: [[17-leasing-and-real-estate/test-script-lease-out-for-sublease-accounting-2sb-ae-859]]

Overview Table lists Accounts Payable Accountant - Leasing as the role for periodic posting, reverse contract postings and several accounting reports, while the test steps and the Roles table use Accounts Receivable Accountant - Leasing.

**Status:** open — needs a human decision

## C707 — test-script-lease-out-for-sublease-accounting-group-ledger-us-gaap-34o

Page: [[17-leasing-and-real-estate/test-script-lease-out-for-sublease-accounting-group-ledger-us-gaap-34o]]

Periodic Posting (F4607) and Reverse Contract Postings (F6275) are assigned to 'Accounts Payable Accountant - Leasing' in the Overview Table, but the test procedures log on as 'Accounts Receivable Accountant - Leasing', and the Roles table lists only the AR role.

**Status:** open — needs a human decision

## C708 — test-script-lease-out-for-sublease-accounting-group-ledger-us-gaap-34o

Page: [[17-leasing-and-real-estate/test-script-lease-out-for-sublease-accounting-group-ledger-us-gaap-34o]]

Overview Table lists Item Overview, Contract Cashflow Report and Periodic Posting Previous Period Comparison under Accounts Payable Accountant - Leasing, while the procedures use Accounts Receivable Accountant - Leasing.

**Status:** open — needs a human decision

## C709 — test-script-sales-based-rent-3f4-ae-sap-s-4hana-cloud-public-edition-9

Page: [[17-leasing-and-real-estate/test-script-sales-based-rent-3f4-ae-sap-s-4hana-cloud-public-edition-9]]

Overview table assigns periodic posting and reverse posting steps to 'Accounts Payable Accountant - Leasing', but the test procedures log on as 'Accounts Receivable Accountant - Leasing'; the roles table lists only the AR role. Likewise 'Contract Valuation Specialist - Leasing' appears in the overview but not in the roles table.

**Status:** open — needs a human decision
