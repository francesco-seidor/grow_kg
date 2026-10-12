---
title: Solution Foundation and Platform
description: "SSCUI configuration activity list and process steps, org units, fiscal year variants, scope item links, and platform services: output, events, archiving, data privacy, migration, testing."
cluster: 01-solution-foundation-and-platform
type: cluster
tags: [kb/solution-foundation-and-platform, kb/hub]
keywords: [SSCUI, configuration activities, process steps, enterprise structure, org units, fiscal year variant, scope item, output management, business events, ILM, data privacy, CDS extraction, data migration, test automation, configuration, document management]
node_count: 119
created: 2026-10-12
updated: 2026-10-12
---

# Solution Foundation and Platform

Covers system-wide setup reference and technical/platform services used by every process. Reserved home for the SSCUI configuration-activity list and process-steps sheet (incremental). Excludes business partner and product records (see 02), G/L accounts (see 03), country tax codes (see 04) and HQ-subsidiary integration (see 16).

Every node below is the verbatim text of one source document (or one part of a long one), grouped by topic.

## Nodes

### Best Practices Scope Item and Test Script Link Index

Where to find set-up instructions and test scripts per scope item and solution scenario for the UAE (AE) 2608 package.

| Node | Description |
| --- | --- |
| [[01-solution-foundation-and-platform/readme-2608\|README (README)]] | README for the downloaded SAP Best Practices ZIP: explains the packExcel folder (links/URLs) and the scenario-specific Library folder (S4C, IBP) holding the assets. |
| [[01-solution-foundation-and-platform/s4c-2608-ae-links-1313\|S4C 2608 AE links (S4C_2608_AE_links)]] | Link index (xlsx) for SAP S/4HANA Cloud Public Edition 2608 Best Practices, UAE (AE) pack: scenario links plus per-scope-item set-up instructions and test script URLs. |

### Business Event Handling with Event Mesh

How to test business event integration from S/4HANA Cloud to SAP Event Mesh and Advanced Event Mesh, including channel and topic setup.

| Node | Description |
| --- | --- |
| [[01-solution-foundation-and-platform/test-script-business-event-handling-1nn-748\|Test Script: Business Event Handling (1NN) (1NN_S4CLD2608_BPD_EN_XX)]] | SAP S/4HANA Cloud Public Edition test script for scope item 1NN: testing business event integration with Event Mesh and Advanced Event Mesh. |

### CDS-Based Data Extraction to BW, Datasphere, Data Intelligence, HANA and SAC

How to extract ABAP CDS view data from S/4HANA Cloud to BW/4HANA, SAP Datasphere, Data Intelligence, SAP HANA or an SAP Analytics Cloud import connection.

| Node | Description |
| --- | --- |
| [[01-solution-foundation-and-platform/test-script-abap-core-data-services-extraction-for-sap-datasphere-53l\|Test Script: ABAP Core Data Services Extraction for SAP Datasphere (53L) (53L_S4CLD2608_BPD_EN_XX)]] | Test script for scope item 53L: extracting ABAP CDS views from S/4HANA Cloud Public Edition 2608 into SAP Datasphere via views, data flows, entity import and replication flows. |
| [[01-solution-foundation-and-platform/test-script-abap-core-data-services-extraction-for-sap-data-intelligen\|Test Script: ABAP Core Data Services Extraction for SAP Data Intelligence (53M) (53M_S4CLD2608_BPD_EN_XX)]] | Test script for scope item 53M: extracting ABAP CDS view data from S/4HANA Cloud Public Edition to SAP Data Intelligence via pipelines and replication flows. |
| [[01-solution-foundation-and-platform/abap-core-data-services-extraction-for-sap-hana-6n4-test-script-1179\|ABAP Core Data Services Extraction for SAP HANA (6N4) - Test Script (6N4_S4CLD2608_BPD_EN_XX)]] | Test script (6N4) for replicating ABAP CDS views from S/4HANA Cloud Public Edition to SAP HANA via a Replication Task in SAP Web IDE. |
| [[01-solution-foundation-and-platform/import-connection-setup-with-sap-analytics-cloud-1yb-786\|Import Connection Setup with SAP Analytics Cloud (1YB) (1YB_S4CLD2608_BPD_EN_XX)]] | Test script (1YB) for loading S/4HANA master data into an SAP Analytics Cloud public dimension via OData import connection. |
| [[01-solution-foundation-and-platform/cds-based-extraction-with-sap-s-4hana-cloud-public-edition-35d-test-sc\|CDS-Based Extraction with SAP S/4HANA Cloud Public Edition (35D) - Test Script (35D_S4CLD2608_BPD_EN_XX)]] | SAP test script for scope item 35D: verifying CDS-based data extraction via ODP from S/4HANA Cloud Public Edition to BW/4HANA (source system, data flow, extracted data). |

### Data Migration with the Migration Cockpit (Direct Transfer and Staging Tables)

How data is migrated with the migration cockpit, directly from an SAP source system (BH3) or via staging tables (2Q2): project setup, selection, mapping, simulation, monitoring.

| Node | Description |
| --- | --- |
| [[01-solution-foundation-and-platform/test-script-data-migration-to-sap-s-4hana-from-sap-bh3-1268\|Test Script: Data Migration to SAP S/4HANA from SAP (BH3) (BH3_S4CLD2608_BPD_EN_XX)]] | SAP S/4HANA Cloud Public Edition test script (BH3) for migrating data directly from an SAP source system with the migration cockpit: role setup, steps, validation. |
| [[01-solution-foundation-and-platform/test-script-data-migration-to-sap-s-4hana-from-staging-2q2-848\|Test Script: Data Migration to SAP S/4HANA from Staging (2Q2) (2Q2_S4CLD2608_BPD_EN_XX)]] | S/4HANA Cloud Public Edition test script (scope item 2Q2): migrating data via staging tables with the migration cockpit, plus roles and finance/logistics notes. |

### SAP Document AI Integration

How to check Document AI schema registration subscriptions (F8996) and activate or deactivate Document AI document extraction.

| Node | Description |
| --- | --- |
| [[01-solution-foundation-and-platform/test-script-integration-with-sap-document-ai-7tc-1225\|Test Script: Integration with SAP Document AI (7TC) (7TC_S4CLD2608_BPD_EN_XX)]] | SAP S/4HANA Cloud 2608 test script (7TC) for checking the Manage Document AI Schema Registration Subscriptions app (F8996) and activating/deactivating schemas. |

### Document Info Records and Attachment Services

How to manage document info records and upload/download attachments via SAP Document Management service or OpenText archiving, content and Extended ECM.

| Node | Description |
| --- | --- |
| [[01-solution-foundation-and-platform/test-script-sap-archiving-and-document-access-core-by-opentext-integra\|Test Script - SAP Archiving and Document Access Core by OpenText Integration (7W6) (7W6_S4CLD2608_BPD_EN_XX)]] | SAP S/4HANA Cloud Public Edition test script (7W6) for uploading and downloading attachments via OpenText archiving integration, at business-object level and in Manage Documents. |
| [[01-solution-foundation-and-platform/sap-content-management-core-by-opentext-integration-7wc-test-script-12\|SAP Content Management Core by OpenText Integration (7WC) - Test Script (7WC_S4CLD2608_BPD_EN_XX)]] | SAP S/4HANA Cloud Public Edition test script for scope item 7WC: uploading and downloading attachments via OpenText integration, at business-object level and in Manage Documents. |
| [[01-solution-foundation-and-platform/test-script-sap-document-management-service-integration-7xy-1234\|Test Script - SAP Document Management Service Integration (7XY) (7XY_S4CLD2608_BPD_EN_XX)]] | SAP S/4HANA Cloud Public Edition test script (7XY) for uploading and downloading attachments via SAP Document Management service on SAP BTP. |
| [[01-solution-foundation-and-platform/test-script-sap-extended-ecm-by-opentext-integration-7y0-1235\|Test Script: SAP Extended ECM by OpenText Integration (7Y0) (7Y0_S4CLD2608_BPD_EN_XX)]] | Test script for scope item 7Y0 on SAP S/4HANA Cloud Public Edition 2608: uploading and downloading attachments via business objects (Product) and the Manage Documents app. |
| [[01-solution-foundation-and-platform/test-script-manage-documents-22p-ae-sap-s-4hana-cloud-public-edition-8\|Test Script: Manage Documents (22P_AE) - SAP S/4HANA Cloud Public Edition (22P_S4CLD2608_BPD_EN_AE)]] | SAP S/4HANA Cloud Public Edition test script for scope item 22P_AE: managing Document Info Records (search, create, version, classify, release, download) as Design Engineer. |

### EDI and API Field Extensibility

How to add custom fields to EDI-based SOAP APIs and IDocs (sales order example) and monitor messages in AIF.

| Node | Description |
| --- | --- |
| [[01-solution-foundation-and-platform/edi-extensibility-customer-guide-229\|EDI Extensibility Customer Guide (S4CLD2608_2T_ EDI Extensibility_User_Guide_EN)]] | Customer guide for adding custom fields to EDI-based SOAP APIs and IDocs in SAP Cloud ERP, with a Sales Order example, prerequisites and AIF monitoring. |

### Enterprise Contract Assembly Integration

How legal counsel authors and assembles legal documents with SAP Enterprise Contract Assembly: areas, document variables, creating and managing legal documents.

| Node | Description |
| --- | --- |
| [[01-solution-foundation-and-platform/test-script-integration-to-icertis-for-contract-assembly-6v2-sap-s-4ha\|Test Script: Integration to Icertis for Contract Assembly (6V2) - SAP S/4HANA Cloud Public Edition (6V2_S4CLD2608_BPD_EN_XX)]] | SAP test script for scope item 6V2: Icertis integration with Enterprise Contract Management; prerequisites, configuration, legal document and signature tests. |
| [[01-solution-foundation-and-platform/test-script-sap-s-4hana-cloud-public-edition-sap-s-4hana-for-enterpris\|Test Script - SAP S/4HANA Cloud Public Edition: SAP S/4HANA for Enterprise Contract Management (1XV) (1XV_S4CLD2608_BPD_EN_XX)]] | SAP S/4HANA Cloud Public Edition 2608 test script for scope item 1XV Enterprise Contract Management: roles, configuration UIs and 9 test procedures. |
| [[01-solution-foundation-and-platform/test-script-integration-to-sap-enterprise-contract-assembly-2oq-846\|Test Script: Integration to SAP Enterprise Contract Assembly (2OQ) (2OQ_S4CLD2608_BPD_EN_XX)]] | SAP S/4HANA Cloud Public Edition test script for scope item 2OQ: ECA integration setup (areas, document variables) and creating/managing legal documents. |

### Enterprise Structure and Organizational Units

Which org units (company codes, plants, sales areas, storage locations) the best-practice content uses, naming conventions and country codes.

| Node | Description |
| --- | --- |
| [[01-solution-foundation-and-platform/2608-org-data-overview-en-xx-121\|2608 Org Data Overview EN XX (2608_Org_Data_Overview_EN_XX)]] | Workbook of SAP S/4HANA Cloud 2608 enterprise structure naming conventions (global and retail) for org units, with building-block origins and a hidden sample data sheet. |

### Predelivered Fiscal Year Variants

Which fiscal year variants are predelivered in 2608, their periods and special periods, and which can be used as corporate FYV.

| Node | Description |
| --- | --- |
| [[01-solution-foundation-and-platform/2608-predelivered-fyv-253\|2608 predelivered FYV (2608_predelivered_FYV)]] | Reference table of fiscal year variants predelivered in SAP S/4HANA Cloud Public Edition 2608: periods, special periods, corporate FYV eligibility, origin and remarks. |

### Risk, Control and Privacy Monitoring (SAP Risk and Assurance Management)

How key risk indicators, automated control procedures, work packages and privacy risk detection run with SAP Risk Management and Risk and Assurance Management.

| Node | Description |
| --- | --- |
| [[01-solution-foundation-and-platform/test-script-continuous-control-monitoring-with-sap-process-control-2oh\|Test Script: Continuous Control Monitoring with SAP Process Control (2OH) (2OH_S4CLD2608_BPD_EN_XX)]] | S/4HANA Cloud Public Edition test script, scope item 2OH: SAP Process Control data sources, business rules and ad-hoc queries for continuous control monitoring. |
| [[01-solution-foundation-and-platform/test-script-key-risk-indicator-monitoring-with-sap-risk-management-2u2\|Test Script: Key Risk Indicator Monitoring with SAP Risk Management (2U2) (2U2_S4CLD2608_BPD_EN_XX)]] | SAP S/4HANA Cloud Public Edition test script for 2U2: creating KRI templates, implementations and risks in on-premise SAP Risk Management and checking threshold violations. |
| [[01-solution-foundation-and-platform/test-script-privacy-risk-detection-with-sap-risk-and-assurance-managem\|Test Script: Privacy Risk Detection with SAP Risk and Assurance Management (3KX) (3KX_S4CLD2608_BPD_EN_XX)]] | Test script for scope item 3KX on SAP S/4HANA Cloud Public Edition: creating automated procedures, controls and work packages to detect privacy risks, e.g. in sales orders. |
| [[01-solution-foundation-and-platform/test-script-control-monitoring-with-sap-risk-and-assurance-management\|Test Script: Control Monitoring with SAP Risk and Assurance Management (3KY) (3KY_S4CLD2608_BPD_EN_XX)]] | SAP S/4HANA Cloud Public Edition 2608 test script for scope item 3KY: automated procedures, controls, work packages, run results and issues in SAP Risk and Assurance Management. |

### In-App User Assistance (SAP Enable Now and WalkMe)

How to customize, publish and revert Web Assistant help content with SAP Enable Now or WalkMe Premium in the Fiori launchpad.

| Node | Description |
| --- | --- |
| [[01-solution-foundation-and-platform/walkme-premium-integration-7te-test-script-1226\|WalkMe Premium Integration (7TE) Test Script (7TE_S4CLD2608_BPD_EN_XX)]] | SAP Best Practices test script for the WalkMe Premium Integration scope item (7TE): customizing and publishing user assistant content in S/4HANA Cloud Public Edition. |
| [[01-solution-foundation-and-platform/test-script-sap-enable-now-integration-3n5-962\|Test Script: SAP Enable Now Integration (3N5) (3N5_S4CLD2608_BPD_EN_XX)]] | SAP S/4HANA Cloud Public Edition test script for SAP Enable Now integration: customizing, adding, publishing and reverting Web Assistant user assistance content. |

### Information Lifecycle Management and Data Protection

How ILM audit areas, retention rules, archiving and destruction work, and how personal data is blocked, deleted, reported and access-logged.

| Node | Description |
| --- | --- |
| [[01-solution-foundation-and-platform/test-script-sap-s-4hana-cloud-public-edition-data-protection-and-priva\|Test Script: SAP S/4HANA Cloud Public Edition - Data Protection and Privacy (5LE_AE) (5LE_S4CLD2608_BPD_EN_AE)]] | SAP test script for scope item 5LE (AE): ILM-based blocking/deletion, information retrieval, consent administration and read access logging in S/4HANA Cloud Public Edition 2608. |
| [[01-solution-foundation-and-platform/data-protection-and-privacy-data-controller-and-purpose-6n9-ae-1180\|Data Protection and Privacy – Data Controller and Purpose (6N9_AE) (6N9_S4CLD2608_BPD_EN_AE)]] | SAP S/4HANA Cloud Public Edition test script for scope item 6N9: assigning data controllers and purposes to business partners and testing access restrictions. |
| [[01-solution-foundation-and-platform/test-script-information-lifecycle-management-1ka-sap-s-4hana-cloud-pub\|Test Script: Information Lifecycle Management (1KA), SAP S/4HANA Cloud Public Edition (1KA_S4CLD2608_BPD_EN_XX)]] | SAP test script for scope item 1KA Information Lifecycle Management: audit areas, ILM rules, rule generator, archiving, data destruction and file conversion steps. |

### Output Management and External Output Systems

How output control and output management apps are checked and configured, and how output items reach an external output management solution.

| Node | Description |
| --- | --- |
| [[01-solution-foundation-and-platform/test-script-integration-of-external-output-management-solution-7dj-120\|Test Script: Integration of External Output Management Solution (7DJ) (7DJ_S4CLD2608_BPD_EN_XX)]] | SAP S/4HANA Cloud Public Edition test script (scope item 7DJ) for creating an output queue and test item and verifying transmission to an external output management target. |
| [[01-solution-foundation-and-platform/bp-cld-entpr-2608-forms-list-en-ae-134\|BP CLD ENTPR 2608 Forms List EN AE (BP_CLD_ENTPR_2608_Forms_List_EN_AE)]] | Spreadsheet of 269 Adobe form templates for SAP S/4HANA Cloud Public Edition 2608 (AE): application object, output type, callback class, scope and use codes. |
| [[01-solution-foundation-and-platform/test-script-output-management-1lq-733\|Test Script: Output Management (1LQ) (1LQ_S4CLD2608_BPD_EN_XX)]] | SAP S/4HANA Cloud Public Edition test script for scope item 1LQ: checking availability of output management and output control apps and configuration steps. |

### Predictive Analytics Model Training for Sales and Supply Chain

How to train and activate predictive models (intelligent scenarios) for quotation conversion, delivery delay, overdue stock in transit and demand-driven replenishment.

| Node | Description |
| --- | --- |
| [[01-solution-foundation-and-platform/predictive-analytics-model-training-supply-chain-20n-test-script-795\|Predictive Analytics Model Training – Supply Chain (20N) Test Script (20N_S4CLD2608_BPD_EN_XX)]] | SAP S/4HANA Cloud Public Edition test script for scope item 20N: train and activate predictive models and check overdue stock in transit and demand-driven replenishment. |
| [[01-solution-foundation-and-platform/predictive-analytics-model-training-sales-2yj-888\|Predictive Analytics Model Training – Sales (2YJ) (2YJ_S4CLD2608_BPD_EN_XX)]] | SAP S/4HANA Cloud 2608 test script 2YJ: train and activate predictive models and test Quotation Conversion Rates, Sales Performance and Predicted Delivery Delay apps. |

### Test Automation Tool

How to build test processes and plans, manage test data, run post-upgrade tests and analyze results with the Test Automation Tool.

| Node | Description |
| --- | --- |
| [[01-solution-foundation-and-platform/test-automation-tool-for-sap-s-4hana-public-cloud-86c-test-script-1246\|Test Automation Tool for SAP S/4HANA Public Cloud (86C) - Test Script (86C_S4CLD2608_BPD_EN_XX)]] | Test script for the Test Automation Tool (86C) in SAP S/4HANA Cloud Public Edition 2608: test processes, plans, test data, post-upgrade tests and results. |

### Self-Service Configuration (SSCUI) Activity List

Which self-service configuration activities (SSCUIs) exist in 2608 by application area, with configuration item IDs, scope item, country dependency, category and component.

| Node | Description |
| --- | --- |
| [[01-solution-foundation-and-platform/sscui-list-en-xx-sap-s-4hana-cloud-2608-configuration-2-part-01\|SSCUI List EN XX (SAP S/4HANA Cloud 2608 Configuration) (SSCUI_List_EN_XX) — part 1 of 40]] | Part 1 of 40: SAP S/4HANA Cloud Public Edition 2608 list of self-service configuration (SSCUI) activities by application area, scope item, country scope, category and component. |
| [[01-solution-foundation-and-platform/sscui-list-en-xx-sap-s-4hana-cloud-2608-configuration-2-part-02\|SSCUI List EN XX (SAP S/4HANA Cloud 2608 Configuration) (SSCUI_List_EN_XX) — part 2 of 40]] | SAP S/4HANA Cloud Public Edition 2608 SSCUI list: configuration activities by area with category, scope items, country scope and application component. |
| [[01-solution-foundation-and-platform/sscui-list-en-xx-sap-s-4hana-cloud-2608-configuration-2-part-03\|SSCUI List EN XX (SAP S/4HANA Cloud 2608 Configuration) (SSCUI_List_EN_XX) — part 3 of 40]] | SSCUI list for SAP S/4HANA Cloud Public Edition 2608: configuration steps by area, scope item, country scope and Mandatory/Recommended/Optional status. |
| [[01-solution-foundation-and-platform/sscui-list-en-xx-sap-s-4hana-cloud-2608-configuration-2-part-04\|SSCUI List EN XX (SAP S/4HANA Cloud 2608 Configuration) (SSCUI_List_EN_XX) — part 4 of 40]] | Part 4 of 40: SAP S/4HANA Cloud Public Edition 2608 list of self-service configuration (SSCUI) activities by application area, scope item, country scope, category and component. |
| [[01-solution-foundation-and-platform/sscui-list-en-xx-sap-s-4hana-cloud-2608-configuration-2-part-05\|SSCUI List EN XX (SAP S/4HANA Cloud 2608 Configuration) (SSCUI_List_EN_XX) — part 5 of 40]] | SAP S/4HANA Cloud 2608 SSCUI catalogue: one row per configuration activity with category, scope items, country scope, table ID, component (segment 5 of 40). |
| [[01-solution-foundation-and-platform/sscui-list-en-xx-sap-s-4hana-cloud-2608-configuration-2-part-06\|SSCUI List EN XX (SAP S/4HANA Cloud 2608 Configuration) (SSCUI_List_EN_XX) — part 6 of 40]] | SAP S/4HANA Cloud Public Edition 2608 SSCUI list; this slice: contract and lease, JV, EWM, trade, tax and eDocument configuration activities. |
| [[01-solution-foundation-and-platform/sscui-list-en-xx-sap-s-4hana-cloud-2608-configuration-2-part-07\|SSCUI List EN XX (SAP S/4HANA Cloud 2608 Configuration) (SSCUI_List_EN_XX) — part 7 of 40]] | SAP S/4HANA Cloud Public Edition 2608 SSCUI list of self-service configuration activities by application area, scope item, country scope and category. |
| [[01-solution-foundation-and-platform/sscui-list-en-xx-sap-s-4hana-cloud-2608-configuration-2-part-08\|SSCUI List EN XX (SAP S/4HANA Cloud 2608 Configuration) (SSCUI_List_EN_XX) — part 8 of 40]] | SSCUI configuration-activity catalogue for SAP S/4HANA Cloud Public Edition 2608 (sheet 2608); segment 8 of 40 covers 194 activities, mostly Finance. |
| [[01-solution-foundation-and-platform/sscui-list-en-xx-sap-s-4hana-cloud-2608-configuration-2-part-09\|SSCUI List EN XX (SAP S/4HANA Cloud 2608 Configuration) (SSCUI_List_EN_XX) — part 9 of 40]] | SSCUI configuration-activity catalogue, SAP S/4HANA Cloud Public Edition 2608; segment 9 of 40 lists 247 activities (Finance, PLM integration, localization). |
| [[01-solution-foundation-and-platform/sscui-list-en-xx-sap-s-4hana-cloud-2608-configuration-2-part-10\|SSCUI List EN XX (SAP S/4HANA Cloud 2608 Configuration) (SSCUI_List_EN_XX) — part 10 of 40]] | SSCUI configuration-activity catalogue, SAP S/4HANA Cloud Public Edition 2608; segment 10 of 40 lists 434 activities (tax/eDocument localization, EHS). |
| [[01-solution-foundation-and-platform/sscui-list-en-xx-sap-s-4hana-cloud-2608-configuration-2-part-11\|SSCUI List EN XX (SAP S/4HANA Cloud 2608 Configuration) (SSCUI_List_EN_XX) — part 11 of 40]] | SAP S/4HANA Cloud 2608 SSCUI configuration catalogue (segment 11 of 40): activities with category, scope items, country, component and table IDs. |
| [[01-solution-foundation-and-platform/sscui-list-en-xx-sap-s-4hana-cloud-2608-configuration-2-part-12\|SSCUI List EN XX (SAP S/4HANA Cloud 2608 Configuration) (SSCUI_List_EN_XX) — part 12 of 40]] | SSCUI list for SAP S/4HANA Cloud Public Edition 2608: each configuration step with rating, scope items, country scope, component and deletion support. |
| [[01-solution-foundation-and-platform/sscui-list-en-xx-sap-s-4hana-cloud-2608-configuration-2-part-13\|SSCUI List EN XX (SAP S/4HANA Cloud 2608 Configuration) (SSCUI_List_EN_XX) — part 13 of 40]] | SAP S/4HANA Cloud release 2608 catalogue of SSCUI configuration steps: area, importance, scope items, country scope, IMG activity and component per step (segment 13/40). |
| [[01-solution-foundation-and-platform/sscui-list-en-xx-sap-s-4hana-cloud-2608-configuration-2-part-14\|SSCUI List EN XX (SAP S/4HANA Cloud 2608 Configuration) (SSCUI_List_EN_XX) — part 14 of 40]] | SAP S/4HANA Cloud 2608 SSCUI configuration catalogue, one row per activity: category, scope items, country scope, component. This slice: rows 2903-3272. |
| [[01-solution-foundation-and-platform/sscui-list-en-xx-sap-s-4hana-cloud-2608-configuration-2-part-15\|SSCUI List EN XX (SAP S/4HANA Cloud 2608 Configuration) (SSCUI_List_EN_XX) — part 15 of 40]] | SSCUI configuration-activity catalogue, SAP S/4HANA Cloud 2608; segment 15 of 40 lists 270 activities (Treasury, Warehouse Mgmt, Withholding Tax, Retail, Brazil NF-e). |
| [[01-solution-foundation-and-platform/sscui-list-en-xx-sap-s-4hana-cloud-2608-configuration-2-part-16\|SSCUI List EN XX (SAP S/4HANA Cloud 2608 Configuration) (SSCUI_List_EN_XX) — part 16 of 40]] | SAP S/4HANA Cloud Public Edition 2608 SSCUI list: configuration activities with category, scope items, country scope, component, deletion support. |
| [[01-solution-foundation-and-platform/sscui-list-en-xx-sap-s-4hana-cloud-2608-configuration-2-part-17\|SSCUI List EN XX (SAP S/4HANA Cloud 2608 Configuration) (SSCUI_List_EN_XX) — part 17 of 40]] | Part 17 of 40: SSCUI configuration-step catalogue, SAP S/4HANA Cloud Public Edition 2608: area, ID, title, Mandatory/Optional, scope items, countries, component. |
| [[01-solution-foundation-and-platform/sscui-list-en-xx-sap-s-4hana-cloud-2608-configuration-2-part-18\|SSCUI List EN XX (SAP S/4HANA Cloud 2608 Configuration) (SSCUI_List_EN_XX) — part 18 of 40]] | SAP S/4HANA Cloud 2608 SSCUI configuration list (part 18 of 40): activities with category, scope items, country scope, component and deprecation status. |
| [[01-solution-foundation-and-platform/sscui-list-en-xx-sap-s-4hana-cloud-2608-configuration-2-part-19\|SSCUI List EN XX (SAP S/4HANA Cloud 2608 Configuration) (SSCUI_List_EN_XX) — part 19 of 40]] | SSCUI list (sheet 2608) for SAP S/4HANA Cloud Public Edition: configuration activities per area with scope items, mandatory/optional category, deprecation flags |
| [[01-solution-foundation-and-platform/sscui-list-en-xx-sap-s-4hana-cloud-2608-configuration-2-part-20\|SSCUI List EN XX (SAP S/4HANA Cloud 2608 Configuration) (SSCUI_List_EN_XX) — part 20 of 40]] | Part 20 of 40: SSCUI configuration-step catalogue, SAP S/4HANA Cloud Public Edition 2608: area, ID, title, Mandatory/Optional, scope items, countries, component. |
| [[01-solution-foundation-and-platform/sscui-list-en-xx-sap-s-4hana-cloud-2608-configuration-2-part-21\|SSCUI List EN XX (SAP S/4HANA Cloud 2608 Configuration) (SSCUI_List_EN_XX) — part 21 of 40]] | SSCUI List (2608) shared-values legend V40-V70: long lists of scope item names and 3-character scope item IDs that sheet rows reference as ⟦Vn⟧. |
| [[01-solution-foundation-and-platform/sscui-list-en-xx-sap-s-4hana-cloud-2608-configuration-2-part-22\|SSCUI List EN XX (SAP S/4HANA Cloud 2608 Configuration) (SSCUI_List_EN_XX) — part 22 of 40]] | SSCUI List workbook, Sheet 2608: this slice is shared-values legend V71-V105, comma-separated lists of SAP scope item names and scope item ID codes. |
| [[01-solution-foundation-and-platform/sscui-list-en-xx-sap-s-4hana-cloud-2608-configuration-2-part-23\|SSCUI List EN XX (SAP S/4HANA Cloud 2608 Configuration) (SSCUI_List_EN_XX) — part 23 of 40]] | Slice 23/40 of the SSCUI list (S/4HANA Cloud Public Edition 2608 config library): shared-values legend V106-V143, lists of scope item names and scope item IDs. |
| [[01-solution-foundation-and-platform/sscui-list-en-xx-sap-s-4hana-cloud-2608-configuration-2-part-24\|SSCUI List EN XX (SAP S/4HANA Cloud 2608 Configuration) (SSCUI_List_EN_XX) — part 24 of 40]] | Slice of SSCUI List EN XX, sheet 2608 shared-values legend V144-V179: comma-joined lists of SAP scope item names and 3-character codes cited by ⟦Vn⟧ cells. |
| [[01-solution-foundation-and-platform/sscui-list-en-xx-sap-s-4hana-cloud-2608-configuration-2-part-25\|SSCUI List EN XX (SAP S/4HANA Cloud 2608 Configuration) (SSCUI_List_EN_XX) — part 25 of 40]] | SSCUI List EN XX, SAP S/4HANA Cloud 2608 configuration list: this slice is the shared-values legend V180-V212 (scope item name lists and scope item ID lists). |
| [[01-solution-foundation-and-platform/sscui-list-en-xx-sap-s-4hana-cloud-2608-configuration-2-part-26\|SSCUI List EN XX (SAP S/4HANA Cloud 2608 Configuration) (SSCUI_List_EN_XX) — part 26 of 40]] | SAP S/4HANA Cloud 2608 configuration (SSCUI) list; this slice is the shared-values legend V213-V242: scope item name lists and 3-character scope item ID lists. |
| [[01-solution-foundation-and-platform/sscui-list-en-xx-sap-s-4hana-cloud-2608-configuration-2-part-27\|SSCUI List EN XX (SAP S/4HANA Cloud 2608 Configuration) (SSCUI_List_EN_XX) — part 27 of 40]] | SSCUI List EN XX (S/4HANA Cloud Public Edition 2608): this slice is shared-values legend V243-V271, comma-joined scope item names and 3-char scope item IDs. |
| [[01-solution-foundation-and-platform/sscui-list-en-xx-sap-s-4hana-cloud-2608-configuration-2-part-28\|SSCUI List EN XX (SAP S/4HANA Cloud 2608 Configuration) (SSCUI_List_EN_XX) — part 28 of 40]] | Segment 28/40 of the SSCUI list (S/4HANA Cloud Public Edition 2608): shared-values legend V272-V306, comma lists of scope item names and IDs for sheet cells. |
| [[01-solution-foundation-and-platform/sscui-list-en-xx-sap-s-4hana-cloud-2608-configuration-2-part-29\|SSCUI List EN XX (SAP S/4HANA Cloud 2608 Configuration) (SSCUI_List_EN_XX) — part 29 of 40]] | SSCUI List (sheet 2608) shared-values legend V307-V341: comma-separated SAP scope-item name lists (finance, logistics, production, service) and 3-char codes. |
| [[01-solution-foundation-and-platform/sscui-list-en-xx-sap-s-4hana-cloud-2608-configuration-2-part-30\|SSCUI List EN XX (SAP S/4HANA Cloud 2608 Configuration) (SSCUI_List_EN_XX) — part 30 of 40]] | SSCUI List EN XX, SAP S/4HANA Cloud 2608 configuration list: this slice is the end of the shared-values legend, V342-V369 (scope item name lists and scope item ID lists). |
| [[01-solution-foundation-and-platform/sscui-list-en-xx-sap-s-4hana-cloud-2608-configuration-2-part-31\|SSCUI List EN XX (SAP S/4HANA Cloud 2608 Configuration) (SSCUI_List_EN_XX) — part 31 of 40]] | SSCUI list workbook (SAP S/4HANA Cloud Public Edition 2608); this segment is the shared-values legend V370-V395: repeated lists of scope item names and codes. |
| [[01-solution-foundation-and-platform/sscui-list-en-xx-sap-s-4hana-cloud-2608-configuration-2-part-32\|SSCUI List EN XX (SAP S/4HANA Cloud 2608 Configuration) (SSCUI_List_EN_XX) — part 32 of 40]] | SSCUI List workbook, sheet 2608, part 32/40: shared-values legend V396-V434, comma lists of SAP scope item names and three-character scope item codes. |
| [[01-solution-foundation-and-platform/sscui-list-en-xx-sap-s-4hana-cloud-2608-configuration-2-part-33\|SSCUI List EN XX (SAP S/4HANA Cloud 2608 Configuration) (SSCUI_List_EN_XX) — part 33 of 40]] | SSCUI List EN XX, SAP S/4HANA Cloud 2608 config list: slice ends the shared-values legend (V435-V457), opens sheet 'IMG Activity TRAN in BC'. |
| [[01-solution-foundation-and-platform/sscui-list-en-xx-sap-s-4hana-cloud-2608-configuration-2-part-34\|SSCUI List EN XX (SAP S/4HANA Cloud 2608 Configuration) (SSCUI_List_EN_XX) — part 34 of 40]] | SSCUI List EN XX (S/4HANA Cloud 2608), segment 34: rows of sheet 'IMG Activity TRAN in BC' mapping business catalogs and tcodes to IMG activities and SSCUI IDs. |
| [[01-solution-foundation-and-platform/sscui-list-en-xx-sap-s-4hana-cloud-2608-configuration-2-part-35\|SSCUI List EN XX (SAP S/4HANA Cloud 2608 Configuration) (SSCUI_List_EN_XX) — part 35 of 40]] | Segment 35/40 of the SSCUI list: 'IMG Activity TRAN in BC' rows mapping SAP business catalogs to transaction codes, IAM app IDs, IMG activities, SSCUI IDs. |
| [[01-solution-foundation-and-platform/sscui-list-en-xx-sap-s-4hana-cloud-2608-configuration-2-part-36\|SSCUI List EN XX (SAP S/4HANA Cloud 2608 Configuration) (SSCUI_List_EN_XX) — part 36 of 40]] | SSCUI list segment 36/40 (S/4HANA Cloud 2608): business catalog rows mapping transaction codes to IMG activities, SSCUI IDs, components (EWM, FI-CA, RE-FX). |
| [[01-solution-foundation-and-platform/sscui-list-en-xx-sap-s-4hana-cloud-2608-configuration-2-part-37\|SSCUI List EN XX (SAP S/4HANA Cloud 2608 Configuration) (SSCUI_List_EN_XX) — part 37 of 40]] | Spreadsheet list of SAP S/4HANA Cloud Public Edition SSCUI configuration activities by business configuration set; this slice covers FI-CA, CINV, SD, MRP, AR. |
| [[01-solution-foundation-and-platform/sscui-list-en-xx-sap-s-4hana-cloud-2608-configuration-2-part-38\|SSCUI List EN XX (SAP S/4HANA Cloud 2608 Configuration) (SSCUI_List_EN_XX) — part 38 of 40]] | SAP S/4HANA Cloud 2608 SSCUI list workbook; this slice maps business catalogs and transaction codes to IMG activities, SSCUI IDs and components. |
| [[01-solution-foundation-and-platform/sscui-list-en-xx-sap-s-4hana-cloud-2608-configuration-2-part-39\|SSCUI List EN XX (SAP S/4HANA Cloud 2608 Configuration) (SSCUI_List_EN_XX) — part 39 of 40]] | SSCUI list workbook, segment 39/40: 'IMG Activity TRAN in BC' rows mapping business catalogs and transaction codes to IMG activities, SSCUI IDs, components. |
| [[01-solution-foundation-and-platform/sscui-list-en-xx-sap-s-4hana-cloud-2608-configuration-2-part-40\|SSCUI List EN XX (SAP S/4HANA Cloud 2608 Configuration) (SSCUI_List_EN_XX) — part 40 of 40]] | SAP S/4HANA Cloud 2608 SSCUI list; final part: business catalog to IMG activity mappings plus expert-configuration incident templates. |

### Scope Item Availability, Prerequisites and Process Steps

Which scope items are available per country, their prerequisites, bundles and required master data, and which process steps, Fiori apps and business roles each uses.

| Node | Description |
| --- | --- |
| [[01-solution-foundation-and-platform/availability-dependencies-en-xx-131-part-01\|Availability Dependencies EN XX (Availability_Dependencies_EN_XX) — part 1 of 3]] | Scope item matrix for SAP S/4HANA Cloud Public Edition 2608: provisioning, bundles, prerequisites, master data and release per country (part 1 of 3). |
| [[01-solution-foundation-and-platform/availability-dependencies-en-xx-131-part-02\|Availability Dependencies EN XX (Availability_Dependencies_EN_XX) — part 2 of 3]] | SAP S/4HANA Cloud Public Edition 2608 scope-item availability and dependency matrix, part 2 of 3: Manufacturing to Sourcing and Procurement rows. |
| [[01-solution-foundation-and-platform/availability-dependencies-en-xx-131-part-03\|Availability Dependencies EN XX (Availability_Dependencies_EN_XX) — part 3 of 3]] | SAP S/4HANA Cloud Public Edition scope-item matrix by country/release with dependencies; this part: Procurement and Supply Chain rows plus retired items. |
| [[01-solution-foundation-and-platform/bp-cld-entpr-2608-process-steps-en-xx-135-part-01\|BP CLD ENTPR 2608 Process Steps EN XX (BP_CLD_ENTPR_2608_Process-Steps_EN_XX) — part 1 of 35]] | SAP S/4HANA Cloud Public Edition 2608 process-steps matrix: scope items, solution activities, Fiori apps, business roles and per-country availability. |
| [[01-solution-foundation-and-platform/bp-cld-entpr-2608-process-steps-en-xx-135-part-02\|BP CLD ENTPR 2608 Process Steps EN XX (BP_CLD_ENTPR_2608_Process-Steps_EN_XX) — part 2 of 35]] | SAP S/4HANA Cloud 2608 process-steps matrix: scope item, step, Fiori app, business role, country X-marks; this slice covers items 1GB-1J2 (Finance, Sales). |
| [[01-solution-foundation-and-platform/bp-cld-entpr-2608-process-steps-en-xx-135-part-03\|BP CLD ENTPR 2608 Process Steps EN XX (BP_CLD_ENTPR_2608_Process-Steps_EN_XX) — part 3 of 35]] | SAP S/4HANA Cloud Public Edition 2608 process-step matrix: scope items and steps mapped to Fiori apps, business roles and country availability flags. |
| [[01-solution-foundation-and-platform/bp-cld-entpr-2608-process-steps-en-xx-135-part-04\|BP CLD ENTPR 2608 Process Steps EN XX (BP_CLD_ENTPR_2608_Process-Steps_EN_XX) — part 4 of 35]] | Matrix of SAP S/4HANA Cloud Public Edition 2608 best-practice scope items: process steps, Fiori app IDs, business roles and per-column availability markers. |
| [[01-solution-foundation-and-platform/bp-cld-entpr-2608-process-steps-en-xx-135-part-05\|BP CLD ENTPR 2608 Process Steps EN XX (BP_CLD_ENTPR_2608_Process-Steps_EN_XX) — part 5 of 35]] | SAP S/4HANA Cloud Public Edition 2608 process-step matrix (slice 5/35): app, role and scope flags for scope items 1WE, 1WO, 1WQ, 1WV and start of 1X1. |
| [[01-solution-foundation-and-platform/bp-cld-entpr-2608-process-steps-en-xx-135-part-06\|BP CLD ENTPR 2608 Process Steps EN XX (BP_CLD_ENTPR_2608_Process-Steps_EN_XX) — part 6 of 35]] | SAP S/4HANA Cloud Public Edition 2608 process-steps matrix (scope item, step, app, role, availability); this part: treasury, procurement, manufacturing, sales |
| [[01-solution-foundation-and-platform/bp-cld-entpr-2608-process-steps-en-xx-135-part-07\|BP CLD ENTPR 2608 Process Steps EN XX (BP_CLD_ENTPR_2608_Process-Steps_EN_XX) — part 7 of 35]] | Segment 7/35 of SAP S/4HANA Cloud Public Edition 2608 Process Steps Scope sheet: steps, Fiori apps, roles, country flags for scope items 1ZQ to 2AR. |
| [[01-solution-foundation-and-platform/bp-cld-entpr-2608-process-steps-en-xx-135-part-08\|BP CLD ENTPR 2608 Process Steps EN XX (BP_CLD_ENTPR_2608_Process-Steps_EN_XX) — part 8 of 35]] | SAP S/4HANA Cloud Public Edition 2608 process-steps matrix: scope items, solution activities, Fiori apps, business roles and per-country availability (segment 8 of 35). |
| [[01-solution-foundation-and-platform/bp-cld-entpr-2608-process-steps-en-xx-135-part-09\|BP CLD ENTPR 2608 Process Steps EN XX (BP_CLD_ENTPR_2608_Process-Steps_EN_XX) — part 9 of 35]] | SAP S/4HANA Cloud Public Edition 2608 process-steps matrix (segment 9, scope items 2F5-2QI): activities, Fiori apps, business roles, country availability. |
| [[01-solution-foundation-and-platform/bp-cld-entpr-2608-process-steps-en-xx-135-part-10\|BP CLD ENTPR 2608 Process Steps EN XX (BP_CLD_ENTPR_2608_Process-Steps_EN_XX) — part 10 of 35]] | SAP BP 2608 process-steps matrix (this slice: scope items 2QI-2TS): steps, Fiori apps/transactions, business roles and per-country availability marks. |
| [[01-solution-foundation-and-platform/bp-cld-entpr-2608-process-steps-en-xx-135-part-11\|BP CLD ENTPR 2608 Process Steps EN XX (BP_CLD_ENTPR_2608_Process-Steps_EN_XX) — part 11 of 35]] | Process-steps matrix for SAP S/4HANA Cloud Public Edition 2608 (segment 11 of 35, scope items 2TS tail to 2UN): steps mapped to Fiori apps/transactions, business roles and availability marks. |
| [[01-solution-foundation-and-platform/bp-cld-entpr-2608-process-steps-en-xx-135-part-12\|BP CLD ENTPR 2608 Process Steps EN XX (BP_CLD_ENTPR_2608_Process-Steps_EN_XX) — part 12 of 35]] | SAP S/4HANA Cloud Public Edition 2608 process-steps matrix (segment 12, scope items 2UN-33V): activities, Fiori apps, business roles, country availability. |
| [[01-solution-foundation-and-platform/bp-cld-entpr-2608-process-steps-en-xx-135-part-13\|BP CLD ENTPR 2608 Process Steps EN XX (BP_CLD_ENTPR_2608_Process-Steps_EN_XX) — part 13 of 35]] | SAP S/4HANA Cloud Public Edition 2608 process-steps matrix, segment 13 (scope items 33V-3D2): Fiori apps, business roles and country availability per activity. |
| [[01-solution-foundation-and-platform/bp-cld-entpr-2608-process-steps-en-xx-135-part-14\|BP CLD ENTPR 2608 Process Steps EN XX (BP_CLD_ENTPR_2608_Process-Steps_EN_XX) — part 14 of 35]] | SAP S/4HANA Cloud Public Edition 2608 process-step matrix (scope item, step, Fiori app/ID, role, per-country availability); this part: 3D2 tail to 3HU start. |
| [[01-solution-foundation-and-platform/bp-cld-entpr-2608-process-steps-en-xx-135-part-15\|BP CLD ENTPR 2608 Process Steps EN XX (BP_CLD_ENTPR_2608_Process-Steps_EN_XX) — part 15 of 35]] | SAP S/4HANA Cloud Public Edition 2608 process-steps matrix: scope items, steps, Fiori apps, business roles and scope flags (segment 15: 3HU-3OK). |
| [[01-solution-foundation-and-platform/bp-cld-entpr-2608-process-steps-en-xx-135-part-16\|BP CLD ENTPR 2608 Process Steps EN XX (BP_CLD_ENTPR_2608_Process-Steps_EN_XX) — part 16 of 35]] | SAP S/4HANA Cloud Public Edition 2608 process-steps matrix: scope item, step, Fiori app/ID, business role, applicability. Slice: 3OK-3X1. |
| [[01-solution-foundation-and-platform/bp-cld-entpr-2608-process-steps-en-xx-135-part-17\|BP CLD ENTPR 2608 Process Steps EN XX (BP_CLD_ENTPR_2608_Process-Steps_EN_XX) — part 17 of 35]] | SAP S/4HANA Cloud Public Edition 2608 process-steps matrix: scope items with Fiori apps, business roles and country availability (slice 3X1-42L). |
| [[01-solution-foundation-and-platform/bp-cld-entpr-2608-process-steps-en-xx-135-part-18\|BP CLD ENTPR 2608 Process Steps EN XX (BP_CLD_ENTPR_2608_Process-Steps_EN_XX) — part 18 of 35]] | SAP S/4HANA Cloud Public Edition 2608 process-steps matrix: scope items with Fiori apps, business roles and country availability (slice 42L-4BL). |
| [[01-solution-foundation-and-platform/bp-cld-entpr-2608-process-steps-en-xx-135-part-19\|BP CLD ENTPR 2608 Process Steps EN XX (BP_CLD_ENTPR_2608_Process-Steps_EN_XX) — part 19 of 35]] | SAP S/4HANA Cloud Public Edition 2608 process-steps matrix: scope items 4BL-4QN with Fiori apps, business roles and country availability (segment 19 of 35). |
| [[01-solution-foundation-and-platform/bp-cld-entpr-2608-process-steps-en-xx-135-part-20\|BP CLD ENTPR 2608 Process Steps EN XX (BP_CLD_ENTPR_2608_Process-Steps_EN_XX) — part 20 of 35]] | SAP S/4HANA Cloud Public Edition 2608 scope-item process steps mapped to Fiori apps, business roles and country marks; this slice covers items 4QN to 54V. |
| [[01-solution-foundation-and-platform/bp-cld-entpr-2608-process-steps-en-xx-135-part-21\|BP CLD ENTPR 2608 Process Steps EN XX (BP_CLD_ENTPR_2608_Process-Steps_EN_XX) — part 21 of 35]] | SAP S/4HANA Cloud Public Edition 2608 process-steps matrix (slice 21/35, scope items 54V-5FQ): steps, app ID, business role, per-column availability. |
| [[01-solution-foundation-and-platform/bp-cld-entpr-2608-process-steps-en-xx-135-part-22\|BP CLD ENTPR 2608 Process Steps EN XX (BP_CLD_ENTPR_2608_Process-Steps_EN_XX) — part 22 of 35]] | SAP S/4HANA Cloud Public Edition 2608 process-steps matrix: per scope item activity, Fiori app, business role, country availability (this slice: 5FQ-5JT). |
| [[01-solution-foundation-and-platform/bp-cld-entpr-2608-process-steps-en-xx-135-part-23\|BP CLD ENTPR 2608 Process Steps EN XX (BP_CLD_ENTPR_2608_Process-Steps_EN_XX) — part 23 of 35]] | SAP S/4HANA Cloud Public Edition 2608 process-steps matrix: scope items, Fiori apps, business roles and per-country availability (this slice: 5JT to 5W4). |
| [[01-solution-foundation-and-platform/bp-cld-entpr-2608-process-steps-en-xx-135-part-24\|BP CLD ENTPR 2608 Process Steps EN XX (BP_CLD_ENTPR_2608_Process-Steps_EN_XX) — part 24 of 35]] | SAP S/4HANA Cloud Public Edition 2608 process-steps matrix: scope items, Fiori apps, roles, per-country availability. This slice: 5W4 tail through 6A9 start. |
| [[01-solution-foundation-and-platform/bp-cld-entpr-2608-process-steps-en-xx-135-part-25\|BP CLD ENTPR 2608 Process Steps EN XX (BP_CLD_ENTPR_2608_Process-Steps_EN_XX) — part 25 of 35]] | Process-steps matrix slice (SAP S/4HANA Cloud Public Edition 2608): scope items 6A9, 6AA, 6AV, 6B5-6B7, 6BA, 6BJ, 6BP with apps, roles, country flags. |
| [[01-solution-foundation-and-platform/bp-cld-entpr-2608-process-steps-en-xx-135-part-26\|BP CLD ENTPR 2608 Process Steps EN XX (BP_CLD_ENTPR_2608_Process-Steps_EN_XX) — part 26 of 35]] | SAP S/4HANA Cloud Public Edition 2608 best-practice process steps by scope item, with Fiori app, app ID, business role and per-country availability marks. |
| [[01-solution-foundation-and-platform/bp-cld-entpr-2608-process-steps-en-xx-135-part-27\|BP CLD ENTPR 2608 Process Steps EN XX (BP_CLD_ENTPR_2608_Process-Steps_EN_XX) — part 27 of 35]] | SAP Best Practices 2608 process-steps matrix (part 27/35): per-step Fiori app, app ID, business role and availability flags for scope items 6W2 to 78J. |
| [[01-solution-foundation-and-platform/bp-cld-entpr-2608-process-steps-en-xx-135-part-28\|BP CLD ENTPR 2608 Process Steps EN XX (BP_CLD_ENTPR_2608_Process-Steps_EN_XX) — part 28 of 35]] | SAP S/4HANA Cloud Public Edition 2608 best-practice process steps matrix: scope items, steps, apps, business roles and per-country X marks. |
| [[01-solution-foundation-and-platform/bp-cld-entpr-2608-process-steps-en-xx-135-part-29\|BP CLD ENTPR 2608 Process Steps EN XX (BP_CLD_ENTPR_2608_Process-Steps_EN_XX) — part 29 of 35]] | SAP S/4HANA Cloud Public Edition 2608 process-steps matrix: per scope item the steps, Fiori app/transaction IDs, business roles and X flags (slice: 7HO to 830). |
| [[01-solution-foundation-and-platform/bp-cld-entpr-2608-process-steps-en-xx-135-part-30\|BP CLD ENTPR 2608 Process Steps EN XX (BP_CLD_ENTPR_2608_Process-Steps_EN_XX) — part 30 of 35]] | Segment 30/35 of the SAP S/4HANA Cloud 2608 process-steps matrix: scope items 830-BEJ with steps, Fiori app IDs, business roles and country X-flags. |
| [[01-solution-foundation-and-platform/bp-cld-entpr-2608-process-steps-en-xx-135-part-31\|BP CLD ENTPR 2608 Process Steps EN XX (BP_CLD_ENTPR_2608_Process-Steps_EN_XX) — part 31 of 35]] | SAP S/4HANA Cloud Public Edition 2608 best-practice process-steps matrix: steps per scope item with Fiori app, app ID, role and flags (segment 31/35: BEJ-BKP). |
| [[01-solution-foundation-and-platform/bp-cld-entpr-2608-process-steps-en-xx-135-part-32\|BP CLD ENTPR 2608 Process Steps EN XX (BP_CLD_ENTPR_2608_Process-Steps_EN_XX) — part 32 of 35]] | SAP S/4HANA Cloud Public Edition 2608 process-steps scope matrix; this slice maps scope items BKP to J11 steps to Fiori apps, business roles, country markers. |
| [[01-solution-foundation-and-platform/bp-cld-entpr-2608-process-steps-en-xx-135-part-33\|BP CLD ENTPR 2608 Process Steps EN XX (BP_CLD_ENTPR_2608_Process-Steps_EN_XX) — part 33 of 35]] | SAP S/4HANA Cloud 2608 process-step scope matrix, segment 33/35: J11-J14 project services, J44-J45 MRP and procurement, J54-J58 cost and close. |
| [[01-solution-foundation-and-platform/bp-cld-entpr-2608-process-steps-en-xx-135-part-34\|BP CLD ENTPR 2608 Process Steps EN XX (BP_CLD_ENTPR_2608_Process-Steps_EN_XX) — part 34 of 35]] | SAP S/4HANA Cloud 2608 process-step matrix, segment 34/35: end of J58 close, J59 Accounts Receivable, J60 Accounts Payable, start of J62 Asset Accounting. |
| [[01-solution-foundation-and-platform/bp-cld-entpr-2608-process-steps-en-xx-135-part-35\|BP CLD ENTPR 2608 Process Steps EN XX (BP_CLD_ENTPR_2608_Process-Steps_EN_XX) — part 35 of 35]] | Process-step matrix for SAP S/4HANA Cloud Public Edition 2608 best practices mapping scope-item steps to Fiori apps, business roles and availability columns. |

### Responsibility Management and Situation Handling

How teams, team hierarchies and responsibility rules determine responsible users, and how situation types in the standard and extended frameworks raise and close situations.

| Node | Description |
| --- | --- |
| [[01-solution-foundation-and-platform/test-script-responsibility-management-1nj-746\|Test Script: Responsibility Management (1NJ) (1NJ_S4CLD2608_BPD_EN_XX)]] | S/4HANA Cloud test script for scope item 1NJ: creating teams, team hierarchies, responsibility rules, contexts and team categories in Fiori apps. |
| [[01-solution-foundation-and-platform/test-script-situation-handling-31n-sap-s-4hana-cloud-public-edition-89\|Test Script: Situation Handling (31N) - SAP S/4HANA Cloud Public Edition (31N_S4CLD2608_BPD_EN_XX)]] | SAP Best Practices test script for scope item 31N Situation Handling: roles, prerequisite teams/data, and step-by-step tests of the standard and extended frameworks. |

### SuccessFactors Employee Central Integration and User Provisioning

How banks, company codes, cost centers and workers replicate with SuccessFactors Employee Central, and how HR events provision user roles via Cloud Identity Access Governance.

| Node | Description |
| --- | --- |
| [[01-solution-foundation-and-platform/test-script-exception-based-core-hr-with-sap-successfactors-employee-c\|Test Script: Exception-Based Core HR with SAP SuccessFactors Employee Central (JB1_AE) (JB1_S4CLD2608_BPD_EN_AE)]] | S/4HANA Cloud 2608 test script for JB1 (UAE): replicating banks, company codes, cost centers, workers and photos with SuccessFactors Employee Central. |
| [[01-solution-foundation-and-platform/test-script-automated-provisioning-via-sap-cloud-identity-access-gover\|Test Script: Automated Provisioning via SAP Cloud Identity Access Governance (3AB) (3AB_S4CLD2608_BPD_EN_XX)]] | S/4HANA Cloud Public Edition test script for scope item 3AB: SuccessFactors HR events (hire, job change, termination) drive role provisioning via Cloud IAG. |

## Related categories
- related-to :: [[02-business-partner-and-product-master-data/_cluster]]
- related-to :: [[16-two-tier-erp-and-central-finance/_cluster]]
