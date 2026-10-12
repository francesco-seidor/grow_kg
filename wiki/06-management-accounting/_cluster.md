---
title: Management Accounting
description: "Cost centers, activity types, cost rates, allocations, profit centers, product costing, margin analysis, budgets, predictive accounting and event-based revenue recognition."
cluster: 06-management-accounting
type: cluster
tags: [kb/management-accounting, kb/hub]
keywords: [controlling, cost center, activity type, cost rate, allocation, profit center, costing run, margin analysis, predictive accounting, revenue recognition]
node_count: 94
created: 2026-10-12
updated: 2026-10-12
---

# Management Accounting

Covers CO master data, costing, profitability and event-based revenue recognition. Excludes G/L and asset accounting (see 03), group planning and consolidation (see 07), FI-CA contract-based revenue recognition (see 09) and carbon quantities in costing (see 13).

Every node below is the verbatim text of one source document (or one part of a long one), grouped by topic.

## Nodes

### Activity Types and Activity Type Hierarchies

How to create activity types and hierarchies, review the change log and run where-used analysis.

| Node | Description |
| --- | --- |
| [[06-management-accounting/leistungsart-und-leistungsartenhierarchie-anlegen-sds-bnn-640\|Leistungsart und Leistungsartenhierarchie anlegen – SDS (BNN) (BNN_S4CLD2608_Master_Data_DE_XX)]] | German SAP S/4HANA Cloud 2608 master data script (BNN): activity types and activity type hierarchies, change log and where-used analyses. Gemeinkostencontroller. |
| [[06-management-accounting/master-data-script-create-activity-type-and-activity-type-hierarchy-bn\|Master Data Script - Create Activity Type and Activity Type Hierarchy (BNN) (BNN_S4CLD2608_Master_Data_EN_XX)]] | English SAP master data script BNN for creating activity types and activity type hierarchies in Controlling, with change log and where-used analytics, release 2608. |
| [[06-management-accounting/script-de-datos-maestros-crear-clase-de-actividad-y-jerarquia-de-clase\|Script de datos maestros: Crear clase de actividad y jerarquía de clases de actividad - MDS (BNN) (BNN_S4CLD2608_Master_Data_ES_XX)]] | Spanish (machine-translated) SAP S/4HANA Cloud Public Edition master data script BNN for creating activity types and activity type hierarchies, with change log and usage analysis. |
| [[06-management-accounting/mds-bnn-643\|活動タイプおよび活動タイプ階層の登録 - MDS (BNN) (BNN_S4CLD2608_Master_Data_JA_XX)]] | Japanese SAP master data script BNN for creating activity types and activity type hierarchies, with change log and where-used test steps. |
| [[06-management-accounting/criar-tipo-de-atividade-e-hierarquia-de-tipo-de-atividade-mds-bnn-644\|Criar tipo de atividade e hierarquia de tipo de atividade – MDS (BNN) (BNN_S4CLD2608_Master_Data_PT_XX)]] | Portuguese master data script (BNN) for SAP S/4HANA Cloud Public Edition: create activity types and activity type hierarchies, change log and where-used list. |
| [[06-management-accounting/mds-bnn-645\|创建活动类型和活动类型层次结构 - MDS (BNN) (BNN_S4CLD2608_Master_Data_ZH_XX)]] | SAP S/4HANA Cloud 2608 master data script (ZH, machine-translated) for creating activity types and hierarchies, change log and where-used list in Controlling. |

### Budgets and Commitment Management

How budgets are uploaded and how commitments are reported against cost center and project budgets.

| Node | Description |
| --- | --- |
| [[06-management-accounting/budgetupload-xx-3\|Budgetupload XX (budgetupload_XX)]] | Budget upload CSV template for S/4HANA Cloud 2608 with sample rows: process ENTR, subcategory S_SCAT1, plan category BUDGET03, account 61002000, by cost center |
| [[06-management-accounting/test-script-predictive-commitments-management-2i3-ae-sap-s-4hana-cloud\|Test Script: Predictive Commitments Management (2I3_AE) - SAP S/4HANA Cloud Public Edition (2I3_S4CLD2608_BPD_EN_AE)]] | SAP test script for scope item 2I3 Predictive Commitments Management (AE): commitment reporting, cost center and project budgeting, with prerequisites and step tables. |

### Best Practice CO and FI Master Data Values

Which cost centers, activity types, cost elements and groups (CO workbook) and which profit center hierarchy YBPH, functional areas and segments (FI workbook) are delivered.

| Node | Description |
| --- | --- |
| [[06-management-accounting/2608-master-data-co-en-xx-118\|2608 Master Data CO EN XX (2608_Master_Data_CO_EN_XX)]] | SAP S/4HANA Cloud Public Edition 2608 Best Practices controlling master data workbook: cost centers, activity types, secondary cost elements, groups, statistical key figures. |
| [[06-management-accounting/2608-master-data-fi-en-xx-119\|2608 Master Data FI EN XX (2608_Master_Data_FI_EN_XX)]] | SAP Best Practices 2608 FI master data workbook: profit center hierarchy (YBPH), 21 functional areas (YB10-YB99) and 3 segments; YCOA sheet empty. |

### Cost Centers and Cost Center Groups

How to create cost centers and cost center groups (global hierarchy or set-based) and run where-used analysis.

| Node | Description |
| --- | --- |
| [[06-management-accounting/stammdatenskript-kostenstelle-und-kostenstellengruppe-anlegen-bnm-634\|Stammdatenskript: Kostenstelle und Kostenstellengruppe anlegen (BNM) (BNM_S4CLD2608_Master_Data_DE_XX)]] | German SAP S/4HANA Cloud Public Edition master data script (BNM) for creating cost centers and cost center groups, with test steps and where-used analysis; dated 02-07-26. |
| [[06-management-accounting/create-cost-center-and-cost-center-group-mds-bnm-635\|Create Cost Center and Cost Center Group - MDS (BNM) (BNM_S4CLD2608_Master_Data_EN_XX)]] | SAP S/4HANA Cloud 2608 master data script for creating cost centers and cost center groups (global hierarchy or set-based), plus where-used analytics. |
| [[06-management-accounting/script-de-datos-maestros-crear-centro-de-coste-y-grupo-de-centros-de-c\|Script de datos maestros - Crear centro de coste y grupo de centros de coste (BNM) (BNM_S4CLD2608_Master_Data_ES_XX)]] | Spanish (machine-translated) SAP S/4HANA Cloud Public Edition master data script for creating cost centers and cost center groups, with usage analysis; dated 02-07-26. |
| [[06-management-accounting/mds-bnm-637\|原価センタおよび原価センタグループの登録 - MDS (BNM) (BNM_S4CLD2608_Master_Data_JA_XX)]] | Japanese master data script (BNM) for SAP S/4HANA Cloud Public Edition 2608: creating cost centers and cost center groups, and where-used analysis. |
| [[06-management-accounting/script-de-dados-mestre-criar-centro-de-custo-e-grupo-de-centros-de-cus\|Script de dados mestre - Criar centro de custo e grupo de centros de custo (MDS BNM) (BNM_S4CLD2608_Master_Data_PT_XX)]] | Portuguese SAP S/4HANA Cloud Public Edition master data script (BNM): create cost centers and cost center groups, plus where-used analysis, dated 02-07-26. |
| [[06-management-accounting/mds-bnm-639\|创建成本中心和成本中心组 - MDS (BNM) (BNM_S4CLD2608_Master_Data_ZH_XX)]] | Chinese (machine-translated) SAP master data script BNM for creating cost centers and cost center groups, with test steps and where-used analysis. |

### Cost Element Groups

How to create cost element groups in Manage Cost Element Groups (F5373).

| Node | Description |
| --- | --- |
| [[06-management-accounting/kostenartengruppe-anlegen-sds-bnp-646\|Kostenartengruppe anlegen - SDS (BNP) (BNP_S4CLD2608_Master_Data_DE_XX)]] | German master data script for creating a cost element group in SAP S/4HANA Cloud Public Edition via Kostenartengruppen verwalten (F5373). |
| [[06-management-accounting/create-cost-element-group-mds-bnp-647\|Create Cost Element Group - MDS (BNP) (BNP_S4CLD2608_Master_Data_EN_XX)]] | SAP S/4HANA Cloud Public Edition master data script (EN) for creating cost element groups via Manage Cost Element Groups (F5373) as Cost Accountant - Overhead. |
| [[06-management-accounting/script-de-datos-maestros-crear-grupo-de-clases-de-coste-mds-bnp-648\|Script de datos maestros: Crear grupo de clases de coste - MDS (BNP) (BNP_S4CLD2608_Master_Data_ES_XX)]] | Spanish (machine-translated) master data script BNP for creating cost element groups in SAP S/4HANA Cloud Public via app Gestionar grupos de clases de coste (F5373). |
| [[06-management-accounting/mds-bnp-649\|原価要素グループの登録 - MDS (BNP) (BNP_S4CLD2608_Master_Data_JA_XX)]] | SAP S/4HANA Cloud Public Edition 2608 マスタデータスクリプト (BNP): 管理会計担当者が原価要素グループ管理 (F5373) で原価要素グループを登録する手順 (日本語)。 |
| [[06-management-accounting/criar-grupo-de-classes-de-custo-mds-bnp-650\|Criar grupo de classes de custo – MDS (BNP) (BNP_S4CLD2608_Master_Data_PT_XX)]] | Portuguese master data script BNP: create a cost element group with Administrar grupos de classes de custo (F5373) as Controlador - custos indiretos, S/4HANA Cl |
| [[06-management-accounting/mds-bnp-651\|创建成本要素组 - MDS (BNP) (BNP_S4CLD2608_Master_Data_ZH_XX)]] | Chinese (machine-translated) master data script BNP: create a cost element group with Manage Cost Element Groups app F5373 as overhead cost accountant. |

### CO Cost Rates (Service, Plan and Actual)

How to maintain service, plan and actual cost rates for activity types in the Manage Cost Rates apps.

| Node | Description |
| --- | --- |
| [[06-management-accounting/stammdatenskript-leistungstarife-anlegen-sds-3kw-352\|Stammdatenskript: Leistungstarife anlegen – SDS (3KW) (3KW_S4CLD2608_Master_Data_DE_XX)]] | German master data/test script (3KW) for SAP S/4HANA Cloud Public Edition: maintaining activity-type rates (Leistungstarife) via Services, Plan and Actual apps, plus display report. |
| [[06-management-accounting/master-data-script-create-co-cost-rates-mds-3kw-353\|Master Data Script: Create CO Cost Rates - MDS (3KW) (3KW_S4CLD2608_Master_Data_EN_XX)]] | SAP S/4HANA Cloud Public Edition 2608 master data script for creating CO cost rates (services, plan, actual) via Fiori apps F3161, F3162, F3422, plus display report. |
| [[06-management-accounting/crear-tasas-de-coste-co-mds-3kw-354\|Crear tasas de coste CO - MDS (3KW) (3KW_S4CLD2608_Master_Data_ES_XX)]] | Spanish (machine-translated) SAP S/4HANA Cloud Public Edition master data script 3KW: creating CO cost rates (services, plan, actual) with test steps and display report. |
| [[06-management-accounting/co-mds-3kw-355\|CO 原価率の登録 - MDS (3KW) (3KW_S4CLD2608_Master_Data_JA_XX)]] | Japanese master data script (3KW) for maintaining CO cost rates (activity prices) via Manage Cost Rates apps for service, plan and actual, plus ICO account setup and cost rate query. |
| [[06-management-accounting/script-de-dados-mestre-criar-taxas-de-custo-co-mds-3kw-356\|Script de dados mestre - Criar taxas de custo CO – MDS (3KW) (3KW_S4CLD2608_Master_Data_PT_XX)]] | Portuguese SAP S/4HANA Cloud Public Edition master data test script (3KW) for creating service, planned and actual cost rates in Controlling, plus the display report. |
| [[06-management-accounting/co-mds-3kw-357\|主数据脚本 - 创建 CO 成本率 - MDS (3KW) (3KW_S4CLD2608_Master_Data_ZH_XX)]] | Chinese (machine-translated) SAP S/4HANA Cloud 2608 master data script 3KW: maintain CO cost rates (service, plan, actual) and ICO account prerequisites. |

### Event-Based Revenue Recognition for Sell from Stock

How event-based revenue recognition posts revenue and COGS for sell-from-stock under IFRS and US GAAP, including URR test materials.

| Node | Description |
| --- | --- |
| [[06-management-accounting/stammdatenskript-materialstamm-fur-universelle-erlosrealisierung-anleg\|Stammdatenskript: Materialstamm für universelle Erlösrealisierung anlegen (7R8) (7R8_S4CLD2608_Master_Data_DE_XX)]] | German SAP S/4HANA Cloud Public Edition 2608 master data script (7R8): create UER test materials and sales prices for stock sales, fixed-price project and service contract. |
| [[06-management-accounting/master-data-script-create-material-master-for-universal-revenue-recogn\|Master Data Script: Create Material Master for Universal Revenue Recognition (7R8) (7R8_S4CLD2608_Master_Data_EN_XX)]] | SAP S/4HANA Cloud Public Edition 2608 test script for creating URR test materials and their sales prices for Sell from Stock, fixed price project and service contract scenarios. |
| [[06-management-accounting/script-de-datos-maestros-crear-maestro-de-materiales-para-el-reconocim\|Script de datos maestros - Crear maestro de materiales para el reconocimiento universal de ingresos (7R8) (7R8_S4CLD2608_Master_Data_ES_XX)]] | SAP S/4HANA Cloud Public Edition 2608 master data script (ES, machine-translated): create URR test materials and condition prices for SFS, fixed-price project and service contract scenarios. |
| [[06-management-accounting/master-data-script-item-master-for-universal-revenue-recognition-7r8-j\|目的 (Master Data Script: Item Master for Universal Revenue Recognition, 7R8, Japanese) (7R8_S4CLD2608_Master_Data_JA_XX)]] | Japanese master data script (7R8) for creating URR test product master records and condition-record prices for stock-sales, fixed-price project and service contract scenarios. |
| [[06-management-accounting/script-de-dados-mestre-criar-mestre-de-materiais-para-realizacao-de-re\|Script de dados mestre - Criar mestre de materiais para realização de receita universal (7R8) (7R8_S4CLD2608_Master_Data_PT_XX)]] | Portuguese SAP S/4HANA Cloud Public Edition 2608 script for creating URR test material master data and condition prices for SFS, fixed-price project and service contract scenarios. |
| [[06-management-accounting/7r8-537\|创建统一收入确认的物料主数据 (7R8) (7R8_S4CLD2608_Master_Data_ZH_XX)]] | Chinese master data script (7R8) for creating URR test materials and their sales prices for unified revenue recognition scenarios in SAP S/4HANA Cloud Public Edition. |
| [[06-management-accounting/event-based-revenue-recognition-sell-from-stock-1k2-ae-test-script-731\|Event-Based Revenue Recognition – Sell from Stock (1K2_AE) Test Script (1K2_S4CLD2608_BPD_EN_AE)]] | SAP S/4HANA Cloud Public Edition test script for event-based revenue recognition, sell from stock (1K2_AE): prerequisites, config steps, Fiori app test procedures, reversal. |
| [[06-management-accounting/test-script-event-based-revenue-recognition-sell-from-stock-us-gaap-33\|Test Script: Event-Based Revenue Recognition – Sell from Stock – US GAAP (33J_AE) (33J_S4CLD2608_BPD_EN_AE)]] | SAP S/4HANA Cloud Public Edition 2608 test script for event-based revenue recognition, sell from stock, US GAAP (33J_AE): prerequisites, config and test steps. |
| [[06-management-accounting/test-script-event-based-revenue-recognition-sell-from-stock-ifrs-33m-a\|Test Script: Event-Based Revenue Recognition – Sell from Stock – IFRS (33M_AE) (33M_S4CLD2608_BPD_EN_AE)]] | SAP S/4HANA Cloud Public Edition test script 33M_AE: event-based revenue recognition, sell from stock, IFRS; prerequisites, config, run, issues, reversal. |

### Event-Based Revenue Recognition for Subscriptions

How event-based revenue recognition handles subscription provider contracts under standard, IFRS and US GAAP ledgers.

| Node | Description |
| --- | --- |
| [[06-management-accounting/event-based-revenue-recognition-subscription-billing-5dq-ae-test-scrip\|Event-Based Revenue Recognition – Subscription Billing (5DQ_AE) Test Script (5DQ_S4CLD2608_BPD_EN_AE)]] | SAP S/4HANA Cloud Public Edition test script for scope item 5DQ: event-based revenue recognition of subscription provider contracts, with prerequisites, steps and reversal. |
| [[06-management-accounting/test-script-event-based-revenue-recognition-subscription-billing-ifrs\|Test Script: Event-Based Revenue Recognition – Subscription Billing – IFRS (5DR_AE) (5DR_S4CLD2608_BPD_EN_AE)]] | SAP S/4HANA Cloud Public Edition 2608 test script for scope item 5DR: event-based revenue recognition of subscription provider contracts under IFRS, with prerequisites and steps. |
| [[06-management-accounting/event-based-revenue-recognition-subscription-billing-us-gaap-5ds-ae-te\|Event-Based Revenue Recognition – Subscription Billing – US GAAP (5DS_AE) Test Script (5DS_S4CLD2608_BPD_EN_AE)]] | SAP S/4HANA Cloud Public Edition test script for scope item 5DS: event-based revenue recognition of subscription provider contracts under US GAAP, with prerequisites and steps. |

### Financial Planning and Analysis Statement Version

How the predefined financial statement version FPA1 and its semantic tags are maintained for financial planning and analysis.

| Node | Description |
| --- | --- |
| [[06-management-accounting/test-script-financial-planning-and-analysis-2fm-ae-825\|Test Script: Financial Planning and Analysis (2FM_AE) (2FM_S4CLD2608_BPD_EN_AE)]] | SAP S/4HANA Cloud Public Edition 2608 test script for scope item 2FM (AE): maintaining the predefined Financial Statement Version FPA1 and its semantic tags. |

### Group Valuation

How group valuation is configured and how costing runs, cost estimates and actual costing work in the group valuation ledger.

| Node | Description |
| --- | --- |
| [[06-management-accounting/test-script-group-valuation-5w2-ae-1123\|Test Script: Group Valuation (5W2_AE) (5W2_S4CLD2608_BPD_EN_AE)]] | SAP S/4HANA Cloud Public Edition test script for scope item 5W2 Group Valuation: prerequisites, configuration, costing run, cost estimates, actual costing for ledger 4G. |

### Margin Analysis (CO-PA)

How margin analysis allocations, top-down distribution, realignment and profitability reports work in CO-PA.

| Node | Description |
| --- | --- |
| [[06-management-accounting/margin-analysis-j55-ae-test-script-sap-s-4hana-cloud-public-edition-13\|Margin Analysis (J55_AE) Test Script - SAP S/4HANA Cloud Public Edition (J55_S4CLD2608_BPD_EN_AE)]] | SAP Best Practices test script for scope item J55 Margin Analysis (AE): prerequisites, CO-PA allocations, top-down distribution, realignment and profitability reports. |

### Predictive Accounting for Sales Orders, Service Contracts and Travel

How predictive accounting shows presumed margins from incoming sales orders, service contracts and Concur travel commitments.

| Node | Description |
| --- | --- |
| [[06-management-accounting/predictive-accounting-for-travel-and-expense-management-4q0-ae-1042\|Predictive Accounting for Travel and Expense Management (4Q0_AE) (4Q0_S4CLD2608_BPD_EN_AE)]] | Test script for scope item 4Q0: commitments by cost center and project budget reporting from SAP Concur travel and expense, in S/4HANA Cloud Public Edition 2608. |
| [[06-management-accounting/predictive-accounting-for-service-contract-management-4v7-ae-test-scri\|Predictive Accounting for Service Contract Management (4V7_AE) - Test Script (4V7_S4CLD2608_BPD_EN_AE)]] | SAP S/4HANA Cloud Public Edition test script for scope item 4V7_AE: predictive accounting for service contracts, margin analysis line items and revenue recognition run. |
| [[06-management-accounting/predictive-accounting-for-sales-orders-2fd-ae-test-script-824\|Predictive Accounting for Sales Orders (2FD_AE) - Test Script (2FD_S4CLD2608_BPD_EN_AE)]] | SAP S/4HANA Cloud Public Edition 2608 test script for scope item 2FD: sales accounting overview, incoming sales orders and presumed/actual gross margin reports. |

### Product Costing Runs and Standard Cost Updates

How to create and run costing runs (F1865) and perform off-cycle standard cost updates after BOM or price changes.

| Node | Description |
| --- | --- |
| [[06-management-accounting/product-cost-related-master-data-changes-consumer-products-61w-ae-test\|Product Cost Related Master Data Changes – Consumer Products (61W_AE) Test Script (61W_S4CLD2608_BPD_EN_AE)]] | SAP S/4HANA Cloud Public Edition 2608 test script (scope item 61W, AE) for off-cycle standard cost updates: BOM change, price change, costing run, analytics. |
| [[06-management-accounting/test-script-product-cost-breakdown-in-plan-actual-value-flow-7nh-ae-sa\|Test Script: Product Cost Breakdown in Plan/Actual Value Flow (7NH_AE) - SAP S/4HANA Cloud Public Edition (7NH_S4CLD2608_BPD_EN_AE)]] | SAP S/4HANA Cloud Public Edition 2608 test script for scope item 7NH: plan/actual product cost breakdown, prerequisites, configuration and Fiori test steps. |
| [[06-management-accounting/test-script-standard-cost-calculation-beg-ae-sap-s-4hana-cloud-public\|Test Script: Standard Cost Calculation (BEG_AE) - SAP S/4HANA Cloud Public Edition (BEG_S4CLD2608_BPD_EN_AE)]] | SAP S/4HANA Cloud Public Edition 2608 test script for standard cost calculation (BEG_AE): prerequisites, setup, costing run steps, analytics. |
| [[06-management-accounting/kalkulationslauf-anlegen-sds-bnu-676\|Kalkulationslauf anlegen – SDS (BNU) (BNU_S4CLD2608_Master_Data_DE_XX)]] | German master data test script (BNU) for SAP S/4HANA Cloud Public Edition 2608: creating and executing a product costing run (F1865) as a prerequisite for logistics scenarios. |
| [[06-management-accounting/master-data-script-create-costing-run-mds-bnu-677\|Master Data Script - Create Costing Run – MDS (BNU) (BNU_S4CLD2608_Master_Data_EN_XX)]] | English master data script (BNU) for SAP S/4HANA Cloud Public Edition: creating and executing a product costing run with app F1865 as logistics test prerequisite. |
| [[06-management-accounting/crear-ejecucion-del-calculo-del-coste-mds-bnu-678\|Crear ejecución del cálculo del coste - MDS (BNU) (BNU_S4CLD2608_Master_Data_ES_XX)]] | Spanish (machine-translated) SAP S/4HANA Cloud 2608 master data script BNU: creating and executing a product cost estimate run with variant PYC1. |
| [[06-management-accounting/mds-bnu-679\|原価積上実行の登録 - MDS (BNU) (BNU_S4CLD2608_Master_Data_JA_XX)]] | SAP S/4HANA Cloud 2608 master data script (JA) for registering and executing cost estimate runs (product costing) with app F1865 as Inventory Accountant. |
| [[06-management-accounting/criar-execucao-de-calculo-de-custos-mds-bnu-680\|Criar execução de cálculo de custos – MDS (BNU) (BNU_S4CLD2608_Master_Data_PT_XX)]] | Portuguese master data script (BNU) for creating and executing a product cost estimate run in SAP S/4HANA Cloud Public Edition 2608, with prerequisites and test steps. |
| [[06-management-accounting/mds-bnu-681\|创建成本核算运行 - MDS (BNU) (BNU_S4CLD2608_Master_Data_ZH_XX)]] | Chinese (machine-translated) SAP S/4HANA Cloud 2608 master data script BNU: create and execute a product costing run in app F1865 as Inventory Accountant. |

### Profit Centers and Profit Center Reorganization

How profit center master data is created in F3516 (validity, company codes; scripts in six languages) and how an organizational change reassigns profit centers (4PG).

| Node | Description |
| --- | --- |
| [[06-management-accounting/2608-master-data-fi-en-xx-119\|2608 Master Data FI EN XX (2608_Master_Data_FI_EN_XX)]] | SAP Best Practices 2608 FI master data workbook: profit center hierarchy (YBPH), 21 functional areas (YB10-YB99) and 3 segments; YCOA sheet empty. |
| [[06-management-accounting/test-script-organizational-flexibility-in-financial-accounting-4pg-sap\|Test Script: Organizational Flexibility in Financial Accounting (4PG) - SAP S/4HANA Cloud Public Edition (4PG_S4CLD2608_BPD_EN_XX)]] | SAP S/4HANA Cloud Public Edition test script for scope item 4PG: create, simulate, activate and process a profit center organizational change. |
| [[06-management-accounting/profitcenter-anlegen-sds-bnh-604\|Profitcenter anlegen – SDS (BNH) (BNH_S4CLD2608_Master_Data_DE_XX)]] | German SAP S/4HANA Cloud master data script (BNH) for creating profit center master data with app F3516 as Divisional Accountant, incl. validity periods. |
| [[06-management-accounting/create-profit-center-mds-bnh-605\|Create Profit Center - MDS (BNH) (BNH_S4CLD2608_Master_Data_EN_XX)]] | Master data script (BNH) for creating profit center master data with Manage Profit Centers - Old Version (F3516) in SAP S/4HANA Cloud Public Edition 2608. |
| [[06-management-accounting/script-de-datos-maestros-crear-centro-de-beneficio-mds-bnh-606\|Script de datos maestros - Crear centro de beneficio - MDS (BNH) (BNH_S4CLD2608_Master_Data_ES_XX)]] | Spanish master data script (MDS BNH) with prerequisites and test steps to create and maintain profit center master data in SAP S/4HANA Cloud Public Edition. |
| [[06-management-accounting/mds-bnh-607\|利益センタの登録 - MDS (BNH) (BNH_S4CLD2608_Master_Data_JA_XX)]] | Japanese master data script BNH: creating profit center master data via app F3516 (legacy) in S/4HANA Cloud Public Edition 2608, with mandatory fields and validity periods. |
| [[06-management-accounting/script-de-dados-mestre-criar-centro-de-lucro-mds-bnh-608\|Script de dados mestre - Criar centro de lucro (MDS, BNH) (BNH_S4CLD2608_Master_Data_PT_XX)]] | Portuguese master data script (scope BNH) for creating a profit center in SAP S/4HANA Cloud Public Edition: prerequisites, mandatory fields and test steps. |
| [[06-management-accounting/mds-bnh-609\|创建利润中心 - MDS (BNH) (BNH_S4CLD2608_Master_Data_ZH_XX)]] | Chinese (machine-translated) master data script (MDS BNH) for creating a profit center via Manage Profit Centers - Old Version (F3516) in SAP S/4HANA Cloud 2608. |

### Universal Allocation Cycles

How to create plan and actual overhead assessment and profit center distribution cycles in Manage Allocations.

| Node | Description |
| --- | --- |
| [[06-management-accounting/stammdaten-fur-universelle-verrechnung-anlegen-sds-2us-286\|Stammdaten für universelle Verrechnung anlegen – SDS (2US) (2US_S4CLD2608_Master_Data_DE_XX)]] | German SAP S/4HANA Cloud Public Edition 2608 master data script: test steps for plan/actual allocation and profit center distribution cycles in app Verrechnungen verwalten (F3338A). |
| [[06-management-accounting/create-universal-allocation-master-data-mds-2us-287\|Create Universal Allocation Master Data - MDS (2US) (2US_S4CLD2608_Master_Data_EN_XX)]] | SAP S/4HANA Cloud Public Edition 2608 master data script (2US) for creating plan/actual overhead assessment and profit center distribution cycles in Manage Allocations (F3338A). |
| [[06-management-accounting/script-de-datos-maestros-crear-datos-maestros-de-asignacion-universal\|Script de datos maestros - Crear datos maestros de asignación universal - MDS (2US) (2US_S4CLD2608_Master_Data_ES_XX)]] | Spanish (machine-translated) SAP S/4HANA Cloud Public Edition 2608 master data script for universal allocation: plan/actual overhead and profit center cycles via Fiori F3338A. |
| [[06-management-accounting/mds-2us-289\|マスタデータスクリプト: ユニバーサルアロケーションマスタデータの登録 - MDS (2US) (2US_S4CLD2608_Master_Data_JA_XX)]] | Japanese master data script (2US) for SAP S/4HANA Cloud Public Edition 2608: creating universal allocation cycles (planned/actual overhead and profit center) in app F3338A. |
| [[06-management-accounting/script-de-dados-mestre-criar-dados-mestre-de-alocacao-universal-mds-2u\|Script de dados mestre: Criar dados mestre de alocação universal - MDS (2US) (2US_S4CLD2608_Master_Data_PT_XX)]] | Portuguese SAP S/4HANA Cloud Public Edition 2608 master data script (2US) for creating planned/actual universal allocation cycles for cost centers and profit centers. |
| [[06-management-accounting/mds-2us-291\|主数据脚本 - 创建通用分配主数据 - MDS (2US) (2US_S4CLD2608_Master_Data_ZH_XX)]] | Chinese master data script (MDS 2US) for testing universal allocation cycles (plan/actual overhead and profit center allocations) in SAP S/4HANA Cloud Public Edition. |
| [[06-management-accounting/test-script-universal-allocation-2ql-ae-sap-s-4hana-cloud-public-editi\|Test Script: Universal Allocation (2QL_AE) - SAP S/4HANA Cloud Public Edition (2QL_S4CLD2608_BPD_EN_AE)]] | S/4HANA Cloud Public Edition 2608 test script for Universal Allocation (2QL_AE): plan data upload, allocation cycles and runs, profit center, intercompany. |

### Overhead Cost Accounting

How cost center postings, direct activity allocation, overhead allocation, statistical key figures, budgets and cost center reports run in overhead cost accounting.

| Node | Description |
| --- | --- |
| [[06-management-accounting/test-script-overhead-cost-accounting-j54-ae-sap-s-4hana-cloud-public-e\|Test Script: Overhead Cost Accounting (J54_AE) - SAP S/4HANA Cloud Public Edition (J54_S4CLD2608_BPD_EN_AE)]] | Test script for SAP S/4HANA Cloud scope item J54 Overhead Cost Accounting (AE, 2608): prerequisites, cost center postings, allocations, reports, budgeting. |

### Financial Plan Data Upload and Integrated Financial Planning

How financial plan data is uploaded, copied and deleted from CSV files, and how OPEX, CAPEX, product cost and profitability plans are built in SAP Analytics Cloud.

| Node | Description |
| --- | --- |
| [[06-management-accounting/test-script-sap-s-4hana-cloud-public-edition-integrated-financial-plan\|Test Script SAP S/4HANA Cloud Public Edition - Integrated Financial Planning (4RC) (4RC_S4CLD2608_BPD_EN_XX)]] | Test script for scope item 4RC Integrated Financial Planning in SAP Analytics Cloud: OPEX, product cost, profitability, CAPEX, financial statement, GHG, add-ons, S/4HANA integration. |
| [[06-management-accounting/test-script-financial-plan-data-upload-from-file-1hb-ae-sap-s-4hana-cl\|Test Script: Financial Plan Data Upload from File (1HB_AE) - SAP S/4HANA Cloud Public Edition (1HB_S4CLD2608_BPD_EN_AE)]] | SAP Best Practices test script (scope item 1HB_AE, release 2608): uploading, updating, copying, deleting and compressing financial plan data via CSV in Fiori. |

### Project Control for Finance, Capital, R&D and Sales Projects

How finance, capital, R&D and fixed-price sales projects are created, budgeted with availability control, resourced, reviewed, settled and closed in project control.

| Node | Description |
| --- | --- |
| [[06-management-accounting/test-script-project-control-sales-4i9-ae-sap-s-4hana-cloud-public-edit\|Test Script: Project Control – Sales (4I9_AE), SAP S/4HANA Cloud Public Edition (4I9_S4CLD2608_BPD_EN_AE)]] | SAP test script for scope item 4I9_AE: fixed-price projects with revenue, from project creation and sales order billing plan to revenue recognition and closure. |
| [[06-management-accounting/test-script-project-control-resourcing-and-procurement-4rf-ae-1049\|Test Script: Project Control – Resourcing and Procurement (4RF_AE) (4RF_S4CLD2608_BPD_EN_AE)]] | SAP S/4HANA Cloud Public Edition test script for scope item 4RF_AE: project demands for materials, services and resources, with roles, apps and sample data. |
| [[06-management-accounting/period-end-closing-projects-bna-ae-test-script-sap-s-4hana-cloud-publi\|Period-End Closing – Projects (BNA_AE) – Test Script, SAP S/4HANA Cloud Public Edition 2608 (BNA_S4CLD2608_BPD_EN_AE)]] | SAP S/4HANA Cloud 2608 (AE) test script for project period-end closing: overhead, project and AuC settlement, final settlement, reports, config prerequisites. |
| [[06-management-accounting/test-script-project-control-finance-1nt-ae-sap-s-4hana-cloud-public-ed\|Test Script: Project Control – Finance (1NT_AE), SAP S/4HANA Cloud Public Edition (1NT_S4CLD2608_BPD_EN_AE)]] | SAP S/4HANA Cloud Public Edition test script for scope item 1NT (Project Control – Finance, AE): create, budget, monitor, settle, complete and close projects. |
| [[06-management-accounting/test-script-project-review-1yf-ae-sap-s-4hana-cloud-public-edition-787\|Test Script: Project Review (1YF_AE) - SAP S/4HANA Cloud Public Edition (1YF_S4CLD2608_BPD_EN_AE)]] | S/4HANA Cloud test script for scope item 1YF Project Review: roles, apps and test steps for project setup, release workflow and milestone review. |
| [[06-management-accounting/test-script-project-control-research-and-development-projects-35e-ae-9\|Test Script: Project Control – Research and Development Projects (35E_AE) (35E_S4CLD2608_BPD_EN_AE)]] | SAP S/4HANA Cloud Public Edition test script for scope item 35E (AE): create, budget, release, monitor, close R&D projects, with prerequisites and Fiori app steps. |
| [[06-management-accounting/test-script-project-control-capital-projects-35f-ae-sap-s-4hana-cloud\|Test Script: Project Control – Capital Projects (35F_AE), SAP S/4HANA Cloud Public Edition (35F_S4CLD2608_BPD_EN_AE)]] | SAP test script for scope item 35F (AE): prerequisites and test steps to create, budget, release, monitor, settle and close capital investment projects. |

### Event-Based Revenue Recognition for Projects

How event-based revenue recognition posts revenue and margin for project-based services and project-based sales under standard, IFRS and US GAAP ledgers.

| Node | Description |
| --- | --- |
| [[06-management-accounting/event-based-revenue-recognition-project-based-sales-4gq-ae-1024\|Event-Based Revenue Recognition – Project-Based Sales (4GQ_AE) (4GQ_S4CLD2608_BPD_EN_AE)]] | SAP S/4HANA Cloud Public Edition test script (4GQ_AE): prerequisites, configuration and test steps for event-based revenue recognition on project-based sales. |
| [[06-management-accounting/test-script-event-based-revenue-recognition-project-based-sales-ifrs-4\|Test Script: Event-Based Revenue Recognition – Project-Based Sales – IFRS (4GR_AE) (4GR_S4CLD2608_BPD_EN_AE)]] | SAP S/4HANA Cloud Public Edition 2608 test script (scope item 4GR_AE): prerequisites and step-by-step tests for event-based revenue recognition on project-based sales under IFRS. |
| [[06-management-accounting/test-script-event-based-revenue-recognition-project-based-sales-us-gaa\|Test Script: Event-Based Revenue Recognition – Project-Based Sales – US GAAP (4GS_AE), SAP S/4HANA Cloud Public Edition (4GS_S4CLD2608_BPD_EN_AE)]] | SAP S/4HANA Cloud Public Edition 2608 test script (4GS_AE): prerequisites, config and test steps for event-based revenue recognition, project sales, US GAAP. |
| [[06-management-accounting/test-script-event-based-revenue-recognition-project-based-services-1il\|Test Script: Event-Based Revenue Recognition – Project-Based Services (1IL_AE) (1IL_S4CLD2608_BPD_EN_AE)]] | SAP S/4HANA Cloud Public Edition test script (1IL_AE) for event-based revenue recognition in project-based services: prerequisites, setup, test steps. |
| [[06-management-accounting/test-script-event-based-revenue-recognition-project-based-services-ifr\|Test Script: Event-Based Revenue Recognition – Project-Based Services – IFRS (1P0_AE) (1P0_S4CLD2608_BPD_EN_AE)]] | Test script for SAP S/4HANA Cloud scope item 1P0_AE: FSV YPS2, recognition key and hierarchy setup, then event-based project revenue recognition tests. |
| [[06-management-accounting/event-based-revenue-recognition-project-based-services-us-gaap-33o-ae\|Event-Based Revenue Recognition – Project-Based Services – US GAAP (33O_AE) (33O_S4CLD2608_BPD_EN_AE)]] | SAP S/4HANA Cloud Public Edition test script for scope item 33O_AE: event-based revenue recognition for project-based services (US GAAP), setup and test steps. |
| [[06-management-accounting/test-script-project-control-sales-4i9-ae-sap-s-4hana-cloud-public-edit\|Test Script: Project Control – Sales (4I9_AE), SAP S/4HANA Cloud Public Edition (4I9_S4CLD2608_BPD_EN_AE)]] | SAP test script for scope item 4I9_AE: fixed-price projects with revenue, from project creation and sales order billing plan to revenue recognition and closure. |

### Event-Based Revenue Recognition for Service Documents

How event-based revenue recognition posts revenue for service contracts and service orders under standard, IFRS and US GAAP ledgers, including period-end runs.

| Node | Description |
| --- | --- |
| [[06-management-accounting/test-script-event-based-revenue-recognition-service-documents-3m3-ae-9\|Test Script: Event-Based Revenue Recognition – Service Documents (3M3_AE) (3M3_S4CLD2608_BPD_EN_AE)]] | SAP S/4HANA Cloud Public Edition test script (scope item 3M3, AE): configure and test event-based revenue recognition for service contracts and orders. |
| [[06-management-accounting/test-script-event-based-revenue-recognition-service-documents-ifrs-3m4\|Test Script: Event-Based Revenue Recognition – Service Documents – IFRS (3M4_AE) (3M4_S4CLD2608_BPD_EN_AE)]] | SAP S/4HANA Cloud Public Edition test script for scope item 3M4_AE: event-based revenue recognition on service contracts/orders (IFRS), prerequisites, steps, settlement. |
| [[06-management-accounting/event-based-revenue-recognition-service-documents-us-gaap-3m5-ae-960\|Event-Based Revenue Recognition – Service Documents – US GAAP (3M5_AE) (3M5_S4CLD2608_BPD_EN_AE)]] | SAP S/4HANA Cloud Public Edition 2608 test script for scope item 3M5_AE: event-based revenue recognition on service contracts and orders (US GAAP), with prerequisites and test steps. |

### Contract-Based Revenue Recognition (Universal Revenue Recognition)

How universal and contract-based revenue recognition (IFRS 15) builds revenue contracts from revenue accounting items under IFRS or US GAAP ledgers.

| Node | Description |
| --- | --- |
| [[06-management-accounting/test-script-contract-based-revenue-recognition-ifrs-3kk-ae-949\|Test Script: Contract-Based Revenue Recognition – IFRS (3KK_AE) (3KK_S4CLD2608_BPD_EN_AE)]] | S/4HANA Cloud 2608 (AE) test script, scope item 3KK: Universal and Contract-Based Revenue Recognition (IFRS 15), prerequisites and Fiori test steps. |
| [[06-management-accounting/test-script-contract-based-revenue-recognition-us-gaap-3vs-ae-976\|Test Script: Contract-Based Revenue Recognition – US GAAP (3VS_AE) (3VS_S4CLD2608_BPD_EN_AE)]] | SAP S/4HANA Cloud test script 3VS_AE (US GAAP, company 3310): prerequisites, configuration and test steps for Universal and Contract-Based Revenue Recognition. |

### Inventory Valuation and Actual Costing

How material prices are changed, actual costing runs determine actual prices in the material ledger, and year-end FIFO and lowest-value valuation adjust inventory values.

| Node | Description |
| --- | --- |
| [[06-management-accounting/test-script-inventory-valuation-for-year-end-closing-bej-ae-1260\|Test Script: Inventory Valuation for Year-End Closing (BEJ_AE) (BEJ_S4CLD2608_BPD_EN_AE)]] | SAP S/4HANA Cloud Public Edition 2608 test script for scope item BEJ_AE: FIFO, lowest-value determination, balance sheet value and adjustment for year-end inventory valuation. |
| [[06-management-accounting/managing-material-price-changes-and-inventory-values-1zt-ae-test-scrip\|Managing Material Price Changes and Inventory Values (1ZT_AE) - Test Script (1ZT_S4CLD2608_BPD_EN_AE)]] | Test script for SAP S/4HANA Cloud scope item 1ZT_AE: immediate and future material price changes, stock-value adjustments, inventory value analysis. |
| [[06-management-accounting/test-script-actual-costing-33q-ae-sap-s-4hana-cloud-public-edition-903\|Test Script: Actual Costing (33Q_AE) - SAP S/4HANA Cloud Public Edition (33Q_S4CLD2608_BPD_EN_AE)]] | SAP S/4HANA Cloud Public Edition test script for Actual Costing (scope item 33Q_AE): prerequisites, preliminary config and step-by-step test procedures. |

### Event-Based Production Cost Posting

How event-based WIP, variances and overhead post for production orders and product cost collectors, with manual settlement and production cost analytics.

| Node | Description |
| --- | --- |
| [[06-management-accounting/test-script-event-based-production-cost-posting-3f0-ae-sap-s-4hana-clo\|Test Script: Event-Based Production Cost Posting (3F0_AE) - SAP S/4HANA Cloud Public Edition (3F0_S4CLD2608_BPD_EN_AE)]] | SAP S/4HANA Cloud test script for scope item 3F0_AE: set up and test event-based WIP, variance and overhead posting, manual settlement and cost analytics. |

## Related categories
- related-to :: [[03-financial-accounting-and-close/_cluster]]
- related-to :: [[07-group-reporting-and-consolidation/_cluster]]
