---
title: "Inventory, Warehouse and Transportation"
description: "Goods movements, stock transfers, physical inventory, batches and serial numbers, EWM bins, inbound, outbound, waves and RF, plus freight agreements, carriers and freight settlement."
cluster: 11-inventory-warehouse-and-transportation
type: cluster
tags: [kb/inventory-warehouse-and-transportation, kb/hub]
keywords: [inventory, goods movement, stock transfer, physical inventory, batch, serial number, EWM, storage bin, wave, RF, freight agreement, carrier, transportation management]
node_count: 101
created: 2026-10-12
updated: 2026-10-12
---

# Inventory, Warehouse and Transportation

Covers plant inventory, EWM warehouse execution and transportation management. Excludes retail DC and store logistics (see 15), production supply areas (see 12), quality inspection decisions (see 13) and customs and trade screening (see 13).

Every node below is the verbatim text of one source document (or one part of a long one), grouped by topic.

## Nodes

### Advanced Intercompany Stock Transfer

How intercompany stock transport orders move stock between company codes with deliveries, billing and financial postings.

| Node | Description |
| --- | --- |
| [[11-inventory-warehouse-and-transportation/advanced-intercompany-stock-transfer-5hp-ae-test-script-sap-s-4hana-cl\|Advanced Intercompany Stock Transfer (5HP_AE) - Test Script, SAP S/4HANA Cloud Public Edition (5HP_S4CLD2608_BPD_EN_AE)]] | SAP S/4HANA Cloud Public Edition test script (5HP_AE, 2608) for advanced intercompany stock transfer: roles, master data, steps, apps and financial postings. |
| [[11-inventory-warehouse-and-transportation/test-script-intercompany-stock-transfer-1p9-ae-sap-s-4hana-cloud-publi\|Test Script: Intercompany Stock Transfer (1P9_AE) - SAP S/4HANA Cloud Public Edition (1P9_S4CLD2608_BPD_EN_AE)]] | SAP S/4HANA Cloud Public Edition 2608 (AE) test script for scope item 1P9: domestic and international intercompany stock transfer, from STO to billing and supplier invoice. |

### Batch Management Master Data

How to create batch characteristics, classes, sort sequences, batch search strategies and batch derivation for batch-managed materials.

| Node | Description |
| --- | --- |
| [[11-inventory-warehouse-and-transportation/batch-derivation-consumer-products-77g-ae-1204\|Batch Derivation – Consumer Products (77G_AE) (77G_S4CLD2608_BPD_EN_AE)]] | SAP S/4HANA Cloud Public Edition 2608 test script for scope item 77G_AE: one- and two-level batch derivation in consumer products, with SSCUI setup, MRP, process orders and batch cockpit. |
| [[11-inventory-warehouse-and-transportation/test-script-batch-management-blf-ae-sap-s-4hana-cloud-public-edition-2\|Test Script: Batch Management (BLF_AE) - SAP S/4HANA Cloud Public Edition 2608 (BLF_S4CLD2608_BPD_EN_AE)]] | SAP test script for the Batch Management scope item (UAE localization): prerequisites, sample materials and step-by-step Fiori tests for batch creation, change, search and where-used. |
| [[11-inventory-warehouse-and-transportation/stammdaten-der-chargenverwaltung-anlegen-sds-2zw-298\|Stammdaten der Chargenverwaltung anlegen – SDS (2ZW) (2ZW_S4CLD2608_Master_Data_DE_XX)]] | German SAP S/4HANA Cloud master data script (2ZW): create batch management master data - characteristics, classes, sort orders, search and derivation strategies. |
| [[11-inventory-warehouse-and-transportation/master-data-script-create-batch-management-master-data-mds-2zw-299\|Master Data Script: Create Batch Management Master Data - MDS (2ZW) (2ZW_S4CLD2608_Master_Data_EN_XX)]] | SAP S/4HANA Cloud Public Edition 2608 test script (2ZW) for creating batch management master data: characteristics, classes, sort sequences, search and derivation strategies. |
| [[11-inventory-warehouse-and-transportation/script-de-datos-maestros-crear-datos-maestros-de-gestion-de-lotes-mds\|Script de datos maestros - Crear datos maestros de gestión de lotes - MDS (2ZW) (2ZW_S4CLD2608_Master_Data_ES_XX)]] | Spanish test script (SAP S/4HANA Cloud Public Edition 2608) for creating batch management master data: characteristics, classes, sort sequences, batch search and derivation strategies. |
| [[11-inventory-warehouse-and-transportation/mds-2zw-301\|マスタデータスクリプト: ロット管理マスタデータの登録 - MDS (2ZW) (2ZW_S4CLD2608_Master_Data_JA_XX)]] | Japanese SAP S/4HANA Cloud Public Edition test script (2ZW) for creating batch management master data: characteristics, classes, sort orders, search and inheritance strategy records. |
| [[11-inventory-warehouse-and-transportation/script-de-dados-mestre-criar-dados-mestre-de-administracao-de-lotes-2z\|Script de dados mestre - Criar dados mestre de administração de lotes (2ZW) (2ZW_S4CLD2608_Master_Data_PT_XX)]] | Portuguese SAP S/4HANA Cloud Public Edition 2608 master data script (2ZW): test steps to create batch management master data, search and derivation strategies. |
| [[11-inventory-warehouse-and-transportation/mds-2zw-303\|创建批次管理主数据 - MDS (2ZW) (2ZW_S4CLD2608_Master_Data_ZH_XX)]] | Chinese (machine-translated) SAP S/4HANA Cloud Public 2608 master data script 2ZW: batch management master data (characteristics, classes, sort order, search and derivation strategies). |

### Carrier Business Partners

How carrier and forwarder business partners for road, rail, ocean and air are created.

| Node | Description |
| --- | --- |
| [[11-inventory-warehouse-and-transportation/stammdatenskript-spediteurstamm-anlegen-sds-4de-406\|Stammdatenskript: Spediteurstamm anlegen – SDS (4DE) (4DE_S4CLD2608_Master_Data_DE_XX)]] | German SAP S/4HANA Cloud Public Edition 2608 master data script: creating carrier/forwarder business partners (road, rail, sea, air, forwarder) for invoice verification and ERS. |
| [[11-inventory-warehouse-and-transportation/master-data-script-create-carrier-master-mds-4de-407\|Master Data Script: Create Carrier Master - MDS (4DE) (4DE_S4CLD2608_Master_Data_EN_XX)]] | SAP S/4HANA Cloud Public Edition 2608 master data script (4DE) for creating Business Partner Carriers (road, rail, ocean, forwarder, air) for invoice verification and ERS. |
| [[11-inventory-warehouse-and-transportation/script-de-datos-maestros-creacion-de-maestro-de-transportistas-mds-4de\|Script de datos maestros - Creación de maestro de transportistas - MDS (4DE) (4DE_S4CLD2608_Master_Data_ES_XX)]] | SAP S/4HANA Cloud Public Edition 2608 master data script (Spanish, machine-translated): step-by-step creation of carrier business partners by transport mode for invoice verification and ERS. |
| [[11-inventory-warehouse-and-transportation/mds-4de-master-data-script-create-carrier-master-409\|運送業者マスタの登録 - MDS (4DE) (Master Data Script: Create Carrier Master) (4DE_S4CLD2608_Master_Data_JA_XX)]] | Japanese SAP S/4HANA Cloud Public Edition 2608 master data script for creating carrier business partners (road, rail, ocean, forwarder, air) for invoice verification and ERS. |
| [[11-inventory-warehouse-and-transportation/script-de-dados-mestre-criar-mestre-de-transportadoras-mds-4de-410\|Script de dados mestre - Criar mestre de transportadoras (MDS 4DE) (4DE_S4CLD2608_Master_Data_PT_XX)]] | SAP S/4HANA Cloud Public Edition 2608 master data script (PT): step-by-step creation of carrier/freight agent business partners for road, rail, sea, forwarder and air. |
| [[11-inventory-warehouse-and-transportation/mds-4de-411\|主数据脚本 - 创建承运人主数据 - MDS (4DE) (4DE_S4CLD2608_Master_Data_ZH_XX)]] | Chinese (machine-translated) SAP S/4HANA Cloud 2608 master data script 4DE: creating carrier business partners for road, rail, ocean, forwarder and air, for invoice verification and ERS. |

### Core Inventory Management

How goods receipts, scrapping, transfer postings, reservations and stock analytics are handled in core inventory management.

| Node | Description |
| --- | --- |
| [[11-inventory-warehouse-and-transportation/test-script-sap-s-4hana-cloud-public-edition-core-inventory-management\|Test Script SAP S/4HANA Cloud Public Edition - Core Inventory Management (BMC_AE) (BMC_S4CLD2608_BPD_EN_AE)]] | SAP S/4HANA Cloud Public Edition 2608 (AE) test script for core inventory management: goods receipt, scrapping, stock transfers, stock analytics, reservations. |

### EWM Customer Returns

How customer return deliveries are received and put away in EWM.

| Node | Description |
| --- | --- |
| [[11-inventory-warehouse-and-transportation/sap-ewm-integration-customer-returns-2vo-ae-884\|SAP EWM Integration – Customer Returns (2VO_AE) (2VO_S4CLD2608_BPD_EN_AE)]] | Test script for scope item 2VO_AE: customer return order, return delivery, SAP EWM goods receipt and putaway in SAP S/4HANA Cloud Public Edition 2608. |

### Warehouse Inbound Processing and SAP EWM Inbound Integration

How inbound deliveries reach goods receipt and putaway: warehouse inbound with synchronous GR (5HN) or standard (3BR), and SAP EWM integration from supplier (2VJ) and with batches (2VN).

| Node | Description |
| --- | --- |
| [[11-inventory-warehouse-and-transportation/test-script-warehouse-inbound-processing-with-synchronous-goods-receip\|Test Script: Warehouse Inbound Processing with Synchronous Goods Receipt (5HN_AE) (5HN_S4CLD2608_BPD_EN_AE)]] | SAP S/4HANA Cloud Public Edition 2608 test script (5HN, AE) for synchronous warehouse goods receipt, putaway warehouse tasks and clarification zone handling. |
| [[11-inventory-warehouse-and-transportation/sap-ewm-integration-inbound-processing-from-supplier-2vj-ae-test-scrip\|SAP EWM Integration – Inbound Processing from Supplier (2VJ_AE) – Test Script (2VJ_S4CLD2608_BPD_EN_AE)]] | SAP S/4HANA Cloud Public Edition 2608 test script for scope item 2VJ_AE: PO, expected goods receipt or inbound delivery, goods receipt and putaway in SAP EWM. |
| [[11-inventory-warehouse-and-transportation/test-script-sap-ewm-integration-batch-management-2vn-ae-sap-s-4hana-cl\|Test Script: SAP EWM Integration – Batch Management (2VN_AE), SAP S/4HANA Cloud Public Edition (2VN_S4CLD2608_BPD_EN_AE)]] | S/4HANA Cloud Public Edition test script for scope item 2VN (AE): batch creation in S/4HANA or EWM, PO, inbound delivery, goods receipt, putaway, batch checks. |
| [[11-inventory-warehouse-and-transportation/test-script-warehouse-inbound-processing-3br-ae-sap-s-4hana-cloud-publ\|Test Script: Warehouse Inbound Processing (3BR_AE) - SAP S/4HANA Cloud Public Edition (3BR_S4CLD2608_BPD_EN_AE)]] | Test script for SAP scope item 3BR (AE): Cloud WM inbound from delivery to putaway - batches, serials, HUs, GR, WTs, GR reversal, clarification zone, RF. |

### Warehouse Internal Inspections

How inspection lots for warehouse stock are created, usage decisions recorded and follow-up warehouse tasks handled.

| Node | Description |
| --- | --- |
| [[11-inventory-warehouse-and-transportation/test-script-warehouse-internal-inspections-5ok-ae-sap-s-4hana-cloud-pu\|Test Script: Warehouse Internal Inspections (5OK_AE) - SAP S/4HANA Cloud Public Edition (5OK_S4CLD2608_BPD_EN_AE)]] | SAP S/4HANA Cloud Public Edition 2608 test script for scope item 5OK_AE: warehouse internal inspections, inspection lots, usage decisions, warehouse tasks, repacking. |
| [[11-inventory-warehouse-and-transportation/test-script-quality-management-in-warehousing-3m0-ae-sap-s-4hana-cloud\|Test Script: Quality Management in Warehousing (3M0_AE) - SAP S/4HANA Cloud Public Edition (3M0_S4CLD2608_BPD_EN_AE)]] | SAP test script for scope item 3M0_AE: inspecting goods from production and suppliers in the warehouse (inspection lot, usage decision, putaway), Fiori and RF. |

### Mobile RF Devices in Warehousing

How warehouse tasks, physical inventory, production staging and QM inspections are confirmed on mobile RF devices.

| Node | Description |
| --- | --- |
| [[11-inventory-warehouse-and-transportation/mobile-rf-devices-in-warehousing-63v-ae-test-script-1144\|Mobile RF Devices in Warehousing (63V_AE) Test Script (63V_S4CLD2608_BPD_EN_AE)]] | SAP S/4HANA Cloud Public Edition test script for scope item 63V (AE): confirm warehouse tasks and physical inventory with mobile RF devices, referencing other scope items. |
| [[11-inventory-warehouse-and-transportation/mobile-rf-devices-in-warehousing-with-production-integration-63w-ae-te\|Mobile RF Devices in Warehousing with Production Integration (63W_AE) - Test Script (63W_S4CLD2608_BPD_EN_AE)]] | SAP S/4HANA Cloud Public Edition test script for scope item 63W: confirming staging and putaway warehouse tasks via mobile RF devices with production integration. |
| [[11-inventory-warehouse-and-transportation/test-script-mobile-rf-devices-in-warehousing-with-quality-management-6\|Test Script: Mobile RF Devices in Warehousing with Quality Management (63X_AE) (63X_S4CLD2608_BPD_EN_AE)]] | Test script for scope item 63X (AE) on SAP S/4HANA Cloud Public Edition 2608: confirming warehouse tasks and creating inspection lots on mobile RF devices in EWM. |

### EWM Outbound Processing to Customer

How sales order deliveries are picked, packed and goods-issued through EWM.

| Node | Description |
| --- | --- |
| [[11-inventory-warehouse-and-transportation/sap-ewm-integration-outbound-processing-to-customer-2vk-ae-test-script\|SAP EWM Integration – Outbound Processing to Customer (2VK_AE) Test Script (2VK_S4CLD2608_BPD_EN_AE)]] | SAP S/4HANA Cloud Public Edition test script for scope item 2VK: ship goods to customers from sales order through EWM picking and goods issue, with sample data and steps. |
| [[11-inventory-warehouse-and-transportation/test-script-warehouse-outbound-processing-3bs-ae-sap-s-4hana-cloud-pub\|Test Script: Warehouse Outbound Processing (3BS_AE) - SAP S/4HANA Cloud Public Edition (3BS_S4CLD2608_BPD_EN_AE)]] | SAP test script for scope item 3BS (AE), Public Edition 2608: setup prerequisites and test steps for warehouse outbound picking, packing, loading, goods issue. |

### Warehouse Posting Changes

How stock moves from unrestricted to blocked or quality stock via warehouse or inventory management posting changes.

| Node | Description |
| --- | --- |
| [[11-inventory-warehouse-and-transportation/warehouse-posting-changes-3bu-ae-test-script-sap-s-4hana-cloud-public\|Warehouse Posting Changes (3BU_AE) - Test Script, SAP S/4HANA Cloud Public Edition (3BU_S4CLD2608_BPD_EN_AE)]] | SAP test script for scope item 3BU_AE: posting changes in the warehouse (unrestricted to blocked/quality stock) via warehouse, inventory management or synchronous routes. |

### EWM Production Supply and Receipt

How EWM stages components to production supply areas, supplies kanban to production, and receives repetitive manufacturing output.

| Node | Description |
| --- | --- |
| [[11-inventory-warehouse-and-transportation/test-script-warehouse-production-integration-with-synchronous-goods-re\|Test Script: Warehouse Production Integration with Synchronous Goods Receipt (5HO_AE) (5HO_S4CLD2608_BPD_EN_AE)]] | SAP S/4HANA Cloud 2608 test script for scope item 5HO_AE: staging material to production and synchronous goods receipt into the EWM warehouse. |
| [[11-inventory-warehouse-and-transportation/warehouse-advanced-production-integration-6ni-ae-test-script-sap-s-4ha\|Warehouse Advanced Production Integration (6NI_AE) - Test Script, SAP S/4HANA Cloud Public Edition (6NI_S4CLD2608_BPD_EN_AE)]] | Test script for SAP S/4HANA Cloud scope item 6NI_AE: staging, consumption posting/reversal and PSA clearance between shop floor and EWM, via Fiori and RF. |
| [[11-inventory-warehouse-and-transportation/produktionsversorgungsbereich-pflegen-sds-3ks-340\|Produktionsversorgungsbereich pflegen – SDS (3KS) (3KS_S4CLD2608_Master_Data_DE_XX)]] | German SAP S/4HANA Cloud Public 2608 master data script 3KS: optional assignment of storage bins to production supply areas (PSA/PVB) in cloud warehouse management. |
| [[11-inventory-warehouse-and-transportation/maintain-production-supply-area-mds-3ks-341\|Maintain Production Supply Area - MDS (3KS) (3KS_S4CLD2608_Master_Data_EN_XX)]] | Master data script (3KS) for optionally assigning storage bins to Production Supply Areas in warehouse production integration, SAP S/4HANA Cloud Public Edition. |
| [[11-inventory-warehouse-and-transportation/script-de-datos-maestros-actualizar-area-de-suministro-de-produccion-m\|Script de datos maestros - Actualizar área de suministro de producción - MDS (3KS) (3KS_S4CLD2608_Master_Data_ES_XX)]] | Spanish (machine-translated) SAP S/4HANA Cloud Public Edition 2608 master data script (3KS): optionally assigning bin locations to production supply areas (PSA) in warehouse management. |
| [[11-inventory-warehouse-and-transportation/mds-3ks-343\|生産供給場所の更新 - MDS (3KS) (3KS_S4CLD2608_Master_Data_JA_XX)]] | Japanese master data script (3KS) for optionally assigning storage bins to production supply areas (PSA) in warehouse-production integration. |
| [[11-inventory-warehouse-and-transportation/atualizar-area-de-abastecimento-da-producao-mds-3ks-344\|Atualizar área de abastecimento da produção – MDS (3KS) (3KS_S4CLD2608_Master_Data_PT_XX)]] | Portuguese master data script (3KS) for optionally assigning warehouse storage bins to a production supply area (AAP) in SAP S/4HANA Cloud Public Edition, with prerequisites and test steps. |
| [[11-inventory-warehouse-and-transportation/mds-3ks-345\|维护生产供应区 - MDS (3KS) (3KS_S4CLD2608_Master_Data_ZH_XX)]] | Chinese (machine-translated) master data script 3KS for optionally assigning bins to production supply areas (PSA) in warehouse management, with prerequisite sc |
| [[11-inventory-warehouse-and-transportation/sap-ewm-integration-delivery-based-production-integration-2vm-ae-test\|SAP EWM Integration – Delivery-Based Production Integration (2VM_AE) – Test Script, SAP S/4HANA Cloud Public Edition… (2VM_S4CLD2608_BPD_EN_AE)]] | Test script for scope item 2VM_AE: staging components from SAP EWM to production and receiving finished goods back into EWM via delivery-based integration. |
| [[11-inventory-warehouse-and-transportation/warehouse-production-integration-3dv-ae-test-script-sap-s-4hana-cloud\|Warehouse Production Integration (3DV_AE) - Test Script, SAP S/4HANA Cloud Public Edition (3DV_S4CLD2608_BPD_EN_AE)]] | SAP test script for scope item 3DV_AE: staging material to production and goods receipt/putaway of finished goods via Fiori or RF, with prerequisites. |
| [[11-inventory-warehouse-and-transportation/warehouse-kanban-supply-into-production-3vt-ae-test-script-977\|Warehouse Kanban Supply into Production (3VT_AE) - Test Script (3VT_S4CLD2608_BPD_EN_AE)]] | SAP S/4HANA Cloud Public Edition 2608 test script for scope item 3VT: Kanban replenishment from warehouse to production, with prerequisites, roles and test steps. |
| [[11-inventory-warehouse-and-transportation/test-script-warehouse-goods-receipt-from-repetitive-manufacturing-41u\|Test Script: Warehouse Goods Receipt from Repetitive Manufacturing (41U_AE) (41U_S4CLD2608_BPD_EN_AE)]] | SAP S/4HANA Cloud Public Edition 2608 test script for scope item 41U: goods receipt of repetitive manufacturing output into the warehouse, with putaway variants. |

### Warehouse Internal Repacking

How handling units are repacked, packed and unpacked in the Pack Warehouse Stock app.

| Node | Description |
| --- | --- |
| [[11-inventory-warehouse-and-transportation/test-script-warehouse-internal-repacking-3bw-ae-925\|Test Script: Warehouse Internal Repacking (3BW_AE) (3BW_S4CLD2608_BPD_EN_AE)]] | SAP S/4HANA Cloud Public Edition test script (19-06-26) for warehouse internal repacking (3BW_AE): repack, pack and unpack handling units with Pack Warehouse Stock (F3738). |

### EWM Replenishment of Fixed Bins

How planned and automatic replenishment of fixed bins is scheduled and replenishment tasks executed.

| Node | Description |
| --- | --- |
| [[11-inventory-warehouse-and-transportation/test-script-replenishment-in-warehousing-4a2-ae-1007\|Test Script: Replenishment in Warehousing (4A2_AE) (4A2_S4CLD2608_BPD_EN_AE)]] | SAP S/4HANA Cloud Public Edition 2608 test script for scope item 4A2: planned/automatic replenishment of fixed bins in EWM, with job scheduling and task confirmation. |

### EWM Storage Bins and Fixed Bin Assignments

How storage bins are created, changed, mass-changed and fixed bins assigned in EWM.

| Node | Description |
| --- | --- |
| [[11-inventory-warehouse-and-transportation/stammdatenskript-lagerplatze-und-fixplatzzuordnungen-pflegen-sds-3kr-3\|Stammdatenskript: Lagerplätze und Fixplatzzuordnungen pflegen – SDS (3KR) (3KR_S4CLD2608_Master_Data_DE_XX)]] | German master data script (3KR) for SAP S/4HANA Cloud Public Edition: create, change, display, mass-change storage bins and assign fixed bins in EWM. |
| [[11-inventory-warehouse-and-transportation/maintain-storage-bins-and-fixed-bin-assignments-mds-3kr-335\|Maintain Storage Bins and Fixed Bin Assignments - MDS (3KR) (3KR_S4CLD2608_Master_Data_EN_XX)]] | SAP S/4HANA Cloud Public Edition master data script (3KR) for creating, changing, displaying, mass-changing storage bins and assigning fixed bins in EWM warehouse management. |
| [[11-inventory-warehouse-and-transportation/script-de-datos-maestros-actualizar-ubicaciones-y-asignaciones-de-ubic\|Script de datos maestros - Actualizar ubicaciones y asignaciones de ubicación fija (3KR) (3KR_S4CLD2608_Master_Data_ES_XX)]] | Spanish (machine-translated) SAP master data script 3KR: create, change, display, mass-change warehouse storage bins and assign fixed bins in EWM via Fiori, release 2608. |
| [[11-inventory-warehouse-and-transportation/mds-3kr-337\|棚番および固定保管棚の割当の更新 - MDS (3KR) (3KR_S4CLD2608_Master_Data_JA_XX)]] | Japanese SAP master data script (3KR, 2608): create, change, display, mass-change storage bins and assign fixed storage bins in EWM as warehouse clerk. |
| [[11-inventory-warehouse-and-transportation/script-de-dados-mestre-atualizar-posicoes-no-deposito-e-atribuicoes-de\|Script de dados mestre - Atualizar posições no depósito e atribuições de posições fixas (3KR) (3KR_S4CLD2608_Master_Data_PT_XX)]] | Portuguese SAP master data script 3KR: create, change, display, mass-change warehouse storage bins and assign fixed bins in EWM via Fiori, release 2608. |
| [[11-inventory-warehouse-and-transportation/mds-3kr-339\|维护仓位和固定仓位分配 - MDS (3KR) (3KR_S4CLD2608_Master_Data_ZH_XX)]] | Chinese (machine-translated) master data script 3KR: create, change, display, mass-change storage bins and assign fixed bins in EWM, S/4HANA Cloud Public Edition 2608. |

### EWM Warehouse Product Attributes

How warehouse-relevant product attributes are maintained in the Warehouse Monitor or Manage Product Master Data.

| Node | Description |
| --- | --- |
| [[11-inventory-warehouse-and-transportation/attribute-fur-lagerprodukte-pflegen-sds-3kq-328\|Attribute für Lagerprodukte pflegen – SDS (3KQ) (3KQ_S4CLD2608_Master_Data_DE_XX)]] | German SAP S/4HANA Cloud Public 2608 master data script 3KQ: maintaining warehouse product attributes via Warehouse Monitor (mass) or Manage Product Master Data (F1602). |
| [[11-inventory-warehouse-and-transportation/master-data-script-maintain-warehouse-products-attributes-3kq-329\|Master Data Script: Maintain Warehouse Products Attributes (3KQ) (3KQ_S4CLD2608_Master_Data_EN_XX)]] | SAP S/4HANA Cloud 2608 master data script 3KQ: maintaining warehouse product attributes via Warehouse Monitor (/SCWM/MON) or Manage Product Master Data (F1602). |
| [[11-inventory-warehouse-and-transportation/actualizar-atributos-de-productos-de-almacen-mds-3kq-es-330\|Actualizar atributos de productos de almacén - MDS (3KQ) [ES] (3KQ_S4CLD2608_Master_Data_ES_XX)]] | Spanish machine-translated SAP S/4HANA Cloud master data script 3KQ for updating warehouse product attributes via Warehouse Monitor or Manage Product Master Data (F1602). |
| [[11-inventory-warehouse-and-transportation/mds-3kq-331\|倉庫製品属性の更新 - MDS (3KQ) (3KQ_S4CLD2608_Master_Data_JA_XX)]] | Japanese master data script (3KQ) for updating warehouse-relevant product attributes via Warehouse Monitor (mass) or Manage Product Master Data (F1602). |
| [[11-inventory-warehouse-and-transportation/script-de-dados-mestre-atualizar-atributos-de-produtos-de-deposito-mds\|Script de dados mestre - Atualizar atributos de produtos de depósito - MDS (3KQ) (3KQ_S4CLD2608_Master_Data_PT_XX)]] | Portuguese SAP S/4HANA Cloud Public Edition 2608 master data script (3KQ): updating warehouse product attributes via the /SCWM/MON monitor or app F1602. |
| [[11-inventory-warehouse-and-transportation/mds-3kq-333\|维护仓库产品属性 - MDS (3KQ) (3KQ_S4CLD2608_Master_Data_ZH_XX)]] | Chinese (machine-translated) master data script 3KQ for maintaining warehouse product attributes via Warehouse Monitor (/SCWM/MON) or Manage Product Master Data |

### EWM Warehouse Resources

How warehouse resources (users, devices) are created and deleted in the Warehouse Monitor.

| Node | Description |
| --- | --- |
| [[11-inventory-warehouse-and-transportation/stammdatenskript-lagerstammdaten-fur-ressource-anlegen-sds-3y2-394\|Stammdatenskript: Lagerstammdaten für Ressource anlegen – SDS (3Y2) (3Y2_S4CLD2608_Master_Data_DE_XX)]] | German master data test script (3Y2): create and delete warehouse resources in the EWM warehouse monitor (/SCWM/MON) as Lagerist (EWM). |
| [[11-inventory-warehouse-and-transportation/master-data-script-create-warehouse-master-data-for-resource-mds-3y2-3\|Master Data Script: Create Warehouse Master Data for Resource – MDS (3Y2) (3Y2_S4CLD2608_Master_Data_EN_XX)]] | SAP S/4HANA Cloud 2608 master data script (3Y2) for creating and deleting warehouse resources in the Warehouse Monitor (/SCWM/MON) as Warehouse Clerk (EWM). |
| [[11-inventory-warehouse-and-transportation/crear-datos-maestros-de-almacen-para-recurso-mds-3y2-396\|Crear datos maestros de almacén para recurso - MDS (3Y2) (3Y2_S4CLD2608_Master_Data_ES_XX)]] | Spanish (machine-translated) SAP master data script for creating and deleting warehouse resources via Warehouse Monitor (/SCWM/MON) in S/4HANA Cloud Public Edition 2608. |
| [[11-inventory-warehouse-and-transportation/mds-3y2-397\|資源の倉庫マスタデータの登録 - MDS (3Y2) (3Y2_S4CLD2608_Master_Data_JA_XX)]] | Japanese master data script 3Y2 for creating and deleting warehouse resources with Warehouse Monitor (/SCWM/MON) in S/4HANA Cloud Public Edition 2608. |
| [[11-inventory-warehouse-and-transportation/script-de-dados-mestre-criar-dados-mestre-de-deposito-para-recurso-mds\|Script de dados mestre: Criar dados mestre de depósito para recurso – MDS (3Y2) (3Y2_S4CLD2608_Master_Data_PT_XX)]] | Portuguese master data test script (3Y2): create and delete warehouse resources in the EWM warehouse monitor (/SCWM/MON) as warehouse clerk. |
| [[11-inventory-warehouse-and-transportation/mds-3y2-399\|创建资源的仓库主数据 - MDS (3Y2) (3Y2_S4CLD2608_Master_Data_ZH_XX)]] | Master data script (Chinese, machine-translated) for creating and deleting warehouse resources in the EWM Warehouse Monitor (/SCWM/MON), SAP S/4HANA Cloud Publi |

### Wave Management in Warehousing

How wave templates, wave jobs, simulation and release group outbound warehouse requests.

| Node | Description |
| --- | --- |
| [[11-inventory-warehouse-and-transportation/test-script-wave-management-in-warehousing-6nh-ae-1184\|Test Script: Wave Management in Warehousing (6NH_AE) (6NH_S4CLD2608_BPD_EN_AE)]] | SAP S/4HANA Cloud Public Edition test script for scope item 6NH Wave Management in Warehousing: wave templates, wave job, simulation, release, logs, exception handling. |

### Freight Agreements

How freight agreements with calculation sheets and rate tables are created for road, rail, sea and air carriers.

| Node | Description |
| --- | --- |
| [[11-inventory-warehouse-and-transportation/stammdatenskript-lieferplan-anlegen-sds-3tl-sap-s-4hana-cloud-public-e\|Stammdatenskript: Lieferplan anlegen – SDS (3TL) – SAP S/4HANA Cloud Public Edition (3TL_S4CLD2608_Master_Data_DE_XX)]] | German master data script (SAP S/4HANA Cloud Public Edition 2608) for creating freight agreements (Frachtvereinbarungen) for road, rail, sea and air carriers in Transportation Management. |
| [[11-inventory-warehouse-and-transportation/master-data-script-create-freight-agreement-mds-3tl-sap-s-4hana-cloud\|Master Data Script: Create Freight Agreement - MDS (3TL), SAP S/4HANA Cloud Public Edition (3TL_S4CLD2608_Master_Data_EN_XX)]] | SAP Best Practices master data script (3TL) for creating freight agreements in Transportation Management: road, rail, ocean, air carriers, with example rate tables. |
| [[11-inventory-warehouse-and-transportation/script-de-datos-maestros-creacion-de-acuerdo-de-flete-mds-3tl-366\|Script de datos maestros - Creación de acuerdo de flete - MDS (3TL) (3TL_S4CLD2608_Master_Data_ES_XX)]] | SAP S/4HANA Cloud Public Edition 2608 master data script (ES, machine-translated): create freight agreements (F3790) for road, rail, sea and air carriers, with sample rates. |
| [[11-inventory-warehouse-and-transportation/sap-s-4hana-cloud-public-edition-mds-3tl-367\|マスタデータスクリプト SAP S/4HANA Cloud Public Edition - 運送契約登録 - MDS (3TL) (3TL_S4CLD2608_Master_Data_JA_XX)]] | Japanese master data script (3TL, 2608) for creating freight agreements in S/4HANA Cloud Public Edition: land, rail, sea, air, with sample rate tables. |
| [[11-inventory-warehouse-and-transportation/script-de-dados-mestre-criar-acordo-de-frete-mds-3tl-368\|Script de dados mestre - Criar acordo de frete – MDS (3TL) (3TL_S4CLD2608_Master_Data_PT_XX)]] | SAP S/4HANA Cloud Public Edition 2608 master data script (PT) for creating freight agreements (road, rail, sea, air) with calculation sheets, rate tables and sample values. |
| [[11-inventory-warehouse-and-transportation/sap-s-4hana-cloud-public-edition-mds-3tl-369\|主数据脚本 SAP S/4HANA Cloud Public Edition - 创建货运协议 - MDS (3TL) (3TL_S4CLD2608_Master_Data_ZH_XX)]] | Chinese machine-translated master data script (3TL, 2608) for creating freight agreements in SAP S/4HANA Cloud Public Edition: road, rail, sea, air carriers and forwarders. |

### Freight Settlement

How freight costs are accrued, allocated, and carrier invoices verified and posted.

| Node | Description |
| --- | --- |
| [[11-inventory-warehouse-and-transportation/test-script-freight-settlement-6w4-ae-sap-s-4hana-cloud-public-edition\|Test Script: Freight Settlement (6W4_AE) - SAP S/4HANA Cloud Public Edition (6W4_S4CLD2608_BPD_EN_AE)]] | SAP S/4HANA Cloud Public Edition test script for scope item 6W4 Freight Settlement (AE): accrual posting, cost allocation, carrier invoice verification, ERS, SOAP invoices. |

### Stock Transfers Within a Company Code

How stock moves between plants with or without delivery, by stock transport order or one-/two-step cross-plant transfer posting.

| Node | Description |
| --- | --- |
| [[11-inventory-warehouse-and-transportation/test-script-stock-transfer-with-delivery-bme-ae-sap-s-4hana-cloud-publ\|Test Script: Stock Transfer with Delivery (BME_AE) - SAP S/4HANA Cloud Public Edition (BME_S4CLD2608_BPD_EN_AE)]] | SAP S/4HANA Cloud Public Edition 2608 (AE) test script for intracompany stock transfer with delivery (BME): prerequisites, roles, and step-by-step Fiori test procedures. |
| [[11-inventory-warehouse-and-transportation/test-script-stock-transfer-without-delivery-bmh-ae-sap-s-4hana-cloud-p\|Test Script: Stock Transfer Without Delivery (BMH_AE) - SAP S/4HANA Cloud Public Edition (BMH_S4CLD2608_BPD_EN_AE)]] | SAP S/4HANA Cloud Public Edition 2608 test script (BMH_AE, plants 3310/3320) for stock transfer without delivery via stock transport orders, with prerequisites and Fiori app steps. |
| [[11-inventory-warehouse-and-transportation/test-script-cross-plant-transfer-posting-1p7-ae-752\|Test Script: Cross-Plant Transfer Posting (1P7_AE) (1P7_S4CLD2608_BPD_EN_AE)]] | SAP S/4HANA Cloud Public Edition 2608 test script for scope item 1P7_AE: one-step and two-step cross-plant stock transfer posting, with prerequisites and test steps. |
| [[11-inventory-warehouse-and-transportation/test-script-sap-ewm-integration-stock-transport-orders-2vl-ae-sap-s-4h\|Test Script: SAP EWM Integration – Stock Transport Orders (2VL_AE), SAP S/4HANA Cloud Public Edition (2VL_S4CLD2608_BPD_EN_AE)]] | SAP S/4HANA Cloud Public Edition 2608 test script for scope item 2VL_AE: stock transport orders with SAP EWM, in three EWM/inventory-managed transfer scenarios. |

### MM Posting Periods

How the current MM period is closed and a new materials management posting period opened with Close Periods (MMPV).

| Node | Description |
| --- | --- |
| [[11-inventory-warehouse-and-transportation/neue-offene-mm-buchungsperiode-anlegen-sds-bnz-694\|Neue offene MM-Buchungsperiode anlegen – SDS (BNZ) (BNZ_S4CLD2608_Master_Data_DE_XX)]] | German SAP master data script (BNZ, 2608): close the MM period and open a new posting period with Perioden abschließen (MMPV) as Stammdatenexperte – Produktdaten. |
| [[11-inventory-warehouse-and-transportation/create-new-open-mm-posting-period-mds-bnz-695\|Create New Open MM Posting Period - MDS (BNZ) (BNZ_S4CLD2608_Master_Data_EN_XX)]] | SAP S/4HANA Cloud Public Edition 2608 master data script for closing the MM period and opening a new posting period via Close Periods (MMPV). |
| [[11-inventory-warehouse-and-transportation/crear-nuevo-periodo-contable-mm-abierto-mds-bnz-696\|Crear nuevo período contable MM abierto - MDS (BNZ) (BNZ_S4CLD2608_Master_Data_ES_XX)]] | Spanish (machine-translated) master data script BNZ: close MM period and open a new material-management posting period via Cerrar períodos (MMPV), SAP S/4HANA C |
| [[11-inventory-warehouse-and-transportation/mm-mds-bnz-697\|オープン MM 転記期間の新規登録 - MDS (BNZ) (BNZ_S4CLD2608_Master_Data_JA_XX)]] | Master data script (Japanese) for opening a new MM posting period in SAP S/4HANA Cloud Public Edition 2608 using the Close Periods app (MMPV). |
| [[11-inventory-warehouse-and-transportation/criar-periodo-contabil-mm-aberto-mds-bnz-698\|Criar período contábil MM aberto – MDS (BNZ) (BNZ_S4CLD2608_Master_Data_PT_XX)]] | Portuguese SAP master data script (BNZ, 2608): close the MM period and open a new posting period with Encerrar períodos (MMPV) as Especialista em dados mestre - Dados do produto. |
| [[11-inventory-warehouse-and-transportation/mds-bnz-699\|创建新的未清物料管理过账期间 - MDS (BNZ) (BNZ_S4CLD2608_Master_Data_ZH_XX)]] | Chinese (machine-translated) master data script BNZ: close the MM period and open a new posting period with the Close Periods app (MMPV). |

### Physical Inventory Count and Adjustment

How physical inventory documents are created, printed, counted, recounted and differences posted.

| Node | Description |
| --- | --- |
| [[11-inventory-warehouse-and-transportation/physical-inventory-cycle-counting-4lu-ae-test-script-sap-s-4hana-cloud\|Physical Inventory – Cycle Counting (4LU_AE) – Test Script, SAP S/4HANA Cloud Public Edition (4LU_S4CLD2608_BPD_EN_AE)]] | SAP S/4HANA Cloud Public Edition test script (4LU, AE) for cycle counting: prerequisites, indicator setup, and count-to-posting steps with Fiori apps. |
| [[11-inventory-warehouse-and-transportation/physical-inventory-inventory-count-and-adjustment-bml-ae-test-script-1\|Physical Inventory – Inventory Count and Adjustment (BML_AE) Test Script (BML_S4CLD2608_BPD_EN_AE)]] | SAP S/4HANA Cloud Public Edition test script (UAE, plant 3310) for physical inventory: create documents, print, count, recount, post differences, notifications, analysis. |

### Serial Number Management

How serial numbers are created, maintained and displayed with history, status and logs.

| Node | Description |
| --- | --- |
| [[11-inventory-warehouse-and-transportation/serial-number-management-in-logistics-bll-ae-test-script-1284\|Serial Number Management in Logistics (BLL_AE) Test Script (BLL_S4CLD2608_BPD_EN_AE)]] | SAP S/4HANA Cloud Public Edition test script for scope item BLL_AE: creating, maintaining and displaying serial numbers, history, status and logs (AE localization). |

### Transportation Locations

How transportation location master records and location types are created in Manage Locations (F6225).

| Node | Description |
| --- | --- |
| [[11-inventory-warehouse-and-transportation/standorte-verwalten-sds-7e9-526\|Standorte verwalten - SDS (7E9) (7E9_S4CLD2608_Master_Data_DE_XX)]] | SAP S/4HANA Cloud 2608 master data script (DE) for creating locations via Manage Locations (F6225) as transportation management master data expert. |
| [[11-inventory-warehouse-and-transportation/manage-locations-mds-7e9-527\|Manage Locations - MDS (7E9) (7E9_S4CLD2608_Master_Data_EN_XX)]] | SAP S/4HANA Cloud Public Edition master data script (7E9) for creating transportation location master records in Manage Locations (F6225). |
| [[11-inventory-warehouse-and-transportation/gestion-de-ubicaciones-mds-7e9-528\|Gestión de ubicaciones - MDS (7E9) (7E9_S4CLD2608_Master_Data_ES_XX)]] | Spanish (machine-translated) SAP S/4HANA Cloud Public Edition master data script (7E9) for creating transportation locations with Manage Locations (F6225). |
| [[11-inventory-warehouse-and-transportation/mds-7e9-529\|ロケーション管理 - MDS (7E9) (7E9_S4CLD2608_Master_Data_JA_XX)]] | SAP S/4HANA Cloud Public Edition 2608 マスタデータスクリプト (7E9): ロケーション管理 (F6225) でロケーションマスタを登録する手順とロケーションタイプ (日本語)。 |
| [[11-inventory-warehouse-and-transportation/administrar-localizacoes-mds-7e9-530\|Administrar localizações - MDS (7E9) (7E9_S4CLD2608_Master_Data_PT_XX)]] | SAP S/4HANA Cloud 2608 master data script (PT) for creating locations (location master) via Manage Locations (F6225) as transportation master data specialist. |
| [[11-inventory-warehouse-and-transportation/mds-7e9-531\|管理位置 - MDS (7E9) (7E9_S4CLD2608_Master_Data_ZH_XX)]] | Chinese (machine-translated) master data script 7E9: create location master data (port, airport, train station) with Manage Locations app F6225. |

### Stock Transfer Returns

How stock is returned between plants of one company code or across company codes with returns stock transport orders, deliveries, goods movements and credit memos.

| Node | Description |
| --- | --- |
| [[11-inventory-warehouse-and-transportation/intra-company-returns-stock-transfers-5wi-ae-test-script-1129\|Intra-Company Returns Stock Transfers (5WI_AE) - Test Script (5WI_S4CLD2608_BPD_EN_AE)]] | SAP S/4HANA Cloud test script for scope item 5WI_AE: returning stock between plants of one company code, with prerequisites, roles, apps and test steps. |
| [[11-inventory-warehouse-and-transportation/test-script-intercompany-stock-transfer-returns-2ts-ae-sap-s-4hana-clo\|Test Script: Intercompany Stock Transfer Returns (2TS_AE) - SAP S/4HANA Cloud Public Edition 2608 (2TS_S4CLD2608_BPD_EN_AE)]] | SAP test script (AE, release 2608) for intercompany stock transfer returns, domestic and international: returns STO through credit memo, with prerequisites. |

### Logistics with Third-Party Warehouse Management

How stock transfers, procurement receipts, sales deliveries and returns are executed by an external WMS integrated through warehouse web services.

| Node | Description |
| --- | --- |
| [[11-inventory-warehouse-and-transportation/test-script-logistics-with-third-party-warehouse-management-1zq-ae-793\|Test Script: Logistics with Third-Party Warehouse Management (1ZQ_AE) (1ZQ_S4CLD2608_BPD_EN_AE)]] | SAP S/4HANA Cloud Public Edition test script for scope item 1ZQ_AE: stock transfers, procurement, sales and returns integrated with a third-party WMS. |

### Handling Unit Management

How handling units are packed in inbound and outbound deliveries with packing instructions and managed through HU inventory, physical inventory and manufacturing.

| Node | Description |
| --- | --- |
| [[11-inventory-warehouse-and-transportation/test-script-handling-unit-management-4mm-ae-sap-s-4hana-cloud-public-e\|Test Script: Handling Unit Management (4MM_AE) - SAP S/4HANA Cloud Public Edition 2608 (4MM_S4CLD2608_BPD_EN_AE)]] | SAP test script (UAE localization, 4MM_AE) for Handling Unit Management: packing in deliveries, HU inventory, physical inventory and HU in manufacturing; prerequisites and steps. |

### EWM Physical Inventory, Scrapping and Ad Hoc Goods Issue

How warehouse physical inventory and cycle counts are posted in EWM, initial stock uploaded, and unplanned goods issues and scrapping executed.

| Node | Description |
| --- | --- |
| [[11-inventory-warehouse-and-transportation/test-script-sap-ewm-integration-warehouse-stock-handling-2yl-ae-889\|Test Script: SAP EWM Integration – Warehouse Stock Handling (2YL_AE) (2YL_S4CLD2608_BPD_EN_AE)]] | SAP test script for scope item 2YL_AE: EWM integration with S/4HANA Cloud Public Edition covering initial stock upload, physical inventory and scrapping. |
| [[11-inventory-warehouse-and-transportation/test-script-warehouse-ad-hoc-goods-issue-3bt-ae-sap-s-4hana-cloud-publ\|Test Script: Warehouse Ad Hoc Goods Issue (3BT_AE) - SAP S/4HANA Cloud Public Edition (3BT_S4CLD2608_BPD_EN_AE)]] | SAP S/4HANA Cloud test script for scope item 3BT_AE: unplanned warehouse goods issue, scrapping and synchronous goods movements, with roles, data and steps. |
| [[11-inventory-warehouse-and-transportation/warehouse-physical-inventory-3bx-ae-test-script-sap-s-4hana-cloud-publ\|Warehouse Physical Inventory (3BX_AE) - Test Script, SAP S/4HANA Cloud Public Edition (3BX_S4CLD2608_BPD_EN_AE)]] | Test script for SAP S/4HANA Cloud scope item 3BX_AE: warehouse physical inventory and cycle counting, from document creation to difference posting. |

### Transportation Planning and Execution

How freight units become freight orders and bookings for road, rail, ocean and air, are planned manually or externally, executed and accrued.

| Node | Description |
| --- | --- |
| [[11-inventory-warehouse-and-transportation/test-script-sap-s-4hana-cloud-public-edition-external-transportation-p\|Test Script SAP S/4HANA Cloud Public Edition - External Transportation Planning (6W1_AE) (6W1_S4CLD2608_BPD_EN_AE)]] | SAP S/4HANA Cloud Public Edition test script, scope item 6W1_AE: monitor freight units and freight orders and create deliveries as Dispatcher (TM). |
| [[11-inventory-warehouse-and-transportation/manual-transportation-planning-6w2-ae-test-script-sap-s-4hana-cloud-pu\|Manual Transportation Planning (6W2_AE) - Test Script, SAP S/4HANA Cloud Public Edition (6W2_S4CLD2608_BPD_EN_AE)]] | SAP test script for scope item 6W2 (AE): manual transportation planning in TM for road, rail, ocean, air and advanced intercompany, with prerequisites, sample data, steps. |
| [[11-inventory-warehouse-and-transportation/test-script-transportation-execution-6w3-ae-sap-s-4hana-cloud-public-e-part-01\|Test Script: Transportation Execution (6W3_AE) - SAP S/4HANA Cloud Public Edition (6W3_S4CLD2608_BPD_EN_AE) — part 1 of 3]] | Test script for SAP S/4HANA Cloud Public Edition scope item 6W3 Transportation Execution (AE): road, rail, ocean, air and advanced intercompany test steps. |
| [[11-inventory-warehouse-and-transportation/test-script-transportation-execution-6w3-ae-sap-s-4hana-cloud-public-e-part-02\|Test Script: Transportation Execution (6W3_AE) - SAP S/4HANA Cloud Public Edition (6W3_S4CLD2608_BPD_EN_AE) — part 2 of 3]] | Test script for scope item 6W3 Transportation Execution: ocean, air, stock transfer and advanced intercompany freight steps in SAP Fiori (TM/EWM). |
| [[11-inventory-warehouse-and-transportation/test-script-transportation-execution-6w3-ae-sap-s-4hana-cloud-public-e-part-03\|Test Script: Transportation Execution (6W3_AE) - SAP S/4HANA Cloud Public Edition (6W3_S4CLD2608_BPD_EN_AE) — part 3 of 3]] | SAP test script for scope item 6W3 Transportation Execution (AE), S/4HANA Cloud 2608; ends with accrual posting, error repost, follow-on processes. |

## Related categories
- related-to :: [[12-production-and-manufacturing/_cluster]]
- related-to :: [[15-retail-operations/_cluster]]
