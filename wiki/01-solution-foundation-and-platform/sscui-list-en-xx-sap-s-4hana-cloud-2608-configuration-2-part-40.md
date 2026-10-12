---
id: 01-solution-foundation-and-platform/sscui-list-en-xx-sap-s-4hana-cloud-2608-configuration-2-part-40
title: SSCUI List EN XX (SAP S/4HANA Cloud 2608 Configuration) (SSCUI_List_EN_XX) — part 40 of 40
description: "SAP S/4HANA Cloud 2608 SSCUI list; final part: business catalog to IMG activity mappings plus expert-configuration incident templates."
cluster: 01-solution-foundation-and-platform
tags: [kb/solution-foundation-and-platform, topic/sscui-configuration-activity-list]
aliases: []
keywords: [Self-Service Configuration (SSCUI) Activity List, expert configuration, business catalog transactions, currency codes, depreciation keys, asset revaluation, storage types, storage locations, warehouse queues, material groups]
sources: ["raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Configuration/SSCUI_List_EN_XX.xlsm#lines-12532-13731"]
confidence: high
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-2
topic: 01-solution-foundation-and-platform/sscui-configuration-activity-list
language: EN
part: 40/40
created: 2026-10-12
updated: 2026-10-12
---

# SSCUI List EN XX (SAP S/4HANA Cloud 2608 Configuration) (SSCUI_List_EN_XX) — part 40 of 40

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Configuration/SSCUI_List_EN_XX.xlsm`, part 40 of 40 (lines 12532–13731 of the extracted text), extracted with `xlsx2md`. Grouped under **Self-Service Configuration (SSCUI) Activity List** in Solution Foundation and Platform. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

| SAP_CA_BC_IC_LND_EAM_DSP_PC | Enterprise Asset Management - Configuration Display | EAM_JOBPCKGBLD |  | EAM_JOBPCKGBLD | Maintain Work Pack Number Range |  | PM | PM-WOC-MO-PRI-2CL |
| SAP_CA_BC_IC_LND_EAM_DSP_PC | Enterprise Asset Management - Configuration Display | IP21 |  | SIMG_CFMENUOLIPIP21 | Define Number Ranges for Maintenance Items |  | PM | PM-2CL |
| SAP_CA_BC_IC_LND_EAM_DSP_PC | Enterprise Asset Management - Configuration Display | IP20 |  | SIMG_CFMENUOLIPIP20 | Define Number Ranges for Maintenance Plans |  | PM | PM-2CL |
| SAP_CA_BC_IC_LND_EAM_DSP_PC | Enterprise Asset Management - Configuration Display | OIZM |  | SIMG_CFMENUOLIPOIZM1 | Configure Formula Definition |  | PM | PM-2CL |
| SAP_CA_BC_IC_LND_EAM_DSP_PC | Enterprise Asset Management - Configuration Display | OIL0 |  | SIMG_CFMENUOLIPOIL0 | Define Number Ranges for Task Lists for Functional Locations |  | PM | PM-2CL |
| SAP_CA_BC_IC_LND_EAM_DSP_PC | Enterprise Asset Management - Configuration Display | OIL5 |  | SIMG_CFMENUOLIPOIL5 | Define Number Ranges for Equipment Task Lists |  | PM | PM-2CL |
| SAP_CA_BC_IC_LND_GLOFI_DSP_PC | Globalization Financials - Configuration Display | S_ER9_11001798 | S_ER9_11001798_03_TRAN | TAX_FFD_BUSTRANS | Define Business Transaction Types |  | FI-LOC-IAM | FI-LOC-FI-HU |
| SAP_CA_BC_IC_LND_GLOFI_DSP_PC | Globalization Financials - Configuration Display | SI_CBR_IINSC |  | FIIS_SI_CBR_IINS | Define International Institution Codes |  | FI-LOC-IAM | FI-LOC-FI-SI |
| SAP_CA_BC_IC_LND_GLOFI_DSP_PC | Globalization Financials - Configuration Display | IE_ERR_EXP_CAT |  | IEERREXPCAT | Enumerate the Available Expense Type Categories |  | FI-LOC-IAM | FI-LOC-FI-IE |
| SAP_CA_BC_IC_LND_GLOFI_DSP_PC | Globalization Financials - Configuration Display | S_ER1_70000909 | S_ER1_70000909_TRAN | IEERREXPCAT | Enumerate the Available Expense Type Categories |  | FI-LOC-IAM | FI-LOC-FI-IE |
| SAP_CA_BC_IC_LND_GLOFI_DSP_PC | Globalization Financials - Configuration Display | /TMF/70000077 | TMF_REP_CUST_VC_TRAN | /TMF/REP_CUST_VC | Define Reporting Framework Settings |  | FI-LOC-IAM | FI-LOC-FI-BR-ACR |
| SAP_CA_BC_IC_LND_GLOFI_DSP_PC | Globalization Financials - Configuration Display | SI_BST_CODE |  | FIIS_SI_BST_CODE | Define BST Code |  | FI-LOC-IAM | FI-LOC-FI-SI |
| SAP_CA_BC_IC_LND_GLOFI_DSP_PC | Globalization Financials - Configuration Display | IE_ERR_EXP_SUBCAT |  | IEERREXPSUBCAT | Enumerate the Available Expense Type Subcategories |  | FI-LOC-IAM | FI-LOC-FI-IE |
| SAP_CA_BC_IC_LND_GLOFI_DSP_PC | Globalization Financials - Configuration Display | S_ER1_70000978 | S_ER1_70000978_TRAN | FIIS_SI_CBR_IINS | Define International Institution Codes |  | FI-LOC-IAM | FI-LOC-FI-SI |
| SAP_CA_BC_IC_LND_GLOFI_DSP_PC | Globalization Financials - Configuration Display | S_ER1_70000970 | S_ER1_70000970_TRAN | FIIS_SI_BST_CODE | Define BST Code |  | FI-LOC-IAM | FI-LOC-FI-SI |
| SAP_CA_BC_IC_LND_GLOFI_DSP_PC | Globalization Financials - Configuration Display | S_ER1_70000910 | S_ER1_70000910_TRAN | IEERREXPSUBCAT | Enumerate the Available Expense Type Subcategories |  | FI-LOC-IAM | FI-LOC-FI-IE |
| SAP_CA_BC_IC_LND_GLOFI_DSP_PC | Globalization Financials - Configuration Display | SI_SFR_SBOX |  | FIIS_SI_SFR_SBOX | Assign Financial Sector to Financial Box |  | FI-LOC-IAM | FI-LOC-FI-SI |
| SAP_CA_BC_IC_LND_GLOFI_DSP_PC | Globalization Financials - Configuration Display | SI_SFR_IBOX |  | FIIS_SI_SFR_IBOX | Assign Financial Instrument to Financial Box |  | FI-LOC-IAM | FI-LOC-FI-SI |
| SAP_CA_BC_IC_LND_GLOFI_DSP_PC | Globalization Financials - Configuration Display | SI_KRD_MTTY |  | FIIS_SI_KRD_MRTY | Define Financial Instrument Maturity |  | FI-LOC-IAM | FI-LOC-FI-SI |
| SAP_CA_BC_IC_LND_GLOFI_DSP_PC | Globalization Financials - Configuration Display | SI_KRD_INTY |  | FIIS_SI_KRD_INTY | Define Financial Instrument Types |  | FI-LOC-IAM | FI-LOC-FI-SI |
| SAP_CA_BC_IC_LND_GLOFI_DSP_PC | Globalization Financials - Configuration Display | SI_KRD_CAPR |  | FIIS_SI_KRD_CAPR | Define Capital Relationship Between the Debtor and the Creditor |  | FI-LOC-IAM | FI-LOC-FI-SI |
| SAP_CA_BC_IC_LND_GLOFI_DSP_PC | Globalization Financials - Configuration Display | SI_CBR_SCTR |  | FIIS_SI_CBR_SECT | Define Financial Sectors |  | FI-LOC-IAM | FI-LOC-FI-SI |
| SAP_CA_BC_IC_LND_GLOFI_DSP_PC | Globalization Financials - Configuration Display | S_ER1_70000979 | S_ER1_70000979_TRAN | FIIS_SI_CBR_SECT | Define Financial Sectors |  | FI-LOC-IAM | FI-LOC-FI-SI |
| SAP_CA_BC_IC_LND_GLOFI_DSP_PC | Globalization Financials - Configuration Display | S_ER1_70000976 | S_ER1_70000976_TRAN | FIIS_SI_KRD_MRTY | Define Financial Instrument Maturity |  | FI-LOC-IAM | FI-LOC-FI-SI |
| SAP_CA_BC_IC_LND_GLOFI_DSP_PC | Globalization Financials - Configuration Display | S_ER1_70000975 | S_ER1_70000975_TRAN | FIIS_SI_KRD_INTY | Define Financial Instrument Types |  | FI-LOC-IAM | FI-LOC-FI-SI |
| SAP_CA_BC_IC_LND_GLOFI_DSP_PC | Globalization Financials - Configuration Display | S_ER1_70000974 | S_ER1_70000974_TRAN | FIIS_SI_KRD_CAPR | Define Capital Relationship Between the Debtor and the Creditor |  | FI-LOC-IAM | FI-LOC-FI-SI |
| SAP_CA_BC_IC_LND_GLOFI_DSP_PC | Globalization Financials - Configuration Display | S_ER1_70000929 | S_ER1_70000929_TRAN | FIIS_SI_SFR_SBOX | Assign Financial Sector to Financial Box |  | FI-LOC-IAM | FI-LOC-FI-SI |
| SAP_CA_BC_IC_LND_GLOFI_DSP_PC | Globalization Financials - Configuration Display | S_ER1_70000924 | S_ER1_70000924_TRAN | FIIS_SI_SFR_IBOX | Assign Financial Instrument to Financial Box |  | FI-LOC-IAM | FI-LOC-FI-SI |
| SAP_CA_BC_IC_LND_GLOFI_DSP_PC | Globalization Financials - Configuration Display | S_PCO_36000445 | S_PCO_36000445_03_TRAN | V_T007BE | Specify When Bills of Exchange Are Recognized |  | FI-LOC-IAM | FI-GL-GL-F1 |
| SAP_CA_BC_IC_LND_GLOFI_DSP_PC | Globalization Financials - Configuration Display | S_PCO_36000430 | S_PCO_36000430_03_TRAN | J_3RCLASSSAKNR | Classify G/L Accounts |  | FI-LOC-IAM | FI-LOC-FI-RU |
| SAP_CA_BC_IC_LND_GLOFI_DSP_PC | Globalization Financials - Configuration Display | S_PCO_36000427 | S_PCO_36000427_03_TRAN | J_3RCLASSBWASL | Classify Transaction Types |  | FI-LOC-IAM | FI-LOC-FI-RU |
| SAP_CA_BC_IC_LND_GLOFI_DSP_PC | Globalization Financials - Configuration Display | S_PCO_36000411 | S_PCO_36000411_03_TRAN | J_3RFDEPRGROUP | Define Depreciation Groups |  | FI-LOC-IAM | FI-LOC-FI-RU |
| SAP_CA_BC_IC_LND_GLOFI_DSP_PC | Globalization Financials - Configuration Display | S_P7D_67000083 | S_P7D_67000083_03_TRAN | J_3ROS6_TB5BWASL | Maintain Transaction Types for Investments and Improvements |  | FI-LOC-IAM | FI-LOC-FI-RU |
| SAP_CA_BC_IC_LND_GLOFI_DSP_PC | Globalization Financials - Configuration Display | S_ERX_29000073 | S_ERX_29000073_03_TRAN | FIKZV_TURNCODMAP | Assign Taxable Turnover Type Codes to Tax Codes |  | FI-LOC-IAM | FI-LOC-FI-KZ |
| SAP_CA_BC_IC_LND_GLOFI_DSP_PC | Globalization Financials - Configuration Display | S_ER9_52001486 | S_ER9_52001486_03_TRAN | FIRUV_SD_STGRD | Enable Saving of Reversal Reasons for Billing Documents |  | FI-LOC-IAM | FI-LOC-LO-RU |
| SAP_CA_BC_IC_LND_GLOFI_DSP_PC | Globalization Financials - Configuration Display | S_ER9_11002553 | S_ER9_11002553_03_TRAN | FIRUVC_OFFS_GROUP_UA | Define Field Sets for Grouping |  | FI-LOC-IAM | FI-LOC-FI-RU |
| SAP_CA_BC_IC_LND_GLOFI_DSP_PC | Globalization Financials - Configuration Display | S_ER9_11001621 | S_ER9_11001621_03_TRAN | FIRUV_EACU_CNTRY | Specify Countries/Regions for Customs Union |  | FI-LOC-IAM | FI-LOC-FI-RU |
| SAP_CA_BC_IC_LND_GLOFI_DSP_PC | Globalization Financials - Configuration Display | S_ER9_11001186 | S_ER9_11001186_03_TRAN | FIRUV_SDCOMTRTXT | Maintain Text Object IDs for SD Documents (Commission) |  | FI-LOC-IAM | FI-LOC-FI-RU |
| SAP_CA_BC_IC_LND_GLOFI_DSP_PC | Globalization Financials - Configuration Display | S_ER9_11000480 | S_ER9_11000480_03_TRAN | FIRUV_REP_PERIOD | Maintain Reporting Periods |  | FI-LOC-IAM | FI-LOC-FI-RU |
| SAP_CA_BC_IC_LND_GLOFI_DSP_PC | Globalization Financials - Configuration Display | S_ER9_11001160 | S_ER9_11001160_03_TRAN | FIRUV_RECON_CONT | Split Reconciliation Reports by Contract | 102946 | FI-LOC-IAM | FI-LOC-FI-RU |
| SAP_CA_BC_IC_LND_GLOFI_DSP_PC | Globalization Financials - Configuration Display | S_ER9_11001185 | S_ER9_11001185_03_TRAN | FIRUV_FICOMTRTXT | Maintain Text Object IDs for FI Invoices (Commission) |  | FI-LOC-IAM | FI-LOC-FI-RU |
| SAP_CA_BC_IC_LND_GLOFI_DSP_PC | Globalization Financials - Configuration Display | S_ER9_11000473 | S_ER9_11000473_03_TRAN | FIRUV_BILDOCTXT | Maintain Text Object IDs for SD Documents |  | FI-LOC-IAM | FI-LOC-FI-RU |
| SAP_CA_BC_IC_LND_GLOFI_DSP_PC | Globalization Financials - Configuration Display | S_EBJ_98000038 | S_EBJ_98000038_03_TRAN | J_3RVDEPB_BWASL | Define Depreciation Bonus Transaction Types |  | FI-LOC-IAM | FI-LOC-FI-RU |
| SAP_CA_BC_IC_LND_GLOFI_DSP_PC | Globalization Financials - Configuration Display | S_EBJ_45000099 | S_EBJ_45000099_03_TRAN | J_3R_TTAX_ECOEFV | Define Tax Coefficients for Expensive Vehicles |  | FI-LOC-IAM | FI-LOC-FI-RU |
| SAP_CA_BC_IC_LND_GLOFI_DSP_PC | Globalization Financials - Configuration Display | S_EBJ_45000098 | S_EBJ_45000098_03_TRAN | J_3R_TTAX_ECATV | Maintain Vehicle Price Categories |  | FI-LOC-IAM | FI-LOC-FI-RU |
| SAP_CA_BC_IC_LND_GLOFI_DSP_PC | Globalization Financials - Configuration Display | S_EBJ_45000064 | S_EBJ_45000064_03_TRAN | V_J_3RFREGREVTXT | Maintain Text Object IDs for Revised Documents |  | FI-LOC-IAM | FI-LOC-FI-RU |
| SAP_CA_BC_IC_LND_GLOFI_DSP_PC | Globalization Financials - Configuration Display | S_EB5_05000481 | S_EB5_05000481_03_TRAN | J_3RSCCDTYPE | Define Customs Declaration Types |  | FI-LOC-IAM | FI-LOC-SD-RU |
| SAP_CA_BC_IC_LND_GLOFI_DSP_PC | Globalization Financials - Configuration Display | S_EB5_05000321 | S_EB5_05000321_03_TRAN | J_3RF_XNEGP_ACT | Activate Negative Posting for Country/Region |  | FI-LOC-IAM | FI-LOC-FI-RU |
| SAP_CA_BC_IC_LND_GLOFI_DSP_PC | Globalization Financials - Configuration Display | S_EB5_05000307 | S_EB5_05000307_03_TRAN | J_3RNEGPAFABE | Permit Negative Posting |  | FI-LOC-IAM | FI-LOC-FI-RU |
| SAP_CA_BC_IC_LND_GLOFI_DSP_PC | Globalization Financials - Configuration Display | S_ER9_11001021 | S_ER9_11001021_03_TRAN | J_3RF_101_VAL_V | Maintain Payer Statuses |  | FI-LOC-IAM | FI-LOC-FI-RU |
| SAP_CA_BC_IC_LND_GLOFI_DSP_PC | Globalization Financials - Configuration Display | S_ER9_11001380 | S_ER9_11001380_03_TRAN | GLOFAAV_RUTAX0 | Define General Parameters of Depreciation Bonus |  | FI-LOC-IAM | FI-LOC-AA-RU |
| SAP_CA_BC_IC_LND_GLOFI_DSP_PC | Globalization Financials - Configuration Display | S_ER9_11001294 | S_ER9_11001294_03_TRAN | J_3RF_PAYNUMV | Maintain Document Types for Source Documents |  | FI-LOC-IAM | FI-LOC-FI-RU |
| SAP_CA_BC_IC_LND_GLOFI_DSP_PC | Globalization Financials - Configuration Display | S_ER9_11001223 | S_ER9_11001223_03_TRAN | J_3RFREGCUSINC_RU | Automatic Registration of Incoming Invoices (Cloud) |  | FI-LOC-IAM | FI-LOC-FI-RU |
| SAP_CA_BC_IC_LND_GLOFI_DSP_PC | Globalization Financials - Configuration Display | S_ER9_11001561 | S_ER9_11001561_03_TRAN | J_3RF_020_VAL_V | Maintain Payment Purposes |  | FI-LOC-IAM | FI-LOC-FI-RU |
| SAP_CA_BC_IC_LND_GLOFI_DSP_PC | Globalization Financials - Configuration Display | S_ER9_11001020 | S_ER9_11001020_03_TRAN | J_3RF_PAYTV | Maintain Payment Types |  | FI-LOC-IAM | FI-LOC-FI-RU |
| SAP_CA_BC_IC_LND_GLOFI_DSP_PC | Globalization Financials - Configuration Display | S_ER9_11001379 | S_ER9_11001379_03_TRAN | GLOFAAVC_RUDBGR | Define Percentage Groups for Depreciation Bonus Calculation |  | FI-LOC-IAM | FI-LOC-AA-RU |
| SAP_CA_BC_IC_LND_GLOFI_DSP_PC | Globalization Financials - Configuration Display | S_ER9_11001019 | S_ER9_11001019_03_TRAN | J_3RF_PAYRV | Maintain Payment Reasons |  | FI-LOC-IAM | FI-LOC-FI-RU |
| SAP_CA_BC_IC_LND_GLOFI_DSP_PC | Globalization Financials - Configuration Display | S_ER9_11001151 | S_ER9_11001151_03_TRAN | V_T007K_RUSSIA | Group Tax Base Balances |  | FI-LOC-IAM | FI-LOC-FI-RU |
| SAP_CA_BC_IC_LND_GLOFI_DSP_PC | Globalization Financials - Configuration Display | S_ER9_11000952 | S_ER9_11000952_03_TRAN | J_3RJ_CNTRY | Maintain Countries/Regions |  | FI-LOC-IAM | FI-LOC-FI-RU |
| SAP_CA_BC_IC_LND_GLOFI_DSP_PC | Globalization Financials - Configuration Display | S_ER9_11000950 | S_ER9_11000950_03_TRAN | J_3RJ_UOM | Maintain OKEI Codes |  | FI-LOC-IAM | FI-LOC-FI-RU |
| SAP_CA_BC_IC_LND_GLOFI_DSP_PC | Globalization Financials - Configuration Display | S_ER9_11000729 | S_ER9_11000729_03_TRAN | FIRUV_VATOPTYP | Maintain Operation Type Codes |  | FI-LOC-IAM | FI-LOC-FI-RU |
| SAP_CA_BC_IC_LND_GLOFI_DSP_PC | Globalization Financials - Configuration Display | S_ER9_11000472 | S_ER9_11000472_03_TRAN | V_J_3RFREGCUSTXT1 | Maintain Text Object IDs for FI Documents |  | FI-LOC-IAM | FI-LOC-FI-RU |
| SAP_CA_BC_IC_LND_GLOFI_DSP_PC | Globalization Financials - Configuration Display | S_ER9_11000362 | S_ER9_11000362_03_TRAN | J_3RS_REG_TR_TYV | Maintain Transportation Types |  | FI-LOC-IAM | FI-LOC-FI-RU |
| SAP_CA_BC_IC_LND_GLOFI_DSP_PC | Globalization Financials - Configuration Display | J_3RF_IMNT | J_3RF_IMNT_03_TRAN | J_3RF_IMNT | Maintain Number Ranges for Internal Numbers of Import Notification |  | FI-LOC-IAM | FI-LOC-SD-RU |
| SAP_CA_BC_IC_LND_GLOFI_DSP_PC | Globalization Financials - Configuration Display | S_ER9_52003801 | S_ER9_52003801_03_TRAN | J_3RSCCD | Maintain Number Ranges for Internal Numbers of Export Customs Declarations |  | FI-LOC-IAM | FI-LOC-SD-RU |
| SAP_CA_BC_IC_LND_GLOFI_DSP_PC | Globalization Financials - Configuration Display | S_ER9_11000363 | S_ER9_11000363_03_TRAN | J_3RS_REG_RE_DOV | Maintain Transportation Document Types |  | FI-LOC-IAM | FI-LOC-FI-RU |
| SAP_CA_BC_IC_LND_GLOFI_DSP_PC | Globalization Financials - Configuration Display | S_AC0_52000714 | S_AC0_52000714_03_TRAN | J_3RKKRN_V1 | Define Preferred and Disallowed Pairs of G/L Accounts | 101865 | FI-LOC-IAM | FI-LOC-FI-RU |
| SAP_CA_BC_IC_LND_GLOFI_DSP_PC | Globalization Financials - Configuration Display | J_3RSCCD | J_3RSCCD_03_TRAN | J_3RSCCD | Maintain Number Ranges for Internal Numbers of Export Customs Declarations |  | FI-LOC-IAM | FI-LOC-SD-RU |
| SAP_CA_BC_IC_LND_GLOFI_DSP_PC | Globalization Financials - Configuration Display | S_ER9_52003858 | S_ER9_52003858_03_TRAN | J_3RF_IMNT | Maintain Number Ranges for Internal Numbers of Import Notification |  | FI-LOC-IAM | FI-LOC-SD-RU |
| SAP_CA_BC_IC_LND_GLOFI_DSP_PC | Globalization Financials - Configuration Display | S_EBJ_45000109 | S_EBJ_45000109_03_TRAN | J_3RF_IMCD | Assign Import Declaration Number Ranges |  | FI-LOC-IAM | FI-LOC-FI-RU |
| SAP_CA_BC_IC_LND_GLOFI_DSP_PC | Globalization Financials - Configuration Display | S_ER9_11000859 | S_ER9_11000859_03_TRAN | FIPL_INVTYPE_FI | Map Invoice Type for FI Invoices |  | FI-LOC-IAM | FI-LOC-FI-PL |
| SAP_CA_BC_IC_LND_GLOFI_DSP_PC | Globalization Financials - Configuration Display | J_3RF_IMCD | J_3RF_IMCD_03_TRAN |  |  |  | FI-LOC-IAM |  |
| SAP_CA_BC_IC_LND_GLOFI_DSP_PC | Globalization Financials - Configuration Display | S_ER9_11000860 | S_ER9_11000860_03_TRAN | FIPL_INVTYPE_SD | Map Invoice Type for SD Invoices |  | FI-LOC-IAM | FI-LOC-FI-PL |
| SAP_CA_BC_IC_LND_GLOFI_DSP_PC | Globalization Financials - Configuration Display | S_P9C_18000024 | S_P9C_18000024_03_TRAN | TAIWAN_005 | Maintain Document Classes for Taiwan |  | FI-LOC-IAM | FI-LOC-FI-TW |
| SAP_CA_BC_IC_LND_GLOFI_DSP_PC | Globalization Financials - Configuration Display | S_EBJ_98000688 | S_EBJ_98000688_03_TRAN | V_EINV_CUST_TW | Determine Customer Relevance for eInvoicing |  | FI-LOC-IAM | FI-LOC-FI-TW |
| SAP_CA_BC_IC_LND_GLOFI_DSP_PC | Globalization Financials - Configuration Display | S_EBJ_45000091 | S_EBJ_45000091_03_TRAN | V_J_3RFPARTN | Assign Partner Functions to Partner Roles |  | FI-LOC-IAM | FI-LOC-FI-RU |
| SAP_CA_BC_IC_LND_GLOFI_DSP_PC | Globalization Financials - Configuration Display | S_ER9_11000468 | S_ER9_11000468_03_TRAN | V_IDTW_GUI_D_OPT | Determine Deletion Option of Reversed Documents |  | FI-LOC-IAM | FI-LOC-FI-TW |
| SAP_CA_BC_IC_LND_GLOFI_DSP_PC | Globalization Financials - Configuration Display | S_EB5_05000524 | S_EB5_05000524_03_TRAN | IDDOCTYPCN | Assign Document Types to G/L Account Voucher Types |  | FI-LOC-IAM | FI-LOC-FI-CN |
| SAP_CA_BC_IC_LND_GLOFI_DSP_PC | Globalization Financials - Configuration Display | S_EB5_05000470 | S_EB5_05000470_03_TRAN | IDCN_V_REPFORM | Assign PDF Form to Programs |  | FI-LOC-IAM | FI-LOC-FI-CN |
| SAP_CA_BC_IC_LND_GLOFI_DSP_PC | Globalization Financials - Configuration Display | TXI_JOBNR |  | TXI_JOBNR | Define Number Range for Invoice Job Batches |  | FI-LOC-IAM | FI-LOC-TIM-CN |
| SAP_CA_BC_IC_LND_GLOFI_DSP_PC | Globalization Financials - Configuration Display | S_ER1_70001101 | S_ER1_70001101_TRAN | TXI_JOBNR | Define Number Range for Invoice Job Batches |  | FI-LOC-IAM | FI-LOC-TIM-CN |
| SAP_CA_BC_IC_LND_GLOFI_DSP_PC | Globalization Financials - Configuration Display | S_ER9_11001382 | S_ER9_11001382_TRAN | V_GLOFAA_JPCLK | Define Property Classification Keys |  | FI-LOC-IAM | FI-LOC-AA-JP |
| SAP_CA_BC_IC_LND_GLOFI_DSP_PC | Globalization Financials - Configuration Display | S_EBJ_98000869 | S_EBJ_98000869_TRAN | CIAP_C_ACC_SETT | Define Accounting Execution Settings |  | FI-LOC-IAM | FI-LOC-FI-BR |
| SAP_CA_BC_IC_LND_GLOFI_DSP_PC | Globalization Financials - Configuration Display | S_EBJ_98000661 | S_EBJ_98000661_TRAN | CIAP_C_PART_RET | Define Partial Retirement |  | FI-LOC-IAM | FI-LOC-FI-BR |
| SAP_CA_BC_IC_LND_GLOFI_DSP_PC | Globalization Financials - Configuration Display | S_AL0_96000809 | S_AL0_96000809_TRAN | J_1IN0002 | Activate Local Version India for Specific Fiscal Years |  | FI-LOC-IAM | FI-LOC-FI-IN |
| SAP_CA_BC_IC_LND_GLOFI_DSP_PC | Globalization Financials - Configuration Display | S_EB5_05000391 | S_EB5_05000391_TRAN | J_1IEWTCALID_N | Assign Factory Calendars to Section Codes |  | FI-LOC-IAM | FI-LOC-FI-IN |
| SAP_CA_BC_IC_LND_GLOFI_DSP_PC | Globalization Financials - Configuration Display | FIWTIE_RCT_CONTRACT |  | FIWTIE_RCT_CONTRACT | Maintain Number Range for Contract Creation |  | FI-LOC-IAM | FI-AP-AP-Q1 |
| SAP_CA_BC_IC_LND_GLOFI_DSP_PC | Globalization Financials - Configuration Display | S_ER9_11000643 | S_ER9_11000643_TRAN | FIWTIE_RCT_CONTRACT | Maintain Number Range for Contract Creation |  | FI-LOC-IAM | FI-AP-AP-Q1 |
| SAP_CA_BC_IC_LND_GLOFI_DSP_PC | Globalization Financials - Configuration Display | S_ER9_11001745 | S_ER9_11001745_03_TRAN | PAYREQN_V_REASON | Specify Payment Block Reason and Reversal Reason for Payment Requisitions |  | FI-LOC-IAM | FI-LOC-CM-CN |
| SAP_CA_BC_IC_LND_GLOFI_DSP_PC | Globalization Financials - Configuration Display | S_EIX_71000026 | S_EIX_71000026_03_TRAN | BOE_COUNT_OPTION | Maintain Settings for Count Management |  | FI-LOC-IAM | FI-LOC-CM-CN |
| SAP_CA_BC_IC_LND_GLOFI_DSP_PC | Globalization Financials - Configuration Display | S_EIX_71000023 | S_EIX_71000023_03_TRAN | V_BOE_C_AMOUNT | Maintain Maximum Amount for Bill of Exchange |  | FI-LOC-IAM | FI-LOC-CM-CN |
| SAP_CA_BC_IC_LND_GLOFI_DSP_PC | Globalization Financials - Configuration Display | FIWTIE_RCT_SIN |  | FIWTIE_RCT_SIN | Maintain Number Range for SIN Creation |  | FI-LOC-IAM | FI-AP-AP-Q1 |
| SAP_CA_BC_IC_LND_GLOFI_DSP_PC | Globalization Financials - Configuration Display | S_ER9_11001813 | S_ER9_11001813_TRAN | GLO_BUPLA_ACT_V | Maintain Scenarios for Activation |  | FI-LOC-IAM | FI-LOC-BUP |
| SAP_CA_BC_IC_LND_GLOFI_DSP_PC | Globalization Financials - Configuration Display | S_ER9_11001811 | S_ER9_11001811_TRAN | GLO_BUPLA_SVC_V | Register Country/Region Service Providers |  | FI-LOC-IAM | FI-LOC-BUP |
| SAP_CA_BC_IC_LND_GLOFI_DSP_PC | Globalization Financials - Configuration Display | S_ER9_11000644 | S_ER9_11000644_TRAN | FIWTIE_RCT_SIN | Maintain Number Range for SIN Creation |  | FI-LOC-IAM | FI-AP-AP-Q1 |
| SAP_CA_BC_IC_LND_GLOFI_DSP_PC | Globalization Financials - Configuration Display | S_EBJ_45000243 | S_EBJ_45000243_TRAN | FIWTJPV_CONFIRM | Define Evidence Codes |  | FI-LOC-IAM | FI-AP-AP-Q1 |
| SAP_CA_BC_IC_LND_GLOFI_DSP_PC | Globalization Financials - Configuration Display | S_EBJ_45000244 | S_EBJ_45000244_TRAN | FIWTJPV_STATUS | Define Collection Status Codes |  | FI-LOC-IAM | FI-AP-AP-Q1 |
| SAP_CA_BC_IC_LND_GLOFI_DSP_PC | Globalization Financials - Configuration Display | S_PCO_36000093 | S_PCO_36000093_TRAN | JPINVSUM_005 | Maintain Number Ranges |  | FI-LOC-IAM | FI-LOC-FI-JP |
| SAP_CA_BC_IC_LND_GLOFI_DSP_PC | Globalization Financials - Configuration Display | S_ER9_52001072 | S_ER9_52001072_TRAN | IDGT_WHITELIST_V | Define a White List for Writing Back |  | FI-LOC-IAM | FI-LOC-GTI-CN |
| SAP_CA_BC_IC_LND_GLOFI_DSP_PC | Globalization Financials - Configuration Display | FIRU_PRT_CNCLC |  | J_3RFPOFPRIV | Define Federal Tax Concessions | 107296 | FI-LOC-IAM | FI-LOC-FI-RU |
| SAP_CA_BC_IC_LND_GLOFI_DSP_PC | Globalization Financials - Configuration Display | S_ER1_70001112 | S_ER1_70001112_03_TRAN | V_BOE_C_CB_INT | Maintain Settings for Integration with Cash Budgeting and EPIC |  | FI-LOC-IAM | FI-LOC-CM-CN |
| SAP_CA_BC_IC_LND_GLOFI_DSP_PC | Globalization Financials - Configuration Display | ISJP_SNRO |  | JPINVSUM_005 | Maintain Number Ranges |  | FI-LOC-IAM | FI-LOC-FI-JP |
| SAP_CA_BC_IC_LND_GLOFI_DSP_PC | Globalization Financials - Configuration Display | S_ER9_11001144 | S_ER9_11001144_TRAN | FAA_GLOFAA_RUCISREV | Maintain Local Accounting Rules for FI-AA Revaluation Posted to FI |  | FI-LOC-IAM | FI-LOC-AA-RU |
| SAP_CA_BC_IC_LND_GLOFI_DSP_PC | Globalization Financials - Configuration Display | FIRU_TRT_CNCLC |  | FIRUV_TRT_CNCLC | Define Tax Concession Legal Codes | 107404 | FI-LOC-IAM | FI-LOC-FI-RU |
| SAP_CA_BC_IC_LND_GLOFI_DSP_PC | Globalization Financials - Configuration Display | S_PCO_36000318 | S_PCO_36000318_03_TRAN | J_3RFPOFPRIV | Define Federal Tax Concessions | 107296 | FI-LOC-IAM | FI-LOC-FI-RU |
| SAP_CA_BC_IC_LND_GLOFI_DSP_PC | Globalization Financials - Configuration Display | FIRU_VATOUTPUT |  | FIRUV_VATOUTPUT | Define VAT Return Version for Output | 107320 | FI-LOC-IAM | FI-LOC-FI-RU |
| SAP_CA_BC_IC_LND_GLOFI_DSP_PC | Globalization Financials - Configuration Display | S_ER9_11001145 | S_ER9_11001145_TRAN | FAA_GLOFAA_RUACCS | Assign Revaluation Accounts |  | FI-LOC-IAM | FI-LOC-AA-RU |
| SAP_CA_BC_IC_LND_GLOFI_DSP_PC | Globalization Financials - Configuration Display | S_ER9_11000642 | S_ER9_11000642_03_TRAN | FIRUV_VATOUTPUT | Define VAT Return Version for Output | 107320 | FI-LOC-IAM | FI-LOC-FI-RU |
| SAP_CA_BC_IC_LND_GLOFI_DSP_PC | Globalization Financials - Configuration Display | S_ER9_11001735 | S_ER9_11001735_03_TRAN | FIRUV_TRT_CNCLC | Define Tax Concession Legal Codes | 107404 | FI-LOC-IAM | FI-LOC-FI-RU |
| SAP_CA_BC_IC_LND_COM_DSP_PC | CO Content - Configuration Display | COKN |  | SIMG_CFMENUCONTCOKN | Define Number Range for CO Attributes |  | CO-OM | FI-CNT-GL |
| SAP_CA_BC_IC_LND_COM_DSP_PC | CO Content - Configuration Display | S_ER9_11002286 | S_ER9_11002286_TRAN | SIMG_CFMENUCONTCOKN | Define Number Range for CO Attributes |  | CO-OM | FI-CNT-GL |
| SAP_CA_BC_IC_LND_WFD_DSP_PC | Workforce Integration - Configuration Display | /SHCM/68000003 | /SHCM/68000003_TRAN | /SHCM/T77BPSYNC | Maintain BP Integration Parameter Values |  | CA-WFD-INT | CA-WFD-BL |
| SAP_CA_BC_IC_LND_WFD_DSP_PC | Workforce Integration - Configuration Display | /SHCM/T77BPSYNC |  | /SHCM/T77BPSYNC | Maintain BP Integration Parameter Values |  | CA-WFD-INT | CA-WFD-BL |
| SAP_CA_BC_IC_LND_WFD_DSP_PC | Workforce Integration - Configuration Display | S_ER1_70001800 | S_ER1_70001800_03_TRAN | V_WFD_D_TARGETS | Determine Target System for Retrieving Photo of Worker |  | CA-WFD-INT | CA-WFD-BL |
| SAP_CA_BC_IC_LND_WFD_DSP_PC | Workforce Integration - Configuration Display | WFD_TARGETS |  | V_WFD_D_TARGETS | Determine Target System for Retrieving Photo of Worker |  | CA-WFD-INT | CA-WFD-BL |
| SAP_CA_BC_IC_LND_WFD_DSP_PC | Workforce Integration - Configuration Display | /SHCM/52000194 | /SHCM/52000194_TRAN | /SHCM/RECON | Display Reconciliation Accounts for Employees in Role FI Supplier | 100297 | CA-WFD-INT | CA-WFD |
| SAP_CA_BC_IC_LND_FIN_BV0_PC | Consolidation - Balance Validation Tasks Configuration | S_ER1_70001171 | S_ER1_70001171_TRAN | SIMG_CFMENU_BVTSK | Define Balance Validation Tasks | 106862 | FIN-CS | FIN-CS-BV-2CL |
| SAP_CA_BC_IC_LND_FIN_BV0_PC | Consolidation - Balance Validation Tasks Configuration | FINCS_CV_ASSIGN |  | SIMG_CFMENU_BVCVA | Define Comparison Versions | 107033 | FIN-CS | FIN-CS-BV-2CL |
| SAP_CA_BC_IC_LND_FIN_BV0_PC | Consolidation - Balance Validation Tasks Configuration | S_ER1_70001509 | S_ER1_70001509_TRAN | SIMG_CFMENU_BVCVA | Define Comparison Versions | 107033 | FIN-CS | FIN-CS-BV-2CL |
| SAP_CA_BC_IC_LND_FIN_BV0_PC | Consolidation - Balance Validation Tasks Configuration | FINCS_BV_TASK |  | SIMG_CFMENU_BVTSK | Define Balance Validation Tasks | 106862 | FIN-CS | FIN-CS-BV-2CL |
| SAP_FIN_BC_DCO_SETTINGS_PC | Collections and Dispute Automation - Current Settings | /DCO/V_CCODE_FI | DCO_V_CCODE_FI_TRAN |  |  |  | FIN-FIO-CCD-COL |  |
| SAP_FIN_BC_DCO_SETTINGS_PC | Collections and Dispute Automation - Current Settings | /DCO/V_CCODE_M | DCO_V_CCODE_M_TRAN |  |  |  | FIN-FIO-CCD-COL |  |
| SAP_FIN_BC_DCO_SETTINGS_PC | Collections and Dispute Automation - Current Settings | DCO_ACTIVATION | DCO_ACTIVATION_TRAN |  |  |  | FIN-FIO-CCD-COL |  |
| SAP_FIN_BC_DCO_SETTINGS_PC | Collections and Dispute Automation - Current Settings | /DCO/V_PMT_DFF_R | DCO_V_PMT_DFF_R_TRAN |  |  |  | FIN-FIO-CCD-COL |  |
| SAP_FIN_BC_DCO_SETTINGS_PC | Collections and Dispute Automation - Current Settings | /DCO/V_PST_S_CLS | DCO_V_PST_S_CLS_TRAN |  |  |  | FIN-FIO-CCD-COL |  |
| SAP_FIN_BC_DCO_SETTINGS_PC | Collections and Dispute Automation - Current Settings | /DCO/V_PST_CLSS | DCO_V_PST_CLSS_TRAN |  |  |  | FIN-FIO-CCD-COL |  |
| SAP_CA_BC_IC_LND_GLO_DSP_PC | Globalization Logistics - Configuration Display | S_P7D_67000069 | S_P7D_67000069_03_TRAN | V_DOCCLS_ID | Maintain Document Classes |  | FI-LOC-LO | FI-LOC-FI-ID |
| SAP_CA_BC_IC_LND_GLO_DSP_PC | Globalization Logistics - Configuration Display | S_ER9_52000656 | S_ER9_52000656_03_TRAN | GLO_DOC_TYP_V | Assign Document Types to Billing Types | 101860 | FI-LOC-LO | FI-LOC-LO-IT |
| SAP_CA_BC_IC_LND_GLO_DSP_PC | Globalization Logistics - Configuration Display | S_AL0_19000044 | S_AL0_19000044_03_TRAN | OFFDOCNO_TH_001 | Maintain Number Groups |  | FI-LOC-LO | FI-LOC-FI-TH |
| SAP_CA_BC_IC_LND_GLO_DSP_PC | Globalization Logistics - Configuration Display | S_ER9_52000851 | S_ER9_52000851_03_TRAN | GLO_ODN_DOC_TY_V | Assign Document Types to Billing Types |  | FI-LOC-LO | FI-LOC-LO-IT |
| SAP_CA_BC_IC_LND_GLO_DSP_PC | Globalization Logistics - Configuration Display | S_AL0_19000050 | S_AL0_19000050_03_TRAN | OFFDOCNO_TH_007 | Activate Official Document Numbering |  | FI-LOC-LO | FI-LOC-FI-TH |
| SAP_CA_BC_IC_LND_GLO_DSP_PC | Globalization Logistics - Configuration Display | S_ER9_11000889 | S_ER9_11000889_03_TRAN | OFFDOCNO_IT_006 | Assign Document Types to Billing Types | 102471 | FI-LOC-LO | CA-GTF-CSC-ODN |
| SAP_CA_BC_IC_LND_GLO_DSP_PC | Globalization Logistics - Configuration Display | S_E4A_94000051 | S_E4A_94000051_03_TRAN | ERS_005 | Assign Document Class to Document Type |  | FI-LOC-LO | CA-GTF-CSC-ODN |
| SAP_CA_BC_IC_LND_GLO_DSP_PC | Globalization Logistics - Configuration Display | S_E4A_94000050 | S_E4A_94000050_03_TRAN | ERS_004 | Define Document Classes |  | FI-LOC-LO | CA-GTF-CSC-ODN |
| SAP_CA_BC_IC_LND_GLO_DSP_PC | Globalization Logistics - Configuration Display | S_AC0_52000202 | S_AC0_52000202_03_TRAN | OFFDOCNO_IT_002 | Assign Document Classes to Document Types |  | FI-LOC-LO | CA-GTF-CSC-ODN |
| SAP_CA_BC_IC_LND_GLO_DSP_PC | Globalization Logistics - Configuration Display | S_AC0_52000199 | S_AC0_52000199_03_TRAN | OFFDOCNO_IT_001 | Define Document Classes |  | FI-LOC-LO | CA-GTF-CSC-ODN |
| SAP_CA_BC_IC_LND_GLO_DSP_PC | Globalization Logistics - Configuration Display | S_ER9_52002087 | S_ER9_52002087_03_TRAN | LOG_EINV_IN_01 | Map Customer/ Vendor Tax Classification |  | FI-LOC-LO | CA-GTF-CSC-EDO-IN-DC |
| SAP_CA_BC_IC_LND_GLO_DSP_PC | Globalization Logistics - Configuration Display | S_P6B_12000021 | S_P6B_12000021_TRAN | V_T604F | Maintain PKWiUs |  | FI-LOC-LO | CA-GTF-CSC-PL |
| SAP_CA_BC_IC_LND_GLO_DSP_PC | Globalization Logistics - Configuration Display | S_SL0_21000022 | S_SL0_21000022_03_TRAN | V_1ANUMGR1_PH | Maintain Number Groups |  | FI-LOC-LO | FI-LOC-FI-PH |
| SAP_CA_BC_IC_LND_PR1_DSP_PC | Central Master Data Product - Configuration Display | S_ALR_87002414 | S_ALR_87002414_03_TRAN | SIMG_CFMENUOLMSW4EQ | Define Prefixes for EANs/UPCs |  | LO-MD-MM | LO-MD-MM-2CL |
| SAP_CA_BC_IC_LND_PR1_DSP_PC | Central Master Data Product - Configuration Display | OMT0 |  | SIMG_CFMENUOLMSOMT0 | Make Global Settings |  | LO-MD-MM | LO-MD-MM-2CL |
| SAP_CA_BC_IC_LND_PR1_DSP_PC | Central Master Data Product - Configuration Display | S_ALR_87002305 | S_ALR_87002305_03_TRAN | SIMG_CFMENUOLMSOMT0 | Make Global Settings |  | LO-MD-MM | LO-MD-MM-2CL |
| SAP_CA_BC_IC_LND_FLOG_DSP_PC | Field Logistics - Configuration Display | S_ER1_70000183 | S_ER1_70000183_03_TRAN | FLOG_V_RT_INIT | Maintain Return Initiation Document |  | CA-FL | CA-FL |
| SAP_CA_BC_IC_LND_FLOG_DSP_PC | Field Logistics - Configuration Display | S_ER1_70000181 | S_ER1_70000181_03_TRAN | FLOG_V_RT_RECACT | Maintain Recommended Action |  | CA-FL | CA-FL |
| SAP_CA_BC_IC_LND_FLOG_DSP_PC | Field Logistics - Configuration Display | S_ER1_70000236 | S_ER1_70000236_03_TRAN | FLOG_V_RET_QKACT | Maintain Handling Decision |  | CA-FL | CA-FL |
| SAP_CA_BC_IC_LND_FLOG_DSP_PC | Field Logistics - Configuration Display | S_ER1_70000180 | S_ER1_70000180_03_TRAN | FLOG_V_RT_STAT | Maintain Return Status |  | CA-FL | CA-FL |
| SAP_CA_BC_IC_LND_FLOG_DSP_PC | Field Logistics - Configuration Display | S_ER1_70000238 | S_ER1_70000238_03_TRAN | FLOG_V_QUK_INIT | Maintain Initiating Documents for Handling Decision |  | CA-FL | CA-FL |
| SAP_CA_BC_IC_LND_FLOG_DSP_PC | Field Logistics - Configuration Display | S_ER1_70000135 | S_ER1_70000135_03_TRAN | FLOG_V_SUPPROC | Maintain Supply Process Definition |  | CA-FL | CA-FL |
| SAP_CA_BC_IC_LND_FICA_DSP_PC | Contract Accounting - Configuration Display | S_KK4_74002088 | S_KK4_74002088_03_TRAN | _FICABTPYPC_FQZX | Define Specifications for Posting Settlement Document | 106981 | FI-CA | FI-CA-2CL |
| SAP_CA_BC_IC_LND_FICA_DSP_PC | Contract Accounting - Configuration Display | FQZX |  | _FICABTPYPC_FQZX | Define Specifications for Posting Settlement Document | 106981 | FI-CA | FI-CA-2CL |
| SAP_CA_BC_IC_LND_FICA_DSP_PC | Contract Accounting - Configuration Display | FQKPZ |  | _FICABTPY_FQZ6 | Define Screen Variants for Payment Lot |  | FI-CA | FI-CA-2CL |
| SAP_CA_BC_IC_LND_FICA_DSP_PC | Contract Accounting - Configuration Display | S_KK4_74002179 | S_KK4_74002179_03_TRAN | _FICABTPY_FQZ6 | Define Screen Variants for Payment Lot |  | FI-CA | FI-CA-2CL |
| SAP_CA_BC_IC_LND_FICA_DSP_PC | Contract Accounting - Configuration Display | S_KK4_74002311 | S_KK4_74002311_03_TRAN | _FICABTPY_TFK004B | Specify Selection Categories |  | FI-CA | FI-CA-2CL |
| SAP_CA_BC_IC_LND_FICA_DSP_PC | Contract Accounting - Configuration Display | S_KK4_74002373 | S_KK4_74002373_03_TRAN | _FICABFTX_TFK048B | Define Tax Calc. Types in Write-Offs and Ind. Val. Adj. |  | FI-CA | FI-CA-2CL |
| SAP_CA_BC_IC_LND_FICA_DSP_PC | Contract Accounting - Configuration Display | S_KK4_74002377 | S_KK4_74002377_03_TRAN | _FICAISAD_FQK1 | Select Fields for Search Function |  | FI-CA | FI-CA-2CL |
| SAP_CA_BC_IC_LND_FICA_DSP_PC | Contract Accounting - Configuration Display | S_KK4_74002378 | S_KK4_74002378_03_TRAN | _FICAISAD_TFK021U | Define Proposal for Line Layout |  | FI-CA | FI-CA-2CL |
| SAP_CA_BC_IC_LND_FICA_DSP_PC | Contract Accounting - Configuration Display | S_KK4_74002379 | S_KK4_74002379_03_TRAN | _FICAISAD_V_TFK021SV | Maintain Sorting Variants |  | FI-CA | FI-CA-2CL |
| SAP_CA_BC_IC_LND_FICA_DSP_PC | Contract Accounting - Configuration Display | S_KK4_74002419 | S_KK4_74002419_03_TRAN | _FICAISAD_V_TFK021L | Define List Category |  | FI-CA | FI-CA-2CL |
| SAP_CA_BC_IC_LND_FICA_DSP_PC | Contract Accounting - Configuration Display | S_KK4_74002113 | S_KK4_74002113_03_TRAN | _FICABTDU_V_TFK047L | Configure Dunning Activities |  | FI-CA | FI-CA-2CL |
| SAP_CA_BC_IC_LND_FICA_DSP_PC | Contract Accounting - Configuration Display | S_ER9_52000844 | S_ER9_52000844_03_TRAN | _FICABTPY_VTFKPCARDR | Categorize SAP Digitial Payment Add-On Error Code |  | FI-CA | FI-CA-2CL |
| SAP_CA_BC_IC_LND_FICA_DSP_PC | Contract Accounting - Configuration Display | S_ER9_52000795 | S_ER9_52000795_03_TRAN | _FICABTRE_VC_TFKFS | Define Screen Variant Returns |  | FI-CA | FI-CA-2CL |
| SAP_CA_BC_IC_LND_FICA_DSP_PC | Contract Accounting - Configuration Display | S_EMO_14000326 | S_EMO_14000326_03_TRAN | _FICACVORG_V_TFKIVV | Assign External Transactions |  | FI-CA | FI-CA-2CL |
| SAP_CA_BC_IC_LND_FICA_DSP_PC | Contract Accounting - Configuration Display | FQZI |  | _FICABTPY_FQZI | Define Default Values for Payment Lot | 106973 | FI-CA | FI-CA-2CL |
| SAP_CA_BC_IC_LND_FICA_DSP_PC | Contract Accounting - Configuration Display | S_EMI_14000130 | S_EMI_14000130_03_TRAN | _FICAPV_TFK_VT_PRD | Make Central Settings for Products |  | FI-CA | FI-CA-2CL |
| SAP_CA_BC_IC_LND_FICA_DSP_PC | Contract Accounting - Configuration Display | S_KK4_74002178 | S_KK4_74002178_03_TRAN | _FICABTPY_FQZI | Define Default Values for Payment Lot | 106973 | FI-CA | FI-CA-2CL |
| SAP_CA_BC_IC_LND_FICA_DSP_PC | Contract Accounting - Configuration Display | S_EMI_14000253 | S_EMI_14000253_03_TRAN | _FICARA_V_TFK_RA_SET | Activate Integration with Revenue Accounting |  | FI-CA | FI-CA-2CL |
| SAP_CA_BC_IC_LND_FICA_DSP_PC | Contract Accounting - Configuration Display | S_ER1_70001229 | S_ER1_70001229_03_TRAN | _FICAPV_TFK000V | Activate Provider Contract |  | FI-CA | FI-CA-2CL |
| SAP_CA_BC_IC_LND_MDC_PC | Master Data Governance - Business Configuration | S_SAL_71000110 | S_SAL_71000110_TRAN | V_MDC_PRIORITIES | Define Process Priorities |  | CA-MDG-CL | CA-MDG-PF-AF |
| SAP_CA_BC_IC_LND_MDC_PC | Master Data Governance - Business Configuration | MDC_PROCESS_PRIORITY |  | V_MDC_PRIORITIES | Define Process Priorities |  | CA-MDG-CL | CA-MDG-PF-AF |
| SAP_CA_BC_IC_LND_MDC_PC | Master Data Governance - Business Configuration | S_SAL_71000111 | S_SAL_71000111_TRAN | V_MDC_REASONS | Define Process Reasons |  | CA-MDG-CL | CA-MDG-PF-AF |
| SAP_CA_BC_IC_LND_MDC_PC | Master Data Governance - Business Configuration | MDC_PROCESS_REASON |  | V_MDC_REASONS | Define Process Reasons |  | CA-MDG-CL | CA-MDG-PF-AF |
| SAP_CA_BC_IC_LND_JIT_DSP_PC | Logistics Execution - Next Generation Just-In-Time Processing - Configuration | S_ER9_52001889 | S_ER9_52001889_TRAN | SIMG_NJIT_DELY_CNTRL | Maintain JIT Delivery Split Criteria |  | LE-JIT-S2C | LE-JIT-S2C |
| SAP_CA_BC_IC_LND_JIT_DSP_PC | Logistics Execution - Next Generation Just-In-Time Processing - Configuration | S_ER9_52001376 | S_ER9_52001376_TRAN | SIMG_NJIT_SUPCTRL_I | Maintain Number Range Objects for Customer Supply Control |  | LE-JIT-S2C | LE-JIT-S2C |
| SAP_CA_BC_IC_LND_JIT_DSP_PC | Logistics Execution - Next Generation Just-In-Time Processing - Configuration | NJITSCID |  | SIMG_NJIT_SUPCTRL_I | Maintain Number Range Objects for Customer Supply Control |  | LE-JIT-S2C | LE-JIT-S2C |
| SAP_CA_BC_IC_LND_JIT_DSP_PC | Logistics Execution - Next Generation Just-In-Time Processing - Configuration | S_ER9_52001375 | S_ER9_52001375_TRAN | SIMG_NJIT_CALLNO_I | Maintain Number Range Objects for Just-In-Time Calls |  | LE-JIT-S2C | LE-JIT-S2C |
| SAP_CA_BC_IC_LND_JIT_DSP_PC | Logistics Execution - Next Generation Just-In-Time Processing - Configuration | S_ER9_52002822 | S_ER9_52002822_TRAN | SIMG_NJIT_VP | Maintain Verification Profile |  | LE-JIT-S2C | LE-JIT-S2C |
| SAP_CA_BC_IC_LND_JIT_DSP_PC | Logistics Execution - Next Generation Just-In-Time Processing - Configuration | NJITREQID |  | SIMG_NJIT_CALLNO_I | Maintain Number Range Objects for Just-In-Time Calls |  | LE-JIT-S2C | LE-JIT-S2C |
| SAP_CA_BC_IC_LND_JIT_DSP_PC | Logistics Execution - Next Generation Just-In-Time Processing - Configuration | S_ER9_52001377 | S_ER9_52001377_TRAN | SIMG_NJIT_PKGDEF_I | Maintain Number Range Objects for Packing Group Specification |  | LE-JIT-S2C | LE-JIT-S2C |
| SAP_CA_BC_IC_LND_JIT_DSP_PC | Logistics Execution - Next Generation Just-In-Time Processing - Configuration | NJITPGDID |  | SIMG_NJIT_PKGDEF_I | Maintain Number Range Objects for Packing Group Specification |  | LE-JIT-S2C | LE-JIT-S2C |
| SAP_CA_BC_IC_LND_JIT_DSP_PC | Logistics Execution - Next Generation Just-In-Time Processing - Configuration | NJITPGID |  | SIMG_NJIT_PKG_I | Maintain Number Range Objects for Packing Group |  | LE-JIT-S2C | LE-JIT-S2C |
| SAP_CA_BC_IC_LND_JIT_DSP_PC | Logistics Execution - Next Generation Just-In-Time Processing - Configuration | S_ER9_52001378 | S_ER9_52001378_TRAN | SIMG_NJIT_PKG_I | Maintain Number Range Objects for Packing Group |  | LE-JIT-S2C | LE-JIT-S2C |
| SAP_CA_BC_IC_LND_JIT_DSP_PC | Logistics Execution - Next Generation Just-In-Time Processing - Configuration | S_ER9_52002198 | S_ER9_52002198_TRAN | SIMG_NJIT_DSGID | Maintain Number Range Objects for Delivery Sequence Groups |  | LE-JIT-S2C | LE-JIT-S2C |
| SAP_CA_BC_IC_LND_JIT_DSP_PC | Logistics Execution - Next Generation Just-In-Time Processing - Configuration | NJITDSGID |  | SIMG_NJIT_DSGID | Maintain Number Range Objects for Delivery Sequence Groups |  | LE-JIT-S2C | LE-JIT-S2C |
| SAP_CA_BC_IC_LND_JIT_DSP_PC | Logistics Execution - Next Generation Just-In-Time Processing - Configuration | NJITDCID |  | SIMG_NJIT_DCID | Maintain Number Range Objects for JIT Delivery Confirmations |  | LE-JIT-S2C | LE-JIT-S2C |
| SAP_CA_BC_IC_LND_JIT_DSP_PC | Logistics Execution - Next Generation Just-In-Time Processing - Configuration | S_ER9_52002545 | S_ER9_52002545_TRAN | SIMG_NJIT_DCID | Maintain Number Range Objects for JIT Delivery Confirmations |  | LE-JIT-S2C | LE-JIT-S2C |
| SAP_CA_BC_IC_LND_FIN_GL_VN_PC | General Ledger for Vietnam - Configuration | FIVN_OFFS_DET |  | FIVN_OFFS_DET | Activate Online Offsetting Account Determination | 107053 | FI-LOC-FI-VN | FI-LOC-FI-VN |
| SAP_CA_BC_IC_LND_FIN_GL_VN_PC | General Ledger for Vietnam - Configuration | S_ER1_70001535 | S_ER1_70001535_TRAN | FIVN_OFFS_GROUPING | Define Field Sets for Grouping | 107055 | FI-LOC-FI-VN | FI-LOC-FI-VN |
| SAP_CA_BC_IC_LND_FIN_GL_VN_PC | General Ledger for Vietnam - Configuration | S_ER1_70001658 | S_ER1_70001658_TRAN | FIVNVC_CF_VERS_DRC | Manage Cash Flow Statement Version | 107127 | FI-LOC-FI-VN | FI-LOC-FI-VN |
| SAP_CA_BC_IC_LND_FIN_GL_VN_PC | General Ledger for Vietnam - Configuration | S_ER1_70001532 | S_ER1_70001532_TRAN | FIVN_OFFS_DET | Activate Online Offsetting Account Determination | 107053 | FI-LOC-FI-VN | FI-LOC-FI-VN |
| SAP_CA_BC_IC_LND_FIN_GL_VN_PC | General Ledger for Vietnam - Configuration | FIVNVC_CF_VERS_DRC |  | FIVNVC_CF_VERS_DRC | Manage Cash Flow Statement Version | 107127 | FI-LOC-FI-VN | FI-LOC-FI-VN |
| SAP_CA_BC_IC_LND_FIN_GL_VN_PC | General Ledger for Vietnam - Configuration | S_ER1_70001534 | S_ER1_70001534_TRAN | FIVN_OFFS_VERSIONS | Define Versions for Offsetting Account Determination | 107054 | FI-LOC-FI-VN | FI-LOC-FI-VN |
| SAP_CA_BC_IC_LND_FIN_GL_VN_PC | General Ledger for Vietnam - Configuration | FIVN_OFFS_GROUPING |  | FIVN_OFFS_GROUPING | Define Field Sets for Grouping | 107055 | FI-LOC-FI-VN | FI-LOC-FI-VN |
| SAP_CA_BC_IC_LND_FIN_GL_VN_PC | General Ledger for Vietnam - Configuration | F4232 | F4232_TRAN |  |  |  | FI-LOC-FI-VN |  |
| SAP_FIN_BC_RPI_SETTINGS_PC | Accounts Payable and Receivable - Receivable/Payable Item | F8418 | F8418_TRAN |  |  |  | FI-AR-AR |  |
| SAP_CA_BC_IC_LND_RFM_VAS_PC | Retail Value Added Services - Configuration | S_ESI_04000092 | S_ESI_04000092_TRAN | FSH_VAS_MAINTAIN | Maintain Service Types and Subservice Types | 106837 | LO-RFM | LO-RFM-CA-VAS-2CL |
| SAP_CA_BC_IC_LND_RFM_VAS_PC | Retail Value Added Services - Configuration | S_ER1_70001131 | S_ER1_70001131_TRAN | RTL_VAS_ACTVT | Activate Business Function ‘Retail Value-Added Services’ | 106858 | LO-RFM | LO-RFM-CA-VAS-2CL |
| SAP_CA_BC_IC_LND_RFM_VAS_PC | Retail Value Added Services - Configuration | S_ESI_04000114 | S_ESI_04000114_TRAN | FSH_V_VAS_CHRG | Define Charge Code | 107060 | LO-RFM | LO-RFM-CA-VAS-2CL |
| SAP_CA_BC_IC_LND_RFM_VAS_PC | Retail Value Added Services - Configuration | S_ESI_04000079 | S_ESI_04000079_TRAN | FSH_V_TVLK_NEW | Define VAS Controls for Delivery Types | 107016 | LO-RFM | LO-RFM-SD-2CL |
| SAP_CA_BC_IC_LND_RFM_VAS_PC | Retail Value Added Services - Configuration | RTL_VAS_ACTVT |  | RTL_VAS_ACTVT | Activate Business Function ‘Retail Value-Added Services’ | 106858 | LO-RFM | LO-RFM-CA-VAS-2CL |
| SAP_CA_BC_IC_LND_IA_DSP_PC | Inventory Accounting - Configuration Display | S_ALR_87008196 | S_ALR_87008196_TRAN | SIMG_CFMENUORKKOKK6 | Define Date Control |  | CO-PC-ML | CO-PC-PCP-2CL |
| SAP_CA_BC_IC_LND_IA_DSP_PC | Inventory Accounting - Configuration Display | OKK6 |  | SIMG_CFMENUORKKOKK6 | Define Date Control |  | CO-PC-ML | CO-PC-PCP-2CL |
| SAP_CA_BC_IC_LND_IA_DSP_PC | Inventory Accounting - Configuration Display | FUCB_METHOD |  | FUCB_METHOD | Define and Assign Method for Universal Component Breakdown |  | CO-PC-ML | CO-PC-PCP-2CL |
| SAP_CA_BC_IC_LND_IA_DSP_PC | Inventory Accounting - Configuration Display | S_ALR_87008224 | S_ALR_87008224_TRAN | SIMG_CFMENUORKKOKK5 | Define Quantity Structure Control |  | CO-PC-ML | CO-PC-PCP-2CL |
| SAP_CA_BC_IC_LND_IA_DSP_PC | Inventory Accounting - Configuration Display | OKYC |  | SIMG_ORKK_REFERENZ | Define Reference Variants |  | CO-PC-ML | CO-PC-PCP-2CL |
| SAP_CA_BC_IC_LND_IA_DSP_PC | Inventory Accounting - Configuration Display | S_ER9_11002727 | S_ER9_11002727_TRAN | FUCB_METHOD | Define and Assign Method for Universal Component Breakdown |  | CO-PC-ML | CO-PC-PCP-2CL |
| SAP_CA_BC_IC_LND_IA_DSP_PC | Inventory Accounting - Configuration Display | S_ALR_87008165 | S_ALR_87008165_TRAN | SIMG_ORKK_REFERENZ | Define Reference Variants |  | CO-PC-ML | CO-PC-PCP-2CL |
| SAP_CA_BC_IC_LND_IA_DSP_PC | Inventory Accounting - Configuration Display | S_ALR_87008199 | S_ALR_87008199_03_TRAN | SIMG_CFMENUORKKOKKI | Define Costing Types |  | CO-PC-ML | CO-PC-PCP-2CL |
| SAP_CA_BC_IC_LND_IA_DSP_PC | Inventory Accounting - Configuration Display | FUCB_QBS |  | FUCB_QBS | Define Quantity Breakdown Structures |  | CO-PC-ML | CO-PC-PCP-2CL |
| SAP_CA_BC_IC_LND_IA_DSP_PC | Inventory Accounting - Configuration Display | OKK5 |  | SIMG_CFMENUORKKOKK5 | Define Quantity Structure Control |  | CO-PC-ML | CO-PC-PCP-2CL |
| SAP_CA_BC_IC_LND_IA_DSP_PC | Inventory Accounting - Configuration Display | OKKI |  | SIMG_CFMENUORKKOKKI | Define Costing Types |  | CO-PC-ML | CO-PC-PCP-2CL |
| SAP_CA_BC_IC_LND_IA_DSP_PC | Inventory Accounting - Configuration Display | S_ER1_70001231 | S_ER1_70001231_TRAN | FUCB_QBS | Define Quantity Breakdown Structures |  | CO-PC-ML | CO-PC-PCP-2CL |
| SAP_CA_BC_IC_LND_IA_DSP_PC | Inventory Accounting - Configuration Display | OKYA |  | SIMG_CFMENUORKKOKYA | Check Costing Types |  | CO-PC-ML | CO-PC-PCP-2CL |
| SAP_CA_BC_IC_LND_IA_DSP_PC | Inventory Accounting - Configuration Display | S_ALR_87008014 | S_ALR_87008014_TRAN | SIMG_CFMENUORKKOKYA | Check Costing Types |  | CO-PC-ML | CO-PC-PCP-2CL |
| SAP_CA_BC_IC_LND_IA_DSP_PC | Inventory Accounting - Configuration Display | OKY9 |  | SIMG_CFMENUORKKOKY9 | Check Costing Variants for Sales Order Costing |  | CO-PC-ML | CO-PC-PCP-2CL |
| SAP_CA_BC_IC_LND_IA_DSP_PC | Inventory Accounting - Configuration Display | S_ALR_87008015 | S_ALR_87008015_TRAN | SIMG_CFMENUORKKOKY9 | Check Costing Variants for Sales Order Costing |  | CO-PC-ML | CO-PC-PCP-2CL |
| SAP_CA_BC_IC_LND_PS_DSP_PC | Enterprise Projects - Configuration Display | S_ER9_52002124 | S_ER9_52002124_TRAN | VPS_ORDERCATMAP | Maintain Planning Categories for Order Types |  | PPM-SCL-STR | PPM-SCL-REP |
| SAP_CA_BC_IC_LND_APM_DSP_PC | Advanced Payment Management - Configuration Display | /PF1/04000018 | S_PF1_04000018_03_TRAN | /PF1/V_GL_AC_DET | Define Pattern for G/L Overlay |  | FIN-FSCM-PF | FIN-FSCM-PF |
| SAP_CA_BC_IC_LND_APM_DSP_PC | Advanced Payment Management - Configuration Display | /PF1/04000021 | S_PF1_04000021_03_TRAN | /PF1/V_GL_SUSP | Define APM Clearing/Suspense Accounts |  | FIN-FSCM-PF | FIN-FSCM-PF |
| SAP_CA_BC_IC_LND_APM_DSP_PC | Advanced Payment Management - Configuration Display | /PF1/04000030 | S_PF1_04000030_03_TRAN | /PF1/V_PROCORDER | Maintain Payment Order Fields for Processes |  | FIN-FSCM-PF | FIN-FSCM-PF |
| SAP_CA_BC_IC_LND_APM_DSP_PC | Advanced Payment Management - Configuration Display | /PF1/04000020 | S_PF1_04000020_03_TRAN | /PF1/V_EH_RESUB | Define Response Type for Internal Automatic Resubmission |  | FIN-FSCM-PF | FIN-FSCM-PF |
| SAP_CA_BC_IC_LND_APM_DSP_PC | Advanced Payment Management - Configuration Display | /PF1/04000035 | S_PF1_04000035_03_TRAN | /PF1/V_TPM_FMC | Define Inbound Channel for External Interface |  | FIN-FSCM-PF | FIN-FSCM-PF |
| SAP_CA_BC_IC_LND_APM_DSP_PC | Advanced Payment Management - Configuration Display | /PF1/04000045 | S_PF1_04000045_03_TRAN | /PF1/V_PACK_SIZE | Maintain Technical Package Settings |  | FIN-FSCM-PF | FIN-FSCM-PF |
| SAP_CA_BC_IC_LND_APM_DSP_PC | Advanced Payment Management - Configuration Display | /PF1/11001751 | S_PF1_11001751_03_TRAN | /PF1/V_FEATURE | Switchable Features |  | FIN-FSCM-PF | FIN-FSCM-PF |
| SAP_CA_BC_IC_LND_APM_DSP_PC | Advanced Payment Management - Configuration Display | /PF1/11001578 | S_PF1_11001578_03_TRAN | /PF1/V_EH_RTYPE1 | Maintain Exception Handling Reaction Type |  | FIN-FSCM-PF | FIN-FSCM-PF |
| SAP_CA_BC_IC_LND_APM_DSP_PC | Advanced Payment Management - Configuration Display | /PF1/11001847 | S_PF1_11001847_03_TRAN | /PF1/IMG_V_BANK | Assign Internal Bank Keys to Clearing Areas |  | FIN-FSCM-PF | FIN-FSCM-PF |
| SAP_CA_BC_IC_LND_APM_DSP_PC | Advanced Payment Management - Configuration Display | /PF1/NUM_RANGE_OL |  | /PF1/FH_NUM_RANGE_OL | Maintain Number Ranges for Object List |  | FIN-FSCM-PF | FIN-FSCM-PF |
| SAP_CA_BC_IC_LND_APM_DSP_PC | Advanced Payment Management - Configuration Display | /PF1/11001882 | S_PF1_11001882_03_TRAN | /PF1/V_FH_XML | Define XML Settings for Format Converter |  | FIN-FSCM-PF | FIN-FSCM-PF |
| SAP_CA_BC_IC_LND_APM_DSP_PC | Advanced Payment Management - Configuration Display | /PF1/11001927 | S_PF1_11001927_03_TRAN | /PF1/VC_CONVERTER | Define Converter (new) |  | FIN-FSCM-PF | FIN-FSCM-PF |
| SAP_CA_BC_IC_LND_APM_DSP_PC | Advanced Payment Management - Configuration Display | /PF1/11002044 | S_PF1_11002044_03_TRAN | /PF1/V_XML_TRTYP_CE | Determine Transaction Type(View) |  | FIN-FSCM-PF | FIN-FSCM-PF |
| SAP_CA_BC_IC_LND_APM_DSP_PC | Advanced Payment Management - Configuration Display | /PF1/41000003 | S_PF1_41000003_03_TRAN | /PF1/FH_NUM_RANGE_OL | Maintain Number Ranges for Object List |  | FIN-FSCM-PF | FIN-FSCM-PF |
| SAP_CA_BC_IC_LND_APM_DSP_PC | Advanced Payment Management - Configuration Display | /PF1/41000040 | S_PF1_41000040_03_TRAN | /PF1/VC_TRANSTYPE | Define Transaction Types |  | FIN-FSCM-PF | FIN-FSCM-PF |
| SAP_CA_BC_IC_LND_APM_DSP_PC | Advanced Payment Management - Configuration Display | /PF1/41000049 | S_PF1_41000049_03_TRAN | /PF1/EH_EH_PO_PP | Define Response Types for Postprocessing |  | FIN-FSCM-PF | FIN-FSCM-PF |
| SAP_CA_BC_IC_LND_APM_DSP_PC | Advanced Payment Management - Configuration Display | /PF1/41000067 | S_PF1_41000067_03_TRAN | /PF1/NUM_RANGE_CSTID | Maintain Number Ranges for Customer ID |  | FIN-FSCM-PF | FIN-FSCM-PF |
| SAP_CA_BC_IC_LND_APM_DSP_PC | Advanced Payment Management - Configuration Display | /PF1/NUM_RANGE_CSTID |  | /PF1/NUM_RANGE_CSTID | Maintain Number Ranges for Customer ID |  | FIN-FSCM-PF | FIN-FSCM-PF |
| SAP_CA_BC_IC_LND_APM_DSP_PC | Advanced Payment Management - Configuration Display | /PF1/41000083 | S_PF1_41000083_03_TRAN | /PF1/FH_PP_CNT | Maintain Maximum Number of Parallel Processes |  | FIN-FSCM-PF | FIN-FSCM-PF |
| SAP_CA_BC_IC_LND_APM_DSP_PC | Advanced Payment Management - Configuration Display | /PF1/47000006 | S_PF1_47000006_03_TRAN | /PF1/V_XI_PODEF | Map Default Values to Metaformat for Payment Orders |  | FIN-FSCM-PF | FIN-FSCM-PF |
| SAP_CA_BC_IC_LND_APM_DSP_PC | Advanced Payment Management - Configuration Display | /PF1/NUM_RANGE_RA |  | /PF1/NUM_RANGE_RA | Define Number Ranges for Request Agent |  | FIN-FSCM-PF | FIN-FSCM-PF |
| SAP_CA_BC_IC_LND_APM_DSP_PC | Advanced Payment Management - Configuration Display | /PF1/47000098 | S_PF1_47000098_03_TRAN | /PF1/NUM_RANGE_RA | Define Number Ranges for Request Agent |  | FIN-FSCM-PF | FIN-FSCM-PF |
| SAP_CA_BC_IC_LND_APM_DSP_PC | Advanced Payment Management - Configuration Display | /PF1/47000123 | S_PF1_47000123_03_TRAN | /PF1/VC_EV_MAIN | Maintain Enrichment and Validation Check Sets |  | FIN-FSCM-PF | FIN-FSCM-PF |
| SAP_CA_BC_IC_LND_APM_DSP_PC | Advanced Payment Management - Configuration Display | /PF1/47000117 | S_PF1_47000117_03_TRAN | /PF1/VC_SN_TEMPLATES | Define Notification Templates |  | FIN-FSCM-PF | FIN-FSCM-PF |
| SAP_CA_BC_IC_LND_APM_DSP_PC | Advanced Payment Management - Configuration Display | /PF1/47000144 | S_PF1_47000144_03_TRAN | /PF1/V_EH_PO_RP | Define Response Types for Payment Order Reprocessing |  | FIN-FSCM-PF | FIN-FSCM-PF |
| SAP_CA_BC_IC_LND_APM_DSP_PC | Advanced Payment Management - Configuration Display | /PF1/47000168 | S_PF1_47000168_03_TRAN | /PF1/V_POT_TRANT | Assign Transaction Types to Order Types |  | FIN-FSCM-PF | FIN-FSCM-PF |
| SAP_CA_BC_IC_LND_APM_DSP_PC | Advanced Payment Management - Configuration Display | /PF1/47000203 | S_PF1_47000203_03_TRAN | /PF1/V_SIN_OPROC | Control Payment Order Process |  | FIN-FSCM-PF | FIN-FSCM-PF |
| SAP_CA_BC_IC_LND_APM_DSP_PC | Advanced Payment Management - Configuration Display | /PF1/47000219 | S_PF1_47000219_03_TRAN | /PF1/V_RA_CONV | Maintain Format Conversion Information for RA-Activities |  | FIN-FSCM-PF | FIN-FSCM-PF |
| SAP_CA_BC_IC_LND_APM_DSP_PC | Advanced Payment Management - Configuration Display | /PF1/47000245 | S_PF1_47000245_03_TRAN | /PF1/VC_LM_AREA | Define Local Application Management Areas |  | FIN-FSCM-PF | FIN-FSCM-PF |
| SAP_CA_BC_IC_LND_APM_DSP_PC | Advanced Payment Management - Configuration Display | /PF1/51000001 | S_PF1_51000001_03_TRAN | /PF1/V_CLAREA | Define Clearing Areas |  | FIN-FSCM-PF | FIN-FSCM-PF |
| SAP_CA_BC_IC_LND_APM_DSP_PC | Advanced Payment Management - Configuration Display | /PF1/51000013 | S_PF1_51000013_03_TRAN | /PF1/V_MEDIUM | Define Media |  | FIN-FSCM-PF | FIN-FSCM-PF |
| SAP_CA_BC_IC_LND_APM_DSP_PC | Advanced Payment Management - Configuration Display | /PF1/51000029 | S_PF1_51000029_03_TRAN | /PF1/V_POTYPE | Define Payment Order Types |  | FIN-FSCM-PF | FIN-FSCM-PF |
| SAP_CA_BC_IC_LND_APM_DSP_PC | Advanced Payment Management - Configuration Display | /PF1/51000064 | S_PF1_51000064_03_TRAN | /PF1/V_EH_PI_RJ | Define Response Type for Transaction Reject |  | FIN-FSCM-PF | FIN-FSCM-PF |
| SAP_CA_BC_IC_LND_APM_DSP_PC | Advanced Payment Management - Configuration Display | /PF1/NUM_RANGE_PI |  | /PF1/NUM_RANGE_PI | Maintain Number Ranges for Payment Items |  | FIN-FSCM-PF | FIN-FSCM-PF |
| SAP_CA_BC_IC_LND_APM_DSP_PC | Advanced Payment Management - Configuration Display | /PF1/51000034 | S_PF1_51000034_03_TRAN | /PF1/V_AM_AREA | Define Posting Item Areas |  | FIN-FSCM-PF | FIN-FSCM-PF |
| SAP_CA_BC_IC_LND_APM_DSP_PC | Advanced Payment Management - Configuration Display | /PF1/51000047 | S_PF1_51000047_03_TRAN | /PF1/NUM_RANGE_COLL | Maintain Number Ranges for Payment Batches |  | FIN-FSCM-PF | FIN-FSCM-PF |
| SAP_CA_BC_IC_LND_APM_DSP_PC | Advanced Payment Management - Configuration Display | /PF1/NUM_RANGE_PO |  | /PF1/NUM_RANGE_PO | Maintain Number Ranges for Payment Orders |  | FIN-FSCM-PF | FIN-FSCM-PF |
| SAP_CA_BC_IC_LND_APM_DSP_PC | Advanced Payment Management - Configuration Display | /PF1/51000048 | S_PF1_51000048_03_TRAN | /PF1/NUM_RANGE_PO | Maintain Number Ranges for Payment Orders |  | FIN-FSCM-PF | FIN-FSCM-PF |
| SAP_CA_BC_IC_LND_APM_DSP_PC | Advanced Payment Management - Configuration Display | /PF1/51000085 | S_PF1_51000085_03_TRAN | /PF1/NUM_RANGE_RE | Maintain Number Ranges for Recalls |  | FIN-FSCM-PF | FIN-FSCM-PF |
| SAP_CA_BC_IC_LND_APM_DSP_PC | Advanced Payment Management - Configuration Display | /PF1/51000049 | S_PF1_51000049_03_TRAN | /PF1/NUM_RANGE_PI | Maintain Number Ranges for Payment Items |  | FIN-FSCM-PF | FIN-FSCM-PF |
| SAP_CA_BC_IC_LND_APM_DSP_PC | Advanced Payment Management - Configuration Display | /PF1/51000036 | S_PF1_51000036_03_TRAN | /PF1/V_AM_VALUE | Maintain Attribute Values for Posting Item Areas |  | FIN-FSCM-PF | FIN-FSCM-PF |
| SAP_CA_BC_IC_LND_APM_DSP_PC | Advanced Payment Management - Configuration Display | /PF1/51000076 | S_PF1_51000076_03_TRAN | /PF1/V_PROCTTSYM | Assign Transaction Type Symbols to Processes |  | FIN-FSCM-PF | FIN-FSCM-PF |
| SAP_CA_BC_IC_LND_APM_DSP_PC | Advanced Payment Management - Configuration Display | /PF1/NUM_RANGE_COLL |  | /PF1/NUM_RANGE_COLL | Maintain Number Ranges for Payment Batches |  | FIN-FSCM-PF | FIN-FSCM-PF |
| SAP_CA_BC_IC_LND_APM_DSP_PC | Advanced Payment Management - Configuration Display | /PF1/51000035 | S_PF1_51000035_03_TRAN | /PF1/V_TRTYPSYM | Define and Maintain Transaction Type Symbols |  | FIN-FSCM-PF | FIN-FSCM-PF |
| SAP_CA_BC_IC_LND_APM_DSP_PC | Advanced Payment Management - Configuration Display | /PF1/51000066 | S_PF1_51000066_03_TRAN | /PF1/V_EH_IGNORE | Define Response Types for Further Processing |  | FIN-FSCM-PF | FIN-FSCM-PF |
| SAP_CA_BC_IC_LND_APM_DSP_PC | Advanced Payment Management - Configuration Display | /PF1/51000126 | S_PF1_51000126_03_TRAN | /PF1/V_REVERSE | Define Reasons for Payment Rejection |  | FIN-FSCM-PF | FIN-FSCM-PF |
| SAP_CA_BC_IC_LND_APM_DSP_PC | Advanced Payment Management - Configuration Display | /PF1/NUM_RANGE_RE |  | /PF1/NUM_RANGE_RE | Maintain Number Ranges for Recalls |  | FIN-FSCM-PF | FIN-FSCM-PF |
| SAP_CA_BC_IC_LND_APM_DSP_PC | Advanced Payment Management - Configuration Display | /PF1/51000134 | S_PF1_51000134_03_TRAN | /PF1/V_EH_PO_REV | Define Response Types for Rejection |  | FIN-FSCM-PF | FIN-FSCM-PF |
| SAP_CA_BC_IC_LND_CTR_DSP_PC | TRM Content - Configuration Display | TIC1 |  | SIMG_CFMENUCONTTIC1 | Define Number Range for Option and Future Master Data |  | FIN-FSCM-TRM | FI-CNT-GL |
| SAP_CA_BC_IC_LND_CTR_DSP_PC | TRM Content - Configuration Display | S_ER9_11002289 | S_ER9_11002289_TRAN | SIMG_CFMENUCONTTIC1 | Define Number Range for Option and Future Master Data |  | FIN-FSCM-TRM | FI-CNT-GL |
| SAP_CA_BC_IC_LND_FIN_AR1_PC | Accounts Receivable - System Specific Configuration | S_E91_86000010 | S_E91_86000010_TRAN | SEPA_NR_CUST | Assign Number Range Intervals | 102561 | FI-AR-AR | CA-BK-SEP-2CL |
| SAP_CA_BC_IC_LND_FIN_AR1_PC | Accounts Receivable - System Specific Configuration | SEPA_NR_CUST |  | SEPA_NR_CUST | Assign Number Range Intervals | 102561 | FI-AR-AR | CA-BK-SEP-2CL |
| SAP_CA_BC_IC_LND_FIN_AR1_PC | Accounts Receivable - System Specific Configuration | SEPA_NR_MT | SEPA_NR_MT_TRAN | SEPA_NR_MT | Define Number Range Intervals | 102541 | FI-AR-AR | CA-BK-SEP-2CL |
| SAP_CA_BC_IC_LND_FIN_AR1_PC | Accounts Receivable - System Specific Configuration | S_E91_86000009 | S_E91_86000009_TRAN | SEPA_NR_MT | Define Number Range Intervals | 102541 | FI-AR-AR | CA-BK-SEP-2CL |
| SAP_CA_BC_IC_LND_FIN_AR1_PC | Accounts Receivable - System Specific Configuration | SEPA_NR_MT | SEPA_NR_MT_TRAN | SEPA_NR_MT | Define Number Range Intervals | 102541 | FI-AR-AR | CA-BK-SEP-2CL |
| SAP_CORE_BC_BCT_IMG_SCO_PC | Implementation Activities - Scoped Activities | SIMG_ACTIVITY_DOCU | SIMG_ACTIVITY_DOCU_TRAN |  |  |  | BC-CUS-TOL-IMG |  |
| SAP_CORE_BC_BCT_IMG_SCO_PC | Implementation Activities - Scoped Activities | SIMG | SIMG_PC_TRAN |  |  |  | BC-CUS-TOL-IMG |  |
| SAP_CA_BC_IC_LND_FIN_SR_SK_PC | Statutory Reporting for Slovakia - Configuration | S_ERX_29000321 | S_ERX_29000321_TRAN | FISKVATCV_GOODST | Assign Goods Type to Classification Code | 106952 | FI-LOC-FI-SK | FI-LOC-FI-SK |
| SAP_CA_BC_IC_LND_FIN_AF_RO_PC | Statutory Reporting Audit File for Romania - Configuration | S_ER1_70001565 | S_ER1_70001565_TRAN | FKKID_RO_CINCA_V | Map Contract Accounting Document Types to Invoice Types | 107088 | FI-LOC-FI-RO | CA-GTF-CSC-DRC |
| SAP_CA_BC_IC_LND_FIN_AF_RO_PC | Statutory Reporting Audit File for Romania - Configuration | S_ER1_70001564 | S_ER1_70001564_TRAN | FKKID_RO_CDOCCAV | Define Document Types for Reporting in Contract Accounting | 107087 | FI-LOC-FI-RO | CA-GTF-CSC-DRC |
| SAP_CA_BC_IC_LND_FIN_AF_RO_PC | Statutory Reporting Audit File for Romania - Configuration | S_ER1_70001566 | S_ER1_70001566_TRAN | FKKID_RO_CINCI_V | Map Invoice Types for Invoicing Documents in Convergent Invoicing | 107089 | FI-LOC-FI-RO | CA-GTF-CSC-DRC |
| SAP_CA_BC_IC_LND_FIN_AF_RO_PC | Statutory Reporting Audit File for Romania - Configuration | FKKID_RO_CINCI | FKKID_RO_CINCI_TRAN | FKKID_RO_CINCI_V | Map Invoice Types for Invoicing Documents in Convergent Invoicing | 107089 | FI-LOC-FI-RO | CA-GTF-CSC-DRC |
| SAP_CA_BC_IC_LND_FIN_AF_RO_PC | Statutory Reporting Audit File for Romania - Configuration | FKKID_RO_CINCA | FKKID_RO_CINCA_TRAN | FKKID_RO_CINCA_V | Map Contract Accounting Document Types to Invoice Types | 107088 | FI-LOC-FI-RO | CA-GTF-CSC-DRC |
| SAP_CA_BC_IC_LND_FIN_AF_RO_PC | Statutory Reporting Audit File for Romania - Configuration | FKKID_RO_CDOCCA | FKKID_RO_CDOCCA_TRAN | FKKID_RO_CDOCCAV | Define Document Types for Reporting in Contract Accounting | 107087 | FI-LOC-FI-RO | CA-GTF-CSC-DRC |
| SAP_CA_BC_IC_LND_AP_DSP_PC | Accounts Payable - Configuration Display | S_E91_86000156 | S_E91_86000156_03_TRAN | FAP_C_CMP_CONF | Configure Manual Payments |  | FI-AP-AP | FI-AP-AP-B-2CL |
| SAP_CA_BC_IC_LND_AP_DSP_PC | Accounts Payable - Configuration Display | FBN2 |  | FBN2_PAYTORDER | Define Number Ranges for Payment Orders |  | FI-AP-AP | FI-AP-AP-B-2CL |
| SAP_CA_BC_IC_LND_AP_DSP_PC | Accounts Payable - Configuration Display | S_ER1_70001501 | S_ER1_70001501_03_TRAN | SIMG_FIAP_GUAR | Define Alternative Reconciliation Accounts for Guarantees Received |  | FI-AP-AP | FI-FIO-AP-2CL |
| SAP_CA_BC_IC_LND_AP_DSP_PC | Accounts Payable - Configuration Display | OBXT |  | SIMG_FIAP_GUAR | Define Alternative Reconciliation Accounts for Guarantees Received |  | FI-AP-AP | FI-FIO-AP-2CL |
| SAP_CA_BC_IC_LND_AP_DSP_PC | Accounts Payable - Configuration Display | S_ER9_11001092 | S_ER9_11001092_03_TRAN | FBN2_PAYTORDER | Define Number Ranges for Payment Orders |  | FI-AP-AP | FI-AP-AP-B-2CL |
| SAP_CA_BC_IC_LND_RFM_SEGMN_PC | Retail Segmentation - Configuration | S_ER1_70001913 | S_ER1_70001913_TRAN | RTL_SEGMN_BASE_ACTVT | Activate Business Function 'Retail Segmentation Base Scope' | 107383 | LO-RFM | LO-RFM-SGT-2CL |
| SAP_CA_BC_IC_LND_RFM_SEGMN_PC | Retail Segmentation - Configuration | RTL_SEGMN_BASE_ACTVT |  | RTL_SEGMN_BASE_ACTVT | Activate Business Function 'Retail Segmentation Base Scope' | 107383 | LO-RFM | LO-RFM-SGT-2CL |
| SAP_CA_BC_IC_LND_RFM_SEGMN_PC | Retail Segmentation - Configuration | S_ER1_70001914 | S_ER1_70001914_TRAN | RTL_SEGMTN_ACTVT | Activate Business Function ‘Retail Segmentation' | 107384 | LO-RFM | LO-RFM-SGT-2CL |
| SAP_CA_BC_IC_LND_RFM_SEGMN_PC | Retail Segmentation - Configuration | RTL_SEGMTN_ACTVT |  | RTL_SEGMTN_ACTVT | Activate Business Function ‘Retail Segmentation' | 107384 | LO-RFM | LO-RFM-SGT-2CL |
| SAP_CA_BC_IC_LND_FI_CR_DSP_PC | Credit Management - Configuration Display | S_ER9_11001677 | S_ER9_11001677_03_TRAN | FIN_CR_COMM_TYPEST | Define Liability Categories - Only Texts for Content Delivery |  | FIN-FSCM-CR | FIN-FSCM-CR-2CL |
| SAP_CA_BC_IC_LND_FI_CR_DSP_PC | Credit Management - Configuration Display | S_SE6_85000017 | S_SE6_85000017_03_TRAN | CR_UDMV_SPS_ADMIN | Define Derivation of Element Types |  | FIN-FSCM-CR | FIN-FSCM-CR-2CL |
| SAP_CA_BC_IC_LND_FI_CR_DSP_PC | Credit Management - Configuration Display | S_ER1_70001505 | S_ER1_70001505_03_TRAN | UKM_DCD_NRI | Maintain Number Range Intervals for Documented Credit Decisions |  | FIN-FSCM-CR | FIN-FSCM-CR-2CL |
| SAP_CA_BC_IC_LND_FI_CR_DSP_PC | Credit Management - Configuration Display | UKM_DCD_NRI |  | UKM_DCD_NRI | Maintain Number Range Intervals for Documented Credit Decisions |  | FIN-FSCM-CR | FIN-FSCM-CR-2CL |
| SAP_CA_BC_IC_LND_EAM_PTW_PC | Plant Maintenance Permit To Work - Configuration | S_ER9_52003552 | S_ER9_52003552_TRAN | _WCMPTW_00003 | Maintain Permit to Work Profile for Planning Plant | 107252 | PM | PM-WCM-2CL |
| SAP_CA_BC_IC_LND_EAM_PTW_PC | Plant Maintenance Permit To Work - Configuration | S_ER9_52003550 | S_ER9_52003550_TRAN | _WCMPTW_00001 | Define Work Permit Types | 107253 | PM | PM-WCM-2CL |
| SAP_CA_BC_IC_LND_EAM_PTW_PC | Plant Maintenance Permit To Work - Configuration | S_ER9_52004067 | S_ER9_52004067_TRAN | _WCMPTW_00010 | Define Work Permit Template Types | 107249 | PM | PM-WCM-2CL |
| SAP_CA_BC_IC_LND_EAM_PTW_PC | Plant Maintenance Permit To Work - Configuration | S_ER9_52003551 | S_ER9_52003551_TRAN | _WCMPTW_00002 | Define Nature of Work | 107251 | PM | PM-WCM-2CL |
| SAP_CA_BC_IC_LND_EAM_PTW_PC | Plant Maintenance Permit To Work - Configuration | S_ER9_52003997 | S_ER9_52003997_TRAN | _WCMPTW_00009 | Assign Nature of Work | 107248 | PM | PM-WCM-2CL |
| SAP_CA_BC_IC_LND_EAM_PTW_PC | Plant Maintenance Permit To Work - Configuration | S_ER9_52003925 | S_ER9_52003925_TRAN | _WCMPTW_00006 | Maintain Number Ranges | 107250 | PM | PM-WCM-2CL |
| SAP_CA_BC_IC_LND_EAM_PTW_PC | Plant Maintenance Permit To Work - Configuration | WCC5 |  | _WCMPTW_00006 | Maintain Number Ranges | 107250 | PM | PM-WCM-2CL |
| SAP_CA_BC_IC_LND_AR_DSP_PC | Accounts Receivable - Configuration Display | S_ER1_70001503 | S_ER1_70001503_03_TRAN | SIMG_FIAR_GUAR | Define Alternative Reconciliation Accounts for Guarantees Made |  | FI-AR-AR | FI-FIO-AR-2CL |
| SAP_CA_BC_IC_LND_AR_DSP_PC | Accounts Receivable - Configuration Display | OBXY |  | SIMG_FIAR_GUAR | Define Alternative Reconciliation Accounts for Guarantees Made |  | FI-AR-AR | FI-FIO-AR-2CL |
| SAP_CA_BC_IC_LND_AR_DSP_PC | Accounts Receivable - Configuration Display | S_ALR_87002833 | S_ALR_87002833_03_TRAN | SIMG_CFMENUORFBOB84 | Assign Forms for Interest Indicators |  | FI-AR-AR | FI-AR-AR-C-2CL |
| SAP_CA_BC_IC_LND_FIN_GL_AT_PC | General Ledger for Austria - Configuration | S_ER1_70001782 | S_ER1_70001782_TRAN | FIATVC_JAB_MAP | Define Mapping for Financial Statement Version (ERV-JAb) | 107258 | FI-LOC-FI-AT | FI-GL-GL-2CL |
| SAP_CA_BC_IC_LND_FIN_GL_AT_PC | General Ledger for Austria - Configuration | FIATVC_JAB_MAP |  | FIATVC_JAB_MAP | Define Mapping for Financial Statement Version (ERV-JAb) | 107258 | FI-LOC-FI-AT | FI-GL-GL-2CL |
| SAP_CA_BC_IC_LND_FIN_APRD_PC | Accounts Payable for Invoice Receipt Date - Configuration | S_ER1_70001807 | S_ER1_70001807_TRAN | IDFIVATV_DEF1 | Activate Invoice Receipt Date | 107263 | FI-LOC | FI-LOC-FI-CZ |
| SAP_CA_BC_IC_LND_FIN_APRD_PC | Accounts Payable for Invoice Receipt Date - Configuration | IDFIVATV_DEF1T | IDFIVATV_DEF1T_TRAN | IDFIVATV_DEF1 | Activate Invoice Receipt Date | 107263 | FI-LOC | FI-LOC-FI-CZ |
| SAP_CA_BC_IC_LND_PSM_DSP_PC | Public Sector Management - Configuration Display | S_ER9_11001935 | S_ER9_11001935_03_TRAN | PSM_S4C_SPL_GRP | Define Rule Groups |  | PSM | PSM-FM |
| SAP_CA_BC_IC_LND_PSM_DSP_PC | Public Sector Management - Configuration Display | S_ER1_84000041 | S_ER1_84000041_03_TRAN | PSM_S4C_AADT_NR | Define Document Number Ranges for Account Assignment Distribution |  | PSM | PSM |
| SAP_CA_BC_IC_LND_PSM_DSP_PC | Public Sector Management - Configuration Display | PSM_S4C_AADT_NR |  | PSM_S4C_AADT_NR | Define Document Number Ranges for Account Assignment Distribution |  | PSM | PSM |
| SAP_CA_BC_IC_LND_PSM_DSP_PC | Public Sector Management - Configuration Display | S_ER9_11001491 | S_ER9_11001491_03_TRAN | PSM_S4C_V_FMRE_MM_CA | Permit Earmarked Funds in Purchase Orders |  | PSM | PSM-FM-PO-EF |
| SAP_CA_BC_IC_LND_PSM_DSP_PC | Public Sector Management - Configuration Display | S_ER9_11001934 | S_ER9_11001934_03_TRAN | PSM_S4C_SPL_AUTG | Define Authorization Groups |  | PSM | PSM-FM |
| SAP_CA_BC_IC_LND_PSM_DSP_PC | Public Sector Management - Configuration Display | S_ER9_11001478 | S_ER9_11001478_03_TRAN | PSM_S4C_FMRESGLOBALS | Maintain Global Settings |  | PSM | PSM-FM-PO-EF |
| SAP_CA_BC_IC_LND_PSM_DSP_PC | Public Sector Management - Configuration Display | S_ER9_11001479 | S_ER9_11001479_03_TRAN | PSM_S4C_V_TREV | Define Field Status Variant |  | PSM | PSM-FM-PO-EF |
| SAP_CA_BC_IC_LND_PSM_DSP_PC | Public Sector Management - Configuration Display | S_ER9_11001480 | S_ER9_11001480_03_TRAN | PSM_S4C_V_TREVBUKRS | Assign Field Status Variant to Company Code |  | PSM | PSM-FM-PO-EF |
| SAP_CA_BC_IC_LND_PSM_DSP_PC | Public Sector Management - Configuration Display | S_ER9_11001481 | S_ER9_11001481_03_TRAN | PSM_S4C_V_TREG | Define Field Status Groups |  | PSM | PSM-FM-PO-EF |
| SAP_CA_BC_IC_LND_PSM_DSP_PC | Public Sector Management - Configuration Display | S_ER9_11001482 | S_ER9_11001482_03_TRAN | PSM_S4C_V_TREFST | Define Field Selection String |  | PSM | PSM-FM-PO-EF |
| SAP_CA_BC_IC_LND_PSM_DSP_PC | Public Sector Management - Configuration Display | S_ER9_11001483 | S_ER9_11001483_03_TRAN | PSM_S4C_V_TREVGFST | Assign Field Selection String to Field Status Variant/Group |  | PSM | PSM-FM-PO-EF |
| SAP_CA_BC_IC_LND_PSM_DSP_PC | Public Sector Management - Configuration Display | S_ER9_11001489 | S_ER9_11001489_03_TRAN | PSM_S4C_V_FMRACCMVAS | Assign Rules |  | PSM | PSM-FM-PO-EF |
| SAP_CA_BC_IC_LND_PSM_DSP_PC | Public Sector Management - Configuration Display | S_ER9_11001484 | S_ER9_11001484_03_TRAN | PSM_S4C_V_TRE01 | Maintain Reference Template Types |  | PSM | PSM-FM-PO-EF |
| SAP_CA_BC_IC_LND_PSM_DSP_PC | Public Sector Management - Configuration Display | S_ER9_11001488 | S_ER9_11001488_03_TRAN | PSM_S4C_V_FMRACCMVA | Define Rules for Account Assignment Transfer |  | PSM | PSM-FM-PO-EF |
| SAP_CA_BC_IC_LND_PSM_DSP_PC | Public Sector Management - Configuration Display | S_ER1_84000036 | S_ER1_84000036_03_TRAN | PSM_S4C_V_TIVCAAPPLA | Activate Application for Flexible Real Estate Management |  | PSM | PSM |
| SAP_CA_BC_IC_LND_PSM_DSP_PC | Public Sector Management - Configuration Display | S_ER1_84000007 | S_ER1_84000007_03_TRAN | PSM_S4C_GMCCSETTING | Define Company Code Settings for Grantee Management |  | PSM | PSM |
| SAP_CA_BC_IC_LND_PSM_DSP_PC | Public Sector Management - Configuration Display | S_ER1_84000012 | S_ER1_84000012_03_TRAN | PSM_S4C_GMSPLITRULES | Define GM Time Slice Splitting Rules |  | PSM | PSM |
| SAP_CA_BC_IC_LND_PSM_DSP_PC | Public Sector Management - Configuration Display | S_ER1_84000013 | S_ER1_84000013_03_TRAN | PSM_S4C_GMCSRULES | Define Cost Sharing Rules |  | PSM | PSM |
| SAP_CA_BC_IC_LND_PSM_DSP_PC | Public Sector Management - Configuration Display | S_ER1_84000014 | S_ER1_84000014_03_TRAN | PSM_S4C_GMBR | Define GM Billing Rules |  | PSM | PSM |
| SAP_CA_BC_IC_LND_PSM_DSP_PC | Public Sector Management - Configuration Display | S_ER1_84000020 | S_ER1_84000020_03_TRAN | PSM_S4C_GMBILGREQ_NR | Define Number Range for Grant Billing Requests |  | PSM | PSM |
| SAP_CA_BC_IC_LND_PSM_DSP_PC | Public Sector Management - Configuration Display | S_ER1_84000018 | S_ER1_84000018_03_TRAN | PSM_S4C_GMIDCRULES | Define Indirect Cost Rules |  | PSM | PSM |
| SAP_CA_BC_IC_LND_PSM_DSP_PC | Public Sector Management - Configuration Display | S_ER6_68000015 | S_ER6_68000015_03_TRAN | PSM_S4C_FM_FM01_ST | Assign Field Selection Strings to FM Area |  | PSM | PSM |
| SAP_CA_BC_IC_LND_PSM_DSP_PC | Public Sector Management - Configuration Display | GMBILGREQ_NUMRANGE |  | PSM_S4C_GMBILGREQ_NR | Define Number Range for Grant Billing Requests |  | PSM | PSM |
| SAP_CA_BC_IC_LND_PSM_DSP_PC | Public Sector Management - Configuration Display | S_ER6_68000017 | S_ER6_68000017_03_TRAN | PSM_S4C_FMMDST_3 | Edit Field Selection Strings for Funds |  | PSM | PSM |
| SAP_CA_BC_IC_LND_PSM_DSP_PC | Public Sector Management - Configuration Display | S_ER6_68000019 | S_ER6_68000019_03_TRAN | PSM_S4C_FMZUCO | Define Field Status for FM Account Assignments |  | PSM | PSM |
| SAP_CA_BC_IC_LND_PSM_DSP_PC | Public Sector Management - Configuration Display | S_ER9_11001114 | S_ER9_11001114_03_TRAN | PSM_S4C_BDGTCNSTY | Define Budget Consumption Type |  | PSM | PSM-FM-UP |
| SAP_CA_BC_IC_LND_PSM_DSP_PC | Public Sector Management - Configuration Display | S_ER9_11001115 | S_ER9_11001115_03_TRAN | PSM_S4C_GLACCTX | Define FM Settings for G/L Accounts |  | PSM | PSM-FM-UP |
| SAP_CA_BC_IC_LND_FIN_CI_PT_PC | Contract Accounting for Portugal - Configuration | S_ERX_29000595 | S_ERX_29000595_TRAN | _FICAINV_FQ2665 | Define Tax Codes for Correction Invoices | 107125 | FI-LOC-IAM | FI-LOC-CA-XX |
| SAP_CA_BC_IC_LND_FIN_CI_PT_PC | Contract Accounting for Portugal - Configuration | FQ2665 |  | _FICAINV_FQ2665 | Define Tax Codes for Correction Invoices | 107125 | FI-LOC-IAM | FI-LOC-CA-XX |
| SAP_CA_BC_IC_LND_PSP_DSP_PC | Professional Services Projects - Configuration Display | /CPD/90000006 | CPD_90000006_03_TRAN | /CPD/VFC_RTYP | Define Resource Types |  | CA-CPD-SS | CA-CPD-SS |
| SAP_CA_BC_IC_LND_PSP_DSP_PC | Professional Services Projects - Configuration Display | /CPD/90000011 | CPD_90000011_03_TRAN | /CPD/VC_STG_PROFILE | Make Settings for Stages |  | CA-CPD-SS | CA-CPD-SS |
| SAP_CA_BC_IC_LND_PSP_DSP_PC | Professional Services Projects - Configuration Display | /CPD/90000023 | CPD_90000023_03_TRAN | /CPD/VC_STS_PROFILE | Make Settings for Status Management |  | CA-CPD-SS | CA-CPD-SS |
| SAP_CA_BC_IC_LND_PSP_DSP_PC | Professional Services Projects - Configuration Display | /CPD/90000040 | CPD_90000040_03_TRAN | /CPD/VCPWS_MP_STATUS | Define Settings for Status Management |  | CA-CPD-SS | CA-CPD-SS |
| SAP_CA_BC_IC_LND_CUR_DSP_PC | Currencies - Configuration | OY03 |  | SIMG_CFMENUSAPCOY03 | Check Currency Codes | 107225 | BC-SRV-BSF-CUR | BC-SRV-BSF-CUR-2CL |
| SAP_CA_BC_IC_LND_CUR_DSP_PC | Currencies - Configuration | S_BCE_68000191 | S_BCE_68000191_03_TRAN | SIMG_CFMENUSAPCOY03 | Check Currency Codes | 107225 | BC-SRV-BSF-CUR | BC-SRV-BSF-CUR-2CL |
| SAP_CA_BC_IC_LND_FIN_CA_PT_PC | Contract Accounting for Portugal - Configuration | S_EMI_14000001 | S_EMI_14000001_TRAN | FICA_PT_DFKK_PT_NUMR | Define Series and SAF-T Document Types | 500730 | FI-LOC-IAM | FI-LOC-CA-PT |
| SAP_CA_BC_IC_LND_FIN_CA_PT_PC | Contract Accounting for Portugal - Configuration | FICA_PTDFKKPTNUMR |  | FICA_PT_DFKK_PT_NUMR | Define Series and SAF-T Document Types | 500730 | FI-LOC-IAM | FI-LOC-CA-PT |
| SAP_CA_BC_IC_LND_FIN_GL_BG_PC | General Ledger for Bulgaria - Configuration | V_BGSAFT_VALANL |  | V_BGSAFT_VALANL | Define Valid Analysis Types | 107276 | FI-LOC-FI-BG | FI-LOC-SAF-BG |
| SAP_CA_BC_IC_LND_FIN_GL_BG_PC | General Ledger for Bulgaria - Configuration | V_BGSAFT_UOMMAP |  | V_BGSAFT_UOMMAP | Map Unit of Measures | 107278 | FI-LOC-FI-BG | FI-LOC-SAF-BG |
| SAP_CA_BC_IC_LND_FIN_GL_BG_PC | General Ledger for Bulgaria - Configuration | V_BGSAFT_TAXCOD |  | V_BGSAFT_TAXCOD | Define Tax Codes | 107272 | FI-LOC-FI-BG | FI-LOC-SAF-BG |
| SAP_CA_BC_IC_LND_FIN_GL_BG_PC | General Ledger for Bulgaria - Configuration | V_BGSAFT_TAXTYP |  | V_BGSAFT_TAXTYP | Define Tax Types | 107271 | FI-LOC-FI-BG | FI-LOC-SAF-BG |
| SAP_CA_BC_IC_LND_FIN_GL_BG_PC | General Ledger for Bulgaria - Configuration | V_BGSAFT_TAXMAP |  | V_BGSAFT_TAXMAP | Map Tax Codes | 107273 | FI-LOC-FI-BG | FI-LOC-SAF-BG |
| SAP_CA_BC_IC_LND_FIN_GL_BG_PC | General Ledger for Bulgaria - Configuration | V_BGSAFT_UOM |  | V_BGSAFT_UOM | Define Unit of Measures | 107277 | FI-LOC-FI-BG | FI-LOC-SAF-BG |
| SAP_CA_BC_IC_LND_FIN_GL_BG_PC | General Ledger for Bulgaria - Configuration | V_BGSAFT_SPGLIE |  | V_BGSAFT_SPGLIE | Special G/L Indicators for Exclusion from Customer/Vendor Balances | 107285 | FI-LOC-FI-BG | FI-LOC-SAF-BG |
| SAP_CA_BC_IC_LND_FIN_GL_BG_PC | General Ledger for Bulgaria - Configuration | V_BGSAFT_SPGLI |  | V_BGSAFT_SPGLI | Special G/L Indicators Relevant for Invoices Lines | 107284 | FI-LOC-FI-BG | FI-LOC-SAF-BG |
| SAP_CA_BC_IC_LND_FIN_GL_BG_PC | General Ledger for Bulgaria - Configuration | V_BGSAFT_RELPAR |  | V_BGSAFT_RELPAR | Related Party | 107289 | FI-LOC-FI-BG | FI-LOC-SAF-BG |
| SAP_CA_BC_IC_LND_FIN_GL_BG_PC | General Ledger for Bulgaria - Configuration | V_BGSAFT_PYMCHM |  | V_BGSAFT_PYMCHM | Map Payment Methods | 107281 | FI-LOC-FI-BG | FI-LOC-SAF-BG |
| SAP_CA_BC_IC_LND_FIN_GL_BG_PC | General Ledger for Bulgaria - Configuration | V_BGSAFT_PAYMTH |  | V_BGSAFT_PAYMTH | Payment Method | 107280 | FI-LOC-FI-BG | FI-LOC-SAF-BG |
| SAP_CA_BC_IC_LND_FIN_GL_BG_PC | General Ledger for Bulgaria - Configuration | V_BGSAFT_PAYMCH |  | V_BGSAFT_PAYMCH | Payment Mechanism | 107279 | FI-LOC-FI-BG | FI-LOC-SAF-BG |
| SAP_CA_BC_IC_LND_FIN_GL_BG_PC | General Ledger for Bulgaria - Configuration | V_BGSAFT_JRNLID |  | V_BGSAFT_JRNLID | Define Journal ID Code | 107286 | FI-LOC-FI-BG | FI-LOC-SAF-BG |
| SAP_CA_BC_IC_LND_FIN_GL_BG_PC | General Ledger for Bulgaria - Configuration | V_BGSAFT_GOODSV |  | V_BGSAFT_GOODSV | Classify Material Types | 107287 | FI-LOC-FI-BG | FI-LOC-SAF-BG |
| SAP_CA_BC_IC_LND_FIN_GL_BG_PC | General Ledger for Bulgaria - Configuration | V_BGSAFT_WHTMAP |  | V_BGSAFT_WHTMAP | Map Extended Withholding Tax Types and Codes | 107274 | FI-LOC-FI-BG | FI-LOC-SAF-BG |
| SAP_CA_BC_IC_LND_FIN_GL_BG_PC | General Ledger for Bulgaria - Configuration | V_BGSAFT_EXSTDOC |  | V_BGSAFT_EXSTDOC | Define Document Statuses for Exclusion | 107283 | FI-LOC-FI-BG | FI-LOC-SAF-BG |
| SAP_CA_BC_IC_LND_FIN_GL_BG_PC | General Ledger for Bulgaria - Configuration | V_BGSAFT_DOCPAY |  | V_BGSAFT_DOCPAY | Define Payment Document Types for Reporting | 107282 | FI-LOC-FI-BG | FI-LOC-SAF-BG |
| SAP_CA_BC_IC_LND_FIN_GL_BG_PC | General Ledger for Bulgaria - Configuration | V_BGSAFT_DBHINT |  | V_BGSAFT_DBHINT | DB Hints | 107288 | FI-LOC-FI-BG | FI-LOC-SAF-BG |
| SAP_CA_BC_IC_LND_FIN_GL_BG_PC | General Ledger for Bulgaria - Configuration | V_BGSAFT_ANALIS |  | V_BGSAFT_ANALIS | Valid Analysis Types | 107275 | FI-LOC-FI-BG | FI-LOC-SAF-BG |
| SAP_CA_BC_IC_LND_FIN_GL_BG_PC | General Ledger for Bulgaria - Configuration | V_BGSAFT_ACCTYPE |  | V_BGSAFT_ACCTYPE | Accounting Type | 107269 | FI-LOC-FI-BG | FI-LOC-SAF-BG |
| SAP_CA_BC_IC_LND_FIN_GL_BG_PC | General Ledger for Bulgaria - Configuration | V_BGSAFT_ACCMAP |  | V_BGSAFT_ACCMAP | Classify G/L Accounts | 107270 | FI-LOC-FI-BG | FI-LOC-SAF-BG |
| SAP_CA_BC_IC_LND_FIN_GL_BG_PC | General Ledger for Bulgaria - Configuration | S_ER1_70001772 | S_ER1_70001772_TRAN | V_BGSAFT_DBHINT | DB Hints | 107288 | FI-LOC-FI-BG | FI-LOC-SAF-BG |
| SAP_CA_BC_IC_LND_FIN_GL_BG_PC | General Ledger for Bulgaria - Configuration | S_ER1_70001771 | S_ER1_70001771_TRAN | V_BGSAFT_ANALIS | Valid Analysis Types | 107275 | FI-LOC-FI-BG | FI-LOC-SAF-BG |
| SAP_CA_BC_IC_LND_FIN_GL_BG_PC | General Ledger for Bulgaria - Configuration | S_ER1_70001770 | S_ER1_70001770_TRAN | V_BGSAFT_VALANL | Define Valid Analysis Types | 107276 | FI-LOC-FI-BG | FI-LOC-SAF-BG |
| SAP_CA_BC_IC_LND_FIN_GL_BG_PC | General Ledger for Bulgaria - Configuration | S_ER1_70001769 | S_ER1_70001769_TRAN | V_BGSAFT_PAYMCH | Payment Mechanism | 107279 | FI-LOC-FI-BG | FI-LOC-SAF-BG |
| SAP_CA_BC_IC_LND_FIN_GL_BG_PC | General Ledger for Bulgaria - Configuration | S_ER1_70001768 | S_ER1_70001768_TRAN | V_BGSAFT_RELPAR | Related Party | 107289 | FI-LOC-FI-BG | FI-LOC-SAF-BG |
| SAP_CA_BC_IC_LND_FIN_GL_BG_PC | General Ledger for Bulgaria - Configuration | S_ER1_70001767 | S_ER1_70001767_TRAN | V_BGSAFT_ACCTYPE | Accounting Type | 107269 | FI-LOC-FI-BG | FI-LOC-SAF-BG |
| SAP_CA_BC_IC_LND_FIN_GL_BG_PC | General Ledger for Bulgaria - Configuration | S_ER1_70001766 | S_ER1_70001766_TRAN | V_BGSAFT_JRNLID | Define Journal ID Code | 107286 | FI-LOC-FI-BG | FI-LOC-SAF-BG |
| SAP_CA_BC_IC_LND_FIN_GL_BG_PC | General Ledger for Bulgaria - Configuration | S_ER1_70001765 | S_ER1_70001765_TRAN | V_BGSAFT_PAYMTH | Payment Method | 107280 | FI-LOC-FI-BG | FI-LOC-SAF-BG |
| SAP_CA_BC_IC_LND_FIN_GL_BG_PC | General Ledger for Bulgaria - Configuration | S_ER1_70001764 | S_ER1_70001764_TRAN | V_BGSAFT_SPGLIE | Special G/L Indicators for Exclusion from Customer/Vendor Balances | 107285 | FI-LOC-FI-BG | FI-LOC-SAF-BG |
| SAP_CA_BC_IC_LND_FIN_GL_BG_PC | General Ledger for Bulgaria - Configuration | S_ER1_70001763 | S_ER1_70001763_TRAN | V_BGSAFT_SPGLI | Special G/L Indicators Relevant for Invoices Lines | 107284 | FI-LOC-FI-BG | FI-LOC-SAF-BG |
| SAP_CA_BC_IC_LND_FIN_GL_BG_PC | General Ledger for Bulgaria - Configuration | S_ER1_70001762 | S_ER1_70001762_TRAN | V_BGSAFT_DOCPAY | Define Payment Document Types for Reporting | 107282 | FI-LOC-FI-BG | FI-LOC-SAF-BG |
| SAP_CA_BC_IC_LND_FIN_GL_BG_PC | General Ledger for Bulgaria - Configuration | S_ER1_70001761 | S_ER1_70001761_TRAN | V_BGSAFT_TAXMAP | Map Tax Codes | 107273 | FI-LOC-FI-BG | FI-LOC-SAF-BG |
| SAP_CA_BC_IC_LND_FIN_GL_BG_PC | General Ledger for Bulgaria - Configuration | S_ER1_70001760 | S_ER1_70001760_TRAN | V_BGSAFT_UOMMAP | Map Unit of Measures | 107278 | FI-LOC-FI-BG | FI-LOC-SAF-BG |
| SAP_CA_BC_IC_LND_FIN_GL_BG_PC | General Ledger for Bulgaria - Configuration | S_ER1_70001759 | S_ER1_70001759_TRAN | V_BGSAFT_GOODSV | Classify Material Types | 107287 | FI-LOC-FI-BG | FI-LOC-SAF-BG |
| SAP_CA_BC_IC_LND_FIN_GL_BG_PC | General Ledger for Bulgaria - Configuration | S_ER1_70001758 | S_ER1_70001758_TRAN | V_BGSAFT_UOM | Define Unit of Measures | 107277 | FI-LOC-FI-BG | FI-LOC-SAF-BG |
| SAP_CA_BC_IC_LND_FIN_GL_BG_PC | General Ledger for Bulgaria - Configuration | S_ER1_70001757 | S_ER1_70001757_TRAN | V_BGSAFT_PYMCHM | Map Payment Methods | 107281 | FI-LOC-FI-BG | FI-LOC-SAF-BG |
| SAP_CA_BC_IC_LND_FIN_GL_BG_PC | General Ledger for Bulgaria - Configuration | S_ER1_70001754 | S_ER1_70001754_TRAN | V_BGSAFT_TAXCOD | Define Tax Codes | 107272 | FI-LOC-FI-BG | FI-LOC-SAF-BG |
| SAP_CA_BC_IC_LND_FIN_GL_BG_PC | General Ledger for Bulgaria - Configuration | S_ER1_70001755 | S_ER1_70001755_TRAN | V_BGSAFT_WHTMAP | Map Extended Withholding Tax Types and Codes | 107274 | FI-LOC-FI-BG | FI-LOC-SAF-BG |
| SAP_CA_BC_IC_LND_FIN_GL_BG_PC | General Ledger for Bulgaria - Configuration | S_ER1_70001756 | S_ER1_70001756_TRAN | V_BGSAFT_EXSTDOC | Define Document Statuses for Exclusion | 107283 | FI-LOC-FI-BG | FI-LOC-SAF-BG |
| SAP_CA_BC_IC_LND_FIN_GL_BG_PC | General Ledger for Bulgaria - Configuration | S_ER1_70001753 | S_ER1_70001753_TRAN | V_BGSAFT_TAXTYP | Define Tax Types | 107271 | FI-LOC-FI-BG | FI-LOC-SAF-BG |
| SAP_CA_BC_IC_LND_FIN_GL_BG_PC | General Ledger for Bulgaria - Configuration | S_ER1_70001752 | S_ER1_70001752_TRAN | V_BGSAFT_ACCMAP | Classify G/L Accounts | 107270 | FI-LOC-FI-BG | FI-LOC-SAF-BG |
| SAP_CA_BC_IC_LND_DEP_DSP_PC | Object Dependencies - Configuration Display | S_ALR_87006904 | S_ALR_87006904_TRAN | SIMG_CFMENUOCU0CU10 | Edit Statuses |  | CA-GTF-DEP | CA-GTF-DEP-2CL |
| SAP_CA_BC_IC_LND_DEP_DSP_PC | Object Dependencies - Configuration Display | CU10 |  | SIMG_CFMENUOCU0CU10 | Edit Statuses |  | CA-GTF-DEP | CA-GTF-DEP-2CL |
| SAP_CA_BC_IC_LND_DEP_DSP_PC | Object Dependencies - Configuration Display | CU16 |  | SIMG_CFMENUOCU0CU16 | Edit Statuses |  | CA-GTF-DEP | CA-GTF-DEP-2CL |
| SAP_CA_BC_IC_LND_DEP_DSP_PC | Object Dependencies - Configuration Display | CU18 |  | SIMG_CFMENUOCU0CU18 | Maintain Settings |  | CA-GTF-DEP | CA-GTF-DEP-2CL |
| SAP_CA_BC_IC_LND_DEP_DSP_PC | Object Dependencies - Configuration Display | S_ALR_87006880 | S_ALR_87006880_TRAN | SIMG_CFMENUOCU0CU16 | Edit Statuses |  | CA-GTF-DEP | CA-GTF-DEP-2CL |
| SAP_CA_BC_IC_LND_DEP_DSP_PC | Object Dependencies - Configuration Display | S_ALR_87006885 | S_ALR_87006885_TRAN | SIMG_CFMENUOCU0CU18 | Maintain Settings |  | CA-GTF-DEP | CA-GTF-DEP-2CL |
| SAP_CA_BC_IC_LND_DEP_DSP_PC | Object Dependencies - Configuration Display | S_ALR_87006907 | S_ALR_87006907_TRAN | SIMG_CFMENUOCU0CU28 | Edit Statuses |  | CA-GTF-DEP | CA-GTF-DEP-2CL |
| SAP_CA_BC_IC_LND_DEP_DSP_PC | Object Dependencies - Configuration Display | CU28 |  | SIMG_CFMENUOCU0CU28 | Edit Statuses |  | CA-GTF-DEP | CA-GTF-DEP-2CL |
| SAP_CA_BC_IC_LND_DEP_DSP_PC | Object Dependencies - Configuration Display | S_ALR_87006856 | S_ALR_87006856_TRAN | SIMG_CFMENUOCU0CU30 | Edit Statuses |  | CA-GTF-DEP | CA-GTF-DEP-2CL |
| SAP_CA_BC_IC_LND_DEP_DSP_PC | Object Dependencies - Configuration Display | CU30 |  | SIMG_CFMENUOCU0CU30 | Edit Statuses |  | CA-GTF-DEP | CA-GTF-DEP-2CL |
| SAP_FIN_BC_TRM_BP_WF_CONF_PC | TRM - Configuration for Business Partner Workflow | F9582 | F9582_TRAN |  |  |  | FIN-FSCM-TRM |  |
| SAP_CA_BC_IC_LND_FIN_WT_JP_PC | Statutory Reporting WT for Japan - Configuration | S_ALR_87004858 | S_ALR_87004858_TRAN | SIMG_CFORFBT059MCR | Define Minimum Amounts per Withholding Tax Code | 107169 | FI-LOC-FI-JP | FI-AR-AR-2CL |
| SAP_CA_BC_IC_LND_FIN_WT_JP_PC | Statutory Reporting WT for Japan - Configuration | S_ALR_87004855 | S_ALR_87004855_TRAN | SIMG_CFORFBT059MTR | Define Minimum Amounts per Withholding Tax Type | 107170 | FI-LOC-FI-JP | FI-AR-AR-2CL |
| SAP_CA_BC_IC_LND_FIN_CA_TR_PC | Contract Accounting for Turkey - Configuration | S_ERX_29000490 | S_ERX_29000490_TRAN | VFICATR_ELPY_MAP | Assign SAP Document Type for Contract Accounting to E-Ledger Payment Method | 107165 | FI-LOC-IAM | FI-LOC-CA-XX |
| SAP_CA_BC_IC_LND_FIN_CA_TR_PC | Contract Accounting for Turkey - Configuration | SFICATR_DOTY_MAP |  | VFICATR_DOTY_MAP | Assign SAP Document Type for Contract Accounting to External Document Type | 107166 | FI-LOC-IAM | FI-LOC-CA-XX |
| SAP_CA_BC_IC_LND_FIN_CA_TR_PC | Contract Accounting for Turkey - Configuration | S_ERX_29000491 | S_ERX_29000491_TRAN | VFICATR_DOTY_MAP | Assign SAP Document Type for Contract Accounting to External Document Type | 107166 | FI-LOC-IAM | FI-LOC-CA-XX |
| SAP_CA_BC_IC_LND_FIN_CA_TR_PC | Contract Accounting for Turkey - Configuration | SFICATR_ELPY_MAP |  | VFICATR_ELPY_MAP | Assign SAP Document Type for Contract Accounting to E-Ledger Payment Method | 107165 | FI-LOC-IAM | FI-LOC-CA-XX |
| SAP_CA_BC_IC_LND_UOM_BCO_PC | Units of Measurement - Configuration | S_YI3_39001451 | S_YI3_39001451_TRAN | SMBC_ISOCODE | Maintain ISO Code for Units of Measurement |  | BC-SRV-ASF-UOM | BC-SRV-ASF-UOM |
| SAP_CA_BC_IC_LND_UOM_BCO_PC | Units of Measurement - Configuration | SMBC_ISOCODE |  | SMBC_ISOCODE | Maintain ISO Code for Units of Measurement |  | BC-SRV-ASF-UOM | BC-SRV-ASF-UOM |
| SAP_CA_BC_IC_LND_UOM_BCO_PC | Units of Measurement - Configuration | SMBC_DIMENSION |  | SMBC_DIMENSION | Maintain Dimension for Units of Measurement |  | BC-SRV-ASF-UOM | BC-SRV-ASF-UOM |
| SAP_CA_BC_IC_LND_UOM_BCO_PC | Units of Measurement - Configuration | S_YI3_39001454 | S_YI3_39001454_TRAN | SMBC_DIMENSION | Maintain Dimension for Units of Measurement |  | BC-SRV-ASF-UOM | BC-SRV-ASF-UOM |
| SAP_CA_BC_IC_LND_UOM_BCO_PC | Units of Measurement - Configuration | S_YI3_39001455 | S_YI3_39001455_TRAN | SMBC_UOM | Maintain Unit of Measurement |  | BC-SRV-ASF-UOM | BC-SRV-ASF-UOM |
| SAP_CA_BC_IC_LND_UOM_BCO_PC | Units of Measurement - Configuration | SMBC_UOM |  | SMBC_UOM | Maintain Unit of Measurement |  | BC-SRV-ASF-UOM | BC-SRV-ASF-UOM |
| SAP_CA_BC_IC_LND_FIN_EPC_PC | Third-Party Payment - Configuration | F9009 | F9009_TRAN |  |  |  | FI-LOC-IAM |  |
| SAP_CA_BC_IC_LND_FIN_EPC_PC | Third-Party Payment - Configuration | S_ER1_70001706 | S_ER1_70001706_TRAN | VIDFIEXPCFOTYC | Define Import Format Types |  | FI-LOC-IAM | FI-LOC-CA-PAY |
| SAP_CA_BC_IC_LND_FIN_EPC_PC | Third-Party Payment - Configuration | IDFIEXPC_FOTYCFG |  | VIDFIEXPCFOTYC | Define Import Format Types |  | FI-LOC-IAM | FI-LOC-CA-PAY |
| SAP_CA_BC_IC_LND_FIN_EPC_PC | Third-Party Payment - Configuration | S_ER1_70001707 | S_ER1_70001707_TRAN | MFD_F9009 | Map Format Data for Third-Party Payment |  | FI-LOC-IAM | CA-GTF-CSC-DME |
| SAP_CA_BC_IC_LND_FIN_EPC_PC | Third-Party Payment - Configuration | MFD_F9009 |  | MFD_F9009 | Map Format Data for Third-Party Payment |  | FI-LOC-IAM | CA-GTF-CSC-DME |
| SAP_CA_BC_IC_LND_FIN_EPC_PC | Third-Party Payment - Configuration | F9009 | F9009_TRAN |  |  |  | FI-LOC-IAM |  |
| SAP_CA_BC_IC_LND_FIN_EPC_PC | Third-Party Payment - Configuration | FKKIDEXPC_ZKCFG |  | V_TFKIDEXPC_ZK | Define Payment Lot Specifications | 107255 | FI-LOC-IAM | FI-LOC-CA |
| SAP_CA_BC_IC_LND_FIN_EPC_PC | Third-Party Payment - Configuration | S_ER1_70001775 | S_ER1_70001775_TRAN | V_TFKIDEXPC_ZK | Define Payment Lot Specifications | 107255 | FI-LOC-IAM | FI-LOC-CA |
| SAP_CA_BC_IC_LND_FIN_EPC_PC | Third-Party Payment - Configuration | S_ER1_70001776 | S_ER1_70001776_TRAN | V_TFKIDEXPC_RK | Define Return Lot Specifications | 107256 | FI-LOC-IAM | FI-LOC-CA |
| SAP_CA_BC_IC_LND_FIN_EPC_PC | Third-Party Payment - Configuration | FKKIDEXPC_RKCFG |  | V_TFKIDEXPC_RK | Define Return Lot Specifications | 107256 | FI-LOC-IAM | FI-LOC-CA |
| SAP_CA_BC_IC_LND_TS_DSP_PC | Timesheet - Configuration Display | S_ALR_87001244 | S_ALR_87001244_TRAN | CATS0201 | Set Up Data Entry Profiles |  | CA-TS-S4 | CA-TS-S4 |
| SAP_CA_BC_IC_LND_TS_DSP_PC | Timesheet - Configuration Display | S_PL0_09000016 | S_PL0_09000016_TRAN | SIMG_ACT_CATSXC55A | Define Access Key for Transaction Control |  | CA-TS-S4 | CA-TS-S4 |
| SAP_CA_BC_IC_LND_CP_TS0_PC | Revenue Growth Management - Configuration | S_ERX_29000659 | S_ERX_29000659_TRAN | RGM_PROMO_PROXY_CONF | Define Spend Scenarios | 107171 | IS-RGM | IS-RGM-PP |
| SAP_CA_BC_IC_LND_CP_TS0_PC | Revenue Growth Management - Configuration | S_ERX_29000676 | S_ERX_29000676_TRAN | RGM_PROMNPOST2 | Configure General Settings | 107172 | IS-RGM | IS-RGM-PP |
| SAP_FS_BC_GLE_ECS_WORKFLOW_PC | Error Correction and Suspense Accounting - Workflow Configuration | F9593 | F9593_TRAN |  |  |  | FI-GL-GL-ADB |  |
| SAP_CA_BC_IC_LND_LO_NFE_BR_PC | Logistics NF-e for Brazil - Configuration | S_ER1_70001657 | NFECE_SWITCHES_TRAN | NFECE_SWITCHES | Maintain Electronic Fiscal Document Features | 107139 | FI-LOC-LO-BR-NFE | FI-LOC-NFE-BR-OUT |
| SAP_CA_BC_IC_LND_LO_NFE_BR_PC | Logistics NF-e for Brazil - Configuration | NFECE_SWITCHES |  | NFECE_SWITCHES | Maintain Electronic Fiscal Document Features | 107139 | FI-LOC-LO-BR-NFE | FI-LOC-NFE-BR-OUT |
| SAP_CA_BC_IC_LND_LOG_IN_VN_PC | Inventory for Vietnam - Configuration | S_EBJ_98000546 | S_EBJ_98000546_TRAN | V_J_3RM_TURNTYP | Define Turnover Types | 104250 | FI-LOC-FI-VN | FI-LOC-LO-RU |
| SAP_CA_BC_IC_LND_ML_DSP_PC | CO Content - Display AIM - Configuration | S_ER1_70001841 | S_ER1_70001841_TRAN | SIMG_CFG_CNTACT_CO | Configuration for CKMSTART and FCML4H Startup |  | CO-OM | FI-CNT-GL |
| SAP_CA_BC_IC_LND_ML_DSP_PC | CO Content - Display AIM - Configuration | CKM9 |  | SIMG_CFG_CNTACT_CO | Configuration for CKMSTART and FCML4H Startup |  | CO-OM | FI-CNT-GL |
| SAP_CA_BC_IC_LND_FIN_CJDSP_PC | Cash Journal - Configuration Display | S_ALR_87009226 | S_ALR_87009226_03_TRAN | FI_BL_CJ_T_FBCJC3 | Set Up Print Parameters for Cash Journal |  | FI-BL | FI-BL-PT-CJ-2CL |
| SAP_CA_BC_IC_LND_FIN_CJDSP_PC | Cash Journal - Configuration Display | FBCJC3 |  |  |  |  | FI-BL |  |
| SAP_CA_BC_IC_LND_FIN_CJDSP_PC | Cash Journal - Configuration Display | FBCJC1 |  |  |  |  | FI-BL |  |
| SAP_CA_BC_IC_LND_FIN_CJDSP_PC | Cash Journal - Configuration Display | S_P99_41000016 | S_P99_41000016_03_TRAN | FIBLCJ_T_FBCJC1 | Define Number Range Intervals for Cash Journal Documents |  | FI-BL | FI-BL-PT-CJ-2CL |
| SAP_CA_BC_IC_LND_CP_TS0_PC | Revenue Growth Management - Configuration | S_ERX_29000659 | S_ERX_29000659_TRAN | RGM_PROMO_PROXY_CONF | Define Spend Scenarios | 107171 | IS-RGM | IS-RGM-PP |
| SAP_CA_BC_IC_LND_CP_TS0_PC | Revenue Growth Management - Configuration | S_ERX_29000676 | S_ERX_29000676_TRAN | RGM_PROMNPOST2 | Configure General Settings | 107172 | IS-RGM | IS-RGM-PP |
| SAP_CA_BC_IC_LND_PP_MD_DSP_PC | Manufacturing Master Data - Configuration Display | S_ALR_87003785 | S_ALR_87003785_03_TRAN | SIMG_CFMENUOLPSOP04 | Define Line Length for Long Texts |  | PP-BD-RTG | PP-BD-RTG-2CL |
| SAP_CA_BC_IC_LND_PP_MD_DSP_PC | Manufacturing Master Data - Configuration Display | S_ALR_87003816 | S_ALR_87003816_03_TRAN | SIMG_CFMENUOLPSCANM | Define Number Ranges for Reference Rate Routings |  | PP-BD-RTG | PP-BD-RTG-2CL |
| SAP_CA_BC_IC_LND_PP_MD_DSP_PC | Manufacturing Master Data - Configuration Display | CANM |  | SIMG_CFMENUOLPSCANM | Define Number Ranges for Reference Rate Routings |  | PP-BD-RTG | PP-BD-RTG-2CL |
| SAP_CA_BC_IC_LND_PP_MD_DSP_PC | Manufacturing Master Data - Configuration Display | S_ALR_87003826 | S_ALR_87003826_03_TRAN | SIMG_CFMENUOLPSCANR | Define Number Ranges for Rate Routings |  | PP-BD-RTG | PP-BD-RTG-2CL |
| SAP_CA_BC_IC_LND_PP_MD_DSP_PC | Manufacturing Master Data - Configuration Display | CANR |  | SIMG_CFMENUOLPSCANR | Define Number Ranges for Rate Routings |  | PP-BD-RTG | PP-BD-RTG-2CL |
| SAP_CA_BC_IC_LND_PP_MD_DSP_PC | Manufacturing Master Data - Configuration Display | S_ALR_87003798 | S_ALR_87003798_03_TRAN | SIMG_CFMENUOLPSOP8A | Define Standard Value Descriptions in Operation Overviews |  | PP-BD-RTG | PP-BD-RTG-2CL |
| SAP_CA_BC_IC_LND_PP_MD_DSP_PC | Manufacturing Master Data - Configuration Display | S_ALR_87003839 | S_ALR_87003839_03_TRAN | SIMG_CFMENUOLPSOP46 | Define Routing Statuses |  | PP-BD-RTG | PP-BD-RTG-2CL |
| SAP_CA_BC_IC_LND_PP_MD_DSP_PC | Manufacturing Master Data - Configuration Display | OP46 |  | SIMG_CFMENUOLPSOP46 | Define Routing Statuses |  | PP-BD-RTG | PP-BD-RTG-2CL |
| SAP_CA_BC_IC_LND_PP_MD_DSP_PC | Manufacturing Master Data - Configuration Display | S_ALR_87003871 | S_ALR_87003871_03_TRAN | SIMG_CFMENUOLPSOPJS | Define Reduction Strategy |  | PP-BD-RTG | PP-BD-RTG-2CL |
| SAP_CA_BC_IC_LND_PP_MD_DSP_PC | Manufacturing Master Data - Configuration Display | S_ALR_87003849 | S_ALR_87003849_03_TRAN | SIMG_CFMENUOLPSOP71 | Define Wage Group |  | PP-BD-RTG | PP-BD-RTG-2CL |
| SAP_CA_BC_IC_LND_PP_MD_DSP_PC | Manufacturing Master Data - Configuration Display | OPJS |  | SIMG_CFMENUOLPSOPJS | Define Reduction Strategy |  | PP-BD-RTG | PP-BD-RTG-2CL |
| SAP_CA_BC_IC_LND_PP_MD_DSP_PC | Manufacturing Master Data - Configuration Display | S_ALR_87003933 | S_ALR_87003933_03_TRAN | SIMG_CFMENUOLPSOP63 | Define Number Ranges for Reference Operation Sets |  | PP-BD-RTG | PP-BD-RTG-2CL |
| SAP_CA_BC_IC_LND_PP_MD_DSP_PC | Manufacturing Master Data - Configuration Display | OP63 |  | SIMG_CFMENUOLPSOP63 | Define Number Ranges for Reference Operation Sets |  | PP-BD-RTG | PP-BD-RTG-2CL |
| SAP_CA_BC_IC_LND_PP_MD_DSP_PC | Manufacturing Master Data - Configuration Display | S_ALR_87003982 | S_ALR_87003982_03_TRAN | SIMG_CFMENUOLPSOP28 | Define key for performance efficiency rate |  | PP-BD-RTG | PP-BD-RTG-2CL |
| SAP_CA_BC_IC_LND_PP_MD_DSP_PC | Manufacturing Master Data - Configuration Display | OP28 |  | SIMG_CFMENUOLPSOP28 | Define key for performance efficiency rate |  | PP-BD-RTG | PP-BD-RTG-2CL |
| SAP_CA_BC_IC_LND_PP_MD_DSP_PC | Manufacturing Master Data - Configuration Display | S_ALR_87003991 | S_ALR_87003991_03_TRAN | SIMG_CFMENUOLPSOP37 | Define version of available capacity |  | PP-BD-RTG | PP-BD-RTG-2CL |
| SAP_CA_BC_IC_LND_PP_MD_DSP_PC | Manufacturing Master Data - Configuration Display | S_ALR_87004250 | S_ALR_87004250_03_TRAN | SIMG_CFMENUOLPSOPEA | Define User Selection |  | PP-BD-RTG | PP-BD-RTG-2CL |
| SAP_CA_BC_IC_LND_PP_MD_DSP_PC | Manufacturing Master Data - Configuration Display | S_ALR_87004265 | S_ALR_87004265_03_TRAN | SIMG_CFMENUOLPSOPL3 | Define (Standard) Trigger Point Usage |  | PP-BD-RTG | PP-BD-RTG-2CL |
| SAP_CA_BC_IC_LND_PP_MD_DSP_PC | Manufacturing Master Data - Configuration Display | S_ALR_87004304 | S_ALR_87004304_03_TRAN | SIMG_CFMENUOLPSOP78 | Define Type of Standard Value Determination |  | PP-BD-RTG | PP-BD-RTG-2CL |
| SAP_CA_BC_IC_LND_PP_MD_DSP_PC | Manufacturing Master Data - Configuration Display | S_ALR_87004314 | S_ALR_87004314_03_TRAN | SIMG_CFMENUOLPSOP76 | Define Suitability |  | PP-BD-RTG | PP-BD-RTG-2CL |
| SAP_CA_BC_IC_LND_PP_MD_DSP_PC | Manufacturing Master Data - Configuration Display | OPEB |  | SIMG_CFMENUOLPSOPEB | Select Automatically |  | PP-BD-RTG | PP-BD-RTG-2CL |
| SAP_CA_BC_IC_LND_PP_MD_DSP_PC | Manufacturing Master Data - Configuration Display | S_ALR_87004323 | S_ALR_87004323_03_TRAN | SIMG_CFMENUOLPSOPEB | Select Automatically |  | PP-BD-RTG | PP-BD-RTG-2CL |
| SAP_CA_BC_IC_LND_PP_MD_DSP_PC | Manufacturing Master Data - Configuration Display | S_ALR_87004333 | S_ALR_87004333_03_TRAN | SIMG_OLPS_NUM_GROBPL | Define number range for rough-cut planning profile |  | PP-BD-RTG | PP-BD-RTG-2CL |
| SAP_CA_BC_IC_LND_PP_MD_DSP_PC | Manufacturing Master Data - Configuration Display | OP61 |  | SIMG_OLPS_NUM_GROBPL | Define number range for rough-cut planning profile |  | PP-BD-RTG | PP-BD-RTG-2CL |
| SAP_CA_BC_IC_LND_PP_MD_DSP_PC | Manufacturing Master Data - Configuration Display | S_ALR_87004402 | S_ALR_87004402_03_TRAN | SIMG_CFMENUOLPSOS38 | Define Alternative Determination for MRP |  | PP-BD-RTG | PP-BD-RTG-2CL |
| SAP_CA_BC_IC_LND_PP_MD_DSP_PC | Manufacturing Master Data - Configuration Display | S_ALR_87004459 | S_ALR_87004459_03_TRAN | SIMG_CFMENUOLPSOVT6 | Define Relevancy to Sales |  | PP-BD-RTG | PP-BD-RTG-2CL |
| SAP_CA_BC_IC_LND_PP_MD_DSP_PC | Manufacturing Master Data - Configuration Display | S_ALR_87004450 | S_ALR_87004450_03_TRAN | SIMG_CFMENUOLPSOKK9 | Define Relevancy to Costing |  | PP-BD-RTG | PP-BD-RTG-2CL |
| SAP_CA_BC_IC_LND_PP_MD_DSP_PC | Manufacturing Master Data - Configuration Display | OS18 |  | SIMG_CFMENUOLPSOKK9 | Define Relevancy to Costing |  | PP-BD-RTG | PP-BD-RTG-2CL |
| SAP_CA_BC_IC_LND_PP_MD_DSP_PC | Manufacturing Master Data - Configuration Display | S_ALR_87004529 | S_ALR_87004529_03_TRAN | SIMG_CFMENUOLPSOS23 | Define BOM Status | 107378 | PP-BD-RTG | PP-BD-RTG-2CL |
| SAP_CA_BC_IC_LND_PP_MD_DSP_PC | Manufacturing Master Data - Configuration Display | OS23 |  | SIMG_CFMENUOLPSOS23 | Define BOM Status | 107378 | PP-BD-RTG | PP-BD-RTG-2CL |
| SAP_CA_BC_IC_LND_PP_MD_DSP_PC | Manufacturing Master Data - Configuration Display | S_ALR_87004553 | S_ALR_87004553_03_TRAN | SIMG_CFMENUOLPSOS27 | Define Modification Parameters |  | PP-BD-RTG | PP-BD-RTG-2CL |
| SAP_CA_BC_IC_LND_PP_MD_DSP_PC | Manufacturing Master Data - Configuration Display | OS27 |  | SIMG_CFMENUOLPSOS27 | Define Modification Parameters |  | PP-BD-RTG | PP-BD-RTG-2CL |
| SAP_CA_BC_IC_LND_PP_MD_DSP_PC | Manufacturing Master Data - Configuration Display | S_ALR_87004563 | S_ALR_87004563_03_TRAN | SIMG_CFMENUOLPSOS12 | Define Material Provision Indicators |  | PP-BD-RTG | PP-BD-RTG-2CL |
| SAP_CA_BC_IC_LND_PP_MD_DSP_PC | Manufacturing Master Data - Configuration Display | OS12 |  | SIMG_CFMENUOLPSOS12 | Define Material Provision Indicators |  | PP-BD-RTG | PP-BD-RTG-2CL |
| SAP_CA_BC_IC_LND_PP_MD_DSP_PC | Manufacturing Master Data - Configuration Display | S_ALR_87004567 | S_ALR_87004567_03_TRAN | SIMG_CFMENUOLPSOS11 | Define Spare Part Indicators |  | PP-BD-RTG | PP-BD-RTG-2CL |
| SAP_CA_BC_IC_LND_PP_MD_DSP_PC | Manufacturing Master Data - Configuration Display | S_ALR_87004590 | S_ALR_87004590_03_TRAN | SIMG_CFMENUOLPSOS25 | Configure History Requirement for BOMs | 107343 | PP-BD-RTG | PP-BD-RTG-2CL |
| SAP_CA_BC_IC_LND_PP_MD_DSP_PC | Manufacturing Master Data - Configuration Display | OS11 |  | SIMG_CFMENUOLPSOS11 | Define Spare Part Indicators |  | PP-BD-RTG | PP-BD-RTG-2CL |
| SAP_CA_BC_IC_LND_PP_MD_DSP_PC | Manufacturing Master Data - Configuration Display | OS25 |  | SIMG_CFMENUOLPSOS25 | Configure History Requirement for BOMs | 107343 | PP-BD-RTG | PP-BD-RTG-2CL |
| SAP_CA_BC_IC_LND_PP_MD_DSP_PC | Manufacturing Master Data - Configuration Display | S_ER9_52001901 | S_ER9_52001901_03_TRAN | SIMG_V_TCA09_A | IMG: PP Configuration |  | PP-BD-RTG | PP-BD-RTG-2CL |
| SAP_CA_BC_IC_LND_PP_MD_DSP_PC | Manufacturing Master Data - Configuration Display | SSCUI_PP_NR_TLT_S |  | SIMG_CFMENUOP8BTLTS | Assign Number Ranges to Task List Type Reference Operation Set |  | PP-BD-RTG | PP-BD-RTG-2CL |
| SAP_CA_BC_IC_LND_PP_MD_DSP_PC | Manufacturing Master Data - Configuration Display | S_ER9_52001317 | S_ER9_52001317_03_TRAN | SIMG_CFMENUOP8BTLT2 | Assign Number Ranges to Task List Type Master Recipe |  | PP-BD-RTG | PP-BD-RTG-2CL |
| SAP_CA_BC_IC_LND_PP_MD_DSP_PC | Manufacturing Master Data - Configuration Display | OP40 |  | SIMG_CFMENUOLPSOP40 | Define work center category |  | PP-BD-RTG | PP-BD-RTG-2CL |
| SAP_CA_BC_IC_LND_PP_MD_DSP_PC | Manufacturing Master Data - Configuration Display | S_ER9_52001318 | S_ER9_52001318_03_TRAN | SIMG_CFMENUOP8BTLTS | Assign Number Ranges to Task List Type Reference Operation Set |  | PP-BD-RTG | PP-BD-RTG-2CL |
| SAP_CA_BC_IC_LND_PP_MD_DSP_PC | Manufacturing Master Data - Configuration Display | SSCUI_PP_NR_TLT_2 |  | SIMG_CFMENUOP8BTLT2 | Assign Number Ranges to Task List Type Master Recipe |  | PP-BD-RTG | PP-BD-RTG-2CL |
| SAP_CA_BC_IC_LND_PP_MD_DSP_PC | Manufacturing Master Data - Configuration Display | S_ER9_52001729 | S_ER9_52001729_03_TRAN | SIMG_CFMENUOLPSOP43 | Define Work Center Group Type |  | PP-BD-RTG | PP-BD-RTG-2CL |
| SAP_CA_BC_IC_LND_PP_MD_DSP_PC | Manufacturing Master Data - Configuration Display | S_ER1_70000954 | S_ER1_70000954_03_TRAN | SIMG_DNRPVP | Define Number Ranges for Production Version Proposals |  | PP-BD-RTG | PP-PI-MD-PRV-2CL |
| SAP_CA_BC_IC_LND_PP_MD_DSP_PC | Manufacturing Master Data - Configuration Display | S_ALR_87004695 | S_ALR_87004695_03_TRAN | SIMG_CFMENUOLPSOP40 | Define work center category |  | PP-BD-RTG | PP-BD-RTG-2CL |
| SAP_CA_BC_IC_LND_PP_MD_DSP_PC | Manufacturing Master Data - Configuration Display | PPH_PPV |  | SIMG_DNRPVP | Define Number Ranges for Production Version Proposals |  | PP-BD-RTG | PP-PI-MD-PRV-2CL |
| SAP_CA_BC_IC_LND_SLL_DSP_PC | International Trade - Configuration Display | /ECRS/12000001 | ECRS_12000001_03_TRAN | /ECRS/GP_COUNTRY_DEF | Define Partner Countries |  | FT-ITR-TRC | FT-ITR-ISR |
| SAP_CA_BC_IC_LND_SLL_DSP_PC | International Trade - Configuration Display | /ECRS/12000007 | ECRS_12000007_03_TRAN | /ECRS/PROCEDURE_DEF | Define Procedures |  | FT-ITR-TRC | FT-ITR-ISR |
| SAP_CA_BC_IC_LND_SLL_DSP_PC | International Trade - Configuration Display | /ECRS/12000010 | ECRS_12000010_03_TRAN | /ECRS/PORT_AIRPO_DEF | Define Ports and Airports |  | FT-ITR-TRC | FT-ITR-ISR |
| SAP_CA_BC_IC_LND_SLL_DSP_PC | International Trade - Configuration Display | /ECRS/12000003 | ECRS_12000003_03_TRAN | /ECRS/CNTRY_ORIG_DEF | Define Countries of Origin |  | FT-ITR-TRC | FT-ITR-ISR |
| SAP_CA_BC_IC_LND_SLL_DSP_PC | International Trade - Configuration Display | /ECRS/12000011 | ECRS_12000011_03_TRAN | /ECRS/SPECMOVEMT_DEF | Define Movement Codes |  | FT-ITR-TRC | FT-ITR-ISR |
| SAP_CA_BC_IC_LND_SLL_DSP_PC | International Trade - Configuration Display | /ECRS/12000012 | ECRS_12000012_03_TRAN | /ECRS/OFFICE_DEFINE | Define Collection Centers |  | FT-ITR-TRC | FT-ITR-ISR |
| SAP_CA_BC_IC_LND_SLL_DSP_PC | International Trade - Configuration Display | /SAPSLL/52000653 | SAPSLL_52000653_03_TRAN | /SAPSLL/PARTNERMAPPI | Mapping of Partner Functions to Partner Roles |  | FT-ITR-TRC | FT-ITR-TRC |
| SAP_CA_BC_IC_LND_SLL_DSP_PC | International Trade - Configuration Display | /SAPSLL/52000643 | SAPSLL_52000643_03_TRAN | /SAPSLL/PARTNERROLES | Define Partner Roles |  | FT-ITR-TRC | FT-ITR-TRC |
| SAP_CA_BC_IC_LND_SLL_DSP_PC | International Trade - Configuration Display | /SAPSLL/52000702 | SAPSLL_52000702_03_TRAN | /SAPSLL/NRLICENTYPE | Define Number Ranges for Licenses |  | FT-ITR-TRC | FT-ITR-TRC |
| SAP_CA_BC_IC_LND_SLL_DSP_PC | International Trade - Configuration Display | /SAPSLL/SNUM_LICNO |  | /SAPSLL/NRLICENTYPE | Define Number Ranges for Licenses |  | FT-ITR-TRC | FT-ITR-TRC |
| SAP_CA_BC_IC_LND_SLL_DSP_PC | International Trade - Configuration Display | /SAPSLL/52002149 | SAPSLL_52002149_03_TRAN | /SAPSLL/DEF_STCCS_03 | Define Numbering Scheme Content for Intrastat Service Codes |  | FT-ITR-TRC | FT-ITR-TRC |
| SAP_CA_BC_IC_LND_SLL_DSP_PC | International Trade - Configuration Display | /SAPSLL/52000668 | SAPSLL_52000668_03_TRAN | /SAPSLL/ASNOSCHEMISC | Assign Numbering Scheme for Intrastat Service Codes to Country/Region |  | FT-ITR-TRC | FT-ITR-TRC |
| SAP_CA_BC_IC_LND_SLL_DSP_PC | International Trade - Configuration Display | /SAPSLL/52002150 | SAPSLL_52002150_03_TRAN | /SAPSLL/DEF_STCTS_03 | Define Numbering Scheme for Intrastat Service Codes |  | FT-ITR-TRC | FT-ITR-TRC |
| SAP_CA_BC_IC_LND_SLL_DSP_PC | International Trade - Configuration Display | /SAPSLL/52002181 | SAPSLL_52002181_03_TRAN | /SAPSLL/ACT_STCCS_03 | Activate Numbering Scheme Content for Intrastat Service Codes |  | FT-ITR-TRC | FT-ITR-TRC |
| SAP_CA_BC_IC_LND_FIN_WT_DE_PC | Statutory Reporting WT for Germany - Configuration | S_ER1_70001606 | S_ER1_70001606_TRAN | V_J_1_T059WTK_DE | Define Threshold and Rate for 50A | 107259 | FI-LOC-IAM | FI-AP-AP-Q1 |
| SAP_CA_BC_IC_LND_FCLM_DSP_PC | Cash Management - Configuration Display | S_E91_86000029 | S_E91_86000029_TRAN | FCLM_BAM_ACCTNR | Define Number Ranges for Bank Account Technical IDs |  | FIN-FSCM-CLM | FIN-FSCM-CLM-BAM-2CL |
| SAP_CA_BC_IC_LND_FCLM_DSP_PC | Cash Management - Configuration Display | FCLM_BAM_ACCNR |  | FCLM_BAM_ACCTNR | Define Number Ranges for Bank Account Technical IDs |  | FIN-FSCM-CLM | FIN-FSCM-CLM-BAM-2CL |
| SAP_CA_BC_IC_LND_FCLM_DSP_PC | Cash Management - Configuration Display | S_ER1_70000876 | S_ER1_70000876_TRAN | FCLM_IB | Define Number Ranges for Instant Balance Responses |  | FIN-FSCM-CLM | FIN-FSCM-CLM-BAM-2CL |
| SAP_CA_BC_IC_LND_FCLM_DSP_PC | Cash Management - Configuration Display | FCLM_BAM_IBNR |  | FCLM_IB | Define Number Ranges for Instant Balance Responses |  | FIN-FSCM-CLM | FIN-FSCM-CLM-BAM-2CL |
| SAP_CA_BC_IC_LND_FCLM_DSP_PC | Cash Management - Configuration Display | S_ALR_87007283 | S_ALR_87007283_TRAN | SIMG_CFMENUOFTDOT22 | Maintain Archive Retention Period |  | FIN-FSCM-CLM | FIN-FSCM-CLM-2CL |
| SAP_CA_BC_IC_LND_FCLM_DSP_PC | Cash Management - Configuration Display | S_ER1_70000885 | S_ER1_70000885_TRAN | FCLM_IBREQ | Define Number Ranges for Instant Balance Requests |  | FIN-FSCM-CLM | FIN-FSCM-CLM-BAM-2CL |
| SAP_CA_BC_IC_LND_FCLM_DSP_PC | Cash Management - Configuration Display | FCLM_BAM_IBREQNR |  | FCLM_IBREQ | Define Number Ranges for Instant Balance Requests |  | FIN-FSCM-CLM | FIN-FSCM-CLM-BAM-2CL |
| SAP_CA_BC_IC_LND_FCLM_DSP_PC | Cash Management - Configuration Display | S_ER9_11000372 | S_ER9_11000372_TRAN | FCLM_BAM_CONFIG | Assign Number Ranges |  | FIN-FSCM-CLM | FIN-FSCM-CLM-BAM-2CL |
| SAP_CA_BC_IC_LND_FCLM_DSP_PC | Cash Management - Configuration Display | S_ALR_87007417 | S_ALR_87007417_TRAN | SIMG_CFMENUOFTDOT05 | Define Source Symbols |  | FIN-FSCM-CLM | FIN-FSCM-CLM-FQM-2CL |
| SAP_CA_BC_IC_LND_FCLM_DSP_PC | Cash Management - Configuration Display | S_E91_86000085 | S_E91_86000085_TRAN | FQMV_FLOW_TYPE | Define Flow Types |  | FIN-FSCM-CLM | FIN-FSCM-CLM-FQM-2CL |
| SAP_CA_BC_IC_LND_FCLM_DSP_PC | Cash Management - Configuration Display | S_E91_86000030 | S_E91_86000030_TRAN | FCLM_BAM_REQNR | Define Number Ranges for Change Requests |  | FIN-FSCM-CLM | FIN-FSCM-CLM-BAM-2CL |
| SAP_CA_BC_IC_LND_FCLM_DSP_PC | Cash Management - Configuration Display | FCLM_BAM_REQNR |  | FCLM_BAM_REQNR | Define Number Ranges for Change Requests |  | FIN-FSCM-CLM | FIN-FSCM-CLM-BAM-2CL |
| SAP_CA_BC_IC_LND_FCLM_DSP_PC | Cash Management - Configuration Display | S_E91_86000141 | S_E91_86000141_TRAN | FQMV_FLOWT_FDLEV | Assign Planning Levels to Flow Types |  | FIN-FSCM-CLM | FIN-FSCM-CLM-2CL |
| SAP_CA_BC_IC_LND_CMP_PC | Consolidation and Mass Processing - Configuration | S_ER1_70000969 | S_ER1_70000969_TRAN | MDC_CFG_MTC_2 | Configure Matching and Duplicate Check | 100274 | CA-MDG-CMP | CA-MDG-CMP-AF |
| SAP_CA_BC_IC_LND_CMP_PC | Consolidation and Mass Processing - Configuration | MDC_CFG_MTC_2 |  | MDC_CFG_MTC_2 | Configure Matching and Duplicate Check | 100274 | CA-MDG-CMP | CA-MDG-CMP-AF |
| SAP_CA_BC_IC_LND_CMP_PC | Consolidation and Mass Processing - Configuration | F2415 | F2415_TRAN |  |  |  | CA-MDG-CMP |  |
| SAP_CA_BC_IC_LND_CMP_PC | Consolidation and Mass Processing - Configuration | F2415 | F2415_TRAN |  |  |  | CA-MDG-CMP |  |
| SAP_CA_BC_IC_LND_RFM_OPPS_PC | Omnichannel - Sales Promotions Configuration | S_ER1_70001729 | S_ER1_70001729_TRAN | RTL_OPPS_ACTVT | Activate Omnichannel Sales Promotions for Sales Orders | 107198 | LO-RFM | LO-RFM-OPP-2CL |
| SAP_CA_BC_IC_LND_RFM_OPPS_PC | Omnichannel - Sales Promotions Configuration | RTL_OPPS_ACTVT |  | RTL_OPPS_ACTVT | Activate Omnichannel Sales Promotions for Sales Orders | 107198 | LO-RFM | LO-RFM-OPP-2CL |
| SAP_CA_BC_IC_LND_RFM_OPPS_PC | Omnichannel - Sales Promotions Configuration | S_ER9_52002782 | S_ER9_52002782_TRAN | V_SDOPS_ATRASG_C | Assign Generic Attributes to Distribution Chain | 107361 | LO-RFM | LO-RFM-OPP-2CL |
| SAP_CA_BC_IC_LND_RFM_OPPS_PC | Omnichannel - Sales Promotions Configuration | S_ER9_52002711 | S_ER9_52002711_TRAN | SDBOBRELEVANCE | Maintain Relevance for Omnichannel Sales Promotions | 107197 | LO-RFM | LO-RFM-OPP-2CL |
| SAP_CA_BC_IC_LND_RFM_OPPS_PC | Omnichannel - Sales Promotions Configuration | S_ER9_52002781 | S_ER9_52002781_TRAN | V_SDOPS_ATTR_C | Define Fields Used for Generic Attributes | 107360 | LO-RFM | LO-RFM-OPP-2CL |
| SAP_CA_BC_IC_LND_RFM_OPPS_PC | Omnichannel - Sales Promotions Configuration | S_ER9_52002747 | S_ER9_52002747_TRAN | V_OPPS_CND_PRPS | Assign Discount Types to Condition Purposes | 107179 | LO-RFM | LO-RFM-OPP-2CL |
| SAP_CA_BC_IC_LND_RFM_OPPS_PC | Omnichannel - Sales Promotions Configuration | SDBOBRELEVANCE |  | SDBOBRELEVANCE | Maintain Relevance for Omnichannel Sales Promotions | 107197 | LO-RFM | LO-RFM-OPP-2CL |
| SAP_CA_BC_IC_LND_RFM_OPPS_PC | Omnichannel - Sales Promotions Configuration | S_ER9_52002694 | S_ER9_52002694_TRAN | V_CNDN_PRPS_ASSG | Assign Condition Purposes to Condition Types | 107178 | LO-RFM | LO-RFM-OPP-2CL |
| SAP_CA_BC_IC_LND_RFM_OPPS_PC | Omnichannel - Sales Promotions Configuration | S_ER9_52002693 | S_ER9_52002693_TRAN | V_CNDN_PRPS_C | Define Condition Purposes | 107177 | LO-RFM | LO-RFM-OPP-2CL |
| SAP_CA_BC_IC_LND_EHS_OH0_PC | EHS Occupational Health Management - Configuration | EHOHM_PROT_OWNER |  | EHOHM_PROT_OWNR | Define Health Protocol Owners | 107237 | EHS-SUS-FND-EHS | EHS-SUS-OH |
| SAP_CA_BC_IC_LND_EHS_OH0_PC | EHS Occupational Health Management - Configuration | EHOHM_PROT_TYPE |  | EHOHM_PROT_TYPE | Define Health Protocol Types | 107236 | EHS-SUS-FND-EHS | EHS-SUS-OH |
| SAP_CA_BC_IC_LND_EHS_OH0_PC | EHS Occupational Health Management - Configuration | S_ER1_70001740 | S_ER1_70001740_TRAN | EHOHM_PROT_CAT | Define Health Protocol Categories | 107235 | EHS-SUS-FND-EHS | EHS-SUS-OH |
| SAP_CA_BC_IC_LND_EHS_OH0_PC | EHS Occupational Health Management - Configuration | S_ER1_70001730 | S_ER1_70001730_TRAN | EHOHM_SRV_ITEM | Define Health Service Items | 107233 | EHS-SUS-FND-EHS | EHS-SUS-OH |
| SAP_CA_BC_IC_LND_EHS_OH0_PC | EHS Occupational Health Management - Configuration | EHOHM_PROT_CAT |  | EHOHM_PROT_CAT | Define Health Protocol Categories | 107235 | EHS-SUS-FND-EHS | EHS-SUS-OH |
| SAP_CA_BC_IC_LND_EHS_OH0_PC | EHS Occupational Health Management - Configuration | S_ER1_70001739 | S_ER1_70001739_TRAN | EHOHM_PROT_OWNR | Define Health Protocol Owners | 107237 | EHS-SUS-FND-EHS | EHS-SUS-OH |
| SAP_CA_BC_IC_LND_EHS_OH0_PC | EHS Occupational Health Management - Configuration | S_ER1_70001778 | S_ER1_70001778_TRAN | EHOHM_PROT_TYPE | Define Health Protocol Types | 107236 | EHS-SUS-FND-EHS | EHS-SUS-OH |
| SAP_CA_BC_IC_LND_EHS_OH0_PC | EHS Occupational Health Management - Configuration | EHOHM_SRV_ITEM |  | EHOHM_SRV_ITEM | Define Health Service Items | 107233 | EHS-SUS-FND-EHS | EHS-SUS-OH |
| SAP_CA_BC_IC_LND_EHS_OH0_PC | EHS Occupational Health Management - Configuration | S_ER1_70001735 | S_ER1_70001735_TRAN | EHOHM_SRV_TYPE | Define Health Service Types | 107232 | EHS-SUS-FND-EHS | EHS-SUS-OH |
| SAP_CA_BC_IC_LND_EHS_OH0_PC | EHS Occupational Health Management - Configuration | EHOHM_SRV_TYPE |  | EHOHM_SRV_TYPE | Define Health Service Types | 107232 | EHS-SUS-FND-EHS | EHS-SUS-OH |
| SAP_CA_BC_IC_LND_EHS_OH0_PC | EHS Occupational Health Management - Configuration | EHFND_LOC_OHROL |  | EHFND_LOC_OHROL | Define Location Roles | 107262 | EHS-SUS-FND-EHS | EHS-SUS-FND-EHS |
| SAP_CA_BC_IC_LND_EHS_OH0_PC | EHS Occupational Health Management - Configuration | S_ER1_70001816 | S_ER1_70001816_TRAN | EHFND_LOC_OHROL | Define Location Roles | 107262 | EHS-SUS-FND-EHS | EHS-SUS-FND-EHS |
| SAP_CA_BC_IC_LND_EHS_OH0_PC | EHS Occupational Health Management - Configuration | EHOHM_NR_PROTID |  | EHOHM_NR_PROTID | Maintain Number Range for Health Protocol Identifier | 107340 | EHS-SUS-FND-EHS | EHS-SUS-OH |
| SAP_CA_BC_IC_LND_EHS_OH0_PC | EHS Occupational Health Management - Configuration | S_ER1_70001876 | S_ER1_70001876_TRAN | EHOHM_NR_PROTID | Maintain Number Range for Health Protocol Identifier | 107340 | EHS-SUS-FND-EHS | EHS-SUS-OH |
| SAP_CA_BC_IC_LND_EHS_OH0_PC | EHS Occupational Health Management - Configuration | EHOHM_HLOC_TYPE |  | EHOHM_HLOC_TYPE | Define Health-Related Location Types | 107163 | EHS-SUS-FND-EHS | EHS-SUS-OH |
| SAP_CA_BC_IC_LND_EHS_OH0_PC | EHS Occupational Health Management - Configuration | EHOHM_NR_SRID |  | EHOHM_NR_SRID | Maintain Number Range for Health Service Request Identifier | 107369 | EHS-SUS-FND-EHS | EHS-SUS-OH |
| SAP_CA_BC_IC_LND_EHS_OH0_PC | EHS Occupational Health Management - Configuration | S_ER1_70001912 | S_ER1_70001912_TRAN | EHFND_NR_PHCID | Maintain Number Range for Personal Health Card Identifier | 107379 | EHS-SUS-FND-EHS | EHS-SUS-FND-EHS |
| SAP_CA_BC_IC_LND_EHS_OH0_PC | EHS Occupational Health Management - Configuration | S_ER1_70001893 | S_ER1_70001893_TRAN | EHOHM_NR_SRID | Maintain Number Range for Health Service Request Identifier | 107369 | EHS-SUS-FND-EHS | EHS-SUS-OH |
| SAP_CA_BC_IC_LND_EHS_OH0_PC | EHS Occupational Health Management - Configuration | EHFND_NR_PHCID |  | EHFND_NR_PHCID | Maintain Number Range for Personal Health Card Identifier | 107379 | EHS-SUS-FND-EHS | EHS-SUS-FND-EHS |
| SAP_CA_BC_IC_LND_EHS_OH0_PC | EHS Occupational Health Management - Configuration | EHOHM_NR_SIRID |  | EHOHM_NR_SIRID | Maintain Number Range for Health Service Item Result Identifier | 107380 | EHS-SUS-FND-EHS | EHS-SUS-OH |
| SAP_CA_BC_IC_LND_EHS_OH0_PC | EHS Occupational Health Management - Configuration | S_ER1_70001910 | S_ER1_70001910_TRAN | EHOHM_NR_SIRID | Maintain Number Range for Health Service Item Result Identifier | 107380 | EHS-SUS-FND-EHS | EHS-SUS-OH |
| SAP_CA_BC_IC_LND_EHS_OH0_PC | EHS Occupational Health Management - Configuration | EHOHM_NR_SRRID |  | EHOHM_NR_SRRID | Maintain Number Range for Health Service Request Result Identifier | 107401 | EHS-SUS-FND-EHS | EHS-SUS-OH |
| SAP_CA_BC_IC_LND_EHS_OH0_PC | EHS Occupational Health Management - Configuration | S_ER1_70001937 | S_ER1_70001937_TRAN | EHOHM_NR_SRRID | Maintain Number Range for Health Service Request Result Identifier | 107401 | EHS-SUS-FND-EHS | EHS-SUS-OH |
| SAP_CA_BC_IC_LND_EHS_OH0_PC | EHS Occupational Health Management - Configuration | S_ER1_70001679 | S_ER1_70001679_TRAN | EHOHM_HLOC_TYPE | Define Health-Related Location Types | 107163 | EHS-SUS-FND-EHS | EHS-SUS-OH |
| SAP_CA_BC_IC_LND_AA_DSP_PC | Asset Accounting - Configuration Display | S_ER9_11001057 | S_ER9_11001057_03_TRAN | V_FAA_ACLS0 | Specify Asset Class (Auxiliary Activity) |  | FI-AA | FI-AA-AA-2CL |
| SAP_CA_BC_IC_LND_AA_DSP_PC | Asset Accounting - Configuration Display | S_ER9_11001627 | S_ER9_11001627_03_TRAN | FAA_SNUM_UO | UoP Depreciation: Define Number Ranges for Usage Object |  | FI-AA | FI-AA-AA-2CL |
| SAP_CA_BC_IC_LND_AA_DSP_PC | Asset Accounting - Configuration Display | FAA_SNUM_UO |  | FAA_SNUM_UO | UoP Depreciation: Define Number Ranges for Usage Object |  | FI-AA | FI-AA-AA-2CL |
| SAP_CA_BC_IC_LND_AA_DSP_PC | Asset Accounting - Configuration Display | S_ER9_56000033 | S_ER9_56000033_03_TRAN | FAA_VALVIEW | Define Valuation View |  | FI-AA | FI-AA-AA-2CL |
| SAP_CA_BC_IC_LND_AA_DSP_PC | Asset Accounting - Configuration Display | S_ER9_11001413 | S_ER9_11001413_03_TRAN | FAA_LAYOUT | Define Layout for Asset Master Record |  | FI-AA | FI-AA-AA-2CL |
| SAP_CA_BC_IC_LND_AA_DSP_PC | Asset Accounting - Configuration Display | S_ER9_56000034 | S_ER9_56000034_03_TRAN | FAA_AP_VALV | Assign Valuation Views to Accounting Principle |  | FI-AA | FI-AA-AA-2CL |
| SAP_CA_BC_IC_LND_AA_DSP_PC | Asset Accounting - Configuration Display | S_ER9_56000035 | S_ER9_56000035_03_TRAN | FAA_AP_CHART | Make Cross-Company Code FI-AA Settings per Accounting Principle |  | FI-AA | FI-AA-AA-2CL |
| SAP_CA_BC_IC_LND_AA_DSP_PC | Asset Accounting - Configuration Display | S_ER9_56000042 | S_ER9_56000042_03_TRAN | FAA_ACLS_CMP | Make Company Code-Dependent Settings for Asset Class |  | FI-AA | FI-AA-AA-2CL |
| SAP_CA_BC_IC_LND_AA_DSP_PC | Asset Accounting - Configuration Display | S_ER9_56000043 | S_ER9_56000043_03_TRAN | FAA_ACCTASN | Activate Account Assignment Objects |  | FI-AA | FI-AA-AA-2CL |
| SAP_CA_BC_IC_LND_AA_DSP_PC | Asset Accounting - Configuration Display | S_ER9_56000046 | S_ER9_56000046_03_TRAN | FAA_ACCTASN_A | Define Account Assignment Rules per Accounting Principle |  | FI-AA | FI-AA-AA-2CL |
| SAP_CA_BC_IC_LND_AA_DSP_PC | Asset Accounting - Configuration Display | S_ER9_56000050 | S_ER9_56000050_03_TRAN | FAA_CMP0 | Make FI-AA-Specific Settings per Company Code |  | FI-AA | FI-AA-AA-2CL |
| SAP_CA_BC_IC_LND_AA_DSP_PC | Asset Accounting - Configuration Display | S_ER9_11000520 | S_ER9_11000520_03_TRAN | VC_FAAC_KEY_FIGURES | Display Key Figures for Asset Accounting (Fiori) |  | FI-AA | FI-AA-AA-2CL |
| SAP_CA_BC_IC_LND_AA_DSP_PC | Asset Accounting - Configuration Display | S_ER9_11000298 | S_ER9_11000298_03_TRAN | VC_FAAC_KFCSET_ABS | Define Key Figure Groups for Asset Balances (Fiori) |  | FI-AA | FI-AA-AA-2CL |
| SAP_CA_BC_IC_LND_AA_DSP_PC | Asset Accounting - Configuration Display | FAA_KFC |  | VC_FAAC_KEY_FIGURES | Display Key Figures for Asset Accounting (Fiori) |  | FI-AA | FI-AA-AA-2CL |
| SAP_CA_BC_IC_LND_AA_DSP_PC | Asset Accounting - Configuration Display | S_ER9_11000501 | S_ER9_11000501_03_TRAN | VC_FAAC_KFCSET_TRANS | Define Key Figure Groups for Asset Transactions (Fiori) |  | FI-AA | FI-AA-AA-2CL |
| SAP_CA_BC_IC_LND_AA_DSP_PC | Asset Accounting - Configuration Display | S_ER9_11000300 | S_ER9_11000300_03_TRAN | VC_FAAC_KFCSET_AHS | Define Key Figure Groups for Asset History Sheet (Fiori) |  | FI-AA | FI-AA-AA-2CL |
| SAP_CA_BC_IC_LND_PM_FSM_PC | Plant Maintenance - SAP FSM - Direct Integration(P2P) - Configuration | S_ERX_29000646 | S_ERX_29000646_TRAN | EAM_FSM_EXP_TY | Configure Mapping for Expense Type | 107208 | PM-INT-FSM | PM-INT-FSM-2CL |
| SAP_CA_BC_IC_LND_PM_FSM_PC | Plant Maintenance - SAP FSM - Direct Integration(P2P) - Configuration | S_ERX_29000418 | S_ERX_29000418_TRAN | EAM_FSM_BP_DEF | Set Default Business Partner (Customer) | 107214 | PM-INT-FSM | PM-INT-FSM-2CL |
| SAP_CA_BC_IC_LND_PM_FSM_PC | Plant Maintenance - SAP FSM - Direct Integration(P2P) - Configuration | S_ERX_29000647 | S_ERX_29000647_TRAN | EAM_FSM_EXP_ITM | Configure Mapping for Expense Type Item | 107209 | PM-INT-FSM | PM-INT-FSM-2CL |
| SAP_CA_BC_IC_LND_PM_FSM_PC | Plant Maintenance - SAP FSM - Direct Integration(P2P) - Configuration | S_ERX_29000415 | S_ERX_29000415_TRAN | EAM_FSM_REG_SRC | Configure Region | 107212 | PM-INT-FSM | PM-INT-FSM-2CL |
| SAP_CA_BC_IC_LND_PM_FSM_PC | Plant Maintenance - SAP FSM - Direct Integration(P2P) - Configuration | S_ERX_29000414 | S_ERX_29000414_TRAN | EAM_FSM_PROB_TY | Configure Mapping for Problem Type Codelist | 107211 | PM-INT-FSM | PM-INT-FSM-2CL |
| SAP_CA_BC_IC_LND_PM_FSM_PC | Plant Maintenance - SAP FSM - Direct Integration(P2P) - Configuration | S_ERX_29000413 | S_ERX_29000413_TRAN | EAM_FSM_PRIO | Configure Mapping for Priority Codelist | 107210 | PM-INT-FSM | PM-INT-FSM-2CL |
| SAP_CA_BC_IC_LND_PM_FSM_PC | Plant Maintenance - SAP FSM - Direct Integration(P2P) - Configuration | S_ERX_29000411 | S_ERX_29000411_TRAN | EAM_FSM_SRV_TY | Configure Mapping for Service Call Type Codelist | 107213 | PM-INT-FSM | PM-INT-FSM-2CL |
| SAP_CA_BC_IC_LND_PM_FSM_PC | Plant Maintenance - SAP FSM - Direct Integration(P2P) - Configuration | S_ERX_29000410 | S_ERX_29000410_TRAN | EAM_FSM_FLT_RPL | Define System Status to filter Maintenance Order replication | 107206 | PM-INT-FSM | PM-INT-FSM-2CL |
| SAP_CA_BC_IC_LND_PM_FSM_PC | Plant Maintenance - SAP FSM - Direct Integration(P2P) - Configuration | S_ERX_29000409 | S_ERX_29000409_TRAN | EAM_FSM_FLT_ORD | Define Plant Specific Order Types | 107205 | PM-INT-FSM | PM-INT-FSM-2CL |
| SAP_CA_BC_IC_LND_PM_FSM_PC | Plant Maintenance - SAP FSM - Direct Integration(P2P) - Configuration | S_ER1_70001788 | S_ER1_70001788_TRAN | EAM_FSM_PHASE | Configure Mapping for Phase Codelist | 107247 | PM-INT-FSM | PM-INT-FSM-2CL |
| SAP_CA_BC_IC_LND_FIN_AP1_PC | Accounts Payable - CLT Countries with Taulia Configuration | S_ER1_70001926 | S_ER1_70001926_TRAN | V_TINT_CLT_SCP | Activate Dynamic Discount for CLT | 107342 | FI-LOC-IAM | FI-LOC-TI |
| SAP_CA_BC_IC_LND_FIN_AP1_PC | Accounts Payable - CLT Countries with Taulia Configuration | TINT_CLTSCP |  | V_TINT_CLT_SCP | Activate Dynamic Discount for CLT | 107342 | FI-LOC-IAM | FI-LOC-TI |
| SAP_CA_BC_IC_LND_RFM_DSP_PC | Retail and Fashion Management - Configuration Display | S_ALR_87005968 | S_ALR_87005968_03_TRAN | W_OE_EG_WL_0101 | Distribution Chain Control | 105705 | LO-RFM | LO-RFM-CA-2CL |
| SAP_CA_BC_IC_LND_RFM_DSP_PC | Retail and Fashion Management - Configuration Display | S_ALR_87001921 | S_ALR_87001921_03_TRAN | W_ZF_VK_0108 | Assign Follow-Up Actions to Error Messages |  | LO-RFM | LO-RFM-MD-LST-2CL |
| SAP_CA_BC_IC_LND_RFM_DSP_PC | Retail and Fashion Management - Configuration Display | S_ALR_87005445 | S_ALR_87005445_03_TRAN | W_MDS_0001 | Distribution Profile of Material in DC |  | LO-RFM | LO-RFM-MDS-2CL |
| SAP_CA_BC_IC_LND_RFM_DSP_PC | Retail and Fashion Management - Configuration Display | S_ALR_87001912 | S_ALR_87001912_03_TRAN | W_ZF_VK_0107 | Define Follow-Up Actions |  | LO-RFM | LO-RFM-MD-LST-2CL |
| SAP_CA_BC_IC_LND_RFM_DSP_PC | Retail and Fashion Management - Configuration Display | S_ALR_87005449 | S_ALR_87005449_03_TRAN | W_MDS_0002 | Adjustment Profiles per Processing Method |  | LO-RFM | LO-RFM-MDS-2CL |
| SAP_CA_BC_IC_LND_RFM_DSP_PC | Retail and Fashion Management - Configuration Display | S_ALR_87005452 | S_ALR_87005452_03_TRAN | W_MDS_0000 | Plant Profiles for Merchandise Distribution |  | LO-RFM | LO-RFM-MDS-2CL |
| SAP_CA_BC_IC_LND_RFM_DSP_PC | Retail and Fashion Management - Configuration Display | S_ALR_87008671 | S_ALR_87008671_03_TRAN | W_ZF_VK_0410 | Allocation Table Types |  | LO-RFM | LO-RFM-PUR-AL-2CL |
| SAP_CA_BC_IC_LND_RFM_DSP_PC | Retail and Fashion Management - Configuration Display | S_ALR_87008670 | S_ALR_87008670_03_TRAN | W_ZF_VK_0620 | Allocation Strategies |  | LO-RFM | LO-RFM-PUR-AL-2CL |
| SAP_CA_BC_IC_LND_RFM_DSP_PC | Retail and Fashion Management - Configuration Display | S_ALR_87008672 | S_ALR_87008672_03_TRAN | W_ZF_VK_0630 | Reasons for Rejection |  | LO-RFM | LO-RFM-PUR-AL-2CL |
| SAP_CA_BC_IC_LND_RFM_DSP_PC | Retail and Fashion Management - Configuration Display | V_RFM_SC_PICKSEQ |  | STORE_PICKSEQ_SCHEMA | Define Schema for Store Picking Sequence |  | LO-RFM | LO-RFM-STO-FIO-2CL |
| SAP_CA_BC_IC_LND_RFM_DSP_PC | Retail and Fashion Management - Configuration Display | S_ER9_52002184 | S_ER9_52002184_03_TRAN | STORE_PICKSEQ_SCHEMA | Define Schema for Store Picking Sequence |  | LO-RFM | LO-RFM-STO-FIO-2CL |
| SAP_CA_BC_IC_LND_RFM_DSP_PC | Retail and Fashion Management - Configuration Display | V_RTST_OP_BASICS |  | V_RTST_OP_BASICS | Define Basic Settings for Order Products |  | LO-RFM | LO-RFM-STO-FIO-2CL |
| SAP_CA_BC_IC_LND_RFM_DSP_PC | Retail and Fashion Management - Configuration Display | S_ER9_52003838 | S_ER9_52003838_03_TRAN | V_RFM_RP_CUSTORD | Define Settings for Purchase-to-Order Process |  | LO-RFM | LO-RFM-STO-FIO-2CL |
| SAP_CA_BC_IC_LND_RFM_DSP_PC | Retail and Fashion Management - Configuration Display | S_ESI_48000190 | S_ESI_48000190_03_TRAN | V_RTST_OP_BASICS | Define Basic Settings for Order Products |  | LO-RFM | LO-RFM-STO-FIO-2CL |
| SAP_CA_BC_IC_LND_RFM_DSP_PC | Retail and Fashion Management - Configuration Display | V_RFM_RP_CUSTORD |  | V_RFM_RP_CUSTORD | Define Settings for Purchase-to-Order Process |  | LO-RFM | LO-RFM-STO-FIO-2CL |
| SAP_CA_BC_IC_LND_RFM_DSP_PC | Retail and Fashion Management - Configuration Display | V_TBSG |  | V_RTST_TP_TRANSF_RSN | Define Transfer Reasons |  | LO-RFM | LO-RFM-STO-FIO-2CL |
| SAP_CA_BC_IC_LND_RFM_DSP_PC | Retail and Fashion Management - Configuration Display | S_ESI_48000213 | S_ESI_48000213_03_TRAN | V_RTST_TP_TRANSF_RSN | Define Transfer Reasons |  | LO-RFM | LO-RFM-STO-FIO-2CL |
| SAP_CA_BC_IC_LND_RFM_DSP_PC | Retail and Fashion Management - Configuration Display | S_XB4_60000080 | S_XB4_60000080_03_TRAN | WRF_AT_CONS_0001 | Enhancements for Item Categories of Allocation Table |  | LO-RFM | LO-RFM-PUR-AL-2CL |
| SAP_CA_BC_IC_LND_RFM_DSP_PC | Retail and Fashion Management - Configuration Display | S_XB4_60000083 | S_XB4_60000083_03_TRAN | WRF_AT_0001 | General Settings for Allocation Table Application |  | LO-RFM | LO-RFM-PUR-AL-2CL |
| SAP_CA_BC_IC_LND_RFM_DSP_PC | Retail and Fashion Management - Configuration Display | S_XB4_60000084 | S_XB4_60000084_03_TRAN | WRF_AT_0002 | Enhancements for Allocation Table Strategy |  | LO-RFM | LO-RFM-PUR-AL-2CL |
| SAP_CA_BC_IC_LND_RFM_DSP_PC | Retail and Fashion Management - Configuration Display | S_XB4_60000156 | S_XB4_60000156_03_TRAN | WRF_GEN_HIER_001 | Edit Application Parameters |  | LO-RFM | LO-RFM-MD-MC-2CL |
| SAP_CA_BC_IC_LND_RFM_DSP_PC | Retail and Fashion Management - Configuration Display | WC05 |  | W_ZF_VK_0490 | Number Ranges, Allocation Table |  | LO-RFM | LO-RFM-PUR-AL-2CL |
| SAP_CA_BC_IC_LND_RFM_DSP_PC | Retail and Fashion Management - Configuration Display | S_ALR_87008663 | S_ALR_87008663_03_TRAN | W_ZF_VK_0490 | Number Ranges, Allocation Table |  | LO-RFM | LO-RFM-PUR-AL-2CL |
| SAP_CA_BC_IC_LND_RFM_DSP_PC | Retail and Fashion Management - Configuration Display | S_ALR_87006137 | S_ALR_87006137_03_TRAN | W_ZF_VK_0240 | Number Ranges, Promotions |  | LO-RFM | LO-RFM-MD-PR-2CL |
| SAP_CA_BC_IC_LND_RFM_DSP_PC | Retail and Fashion Management - Configuration Display | S_ALR_87000648 | S_ALR_87000648_03_TRAN | W_DF_LT_0611 | Number Ranges for Replenishment Run |  | LO-RFM | LO-RFM-PUR-2CL |
| SAP_CA_BC_IC_LND_RFM_DSP_PC | Retail and Fashion Management - Configuration Display | WC61 |  | W_DF_LT_0611 | Number Ranges for Replenishment Run |  | LO-RFM | LO-RFM-PUR-2CL |
| SAP_CA_BC_IC_LND_RFM_DSP_PC | Retail and Fashion Management - Configuration Display | WC04 |  | W_ZF_VK_0240 | Number Ranges, Promotions |  | LO-RFM | LO-RFM-MD-PR-2CL |
| SAP_CA_BC_IC_LND_RFM_DSP_PC | Retail and Fashion Management - Configuration Display | S_XB4_60000024 | S_XB4_60000024_03_TRAN | W_ZF_VK_1000_ADD | Additional Parameters for Pricing |  | LO-RFM | LO-RFM-MD-RPC-2CL |
| SAP_CA_BC_IC_LND_RFM_DSP_PC | Retail and Fashion Management - Configuration Display | S_P99_41000051 | S_P99_41000051_03_TRAN | W_ZF_VK_0301 | Number Ranges, Pricing Document |  | LO-RFM | LO-RFM-MD-RPC-2CL |
| SAP_CA_BC_IC_LND_RFM_DSP_PC | Retail and Fashion Management - Configuration Display | WC02 |  | W_ZF_VK_0301 | Number Ranges, Pricing Document |  | LO-RFM | LO-RFM-MD-RPC-2CL |
| SAP_CA_BC_IC_LND_RFM_DSP_PC | Retail and Fashion Management - Configuration Display | S_ER9_52002641 | S_ER9_52002641_03_TRAN | W_ZF_VK_0302 | Maintain Assignment of Number Range to Pricing Document Type |  | LO-RFM | LO-RFM-MD-RPC-2CL |
| SAP_CA_BC_IC_LND_RFM_DSP_PC | Retail and Fashion Management - Configuration Display | S_ER9_52002642 | S_ER9_52002642_03_TRAN | W_ZF_VK_0303 | Maintain Purchase Price Determination Sequence |  | LO-RFM | LO-RFM-MD-RPC-2CL |
| SAP_CA_BC_IC_LND_RFM_DSP_PC | Retail and Fashion Management - Configuration Display | S_ER9_52002643 | S_ER9_52002643_03_TRAN | W_ZF_VK_0304 | Maintain Sales Price Determination Sequence |  | LO-RFM | LO-RFM-MD-RPC-2CL |
| SAP_CA_BC_IC_LND_RFM_DSP_PC | Retail and Fashion Management - Configuration Display | S_ALR_87007780 | S_ALR_87007780_03_TRAN | W_ZF_VK_0360 | Texts For List Fields |  | LO-RFM | LO-RFM-MD-RPC-2CL |
| SAP_CA_BC_IC_LND_RFM_DSP_PC | Retail and Fashion Management - Configuration Display | OWV8 |  | W_ZF_VK_0360 | Texts For List Fields |  | LO-RFM | LO-RFM-MD-RPC-2CL |
| SAP_CA_BC_IC_LND_RFM_DSP_PC | Retail and Fashion Management - Configuration Display | S_ER9_52003372 | S_ER9_52003372_03_TRAN | V_RFM_SITE_SLSAR | Maintain Sales Area for Retail Site |  | LO-RFM | LO-RFM-MD-SIT-2CL |
| SAP_CA_BC_IC_LND_RFM_DSP_PC | Retail and Fashion Management - Configuration Display | S_AL0_96000510 | S_AL0_96000510_03_TRAN | W_ZF_VK_1000 | General Parameters for Pricing |  | LO-RFM | LO-RFM-MD-RPC-2CL |
| SAP_CA_BC_IC_LND_RFM_DSP_PC | Retail and Fashion Management - Configuration Display | S_ALR_87007677 | S_ALR_87007677_03_TRAN | W_OE_EG_WL_0170 | Plant Profiles |  | LO-RFM | LO-RFM-MD-SIT-2CL |
| SAP_CA_BC_IC_LND_RFM_DSP_PC | Retail and Fashion Management - Configuration Display | S_ER9_52004141 | S_ER9_52004141_03_TRAN | V_RFM_EMPTIES | Activate Empties Processing |  | LO-RFM | LO-RFM-MD-SIT-2CL |
| SAP_CA_BC_IC_LND_RFM_DSP_PC | Retail and Fashion Management - Configuration Display | S_ER9_52003119 | S_ER9_52003119_03_TRAN | V_RFM_SITE | Define Retail Site |  | LO-RFM | LO-RFM-MD-SIT-2CL |
| SAP_CA_BC_IC_LND_RFM_DSP_PC | Retail and Fashion Management - Configuration Display | S_ER1_70001313 | S_ER1_70001313_03_TRAN | RTL_MNG_SO_ACTVT | Activate Retail Features in Manage In-Store Sales Orders |  | LO-RFM | LO-RFM-STO-FIO-2CL |
| SAP_CA_BC_IC_LND_RFM_DSP_PC | Retail and Fashion Management - Configuration Display | V_RFM_SITE |  | V_RFM_SITE | Define Retail Site |  | LO-RFM | LO-RFM-MD-SIT-2CL |
| SAP_CA_BC_IC_LND_RFM_DSP_PC | Retail and Fashion Management - Configuration Display | S_ER1_70001253 | S_ER1_70001253_03_TRAN | RFM_CBC_SITE_OKB9 | Manage Default Account Assignments |  | LO-RFM | LO-RFM-MD-SIT-2CL |
| SAP_CA_BC_IC_LND_RFM_DSP_PC | Retail and Fashion Management - Configuration Display | RFM_ST_PICK_REQ_NR |  | NUM_RANGE_STORE_PICK | Maintain Number Range for Store Picking Requests |  | LO-RFM | LO-RFM-STO-FIO-2CL |
| SAP_CA_BC_IC_LND_RFM_DSP_PC | Retail and Fashion Management - Configuration Display | S_EB5_05000251 | S_EB5_05000251_03_TRAN | V_T6I2 | Document Category WIND Direct Entry |  | LO-RFM | LO-RFM-PUR-ADA-2CL |
| SAP_CA_BC_IC_LND_RFM_DSP_PC | Retail and Fashion Management - Configuration Display | V_RFM_SITE_SLSAR |  | V_RFM_SITE_SLSAR | Maintain Sales Area for Retail Site |  | LO-RFM | LO-RFM-MD-SIT-2CL |
| SAP_CA_BC_IC_LND_RFM_DSP_PC | Retail and Fashion Management - Configuration Display | OKB9 |  | RFM_CBC_SITE_OKB9 | Manage Default Account Assignments |  | LO-RFM | LO-RFM-MD-SIT-2CL |
| SAP_CA_BC_IC_LND_RFM_DSP_PC | Retail and Fashion Management - Configuration Display | S_ER1_70001537 | S_ER1_70001537_03_TRAN | RTL_PKNG_REQ_ACTVT | Activate Store Pickup Order and Store Picking Request Generation |  | LO-RFM | LO-RFM-STO-FIO-2CL |
| SAP_CA_BC_IC_LND_RFM_DSP_PC | Retail and Fashion Management - Configuration Display | RTL_PKNG_REQ_ACTVT |  | RTL_PKNG_REQ_ACTVT | Activate Store Pickup Order and Store Picking Request Generation |  | LO-RFM | LO-RFM-STO-FIO-2CL |
| SAP_CA_BC_IC_LND_RFM_DSP_PC | Retail and Fashion Management - Configuration Display | S_ER9_52002047 | S_ER9_52002047_03_TRAN | NUM_RANGE_STORE_PICK | Maintain Number Range for Store Picking Requests |  | LO-RFM | LO-RFM-STO-FIO-2CL |
| SAP_CA_BC_IC_LND_RFM_DSP_PC | Retail and Fashion Management - Configuration Display | S_AEN_10000424 | S_AEN_10000424_03_TRAN | W_CONS_0007 | Activate Consignment Returns with Shipping Processing |  | LO-RFM | LO-RFM-LG-IM-2CL |
| SAP_CA_BC_IC_LND_RFM_DSP_PC | Retail and Fashion Management - Configuration Display | S_P00_07000205 | S_P00_07000205_03_TRAN | SIMG_CMMENUOLMSRETL1 | Check Settings Related to Structured Materials |  | LO-RFM | LO-RFM-MD-ART-2CL |
| SAP_CA_BC_IC_LND_RFM_DSP_PC | Retail and Fashion Management - Configuration Display | RTL_MNG_SO_ACTVT |  | RTL_MNG_SO_ACTVT | Activate Retail Features in Manage In-Store Sales Orders |  | LO-RFM | LO-RFM-STO-FIO-2CL |
| SAP_CA_BC_IC_LND_RFM_DSP_PC | Retail and Fashion Management - Configuration Display | S_ALR_87001945 | S_ALR_87001945_03_TRAN | W_GE_0300 | Structured Material Maintenance |  | LO-RFM | LO-RFM-MD-ART-2CL |
| SAP_CA_BC_IC_LND_RFM_DSP_PC | Retail and Fashion Management - Configuration Display | OS24 |  | SIMG_CMMENUOLMSRETL1 | Check Settings Related to Structured Materials |  | LO-RFM | LO-RFM-MD-ART-2CL |
| SAP_CA_BC_IC_LND_RFM_DSP_PC | Retail and Fashion Management - Configuration Display | V_TVAP |  | SIMG_CMMENUOLMSRETL1 | Check Settings Related to Structured Materials |  | LO-RFM | LO-RFM-MD-ART-2CL |
| SAP_CA_BC_IC_LND_RFM_DSP_PC | Retail and Fashion Management - Configuration Display | OS31 |  | SIMG_CMMENUOLMSRETL1 | Check Settings Related to Structured Materials |  | LO-RFM | LO-RFM-MD-ART-2CL |
| SAP_CA_BC_IC_LND_RFM_DSP_PC | Retail and Fashion Management - Configuration Display | OS14 |  | SIMG_CMMENUOLMSRETL1 | Check Settings Related to Structured Materials |  | LO-RFM | LO-RFM-MD-ART-2CL |
| SAP_CA_BC_IC_LND_RFM_DSP_PC | Retail and Fashion Management - Configuration Display | S_ALR_87001951 | S_ALR_87001951_03_TRAN | W_ZF_ST_0350 | Structured Material in Logistics Process | 107393 | LO-RFM | LO-RFM-MD-ART-2CL |
| SAP_CA_BC_IC_LND_RFM_DSP_PC | Retail and Fashion Management - Configuration Display | V_T184 |  | SIMG_CMMENUOLMSRETL1 | Check Settings Related to Structured Materials |  | LO-RFM | LO-RFM-MD-ART-2CL |
| SAP_CA_BC_IC_LND_RFM_DSP_PC | Retail and Fashion Management - Configuration Display | OMXL |  | SIMG_CMMENUOLMSRETL1 | Check Settings Related to Structured Materials |  | LO-RFM | LO-RFM-MD-ART-2CL |
| SAP_CA_BC_IC_LND_RFM_DSP_PC | Retail and Fashion Management - Configuration Display | S_XB4_60000027 | S_XB4_60000027_03_TRAN | W_CONS_0004 | Edit Values for Consignment Control |  | LO-RFM | LO-RFM-LG-IM-2CL |
| SAP_CA_BC_IC_LND_RFM_DSP_PC | Retail and Fashion Management - Configuration Display | OS30 |  | SIMG_CMMENUOLMSRETL1 | Check Settings Related to Structured Materials |  | LO-RFM | LO-RFM-MD-ART-2CL |
| SAP_CA_BC_IC_LND_RFM_DSP_PC | Retail and Fashion Management - Configuration Display | OS20 |  | SIMG_CMMENUOLMSRETL1 | Check Settings Related to Structured Materials |  | LO-RFM | LO-RFM-MD-ART-2CL |
| SAP_CA_BC_IC_LND_RFM_DSP_PC | Retail and Fashion Management - Configuration Display | S_XB4_60000011 | S_XB4_60000011_03_TRAN | W_CONS_0002 | Activate Retail Consignment Processing |  | LO-RFM | LO-RFM-LG-IM-2CL |
| SAP_CA_BC_IC_LND_RFM_DSP_PC | Retail and Fashion Management - Configuration Display | S_XB4_60000185 | S_XB4_60000185_03_TRAN | W_CONS_0006 | Define Strategies for Stock Determination |  | LO-RFM | LO-RFM-LG-IM-2CL |
| SAP_CA_BC_IC_LND_RFM_DSP_PC | Retail and Fashion Management - Configuration Display | OSPX |  |  |  |  | LO-RFM |  |
| SAP_CA_BC_IC_LND_RFM_DSP_PC | Retail and Fashion Management - Configuration Display | S_PEN_05000049 | S_PEN_05000049_03_TRAN | W_CONS_0015 | Delivery |  | LO-RFM | LO-RFM-LG-IM-2CL |
| SAP_CA_BC_IC_LND_RFM_DSP_PC | Retail and Fashion Management - Configuration Display | S_ALN_01000936 | S_ALN_01000936_03_TRAN | W_ZF_ST_0380 | Changeability of Structured Materials |  | LO-RFM | LO-RFM-MD-ART-2CL |
| SAP_CA_BC_IC_LND_RFM_DSP_PC | Retail and Fashion Management - Configuration Display | S_ER9_52000405 | S_ER9_52000405_03_TRAN | SIMG_T160M_GA_S4 | Deactivate Compatibility Check for Configuration Classes |  | LO-RFM | LO-RFM-MD-ART-2CL |
| SAP_CA_BC_IC_LND_RFM_DSP_PC | Retail and Fashion Management - Configuration Display | S_PEN_05000044 | S_PEN_05000044_03_TRAN | W_CONS_0010 | Inventory Management |  | LO-RFM | LO-RFM-LG-IM-2CL |
| SAP_CA_BC_IC_LND_RFM_DSP_PC | Retail and Fashion Management - Configuration Display | S_ER9_52002716 | S_ER9_52002716_03_TRAN | V_RFM_C_REFSITE | Enable Group Type for Reference Site |  | LO-RFM | LO-RFM-IFC-OUT-2CL |
| SAP_CA_BC_IC_LND_RFM_DSP_PC | Retail and Fashion Management - Configuration Display | S_AL0_96000461 | S_AL0_96000461_03_TRAN | W_GE_0400 | Activation of the Direct Entry for Creating the Worklist |  | LO-RFM | LO-RFM-PUR-ADA-2CL |
| SAP_CA_BC_IC_LND_RFM_DSP_PC | Retail and Fashion Management - Configuration Display | S_EB5_05000250 | S_EB5_05000250_03_TRAN | V_T6I1_P | Document Index | 105390 | LO-RFM | LO-RFM-PUR-ADA-2CL |
| SAP_CA_BC_IC_LND_RFM_DSP_PC | Retail and Fashion Management - Configuration Display | S_PL0_09000435 | S_PL0_09000435_03_TRAN | W_GE_0402 | Define the Scope of Change for Direct Entry in Worklist |  | LO-RFM | LO-RFM-PUR-ADA-2CL |
| SAP_CA_BC_IC_LND_RFM_DSP_PC | Retail and Fashion Management - Configuration Display | WC36 |  | W_DF_LT_0331 | Number Ranges, Revaluation |  | LO-RFM | LO-RFM-LG-SPV-2CL |
| SAP_CA_BC_IC_LND_RFM_DSP_PC | Retail and Fashion Management - Configuration Display | S_ALR_87002274 | S_ALR_87002274_03_TRAN | W_DF_LT_0331 | Number Ranges, Revaluation |  | LO-RFM | LO-RFM-LG-SPV-2CL |
| SAP_CA_BC_IC_LND_RFM_DSP_PC | Retail and Fashion Management - Configuration Display | FSH_VAS_NR |  | FSH_VAS_NR | Define Number Ranges |  | LO-RFM | LO-RFM-SD-2CL |
| SAP_CA_BC_IC_LND_RFM_DSP_PC | Retail and Fashion Management - Configuration Display | S_ALR_87005960 | S_ALR_87005960_03_TRAN | W_GE_0200 | Applications |  | LO-RFM | LO-RFM-CA-2CL |
| SAP_CA_BC_IC_LND_RFM_DSP_PC | Retail and Fashion Management - Configuration Display | FSH_SEASONS_NR |  | FSH_SEASONS_NR | Define Number Ranges |  | LO-RFM | LO-RFM-CA-SE-2CL |
| SAP_CA_BC_IC_LND_RFM_DSP_PC | Retail and Fashion Management - Configuration Display | S_ESI_04000084 | S_ESI_04000084_03_TRAN | FSH_VAS_NR | Define Number Ranges |  | LO-RFM | LO-RFM-SD-2CL |
| SAP_CA_BC_IC_LND_RFM_DSP_PC | Retail and Fashion Management - Configuration Display | S_ESI_04000095 | S_ESI_04000095_03_TRAN | FSH_SEASONS_NR | Define Number Ranges |  | LO-RFM | LO-RFM-CA-SE-2CL |
| SAP_CA_BC_IC_LND_RFM_DSP_PC | Retail and Fashion Management - Configuration Display | S_ALR_87001951 | S_ALR_87001951_03_TRAN | W_ZF_ST_0350 | Structured Material in Logistics Process | 107393 | LO-RFM | LO-RFM-MD-ART-2CL |
| SAP_CA_BC_IC_LND_RFM_DSP_PC | Retail and Fashion Management - Configuration Display | V_TWZLA |  | W_ZF_ST_0350 | Structured Material in Logistics Process | 107393 | LO-RFM | LO-RFM-MD-ART-2CL |
| SAP_CA_BC_IC_LND_PRD_DSP_PC | Settings for Product Cost Accounting - Display Configuration | S_ALR_87008030 | S_ALR_87008030_TRAN | SIMG_CFMENUORKKOPK9 | Define Goods Received Valuation for Order Delivery |  | CO-PC-OBJ | CO-PC-OBJ-2CL |
| SAP_CA_BC_IC_LND_PRD_DSP_PC | Settings for Product Cost Accounting - Display Configuration | OPL1 |  | SIMG_PP3ORKKOPL1 | Check Costing Variants for Product Cost Collectors |  | CO-PC-OBJ | CO-PC-OBJ-2CL |
| SAP_CA_BC_IC_LND_PRD_DSP_PC | Settings for Product Cost Accounting - Display Configuration | OPL1 |  | SIMG_PP3ORKKOPL1 | Check Costing Variants for Product Cost Collectors |  | CO-PC-OBJ | CO-PC-OBJ-2CL |
| SAP_CA_BC_IC_LND_PRD_DSP_PC | Settings for Product Cost Accounting - Display Configuration | S_ALR_87008271 | S_ALR_87008271_TRAN | SIMG_PP3ORKKOPL1 | Check Costing Variants for Product Cost Collectors |  | CO-PC-OBJ | CO-PC-OBJ-2CL |
| SAP_CA_BC_IC_LND_PRD_DSP_PC | Settings for Product Cost Accounting - Display Configuration | OKKN |  | SIMG_PP3ORKKOPL1 | Check Costing Variants for Product Cost Collectors |  | CO-PC-OBJ | CO-PC-OBJ-2CL |
| SAP_CA_BC_IC_LND_PRD_DSP_PC | Settings for Product Cost Accounting - Display Configuration | S_ALR_87008037 | S_ALR_87008037_TRAN | SIMG_CFMENUORKKOPL1 | Check Costing Variants for Manufacturing Orders (PP) |  | CO-PC-OBJ | CO-PC-OBJ-2CL |
| SAP_CA_BC_IC_LND_SCM_ATP7_PC | ATP Influencer Log Activation - Configuration | S_ER1_70001918 | S_ER1_70001918_TRAN | ATP_INFLCR_LOG_V | Define Influencer Logging Level Configuration |  | CA-ATP | CA-ATP-2CL |
| SAP_CA_BC_IC_LND_SMGMT_DSP_PC | Settlement Management - Configuration Display | S_AEN_10000151 | S_AEN_10000151_TRAN | W_WCB_CC__PERS_VM02 | Define Check Groups |  | LO-AB | LO-GT-CHB |
| SAP_CA_BC_IC_LND_SMGMT_DSP_PC | Settlement Management - Configuration Display | S_AEN_10000193 | S_AEN_10000193_TRAN | W_WCB_CC__PERS_VM10 | Define Condition Type Groups |  | LO-AB | LO-GT-CHB |
| SAP_CA_BC_IC_LND_SMGMT_DSP_PC | Settlement Management - Configuration Display | S_ALN_01001454 | S_ALN_01001454_TRAN | W_WLFA_0056 | Define Number Range |  | LO-AB | LO-AB |
| SAP_CA_BC_IC_LND_SMGMT_DSP_PC | Settlement Management - Configuration Display | WCWBNR |  | W_WLFA_0056 | Define Number Range |  | LO-AB | LO-AB |
| SAP_CA_BC_IC_LND_SMGMT_DSP_PC | Settlement Management - Configuration Display | S_AEN_10000157 | S_AEN_10000157_TRAN | W_WCB_CC_PERS_VM08 | Assign Check Classes to Condition Contract Table Structures |  | LO-AB | LO-GT-CHB |
| SAP_CA_BC_IC_LND_SMGMT_DSP_PC | Settlement Management - Configuration Display | S_AEN_10000195 | S_AEN_10000195_TRAN | W_WCB_CC__PERS_VM12 | Define Condition Type Groups |  | LO-AB | LO-GT-CHB |
| SAP_CA_BC_IC_LND_SMGMT_DSP_PC | Settlement Management - Configuration Display | S_AEN_10000194 | S_AEN_10000194_TRAN | W_WCB_CC__PERS_VM11 | Assign Condition Types to Condition Type Groups |  | LO-AB | LO-GT-CHB |
| SAP_CA_BC_IC_LND_SMGMT_DSP_PC | Settlement Management - Configuration Display | S_AEN_10000196 | S_AEN_10000196_TRAN | W_WCB_CC__PERS_VM13 | Assign Condition Types to Condition Type Groups |  | LO-AB | LO-GT-CHB |
| SAP_CA_BC_IC_LND_SMGMT_DSP_PC | Settlement Management - Configuration Display | S_AEN_10000201 | S_AEN_10000201_TRAN | W_WCB_CC_PERS_VM15 | Specify CC Determination Relevance and Copy Control for Condition Types |  | LO-AB | LO-GT-CHB |
| SAP_CA_BC_IC_LND_SMGMT_DSP_PC | Settlement Management - Configuration Display | S_AEN_10000203 | S_AEN_10000203_TRAN | W_WCB_CC_PERS_VM17 | Specify CC Determination Relevance and Copy Control for Condition Types |  | LO-AB | LO-GT-CHB |
| SAP_CA_BC_IC_LND_SMGMT_DSP_PC | Settlement Management - Configuration Display | S_AEN_10000364 | S_AEN_10000364_TRAN | W_WCB_CC_PERS_VM24 | Define Text Determination Procedures |  | LO-AB | LO-GT-CHB |
| SAP_CA_BC_IC_LND_SMGMT_DSP_PC | Settlement Management - Configuration Display | S_AEN_10000365 | S_AEN_10000365_TRAN | W_WCB_CC_PERS_VM25 | Specify Text Types for Text Determination Procedure |  | LO-AB | LO-GT-CHB |
| SAP_CA_BC_IC_LND_SMGMT_DSP_PC | Settlement Management - Configuration Display | SSCUI_VC_TTXZ_SDH |  | W_WLFA_0016 | Specify Text Determination |  | LO-AB | LO-AB |
| SAP_CA_BC_IC_LND_SMGMT_DSP_PC | Settlement Management - Configuration Display | S_ALR_87001863 | S_ALR_87001863_TRAN | W_WLFA_0016 | Specify Text Determination |  | LO-AB | LO-AB |
| SAP_CA_BC_IC_LND_SMGMT_DSP_PC | Settlement Management - Configuration Display | SSCUI_VC_TTXZ_SDI |  | W_WLFA_0016 | Specify Text Determination |  | LO-AB | LO-AB |
| SAP_CA_BC_IC_LND_SMGMT_DSP_PC | Settlement Management - Configuration Display | SSCUI_VC_WBRK_SSCUI |  | W_WLFA_0016 | Specify Text Determination |  | LO-AB | LO-AB |
| SAP_CA_BC_IC_LND_SMGMT_DSP_PC | Settlement Management - Configuration Display | VOTXN |  | W_WLFA_0016 | Specify Text Determination |  | LO-AB | LO-AB |
| SAP_CA_BC_IC_LND_SMGMT_DSP_PC | Settlement Management - Configuration Display | SSCUI_VC_WBRP_SSCUI |  | W_WLFA_0016 | Specify Text Determination |  | LO-AB | LO-AB |
| SAP_CA_BC_IC_LND_SMGMT_DSP_PC | Settlement Management - Configuration Display | S_ALR_87001898 | S_ALR_87001898_TRAN | W_WLFA_0019 | Define Status Groups with Application Statuses |  | LO-AB | LO-AB |
| SAP_CA_BC_IC_LND_SMGMT_DSP_PC | Settlement Management - Configuration Display | S_E4A_94000042 | S_E4A_94000042_TRAN | W_WLFA_0001 | Specify Copy Control |  | LO-AB | LO-AB |
| SAP_CA_BC_IC_LND_SMGMT_DSP_PC | Settlement Management - Configuration Display | CUST_V_TMCPF |  | W_WLFA_0001 | Specify Copy Control |  | LO-AB | LO-AB |
| SAP_CA_BC_IC_LND_SMGMT_DSP_PC | Settlement Management - Configuration Display | CUST_V_TMCPF_VT |  | W_WLFA_0001 | Specify Copy Control |  | LO-AB | LO-AB |
| SAP_CA_BC_IC_LND_SMGMT_DSP_PC | Settlement Management - Configuration Display | S_E4A_94000059 | S_E4A_94000059_TRAN | WLF_PV_01 | Specify Extended Scope of Settlement Management |  | LO-AB | LO-AB |
| SAP_CA_BC_IC_LND_SMGMT_DSP_PC | Settlement Management - Configuration Display | S_E31_55000001 | S_E31_55000001_TRAN | W_WCB_PERS_FEAT | Activate Additional Functions |  | LO-AB | LO-GT-CHB |
| SAP_CA_BC_IC_LND_SMGMT_DSP_PC | Settlement Management - Configuration Display | S_E4A_94000134 | S_E4A_94000134_TRAN | WLF_TMFSG | Define Field Status Groups |  | LO-AB | LO-AB |
| SAP_CA_BC_IC_LND_SMGMT_DSP_PC | Settlement Management - Configuration Display | S_E4A_94000135 | S_E4A_94000135_TRAN | WLF_TMCSGR | Define Column Sorting Groups |  | LO-AB | LO-AB |
| SAP_CA_BC_IC_LND_SMGMT_DSP_PC | Settlement Management - Configuration Display | S_E4A_94000143 | S_E4A_94000143_TRAN | V_WRART_LFART | Allowed Combinations Settlement Process Type / Settlement Document Type |  | LO-AB | LO-AB |
| SAP_CA_BC_IC_LND_SMGMT_DSP_PC | Settlement Management - Configuration Display | S_EBJ_98000089 | S_EBJ_98000089_TRAN | WLF_V_PROCTYPE | Define Process Categories |  | LO-AB | LO-AB |
| SAP_CA_BC_IC_LND_SMGMT_DSP_PC | Settlement Management - Configuration Display | WLF_VC_TPAR_AK_SSCUI |  | WLF_PART_IMG | Specify Settings for Partner Determination |  | LO-AB | LO-AB |
| SAP_CA_BC_IC_LND_SMGMT_DSP_PC | Settlement Management - Configuration Display | S_EBS_44000108 | S_EBS_44000108_TRAN | WLF_PART_IMG | Specify Settings for Partner Determination |  | LO-AB | LO-AB |
| SAP_CA_BC_IC_LND_SMGMT_DSP_PC | Settlement Management - Configuration Display | WLF_VC_TPAR_AI_SSCUI |  | WLF_PART_IMG | Specify Settings for Partner Determination |  | LO-AB | LO-AB |
| SAP_CA_BC_IC_LND_SMGMT_DSP_PC | Settlement Management - Configuration Display | S_EBS_44000373 | S_EBS_44000373_TRAN | VWLF_DOCTYPE_AIS | Assign Archive Info Structure to Document Category for Enh. Archive Display |  | LO-AB | LO-AB |
| SAP_CA_BC_IC_LND_SMGMT_DSP_PC | Settlement Management - Configuration Display | S_EBS_44000549 | S_EBS_44000549_TRAN | WZRE_EPOST_DATA | Basic Settings for Creation of Settlement Management Documents |  | LO-AB | LO-AB |
| SAP_CA_BC_IC_LND_SMGMT_DSP_PC | Settlement Management - Configuration Display | S_EG6_66000014 | S_EG6_66000014_TRAN | WB2_V_BVTAB | Define and Configure Profiles for Business Volume Determination |  | LO-AB | LO-GT-CHB |
| SAP_CA_BC_IC_LND_SMGMT_DSP_PC | Settlement Management - Configuration Display | WZRN1 |  | W_WLFA_0011 | Define Number Ranges |  | LO-AB | LO-AB |
| SAP_CA_BC_IC_LND_SMGMT_DSP_PC | Settlement Management - Configuration Display | S_EG6_66000015 | S_EG6_66000015_TRAN | WB2_VC_BVB_FC | Define and Configure Field Combinations for Business Volume Selection |  | LO-AB | LO-GT-CHB |
| SAP_CA_BC_IC_LND_SMGMT_DSP_PC | Settlement Management - Configuration Display | S_EGI_66000080 | S_EGI_66000080_TRAN | WB2_C_AF_GROUP | Define Amount Fields Groups |  | LO-AB | LO-GT-CHB |
| SAP_CA_BC_IC_LND_SMGMT_DSP_PC | Settlement Management - Configuration Display | S_ER9_52000113 | S_ER9_52000113_TRAN | W_WLFA_0011 | Define Number Ranges |  | LO-AB | LO-AB |
| SAP_CA_BC_IC_LND_SMGMT_DSP_PC | Settlement Management - Configuration Display | S_EGI_66000082 | S_EGI_66000082_TRAN | W_WCB_CC_PERS_VM28 | Define and Configure Critical Changes Groups |  | LO-AB | LO-GT-CHB |
| SAP_CA_BC_IC_LND_SMGMT_DSP_PC | Settlement Management - Configuration Display | S_ER9_52000064 | S_ER9_52000064_TRAN | W_WLFA_0008 | Define Document Schema Groups for Settlement Document Types |  | LO-AB | LO-AB |
| SAP_CA_BC_IC_LND_SMGMT_DSP_PC | Settlement Management - Configuration Display | S_EG6_66000042 | S_EG6_66000042_TRAN | W_WCB_CC_PERS_VM26 | Define and Configure Field Status Groups |  | LO-AB | LO-GT-CHB |
| SAP_CA_BC_IC_LND_SMGMT_DSP_PC | Settlement Management - Configuration Display | VV_T687_M1_SSCUI |  | W_WLFA_0002 | Define Account Keys |  | LO-AB | LO-AB |
| SAP_CA_BC_IC_LND_SMGMT_DSP_PC | Settlement Management - Configuration Display | S_EGI_66000068 | S_EGI_66000068_TRAN | WB2_VC_BVTAB_GRP | Define and Configure Business Volume Table Groups |  | LO-AB | LO-GT-CHB |
| SAP_CA_BC_IC_LND_SMGMT_DSP_PC | Settlement Management - Configuration Display | S_ER9_52000126 | S_ER9_52000126_TRAN | W_WLFA_0002 | Define Account Keys |  | LO-AB | LO-AB |
| SAP_CA_BC_IC_LND_SMGMT_DSP_PC | Settlement Management - Configuration Display | S_ER9_52000132 | S_ER9_52000132_TRAN | WLF_SD_PRICE_PRO | Define Pricing Procedures |  | LO-AB | LO-AB |
| SAP_CA_BC_IC_LND_SMGMT_DSP_PC | Settlement Management - Configuration Display | S_EGI_66000029 | S_EGI_66000029_TRAN | W_WCB_CC_PERS_VM27 | Define Condition Contract Categories |  | LO-AB | LO-GT-CHB |
| SAP_CA_BC_IC_LND_SMGMT_DSP_PC | Settlement Management - Configuration Display | OMRS |  | W_WLFA_0002 | Define Account Keys |  | LO-AB | LO-AB |
| SAP_CA_BC_IC_LND_SMGMT_DSP_PC | Settlement Management - Configuration Display | S_EG6_66000046 | S_EG6_66000046_TRAN | WB2_VC_ACCRUALS | Define and Configure Condition Type Groups for Accruals |  | LO-AB | LO-GT-CHB |
| SAP_CA_BC_IC_LND_SMGMT_DSP_PC | Settlement Management - Configuration Display | S_ER9_52000244 | S_ER9_52000244_TRAN | WLF_VC_CFCG | Define Field Change Groups for Cancellation Documents |  | LO-AB | LO-AB |
| SAP_CA_BC_IC_LND_SMGMT_DSP_PC | Settlement Management - Configuration Display | S_ER9_52001521 | S_ER9_52001521_TRAN | WLF_V_COUNTRY | Country/Region Specific Settings in Settlement Management | 106704 | LO-AB | LO-AB |
| SAP_CA_BC_IC_LND_SMGMT_DSP_PC | Settlement Management - Configuration Display | S_ER9_52002938 | S_ER9_52002938_TRAN | WLF_SWL_NMR | Define Number Ranges for Scheduling Worklists |  | LO-AB | LO-AB |
| SAP_CA_BC_IC_LND_SMGMT_DSP_PC | Settlement Management - Configuration Display | S_ER9_52000620 | S_ER9_52000620_TRAN | WLF_V_NRG_ASGN | Define Country/Region and Company Code Specific Number Ranges |  | LO-AB | LO-AB |
| SAP_CA_BC_IC_LND_SMGMT_DSP_PC | Settlement Management - Configuration Display | S_ER9_52002939 | S_ER9_52002939_TRAN | WLF_V_SWL_NMR | Assign Number Range Intervals to Scheduling Worklist Templates |  | LO-AB | LO-AB |
| SAP_CA_BC_IC_LND_SMGMT_DSP_PC | Settlement Management - Configuration Display | S_ER9_52001606 | S_ER9_52001606_TRAN | WLF_V_TMFK_ASDT | Alternative Settlement Document Type Assignment |  | LO-AB | LO-AB |
| SAP_CA_BC_IC_LND_SMGMT_DSP_PC | Settlement Management - Configuration Display | S_ER9_52000822 | S_ER9_52000822_TRAN | WLF_TTXZI_WCB | Define and Configure Text Transfer Groups |  | LO-AB | LO-AB |
| SAP_CA_BC_IC_LND_SMGMT_DSP_PC | Settlement Management - Configuration Display | WLF_SWL_NMR |  | WLF_SWL_NMR | Define Number Ranges for Scheduling Worklists |  | LO-AB | LO-AB |
| SAP_CA_BC_IC_LND_SMGMT_DSP_PC | Settlement Management - Configuration Display | S_ER9_52002912 | S_ER9_52002912_TRAN | WLF_V_SWL_TECJOB | Define Retention Days for Scheduling Worklist Entries |  | LO-AB | LO-AB |
| SAP_CA_BC_IC_LND_SMGMT_DSP_PC | Settlement Management - Configuration Display | S_P7D_67000074 | S_P7D_67000074_TRAN | WLF_TMPR | Define Posting Rules |  | LO-AB | LO-AB |
| SAP_CA_BC_IC_LND_SMGMT_DSP_PC | Settlement Management - Configuration Display | S_PCO_36000353 | S_PCO_36000353_TRAN | W_WLFA_0035 | Specify Settings for Transfer Manager |  | LO-AB | LO-AB |
| SAP_CA_BC_IC_LND_SMGMT_DSP_PC | Settlement Management - Configuration Display | WLF_VC_TMTEFK_SSCUI |  | W_WLFA_0035 | Specify Settings for Transfer Manager |  | LO-AB | LO-AB |
| SAP_CA_BC_IC_LND_SMGMT_DSP_PC | Settlement Management - Configuration Display | OWCB_CC10 |  | W_WCB_PERS_NUM | Define Number Ranges |  | LO-AB | LO-GT-CHB |
| SAP_CA_BC_IC_LND_SMGMT_DSP_PC | Settlement Management - Configuration Display | S_PRN_53000396 | S_PRN_53000396_TRAN | W_WCB_PERS_NUM | Define Number Ranges |  | LO-AB | LO-GT-CHB |
| SAP_CA_BC_IC_LND_SMGMT_DSP_PC | Settlement Management - Configuration Display | S_EGI_66000020 | S_EGI_66000020_TRAN | WB2_C_CCS | Specify General Settings |  | LO-AB | LO-GT-CHB |
| SAP_CA_BC_IC_LND_SMGMT_DSP_PC | Settlement Management - Configuration Display | WLF_VC_TMTR_SSCUI |  | W_WLFA_0035 | Specify Settings for Transfer Manager |  | LO-AB | LO-AB |
| SAP_CA_BC_IC_LND_SMGMT_DSP_PC | Settlement Management - Configuration Display | WLF_VC_TMFKTG_SSCUI |  | W_WLFA_0035 | Specify Settings for Transfer Manager |  | LO-AB | LO-AB |
| SAP_CA_BC_IC_LND_SMGMT_DSP_PC | Settlement Management - Configuration Display | S_EGI_66000081 | S_EGI_66000081_TRAN | WB2_V_SEL_GRP | Define Selection Groups |  | LO-AB | LO-GT-CHB |
| SAP_CA_BC_IC_LND_SMGMT_DSP_PC | Settlement Management - Configuration Display | S_ER9_52002206 | S_ER9_52002206_TRAN | WLF_VC_FVISG | Specify UI Behavior for Elements of SAP Fiori Apps |  | LO-AB | LO-AB |
| SAP_CA_BC_IC_LND_PLMCR_DSP_PC | Change Record Read Only - Configuration | S_ER1_70001281 | S_ER1_70001281_03_TRAN | PLM_V_STATFLD | Define Status Fields |  | PLM-CR | PLM-CR-2CL |
| SAP_CA_BC_IC_LND_PLMCR_DSP_PC | Change Record Read Only - Configuration | PLM_STATUSFLD |  | PLM_V_STATFLD | Define Status Fields |  | PLM-CR | PLM-CR-2CL |
| SAP_CA_BC_IC_LND_FIN_POA_D_PC | Purchase Order Accruals - Configuration Display | S_ER9_11001599 | S_ER9_11001599_03_TRAN | V_TACES4_POSTING | Define Posting Summarization |  | FI-GL | FI-GL-GL-ACE-2CL |
| SAP_CA_BC_IC_LND_GLO_LO_BG_PC | Globalisation Logistics for Bulgaria - Configuration | S_ER1_70001037 | S_ER1_70001037_TRAN | GLO_WLF_BLT_BG_V | Define Accounting Document Types for Settlement Management | 106782 | CA-GTF-CSC | FI-LOC-LO-BG-FRM |
| SAP_CA_BC_IC_LND_GLO_LO_BG_PC | Globalisation Logistics for Bulgaria - Configuration | WLF_V_BLART_BG |  | GLO_WLF_BLT_BG_V | Define Accounting Document Types for Settlement Management | 106782 | CA-GTF-CSC | FI-LOC-LO-BG-FRM |
| SAP_CA_BC_IC_LND_TAX_DSP_PC | Tax - Configuration Display | S_ALR_87099830 | S_ALR_87099830_TRAN | FI_APAR_TAX_OBETX | Define Number Ranges for External Tax Returns |  | FI-GL | FI-TXL-EXT-2CL |
| SAP_CA_BC_IC_LND_TAX_DSP_PC | Tax - Configuration Display | OBETX |  |  |  |  | FI-GL |  |
| SAP_CA_BC_IC_LND_TAX_DSP_PC | Tax - Configuration Display | S_ER9_11001295 | S_ER9_11001295_TRAN | V_FOT_TDT_ACTSTS | Maintain the Activation Status of Time-Dependent Taxes |  | FI-GL | FI-GL-GL-F-2CL |
| SAP_CA_BC_IC_LND_FIN_PR_PT_PC | Payment Receipt for Portugal - Configuration | PRNR |  | PRNR | Define Internal Number Ranges for Payment Receipts | 103389 | FI-LOC-FI-PT | FI-LOC-PR |
| SAP_CA_BC_IC_LND_FIN_PR_PT_PC | Payment Receipt for Portugal - Configuration | S_ER9_11001461 | S_ER9_11001461_TRAN | PAYTRCPT_CONFIG | Define Payment Receipt Types | 103387 | FI-LOC-FI-PT | FI-LOC-PR |
| SAP_CA_BC_IC_LND_FIN_PR_PT_PC | Payment Receipt for Portugal - Configuration | S_ER9_11001463 | S_ER9_11001463_TRAN | PRNR | Define Internal Number Ranges for Payment Receipts | 103389 | FI-LOC-FI-PT | FI-LOC-PR |
| SAP_CA_BC_IC_LND_FIN_PR_AR_PC | Payment Receipt for Argentina - Configuration | S_ER9_11001461 | S_ER9_11001461_TRAN | PAYTRCPT_CONFIG | Define Payment Receipt Types | 103387 | FI-LOC-FI-AR | FI-LOC-PR |
| SAP_CA_BC_IC_LND_FIN_PFC_PC | Advanced Payment Management - Configuration | MFD_F5617 |  | MFD_F5617 | Map Format Data for Advanced Payment Management | 170009 | FIN-FSCM-PF | CA-GTF-CSC-DME |
| SAP_CA_BC_IC_LND_FIN_PFC_PC | Advanced Payment Management - Configuration | MFD_F5617 |  | MFD_F5617 | Map Format Data for Advanced Payment Management | 170009 | FIN-FSCM-PF | CA-GTF-CSC-DME |
| SAP_CA_BC_IC_LND_FIN_PFC_PC | Advanced Payment Management - Configuration | MFD_F5617 |  | MFD_F5617 | Map Format Data for Advanced Payment Management | 170009 | FIN-FSCM-PF | CA-GTF-CSC-DME |
| SAP_CA_BC_IC_LND_GLO_LO2_PC | Globalisation Logistics - Configuration | OMC1 |  | SIMG_CFMENUOLMBOMC1 | Define Number Assignment for Goods Receipt/Issue Slips | 105614 | FI-LOC-LO | MM-IM-GF-2CL |
| SAP_CA_BC_IC_LND_GLO_LO2_PC | Globalisation Logistics - Configuration | OMC1 |  | SIMG_CFMENUOLMBOMC1 | Define Number Assignment for Goods Receipt/Issue Slips | 105614 | FI-LOC-LO | MM-IM-GF-2CL |
| SAP_CA_BC_IC_LND_GLO_LO2_PC | Globalisation Logistics - Configuration | OMC1 |  | SIMG_CFMENUOLMBOMC1 | Define Number Assignment for Goods Receipt/Issue Slips | 105614 | FI-LOC-LO | MM-IM-GF-2CL |
| SAP_CA_BC_IC_LND_GLO_LO2_PC | Globalisation Logistics - Configuration | V_158_2D | V_158_2D_TRAN | OLMW_001K_EK2_GLO | Configure Document Type for Separate FI Document | 106880 | FI-LOC-LO | FI-LOC-LO |
| SAP_CA_BC_IC_LND_FIN_TAX_PC | Tax - Configuration | FOT_F2609 |  | SIMG_FOT_F2609 | Upload Tax Rates | 100426 | FI-GL | FI-GL-GL-F-2CL |
| SAP_CA_BC_IC_LND_FIN_TAX_PC | Tax - Configuration | OBWZ |  | SIMG_CFORFBOBWZ | Define Number Ranges for Withholding Tax | 104786 | FI-GL | FI-AR-AR-2CL |
| SAP_CA_BC_IC_LND_QLTYMGMT_PC | Quality Management - Configuration | V_TQ80_E |  | OLQN-SCR_2 | Define Initial Screens | 104779 | QM | QM-2CL |
| SAP_CA_BC_IC_LND_QLTYMGMT_PC | Quality Management - Configuration | V_TQ32B |  | OLQW_OQLV_2 | Assign Inspection Type to Delivery Category | 105136 | QM | QM-2CL |
| SAP_CA_BC_IC_LND_QLTYMGMT_PC | Quality Management - Configuration | S_ALR_87000814_1 |  | OLQN-OQNP_2 | Assign Partner Determination Procedure to Notification Type | 105492 | QM | QM-2CL |
| SAP_CA_BC_IC_LND_QLTYMGMT_PC | Quality Management - Configuration | V_TQ80_PA |  | OLQN-OQNP | Define Partner Functions and Determination Procedures | 105493 | QM | QM-2CL |
| SAP_CA_BC_IC_LND_FIN_TRM_PC | Treasury and Risk Management - Configuration | MFD_F3554A |  | MFD_F3554A | Map Format Data for Treasury Correspondence | 170004 | FIN-FSCM-TRM | FIN-FSCM-TRM-TM-2CL |
| SAP_CA_BC_IC_LND_FIN_TRM_PC | Treasury and Risk Management - Configuration | MFD_F3554A |  | MFD_F3554A | Map Format Data for Treasury Correspondence | 170004 | FIN-FSCM-TRM | FIN-FSCM-TRM-TM-2CL |
| SAP_CA_BC_IC_LND_FIN_TRM_PC | Treasury and Risk Management - Configuration | MFD_F3554A |  | MFD_F3554A | Map Format Data for Treasury Correspondence | 170004 | FIN-FSCM-TRM | FIN-FSCM-TRM-TM-2CL |
| SAP_CA_BC_IC_LND_PP_DI0_PC | Shop Floor Control for Discrete Industries - Configuration | OP58 |  | SIMG_CFMENUOLPSOP58 | Define Routing Profiles with Default Values | 102528 | PP-FIO-SFC | PP-BD-RTG-2CL |
| SAP_CA_BC_IC_LND_FIN_GLA_PC | G/L Account Master Data - Configuration | OB_GLACC_F01 |  | SKAD | Not Used G/L Accounts |  | FI-GL | FI-GL-GL-N-2CL |
| SAP_CA_BC_IC_LND_FIN_GLA_PC | G/L Account Master Data - Configuration | OB_GLACC_F01 |  | SKBD | Not Used G/L Account Company Code Assignments |  | FI-GL | FI-GL-GL-N-2CL |
| SAP_CA_BC_IC_LND_FIN_GLA_PC | G/L Account Master Data - Configuration | OB_GLACC_F01 |  | GL_ACCOUNT | G/L Account Master Data |  | FI-GL | FI-GL-GL-N-2CL |
| SAP_CA_BC_IC_LND_FIN_CJ0_PC | Cash Journal - Configuration | FBCJC5 |  | V_TCJ_NUMB_GROUP | Define Numbering Groups |  | FI-BL | FI-BL-PT-CJ-2CL |
| SAP_FIN_BC_AR_DP_SETTINGS_PC | Accounts Receivable - Digital Payments Settings | FDP3 | FDP3_TRAN | FINS_AR_DP_TAXCODE | Maintain Tax Codes for Posting Charges | 102593 | FI-AR-AR | FIN-FSCM-DP-DP-2CL |
| SAP_FIN_BC_AR_DP_SETTINGS_PC | Accounts Receivable - Digital Payments Settings | FDP1 | FDP1_TRAN | FINS_AR_DP_ACT | Activate SAP Digital Payments Add-On | 102562 | FI-AR-AR | FIN-FSCM-DP-DP-2CL |
| SAP_CA_BC_IC_LND_UOM_PC | Units of Measurement - Configuration | CUNI |  | SIMG_CFMENUOLMSOMSC | Check Units of Measurement | 102179 | BC-SRV-ASF-UOM | BC-SRV-ASF-UOM |
| SAP_CA_BC_IC_LND_UOM_PC | Units of Measurement - Configuration | CUNI |  | SIMG_CFMENUOLMSOMSC | Check Units of Measurement | 102179 | BC-SRV-ASF-UOM | BC-SRV-ASF-UOM |
| SAP_CA_BC_IC_LND_PP_MRP_PC | Material Requirements Planning - Configuration | OMI4 | OMI4_TRAN | SIMG_CFMENUOPP1OMI4 | Check Lot-Sizing Procedure | 101112 | PP-FIO-MRP | PP-MRP-BD-2CL |
| SAP_CA_BC_IC_LND_PP_MRP_PC | Material Requirements Planning - Configuration | OMDW | OMDW_TRAN | SIMG_CFMENUOPP1OMDW | Define Rescheduling Check for Plant | 102658 | PP-FIO-MRP | PP-MRP-BD-2CL |
| SAP_CA_BC_IC_LND_FIN_GL1_PC | Chart of Accounts - Configuration | OB53 |  | SIMG_CFMENUORFBOB53 | Define Retained Earnings Account | 100297 | FI-GL | FI-AR-AR-2CL |
| SAP_CA_BC_IC_LND_SD0_PC | Sales - Configuration | VN01 |  | SIMG_CFMENUOLSDVN01 | Define Number Ranges for Sales Documents | 102819 | SD-SLS | SD-CAS-BD-2CL |
| SAP_CA_BC_IC_LND_SD0_PC | Sales - Configuration | POC_O2C_AUART |  | POC_O2C_AUART | Maintain Order Types for Performance Monitoring | 103273 | SD-SLS | CA-EPT-POC |
| SAP_CA_BC_IC_LND_SD0_PC | Sales - Configuration | V/14 |  | SIMG_CMMENUOLSDFKM | Define Dependencies Of Revenue Account Determination |  | SD-SLS | SD-BF-ACT-2CL |
| SAP_CA_BC_IC_LND_SD0_PC | Sales - Configuration | V/13 |  | SIMG_CMMENUOLSDFKM | Define Dependencies Of Revenue Account Determination |  | SD-SLS | SD-BF-ACT-2CL |
| SAP_CA_BC_IC_LND_SD0_PC | Sales - Configuration | V/12 |  | SIMG_CMMENUOLSDFKM | Define Dependencies Of Revenue Account Determination |  | SD-SLS | SD-BF-ACT-2CL |
| SAP_CA_BC_IC_LND_SD0_PC | Sales - Configuration | V_TVLP_VUV |  | SIMG_CFMENUOLSDUVSZ | Assign Incompleteness Procedures | 101190 101191 | SD-SLS | SD-CAS-BD-2CL |
| SAP_CA_BC_IC_LND_SD0_PC | Sales - Configuration | V_TVLK_VUV |  | SIMG_CFMENUOLSDUVSZ | Assign Incompleteness Procedures | 101190 101191 | SD-SLS | SD-CAS-BD-2CL |
| SAP_CA_BC_IC_LND_PP_REM_PC | Repetitive Manufacturing - Configuration | OP58 |  | SIMG_CFMENUOLPSOP58 | Define Routing Profiles with Default Values | 102528 | PP-FIO-SFC | PP-BD-RTG-2CL |
| SAP_CA_BC_IC_LND_FIN_AR0_PC | Accounts Receivable - Configuration | FBMP |  | SIMG_CFMENUORFBFBMP | Define Dunning Procedures | 102302 | FI-AR-AR | FI-AR-AR-C-2CL |
| SAP_CA_BC_IC_LND_FIN_AR0_PC | Accounts Receivable - Configuration | FBMP |  | SIMG_CFMENUORFBFBMP | Define Dunning Procedures | 102302 | FI-AR-AR | FI-AR-AR-C-2CL |
| SAP_CA_BC_IC_LND_FIN_AR0_PC | Accounts Receivable - Configuration | FBMP |  | SIMG_CFMENUORFBFBMP | Define Dunning Procedures | 102302 | FI-AR-AR | FI-AR-AR-C-2CL |
| SAP_CA_BC_IC_LND_FIN_AR0_PC | Accounts Receivable - Configuration | MFD_F7519 |  | MFD_F7519 | Map Format Data for Direct Debit Mandate Instructions | 170015 | FI-AR-AR | CA-GTF-CSC-DME |
| SAP_CA_BC_IC_LND_FIN_AR0_PC | Accounts Receivable - Configuration | MFD_F7519 |  | MFD_F7519 | Map Format Data for Direct Debit Mandate Instructions | 170015 | FI-AR-AR | CA-GTF-CSC-DME |
| SAP_CA_BC_IC_LND_FIN_AR0_PC | Accounts Receivable - Configuration | MFD_F7519 |  | MFD_F7519 | Map Format Data for Direct Debit Mandate Instructions | 170015 | FI-AR-AR | CA-GTF-CSC-DME |
| SAP_CA_BC_IC_LND_FIN_AR0_PC | Accounts Receivable - Configuration | TMDIR |  | V_T056P | Maintain Reference Interest Rate Values |  | FI-AR-AR | CA-FIM-FMA |
| SAP_CA_BC_IC_LND_FIN_AR0_PC | Accounts Receivable - Configuration | TMDIR |  | V_T056P | Maintain Reference Interest Rate Values |  | FI-AR-AR | CA-FIM-FMA |
| SAP_CA_BC_IC_LND_FIN_AP0_PC | Accounts Payable - Configuration | MFD_F2685A |  | MFD_F2685A | Map Format Data for Payments | 100558 | FI-AP-AP | CA-GTF-CSC-DME |
| SAP_CA_BC_IC_LND_FIN_CS0_PC | Consolidation - Configuration | CX1I4 | CX1I4_TRAN | SIMG_CFMENUCX01_MD3C | Define Breakdown Categories | 106346 | FIN-CS | FIN-CS-MD-2CL |
| SAP_CA_BC_IC_LND_FIN_CS0_PC | Consolidation - Configuration | CX1S4 | CX1S4_TRAN | SIMG_CFMENUCX01_MD31 | Define Subitem Categories and Subitems |  | FIN-CS | EC-CS |
| SAP_CA_BC_IC_LND_FIN_CS0_PC | Consolidation - Configuration | CXL2 | CXL2_TRAN | SIMG_CFMENUCX01CXL1C | Define Consolidation Ledgers | 101010 | FIN-CS | FIN-CS-2CL |
| SAP_CA_BC_IC_LND_FIN_JVA_PC | Joint Venture Accounting - Configuration | GJ85_J9O |  | SIMG_GJ85_J9O | Catastrophe Overhead Offset Account | 100297 | CA-JVA | CA-JVA |
| SAP_CA_BC_IC_LND_FIN_JVA_PC | Joint Venture Accounting - Configuration | GJ85_JPA |  | SIMG_GJ85_JPA | Payroll Burden Clearing Adjustment | 100297 | CA-JVA | CA-JVA |
| SAP_CA_BC_IC_LND_FIN_JVA_PC | Joint Venture Accounting - Configuration | GJ85_JIO |  | SIMG_GJ85_JIO | International Overhead Offset Account | 100297 | CA-JVA | CA-JVA |
| SAP_CA_BC_IC_LND_FIN_JVA_PC | Joint Venture Accounting - Configuration | GJ85_J7O |  | SIMG_GJ85_J7O | Exploration Overhead Offset Account | 100297 | CA-JVA | CA-JVA |
| SAP_CA_BC_IC_LND_FIN_JVA_PC | Joint Venture Accounting - Configuration | GJ85_J7E |  | SIMG_GJ85_J7E | Exploration Overhead Expense Account | 100297 | CA-JVA | CA-JVA |
| SAP_CA_BC_IC_LND_FIN_JVA_PC | Joint Venture Accounting - Configuration | GJ85_JPE |  | SIMG_GJ85_JPE | Payroll Burden Clearing Expense Account | 100297 | CA-JVA | CA-JVA |
| SAP_CA_BC_IC_LND_FIN_JVA_PC | Joint Venture Accounting - Configuration | GJ85_J9E |  | SIMG_GJ85_J9E | Catastrophe Overhead Expense Account | 100297 | CA-JVA | CA-JVA |
| SAP_CA_BC_IC_LND_FIN_JVA_PC | Joint Venture Accounting - Configuration | GJ85_J8E |  | SIMG_GJ85_J8E | Capital Drilling Overhead Expense - Can. | 100297 | CA-JVA | CA-JVA |
| SAP_CA_BC_IC_LND_FIN_JVA_PC | Joint Venture Accounting - Configuration | GJ85_J6O |  | SIMG_GJ85_J6O | Construction Overhead Offset Account | 100297 | CA-JVA | CA-JVA |
| SAP_CA_BC_IC_LND_FIN_JVA_PC | Joint Venture Accounting - Configuration | GJ85_J6E |  | SIMG_GJ85_J6E | Construction Overhead Expense Account | 100297 | CA-JVA | CA-JVA |
| SAP_CA_BC_IC_LND_FIN_JVA_PC | Joint Venture Accounting - Configuration | GJ83_JVB |  | SIMG_GJ83_JVB | Cutback Tax Suspense Gross | 100297 | CA-JVA | CA-JVA |
| SAP_CA_BC_IC_LND_FIN_JVA_PC | Joint Venture Accounting - Configuration | GJ83_JV7 |  | SIMG_GJ83_JV7 | Interest Charged in JV Bank Transfers | 100297 | CA-JVA | CA-JVA |
| SAP_CA_BC_IC_LND_FIN_JVA_PC | Joint Venture Accounting - Configuration | GJ83_JV6 |  | SIMG_GJ83_JV6 | Interventure Account for Balanced BbV | 100297 | CA-JVA | CA-JVA |
| SAP_CA_BC_IC_LND_FIN_JVA_PC | Joint Venture Accounting - Configuration | GJ83_JV5 |  | SIMG_GJ83_JV5 | Misc. Income Holding for Net Profit Int. | 100297 | CA-JVA | CA-JVA |
| SAP_CA_BC_IC_LND_FIN_JVA_PC | Joint Venture Accounting - Configuration | GJ83_JV4 |  | SIMG_GJ83_JV4 | Net Expense Account for Net Profit Int. | 100297 | CA-JVA | CA-JVA |
| SAP_CA_BC_IC_LND_FIN_JVA_PC | Joint Venture Accounting - Configuration | GJ83_JV3 |  | SIMG_GJ83_JV3 | Misc. Income for Net Profit Interests | 100297 | CA-JVA | CA-JVA |
| SAP_CA_BC_IC_LND_FIN_JVA_PC | Joint Venture Accounting - Configuration | GJ83_JV2 |  | SIMG_GJ83_JV2 | Non-Op Billing: Acct for Document Split | 100297 | CA-JVA | CA-JVA |
| SAP_CA_BC_IC_LND_FIN_JVA_PC | Joint Venture Accounting - Configuration | GJ83_JV1 |  | SIMG_GJ83_JV1 | Cutback - Tax Clearing Account | 100297 | CA-JVA | CA-JVA |
| SAP_CA_BC_IC_LND_FIN_JVA_PC | Joint Venture Accounting - Configuration | GJ85_J1O |  | SIMG_GJ85_J1O | % Prod. (U.S.), % (Can.) Overhead Offset | 100297 | CA-JVA | CA-JVA |
| SAP_CA_BC_IC_LND_FIN_JVA_PC | Joint Venture Accounting - Configuration | GJ85_J1E |  | SIMG_GJ85_J1E | % Prod. (U.S.), % (Can.) Overhead Exp. | 100297 | CA-JVA | CA-JVA |
| SAP_CA_BC_IC_LND_FIN_JVA_PC | Joint Venture Accounting - Configuration | GJ83_JVX |  | SIMG_GJ83_JVX | JV Exchange Rate Differences | 100297 | CA-JVA | CA-JVA |
| SAP_CA_BC_IC_LND_FIN_JVA_PC | Joint Venture Accounting - Configuration | GJ83_JVE |  | SIMG_GJ83_JVE | Funding Write-Off | 100297 | CA-JVA | CA-JVA |
| SAP_CA_BC_IC_LND_FIN_JVA_PC | Joint Venture Accounting - Configuration | GJ83_JVC |  | SIMG_GJ83_JVC | Offset Acct Equity Change - Adjustment | 100297 | CA-JVA | CA-JVA |
| SAP_CA_BC_IC_LND_FIN_JVA_PC | Joint Venture Accounting - Configuration | GJ83_JVA |  | SIMG_GJ83_JVA | Cutback Tax Expense Account | 100297 | CA-JVA | CA-JVA |
| SAP_CA_BC_IC_LND_FIN_JVA_PC | Joint Venture Accounting - Configuration | GJ83_JV8 |  | SIMG_GJ83_JV8 | GR/IR Shadow Account | 100297 | CA-JVA | CA-JVA |
| SAP_CA_BC_IC_LND_FIN_JVA_PC | Joint Venture Accounting - Configuration | GJ85_J3E |  | SIMG_GJ85_J3E | CFR Prod. (U.S.) Overhead Expense | 100297 | CA-JVA | CA-JVA |
| SAP_CA_BC_IC_LND_FIN_JVA_PC | Joint Venture Accounting - Configuration | GJ85_J2O |  | SIMG_GJ85_J2O | % Development (U.S.) Overhead Offset | 100297 | CA-JVA | CA-JVA |
| SAP_CA_BC_IC_LND_FIN_JVA_PC | Joint Venture Accounting - Configuration | GJ85_J2E |  | SIMG_GJ85_J2E | % Development (U.S) Overhead Expense | 100297 | CA-JVA | CA-JVA |
| SAP_CA_BC_IC_LND_FIN_JVA_PC | Joint Venture Accounting - Configuration | GJ85_J4O |  | SIMG_GJ85_J4O | CFR Drilling (U.S) Overhead Offset Acct | 100297 | CA-JVA | CA-JVA |
| SAP_CA_BC_IC_LND_FIN_JVA_PC | Joint Venture Accounting - Configuration | GJ85_J4E |  | SIMG_GJ85_J4E | CFR Drilling (U.S) Overhead Expense | 100297 | CA-JVA | CA-JVA |
| SAP_CA_BC_IC_LND_FIN_JVA_PC | Joint Venture Accounting - Configuration | GJ85_J3O |  | SIMG_GJ85_J3O | CFR Prod. (U.S.) Overhead Offset Acct | 100297 | CA-JVA | CA-JVA |
| SAP_CA_BC_IC_LND_FIN_JVA_PC | Joint Venture Accounting - Configuration | GJ85_JPO |  | SIMG_GJ85_JPO | Payroll Burden Clearing Offset Account | 100297 | CA-JVA | CA-JVA |
| SAP_CA_BC_IC_LND_FIN_JVA_PC | Joint Venture Accounting - Configuration | GJ85_JIE |  | SIMG_GJ85_JIE | International Overhead Expense Account | 100297 | CA-JVA | CA-JVA |
| SAP_CA_BC_IC_LND_FIN_JVA_PC | Joint Venture Accounting - Configuration | GJ85_J8O |  | SIMG_GJ85_J8O | Capital Drilling Overhead Offset - Canada | 100297 | CA-JVA | CA-JVA |
| SAP_CA_BC_IC_LND_FIN_JVA_PC | Joint Venture Accounting - Configuration | GJ83_JVD |  | SIMG_GJ83_JVD | Funding Corp.Pay Actualization | 100297 | CA-JVA | CA-JVA |
| SAP_CA_BC_IC_LND_FIN_BA0_PC | Bank Accounting - Configuration | MFD_F5608 |  | MFD_F5608 | Map Format Data for Incoming Files from Banks | 170010 | FI-BL | CA-GTF-CSC-DME |
| SAP_CA_BC_IC_LND_CMD_PRD_PC | Central Master Data Product - Configuration | OMT4 |  | SIMG_CFMENUOLMSOMT4 | Define Attributes of System Messages | 103090 | LO-MD-MM | LO-MD-MM-2CL |
| SAP_CA_BC_IC_LND_CMD_PRD_PC | Central Master Data Product - Configuration | OS26 |  | SIMG_CFMENUOLPSOS26 | Define Laboratory/Design Office | 103123 | LO-MD-MM | PP-BD-RTG-2CL |
| SAP_CA_BC_IC_LND_FIN_INT_PC | Finance Integration - Configuration | FDP3 | FDP3_TRAN | FINS_AR_DP_TAXCODE | Maintain Tax Codes for Posting Charges | 102593 | FI-AR-AR | FIN-FSCM-DP-DP-2CL |
| SAP_CA_BC_IC_LND_FIN_INT_PC | Finance Integration - Configuration | FDP1 | FDP1_TRAN | FINS_AR_DP_ACT | Activate SAP Digital Payments Add-On | 102562 | FI-AR-AR | FIN-FSCM-DP-DP-2CL |
| SAP_CA_BC_IC_LND_MM_IM0_PC | Inventory Management - Configuration | OMJ_EXPIRATION_CHECK |  | SIMG_V_156_MHD_SSCUI | Set Expiration Date Check | 101913 | MM-IM-IAM | MM-IM-GF-2CL |
| SAP_CA_BC_IC_LND_MM_IM0_PC | Inventory Management - Configuration | OMB_STORE_LOC_AUTO |  | SIMG_V_156_X_SSCUI | Create Storage Location Automatically | 101914 | MM-IM-IAM | MM-IM-GF-2CL |
| SAP_CA_BC_IC_LND_MM_IM0_PC | Inventory Management - Configuration | OMB_REASON_CODE |  | SIMG_V157D_SSCUI | Reason for Movement | 101091 | MM-IM-IAM | MM-IM-GF-2CL |
| SAP_CA_BC_IC_LND_MM_IM0_PC | Inventory Management - Configuration | OMB_CONTROL_REASON |  | SIMG_V_156_G_SSCUI | Control: Reason for Movement | 103222 | MM-IM-IAM | MM-IM-GF-2CL |
| SAP_CA_BC_IC_LND_SD1_PC | Sales - Cross-Client Configuration | V/03 |  | V_03 | Create Condition Tables for Pricing in Sales | 103119 | SD-SLS | SD-MD-CM-2CL |
| SAP_CA_BC_IC_LND_SD1_PC | Sales - Cross-Client Configuration | V/05 |  | V_05 | Display Condition Tables for Pricing in Sales |  | SD-SLS | SD-MD-CM-2CL |
| SAP_CA_BC_IC_LND_SD1_PC | Sales - Cross-Client Configuration | V/04 |  | V_04 | Change Condition Tables for Pricing in Sales | 103120 | SD-SLS | SD-MD-CM-2CL |
| SAP_CA_BC_IC_LND_FIN_GL_RS_PC | General Ledger for Serbia - Configuration | GLO_TRANS_DATE | GLO_TRANS_DATE_TRAN | GLO_V_TRANS_DATE | Define Currency Translation Date | 106806 | FI-LOC-FI-RS | FI-LOC-GEN |
| SAP_CA_BC_IC_LND_FIN_GL_RS_PC | General Ledger for Serbia - Configuration | GLO_TRANS_DATE | GLO_TRANS_DATE_TRAN | GLO_V_TRANS_DATE | Define Currency Translation Date | 106806 | FI-LOC-FI-RS | FI-LOC-GEN |
| SAP_CA_BC_IC_LND_EWM_DSP_PC | Warehouse Management - Configuration Display | /SCWM/0DSTGRP |  | /SCWM/V_T340DA | Define Number Ranges |  | SCM-EWM-AUT | SCM-EWM-CFG-2CL |
| SAP_CA_BC_IC_LND_EWM_DSP_PC | Warehouse Management - Configuration Display | /SCWM/0DSTGRP |  | /SCWM/V_T340DA | Define Number Ranges |  | SCM-EWM-AUT | SCM-EWM-CFG-2CL |
| SAP_CA_BC_IC_LND_PRC_DSP_PC | Procurement - Configuration Display | OMRA |  | SIMG_CFMENUOLMROMRA | Define Subsequent Debit/Credit Key f. Order History Category |  | MM-PUR-IAM | MM-IV-LIV-2CL |
| SAP_CA_BC_IC_LND_FIN_EPC_PC | Third-Party Payment - Configuration | MFD_F9009 |  | MFD_F9009 | Map Format Data for Third-Party Payment |  | FI-LOC-IAM | CA-GTF-CSC-DME |
| SAP_CA_BC_IC_LND_RFM_DSP_PC | Retail and Fashion Management - Configuration Display | V_TWZLA |  | W_ZF_ST_0350 | Structured Material in Logistics Process | 107393 | LO-RFM | LO-RFM-MD-ART-2CL |
| SAP_CA_BC_IC_LND_PRD_DSP_PC | Settings for Product Cost Accounting - Display Configuration | OPL1 |  | SIMG_CFMENUORKKOPL1 | Check Costing Variants for Manufacturing Orders (PP) |  | CO-PC-OBJ | CO-PC-OBJ-2CL |
| SAP_CA_BC_IC_LND_PRD_DSP_PC | Settings for Product Cost Accounting - Display Configuration | OPL1 |  | SIMG_CFMENUORKKOPL1 | Check Costing Variants for Manufacturing Orders (PP) |  | CO-PC-OBJ | CO-PC-OBJ-2CL |

### Sheet: 61

| Expert Configuration: Define Tax Code Russia |  |
| --- | --- |
| Last Update: September 9, 2026 |  |
|  | Road Map Viewer - SAP for Me |
|  | Expert Configuration for Tax Code accelerator (SAP Activate) |

### Sheet: 73

| Expert Configuration: Define Country Code Kosovo (Iso Code XK) |  |  |
| --- | --- | --- |
| Last Update: September 9, 2026 |  |  |
|  | REMARK: The values you see in this tempalte are FIXED and cannot be adjusted/changed in this Expert Configuration. It only provides this feature for 'Kosovo' and NO other country is supported. |  |
|  | Field Name (Country Specifics) |  |
|  | Country: | XK |
|  | Name: | Kosovo |
|  | Description(long): | Kosovo |
|  | Nationality: | Kosovar |
|  | Nationality (long): | Kosovar |
|  | Vehicle Country key: | RKS |
|  | ISO code: | XK |
|  | ISO code 3 char: | XKX |
|  | Date format: | DD.MM.YYYY |
|  | Dec. Format: | 1.234.567,89 |
|  | Time Format: | 24 Hour Format |
|  | Field Name (Country Codes) | Value |
|  | Ctry: | XK |
|  | Tel.from: | 00 |
|  | Tel. to | 383 |
|  | Digit del. | 0 |
|  | TLX fr. | <EMPTY> |
|  | Telex to | 621 |

### Sheet: 5D2_7DM

| Expert Configuration: Assign Transit Plant to Company Code<br>Related Scope Items 5D2, 7DM |  |  |
| --- | --- | --- |
| Last Update: August 28, 2026 |  |  |
| To Assign Transit Plant to Company Code create an incident: |  |  |
| Subject: ‘ Assign Transit Plant to Company Code’ |  |  |
| Component: XX-S4C-OPR-SRV |  |  |
| Please provide the following information and attach this xls to the incident. |  |  |
| Adjust the following default values to your requirements: |  |  |
| 1. Assign Transit Plant to Company Code |  |  |
|  | Company Code | Transit Plant |
|  | 1010 | 1010 |
|  | 1710 | 1710 |

### Sheet: J87

| Expert Configuration: Define Prefixes for EANs/UPCs |  |  |  |  |
| --- | --- | --- | --- | --- |
| Last Update: September 09, 2026 |  |  |  |  |
|  | To add EAN prefix please create an incident: |  |  |  |
|  | Subject: ‘Define Prefixes for EANs/UPCs’ |  |  |  |
|  | Component: XX-S4C-OPR-SRV |  |  |  |
|  | Please provide the following information to the incident: |  |  |  |
| Please fill in the below template for the countries you would like to add EAN prefixes , also maintain the description in the logon language |  |  |  |  |
|  | Prefix<br>(maximum length allowed is 3 numerical digits) | Description of Prefix<br>(EN - default system language) | Additional Language (only if you require) |  |
|  |  |  | Language (indicate the additional language you required Description of Prefix) | Description of Prefix<br>(in the additional language) |
| e.g. | 20 | Internal numbering | DE | Interne Nummerierung |
| * Deletion not supported via the pre-approved expert configuration – for deletion please reach out to your SAP customer/partner facing role. |  |  |  |  |
| ** Only creation of new Prefix is allowed, edit/change option for the existing data via the pre-approved expert configuration is not allowed - for changing existing data please contact your SAP customer/partner facing role. |  |  |  |  |

### Sheet: 4KL

| Expert Configuration: Define Material Groups |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| Last Update: September 9, 2026 |  |  |  |  |  |
|  | To delete Material Groups created by customer please create an incident: |  |  |  |  |
|  | Subject: ‘Delete Material Groups’ |  |  |  |  |
|  | Component: XX-S4C-OPR-SRV |  |  |  |  |
|  | Please provide the following information to the incident. |  |  |  |  |
| Please fill in the below template only with Customer created Material Groups that you would like to delete. |  |  |  |  |  |
|  | Material Group | Material Group Description<br>(EN - default system language) | Authorization Group (AGrp) | Default unit of weight in the material master | Description 2 of the Material Group |
| e.g. | ZASP | Plastics |  |  | A001 material |
| *Please confirm in the ticket, that the material groups you want to be deleted, are not used in any of your systems. |  |  |  |  |  |
| ** If used, Customer has to delete the references and re-submit the request |  |  |  |  |  |
| ***Deletion of customer created material groups is supported via the pre-approved expert configuration. |  |  |  |  |  |
| ****Deletion of material groups delivered as part of Standard Best Practice pre-delivered content is not supported, for more details please contact your SAP customer/partner facing role. |  |  |  |  |  |

### Sheet: 699

| Expert Configuration: Delete Queues |  |  |
| --- | --- | --- |
| Last Update: January 29, 2026 |  |  |
| If customer is already live with production data, as a general rule we do NOT perform expert configuration. Please align with product team about further processing. |  |  |
| To perform Expert Configuration for Delete Queues please create incidents as per below: |  |  |
| For 3SL System: open incident for Development and Production |  |  |
| For 2SL System: open incident for Test and Production |  |  |
| Subject: ‘Delete Queues’ |  |  |
| Component: XX-S4C-OPR-SRV |  |  |
| Please provide the following information to the incidents: |  |  |
| Please confirm the following: |  |  |
| Has the storage type been released to production system? | Yes |  |
|  | No | X |
| Actions to be executed by the Customer in advance |  | Confirm |
| The entries in SSCUI "Define Queues", "Define Queue Determination Criteria" node refer to the queue to be deleted. <br>If there are entries in the "Define Queue Determination Criteria" node, please check all the entries, which entries are to be deleted and which entries are updated with other queue. |  | X |
| The entries in SSCUI "Define Queues", "Define Queues for Physical Inventory" node refer to the queue to be deleted. <br>If there are entries in the "Define Queues for Physical Inventory" node, please check all the entries, which entries are to be deleted and which entries updated with other queue. |  | X |
| Is there a warehouse order refer to the queue that is planned to be deleted?<br>If there are open warehouse orders or in-process warehouse orders, please update to other queues which are NOT planned to be deleted or left queue empty, using transaction "/SCWM/TO_CONF" (Fiori app "Confirm Warehouse Tasks - Advanced") |  | X |
| Is there a resource refer to the queue that is planned to be deleted? <br>Please update the entries in Fiori app "Maintain Resources" with empty queue or another queue. |  | X |
| Is there queue sequence refer to the queue that is planned to be deleted? Please update the entries in Fiori app "Define Queue Sequence" with another queue or delete it. |  | X |
| Please provide the entries to be deleted: |  |  |
| The entries to be deleted in SSCUI "Define Queues" - "Define Queues" node | Warehouse Number | Queue |
|  | e.g.1050 | e.g. ZO-001 |

### Sheet: 983

| Expert Configuration: Maintain External Material Groups |  |  |
| --- | --- | --- |
| Last Update: January 29, 2026 |  |  |
|  | To delete External Material Groups created by customer please create an incident: |  |
|  | Subject: ‘Delete External Material Groups’ |  |
|  | Component: XX-S4C-OPR-SRV |  |
|  | Please provide the following information to the incident. |  |
| Please fill in the below template only with Customer created External Material Groups that you would like to delete. |  |  |
|  | External Material Group | External material grp. Description<br>(EN - default system language) |
| e.g. | ZASP | Plastics |
| *Please confirm in the ticket, that the material groups you want to be deleted, are not used in the system. |  |  |
| **Deletion of customer created external material groups is supported via the pre-approved expert configuration. |  |  |

### Sheet: J90

| Expert Configuration: Request Currency Codes |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Last Update: January 29, 2026 |  |  |  |  |  |  |  |  |  |
| With S/4HANA Cloud currency codes and the related settings are provided by default. |  |  |  |  |  |  |  |  |  |
| There are a few currency codes few customers have asked for and we consider that other customers may also ask for them. |  |  |  |  |  |  |  |  |  |
| We do not plan to add them to the standard content as only few customers need them. |  |  |  |  |  |  |  |  |  |
| We only provide ISO 4217 currency codes. |  |  | ISO 4217 - Wikipedia |  |  |  |  |  |  |
| Before you ask for the new following codes you have to acknowledge that you have read the note 137626 - Information about codes, and that you accept the risks mentioned in the note. |  |  |  |  |  |  |  |  |  |
| You can via Pre-approved Expert Configuration ask for the following ISO codes to be added. |  |  |  |  |  |  |  |  |  |
| You can ask for adjusted settings, but only for decimals points. |  |  |  |  |  |  |  |  |  |
| Code | Long Text | Short Text | Decimal Points | ISO | Primary | Alternative Key | Valid until | Comment | Note |
| XAG | Silver | Silver | 3 | XAG |  | 961 |  | Silver (one troy ounce) | 137626 - FAQ: Decimal Places for Currency Codes |
| XAU | Gold | Gold | 3 | XAU |  | 959 |  | Gold (one troy ounce) | 137626 - FAQ: Decimal Places for Currency Codes |
| XPD | Palladium | Palladium | 3 | XPD |  | 964 |  | Palladium (one troy ounce) | 137626 - FAQ: Decimal Places for Currency Codes |
| XPT | Platinum | Platinum | 3 | XPT |  | 962 |  | Platinum (one troy ounce) | 137626 - FAQ: Decimal Places for Currency Codes |
| XDR | Special drawing rights | Spl. Drw. Right |  | XDR |  | 960 |  | IMF special drawing rights | 137626 - FAQ: Decimal Places for Currency Codes |
| It is common for banks to offer bank accounts using the currency code CNH. CNH is CNY circulating outside of China and can be traded in off-shore FX market, mainly in Hongkong and Singapore. |  |  |  |  |  |  |  |  |  |
| CNH is only used in off-shore financial market and is known mainly by financial professionals while CNY as main currency code are widely used in global trade. |  |  |  |  |  |  |  |  |  |
| Before you ask for the CNH currency you have to acknowledge that you have read the note 3390994 - Information about CNH, and that you accept the risks mentioned in the note. |  |  |  |  |  |  |  |  |  |
| You can via Pre-approved Expert Configuration ask for CNH as non-ISO code to be added. |  |  |  |  |  |  |  |  |  |
| You can ask for adjusted settings, but only for decimals points. |  |  |  |  |  |  |  |  |  |
| Code | Long Text | Short Text | Decimal Points | ISO | Primary | Alternative Key | Valid until | Comment | Note |
| CNH | Renminbi (offshore) | Renminbi-offsh. | 2 | CNY |  | 156 |  | Read the following note: | 3390994 - Information about CNH. |
| CNY | Chinese Yuan Renminbi | Renminbi | 2 | CNY |  | 156 |  | The existing entry for CNY will be marked as "Primary" |  |
| If you consider having other settings for the codes listed above, please contact your SAP customer facing role or any SAP individual with a similar role. |  |  |  |  |  |  |  |  |  |
| For 3SL System: open incident for Development |  |  |  |  |  |  |  |  |  |
| For 2SL System: open incident for Test |  |  |  |  |  |  |  |  |  |
| Subject: ‘Request Currency Codes’ |  |  |  |  |  |  |  |  |  |
| Component: XX-S4C-OPR-SRV |  |  |  |  |  |  |  |  |  |
| Please provide the following information: |  |  |  |  |  |  |  |  |  |
| Delete the lines that do not apply for your request. |  |  |  |  |  |  |  |  |  |
|  | Requested currency codes: |  |  |  |  |  |  |  |  |
|  | Code | Fill in the decimals points (between 0 and 5) |  |  |  |  |  |  |  |
|  | XAG |  |  |  |  |  |  |  |  |
|  | XAU |  |  |  |  |  |  |  |  |
|  | XPD |  |  |  |  |  |  |  |  |
|  | XPT |  |  |  |  |  |  |  |  |
|  | XDR |  |  |  |  |  |  |  |  |
|  | CNH |  |  |  |  |  |  |  |  |
|  | I have read and accepted the risks mentioned in note 3390994 regarding CNH code |  |  |  |  | YES |  |  |  |
|  | I have read and accepted the risks mentioned in SAP note 137626 and I confirm that once the decimal points are configured, they cannot be modified or edited later. |  |  |  |  | YES |  |  |  |

### Sheet: DPK

|  |  | Expert Configuration For Depreciation Keys |
| --- | --- | --- |
| 1 | If the depreciation key is requested as per a legal requirement please open a customer case on the localization relevant component |  |
|  | Subject: New Depreciation Keys - legal requirement |  |
|  | Component: FI-LOC-CNT-** (**= Two letters for abreviation of the country) |  |
|  | Priority: Medium |  |
| 2 | In SAP S/4HANA Cloud Public Edition 2608, SAP provides configurable depreciation profiles that replace the previously predefined depreciation keys |  |
|  | If you are interested in the new depreciation profile feature, see the detailed information on the SAP Help Portal: |  |
|  | What's New information:  Introduction of Configurable Depreciation Profiles \| SAP Help Portal |  |
|  | Transition from Depreciation Keys to Depreciation Profiles \| SAP Help Portal |  |
|  | If you have decided to become a pilot customer, create a separate support case to ask SAP to activate the depreciation profile feature. |  |
|  | For the support case, you should use the following parameters: |  |
|  | Subject: Request for Depreciation Profiles |  |
|  | Component: FI-AA-AA |  |
|  | Priority: Medium |  |
| 3 | If the requested depreciation key is for customer specific process open a customer case for Expert Configuration Team. |  |
|  | Please create an SAP incident with the following information and include the template from the link below, completed with all required data. |  |
|  | Subject: Expert Configuration - Depreciation Keys |  |
|  | Component: XX-S4C-OPR-SRV |  |
|  | Priority: Medium |  |
|  | Depreciation key - Template DPK |  |
|  | IMPORTANT CONSTRAINTS FOR EXPERT CONFIGURATION OF DEPRECIATION KEYS: Non-compliance with these restrictions will result in case closure. |  |
|  | • This service represents an additional optional offer without SLA to be applied, thus priority is to be medium or lower.<br>• SAP allows Expert configuration for Depreciation Keys only for CBC customers. Solution Builder requests will be rejected.<br>• SAP does not allow the creation of new customer depreciation keys for CLT countries.<br>• The pre-approved expert configuration for depreciation keys is not supported in the parallel line. If additional depreciation keys are needed, it must be requested and implemented in the main line before starting the branch process.<br>• Customer-specific depreciation keys must be defined exclusively using the fields available in the template. No changes to fields outside the template is allowed (e.g.Cutoff Value Key).<br>• Changes to SAP standard delivered depreciation keys are not allowed.<br>• SAP does not provide consulting services for the creation of these keys. Customers should contact their internal SAP Advisors/ Partners when completing the template. |  |

### Sheet: REV

| Expert Configuration: Activation of Index Type “Replacement Value, Monthly” |  |  |
| --- | --- | --- |
| Last Update: January 29, 2026 |  |  |
|  | IMPORTANT:<br>SAP allows expert configuration for activation of Index Type “Replacement Value, Monthly” for CBC customers but not those using Solution Builder.<br>SAP does not allow activation of the Index Type “Replacement Value, Monthly” for other valuation views besides the country specific valuation views for Argentina and Chile. Activation for IFRS or USGAAP valuation view is not allowed.<br>Prior to activation of Index Type “Replacement Value, Monthly”, customers needs to understand that every asset using this Index Type will be impacted by the new calculation logic. Additionally, depreciation recalculation will need to be done in all affected systems. Customers must confirm in writing that they understand the far-reaching impacts and agree to complete depreciation recalculation in all affected systems. |  |
| 1 | To activate Periodic Asset Revaluation with Index Type “Replacement Value, Monthly” please create an incident: |  |
|  | Subject: Activation of Index Type “Replacement Value, Monthly” |  |
|  | Component: FI-LOC-FI-** (**= Two letters for abreviation of the country - only AR-Argentina and CL-Chile is allowed) |  |
|  | Priority: Medium |  |
|  | Prerequisites - Please include this required information in the incident to SAP | I have read and accepted the pre-requisites information. (Type YES or NO to each statement). |
|  | If you are requesting an activation of the Asset revaluation with the Index Type “Replacement Value, Monthly” you acknowledge it is allowed only for countries Argentina and Chile. | » type here your reply: YES or NO. |
|  | No derived depreciation area is defined in accounting principle. | » type here your reply: YES or NO. |
|  | The valuation views which are requested for activation of Index Type “Replacement Value, Monthly” are assigned to depreciation areas. | » type here your reply: YES or NO. |
|  | Index type “Replacement Value, Monthly” cannot be activated if there is any revaluation posted (annual revaluation, manual, etc.) | » type here your reply: YES or NO. |
|  | Functionality cannot be deactivated once it is activated | » type here your reply: YES or NO. |
|  | Index Type “Replacement Value, Monthly” can be activated only for country specific valuation views: 0AR_0001, 0AR_0015, 0CL_0001, 0CL_0015 | » type here your reply: YES or NO. |
|  | Do you understand that activation of the Index Type “Replacement Value, Monthly” will impact ALL assets using such Index in all systems. | » type here your reply: YES or NO. |
|  | ***Please be informed that you are responsible for the activation of Index Type “Replacement Value, Monthly” for the valuation views you have defined. |  |
|  | Please fill with "X" in the column RV: Dsplit in the below template only for the Valuation Views for which you would like to activate the usage of Index Type “Replacement Value, Monthly”. |  |
|  | Valuation view | RV: Dsplit |
|  | 0AR_0001 |  |
|  | 0AR_0015 |  |
|  | 0CL_0001 |  |
|  | 0CL_0015 |  |
| 2 | After the initial check by the Localization team, your request will be handed over to Expert Configuration team. |  |
|  | The Expert Configuration team will activate the depreciation split (only for those marked as "X" above), which enables you to assign the Index Type “Replacement Value, Monthly”. |  |

### Sheet: ABCOI

| Expert Configuration: Enablement of Activity-based Consolidation of Investment |  |  |
| --- | --- | --- |
| Last Update: January 29, 2026 |  |  |
|  | To enable Activity-Based Consolidation of Investment please create an incident: |  |
|  | Subject: Activation of Activity-based Consolidation of Investment |  |
|  | Component: XX-S4C-OPR-SRV |  |
|  | By using activity-based consolidation of investments (ABCOI), you accept that there are no functional improvements planned for the near- / mid future, i.e. you fully accept the current functional scope of ABCOI. |  |
|  | Please provide the following information to the incident: |  |
|  | Version/Time Period |  |
|  | Version | Y10 |
|  | Fiscal Year | current year |
|  | Period | 12 |
|  | Cons. COA | Y1 |
|  | Following standard values will be maintained (provided for information only) |  |
|  | Short Text | CoI |
|  | Medium Text | Cons. of Invest. (Act.-Based) |
|  | Maintain Text in other language | » type here your reply: YES or NO. |
|  | *If "Yes", specify the language, if “No,” skip this section of the template |  |
|  | These field are standard values for this activity (no change possible) |  |
|  | Task | 2101 |
|  | Document Type | 3B |

### Sheet: 519

| Expert Configuration: Delete Storage Type With Template |  |  |  |
| --- | --- | --- | --- |
| Last Update: September 9, 2026 |  |  |  |
| If customer is already live with production data, as a general rule we do NOT perform expert configuration.<br>If you have postings in the Production System please contact your SAP customer/partner facing role about further processing. |  |  |  |
| To perform Expert Configuration for Maintain Storage Types please create an incident: |  |  |  |
| Subject: "Delete Storage Type With Template" |  |  |  |
| Component: XX-S4C-OPR-SRV |  |  |  |
| Please provide the following information to the incident. |  |  |  |
| Please confirm: |  |  |  |
| Is the storage type has been released to production system? | » type here your reply: YES or NO. |  |  |
| Actions to be executed by the Customer in advance |  |  | Confirm |
| Check Storage bins referring the storage type to be deleted |  |  | » type here your reply: YES or NO. |
| The referring storage bins are deleted via /SCWM/LS11" transaction (Fiori app "Mass Edit Storage Bins" |  |  | » type here your reply: YES or NO. |
| In case of stock left in the storage bins that need to be deleted - this is moved to another bin using the "/SCWM/MONNAV_CR_HUWT" transaction (Fiori app "Create HU Warehouse Tasks") or the "/SCWM/MONNAV_CR_P_WT" transaction (Fiori app "Create Product Warehouse Tasks"). |  |  | » type here your reply: YES or NO. |
| The entries to be deleted in SSCUI "Create Storage Types Using Templates" | Warehouse Number | Storage Type Search Sequence | Sequence Number |
|  | e.g. 1050 | e.g ZST1 | e.g. 1 |

### Sheet: 619

| Expert Configuration: Delete Storage Type Without Template |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Last Update: September 9, 2026 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| If customer is already live with production data, as a general rule we do NOT perform expert configuration.<br>If you have postings in the Production System please contact your SAP customer/partner facing role about further processing. |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| To perform Expert Configuration for Maintain Storage Types please create an incident: |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Subject: "Delete Storage Type Without Template" |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Component: XX-S4C-OPR-SRV |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Please provide the following information to the incident. |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Please confirm: |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Is the storage type has been released to production system? | » type here your reply: YES or NO. |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Actions to be executed by the Customer in advance |  |  | Confirm |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Check Storage bins referring the storage type to be deleted |  |  | » type here your reply: YES or NO. |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| The referring storage bins are deleted via /SCWM/LS11" transaction (Fiori app "Mass Edit Storage Bins" |  |  | » type here your reply: YES or NO. |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| In case of stock left in the storage bins that need to be deleted - this is moved to another bin using the "/SCWM/MONNAV_CR_HUWT" transaction (Fiori app "Create HU Warehouse Tasks") or the "/SCWM/MONNAV_CR_P_WT" transaction (Fiori app "Create Product Warehouse Tasks"). |  |  | » type here your reply: YES or NO. |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Entries to be deleted in SSCUI "Maintain Storage Types" | Warehouse Number | Storage Type Search Sequence | Sequence Number |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  | e.g. 1050 | e.g ZST1 | e.g. 1 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Other custom settings related to the storage type that need to be deleted | SCCUI |  | Warehouse Number |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  | "Assign Storage Types to Storage Type Search Sequence" |  | e.g. 1050 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  | "Assign Storage Bins to Activity Areas" |  | e.g. 1050 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| DEPENDENCIES - please fill in all the data you need to deleted: |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Delete Entries of "Assign Storage Types to Storage Type Search Sequence" | SSCUI 104732 | Warehouse Number | Storage Type Search Sequence | Sequence Number | Storage Type | Storage Type Group | Description |  |  |  |  |  |  |  |  |  |  |  |
| Delete Entries of "Assign Storage Bins to Activity Areas" | SSCUI 104436 | Warehouse Number | Activity Area | Sequence Number | Storage Type | Aisle Start | Aisle Start | Stack Start | Stack End | Level Start | Level End | Bin Section Start | Bin Section End | Consolidation Group | Intermediate Storage Type | Intermediate Storage Section | Intermediate Storage Bin |  |
| Delete Entries of "Specify Storage Type Search Sequence for Putaway" | SSCUI 104733 | Warehouse Number | Putaway Control | Warehouse Process Type/Group | Quantity Classification | Stock Type | Type | Usage | Storage Type Search Sequence | Putaway Rules |  |  |  |  |  |  |  |  |
| Delete Entries of "Determine Storage Type Search Sequence for Stock Removal | SSCUI 104685 | Warehouse Number | Stock Removal Control | Warehouse Process Type/Group | Quantity Classification | Stock Type | Type | Usage | Storage Type Search Sequence | Stock Removal Rule |  |  |  |  |  |  |  |  |
| Delete Entries of "Specify Storage Type Search Sequence - Assign Storage Types to Storage Type Search Sequence" | SSCUI 104732 | Warehouse Number | Storage Type Search Sequence | Description | Sequence Number | Storage Type | Storage Type Group | Stock on Transportation Unit |  |  |  |  |  |  |  |  |  |  |
| Delete Entries of “Specify Storage Type Search Sequence" | SSCUI 104683 | Warehouse Number | Storage Type Search Sequence | Description |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Delete Entries of "Define Storage Type Search Sequence for Putaway" | SSCUI 104731 | Warehouse Number | Storage Type Search Sequence | Description |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Delete Entries of "Define Sort Sequence for Activity Area" | SSCUI 104437 | Warehouse Number | Activity Area | Activity | Sequence Number | Storage Type | Sort Sequence | Sort Direction: Aisle | Sort Direction for Stack | Path Direction: Stack | Sort Direction Level | Path Direction Level | Sort Direction: Bid Subdivision | Path Direction: Bid Subdivision | Picking Mode | Fixed Sorting |  |  |
| Delete Entries of "Define Search Sequence of Creation Rules for Activity Areas" | SSCUI 104759 | Warehouse Number | Activity Area | Activity | Sequence Number | WO Creation Rule | Description |  |  |  |  |  |  |  |  |  |  |  |
| Delete Entries of "Define Physical Inventory Area" | SCCUI 102621 | Warehouse Number | Activity Area | Putaway Physical Inventory | Low Stock Check with Physical Inventory | Low Stock Check | Tolerance Check with Low Stock Check | Posting After Count Entry | Proposed Quantity at Time of Count Entry | No Automatic Check | Disp.Item Object at Time of Count Entry | "HU Complete" Allowed | HU Counting Method | Print Item Objects | Quantity Threshhold Value | Completeness Check Onl./Offl. | Serial Number for Count | No Default Stock Type |
| Delete Entries of "Define Activity Area" | SSCUI 104435 | Warehouse Number | Activity Area | Description | Activity Areas Joined |  |  |  |  |  |  |  |  |  |  |  |  |  |

### Sheet: SLoc

| Expert Configuration: Deprecation of STORAGE LOCATIONS (SLoc) |  |  |  |
| --- | --- | --- | --- |
| Last Update: September 10, 2026 |  |  |  |
| To perform Expert Configuration for Deprecation of Storage Locations please create an incident: |  |  |  |
| Subject: "Deprecate Storage Location" |  |  |  |
| Component: XX-S4C-OPR-SRV |  |  |  |
| Please provide the following information to the incident. |  |  |  |
| Actions to be executed by the Customer in advance (Mandatory Pre-requisites) |  |  | Confirm |
| All the in-transit documents related to the Storage Locations need to be closed. Otherwise, which error will show in deprecation. What steps should be done for the clean-up. |  |  | » type here your reply: YES or NO. |
| All the related material stock needs to be cleared. Otherwise, which error will show in deprecation. What steps should be done for the clean-up. |  |  | » type here your reply: YES or NO. |
| All the related material needs to set Material for Deletion flag for Storage Location level. Otherwise, which error will show in deprecation. What steps should be done for the clean-up. |  |  | » type here your reply: YES or NO. |
| The Storage location must not be referenced by any Kanban Control cycle or Handling Unit |  |  | » type here your reply: YES or NO. |
| The Storage location must not be referenced in any QM customizing, Inspection Lots, Material Samples, Quality Notifications or Defects |  |  | » type here your reply: YES or NO. |
| All tasks must be done in all systems (Productive, Test, Development) |  |  | » type here your reply: YES or NO. |
| Storage locations, which are not marked for deletion (field Flag Material for Deletion at Storage Location Level (LVORM)) in the table Storage Location Data for Material (MARD) cannot be deprecated. |  |  | » type here your reply: YES or NO. |
| Check whether table Storage Location Data for Material (MARD) can be marked for deletion in the product master Fiori app. |  |  | » type here your reply: YES or NO. |
| When checking with F1595 it is important to explicitly select Stocks with Zero (You may create a Stock relevant entry but never post or create one a cancel all postings). In addition, it important that users have the appropriate authorization to display stock quantities in the respective plant. |  |  | » type here your reply: YES or NO. |
| Please provide the entries to be deprecated: |  |  |  |
| Plant | Storage Location | Warehouse relationship (if any) |  |

### Sheet: 3BR

| Expert Configuration: Delete Storage Location and Warehouse Relation |  |
| --- | --- |
| Last Update: September 10, 2026 |  |
| To perform Expert Configuration for Delete Storage Location and Warehouse Relation please create an incident: |  |
| Subject: "Delete Storage Location and Warehouse Relation" |  |
| Component: XX-S4C-OPR-SRV |  |
| Please provide the following information to the incident. |  |
| Please provide the entries to be deleted: |  |
| Warehouse Number | Storage Location |

### Sheet: SPL

| Expert Configuration: Define Split Clearing Account SPL |  |
| --- | --- |
| Last Update: September 10, 2026 |  |
| To perform Define Split Clearing Account SPL please create an incident: |  |
| Subject: "‘Split Clearing Account SPL India" |  |
| Component: XX-S4C-OPR-SRV |  |
| Please provide the following information to the incident. |  |
| Actions to be executed by the Customer in advance (Mandatory Pre-requisites) | Confirm |
| Company code is configured in Country India | » type here your reply: YES or NO. |
| Chart of accounts is assigned to the company code | » type here your reply: YES or NO. |
| Relevant G/L accounts must already exist in the chart of accounts (FS00/GL master) | » type here your reply: YES or NO. |
| Customer must explicitly provide the G/L account and <br>create it in the system on YCOA, as a pre-requisite. | Action |
| Please specify the G/L Account to be used for this configuration. | » type here your reply: GL a/c reference |

*Empty sheets: Doc. Info*

## Connections
- part-of :: [[_cluster]]
- related-to :: [[01-solution-foundation-and-platform/sscui-list-en-xx-sap-s-4hana-cloud-2608-configuration-2-part-39]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Configuration/SSCUI_List_EN_XX.xlsm` — lines 12532–13731 of the extracted text · extracted with `xlsx2md` · 9,788,312 chars in the whole document
