---
id: 01-solution-foundation-and-platform/sscui-list-en-xx-sap-s-4hana-cloud-2608-configuration-2-part-36
title: SSCUI List EN XX (SAP S/4HANA Cloud 2608 Configuration) (SSCUI_List_EN_XX) — part 36 of 40
description: "SSCUI list segment 36/40 (S/4HANA Cloud 2608): business catalog rows mapping transaction codes to IMG activities, SSCUI IDs, components (EWM, FI-CA, RE-FX)."
cluster: 01-solution-foundation-and-platform
tags: [kb/solution-foundation-and-platform, topic/sscui-configuration-activity-list]
aliases: []
keywords: [Self-Service Configuration (SSCUI) Activity List, business catalog mapping, img activities, sscui ids, transaction codes, warehouse management, contract accounting, real estate, funds management, country localization]
sources: ["raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Configuration/SSCUI_List_EN_XX.xlsm#lines-7497-8758"]
confidence: high
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-2
topic: 01-solution-foundation-and-platform/sscui-configuration-activity-list
language: EN
part: 36/40
created: 2026-10-12
updated: 2026-10-12
---

# SSCUI List EN XX (SAP S/4HANA Cloud 2608 Configuration) (SSCUI_List_EN_XX) — part 36 of 40

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Configuration/SSCUI_List_EN_XX.xlsm`, part 36 of 40 (lines 7497–8758 of the extracted text), extracted with `xlsx2md`. Grouped under **Self-Service Configuration (SSCUI) Activity List** in Solution Foundation and Platform. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

| SAP_CA_BC_IC_LND_FIN_OA0_PC | Overhead Cost Accounting - Configuration | FINS_BT_NUM | FINS_BT_NUM_TRAN | PSM_S4C_V_BDGTD_SNUM | Define Number Range for Budget Documents | 180023 | CO-OM | PSM-FM-BU |
| SAP_CA_BC_IC_LND_FIN_OA0_PC | Overhead Cost Accounting - Configuration | S_ER9_11001356 | S_ER9_11001356_TRAN | PSM_S4C_V_BDGTD_SNUM | Define Number Range for Budget Documents | 180023 | CO-OM | PSM-FM-BU |
| SAP_CA_BC_IC_LND_FIN_OA0_PC | Overhead Cost Accounting - Configuration | S_ER9_11002440 | S_ER9_11002440_TRAN | FJEPVC_IHB_DERIV_CO | Maintain Settings for Posting Expenses and Incomes for In-House Banking | 105995 | CO-OM | FI-GL-BTI-2CL |
| SAP_CA_BC_IC_LND_FIN_OA0_PC | Overhead Cost Accounting - Configuration | S_ER9_11001320 | S_ER9_11001320_TRAN | PSM_S4C_V_BDGT_DOCTY | Define Budget Document Type | 180020 | CO-OM | PSM |
| SAP_CA_BC_IC_LND_FIN_OA0_PC | Overhead Cost Accounting - Configuration | OKZ2 |  | SIMG_ORKK_WERK_OKZ2 | Define Overhead Groups | 106748 | CO-OM | CO-PC-OBJ-2CL |
| SAP_CA_BC_IC_LND_FIN_OA0_PC | Overhead Cost Accounting - Configuration | S_ER9_11001319 | S_ER9_11001319_TRAN | PSM_S4C_V_BDGT_SUBCT | Define Budget Type | 180014 | CO-OM | PSM-FM-BU-AC |
| SAP_CA_BC_IC_LND_FIN_OA0_PC | Overhead Cost Accounting - Configuration | S_ALR_87008033 | S_ALR_87008033_TRAN | SIMG_ORKK_WERK_OKZ2 | Define Overhead Groups | 106748 | CO-OM | CO-PC-OBJ-2CL |
| SAP_CA_BC_IC_LND_FIN_OA0_PC | Overhead Cost Accounting - Configuration | S_ALR_87008034 | S_ALR_87008034_TRAN | SIMG_ORKK_AUF_OKOG | Define Overhead Keys | 106747 | CO-OM | CO-PC-OBJ-2CL |
| SAP_CA_BC_IC_LND_FIN_OA0_PC | Overhead Cost Accounting - Configuration | FINS_BT_NUM | FINS_BT_NUM_TRAN | PSM_S4C_V_BDGTD_SNUM | Define Number Range for Budget Documents | 180023 | CO-OM | PSM-FM-BU |
| SAP_CA_BC_IC_LND_FIN_OA0_PC | Overhead Cost Accounting - Configuration | S_ER1_70001594 | S_ER1_70001594_TRAN | FCO_V_ICO_CLR | Define Posting Scheme for Intercompany Clearing Accounts | 107107 | CO-OM | CO-OM-2CL |
| SAP_CA_BC_IC_LND_FIN_OA0_PC | Overhead Cost Accounting - Configuration | S_ER1_70001815 | S_ER1_70001815_TRAN | FCO_V_ACTAL_CCNV | Define Currency Settings for Activity Allocation | 107337 | CO-OM | CO-OM-2CL |
| SAP_CA_BC_IC_LND_FIN_BOE_PC | Bill of Exchange - Configuration | S_ALR_87015290 | S_ALR_87015290_TRAN | FI_BL_BE_V_T045F | Enter Bank Assignments | 101083 | FI-LOC-IAM | FI-AR-AR-2CL |
| SAP_CA_BC_IC_LND_FIN_BOE_PC | Bill of Exchange - Configuration | S_ALR_87015287 | S_ALR_87015287_TRAN | FI_BL_BE_V_T045D | Define Available Amounts | 101082 | FI-LOC-IAM | FI-AR-AR-2CL |
| SAP_CA_BC_IC_LND_FIN_BOE_PC | Bill of Exchange - Configuration | S_ALR_87002791 | S_ALR_87002791_TRAN | SIMG_CFMENUOFTDOT67 | Define Exception Types | 106787 | FI-LOC-IAM | FI-AR-AR-2CL |
| SAP_CA_BC_IC_LND_FIN_BOE_PC | Bill of Exchange - Configuration | S_ALR_87001397 | S_ALR_87001397_TRAN | SIMG_CFMENUORFBOBYK | Define Bank Subaccounts | 101081 | FI-LOC-IAM | FI-AR-AR-2CL |
| SAP_CA_BC_IC_LND_FIN_BOE_PC | Bill of Exchange - Configuration | OBYK |  | SIMG_CFMENUORFBOBYK | Define Bank Subaccounts | 101081 | FI-LOC-IAM | FI-AR-AR-2CL |
| SAP_CA_BC_IC_LND_FIN_BOE_PC | Bill of Exchange - Configuration | S_ALR_87002691 | S_ALR_87002691_TRAN | SIMG_CFMENUOFTDOT68 | Define Account for Returned Bills of Exchange | 101084 | FI-LOC-IAM | FI-AR-AR-2CL |
| SAP_CA_BC_IC_LND_FIN_BOE_PC | Bill of Exchange - Configuration | S_ALR_87099784 | S_ALR_87099784_TRAN | FI_BL_BE_V_T045P | Define Bill of Exchange Portfolios | 101235 | FI-LOC-IAM | FI-LOC-BOE |
| SAP_CA_BC_IC_LND_PSS_PC0_PC | Product Compliance - Configuration | S_ER1_70000119 | S_ER1_70000119_TRAN | EHFND_DGM_SHCOND | Specify Shipping Conditions for Sales Documents | 103138 | EHS-SUS-FND-PC | EHS-SUS-DG |
| SAP_CA_BC_IC_LND_PSS_PC0_PC | Product Compliance - Configuration | S_ER1_70000161 | S_ER1_70000161_TRAN | EHFND_PC_CHKBEHVR | Adapt Behavior of Compliance Checks in Value Chain | 103325 | EHS-SUS-FND-PC | EHS-SUS-FND-PC |
| SAP_CA_BC_IC_LND_PSS_PC0_PC | Product Compliance - Configuration | S_ER1_70000092 | S_ER1_70000092_TRAN | EHFND_DGM_PACKDESC | Specify Descriptions of Dangerous Goods Packagings | 102900 | EHS-SUS-FND-PC | EHS-SUS-FND |
| SAP_CA_BC_IC_LND_PSS_PC0_PC | Product Compliance - Configuration | S_ER1_70000074 | S_ER1_70000074_TRAN | EHFND_DGM_RESPUNITDG | Specify Responsible Units for Dangerous Goods | 102790 | EHS-SUS-FND-PC | EHS-SUS-FND-PC |
| SAP_CA_BC_IC_LND_PSS_PC0_PC | Product Compliance - Configuration | S_ER1_70000031 | S_ER1_70000031_TRAN | EHFND_PMC_CCI_CMPSTY | Specify Legal Areas for Product Compliance | 102414 | EHS-SUS-FND-PC | EHS-SUS-FND-PC |
| SAP_CA_BC_IC_LND_PSS_PC0_PC | Product Compliance - Configuration | S_ER1_70000028 | S_ER1_70000028_TRAN | EHFND_PMC_GEN_RESPUN | Specify Responsible Units for Product Compliance | 102404 | EHS-SUS-FND-PC | EHS-SUS-FND-PC |
| SAP_CA_BC_IC_LND_PSS_PC0_PC | Product Compliance - Configuration | S_ER1_70000283 | S_ER1_70000283_TRAN | EHFND_DGM_DSCR_TMPL | Specify Output of Dangerous Goods Description | 103968 | EHS-SUS-FND-PC | EHS-SUS-DG |
| SAP_CA_BC_IC_LND_PSS_PC0_PC | Product Compliance - Configuration | S_ER1_70000351 | S_ER1_70000351_TRAN | EHFND_PC_SNUM | Specify Number Ranges for Product Compliance | 105378 | EHS-SUS-FND-PC | EHS-SUS-FND-PC |
| SAP_CA_BC_IC_LND_PSS_PC0_PC | Product Compliance - Configuration | S_ER1_70000378 | S_ER1_70000378_TRAN | EHSDSV_PRN_RANK | Specify Priority for Product Name Determination for Safety Data Sheets | 105600 | EHS-SUS-FND-PC | EHS-SUS-SDS |
| SAP_CA_BC_IC_LND_PSS_PC0_PC | Product Compliance - Configuration | EHFND_SNUM_INTNR |  | EHFND_PC_SNUM | Specify Number Ranges for Product Compliance | 105378 | EHS-SUS-FND-PC | EHS-SUS-FND-PC |
| SAP_CA_BC_IC_LND_PSS_PC0_PC | Product Compliance - Configuration | S_ER1_70000318 | S_ER1_70000318_TRAN | EHFND_PC_BUSFEAT_DT | Specify Excluded Document Types for Integration | 104454 | EHS-SUS-FND-PC | EHS-SUS-FND |
| SAP_CA_BC_IC_LND_PSS_PC0_PC | Product Compliance - Configuration | S_ER1_70000451 | S_ER1_70000451_TRAN | EHPMA_SVT_ESIC | Specify Excluded Sales Item Categories | 106137 | EHS-SUS-FND-PC | EHS-SUS-PMA |
| SAP_CA_BC_IC_LND_PSS_PC0_PC | Product Compliance - Configuration | S_ER1_70000464 | S_ER1_70000464_TRAN | EHFND_DGM_DSCR_GRPG | Adapt Behavior for Grouping of Dangerous Goods in Documents | 106130 | EHS-SUS-FND-PC | EHS-SUS-DG |
| SAP_CA_BC_IC_LND_PSS_PC0_PC | Product Compliance - Configuration | S_ER1_70000399 | S_ER1_70000399_TRAN | EHPMA_SVT_IMVT | Specify Included Movement Types | 105751 | EHS-SUS-FND-PC | EHS-SUS-PMA |
| SAP_CA_BC_IC_LND_PSS_PC0_PC | Product Compliance - Configuration | S_ER1_70000379 | S_ER1_70000379_TRAN | EHPMA_SVT_EPIC | Specify Excluded Purchasing Item Categories | 105752 | EHS-SUS-FND-PC | EHS-SUS-PMA |
| SAP_CA_BC_IC_LND_PSS_PC0_PC | Product Compliance - Configuration | S_ER1_70000380 | S_ER1_70000380_TRAN | EHPMA_SVT_EDIC | Specify Excluded Delivery Item Categories | 105753 | EHS-SUS-FND-PC | EHS-SUS-PMA |
| SAP_CA_BC_IC_LND_PSS_PC0_PC | Product Compliance - Configuration | EHLBLV_CATEGORY |  | EHLBL_LABEL_CTGRY | Specify Label Categories | 106617 | EHS-SUS-FND-PC | EHS-SUS-SDS |
| SAP_CA_BC_IC_LND_PSS_PC0_PC | Product Compliance - Configuration | S_ER1_70000732 | S_ER1_70000732_TRAN | EHLBL_LABEL_CTGRY | Specify Label Categories | 106617 | EHS-SUS-FND-PC | EHS-SUS-SDS |
| SAP_CA_BC_IC_LND_PSS_PC0_PC | Product Compliance - Configuration | S_ER1_70000691 | S_ER1_70000691_TRAN | EHFND_DGM_EXCATEGORY | Specify Exemption Categories | 106605 | EHS-SUS-FND-PC | EHS-SUS-CI |
| SAP_CA_BC_IC_LND_PSS_PC0_PC | Product Compliance - Configuration | S_ER1_70000890 | S_ER1_70000890_TRAN | EHSDSV_CNF_SHPMT | Specify Shipment Level for Safety Data Sheets | 106722 | EHS-SUS-FND-PC | EHS-SUS-SDS |
| SAP_CA_BC_IC_LND_PSS_PC0_PC | Product Compliance - Configuration | S_ER1_70000930 | S_ER1_70000930_TRAN | EHFND_PC_CCIDFR | Specify Product Identifier Types | 106755 | EHS-SUS-FND-PC | EHS-SUS-FND-PC |
| SAP_CA_BC_IC_LND_PSS_PC0_PC | Product Compliance - Configuration | S_ER1_70000925 | S_ER1_70000925_TRAN | EHFND_DGM_MXDLOAD | Enable Mixed Loading Check | 106753 | EHS-SUS-FND-PC | EHS-SUS-DG |
| SAP_CA_BC_IC_LND_PSS_PC0_PC | Product Compliance - Configuration | S_ER1_70000290 | S_ER1_70000290_TRAN | EHFND_BF_PC_ACTIVATE | Activate Product Compliance |  | EHS-SUS-FND-PC | EHS-SUS-FND |
| SAP_CA_BC_IC_LND_PSS_PC0_PC | Product Compliance - Configuration | S_ER1_70000280 | S_ER1_70000280_TRAN | EHFND_DGM_TM_MOT_MAP | Assign Modes of Transport for Transportation Management |  | EHS-SUS-FND-PC | EHS-SUS-FND-PC |
| SAP_CA_BC_IC_LND_PSS_PC0_PC | Product Compliance - Configuration | EHFND_NRO_CRQID |  | EHFND_CRQ_SNUM | Specify Number Ranges for Compliance Requests |  | EHS-SUS-FND-PC | EHS-SUS-FND-PC |
| SAP_CA_BC_IC_LND_PSS_PC0_PC | Product Compliance - Configuration | S_ER1_70001922 | S_ER1_70001922_TRAN | EHFND_CRQ_SNUM | Specify Number Ranges for Compliance Requests |  | EHS-SUS-FND-PC | EHS-SUS-FND-PC |
| SAP_CA_BC_IC_LND_IRF_MOD_PC | Information Retrieval Framework Modelling - Configuration | DTINF_MAINTAIN_PURP |  | DTINF_PU_C | Maintain IRF Purposes | 103525 | CA-GTF-INF | CA-GTF-INF |
| SAP_CA_BC_IC_LND_IRF_MOD_PC | Information Retrieval Framework Modelling - Configuration | S_SAL_71000036 | S_SAL_71000036_TRAN | DTINF_PU_C | Maintain IRF Purposes | 103525 | CA-GTF-INF | CA-GTF-INF |
| SAP_SM_BC_PSDOC_CONFIGURE_PC | Settlement Management - Personnel Settlement Document Configuration | F4021 | F4021_TRAN |  |  |  | LO-AB |  |
| SAP_CA_BC_IC_LND_PP_KAB0_PC | Kanban Replenishment Strategies for Stock Transfer - Configuration | OM19 |  | SIMG_CFMENUOM00OM19 | Define Kanban Calculation Profiles | 105567 | PP-KAB | PP-KAB-2CL |
| SAP_CA_BC_IC_LND_PP_KAB0_PC | Kanban Replenishment Strategies for Stock Transfer - Configuration | S_ALR_87005442 | S_ALR_87005442_TRAN | SIMG_CFMENUOM00OM15 | Define Kanban Container Status Texts | 106281 | PP-KAB | PP-KAB-2CL |
| SAP_CA_BC_IC_LND_PP_KAB0_PC | Kanban Replenishment Strategies for Stock Transfer - Configuration | S_ALR_87005461 | S_ALR_87005461_TRAN | SIMG_CFMENUOM00OM20 | Define Strategies for Adopting Kanban Calculation Proposals | 105733 | PP-KAB | PP-KAB-2CL |
| SAP_CA_BC_IC_LND_PP_KAB0_PC | Kanban Replenishment Strategies for Stock Transfer - Configuration | S_ALR_87005446 | S_ALR_87005446_TRAN | SIMG_CFMENUOM00OM16 | Define Kanban Container Status Sequences | 106282 | PP-KAB | PP-KAB-2CL |
| SAP_CA_BC_IC_LND_PP_KAB0_PC | Kanban Replenishment Strategies for Stock Transfer - Configuration | S_ALR_87005457 | S_ALR_87005457_TRAN | SIMG_CFMENUOM00OM19 | Define Kanban Calculation Profiles | 105567 | PP-KAB | PP-KAB-2CL |
| SAP_CA_BC_IC_LND_PP_KAB0_PC | Kanban Replenishment Strategies for Stock Transfer - Configuration | S_ALR_87005485 | S_ALR_87005485_TRAN | SIMG_CFMENUOM00OM13 | Define Stock Transfer Strategies | 103917 | PP-KAB | PP-KAB-2CL |
| SAP_CA_BC_IC_LND_PSM_FM0_PC | Funds Management - Configuration | S_ER6_68000022 | S_ER6_68000022_TRAN | PSM_S4C_V_RE_ACC_CON | Edit Constant for Expense or Revenue Account | 180017 | PSM | PSM |
| SAP_CA_BC_IC_LND_PSM_FM0_PC | Funds Management - Configuration | S_ER9_11001207 | S_ER9_11001207_TRAN | PSM_S4C_V_MDWHM | Derive Account Assignment for Material Stock Postings | 180018 | PSM | PSM-FM-UP |
| SAP_CA_BC_IC_LND_PSM_FM0_PC | Funds Management - Configuration | S_ER9_11001196 | S_ER9_11001196_TRAN | PSM_S4C_VC_AVC_PRO | Define Availability Control Profile | 180015 | PSM | PSM-FM-BU-AC |
| SAP_CA_BC_IC_LND_PSM_FM0_PC | Funds Management - Configuration | S_ER9_11001210 | S_ER9_11001210_TRAN | PSM_S4C_V_BGTACCAAM | Derive Budget Account for Assets | 180029 | PSM | PSM-FM-UP |
| SAP_CA_BC_IC_LND_PSM_FM0_PC | Funds Management - Configuration | S_ER6_68000014 | S_ER6_68000014_TRAN | PSM_S4C_FM_FUNDTYPE | Create FM Fund Types | 180012 | PSM | PSM |
| SAP_CA_BC_IC_LND_PSM_FM0_PC | Funds Management - Configuration | S_ER9_11001204 | S_ER9_11001204_TRAN | PSM_S4C_V_AVC_PRO_AS | Assign AVC Profile to Company Code/Budget Consumption Year | 180022 | PSM | PSM-FM-BU-AC |
| SAP_CA_BC_IC_LND_PSM_FM0_PC | Funds Management - Configuration | S_ER9_11001358 | S_ER9_11001358_TRAN | PSM_S4C_V_BGTACCDP | Derive Budget Account for Down Payments without Commitment Reference | 180024 | PSM | PSM-FM-UP |
| SAP_CA_BC_IC_LND_PSM_FM0_PC | Funds Management - Configuration | S_ER9_11001320 | S_ER9_11001320_TRAN | PSM_S4C_V_BDGT_DOCTY | Define Budget Document Type | 180020 | PSM | PSM |
| SAP_CA_BC_IC_LND_PSM_FM0_PC | Funds Management - Configuration | S_ER9_11001319 | S_ER9_11001319_TRAN | PSM_S4C_V_BDGT_SUBCT | Define Budget Type | 180014 | PSM | PSM-FM-BU-AC |
| SAP_CA_BC_IC_LND_PSM_FM0_PC | Funds Management - Configuration | S_ER9_11001541 | S_ER9_11001541_TRAN | PSM_S4C_V_COBDGTRLVC | Define Budget Relevance of CO Processes | 180026 | PSM | PSM-FM |
| SAP_CA_BC_IC_LND_PSM_FM0_PC | Funds Management - Configuration | S_ER9_11001324 | S_ER9_11001324_TRAN | PSM_S4C_V_BDGT_CUST | Activate Journal Fields for Budgeting | 180021 | PSM | PSM-FM-BU |
| SAP_CA_BC_IC_LND_PSM_FM0_PC | Funds Management - Configuration | S_ER9_11001119 | S_ER9_11001119_TRAN | PSM_S4C_PRDICITY | Define Frequency Types | 180016 | PSM | PSM-FM-MD |
| SAP_CA_BC_IC_LND_PSM_FM0_PC | Funds Management - Configuration | S_ER9_11001486 | S_ER9_11001486_TRAN | PSM_S4C_V_FMR_TOL | Define Amount Tolerance Limits for Earmarked Funds | 180030 | PSM | PSM-FM-PO-EF |
| SAP_CA_BC_IC_LND_PSM_FM0_PC | Funds Management - Configuration | S_ER9_11001116 | S_ER9_11001116_TRAN | PSM_S4C_FMC_AUTHGRP | Define Authorization Groups for Fund | 180013 | PSM | PSM-FM-MD |
| SAP_CA_BC_IC_LND_PSM_FM0_PC | Funds Management - Configuration | S_ER9_11001839 | S_ER9_11001839_TRAN | PSM_S4C_V_POOLFNDACT | Activate Pooled Funds | 180045 | PSM | PSM-FM-UP |
| SAP_CA_BC_IC_LND_PSM_FM0_PC | Funds Management - Configuration | S_ER9_11001902 | S_ER9_11001902_TRAN | PSM_S4C_VC_AVC_T_PRO | Define AVC Tolerance Profile | 180046 | PSM | PSM-FM-BU-AC |
| SAP_CA_BC_IC_LND_PSM_FM0_PC | Funds Management - Configuration | S_ER1_84000025 | S_ER1_84000025_TRAN | PSM_S4C_V_TKBBA_CE | Define Document Types for Earmarked Funds | 180086 | PSM | PSM |
| SAP_CA_BC_IC_LND_PSM_FM0_PC | Funds Management - Configuration | S_ER1_84000024 | S_ER1_84000024_TRAN | PSM_S4C_V_FMR_TOL_CE | Define Tolerance Keys for Earmarked Funds | 180085 | PSM | PSM |
| SAP_CA_BC_IC_LND_PSM_FM0_PC | Funds Management - Configuration | S_ER1_84000026 | S_ER1_84000026_TRAN | PSM_S4C_SPL_FPROF_CE | Define Field Profiles for Automatic Account Assignment Distribution | 180088 | PSM | PSM |
| SAP_CA_BC_IC_LND_PSM_FM0_PC | Funds Management - Configuration | S_ER1_84000027 | S_ER1_84000027_TRAN | PSM_S4C_SPL_APROF_CE | Define Action Profiles for Automatic Account Assignment Distribution | 180089 | PSM | PSM |
| SAP_CA_BC_IC_LND_PSM_FM0_PC | Funds Management - Configuration | S_ER9_11001356 | S_ER9_11001356_TRAN | PSM_S4C_V_BDGTD_SNUM | Define Number Range for Budget Documents | 180023 | PSM | PSM-FM-BU |
| SAP_CA_BC_IC_LND_PSM_FM0_PC | Funds Management - Configuration | S_ER1_84000029 | S_ER1_84000029_TRAN | PSM_S4C_VC_MSG_FM | Change Message Control for Budget Management | 180090 | PSM | PSM |
| SAP_CA_BC_IC_LND_PSM_FM0_PC | Funds Management - Configuration | S_ER1_84000030 | S_ER1_84000030_TRAN | PSM_S4C_VC_MSG_FA | Change Message Control for Fund Accounting | 180092 | PSM | PSM |
| SAP_CA_BC_IC_LND_PSM_FM0_PC | Funds Management - Configuration | S_ER9_11002426 | S_ER9_11002426_TRAN | PSM_S4C_RIB_PRF_AS | Assign RIB Profile to Company Code and Fiscal Year | 180093 | PSM | PSM-FM-BU |
| SAP_CA_BC_IC_LND_PSM_FM0_PC | Funds Management - Configuration | S_ER9_11002427 | S_ER9_11002427_TRAN | PSM_S4C_CAL_SC | Maintain Calculation Scheme | 180094 | PSM | PSM-FM-BU |
| SAP_CA_BC_IC_LND_PSM_FM0_PC | Funds Management - Configuration | S_ER9_11002425 | S_ER9_11002425_TRAN | PSM_S4C_RIB_PROF | Define RIB Profile | 180095 | PSM | PSM-FM-BU |
| SAP_CA_BC_IC_LND_PSM_FM0_PC | Funds Management - Configuration | S_ER1_84000028 | S_ER1_84000028_TRAN | PSM_S4C_IRW_BELEG_CE | Define Document Number Ranges for Earmarked Funds | 180087 | PSM | PSM |
| SAP_CA_BC_IC_LND_PSM_FM0_PC | Funds Management - Configuration | S_ER1_84000033 | S_ER1_84000033_TRAN | PSM_S4C_V_TIVCACCSET | Activate Earmarked Funds for Company Code | 180096 | PSM | PSM |
| SAP_CA_BC_IC_LND_PSM_FM0_PC | Funds Management - Configuration | S_ER1_84000037 | S_ER1_84000037_TRAN | PSM_S4C_V_FLOWTYPE | Define Flow Types for Earmarked Funds Generation | 180100 | PSM | PSM |
| SAP_CA_BC_IC_LND_PSM_FM0_PC | Funds Management - Configuration | S_ER1_84000034 | S_ER1_84000034_TRAN | PSM_S4C_V_CLMEFBUACC | Derive Budget Account for CLM Contracts | 180097 | PSM | PSM |
| SAP_CA_BC_IC_LND_PSM_FM0_PC | Funds Management - Configuration | S_ER1_84000035 | S_ER1_84000035_TRAN | PSM_S4C_V_EXCNTYPE | Activate Earmarked Funds for CLM Contract Types | 180098 | PSM | PSM |
| SAP_CA_BC_IC_LND_PSM_FM0_PC | Funds Management - Configuration | S_ER1_84000080 | S_ER1_84000080_TRAN | PSM_S4C_FMRESLOCKS | Define Earmarked Funds Blocks | 106432 | PSM | PSM |
| SAP_CA_BC_IC_LND_PSM_FM0_PC | Funds Management - Configuration | S_ER1_84000081 | S_ER1_84000081_TRAN | PSM_S4C_FMRCCVARI | Define Company Code Groups for Earmarked Funds | 106447 | PSM | PSM |
| SAP_CA_BC_IC_LND_PSM_FM0_PC | Funds Management - Configuration | S_ER1_84000082 | S_ER1_84000082_TRAN | PSM_S4C_FMRCCVARIA | Assign Company Code Groups to Company Codes for Earmarked Funds | 106448 | PSM | PSM |
| SAP_CA_BC_IC_LND_PSM_FM0_PC | Funds Management - Configuration | S_ER1_84000083 | S_ER1_84000083_TRAN | PSM_S4C_FMRSCDATA | Define Integrated Scenarios for Earmarked Funds | 106494 | PSM | PSM |
| SAP_CA_BC_IC_LND_PSM_FM0_PC | Funds Management - Configuration | S_ER1_70000722 | S_ER1_70000722_TRAN | PSM_S4C_V_001_COS_CE | Deactivate Cost of Sales Accounting | 106609 | PSM | PSM-FM-MD |
| SAP_CA_BC_IC_LND_PSM_FM0_PC | Funds Management - Configuration | S_ER1_70001071 | S_ER1_70001071_TRAN | PSM_S4C_UPDDATETY | Define Update Date for Budget Consumption | 106827 | PSM | PSM-FM-UP |
| SAP_CA_BC_IC_LND_PSM_FM0_PC | Funds Management - Configuration | FINS_BT_NUM | FINS_BT_NUM_TRAN | PSM_S4C_V_BDGTD_SNUM | Define Number Range for Budget Documents | 180023 | PSM | PSM-FM-BU |
| SAP_CA_BC_IC_LND_PSM_FM0_PC | Funds Management - Configuration | FMEFDOCUNUMBER | FMEFDOCUNUMBER_TRAN | PSM_S4C_IRW_BELEG_CE | Define Document Number Ranges for Earmarked Funds | 180087 | PSM | PSM |
| SAP_CMD_BC_SUPPLIER_DSP_PC | Master Data - Supplier Display | F0354 | F0354_03_TRAN |  |  |  | LO-MD-BP |  |
| SAP_CA_BC_IC_LND_FIN_CJ0_PC | Cash Journal - Configuration | FBCJC0 | SAIS_FBCJC0_TRAN |  |  |  | FI-BL |  |
| SAP_CA_BC_IC_LND_FIN_CJ0_PC | Cash Journal - Configuration | S_ALR_87009225 | S_ALR_87009225_TRAN | FI_BL_CJ_T_FBCJC2 | Maintain Business Transactions | 101003 | FI-BL | FI-BL-PT-CJ-2CL |
| SAP_CA_BC_IC_LND_FIN_CJ0_PC | Cash Journal - Configuration | FBCJC2 | SAIS_FBCJC2_TRAN |  |  |  | FI-BL |  |
| SAP_CA_BC_IC_LND_FIN_CJ0_PC | Cash Journal - Configuration | S_ALR_87009221 | S_ALR_87009221_TRAN | FI_BL_CJ_T_FBCJC0 | Set Up Cash Journal | 101002 | FI-BL | FI-BL-PT-CJ-2CL |
| SAP_CA_BC_IC_LND_FIN_CJ0_PC | Cash Journal - Configuration | FBCJC5 |  | FI_BL_CJ_T_FBCJC5 | Define Numbering Groups for Cash Journal | 103549 | FI-BL | FI-BL-PT-CJ-2CL |
| SAP_CA_BC_IC_LND_FIN_CJ0_PC | Cash Journal - Configuration | S_EB5_05000362 | S_EB5_05000362_TRAN | FI_BL_CJ_T_FBCJC5 | Define Numbering Groups for Cash Journal | 103549 | FI-BL | FI-BL-PT-CJ-2CL |
| SAP_CA_BC_IC_LND_FIN_CJ0_PC | Cash Journal - Configuration | S_EB5_05000336 | S_EB5_05000336_TRAN | V_TCJ_NUMB_GROUP | Define Numbering Groups |  | FI-BL | FI-BL-PT-CJ-2CL |
| SAP_CA_BC_IC_LND_FIN_CJ0_PC | Cash Journal - Configuration | S_P7D_67000037 | S_P7D_67000037_TRAN | FI_BL_CJ_V_MAXAMOUNT | Define Amount Limit | 101004 | FI-BL | FI-BL-PT-CJ-2CL |
| SAP_CA_BC_IC_LND_LOG_VE_PC | Logistics for Venezuela - Configuration | S_E4A_94000011 | S_E4A_94000011_TRAN | V_DOCCLS_PF_VE | Maintain Document Classes for Prenumbered Forms | 102553 | FI-LOC-LO-VE | FI-LOC-LO-VE |
| SAP_CA_BC_IC_LND_LOG_VE_PC | Logistics for Venezuela - Configuration | S_E4A_94000010 | S_E4A_94000010_TRAN | V_IDCN_VOID_VE | Maintain Void Reason Codes | 102567 | FI-LOC-LO-VE | FI-LOC-LO-VE |
| SAP_CA_BC_IC_LND_LOG_VE_PC | Logistics for Venezuela - Configuration | S_E4A_94000008 | S_E4A_94000008_TRAN | V_IDCN_DOTY_VE | Maintain Form Types | 102552 | FI-LOC-LO-VE | FI-LOC-LO-VE |
| SAP_CA_BC_IC_LND_LOG_VE_PC | Logistics for Venezuela - Configuration | S_ER9_52001407 | S_ER9_52001407_TRAN | GLO_ODN_DOC_TY_V_VE | Assign Document Types to Billing Types | 102907 | FI-LOC-LO-VE | FI-LOC-LO-VE |
| SAP_CA_BC_IC_LND_LOG_VE_PC | Logistics for Venezuela - Configuration | S_E4A_94000009 | S_E4A_94000009_TRAN | VC_IDCN_LBMA_VE | Maintain Lots and Books for Prenumbered Forms | 102566 | FI-LOC-LO-VE | FI-LOC-LO-VE |
| SAP_CA_BC_IC_LND_LOG_VE_PC | Logistics for Venezuela - Configuration | S_E4A_94000012 | S_E4A_94000012_TRAN | V_T003_B_I_PF_VE | Assign Document Classes to Document Types for Prenumbered Forms | 102554 | FI-LOC-LO-VE | FI-LOC-LO-VE |
| SAP_FIN_BC_AR_NRO_PC | Accounts Receivable - Adjust Number Ranges | SEPA_NR_MT | SEPA_NR_MT_TRAN |  |  |  | FI-AR-AR |  |
| SAP_CA_BC_IC_LND_GLO_LO3_PC | Globalisation Logistics MENA/India/Others - Configuration | S_ER9_52001029 | S_ER9_52001029_TRAN | LOG_MENA_ODN_02 | Maintain Number Groups for Official Document Numbering for MENA | 102410 | FI-LOC-LO-IN | FI-LOC-LO-AE |
| SAP_CA_BC_IC_LND_GLO_LO3_PC | Globalisation Logistics MENA/India/Others - Configuration | S_ER9_52001028 | S_ER9_52001028_TRAN | LOG_MENA_ODN_01 | Assign Document Classes to Document Types for Official Doc. Numbering MENA | 102409 | FI-LOC-LO-IN | FI-LOC-LO-AE |
| SAP_CA_BC_IC_LND_GLO_LO3_PC | Globalisation Logistics MENA/India/Others - Configuration | S_ER9_52001027 | S_ER9_52001027_TRAN | LOG_MENA_IMPORT | Maintain Condition Type for MENA | 102453 | FI-LOC-LO-IN | FI-LOC-LO-AE |
| SAP_CA_BC_IC_LND_GLO_LO3_PC | Globalisation Logistics MENA/India/Others - Configuration | S_ER9_52001088 | S_ER9_52001088_TRAN | LOG_MENA_ODN_07 | Configure Document Types and Tax Codes | 102492 | FI-LOC-LO-IN | FI-LOC-LO-IT |
| SAP_CA_BC_IC_LND_GLO_LO3_PC | Globalisation Logistics MENA/India/Others - Configuration | S_ER9_52001030 | S_ER9_52001030_TRAN | LOG_MENA_ODN_03 | Assign Number Ranges to Business Places for Official Doc. Numbering MENA | 102411 | FI-LOC-LO-IN | FI-LOC-LO-AE |
| SAP_CA_BC_IC_LND_GLO_LO3_PC | Globalisation Logistics MENA/India/Others - Configuration | S_ER9_52002400 | S_ER9_52002400_TRAN | GLO_TAXCODE_V | ICV Retention | 104113 | FI-LOC-LO-IN | FI-LOC-LO-AE |
| SAP_CA_BC_IC_LND_GLO_LO3_PC | Globalisation Logistics MENA/India/Others - Configuration | S_ER9_52002759 | S_ER9_52002759_TRAN | EDOC_IN_MAP_VPA | Map Virtual Payment Address to House Bank | 104764 | FI-LOC-LO-IN | FI-LOC-LO-IN |
| SAP_CA_BC_IC_LND_GLO_LO3_PC | Globalisation Logistics MENA/India/Others - Configuration | S_ER9_52003356 | S_ER9_52003356_TRAN | IDIN_J_1IG_ICOV | Assign Tax Determination Parameters for India | 105766 | FI-LOC-LO-IN | FI-LOC-LO-IN |
| SAP_CA_BC_IC_LND_GLO_LO3_PC | Globalisation Logistics MENA/India/Others - Configuration | S_ER9_52001053 | S_ER9_52001053_TRAN | LOG_MENA_ODN_05 | Maintain Number Ranges for Official Document Numbering for MENA | 102412 | FI-LOC-LO-IN | FI-LOC-LO-AE |
| SAP_CA_BC_IC_LND_GLO_LO3_PC | Globalisation Logistics MENA/India/Others - Configuration | S_ER9_52002345 | S_ER9_52002345_TRAN | J_1IG_PRCTXCODEV | Maintain Default Tax Code for Process Type | 103810 | FI-LOC-LO-IN | FI-LOC-LO-IN |
| SAP_CA_BC_IC_LND_GLO_LO3_PC | Globalisation Logistics MENA/India/Others - Configuration | S_ER9_52001727 | S_ER9_52001727_TRAN | J1IGSUBCAUTOV | Configure Subcontracting Automation | 103373 | FI-LOC-LO-IN | FI-LOC-LO-IN |
| SAP_CA_BC_IC_LND_GLO_LO3_PC | Globalisation Logistics MENA/India/Others - Configuration | S_ER9_52002062 | S_ER9_52002062_TRAN | J_1IG_V_VENRET | Region-wise Customer for Vendor Returns | 103582 | FI-LOC-LO-IN | FI-LOC-LO-IN |
| SAP_CA_BC_IC_LND_GLO_LO3_PC | Globalisation Logistics MENA/India/Others - Configuration | S_ER9_52002363 | S_ER9_52002363_TRAN | J_1IGVENPYMTVALV | Maintain Supplier Payment Validity Period | 105854 | FI-LOC-LO-IN | FI-LOC-LO-IN |
| SAP_CA_BC_IC_LND_GLO_LO3_PC | Globalisation Logistics MENA/India/Others - Configuration | S_ER9_52002332 | S_ER9_52002332_TRAN | J_1IG_THLDV | Maintain Threshold Amount | 103822 | FI-LOC-LO-IN | FI-LOC-LO-IN |
| SAP_CA_BC_IC_LND_GLO_LO3_PC | Globalisation Logistics MENA/India/Others - Configuration | S_ER9_52003307 | S_ER9_52003307_TRAN | IDIND_J_1IG_CERTV | Maintain Certificate Category | 105767 | FI-LOC-LO-IN | FI-LOC-LO-IN |
| SAP_CA_BC_IC_LND_GLO_LO3_PC | Globalisation Logistics MENA/India/Others - Configuration | S_EBJ_98000990 | S_EBJ_98000990_TRAN | V_DOCCLS_IN | Maintain Document Classes | 101872 | FI-LOC-LO-IN | FI-LOC-LO-IN |
| SAP_CA_BC_IC_LND_GLO_LO3_PC | Globalisation Logistics MENA/India/Others - Configuration | S_EBJ_98000996 | S_EBJ_98000996_TRAN | J_1IG_ISD_POST_V | Configure ISD Invoice Posting Settings | 101927 | FI-LOC-LO-IN | FI-LOC-LO-IN |
| SAP_CA_BC_IC_LND_GLO_LO3_PC | Globalisation Logistics MENA/India/Others - Configuration | S_EBJ_98000997 | S_EBJ_98000997_TRAN | J_1IG_ISD_TO_V | Maintain Turnover for Receiving Business Places | 101912 | FI-LOC-LO-IN | FI-LOC-LO-IN |
| SAP_CA_BC_IC_LND_GLO_LO3_PC | Globalisation Logistics MENA/India/Others - Configuration | S_ER9_52001726 | S_ER9_52001726_TRAN | J_1IG_V_PERIV | Maintain Fiscal Year Variant for ODN | 103408 | FI-LOC-LO-IN | FI-LOC-LO-IN |
| SAP_CA_BC_IC_LND_GLO_LO3_PC | Globalisation Logistics MENA/India/Others - Configuration | S_ER9_52001078 | S_ER9_52001078_TRAN | GLO_ODN_DOC_TY_V_IN | Assign Document Types to Billing Types | 102473 | FI-LOC-LO-IN | FI-LOC-LO-IT |
| SAP_CA_BC_IC_LND_GLO_LO3_PC | Globalisation Logistics MENA/India/Others - Configuration | S_ER9_52000960 | S_ER9_52000960_TRAN | J_1IG_SUBCONVALV | Maintain subcontracting challan validity period | 102237 | FI-LOC-LO-IN | FI-LOC-LO-IN |
| SAP_CA_BC_IC_LND_GLO_LO3_PC | Globalisation Logistics MENA/India/Others - Configuration | J1AB | J1AB_TRAN | LOG_MENA_ODN_05 | Maintain Number Ranges for Official Document Numbering for MENA | 102412 | FI-LOC-LO-IN | FI-LOC-LO-AE |
| SAP_CA_BC_IC_LND_GLO_LO3_PC | Globalisation Logistics MENA/India/Others - Configuration | S_ER9_52001031 | S_ER9_52001031_TRAN | LOG_MENA_ODN_04 | Maintain Document Classes for Official Document Numbering for MENA | 102408 | FI-LOC-LO-IN | FI-LOC-LO-AE |
| SAP_CA_BC_IC_LND_GLO_LO3_PC | Globalisation Logistics MENA/India/Others - Configuration | S_ER1_70001204 | S_ER1_70001204_TRAN | J_1IG_OFNUM1V | Assign Process-Specific Number Ranges to Business Places for India | 106861 | FI-LOC-LO-IN | FI-LOC-LO-IN |
| SAP_CA_BC_IC_LND_GLO_LO3_PC | Globalisation Logistics MENA/India/Others - Configuration | S_EBJ_98000991 | S_EBJ_98000991_TRAN | J_1IG_V_T003_I | Assign Document Types to Document Classes for GST for India | 101338 | FI-LOC-LO-IN | FI-LOC-LO-IN |
| SAP_CA_BC_IC_LND_GLO_LO3_PC | Globalisation Logistics MENA/India/Others - Configuration | S_ER9_52000792 | S_ER9_52000792_TRAN | J_1ATJ1AB-IN | Maintain Number Ranges for Goods and Services Tax for India | 102879 | FI-LOC-LO-IN | FI-LOC-LO-IN |
| SAP_CA_BC_IC_LND_GLO_LO3_PC | Globalisation Logistics MENA/India/Others - Configuration | J1IG_ODN | J1IG_ODN_TRAN | J_1ATJ1AB-IN | Maintain Number Ranges for Goods and Services Tax for India | 102879 | FI-LOC-LO-IN | FI-LOC-LO-IN |
| SAP_CA_BC_IC_LND_GLO_LO3_PC | Globalisation Logistics MENA/India/Others - Configuration | S_ER1_70001317 | S_ER1_70001317_TRAN | GLO_TVBURV | Maintain Additional Fiscal Data for Sales Office | 106929 | FI-LOC-LO-IN | FI-LOC-LO-AE |
| SAP_CA_BC_IC_LND_GLO_LO3_PC | Globalisation Logistics MENA/India/Others - Configuration | S_EBJ_98000981 | S_EBJ_98000981_TRAN | J_1ICONDTAX_IN | Assign Tax Code to Company Codes | 101320 | FI-LOC-LO-IN | FI-LOC-LO-IN |
| SAP_CA_BC_IC_LND_GLO_LO3_PC | Globalisation Logistics MENA/India/Others - Configuration | S_EBJ_98000984 | S_EBJ_98000984_TRAN | J_1BBRANCV_IN | Define Business Places for Goods and Services Tax for India | 101326 | FI-LOC-LO-IN | FI-LOC-LO-IN |
| SAP_CA_BC_IC_LND_GLO_LO3_PC | Globalisation Logistics MENA/India/Others - Configuration | S_EBJ_98000982 | S_EBJ_98000982_TRAN | J_1IEXCDEFN_IN | Classify Condition Types for Goods and Services Tax for India | 101934 | FI-LOC-LO-IN | FI-LOC-LO-IN |
| SAP_CA_BC_IC_LND_GLO_LO3_PC | Globalisation Logistics MENA/India/Others - Configuration | S_EBJ_98000987 | S_EBJ_98000987_TRAN | J_1IMESG_IN | Message Control | 101923 | FI-LOC-LO-IN | FI-LOC-LO-IN |
| SAP_CA_BC_IC_LND_GLO_LO3_PC | Globalisation Logistics MENA/India/Others - Configuration | S_EBJ_98000985 | S_EBJ_98000985_TRAN | J_1BT001WV_IN | Assign Business Places to Plants for Goods and Services Tax for India | 101316 | FI-LOC-LO-IN | FI-LOC-LO-IN |
| SAP_CA_BC_IC_LND_GLO_LO3_PC | Globalisation Logistics MENA/India/Others - Configuration | S_EBJ_98000986 | S_EBJ_98000986_TRAN | J_1IT030K_V_IN | Define and Assign G/L Accounts | 101871 | FI-LOC-LO-IN | FI-LOC-LO-IN |
| SAP_CA_BC_IC_LND_GLO_LO3_PC | Globalisation Logistics MENA/India/Others - Configuration | S_EBJ_98000992 | S_EBJ_98000992_TRAN | J_1IG_V_NUMGRP | Maintain Number Groups for Goods and Services Tax for India | 101869 | FI-LOC-LO-IN | FI-LOC-LO-IN |
| SAP_CA_BC_IC_LND_GLO_LO3_PC | Globalisation Logistics MENA/India/Others - Configuration | S_EBJ_98000993 | S_EBJ_98000993_TRAN | J_1IG_V_OFNUM | Assign Number Ranges to Business Places for GST for India | 101319 | FI-LOC-LO-IN | FI-LOC-LO-IN |
| SAP_CA_BC_IC_LND_GLO_LO3_PC | Globalisation Logistics MENA/India/Others - Configuration | S_ER1_70001601 | S_ER1_70001601_TRAN | J_1IG_T030V | Define Split Clearing Account - India | 107109 | FI-LOC-LO-IN | FI-LOC-LO-IN |
| SAP_CA_BC_IC_LND_GLO_LO3_PC | Globalisation Logistics MENA/India/Others - Configuration | S_EBJ_98000988 | S_EBJ_98000988_TRAN | J_1IG_V_SUBINV | Classify Subcontracting Billing Types | 101924 | FI-LOC-LO-IN | FI-LOC-LO-IN |
| SAP_CA_BC_IC_LND_GLO_LO3_PC | Globalisation Logistics MENA/India/Others - Configuration | S_EBJ_98000995 | S_EBJ_98000995_TRAN | J_1IG_ISD_MAP_V | Map ISD Business Places to Receiving Business Places | 101911 | FI-LOC-LO-IN | FI-LOC-LO-IN |
| SAP_CA_BC_IC_LND_GLO_LO3_PC | Globalisation Logistics MENA/India/Others - Configuration | S_EBJ_98000989 | S_EBJ_98000989_TRAN | J_1IG_DOCTYP_V | Specify Document Types for Goods and Services Tax for India | 101910 | FI-LOC-LO-IN | FI-LOC-LO-IN |
| SAP_CA_BC_IC_LND_GLO_LO3_PC | Globalisation Logistics MENA/India/Others - Configuration | S_EBJ_98000983 | S_EBJ_98000983_TRAN | V_T604F_IN | Maintain HSN and SAC | 101332 | FI-LOC-LO-IN | FI-LOC-LO-IN |
| SAP_MM_BC_CTLG_CONFIG_PC | Materials Management - Catalog Management | F1994 | F1994_TRAN |  |  |  | MM-PUR-GF |  |
| SAP_MM_BC_CTLG_CONFIG_PC | Materials Management - Catalog Management | F3149 | F3149_TRAN |  |  |  | MM-PUR-GF |  |
| SAP_MM_BC_CTLG_CONFIG_PC | Materials Management - Catalog Management | F3293 | F3293_TRAN |  |  |  | MM-PUR-GF |  |
| SAP_CA_BC_IC_LND_SCM_ATP2_PC | Advanced Available-to-Promise Product Allocation - Configuration | S_ER9_52000267 | S_ER9_52000267_TRAN | CA_ATP_PAL_002 | Activate Product Allocation | 102132 | CA-ATP-PAL | CA-ATP-PAL-2CL |
| SAP_CA_BC_IC_LND_S4CRM_SC0_PC | Service Contract - Configuration | S_ER1_83000057 | S_ER1_83000057_TRAN | VCRMD_SERWI | Define Service Profiles | 103194 | CRM-S4-SRV-SVO | CRM-S4-SRV-CTR-2CL |
| SAP_CA_BC_IC_LND_S4CRM_SC0_PC | Service Contract - Configuration | S_ER1_83000058 | S_ER1_83000058_TRAN | CRMS4VC_ESCAL | Define Response Profiles for Service Transactions | 103329 | CRM-S4-SRV-SVO | CRM-S4-SRV-CTR-2CL |
| SAP_CA_BC_IC_LND_S4CRM_SC0_PC | Service Contract - Configuration | S_ER1_83000060 | S_ER1_83000060_TRAN | S4CRM_PLANT_SRV_CTRY | Assign Plant and Storage Location to Country/Region | 103352 | CRM-S4-SRV-SVO | CRM-BF-2CL |
| SAP_CA_BC_IC_LND_S4CRM_SC0_PC | Service Contract - Configuration | S_PNE_45000063 | S_PNE_45000063_TRAN | CRMVC_SRQM_SDP | Define SLA Determination Procedures for Service Transactions | 103193 | CRM-S4-SRV-SVO | CRM-S4-BTX-2CL |
| SAP_CA_BC_IC_LND_S4CRM_SC0_PC | Service Contract - Configuration | S_PIC_80000159 | S_PIC_80000159_TRAN | CRMC_CANC_GRUND | Define Cancellation Reasons | 106895 | CRM-S4-SRV-SVO | CRM-S4-BTX-2CL |
| SAP_CA_BC_IC_LND_S4CRM_SC0_PC | Service Contract - Configuration | S_ER1_83000006 | S_ER1_83000006_TRAN | S4CRM_PLANT_SRV | Assign Plant and Storage Location to Service Employee and Country/Region | 102883 | CRM-S4-SRV-SVO | CRM-BF-2CL |
| SAP_CA_BC_IC_LND_S4CRM_SC0_PC | Service Contract - Configuration | S_A2C_40000021 | S_A2C_40000021_TRAN | CRMC_CANCEL_PARTY | Define Cancelling Party | 106894 | CRM-S4-SRV-SVO | CRM-S4-BTX-2CL |
| SAP_CA_BC_IC_LND_S4CRM_SC0_PC | Service Contract - Configuration | S_ER1_83000117 | S_ER1_83000117_TRAN | CRMS4_SC_VLDN | Deactivate Service Contract Validation | 103807 | CRM-S4-SRV-SVO | CRM-BF-2CL |
| SAP_CA_BC_IC_LND_S4CRM_SC0_PC | Service Contract - Configuration | S_ER1_83000109 | S_ER1_83000109_TRAN | CRMS4_SC_I_DTEM | Specify Item Filtering Option for Contract Determination | 103700 | CRM-S4-SRV-SVO | CRM-S4-SRV-CTR-2CL |
| SAP_CA_BC_IC_LND_S4CRM_SC0_PC | Service Contract - Configuration | S_ER1_83000108 | S_ER1_83000108_TRAN | CRMS4_SC_DETERM | Specify Contract Determination Option for Trans. Types | 103686 | CRM-S4-SRV-SVO | CRM-S4-SRV-CTR-2CL |
| SAP_CA_BC_IC_LND_ADD1_PC | Business Services Address Management - Configuration | S_ABA_72000037 | S_ABA_72000037_TRAN | _CABP_V_TSAD3 | Maintain Forms of Address | 103436 | BC-SRV-ADR | AP-MD-BP |
| SAP_CA_BC_IC_LND_ADD1_PC | Business Services Address Management - Configuration | S_BCE_68000187 | S_BCE_68000187_TRAN | SIMG_CFMENUSAPCOVK2 | Insert Regions (Subnational Administration Units) | 103826 | BC-SRV-ADR | BC-SRV-ADR |
| SAP_CA_BC_IC_LND_ADD1_PC | Business Services Address Management - Configuration | OVK2 |  | SIMG_CFMENUSAPCOVK2 | Insert Regions (Subnational Administration Units) | 103826 | BC-SRV-ADR | BC-SRV-ADR |
| SAP_CA_BC_IC_LND_ADD1_PC | Business Services Address Management - Configuration | S_YI3_39000591 | S_YI3_39000591_TRAN | IMG_SET_CTRY_LANG_EN | Name of the Recipient Country in English in Output Forms | 106025 | BC-SRV-ADR | BC-SRV-ADR |
| SAP_CA_BC_IC_LND_ADD1_PC | Business Services Address Management - Configuration | SA25 | SA25_TRAN |  |  |  | BC-SRV-ADR |  |
| SAP_CA_BC_IC_LND_ADD1_PC | Business Services Address Management - Configuration | S_YI3_39000309 | S_YI3_39000309_TRAN | SIMG_ADDRESSES_SA09C | Activate International Address Versions - Client-Specific | 103268 | BC-SRV-ADR | BC-SRV-ADR |
| SAP_CA_BC_IC_LND_ADD1_PC | Business Services Address Management - Configuration | SA09C | SA09C_TRAN | SIMG_ADDRESSES_SA09C | Activate International Address Versions - Client-Specific | 103268 | BC-SRV-ADR | BC-SRV-ADR |
| SAP_CA_BC_IC_LND_ADD1_PC | Business Services Address Management - Configuration | S_ABA_72000014 | S_ABA_72000014_TRAN | _CABP_NAMEFORMAT | Maintain Name Formatting Rules |  | BC-SRV-ADR | AP-MD-BP |
| SAP_CA_BC_IC_LND_ADD1_PC | Business Services Address Management - Configuration | SA13 | SA13_TRAN | _CABP_NAMEFORMAT | Maintain Name Formatting Rules |  | BC-SRV-ADR | AP-MD-BP |
| SAP_CA_BC_IC_LND_ADD1_PC | Business Services Address Management - Configuration | S_YI3_39001476 | S_YI3_39001476_TRAN | ADDR_GEOLOC_BF | Activate Geolocation in Business Address Services | 107356 | BC-SRV-ADR | BC-SRV-ADR |
| SAP_CA_BC_IC_LND_ADD1_PC | Business Services Address Management - Configuration | ADDR_GEOLOC_BF |  | ADDR_GEOLOC_BF | Activate Geolocation in Business Address Services | 107356 | BC-SRV-ADR | BC-SRV-ADR |
| SAP_CA_BC_IC_LND_FIN_WT_IT_PC | Statutory Reporting WT for Italy - Configuration | S_EBJ_45000263 | S_EBJ_45000263_TRAN | FIWTITV_SSI | Assign Withholding Tax Type and Tax Code to Social Security Institution | 101848 | FI-LOC-FI-IT | FI-LOC-FI-IT |
| SAP_CA_BC_IC_LND_FIN_WT_IT_PC | Statutory Reporting WT for Italy - Configuration | S_EBJ_45000262 | S_EBJ_45000262_TRAN | FIWTITV_SSIFCOD | Define Social Security Institution | 101849 | FI-LOC-FI-IT | FI-LOC-FI-IT |
| SAP_CA_BC_IC_LND_FIN_WT_IT_PC | Statutory Reporting WT for Italy - Configuration | S_E4A_94000037 | S_E4A_94000037_TRAN | T005_IT_UIC | UIC Code for Italy | 104312 | FI-LOC-FI-IT | FI-AP-AP-B-2CL |
| SAP_CA_BC_IC_LND_FIN_WT_IT_PC | Statutory Reporting WT for Italy - Configuration | S_EBJ_45000050 | S_EBJ_45000050_TRAN | FIITC_CONFIG | Define Generic Parameters for Company Code | 102644 | FI-LOC-FI-IT | FI-LOC-FI-IT |
| SAP_CA_BC_IC_LND_FIN_AA_BG_PC | Asset Accounting for Bulgaria - Configuration | /BGLOCS/11000040 | BGLOCS_11000040_TRAN | /BGLOCS/FIFXAFGT | Define Legal Figures for Fixed Assets | 105847 | FI-LOC-FI-BG | FI-LOC-FI-BG |
| SAP_CA_BC_IC_LND_FIN_AA_BG_PC | Asset Accounting for Bulgaria - Configuration | FIAABG_FIGCL | FIAABG_FIGCL_TRAN | FIAABGV_FIGCL | Assign Legal Figures to Asset Classes | 105848 | FI-LOC-FI-BG | FI-LOC-AA |
| SAP_CA_BC_IC_LND_FIN_AA_BG_PC | Asset Accounting for Bulgaria - Configuration | FIAABG_FIFXAFGT | FIAABG_FIFXAFGT_TRAN | /BGLOCS/FIFXAFGT | Define Legal Figures for Fixed Assets | 105847 | FI-LOC-FI-BG | FI-LOC-FI-BG |
| SAP_CA_BC_IC_LND_FIN_AA_BG_PC | Asset Accounting for Bulgaria - Configuration | S_ER9_11002384 | S_ER9_11002384_TRAN | FIAABGV_FIGCL | Assign Legal Figures to Asset Classes | 105848 | FI-LOC-FI-BG | FI-LOC-AA |
| SAP_CA_BC_IC_LND_FIN_AA_BG_PC | Asset Accounting for Bulgaria - Configuration | FIBG_SA_CONF_U |  | FIBGVC_SA_CONF_U | Maintain Settings for SAF-T Fixed Assets | 107344 | FI-LOC-FI-BG | FI-LOC-SAF-BG |
| SAP_CA_BC_IC_LND_FIN_AA_BG_PC | Asset Accounting for Bulgaria - Configuration | S_ER1_70001879 | S_ER1_70001879_TRAN | FIBGVC_SA_CONF_U | Maintain Settings for SAF-T Fixed Assets | 107344 | FI-LOC-FI-BG | FI-LOC-SAF-BG |
| SAP_SD_BC_BIL_CONFIGURE_PC | Sales - Billing Configuration | F4274 | F4274_TRAN |  |  |  | SD-BIL |  |
| SAP_CA_BC_IC_LND_RFM_PROMN_PC | Retail Promotion - Configuration | V_TWAA_EA_RETAIL |  | W_ZF_VK_0221 | Promotion Type | 105695 | LO-RFM | LO-RFM-MD-PR-2CL |
| SAP_CA_BC_IC_LND_RFM_PROMN_PC | Retail Promotion - Configuration | S_E5R_84000040 | S_E5R_84000040_TRAN | W_ZF_VK_0221 | Promotion Type | 105695 | LO-RFM | LO-RFM-MD-PR-2CL |
| SAP_TM_BC_PRFS_PC | Transportation - Profiles and Settings | /SCMTMS/WD42F | SCMTMS_WD42F_TRAN |  |  |  | TM-BF-AUT |  |
| SAP_TM_BC_PRFS_PC | Transportation - Profiles and Settings | /SCMTMS/WD43A | SCMTMS_WD43A_TRAN |  |  |  | TM-BF-AUT |  |
| SAP_TM_BC_PRFS_PC | Transportation - Profiles and Settings | /SCMTMS/WD43B | SCMTMS_WD43B_TRAN |  |  |  | TM-BF-AUT |  |
| SAP_TM_BC_PRFS_PC | Transportation - Profiles and Settings | /SCMTMS/WD43C | SCMTMS_WD43C_TRAN |  |  |  | TM-BF-AUT |  |
| SAP_TM_BC_PRFS_PC | Transportation - Profiles and Settings | /SCMTMS/WD53A | SCMTMS_WD53A_TRAN |  |  |  | TM-BF-AUT |  |
| SAP_TM_BC_PRFS_PC | Transportation - Profiles and Settings | /SCMTMS/WD53B | SCMTMS_WD53B_TRAN |  |  |  | TM-BF-AUT |  |
| SAP_TM_BC_PRFS_PC | Transportation - Profiles and Settings | /SCMTMS/WD53C | SCMTMS_WD53C_TRAN |  |  |  | TM-BF-AUT |  |
| SAP_TM_BC_PRFS_PC | Transportation - Profiles and Settings | /SCMTMS/WD55A | SCMTMS_WD55A_TRAN |  |  |  | TM-BF-AUT |  |
| SAP_TM_BC_PRFS_PC | Transportation - Profiles and Settings | /SCMTMS/WD55B | SCMTMS_WD55B_TRAN |  |  |  | TM-BF-AUT |  |
| SAP_TM_BC_PRFS_PC | Transportation - Profiles and Settings | /SCMTMS/WD55C | SCMTMS_WD55C_TRAN |  |  |  | TM-BF-AUT |  |
| SAP_TM_BC_PRFS_PC | Transportation - Profiles and Settings | /SCMTMS/WD57A | SCMTMS_WD57A_TRAN |  |  |  | TM-BF-AUT |  |
| SAP_TM_BC_PRFS_PC | Transportation - Profiles and Settings | /SCMTMS/WD57B | SCMTMS_WD57B_TRAN |  |  |  | TM-BF-AUT |  |
| SAP_TM_BC_PRFS_PC | Transportation - Profiles and Settings | /SCMTMS/WD57C | SCMTMS_WD57C_TRAN |  |  |  | TM-BF-AUT |  |
| SAP_TM_BC_PRFS_PC | Transportation - Profiles and Settings | /SCMTMS/WD64A | SCMTMS_WD64A_TRAN |  |  |  | TM-BF-AUT |  |
| SAP_TM_BC_PRFS_PC | Transportation - Profiles and Settings | /SCMTMS/WD64B | SCMTMS_WD64B_TRAN |  |  |  | TM-BF-AUT |  |
| SAP_TM_BC_PRFS_PC | Transportation - Profiles and Settings | /SCMTMS/WD64C | SCMTMS_WD64C_TRAN |  |  |  | TM-BF-AUT |  |
| SAP_TM_BC_PRFS_PC | Transportation - Profiles and Settings | /SCMTMS/WD65A | SCMTMS_WD65A_TRAN |  |  |  | TM-BF-AUT |  |
| SAP_TM_BC_PRFS_PC | Transportation - Profiles and Settings | /SCMTMS/WD65B | SCMTMS_WD65B_TRAN |  |  |  | TM-BF-AUT |  |
| SAP_TM_BC_PRFS_PC | Transportation - Profiles and Settings | /SCMTMS/WD66B | SCMTMS_WD66B_TRAN |  |  |  | TM-BF-AUT |  |
| SAP_TM_BC_PRFS_PC | Transportation - Profiles and Settings | /SCMTMS/WD66A | SCMTMS_WD66A_TRAN |  |  |  | TM-BF-AUT |  |
| SAP_TM_BC_PRFS_PC | Transportation - Profiles and Settings | /SCMTMS/WD65C | SCMTMS_WD65C_TRAN |  |  |  | TM-BF-AUT |  |
| SAP_TM_BC_PRFS_PC | Transportation - Profiles and Settings | /SCMTMS/WD66C | SCMTMS_WD66C_TRAN |  |  |  | TM-BF-AUT |  |
| SAP_TM_BC_PRFS_PC | Transportation - Profiles and Settings | /SCMTMS/WD69A | SCMTMS_WD69A_TRAN |  |  |  | TM-BF-AUT |  |
| SAP_TM_BC_PRFS_PC | Transportation - Profiles and Settings | /SCMTMS/WD69B | SCMTMS_WD69B_TRAN |  |  |  | TM-BF-AUT |  |
| SAP_TM_BC_PRFS_PC | Transportation - Profiles and Settings | /SCMTMS/WD69C | SCMTMS_WD69C_TRAN |  |  |  | TM-BF-AUT |  |
| SAP_TM_BC_PRFS_PC | Transportation - Profiles and Settings | F5768 | F5768_TRAN |  |  |  | TM-BF-AUT |  |
| SAP_TM_BC_PRFS_PC | Transportation - Profiles and Settings | F5769 | F5769_TRAN |  |  |  | TM-BF-AUT |  |
| SAP_TM_BC_PRFS_PC | Transportation - Profiles and Settings | F5770 | F5770_TRAN |  |  |  | TM-BF-AUT |  |
| SAP_TM_BC_PRFS_PC | Transportation - Profiles and Settings | F5771 | F5771_TRAN |  |  |  | TM-BF-AUT |  |
| SAP_TM_BC_PRFS_PC | Transportation - Profiles and Settings | F6014 | F6014_TRAN |  |  |  | TM-BF-AUT |  |
| SAP_TM_BC_PRFS_PC | Transportation - Profiles and Settings | F6608 | F6608_TRAN |  |  |  | TM-BF-AUT |  |
| SAP_TM_BC_PRFS_PC | Transportation - Profiles and Settings | F6609 | F6609_TRAN |  |  |  | TM-BF-AUT |  |
| SAP_TM_BC_PRFS_PC | Transportation - Profiles and Settings | F7434 | F7434_TRAN |  |  |  | TM-BF-AUT |  |
| SAP_CA_BC_IC_LND_EAM_MDATA_PC | Plant Maintenance Master Data - Configuration | S_ALR_87000419 | S_ALR_87000419_TRAN | SIMG_CFMENUOLI0OIPK | Create Structure Indicator for Reference Locations/Functional Locations | 101889 | PM | PM-2CL |
| SAP_CA_BC_IC_LND_EAM_MDATA_PC | Plant Maintenance Master Data - Configuration | S_ALR_87000381 | S_ALR_87000381_TRAN | OLI0T370P | Define Measuring Point Categories | 102636 | PM | PM-2CL |
| SAP_CA_BC_IC_LND_EAM_MDATA_PC | Plant Maintenance Master Data - Configuration | OIEN |  | SIMG_CFMENUOLI0OIEN | Define Number Ranges for Equipment Categories | 103091 | PM | PM-2CL |
| SAP_CA_BC_IC_LND_EAM_MDATA_PC | Plant Maintenance Master Data - Configuration | S_ALR_87000088 | S_ALR_87000088_TRAN | SIMG_CFMENUOLI0OIAA | Define ABC Indicators | 102260 | PM | PM-2CL |
| SAP_CA_BC_IC_LND_EAM_MDATA_PC | Plant Maintenance Master Data - Configuration | OIPK |  | SIMG_CFMENUOLI0OIPK | Create Structure Indicator for Reference Locations/Functional Locations | 101889 | PM | PM-2CL |
| SAP_CA_BC_IC_LND_EAM_MDATA_PC | Plant Maintenance Master Data - Configuration | S_ALR_87000101 | S_ALR_87000101_TRAN | SIMG_CFMENUOLI0OIEA | Define Types of Technical Objects | 101896 | PM | PM-2CL |
| SAP_CA_BC_IC_LND_EAM_MDATA_PC | Plant Maintenance Master Data - Configuration | S_ALR_87000084 | S_ALR_87000084_TRAN | SIMG_CFMENUOLI0OIAG | Define Authorization Groups for Technical Objects | 104801 | PM | PM-2CL |
| SAP_CA_BC_IC_LND_EAM_MDATA_PC | Plant Maintenance Master Data - Configuration | S_AL0_96000746 | S_AL0_96000746_TRAN | OLI0IMRCCUST | Make System Settings for Measuring Points and Measurement Documents | 105116 | PM | PM-2CL |
| SAP_CA_BC_IC_LND_EAM_MDATA_PC | Plant Maintenance Master Data - Configuration | S_ER9_52002695 | S_ER9_52002695_TRAN | SIMG_VC_EAMDETMETHOD | Define Detection Methods | 104804 | PM | PM-WOC-MN-2CL |
| SAP_CA_BC_IC_LND_EAM_MDATA_PC | Plant Maintenance Master Data - Configuration | S_ER9_52002682 | S_ER9_52002682_TRAN | SIMG_EAM_NOTIFDETCAT | Maintain Additional Functions | 104803 | PM | PM-WOC-MN-2CL |
| SAP_CA_BC_IC_LND_EAM_MDATA_PC | Plant Maintenance Master Data - Configuration | OIL4 | OIL4_TRAN | SIMG_CFMENUOLIPOIL4 | Define Number Ranges for General Maintenance Task Lists | 105676 | PM | PM-2CL |
| SAP_CA_BC_IC_LND_EAM_MDATA_PC | Plant Maintenance Master Data - Configuration | S_ALR_87000089 | S_ALR_87000089_TRAN | SIMG_CFMENUOLIPOIL4 | Define Number Ranges for General Maintenance Task Lists | 105676 | PM | PM-2CL |
| SAP_CA_BC_IC_LND_EAM_MDATA_PC | Plant Maintenance Master Data - Configuration | S_ER9_52001757 | S_ER9_52001757_TRAN | SIMG_CFMENUOLVT370T | Assign Number Ranges to Equipment Categories | 105862 | PM | PM-2CL |
| SAP_CA_BC_IC_LND_EAM_MDATA_PC | Plant Maintenance Master Data - Configuration | OIL6 | OIL6_TRAN | SIMG_CFMENUOLIPOIL6 | Define Profiles with Default Values for Task Lists | 106446 | PM | PM-2CL |
| SAP_CA_BC_IC_LND_EAM_MDATA_PC | Plant Maintenance Master Data - Configuration | S_ALR_87000539 | S_ALR_87000539_TRAN | SIMG_CFMENUOLI0OIEN | Define Number Ranges for Equipment Categories | 103091 | PM | PM-2CL |
| SAP_CA_BC_IC_LND_EAM_MDATA_PC | Plant Maintenance Master Data - Configuration | S_ALR_87000103 | S_ALR_87000103_TRAN | SIMG_CFMENUOLIPOIL6 | Define Profiles with Default Values for Task Lists | 106446 | PM | PM-2CL |
| SAP_CA_BC_IC_LND_SRV_GS0_PC | Service - General Settings - Configuration | S_ER1_83000112 | S_ER1_83000112_TRAN | CRM_SLS_COPY_ITCAT2 | Copy Pricing Conditions | 103866 | CRM-S4-SRV-SVO | CRM-BF-2CL |
| SAP_CA_BC_IC_LND_SCM_EWM_PC | Warehouse Management - Configuration | /SCWM/60000631 | SCWM_60000631_TRAN | /SCWM/PI_CC_PERI | Configure Cycle Counting | 102730 | SCM-EWM-AUT | SCM-EWM-CFG-2CL |
| SAP_CA_BC_IC_LND_SCM_EWM_PC | Warehouse Management - Configuration | /SCWM/60000599 | SCWM_60000599_TRAN | /SCWM/V_TCAT | Define Stock Types | 102590 | SCM-EWM-AUT | SCM-EWM-CFG-2CL |
| SAP_CA_BC_IC_LND_SCM_EWM_PC | Warehouse Management - Configuration | /SCWM/60000155 | SCWM_60000155_TRAN | /SCWM/T313Z | Maintain SSCC Generation for Each Warehouse Number | 102843 | SCM-EWM-AUT | SCM-EWM-CFG-2CL |
| SAP_CA_BC_IC_LND_SCM_EWM_PC | Warehouse Management - Configuration | /SCWM/60000154 | SCWM_60000154_TRAN | /SCWM/SNRO | Define Number Range Intervals for SSCC | 102867 | SCM-EWM-AUT | SCM-EWM-CFG-2CL |
| SAP_CA_BC_IC_LND_SCM_EWM_PC | Warehouse Management - Configuration | /SCWM/60000288 | SCWM_60000288_TRAN | /SCWM/T338 | Define Bulk Storage Indicators | 102531 | SCM-EWM-AUT | SCM-EWM-CFG-2CL |
| SAP_CA_BC_IC_LND_SCM_EWM_PC | Warehouse Management - Configuration | /SCWM/60000289 | SCWM_60000289_TRAN | /SCWM/T337B | Define Bulk Structures | 102555 | SCM-EWM-AUT | SCM-EWM-CFG-2CL |
| SAP_CA_BC_IC_LND_SCM_EWM_PC | Warehouse Management - Configuration | /SCWM/22000151 | SCWM_22000151_TRAN | /SCWM/V_T340DSSC | Define Warehouse Attributes | 102480 | SCM-EWM-AUT | SCM-EWM-CFG-2CL |
| SAP_CA_BC_IC_LND_SCM_EWM_PC | Warehouse Management - Configuration | /SCWM/22000154 | SCWM_22000154_TRAN | /SCWM/V_T331SSC | Create Storage Types Using Templates | 102519 | SCM-EWM-AUT | SCM-EWM-CFG-2CL |
| SAP_CA_BC_IC_LND_SCM_EWM_PC | Warehouse Management - Configuration | /SCWM/22000172 | SCWM_22000172_TRAN | /SCWM/VC_PIAA_WH | Define Physical Inventory Area | 102621 | SCM-EWM-AUT | SCM-EWM-CFG-2CL |
| SAP_CA_BC_IC_LND_SCM_EWM_PC | Warehouse Management - Configuration | /SCWM/22000156 | SCWM_22000156_TRAN | /SCWM/VFORMFLDSC | Define Print Form for Physical Inventory Documents | 102616 | SCM-EWM-AUT | SCM-EWM-CFG-2CL |
| SAP_CA_BC_IC_LND_SCM_EWM_PC | Warehouse Management - Configuration | /SCWM/22000160 | SCWM_22000160_TRAN | /SCWM/V_T3010SSC | Maintain Storage Types | 102666 | SCM-EWM-AUT | SCM-EWM-WOP-2CL |
| SAP_CA_BC_IC_LND_SCM_EWM_PC | Warehouse Management - Configuration | /SCWM/09000019 | SCWM_09000019_TRAN | /SCWM/V_PI_TOL | Define Tolerance Group for Difference Analyzer | 102539 | SCM-EWM-AUT | SCM-EWM-CFG-2CL |
| SAP_CA_BC_IC_LND_SCM_EWM_PC | Warehouse Management - Configuration | /SCWM/22000158 | SCWM_22000158_TRAN | /SCWM/V_T300MSSC | Set Warehouse Address | 102657 | SCM-EWM-AUT | SCM-EWM-CFG-2CL |
| SAP_CA_BC_IC_LND_SCM_EWM_PC | Warehouse Management - Configuration | /SCWM/09000682 | SCWM_09000682_TRAN | /SCWM/V_TOL_POST | Define Tolerance Group for Posting Differences | 102585 | SCM-EWM-AUT | SCM-EWM-CFG-2CL |
| SAP_CA_BC_IC_LND_SCM_EWM_PC | Warehouse Management - Configuration | /SCWM/41000004 | SCWM_41000004_TRAN | /SCWM/TUOM_QCLA | Define Unit of Measure Attributes | 102506 | SCM-EWM-AUT | SCM-EWM-CFG-2CL |
| SAP_CA_BC_IC_LND_SCM_EWM_PC | Warehouse Management - Configuration | S_ER9_52000775 | S_ER9_52000775_TRAN | V_T340DL | Define Default Values for Deliveries | 101303 | SCM-EWM-AUT | SCM-EWM-IF-ERP-2CL |
| SAP_CA_BC_IC_LND_SCM_EWM_PC | Warehouse Management - Configuration | /SCWM/60000119 | SCWM_60000119_TRAN | /SCWM/V_T343XYZ | Define Storage Bin Structure | 104289 | SCM-EWM-AUT | SCM-EWM-CFG-2CL |
| SAP_CA_BC_IC_LND_SCM_EWM_PC | Warehouse Management - Configuration | /SCWM/60000067 | SCWM_60000067_TRAN | /SCWM/V_TREPA | Activate Replenishment Strategies in Storage Types | 103343 | SCM-EWM-AUT | SCM-EWM-CFG-2CL |
| SAP_CA_BC_IC_LND_SCM_EWM_PC | Warehouse Management - Configuration | /SCWM/60000164 | SCWM_60000164_TRAN | /SCWM/RMDEFINEBAT | Define Bin Access Types | 104287 | SCM-EWM-AUT | SCM-EWM-CFG-2CL |
| SAP_CA_BC_IC_LND_SCM_EWM_PC | Warehouse Management - Configuration | /SCWM/60000290 | SCWM_60000290_TRAN | /SCWM/T331C | Storage Type Control: Near to Picking Fixed Bin | 104283 | SCM-EWM-AUT | SCM-EWM-CFG-2CL |
| SAP_CA_BC_IC_LND_SCM_EWM_PC | Warehouse Management - Configuration | /SCWM/60000285 | SCWM_60000285_TRAN | /SCWM/T337A | Define Bin Sections | 104280 | SCM-EWM-AUT | SCM-EWM-CFG-2CL |
| SAP_CA_BC_IC_LND_SCM_EWM_PC | Warehouse Management - Configuration | /SCWM/22000230 | SCWM_22000230_TRAN | /SCWM/SERIPROF | Define Serial Number Profiles | 103636 | SCM-EWM-AUT | SCM-EWM-CFG-2CL |
| SAP_CA_BC_IC_LND_SCM_EWM_PC | Warehouse Management - Configuration | /SCWM/60000635 | SCWM_60000635_TRAN | /SCWM/V_TPRF_ACT | Activate Process Block Profile | 104292 | SCM-EWM-AUT | SCM-EWM-CFG-2CL |
| SAP_CA_BC_IC_LND_SCM_EWM_PC | Warehouse Management - Configuration | /SCWM/60000287 | SCWM_60000287_TRAN | /SCWM/T331B | Storage Type Control for Bulk Storage | 104282 | SCM-EWM-AUT | SCM-EWM-CFG-2CL |
| SAP_CA_BC_IC_LND_SCM_EWM_PC | Warehouse Management - Configuration | /SCWM/60000199 | SCWM_60000199_TRAN | /SCWM/T305Q | Define Putaway Control Indicator | 104279 | SCM-EWM-AUT | SCM-EWM-CFG-2CL |
| SAP_CA_BC_IC_LND_SCM_EWM_PC | Warehouse Management - Configuration | /SCWM/60000076 | SCWM_60000076_TRAN | /SCWM/TWRKTYP | Specify Work Center Layout | 104260 | SCM-EWM-AUT | SCM-EWM-CFG-2CL |
| SAP_CA_BC_IC_LND_SCM_EWM_PC | Warehouse Management - Configuration | /SCWM/52001796 | SCWM_52001796_TRAN | /SCWM/V_THUNR_S4 | Assign Number Range Intervals to Packaging Material Types | 103418 | SCM-EWM-AUT | SCM-EWM-IF-ERP-2CL |
| SAP_CA_BC_IC_LND_SCM_EWM_PC | Warehouse Management - Configuration | S_AXA_22000088 | S_AXA_22000088_TRAN | SCM_DEZSYS_TWHMATGR | Define Warehouse Material Group | 104278 | SCM-EWM-AUT | SCM-EWM-IF-ERP-2CL |
| SAP_CA_BC_IC_LND_SCM_EWM_PC | Warehouse Management - Configuration | /SCWM/60000077 | SCWM_60000077_TRAN | /SCWM/TWORKST | Define Work Center | 104259 | SCM-EWM-AUT | SCM-EWM-CFG-2CL |
| SAP_CA_BC_IC_LND_SCM_EWM_PC | Warehouse Management - Configuration | /SCWM/60000291 | SCWM_60000291_TRAN | /SCWM/T337C | Define Search Scope for Each Level | 104284 | SCM-EWM-AUT | SCM-EWM-CFG-2CL |
| SAP_CA_BC_IC_LND_SCM_EWM_PC | Warehouse Management - Configuration | /SCWM/60000174 | SCWM_60000174_TRAN | /SCWM/VC_PROCPROFL | Define Process Block Profile | 104291 | SCM-EWM-AUT | SCM-EWM-CFG-2CL |
| SAP_CA_BC_IC_LND_SCM_EWM_PC | Warehouse Management - Configuration | /SCWM/47000118 | SCWM_47000118_TRAN | /SCWM/V_DIFF_REA | Define Reason for Differences | 104299 | SCM-EWM-AUT | SCM-EWM-CFG-2CL |
| SAP_CA_BC_IC_LND_SCM_EWM_PC | Warehouse Management - Configuration | /SCWM/60000286 | SCWM_60000286_TRAN | /SCWM/T337Z | Perform Bin Sectioning for Bin Type and HU Type | 104281 | SCM-EWM-AUT | SCM-EWM-CFG-2CL |
| SAP_CA_BC_IC_LND_SCM_EWM_PC | Warehouse Management - Configuration | /SCWM/60000091 | SCWM_60000091_TRAN | /SCWM/TMAPWHNUM | Assign Warehouse Numbers from Logistics Execution | 102715 | SCM-EWM-AUT | SCM-EWM-CFG-2CL |
| SAP_CA_BC_IC_LND_SCM_EWM_PC | Warehouse Management - Configuration | /SCWM/60000118 | SCWM_60000118_TRAN | /SCWM/V_T343G | Define Storage Bin Identifiers for Storage Bin Structures | 104288 | SCM-EWM-AUT | SCM-EWM-CFG-2CL |
| SAP_CA_BC_IC_LND_SCM_EWM_PC | Warehouse Management - Configuration | /SCWM/22000144 | SCWM_22000144_TRAN | /SCWM/VABINCD | Activate Change Documents for Storage Bins | 104290 | SCM-EWM-AUT | SCM-EWM-CFG-2CL |
| SAP_CA_BC_IC_LND_SCM_EWM_PC | Warehouse Management - Configuration | S_AXA_22000087 | S_AXA_22000087_TRAN | SCM_DEZSYS_TWHSTC | Define Warehouse Storage Condition | 104285 | SCM-EWM-AUT | SCM-EWM-IF-ERP-2CL |
| SAP_CA_BC_IC_LND_SCM_EWM_PC | Warehouse Management - Configuration | /SCWM/22000154_CE | SCWM_22000154_CE_TRAN |  |  |  | SCM-EWM-AUT |  |
| SAP_CA_BC_IC_LND_SCM_EWM_PC | Warehouse Management - Configuration | /SCWM/52001959 | SCWM_52001959_TRAN | /SCWM/V_TGTL | Maintain GTL Generation for Each Warehouse Number | 103512 | SCM-EWM-AUT | SCM-EWM-IF-ERP-2CL |
| SAP_CA_BC_IC_LND_SCM_EWM_PC | Warehouse Management - Configuration | /SCWM/60000117 | SCWM_60000117_TRAN | /SCWM/V_T303 | Define Storage Bin Types | 104286 | SCM-EWM-AUT | SCM-EWM-CFG-2CL |
| SAP_CA_BC_IC_LND_SCM_EWM_PC | Warehouse Management - Configuration | /SCWM/09000408 | SCWM_09000408_TRAN | /SCWM/TPACKSTDTA | Optimize Work Center Determination in Goods Issue | 104258 | SCM-EWM-AUT | SCM-EWM-CFG-2CL |
| SAP_CA_BC_IC_LND_SCM_EWM_PC | Warehouse Management - Configuration | /SCWM/22000278 | SCWM_22000278_TRAN | /SCWM/V_T333SSC | Define Warehouse Process Type | 103863 | SCM-EWM-AUT | SCM-EWM-CFG-2CL |
| SAP_CA_BC_IC_LND_SCM_EWM_PC | Warehouse Management - Configuration | /SCWM/60000190 | SCWM_60000190_TRAN | /SCWM/V_T3001_CU | Define Warehouse Numbers | 102399 | SCM-EWM-AUT | SCM-EWM-CFG-2CL |
| SAP_CA_BC_IC_LND_SCM_EWM_PC | Warehouse Management - Configuration | S_AXA_22000089 | S_AXA_22000089_TRAN | SCM_DEZSYS_THNDLCD | Define Handling Indicator | 104294 | SCM-EWM-AUT | SCM-EWM-IF-ERP-2CL |
| SAP_CA_BC_IC_LND_SCM_EWM_PC | Warehouse Management - Configuration | /SCWM/0SSCC |  | /SCWM/SNRO | Define Number Range Intervals for SSCC | 102867 | SCM-EWM-AUT | SCM-EWM-CFG-2CL |
| SAP_CA_BC_IC_LND_SCM_EWM_PC | Warehouse Management - Configuration | /SCWM/09000683 | SCWM_09000683_TRAN | /SCWM/V_TOL_RECO | Define Tolerance Group for Recounting | 104304 | SCM-EWM-AUT | SCM-EWM-CFG-2CL |
| SAP_CA_BC_IC_LND_SCM_EWM_PC | Warehouse Management - Configuration | /SCWM/60000630 | SCWM_60000630_TRAN | /SCWM/PI_V_LGNUM | Specify Physical-Inventory-Specific Settings in the Warehouse | 104314 | SCM-EWM-AUT | SCM-EWM-CFG-2CL |
| SAP_CA_BC_IC_LND_SCM_EWM_PC | Warehouse Management - Configuration | OIS2 |  | /SCWM/SERIPROF | Define Serial Number Profiles | 103636 | SCM-EWM-AUT | SCM-EWM-CFG-2CL |
| SAP_CA_BC_IC_LND_SCM_EWM_PC | Warehouse Management - Configuration | /SCWM/09000293 | SCWM_09000293_TRAN | /SCWM/PICUST_PRI | Define Priorities | 104305 | SCM-EWM-AUT | SCM-EWM-CFG-2CL |
| SAP_CA_BC_IC_LND_SCM_EWM_PC | Warehouse Management - Configuration | /SCWM/09000295 | SCWM_09000295_TRAN | /SCWM/PICUST_DTY | Define Standard Reason for Each Phys. Inv. Procedure | 104315 | SCM-EWM-AUT | SCM-EWM-CFG-2CL |
| SAP_CA_BC_IC_LND_SCM_EWM_PC | Warehouse Management - Configuration | /SCWM/22000246 | SCWM_22000246_TRAN | /SCWM/VAPASCD | Activate Change Documents for Preallocated Stock | 104386 | SCM-EWM-AUT | SCM-EWM-CFG-2CL |
| SAP_CA_BC_IC_LND_SCM_EWM_PC | Warehouse Management - Configuration | /SCWM/PIDO |  | /SCWM/PIDO | Define Number Range for Physical Inventory Documents | 104384 | SCM-EWM-AUT | SCM-EWM-CFG-2CL |
| SAP_CA_BC_IC_LND_SCM_EWM_PC | Warehouse Management - Configuration | /SCWM/60000228 | SCWM_60000228_TRAN | /SCWM/THUTYPG | Define HU Type Groups | 104334 | SCM-EWM-AUT | SCM-EWM-CFG-2CL |
| SAP_CA_BC_IC_LND_SCM_EWM_PC | Warehouse Management - Configuration | /SCWM/60000575 | SCWM_60000575_TRAN | /SCWM/TQUANCLA | Define Quantity Classifications | 106847 | SCM-EWM-AUT | SCM-EWM-CFG-2CL |
| SAP_CA_BC_IC_LND_SCM_EWM_PC | Warehouse Management - Configuration | /SCWM/41000133 | SCWM_41000133_TRAN | /SCWM/V_T_333_BB | Define Control for Blocking Storage Bins | 104316 | SCM-EWM-AUT | SCM-EWM-CFG-2CL |
| SAP_CA_BC_IC_LND_SCM_EWM_PC | Warehouse Management - Configuration | /SCWM/60000346 | SCWM_60000346_TRAN | /SCWM/TFBIN_UNAS | Configure Deletion of Fixed Bin Assignments | 104296 | SCM-EWM-AUT | SCM-EWM-CFG-2CL |
| SAP_CA_BC_IC_LND_SCM_EWM_PC | Warehouse Management - Configuration | /SCWM/22000174 | SCWM_22000174_TRAN | /SCWM/V_T3000_CE | Define Warehouse Number Control | 104735 | SCM-EWM-AUT | SCM-EWM-CFG-2CL |
| SAP_CA_BC_IC_LND_SCM_EWM_PC | Warehouse Management - Configuration | /SCWM/09000294 | SCWM_09000294_TRAN | /SCWM/PICUST_REA | Define Reason for Physical Inventory | 104341 | SCM-EWM-AUT | SCM-EWM-CFG-2CL |
| SAP_CA_BC_IC_LND_SCM_EWM_PC | Warehouse Management - Configuration | /SCWM/60000383 | SCWM_60000383_TRAN | /SCWM/TPTDETIND | Define Control Indicators for Determining Warehouse Process Types | 106846 | SCM-EWM-AUT | SCM-EWM-CFG-2CL |
| SAP_CA_BC_IC_LND_SCM_EWM_PC | Warehouse Management - Configuration | /SCWM/60000542 | SCWM_60000542_TRAN | /SCWM/TDRDETGR | Define Staging Area and Door Determination Groups | 104333 | SCM-EWM-AUT | SCM-EWM-CFG-2CL |
| SAP_CA_BC_IC_LND_SCM_EWM_PC | Warehouse Management - Configuration | /SCMB/72000013 | SCMB_72000013_TRAN | /SCMB/TIDART | Define Identification Types for Assigning to Handling Units | 104335 | SCM-EWM-AUT | SCM-BAS-IMG |
| SAP_CA_BC_IC_LND_SCM_EWM_PC | Warehouse Management - Configuration | /SCWM/09000028 | SCWM_09000028_TRAN | /SCWM/TROUTLS | Define Storage Groups for Layout-Oriented Storage Control | 106848 | SCM-EWM-AUT | SCM-EWM-CFG-2CL |
| SAP_CA_BC_IC_LND_SCM_EWM_PC | Warehouse Management - Configuration | /SCWM/60000064 | SCWM_60000064_TRAN | /SCWM/TROUTL | Define Layout-Oriented Storage Process Control | 106849 | SCM-EWM-AUT | SCM-EWM-CFG-2CL |
| SAP_CA_BC_IC_LND_SCM_EWM_PC | Warehouse Management - Configuration | /SCWM/60000116 | SCWM_60000116_TRAN | /SCWM/TSTAREA_V | Define Staging Areas | 104332 | SCM-EWM-AUT | SCM-EWM-CFG-2CL |
| SAP_CA_BC_IC_LND_SCM_EWM_PC | Warehouse Management - Configuration | /SCWM/60000632 | SCWM_60000632_TRAN | /SCWM/PIDO | Define Number Range for Physical Inventory Documents | 104384 | SCM-EWM-AUT | SCM-EWM-CFG-2CL |
| SAP_CA_BC_IC_LND_SCM_EWM_PC | Warehouse Management - Configuration | S_AXA_22000086 | S_AXA_22000086_TRAN | SCM_DEZSYS_HUTYPDEF | Define Handling Unit Type | 104336 | SCM-EWM-AUT | SCM-EWM-IF-ERP-2CL |
| SAP_CA_BC_IC_LND_SCM_EWM_PC | Warehouse Management - Configuration | /SCWM/22000245 | SCWM_22000245_TRAN | /SCWM/VPASRCAT | Define Preallocated-Stock References | 104385 | SCM-EWM-AUT | SCM-EWM-CFG-2CL |
| SAP_CA_BC_IC_LND_SCM_EWM_PC | Warehouse Management - Configuration | /SCWM/22000296 | SCWM_22000296_TRAN | /SCWM/V_TWPTDSSC | Determine Warehouse Process Type | 104392 | SCM-EWM-AUT | SCM-EWM-CFG-2CL |
| SAP_CA_BC_IC_LND_SCM_EWM_PC | Warehouse Management - Configuration | /SCWM/22000297 | SCWM_22000297_TRAN | /SCWM/V_T333CSSC | Assign Storage Bins to Warehouse Process Type | 104391 | SCM-EWM-AUT | SCM-EWM-CFG-2CL |
| SAP_CA_BC_IC_LND_SCM_EWM_PC | Warehouse Management - Configuration | /SCWM/60000062 | SCWM_60000062_TRAN | /SCWM/V_STCKDTGR | Maintain Stock Determination Groups | 104394 | SCM-EWM-AUT | SCM-EWM-CFG-2CL |
| SAP_CA_BC_IC_LND_SCM_EWM_PC | Warehouse Management - Configuration | /SCWM/22000295 | SCWM_22000295_TRAN | /SCWM/V_MG_STDAS | Assign Partners to Groups for Stock Determination | 104397 | SCM-EWM-AUT | SCM-EWM-CFG-2CL |
| SAP_CA_BC_IC_LND_SCM_EWM_PC | Warehouse Management - Configuration | /SCWM/22000294 | SCWM_22000294_TRAN | /SCWM/V_MG_STCKD | Maintain Groups of Partners for Stock Determination | 104396 | SCM-EWM-AUT | SCM-EWM-CFG-2CL |
| SAP_CA_BC_IC_LND_SCM_EWM_PC | Warehouse Management - Configuration | /SCWM/22000293 | SCWM_22000293_TRAN | /SCWM/V_STOCKDET | Configure Stock Determination | 104395 | SCM-EWM-AUT | SCM-EWM-CFG-2CL |
| SAP_CA_BC_IC_LND_SCM_EWM_PC | Warehouse Management - Configuration | /SCWM/60000226 | SCWM_60000226_TRAN | /SCWM/V_T334E | Define HU Types for Each Storage Type | 104388 | SCM-EWM-AUT | SCM-EWM-CFG-2CL |
| SAP_CA_BC_IC_LND_SCM_EWM_PC | Warehouse Management - Configuration | S_P99_41000250 | S_P99_41000250_TRAN | SIMG_HUMIDHUEX | Number Range Maintenance for HU Identification | 103442 | SCM-EWM-AUT | LO-HU-2CL |
| SAP_CA_BC_IC_LND_SCM_EWM_PC | Warehouse Management - Configuration | /SCWM/22000298 | SCWM_22000298_TRAN | /SCWM/VC_MOVE_RSNSSC | Configure Reasons for Warehouse Movements | 104393 | SCM-EWM-AUT | SCM-EWM-CFG-2CL |
| SAP_CA_BC_IC_LND_SCM_EWM_PC | Warehouse Management - Configuration | S_ALR_87006780 | S_ALR_87006780_TRAN | SIMG_CFMENUOLSDVEGR | Define Material Group for Packaging Materials | 103927 | SCM-EWM-AUT | LO-HU-2CL |
| SAP_CA_BC_IC_LND_SCM_EWM_PC | Warehouse Management - Configuration | /SCWM/60000574 | SCWM_60000574_TRAN | /SCWM/TBINTYPSQ2 | Alternative Storage Bin Type Sequence | 104724 | SCM-EWM-AUT | SCM-EWM-CFG-2CL |
| SAP_CA_BC_IC_LND_SCM_EWM_PC | Warehouse Management - Configuration | S_ALR_87006781 | S_ALR_87006781_TRAN | SIMG_CFMENUOLSDVHZU | Define Allowed Packaging Materials | 103925 | SCM-EWM-AUT | LO-HU-2CL |
| SAP_CA_BC_IC_LND_SCM_EWM_PC | Warehouse Management - Configuration | HUEX |  | SIMG_HUMIDHUEX | Number Range Maintenance for HU Identification | 103442 | SCM-EWM-AUT | LO-HU-2CL |
| SAP_CA_BC_IC_LND_SCM_EWM_PC | Warehouse Management - Configuration | /SCWM/60000284 | SCWM_60000284_TRAN | /SCWM/TBINTYP_SQ | Define HU Types for Each Storage Bin Type | 104387 | SCM-EWM-AUT | SCM-EWM-CFG-2CL |
| SAP_CA_BC_IC_LND_SCM_EWM_PC | Warehouse Management - Configuration | /SCWM/60000206 | SCWM_60000206_TRAN | /SCWM/V_T334QS_N | Assign Storage Types to Storage Type Search Sequence | 104732 | SCM-EWM-AUT | SCM-EWM-CFG-2CL |
| SAP_CA_BC_IC_LND_SCM_EWM_PC | Warehouse Management - Configuration | /SCWM/60000225 | SCWM_60000225_TRAN | /SCWM/V_T307 | Define HU Types for Each Warehouse Number and Assign HU Type Group | 104383 | SCM-EWM-AUT | SCM-EWM-CFG-2CL |
| SAP_CA_BC_IC_LND_SCM_EWM_PC | Warehouse Management - Configuration | /SCWM/60000204 | SCWM_60000204_TRAN | /SCWM/T334QSD | Define Storage Type Search Sequence for Putaway | 104731 | SCM-EWM-AUT | SCM-EWM-CFG-2CL |
| SAP_CA_BC_IC_LND_SCM_EWM_PC | Warehouse Management - Configuration | /SCWM/60000282 | SCWM_60000282_TRAN | /SCWM/V_T334QA | Optimize Access Strategy for Storage Type Search: Putaway | 104730 | SCM-EWM-AUT | SCM-EWM-CFG-2CL |
| SAP_CA_BC_IC_LND_SCM_EWM_PC | Warehouse Management - Configuration | /SCWM/60000281 | SCWM_60000281_TRAN | /SCWM/T334Q | Specify Storage Type Search Sequence for Putaway | 104733 | SCM-EWM-AUT | SCM-EWM-CFG-2CL |
| SAP_CA_BC_IC_LND_SCM_EWM_PC | Warehouse Management - Configuration | /SCWM/22000005 | SCWM_22000005_TRAN | /SCWM/T303S | Assign Storage Bin Types to Storage Types | 104725 | SCM-EWM-AUT | SCM-EWM-CFG-2CL |
| SAP_CA_BC_IC_LND_SCM_EWM_PC | Warehouse Management - Configuration | /SCWM/60000061 | SCWM_60000061_TRAN | /SCWM/TPROCTYG | Define Group for Process Types | 104463 | SCM-EWM-AUT | SCM-EWM-CFG-2CL |
| SAP_CA_BC_IC_LND_SCM_EWM_PC | Warehouse Management - Configuration | /SCWM/30000042 | SCWM_30000042_TRAN | /SCWM/V_T347 | Define Queue Types | 104700 | SCM-EWM-AUT | SCM-EWM-CFG-2CL |
| SAP_CA_BC_IC_LND_SCM_EWM_PC | Warehouse Management - Configuration | /SCWM/60000060 | SCWM_60000060_TRAN | /SCWM/TCATG | Define Group for Stock Type | 104462 | SCM-EWM-AUT | SCM-EWM-CFG-2CL |
| SAP_CA_BC_IC_LND_SCM_EWM_PC | Warehouse Management - Configuration | /SCWM/ERPDOCNO |  | /SCWM/ERPDOCNO | Define Number Ranges for LE Deliveries | 104695 | SCM-EWM-AUT | SCM-EWM-CFG-2CL |
| SAP_CA_BC_IC_LND_SCM_EWM_PC | Warehouse Management - Configuration | /SCWM/60000202 | SCWM_60000202_TRAN | /SCWM/TSECT_SQ | Maintain Storage Section Search Sequence | 104664 | SCM-EWM-AUT | SCM-EWM-CFG-2CL |
| SAP_CA_BC_IC_LND_SCM_EWM_PC | Warehouse Management - Configuration | /SCWM/60000201 | SCWM_60000201_TRAN | /SCWM/V_T304 | Create Storage Section Indicators | 104447 | SCM-EWM-AUT | SCM-EWM-CFG-2CL |
| SAP_CA_BC_IC_LND_SCM_EWM_PC | Warehouse Management - Configuration | /SCWM/60000052 | SCWM_60000052_TRAN | /SCWM/V_T301M | Assign Storage Types to Storage Type Groups | 104446 | SCM-EWM-AUT | SCM-EWM-CFG-2CL |
| SAP_CA_BC_IC_LND_SCM_EWM_PC | Warehouse Management - Configuration | /SCWM/60000527 | SCWM_60000527_TRAN | /SCWM/V_ACT_TID | Assign Activities to Text Identifiers | 104693 | SCM-EWM-AUT | SCM-EWM-CFG-2CL |
| SAP_CA_BC_IC_LND_SCM_EWM_PC | Warehouse Management - Configuration | /SCWM/60000051 | SCWM_60000051_TRAN | /SCWM/T301G | Define Storage Type Groups | 104445 | SCM-EWM-AUT | SCM-EWM-CFG-2CL |
| SAP_CA_BC_IC_LND_SCM_EWM_PC | Warehouse Management - Configuration | /SCWM/VITYPE_O |  | /SCWM/VITYPE_O | Define Item Types for Outbound Delivery Process | 106702 | SCM-EWM-AUT | SCM-EWM-CFG-2CL |
| SAP_CA_BC_IC_LND_SCM_EWM_PC | Warehouse Management - Configuration | /SCWM/70000853 | SCWM_70000853_TRAN | /SCWM/VITYPE_O | Define Item Types for Outbound Delivery Process | 106702 | SCM-EWM-AUT | SCM-EWM-CFG-2CL |
| SAP_CA_BC_IC_LND_SCM_EWM_PC | Warehouse Management - Configuration | /SCWM/60000401 | SCWM_60000401_TRAN | /SCWM/ERPDOCNO | Define Number Ranges for LE Deliveries | 104695 | SCM-EWM-AUT | SCM-EWM-CFG-2CL |
| SAP_CA_BC_IC_LND_SCM_EWM_PC | Warehouse Management - Configuration | /SCWM/V_TIMCBWA |  | /SCWM/V_TIMCBWA_SSC | Define Customer Movement Types in WM | 104710 | SCM-EWM-AUT | SCM-EWM-CFG-2CL |
| SAP_CA_BC_IC_LND_SCM_EWM_PC | Warehouse Management - Configuration | /SCWM/60000120 | SCWM_60000120_TRAN | /SCWM/V_TACTTY | Define Activities for Activity Areas | 104701 | SCM-EWM-AUT | SCM-EWM-CFG-2CL |
| SAP_CA_BC_IC_LND_SCM_EWM_PC | Warehouse Management - Configuration | /SCWM/22000312 | SCWM_22000312_TRAN | /SCWM/TWCRSORTDSSC | Define Sort Rules for Warehouse Tasks | 104704 | SCM-EWM-AUT | SCM-EWM-CFG-2CL |
| SAP_CA_BC_IC_LND_SCM_EWM_PC | Warehouse Management - Configuration | /SCWM/VC_DLVPACI |  | /SCWM/VC_DLVPACI | Automatically Generate Packaging Items for Outbound Delivery Orders | 106790 | SCM-EWM-AUT | SCM-EWM-CFG-2CL |
| SAP_CA_BC_IC_LND_SCM_EWM_PC | Warehouse Management - Configuration | S_ER9_52001950 | S_ER9_52001950_TRAN | SIMG_TVHUGTLNRO | Define Number Range Intervals for GTL | 103522 | SCM-EWM-AUT | LO-HU-2CL |
| SAP_CA_BC_IC_LND_SCM_EWM_PC | Warehouse Management - Configuration | /SCWM/22000349 | SCWM_22000349_TRAN | /SCWM/VC_TSGMACT | Activate Synchronous Goods Movements in the Warehouse | 105672 | SCM-EWM-AUT | SCM-EWM-CFG-2CL |
| SAP_CA_BC_IC_LND_SCM_EWM_PC | Warehouse Management - Configuration | /SCMB/05000017 | SCMB_05000017_TRAN | /SCMB/V_PB_PROFX | Define Unified Package Building Profile | 105798 | SCM-EWM-AUT | SCM-BAS-IMG |
| SAP_CA_BC_IC_LND_SCM_EWM_PC | Warehouse Management - Configuration | /SCWM/22000310 | SCWM_22000310_TRAN | /SCWM/V_T340DA_SSC | Assign Number Range Intervals to Warehouse Number | 104734 | SCM-EWM-AUT | SCM-EWM-CFG-2CL |
| SAP_CA_BC_IC_LND_SCM_EWM_PC | Warehouse Management - Configuration | /SCWM/22000314 | SCWM_22000314_TRAN | /SCWM/WHONUMSSC | Define Number Range Intervals for Warehouse Orders | 104708 | SCM-EWM-AUT | SCM-EWM-CFG-2CL |
| SAP_CA_BC_IC_LND_SCM_EWM_PC | Warehouse Management - Configuration | /SCWM/22000331 | SCWM_22000331_TRAN | /SCWM/TAVLGROUP_SSC | Define Availability Group | 105114 | SCM-EWM-AUT | SCM-EWM-CFG-2CL |
| SAP_CA_BC_IC_LND_SCM_EWM_PC | Warehouse Management - Configuration | /SCWM/22000135 | SCWM_22000135_TRAN | /SCWM/VC_RF_SKIPHU | Control Display of Pick-HU Screen During RF Picking | 104452 | SCM-EWM-AUT | SCM-EWM-CFG-2CL |
| SAP_CA_BC_IC_LND_SCM_EWM_PC | Warehouse Management - Configuration | /SCWM/52002703 | SCWM_52002703_TRAN | /SCWM/QFUCODE_S4SSCU | Maintain Follow-Up Actions | 104709 | SCM-EWM-AUT | SCM-EWM-IF-ERP-2CL |
| SAP_CA_BC_IC_LND_SCM_EWM_PC | Warehouse Management - Configuration | /SCWM/41000087 | SCWM_41000087_TRAN | /SCWM/TDLVBATCH | Define Setting for Delivery - Warehouse Request | 104697 | SCM-EWM-AUT | SCM-EWM-CFG-2CL |
| SAP_CA_BC_IC_LND_SCM_EWM_PC | Warehouse Management - Configuration | /SCWM/60000176 | SCWM_60000176_TRAN | /SCWM/V_WAVETYPE | Maintain Wave Types | 104729 | SCM-EWM-AUT | SCM-EWM-CFG-2CL |
| SAP_CA_BC_IC_LND_SCM_EWM_PC | Warehouse Management - Configuration | /SCWM/60000326 | SCWM_60000326_TRAN | /SCWM/TDOOR | Define Warehouse Door | 106083 | SCM-EWM-AUT | SCM-EWM-CFG-2CL |
| SAP_CA_BC_IC_LND_SCM_EWM_PC | Warehouse Management - Configuration | /SCWM/09000191 | SCWM_09000191_TRAN | /SCWM/TWAVE_CAPA | Maintain Wave Capacity Profiles | 104726 | SCM-EWM-AUT | SCM-EWM-CFG-2CL |
| SAP_CA_BC_IC_LND_SCM_EWM_PC | Warehouse Management - Configuration | /SCWM/69000021 | SCWM_69000021_TRAN | /SCWM/V_T340_MFG | Maintain Warehouse Parameters for Production | 104728 | SCM-EWM-AUT | SCM-EWM-CFG-2CL |
| SAP_CA_BC_IC_LND_SCM_EWM_PC | Warehouse Management - Configuration | /SCWM/60000056 | SCWM_60000056_TRAN | /SCWM/V_T334RS | Specify Storage Type Search Sequence | 104683 | SCM-EWM-AUT | SCM-EWM-CFG-2CL |
| SAP_CA_BC_IC_LND_SCM_EWM_PC | Warehouse Management - Configuration | HUGTLNRO |  | SIMG_TVHUGTLNRO | Define Number Range Intervals for GTL | 103522 | SCM-EWM-AUT | LO-HU-2CL |
| SAP_CA_BC_IC_LND_SCM_EWM_PC | Warehouse Management - Configuration | /SCWM/82000009 | SCWM_82000009_TRAN | /SCWM/T334R | Determine Storage Type Search Sequence for Stock Removal | 104685 | SCM-EWM-AUT | SCM-EWM-WOP-2CL |
| SAP_CA_BC_IC_LND_SCM_EWM_PC | Warehouse Management - Configuration | /SCWM/22000315 | SCWM_22000315_TRAN | /SCWM/V_TIMCBWA_SSC | Define Customer Movement Types in WM | 104710 | SCM-EWM-AUT | SCM-EWM-CFG-2CL |
| SAP_CA_BC_IC_LND_SCM_EWM_PC | Warehouse Management - Configuration | /SCWM/VC_TSGMACT |  | /SCWM/VC_TSGMACT | Activate Synchronous Goods Movements in the Warehouse | 105672 | SCM-EWM-AUT | SCM-EWM-CFG-2CL |
| SAP_CA_BC_IC_LND_SCM_EWM_PC | Warehouse Management - Configuration | /SCWM/60000128 | SCWM_60000128_TRAN | /SCWM/TWCRFILTER | Define Filters for Warehouse Order Creation Rules | 104706 | SCM-EWM-AUT | SCM-EWM-CFG-2CL |
| SAP_CA_BC_IC_LND_SCM_EWM_PC | Warehouse Management - Configuration | /SCWM/22000313 | SCWM_22000313_TRAN | /SCWM/V_TWCRSORTSSC | Assign Sort Fields for Warehouse Tasks | 104705 | SCM-EWM-AUT | SCM-EWM-CFG-2CL |
| SAP_CA_BC_IC_LND_SCM_EWM_PC | Warehouse Management - Configuration | /SCWM/41000063 | SCWM_41000063_TRAN | /SCWM/TTYPE_I | Define Document Types for Inbound Delivery Process | 105786 | SCM-EWM-AUT | SCM-EWM-CFG-2CL |
| SAP_CA_BC_IC_LND_SCM_EWM_PC | Warehouse Management - Configuration | /SCWM/22000327 | SCWM_22000327_TRAN | /SCWM/WAVENUM | Define Number Range Intervals for Waves | 104736 | SCM-EWM-AUT | SCM-EWM-CFG-2CL |
| SAP_CA_BC_IC_LND_SCM_EWM_PC | Warehouse Management - Configuration | /SCWM/VCTRLPR_DC |  | /SCWM/VCTRLPR_DC | Set Control Parameters for ERP Version Control | 106376 | SCM-EWM-AUT | SCM-EWM-CFG-2CL |
| SAP_CA_BC_IC_LND_SCM_EWM_PC | Warehouse Management - Configuration | /SCWM/52001314 | SCWM_52001314_TRAN | /SCWM/QIOTWM_NIR_S4 | Define and Activate Warehouse-Dependent IOTs | 104666 | SCM-EWM-AUT | SCM-EWM-IF-ERP-2CL |
| SAP_CA_BC_IC_LND_SCM_EWM_PC | Warehouse Management - Configuration | /SCWM/60000057 | SCWM_60000057_TRAN | /SCWM/T334RA | Optimize Access Strategies for Stor. Type Determination in Stock Removal | 104686 | SCM-EWM-AUT | SCM-EWM-CFG-2CL |
| SAP_CA_BC_IC_LND_SCM_EWM_PC | Warehouse Management - Configuration | /SCWM/60000177 | SCWM_60000177_TRAN | /SCWM/V_WAVECAT | Maintain Wave Categories | 104720 | SCM-EWM-AUT | SCM-EWM-CFG-2CL |
| SAP_CA_BC_IC_LND_SCM_EWM_PC | Warehouse Management - Configuration | /SCWM/22000330 | SCWM_22000330_TRAN | /SCWM/V_TMAPSTLO_SSC | Map Storage Locations to the Warehouse | 105113 | SCM-EWM-AUT | SCM-EWM-CFG-2CL |
| SAP_CA_BC_IC_LND_SCM_EWM_PC | Warehouse Management - Configuration | S_ER9_52001696 | S_ER9_52001696_TRAN | SIMG_CFMENUOCHADBNR | Define Batch Number Ranges | 103291 | SCM-EWM-AUT | LO-BM-2CL |
| SAP_CA_BC_IC_LND_SCM_EWM_PC | Warehouse Management - Configuration | /SCWM/23000037 | SCWM_23000037_TRAN | /SCWM/VC_DLVPACI | Automatically Generate Packaging Items for Outbound Delivery Orders | 106790 | SCM-EWM-AUT | SCM-EWM-CFG-2CL |
| SAP_CA_BC_IC_LND_SCM_EWM_PC | Warehouse Management - Configuration | /SCWM/22000226 | SCWM_22000226_TRAN | /SCWM/V_T340WSIM | Define Wave Simulation Settings | 104722 | SCM-EWM-AUT | SCM-EWM-CFG-2CL |
| SAP_CA_BC_IC_LND_SCM_EWM_PC | Warehouse Management - Configuration | /SCMB/UPB_PROFILE |  | /SCMB/V_PB_PROFX | Define Unified Package Building Profile | 105798 | SCM-EWM-AUT | SCM-BAS-IMG |
| SAP_CA_BC_IC_LND_SCM_EWM_PC | Warehouse Management - Configuration | /SCWM/59000014 | SCWM_59000014_TRAN | /SCWM/VC_MPHU_DET | Define Confirmation Methods for Pick-HUs | 106967 | SCM-EWM-AUT | SCM-EWM-CFG-2CL |
| SAP_CA_BC_IC_LND_SCM_EWM_PC | Warehouse Management - Configuration | /SCWM/VHULBL_PRC |  | /SCWM/VHULBL_PRC | Control Automatic Printing of HU Labels for Processes | 106993 | SCM-EWM-AUT | SCM-EWM-CFG-2CL |
| SAP_CA_BC_IC_LND_SCM_EWM_PC | Warehouse Management - Configuration | /SCWM/60000166 | SCWM_60000166_TRAN | /SCWM/RMDEFINERSRCTY | Define Resource Types | 104698 | SCM-EWM-AUT | SCM-EWM-CFG-2CL |
| SAP_CA_BC_IC_LND_SCM_EWM_PC | Warehouse Management - Configuration | /SCWM/22000305 | SCWM_22000305_TRAN | /SCWM/TONUM | Define Number Ranges for Warehouse Tasks/Warehouse Documents | 104418 | SCM-EWM-AUT | SCM-EWM-CFG-2CL |
| SAP_CA_BC_IC_LND_SCM_EWM_PC | Warehouse Management - Configuration | /SCWM/WAVENUM |  | /SCWM/WAVENUM | Define Number Range Intervals for Waves | 104736 | SCM-EWM-AUT | SCM-EWM-CFG-2CL |
| SAP_CA_BC_IC_LND_SCM_EWM_PC | Warehouse Management - Configuration | /SCWM/09000029 | SCWM_09000029_TRAN | /SCWM/V_TAAREASA | Define Sort Sequence for Cross-Line Stock Putaway | 104438 | SCM-EWM-AUT | SCM-EWM-CFG-2CL |
| SAP_CA_BC_IC_LND_SCM_EWM_PC | Warehouse Management - Configuration | /SCWM/VMAPITMTYP_CLD | SCWM_VMAPITMTYP_CLD_TRAN | /SCWM/TMAPITMTYP_SSC | Map Item Type from ERP System to WM | 106565 | SCM-EWM-AUT | SCM-EWM-CFG-2CL |
| SAP_CA_BC_IC_LND_SCM_EWM_PC | Warehouse Management - Configuration | PKGMATTYP | PKGMATTYP_TRAN | SIMG_PKGMATTYP | Maintain Packaging Material Types | 103665 | SCM-EWM-AUT | LO-HU-2CL |
| SAP_CA_BC_IC_LND_SCM_EWM_PC | Warehouse Management - Configuration | /SCWM/60000088 | SCWM_60000088_TRAN | /SCWM/TMAPDLVTYP | Map Document Types from ERP System to EWM | 106509 | SCM-EWM-AUT | SCM-EWM-CFG-2CL |
| SAP_CA_BC_IC_LND_SCM_EWM_PC | Warehouse Management - Configuration | /SCWM/22000187 | SCWM_22000187_TRAN | /SCWM/VTMAPPLANT | Assign Business Partners to Plant | 106508 | SCM-EWM-AUT | SCM-EWM-CFG-2CL |
| SAP_CA_BC_IC_LND_SCM_EWM_PC | Warehouse Management - Configuration | /SCWM/22000389 | SCWM_22000389_TRAN | /SCWM/TMAPITMTYP_SSC | Map Item Type from ERP System to WM | 106565 | SCM-EWM-AUT | SCM-EWM-CFG-2CL |
| SAP_CA_BC_IC_LND_SCM_EWM_PC | Warehouse Management - Configuration | /SCWM/60000123 | SCWM_60000123_TRAN | /SCWM/V_TAAREAS | Define Sort Sequence for Activity Areas | 104437 | SCM-EWM-AUT | SCM-EWM-CFG-2CL |
| SAP_CA_BC_IC_LND_SCM_EWM_PC | Warehouse Management - Configuration | /SCWM/60000122 | SCWM_60000122_TRAN | /SCWM/V_TAAREAD | Assign Storage Bins to Activity Areas | 104436 | SCM-EWM-AUT | SCM-EWM-CFG-2CL |
| SAP_CA_BC_IC_LND_SCM_EWM_PC | Warehouse Management - Configuration | /SCWM/60000133 | SCWM_60000133_TRAN | /SCWM/V_TWCRSSEQ | Define Search Sequence of Creation Rules for Activity Areas | 104759 | SCM-EWM-AUT | SCM-EWM-CFG-2CL |
| SAP_CA_BC_IC_LND_SCM_EWM_PC | Warehouse Management - Configuration | /SCWM/TONUM |  | /SCWM/TONUM | Define Number Ranges for Warehouse Tasks/Warehouse Documents | 104418 | SCM-EWM-AUT | SCM-EWM-CFG-2CL |
| SAP_CA_BC_IC_LND_SCM_EWM_PC | Warehouse Management - Configuration | /SCWM/60000069 | SCWM_60000069_TRAN | /SCWM/V_T333U | Default Values for Posting Changes | 104723 | SCM-EWM-AUT | SCM-EWM-CFG-2CL |
| SAP_CA_BC_IC_LND_SCM_EWM_PC | Warehouse Management - Configuration | /SCWM/60000054 | SCWM_60000054_TRAN | /SCWM/V_T334RR | Specify Stock Removal Rules | 104682 | SCM-EWM-AUT | SCM-EWM-CFG-2CL |
| SAP_CA_BC_IC_LND_SCM_EWM_PC | Warehouse Management - Configuration | S_ER9_52002185 | S_ER9_52002185_TRAN | SIMG_PKGMATTYP | Maintain Packaging Material Types | 103665 | SCM-EWM-AUT | LO-HU-2CL |
| SAP_CA_BC_IC_LND_SCM_EWM_PC | Warehouse Management - Configuration | /SCWM/60000121 | SCWM_60000121_TRAN | /SCWM/V_TAAREA | Define Activity Areas | 104435 | SCM-EWM-AUT | SCM-EWM-CFG-2CL |
| SAP_CA_BC_IC_LND_SCM_EWM_PC | Warehouse Management - Configuration | /SCWM/22000381 | SCWM_22000381_TRAN | /SCWM/VCTRLPR_DC | Set Control Parameters for ERP Version Control | 106376 | SCM-EWM-AUT | SCM-EWM-CFG-2CL |
| SAP_CA_BC_IC_LND_SCM_EWM_PC | Warehouse Management - Configuration | OMAD |  |  |  |  | SCM-EWM-AUT |  |
| SAP_CA_BC_IC_LND_SCM_EWM_PC | Warehouse Management - Configuration | /SCWM/70001422 | SCWM_70001422_TRAN | /SCWM/VHULBL_PRC | Control Automatic Printing of HU Labels for Processes | 106993 | SCM-EWM-AUT | SCM-EWM-CFG-2CL |
| SAP_CA_BC_IC_LND_SCM_EWM_PC | Warehouse Management - Configuration | /SCWM/22000308 | SCWM_22000308_TRAN | /SCWM/VC_QUEUES | Define Queues | 104699 | SCM-EWM-AUT | SCM-EWM-CFG-2CL |
| SAP_CA_BC_IC_LND_SCM_EWM_PC | Warehouse Management - Configuration | /SCWM/WHONUM |  | /SCWM/WHONUMSSC | Define Number Range Intervals for Warehouse Orders | 104708 | SCM-EWM-AUT | SCM-EWM-CFG-2CL |
| SAP_CA_BC_IC_LND_SCM_EWM_PC | Warehouse Management - Configuration | /SCWM/60000279 | SCWM_60000279_TRAN | /SCWM/TMATPP | Define Product Putaway Profile | 104721 | SCM-EWM-AUT | SCM-EWM-CFG-2CL |
| SAP_CA_BC_IC_LND_SCM_EWM_PC | Warehouse Management - Configuration | /SCWM/60000640 | SCWM_60000640_TRAN | /SCWM/T305R | Define Stock Removal Control Indicator | 104684 | SCM-EWM-AUT | SCM-EWM-CFG-2CL |
| SAP_CA_BC_IC_LND_SCM_EWM_PC | Warehouse Management - Configuration | /SCWM/60000411 | SCWM_60000411_TRAN | /SCWM/VC_VPRF | Define Warehouse-Specific Verification | 104450 | SCM-EWM-AUT | SCM-EWM-CFG-2CL |
| SAP_CA_BC_IC_LND_SCM_EWM_PC | Warehouse Management - Configuration | /SCWM/60000138 | SCWM_60000138_TRAN | /SCWM/VC_EXCODE | Define Exception Codes | 104743 | SCM-EWM-AUT | SCM-EWM-CFG-2CL |
| SAP_CA_BC_IC_LND_SCM_EWM_PC | Warehouse Management - Configuration | /SCWM/60000129 | SCWM_60000129_TRAN | /SCWM/TWCRLIMIT | Define Limit Values for the Size of a Warehouse Order | 104707 | SCM-EWM-AUT | SCM-EWM-CFG-2CL |
| SAP_CA_BC_IC_LND_SCM_EWM_PC | Warehouse Management - Configuration | /SCWM/60000050 | SCWM_60000050_TRAN | /SCWM/T302 | Define Storage Sections | 104453 | SCM-EWM-AUT | SCM-EWM-CFG-2CL |
| SAP_CA_BC_IC_LND_SCM_EWM_PC | Warehouse Management - Configuration | /SCWM/60000132 | SCWM_60000132_TRAN | /SCWM/TWCR | Define Creation Rules for Warehouse Orders | 104744 | SCM-EWM-AUT | SCM-EWM-CFG-2CL |
| SAP_CA_BC_IC_LND_SCM_EWM_PC | Warehouse Management - Configuration | /SCWM/22000311 | SCWM_22000311_TRAN | /SCWM/VC_MODES | Define Modes | 104694 | SCM-EWM-AUT | SCM-EWM-CFG-2CL |
| SAP_CA_BC_IC_LND_SCM_EWM_PC | Warehouse Management - Configuration | /SCWM/59000027 | SCWM_59000027_TRAN | /SCWM/VC_COMB_DET | Define Combined Picking Profile | 107102 | SCM-EWM-AUT | SCM-EWM-RF-2CL |
| SAP_CA_BC_IC_LND_SCM_EWM_PC | Warehouse Management - Configuration | /SCWM/60000412 | SCWM_60000412_TRAN | /SCWM/VC_VPRF_DET | Define Warehouse-Specific Verification Determination | 104451 | SCM-EWM-AUT | SCM-EWM-CFG-2CL |
| SAP_CA_BC_IC_LND_RFM_PURAL_PC | Allocation Table - Configuration | V_T621 |  | W_ZF_VK_0420 | Item Categories of Allocation Table | 105443 | LO-RFM | LO-RFM-PUR-AL-2CL |
| SAP_CA_BC_IC_LND_RFM_PURAL_PC | Allocation Table - Configuration | V_T628 |  | W_ZF_VK_0471 | Maintain Split Criteria for Allocation Table Follow-On Document Generation | 105442 | LO-RFM | LO-RFM-PUR-AL-2CL |
| SAP_CA_BC_IC_LND_RFM_PURAL_PC | Allocation Table - Configuration | S_ALR_87099969 | S_ALR_87099969_TRAN | W_ZF_VK_0471 | Maintain Split Criteria for Allocation Table Follow-On Document Generation | 105442 | LO-RFM | LO-RFM-PUR-AL-2CL |
| SAP_CA_BC_IC_LND_RFM_PURAL_PC | Allocation Table - Configuration | S_ALR_87008674 | S_ALR_87008674_TRAN | W_ZF_VK_0420 | Item Categories of Allocation Table | 105443 | LO-RFM | LO-RFM-PUR-AL-2CL |
| SAP_CA_BC_IC_LND_EIM_DX0_PC | Data Extraction - Configuration | S_SAL_71000066 | S_SAL_71000066_TRAN | DHCDC_CUST_ALIST | Define Allowlists for CDS View Extraction | 105575 | CA-DI-IS-ABA | CA-DI-IS-ABA |
| SAP_CA_BC_IC_LND_EIM_DX0_PC | Data Extraction - Configuration | DHCDC_IMG_AUTH_GROUP |  | DHCDC_CUST_ALIST | Define Allowlists for CDS View Extraction | 105575 | CA-DI-IS-ABA | CA-DI-IS-ABA |
| SAP_CA_BC_IC_LND_FIN_IM_RU_PC | International Trade Management for Russian Federation - Configuration | S_ER9_11001624 | S_ER9_11001624_TRAN | J_3RM_RN_MOVMTV | Define Material Movement Types for Traceability | 103743 | FI-LOC-FI-RU | FI-LOC-FI-RU |
| SAP_CA_BC_IC_LND_FIN_IM_RU_PC | International Trade Management for Russian Federation - Configuration | S_ER9_11001623 | S_ER9_11001623_TRAN | J_3RM_RN_BILV | Define Billing Types for Traceability | 103742 | FI-LOC-FI-RU | FI-LOC-FI-RU |
| SAP_CA_BC_IC_LND_FIN_IM_RU_PC | International Trade Management for Russian Federation - Configuration | S_EB5_05000326 | S_EB5_05000326_TRAN | J_3RFGTDINVT | Define Billing Types for Customs Declaration Tracking | 103493 | FI-LOC-FI-RU | FI-LOC-FI-RU |
| SAP_CA_BC_IC_LND_FIN_IM_RU_PC | International Trade Management for Russian Federation - Configuration | S_EB5_05000325 | S_EB5_05000325_TRAN | J_3RFGTDMATT | Define Material Movement Types for Customs Decl. Tracking | 103494 | FI-LOC-FI-RU | FI-LOC-FI-RU |
| SAP_CA_BC_IC_LND_FIN_IM_RU_PC | International Trade Management for Russian Federation - Configuration | S_ER9_11001533 | S_ER9_11001533_TRAN | J_3RFCUSTOMSV | Define Customs Offices | 103514 | FI-LOC-FI-RU | FI-LOC-FI-RU |
| SAP_CA_BC_IC_LND_FIN_IM_RU_PC | International Trade Management for Russian Federation - Configuration | S_EBJ_98001157 | S_EBJ_98001157_TRAN | J_3RM_RNOPERSETV | Maintain Assignments of Codes of Operations With Traceable Goods | 105668 | FI-LOC-FI-RU | FI-LOC-LO-RU |
| SAP_CA_BC_IC_LND_FIN_IM_RU_PC | International Trade Management for Russian Federation - Configuration | S_ER9_52003183 | S_ER9_52003183_TRAN | J_3RM_RN_OPERV | Maintain Codes of Operations With Traceable Goods | 105667 | FI-LOC-FI-RU | FI-LOC-LO-RU |
| SAP_CA_BC_GL_JE_CONFIG_PC | Journal Entry - Configuration | F4406 | F4406_TRAN |  |  |  | FI-GL |  |
| SAP_CA_BC_GL_JE_CONFIG_PC | Journal Entry - Configuration | F4945 | F4945_TRAN |  |  |  | FI-GL |  |
| SAP_CA_BC_GL_JE_CONFIG_PC | Journal Entry - Configuration | F4886 | F4886_TRAN |  |  |  | FI-GL |  |
| SAP_CA_BC_IC_LND_TMS_PC | Transportation Management - Configuration | S_EB5_05000460 | S_EB5_05000460_TRAN | SIMG_V_TMS_C_SLS | Define Transportation-Relevance of Sales Documents | 102646 | TM-BF-AUT | TM-INT-LI-2CL |
| SAP_CA_BC_IC_LND_TMS_PC | Transportation Management - Configuration | /SCMTMS/52001701 | SCMTMS_52001701_TRAN | /SCMTMS/V_CCPLNT | Assign Default Plant for Company Code | 103350 | TM-BF-AUT | TM-CF-2CL |
| SAP_CA_BC_IC_LND_TMS_PC | Transportation Management - Configuration | /SCMTMS/52001702 | SCMTMS_52001702_TRAN | /SCMTMS/V_CTPVCC | Assign MM Integration Settings to Charge Types | 103621 | TM-BF-AUT | TM-CF-2CL |
| SAP_CA_BC_IC_LND_TMS_PC | Transportation Management - Configuration | /SCMTMS/72000015 | SCMTMS_72000015_TRAN | /SCMTMS/V_TRQAT1 | Assign SD/MM Text Types to TM Text Types for SO/PO | 105510 | TM-BF-AUT | TM-CF-2CL |
| SAP_CA_BC_IC_LND_TMS_PC | Transportation Management - Configuration | /SCMTMS/52000635 | SCMTMS_52000635_TRAN | /SCMTMS/V_LOINT | Define Logistics Integration Profile | 105122 | TM-BF-AUT | TM-CF-2CL |
| SAP_CA_BC_IC_LND_TMS_PC | Transportation Management - Configuration | /SCMTMS/24000115 | SCMTMS_24000115_TRAN | /SCMTMS/V_TCET | Define Charge Types | 104376 | TM-BF-AUT | TM-CF-2CL |
| SAP_CA_BC_IC_LND_TMS_PC | Transportation Management - Configuration | /SCMTMS/TOR_NR | SCMTMS_TOR_NR_TRAN | /SCMTMS/TOR_NR | Define Number Range Intervals for Freight Order Management | 103506 | TM-BF-AUT | TM-CF-2CL |
| SAP_CA_BC_IC_LND_TMS_PC | Transportation Management - Configuration | /SCMTMS/50000090 | SCMTMS_50000090_TRAN | /SCMTMS/TOR_NR | Define Number Range Intervals for Freight Order Management | 103506 | TM-BF-AUT | TM-CF-2CL |
| SAP_CA_BC_IC_LND_TMS_PC | Transportation Management - Configuration | /SCMTMS/50000070 | SCMTMS_50000070_TRAN | /SCMTMS/V_DIMWP | Define Dimensional Weight Profiles | 104373 | TM-BF-AUT | TM-CF-2CL |
| SAP_CA_BC_IC_LND_TMS_PC | Transportation Management - Configuration | /SCMTMS/24000013 | SCMTMS_24000013_TRAN | /SCMTMS/V_BTDIT | Define Business Transaction Document Item Type Codes | 106045 | TM-BF-AUT | TM-CF-2CL |
| SAP_CA_BC_IC_LND_TMS_PC | Transportation Management - Configuration | /SCMTMS/52001538 | SCMTMS_52001538_TRAN | /SCMTMS/V_LCUOMC | Define Conversion Between NLQ and ALQ UoM | 106465 | TM-BF-AUT | TM-CF-2CL |
| SAP_CA_BC_IC_LND_TMS_PC | Transportation Management - Configuration | /SCMTMS/52004158 | SCMTMS_52004158_TRAN | /SCMTMS/V_NSCA | Activate Numbering Scheme Content for Commodity Codes | 106328 | TM-BF-AUT | TM-CF-2CL |
| SAP_CA_BC_IC_LND_TMS_PC | Transportation Management - Configuration | S_EB5_05000461 | S_EB5_05000461_TRAN | SIMG_V_TMS_C_SHP | Define Transportation-Relevance of Delivery Documents | 105126 | TM-BF-AUT | TM-INT-LI-2CL |
| SAP_CA_BC_IC_LND_TMS_PC | Transportation Management - Configuration | /SCMTMS/20000039 | SCMTMS_20000039_TRAN | /SCMTMS/V_FASETP | Define Charges Profiles | 104374 | TM-BF-AUT | TM-CF-2CL |
| SAP_CA_BC_IC_LND_TMS_PC | Transportation Management - Configuration | /SCMTMS/76000023 | SCMTMS_76000023_TRAN | /SCMTMS/VC_EQU | Define Equipment Groups and Equipment Types | 105134 | TM-BF-AUT | TM-CF-2CL |
| SAP_CA_BC_IC_LND_TMS_PC | Transportation Management - Configuration | /SCMTMS/24000023 | SCMTMS_24000023_TRAN | /SCMTMS/V_BTDTY | Define Business Transaction Document Type Codes | 106042 | TM-BF-AUT | TM-CF-2CL |
| SAP_CA_BC_IC_LND_TMS_PC | Transportation Management - Configuration | /SCMTMS/52004156 | SCMTMS_52004156_TRAN | /SCMTMS/V_NSC | Define Numbering Scheme Content for Commodity Codes | 106327 | TM-BF-AUT | TM-CF-2CL |
| SAP_CA_BC_IC_LND_TMS_PC | Transportation Management - Configuration | /SCMTMS/07000039 | SCMTMS_07000039_TRAN | /SCMTMS/V_CAPR | Define Calculation Profiles | 104410 | TM-BF-AUT | TM-CF-2CL |
| SAP_CA_BC_IC_LND_TMS_PC | Transportation Management - Configuration | /SCMTMS/50000188 | SCMTMS_50000188_TRAN | /SCMTMS/V_IATAC | Define Airport Codes | 105746 | TM-BF-AUT | TM-CF-2CL |
| SAP_CA_BC_IC_LND_TMS_PC | Transportation Management - Configuration | /SCMTMS/52004159 | SCMTMS_52004159_TRAN | /SCMTMS/V_TUNS | Assign Numbering Scheme for Commodity Codes to Country/Region | 106329 | TM-BF-AUT | TM-CF-2CL |
| SAP_CA_BC_IC_LND_TMS_PC | Transportation Management - Configuration | /SCMB/05000034 | SCMB_05000034_TRAN | /SCMB/V_FTPT_UOM | Define UoM Relevance for NLQ and ALQ | 106442 | TM-BF-AUT | SCM-BAS-IMG |
| SAP_CA_BC_IC_LND_TMS_PC | Transportation Management - Configuration | /SCMTMS/20000021 | SCMTMS_20000021_TRAN | /SCMTMS/V_DLVCPE | Define Blocks Based on Delivery Block | 106189 | TM-BF-AUT | TM-CF-2CL |
| SAP_CA_BC_IC_LND_TMS_PC | Transportation Management - Configuration | /SCMTMS/52004155 | SCMTMS_52004155_TRAN | /SCMTMS/V_NOS | Define Numbering Scheme for Commodity Codes | 106326 | TM-BF-AUT | TM-CF-2CL |
| SAP_CA_BC_IC_LND_TMS_PC | Transportation Management - Configuration | /SCMTMS/72000016 | SCMTMS_72000016_TRAN | /SCMTMS/V_TRQAT2 | Assign Logistics Execution Text Types to TM Text Types for Deliveries | 105964 | TM-BF-AUT | TM-CF-2CL |
| SAP_CA_BC_IC_LND_TMS_PC | Transportation Management - Configuration | S_EB5_05000462 | S_EB5_05000462_TRAN | SIMG_V_TMS_C_PUR | Define Transportation-Relevance of Purchasing Documents | 105125 | TM-BF-AUT | TM-INT-LI-2CL |
| SAP_CA_BC_IC_LND_TMS_PC | Transportation Management - Configuration | /SCMTMS/52001982 | SCMTMS_52001982_TRAN | /SCMTMS/V_LOC_CA | Define Location Calendar | 103639 | TM-BF-AUT | TM-CF-2CL |
| SAP_CA_BC_IC_LND_TMS_PC | Transportation Management - Configuration | S_ER9_52003264 | S_ER9_52003264_TRAN | V_TMFG | Define Material Freight Groups | 105681 | TM-BF-AUT | TM-MD-PR-2CL |
| SAP_CA_BC_IC_LND_TMS_PC | Transportation Management - Configuration | /SCMTMS/20000041 | SCMTMS_20000041_TRAN | /SCMTMS/V_UNLOC | Define UN/LOCODE | 105747 | TM-BF-AUT | TM-CF-2CL |
| SAP_CA_BC_IC_LND_TMS_PC | Transportation Management - Configuration | S_BTD_53000090 | S_BTD_53000090_TRAN | BS_FND_BO_TXC | Maintain Text Schema | 105509 | TM-BF-AUT | CA-EPT-BRC |
| SAP_CA_BC_IC_LND_TMS_PC | Transportation Management - Configuration | /SCMTMS/50000137 | SCMTMS_50000137_TRAN | /SCMTMS/C_SCAC | Define Standard Carrier Alpha Codes | 105745 | TM-BF-AUT | TM-CF-2CL |
| SAP_CA_BC_IC_LND_FIN_TA0_PC | Financials - Jurisdiction Code and Taxes - Configuration | V_TTXJ_ABA |  | V_TTXJ_ABA | Define Tax Jurisdictions |  | CA-GTF-TS-TAX | CA-GTF-TS-TAX-2CL |
| SAP_CA_BC_IC_LND_FIN_TA0_PC | Financials - Jurisdiction Code and Taxes - Configuration | S_SAL_71000096 | S_SAL_71000096_TRAN | V_TTXJ_ABA | Define Tax Jurisdictions |  | CA-GTF-TS-TAX | CA-GTF-TS-TAX-2CL |
| SAP_CA_BC_IC_LND_FIN_TA0_PC | Financials - Jurisdiction Code and Taxes - Configuration | V_TTXC_ABA |  |  |  |  | CA-GTF-TS-TAX |  |
| SAP_CA_BC_IC_LND_FIN_TA0_PC | Financials - Jurisdiction Code and Taxes - Configuration | S_PAB_37000005 | S_PAB_37000005_TRAN | TJC_005 | Assign Function Module to Indicator |  | CA-GTF-TS-TAX | CA-GTF-CSC |
| SAP_CA_BC_IC_LND_FIN_ICA_PC | Intercompany - Configuration | S_ER9_11001331 | S_ER9_11001331_TRAN | ICAADT | Assign Document Templates to Companies | 103242 | FI-GL | FIN-CS-ICR-2CL |
| SAP_CA_BC_IC_LND_FIN_ICA_PC | Intercompany - Configuration | S_ER9_11001610 | S_ER9_11001610_TRAN | ICAAPT | Assign Posting Rules | 103658 | FI-GL | FIN-CS-ICR-2CL |
| SAP_CA_BC_IC_LND_FIN_ICA_PC | Intercompany - Configuration | S_ER9_11001594 | S_ER9_11001594_TRAN | ICAEM | Define Elimination Methods | 103559 | FI-GL | FIN-CS-ICR-2CL |
| SAP_CA_BC_IC_LND_FIN_ICA_PC | Intercompany - Configuration | S_ER9_11001593 | S_ER9_11001593_TRAN | ICAARC | Activate Reconciliation Close Process | 103560 | FI-GL | FIN-CS-ICR-2CL |
| SAP_CA_BC_IC_LND_FIN_ICA_PC | Intercompany - Configuration | S_ER9_11001332 | S_ER9_11001332_TRAN | ICAFC | Define Filters for Assignment List | 103240 | FI-GL | FIN-CS-ICR-2CL |
| SAP_CA_BC_IC_LND_FIN_ICA_PC | Intercompany - Configuration | S_ER9_11001330 | S_ER9_11001330_TRAN | ICADT | Define G/L Posting Document Templates | 103241 | FI-GL | FIN-CS-ICR-2CL |
| SAP_CA_BC_IC_LND_FIN_ICA_PC | Intercompany - Configuration | S_ER9_11001445 | S_ER9_11001445_TRAN | ICA_AS | Define Additional Settings for Matching Methods | 103381 | FI-GL | FIN-CS-ICR-2CL |
| SAP_CA_BC_IC_LND_FIN_ICA_PC | Intercompany - Configuration | S_ER9_11001444 | S_ER9_11001444_TRAN | ICA_EA | Assign Email Templates to Matching Methods | 103380 | FI-GL | FIN-CS-ICR-2CL |
| SAP_CA_BC_IC_LND_FIN_ICA_PC | Intercompany - Configuration | S_ER9_11001180 | S_ER9_11001180_TRAN | ICA_DS | Maintain Data Sources | 103244 | FI-GL | FIN-CS-ICR-2CL |
| SAP_CA_BC_IC_LND_FIN_ICA_PC | Intercompany - Configuration | S_ER9_11001181 | S_ER9_11001181_TRAN | ICA_RC | Maintain Reason Codes | 103243 | FI-GL | FIN-CS-ICR-2CL |
| SAP_CA_BC_IC_LND_FIN_ICA_PC | Intercompany - Configuration | ICAADT |  | ICAADT | Assign Document Templates to Companies | 103242 | FI-GL | FIN-CS-ICR-2CL |
| SAP_CA_BC_IC_LND_FIN_ICA_PC | Intercompany - Configuration | ICARC |  | ICA_RC | Maintain Reason Codes | 103243 | FI-GL | FIN-CS-ICR-2CL |
| SAP_CA_BC_IC_LND_FIN_ICA_PC | Intercompany - Configuration | ICAFC |  | ICAFC | Define Filters for Assignment List | 103240 | FI-GL | FIN-CS-ICR-2CL |
| SAP_CA_BC_IC_LND_FIN_ICA_PC | Intercompany - Configuration | ICAEM |  | ICAEM | Define Elimination Methods | 103559 | FI-GL | FIN-CS-ICR-2CL |
| SAP_CA_BC_IC_LND_FIN_ICA_PC | Intercompany - Configuration | ICAEA |  | ICA_EA | Assign Email Templates to Matching Methods | 103380 | FI-GL | FIN-CS-ICR-2CL |
| SAP_CA_BC_IC_LND_FIN_ICA_PC | Intercompany - Configuration | ICAAS |  | ICA_AS | Define Additional Settings for Matching Methods | 103381 | FI-GL | FIN-CS-ICR-2CL |
| SAP_CA_BC_IC_LND_FIN_ICA_PC | Intercompany - Configuration | ICADS |  | ICA_DS | Maintain Data Sources | 103244 | FI-GL | FIN-CS-ICR-2CL |
| SAP_CA_BC_IC_LND_FIN_ICA_PC | Intercompany - Configuration | ICADT |  | ICADT | Define G/L Posting Document Templates | 103241 | FI-GL | FIN-CS-ICR-2CL |
| SAP_CA_BC_IC_LND_FIN_ICA_PC | Intercompany - Configuration | ICAARC |  | ICAARC | Activate Reconciliation Close Process | 103560 | FI-GL | FIN-CS-ICR-2CL |
| SAP_CA_BC_IC_LND_FIN_ICA_PC | Intercompany - Configuration | ICAN1 |  | ICAN1 | Define Number Range for Matching Documents |  | FI-GL | FIN-CS-ICR-2CL |
| SAP_CA_BC_IC_LND_FIN_ICA_PC | Intercompany - Configuration | ICAAPT |  | ICAAPT | Assign Posting Rules | 103658 | FI-GL | FIN-CS-ICR-2CL |
| SAP_CA_BC_IC_LND_FIN_ICA_PC | Intercompany - Configuration | S_ER9_11001335 | S_ER9_11001335_TRAN | ICAN1 | Define Number Range for Matching Documents |  | FI-GL | FIN-CS-ICR-2CL |
| SAP_CA_BC_IC_LND_FIN_ICA_PC | Intercompany - Configuration | S_ER9_11001336 | S_ER9_11001336_TRAN | ICAN2 | Define Number Range for Matching Assignments |  | FI-GL | FIN-CS-ICR-2CL |
| SAP_CA_BC_IC_LND_FIN_ICA_PC | Intercompany - Configuration | ICAN2 |  | ICAN2 | Define Number Range for Matching Assignments |  | FI-GL | FIN-CS-ICR-2CL |
| SAP_FIN_BC_AR_DP_SETTINGS_PC | Accounts Receivable - Digital Payments Settings | FDP3 | FDP3_TRAN | FINS_AR_DP_TAXCODE | Maintain Tax Codes for Posting Charges | 102593 | FI-AR-AR | FIN-FSCM-DP-DP-2CL |
| SAP_FIN_BC_AR_DP_SETTINGS_PC | Accounts Receivable - Digital Payments Settings | S_ER9_11000661 | S_ER9_11000661_TRAN | FINS_AR_DP_TAXCODE | Maintain Tax Codes for Posting Charges | 102593 | FI-AR-AR | FIN-FSCM-DP-DP-2CL |
| SAP_FIN_BC_AR_DP_SETTINGS_PC | Accounts Receivable - Digital Payments Settings | S_ER9_11000406 | S_ER9_11000406_TRAN | FINS_AR_DP_ACT | Activate SAP Digital Payments Add-On | 102562 | FI-AR-AR | FIN-FSCM-DP-DP-2CL |
| SAP_FIN_BC_AR_DP_SETTINGS_PC | Accounts Receivable - Digital Payments Settings | FDP1 | FDP1_TRAN | FINS_AR_DP_ACT | Activate SAP Digital Payments Add-On | 102562 | FI-AR-AR | FIN-FSCM-DP-DP-2CL |
| SAP_FIN_BC_AR_DP_SETTINGS_PC | Accounts Receivable - Digital Payments Settings | S_ER9_11000661 | S_ER9_11000661_TRAN | FINS_AR_DP_TAXCODE | Maintain Tax Codes for Posting Charges | 102593 | FI-AR-AR | FIN-FSCM-DP-DP-2CL |
| SAP_FIN_BC_AR_DP_SETTINGS_PC | Accounts Receivable - Digital Payments Settings | S_ER9_11000406 | S_ER9_11000406_TRAN | FINS_AR_DP_ACT | Activate SAP Digital Payments Add-On | 102562 | FI-AR-AR | FIN-FSCM-DP-DP-2CL |
| SAP_CA_BC_IC_LND_FIN_LC_CN_PC | Legal Compliance for China - Configuration | S_EBS_44000099 | S_EBS_44000099_TRAN | IDCN_VODN_CLEAR | Maintain Settings for Clearing Documents Without Line Items | 101074 | FI-LOC-IAM | FI-LOC-FI-CN |
| SAP_CA_BC_IC_LND_FIN_LC_CN_PC | Legal Compliance for China - Configuration | S_EB5_05000496 | S_EB5_05000496_TRAN | V_OFFNUM_CN | Assign Number Group to Company Code | 101078 | FI-LOC-IAM | FI-LOC-FI-CN |
| SAP_CA_BC_IC_LND_FIN_LC_CN_PC | Legal Compliance for China - Configuration | S_EB5_05000492 | S_EB5_05000492_TRAN | V_DOCCLS_CN | Maintain Document Classes for China | 101077 | FI-LOC-IAM | FI-LOC-FI-CN |
| SAP_CA_BC_IC_LND_FIN_LC_CN_PC | Legal Compliance for China - Configuration | S_EB5_05000494 | S_EB5_05000494_TRAN | V_1ANUMGR1_CN | Maintain Number Groups for China | 101076 | FI-LOC-IAM | FI-LOC-FI-CN |
| SAP_CA_BC_IC_LND_FIN_LC_CN_PC | Legal Compliance for China - Configuration | S_EB5_05000493 | S_EB5_05000493_TRAN | V_T003_B_I_CN | Assign Document Classes to Document Types for China | 101079 | FI-LOC-IAM | FI-LOC-FI-CN |
| SAP_CA_BC_IC_LND_FIN_LC_CN_PC | Legal Compliance for China - Configuration | S_EB5_05000495 | S_EB5_05000495_TRAN | J_1ATJ1AB_CN | Maintain Number Ranges for China | 103406 | FI-LOC-IAM | FI-LOC-FI-CN |
| SAP_CA_BC_IC_LND_FIN_LC_CN_PC | Legal Compliance for China - Configuration | S_EBJ_98000235 | S_EBJ_98000235_TRAN | ADJNR | Define Number Ranges for Adjustment Documents | 103720 | FI-LOC-IAM | FI-LOC-FI-CN |
| SAP_CA_BC_IC_LND_FIN_LC_CN_PC | Legal Compliance for China - Configuration | ADJNR |  | ADJNR | Define Number Ranges for Adjustment Documents | 103720 | FI-LOC-IAM | FI-LOC-FI-CN |
| SAP_CA_BC_IC_LND_FIN_LC_CN_PC | Legal Compliance for China - Configuration | OFN_YR |  | J_1ATJ1AB_CN | Maintain Number Ranges for China | 103406 | FI-LOC-IAM | FI-LOC-FI-CN |
| SAP_CA_BC_IC_LND_FIN_LC_CN_PC | Legal Compliance for China - Configuration | S_ER1_70001519 | S_ER1_70001519_TRAN | J_3RF_XNEGP_ACT_CN | Activate Negative Posting for Country/Region | 107034 | FI-LOC-IAM | FI-LOC-FI-CN |
| SAP_CA_BC_IC_LND_FIN_LC_CN_PC | Legal Compliance for China - Configuration | S_EBS_44000467 | S_EBS_44000467_TRAN | IDCN_VODN_ACTIVE | Activate Document Numbering for Company Code | 101073 | FI-LOC-IAM | FI-LOC-FI-CN |
| SAP_CA_BC_IC_LND_FIN_FSV_PC | Financial Statement Version - Configuration | S_ALR_87003215 | S_ALR_87003215_TRAN | SIMG_CFMENUORFBOB58 | Define Financial Statement Versions | 102669 | FI-GL | FI-GL-GL-N-2CL |
| SAP_CA_BC_IC_LND_FIN_FSV_PC | Financial Statement Version - Configuration | S_ER9_11000216 | S_ER9_11000216_TRAN | FINSC_FAGL2SEMTA | Assign Semantic Tags to Financial Statement Versions | 102659 | FI-GL | FI-FIO-GL-HIE-2CL |
| SAP_CA_BC_IC_LND_FIN_FSV_PC | Financial Statement Version - Configuration | S_ER9_11001952 | S_ER9_11001952_TRAN | FINS_UH_FSV_SSCUI | Define Financial Statement Versions in Global Hierarchies | 150003 | FI-GL | FI-FIO-GL-HIE-2CL |
| SAP_CA_BC_IC_LND_FIN_FSV_PC | Financial Statement Version - Configuration | FINS_UH_FSV_SSCUI |  | FINS_UH_FSV_SSCUI | Define Financial Statement Versions in Global Hierarchies | 150003 | FI-GL | FI-FIO-GL-HIE-2CL |
| SAP_CA_BC_IC_LND_FIN_FSV_PC | Financial Statement Version - Configuration | S_ER9_11001951 | S_ER9_11001951_TRAN | FINS_UH_FSVMIG_SSCUI | Migrate Financial Statement Versions to Global Hierarchies | 170006 | FI-GL | FI-FIO-GL-HIE-2CL |
| SAP_CA_BC_IC_LND_FIN_FSV_PC | Financial Statement Version - Configuration | FINS_UH_FSVMIG_SSCUI |  | FINS_UH_FSVMIG_SSCUI | Migrate Financial Statement Versions to Global Hierarchies | 170006 | FI-GL | FI-FIO-GL-HIE-2CL |
| SAP_CA_BC_IC_LND_FIN_FSV_PC | Financial Statement Version - Configuration | F4965 |  |  |  |  | FI-GL |  |
| SAP_CA_BC_IC_LND_FIN_FSV_PC | Financial Statement Version - Configuration | F5002 | F5002_GL_TRAN |  |  |  | FI-GL |  |
| SAP_CA_BC_IC_LND_FIN_FSV_PC | Financial Statement Version - Configuration | F6748 |  |  |  |  | FI-GL |  |
| SAP_CA_BC_IC_LND_FIN_FSV_PC | Financial Statement Version - Configuration | F5097 | F5097_TRAN |  |  |  | FI-GL |  |
| SAP_CA_BC_IC_LND_FIN_FSV_PC | Financial Statement Version - Configuration | F7019 | F7019_TRAN |  |  |  | FI-GL |  |
| SAP_CA_BC_IC_LND_FIN_FSV_PC | Financial Statement Version - Configuration | F6259 | F6259_TRAN |  |  |  | FI-GL |  |
| SAP_CA_BC_IC_LND_FIN_FSV_PC | Financial Statement Version - Configuration | FINSC_FAGL2SEMTA | FINSC_FAGL2SEMTA_TRAN | FINSC_FAGL2SEMTA | Assign Semantic Tags to Financial Statement Versions | 102659 | FI-GL | FI-FIO-GL-HIE-2CL |
| SAP_CA_BC_IC_LND_FIN_FSV_PC | Financial Statement Version - Configuration | FSE2 | FSE2_TRAN |  |  |  | FI-GL |  |
| SAP_CA_BC_IC_LND_FIN_FSV_PC | Financial Statement Version - Configuration | FSE3 | FSE3_TRAN |  |  |  | FI-GL |  |
| SAP_CA_BC_IC_LND_FIN_FSV_PC | Financial Statement Version - Configuration | OB58 | OB58_03_TRAN | SIMG_CFMENUORFBOB58 | Define Financial Statement Versions | 102669 | FI-GL | FI-GL-GL-N-2CL |
| SAP_CA_BC_IC_LND_LE_DWM0_PC | Logistics Execution Decentralized WM System Integration - Configuration | S_ALR_87007555 | S_ALR_87007555_TRAN | SAPC_LGNUM | Define Warehouse Number | 101105 | SCM-EWM-AUT | SCM-EWM-IF-ERP-2CL |
| SAP_CA_BC_IC_LND_LE_DWM0_PC | Logistics Execution Decentralized WM System Integration - Configuration | S_ALR_87007419 | S_ALR_87007419_TRAN | SIMG_SAPCOML2 | Assign Warehouse Number to Plant and Storage Location | 101109 | SCM-EWM-AUT | SCM-EWM-IF-ERP-2CL |
| SAP_CA_BC_IC_LND_LE_DWM0_PC | Logistics Execution Decentralized WM System Integration - Configuration | /SPE/52004316 | SPE_52004316_TRAN | /SPE/V_T340_3PL_SSC | Configure SAP 3PL-Specific Parameters | 106429 | SCM-EWM-AUT | LE-IEW-X-2CL |
| SAP_CA_BC_IC_LND_LE_DWM0_PC | Logistics Execution Decentralized WM System Integration - Configuration | OL20 | OL20_TRAN | SIMG_XXLEIDW2008 | Consistency Check | 101110 | SCM-EWM-AUT | SCM-EWM-IF-ERP-2CL |
| SAP_CA_BC_IC_LND_LE_DWM0_PC | Logistics Execution Decentralized WM System Integration - Configuration | EC18 |  | SAPC_LGNUM | Define Warehouse Number | 101105 | SCM-EWM-AUT | SCM-EWM-IF-ERP-2CL |
| SAP_CA_BC_IC_LND_LE_DWM0_PC | Logistics Execution Decentralized WM System Integration - Configuration | S_ALR_87003590 | S_ALR_87003590_TRAN | SIMG_XXLEIDW2008 | Consistency Check | 101110 | SCM-EWM-AUT | SCM-EWM-IF-ERP-2CL |
| SAP_CA_BC_IC_LND_LE_DWM0_PC | Logistics Execution Decentralized WM System Integration - Configuration | /SPE/V_T340_3PL |  | /SPE/V_T340_3PL_SSC | Configure SAP 3PL-Specific Parameters | 106429 | SCM-EWM-AUT | LE-IEW-X-2CL |
| SAP_CA_BC_IC_LND_LE_DWM0_PC | Logistics Execution Decentralized WM System Integration - Configuration | S_ER9_52000775 | S_ER9_52000775_TRAN | V_T340DL | Define Default Values for Deliveries | 101303 | SCM-EWM-AUT | SCM-EWM-IF-ERP-2CL |
| SAP_CA_BC_IC_LND_RFM_MDPRC_PC | Retail Pricing - Configuration | S_ALR_87007789 | S_ALR_87007789_TRAN | W_ZF_VK_0320 | Assign Pricing Type/Reference Plant to Organizational Level | 105306 | LO-RFM | LO-RFM-MD-RPC-2CL |
| SAP_CA_BC_IC_LND_RFM_MDPRC_PC | Retail Pricing - Configuration | V_TWLFE |  | W_ZF_VK_0380 | Control Pricing Per List Field | 105307 | LO-RFM | LO-RFM-MD-RPC-2CL |
| SAP_CA_BC_IC_LND_RFM_MDPRC_PC | Retail Pricing - Configuration | S_ALR_87007784 | S_ALR_87007784_TRAN | W_ZF_VK_0380 | Control Pricing Per List Field | 105307 | LO-RFM | LO-RFM-MD-RPC-2CL |
| SAP_CA_BC_IC_LND_RFM_MDPRC_PC | Retail Pricing - Configuration | S_ER9_52002635 | S_ER9_52002635_TRAN | W_ZF_VK_0350 | Maintain Pricing Type | 105310 | LO-RFM | LO-RFM-MD-RPC-2CL |
| SAP_CA_BC_IC_LND_RFM_MDPRC_PC | Retail Pricing - Configuration | S_ER9_52002853 | S_ER9_52002853_TRAN | RFM_PP_TWEGO_ORMC | Assign Price Point Group to Organization Level/Merchandise Category | 105308 | LO-RFM | LO-RFM-MD-RPC-2CL |
| SAP_CA_BC_IC_LND_RFM_MDPRC_PC | Retail Pricing - Configuration | S_ER9_52002852 | S_ER9_52002852_TRAN | RFM_PP_TWEGO_ORG | Assign Price Point Group to Organization Level | 105309 | LO-RFM | LO-RFM-MD-RPC-2CL |
| SAP_CA_BC_IC_LND_RFM_MDPRC_PC | Retail Pricing - Configuration | V_RFM_TWEGO_ORMC |  | RFM_PP_TWEGO_ORMC | Assign Price Point Group to Organization Level/Merchandise Category | 105308 | LO-RFM | LO-RFM-MD-RPC-2CL |
| SAP_CA_BC_IC_LND_RFM_MDPRC_PC | Retail Pricing - Configuration | V_RFM_TWEGO_ORG |  | RFM_PP_TWEGO_ORG | Assign Price Point Group to Organization Level | 105309 | LO-RFM | LO-RFM-MD-RPC-2CL |
| SAP_CA_BC_IC_LND_RFM_MDPRC_PC | Retail Pricing - Configuration | V_TWVK |  | V_TWVK | Assign Allowed Pricing Levels | 105305 | LO-RFM | LO-RFM-MD-RPC-2CL |
| SAP_CA_BC_IC_LND_RFM_MDPRC_PC | Retail Pricing - Configuration | S_ER9_52003517 | S_ER9_52003517_TRAN | V_TWVK | Assign Allowed Pricing Levels | 105305 | LO-RFM | LO-RFM-MD-RPC-2CL |
| SAP_CA_BC_IC_LND_RFM_MDPRC_PC | Retail Pricing - Configuration | S_ER9_52001365 | S_ER9_52001365_TRAN | W_ZF_VK_0314 | Define Price Point Group and Assign Price Point Ranges | 104667 | LO-RFM | LO-RFM-MD-RPC-2CL |
| SAP_CA_BC_IC_LND_RFM_MDPRC_PC | Retail Pricing - Configuration | S_ALR_87100602 | S_ALR_87100602_TRAN | W_ZF_VK_0324 | Subsequent Index Compilation for Sales Prices | 106075 | LO-RFM | LO-RFM-MD-RPC-2CL |
| SAP_CA_BC_IC_LND_RFM_MDPRC_PC | Retail Pricing - Configuration | S_ALR_87007787 | S_ALR_87007787_TRAN | W_ZF_VK_0323 | Control Pricing Document Adjustment for Internal Procurement | 106076 | LO-RFM | LO-RFM-MD-RPC-2CL |
| SAP_CA_BC_IC_LND_RFM_MDPRC_PC | Retail Pricing - Configuration | S_ALR_87007786 | S_ALR_87007786_TRAN | W_ZF_VK_0322 | Control Pricing Document Adjustment for External Procurement | 106074 | LO-RFM | LO-RFM-MD-RPC-2CL |
| SAP_CA_BC_IC_LND_RFM_MDPRC_PC | Retail Pricing - Configuration | VV_T6I1_VA |  | W_ZF_VK_0323 | Control Pricing Document Adjustment for Internal Procurement | 106076 | LO-RFM | LO-RFM-MD-RPC-2CL |
| SAP_CA_BC_IC_LND_RFM_MDPRC_PC | Retail Pricing - Configuration | VV_T6I1_P_VA11 |  | W_ZF_VK_0324 | Subsequent Index Compilation for Sales Prices | 106075 | LO-RFM | LO-RFM-MD-RPC-2CL |
| SAP_CA_BC_IC_LND_RFM_MDPRC_PC | Retail Pricing - Configuration | VV_T6I1_MA |  | W_ZF_VK_0322 | Control Pricing Document Adjustment for External Procurement | 106074 | LO-RFM | LO-RFM-MD-RPC-2CL |
| SAP_CA_BC_IC_LND_RFM_MDPRC_PC | Retail Pricing - Configuration | VC_TWST |  | W_ZF_VK_0330 | Define List Variant and Assign Items | 107021 | LO-RFM | LO-RFM-MD-RPC-2CL |
| SAP_CA_BC_IC_LND_RFM_MDPRC_PC | Retail Pricing - Configuration | S_ALR_87007782 | S_ALR_87007782_TRAN | W_ZF_VK_0330 | Define List Variant and Assign Items | 107021 | LO-RFM | LO-RFM-MD-RPC-2CL |
| SAP_CA_BC_IC_LND_FIN_MAP_PC | Margin Analysis Processes - Configuration | S_ER9_11001354 | S_ER9_11001354_TRAN | FINS_ALLOC_TMPL | Define Template for Top-Down Distribution | 150005 | CO-PA | FI-GL-GL-AL-2CL |
| SAP_CA_BC_IC_LND_FIN_MAP_PC | Margin Analysis Processes - Configuration | S_E91_86000122 | S_E91_86000122_TRAN | SIMG_FCOC_FDIM_1 | Define Additional Quantity Fields | 102406 | CO-PA | CO-PA-2CL |
| SAP_CA_BC_IC_LND_FIN_MAP_PC | Margin Analysis Processes - Configuration | S_ER9_11000517 | S_ER9_11000517_TRAN | FCO_COPA_EX_N | Exceptions for Postings to Profitability Segment | 105626 | CO-PA | CO-PA-2CL |
| SAP_CA_BC_IC_LND_FIN_MAP_PC | Margin Analysis Processes - Configuration | FCO_COPA_EX_N |  | FCO_COPA_EX_N | Exceptions for Postings to Profitability Segment | 105626 | CO-PA | CO-PA-2CL |
| SAP_CA_BC_IC_LND_FIN_MAP_PC | Margin Analysis Processes - Configuration | S_E91_86000124 | S_E91_86000124_TRAN | SIMG_FCOC_COGS_SCHEM | Define Accounts for Splitting the Cost of Goods Sold | 102617 | CO-PA | CO-PA-2CL |
| SAP_CA_BC_IC_LND_FIN_MAP_PC | Margin Analysis Processes - Configuration | S_ER1_70001432 | S_ER1_70001432_TRAN | FCOPA_PROFSEG_SUMM | Summarization of Profitabiility Segments | 107006 | CO-PA | CO-PA-2CL |
| SAP_CA_BC_IC_LND_FIN_LC_TW_PC | Legal Compliance for Taiwan - Configuration | S_P9C_18000047 | S_P9C_18000047_TRAN | TAIWAN_009 | Maintain Number Ranges for Taiwan | 102328 | FI-LOC-FI-TW | FI-LOC-FI-TW |
| SAP_CA_BC_IC_LND_FIN_LC_TW_PC | Legal Compliance for Taiwan - Configuration | S_P9C_18000046 | S_P9C_18000046_TRAN | TAIWAN_008 | Maintain Number Groups for Taiwan | 102325 | FI-LOC-FI-TW | FI-LOC-FI-TW |
| SAP_CA_BC_IC_LND_FIN_LC_TW_PC | Legal Compliance for Taiwan - Configuration | J1AB | J1AB_TRAN |  |  |  | FI-LOC-FI-TW |  |
| SAP_CA_BC_IC_LND_FIN_LC_TW_PC | Legal Compliance for Taiwan - Configuration | S_ER9_11000380 | S_ER9_11000380_TRAN | IDTW_GUI_DET_FI | Assign Document Class to Accounting Document Type and Tax Code | 101929 | FI-LOC-FI-TW | FI-LOC-FI-CN |
| SAP_CA_BC_IC_LND_FIN_LC_TW_PC | Legal Compliance for Taiwan - Configuration | S_ER9_11000382 | S_ER9_11000382_TRAN | IDTW_GUI_DET_SD | Assign Document Class to Billing Type and Tax Code | 101936 | FI-LOC-FI-TW | FI-LOC-FI-CN |
| SAP_CA_BC_IC_LND_FIN_LC_TW_PC | Legal Compliance for Taiwan - Configuration | J_1BBRANCV_TW |  | J_1BBRANCV_TW | Define Business Places for Taiwan | 106596 | FI-LOC-FI-TW | FI-LOC-FI-TW |
| SAP_CA_BC_IC_LND_FIN_LC_TW_PC | Legal Compliance for Taiwan - Configuration | S_PL0_86000001 | S_PL0_86000001_TRAN | J_1BBRANCV_TW | Define Business Places for Taiwan | 106596 | FI-LOC-FI-TW | FI-LOC-FI-TW |
| SAP_CA_BC_IC_LND_FIN_LC_TW_PC | Legal Compliance for Taiwan - Configuration | S_P9C_18000052 | S_P9C_18000052_TRAN | TAIWAN_007 | Assign Number Ranges to Business Places | 102326 | FI-LOC-FI-TW | FI-LOC-FI-TW |
| SAP_CMD_BC_CUSTOMER_DSP_PC | Master Data - Customer Display | F0046A | F0046A_03_TRAN |  |  |  | LO-MD-BP |  |
| SAP_CMD_BC_CUSTOMER_DSP_PC | Master Data - Customer Display | F5794 | F5794_03_TRAN |  |  |  | LO-MD-BP |  |
| SAP_MM_BC_CA_CONFIGURE_PC | Materials Management - Configuration | /SRMSMC/CREA_QLB_EVL | SRMSMC_CREA_QLB_EVL_TRAN |  |  |  | MM-PUR-GF |  |
| SAP_MM_BC_CA_CONFIGURE_PC | Materials Management - Configuration | RM06C020 | RM06C020_TRAN |  |  |  | MM-PUR-GF |  |
| SAP_MM_BC_CA_CONFIGURE_PC | Materials Management - Configuration | F3077 | F3077_03_TRAN |  |  |  | MM-PUR-GF |  |
| SAP_MM_BC_CA_CONFIGURE_PC | Materials Management - Configuration | F4042 | F4042_TRAN |  |  |  | MM-PUR-GF |  |
| SAP_MM_BC_CA_CONFIGURE_PC | Materials Management - Configuration | F2278 | F2278_TRAN |  |  |  | MM-PUR-GF |  |
| SAP_MM_BC_CA_CONFIGURE_PC | Materials Management - Configuration | F2412 | F2412_03_TRAN |  |  |  | MM-PUR-GF |  |
| SAP_CA_BC_IC_LND_MDA_PC | Master Data - Configuration | /SMB/75000002 | SMB_75000002_03_TRAN | /SMB/MDASCUST | Master Data as Customizing Data |  | SV-CLD-FRM-APP | SV-CLD-FRM-INF |
| SAP_CA_BC_IC_LND_MDA_PC | Master Data - Configuration | /SMB/MDASCUST_DIS |  | /SMB/MDASCUST | Master Data as Customizing Data |  | SV-CLD-FRM-APP | SV-CLD-FRM-INF |
| SAP_CA_BC_IC_LND_FIN_SR_BR_PC | Statutory Reporting for Brazil - Configuration | S_EBJ_98000420 | S_EBJ_98000420_TRAN | CIAP_C_NO_QUO_ST | Maintain Record Settings per Country/Region | 102797 | FI-LOC-FI-BR | FI-LOC-FI-BR |
| SAP_CA_BC_IC_LND_FIN_SR_BR_PC | Statutory Reporting for Brazil - Configuration | /TMF/70000252 | TMF_70000252_TRAN | /TMF/CCCFG_VC | Configure Asset Classes to Control Credits | 103689 | FI-LOC-FI-BR | FI-LOC-FI-BR |
| SAP_CA_BC_IC_LND_FIN_SR_BR_PC | Statutory Reporting for Brazil - Configuration | /TMF/70000089 | TMF_70000089_TRAN | /TMF/D_TIPOORDEM | Define Production Order Type | 102838 | FI-LOC-FI-BR | FI-LOC-FI-BR-ACR |
| SAP_CA_BC_IC_LND_FIN_SR_BR_PC | Statutory Reporting for Brazil - Configuration | /TMF/70000198 | TMF_70000198_TRAN | /TMF/D_R_FILTER | Assign Tax Type and Tax Code to Files | 103109 | FI-LOC-FI-BR | FI-LOC-FI-BR |
| SAP_CA_BC_IC_LND_FIN_SR_BR_PC | Statutory Reporting for Brazil - Configuration | /TMF/70000121 | TMF_70000121_TRAN | /TMF/CONTR_AUT_DET_V | Define Automatic Determination | 103147 | FI-LOC-FI-BR | FI-LOC-FI-BR-ACR |
| SAP_CA_BC_IC_LND_FIN_SR_BR_PC | Statutory Reporting for Brazil - Configuration | /TMF/70000230 | TMF_70000230_TRAN | /TMF/D_WHTX_TYPE | Define Withholding Tax Type | 103688 | FI-LOC-FI-BR | FI-LOC-FI-BR-ACR |
| SAP_CA_BC_IC_LND_FIN_SR_BR_PC | Statutory Reporting for Brazil - Configuration | /TMF/70000088 | TMF_70000088_TRAN | /TMF/D_CONF_BOM | Define Alternative Bill of Material | 102837 | FI-LOC-FI-BR | FI-LOC-FI-BR-ACR |
| SAP_CA_BC_IC_LND_FIN_SR_BR_PC | Statutory Reporting for Brazil - Configuration | /TMF/70000086 | TMF_70000086_TRAN | /TMF/D_MAT_CONF | Define Products and Services for EFD | 102836 | FI-LOC-FI-BR | FI-LOC-FI-BR-ACR |
| SAP_CA_BC_IC_LND_FIN_SR_BR_PC | Statutory Reporting for Brazil - Configuration | /TMF/70000085 | TMF_70000085_TRAN | /TMF/SPED_TXT_VC | Define Information Codes for EFD | 102834 | FI-LOC-FI-BR | FI-LOC-FI-BR-ACR |
| SAP_CA_BC_IC_LND_FIN_SR_BR_PC | Statutory Reporting for Brazil - Configuration | /TMF/70000070 | TMF_70000070_TRAN | /TMF/D_QUESTION | Define Company Questionnaire | 102656 | FI-LOC-FI-BR | FI-LOC-FI-BR-ACR |
| SAP_CA_BC_IC_LND_FIN_SR_BR_PC | Statutory Reporting for Brazil - Configuration | /TMF/70000065 | TMF_70000065_TRAN | /TMF/D_SIGNATAR | Define Company Signatory | 102649 | FI-LOC-FI-BR | FI-LOC-FI-BR-ACR |
| SAP_CA_BC_IC_LND_FIN_SR_BR_PC | Statutory Reporting for Brazil - Configuration | /TMF/70000063 | TMF_70000063_TRAN | /TMF/ORGSTR_VC | Define Organizational Structure | 102648 | FI-LOC-FI-BR | FI-LOC-FI-BR-ACR |
| SAP_CA_BC_IC_LND_FIN_SR_BR_PC | Statutory Reporting for Brazil - Configuration | S_ER9_52000069 | S_ER9_52000069_TRAN | CIAP_V_CFOP | Determine Relevance of CIAP Record Creation | 102796 | FI-LOC-FI-BR | FI-LOC-FI-BR |
| SAP_CA_BC_IC_LND_FIN_SR_BR_PC | Statutory Reporting for Brazil - Configuration | /TMF/70000369 | TMF_70000369_TRAN | /TMF/V_CCPRCSTCT | Define Production Cost Center Relevant for Credit Control | 105587 | FI-LOC-FI-BR | FI-LOC-FI-BR |
| SAP_CA_BC_IC_LND_FIN_SR_BR_PC | Statutory Reporting for Brazil - Configuration | CIAP_QUONR | CIAP_QUONR_TRAN | CIAP_QUONR | Number Ranges for Mapping CIAP Accounting Documents to FI Documents | 106091 | FI-LOC-FI-BR | FI-LOC-FI-BR |
| SAP_CA_BC_IC_LND_FIN_SR_BR_PC | Statutory Reporting for Brazil - Configuration | /TMF/70000541 | TMF_70000541_TRAN | /TMF/D_R_NATREND | Configure the Nature of Income | 106557 | FI-LOC-FI-BR | FI-LOC-FI-BR |
| SAP_CA_BC_IC_LND_FIN_SR_BR_PC | Statutory Reporting for Brazil - Configuration | /TMF/70000363 | TMF_70000363_TRAN | /TMF/D_WH_TAXGRP | Define Withholding Tax of Nota Fiscal | 105497 | FI-LOC-FI-BR | FI-LOC-FI-BR |
| SAP_CA_BC_IC_LND_FIN_SR_BR_PC | Statutory Reporting for Brazil - Configuration | CIAP_ACC | CIAP_ACC_TRAN | CIAP_ACC | Number Ranges for CIAP Accounting Documents | 106090 | FI-LOC-FI-BR | FI-LOC-FI-BR |
| SAP_CA_BC_IC_LND_FIN_SR_BR_PC | Statutory Reporting for Brazil - Configuration | S_EBJ_98000827 | S_EBJ_98000827_TRAN | CIAP_ACC | Number Ranges for CIAP Accounting Documents | 106090 | FI-LOC-FI-BR | FI-LOC-FI-BR |
| SAP_CA_BC_IC_LND_FIN_SR_BR_PC | Statutory Reporting for Brazil - Configuration | S_EBJ_98000561 | S_EBJ_98000561_TRAN | CIAP_QUONR | Number Ranges for Mapping CIAP Accounting Documents to FI Documents | 106091 | FI-LOC-FI-BR | FI-LOC-FI-BR |
| SAP_CA_BC_IC_LND_FIN_SR_BR_PC | Statutory Reporting for Brazil - Configuration | /TMF/70001106 | TMF_70001106_TRAN | /TMF/D_BOM_USAGE | Define Bill of Material Usage | 106938 | FI-LOC-FI-BR | FI-LOC-FI-BR-ACR |
| SAP_CA_BC_IC_LND_FIN_SR_BR_PC | Statutory Reporting for Brazil - Configuration | S_EBJ_98000417 | S_EBJ_98000417_TRAN | CIAP_C_ACCOUNT | Define Financial Account Information | 106903 | FI-LOC-FI-BR | FI-LOC-FI-BR |
| SAP_CA_BC_IC_LND_GLO_GCO_PC | Document and Reporting Compliance - Configuration | S_ER9_52003057 | S_ER9_52003057_TRAN | GCOV_ADV_LIC_CTR | Activate Document and Reporting Compliance Features | 105518 | FI-LOC-IAM | CA-GTF-CSC-DRC-LIC |
| SAP_FIN_BC_TRM_AARSESICONF_PC | TRM - Configuration for AAR Substitution Rules - Exposure Subitems | F7682 | F7682_TRAN |  |  |  | FIN-FSCM-TRM |  |
| SAP_CA_BC_IC_LND_LO_BDV_PC | Batch Derivation - Configuration | DVC8 |  | SIMG_CFMENUODRVDVC8 | Define Derivation Events | 103728 | LO-BM | LO-BM-2CL |
| SAP_CA_BC_IC_LND_LO_BDV_PC | Batch Derivation - Configuration | DSC6 |  | SIMG_CFMENUODRVDSC6 | Define Strategy Types to Determine Sending Batches | 103734 | LO-BM | LO-BM-2CL |
| SAP_CA_BC_IC_LND_LO_BDV_PC | Batch Derivation - Configuration | DVC1 |  | SIMG_CFMENUODRVDVC1 | Maintain Number Range for Batch Derivation ID | 103730 | LO-BM | LO-BM-2CL |
| SAP_CA_BC_IC_LND_LO_BDV_PC | Batch Derivation - Configuration | DSC7 |  | SIMG_CFMENUODRVDSC7 | Define Search Procedures to Determine Sending Batches | 103736 | LO-BM | LO-BM-2CL |
| SAP_CA_BC_IC_LND_LO_BDV_PC | Batch Derivation - Configuration | DVC2 |  | SIMG_CFMENUODRVDVC2 | Maintain Number Range for Batch Derivation Condition Records | 103729 | LO-BM | LO-BM-2CL |
| SAP_CA_BC_IC_LND_LO_BDV_PC | Batch Derivation - Configuration | DSC5 |  | SIMG_CFMENUODRVDSC5 | Define Access Sequences to Determine Sending Batches | 103732 | LO-BM | LO-BM-2CL |
| SAP_CA_BC_IC_LND_LO_BDV_PC | Batch Derivation - Configuration | DRC7 |  | SIMG_CFMENUODRVDRC7 | Define Search Procedures to Determine Receiving Batches | 103735 | LO-BM | LO-BM-2CL |
| SAP_CA_BC_IC_LND_LO_BDV_PC | Batch Derivation - Configuration | DRC6 |  | SIMG_CFMENUODRVDRC6 | Define Strategy Types to Determine Receiving Batches | 103733 | LO-BM | LO-BM-2CL |
| SAP_CA_BC_IC_LND_LO_BDV_PC | Batch Derivation - Configuration | DRC5 |  | SIMG_CFMENUODRVDRC5 | Define Access Sequences to Determine Receiving Batches | 103731 | LO-BM | LO-BM-2CL |
| SAP_CA_BC_IC_LND_LO_BDV_PC | Batch Derivation - Configuration | S_P00_07000044 | S_P00_07000044_TRAN | SIMG_CFMENUODRVDVC2 | Maintain Number Range for Batch Derivation Condition Records | 103729 | LO-BM | LO-BM-2CL |
| SAP_CA_BC_IC_LND_LO_BDV_PC | Batch Derivation - Configuration | S_P00_07000043 | S_P00_07000043_TRAN | SIMG_CFMENUODRVDVC1 | Maintain Number Range for Batch Derivation ID | 103730 | LO-BM | LO-BM-2CL |
| SAP_CA_BC_IC_LND_LO_BDV_PC | Batch Derivation - Configuration | DSC2 |  | SIMG_LOBM_DSC2 | Change Condition Tables to Determine Sending Batches | 103912 | LO-BM | LO-BM-2CL |
| SAP_CA_BC_IC_LND_LO_BDV_PC | Batch Derivation - Configuration | DSC1 |  | SIMG_LOBM_DSC1 | Create Condition Tables to Determine Sending Batches | 103911 | LO-BM | LO-BM-2CL |
| SAP_CA_BC_IC_LND_LO_BDV_PC | Batch Derivation - Configuration | DRC1 |  | SIMG_LOBM_DRC1 | Create Condition Tables to Determine Receiving Batches | 103960 | LO-BM | LO-BM-2CL |
| SAP_CA_BC_IC_LND_LO_BDV_PC | Batch Derivation - Configuration | DRC2 |  | SIMG_LOBM_DRC2 | Change Condition Tables to Determine Receiving Batches | 103961 | LO-BM | LO-BM-2CL |
| SAP_CA_BC_IC_LND_LO_BDV_PC | Batch Derivation - Configuration | S_ER9_52002458 | S_ER9_52002458_TRAN | SIMG_LOBM_DRC2 | Change Condition Tables to Determine Receiving Batches | 103961 | LO-BM | LO-BM-2CL |
| SAP_CA_BC_IC_LND_LO_BDV_PC | Batch Derivation - Configuration | S_ER9_52002457 | S_ER9_52002457_TRAN | SIMG_LOBM_DRC1 | Create Condition Tables to Determine Receiving Batches | 103960 | LO-BM | LO-BM-2CL |
| SAP_CA_BC_IC_LND_LO_BDV_PC | Batch Derivation - Configuration | S_ER9_52002437 | S_ER9_52002437_TRAN | SIMG_LOBM_DSC1 | Create Condition Tables to Determine Sending Batches | 103911 | LO-BM | LO-BM-2CL |
| SAP_CA_BC_IC_LND_LO_BDV_PC | Batch Derivation - Configuration | S_ER9_52002436 | S_ER9_52002436_TRAN | SIMG_LOBM_DSC2 | Change Condition Tables to Determine Sending Batches | 103912 | LO-BM | LO-BM-2CL |
| SAP_CA_BC_IC_LND_LO_BDV_PC | Batch Derivation - Configuration | S_ALR_87100532 | S_ALR_87100532_TRAN | SIMG_CFMENUODRVDSC5 | Define Access Sequences to Determine Sending Batches | 103732 | LO-BM | LO-BM-2CL |
| SAP_CA_BC_IC_LND_LO_BDV_PC | Batch Derivation - Configuration | S_ALR_87100531 | S_ALR_87100531_TRAN | SIMG_CFMENUODRVDRC5 | Define Access Sequences to Determine Receiving Batches | 103731 | LO-BM | LO-BM-2CL |
| SAP_CA_BC_IC_LND_LO_BDV_PC | Batch Derivation - Configuration | S_ALR_87100530 | S_ALR_87100530_TRAN | SIMG_CFMENUODRVDSC6 | Define Strategy Types to Determine Sending Batches | 103734 | LO-BM | LO-BM-2CL |
| SAP_CA_BC_IC_LND_LO_BDV_PC | Batch Derivation - Configuration | S_ALR_87100527 | S_ALR_87100527_TRAN | SIMG_CFMENUODRVDRC7 | Define Search Procedures to Determine Receiving Batches | 103735 | LO-BM | LO-BM-2CL |
| SAP_CA_BC_IC_LND_LO_BDV_PC | Batch Derivation - Configuration | S_ALR_87100528 | S_ALR_87100528_TRAN | SIMG_CFMENUODRVDSC7 | Define Search Procedures to Determine Sending Batches | 103736 | LO-BM | LO-BM-2CL |
| SAP_CA_BC_IC_LND_LO_BDV_PC | Batch Derivation - Configuration | S_ALR_87100529 | S_ALR_87100529_TRAN | SIMG_CFMENUODRVDRC6 | Define Strategy Types to Determine Receiving Batches | 103733 | LO-BM | LO-BM-2CL |
| SAP_CA_BC_IC_LND_LO_BDV_PC | Batch Derivation - Configuration | S_ALR_87100526 | S_ALR_87100526_TRAN | SIMG_CFMENUODRVDVC8 | Define Derivation Events | 103728 | LO-BM | LO-BM-2CL |
| SAP_CA_BC_IC_LND_FIN_CM2_PC | Cash Operations - Configuration | S_ALR_87007397 | S_ALR_87007397_TRAN | SIMG_CFMENUOFTDOT12 | Define Planning Levels | 101027 | FIN-FSCM-CLM | FIN-FSCM-CLM-FQM-2CL |
| SAP_CA_BC_IC_LND_FIN_CM2_PC | Cash Operations - Configuration | S_ALR_87009508 | S_ALR_87009508_TRAN | SIMG_CFMENUOFTDOT13 | Define Planning Groups | 101028 | FIN-FSCM-CLM | CA-FS-CVI-2CL |
| SAP_CA_BC_IC_LND_FIN_CM2_PC | Cash Operations - Configuration | S_ALR_87007261 | S_ALR_87007261_TRAN | SIMG_CFMENUOFTDOT23 | Maintain Blocked Levels | 101053 | FIN-FSCM-CLM | FIN-FSCM-CLM-FQM-2CL |
| SAP_CA_BC_IC_LND_FIN_CM2_PC | Cash Operations - Configuration | S_ER9_11001352 | S_ER9_11001352_TRAN | V_FCLM_CR_FDLEV | Assign Planning Levels to Cash Trade Requests | 103256 | FIN-FSCM-CLM | FIN-FSCM-CLM-2CL |
| SAP_CA_BC_IC_LND_FIN_CM2_PC | Cash Operations - Configuration | S_ER9_11000888 | S_ER9_11000888_TRAN | FCLM_CM_RECONCILE | Define Tolerance Groups for Cash Flow Reconciliation | 102474 | FIN-FSCM-CLM | FIN-FSCM-CLM-2CL |
| SAP_CA_BC_IC_LND_FIN_CM2_PC | Cash Operations - Configuration | S_ER9_11000763 | S_ER9_11000763_TRAN | FCLM_BALC_CONF | Assign Planning Levels to Profiles | 102211 | FIN-FSCM-CLM | FIN-FSCM-CLM-2CL |
| SAP_CA_BC_IC_LND_FIN_CM2_PC | Cash Operations - Configuration | S_ALR_87001860 | S_ALR_87001860_TRAN | SIMG_CFFIBAT042Y | Define Account Determination for Bank Clearing Accounts | 102803 | FIN-FSCM-CLM | FI-AP-AP-B-2CL |
| SAP_CA_BC_IC_LND_FIN_CM2_PC | Cash Operations - Configuration | S_ALR_87001755 | S_ALR_87001755_TRAN | SIMG_CFFIBAT018V | Define Clearing Accounts for Receiving Bank for Account Transfer | 102802 | FIN-FSCM-CLM | FI-AP-AP-B-2CL |
| SAP_CA_BC_IC_LND_FIN_CM2_PC | Cash Operations - Configuration | S_ALR_87007271 | S_ALR_87007271_TRAN | SIMG_CFMENUOFTDOT21 | Define Memo Record Types | 101029 | FIN-FSCM-CLM | FIN-FSCM-CLM-2CL |
| SAP_CA_BC_IC_LND_FIN_CM2_PC | Cash Operations - Configuration | S_ER9_11002105 | S_ER9_11002105_TRAN | FCLM_MR_GSTTG | Define Planning Levels for Bank Statements | 105440 | FIN-FSCM-CLM | FIN-FSCM-CLM-2CL |
| SAP_CA_BC_IC_LND_FIN_CM2_PC | Cash Operations - Configuration | S_ER9_11002202 | S_ER9_11002202_TRAN | FCLM_CPL_AGT | Define Authorization Groups for Cash Pools | 105663 | FIN-FSCM-CLM | FIN-FSCM-CLM-2CL |
| SAP_CA_BC_IC_LND_FIN_CM2_PC | Cash Operations - Configuration | FCLM_CPL_ASGTNR |  | FCLM_CP_NUMBER | Define Number Range for Cash Pools | 105664 | FIN-FSCM-CLM | FIN-FSCM-CLM-2CL |
| SAP_CA_BC_IC_LND_FIN_CM2_PC | Cash Operations - Configuration | S_ER9_11002197 | S_ER9_11002197_TRAN | FCLM_CP_NUMBER | Define Number Range for Cash Pools | 105664 | FIN-FSCM-CLM | FIN-FSCM-CLM-2CL |
| SAP_CA_BC_IC_LND_FIN_CM2_PC | Cash Operations - Configuration | S_ER9_11002614 | S_ER9_11002614_TRAN | FCLM_MR_RECON_PROF | Define Profiles for Cash Flow Reconciliation | 106226 | FIN-FSCM-CLM | FIN-FSCM-CLM-2CL |
| SAP_CA_BC_IC_LND_FIN_CM2_PC | Cash Operations - Configuration | FCLM_RCN_BNDLNR |  | FCLM_MR_RECON_BNDL | Define Number Range for Reconciliation Bundles | 106245 | FIN-FSCM-CLM | FIN-FSCM-CLM-2CL |
| SAP_CA_BC_IC_LND_FIN_CM2_PC | Cash Operations - Configuration | S_ER9_11002633 | S_ER9_11002633_TRAN | FCLM_MR_RECON_BNDL | Define Number Range for Reconciliation Bundles | 106245 | FIN-FSCM-CLM | FIN-FSCM-CLM-2CL |
| SAP_CA_BC_IC_LND_FIN_CM2_PC | Cash Operations - Configuration | S_ER9_11002712 | S_ER9_11002712_TRAN | FCLM_COP_MMRD_FSG | Manage Field Status Groups for Memo Records | 106455 | FIN-FSCM-CLM | FIN-FSCM-CLM-2CL |
| SAP_CA_BC_IC_LND_FIN_CM2_PC | Cash Operations - Configuration | FCLM_MR_MRINR |  | FCLM_MRMM2_NR | Define Number Range for Memo Record Imports | 106499 | FIN-FSCM-CLM | FIN-FSCM-CLM-2CL |
| SAP_CA_BC_IC_LND_FIN_CM2_PC | Cash Operations - Configuration | S_ER9_11002755 | S_ER9_11002755_TRAN | FCLM_MRMM2_NR | Define Number Range for Memo Record Imports | 106499 | FIN-FSCM-CLM | FIN-FSCM-CLM-2CL |
| SAP_CA_BC_IC_LND_FIN_CM2_PC | Cash Operations - Configuration | FCLM_MR_MMRNR |  | FCLM_MRN2 | Define Number Range for Memo Records | 106556 | FIN-FSCM-CLM | FIN-FSCM-CLM-2CL |
| SAP_CA_BC_IC_LND_FIN_CM2_PC | Cash Operations - Configuration | S_ER9_11002783 | S_ER9_11002783_TRAN | FCLM_MRN2 | Define Number Range for Memo Records | 106556 | FIN-FSCM-CLM | FIN-FSCM-CLM-2CL |
| SAP_CA_BC_IC_LND_FIN_CM2_PC | Cash Operations - Configuration | FCLM_CASH_CONCN |  | FCLM_CP_CONC_NR | Define Number Range for Cash Concentrations | 106736 | FIN-FSCM-CLM | FIN-FSCM-CLM-2CL |
| SAP_CA_BC_IC_LND_FIN_CM2_PC | Cash Operations - Configuration | S_ER1_70000907 | S_ER1_70000907_TRAN | FCLM_CP_CONC_NR | Define Number Range for Cash Concentrations | 106736 | FIN-FSCM-CLM | FIN-FSCM-CLM-2CL |
| SAP_CA_BC_IC_LND_FIN_CM2_PC | Cash Operations - Configuration | S_ER1_70000951 | S_ER1_70000951_TRAN | FCLM_CP_STTG | Define Settings for Cash Concentration | 106751 | FIN-FSCM-CLM | FIN-FSCM-CLM-2CL |
| SAP_CA_BC_IC_LND_FIN_CM2_PC | Cash Operations - Configuration | S_ER1_70001099 | S_ER1_70001099_TRAN | FCLM_CCONC_GROUP | Define Cash Concentration Groups for Cash Pools | 106818 | FIN-FSCM-CLM | FIN-FSCM-CLM-2CL |
| SAP_CA_BC_IC_LND_FIN_CM2_PC | Cash Operations - Configuration | FCLM_SNAPSHOT_NR |  | FCLM_SNAPSHOT_NR | Define Number Range for Cash Snapshots | 107181 | FIN-FSCM-CLM | FIN-FSCM-CLM-2CL |
| SAP_CA_BC_IC_LND_FIN_CM2_PC | Cash Operations - Configuration | S_ER1_70001702 | S_ER1_70001702_TRAN | FCLM_SNAPSHOT_NR | Define Number Range for Cash Snapshots | 107181 | FIN-FSCM-CLM | FIN-FSCM-CLM-2CL |
| SAP_CA_BC_IC_LND_CVP_DP0_PC | Customer/Supplier Data Privacy - Configuration | S_EBJ_98000363 | S_EBJ_98000363_TRAN | CVP_EOPARV | Assign Rule Variants and Groups for the Customer/Supplier EoP Check | 102442 | LO-MD-BP-DP | LO-MD-BP-DP-2CL |
| SAP_CA_BC_IC_LND_S4CRM_SO0_PC | Service Order - Configuration | S_ER1_70001527 | S_ER1_70001527_TRAN | CRMS4_SRV_SCPRI | Copy Procurement Price to Service Confirmation | 107047 | CRM-S4-SRV-SVO | CRM-S4-BTX-2CL |
| SAP_CA_BC_IC_LND_S4CRM_SO0_PC | Service Order - Configuration | S_ER1_83000045 | S_ER1_83000045_TRAN | CRMC_ORGMAN_008 | Define Service Team Profile and Assign Service Team Types | 103247 | CRM-S4-SRV-SVO | CRM-BF-2CL |
| SAP_CA_BC_IC_LND_S4CRM_SO0_PC | Service Order - Configuration | S_ER1_83000060 | S_ER1_83000060_TRAN | S4CRM_PLANT_SRV_CTRY | Assign Plant and Storage Location to Country/Region | 103352 | CRM-S4-SRV-SVO | CRM-BF-2CL |
| SAP_CA_BC_IC_LND_S4CRM_SO0_PC | Service Order - Configuration | S_ER1_70001885 | S_ER1_70001885_TRAN | CRMS4_SRV_CONCUR | Configure Concur Integration in Service Order Management | 107355 | CRM-S4-SRV-SVO | CRM-S4-SRV-SVO-2CL |
| SAP_CA_BC_IC_LND_S4CRM_SO0_PC | Service Order - Configuration | S_ER1_83000006 | S_ER1_83000006_TRAN | S4CRM_PLANT_SRV | Assign Plant and Storage Location to Service Employee and Country/Region | 102883 | CRM-S4-SRV-SVO | CRM-BF-2CL |
| SAP_CA_BC_IC_LND_S4CRM_SO0_PC | Service Order - Configuration | S_ER1_83000046 | S_ER1_83000046_TRAN | CRMC_ORGMAN_009 | Assign Service Team Profile to Service Transaction Type | 103246 | CRM-S4-SRV-SVO | CRM-BF-2CL |
| SAP_CA_BC_IC_LND_S4CRM_SO0_PC | Service Order - Configuration | S_ER1_83000030 | S_ER1_83000030_TRAN | S4CRM_SALES_I | Assign Condition Type to Item Categories (Service Orders and Confirmations) | 180011 | CRM-S4-SRV-SVO | CRM-BF-2CL |
| SAP_CA_BC_IC_LND_S4CRM_SO0_PC | Service Order - Configuration | S_ER1_83000085 | S_ER1_83000085_TRAN | S4CRM_PROC_I | Define Account Assignment Category for Procurement in Service Transactions | 103526 | CRM-S4-SRV-SVO | CRM-BF-2CL |
| SAP_CA_BC_IC_LND_CAL_CA0_PC | Factory Calendar - Configuration | S_YI3_39000476 | S_YI3_39000476_TRAN | SFHC_FCAL | Edit Factory Calendar |  | BC-SRV-ASF-CAL | BC-SRV-ASF-CAL |
| SAP_CA_BC_IC_LND_CAL_CA0_PC | Factory Calendar - Configuration | S_YI3_39000477 | S_YI3_39000477_TRAN | SFHC_HCAL | Edit Factory Calendar |  | BC-SRV-ASF-CAL | BC-SRV-ASF-CAL |
| SAP_CA_BC_IC_LND_CAL_CA0_PC | Factory Calendar - Configuration | S_YI3_39000478 | S_YI3_39000478_TRAN | SFHC_HOL | Edit Public Holidays |  | BC-SRV-ASF-CAL | BC-SRV-ASF-CAL |
| SAP_CA_BC_IC_LND_CAL_CA0_PC | Factory Calendar - Configuration | SFHC_HCAL |  | SFHC_HCAL | Edit Factory Calendar |  | BC-SRV-ASF-CAL | BC-SRV-ASF-CAL |
| SAP_CA_BC_IC_LND_CAL_CA0_PC | Factory Calendar - Configuration | SFHC_FCAL |  | SFHC_FCAL | Edit Factory Calendar |  | BC-SRV-ASF-CAL | BC-SRV-ASF-CAL |
| SAP_CA_BC_IC_LND_CAL_CA0_PC | Factory Calendar - Configuration | SFHC_HOL |  | SFHC_HOL | Edit Public Holidays |  | BC-SRV-ASF-CAL | BC-SRV-ASF-CAL |
| SAP_CA_BC_IC_LND_FIN_RE0_PC | Real Estate - Configuration | S_ALN_01001775 | S_ALN_01001775_TRAN | REFXV_TIVCAARRES | Define Residence Times for Archiving | 102407 | RE-FX | RE-FX-2CL |
| SAP_CA_BC_IC_LND_FIN_RE0_PC | Real Estate - Configuration | S_EBJ_45000178 | S_EBJ_45000178_TRAN | REFX_V_TIVCERULE | Valuation Rule | 102117 | RE-FX | RE-FX-2CL |
| SAP_CA_BC_IC_LND_FIN_RE0_PC | Real Estate - Configuration | S_ALN_01000920 | S_ALN_01000920_TRAN | REFXV_TIV26CNGROUP | Assign Condition Group to Contract per Contract Type |  | RE-FX | RE-FX-2CL |
| SAP_CA_BC_IC_LND_FIN_RE0_PC | Real Estate - Configuration | S_EBJ_45000229 | S_EBJ_45000229_TRAN | VC_TIVCECDGRP | Condition Valuation Groups | 103405 | RE-FX | RE-FX-2CL |
| SAP_CA_BC_IC_LND_FIN_RE0_PC | Real Estate - Configuration | S_ALN_01001554 | S_ALN_01001554_TRAN | REFXVC_REAJINDX | Enter Index Levels | 102192 | RE-FX | RE-FX-2CL |
| SAP_CA_BC_IC_LND_FIN_RE0_PC | Real Estate - Configuration | S_ALN_01000808 | S_ALN_01000808_TRAN | REFXV_TIVCDFLOWTYPE | Define Flow Types | 103398 | RE-FX | RE-FX-2CL |
| SAP_CA_BC_IC_LND_FIN_RE0_PC | Real Estate - Configuration | S_ALN_01001097 | S_ALN_01001097_TRAN | REFXV_TIVEXTAXMAP | Assign Tax Code (for FI Document) | 102115 | RE-FX | RE-FX-2CL |
| SAP_CA_BC_IC_LND_FIN_RE0_PC | Real Estate - Configuration | S_ALN_01000805 | S_ALN_01000805_TRAN | REFXVC_TIVCDCONDREL | Define Condition Groups and Assign Condition Types | 103400 | RE-FX | RE-FX-2CL |
| SAP_CA_BC_IC_LND_FIN_RE0_PC | Real Estate - Configuration | S_EBJ_45000241 | S_EBJ_45000241_TRAN | V_TIVCEASSETDIF | Valuation Object-Dependent Control Parameters | 102118 | RE-FX | RE-FX-2CL |
| SAP_CA_BC_IC_LND_FIN_RE0_PC | Real Estate - Configuration | S_EBJ_45000324 | S_EBJ_45000324_TRAN | V_TIVCEQUERYDIF | Control Parameters Question Catalog | 103253 | RE-FX | RE-FX-2CL |
| SAP_CA_BC_IC_LND_FIN_RE0_PC | Real Estate - Configuration | S_ALN_01000803 | S_ALN_01000803_TRAN | REFXV_TIVCDFLOWREL | Assign Reference Flow Types | 103403 | RE-FX | RE-FX-2CL |
| SAP_CA_BC_IC_LND_FIN_RE0_PC | Real Estate - Configuration | S_ALN_01000801 | S_ALN_01000801_TRAN | REFXV_TIVCDCONDTYPE | Define Condition Types | 103399 | RE-FX | RE-FX-2CL |
| SAP_CA_BC_IC_LND_FIN_RE0_PC | Real Estate - Configuration | S_ALN_01000663 | S_ALN_01000663_TRAN | REFXV_TIVRAACCSYMB | Account Symbols | 103402 | RE-FX | RE-FX-2CL |
| SAP_CA_BC_IC_LND_FIN_RE0_PC | Real Estate - Configuration | S_ALN_01000661 | S_ALN_01000661_TRAN | REFXV_TIVRAACCDET | Assign Account Symbol to Flow Type | 103404 | RE-FX | RE-FX-2CL |
| SAP_CA_BC_IC_LND_FIN_RE0_PC | Real Estate - Configuration | S_ALN_01000656 | S_ALN_01000656_TRAN | REFXV_TIVEXFIREPSYMB | Replace Account Symbols | 102120 | RE-FX | RE-FX-2CL |
| SAP_CA_BC_IC_LND_FIN_RE0_PC | Real Estate - Configuration | S_PLN_06000055 | S_PLN_06000055_TRAN | REFXV_TIVRATAXDFLT | Default Value for Tax Rate per Contract Type | 102703 | RE-FX | RE-FX-2CL |
| SAP_CA_BC_IC_LND_FIN_RE0_PC | Real Estate - Configuration | S_PLN_06000038 | S_PLN_06000038_TRAN | REFXV_TIVCARSREASON | Define Resubmission Reasons | 103847 | RE-FX | RE-FX-2CL |
| SAP_CA_BC_IC_LND_FIN_RE0_PC | Real Estate - Configuration | S_PLN_62000055 | S_PLN_62000055_TRAN | REFXV_TIVCDCHGREAS | Define Reason for Change | 103848 | RE-FX | RE-FX-2CL |
| SAP_CA_BC_IC_LND_FIN_RE0_PC | Real Estate - Configuration | S_EEI_11000063 | S_EEI_11000063_TRAN | REFXVC_TIVCARSRULPTM | Set Default Values for Reminder Rules and Enter Automatically in Contracts | 103839 | RE-FX | RE-FX-2CL |
| SAP_CA_BC_IC_LND_FIN_RE0_PC | Real Estate - Configuration | S_ALN_01002142 | S_ALN_01002142_TRAN | REFXVC_TIVCARSRULE | Define Resubmission Rules |  | RE-FX | RE-FX-2CL |
| SAP_CA_BC_IC_LND_FIN_RE0_PC | Real Estate - Configuration | S_ER9_11001033 | S_ER9_11001033_TRAN | REFXV_TIVCNSUBJCNTY | Permitted Contract Object Types for Each Contract Type | 102670 | RE-FX | RE-FX-CN-2CL |
| SAP_CA_BC_IC_LND_FIN_RE0_PC | Real Estate - Configuration | S_ALN_01002141 | S_ALN_01002141_TRAN | REFXVC_TIVCARSOTRR | Make Settings per Object Type | 103837 | RE-FX | RE-FX-2CL |
| SAP_CA_BC_IC_LND_FIN_RE0_PC | Real Estate - Configuration | S_ALN_01001272 | S_ALN_01001272_TRAN | REFX_V_TIVBPSUBROLE | Role Types | 103857 | RE-FX | RE-FX-2CL |
| SAP_CA_BC_IC_LND_FIN_RE0_PC | Real Estate - Configuration | S_ALN_01000691 | S_ALN_01000691_TRAN | REFXV_TIVCNCCTADD | Define Contract Types | 103849 | RE-FX | RE-FX-2CL |
| SAP_CA_BC_IC_LND_FIN_RE0_PC | Real Estate - Configuration | S_ALN_01000683 | S_ALN_01000683_TRAN | REFXV_TIVCNNTRE | Notice Reasons | 103851 | RE-FX | RE-FX-2CL |
| SAP_CA_BC_IC_LND_FIN_RE0_PC | Real Estate - Configuration | S_ALN_01001257 | S_ALN_01001257_TRAN | REFX_SNUMBDCN | Number Range for Contracts | 103860 | RE-FX | RE-FX-2CL |
| SAP_CA_BC_IC_LND_FIN_RE0_PC | Real Estate - Configuration | S_EBJ_45000325 | S_EBJ_45000325_TRAN | VC_TIVCEQUERY | Define Question Catalogs | 103252 | RE-FX | RE-FX-2CL |
| SAP_CA_BC_IC_LND_FIN_RE0_PC | Real Estate - Configuration | S_ALN_01000682 | S_ALN_01000682_TRAN | REFXV_TIVCNNTRR | Reasons for Rejection | 103852 | RE-FX | RE-FX-2CL |
| SAP_CA_BC_IC_LND_FIN_RE0_PC | Real Estate - Configuration | S_ALN_01000671 | S_ALN_01000671_TRAN | REFXVC_TIVTMNTPROC | Notice Procedures | 103840 | RE-FX | RE-FX-2CL |
| SAP_CA_BC_IC_LND_FIN_RE0_PC | Real Estate - Configuration | S_ALN_01001038 | S_ALN_01001038_TRAN | REFXVC_TIVTMRNRULE | Renewal Rules | 103843 | RE-FX | RE-FX-2CL |
| SAP_CA_BC_IC_LND_FIN_RE0_PC | Real Estate - Configuration | S_ALN_01000673 | S_ALN_01000673_TRAN | REFXVC_TIVTMNTRULEPR | Notice Rules: Period Regulations | 103842 | RE-FX | RE-FX-2CL |
| SAP_CA_BC_IC_LND_FIN_RE0_PC | Real Estate - Configuration | S_ALN_01001221 | S_ALN_01001221_TRAN | REFXCL_FVVIBUKRS | Basic Settings in Company Code |  | RE-FX | RE-FX-2CL |
| SAP_CA_BC_IC_LND_FIN_RE0_PC | Real Estate - Configuration | S_AER_95000244 | S_AER_95000244_TRAN | REFXV_TIVCACTCNTYPE | Specify Possible Currency Translation Rules per Contract Type | 103846 | RE-FX | RE-FX-2CL |
| SAP_CA_BC_IC_LND_FIN_RE0_PC | Real Estate - Configuration | S_ALN_01000672 | S_ALN_01000672_TRAN | REFXVC_TIVTMNTRULEDR | Notice Rules: Deadline Regulations | 103841 | RE-FX | RE-FX-2CL |
| SAP_CA_BC_IC_LND_FIN_RE0_PC | Real Estate - Configuration | S_ALN_01001558 | S_ALN_01001558_TRAN | REFXV_TIVSRRPT | Sales ID | 103854 | RE-FX | RE-FX-2CL |
| SAP_CA_BC_IC_LND_FIN_RE0_PC | Real Estate - Configuration | S_PLN_62000056 | S_PLN_62000056_TRAN | REFXV_TIVAJREAS | Define Adjustment Reason | 103844 | RE-FX | RE-FX-2CL |
| SAP_CA_BC_IC_LND_FIN_RE0_PC | Real Estate - Configuration | S_ALN_01001557 | S_ALN_01001557_TRAN | REFXV_TIVSRSR | Type of Sales Rule | 103855 | RE-FX | RE-FX-2CL |
| SAP_CA_BC_IC_LND_FIN_RE0_PC | Real Estate - Configuration | S_ALN_01001556 | S_ALN_01001556_TRAN | REFXV_TIVSRST | Sales Types | 103856 | RE-FX | RE-FX-2CL |
| SAP_CA_BC_IC_LND_FIN_RE0_PC | Real Estate - Configuration | S_PLN_06000028 | S_PLN_06000028_TRAN | REFXV_TIVCDDUEDATE | Due Date Correction Rule | 103787 | RE-FX | RE-FX-2CL |
| SAP_CA_BC_IC_LND_FIN_RE0_PC | Real Estate - Configuration | S_ALN_01002428 | S_ALN_01002428_TRAN | REFXV_TIVBPOBJROLE | Make Settings for Roles per Object Type | 103845 | RE-FX | RE-FX-2CL |
| SAP_CA_BC_IC_LND_FIN_RE0_PC | Real Estate - Configuration | S_EBJ_45000286 | S_EBJ_45000286_TRAN | V_TIVCERELEVAL | Valuation Relevance | 103858 | RE-FX | RE-FX-2CL |
| SAP_CA_BC_IC_LND_FIN_RE0_PC | Real Estate - Configuration | S_EBJ_45000257 | S_EBJ_45000257_TRAN | V_TIVCEASSETFT | Assign Asset Transaction Types | 103788 | RE-FX | RE-FX-2CL |
| SAP_CA_BC_IC_LND_FIN_RE0_PC | Real Estate - Configuration | S_ALN_01000655 | S_ALN_01000655_TRAN | REFXV_TIVEXFIDOCTYPE | Define Document Type Determination | 103853 | RE-FX | RE-FX-2CL |
| SAP_CA_BC_IC_LND_FIN_RE0_PC | Real Estate - Configuration | S_EBJ_45000227 | S_EBJ_45000227_TRAN | V_TIVCECTADD | Control Settings for Each Contract Type in Company Code | 103859 | RE-FX | RE-FX-2CL |
| SAP_CA_BC_IC_LND_FIN_RE0_PC | Real Estate - Configuration | S_EBJ_45000292 | S_EBJ_45000292_TRAN | REFXV_TIBBDCNSUBTYPE | Contract Object: Object Type | 102116 | RE-FX | RE-FX-BD-2CL |
| SAP_CA_BC_IC_LND_FIN_RE0_PC | Real Estate - Configuration | S_ALN_01000662 | S_ALN_01000662_TRAN | REFXV_TIVRADETKEY | Account Determination Values | 103789 | RE-FX | RE-FX-2CL |
| SAP_CA_BC_IC_LND_FIN_RE0_PC | Real Estate - Configuration | S_ALN_01000677 | S_ALN_01000677_TRAN | REFXV_TIVCNCCTFMOD | Field Status per Contract Type | 103850 | RE-FX | RE-FX-2CL |
| SAP_CA_BC_IC_LND_FIN_RE0_PC | Real Estate - Configuration | FOIX_NR | FOIX_NR_TRAN | REFX_SNUMBDCN | Number Range for Contracts | 103860 | RE-FX | RE-FX-2CL |
| SAP_CA_BC_IC_LND_FIN_RE0_PC | Real Estate - Configuration | S_ER9_11001614 | S_ER9_11001614_TRAN | REFXV_TIVXCBPLDOCTYP | Define Document Type Determination for Company Code | 103677 | RE-FX | RE-FX-LC |
| SAP_CA_BC_IC_LND_FIN_RE0_PC | Real Estate - Configuration | REIPIONR | REIPIONR_TRAN | REFX_SNUMIONR | Number Range for Real Estate Objects | 105400 | RE-FX | RE-FX-IP-2CL |
| SAP_CA_BC_IC_LND_FIN_RE0_PC | Real Estate - Configuration | S_ER9_11002070 | S_ER9_11002070_TRAN | REFX_SNUMIONR | Number Range for Real Estate Objects | 105400 | RE-FX | RE-FX-IP-2CL |
| SAP_CA_BC_IC_LND_FIN_RE0_PC | Real Estate - Configuration | S_ER9_11002069 | S_ER9_11002069_TRAN | V_TIVIPAREATYID | Maintain Area Types | 105393 | RE-FX | RE-FX-IP-2CL |
| SAP_CA_BC_IC_LND_FIN_RE0_PC | Real Estate - Configuration | S_ER9_11002071 | S_ER9_11002071_TRAN | V_TIVIPIOTYPE | Settings per Real Estate Object Type | 105401 | RE-FX | RE-FX-IP-2CL |
| SAP_CA_BC_IC_LND_FIN_RE0_PC | Real Estate - Configuration | S_PLN_62000480 | S_PLN_62000480_TRAN | REFXV_TIVBDOBJASSCN | Permitted Object Types per Contract Type | 105407 | RE-FX | RE-FX-2CL |
| SAP_CA_BC_IC_LND_FIN_RE0_PC | Real Estate - Configuration | S_ER9_11002053 | S_ER9_11002053_TRAN | V_TIVIPIOUSAGETY | Real Estate Object Usage Types | 105402 | RE-FX | RE-FX-IP-2CL |
| SAP_CA_BC_IC_LND_FIN_RE0_PC | Real Estate - Configuration | S_ER9_11002055 | S_ER9_11002055_TRAN | V_TIVIPCTRYREG | Country/Region Mapping | 105392 | RE-FX | RE-FX-IP-2CL |
| SAP_CA_BC_IC_LND_FIN_RE0_PC | Real Estate - Configuration | S_ER9_11002058 | S_ER9_11002058_TRAN | V_TIVIPAREAMAPIO | Area Type Mapping | 105396 | RE-FX | RE-FX-IP-2CL |
| SAP_CA_BC_IC_LND_FIN_RE0_PC | Real Estate - Configuration | S_ER9_11002056 | S_ER9_11002056_TRAN | V_TIVIPUSEMAPIO | Real Estate Object Usage Type Mapping | 105403 | RE-FX | RE-FX-IP-2CL |
| SAP_CA_BC_IC_LND_FIN_RE0_PC | Real Estate - Configuration | S_ER9_11002057 | S_ER9_11002057_TRAN | V_TIVIPAREAUNITM | Area Unit Mapping | 105397 | RE-FX | RE-FX-IP-2CL |
| SAP_CA_BC_IC_LND_FIN_RE0_PC | Real Estate - Configuration | S_ER9_11002050 | S_ER9_11002050_TRAN | V_TIVIPSGUSAGETY | Group Usage Types | 105405 | RE-FX | RE-FX-IP-2CL |
| SAP_CA_BC_IC_LND_FIN_RE0_PC | Real Estate - Configuration | S_ER9_11002052 | S_ER9_11002052_TRAN | V_TIVIPIOINTCN | Settings for Internal Cost allocation | 105406 | RE-FX | RE-FX-IP-2CL |
| SAP_CA_BC_IC_LND_FIN_RE0_PC | Real Estate - Configuration | S_ER9_11002051 | S_ER9_11002051_TRAN | V_TIVIPPMIO | Settings for Functional Location Integration |  | RE-FX | RE-FX-IP-2CL |
| SAP_CA_BC_IC_LND_FIN_RE0_PC | Real Estate - Configuration | S_ER9_11002049 | S_ER9_11002049_TRAN | V_TIVIPENUSETYPE | Usage Enablement Group Types | 105404 | RE-FX | RE-FX-IP-2CL |
| SAP_CA_BC_IC_LND_FIN_RE0_PC | Real Estate - Configuration | S_ER9_11002048 | S_ER9_11002048_TRAN | V_TIVCACHARTCOL | Maintain Colors for Charts | 105398 | RE-FX | RE-FX-2CL |
| SAP_CA_BC_IC_LND_FIN_RE0_PC | Real Estate - Configuration | S_ALN_01000689 | S_ALN_01000689_TRAN | REFXV_TIVBDMEAS | Define Measurement Types | 105394 | RE-FX | RE-FX-2CL |
| SAP_CA_BC_IC_LND_FIN_RE0_PC | Real Estate - Configuration | S_ALN_01001020 | S_ALN_01001020_TRAN | REFXV_TIVBDMEASSUM | Define Total Measurements | 105395 | RE-FX | RE-FX-2CL |
| SAP_CA_BC_IC_LND_FIN_RE0_PC | Real Estate - Configuration | S_ER9_11002163 | S_ER9_11002163_TRAN | V_TIVIPUSAGETYID | Maintain Usage Types | 105554 | RE-FX | RE-FX-IP-2CL |
| SAP_CA_BC_IC_LND_FIN_RE0_PC | Real Estate - Configuration | S_ALN_01000654 | S_ALN_01000654_TRAN | REFXV_TIVEXFITAXMAP | Assign Tax Codes | 102119 | RE-FX | RE-FX-2CL |
| SAP_CA_BC_IC_LND_FIN_RE0_PC | Real Estate - Configuration | REEXZB | REEXZB_TRAN | REFXV_TIVEXFITAXMAP | Assign Tax Codes | 102119 | RE-FX | RE-FX-2CL |
| SAP_CA_BC_IC_LND_FIN_RE0_PC | Real Estate - Configuration | S_ER9_11002168 | S_ER9_11002168_TRAN | V_TIVIPIOSTATUS | Define Real Estate Object Status | 105658 | RE-FX | RE-FX-IP-2CL |
| SAP_CA_BC_IC_LND_FIN_RE0_PC | Real Estate - Configuration | S_ER9_11002430 | S_ER9_11002430_TRAN | VC_RECASTATUSPROFILE | Define Real Estate Status Profiles | 105915 | RE-FX | RE-FX-2CL |
| SAP_CA_BC_IC_LND_FIN_RE0_PC | Real Estate - Configuration | S_ER9_11002577 | S_ER9_11002577_TRAN | V_TIVCSCOSTCATE | Define Real Estate Cost Category | 106148 | RE-FX | RE-FX-CS-2CL |
| SAP_CA_BC_IC_LND_FIN_RE0_PC | Real Estate - Configuration | S_ER9_11002167 | S_ER9_11002167_TRAN | V_TIVIPSTATUSMAP | Object Status Mapping | 105659 | RE-FX | RE-FX-IP-2CL |
| SAP_CA_BC_IC_LND_FIN_RE0_PC | Real Estate - Configuration | FOB0 | FOB0_TRAN | REFX_SNUMRAFOB0 | Set Up Number Range for Automatically Created Posting Documents |  | RE-FX | RE-FX-2CL |
| SAP_CA_BC_IC_LND_FIN_RE0_PC | Real Estate - Configuration | S_ER9_11002579 | S_ER9_11002579_TRAN | V_TIVCSCEGLASS | Define Cost Element / GL Account assignment | 106159 | RE-FX | RE-FX-CS-2CL |
| SAP_CA_BC_IC_LND_FIN_RE0_PC | Real Estate - Configuration | S_PDE_26000001 | S_PDE_26000001_TRAN | REFX_SNUMRAFOB0 | Set Up Number Range for Automatically Created Posting Documents |  | RE-FX | RE-FX-2CL |
| SAP_CA_BC_IC_LND_FIN_RE0_PC | Real Estate - Configuration | S_ER9_11002572 | S_ER9_11002572_TRAN | V_TIVCSCOSTCATGR | Define Real Estate Cost Category Group | 106149 | RE-FX | RE-FX-CS-2CL |
| SAP_CA_BC_IC_LND_FIN_RE0_PC | Real Estate - Configuration | S_ER9_11002570 | S_ER9_11002570_TRAN | V_TIVCSCOSTHIER | Define Real Estate Cost Hierarchy | 106150 | RE-FX | RE-FX-CS-2CL |
| SAP_CA_BC_IC_LND_FIN_RE0_PC | Real Estate - Configuration | S_ER1_70001904 | S_ER1_70001904_TRAN | REFXV_TIVCSADVCDTYPE | Define Default Condition Type for Advance Payment or Flatrate | 107373 | RE-FX | RE-FX-CS-2CL |
| SAP_CA_BC_IC_LND_FIN_RE0_PC | Real Estate - Configuration | S_ER9_11002668 | S_ER9_11002668_TRAN | V_TIVCSCEFLOWTY | Define Flow Type Assignment to Cost Category | 106275 | RE-FX | RE-FX-CS-2CL |
| SAP_CA_BC_IC_LND_FIN_RE0_PC | Real Estate - Configuration | S_ER1_70000695 | S_ER1_70000695_TRAN | REFXV_TIVGOOWNERSHIP | Define Ownership IDs for Usable Objects | 106593 | RE-FX | RE-FX-BD-2CL |
| SAP_CA_BC_IC_LND_FIN_RE0_PC | Real Estate - Configuration | S_ALN_01000658 | S_ALN_01000658_TRAN | REFXV_TIVRATAXGROUP | Create Tax Groups | 106247 | RE-FX | RE-FX-2CL |
| SAP_CA_BC_IC_LND_FIN_RE0_PC | Real Estate - Configuration | S_ER1_70001835 | S_ER1_70001835_TRAN | REFXV_TIVCSSETTLCDTY | Define Condition Type for Cost Settlement | 107292 | RE-FX | RE-FX-CS-2CL |
| SAP_CA_BC_IC_LND_FIN_RE0_PC | Real Estate - Configuration | S_ER1_70000763 | S_ER1_70000763_TRAN | REFXV_TIVOBSTATUS | Define Statuses for Architecture Objects |  | RE-FX | RE-FX-BD-2CL |
| SAP_CA_BC_IC_LND_FIN_RE0_PC | Real Estate - Configuration | RECSSGNR | RECSSGNR_TRAN | REFX_RECSSGNR | Define Number Range for Service Group | 106151 | RE-FX | RE-FX-CS-2CL |
| SAP_CA_BC_IC_LND_FIN_RE0_PC | Real Estate - Configuration | S_ER9_11002576 | S_ER9_11002576_TRAN | V_TIVCSSETTLPROC | Define Real Estate Settlement Procedure | 106270 | RE-FX | RE-FX-CS-2CL |
| SAP_CA_BC_IC_LND_FIN_RE0_PC | Real Estate - Configuration | S_ER1_70000696 | S_ER1_70000696_TRAN | REFXV_TIVGOPORTFOLIO | Define Portfolio IDs for Usable Objects | 106594 | RE-FX | RE-FX-BD-2CL |
| SAP_CA_BC_IC_LND_FIN_RE0_PC | Real Estate - Configuration | S_ER1_70000762 | S_ER1_70000762_TRAN | REFXV_TIVOBNODE | Define Permitted Superordinate Architecture Object Types | 106630 | RE-FX | RE-FX-BD-2CL |
| SAP_CA_BC_IC_LND_FIN_RE0_PC | Real Estate - Configuration | S_ER1_70001304 | S_ER1_70001304_TRAN | REFXV_TIVEXCOEXACDET | Define Real Estate G/L Account Determination | 106906 | RE-FX | RE-FX-CO-2CL |
| SAP_CA_BC_IC_LND_FIN_RE0_PC | Real Estate - Configuration | S_ER9_11002588 | S_ER9_11002588_TRAN | REFX_RECSSGNR | Define Number Range for Service Group | 106151 | RE-FX | RE-FX-CS-2CL |
| SAP_CA_BC_IC_LND_FIN_RE0_PC | Real Estate - Configuration | S_ER1_70000699 | S_ER1_70000699_TRAN | REFX_REGOGONR | Define Number Ranges for Generic Rental Objects | 106591 | RE-FX | RE-FX-BD-2CL |
| SAP_CA_BC_IC_LND_FIN_RE0_PC | Real Estate - Configuration | S_ER1_70000764 | S_ER1_70000764_TRAN | REFX_REOBOBNR | Define Number Ranges for Architecture Objects | 106628 | RE-FX | RE-FX-BD-2CL |
| SAP_CA_BC_IC_LND_FIN_RE0_PC | Real Estate - Configuration | S_ER1_70001248 | S_ER1_70001248_TRAN | REFXV_TIVEXCOEXPTYPE | Define Real Estate Expense Type | 106882 | RE-FX | RE-FX-CO-2CL |
| SAP_CA_BC_IC_LND_FIN_RE0_PC | Real Estate - Configuration | REOBOBNR | REOBOBNR_TRAN | REFX_REOBOBNR | Define Number Ranges for Architecture Objects | 106628 | RE-FX | RE-FX-BD-2CL |
| SAP_CA_BC_IC_LND_FIN_RE0_PC | Real Estate - Configuration | S_ER1_70000761 | S_ER1_70000761_TRAN | REFXV_TIVOBOBJTYPE | Define Architecture Object Types | 106629 | RE-FX | RE-FX-BD-2CL |
| SAP_CA_BC_IC_LND_FIN_RE0_PC | Real Estate - Configuration | S_ALN_01001565 | S_ALN_01001565_TRAN | REFXV_TIVCAAUTHGRP | Define Authorization Groups | 106307 | RE-FX | RE-FX-2CL |
| SAP_CA_BC_IC_LND_FIN_RE0_PC | Real Estate - Configuration | S_ER1_70000698 | S_ER1_70000698_TRAN | REFXV_TIVGOUSAGETYPE | Define Usage Types for Generic Rental Objects | 106592 | RE-FX | RE-FX-BD-2CL |
| SAP_CA_BC_IC_LND_FIN_RE0_PC | Real Estate - Configuration | S_ER9_11002573 | S_ER9_11002573_TRAN | V_TIVCSPART2COST | Define Participation per Cost Category | 106273 | RE-FX | RE-FX-CS-2CL |
| SAP_CA_BC_IC_LND_FIN_RE0_PC | Real Estate - Configuration | S_ER9_11002580 | S_ER9_11002580_TRAN | V_TIVCSCOMPASS | Assign Settlement Procedure to Company Code | 106157 | RE-FX | RE-FX-CS-2CL |
| SAP_CA_BC_IC_LND_FIN_RE0_PC | Real Estate - Configuration | S_ER9_11002571 | S_ER9_11002571_TRAN | V_TIVCSCNPARTPRO | Define Participation Procedure for Contract/Usage Type | 106274 | RE-FX | RE-FX-CS-2CL |
| SAP_CA_BC_IC_LND_FIN_RE0_PC | Real Estate - Configuration | REGOGONR | REGOGONR_TRAN | REFX_REGOGONR | Define Number Ranges for Generic Rental Objects | 106591 | RE-FX | RE-FX-BD-2CL |
| SAP_CA_BC_IC_LND_FIN_RE0_PC | Real Estate - Configuration | S_ER9_11002574 | S_ER9_11002574_TRAN | V_TIVCSPARTPROC | Define Real Estate Participation Procedure | 106271 | RE-FX | RE-FX-CS-2CL |
| SAP_CA_BC_IC_LND_FIN_RE0_PC | Real Estate - Configuration | S_ER9_11002667 | S_ER9_11002667_TRAN | V_TIVCSSGCATE | Define Real Estate Service Group Category | 106269 | RE-FX | RE-FX-CS-2CL |
| SAP_CA_BC_IC_LND_FIN_RE0_PC | Real Estate - Configuration | S_ER9_11002575 | S_ER9_11002575_TRAN | V_TIVCSS2PPROC | Assign Participation Procedure to Settlement Procedure | 106272 | RE-FX | RE-FX-CS-2CL |
| SAP_CA_BC_IC_LND_LOG_AR_PC | Logistics for Argentina - Configuration | S_EBS_44000495 | S_EBS_44000495_TRAN | V_1A_WS_BRANCH | Define a Branch for Web Service | 102859 | FI-LOC-LO-AR | FI-LOC-LO-AR |
| SAP_CA_BC_IC_LND_LOG_AR_PC | Logistics for Argentina - Configuration | S_EBS_44000493 | S_EBS_44000493_TRAN | J_1A_WS_COND_MAP | Assign Condition Types to Material Codes | 102855 | FI-LOC-LO-AR | FI-LOC-LO-AR |
| SAP_CA_BC_IC_LND_LOG_AR_PC | Logistics for Argentina - Configuration | S_AL0_19000061 | S_AL0_19000061_TRAN | OFFDOCNO_AR_001 | Maintain Number Groups | 102774 | FI-LOC-LO-AR | FI-LOC-LO-AR |
| SAP_CA_BC_IC_LND_LOG_AR_PC | Logistics for Argentina - Configuration | S_EBJ_98000257 | S_EBJ_98000257_TRAN | V_J1AVATCODE | Define VAT Rate Codes and VAT Percentages for Web Service | 102860 | FI-LOC-LO-AR | FI-LOC-LO-AR |
| SAP_CA_BC_IC_LND_LOG_AR_PC | Logistics for Argentina - Configuration | S_EB5_05000116 | S_EB5_05000116_TRAN | J_1AVEBRCH | Define Electronic Branches | 102854 | FI-LOC-LO-AR | FI-LOC-LO-AR |
| SAP_CA_BC_IC_LND_LOG_AR_PC | Logistics for Argentina - Configuration | S_EBS_44000492 | S_EBS_44000492_TRAN | J_1A_RFC_DEST | Define Settings for Web Services | 102856 | FI-LOC-LO-AR | FI-LOC-LO-AR |
| SAP_CA_BC_IC_LND_LOG_AR_PC | Logistics for Argentina - Configuration | S_AL0_19000057 | S_AL0_19000057_TRAN | OFFDOCNO_AR_008 | Generate Number Groups | 102773 | FI-LOC-LO-AR | FI-LOC-LO-AR |
| SAP_CA_BC_IC_LND_LOG_AR_PC | Logistics for Argentina - Configuration | S_AL0_19000056 | S_AL0_19000056_TRAN | OFFDOCNO_AR_007 | Define Print Characters | 102775 | FI-LOC-LO-AR | FI-LOC-LO-AR |
| SAP_CA_BC_IC_LND_LOG_AR_PC | Logistics for Argentina - Configuration | S_ER9_52001627 | S_ER9_52001627_TRAN | EDOARPRINTFORMV | Configure Printing Form for eInvoice | 103277 | FI-LOC-LO-AR | CA-GTF-CSC-EDO-AR |
| SAP_CA_BC_IC_LND_LOG_AR_PC | Logistics for Argentina - Configuration | S_EB5_05000117 | S_EB5_05000117_TRAN | J_1A_V_CAE_REJCD | Maintain AFIP Return Codes and Descriptions | 106132 | FI-LOC-LO-AR | FI-LOC-LO-AR |
| SAP_CA_BC_IC_LND_LOG_AR_PC | Logistics for Argentina - Configuration | S_ALR_87006727 | S_ALR_87006727_TRAN | J_1AASSIGN_BR_SHIP | Assign Issuing Branch to Shipping Point | 106135 | FI-LOC-LO-AR | FI-LOC-LO-AR |
| SAP_CA_BC_IC_LND_LOG_AR_PC | Logistics for Argentina - Configuration | S_EBS_44000344 | S_EBS_44000344_TRAN | J_1A_UOMCODE | Maintain Unit of Measure | 106141 | FI-LOC-LO-AR | FI-LOC-LO-AR |
| SAP_CA_BC_IC_LND_LOG_AR_PC | Logistics for Argentina - Configuration | S_EBS_44000343 | S_EBS_44000343_TRAN | J_1A_CURCODE | Maintain Currency Codes | 106143 | FI-LOC-LO-AR | FI-LOC-LO-AR |
| SAP_CA_BC_IC_LND_LOG_AR_PC | Logistics for Argentina - Configuration | S_EBS_44000342 | S_EBS_44000342_TRAN | J_1A_CTYCODE | Maintain Country/Region Codes | 106142 | FI-LOC-LO-AR | FI-LOC-LO-AR |
| SAP_CA_BC_IC_LND_LOG_AR_PC | Logistics for Argentina - Configuration | S_ER9_52001410 | S_ER9_52001410_TRAN | GLO_ODN_DOC_TY_V_AR | Assign Document Types to Billing Types | 102908 | FI-LOC-LO-AR | FI-LOC-SD-AR |
| SAP_CA_BC_IC_LND_LOG_AR_PC | Logistics for Argentina - Configuration | S_ALR_87003246 | S_ALR_87003246_TRAN | J_1AREASON_PER_TAXC4 | Assign Reasons to Tax Codes | 106144 | FI-LOC-LO-AR | FI-AR-AR-2CL |
| SAP_CA_BC_IC_LND_LOG_AR_PC | Logistics for Argentina - Configuration | S_AL0_19000053 | S_AL0_19000053_TRAN | OFFDOCNO_AR_005 | Define Document Classes | 106140 | FI-LOC-LO-AR | FI-LOC-LO-AR |
| SAP_CA_BC_IC_LND_LOG_AR_PC | Logistics for Argentina - Configuration | S_AL0_19000058 | S_AL0_19000058_TRAN | OFFDOCNO_AR_002 | Maintain Number Ranges | 106160 | FI-LOC-LO-AR | FI-LOC-LO-AR |
| SAP_CA_BC_IC_LND_LOG_AR_PC | Logistics for Argentina - Configuration | J1AB | J1AB_TRAN |  |  |  | FI-LOC-LO-AR |  |
| SAP_CA_BC_IC_LND_LOG_AR_PC | Logistics for Argentina - Configuration | S_ALR_87003303 | S_ALR_87003303_TRAN | J_1ATAX_CLASSIF4 | Maintain Tax Classification | 102772 | FI-LOC-LO-AR | FI-AR-AR-2CL |
| SAP_CA_BC_IC_LND_LOG_AR_PC | Logistics for Argentina - Configuration | S_ALR_87003300 | S_ALR_87003300_TRAN | J_1ATAX_MINIMUM4 | Maintain Minimum Amounts per Processing Key | 102771 | FI-LOC-LO-AR | FI-AR-AR-2CL |
| SAP_CA_BC_IC_LND_LOG_AR_PC | Logistics for Argentina - Configuration | S_ALR_87003298 | S_ALR_87003298_TRAN | J_1ATAXCAT_BKRS_INFK | Maintain Company Code Tax Categories for Accounts Payable | 102770 | FI-LOC-LO-AR | FI-AR-AR-2CL |
| SAP_CA_BC_IC_LND_LOG_AR_PC | Logistics for Argentina - Configuration | S_ALR_87003295 | S_ALR_87003295_TRAN | J_1ATAXCAT_BKRS_INFD | Maintain Company Code Tax Categories for Accounts Receivable | 102769 | FI-LOC-LO-AR | FI-AR-AR-2CL |
| SAP_CA_BC_IC_LND_LOG_AR_PC | Logistics for Argentina - Configuration | S_ALR_87003293 | S_ALR_87003293_TRAN | J_1ATAX_CAT | Maintain Tax Categories | 102768 | FI-LOC-LO-AR | FI-AR-AR-2CL |
| SAP_CA_BC_IC_LND_LOG_AR_PC | Logistics for Argentina - Configuration | S_ALR_87003113 | S_ALR_87003113_TRAN | J_1AACTIVITY_GIT4 | Define Activity Codes for Gross Income Tax | 106249 | FI-LOC-LO-AR | FI-AR-AR-2CL |
| SAP_CA_BC_IC_LND_LOG_AR_PC | Logistics for Argentina - Configuration | S_ALR_87003112 | S_ALR_87003112_TRAN | J_1AGI_DIST_TYPES4 | Define Distribution Type for Gross Income Tax | 106250 | FI-LOC-LO-AR | FI-AR-AR-2CL |
| SAP_CA_BC_IC_LND_LOG_AR_PC | Logistics for Argentina - Configuration | S_AL0_19000052 | S_AL0_19000052_TRAN | OFFDOCNO_AR_004 | Define Issuing Branches | 106681 | FI-LOC-LO-AR | FI-LOC-LO-AR |
| SAP_CA_BC_IC_LND_LOG_AR_PC | Logistics for Argentina - Configuration | S_ALR_87003243 | S_ALR_87003243_TRAN | J_1AREASON_DEF4 | Define Reasons | 102858 | FI-LOC-LO-AR | FI-AR-AR-2CL |
| SAP_CA_BC_IC_LND_LOG_AR_PC | Logistics for Argentina - Configuration | S_ER9_52001356 | S_ER9_52001356_TRAN | EDOARCERTALIASV | Assign Digital Certificate to Branch | 102882 | FI-LOC-LO-AR | CA-GTF-CSC-EDO-AR |
| SAP_CA_BC_IC_LND_PP_MFGMD_PC | Manufacturing Master Data - Configuration | S_ALR_87004624 | S_ALR_87004624_TRAN | SIMG_CFMENUOLPFOPJR | Define Move Time Matrix |  | PP-BD-RTG | PP-SFC-PLN-2CL |
| SAP_CA_BC_IC_LND_PP_MFGMD_PC | Manufacturing Master Data - Configuration | OP72 |  | SIMG_CFMENUOLPSOP72 | Define PRT control keys | 103762 | PP-BD-RTG | PP-BD-RTG-2CL |
| SAP_CA_BC_IC_LND_PP_MFGMD_PC | Manufacturing Master Data - Configuration | S_ALR_87004628 | S_ALR_87004628_TRAN | SIMG_CFMENUOLPSOP10 | Determine Person Responsible | 102966 | PP-BD-RTG | PP-BD-RTG-2CL |
| SAP_CA_BC_IC_LND_PP_MFGMD_PC | Manufacturing Master Data - Configuration | S_ALR_87004605 | S_ALR_87004605_TRAN | SIMG_CFMENUOLPSOP7B | Define Parameters | 102242 | PP-BD-RTG | PP-BD-RTG-2CL |
| SAP_CA_BC_IC_LND_PP_MFGMD_PC | Manufacturing Master Data - Configuration | S_ALR_87004626 | S_ALR_87004626_TRAN | SIMG_CFMENUOLPFOPJQ | Define Standard Value Keys |  | PP-BD-RTG | PP-SFC-PLN-2CL |
| SAP_CA_BC_IC_LND_PP_MFGMD_PC | Manufacturing Master Data - Configuration | OP80 |  | SIMG_CFMENUOLPSOP80 | Define PRT status | 103723 | PP-BD-RTG | PP-BD-RTG-2CL |
| SAP_CA_BC_IC_LND_PP_MFGMD_PC | Manufacturing Master Data - Configuration | S_ALR_87004248 | S_ALR_87004248_TRAN | SIMG_CFMENUOLPKOP4A | Define Shift Sequences | 102429 | PP-BD-RTG | PP-BD-RTG-2CL |
| SAP_CA_BC_IC_LND_PP_MFGMD_PC | Manufacturing Master Data - Configuration | OP74 |  | SIMG_CFMENUOLPSOP74 | Define PRT group key | 103722 | PP-BD-RTG | PP-BD-RTG-2CL |
| SAP_CA_BC_IC_LND_PP_MFGMD_PC | Manufacturing Master Data - Configuration | S_ALR_87003963 | S_ALR_87003963_TRAN | SIMG_CFMENUOLPSOP21 | Define Formulas for Work Centers | 102002 | PP-BD-RTG | PP-BD-RTG-2CL |
| SAP_CA_BC_IC_LND_PP_MFGMD_PC | Manufacturing Master Data - Configuration | S_ALR_87003923 | S_ALR_87003923_TRAN | SIMG_CFMENUOLPSOP44 | Define Task List Usage for Routings | 102533 | PP-BD-RTG | PP-BD-RTG-2CL |
| SAP_CA_BC_IC_LND_PP_MFGMD_PC | Manufacturing Master Data - Configuration | OP21 |  | SIMG_CFMENUOLPSOP21 | Define Formulas for Work Centers | 102002 | PP-BD-RTG | PP-BD-RTG-2CL |
| SAP_CA_BC_IC_LND_PP_MFGMD_PC | Manufacturing Master Data - Configuration | OPJR |  | SIMG_CFMENUOLPFOPJR | Define Move Time Matrix |  | PP-BD-RTG | PP-SFC-PLN-2CL |
| SAP_CA_BC_IC_LND_PP_MFGMD_PC | Manufacturing Master Data - Configuration | OPJQ |  | SIMG_CFMENUOLPFOPJQ | Define Standard Value Keys |  | PP-BD-RTG | PP-SFC-PLN-2CL |
| SAP_CA_BC_IC_LND_PP_MFGMD_PC | Manufacturing Master Data - Configuration | OPJ8 |  | SIMG_CFMENUOLPFOPJ8 | Define control key |  | PP-BD-RTG | PP-SFC-PLN-2CL |
| SAP_CA_BC_IC_LND_PP_MFGMD_PC | Manufacturing Master Data - Configuration | OP7B |  | SIMG_CFMENUOLPSOP7B | Define Parameters | 102242 | PP-BD-RTG | PP-BD-RTG-2CL |
| SAP_CA_BC_IC_LND_PP_MFGMD_PC | Manufacturing Master Data - Configuration | OP4A |  | SIMG_CFMENUOLPKOP4A | Define Shift Sequences | 102429 | PP-BD-RTG | PP-BD-RTG-2CL |
| SAP_CA_BC_IC_LND_PP_MFGMD_PC | Manufacturing Master Data - Configuration | S_ALR_87004501 | S_ALR_87004501_TRAN | SIMG_CFMENUOLPFOPJ8 | Define control key |  | PP-BD-RTG | PP-SFC-PLN-2CL |
| SAP_CA_BC_IC_LND_PP_MFGMD_PC | Manufacturing Master Data - Configuration | S_ALR_87004619 | S_ALR_87004619_TRAN | SIMG_CFMENUOLPSOP30 | Define Move Time Matrix | 103397 | PP-BD-RTG | PP-BD-RTG-2CL |
| SAP_CA_BC_IC_LND_PP_MFGMD_PC | Manufacturing Master Data - Configuration | S_ALR_87004614 | S_ALR_87004614_TRAN | SIMG_CFMENUOLPSOP19 | Define Standard Value Key | 102003 | PP-BD-RTG | PP-BD-RTG-2CL |
| SAP_CA_BC_IC_LND_PP_MFGMD_PC | Manufacturing Master Data - Configuration | S_ALR_87004422 | S_ALR_87004422_TRAN | SIMG_CFMENUOLPKOPCD | Define Capacity Category | 102984 | PP-BD-RTG | PP-BD-RTG-2CL |
| SAP_CA_BC_IC_LND_PP_MFGMD_PC | Manufacturing Master Data - Configuration | OP30 |  | SIMG_CFMENUOLPSOP30 | Define Move Time Matrix | 103397 | PP-BD-RTG | PP-BD-RTG-2CL |
| SAP_CA_BC_IC_LND_PP_MFGMD_PC | Manufacturing Master Data - Configuration | OP67 |  | SIMG_CFMENUOLPSOP67 | Define Control Key | 102001 | PP-BD-RTG | PP-BD-RTG-2CL |
| SAP_CA_BC_IC_LND_PP_MFGMD_PC | Manufacturing Master Data - Configuration | S_ALR_87007513 | S_ALR_87007513_TRAN | SAPC_STANDORT | Define Location | 102783 | PP-BD-RTG | PM-2CL |
| SAP_CA_BC_IC_LND_PP_MFGMD_PC | Manufacturing Master Data - Configuration | S_ALR_87003879 | S_ALR_87003879_TRAN | SIMG_CFMENUOLPSOP67 | Define Control Key | 102001 | PP-BD-RTG | PP-BD-RTG-2CL |
| SAP_CA_BC_IC_LND_PP_MFGMD_PC | Manufacturing Master Data - Configuration | OP19 |  | SIMG_CFMENUOLPSOP19 | Define Standard Value Key | 102003 | PP-BD-RTG | PP-BD-RTG-2CL |
| SAP_CA_BC_IC_LND_PP_MFGMD_PC | Manufacturing Master Data - Configuration | S_ALR_87004163 | S_ALR_87004163_TRAN | SIMG_CFMENUOLPSOP74 | Define PRT group key | 103722 | PP-BD-RTG | PP-BD-RTG-2CL |
| SAP_CA_BC_IC_LND_PP_MFGMD_PC | Manufacturing Master Data - Configuration | S_ER1_70000751 | S_ER1_70000751_TRAN | SIMG_PPH_CUST_FORM | Mapping Custom Tasklist Operation Fields to Work Center Formula Parameters | 106627 | PP-BD-RTG | PP-BD-WKC-2CL |
| SAP_CA_BC_IC_LND_PP_MFGMD_PC | Manufacturing Master Data - Configuration | S_ALR_87004142 | S_ALR_87004142_TRAN | SIMG_CFMENUOLPSOP72 | Define PRT control keys | 103762 | PP-BD-RTG | PP-BD-RTG-2CL |
| SAP_CA_BC_IC_LND_PP_MFGMD_PC | Manufacturing Master Data - Configuration | S_ER9_52004046 | S_ER9_52004046_TRAN | OLPS_V_MKALINCONSTCY | Define Inconsistency checks for Production Versions | 106225 | PP-BD-RTG | PP-PI-MD-PRV-2CL |
| SAP_CA_BC_IC_LND_PP_MFGMD_PC | Manufacturing Master Data - Configuration | S_ER9_52003787 | S_ER9_52003787_TRAN | OLPS_PRODNVRECMDRULE | Define Rules for Production Version Proposals | 105965 | PP-BD-RTG | PP-PI-MD-PRV-2CL |
| SAP_CA_BC_IC_LND_PP_MFGMD_PC | Manufacturing Master Data - Configuration | S_ALR_87004178 | S_ALR_87004178_TRAN | SIMG_CFMENUOLPSOP80 | Define PRT status | 103723 | PP-BD-RTG | PP-BD-RTG-2CL |
| SAP_CA_BC_IC_LND_PP_MFGMD_PC | Manufacturing Master Data - Configuration | S_ALR_87004610 | S_ALR_87004610_TRAN | SIMG_CFMENUOLPSOP34 | Determine Capacity Planner | 107245 | PP-BD-RTG | PP-BD-RTG-2CL |
| SAP_CA_BC_IC_LND_FIN_FICAS_PC | Contract Accounting for Sales - Configuration | S_ER1_70000060 | S_ER1_70000060_TRAN | _FICAPV_FPN_VT | Define Number Range | 102680 | FI-CA | FI-CA-2CL |
| SAP_CA_BC_IC_LND_FIN_FICAS_PC | Contract Accounting for Sales - Configuration | S_ER1_70000059 | S_ER1_70000059_TRAN | _FICAPV_FQ0500 | Define Specifications for Derivation of Standard Account Assignment | 102679 | FI-CA | FI-CA-2CL |
| SAP_CA_BC_IC_LND_FIN_FICAS_PC | Contract Accounting for Sales - Configuration | FQ0500 |  | _FICAPV_FQ0500 | Define Specifications for Derivation of Standard Account Assignment | 102679 | FI-CA | FI-CA-2CL |
| SAP_CA_BC_IC_LND_FIN_FICAS_PC | Contract Accounting for Sales - Configuration | FPN_VT | FPN_VT_TRAN | _FICAPV_FPN_VT | Define Number Range | 102680 | FI-CA | FI-CA-2CL |
| SAP_CA_BC_IC_LND_FIN_FICAS_PC | Contract Accounting for Sales - Configuration | S_ER1_70000288 | S_ER1_70000288_TRAN | _FICAPV_VTFKVTSENDER | Configure Sender | 103965 | FI-CA | FI-CA-2CL |
| SAP_CA_BC_IC_LND_FIN_BS0_PC | Bank Statements - Configuration | S_ER9_11000654 | S_ER9_11000654_TRAN | IDFI_T028G_S_V | Define Search Priorities | 101280 | FI-LOC-IAM | FI-AP-AP-B1 |
| SAP_CA_BC_IC_LND_FIN_BS0_PC | Bank Statements - Configuration | S_ER9_11000371 | S_ER9_11000371_TRAN | IDFIPAYM_EOB_V | Assign External Transaction to Payment Symbols | 103103 | FI-LOC-IAM | FI-AP-AP-B1 |
| SAP_CA_BC_IC_LND_FIN_BS0_PC | Bank Statements - Configuration | S_ER9_11001425 | S_ER9_11001425_TRAN | IDFI_MT940_C | Map Data for MT940 Bank Statement Import | 103349 | FI-LOC-IAM | FI-AP-AP-B1 |
| SAP_CA_BC_IC_LND_FIN_SR_TR_PC | Statutory Reporting for Turkey - Configuration | S_ER9_11001217 | S_ER9_11001217_TRAN | FITRV_ELPYMT_MAP_TR | Assign SAP Document Type to E-Ledger Payment Method | 103081 | FI-LOC-FI-TR | FI-LOC-FI-TR |
| SAP_CA_BC_IC_LND_FIN_SR_TR_PC | Statutory Reporting for Turkey - Configuration | S_ER9_11001216 | S_ER9_11001216_TRAN | FITRV_ELPAYMTHD_TR | Specify the E-Ledger Payment Method | 103080 | FI-LOC-FI-TR | FI-LOC-FI-TR |
| SAP_CA_BC_IC_LND_FIN_SR_TR_PC | Statutory Reporting for Turkey - Configuration | S_ER9_11000573 | S_ER9_11000573_TRAN | FITRV_LIMIT | Set Threshold Limit for Ba/Bs Reporting | 102684 | FI-LOC-FI-TR | FI-LOC-FI-TR |
| SAP_CA_BC_IC_LND_FIN_SR_TR_PC | Statutory Reporting for Turkey - Configuration | S_ER9_11001202 | S_ER9_11001202_TRAN | FIGNV_DOCTYP_MAP_TR | Assign SAP Document Type to External Document Type | 103078 | FI-LOC-FI-TR | FI-LOC-FI-CA |
| SAP_CA_BC_IC_LND_FIN_SR_TR_PC | Statutory Reporting for Turkey - Configuration | S_ER9_11001201 | S_ER9_11001201_TRAN | FIGNV_EXTDOCTYP_TR | Specify the External Document Type | 103077 | FI-LOC-FI-TR | FI-LOC-FI-CA |
| SAP_CA_BC_IC_LND_FIN_SR_TR_PC | Statutory Reporting for Turkey - Configuration | S_ER9_11001203 | S_ER9_11001203_TRAN | FITRV_ELGLACTDES_TR | Maintain the General Ledger Account Description | 103079 | FI-LOC-FI-TR | FI-LOC-FI-CA |
| SAP_CA_BC_IC_LND_FIN_SR_TR_PC | Statutory Reporting for Turkey - Configuration | S_ER9_11000572 | S_ER9_11000572_TRAN | FITRV_CONF_KTOSL | Configure Transaction Keys for Ba/Bs Reporting | 102685 | FI-LOC-FI-TR | FI-LOC-FI-TR |
| SAP_CA_BC_IC_LND_FIN_SR_TR_PC | Statutory Reporting for Turkey - Configuration | S_ER9_11002682 | S_ER9_11002682_TRAN | FITRVC_OFFS_VER_D_CE | Define Offsetting Account Determination Versions for Turkey | 106366 | FI-LOC-FI-TR | FI-LOC-CF-TR |
| SAP_CA_BC_IC_LND_FIN_SR_TR_PC | Statutory Reporting for Turkey - Configuration | S_ER9_11001218 | S_ER9_11001218_TRAN | FITRV_INIT_SEQNO_TR | Maintain Initial Sequence Number | 103082 | FI-LOC-FI-TR | FI-LOC-FI-TR |
| SAP_CA_BC_IC_LND_FIN_SR_TR_PC | Statutory Reporting for Turkey - Configuration | S_ER9_11002680 | S_ER9_11002680_TRAN | FITRVC_CF_VERS_DRC | Define Cash Flow Statement Versions for Turkey | 106367 | FI-LOC-FI-TR | FI-LOC-CF-TR |
| SAP_CA_BC_IC_LND_FIN_SR_TR_PC | Statutory Reporting for Turkey - Configuration | S_ER9_11002335 | S_ER9_11002335_TRAN | FIVC_OFFS_GROUP_DRC | Define Field Sets for Grouping for Several Countries/Regions | 105762 | FI-LOC-FI-TR | FI-LOC-CF |
| SAP_CA_BC_IC_LND_FIN_SR_TR_PC | Statutory Reporting for Turkey - Configuration | S_ER9_11002017 | S_ER9_11002017_TRAN | FIVC_OFFS_DET_ACR | Activate Online Offsetting Account Determination for Several Countries/Rgns | 105333 | FI-LOC-FI-TR | FI-LOC-CF |
| SAP_CA_BC_IC_LND_FIN_SR_LU_PC | Statutory Reporting for Luxembourg - Configuration | S_ER9_11001900 | S_ER9_11001900_TRAN | SAFT_LUV_GENERIC | Specify Generic Settings | 104353 | FI-LOC-FI-LU | FI-LOC-FI-BE |
| SAP_CA_BC_IC_LND_FIN_SR_LU_PC | Statutory Reporting for Luxembourg - Configuration | S_ER9_11002116 | S_ER9_11002116_TRAN | FILUV_SP_GL_TAX | Enable Tax Reporting in Special G/L Indicator Line | 105503 | FI-LOC-FI-LU | FI-LOC-FI-BE |
| SAP_CA_BC_IC_LND_FIN_SR_LU_PC | Statutory Reporting for Luxembourg - Configuration | S_ER9_11000673 | S_ER9_11000673_TRAN | FILU_PCNACC | Assign PCN Codes to Accounts | 101991 | FI-LOC-FI-LU | FI-LOC-FI-BE |
| SAP_CA_BC_IC_LND_FIN_SA2_PC | Service Orders and Contracts - Configuration | S_ER9_11001027 | S_ER9_11001027_TRAN | FCOV_SRVPRD_ACTY | Assign Activity Type to Service Product | 102920 | CO-PA | CO-PC-OBJ-SRV |
| SAP_CA_BC_IC_LND_FIN_SA2_PC | Service Orders and Contracts - Configuration | S_ER9_11001107 | S_ER9_11001107_TRAN | FINS_TRR_DRK_CRM | Derivation of Recognition Key for Service Documents | 102968 | CO-PA | CO-PC-OBJ-EBR-2CL |
| SAP_CA_BC_IC_LND_FIN_SA2_PC | Service Orders and Contracts - Configuration | S_ER9_11001028 | S_ER9_11001028_TRAN | FCOV_EXPPRD_ACCT | Assign G/L Accounts to Expense Product | 102921 | CO-PA | CO-PC-OBJ-SRV |
| SAP_CA_BC_IC_LND_CONSENT_PC | Consent Administration - Configuration | S_ER9_68000459 | S_ER9_68000459_TRAN | CMVC_DC | Define Data Controllers | 103536 | CA-GTF-CON | CA-GTF-CON |
| SAP_CA_BC_IC_LND_FIN_WT_KR_PC | Statutory Reporting WT for South Korea - Configuration | S_EB5_05000022 | S_EB5_05000022_TRAN | J_KR_T059C | Create Recipient Types | 107058 | FI-LOC-FI-KR | FI-LOC-FI-KR |
| SAP_CA_BC_IC_LND_FIN_WT_KR_PC | Statutory Reporting WT for South Korea - Configuration | S_ALR_87003260 | S_ALR_87003260_TRAN | SIMG_ORFB_V_TAXOFF | Define Tax Offices | 103551 | FI-LOC-FI-KR | FI-AR-AR-2CL |
| SAP_CA_BC_IC_LND_FIN_WT_KR_PC | Statutory Reporting WT for South Korea - Configuration | S_ALR_87003258 | S_ALR_87003258_TRAN | SIMG_ORFB_V_RGOFFICE | Define Regional Tax Offices | 103552 | FI-LOC-FI-KR | FI-AR-AR-2CL |
| SAP_CA_BC_IC_LND_FIN_WT_KR_PC | Statutory Reporting WT for South Korea - Configuration | S_ALR_87003254 | S_ALR_87003254_TRAN | SIMG_ORFB_V_SECCODE | Define Section Codes | 103553 | FI-LOC-FI-KR | FI-AR-AR-2CL |
| SAP_CA_BC_IC_LND_SLL_TRC_PC | International Trade Compliance - Configuration | /SAPSLL/52000650 | SAPSLL_52000650_TRAN | /SAPSLL/DEFLICENTYPE | Define License Types | 101156 | FT-ITR-TRC | FT-ITR-TRC |
| SAP_CA_BC_IC_LND_SLL_TRC_PC | International Trade Compliance - Configuration | /SAPSLL/52000758 | SAPSLL_52000758_TRAN | /SAPSLL/V_ALRLCC | Activate Legal Regulations for Legal Control | 101154 | FT-ITR-TRC | FT-ITR-TRC |
| SAP_CA_BC_IC_LND_SLL_TRC_PC | International Trade Compliance - Configuration | /SAPSLL/52000649 | SAPSLL_52000649_TRAN | /SAPSLL/CONTLEGALREG | Control Settings for Legal Regulations for Legal Control | 101155 | FT-ITR-TRC | FT-ITR-TRC |
| SAP_CA_BC_IC_LND_SLL_TRC_PC | International Trade Compliance - Configuration | /SAPSLL/52000848 | SAPSLL_52000848_TRAN | /SAPSLL/CONTLEGEMB | Control Settings for Legal Regulations for Embargo | 101812 | FT-ITR-TRC | FT-ITR-TRC |
| SAP_CA_BC_IC_LND_SLL_TRC_PC | International Trade Compliance - Configuration | /SAPSLL/52000847 | SAPSLL_52000847_TRAN | /SAPSLL/ACTLEGREGEMB | Activate Legal Regulations for Embargo | 101813 | FT-ITR-TRC | FT-ITR-TRC |
| SAP_CA_BC_IC_LND_RFM_MDMC_PC | Merchandise Category - Configuration | S_ER9_52002862 | S_ER9_52002862_TRAN | RFM_V_CHAR_CUST | Display Generic Characteristics Type | 105694 | LO-RFM | LO-RFM-CA-CV-2CL |
| SAP_CA_BC_IC_LND_RFM_MDMC_PC | Merchandise Category - Configuration | RFM_V_CHAR_CUST |  | RFM_V_CHAR_CUST | Display Generic Characteristics Type | 105694 | LO-RFM | LO-RFM-CA-CV-2CL |
| SAP_CA_BC_IC_LND_RFM_MDMC_PC | Merchandise Category - Configuration | V_WRFT_CUSTFLD |  | WRF_CHAR_VAL_GRP_001 | Edit Headers for Each Characteristic Type | 105444 | LO-RFM | LO-RFM-CA-CV-2CL |
| SAP_CA_BC_IC_LND_RFM_MDMC_PC | Merchandise Category - Configuration | S_XB4_60000136 | S_XB4_60000136_TRAN | WRF_CHAR_VAL_GRP_001 | Edit Headers for Each Characteristic Type | 105444 | LO-RFM | LO-RFM-CA-CV-2CL |
| SAP_CA_BC_IC_LND_S4CRM_SM0_PC | Service Management - Configuration | S_ER1_83000154 | S_ER1_83000154_TRAN | CRM_ACT_ATP_CHK_SRV | Activate ATP Check for Service Parts | 105358 | CRM-S4-SRV-SVO | CRM-BF-2CL |
| SAP_CA_BC_IC_LND_S4CRM_SM0_PC | Service Management - Configuration | S_ER1_83000123 | S_ER1_83000123_TRAN | CRMS4_DEFREJCTPRFL | Define Rejection Profiles for Service Transactions | 104069 | CRM-S4-SRV-SVO | CRM-BF-2CL |
| SAP_CA_BC_IC_LND_S4CRM_SM0_PC | Service Management - Configuration | S_ER1_83000124 | S_ER1_83000124_TRAN | CRMS4_ASSGNREJCTPRFL | Assign Rejection Profiles to Service Transactions | 104070 | CRM-S4-SRV-SVO | CRM-BF-2CL |
| SAP_CA_BC_IC_LND_S4CRM_SM0_PC | Service Management - Configuration | S_ER1_83000164 | S_ER1_83000164_TRAN | CRM_SRV_LIF_STS_RES | Define Lifecycle Status for Reservation Creation in Service Transaction | 105671 | CRM-S4-SRV-SVO | CRM-BF-2CL |
| SAP_CA_BC_IC_LND_S4CRM_SM0_PC | Service Management - Configuration | S_ER1_83000169 | S_ER1_83000169_TRAN | CRM_SRVPROC_ACCTIND2 | Define Accounting Indicators for Service | 105957 | CRM-S4-SRV-SVO | CRM-BTX-SVO-2CL |
| SAP_CA_BC_IC_LND_FIN_AA_JP_PC | Asset Accounting for Japan - Configuration | S_PRN_53000403 | S_PRN_53000403_TRAN | PTR_013 | Enter Migration Status | 102026 | FI-LOC-FI-JP | FI-LOC-AA-JP |
| SAP_CA_BC_IC_LND_FIN_AA_JP_PC | Asset Accounting for Japan - Configuration | S_PRN_53000349 | S_PRN_53000349_TRAN | PTR_011 | Enter Additional Depreciation Rates | 102028 | FI-LOC-FI-JP | FI-LOC-AA-JP |
| SAP_CA_BC_IC_LND_FIN_AA_JP_PC | Asset Accounting for Japan - Configuration | S_ER9_11001041 | S_ER9_11001041_TRAN | FAA_GLOFAA_JPAX160 | Determine Additional Attributes for Asset Classes | 102884 | FI-LOC-FI-JP | FI-LOC-AA-JP |
| SAP_CA_BC_IC_LND_FIN_AA_JP_PC | Asset Accounting for Japan - Configuration | S_ER9_11001040 | S_ER9_11001040_TRAN | FAA_GLOFAA_JPTSI0 | Define Default Values for Type-Structure-Item Combinations | 102885 | FI-LOC-FI-JP | FI-LOC-AA-JP |
| SAP_CA_BC_IC_LND_FIN_AA_JP_PC | Asset Accounting for Japan - Configuration | S_AER_95000498 | S_AER_95000498_TRAN | PTR_010 | Assign Declaration Key to Company Code and City Code | 102025 | FI-LOC-FI-JP | FI-LOC-AA-JP |
| SAP_CA_BC_IC_LND_FIN_AA_JP_PC | Asset Accounting for Japan - Configuration | S_ER9_11001039 | S_ER9_11001039_TRAN | FAA_GLOFAA_JPTAX | Make Settings for Property Tax Report | 102886 | FI-LOC-FI-JP | FI-LOC-AA-JP |
| SAP_CA_BC_IC_LND_FIN_AA_JP_PC | Asset Accounting for Japan - Configuration | S_EE5_50000361 | S_EE5_50000361_TRAN | PTR_14 | Round off Taxable Amounts for Tax Office | 102027 | FI-LOC-FI-JP | FI-LOC-AA-JP |
| SAP_CA_BC_IC_LND_FIN_AA_JP_PC | Asset Accounting for Japan - Configuration | S_EEI_11000022 | S_EEI_11000022_TRAN | FIAAJPV_UNDEPR | Specify Transaction Types for Unplanned Depreciation | 102347 | FI-LOC-FI-JP | FI-LOC-AA-JP |
| SAP_CA_BC_IC_LND_FIN_AA_JP_PC | Asset Accounting for Japan - Configuration | S_AER_95000497 | S_AER_95000497_TRAN | PTR_009 | Assign Declaration Key to Company Code | 102024 | FI-LOC-FI-JP | FI-LOC-AA-JP |
| SAP_CA_BC_IC_LND_FIN_AA_JP_PC | Asset Accounting for Japan - Configuration | S_AER_95000495 | S_AER_95000495_TRAN | PTR_008 | Enter City-Code-Dependent Data | 102023 | FI-LOC-FI-JP | FI-LOC-AA-JP |
| SAP_CA_BC_IC_LND_FIN_AA_JP_PC | Asset Accounting for Japan - Configuration | S_AER_95000484 | S_AER_95000484_TRAN | PTR_007 | Define Declaration Key | 102022 | FI-LOC-FI-JP | FI-LOC-AA-JP |
| SAP_CA_BC_IC_LND_FIN_AA_JP_PC | Asset Accounting for Japan - Configuration | S_AER_95000285 | S_AER_95000285_TRAN | FIAA_ANNEX16_STRCITM | Define Type-Structure-Item Combinations | 102342 | FI-LOC-FI-JP | FI-LOC-AA-JP |
| SAP_CA_BC_IC_LND_FIN_AA_JP_PC | Asset Accounting for Japan - Configuration | S_AER_95000283 | S_AER_95000283_TRAN | FIAA_ANNEX16_ASSTRUC | Create Asset Structures | 102340 | FI-LOC-FI-JP | FI-LOC-AA-JP |
| SAP_CA_BC_IC_LND_FIN_AA_JP_PC | Asset Accounting for Japan - Configuration | S_ER9_11001381 | S_ER9_11001381_TRAN | V_GLOFAA_JPCITY | Define City Codes | 103327 | FI-LOC-FI-JP | FI-LOC-AA-JP |
| SAP_CA_BC_IC_LND_FIN_AA_JP_PC | Asset Accounting for Japan - Configuration | S_ER9_11001383 | S_ER9_11001383_TRAN | V_GLOFAA_JPSDR | Enter Special Depreciation Rates | 103328 | FI-LOC-FI-JP | FI-LOC-AA-JP |
| SAP_CA_BC_IC_LND_FIN_AA_JP_PC | Asset Accounting for Japan - Configuration | GLOFAA_JPNAD0 |  | V_GLOFAA_JPNAD0 | Define New Additional Depreciation Solution for Annex 16-1 and 16-2 | 105872 | FI-LOC-FI-JP | FI-LOC-AA-JP |
| SAP_CA_BC_IC_LND_FIN_AA_JP_PC | Asset Accounting for Japan - Configuration | S_AER_95000282 | S_AER_95000282_TRAN | FIAA_ANNEX16_ASSITEM | Create Asset Items | 102341 | FI-LOC-FI-JP | FI-LOC-AA-JP |
| SAP_CA_BC_IC_LND_FIN_AA_JP_PC | Asset Accounting for Japan - Configuration | S_ER9_11001702 | S_ER9_11001702_TRAN | V_GLOFAA_JPGVTMV | Define GLO Valuation View Type with Memo Value 1 JPY | 103738 | FI-LOC-FI-JP | FI-LOC-AA-JP |
| SAP_CA_BC_IC_LND_FIN_AA_JP_PC | Asset Accounting for Japan - Configuration | S_ER9_11002424 | S_ER9_11002424_TRAN | V_GLOFAA_JPNAD0 | Define New Additional Depreciation Solution for Annex 16-1 and 16-2 | 105872 | FI-LOC-FI-JP | FI-LOC-AA-JP |
| SAP_CA_BC_IC_LND_FIN_AA_JP_PC | Asset Accounting for Japan - Configuration | S_ER9_11002080 | S_ER9_11002080_TRAN | JP_PTX_CTCODE | Define City Code Without Adjusted Additional Depreciation Rates | 105586 | FI-LOC-FI-JP | FI-LOC-AA-JP |
| SAP_CA_BC_IC_LND_FIN_AA_JP_PC | Asset Accounting for Japan - Configuration | GLOFAA_JPLNDLAW |  | GLOFAAC_JPLNDLAW | Specify Asset Classes for Land Law | 107036 | FI-LOC-FI-JP | FI-LOC-AA-JP |
| SAP_CA_BC_IC_LND_FIN_AA_JP_PC | Asset Accounting for Japan - Configuration | S_ER1_70001524 | S_ER1_70001524_TRAN | GLOFAAC_JPLNDLAW | Specify Asset Classes for Land Law | 107036 | FI-LOC-FI-JP | FI-LOC-AA-JP |
| SAP_CA_BC_IC_LND_FIN_AA_JP_PC | Asset Accounting for Japan - Configuration | GLOFAA_JPPRFMTH |  | V_GLOFAAC_JPPRFM | Assign Changeover Method to Depreciation Profile | 107362 | FI-LOC-FI-JP | FI-LOC-AA-JP |
| SAP_CA_BC_IC_LND_FIN_AA_JP_PC | Asset Accounting for Japan - Configuration | S_ER1_70001898 | S_ER1_70001898_TRAN | V_GLOFAAC_JPPRFM | Assign Changeover Method to Depreciation Profile | 107362 | FI-LOC-FI-JP | FI-LOC-AA-JP |
| SAP_CA_BC_IC_LND_FIN_CR0_PC | Credit Management - Configuration | S_ER9_11000391 | S_ER9_11000391_TRAN | V_UKM_IS_ACTIVE | Deactivate SAP Credit Management | 101015 | FIN-FSCM-CR | FIN-FSCM-CR-2CL |
| SAP_CA_BC_IC_LND_FIN_CR0_PC | Credit Management - Configuration | OVA8 |  | SIMG_CFMENUOLSDOVA8 | Define Automatic Credit Control | 101518 | FIN-FSCM-CR | SD-BF-CM-2CL |
| SAP_CA_BC_IC_LND_FIN_CR0_PC | Credit Management - Configuration | S_ALR_87007379 | S_ALR_87007379_TRAN | SIMG_CFMENUSAPCOB38 | Assign Company Codes to Credit Segments | 102255 | FIN-FSCM-CR | FIN-FSCM-CR-2CL |
| SAP_CA_BC_IC_LND_FIN_CR0_PC | Credit Management - Configuration | S_ALR_87007469 | S_ALR_87007469_TRAN | SIMG_CFMENUSAPOVFL | Assign Sales Area to Credit Segment | 101508 | FIN-FSCM-CR | SD-BF-CM-2CL |
| SAP_CA_BC_IC_LND_FIN_CR0_PC | Credit Management - Configuration | S_P99_41000113 | S_P99_41000113_TRAN | SIMG_CFMENUOLSDOVA7 | Determine Active Receivables Per Item Category | 102571 | FIN-FSCM-CR | SD-BF-CM-2CL |
| SAP_CA_BC_IC_LND_FIN_CR0_PC | Credit Management - Configuration | S_ALR_87006111 | S_ALR_87006111_TRAN | SIMG_CFMENUOLSDOVA8 | Define Automatic Credit Control | 101518 | FIN-FSCM-CR | SD-BF-CM-2CL |
| SAP_CA_BC_IC_LND_FIN_CR0_PC | Credit Management - Configuration | S_SE3_50000109 | S_SE3_50000109_TRAN | FIN_CR_RATING_PROC | Define Rating Procedure | 103463 | FIN-FSCM-CR | FIN-FSCM-CR-2CL |
| SAP_CA_BC_IC_LND_FIN_CR0_PC | Credit Management - Configuration | OVA7 |  | SIMG_CFMENUOLSDOVA7 | Determine Active Receivables Per Item Category | 102571 | FIN-FSCM-CR | SD-BF-CM-2CL |
| SAP_CA_BC_IC_LND_FIN_CR0_PC | Credit Management - Configuration | OVA6 |  | SIMG_CFMENUOLSDOVA6 | Define Credit Groups | 102570 | FIN-FSCM-CR | SD-BF-CM-2CL |
| SAP_CA_BC_IC_LND_FIN_CR0_PC | Credit Management - Configuration | S_ER9_11001096 | S_ER9_11001096_TRAN | UKM_ATTRCATEGO | Create Values for "Category" Attribute in Credit Management | 102828 | FIN-FSCM-CR | FIN-FSCM-CR-2CL |
| SAP_CA_BC_IC_LND_FIN_CR0_PC | Credit Management - Configuration | S_ER9_11001097 | S_ER9_11001097_TRAN | UKM_ATTRREASON | Create Values for "Reason" Attribute in Credit Management | 102829 | FIN-FSCM-CR | FIN-FSCM-CR-2CL |
| SAP_CA_BC_IC_LND_FIN_CR0_PC | Credit Management - Configuration | S_ALR_87006194 | S_ALR_87006194_TRAN | SIMG_CFMENUOLSDOVA6 | Define Credit Groups | 102570 | FIN-FSCM-CR | SD-BF-CM-2CL |
| SAP_CA_BC_IC_LND_FIN_CR0_PC | Credit Management - Configuration | S_SE3_50000108 | S_SE3_50000108_TRAN | FIN_CR_LIMIT_RULE | Create Rule for Scoring and Credit Limit Calculation | 103113 | FIN-FSCM-CR | FIN-FSCM-CR-2CL |
| SAP_CA_BC_IC_LND_FIN_CR0_PC | Credit Management - Configuration | S_SE3_50000106 | S_SE3_50000106_TRAN | FIN_CR_CREDIT_SGM | Create Credit Segments | 102104 | FIN-FSCM-CR | FIN-FSCM-CR-2CL |
| SAP_CA_BC_IC_LND_FIN_CR0_PC | Credit Management - Configuration | S_SE3_50000107 | S_SE3_50000107_TRAN | FIN_CR_EVENT | Define Events and Follow-On Processes | 102279 | FIN-FSCM-CR | FIN-FSCM-CR-2CL |
| SAP_CA_BC_IC_LND_FIN_CR0_PC | Credit Management - Configuration | S_SE3_50000213 | S_SE3_50000213_TRAN | FIN_CR_INFOCAT | Define Info Categories | 102312 | FIN-FSCM-CR | FIN-FSCM-CR-2CL |
| SAP_CA_BC_IC_LND_FIN_CR0_PC | Credit Management - Configuration | S_SE3_50000110 | S_SE3_50000110_TRAN | FIN_CR_RISK_CLASS | Create Risk Classes | 102105 | FIN-FSCM-CR | FIN-FSCM-CR-2CL |
| SAP_CA_BC_IC_LND_FIN_CR0_PC | Credit Management - Configuration | S_SE3_50000119 | S_SE3_50000119_TRAN | FIN_CR_FORMULAS | Define Formulas | 103112 | FIN-FSCM-CR | FIN-FSCM-CR-2CL |
| SAP_CA_BC_IC_LND_FIN_CR0_PC | Credit Management - Configuration | S_SE3_50000198 | S_SE3_50000198_TRAN | FIN_CR_CUST_GRP | Define Customer Credit Group | 101850 | FIN-FSCM-CR | FIN-FSCM-CR-2CL |
| SAP_CA_BC_IC_LND_FIN_CR0_PC | Credit Management - Configuration | S_SE3_50000203 | S_SE3_50000203_TRAN | FIN_CR_BL_REASON | Define Blocking Reasons | 101014 | FIN-FSCM-CR | FIN-FSCM-CR-2CL |
| SAP_CA_BC_IC_LND_FIN_CR0_PC | Credit Management - Configuration | S_SE3_50000204 | S_SE3_50000204_TRAN | FIN_CR_CHECK_RULE | Define Checking Rules | 102623 | FIN-FSCM-CR | FIN-FSCM-CR-2CL |
| SAP_CA_BC_IC_LND_FIN_CR0_PC | Credit Management - Configuration | S_ER1_70001154 | S_ER1_70001154_TRAN | SIMG_CFMENUOLSDOVAK0 | Set Credit Limit Checks for Sales Document Types | 102137 | FIN-FSCM-CR | SD-BF-CM-2CL |
| SAP_CA_BC_IC_LND_FIN_CR0_PC | Credit Management - Configuration | S_ER1_70001129 | S_ER1_70001129_TRAN | V_UKM_DCD_CAT | Create Categories for Documented Credit Decisions | 106899 | FIN-FSCM-CR | FIN-FSCM-CR-2CL |
| SAP_CA_BC_IC_LND_FIN_CR0_PC | Credit Management - Configuration | S_ER1_70001213 | S_ER1_70001213_TRAN | SIMG_CFMENUOLSDOVAD1 | Set Credit Limit Checks for Delivery Types | 101707 | FIN-FSCM-CR | SD-BF-CM-2CL |
| SAP_CA_BC_IC_LND_FIN_CR0_PC | Credit Management - Configuration | OVAK |  | SIMG_CFMENUOLSDOVAK0 | Set Credit Limit Checks for Sales Document Types | 102137 | FIN-FSCM-CR | SD-BF-CM-2CL |
| SAP_CA_BC_IC_LND_FIN_CR0_PC | Credit Management - Configuration | OVAD |  | SIMG_CFMENUOLSDOVAD1 | Set Credit Limit Checks for Delivery Types | 101707 | FIN-FSCM-CR | SD-BF-CM-2CL |
| SAP_CA_BC_IC_LND_FIN_CR0_PC | Credit Management - Configuration | V_UKM_DCD_CAT |  | V_UKM_DCD_CAT | Create Categories for Documented Credit Decisions | 106899 | FIN-FSCM-CR | FIN-FSCM-CR-2CL |
| SAP_CA_BC_IC_LND_FIN_CR0_PC | Credit Management - Configuration | S_ER1_70001128 | S_ER1_70001128_TRAN | V_UKM_DCDREASON | Create Reasons for Documented Credit Decisions | 106900 | FIN-FSCM-CR | FIN-FSCM-CR-2CL |
| SAP_CA_BC_IC_LND_FIN_CR0_PC | Credit Management - Configuration | V_UKM_DCDREASON |  | V_UKM_DCDREASON | Create Reasons for Documented Credit Decisions | 106900 | FIN-FSCM-CR | FIN-FSCM-CR-2CL |
| SAP_CA_BC_IC_LND_FIN_CR0_PC | Credit Management - Configuration | V_UKM_DCD_APR_BH |  | V_UKM_DCD_APR_BH | Maintain Influence of Parameters on Approval Level of DCDs | 107035 | FIN-FSCM-CR | FIN-FSCM-CR-2CL |
| SAP_CA_BC_IC_LND_FIN_CR0_PC | Credit Management - Configuration | S_ER1_70001525 | S_ER1_70001525_TRAN | V_UKM_DCD_APR_BH | Maintain Influence of Parameters on Approval Level of DCDs | 107035 | FIN-FSCM-CR | FIN-FSCM-CR-2CL |
| SAP_CA_BC_IC_LND_FIN_CR0_PC | Credit Management - Configuration | S_ER9_11002422 | S_ER9_11002422_TRAN | UKM_FMLA_PARAMETER | Maintain Formula Parameters | 107110 | FIN-FSCM-CR | FIN-FSCM-CR-2CL |
| SAP_CA_BC_IC_LND_FIN_AA_CZ_PC | Asset Accounting for Czech Republic - Configuration | GLOFAA_CZ_VEH |  | GLOFAA_CZ_VEH | Define Tax Depreciation Limit for Vehicles | 106942 | FI-LOC-FI-CZ | FI-LOC-AA-CZ |
| SAP_CA_BC_IC_LND_FIN_AA_CZ_PC | Asset Accounting for Czech Republic - Configuration | S_ER1_70001327 | S_ER1_70001327_TRAN | GLOFAA_CZ_VEH | Define Tax Depreciation Limit for Vehicles | 106942 | FI-LOC-FI-CZ | FI-LOC-AA-CZ |
| SAP_CA_BC_IC_LND_FIN_AA_CZ_PC | Asset Accounting for Czech Republic - Configuration | S_ER9_11001366 | S_ER9_11001366_TRAN | V_GLOFAACZNCLCOD | Define National Classification Code (Czech Republic) | 103191 | FI-LOC-FI-CZ | FI-LOC-AA-CZ |
| SAP_CORE_BC_BCT_IMG | Implementation Activities - Authorized Activities (Deprecated) | SIMG_ACTIVITY_EXEC | SIMG_ACTIVITY_EXEC_TRAN |  |  |  | BC-CUS-TOL-IMG |  |
| SAP_CORE_BC_BCT_IMG | Implementation Activities - Authorized Activities (Deprecated) | SIMG_ACTIVITY_COMP | SIMG_ACTIVITY_COMP_PC_TRAN |  |  |  | BC-CUS-TOL-IMG |  |
| SAP_CORE_BC_BCT_IMG | Implementation Activities - Authorized Activities (Deprecated) | SIMG_ACTIVITY_DOCU | SIMG_ACTIVITY_DOCU_TRAN |  |  |  | BC-CUS-TOL-IMG |  |
| SAP_CORE_BC_BCT_IMG | Implementation Activities - Authorized Activities (Deprecated) | SIMG | SIMG_PC_TRAN |  |  |  | BC-CUS-TOL-IMG |  |
| SAP_SD_BC_PRICE_CONFIGURE_PC | Sales - Pricing Configuration | F5525 | F5525_TRAN |  |  |  | SD-SLS |  |
| SAP_CA_BC_IC_LND_FIN_SR_IT_PC | Statutory Reporting for Italy - Configuration | S_ER9_11000851 | S_ER9_11000851_TRAN | FIITVR_DOCTYPEV | Assign VAT Registers to Accounting Document Types | 102451 | FI-LOC-FI-IT | FI-LOC-FI-IT |
| SAP_CA_BC_IC_LND_FIN_SR_IT_PC | Statutory Reporting for Italy - Configuration | S_EBJ_45000263 | S_EBJ_45000263_TRAN | FIWTITV_SSI | Assign Withholding Tax Type and Tax Code to Social Security Institution | 101848 | FI-LOC-FI-IT | FI-LOC-FI-IT |
| SAP_CA_BC_IC_LND_FIN_SR_IT_PC | Statutory Reporting for Italy - Configuration | S_EBJ_45000050 | S_EBJ_45000050_TRAN | FIITC_CONFIG | Define Generic Parameters for Company Code | 102644 | FI-LOC-FI-IT | FI-LOC-FI-IT |
| SAP_CA_BC_IC_LND_FIN_SR_IT_PC | Statutory Reporting for Italy - Configuration | S_EBJ_45000262 | S_EBJ_45000262_TRAN | FIWTITV_SSIFCOD | Define Social Security Institution | 101849 | FI-LOC-FI-IT | FI-LOC-FI-IT |
| SAP_CA_BC_IC_LND_FIN_SR_IT_PC | Statutory Reporting for Italy - Configuration | S_E4A_94000037 | S_E4A_94000037_TRAN | T005_IT_UIC | UIC Code for Italy | 104312 | FI-LOC-FI-IT | FI-AP-AP-B-2CL |
| SAP_CA_BC_IC_LND_FIN_SR_IT_PC | Statutory Reporting for Italy - Configuration | S_ER1_70000422 | S_ER1_70000422_TRAN | V_FICA_FI_DOCTYP_IT | Assign Document Type for Transfer to General Ledger | 105940 | FI-LOC-FI-IT | FI-LOC-CA-IT |
| SAP_CA_BC_IC_LND_FIN_SR_IT_PC | Statutory Reporting for Italy - Configuration | S_EBJ_45000049 | S_EBJ_45000049_TRAN | TAXCD_REPR_IT | Maintain Details of Tax Code Representative | 106752 | FI-LOC-FI-IT | FI-LOC-FI-IT |
| SAP_CA_BC_IC_LND_FIN_SR_IT_PC | Statutory Reporting for Italy - Configuration | S_P7D_67000455 | S_P7D_67000455_TRAN | ITFI_V_IDES_SI | Assign Number Range for Self Invoices to Company Code | 106937 | FI-LOC-FI-IT | FI-LOC-FI |
| SAP_CA_BC_IC_LND_FIN_SR_IT_PC | Statutory Reporting for Italy - Configuration | S_ER9_11000852 | S_ER9_11000852_TRAN | FIITVR_TAXCODEV | Assign VAT Registers to Tax Codes | 102452 | FI-LOC-FI-IT | FI-LOC-FI-IT |
| SAP_CA_BC_IC_LND_FIN_SR_RU_PC | Statutory Reporting for Russian Federation - Configuration | S_ER9_11001731 | S_ER9_11001731_TRAN | FIRUVC_TRT_RATE | Define Tax Rates | 103800 | FI-LOC-FI-RU | FI-LOC-FI-RU |
| SAP_CA_BC_IC_LND_FIN_SR_RU_PC | Statutory Reporting for Russian Federation - Configuration | S_ER9_11001252 | S_ER9_11001252_TRAN | FIRUV_TAX_OFFICE | Define Tax Offices | 103307 | FI-LOC-FI-RU | FI-LOC-FI-RU |
| SAP_CA_BC_IC_LND_FIN_SR_RU_PC | Statutory Reporting for Russian Federation - Configuration | S_ER9_11001508 | S_ER9_11001508_TRAN | FIRUVC_TXPST_DET | Define Tax Payable Posting Rules | 103496 | FI-LOC-FI-RU | FI-LOC-FI-RU |
| SAP_CA_BC_IC_LND_FIN_SR_RU_PC | Statutory Reporting for Russian Federation - Configuration | S_ER9_11001730 | S_ER9_11001730_TRAN | FIRUVC_TRT_CNCMNT | Define Tax Concessions | 103799 | FI-LOC-FI-RU | FI-LOC-FI-RU |
| SAP_CA_BC_IC_LND_FIN_SR_RU_PC | Statutory Reporting for Russian Federation - Configuration | S_ER9_11001247 | S_ER9_11001247_TRAN | FIRUV_PRT_STXCT | Define Special Tax Categories | 103309 | FI-LOC-FI-RU | FI-LOC-FI-RU |
| SAP_CA_BC_IC_LND_FIN_SR_RU_PC | Statutory Reporting for Russian Federation - Configuration | S_ER9_11001127 | S_ER9_11001127_TRAN | FIRUVC_PRT_CNCMNT | Define Tax Concessions | 103311 | FI-LOC-FI-RU | FI-LOC-FI-RU |
| SAP_CA_BC_IC_LND_FIN_SR_RU_PC | Statutory Reporting for Russian Federation - Configuration | S_ER9_11001125 | S_ER9_11001125_TRAN | FIRUV_PRT_SBMDCL | Assign Tax Offices | 103308 | FI-LOC-FI-RU | FI-LOC-FI-RU |
| SAP_CA_BC_IC_LND_FIN_SR_RU_PC | Statutory Reporting for Russian Federation - Configuration | S_ER9_11001124 | S_ER9_11001124_TRAN | FIRUV_PRT_TXRATE | Define Tax Rates | 103310 | FI-LOC-FI-RU | FI-LOC-FI-RU |
| SAP_CA_BC_IC_LND_FIN_SR_RU_PC | Statutory Reporting for Russian Federation - Configuration | S_ER9_11000728 | S_ER9_11000728_TRAN | FIRUV_EXT_NUM | Define External Number and Date Filling Rules | 102760 | FI-LOC-FI-RU | FI-LOC-FI-RU |
| SAP_CA_BC_IC_LND_FIN_SR_RU_PC | Statutory Reporting for Russian Federation - Configuration | S_ER9_11000479 | S_ER9_11000479_TRAN | FIRUVC_VATSUBS | Maintain VAT Subscenarios | 102758 | FI-LOC-FI-RU | FI-LOC-FI-RU |
| SAP_CA_BC_IC_LND_FIN_SR_RU_PC | Statutory Reporting for Russian Federation - Configuration | S_ER9_11000478 | S_ER9_11000478_TRAN | FIRUVC_VAT | Maintain VAT Return Versions | 102765 | FI-LOC-FI-RU | FI-LOC-FI-RU |
| SAP_CA_BC_IC_LND_FIN_SR_RU_PC | Statutory Reporting for Russian Federation - Configuration | S_ER9_11001734 | S_ER9_11001734_TRAN | FIRUVC_TXPST_DET_TRT | Define Tax Payable Posting Rules | 103802 | FI-LOC-FI-RU | FI-LOC-FI-RU |
| SAP_CA_BC_IC_LND_FIN_SR_RU_PC | Statutory Reporting for Russian Federation - Configuration | S_ER9_11001929 | S_ER9_11001929_TRAN | FIRUV_RGN_OKTMO | Assign OKTMO Codes to Region Numbers | 105129 | FI-LOC-FI-RU | FI-LOC-FI-RU |
| SAP_CA_BC_IC_LND_FIN_SR_RU_PC | Statutory Reporting for Russian Federation - Configuration | S_ER9_11000364 | S_ER9_11000364_TRAN | J_3RF_REG_ASGNC | Assign Transportation Types | 105990 | FI-LOC-FI-RU | FI-LOC-FI-RU |
| SAP_CA_BC_IC_LND_FIN_SR_RU_PC | Statutory Reporting for Russian Federation - Configuration | S_ER9_11001885 | S_ER9_11001885_TRAN | FIRUD_VATOPCODE | Define Operation Code Relevance | 105991 | FI-LOC-FI-RU | FI-LOC-FI-RU |
| SAP_CA_BC_IC_LND_FIN_SR_RU_PC | Statutory Reporting for Russian Federation - Configuration | S_ER9_11002099 | S_ER9_11002099_TRAN | FICITV_CLSF_CUST | Make Classification Settings for Corporate Income Tax | 105987 | FI-LOC-FI-RU | FI-LOC-CIT |
| SAP_CA_BC_IC_LND_FIN_SR_RU_PC | Statutory Reporting for Russian Federation - Configuration | S_ER9_11002101 | S_ER9_11002101_TRAN | FICITVC_STTLMT | Define Settlement Codes for Corporate Income Tax | 105989 | FI-LOC-FI-RU | FI-LOC-CIT |
| SAP_CA_BC_IC_LND_FIN_SR_RU_PC | Statutory Reporting for Russian Federation - Configuration | S_ER9_11002100 | S_ER9_11002100_TRAN | FICITVC_RPTVERS | Define Report Versions for Corporate Income Tax | 105988 | FI-LOC-FI-RU | FI-LOC-CIT |
| SAP_CA_BC_IC_LND_FIN_SR_RU_PC | Statutory Reporting for Russian Federation - Configuration | S_ER9_11002714 | S_ER9_11002714_TRAN | FIRUVC_UTNP_CSTMZG | Define Versions of Unified Tax Notice and Payment | 106501 | FI-LOC-FI-RU | FI-LOC-FI-RU |
| SAP_CA_BC_IC_LND_FIN_SR_RU_PC | Statutory Reporting for Russian Federation - Configuration | FIRU_PRT_CNCLC |  | J_3RFPOFPRIV | Define Federal Tax Concessions | 107296 | FI-LOC-FI-RU | FI-LOC-FI-RU |
| SAP_CA_BC_IC_LND_FIN_SR_RU_PC | Statutory Reporting for Russian Federation - Configuration | S_PCO_36000318 | S_PCO_36000318_03_TRAN | J_3RFPOFPRIV | Define Federal Tax Concessions | 107296 | FI-LOC-FI-RU | FI-LOC-FI-RU |
| SAP_CA_BC_IC_LND_FIN_SR_RU_PC | Statutory Reporting for Russian Federation - Configuration | FIRU_VATOUTPUT |  | FIRUV_VATOUTPUT | Define VAT Return Version for Output | 107320 | FI-LOC-FI-RU | FI-LOC-FI-RU |
| SAP_CA_BC_IC_LND_FIN_SR_RU_PC | Statutory Reporting for Russian Federation - Configuration | S_ER9_11000642 | S_ER9_11000642_03_TRAN | FIRUV_VATOUTPUT | Define VAT Return Version for Output | 107320 | FI-LOC-FI-RU | FI-LOC-FI-RU |
| SAP_CA_BC_IC_LND_FIN_SR_RU_PC | Statutory Reporting for Russian Federation - Configuration | FIRU_TRT_CNCLC |  | FIRUV_TRT_CNCLC | Define Tax Concession Legal Codes | 107404 | FI-LOC-FI-RU | FI-LOC-FI-RU |
| SAP_CA_BC_IC_LND_FIN_SR_RU_PC | Statutory Reporting for Russian Federation - Configuration | S_ER9_11001735 | S_ER9_11001735_03_TRAN | FIRUV_TRT_CNCLC | Define Tax Concession Legal Codes | 107404 | FI-LOC-FI-RU | FI-LOC-FI-RU |
| SAP_CORE_BC_BCT_TRN_MNG_PC | Business Configuration - Transport Management | F5069 | F5069_03_TRAN |  |  |  | BC-CUS-TOL-CTO |  |
| SAP_CORE_BC_BCT_TRN_MNG_PC | Business Configuration - Transport Management | F7042 | F7042_TRAN |  |  |  | BC-CUS-TOL-CTO |  |
| SAP_CA_BC_IC_LND_EHS_MOC_PC | Management of Change - Configuration | /MOC/VC_CATALOG_SM34 |  | /MOC/VC_CATALOG | Define Catalogs and Code Groups | 104231 | CA-IAM-MOC | CA-IAM-MOC |
| SAP_CA_BC_IC_LND_EHS_MOC_PC | Management of Change - Configuration | /MOC/29000028 | MOC_29000028_TRAN | /MOC/VV_CODE | Define Codes | 104230 | CA-IAM-MOC | CA-IAM-MOC |
| SAP_CA_BC_IC_LND_EHS_MOC_PC | Management of Change - Configuration | /MOC/VC_ISS_SM34 |  | /MOC/VC_ISS | Define Change Request Types | 104461 | CA-IAM-MOC | CA-IAM-MOC |
| SAP_CA_BC_IC_LND_EHS_MOC_PC | Management of Change - Configuration | /MOC/ACT_TEMPLT_SM34 |  | /MOC/VC_ACTTMPLT | Define Activity Templates | 104443 | CA-IAM-MOC | CA-IAM-MOC |
| SAP_CA_BC_IC_LND_EHS_MOC_PC | Management of Change - Configuration | /MOC/29000019 | MOC_29000019_TRAN | /MOC/VC_ACTTMPLT | Define Activity Templates | 104443 | CA-IAM-MOC | CA-IAM-MOC |
| SAP_CA_BC_IC_LND_EHS_MOC_PC | Management of Change - Configuration | /MOC/29000017 | MOC_29000017_TRAN | /MOC/VC_CATALOG | Define Catalogs and Code Groups | 104231 | CA-IAM-MOC | CA-IAM-MOC |
| SAP_CA_BC_IC_LND_EHS_MOC_PC | Management of Change - Configuration | /MOC/29000018 | MOC_29000018_TRAN | /MOC/VC_ISS | Define Change Request Types | 104461 | CA-IAM-MOC | CA-IAM-MOC |
| SAP_CA_BC_IC_LND_EHS_MOC_PC | Management of Change - Configuration | /MOC/VV_CODE_SM30 |  | /MOC/VV_CODE | Define Codes | 104230 | CA-IAM-MOC | CA-IAM-MOC |
| SAP_CA_BC_IC_LND_EHS_MOC_PC | Management of Change - Configuration | /IAM/29000526 | IAM_29000526_TRAN | /IAM/V_BRF_MOC | Define BRFplus Applications and Functions | 107051 | CA-IAM-MOC | CA-IAM-MOC |
| SAP_CA_BC_IC_LND_EHS_MOC_PC | Management of Change - Configuration | /IAM/V_BRF_MOC |  | /IAM/V_BRF_MOC | Define BRFplus Applications and Functions | 107051 | CA-IAM-MOC | CA-IAM-MOC |
| SAP_EAM_BC_OSAM_MNG_PC | EAM - Output Scheduling in Asset Management | F6075 | F6075_TRAN |  |  |  | PM |  |
| SAP_EAM_BC_OSAM_MNG_PC | EAM - Output Scheduling in Asset Management | F6074 | F6074_TRAN |  |  |  | PM |  |
| SAP_EAM_BC_OSAM_MNG_PC | EAM - Output Scheduling in Asset Management | F6076 | F6076_TRAN |  |  |  | PM |  |
| SAP_CA_BC_IC_LND_LE_EWM0_PC | Logistics Execution EWM System Integration - Configuration | /SPE/52001008 | SPE_52001008_TRAN | /SPE/V_T340_SSC | Configure SAP EWM-Specific Parameters | 102212 | LE-SHP-IAM | LE-IEW-X-2CL |
| SAP_CA_BC_IC_LND_LE_EWM0_PC | Logistics Execution EWM System Integration - Configuration | EC22 |  | /SPE/V_T340_SSC | Configure SAP EWM-Specific Parameters | 102212 | LE-SHP-IAM | LE-IEW-X-2CL |
| SAP_CA_BC_IC_LND_FIN_SA3_PC | Sales and Services Projects - Configuration | S_ER9_11000350 | S_ER9_11000350_TRAN | FINS_TRR_DRAKEY | Derivation of Recognition Key for Projects | 102517 | CO-PA | CO-PC-OBJ-EBR-2CL |
| SAP_CA_BC_IC_LND_SCM_ATP0_PC | ATP General Functions - Configuration | S_ER9_52002826 | S_ER9_52002826_TRAN | CA_ATP_ENH_CHK_MTHDS | Configure Enhanced Check Methods by Document Purpose | 105339 | CA-ATP | CA-ATP-2CL |
| SAP_CA_BC_IC_LND_FIN_WT_BR_PC | Statutory Reporting WT for Brazil - Configuration | S_ER1_70001848 | S_ER1_70001848_TRAN | V_T059Z_BR_CE | Assign Withholding Tax Keys to Withholding Tax Codes | 107297 | FI-LOC-FI-BR | FI-LOC-FI-BR-WHT |
| SAP_CA_BC_IC_LND_FIN_WT_BR_PC | Statutory Reporting WT for Brazil - Configuration | V_T059Z_BR |  | V_T059Z_BR_CE | Assign Withholding Tax Keys to Withholding Tax Codes | 107297 | FI-LOC-FI-BR | FI-LOC-FI-BR-WHT |
| SAP_CA_BC_IC_LND_FIN_WT_BR_PC | Statutory Reporting WT for Brazil - Configuration | S_P6D_40000029 | S_P6D_40000029_TRAN | V_T059Z_WITHCD2_BR | Define Official Collection Codes | 105178 | FI-LOC-FI-BR | FI-LOC-LO-BR |
| SAP_CA_BC_IC_LND_FIN_WT_BR_PC | Statutory Reporting WT for Brazil - Configuration | S_EBJ_98000791 | S_EBJ_98000791_TRAN | FIWTBRV_TDS_THR | Define Minimum Threshold Amount | 105179 | FI-LOC-FI-BR | FI-LOC-LO-BR |
| SAP_CA_BC_IC_LND_FIN_CJ1_PC | Cash Journal - System Specific Configuration | FBCJC6 |  | FI_BL_CJ_T_FBCJC6 | Define Number Ranges for Numbering Groups | 103550 | FI-BL | FI-BL-PT-CJ-2CL |
| SAP_CA_BC_IC_LND_FIN_CJ1_PC | Cash Journal - System Specific Configuration | S_EB5_05000344 | S_EB5_05000344_TRAN | FI_BL_CJ_T_FBCJC6 | Define Number Ranges for Numbering Groups | 103550 | FI-BL | FI-BL-PT-CJ-2CL |
| SAP_CA_BC_IC_LND_FIN_SRF_PC | Statutory Reporting - Configuration | S_ER9_52000057 | S_ER9_52000057_TRAN | SRFVC_REP_ENTITY | Setting Up Your Statutory Reporting | 101071 | FI-LOC-IAM | FI-LOC-SRF-DEF |
| SAP_CA_BC_IC_LND_EHS_IM0_PC | EHS Incident Management - Configuration | EHHSSVC_INC_CLOSE |  | EHHSS_INC_TASK | Specify Incident, Near Miss, and Safety Observation Groups | 103393 | EHS-SUS-FND-EHS | EHS-SUS-IM |
| SAP_CA_BC_IC_LND_EHS_IM0_PC | EHS Incident Management - Configuration | S_ER1_70000303 | S_ER1_70000303_TRAN | EHHSS_BGHW_EMPLOYER | Specify Employer Details | 104389 | EHS-SUS-FND-EHS | EHS-SUS-IM |
| SAP_CA_BC_IC_LND_EHS_IM0_PC | EHS Incident Management - Configuration | EHHSSVC_INC_REG |  | EHHSS_INC_REGULATION | Specify Regulations | 103446 | EHS-SUS-FND-EHS | EHS-SUS-IM |
| SAP_CA_BC_IC_LND_EHS_IM0_PC | EHS Incident Management - Configuration | EHHSS_BGHW_EMPL_SM30 |  | EHHSS_BGHW_EMPLOYER | Specify Employer Details | 104389 | EHS-SUS-FND-EHS | EHS-SUS-IM |
| SAP_CA_BC_IC_LND_EHS_IM0_PC | EHS Incident Management - Configuration | S_EH1_32000032 | S_EH1_32000032_TRAN | EHHSS_INC_RCTYPE | Specify Root Cause Types | 103013 | EHS-SUS-FND-EHS | EHS-SUS-IM |
| SAP_CA_BC_IC_LND_EHS_IM0_PC | EHS Incident Management - Configuration | S_ER9_52000965 | S_ER9_52000965_TRAN | EHHSS_INC_TASK | Specify Incident, Near Miss, and Safety Observation Groups | 103393 | EHS-SUS-FND-EHS | EHS-SUS-IM |
| SAP_CA_BC_IC_LND_EHS_IM0_PC | EHS Incident Management - Configuration | EHHSSV_INC_FORMN |  | EHHSS_INC_INC_FRM | Assign Forms to Regulations | 103511 | EHS-SUS-FND-EHS | EHS-SUS-IM |
| SAP_CA_BC_IC_LND_EHS_IM0_PC | EHS Incident Management - Configuration | S_EH1_32000029 | S_EH1_32000029_TRAN | EHHSS_INC_INC_FRM | Assign Forms to Regulations | 103511 | EHS-SUS-FND-EHS | EHS-SUS-IM |
| SAP_CA_BC_IC_LND_EHS_IM0_PC | EHS Incident Management - Configuration | EHHSSVC_RCTYPE |  | EHHSS_INC_RCTYPE | Specify Root Cause Types | 103013 | EHS-SUS-FND-EHS | EHS-SUS-IM |
| SAP_CA_BC_IC_LND_EHS_IM0_PC | EHS Incident Management - Configuration | S_EH1_32000011 | S_EH1_32000011_TRAN | EHHSS_INC_REGULATION | Specify Regulations | 103446 | EHS-SUS-FND-EHS | EHS-SUS-IM |
| SAP_CA_BC_IC_LND_EHS_IM0_PC | EHS Incident Management - Configuration | EHHSSV_INJ_ENTRY |  | EHHSS_INJ_ILL_TYPE | Specify Injury/Illness Log Entry Types | 106643 | EHS-SUS-FND-EHS | EHS-SUS-IM |
| SAP_CA_BC_IC_LND_EHS_IM0_PC | EHS Incident Management - Configuration | S_ER1_70000114 | S_ER1_70000114_TRAN | EHHSS_INJ_ILL_TYPE | Specify Injury/Illness Log Entry Types | 106643 | EHS-SUS-FND-EHS | EHS-SUS-IM |
| SAP_CA_BC_IC_LND_EHS_IM0_PC | EHS Incident Management - Configuration | EHHSSV_OCC_TYP |  | EHHSS_INC_OCC_TYP | Specify Incident Types | 106655 | EHS-SUS-FND-EHS | EHS-SUS-IM |
| SAP_CA_BC_IC_LND_EHS_IM0_PC | EHS Incident Management - Configuration | EHHSSV_PERMOVE |  | EHHSS_INC_PERMOV | Specify Movements of Injured Persons | 106674 | EHS-SUS-FND-EHS | EHS-SUS-IM |
| SAP_CA_BC_IC_LND_EHS_IM0_PC | EHS Incident Management - Configuration | S_EE5_50000056 | S_EE5_50000056_TRAN | EHHSS_INC_OCC_TYP | Specify Incident Types | 106655 | EHS-SUS-FND-EHS | EHS-SUS-IM |
| SAP_CA_BC_IC_LND_EHS_IM0_PC | EHS Incident Management - Configuration | S_ER9_52000983 | S_ER9_52000983_TRAN | EHHSS_INC_GRP_SEV | Specify Incident Severity Levels | 106656 | EHS-SUS-FND-EHS | EHS-SUS-IM |
| SAP_CA_BC_IC_LND_EHS_IM0_PC | EHS Incident Management - Configuration | EHHSSV_GRP_SEV |  | EHHSS_INC_GRP_SEV | Specify Incident Severity Levels | 106656 | EHS-SUS-FND-EHS | EHS-SUS-IM |
| SAP_CA_BC_IC_LND_EHS_IM0_PC | EHS Incident Management - Configuration | EHHSSV_PERACTY |  | EHHSS_INC_PERACTY | Specify Activities of Injured Persons | 106673 | EHS-SUS-FND-EHS | EHS-SUS-IM |
| SAP_CA_BC_IC_LND_EHS_IM0_PC | EHS Incident Management - Configuration | EHHSSV_INJILTP |  | EHHSS_INC_INJILTP | Specify Injury/Illness Types | 106670 | EHS-SUS-FND-EHS | EHS-SUS-IM |
| SAP_CA_BC_IC_LND_EHS_IM0_PC | EHS Incident Management - Configuration | EHHSSV_INJIL |  | EHHSS_INC_INJIL | Specify Injury/Illness Classifications | 106669 | EHS-SUS-FND-EHS | EHS-SUS-IM |
| SAP_CA_BC_IC_LND_EHS_IM0_PC | EHS Incident Management - Configuration | EHHSSV_INCCOBM |  | EHHSS_INC_INCCOBM | Specify Movements of Incident-Causing Objects | 106672 | EHS-SUS-FND-EHS | EHS-SUS-IM |
| SAP_CA_BC_IC_LND_EHS_IM0_PC | EHS Incident Management - Configuration | EHHSSV_INCCOBJ |  | EHHSS_INC_INCCOBJ | Specify Incident-Causing Objects | 106671 | EHS-SUS-FND-EHS | EHS-SUS-IM |
| SAP_CA_BC_IC_LND_EHS_IM0_PC | EHS Incident Management - Configuration | S_EE5_50000063 | S_EE5_50000063_TRAN | EHHSS_INC_INJILTP | Specify Injury/Illness Types | 106670 | EHS-SUS-FND-EHS | EHS-SUS-IM |
| SAP_CA_BC_IC_LND_EHS_IM0_PC | EHS Incident Management - Configuration | S_EE5_50000072 | S_EE5_50000072_TRAN | EHHSS_INC_INCCOBJ | Specify Incident-Causing Objects | 106671 | EHS-SUS-FND-EHS | EHS-SUS-IM |
| SAP_CA_BC_IC_LND_EHS_IM0_PC | EHS Incident Management - Configuration | S_ER1_70001029 | S_ER1_70001029_TRAN | EHHSS_INV_RC | Specify Root Cause Categories | 106804 | EHS-SUS-FND-EHS | EHS-SUS-IM |
| SAP_CA_BC_IC_LND_EHS_IM0_PC | EHS Incident Management - Configuration | S_EE5_50000093 | S_EE5_50000093_TRAN | EHHSS_INC_INCCOBM | Specify Movements of Incident-Causing Objects | 106672 | EHS-SUS-FND-EHS | EHS-SUS-IM |
| SAP_CA_BC_IC_LND_EHS_IM0_PC | EHS Incident Management - Configuration | S_EE5_50000062 | S_EE5_50000062_TRAN | EHHSS_INC_INJIL | Specify Injury/Illness Classifications | 106669 | EHS-SUS-FND-EHS | EHS-SUS-IM |
| SAP_CA_BC_IC_LND_EHS_IM0_PC | EHS Incident Management - Configuration | EHHSSV_INV_TYP |  | EHHSS_INV_TYP | Specify Investigation Types | 106803 | EHS-SUS-FND-EHS | EHS-SUS-IM |
| SAP_CA_BC_IC_LND_EHS_IM0_PC | EHS Incident Management - Configuration | S_ER1_70001040 | S_ER1_70001040_TRAN | EHHSS_INV_EV | Specify Evidence Types | 106805 | EHS-SUS-FND-EHS | EHS-SUS-IM |
| SAP_CA_BC_IC_LND_EHS_IM0_PC | EHS Incident Management - Configuration | S_EE5_50000061 | S_EE5_50000061_TRAN | EHHSS_INC_PERMOV | Specify Movements of Injured Persons | 106674 | EHS-SUS-FND-EHS | EHS-SUS-IM |
| SAP_CA_BC_IC_LND_EHS_IM0_PC | EHS Incident Management - Configuration | EHHSSV_INV_EV |  | EHHSS_INV_EV | Specify Evidence Types | 106805 | EHS-SUS-FND-EHS | EHS-SUS-IM |
| SAP_CA_BC_IC_LND_EHS_IM0_PC | EHS Incident Management - Configuration | EHHSSV_INV_RC |  | EHHSS_INV_RC | Specify Root Cause Categories | 106804 | EHS-SUS-FND-EHS | EHS-SUS-IM |
| SAP_CA_BC_IC_LND_EHS_IM0_PC | EHS Incident Management - Configuration | S_EE5_50000060 | S_EE5_50000060_TRAN | EHHSS_INC_PERACTY | Specify Activities of Injured Persons | 106673 | EHS-SUS-FND-EHS | EHS-SUS-IM |
| SAP_CA_BC_IC_LND_EHS_IM0_PC | EHS Incident Management - Configuration | S_ER1_70001027 | S_ER1_70001027_TRAN | EHHSS_INV_TYP | Specify Investigation Types | 106803 | EHS-SUS-FND-EHS | EHS-SUS-IM |
| SAP_CA_BC_IC_LND_EHS_IM0_PC | EHS Incident Management - Configuration | S_ER1_70001541 | S_ER1_70001541_TRAN | EHHSS_INC_CAT_ICON | Specify Icons for Incident Categories | 107079 | EHS-SUS-FND-EHS | EHS-SUS-IM |
| SAP_CA_BC_IC_LND_EHS_IM0_PC | EHS Incident Management - Configuration | EHHSSV_INC_ICON |  | EHHSS_INC_CAT_ICON | Specify Icons for Incident Categories | 107079 | EHS-SUS-FND-EHS | EHS-SUS-IM |
| SAP_CA_BC_IC_LND_EHS_IM0_PC | EHS Incident Management - Configuration | S_ER1_70001563 | S_ER1_70001563_TRAN | EHHSS_INV_ACT | Specify Investigation Activity Types | 107103 | EHS-SUS-FND-EHS | EHS-SUS-IM |
| SAP_CA_BC_IC_LND_EHS_IM0_PC | EHS Incident Management - Configuration | EHHSSV_INV_ACT |  | EHHSS_INV_ACT | Specify Investigation Activity Types | 107103 | EHS-SUS-FND-EHS | EHS-SUS-IM |
| SAP_CA_BC_IC_LND_LE_PI0_PC | Logistics Execution Picking - Configuration | S_ALR_87006719 | S_ALR_87006719_TRAN | SIMG_CFMENUOLSDVSTK | Define Confirmation Requirements | 101903 | LE-SHP-IAM | LE-SHP-GF-2CL |
| SAP_CA_BC_IC_LND_LE_PI0_PC | Logistics Execution Picking - Configuration | S_ALR_87006718 | S_ALR_87006718_TRAN | SIMG_CFMENUOLSDOVLP | Define Relevant Item Categories | 101902 | LE-SHP-IAM | LE-SHP-GF-2CL |
| SAP_CA_BC_IC_LND_LE_PI0_PC | Logistics Execution Picking - Configuration | S_ALR_87006700 | S_ALR_87006700_TRAN | SIMG_CFMENUOLSDOMS6 | Define Storage Conditions | 102128 | LE-SHP-IAM | LE-SHP-GF-2CL |
| SAP_CA_BC_IC_LND_LE_PI0_PC | Logistics Execution Picking - Configuration | S_ALR_87006689 | S_ALR_87006689_TRAN | SIMG_CFMENUOLSDOVLQ | Define Rules for Picking Location Determination | 101107 | LE-SHP-IAM | LE-SHP-GF-2CL |
| SAP_CA_BC_IC_LND_LE_PI0_PC | Logistics Execution Picking - Configuration | S_ALR_87006701 | S_ALR_87006701_TRAN | SIMG_CFMENUOLSDOVL3 | Assign Picking Locations | 102130 | LE-SHP-IAM | LE-SHP-GF-2CL |
| SAP_CA_BC_IC_LND_LE_PI0_PC | Logistics Execution Picking - Configuration | VSTK |  | SIMG_CFMENUOLSDVSTK | Define Confirmation Requirements | 101903 | LE-SHP-IAM | LE-SHP-GF-2CL |
| SAP_CA_BC_IC_LND_RFM_MDSIT_PC | Site Master - Configuration | S_ER9_52002633 | S_ER9_52002633_TRAN | V_RFM_SITE_CUST2 | Maintain Retail Site Parameters | 104671 | LO-RFM | LO-RFM-MD-SIT-2CL |
| SAP_CA_BC_IC_LND_RFM_MDSIT_PC | Site Master - Configuration | S_ER9_52002634 | S_ER9_52002634_TRAN | V_RFM_SITE_CUST3 | Maintain Attributes for Retail Valuation Area | 104672 | LO-RFM | LO-RFM-MD-SIT-2CL |
| SAP_CA_BC_IC_LND_RFM_MDSIT_PC | Site Master - Configuration | V_RFM_SITE_CUST2 |  | V_RFM_SITE_CUST2 | Maintain Retail Site Parameters | 104671 | LO-RFM | LO-RFM-MD-SIT-2CL |
| SAP_CA_BC_IC_LND_RFM_MDSIT_PC | Site Master - Configuration | V_RFM_SITE_CUST3 |  | V_RFM_SITE_CUST3 | Maintain Attributes for Retail Valuation Area | 104672 | LO-RFM | LO-RFM-MD-SIT-2CL |
| SAP_CA_BC_IC_LND_RFM_MDSIT_PC | Site Master - Configuration | V_RFM_SITE_PORG |  | V_RFM_SITE_PORG | Maintain Default Purchasing Organization for Retail Site | 105801 | LO-RFM | LO-RFM-MD-SIT-2CL |
| SAP_CA_BC_IC_LND_RFM_MDSIT_PC | Site Master - Configuration | S_ER9_52003373 | S_ER9_52003373_TRAN | V_RFM_SITE_PORG | Maintain Default Purchasing Organization for Retail Site | 105801 | LO-RFM | LO-RFM-MD-SIT-2CL |
| SAP_CA_BC_IC_LND_RFM_MDSIT_PC | Site Master - Configuration | S_ALR_87007687 | S_ALR_87007687_TRAN | W_OE_EG_WL_0160 | Blocking Reasons | 104670 | LO-RFM | LO-RFM-MD-SIT-2CL |
| SAP_MM_BC_USRDFLT_CONFIG_PC | Materials Management - User Defaults | F1995 | F1995_ADMIN_TRAN |  |  |  | MM-PUR-REQ |  |
| SAP_CA_BC_IC_LND_FIN_SSA_PC | Service Entry Sheet Accruals - Configuration | S_ER9_11002085 | S_ER9_11002085_TRAN | VC_TSSAC_PO_ACRTM | Define Accrual Item Types and Methods for Purchase Orders of Services | 105580 | FI-GL | FI-GL-GL-SSA-2CL |
| SAP_CA_BC_IC_LND_FIN_SSA_PC | Service Entry Sheet Accruals - Configuration | S_ER9_11002174 | S_ER9_11002174_TRAN | VC_TACE_ITEMTY_SSAC | Define Accrual Item Types for Service Entry Sheet Accruals | 105583 | FI-GL | FI-GL-GL-SSA-2CL |
| SAP_CA_BC_IC_LND_FIN_SSA_PC | Service Entry Sheet Accruals - Configuration | S_ER9_11002090 | S_ER9_11002090_TRAN | V_TSSAC_ACCDET | Create and Edit Account Determination for Service Entry Sheet Accruals | 105582 | FI-GL | FI-GL-GL-SSA-2CL |
| SAP_CA_BC_IC_LND_FIN_SSA_PC | Service Entry Sheet Accruals - Configuration | SSACIMGCHK |  | SSAC_IMG_CHECK | Check Customizing Settings for Service Entry Sheet Accruals | 105584 | FI-GL | FI-GL-GL-SSA-2CL |
| SAP_CA_BC_IC_LND_FIN_SSA_PC | Service Entry Sheet Accruals - Configuration | S_ER9_11002164 | S_ER9_11002164_TRAN | SSAC_IMG_CHECK | Check Customizing Settings for Service Entry Sheet Accruals | 105584 | FI-GL | FI-GL-GL-SSA-2CL |
| SAP_CA_BC_IC_LND_FIN_SSA_PC | Service Entry Sheet Accruals - Configuration | S_ER9_11002104 | S_ER9_11002104_TRAN | V_TACE_TRNSFPRIO | Adjust Transfer Priorities for Accruals | 105581 | FI-GL | FI-GL-GL-SSA-2CL |
| SAP_CA_BC_IC_LND_FIN_SR_ES_PC | Statutory Reporting for Spain - Configuration | S_ER9_11001471 | S_ER9_11001471_TRAN | ES_FIWTES_V_WHTKEY | Assign Country/Rgn Specific Withholding Tax Keys to Withholding Tax Codes | 104311 | FI-LOC-FI-ES | FI-AP-AP-Q1 |
| SAP_CA_BC_IC_LND_FIN_SR_ES_PC | Statutory Reporting for Spain - Configuration | S_ER9_11001598 | S_ER9_11001598_TRAN | V_RAT_COEF | Define Pro Rata Coefficients | 103619 | FI-LOC-FI-ES | FI-LOC-RAT |
| SAP_CA_BC_IC_LND_UOM_PC | Units of Measurement - Configuration | V_T006I |  | V_T006I | Maintain ISO Codes for Units of Measurement | 107325 | BC-SRV-ASF-UOM | BC-SRV-ASF-UOM |
| SAP_CA_BC_IC_LND_UOM_PC | Units of Measurement - Configuration | V_T006D |  | V_T006D | Maintain Dimensions for Units of Measurement | 107324 | BC-SRV-ASF-UOM | BC-SRV-ASF-UOM |
| SAP_CA_BC_IC_LND_UOM_PC | Units of Measurement - Configuration | V_T006 |  | V_T006 | Maintain Units of Measurement | 102179 | BC-SRV-ASF-UOM | BC-SRV-ASF-UOM |
| SAP_CA_BC_IC_LND_UOM_PC | Units of Measurement - Configuration | S_YI3_39001375 | S_YI3_39001375_TRAN | V_T006 | Maintain Units of Measurement | 102179 | BC-SRV-ASF-UOM | BC-SRV-ASF-UOM |
| SAP_CA_BC_IC_LND_UOM_PC | Units of Measurement - Configuration | S_YI3_39001374 | S_YI3_39001374_TRAN | V_T006I | Maintain ISO Codes for Units of Measurement | 107325 | BC-SRV-ASF-UOM | BC-SRV-ASF-UOM |
| SAP_CA_BC_IC_LND_UOM_PC | Units of Measurement - Configuration | S_YI3_39001373 | S_YI3_39001373_TRAN | V_T006D | Maintain Dimensions for Units of Measurement | 107324 | BC-SRV-ASF-UOM | BC-SRV-ASF-UOM |
| SAP_CA_BC_IC_LND_UOM_PC | Units of Measurement - Configuration | CUNI |  | SIMG_CFMENUOLMSOMSC | Check Units of Measurement | 102179 | BC-SRV-ASF-UOM | BC-SRV-ASF-UOM |
| SAP_CA_BC_IC_LND_UOM_PC | Units of Measurement - Configuration | S_BCE_68000183 | S_BCE_68000183_TRAN | SIMG_CFMENUOLMSOMSC | Check Units of Measurement | 102179 | BC-SRV-ASF-UOM | BC-SRV-ASF-UOM |
| SAP_CA_BC_IC_LND_FIN_FICA_PC | Contract Accounting - Configuration | S_KK4_74002740 | S_KK4_74002740_TRAN | _FICACREDMGT_FQK50 | Assign Open Items to Credit Segments | 103598 | FI-CA | FI-CA-2CL |
| SAP_CA_BC_IC_LND_FIN_FICA_PC | Contract Accounting - Configuration | S_KK4_74002679 | S_KK4_74002679_TRAN | _FICABTREVD_FQ1382 | Define Main and Subtransactions for the Distribution Posting | 103642 | FI-CA | FI-CA-2CL |
| SAP_CA_BC_IC_LND_FIN_FICA_PC | Contract Accounting - Configuration | S_KK4_74002741 | S_KK4_74002741_TRAN | _FICACREDMGT_FQK53 | Define Specifications for Credit Management | 103599 | FI-CA | FI-CA-2CL |
| SAP_CA_BC_IC_LND_FIN_FICA_PC | Contract Accounting - Configuration | S_ER1_70000228 | S_ER1_70000228_TRAN | _FICAACREDMGT_FQK57 | Define Credit Exposure Category for External Billing Systems | 103600 | FI-CA | FI-CA-2CL |
| SAP_CA_BC_IC_LND_FIN_FICA_PC | Contract Accounting - Configuration | S_KK4_74002597 | S_KK4_74002597_TRAN | _FICABTREVD_FQ1380 | Define Specifications for Deriving Final Recipient | 103640 | FI-CA | FI-CA-2CL |
| SAP_CA_BC_IC_LND_FIN_FICA_PC | Contract Accounting - Configuration | S_KK4_74002596 | S_KK4_74002596_TRAN | _FICABTREVD_FQ1381 | Define Specifications for Revenue Distribution | 103641 | FI-CA | FI-CA-2CL |
| SAP_CA_BC_IC_LND_FIN_FICA_PC | Contract Accounting - Configuration | S_ER1_70000044 | S_ER1_70000044_TRAN | _FICAGP_V_TFKEVLCTRL | Define Record for Business Transactions in Contract Partner | 103718 | FI-CA | FI-CA-2CL |
| SAP_CA_BC_IC_LND_FIN_FICA_PC | Contract Accounting - Configuration | S_KK4_74002568 | S_KK4_74002568_TRAN | _FICAWRKFL_V_TFK4EYE | Define Check Reasons | 103740 | FI-CA | FI-CA-2CL |
| SAP_CA_BC_IC_LND_FIN_FICA_PC | Contract Accounting - Configuration | S_KK4_74002620 | S_KK4_74002620_TRAN | _FICABTIN_FQZ22 | Define Default Value for Callback Reasons | 103705 | FI-CA | FI-CA-2CL |
| SAP_CA_BC_IC_LND_FIN_FICA_PC | Contract Accounting - Configuration | S_KK4_74002619 | S_KK4_74002619_TRAN | _FICABTIN_TFK050D | Define Reasons for Receivables Callbacks | 103704 | FI-CA | FI-CA-2CL |
| SAP_CA_BC_IC_LND_FIN_FICA_PC | Contract Accounting - Configuration | S_KK4_74002593 | S_KK4_74002593_TRAN | _FICABTIN_FQZ21 | Define Defaults for Collection Agency Charges | 103703 | FI-CA | FI-CA-2CL |
| SAP_CA_BC_IC_LND_FIN_FICA_PC | Contract Accounting - Configuration | S_E4M_85000036 | S_E4M_85000036_TRAN | _FICABTIN_FQ1132 | Define Defaults for Collection Agency Postings | 103709 | FI-CA | FI-CA-2CL |
| SAP_CA_BC_IC_LND_FIN_FICA_PC | Contract Accounting - Configuration | S_KK4_74002278 | S_KK4_74002278_TRAN | _FICABTIN_1054 | Define Specs for Submission to External Collection Agencies | 103702 | FI-CA | FI-CA-2CL |
| SAP_CA_BC_IC_LND_FIN_FICA_PC | Contract Accounting - Configuration | S_E4M_85000037 | S_E4M_85000037_TRAN | _FICABTIN_V_TFK050S | Maintain Status of Collection Units | 103710 | FI-CA | FI-CA-2CL |
| SAP_CA_BC_IC_LND_FIN_FICA_PC | Contract Accounting - Configuration | S_E4M_85000038 | S_E4M_85000038_TRAN | _FICABTIN_V_TFK050T | Define Categories of Collection Units | 103711 | FI-CA | FI-CA-2CL |
| SAP_CA_BC_IC_LND_FIN_FICA_PC | Contract Accounting - Configuration | S_E4M_85000035 | S_E4M_85000035_TRAN | _FICABTIN_FQ1131 | Define Defaults for Processing Collection Agency Information | 103708 | FI-CA | FI-CA-2CL |
| SAP_CA_BC_IC_LND_FIN_FICA_PC | Contract Accounting - Configuration | S_EAI_74002802 | S_EAI_74002802_TRAN | _FICABTPY_V_TFKP2P | Define Specifications for Valuation of Promise to Pay | 103809 | FI-CA | FI-CA-2CL |
| SAP_CA_BC_IC_LND_FIN_FICA_PC | Contract Accounting - Configuration | S_EAI_74002801 | S_EAI_74002801_TRAN | _FICABTPY_TFKP2PD | Define Specifications for Creation | 103768 | FI-CA | FI-CA-2CL |
| SAP_CA_BC_IC_LND_FIN_FICA_PC | Contract Accounting - Configuration | S_EAI_74002800 | S_EAI_74002800_TRAN | _FICABTPY_TFKP2PRW | Define Reasons for Withdrawal | 103767 | FI-CA | FI-CA-2CL |
| SAP_CA_BC_IC_LND_FIN_FICA_PC | Contract Accounting - Configuration | S_ER1_70000274 | S_ER1_70000274_TRAN | _FICAWRKFL_FQC003 | Define Default Check Reason for Workflow | 103769 | FI-CA | FI-CA-2CL |
| SAP_CA_BC_IC_LND_FIN_FICA_PC | Contract Accounting - Configuration | S_EAI_74002798 | S_EAI_74002798_TRAN | _FICABTPY_TFKP2PC | Define Categories | 103765 | FI-CA | FI-CA-2CL |
| SAP_CA_BC_IC_LND_FIN_FICA_PC | Contract Accounting - Configuration | S_EMI_14000206 | S_EMI_14000206_TRAN | _FICABTPY_FQEXC8 | Make Basic Settings | 103606 | FI-CA | FI-CA-2CL |
| SAP_CA_BC_IC_LND_FIN_FICA_PC | Contract Accounting - Configuration | S_EAI_74002799 | S_EAI_74002799_TRAN | _FICABTPY_TFKP2PRC | Define Reasons for Creation | 103766 | FI-CA | FI-CA-2CL |
| SAP_CA_BC_IC_LND_FIN_FICA_PC | Contract Accounting - Configuration | S_SK4_84000011 | S_SK4_84000011_TRAN | _FICABTPY_FPCJM | Define Master Data for Cash Journal | 103609 | FI-CA | FI-CA-2CL |
| SAP_CA_BC_IC_LND_FIN_FICA_PC | Contract Accounting - Configuration | S_ER1_70000241 | S_ER1_70000241_TRAN | _FICABFDP_TFK012B | Define Additional Bank Accounts for Bank Clearing Accounts | 103687 | FI-CA | FI-CA-2CL |
| SAP_CA_BC_IC_LND_FIN_FICA_PC | Contract Accounting - Configuration | S_KK4_74002161 | S_KK4_74002161_TRAN | _FICABTPY_TFK012 | Define Bank Clearing Accounts for Payment Lots | 103605 | FI-CA | FI-CA-2CL |
| SAP_CA_BC_IC_LND_FIN_FICA_PC | Contract Accounting - Configuration | S_EAI_74002808 | S_EAI_74002808_TRAN | _FICABTPY_FQEXC2 | Define Document Types for Postings for External Cash Desk Services | 103614 | FI-CA | FI-CA-2CL |
| SAP_CA_BC_IC_LND_FIN_FICA_PC | Contract Accounting - Configuration | S_EAI_74002806 | S_EAI_74002806_TRAN | _FICABTPY_VC_DFKKCJM | Define Master Data for External Cash Desk Services | 103608 | FI-CA | FI-CA-2CL |
| SAP_CA_BC_IC_LND_FIN_FICA_PC | Contract Accounting - Configuration | S_EAI_74002807 | S_EAI_74002807_TRAN | _FICABTPY_FQEXC1 | Define Specifications for Agent Postings | 103611 | FI-CA | FI-CA-2CL |
| SAP_CA_BC_IC_LND_FIN_FICA_PC | Contract Accounting - Configuration | S_EAI_74002805 | S_EAI_74002805_TRAN | _FICABTPY_EXTCDS | Define Cash Desk Structure | 103607 | FI-CA | FI-CA-2CL |
| SAP_CA_BC_IC_LND_FIN_FICA_PC | Contract Accounting - Configuration | S_EAI_14000023 | S_EAI_14000023_TRAN | _FICABTPY_FQH4 | Define Cash Desk Clearing Accounts | 103610 | FI-CA | FI-CA-2CL |
| SAP_CA_BC_IC_LND_FIN_FICA_PC | Contract Accounting - Configuration | S_AIR_74002798 | S_AIR_74002798_TRAN | _FICABTPY_FQEXC3 | Define Clearing Accounts for Payment Lot for External Cash Desks | 103615 | FI-CA | FI-CA-2CL |
| SAP_CA_BC_IC_LND_FIN_FICA_PC | Contract Accounting - Configuration | FQC003 |  | _FICAWRKFL_FQC003 | Define Default Check Reason for Workflow | 103769 | FI-CA | FI-CA-2CL |
| SAP_CA_BC_IC_LND_FIN_FICA_PC | Contract Accounting - Configuration | FQZ22 |  | _FICABTIN_FQZ22 | Define Default Value for Callback Reasons | 103705 | FI-CA | FI-CA-2CL |
| SAP_CA_BC_IC_LND_FIN_FICA_PC | Contract Accounting - Configuration | FQZ21 |  | _FICABTIN_FQZ21 | Define Defaults for Collection Agency Charges | 103703 | FI-CA | FI-CA-2CL |
| SAP_CA_BC_IC_LND_FIN_FICA_PC | Contract Accounting - Configuration | FQZ15 |  | _FICABTIN_1054 | Define Specs for Submission to External Collection Agencies | 103702 | FI-CA | FI-CA-2CL |
| SAP_CA_BC_IC_LND_FIN_FICA_PC | Contract Accounting - Configuration | FQK50 |  | _FICACREDMGT_FQK50 | Assign Open Items to Credit Segments | 103598 | FI-CA | FI-CA-2CL |
| SAP_CA_BC_IC_LND_FIN_FICA_PC | Contract Accounting - Configuration | FQH4 |  | _FICABTPY_FQH4 | Define Cash Desk Clearing Accounts | 103610 | FI-CA | FI-CA-2CL |
| SAP_CA_BC_IC_LND_FIN_FICA_PC | Contract Accounting - Configuration | FQK53 |  | _FICACREDMGT_FQK53 | Define Specifications for Credit Management | 103599 | FI-CA | FI-CA-2CL |
| SAP_CA_BC_IC_LND_FIN_FICA_PC | Contract Accounting - Configuration | FQK57 |  | _FICAACREDMGT_FQK57 | Define Credit Exposure Category for External Billing Systems | 103600 | FI-CA | FI-CA-2CL |
| SAP_CA_BC_IC_LND_FIN_FICA_PC | Contract Accounting - Configuration | FQEXC3 |  | _FICABTPY_FQEXC3 | Define Clearing Accounts for Payment Lot for External Cash Desks | 103615 | FI-CA | FI-CA-2CL |
| SAP_CA_BC_IC_LND_FIN_FICA_PC | Contract Accounting - Configuration | FQEXC8 |  | _FICABTPY_FQEXC8 | Make Basic Settings | 103606 | FI-CA | FI-CA-2CL |
| SAP_CA_BC_IC_LND_FIN_FICA_PC | Contract Accounting - Configuration | FQ1382 |  | _FICABTREVD_FQ1382 | Define Main and Subtransactions for the Distribution Posting | 103642 | FI-CA | FI-CA-2CL |
| SAP_CA_BC_IC_LND_FIN_FICA_PC | Contract Accounting - Configuration | FQEXC2 |  | _FICABTPY_FQEXC2 | Define Document Types for Postings for External Cash Desk Services | 103614 | FI-CA | FI-CA-2CL |
| SAP_CA_BC_IC_LND_FIN_FICA_PC | Contract Accounting - Configuration | FQEXC1 |  | _FICABTPY_FQEXC1 | Define Specifications for Agent Postings | 103611 | FI-CA | FI-CA-2CL |
| SAP_CA_BC_IC_LND_FIN_FICA_PC | Contract Accounting - Configuration | FQ1381 |  | _FICABTREVD_FQ1381 | Define Specifications for Revenue Distribution | 103641 | FI-CA | FI-CA-2CL |
| SAP_CA_BC_IC_LND_FIN_FICA_PC | Contract Accounting - Configuration | FQ1380 |  | _FICABTREVD_FQ1380 | Define Specifications for Deriving Final Recipient | 103640 | FI-CA | FI-CA-2CL |
| SAP_CA_BC_IC_LND_FIN_FICA_PC | Contract Accounting - Configuration | FQ1132 |  | _FICABTIN_FQ1132 | Define Defaults for Collection Agency Postings | 103709 | FI-CA | FI-CA-2CL |
| SAP_CA_BC_IC_LND_FIN_FICA_PC | Contract Accounting - Configuration | FQEXC9 |  | _FICABTPY_FQEXC9 | Enter Cash Desk Closing Accounts | 103613 | FI-CA | FI-CA-2CL |
| SAP_CA_BC_IC_LND_FIN_FICA_PC | Contract Accounting - Configuration | FQ1131 |  | _FICABTIN_FQ1131 | Define Defaults for Processing Collection Agency Information | 103708 | FI-CA | FI-CA-2CL |
| SAP_CA_BC_IC_LND_FIN_FICA_PC | Contract Accounting - Configuration | S_EMI_14000251 | S_EMI_14000251_TRAN | _FICABTPY_FQEXC9 | Enter Cash Desk Closing Accounts | 103613 | FI-CA | FI-CA-2CL |
| SAP_CA_BC_IC_LND_FIN_FICA_PC | Contract Accounting - Configuration | FQ2104 |  | _FICABFDP_FQ2104 | Enter Alternative Tax Determination Code | 103548 | FI-CA | FI-CA-2CL |
| SAP_CA_BC_IC_LND_FIN_FICA_PC | Contract Accounting - Configuration | FQ1133 |  | _FICABTIN_FQ1133 | Maintain Defaults for Automatic Returns | 103763 | FI-CA | FI-CA-2CL |
| SAP_CA_BC_IC_LND_FIN_FICA_PC | Contract Accounting - Configuration | S_ER1_70000269 | S_ER1_70000269_TRAN | _FICABTIN_FQ1133 | Maintain Defaults for Automatic Returns | 103763 | FI-CA | FI-CA-2CL |
| SAP_CA_BC_IC_LND_FIN_FICA_PC | Contract Accounting - Configuration | FQ1150 |  | _FICABTPY_FQ1150 | Define Account Determination for Payments via Payment Service Provider | 102546 | FI-CA | FI-CA-2CL |
| SAP_CA_BC_IC_LND_FIN_FICA_PC | Contract Accounting - Configuration | FQ1152 |  | _FICABTPY_FQ1152 | Specifications for Billing Document Posting | 102547 | FI-CA | FI-CA-2CL |
| SAP_CA_BC_IC_LND_FIN_FICA_PC | Contract Accounting - Configuration | FQ1291 |  | _FICABTDCSV_FQ1291 | Maintain Alternative Accounts for Resetting Flat-Rate Value Adjustments | 102719 | FI-CA | FI-CA-2CL |
| SAP_CA_BC_IC_LND_FIN_FICA_PC | Contract Accounting - Configuration | FQ1155 |  | _FICABTPY_FQ1155 | Define Specifications for Posting Exchange Rate Differences | 102549 | FI-CA | FI-CA-2CL |
| SAP_CA_BC_IC_LND_FIN_FICA_PC | Contract Accounting - Configuration | FQ1290 |  | _FICABTDCSV_FQ1290 | Maintain Account Determination for Flat-Rate Value Adjustment | 102718 | FI-CA | FI-CA-2CL |
| SAP_CA_BC_IC_LND_FIN_FICA_PC | Contract Accounting - Configuration | FQ1154 |  | _FICABTPY_FQ1154 | Define Specifications for Charge Postings | 102548 | FI-CA | FI-CA-2CL |
| SAP_CA_BC_IC_LND_FIN_FICA_PC | Contract Accounting - Configuration | FQ1032 |  | _FICABTPY_FQ1032 | Define Default Values for Payment Order Lots | 102681 | FI-CA | FI-CA-2CL |
| SAP_CA_BC_IC_LND_FIN_FICA_PC | Contract Accounting - Configuration | FQ1041 |  | _FICABTRE_FQ1041 | Define Clarification Accounts for Returns | 102256 | FI-CA | FI-CA-2CL |
| SAP_CA_BC_IC_LND_FIN_FICA_PC | Contract Accounting - Configuration | FQ1297 |  | _BTDCSV_FQ1297 | Define Valuation Areas for Receivables Adjustments | 102194 | FI-CA | FI-CA-2CL |
| SAP_CA_BC_IC_LND_FIN_FICA_PC | Contract Accounting - Configuration | FQ1153 |  | _FICABTPY_FQ1153 | Define Specifications for Automatic Returns Posting | 103100 | FI-CA | FI-CA-2CL |
| SAP_CA_BC_IC_LND_FIN_FICA_PC | Contract Accounting - Configuration | FQ1321 |  | _FICABTCP_FQ1321 | Define Clearing Account for Transferring Credits | 102265 | FI-CA | FI-CA-2CL |
| SAP_CA_BC_IC_LND_FIN_FICA_PC | Contract Accounting - Configuration | FPU1 |  | _FICACLRE_FPU1 | Define Receivables and Payables Accounts | 102513 | FI-CA | FI-CA-2CL |
| SAP_CA_BC_IC_LND_FIN_FICA_PC | Contract Accounting - Configuration | FQ1156 |  | _FICABTPY_FQ1156 | Define Accounts for Posting for Exchange Rate Differences | 102550 | FI-CA | FI-CA-2CL |
| SAP_CA_BC_IC_LND_FIN_FICA_PC | Contract Accounting - Configuration | FQ1095 |  | _FICABTPY_FQ1095 | Define Variant Determination for Payment Medium Program | 102207 | FI-CA | FI-CA-2CL |
| SAP_CA_BC_IC_LND_FIN_FICA_PC | Contract Accounting - Configuration | FQ0500 |  | _FICAPV_FQ0500 | Define Specifications for Derivation of Standard Account Assignment | 102679 | FI-CA | FI-CA-2CL |
| SAP_CA_BC_IC_LND_FIN_FICA_PC | Contract Accounting - Configuration | FQ1062 |  | _FICABTTP_FQ1062 | Define Specifications Dependent on Transfer Reason | 103417 | FI-CA | FI-CA-2CL |
| SAP_CA_BC_IC_LND_FIN_FICA_PC | Contract Accounting - Configuration | FQ0310 |  | _FICABFDP_FQ0310 | Define Additional Account Assignments for Down Payments | 103444 | FI-CA | FI-CA-2CL |
| SAP_CA_BC_IC_LND_FIN_FICA_PC | Contract Accounting - Configuration | FQKPM |  | _FICAISAD_FQZ1 | Define Line Layout Variants for Account Balance | 101950 | FI-CA | FI-CA-2CL |
| SAP_CA_BC_IC_LND_FIN_FICA_PC | Contract Accounting - Configuration | FQI4Z |  | _FICABTIC_FQI4Z | Activate Additional Functions for Interest Calculation | 102203 | FI-CA | FI-CA-2CL |
| SAP_CA_BC_IC_LND_FIN_FICA_PC | Contract Accounting - Configuration | FQC1210 |  | _FICAINSD_FQC1210 | Derive Document Type from SD Billing Doc Data | 103207 | FI-CA | FI-CA-2CL |
| SAP_CA_BC_IC_LND_FIN_FICA_PC | Contract Accounting - Configuration | FQC0_ASS | FQC0_ASS_TRAN |  |  |  | FI-CA |  |
| SAP_CA_BC_IC_LND_FIN_FICA_PC | Contract Accounting - Configuration | FQCG |  | _FICABTDU_FQCG | Define Default Values for Contract Account Group and Strategy | 103567 | FI-CA | FI-CA-2CL |
| SAP_CA_BC_IC_LND_FIN_FICA_PC | Contract Accounting - Configuration | FQKPA |  | _FICABFDP_FQKPA | Define Line Layout for Mass Change in Account Maintenance | 103375 | FI-CA | FI-CA-2CL |
| SAP_CA_BC_IC_LND_FIN_FICA_PC | Contract Accounting - Configuration | FQC1350 |  | _FICACLRE_FQC1350 | Define Adjustment Accounts | 102514 | FI-CA | FI-CA-2CL |
| SAP_CA_BC_IC_LND_FIN_FICA_PC | Contract Accounting - Configuration | FQI7 |  | _FICABTSE_FQI7 | Define Specifications for Cash Security Deposit Int. Calc. (Mass Proc.) | 103483 | FI-CA | FI-CA-2CL |
| SAP_CA_BC_IC_LND_FIN_FICA_PC | Contract Accounting - Configuration | FQI4 |  | _FICABTIC_FQI4 | Define Specifications for Interest Calculation | 102202 | FI-CA | FI-CA-2CL |
| SAP_CA_BC_IC_LND_FIN_FICA_PC | Contract Accounting - Configuration | FQC8 |  | _FICACLFC_FQC8 | Define Valuation Area-Specific Accounts for Exchange Rate Differences | 102205 | FI-CA | FI-CA-2CL |
| SAP_CA_BC_IC_LND_FIN_FICA_PC | Contract Accounting - Configuration | FQC0075 |  | _FICACLFC_FQC0075 | Define Accounts for Translation of Account Balances | 102206 | FI-CA | FI-CA-2CL |
| SAP_CA_BC_IC_LND_FIN_FICA_PC | Contract Accounting - Configuration | FQI8 |  | _FICABTDU_FQI8 | Define Specifications for Interest on Arrears | 102195 | FI-CA | FI-CA-2CL |
| SAP_CA_BC_IC_LND_FIN_FICA_PC | Contract Accounting - Configuration | FQC1351 |  | _FICABFDP_FQC1351 | Specification of Document Types for Reclassifications | 106710 | FI-CA | FI-CA-2CL |
| SAP_CA_BC_IC_LND_FIN_FICA_PC | Contract Accounting - Configuration | FQDPR |  | _FICADS_FQDPR | Specify Determination of Rule Variants for Data Protection in FI-CA | 102286 | FI-CA | FI-CA-2CL |
| SAP_CA_BC_IC_LND_FIN_FICA_PC | Contract Accounting - Configuration | FQC0_AS | FQC0_AS_TRAN |  |  |  | FI-CA |  |
| SAP_CA_BC_IC_LND_FIN_FICA_PC | Contract Accounting - Configuration | FQC1355 |  | _FICACLRE_FQC1355 | Define Adjustment Accounts for Reclassification by Due Date | 102516 | FI-CA | FI-CA-2CL |
| SAP_CA_BC_IC_LND_FIN_FICA_PC | Contract Accounting - Configuration | FQC73 |  | _FICABTDCSV_FQC73 | Define Accounts for Exchange Rate Differences During Value Adjustments | 102861 | FI-CA | FI-CA-2CL |
| SAP_CA_BC_IC_LND_FIN_FICA_PC | Contract Accounting - Configuration | FQC1200 |  | _FICAINSD_FQC1200 | Derive Main/Subtransaction from SD Information | 103206 | FI-CA | FI-CA-2CL |
| SAP_CA_BC_IC_LND_FIN_FICA_PC | Contract Accounting - Configuration | FQI6 |  | _FICABTIC_FQI6 | Define Specifications for the Mass Run | 102204 | FI-CA | FI-CA-2CL |
| SAP_CA_BC_IC_LND_FIN_FICA_PC | Contract Accounting - Configuration | FQC002 |  | _FICABFGFTD_FQC002 | Define Determination of Reporting Key | 102664 | FI-CA | FI-CA-2CL |
| SAP_CA_BC_IC_LND_FIN_FICA_PC | Contract Accounting - Configuration | FQC1005 |  | _FICABTPY_FQC1005 | Define Prefix for Created Lot IDs During Account Statement Transfer | 102551 | FI-CA | FI-CA-2CL |
| SAP_CA_BC_IC_LND_FIN_FICA_PC | Contract Accounting - Configuration | FQZJ |  | _FICABTPY_FQZJ | Define Clarification Account | 102267 | FI-CA | FI-CA-2CL |
| SAP_CA_BC_IC_LND_FIN_FICA_PC | Contract Accounting - Configuration | FQC001 |  | _FICACBFDP_FQC001 | Define Account Determination Data Relevant to Transactions | 102293 | FI-CA | FI-CA-2CL |
| SAP_CA_BC_IC_LND_FIN_FICA_PC | Contract Accounting - Configuration | FQC000 |  | _FICACBFDP_FQC000 | Define Acct Assmt Data Relevant to Main Transactions | 102292 | FI-CA | FI-CA-2CL |
| SAP_CA_BC_IC_LND_FIN_FICA_PC | Contract Accounting - Configuration | FQZ11 |  | _FICABTDCSV_FQZ11 | Maintain Account Determination for Ind. Value Adjustment | 102200 | FI-CA | FI-CA-2CL |
| SAP_CA_BC_IC_LND_FIN_FICA_PC | Contract Accounting - Configuration | FQZ9 |  | _FICABFDP_FQZ9 | Define Accounts for Down Payment Tax Clearing | 103445 | FI-CA | FI-CA-2CL |
| SAP_CA_BC_IC_LND_FIN_FICA_PC | Contract Accounting - Configuration | FQZE |  | _FICAINGL_FQZE | Define Posting Specifications for General Ledger Transfer | 101886 | FI-CA | FI-CA-2CL |
| SAP_CA_BC_IC_LND_FIN_FICA_PC | Contract Accounting - Configuration | FQZ1A |  | _FICATDCSV_FQZ1A | Maintain Alternative Accounts for Resetting Individual Value Adjustments | 102904 | FI-CA | FI-CA-2CL |
| SAP_CA_BC_IC_LND_FIN_FICA_PC | Contract Accounting - Configuration | FQZ8 |  | _FICABFDP_FQZ8 | Define Accounts for Sales/Purchase Tax | 101845 | FI-CA | FI-CA-2CL |
| SAP_CA_BC_IC_LND_FIN_FICA_PC | Contract Accounting - Configuration | FQZD |  | _FICABFDP_FQZD | Define Accounts for Exchange Rate Differences | 102208 | FI-CA | FI-CA-2CL |
| SAP_CA_BC_IC_LND_FIN_FICA_PC | Contract Accounting - Configuration | FQZ1123 |  | _FICABTPYPC_FQZ1123 | Define Specifications for Automatic Returns Posting | 101958 | FI-CA | FI-CA-2CL |
| SAP_CA_BC_IC_LND_FIN_FICA_PC | Contract Accounting - Configuration | FQZG |  | _FICABFDP_FQZG | Define Account Assignments for Down Payments and Charges | 102254 | FI-CA | FI-CA-2CL |
| SAP_CA_BC_IC_LND_FIN_FICA_PC | Contract Accounting - Configuration | FQZF |  | _FICABTRE_FQZF | Define Bank Clearing Accounts and Charges Accounts | 102257 | FI-CA | FI-CA-2CL |
| SAP_CA_BC_IC_LND_FIN_FICA_PC | Contract Accounting - Configuration | FQZ16 |  | _FICABTTP_FQZ16 | Define Specifications and Default Values for Transfer | 103416 | FI-CA | FI-CA-2CL |
| SAP_CA_BC_IC_LND_FIN_FICA_PC | Contract Accounting - Configuration | FQZ08 |  | _FICABTDCSV_FQZ08 | Maintain Account Determination for Doubtful Item Entries | 102199 | FI-CA | FI-CA-2CL |
| SAP_CA_BC_IC_LND_FIN_FICA_PC | Contract Accounting - Configuration | FQZ07 |  | _FICABTDCSV_FQZ07 | Maintain Default Values for Transfer Posting Run | 102227 | FI-CA | FI-CA-2CL |
| SAP_CA_BC_IC_LND_FIN_FICA_PC | Contract Accounting - Configuration | FQZ06 |  | _FICABTDU_FQZ06 | Specifications for Automatically Deactivating Installment Plans | 102253 | FI-CA | FI-CA-2CL |
| SAP_CA_BC_IC_LND_FIN_FICA_PC | Contract Accounting - Configuration | FQZ05 |  | _FICABFOI_FQZ05 | Define Default Values for Automatic Clearing | 103368 | FI-CA | FI-CA-2CL |
| SAP_CA_BC_IC_LND_FIN_FICA_PC | Contract Accounting - Configuration | FQZ04 |  | _FICABTWO_FQZ04 | Define Automatic G/L Account Determination for Write-Offs | 102226 | FI-CA | FI-CA-2CL |
| SAP_CA_BC_IC_LND_FIN_FICA_PC | Contract Accounting - Configuration | FQZ1124 |  | _FICABTPYPC_FQZ1124 | Define Specification for Charge Posting | 101959 | FI-CA | FI-CA-2CL |
| SAP_CA_BC_IC_LND_FIN_FICA_PC | Contract Accounting - Configuration | FQZ03 |  | _FICABTWO_FQZ03 | Define Specs and Default Values for Mass Write-Offs | 102225 | FI-CA | FI-CA-2CL |
| SAP_CA_BC_IC_LND_FIN_FICA_PC | Contract Accounting - Configuration | FQU1 |  | _FICABTTP_FQU1 | Define Default Value for Transfer Reason | 103415 | FI-CA | FI-CA-2CL |
| SAP_CA_BC_IC_LND_FIN_FICA_PC | Contract Accounting - Configuration | FQU2 |  | _FICABTTP_FQU2_A | Define Transactions for the Transfer of Items and Requests | 103414 | FI-CA | FI-CA-2CL |
| SAP_CA_BC_IC_LND_FIN_FICA_PC | Contract Accounting - Configuration | S_EAI_74002829 | S_EAI_74002829_TRAN | _FICABTDU_V_TFK041B | Define Master Data Groups | 103566 | FI-CA | FI-CA-2CL |
| SAP_CA_BC_IC_LND_FIN_FICA_PC | Contract Accounting - Configuration | FQZ02 |  | _FICABTWO_FQZ02 | Define Specifications and Default Values for Write-Off | 101960 | FI-CA | FI-CA-2CL |
| SAP_CA_BC_IC_LND_FIN_FICA_PC | Contract Accounting - Configuration | FQP4 |  | _FICABTPY_VC_TFK042E | Define Specifications for Paying Company Code | 101251 | FI-CA | FI-CA-2CL |
| SAP_CA_BC_IC_LND_FIN_FICA_PC | Contract Accounting - Configuration | FQKPO |  | _FICABFOI_FQZ2 | Define Line Layout Variants for Open Item Processing | 103374 | FI-CA | FI-CA-2CL |
| SAP_CA_BC_IC_LND_FIN_FICA_PC | Contract Accounting - Configuration | S_E5M_74000080 | S_E5M_74000080_TRAN | _FICAECSL_V_TFK001ZM | Make Specifications for EC Sales List | 102840 | FI-CA | FI-CA-2CL |
| SAP_CA_BC_IC_LND_FIN_FICA_PC | Contract Accounting - Configuration | FQP1 |  | _FICABTPY_VC_TFK042Z | Define Payment Methods | 101952 | FI-CA | FI-CA-2CL |
| SAP_CA_BC_IC_LND_FIN_FICA_PC | Contract Accounting - Configuration | S_E5M_74000078 | S_E5M_74000078_TRAN | _FICABTTP_FQU2_A | Define Transactions for the Transfer of Items and Requests | 103414 | FI-CA | FI-CA-2CL |
| SAP_CA_BC_IC_LND_FIN_FICA_PC | Contract Accounting - Configuration | S_EAI_14000018 | S_EAI_14000018_TRAN | _FICABTTP_FQ1062 | Define Specifications Dependent on Transfer Reason | 103417 | FI-CA | FI-CA-2CL |
| SAP_CA_BC_IC_LND_FIN_FICA_PC | Contract Accounting - Configuration | S_EAI_14000006 | S_EAI_14000006_TRAN | _FICABTDU_VC_TFK047U | Define Collection Step | 103563 | FI-CA | FI-CA-2CL |
| SAP_CA_BC_IC_LND_FIN_FICA_PC | Contract Accounting - Configuration | S_E5M_74000008 | S_E5M_74000008_TRAN | _FICACLRE_FQC1355 | Define Adjustment Accounts for Reclassification by Due Date | 102516 | FI-CA | FI-CA-2CL |
| SAP_CA_BC_IC_LND_FIN_FICA_PC | Contract Accounting - Configuration | S_E4I_14000030 | S_E4I_14000030_TRAN | _BTDCSV_FQ1297 | Define Valuation Areas for Receivables Adjustments | 102194 | FI-CA | FI-CA-2CL |
| SAP_CA_BC_IC_LND_FIN_FICA_PC | Contract Accounting - Configuration | FQZV |  | _FICABTPYPC_FQZV | Define Accounts for Payment Card Institute | 101957 | FI-CA | FI-CA-2CL |
| SAP_CA_BC_IC_LND_FIN_FICA_PC | Contract Accounting - Configuration | S_E4M_85000084 | S_E4M_85000084_TRAN | _FICABTDU_TFK047Y | Define Collection Levels | 103564 | FI-CA | FI-CA-2CL |
| SAP_CA_BC_IC_LND_FIN_FICA_PC | Contract Accounting - Configuration | S_E4M_85000083 | S_E4M_85000083_TRAN | _FICABTDU_TFK047Q | Define Collection Step Category | 103565 | FI-CA | FI-CA-2CL |
| SAP_CA_BC_IC_LND_FIN_FICA_PC | Contract Accounting - Configuration | S_E4M_85000049 | S_E4M_85000049_TRAN | _FICABFDP_FQ0310 | Define Additional Account Assignments for Down Payments | 103444 | FI-CA | FI-CA-2CL |
| SAP_CA_BC_IC_LND_FIN_FICA_PC | Contract Accounting - Configuration | FQZZ |  | _FICABTDI_FQZZ | Define Default Values for Interest on Installment Plans | 102198 | FI-CA | FI-CA-2CL |
| SAP_CA_BC_IC_LND_FIN_FICA_PC | Contract Accounting - Configuration | FQZT |  | _FICABTPY_FQZT | Define Clearing Account for Check Deposit | 102266 | FI-CA | FI-CA-2CL |
| SAP_CA_BC_IC_LND_FIN_FICA_PC | Contract Accounting - Configuration | FQZY |  | _FICABTDU_FQZY | Define Document Types for Dunning Charge Categories | 102193 | FI-CA | FI-CA-2CL |
| SAP_CA_BC_IC_LND_FIN_FICA_PC | Contract Accounting - Configuration | FQZU |  | _FICABTDI_FQZU | Define Default Values for Installment Plan Charge | 102197 | FI-CA | FI-CA-2CL |
| SAP_CA_BC_IC_LND_FIN_FICA_PC | Contract Accounting - Configuration | FQZO |  | _FICABFOI_FQZO | Define Default Values for Resetting Clearing | 102319 | FI-CA | FI-CA-2CL |
| SAP_CA_BC_IC_LND_FIN_FICA_PC | Contract Accounting - Configuration | S_KK4_74002189 | S_KK4_74002189_TRAN | _FICAINCM_V_TFK036V | Define Alternative Planning Levels for Transactions | 101888 | FI-CA | FI-CA-2CL |
| SAP_CA_BC_IC_LND_FIN_FICA_PC | Contract Accounting - Configuration | FQZQ |  | _FICABTDI_FQZQ | Define Default Values for Installment Plan | 102196 | FI-CA | FI-CA-2CL |
| SAP_CA_BC_IC_LND_FIN_FICA_PC | Contract Accounting - Configuration | FQZN |  | _FICABTPY_FQZN | Define Specifications for Repayment of Incoming Payments | 102268 | FI-CA | FI-CA-2CL |
| SAP_CA_BC_IC_LND_FIN_FICA_PC | Contract Accounting - Configuration | S_ER1_70000055 | S_ER1_70000055_TRAN | _FICABFDP_FQC1351 | Specification of Document Types for Reclassifications | 106710 | FI-CA | FI-CA-2CL |
| SAP_CA_BC_IC_LND_FIN_FICA_PC | Contract Accounting - Configuration | FQZM |  | _FICABFDP_FQZM | Define Default Values for Document Entry | 103367 | FI-CA | FI-CA-2CL |
| SAP_CA_BC_IC_LND_FIN_FICA_PC | Contract Accounting - Configuration | S_ER1_70000080 | S_ER1_70000080_TRAN | _FICABTDCSV_FQ1290 | Maintain Account Determination for Flat-Rate Value Adjustment | 102718 | FI-CA | FI-CA-2CL |
| SAP_CA_BC_IC_LND_FIN_FICA_PC | Contract Accounting - Configuration | S_KK4_74002171 | S_KK4_74002171_TRAN | _FICAABTPY_VC_TFK006 | Define Interpretation Rules for Note to Payee | 102222 | FI-CA | FI-CA-2CL |
| SAP_CA_BC_IC_LND_FIN_FICA_PC | Contract Accounting - Configuration | S_KK4_74002124 | S_KK4_74002124_TRAN | _FICABTIC_FQI6 | Define Specifications for the Mass Run | 102204 | FI-CA | FI-CA-2CL |
| SAP_CA_BC_IC_LND_FIN_FICA_PC | Contract Accounting - Configuration | S_KK4_74002120 | S_KK4_74002120_TRAN | _FICABTDU_V_TFK047S | Define Dunning Lock Reasons | 101946 | FI-CA | FI-CA-2CL |
| SAP_CA_BC_IC_LND_FIN_FICA_PC | Contract Accounting - Configuration | S_KK4_74002119 | S_KK4_74002119_TRAN | _FICABTDU_TFK046A | Define Time-Dependent Creditworthiness Weightings | 103523 | FI-CA | FI-CA-2CL |
| SAP_CA_BC_IC_LND_FIN_FICA_PC | Contract Accounting - Configuration | S_ER1_70000243 | S_ER1_70000243_TRAN | _FICADM_FICADMCATEGO | Create Values for "Category" Attribute | 103647 | FI-CA | FI-CA-2CL |
| SAP_CA_BC_IC_LND_FIN_FICA_PC | Contract Accounting - Configuration | S_ER1_70000090 | S_ER1_70000090_TRAN | _FICABTDCSV_FQC73 | Define Accounts for Exchange Rate Differences During Value Adjustments | 102861 | FI-CA | FI-CA-2CL |
| SAP_CA_BC_IC_LND_FIN_FICA_PC | Contract Accounting - Configuration | S_KK4_74002127 | S_KK4_74002127_TRAN | _FICABTIC_TFK056S | Define Interest Lock Reasons | 102068 | FI-CA | FI-CA-2CL |
| SAP_CA_BC_IC_LND_FIN_FICA_PC | Contract Accounting - Configuration | S_KK4_74002107 | S_KK4_74002107_TRAN | _FICABTPY_TFKPKC | Select Item Indicator for the Clarification Worklist | 102465 | FI-CA | FI-CA-2CL |
| SAP_CA_BC_IC_LND_FIN_FICA_PC | Contract Accounting - Configuration | S_KK4_74002184 | S_KK4_74002184_TRAN | _FICABTDCSV_FQZ07 | Maintain Default Values for Transfer Posting Run | 102227 | FI-CA | FI-CA-2CL |
| SAP_CA_BC_IC_LND_FIN_FICA_PC | Contract Accounting - Configuration | S_ER1_70000045 | S_ER1_70000045_TRAN | _FICABTDU_VCTFK047AC | Configure Dunning Procedure | 102469 | FI-CA | FI-CA-2CL |
| SAP_CA_BC_IC_LND_FIN_FICA_PC | Contract Accounting - Configuration | S_EMI_14000209 | S_EMI_14000209_TRAN | _FICAFIORI_VTFKKWLAC | Define Actions for Worklists | 101951 | FI-CA | FI-CA-2CL |
| SAP_CA_BC_IC_LND_FIN_FICA_PC | Contract Accounting - Configuration | S_EMI_14000101 | S_EMI_14000101_TRAN | _FICADISMAN_FPNDISPU | Define Number Ranges for Dispute Cases | 103646 | FI-CA | FI-CA-2CL |
| SAP_CA_BC_IC_LND_FIN_FICA_PC | Contract Accounting - Configuration | S_ER1_70000062 | S_ER1_70000062_TRAN | _FICABFGFTD_FQC002 | Define Determination of Reporting Key | 102664 | FI-CA | FI-CA-2CL |
| SAP_CA_BC_IC_LND_FIN_FICA_PC | Contract Accounting - Configuration | FQZL |  | _FICABTPY_FQZL | Define Accounts for Payment Program | 102217 | FI-CA | FI-CA-2CL |
| SAP_CA_BC_IC_LND_FIN_FICA_PC | Contract Accounting - Configuration | S_KK4_74002112 | S_KK4_74002112_TRAN | _FICABTDU_VC_TFK047A | Configure Dunning Procedure |  | FI-CA | FI-CA-2CL |
| SAP_CA_BC_IC_LND_FIN_FICA_PC | Contract Accounting - Configuration | S_ER1_70000097 | S_ER1_70000097_TRAN | _FICABTPY_FQ1153 | Define Specifications for Automatic Returns Posting | 103100 | FI-CA | FI-CA-2CL |
| SAP_CA_BC_IC_LND_FIN_FICA_PC | Contract Accounting - Configuration | S_KK4_74002202 | S_KK4_74002202_TRAN | _FICAINCM_V_TFK036S | Define Alternative Planning Levels for Locks | 101887 | FI-CA | FI-CA-2CL |
| SAP_CA_BC_IC_LND_FIN_FICA_PC | Contract Accounting - Configuration | S_KK4_74002465 | S_KK4_74002465_TRAN | _FICABTTP_FQZ16 | Define Specifications and Default Values for Transfer | 103416 | FI-CA | FI-CA-2CL |
| SAP_CA_BC_IC_LND_FIN_FICA_PC | Contract Accounting - Configuration | S_EAI_74002830 | S_EAI_74002830_TRAN | _FICABTDU_FQCG | Define Default Values for Contract Account Group and Strategy | 103567 | FI-CA | FI-CA-2CL |
| SAP_CA_BC_IC_LND_FIN_FICA_PC | Contract Accounting - Configuration | S_ER1_70000199 | S_ER1_70000199_TRAN | _FICADC_TFKDISCOCTRL | Configure Disconnection and Reconnection of Services | 103535 | FI-CA | FI-CA-2CL |
| SAP_CA_BC_IC_LND_FIN_FICA_PC | Contract Accounting - Configuration | S_KK4_74002125 | S_KK4_74002125_TRAN | _FICABTIC_TFK056C | Define Clearing Reasons for Which Interest Is not Calculated | 102069 | FI-CA | FI-CA-2CL |
| SAP_CA_BC_IC_LND_FIN_FICA_PC | Contract Accounting - Configuration | S_KK4_74002460 | S_KK4_74002460_TRAN | _FICABFDP_VC_TFKCOK | Define CO Account Assignment Keys | 101248 | FI-CA | FI-CA-2CL |
| SAP_CA_BC_IC_LND_FIN_FICA_PC | Contract Accounting - Configuration | S_ER1_70000242 | S_ER1_70000242_TRAN | _FICADM_FICADMREASON | Create Values for "Reason" Attribute | 103648 | FI-CA | FI-CA-2CL |
| SAP_CA_BC_IC_LND_FIN_FICA_PC | Contract Accounting - Configuration | S_ER1_70000059 | S_ER1_70000059_TRAN | _FICAPV_FQ0500 | Define Specifications for Derivation of Standard Account Assignment | 102679 | FI-CA | FI-CA-2CL |
| SAP_CA_BC_IC_LND_FIN_FICA_PC | Contract Accounting - Configuration | S_KK4_74002177 | S_KK4_74002177_TRAN | _FICABTSE_FQI7 | Define Specifications for Cash Security Deposit Int. Calc. (Mass Proc.) | 103483 | FI-CA | FI-CA-2CL |
| SAP_CA_BC_IC_LND_FIN_FICA_PC | Contract Accounting - Configuration | S_EMI_14000091 | S_EMI_14000091_TRAN | _FICASEPA_VTFK000SEP | Enter General Specifications for SEPA | 102219 | FI-CA | FI-CA-2CL |
| SAP_CA_BC_IC_LND_FIN_FICA_PC | Contract Accounting - Configuration | S_KK4_74002121 | S_KK4_74002121_TRAN | _FICABTDU_V_TFK047F | Define Dunning Grouping | 101963 | FI-CA | FI-CA-2CL |
| SAP_CA_BC_IC_LND_FIN_FICA_PC | Contract Accounting - Configuration | S_KK4_74002204 | S_KK4_74002204_TRAN | _FICAINGL_FQZE | Define Posting Specifications for General Ledger Transfer | 101886 | FI-CA | FI-CA-2CL |
| SAP_CA_BC_IC_LND_FIN_FICA_PC | Contract Accounting - Configuration | S_ER9_52000740 | S_ER9_52000740_TRAN | _FICABTRE_VCTFK045AC | Configure Returns Reasons | 102269 | FI-CA | FI-CA-2CL |
| SAP_CA_BC_IC_LND_FIN_FICA_PC | Contract Accounting - Configuration | S_ER1_70000081 | S_ER1_70000081_TRAN | _FICABTDCSV_FQ1291 | Maintain Alternative Accounts for Resetting Flat-Rate Value Adjustments | 102719 | FI-CA | FI-CA-2CL |
| SAP_CA_BC_IC_LND_FIN_FICA_PC | Contract Accounting - Configuration | S_KK4_74002420 | S_KK4_74002420_TRAN | _FICABFCA_TFK002A | Configure Contract Acct Categories and Assign Number Ranges | 101243 | FI-CA | FI-CA-2CL |
| SAP_CA_BC_IC_LND_FIN_FICA_PC | Contract Accounting - Configuration | S_KK4_74002108 | S_KK4_74002108_TRAN | _FICABTPY_V_TFK008 | Define Payment Lock Reasons | 102545 | FI-CA | FI-CA-2CL |
| SAP_CA_BC_IC_LND_FIN_FICA_PC | Contract Accounting - Configuration | S_KK4_74002101 | S_KK4_74002101_TRAN | _FICA_BTPY_TFK042M | Define Bank User Numbers for Payment Medium | 101955 | FI-CA | FI-CA-2CL |
| SAP_CA_BC_IC_LND_FIN_FICA_PC | Contract Accounting - Configuration | S_KK4_74002464 | S_KK4_74002464_TRAN | _FICABTTP_TFK051A | Define Transfer Reasons | 103413 | FI-CA | FI-CA-2CL |
| SAP_CA_BC_IC_LND_FIN_FICA_PC | Contract Accounting - Configuration | S_EAI_74002831 | S_EAI_74002831_TRAN | _FICABTDU_V_TFK041C | Assign Account Categories to Master Data Groups | 103568 | FI-CA | FI-CA-2CL |
| SAP_CA_BC_IC_LND_FIN_FICA_PC | Contract Accounting - Configuration | S_ER1_70000200 | S_ER1_70000200_TRAN | _FICADC_FKK_DISCO_NR | Check Number Ranges for Disconnection and Reconnection Requests | 103534 | FI-CA | FI-CA-2CL |
| SAP_CA_BC_IC_LND_FIN_FICA_PC | Contract Accounting - Configuration | S_ER1_70000102 | S_ER1_70000102_TRAN | _FICAINGL_VTFK001CGL | Define Direct G/L Transfer for Document Origins | 102972 | FI-CA | FI-CA-2CL |
| SAP_CA_BC_IC_LND_FIN_FICA_PC | Contract Accounting - Configuration | S_KK4_74002126 | S_KK4_74002126_TRAN | _FICABTIC_FQI4 | Define Specifications for Interest Calculation | 102202 | FI-CA | FI-CA-2CL |
| SAP_CA_BC_IC_LND_FIN_FICA_PC | Contract Accounting - Configuration | S_ER1_70000060 | S_ER1_70000060_TRAN | _FICAPV_FPN_VT | Define Number Range | 102680 | FI-CA | FI-CA-2CL |
| SAP_CA_BC_IC_LND_FIN_FICA_PC | Contract Accounting - Configuration | S_ER9_52000846 | S_ER9_52000846_TRAN | _FICABTPY_FQ1152 | Specifications for Billing Document Posting | 102547 | FI-CA | FI-CA-2CL |
| SAP_CA_BC_IC_LND_FIN_FICA_PC | Contract Accounting - Configuration | S_KK4_74002169 | S_KK4_74002169_TRAN | _FICABTPY_FQZT | Define Clearing Account for Check Deposit | 102266 | FI-CA | FI-CA-2CL |
| SAP_CA_BC_IC_LND_FIN_FICA_PC | Contract Accounting - Configuration | S_KK4_74002118 | S_KK4_74002118_TRAN | _FICABTDU_FQZ06 | Specifications for Automatically Deactivating Installment Plans | 102253 | FI-CA | FI-CA-2CL |
| SAP_CA_BC_IC_LND_FIN_FICA_PC | Contract Accounting - Configuration | S_KK4_74002165 | S_KK4_74002165_TRAN | _FICABTPY_FQZJ | Define Clarification Account | 102267 | FI-CA | FI-CA-2CL |
| SAP_CA_BC_IC_LND_FIN_FICA_PC | Contract Accounting - Configuration | S_KK4_74002164 | S_KK4_74002164_TRAN | _FICABPTY_TFK020K | Define Short Account Assignments for Transfer Postings |  | FI-CA | FI-CA-2CL |
| SAP_CA_BC_IC_LND_FIN_FICA_PC | Contract Accounting - Configuration | S_ER1_70000040 | S_ER1_70000040_TRAN | _FICAPDCE_TFK020K | Define Short Account Assignments for Transfer Postings | 102428 | FI-CA | FI-CA-2CL |
| SAP_CA_BC_IC_LND_FIN_FICA_PC | Contract Accounting - Configuration | S_ER1_70000004 | S_ER1_70000004_TRAN | _FICACLFC_VC_TFK044F | Define Valuation Plan Variants | 102064 | FI-CA | FI-CA-2CL |
| SAP_CA_BC_IC_LND_FIN_FICA_PC | Contract Accounting - Configuration | S_KK4_74002110 | S_KK4_74002110_TRAN | _FICABTPY_FQZL | Define Accounts for Payment Program | 102217 | FI-CA | FI-CA-2CL |
| SAP_CA_BC_IC_LND_FIN_FICA_PC | Contract Accounting - Configuration | S_ER1_70000041 | S_ER1_70000041_TRAN | _FICAPDCE_TFK012 | Define Bank Clearing Account | 102466 | FI-CA | FI-CA-2CL |
| SAP_CA_BC_IC_LND_FIN_FICA_PC | Contract Accounting - Configuration | S_EMO_14000325 | S_EMO_14000325_TRAN | _FICACVORG_TFKC_HVTV | Define and Parameterize External Transactions | 101245 | FI-CA | FI-CA-2CL |
| SAP_CA_BC_IC_LND_FIN_FICA_PC | Contract Accounting - Configuration | S_ER9_52000870 | S_ER9_52000870_TRAN | _FICABTPY_FQ1155 | Define Specifications for Posting Exchange Rate Differences | 102549 | FI-CA | FI-CA-2CL |
| SAP_CA_BC_IC_LND_FIN_FICA_PC | Contract Accounting - Configuration | S_KK4_74002205 | S_KK4_74002205_TRAN | _FICAINSD_FQC1210 | Derive Document Type from SD Billing Doc Data | 103207 | FI-CA | FI-CA-2CL |
| SAP_CA_BC_IC_LND_FIN_FICA_PC | Contract Accounting - Configuration | S_KK4_74002099 | S_KK4_74002099_TRAN | _FICABTPY_VC_TFK042E | Define Specifications for Paying Company Code | 101251 | FI-CA | FI-CA-2CL |
| SAP_CA_BC_IC_LND_FIN_FICA_PC | Contract Accounting - Configuration | S_KK4_74002089 | S_KK4_74002089_TRAN | _FICABTPYPC_FQZV | Define Accounts for Payment Card Institute | 101957 | FI-CA | FI-CA-2CL |
| SAP_CA_BC_IC_LND_FIN_FICA_PC | Contract Accounting - Configuration | S_ER9_52000871 | S_ER9_52000871_TRAN | _FICABTPY_FQ1156 | Define Accounts for Posting for Exchange Rate Differences | 102550 | FI-CA | FI-CA-2CL |
| SAP_CA_BC_IC_LND_FIN_FICA_PC | Contract Accounting - Configuration | S_KK4_74002163 | S_KK4_74002163_TRAN | _FICABTPY_FQZN | Define Specifications for Repayment of Incoming Payments | 102268 | FI-CA | FI-CA-2CL |
| SAP_CA_BC_IC_LND_FIN_FICA_PC | Contract Accounting - Configuration | FQZK |  | _FICABFDP_FQZK | Define Default Values for Reversal | 102332 | FI-CA | FI-CA-2CL |
| SAP_CA_BC_IC_LND_FIN_FICA_PC | Contract Accounting - Configuration | S_ER9_52000869 | S_ER9_52000869_TRAN | _FICABTPY_FQ1154 | Define Specifications for Charge Postings | 102548 | FI-CA | FI-CA-2CL |
| SAP_CA_BC_IC_LND_FIN_FICA_PC | Contract Accounting - Configuration | S_KK4_74002506 | S_KK4_74002506_TRAN | _FICABFOI_VC_TFK119 | Define Amount Check Group | 102870 | FI-CA | FI-CA-2CL |
| SAP_CA_BC_IC_LND_FIN_FICA_PC | Contract Accounting - Configuration | S_KK4_74002417 | S_KK4_74002417_TRAN | _FICABFOI_FQZO | Define Default Values for Resetting Clearing | 102319 | FI-CA | FI-CA-2CL |
| SAP_CA_BC_IC_LND_FIN_FICA_PC | Contract Accounting - Configuration | S_ER1_15000001 | S_ER1_15000001_TRAN | _FICABTDU_V_TFK047X | Define Collection Strategy | 103562 | FI-CA | FI-CA-2CL |
| SAP_CA_BC_IC_LND_FIN_FICA_PC | Contract Accounting - Configuration | S_EMO_14000329 | S_EMO_14000329_TRAN | _FICACBFDP_FQC001 | Define Account Determination Data Relevant to Transactions | 102293 | FI-CA | FI-CA-2CL |
| SAP_CA_BC_IC_LND_FIN_FICA_PC | Contract Accounting - Configuration | S_KK4_74002206 | S_KK4_74002206_TRAN | _FICAINSD_FQC1200 | Derive Main/Subtransaction from SD Information | 103206 | FI-CA | FI-CA-2CL |
| SAP_CA_BC_IC_LND_FIN_FICA_PC | Contract Accounting - Configuration | S_ER1_70000023 | S_ER1_70000023_TRAN | _FICABTDU_VCTFK047EC | Configure Charge Schedules for Dunning Procedure | 102317 | FI-CA | FI-CA-2CL |
| SAP_CA_BC_IC_LND_FIN_FICA_PC | Contract Accounting - Configuration | S_EMI_14000004 | S_EMI_14000004_TRAN | _FICAPV_TFK_VT_TRT | Define the Type of ID | 102678 | FI-CA | FI-CA-2CL |
| SAP_CA_BC_IC_LND_FIN_FICA_PC | Contract Accounting - Configuration | S_ER1_70000113 | S_ER1_70000113_TRAN | _FICAML_TFK006ML | Make Settings for SAP Cash Application for Contract Accounting | 103245 | FI-CA | FI-CA-2CL |

## Connections
- part-of :: [[_cluster]]
- related-to :: [[01-solution-foundation-and-platform/sscui-list-en-xx-sap-s-4hana-cloud-2608-configuration-2-part-35]]
- related-to :: [[01-solution-foundation-and-platform/sscui-list-en-xx-sap-s-4hana-cloud-2608-configuration-2-part-37]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Configuration/SSCUI_List_EN_XX.xlsm` — lines 7497–8758 of the extracted text · extracted with `xlsx2md` · 9,788,312 chars in the whole document
