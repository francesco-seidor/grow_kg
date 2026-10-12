---
title: Business Partner and Product Master Data
description: "Creating product masters by material type, configurable materials, product hierarchies, customer and supplier business partners, and master data consolidation, quality and mass load."
cluster: 02-business-partner-and-product-master-data
type: cluster
tags: [kb/business-partner-and-product-master-data, kb/hub]
keywords: [product master, material type, business partner, customer master, supplier master, KMAT, product hierarchy, MDG, consolidation, mass maintenance, data quality]
node_count: 99
created: 2026-10-12
updated: 2026-10-12
---

# Business Partner and Product Master Data

Covers only cross-process master data: products and business partners and their governance. Excludes process-specific master data, which lives with its process: customer hierarchies, customer-material info records and substitutions (see 08), batches and EWM product attributes (see 11), BOMs, routings and work centers (see 12), QM views (see 13), service products (see 14), treasury partners (see 05), carriers (see 11) and HQ-subsidiary replication (see 16).

Every node below is the verbatim text of one source document (or one part of a long one), grouped by topic.

## Nodes

### Integration of Core Master Data from On-Premise

How material, customer and supplier master data is replicated from an SAP on-premise system into S/4HANA Cloud (scope item 1RO).

| Node | Description |
| --- | --- |
| [[02-business-partner-and-product-master-data/test-script-integration-of-core-master-data-1ro-ae-758\|Test Script: Integration of Core Master Data (1RO_AE) (1RO_S4CLD2608_BPD_EN_AE)]] | SAP S/4HANA Cloud Public Edition 2608 test script for scope item 1RO: replicating material, customer and supplier master data from an SAP on-premise system. |

### Customer Master Data

How to create customer business partners with general, company code and sales area data via Maintain Business Partner or Manage Customer Master Data.

| Node | Description |
| --- | --- |
| [[02-business-partner-and-product-master-data/stammdatenskript-kundenstamm-anlegen-sds-bnd-580\|Stammdatenskript: Kundenstamm anlegen – SDS (BND) (BND_S4CLD2608_Master_Data_DE_XX)]] | German SAP S/4HANA Cloud Public Edition 2608 master data script: test procedures to create customer master data (general, company code, sales area) via BP or F0850A. |
| [[02-business-partner-and-product-master-data/master-data-script-create-customer-master-mds-bnd-sap-s-4hana-cloud-pu\|Master Data Script - Create Customer Master - MDS (BND), SAP S/4HANA Cloud Public Edition (BND_S4CLD2608_Master_Data_EN_XX)]] | SAP S/4HANA Cloud Public Edition 2608 test script for creating customer master data (general, company code, sales area) via Maintain Business Partner or F0850A. |
| [[02-business-partner-and-product-master-data/script-de-datos-maestros-creacion-de-maestro-de-clientes-mds-bnd-582\|Script de datos maestros - Creación de maestro de clientes (MDS BND) (BND_S4CLD2608_Master_Data_ES_XX)]] | SAP S/4HANA Cloud Public Edition 2608 (Spanish) test script for creating customer master data: general, company code and sales area data via two Fiori apps. |
| [[02-business-partner-and-product-master-data/mds-bnd-583\|マスタデータスクリプト 得意先マスタの登録 - MDS (BND) (BND_S4CLD2608_Master_Data_JA_XX)]] | Japanese master data script (BND) for SAP S/4HANA Cloud Public Edition 2608: creating customer master data (general, company code, sales area) via BP or F0850A. |
| [[02-business-partner-and-product-master-data/script-de-dados-mestre-criar-mestre-de-clientes-bnd-sap-s-4hana-cloud\|Script de dados mestre - Criar mestre de clientes (BND) - SAP S/4HANA Cloud Public Edition (BND_S4CLD2608_Master_Data_PT_XX)]] | Portuguese SAP S/4HANA Cloud Public Edition 2608 master data test script for creating customer master (general, company code, sales area data) via BP or F0850A apps. |
| [[02-business-partner-and-product-master-data/mds-bnd-585\|创建客户主数据 - MDS (BND) 主数据脚本 (BND_S4CLD2608_Master_Data_ZH_XX)]] | Chinese (machine-translated) SAP S/4HANA Cloud Public Edition 2608 master data script for creating customer master data: general, company code and sales area data. |

### Data Quality Management for Products and Business Partners

How rule mining, validation rules, data quality scores and evaluation runs measure and fix product and business partner data quality.

| Node | Description |
| --- | --- |
| [[02-business-partner-and-product-master-data/data-quality-management-for-business-partner-4ap-test-script-1011\|Data Quality Management for Business Partner (4AP) Test Script (4AP_S4CLD2608_BPD_EN_XX)]] | Test script for scope item 4AP in SAP S/4HANA Cloud Public Edition: rule mining, validation rules, data quality scores and evaluation for business partner master data. |
| [[02-business-partner-and-product-master-data/test-script-data-quality-management-for-product-4aq-1012\|Test Script: Data Quality Management for Product (4AQ) (4AQ_S4CLD2608_BPD_EN_XX)]] | SAP S/4HANA Cloud Public Edition 2608 test script (4AQ) for product data quality: rule mining, validation rules, quality scores, evaluation runs and overview. |

### Master Data Consolidation for Products and Business Partners

How to import, match duplicates, calculate best records, validate and activate product or business partner data in consolidation processes.

| Node | Description |
| --- | --- |
| [[02-business-partner-and-product-master-data/test-script-master-data-consolidation-for-product-1n1-742\|Test Script: Master Data Consolidation for Product (1N1) (1N1_S4CLD2608_BPD_EN_XX)]] | SAP S/4HANA Cloud Public Edition 2608 test script for scope item 1N1: import, match, consolidate, validate and activate product master data. |
| [[02-business-partner-and-product-master-data/test-script-master-data-consolidation-for-business-partner-1n3-743\|Test Script: Master Data Consolidation for Business Partner (1N3) (1N3_S4CLD2608_BPD_EN_XX)]] | SAP S/4HANA Cloud Public Edition test script for scope item 1N3: importing, matching, best-record calculation, validation, activation and automation of business partner consolidation. |

### Product Hierarchies

How to configure product hierarchy nodes and create, validate and activate a product hierarchy in Manage Product Hierarchies.

| Node | Description |
| --- | --- |
| [[02-business-partner-and-product-master-data/stammdatenskript-produkthierarchie-anlegen-4dx-412\|Stammdatenskript: Produkthierarchie anlegen (4DX) (4DX_S4CLD2608_Master_Data_DE_XX)]] | German master data script (4DX) for SAP S/4HANA Cloud Public Edition 2608: configure hierarchy nodes and create/activate a product hierarchy with Manage Product Hierarchies (F4359). |
| [[02-business-partner-and-product-master-data/master-data-script-create-product-hierarchy-4dx-413\|Master Data Script: Create Product Hierarchy (4DX) (4DX_S4CLD2608_Master_Data_EN_XX)]] | SAP S/4HANA Cloud Public Edition 2608 master data script (4DX) for configuring product hierarchy nodes and creating/activating a Product Hierarchy in Manage Product Hierarchies. |
| [[02-business-partner-and-product-master-data/script-de-datos-maestros-crear-jerarquia-de-productos-4dx-414\|Script de datos maestros: Crear jerarquía de productos (4DX) (4DX_S4CLD2608_Master_Data_ES_XX)]] | Spanish SAP S/4HANA Cloud Public Edition master data script (4DX) for creating product hierarchies, incl. node configuration prerequisite and test steps; dated 02-07-26. |
| [[02-business-partner-and-product-master-data/4dx-415\|マスタデータスクリプト 製品階層の登録 (4DX) (4DX_S4CLD2608_Master_Data_JA_XX)]] | Japanese master data script (4DX) for creating product hierarchies in SAP S/4HANA Cloud Public Edition 2608, incl. node configuration and app F4359 steps. |
| [[02-business-partner-and-product-master-data/script-de-dados-mestre-criar-hierarquia-de-produtos-4dx-416\|Script de dados mestre - Criar hierarquia de produtos (4DX) (4DX_S4CLD2608_Master_Data_PT_XX)]] | Portuguese SAP S/4HANA Cloud Public Edition master data script (4DX): configure hierarchy nodes and create/activate a product hierarchy in Fiori app F4359. |
| [[02-business-partner-and-product-master-data/4dx-417\|创建产品层次结构 (4DX) 主数据脚本 (4DX_S4CLD2608_Master_Data_ZH_XX)]] | Chinese (machine-translated) master data script 4DX: configure product hierarchy nodes then create and activate a product hierarchy via Manage Product Hierarchi |

### Mass Load and Mass Maintenance for Products

How to mass load, mass change, export and remediate product master data in the 1RM mass processing apps.

| Node | Description |
| --- | --- |
| [[02-business-partner-and-product-master-data/test-script-mass-load-and-mass-maintenance-for-product-1rm-757\|Test Script: Mass Load and Mass Maintenance for Product (1RM) (1RM_S4CLD2608_BPD_EN_XX)]] | SAP S/4HANA Cloud Public Edition 2608 test script for scope item 1RM: mass load, mass maintenance, export and remediation of Product master data via Fiori apps. |

### Product Master: Non-Stock Materials and Service Products

How to create NLAG non-stock material and SERV service product masters (basic, sales/tax, purchasing, accounting) via MM01 or F1602.

| Node | Description |
| --- | --- |
| [[02-business-partner-and-product-master-data/stammdatenskript-produktstamm-vom-typ-serviceprodukt-anlegen-sds-31x-3\|Stammdatenskript: Produktstamm vom Typ „Serviceprodukt“ anlegen – SDS (31X) (31X_S4CLD2608_Master_Data_DE_XX)]] | German SAP S/4HANA Cloud Public Edition master data script (31X): create a service product master (basic, sales/tax, purchasing, accounting data) via MM01 or F1602. |
| [[02-business-partner-and-product-master-data/master-data-script-create-product-master-of-type-service-product-mds-3\|Master Data Script: Create Product Master of type "Service Product" - MDS (31X) (31X_S4CLD2608_Master_Data_EN_XX)]] | SAP S/4HANA Cloud Public Edition 2608 master data script (31X) for creating a Service Product master: basic, sales, purchasing and accounting data via MM01 or F1602. |
| [[02-business-partner-and-product-master-data/script-de-datos-maestros-crear-maestro-de-productos-de-tipo-producto-d\|Script de datos maestros - Crear maestro de productos de tipo "Producto de servicio" - MDS (31X) (31X_S4CLD2608_Master_Data_ES_XX)]] | SAP S/4HANA Cloud Public Edition 2608 master data script (31X, Spanish): creating a service product master via MM01 or F1602 across basic, sales, purchasing, accounting views. |
| [[02-business-partner-and-product-master-data/mds-31x-307\|マスタデータスクリプト: タイプ "サービス製品" の製品マスタの登録 - MDS (31X) (31X_S4CLD2608_Master_Data_JA_XX)]] | Japanese master data script 31X for SAP S/4HANA Cloud Public Edition: creating service-product material masters (basic, sales, purchasing, accounting) via MM01 or F1602. |
| [[02-business-partner-and-product-master-data/script-de-dados-mestre-criar-mestre-de-produtos-do-tipo-produto-de-ser\|Script de dados mestre - Criar mestre de produtos do tipo Produto de serviço (31X) (31X_S4CLD2608_Master_Data_PT_XX)]] | SAP S/4HANA Cloud Public Edition 2608 master data script (PT, 31X): create service product master via MM01 or F1602 across basic, sales, purchasing, accounting views. |
| [[02-business-partner-and-product-master-data/mds-31x-309\|创建“服务产品”类型的产品主数据 - MDS (31X) (31X_S4CLD2608_Master_Data_ZH_XX)]] | Chinese (machine-translated) SAP S/4HANA Cloud 2608 master data script 31X: create service-product (SERV) material master via MM01 or F1602, with test steps. |
| [[02-business-partner-and-product-master-data/stammdatenskript-produktstamm-fur-materialart-nichtlagermaterial-anleg\|Stammdatenskript: Produktstamm für Materialart "Nichtlagermaterial" anlegen – MDS (31Y) (31Y_S4CLD2608_Master_Data_DE_XX)]] | German SAP S/4HANA Cloud Public Edition 2608 master data script (31Y): creating a non-stock material (NLAG) via MM01 or F1602, covering basic, sales, purchasing and accounting data. |
| [[02-business-partner-and-product-master-data/master-data-script-create-product-master-of-type-non-stock-material-md\|Master Data Script: Create Product Master of type "Non-Stock Material" - MDS (31Y) (31Y_S4CLD2608_Master_Data_EN_XX)]] | SAP S/4HANA Cloud Public Edition 2608 master data script (31Y) for creating a non-stock material (NLAG) product master: basic, sales, purchasing, accounting data. |
| [[02-business-partner-and-product-master-data/script-de-datos-maestros-creacion-de-maestro-de-productos-de-tipo-mate\|Script de datos maestros: Creación de maestro de productos de tipo "Material no de almacén" - MDS (31Y) (31Y_S4CLD2608_Master_Data_ES_XX)]] | Spanish SAP S/4HANA Cloud Public Edition 2608 master data script (31Y): test steps to create a non-stock material via MM01 or F1602 (basic, sales, purchasing, accounting). |
| [[02-business-partner-and-product-master-data/mds-31y-313\|タイプ "非在庫品目" の製品マスタの登録 - MDS (31Y) (31Y_S4CLD2608_Master_Data_JA_XX)]] | Japanese master data script 31Y for SAP S/4HANA Cloud 2608: creating non-stock (NLAG) product master data - basic, sales, purchasing and accounting views via MM01 or F1602. |
| [[02-business-partner-and-product-master-data/script-de-dados-mestre-criar-mestre-de-produtos-do-tipo-material-nao-e\|Script de dados mestre: Criar mestre de produtos do tipo "Material não estocável" – MDS (31Y) (31Y_S4CLD2608_Master_Data_PT_XX)]] | SAP S/4HANA Cloud Public Edition master data script (PT, 31Y): creating non-stock material product masters via MM01 or F1602 across basic, sales, purchasing, accounting views. |
| [[02-business-partner-and-product-master-data/master-data-script-creating-non-stock-material-product-master-data-31y\|Master Data Script: Creating Non-Stock Material Product Master Data (31Y) [ZH] (31Y_S4CLD2608_Master_Data_ZH_XX)]] | Chinese machine-translated SAP S/4HANA Cloud master data script 31Y for creating non-stock material (NLAG) product master data via MM01 or F1602. |

### Product Master: Packaging and Returnable Packaging

How to create VERP packaging and LEIH returnable packaging product masters, including warehouse-management views for EWM packing.

| Node | Description |
| --- | --- |
| [[02-business-partner-and-product-master-data/stammdatenskript-produktstamm-vom-typ-verpackung-anlegen-sds-3y1-388\|Stammdatenskript: Produktstamm vom Typ "Verpackung" anlegen – SDS (3Y1) (3Y1_S4CLD2608_Master_Data_DE_XX)]] | German SAP S/4HANA Cloud Public Edition master data script (3Y1) for creating packaging-type product masters: basic, sales and WM views via MM01/MM02/F1602. |
| [[02-business-partner-and-product-master-data/create-product-master-of-type-packaging-mds-3y1-389\|Create Product Master of Type "Packaging" - MDS (3Y1) (3Y1_S4CLD2608_Master_Data_EN_XX)]] | Master data script (3Y1) for SAP S/4HANA Cloud Public Edition: create packaging material/product master (basic, sales, WM views) for Warehouse Management scope items. |
| [[02-business-partner-and-product-master-data/script-de-datos-maestros-creacion-de-maestro-de-productos-de-tipo-emba\|Script de datos maestros - Creación de maestro de productos de tipo "Embalaje" - MDS (3Y1) (3Y1_S4CLD2608_Master_Data_ES_XX)]] | SAP S/4HANA Cloud Public Edition master data script (3Y1, Spanish) for creating a packaging material master: basic, sales and WM views via MM01/MM02/F1602. |
| [[02-business-partner-and-product-master-data/mds-3y1-391\|目的 (マスタデータスクリプト: タイプ "梱包材" の製品マスタの登録 - MDS 3Y1) (3Y1_S4CLD2608_Master_Data_JA_XX)]] | Japanese master data script (3Y1) for creating packaging-material product masters (basic, sales, warehouse views) in SAP S/4HANA Cloud Public Edition 2608. |
| [[02-business-partner-and-product-master-data/criar-mestre-de-produtos-do-tipo-embalagem-mds-3y1-392\|Criar mestre de produtos do tipo "Embalagem" – MDS (3Y1) (3Y1_S4CLD2608_Master_Data_PT_XX)]] | Portuguese SAP S/4HANA Cloud 2608 master data script (3Y1): create packaging-type product master in Basic, SD and WM views via MM01/MM02/F1602. |
| [[02-business-partner-and-product-master-data/mds-3y1-393\|创建“包装”类型的产品主数据 - MDS (3Y1) (3Y1_S4CLD2608_Master_Data_ZH_XX)]] | Chinese (machine-translated) SAP master data script 3Y1 for creating packaging-type product master data (basic, sales, warehouse management views). |
| [[02-business-partner-and-product-master-data/stammdatenskript-produktstamm-vom-typ-leihgut-anlegen-sds-65b-496\|Stammdatenskript: Produktstamm vom Typ "Leihgut" anlegen – SDS (65B) (65B_S4CLD2608_Master_Data_DE_XX)]] | German master data script (SAP S/4HANA Cloud Public Edition 2608) for creating a product master of type Leihgut (loaned item, LEIH) via MM01 or F1602, across five data segments. |
| [[02-business-partner-and-product-master-data/master-data-script-create-product-master-of-type-returnable-packaging\|Master Data Script: Create Product Master of type "Returnable Packaging" - MDS (65B) (65B_S4CLD2608_Master_Data_EN_XX)]] | SAP S/4HANA Cloud Public Edition 2608 test script for creating a Returnable Packaging (LEIH) product master via MM01 or F1602, across basic, sales, MRP, storage and accounting data. |
| [[02-business-partner-and-product-master-data/script-de-datos-maestros-crear-maestro-de-productos-de-tipo-embalaje-e\|Script de datos maestros: Crear maestro de productos de tipo "Embalaje en préstamo" - MDS (65B) (65B_S4CLD2608_Master_Data_ES_XX)]] | Spanish SAP S/4HANA Cloud Public Edition 2608 master data script (65B): test steps to create a returnable packaging (LEIH) product master via MM01 or F1602. |
| [[02-business-partner-and-product-master-data/mds-65b-499\|マスタデータスクリプト: タイプ "要返却梱包材" の製品マスタの登録 - MDS (65B) (65B_S4CLD2608_Master_Data_JA_XX)]] | Japanese SAP S/4HANA Cloud Public Edition master data script (65B, 02-07-26) for creating a returnable packaging (LEIH) product master across five data views. |
| [[02-business-partner-and-product-master-data/script-de-dados-mestre-criar-mestre-de-produtos-do-tipo-embalagem-reto\|Script de dados mestre - Criar mestre de produtos do tipo "Embalagem retornável" (MDS 65B) (65B_S4CLD2608_Master_Data_PT_XX)]] | Portuguese SAP S/4HANA Cloud Public Edition 2608 master data script (65B): test procedures to create a returnable-packaging (LEIH) product master via MM01 or F1602. |
| [[02-business-partner-and-product-master-data/mds-65b-501\|主数据脚本 - 创建“可回收包装”类型的产品主数据 - MDS (65B) (65B_S4CLD2608_Master_Data_ZH_XX)]] | Chinese (machine-translated) SAP S/4HANA Cloud Public Edition 2608 master data test script 65B: create returnable-packaging (LEIH) product master via MM01 or F1602. |

### Product Master: Raw Materials, Semi-Finished and Finished Goods

How to create ROH, HALB and FERT product masters view by view (basic, purchasing, MRP, work scheduling, accounting, costing) via MM01 or F1602.

| Node | Description |
| --- | --- |
| [[02-business-partner-and-product-master-data/stammdatenskript-produktstamm-vom-typ-rohstoff-anlegen-sds-bnr-658\|Stammdatenskript: Produktstamm vom Typ „Rohstoff“ anlegen – SDS (BNR) (BNR_S4CLD2608_Master_Data_DE_XX)]] | German SAP S/4HANA Cloud Public Edition 2608 master data test script for creating a raw material (ROH) product master via MM01 or F1602, step by step. |
| [[02-business-partner-and-product-master-data/master-data-script-create-product-master-of-type-raw-material-mds-bnr\|Master Data Script: Create Product Master of type "Raw Material" - MDS (BNR) (BNR_S4CLD2608_Master_Data_EN_XX)]] | SAP S/4HANA Cloud Public Edition 2608 test script for creating a Raw Material (ROH) product master across views, via Create Material (MM01) or Manage Product Master Data (F1602). |
| [[02-business-partner-and-product-master-data/script-de-datos-maestros-creacion-de-maestro-de-productos-de-tipo-mate-2\|Script de datos maestros - Creación de maestro de productos de tipo "Materia prima" (BNR) (BNR_S4CLD2608_Master_Data_ES_XX)]] | Spanish machine-translated SAP S/4HANA Cloud Public 2608 master data test script (BNR) for creating raw-material (ROH) product masters via MM01 or F1602. |
| [[02-business-partner-and-product-master-data/sap-s-4hana-cloud-public-edition-mds-bnr-661\|マスタデータスクリプト SAP S/4HANA Cloud Public Edition - "原材料" タイプの製品マスタの登録 (MDS BNR) (BNR_S4CLD2608_Master_Data_JA_XX)]] | Japanese master data script for S/4HANA Cloud Public Edition 2608: test steps to create ROH (raw material) product masters via MM01 or Manage Product Master Data (F1602). |
| [[02-business-partner-and-product-master-data/script-de-dados-mestre-criar-mestre-de-produtos-do-tipo-materia-prima\|Script de dados mestre - Criar mestre de produtos do tipo "Matéria-prima" – MDS (BNR) (BNR_S4CLD2608_Master_Data_PT_XX)]] | Portuguese (Brazil) SAP S/4HANA Cloud Public Edition test script for creating raw-material (ROH) product master data via MM01 and F1602, by data view. |
| [[02-business-partner-and-product-master-data/sap-s-4hana-cloud-public-edition-mds-bnr-663\|主数据脚本 SAP S/4HANA Cloud Public Edition - 创建“原材料”类型的产品主数据 (MDS BNR) (BNR_S4CLD2608_Master_Data_ZH_XX)]] | Chinese (machine-translated) master data script for SAP S/4HANA Cloud Public Edition 2608: creating raw material (ROH) product master data via MM01 or F1602, dated 02-07-26. |
| [[02-business-partner-and-product-master-data/stammdatenskript-produktstamm-vom-typ-halbfabrikat-anlegen-sds-bns-664\|Stammdatenskript: Produktstamm vom Typ „Halbfabrikat“ anlegen – SDS (BNS) (BNS_S4CLD2608_Master_Data_DE_XX)]] | German SAP S/4HANA Cloud Public Edition 2608 master data test script (BNS) for creating a semi-finished (HALB) product master via MM01 or F1602, by data view. |
| [[02-business-partner-and-product-master-data/master-data-script-create-product-master-of-type-semi-finished-good-md\|Master Data Script: Create Product Master of type "Semi-Finished Good" - MDS (BNS) (BNS_S4CLD2608_Master_Data_EN_XX)]] | SAP S/4HANA Cloud Public Edition 2608 test script for creating a HALB semi-finished product master via MM01 or F1602, by data view, with prerequisites. |
| [[02-business-partner-and-product-master-data/script-de-datos-maestros-creacion-de-maestro-de-productos-de-tipo-prod\|Script de datos maestros - Creación de maestro de productos de tipo "Producto semielaborado" (MDS BNS) (BNS_S4CLD2608_Master_Data_ES_XX)]] | SAP S/4HANA Cloud Public Edition 2608 master data script (Spanish, machine-translated): test steps to create a HALB semi-finished product master via MM01 or F1602. |
| [[02-business-partner-and-product-master-data/mds-bns-sap-s-4hana-cloud-public-edition-2608-japanese-667\|マスタデータスクリプト - "半製品" タイプの製品マスタの登録 (MDS BNS, SAP S/4HANA Cloud Public Edition 2608, Japanese) (BNS_S4CLD2608_Master_Data_JA_XX)]] | Japanese master data script for SAP S/4HANA Cloud Public Edition 2608: test steps to create a semifinished (HALB) product master via MM01 or F1602, per data view. |
| [[02-business-partner-and-product-master-data/script-de-dados-mestre-criar-mestre-de-produtos-do-tipo-produto-semiac\|Script de dados mestre - Criar mestre de produtos do tipo "Produto semiacabado" – MDS (BNS) (BNS_S4CLD2608_Master_Data_PT_XX)]] | Portuguese SAP S/4HANA Cloud Public Edition 2608 master data script: test steps to create semi-finished (HALB) product masters via MM01 or F1602. |
| [[02-business-partner-and-product-master-data/mds-bns-669\|主数据脚本 - 创建“半成品”类型的产品主数据 - MDS (BNS) (BNS_S4CLD2608_Master_Data_ZH_XX)]] | Chinese (machine-translated) SAP S/4HANA Cloud 2608 master data script BNS: creating semi-finished (HALB) product master via MM01 or F1602, by data view. |
| [[02-business-partner-and-product-master-data/stammdatenskript-sap-s-4hana-cloud-public-edition-produktstamm-vom-typ\|Stammdatenskript SAP S/4HANA Cloud Public Edition – Produktstamm vom Typ „Fertigerzeugnis“ anlegen – SDS (BNT) (BNT_S4CLD2608_Master_Data_DE_XX)]] | German master data test script (SAP S/4HANA Cloud Public Edition 2608) for creating a finished-product (FERT) material master via MM01 or F1602, step by step per data view. |
| [[02-business-partner-and-product-master-data/master-data-script-create-product-master-of-type-finished-good-sap-s-4\|Master Data Script - Create Product Master of type "Finished Good" (SAP S/4HANA Cloud Public Edition) (BNT_S4CLD2608_Master_Data_EN_XX)]] | SAP S/4HANA Cloud Public Edition 2608 test script for creating a Finished Good (FERT) product master via MM01 or Manage Product Master Data (F1602), by data segment. |
| [[02-business-partner-and-product-master-data/script-de-datos-maestros-creacion-de-maestro-de-productos-de-tipo-prod-2\|Script de datos maestros - Creación de maestro de productos de tipo "Producto terminado" (MDS BNT) (BNT_S4CLD2608_Master_Data_ES_XX)]] | Spanish (machine-translated) SAP S/4HANA Cloud Public Edition 2608 test script for creating finished-product (FERT) material master data via MM01 or F1602. |
| [[02-business-partner-and-product-master-data/sap-s-4hana-cloud-public-edition-mds-bnt-673\|マスタデータスクリプト SAP S/4HANA Cloud Public Edition - "最終製品" タイプの製品マスタの登録 (MDS BNT) (BNT_S4CLD2608_Master_Data_JA_XX)]] | Japanese SAP S/4HANA Cloud Public Edition 2608 master data script: test steps to create finished-product (FERT) material masters via MM01 or Product Master F1602. |
| [[02-business-partner-and-product-master-data/script-de-dados-mestre-criar-mestre-de-produtos-do-tipo-produto-acabad\|Script de dados mestre - Criar mestre de produtos do tipo "Produto acabado" (MDS BNT) (BNT_S4CLD2608_Master_Data_PT_XX)]] | Portuguese SAP S/4HANA Cloud Public Edition master data test script for creating finished-product (FERT) material masters via MM01 and F1602, dated 02-07-26. |
| [[02-business-partner-and-product-master-data/sap-s-4hana-cloud-public-edition-bnt-675\|主数据脚本 SAP S/4HANA Cloud Public Edition - 创建“成品”类型的产品主数据 (BNT) (BNT_S4CLD2608_Master_Data_ZH_XX)]] | Chinese (machine-translated) SAP S/4HANA Cloud 2608 master data script BNT: step-by-step creation of finished-goods (FERT) product master via MM01 or F1602. |

### Product Master: Spare Parts

How to create an ERSA spare parts material master across basic, purchasing, MRP, storage and accounting views, with optional document link.

| Node | Description |
| --- | --- |
| [[02-business-partner-and-product-master-data/stammdatenskript-produktstamm-vom-typ-ersatzteile-anlegen-sds-2j7-262\|Stammdatenskript: Produktstamm vom Typ „Ersatzteile“ anlegen – SDS (2J7) (2J7_S4CLD2608_Master_Data_DE_XX)]] | German SAP S/4HANA Cloud Public Edition 2608 master data script (2J7): test steps to create a spare-parts (ERSA) material master via MM01, plus optional document linking. |
| [[02-business-partner-and-product-master-data/master-data-script-create-product-master-of-type-spare-parts-mds-2j7-2\|Master Data Script: Create Product Master of type Spare Parts - MDS (2J7) (2J7_S4CLD2608_Master_Data_EN_XX)]] | SAP master data script (2J7) for creating a Spare Parts (ERSA) material master across basic, purchasing, MRP, storage, accounting views, plus optional document linking. |
| [[02-business-partner-and-product-master-data/script-de-datos-maestros-creacion-de-maestro-de-productos-de-tipo-piez\|Script de datos maestros - Creación de maestro de productos de tipo "Piezas de recambio" (MDS 2J7) (2J7_S4CLD2608_Master_Data_ES_XX)]] | Spanish SAP S/4HANA Cloud Public Edition 2608 master data script (2J7): test steps to create a spare parts (ERSA) material master via MM01, with optional document link. |
| [[02-business-partner-and-product-master-data/mds-2j7-265\|マスタデータスクリプト - "予備部品" タイプの製品マスタの登録 – MDS (2J7) (2J7_S4CLD2608_Master_Data_JA_XX)]] | Japanese SAP S/4HANA Cloud Public Edition 2608 master data test script 2J7: create spare-parts (ERSA) material master via MM01, plus optional document creation and linking. |
| [[02-business-partner-and-product-master-data/script-de-dados-mestre-criar-mestre-de-produtos-do-tipo-pecas-de-repos\|Script de dados mestre - Criar mestre de produtos do tipo "Peças de reposição" – MDS (2J7) (2J7_S4CLD2608_Master_Data_PT_XX)]] | SAP S/4HANA Cloud Public Edition 2608 master data script (PT): create spare-parts (ERSA) material master via MM01, with optional document link via F2733/MM02. |
| [[02-business-partner-and-product-master-data/mds-2j7-267\|创建“备件”类型的产品主数据 - MDS (2J7) (2J7_S4CLD2608_Master_Data_ZH_XX)]] | Chinese (machine-translated) SAP S/4HANA Cloud 2608 master data script 2J7: create spare-part (ERSA) material master via MM01, plus optional document link. |

### Product Master: Trading Goods

How to create a trading goods (HAWA) product master by data view via MM01 or F1602, including sales, purchasing and accounting data.

| Node | Description |
| --- | --- |
| [[02-business-partner-and-product-master-data/stammdatenskript-produktstamm-vom-typ-handelsware-anlegen-sds-bnf-592\|Stammdatenskript: Produktstamm vom Typ „Handelsware“ anlegen – SDS (BNF) (BNF_S4CLD2608_Master_Data_DE_XX)]] | German SAP S/4HANA Cloud Public Edition 2608 master data test script for creating a trading goods (Handelsware) product master via MM01 or F1602, by data view. |
| [[02-business-partner-and-product-master-data/master-data-script-create-product-master-of-type-trading-good-mds-bnf\|Master Data Script: Create Product Master of type "Trading Good" - MDS (BNF), SAP S/4HANA Cloud Public Edition (BNF_S4CLD2608_Master_Data_EN_XX)]] | SAP S/4HANA Cloud Public Edition 2608 test script for creating Trading Goods product master data per view, via Create Material (MM01) or Manage Product Master Data (F1602). |
| [[02-business-partner-and-product-master-data/script-de-datos-maestros-crear-maestro-de-productos-de-tipo-mercaderia\|Script de datos maestros - Crear maestro de productos de tipo "Mercadería" (BNF) (BNF_S4CLD2608_Master_Data_ES_XX)]] | Spanish (machine-translated) SAP S/4HANA Cloud Public Edition 2608 test script for creating a Merchandise product master via MM01 or F1602, by data view. |
| [[02-business-partner-and-product-master-data/sap-s-4hana-cloud-public-edition-bnf-595\|マスタデータスクリプト SAP S/4HANA Cloud Public Edition - "商品" タイプの製品マスタの登録 (BNF) (BNF_S4CLD2608_Master_Data_JA_XX)]] | Japanese master data script (BNF) for SAP S/4HANA Cloud Public Edition 2608: test steps to create 'trading goods' product masters via MM01 and F1602 apps. |
| [[02-business-partner-and-product-master-data/script-de-dados-mestre-criar-mestre-de-produtos-do-tipo-produto-comerc\|Script de dados mestre - Criar mestre de produtos do tipo "Produto comercializável" – MDS (BNF) (BNF_S4CLD2608_Master_Data_PT_XX)]] | SAP S/4HANA Cloud Public Edition 2608 test script (PT) for creating tradable-goods product master data via MM01 or F1602, by view; Brazil (BNF) variant. |
| [[02-business-partner-and-product-master-data/mds-bnf-597\|主数据脚本: 创建“贸易货物”类型的产品主数据 - MDS (BNF) (BNF_S4CLD2608_Master_Data_ZH_XX)]] | Chinese machine-translated SAP S/4HANA Cloud Public Edition 2608 test script (BNF) for creating trading goods product master data via MM01 and Manage Product Master Data (F1602). |

### Supplier Master Data

How to create supplier business partners with general, company code and purchasing organization data via Maintain Business Partner or F1053A.

| Node | Description |
| --- | --- |
| [[02-business-partner-and-product-master-data/stammdatenskript-sap-s-4hana-cloud-public-edition-lieferantenstamm-anl\|Stammdatenskript SAP S/4HANA Cloud Public Edition - Lieferantenstamm anlegen – SDS (BNE) (BNE_S4CLD2608_Master_Data_DE_XX)]] | German master data script (SAP S/4HANA Cloud Public Edition 2608) with test steps to create supplier master data: general, company code and purchasing org data. |
| [[02-business-partner-and-product-master-data/master-data-script-create-supplier-master-mds-bne-sap-s-4hana-cloud-pu\|Master Data Script: Create Supplier Master - MDS (BNE), SAP S/4HANA Cloud Public Edition (BNE_S4CLD2608_Master_Data_EN_XX)]] | SAP S/4HANA Cloud Public Edition 2608 test script for creating supplier master data (general, company code, purchasing org) via Maintain Business Partner or F1053A. |
| [[02-business-partner-and-product-master-data/script-de-datos-maestros-creacion-de-maestro-de-proveedores-bne-588\|Script de datos maestros - Creación de maestro de proveedores (BNE) (BNE_S4CLD2608_Master_Data_ES_XX)]] | Spanish SAP S/4HANA Cloud Public Edition 2608 master data script: test steps to create a supplier master (general, company code, purchasing org data). |
| [[02-business-partner-and-product-master-data/sap-s-4hana-cloud-public-edition-mds-bne-589\|マスタデータスクリプト SAP S/4HANA Cloud Public Edition - サプライヤマスタの登録 - MDS (BNE) (BNE_S4CLD2608_Master_Data_JA_XX)]] | Japanese SAP S/4HANA Cloud 2608 master data script for creating supplier master records (general, company code, purchasing org data) via BP or F1053A apps. |
| [[02-business-partner-and-product-master-data/script-de-dados-mestre-criar-mestre-de-fornecedores-mds-bne-590\|Script de dados mestre - Criar mestre de fornecedores - MDS (BNE) (BNE_S4CLD2608_Master_Data_PT_XX)]] | Portuguese SAP S/4HANA Cloud Public Edition 2608 master data test script for creating supplier master (general, company code, purchasing org data) via Fiori apps BP and F1053A. |
| [[02-business-partner-and-product-master-data/mds-bne-591\|创建供应商主数据 - MDS (BNE) (BNE_S4CLD2608_Master_Data_ZH_XX)]] | Chinese master data script (BNE) for SAP S/4HANA Cloud Public Edition: creating supplier master data (general, company code, purchasing org) via Maintain Business Partner or F1053A. |

### Configurable Materials and Characteristic Display

How to create KMAT configurable material masters and the application groups and characteristic displays used in variant configuration.

| Node | Description |
| --- | --- |
| [[02-business-partner-and-product-master-data/anwendungsgruppe-und-merkmalsanzeige-anlegen-sds-2ni-268\|Anwendungsgruppe und Merkmalsanzeige anlegen – SDS (2NI) (2NI_S4CLD2608_Master_Data_DE_XX)]] | German master data script (2NI) for SAP S/4HANA Cloud Public Edition: creating an application group and a characteristic display with characteristic assignment (CU_CHAR_DISPLAY). |
| [[02-business-partner-and-product-master-data/create-application-group-and-characteristic-display-mds-2ni-269\|Create Application Group and Characteristic Display - MDS (2NI) (2NI_S4CLD2608_Master_Data_EN_XX)]] | English SAP S/4HANA Cloud master data script (2NI): create an application group and characteristic display for variant configuration via CU_CHAR_DISPLAY. |
| [[02-business-partner-and-product-master-data/crear-grupo-de-aplicaciones-y-visualizacion-de-caracteristicas-mds-2ni\|Crear grupo de aplicaciones y visualización de características - MDS (2NI) (2NI_S4CLD2608_Master_Data_ES_XX)]] | Spanish (machine-translated) master data script 2NI: create an application group and characteristic display with characteristic assignment in SAP S/4HANA Cloud Public Edition. |
| [[02-business-partner-and-product-master-data/mds-2ni-271\|マスタデータスクリプト: アプリケーショングループおよび特性照会の登録 - MDS (2NI) (2NI_S4CLD2608_Master_Data_JA_XX)]] | Japanese master data script (MDS 2NI) for creating application groups and characteristic inquiries (with characteristic assignment) in SAP S/4HANA Cloud Public Edition 2608. |
| [[02-business-partner-and-product-master-data/script-de-dados-mestre-criar-grupo-de-aplicacao-e-exibicao-de-caracter\|Script de dados mestre - Criar grupo de aplicação e exibição de característica – MDS (2NI) (2NI_S4CLD2608_Master_Data_PT_XX)]] | Portuguese master data script (2NI) for creating an application group and characteristic display with characteristic assignment via CU_CHAR_DISPLAY in S/4HANA Cloud Public Edition 2608. |
| [[02-business-partner-and-product-master-data/mds-2ni-273\|创建应用程序组和特征显示 - MDS (2NI) (2NI_S4CLD2608_Master_Data_ZH_XX)]] | 主数据脚本（中文机器翻译）：用 CU_CHAR_DISPLAY 创建应用程序组和特征显示并分配特征。 |
| [[02-business-partner-and-product-master-data/stammdatenskript-produktstamm-fur-materialart-konfigurierbares-materia\|Stammdatenskript: Produktstamm für Materialart "Konfigurierbares Material" anlegen – MDS (2T7) (2T7_S4CLD2608_Master_Data_DE_XX)]] | German SAP S/4HANA Cloud Public Edition 2608 master data script (2T7): test steps to create a KMAT configurable material master via MM01 or F1602. |
| [[02-business-partner-and-product-master-data/master-data-script-create-product-master-of-type-configurable-material\|Master Data Script: Create Product Master of Type "Configurable Material" - MDS (2T7) (2T7_S4CLD2608_Master_Data_EN_XX)]] | SAP S/4HANA Cloud Public Edition 2608 test script (2T7) for creating a KMAT configurable material master via MM01 or F1602, view by view. |
| [[02-business-partner-and-product-master-data/script-de-datos-maestros-creacion-de-maestro-de-productos-de-tipo-mate-3\|Script de datos maestros: Creación de maestro de productos de tipo "Material configurable" - MDS (2T7) (2T7_S4CLD2608_Master_Data_ES_XX)]] | SAP S/4HANA Cloud Public Edition 2608 master data script (ES, machine-translated) for creating KMAT configurable material masters via MM01 or F1602, scope item 2T7. |
| [[02-business-partner-and-product-master-data/sap-s-4hana-cloud-public-edition-mds-2t7-283\|マスタデータスクリプト SAP S/4HANA Cloud Public Edition - タイプ "選定可能品目" の製品マスタの登録 - MDS (2T7) (2T7_S4CLD2608_Master_Data_JA_XX)]] | Japanese master data script (2T7) for creating a configurable (KMAT) product master in S/4HANA Cloud Public Edition via MM01 or F1602, across all data views. |
| [[02-business-partner-and-product-master-data/script-de-dados-mestre-criar-mestre-de-produtos-do-tipo-material-confi\|Script de dados mestre - Criar mestre de produtos do tipo Material configurável (MDS 2T7) (2T7_S4CLD2608_Master_Data_PT_XX)]] | SAP S/4HANA Cloud Public Edition 2608 master data script (PT) 2T7: test steps to create a KMAT configurable material via MM01 or F1602, across all views. |
| [[02-business-partner-and-product-master-data/mds-2t7-285\|创建“可配置物料”类型的产品主数据 - MDS (2T7) (2T7_S4CLD2608_Master_Data_ZH_XX)]] | SAP S/4HANA Cloud Public Edition 2608 master data script (Chinese, machine-translated): creating KMAT configurable-material product master data via MM01 or F1602. |
| [[02-business-partner-and-product-master-data/set-up-configurable-model-using-variant-configuration-22t-ae-test-scri\|Set Up Configurable Model Using Variant Configuration (22T_AE) - Test Script, SAP S/4HANA Cloud Public Edition 2608 (22T_S4CLD2608_BPD_EN_AE)]] | SAP S/4HANA Cloud Public Edition 2608 (AE) test script for scope item 22T: model, simulate and replicate a configurable forklift using variant configuration. |

### Central Governance for Products and Business Partners

How governance processes create, change, mass-process and approve product and business partner master data centrally, including inbound replication.

| Node | Description |
| --- | --- |
| [[02-business-partner-and-product-master-data/test-script-central-governance-for-product-1n5-sap-s-4hana-cloud-publi\|Test Script: Central Governance for Product (1N5) - SAP S/4HANA Cloud Public Edition (1N5_S4CLD2608_BPD_EN_XX)]] | SAP S/4HANA Cloud Public Edition 2608 test script for scope item 1N5: product master data mass processing and central governance create/change/approve flows. |
| [[02-business-partner-and-product-master-data/test-script-central-governance-for-business-partner-1n7-sap-s-4hana-cl\|Test Script: Central Governance for Business Partner (1N7) - SAP S/4HANA Cloud Public Edition (1N7_S4CLD2608_BPD_EN_XX)]] | SAP test script for scope item 1N7: mass and single-record business partner governance, approval workflow and inbound replication in S/4HANA Cloud. |

### Mass Load and Mass Maintenance for Business Partners

How business partners and BP relationships are mass loaded, mass changed, exported, tracked and remediated with validation and activation steps.

| Node | Description |
| --- | --- |
| [[02-business-partner-and-product-master-data/mass-load-and-mass-maintenance-for-business-partners-7mi-test-script-1\|Mass Load and Mass Maintenance for Business Partners (7MI) - Test Script (7MI_S4CLD2608_BPD_EN_XX)]] | SAP S/4HANA Cloud Public Edition test script, scope item 7MI: business partner mass load, relationship load, mass maintenance, export, tracking, remediation. |
| [[02-business-partner-and-product-master-data/test-script-mass-load-and-mass-maintenance-for-business-partner-1rk-75\|Test Script: Mass Load and Mass Maintenance for Business Partner (1RK) (1RK_S4CLD2608_BPD_EN_XX)]] | SAP S/4HANA Cloud 1RK test script: Fiori test steps for business partner mass load, BP relationship load, mass maintenance, export and remediation. |

### Best Practice Master Data Overview and Naming Conventions

Which material master records the best-practice content delivers per scope item, and which ID naming conventions and material type (MTART) abbreviations it uses.

| Node | Description |
| --- | --- |
| [[02-business-partner-and-product-master-data/2608-master-data-overview-en-xx-120-part-01\|2608 Master Data Overview EN XX (2608_Master_Data_Overview_EN_XX) — part 1 of 4]] | SAP S/4HANA Cloud Public Edition 2608 master data overview: ID naming conventions, MTART abbreviations and the material master record catalogue by scope item. |
| [[02-business-partner-and-product-master-data/2608-master-data-overview-en-xx-120-part-02\|2608 Master Data Overview EN XX (2608_Master_Data_Overview_EN_XX) — part 2 of 4]] | SAP S/4HANA Cloud Public Edition 2608 sample master data catalogue (materials, partners, work centers, retail) mapped to scope items and building blocks. |
| [[02-business-partner-and-product-master-data/2608-master-data-overview-en-xx-120-part-03\|2608 Master Data Overview EN XX (2608_Master_Data_Overview_EN_XX) — part 3 of 4]] | SAP S/4HANA Cloud 2608 master data overview workbook: sample materials, supplier and customer business partners, each mapped to scope items and building blocks. |
| [[02-business-partner-and-product-master-data/2608-master-data-overview-en-xx-120-part-04\|2608 Master Data Overview EN XX (2608_Master_Data_Overview_EN_XX) — part 4 of 4]] | SAP S/4HANA Cloud 2608 master data workbook (final part): BP customers/contacts, work centers, retail articles, suppliers, merchandise categories, customers. |

## Related categories
- related-to :: [[08-sales-order-management/_cluster]]
- related-to :: [[10-procurement/_cluster]]
- related-to :: [[12-production-and-manufacturing/_cluster]]
