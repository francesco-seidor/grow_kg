---
title: "Quality, EHS and Compliance"
description: "Quality planning, inspections and notifications, EHS locations, waste, audits and permits, dangerous goods, safety data sheets, product footprints, customs (GTS), embargo and sanctioned-party checks."
cluster: 13-quality-ehs-and-compliance
type: cluster
tags: [kb/quality-ehs-and-compliance, kb/hub]
keywords: [quality management, inspection plan, quality notification, EHS, permit to work, dangerous goods, safety data sheet, carbon footprint, GTS, customs, embargo, sanctioned party]
node_count: 80
created: 2026-10-12
updated: 2026-10-12
---

# Quality, EHS and Compliance

Covers QM, EHS, product compliance and trade compliance checks that block documents. Excludes EWM internal inspections (see 11), ESG consolidation (see 07), VAT (see 04) and freight (see 11).

Every node below is the verbatim text of one source document (or one part of a long one), grouped by topic.

## Nodes

### Dangerous Goods Classification and Checks

How products are classified as dangerous goods and how DG checks block sales orders and deliveries.

| Node | Description |
| --- | --- |
| [[13-quality-ehs-and-compliance/assess-dangerous-goods-for-a-product-3fc-ae-test-script-933\|Assess Dangerous Goods for a Product (3FC_AE) - Test Script (3FC_S4CLD2608_BPD_EN_AE)]] | SAP S/4HANA Cloud Public Edition 2608 test script for scope item 3FC: classifying products as dangerous goods or not, and applying regulations to countries. |
| [[13-quality-ehs-and-compliance/test-script-dangerous-goods-in-the-value-chain-3g8-ae-sap-s-4hana-clou\|Test Script: Dangerous Goods in the Value Chain (3G8_AE) - SAP S/4HANA Cloud Public Edition (3G8_S4CLD2608_BPD_EN_AE)]] | SAP S/4HANA Cloud Public Edition test script for scope item 3G8 (AE): dangerous goods transport checks in sales orders and outbound deliveries, with prerequisites and steps. |

### EHS Audits and Inspections

How EHS checklists are built, inspections run and CAPA tasks added to findings.

| Node | Description |
| --- | --- |
| [[13-quality-ehs-and-compliance/test-script-audit-and-inspection-management-for-ehs-7z7-1241\|Test Script: Audit and Inspection Management for EHS (7Z7) (7Z7_S4CLD2608_BPD_EN_XX)]] | SAP S/4HANA Cloud Public Edition test script for scope item 7Z7: create EHS checklists, run inspections, and add CAPA tasks to findings. |

### EHS Locations

How EHS locations are created and placed in the location structure in Manage Locations.

| Node | Description |
| --- | --- |
| [[13-quality-ehs-and-compliance/ehs-lokation-anlegen-sds-3sr-358\|EHS-Lokation anlegen – SDS (3SR) (3SR_S4CLD2608_Master_Data_DE_XX)]] | German SAP S/4HANA Cloud master data script (3SR): create an EHS location in the location structure using Manage Locations (EHFND_UI_LOC_ENTRY). |
| [[13-quality-ehs-and-compliance/create-ehs-location-mds-3sr-359\|Create EHS Location - MDS (3SR) (3SR_S4CLD2608_Master_Data_EN_XX)]] | SAP S/4HANA Cloud Public Edition master data script for creating an EHS Location and assigning it to the location structure in Manage Locations. |
| [[13-quality-ehs-and-compliance/script-de-datos-maestros-crear-ubicacion-ehs-mds-3sr-360\|Script de datos maestros: Crear ubicación EHS - MDS (3SR) (3SR_S4CLD2608_Master_Data_ES_XX)]] | Spanish (machine-translated) master data script 3SR for creating an EHS location and assigning it to the EHS location structure in S/4HANA Cloud Public Edition. |
| [[13-quality-ehs-and-compliance/ehs-mds-3sr-361\|EHS ロケーション登録 - MDS (3SR) (3SR_S4CLD2608_Master_Data_JA_XX)]] | Japanese master data script (MDS 3SR) for creating EHS locations in a location structure via EHFND_UI_LOC_ENTRY in SAP S/4HANA Cloud Public Edition 2608. |
| [[13-quality-ehs-and-compliance/script-de-dados-mestre-criar-local-ehs-mds-3sr-362\|Script de dados mestre: Criar local EHS – MDS (3SR) (3SR_S4CLD2608_Master_Data_PT_XX)]] | Portuguese master data script (3SR) for creating an EHS location in the location structure in SAP S/4HANA Cloud Public Edition via app EHFND_UI_LOC_ENTRY. |
| [[13-quality-ehs-and-compliance/ehs-mds-3sr-363\|创建 EHS 位置 - MDS (3SR) (3SR_S4CLD2608_Master_Data_ZH_XX)]] | Master data script (Chinese, machine-translated) for creating EHS locations and assigning them to the location structure via Manage Locations (EHFND_UI_LOC_ENTR |

### EHS Products and Chemical Compliance Materials for Waste

How EHS products and chemical compliance information materials are created for waste management.

| Node | Description |
| --- | --- |
| [[13-quality-ehs-and-compliance/stammdatenskript-informationsmaterial-fur-chemische-compliance-ehs-anl\|Stammdatenskript: Informationsmaterial für chemische Compliance (EHS) anlegen - SDS (65Z) (65Z_S4CLD2608_Master_Data_DE_XX)]] | German master data script (65Z) for creating a material master for EHS chemical compliance information in SAP S/4HANA Cloud Public Edition 2608 via Fiori app F4864. |
| [[13-quality-ehs-and-compliance/create-an-ehs-chemical-compliance-information-material-mds-65z-503\|Create an EHS Chemical Compliance Information Material - MDS (65Z) (65Z_S4CLD2608_Master_Data_EN_XX)]] | English master data script (MDS 65Z) for creating an EHS Chemical Compliance Information material via Manage Material Data (F4864), for later Waste Management use. |
| [[13-quality-ehs-and-compliance/crear-un-material-de-informacion-de-conformidad-de-producto-quimico-eh\|Crear un material de información de conformidad de producto químico EHS - MDS (65Z) (65Z_S4CLD2608_Master_Data_ES_XX)]] | Spanish (machine-translated) SAP S/4HANA Cloud 2608 master data script 65Z: create an EHS chemical compliance information material in app F4864 for waste management. |
| [[13-quality-ehs-and-compliance/ehs-mds-65z-japanese-505\|EHS 化学物質コンプライアンス情報品目の登録 - MDS (65Z) (Japanese) (65Z_S4CLD2608_Master_Data_JA_XX)]] | Japanese master data script for creating an EHS Chemical Compliance Information (CCI) item in SAP S/4HANA Cloud Public Edition via app F4864. |
| [[13-quality-ehs-and-compliance/criar-um-material-de-informacoes-de-conformidade-quimica-ehs-mds-65z-5\|Criar um material de informações de conformidade química EHS – MDS (65Z) (65Z_S4CLD2608_Master_Data_PT_XX)]] | Portuguese master data script (65Z) for creating an EHS chemical compliance information material via Manage Material Data (F4864) in SAP S/4HANA Cloud Public Ed |
| [[13-quality-ehs-and-compliance/ehs-mds-65z-chinese-507\|创建 EHS 化学品合规性信息材料 - MDS (65Z) (Chinese) (65Z_S4CLD2608_Master_Data_ZH_XX)]] | Chinese machine-translated master data script for creating an EHS Chemical Compliance Information (CCI) material in SAP S/4HANA Cloud Public Edition via app F4864. |
| [[13-quality-ehs-and-compliance/ehs-produkt-anlegen-sds-660-508\|EHS-Produkt anlegen – SDS (660) (660_S4CLD2608_Master_Data_DE_XX)]] | German master data script 660: create an EHS product master record via Manage Product Master Data (F1602) in SAP S/4HANA Cloud Public Edition 2608, for waste management. |
| [[13-quality-ehs-and-compliance/master-data-script-create-an-ehs-product-mds-660-509\|Master Data Script: Create an EHS Product - MDS (660) (660_S4CLD2608_Master_Data_EN_XX)]] | English master data script (660) for creating an EHS product master record for waste management in SAP S/4HANA Cloud Public Edition 2608 via Manage Product Master Data (F1602). |
| [[13-quality-ehs-and-compliance/crear-un-producto-ehs-mds-660-510\|Crear un producto EHS - MDS (660) (660_S4CLD2608_Master_Data_ES_XX)]] | Spanish (machine-translated) SAP S/4HANA Cloud Public Edition 2608 master data script for creating an EHS product in Manage Product Master Data (F1602) for waste management. |
| [[13-quality-ehs-and-compliance/ehs-mds-660-511\|EHS 製品の登録 - MDS (660) (660_S4CLD2608_Master_Data_JA_XX)]] | Japanese master data script 660: register an EHS product master data record, usable later in EHS waste management, with app F1602. |
| [[13-quality-ehs-and-compliance/criar-um-produto-ehs-mds-660-512\|Criar um produto EHS – MDS (660) (660_S4CLD2608_Master_Data_PT_XX)]] | Portuguese master data script 660: create an EHS product master record via Administrar dados mestre do produto (F1602) in SAP S/4HANA Cloud Public Edition 2608. |
| [[13-quality-ehs-and-compliance/ehs-mds-660-chinese-513\|创建 EHS 产品 - MDS (660) (Chinese) (660_S4CLD2608_Master_Data_ZH_XX)]] | Chinese machine-translated master data script for creating an EHS product master record in SAP S/4HANA Cloud Public Edition via app F1602. |

### Embargo Control

How embargo checks block outbound and inbound documents and how blocks are released.

| Node | Description |
| --- | --- |
| [[13-quality-ehs-and-compliance/test-script-embargo-control-1wc-ae-sap-s-4hana-cloud-public-edition-76\|Test Script: Embargo Control (1WC_AE) - SAP S/4HANA Cloud Public Edition (1WC_S4CLD2608_BPD_EN_AE)]] | SAP test script for scope item 1WC Embargo Control (AE, company code 3310): prerequisites, configuration, and outbound/inbound embargo block, release and analysis steps. |

### First Article Inspection

How first article inspection and regular goods receipt inspections with PPAP run for new supplier parts.

| Node | Description |
| --- | --- |
| [[13-quality-ehs-and-compliance/test-script-first-article-inspection-consumer-products-7l4-ae-sap-s-4h\|Test Script: First Article Inspection – Consumer Products (7L4_AE), SAP S/4HANA Cloud Public Edition (7L4_S4CLD2608_BPD_EN_AE)]] | SAP S/4HANA Cloud Public Edition 2608 (AE) test script for scope item 7L4: first article inspection (FAI) and regular goods receipt inspection with PPAP in the quality info record. |

### Customs Management with SAP GTS

How export declarations and import declarations before goods receipt integrate with SAP Global Trade Services.

| Node | Description |
| --- | --- |
| [[13-quality-ehs-and-compliance/customs-management-with-sap-global-trade-services-2u1-ae-test-script-s\|Customs Management with SAP Global Trade Services (2U1_AE) - Test Script, SAP S/4HANA Cloud Public Edition (2U1_S4CLD2608_BPD_EN_AE)]] | Test script for scope item 2U1: integrating SAP S/4HANA Cloud Public Edition with SAP GTS for export management and import declaration before goods receipt. |

### Transfer of Contact Persons and BOMs to SAP GTS

How customer contact persons and BOMs are transferred to SAP Global Trade Services.

| Node | Description |
| --- | --- |
| [[13-quality-ehs-and-compliance/test-script-transfer-of-primary-master-data-for-sap-global-trade-servi\|Test Script: Transfer of Primary Master Data for SAP Global Trade Services (1WA) (1WA_S4CLD2608_BPD_EN_XX)]] | S/4HANA Cloud Public Edition 2608 test script (1WA): transfer supplier, customer and product master data to SAP Global Trade Services via SOAP or RFC. |
| [[13-quality-ehs-and-compliance/transfer-of-contact-person-for-sap-global-trade-services-24f-test-scri\|Transfer of Contact Person for SAP Global Trade Services (24F) - Test Script (24F_S4CLD2608_BPD_EN_XX)]] | SAP S/4HANA Cloud Public Edition 2608 test script for scope item 24F: transferring customer contact persons to SAP Global Trade Services via SOAP or RFC. |
| [[13-quality-ehs-and-compliance/transfer-of-bill-of-materials-for-sap-global-trade-services-24h-ae-805\|Transfer of Bill of Materials for SAP Global Trade Services (24H_AE) (24H_S4CLD2608_BPD_EN_AE)]] | SAP S/4HANA Cloud Public Edition 2608 test script 24H_AE for scheduling BOM transfer to SAP Global Trade Services, plus GTS configuration appendix. |

### Quality Inspection Plans

How inspection plans and prerequisites (catalogs, master inspection characteristics, sampling procedures) are created and managed.

| Node | Description |
| --- | --- |
| [[13-quality-ehs-and-compliance/stammdatenskript-qualitatsprufplan-anlegen-sds-bnq-652\|Stammdatenskript: Qualitätsprüfplan anlegen – SDS (BNQ) (BNQ_S4CLD2608_Master_Data_DE_XX)]] | German SAP S/4HANA Cloud Public Edition 2608 master data script (BNQ): step-by-step creation and maintenance of quality inspection plans and their prerequisite QM master data. |
| [[13-quality-ehs-and-compliance/master-data-script-create-quality-inspection-plan-mds-bnq-653\|Master Data Script: Create Quality Inspection Plan - MDS (BNQ) (BNQ_S4CLD2608_Master_Data_EN_XX)]] | SAP S/4HANA Cloud Public Edition 2608 master data script (BNQ): prerequisites and Fiori test steps to create and manage quality inspection plans and their master data. |
| [[13-quality-ehs-and-compliance/script-de-datos-maestros-creacion-de-plan-de-inspeccion-de-calidad-mds\|Script de datos maestros - Creación de plan de inspección de calidad - MDS (BNQ) (BNQ_S4CLD2608_Master_Data_ES_XX)]] | SAP S/4HANA Cloud Public Edition 2608 master data script (ES, machine-translated) for creating quality inspection plans and prerequisites: catalogs, characteristics, sampling, dynamic modification. |
| [[13-quality-ehs-and-compliance/sap-s-4hana-cloud-public-edition-mds-bnq-655\|マスタデータスクリプト SAP S/4HANA Cloud Public Edition - 品質検査計画の登録 - MDS (BNQ) (BNQ_S4CLD2608_Master_Data_JA_XX)]] | Japanese master data script (BNQ) for SAP S/4HANA Cloud Public Edition 2608: prerequisites and test steps to create and manage quality inspection plans. |
| [[13-quality-ehs-and-compliance/script-de-dados-mestre-criar-plano-de-controle-de-qualidade-mds-bnq-65\|Script de dados mestre - Criar plano de controle de qualidade - MDS (BNQ) (BNQ_S4CLD2608_Master_Data_PT_XX)]] | Portuguese SAP S/4HANA Cloud Public Edition 2608 master data script (BNQ): prerequisites and step-by-step Fiori test procedures to create quality inspection plans. |
| [[13-quality-ehs-and-compliance/sap-s-4hana-cloud-public-edition-mds-bnq-657\|主数据脚本 SAP S/4HANA Cloud Public Edition - 创建质量检验计划 - MDS (BNQ) (BNQ_S4CLD2608_Master_Data_ZH_XX)]] | Chinese (machine-translated) SAP S/4HANA Cloud 2608 master data script BNQ: prerequisites and test steps for creating quality inspection plans and their master data. |

### Quality Management of Internal Problems

How internal quality notifications, root cause analysis and corrective/preventive actions are handled.

| Node | Description |
| --- | --- |
| [[13-quality-ehs-and-compliance/nonconformance-management-2qn-ae-test-script-sap-s-4hana-cloud-public\|Nonconformance Management (2QN_AE) - Test Script, SAP S/4HANA Cloud Public Edition (2QN_S4CLD2608_BPD_EN_AE)]] | S/4HANA Cloud test script for scope item 2QN_AE: record, process (notification/8D), analyze, close defects; manual inspection lots and usage decisions. |
| [[13-quality-ehs-and-compliance/test-script-quality-management-of-internal-problems-2qp-ae-sap-s-4hana\|Test Script: Quality Management of Internal Problems (2QP_AE) - SAP S/4HANA Cloud Public Edition (2QP_S4CLD2608_BPD_EN_AE)]] | SAP S/4HANA Cloud Public Edition test script for scope item 2QP_AE: internal quality notifications, root cause analysis, corrective/preventive actions, closure (QM01/QM02/QM12). |

### Lean Management of Change

How change requests for products, processes and equipment are reviewed, approved, executed and analyzed.

| Node | Description |
| --- | --- |
| [[13-quality-ehs-and-compliance/test-script-lean-management-of-change-process-4yx-sap-s-4hana-cloud-pu\|Test Script: Lean Management of Change Process (4YX) - SAP S/4HANA Cloud Public Edition (4YX_S4CLD2608_BPD_EN_XX)]] | SAP S/4HANA Cloud Public Edition 2608 test script for scope item 4YX, Lean Management of Change: change request lifecycle, analysis apps and change request type configuration. |

### Permit to Work

How work permit templates and work permits are configured and issued.

| Node | Description |
| --- | --- |
| [[13-quality-ehs-and-compliance/test-script-permit-to-work-7z4-ae-sap-s-4hana-cloud-public-edition-123\|Test Script: Permit to Work (7Z4_AE) - SAP S/4HANA Cloud Public Edition (7Z4_S4CLD2608_BPD_EN_AE)]] | SAP test script for scope item 7Z4 (AE) Permit to Work: configuration prerequisites and test steps for work permit templates and work permits, 2608 release. |

### Product Footprints and Carbon Emission Quantities

How product footprints from SAP Sustainability Footprint Management are viewed and CO2e quantities determined in costing runs.

| Node | Description |
| --- | --- |
| [[13-quality-ehs-and-compliance/product-footprint-management-5im-test-script-1104\|Product Footprint Management (5IM) Test Script (5IM_S4CLD2608_BPD_EN_XX)]] | SAP S/4HANA Cloud Public Edition 2608 test script for scope item 5IM: viewing product footprints from SAP Sustainability Footprint Management, incl. purchase requisition CO2e. |
| [[13-quality-ehs-and-compliance/product-related-carbon-emission-quantities-6vn-ae-test-script-1192\|Product-Related Carbon Emission Quantities (6VN_AE) Test Script (6VN_S4CLD2608_BPD_EN_AE)]] | SAP S/4HANA Cloud Public Edition test script for scope item 6VN: determining, displaying and releasing CO2e emission quantities in product costing runs. |

### Quality Management View of the Material Master

How the QM view and inspection types are maintained per plant on a material master.

| Node | Description |
| --- | --- |
| [[13-quality-ehs-and-compliance/stammdatenskript-qualitatsmanagementattribute-fur-material-produktstam\|Stammdatenskript: Qualitätsmanagementattribute für Material-/Produktstamm anlegen – SDS (BNY) (BNY_S4CLD2608_Master_Data_DE_XX)]] | German SAP S/4HANA Cloud 2608 master data script (BNY) for creating quality management view data on a material master via MM01 as product data specialist. |
| [[13-quality-ehs-and-compliance/create-quality-management-attributes-for-material-product-master-mds-b\|Create Quality Management Attributes for Material/Product Master - MDS (BNY) (BNY_S4CLD2608_Master_Data_EN_XX)]] | SAP S/4HANA Cloud Public Edition master data script (BNY) for maintaining the Quality Management view of a material via Create Material (MM01). |
| [[13-quality-ehs-and-compliance/script-de-datos-maestros-crear-atributos-de-gestion-de-calidad-para-ma\|Script de datos maestros: Crear atributos de gestión de calidad para maestro de materiales/productos - MDS (BNY) (BNY_S4CLD2608_Master_Data_ES_XX)]] | Spanish (machine-translated) SAP S/4HANA Cloud master data script BNY: create quality management attributes in the material master via MM01. |
| [[13-quality-ehs-and-compliance/mds-bny-691\|品目/製品マスタの品質管理属性の登録 - MDS (BNY) (BNY_S4CLD2608_Master_Data_JA_XX)]] | マスタデータスクリプト（日本語）：MM01 で品目マスタの品質管理ビュー（検査タイプ等）をプラント別に登録する手順。 |
| [[13-quality-ehs-and-compliance/criar-atributos-de-administracao-de-qualidade-para-mestre-de-materiais\|Criar atributos de administração de qualidade para mestre de materiais/produtos – MDS (BNY) (BNY_S4CLD2608_Master_Data_PT_XX)]] | Portuguese SAP master data script BNY for creating quality management attributes in the material/product master (MM01), with test steps. |
| [[13-quality-ehs-and-compliance/mds-bny-693\|创建物料/产品主数据的质量管理属性 - MDS (BNY) (BNY_S4CLD2608_Master_Data_ZH_XX)]] | Master data script (Chinese, machine-translated) for maintaining Quality Management views of material master data via MM01, incl. inspection type setup. |

### Quality Management in Stock Handling

How stock is posted to quality inspection, usage decisions made and stock moved after inspection.

| Node | Description |
| --- | --- |
| [[13-quality-ehs-and-compliance/quality-management-in-stock-handling-1mr-ae-test-script-739\|Quality Management in Stock Handling (1MR_AE) - Test Script (1MR_S4CLD2608_BPD_EN_AE)]] | SAP S/4HANA Cloud Public Edition 2608 test script for scope item 1MR_AE: posting stock to quality inspection, usage decisions, and storage location changes. |

### Quality Info Records in Procurement

How quality info records, QM control keys and PPAP settings release suppliers for procurement.

| Node | Description |
| --- | --- |
| [[13-quality-ehs-and-compliance/qualitatsinfosatz-anlegen-sds-bf5-550\|Qualitätsinfosatz anlegen – SDS (BF5) (BF5_S4CLD2608_Master_Data_DE_XX)]] | German master data script (BF5) for SAP S/4HANA Cloud Public Edition 2608: creating quality info records, QM control keys and PPAP settings in procurement. |
| [[13-quality-ehs-and-compliance/create-quality-info-record-mds-bf5-551\|Create Quality Info Record - MDS (BF5) (BF5_S4CLD2608_Master_Data_EN_XX)]] | SAP S/4HANA Cloud Public Edition 2608 master data script (BF5): creating quality info records, QM control keys and PPAP settings in procurement. |
| [[13-quality-ehs-and-compliance/crear-registro-info-de-calidad-mds-bf5-552\|Crear registro info de calidad - MDS (BF5) (BF5_S4CLD2608_Master_Data_ES_XX)]] | Spanish master data script (BF5) for SAP S/4HANA Cloud Public Edition: creating quality info records, QM control keys and first-sample (PAPF) options. |
| [[13-quality-ehs-and-compliance/mds-bf5-553\|マスタデータスクリプト: 品質管理情報の登録 - MDS (BF5) (BF5_S4CLD2608_Master_Data_JA_XX)]] | Japanese master data script BF5 for creating quality info records (procurement), QM control key assignment (QI05) and PPAP setup in SAP S/4HANA Cloud Public. |
| [[13-quality-ehs-and-compliance/criar-registro-info-de-qualidade-mds-bf5-554\|Criar registro info de qualidade – MDS (BF5) (BF5_S4CLD2608_Master_Data_PT_XX)]] | Portuguese master data test script (BF5) for creating quality info records, QM control keys and first-sample (PAPP) settings in SAP S/4HANA Cloud Public Edition 2608. |
| [[13-quality-ehs-and-compliance/mds-bf5-555\|创建质量信息记录 - MDS (BF5) (BF5_S4CLD2608_Master_Data_ZH_XX)]] | SAP S/4HANA Cloud 2608 master data script (ZH, machine-translated) for creating quality info records, QM control keys and PPAP setup as quality planner. |

### Restricted Party Screening with SAP Watch List Screening

How business partners, sales and purchasing documents are screened against sanctioned party lists.

| Node | Description |
| --- | --- |
| [[13-quality-ehs-and-compliance/test-script-restricted-party-screening-with-sap-watch-list-screening-1\|Test Script: Restricted Party Screening with SAP Watch List Screening (1WE_AE) (1WE_S4CLD2608_BPD_EN_AE)]] | SAP S/4HANA Cloud Public Edition 2608 test script for scope item 1WE (AE): configuring and testing sanctioned party screening of BPs, sales and purchasing documents via SAP Watch List Screening. |

### Safety Data Sheets in the Value Chain

How missing or outdated safety data sheets block sales orders and outbound deliveries.

| Node | Description |
| --- | --- |
| [[13-quality-ehs-and-compliance/test-script-safety-data-sheets-in-the-value-chain-3vq-ae-974\|Test Script: Safety Data Sheets in the Value Chain (3VQ_AE) (3VQ_S4CLD2608_BPD_EN_AE)]] | SAP S/4HANA Cloud Public Edition test script for scope item 3VQ_AE: safety data sheet checks blocking sales orders and outbound deliveries, UAE (AE) localization. |

### Supplier Compliance in the Value Chain

How purchase orders are blocked by supplier compliance issues and released after resolution.

| Node | Description |
| --- | --- |
| [[13-quality-ehs-and-compliance/test-script-supplier-compliance-in-the-value-chain-5oj-ae-1115\|Test Script: Supplier Compliance in the Value Chain (5OJ_AE) (5OJ_S4CLD2608_BPD_EN_AE)]] | SAP S/4HANA Cloud Public Edition 2608 test script for scope item 5OJ (AE) Supplier Compliance in the Value Chain: purchase order blocking by supplier assessment status. |

### Quality Inspection in Manufacturing

How in-process and goods-receipt inspection lots in discrete and process manufacturing are recorded, monitored with SPC control charts and closed by usage decision.

| Node | Description |
| --- | --- |
| [[13-quality-ehs-and-compliance/test-script-quality-management-in-discrete-manufacturing-consumer-prod\|Test Script: Quality Management in Discrete Manufacturing – Consumer Products (5HK_AE) (5HK_S4CLD2608_BPD_EN_AE)]] | SAP S/4HANA Cloud Public Edition 2608 test script for scope item 5HK_AE: make-to-stock discrete manufacturing of coffee displays with integrated QM, plant 3310. |
| [[13-quality-ehs-and-compliance/test-script-quality-management-in-discrete-and-process-manufacturing-1\|Test Script: Quality Management in Discrete and Process Manufacturing (1E1_AE) (1E1_S4CLD2608_BPD_EN_AE)]] | SAP S/4HANA Cloud Public Edition 2608 test script for scope item 1E1 (AE): QM inspections, SPC control charts and usage decisions in discrete and process manufacturing. |

### Quality Inspection in Procurement and Sales

How goods receipt inspections (sampling schemes, dynamic modification, certificates) and outbound delivery inspections lead to usage decisions on supplier or customer stock.

| Node | Description |
| --- | --- |
| [[13-quality-ehs-and-compliance/quality-management-in-procurement-1fm-ae-test-script-sap-s-4hana-cloud\|Quality Management in Procurement (1FM_AE) - Test Script, SAP S/4HANA Cloud Public Edition (1FM_S4CLD2608_BPD_EN_AE)]] | SAP test script for scope item 1FM_AE (Quality Management in Procurement, UAE, 2608): prerequisites and five inspection test procedures with apps, roles and sample data. |
| [[13-quality-ehs-and-compliance/test-script-quality-management-in-sales-1mp-ae-sap-s-4hana-cloud-publi\|Test Script: Quality Management in Sales (1MP_AE) - SAP S/4HANA Cloud Public Edition (1MP_S4CLD2608_BPD_EN_AE)]] | Test script, SAP S/4HANA Cloud scope item 1MP_AE (UAE): quality inspection in outbound delivery, sales order to usage decision, goods issue or blocked stock. |

### Quality Notifications for Customer and Supplier Complaints

How customer and supplier complaint notifications capture defects, root causes, tasks and corrective and preventive actions through to closure.

| Node | Description |
| --- | --- |
| [[13-quality-ehs-and-compliance/test-script-quality-management-for-complaints-against-suppliers-2f9-ae\|Test Script: Quality Management for Complaints Against Suppliers (2F9_AE) (2F9_S4CLD2608_BPD_EN_AE)]] | SAP S/4HANA Cloud 2608 (AE) test script for scope item 2F9: supplier complaint quality notifications (QM01/QM02/QM12) and optional complaints (F8685). |
| [[13-quality-ehs-and-compliance/quality-management-for-complaints-from-customers-2fa-ae-test-script-sa\|Quality Management for Complaints from Customers (2FA_AE) - Test Script, SAP S/4HANA Cloud Public Edition (2FA_S4CLD2608_BPD_EN_AE)]] | SAP S/4HANA Cloud Public Edition 2608 (AE) test script for scope item 2FA: customer complaint quality notifications, root cause, actions, closure. |

### Quality Management Analytics

Which overview pages and analytical apps show inspection lots, skip rates and quality KPIs to quality engineers and quality technicians.

| Node | Description |
| --- | --- |
| [[13-quality-ehs-and-compliance/test-script-sap-fiori-analytical-apps-for-quality-management-2v0-875\|Test Script: SAP Fiori Analytical Apps for Quality Management (2V0) (2V0_S4CLD2608_BPD_EN_XX)]] | Test script for SAP S/4HANA Cloud scope item 2V0: Quality Engineer/Technician overview pages and Fiori quality analytics apps, with roles and prerequisites. |

### EHS Incident Management

How incidents, near misses and safety observations are reported, investigated and followed up with tasks and OSHA or BG reports.

| Node | Description |
| --- | --- |
| [[13-quality-ehs-and-compliance/test-script-lean-incident-management-reporting-3fp-ae-sap-s-4hana-clou\|Test Script: Lean Incident Management Reporting (3FP_AE) - SAP S/4HANA Cloud Public Edition (3FP_S4CLD2608_BPD_EN_AE)]] | SAP test script (scope item 3FP, release 2608) for incident, near miss and safety observation reporting, investigations, tasks, OSHA/BG reports and workplace safety. |

### Health and Safety Management and Occupational Health

How chemical approvals, risk assessments, job hazard analyses and safety instructions are managed, and how health centers, protocols and appointments run occupational health.

| Node | Description |
| --- | --- |
| [[13-quality-ehs-and-compliance/health-and-safety-management-54a-ae-test-script-sap-s-4hana-cloud-publ\|Health and Safety Management (54A_AE) - Test Script, SAP S/4HANA Cloud Public Edition (54A_S4CLD2608_BPD_EN_AE)]] | SAP test script for scope item 54A_AE Health and Safety Management: roles, sample data, and tests for chemical approvals, risk assessments, safety instructions. |
| [[13-quality-ehs-and-compliance/test-script-occupational-health-for-environment-health-and-safety-7za\|Test Script: Occupational Health for Environment, Health, and Safety (7ZA) - SAP S/4HANA Cloud Public Edition (7ZA_S4CLD2608_BPD_EN_XX)]] | Test script for scope item 7ZA Occupational Health: prerequisite configuration, then health centers, protocols, appointments and health service requests. |

### Environmental Compliance and Emissions Management

How EHS compliance requirements, permits, obligations and deviations are managed, and how GHG emissions are calculated, checked against limits and reported annually.

| Node | Description |
| --- | --- |
| [[13-quality-ehs-and-compliance/test-script-compliance-management-for-environment-health-and-safety-4c\|Test Script: Compliance Management for Environment, Health, and Safety (4C8) - SAP S/4HANA Cloud Public Edition (4C8_S4CLD2608_BPD_EN_XX)]] | SAP S/4HANA Cloud Public Edition 2608 test script for scope item 4C8: EHS compliance management (locations, permits, requirements, tasks, deviations) with step tables. |
| [[13-quality-ehs-and-compliance/test-script-emissions-management-4xd-sap-s-4hana-cloud-public-edition\|Test Script: Emissions Management (4XD) - SAP S/4HANA Cloud Public Edition (4XD_S4CLD2608_BPD_EN_XX)]] | SAP S/4HANA Cloud Public Edition 2608 test script for Emissions Management (4XD): GHG compliance requirement, scenarios, data entry, deviation, annual report. |

### Waste Management

How waste materials, waste locations, disposers and transporters, and waste permits run through the EHS waste management process to transport documents.

| Node | Description |
| --- | --- |
| [[13-quality-ehs-and-compliance/test-script-waste-management-60h-sap-s-4hana-cloud-public-edition-1139\|Test Script: Waste Management (60H) - SAP S/4HANA Cloud Public Edition (60H_S4CLD2608_BPD_EN_XX)]] | SAP S/4HANA Cloud Public Edition 2608 test script for scope item 60H Waste Management: EHS waste process from material data to transport documents. |

### Chemical Compliance and Product Marketability

How raw material and product marketability is assessed from substance data and supplier disclosures, sales orders blocked, and substance volumes tracked.

| Node | Description |
| --- | --- |
| [[13-quality-ehs-and-compliance/substance-volume-tracking-4ol-ae-test-script-sap-s-4hana-cloud-public\|Substance Volume Tracking (4OL_AE) - Test Script, SAP S/4HANA Cloud Public Edition (4OL_S4CLD2608_BPD_EN_AE)]] | SAP S/4HANA Cloud test script for scope item 4OL_AE: prerequisites and test steps for substance volume tracking across purchasing, manufacturing and sales. |
| [[13-quality-ehs-and-compliance/test-script-chemical-compliance-approval-for-purchased-material-and-su\|Test Script: Chemical Compliance Approval for Purchased Material and Supplier (31G_AE) (31G_S4CLD2608_BPD_EN_AE)]] | SAP S/4HANA Cloud Public Edition test script for scope item 31G_AE: assess raw material marketability, approve suppliers, process supplier disclosures. |
| [[13-quality-ehs-and-compliance/test-script-assess-marketability-of-a-product-31h-ae-sap-s-4hana-cloud\|Test Script: Assess Marketability of a Product (31H_AE) - SAP S/4HANA Cloud Public Edition (31H_S4CLD2608_BPD_EN_AE)]] | SAP S/4HANA Cloud Public Edition 2608 (AE) test script for scope item 31H: prerequisites and Fiori app steps to assess product marketability via substance data and supplier disclosures. |
| [[13-quality-ehs-and-compliance/test-script-chemical-compliance-in-the-value-chain-31j-ae-sap-s-4hana\|Test Script: Chemical Compliance in the Value Chain (31J_AE) - SAP S/4HANA Cloud Public Edition 2608 (31J_S4CLD2608_BPD_EN_AE)]] | SAP test script for scope item 31J_AE: compliance marketability checks on sales orders, DG classification, market and customer assessments, with prerequisites. |

### Safety Data Sheet Authoring, Distribution and Labels

How product compliance data produces safety data sheets, how SDSs are uploaded and shipped, regulatory documents requested from providers and compliance labels printed.

| Node | Description |
| --- | --- |
| [[13-quality-ehs-and-compliance/test-script-request-regulatory-documentation-from-service-provider-6av\|Test Script: Request Regulatory Documentation from Service Provider (6AV) - SAP S/4HANA Cloud Public Edition (6AV_S4CLD2608_BPD_EN_XX)]] | SAP test script for scope item 6AV: simulating cooperation with a regulatory documentation service provider via substance and product service requests. |
| [[13-quality-ehs-and-compliance/test-script-label-management-6mt-ae-sap-s-4hana-cloud-public-edition-1\|Test Script: Label Management (6MT_AE) - SAP S/4HANA Cloud Public Edition (6MT_S4CLD2608_BPD_EN_AE)]] | SAP S/4HANA Cloud Public Edition 2608 (AE) test script for scope item 6MT Label Management: prerequisites, print queue setup, generic and delivery label test steps. |
| [[13-quality-ehs-and-compliance/product-compliance-document-authoring-7do-ae-test-script-sap-s-4hana-c\|Product Compliance Document Authoring (7DO_AE) - Test Script, SAP S/4HANA Cloud Public Edition (7DO_S4CLD2608_BPD_EN_AE)]] | SAP S/4HANA Cloud Public Edition test script for scope item 7DO: step-by-step product compliance data entry through to German safety data sheet generation. |
| [[13-quality-ehs-and-compliance/test-script-manage-safety-data-sheets-for-products-3vr-ae-sap-s-4hana\|Test Script: Manage Safety Data Sheets for Products (3VR_AE) - SAP S/4HANA Cloud Public Edition (3VR_S4CLD2608_BPD_EN_AE)]] | S/4HANA Cloud Public Edition 2608 test script for scope item 3VR (AE): prerequisites and steps to upload, contact-set, ship and monitor safety data sheets. |

### Trade Classification and Legal Control

How products are classified with commodity codes, customs tariff numbers and control classes, and how legal control licenses block or allow trade documents.

| Node | Description |
| --- | --- |
| [[13-quality-ehs-and-compliance/test-script-sap-s-4hana-cloud-public-edition-legal-control-1w8-ae-767\|Test Script SAP S/4HANA Cloud Public Edition - Legal Control (1W8_AE) (1W8_S4CLD2608_BPD_EN_AE)]] | Test script for scope item 1W8 Legal Control (UAE, company code 3310): configuration, master data, control classes, licenses, allow/blocklisting rules, inbound and outbound checks. |
| [[13-quality-ehs-and-compliance/classification-for-customs-tariff-number-and-commodity-code-2u3-ae-868\|Classification for Customs Tariff Number and Commodity Code (2U3_AE) (2U3_S4CLD2608_BPD_EN_AE)]] | Test script for SAP S/4HANA Cloud 2608 (AE) scope item 2U3_AE: maintaining and classifying commodity codes and customs tariff numbers, incl. AI options. |

### SAP GTS Compliance and Preference Management Integration

How documents transfer to SAP Global Trade Services for compliance checks and reprocessing, and how preference determination uses long-term vendor declarations.

| Node | Description |
| --- | --- |
| [[13-quality-ehs-and-compliance/test-script-compliance-management-with-sap-global-trade-services-24j-a\|Test Script: Compliance Management with SAP Global Trade Services (24J_AE) (24J_S4CLD2608_BPD_EN_AE)]] | SAP S/4HANA Cloud Public Edition test script for scope item 24J: GTS document transfer settings, test steps for transferred documents and reprocessing, GTS mapping appendix. |
| [[13-quality-ehs-and-compliance/test-script-preference-management-with-sap-global-trade-services-3jx-a\|Test Script: Preference Management with SAP Global Trade Services (3JX_AE) (3JX_S4CLD2608_BPD_EN_AE)]] | Test script for scope item 3JX_AE: SAP GTS Preference Management with S/4HANA Cloud Public Edition, covering LTSD worklists and configurable materials. |

## Related categories
- related-to :: [[11-inventory-warehouse-and-transportation/_cluster]]
- related-to :: [[12-production-and-manufacturing/_cluster]]
