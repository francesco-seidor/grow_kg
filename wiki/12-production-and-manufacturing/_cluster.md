---
title: Production and Manufacturing
description: "Production master data (work centers, routings, BOMs, versions, PRTs, recipes) and discrete and process manufacturing: MTO, MTS, subcontracting, rework, kanban, MES."
cluster: 12-production-and-manufacturing
type: cluster
tags: [kb/production-and-manufacturing, kb/hub]
keywords: [production, work center, routing, BOM, production version, PRT, master recipe, process order, MRP, subcontracting, rework, kanban, MES]
node_count: 98
created: 2026-10-12
updated: 2026-10-12
---

# Production and Manufacturing

Covers plant production planning and execution. Excludes product master creation (see 02), EWM staging (see 11), product costing (see 06), project-based ETO (see 14) and maintenance work centers (see 14).

Every node below is the verbatim text of one source document (or one part of a long one), grouped by topic.

## Nodes

### Engineer-to-Order with Variant Configuration

How ETO sales orders create order BOMs and how engineering changes are accepted.

| Node | Description |
| --- | --- |
| [[12-production-and-manufacturing/test-script-engineer-to-order-production-with-variant-configuration-4r\|Test Script: Engineer-to-Order Production with Variant Configuration (4R8_AE) (4R8_S4CLD2608_BPD_EN_AE)]] | SAP S/4HANA Cloud Public Edition 2608 test script for scope item 4R8 (AE): ETO sales order, Order BOM creation and acceptance of engineering changes. |

### Kanban Replenishment (In-House Production, External Procurement, Stock Transfer)

How kanban control cycles trigger replenishment by in-house production (4B3), external procurement incl. event-driven kanban (1E3), or classic and one-card stock transfer (4B4).

| Node | Description |
| --- | --- |
| [[12-production-and-manufacturing/test-script-material-replenishment-with-kanban-in-house-production-4b3\|Test Script: Material Replenishment with Kanban – In-House Production (4B3_AE) (4B3_S4CLD2608_BPD_EN_AE)]] | SAP S/4HANA Cloud Public Edition 2608 (AE) test script for scope item 4B3: Kanban replenishment with in-house production, covering prerequisites, MRP, Kanban status and backflush. |
| [[12-production-and-manufacturing/test-script-material-replenishment-with-kanban-stock-transfer-4b4-ae-s\|Test Script: Material Replenishment with Kanban – Stock Transfer (4B4_AE), SAP S/4HANA Cloud Public Edition (4B4_S4CLD2608_BPD_EN_AE)]] | S/4HANA Cloud 2608 (AE) test script for scope item 4B4: classic and one-card Kanban stock-transfer replenishment, roles, master data, control cycles. |
| [[12-production-and-manufacturing/material-replenishment-with-kanban-external-procurement-1e3-ae-test-sc\|Material Replenishment with Kanban – External Procurement (1E3_AE) – Test Script, SAP S/4HANA Cloud Public Edition (1E3_S4CLD2608_BPD_EN_AE)]] | SAP test script for scope item 1E3_AE (UAE): Kanban external procurement, event-driven Kanban and procurement to cost center, with master data, roles and steps. |

### Make-to-Order with Semi-Finished Goods Planning

How semi-finished goods are planned by PIRs and MRP, then assembled to order via production orders.

| Node | Description |
| --- | --- |
| [[12-production-and-manufacturing/make-to-order-production-semifinished-goods-planning-and-assembly-1bm\|Make-to-Order Production – Semifinished Goods Planning and Assembly (1BM_AE) Test Script (1BM_S4CLD2608_BPD_EN_AE)]] | SAP S/4HANA Cloud Public Edition 2608 test script for scope item 1BM_AE: MTO semifinished goods planning via PIRs, MRP, production orders and sales order consumption (plant 3310). |

### Make-to-Stock Process Manufacturing

How process orders run from PIRs and MRP through goods issue, confirmation, goods receipt and settlement.

| Node | Description |
| --- | --- |
| [[12-production-and-manufacturing/make-to-stock-process-manufacturing-based-on-process-order-bj8-ae-test\|Make-to-Stock – Process Manufacturing Based on Process Order (BJ8_AE) – Test Script (BJ8_S4CLD2608_BPD_EN_AE)]] | SAP S/4HANA Cloud Public Edition test script for scope item BJ8_AE: make-to-stock process manufacturing via PIRs, MRP, process orders, goods issue, confirmation and goods receipt. |
| [[12-production-and-manufacturing/test-script-make-to-stock-process-manufacturing-based-on-production-or\|Test Script: Make-to-Stock – Process Manufacturing Based on Production Order (2UG_AE) (2UG_S4CLD2608_BPD_EN_AE)]] | SAP S/4HANA Cloud Public Edition test script for scope item 2UG_AE: MTS process manufacturing via production orders, from PIRs and MRP to confirmation and scrap review. |
| [[12-production-and-manufacturing/test-script-make-to-stock-with-co-and-by-products-process-manufacturin\|Test Script: Make-to-Stock with Co- and By-Products – Process Manufacturing (3L7_AE) (3L7_S4CLD2608_BPD_EN_AE)]] | SAP S/4HANA Cloud test script for scope item 3L7 (AE): make-to-stock process manufacturing with co- and by-products, from PIRs and MRP to goods receipt. |
| [[12-production-and-manufacturing/make-to-stock-with-silo-material-process-manufacturing-3ul-ae-test-scr\|Make-to-Stock with Silo Material – Process Manufacturing (3UL_AE) – Test Script (3UL_S4CLD2608_BPD_EN_AE)]] | SAP S/4HANA Cloud Public Edition test script for scope item 3UL_AE: PIRs, MRP, process orders, goods issue, backflush confirmation, goods receipt (silo). |

### Material BOMs for Production and Sales

How change numbers, production BOMs (usage 1) and sales BOMs (usage 5) with item categories are created.

| Node | Description |
| --- | --- |
| [[12-production-and-manufacturing/test-script-bill-of-material-management-64f-ae-sap-s-4hana-cloud-publi\|Test Script: Bill of Material Management (64F_AE) - SAP S/4HANA Cloud Public Edition (64F_S4CLD2608_BPD_EN_AE)]] | SAP S/4HANA Cloud Public Edition 2608 (AE) test script for scope item 64F: BOM creation, major/minor change, handover to manufacturing, where-used and mass maintenance. |
| [[12-production-and-manufacturing/stammdatenskript-materialstuckliste-fur-produktion-und-vertrieb-anlege\|Stammdatenskript - Materialstückliste für Produktion und Vertrieb anlegen (BNK), DE (BNK_S4CLD2608_Master_Data_DE_XX)]] | German SAP S/4HANA Cloud Public Edition 2608 master data script (BNK): create material BOMs for production and sales, with test steps. |
| [[12-production-and-manufacturing/create-material-bom-for-production-and-sales-mds-bnk-623\|Create Material BOM for Production and Sales - MDS (BNK) (BNK_S4CLD2608_Master_Data_EN_XX)]] | SAP S/4HANA Cloud Public Edition 2608 master data script (BNK): create change number, production BOM (usage 1) and sales BOM (usage 5) with item categories. |
| [[12-production-and-manufacturing/crear-lista-de-materiales-para-material-para-produccion-y-ventas-mds-b\|Crear lista de materiales para material para producción y ventas - MDS (BNK) (BNK_S4CLD2608_Master_Data_ES_XX)]] | Spanish (machine-translated) master data test script (BNK) for creating change numbers, production BOMs and sales BOMs in SAP S/4HANA Cloud Public Edition 2608. |
| [[12-production-and-manufacturing/bom-mds-bnk-625\|マスタデータスクリプト: 製造および販売向けの品目 BOM の登録 - MDS (BNK) (BNK_S4CLD2608_Master_Data_JA_XX)]] | Japanese SAP S/4HANA Cloud 2608 master data script (BNK) for creating change numbers, production BOMs and sales BOMs (F1813A, F1813, CC01). |
| [[12-production-and-manufacturing/script-de-dados-mestre-criar-lista-tecnica-de-materiais-para-producao\|Script de dados mestre - Criar lista técnica de materiais para produção e vendas (BNK), PT (BNK_S4CLD2608_Master_Data_PT_XX)]] | Portuguese SAP S/4HANA Cloud Public Edition 2608 master data script (BNK): create material BOMs for production and sales, with test steps. |
| [[12-production-and-manufacturing/mds-bnk-627\|创建生产和销售物料清单 - MDS (BNK) (BNK_S4CLD2608_Master_Data_ZH_XX)]] | Chinese (machine-translated) SAP S/4HANA Cloud Public Edition 2608 master data script for creating production (usage 1) and sales (usage 5) BOMs with change number. |

### Manufacturing Execution System and Third-Party Shop Floor Integration

How production and process orders integrate with SAP or third-party MES for execution and confirmations.

| Node | Description |
| --- | --- |
| [[12-production-and-manufacturing/test-script-production-operations-with-manufacturing-execution-system\|Test Script: Production Operations with Manufacturing Execution System (1Y5) (1Y5_S4CLD2608_BPD_EN_XX)]] | SAP S/4HANA Cloud Public Edition 2608 test script for scope item 1Y5: MES integration with final assembly production order processing, roles, apps and steps. |
| [[12-production-and-manufacturing/test-script-third-party-shop-floor-execution-process-industry-3w3-979\|Test Script - Third-Party Shop Floor Execution – Process Industry (3W3) (3W3_S4CLD2608_BPD_EN_XX)]] | SAP S/4HANA Cloud Public Edition test script for scope item 3W3: integrating a third-party MES with process orders, from order creation to goods receipt and scrap review. |
| [[12-production-and-manufacturing/test-script-third-party-shop-floor-execution-discrete-industry-3w4-980\|Test Script: Third-Party Shop Floor Execution – Discrete Industry (3W4) (3W4_S4CLD2608_BPD_EN_XX)]] | SAP S/4HANA Cloud Public Edition 2608 test script for scope item 3W4: MES/third-party shop floor integration, from PIRs and MRP to capacity check and production orders. |

### Process Manufacturing Resources and Master Recipes

How process resources (F6176) and master recipes with phases and production versions (F5426) are created.

| Node | Description |
| --- | --- |
| [[12-production-and-manufacturing/stammdatenskript-ressource-anlegen-sds-3x8-376\|Stammdatenskript: Ressource anlegen - SDS (3X8) (3X8_S4CLD2608_Master_Data_DE_XX)]] | German master data/test script (3X8) for creating a resource (type 0008 processing unit) with app F6176 in SAP S/4HANA Cloud Public Edition 2608. |
| [[12-production-and-manufacturing/master-data-script-create-resource-mds-3x8-377\|Master Data Script: Create Resource - MDS (3X8) (3X8_S4CLD2608_Master_Data_EN_XX)]] | English master data test script (3X8): create a process manufacturing resource (processing unit 0008) in Manage Resources (F6176), with capacity and costing. |
| [[12-production-and-manufacturing/crear-recurso-mds-3x8-378\|Crear recurso - MDS (3X8) (3X8_S4CLD2608_Master_Data_ES_XX)]] | Spanish (machine-translated) master data script 3X8 for creating a production resource (app F6176) in SAP S/4HANA Cloud 2608, with a pointer to script 3X9. |
| [[12-production-and-manufacturing/mds-3x8-379\|マスタデータスクリプト: リソースの登録 - MDS (3X8) (3X8_S4CLD2608_Master_Data_JA_XX)]] | Japanese master data script (MDS 3X8) for creating process-manufacturing resources via Fiori app F6176 in SAP S/4HANA Cloud Public Edition 2608, with capacity, scheduling and costing data. |
| [[12-production-and-manufacturing/script-de-dados-mestre-criar-recurso-mds-3x8-380\|Script de dados mestre: Criar recurso - MDS (3X8) (3X8_S4CLD2608_Master_Data_PT_XX)]] | Portuguese master data/test script (3X8) for creating a resource (category 0008 processing unit) with app F6176 in SAP S/4HANA Cloud Public Edition 2608. |
| [[12-production-and-manufacturing/mds-3x8-381\|创建资源 - MDS (3X8) (3X8_S4CLD2608_Master_Data_ZH_XX)]] | 主数据脚本（中文机器翻译）：通过管理资源 (F6176) 为流程制造创建资源（处理单元），含产能、公式和成本核算。 |
| [[12-production-and-manufacturing/stammdatenskript-planungsrezept-anlegen-sds-3x9-382\|Stammdatenskript - Planungsrezept anlegen (SDS, 3X9) (3X9_S4CLD2608_Master_Data_DE_XX)]] | German master data script (scope 3X9) for creating a planning recipe in process industry in SAP S/4HANA Cloud Public Edition, with prerequisites and 18 test steps. |
| [[12-production-and-manufacturing/create-master-recipe-mds-3x9-383\|Create Master Recipe - MDS (3X9) (3X9_S4CLD2608_Master_Data_EN_XX)]] | SAP S/4HANA Cloud master data script (3X9, EN): creating a master recipe for process manufacturing in the Manage Master Recipes app (F5426). |
| [[12-production-and-manufacturing/script-de-datos-maestros-creacion-de-receta-de-planificacion-mds-3x9-3\|Script de datos maestros: Creación de receta de planificación - MDS (3X9) (3X9_S4CLD2608_Master_Data_ES_XX)]] | Spanish (machine-translated) master data script for scope item 3X9: creating a master recipe in SAP S/4HANA Cloud Public Edition via Fiori app F5426. |
| [[12-production-and-manufacturing/mds-3x9-385\|マスタレシピの登録 - MDS (3X9) (3X9_S4CLD2608_Master_Data_JA_XX)]] | Japanese master data script 3X9: creating master recipes (process industry) via app F5426 in SAP S/4HANA Cloud Public Edition 2608, with prerequisites and test steps. |
| [[12-production-and-manufacturing/criar-receita-mestre-mds-3x9-386\|Criar receita mestre - MDS (3X9) (3X9_S4CLD2608_Master_Data_PT_XX)]] | Portuguese SAP S/4HANA Cloud 2608 master data script (3X9) for creating a master recipe for process manufacturing, with phases, production version and component assignment. |
| [[12-production-and-manufacturing/mds-3x9-387\|创建主配方 - MDS (3X9) (3X9_S4CLD2608_Master_Data_ZH_XX)]] | Chinese (machine-translated) master data script 3X9 for creating a master recipe in process manufacturing via Manage Master Recipes (F5426) in S/4HANA Cloud 260 |

### Production Resources/Tools (PRTs)

How material, miscellaneous, document and equipment PRTs are created and assigned to routings and production orders.

| Node | Description |
| --- | --- |
| [[12-production-and-manufacturing/stammdatenskript-fertigungshilfsmittel-anlegen-sds-5cp-436\|Stammdatenskript - Fertigungshilfsmittel anlegen - SDS (5CP) (5CP_S4CLD2608_Master_Data_DE_XX)]] | German master data script (5CP) for SAP S/4HANA Cloud 2608: creating production resources/tools (FHM) of four types and assigning them to routings and production orders. |
| [[12-production-and-manufacturing/master-data-script-create-production-resources-tools-mds-5cp-437\|Master Data Script: Create Production Resources/Tools - MDS (5CP) (5CP_S4CLD2608_Master_Data_EN_XX)]] | SAP S/4HANA Cloud Public Edition master data script (5CP, 02-07-26) for creating material, miscellaneous, document and equipment PRTs and assigning them to routings and production orders. |
| [[12-production-and-manufacturing/script-de-datos-maestros-creacion-de-medios-auxiliares-de-fabricacion\|Script de datos maestros - Creación de medios auxiliares de fabricación - MDS (5CP) (5CP_S4CLD2608_Master_Data_ES_XX)]] | Spanish SAP S/4HANA Cloud Public Edition 2608 master data script (5CP) for creating production resources/tools (MAF) and assigning them to routings and production orders. |
| [[12-production-and-manufacturing/master-data-script-mds-5cp-japanese-439\|目的 (Master Data Script: 生産資源/治工具の登録 - MDS 5CP, Japanese) (5CP_S4CLD2608_Master_Data_JA_XX)]] | Japanese master data script (5CP) for SAP S/4HANA Cloud 2608: creating production resources/tools (PRT) as material, other, document and equipment PRTs and assigning them to routings and orders. |
| [[12-production-and-manufacturing/script-de-dados-mestre-criar-meio-auxiliar-de-producao-mds-5cp-440\|Script de dados mestre - Criar meio auxiliar de produção - MDS (5CP) (5CP_S4CLD2608_Master_Data_PT_XX)]] | Portuguese master data script (5CP) for SAP S/4HANA Cloud: creating production resources/tools (MAP/PRT) and assigning them to routings and production orders. |
| [[12-production-and-manufacturing/mds-5cp-441\|创建生产资源/工具 - MDS (5CP) (5CP_S4CLD2608_Master_Data_ZH_XX)]] | Chinese (machine-translated) master data script 5CP for SAP S/4HANA Cloud Public Edition 2608: creating production resources/tools (PRTs) and assigning them to routings and production orders. |

### Production Supply Areas

How production supply areas are created per plant and storage location via PK05S or Manage Production Supply Areas (F6935).

| Node | Description |
| --- | --- |
| [[12-production-and-manufacturing/stammdatenskript-produktionsversorgungsbereich-anlegen-sds-40d-400\|Stammdatenskript: Produktionsversorgungsbereich anlegen – SDS (40D) (40D_S4CLD2608_Master_Data_DE_XX)]] | German master data script (40D) for creating a production supply area (PVB) in SAP S/4HANA Cloud Public Edition via Fiori apps PK05S or F6935. |
| [[12-production-and-manufacturing/create-production-supply-area-mds-40d-401\|Create Production Supply Area - MDS (40D) (40D_S4CLD2608_Master_Data_EN_XX)]] | English master data script 40D: create a production supply area via PK05S or Manage Production Supply Areas (F6935) as Production Planner - Lean Manufacturing, |
| [[12-production-and-manufacturing/creacion-de-area-de-suministro-de-produccion-mds-40d-402\|Creación de área de suministro de producción - MDS (40D) (40D_S4CLD2608_Master_Data_ES_XX)]] | Spanish (machine-translated) SAP master data script for creating a production supply area via PK05S or F6935 in S/4HANA Cloud Public Edition 2608. |
| [[12-production-and-manufacturing/mds-40d-403\|供給場所の登録 - MDS (40D) (40D_S4CLD2608_Master_Data_JA_XX)]] | Japanese master data test script (MDS 40D) for creating a production supply area in SAP S/4HANA Cloud Public Edition 2608 via PK05S or F6935. |
| [[12-production-and-manufacturing/criar-area-de-abastecimento-da-producao-mds-40d-404\|Criar área de abastecimento da produção – MDS (40D) (40D_S4CLD2608_Master_Data_PT_XX)]] | Portuguese SAP S/4HANA Cloud master data script (40D): create a production supply area via PK05S (quick entry) or F6935 (manage), by plant and storage location. |
| [[12-production-and-manufacturing/mds-40d-405\|创建生产供应区 - MDS (40D) (40D_S4CLD2608_Master_Data_ZH_XX)]] | SAP S/4HANA Cloud Public Edition 2608 主数据脚本 (40D): 通过 PK05S 或 F6935 创建生产供应区的步骤 (中文机器翻译)。 |

### Production Versions

How production versions linking BOM and routing are created and edited (F6400, F2568).

| Node | Description |
| --- | --- |
| [[12-production-and-manufacturing/fertigungsversion-anlegen-sds-bld-568\|Fertigungsversion anlegen – SDS (BLD) (BLD_S4CLD2608_Master_Data_DE_XX)]] | German master data script (BLD) for SAP S/4HANA Cloud Public Edition: create and edit production versions via Fiori apps F6400 and F2568. |
| [[12-production-and-manufacturing/master-data-script-create-production-version-mds-bld-569\|Master Data Script: Create Production Version - MDS (BLD) (BLD_S4CLD2608_Master_Data_EN_XX)]] | Master data script BLD for creating and editing production versions in S/4HANA Cloud Public Edition 2608 using Fiori apps F6400 and F2568. |
| [[12-production-and-manufacturing/script-de-datos-maestros-creacion-de-version-de-produccion-mds-bld-570\|Script de datos maestros: Creación de versión de producción - MDS (BLD) (BLD_S4CLD2608_Master_Data_ES_XX)]] | Spanish (machine-translated) master data script for creating and editing production versions in SAP S/4HANA Cloud Public Edition via Fiori apps F6400 and F2568. |
| [[12-production-and-manufacturing/mds-bld-571\|製造バージョンの登録 - MDS (BLD) (BLD_S4CLD2608_Master_Data_JA_XX)]] | Japanese SAP S/4HANA Cloud Public Edition master data script (BLD) for creating and editing production versions via F6400 or F2568. |
| [[12-production-and-manufacturing/script-de-dados-mestre-criar-versao-de-producao-mds-bld-572\|Script de dados mestre: Criar versão de produção - MDS (BLD) (BLD_S4CLD2608_Master_Data_PT_XX)]] | Portuguese master data script for SAP S/4HANA Cloud Public Edition: creating and editing a production version (F6400, F2568), with roles and required master data. |
| [[12-production-and-manufacturing/mds-bld-573\|创建生产版本 - MDS (BLD) (BLD_S4CLD2608_Master_Data_ZH_XX)]] | Chinese machine-translated master data script (BLD) for creating and editing production versions via F6400 or F2568 in SAP S/4HANA Cloud Public Edition. |

### Production Work Centers and Work Center Groups

How production work centers (F6175) with capacities, costing and scheduling data and optional work center groups (F4044) are created.

| Node | Description |
| --- | --- |
| [[12-production-and-manufacturing/stammdatenskript-produktionsarbeitsplatz-anlegen-sds-bnj-616\|Stammdatenskript: Produktionsarbeitsplatz anlegen – SDS (BNJ) (BNJ_S4CLD2608_Master_Data_DE_XX)]] | German SAP S/4HANA Cloud Public Edition test script (BNJ) for creating a production work center and optionally work center groups; lists roles, parameters and steps. |
| [[12-production-and-manufacturing/create-production-work-center-mds-bnj-617\|Create Production Work Center - MDS (BNJ) (BNJ_S4CLD2608_Master_Data_EN_XX)]] | SAP S/4HANA Cloud 2608 master data script BNJ: create a production work center (F6175) and optionally work center groups (F4044), with test steps. |
| [[12-production-and-manufacturing/script-de-datos-maestros-crear-puesto-de-trabajo-de-produccion-mds-bnj\|Script de datos maestros - Crear puesto de trabajo de producción - MDS (BNJ) (BNJ_S4CLD2608_Master_Data_ES_XX)]] | Spanish SAP S/4HANA Cloud Public Edition 2608 master data test script BNJ: create a production work center (F6175) and optionally work center groups (F4044). |
| [[12-production-and-manufacturing/mds-bnj-619\|製造作業区の登録 - MDS (BNJ) (BNJ_S4CLD2608_Master_Data_JA_XX)]] | Japanese SAP S/4HANA Cloud Public Edition master data script (BNJ) for creating production work centers and work center groups with F6175 and F4044. |
| [[12-production-and-manufacturing/script-de-dados-mestre-criar-centro-de-trabalho-da-producao-mds-bnj-62\|Script de dados mestre - Criar centro de trabalho da produção – MDS (BNJ) (BNJ_S4CLD2608_Master_Data_PT_XX)]] | SAP S/4HANA Cloud Public Edition 2608 master data script (Portuguese) for creating production work centers and optional work center groups via Fiori apps. |
| [[12-production-and-manufacturing/mds-bnj-621\|创建生产工作中心 - MDS (BNJ) (BNJ_S4CLD2608_Master_Data_ZH_XX)]] | Chinese machine-translated master data script (BNJ) for creating production work centers, work center groups and assignments in SAP S/4HANA Cloud Public Edition. |

### Rework Processing

How rework is handled via separate rework orders for stock material or inserted rework operations for work in process.

| Node | Description |
| --- | --- |
| [[12-production-and-manufacturing/test-script-rework-with-quality-management-consumer-products-6a9-ae-11\|Test Script: Rework with Quality Management – Consumer Products (6A9_AE) (6A9_S4CLD2608_BPD_EN_AE)]] | SAP S/4HANA Cloud Public Edition 2608 test script for scope item 6A9 (AE): rework of production orders with QM, covering in-production and post-goods-receipt rework. |
| [[12-production-and-manufacturing/rework-processing-stock-manufactured-material-bjn-ae-test-script-1275\|Rework Processing – Stock-Manufactured Material (BJN_AE) Test Script (BJN_S4CLD2608_BPD_EN_AE)]] | SAP S/4HANA Cloud Public Edition 2608 test script for scope item BJN (AE): rework production order for stock-manufactured material, from order creation to goods receipt. |
| [[12-production-and-manufacturing/test-script-rework-processing-work-in-process-bjq-ae-1276\|Test Script: Rework Processing - Work-in-Process (BJQ_AE) (BJQ_S4CLD2608_BPD_EN_AE)]] | Test script for scope item BJQ (AE): rework operation inserted within a production order, confirmed and settled in S/4HANA Cloud Public Edition 2608, plant 3310. |

### Routings and Reference Operation Sets

How production routings with operations and component assignment (F5425) and reference operation sets (CA11) are created.

| Node | Description |
| --- | --- |
| [[12-production-and-manufacturing/standardarbeitsplan-anlegen-sds-ble-574\|Standardarbeitsplan anlegen – SDS (BLE) (BLE_S4CLD2608_Master_Data_DE_XX)]] | German SAP S/4HANA Cloud master data script (BLE): create a standard routing (reference operation set) with CA11, including prerequisites and test steps. |
| [[12-production-and-manufacturing/master-data-script-create-reference-operation-set-mds-ble-575\|Master Data Script: Create Reference Operation Set - MDS (BLE) (BLE_S4CLD2608_Master_Data_EN_XX)]] | SAP S/4HANA Cloud 2608 master data script (BLE) for creating a reference operation set (reference routing) via CA11 as Production Engineer - Discrete Manufacturing. |
| [[12-production-and-manufacturing/script-de-datos-maestros-crear-hoja-de-ruta-estandar-mds-ble-576\|Script de datos maestros - Crear hoja de ruta estándar - MDS (BLE) (BLE_S4CLD2608_Master_Data_ES_XX)]] | Spanish (machine-translated) SAP S/4HANA Cloud 2608 master data script BLE: create a reference (standard) routing with transaction CA11. |
| [[12-production-and-manufacturing/mds-ble-577\|参照作業セットの登録 - MDS (BLE) (BLE_S4CLD2608_Master_Data_JA_XX)]] | Japanese master data test script (MDS BLE) for creating a reference operation set in SAP S/4HANA Cloud Public Edition 2608 via CA11, Production Engineer role. |
| [[12-production-and-manufacturing/script-de-dados-mestre-criar-conjunto-de-operacoes-de-referencia-mds-b\|Script de dados mestre: Criar conjunto de operações de referência – MDS (BLE) (BLE_S4CLD2608_Master_Data_PT_XX)]] | Portuguese SAP S/4HANA Cloud master data script BLE: create a reference operation set (standard task list) in transaction CA11 for discrete production. |
| [[12-production-and-manufacturing/mds-ble-579\|创建参考工序集 - MDS (BLE) (BLE_S4CLD2608_Master_Data_ZH_XX)]] | SAP S/4HANA Cloud Public Edition 2608 主数据脚本 (BLE): 通过 CA11 创建参考工序集 (参考工艺路线) 的步骤 (中文机器翻译)。 |
| [[12-production-and-manufacturing/arbeitsplan-anlegen-sds-bnl-628\|Arbeitsplan anlegen – SDS (BNL) (BNL_S4CLD2608_Master_Data_DE_XX)]] | German master data script BNL for SAP S/4HANA Cloud Public Edition 2608: creating a manufacturing routing (Arbeitsplan) with operations and component allocation in app F5425. |
| [[12-production-and-manufacturing/master-data-script-create-routing-mds-bnl-629\|Master Data Script: Create Routing - MDS (BNL) (BNL_S4CLD2608_Master_Data_EN_XX)]] | Master data script BNL for creating a production routing in SAP S/4HANA Cloud Public Edition with Manage Routings (F5425) as Production Engineer. |
| [[12-production-and-manufacturing/creacion-de-hoja-de-ruta-mds-bnl-630\|Creación de hoja de ruta - MDS (BNL) (BNL_S4CLD2608_Master_Data_ES_XX)]] | Spanish machine-translated SAP S/4HANA Cloud 2608 master data script (BNL) for creating a production routing (hoja de ruta) with operations and component assignment in discrete manufacturing. |
| [[12-production-and-manufacturing/mds-bnl-631\|マスタデータスクリプト: 作業手順の登録 - MDS (BNL) (BNL_S4CLD2608_Master_Data_JA_XX)]] | Japanese master data script (MDS BNL) for creating production routings in SAP S/4HANA Cloud Public Edition 2608 via Fiori app F5425, with prerequisites and test steps. |
| [[12-production-and-manufacturing/criar-roteiro-mds-bnl-632\|Criar roteiro - MDS (BNL) (BNL_S4CLD2608_Master_Data_PT_XX)]] | Portuguese SAP S/4HANA Cloud master data script (BNL): creating a production routing (roteiro) for discrete manufacturing in Administrar itinerários (F5425). |
| [[12-production-and-manufacturing/mds-bnl-633\|创建工艺路线 - MDS (BNL) (BNL_S4CLD2608_Master_Data_ZH_XX)]] | 主数据脚本（中文机器翻译）：通过管理工艺路线 (F5425) 为成品/半成品创建生产工艺路线，含工序、组件分配。 |

### Storage Tank Management and Tank Trailer Filling

How batches are received into day tanks and mixed with main tank batches via process orders (3UK), and how tank trailers are filled from process orders netting residuals (42N).

| Node | Description |
| --- | --- |
| [[12-production-and-manufacturing/inbound-storage-tank-management-process-manufacturing-3uk-ae-971\|Inbound Storage Tank Management – Process Manufacturing (3UK_AE) (3UK_S4CLD2608_BPD_EN_AE)]] | SAP S/4HANA Cloud Public Edition 2608 test script for scope item 3UK_AE: receive a batch into a day tank, mix with main tank batch via process order, with QM. |
| [[12-production-and-manufacturing/test-script-tank-trailer-filling-with-residuals-42n-ae-997\|Test Script: Tank Trailer Filling with Residuals (42N_AE) (42N_S4CLD2608_BPD_EN_AE)]] | SAP S/4HANA Cloud Public Edition test script (scope item 42N_AE): fill tank trailers from a process order, netting residual stock via container ID and MQC. |

### Production Subcontracting and External Processing

How externally processed operations create POs, provide components and receive goods back into production orders.

| Node | Description |
| --- | --- |
| [[12-production-and-manufacturing/production-subcontracting-external-processing-bjk-ae-1274\|Production Subcontracting – External Processing (BJK_AE) (BJK_S4CLD2608_BPD_EN_AE)]] | SAP S/4HANA Cloud Public Edition 2608 test script (BJK_AE, UAE) for production subcontracting: external-operation production order, PO, goods receipt, supplier invoice, payment. |

### Production with Third-Party Warehouse Management

How production and process orders stage and backflush materials when storage locations are managed by a third-party WMS.

| Node | Description |
| --- | --- |
| [[11-inventory-warehouse-and-transportation/test-script-logistics-with-third-party-warehouse-management-1zq-ae-793\|Test Script: Logistics with Third-Party Warehouse Management (1ZQ_AE) (1ZQ_S4CLD2608_BPD_EN_AE)]] | SAP S/4HANA Cloud Public Edition test script for scope item 1ZQ_AE: stock transfers, procurement, sales and returns integrated with a third-party WMS. |
| [[12-production-and-manufacturing/test-script-production-order-processing-with-third-party-warehouse-man\|Test Script: Production Order Processing with Third-Party Warehouse Management (2RU_AE) (2RU_S4CLD2608_BPD_EN_AE)]] | SAP S/4HANA Cloud Public Edition 2608 test script for scope item 2RU_AE: production/process order processing with a third-party WMS, with prerequisites and test steps. |

### Production of Variant-Configured Products

How configurable products are quoted, ordered, planned and produced to order (incl. lot size one with advanced variant configuration) or to stock as material variants.

| Node | Description |
| --- | --- |
| [[02-business-partner-and-product-master-data/set-up-configurable-model-using-variant-configuration-22t-ae-test-scri\|Set Up Configurable Model Using Variant Configuration (22T_AE) - Test Script, SAP S/4HANA Cloud Public Edition 2608 (22T_S4CLD2608_BPD_EN_AE)]] | SAP S/4HANA Cloud Public Edition 2608 (AE) test script for scope item 22T: model, simulate and replicate a configurable forklift using variant configuration. |
| [[12-production-and-manufacturing/test-script-lot-size-of-one-with-advanced-variant-configuration-55e-ae\|Test Script: Lot Size of One with Advanced Variant Configuration (55E_AE) (55E_S4CLD2608_BPD_EN_AE)]] | SAP S/4HANA Cloud Public Edition 2608 test script for scope item 55E (AE): make-to-order robot with advanced variant configuration, from inquiry to payments. |
| [[12-production-and-manufacturing/test-script-make-to-order-production-with-variant-configuration-1yt-ae\|Test Script: Make-to-Order Production with Variant Configuration (1YT_AE) - SAP S/4HANA Cloud Public Edition (1YT_S4CLD2608_BPD_EN_AE)]] | SAP S/4HANA Cloud 2608 (AE) test script for scope item 1YT_AE: make-to-order production of configurable fork lifters, from quotation to billing. |
| [[12-production-and-manufacturing/test-script-make-to-stock-production-with-variant-configuration-21d-ae\|Test Script: Make-to-Stock Production with Variant Configuration (21D_AE) (21D_S4CLD2608_BPD_EN_AE)]] | SAP S/4HANA Cloud Public Edition test script for scope item 21D_AE: prerequisites and steps to produce, stock, sell and bill forklifter material variants. |

### Make-to-Stock Discrete and Repetitive Manufacturing

How PIRs and MRP drive production orders or repetitive manufacturing planned orders through staging, confirmation, backflush and goods receipt.

| Node | Description |
| --- | --- |
| [[12-production-and-manufacturing/test-script-make-to-stock-production-discrete-manufacturing-bj5-ae-sap\|Test Script: Make-to-Stock Production – Discrete Manufacturing (BJ5_AE), SAP S/4HANA Cloud Public Edition (BJ5_S4CLD2608_BPD_EN_AE)]] | SAP S/4HANA Cloud Public Edition test script for scope item BJ5_AE: MTS discrete manufacturing from PIRs and MRP to production orders and goods receipt. |
| [[12-production-and-manufacturing/test-script-make-to-stock-production-repetitive-manufacturing-bjh-ae-s\|Test Script: Make-to-Stock Production – Repetitive Manufacturing (BJH_AE), SAP S/4HANA Cloud Public Edition (BJH_S4CLD2608_BPD_EN_AE)]] | SAP Best Practices test script for scope item BJH_AE: repetitive manufacturing from PIRs and MRP to planning table, staging, REM backflush, error handling. |

### Make-to-Order Production

How customer sales orders for finished goods trigger MRP, order BOMs, production or process orders, down payments, delivery and billing in make-to-order.

| Node | Description |
| --- | --- |
| [[12-production-and-manufacturing/test-script-lot-size-of-one-based-on-make-to-order-7dw-ae-sap-s-4hana\|Test Script: Lot Size of One based on Make to Order (7DW_AE) - SAP S/4HANA Cloud Public Edition (7DW_S4CLD2608_BPD_EN_AE)]] | SAP S/4HANA Cloud Public Edition 2608 test script for scope item 7DW (AE): make-to-order lot size one, from sales order and down payment through production, QM, delivery, billing, payments. |
| [[12-production-and-manufacturing/test-script-make-to-order-production-finished-goods-sales-and-final-as\|Test Script: Make-to-Order Production – Finished Goods Sales and Final Assembly (BJE_AE) (BJE_S4CLD2608_BPD_EN_AE)]] | SAP S/4HANA Cloud Public Edition 2608 (AE) test script for scope item BJE: make-to-order quotation, sales order, MRP, production, delivery and billing steps. |
| [[12-production-and-manufacturing/test-script-make-to-order-production-process-manufacturing-3ok-ae-966\|Test Script: Make-to-Order Production – Process Manufacturing (3OK_AE) (3OK_S4CLD2608_BPD_EN_AE)]] | SAP S/4HANA Cloud Public Edition 2608 (AE) test script for scope item 3OK: make-to-order process manufacturing from sales order/quotation through MRP, process order, delivery and billing. |

### Material Requirements Planning and Predictive MRP

How PIRs, MRP runs, coverage and exceptions plan materials across plants, and how predictive MRP simulates demand against supplier and capacity constraints.

| Node | Description |
| --- | --- |
| [[12-production-and-manufacturing/test-script-sap-s-4hana-cloud-public-edition-predictive-material-and-r\|Test Script SAP S/4HANA Cloud Public Edition - Predictive Material and Resource Planning (4B5_AE) (4B5_S4CLD2608_BPD_EN_AE)]] | SAP test script for scope item 4B5 (AE, 2608): predictive MRP simulations, PIR release, plus supplier and production-line constraint use cases. |
| [[12-production-and-manufacturing/test-script-planning-and-production-in-other-plant-consumer-products-7\|Test Script: Planning and Production in Other Plant – Consumer Products (7DN_AE), SAP S/4HANA Cloud Public Edition (7DN_S4CLD2608_BPD_EN_AE)]] | SAP test script, scope item 7DN_AE: cross-plant MRP, process/production orders, sales order, delivery and billing for Consumer Products (plants 3310, 3320). |
| [[12-production-and-manufacturing/test-script-material-requirements-planning-j44-ae-sap-s-4hana-cloud-pu\|Test Script: Material Requirements Planning (J44_AE) - SAP S/4HANA Cloud Public Edition (J44_S4CLD2608_BPD_EN_AE)]] | Step-by-step Fiori test script for scope item J44_AE (MRP, UAE plant 3310): PIRs, MRP run, safety stock/days of supply, material exceptions, MRP change requests |

### Capacity Evaluation and Leveling

How work center capacity is evaluated, bottlenecks detected and production or process orders leveled with the capacity scheduling table or board.

| Node | Description |
| --- | --- |
| [[12-production-and-manufacturing/production-capacity-evaluation-and-leveling-consumer-products-5oi-ae-t\|Production Capacity Evaluation and Leveling – Consumer Products (5OI_AE) – Test Script (5OI_S4CLD2608_BPD_EN_AE)]] | SAP S/4HANA Cloud Public Edition test script for scope item 5OI_AE: PIRs, pMRP simulations, MRP, capacity evaluation and leveling for a coffee MTS process. |
| [[12-production-and-manufacturing/test-script-capacity-planning-evaluation-scope-item-31l-sap-s-4hana-cl\|Test Script - Capacity Planning Evaluation (scope item 31L), SAP S/4HANA Cloud Public Edition 2608 (31L_S4CLD2608_BPD_EN_AE)]] | SAP test script for capacity evaluation in make-to-stock Discrete and Process Manufacturing: PIRs, MRP, bottleneck check, shift changes, order conversion. |
| [[12-production-and-manufacturing/test-script-production-capacity-leveling-3lq-ae-sap-s-4hana-cloud-publ\|Test Script: Production Capacity Leveling (3LQ_AE) - SAP S/4HANA Cloud Public Edition (3LQ_S4CLD2608_BPD_EN_AE)]] | SAP S/4HANA Cloud Public Edition 2608 test script for scope item 3LQ_AE: prerequisites, sample data and steps for production capacity leveling, discrete and process manufacturing. |

### Demand-Driven Replenishment (DDMRP)

How buffer positioning, buffer sizing and net flow planning manage decoupled lead time, replenishment execution and buffer performance in demand-driven MRP.

| Node | Description |
| --- | --- |
| [[12-production-and-manufacturing/test-script-demand-driven-buffer-level-management-1y2-ae-sap-s-4hana-c\|Test Script: Demand-Driven Buffer Level Management (1Y2_AE) - SAP S/4HANA Cloud Public Edition (1Y2_S4CLD2608_BPD_EN_AE)]] | SAP S/4HANA Cloud 2608 test script for scope item 1Y2 (AE): demand-driven buffer positioning, buffer sizing and buffer level management, plus pMRP use cases. |
| [[12-production-and-manufacturing/test-script-demand-driven-replenishment-planning-and-execution-2qi-ae\|Test Script: Demand-Driven Replenishment Planning and Execution (2QI_AE) (2QI_S4CLD2608_BPD_EN_AE)]] | S/4HANA Cloud test script for scope item 2QI_AE: demand-driven replenishment planning, execution, projected on-hand alerts and buffer performance (plant 3310). |

### Production Order Combination

How make-to-stock and make-to-order production orders are combined into one combined order, released, confirmed and reviewed against the original orders.

| Node | Description |
| --- | --- |
| [[12-production-and-manufacturing/test-script-production-order-combination-7to-ae-sap-s-4hana-cloud-publ\|Test Script: Production Order Combination (7TO_AE) - SAP S/4HANA Cloud Public Edition 2608 (7TO_S4CLD2608_BPD_EN_AE)]] | SAP Best Practices test script (UAE localization) for scope item 7TO: combining MTS/MTO production orders into a combined order, executing it and reviewing original orders. |

### Product Change Management with Change Records

How change records bundle BOM and product changes and move them through submission, approval, implementation, closing and release.

| Node | Description |
| --- | --- |
| [[12-production-and-manufacturing/test-script-product-change-management-with-change-records-64e-ae-sap-s\|Test Script: Product Change Management with Change Records (64E_AE) - SAP S/4HANA Cloud Public Edition 2608 (64E_S4CLD2608_BPD_EN_AE)]] | SAP test script for scope item 64E: change record lifecycle (create, assign BOM, submit, approve, implement, close, release) in S/4HANA Cloud 2608. |

### End-to-End Produce-and-Sell Scenarios

How end-to-end scenarios run from planning and production through warehouse, quality, sales, billing and payment for standard and consumer products.

| Node | Description |
| --- | --- |
| [[08-sales-order-management/customer-returns-management-consumer-products-61v-ae-test-script-sap-s\|Customer Returns Management – Consumer Products (61V_AE) – Test Script, SAP S/4HANA Cloud Public Edition (61V_S4CLD2608_BPD_EN_AE)]] | SAP test script for scope item 61V_AE (Customer Returns, Consumer Products): roles, master data and test steps from returns order to refund and credit memo. |
| [[08-sales-order-management/test-script-sell-from-stock-consumer-products-5hl-ae-sap-s-4hana-cloud\|Test Script: Sell from Stock – Consumer Products (5HL_AE), SAP S/4HANA Cloud Public Edition (5HL_S4CLD2608_BPD_EN_AE)]] | SAP test script for scope item 5HL_AE: sell from stock and from valuated stock in transit, order to invoice list, with roles, apps, test data and postings. |
| [[10-procurement/test-script-procurement-of-production-components-consumer-products-5w3\|Test Script: Procurement of Production Components – Consumer Products (5W3_AE) (5W3_S4CLD2608_BPD_EN_AE)]] | SAP S/4HANA Cloud Public Edition 2608 test script for scope item 5W3 (AE): procure batch-managed raw material with QM and packaging without QM, plant 3310. |
| [[10-procurement/test-script-subcontracting-consumer-products-5w4-ae-sap-s-4hana-cloud\|Test Script: Subcontracting - Consumer Products (5W4_AE), SAP S/4HANA Cloud Public Edition (5W4_S4CLD2608_BPD_EN_AE)]] | SAP S/4HANA Cloud Public Edition 2608 test script for scope item 5W4_AE: subcontracting with batch anonymization, MRP areas, quality inspection and invoicing (plant 3310). |
| [[12-production-and-manufacturing/production-capacity-evaluation-and-leveling-consumer-products-5oi-ae-t\|Production Capacity Evaluation and Leveling – Consumer Products (5OI_AE) – Test Script (5OI_S4CLD2608_BPD_EN_AE)]] | SAP S/4HANA Cloud Public Edition test script for scope item 5OI_AE: PIRs, pMRP simulations, MRP, capacity evaluation and leveling for a coffee MTS process. |
| [[12-production-and-manufacturing/test-script-produce-and-sell-standard-products-inventory-management-54-part-01\|Test Script: Produce and Sell Standard Products – Inventory Management (54U_AE), SAP S/4HANA Cloud Public Edition (54U_S4CLD2608_BPD_EN_AE) — part 1 of 2]] | S/4HANA Cloud Public Edition test script, scope item 54U_AE (UAE, plant 3310): make-to-stock production of a serial-numbered product, planning to payment. |
| [[12-production-and-manufacturing/test-script-produce-and-sell-standard-products-inventory-management-54-part-02\|Test Script: Produce and Sell Standard Products – Inventory Management (54U_AE), SAP S/4HANA Cloud Public Edition (54U_S4CLD2608_BPD_EN_AE) — part 2 of 2]] | SAP S/4HANA Cloud 2608 test script 54U (AE), part 2: usage decision, outbound delivery, rejected stock, billing, customer/supplier payments. |
| [[12-production-and-manufacturing/produce-and-sell-standard-products-warehouse-managed-54v-ae-test-scrip\|Produce and Sell Standard Products – Warehouse Managed (54V_AE) – Test Script, SAP S/4HANA Cloud Public Edition (54V_S4CLD2608_BPD_EN_AE)]] | Test script for scope item 54V_AE (UAE, plant 3310): MTS planning, repetitive and discrete production, WM-managed warehouse, QM, sales, billing and AP/AR posting. |
| [[12-production-and-manufacturing/test-script-sap-s-4hana-cloud-public-edition-from-planning-to-fulfillm-part-01\|Test Script SAP S/4HANA Cloud Public Edition - From Planning to Fulfillment - Consumer Products (6AA_AE) (6AA_S4CLD2608_BPD_EN_AE) — part 1 of 3]] | SAP Best Practices test script for the AE Consumer Products planning-to-fulfillment scenario (5OI, 5W3, 5HK, 5W4, 5HL, 61V): prerequisites, setup, step-by-step Fiori test procedures. |
| [[12-production-and-manufacturing/test-script-sap-s-4hana-cloud-public-edition-from-planning-to-fulfillm-part-02\|Test Script SAP S/4HANA Cloud Public Edition - From Planning to Fulfillment - Consumer Products (6AA_AE) (6AA_S4CLD2608_BPD_EN_AE) — part 2 of 3]] | SAP S/4HANA Cloud 6AA_AE Consumer Products test script, part 2: raw-material QM, 5HK QM in discrete manufacturing, start of 5W4 subcontracting; Fiori steps. |
| [[12-production-and-manufacturing/test-script-sap-s-4hana-cloud-public-edition-from-planning-to-fulfillm-part-03\|Test Script SAP S/4HANA Cloud Public Edition - From Planning to Fulfillment - Consumer Products (6AA_AE) (6AA_S4CLD2608_BPD_EN_AE) — part 3 of 3]] | SAP Fiori test script 6AA_AE (UAE); this part: subcontracting inspection and invoicing, sell from stock/in transit, customer returns, billing jobs. |

## Related categories
- related-to :: [[02-business-partner-and-product-master-data/_cluster]]
- related-to :: [[11-inventory-warehouse-and-transportation/_cluster]]
- related-to :: [[06-management-accounting/_cluster]]
