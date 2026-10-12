---
id: 01-solution-foundation-and-platform/sscui-list-en-xx-sap-s-4hana-cloud-2608-configuration-2-part-38
title: SSCUI List EN XX (SAP S/4HANA Cloud 2608 Configuration) (SSCUI_List_EN_XX) — part 38 of 40
description: "SAP S/4HANA Cloud 2608 SSCUI list workbook; this slice maps business catalogs and transaction codes to IMG activities, SSCUI IDs and components."
cluster: 01-solution-foundation-and-platform
tags: [kb/solution-foundation-and-platform, topic/sscui-configuration-activity-list]
aliases: []
keywords: [Self-Service Configuration (SSCUI) Activity List, business catalog mapping, transaction code mapping, sscui ids, img activities, joint venture accounting, consolidation configuration, accounts payable configuration, inventory management configuration, plm system integration]
sources: ["raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Configuration/SSCUI_List_EN_XX.xlsm#lines-10035-11300"]
confidence: high
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-2
topic: 01-solution-foundation-and-platform/sscui-configuration-activity-list
language: EN
part: 38/40
created: 2026-10-12
updated: 2026-10-12
---

# SSCUI List EN XX (SAP S/4HANA Cloud 2608 Configuration) (SSCUI_List_EN_XX) — part 38 of 40

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Configuration/SSCUI_List_EN_XX.xlsm`, part 38 of 40 (lines 10035–11300 of the extracted text), extracted with `xlsx2md`. Grouped under **Self-Service Configuration (SSCUI) Activity List** in Solution Foundation and Platform. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

| SAP_CORE_BC_BCT_TRN_REL_PC | Business Configuration - Transport Release Management | F7042 | F7042_TRAN |  |  |  | BC-CUS-TOL-CTO |  |
| SAP_CA_BC_TAX_CURR_SET_PC | Tax - Current Settings | F3899 | F3899_TRAN |  |  |  | FI-GL |  |
| SAP_CA_BC_TAX_CURR_SET_PC | Tax - Current Settings | ETAX_CONFIG_CHECK | ETAX_CONFIG_CHECK_TRAN |  |  |  | FI-GL |  |
| SAP_CA_BC_TAX_CURR_SET_PC | Tax - Current Settings | S_ALR_87003632 | S_ALR_87003632_TRAN | SIMG_CFORFBOBWZ | Define Number Ranges for Withholding Tax | 104786 | FI-GL | FI-AR-AR-2CL |
| SAP_CA_BC_TAX_CURR_SET_PC | Tax - Current Settings | S_ER9_11001535 | S_ER9_11001535_TRAN | VC_FOT_TXA_ACT | Activate RITA and Maintain Tax Registration Countries/Regions | 103464 | FI-GL | FI-GL-GL-F-2CL |
| SAP_CA_BC_TAX_CURR_SET_PC | Tax - Current Settings | S_ER9_11001292 | S_ER9_11001292_TRAN | V_FOT_TDT_MIGSTS | Maintain Migration Status for Time-Dependent Taxes | 103140 | FI-GL | FI-GL-GL-F-2CL |
| SAP_CA_BC_TAX_CURR_SET_PC | Tax - Current Settings | OBWZ |  | SIMG_CFORFBOBWZ | Define Number Ranges for Withholding Tax | 104786 | FI-GL | FI-AR-AR-2CL |
| SAP_CA_BC_TAX_CURR_SET_PC | Tax - Current Settings | S_ALR_87012365 | S_ALR_87012365_TRAN |  |  |  | FI-GL |  |
| SAP_CA_BC_TAX_CURR_SET_PC | Tax - Current Settings | TAX_RATE_TRANS | TAX_RATE_TRANS_TRAN |  |  |  | FI-GL |  |
| SAP_CA_BC_IC_LND_FIN_AA_SK_PC | Asset Accounting for Slovakia - Configuration | S_ER9_11001470 | S_ER9_11001470_TRAN | V_GLOFAASKNCLCOD | Define National Classification Code (Slovakia) | 103425 | FI-LOC-FI-SK | FI-LOC-AA-SK |
| SAP_CA_BC_IC_LND_BNS_ARB_PC | Ariba Integration - Configuration | S_ER9_52003791 | S_ER9_52003791_TRAN | ARBS4_V_POTX_CND | Maintenance View for Tax Conditions Details | 105920 | MM-PUR-IAM | BNS-ARI-CI-S4-MM |
| SAP_CA_BC_IC_LND_BNS_ARB_PC | Ariba Integration - Configuration | S_ER9_52001601 | S_ER9_52001601_TRAN | ARBS4_V_EDI_CTRL | Settings for Parking of Supplier Invoices | 103263 | MM-PUR-IAM | BNS-ARI-CI-S4 |
| SAP_CA_BC_IC_LND_BNS_ARB_PC | Ariba Integration - Configuration | S_ER9_52003320 | S_ER9_52003320_TRAN | ARBS4_V_CC_INVC | Settings for Tax Code to Tax Category for CC Invoices | 105699 | MM-PUR-IAM | BNS-ARI-CI-S4 |
| SAP_CA_BC_IC_LND_FIN_SRF2_PC | Statutory Reporting (Cross Country) - Configuration | S_ER9_11001598 | S_ER9_11001598_TRAN | V_RAT_COEF | Define Pro Rata Coefficients | 103619 | FI-LOC-IAM | FI-LOC-RAT |
| SAP_CA_BC_IC_LND_FIN_SRF2_PC | Statutory Reporting (Cross Country) - Configuration | S_ER9_11002117 | S_ER9_11002117_TRAN | V_RAT_COEF_FINAL | Define Final Pro Rata Coefficient for Year-End Adjustment | 105523 | FI-LOC-IAM | FI-LOC-RAT |
| SAP_CA_BC_IC_LND_FIN_PA0_PC | Revenue Recognition - Configuration | S_ER9_11001915 | S_ER9_11001915_TRAN | FINS_TRR_DRK_PC | Derivation of Recognition Key for Provider Contracts | 105138 | CO-PC-OBJ-EBR | CO-PC-OBJ-EBR-2CL |
| SAP_CA_BC_IC_LND_FIN_PA0_PC | Revenue Recognition - Configuration | S_ER9_11000209 | S_ER9_11000209_TRAN | FINS_TRR | Maintain Settings for Event-Based Revenue Recognition | 102530 | CO-PC-OBJ-EBR | CO-PC-OBJ-EBR-2CL |
| SAP_CA_BC_IC_LND_FIN_PA0_PC | Revenue Recognition - Configuration | S_ER9_11000350 | S_ER9_11000350_TRAN | FINS_TRR_DRAKEY | Derivation of Recognition Key for Projects | 102517 | CO-PC-OBJ-EBR | CO-PC-OBJ-EBR-2CL |
| SAP_CA_BC_IC_LND_FIN_PA0_PC | Revenue Recognition - Configuration | S_ER9_11001818 | S_ER9_11001818_TRAN | FINS_TRR_REP | Define Replacement Rules of Recognition Keys | 104054 | CO-PC-OBJ-EBR | CO-PC-OBJ-EBR-2CL |
| SAP_CA_BC_IC_LND_FIN_PA0_PC | Revenue Recognition - Configuration | S_ER9_11001323 | S_ER9_11001323_TRAN | FINS_TRR_DRK_SFS | Derivation of Recognition Key for Sell from Stock | 103198 | CO-PC-OBJ-EBR | CO-PC-OBJ-EBR-2CL |
| SAP_CA_BC_IC_LND_FIN_PA0_PC | Revenue Recognition - Configuration | S_ER9_11001107 | S_ER9_11001107_TRAN | FINS_TRR_DRK_CRM | Derivation of Recognition Key for Service Documents | 102968 | CO-PC-OBJ-EBR | CO-PC-OBJ-EBR-2CL |
| SAP_CA_BC_IC_LND_FIN_AP0_PC | Accounts Payable - Configuration | S_ER9_11000871 | S_ER9_11000871_TRAN | V_FAP_T076I | Assign G/L Accounts | 102463 | FI-AP-AP | FI-AP-AP-M-2CL |
| SAP_CA_BC_IC_LND_FIN_AP0_PC | Accounts Payable - Configuration | S_ER9_11000870 | S_ER9_11000870_TRAN | V_FAP_T076S | Make Settings for Posting | 102462 | FI-AP-AP | FI-AP-AP-M-2CL |
| SAP_CA_BC_IC_LND_FIN_AP0_PC | Accounts Payable - Configuration | S_ER9_11000794 | S_ER9_11000794_TRAN | VC_T042ZA_FORMAT | Set Up Payment Medium Formats per Company Code | 102216 | FI-AP-AP | FI-AP-AP-B-2CL |
| SAP_CA_BC_IC_LND_FIN_AP0_PC | Accounts Payable - Configuration | S_ER9_11000868 | S_ER9_11000868_TRAN | V_FAP_IC_AD_GRP | Define Account Determination Groups | 102454 | FI-AP-AP | FI-AP-AP-M-2CL |
| SAP_CA_BC_IC_LND_FIN_AP0_PC | Accounts Payable - Configuration | S_ER9_11000815 | S_ER9_11000815_TRAN | V_DFPAYV_SELVAR | Create/Assign Selection Variants (Alternative) | 102238 | FI-AP-AP | FI-AP-AP-B-2CL |
| SAP_CA_BC_IC_LND_FIN_AP0_PC | Accounts Payable - Configuration | S_ER9_11000869 | S_ER9_11000869_TRAN | V_FAP_IC_ADGRPAS | Assign Sales Organizations | 102455 | FI-AP-AP | FI-AP-AP-M-2CL |
| SAP_CA_BC_IC_LND_FIN_AP0_PC | Accounts Payable - Configuration | S_E91_86000012 | S_E91_86000012_TRAN | SEPA_RC_CUST | Define Reason Code for Status Changes | 101305 | FI-AP-AP | CA-BK-SEP |
| SAP_CA_BC_IC_LND_FIN_AP0_PC | Accounts Payable - Configuration | S_E91_86000011 | S_E91_86000011_TRAN | SEPA_STATUS_CUST | Define Status Changes Not Permitted | 101304 | FI-AP-AP | CA-BK-SEP |
| SAP_CA_BC_IC_LND_FIN_AP0_PC | Accounts Payable - Configuration | S_E91_86000008 | S_E91_86000008_TRAN | SEPA_MND_FM_CUST | Select Function Module for Generation of Mandate IDs | 101047 | FI-AP-AP | CA-BK-SEP-2CL |
| SAP_CA_BC_IC_LND_FIN_AP0_PC | Accounts Payable - Configuration | S_ALR_87100696 | S_ALR_87100696_TRAN | FIAPPY_V_T042F | Define Payment Method Supplements | 102396 | FI-AP-AP | FI-AP-AP-B-2CL |
| SAP_CA_BC_IC_LND_FIN_AP0_PC | Accounts Payable - Configuration | S_ALR_87100690 | S_ALR_87100690_TRAN | FIAPPY_V_T042E | Set Up Payment Methods per Company Code for Payment Transactions | 101044 | FI-AP-AP | FI-AP-AP-B-2CL |
| SAP_CA_BC_IC_LND_FIN_AP0_PC | Accounts Payable - Configuration | S_ALR_87100689 | S_ALR_87100689_TRAN | FIAPPY_V_T042ZL | Set Up Payment Methods for Each Country/Region for Payment Transactions | 101972 | FI-AP-AP | FI-AP-AP-B-2CL |
| SAP_CA_BC_IC_LND_FIN_AP0_PC | Accounts Payable - Configuration | S_ALR_87100688 | S_ALR_87100688_TRAN | FIAPPY_V_T042B | Set Up Paying Company Codes for Payment Transactions | 101001 | FI-AP-AP | FI-AP-AP-B-2CL |
| SAP_CA_BC_IC_LND_FIN_AP0_PC | Accounts Payable - Configuration | S_ER9_11000872 | S_ER9_11000872_TRAN | V_FAP_T076M | Assign Tax Codes | 102464 | FI-AP-AP | FI-AP-AP-M-2CL |
| SAP_CA_BC_IC_LND_FIN_AP0_PC | Accounts Payable - Configuration | S_ALR_87100687 | S_ALR_87100687_TRAN | FIAPPY_V_T042 | Set Up All Company Codes for Payment Transactions | 101293 | FI-AP-AP | FI-AP-AP-B-2CL |
| SAP_CA_BC_IC_LND_FIN_AP0_PC | Accounts Payable - Configuration | S_ALR_87009507 | S_ALR_87009507_TRAN | SIMG_CFMENUORFBOB47 | Define Instruction Keys | 101046 | FI-AP-AP | CA-FS-CVI-2CL |
| SAP_CA_BC_IC_LND_FIN_AP0_PC | Accounts Payable - Configuration | S_ALR_87003288 | S_ALR_87003288_TRAN | SIMG_CFORFBOB27ZMAN | Check Payment Block Reason | 101040 | FI-AP-AP | FI-AP-AP-B-2CL |
| SAP_CA_BC_IC_LND_FIN_AP0_PC | Accounts Payable - Configuration | S_ACR_23000641 | S_ACR_23000641_TRAN | BNK_V_TBNK_CUST_DFLT | Basic Settings for Approval | 101023 | FI-AP-AP | FIN-FSCM-BNK-2CL |
| SAP_CA_BC_IC_LND_FIN_AP0_PC | Accounts Payable - Configuration | SEPA_STATUS_CUST |  | SEPA_STATUS_CUST | Define Status Changes Not Permitted | 101304 | FI-AP-AP | CA-BK-SEP |
| SAP_CA_BC_IC_LND_FIN_AP0_PC | Accounts Payable - Configuration | SEPA_RC_CUST |  | SEPA_RC_CUST | Define Reason Code for Status Changes | 101305 | FI-AP-AP | CA-BK-SEP |
| SAP_CA_BC_IC_LND_FIN_AP0_PC | Accounts Payable - Configuration | SEPA_MND_FM_CUST |  | SEPA_MND_FM_CUST | Select Function Module for Generation of Mandate IDs | 101047 | FI-AP-AP | CA-BK-SEP-2CL |
| SAP_CA_BC_IC_LND_FIN_AP0_PC | Accounts Payable - Configuration | S_ER9_11001586 | S_ER9_11001586_TRAN | V_T042Z_AD | Assign Account Symbol to Payment Methods | 103557 | FI-AP-AP | FI-AP-AP-B-2CL |
| SAP_CA_BC_IC_LND_FIN_AP0_PC | Accounts Payable - Configuration | S_ER9_11001417 | S_ER9_11001417_TRAN | V_FAP_H2R_PM_MAP | Map Payment Methods Between Workforce Integration and SAP S/4HANA Cloud | 103326 | FI-AP-AP | FI-AP-AP-M-2CL |
| SAP_CA_BC_IC_LND_FIN_AP0_PC | Accounts Payable - Configuration | S_ER9_11000938 | S_ER9_11000938_TRAN | VC_TFCUPM042F | Create Payment Medium Formats | 102569 | FI-AP-AP | FI-AP-AP-B-2CL |
| SAP_CA_BC_IC_LND_FIN_AP0_PC | Accounts Payable - Configuration | S_E91_86000010 | S_E91_86000010_TRAN | SEPA_NR_CUST | Assign Number Range Intervals | 102561 | FI-AP-AP | CA-BK-SEP-2CL |
| SAP_CA_BC_IC_LND_FIN_AP0_PC | Accounts Payable - Configuration | S_E4A_94000031 | S_E4A_94000031_TRAN | FI_APAR_SEPA_CUST | General Settings | 103537 | FI-AP-AP | CA-BK-SEP-2CL |
| SAP_CA_BC_IC_LND_FIN_AP0_PC | Accounts Payable - Configuration | S_ALR_87100691 | S_ALR_87100691_TRAN | FIAPPY_VC_BANKDET | Set Up Bank Determination for Payment Transactions | 101045 | FI-AP-AP | FI-AP-AP-B-2CL |
| SAP_CA_BC_IC_LND_FIN_AP0_PC | Accounts Payable - Configuration | S_ALR_87003174 | S_ALR_87003174_TRAN | SIMG_CFMENUORFBOB19 | Define Minority Indicators | 103384 | FI-AP-AP | FI-AP-AP-B-2CL |
| SAP_CA_BC_IC_LND_FIN_AP0_PC | Accounts Payable - Configuration | S_ALR_87003082 | S_ALR_87003082_TRAN | SIMG_XXMENUORFBOBB8 | Maintain Terms of Payment | 102934 | FI-AP-AP | FI-AR-AR-2CL |
| SAP_CA_BC_IC_LND_FIN_AP0_PC | Accounts Payable - Configuration | S_ALR_87001860 | S_ALR_87001860_TRAN | SIMG_CFFIBAT042Y | Define Account Determination for Bank Clearing Accounts | 102803 | FI-AP-AP | FI-AP-AP-B-2CL |
| SAP_CA_BC_IC_LND_FIN_AP0_PC | Accounts Payable - Configuration | S_ALR_87001755 | S_ALR_87001755_TRAN | SIMG_CFFIBAT018V | Define Clearing Accounts for Receiving Bank for Account Transfer | 102802 | FI-AP-AP | FI-AP-AP-B-2CL |
| SAP_CA_BC_IC_LND_FIN_AP0_PC | Accounts Payable - Configuration | SEPA_NR_CUST |  | SEPA_NR_CUST | Assign Number Range Intervals | 102561 | FI-AP-AP | CA-BK-SEP-2CL |
| SAP_CA_BC_IC_LND_FIN_AP0_PC | Accounts Payable - Configuration | OBPM2 | OBPM2_TRAN |  |  |  | FI-AP-AP |  |
| SAP_CA_BC_IC_LND_FIN_AP0_PC | Accounts Payable - Configuration | FI_APAR_SEPA_CUST |  | FI_APAR_SEPA_CUST | General Settings | 103537 | FI-AP-AP | CA-BK-SEP-2CL |
| SAP_CA_BC_IC_LND_FIN_AP0_PC | Accounts Payable - Configuration | S_E91_86000118 | S_E91_86000118_TRAN | IDSAU_CR_V_BR | Specify Supplier Blocking Reason for Expired Certificates | 101232 | FI-AP-AP | FI-LOC-FI-EG |
| SAP_CA_BC_IC_LND_FIN_AP0_PC | Accounts Payable - Configuration | S_E91_86000115 | S_E91_86000115_TRAN | IDSAU_CR_V_C_CR | Define Certificate IDs | 101310 | FI-AP-AP | FI-LOC-FI-EG |
| SAP_CA_BC_IC_LND_FIN_AP0_PC | Accounts Payable - Configuration | S_E91_86000116 | S_E91_86000116_TRAN | IDSAU_CR_V_AS | Assign Certificate IDs | 101231 | FI-AP-AP | FI-LOC-FI-EG |
| SAP_CA_BC_IC_LND_FIN_AP0_PC | Accounts Payable - Configuration | S_E91_86000117 | S_E91_86000117_TRAN | IDSAU_CR_V_C_BLO | Specify Blocking Behavior for Certificates | 101233 | FI-AP-AP | FI-LOC-FI-EG |
| SAP_CA_BC_IC_LND_FIN_AP0_PC | Accounts Payable - Configuration | S_ER9_11000902 | S_ER9_11000902_TRAN | V_ABPAUTH | Specify Optional User Authentication | 102632 | FI-AP-AP | CA-GTF-FXU-FI-AP |
| SAP_CA_BC_IC_LND_FIN_AP0_PC | Accounts Payable - Configuration | S_ER9_11001842 | S_ER9_11001842_TRAN | V_FAP_PP_CAT | Define Payment Plan Categories | 104084 | FI-AP-AP | FI-AP-AP-B-2CL |
| SAP_CA_BC_IC_LND_FIN_AP0_PC | Accounts Payable - Configuration | S_ER9_11001894 | S_ER9_11001894_TRAN | FI_WHT_PB_QA | Specify payment blocks for validation categories | 104350 | FI-AP-AP | FI-LOC-FI-QA |
| SAP_CA_BC_IC_LND_FIN_AP0_PC | Accounts Payable - Configuration | S_ER9_11001846 | S_ER9_11001846_TRAN | FI_WHT_MGC_QA | Specify Service Origin and Withholding Tax Codes for Material Groups | 104295 | FI-AP-AP | FI-LOC-FI-QA |
| SAP_CA_BC_IC_LND_FIN_AP0_PC | Accounts Payable - Configuration | S_ER9_11001991 | S_ER9_11001991_TRAN | VC_FAP_CAL | Define Payment Plan Customized Calendar | 105115 | FI-AP-AP | FI-AP-AP-B-2CL |
| SAP_CA_BC_IC_LND_FIN_AP0_PC | Accounts Payable - Configuration | S_ER9_11001901 | S_ER9_11001901_TRAN | VC_FARP_PAYT_RSN | Define Payment Reasons | 105311 | FI-AP-AP | FI-AP-AP-B-2CL |
| SAP_CA_BC_IC_LND_FIN_AP0_PC | Accounts Payable - Configuration | S_ALR_87100703 | S_ALR_87100703_TRAN | ACAPPY_VC_TFPM042V | Adjust Note to Payee | 102655 | FI-AP-AP | FI-AR-AR-2CL |
| SAP_CA_BC_IC_LND_FIN_AP0_PC | Accounts Payable - Configuration | S_ALR_87002626 | S_ALR_87002626_TRAN | SIMG_CFMENUORFBOBBA | Define Value Date Rules | 105590 | FI-AP-AP | FI-AP-AP-B-2CL |
| SAP_CA_BC_IC_LND_FIN_AP0_PC | Accounts Payable - Configuration | MFD_F2685A |  | MFD_F2685A | Map Format Data for Payments | 100558 | FI-AP-AP | CA-GTF-CSC-DME |
| SAP_CA_BC_IC_LND_FIN_AP0_PC | Accounts Payable - Configuration | S_ER9_11001961 | S_ER9_11001961_TRAN | MFD_F2685A | Map Format Data for Payments | 100558 | FI-AP-AP | CA-GTF-CSC-DME |
| SAP_CA_BC_IC_LND_FIN_AP0_PC | Accounts Payable - Configuration | S_ALR_87002750 | S_ALR_87002750_TRAN | SIMG_CFMENUORFBOBBB | Assign Payment Method to Bank Transaction | 105591 | FI-AP-AP | FI-AP-AP-B-2CL |
| SAP_CA_BC_IC_LND_FIN_AP0_PC | Accounts Payable - Configuration | S_E91_86000004 | S_E91_86000004_TRAN | V_FSEPA_INST_CD | Determine Local Instrument Code and Lead Times | 105971 | FI-AP-AP | CA-BK-SEP-2CL |
| SAP_CA_BC_IC_LND_FIN_AP0_PC | Accounts Payable - Configuration | S_PL0_09000090 | S_PL0_09000090_TRAN | FIBL_V_ATPRA_FI | Define Clearing Accounts for Cross-Country/Region Bank Account Transfers | 105589 | FI-AP-AP | FI-AR-AR-2CL |
| SAP_CA_BC_IC_LND_FIN_AP0_PC | Accounts Payable - Configuration | OY13 |  | V_T005SEPA | Define Settings for SEPA Countries/Regions | 105423 | FI-AP-AP | CA-BK |
| SAP_CA_BC_IC_LND_FIN_AP0_PC | Accounts Payable - Configuration | S_ER9_11000854 | S_ER9_11000854_TRAN | V_T005SEPA | Define Settings for SEPA Countries/Regions | 105423 | FI-AP-AP | CA-BK |
| SAP_CA_BC_IC_LND_FIN_AP0_PC | Accounts Payable - Configuration | FPF_ORDER_NR | FPF_ORDER_NR_TRAN | FPF_ORDER_NR | Define Number Range Intervals for Payables Financing Orders | 106893 | FI-AP-AP | FI-AP-AP-PF-2CL |
| SAP_CA_BC_IC_LND_FIN_AP0_PC | Accounts Payable - Configuration | S_ER1_70001238 | S_ER1_70001238_TRAN | FPF_ORDER_NR | Define Number Range Intervals for Payables Financing Orders | 106893 | FI-AP-AP | FI-AP-AP-PF-2CL |
| SAP_CA_BC_IC_LND_FIN_AP0_PC | Accounts Payable - Configuration | S_ER1_70001237 | S_ER1_70001237_TRAN | V_FPF_ORDER_STTG | Define Default Payment Methods for Virtual Cards | 106892 | FI-AP-AP | FI-AP-AP-PF-2CL |
| SAP_CA_BC_IC_LND_FIN_AP0_PC | Accounts Payable - Configuration | S_ER1_70001371 | S_ER1_70001371_TRAN | V_T100C_GLO_PAYM | Change Message Control - Payments | 106990 | FI-AP-AP | FI-AP-AP-B1 |
| SAP_CA_BC_IC_LND_FIN_AP0_PC | Accounts Payable - Configuration | S_ER1_70001427 | S_ER1_70001427_TRAN | V_T100C_GLO_PAYM | Change Message Control - Payments | 106990 | FI-AP-AP | FI-AP-AP-B1 |
| SAP_CA_BC_IC_LND_FIN_AP0_PC | Accounts Payable - Configuration | S_ER1_70001804 | S_ER1_70001804_TRAN | V_DFPAY_DYN_SEL | Payment Medium Format Variant: Dynamic Selection |  | FI-AP-AP | FI-AP-AP-B-2CL |
| SAP_CA_BC_IC_LND_FIN_AP0_PC | Accounts Payable - Configuration | S_ER1_70001806 | S_ER1_70001806_TRAN | V_DFPAY_XREL | Payment Medium Format: Relation of Field to Format |  | FI-AP-AP | FI-AP-AP-B-2CL |
| SAP_CA_BC_IC_LND_FIN_AP0_PC | Accounts Payable - Configuration | S_ER1_70001968 | S_ER1_70001968_TRAN | V_FAP_BAV_SYS | Maintain Bank Account Validation Settings | 107407 | FI-AP-AP | FI-AP-AP-B-2CL |
| SAP_CA_BC_IC_LND_FIN_AP0_PC | Accounts Payable - Configuration | S_ER1_70001967 | S_ER1_70001967_TRAN | V_FAP_BAV_PRO | Set Up Validation Providers | 107408 | FI-AP-AP | FI-AP-AP-B-2CL |
| SAP_CA_BC_IC_LND_FIN_AP0_PC | Accounts Payable - Configuration | FIPAY_CUST01 | FIPAY_CUST01_TRAN | V_FIPAY_T042_GTS | Activate Check in SAP Global Trade Services for FI Payments | 107387 | FI-AP-AP | FI-AP-AP-B-2CL |
| SAP_CA_BC_IC_LND_FIN_AP0_PC | Accounts Payable - Configuration | S_PR0_40000033 | S_PR0_40000033_TRAN | V_FIPAY_T042_GTS | Activate Check in SAP Global Trade Services for FI Payments | 107387 | FI-AP-AP | FI-AP-AP-B-2CL |
| SAP_CA_BC_IC_LND_FIN_AP0_PC | Accounts Payable - Configuration | DMEEX_TRACE_CLOUD | DMEEX_TRACE_CLOUD_TRAN |  |  |  | FI-AP-AP |  |
| SAP_CA_BC_IC_LND_FIN_AP0_PC | Accounts Payable - Configuration | F2685A | F2685A_TRAN |  |  |  | FI-AP-AP |  |
| SAP_CA_BC_IC_LND_FIN_AP0_PC | Accounts Payable - Configuration | S_ER1_70001742 | S_ER1_70001742_TRAN | SIMG_FPF_CRDMM_STTG | Define Settings for Dynamic Discount Credit Memos | 107204 | FI-AP-AP | FI-AP-AP-PF-2CL |
| SAP_CA_BC_IC_LND_LO_WTY_PC | Warranty Claim - Configuration | S_ER9_52003259 | S_ER9_52003259_TRAN | VC_WTY_RULE_ENG | Maintain Claim Rules | 105967 | LO-WTY | LO-WTY-FIO-2CL |
| SAP_CA_BC_IC_LND_LO_WTY_PC | Warranty Claim - Configuration | S_ER9_52003169 | S_ER9_52003169_TRAN | V_CWTYPR01_CNTRY | Assign Pricing Procedure to Claim Type/Company Code | 105647 | LO-WTY | LO-WTY-FIO-2CL |
| SAP_CA_BC_IC_LND_LO_WTY_PC | Warranty Claim - Configuration | S_ER9_52003870 | S_ER9_52003870_TRAN | VC_WTYA01_C | Define Actions |  | LO-WTY | LO-WTY-FIO-2CL |
| SAP_CA_BC_IC_LND_LO_WTY_PC | Warranty Claim - Configuration | S_ER9_52002692 | S_ER9_52002692_TRAN | V_CWTY001_NR | Assign Number Ranges to Claim Types | 104813 | LO-WTY | LO-WTY-FIO-2CL |
| SAP_CA_BC_IC_LND_LO_WTY_PC | Warranty Claim - Configuration | S_ER9_52003869 | S_ER9_52003869_TRAN | VC_WTYA02_C | Define Action Controls |  | LO-WTY | LO-WTY-FIO-2CL |
| SAP_CA_BC_IC_LND_LO_WTY_PC | Warranty Claim - Configuration | WTYNK | WTYNK_TRAN | WTYNK | Define Number Ranges for Warranty Claims | 104812 | LO-WTY | LO-WTY-FIO-2CL |
| SAP_CA_BC_IC_LND_LO_WTY_PC | Warranty Claim - Configuration | OWTYP21 | OWTYP21_TRAN | SIMG_CFMENUOWTYP21 | Define Condition Types |  | LO-WTY | LO-WTY-FIO-2CL |
| SAP_CA_BC_IC_LND_LO_WTY_PC | Warranty Claim - Configuration | S_KA5_12001031 | S_KA5_12001031_TRAN | WTYNK | Define Number Ranges for Warranty Claims | 104812 | LO-WTY | LO-WTY-FIO-2CL |
| SAP_CA_BC_IC_LND_LO_WTY_PC | Warranty Claim - Configuration | OWTYP11 | OWTYP11_TRAN | SIMG_CFMENUOWTYP11 | Define Access Sequences |  | LO-WTY | LO-WTY-FIO-2CL |
| SAP_CA_BC_IC_LND_LO_WTY_PC | Warranty Claim - Configuration | OWTYP04 | OWTYP04_TRAN | SIMG_CFMENUOWTYP00 | Define Condition Tables |  | LO-WTY | LO-WTY-FIO-2CL |
| SAP_CA_BC_IC_LND_LO_WTY_PC | Warranty Claim - Configuration | OWTYP03 | OWTYP03_TRAN | SIMG_CFMENUOWTYP00 | Define Condition Tables |  | LO-WTY | LO-WTY-FIO-2CL |
| SAP_CA_BC_IC_LND_LO_WTY_PC | Warranty Claim - Configuration | OWTYP02 | OWTYP02_TRAN | SIMG_CFMENUOWTYP00 | Define Condition Tables |  | LO-WTY | LO-WTY-FIO-2CL |
| SAP_CA_BC_IC_LND_LO_WTY_PC | Warranty Claim - Configuration | OWTYP01 | OWTYP01_TRAN | SIMG_CFMENUOWTYP00 | Define Condition Tables |  | LO-WTY | LO-WTY-FIO-2CL |
| SAP_CA_BC_IC_LND_LO_WTY_PC | Warranty Claim - Configuration | OWTYA21 | OWTYA21_TRAN | SIMG_CFMENUOWTYA21 | Define Account Determination Types |  | LO-WTY | LO-WTY-FIO-2CL |
| SAP_CA_BC_IC_LND_LO_WTY_PC | Warranty Claim - Configuration | OWTYA02 | OWTYA02_TRAN | SIMG_CFMENUOWTYA00 | Define Condition Tables |  | LO-WTY | LO-WTY-FIO-2CL |
| SAP_CA_BC_IC_LND_LO_WTY_PC | Warranty Claim - Configuration | OWTYA11 | OWTYA11_TRAN | SIMG_CFMENUOWTYA11 | Define Access Sequences |  | LO-WTY | LO-WTY-FIO-2CL |
| SAP_CA_BC_IC_LND_LO_WTY_PC | Warranty Claim - Configuration | OWTYA03 | OWTYA03_TRAN | SIMG_CFMENUOWTYA00 | Define Condition Tables |  | LO-WTY | LO-WTY-FIO-2CL |
| SAP_CA_BC_IC_LND_LO_WTY_PC | Warranty Claim - Configuration | OWTYA04 | OWTYA04_TRAN | SIMG_CFMENUOWTYA00 | Define Condition Tables |  | LO-WTY | LO-WTY-FIO-2CL |
| SAP_CA_BC_IC_LND_LO_WTY_PC | Warranty Claim - Configuration | OWTYA01 | OWTYA01_TRAN | SIMG_CFMENUOWTYA00 | Define Condition Tables |  | LO-WTY | LO-WTY-FIO-2CL |
| SAP_CA_BC_IC_LND_LO_WTY_PC | Warranty Claim - Configuration | S_KA5_12000989 | S_KA5_12000989_TRAN | SIMG_CFMENUOWTYA51 | Define Account Key |  | LO-WTY | LO-WTY-FIO-2CL |
| SAP_CA_BC_IC_LND_LO_WTY_PC | Warranty Claim - Configuration | S_KA5_12000604 | S_KA5_12000604_TRAN | SIMG_CFMENUOWTYP51 | Restrict Validity of Condition Types |  | LO-WTY | LO-WTY-FIO-2CL |
| SAP_CA_BC_IC_LND_LO_WTY_PC | Warranty Claim - Configuration | S_KA5_12000586 | S_KA5_12000586_TRAN | SIMG_CFMENUOWTYA21 | Define Account Determination Types |  | LO-WTY | LO-WTY-FIO-2CL |
| SAP_CA_BC_IC_LND_LO_WTY_PC | Warranty Claim - Configuration | S_KA5_12000585 | S_KA5_12000585_TRAN | SIMG_CFMENUOWTYA11 | Define Access Sequences |  | LO-WTY | LO-WTY-FIO-2CL |
| SAP_CA_BC_IC_LND_LO_WTY_PC | Warranty Claim - Configuration | S_KA5_12000580 | S_KA5_12000580_TRAN | SIMG_CFMENUOWTYP11 | Define Access Sequences |  | LO-WTY | LO-WTY-FIO-2CL |
| SAP_CA_BC_IC_LND_LO_WTY_PC | Warranty Claim - Configuration | S_KA5_12000581 | S_KA5_12000581_TRAN | SIMG_CFMENUOWTYP21 | Define Condition Types |  | LO-WTY | LO-WTY-FIO-2CL |
| SAP_CA_BC_IC_LND_LO_WTY_PC | Warranty Claim - Configuration | S_KA5_12000584 | S_KA5_12000584_TRAN | SIMG_CFMENUOWTYA00 | Define Condition Tables |  | LO-WTY | LO-WTY-FIO-2CL |
| SAP_CA_BC_IC_LND_LO_WTY_PC | Warranty Claim - Configuration | S_KA5_12000579 | S_KA5_12000579_TRAN | SIMG_CFMENUOWTYP00 | Define Condition Tables |  | LO-WTY | LO-WTY-FIO-2CL |
| SAP_FI_BC_LO_MASSUPLD_PC | Globalization - Mass Upload Utility | F7640 | F7640_TRAN |  |  |  | FI-LOC-LO-IN |  |
| SAP_FI_BC_LO_MASSUPLD_PC | Globalization - Mass Upload Utility | F4383 | F4383_TRAN |  |  |  | FI-LOC-LO-IN |  |
| SAP_CA_BC_IC_LND_FIN_SR_PL_PC | Statutory Reporting for Poland - Configuration | S_ER9_11002079 | S_ER9_11002079_TRAN | FIVC_OFFS_VERS_A_CE | Define Offsetting Account Determination Versions for Several Countries/Rgns | 105370 | FI-LOC-FI-PL | FI-LOC-CF |
| SAP_CA_BC_IC_LND_FIN_SR_PL_PC | Statutory Reporting for Poland - Configuration | S_ER9_11002015 | S_ER9_11002015_TRAN | FIVC_CF_VERSION_ACR | Define Cash Flow Statement Versions for Several Countries/Regions | 105331 | FI-LOC-FI-PL | FI-LOC-CF |
| SAP_CA_BC_IC_LND_FIN_SR_PL_PC | Statutory Reporting for Poland - Configuration | S_ER9_11000939 | S_ER9_11000939_TRAN | IDEU_TAX_MAP | Map Tax Codes to Acquisition Tax Posting Types | 105563 | FI-LOC-FI-PL | FI-LOC-FI |
| SAP_CA_BC_IC_LND_FIN_SR_PL_PC | Statutory Reporting for Poland - Configuration | S_ER9_11001580 | S_ER9_11001580_TRAN | FIPL_VAT_TAXSP | Define Special Mappings for SAF-T Elements | 105415 | FI-LOC-FI-PL | FI-LOC-FI-PL |
| SAP_CA_BC_IC_LND_FIN_SR_PL_PC | Statutory Reporting for Poland - Configuration | S_ER9_11000940 | S_ER9_11000940_TRAN | IDEU_ACCOUNT_MAP | Map G/L Accounts to Acquisition Tax Posting Types | 105564 | FI-LOC-FI-PL | FI-LOC-FI |
| SAP_CA_BC_IC_LND_FIN_SR_PL_PC | Statutory Reporting for Poland - Configuration | S_ER9_11000861 | S_ER9_11000861_TRAN | FIPL_TAXMAP | Map Tax Codes to SAF-T Elements | 105414 | FI-LOC-FI-PL | FI-LOC-FI-PL |
| SAP_CA_BC_IC_LND_FIN_SR_PL_PC | Statutory Reporting for Poland - Configuration | S_ER9_11000936 | S_ER9_11000936_TRAN | SAFT_N_MOV_TYPE_PL | Map Material Movement Types | 102538 | FI-LOC-FI-PL | FI-LOC-FI-PL |
| SAP_CA_BC_IC_LND_FIN_SR_PL_PC | Statutory Reporting for Poland - Configuration | S_ER9_11002335 | S_ER9_11002335_TRAN | FIVC_OFFS_GROUP_DRC | Define Field Sets for Grouping for Several Countries/Regions | 105762 | FI-LOC-FI-PL | FI-LOC-CF |
| SAP_CA_BC_IC_LND_FIN_SR_PL_PC | Statutory Reporting for Poland - Configuration | S_ER9_11002017 | S_ER9_11002017_TRAN | FIVC_OFFS_DET_ACR | Activate Online Offsetting Account Determination for Several Countries/Rgns | 105333 | FI-LOC-FI-PL | FI-LOC-CF |
| SAP_CA_BC_IC_LND_FIN_SR_PL_PC | Statutory Reporting for Poland - Configuration | S_ER9_11002277 | S_ER9_11002277_TRAN | V_IDPL_PP | Define Posting Parameters | 105706 | FI-LOC-FI-PL | FI-LOC-FI-PL |
| SAP_CA_BC_IC_LND_FIN_SR_PL_PC | Statutory Reporting for Poland - Configuration | S_ER9_11002481 | S_ER9_11002481_TRAN | V_100C_IDPLDP | Change Message Control for VAT Validation | 106047 | FI-LOC-FI-PL | FI-LOC-FI-PL |
| SAP_CA_BC_IC_LND_FIN_SR_PL_PC | Statutory Reporting for Poland - Configuration | FIPL_VAT_DISMAP |  | V_SNC_PL_MAP_DIS | Map PL Discount Tag to Pricing Condition | 106709 | FI-LOC-FI-PL | FI-LOC-SAF-PL |
| SAP_CA_BC_IC_LND_FIN_SR_PL_PC | Statutory Reporting for Poland - Configuration | S_ER9_11000862 | S_ER9_11000862_TRAN | FIPL_SAFT_GEN | Define Generic Settings for SAF-T | 102434 | FI-LOC-FI-PL | FI-LOC-FI-PL |
| SAP_CA_BC_IC_LND_FIN_SR_PL_PC | Statutory Reporting for Poland - Configuration | S_ER1_70000848 | S_ER1_70000848_TRAN | V_SNC_PL_MAP_DIS | Map PL Discount Tag to Pricing Condition | 106709 | FI-LOC-FI-PL | FI-LOC-SAF-PL |
| SAP_CA_BC_IC_LND_FIN_SR_PL_PC | Statutory Reporting for Poland - Configuration | S_ER9_11001799 | S_ER9_11001799_TRAN | TAX_FFD_DERIVRUL | Define Derivation Rules for Business Transaction Types | 105884 | FI-LOC-FI-PL | FI-LOC-FI-HU |
| SAP_CA_BC_IC_LND_FIN_SR_PL_PC | Statutory Reporting for Poland - Configuration | FIPL_SAFT_GL |  | V_SNC_PL_GL_XCL | Exclude General Ledger accounts from the Accounting XML file | 106724 | FI-LOC-FI-PL | FI-LOC-SAF-PL |
| SAP_CA_BC_IC_LND_FIN_SR_PL_PC | Statutory Reporting for Poland - Configuration | TAX_FFD_DERIVRUL | TAX_FFD_DERIVRUL_TRAN | TAX_FFD_DERIVRUL | Define Derivation Rules for Business Transaction Types | 105884 | FI-LOC-FI-PL | FI-LOC-FI-HU |
| SAP_CA_BC_IC_LND_FIN_SR_PL_PC | Statutory Reporting for Poland - Configuration | S_ER1_70000895 | S_ER1_70000895_TRAN | V_SNC_PL_GL_XCL | Exclude General Ledger accounts from the Accounting XML file | 106724 | FI-LOC-FI-PL | FI-LOC-SAF-PL |
| SAP_CA_BC_IC_LND_FIN_SR_PL_PC | Statutory Reporting for Poland - Configuration | S_ERX_29000327 | S_ERX_29000327_TRAN | FKKID_GLO_001_V | Define Indicators for Transactions in Contract Accounting | 106928 | FI-LOC-FI-PL | FI-LOC-CA-REP |
| SAP_CA_BC_IC_LND_FIN_SR_PL_PC | Statutory Reporting for Poland - Configuration | SNV_PL_PDTAG |  | SNV_PL_PDTAG | Define Income Tax Tags | 106970 | FI-LOC-FI-PL | FI-LOC-SAF-PL |
| SAP_CA_BC_IC_LND_FIN_SR_PL_PC | Statutory Reporting for Poland - Configuration | SNV_PL_KR_TAG |  | SNV_PL_KR_TAG | Map G/L Accounts to Financial Tags and Income Tax Tags | 106971 | FI-LOC-FI-PL | FI-LOC-SAF-PL |
| SAP_CA_BC_IC_LND_FIN_SR_PL_PC | Statutory Reporting for Poland - Configuration | SNV_PL_FINTAG |  | SNV_PL_FINTAG | Define Financial Tags | 106969 | FI-LOC-FI-PL | FI-LOC-SAF-PL |
| SAP_CA_BC_IC_LND_FIN_SR_PL_PC | Statutory Reporting for Poland - Configuration | S_ER1_70001383 | S_ER1_70001383_TRAN | SNV_PL_KR_TAG | Map G/L Accounts to Financial Tags and Income Tax Tags | 106971 | FI-LOC-FI-PL | FI-LOC-SAF-PL |
| SAP_CA_BC_IC_LND_FIN_SR_PL_PC | Statutory Reporting for Poland - Configuration | S_ER1_70001382 | S_ER1_70001382_TRAN | SNV_PL_PDTAG | Define Income Tax Tags | 106970 | FI-LOC-FI-PL | FI-LOC-SAF-PL |
| SAP_CA_BC_IC_LND_FIN_SR_PL_PC | Statutory Reporting for Poland - Configuration | S_ER9_11001422 | S_ER9_11001422_TRAN | FIWTV_ASGN_KEY | Assign Withholding Tax Key to Withholding Tax Code and Type | 107050 | FI-LOC-FI-PL | FI-AP-AP-Q1 |
| SAP_CA_BC_IC_LND_FIN_SR_PL_PC | Statutory Reporting for Poland - Configuration | S_ER1_70001381 | S_ER1_70001381_TRAN | SNV_PL_FINTAG | Define Financial Tags | 106969 | FI-LOC-FI-PL | FI-LOC-SAF-PL |
| SAP_CA_BC_IC_LND_FIN_SR_PL_PC | Statutory Reporting for Poland - Configuration | S_ER9_11001421 | S_ER9_11001421_TRAN | FIWTV_WHT_KEY | Define Withholding Tax Key and Threshold | 107049 | FI-LOC-FI-PL | FI-AP-AP-Q1 |
| SAP_CA_BC_IC_LND_LE_DL0_PC | Logistics Execution Deliveries - Configuration | S_P00_07000186 | S_P00_07000186_TRAN | SIMG_CFMENUOLSDTVLPB | Define Batch Creation Controls in Inbound Deliveries | 102338 | LE-SHP-IAM | LE-SHP-GF-2CL |
| SAP_CA_BC_IC_LND_LE_DL0_PC | Logistics Execution Deliveries - Configuration | S_ER9_52002499 | S_ER9_52002499_TRAN | LESHP_ENH_REG_NRIV | Define Custom Routines for Flexible Delivery Document Numbering | 104045 | LE-SHP-IAM | LE-SHP-GF-2CL |
| SAP_CA_BC_IC_LND_LE_DL0_PC | Logistics Execution Deliveries - Configuration | S_ER9_52002493 | S_ER9_52002493_TRAN | LESHP_CPFV_PARAMCAT | Define Parameter Catalog for Flexible Delivery Document Numbering | 104041 | LE-SHP-IAM | LE-SHP-GF-2CL |
| SAP_CA_BC_IC_LND_LE_DL0_PC | Logistics Execution Deliveries - Configuration | S_ER9_52002494 | S_ER9_52002494_TRAN | LESHP_CPFVC_FORMULA | Define Formulas for Flexible Delivery Document Numbering | 104042 | LE-SHP-IAM | LE-SHP-GF-2CL |
| SAP_CA_BC_IC_LND_LE_DL0_PC | Logistics Execution Deliveries - Configuration | S_ER9_52002498 | S_ER9_52002498_TRAN | LESHP_V_TVLK_PF | Assign Custom Routines to Delivery Document Types | 104043 | LE-SHP-IAM | LE-SHP-GF-2CL |
| SAP_CA_BC_IC_LND_LE_DL0_PC | Logistics Execution Deliveries - Configuration | S_ER9_52000936 | S_ER9_52000936_TRAN | V_TVLSP | Assign Blocking Reasons to Delivery Types | 102214 | LE-SHP-IAM | LE-SHP-GF-2CL |
| SAP_CA_BC_IC_LND_LE_DL0_PC | Logistics Execution Deliveries - Configuration | S_ER9_52000935 | S_ER9_52000935_TRAN | V_TVLS | Define Reasons for Blocking in Shipping | 102213 | LE-SHP-IAM | LE-SHP-GF-2CL |
| SAP_CA_BC_IC_LND_LE_DL0_PC | Logistics Execution Deliveries - Configuration | S_ALR_87100133 | S_ALR_87100133_TRAN | SIMG_CFMENUOLSDPODAG | Define Reasons for Quantity Differences | 102359 | LE-SHP-IAM | LE-SHP-GF-2CL |
| SAP_CA_BC_IC_LND_LE_DL0_PC | Logistics Execution Deliveries - Configuration | S_ALR_87100132 | S_ALR_87100132_TRAN | SIMG_CFMENUOLSDPODRL | Set POD-Relevance Depending on Delivery Item Category | 101904 | LE-SHP-IAM | LE-SHP-GF-2CL |
| SAP_CA_BC_IC_LND_LE_DL0_PC | Logistics Execution Deliveries - Configuration | S_ALR_87006841 | S_ALR_87006841_TRAN | SIMG_CFMENUOLSD0VSH | Configure Global Shipping Data | 102565 | LE-SHP-IAM | LE-SHP-GF-2CL |
| SAP_CA_BC_IC_LND_LE_DL0_PC | Logistics Execution Deliveries - Configuration | S_ALR_87006724 | S_ALR_87006724_TRAN | SIMG_CFMENUOLSDVN01L | Define Number Ranges for Deliveries | 104047 | LE-SHP-IAM | LE-SHP-GF-2CL |
| SAP_CA_BC_IC_LND_LE_DL0_PC | Logistics Execution Deliveries - Configuration | S_ALR_87006709 | S_ALR_87006709_TRAN | SIMG_CFMENUOLSDVOLB | Define Delivery Item Categories | 102974 | LE-SHP-IAM | LE-SHP-GF-2CL |
| SAP_CA_BC_IC_LND_LE_DL0_PC | Logistics Execution Deliveries - Configuration | S_ALR_87006708 | S_ALR_87006708_TRAN | SIMG_CFMENUOLSDVOLF | Define Delivery Types | 102123 | LE-SHP-IAM | LE-SHP-GF-2CL |
| SAP_CA_BC_IC_LND_LE_DL0_PC | Logistics Execution Deliveries - Configuration | VN01 |  | SIMG_CFMENUOLSDVN01L | Define Number Ranges for Deliveries | 104047 | LE-SHP-IAM | LE-SHP-GF-2CL |
| SAP_CA_BC_IC_LND_LE_DL0_PC | Logistics Execution Deliveries - Configuration | S_ALR_87006586 | S_ALR_87006586_TRAN | SIMG_CFMENUOLSDOVSD | Define Delivery Priorities | 102124 | LE-SHP-IAM | LE-SHP-GF-2CL |
| SAP_CA_BC_IC_LND_LE_DL0_PC | Logistics Execution Deliveries - Configuration | CPF_D01_FORM |  | LESHP_CPFVC_FORMULA | Define Formulas for Flexible Delivery Document Numbering | 104042 | LE-SHP-IAM | LE-SHP-GF-2CL |
| SAP_CA_BC_IC_LND_LE_DL0_PC | Logistics Execution Deliveries - Configuration | CPF_D01_CAT |  | LESHP_CPFV_PARAMCAT | Define Parameter Catalog for Flexible Delivery Document Numbering | 104041 | LE-SHP-IAM | LE-SHP-GF-2CL |
| SAP_CA_BC_IC_LND_LE_DL0_PC | Logistics Execution Deliveries - Configuration | 0VLP |  | SIMG_CFMENUOLSDVOLB | Define Delivery Item Categories | 102974 | LE-SHP-IAM | LE-SHP-GF-2CL |
| SAP_CA_BC_IC_LND_LE_DL0_PC | Logistics Execution Deliveries - Configuration | 0VLK |  | SIMG_CFMENUOLSDVOLF | Define Delivery Types | 102123 | LE-SHP-IAM | LE-SHP-GF-2CL |
| SAP_CA_BC_IC_LND_LE_DL0_PC | Logistics Execution Deliveries - Configuration | S_ER9_52001686 | S_ER9_52001686_TRAN | SDNRRANGEPREFIX | Define Number Range Prefixes for SD Documents | 103283 | LE-SHP-IAM | SD-SLS-GF-CU-2CL |
| SAP_CA_BC_IC_LND_LE_DL0_PC | Logistics Execution Deliveries - Configuration | 0184 |  | SIMG_XXMENUOLSDVOLB | Define Item Category Determination in Deliveries | 105417 | LE-SHP-IAM | LE-SHP-GF-2CL |
| SAP_CA_BC_IC_LND_LE_DL0_PC | Logistics Execution Deliveries - Configuration | S_ALR_87006710 | S_ALR_87006710_TRAN | SIMG_XXMENUOLSDVOLB | Define Item Category Determination in Deliveries | 105417 | LE-SHP-IAM | LE-SHP-GF-2CL |
| SAP_CA_BC_IC_LND_LE_DL0_PC | Logistics Execution Deliveries - Configuration | OVDSP |  | SIMG_CFMENUOLSDOVDSP | Subsequent Delivery Split | 105481 | LE-SHP-IAM | LE-SHP-GF-2CL |
| SAP_CA_BC_IC_LND_LE_DL0_PC | Logistics Execution Deliveries - Configuration | S_ALR_87009595 | S_ALR_87009595_TRAN | SIMG_CFMENUOLSDOVDSP | Subsequent Delivery Split | 105481 | LE-SHP-IAM | LE-SHP-GF-2CL |
| SAP_CA_BC_IC_LND_LE_DL0_PC | Logistics Execution Deliveries - Configuration | OVM1 |  | SIMG_CFMENUOLSDOVM1C | Specify Characteristics for System Messages | 106426 | LE-SHP-IAM | LE-SHP-GF-2CL |
| SAP_CA_BC_IC_LND_LE_DL0_PC | Logistics Execution Deliveries - Configuration | S_ER9_52004313 | S_ER9_52004313_TRAN | SIMG_CFMENUOLSDOVM1C | Specify Characteristics for System Messages | 106426 | LE-SHP-IAM | LE-SHP-GF-2CL |
| SAP_CA_BC_IC_LND_NUM_PC | Number Range Management - Configuration | F4290 | F4290_TRAN |  |  |  | BC-SRV-NUM |  |
| SAP_CA_BC_IC_LND_NUM_PC | Number Range Management - Configuration | SNUM_FIORI | SNUM_FIORI_TRAN | SNUM_FIORI | Edit Number Range Intervals |  | BC-SRV-NUM | BC-SRV-NUM |
| SAP_CA_BC_IC_LND_NUM_PC | Number Range Management - Configuration | S_YI3_39000485 | S_YI3_39000485_TRAN | SNUM_FIORI | Edit Number Range Intervals |  | BC-SRV-NUM | BC-SRV-NUM |
| SAP_CA_BC_GL_COA_CURR_SET_PC | Chart of Accounts - Current Settings | OB_GLACC71 | OB_GLACC71_TRAN |  |  |  | FI-GL |  |
| SAP_CA_BC_IC_LND_FIN_TX_PT_PC | Tax for Portugal - Configuration | FIPT_VAT_VCT |  | FIPT_VAT_VC | Classify Tax Codes for Periodic VAT Return Annexes | 106251 | FI-LOC-FI-PT | FI-LOC-FI-PT |
| SAP_CA_BC_IC_LND_FIN_TX_PT_PC | Tax for Portugal - Configuration | S_ER9_11002587 | S_ER9_11002587_TRAN | FIPT_VAT_VC | Classify Tax Codes for Periodic VAT Return Annexes | 106251 | FI-LOC-FI-PT | FI-LOC-FI-PT |
| SAP_CA_BC_IC_LND_FIN_TX_PT_PC | Tax for Portugal - Configuration | S_ER9_11001784 | S_ER9_11001784_TRAN | FIPT_V_ST_ASSIGN | Assign Stamp Tax Attributes to Tax Codes | 104072 | FI-LOC-FI-PT | FI-LOC-FI-PT |
| SAP_CA_BC_IC_LND_SIT_PC | Situation Handling - Configuration | S_ER1_70001560 | S_ER1_70001560_TRAN | CA_SIT2_AUTH_GRP | Maintain Authorization Groups for Situation Handling | 107070 | CA-SIT | CA-SIT-WB |
| SAP_CA_BC_IC_LND_SIT_PC | Situation Handling - Configuration | CUST_SIT2_AUTH_GRP |  | CA_SIT2_AUTH_GRP | Maintain Authorization Groups for Situation Handling | 107070 | CA-SIT | CA-SIT-WB |
| SAP_CA_BC_IC_LND_SIT_PC | Situation Handling - Configuration | F5437 | F5437_TRAN |  |  |  | CA-SIT |  |
| SAP_CA_BC_IC_LND_SIT_PC | Situation Handling - Configuration | S_ER9_52003005 | S_ER9_52003005_TRAN | CA_SIT2_F5437 | Manage Situation Types - Extended | 170013 | CA-SIT | CA-SIT-ENG |
| SAP_CA_BC_IC_LND_SIT_PC | Situation Handling - Configuration | MST_F5437 |  | CA_SIT2_F5437 | Manage Situation Types - Extended | 170013 | CA-SIT | CA-SIT-ENG |
| SAP_CA_BC_IC_LND_SIT_PC | Situation Handling - Configuration | F5437 | F5437_TRAN |  |  |  | CA-SIT |  |
| SAP_CA_BC_IC_LND_CMD_BP3_PC | Business Partner - Configuration | BPCUST_MULTIADDR_BF |  | BPCUST_MULTIADDR_BF | Activate Multiple Address Handling for Customer Master Data in SAP BP | 105612 | AP-MD-BP | AP-MD-BP |
| SAP_CA_BC_IC_LND_CMD_BP3_PC | Business Partner - Configuration | BUT_DC_CONFIG | BUT_DC_CONFIG_TRAN | VBUT_DC_CONFIG | Manage Data Controller and Purpose Settings for Business Partner | 104809 | AP-MD-BP | AP-MD-BP |
| SAP_CA_BC_IC_LND_CMD_BP3_PC | Business Partner - Configuration | S_SAL_71000069 | S_SAL_71000069_TRAN | BPCUST_MULTIADDR_BF | Activate Multiple Address Handling for Customer Master Data in SAP BP | 105612 | AP-MD-BP | AP-MD-BP |
| SAP_CA_BC_IC_LND_CMD_BP3_PC | Business Partner - Configuration | S_SAL_71000054 | S_SAL_71000054_TRAN | VBUT_DC_CONFIG | Manage Data Controller and Purpose Settings for Business Partner | 104809 | AP-MD-BP | AP-MD-BP |
| SAP_CA_BC_IC_LND_FIN_FARR0_PC | Revenue Accounting - Configuration | FARR_POB_TYPE_SM30 |  | FARR_POB_TYPE | Define Performance Obligation Types | 103886 | FI-RA | FI-RA-2CL |
| SAP_CA_BC_IC_LND_FIN_FARR0_PC | Revenue Accounting - Configuration | S_ER1_70000385 | S_ER1_70000385_TRAN | FARR_ACT_DET_SSCUI | Maintain Account Determination Business Rules | 105701 | FI-RA | FI-RA-2CL |
| SAP_CA_BC_IC_LND_FIN_FARR0_PC | Revenue Accounting - Configuration | FARR_ACT_DET_SSCUI |  | FARR_ACT_DET_SSCUI | Maintain Account Determination Business Rules | 105701 | FI-RA | FI-RA-2CL |
| SAP_CA_BC_IC_LND_FIN_FARR0_PC | Revenue Accounting - Configuration | S_ER1_70000073 | S_ER1_70000073_TRAN | FARR_V_ACPR_CC | Assign Company Code to Accounting Principle | 102675 | FI-RA | FI-RA-2CL |
| SAP_CA_BC_IC_LND_FIN_FARR0_PC | Revenue Accounting - Configuration | S_RGD_01000003 | S_RGD_01000003_TRAN | FARR_POB_TYPE | Define Performance Obligation Types | 103886 | FI-RA | FI-RA-2CL |
| SAP_CA_BC_IC_LND_FIN_FARR0_PC | Revenue Accounting - Configuration | S_ER1_70000386 | S_ER1_70000386_TRAN | FARR_CONT_DET_SSCUI | Maintain Contract Attribute Business Rules | 105700 | FI-RA | FI-RA-2CL |
| SAP_CA_BC_IC_LND_FIN_FARR0_PC | Revenue Accounting - Configuration | FARR_CONT_DET_SSCUI |  | FARR_CONT_DET_SSCUI | Maintain Contract Attribute Business Rules | 105700 | FI-RA | FI-RA-2CL |
| SAP_CA_BC_IC_LND_SLL_SCR_PC | Screening Integration - Configuration | /SAPSLL/70001026 | SAPSLL_70001026_TRAN | /SAPSLL/V_WLSBP | Business Partner Roles for SAP Watchlist Screening | 106809 | FT-ITR-TRC | FT-ITR-TRC |
| SAP_CA_BC_IC_LND_SLL_SCR_PC | Screening Integration - Configuration | /SAPSLL/52000759 | SAPSLL_52000759_TRAN | /SAPSLL/V_ALRWLS | Activate Legal Regulations for SAP Watch List Screening | 101157 | FT-ITR-TRC | FT-ITR-TRC |
| SAP_CA_BC_IC_LND_SLL_SCR_PC | Screening Integration - Configuration | /SAPSLL/70001024 | SAPSLL_70001024_TRAN | /SAPSLL/V_T6GWLS | Watch List Screening: Control Settings for Legal Regulation | 106808 | FT-ITR-TRC | FT-ITR-TRC |
| SAP_CA_BC_IC_LND_FIN_SR_AT_PC | Statutory Reporting for Austria - Configuration | S_EB5_05000419 | S_EB5_05000419_TRAN | FI_TAX_RFD_CHARS | Define Code for Goods and Services for Each VAT Refund Country/Region | 103490 | FI-LOC-FI-AT | FI-GL-GL-F-2CL |
| SAP_CA_BC_IC_LND_FIN_SR_AT_PC | Statutory Reporting for Austria - Configuration | S_EB5_05000420 | S_EB5_05000420_TRAN | FI_TAX_RFD_C_MAP | Assign Code for Goods and Services to a G/L Account | 103492 | FI-LOC-FI-AT | FI-GL-GL-F-2CL |
| SAP_PSM_BC_GM_WRKFLW_PC | Grants Management - Workflow Configuration | F7321 | F7321_TRAN |  |  |  | PSM |  |
| SAP_PSM_BC_GM_WRKFLW_PC | Grants Management - Workflow Configuration | F6588 | F6588_TRAN |  |  |  | PSM |  |
| SAP_FIN_BC_AP_OPER_PC | Accounts Payable - Operational Processing | FIWT_MGRT_WHT_DATE | FIWT_MGRT_WHT_DATE_TRAN |  |  |  | FI-LOC-IAM |  |
| SAP_CA_BC_IC_LND_ARB_PC | Ariba Network Integration - Configuration | S_SAL_71000055 | S_SAL_71000055_TRAN | ARBFND1_MGS | Define Basic Message Settings | 104046 | BNS-INT-FND | BNS-INT-FND |
| SAP_CA_BC_IC_LND_FIN_BP_TH_PC | Business Place for Thailand - Configuration | S_ALR_87001497 | S_ALR_87001497_TRAN | J_1A_ASSIGNMENT_KEYS | Define Assignment Keys | 106580 | FI-LOC-FI-TH | FI-AR-AR-2CL |
| SAP_CA_BC_IC_LND_FIN_BP_TH_PC | Business Place for Thailand - Configuration | S_ALR_87001495 | S_ALR_87001495_TRAN | J_1A_BRA_ASSIGNMENT | Define Branch Assignment for Automatic Postings | 106581 | FI-LOC-FI-TH | FI-AR-AR-2CL |
| SAP_CA_BC_IC_LND_FIN_BP_TH_PC | Business Place for Thailand - Configuration | GLO_DEFINE_BUPLA_TH |  | OFFDOCNO_TH_003 | Define Business Places for Thailand | 105655 | FI-LOC-FI-TH | FI-LOC-FI-TH |
| SAP_CA_BC_IC_LND_FIN_BP_TH_PC | Business Place for Thailand - Configuration | S_AL0_19000046 | S_AL0_19000046_TRAN | OFFDOCNO_TH_003 | Define Business Places for Thailand | 105655 | FI-LOC-FI-TH | FI-LOC-FI-TH |
| SAP_FIN_BC_SRF_TASK_CLEAN_PC | Statutory Reporting - Clean Up Reporting Tasks | SRF_TASK_CLEANER | SRF_TASK_CLEANER_TRAN | SRF_RPG_ENTITY_CLEAN | Clean Up Reporting Tasks | 103124 | FI-LOC-IAM | FI-LOC-SRF-RUN |
| SAP_FIN_BC_SRF_TASK_CLEAN_PC | Statutory Reporting - Clean Up Reporting Tasks | S_ER9_52001512 | S_ER9_52001512_TRAN | SRF_RPG_ENTITY_CLEAN | Clean Up Reporting Tasks | 103124 | FI-LOC-IAM | FI-LOC-SRF-RUN |
| SAP_CA_BC_IC_LND_GEN_DPP_PC | Data Privacy Extractor - Configuration | S_KIW_52000032 | S_KIW_52000032_TRAN | FD_ILM_CDS_EXTRACTOR | Map ILM Objects to CDS View | 103300 | BW-GEN-DPP | BW-GEN-DPP |
| SAP_CA_BC_IC_LND_GEN_DPP_PC | Data Privacy Extractor - Configuration | GEN_NOTIF_MAP_CE |  | FD_ILM_CDS_EXTRACTOR | Map ILM Objects to CDS View | 103300 | BW-GEN-DPP | BW-GEN-DPP |
| SAP_CA_BC_IC_LND_FIN_CS0_PC | Consolidation - Configuration | FINCS_MAP_RLDNR_U |  | SIMG_CFMENUMAPRLDNR | Define Group Reporting Preparation Ledgers | 104277 | FIN-CS | FIN-CS-2CL |
| SAP_CA_BC_IC_LND_FIN_CS0_PC | Consolidation - Configuration | S_ER9_11001857 | S_ER9_11001857_TRAN | SIMG_CFMENUMAPRLDNR | Define Group Reporting Preparation Ledgers | 104277 | FIN-CS | FIN-CS-2CL |
| SAP_CA_BC_IC_LND_FIN_CS0_PC | Consolidation - Configuration | FINCS_ADDLFLD_SEL_U | FINCS_ADDLFLD_SEL_U_TRAN | SIMG_CFMENUADDLFLDU | Define Consolidation Master Data Fields | 101296 | FIN-CS | FIN-CS-2CL |
| SAP_CA_BC_IC_LND_FIN_CS0_PC | Consolidation - Configuration | FINCS_EPUC_GL |  | SIMG_CFFINCS_EPU_GL | Define G/L Settings for Equity Pickup | 104347 | FIN-CS | FIN-CS-COR-EPU-2CL |
| SAP_CA_BC_IC_LND_FIN_CS0_PC | Consolidation - Configuration | FINCS_EPUC_PI |  | SIMG_CFFINCS_EPUC_PI | Define Posting Items for Equity Pickup | 104219 | FIN-CS | FIN-CS-COR-EPU-2CL |
| SAP_CA_BC_IC_LND_FIN_CS0_PC | Consolidation - Configuration | S_ER9_11000639 | S_ER9_11000639_TRAN | SIMG_CFMENUCCX8ITAVC | Define FS Item Attribute Values | 101937 | FIN-CS | FIN-CS-2CL |
| SAP_CA_BC_IC_LND_FIN_CS0_PC | Consolidation - Configuration | FINCS_EPUC_GS |  | SIMG_CFFINCS_EPU_GS | Define General Settings for Equity Pickup | 104218 | FIN-CS | FIN-CS-COR-EPU-2CL |
| SAP_CA_BC_IC_LND_FIN_CS0_PC | Consolidation - Configuration | S_ER9_11001747 | S_ER9_11001747_TRAN | SIMG_CFFINCS_EPU_GS | Define General Settings for Equity Pickup | 104218 | FIN-CS | FIN-CS-COR-EPU-2CL |
| SAP_CA_BC_IC_LND_FIN_CS0_PC | Consolidation - Configuration | S_ER9_11000638 | S_ER9_11000638_TRAN | SIMG_CFMENUCXCX8CPVC | Create Version from Reference Version | 101281 | FIN-CS | FIN-CS-2CL |
| SAP_CA_BC_IC_LND_FIN_CS0_PC | Consolidation - Configuration | S_ER9_11000533 | S_ER9_11000533_TRAN | SIMG_CFMENUCX01CXD1C | Define Currency Translation Methods | 102661 | FIN-CS | FIN-CS-2CL |
| SAP_CA_BC_IC_LND_FIN_CS0_PC | Consolidation - Configuration | S_ER9_11000491 | S_ER9_11000491_TRAN | SIMG_CFMENUCX01CX1DC | Define Subitem Categories and Subitems | 101008 | FIN-CS | FIN-CS-2CL |
| SAP_CA_BC_IC_LND_FIN_CS0_PC | Consolidation - Configuration | S_ER9_11000446 | S_ER9_11000446_TRAN | SIMG_CFMENUCX01RCLMC | Define Reclassification Methods | 101011 | FIN-CS | FIN-CS-2CL |
| SAP_CA_BC_IC_LND_FIN_CS0_PC | Consolidation - Configuration | S_P9C_18000042 | S_P9C_18000042_TRAN | SIMG_CFMENUCX01_CC02 | Assign Consolidation Cycle to Version | 101006 | FIN-CS | EC-CS |
| SAP_CA_BC_IC_LND_FIN_CS0_PC | Consolidation - Configuration | S_P9C_18000041 | S_P9C_18000041_TRAN | SIMG_CFMENUCX01_CC01 | Define Consolidation Cycle | 101005 | FIN-CS | EC-CS |
| SAP_CA_BC_IC_LND_FIN_CS0_PC | Consolidation - Configuration | S_ALR_87003004 | S_ALR_87003004_TRAN | SIMG_CFMENUCX01_MD01 | Check Global System Settings | 102660 | FIN-CS | EC-CS |
| SAP_CA_BC_IC_LND_FIN_CS0_PC | Consolidation - Configuration | S_ER9_11001781 | S_ER9_11001781_TRAN | SIMG_CFFINCS_EPU_GL | Define G/L Settings for Equity Pickup | 104347 | FIN-CS | FIN-CS-COR-EPU-2CL |
| SAP_CA_BC_IC_LND_FIN_CS0_PC | Consolidation - Configuration | S_ALR_87002880 | S_ALR_87002880_TRAN | SIMG_CFMENUCX01_MD30 | Define Breakdown Categories | 102697 | FIN-CS | EC-CS |
| SAP_CA_BC_IC_LND_FIN_CS0_PC | Consolidation - Configuration | CXEA |  | SIMG_CFMENUCX01_RC02 | Define Reclassification Tasks | 101294 | FIN-CS | EC-CS |
| SAP_CA_BC_IC_LND_FIN_CS0_PC | Consolidation - Configuration | S_ALR_87002855 | S_ALR_87002855_TRAN | SIMG_CFMENUCX01_CM02 | Assign Task Group to Version | 101295 | FIN-CS | EC-CS |
| SAP_CA_BC_IC_LND_FIN_CS0_PC | Consolidation - Configuration | S_ER9_11001748 | S_ER9_11001748_TRAN | SIMG_CFFINCS_EPUC_PI | Define Posting Items for Equity Pickup | 104219 | FIN-CS | FIN-CS-COR-EPU-2CL |
| SAP_CA_BC_IC_LND_FIN_CS0_PC | Consolidation - Configuration | CXP1 |  | SIMG_CFMENUCX01_CM02 | Assign Task Group to Version | 101295 | FIN-CS | EC-CS |
| SAP_CA_BC_IC_LND_FIN_CS0_PC | Consolidation - Configuration | CXEB | CXEB_TRAN | SIMG_CFMENUCX01RCLMC | Define Reclassification Methods | 101011 | FIN-CS | FIN-CS-2CL |
| SAP_CA_BC_IC_LND_FIN_CS0_PC | Consolidation - Configuration | CXGP | CXGP_03_TRAN | SIMG_CFMENUCX01_GP0C | Set Global Parameters | 104741 | FIN-CS | FIN-CS-MD-2CL |
| SAP_CA_BC_IC_LND_FIN_CS0_PC | Consolidation - Configuration | CXB3 |  | SIMG_CFMENUCX01_MD01 | Check Global System Settings | 102660 | FIN-CS | EC-CS |
| SAP_CA_BC_IC_LND_FIN_CS0_PC | Consolidation - Configuration | CXD1 |  | SIMG_CFMENUCX01CXD1C | Define Currency Translation Methods | 102661 | FIN-CS | FIN-CS-2CL |
| SAP_CA_BC_IC_LND_FIN_CS0_PC | Consolidation - Configuration | CX8ITAVC |  | SIMG_CFMENUCCX8ITAVC | Define FS Item Attribute Values | 101937 | FIN-CS | FIN-CS-2CL |
| SAP_CA_BC_IC_LND_FIN_CS0_PC | Consolidation - Configuration | CX5TE |  | SIMG_CFMENUCX01_CC02 | Assign Consolidation Cycle to Version | 101006 | FIN-CS | EC-CS |
| SAP_CA_BC_IC_LND_FIN_CS0_PC | Consolidation - Configuration | CX8CPV |  | SIMG_CFMENUCXCX8CPVC | Create Version from Reference Version | 101281 | FIN-CS | FIN-CS-2CL |
| SAP_CA_BC_IC_LND_FIN_CS0_PC | Consolidation - Configuration | CX5TD |  | SIMG_CFMENUCX01_CC01 | Define Consolidation Cycle | 101005 | FIN-CS | EC-CS |
| SAP_CA_BC_IC_LND_FIN_CS0_PC | Consolidation - Configuration | CX1I4 | CX1I4_TRAN | SIMG_CFMENUCX01_MD30 | Define Breakdown Categories | 102697 | FIN-CS | EC-CS |
| SAP_CA_BC_IC_LND_FIN_CS0_PC | Consolidation - Configuration | CXD2 |  | SIMG_CFMENUCX01_CU05 | Define Exchange Rate Indicators | 104460 | FIN-CS | EC-CS |
| SAP_CA_BC_IC_LND_FIN_CS0_PC | Consolidation - Configuration | S_ALR_87003184 | S_ALR_87003184_TRAN | SIMG_CFMENUCX01_CU05 | Define Exchange Rate Indicators | 104460 | FIN-CS | EC-CS |
| SAP_CA_BC_IC_LND_FIN_CS0_PC | Consolidation - Configuration | S_ER9_11000784 | S_ER9_11000784_TRAN | SIMG_CFMENUCX8BCF_RA | Specify Account Numbers for Annual Net Income and Balance Carryforward | 105363 | FIN-CS | FIN-CS-2CL |
| SAP_CA_BC_IC_LND_FIN_CS0_PC | Consolidation - Configuration | CX8BCF_RACCT | CX8BCF_RACCT_TRAN | SIMG_CFMENUCX8BCF_RA | Specify Account Numbers for Annual Net Income and Balance Carryforward | 105363 | FIN-CS | FIN-CS-2CL |
| SAP_CA_BC_IC_LND_FIN_CS0_PC | Consolidation - Configuration | S_ALR_87001738 | S_ALR_87001738_TRAN | SIMG_CFMENUCX01_RC02 | Define Reclassification Tasks | 101294 | FIN-CS | EC-CS |
| SAP_CA_BC_IC_LND_FIN_CS0_PC | Consolidation - Configuration | CXE1 |  | SIMG_CFMENUCX01_CXE1 | Define Document Types | 104665 | FIN-CS | EC-CS |
| SAP_CA_BC_IC_LND_FIN_CS0_PC | Consolidation - Configuration | CXP5 |  | SIMG_CFMENUCX01_PO03 | Define Tasks for Manual Posting | 104738 | FIN-CS | EC-CS |
| SAP_CA_BC_IC_LND_FIN_CS0_PC | Consolidation - Configuration | S_ER9_11001928 | S_ER9_11001928_TRAN | SIMG_CFMENUCX01_GP0C | Set Global Parameters | 104741 | FIN-CS | FIN-CS-MD-2CL |
| SAP_CA_BC_IC_LND_FIN_CS0_PC | Consolidation - Configuration | S_ER9_11001385 | S_ER9_11001385_TRAN | SIMG_CFMENUCX01_CXE1 | Define Document Types | 104665 | FIN-CS | EC-CS |
| SAP_CA_BC_IC_LND_FIN_CS0_PC | Consolidation - Configuration | S_ER9_11000657 | S_ER9_11000657_TRAN | SIMG_CFMENUADDLFLDU | Define Consolidation Master Data Fields | 101296 | FIN-CS | FIN-CS-2CL |
| SAP_CA_BC_IC_LND_FIN_CS0_PC | Consolidation - Configuration | CXE0 |  | SIMG_CFMENUCX01_CM01 | Define Task Group | 104737 | FIN-CS | EC-CS |
| SAP_CA_BC_IC_LND_FIN_CS0_PC | Consolidation - Configuration | CX8TT16 |  | SIMG_CFMENUCXCX8TT16 | Define Tasks for ICMR Eliminations | 104760 | FIN-CS | EC-CS |
| SAP_CA_BC_IC_LND_FIN_CS0_PC | Consolidation - Configuration | S_ER9_11001629 | S_ER9_11001629_TRAN | SIMG_CFMENUCXCX8TT16 | Define Tasks for ICMR Eliminations | 104760 | FIN-CS | EC-CS |
| SAP_CA_BC_IC_LND_FIN_CS0_PC | Consolidation - Configuration | S_ALR_87003143 | S_ALR_87003143_TRAN | SIMG_CFMENUCX01_CM01 | Define Task Group | 104737 | FIN-CS | EC-CS |
| SAP_CA_BC_IC_LND_FIN_CS0_PC | Consolidation - Configuration | S_ALR_87003117 | S_ALR_87003117_TRAN | SIMG_CFMENUCX01_PO03 | Define Tasks for Manual Posting | 104738 | FIN-CS | EC-CS |
| SAP_CA_BC_IC_LND_FIN_CS0_PC | Consolidation - Configuration | S_ER9_11001983 | S_ER9_11001983_TRAN | FINCS_VC_TF540_9U | Add Custom Task for Consolidation Monitor | 105155 | FIN-CS | FIN-CS-COR-2CL |
| SAP_CA_BC_IC_LND_FIN_CS0_PC | Consolidation - Configuration | S_ALR_87002681 | S_ALR_87002681_TRAN | SIMG_CMMENUORFF_1510 | Maintain Transaction Types for Consolidation | 102366 | FIN-CS | FI-GL-GL-A-2CL |
| SAP_CA_BC_IC_LND_FIN_CS0_PC | Consolidation - Configuration | OC08 |  | SIMG_CMMENUORFF_1510 | Maintain Transaction Types for Consolidation | 102366 | FIN-CS | FI-GL-GL-A-2CL |
| SAP_CA_BC_IC_LND_FIN_CS0_PC | Consolidation - Configuration | S_ER9_11001978 | S_ER9_11001978_TRAN | FINCS_VC_TF540_0U | Add Custom Task for Data Monitor | 105154 | FIN-CS | FIN-CS-COR-2CL |
| SAP_CA_BC_IC_LND_FIN_CS0_PC | Consolidation - Configuration | FINCS_CUST_CM |  | FINCS_VC_TF540_9U | Add Custom Task for Consolidation Monitor | 105155 | FIN-CS | FIN-CS-COR-2CL |
| SAP_CA_BC_IC_LND_FIN_CS0_PC | Consolidation - Configuration | S_ER9_11001630 | S_ER9_11001630_TRAN | SIMG_CFMENUCXCX8TT02 | Define Data Collection Tasks with Document Type Assignment | 104761 | FIN-CS | EC-CS |
| SAP_CA_BC_IC_LND_FIN_CS0_PC | Consolidation - Configuration | FINCS_CUST_DM |  | FINCS_VC_TF540_0U | Add Custom Task for Data Monitor | 105154 | FIN-CS | FIN-CS-COR-2CL |
| SAP_CA_BC_IC_LND_FIN_CS0_PC | Consolidation - Configuration | CX8TT02 |  | SIMG_CFMENUCXCX8TT02 | Define Data Collection Tasks with Document Type Assignment | 104761 | FIN-CS | EC-CS |
| SAP_CA_BC_IC_LND_FIN_CS0_PC | Consolidation - Configuration | FINCS_DRT_TRAN_U |  | SIMG_CFMENUMDRTTRAN | Data Release Task: Define Mapping for Jrnl Entry to Group Jrnl Entry Fields | 105996 | FIN-CS | FIN-CS-COR-2CL |
| SAP_CA_BC_IC_LND_FIN_CS0_PC | Consolidation - Configuration | S_ER9_11002373 | S_ER9_11002373_TRAN | FINCS_VC_TF540_EX | Define External Posting Task | 105881 | FIN-CS | FIN-CS-2CL |
| SAP_CA_BC_IC_LND_FIN_CS0_PC | Consolidation - Configuration | S_ER9_11002322 | S_ER9_11002322_TRAN | SIMG_CFMENUCUSELATTR | Define Consolidation Unit Attribute Values | 105735 | FIN-CS | FIN-CS-MD-2CL |
| SAP_CA_BC_IC_LND_FIN_CS0_PC | Consolidation - Configuration | S_ER9_11000846 | S_ER9_11000846_TRAN | SIMG_CFMENUCX01CX53C | Edit Number Range Intervals for Posting |  | FIN-CS | FIN-CS-2CL |
| SAP_CA_BC_IC_LND_FIN_CS0_PC | Consolidation - Configuration | FINCS_BCF_CONFIG |  | VC_FINCS_BCF_CONFIGU | Define Balance Carryforward Settings | 105896 | FIN-CS | FIN-CS-COR-2CL |
| SAP_CA_BC_IC_LND_FIN_CS0_PC | Consolidation - Configuration | S_ALR_87002888 | S_ALR_87002888_TRAN | SIMG_CFMENUCX01_MD31 | Define Subitem Categories and Subitems |  | FIN-CS | EC-CS |
| SAP_CA_BC_IC_LND_FIN_CS0_PC | Consolidation - Configuration | FINCS_CU_SATTR_U |  | SIMG_CFMENUCUSELATTR | Define Consolidation Unit Attribute Values | 105735 | FIN-CS | FIN-CS-MD-2CL |
| SAP_CA_BC_IC_LND_FIN_CS0_PC | Consolidation - Configuration | FINCS_TASK_EX |  | FINCS_VC_TF540_EX | Define External Posting Task | 105881 | FIN-CS | FIN-CS-2CL |
| SAP_CA_BC_IC_LND_FIN_CS0_PC | Consolidation - Configuration | S_ER9_11002674 | S_ER9_11002674_TRAN | SIMG_CFMENUCX01_MD3C | Define Breakdown Categories | 106346 | FIN-CS | FIN-CS-MD-2CL |
| SAP_CA_BC_IC_LND_FIN_CS0_PC | Consolidation - Configuration | S_ER9_11002429 | S_ER9_11002429_TRAN | VC_FINCS_BCF_CONFIGU | Define Balance Carryforward Settings | 105896 | FIN-CS | FIN-CS-COR-2CL |
| SAP_CA_BC_IC_LND_FIN_CS0_PC | Consolidation - Configuration | S_ER9_11002448 | S_ER9_11002448_TRAN | SIMG_CFMENUMDRTTRAN | Data Release Task: Define Mapping for Jrnl Entry to Group Jrnl Entry Fields | 105996 | FIN-CS | FIN-CS-COR-2CL |
| SAP_CA_BC_IC_LND_FIN_CS0_PC | Consolidation - Configuration | FINCS_VERS_DEF |  | SIMG_CFMENUCX01TF200 | Define Versions | 101012 | FIN-CS | FIN-CS-2CL |
| SAP_CA_BC_IC_LND_FIN_CS0_PC | Consolidation - Configuration | S_ER9_11000485 | S_ER9_11000485_TRAN | SIMG_CFMENUCX01TF200 | Define Versions | 101012 | FIN-CS | FIN-CS-2CL |
| SAP_CA_BC_IC_LND_FIN_CS0_PC | Consolidation - Configuration | CX53 |  | SIMG_CFMENUCX01CX53C | Edit Number Range Intervals for Posting |  | FIN-CS | FIN-CS-2CL |
| SAP_CA_BC_IC_LND_FIN_CS0_PC | Consolidation - Configuration | CX1S3 | CX1S3_TRAN | SIMG_CFMENUCX01_MD31 | Define Subitem Categories and Subitems |  | FIN-CS | EC-CS |
| SAP_CA_BC_IC_LND_FIN_CS0_PC | Consolidation - Configuration | FINCS_LIVT_U |  | SIMG_CFMENU_LIVT | Define Tasks for Line Item Validation | 106812 | FIN-CS | FIN-CS-COR-DT-2CL |
| SAP_CA_BC_IC_LND_FIN_CS0_PC | Consolidation - Configuration | FINCS_LWBF_FS |  | SIMG_CFMENULWBF_FS | Activate Fields for Financial Services | 106739 | FIN-CS | FIN-CS-MD-2CL |
| SAP_CA_BC_IC_LND_FIN_CS0_PC | Consolidation - Configuration | FINCS_LWBF_GHG |  | SIMG_CFMENULWBF_GHG | Activate Fields for Greenhouse Gas | 106770 | FIN-CS | FIN-CS-MD-2CL |
| SAP_CA_BC_IC_LND_FIN_CS0_PC | Consolidation - Configuration | CX1S4 | CX1S4_TRAN | SIMG_CFMENUCX01CX1DC | Define Subitem Categories and Subitems | 101008 | FIN-CS | FIN-CS-2CL |
| SAP_CA_BC_IC_LND_FIN_CS0_PC | Consolidation - Configuration | S_ER1_70001288 | S_ER1_70001288_TRAN | FINCS_TM_PRCPERASGN | Assign Process Period Cycles | 106904 | FIN-CS | FIN-CS-COR-MON-2CL |
| SAP_CA_BC_IC_LND_FIN_CS0_PC | Consolidation - Configuration | S_ER1_70000916 | S_ER1_70000916_TRAN | SIMG_CFMENULWBF_FS | Activate Fields for Financial Services | 106739 | FIN-CS | FIN-CS-MD-2CL |
| SAP_CA_BC_IC_LND_FIN_CS0_PC | Consolidation - Configuration | S_ER1_70001011 | S_ER1_70001011_TRAN | SIMG_CFMENULWBF_GHG | Activate Fields for Greenhouse Gas | 106770 | FIN-CS | FIN-CS-MD-2CL |
| SAP_CA_BC_IC_LND_FIN_CS0_PC | Consolidation - Configuration | S_ER1_70001062 | S_ER1_70001062_TRAN | SIMG_CFMENULWBF_PS | Activate Fields for Public Sector | 106789 | FIN-CS | FIN-CS-MD-2CL |
| SAP_CA_BC_IC_LND_FIN_CS0_PC | Consolidation - Configuration | FINCS_FSI_TYPE_U |  | SIMG_CFFINCS_FSITEYP | Define Default Sign Convention for FS Item Types | 106968 | FIN-CS | FIN-CS-MD-2CL |
| SAP_CA_BC_IC_LND_FIN_CS0_PC | Consolidation - Configuration | S_ER1_70001080 | S_ER1_70001080_TRAN | SIMG_CFMENU_LIVT | Define Tasks for Line Item Validation | 106812 | FIN-CS | FIN-CS-COR-DT-2CL |
| SAP_CA_BC_IC_LND_FIN_CS0_PC | Consolidation - Configuration | S_ER1_70001245 | S_ER1_70001245_TRAN | FINCS_TM_PRCPER | Define Process Period Cycles | 106889 | FIN-CS | FIN-CS-COR-MON-2CL |
| SAP_CA_BC_IC_LND_FIN_CS0_PC | Consolidation - Configuration | FINCS_RT_DF |  | V_TF540_RT | Define Tasks for Automatic Postings | 106920 | FIN-CS | FIN-CS-RUL-2CL |
| SAP_CA_BC_IC_LND_FIN_CS0_PC | Consolidation - Configuration | S_ER1_70001388 | S_ER1_70001388_TRAN | SIMG_CFFINCS_FSITEYP | Define Default Sign Convention for FS Item Types | 106968 | FIN-CS | FIN-CS-MD-2CL |
| SAP_CA_BC_IC_LND_FIN_CS0_PC | Consolidation - Configuration | CXL4 |  | SIMG_CFMENUCX01_MD06 | Define Ledgers |  | FIN-CS | EC-CS |
| SAP_CA_BC_IC_LND_FIN_CS0_PC | Consolidation - Configuration | FINCS_TM_PRCPERCYC_U |  | FINCS_TM_PRCPER | Define Process Period Cycles | 106889 | FIN-CS | FIN-CS-COR-MON-2CL |
| SAP_CA_BC_IC_LND_FIN_CS0_PC | Consolidation - Configuration | S_ER1_70001307 | S_ER1_70001307_TRAN | V_TF540_RT | Define Tasks for Automatic Postings | 106920 | FIN-CS | FIN-CS-RUL-2CL |
| SAP_CA_BC_IC_LND_FIN_CS0_PC | Consolidation - Configuration | FINCS_LWBF_PS |  | SIMG_CFMENULWBF_PS | Activate Fields for Public Sector | 106789 | FIN-CS | FIN-CS-MD-2CL |
| SAP_CA_BC_IC_LND_FIN_CS0_PC | Consolidation - Configuration | CXEC | CXEC_TRAN |  |  |  | FIN-CS |  |
| SAP_CA_BC_IC_LND_FIN_CS0_PC | Consolidation - Configuration | FINCS_TM_PRCPERASG_U |  | FINCS_TM_PRCPERASGN | Assign Process Period Cycles | 106904 | FIN-CS | FIN-CS-COR-MON-2CL |
| SAP_CA_BC_IC_LND_FIN_CS0_PC | Consolidation - Configuration | CXL3 | CXL3_TRAN | SIMG_CFMENUCX01_MD06 | Define Ledgers |  | FIN-CS | EC-CS |
| SAP_CA_BC_IC_LND_FIN_CS0_PC | Consolidation - Configuration | S_ALR_87002958 | S_ALR_87002958_TRAN | SIMG_CFMENUCX01_MD06 | Define Ledgers |  | FIN-CS | EC-CS |
| SAP_CA_BC_IC_LND_FIN_CS0_PC | Consolidation - Configuration | CXL2 | CXL2_TRAN | SIMG_CFMENUCX01_MD06 | Define Ledgers |  | FIN-CS | EC-CS |
| SAP_CA_BC_IC_LND_FIN_CS0_PC | Consolidation - Configuration | CXL1 |  | SIMG_CFMENUCX01_MD06 | Define Ledgers |  | FIN-CS | EC-CS |
| SAP_CA_BC_IC_LND_FIN_CS0_PC | Consolidation - Configuration | FINCS_CV_ASSIGN |  | SIMG_CFMENU_BVCVA | Define Comparison Versions | 107033 | FIN-CS | FIN-CS-BV-2CL |
| SAP_CA_BC_IC_LND_FIN_CS0_PC | Consolidation - Configuration | FINCS_RT_DM |  | VC_TF600_SSCUI | Define Consolidation Methods | 107264 | FIN-CS | FIN-CS-RUL-2CL |
| SAP_CA_BC_IC_LND_FIN_CS0_PC | Consolidation - Configuration | CXE5 | CXE5_TRAN | SIMG_CFMENUCX01CXE5C | Specify Selected FS Items for Automatic Posting | 101009 | FIN-CS | FIN-CS-2CL |
| SAP_CA_BC_IC_LND_FIN_CS0_PC | Consolidation - Configuration | S_ER1_70001799 | S_ER1_70001799_TRAN | VC_TF600_SSCUI | Define Consolidation Methods | 107264 | FIN-CS | FIN-CS-RUL-2CL |
| SAP_CA_BC_IC_LND_FIN_CS0_PC | Consolidation - Configuration | S_ER9_11000495 | S_ER9_11000495_TRAN | SIMG_CFMENUCX01CXE5C | Specify Selected FS Items for Automatic Posting | 101009 | FIN-CS | FIN-CS-2CL |
| SAP_CA_BC_IC_LND_FIN_CS0_PC | Consolidation - Configuration | S_ER1_70001895 | S_ER1_70001895_TRAN | SIMG_CFFINCS_GRPSTR | Define Settings for Group Structure Management | 107370 | FIN-CS | FIN-CS-MD-2CL |
| SAP_CA_BC_IC_LND_FIN_CS0_PC | Consolidation - Configuration | S_ER9_11000548 | S_ER9_11000548_TRAN | SIMG_CFMENUCX01CXL1C | Define Consolidation Ledgers | 101010 | FIN-CS | FIN-CS-2CL |
| SAP_CA_BC_IC_LND_FIN_CS0_PC | Consolidation - Configuration | S_ER1_70001509 | S_ER1_70001509_TRAN | SIMG_CFMENU_BVCVA | Define Comparison Versions | 107033 | FIN-CS | FIN-CS-BV-2CL |
| SAP_CA_BC_IC_LND_LE_JIT0_PC | Logistics Execution - Next Generation Just-In-Time Processing - Configuration | S_ER9_52001263 | S_ER9_52001263_TRAN | SIMG_NJIT_ACT_CTRL | Define JIT Action Control | 103116 | LE-JIT-S2C | LE-JIT |
| SAP_CA_BC_IC_LND_LE_JIT0_PC | Logistics Execution - Next Generation Just-In-Time Processing - Configuration | S_ER9_52001262 | S_ER9_52001262_TRAN | SIMG_NJIT_STATUS | Define External Status and Internal Processing Status (JIT) | 103114 | LE-JIT-S2C | LE-JIT |
| SAP_CA_BC_IC_LND_LE_JIT0_PC | Logistics Execution - Next Generation Just-In-Time Processing - Configuration | S_ER9_52002790 | S_ER9_52002790_TRAN | SIMG_NJIT_MAP_AC_FN | Map Responsibility Management Functions to JIT Actions | 105318 | LE-JIT-S2C | LE-JIT-S2C |
| SAP_CA_BC_IC_LND_LE_JIT0_PC | Logistics Execution - Next Generation Just-In-Time Processing - Configuration | S_ER9_52001228 | S_ER9_52001228_TRAN | SIMG_NJIT_REFNUM | Define Reference Types for Additional JIT Call Data | 103117 | LE-JIT-S2C | LE-JIT |
| SAP_CA_BC_IC_LND_LE_JIT0_PC | Logistics Execution - Next Generation Just-In-Time Processing - Configuration | S_ER9_52002022 | S_ER9_52002022_TRAN | SIMG_NJIT_SEQN_PRF | Maintain JIT Sequence Number Profiles | 103561 | LE-JIT-S2C | LE-JIT-S2C |
| SAP_CA_BC_IC_LND_LE_JIT0_PC | Logistics Execution - Next Generation Just-In-Time Processing - Configuration | S_ER9_52001258 | S_ER9_52001258_TRAN | SIMG_NJIT_ACTIONS | Define JIT Actions | 103115 | LE-JIT-S2C | LE-JIT |
| SAP_CA_BC_IC_LND_LE_JIT0_PC | Logistics Execution - Next Generation Just-In-Time Processing - Configuration | NJITSCID |  | SIMG_NJIT_SUPCTRL_I | Maintain Number Range Objects for Customer Supply Control |  | LE-JIT-S2C | LE-JIT-S2C |
| SAP_CA_BC_IC_LND_LE_JIT0_PC | Logistics Execution - Next Generation Just-In-Time Processing - Configuration | NJITREQID |  | SIMG_NJIT_CALLNO_I | Maintain Number Range Objects for Just-In-Time Calls |  | LE-JIT-S2C | LE-JIT-S2C |
| SAP_CA_BC_IC_LND_LE_JIT0_PC | Logistics Execution - Next Generation Just-In-Time Processing - Configuration | NJITPGID |  | SIMG_NJIT_PKG_I | Maintain Number Range Objects for Packing Group |  | LE-JIT-S2C | LE-JIT-S2C |
| SAP_CA_BC_IC_LND_LE_JIT0_PC | Logistics Execution - Next Generation Just-In-Time Processing - Configuration | NJITPGDID |  | SIMG_NJIT_PKGDEF_I | Maintain Number Range Objects for Packing Group Specification |  | LE-JIT-S2C | LE-JIT-S2C |
| SAP_CA_BC_IC_LND_LE_JIT0_PC | Logistics Execution - Next Generation Just-In-Time Processing - Configuration | NJITDSGID |  | SIMG_NJIT_DSGID | Maintain Number Range Objects for Delivery Sequence Groups |  | LE-JIT-S2C | LE-JIT-S2C |
| SAP_CA_BC_IC_LND_LE_JIT0_PC | Logistics Execution - Next Generation Just-In-Time Processing - Configuration | NJITDCID |  | SIMG_NJIT_DCID | Maintain Number Range Objects for JIT Delivery Confirmations |  | LE-JIT-S2C | LE-JIT-S2C |
| SAP_CA_BC_IC_LND_LE_JIT0_PC | Logistics Execution - Next Generation Just-In-Time Processing - Configuration | S_ER9_52004173 | S_ER9_52004173_TRAN | SIMG_NJIT_SCHEDULING | Activate Business Process Scheduling Schema for JIT Attributes |  | LE-JIT-S2C | LE-JIT-S2C |
| SAP_CA_BC_IC_LND_LE_JIT0_PC | Logistics Execution - Next Generation Just-In-Time Processing - Configuration | S_ER9_52002447 | S_ER9_52002447_TRAN | SIMG_NJIT_SORT_VAR | Maintain JIT Sort Variants | 103963 | LE-JIT-S2C | LE-JIT-S2C |
| SAP_CA_BC_IC_LND_LE_JIT0_PC | Logistics Execution - Next Generation Just-In-Time Processing - Configuration | S_ER9_52003319 | S_ER9_52003319_TRAN | SMIG_NJIT_INB_PARAM | BAdI: Inbound Mapping for JIT Call Request EDI message |  | LE-JIT-S2C | LE-JIT-S2C |
| SAP_CA_BC_IC_LND_LE_JIT0_PC | Logistics Execution - Next Generation Just-In-Time Processing - Configuration | S_ER9_52003317 | S_ER9_52003317_TRAN | SMIG_NJIT_CSTM_ACTN | BAdI: Implementation of custom actions in JIT Supply to Customer solution |  | LE-JIT-S2C | LE-JIT-S2C |
| SAP_CA_BC_IC_LND_LE_JIT0_PC | Logistics Execution - Next Generation Just-In-Time Processing - Configuration | S_ER9_52003316 | S_ER9_52003316_TRAN | SMIG_NJIT_PRODN_CONF | BAdI: Modify Production Confirmation Profile |  | LE-JIT-S2C | LE-JIT-S2C |
| SAP_CA_BC_IC_LND_LE_JIT0_PC | Logistics Execution - Next Generation Just-In-Time Processing - Configuration | S_ER9_52003315 | S_ER9_52003315_TRAN | SMIG_NJIT_LFCYC_STS | BAdI: Influence JIT Call Lifecycle Status determination |  | LE-JIT-S2C | LE-JIT-S2C |
| SAP_CA_BC_IC_LND_LE_JIT0_PC | Logistics Execution - Next Generation Just-In-Time Processing - Configuration | S_ER9_52003314 | S_ER9_52003314_TRAN | SMIG_NJIT_PRE_PROCG | BAdI: Enhance pre-processing of standard action |  | LE-JIT-S2C | LE-JIT-S2C |
| SAP_CA_BC_IC_LND_LE_JIT0_PC | Logistics Execution - Next Generation Just-In-Time Processing - Configuration | S_ER9_52003313 | S_ER9_52003313_TRAN | SMIG_NJIT_POST_PROCG | BAdI: Enhance post-processing of standard action |  | LE-JIT-S2C | LE-JIT-S2C |
| SAP_CA_BC_IC_LND_LE_JIT0_PC | Logistics Execution - Next Generation Just-In-Time Processing - Configuration | S_ER9_52003312 | S_ER9_52003312_TRAN | SMIG_NJIT_JITDLVSCH | BAdI: Modify JIT Delivery Schedule lines before generation |  | LE-JIT-S2C | LE-JIT-S2C |
| SAP_CA_BC_IC_LND_LE_JIT0_PC | Logistics Execution - Next Generation Just-In-Time Processing - Configuration | S_ER9_52003311 | S_ER9_52003311_TRAN | SMIG_NJIT_PROC_BKFLH | BAdI: Implementation of custom backflush for JIT Call Components |  | LE-JIT-S2C | LE-JIT-S2C |
| SAP_CA_BC_IC_LND_LE_JIT0_PC | Logistics Execution - Next Generation Just-In-Time Processing - Configuration | S_ER9_52003309 | S_ER9_52003309_TRAN | SMIG_NJIT_CG_DETN | BAdI: Determination of Component Groups for JIT Inbound Call Components |  | LE-JIT-S2C | LE-JIT-S2C |
| SAP_CA_BC_IC_LND_LE_JIT0_PC | Logistics Execution - Next Generation Just-In-Time Processing - Configuration | S_ER9_52002822 | S_ER9_52002822_TRAN | SIMG_NJIT_VP | Maintain Verification Profile |  | LE-JIT-S2C | LE-JIT-S2C |
| SAP_CA_BC_IC_LND_LE_JIT0_PC | Logistics Execution - Next Generation Just-In-Time Processing - Configuration | S_ER9_52002545 | S_ER9_52002545_TRAN | SIMG_NJIT_DCID | Maintain Number Range Objects for JIT Delivery Confirmations |  | LE-JIT-S2C | LE-JIT-S2C |
| SAP_CA_BC_IC_LND_LE_JIT0_PC | Logistics Execution - Next Generation Just-In-Time Processing - Configuration | S_ER9_52002198 | S_ER9_52002198_TRAN | SIMG_NJIT_DSGID | Maintain Number Range Objects for Delivery Sequence Groups |  | LE-JIT-S2C | LE-JIT-S2C |
| SAP_CA_BC_IC_LND_LE_JIT0_PC | Logistics Execution - Next Generation Just-In-Time Processing - Configuration | S_ER9_52001378 | S_ER9_52001378_TRAN | SIMG_NJIT_PKG_I | Maintain Number Range Objects for Packing Group |  | LE-JIT-S2C | LE-JIT-S2C |
| SAP_CA_BC_IC_LND_LE_JIT0_PC | Logistics Execution - Next Generation Just-In-Time Processing - Configuration | S_ER9_52001377 | S_ER9_52001377_TRAN | SIMG_NJIT_PKGDEF_I | Maintain Number Range Objects for Packing Group Specification |  | LE-JIT-S2C | LE-JIT-S2C |
| SAP_CA_BC_IC_LND_LE_JIT0_PC | Logistics Execution - Next Generation Just-In-Time Processing - Configuration | S_ER9_52001376 | S_ER9_52001376_TRAN | SIMG_NJIT_SUPCTRL_I | Maintain Number Range Objects for Customer Supply Control |  | LE-JIT-S2C | LE-JIT-S2C |
| SAP_CA_BC_IC_LND_LE_JIT0_PC | Logistics Execution - Next Generation Just-In-Time Processing - Configuration | S_ER9_52001375 | S_ER9_52001375_TRAN | SIMG_NJIT_CALLNO_I | Maintain Number Range Objects for Just-In-Time Calls |  | LE-JIT-S2C | LE-JIT-S2C |
| SAP_CA_BC_IC_LND_FIN_JVA_PC | Joint Venture Accounting - Configuration | S_KK4_66000092 | S_KK4_66000092_TRAN | SIMG_MAS_0011 | Clearing Procedures | 103075 | CA-JVA | CA-JVA |
| SAP_CA_BC_IC_LND_FIN_JVA_PC | Joint Venture Accounting - Configuration | S_KK4_66000113 | S_KK4_66000113_TRAN | SIMG_PRO_0003 | Posting Rules | 103076 | CA-JVA | CA-JVA |
| SAP_CA_BC_IC_LND_FIN_JVA_PC | Joint Venture Accounting - Configuration | S_KK4_66000093 | S_KK4_66000093_TRAN | SIMG_MAS_0010 | Define Billing Indicator | 103074 | CA-JVA | CA-JVA |
| SAP_CA_BC_IC_LND_FIN_JVA_PC | Joint Venture Accounting - Configuration | S_KK4_66000094 | S_KK4_66000094_TRAN | SIMG_MAS_0009 | Define Recovery Indicators | 102809 | CA-JVA | CA-JVA |
| SAP_CA_BC_IC_LND_FIN_JVA_PC | Joint Venture Accounting - Configuration | S_KK4_66000084 | S_KK4_66000084_TRAN | SIMG_MAS_0002 | JOA Class | 102959 | CA-JVA | CA-JVA |
| SAP_CA_BC_IC_LND_FIN_JVA_PC | Joint Venture Accounting - Configuration | S_KK4_66000083 | S_KK4_66000083_TRAN | SIMG_MAS_0003 | Define Venture Class | 102960 | CA-JVA | CA-JVA |
| SAP_CA_BC_IC_LND_FIN_JVA_PC | Joint Venture Accounting - Configuration | S_ER9_11000949 | S_ER9_11000949_TRAN | SIMG_MAS_0112 | Maintain Joint Venture Master Number Range | 103021 | CA-JVA | CA-JVA |
| SAP_CA_BC_IC_LND_FIN_JVA_PC | Joint Venture Accounting - Configuration | S_ER9_11000948 | S_ER9_11000948_TRAN | SIMG_MAS_0111 | Maintain JOA Number Range | 103016 | CA-JVA | CA-JVA |
| SAP_CA_BC_IC_LND_FIN_JVA_PC | Joint Venture Accounting - Configuration | S_KK4_66000124 | S_KK4_66000124_TRAN | SIMG_PRO_0002 | Posting Methods | 103157 | CA-JVA | CA-JVA |
| SAP_CA_BC_IC_LND_FIN_JVA_PC | Joint Venture Accounting - Configuration | S_KK4_66000120 | S_KK4_66000120_TRAN | SIMG_MAS_0023 | Define Subclass B for Joint Interest Billing | 103182 | CA-JVA | CA-JVA |
| SAP_CA_BC_IC_LND_FIN_JVA_PC | Joint Venture Accounting - Configuration | S_KK4_66000118 | S_KK4_66000118_TRAN | SIMG_MAS_0022 | Define Subclass A for Joint Interest Billing | 103181 | CA-JVA | CA-JVA |
| SAP_CA_BC_IC_LND_FIN_JVA_PC | Joint Venture Accounting - Configuration | S_KK4_66000117 | S_KK4_66000117_TRAN | SIMG_MAS_0024 | Tubular Material Definition | 103177 | CA-JVA | CA-JVA |
| SAP_CA_BC_IC_LND_FIN_JVA_PC | Joint Venture Accounting - Configuration | S_KK4_66000115 | S_KK4_66000115_TRAN | SIMG_MAS_0021 | Define Class for Joint Interest Billing | 103180 | CA-JVA | CA-JVA |
| SAP_CA_BC_IC_LND_FIN_JVA_PC | Joint Venture Accounting - Configuration | S_KK4_66000114 | S_KK4_66000114_TRAN | SIMG_MAS_0025 | Non-Tubular Material Definition | 103178 | CA-JVA | CA-JVA |
| SAP_CA_BC_IC_LND_FIN_JVA_PC | Joint Venture Accounting - Configuration | S_KK4_66000091 | S_KK4_66000091_TRAN | SIMG_MAS_0012 | Net Profit Interest Partner Groups | 103155 | CA-JVA | CA-JVA |
| SAP_CA_BC_IC_LND_FIN_JVA_PC | Joint Venture Accounting - Configuration | S_KK4_66000090 | S_KK4_66000090_TRAN | SIMG_MAS_0013 | Carried Interest Partner Groups | 103156 | CA-JVA | CA-JVA |
| SAP_CA_BC_IC_LND_FIN_JVA_PC | Joint Venture Accounting - Configuration | S_KK4_66000089 | S_KK4_66000089_TRAN | SIMG_MAS_0014 | Cash Call Reclassification Groups | 103154 | CA-JVA | CA-JVA |
| SAP_CA_BC_IC_LND_FIN_JVA_PC | Joint Venture Accounting - Configuration | S_KK4_66000082 | S_KK4_66000082_TRAN | SIMG_MAS_0004 | Equity Types | 103185 | CA-JVA | CA-JVA |
| SAP_CA_BC_IC_LND_FIN_JVA_PC | Joint Venture Accounting - Configuration | S_KK4_66000081 | S_KK4_66000081_TRAN | SIMG_MAS_0005 | CI Penalty Categories | 103187 | CA-JVA | CA-JVA |
| SAP_CA_BC_IC_LND_FIN_JVA_PC | Joint Venture Accounting - Configuration | S_KK4_66000080 | S_KK4_66000080_TRAN | SIMG_MAS_0029 | Overhead Rate Types | 103151 | CA-JVA | CA-JVA |
| SAP_CA_BC_IC_LND_FIN_JVA_PC | Joint Venture Accounting - Configuration | S_KK4_66000079 | S_KK4_66000079_TRAN | SIMG_MAS_0006 | Project/WBS Element Object Types | 103174 | CA-JVA | CA-JVA |
| SAP_CA_BC_IC_LND_FIN_JVA_PC | Joint Venture Accounting - Configuration | S_KK4_66000078 | S_KK4_66000078_TRAN | SIMG_MAS_0007 | Cost Center Object Types | 103186 | CA-JVA | CA-JVA |
| SAP_CA_BC_IC_LND_FIN_JVA_PC | Joint Venture Accounting - Configuration | S_KK4_66000005 | S_KK4_66000005_TRAN | SIMG_PRO_0017 | Risk Labor Cost Elements | 103162 | CA-JVA | CA-JVA |
| SAP_CA_BC_IC_LND_FIN_JVA_PC | Joint Venture Accounting - Configuration | S_KK4_66000004 | S_KK4_66000004_TRAN | SIMG_PRO_0018 | Stepped Rate Rules | 103163 | CA-JVA | CA-JVA |
| SAP_CA_BC_IC_LND_FIN_JVA_PC | Joint Venture Accounting - Configuration | S_ER9_11001342 | S_ER9_11001342_TRAN | GJNR_OHLIST | Maintain Overhead List Number Range for Overhead Organizer | 103262 | CA-JVA | CA-JVA |
| SAP_CA_BC_IC_LND_FIN_JVA_PC | Joint Venture Accounting - Configuration | S_ER9_11001341 | S_ER9_11001341_TRAN | GJNR_OHKEY | Maintain Overhead Key Number Range for Overhead Organizer | 103261 | CA-JVA | CA-JVA |
| SAP_CA_BC_IC_LND_FIN_JVA_PC | Joint Venture Accounting - Configuration | S_ER9_11001339 | S_ER9_11001339_TRAN | GJNR_OHCHAR | Maintain Overhead Character Key Number Range for Overhead Organizer | 103260 | CA-JVA | CA-JVA |
| SAP_CA_BC_IC_LND_FIN_JVA_PC | Joint Venture Accounting - Configuration | S_ER9_11001338 | S_ER9_11001338_TRAN | GJNR_RECID | Maintain Record Index Number Range for Billing | 103259 | CA-JVA | CA-JVA |
| SAP_CA_BC_IC_LND_FIN_JVA_PC | Joint Venture Accounting - Configuration | S_ER9_11001337 | S_ER9_11001337_TRAN | GJNR_CUTBACK | Maintain Cutback Number Range | 103258 | CA-JVA | CA-JVA |
| SAP_CA_BC_IC_LND_FIN_JVA_PC | Joint Venture Accounting - Configuration | S_ER9_11001249 | S_ER9_11001249_TRAN | V_T001_JVA_ACTIV | Activate JVA at Company Code Level | 103134 | CA-JVA | CA-JVA |
| SAP_CA_BC_IC_LND_FIN_JVA_PC | Joint Venture Accounting - Configuration | S_KK4_66000125 | S_KK4_66000125_TRAN | SIMG_PRO_0001 | Processes | 103341 | CA-JVA | CA-JVA |
| SAP_CA_BC_IC_LND_FIN_JVA_PC | Joint Venture Accounting - Configuration | S_KK4_66000116 | S_KK4_66000116_TRAN | SIMG_PRO_0004 | RI Manipulation Rules | 103342 | CA-JVA | CA-JVA |
| SAP_CA_BC_IC_LND_FIN_JVA_PC | Joint Venture Accounting - Configuration | S_KK4_66000088 | S_KK4_66000088_TRAN | SIMG_MAS_0015 | Funding Groups | 103189 | CA-JVA | CA-JVA |
| SAP_CA_BC_IC_LND_FIN_JVA_PC | Joint Venture Accounting - Configuration | S_KK4_66000066 | S_KK4_66000066_TRAN | SIMG_BIL_0003 | Mapping Accounts to JIB Classes for Non-AFEs | 103337 | CA-JVA | CA-JVA |
| SAP_CA_BC_IC_LND_FIN_JVA_PC | Joint Venture Accounting - Configuration | S_KK4_66000062 | S_KK4_66000062_TRAN | SIMG_BIL_0012 | Define Billing Structure | 103320 | CA-JVA | CA-JVA |
| SAP_CA_BC_IC_LND_FIN_JVA_PC | Joint Venture Accounting - Configuration | S_KK4_66000064 | S_KK4_66000064_TRAN | SIMG_BIL_0005 | Mapping JIB Subclasses to Accounts | 103339 | CA-JVA | CA-JVA |
| SAP_CA_BC_IC_LND_FIN_JVA_PC | Joint Venture Accounting - Configuration | S_KK4_66000065 | S_KK4_66000065_TRAN | SIMG_BIL_0004 | Mapping JIB Classes and Accounts to Overwrite Classes | 103338 | CA-JVA | CA-JVA |
| SAP_CA_BC_IC_LND_FIN_JVA_PC | Joint Venture Accounting - Configuration | S_KK4_66000059 | S_KK4_66000059_TRAN | SIMG_BIL_0016 | Billing Formats for Joint Venture Partner Billing | 103324 | CA-JVA | CA-JVA |
| SAP_CA_BC_IC_LND_FIN_JVA_PC | Joint Venture Accounting - Configuration | S_KK4_66000011 | S_KK4_66000011_TRAN | SIMG_BIL_0002 | Mapping Accounts to JIB Classes for AFE's | 103336 | CA-JVA | CA-JVA |
| SAP_CA_BC_IC_LND_FIN_JVA_PC | Joint Venture Accounting - Configuration | S_ER9_11001347 | S_ER9_11001347_TRAN | SIMG_BIL_0025 | Output Control Framework: Maintain Billing Layout | 103340 | CA-JVA | CA-JVA |
| SAP_CA_BC_IC_LND_FIN_JVA_PC | Joint Venture Accounting - Configuration | S_KK4_66000087 | S_KK4_66000087_TRAN | SIMG_MAS_0016 | Bank Accounts | 103347 | CA-JVA | CA-JVA |
| SAP_CA_BC_IC_LND_FIN_JVA_PC | Joint Venture Accounting - Configuration | S_KK4_66000086 | S_KK4_66000086_TRAN | SIMG_MAS_0017 | Funding Group Assignment | 103378 | CA-JVA | CA-JVA |
| SAP_CA_BC_IC_LND_FIN_JVA_PC | Joint Venture Accounting - Configuration | S_KK4_66000044 | S_KK4_66000044_TRAN | SIMG_NOP_0001 | JV Non-Operated Billing Form | 103376 | CA-JVA | CA-JVA |
| SAP_CA_BC_IC_LND_FIN_JVA_PC | Joint Venture Accounting - Configuration | S_KK4_66000012 | S_KK4_66000012_TRAN | SIMG_BIL_0001 | Mapping Billing Indicators to Service Codes | 103377 | CA-JVA | CA-JVA |
| SAP_CA_BC_IC_LND_FIN_JVA_PC | Joint Venture Accounting - Configuration | S_KK4_66000076 | S_KK4_66000076_TRAN | SIMG_BIL_0018 | Accounts for Supplemental Driver | 103430 | CA-JVA | CA-JVA |
| SAP_CA_BC_IC_LND_FIN_JVA_PC | Joint Venture Accounting - Configuration | S_KK4_66000075 | S_KK4_66000075_TRAN | SIMG_BIL_0019 | Recovery Indicators for Supplemental Driver | 103432 | CA-JVA | CA-JVA |
| SAP_CA_BC_IC_LND_FIN_JVA_PC | Joint Venture Accounting - Configuration | S_KK4_66000074 | S_KK4_66000074_TRAN | SIMG_BIL_0020 | JVA Project Types | 103433 | CA-JVA | CA-JVA |
| SAP_CA_BC_IC_LND_FIN_JVA_PC | Joint Venture Accounting - Configuration | S_KK4_66000073 | S_KK4_66000073_TRAN | SIMG_BIL_0021 | JVA Cost Center Types | 103434 | CA-JVA | CA-JVA |
| SAP_CA_BC_IC_LND_FIN_JVA_PC | Joint Venture Accounting - Configuration | GJNR_MASTER | GJNR_MASTER_TRAN | SIMG_MAS_0112 | Maintain Joint Venture Master Number Range | 103021 | CA-JVA | CA-JVA |
| SAP_CA_BC_IC_LND_FIN_JVA_PC | Joint Venture Accounting - Configuration | S_KK4_66000071 | S_KK4_66000071_TRAN | SIMG_BIL_0023 | Driver Protocols | 103431 | CA-JVA | CA-JVA |
| SAP_CA_BC_IC_LND_FIN_JVA_PC | Joint Venture Accounting - Configuration | S_ER9_11001468 | S_ER9_11001468_TRAN | SIMG_MAS_0030 | Interest Calculation Groups | 103427 | CA-JVA | CA-JVA |
| SAP_CA_BC_IC_LND_FIN_JVA_PC | Joint Venture Accounting - Configuration | S_KK4_66000067 | S_KK4_66000067_TRAN | SIMG_BIL_0017 | Billing Indicators for Supplemental Driver | 103429 | CA-JVA | CA-JVA |
| SAP_CA_BC_IC_LND_FIN_JVA_PC | Joint Venture Accounting - Configuration | S_KK4_66000058 | S_KK4_66000058_TRAN | SIMG_BIL_0014 | Supplemental Detail Sets | 103428 | CA-JVA | CA-JVA |
| SAP_CA_BC_IC_LND_FIN_JVA_PC | Joint Venture Accounting - Configuration | GJNR_JOA | GJNR_JOA_TRAN | SIMG_MAS_0111 | Maintain JOA Number Range | 103016 | CA-JVA | CA-JVA |
| SAP_CA_BC_IC_LND_FIN_JVA_PC | Joint Venture Accounting - Configuration | GJEZ |  | SIMG_MAS_0025 | Non-Tubular Material Definition | 103178 | CA-JVA | CA-JVA |
| SAP_CA_BC_IC_LND_FIN_JVA_PC | Joint Venture Accounting - Configuration | GJPC |  | SIMG_MAS_0005 | CI Penalty Categories | 103187 | CA-JVA | CA-JVA |
| SAP_CA_BC_IC_LND_FIN_JVA_PC | Joint Venture Accounting - Configuration | GJEY |  | SIMG_MAS_0024 | Tubular Material Definition | 103177 | CA-JVA | CA-JVA |
| SAP_CA_BC_IC_LND_FIN_JVA_PC | Joint Venture Accounting - Configuration | GJCG |  | SIMG_MAS_0013 | Carried Interest Partner Groups | 103156 | CA-JVA | CA-JVA |
| SAP_CA_BC_IC_LND_FIN_JVA_PC | Joint Venture Accounting - Configuration | GJ76 |  | SIMG_MAS_0014 | Cash Call Reclassification Groups | 103154 | CA-JVA | CA-JVA |
| SAP_CA_BC_IC_LND_FIN_JVA_PC | Joint Venture Accounting - Configuration | GJ72 |  | SIMG_MAS_0002 | JOA Class | 102959 | CA-JVA | CA-JVA |
| SAP_CA_BC_IC_LND_FIN_JVA_PC | Joint Venture Accounting - Configuration | GJ66 |  | SIMG_MAS_0023 | Define Subclass B for Joint Interest Billing | 103182 | CA-JVA | CA-JVA |
| SAP_CA_BC_IC_LND_FIN_JVA_PC | Joint Venture Accounting - Configuration | GJ63 |  | SIMG_MAS_0006 | Project/WBS Element Object Types | 103174 | CA-JVA | CA-JVA |
| SAP_CA_BC_IC_LND_FIN_JVA_PC | Joint Venture Accounting - Configuration | GJ49 |  | SIMG_PRO_0003 | Posting Rules | 103076 | CA-JVA | CA-JVA |
| SAP_CA_BC_IC_LND_FIN_JVA_PC | Joint Venture Accounting - Configuration | GJ33 |  | SIMG_MAS_0004 | Equity Types | 103185 | CA-JVA | CA-JVA |
| SAP_CA_BC_IC_LND_FIN_JVA_PC | Joint Venture Accounting - Configuration | GJ64 |  | SIMG_MAS_0007 | Cost Center Object Types | 103186 | CA-JVA | CA-JVA |
| SAP_CA_BC_IC_LND_FIN_JVA_PC | Joint Venture Accounting - Configuration | GJ58 |  | SIMG_MAS_0022 | Define Subclass A for Joint Interest Billing | 103181 | CA-JVA | CA-JVA |
| SAP_CA_BC_IC_LND_FIN_JVA_PC | Joint Venture Accounting - Configuration | GJ57 |  | SIMG_MAS_0021 | Define Class for Joint Interest Billing | 103180 | CA-JVA | CA-JVA |
| SAP_CA_BC_IC_LND_FIN_JVA_PC | Joint Venture Accounting - Configuration | GJ39 |  | SIMG_MAS_0010 | Define Billing Indicator | 103074 | CA-JVA | CA-JVA |
| SAP_CA_BC_IC_LND_FIN_JVA_PC | Joint Venture Accounting - Configuration | GJ21 |  | SIMG_MAS_0009 | Define Recovery Indicators | 102809 | CA-JVA | CA-JVA |
| SAP_CA_BC_IC_LND_FIN_JVA_PC | Joint Venture Accounting - Configuration | GJNR_RECID | GJNR_RECID_TRAN | GJNR_RECID | Maintain Record Index Number Range for Billing | 103259 | CA-JVA | CA-JVA |
| SAP_CA_BC_IC_LND_FIN_JVA_PC | Joint Venture Accounting - Configuration | GJ44 |  | SIMG_MAS_0012 | Net Profit Interest Partner Groups | 103155 | CA-JVA | CA-JVA |
| SAP_CA_BC_IC_LND_FIN_JVA_PC | Joint Venture Accounting - Configuration | GJRT |  | SIMG_MAS_0029 | Overhead Rate Types | 103151 | CA-JVA | CA-JVA |
| SAP_CA_BC_IC_LND_FIN_JVA_PC | Joint Venture Accounting - Configuration | GJNR_OHLIST | GJNR_OHLIST_TRAN | GJNR_OHLIST | Maintain Overhead List Number Range for Overhead Organizer | 103262 | CA-JVA | CA-JVA |
| SAP_CA_BC_IC_LND_FIN_JVA_PC | Joint Venture Accounting - Configuration | GJ73 | GJ73_TRAN | SIMG_PRO_0017 | Risk Labor Cost Elements | 103162 | CA-JVA | CA-JVA |
| SAP_CA_BC_IC_LND_FIN_JVA_PC | Joint Venture Accounting - Configuration | GJ61 |  | SIMG_MAS_0011 | Clearing Procedures | 103075 | CA-JVA | CA-JVA |
| SAP_CA_BC_IC_LND_FIN_JVA_PC | Joint Venture Accounting - Configuration | GJNR_CUTBACK | GJNR_CUTBACK_TRAN | GJNR_CUTBACK | Maintain Cutback Number Range | 103258 | CA-JVA | CA-JVA |
| SAP_CA_BC_IC_LND_FIN_JVA_PC | Joint Venture Accounting - Configuration | GJ74 | GJ74_TRAN | SIMG_PRO_0018 | Stepped Rate Rules | 103163 | CA-JVA | CA-JVA |
| SAP_CA_BC_IC_LND_FIN_JVA_PC | Joint Venture Accounting - Configuration | GJ47 | GJ47_TRAN | SIMG_PRO_0002 | Posting Methods | 103157 | CA-JVA | CA-JVA |
| SAP_CA_BC_IC_LND_FIN_JVA_PC | Joint Venture Accounting - Configuration | GJNR_OHKEY | GJNR_OHKEY_TRAN | GJNR_OHKEY | Maintain Overhead Key Number Range for Overhead Organizer | 103261 | CA-JVA | CA-JVA |
| SAP_CA_BC_IC_LND_FIN_JVA_PC | Joint Venture Accounting - Configuration | GJVS |  | SIMG_BIL_0014 | Supplemental Detail Sets | 103428 | CA-JVA | CA-JVA |
| SAP_CA_BC_IC_LND_FIN_JVA_PC | Joint Venture Accounting - Configuration | GJVB |  | SIMG_BIL_0016 | Billing Formats for Joint Venture Partner Billing | 103324 | CA-JVA | CA-JVA |
| SAP_CA_BC_IC_LND_FIN_JVA_PC | Joint Venture Accounting - Configuration | GJIC1 | GJIC1_TRAN | SIMG_MAS_0030 | Interest Calculation Groups | 103427 | CA-JVA | CA-JVA |
| SAP_CA_BC_IC_LND_FIN_JVA_PC | Joint Venture Accounting - Configuration | GJNR_OHCHAR | GJNR_OHCHAR_TRAN | GJNR_OHCHAR | Maintain Overhead Character Key Number Range for Overhead Organizer | 103260 | CA-JVA | CA-JVA |
| SAP_CA_BC_IC_LND_FIN_JVA_PC | Joint Venture Accounting - Configuration | GJE6 |  | SIMG_BIL_0001 | Mapping Billing Indicators to Service Codes | 103377 | CA-JVA | CA-JVA |
| SAP_CA_BC_IC_LND_FIN_JVA_PC | Joint Venture Accounting - Configuration | GJCS | GJCS_TRAN | SIMG_PRO_0004 | RI Manipulation Rules | 103342 | CA-JVA | CA-JVA |
| SAP_CA_BC_IC_LND_FIN_JVA_PC | Joint Venture Accounting - Configuration | GJBL | GJBL_TRAN | SIMG_BIL_0025 | Output Control Framework: Maintain Billing Layout | 103340 | CA-JVA | CA-JVA |
| SAP_CA_BC_IC_LND_FIN_JVA_PC | Joint Venture Accounting - Configuration | GJB2 |  | SIMG_BIL_0019 | Recovery Indicators for Supplemental Driver | 103432 | CA-JVA | CA-JVA |
| SAP_CA_BC_IC_LND_FIN_JVA_PC | Joint Venture Accounting - Configuration | GJB1 |  | SIMG_BIL_0017 | Billing Indicators for Supplemental Driver | 103429 | CA-JVA | CA-JVA |
| SAP_CA_BC_IC_LND_FIN_JVA_PC | Joint Venture Accounting - Configuration | GJ80 |  | SIMG_BIL_0002 | Mapping Accounts to JIB Classes for AFE's | 103336 | CA-JVA | CA-JVA |
| SAP_CA_BC_IC_LND_FIN_JVA_PC | Joint Venture Accounting - Configuration | GJ69 |  | SIMG_BIL_0005 | Mapping JIB Subclasses to Accounts | 103339 | CA-JVA | CA-JVA |
| SAP_CA_BC_IC_LND_FIN_JVA_PC | Joint Venture Accounting - Configuration | GJ52 | GJ52_TRAN | SIMG_NOP_0001 | JV Non-Operated Billing Form | 103376 | CA-JVA | CA-JVA |
| SAP_CA_BC_IC_LND_FIN_JVA_PC | Joint Venture Accounting - Configuration | GJ45 | GJ45_TRAN | SIMG_PRO_0001 | Processes | 103341 | CA-JVA | CA-JVA |
| SAP_CA_BC_IC_LND_FIN_JVA_PC | Joint Venture Accounting - Configuration | GJ81 |  | SIMG_BIL_0012 | Define Billing Structure | 103320 | CA-JVA | CA-JVA |
| SAP_CA_BC_IC_LND_FIN_JVA_PC | Joint Venture Accounting - Configuration | GJ68 |  | SIMG_BIL_0004 | Mapping JIB Classes and Accounts to Overwrite Classes | 103338 | CA-JVA | CA-JVA |
| SAP_CA_BC_IC_LND_FIN_JVA_PC | Joint Venture Accounting - Configuration | GJB4 |  | SIMG_BIL_0021 | JVA Cost Center Types | 103434 | CA-JVA | CA-JVA |
| SAP_CA_BC_IC_LND_FIN_JVA_PC | Joint Venture Accounting - Configuration | GJB3 |  | SIMG_BIL_0020 | JVA Project Types | 103433 | CA-JVA | CA-JVA |
| SAP_CA_BC_IC_LND_FIN_JVA_PC | Joint Venture Accounting - Configuration | GJ67 |  | SIMG_BIL_0003 | Mapping Accounts to JIB Classes for Non-AFEs | 103337 | CA-JVA | CA-JVA |
| SAP_CA_BC_IC_LND_FIN_JVA_PC | Joint Venture Accounting - Configuration | GJ40 | GJ40_TRAN | SIMG_BIL_0018 | Accounts for Supplemental Driver | 103430 | CA-JVA | CA-JVA |
| SAP_CA_BC_IC_LND_FIN_JVA_PC | Joint Venture Accounting - Configuration | GJ37 |  | SIMG_MAS_0017 | Funding Group Assignment | 103378 | CA-JVA | CA-JVA |
| SAP_CA_BC_IC_LND_FIN_JVA_PC | Joint Venture Accounting - Configuration | GJ35 |  | SIMG_MAS_0016 | Bank Accounts | 103347 | CA-JVA | CA-JVA |
| SAP_CA_BC_IC_LND_FIN_JVA_PC | Joint Venture Accounting - Configuration | GJB6 |  | SIMG_BIL_0023 | Driver Protocols | 103431 | CA-JVA | CA-JVA |
| SAP_CA_BC_IC_LND_FIN_JVA_PC | Joint Venture Accounting - Configuration | GJ85_J9O |  | SIMG_GJ85_J9O | Catastrophe Overhead Offset Account | 100297 | CA-JVA | CA-JVA |
| SAP_CA_BC_IC_LND_FIN_JVA_PC | Joint Venture Accounting - Configuration | GJ36 |  | SIMG_MAS_0015 | Funding Groups | 103189 | CA-JVA | CA-JVA |
| SAP_CA_BC_IC_LND_FIN_JVA_PC | Joint Venture Accounting - Configuration | GJ24 |  | SIMG_MAS_0003 | Define Venture Class | 102960 | CA-JVA | CA-JVA |
| SAP_CA_BC_IC_LND_FIN_JVA_PC | Joint Venture Accounting - Configuration | GJ85_JPA |  | SIMG_GJ85_JPA | Payroll Burden Clearing Adjustment | 100297 | CA-JVA | CA-JVA |
| SAP_CA_BC_IC_LND_FIN_JVA_PC | Joint Venture Accounting - Configuration | GJ85_JIO |  | SIMG_GJ85_JIO | International Overhead Offset Account | 100297 | CA-JVA | CA-JVA |
| SAP_CA_BC_IC_LND_FIN_JVA_PC | Joint Venture Accounting - Configuration | GJ85_J7O |  | SIMG_GJ85_J7O | Exploration Overhead Offset Account | 100297 | CA-JVA | CA-JVA |
| SAP_CA_BC_IC_LND_FIN_JVA_PC | Joint Venture Accounting - Configuration | GJ85_J7E |  | SIMG_GJ85_J7E | Exploration Overhead Expense Account | 100297 | CA-JVA | CA-JVA |
| SAP_CA_BC_IC_LND_FIN_JVA_PC | Joint Venture Accounting - Configuration | GJ85_JPE |  | SIMG_GJ85_JPE | Payroll Burden Clearing Expense Account | 100297 | CA-JVA | CA-JVA |
| SAP_CA_BC_IC_LND_FIN_JVA_PC | Joint Venture Accounting - Configuration | GJ85_J9E |  | SIMG_GJ85_J9E | Catastrophe Overhead Expense Account | 100297 | CA-JVA | CA-JVA |
| SAP_CA_BC_IC_LND_FIN_JVA_PC | Joint Venture Accounting - Configuration | GJ85_J8E |  | SIMG_GJ85_J8E | Capital Drilling Overhead Expense - Can. | 100297 | CA-JVA | CA-JVA |
| SAP_CA_BC_IC_LND_FIN_JVA_PC | Joint Venture Accounting - Configuration | GJ85_J6O |  | SIMG_GJ85_J6O | Construction Overhead Offset Account | 100297 | CA-JVA | CA-JVA |
| SAP_CA_BC_IC_LND_FIN_JVA_PC | Joint Venture Accounting - Configuration | GJ85_J6E |  | SIMG_GJ85_J6E | Construction Overhead Expense Account | 100297 | CA-JVA | CA-JVA |
| SAP_CA_BC_IC_LND_FIN_JVA_PC | Joint Venture Accounting - Configuration | S_ER9_11001274 | S_ER9_11001274_TRAN | SIMG_GJ85_JPE | Payroll Burden Clearing Expense Account | 100297 | CA-JVA | CA-JVA |
| SAP_CA_BC_IC_LND_FIN_JVA_PC | Joint Venture Accounting - Configuration | S_ER9_11001273 | S_ER9_11001273_TRAN | SIMG_GJ85_JPA | Payroll Burden Clearing Adjustment | 100297 | CA-JVA | CA-JVA |
| SAP_CA_BC_IC_LND_FIN_JVA_PC | Joint Venture Accounting - Configuration | GJ83_JVB |  | SIMG_GJ83_JVB | Cutback Tax Suspense Gross | 100297 | CA-JVA | CA-JVA |
| SAP_CA_BC_IC_LND_FIN_JVA_PC | Joint Venture Accounting - Configuration | S_ER9_11001232 | S_ER9_11001232_TRAN | SIMG_GJ83_JV1 | Cutback - Tax Clearing Account | 100297 | CA-JVA | CA-JVA |
| SAP_CA_BC_IC_LND_FIN_JVA_PC | Joint Venture Accounting - Configuration | GJ83_JV7 |  | SIMG_GJ83_JV7 | Interest Charged in JV Bank Transfers | 100297 | CA-JVA | CA-JVA |
| SAP_CA_BC_IC_LND_FIN_JVA_PC | Joint Venture Accounting - Configuration | S_ER9_11001239 | S_ER9_11001239_TRAN | SIMG_GJ83_JV8 | GR/IR Shadow Account | 100297 | CA-JVA | CA-JVA |
| SAP_CA_BC_IC_LND_FIN_JVA_PC | Joint Venture Accounting - Configuration | S_ER9_11001235 | S_ER9_11001235_TRAN | SIMG_GJ83_JV4 | Net Expense Account for Net Profit Int. | 100297 | CA-JVA | CA-JVA |
| SAP_CA_BC_IC_LND_FIN_JVA_PC | Joint Venture Accounting - Configuration | S_ER9_11001234 | S_ER9_11001234_TRAN | SIMG_GJ83_JV3 | Misc. Income for Net Profit Interests | 100297 | CA-JVA | CA-JVA |
| SAP_CA_BC_IC_LND_FIN_JVA_PC | Joint Venture Accounting - Configuration | S_ER9_11001233 | S_ER9_11001233_TRAN | SIMG_GJ83_JV2 | Non-Op Billing: Acct for Document Split | 100297 | CA-JVA | CA-JVA |
| SAP_CA_BC_IC_LND_FIN_JVA_PC | Joint Venture Accounting - Configuration | GJ83_JV6 |  | SIMG_GJ83_JV6 | Interventure Account for Balanced BbV | 100297 | CA-JVA | CA-JVA |
| SAP_CA_BC_IC_LND_FIN_JVA_PC | Joint Venture Accounting - Configuration | GJ83_JV5 |  | SIMG_GJ83_JV5 | Misc. Income Holding for Net Profit Int. | 100297 | CA-JVA | CA-JVA |
| SAP_CA_BC_IC_LND_FIN_JVA_PC | Joint Venture Accounting - Configuration | GJ83_JV4 |  | SIMG_GJ83_JV4 | Net Expense Account for Net Profit Int. | 100297 | CA-JVA | CA-JVA |
| SAP_CA_BC_IC_LND_FIN_JVA_PC | Joint Venture Accounting - Configuration | GJ83_JV3 |  | SIMG_GJ83_JV3 | Misc. Income for Net Profit Interests | 100297 | CA-JVA | CA-JVA |
| SAP_CA_BC_IC_LND_FIN_JVA_PC | Joint Venture Accounting - Configuration | GJ83_JV2 |  | SIMG_GJ83_JV2 | Non-Op Billing: Acct for Document Split | 100297 | CA-JVA | CA-JVA |
| SAP_CA_BC_IC_LND_FIN_JVA_PC | Joint Venture Accounting - Configuration | GJ83_JV1 |  | SIMG_GJ83_JV1 | Cutback - Tax Clearing Account | 100297 | CA-JVA | CA-JVA |
| SAP_CA_BC_IC_LND_FIN_JVA_PC | Joint Venture Accounting - Configuration | S_ER9_11001275 | S_ER9_11001275_TRAN | SIMG_GJ85_JPO | Payroll Burden Clearing Offset Account | 100297 | CA-JVA | CA-JVA |
| SAP_CA_BC_IC_LND_FIN_JVA_PC | Joint Venture Accounting - Configuration | S_ER9_11001272 | S_ER9_11001272_TRAN | SIMG_GJ85_JIO | International Overhead Offset Account | 100297 | CA-JVA | CA-JVA |
| SAP_CA_BC_IC_LND_FIN_JVA_PC | Joint Venture Accounting - Configuration | GJ85_J1O |  | SIMG_GJ85_J1O | % Prod. (U.S.), % (Can.) Overhead Offset | 100297 | CA-JVA | CA-JVA |
| SAP_CA_BC_IC_LND_FIN_JVA_PC | Joint Venture Accounting - Configuration | GJ85_J1E |  | SIMG_GJ85_J1E | % Prod. (U.S.), % (Can.) Overhead Exp. | 100297 | CA-JVA | CA-JVA |
| SAP_CA_BC_IC_LND_FIN_JVA_PC | Joint Venture Accounting - Configuration | GJ83_JVX |  | SIMG_GJ83_JVX | JV Exchange Rate Differences | 100297 | CA-JVA | CA-JVA |
| SAP_CA_BC_IC_LND_FIN_JVA_PC | Joint Venture Accounting - Configuration | GJ83_JVE |  | SIMG_GJ83_JVE | Funding Write-Off | 100297 | CA-JVA | CA-JVA |
| SAP_CA_BC_IC_LND_FIN_JVA_PC | Joint Venture Accounting - Configuration | GJ83_JVC |  | SIMG_GJ83_JVC | Offset Acct Equity Change - Adjustment | 100297 | CA-JVA | CA-JVA |
| SAP_CA_BC_IC_LND_FIN_JVA_PC | Joint Venture Accounting - Configuration | GJ83_JVA |  | SIMG_GJ83_JVA | Cutback Tax Expense Account | 100297 | CA-JVA | CA-JVA |
| SAP_CA_BC_IC_LND_FIN_JVA_PC | Joint Venture Accounting - Configuration | GJ83_JV8 |  | SIMG_GJ83_JV8 | GR/IR Shadow Account | 100297 | CA-JVA | CA-JVA |
| SAP_CA_BC_IC_LND_FIN_JVA_PC | Joint Venture Accounting - Configuration | S_ER9_11001271 | S_ER9_11001271_TRAN | SIMG_GJ85_JIE | International Overhead Expense Account | 100297 | CA-JVA | CA-JVA |
| SAP_CA_BC_IC_LND_FIN_JVA_PC | Joint Venture Accounting - Configuration | GJ85_J3E |  | SIMG_GJ85_J3E | CFR Prod. (U.S.) Overhead Expense | 100297 | CA-JVA | CA-JVA |
| SAP_CA_BC_IC_LND_FIN_JVA_PC | Joint Venture Accounting - Configuration | GJ85_J2O |  | SIMG_GJ85_J2O | % Development (U.S.) Overhead Offset | 100297 | CA-JVA | CA-JVA |
| SAP_CA_BC_IC_LND_FIN_JVA_PC | Joint Venture Accounting - Configuration | GJ85_J2E |  | SIMG_GJ85_J2E | % Development (U.S) Overhead Expense | 100297 | CA-JVA | CA-JVA |
| SAP_CA_BC_IC_LND_FIN_JVA_PC | Joint Venture Accounting - Configuration | S_ER9_11001241 | S_ER9_11001241_TRAN | SIMG_GJ83_JVB | Cutback Tax Suspense Gross | 100297 | CA-JVA | CA-JVA |
| SAP_CA_BC_IC_LND_FIN_JVA_PC | Joint Venture Accounting - Configuration | S_ER9_11001240 | S_ER9_11001240_TRAN | SIMG_GJ83_JVA | Cutback Tax Expense Account | 100297 | CA-JVA | CA-JVA |
| SAP_CA_BC_IC_LND_FIN_JVA_PC | Joint Venture Accounting - Configuration | S_ER9_11001238 | S_ER9_11001238_TRAN | SIMG_GJ83_JV7 | Interest Charged in JV Bank Transfers | 100297 | CA-JVA | CA-JVA |
| SAP_CA_BC_IC_LND_FIN_JVA_PC | Joint Venture Accounting - Configuration | S_ER9_11001236 | S_ER9_11001236_TRAN | SIMG_GJ83_JV5 | Misc. Income Holding for Net Profit Int. | 100297 | CA-JVA | CA-JVA |
| SAP_CA_BC_IC_LND_FIN_JVA_PC | Joint Venture Accounting - Configuration | S_ER9_11001257 | S_ER9_11001257_TRAN | SIMG_GJ85_J2E | % Development (U.S) Overhead Expense | 100297 | CA-JVA | CA-JVA |
| SAP_CA_BC_IC_LND_FIN_JVA_PC | Joint Venture Accounting - Configuration | S_ER9_11001256 | S_ER9_11001256_TRAN | SIMG_GJ85_J1O | % Prod. (U.S.), % (Can.) Overhead Offset | 100297 | CA-JVA | CA-JVA |
| SAP_CA_BC_IC_LND_FIN_JVA_PC | Joint Venture Accounting - Configuration | S_ER9_11001255 | S_ER9_11001255_TRAN | SIMG_GJ85_J1E | % Prod. (U.S.), % (Can.) Overhead Exp. | 100297 | CA-JVA | CA-JVA |
| SAP_CA_BC_IC_LND_FIN_JVA_PC | Joint Venture Accounting - Configuration | S_ER9_11001250 | S_ER9_11001250_TRAN | SIMG_GJ83_JV6 | Interventure Account for Balanced BbV | 100297 | CA-JVA | CA-JVA |
| SAP_CA_BC_IC_LND_FIN_JVA_PC | Joint Venture Accounting - Configuration | S_ER9_11001245 | S_ER9_11001245_TRAN | SIMG_GJ83_JVX | JV Exchange Rate Differences | 100297 | CA-JVA | CA-JVA |
| SAP_CA_BC_IC_LND_FIN_JVA_PC | Joint Venture Accounting - Configuration | S_ER9_11001244 | S_ER9_11001244_TRAN | SIMG_GJ83_JVE | Funding Write-Off | 100297 | CA-JVA | CA-JVA |
| SAP_CA_BC_IC_LND_FIN_JVA_PC | Joint Venture Accounting - Configuration | S_ER9_11001243 | S_ER9_11001243_TRAN | SIMG_GJ83_JVD | Funding Corp.Pay Actualization | 100297 | CA-JVA | CA-JVA |
| SAP_CA_BC_IC_LND_FIN_JVA_PC | Joint Venture Accounting - Configuration | S_ER9_11001242 | S_ER9_11001242_TRAN | SIMG_GJ83_JVC | Offset Acct Equity Change - Adjustment | 100297 | CA-JVA | CA-JVA |
| SAP_CA_BC_IC_LND_FIN_JVA_PC | Joint Venture Accounting - Configuration | S_ER9_11001267 | S_ER9_11001267_TRAN | SIMG_GJ85_J8E | Capital Drilling Overhead Expense - Can. | 100297 | CA-JVA | CA-JVA |
| SAP_CA_BC_IC_LND_FIN_JVA_PC | Joint Venture Accounting - Configuration | S_ER9_11001266 | S_ER9_11001266_TRAN | SIMG_GJ85_J7O | Exploration Overhead Offset Account | 100297 | CA-JVA | CA-JVA |
| SAP_CA_BC_IC_LND_FIN_JVA_PC | Joint Venture Accounting - Configuration | S_ER9_11001265 | S_ER9_11001265_TRAN | SIMG_GJ85_J7E | Exploration Overhead Expense Account | 100297 | CA-JVA | CA-JVA |
| SAP_CA_BC_IC_LND_FIN_JVA_PC | Joint Venture Accounting - Configuration | S_ER9_11001264 | S_ER9_11001264_TRAN | SIMG_GJ85_J6O | Construction Overhead Offset Account | 100297 | CA-JVA | CA-JVA |
| SAP_CA_BC_IC_LND_FIN_JVA_PC | Joint Venture Accounting - Configuration | S_ER9_11001263 | S_ER9_11001263_TRAN | SIMG_GJ85_J6E | Construction Overhead Expense Account | 100297 | CA-JVA | CA-JVA |
| SAP_CA_BC_IC_LND_FIN_JVA_PC | Joint Venture Accounting - Configuration | S_ER9_11001262 | S_ER9_11001262_TRAN | SIMG_GJ85_J4O | CFR Drilling (U.S) Overhead Offset Acct | 100297 | CA-JVA | CA-JVA |
| SAP_CA_BC_IC_LND_FIN_JVA_PC | Joint Venture Accounting - Configuration | S_ER9_11001261 | S_ER9_11001261_TRAN | SIMG_GJ85_J4E | CFR Drilling (U.S) Overhead Expense | 100297 | CA-JVA | CA-JVA |
| SAP_CA_BC_IC_LND_FIN_JVA_PC | Joint Venture Accounting - Configuration | S_ER9_11001258 | S_ER9_11001258_TRAN | SIMG_GJ85_J2O | % Development (U.S.) Overhead Offset | 100297 | CA-JVA | CA-JVA |
| SAP_CA_BC_IC_LND_FIN_JVA_PC | Joint Venture Accounting - Configuration | GJ85_J4O |  | SIMG_GJ85_J4O | CFR Drilling (U.S) Overhead Offset Acct | 100297 | CA-JVA | CA-JVA |
| SAP_CA_BC_IC_LND_FIN_JVA_PC | Joint Venture Accounting - Configuration | GJ85_J4E |  | SIMG_GJ85_J4E | CFR Drilling (U.S) Overhead Expense | 100297 | CA-JVA | CA-JVA |
| SAP_CA_BC_IC_LND_FIN_JVA_PC | Joint Venture Accounting - Configuration | GJ85_J3O |  | SIMG_GJ85_J3O | CFR Prod. (U.S.) Overhead Offset Acct | 100297 | CA-JVA | CA-JVA |
| SAP_CA_BC_IC_LND_FIN_JVA_PC | Joint Venture Accounting - Configuration | S_ER9_11001269 | S_ER9_11001269_TRAN | SIMG_GJ85_J9E | Catastrophe Overhead Expense Account | 100297 | CA-JVA | CA-JVA |
| SAP_CA_BC_IC_LND_FIN_JVA_PC | Joint Venture Accounting - Configuration | S_ER9_11001268 | S_ER9_11001268_TRAN | SIMG_GJ85_J8O | Capital Drilling Overhead Offset - Canada | 100297 | CA-JVA | CA-JVA |
| SAP_CA_BC_IC_LND_FIN_JVA_PC | Joint Venture Accounting - Configuration | S_ER9_11001260 | S_ER9_11001260_TRAN | SIMG_GJ85_J3O | CFR Prod. (U.S.) Overhead Offset Acct | 100297 | CA-JVA | CA-JVA |
| SAP_CA_BC_IC_LND_FIN_JVA_PC | Joint Venture Accounting - Configuration | S_ER9_11001259 | S_ER9_11001259_TRAN | SIMG_GJ85_J3E | CFR Prod. (U.S.) Overhead Expense | 100297 | CA-JVA | CA-JVA |
| SAP_CA_BC_IC_LND_FIN_JVA_PC | Joint Venture Accounting - Configuration | GJ85_JPO |  | SIMG_GJ85_JPO | Payroll Burden Clearing Offset Account | 100297 | CA-JVA | CA-JVA |
| SAP_CA_BC_IC_LND_FIN_JVA_PC | Joint Venture Accounting - Configuration | GJ85_JIE |  | SIMG_GJ85_JIE | International Overhead Expense Account | 100297 | CA-JVA | CA-JVA |
| SAP_CA_BC_IC_LND_FIN_JVA_PC | Joint Venture Accounting - Configuration | GJ85_J8O |  | SIMG_GJ85_J8O | Capital Drilling Overhead Offset - Canada | 100297 | CA-JVA | CA-JVA |
| SAP_CA_BC_IC_LND_FIN_JVA_PC | Joint Venture Accounting - Configuration | GJ83_JVD |  | SIMG_GJ83_JVD | Funding Corp.Pay Actualization | 100297 | CA-JVA | CA-JVA |
| SAP_CA_BC_IC_LND_FIN_JVA_PC | Joint Venture Accounting - Configuration | S_ER9_11001270 | S_ER9_11001270_TRAN | SIMG_GJ85_J9O | Catastrophe Overhead Offset Account | 100297 | CA-JVA | CA-JVA |
| SAP_PS_BC_WRKFLW_CONF_PC | Enterprise Projects - Workflow Configuration | F6158 | F6158_TRAN |  |  |  | PPM-SCL-STR |  |
| SAP_CA_BC_IC_LND_FIN_BP_PH_PC | Business Place for Philippines - Configuration | S_ER9_11002323 | S_ER9_11002323_TRAN | OFFDOCNO_PH_01 | Define Business Places for Philippines | 105727 | FI-LOC-FI-PH | FI-LOC-FI-PH |
| SAP_CA_BC_IC_LND_FIN_BP_PH_PC | Business Place for Philippines - Configuration | S_ER9_11001463 | S_ER9_11001463_TRAN | PRNR | Define Internal Number Ranges for Payment Receipts | 103389 | FI-LOC-FI-PH | FI-LOC-PR |
| SAP_CA_BC_IC_LND_FIN_BP_PH_PC | Business Place for Philippines - Configuration | GLO_DEFINE_BUPLA_PH |  | OFFDOCNO_PH_01 | Define Business Places for Philippines | 105727 | FI-LOC-FI-PH | FI-LOC-FI-PH |
| SAP_CA_BC_IC_LND_FIN_BP_PH_PC | Business Place for Philippines - Configuration | PRNR |  | PRNR | Define Internal Number Ranges for Payment Receipts | 103389 | FI-LOC-FI-PH | FI-LOC-PR |
| SAP_CA_BC_IC_LND_FIN_SRF3_PC | Statutory Reporting (Cross Country) - Configuration | S_ER9_11002015 | S_ER9_11002015_TRAN | FIVC_CF_VERSION_ACR | Define Cash Flow Statement Versions for Several Countries/Regions | 105331 | FI-LOC-IAM | FI-LOC-CF |
| SAP_CA_BC_IC_LND_FIN_SRF3_PC | Statutory Reporting (Cross Country) - Configuration | S_ER9_11002335 | S_ER9_11002335_TRAN | FIVC_OFFS_GROUP_DRC | Define Field Sets for Grouping for Several Countries/Regions | 105762 | FI-LOC-IAM | FI-LOC-CF |
| SAP_CA_BC_IC_LND_FIN_SRF3_PC | Statutory Reporting (Cross Country) - Configuration | S_ER9_11002079 | S_ER9_11002079_TRAN | FIVC_OFFS_VERS_A_CE | Define Offsetting Account Determination Versions for Several Countries/Rgns | 105370 | FI-LOC-IAM | FI-LOC-CF |
| SAP_CA_BC_IC_LND_FIN_SRF3_PC | Statutory Reporting (Cross Country) - Configuration | S_ER9_11002017 | S_ER9_11002017_TRAN | FIVC_OFFS_DET_ACR | Activate Online Offsetting Account Determination for Several Countries/Rgns | 105333 | FI-LOC-IAM | FI-LOC-CF |
| SAP_CA_BC_IC_LND_OVS_PC | Online Validation Service (Cross Country) - Configuration | OVS_V_CHECKID | OVS_V_CHECKID_TRAN |  |  |  | CA-GTF-CSC-OVF |  |
| SAP_CA_BC_IC_LND_OVS_PC | Online Validation Service (Cross Country) - Configuration | OVS_V_CHKRSLT | OVS_V_CHKRSLT_TRAN |  |  |  | CA-GTF-CSC-OVF |  |
| SAP_CA_BC_IC_LND_OVS_PC | Online Validation Service (Cross Country) - Configuration | OVS_V_SPOTACTIV | OVS_V_SPOTACTIV_TRAN |  |  |  | CA-GTF-CSC-OVF |  |
| SAP_CA_BC_IC_LND_OVS_PC | Online Validation Service (Cross Country) - Configuration | OVS_V_VIES | OVS_V_VIES_TRAN |  |  |  | CA-GTF-CSC-OVF |  |
| SAP_CA_BC_IC_LND_OVS_PC | Online Validation Service (Cross Country) - Configuration | S_SAL_71000070 | S_SAL_71000070_TRAN | OVF_VC_CHECKS_ABA | Maintain Online Validation Checks | 105630 | CA-GTF-CSC-OVF | CA-GTF-CSC-OVF |
| SAP_CA_BC_IC_LND_OVS_PC | Online Validation Service (Cross Country) - Configuration | OVS_CHECKS | OVS_CHECKS_TRAN | OVF_VC_CHECKS_ABA | Maintain Online Validation Checks | 105630 | CA-GTF-CSC-OVF | CA-GTF-CSC-OVF |
| SAP_CA_BC_IC_LND_BNK_SEPA_PC | Bank - SEPA - Configuration | S_ER9_11000854 | S_ER9_11000854_TRAN | V_T005SEPA | Define Settings for SEPA Countries/Regions | 105423 | CA-BK-SEP | CA-BK |
| SAP_CA_BC_IC_LND_BNK_SEPA_PC | Bank - SEPA - Configuration | OY13 |  | V_T005SEPA | Define Settings for SEPA Countries/Regions | 105423 | CA-BK-SEP | CA-BK |
| SAP_CA_BC_IC_LND_BNK_SEPA_PC | Bank - SEPA - Configuration | S_E91_86000011 | S_E91_86000011_TRAN | SEPA_STATUS_CUST | Define Status Changes Not Permitted | 101304 | CA-BK-SEP | CA-BK-SEP |
| SAP_CA_BC_IC_LND_BNK_SEPA_PC | Bank - SEPA - Configuration | SEPA_STATUS_CUST |  | SEPA_STATUS_CUST | Define Status Changes Not Permitted | 101304 | CA-BK-SEP | CA-BK-SEP |
| SAP_CA_BC_IC_LND_BNK_SEPA_PC | Bank - SEPA - Configuration | S_E91_86000012 | S_E91_86000012_TRAN | SEPA_RC_CUST | Define Reason Code for Status Changes | 101305 | CA-BK-SEP | CA-BK-SEP |
| SAP_CA_BC_IC_LND_BNK_SEPA_PC | Bank - SEPA - Configuration | SEPA_RC_CUST |  | SEPA_RC_CUST | Define Reason Code for Status Changes | 101305 | CA-BK-SEP | CA-BK-SEP |
| SAP_CA_BC_IC_LND_BNK_SEPA_PC | Bank - SEPA - Configuration | V_SEPA_CUST |  | SEPA_CUST | Maintain SEPA Mandate Management: General Settings |  | CA-BK-SEP | CA-BK-SEP |
| SAP_CA_BC_IC_LND_BNK_SEPA_PC | Bank - SEPA - Configuration | S_SAL_71000125 | S_SAL_71000125_TRAN | SEPA_CUST | Maintain SEPA Mandate Management: General Settings |  | CA-BK-SEP | CA-BK-SEP |
| SAP_CA_BC_IC_LND_FIN_WT_ID_PC | Statutory Reporting WT for Indonesia - Configuration | S_ER9_11001741 | S_ER9_11001741_TRAN | ID_V_T059Z_CO | Assign Withholding Tax Keys to Withholding Tax Codes | 105911 | FI-LOC-FI-ID | FI-LOC-FI-ID |
| SAP_CA_BC_IC_LND_OIL_FLOG1_PC | Field Logistics Returns - Configuration | S_ER1_70000317 | S_ER1_70000317_TRAN | FLOG_V_RET_TMFUN | Maintain Team Functions for Handling Decision Notification | 104424 | CA-FL | CA-FL-RET |
| SAP_CA_BC_IC_LND_OIL_FLOG1_PC | Field Logistics Returns - Configuration | S_ER1_70000403 | S_ER1_70000403_TRAN | FLOGV_DF_QKANSUP | Maintain Default Handling Decision to Receive at Remote Location | 105769 | CA-FL | CA-FL |
| SAP_CA_BC_IC_LND_OIL_FLOG1_PC | Field Logistics Returns - Configuration | S_ER1_70000402 | S_ER1_70000402_TRAN | FLOGV_DF_QKANRET | Maintain Default Recommended Action to Initiate Returns | 105770 | CA-FL | CA-FL |
| SAP_CA_BC_IC_LND_OIL_FLOG1_PC | Field Logistics Returns - Configuration | S_ER1_70000182 | S_ER1_70000182_TRAN | FLOG_V_RT_SUPREC | Maintain Return Action | 103505 | CA-FL | CA-FL |
| SAP_CA_BC_IC_LND_PLM_DIR_PC | Document Management - Configuration | S_ALR_87008831 | S_ALR_87008831_TRAN | SIMG_VC_DVS10 | Define DMS Document Types | 101090 | PLM-WUI-OBJ-DMS | CA-DMS |
| SAP_CA_BC_IC_LND_PLM_DIR_PC | Document Management - Configuration | DC10 |  | SIMG_VC_DVS10 | Define DMS Document Types | 101090 | PLM-WUI-OBJ-DMS | CA-DMS |
| SAP_CORE_BC_BCT_BCA | Business Configuration - BC Set Activation | SCPR20PR | SCPR20PR_TRAN |  |  |  | BC-CUS-TOL-CST |  |
| SAP_CORE_BC_BCT_BCA | Business Configuration - BC Set Activation | SCPR20 | SCPR20_TRAN |  |  |  | BC-CUS-TOL-CST |  |
| SAP_CA_BC_IC_LND_EAM_ORD_PC | Maintenance Order Processing - Configuration | S_ER9_52002175 | S_ER9_52002175_TRAN | SIMG_EAM_USRSTS_ASGN | Define Phase Control Code for Maintenance Orders | 103676 | PM | PM-2CL |
| SAP_CA_BC_IC_LND_EAM_ORD_PC | Maintenance Order Processing - Configuration | S_ALR_87000713 | S_ALR_87000713_TRAN | SIMG_CFMENUOLIAOIO4 | Default Values for Maintenance Activity Type for Each Order Type | 103650 | PM | PM-2CL |
| SAP_CA_BC_IC_LND_EAM_ORD_PC | Maintenance Order Processing - Configuration | S_ALR_87000090 | S_ALR_87000090_TRAN | OLIAV_TPMP_A | Default Values for Task List Data and Profile Assignments | 103478 | PM | PM-2CL |
| SAP_CA_BC_IC_LND_EAM_ORD_PC | Maintenance Order Processing - Configuration | S_ALR_87000110 | S_ALR_87000110_TRAN | OLIAV_TPEXT_PM | Create Default Value Profiles for External Procurement | 103477 | PM | PM-2CL |
| SAP_CA_BC_IC_LND_EAM_ORD_PC | Maintenance Order Processing - Configuration | S_ALR_87000736 | S_ALR_87000736_TRAN | SIMG_CFMENUOLIAOIOE | Define Change Documents, Collective Purchase Requisition, MRP relevance | 103825 | PM | PM-2CL |
| SAP_CA_BC_IC_LND_EAM_ORD_PC | Maintenance Order Processing - Configuration | S_ALR_87000728 | S_ALR_87000728_TRAN | SIMG_CFMENUOLIAOIO3 | Define Maintenance Activity Types | 103652 | PM | PM-2CL |
| SAP_CA_BC_IC_LND_EAM_ORD_PC | Maintenance Order Processing - Configuration | S_ALR_87000732 | S_ALR_87000732_TRAN | SIMG_CFMENUOLIAOIO5 | Assign Valid Maintenance Activity Types to Maintenance Order Types | 103651 | PM | PM-2CL |
| SAP_CA_BC_IC_LND_EAM_ORD_PC | Maintenance Order Processing - Configuration | OIO5 |  | SIMG_CFMENUOLIAOIO5 | Assign Valid Maintenance Activity Types to Maintenance Order Types | 103651 | PM | PM-2CL |
| SAP_CA_BC_IC_LND_EAM_ORD_PC | Maintenance Order Processing - Configuration | OIO4 |  | SIMG_CFMENUOLIAOIO4 | Default Values for Maintenance Activity Type for Each Order Type | 103650 | PM | PM-2CL |
| SAP_CA_BC_IC_LND_EAM_ORD_PC | Maintenance Order Processing - Configuration | S_ER9_52002553 | S_ER9_52002553_TRAN | EAM_ORDERSETTLE | Assign Valid Settlement Profiles to Order Types | 104120 | PM | PM-WOC-MO-2CL |
| SAP_CA_BC_IC_LND_EAM_ORD_PC | Maintenance Order Processing - Configuration | S_ALR_87000323 | S_ALR_87000323_TRAN | SIMG_CFMENUOLIAOIOC | Set Scheduling Parameters | 104234 | PM | PM-2CL |
| SAP_CA_BC_IC_LND_EAM_ORD_PC | Maintenance Order Processing - Configuration | OPU7 |  | SIMG_CFMENUOLIAOIOC | Set Scheduling Parameters | 104234 | PM | PM-2CL |
| SAP_CA_BC_IC_LND_EAM_ORD_PC | Maintenance Order Processing - Configuration | S_ER9_52002241 | S_ER9_52002241_TRAN | SIMG_MO_FLEX_WF | Define Approval Settings for Maintenance Orders | 103764 | PM | PM-2CL |
| SAP_CA_BC_IC_LND_EAM_ORD_PC | Maintenance Order Processing - Configuration | DIWPSC4 |  | DIWPSC4_1 | Maintain Maintenance Event Type | 104802 | PM | PM-WOC-MO-2CL |
| SAP_CA_BC_IC_LND_EAM_ORD_PC | Maintenance Order Processing - Configuration | S_ER9_52002978 | S_ER9_52002978_TRAN | DIWPSC4_1 | Maintain Maintenance Event Type | 104802 | PM | PM-WOC-MO-2CL |
| SAP_CA_BC_IC_LND_EAM_ORD_PC | Maintenance Order Processing - Configuration | S_ER9_52002931 | S_ER9_52002931_TRAN | EAM_PROCMLSTAS | Define Assignment Rules for Procurement Milestones | 105360 | PM | PM-2CL |
| SAP_CA_BC_IC_LND_EAM_ORD_PC | Maintenance Order Processing - Configuration | S_ALR_87000841 | S_ALR_87000841_TRAN | OLIA_V_TRUG | Define Causes for Variances | 105486 | PM | PM-2CL |
| SAP_CA_BC_IC_LND_EAM_ORD_PC | Maintenance Order Processing - Configuration | S_ALR_87000758 | S_ALR_87000758_TRAN | OLIA_V_160_M_PM | Message Control | 105530 | PM | PM-2CL |
| SAP_CA_BC_IC_LND_EAM_ORD_PC | Maintenance Order Processing - Configuration | S_ER9_52003260 | S_ER9_52003260_TRAN | EAM_REWORK_PARAM | Define Order Parameters for Rework Analysis | 105682 | PM | PM-WOC-2CL |
| SAP_CA_BC_IC_LND_EAM_ORD_PC | Maintenance Order Processing - Configuration | S_ALR_87000127 | S_ALR_87000127_TRAN | OLIA_V_T350_BEZZT | Define Proposed Reference Time for Technical Completion | 105763 | PM | PM-2CL |
| SAP_CA_BC_IC_LND_EAM_ORD_PC | Maintenance Order Processing - Configuration | S_ER9_52003823 | S_ER9_52003823_TRAN | SIMG_EAMCONFCTRL | Define Control Parameters for Perform Maintenance Jobs | 105952 | PM | PM-2CL |
| SAP_CA_BC_IC_LND_EAM_ORD_PC | Maintenance Order Processing - Configuration | S_PLN_16000040 | S_PLN_16000040_TRAN | OLIA_IOCI_FCONV | Convert HTML Fields to SAP Fields | 106191 | PM | PM-WOC-MO-2CL |
| SAP_CA_BC_IC_LND_EAM_ORD_PC | Maintenance Order Processing - Configuration | S_PLN_16000042 | S_PLN_16000042_TRAN | OLIA_IOCI_FCON2 | Convert HTML Field Values | 106192 | PM | PM-WOC-MO-2CL |
| SAP_CA_BC_IC_LND_EAM_ORD_PC | Maintenance Order Processing - Configuration | S_PLN_62000211 | S_PLN_62000211_TRAN | OLIA_VC_TMW03 | Define Catalogs | 106216 | PM | PM-WOC-MO-2CL |
| SAP_CA_BC_IC_LND_EAM_ORD_PC | Maintenance Order Processing - Configuration | S_ER9_52004358 | S_ER9_52004358_TRAN | ORDER_V_T399I_EHS | Activate Integration with Environment, Health, and Safety | 106568 | PM | PM-2CL |
| SAP_CA_BC_IC_LND_EAM_ORD_PC | Maintenance Order Processing - Configuration | S_PLN_16000036 | S_PLN_16000036_TRAN | OLIA_IOCI_ORGU | Assign Catalog to Order Type | 106190 | PM | PM-WOC-MO-2CL |
| SAP_CA_BC_IC_LND_EAM_ORD_PC | Maintenance Order Processing - Configuration | S_ALR_87000028 | S_ALR_87000028_TRAN | SIMG_CFMENUOLIAOION | Configure Number Range for Order Types | 106461 | PM | PM-2CL |
| SAP_CA_BC_IC_LND_EAM_ORD_PC | Maintenance Order Processing - Configuration | OION |  | SIMG_CFMENUOLIAOION | Configure Number Range for Order Types | 106461 | PM | PM-2CL |
| SAP_CA_BC_IC_LND_EAM_ORD_PC | Maintenance Order Processing - Configuration | S_ER9_52001758 | S_ER9_52001758_TRAN | SIMG_CFMENUOLVT003O | Assign Number Range to Order Types | 106462 | PM | PM-2CL |
| SAP_CA_BC_IC_LND_FIN_BA0_PC | Bank Accounting - Configuration | S_P00_07000249 | S_P00_07000249_TRAN | FI_BL_EBS_VC_T028 | Make Global Settings for Electronic Bank Statement | 101024 | FI-BL | FI-BL-PT |
| SAP_CA_BC_IC_LND_FIN_BA0_PC | Bank Accounting - Configuration | S_ALR_87100694 | S_ALR_87100694_TRAN | FIAPPY_V_T042K | Define Accounts for Bank Charges (Japan) | 102624 | FI-BL | FI-AP-AP-B-2CL |
| SAP_CA_BC_IC_LND_FIN_BA0_PC | Bank Accounting - Configuration | S_ALR_87100693 | S_ALR_87100693_TRAN | FIAPPY_V_T042J | Define Bank Charges for Japan | 101223 | FI-BL | FI-AP-AP-B-2CL |
| SAP_CA_BC_IC_LND_FIN_BA0_PC | Bank Accounting - Configuration | S_ER9_11001803 | S_ER9_11001803_TRAN | V_FAR_PYMTCLGGRP | Define Payment Clearing Groups | 104096 | FI-BL | FI-BL-PT |
| SAP_CA_BC_IC_LND_FIN_BA0_PC | Bank Accounting - Configuration | S_ER9_11000107 | S_ER9_11000107_TRAN | V_FEB_REPRO_AVCO | Define Average Cost of Reprocessing | 103059 | FI-BL | FI-FIO-AR-2CL |
| SAP_CA_BC_IC_LND_FIN_BA0_PC | Bank Accounting - Configuration | S_ER9_11001317 | S_ER9_11001317_TRAN | EPIC_BR_ML_CONFG | Define Basic Settings for Bank Reconciliation | 103208 | FI-BL | FI-LOC-EPI-CN |
| SAP_CA_BC_IC_LND_FIN_BA0_PC | Bank Accounting - Configuration | S_ER9_11001563 | S_ER9_11001563_TRAN | FARVC_BSIMP_PSETS | Define Parameter Sets | 103635 | FI-BL | FI-BL-PT |
| SAP_CA_BC_IC_LND_FIN_BA0_PC | Bank Accounting - Configuration | S_ER9_11001038 | S_ER9_11001038_TRAN | FINS_AR_ML_COCD_SET | Set Target Accuracy at Company-Code Level |  | FI-BL | FI-FIO-AR-2CL |
| SAP_CA_BC_IC_LND_FIN_BA0_PC | Bank Accounting - Configuration | S_ER9_11001960 | S_ER9_11001960_TRAN | MFD_F5608 | Map Format Data for Incoming Files from Banks | 170010 | FI-BL | CA-GTF-CSC-DME |
| SAP_CA_BC_IC_LND_FIN_BA0_PC | Bank Accounting - Configuration | F5608 | F5608_03_TRAN |  |  |  | FI-BL |  |
| SAP_CA_BC_IC_LND_FIN_BA0_PC | Bank Accounting - Configuration | F6960 | F6960_TRAN |  |  |  | FI-BL |  |
| SAP_CA_BC_IC_LND_FIN_BA0_PC | Bank Accounting - Configuration | S_ER9_11000399 | S_ER9_11000399_03_TRAN | V_FAR_IPF_FORMAT | Configure Formats for Import |  | FI-BL | FI-BL-PT |
| SAP_CA_BC_IC_LND_FIN_BA0_PC | Bank Accounting - Configuration | MFD_F5608 |  | MFD_F5608 | Map Format Data for Incoming Files from Banks | 170010 | FI-BL | CA-GTF-CSC-DME |
| SAP_CA_BC_IC_LND_FIN_SR_AR_PC | Statutory Reporting for Argentina - Configuration | S_EBJ_45000295 | S_EBJ_45000295_TRAN | FIARV_TAXID | Specify Tax Class | 102746 | FI-LOC-FI-AR | FI-LOC-FI-AR |
| SAP_CA_BC_IC_LND_FIN_SR_AR_PC | Statutory Reporting for Argentina - Configuration | S_ALR_87004789 | S_ALR_87004789_TRAN | J_1AOFF_DOC_ASSIGN4 | Assign Official D.G.I. Document Types | 102747 | FI-LOC-FI-AR | FI-AR-AR-2CL |
| SAP_CA_BC_IC_LND_FIN_SR_AR_PC | Statutory Reporting for Argentina - Configuration | S_ALR_87004707 | S_ALR_87004707_TRAN | J_1AFOREIGN_PERSON4 | Maintain Identification Numbers for Foreign Persons | 106204 | FI-LOC-FI-AR | FI-AR-AR-2CL |
| SAP_CA_BC_IC_LND_FIN_SR_AR_PC | Statutory Reporting for Argentina - Configuration | S_ALR_87004783 | S_ALR_87004783_TRAN | J_1AOFF_TYPE_MAINT4 | Maintain Official D.G.I. Document Types | 106168 | FI-LOC-FI-AR | FI-AR-AR-2CL |
| SAP_CA_BC_IC_LND_FIN_SR_AR_PC | Statutory Reporting for Argentina - Configuration | S_AL0_19000055 | S_AL0_19000055_TRAN | OFFDOCNO_AR_006 | Define Print Authorization Codes | 102744 | FI-LOC-FI-AR | FI-LOC-LO-AR |
| SAP_CA_BC_IC_LND_FIN_SR_AR_PC | Statutory Reporting for Argentina - Configuration | S_EBS_44000040 | S_EBS_44000040_TRAN | V_1AOUM | Maintain Official Unit of Measure | 106212 | FI-LOC-FI-AR | FI-LOC-FI-AR |
| SAP_CA_BC_IC_LND_FIN_SR_AR_PC | Statutory Reporting for Argentina - Configuration | S_AC0_52000381 | S_AC0_52000381_TRAN | J_1APAYMN | Assign AFIP Payment Means to Payment Methods | 106213 | FI-LOC-FI-AR | FI-LOC-FI-AR |
| SAP_CA_BC_IC_LND_FIN_SR_AR_PC | Statutory Reporting for Argentina - Configuration | S_ALR_87003358 | S_ALR_87003358_TRAN | J_1ADISCOUNT_TYPE4 | Configure Automatic Generation of Cash Discount Documents | 106214 | FI-LOC-FI-AR | FI-AR-AR-2CL |
| SAP_CA_BC_IC_LND_FIN_SR_AR_PC | Statutory Reporting for Argentina - Configuration | S_ALR_87001497 | S_ALR_87001497_TRAN | J_1A_ASSIGNMENT_KEYS | Define Assignment Keys | 106580 | FI-LOC-FI-AR | FI-AR-AR-2CL |
| SAP_CA_BC_IC_LND_FIN_SR_AR_PC | Statutory Reporting for Argentina - Configuration | S_ALR_87001495 | S_ALR_87001495_TRAN | J_1A_BRA_ASSIGNMENT | Define Branch Assignment for Automatic Postings | 106581 | FI-LOC-FI-AR | FI-AR-AR-2CL |
| SAP_CA_BC_IC_LND_FIN_SR_AR_PC | Statutory Reporting for Argentina - Configuration | S_ER9_11002015 | S_ER9_11002015_TRAN | FIVC_CF_VERSION_ACR | Define Cash Flow Statement Versions for Several Countries/Regions | 105331 | FI-LOC-FI-AR | FI-LOC-CF |
| SAP_CA_BC_IC_LND_FIN_SR_AR_PC | Statutory Reporting for Argentina - Configuration | S_ER9_11002335 | S_ER9_11002335_TRAN | FIVC_OFFS_GROUP_DRC | Define Field Sets for Grouping for Several Countries/Regions | 105762 | FI-LOC-FI-AR | FI-LOC-CF |
| SAP_CA_BC_IC_LND_FIN_SR_AR_PC | Statutory Reporting for Argentina - Configuration | S_EBJ_98000480 | S_EBJ_98000480_TRAN | V_J_1ATAXP_MAP | Maintain Cross Table for Mapping Tax Payer File | 102745 | FI-LOC-FI-AR | FI-LOC-FI-AR-WHT |
| SAP_CA_BC_IC_LND_FIN_SR_AR_PC | Statutory Reporting for Argentina - Configuration | S_ER9_11002079 | S_ER9_11002079_TRAN | FIVC_OFFS_VERS_A_CE | Define Offsetting Account Determination Versions for Several Countries/Rgns | 105370 | FI-LOC-FI-AR | FI-LOC-CF |
| SAP_CA_BC_IC_LND_FIN_SR_AR_PC | Statutory Reporting for Argentina - Configuration | S_ER9_11002017 | S_ER9_11002017_TRAN | FIVC_OFFS_DET_ACR | Activate Online Offsetting Account Determination for Several Countries/Rgns | 105333 | FI-LOC-FI-AR | FI-LOC-CF |
| SAP_CA_BC_IC_LND_SLL_ISR_PC | Intrastat - Configuration | /ECRS/52000042 | ECRS_52000042_TRAN | /ECRS/PURCHASE_DEF | Define Default Values for Purchasing | 102458 | FT-ITR-TRC | FT-ITR-ISR |
| SAP_CA_BC_IC_LND_SLL_ISR_PC | Intrastat - Configuration | /ECRS/52000114 | ECRS_52000114_TRAN | /ECRS/TICX | Define Exclusion of Sales Document Item Categories | 102459 | FT-ITR-TRC | FT-ITR-ISR |
| SAP_CA_BC_IC_LND_SLL_ISR_PC | Intrastat - Configuration | /ECRS/52000051 | ECRS_52000051_TRAN | /ECRS/MAT_GROUP_DEF | Define Material Groups for Intrastat | 102461 | FT-ITR-TRC | FT-ITR-ISR |
| SAP_CA_BC_IC_LND_SLL_ISR_PC | Intrastat - Configuration | /ECRS/52000044 | ECRS_52000044_TRAN | /ECRS/TD_RECEIPT_DEF | Define Default Values for Transportation Data for Receipts | 102726 | FT-ITR-TRC | FT-ITR-ISR |
| SAP_CA_BC_IC_LND_SLL_ISR_PC | Intrastat - Configuration | /ECRS/52000161 | ECRS_52000161_TRAN | /ECRS/TD_DISPATCH_DE | Define Default Values for Transportation Data for Dispatches | 102727 | FT-ITR-TRC | FT-ITR-ISR |
| SAP_CA_BC_IC_LND_SLL_ISR_PC | Intrastat - Configuration | /ECRS/52000037 | ECRS_52000037_TRAN | /ECRS/V_T609IS_2 | Define Data Selection Control for Sales | 104108 | FT-ITR-TRC | FT-ITR-ISR |
| SAP_CA_BC_IC_LND_SLL_ISR_PC | Intrastat - Configuration | /ECRS/52000166 | ECRS_52000166_TRAN | /ECRS/_DELIVERY_DEF | Define Default Values for Place of Delivery | 105950 | FT-ITR-TRC | FT-ITR-ISR |
| SAP_CA_BC_IC_LND_SLL_ISR_PC | Intrastat - Configuration | /ECRS/52000298 | ECRS_52000298_TRAN | /ECRS/V_TICS | Define Sales Document Item Categories for Services | 102460 | FT-ITR-TRC | FT-ITR-ISR |
| SAP_CA_BC_IC_LND_SLL_ISR_PC | Intrastat - Configuration | /ECRS/52003055 | ECRS_52003055_TRAN | /ECRS/SALES_DEF2 | Define Default Values for Specific Business Processes in Sales | 105515 | FT-ITR-TRC | FT-ITR-ISR |
| SAP_CA_BC_IC_LND_SLL_ISR_PC | Intrastat - Configuration | /ECRS/52000036 | ECRS_52000036_TRAN | /ECRS/V_T609IS_1 | Define Data Selection Control for Purchasing | 104107 | FT-ITR-TRC | FT-ITR-ISR |
| SAP_CA_BC_IC_LND_SLL_ISR_PC | Intrastat - Configuration | /ECRS/52000636 | ECRS_52000636_TRAN | /ECRS/SALES_DEF | Define Default Values for Sales | 102457 | FT-ITR-TRC | FT-ITR-ISR |
| SAP_CA_BC_IC_LND_SLL_ISR_PC | Intrastat - Configuration | /ECRS/12000002 | ECRS_12000002_TRAN | /ECRS/GP_COUNTRY_ASS | Assign Partner Countries to Countries of Declaration | 106995 | FT-ITR-TRC | FT-ITR-ISR |
| SAP_CA_BC_IC_LND_SLL_ISR_PC | Intrastat - Configuration | /ECRS/12000015 | ECRS_12000015_TRAN | /ECRS/EXC_GPCTRY_DEF | Define Exceptions for Conversion of Partner Countries | 106996 | FT-ITR-TRC | FT-ITR-ISR |
| SAP_CA_BC_IC_LND_SLL_ISR_PC | Intrastat - Configuration | /ECRS/12000004 | ECRS_12000004_TRAN | /ECRS/CNTRY_ORIG_ASS | Assign Countries of Origin to Countries of Declaration | 106997 | FT-ITR-TRC | FT-ITR-ISR |
| SAP_CA_BC_IC_LND_SLL_ISR_PC | Intrastat - Configuration | /ECRS/12000016 | ECRS_12000016_TRAN | /ECRS/EXC_COO_DEFINE | Define Exceptions for Conversion of Countries of Origin | 106998 | FT-ITR-TRC | FT-ITR-ISR |
| SAP_CA_BC_IC_LND_SLL_ISR_PC | Intrastat - Configuration | /ECRS/12000005 | ECRS_12000005_TRAN | /ECRS/REGION_DEFINE | Define Regions | 106999 | FT-ITR-TRC | FT-ITR-ISR |
| SAP_CA_BC_IC_LND_SLL_ISR_PC | Intrastat - Configuration | /ECRS/70000733 | ECRS_70000733_TRAN | /ECRS/EXC_CNVRSN_RGN | Define Exceptions for Conversion of Regions | 107000 | FT-ITR-TRC | FT-ITR-ISR |
| SAP_CA_BC_IC_LND_SLL_ISR_PC | Intrastat - Configuration | /ECRS/12000006 | ECRS_12000006_TRAN | /ECRS/BUSTRANSTY_DEF | Define Business Transaction Types | 107001 | FT-ITR-TRC | FT-ITR-ISR |
| SAP_CA_BC_IC_LND_SLL_ISR_PC | Intrastat - Configuration | /ECRS/12000009 | ECRS_12000009_TRAN | /ECRS/INCOTERMS_DEF | Define Incoterms | 107003 | FT-ITR-TRC | FT-ITR-ISR |
| SAP_CA_BC_IC_LND_SLL_ISR_PC | Intrastat - Configuration | /ECRS/12000008 | ECRS_12000008_TRAN | /ECRS/MODE_TRANS_DEF | Define Modes of Transport at the Border | 107002 | FT-ITR-TRC | FT-ITR-ISR |
| SAP_CA_BC_IC_LND_SLL_ISR_PC | Intrastat - Configuration | /ECRS/70000786 | ECRS_70000786_TRAN | /ECRS/EXC_CNVRSN_INC | Define Exceptions for Conversion of Incoterms | 107004 | FT-ITR-TRC | FT-ITR-ISR |
| SAP_CA_BC_IC_LND_SLL_ISR_PC | Intrastat - Configuration | /ECRS/52000055 | ECRS_52000055_TRAN | /ECRS/EX_INCL_CR_DEF | Define Exceptions for Inclusion and Exclusion of Countries and Regions | 107005 | FT-ITR-TRC | FT-ITR-ISR |
| SAP_CA_BC_IC_LND_GLO_LO1_PC | Globalisation Logistics - Configuration | S_PL0_86000099 | S_PL0_86000099_TRAN | ERS_003 | Create ERS Invoice Number Ranges | 103095 | FI-LOC-LO | FI-LOC-FI |
| SAP_CA_BC_IC_LND_GLO_LO1_PC | Globalisation Logistics - Configuration | S_ER9_52002379 | S_ER9_52002379_TRAN | GLO_BILFI_FLXINV | Assign Custom Routines to Tax Departure Countries/Regions | 103885 | FI-LOC-LO | FI-LOC-LO |
| SAP_CA_BC_IC_LND_GLO_LO1_PC | Globalisation Logistics - Configuration | S_ER9_52002378 | S_ER9_52002378_TRAN | VOFMC_BIL_FI_INT_RTN | Define Custom Routines for Flexible Billing Document Posting | 103884 | FI-LOC-LO | FI-LOC-LO |
| SAP_CA_BC_IC_LND_GLO_LO1_PC | Globalisation Logistics - Configuration | S_ER9_52002377 | S_ER9_52002377_TRAN | CPF_BF0_FORM | Define Formulas for Flexible Billing Document Posting | 103883 | FI-LOC-LO | FI-LOC-LO |
| SAP_CA_BC_IC_LND_GLO_LO1_PC | Globalisation Logistics - Configuration | S_ER9_52001241 | S_ER9_52001241_TRAN | ODN_SPAIN_04 | Assign Document Classes to Document Types for Spain | 102700 | FI-LOC-LO | CA-GTF-CSC-ES |
| SAP_CA_BC_IC_LND_GLO_LO1_PC | Globalisation Logistics - Configuration | S_ER9_52002303 | S_ER9_52002303_TRAN | GLO_WLF_BLART_V | Assign FI Document Type to Settlement Document Type | 103805 | FI-LOC-LO | FI-LOC-LO |
| SAP_CA_BC_IC_LND_GLO_LO1_PC | Globalisation Logistics - Configuration | S_ER9_52002376 | S_ER9_52002376_TRAN | CPF_BF0_CAT | Define Parameter Catalog for Flexible Billing Document Posting | 103882 | FI-LOC-LO | FI-LOC-LO |
| SAP_CA_BC_IC_LND_GLO_LO1_PC | Globalisation Logistics - Configuration | S_ER9_52001237 | S_ER9_52001237_TRAN | ODN_SPAIN_06 | Assign Number Ranges to Sales Organization/ Company Code | 102698 | FI-LOC-LO | CA-GTF-CSC-ES |
| SAP_CA_BC_IC_LND_GLO_LO1_PC | Globalisation Logistics - Configuration | GLO_ODN_ES |  | ODN_SPAIN_01 | Maintain Number Ranges for Spain | 102975 | FI-LOC-LO | CA-GTF-CSC-ES |
| SAP_CA_BC_IC_LND_GLO_LO1_PC | Globalisation Logistics - Configuration | CPF_BF0_FORM |  | CPF_BF0_FORM | Define Formulas for Flexible Billing Document Posting | 103883 | FI-LOC-LO | FI-LOC-LO |
| SAP_CA_BC_IC_LND_GLO_LO1_PC | Globalisation Logistics - Configuration | CPF_BF0_CAT |  | CPF_BF0_CAT | Define Parameter Catalog for Flexible Billing Document Posting | 103882 | FI-LOC-LO | FI-LOC-LO |
| SAP_CA_BC_IC_LND_GLO_LO1_PC | Globalisation Logistics - Configuration | S_ER9_52001488 | S_ER9_52001488_TRAN | GLO_PT_OBD | Maintain Number Ranges for Digital Signature OBD | 103092 | FI-LOC-LO | FI-LOC-LO-PT |
| SAP_CA_BC_IC_LND_GLO_LO1_PC | Globalisation Logistics - Configuration | S_ER9_52001790 | S_ER9_52001790_TRAN | SIPT_NUMBR_SET_V | Record Number Ranges for Digital Signature of Settlement Documents | 103407 | FI-LOC-LO | FI-LOC-LO-PT |
| SAP_CA_BC_IC_LND_GLO_LO1_PC | Globalisation Logistics - Configuration | S_EBS_44000451 | S_EBS_44000451_TRAN | SIPT_NUMBR_MM_V | Record Number Ranges for Digital Signature of Self Billing Documents (MM) | 103083 | FI-LOC-LO | FI-LOC-LO-PT |
| SAP_CA_BC_IC_LND_GLO_LO1_PC | Globalisation Logistics - Configuration | S_EBJ_98000096 | S_EBJ_98000096_TRAN | SIPT_NUMBR_OBD_V | Record Number Ranges for Digital Signature of Outbound Delivery Documents | 103084 | FI-LOC-LO | FI-LOC-LO-PT |
| SAP_CA_BC_IC_LND_GLO_LO1_PC | Globalisation Logistics - Configuration | GLO_PT_SET | GLO_PT_SET_TRAN | STLMNT_GLO_PT_SET | Maintain Number Ranges for Settlement Documents Portugal | 103456 | FI-LOC-LO | FI-LOC-LO-PT |
| SAP_CA_BC_IC_LND_GLO_LO1_PC | Globalisation Logistics - Configuration | GLO_PT_OBD | GLO_PT_OBD_TRAN | GLO_PT_OBD | Maintain Number Ranges for Digital Signature OBD | 103092 | FI-LOC-LO | FI-LOC-LO-PT |
| SAP_CA_BC_IC_LND_GLO_LO1_PC | Globalisation Logistics - Configuration | S_ER9_52000142 | S_ER9_52000142_TRAN | GLO_LOG_REAS_TXT | Define Texts for Billing Documents | 103087 | FI-LOC-LO | FI-LOC-LO |
| SAP_CA_BC_IC_LND_GLO_LO1_PC | Globalisation Logistics - Configuration | IDLB |  | VC_IDCN_LBMA_TR | Maintain Lots and Books for Turkey | 102650 | FI-LOC-LO | FI-LOC-LO-TR |
| SAP_CA_BC_IC_LND_GLO_LO1_PC | Globalisation Logistics - Configuration | S_EBJ_98000611 | S_EBJ_98000611_TRAN | VC_IDCN_LBMA_TR | Maintain Lots and Books for Turkey | 102650 | FI-LOC-LO | FI-LOC-LO-TR |
| SAP_CA_BC_IC_LND_GLO_LO1_PC | Globalisation Logistics - Configuration | S_ER9_52003434 | S_ER9_52003434_TRAN | SIPT_NUMBR_SETV | Assign SAF-T Document Types to Number Ranges of Settlement Documents | 105744 | FI-LOC-LO | FI-LOC-LO-PT |
| SAP_CA_BC_IC_LND_GLO_LO1_PC | Globalisation Logistics - Configuration | BPCODE |  | BPCODE | Maintain Business Premise Master Data | 106658 | FI-LOC-LO | FI-LOC-LO-SI |
| SAP_CA_BC_IC_LND_GLO_LO1_PC | Globalisation Logistics - Configuration | S_ER1_70000798 | S_ER1_70000798_TRAN | BPCODE | Maintain Business Premise Master Data | 106658 | FI-LOC-LO | FI-LOC-LO-SI |
| SAP_CA_BC_IC_LND_GLO_LO1_PC | Globalisation Logistics - Configuration | EDCODE |  | EDCODE | Maintain Electronic Device Mapping Details | 106659 | FI-LOC-LO | FI-LOC-LO-SI |
| SAP_CA_BC_IC_LND_GLO_LO1_PC | Globalisation Logistics - Configuration | S_ER1_70000799 | S_ER1_70000799_TRAN | EDCODE | Maintain Electronic Device Mapping Details | 106659 | FI-LOC-LO | FI-LOC-LO-SI |
| SAP_CA_BC_IC_LND_GLO_LO1_PC | Globalisation Logistics - Configuration | S_ER9_52001233 | S_ER9_52001233_TRAN | ODN_SPAIN_01 | Maintain Number Ranges for Spain | 102975 | FI-LOC-LO | CA-GTF-CSC-ES |
| SAP_CA_BC_IC_LND_GLO_LO1_PC | Globalisation Logistics - Configuration | S_ER9_52001789 | S_ER9_52001789_TRAN | STLMNT_GLO_PT_SET | Maintain Number Ranges for Settlement Documents Portugal | 103456 | FI-LOC-LO | FI-LOC-LO-PT |
| SAP_CA_BC_IC_LND_GLO_LO1_PC | Globalisation Logistics - Configuration | S_ER9_52001976 | S_ER9_52001976_TRAN | RDSVV_POS_CERT | Maintain Data for External Digital Signature Software [‘POS’ Invoices] (SD) | 106823 | FI-LOC-LO | FI-LOC-CER |
| SAP_CA_BC_IC_LND_GLO_LO1_PC | Globalisation Logistics - Configuration | PL_KSEF_PODMIOT_V2 | PL_KSEF_PODMIOT_V2_TRAN | EDOPLPODMIOTV2 | Define Additional Business Partner Functions for KSeF Version 2 | 107174 | FI-LOC-LO | CA-GTF-CSC-EDO-PL |
| SAP_CA_BC_IC_LND_GLO_LO1_PC | Globalisation Logistics - Configuration | S_ER1_70001671 | S_ER1_70001671_TRAN | EDOPLPODMIOTV2 | Define Additional Business Partner Functions for KSeF Version 2 | 107174 | FI-LOC-LO | CA-GTF-CSC-EDO-PL |
| SAP_CA_BC_IC_LND_GLO_LO1_PC | Globalisation Logistics - Configuration | S_ER9_52003266 | S_ER9_52003266_TRAN | SIPT_NUMBR_SD_V2 | Assign SAF-T Document Types to Number Ranges (SD) | 105873 | FI-LOC-LO | FI-LOC-SD-PT |
| SAP_CA_BC_IC_LND_GLO_LO1_PC | Globalisation Logistics - Configuration | S_EBS_44000282 | S_EBS_44000282_TRAN | SIPT_NUMBR_SD_V | Record Number Ranges for Digital Signature of Billing Documents (SD) | 180009 | FI-LOC-LO | FI-LOC-SD-PT |
| SAP_CA_BC_IC_LND_GLO_LO1_PC | Globalisation Logistics - Configuration | PL_KSEF_ADD_PARR | PL_KSEF_ADD_PARR_TRAN | EDO_PL_ADDNLPARV | Define Settings for IDWew Field for Poland e-Invocing Through KSeF | 107173 | FI-LOC-LO | CA-GTF-CSC-EDO-PL |
| SAP_CA_BC_IC_LND_GLO_LO1_PC | Globalisation Logistics - Configuration | S_ER1_70001670 | S_ER1_70001670_TRAN | EDO_PL_ADDNLPARV | Define Settings for IDWew Field for Poland e-Invocing Through KSeF | 107173 | FI-LOC-LO | CA-GTF-CSC-EDO-PL |
| SAP_CA_BC_IC_LND_GLO_LO1_PC | Globalisation Logistics - Configuration | S_ER1_70001681 | S_ER1_70001681_TRAN | EDO_PL_TERM_OPV | Define Payment Deadline for KSeF | 107189 | FI-LOC-LO | CA-GTF-CSC-EDO-PL |
| SAP_CA_BC_IC_LND_GLO_LO1_PC | Globalisation Logistics - Configuration | J1AB | J1AB_TRAN | ERS_003 | Create ERS Invoice Number Ranges | 103095 | FI-LOC-LO | FI-LOC-FI |
| SAP_CA_BC_IC_LND_GLO_LO1_PC | Globalisation Logistics - Configuration | PL_KSEF_MAP_TAXV2 | PL_KSEF_MAP_TAXV2_TRAN | EDO_PL_MAPTAXV2V | Map Tax Codes to Invoicing Elements Version 2 | 107188 | FI-LOC-LO | CA-GTF-CSC-EDO-PL |
| SAP_CA_BC_IC_LND_GLO_LO1_PC | Globalisation Logistics - Configuration | EDOESCANTAXTYPE | EDOESCANTAXTYPE_TRAN | EDOESCANTAXTYPEV | Assign Settings for Accounting Key Tax Type | 107186 | FI-LOC-LO | CA-GTF-CSC-EDO-ES |
| SAP_CA_BC_IC_LND_GLO_LO1_PC | Globalisation Logistics - Configuration | S_ER1_70001693 | S_ER1_70001693_TRAN | EDO_PL_MAPTAXV2V | Map Tax Codes to Invoicing Elements Version 2 | 107188 | FI-LOC-LO | CA-GTF-CSC-EDO-PL |
| SAP_CA_BC_IC_LND_GLO_LO1_PC | Globalisation Logistics - Configuration | EDOESCANITADDCLV | EDOESCANITADDCLV_TRAN | FIESCAN_ITADDCLV | Assign Additional Attributes to Input Tax Codes for IGIC | 107267 | FI-LOC-LO | CA-GTF-CSC-EDO-ES |
| SAP_CA_BC_IC_LND_GLO_LO1_PC | Globalisation Logistics - Configuration | S_ER1_70001695 | S_ER1_70001695_TRAN | EDOESCANTAXTYPEV | Assign Settings for Accounting Key Tax Type | 107186 | FI-LOC-LO | CA-GTF-CSC-EDO-ES |
| SAP_CA_BC_IC_LND_GLO_LO1_PC | Globalisation Logistics - Configuration | PL_KSEF_TERMIN_OPIS | PL_KSEF_TERMIN_OPIS_TRAN | EDO_PL_TERM_OPV | Define Payment Deadline for KSeF | 107189 | FI-LOC-LO | CA-GTF-CSC-EDO-PL |
| SAP_CA_BC_IC_LND_GLO_LO1_PC | Globalisation Logistics - Configuration | S_ER1_70001809 | S_ER1_70001809_TRAN | FIESCAN_ITADDCLV | Assign Additional Attributes to Input Tax Codes for IGIC | 107267 | FI-LOC-LO | CA-GTF-CSC-EDO-ES |
| SAP_CA_BC_IC_LND_GLO_LO1_PC | Globalisation Logistics - Configuration | S_ER1_70001934 | S_ER1_70001934_TRAN | GLO_LOG_TAXCODE | Maintain Tax Code against Business Processes | 107402 | FI-LOC-LO | FI-LOC-LO |
| SAP_PS_BC_MANAGE_PBRWF_PC | Project Billing - Workflow Configuration | F5980 | F5980_TRAN |  |  |  | PPM-SCL-STR |  |
| SAP_CA_BC_IC_LND_ADDR1_PC | Business Services Address Management - Configuration | OY01 | SAIS_OY01_TRAN |  |  |  | CA-GTF-SRV-ADR |  |
| SAP_CA_BC_IC_LND_ADDR1_PC | Business Services Address Management - Configuration | S_AC0_52000738 | S_AC0_52000738_TRAN | SIMG_CFMENUSAPCOY01N | Define Countries/Regions | 104076 | CA-GTF-SRV-ADR | CA-GTF-SRV-ADR |
| SAP_CA_BC_IC_LND_CMD_PRD_PC | Central Master Data Product - Configuration | S_ALR_87002272 | S_ALR_87002272_TRAN | SIMG_CFMENUOLMSOMSP | Define Divisions | 100526 | LO-MD-MM | LO-MD-MM-2CL |
| SAP_CA_BC_IC_LND_CMD_PRD_PC | Central Master Data Product - Configuration | S_ALR_87002295 | S_ALR_87002295_TRAN | SIMG_CFMENUOLMSOMS8 | Define Container Requirements | 103907 | LO-MD-MM | LO-MD-MM-2CL |
| SAP_CA_BC_IC_LND_CMD_PRD_PC | Central Master Data Product - Configuration | S_ER9_52001608 | S_ER9_52001608_TRAN | SIMG_EAN_EANGEWICHT | Assign Number Ranges to Number Range Object - EANGEWICHT | 103685 | LO-MD-MM | LO-MD-MM-2CL |
| SAP_CA_BC_IC_LND_CMD_PRD_PC | Central Master Data Product - Configuration | S_ALR_87002429 | S_ALR_87002429_TRAN | SIMG_CFMENUOLMSOMT6 | Define Basic Materials | 103908 | LO-MD-MM | LO-MD-MM-2CL |
| SAP_CA_BC_IC_LND_CMD_PRD_PC | Central Master Data Product - Configuration | S_ER9_52001683 | S_ER9_52001683_TRAN | PM_FPH_001 | Configure Nodes for Product Hierarchies | 103298 | LO-MD-MM | LO-MD-MM-2CL |
| SAP_CA_BC_IC_LND_CMD_PRD_PC | Central Master Data Product - Configuration | S_ER9_52001607 | S_ER9_52001607_TRAN | SIMG_EAN_EUROPARTNR | Assign Number Ranges to Number Range Object - EUROPARTNR | 103683 | LO-MD-MM | LO-MD-MM-2CL |
| SAP_CA_BC_IC_LND_CMD_PRD_PC | Central Master Data Product - Configuration | S_ER9_52001609 | S_ER9_52001609_TRAN | SIMG_EAN_EANGEWICH5 | Assign Number Ranges to Number Range Object - EANGEWICH5 | 103684 | LO-MD-MM | LO-MD-MM-2CL |
| SAP_CA_BC_IC_LND_CMD_PRD_PC | Central Master Data Product - Configuration | S_ALR_87002293 | S_ALR_87002293_TRAN | SIMG_CFMENUOLMSOMS7 | Define Temperature Conditions | 103906 | LO-MD-MM | LO-MD-MM-2CL |
| SAP_CA_BC_IC_LND_CMD_PRD_PC | Central Master Data Product - Configuration | S_ALR_87002397 | S_ALR_87002397_TRAN | SIMG_CFMENUOLMSW4EM | Define Number Ranges for Perishables EANs (4-Figure) | 103681 | LO-MD-MM | LO-MD-MM-2CL |
| SAP_CA_BC_IC_LND_CMD_PRD_PC | Central Master Data Product - Configuration | S_ALR_87002386 | S_ALR_87002386_TRAN | SIMG_CFMENUOLMSW4EN | Define Number Ranges for EANs/UPCs | 103680 | LO-MD-MM | LO-MD-MM-2CL |
| SAP_CA_BC_IC_LND_CMD_PRD_PC | Central Master Data Product - Configuration | S_ALR_87002380 | S_ALR_87002380_TRAN | SIMG_CFMENUOLMSW4ES | Define Attributes of EANs/UPCs | 102782 | LO-MD-MM | LO-MD-MM-2CL |
| SAP_CA_BC_IC_LND_CMD_PRD_PC | Central Master Data Product - Configuration | S_ALR_87002330 | S_ALR_87002330_TRAN | SIMG_CFMENUOLMSMMNR | Define Number Ranges for Each Material Type | 102282 | LO-MD-MM | LO-MD-MM-2CL |
| SAP_CA_BC_IC_LND_CMD_PRD_PC | Central Master Data Product - Configuration | S_ALR_87002312 | S_ALR_87002312_TRAN | SIMG_CFMENUOLMSOMS2 | Define Attributes of Material Types | 103539 | LO-MD-MM | LO-MD-MM-2CL |
| SAP_CA_BC_IC_LND_CMD_PRD_PC | Central Master Data Product - Configuration | S_ALR_87002257 | S_ALR_87002257_TRAN | SIMG_CFMENUOLMSOMSF | Define Material Groups | 102665 | LO-MD-MM | LO-MD-MM-2CL |
| SAP_CA_BC_IC_LND_CMD_PRD_PC | Central Master Data Product - Configuration | S_AL0_96000737 | S_AL0_96000737_TRAN | SIMG_CFMENUOLMS_ABC | Extend ABC Indicator | 102560 | LO-MD-MM | LO-MD-MM-2CL |
| SAP_CA_BC_IC_LND_CMD_PRD_PC | Central Master Data Product - Configuration | OMT4 |  | SIMG_CFMENUOLMSOMT4 | Define Attributes of System Messages | 103090 | LO-MD-MM | LO-MD-MM-2CL |
| SAP_CA_BC_IC_LND_CMD_PRD_PC | Central Master Data Product - Configuration | OMS4 |  | SIMG_CFMENUOLMSOMS4 | Define Material Statuses | 102618 | LO-MD-MM | LO-MD-MM-2CL |
| SAP_CA_BC_IC_LND_CMD_PRD_PC | Central Master Data Product - Configuration | S_ALR_87002348 | S_ALR_87002348_TRAN | SIMG_CFMENUOLMSOMS4 | Define Material Statuses | 102618 | LO-MD-MM | LO-MD-MM-2CL |
| SAP_CA_BC_IC_LND_CMD_PRD_PC | Central Master Data Product - Configuration | OS26 |  | SIMG_CFMENUOLMSOMS5 | Define Laboratories and Offices |  | LO-MD-MM | LO-MD-MM-2CL |
| SAP_CA_BC_IC_LND_CMD_PRD_PC | Central Master Data Product - Configuration | S_ALR_87002355 | S_ALR_87002355_TRAN | SIMG_CFMENUOLMSOMT4 | Define Attributes of System Messages | 103090 | LO-MD-MM | LO-MD-MM-2CL |
| SAP_CA_BC_IC_LND_CMD_PRD_PC | Central Master Data Product - Configuration | S_ALR_87001805 | S_ALR_87001805_TRAN | SIMG_CFMENUOLMSOMSR | Assign Fields to Field Selection Groups | 104026 | LO-MD-MM | LO-MD-MM-2CL |
| SAP_CA_BC_IC_LND_CMD_PRD_PC | Central Master Data Product - Configuration | OMSF |  | SIMG_CFMENUOLMSOMSF | Define Material Groups | 102665 | LO-MD-MM | LO-MD-MM-2CL |
| SAP_CA_BC_IC_LND_CMD_PRD_PC | Central Master Data Product - Configuration | W4E5 |  | W_ZF_ST_0261 | Define Number Ranges for Perishables EANs (5-Figure) | 103682 | LO-MD-MM | LO-MD-MM-2CL |
| SAP_CA_BC_IC_LND_CMD_PRD_PC | Central Master Data Product - Configuration | MMNR |  | SIMG_CFMENUOLMSMMNR | Define Number Ranges for Each Material Type | 102282 | LO-MD-MM | LO-MD-MM-2CL |
| SAP_CA_BC_IC_LND_CMD_PRD_PC | Central Master Data Product - Configuration | OMSR |  | SIMG_CFMENUOLMSOMSR | Assign Fields to Field Selection Groups | 104026 | LO-MD-MM | LO-MD-MM-2CL |
| SAP_CA_BC_IC_LND_CMD_PRD_PC | Central Master Data Product - Configuration | S_ALR_87001816 | S_ALR_87001816_TRAN | SIMG_CFMENUOLMSOMS9 | Maintain Field Selection for Data Screens | 104027 | LO-MD-MM | LO-MD-MM-2CL |
| SAP_CA_BC_IC_LND_CMD_PRD_PC | Central Master Data Product - Configuration | S_ALR_87002264 | S_ALR_87002264_TRAN | SIMG_CFMENUOLMSOMS5 | Define Laboratories and Offices |  | LO-MD-MM | LO-MD-MM-2CL |
| SAP_CA_BC_IC_LND_CMD_PRD_PC | Central Master Data Product - Configuration | OMS9 |  | SIMG_CFMENUOLMSOMS9 | Maintain Field Selection for Data Screens | 104027 | LO-MD-MM | LO-MD-MM-2CL |
| SAP_CA_BC_IC_LND_CMD_PRD_PC | Central Master Data Product - Configuration | SSCUI_MD_VALCLS |  | DVC_CFMENUOLMWOMSK | Define Valuation Classes | 102424 | LO-MD-MM | LO-MD-MM-2CL |
| SAP_CA_BC_IC_LND_CMD_PRD_PC | Central Master Data Product - Configuration | W4EN |  | SIMG_CFMENUOLMSW4EN | Define Number Ranges for EANs/UPCs | 103680 | LO-MD-MM | LO-MD-MM-2CL |
| SAP_CA_BC_IC_LND_CMD_PRD_PC | Central Master Data Product - Configuration | W4EM |  | SIMG_CFMENUOLMSW4EM | Define Number Ranges for Perishables EANs (4-Figure) | 103681 | LO-MD-MM | LO-MD-MM-2CL |
| SAP_CA_BC_IC_LND_CMD_PRD_PC | Central Master Data Product - Configuration | SSCUI_MD_MTYP_AREF |  | DACRM_CFMENUOLMWOMSK | Define Account Category Reference/Material Type | 102423 | LO-MD-MM | LO-MD-MM-2CL |
| SAP_CA_BC_IC_LND_CMD_PRD_PC | Central Master Data Product - Configuration | S_ALR_87004525 | S_ALR_87004525_TRAN | SIMG_CFMENUOLPSOS26 | Define Laboratory/Design Office | 103123 | LO-MD-MM | PP-BD-RTG-2CL |
| SAP_CA_BC_IC_LND_CMD_PRD_PC | Central Master Data Product - Configuration | SSCUI_MD_AREF |  | DACR_CFMENUOLMWOMSK | Define Account Category Reference | 102425 | LO-MD-MM | LO-MD-MM-2CL |
| SAP_CA_BC_IC_LND_CMD_PRD_PC | Central Master Data Product - Configuration | S_ER9_52003048 | S_ER9_52003048_TRAN | DACRM_CFMENUOLMWOMSK | Define Account Category Reference/Material Type | 102423 | LO-MD-MM | LO-MD-MM-2CL |
| SAP_CA_BC_IC_LND_CMD_PRD_PC | Central Master Data Product - Configuration | S_ER9_52003047 | S_ER9_52003047_TRAN | DACR_CFMENUOLMWOMSK | Define Account Category Reference | 102425 | LO-MD-MM | LO-MD-MM-2CL |
| SAP_CA_BC_IC_LND_CMD_PRD_PC | Central Master Data Product - Configuration | S_ER9_52003046 | S_ER9_52003046_TRAN | DVC_CFMENUOLMWOMSK | Define Valuation Classes | 102424 | LO-MD-MM | LO-MD-MM-2CL |
| SAP_CA_BC_IC_LND_CMD_PRD_PC | Central Master Data Product - Configuration | V_T130F_C |  | SIMG_V_T130F_C | Define Copy Behavior of Fields in Material Master | 106049 | LO-MD-MM | LO-MD-MM-2CL |
| SAP_CA_BC_IC_LND_CMD_PRD_PC | Central Master Data Product - Configuration | S_ER1_70000923 | S_ER1_70000923_TRAN | SIMG_V_T130F_C_FIXRE | Define Lock-Relevant Fields in Product Master | 106750 | LO-MD-MM | LO-MD-MM-2CL |
| SAP_CA_BC_IC_LND_CMD_PRD_PC | Central Master Data Product - Configuration | OMSL |  | SIMG_CFMENUOLMSOMSL | Define Output Format of Material Numbers | 102320 | LO-MD-MM | CA-GTF-TS-LO |
| SAP_CA_BC_IC_LND_CMD_PRD_PC | Central Master Data Product - Configuration | OMSFIXC |  | SIMG_V_T130F_C_FIXRE | Define Lock-Relevant Fields in Product Master | 106750 | LO-MD-MM | LO-MD-MM-2CL |
| SAP_CA_BC_IC_LND_CMD_PRD_PC | Central Master Data Product - Configuration | S_ER9_52000318 | S_ER9_52000318_TRAN | SIMG_V_T130F_C | Define Copy Behavior of Fields in Material Master | 106049 | LO-MD-MM | LO-MD-MM-2CL |
| SAP_CA_BC_IC_LND_CMD_PRD_PC | Central Master Data Product - Configuration | S_ALR_87002404 | S_ALR_87002404_TRAN | W_ZF_ST_0261 | Define Number Ranges for Perishables EANs (5-Figure) | 103682 | LO-MD-MM | LO-MD-MM-2CL |
| SAP_CA_BC_IC_LND_CMD_PRD_PC | Central Master Data Product - Configuration | S_ALR_87002338 | S_ALR_87002338_TRAN | SIMG_CFMENUOLMSOMSL | Define Output Format of Material Numbers | 102320 | LO-MD-MM | CA-GTF-TS-LO |
| SAP_CA_BC_IC_LND_CMD_PRD_PC | Central Master Data Product - Configuration | S_ALR_87001873 | S_ALR_87001873_TRAN | W_ZF_ST_0268 | Maintain External Material Groups | 102983 | LO-MD-MM | LO-MD-MM-2CL |
| SAP_CA_BC_IC_LND_CMD_PRD_PC | Central Master Data Product - Configuration | V_TWEW |  | W_ZF_ST_0268 | Maintain External Material Groups | 102983 | LO-MD-MM | LO-MD-MM-2CL |
| SAP_CA_BC_IC_LND_CMD_PRD_PC | Central Master Data Product - Configuration | MFLE_SWITCH |  | V_MFLE_SWITCH | Material Field Length Extension | 107338 | LO-MD-MM | LO-MD-MM-2CL |
| SAP_CA_BC_IC_LND_CMD_PRD_PC | Central Master Data Product - Configuration | S_ER1_70000701 | S_ER1_70000701_TRAN | V_MFLE_SWITCH | Material Field Length Extension | 107338 | LO-MD-MM | LO-MD-MM-2CL |
| SAP_CA_BC_IC_LND_FIN_SR_CH_PC | Statutory Reporting for Switzerland - Configuration | S_E4A_94000278 | S_E4A_94000278_TRAN | IDITSR_POSNUM_V | Define Reporting Subcategories | 101226 | FI-LOC-FI-CH | FI-LOC-FI |
| SAP_CA_BC_IC_LND_FIN_SR_CH_PC | Statutory Reporting for Switzerland - Configuration | S_ER1_70001023 | S_ER1_70001023_TRAN | FICHVC_CF_VERS_DRC | Define Cash Flow Statement Versions for Switzerland | 106784 | FI-LOC-FI-CH | FI-LOC-CF-CH |
| SAP_CA_BC_IC_LND_FIN_SR_CH_PC | Statutory Reporting for Switzerland - Configuration | S_E4A_94000279 | S_E4A_94000279_TRAN | IDITSR_SELECT_V | Define Criteria for Assigning Documents to Reporting Category/Subcategory | 101227 | FI-LOC-FI-CH | FI-LOC-FI |
| SAP_CA_BC_IC_LND_FIN_SR_AU_PC | Statutory Reporting for Australia - Configuration | S_ER9_11001860 | S_ER9_11001860_TRAN | FIAUV_TPAR_GR_CO | Maintain TPAR Configuration Object for Grants | 104109 | FI-LOC-FI-AU | FI-LOC-FI-AU |
| SAP_CA_BC_IC_LND_FIN_SR_AU_PC | Statutory Reporting for Australia - Configuration | S_ER9_11001592 | S_ER9_11001592_TRAN | FIAUV_TPAR_STYP | TPAR Service Type | 103570 | FI-LOC-FI-AU | FI-LOC-FI-AU |
| SAP_CA_BC_IC_LND_FIN_SR_AU_PC | Statutory Reporting for Australia - Configuration | S_ER9_11001609 | S_ER9_11001609_TRAN | FIAUV_PAYG_TYPE | Assign G/L Account to BAS Tax Type | 103632 | FI-LOC-FI-AU | FI-LOC-FI-AU |
| SAP_CA_BC_IC_LND_EAM_ORG_PC | Maintenance Management Organization - Configuration | S_ALR_87007367 | S_ALR_87007367_TRAN | SIMG_CFMENUSAPCOIX0 | Maintain Maintenance Planning Plant | 103771 | PM | PM-2CL |
| SAP_CA_BC_IC_LND_EAM_ORG_PC | Maintenance Management Organization - Configuration | S_ALR_87000093 | S_ALR_87000093_TRAN | SIMG_CFMENUOLI0OIAI | Define Planner Groups | 101897 | PM | PM-2CL |
| SAP_CA_BC_IC_LND_EAM_ORG_PC | Maintenance Management Organization - Configuration | S_ALR_87000097 | S_ALR_87000097_TRAN | SIMG_CFMENUOLI0OIAB | Define Plant Sections | 102635 | PM | PM-2CL |
| SAP_CA_BC_IC_LND_EAM_ORG_PC | Maintenance Management Organization - Configuration | S_ALR_87007433 | S_ALR_87007433_TRAN | SIMG_CFMENUSAPCOIX1 | Assign Maintenance Planning Plant to Maintenance Plant | 103772 | PM | PM-2CL |
| SAP_FIN_BC_TRM_FOMRCONF_PC | TRM - Configuration for FO Substitution Rules - Market Risk | F7688 | F7688_TRAN |  |  |  | FIN-FSCM-TRM |  |
| SAP_CA_BC_IC_LND_FIN_CM0_PC | Bank Relationship Management - Configuration | S_ERW_11000326 | S_ERW_11000326_TRAN | FSCM_CLM_BASIC | Define Basic Settings | 101025 | FIN-FSCM-CLM | FIN-FSCM-CLM-BAM-2CL |
| SAP_CA_BC_IC_LND_FIN_CM0_PC | Bank Relationship Management - Configuration | S_ER9_11001674 | S_ER9_11001674_TRAN | FCLM_BAM_MSG_CTRL | Change Message Control for Bank Account Management | 103894 | FIN-FSCM-CLM | FIN-FSCM-CLM-BAM-2CL |
| SAP_CA_BC_IC_LND_FIN_CM0_PC | Bank Relationship Management - Configuration | S_ER9_11000214 | S_ER9_11000214_TRAN | FCLM_BAM_FSG | Manage Field Status Groups | 104059 | FIN-FSCM-CLM | FIN-FSCM-CLM-BAM-2CL |
| SAP_CA_BC_IC_LND_FIN_CM0_PC | Bank Relationship Management - Configuration | FCLM_BAM_MSG_CTRL |  | FCLM_BAM_MSG_CTRL | Change Message Control for Bank Account Management | 103894 | FIN-FSCM-CLM | FIN-FSCM-CLM-BAM-2CL |
| SAP_CA_BC_IC_LND_FIN_CM0_PC | Bank Relationship Management - Configuration | S_ER9_11001639 | S_ER9_11001639_TRAN | FINS_BACL_PAGRP | Define Authorization Groups for Bank Account Transactions | 103888 | FIN-FSCM-CLM | FI-GL-GL-J-2CL |
| SAP_CA_BC_IC_LND_FIN_CM0_PC | Bank Relationship Management - Configuration | S_ER9_11001898 | S_ER9_11001898_TRAN | FCLM_BS_INTEGRATION | Define Settings for Bank Statements | 104351 | FIN-FSCM-CLM | FIN-FSCM-CLM-2CL |
| SAP_CA_BC_IC_LND_FIN_CM0_PC | Bank Relationship Management - Configuration | S_ER9_11001986 | S_ER9_11001986_TRAN | FCLM_CONTRACT_TYPE | Define Settings for Bank Account Contract Types | 105304 | FIN-FSCM-CLM | FIN-FSCM-CLM-BAM-2CL |
| SAP_CA_BC_IC_LND_FIN_CM0_PC | Bank Relationship Management - Configuration | S_ER9_11002081 | S_ER9_11002081_TRAN | VC_FCLMPOA_AUTHGR | Define Authorization Groups for Powers of Attorney | 105411 | FIN-FSCM-CLM | FIN-FSCM-CLM-BAM-2CL |
| SAP_CA_BC_IC_LND_FIN_CM0_PC | Bank Relationship Management - Configuration | S_ER9_11002112 | S_ER9_11002112_TRAN | FCLMPOAV_ACT | Define Activities for Powers of Attorney | 105484 | FIN-FSCM-CLM | FIN-FSCM-CLM-BAM-2CL |
| SAP_CA_BC_IC_LND_FIN_CM0_PC | Bank Relationship Management - Configuration | S_ER9_11002420 | S_ER9_11002420_TRAN | FCLM_BAM_MAIL | Disable Email Notifications | 105863 | FIN-FSCM-CLM | FIN-FSCM-CLM-BAM-2CL |
| SAP_CA_BC_IC_LND_FIN_CM0_PC | Bank Relationship Management - Configuration | FCLM_BAM_MAIL |  |  |  |  | FIN-FSCM-CLM |  |
| SAP_CA_BC_IC_LND_FIN_CM0_PC | Bank Relationship Management - Configuration | S_ER9_11002350 | S_ER9_11002350_TRAN | FCLMPOAV_CHNL | Define Channels for Powers of Attorney | 105811 | FIN-FSCM-CLM | FIN-FSCM-CLM-BAM-2CL |
| SAP_CA_BC_IC_LND_FIN_CM0_PC | Bank Relationship Management - Configuration | S_E91_86000021 | S_E91_86000021_TRAN | FCLM_BAM_MD | Define Settings for Bank Account Master Data | 102336 | FIN-FSCM-CLM | FIN-FSCM-CLM-BAM-2CL |
| SAP_CA_BC_IC_LND_FIN_CM0_PC | Bank Relationship Management - Configuration | FCLM_BAM_ACCT_CHARC |  | FCLM_BAM_ACCT_CHARC | Define Bank Account Characteristics | 106756 | FIN-FSCM-CLM | FIN-FSCM-CLM-BAM-2CL |
| SAP_CA_BC_IC_LND_FIN_CM0_PC | Bank Relationship Management - Configuration | S_ER1_70000971 | S_ER1_70000971_TRAN | FCLM_BAM_ACCT_CHARC | Define Bank Account Characteristics | 106756 | FIN-FSCM-CLM | FIN-FSCM-CLM-BAM-2CL |
| SAP_CA_BC_IC_LND_FIN_CM0_PC | Bank Relationship Management - Configuration | FCLM_BKCORR_TYPE |  | FCLM_BKCORR_TYPE | Define Bank Correspondence Types | 106791 | FIN-FSCM-CLM | FIN-FSCM-CLM-BAM-2CL |
| SAP_CA_BC_IC_LND_FIN_CM0_PC | Bank Relationship Management - Configuration | FCLM_BKCORR_OBJNR |  | FCLM_BKCORR_OBJNR | Define Number Range for Bank Correspondence Objects | 106794 | FIN-FSCM-CLM | FIN-FSCM-CLM-BAM-2CL |
| SAP_CA_BC_IC_LND_FIN_CM0_PC | Bank Relationship Management - Configuration | FCLM_BKCORR_FLDRNR |  | FCLM_BKCORR_FLDRNR | Define Number Ranges for Bank Correspondence Folders | 106793 | FIN-FSCM-CLM | FIN-FSCM-CLM-BAM-2CL |
| SAP_CA_BC_IC_LND_FIN_CM0_PC | Bank Relationship Management - Configuration | FCLM_BKCORR_AUGP |  | FCLM_BKCORR_AUGP | Define Authorization Groups for Bank Correspondence | 106792 | FIN-FSCM-CLM | FIN-FSCM-CLM-BAM-2CL |
| SAP_CA_BC_IC_LND_FIN_CM0_PC | Bank Relationship Management - Configuration | S_ER1_70001051 | S_ER1_70001051_TRAN | FCLM_BKCORR_TYPE | Define Bank Correspondence Types | 106791 | FIN-FSCM-CLM | FIN-FSCM-CLM-BAM-2CL |
| SAP_CA_BC_IC_LND_FIN_CM0_PC | Bank Relationship Management - Configuration | S_ER1_70001050 | S_ER1_70001050_TRAN | FCLM_BKCORR_AUGP | Define Authorization Groups for Bank Correspondence | 106792 | FIN-FSCM-CLM | FIN-FSCM-CLM-BAM-2CL |
| SAP_CA_BC_IC_LND_FIN_CM0_PC | Bank Relationship Management - Configuration | S_ER1_70001049 | S_ER1_70001049_TRAN | FCLM_BKCORR_FLDRNR | Define Number Ranges for Bank Correspondence Folders | 106793 | FIN-FSCM-CLM | FIN-FSCM-CLM-BAM-2CL |
| SAP_CA_BC_IC_LND_FIN_CM0_PC | Bank Relationship Management - Configuration | S_ER1_70001048 | S_ER1_70001048_TRAN | FCLM_BKCORR_OBJNR | Define Number Range for Bank Correspondence Objects | 106794 | FIN-FSCM-CLM | FIN-FSCM-CLM-BAM-2CL |
| SAP_CA_BC_IC_LND_FIN_CM0_PC | Bank Relationship Management - Configuration | FCLM_BKCORR_AUTO |  | FCLM_BKCORR_AUTO | Define Bank Accounts for Automatic Creation of Correspondence Folders | 106884 | FIN-FSCM-CLM | FIN-FSCM-CLM-BAM-2CL |
| SAP_CA_BC_IC_LND_FIN_CM0_PC | Bank Relationship Management - Configuration | S_ER1_70001254 | S_ER1_70001254_TRAN | FCLM_BKCORR_AUTO | Define Bank Accounts for Automatic Creation of Correspondence Folders | 106884 | FIN-FSCM-CLM | FIN-FSCM-CLM-BAM-2CL |
| SAP_CA_BC_IC_LND_FIN_CM0_PC | Bank Relationship Management - Configuration | FCLM_BAM_ACCT_UID |  | FCLM_BAM_ACCT_UID | Enable Generation of Bank Account Unique IDs | 106994 | FIN-FSCM-CLM | FIN-FSCM-CLM-BAM-2CL |
| SAP_CA_BC_IC_LND_FIN_CM0_PC | Bank Relationship Management - Configuration | S_ER1_70001437 | S_ER1_70001437_TRAN | FCLM_BAM_ACCT_UID | Enable Generation of Bank Account Unique IDs | 106994 | FIN-FSCM-CLM | FIN-FSCM-CLM-BAM-2CL |
| SAP_CA_BC_IC_LND_FIN_CM0_PC | Bank Relationship Management - Configuration | FCLM_OVERDRAFT_TYPE |  | FCLM_OVRDRFTTP | Define Bank Account Overdraft Types | 107092 | FIN-FSCM-CLM | FIN-FSCM-CLM-BAM-2CL |
| SAP_CA_BC_IC_LND_FIN_CM0_PC | Bank Relationship Management - Configuration | S_ER1_70001426 | S_ER1_70001426_TRAN | FCLM_OVRDRFTTP | Define Bank Account Overdraft Types | 107092 | FIN-FSCM-CLM | FIN-FSCM-CLM-BAM-2CL |
| SAP_CA_BC_IC_LND_FIN_CM0_PC | Bank Relationship Management - Configuration | S_ER1_70001167 | S_ER1_70001167_TRAN | FCLMPOAV_TYPE | Define Power of Attorney Types | 106844 | FIN-FSCM-CLM | FIN-FSCM-CLM-BAM-2CL |
| SAP_CA_BC_IC_LND_FIN_CM0_PC | Bank Relationship Management - Configuration | FCLMPOA_FORM |  | FCLMPOA_FORM | Assign Form Templates to POA Types | 107063 | FIN-FSCM-CLM | FIN-FSCM-CLM-BAM-2CL |
| SAP_CA_BC_IC_LND_FIN_CM0_PC | Bank Relationship Management - Configuration | FCLMPOA_TYPE |  | FCLMPOAV_TYPE | Define Power of Attorney Types | 106844 | FIN-FSCM-CLM | FIN-FSCM-CLM-BAM-2CL |
| SAP_CA_BC_IC_LND_FIN_CM0_PC | Bank Relationship Management - Configuration | S_ER1_70001558 | S_ER1_70001558_TRAN | FCLMPOA_FORM | Assign Form Templates to POA Types | 107063 | FIN-FSCM-CLM | FIN-FSCM-CLM-BAM-2CL |
| SAP_CA_BC_IC_LND_FIN_CM0_PC | Bank Relationship Management - Configuration | S_ER1_70001709 | S_ER1_70001709_TRAN | FCLM_BF_CON_AUTH | Define Authorization Groups for Bank Fee Conditions | 107182 | FIN-FSCM-CLM | FIN-FSCM-CLM-BAM-2CL |
| SAP_CA_BC_IC_LND_FIN_CM0_PC | Bank Relationship Management - Configuration | FCLM_BF_C_AUTHGR |  | FCLM_BF_CON_AUTH | Define Authorization Groups for Bank Fee Conditions | 107182 | FIN-FSCM-CLM | FIN-FSCM-CLM-BAM-2CL |
| SAP_CA_BC_IC_LND_FIN_CM0_PC | Bank Relationship Management - Configuration | S_ER1_70001733 | S_ER1_70001733_TRAN | FCLM_BAM_SYSTGRP | Define System Groups | 107199 | FIN-FSCM-CLM | FIN-FSCM-CLM-BAM-2CL |
| SAP_CA_BC_IC_LND_FIN_CM0_PC | Bank Relationship Management - Configuration | FCLM_BAM_SYSTGRP |  | FCLM_BAM_SYSTGRP | Define System Groups | 107199 | FIN-FSCM-CLM | FIN-FSCM-CLM-BAM-2CL |
| SAP_CA_BC_IC_LND_FIN_CM0_PC | Bank Relationship Management - Configuration | FCLM_BAM_SYSTGRP_ASG |  | FCLM_BAM_SYSTGRP_ASG | Assign Logical Systems to System Groups | 107200 | FIN-FSCM-CLM | FIN-FSCM-CLM-BAM-2CL |
| SAP_CA_BC_IC_LND_FIN_CM0_PC | Bank Relationship Management - Configuration | S_ER1_70001734 | S_ER1_70001734_TRAN | FCLM_BAM_SYSTGRP_ASG | Assign Logical Systems to System Groups | 107200 | FIN-FSCM-CLM | FIN-FSCM-CLM-BAM-2CL |
| SAP_CA_BC_IC_LND_FIN_CM0_PC | Bank Relationship Management - Configuration | S_ER1_70001736 | S_ER1_70001736_TRAN | FCLM_BAM_ICON_AUTH | Define Authorization Groups for Interest Conditions | 107201 | FIN-FSCM-CLM | FIN-FSCM-CLM-BAM-2CL |
| SAP_CA_BC_IC_LND_FIN_CM0_PC | Bank Relationship Management - Configuration | FCLM_ICND_CAUTHG |  | FCLM_BAM_ICON_AUTH | Define Authorization Groups for Interest Conditions | 107201 | FIN-FSCM-CLM | FIN-FSCM-CLM-BAM-2CL |
| SAP_CA_BC_IC_LND_FIN_CM0_PC | Bank Relationship Management - Configuration | FCLM_BAI_CONDTYPE |  | FCLM_BAI_CONDTYPE | Define Condition Types for Bank Account Interest | 107261 | FIN-FSCM-CLM | FIN-FSCM-CLM-BAM-2CL |
| SAP_CA_BC_IC_LND_FIN_CM0_PC | Bank Relationship Management - Configuration | S_ER1_70001803 | S_ER1_70001803_TRAN | FCLM_BAI_CONDTYPE | Define Condition Types for Bank Account Interest | 107261 | FIN-FSCM-CLM | FIN-FSCM-CLM-BAM-2CL |
| SAP_CA_BC_IC_LND_FIN_CM0_PC | Bank Relationship Management - Configuration | FSBP_CUS_TPZ21 |  | VC_TPZ21 | Set Rating Procedures and Ratings | 103203 | FIN-FSCM-CLM | FS-BP |
| SAP_CA_BC_IC_LND_FIN_CM0_PC | Bank Relationship Management - Configuration | S_ABA_72000130 | S_ABA_72000130_TRAN | VC_TPZ21 | Set Rating Procedures and Ratings | 103203 | FIN-FSCM-CLM | FS-BP |
| SAP_CA_BC_CUR_CURR_SET_PC | Currencies - Current Settings | S_ER9_11001972 | S_ER9_11001972_TRAN | VC_FOT_HXF_ACT | Specify Currency Translation for Country/Region |  | FI-GL | FI-GL-GL-F-2CL |
| SAP_CA_BC_IC_LND_CRM_RP0_PC | In-House Repair - Configuration | S_ER1_83000167 | S_ER1_83000167_TRAN | CRMS4V_REPA_TVAK | Specify Settings for Returns Orders as Follow-Up | 105806 | CRM-S4-SRV-SVO | CRM-S4-IHR-2CL |
| SAP_CA_BC_IC_LND_MAO_SMA_PC | SAP Maintenance Assistant - Configuration | /MERP/52003821 | MERP_52003821_TRAN | /MERP/C_OPSHCND | Define Operation Push Conditions | 105958 | MOB-APP-MAO | MOB-APP-MAO-ERP |
| SAP_CA_BC_IC_LND_MAO_SMA_PC | SAP Maintenance Assistant - Configuration | /MERP/OPSHCND |  | /MERP/C_OPSHCND | Define Operation Push Conditions | 105958 | MOB-APP-MAO | MOB-APP-MAO-ERP |
| SAP_CA_BC_IC_LND_MAO_SMA_PC | SAP Maintenance Assistant - Configuration | /SMFND/71000018 | SMFND_71000018_TRAN | /SMFND/IMG_4MAGENT | Configure Dynamic Form Agents | 180102 | MOB-APP-MAO | MOB-APP-MAO-FND |
| SAP_CA_BC_IC_LND_MAO_SMA_PC | SAP Maintenance Assistant - Configuration | F8481 |  |  |  |  | MOB-APP-MAO |  |
| SAP_CA_BC_IC_LND_MAO_SMA_PC | SAP Maintenance Assistant - Configuration | MAO_DYN_FORM_AGENT |  | /SMFND/IMG_4MAGENT | Configure Dynamic Form Agents | 180102 | MOB-APP-MAO | MOB-APP-MAO-FND |
| SAP_CA_BC_IC_LND_MAO_SMA_PC | SAP Maintenance Assistant - Configuration | F8481 |  |  |  |  | MOB-APP-MAO |  |
| SAP_CA_BC_IC_LND_MAO_SMA_PC | SAP Maintenance Assistant - Configuration | /MERP/70001947 | MERP_70001947_TRAN | /MERP/SDF_UI_SW_ACT | Toggle Dynamic Forms UI Switch | 108103 | MOB-APP-MAO | MOB-APP-MAO-ERP |
| SAP_CA_BC_IC_LND_MAO_SMA_PC | SAP Maintenance Assistant - Configuration | /MERP/SDF_UI_SWITCH |  | /MERP/SDF_UI_SW_ACT | Toggle Dynamic Forms UI Switch | 108103 | MOB-APP-MAO | MOB-APP-MAO-ERP |
| SAP_CA_BC_IC_LND_RCM_PC | Case Management - Configuration | SCMGATTR_SESCAL_NEW |  | SCMGATTR_SESCAL | Create Values for Attribute 'Reason for Escalation' |  | BC-SRV-CM | BC-SRV-CM |
| SAP_CA_BC_IC_LND_RCM_PC | Case Management - Configuration | S_EKW_85000025 | S_EKW_85000025_TRAN | SCMGATTR_SESCAL | Create Values for Attribute 'Reason for Escalation' |  | BC-SRV-CM | BC-SRV-CM |
| SAP_CA_BC_IC_LND_LOG_CO_PC | Logistics for Colombia - Configuration | S_ER9_52004352 | S_ER9_52004352_TRAN | EDOC_CO_INCREJ | Define Number Range Interval for Rejection of Invoice | 106511 | CA-GTF-CSC-EDO-CO | CA-GTF-CSC-EDO-CO |
| SAP_CA_BC_IC_LND_LOG_CO_PC | Logistics for Colombia - Configuration | EDOC_CO_INCACC | EDOC_CO_INCACC_TRAN | EDOC_CO_INCACC | Define Number Range Interval for Acceptance of Invoice | 106512 | CA-GTF-CSC-EDO-CO | CA-GTF-CSC-EDO-CO |
| SAP_CA_BC_IC_LND_LOG_CO_PC | Logistics for Colombia - Configuration | EDOC_CO_INCREJ | EDOC_CO_INCREJ_TRAN | EDOC_CO_INCREJ | Define Number Range Interval for Rejection of Invoice | 106511 | CA-GTF-CSC-EDO-CO | CA-GTF-CSC-EDO-CO |
| SAP_CA_BC_IC_LND_LOG_CO_PC | Logistics for Colombia - Configuration | S_ER9_52004351 | S_ER9_52004351_TRAN | EDOC_CO_INCACC | Define Number Range Interval for Acceptance of Invoice | 106512 | CA-GTF-CSC-EDO-CO | CA-GTF-CSC-EDO-CO |
| SAP_CA_BC_IC_LND_LOG_CO_PC | Logistics for Colombia - Configuration | S_ER9_52004153 | S_ER9_52004153_TRAN | EDOC_CO_INCREC | Define Number Range Interval for Receipt of Goods | 106256 | CA-GTF-CSC-EDO-CO | CA-GTF-CSC-EDO-CO |
| SAP_CA_BC_IC_LND_LOG_CO_PC | Logistics for Colombia - Configuration | S_ER9_52004152 | S_ER9_52004152_TRAN | EDOC_CO_INCACK | Define Number Range Interval for Acknowledgement of Receipt | 106255 | CA-GTF-CSC-EDO-CO | CA-GTF-CSC-EDO-CO |
| SAP_CA_BC_IC_LND_LOG_CO_PC | Logistics for Colombia - Configuration | EDOC_CO_INCACK | EDOC_CO_INCACK_TRAN | EDOC_CO_INCACK | Define Number Range Interval for Acknowledgement of Receipt | 106255 | CA-GTF-CSC-EDO-CO | CA-GTF-CSC-EDO-CO |
| SAP_CA_BC_IC_LND_LOG_CO_PC | Logistics for Colombia - Configuration | S_EBJ_98000670 | S_EBJ_98000670_TRAN | EDOCONTCTRV | Activate Contingency for eDocument Type | 105737 | CA-GTF-CSC-EDO-CO | CA-GTF-CSC-EDO |
| SAP_CA_BC_IC_LND_LOG_CO_PC | Logistics for Colombia - Configuration | EDOC_CO_INCREC | EDOC_CO_INCREC_TRAN | EDOC_CO_INCREC | Define Number Range Interval for Receipt of Goods | 106256 | CA-GTF-CSC-EDO-CO | CA-GTF-CSC-EDO-CO |
| SAP_CA_BC_IC_LND_FIN_PRD1_PC | Production Cost Accounting - Event-Based Solution Configuration | S_ER9_11000946 | S_ER9_11000946_TRAN | SIMG_V_CK35_CLOUD | Define Valuation Variants per Plant | 102608 | CO-PC-OBJ | CO-PC-PCP-2CL |
| SAP_CA_BC_IC_LND_FIN_PRD1_PC | Production Cost Accounting - Event-Based Solution Configuration | S_ER9_11000945 | S_ER9_11000945_TRAN | SIMG_V_CK05_CLOUD | Define Valuation Variants for Material Cost Estimates | 102607 | CO-PC-OBJ | CO-PC-PCP-2CL |
| SAP_CA_BC_IC_LND_FIN_PRD1_PC | Production Cost Accounting - Event-Based Solution Configuration | S_ALR_87008203 | S_ALR_87008203_TRAN | SIMG_CFMENUORKKKZS2 | Define Costing Sheets | 102922 | CO-PC-OBJ | CO-OM-OPA-2CL |
| SAP_CA_BC_IC_LND_FIN_PRD1_PC | Production Cost Accounting - Event-Based Solution Configuration | S_ALR_87008192 | S_ALR_87008192_TRAN | SIMG_CFMENUORKKOKTZ | Define Cost Component Structure | 102427 | CO-PC-OBJ | CO-PC-PCP-2CL |
| SAP_CA_BC_IC_LND_FIN_PRD1_PC | Production Cost Accounting - Event-Based Solution Configuration | S_ER9_11001043 | S_ER9_11001043_TRAN | FCOVC_EBW | Event-Based WIP and Variance Posting | 103940 | CO-PC-OBJ | CO-PC-OBJ-ORD-2CL |
| SAP_CA_BC_IC_LND_FIN_PRD1_PC | Production Cost Accounting - Event-Based Solution Configuration | OKTZ |  | SIMG_CFMENUORKKOKTZ | Define Cost Component Structure | 102427 | CO-PC-OBJ | CO-PC-PCP-2CL |
| SAP_CA_BC_IC_LND_FIN_PRD1_PC | Production Cost Accounting - Event-Based Solution Configuration | OKZ2 |  | SIMG_ORKK_WERK_OKZ2 | Define Overhead Groups | 106748 | CO-PC-OBJ | CO-PC-OBJ-2CL |
| SAP_CA_BC_IC_LND_FIN_PRD1_PC | Production Cost Accounting - Event-Based Solution Configuration | S_ALR_87008033 | S_ALR_87008033_TRAN | SIMG_ORKK_WERK_OKZ2 | Define Overhead Groups | 106748 | CO-PC-OBJ | CO-PC-OBJ-2CL |
| SAP_CA_BC_IC_LND_FIN_PRD1_PC | Production Cost Accounting - Event-Based Solution Configuration | S_ALR_87008277 | S_ALR_87008277_TRAN | SIMG_PP3ORKKOKZ3 | Define Cost-Accounting-Relevant Default Values for Order Types and Plants | 106081 | CO-PC-OBJ | CO-PC-OBJ-2CL |
| SAP_CA_BC_IC_LND_FIN_PRD1_PC | Production Cost Accounting - Event-Based Solution Configuration | S_ALR_87008034 | S_ALR_87008034_TRAN | SIMG_ORKK_AUF_OKOG | Define Overhead Keys | 106747 | CO-PC-OBJ | CO-PC-OBJ-2CL |
| SAP_CA_BC_IC_LND_GL_MAP_PC | Renumber G/L Accounts - Configuration | S_ER9_52001887 | S_ER9_52001887_TRAN | CNV_2010C_MAP_X4 | Renumber G/L Accounts | 150000 | CA-DT-CNV-S4C | CA-DT-CNV-S4C |
| SAP_CA_BC_IC_LND_GL_MAP_PC | Renumber G/L Accounts - Configuration | CNV_2010C_MAP_X4 |  | CNV_2010C_MAP_X4 | Renumber G/L Accounts | 150000 | CA-DT-CNV-S4C | CA-DT-CNV-S4C |
| SAP_CA_BC_IC_LND_GL_MAP_PC | Renumber G/L Accounts - Configuration | F3026 | F3026_TRAN |  |  |  | CA-DT-CNV-S4C |  |
| SAP_CA_BC_IC_LND_BN0_PC | Accounting - Configuration | V_TACC_PRINCIPLE |  | V_TACC_PRINCIPLE | Define Accounting Principles |  | CA-BK | CA-BK |
| SAP_CA_BC_IC_LND_BN0_PC | Accounting - Configuration | S_SAL_71000077 | S_SAL_71000077_TRAN | V_TACC_PRINCIPLE | Define Accounting Principles |  | CA-BK | CA-BK |
| SAP_CA_BC_IC_LND_CA_DRF_PC | Data Replication Framework - Configuration | S_ER9_68000504 | S_ER9_68000504_TRAN | DRF_EXP_DEL | Specify Days after Which the Data from DRF is Deleted | 105844 | CA-MDG-DRF | CA-MDG-DRF |
| SAP_CA_BC_IC_LND_CA_DRF_PC | Data Replication Framework - Configuration | SSCUI_DRF_EXP_DAY |  | DRF_EXP_DEL | Specify Days after Which the Data from DRF is Deleted | 105844 | CA-MDG-DRF | CA-MDG-DRF |
| SAP_CA_BC_GLO_EDOC_CL_PC | Electronic Documents for Chile - Configuration | EDOC_CL_NRXML | EDOC_CL_NRXML_TRAN |  |  |  | CA-GTF-CSC-EDO-CL |  |
| SAP_CA_BC_GLO_EDOC_CL_PC | Electronic Documents for Chile - Configuration | EDO_CL_DTE_NUMBER | EDO_CL_DTE_NUMBER_TRAN |  |  |  | CA-GTF-CSC-EDO-CL |  |
| SAP_CA_BC_GLO_EDOC_CL_PC | Electronic Documents for Chile - Configuration | EDOC_CL_NRMAINT | EDOC_CL_NRMAINT_TRAN |  |  |  | CA-GTF-CSC-EDO-CL |  |
| SAP_CA_BC_IC_LND_CRM_FS0_PC | Service - SAP Field Service Management - Direct Integration(P2P) - Configuration | S_ER1_70001873 | S_ER1_70001873_TRAN | CRMS4_FSM_EQUIP_CAT | Configure Equipment Category | 107352 | CRM-S4-INT-FSM | CRM-S4-INT-FSM-2CL |
| SAP_CA_BC_IC_LND_CRM_FS0_PC | Service - SAP Field Service Management - Direct Integration(P2P) - Configuration | S_ER1_70001875 | S_ER1_70001875_TRAN | CRMS4_FSM_FLOC_CAT | Configure Functional Location Category | 107353 | CRM-S4-INT-FSM | CRM-S4-INT-FSM-2CL |
| SAP_CA_BC_IC_LND_CRM_FS0_PC | Service - SAP Field Service Management - Direct Integration(P2P) - Configuration | S_ER1_70001886 | S_ER1_70001886_TRAN | CRMS4_FSM_TOB_FILT | Configure Technical Object Filter | 107354 | CRM-S4-INT-FSM | CRM-S4-INT-FSM-2CL |
| SAP_CA_BC_IC_LND_CRM_FS0_PC | Service - SAP Field Service Management - Direct Integration(P2P) - Configuration | S_ER1_83000173 | S_ER1_83000173_TRAN | CRMS4_FSM_PFL_CKLTIN | Prefill Checklist Instances | 107335 | CRM-S4-INT-FSM | CRM-S4-INT-FSM-2CL |
| SAP_CA_BC_IC_LND_CRM_FS0_PC | Service - SAP Field Service Management - Direct Integration(P2P) - Configuration | S_ER1_83000171 | S_ER1_83000171_TRAN | CRMS4_FSM_LANG | Configure Language of Service Transaction | 106002 | CRM-S4-INT-FSM | CRM-S4-INT-FSM-2CL |
| SAP_CA_BC_IC_LND_CRM_FS0_PC | Service - SAP Field Service Management - Direct Integration(P2P) - Configuration | S_ER1_70001004 | S_ER1_70001004_TRAN | CRMS4VC_FSM_MC_REPLI | Configure Multiple Company Replication | 106807 | CRM-S4-INT-FSM | CRM-S4-INT-FSM-2CL |
| SAP_CA_BC_IC_LND_CRM_FS0_PC | Service - SAP Field Service Management - Direct Integration(P2P) - Configuration | S_ER1_83000172 | S_ER1_83000172_TRAN | CRMS4_FSM_TXT_TYPE | Configure Mapping for Text Types and Text Attributes | 106003 | CRM-S4-INT-FSM | CRM-S4-INT-FSM-2CL |
| SAP_CA_BC_IC_LND_WFD_OUT_PC | Workforce Integration Outbound - Configuration | WFD_D_OUT_STAT |  | V_WFD_D_OUT_STAT | Map Outbound Work Assignment Status | 106183 | CA-WFD-INT | CA-WFD-BL |
| SAP_CA_BC_IC_LND_WFD_OUT_PC | Workforce Integration Outbound - Configuration | WFD_D_OUT_SUF |  | V_WFD_D_OUT_SUF | Map Outbound Name Suffixes | 106184 | CA-WFD-INT | CA-WFD-BL |
| SAP_CA_BC_IC_LND_WFD_OUT_PC | Workforce Integration Outbound - Configuration | WFD_D_OUT_FOA |  | V_WFD_D_OUT_FOA | Map Outbound Form of Address | 106182 | CA-WFD-INT | CA-WFD-BL |
| SAP_CA_BC_IC_LND_WFD_OUT_PC | Workforce Integration Outbound - Configuration | WFD_D_OUT_ATL |  | V_WFD_D_OUT_ATL | Map Outbound Academic Titles | 106180 | CA-WFD-INT | CA-WFD-BL |
| SAP_CA_BC_IC_LND_WFD_OUT_PC | Workforce Integration Outbound - Configuration | WFD_D_OUT_PRE |  | V_WFD_D_OUT_PRE | Map Outbound Name Prefixes | 106185 | CA-WFD-INT | CA-WFD-BL |
| SAP_CA_BC_IC_LND_WFD_OUT_PC | Workforce Integration Outbound - Configuration | WFD_D_OUT_AATL |  | V_WFD_D_OUT_AATL | Map Outbound Additional Academic Titles | 106186 | CA-WFD-INT | CA-WFD-BL |
| SAP_CA_BC_IC_LND_WFD_OUT_PC | Workforce Integration Outbound - Configuration | S_ER9_52004032 | S_ER9_52004032_TRAN | V_WFD_D_OUT_FOA | Map Outbound Form of Address | 106182 | CA-WFD-INT | CA-WFD-BL |
| SAP_CA_BC_IC_LND_WFD_OUT_PC | Workforce Integration Outbound - Configuration | S_ER9_52004031 | S_ER9_52004031_TRAN | V_WFD_D_OUT_STAT | Map Outbound Work Assignment Status | 106183 | CA-WFD-INT | CA-WFD-BL |
| SAP_CA_BC_IC_LND_WFD_OUT_PC | Workforce Integration Outbound - Configuration | S_ER9_52004030 | S_ER9_52004030_TRAN | V_WFD_D_OUT_SUF | Map Outbound Name Suffixes | 106184 | CA-WFD-INT | CA-WFD-BL |
| SAP_CA_BC_IC_LND_WFD_OUT_PC | Workforce Integration Outbound - Configuration | S_ER9_52004029 | S_ER9_52004029_TRAN | V_WFD_D_OUT_PRE | Map Outbound Name Prefixes | 106185 | CA-WFD-INT | CA-WFD-BL |
| SAP_CA_BC_IC_LND_WFD_OUT_PC | Workforce Integration Outbound - Configuration | S_ER9_52004028 | S_ER9_52004028_TRAN | V_WFD_D_OUT_AATL | Map Outbound Additional Academic Titles | 106186 | CA-WFD-INT | CA-WFD-BL |
| SAP_CA_BC_IC_LND_WFD_OUT_PC | Workforce Integration Outbound - Configuration | S_ER9_52004027 | S_ER9_52004027_TRAN | V_WFD_D_OUT_ATL | Map Outbound Academic Titles | 106180 | CA-WFD-INT | CA-WFD-BL |
| SAP_CA_BC_IC_LND_WFD_OUT_PC | Workforce Integration Outbound - Configuration | WFD_D_OUT_RGN |  | V_WFD_D_OUT_RGN | Map Outbound Region | 106181 | CA-WFD-INT | CA-WFD-BL |
| SAP_CA_BC_IC_LND_WFD_OUT_PC | Workforce Integration Outbound - Configuration | S_ER9_52004025 | S_ER9_52004025_TRAN | V_WFD_D_OUT_RGN | Map Outbound Region | 106181 | CA-WFD-INT | CA-WFD-BL |
| SAP_CA_BC_IC_LND_FIN_CF0_PC | Central Finance - System Specific Configuration | S_ER9_11000493 | S_ER9_11000493_TRAN | FIN_CFIN_CLD_SRC_GEN | Central Finance Subsidiary - General Settings | 101042 | FI-CF | FI-CF-2CL |
| SAP_CA_BC_ACC_GL_CORR_PC | Accounting - Data Changes | F4622 | F4622_TRAN |  |  |  | FI-GL |  |
| SAP_CA_BC_ACC_GL_CORR_PC | Accounting - Data Changes | SP01_SIMPLE | SP01_SIMPLE_GLO_TRAN |  |  |  | FI-GL |  |
| SAP_CA_BC_IC_LND_FIN_SR_MX_PC | Statutory Reporting for Mexico - Configuration | S_EBJ_98000122 | S_EBJ_98000122_TRAN | V_T059Z_MX | Assign Withholding Tax Keys to Withholding Tax Codes | 105177 | FI-LOC-FI-MX | FI-LOC-FI-LA |
| SAP_CA_BC_IC_LND_FIN_SR_MX_PC | Statutory Reporting for Mexico - Configuration | S_EB5_05000026 | S_EB5_05000026_TRAN | MXTVO | Define Transaction Types for Vendors | 105629 | FI-LOC-FI-MX | FI-LOC-FI-MX |
| SAP_CA_BC_IC_LND_FIN_SR_MX_PC | Statutory Reporting for Mexico - Configuration | S_ER1_70001688 | S_ER1_70001688_TRAN | FIMXV_RGN_CLFN | Configure Mexico Border Region | 107254 | FI-LOC-FI-MX | FI-LOC-FI-MX |
| SAP_CA_BC_IC_LND_FIN_SR_MX_PC | Statutory Reporting for Mexico - Configuration | FIMXV_RGN_CLFN |  | FIMXV_RGN_CLFN | Configure Mexico Border Region | 107254 | FI-LOC-FI-MX | FI-LOC-FI-MX |
| SAP_CA_BC_IC_LND_FIN_SR_MX_PC | Statutory Reporting for Mexico - Configuration | S_ER9_11001474 | S_ER9_11001474_TRAN | V_FIMX_PAYM_MAP | Specify Mapping for External Payment Method | 103451 | FI-LOC-FI-MX | FI-LOC-FI-MX |
| SAP_CA_BC_IC_LND_FIN_INT_PC | Finance Integration - Configuration | S_ER9_11002897 | S_ER9_11002897_TRAN | FARV_ML_CONFIG | Cash Application Service Configuration | 106578 | FI-AR-AR | FI-FIO-AR-2CL |
| SAP_CA_BC_IC_LND_FIN_INT_PC | Finance Integration - Configuration | FDP2 | FDP2_TRAN | FINS_AR_DP_SCEN | Activate SAP Digital Payments Scenarios | 102563 | FI-AR-AR | FIN-FSCM-DP-DP-2CL |
| SAP_CA_BC_IC_LND_FIN_INT_PC | Finance Integration - Configuration | S_ER9_11000407 | S_ER9_11000407_TRAN | FINS_AR_DP_SCEN | Activate SAP Digital Payments Scenarios | 102563 | FI-AR-AR | FIN-FSCM-DP-DP-2CL |
| SAP_CA_BC_IC_LND_FIN_INT_PC | Finance Integration - Configuration | FDP3 | FDP3_TRAN | FINS_AR_DP_TAXCODE | Maintain Tax Codes for Posting Charges | 102593 | FI-AR-AR | FIN-FSCM-DP-DP-2CL |
| SAP_CA_BC_IC_LND_FIN_INT_PC | Finance Integration - Configuration | S_ER9_11000406 | S_ER9_11000406_TRAN | FINS_AR_DP_ACT | Activate SAP Digital Payments Add-On | 102562 | FI-AR-AR | FIN-FSCM-DP-DP-2CL |
| SAP_CA_BC_IC_LND_FIN_INT_PC | Finance Integration - Configuration | S_ER9_11000661 | S_ER9_11000661_TRAN | FINS_AR_DP_TAXCODE | Maintain Tax Codes for Posting Charges | 102593 | FI-AR-AR | FIN-FSCM-DP-DP-2CL |
| SAP_CA_BC_IC_LND_FIN_INT_PC | Finance Integration - Configuration | FDP1 | FDP1_TRAN | FINS_AR_DP_ACT | Activate SAP Digital Payments Add-On | 102562 | FI-AR-AR | FIN-FSCM-DP-DP-2CL |
| SAP_CA_BC_IC_LND_FIN_INT_PC | Finance Integration - Configuration | S_ER9_11000406 | S_ER9_11000406_TRAN | FINS_AR_DP_ACT | Activate SAP Digital Payments Add-On | 102562 | FI-AR-AR | FIN-FSCM-DP-DP-2CL |
| SAP_CA_BC_IC_LND_FIN_INT_PC | Finance Integration - Configuration | S_ER9_11000661 | S_ER9_11000661_TRAN | FINS_AR_DP_TAXCODE | Maintain Tax Codes for Posting Charges | 102593 | FI-AR-AR | FIN-FSCM-DP-DP-2CL |
| SAP_CA_BC_IC_LND_FIN_INT_PC | Finance Integration - Configuration | S_ER9_11000377 | S_ER9_11000377_TRAN | FINS_AR_ML_SETTINGS | Basic Settings | 103060 | FI-AR-AR | FI-FIO-AR-2CL |
| SAP_CA_BC_IC_LND_FIN_INT_PC | Finance Integration - Configuration | S_ER9_11000549 | S_ER9_11000549_TRAN | FINSC_DRF_SFEC1 | Define Custom Field Mapping for Cost Centers | 101051 | FI-AR-AR | CO-OM-2CL |
| SAP_CA_BC_IC_LND_FIN_INT_PC | Finance Integration - Configuration | S_ER9_11000553 | S_ER9_11000553_TRAN | FINSC_DRF_SFEC2 | Define Custom Field Mapping for Bank Master Data | 101052 | FI-AR-AR | FI-GL-GL-2CL |
| SAP_CA_BC_IC_LND_CAL_PC | System Factory Calendar - Configuration | SCAL |  | SIMG_CFMENUSAPCOY05 | Maintain Calendar | 180007 | BC-SRV-ASF-CAL | BC-SRV-ASF-CAL |
| SAP_CA_BC_IC_LND_CAL_PC | System Factory Calendar - Configuration | S_BCE_68000182 | S_BCE_68000182_TRAN | SIMG_CFMENUSAPCOY05 | Maintain Calendar | 180007 | BC-SRV-ASF-CAL | BC-SRV-ASF-CAL |
| SAP_CA_BC_IC_LND_MM_IM0_PC | Inventory Management - Configuration | S_ALR_87000481 | S_ALR_87000481_TRAN | SIMG_CFMENUOLMBOMBP | Allow Freezing of Book Inventory Balance in Storage Location | 103745 | MM-IM-IAM | MM-IM-GF-2CL |
| SAP_CA_BC_IC_LND_MM_IM0_PC | Inventory Management - Configuration | S_ALR_87002253 | S_ALR_87002253_TRAN | SIMG_CFMENUOLMWOMWD | Group Together Valuation Areas | 103790 | MM-IM-IAM | LO-MD-MM-2CL |
| SAP_CA_BC_IC_LND_MM_IM0_PC | Inventory Management - Configuration | OMWD |  | SIMG_CFMENUOLMWOMWD | Group Together Valuation Areas | 103790 | MM-IM-IAM | LO-MD-MM-2CL |
| SAP_CA_BC_IC_LND_MM_IM0_PC | Inventory Management - Configuration | OMJJ_SSCUI |  | SIMGH_OMJJ_SSCUI | Copy of Movement Type | 103898 | MM-IM-IAM | MM-IM-GF-2CL |
| SAP_CA_BC_IC_LND_MM_IM0_PC | Inventory Management - Configuration | MB_T001L_HU_SSCUI |  | SIMG_T001L_HU_SSCUI | HU Requirement for Storage Locations | 103836 | MM-IM-IAM | MM-IM-GF-2CL |
| SAP_CA_BC_IC_LND_MM_IM0_PC | Inventory Management - Configuration | SSCUI_T158B_XKZBEW |  | SIMG_T158B_XKZBEW | Set Manual Account Assignment | 103899 | MM-IM-IAM | MM-IM-GF-2CL |
| SAP_CA_BC_IC_LND_MM_IM0_PC | Inventory Management - Configuration | S_P00_07000059 | S_P00_07000059_TRAN | SIMG_OLMB_CUST_FIELD | Field Selection per Movement Type | 103831 | MM-IM-IAM | MM-IM-GF-2CL |
| SAP_CA_BC_IC_LND_MM_IM0_PC | Inventory Management - Configuration | S_ER9_52002380 | S_ER9_52002380_TRAN | SIMG_T001L_HU_SSCUI | HU Requirement for Storage Locations | 103836 | MM-IM-IAM | MM-IM-GF-2CL |
| SAP_CA_BC_IC_LND_MM_IM0_PC | Inventory Management - Configuration | S_ALR_87000403 | S_ALR_87000403_TRAN | SIMG_CFMENUOLMBOMBT | Define Number Assignment for Material and Physical Inventory Documents | 103896 | MM-IM-IAM | MM-IM-GF-2CL |
| SAP_CA_BC_IC_LND_MM_IM0_PC | Inventory Management - Configuration | S_ER9_52002413 | S_ER9_52002413_TRAN | SIMG_V_160M_SSCUI | Set System Messages in Inventory Management | 103897 | MM-IM-IAM | MM-IM-GF-2CL |
| SAP_CA_BC_IC_LND_MM_IM0_PC | Inventory Management - Configuration | S_ER9_52002414 | S_ER9_52002414_TRAN | SIMG_T158B_XKZBEW | Set Manual Account Assignment | 103899 | MM-IM-IAM | MM-IM-GF-2CL |
| SAP_CA_BC_IC_LND_MM_IM0_PC | Inventory Management - Configuration | OMCQ |  | SIMG_V_160M_SSCUI | Set System Messages in Inventory Management | 103897 | MM-IM-IAM | MM-IM-GF-2CL |
| SAP_CA_BC_IC_LND_MM_IM0_PC | Inventory Management - Configuration | OMW_SPLIT_VAL |  | SIMG_VC_T149 | Activate Split Valuation for Valuation Area | 101717 | MM-IM-IAM | MM-IM-GF-2CL |
| SAP_CA_BC_IC_LND_MM_IM0_PC | Inventory Management - Configuration | OMBT |  | SIMG_CFMENUOLMBOMBT | Define Number Assignment for Material and Physical Inventory Documents | 103896 | MM-IM-IAM | MM-IM-GF-2CL |
| SAP_CA_BC_IC_LND_MM_IM0_PC | Inventory Management - Configuration | S_ER9_52002521 | S_ER9_52002521_TRAN | SIMG_V_156N_VC_SSCUI | Set Reversal Movement Types | 104062 | MM-IM-IAM | MM-IM-GF-2CL |
| SAP_CA_BC_IC_LND_MM_IM0_PC | Inventory Management - Configuration | SSCUI_V_156NVC |  | SIMG_V_156N_VC_SSCUI | Set Reversal Movement Types | 104062 | MM-IM-IAM | MM-IM-GF-2CL |
| SAP_CA_BC_IC_LND_MM_IM0_PC | Inventory Management - Configuration | S_ALR_87006957 | S_ALR_87006957_TRAN | SIMG_CFMENUOLMBCHNEU | Define Batch Creation for Goods Movements | 103517 | MM-IM-IAM | MM-IM-GF-2CL |
| SAP_CA_BC_IC_LND_MM_IM0_PC | Inventory Management - Configuration | S_ALR_87000528 | S_ALR_87000528_TRAN | SIMG_CFMENUOLMBOMCO | Cycle Counting | 103357 | MM-IM-IAM | MM-IM-GF-2CL |
| SAP_CA_BC_IC_LND_MM_IM0_PC | Inventory Management - Configuration | S_ALR_87000430 | S_ALR_87000430_TRAN | SIMG_CFMENUOLMBOMJ1 | Allow Negative Stocks | 103183 | MM-IM-IAM | MM-IM-GF-2CL |
| SAP_CA_BC_IC_LND_MM_IM0_PC | Inventory Management - Configuration | S_ALR_87000171 | S_ALR_87000171_TRAN | J_1ADEFINE_REL_MTYPE | Assign Document Class to Movement Types | 102777 | MM-IM-IAM | MM-IM-GF-2CL |
| SAP_CA_BC_IC_LND_MM_IM0_PC | Inventory Management - Configuration | S_ALR_87000379 | S_ALR_87000379_TRAN | SIMG_CFMENUOLMB001KL | Price Differences for Subcontract Orders at Goods Receipt | 103169 | MM-IM-IAM | MM-IM-GF-2CL |
| SAP_CA_BC_IC_LND_MM_IM0_PC | Inventory Management - Configuration | S_ALR_87000134 | S_ALR_87000134_TRAN | J_1AASSIGN_BR_PLSL | Assign Issuing Subsidiary to Plant/Storage Location | 102776 | MM-IM-IAM | MM-IM-GF-2CL |
| SAP_CA_BC_IC_LND_MM_IM0_PC | Inventory Management - Configuration | S_ALR_87000032 | S_ALR_87000032_TRAN | SIMG_CFMENUOLMBBEFIS | Define Strategies for Stock Determination | 103211 | MM-IM-IAM | MM-IM-GF-2CL |
| SAP_CA_BC_IC_LND_MM_IM0_PC | Inventory Management - Configuration | OX09 |  | SIMG_CFMENUSAPCOX09 | Maintain Storage Location | 000000 | MM-IM-IAM | LO-MD-PL-2CL |
| SAP_CA_BC_IC_LND_MM_IM0_PC | Inventory Management - Configuration | OMJ1 |  | SIMG_CFMENUOLMBOMJ1 | Allow Negative Stocks | 103183 | MM-IM-IAM | MM-IM-GF-2CL |
| SAP_CA_BC_IC_LND_MM_IM0_PC | Inventory Management - Configuration | OMCO |  | SIMG_CFMENUOLMBOMCO | Cycle Counting | 103357 | MM-IM-IAM | MM-IM-GF-2CL |
| SAP_CA_BC_IC_LND_MM_IM0_PC | Inventory Management - Configuration | OSPX |  | SIMG_CFMENUOLMBBEFIS | Define Strategies for Stock Determination | 103211 | MM-IM-IAM | MM-IM-GF-2CL |
| SAP_CA_BC_IC_LND_MM_IM0_PC | Inventory Management - Configuration | S_ALR_87002336 | S_ALR_87002336_TRAN | SIMG_CFMENUOLMWOMW1 | Define Price Control for Material Types | 102133 | MM-IM-IAM | LO-MD-MM-2CL |
| SAP_CA_BC_IC_LND_MM_IM0_PC | Inventory Management - Configuration | S_ER9_52001531 | S_ER9_52001531_TRAN | SIMG_OLMB_INVTCONSGR | Define Inventory Consumption Groups | 103204 | MM-IM-IAM | MM-IM-GF-2CL |
| SAP_CA_BC_IC_LND_MM_IM0_PC | Inventory Management - Configuration | S_ER9_52001933 | S_ER9_52001933_TRAN | SIMGH_OMJJ_SSCUI | Copy of Movement Type | 103898 | MM-IM-IAM | MM-IM-GF-2CL |
| SAP_CA_BC_IC_LND_MM_IM0_PC | Inventory Management - Configuration | S_P99_41000271 | S_P99_41000271_TRAN | SIMG_MMIM_V_156Q_VC | Set QM Check and Delivery Type for Each Movement Type | 103356 | MM-IM-IAM | MM-IM-GF-2CL |
| SAP_CA_BC_IC_LND_MM_IM0_PC | Inventory Management - Configuration | S_ALR_87007549 | S_ALR_87007549_TRAN | SIMG_CFMENUSAPCOX09 | Maintain Storage Location | 000000 | MM-IM-IAM | LO-MD-PL-2CL |
| SAP_CA_BC_IC_LND_MM_IM0_PC | Inventory Management - Configuration | S_ER9_52001129 | S_ER9_52001129_TRAN | SIMG_VC_T149 | Activate Split Valuation for Valuation Area | 101717 | MM-IM-IAM | MM-IM-GF-2CL |
| SAP_CA_BC_IC_LND_MM_IM0_PC | Inventory Management - Configuration | MB_V_156X_VC_SSCUI |  | SIMG_V_156X_VC_SSCUI | Account Modification | 103170 | MM-IM-IAM | MM-IM-GF-2CL |
| SAP_CA_BC_IC_LND_MM_IM0_PC | Inventory Management - Configuration | MB_MMIM_REP_LN_LIM |  | SIMG_V_MMIM_REP_LIM | Set Record Limits in Reports | 105687 | MM-IM-IAM | MM-IM-GF-2CL |
| SAP_CA_BC_IC_LND_MM_IM0_PC | Inventory Management - Configuration | S_ALR_87006965 | S_ALR_87006965_TRAN | SIMG_CFMENUOLMBOMCV | Activate Batch Classification for Goods Movements in IM | 104329 | MM-IM-IAM | LO-BM-2CL |
| SAP_CA_BC_IC_LND_MM_IM0_PC | Inventory Management - Configuration | OMCV |  | SIMG_CFMENUOLMBOMCV | Activate Batch Classification for Goods Movements in IM | 104329 | MM-IM-IAM | LO-BM-2CL |
| SAP_CA_BC_IC_LND_MM_IM0_PC | Inventory Management - Configuration | S_ER9_52002696 | S_ER9_52002696_TRAN | SIMG_V_156X_VC_SSCUI | Account Modification | 103170 | MM-IM-IAM | MM-IM-GF-2CL |
| SAP_CA_BC_IC_LND_MM_IM0_PC | Inventory Management - Configuration | S_ER9_52003279 | S_ER9_52003279_TRAN | SIMG_V_MMIM_REP_LIM | Set Record Limits in Reports | 105687 | MM-IM-IAM | MM-IM-GF-2CL |
| SAP_CA_BC_IC_LND_MM_IM0_PC | Inventory Management - Configuration | S_ER9_52002936 | S_ER9_52002936_TRAN | SIMG_PRINT_ITEM | Assign Printout Document Type | 105353 | MM-IM-IAM | MM-IM-GF-2CL |
| SAP_CA_BC_IC_LND_MM_IM0_PC | Inventory Management - Configuration | SSCUI_PRINT_ITEM |  | SIMG_PRINT_ITEM | Assign Printout Document Type | 105353 | MM-IM-IAM | MM-IM-GF-2CL |
| SAP_CA_BC_IC_LND_MM_IM0_PC | Inventory Management - Configuration | S_ALR_87000026 | S_ALR_87000026_TRAN | SIMG_CFMENUOLMBBFMM | Inventory Management | 105725 | MM-IM-IAM | MM-IM-GF-2CL |
| SAP_CA_BC_IC_LND_MM_IM0_PC | Inventory Management - Configuration | OMJ_EXPIRATION_CHECK |  | SIMG_CFMENUOLMBOMJ5 | Set Expiration Date Check | 101913 | MM-IM-IAM | MM-IM-GF-2CL |
| SAP_CA_BC_IC_LND_MM_IM0_PC | Inventory Management - Configuration | OMB_STORE_LOC_AUTO |  | SIMG_CFMENUOLMBOMB2 | Create Storage Location Automatically | 101914 | MM-IM-IAM | MM-IM-GF-2CL |
| SAP_CA_BC_IC_LND_MM_IM0_PC | Inventory Management - Configuration | OMB_REASON_CODE |  | SIMG_CFMENUOLMBOMBS | Record Reason for Goods Movements | 101091 103222 | MM-IM-IAM | MM-IM-GF-2CL |
| SAP_CA_BC_IC_LND_MM_IM0_PC | Inventory Management - Configuration | OMB_CONTROL_REASON |  | SIMG_CFMENUOLMBOMBS | Record Reason for Goods Movements | 101091 103222 | MM-IM-IAM | MM-IM-GF-2CL |
| SAP_CA_BC_IC_LND_MM_IM0_PC | Inventory Management - Configuration | S_ALR_87001531 | S_ALR_87001531_TRAN | SIMG_CFMENUOLMBOMJ5 | Set Expiration Date Check | 101913 | MM-IM-IAM | MM-IM-GF-2CL |
| SAP_CA_BC_IC_LND_MM_IM0_PC | Inventory Management - Configuration | S_ALR_87000421 | S_ALR_87000421_TRAN | SIMG_CFMENUOLMBOMB2 | Create Storage Location Automatically | 101914 | MM-IM-IAM | MM-IM-GF-2CL |
| SAP_CA_BC_IC_LND_MM_IM0_PC | Inventory Management - Configuration | S_ALR_87000504 | S_ALR_87000504_TRAN | SIMG_CFMENUOLMBOMBS | Record Reason for Goods Movements | 101091 103222 | MM-IM-IAM | MM-IM-GF-2CL |
| SAP_CA_BC_IC_LND_MM_IM0_PC | Inventory Management - Configuration | OMJ_EXPIRA_CHECK_PL |  | SIMG_CFMENUOLMBOMJ5 | Set Expiration Date Check | 101913 | MM-IM-IAM | MM-IM-GF-2CL |
| SAP_CA_BC_IC_LND_MM_IM0_PC | Inventory Management - Configuration | OMB_STORE_PL_AUTO |  | SIMG_CFMENUOLMBOMB2 | Create Storage Location Automatically | 101914 | MM-IM-IAM | MM-IM-GF-2CL |
| SAP_CA_BC_IC_LND_MM_IM0_PC | Inventory Management - Configuration | S_ALR_87000387 | S_ALR_87000387_TRAN | SIMG_CFMENUOLMBOMBZ | Allow Reversal of GR Despite Invoices | 106043 | MM-IM-IAM | MM-IM-GF-2CL |
| SAP_CA_BC_IC_LND_MM_IM0_PC | Inventory Management - Configuration | S_ER9_52003929 | S_ER9_52003929_TRAN | SIMG_V_T001W_OID | Assign Object ID (OID) to Plant | 106041 | MM-IM-IAM | MM-IM-GF-2CL |
| SAP_CA_BC_IC_LND_MM_IM0_PC | Inventory Management - Configuration | S_ER9_52003939 | S_ER9_52003939_TRAN | SIMG_V_159L_PI_STG | Settings for Physical Inventory | 106073 | MM-IM-IAM | MM-IM-GF-2CL |
| SAP_CA_BC_IC_LND_MM_IM0_PC | Inventory Management - Configuration | MB_V_159L_PI_STG |  | SIMG_V_159L_PI_STG | Settings for Physical Inventory | 106073 | MM-IM-IAM | MM-IM-GF-2CL |
| SAP_CA_BC_IC_LND_MM_IM0_PC | Inventory Management - Configuration | OMBZ |  | SIMG_CFMENUOLMBOMBZ | Allow Reversal of GR Despite Invoices | 106043 | MM-IM-IAM | MM-IM-GF-2CL |
| SAP_CA_BC_IC_LND_MM_IM0_PC | Inventory Management - Configuration | MB_T001W_OID |  | SIMG_V_T001W_OID | Assign Object ID (OID) to Plant | 106041 | MM-IM-IAM | MM-IM-GF-2CL |
| SAP_CA_BC_IC_LND_MM_IM0_PC | Inventory Management - Configuration | MB_V_6WP3_LBL_TYPE |  | SIMG_V_6WP3_LBL_TYPE | Define Label Types | 106187 | MM-IM-IAM | MM-IM-GF-2CL |
| SAP_CA_BC_IC_LND_MM_IM0_PC | Inventory Management - Configuration | S_ER9_52004036 | S_ER9_52004036_TRAN | SIMG_V_6WP3_LBL_TYPE | Define Label Types | 106187 | MM-IM-IAM | MM-IM-GF-2CL |
| SAP_CA_BC_IC_LND_MM_IM0_PC | Inventory Management - Configuration | MB_V_6WP4_LBL_FORM |  | SIMG_V_6WP4_LBL_FORM | Define Label Forms | 106188 | MM-IM-IAM | MM-IM-GF-2CL |
| SAP_CA_BC_IC_LND_MM_IM0_PC | Inventory Management - Configuration | S_ER9_52004038 | S_ER9_52004038_TRAN | SIMG_V_6WP4_LBL_FORM | Define Label Forms | 106188 | MM-IM-IAM | MM-IM-GF-2CL |
| SAP_CA_BC_IC_LND_MM_IM0_PC | Inventory Management - Configuration | OMW_SPLIT_VAL_GLOB |  | SIMG_VC_149_GLOBAL | Activate Split Valuation for Global Data | 105535 | MM-IM-IAM | MM-IM-GF-2CL |
| SAP_CA_BC_IC_LND_MM_IM0_PC | Inventory Management - Configuration | S_ER9_52003042 | S_ER9_52003042_TRAN | SIMG_VC_149_GLOBAL | Activate Split Valuation for Global Data | 105535 | MM-IM-IAM | MM-IM-GF-2CL |
| SAP_CA_BC_IC_LND_MM_IM0_PC | Inventory Management - Configuration | S_ER9_52004202 | S_ER9_52004202_TRAN | SIMG_MMIM_V_SCNASGMN | Assign Parsing and Hardware Settings to SAP Fiori App | 106284 | MM-IM-IAM | MM-IM-PI-2CL |
| SAP_CA_BC_IC_LND_MM_IM0_PC | Inventory Management - Configuration | S_ER9_52004207 | S_ER9_52004207_TRAN | SIMG_V_159E_LBL_QDET | Define Quantity Determination for Labels | 106268 | MM-IM-IAM | MM-IM-GF-2CL |
| SAP_CA_BC_IC_LND_MM_IM0_PC | Inventory Management - Configuration | MB_V_159E_LBL_QDET |  | SIMG_V_159E_LBL_QDET | Define Quantity Determination for Labels | 106268 | MM-IM-IAM | MM-IM-GF-2CL |
| SAP_CA_BC_IC_LND_MM_IM0_PC | Inventory Management - Configuration | S_ER9_52004200 | S_ER9_52004200_TRAN | SIMG_MMIM_C_SCANHRDW | Define Settings for Scanner Hardware | 106285 | MM-IM-IAM | MM-IM-PI-2CL |
| SAP_CA_BC_IC_LND_MM_IM0_PC | Inventory Management - Configuration | S_ALR_87009216 | S_ALR_87009216_TRAN | SIMG_OLMB_V_159L_EI | Settings for Physical Inventory | 106608 | MM-IM-IAM | MM-IM-GF-2CL |
| SAP_CA_BC_IC_LND_MM_IM0_PC | Inventory Management - Configuration | V_T001W |  | SIMG_CFMENUSAPCOX10 | Define Plant | 000000 | MM-IM-IAM | LO-MD-PL-2CL |
| SAP_CA_BC_IC_LND_MM_IM0_PC | Inventory Management - Configuration | S_ER9_52004206 | S_ER9_52004206_TRAN | SIMG_MMIM_C_BRCODSTT | Define Barcode Parsing | 106286 | MM-IM-IAM | MM-IM-PI-2CL |
| SAP_CA_BC_IC_LND_MM_IM0_PC | Inventory Management - Configuration | S_ALR_87007507 | S_ALR_87007507_TRAN | SIMG_CFMENUSAPCOX10 | Define Plant | 000000 | MM-IM-IAM | LO-MD-PL-2CL |
| SAP_CA_BC_IC_LND_MM_IM0_PC | Inventory Management - Configuration | S_ER1_70001166 | S_ER1_70001166_TRAN | SIMG_V_156_G_SSCUI | Control: Reason for Movement | 103222 | MM-IM-IAM | MM-IM-GF-2CL |
| SAP_CA_BC_IC_LND_MM_IM0_PC | Inventory Management - Configuration | S_ER1_70001165 | S_ER1_70001165_TRAN | SIMG_V157D_SSCUI | Reason for Movement | 101091 | MM-IM-IAM | MM-IM-GF-2CL |
| SAP_CA_BC_IC_LND_MM_IM0_PC | Inventory Management - Configuration | S_ER1_70001054 | S_ER1_70001054_TRAN | SIMG_VC_PI_TOL_GRP | Manage Tolerances for Physical Inventory Differences | 106788 | MM-IM-IAM | MM-IM-PI-2CL |
| SAP_CA_BC_IC_LND_MM_IM0_PC | Inventory Management - Configuration | S_ER1_70001163 | S_ER1_70001163_TRAN | SIMG_V_156_MHD_SSCUI | Set Expiration Date Check | 101913 | MM-IM-IAM | MM-IM-GF-2CL |
| SAP_CA_BC_IC_LND_MM_IM0_PC | Inventory Management - Configuration | S_ER1_70001676 | S_ER1_70001676_TRAN | SIMG_RES_STORAGELOC | Extend Material Master for Storage Locations in Reservations | 107145 | MM-IM-IAM | MM-IM-GF-2CL |
| SAP_CA_BC_IC_LND_MM_IM0_PC | Inventory Management - Configuration | S_ER1_70001162 | S_ER1_70001162_TRAN | SIMG_V_156_X_SSCUI | Create Storage Location Automatically | 101914 | MM-IM-IAM | MM-IM-GF-2CL |
| SAP_CA_BC_IC_LND_MM_IM0_PC | Inventory Management - Configuration | S_ER1_70001345 | S_ER1_70001345_TRAN | SIMG_PURCHASEACCOUNT | Activate Purchase Account in Company Code | 106961 | MM-IM-IAM | MM-IM-GF-2CL |
| SAP_CA_BC_IC_LND_EHS_HS0_PC | EHS Health and Safety Management - Configuration | S_ER1_70001682 | S_ER1_70001682_TRAN | EHHSS_RMTRX | Configure Risk Matrix | 107161 | EHS-SUS-FND-EHS | EHS-SUS-HS |
| SAP_CA_BC_IC_LND_EHS_HS0_PC | EHS Health and Safety Management - Configuration | EHHSS_RMTRX |  | EHHSS_RMTRX | Configure Risk Matrix | 107161 | EHS-SUS-FND-EHS | EHS-SUS-HS |
| SAP_CA_BC_IC_LND_EHS_HS0_PC | EHS Health and Safety Management - Configuration | S_ER1_70000521 | S_ER1_70000521_TRAN | EHHSS_RAS2_TYPE | Configure Risk Assessment Types | 106451 | EHS-SUS-FND-EHS | EHS-SUS-HS |
| SAP_CA_BC_IC_LND_EHS_HS0_PC | EHS Health and Safety Management - Configuration | S_EM4_11000279 | S_EM4_11000279_TRAN | EHFNDV_PURP | Specify Purposes | 106987 | EHS-SUS-FND-EHS | EHS-SUS-FND-EHS |
| SAP_CA_BC_IC_LND_EHS_HS0_PC | EHS Health and Safety Management - Configuration | EHHSS_RAS2_TYPE |  | EHHSS_RAS2_TYPE | Configure Risk Assessment Types | 106451 | EHS-SUS-FND-EHS | EHS-SUS-HS |
| SAP_CA_BC_IC_LND_EHS_HS0_PC | EHS Health and Safety Management - Configuration | EHFNDV_PURP |  | EHFNDV_PURP | Specify Purposes | 106987 | EHS-SUS-FND-EHS | EHS-SUS-FND-EHS |
| SAP_CA_BC_IC_LND_EHS_HS0_PC | EHS Health and Safety Management - Configuration | S_EM4_11000280 | S_EM4_11000280_TRAN | EHFNDV_METH | Specify Methods of Use | 106682 | EHS-SUS-FND-EHS | EHS-SUS-FND-EHS |
| SAP_CA_BC_IC_LND_EHS_HS0_PC | EHS Health and Safety Management - Configuration | EHFNDV_METH |  | EHFNDV_METH | Specify Methods of Use | 106682 | EHS-SUS-FND-EHS | EHS-SUS-FND-EHS |
| SAP_CA_BC_IC_LND_EHS_HS0_PC | EHS Health and Safety Management - Configuration | S_EH7_11000046 | S_EH7_11000046_TRAN | EHHSS_RAS_HAZREG | Configure Hazard and Control Register | 106331 | EHS-SUS-FND-EHS | EHS-SUS-HS |
| SAP_CA_BC_IC_LND_EHS_HS0_PC | EHS Health and Safety Management - Configuration | S_ER1_70000500 | S_ER1_70000500_TRAN | EHHSS_FSI_SUBST_S02 | Configure Safety Instructions for Substance (Compliance View) | 106239 | EHS-SUS-FND-EHS | EHS-SUS-HS |
| SAP_CA_BC_IC_LND_EHS_HS0_PC | EHS Health and Safety Management - Configuration | EHHSS_RAS_HAZREG |  | EHHSS_RAS_HAZREG | Configure Hazard and Control Register | 106331 | EHS-SUS-FND-EHS | EHS-SUS-HS |
| SAP_CA_BC_IC_LND_EHS_HS0_PC | EHS Health and Safety Management - Configuration | S_ER1_70000263 | S_ER1_70000263_TRAN | EHHSS_FSI_EQP | Configure Safety Instructions for Equipment | 105858 | EHS-SUS-FND-EHS | EHS-SUS-HS |
| SAP_CA_BC_IC_LND_EHS_HS0_PC | EHS Health and Safety Management - Configuration | EHHSS_FSI_EQP |  | EHHSS_FSI_EQP | Configure Safety Instructions for Equipment | 105858 | EHS-SUS-FND-EHS | EHS-SUS-HS |
| SAP_CA_BC_IC_LND_EHS_HS0_PC | EHS Health and Safety Management - Configuration | EHHSS_FSI_SUBST_S02 |  | EHHSS_FSI_SUBST_S02 | Configure Safety Instructions for Substance (Compliance View) | 106239 | EHS-SUS-FND-EHS | EHS-SUS-HS |
| SAP_CA_BC_IC_LND_EHS_HS0_PC | EHS Health and Safety Management - Configuration | S_ER1_70001877 | S_ER1_70001877_TRAN | EHHSS_HSI2_AUT | Specify Authorization Groups for Hazardous Substance Inventory | 107357 | EHS-SUS-FND-EHS | EHS-SUS-HS |
| SAP_CA_BC_IC_LND_EHS_HS0_PC | EHS Health and Safety Management - Configuration | EHHSS_HSI2_AUT |  | EHHSS_HSI2_AUT | Specify Authorization Groups for Hazardous Substance Inventory | 107357 | EHS-SUS-FND-EHS | EHS-SUS-HS |
| SAP_CA_BC_IC_LND_FIN_SCO_PC | Service Controlling - Configuration | F4945 | F4945_TRAN |  |  |  | CO-OM |  |
| SAP_CA_BC_IC_LND_FIN_SCO_PC | Service Controlling - Configuration | F4886 | F4886_TRAN |  |  |  | CO-OM |  |
| SAP_CA_BC_IC_LND_FIN_SCO_PC | Service Controlling - Configuration | F7818 | F7818_TRAN |  |  |  | CO-OM |  |
| SAP_FIN_BC_TRM_FUNDS_CONF_PC | TRM - Configuration for Funds | S_E39_23000019 | S_E39_23000019_TRAN | IDCFMVSETX_RATE | Define Tax Rates for Tax Calculation | 106001 | FI-LOC-FI-BR | FI-LOC-TRM |
| SAP_FIN_BC_TRM_FUNDS_CONF_PC | TRM - Configuration for Funds | S_ER9_68000556 | S_ER9_68000556_TRAN | IDCFMV_FUND_ACT | Activate Features of Fund Taxation | 106000 | FI-LOC-FI-BR | FI-LOC-TRM |
| SAP_FIN_BC_TRM_FUNDS_CONF_PC | TRM - Configuration for Funds | S_ER9_68000557 | S_ER9_68000557_TRAN | IDCFMV_TAX_UPTYP | Assign Update Types to Tax Categories | 105999 | FI-LOC-FI-BR | FI-LOC-TRM |
| SAP_CORE_BC_CBC_STA_PC | Business Configuration - Stagings | SCBC_STA_UI_SIMPLE | SCBC_STA_UI_SIMPLE_TRAN |  |  |  | BC-CBC-STA |  |
| SAP_CORE_BC_CBC_STA_PC | Business Configuration - Stagings | SCBC_STA_LIST_SIMPLE | SCBC_STA_LIST_SIMPLE_TRAN |  |  |  | BC-CBC-STA |  |
| SAP_GLO_BC_DOC_CMPLNC_CO_PC | Globalization - Document Compliance for Colombia | S_EBJ_98000850 | S_EBJ_98000850_TRAN | EDOCORANGESV | Enter Approved Number Ranges for Invoices | 106860 | CA-GTF-CSC-EDO-CO | CA-GTF-CSC-EDO-CO |
| SAP_GLO_BC_DOC_CMPLNC_CO_PC | Globalization - Document Compliance for Colombia | EDOC_CO_RANGES | EDOC_CO_RANGES_TRAN |  |  |  | CA-GTF-CSC-EDO-CO |  |
| SAP_GLO_BC_DOC_CMPLNC_CO_PC | Globalization - Document Compliance for Colombia | EDOC_CO_NUMBER | EDOC_CO_NUMBER_TRAN |  |  |  | CA-GTF-CSC-EDO-CO |  |
| SAP_GLO_BC_DOC_CMPLNC_CO_PC | Globalization - Document Compliance for Colombia | S_EBJ_98000851 | S_EBJ_98000851_TRAN | EDOCONUMBERV | Assign Number Ranges to eDocument Types | 106859 | CA-GTF-CSC-EDO-CO | CA-GTF-CSC-EDO-CO |
| SAP_CA_BC_IC_LND_FIN_WT_CO_PC | Statutory Reporting WT for Colombia - Configuration | S_EBJ_45000239 | S_EBJ_45000239_TRAN | V_J_1_T059WTK | Define Withholding Tax Constants | 105892 | FI-LOC-FI-CO | FI-AP-AP-Q1 |
| SAP_CA_BC_IC_LND_FIN_WT_CO_PC | Statutory Reporting WT for Colombia - Configuration | S_SL0_21000001 | S_SL0_21000001_TRAN | V_T059Z_WITHCD2 | Define Withholding Tax Keys | 106576 106576 | FI-LOC-FI-CO | FI-LOC-FI-LA |
| SAP_CA_BC_IC_LND_FIN_WT_CO_PC | Statutory Reporting WT for Colombia - Configuration | S_ER1_70001323 | S_ER1_70001323_TRAN | V_FIWTGEN_CTRYCT_CO | Maintain Double Taxation Agreement Countries | 106931 | FI-LOC-FI-CO | FI-AP-AP-Q1 |
| SAP_CA_BC_IC_LND_FIN_WT_CO_PC | Statutory Reporting WT for Colombia - Configuration | S_SL0_21000002 | S_SL0_21000002_TRAN | V_T059Z_CO | Assign Withholding Tax Keys to Withholding Tax Codes | 105852 | FI-LOC-FI-CO | FI-LOC-FI-LA |
| SAP_CA_BC_IC_LND_SCM_ATP4_PC | ATP - Object and Value Determination Configuration | S_ER9_52003480 | S_ER9_52003480_TRAN | OVD_DEF_USAGE_TYPE | Define Usage Types | 106011 | CA-ATP | CA-ATP-OVD-2CL |
| SAP_CA_BC_IC_LND_BPM_INB_PC | Business Process Management - Inbox Configuration | S_YI3_39000437 | S_YI3_39000437_TRAN | SWFFLEXDECRSN | Edit Decision Reasons | 104740 | BC-BMT-WFM-RUN-TGW | BC-BMT-WFM |
| SAP_CA_BC_IC_LND_BPM_INB_PC | Business Process Management - Inbox Configuration | SWFFLEXDECRSN |  | SWFFLEXDECRSN | Edit Decision Reasons | 104740 | BC-BMT-WFM-RUN-TGW | BC-BMT-WFM |
| SAP_CA_BC_IC_LND_BPM_INB_PC | Business Process Management - Inbox Configuration | S_YI3_39000307 | S_YI3_39000307_TRAN | SWFSTEPACTIONDEACT | Edit Profiles to Deactivate Inbox Actions | 103105 | BC-BMT-WFM-RUN-TGW | BC-BMT-WFM |
| SAP_CA_BC_IC_LND_BPM_INB_PC | Business Process Management - Inbox Configuration | SWFSTEPACTIONDEACT |  | SWFSTEPACTIONDEACT | Edit Profiles to Deactivate Inbox Actions | 103105 | BC-BMT-WFM-RUN-TGW | BC-BMT-WFM |
| SAP_CA_BC_IC_LND_BPM_INB_PC | Business Process Management - Inbox Configuration | S_YI3_39000681 | S_YI3_39000681_TRAN | SWF_CPTC_DEFREG | Limit exposure of Task Definitions to SAP Task Center | 106343 | BC-BMT-WFM-RUN-TGW | BC-BMT-WFM |
| SAP_CA_BC_IC_LND_BPM_INB_PC | Business Process Management - Inbox Configuration | SWF_TASK_SPI_DEF |  | SWF_CPTC_DEFREG | Limit exposure of Task Definitions to SAP Task Center | 106343 | BC-BMT-WFM-RUN-TGW | BC-BMT-WFM |
| SAP_CA_BC_IC_LND_FIN_WT_PE_PC | Statutory Reporting WT for Peru - Configuration | S_ER9_11002721 | S_ER9_11002721_TRAN | V_FIWTPE_BEPS | Assign BEPS Code to Region | 106418 | FI-LOC-FI-PE | FI-AP-AP-Q1 |
| SAP_CA_BC_IC_LND_FIN_GL_GR_PC | General Ledger for Greece - Configuration | S_ER9_52002628 | S_ER9_52002628_TRAN | LOC_GR_CUSTACC | Maintain G/L Accounts for Invoice Types | 106243 | FI-LOC-FI-GR | FI-LOC-FI-GR |
| SAP_CA_BC_IC_LND_FIN_GL_GR_PC | General Ledger for Greece - Configuration | EDOC_GR_CUST_C |  | LOC_GR_CUSTACC | Maintain G/L Accounts for Invoice Types | 106243 | FI-LOC-FI-GR | FI-LOC-FI-GR |
| SAP_CA_BC_IC_LND_OIL_FLOG4_PC | Field Logistics Logistics Tracking - Configuration | S_ER1_70000515 | S_ER1_70000515_TRAN | FLOG_MT_V_PROF | Define Logistics Tracking Profile | 106419 | CA-FL | CA-FL-MT |
| SAP_CA_BC_IC_LND_CIC_ATP_PC | ATP Snapshot - Configuration | S_ER9_52003971 | S_ER9_52003971_TRAN | V_CIC_ATP_CHK_RL | Set Availability Checking Rule for ATP Snapshot | 106082 | CA-ICS-INT | CA-ICS-INT |
| SAP_CA_BC_IC_LND_GLO_EDC_PC | Electronic Document Consistency - Configuration | S_ER1_70000822 | S_ER1_70000822_TRAN | EDCBLARTMAPV | Assign Journal Entry Types to Comparison Types | 106684 | FI-LOC-LO | CA-GTF-CSC-EDC |
| SAP_CA_BC_IC_LND_GLO_EDC_PC | Electronic Document Consistency - Configuration | S_ER1_70000850 | S_ER1_70000850_TRAN | EDCTOLERANCEV | Define Tolerance Limits for Amount Mismatch | 106707 | FI-LOC-LO | CA-GTF-CSC-EDC |
| SAP_CA_BC_IC_LND_GLO_EDC_PC | Electronic Document Consistency - Configuration | S_ER9_52004250 | S_ER9_52004250_TRAN | EDC_COMPENABLEMENT_V | Enable Consistency Checks for Company Codes | 106403 | FI-LOC-LO | CA-GTF-CSC-EDC |
| SAP_CA_BC_IC_LND_FIN_FYV_PC | Financials - Fiscal Year Variant - Configuration | OB29 |  | SIMG_CFMENUORFBOB29 | Maintain Fiscal Year Variant |  | BC-SRV-ASF-FYV | BC-SRV-ASF-FYV |
| SAP_CA_BC_IC_LND_FIN_FYV_PC | Financials - Fiscal Year Variant - Configuration | S_ALR_87003662 | S_ALR_87003662_TRAN | SIMG_CFMENUORFBOB29 | Maintain Fiscal Year Variant |  | BC-SRV-ASF-FYV | BC-SRV-ASF-FYV |
| SAP_CA_BC_IC_LND_PLM_PLMSI_PC | PLM System Integration - Configuration | /PLMC/84000088 | PLMC_84000088_TRAN | /PLMC/V_DM_CL_CC | Define Domain Model Criticality Code | 106521 | PLM-INT-TC | PLM-INT-TC-2CL |
| SAP_CA_BC_IC_LND_PLM_PLMSI_PC | PLM System Integration - Configuration | /PLMF/DM_CL_CC |  | /PLMC/V_DM_CL_CC | Define Domain Model Criticality Code | 106521 | PLM-INT-TC | PLM-INT-TC-2CL |
| SAP_CA_BC_IC_LND_PLM_PLMSI_PC | PLM System Integration - Configuration | /PLMC/84000101 | PLMC_84000101_TRAN | /PLMC/V_DM_CL_VT | Define Domain Model Vendor Type | 106482 | PLM-INT-TC | PLM-INT-TC-2CL |
| SAP_CA_BC_IC_LND_PLM_PLMSI_PC | PLM System Integration - Configuration | /PLMF/DM_CL_CT |  | /PLMC/V_DM_CL_CT | Define Domain Model Change Type | 106477 | PLM-INT-TC | PLM-INT-TC-2CL |
| SAP_CA_BC_IC_LND_PLM_PLMSI_PC | PLM System Integration - Configuration | /PLMC/84000087 | PLMC_84000087_TRAN | /PLMC/V_DM_CL_CT | Define Domain Model Change Type | 106477 | PLM-INT-TC | PLM-INT-TC-2CL |
| SAP_CA_BC_IC_LND_PLM_PLMSI_PC | PLM System Integration - Configuration | /PLMF/DM_CL_WA |  | /PLMC/V_DM_CL_WA | Define Domain Model Work Area Type | 106481 | PLM-INT-TC | PLM-INT-TC-2CL |
| SAP_CA_BC_IC_LND_PLM_PLMSI_PC | PLM System Integration - Configuration | /PLMF/DM_CL_VT |  | /PLMC/V_DM_CL_VT | Define Domain Model Vendor Type | 106482 | PLM-INT-TC | PLM-INT-TC-2CL |
| SAP_CA_BC_IC_LND_PLM_PLMSI_PC | PLM System Integration - Configuration | /PLMF/DM_CL_ST |  | /PLMC/V_DM_CL_ST | Define Domain Model Structure Type | 106484 | PLM-INT-TC | PLM-INT-TC-2CL |
| SAP_CA_BC_IC_LND_PLM_PLMSI_PC | PLM System Integration - Configuration | /PLMF/DM_CL_SF |  | /PLMC/V_DM_CL_SF | Define Domain Model Semantic File Type | 106473 | PLM-INT-TC | PLM-INT-TC-2CL |
| SAP_CA_BC_IC_LND_PLM_PLMSI_PC | PLM System Integration - Configuration | /PLMF/DM_CL_SC |  | /PLMC/V_DM_CL_SC | Define Domain Model Status Code | 106476 | PLM-INT-TC | PLM-INT-TC-2CL |
| SAP_CA_BC_IC_LND_PLM_PLMSI_PC | PLM System Integration - Configuration | /PLMF/DM_CL_RT |  | /PLMC/V_DM_CL_RT | Define Domain Model Relation Type | 106472 | PLM-INT-TC | PLM-INT-TC-2CL |
| SAP_CA_BC_IC_LND_PLM_PLMSI_PC | PLM System Integration - Configuration | /PLMF/DM_CL_PT |  | /PLMC/V_DM_CL_PT | Define Domain Model Product Type | 106470 | PLM-INT-TC | PLM-INT-TC-2CL |
| SAP_CA_BC_IC_LND_PLM_PLMSI_PC | PLM System Integration - Configuration | /PLMF/DM_CL_OL |  | /PLMC/V_DM_CL_OL | Define Domain Model Production Operation List Type | 106471 | PLM-INT-TC | PLM-INT-TC-2CL |
| SAP_CA_BC_IC_LND_PLM_PLMSI_PC | PLM System Integration - Configuration | /PLMF/DM_CL_MC |  | /PLMC/V_DM_CL_MC | Define Domain Model Maturity Code | 106483 | PLM-INT-TC | PLM-INT-TC-2CL |
| SAP_CA_BC_IC_LND_PLM_PLMSI_PC | PLM System Integration - Configuration | /PLMF/DM_CL_EIC |  | /PLMC/V_DM_CL_EI | Define Domain Model Embedded Inspection Characteristics Type | 106474 | PLM-INT-TC | PLM-INT-TC-2CL |
| SAP_CA_BC_IC_LND_PLM_PLMSI_PC | PLM System Integration - Configuration | /PLMF/DM_CL_LT |  | /PLMC/V_DM_CL_LT | Define Domain Model Linkage Type | 106479 | PLM-INT-TC | PLM-INT-TC-2CL |
| SAP_CA_BC_IC_LND_PLM_PLMSI_PC | PLM System Integration - Configuration | /PLMF/DM_CL_FT |  | /PLMC/V_DM_CL_FT | Define Domain Model Factory Type | 106478 | PLM-INT-TC | PLM-INT-TC-2CL |
| SAP_CA_BC_IC_LND_PLM_PLMSI_PC | PLM System Integration - Configuration | /PLMF/DM_CL_DT |  | /PLMC/V_DM_CL_DT | Define Domain Model Document Type | 106469 | PLM-INT-TC | PLM-INT-TC-2CL |
| SAP_CA_BC_IC_LND_PLM_PLMSI_PC | PLM System Integration - Configuration | /PLMC/DM_CL_MT |  | /PLMC/V_DM_CL_MT | Define Domain Model MIME Type | 106480 | PLM-INT-TC | PLM-INT-TC-2CL |
| SAP_CA_BC_IC_LND_PLM_PLMSI_PC | PLM System Integration - Configuration | /PLMC/84000102 | PLMC_84000102_TRAN | /PLMC/V_DM_CL_WA | Define Domain Model Work Area Type | 106481 | PLM-INT-TC | PLM-INT-TC-2CL |
| SAP_CA_BC_IC_LND_PLM_PLMSI_PC | PLM System Integration - Configuration | /PLMC/84000100 | PLMC_84000100_TRAN | /PLMC/V_DM_CL_ST | Define Domain Model Structure Type | 106484 | PLM-INT-TC | PLM-INT-TC-2CL |
| SAP_CA_BC_IC_LND_PLM_PLMSI_PC | PLM System Integration - Configuration | /PLMC/84000097 | PLMC_84000097_TRAN | /PLMC/V_DM_CL_RT | Define Domain Model Relation Type | 106472 | PLM-INT-TC | PLM-INT-TC-2CL |
| SAP_CA_BC_IC_LND_PLM_PLMSI_PC | PLM System Integration - Configuration | /PLMC/84000098 | PLMC_84000098_TRAN | /PLMC/V_DM_CL_SF | Define Domain Model Semantic File Type | 106473 | PLM-INT-TC | PLM-INT-TC-2CL |
| SAP_CA_BC_IC_LND_PLM_PLMSI_PC | PLM System Integration - Configuration | /PLMC/84000089 | PLMC_84000089_TRAN | /PLMC/V_DM_CL_DT | Define Domain Model Document Type | 106469 | PLM-INT-TC | PLM-INT-TC-2CL |
| SAP_CA_BC_IC_LND_PLM_PLMSI_PC | PLM System Integration - Configuration | /PLMC/84000099 | PLMC_84000099_TRAN | /PLMC/V_DM_CL_SC | Define Domain Model Status Code | 106476 | PLM-INT-TC | PLM-INT-TC-2CL |
| SAP_CA_BC_IC_LND_PLM_PLMSI_PC | PLM System Integration - Configuration | /PLMC/84000096 | PLMC_84000096_TRAN | /PLMC/V_DM_CL_OL | Define Domain Model Production Operation List Type | 106471 | PLM-INT-TC | PLM-INT-TC-2CL |
| SAP_CA_BC_IC_LND_PLM_PLMSI_PC | PLM System Integration - Configuration | /PLMC/84000093 | PLMC_84000093_TRAN | /PLMC/V_DM_CL_LT | Define Domain Model Linkage Type | 106479 | PLM-INT-TC | PLM-INT-TC-2CL |
| SAP_CA_BC_IC_LND_PLM_PLMSI_PC | PLM System Integration - Configuration | /PLMC/84000090 | PLMC_84000090_TRAN | /PLMC/V_DM_CL_EI | Define Domain Model Embedded Inspection Characteristics Type | 106474 | PLM-INT-TC | PLM-INT-TC-2CL |
| SAP_CA_BC_IC_LND_PLM_PLMSI_PC | PLM System Integration - Configuration | /PLMC/84000095 | PLMC_84000095_TRAN | /PLMC/V_DM_CL_PT | Define Domain Model Product Type | 106470 | PLM-INT-TC | PLM-INT-TC-2CL |
| SAP_CA_BC_IC_LND_PLM_PLMSI_PC | PLM System Integration - Configuration | /PLMC/84000091 | PLMC_84000091_TRAN | /PLMC/V_DM_CL_FT | Define Domain Model Factory Type | 106478 | PLM-INT-TC | PLM-INT-TC-2CL |
| SAP_CA_BC_IC_LND_PLM_PLMSI_PC | PLM System Integration - Configuration | /PLMC/84000094 | PLMC_84000094_TRAN | /PLMC/V_DM_CL_MC | Define Domain Model Maturity Code | 106483 | PLM-INT-TC | PLM-INT-TC-2CL |
| SAP_CA_BC_IC_LND_PLM_PLMSI_PC | PLM System Integration - Configuration | /PLMC/84000085 | PLMC_84000085_TRAN | /PLMC/V_DM_CL_MT | Define Domain Model MIME Type | 106480 | PLM-INT-TC | PLM-INT-TC-2CL |
| SAP_CA_BC_IC_LND_PLM_PLMSI_PC | PLM System Integration - Configuration | /PLMC/84000131 | PLMC_84000131_TRAN | /PLMC/V_DM_CL_IC | Define Domain Model Inspection Characteristics Type | 106475 | PLM-INT-TC | PLM-INT-TC-2CL |
| SAP_CA_BC_IC_LND_PLM_PLMSI_PC | PLM System Integration - Configuration | /PLMF/DM_CL_IC |  | /PLMC/V_DM_CL_IC | Define Domain Model Inspection Characteristics Type | 106475 | PLM-INT-TC | PLM-INT-TC-2CL |
| SAP_CA_BC_IC_LND_PLM_PLMSI_PC | PLM System Integration - Configuration | /PLMC/DV_MMT |  | /PLMC/VC_DV_MMT | Define Mapping for MIME Types | 106536 | PLM-INT-TC | PLM-INT-TC-2CL |
| SAP_CA_BC_IC_LND_PLM_PLMSI_PC | PLM System Integration - Configuration | /PLMC/84000086 | PLMC_84000086_TRAN | /PLMC/VC_DV_MMT | Define Mapping for MIME Types | 106536 | PLM-INT-TC | PLM-INT-TC-2CL |
| SAP_CA_BC_IC_LND_PLM_PLMSI_PC | PLM System Integration - Configuration | /PLMC/84000078 | PLMC_84000078_TRAN | /PLMC/VC_SCEN | Define Scenario and Version | 106522 | PLM-INT-TC | PLM-INT-TC-2CL |
| SAP_CA_BC_IC_LND_PLM_PLMSI_PC | PLM System Integration - Configuration | /PLMC/SCEN |  | /PLMC/VC_SCEN | Define Scenario and Version | 106522 | PLM-INT-TC | PLM-INT-TC-2CL |
| SAP_CA_BC_IC_LND_PLM_PLMSI_PC | PLM System Integration - Configuration | /PLMC/SCN_DETN |  | /PLMC/V_SCN_DETN | Define Scenario Determination Rules | 106523 | PLM-INT-TC | PLM-INT-TC-2CL |
| SAP_CA_BC_IC_LND_PLM_PLMSI_PC | PLM System Integration - Configuration | /PLMC/84000103 | PLMC_84000103_TRAN | /PLMC/V_SCN_DETN | Define Scenario Determination Rules | 106523 | PLM-INT-TC | PLM-INT-TC-2CL |
| SAP_CA_BC_IC_LND_PLM_PLMSI_PC | PLM System Integration - Configuration | /PLMF/CNNR |  | /PLMC/CNNR | Maintain Constraint Net ID Number Range | 106529 | PLM-INT-TC | PLM-INT-TC-2CL |
| SAP_CA_BC_IC_LND_PLM_PLMSI_PC | PLM System Integration - Configuration | /PLMC/84000121 | PLMC_84000121_TRAN | /PLMC/CNNR | Maintain Constraint Net ID Number Range | 106529 | PLM-INT-TC | PLM-INT-TC-2CL |
| SAP_CA_BC_IC_LND_PLM_PLMSI_PC | PLM System Integration - Configuration | /PLMC/84000122 | PLMC_84000122_TRAN | /PLMC/VOR | Maintain Dependency Number Range | 106530 | PLM-INT-TC | PLM-INT-TC-2CL |
| SAP_CA_BC_IC_LND_PLM_PLMSI_PC | PLM System Integration - Configuration | /PLMF/VORNR |  | /PLMC/VOR | Maintain Dependency Number Range | 106530 | PLM-INT-TC | PLM-INT-TC-2CL |
| SAP_CA_BC_IC_LND_PLM_PLMSI_PC | PLM System Integration - Configuration | /PLMC/CO |  | /PLMC/VC_CO | Map DM Change Object to SAP Change Master | 106534 | PLM-INT-TC | PLM-INT-TC-2CL |
| SAP_CA_BC_IC_LND_PLM_PLMSI_PC | PLM System Integration - Configuration | /PLMC/84000112 | PLMC_84000112_TRAN | /PLMC/SSN | Maintain Selection Set Number Range | 106533 | PLM-INT-TC | PLM-INT-TC-2CL |
| SAP_CA_BC_IC_LND_PLM_PLMSI_PC | PLM System Integration - Configuration | /PLMF/CGNR |  | /PLMC/CGN | Maintain Code Group Number Range | 106532 | PLM-INT-TC | PLM-INT-TC-2CL |
| SAP_CA_BC_IC_LND_PLM_PLMSI_PC | PLM System Integration - Configuration | /PLMF/SSNR |  | /PLMC/SSN | Maintain Selection Set Number Range | 106533 | PLM-INT-TC | PLM-INT-TC-2CL |
| SAP_CA_BC_IC_LND_PLM_PLMSI_PC | PLM System Integration - Configuration | /PLMC/84000111 | PLMC_84000111_TRAN | /PLMC/CGN | Maintain Code Group Number Range | 106532 | PLM-INT-TC | PLM-INT-TC-2CL |
| SAP_CA_BC_IC_LND_PLM_PLMSI_PC | PLM System Integration - Configuration | /PLMC/84000106 | PLMC_84000106_TRAN | /PLMC/VC_CO | Map DM Change Object to SAP Change Master | 106534 | PLM-INT-TC | PLM-INT-TC-2CL |
| SAP_CA_BC_IC_LND_PLM_PLMSI_PC | PLM System Integration - Configuration | /PLMC/FCTY |  | /PLMC/VC_FCTY | Map DM Factory to SAP Plant | 106537 | PLM-INT-TC | PLM-INT-TC-2CL |
| SAP_CA_BC_IC_LND_PLM_PLMSI_PC | PLM System Integration - Configuration | /PLMC/84000109 | PLMC_84000109_TRAN | /PLMC/VC_FCTY | Map DM Factory to SAP Plant | 106537 | PLM-INT-TC | PLM-INT-TC-2CL |
| SAP_CA_BC_IC_LND_PLM_PLMSI_PC | PLM System Integration - Configuration | /PLMC/84000114 | PLMC_84000114_TRAN | /PLMC/VC_PV | Map DM Product Version to SAP Material Master | 106540 | PLM-INT-TC | PLM-INT-TC-2CL |
| SAP_CA_BC_IC_LND_PLM_PLMSI_PC | PLM System Integration - Configuration | /PLMC/PV |  | /PLMC/VC_PV | Map DM Product Version to SAP Material Master | 106540 | PLM-INT-TC | PLM-INT-TC-2CL |
| SAP_CA_BC_IC_LND_PLM_PLMSI_PC | PLM System Integration - Configuration | /PLMC/84000117 | PLMC_84000117_TRAN | /PLMC/VC_SV | Map DM Structure Version to SAP Classic BOM | 106543 | PLM-INT-TC | PLM-INT-TC-2CL |
| SAP_CA_BC_IC_LND_PLM_PLMSI_PC | PLM System Integration - Configuration | /PLMC/SV |  | /PLMC/VC_SV | Map DM Structure Version to SAP Classic BOM | 106543 | PLM-INT-TC | PLM-INT-TC-2CL |
| SAP_CA_BC_IC_LND_PLM_PLMSI_PC | PLM System Integration - Configuration | /PLMC/VOR |  | /PLMC/VC_VOR | Map DM Variant Option Rule to SAP Object Dependency | 106545 | PLM-INT-TC | PLM-INT-TC-2CL |
| SAP_CA_BC_IC_LND_PLM_PLMSI_PC | PLM System Integration - Configuration | /PLMC/84000120 | PLMC_84000120_TRAN | /PLMC/VC_VOR | Map DM Variant Option Rule to SAP Object Dependency | 106545 | PLM-INT-TC | PLM-INT-TC-2CL |
| SAP_CA_BC_IC_LND_PLM_PLMSI_PC | PLM System Integration - Configuration | /PLMC/VDR |  | /PLMC/VC_VDR | Map DM Vendor to SAP Business Partner | 106549 | PLM-INT-TC | PLM-INT-TC-2CL |
| SAP_CA_BC_IC_LND_PLM_PLMSI_PC | PLM System Integration - Configuration | /PLMC/84000128 | PLMC_84000128_TRAN | /PLMC/VC_VDR | Map DM Vendor to SAP Business Partner | 106549 | PLM-INT-TC | PLM-INT-TC-2CL |
| SAP_CA_BC_IC_LND_PLM_PLMSI_PC | PLM System Integration - Configuration | /PLMC/84000124 | PLMC_84000124_TRAN | /PLMC/V_VO_BV | Define Variant Option Boolean Values | 106547 | PLM-INT-TC | PLM-INT-TC-2CL |
| SAP_CA_BC_IC_LND_PLM_PLMSI_PC | PLM System Integration - Configuration | /PLMC/FVM |  | /PLMC/VC_FVM | Define Field and Value Mapping | 106525 | PLM-INT-TC | PLM-INT-TC-2CL |
| SAP_CA_BC_IC_LND_PLM_PLMSI_PC | PLM System Integration - Configuration | /PLMC/84000110 | PLMC_84000110_TRAN | /PLMC/VC_POL | Map DM POL to SAP Routing | 106538 | PLM-INT-TC | PLM-INT-TC-2CL |
| SAP_CA_BC_IC_LND_PLM_PLMSI_PC | PLM System Integration - Configuration | /PLMC/DV_FE |  | /PLMC/V_DV_FE | Define Files for Document Info Record | 106550 | PLM-INT-TC | PLM-INT-TC-2CL |
| SAP_CA_BC_IC_LND_PLM_PLMSI_PC | PLM System Integration - Configuration | /PLMF/VO_BV |  | /PLMC/V_VO_BV | Define Variant Option Boolean Values | 106547 | PLM-INT-TC | PLM-INT-TC-2CL |
| SAP_CA_BC_IC_LND_PLM_PLMSI_PC | PLM System Integration - Configuration | /PLMC/VD |  | /PLMC/VC_VD | Map DM Variant Definition to SAP Class | 106544 | PLM-INT-TC | PLM-INT-TC-2CL |
| SAP_CA_BC_IC_LND_PLM_PLMSI_PC | PLM System Integration - Configuration | /PLMC/84000125 | PLMC_84000125_TRAN | /PLMC/VC_VO | Map DM Variant Option to SAP Characteristic | 106546 | PLM-INT-TC | PLM-INT-TC-2CL |
| SAP_CA_BC_IC_LND_PLM_PLMSI_PC | PLM System Integration - Configuration | /PLMC/84000132 | PLMC_84000132_TRAN | /PLMC/V_DV_FE | Define Files for Document Info Record | 106550 | PLM-INT-TC | PLM-INT-TC-2CL |
| SAP_CA_BC_IC_LND_PLM_PLMSI_PC | PLM System Integration - Configuration | /PLMC/POL |  | /PLMC/VC_POL | Map DM POL to SAP Routing | 106538 | PLM-INT-TC | PLM-INT-TC-2CL |
| SAP_CA_BC_IC_LND_PLM_PLMSI_PC | PLM System Integration - Configuration | /PLMC/84000118 | PLMC_84000118_TRAN | /PLMC/VC_VD | Map DM Variant Definition to SAP Class | 106544 | PLM-INT-TC | PLM-INT-TC-2CL |
| SAP_CA_BC_IC_LND_PLM_PLMSI_PC | PLM System Integration - Configuration | /PLMC/COCR |  | /PLMC/VC_COCR | Map DM Change Object to SAP Change Record | 106548 | PLM-INT-TC | PLM-INT-TC-2CL |
| SAP_CA_BC_IC_LND_PLM_PLMSI_PC | PLM System Integration - Configuration | /PLMC/API_VRS |  | /PLMC/V_API_VRS | Define API Version | 106551 | PLM-INT-TC | PLM-INT-TC-2CL |
| SAP_CA_BC_IC_LND_PLM_PLMSI_PC | PLM System Integration - Configuration | /PLMC/84000105 | PLMC_84000105_TRAN | /PLMC/VC_FVM | Define Field and Value Mapping | 106525 | PLM-INT-TC | PLM-INT-TC-2CL |
| SAP_CA_BC_IC_LND_PLM_PLMSI_PC | PLM System Integration - Configuration | /PLMC/DV |  | /PLMC/VC_DV | Map DM Document Version to SAP Document Info Record | 106535 | PLM-INT-TC | PLM-INT-TC-2CL |
| SAP_CA_BC_IC_LND_PLM_PLMSI_PC | PLM System Integration - Configuration | /PLMC/CMP_VRS |  | /PLMC/V_CMP_VRS | Define Component Version | 106552 | PLM-INT-TC | PLM-INT-TC-2CL |
| SAP_CA_BC_IC_LND_PLM_PLMSI_PC | PLM System Integration - Configuration | /PLMC/84000113 | PLMC_84000113_TRAN | /PLMC/VC_IC | Map DM IC to SAP Master Inspection Characteristic | 106539 | PLM-INT-TC | PLM-INT-TC-2CL |
| SAP_CA_BC_IC_LND_PLM_PLMSI_PC | PLM System Integration - Configuration | /PLMC/84000107 | PLMC_84000107_TRAN | /PLMC/VC_COCR | Map DM Change Object to SAP Change Record | 106548 | PLM-INT-TC | PLM-INT-TC-2CL |
| SAP_CA_BC_IC_LND_PLM_PLMSI_PC | PLM System Integration - Configuration | /PLMC/IC |  | /PLMC/VC_IC | Map DM IC to SAP Master Inspection Characteristic | 106539 | PLM-INT-TC | PLM-INT-TC-2CL |
| SAP_CA_BC_IC_LND_PLM_PLMSI_PC | PLM System Integration - Configuration | /PLMC/84000137 | PLMC_84000137_TRAN | /PLMC/V_EXT_APP | Define External Application | 106553 | PLM-INT-TC | PLM-INT-TC-2CL |
| SAP_CA_BC_IC_LND_PLM_PLMSI_PC | PLM System Integration - Configuration | /PLMC/VO |  | /PLMC/VC_VO | Map DM Variant Option to SAP Characteristic | 106546 | PLM-INT-TC | PLM-INT-TC-2CL |
| SAP_CA_BC_IC_LND_PLM_PLMSI_PC | PLM System Integration - Configuration | /PLMC/84000119 | PLMC_84000119_TRAN | /PLMC/VDNR | Maintain Class ID Number Range | 106528 | PLM-INT-TC | PLM-INT-TC-2CL |
| SAP_CA_BC_IC_LND_PLM_PLMSI_PC | PLM System Integration - Configuration | /PLMC/LOG_INST |  | /PLMC/V_LOG_INST | Define Logical Instance | 106554 | PLM-INT-TC | PLM-INT-TC-2CL |
| SAP_CA_BC_IC_LND_PLM_PLMSI_PC | PLM System Integration - Configuration | /PLMC/84000140 | PLMC_84000140_TRAN | /PLMC/V_LOG_INST | Define Logical Instance | 106554 | PLM-INT-TC | PLM-INT-TC-2CL |
| SAP_CA_BC_IC_LND_PLM_PLMSI_PC | PLM System Integration - Configuration | /PLMC/84000139 | PLMC_84000139_TRAN | /PLMC/V_CMP_VRS | Define Component Version | 106552 | PLM-INT-TC | PLM-INT-TC-2CL |
| SAP_CA_BC_IC_LND_PLM_PLMSI_PC | PLM System Integration - Configuration | /PLMC/84000108 | PLMC_84000108_TRAN | /PLMC/VC_DV | Map DM Document Version to SAP Document Info Record | 106535 | PLM-INT-TC | PLM-INT-TC-2CL |
| SAP_CA_BC_IC_LND_PLM_PLMSI_PC | PLM System Integration - Configuration | /PLMF/VVNR |  | /PLMC/VVNR | Maintain Characteristic Value Number Range | 106527 | PLM-INT-TC | PLM-INT-TC-2CL |
| SAP_CA_BC_IC_LND_PLM_PLMSI_PC | PLM System Integration - Configuration | /PLMC/EXT_APP |  | /PLMC/V_EXT_APP | Define External Application | 106553 | PLM-INT-TC | PLM-INT-TC-2CL |
| SAP_CA_BC_IC_LND_PLM_PLMSI_PC | PLM System Integration - Configuration | /PLMC/84000138 | PLMC_84000138_TRAN | /PLMC/V_API_VRS | Define API Version | 106551 | PLM-INT-TC | PLM-INT-TC-2CL |
| SAP_CA_BC_IC_LND_PLM_PLMSI_PC | PLM System Integration - Configuration | /PLMC/84000127 | PLMC_84000127_TRAN | /PLMC/VVNR | Maintain Characteristic Value Number Range | 106527 | PLM-INT-TC | PLM-INT-TC-2CL |
| SAP_CA_BC_IC_LND_PLM_PLMSI_PC | PLM System Integration - Configuration | /PLMF/VDNR |  | /PLMC/VDNR | Maintain Class ID Number Range | 106528 | PLM-INT-TC | PLM-INT-TC-2CL |
| SAP_CA_BC_IC_LND_PLM_PLMSI_PC | PLM System Integration - Configuration | /PLMC/84000123 | PLMC_84000123_TRAN | /PLMC/VTNR | Maintain Variant Table ID Number Range | 106531 | PLM-INT-TC | PLM-INT-TC-2CL |
| SAP_CA_BC_IC_LND_PLM_PLMSI_PC | PLM System Integration - Configuration | /PLMC/84000126 | PLMC_84000126_TRAN | /PLMC/VONR | Maintain Characteristic ID Number Range | 106526 | PLM-INT-TC | PLM-INT-TC-2CL |
| SAP_CA_BC_IC_LND_PLM_PLMSI_PC | PLM System Integration - Configuration | /PLMC/FACTORY |  | /PLMC/VC_FACTORY | Map DM Factory Data to SAP Plant | 106932 | PLM-INT-TC | PLM-INT-TC-2CL |
| SAP_CA_BC_IC_LND_PLM_PLMSI_PC | PLM System Integration - Configuration | /PLMC/WAWC |  | /PLMC/VC_WAWC | Map DM Work Area to SAP Work Center | 106933 | PLM-INT-TC | PLM-INT-TC-2CL |
| SAP_CA_BC_IC_LND_PLM_PLMSI_PC | PLM System Integration - Configuration | /PLMF/VTNR |  | /PLMC/VTNR | Maintain Variant Table ID Number Range | 106531 | PLM-INT-TC | PLM-INT-TC-2CL |
| SAP_CA_BC_IC_LND_PLM_PLMSI_PC | PLM System Integration - Configuration | /PLMF/VONR |  | /PLMC/VONR | Maintain Characteristic ID Number Range | 106526 | PLM-INT-TC | PLM-INT-TC-2CL |
| SAP_CA_BC_IC_LND_PLM_PLMSI_PC | PLM System Integration - Configuration | /PLMC/70001157 | PLMC_70001157_TRAN | /PLMC/VC_FACTORY | Map DM Factory Data to SAP Plant | 106932 | PLM-INT-TC | PLM-INT-TC-2CL |
| SAP_CA_BC_IC_LND_PLM_PLMSI_PC | PLM System Integration - Configuration | /PLMC/70001158 | PLMC_70001158_TRAN | /PLMC/VC_WAWC | Map DM Work Area to SAP Work Center | 106933 | PLM-INT-TC | PLM-INT-TC-2CL |
| SAP_CA_BC_IC_LND_PLM_PLMSI_PC | PLM System Integration - Configuration | /PLMC/70001268 | PLMC_70001268_TRAN | /PLMC/V_RGRPDEF | Define Rule Group | 106949 | PLM-INT-TC | PLM-INT-TC-2CL |
| SAP_CA_BC_IC_LND_PLM_PLMSI_PC | PLM System Integration - Configuration | /PLMF/RULE_GRP_DEF |  | /PLMC/V_RGRPDEF | Define Rule Group | 106949 | PLM-INT-TC | PLM-INT-TC-2CL |
| SAP_CA_BC_IC_LND_FTG_PC | Feature Toggles - Configuration | FTG_EXTERNAL |  | FTG_EXTERNAL | Activate Features | 106573 | BC-DWB-TOO-SFW | BC-DWB-TOO-FTG |
| SAP_CA_BC_IC_LND_FTG_PC | Feature Toggles - Configuration | S_UIA_02000072 | S_UIA_02000072_TRAN | FTG_EXTERNAL | Activate Features | 106573 | BC-DWB-TOO-SFW | BC-DWB-TOO-FTG |
| SAP_CA_BC_IC_LND_SD1_PC | Sales - Cross-Client Configuration | S_ER9_52001534 | S_ER9_52001534_TRAN | V_03 | Create Condition Tables for Pricing in Sales | 103119 | SD-SLS | SD-MD-CM-2CL |
| SAP_CA_BC_IC_LND_SD1_PC | Sales - Cross-Client Configuration | V/03 |  | V_03 | Create Condition Tables for Pricing in Sales | 103119 | SD-SLS | SD-MD-CM-2CL |
| SAP_CA_BC_IC_LND_SD1_PC | Sales - Cross-Client Configuration | S_ER9_52001541 | S_ER9_52001541_TRAN | VVC_T682_VA | Set Access Sequences | 103121 | SD-SLS | SD-MD-CM-2CL |
| SAP_CA_BC_IC_LND_SD1_PC | Sales - Cross-Client Configuration | V/07 |  | VVC_T682_VA | Set Access Sequences | 103121 | SD-SLS | SD-MD-CM-2CL |
| SAP_CA_BC_IC_LND_SD1_PC | Sales - Cross-Client Configuration | V/05 |  | V_05 | Display Condition Tables for Pricing in Sales |  | SD-SLS | SD-MD-CM-2CL |
| SAP_CA_BC_IC_LND_SD1_PC | Sales - Cross-Client Configuration | S_ER9_52001540 | S_ER9_52001540_TRAN | V_05 | Display Condition Tables for Pricing in Sales |  | SD-SLS | SD-MD-CM-2CL |
| SAP_CA_BC_IC_LND_SD1_PC | Sales - Cross-Client Configuration | S_ER9_52001532 | S_ER9_52001532_TRAN | VV_T681F_VA | Change Field Catalog for Pricing in Sales | 103118 | SD-SLS | SD-MD-CM-2CL |
| SAP_CA_BC_IC_LND_SD1_PC | Sales - Cross-Client Configuration | OV24 |  | VV_T681F_VA | Change Field Catalog for Pricing in Sales | 103118 | SD-SLS | SD-MD-CM-2CL |
| SAP_CA_BC_IC_LND_SD1_PC | Sales - Cross-Client Configuration | V/04 |  | V_04 | Change Condition Tables for Pricing in Sales | 103120 | SD-SLS | SD-MD-CM-2CL |
| SAP_CA_BC_IC_LND_SD1_PC | Sales - Cross-Client Configuration | S_ER9_52001539 | S_ER9_52001539_TRAN | V_04 | Change Condition Tables for Pricing in Sales | 103120 | SD-SLS | SD-MD-CM-2CL |
| SAP_CA_BC_IC_LND_PLM_PLMSC_PC | PLM System Integration - Configuration | /PLMC/PV_L1CS |  | /PLMC/VC_PV_L1CS | Define Product Templates - DM PV to SAP Material Master | 106542 | PLM-INT-TC | PLM-INT-TC-2CL |
| SAP_CA_BC_IC_LND_PLM_PLMSC_PC | PLM System Integration - Configuration | /PLMC/PV_FC_TM |  | /PLMC/VC_PVFC_TM | Define Product Version Factory Template | 106541 | PLM-INT-TC | PLM-INT-TC-2CL |
| SAP_CA_BC_IC_LND_PLM_PLMSC_PC | PLM System Integration - Configuration | /PLMC/84000104 | PLMC_84000104_TRAN | /PLMC/V_RCVRDETN | Define External System | 106524 | PLM-INT-TC | PLM-INT-TC-2CL |
| SAP_CA_BC_IC_LND_PLM_PLMSC_PC | PLM System Integration - Configuration | /PLMC/84000115 | PLMC_84000115_TRAN | /PLMC/VC_PVFC_TM | Define Product Version Factory Template | 106541 | PLM-INT-TC | PLM-INT-TC-2CL |
| SAP_CA_BC_IC_LND_PLM_PLMSC_PC | PLM System Integration - Configuration | /PLMC/RCVRDETN |  | /PLMC/V_RCVRDETN | Define External System | 106524 | PLM-INT-TC | PLM-INT-TC-2CL |
| SAP_CA_BC_IC_LND_PLM_PLMSC_PC | PLM System Integration - Configuration | /PLMC/84000116 | PLMC_84000116_TRAN | /PLMC/VC_PV_L1CS | Define Product Templates - DM PV to SAP Material Master | 106542 | PLM-INT-TC | PLM-INT-TC-2CL |
| SAP_CA_BC_IC_LND_PLM_PLMSC_PC | PLM System Integration - Configuration | /PLMC/V_DVFILRDR |  | /PLMC/V_DVFILRDR | Define File Redirect Settings | 106824 | PLM-INT-TC | PLM-INT-TC-2CL |
| SAP_CA_BC_IC_LND_PLM_PLMSC_PC | PLM System Integration - Configuration | /PLMC/70001039 | PLMC_70001039_TRAN | /PLMC/V_DVFILRDR | Define File Redirect Settings | 106824 | PLM-INT-TC | PLM-INT-TC-2CL |
| SAP_CA_BC_IC_LND_PLM_PLMSC_PC | PLM System Integration - Configuration | /PLMC/84000141 | PLMC_84000141_TRAN | /PLMC/V_COCR_CS | Define Current Settings for DM CO to SAP CR | 107311 | PLM-INT-TC | PLM-INT-TC-2CL |
| SAP_CA_BC_IC_LND_PLM_PLMSC_PC | PLM System Integration - Configuration | /PLMC/COCR_CS |  | /PLMC/V_COCR_CS | Define Current Settings for DM CO to SAP CR | 107311 | PLM-INT-TC | PLM-INT-TC-2CL |
| SAP_FIN_BC_TRM_CMPLCONF_PC | TRM - Configuration for Planning Levels Substitution Rules | F7689 | F7689_TRAN |  |  |  | FIN-FSCM-TRM |  |
| SAP_CORE_BC_BCT_LOG_DIS_PC | Business Configuration - Change Logs Overview | F7033 | F7033_TRAN |  |  |  | BC-CUS-TOL-ALO |  |
| SAP_CA_BC_IC_LND_FIN_AF_IL_PC | Statutory Reporting Audit File for Israel - Configuration | /ATL/26000101 | ATL_26000101_TRAN | /ATL/SD_DOCUMENT | Define SD Document Classifications | 106294 | FI-LOC-FI-IL | FI-LOC-FI-IL |
| SAP_CA_BC_IC_LND_FIN_AF_IL_PC | Statutory Reporting Audit File for Israel - Configuration | /ATL/26000094 | ATL_26000094_TRAN | /ATL/MAT_MTYPE | Determine Official Document Types by Movement Types | 106292 | FI-LOC-FI-IL | FI-LOC-FI-IL |
| SAP_CA_BC_IC_LND_FIN_AF_IL_PC | Statutory Reporting Audit File for Israel - Configuration | /ATL/26000038 | ATL_26000038_TRAN | /ATL/ILS_LEDGER | Assign ILS Ledger by Company Code | 106291 | FI-LOC-FI-IL | FI-LOC-FI-IL |
| SAP_CA_BC_IC_LND_FIN_AF_IL_PC | Statutory Reporting Audit File for Israel - Configuration | /ATL/26000091 | ATL_26000091_TRAN | /ATL/GLSETCUST | Set Up G/L Sets | 106296 | FI-LOC-FI-IL | FI-LOC-FI-IL |
| SAP_CA_BC_IC_LND_FIN_AF_IL_PC | Statutory Reporting Audit File for Israel - Configuration | /ATL/26000039 | ATL_26000039_TRAN | /ATL/DOCTYPE | Determine Document Types for Tax Authority and Uniform Files | 106293 | FI-LOC-FI-IL | FI-LOC-FI-IL |
| SAP_CA_BC_IC_LND_FIN_AF_IL_PC | Statutory Reporting Audit File for Israel - Configuration | /ATL/26000040 | ATL_26000040_TRAN | /ATL/ACCOUNTTYPE | Assign G/L Accounts to Account Types | 106295 | FI-LOC-FI-IL | FI-LOC-FI-IL |
| SAP_CA_BC_IC_LND_FIN_AF_IL_PC | Statutory Reporting Audit File for Israel - Configuration | /ATL/11002676 | ATL_11002676_TRAN | /ATL/UNIF_IDNUM | Define Number Ranges for Uniform Files | 106333 | FI-LOC-FI-IL | FI-LOC-FI-IL |
| SAP_CA_BC_IC_LND_FIN_AF_IL_PC | Statutory Reporting Audit File for Israel - Configuration | /ATL/UNIF_IDNUM |  | /ATL/UNIF_IDNUM | Define Number Ranges for Uniform Files | 106333 | FI-LOC-FI-IL | FI-LOC-FI-IL |
| SAP_CA_BC_IC_LND_FIN_AF_IL_PC | Statutory Reporting Audit File for Israel - Configuration | /ATL/SD_DOCUMENT |  | /ATL/SD_DOCUMENT | Define SD Document Classifications | 106294 | FI-LOC-FI-IL | FI-LOC-FI-IL |
| SAP_CA_BC_IC_LND_FIN_AF_IL_PC | Statutory Reporting Audit File for Israel - Configuration | S_ER1_70001329 | S_ER1_70001329_TRAN | FKKID_IL_CIDOCTP | Define Invoicing Document Classifications in Convergent Invoicing | 106934 | FI-LOC-FI-IL | CA-GTF-CSC-DRC |
| SAP_CA_BC_IC_LND_FIN_AF_IL_PC | Statutory Reporting Audit File for Israel - Configuration | S_ER1_70001337 | S_ER1_70001337_TRAN | V_FKKID_IL_CADOC | Define Document Classifications in Contract Accounting | 106947 | FI-LOC-FI-IL | CA-GTF-CSC-EDO-IL |
| SAP_CA_BC_IC_LND_BPM_WFL_PC | Business Process Management - Workflow Configuration | S_YI3_39000695 | S_YI3_39000695_TRAN | SWFC_LANGUAGES | Language Vector for Buffering Work Item Texts | 106368 | BC-BMT-WFM-DEF | BC-BMT-WFM |
| SAP_CA_BC_IC_LND_BPM_WFL_PC | Business Process Management - Workflow Configuration | SWFC_LANGUAGES |  | SWFC_LANGUAGES | Language Vector for Buffering Work Item Texts | 106368 | BC-BMT-WFM-DEF | BC-BMT-WFM |
| SAP_CA_BC_IC_LND_BPM_WFL_PC | Business Process Management - Workflow Configuration | S_YI3_39000770 | S_YI3_39000770_TRAN | SWF_USER_ATTR_CDS | Maintain CDS Based Custom Attributes | 106664 | BC-BMT-WFM-DEF | BC-BMT-WFM |
| SAP_CA_BC_IC_LND_BPM_WFL_PC | Business Process Management - Workflow Configuration | SWF_USER_ATTR_CDS |  | SWF_USER_ATTR_CDS | Maintain CDS Based Custom Attributes | 106664 | BC-BMT-WFM-DEF | BC-BMT-WFM |
| SAP_CA_BC_IC_LND_GLO_ODN_PC | Official Document Numbering - Configuration | ODNNR_YRIND | ODNNR_YRIND_TRAN | ODNNR_YRIND | Maintain Number Range for Year Independent ODN Types | 106199 | FI-LOC-LO | FI-LOC-ODN |
| SAP_CA_BC_IC_LND_GLO_ODN_PC | Official Document Numbering - Configuration | ODNTYPC | ODNTYPC_TRAN | ODNTYPC | Configure Official Document Number Type Characteristics | 106198 | FI-LOC-LO | FI-LOC-ODN |
| SAP_CA_BC_IC_LND_GLO_ODN_PC | Official Document Numbering - Configuration | ODNNR_YR | ODNNR_YR_TRAN | ODNNR_YR | Maintain Number Range for Year Dependent ODN Types | 106200 | FI-LOC-LO | FI-LOC-ODN |
| SAP_CA_BC_IC_LND_GLO_ODN_PC | Official Document Numbering - Configuration | ODNTYP | ODNTYP_TRAN | ODNTYP | Maintain Official Document Number Types | 106197 | FI-LOC-LO | FI-LOC-ODN |
| SAP_CA_BC_IC_LND_GLO_ODN_PC | Official Document Numbering - Configuration | S_ER9_52004021 | S_ER9_52004021_TRAN | ODNNR_YRIND | Maintain Number Range for Year Independent ODN Types | 106199 | FI-LOC-LO | FI-LOC-ODN |
| SAP_CA_BC_IC_LND_GLO_ODN_PC | Official Document Numbering - Configuration | S_ER9_52004020 | S_ER9_52004020_TRAN | ODNNR_YR | Maintain Number Range for Year Dependent ODN Types | 106200 | FI-LOC-LO | FI-LOC-ODN |
| SAP_CA_BC_IC_LND_GLO_ODN_PC | Official Document Numbering - Configuration | S_ER9_52004019 | S_ER9_52004019_TRAN | ODNTYPC | Configure Official Document Number Type Characteristics | 106198 | FI-LOC-LO | FI-LOC-ODN |
| SAP_CA_BC_IC_LND_GLO_ODN_PC | Official Document Numbering - Configuration | S_ER9_52004018 | S_ER9_52004018_TRAN | ODNTYP | Maintain Official Document Number Types | 106197 | FI-LOC-LO | FI-LOC-ODN |
| SAP_CA_BC_IC_LND_GLO_ODN_PC | Official Document Numbering - Configuration | ODNINTTYP | ODNINTTYP_TRAN | ODN_C_INTMAPV | Map Official Document Number Type to Internal Type | 106519 | FI-LOC-LO | FI-LOC-ODN |
| SAP_CA_BC_IC_LND_GLO_ODN_PC | Official Document Numbering - Configuration | S_ER9_52004345 | S_ER9_52004345_TRAN | ODN_C_INTMAPV | Map Official Document Number Type to Internal Type | 106519 | FI-LOC-LO | FI-LOC-ODN |
| SAP_CA_BC_IC_LND_GLO_ODN_PC | Official Document Numbering - Configuration | ODN_NR_SO_YRIND |  | ODN_NR_SO_YRIND | Define Number Range Intervals for Year Independent Overlapping Number Range | 106919 | FI-LOC-LO | FI-LOC-ODN |
| SAP_CA_BC_IC_LND_GLO_ODN_PC | Official Document Numbering - Configuration | S_ER1_70000713 | S_ER1_70000713_TRAN | ODN_NR_SO_YR | Define Number Range Intervals for Year Dependent Overlapping Number Ranges | 106918 | FI-LOC-LO | FI-LOC-ODN |
| SAP_CA_BC_IC_LND_GLO_ODN_PC | Official Document Numbering - Configuration | ODN_NR_SO_YR |  | ODN_NR_SO_YR | Define Number Range Intervals for Year Dependent Overlapping Number Ranges | 106918 | FI-LOC-LO | FI-LOC-ODN |
| SAP_CA_BC_IC_LND_GLO_ODN_PC | Official Document Numbering - Configuration | S_ER1_70000714 | S_ER1_70000714_TRAN | ODN_NR_SO_YRIND | Define Number Range Intervals for Year Independent Overlapping Number Range | 106919 | FI-LOC-LO | FI-LOC-ODN |
| SAP_CA_BC_IC_LND_GLO_ODN_PC | Official Document Numbering - Configuration | ODNSO |  | ODNSO | Define Number Range Subobject for Overlapping Number Ranges | 106917 | FI-LOC-LO | FI-LOC-ODN |
| SAP_CA_BC_IC_LND_GLO_ODN_PC | Official Document Numbering - Configuration | S_ER1_70000711 | S_ER1_70000711_TRAN | ODNSO | Define Number Range Subobject for Overlapping Number Ranges | 106917 | FI-LOC-LO | FI-LOC-ODN |
| SAP_CA_BC_IC_LND_FIN_FS_IL_PC | Statutory Reporting Financial Statements for Israel - Configuration | /ATL/26000160 | ATL_26000160_TRAN | /ATL/6111_CONV | Convert Fin. Key and Func. Area to Form 6111 Code | 106287 | FI-LOC-FI-IL | FI-LOC-FI-IL |
| SAP_CA_BC_IC_LND_FIN_FS_IL_PC | Statutory Reporting Financial Statements for Israel - Configuration | /ATL/26000099 | ATL_26000099_TRAN | /ATL/6111_HEADER | Determine Fields for Form 6111 Header | 106288 | FI-LOC-FI-IL | FI-LOC-FI-IL |
| SAP_CA_BC_IC_LND_FIN_FS_IL_PC | Statutory Reporting Financial Statements for Israel - Configuration | /ATL/26000098 | ATL_26000098_TRAN | /ATL/V_6111_CODE | Define Field Codes | 106290 | FI-LOC-FI-IL | FI-LOC-FI-IL |
| SAP_CA_BC_IC_LND_WFA_PC | Workforce Availabilty - Configuration | S_ER9_52003845 | S_ER9_52003845_TRAN | WFD_D_JOBCDFAM | Define Job Code Family | 106358 | CA-WFD-AVL | CA-WFD-AVL |
| SAP_CA_BC_IC_LND_WFA_PC | Workforce Availabilty - Configuration | S_ER9_52003846 | S_ER9_52003846_TRAN | WFD_D_JOBCDMAP | Define Mapping of Job Code Family to Job Code | 106357 | CA-WFD-AVL | CA-WFD-AVL |
| SAP_CA_BC_AA_MDAT_CONFIG_PC | Asset Accounting - Configuration for Master Data | F4886 | F4886_TRAN |  |  |  | FI-AA |  |
| SAP_CA_BC_AA_MDAT_CONFIG_PC | Asset Accounting - Configuration for Master Data | F4945 | F4945_TRAN |  |  |  | FI-AA |  |
| SAP_CA_BC_AA_MDAT_CONFIG_PC | Asset Accounting - Configuration for Master Data | F6968 | F6968_TRAN |  |  |  | FI-AA |  |
| SAP_CA_BC_IC_LND_FIN_BK_IL_PC | Bank Accounting for Israel - Configuration | /ATL/26000083 | ATL_26000083_TRAN | /ATL/LCHK_BNKAP | Specify Relevancy of Account Number Length | 106289 | FI-LOC-FI-IL | FI-LOC-FI-IL |
| SAP_CA_BC_IC_LND_FIN_AA_IL_PC | Asset Accounting for Israel - Configuration | /ATL/26000056 | ATL_26000056_TRAN | /ATL/GV_GL1V | Maintain Index Values | 106399 | FI-LOC-FI-IL | FI-LOC-FI-IL |
| SAP_CA_BC_IC_LND_FIN_AA_IL_PC | Asset Accounting for Israel - Configuration | /ATL/26000055 | ATL_26000055_TRAN | /ATL/GV_GL1 | Maintain Inflation Indexes | 106398 | FI-LOC-FI-IL | FI-LOC-FI-IL |
| SAP_CA_BC_IC_LND_FIN_AA_IL_PC | Asset Accounting for Israel - Configuration | /ATL/GLV |  | /ATL/GV_GL1V | Maintain Index Values | 106399 | FI-LOC-FI-IL | FI-LOC-FI-IL |
| SAP_CA_BC_IC_LND_SCM_ATP6_PC | ATP Availability Change Log - Configuration | S_ER9_52004229 | S_ER9_52004229_TRAN | ATP_CHANGE_LOG_ACTVT | Activate Availability Change Log | 106365 | CA-ATP | CA-ATP-ACL-2CL |
| SAP_CA_BC_IC_LND_SCM_ATP6_PC | ATP Availability Change Log - Configuration | S_ER9_52004230 | S_ER9_52004230_TRAN | ATP_CHANGE_LOG_SCOPE | Configure Availability Change Log for Availability Checking Group | 106364 | CA-ATP | CA-ATP-ACL-2CL |
| SAP_CRM_BC_SERV_WRKFLW_PC | Service - Service Workflow Configuration | F7072 | F7072_TRAN |  |  |  | CRM-S4-SRV-SVO |  |
| SAP_MM_BC_BUYING_CONFIG_PC | Materials Management - Configuration - Buying | U0100 | U0100_TRAN |  |  |  | MM-PUR-GF |  |
| SAP_PSM_BC_BDGT_WRKFLW_PC | Budget Management PSM - Workflow Configuration | F7308 | F7308_TRAN |  |  |  | PSM |  |
| SAP_MM_BC_BUYING_PRSDATA_PC | Materials Management - Personal Data - Buying | F3287 | F3287_TRAN |  |  |  | MM-PUR-GF |  |
| SAP_CA_BC_IC_LND_LOG_IN_UA_PC | Inventory for Ukraine - Configuration | S_EBJ_98000546 | S_EBJ_98000546_TRAN | V_J_3RM_TURNTYP | Define Turnover Types | 104250 | FI-LOC-FI-UA | FI-LOC-LO-RU |
| SAP_CA_BC_IC_LND_LOG_IN_UA_PC | Inventory for Ukraine - Configuration | S_EBS_44000003 | S_EBS_44000003_TRAN | J_3R_INVDIFFMATV | Assign Material Groups to Groups for Offsetting Inventory Differences | 104252 | FI-LOC-FI-UA | FI-LOC-FI-RU |
| SAP_CA_BC_IC_LND_LOG_IN_UA_PC | Inventory for Ukraine - Configuration | S_EBS_44000002 | S_EBS_44000002_TRAN | J_3R_INVDIFFGRV | Define Groups for Offsetting Inventory Differences | 104251 | FI-LOC-FI-UA | FI-LOC-FI-RU |
| SAP_FIN_BC_GL_VAL_CONF_PC | General Ledger - Validation Configuration | F5003 | F5003_GLAUDIT_TRAN |  |  |  | FI-GL |  |
| SAP_FIN_BC_GL_VAL_CONF_PC | General Ledger - Validation Configuration | F5097 | F5097_TRAN |  |  |  | FI-GL |  |
| SAP_FIN_BC_GL_VAL_CONF_PC | General Ledger - Validation Configuration | F6386 | F6386_03_TRAN |  |  |  | FI-GL |  |
| SAP_FIN_BC_GL_VAL_CONF_PC | General Ledger - Validation Configuration | F7019 | F7019_TRAN |  |  |  | FI-GL |  |
| SAP_FIN_BC_GL_VAL_CONF_PC | General Ledger - Validation Configuration | F8362 | F8362_03_TRAN |  |  |  | FI-GL |  |
| SAP_FIN_BC_GL_VAL_CONF_PC | General Ledger - Validation Configuration | F8363 | F8363_TRAN |  |  |  | FI-GL |  |
| SAP_FIN_BC_GL_VAL_CONF_PC | General Ledger - Validation Configuration | F9259 | F9259_TRAN |  |  |  | FI-GL |  |
| SAP_CA_BC_IC_LND_RFM_BF1_PC | Fashion Retail Base Scope Business Function - Configuration | FSH_RTL_BASIC_ACTVT |  | FSH_RTL_BASIC_ACTVT | Activate Business Function 'Retail Season' | 106404 | LO-RFM | LO-RFM-CA-SE-2CL |
| SAP_CA_BC_IC_LND_RFM_BF1_PC | Fashion Retail Base Scope Business Function - Configuration | S_ER9_52004258 | S_ER9_52004258_TRAN | FSH_RTL_BASIC_ACTVT | Activate Business Function 'Retail Season' | 106404 | LO-RFM | LO-RFM-CA-SE-2CL |
| SAP_FIN_BC_TAX_MIGRTN_PC | Tax Management - Migrate Tax Item | F7471 | F7471_TRAN |  |  |  | FI-TXL-OPS |  |
| SAP_FIN_BC_TAX_MIGRTN_PC | Tax Management - Migrate Tax Item | F6715 | F6715_TRAN |  |  |  | FI-TXL-OPS |  |
| SAP_CA_BC_IC_LND_CDB_PC | Customer Data Browser - Configuration | SCDB_VC_OBJ_GRP |  | SCDB_VC_OBJ_GRP | Maintain Object Groups | 106306 | BC-SRV-APS-CDB | BC-SRV-APS-CDB |
| SAP_CA_BC_IC_LND_CDB_PC | Customer Data Browser - Configuration | S_YI3_39000590 | S_YI3_39000590_TRAN | SCDB_VC_OBJ_GRP | Maintain Object Groups | 106306 | BC-SRV-APS-CDB | BC-SRV-APS-CDB |
| SAP_FIN_BC_SETTINGS_UA_PC | Globalization Finance - System Specific Configuration for Ukraine | J1UDIUSERS | J1UDIUSERS_TRAN |  |  |  | FI-LOC-FI-UA |  |
| SAP_FIN_BC_SETTINGS_UA_PC | Globalization Finance - System Specific Configuration for Ukraine | J1UFRGOUT | J1UFRGOUT_TRAN |  |  |  | FI-LOC-FI-UA |  |
| SAP_FIN_BC_SETTINGS_UA_PC | Globalization Finance - System Specific Configuration for Ukraine | J_3RCNT | J_3RCNT_TRAN |  |  |  | FI-LOC-FI-UA |  |
| SAP_FIN_BC_SETTINGS_UA_PC | Globalization Finance - System Specific Configuration for Ukraine | J1UFSUMREL | J1UFSUMREL_TRAN |  |  |  | FI-LOC-FI-UA |  |
| SAP_CA_BC_IC_LND_AR1_PC | Ariba Network Integration Credentials - Configuration | S_NWC_69000001 | S_NWC_69000001_TRAN | ARBFND1_CRED_ANID | Define Credentials and End Points for SAP Business Network | 102036 | BNS-INT-FND | BNS-INT-FND |
| SAP_CA_BC_IC_LND_AR1_PC | Ariba Network Integration Credentials - Configuration | ARBFND_C_ANCRED |  | ARBFND1_CRED_ANID | Define Credentials and End Points for SAP Business Network | 102036 | BNS-INT-FND | BNS-INT-FND |
| SAP_CA_BC_IC_LND_AR1_PC | Ariba Network Integration Credentials - Configuration | S_ER9_52000334 | S_ER9_52000334_TRAN | ARBFND1_CRED_FG | Define Credentials for SAP Fieldglass | 102037 | BNS-INT-FND | BNS-INT-FND |
| SAP_CA_BC_IC_LND_AR1_PC | Ariba Network Integration Credentials - Configuration | ARBFND_V_FGCRED |  | ARBFND1_CRED_FG | Define Credentials for SAP Fieldglass | 102037 | BNS-INT-FND | BNS-INT-FND |
| SAP_CA_BC_IC_LND_SC1_PC | Central Business Configuration - Scoping Display - Configuration | /CFG/CONT_VERS |  | /CFG/CONT_VERS | Maintain Active Content Version |  | SV-CLD-FRM-APP | SV-BC-ACT |
| SAP_CA_BC_IC_LND_SC1_PC | Central Business Configuration - Scoping Display - Configuration | START_A_PR_ACTIV |  | START_A_PR_ACTIV | Maintain Active Scope Items |  | SV-CLD-FRM-APP | CA-CTT-S4C |
| SAP_CA_BC_IC_LND_SC1_PC | Central Business Configuration - Scoping Display - Configuration | /CFG/75000004 | CFG_75000004_03_TRAN | /CFG/CONT_VERS | Maintain Active Content Version |  | SV-CLD-FRM-APP | SV-BC-ACT |
| SAP_CA_BC_IC_LND_SC1_PC | Central Business Configuration - Scoping Display - Configuration | S_ER9_52003775 | S_ER9_52003775_03_TRAN | START_A_PR_ACTIV | Maintain Active Scope Items |  | SV-CLD-FRM-APP | CA-CTT-S4C |
| SAP_CA_BC_IC_LND_BCL_TST_PC | Semantic Business Configuration Locks Test - Configuration | BCL_V_TEST |  | BCL_V_TEST | SBCL Test |  | BC-CTS-BCL | BC-CTS-BCL |
| SAP_CA_BC_IC_LND_BCL_TST_PC | Semantic Business Configuration Locks Test - Configuration | S_YI3_39000587 | S_YI3_39000587_TRAN | BCL_V_TEST | SBCL Test |  | BC-CTS-BCL | BC-CTS-BCL |
| SAP_CA_BC_IC_LND_FIN_SR_IL_PC | Statutory Reporting VAT for Israel - Configuration | /ATL/VATRECT3 | ATL_VATRECT3_TRAN | /ATL/VATRECT3 | Assign Record Types for Reconciliation Accounts and Document Types | 106298 | FI-LOC-FI-IL | FI-LOC-FI-IL |
| SAP_CA_BC_IC_LND_FIN_SR_IL_PC | Statutory Reporting VAT for Israel - Configuration | /ATL/26000092 | ATL_26000092_TRAN | /ATL/VATRECT3 | Assign Record Types for Reconciliation Accounts and Document Types | 106298 | FI-LOC-FI-IL | FI-LOC-FI-IL |
| SAP_CA_BC_IC_LND_FIN_SR_IL_PC | Statutory Reporting VAT for Israel - Configuration | /ATL/26000090 | ATL_26000090_TRAN | /ATL/RECTYPE2 | Assign Record Types for Account Groups | 106299 | FI-LOC-FI-IL | FI-LOC-FI-IL |
| SAP_CA_BC_IC_LND_FIN_SR_IL_PC | Statutory Reporting VAT for Israel - Configuration | FKKID_VAT_IL | FKKID_VAT_IL_TRAN | FKKID_IL_VAT_V | Assign Record Types for Contract Accounting | 107066 | FI-LOC-FI-IL | CA-GTF-CSC-DRC |
| SAP_CA_BC_IC_LND_FIN_SR_IL_PC | Statutory Reporting VAT for Israel - Configuration | /ATL/26000089 | ATL_26000089_TRAN | /ATL/RECTYPE1 | Assign Record Types for Customers and Vendors | 106300 | FI-LOC-FI-IL | FI-LOC-FI-IL |
| SAP_CA_BC_IC_LND_FIN_SR_IL_PC | Statutory Reporting VAT for Israel - Configuration | /ATL/11001253 | ATL_11001253_TRAN | /ATL/PCN874_ACR | Define Settings for PCN874 on Statutory Reporting | 106303 | FI-LOC-FI-IL | FI-LOC-FI-IL |
| SAP_CA_BC_IC_LND_FIN_SR_IL_PC | Statutory Reporting VAT for Israel - Configuration | /ATL/26000046 | ATL_26000046_TRAN | /ATL/VAT_TRANKEY | Determine Transaction Keys | 106297 | FI-LOC-FI-IL | FI-LOC-FI-IL |
| SAP_CA_BC_IC_LND_FIN_SR_IL_PC | Statutory Reporting VAT for Israel - Configuration | S_ER1_70001552 | S_ER1_70001552_TRAN | FKKID_IL_VAT_V | Assign Record Types for Contract Accounting | 107066 | FI-LOC-FI-IL | CA-GTF-CSC-DRC |
| SAP_CA_BC_IC_LND_FIN_WT_AR_PC | Statutory Reporting WT for Argentina - Configuration | S_P7D_67000454 | S_P7D_67000454_TRAN | FIWTARV_FORMCOD | Assign Form Code to Official Withholding Tax Key | 106133 | FI-LOC-FI-AR | FI-LOC-FI-AR-WHT |
| SAP_CA_BC_IC_LND_FIN_WT_AR_PC | Statutory Reporting WT for Argentina - Configuration | S_EB5_05000349 | S_EB5_05000349_TRAN | V_WTAX_KEY_AR | Define Withholding Tax Keys | 106167 | FI-LOC-FI-AR | FI-LOC-FI-AR-WHT |
| SAP_CA_BC_IC_LND_FIN_WT_AR_PC | Statutory Reporting WT for Argentina - Configuration | S_EB5_05000350 | S_EB5_05000350_TRAN | V_T059Z_AR | Assign Withholding Tax Keys | 106166 | FI-LOC-FI-AR | FI-LOC-FI-AR-WHT |
| SAP_CA_BC_IC_LND_FIN_WT_AR_PC | Statutory Reporting WT for Argentina - Configuration | S_ALR_87004775 | S_ALR_87004775_TRAN | J_1AASSIGN_CODES4 | Assign Official Tax Code to Processing Keys | 106222 | FI-LOC-FI-AR | FI-AR-AR-2CL |
| SAP_CA_BC_IC_LND_FIN_WT_AR_PC | Statutory Reporting WT for Argentina - Configuration | S_ALR_87004713 | S_ALR_87004713_TRAN | J_1ATAX_ID4 | Maintain Tax Classes | 106223 | FI-LOC-FI-AR | FI-AR-AR-2CL |
| SAP_CA_BC_IC_LND_FIN_WT_AR_PC | Statutory Reporting WT for Argentina - Configuration | S_ALR_87003096 | S_ALR_87003096_TRAN | J_1AFISCAL_TYPE1 | Define Fiscal Type | 106236 | FI-LOC-FI-AR | FI-AR-AR-2CL |
| SAP_CA_BC_IC_LND_FIN_WT_AR_PC | Statutory Reporting WT for Argentina - Configuration | S_ALR_87003093 | S_ALR_87003093_TRAN | J_1AASSIGN_FISC_TYP2 | Assign Fiscal Type | 106237 | FI-LOC-FI-AR | FI-AR-AR-2CL |
| SAP_CA_BC_IC_LND_FIN_WT_AR_PC | Statutory Reporting WT for Argentina - Configuration | S_EBJ_98000112 | S_EBJ_98000112_TRAN | J_1AWTH_VTAX | Maintain Conditions for Applying Withholding Tax Code | 106238 | FI-LOC-FI-AR | FI-LOC-FI-AR-WHT |
| SAP_CA_BC_IC_LND_FIN_WT_AR_PC | Statutory Reporting WT for Argentina - Configuration | S_EBJ_98000109 | S_EBJ_98000109_TRAN | V_J_1ATAXP_TT | Maintain Tax Type Key | 106360 | FI-LOC-FI-AR | FI-LOC-FI-AR-WHT |
| SAP_CA_BC_IC_LND_FIN_WT_AR_PC | Statutory Reporting WT for Argentina - Configuration | S_EBJ_98000108 | S_EBJ_98000108_TRAN | V_J_1ATAXP_ES | Maintain Earning Status | 106359 | FI-LOC-FI-AR | FI-LOC-FI-AR-WHT |
| SAP_CA_BC_IC_LND_FIN_WT_AR_PC | Statutory Reporting WT for Argentina - Configuration | S_ALR_87004797 | S_ALR_87004797_TRAN | J_1ADEF_OFF_TAX_COD4 | Maintain Official Tax Codes | 106134 | FI-LOC-FI-AR | FI-AR-AR-2CL |
| SAP_CA_BC_IC_LND_FIN_WT_AR_PC | Statutory Reporting WT for Argentina - Configuration | S_ALR_87003115 | S_ALR_87003115_TRAN | J_1AACTIVITY_SSWT4 | Define Activity Codes for Social Security Insurance | 106417 | FI-LOC-FI-AR | FI-AR-AR-2CL |
| SAP_CA_BC_IC_LND_FIN_WT_AR_PC | Statutory Reporting WT for Argentina - Configuration | S_KK4_74002717 | S_KK4_74002717_TRAN | FICA_AR_RTAX_GI_RATE | Maintain Gross Income Tax Rates | 106816 | FI-LOC-FI-AR | FI-LOC-FI-AR-WHT |
| SAP_CA_BC_IC_LND_FIN_WT_AR_PC | Statutory Reporting WT for Argentina - Configuration | S_KK4_74002710 | S_KK4_74002710_TRAN | FICA_AR_REVTAX_MAC | Maintain Multilateral Agreement Coefficients | 106815 | FI-LOC-FI-AR | FI-LOC-FI-AR-WHT |
| SAP_CA_BC_IC_LND_FIN_SR_BG_PC | Statutory Reporting for Bulgaria - Configuration | S_ER9_11002079 | S_ER9_11002079_TRAN | FIVC_OFFS_VERS_A_CE | Define Offsetting Account Determination Versions for Several Countries/Rgns | 105370 | FI-LOC-FI-BG | FI-LOC-CF |
| SAP_CA_BC_IC_LND_FIN_SR_BG_PC | Statutory Reporting for Bulgaria - Configuration | S_ER9_11002015 | S_ER9_11002015_TRAN | FIVC_CF_VERSION_ACR | Define Cash Flow Statement Versions for Several Countries/Regions | 105331 | FI-LOC-FI-BG | FI-LOC-CF |
| SAP_CA_BC_IC_LND_FIN_SR_BG_PC | Statutory Reporting for Bulgaria - Configuration | S_ALR_87003246 | S_ALR_87003246_TRAN | J_1AREASON_PER_TAXC4 | Assign Reasons to Tax Codes | 106144 | FI-LOC-FI-BG | FI-AR-AR-2CL |
| SAP_CA_BC_IC_LND_FIN_SR_BG_PC | Statutory Reporting for Bulgaria - Configuration | S_ALR_87003243 | S_ALR_87003243_TRAN | J_1AREASON_DEF4 | Define Reasons | 102858 | FI-LOC-FI-BG | FI-AR-AR-2CL |
| SAP_CA_BC_IC_LND_FIN_SR_BG_PC | Statutory Reporting for Bulgaria - Configuration | FIBGVAT_SDDTYP | FIBGVAT_SDDTYP_TRAN | V_FIBGVAT_SDDTYP | Define Attributes for SD Documents | 106415 | FI-LOC-FI-BG | FI-LOC-FI-BG |
| SAP_CA_BC_IC_LND_FIN_SR_BG_PC | Statutory Reporting for Bulgaria - Configuration | FIBGVAT_RVCHRG | FIBGVAT_RVCHRG_TRAN | V_FIBGVAT_RVCHR | Define Tax Codes for Reverse-Charge VAT | 106412 | FI-LOC-FI-BG | FI-LOC-FI-BG |
| SAP_CA_BC_IC_LND_FIN_SR_BG_PC | Statutory Reporting for Bulgaria - Configuration | S_ER9_11002398 | S_ER9_11002398_TRAN | V_FIBGVAT_RVCHR | Define Tax Codes for Reverse-Charge VAT | 106412 | FI-LOC-FI-BG | FI-LOC-FI-BG |
| SAP_CA_BC_IC_LND_FIN_SR_BG_PC | Statutory Reporting for Bulgaria - Configuration | FIBGVAT_FIDTYP | FIBGVAT_FIDTYP_TRAN | V_FIBGVAT_FIDTYP | Define Attributes for FI Documents | 106413 | FI-LOC-FI-BG | FI-LOC-FI-BG |
| SAP_CA_BC_IC_LND_FIN_SR_BG_PC | Statutory Reporting for Bulgaria - Configuration | FIBGVAT_MMDTYP | FIBGVAT_MMDTYP_TRAN | V_FIBGVAT_MMDTYP | Define Attributes for MM Documents | 106414 | FI-LOC-FI-BG | FI-LOC-FI-BG |
| SAP_CA_BC_IC_LND_FIN_SR_BG_PC | Statutory Reporting for Bulgaria - Configuration | S_ER9_11002392 | S_ER9_11002392_TRAN | V_FIBGVAT_SDDTYP | Define Attributes for SD Documents | 106415 | FI-LOC-FI-BG | FI-LOC-FI-BG |
| SAP_CA_BC_IC_LND_FIN_SR_BG_PC | Statutory Reporting for Bulgaria - Configuration | S_ER9_11002391 | S_ER9_11002391_TRAN | V_FIBGVAT_MMDTYP | Define Attributes for MM Documents | 106414 | FI-LOC-FI-BG | FI-LOC-FI-BG |
| SAP_CA_BC_IC_LND_FIN_SR_BG_PC | Statutory Reporting for Bulgaria - Configuration | S_ER9_11002390 | S_ER9_11002390_TRAN | V_FIBGVAT_FIDTYP | Define Attributes for FI Documents | 106413 | FI-LOC-FI-BG | FI-LOC-FI-BG |
| SAP_CA_BC_IC_LND_FIN_SR_BG_PC | Statutory Reporting for Bulgaria - Configuration | S_ER9_11002335 | S_ER9_11002335_TRAN | FIVC_OFFS_GROUP_DRC | Define Field Sets for Grouping for Several Countries/Regions | 105762 | FI-LOC-FI-BG | FI-LOC-CF |
| SAP_CA_BC_IC_LND_FIN_SR_BG_PC | Statutory Reporting for Bulgaria - Configuration | S_ER9_11002017 | S_ER9_11002017_TRAN | FIVC_OFFS_DET_ACR | Activate Online Offsetting Account Determination for Several Countries/Rgns | 105333 | FI-LOC-FI-BG | FI-LOC-CF |
| SAP_CA_BC_IC_LND_FIN_WT_IL_PC | Statutory Reporting WT for Israel - Configuration | /ATL/26000044 | ATL_26000044_TRAN | /ATL/VFI00004 | Determine Shaam Rate Groups (Extended) | 106302 | FI-LOC-FI-IL | FI-LOC-FI-IL |
| SAP_CA_BC_IC_LND_FIN_WT_IL_PC | Statutory Reporting WT for Israel - Configuration | /ATL/26000043 | ATL_26000043_TRAN | /ATL/VFI00003 | Assign Posting Keys for Withholding Tax Returns | 106301 | FI-LOC-FI-IL | FI-LOC-FI-IL |
| SAP_CORE_BC_BCT_TRA_PC | Translation - Customizing | F6962 | F6962_TRAN |  |  |  | BC-DOC-TTL-MTR |  |
| SAP_CA_BC_IC_LND_FIN_SR_PE_PC | Statutory Reporting for Peru - Configuration | S_ER9_11002661 | S_ER9_11002661_TRAN | FIPEV_DBLTAXCNVN | Define Convention Code | 106371 | FI-LOC-FI-PE | FI-LOC-FI-PE |
| SAP_CA_BC_IC_LND_FIN_SR_PE_PC | Statutory Reporting for Peru - Configuration | S_ER9_11002504 | S_ER9_11002504_TRAN | V_T003_B_I_PE | Assign Document Classes to Document Types | 106374 | FI-LOC-FI-PE | FI-LOC-FI-PE |
| SAP_CA_BC_IC_LND_FIN_SR_PE_PC | Statutory Reporting for Peru - Configuration | S_ER9_11001184 | S_ER9_11001184_TRAN | V_FOT_TBS2 | Define Enhanced Tax Box Structure | 103011 | FI-LOC-FI-PE | FI-LOC-FI |
| SAP_CA_BC_IC_LND_FIN_SR_PE_PC | Statutory Reporting for Peru - Configuration | S_ER9_11002503 | S_ER9_11002503_TRAN | V_DOCCLS_PE | Maintain Document Classes | 106373 | FI-LOC-FI-PE | FI-LOC-FI-PE |
| SAP_CA_BC_IC_LND_FIN_SR_PE_PC | Statutory Reporting for Peru - Configuration | S_ER9_11002662 | S_ER9_11002662_TRAN | FIPEV_DTXCNVVSCT | Assign Country/Region to Convention Code | 106372 | FI-LOC-FI-PE | FI-LOC-FI-PE |
| SAP_CA_BC_IC_LND_FIN_SR_UA_PC | Statutory Reporting for Ukraine - Configuration | S_ER9_11002891 | S_ER9_11002891_TRAN | J_1UJ_UOMV | Assign Units of Measurement to KSPOVO Keys | 106561 | FI-LOC-FI-UA | FI-LOC-FI-UA |
| SAP_CA_BC_IC_LND_FIN_SR_UA_PC | Statutory Reporting for Ukraine - Configuration | S_ER9_11002866 | S_ER9_11002866_TRAN | J_1UFV_VAT_OPTCE | Assign Tax Exemption Codes to VAT Codes | 106558 | FI-LOC-FI-UA | FI-LOC-FI-UA |
| SAP_CA_BC_IC_LND_FIN_SR_UA_PC | Statutory Reporting for Ukraine - Configuration | S_ER9_11002886 | S_ER9_11002886_TRAN | J_1UFDI_SPTXCODV | Maintain Reasons for Special Tax Codes | 106560 | FI-LOC-FI-UA | FI-LOC-FI-UA |
| SAP_CA_BC_IC_LND_FIN_SR_UA_PC | Statutory Reporting for Ukraine - Configuration | S_ER9_11002885 | S_ER9_11002885_TRAN | J_1UFV_VAT_EXEMP | Define Tax Exemptions for VAT Accounting | 106559 | FI-LOC-FI-UA | FI-LOC-FI-UA |
| SAP_CA_BC_IC_LND_FIN_SR_UA_PC | Statutory Reporting for Ukraine - Configuration | S_ER9_11002887 | S_ER9_11002887_TRAN | J_1UFDI_TXDCTYPV | Maintain Document Types for Tax Invoices | 106452 | FI-LOC-FI-UA | FI-LOC-FI-UA |
| SAP_CA_BC_IC_LND_FIN_SR_UA_PC | Statutory Reporting for Ukraine - Configuration | S_ER9_11001184 | S_ER9_11001184_TRAN | V_FOT_TBS2 | Define Enhanced Tax Box Structure | 103011 | FI-LOC-FI-UA | FI-LOC-FI |
| SAP_CA_BC_IC_LND_FIN_SR_UA_PC | Statutory Reporting for Ukraine - Configuration | S_ER9_11002901 | S_ER9_11002901_TRAN | V_T604F_UA | Define Codes for Products and Services | 106574 | FI-LOC-FI-UA | FI-LOC-FI-UA |
| SAP_CA_BC_IC_LND_FIN_SR_UA_PC | Statutory Reporting for Ukraine - Configuration | S_ER1_70000883 | S_ER1_70000883_TRAN | J_1UVCM_USER | Define Custom Statuses for Incoming Tax Invoice XML Files | 106715 | FI-LOC-FI-UA | FI-LOC-FI-UA |
| SAP_CA_BC_IC_LND_FIN_SR_UA_PC | Statutory Reporting for Ukraine - Configuration | S_ER1_70000882 | S_ER1_70000882_TRAN | J_1UV_CASH_KVED | Define Accounting Method for Incoming Tax Invoices Based on FEA Code | 106714 | FI-LOC-FI-UA | FI-LOC-FI-UA |
| SAP_CA_BC_IC_LND_FIN_SR_UA_PC | Statutory Reporting for Ukraine - Configuration | S_ER1_70000887 | S_ER1_70000887_TRAN | J_1UF_REG_PER_V | Define Rules for ERPN Registration Period Determination | 106562 | FI-LOC-FI-UA | FI-LOC-FI-UA |
| SAP_CA_BC_IC_LND_FIN_SR_UA_PC | Statutory Reporting for Ukraine - Configuration | S_ER1_70001728 | S_ER1_70001728_TRAN | J_1UFV_VAT_ARTCL | Define Tax Article of the Code for VAT Accounting | 107203 | FI-LOC-FI-UA | FI-LOC-FI-UA |
| SAP_CA_BC_IC_LND_FIN_SR_UA_PC | Statutory Reporting for Ukraine - Configuration | S_ER1_70001750 | S_ER1_70001750_TRAN | J_1UFV_VAT_OPACE | Assign Article of Tax Law to VAT Codes | 107230 | FI-LOC-FI-UA | FI-LOC-FI-UA |
| SAP_CA_BC_IC_LND_FIN_SR_UA_PC | Statutory Reporting for Ukraine - Configuration | S_ER9_11002893 | S_ER9_11002893_TRAN |  |  |  | FI-LOC-FI-UA |  |
| SAP_PSM_BC_EF_WRKFLW_PC | Earmarked Funds - Workflow Configuration | F6951 | F6951_TRAN |  |  |  | PSM |  |
| SAP_CA_BC_IC_LND_FIN_BP0_PC | Business Partner - Configuration | S_ER9_52004337 | S_ER9_52004337_TRAN | BP_CERT_ACT | Activate Business Partner Certificates Functionality | 106517 | FI-LOC-IAM | FI-LOC-FI-QA |
| SAP_CA_BC_IC_LND_FIN_BP0_PC | Business Partner - Configuration | S_ER1_70000785 | S_ER1_70000785_TRAN | BP_CERT_ID | Define Business Partner Certificate IDs | 106646 | FI-LOC-IAM | FI-LOC-FI-QA |
| SAP_CA_BC_IC_LND_FIN_BP0_PC | Business Partner - Configuration | S_ER9_52004338 | S_ER9_52004338_TRAN | BP_CERT_ASSGN | Assign Business Partner Certificates to Country | 106468 | FI-LOC-IAM | FI-LOC-FI-QA |
| SAP_GLO_BC_ODN_PC | Globalization - Official Document Numbers | ODN_NR_DET | ODN_NR_DET_TRAN |  |  |  | FI-LOC-LO |  |
| SAP_GLO_BC_ODN_PC | Globalization - Official Document Numbers | WDA0180 | WDA0180_TRAN |  |  |  | FI-LOC-LO |  |
| SAP_CORE_BC_BCT_LLOG_PC | Business Configuration - Local Settings Change Logs | F6602 | F6602_TRAN |  |  |  | BC-CUS-TOL-ALO |  |
| SAP_CORE_BC_BCT_LLOG_PC | Business Configuration - Local Settings Change Logs | SP01_SIMPLE | SP01_SIMPLE_GLO_TRAN |  |  |  | BC-CUS-TOL-ALO |  |
| SAP_CA_BC_IC_LND_MIG_PC | Data Migration - Configuration | LTMOM_CU_02 |  | /LTB/MC_LTMOM_CU_02 | Model Your Migration Objects | 106575 | CA-LT | CA-LT-MC |
| SAP_CA_BC_IC_LND_MIG_PC | Data Migration - Configuration | /LTB/70000529 | LTB_70000529_TRAN | /LTB/MC_LTMOM_CU_02 | Model Your Migration Objects | 106575 | CA-LT | CA-LT-MC |
| SAP_CA_BC_IC_LND_FIN_COMP_PC | Company - Configuration | S_ALR_87007374 | S_ALR_87007374_TRAN | SIMG_CFMENUSAPCOX16 | Assign company code to company | 101631 | FI-GL | FI-GL-GL-N-2CL |
| SAP_CA_BC_IC_LND_FIN_COMP_PC | Company - Configuration | V_880_CLD |  | V_880_CLD | Create Company | 106040 | FI-GL | FI-GL-GL-N-2CL |
| SAP_CA_BC_IC_LND_FIN_COMP_PC | Company - Configuration | S_ER9_11002556 | S_ER9_11002556_TRAN | V_880_CLD | Create Company | 106040 | FI-GL | FI-GL-GL-N-2CL |
| SAP_CORE_BC_BCT_IMG_SCO | Implementation Activities - Scoped Activities (Deprecated) | SIMG_ACTIVITY_DOCU | SIMG_ACTIVITY_DOCU_TRAN |  |  |  | BC-CUS-TOL-IMG |  |
| SAP_CORE_BC_BCT_IMG_SCO | Implementation Activities - Scoped Activities (Deprecated) | SIMG | SIMG_PC_TRAN |  |  |  | BC-CUS-TOL-IMG |  |
| SAP_FIN_BC_TRM_AAASR_CONF_PC | TRM - Configuration for Additional Acct Assignments Substitution Rules | F7685 | F7685_TRAN |  |  |  | FIN-FSCM-TRM |  |
| SAP_CA_BC_IC_LND_FIN_TA2_PC | Financials - Jurisdiction Code and Taxes - Configuration | S_SAL_71000096 | S_SAL_71000096_TRAN | V_TTXJ_ABA | Define Tax Jurisdictions |  | CA-GTF-TS-TAX | CA-GTF-TS-TAX-2CL |
| SAP_CA_BC_IC_LND_FIN_TA2_PC | Financials - Jurisdiction Code and Taxes - Configuration | V_TTXJ_ABA |  | V_TTXJ_ABA | Define Tax Jurisdictions |  | CA-GTF-TS-TAX | CA-GTF-TS-TAX-2CL |
| SAP_CA_BC_IC_LND_FIN_SR_RS_PC | Statutory Reporting for Serbia - Configuration | S_ER9_11002017 | S_ER9_11002017_TRAN | FIVC_OFFS_DET_ACR | Activate Online Offsetting Account Determination for Several Countries/Rgns | 105333 | FI-LOC-FI-RS | FI-LOC-CF |
| SAP_CA_BC_IC_LND_FIN_SR_RS_PC | Statutory Reporting for Serbia - Configuration | S_ER9_11002764 | S_ER9_11002764_TRAN | FIRSVC_OFFS_VER_D_CE | Define Offsetting Account Determination Versions for Serbia | 106492 | FI-LOC-FI-RS | FI-LOC-CF-RS |

## Connections
- part-of :: [[_cluster]]
- related-to :: [[01-solution-foundation-and-platform/sscui-list-en-xx-sap-s-4hana-cloud-2608-configuration-2-part-37]]
- related-to :: [[01-solution-foundation-and-platform/sscui-list-en-xx-sap-s-4hana-cloud-2608-configuration-2-part-39]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Configuration/SSCUI_List_EN_XX.xlsm` — lines 10035–11300 of the extracted text · extracted with `xlsx2md` · 9,788,312 chars in the whole document
