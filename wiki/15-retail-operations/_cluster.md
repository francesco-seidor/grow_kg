---
title: Retail Operations
description: "Distribution center inbound and outbound, store ordering and returns, in-store inventory, store management, retail price valuation, consignment, DC replenishment and promotions."
cluster: 15-retail-operations
type: cluster
tags: [kb/retail-operations, kb/hub]
keywords: [retail, distribution center, store, store ordering, in-store inventory, My Store, sales price valuation, omnichannel promotion]
node_count: 40
created: 2026-10-12
updated: 2026-10-12
---

# Retail Operations

Covers retail-specific scope items. Excludes general EWM and inventory processes (see 11) and non-retail sales and pricing (see 08).

Every node below is the verbatim text of one source document (or one part of a long one), grouped by topic.

## Nodes

### Inbound Logistics for Distribution Centers

How DC inbound deliveries, putaway confirmation and goods receipt postings are processed.

| Node | Description |
| --- | --- |
| [[15-retail-operations/test-script-inbound-logistics-for-distribution-centers-5fu-ae-1089\|Test Script: Inbound Logistics for Distribution Centers (5FU_AE) (5FU_S4CLD2608_BPD_EN_AE)]] | SAP S/4HANA Cloud Public Edition test script for scope item 5FU_AE: inbound delivery, putaway confirmation and goods receipt posting at a distribution center. |

### Outbound Logistics for Distribution Centers

How DCs ship to stores: stock transfer orders, outbound deliveries, pick/pack, goods issue and store receipt.

| Node | Description |
| --- | --- |
| [[15-retail-operations/outbound-logistics-for-distribution-centers-5fv-ae-test-script-1090\|Outbound Logistics for Distribution Centers (5FV_AE) - Test Script (5FV_S4CLD2608_BPD_EN_AE)]] | SAP S/4HANA Cloud Public Edition test script (19-06-26) for scope item 5FV_AE: stock transfer order, outbound delivery, pick/pack, goods issue and store goods receipt. |

### Replenishment Planning for Distribution Centers

How DC replenishment uses forecasts, PIRs, MRP runs and background jobs to create purchase requisitions.

| Node | Description |
| --- | --- |
| [[15-retail-operations/replenishment-planning-for-distribution-centers-3i8-ae-test-script-947\|Replenishment Planning for Distribution Centers (3I8_AE) - Test Script (3I8_S4CLD2608_BPD_EN_AE)]] | SAP S/4HANA Cloud Public Edition test script for scope item 3I8_AE: DC replenishment via forecast, PIR, MRP runs, background jobs and purchase requisition checks. |

### In-Store Inventory Management

How stores perform physical inventory, ad hoc counts and mass stock adjustments.

| Node | Description |
| --- | --- |
| [[15-retail-operations/test-script-in-store-inventory-management-3hr-ae-sap-s-4hana-cloud-pub\|Test Script: In-Store Inventory Management (3HR_AE) - SAP S/4HANA Cloud Public Edition (3HR_S4CLD2608_BPD_EN_AE)]] | SAP S/4HANA Cloud Public Edition test script (3HR_AE, dated 19-06-26) for in-store inventory: physical inventory, ad hoc count, mass stock adjustment, transfers, clean-up. |

### My Store Management

How store associates are assigned, picking sequences set and the My Store Overview app used.

| Node | Description |
| --- | --- |
| [[15-retail-operations/test-script-my-store-management-5fw-ae-sap-s-4hana-cloud-public-editio\|Test Script: My Store Management (5FW_AE) - SAP S/4HANA Cloud Public Edition (5FW_S4CLD2608_BPD_EN_AE)]] | SAP test script for scope item 5FW My Store Management (AE): store associate assignment, picking sequence and My Store Overview app, with prerequisites and sample data. |
| [[15-retail-operations/test-script-in-store-merchandise-management-3hq-ae-sap-s-4hana-cloud-p\|Test Script: In-Store Merchandise Management (3HQ_AE), SAP S/4HANA Cloud Public Edition (3HQ_S4CLD2608_BPD_EN_AE)]] | SAP S/4HANA Cloud Public Edition test script for scope item 3HQ_AE: store associates look up retail products and print labels; prerequisites and steps. |

### Omnichannel Promotion Pricing for Sales Orders

How SAP Omnichannel Promotion Pricing applies promotions to in-store sales orders.

| Node | Description |
| --- | --- |
| [[15-retail-operations/test-script-omnichannel-sales-promotion-opps-consumer-products-7t7-ae\|Test Script: Omnichannel Sales Promotion (OPPS) – Consumer Products (7T7_AE) (7T7_S4CLD2608_BPD_EN_AE)]] | SAP S/4HANA Cloud 2608 test script, scope item 7T7_AE: OPPS promotion rules (free item, discount, combined), prerequisites and sales order tests, AE/AED. |
| [[15-retail-operations/omnichannel-sales-promotions-for-sales-orders-in-retail-7z6-ae-test-sc\|Omnichannel Sales Promotions for Sales Orders in Retail (7Z6_AE) - Test Script (7Z6_S4CLD2608_BPD_EN_AE)]] | SAP S/4HANA Cloud Public Edition 2608 test script for scope item 7Z6: applying SAP Omnichannel Promotion Pricing promotions to in-store sales orders and POS payments. |

### Sales Price Valuation for Retail

How retail inventory is valued and revalued at sales prices.

| Node | Description |
| --- | --- |
| [[15-retail-operations/test-script-sales-price-valuation-for-retail-5ft-ae-sap-s-4hana-cloud\|Test Script: Sales Price Valuation for Retail (5FT_AE) - SAP S/4HANA Cloud Public Edition (5FT_S4CLD2608_BPD_EN_AE)]] | SAP S/4HANA Cloud Public Edition test script (scope item 5FT, AE) for sales price valuation and revaluation in retail, with roles, sample data and step-by-step Fiori test procedures. |

### Supplier Consignment for Retail

How retail consignment stock is procured, sold and settled with suppliers.

| Node | Description |
| --- | --- |
| [[15-retail-operations/test-script-supplier-consignment-for-retail-71p-ae-sap-s-4hana-cloud-p\|Test Script: Supplier Consignment for Retail (71P_AE) - SAP S/4HANA Cloud Public Edition (71P_S4CLD2608_BPD_EN_AE)]] | SAP test script for scope item 71P_AE (AE localization): supplier consignment retail processes, roles, sample data, Fiori apps and step-by-step test procedures. |

### Store Ordering from Distribution Centers

How stores order from distribution centers via stock transport orders and advance shipping notifications.

| Node | Description |
| --- | --- |
| [[15-retail-operations/test-script-store-ordering-from-distribution-center-5fx-ae-1092\|Test Script: Store Ordering from Distribution Center (5FX_AE) (5FX_S4CLD2608_BPD_EN_AE)]] | SAP S/4HANA Cloud Public Edition 2608 test script for scope item 5FX: stores ordering from distribution centers via stock transport orders and advanced intercompany stock transfer. |
| [[15-retail-operations/test-script-in-store-purchase-order-management-5fy-ae-sap-s-4hana-clou\|Test Script: In-Store Purchase Order Management (5FY_AE) - SAP S/4HANA Cloud Public Edition (5FY_S4CLD2608_BPD_EN_AE)]] | SAP S/4HANA Cloud Public Edition test script for scope item 5FY_AE: store order proposals plus standard, customer-order-based and trusted receiving. |

### Returns from Store

How merchandise is returned from a store to a distribution center via returns stock transport orders.

| Node | Description |
| --- | --- |
| [[15-retail-operations/returns-from-store-5fr-ae-1086\|Returns from Store (5FR_AE) (5FR_S4CLD2608_BPD_EN_AE)]] | SAP S/4HANA Cloud Public Edition test script for scope item 5FR_AE: returning merchandise from a store to a distribution center via returns stock transport order. |

### Retail Articles, Merchandise Categories and Seasons

How retail articles (single, generic, sets) are created in merchandise category hierarchies, reclassified, assigned seasons and converted by characteristic values.

| Node | Description |
| --- | --- |
| [[15-retail-operations/product-taxonomies-for-retail-5fj-ae-test-script-1079\|Product Taxonomies for Retail (5FJ_AE) - Test Script (5FJ_S4CLD2608_BPD_EN_AE)]] | SAP S/4HANA Cloud Public Edition test script (AE, 19-06-26) for scope item 5FJ: merchandise categories, hierarchies, reclassification, with article, assortment, PO and allocation prerequisites. |
| [[15-retail-operations/test-script-seasons-for-retail-6di-ae-sap-s-4hana-cloud-public-edition\|Test Script: Seasons for Retail (6DI_AE) - SAP S/4HANA Cloud Public Edition (6DI_S4CLD2608_BPD_EN_AE)]] | SAP test script for Seasons for Retail (6DI_AE): create season master data, assign it to products, verify season copy across sales, purchase and STO documents. |
| [[15-retail-operations/test-script-characteristic-value-conversion-for-retail-7dl-ae-sap-s-4h\|Test Script: Characteristic Value Conversion for Retail (7DL_AE) - SAP S/4HANA Cloud Public Edition (7DL_S4CLD2608_BPD_EN_AE)]] | SAP S/4HANA Cloud Public Edition test script for scope item 7DL_AE: converting article characteristic values across sales, purchase and STO documents. |
| [[15-retail-operations/products-for-retail-3i1-ae-test-script-sap-s-4hana-cloud-public-editio\|Products for Retail (3I1_AE) - Test Script, SAP S/4HANA Cloud Public Edition (3I1_S4CLD2608_BPD_EN_AE)]] | Test script for scope item 3I1 Products for Retail (AE): creating retail article master data of all article types, info records, interfaces, discontinuation. |

### Retail Sites, Business Partners and Assortments

How store and DC sites and retail supplier and customer business partners are created, and how assortment modules assign products to stores and DCs.

| Node | Description |
| --- | --- |
| [[15-retail-operations/test-script-business-partners-for-retail-5fh-ae-sap-s-4hana-cloud-publ\|Test Script: Business Partners for Retail (5FH_AE) - SAP S/4HANA Cloud Public Edition (5FH_S4CLD2608_BPD_EN_AE)]] | Test script for Business Partners for Retail (5FH_AE): creating, extending and blocking supplier and customer master data in S/4HANA Cloud (UAE sample data). |
| [[15-retail-operations/sites-for-retail-3i3-ae-test-script-sap-s-4hana-cloud-public-edition-9\|Sites for Retail (3I3_AE) - Test Script, SAP S/4HANA Cloud Public Edition (3I3_S4CLD2608_BPD_EN_AE)]] | AE-localized test script for scope item 3I3 Sites for Retail in S/4HANA Cloud Public Edition 2608: creating DC/store sites, business partners, site groups, copy and blocking. |
| [[15-retail-operations/test-script-sap-s-4hana-cloud-public-edition-assortments-3i5-ae-945\|Test Script: SAP S/4HANA Cloud Public Edition - Assortments (3I5_AE) (3I5_S4CLD2608_BPD_EN_AE)]] | Test script for SAP S/4HANA Cloud scope item Assortments (3I5, AE): assortment modules, versions, product/store/DC assignment, plus optional steps. |

### Retail Sales Pricing and Promotions

How retail sales prices are calculated with markups and pricing worklists, and how retail promotions are created, sourced, priced, listed and activated.

| Node | Description |
| --- | --- |
| [[15-retail-operations/test-script-retail-promotions-637-ae-sap-s-4hana-cloud-public-edition\|Test Script: Retail Promotions (637_AE) - SAP S/4HANA Cloud Public Edition (637_S4CLD2608_BPD_EN_AE)]] | Test script for SAP S/4HANA Cloud Public Edition scope item Retail Promotions (637_AE): create promotion, supply source, prices, listing, allocation, jobs. |
| [[15-retail-operations/test-script-sales-pricing-for-retail-3i4-ae-sap-s-4hana-cloud-public-e\|Test Script: Sales Pricing for Retail (3I4_AE) - SAP S/4HANA Cloud Public Edition (3I4_S4CLD2608_BPD_EN_AE)]] | S/4HANA Cloud Public Edition test script for scope item 3I4_AE Sales Pricing for Retail: prerequisites, configuration and 38 pricing test procedures. |

### Store Connectivity (POS Inbound and Outbound)

How article and price master data replicate to store POS systems, and how POS sales, returns and payments are received, posted and monitored in AIF.

| Node | Description |
| --- | --- |
| [[15-retail-operations/store-connectivity-inbound-3hv-ae-test-script-sap-s-4hana-cloud-public\|Store Connectivity – Inbound (3HV_AE) Test Script, SAP S/4HANA Cloud Public Edition (3HV_S4CLD2608_BPD_EN_AE)]] | Test script for scope item 3HV: receiving POS sales, returns, payments and finance data via SOAP, scheduling posting jobs, AIF monitoring, sample payloads. |
| [[15-retail-operations/test-script-store-connectivity-outbound-3i2-ae-sap-s-4hana-cloud-publi\|Test Script: Store Connectivity – Outbound (3I2_AE), SAP S/4HANA Cloud Public Edition (3I2_S4CLD2608_BPD_EN_AE)]] | SAP S/4HANA Cloud Public Edition test script for scope item 3I2 (AE): replicating retail article master data and sales prices to store POS, initial and delta, with monitoring. |

### Omnichannel and In-Store Customer Order Fulfillment

How click-and-collect, click-and-reserve and in-store customer orders are picked, replenished and handed over in the store, or shipped from the DC.

| Node | Description |
| --- | --- |
| [[15-retail-operations/test-script-omnichannel-order-fulfillment-for-retail-5fz-ae-sap-s-4han\|Test Script: Omnichannel Order Fulfillment for Retail (5FZ_AE) - SAP S/4HANA Cloud Public Edition (5FZ_S4CLD2608_BPD_EN_AE)]] | SAP S/4HANA Cloud Public Edition test script for scope item 5FZ_AE: click-and-collect, click-and-reserve and DC-to-customer retail order fulfillment steps. |
| [[15-retail-operations/in-store-customer-order-management-3hu-ae-test-script-sap-s-4hana-clou\|In-Store Customer Order Management (3HU_AE) - Test Script, SAP S/4HANA Cloud Public Edition (3HU_S4CLD2608_BPD_EN_AE)]] | SAP test script for scope item 3HU_AE: in-store customer orders with immediate or later pickup, replenishment, picking, handover; prerequisites and sample data. |

### Retail Procurement, Invoice Verification and Supplier Returns

How retail purchase orders are created and monitored, supplier invoices verified by three-way matching, and merchandise returned to suppliers.

| Node | Description |
| --- | --- |
| [[15-retail-operations/test-script-procurement-for-retail-5fm-ae-sap-s-4hana-cloud-public-edi\|Test Script: Procurement for Retail (5FM_AE) - SAP S/4HANA Cloud Public Edition (5FM_S4CLD2608_BPD_EN_AE)]] | S/4HANA Cloud Public Edition test script, scope item 5FM_AE Procurement for Retail: PO creation, PR conversion, monitoring, EDI output, quantity optimization. |
| [[15-retail-operations/invoice-verification-for-retail-5fn-ae-test-script-sap-s-4hana-cloud-p\|Invoice Verification for Retail (5FN_AE) - Test Script, SAP S/4HANA Cloud Public Edition (5FN_S4CLD2608_BPD_EN_AE)]] | Test script for SAP S/4HANA Cloud scope item 5FN_AE: retail supplier invoice verification (three-way matching), incl. blocked, freight, background, API cases. |
| [[15-retail-operations/test-script-returns-to-supplier-for-retail-5fo-ae-sap-s-4hana-cloud-pu\|Test Script: Returns to Supplier for Retail (5FO_AE) - SAP S/4HANA Cloud Public Edition (5FO_S4CLD2608_BPD_EN_AE)]] | SAP S/4HANA Cloud test script for scope item 5FO_AE: retail returns to supplier, from returns PO to delivery, goods issue, then credit memo or replacement. |

### Merchandise Distribution and Allocation

How allocation tables and collective purchase orders push merchandise to stores via cross-docking, flow-through or put-away distribution.

| Node | Description |
| --- | --- |
| [[15-retail-operations/test-script-merchandise-allocation-5fl-ae-sap-s-4hana-cloud-public-edi\|Test Script: Merchandise Allocation (5FL_AE) - SAP S/4HANA Cloud Public Edition (5FL_S4CLD2608_BPD_EN_AE)]] | S/4HANA Cloud Public Edition retail test script, scope item 5FL: create, change, follow on and delete allocation tables to push merchandise to stores. |
| [[15-retail-operations/merchandise-distribution-and-collective-purchase-order-71o-ae-test-scr\|Merchandise Distribution and Collective Purchase Order (71O_AE) - Test Script, SAP S/4HANA Cloud Public Edition 2608 (71O_S4CLD2608_BPD_EN_AE)]] | SAP test script for scope item 71O_AE: collective purchase orders and merchandise distribution by cross-docking, flow-through and put-away, with prerequisites. |

### Replenishment Planning for Stores

How store forecasts and rapid replenishment runs create store replenishment orders through scheduled replenishment jobs.

| Node | Description |
| --- | --- |
| [[15-retail-operations/test-script-replenishment-planning-for-stores-3i7-ae-946\|Test Script: Replenishment Planning for Stores (3I7_AE) (3I7_S4CLD2608_BPD_EN_AE)]] | SAP S/4HANA Cloud Public Edition test script for scope item 3I7_AE: store replenishment (forecast run, rapid replenishment run, scheduled jobs). |

### Sales from Distribution Centers

How sales orders are fulfilled from a retail distribution center through delivery, picking, goods issue and billing, incl. debit memo, consignment and intercompany variants.

| Node | Description |
| --- | --- |
| [[15-retail-operations/sales-from-distribution-center-3hs-ae-test-script-sap-s-4hana-cloud-pu\|Sales from Distribution Center (3HS_AE) - Test Script, SAP S/4HANA Cloud Public Edition (3HS_S4CLD2608_BPD_EN_AE)]] | Test script for scope item 3HS_AE (UAE): sales from distribution center, debit memos, consignment, advanced intercompany sales; roles, apps, sample data, postings. |

### Inventory Management and Physical Inventory for Distribution Centers

How DC goods receipts, scrapping, stock transfers and blocking are posted, and physical inventory and cycle counts are run in distribution centers.

| Node | Description |
| --- | --- |
| [[15-retail-operations/test-script-inventory-management-for-distribution-centers-5fq-ae-sap-s\|Test Script: Inventory Management for Distribution Centers (5FQ_AE) - SAP S/4HANA Cloud Public Edition (5FQ_S4CLD2608_BPD_EN_AE)]] | SAP S/4HANA Cloud Public Edition test script for scope item 5FQ_AE: DC inventory goods receipt, scrapping, stock transfers, blocking and stock/material document display. |
| [[15-retail-operations/test-script-physical-inventory-for-distribution-centers-5fs-ae-sap-s-4\|Test Script: Physical Inventory for Distribution Centers (5FS_AE) - SAP S/4HANA Cloud Public Edition (5FS_S4CLD2608_BPD_EN_AE)]] | S/4HANA Cloud Public Edition 2608 test script for scope item 5FS_AE: prerequisites and steps for physical inventory and cycle counting in distribution centers. |

### Retail DC Warehouse Execution (Embedded EWM or Third-Party WMS)

How retail DC inbound, outbound, physical inventory, posting changes and replenishment run in embedded EWM or an integrated third-party WMS.

| Node | Description |
| --- | --- |
| [[15-retail-operations/test-script-retail-logistics-with-embedded-warehouse-management-69l-ae\|Test Script - Retail Logistics with Embedded Warehouse Management (69L_AE) (69L_S4CLD2608_BPD_EN_AE)]] | S/4HANA Cloud test script for scope item 69L_AE: embedded EWM inbound, outbound, physical inventory, posting changes, replenishment, prerequisites. |
| [[15-retail-operations/retail-logistics-with-third-party-warehouse-management-69m-ae-test-scr\|Retail Logistics with Third-Party Warehouse Management (69M_AE) - Test Script (69M_S4CLD2608_BPD_EN_AE)]] | SAP S/4HANA Cloud Public Edition 2608 test script for scope item 69M_AE: retail DC logistics integrated with a third-party WMS via SOAP web services. |

### Empties Management for Retail

How empties BOMs and prices are set up and empties handled in supplier procurement, returns, inventory and store order fulfillment for retail articles.

| Node | Description |
| --- | --- |
| [[15-retail-operations/empties-for-retail-5fk-ae-test-script-sap-s-4hana-cloud-public-edition-part-01\|Empties for Retail (5FK_AE) - Test Script, SAP S/4HANA Cloud Public Edition (5FK_S4CLD2608_BPD_EN_AE) — part 1 of 2]] | Test script for SAP S/4HANA Cloud scope item 5FK_AE Empties for Retail: prerequisites, master data, procurement, returns, inventory, store order fulfillment. |
| [[15-retail-operations/empties-for-retail-5fk-ae-test-script-sap-s-4hana-cloud-public-edition-part-02\|Empties for Retail (5FK_AE) - Test Script, SAP S/4HANA Cloud Public Edition (5FK_S4CLD2608_BPD_EN_AE) — part 2 of 2]] | SAP S/4HANA Cloud Public Edition test script for Empties for Retail (5FK_AE): prerequisites, master data, procurement and store/online sales flows with step-by-step test procedures. |

### Value-Added Services for Retail

How VAS service types, charge codes and pricing procedures are configured and applied to sales, purchasing and stock transfer documents.

| Node | Description |
| --- | --- |
| [[15-retail-operations/test-script-value-added-services-for-retail-6nm-ae-sap-s-4hana-cloud-p\|Test Script: Value-Added Services for Retail (6NM_AE), SAP S/4HANA Cloud Public Edition (6NM_S4CLD2608_BPD_EN_AE)]] | SAP test script for scope item 6NM_AE: configuring and testing retail value-added services (VAS) across sales, purchasing and stock transfer, with sample data and roles. |

## Related categories
- related-to :: [[11-inventory-warehouse-and-transportation/_cluster]]
- related-to :: [[08-sales-order-management/_cluster]]
