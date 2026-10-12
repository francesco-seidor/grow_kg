---
id: 06-management-accounting/2608-master-data-co-en-xx-118
title: 2608 Master Data CO EN XX (2608_Master_Data_CO_EN_XX)
description: "SAP S/4HANA Cloud Public Edition 2608 Best Practices controlling master data workbook: cost centers, activity types, secondary cost elements, groups, statistical key figures."
cluster: 06-management-accounting
tags: [kb/management-accounting, topic/controlling-master-data-workbook]
aliases: [2608_Master_Data_CO_EN_XX]
keywords: [Best Practice CO and FI Master Data Values, cost centers, cost center groups, cost center id convention, activity types, activity type groups, secondary cost elements, cost element groups, statistical key figures, controlling master data]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/General/2608_Master_Data_CO_EN_XX.xlsx]
confidence: low
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-118
topic: 06-management-accounting/controlling-master-data-workbook
language: EN
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# 2608 Master Data CO EN XX (2608_Master_Data_CO_EN_XX)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/General/2608_Master_Data_CO_EN_XX.xlsx`, extracted with `xlsx2md`. Grouped under **Best Practice CO and FI Master Data Values** in Management Accounting. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

## 2608 Master Data CO EN XX

### Sheet: Start

Cost Centers

Cost Center Groups

Activity Types

Activity Type Groups

Secondary Cost Elements

Cost Element Groups

Statistical Key Figures

Cost Center IDs are defined using the following convention: CoCo9999:
CoCo = the four digit Company Code with ##10 (## 2 digit country code)
9999 = a four digit, numeric ID indicating the function of the cost center (same in all company codes)
--> Cost Center 1101 in the US Company Code 1710 = 17101101
--> Cost Center 1101 in the DE Company Code 1010 = 10101101

### Sheet: Copyright

© 2026 SAP SE or an SAP affiliate company. All rights reserved.

No part of this publication may be reproduced or transmitted in any form or for any purpose without the express permission of SAP SE or an SAP affiliate company.

The information contained herein may be changed without prior notice. Some software products marketed by SAP SE and its distributors contain proprietary software components of other software vendors. National product specifications may vary.

These materials are provided by SAP SE or an SAP affiliate company for informational purposes only, without representation or warranty of any kind, and SAP or its affiliated companies shall not be liable for errors or omissions with respect to the materials. The only warranties for SAP or SAP affiliate company products and services are those that are set forth in the express warranty statements accompanying such products and services, if any. Nothing herein should be construed as constituting an additional warranty.

In particular, SAP SE or its affiliated companies have no obligation to pursue any course of business outlined in this document or any related presentation, or to develop or release any functionality mentioned therein. This document, or any related presentation, and SAP SE’s or its affiliated companies’ strategy and possible future developments, products, and/or platforms, directions, and functionality are all subject to change and may be changed by SAP SE or its affiliated companies at any time for any reason without notice. The information in this document is not a commitment, promise, or legal obligation to deliver any material, code, or functionality. All forward-looking statements are subject to various risks and uncertainties that could cause actual results to differ materially from expectations. Readers are cautioned not to place undue reliance on these forward-looking statements, and they should not be relied upon in making purchasing decisions.

SAP and other SAP products and services mentioned herein as well as their respective logos are trademarks or registered trademarks of SAP SE (or an SAP affiliate company) in Germany and other countries. All other product and service names mentioned are the trademarks of their respective companies.

See www.sap.com/copyright for additional trademark information and notices.

### Sheet: Cost Centers

| Cost Center ID | Name | Category | Standard Hierarchy | Functional Area | Controlling Area | Country |
| --- | --- | --- | --- | --- | --- | --- |
| 10101040 | Template Store | V | 001 |  | A000 | DE |
| 10101050 | Template DC | V | 001 |  | A000 | DE |
| 17101740 | Template Store | V | 001 |  | A000 | US |
| 17101754 | Template DC | V | 001 |  | A000 | US |
| 29102940 | Template Store | V | 001 |  | A000 | CA |
| 29102950 | Template DC | V | 001 |  | A000 | CA |
| 22102240 | Template Store | V | 001 |  | A000 | CH |
| 22102250 | Template DC | V | 001 |  | A000 | CH |
| 20102040 | Template Store | V | 001 |  | A000 | CZ |
| 20102050 | Template DC | V | 001 |  | A000 | CZ |
| 24102440 | Template Store | V | 001 |  | A000 | ES |
| 24102450 | Template DC | V | 001 |  | A000 | ES |
| 12101240 | Template Store | V | 001 |  | A000 | FR |
| 12101250 | Template DC | V | 001 |  | A000 | FR |
| 44104440 | Template Store | V | 001 |  | A000 | NO |
| 44104450 | Template DC | V | 001 |  | A000 | NO |
| 26102640 | Template Store | V | 001 |  | A000 | PL |
| 26102650 | Template DC | V | 001 |  | A000 | PL |
| 35103540 | Template Store | V | 001 |  | A000 | PT |
| 35103550 | Template DC | V | 001 |  | A000 | PT |
| 27102740 | Template Store | V | 001 |  | A000 | SK |
| 27102750 | Template DC | V | 001 |  | A000 | SK |
| 10101041 | Demo Store 1 | V | 001 | YB30 | A000 | DE |
| 10101042 | Demo Store 2 | V | 001 | YB30 | A000 | DE |
| 10101043 | Demo Store 3 | V | 001 | YB30 | A000 | DE |
| 10101044 | Demo Store 4 | V | 001 | YB30 | A000 | DE |
| 17101741 | Demo Store 1 | V | 001 | YB30 | A000 | US |
| 17101742 | Demo Store 2 | V | 001 | YB30 | A000 | US |
| 17101743 | Demo Store 3 | V | 001 | YB30 | A000 | US |
| 17101744 | Demo Store 4 | V | 001 | YB30 | A000 | US |
| 29102941 | Demo Store 1 | V | 001 | YB30 | A000 | CA |
| 29102942 | Demo Store 2 | V | 001 | YB30 | A000 | CA |
| 29102943 | Demo Store 3 | V | 001 | YB30 | A000 | CA |
| 29102944 | Demo Store 4 | V | 001 | YB30 | A000 | CA |
| 22102241 | Demo Store 1 | V | 001 | YB30 | A000 | CH |
| 22102242 | Demo Store 2 | V | 001 | YB30 | A000 | CH |
| 22102243 | Demo Store 3 | V | 001 | YB30 | A000 | CH |
| 22102244 | Demo Store 4 | V | 001 | YB30 | A000 | CH |
| 20102041 | Demo Store 1 | V | 001 | YB30 | A000 | CZ |
| 20102042 | Demo Store 2 | V | 001 | YB30 | A000 | CZ |
| 20102043 | Demo Store 3 | V | 001 | YB30 | A000 | CZ |
| 20102044 | Demo Store 4 | V | 001 | YB30 | A000 | CZ |
| 24102441 | Demo Store 1 | V | 001 | YB30 | A000 | ES |
| 24102442 | Demo Store 2 | V | 001 | YB30 | A000 | ES |
| 24102443 | Demo Store 3 | V | 001 | YB30 | A000 | ES |
| 24102444 | Demo Store 4 | V | 001 | YB30 | A000 | ES |
| 12101241 | Demo Store 1 | V | 001 | YB30 | A000 | FR |
| 12101242 | Demo Store 2 | V | 001 | YB30 | A000 | FR |
| 12101243 | Demo Store 3 | V | 001 | YB30 | A000 | FR |
| 12101244 | Demo Store 4 | V | 001 | YB30 | A000 | FR |
| 44104441 | Demo Store 1 | V | 001 | YB30 | A000 | NO |
| 44104442 | Demo Store 2 | V | 001 | YB30 | A000 | NO |
| 44104443 | Demo Store 3 | V | 001 | YB30 | A000 | NO |
| 44104444 | Demo Store 4 | V | 001 | YB30 | A000 | NO |
| 26102641 | Demo Store 1 | V | 001 | YB30 | A000 | PL |
| 26102642 | Demo Store 2 | V | 001 | YB30 | A000 | PL |
| 26102643 | Demo Store 3 | V | 001 | YB30 | A000 | PL |
| 26102644 | Demo Store 4 | V | 001 | YB30 | A000 | PL |
| 35103541 | Demo Store 1 | V | 001 | YB30 | A000 | PT |
| 35103542 | Demo Store 2 | V | 001 | YB30 | A000 | PT |
| 35103543 | Demo Store 3 | V | 001 | YB30 | A000 | PT |
| 35103544 | Demo Store 4 | V | 001 | YB30 | A000 | PT |
| 27102741 | Demo Store 1 | V | 001 | YB30 | A000 | SK |
| 27102742 | Demo Store 2 | V | 001 | YB30 | A000 | SK |
| 27102743 | Demo Store 3 | V | 001 | YB30 | A000 | SK |
| 27102744 | Demo Store 4 | V | 001 | YB30 | A000 | SK |
| 10101101 | Financials (DE) | W | 001 | YB40 | A000 | DE |
| 10101601 | Marketing (DE) | 9 | 001 | YB35 | A000 | DE |
| 10101602 | Sales (DE) | V | 001 | YB30 | A000 | DE |
| 10101801 | Other Inc.&Expense (DE) | W | 001 | YB40 | A000 | DE |
| 10101750 | Build. & Maintenance (DE) | H | 001 | YB40 | A000 | DE |
| 10101201 | Purch & Stores 1 (DE) | G | 001 | YB20 | A000 | DE |
| 10101202 | Purch & Stores 2 (DE) | G | 001 | YB20 | A000 | DE |
| 10101902 | Consulting Unit A (DE) | C | 001 | YB25 | A000 | DE |
| 10101301 | Manufacturing 1 (DE) | F | 001 | YB20 | A000 | DE |
| 10101302 | Manufacturing 2 (DE) | F | 001 | YB20 | A000 | DE |
| 10101401 | QM (DE) | H | 001 | YB40 | A000 | DE |
| 10101501 | R&D (DE) | E | 001 | YB50 | A000 | DE |
| 10101701 | Plant & Maintenance (DE) | H | 001 | YB40 | A000 | DE |
| 10101321 | Services/Consulting (DE) | F | 001 | YB20 | A000 | DE |
| 10101751 | HR Services (DE) | W | 001 | YB40 | A000 | DE |
| 10101752 | HR Recruitment (DE) | W | 001 | YB40 | A000 | DE |
| 10101753 | IT Services (DE) | W | 001 | YB40 | A000 | DE |
| 10101901 | Back Office (DE) | H | 001 | YB30 | A000 | DE |
| 10101903 | Consulting Unit B (DE) | C | 001 | YB25 | A000 | DE |
| 10101904 | Customer Development (DE) | C | 001 | YB25 | A000 | DE |
| 17109000 | Small Bus. Lending, Payments & Services | R | 001 |  | A000 | US |
| 17109005 | Small Bus. Deposit Gathering & Services | R | 001 |  | A000 | US |
| 17109010 | Community Lending, Payments & Services | U | 001 |  | A000 | US |
| 17109015 | Community Deposit Gathering & Services | U | 001 |  | A000 | US |
| 17109020 | Consumer Lending & Services | R | 001 |  | A000 | US |
| 17109025 | Consumer Deposit Gathering & Services | R | 001 |  | A000 | US |
| 17109027 | Consumer Payments & Services | R | 001 |  | A000 | US |
| 17109030 | Commercial Lending & Services | O | 001 |  | A000 | US |
| 17109035 | Commercial Deposit Gathering & Services | O | 001 |  | A000 | US |
| 17109037 | Corporate Teasury Services | O | 001 |  | A000 | US |
| 17109040 | Wealth Management  Services | P | 001 |  | A000 | US |
| 17109045 | Brokerage & Private Client Services | P | 001 |  | A000 | US |
| 17109050 | Investments & Trading Operations | T | 001 |  | A000 | US |
| 17109055 | Trade Settlements and Services | T | 001 |  | A000 | US |
| 17109060 | Corporate  Finance Controllership | X | 001 |  | A000 | US |
| 17109065 | Corporate Risk Controllership | X | 001 |  | A000 | US |
| 17109070 | Real Estate Management & Services | X | 001 |  | A000 | US |
| 17109075 | Technology Services | X | 001 |  | A000 | US |
| 17109057 | Corporate Overhead | X | 001 |  | A000 | US |
| 17109999 | Suspense Cost Center | X | 001 |  | A000 | US |
| 17108000 | Marketing | V | 001 |  | A000 | US |
| 17108005 | Sales Region A | V | 001 |  | A000 | US |
| 17108010 | Sales Region B | V | 001 |  | A000 | US |
| 17108015 | Sales Region C | V | 001 |  | A000 | US |
| 17108020 | Billing | V | 001 |  | A000 | US |
| 17108025 | Claims Handling | A | 001 |  | A000 | US |
| 17108030 | Underwriting | Q | 001 |  | A000 | US |
| 17108035 | Corporate Accounting | I | 001 |  | A000 | US |
| 17108040 | Information Technology | I | 001 |  | A000 | US |
| 17108045 | Human Resources | I | 001 |  | A000 | US |
| 17108050 | Legal Department | I | 001 |  | A000 | US |
| 17108055 | Corporate Actuary | I | 001 |  | A000 | US |
| 17108060 | Internal Audit | I | 001 |  | A000 | US |
| 17108065 | Investments | I | 001 |  | A000 | US |
| 17108070 | Corporate Facility Mgmt & Real Estate | I | 001 |  | A000 | US |
| 17108075 | Administration Intercompany Settlement | I | 001 |  | A000 | US |
| 17101101 | Financials (US) | W | 001 | YB40 | A000 | US |
| 17101601 | Marketing (US) | 9 | 001 | YB35 | A000 | US |
| 17101602 | Sales (US) | V | 001 | YB30 | A000 | US |
| 17101801 | Other Inc.&Expense (US) | W | 001 | YB40 | A000 | US |
| 17101750 | Build. & Maintenance (US) | H | 001 | YB40 | A000 | US |
| 17101201 | Purch & Stores 1 (US) | G | 001 | YB20 | A000 | US |
| 17101202 | Purch & Stores 2 (US) | G | 001 | YB20 | A000 | US |
| 17101902 | Consulting Unit A (US) | C | 001 | YB25 | A000 | US |
| 17101301 | Manufacturing 1 (US) | F | 001 | YB20 | A000 | US |
| 17101302 | Manufacturing 2 (US) | F | 001 | YB20 | A000 | US |
| 17101401 | QM (US) | H | 001 | YB40 | A000 | US |
| 17101501 | R&D (US) | E | 001 | YB50 | A000 | US |
| 17101701 | Plant & Maintenance (US) | H | 001 | YB40 | A000 | US |
| 17101321 | Services/Consulting (US) | F | 001 | YB20 | A000 | US |
| 17101751 | HR Services-(US) | W | 001 | YB40 | A000 | US |
| 17101752 | HR Recruitment-(US) | W | 001 | YB40 | A000 | US |
| 17101753 | IT Services-(US) | W | 001 | YB40 | A000 | US |
| 17101901 | Back Office-(US) | H | 001 | YB30 | A000 | US |
| 17101903 | Consulting Unit B-(US) | C | 001 | YB25 | A000 | US |
| 17101904 | Customer Development-(US) | C | 001 | YB25 | A000 | US |
| 17101101 | Financials (US) | W | 001 | 1000 | A000 | US |
| 17101601 | Transportation (US) | 9 | 001 | 1500 | A000 | US |
| 17101602 | Human Resources (US) | V | 001 | 1000 | A000 | US |
| 17101801 | Other Inc.&Expense (US) | W | 001 | 1000 | A000 | US |
| 17101750 | Build. & Maintenance (US) | H | 001 | 1500 | A000 | US |
| 17101201 | Purch & Store (US) | G | 001 | 1000 | A000 | US |
| 17101202 | Construction & Engineering (US) | G | 001 | 4000 | A000 | US |
| 17101902 | Communications (US) | C | 001 | 3000 | A000 | US |
| 17101301 | Planning (US) | F | 001 | 1000 | A000 | US |
| 17101302 | Administration (US) | F | 001 | 1500 | A000 | US |
| 17101401 | Operations (US) | H | 001 | 1000 | A000 | US |
| 17101501 | Information Technology (US) | E | 001 | 4750 | A000 | US |
| 17101701 | Plant & Maintenance (US) | H | 001 | 4000 | A000 | US |
| 17101321 | Services (US) | F | 001 | 1000 | A000 | US |
| 17101751 | HR Services (US) | W | 001 | 1550 | A000 | US |
| 17101752 | HR Recruitment (US) | W | 001 | 1550 | A000 | US |
| 17101753 | IT Services (US) | W | 001 | 4750 | A000 | US |
| 17101901 | Back Office (US) | H | 001 | 1500 | A000 | US |
| 17101903 | Consulting Unit B (US) | C | 001 | 8000 | A000 | US |
| 17101904 | Customer Development (US) | C | 001 | 5500 | A000 | US |
| 33101101 | Financials (AE) | W | 001 | YB40 | A000 | AE |
| 33101601 | Marketing (AE) | 9 | 001 | YB35 | A000 | AE |
| 33101602 | Sales (AE) | V | 001 | YB30 | A000 | AE |
| 33101801 | Other Inc.&Expense (AE) | W | 001 | YB40 | A000 | AE |
| 33101750 | Build. & Maintenance (AE) | H | 001 | YB40 | A000 | AE |
| 33101201 | Purch & Stores 1 (AE) | G | 001 | YB20 | A000 | AE |
| 33101202 | Purch & Stores 2 (AE) | G | 001 | YB20 | A000 | AE |
| 33101902 | Consulting Unit A (AE) | C | 001 | YB25 | A000 | AE |
| 33101301 | Manufacturing 1 (AE) | F | 001 | YB20 | A000 | AE |
| 33101302 | Manufacturing 2 (AE) | F | 001 | YB20 | A000 | AE |
| 33101401 | QM (AE) | H | 001 | YB40 | A000 | AE |
| 33101501 | R&D (AE) | E | 001 | YB50 | A000 | AE |
| 33101701 | Plant & Maintenance (AE) | H | 001 | YB40 | A000 | AE |
| 33101321 | Services/Consulting (AE) | F | 001 | YB20 | A000 | AE |
| 33101751 | HR Services (AE) | W | 001 | YB40 | A000 | AE |
| 33101752 | HR Recruitment (AE) | W | 001 | YB40 | A000 | AE |
| 33101753 | IT Services (AE) | W | 001 | YB40 | A000 | AE |
| 33101901 | Back Office (AE) | H | 001 | YB30 | A000 | AE |
| 33101903 | Consulting Unit B (AE) | C | 001 | YB25 | A000 | AE |
| 33101904 | Customer Development (AE) | C | 001 | YB25 | A000 | AE |
| 31101101 | Financials (AR) | W | 001 |  | A000 | AR |
| 31101601 | Marketing (AR) | 9 | 001 |  | A000 | AR |
| 31101602 | Sales (AR) | V | 001 |  | A000 | AR |
| 31101801 | Other Inc.&Expense (AR) | W | 001 |  | A000 | AR |
| 31101750 | Build. & Maintenance (AR) | H | 001 |  | A000 | AR |
| 31101201 | Purch & Stores 1 (AR) | G | 001 |  | A000 | AR |
| 31101202 | Purch & Stores 2 (AR) | G | 001 |  | A000 | AR |
| 31101902 | Consulting Unit A (AR) | C | 001 |  | A000 | AR |
| 31101301 | Manufacturing 1 (AR) | F | 001 |  | A000 | AR |
| 31101302 | Manufacturing 2 (AR) | F | 001 |  | A000 | AR |
| 31101401 | QM (AR) | H | 001 |  | A000 | AR |
| 31101501 | R&D (AR) | E | 001 |  | A000 | AR |
| 31101701 | Plant & Maintenance (AR) | H | 001 |  | A000 | AR |
| 31101321 | Services/Consulting (AR) | F | 001 |  | A000 | AR |
| 31101751 | HR Services (AR) | W | 001 | YB40 | A000 | AR |
| 31101752 | HR Recruitment (AR) | W | 001 | YB40 | A000 | AR |
| 31101753 | IT Services (AR) | W | 001 | YB40 | A000 | AR |
| 31101901 | Back Office (AR) | H | 001 | YB30 | A000 | AR |
| 31101903 | Consulting Unit B (AR) | C | 001 | YB25 | A000 | AR |
| 31101904 | Customer Development (AR) | C | 001 | YB25 | A000 | AR |
| 39101101 | Financials (AT) | W | 001 | YB40 | A000 | AT |
| 39101601 | Marketing (AT) | 9 | 001 | YB35 | A000 | AT |
| 39101602 | Sales (AT) | V | 001 | YB30 | A000 | AT |
| 39101801 | Other Inc.&Expense (AT) | W | 001 | YB40 | A000 | AT |
| 39101750 | Build. & Maintenance (AT) | H | 001 | YB40 | A000 | AT |
| 39101201 | Purch & Stores 1 (AT) | G | 001 | YB20 | A000 | AT |
| 39101202 | Purch & Stores 2 (AT) | G | 001 | YB20 | A000 | AT |
| 39101902 | Consulting Unit A (AT) | C | 001 | YB25 | A000 | AT |
| 39101301 | Manufacturing 1 (AT) | F | 001 | YB20 | A000 | AT |
| 39101302 | Manufacturing 2 (AT) | F | 001 | YB20 | A000 | AT |
| 39101401 | QM (AT) | H | 001 | YB40 | A000 | AT |
| 39101501 | R&D (AT) | E | 001 | YB50 | A000 | AT |
| 39101701 | Plant & Maintenance (AT) | H | 001 | YB40 | A000 | AT |
| 39101321 | Services/Consulting (AT) | F | 001 | YB20 | A000 | AT |
| 39101751 | HR Services (AT) | W | 001 | YB40 | A000 | AT |
| 39101752 | HR Recruitment (AT) | W | 001 | YB40 | A000 | AT |
| 39101753 | IT Services (AT) | W | 001 | YB40 | A000 | AT |
| 39101901 | Back Office (AT) | H | 001 | YB30 | A000 | AT |
| 39101903 | Consulting Unit B (AT) | C | 001 | YB25 | A000 | AT |
| 39101904 | Customer Development (AT) | C | 001 | YB25 | A000 | AT |
| 30101101 | Financials (AU) | W | 001 | YB40 | A000 | AU |
| 30101601 | Marketing (AU) | 9 | 001 | YB35 | A000 | AU |
| 30101602 | Sales (AU) | V | 001 | YB30 | A000 | AU |
| 30101801 | Other Inc.&Expense (AU) | W | 001 | YB40 | A000 | AU |
| 30101750 | Build. & Maintenance (AU) | H | 001 | YB40 | A000 | AU |
| 30101201 | Purch & Stores 1 (AU) | G | 001 | YB20 | A000 | AU |
| 30101202 | Purch & Stores 2 (AU) | G | 001 | YB20 | A000 | AU |
| 30101902 | Consulting Unit A-(AU) | C | 001 | YB25 | A000 | AU |
| 30101301 | Manufacturing 1 (AU) | F | 001 | YB20 | A000 | AU |
| 30101302 | Manufacturing 2 (AU) | F | 001 | YB20 | A000 | AU |
| 30101401 | QM (AU) | H | 001 | YB40 | A000 | AU |
| 30101501 | R&D (AU) | E | 001 | YB50 | A000 | AU |
| 30101701 | Plant & Maintenance (AU) | H | 001 | YB40 | A000 | AU |
| 30101321 | Services/Consulting (AU) | F | 001 | YB20 | A000 | AU |
| 30101751 | HR Services-(AU) | W | 001 | YB40 | A000 | AU |
| 30101752 | HR Recruitment-(AU) | W | 001 | YB40 | A000 | AU |
| 30101753 | IT Services-(AU) | W | 001 | YB40 | A000 | AU |
| 30101901 | Back Office-(AU) | H | 001 | YB30 | A000 | AU |
| 30101903 | Consulting Unit B-(AU) | C | 001 | YB25 | A000 | AU |
| 30101904 | Customer Development-(AU) | C | 001 | YB25 | A000 | AU |
| 25101101 | Financials (BE) | W | 001 | YB40 | A000 | BE |
| 25101601 | Marketing (BE) | 9 | 001 | YB35 | A000 | BE |
| 25101602 | Sales (BE) | V | 001 | YB30 | A000 | BE |
| 25101801 | Other Inc.&Expense (BE) | W | 001 | YB40 | A000 | BE |
| 25101750 | Build. & Maintenance (BE) | H | 001 | YB40 | A000 | BE |
| 25101201 | Purch & Stores 1 (BE) | G | 001 | YB20 | A000 | BE |
| 25101202 | Purch & Stores 2 (BE) | G | 001 | YB20 | A000 | BE |
| 25101902 | Consulting Unit A (BE) | C | 001 | YB25 | A000 | BE |
| 25101301 | Manufacturing 1 (BE) | F | 001 | YB20 | A000 | BE |
| 25101302 | Manufacturing 2 (BE) | F | 001 | YB20 | A000 | BE |
| 25101401 | QM (BE) | H | 001 | YB40 | A000 | BE |
| 25101501 | R&D (BE) | E | 001 | YB50 | A000 | BE |
| 25101701 | Plant & Maintenance (BE) | H | 001 | YB40 | A000 | BE |
| 25101321 | Services/Consulting (BE) | F | 001 | YB20 | A000 | BE |
| 25101751 | HR Services (BE) | W | 001 | YB40 | A000 | BE |
| 25101752 | HR Recruitment (BE) | W | 001 | YB40 | A000 | BE |
| 25101753 | IT Services (BE) | W | 001 | YB40 | A000 | BE |
| 25101901 | Back Office (BE) | H | 001 | YB30 | A000 | BE |
| 25101903 | Consulting Unit B (BE) | C | 001 | YB25 | A000 | BE |
| 25101904 | Customer Development (BE) | C | 001 | YB25 | A000 | BE |
| 38101101 | Financials (BG) | W | 001 | YB40 | A000 | BG |
| 38101601 | Marketing (BG) | 9 | 001 | YB35 | A000 | BG |
| 38101602 | Sales (BG) | V | 001 | YB30 | A000 | BG |
| 38101801 | Other Inc.&Expense (BG) | W | 001 | YB40 | A000 | BG |
| 38101750 | Build. & Maintenance (BG) | H | 001 | YB40 | A000 | BG |
| 38101201 | Purch & Stores 1 (BG) | G | 001 | YB20 | A000 | BG |
| 38101202 | Purch & Stores 2 (BG) | G | 001 | YB20 | A000 | BG |
| 38101902 | Consulting Unit A (BG) | C | 001 | YB25 | A000 | BG |
| 38101301 | Manufacturing 1 (BG) | F | 001 | YB20 | A000 | BG |
| 38101302 | Manufacturing 2 (BG) | F | 001 | YB20 | A000 | BG |
| 38101401 | QM (BG) | H | 001 | YB40 | A000 | BG |
| 38101501 | R&D (BG) | E | 001 | YB50 | A000 | BG |
| 38101701 | Plant & Maintenance (BG) | H | 001 | YB40 | A000 | BG |
| 38101321 | Services/Consulting (BG) | F | 001 | YB20 | A000 | BG |
| 38101751 | HR Services (BG) | W | 001 | YB40 | A000 | BG |
| 38101752 | HR Recruitment (BG) | W | 001 | YB40 | A000 | BG |
| 38101753 | IT Services (BG) | W | 001 | YB40 | A000 | BG |
| 38101901 | Back Office (BG) | H | 001 | YB30 | A000 | BG |
| 38101903 | Consulting Unit B (BG) | C | 001 | YB25 | A000 | BG |
| 38101904 | Customer Development (BG) | C | 001 | YB25 | A000 | BG |
| 14101101 | Financials (BR) | W | 001 | YB40 | A000 | BR |
| 14101601 | Marketing (BR) | 9 | 001 | YB35 | A000 | BR |
| 14101602 | Sales (BR) | V | 001 | YB30 | A000 | BR |
| 14101801 | Other Inc.&Expense (BR) | W | 001 | YB40 | A000 | BR |
| 14101750 | Build. & Maintenance (BR) | H | 001 | YB40 | A000 | BR |
| 14101201 | Purch & Stores 1 (BR) | G | 001 | YB20 | A000 | BR |
| 14101202 | Purch & Stores 2 (BR) | G | 001 | YB20 | A000 | BR |
| 14101902 | Consulting Unit A (BR) | C | 001 | YB25 | A000 | BR |
| 14101301 | Manufacturing 1 (BR) | F | 001 | YB20 | A000 | BR |
| 14101302 | Manufacturing 2 (BR) | F | 001 | YB20 | A000 | BR |
| 14101401 | QM (BR) | H | 001 | YB40 | A000 | BR |
| 14101501 | R&D (BR) | E | 001 | YB50 | A000 | BR |
| 14101701 | Plant & Maintenance (BR) | H | 001 | YB40 | A000 | BR |
| 14101321 | Services/Consulting (BR) | F | 001 | YB20 | A000 | BR |
| 14101751 | HR Services-(BR) | W | 001 | YB40 | A000 | BR |
| 14101752 | HR Recruitment-(BR) | W | 001 | YB40 | A000 | BR |
| 14101753 | IT Services-(BR) | W | 001 | YB40 | A000 | BR |
| 14101901 | Back Office-(BR) | H | 001 | YB30 | A000 | BR |
| 14101903 | Consulting Unit B-(BR) | C | 001 | YB25 | A000 | BR |
| 14101904 | Customer Development-(BR) | C | 001 | YB25 | A000 | BR |
| 29101101 | Financials (CA) | W | 001 | YB40 | A000 | CA |
| 29101601 | Marketing (CA) | 9 | 001 | YB35 | A000 | CA |
| 29101602 | Sales (CA) | V | 001 | YB30 | A000 | CA |
| 29101801 | Other Inc.&Expense (CA) | W | 001 | YB40 | A000 | CA |
| 29101750 | Build. & Maintenance (CA) | H | 001 | YB40 | A000 | CA |
| 29101201 | Purchasing & Stores 1 (CA) | G | 001 | YB20 | A000 | CA |
| 29101202 | Purchasing & Stores 2 (CA) | G | 001 | YB20 | A000 | CA |
| 29101902 | Consulting Unit A (CA) | C | 001 | YB25 | A000 | CA |
| 29101301 | Manufacturing 1 (CA) | F | 001 | YB20 | A000 | CA |
| 29101302 | Manufacturing 2 (CA) | F | 001 | YB20 | A000 | CA |
| 29101401 | Quality management (CA) | H | 001 | YB40 | A000 | CA |
| 29101501 | Research and development (CA) | E | 001 | YB50 | A000 | CA |
| 29101701 | Plant & Maintenance (CA) | H | 001 | YB40 | A000 | CA |
| 29101321 | Services/Consulting (US) | F | 001 | YB20 | A000 | CA |
| 29101751 | HR Services (CA) | W | 001 | YB40 | A000 | CA |
| 29101752 | HR Recruitment (CA) | W | 001 | YB40 | A000 | CA |
| 29101753 | IT Services (CA) | W | 001 | YB40 | A000 | CA |
| 29101901 | Back Office (CA) | H | 001 | YB30 | A000 | CA |
| 29101903 | Consulting Unit B (CA) | C | 001 | YB25 | A000 | CA |
| 29101904 | Customer Development (CA) | C | 001 | YB25 | A000 | CA |
| 22101101 | Financials (CH) | W | 001 | YB40 | A000 | CH |
| 22101601 | Marketing (CH) | 9 | 001 | YB35 | A000 | CH |
| 22101602 | Sales (CH) | V | 001 | YB30 | A000 | CH |
| 22101801 | Other Inc.&Expense (CH) | W | 001 | YB40 | A000 | CH |
| 22101750 | Build. & Maintenance (CH) | H | 001 | YB40 | A000 | CH |
| 22101201 | Purch & Stores 1 (CH) | G | 001 | YB20 | A000 | CH |
| 22101202 | Purch & Stores 2 (CH) | G | 001 | YB20 | A000 | CH |
| 22101902 | Consulting Unit A (CH) | C | 001 | YB25 | A000 | CH |
| 22101301 | Manufacturing 1 (CH) | F | 001 | YB20 | A000 | CH |
| 22101302 | Manufacturing 2 (CH) | F | 001 | YB20 | A000 | CH |
| 22101401 | QM (CH) | H | 001 | YB40 | A000 | CH |
| 22101501 | R&D (CH) | E | 001 | YB50 | A000 | CH |
| 22101701 | Plant & Maintenance (CH) | H | 001 | YB40 | A000 | CH |
| 22101321 | Services/Consulting (CH) | F | 001 | YB20 | A000 | CH |
| 22101751 | HR Services (CH) | W | 001 | YB40 | A000 | CH |
| 22101752 | HR Recruitment (CH) | W | 001 | YB40 | A000 | CH |
| 22101753 | IT Services (CH) | W | 001 | YB40 | A000 | CH |
| 22101901 | Back Office (CH) | H | 001 | YB30 | A000 | CH |
| 22101903 | Consulting Unit B (CH) | C | 001 | YB25 | A000 | CH |
| 22101904 | Customer Development (CH) | C | 001 | YB25 | A000 | CH |
| 46101101 | Financials (CL) | W | 001 | YB40 | A000 | CL |
| 46101601 | Marketing (CL) | 9 | 001 | YB35 | A000 | CL |
| 46101602 | Sales (CL) | V | 001 | YB30 | A000 | CL |
| 46101801 | Other Inc.&Expense (CL) | W | 001 | YB40 | A000 | CL |
| 46101750 | Build. & Maintenance (CL) | H | 001 | YB40 | A000 | CL |
| 46101201 | Purch & Stores 1 (CL) | G | 001 | YB20 | A000 | CL |
| 46101202 | Purch & Stores 2 (CL) | G | 001 | YB20 | A000 | CL |
| 46101902 | Consulting Unit A (CL) | C | 001 | YB25 | A000 | CL |
| 46101301 | Manufacturing 1 (CL) | F | 001 | YB20 | A000 | CL |
| 46101302 | Manufacturing 2 (CL) | F | 001 | YB20 | A000 | CL |
| 46101401 | QM (CL) | H | 001 | YB40 | A000 | CL |
| 46101501 | R&D (CL) | E | 001 | YB50 | A000 | CL |
| 46101701 | Plant & Maintenance (CL) | H | 001 | YB40 | A000 | CL |
| 46101321 | Services/Consulting (CL) | F | 001 | YB20 | A000 | CL |
| 46101751 | HR Services (CL) | W | 001 | YB40 | A000 | CL |
| 46101752 | HR Recruitment (CL) | W | 001 | YB40 | A000 | CL |
| 46101753 | IT Services (CL) | W | 001 | YB40 | A000 | CL |
| 46101901 | Back Office (CL) | H | 001 | YB30 | A000 | CL |
| 46101903 | Consulting Unit B (CL) | C | 001 | YB25 | A000 | CL |
| 46101904 | Customer Development (CL) | C | 001 | YB25 | A000 | CL |
| 13101101 | Financials (CN) | W | 001 | YB40 | A000 | CN |
| 13101601 | Marketing (CN) | 9 | 001 | YB35 | A000 | CN |
| 13101602 | Sales (CN) | V | 001 | YB30 | A000 | CN |
| 13101801 | Other Inc.&Expense (CN) | W | 001 | YB40 | A000 | CN |
| 13101750 | Build. & Maintenance (CN) | H | 001 | YB40 | A000 | CN |
| 13101201 | Purch & Stores 1 (CN) | G | 001 | YB20 | A000 | CN |
| 13101202 | Purch & Stores 2 (CN) | G | 001 | YB20 | A000 | CN |
| 13101902 | Consulting Unit A (CN) | C | 001 | YB25 | A000 | CN |
| 13101301 | Manufacturing 1 (CN) | F | 001 | YB20 | A000 | CN |
| 13101302 | Manufacturing 2 (CN) | F | 001 | YB20 | A000 | CN |
| 13101401 | QM (CN) | H | 001 | YB40 | A000 | CN |
| 13101501 | R&D (CN) | E | 001 | YB50 | A000 | CN |
| 13101701 | Plant & Maintenance (CN) | H | 001 | YB40 | A000 | CN |
| 13101321 | Services/Consulting (CN) | F | 001 | YB20 | A000 | CN |
| 13101751 | HR Services (CN) | W | 001 | YB40 | A000 | CN |
| 13101752 | HR Recruitment (CN) | W | 001 | YB40 | A000 | CN |
| 13101753 | IT Services (CN) | W | 001 | YB40 | A000 | CN |
| 13101901 | Back Office (CN) | H | 001 | YB30 | A000 | CN |
| 13101903 | Consulting Unit B (CN) | C | 001 | YB25 | A000 | CN |
| 13101904 | Customer Development (CN) | C | 001 | YB25 | A000 | CN |
| 48101101 | Financials (CO) | W | 001 | YB40 | A000 | CO |
| 48101601 | Marketing (CO) | 9 | 001 | YB35 | A000 | CO |
| 48101602 | Sales (CO) | V | 001 | YB30 | A000 | CO |
| 48101801 | Other Inc.&Expense (CO) | W | 001 | YB40 | A000 | CO |
| 48101750 | Build. & Maintenance (CO) | H | 001 | YB40 | A000 | CO |
| 48101201 | Purch & Stores 1 (CO) | G | 001 | YB20 | A000 | CO |
| 48101202 | Purch & Stores 2 (CO) | G | 001 | YB20 | A000 | CO |
| 48101902 | Consulting Unit A (CO) | C | 001 | YB25 | A000 | CO |
| 48101301 | Manufacturing 1 (CO) | F | 001 | YB20 | A000 | CO |
| 48101302 | Manufacturing 2 (CO) | F | 001 | YB20 | A000 | CO |
| 48101401 | QM (CO) | H | 001 | YB40 | A000 | CO |
| 48101501 | R&D (CO) | E | 001 | YB50 | A000 | CO |
| 48101701 | Plant & Maintenance (CO) | H | 001 | YB40 | A000 | CO |
| 48101321 | Services/Consulting (CO) | F | 001 | YB20 | A000 | CO |
| 48101751 | HR Services (CO) | W | 001 | YB40 | A000 | CO |
| 48101752 | HR Recruitment (CO) | W | 001 | YB40 | A000 | CO |
| 48101753 | IT Services (CO) | W | 001 | YB40 | A000 | CO |
| 48101901 | Back Office (CO) | H | 001 | YB30 | A000 | CO |
| 48101903 | Consulting Unit B (CO) | C | 001 | YB25 | A000 | CO |
| 48101904 | Customer Development (CO) | C | 001 | YB25 | A000 | CO |
| 20101101 | Financials (CZ) | W | 001 | YB40 | A000 | CZ |
| 20101601 | Marketing (CZ) | 9 | 001 | YB35 | A000 | CZ |
| 20101602 | Sales (CZ) | V | 001 | YB30 | A000 | CZ |
| 20101801 | Other Inc.&Expense (CZ) | W | 001 | YB40 | A000 | CZ |
| 20101750 | Build. & Maintenance (CZ) | H | 001 | YB40 | A000 | CZ |
| 20101201 | Purch & Stores 1 (CZ) | G | 001 | YB20 | A000 | CZ |
| 20101202 | Purch & Stores 2 (CZ) | G | 001 | YB20 | A000 | CZ |
| 20101902 | Consulting Unit A (CZ) | C | 001 | YB25 | A000 | CZ |
| 20101301 | Manufacturing 1 (CZ) | F | 001 | YB20 | A000 | CZ |
| 20101302 | Manufacturing 2 (CZ) | F | 001 | YB20 | A000 | CZ |
| 20101401 | QM (CZ) | H | 001 | YB40 | A000 | CZ |
| 20101501 | R&D (CZ) | E | 001 | YB50 | A000 | CZ |
| 20101701 | Plant & Maintenance (CZ) | H | 001 | YB40 | A000 | CZ |
| 20101321 | Services/Consulting (CZ) | F | 001 | YB20 | A000 | CZ |
| 20101751 | HR Services (CZ) | W | 001 | YB40 | A000 | CZ |
| 20101752 | HR Recruitment (CZ) | W | 001 | YB40 | A000 | CZ |
| 20101753 | IT Services (CZ) | W | 001 | YB40 | A000 | CZ |
| 20101901 | Back Office (CZ) | H | 001 | YB30 | A000 | CZ |
| 20101903 | Consulting Unit B (CZ) | C | 001 | YB25 | A000 | CZ |
| 20101904 | Customer Development (CZ) | C | 001 | YB25 | A000 | CZ |
| 32101101 | Financials (DK) | W | 001 | YB40 | A000 | DK |
| 32101601 | Marketing (DK) | 9 | 001 | YB35 | A000 | DK |
| 32101602 | Sales (DK) | V | 001 | YB30 | A000 | DK |
| 32101801 | Other Inc.&Expense (DK) | W | 001 | YB40 | A000 | DK |
| 32101750 | Build. & Maintenance (DK) | H | 001 | YB40 | A000 | DK |
| 32101201 | Purch & Stores 1 (DK) | G | 001 | YB20 | A000 | DK |
| 32101202 | Purch & Stores 2 (DK) | G | 001 | YB20 | A000 | DK |
| 32101902 | Consulting Unit A (DK) | C | 001 | YB25 | A000 | DK |
| 32101301 | Manufacturing 1 (DK) | F | 001 | YB20 | A000 | DK |
| 32101302 | Manufacturing 2 (DK) | F | 001 | YB20 | A000 | DK |
| 32101401 | QM (DK) | H | 001 | YB40 | A000 | DK |
| 32101501 | R&D (DK) | E | 001 | YB50 | A000 | DK |
| 32101701 | Plant & Maintenance (DK) | H | 001 | YB40 | A000 | DK |
| 32101321 | Services/Consulting (DK) | F | 001 | YB20 | A000 | DK |
| 32101751 | HR Services-(DK) | W | 001 | YB40 | A000 | DK |
| 32101752 | HR Recruitment-(DK) | W | 001 | YB40 | A000 | DK |
| 32101753 | IT Services-(DK) | W | 001 | YB40 | A000 | DK |
| 32101901 | Back Office-(DK) | H | 001 | YB30 | A000 | DK |
| 32101903 | Consulting Unit B-(DK) | C | 001 | YB25 | A000 | DK |
| 32101904 | Customer Development-(DK) | C | 001 | YB25 | A000 | DK |
| 73101101 | Financials (EG) | W | 001 | YB40 | A000 | EG |
| 73101601 | Marketing (EG) | 9 | 001 | YB35 | A000 | EG |
| 73101602 | Sales (EG) | V | 001 | YB30 | A000 | EG |
| 73101801 | Other Inc.&Expense (EG) | W | 001 | YB40 | A000 | EG |
| 73101750 | Build. & Maintenance (EG) | H | 001 | YB40 | A000 | EG |
| 73101201 | Purch & Stores 1 (EG) | G | 001 | YB20 | A000 | EG |
| 73101202 | Purch & Stores 2 (EG) | G | 001 | YB20 | A000 | EG |
| 73101902 | Consulting Unit A (EG) | C | 001 | YB25 | A000 | EG |
| 73101301 | Manufacturing 1 (EG) | F | 001 | YB20 | A000 | EG |
| 73101302 | Manufacturing 2 (EG) | F | 001 | YB20 | A000 | EG |
| 73101401 | QM (EG) | H | 001 | YB40 | A000 | EG |
| 73101501 | R&D (EG) | E | 001 | YB50 | A000 | EG |
| 73101701 | Plant & Maintenance (EG) | H | 001 | YB40 | A000 | EG |
| 73101321 | Services/Consulting (EG) | F | 001 | YB20 | A000 | EG |
| 73101751 | HR Services (EG) | W | 001 | YB40 | A000 | EG |
| 73101752 | HR Recruitment (EG) | W | 001 | YB40 | A000 | EG |
| 73101753 | IT Services (EG) | W | 001 | YB40 | A000 | EG |
| 73101901 | Back Office (EG) | H | 001 | YB30 | A000 | EG |
| 73101903 | Consulting Unit B (EG) | C | 001 | YB25 | A000 | EG |
| 73101904 | Customer Development (EG) | C | 001 | YB25 | A000 | EG |
| 24101101 | Financials (ES) | W | 001 | YB40 | A000 | ES |
| 24101601 | Marketing (ES) | 9 | 001 | YB35 | A000 | ES |
| 24101602 | Sales (ES) | V | 001 | YB30 | A000 | ES |
| 24101801 | Other Inc.&Expense (ES) | W | 001 | YB40 | A000 | ES |
| 24101750 | Build. & Maintenance (ES) | H | 001 | YB40 | A000 | ES |
| 24101201 | Purch & Stores 1 (ES) | G | 001 | YB20 | A000 | ES |
| 24101202 | Purch & Stores 2 (ES) | G | 001 | YB20 | A000 | ES |
| 24101902 | Consulting Unit A (ES) | C | 001 | YB25 | A000 | ES |
| 24101301 | Manufacturing 1 (ES) | F | 001 | YB20 | A000 | ES |
| 24101302 | Manufacturing 2 (ES) | F | 001 | YB20 | A000 | ES |
| 24101401 | QM (ES) | H | 001 | YB40 | A000 | ES |
| 24101501 | R&D (ES) | E | 001 | YB50 | A000 | ES |
| 24101701 | Plant & Maintenance (ES) | H | 001 | YB40 | A000 | ES |
| 24101321 | Services/Consulting (ES) | F | 001 | YB20 | A000 | ES |
| 24101751 | HR Services-(ES) | W | 001 | YB40 | A000 | ES |
| 24101752 | HR Recruitment-(ES) | W | 001 | YB40 | A000 | ES |
| 24101753 | IT Services-(ES) | W | 001 | YB40 | A000 | ES |
| 24101901 | Back Office-(ES) | H | 001 | YB30 | A000 | ES |
| 24101903 | Consulting Unit B-(ES) | C | 001 | YB25 | A000 | ES |
| 24101904 | Customer Development-(ES) | C | 001 | YB25 | A000 | ES |
| 45101101 | Financials (FI) | W | 001 | YB40 | A000 | FI |
| 45101601 | Marketing (FI) | 9 | 001 | YB35 | A000 | FI |
| 45101602 | Sales (FI) | V | 001 | YB30 | A000 | FI |
| 45101801 | Other Inc.&Expense (FI) | W | 001 | YB40 | A000 | FI |
| 45101750 | Build. & Maintenance (FI) | H | 001 | YB40 | A000 | FI |
| 45101201 | Purch & Stores 1 (FI) | G | 001 | YB20 | A000 | FI |
| 45101202 | Purch & Stores 2 (FI) | G | 001 | YB20 | A000 | FI |
| 45101902 | Consulting Unit A (FI) | C | 001 | YB25 | A000 | FI |
| 45101301 | Manufacturing 1 (FI) | F | 001 | YB20 | A000 | FI |
| 45101302 | Manufacturing 2 (FI) | F | 001 | YB20 | A000 | FI |
| 45101401 | QM (FI) | H | 001 | YB40 | A000 | FI |
| 45101501 | R&D (FI) | E | 001 | YB50 | A000 | FI |
| 45101701 | Plant & Maintenance (FI) | H | 001 | YB40 | A000 | FI |
| 45101321 | Services/Consulting (FI) | F | 001 | YB20 | A000 | FI |
| 45101751 | HR Services-(FI) | W | 001 | YB40 | A000 | FI |
| 45101752 | HR Recruitment-(FI) | W | 001 | YB40 | A000 | FI |
| 45101753 | IT Services-(FI) | W | 001 | YB40 | A000 | FI |
| 45101901 | Back Office-(FI) | H | 001 | YB30 | A000 | FI |
| 45101903 | Consulting Unit B-(FI) | C | 001 | YB25 | A000 | FI |
| 45101904 | Customer Development-(FI) | C | 001 | YB25 | A000 | FI |
| 12101101 | Financials (FR) | W | 001 | YB40 | A000 | FR |
| 12101601 | Marketing (FR) | 9 | 001 | YB35 | A000 | FR |
| 12101602 | Sales (FR) | V | 001 | YB30 | A000 | FR |
| 12101801 | Other Inc.&Expense (FR) | W | 001 | YB40 | A000 | FR |
| 12101750 | Build. & Maintenance (FR) | H | 001 | YB40 | A000 | FR |
| 12101201 | Purch & Stores 1 (FR) | G | 001 | YB20 | A000 | FR |
| 12101202 | Purch & Stores 2 (FR) | G | 001 | YB20 | A000 | FR |
| 12101902 | Consulting Unit A (FR) | C | 001 | YB25 | A000 | FR |
| 12101301 | Manufacturing 1 (FR) | F | 001 | YB20 | A000 | FR |
| 12101302 | Manufacturing 2 (FR) | F | 001 | YB20 | A000 | FR |
| 12101401 | QM (FR) | H | 001 | YB40 | A000 | FR |
| 12101501 | R&D (FR) | E | 001 | YB50 | A000 | FR |
| 12101701 | Plant & Maintenance (FR) | H | 001 | YB40 | A000 | FR |
| 12101321 | Services/Consulting (FR) | F | 001 | YB20 | A000 | FR |
| 12101751 | HR Services-(FR) | W | 001 | YB40 | A000 | FR |
| 12101752 | HR Recruitment-(FR) | W | 001 | YB40 | A000 | FR |
| 12101753 | IT Services-(FR) | W | 001 | YB40 | A000 | FR |
| 12101901 | Back Office-(FR) | H | 001 | YB30 | A000 | FR |
| 12101903 | Consulting Unit B-(FR) | C | 001 | YB25 | A000 | FR |
| 12101904 | Customer Development-(FR) | C | 001 | YB25 | A000 | FR |
| 11101101 | Financials (GB) | W | 001 | YB40 | A000 | GB |
| 11101601 | Marketing (GB) | 9 | 001 | YB35 | A000 | GB |
| 11101602 | Sales (GB) | V | 001 | YB30 | A000 | GB |
| 11101801 | Other Inc.&Expense (GB) | W | 001 | YB40 | A000 | GB |
| 11101750 | Build. & Maintenance (GB) | H | 001 | YB40 | A000 | GB |
| 11101201 | Purch & Stores 1 (GB) | G | 001 | YB20 | A000 | GB |
| 11101202 | Purch & Stores 2 (GB) | G | 001 | YB20 | A000 | GB |
| 11101902 | Consulting Unit A (GB) | C | 001 | YB25 | A000 | GB |
| 11101301 | Manufacturing 1 (GB) | F | 001 | YB20 | A000 | GB |
| 11101302 | Manufacturing 2 (GB) | F | 001 | YB20 | A000 | GB |
| 11101401 | QM (GB) | H | 001 | YB40 | A000 | GB |
| 11101501 | R&D (GB) | E | 001 | YB50 | A000 | GB |
| 11101701 | Plant & Maintenance (GB) | H | 001 | YB40 | A000 | GB |
| 11101321 | Services/Consulting (GB) | F | 001 | YB20 | A000 | GB |
| 11101751 | HR Services (GB) | W | 001 | YB40 | A000 | GB |
| 11101752 | HR Recruitment (GB) | W | 001 | YB40 | A000 | GB |
| 11101753 | IT Services (GB) | W | 001 | YB40 | A000 | GB |
| 11101901 | Back Office (GB) | H | 001 | YB30 | A000 | GB |
| 11101903 | Consulting Unit B (GB) | C | 001 | YB25 | A000 | GB |
| 11101904 | Customer Development (GB) | C | 001 | YB25 | A000 | GB |
| 34101101 | Financials (GR) | W | 001 | YB40 | A000 | GR |
| 34101601 | Marketing (GR) | 9 | 001 | YB35 | A000 | GR |
| 34101602 | Sales (GR) | V | 001 | YB30 | A000 | GR |
| 34101801 | Other Inc.&Expense (GR) | W | 001 | YB40 | A000 | GR |
| 34101950 | Build. & Maintenance (GR) | H | 001 | YB40 | A000 | GR |
| 34101201 | Purch & Stores 1 (GR) | G | 001 | YB20 | A000 | GR |
| 34101202 | Purch & Stores 2 (GR) | G | 001 | YB20 | A000 | GR |
| 34101902 | Consulting Unit A (GR) | C | 001 | YB25 | A000 | GR |
| 34101301 | Manufacturing 1 (GR) | F | 001 | YB20 | A000 | GR |
| 34101302 | Manufacturing 2 (GR) | F | 001 | YB20 | A000 | GR |
| 34101401 | QM (GR) | H | 001 | YB40 | A000 | GR |
| 34101501 | R&D (GR) | E | 001 | YB50 | A000 | GR |
| 34101701 | Plant & Maintenance (GR) | H | 001 | YB40 | A000 | GR |
| 34101321 | Services/Consulting (GR) | F | 001 | YB20 | A000 | GR |
| 34101951 | HR Services (GR) | W | 001 | YB40 | A000 | GR |
| 34101952 | HR Recruitment (GR) | W | 001 | YB40 | A000 | GR |
| 34101953 | IT Services (GR) | W | 001 | YB40 | A000 | GR |
| 34101901 | Back Office (GR) | H | 001 | YB30 | A000 | GR |
| 34101903 | Consulting Unit B (GR) | C | 001 | YB25 | A000 | GR |
| 34101904 | Customer Development (GR) | C | 001 | YB25 | A000 | GR |
| 62101101 | Financials (HK) | W | 001 | YB40 | A000 | HK |
| 62101601 | Marketing (HK) | 9 | 001 | YB35 | A000 | HK |
| 62101602 | Sales (HK) | V | 001 | YB30 | A000 | HK |
| 62101801 | Other Inc.&Expense (HK) | W | 001 | YB40 | A000 | HK |
| 62101750 | Build. & Maintenance (HK) | H | 001 | YB40 | A000 | HK |
| 62101201 | Purch & Stores 1 (HK) | G | 001 | YB20 | A000 | HK |
| 62101202 | Purch & Stores 2 (HK) | G | 001 | YB20 | A000 | HK |
| 62101902 | Consulting Unit A (HK) | C | 001 | YB25 | A000 | HK |
| 62101301 | Manufacturing 1 (HK) | F | 001 | YB20 | A000 | HK |
| 62101302 | Manufacturing 2 (HK) | F | 001 | YB20 | A000 | HK |
| 62101401 | QM (HK) | H | 001 | YB40 | A000 | HK |
| 62101501 | R&D (HK) | E | 001 | YB50 | A000 | HK |
| 62101701 | Plant & Maintenance (HK) | H | 001 | YB40 | A000 | HK |
| 62101321 | Services/Consulting (HK) | F | 001 | YB20 | A000 | HK |
| 62101751 | HR Services-(HK) | W | 001 | YB40 | A000 | HK |
| 62101752 | HR Recruitment-(HK) | W | 001 | YB40 | A000 | HK |
| 62101753 | IT Services-(HK) | W | 001 | YB40 | A000 | HK |
| 62101901 | Back Office-(HK) | H | 001 | YB30 | A000 | HK |
| 62101903 | Consulting Unit B-(HK) | C | 001 | YB25 | A000 | HK |
| 62101904 | Customer Development-(HK) | C | 001 | YB25 | A000 | HK |
| 40101101 | Financials (HR) | W | 001 | YB40 | A000 | HR |
| 40101601 | Marketing (HR) | 9 | 001 | YB35 | A000 | HR |
| 40101602 | Sales (HR) | V | 001 | YB30 | A000 | HR |
| 40101801 | Other Inc.&Expense (HR) | W | 001 | YB40 | A000 | HR |
| 40101750 | Build. & Maintenance (HR) | H | 001 | YB40 | A000 | HR |
| 40101201 | Purch & Stores 1 (HR) | G | 001 | YB20 | A000 | HR |
| 40101202 | Purch & Stores 2 (HR) | G | 001 | YB20 | A000 | HR |
| 40101902 | Consulting Unit A (HR) | C | 001 | YB25 | A000 | HR |
| 40101301 | Manufacturing 1 (HR) | F | 001 | YB20 | A000 | HR |
| 40101302 | Manufacturing 2 (HR) | F | 001 | YB20 | A000 | HR |
| 40101401 | QM (HR) | H | 001 | YB40 | A000 | HR |
| 40101501 | R&D (HR) | E | 001 | YB50 | A000 | HR |
| 40101701 | Plant & Maintenance (HR) | H | 001 | YB40 | A000 | HR |
| 40101321 | Services/Consulting (HR) | F | 001 | YB20 | A000 | HR |
| 40101751 | HR Services (HR) | W | 001 | YB40 | A000 | HR |
| 40101752 | HR Recruitment (HR) | W | 001 | YB40 | A000 | HR |
| 40101753 | IT Services (HR) | W | 001 | YB40 | A000 | HR |
| 40101901 | Back Office (HR) | H | 001 | YB30 | A000 | HR |
| 40101903 | Consulting Unit B (HR) | C | 001 | YB25 | A000 | HR |
| 40101904 | Customer Development (HR) | C | 001 | YB25 | A000 | HR |
| 21101101 | Financials (HU) | W | 001 | YB40 | A000 | HU |
| 21101601 | Marketing (HU) | 9 | 001 | YB35 | A000 | HU |
| 21101602 | Sales (HU) | V | 001 | YB30 | A000 | HU |
| 21101801 | Other Inc.&Expense (HU) | W | 001 | YB40 | A000 | HU |
| 21101750 | Build. & Maintenance (HU) | H | 001 | YB40 | A000 | HU |
| 21101201 | Purch & Stores 1 (HU) | G | 001 | YB20 | A000 | HU |
| 21101202 | Purch & Stores 2 (HU) | G | 001 | YB20 | A000 | HU |
| 21101902 | Consulting Unit A (HU) | C | 001 | YB25 | A000 | HU |
| 21101301 | Manufacturing 1 (HU) | F | 001 | YB20 | A000 | HU |
| 21101302 | Manufacturing 2 (HU) | F | 001 | YB20 | A000 | HU |
| 21101401 | QM (HU) | H | 001 | YB40 | A000 | HU |
| 21101501 | R&D (HU) | E | 001 | YB50 | A000 | HU |
| 21101701 | Plant & Maintenance (HU) | H | 001 | YB40 | A000 | HU |
| 21101321 | Services/Consulting (HU) | F | 001 | YB20 | A000 | HU |
| 21101751 | HR Services-(HU) | W | 001 | YB40 | A000 | HU |
| 21101752 | HR Recruitment-(HU) | W | 001 | YB40 | A000 | HU |
| 21101753 | IT Services-(HU) | W | 001 | YB40 | A000 | HU |
| 21101901 | Back Office-(HU) | H | 001 | YB30 | A000 | HU |
| 21101903 | Consulting Unit B-(HU) | C | 001 | YB25 | A000 | HU |
| 21101904 | Customer Development-(HU) | C | 001 | YB25 | A000 | HU |
| 51101101 | Financials (ID) | W | 001 | YB40 | A000 | ID |
| 51101601 | Marketing (ID) | 9 | 001 | YB35 | A000 | ID |
| 51101602 | Sales (ID) | V | 001 | YB30 | A000 | ID |
| 51101801 | Other Inc.&Expense (ID) | W | 001 | YB40 | A000 | ID |
| 51101750 | Build. & Maintenance (ID) | H | 001 | YB40 | A000 | ID |
| 51101201 | Purch & Stores 1 (ID) | G | 001 | YB20 | A000 | ID |
| 51101202 | Purch & Stores 2 (ID) | G | 001 | YB20 | A000 | ID |
| 51101902 | Consulting Unit A (ID) | C | 001 | YB25 | A000 | ID |
| 51101301 | Manufacturing 1 (ID) | F | 001 | YB20 | A000 | ID |
| 51101302 | Manufacturing 2 (ID) | F | 001 | YB20 | A000 | ID |
| 51101401 | QM (ID) | H | 001 | YB40 | A000 | ID |
| 51101501 | R&D (ID) | E | 001 | YB50 | A000 | ID |
| 51101701 | Plant & Maintenance (ID) | H | 001 | YB40 | A000 | ID |
| 51101321 | Services/Consulting (ID) | F | 001 | YB20 | A000 | ID |
| 51101751 | HR Services (ID) | W | 001 | YB40 | A000 | ID |
| 51101752 | HR Recruitment (ID) | W | 001 | YB40 | A000 | ID |
| 51101753 | IT Services (ID) | W | 001 | YB40 | A000 | ID |
| 51101901 | Back Office (ID) | H | 001 | YB30 | A000 | ID |
| 51101903 | Consulting Unit B (ID) | C | 001 | YB25 | A000 | ID |
| 51101904 | Customer Development (ID) | C | 001 | YB25 | A000 | ID |
| 42101101 | Financials (IE) | W | 001 | YB40 | A000 | IE |
| 42101601 | Marketing (IE) | 9 | 001 | YB35 | A000 | IE |
| 42101602 | Sales (IE) | V | 001 | YB30 | A000 | IE |
| 42101801 | Other Inc.&Expense (IE) | W | 001 | YB40 | A000 | IE |
| 42101750 | Build. & Maintenance (IE) | H | 001 | YB40 | A000 | IE |
| 42101201 | Purch & Stores 1 (IE) | G | 001 | YB20 | A000 | IE |
| 42101202 | Purch & Stores 2 (IE) | G | 001 | YB20 | A000 | IE |
| 42101902 | Consulting Unit A (IE) | C | 001 | YB25 | A000 | IE |
| 42101301 | Manufacturing 1 (IE) | F | 001 | YB20 | A000 | IE |
| 42101302 | Manufacturing 2 (IE) | F | 001 | YB20 | A000 | IE |
| 42101401 | QM (IE) | H | 001 | YB40 | A000 | IE |
| 42101501 | R&D (IE) | E | 001 | YB50 | A000 | IE |
| 42101701 | Plant & Maintenance (IE) | H | 001 | YB40 | A000 | IE |
| 42101321 | Services/Consulting (IE) | F | 001 | YB20 | A000 | IE |
| 42101751 | HR Services (IE) | W | 001 | YB40 | A000 | IE |
| 42101752 | HR Recruitment (IE) | W | 001 | YB40 | A000 | IE |
| 42101753 | IT Services (IE) | W | 001 | YB40 | A000 | IE |
| 42101901 | Back Office (IE) | H | 001 | YB30 | A000 | IE |
| 42101903 | Consulting Unit B (IE) | C | 001 | YB25 | A000 | IE |
| 42101904 | Customer Development (IE) | C | 001 | YB25 | A000 | IE |
| 47101101 | Financials (IL) | W | 001 | YB40 | A000 | IL |
| 47101601 | Marketing (IL) | 9 | 001 | YB35 | A000 | IL |
| 47101602 | Sales (IL) | V | 001 | YB30 | A000 | IL |
| 47101801 | Other Inc.&Expense (IL) | W | 001 | YB40 | A000 | IL |
| 47101950 | Build. & Maintenance (IL) | H | 001 | YB40 | A000 | IL |
| 47101201 | Purch & Stores 1 (IL) | G | 001 | YB20 | A000 | IL |
| 47101202 | Purch & Stores 2 (IL) | G | 001 | YB20 | A000 | IL |
| 47101902 | Consulting Unit A (IL) | C | 001 | YB25 | A000 | IL |
| 47101301 | Manufacturing 1 (IL) | F | 001 | YB20 | A000 | IL |
| 47101302 | Manufacturing 2 (IL) | F | 001 | YB20 | A000 | IL |
| 47101401 | QM (IL) | H | 001 | YB40 | A000 | IL |
| 47101501 | R&D (IL) | E | 001 | YB50 | A000 | IL |
| 47101701 | Plant & Maintenance (IL) | H | 001 | YB40 | A000 | IL |
| 47101321 | Services/Consulting (IL) | F | 001 | YB20 | A000 | IL |
| 47101951 | HR Services (IL) | W | 001 | YB40 | A000 | IL |
| 47101952 | HR Recruitment (IL) | W | 001 | YB40 | A000 | IL |
| 47101953 | IT Services (IL) | W | 001 | YB40 | A000 | IL |
| 47101901 | Back Office (IL) | H | 001 | YB30 | A000 | IL |
| 47101903 | Consulting Unit B (IL) | C | 001 | YB25 | A000 | IL |
| 47101904 | Customer Development (IL) | C | 001 | YB25 | A000 | IL |
| 18101101 | Financials (IN) | W | 001 | YB40 | A000 | IN |
| 18101601 | Marketing (IN) | 9 | 001 | YB35 | A000 | IN |
| 18101602 | Sales (IN) | V | 001 | YB30 | A000 | IN |
| 18101801 | Other Inc.&Expense (IN) | W | 001 | YB40 | A000 | IN |
| 18101750 | Build. & Maintenance (IN) | H | 001 | YB40 | A000 | IN |
| 18101201 | Purch & Stores 1 (IN) | G | 001 | YB20 | A000 | IN |
| 18101202 | Purch & Stores 2 (IN) | G | 001 | YB20 | A000 | IN |
| 18101902 | Consulting Unit A (IN) | C | 001 | YB25 | A000 | IN |
| 18101301 | Manufacturing 1 (IN) | F | 001 | YB20 | A000 | IN |
| 18101302 | Manufacturing 2 (IN) | F | 001 | YB20 | A000 | IN |
| 18101401 | QM (IN) | H | 001 | YB40 | A000 | IN |
| 18101501 | R&D (IN) | E | 001 | YB50 | A000 | IN |
| 18101701 | Plant & Maintenance (IN) | H | 001 | YB40 | A000 | IN |
| 18101321 | Services/Consulting (IN) | F | 001 | YB20 | A000 | IN |
| 18101751 | HR Services-(IN) | W | 001 | YB40 | A000 | IN |
| 18101752 | HR Recruitment-(IN) | W | 001 | YB40 | A000 | IN |
| 18101753 | IT Services-(IN) | W | 001 | YB40 | A000 | IN |
| 18101901 | Back Office-(IN) | H | 001 | YB30 | A000 | IN |
| 18101903 | Consulting Unit B-(IN) | C | 001 | YB25 | A000 | IN |
| 18101904 | Customer Development-(IN) | C | 001 | YB25 | A000 | IN |
| 23101101 | Financials (IT) | W | 001 | YB40 | A000 | IT |
| 23101601 | Marketing (IT) | 9 | 001 | YB35 | A000 | IT |
| 23101602 | Sales (IT) | V | 001 | YB30 | A000 | IT |
| 23101801 | Other Inc.&Expense (IT) | W | 001 | YB40 | A000 | IT |
| 23101750 | Build. & Maintenance (IT) | H | 001 | YB40 | A000 | IT |
| 23101201 | Purch & Stores 1 (IT) | G | 001 | YB20 | A000 | IT |
| 23101202 | Purch & Stores 2 (IT) | G | 001 | YB20 | A000 | IT |
| 23101902 | Consulting Unit A (IT) | C | 001 | YB25 | A000 | IT |
| 23101301 | Manufacturing 1 (IT) | F | 001 | YB20 | A000 | IT |
| 23101302 | Manufacturing 2 (IT) | F | 001 | YB20 | A000 | IT |
| 23101401 | QM (IT) | H | 001 | YB40 | A000 | IT |
| 23101501 | R&D (IT) | E | 001 | YB50 | A000 | IT |
| 23101701 | Plant & Maintenance (IT) | H | 001 | YB40 | A000 | IT |
| 23101321 | Services/Consulting (IT) | F | 001 | YB20 | A000 | IT |
| 23101751 | HR Services-(IT) | W | 001 | YB40 | A000 | IT |
| 23101752 | HR Recruitment-(IT) | W | 001 | YB40 | A000 | IT |
| 23101753 | IT Services-(IT) | W | 001 | YB40 | A000 | IT |
| 23101901 | Back Office-(IT) | H | 001 | YB30 | A000 | IT |
| 23101903 | Consulting Unit B-(IT) | C | 001 | YB25 | A000 | IT |
| 23101904 | Customer Development-(IT) | C | 001 | YB25 | A000 | IT |
| 15101101 | Financials (JP) | W | 001 | YB40 | A000 | JP |
| 15101601 | Marketing (JP) | 9 | 001 | YB35 | A000 | JP |
| 15101602 | Sales (JP) | V | 001 | YB30 | A000 | JP |
| 15101801 | Other Inc.&Expense (JP) | W | 001 | YB40 | A000 | JP |
| 15101750 | Build. & Maintenance (JP) | H | 001 | YB40 | A000 | JP |
| 15101201 | Purch & Stores 1 (JP) | G | 001 | YB20 | A000 | JP |
| 15101202 | Purch & Stores 2 (JP) | G | 001 | YB20 | A000 | JP |
| 15101902 | Consulting Unit A (JP) | C | 001 | YB25 | A000 | JP |
| 15101301 | Manufacturing 1 (JP) | F | 001 | YB20 | A000 | JP |
| 15101302 | Manufacturing 2 (JP) | F | 001 | YB20 | A000 | JP |
| 15101401 | QM (JP) | H | 001 | YB40 | A000 | JP |
| 15101501 | R&D (JP) | E | 001 | YB50 | A000 | JP |
| 15101701 | Plant & Maintenance (JP) | H | 001 | YB40 | A000 | JP |
| 15101321 | Services/Consulting (JP) | F | 001 | YB20 | A000 | JP |
| 15101751 | HR Services (JP) | W | 001 | YB40 | A000 | JP |
| 15101752 | HR Recruitment (JP) | W | 001 | YB40 | A000 | JP |
| 15101753 | IT Services (JP) | W | 001 | YB40 | A000 | JP |
| 15101901 | Back Office (JP) | H | 001 | YB30 | A000 | JP |
| 15101903 | Consulting Unit B (JP) | C | 001 | YB25 | A000 | JP |
| 15101904 | Customer Development (JP) | C | 001 | YB25 | A000 | JP |
| 43101101 | Financials (KR) | W | 001 | YB40 | A000 | KR |
| 43101601 | Marketing (KR) | 9 | 001 | YB35 | A000 | KR |
| 43101602 | Sales (KR) | V | 001 | YB30 | A000 | KR |
| 43101801 | Other Inc.&Expense (KR) | W | 001 | YB40 | A000 | KR |
| 43101750 | Build. & Maintenance (KR) | H | 001 | YB40 | A000 | KR |
| 43101201 | Purch & Stores 1 (KR) | G | 001 | YB20 | A000 | KR |
| 43101202 | Purch & Stores 2 (KR) | G | 001 | YB20 | A000 | KR |
| 43101902 | Consulting Unit A (KR) | C | 001 | YB25 | A000 | KR |
| 43101301 | Manufacturing 1 (KR) | F | 001 | YB20 | A000 | KR |
| 43101302 | Manufacturing 2 (KR) | F | 001 | YB20 | A000 | KR |
| 43101401 | QM (KR) | H | 001 | YB40 | A000 | KR |
| 43101501 | R&D (KR) | E | 001 | YB50 | A000 | KR |
| 43101701 | Plant & Maintenance (KR) | H | 001 | YB40 | A000 | KR |
| 43101321 | Services/Consulting (KR) | F | 001 | YB20 | A000 | KR |
| 43101751 | HR Services (KR) | W | 001 | YB40 | A000 | KR |
| 43101752 | HR Recruitment (KR) | W | 001 | YB40 | A000 | KR |
| 43101753 | IT Services (KR) | W | 001 | YB40 | A000 | KR |
| 43101901 | Back Office (KR) | H | 001 | YB30 | A000 | KR |
| 43101903 | Consulting Unit B (KR) | C | 001 | YB25 | A000 | KR |
| 43101904 | Customer Development (KR) | C | 001 | YB25 | A000 | KR |
| 74101101 | Financials (KW) | W | 001 | YB40 | A000 | KW |
| 74101601 | Marketing (KW) | 9 | 001 | YB35 | A000 | KW |
| 74101602 | Sales (KW) | V | 001 | YB30 | A000 | KW |
| 74101801 | Other Inc.&Expense (KW) | W | 001 | YB40 | A000 | KW |
| 74101750 | Build. & Maintenance (KW) | H | 001 | YB40 | A000 | KW |
| 74101201 | Purch & Stores 1 (KW) | G | 001 | YB20 | A000 | KW |
| 74101202 | Purch & Stores 2 (KW) | G | 001 | YB20 | A000 | KW |
| 74101902 | Consulting Unit A (KW) | C | 001 | YB25 | A000 | KW |
| 74101301 | Manufacturing 1 (KW) | F | 001 | YB20 | A000 | KW |
| 74101302 | Manufacturing 2 (KW) | F | 001 | YB20 | A000 | KW |
| 74101401 | QM (KW) | H | 001 | YB40 | A000 | KW |
| 74101501 | R&D (KW) | E | 001 | YB50 | A000 | KW |
| 74101701 | Plant & Maintenance (KW) | H | 001 | YB40 | A000 | KW |
| 74101321 | Services/Consulting (KW) | F | 001 | YB20 | A000 | KW |
| 74101751 | HR Services (KW) | W | 001 | YB40 | A000 | KW |
| 74101752 | HR Recruitment (KW) | W | 001 | YB40 | A000 | KW |
| 74101753 | IT Services (KW) | W | 001 | YB40 | A000 | KW |
| 74101901 | Back Office (KW) | H | 001 | YB30 | A000 | KW |
| 74101903 | Consulting Unit B (KW) | C | 001 | YB25 | A000 | KW |
| 74101904 | Customer Development (KW) | C | 001 | YB25 | A000 | KW |
| 94101101 | Financials (KZ) | W | 001 | YB40 | A000 | KZ |
| 94101601 | Marketing (KZ) | 9 | 001 | YB35 | A000 | KZ |
| 94101602 | Sales (KZ) | V | 001 | YB30 | A000 | KZ |
| 94101801 | Other Inc.&Expense (KZ) | W | 001 | YB40 | A000 | KZ |
| 94101750 | Build. & Maintenance (KZ) | H | 001 | YB40 | A000 | KZ |
| 94101201 | Purch & Stores 1 (KZ) | G | 001 | YB20 | A000 | KZ |
| 94101202 | Purch & Stores 2 (KZ) | G | 001 | YB20 | A000 | KZ |
| 94101902 | Consulting Unit A (KZ) | C | 001 | YB25 | A000 | KZ |
| 94101301 | Manufacturing 1 (KZ) | F | 001 | YB20 | A000 | KZ |
| 94101302 | Manufacturing 2 (KZ) | F | 001 | YB20 | A000 | KZ |
| 94101401 | QM (KZ) | H | 001 | YB40 | A000 | KZ |
| 94101501 | R&D (KZ) | E | 001 | YB50 | A000 | KZ |
| 94101701 | Plant & Maintenance (KZ) | H | 001 | YB40 | A000 | KZ |
| 94101321 | Services/Consulting (KZ) | F | 001 | YB20 | A000 | KZ |
| 94101751 | HR Services (KZ) | W | 001 | YB40 | A000 | KZ |
| 94101752 | HR Recruitment (KZ) | W | 001 | YB40 | A000 | KZ |
| 94101753 | IT Services (KZ) | W | 001 | YB40 | A000 | KZ |
| 94101901 | Back Office (KZ) | H | 001 | YB30 | A000 | KZ |
| 94101903 | Consulting Unit B (KZ) | C | 001 | YB25 | A000 | KZ |
| 94101904 | Customer Development (KZ) | C | 001 | YB25 | A000 | KZ |
| 007K101101 | Financials (LU) | W | 001 | YB40 | A000 | LU |
| 007K101601 | Marketing (LU) | 9 | 001 | YB35 | A000 | LU |
| 007K101602 | Sales (LU) | V | 001 | YB30 | A000 | LU |
| 007K101801 | Other Inc.&Expense (LU) | W | 001 | YB40 | A000 | LU |
| 007K101750 | Build. & Maintenance (LU) | H | 001 | YB40 | A000 | LU |
| 007K101201 | Purch & Stores 1 (LU) | G | 001 | YB20 | A000 | LU |
| 007K101202 | Purch & Stores 2 (LU) | G | 001 | YB20 | A000 | LU |
| 007K101902 | Consulting Unit A (LU) | C | 001 | YB25 | A000 | LU |
| 007K101301 | Manufacturing 1 (LU) | F | 001 | YB20 | A000 | LU |
| 007K101302 | Manufacturing 2 (LU) | F | 001 | YB20 | A000 | LU |
| 007K101401 | QM (LU) | H | 001 | YB40 | A000 | LU |
| 007K101501 | R&D (LU) | E | 001 | YB50 | A000 | LU |
| 007K101701 | Plant & Maintenance (LU) | H | 001 | YB40 | A000 | LU |
| 007K101321 | Services/Consulting (LU) | F | 001 | YB20 | A000 | LU |
| 007K101751 | HR Services (LU) | W | 001 | YB40 | A000 | LU |
| 007K101752 | HR Recruitment (LU) | W | 001 | YB40 | A000 | LU |
| 007K101753 | IT Services (LU) | W | 001 | YB40 | A000 | LU |
| 007K101901 | Back Office (LU) | H | 001 | YB30 | A000 | LU |
| 007K101903 | Consulting Unit B (LU) | C | 001 | YB25 | A000 | LU |
| 007K101904 | Customer Development (LU) | C | 001 | YB25 | A000 | LU |
| 55101101 | Financials (MX) | W | 001 | YB40 | A000 | MX |
| 55101601 | Marketing (MX) | 9 | 001 | YB35 | A000 | MX |
| 55101602 | Sales (MX) | V | 001 | YB30 | A000 | MX |
| 55101801 | Other Inc.&Expense (MX) | W | 001 | YB40 | A000 | MX |
| 55101750 | Build. & Maintenance (MX) | H | 001 | YB40 | A000 | MX |
| 55101201 | Purch & Stores 1 (MX) | G | 001 | YB20 | A000 | MX |
| 55101202 | Purch & Stores 2 (MX) | G | 001 | YB20 | A000 | MX |
| 55101902 | Consulting Unit A (MX) | C | 001 | YB25 | A000 | MX |
| 55101301 | Manufacturing 1 (MX) | F | 001 | YB20 | A000 | MX |
| 55101302 | Manufacturing 2 (MX) | F | 001 | YB20 | A000 | MX |
| 55101401 | QM (MX) | H | 001 | YB40 | A000 | MX |
| 55101501 | R&D (MX) | E | 001 | YB50 | A000 | MX |
| 55101701 | Plant & Maintenance (MX) | H | 001 | YB40 | A000 | MX |
| 55101321 | Services/Consulting (MX) | F | 001 | YB20 | A000 | MX |
| 55101751 | HR Services (MX) | W | 001 | YB40 | A000 | MX |
| 55101752 | HR Recruitment (MX) | W | 001 | YB40 | A000 | MX |
| 55101753 | IT Services (MX) | W | 001 | YB40 | A000 | MX |
| 55101901 | Back Office (MX) | H | 001 | YB30 | A000 | MX |
| 55101903 | Consulting Unit B (MX) | C | 001 | YB25 | A000 | MX |
| 55101904 | Customer Development (MX) | C | 001 | YB25 | A000 | MX |
| 54101101 | Financials (MY) | W | 001 | YB40 | A000 | MY |
| 54101601 | Marketing (MY) | 9 | 001 | YB35 | A000 | MY |
| 54101602 | Sales (MY) | V | 001 | YB30 | A000 | MY |
| 54101801 | Other Inc.&Expense (MY) | W | 001 | YB40 | A000 | MY |
| 54101750 | Build. & Maintenance (MY) | H | 001 | YB40 | A000 | MY |
| 54101201 | Purch & Stores 1 (MY) | G | 001 | YB20 | A000 | MY |
| 54101202 | Purch & Stores 2 (MY) | G | 001 | YB20 | A000 | MY |
| 54101902 | Consulting Unit A (MY) | C | 001 | YB25 | A000 | MY |
| 54101301 | Manufacturing 1 (MY) | F | 001 | YB20 | A000 | MY |
| 54101302 | Manufacturing 2 (MY) | F | 001 | YB20 | A000 | MY |
| 54101401 | QM (MY) | H | 001 | YB40 | A000 | MY |
| 54101501 | R&D (MY) | E | 001 | YB50 | A000 | MY |
| 54101701 | Plant & Maintenance (MY) | H | 001 | YB40 | A000 | MY |
| 54101321 | Services/Consulting (MY) | F | 001 | YB20 | A000 | MY |
| 54101751 | HR Services (MY) | W | 001 | YB40 | A000 | MY |
| 54101752 | HR Recruitment (MY) | W | 001 | YB40 | A000 | MY |
| 54101753 | IT Services (MY) | W | 001 | YB40 | A000 | MY |
| 54101901 | Back Office (MY) | H | 001 | YB30 | A000 | MY |
| 54101903 | Consulting Unit B (MY) | C | 001 | YB25 | A000 | MY |
| 54101904 | Customer Development (MY) | C | 001 | YB25 | A000 | MY |
| 37101101 | Financials (NL) | W | 001 | YB40 | A000 | NL |
| 37101601 | Marketing (NL) | 9 | 001 | YB35 | A000 | NL |
| 37101602 | Sales (NL) | V | 001 | YB30 | A000 | NL |
| 37101801 | Other Inc.&Expense (NL) | W | 001 | YB40 | A000 | NL |
| 37101750 | Build. & Maintenance (NL) | H | 001 | YB40 | A000 | NL |
| 37101201 | Purch & Stores 1 (NL) | G | 001 | YB20 | A000 | NL |
| 37101202 | Purch & Stores 2 (NL) | G | 001 | YB20 | A000 | NL |
| 37101902 | Consulting Unit A (NL) | C | 001 | YB25 | A000 | NL |
| 37101301 | Manufacturing 1 (NL) | F | 001 | YB20 | A000 | NL |
| 37101302 | Manufacturing 2 (NL) | F | 001 | YB20 | A000 | NL |
| 37101401 | QM (NL) | H | 001 | YB40 | A000 | NL |
| 37101501 | R&D (NL) | E | 001 | YB50 | A000 | NL |
| 37101701 | Plant & Maintenance (NL) | H | 001 | YB40 | A000 | NL |
| 37101321 | Services/Consulting (NL) | F | 001 | YB20 | A000 | NL |
| 37101751 | HR Services (NL) | W | 001 | YB40 | A000 | NL |
| 37101752 | HR Recruitment (NL) | W | 001 | YB40 | A000 | NL |
| 37101753 | IT Services (NL) | W | 001 | YB40 | A000 | NL |
| 37101901 | Back Office (NL) | H | 001 | YB30 | A000 | NL |
| 37101903 | Consulting Unit B (NL) | C | 001 | YB25 | A000 | NL |
| 37101904 | Customer Development (NL) | C | 001 | YB25 | A000 | NL |
| 44101101 | Financials (NO) | W | 001 | YB40 | A000 | NO |
| 44101601 | Marketing (NO) | 9 | 001 | YB35 | A000 | NO |
| 44101602 | Sales (NO) | V | 001 | YB30 | A000 | NO |
| 44101801 | Other Inc.&Expense (NO) | W | 001 | YB40 | A000 | NO |
| 44101750 | Build. & Maintenance (NO) | H | 001 | YB40 | A000 | NO |
| 44101201 | Purch & Stores 1 (NO) | G | 001 | YB20 | A000 | NO |
| 44101202 | Purch & Stores 2 (NO) | G | 001 | YB20 | A000 | NO |
| 44101902 | Consulting Unit A (NO) | C | 001 | YB25 | A000 | NO |
| 44101301 | Manufacturing 1 (NO) | F | 001 | YB20 | A000 | NO |
| 44101302 | Manufacturing 2 (NO) | F | 001 | YB20 | A000 | NO |
| 44101401 | QM (NO) | H | 001 | YB40 | A000 | NO |
| 44101501 | R&D (NO) | E | 001 | YB50 | A000 | NO |
| 44101701 | Plant & Maintenance (NO) | H | 001 | YB40 | A000 | NO |
| 44101321 | Services/Consulting (NO) | F | 001 | YB20 | A000 | NO |
| 44101751 | HR Services (NO) | W | 001 | YB40 | A000 | NO |
| 44101752 | HR Recruitment (NO) | W | 001 | YB40 | A000 | NO |
| 44101753 | IT Services (NO) | W | 001 | YB40 | A000 | NO |
| 44101901 | Back Office (NO) | H | 001 | YB30 | A000 | NO |
| 44101903 | Consulting Unit B (NO) | C | 001 | YB25 | A000 | NO |
| 44101904 | Customer Development (NO) | C | 001 | YB25 | A000 | NO |
| 69101101 | Financials (NZ) | W | 001 | YB40 | A000 | NZ |
| 69101601 | Marketing (NZ) | 9 | 001 | YB35 | A000 | NZ |
| 69101602 | Sales (NZ) | V | 001 | YB30 | A000 | NZ |
| 69101801 | Other Inc.&Expense (NZ) | W | 001 | YB40 | A000 | NZ |
| 69101750 | Build. & Maintenance (NZ) | H | 001 | YB40 | A000 | NZ |
| 69101201 | Purch & Stores 1 (NZ) | G | 001 | YB20 | A000 | NZ |
| 69101202 | Purch & Stores 2 (NZ) | G | 001 | YB20 | A000 | NZ |
| 69101902 | Consulting Unit A (NZ) | C | 001 | YB25 | A000 | NZ |
| 69101301 | Manufacturing 1 (NZ) | F | 001 | YB20 | A000 | NZ |
| 69101302 | Manufacturing 2 (NZ) | F | 001 | YB20 | A000 | NZ |
| 69101401 | QM (NZ) | H | 001 | YB40 | A000 | NZ |
| 69101501 | R&D (NZ) | E | 001 | YB50 | A000 | NZ |
| 69101701 | Plant & Maintenance (NZ) | H | 001 | YB40 | A000 | NZ |
| 69101321 | Services/Consulting (NZ) | F | 001 | YB20 | A000 | NZ |
| 69101751 | HR Services-(NZ) | W | 001 | YB40 | A000 | NZ |
| 69101752 | HR Recruitment-(NZ) | W | 001 | YB40 | A000 | NZ |
| 69101753 | IT Services-(NZ) | W | 001 | YB40 | A000 | NZ |
| 69101901 | Back Office-(NZ) | H | 001 | YB30 | A000 | NZ |
| 69101903 | Consulting Unit B-(NZ) | C | 001 | YB25 | A000 | NZ |
| 69101904 | Customer Development-(NZ) | C | 001 | YB25 | A000 | NZ |
| 007D101101 | Financials (OM) | W | 001 | YB40 | A000 | OM |
| 007D101601 | Marketing (OM) | 9 | 001 | YB35 | A000 | OM |
| 007D101602 | Sales (OM) | V | 001 | YB30 | A000 | OM |
| 007D101801 | Other Inc.&Expense (OM) | W | 001 | YB40 | A000 | OM |
| 007D101750 | Build. & Maintenance (OM) | H | 001 | YB40 | A000 | OM |
| 007D101201 | Purch & Stores 1 (OM) | G | 001 | YB20 | A000 | OM |
| 007D101202 | Purch & Stores 2 (OM) | G | 001 | YB20 | A000 | OM |
| 007D101902 | Consulting Unit A (OM) | C | 001 | YB25 | A000 | OM |
| 007D101301 | Manufacturing 1 (OM) | F | 001 | YB20 | A000 | OM |
| 007D101302 | Manufacturing 2 (OM) | F | 001 | YB20 | A000 | OM |
| 007D101401 | QM (OM) | H | 001 | YB40 | A000 | OM |
| 007D101501 | R&D (OM) | E | 001 | YB50 | A000 | OM |
| 007D101701 | Plant & Maintenance (OM) | H | 001 | YB40 | A000 | OM |
| 007D101321 | Services/Consulting (OM) | F | 001 | YB20 | A000 | OM |
| 007D101751 | HR Services (OM) | W | 001 | YB40 | A000 | OM |
| 007D101752 | HR Recruitment (OM) | W | 001 | YB40 | A000 | OM |
| 007D101753 | IT Services (OM) | W | 001 | YB40 | A000 | OM |
| 007D101901 | Back Office (OM) | H | 001 | YB30 | A000 | OM |
| 007D101903 | Consulting Unit B (OM) | C | 001 | YB25 | A000 | OM |
| 007D101904 | Customer Development (OM) | C | 001 | YB25 | A000 | OM |
| 57101101 | Financials (PE) | W | 001 | YB40 | A000 | PE |
| 57101601 | Marketing (PE) | 9 | 001 | YB35 | A000 | PE |
| 57101602 | Sales (PE) | V | 001 | YB30 | A000 | PE |
| 57101801 | Other Inc.&Expense (PE) | W | 001 | YB40 | A000 | PE |
| 57101750 | Build. & Maintenance (PE) | H | 001 | YB40 | A000 | PE |
| 57101201 | Purch & Stores 1 (PE) | G | 001 | YB20 | A000 | PE |
| 57101202 | Purch & Stores 2 (PE) | G | 001 | YB20 | A000 | PE |
| 57101902 | Consulting Unit A (PE) | C | 001 | YB25 | A000 | PE |
| 57101301 | Manufacturing 1 (PE) | F | 001 | YB20 | A000 | PE |
| 57101302 | Manufacturing 2 (PE) | F | 001 | YB20 | A000 | PE |
| 57101401 | QM (PE) | H | 001 | YB40 | A000 | PE |
| 57101501 | R&D (PE) | E | 001 | YB50 | A000 | PE |
| 57101701 | Plant & Maintenance (PE) | H | 001 | YB40 | A000 | PE |
| 57101321 | Services/Consulting (PE) | F | 001 | YB20 | A000 | PE |
| 57101751 | HR Services (PE) | W | 001 | YB40 | A000 | PE |
| 57101752 | HR Recruitment (PE) | W | 001 | YB40 | A000 | PE |
| 57101753 | IT Services (PE) | W | 001 | YB40 | A000 | PE |
| 57101901 | Back Office (PE) | H | 001 | YB30 | A000 | PE |
| 57101903 | Consulting Unit B (PE) | C | 001 | YB25 | A000 | PE |
| 57101904 | Customer Development (PE) | C | 001 | YB25 | A000 | PE |
| 58101101 | Financials (PH) | W | 001 | YB40 | A000 | PH |
| 58101601 | Marketing (PH) | 9 | 001 | YB35 | A000 | PH |
| 58101602 | Sales (PH) | V | 001 | YB30 | A000 | PH |
| 58101801 | Other Inc.&Expense (PH) | W | 001 | YB40 | A000 | PH |
| 58101750 | Build. & Maintenance (PH) | H | 001 | YB40 | A000 | PH |
| 58101201 | Purch & Stores 1 (PH) | G | 001 | YB20 | A000 | PH |
| 58101202 | Purch & Stores 2 (PH) | G | 001 | YB20 | A000 | PH |
| 58101902 | Consulting Unit A (PH) | C | 001 | YB25 | A000 | PH |
| 58101301 | Manufacturing 1 (PH) | F | 001 | YB20 | A000 | PH |
| 58101302 | Manufacturing 2 (PH) | F | 001 | YB20 | A000 | PH |
| 58101401 | QM (PH) | H | 001 | YB40 | A000 | PH |
| 58101501 | R&D (PH) | E | 001 | YB50 | A000 | PH |
| 58101701 | Plant & Maintenance (PH) | H | 001 | YB40 | A000 | PH |
| 58101321 | Services/Consulting (PH) | F | 001 | YB20 | A000 | PH |
| 58101751 | HR Services (PH) | W | 001 | YB40 | A000 | PH |
| 58101752 | HR Recruitment (PH) | W | 001 | YB40 | A000 | PH |
| 58101753 | IT Services (PH) | W | 001 | YB40 | A000 | PH |
| 58101901 | Back Office (PH) | H | 001 | YB30 | A000 | PH |
| 58101903 | Consulting Unit B (PH) | C | 001 | YB25 | A000 | PH |
| 58101904 | Customer Development (PH) | C | 001 | YB25 | A000 | PH |
| 26101101 | Financials (PL) | W | 001 | YB40 | A000 | PL |
| 26101601 | Marketing (PL) | 9 | 001 | YB35 | A000 | PL |
| 26101602 | Sales (PL) | V | 001 | YB30 | A000 | PL |
| 26101801 | Other Inc.&Expense (PL) | W | 001 | YB40 | A000 | PL |
| 26101750 | Build. & Maintenance (PL) | H | 001 | YB40 | A000 | PL |
| 26101201 | Purch & Stores 1 (PL) | G | 001 | YB20 | A000 | PL |
| 26101202 | Purch & Stores 2 (PL) | G | 001 | YB20 | A000 | PL |
| 26101902 | Consulting Unit A (PL) | C | 001 | YB25 | A000 | PL |
| 26101301 | Manufacturing 1 (PL) | F | 001 | YB20 | A000 | PL |
| 26101302 | Manufacturing 2 (PL) | F | 001 | YB20 | A000 | PL |
| 26101401 | QM (PL) | H | 001 | YB40 | A000 | PL |
| 26101501 | R&D (PL) | E | 001 | YB50 | A000 | PL |
| 26101701 | Plant & Maintenance (PL) | H | 001 | YB40 | A000 | PL |
| 26101321 | Services/Consulting (PL) | F | 001 | YB20 | A000 | PL |
| 26101751 | HR Services (PL) | W | 001 | YB40 | A000 | PL |
| 26101752 | HR Recruitment (PL) | W | 001 | YB40 | A000 | PL |
| 26101753 | IT Services (PL) | W | 001 | YB40 | A000 | PL |
| 26101901 | Back Office (PL) | H | 001 | YB30 | A000 | PL |
| 26101903 | Consulting Unit B (PL) | C | 001 | YB25 | A000 | PL |
| 26101904 | Customer Development (PL) | C | 001 | YB25 | A000 | PL |
| 35101101 | Financials (PT) | W | 001 | YB40 | A000 | PT |
| 35101601 | Marketing (PT) | 9 | 001 | YB35 | A000 | PT |
| 35101602 | Sales (PT) | V | 001 | YB30 | A000 | PT |
| 35101801 | Other Inc.&Expense (PT) | W | 001 | YB40 | A000 | PT |
| 35101750 | Build. & Maintenance (PT) | H | 001 | YB40 | A000 | PT |
| 35101201 | Purch & Stores 1 (PT) | G | 001 | YB20 | A000 | PT |
| 35101202 | Purch & Stores 2 (PT) | G | 001 | YB20 | A000 | PT |
| 35101902 | Consulting Unit A-(PT) | C | 001 | YB25 | A000 | PT |
| 35101301 | Manufacturing 1 (PT) | F | 001 | YB20 | A000 | PT |
| 35101302 | Manufacturing 2 (PT) | F | 001 | YB20 | A000 | PT |
| 35101401 | QM (PT) | H | 001 | YB40 | A000 | PT |
| 35101501 | R&D (PT) | E | 001 | YB50 | A000 | PT |
| 35101701 | Plant & Maintenance (PT) | H | 001 | YB40 | A000 | PT |
| 35101321 | Services/Consulting (PT) | F | 001 | YB20 | A000 | PT |
| 35101751 | HR Services (PT) | W | 001 | YB40 | A000 | PT |
| 35101752 | HR Recruitment (PT) | W | 001 | YB40 | A000 | PT |
| 35101753 | IT Services (PT) | W | 001 | YB40 | A000 | PT |
| 35101901 | Back Office (PT) | H | 001 | YB30 | A000 | PT |
| 35101903 | Consulting Unit B (PT) | C | 001 | YB25 | A000 | PT |
| 35101904 | Customer Development (PT) | C | 001 | YB25 | A000 | PT |
| 75101101 | Financials (QA) | W | 001 | YB40 | A000 | QA |
| 75101601 | Marketing (QA) | 9 | 001 | YB35 | A000 | QA |
| 75101602 | Sales (QA) | V | 001 | YB30 | A000 | QA |
| 75101801 | Other Inc.&Expense (QA) | W | 001 | YB40 | A000 | QA |
| 75101750 | Build. & Maintenance (QA) | H | 001 | YB40 | A000 | QA |
| 75101201 | Purch & Stores 1 (QA) | G | 001 | YB20 | A000 | QA |
| 75101202 | Purch & Stores 2 (QA) | G | 001 | YB20 | A000 | QA |
| 75101902 | Consulting Unit A (QA) | C | 001 | YB25 | A000 | QA |
| 75101301 | Manufacturing 1 (QA) | F | 001 | YB20 | A000 | QA |
| 75101302 | Manufacturing 2 (QA) | F | 001 | YB20 | A000 | QA |
| 75101401 | QM (QA) | H | 001 | YB40 | A000 | QA |
| 75101501 | R&D (QA) | E | 001 | YB50 | A000 | QA |
| 75101701 | Plant & Maintenance (QA) | H | 001 | YB40 | A000 | QA |
| 75101321 | Services/Consulting (QA) | F | 001 | YB20 | A000 | QA |
| 75101751 | HR Services (QA) | W | 001 | YB40 | A000 | QA |
| 75101752 | HR Recruitment (QA) | W | 001 | YB40 | A000 | QA |
| 75101753 | IT Services (QA) | W | 001 | YB40 | A000 | QA |
| 75101901 | Back Office (QA) | H | 001 | YB30 | A000 | QA |
| 75101903 | Consulting Unit B (QA) | C | 001 | YB25 | A000 | QA |
| 75101904 | Customer Development (QA) | C | 001 | YB25 | A000 | QA |
| 28101101 | Financials (RO) | W | 001 | YB40 | A000 | RO |
| 28101601 | Marketing (RO) | 9 | 001 | YB35 | A000 | RO |
| 28101602 | Sales (RO) | V | 001 | YB30 | A000 | RO |
| 28101801 | Other Inc.&Expense (RO) | W | 001 | YB40 | A000 | RO |
| 28101750 | Build. & Maintenance (RO) | H | 001 | YB40 | A000 | RO |
| 28101201 | Purch & Stores 1 (RO) | G | 001 | YB20 | A000 | RO |
| 28101202 | Purch & Stores 2 (RO) | G | 001 | YB20 | A000 | RO |
| 28101902 | Consulting Unit A (RO) | C | 001 | YB25 | A000 | RO |
| 28101301 | Manufacturing 1 (RO) | F | 001 | YB20 | A000 | RO |
| 28101302 | Manufacturing 2 (RO) | F | 001 | YB20 | A000 | RO |
| 28101401 | QM (RO) | H | 001 | YB40 | A000 | RO |
| 28101501 | R&D (RO) | E | 001 | YB50 | A000 | RO |
| 28101701 | Plant & Maintenance (RO) | H | 001 | YB40 | A000 | RO |
| 28101321 | Services/Consulting (RO) | F | 001 | YB20 | A000 | RO |
| 28101751 | HR Services-(RO) | W | 001 | YB40 | A000 | RO |
| 28101752 | HR Recruitment-(RO) | W | 001 | YB40 | A000 | RO |
| 28101753 | IT Services-(RO) | W | 001 | YB40 | A000 | RO |
| 28101901 | Back Office-(RO) | H | 001 | YB30 | A000 | RO |
| 28101903 | Consulting Unit B-(RO) | C | 001 | YB25 | A000 | RO |
| 28101904 | Customer Development-(RO) | C | 001 | YB25 | A000 | RO |
| 60101101 | Financials (RS) | W | 001 | YB40 | A000 | RS |
| 60101601 | Marketing (RS) | 9 | 001 | YB35 | A000 | RS |
| 60101602 | Sales (RS) | V | 001 | YB30 | A000 | RS |
| 60101801 | Other Inc.&Expense (RS) | W | 001 | YB40 | A000 | RS |
| 60101750 | Build. & Maintenance (RS) | H | 001 | YB40 | A000 | RS |
| 60101201 | Purch & Stores 1 (RS) | G | 001 | YB20 | A000 | RS |
| 60101202 | Purch & Stores 2 (RS) | G | 001 | YB20 | A000 | RS |
| 60101902 | Consulting Unit A (RS) | C | 001 | YB25 | A000 | RS |
| 60101301 | Manufacturing 1 (RS) | F | 001 | YB20 | A000 | RS |
| 60101302 | Manufacturing 2 (RS) | F | 001 | YB20 | A000 | RS |
| 60101401 | QM (RS) | H | 001 | YB40 | A000 | RS |
| 60101501 | R&D (RS) | E | 001 | YB50 | A000 | RS |
| 60101701 | Plant & Maintenance (RS) | H | 001 | YB40 | A000 | RS |
| 60101321 | Services/Consulting (RS) | F | 001 | YB20 | A000 | RS |
| 60101751 | HR Services (RS) | W | 001 | YB40 | A000 | RS |
| 60101752 | HR Recruitment (RS) | W | 001 | YB40 | A000 | RS |
| 60101753 | IT Services (RS) | W | 001 | YB40 | A000 | RS |
| 60101901 | Back Office (RS) | H | 001 | YB30 | A000 | RS |
| 60101903 | Consulting Unit B (RS) | C | 001 | YB25 | A000 | RS |
| 60101904 | Customer Development (RS) | C | 001 | YB25 | A000 | RS |
| 16101101 | Financials (RU) | W | 001 | YB40 | A000 | RU |
| 16101601 | Marketing (RU) | 9 | 001 | YB35 | A000 | RU |
| 16101602 | Sales (RU) | V | 001 | YB30 | A000 | RU |
| 16101801 | Other Inc.&Expense (RU) | W | 001 | YB40 | A000 | RU |
| 16101750 | Build. & Maintenance (RU) | H | 001 | YB40 | A000 | RU |
| 16101201 | Purch & Stores 1 (RU) | G | 001 | YB20 | A000 | RU |
| 16101202 | Purch & Stores 2 (RU) | G | 001 | YB20 | A000 | RU |
| 16101902 | Consulting Unit A (RU) | C | 001 | YB25 | A000 | RU |
| 16101301 | Manufacturing 1 (RU) | F | 001 | YB20 | A000 | RU |
| 16101302 | Manufacturing 2 (RU) | F | 001 | YB20 | A000 | RU |
| 16101401 | QM (RU) | H | 001 | YB40 | A000 | RU |
| 16101501 | R&D (RU) | E | 001 | YB50 | A000 | RU |
| 16101701 | Plant & Maintenance (RU) | H | 001 | YB40 | A000 | RU |
| 16101321 | Services/Consulting (RU) | F | 001 | YB20 | A000 | RU |
| 16101751 | HR Services (RU) | W | 001 | YB40 | A000 | RU |
| 16101752 | HR Recruitment (RU) | W | 001 | YB40 | A000 | RU |
| 16101753 | IT Services (RU) | W | 001 | YB40 | A000 | RU |
| 16101901 | Back Office (RU) | H | 001 | YB30 | A000 | RU |
| 16101903 | Consulting Unit B (RU) | C | 001 | YB25 | A000 | RU |
| 16101904 | Customer Development (RU) | C | 001 | YB25 | A000 | RU |
| 59101101 | Financials (SA) | W | 001 | YB40 | A000 | SA |
| 59101601 | Marketing (SA) | 9 | 001 | YB35 | A000 | SA |
| 59101602 | Sales (SA) | V | 001 | YB30 | A000 | SA |
| 59101801 | Other Inc.&Expense (SA) | W | 001 | YB40 | A000 | SA |
| 59101750 | Build. & Maintenance (SA) | H | 001 | YB40 | A000 | SA |
| 59101201 | Purch & Stores 1 (SA) | G | 001 | YB20 | A000 | SA |
| 59101202 | Purch & Stores 2 (SA) | G | 001 | YB20 | A000 | SA |
| 59101902 | Consulting Unit A (SA) | C | 001 | YB25 | A000 | SA |
| 59101301 | Manufacturing 1 (SA) | F | 001 | YB20 | A000 | SA |
| 59101302 | Manufacturing 2 (SA) | F | 001 | YB20 | A000 | SA |
| 59101401 | QM (SA) | H | 001 | YB40 | A000 | SA |
| 59101501 | R&D (SA) | E | 001 | YB50 | A000 | SA |
| 59101701 | Plant & Maintenance (SA) | H | 001 | YB40 | A000 | SA |
| 59101321 | Services/Consulting (SA) | F | 001 | YB20 | A000 | SA |
| 59101751 | HR Services (SA) | W | 001 | YB40 | A000 | SA |
| 59101752 | HR Recruitment (SA) | W | 001 | YB40 | A000 | SA |
| 59101753 | IT Services (SA) | W | 001 | YB40 | A000 | SA |
| 59101901 | Back Office (SA) | H | 001 | YB30 | A000 | SA |
| 59101903 | Consulting Unit B (SA) | C | 001 | YB25 | A000 | SA |
| 59101904 | Customer Development (SA) | C | 001 | YB25 | A000 | SA |
| 19101101 | Financials (SE) | W | 001 | YB40 | A000 | SE |
| 19101601 | Marketing (SE) | 9 | 001 | YB35 | A000 | SE |
| 19101602 | Sales (SE) | V | 001 | YB30 | A000 | SE |
| 19101801 | Other Inc.&Expense (SE) | W | 001 | YB40 | A000 | SE |
| 19101750 | Build. & Maintenance (SE) | H | 001 | YB40 | A000 | SE |
| 19101201 | Purch & Stores 1 (SE) | G | 001 | YB20 | A000 | SE |
| 19101202 | Purch & Stores 2 (SE) | G | 001 | YB20 | A000 | SE |
| 19101902 | ConsultingUnit A (SE) | C | 001 | YB25 | A000 | SE |
| 19101301 | Manufacturing 1 (SE) | F | 001 | YB20 | A000 | SE |
| 19101302 | Manufacturing 2 (SE) | F | 001 | YB20 | A000 | SE |
| 19101401 | QM (SE) | H | 001 | YB40 | A000 | SE |
| 19101501 | R&D (SE) | E | 001 | YB50 | A000 | SE |
| 19101701 | Plant & Maintenance (SE) | H | 001 | YB40 | A000 | SE |
| 19101321 | Services/Consulting (SE) | F | 001 | YB20 | A000 | SE |
| 19101751 | HR Services (SE) | W | 001 | YB40 | A000 | SE |
| 19101752 | HR Recruitment (SE) | W | 001 | YB40 | A000 | SE |
| 19101753 | IT Services (SE) | W | 001 | YB40 | A000 | SE |
| 19101901 | Back Office (SE) | H | 001 | YB30 | A000 | SE |
| 19101903 | ConsultingUnit B (SE) | C | 001 | YB25 | A000 | SE |
| 19101904 | Customer Development (SE) | C | 001 | YB25 | A000 | SE |
| 61101101 | Financials (SG) | W | 001 | YB40 | A000 | SG |
| 61101601 | Marketing (SG) | 9 | 001 | YB35 | A000 | SG |
| 61101602 | Sales (SG) | V | 001 | YB30 | A000 | SG |
| 61101801 | Other Inc.&Expense (SG) | W | 001 | YB40 | A000 | SG |
| 61101750 | Build. & Maintenance (SG) | H | 001 | YB40 | A000 | SG |
| 61101201 | Purch & Stores 1 (SG) | G | 001 | YB20 | A000 | SG |
| 61101202 | Purch & Stores 2 (SG) | G | 001 | YB20 | A000 | SG |
| 61101902 | Consulting Unit A (SG) | C | 001 | YB25 | A000 | SG |
| 61101301 | Manufacturing 1 (SG) | F | 001 | YB20 | A000 | SG |
| 61101302 | Manufacturing 2 (SG) | F | 001 | YB20 | A000 | SG |
| 61101401 | QM (SG) | H | 001 | YB40 | A000 | SG |
| 61101501 | R&D (SG) | E | 001 | YB50 | A000 | SG |
| 61101701 | Plant & Maintenance (SG) | H | 001 | YB40 | A000 | SG |
| 61101321 | Services/Consulting (SG) | F | 001 | YB20 | A000 | SG |
| 61101751 | HR Services (SG) | W | 001 | YB40 | A000 | SG |
| 61101752 | HR Recruitment (SG) | W | 001 | YB40 | A000 | SG |
| 61101753 | IT Services (SG) | W | 001 | YB40 | A000 | SG |
| 61101901 | Back Office (SG) | H | 001 | YB30 | A000 | SG |
| 61101903 | Consulting Unit B (SG) | C | 001 | YB25 | A000 | SG |
| 61101904 | Customer Development (SG) | C | 001 | YB25 | A000 | SG |
| 41101101 | Financials (SI) | W | 001 | YB40 | A000 | SI |
| 41101601 | Marketing (SI) | 9 | 001 | YB35 | A000 | SI |
| 41101602 | Sales (SI) | V | 001 | YB30 | A000 | SI |
| 41101801 | Other Inc.&Expense (SI) | W | 001 | YB40 | A000 | SI |
| 41101750 | Build. & Maintenance (SI) | H | 001 | YB40 | A000 | SI |
| 41101201 | Purch & Stores 1 (SI) | G | 001 | YB20 | A000 | SI |
| 41101202 | Purch & Stores 2 (SI) | G | 001 | YB20 | A000 | SI |
| 41101902 | Consulting Unit A (SI) | C | 001 | YB25 | A000 | SI |
| 41101301 | Manufacturing 1 (SI) | F | 001 | YB20 | A000 | SI |
| 41101302 | Manufacturing 2 (SI) | F | 001 | YB20 | A000 | SI |
| 41101401 | QM (SI) | H | 001 | YB40 | A000 | SI |
| 41101501 | R&D (SI) | E | 001 | YB50 | A000 | SI |
| 41101701 | Plant & Maintenance (SI) | H | 001 | YB40 | A000 | SI |
| 41101321 | Services/Consulting (SI) | F | 001 | YB20 | A000 | SI |
| 41101751 | HR Services (SI) | W | 001 | YB40 | A000 | SI |
| 41101752 | HR Recruitment (SI) | W | 001 | YB40 | A000 | SI |
| 41101753 | IT Services (SI) | W | 001 | YB40 | A000 | SI |
| 41101901 | Back Office (SI) | H | 001 | YB30 | A000 | SI |
| 41101903 | Consulting Unit B (SI) | C | 001 | YB25 | A000 | SI |
| 41101904 | Customer Development (SI) | C | 001 | YB25 | A000 | SI |
| 27101101 | Financials (SK) | W | 001 | YB40 | A000 | SK |
| 27101601 | Marketing (SK) | 9 | 001 | YB35 | A000 | SK |
| 27101602 | Sales (SK) | V | 001 | YB30 | A000 | SK |
| 27101801 | Other Inc.&Expense (SK) | W | 001 | YB40 | A000 | SK |
| 27101750 | Build. & Maintenance (SK) | H | 001 | YB40 | A000 | SK |
| 27101201 | Purch & Stores 1 (SK) | G | 001 | YB20 | A000 | SK |
| 27101202 | Purch & Stores 2 (SK) | G | 001 | YB20 | A000 | SK |
| 27101902 | Consulting Unit A (SK) | C | 001 | YB25 | A000 | SK |
| 27101301 | Manufacturing 1 (SK) | F | 001 | YB20 | A000 | SK |
| 27101302 | Manufacturing 2 (SK) | F | 001 | YB20 | A000 | SK |
| 27101401 | QM (SK) | H | 001 | YB40 | A000 | SK |
| 27101501 | R&D (SK) | E | 001 | YB50 | A000 | SK |
| 27101701 | Plant & Maintenance (SK) | H | 001 | YB40 | A000 | SK |
| 27101321 | Services/Consulting (SK) | F | 001 | YB20 | A000 | SK |
| 27101751 | HR Services (SK) | W | 001 | YB40 | A000 | SK |
| 27101752 | HR Recruitment (SK) | W | 001 | YB40 | A000 | SK |
| 27101753 | IT Services (SK) | W | 001 | YB40 | A000 | SK |
| 27101901 | Back Office (SK) | H | 001 | YB30 | A000 | SK |
| 27101903 | Consulting Unit B (SK) | C | 001 | YB25 | A000 | SK |
| 27101904 | Customer Development (SK) | C | 001 | YB25 | A000 | SK |
| 68101101 | Financials (TH) | W | 001 | YB40 | A000 | TH |
| 68101601 | Marketing (TH) | 9 | 001 | YB35 | A000 | TH |
| 68101602 | Sales (TH) | V | 001 | YB30 | A000 | TH |
| 68101801 | Other Inc.&Expense (TH) | W | 001 | YB40 | A000 | TH |
| 68101750 | Build. & Maintenance (TH) | H | 001 | YB40 | A000 | TH |
| 68101201 | Purch & Stores 1 (TH) | G | 001 | YB20 | A000 | TH |
| 68101202 | Purch & Stores 2 (TH) | G | 001 | YB20 | A000 | TH |
| 68101902 | Consulting Unit A (TH) | C | 001 | YB25 | A000 | TH |
| 68101301 | Manufacturing 1 (TH) | F | 001 | YB20 | A000 | TH |
| 68101302 | Manufacturing 2 (TH) | F | 001 | YB20 | A000 | TH |
| 68101401 | QM (TH) | H | 001 | YB40 | A000 | TH |
| 68101501 | R&D (TH) | E | 001 | YB50 | A000 | TH |
| 68101701 | Plant & Maintenance (TH) | H | 001 | YB40 | A000 | TH |
| 68101321 | Services/Consulting (TH) | F | 001 | YB20 | A000 | TH |
| 68101751 | HR Services (TH) | W | 001 | YB40 | A000 | TH |
| 68101752 | HR Recruitment (TH) | W | 001 | YB40 | A000 | TH |
| 68101753 | IT Services (TH) | W | 001 | YB40 | A000 | TH |
| 68101901 | Back Office (TH) | H | 001 | YB30 | A000 | TH |
| 68101903 | Consulting Unit B (TH) | C | 001 | YB25 | A000 | TH |
| 68101904 | Customer Development (TH) | C | 001 | YB25 | A000 | TH |
| 36101101 | Financials (TR) | W | 001 | YB40 | A000 | TR |
| 36101601 | Marketing (TR) | 9 | 001 | YB35 | A000 | TR |
| 36101602 | Sales (TR) | V | 001 | YB30 | A000 | TR |
| 36101801 | Other Inc.&Expense (TR) | W | 001 | YB40 | A000 | TR |
| 36101750 | Build. & Maintenance (TR) | H | 001 | YB40 | A000 | TR |
| 36101201 | Purch & Stores 1 (TR) | G | 001 | YB20 | A000 | TR |
| 36101202 | Purch & Stores 2 (TR) | G | 001 | YB20 | A000 | TR |
| 36101902 | Consulting Unit A (TR) | C | 001 | YB25 | A000 | TR |
| 36101301 | Manufacturing 1 (TR) | F | 001 | YB20 | A000 | TR |
| 36101302 | Manufacturing 2 (TR) | F | 001 | YB20 | A000 | TR |
| 36101401 | QM (TR) | H | 001 | YB40 | A000 | TR |
| 36101501 | R&D (TR) | E | 001 | YB50 | A000 | TR |
| 36101701 | Plant & Maintenance (TR) | H | 001 | YB40 | A000 | TR |
| 36101321 | Services/Consulting (TR) | F | 001 | YB20 | A000 | TR |
| 36101751 | HR Services (TR) | W | 001 | YB40 | A000 | TR |
| 36101752 | HR Recruitment (TR) | W | 001 | YB40 | A000 | TR |
| 36101753 | IT Services (TR) | W | 001 | YB40 | A000 | TR |
| 36101901 | Back Office (TR) | H | 001 | YB30 | A000 | TR |
| 36101903 | Consulting Unit B (TR) | C | 001 | YB25 | A000 | TR |
| 36101904 | Customer Development (TR) | C | 001 | YB25 | A000 | TR |
| 63101101 | Financials (TW) | W | 001 | YB40 | A000 | TW |
| 63101601 | Marketing (TW) | 9 | 001 | YB35 | A000 | TW |
| 63101602 | Sales (TW) | V | 001 | YB30 | A000 | TW |
| 63101801 | Other Inc.&Exp (TW) | W | 001 | YB40 | A000 | TW |
| 63101750 | Build. & Maint (TW) | H | 001 | YB40 | A000 | TW |
| 63101201 | Purch & Store 1 (TW) | G | 001 | YB20 | A000 | TW |
| 63101202 | Purch & Store 2 (TW) | G | 001 | YB20 | A000 | TW |
| 63101902 | Csltg Unit A (TW) | C | 001 | YB25 | A000 | TW |
| 63101301 | Manufacturing 1 (TW) | F | 001 | YB20 | A000 | TW |
| 63101302 | Manufacturing 2 (TW) | F | 001 | YB20 | A000 | TW |
| 63101401 | QM (TW) | H | 001 | YB40 | A000 | TW |
| 63101501 | R&D (TW) | E | 001 | YB50 | A000 | TW |
| 63101701 | Plant & Maintenance (TW) | H | 001 | YB40 | A000 | TW |
| 63101321 | Services/Consulting (TW) | F | 001 | YB20 | A000 | TW |
| 63101751 | HR Services (TW) | W | 001 | YB40 | A000 | TW |
| 63101752 | HR Recruitment (TW) | W | 001 | YB40 | A000 | TW |
| 63101753 | IT Services (TW) | W | 001 | YB40 | A000 | TW |
| 63101901 | Back Office (TW) | H | 001 | YB30 | A000 | TW |
| 63101903 | Csltg Unit B (TW) | C | 001 | YB25 | A000 | TW |
| 63101904 | Customer Dev (TW) | C | 001 | YB25 | A000 | TW |
| 65101101 | Financials (UA) | W | 001 | YB40 | A000 | UA |
| 65101601 | Marketing (UA) | 9 | 001 | YB35 | A000 | UA |
| 65101602 | Sales (UA) | V | 001 | YB30 | A000 | UA |
| 65101801 | Other Inc.&Expense (UA) | W | 001 | YB40 | A000 | UA |
| 65101750 | Build. & Maintenance (UA) | H | 001 | YB40 | A000 | UA |
| 65101201 | Purch & Stores 1 (UA) | G | 001 | YB20 | A000 | UA |
| 65101202 | Purch & Stores 2 (UA) | G | 001 | YB20 | A000 | UA |
| 65101902 | Consulting Unit A (UA) | C | 001 | YB25 | A000 | UA |
| 65101301 | Manufacturing 1 (UA) | F | 001 | YB20 | A000 | UA |
| 65101302 | Manufacturing 2 (UA) | F | 001 | YB20 | A000 | UA |
| 65101401 | QM (UA) | H | 001 | YB40 | A000 | UA |
| 65101501 | R&D (UA) | E | 001 | YB50 | A000 | UA |
| 65101701 | Plant & Maintenance (UA) | H | 001 | YB40 | A000 | UA |
| 65101321 | Services/Consulting (UA) | F | 001 | YB20 | A000 | UA |
| 65101751 | HR Services (UA) | W | 001 | YB40 | A000 | UA |
| 65101752 | HR Recruitment (UA) | W | 001 | YB40 | A000 | UA |
| 65101753 | IT Services (UA) | W | 001 | YB40 | A000 | UA |
| 65101901 | Back Office (UA) | H | 001 | YB30 | A000 | UA |
| 65101903 | Consulting Unit B (UA) | C | 001 | YB25 | A000 | UA |
| 65101904 | Customer Development (UA) | C | 001 | YB25 | A000 | UA |
| 64101101 | Financials (ZA) | W | 001 | YB40 | A000 | ZA |
| 64101601 | Marketing (ZA) | 9 | 001 | YB35 | A000 | ZA |
| 64101602 | Sales (ZA) | V | 001 | YB30 | A000 | ZA |
| 64101801 | Other Inc.&Expense (ZA) | W | 001 | YB40 | A000 | ZA |
| 64101750 | Build. & Maintenance (ZA) | H | 001 | YB40 | A000 | ZA |
| 64101201 | Purch & Stores 1 (ZA) | G | 001 | YB20 | A000 | ZA |
| 64101202 | Purch & Stores 2 (ZA) | G | 001 | YB20 | A000 | ZA |
| 64101902 | Consulting Unit A (ZA) | C | 001 | YB25 | A000 | ZA |
| 64101301 | Manufacturing 1 (ZA) | F | 001 | YB20 | A000 | ZA |
| 64101302 | Manufacturing 2 (ZA) | F | 001 | YB20 | A000 | ZA |
| 64101401 | QM (ZA) | H | 001 | YB40 | A000 | ZA |
| 64101501 | R&D (ZA) | E | 001 | YB50 | A000 | ZA |
| 64101701 | Plant & Maintenance (ZA) | H | 001 | YB40 | A000 | ZA |
| 64101321 | Services/Consulting (ZA) | F | 001 | YB20 | A000 | ZA |
| 64101751 | HR Services (ZA) | W | 001 | YB40 | A000 | ZA |
| 64101752 | HR Recruitment (ZA) | W | 001 | YB40 | A000 | ZA |
| 64101753 | IT Services (ZA) | W | 001 | YB40 | A000 | ZA |
| 64101901 | Back Office (ZA) | H | 001 | YB30 | A000 | ZA |
| 64101903 | Consulting Unit B (ZA) | C | 001 | YB25 | A000 | ZA |
| 64101904 | Customer Development (ZA) | C | 001 | YB25 | A000 | ZA |

### Sheet: Cost Center Groups

| Group First Level | Group Second Level | Example<br>US | Group Third Level | Group Fourth level | Group<br>fifth level | Group Name | Cost Center | Cost Center Name |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Country/region-specific Hierarchies 10## |  |  |  |  |  |  |  |  |
| CoCo |  | 1710### |  |  |  | Country (e.g. US) |  |  |
|  | CoCo110 | 1710110 |  |  |  | Shared Services |  |  |
|  |  |  |  |  |  |  | ##101101 | Financials |
|  |  |  |  |  |  |  | ##101750 | Buildings & Plant Maintenance |
|  |  |  |  |  |  |  | ##101701 | Plant & Maintenance |
|  |  |  |  |  |  |  | ##101751 | HR Services |
|  |  |  |  |  |  |  | ##101752 | HR Recruitment |
|  |  |  |  |  |  |  | ##101753 | IT Services |
|  | ##10120 | 1710120 |  |  |  | Stores |  |  |
|  |  |  |  |  |  |  | ##101201 | Purchasing & Stores - 1 |
|  |  |  |  |  |  |  | ##101202 | Purchasing & Stores - 2 |
|  | ##10130 | 1710130 |  |  |  | Operations |  |  |
|  |  |  |  |  |  |  | ##101301 | Manufacturing 1 |
|  |  |  |  |  |  |  | ##101302 | Manufacturing 2 |
|  | ##10140 | 1710140 |  |  |  | Quality Management |  |  |
|  |  |  |  |  |  |  | ##101401 | QM |
|  | ##10150 | 1710150 |  |  |  | Research and Development |  |  |
|  |  |  |  |  |  |  | ##101501 | R&D |
|  | ##10160 | 1710160 |  |  |  | Marketing |  |  |
|  |  |  |  |  |  |  | ##101601 | Marketing |
|  | ##10170 | 1710170 |  |  |  | Sales |  |  |
|  |  |  |  |  |  |  | ##101602 | Sales |
|  | ##10180 | 1710180 |  |  |  | Other Income & Expense |  |  |
|  |  |  |  |  |  |  | ##101801 | Other Income & Expense |
|  | ##10190 | 1710190 |  |  |  | Services and Consulting |  |  |
|  |  |  |  |  |  |  | ##101901 | Back Office |
|  |  |  |  |  |  |  | ##101902 | Consulting Unit A |
|  |  |  |  |  |  |  | ##101903 | Consulting Unit B |
|  |  |  |  |  |  |  | ##101904 | Customer Development |
|  | ##10200 | 1710200 |  |  |  | CCA Receiver Bldg & Mntnce Cost-Service |  |  |
|  |  |  |  |  |  |  | ##101751 | HR Services |
|  |  |  |  |  |  |  | ##101752 | HR Recruitment |
|  |  |  |  |  |  |  | ##101753 | IT Services |
|  |  |  |  |  |  |  | ##101901 | Back Office |
|  |  |  |  |  |  |  | ##101902 | Consulting Unit A |
|  |  |  |  |  |  |  | ##101903 | Consulting Unit B |
|  |  |  |  |  |  |  | ##101904 | Customer Development |
|  |  |  |  |  |  |  | ##101101 | Financials |
|  |  |  |  |  |  |  | ##101601 | Marketing |
|  |  |  |  |  |  |  | ##101602 | Sales |
|  | ##10300 | 1710300 |  |  |  | CCA Receiver Bldg & Mntnce Cost-Manuf |  |  |
|  |  |  |  |  |  |  | ##101201 | Purch & Stores 1 |
|  |  |  |  |  |  |  | ##101202 | Purch & Stores 2 |
|  |  |  |  |  |  |  | ##101701 | Plant & Maintenance |
|  |  |  |  |  |  |  | ##101301 | Manufacturing 1 |
|  |  |  |  |  |  |  | ##101302 | Manufacturing 2 |
|  |  |  |  |  |  |  | ##101401 | QM |
|  |  |  |  |  |  |  | ##101501 | R&D |
|  |  |  |  |  |  |  | ##101101 | Financials |
|  |  |  |  |  |  |  | ##101601 | Marketing |
|  |  |  |  |  |  |  | ##101602 | Sales |
| Standard Hierarchy |  |  |  |  |  |  |  |  |
| 0001 |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  | ##101101 | Financials |
|  |  |  |  |  |  |  | ##101201 | Purchasing & Stores 1 |
|  |  |  |  |  |  |  | ##101202 | Purchasing & Stores 2 |
|  |  |  |  |  |  |  | ##101301 | Manufacturing 1 |
|  |  |  |  |  |  |  | ##101302 | Manufacturing 2 |
|  |  |  |  |  |  |  | ##101321 | Services/Consulting |
|  |  |  |  |  |  |  | ##101401 | Quality Management |
|  |  |  |  |  |  |  | ##101501 | Research and Development |
|  |  |  |  |  |  |  | ##101601 | Marketing |
|  |  |  |  |  |  |  | ##101602 | Sales |
|  |  |  |  |  |  |  | ##101701 | Plant & Maintenance |
|  |  |  |  |  |  |  | ##101750 | Buildings & Plant Maintenance |
|  |  |  |  |  |  |  | ##101751 | HR Services |
|  |  |  |  |  |  |  | ##101752 | HR Recruitment |
|  |  |  |  |  |  |  | ##101753 | IT Services |
|  |  |  |  |  |  |  | ##101801 | Other Income & Expense |
|  |  |  |  |  |  |  | ##101901 | Back Office |
|  |  |  |  |  |  |  | ##101902 | Consulting Unit A |
|  |  |  |  |  |  |  | ##101903 | Consulting Unit B |
|  |  |  |  |  |  |  | ##101904 | Customer Development |
|  |  |  |  |  |  |  | ##10##40 | Template Store |
|  |  |  |  |  |  |  | ##10##41 | Demo Store 1 |
|  |  |  |  |  |  |  | ##10##42 | Demo Store 2 |
|  |  |  |  |  |  |  | ##10##43 | Demo Store 3 |
|  |  |  |  |  |  |  | ##10##44 | Demo Store 4 |

### Sheet: Activity Types

| Activity Type | Name | Allocation CE | Unit | Cost Center Category | Activity Type Category | Price Indicator: Calculate Allocation Price | Country |
| --- | --- | --- | --- | --- | --- | --- | --- |
| SV01 | Service-Time | 94308100 | H | C | #1 | #3 | XX |
| ELEC | Energy- Emission Breakdown | 94306000 | KWH | * | #1 | #3 | XX |
| U001 | UBB-Revenue Cloud Sales | 94308500 | PC | C | #1 | #3 | XX |
| U002 | UBB-Service Center | 94308500 | PC | C | #1 | #3 | XX |
| U003 | UBB-Monitoring | 94308500 | PC | C | #1 | #3 | XX |
| U004 | UBB-type 4 | 94308500 | PC | C | #1 | #3 | XX |
| U005 | UBB-type 5 | 94308500 | PC | C | #1 | #3 | XX |
| U006 | UBB-type 6 | 94308500 | PC | C | #1 | #3 | XX |
| U007 | UBB-type 7 | 94308500 | PC | C | #1 | #3 | XX |
| U008 | UBB-type 8 | 94308500 | PC | C | #1 | #3 | XX |
| U009 | UBB-type 9 | 94308500 | PC | C | #1 | #3 | XX |
| U010 | UBB-type 10 | 94308500 | PC | C | #1 | #3 | XX |
| 8 | Consulting | 94308000 | H | * | #1 | #3 | XX |
| 1 | Machine hours 1 | 94301000 | H | * | #1 | #3 | XX |
| 2 | Machine hours 2 | 94302000 | H | * | #1 | #3 | XX |
| 3 | Setup Production | 94303000 | H | * | #1 | #3 | XX |
| 11 | Personnel Hours | 94311000 | H | * | #1 | #3 | XX |
| 101 | Service Standard | 94311000 | H | * | #1 | #3 | XX |
| 102 | Service Specialist | 94311000 | H | * | #1 | #3 | XX |
| T001 | Junior Consultant | 94308000 | H | C | #1 | #3 | XX |
| T002 | Senior Consultant | 94308000 | H | C | #1 | #3 | XX |
| T003 | Platinum Consultant | 94308000 | H | C | #1 | #3 | XX |
| T004 | Trainer | 94308000 | H | C | #1 | #3 | XX |
| T005 | Project Manager | 94308000 | H | C | #1 | #3 | XX |
| T006 | $ Time / Fee type 6 | 94308000 | H | C | #1 | #3 | XX |
| T007 | $ Time / Fee type 7 | 94308000 | H | C | #1 | #3 | XX |
| T008 | $ Time / Fee type 8 | 94308000 | H | C | #1 | #3 | XX |
| T009 | $ Time / Fee type 9 | 94308000 | H | C | #1 | #3 | XX |
| T010 | $ Time / Fee type 10 | 94308000 | H | C | #1 | #3 | XX |
| T011 | $ Time / Fee type 11 | 94308000 | H | C | #1 | #3 | XX |
| T012 | $ Time / Fee type 12 | 94308000 | H | C | #1 | #3 | XX |
| T013 | $ Time / Fee type 13 | 94308000 | H | C | #1 | #3 | XX |
| T014 | $ Time / Fee type 14 | 94308000 | H | C | #1 | #3 | XX |
| T015 | $ Time / Fee type 15 | 94308000 | H | C | #1 | #3 | XX |
| T016 | $ Time / Fee type 16 | 94308000 | H | C | #1 | #3 | XX |
| T017 | $ Time / Fee type 17 | 94308000 | H | C | #1 | #3 | XX |
| T018 | $ Time / Fee type 18 | 94308000 | H | C | #1 | #3 | XX |
| T019 | $ Time / Fee type 19 | 94308000 | H | C | #1 | #3 | XX |
| T020 | $ Time / Fee type 20 | 94308000 | H | C | #1 | #3 | XX |

### Sheet: Activity Type Groups

| Activity Type Group<br>Level 1 | Activity Type Group<br>Level 2 | Name | Activity Type | Name |
| --- | --- | --- | --- | --- |
| YBMF_P00 |  | Planning Activity Types |  |  |
|  | YBMF_P01 | Manufacturing Labor |  |  |
|  |  |  | 3 | Setup production |
|  |  |  | 11 | Personnel hours |
|  | YBMF_P02 | Manufacturing Overhead |  |  |
|  |  |  | 1 | Machine Hours 1 |
|  |  |  | 2 | Machine Hours 2 |
|  | YBSV_S00 | SP: Planning Activity Types |  |  |
|  |  |  | T001 | Junior Consultant |
|  |  |  | T002 | Senior Consultant |
|  |  |  | T003 | Platinum Consultant |
|  |  |  | T004 | Trainer |
|  |  |  | T005 | Projekt Manager |
|  |  |  | T006 | $ Time / Fee type 6 (res for Travel Time) |
|  |  |  | T007 | $ Time / Fee type 7 |
|  |  |  | T008 | $ Time / Fee type 8 |
|  |  |  | T009 | $ Time / Fee type 9 |
|  |  |  | T010 | $ Time / Fee type 10 |
|  | YBSV_S01 | Consulting |  |  |
|  |  |  | T001 | Junior Consultant |
|  |  |  | T002 | Senior Consultant |
|  |  |  | T003 | Platinum Consultant |
|  |  |  | T004 | Trainer |
|  |  |  | T005 | Projekt Manager |
|  |  |  | T006 | $ Time / Fee type 6 (res for Travel Time) |
|  |  |  | T007 | $ Time / Fee type 7 |
|  |  |  | T008 | $ Time / Fee type 8 |
|  |  |  | T009 | $ Time / Fee type 9 |
|  |  |  | T010 | $ Time / Fee type 10 |
|  | YBSV_S02 | Service |  |  |
|  |  |  | U001 | UBB-Revenue Cloud Sales |
|  |  |  | U002 | UBB-Service Center |
|  |  |  | U003 | UBB-Monitoring |
|  |  |  | U004 | UBB-type 4 |
|  |  |  | U005 | UBB-type 5 |
|  |  |  | U006 | UBB-type 6 |
|  |  |  | U007 | UBB-type 7 |
|  |  |  | U008 | UBB-type 8 |
|  |  |  | U009 | UBB-type 9 |
|  |  |  | U010 | UBB-type 10 |

### Sheet: Secondary Cost Elements

| Controlling Area | Cost Element | Name | Cost Element Category | Country |
| --- | --- | --- | --- | --- |
| A000 | 63009100 | Lease Expense Building (ROU) | #01 | XX |
| A000 | 63009200 | Lease Expense Land (ROU) | #01 | XX |
| A000 | 63009300 | Lease Expense Machinery (ROU) | #01 | XX |
| A000 | 63009400 | Lease Expense Motor Vehicle (ROU) | #01 | XX |
| A000 | 63009500 | Lease Expense Office Equipment (ROU) | #01 | XX |
| A000 | 63009600 | Lease Expense Furniture (ROU) | #01 | XX |
| A000 | 63009700 | Lease Expense Computer Hardware (ROU) | #01 | XX |
| A000 | 63010100 | Service Expense Land (ROU) | #01 | XX |
| A000 | 63010200 | Service Expense Building (ROU) | #01 | XX |
| A000 | 63010300 | Service Expense Machinery (ROU) | #01 | XX |
| A000 | 63010400 | Operating Expense Motor Vehicle (ROU) | #01 | XX |
| A000 | 63010500 | Service Expense Office Equipment (ROU) | #01 | XX |
| A000 | 63010600 | Service Expense Furniture (ROU) | #01 | XX |
| A000 | 63010700 | Service Expense Computer Hardware (ROU) | #01 | XX |
| A000 | 63020100 | Exp./Rev. from Valuation Diff. Building (ROU) | #01 | XX |
| A000 | 63020200 | Exp./Rev. from Valuation Diff. Land (ROU) | #01 | XX |
| A000 | 63020300 | Exp./Rev. from Valuation Diff. Machinery (ROU) | #01 | XX |
| A000 | 63020400 | Exp./Rev. from Valuation Diff. Motor Vehicle (ROU) | #01 | XX |
| A000 | 63020500 | Exp./Rev. Valuation Diff. Office Equipment (ROU) | #01 | XX |
| A000 | 63020600 | Exp./Rev. from Valuation Diff. Furniture (ROU) | #01 | XX |
| A000 | 63020700 | Exp./Rev. Valuation Diff. Computer Hardware (ROU) | #01 | XX |
| A000 | 64010000 | Service Contract Expense | #01 | XX |
| A000 | 64000100 | Depreciation Expense - Land (ROU) | #01 | XX |
| A000 | 64001100 | Depreciation Expense - Buildings (ROU) | #01 | XX |
| A000 | 64002100 | Depreciation Expense - Machinery & Equipment (ROU) | #01 | XX |
| A000 | 64004100 | Depreciation Expense - Motor Vehicles (ROU) | #01 | XX |
| A000 | 64005100 | Depreciation Expense - Office Equipment (ROU) | #01 | XX |
| A000 | 64006100 | Depreciation Expense - Furniture (ROU) | #01 | XX |
| A000 | 64007100 | Depreciation Expense - Computer Hardware (ROU) | #01 | XX |
| A000 | 70700000 | Lease Income for - Non-Residential Real Estate | #01 | XX |
| A000 | 70700100 | Leasing Income - Residential Real Estate | #01 | XX |
| A000 | 70700200 | Leasing Income - Other | #01 | XX |
| A000 | 70800100 | Service Income - Real Estate | #01 | XX |
| A000 | 70800200 | Service Income - Other | #01 | XX |
| A000 | 71100100 | Interest Expense Land (ROU) | #01 | XX |
| A000 | 71100200 | Interest Expense Building (ROU) | #01 | XX |
| A000 | 71100300 | Interest Expense Machinery (ROU) | #01 | XX |
| A000 | 71100400 | Interest Expense Motor Vehicle (ROU) | #01 | XX |
| A000 | 71100500 | Interest Expense Office Equipment (ROU) | #01 | XX |
| A000 | 71100600 | Interest Expense Furniture (ROU) | #01 | XX |
| A000 | 71100700 | Interest Computer Hardware (ROU) | #01 | XX |
| A000 | 71010300 | Loss from Asset Transactions (ROU) | #01 | XX |
| A000 | 70200000 | Interest Income, Unaffiliated(TRM) | #01 | XX |
| A000 | 70200100 | Interest Income, Affiliated, No Consolidation(TRM) | #01 | XX |
| A000 | 70200200 | Interest Income, Affiliated, Consolidation(TRM) | #01 | XX |
| A000 | 70210000 | Realized Price Gains, Unaffiliated(TRM) | #01 | XX |
| A000 | 70210100 | Realized Price Gains, Affiliated, No Consoli.(TRM) | #01 | XX |
| A000 | 70210200 | Realized Price Gains, Affiliated, Consolidat.(TRM) | #01 | XX |
| A000 | 70220000 | Gain from Price Valuation, Unaffiliated(TRM) | #01 | XX |
| A000 | 70220100 | Gain from Price Valuation, Affilia., No Cons.(TRM) | #01 | XX |
| A000 | 70220200 | Gain from Price Valuation, Affilia., Consol.(TRM) | #01 | XX |
| A000 | 70230000 | Other Income (TRM) | #01 | XX |
| A000 | 71000100 | Commission/Charge (TRM) | #01 | XX |
| A000 | 71000200 | Other Expenses (TRM) | #01 | XX |
| A000 | 71400000 | Interest Expense, Unaffiliated(TRM) | #01 | XX |
| A000 | 71400100 | Interest Expense, Affiliated, No Consolidat.(TRM) | #01 | XX |
| A000 | 71400200 | Interest Expense, Affiliated, Consolidation(TRM) | #01 | XX |
| A000 | 71500000 | Gain/Loss from Hedge Ineffectiveness(TRM) | #01 | XX |
| A000 | 71600000 | Realized Price Losses, Unaffiliated(TRM) | #01 | XX |
| A000 | 71600100 | Realized Price Losses, Affili., No Consolid.(TRM) | #01 | XX |
| A000 | 71600200 | Realized Price Losses, Affiliated, Consolid.(TRM) | #01 | XX |
| A000 | 71700000 | Loss from Price Valuation, Unaffiliated(TRM) | #01 | XX |
| A000 | 71700100 | Loss from Price Valuation, Affilia., No Cons.(TRM) | #01 | XX |
| A000 | 71700200 | Loss from Price Valuation, Affilia., Consoli.(TRM) | #01 | XX |
| A000 | 72050000 | Realized Fx Rate Losses, Unaffiliated(TRM) | #01 | XX |
| A000 | 72050100 | Realized Fx Rate Losses, Affili., No Consol.(TRM) | #01 | XX |
| A000 | 72050200 | Realized Fx Rate Losses, Affiliat., Consolid.(TRM) | #01 | XX |
| A000 | 72060000 | Loss from FX Valuation, Unaffiliated(TRM) | #01 | XX |
| A000 | 72060100 | Loss from FX Valuation, Affiliat., No Consol.(TRM) | #01 | XX |
| A000 | 72060200 | Loss from FX Valuation, Affiliat., Consolid.(TRM) | #01 | XX |
| A000 | 72550000 | Realized Fx Rate Gains, Unaffiliated(TRM) | #01 | XX |
| A000 | 72550100 | Realized Fx Rate Gains, Affiliat., No Consol.(TRM) | #01 | XX |
| A000 | 72550200 | Realized Fx Rate Gains, Affiliat., Consolid.(TRM) | #01 | XX |
| A000 | 72560000 | Gain from FX Valuation, Unaffiliated (TRM) | #01 | XX |
| A000 | 72560100 | Gain from FX Valuation, Affiliat., No Consol.(TRM) | #01 | XX |
| A000 | 72560200 | Gain from FX Valuation, Affiliated, Consolid.(TRM) | #01 | XX |
| A000 | 62001000 | Bad Debt Expense-Individual Value Adjustment(FICA) | #01 | XX |
| A000 | 41005100 | Billed Revenue (FI-CA) | #11 | XX |
| A000 | 44008000 | Sales Deduction (FI-CA) | #12 | XX |
| A000 | 62002000 | Bad Debt Expense-Flat Rate Value Adjustment(FICA) | #01 | XX |
| A000 | 62002100 | Bad Debt Expense Reset - Flat Rate Val Adj.(FICA) | #01 | XX |
| A000 | 62001100 | Bad Debt Expense Reset - Individual Val Adj.(FICA) | #01 | XX |
| A000 | 44008100 | Rev. from Return Payment (FI-CA) | #11 | XX |
| A000 | 70700300 | Leasing Income - Interest (ROU) | #01 | XX |
| A000 | 70700400 | Leasing Income - Sublease (ROU) | #01 | XX |
| A000 | 71055000 | Accrual Statistical Condition | #01 | XX |
| A000 | 72531000 | Gain from Supplier Rebate (MM) | #11 | XX |
| A000 | 72532000 | Gain from Supplier Rebate (SD) | #11 | XX |
| A000 | 94308100 | Service Time | #43 | XX |
| A000 | 44421000 | Rev Adjust for Allocation (RAR) | #11 | XX |
| A000 | 61500100 | Internal Commissions | #01 | XX |
| A000 | 70201000 | Bonds Interest Income, Unaffiliated(TRM) | #01 | XX |
| A000 | 70201100 | Bonds Interest Income, Affili., No Consolid.(TRM) | #01 | XX |
| A000 | 70201200 | Bonds Interest Income, Affili., Consolidat.(TRM) | #01 | XX |
| A000 | 71400300 | Bond Interest Expense(TRM) | #01 | XX |
| A000 | 69999200 | Grants Management Indirect Cost | #01 | XX |
| A000 | 49999200 | Grants Management Indirect Cost Recovery | #01 | XX |
| A000 | 80000000 | Land & Land Improvements - Budget Account | #01 | XX |
| A000 | 80001000 | Buildings - Budget Account | #01 | XX |
| A000 | 80002000 | Machinery & Equipment - Budget Account | #01 | XX |
| A000 | 80003000 | Building Improvements - Budget Account | #01 | XX |
| A000 | 80004000 | Vehicles - Budget Account | #01 | XX |
| A000 | 80005000 | Office Equipment - Budget Account | #01 | XX |
| A000 | 80006000 | Fixtures and Fittings - Budget Account | #01 | XX |
| A000 | 80007000 | Computer Hardware - Budget Account | #01 | XX |
| A000 | 80008000 | Computer Software - Budget Account | #01 | XX |
| A000 | 80009000 | Assets Under Construction - Budget Account | #01 | XX |
| A000 | 80020000 | Low Value Assets - Budget Account | #01 | XX |
| A000 | 69999010 | JV Overhead - % Production Exp. | #01 | XX |
| A000 | 69999011 | JV Overhead Offset - % Production | #01 | XX |
| A000 | 69999020 | JV Overhead - % Development Expense | #01 | XX |
| A000 | 69999021 | JV Overhead Offset - % Development | #01 | XX |
| A000 | 69999030 | JV CFR Prod. Overhead Expense | #01 | XX |
| A000 | 69999031 | JV CFR Overhead Offset - Production | #01 | XX |
| A000 | 69999040 | JV CFR Overhead - Drilling Expense | #01 | XX |
| A000 | 69999041 | JV CFR Overhead Offset - Drilling | #01 | XX |
| A000 | 69999060 | JV Overhead - Construction Expense | #01 | XX |
| A000 | 69999061 | JV Overhead Offset - Construction | #01 | XX |
| A000 | 69999070 | JV Overhead - Exploration Expense | #01 | XX |
| A000 | 69999071 | JV Overhead Offset - Exploration | #01 | XX |
| A000 | 69999080 | JV Capital Drilling Overhead Expense | #01 | XX |
| A000 | 69999081 | JV Capital Drilling Overhead Offset | #01 | XX |
| A000 | 69999090 | JV Overhead - Catastrophe Expense | #01 | XX |
| A000 | 69999091 | JV Overhead Offset - Catastrophe | #01 | XX |
| A000 | 69999100 | JV International Overhead Expense Account | #01 | XX |
| A000 | 69999101 | JV International Overhead Expense Offset Account | #01 | XX |
| A000 | 69999110 | JV Payroll Burden Adjustment | #01 | XX |
| A000 | 69999111 | JV Payroll Burden Clearing Expense | #01 | XX |
| A000 | 69999112 | JV Payroll Burden Clearing Offset | #01 | XX |
| A000 | 69999120 | JV Cutback Tax Clearing | #01 | XX |
| A000 | 69999121 | JV Cutback Tax Expense | #01 | XX |
| A000 | 72010100 | JV Cutback Exchange Difference. | #01 | XX |
| A000 | 61500200 | Royalties for Sales | #01 | XX |
| A000 | 41001530 | Revenue Affil-Royalt | #01 | XX |
| A000 | 66999930 | ICO Expense Royalties | #01 | XX |
| A000 | 70500100 | ARO Consumption of Provision | #01 | XX |
| A000 | 71011000 | Aro Other Expense | #01 | XX |
| A000 | 71101000 | Aro Interest Expense | #01 | XX |
| A000 | 70020100 | ARO Other Revenue | #01 | XX |
| A000 | 62003000 | Bad Debt Expense (Write-Off for FI-CA) | #01 | XX |
| A000 | 70201300 | Dividend Income on Equity Securities(TRM) | #01 | XX |
| A000 | 50309600 | Cost of Sales for Subscribed Services (FI-CA) | #01 | XX |
| A000 | 97777500 | Internal Occupancy Cost Clearing Acc. Real Estate | #01 | XX |
| A000 | 66999910 | ICO Lease Expense - Real Estate | #01 | XX |
| A000 | 66999920 | ICO Service Expense - Real Estate | #01 | XX |
| A000 | 70050100 | ICO Leasing Income - Real Estate | #01 | XX |
| A000 | 70050110 | ICO Service Income - Real Estate | #01 | XX |
| A000 | 70201400 | Div. Income, Non-Affl. Company Inv. (TRM) | #01 | XX |
| A000 | 70201500 | Dividend Income, Ass. or Joint Venture (TRM) | #01 | XX |
| A000 | 70201600 | Dividend Income, Subsidiary (TRM) | #01 | XX |
| A000 | 70220300 | Gain from Equity Method Investment (TRM) | #01 | XX |
| A000 | 70240000 | Non-Operating Income from Equity Method Inv. (TRM) | #01 | XX |
| A000 | 71602000 | Impairment Loss from Equity Investment (TRM) | #01 | XX |
| A000 | 65008600 | Warranty Claims Processing | #01 | XX |
| A000 | 70200300 | ABS/MBS Interest Revenue (TRM) | #01 | XX |
| A000 | 70800300 | Charge Income (IHB) | #01 | XX |
| A000 | 41080000 | Grant Revenue | #11 | XX |
| A000 | 41000000 | Revenue Domestic - Product | #11 | XX |
| A000 | 41001000 | Revenue Foreign - Product | #11 | XX |
| A000 | 41000400 | Sales Revenue w/ Cost Element | #11 | XX |
| A000 | 41001500 | Revenue Affiliate - Product | #11 | XX |
| A000 | 41090000 | Other Operating Revenue | #01 | XX |
| A000 | 44000000 | Over/Underpayments and Unallowed Deductions | #01 | XX |
| A000 | 44001000 | Sales Rebates | #12 | XX |
| A000 | 44002000 | Sales Discounts - Domestic | #12 | XX |
| A000 | 44002100 | Sales Discounts - Foreign | #12 | XX |
| A000 | 44003000 | Customer Sales Deduction - Domestic | #12 | XX |
| A000 | 44003100 | Customer Sales Deduction - Foreign | #12 | XX |
| A000 | 44004000 | Sales Deduction - Material | #12 | XX |
| A000 | 44005000 | Free Goods and Discount in Kind | #12 | XX |
| A000 | 51500000 | Consumption - Packaging Material | #01 | XX |
| A000 | 51600000 | Consumption - Trading Goods | #01 | XX |
| A000 | 51700000 | Consumption - Repair Material | #01 | XX |
| A000 | 51950000 | Consumption - Subcontracting | #01 | XX |
| A000 | 52030000 | Loss from Revaluation | #01 | XX |
| A000 | 52031000 | Loss from Valuation of External Products | #01 | XX |
| A000 | 52041000 | Loss Price Variance (PRD) | #01 | XX |
| A000 | 52060000 | Loss Small Price Differences Invoice Receipt (MM) | #01 | XX |
| A000 | 52080000 | Loss from Allowed Differences GL Account Clearing | #01 | XX |
| A000 | 52530000 | Gain from Revaluation | #01 | XX |
| A000 | 52531000 | Gain from Valuation of External Products | #01 | XX |
| A000 | 52541000 | Gain Price Variance (PRD) | #01 | XX |
| A000 | 52560000 | Gain Small Price Difference Invoices Receipt (Mm) | #01 | XX |
| A000 | 52580000 | Gain from Allowed Differences GL Account Clearing | #01 | XX |
| A000 | 52590000 | Freight Revenue - Recovery | #01 | XX |
| A000 | 54051000 | Inventory Change - Scrap External Products | #01 | XX |
| A000 | 61003000 | Travel Expenses - Hotel and Accommodation | #01 | XX |
| A000 | 61004000 | Travel Expenses - Meals | #01 | XX |
| A000 | 61006000 | Travel Expenses - Entertainment | #01 | XX |
| A000 | 61007000 | Travel Expenses - Airfare, Rail, Mileage | #01 | XX |
| A000 | 61008000 | Travel Expenses - Miscellaneous | #01 | XX |
| A000 | 61010000 | Payroll - Other Personnel Expenses | #01 | XX |
| A000 | 61020000 | Payroll - Bonus | #01 | XX |
| A000 | 61021000 | Payroll - Overtime Salaries | #01 | XX |
| A000 | 61021100 | Payroll - Overtime Wages | #01 | XX |
| A000 | 61022000 | Payroll - Vacation Pay Salaries | #01 | XX |
| A000 | 61022100 | Payroll - Vacation Pay Wages | #01 | XX |
| A000 | 61051000 | Payroll Expense - Downtime Wages | #01 | XX |
| A000 | 61052000 | Payroll Expense - Downtime Salaries | #01 | XX |
| A000 | 61060000 | Payroll Expense - Pension Contributions | #01 | XX |
| A000 | 61061000 | Payroll - Benefits | #01 | XX |
| A000 | 61062000 | Workers' Compensation Association Contributions | #01 | XX |
| A000 | 61063000 | Dues to Associations | #01 | XX |
| A000 | 61100000 | Payroll Expense - Salaries | #01 | XX |
| A000 | 61101000 | Payroll Expense - Other Salary-Related Expenses | #01 | XX |
| A000 | 61102000 | Payroll Expense - Other Wage-Related Expenses | #01 | XX |
| A000 | 61103000 | Payroll Expense - Direct Labor Cost | #01 | XX |
| A000 | 61104000 | Payroll Expense - Indirect Labor Cost | #01 | XX |
| A000 | 61200000 | Payroll Expense - Tax and Soc Security - Wages | #01 | XX |
| A000 | 61201000 | Payroll Expense - Tax and Soc Security - Salaries | #01 | XX |
| A000 | 61500000 | Sales Commissions | #01 | XX |
| A000 | 62000000 | Bad Debt Expense | #01 | XX |
| A000 | 62010000 | Individual Value Adjustments | #01 | XX |
| A000 | 62020000 | Flat-Rate Value Adjustments | #01 | XX |
| A000 | 63000000 | Machine and Equipment Periodic Service | #01 | XX |
| A000 | 63000500 | Qualtiy Control Consumption Ext. Prod. w/ Act Type | #01 | XX |
| A000 | 63001000 | Electricity and Other Utilities | #01 | XX |
| A000 | 63002000 | Water | #01 | XX |
| A000 | 63003000 | Other Periodic Service | #01 | XX |
| A000 | 63004000 | Insurance | #01 | XX |
| A000 | 63005000 | Office/Building Rent | #01 | XX |
| A000 | 63006000 | Telephone and Other Communication | #01 | XX |
| A000 | 63007000 | Fax and Internet | #01 | XX |
| A000 | 63008000 | Building Periodic Service | #01 | XX |
| A000 | 63009000 | Leasing Expense | #01 | XX |
| A000 | 64001000 | Depreciation Expense - Buildings | #01 | XX |
| A000 | 64002000 | Depreciation Expense - Machinery & Equipment | #01 | XX |
| A000 | 64003000 | Depreciation Expense - Building Improvement | #01 | XX |
| A000 | 64004000 | Depreciation Expense - Motor Vehicles | #01 | XX |
| A000 | 64005000 | Depreciation Expense - Office Equipment | #01 | XX |
| A000 | 64006000 | Depreciation Expense - Furniture | #01 | XX |
| A000 | 64007000 | Depreciation Expense - Computer Hardware | #01 | XX |
| A000 | 64008000 | Depreciation Expense - Computer Software | #01 | XX |
| A000 | 64020000 | Depreciation Expense - Low Value Assets | #01 | XX |
| A000 | 64021000 | Depreciation Expense - Intangible Assets | #01 | XX |
| A000 | 64030000 | Unplanned Depreciation Expense | #01 | XX |
| A000 | 64040000 | Scheduled Deprec Fixed Assets Below Asset Value | #01 | XX |
| A000 | 64043000 | Amortization Expense - Goodwill | #01 | XX |
| A000 | 64050000 | Estimated Depreciation (CO) | #01 | XX |
| A000 | 64060000 | Accrued Interest (CO) | #01 | XX |
| A000 | 65000000 | Postage and Shipping | #01 | XX |
| A000 | 65000500 | Non Production - Material Consumption | #01 | XX |
| A000 | 65001000 | Purchased Services | #01 | XX |
| A000 | 65002000 | Advertising and Sales Costs | #01 | XX |
| A000 | 65003000 | Vehicle Costs | #01 | XX |
| A000 | 65004000 | Donations | #01 | XX |
| A000 | 65008000 | Purchased Services-Time | #01 | XX |
| A000 | 65009000 | Other Activity Costs | #01 | XX |
| A000 | 65050000 | Unplanned Delivery Costs | #01 | XX |
| A000 | 65100000 | Office Supplies | #01 | XX |
| A000 | 65150000 | Computer Supplies | #01 | XX |
| A000 | 65200000 | Other Supplies | #01 | XX |
| A000 | 65300000 | Legal and Audit Services | #01 | XX |
| A000 | 65400000 | Freight | #01 | XX |
| A000 | 65900000 | Loss in The Event of Damage | #01 | XX |
| A000 | 66000000 | Other Operating Expenses | #01 | XX |
| A000 | 66000600 | Other Gains | #01 | XX |
| A000 | 66010000 | Expense of Discounting (ZKB) | #01 | XX |
| A000 | 66019900 | Addition to Provisions (ZKK) | #01 | XX |
| A000 | 70015000 | Settlement of Asset U. Construction to CO Object | #01 | XX |
| A000 | 70040000 | Discount Received | #01 | XX |
| A000 | 70100000 | Interest Income | #01 | XX |
| A000 | 70300000 | Interest Income - Subsidiaries | #01 | XX |
| A000 | 70300100 | Gain from Long Term Investment | #01 | XX |
| A000 | 70500000 | Consumption of Provisions | #01 | XX |
| A000 | 70800000 | Other Extraordinary Income | #01 | XX |
| A000 | 70900000 | Fines and Penalties | #01 | XX |
| A000 | 71000000 | Bank Charges | #01 | XX |
| A000 | 71040000 | Discount Lost Using Net Procedure | #01 | XX |
| A000 | 71100000 | Interest Expense | #01 | XX |
| A000 | 71300000 | Interest Expense - Subsidiaries | #01 | XX |
| A000 | 71800000 | Other Extraordinary Expenses | #01 | XX |
| A000 | 72010000 | Loss from Exchange Rate Differences | #01 | XX |
| A000 | 72020000 | Loss from Rounding Dif. Foreign Currency (MM) | #01 | XX |
| A000 | 72040000 | Loss from Currency Valuation | #01 | XX |
| A000 | 72510000 | Gain from Exchange Rate Differences | #01 | XX |
| A000 | 72520000 | Gain from Rounding Dif. Foreign Currency (MM) | #01 | XX |
| A000 | 72530000 | Gain from Rebates Differences | #12 | XX |
| A000 | 72540000 | Gain from Currency Valuation | #01 | XX |
| A000 | 75001000 | Excise Taxes | #01 | XX |
| A000 | 75002000 | Corporate Income Tax Expense | #01 | XX |
| A000 | 75002100 | Capital Gains Tax | #01 | XX |
| A000 | 75003000 | Deferred Tax | #01 | XX |
| A000 | 75004000 | Other Taxes on Income | #01 | XX |
| A000 | 75005000 | Input Tax Non Deductable (NAV) | #01 | XX |
| A000 | 75007000 | Property Taxes | #01 | XX |
| A000 | 93100000 | Result Analysis Technical | #31 | XX |
| A000 | 94308000 | Consulting | #43 | XX |
| A000 | 94311000 | Personnel Hours | #43 | XX |
| A000 | 94201000 | Buildings & Periodic Service | #42 | XX |
| A000 | 94222000 | COPA - Marketing | #42 | XX |
| A000 | 94224000 | COPA - Admin. Overhead | #42 | XX |
| A000 | 94225000 | COPA - Sales. Overhead | #42 | XX |
| A000 | 94226000 | COPA - Non-Operating Expense | #42 | XX |
| A000 | 94227000 | COPA - Non-Operating Income | #42 | XX |
| A000 | 94228000 | COPA - Taxes | #42 | XX |
| A000 | 94229000 | COPA - Cash Discount | #42 | XX |
| A000 | 65008300 | Services - General | #01 | XX |
| A000 | 41003000 | Accrued Revenue - Ebr Adjustment | #12 | XX |
| A000 | 71050000 | Cash Discounts Expense | #01 | XX |
| A000 | 44006000 | Sales Deduction - Menge | #12 | XX |
| A000 | 44002200 | Sales Discounts - Affiliated | #12 | XX |
| A000 | 44003200 | Customer Sales Deduction - Affiliated | #12 | XX |
| A000 | 93111100 | Result Analysis Primary Costs | #31 | XX |
| A000 | 92101800 | Settlement R&D | #21 | XX |
| A000 | 61400000 | Training and Education | #01 | XX |
| A000 | 61401000 | Hr Recruitement | #01 | XX |
| A000 | 61005000 | Travel Expenses - Ground Transportation | #01 | XX |
| A000 | 65301000 | Marketing Expenses | #01 | XX |
| A000 | 93112000 | Result Analysis COP Reserv. | #31 | XX |
| A000 | 93113000 | Result Analysis SEC Costs | #31 | XX |
| A000 | 93114000 | Result Analysis COS Reserv. | #31 | XX |
| A000 | 93115000 | Result Analysis OVH Costs | #31 | XX |
| A000 | 93116000 | Result Analysis OVH Reserv. | #31 | XX |
| A000 | 94113000 | Overhead Administration | #41 | XX |
| A000 | 94114000 | Overhead Sales | #41 | XX |
| A000 | 94202000 | Assessment Quality Costs | #42 | XX |
| A000 | 94304000 | Water | #43 | XX |
| A000 | 94305000 | Industry Effluent | #43 | XX |
| A000 | 94306000 | Environmental | #43 | XX |
| A000 | 94307000 | Internal Transport | #43 | XX |
| A000 | 94309000 | Development | #43 | XX |
| A000 | 94310000 | Qm Control | #43 | XX |
| A000 | 71015000 | Offsetting Account Revaluation Ord. Depreciation | #01 | XX |
| A000 | 52041500 | Loss Inventory Value Adjustment Ext. Prod. (BSK) | #01 | XX |
| A000 | 52070500 | Loss Inventory Value Adjustment Own Prod. (BSK) | #01 | XX |
| A000 | 52541500 | Gain Inventory Value Adjustment Ext. Prod. (BSK) | #01 | XX |
| A000 | 52570500 | Gain Inventory Value Adjustment Own Prod. (BSK) | #01 | XX |
| A000 | 68001000 | Purchase Account (Packaging) | #01 | XX |
| A000 | 68002000 | Purchase Account (Trading) | #01 | XX |
| A000 | 68000000 | Purchase Account (Raw) | #01 | XX |
| A000 | 68010000 | Purchase Account (Sf & Finish Goods) | #01 | XX |
| A000 | 61002000 | 3rd Party Material | #01 | XX |
| A000 | 92105100 | Personnel Costs | #21 | XX |
| A000 | 92105200 | Spare/Service/Ext Material Con | #21 | XX |
| A000 | 92105300 | Other Costs | #21 | XX |
| A000 | 92105400 | Secondary Costs | #21 | XX |
| A000 | 66000500 | Income - Reduction in Provisions | #01 | XX |
| A000 | 54011100 | Inventory Change - Purch.Offset.Acct (Packaging) | #01 | XX |
| A000 | 54011200 | Inventory Change - Purch.Offset.Acct (Trading) | #01 | XX |
| A000 | 64031000 | Depr Expense (Bk Less than Tax) - Exceptional Depr (FR) | #01 | XX |
| A000 | 64032000 | Depr Expense (Bk < Tax) - Exceptional Depr (FR) | #01 | XX |
| A000 | 59900000 | Cost of Goods Sold (Affiliated) | #01 | XX |
| A000 | 75002200 | Solidary Surcharge on Corporate Income Tax | #01 | XX |
| A000 | 75002300 | Solidary Surcharge for Interest Income Tax | #01 | XX |
| A000 | 75008000 | Trade Tax | #01 | XX |
| A000 | 75009000 | Export Duty | #01 | XX |
| A000 | 75009900 | Other Company Taxes | #01 | XX |
| A000 | 44007000 | (-) IPI on Sales (BR) | #12 | XX |
| A000 | 44007001 | (-) ICMS on Sales (BR) | #12 | XX |
| A000 | 44007002 | (-) ISS on Sales (BR) | #12 | XX |
| A000 | 44007003 | (-) PIS on Sales (BR) | #12 | XX |
| A000 | 44007004 | (-) Cofins on Sales (BR) | #12 | XX |
| A000 | 61022040 | Workers' Compensation Assoc. Contributions (AU,BR) | #01 | XX |
| A000 | 61023010 | Payroll - Medical Insurance (CN) | #01 | XX |
| A000 | 61310000 | INSS (Direct Production Cost) (BR) | #01 | XX |
| A000 | 61022010 | Payroll - Sick Pay (AU) | #01 | XX |
| A000 | 61022020 | Payroll - Disability Pay (AU) | #01 | XX |
| A000 | 75008020 | Tax Fringe Benefits Tax (AU) | #01 | XX |
| A000 | 75008050 | Export Taxes (FR) (AU) | #01 | XX |
| A000 | 54441000 | Reserves for Unrealized Costs | #01 | XX |
| A000 | 44420000 | Revenue Adjustment - ERR | #11 | XX |
| A000 | 70010000 | Revenue from Post Capitalization | #01 | XX |
| A000 | 71010200 | Gain from Write Up of Fixed Assets | #01 | XX |
| A000 | 71010700 | Estimated Depreciation (FI-AA) | #01 | XX |
| A000 | 55110000 | Settlement to Fixed Asset (FXA) | #22 | XX |
| A000 | 61023020 | Payroll - Endowment Insurance (CN) | #01 | XX |
| A000 | 61023030 | Payroll - Unemployment Insurance (CN) | #01 | XX |
| A000 | 61023040 | Payroll - Work Injury Insurance (CN) | #01 | XX |
| A000 | 61023050 | Payroll - Housing Fund (CN) | #01 | XX |
| A000 | 61023060 | Payroll - Labor Union Dues and Education Dues (CN) | #01 | XX |
| A000 | 75004010 | Vehicle and Vessels Tax (CN) | #01 | XX |
| A000 | 75004020 | Land Usage Tax (CN) | #01 | XX |
| A000 | 75004030 | Stamp Tax (CN) | #01 | XX |
| A000 | 75004040 | Tax&Addit. Duty (CN) | #01 | XX |
| A000 | 52541100 | Activity Price Diff. Writeoff from WIP (PRA) | #01 | XX |
| A000 | 52541200 | Activity Price Diff. Writeoff from WIP (PRM) | #01 | XX |
| A000 | 64000000 | Depreciation Expense - Land and Land Improvements | #01 | XX |
| A000 | 92101500 | Settl. Rework | #21 | XX |
| A000 | 94111000 | Overhead Material | #41 | XX |
| A000 | 94112000 | Overhead Production | #41 | XX |
| A000 | 94301000 | Machine Hours 1 | #43 | XX |
| A000 | 94302000 | Machine Hours 2 | #43 | XX |
| A000 | 94303000 | Setup Production | #43 | XX |
| A000 | 50307000 | COGS Production Overhead | #01 | XX |
| A000 | 50306000 | COGS Setup Time | #01 | XX |
| A000 | 50305000 | COGS Machine Time | #01 | XX |
| A000 | 50304000 | COGS Personnel Time | #01 | XX |
| A000 | 50303000 | COGS Material Overhead | #01 | XX |
| A000 | 50302000 | COGS Third Party | #01 | XX |
| A000 | 50301000 | COGS Direct Material | #01 | XX |
| A000 | 50308000 | COGS Credits (Co/By-Pr) | #01 | XX |
| A000 | 51100000 | Consumption - Raw Material | #01 | XX |
| A000 | 52001000 | Loss Inventory Variance (Raw & Trade) | #01 | XX |
| A000 | 52003000 | Loss Inventory Variance (Sf & Finish Goods) | #01 | XX |
| A000 | 52011000 | Loss Inventory Transfer (Raw & Trade) | #01 | XX |
| A000 | 52013000 | Loss Inventory Transfer (Sf & Finish Goods) | #01 | XX |
| A000 | 52021000 | Loss Consumption for Quality Control (Raw & Trade) | #01 | XX |
| A000 | 52023000 | Loss Consumption for Quality Control (SF&Fin Gds) | #01 | XX |
| A000 | 52033000 | Loss from Valuation of Own Products | #01 | XX |
| A000 | 52042000 | Loss Price Differences (PRV) | #01 | XX |
| A000 | 52043000 | Loss Price Differences (PRY) | #01 | XX |
| A000 | 52044000 | Loss Price Differences - Material Ledger (LKW) | #01 | XX |
| A000 | 52045000 | Loss Price Differences Own Products (PRK) | #01 | XX |
| A000 | 52046000 | Loss Price Diff Fm Lower Lev.Own Mats ML (PRC) | #01 | XX |
| A000 | 52051000 | Loss Consumption of Consign. Mat (Raw & Trade) | #01 | XX |
| A000 | 52053000 | Loss Consumption of Consign. Mat (SF & F.Goods) | #01 | XX |
| A000 | 52501000 | Gain Inventory Variance (Raw & Trade) | #01 | XX |
| A000 | 52503000 | Gain Inventory Variance (Sf & Finish Goods) | #01 | XX |
| A000 | 52511000 | Gain Inventory Transfer (Raw & Trade) | #01 | XX |
| A000 | 52513000 | Gain Inventory Transfer (SF & Finish Goods) | #01 | XX |
| A000 | 52521000 | Gain Consumption for Quality Control (Raw & Trade) | #01 | XX |
| A000 | 52523000 | Gain Consumption for QM (SF & Finish Goods) | #01 | XX |
| A000 | 52532000 | Gain from Valuation Own Products | #01 | XX |
| A000 | 52542000 | Gain Price Differences (PRV) | #01 | XX |
| A000 | 52543000 | Gain Price Differences (PRY) | #01 | XX |
| A000 | 52544000 | Gain Price Differences - Material Ledger (LKW) | #01 | XX |
| A000 | 52545000 | Posterior Real Rate Activity Allocation (AUI) | #01 | XX |
| A000 | 52551000 | Gain Consumption of Consign. Mat (Raw & Trade) | #01 | XX |
| A000 | 52552000 | Gain Consumption of Consign. Mat (SF & F.Goods) | #01 | XX |
| A000 | 54053000 | Inventory Change - Scrap Own Products | #01 | XX |
| A000 | 54083000 | Inventory Change - Cost of Own Goods Sold W/C.Elem | #01 | XX |
| A000 | 54093000 | Inventory Change - QM Cons.Own Prod. w/ Cst Elem. | #01 | XX |
| A000 | 54300000 | Inventory Change - Semi Finished Goods | #01 | XX |
| A000 | 54400000 | Inventory Change - Finished Goods | #01 | XX |
| A000 | 55100000 | Plant Activity Production Order | #22 | XX |
| A000 | 52070000 | Loss from Production Variances | #01 | XX |
| A000 | 52570000 | Gain from Production Variances | #01 | XX |
| A000 | 54011000 | Inventory Change - Purch.Offset.Acct (Raw) | #01 | XX |
| A000 | 54013000 | Inventory Change - Purch.Offset.Acct (SF & F.Good) | #01 | XX |
| A000 | 54084000 | Inventory Change Cost Own Goods Sold SO Cons. W/CE | #01 | XX |
| A000 | 54200100 | Inventory Change - Work in Progress Event Based | #01 | XX |
| A000 | 41910000 | Billed Revenue Domestic | #11 | XX |
| A000 | 41940000 | Billed Revenue Foreign | #11 | XX |
| A000 | 41970000 | Billed Revenue Affiliated | #11 | XX |
| A000 | 44910000 | Sales Deduction Domestic | #12 | XX |
| A000 | 44940000 | Sales Deduction Foreign | #12 | XX |
| A000 | 44970000 | Sales Deduction Affiliated | #12 | XX |
| A000 | 65008400 | Purchased Services - Accommodation | #01 | XX |
| A000 | 65008410 | Purchased Services - Airfair | #01 | XX |
| A000 | 65008420 | Purchased Services - Ground Transportation | #01 | XX |
| A000 | 65008430 | Purchased Services - Travel Miscellaneous | #01 | XX |
| A000 | 50309000 | COGS - Hardware | #01 | XX |
| A000 | 50309500 | COGS - Licenses | #01 | XX |
| A000 | 41007100 | On-Account Issued (Service Provider) | #01 | XX |
| A000 | 41007200 | On-Account Utilized (Service Provider) | #11 | XX |
| A000 | 97777700 | ICO Margin | #01 | XX |
| A000 | 94308500 | Activity Unit Based Billing | #43 | XX |
| A000 | 59801000 | Reserves for Anticipated Losses | #01 | XX |
| A000 | 44401100 | Revenue Adjustment | #11 | XX |
| A000 | 44405600 | Revenue - on Account Adjustment | #11 | XX |
| A000 | 54442000 | Man Adj of Reserves for Imminent Loss | #01 | XX |
| A000 | 54444000 | Man Adj of Reserves for Unrealized Costs | #01 | XX |
| A000 | 49999900 | Clearing Target Revenue Reallocation | #11 | XX |
| A000 | 61320000 | Expense With Social Sec Contrib Over Revenue (BR) | #12 | BR |
| A000 | 99034600 | EFKA Expense(GR) | #01 | GR |
| A000 | 99034601 | Shared Util.Exp.(GR | #01 | GR |
| A000 | 99034602 | Subscrip. Exp. (GR) | #01 | GR |
| A000 | 99034603 | Other dep.charge(GR) | #01 | GR |
| A000 | 99034400 | Contract Revenue(GR) | #11 | GR |
| A000 | 99034401 | Rentals Revenue(GR) | #11 | GR |
| A000 | 99034604 | Contract Expense(GR) | #01 | GR |
| A000 | 99034402 | Sal. Ret.Gds Dom(GR) | #11 | GR |
| A000 | 99034403 | Sal. Dis.Gds Dom(GR) | #11 | GR |
| A000 | 99034404 | Sal.Est.Ret.GdsD(GR) | #11 | GR |
| A000 | 99034405 | Sales Ret. Goods(GR) | #11 | GR |
| A000 | 99034406 | Sales Dis. Goods(GR) | #11 | GR |
| A000 | 99034407 | Sal. Est.Ret.Gds(GR) | #11 | GR |
| A000 | 99034408 | Sales Scrap Dom.(GR) | #11 | GR |
| A000 | 99034409 | Sal.Raw Mat.Dom.(GR) | #11 | GR |
| A000 | 99034410 | Sal.Pac.Mat.Dom.(GR) | #11 | GR |
| A000 | 99034411 | Sales Expend.Dom(GR) | #11 | GR |
| A000 | 99034412 | Sales Spar. Dom.(GR) | #11 | GR |
| A000 | 99034413 | Sal.Pac.Gds Dom.(GR) | #11 | GR |
| A000 | 99034414 | Sales Scrap (GR) | #11 | GR |
| A000 | 99034415 | Sales Raw Mat. (GR) | #11 | GR |
| A000 | 99034416 | Sales Pac. Mat.(GR) | #11 | GR |
| A000 | 99034417 | Sales Expend.(GR) | #11 | GR |
| A000 | 99034418 | Sales Sp&PackMat(GR) | #11 | GR |
| A000 | 99034419 | Sales Serv.Dom.(GR) | #11 | GR |
| A000 | 99034420 | Sal.Ser.Dis.Dom.(GR) | #11 | GR |
| A000 | 99034421 | Ser.Est.Dis.Dom.(GR) | #11 | GR |
| A000 | 99034422 | Sales Services (GR) | #11 | GR |
| A000 | 99034423 | Sales Serv.Disc.(GR) | #11 | GR |
| A000 | 99034424 | Serv.Est.Disc.(GR) | #11 | GR |
| A000 | 99034425 | Rev.Sales Trans.(GR) | #11 | GR |
| A000 | 99034605 | Self Del. Staff(GR) | #01 | GR |
| A000 | 99034606 | Self Del. 3rdPar.GR) | #01 | GR |
| A000 | 99034607 | SelfDel.Pub.Ben.(GR) | #01 | GR |
| A000 | 99034426 | Self Deliveries(GR) | #01 | GR |
| A000 | 99034428 | Sales of Prod Dom(GR) | #11 | GR |
| A000 | 99034429 | Sal Pr Ded Dom(GR) | #11 | GR |
| A000 | 99034430 | Sal.Pr. EsD.Dom.(GR) | #11 | GR |
| A000 | 99034431 | Sales Prod. Ret.(GR) | #11 | GR |
| A000 | 99034432 | Sales Prod. Ded.(GR) | #11 | GR |
| A000 | 99034433 | Sales Pr.EstDed.(GR) | #11 | GR |
| A000 | 99034434 | Sales Prod. Dom(GR) | #11 | GR |
| A000 | 99034435 | Sales Products(GR) | #11 | GR |
| A000 | 99034436 | Sales Reb. Dom.(GR) | #11 | GR |
| A000 | 99034437 | Sales Rebates(GR) | #11 | GR |
| A000 | 99034438 | Sal.Prod.Red.Dom(GR) | #11 | GR |
| A000 | 99034439 | Sal.Prod.Reduct.(GR) | #11 | GR |
| A000 | 99034440 | Rev.Sal.Pr.Aff.(GR) | #11 | GR |
| A000 | 99034441 | Sales Prod. Aff.(GR) | #11 | GR |
| A000 | 99034442 | Sal.Pr.Disc.Aff.(GR) | #11 | GR |
| A000 | 99034443 | SPr.Cust.Disc.Af(GR) | #11 | GR |
| A000 | 99034444 | Sales Pr.Red.Aff(GR) | #11 | GR |
| A000 | 99034608 | Own Use Expense(GR) | #01 | GR |
| A000 | 99034609 | CostsRetail Dom(GR) | #01 | GR |
| A000 | 99034610 | Prov.Retail Dom(GR) | #01 | GR |
| A000 | 99034611 | Rent – Expense(GR) | #01 | GR |
| A000 | 99034427 | Damaged Stock (GR) | #01 | GR |
| A000 | 75005010 | Non-Deductable Input Tax Expense (HU) | #1 | HU |
| A000 | 99035600 | CGSMC-Biological assets (purchases) *(PT) | #01 | PT |
| A000 | 99035601 | ESS-Specialized Serv-Surveillance and Security(PT) | #01 | PT |
| A000 | 99035602 | ESS-Specialized services-Fees(PT) | #01 | PT |
| A000 | 99035603 | ESS-Specialized services-Commissions(PT) | #01 | PT |
| A000 | 99035605 | ESS-Materials-Books and Technical Documentatio(PT) | #01 | PT |
| A000 | 99035606 | ESS-Materials-Gift Items(PT) | #01 | PT |
| A000 | 99035607 | ESS-Materials-Oths(PT) | #01 | PT |
| A000 | 99035608 | ESS-Energy and fluids-Fuels(PT) | #01 | PT |
| A000 | 99035609 | ESS-Energy and fluids-Oths(PT) | #01 | PT |
| A000 | 99035610 | ESS-Travel,stays,transport-Personnel transport(PT) | #01 | PT |
| A000 | 99035611 | ESS-Travel, stays and transport-Oths(PT) | #01 | PT |
| A000 | 99035612 | ESS-Miscellaneous Services-Royalties(PT) | #01 | PT |
| A000 | 99035613 | ESS-Miscellaneous servic-Litigation and notary(PT) | #01 | PT |
| A000 | 99035614 | ESS-Miscellaneous serv-Representation expenses(PT) | #01 | PT |
| A000 | 99035615 | ESS-Miscell serv-Cleanliness,hygiene,comfort(PT) | #01 | PT |
| A000 | 99035616 | ESS-Miscellaneous services-Oth services(PT) | #01 | PT |
| A000 | 99035617 | StaffExp-Post-employment benefits-Oth benefits(PT) | #01 | PT |
| A000 | 99035618 | StaffExp-Compensation(PT) | #01 | PT |
| A000 | 99035619 | StaffExp-Social Action Expenses(PT) | #01 | PT |
| A000 | 99035620 | DepAExp-InvProp-Land and natural resources(PT) | #01 | PT |
| A000 | 99035621 | DepAExp-InvProp-Buildings and Oth construction(PT) | #01 | PT |
| A000 | 99035622 | DepAExp-InvProp-Oth InvProp(PT) | #01 | PT |
| A000 | 99035623 | DepAExp-TangFixedAssets-Biological equipment(PT) | #01 | PT |
| A000 | 99035624 | DepAExp-TangFixedAssets-Oth TangFixedAssets(PT) | #01 | PT |
| A000 | 99035625 | DepAExp-IntangAssets-Development projects(PT) | #01 | PT |
| A000 | 99035626 | DepAExp-IntangAssets-Industrial property(PT) | #01 | PT |
| A000 | 99035627 | DepAExp-Biological assets-Consumables(PT) | #01 | PT |
| A000 | 99035628 | DepAExp-Biological assets-Production(PT) | #01 | PT |
| A000 | 99035629 | DepAExp-finc Invest-Goodwill (PT) | #01 | PT |
| A000 | 99035630 | IL-finc Instruments(PT) | #01 | PT |
| A000 | 99035631 | IL-In receivables-Cust(PT) | #01 | PT |
| A000 | 99035632 | IL-In receivables-Oth debtors(PT) | #01 | PT |
| A000 | 99035633 | IL-In inventories-Goods(PT) | #01 | PT |
| A000 | 99035638 | IL-In inventories-Consumable biological assets(PT) | #01 | PT |
| A000 | 99035639 | IL-In inventories-Production biological assets(PT) | #01 | PT |
| A000 | 99035640 | IL-In finc Invest-Equity Invest(PT) | #01 | PT |
| A000 | 99035641 | IL-In finc Invest-Loans granted(PT) | #01 | PT |
| A000 | 99035642 | IL-In finc Invest-Oth finc Invest(PT) | #01 | PT |
| A000 | 99035643 | IL-In finc Invest-Goodwill(PT) | #01 | PT |
| A000 | 99035644 | IL-On invest property-Land and natural resourc(PT) | #01 | PT |
| A000 | 99035645 | IL-On inves property-Build and Oth constructio(PT) | #01 | PT |
| A000 | 99035646 | IL-On InvProp-Oth InvProp(PT) | #01 | PT |
| A000 | 99035647 | IL-In TangFixedAssets-Land and natural resourc(PT) | #01 | PT |
| A000 | 99035648 | IL-In TangFixedAssets-Buildings Oth construc(PT) | #01 | PT |
| A000 | 99035650 | IL-In TangFixedAssets-Transport equipment(PT) | #01 | PT |
| A000 | 99035651 | IL-In TangFixedAssets-Administrative equipment(PT) | #01 | PT |
| A000 | 99035652 | IL-In TangFixedAssets-Biological equipment(PT) | #01 | PT |
| A000 | 99035653 | IL-Oth property,plant,equipment(PT) | #01 | PT |
| A000 | 99035654 | IL-In IntangAssets-Goodwill(PT) | #01 | PT |
| A000 | 99035655 | IL-In IntangAssets-Development projects(PT) | #01 | PT |
| A000 | 99035656 | IL-In IntangAssets-Computer programs(PT) | #01 | PT |
| A000 | 99035657 | IL-In IntangAssets-Industrial property(PT) | #01 | PT |
| A000 | 99035658 | IL-In IntangAssets-Oth IntangAssets(PT) | #01 | PT |
| A000 | 99035659 | IL-InvestProgr-finc InvestProgr(PT) | #01 | PT |
| A000 | 99035660 | IL-On InvestProgr-InvProp in progress(PT) | #01 | PT |
| A000 | 99035661 | IL-On InvestProgr-tang assets in progress(PT) | #01 | PT |
| A000 | 99035662 | IL-On InvestProgr-IntangAssets in progress(PT) | #01 | PT |
| A000 | 99035663 | IL-On InvProgr-AdAcInv-finc InvestProgr(PT) | #01 | PT |
| A000 | 99035664 | IL-On InvProgr-AdAcInv-Prop of invest in progr(PT) | #01 | PT |
| A000 | 99035665 | IL-On InvProgr-AdAcInv-TangFixAsset in progres(PT) | #01 | PT |
| A000 | 99035666 | IL-On InvProgr-AdAcInv-IntangAssets in progres(PT) | #01 | PT |
| A000 | 99035667 | IL-On non-cur assets held for sale-finc Invest(PT) | #01 | PT |
| A000 | 99035668 | IL-On non-cur assets held for sale-InvProp(PT) | #01 | PT |
| A000 | 99035669 | IL-On non-cur asset held sale-TangFixedAsset(PT) | #01 | PT |
| A000 | 99035670 | IL-In non-cur assets held for sale-IntangAsset(PT) | #01 | PT |
| A000 | 99035671 | IL-On non-cur assets held for sale-Oth(PT) | #01 | PT |
| A000 | 99035672 | LosFairValueReductions-IFinc instruments(PT) | #01 | PT |
| A000 | 99035673 | LosFairValueReductions-IFincInv-Eq Invest(PT) | #01 | PT |
| A000 | 99035674 | LosFairValueReduct-IFincInv-Oth finc Invest(PT) | #01 | PT |
| A000 | 99035675 | LosFairValuRed-InvProp-Land natural resourc(PT) | #01 | PT |
| A000 | 99035676 | LosFairValueRed-InvProp-Buildings Oth construc(PT) | #01 | PT |
| A000 | 99035677 | LosFairValueRed-InvProp-Oth investment propert(PT) | #01 | PT |
| A000 | 99035678 | LosFairValueRed-InvProp-InvProperty in progres(PT) | #01 | PT |
| A000 | 99035679 | LosFairValueRed-In biological assets-Consumabl(PT) | #01 | PT |
| A000 | 99035680 | LosFairValueRed-In biological assets-Productio(PT) | #01 | PT |
| A000 | 99035681 | ProvTaxes(PT) | #01 | PT |
| A000 | 99035682 | Period Provisions-Guarantees to Cust(PT) | #01 | PT |
| A000 | 99035683 | ProvLegal proceedings in progress(PT) | #01 | PT |
| A000 | 99035684 | ProvAccident at work and occupat disease(PT) | #01 | PT |
| A000 | 99035685 | ProvEnvironmental matters(PT) | #01 | PT |
| A000 | 99035686 | ProvOnerous Contracts(PT) | #01 | PT |
| A000 | 99035687 | ProvRestructuring(PT) | #01 | PT |
| A000 | 99035688 | ProvOth provisions(PT) | #01 | PT |
| A000 | 99035689 | OExp-Taxes-Direct taxes(PT) | #01 | PT |
| A000 | 99035690 | OExp-Taxes-Indirect taxes(PT) | #01 | PT |
| A000 | 99035691 | OExp-Taxes-Fees(PT) | #01 | PT |
| A000 | 99035692 | OExp-Inventory losses-Claims(PT) | #01 | PT |
| A000 | 99035693 | OExp-Inventory losses-Breakdowns(PT) | #01 | PT |
| A000 | 99035694 | OExp-Inventory losses-Oth losses(PT) | #01 | PT |
| A000 | 99035695 | OExp-ExpSubsid,assoc,joint ventur-Loss coverag(PT) | #01 | PT |
| A000 | 99035696 | OExp-ExpSubsid,assoc,joint vent-EqMeth applica(PT) | #01 | PT |
| A000 | 99035697 | OExp-ExpSubsid,assoc,joint ventures-Disposals(PT) | #01 | PT |
| A000 | 99035698 | OExp-ExpSubsid,assoc,joint ventures-Oexp(PT) | #01 | PT |
| A000 | 99035699 | OExp-Exp on Oth finc Invest-Loss coverage(PT) | #01 | PT |
| A000 | 99035900 | OExp-Exp on Oth finc Invest-Disposals(PT) | #01 | PT |
| A000 | 99035901 | OExp-ExpOFincInvest-Unfavorable exchange diff(PT) | #01 | PT |
| A000 | 99035902 | OExp-Exp on Oth finc Invest-Oexp(PT) | #01 | PT |
| A000 | 99035903 | OExp-Exp on non-finc Invest-Disposals(PT) | #01 | PT |
| A000 | 99035904 | OExp-Exp on non-finc Invest-Claims(PT) | #01 | PT |
| A000 | 99035905 | OExp-Exp on non-finc Invest-Kills(PT) | #01 | PT |
| A000 | 99035906 | OExp-Non-finc Inv Exp-Investment Property Exp(PT) | #01 | PT |
| A000 | 99035907 | OExp-Expenses on non-finc Invest-Oexp(PT) | #01 | PT |
| A000 | 99035908 | OExp-Oth-Corrections to prior periods(PT) | #01 | PT |
| A000 | 99035909 | OExp-Oth-Quota contributions(PT) | #01 | PT |
| A000 | 99035910 | OExp-Oths-Offers and inventory samples(PT) | #01 | PT |
| A000 | 99035911 | OExp-Oth-Insufficient tax estimate(PT) | #01 | PT |
| A000 | 99035912 | OExp-Oth-Losses on finc instruments(PT) | #01 | PT |
| A000 | 99035913 | OExp-Oth-Oth not specified(PT) | #01 | PT |
| A000 | 99035914 | FIExp-Interest paid-Interest on Finc obt(PT) | #01 | PT |
| A000 | 99035915 | FIExp-Unfavorab exchange diff-Relat to Finc ob(PT) | #01 | PT |
| A000 | 99035916 | FIExp-Unfavorable exchange differences-Oth(PT) | #01 | PT |
| A000 | 99035917 | FIExp-Oth FIExp-Relative to Finc obt(PT) | #01 | PT |
| A000 | 99035918 | FIExp-Oth FIExp-Oth(PT) | #01 | PT |
| A000 | 99035400 | Sales-Fin/Inter Prod(PT) | #11 | PT |
| A000 | 99035401 | Sales-Subproducts, wastes, refuse and scrap(PT) | #11 | PT |
| A000 | 99035402 | Sales-Biological Assets(PT) | #11 | PT |
| A000 | 99035403 | Sales-VAT from sales with tax included(PT) | #11 | PT |
| A000 | 99035404 | Sales-Sales Returns(PT) | #11 | PT |
| A000 | 99035405 | Services-Secondary Services(PT) | #01 | PT |
| A000 | 99035406 | Services-VAT of services with tax included(PT) | #01 | PT |
| A000 | 99035407 | Services-Discounts and rebates(PT) | #01 | PT |
| A000 | 99035700 | VarProdInvent-Products and work in progress(PT) | #01 | PT |
| A000 | 99035701 | VarProdInvent-Biological assets(PT) | #01 | PT |
| A000 | 99035702 | Own work-TangFixedAssets(PT) | #01 | PT |
| A000 | 99035703 | Own work-IntangAssets(PT) | #01 | PT |
| A000 | 99035704 | Own work-InvProp(PT) | #01 | PT |
| A000 | 99035705 | Own work-Deferred charges assets(PT) | #01 | PT |
| A000 | 99035706 | Operating subsidies-Government subsidies(PT) | #01 | PT |
| A000 | 99035707 | Operating Subsidies-Subsidies from Oth Entitie(PT) | #01 | PT |
| A000 | 99035708 | Rev-DepAmortProp-Land and Natural Resources(PT) | #01 | PT |
| A000 | 99035709 | Rev-DepAmortProp-Building and Oth Construction(PT) | #01 | PT |
| A000 | 99035710 | Rev-DepAmortProp-Oth InvProp(PT) | #01 | PT |
| A000 | 99035711 | Rev-DepAmortTangFixAsset-Land Natural Resourc(PT) | #01 | PT |
| A000 | 99035712 | Rev-DepATangFixAsset-Buildings Oth construct(PT) | #01 | PT |
| A000 | 99035713 | Rev-DepAmortTangFixedAssets-Basic Equipment(PT) | #01 | PT |
| A000 | 99035714 | Rev-DepAmortTangFixedAssets-Transport Equipmen(PT) | #01 | PT |
| A000 | 99035715 | Rev-DepATangFixeAsset-Administrative Equipment(PT) | #01 | PT |
| A000 | 99035716 | Rev-DepATangFixedAssets-Biological Equipment(PT) | #01 | PT |
| A000 | 99035717 | Rev-DepATangFixedAssets-Oth TangFixedAssets(PT) | #01 | PT |
| A000 | 99035718 | Rev-DepAIntangAssets-Goodwill(PT) | #01 | PT |
| A000 | 99035719 | Rev-DepAIntangAssets-Development Projects(PT) | #01 | PT |
| A000 | 99035720 | Rev-DepAIntangAssets-Computer Programs(PT) | #01 | PT |
| A000 | 99035721 | Rev-DepAIntangAssets-Industrial Property(PT) | #01 | PT |
| A000 | 99035722 | Rev-DepAIntangAssets-Oth IntangAssets(PT) | #01 | PT |
| A000 | 99035723 | Rev-DepABiological Assets-Consumables(PT) | #01 | PT |
| A000 | 99035724 | Rev-DepABiological Assets-Production(PT) | #01 | PT |
| A000 | 99035725 | Rev-DepAfinc Invest-Goodwill(PT) | #01 | PT |
| A000 | 99035726 | Rev-IL-In receivables-Cust(PT) | #01 | PT |
| A000 | 99035727 | Rev-IL-In receivables-Oth debtors(PT) | #01 | PT |
| A000 | 99035728 | Rev-Of IL-In inventories-Goods(PT) | #01 | PT |
| A000 | 99035729 | Rev-IL-IInv-Raw material,subsid,consumables(PT) | #01 | PT |
| A000 | 99035730 | Rev-IL-In inventories-Fin/Inter Prod(PT) | #01 | PT |
| A000 | 99035731 | Rev-From IL-Iinv-Subprod,wastes,scrap(PT) | #01 | PT |
| A000 | 99035732 | Rev-IL-IInv-Products and work in progress(PT) | #01 | PT |
| A000 | 99035733 | Rev-IL-IInv-Consumable biological assets(PT) | #01 | PT |
| A000 | 99035734 | Rev-IL-IInv-Production biological assets(PT) | #01 | PT |
| A000 | 99035735 | Rev-IL-In finc Invest-Equity Invest(PT) | #01 | PT |
| A000 | 99035736 | Rev-IL-In finc Invest-Loans granted(PT) | #01 | PT |
| A000 | 99035737 | Rev-IL-In finc Invest-Oth finc Invest(PT) | #01 | PT |
| A000 | 99035738 | Rev-IL-On investment property-Land and natural(PT) | #01 | PT |
| A000 | 99035739 | Rev-IL-OInvProp-Buildings and Oth construction(PT) | #01 | PT |
| A000 | 99035740 | Rev-IL-OInvProp-Oth InvProp(PT) | #01 | PT |
| A000 | 99035741 | Rev-IL-ITangFixdAsset-Land Natural Resources(PT) | #01 | PT |
| A000 | 99035742 | Rev-IL-ITangFixAsset-Buildings Oth construct(PT) | #01 | PT |
| A000 | 99035743 | Rev-IL-ITangFixAssets-Basic equipment(PT) | #01 | PT |
| A000 | 99035744 | Rev-IL-ITangFixAssets-Transport equipment(PT) | #01 | PT |
| A000 | 99035745 | Rev-IL-ITangFixAssets-Administrative equipment(PT) | #01 | PT |
| A000 | 99035746 | Rev-IL-ITangFixAssets-Biological equipment(PT) | #01 | PT |
| A000 | 99035747 | Rev-IL-ITangFixAssets-Oth TangFixedAssets(PT) | #01 | PT |
| A000 | 99035748 | Rev-IL-IntangAssets-Development projects(PT) | #01 | PT |
| A000 | 99035749 | Rev-Of IL-IIntangAssets-Computer programs(PT) | #01 | PT |
| A000 | 99035750 | Rev-IL-IntangAssets-Industrial property(PT) | #01 | PT |
| A000 | 99035751 | Rev-IL-IIntangAssets-Oth IntangAssets(PT) | #01 | PT |
| A000 | 99035752 | Rev-IL-On InvestProgr-finc InvestProgr(PT) | #01 | PT |
| A000 | 99035753 | Rev-IL-On InvestProgr-InvProp in progress(PT) | #01 | PT |
| A000 | 99035754 | Rev-IL-OInvestProgr-TangFixedAssets in progres(PT) | #01 | PT |
| A000 | 99035755 | Rev-IL-On InvestProgr-IntangAssets in progress(PT) | #01 | PT |
| A000 | 99035756 | Rev-IL-On InvProgr-AdAcInv-finc InvestProgr(PT) | #01 | PT |
| A000 | 99035757 | Rev-IL-OInvProgr-AdAcInv-Prop invest in progre(PT) | #01 | PT |
| A000 | 99035758 | Rev-IL-InvProgr-AdAcInv-TangFixAsset in progre(PT) | #01 | PT |
| A000 | 99035759 | Rev-IL-InvProgr-AdAcInv-IntangAssets in prog(PT) | #01 | PT |
| A000 | 99035760 | Rev-IL-In non-cur assets held for sale-FInvest(PT) | #01 | PT |
| A000 | 99035761 | Rev-IL-On non-cur assets held for sale-InvProp(PT) | #01 | PT |
| A000 | 99035762 | Rev-IL-non-cur asset held for sale-TangFixAsse(PT) | #01 | PT |
| A000 | 99035763 | Rev-IL-In non-cur asset held f sale-IntangAsse(PT) | #01 | PT |
| A000 | 99035764 | Rev-IL-non-cur assets held for sale-Oth(PT) | #01 | PT |
| A000 | 99035765 | Rev-Provisions-Taxes(PT) | #01 | PT |
| A000 | 99035766 | Rev-Provisions-Guarantees to Cust(PT) | #01 | PT |
| A000 | 99035767 | Rev-Provisions-Legal Proceedings(PT) | #01 | PT |
| A000 | 99035768 | Rev-Prov-Accid at work and occupational diseas(PT) | #01 | PT |
| A000 | 99035769 | Rev-Prov-Environmental Matters(PT) | #01 | PT |
| A000 | 99035770 | Rev-Prov-Onerous Contracts(PT) | #01 | PT |
| A000 | 99035771 | Rev-Prov-Restructuring(PT) | #01 | PT |
| A000 | 99035772 | Rev-Prov-Oth Prov(PT) | #01 | PT |
| A000 | 99035773 | GainFairValueIncr-In finc instruments(PT) | #01 | PT |
| A000 | 99035774 | GainFairValueIncr-In finc Invest-Eq interests(PT) | #01 | PT |
| A000 | 99035775 | GainFairValueIncr-In finc Inv-Oth finc Invest(PT) | #01 | PT |
| A000 | 99035776 | GainFairValueIncr-IProp-Land natural resources(PT) | #01 | PT |
| A000 | 99035777 | GainFairValueIncr-IProp-Buildings Oth construc(PT) | #01 | PT |
| A000 | 99035778 | FairValueGain-On InvProp-Oth InvProp(PT) | #01 | PT |
| A000 | 99035779 | FairValueGain-On InvProp-InvProp in progress(PT) | #01 | PT |
| A000 | 99035780 | GainFairValueIncr-Biological assets-Consumable(PT) | #01 | PT |
| A000 | 99035781 | GainFairValueIncr-Biological assets-Production(PT) | #01 | PT |
| A000 | 99035782 | OInc-Supplementary income-Social services(PT) | #01 | PT |
| A000 | 99035783 | OInc-Extra income-Equipment rental(PT) | #01 | PT |
| A000 | 99035784 | OInc-SupInc-Stud,proj,technological assistance(PT) | #01 | PT |
| A000 | 99035785 | OInc-Supplementary income-Royalties(PT) | #01 | PT |
| A000 | 99035786 | OInc-SupplInc-Perf corp posit in Oth companies(PT) | #01 | PT |
| A000 | 99035787 | OInc-Suppl income-Oth supplementary income(PT) | #01 | PT |
| A000 | 99035788 | OInc-Debt recovery(PT) | #01 | PT |
| A000 | 99035789 | OInc-Inventory gains-Claims(PT) | #01 | PT |
| A000 | 99035790 | OInc-Inventory gains-Leftovers(PT) | #01 | PT |
| A000 | 99035791 | OInc-Gains on inventories-Oth earnings(PT) | #01 | PT |
| A000 | 99035792 | OInc-IncSubs,assoc,joint vent-Application of t(PT) | #01 | PT |
| A000 | 99035793 | OInc-IncSubs,assoc,joint ventures-Disposals(PT) | #01 | PT |
| A000 | 99035794 | OInc-IncSubs,assoc,joint ventures-Oinc(PT) | #01 | PT |
| A000 | 99035795 | OInc-IncOFincAssets-Fav exchange rate differen(PT) | #01 | PT |
| A000 | 99035796 | OInc-Income from Oth finc assets-Disposals(PT) | #01 | PT |
| A000 | 99035797 | OInc-Income from Oth finc assets-Oinc(PT) | #01 | PT |
| A000 | 99035798 | OInc-Income from non-finc Invest-Disposals(PT) | #01 | PT |
| A000 | 99035799 | OInc-Income from non-finc Invest-Claims(PT) | #01 | PT |
| A000 | 99035950 | OInc-IncNon-finc Inv-Inc OInc from inv propert(PT) | #01 | PT |
| A000 | 99035951 | OInc-Income from non-finc Invest-Oinc(PT) | #01 | PT |
| A000 | 99035952 | OInc-Oth-Corrections to prior periods(PT) | #01 | PT |
| A000 | 99035953 | OInc-Oth-Exceeding tax estimate(PT) | #01 | PT |
| A000 | 99035954 | OInc-Oth-Investment allowance allocation(PT) | #01 | PT |
| A000 | 99035955 | OInc-Oth-Gains on Oth finc inst(PT) | #01 | PT |
| A000 | 99035956 | OInc-Oth-Tax Refund(PT) | #01 | PT |
| A000 | 99035957 | OInc-Oth-Oth unspecified(PT) | #01 | PT |
| A000 | 99035958 | Int, divid Oth similar inc-Interest earned-Dep(PT) | #01 | PT |
| A000 | 99035959 | Int,div OSimilar inc-Int earn-From Oth cash In(PT) | #01 | PT |
| A000 | 99035960 | IDOSI-Int obt-From Finc grant assoc joint vent(PT) | #01 | PT |
| A000 | 99035961 | IDOSI-Interest obt-Finc granted to subsidiarie(PT) | #01 | PT |
| A000 | 99035962 | IDOSI-Interest obt-Finc obt(PT) | #01 | PT |
| A000 | 99035963 | IDOSI-Interest earned-Oth Finc granted(PT) | #01 | PT |
| A000 | 99035964 | IDOSI-Divid earned-From cash Invest(PT) | #01 | PT |
| A000 | 99035965 | IDOSI-Divid earned-From assoc and joint ventur(PT) | #01 | PT |
| A000 | 99035966 | IDOSI-Divid earned-From subsidiaries(PT) | #01 | PT |
| A000 | 99035967 | Int, divid Oth similar income-Divid obt-Oth(PT) | #01 | PT |
| A000 | 99035968 | IDOSI-Favorable exchange rate differences(PT) | #01 | PT |
| A000 | 99035969 | Int, divid Oth similar incom-Oth similar incom(PT) | #01 | PT |
| A000 | 99035919 | ESS-Materials-Fast Wear Tools & Utensils(PT) | #01 | PT |
| A000 | 99035920 | Payroll Expense - Social Bodies(PT) | #01 | PT |
| A000 | 99035635 | IL-In inventories-Fin/Inter Prod(PT) | #01 | PT |
| A000 | 99035636 | IL-In invent-Subprod,wastes,residues and scrap(PT) | #01 | PT |
| A000 | 99035637 | IL-In inventories-Products and work in progres(PT) | #01 | PT |
| A000 | 52013100 | Loss Inventory Transfer (WH WIP) (SK) | #01 | SK |
| A000 | 52023100 | Loss Consumption for QC (WH WIP) (SK) | #01 | SK |
| A000 | 52033100 | Loss from Valuation of Own Products - WH WIP (SK) | #01 | SK |
| A000 | 52041010 | Loss Price Variance WH WIP (PRD) (SK) | #01 | SK |
| A000 | 52043100 | Loss Price Differences WH WIP (PRY) (SK) | #01 | SK |
| A000 | 52070100 | Loss Production Variance WH WIP (SK) | #01 | SK |
| A000 | 52070510 | Loss Inventory Value Adjustment (WH WIP) (SK) | #01 | SK |
| A000 | 52513100 | Gain Inventory Transfer (WH WIP) (SK) | #01 | SK |
| A000 | 52523100 | Gain Consumption for QC (WH WIP) (SK) | #01 | SK |
| A000 | 52532100 | Gain from Valuation of Own Products - WH WIP (SK) | #01 | SK |
| A000 | 52545100 | Posterior Real Estate Acti Alloc WH WIP (AUI)(SK) | #01 | SK |
| A000 | 52543100 | Gain Price Differences WH WIP (PRY) (SK) | #01 | SK |
| A000 | 52541010 | Gain Price Variance WH WIP (PRD) (SK) | #01 | SK |
| A000 | 52570100 | Gain Production Variance WH WIP (SK) | #01 | SK |
| A000 | 52570510 | Gain Inventory Value Adjustment (WH WIP) (SK) | #01 | SK |
| A000 | 54083100 | Inventory Change – Cost of Own Goods Sold w/o CE | #01 | SK |
| A000 | 54093100 | Inventory change – QMWH WIP w/ cst elem. (SK) | #01 | SK |
| A000 | 55100100 | Plant Activity, Production Order WH WIP  (SK) | #22 | SK |
| A000 | 65000510 | Non Production – Material Consumption WH WIP (SK) | #01 | SK |
| A000 | 52003100 | Loss Inventory Variance (WH WIP) (SK) | #01 | SK |
| A000 | 52044100 | Loss Price Diff - Mat Ledger (LKW) - WH WIP (SK) | #01 | SK |
| A000 | 52503100 | Gain Inventory Variance (WH WIP) (SK) | #01 | SK |
| A000 | 54053100 | Invent Change - Scrap Own Prod- WH WIP (PRD) (SK) | #01 | SK |
| A000 | 54400100 | Inventory Change - WH WIP  (SK) | #01 | SK |
| A000 | 52544100 | Gain Price Diff - Mat Ledger (LKW) - WH WIP (SK) | #01 | SK |
| A000 | 54084100 | Inv Change - COGS for SO Cons W/C El WH WIP  (SK) | #01 | SK |
| A000 | 44007010 | Sales Returns (TR) | #12 | TR |
| A000 | 41000020 | Revenue Domestic - Trading Goods (UA) | #11 | UA |
| A000 | 41001020 | Revenue Foreign - Trading Goods (UA) | #11 | UA |
| A000 | 41001520 | Revenue Affiliate - Trading Goods (UA) | #11 | UA |
| A000 | 99065501 | Cost of Works and Services (UA) | #1 | UA |
| A000 | 99065502 | Cost of Work and Services (Affiliated) (UA) | #1 | UA |

### Sheet: Cost Element Groups

| Group First Level | Group Second Level | Group Third Level | Group Fourth level | Group Fifth Level | Group Name | Cost Element | Cost Element Name |
| --- | --- | --- | --- | --- | --- | --- | --- |
| YBA000_CE | Cost elements summary Best Practices |  |  |  |  |  |  |
|  | 10_CE | Costs Best Practices |  |  |  |  |  |
|  |  | 100_CE | Primary costs |  |  |  |  |
|  |  |  | 1100_CE |  | Personnel expenses |  |  |
|  |  |  |  |  |  | 61010000 | Payroll - Other Personnel Expenses |
|  |  |  |  |  |  | 61020000 | Payroll - Bonus |
|  |  |  |  |  |  | 61021000 | Payroll - Overtime Salaries |
|  |  |  |  |  |  | 61022000 | Payroll - Vacation Pay Salaries |
|  |  |  |  |  |  | 61051000 | Payroll Expense - Downtime Wages |
|  |  |  |  |  |  | 61052000 | Payroll Expense - Downtime Salaries |
|  |  |  |  |  |  | 61060000 | Payroll Expense - Pension Contributions |
|  |  |  |  |  |  | 61061000 | Payroll - Benefits |
|  |  |  |  |  |  | 61100000 | Payroll Expense - Salaries |
|  |  |  |  |  |  | 61101000 | Payroll Expense - Other Salary-Related Expenses |
|  |  |  |  |  |  | 61102000 | Payroll Expense - Other Wage-Related Expenses |
|  |  |  |  |  |  | 61103000 | Payroll Expense - Direct Labor Cost |
|  |  |  |  |  |  | 61104000 | Payroll Expense - Indirect Labor Cost |
|  |  |  |  |  |  | 61200000 | Payroll Expense - Tax and Soc Security - Wages |
|  |  |  |  |  |  | 61201000 | Payroll Expense - Tax and Soc Security - Salaries |
|  |  |  |  |  |  | 61021100 | Payroll - Overtime Wages |
|  |  |  |  |  |  | 61022100 | Payroll - Vacation Pay Wages |
|  |  |  |  |  |  | 61062000 | Workers' Compensation Association Contributions |
|  |  |  |  |  |  | 61063000 | Dues to Associations |
|  |  |  |  |  |  | 61401000 | Hr Recruitement |
|  |  |  |  |  |  | 61022010 | Payroll - Sick Pay (AU) |
|  |  |  |  |  |  | 61022020 | Payroll - Disability Pay (AU) |
|  |  |  |  |  |  | 61022040 | Workers' Compensation Assoc. Contributions (AU,BR) |
|  |  |  | 1200_CE |  | Production costs materials |  |  |
|  |  |  |  |  |  | 51500000 | Consumption - Packaging Material |
|  |  |  |  |  |  | 51700000 | Consumption - Repair Material |
|  |  |  |  |  |  | 51600000 | Consumption - Trading Goods |
|  |  |  |  |  |  | 51950000 | Consumption - Subcontracting |
|  |  |  |  |  |  | 54051000 | Inventory Change - Scrap External Products |
|  |  |  |  |  |  | 63000500 | Qualtiy Control Consumption Ext. Prod. w/ Act Type |
|  |  |  |  |  |  | 65000500 | Non Production - Material Consumption |
|  |  |  |  |  |  | 68001000 | Purchase Account (Packaging) |
|  |  |  |  |  |  | 68002000 | Purchase Account (Trading) |
|  |  |  |  |  |  | 68000000 | Purchase Account (Raw) |
|  |  |  |  |  |  | 68010000 | Purchase Account (Sf & Finish Goods) |
|  |  |  |  |  |  | 50309000 | COGS - Hardware |
|  |  |  |  |  |  | 50309500 | COGS - Licenses |
|  |  |  |  |  |  | 50307000 | COGS Production Overhead |
|  |  |  |  |  |  | 50306000 | COGS Setup Time |
|  |  |  |  |  |  | 50305000 | COGS Machine Time |
|  |  |  |  |  |  | 50304000 | COGS Personnel Time |
|  |  |  |  |  |  | 50303000 | COGS Material Overhead |
|  |  |  |  |  |  | 50302000 | COGS Third Party |
|  |  |  |  |  |  | 50301000 | COGS Direct Material |
|  |  |  |  |  |  | 50308000 | COGS Credits (Co/By-Pr) |
|  |  |  |  |  |  | 51100000 | Consumption - Raw Material |
|  |  |  |  |  |  | 52021000 | Loss Consumption for Quality Control (Raw & Trade) |
|  |  |  |  |  |  | 52023000 | Loss Consumption for Quality Control (SF&Fin Gds) |
|  |  |  |  |  |  | 52051000 | Loss Consumption of Consign. Mat (Raw & Trade) |
|  |  |  |  |  |  | 52053000 | Loss Consumption of Consign. Mat (SF & F.Goods) |
|  |  |  |  |  |  | 52521000 | Gain Consumption for Quality Control (Raw & Trade) |
|  |  |  |  |  |  | 52523000 | Gain Consumption for QM (SF & Finish Goods) |
|  |  |  |  |  |  | 52551000 | Gain Consumption of Consign. Mat (Raw & Trade) |
|  |  |  |  |  |  | 52552000 | Gain Consumption of Consign. Mat (SF & F.Goods) |
|  |  |  |  |  |  | 54053000 | Inventory Change - Scrap Own Products |
|  |  |  | 1300_CE |  | Utility Costs |  |  |
|  |  |  |  |  |  | 63001000 | Electricity and other utilities |
|  |  |  |  |  |  | 63002000 | Water |
|  |  |  | 1400_CE |  | Subcontracting/Third Party |  |  |
|  |  |  |  |  |  | 65008000 | Purchased Services-Time |
|  |  |  |  |  |  | 65400000 | Freight |
|  |  |  |  |  |  | 65008300 | Services - General |
|  |  |  |  |  |  | 61002000 | 3rd Party Material |
|  |  |  | 1500_CE |  | Changes Inventories |  |  |
|  |  |  |  |  |  | 52570000 | Gain from Production Variances |
|  |  |  |  |  |  | 52070000 | Loss from Production Variances |
|  |  |  |  |  |  | 55100000 | Plant Activity Production Order |
|  |  |  |  |  |  | 54400000 | Inventory Change - Finished Goods |
|  |  |  |  |  |  | 54300000 | Inventory Change - Semi Finished Goods |
|  |  |  |  |  |  | 54093000 | Inventory Change - QM Cons.Own Prod. w/ Cst Elem. |
|  |  |  |  |  |  | 54083000 | Inventory Change - Cost of Own Goods Sold W/C.Elem |
|  |  |  | 1600_CE |  | Purchasing/Inventory Differences |  |  |
|  |  |  |  |  |  | 65050000 | Unplanned Delivery Costs |
|  |  |  |  |  |  | 70040000 | Discount Received |
|  |  |  |  |  |  | 71040000 | Discount Lost Using Net Procedure |
|  |  |  |  |  |  | 52030000 | Loss from Revaluation |
|  |  |  |  |  |  | 52031000 | Loss from Valuation of External Products |
|  |  |  |  |  |  | 52041000 | Loss Price Variance (PRD) |
|  |  |  |  |  |  | 52060000 | Loss Small Price Differences Invoice Receipt (MM) |
|  |  |  |  |  |  | 52080000 | Loss from Allowed Differences GL Account Clearing |
|  |  |  |  |  |  | 52530000 | Gain from Revaluation |
|  |  |  |  |  |  | 52531000 | Gain from Valuation of External Products |
|  |  |  |  |  |  | 52541000 | Gain Price Variance (PRD) |
|  |  |  |  |  |  | 52560000 | Gain Small Price Difference Invoices Receipt (Mm) |
|  |  |  |  |  |  | 52580000 | Gain from Allowed Differences GL Account Clearing |
|  |  |  |  |  |  | 52590000 | Freight Revenue - Recovery |
|  |  |  |  |  |  | 52041500 | Loss Inventory Value Adjustment Ext. Prod. (BSK) |
|  |  |  |  |  |  | 52070500 | Loss Inventory Value Adjustment Own Prod. (BSK) |
|  |  |  |  |  |  | 52541500 | Gain Inventory Value Adjustment Ext. Prod. (BSK) |
|  |  |  |  |  |  | 52570500 | Gain Inventory Value Adjustment Own Prod. (BSK) |
|  |  |  |  |  |  | 54011100 | Inventory Change - Purch.Offset.Acct (Packaging) |
|  |  |  |  |  |  | 54011200 | Inventory Change - Purch.Offset.Acct (Trading) |
|  |  |  |  |  |  | 52001000 | Loss Inventory Variance (Raw & Trade) |
|  |  |  |  |  |  | 52003000 | Loss Inventory Variance (Sf & Finish Goods) |
|  |  |  |  |  |  | 52011000 | Loss Inventory Transfer (Raw & Trade) |
|  |  |  |  |  |  | 52013000 | Loss Inventory Transfer (Sf & Finish Goods) |
|  |  |  |  |  |  | 52033000 | Loss from Valuation of Own Products |
|  |  |  |  |  |  | 52042000 | Loss Price Differences (PRV) |
|  |  |  |  |  |  | 52043000 | Loss Price Differences (PRY) |
|  |  |  |  |  |  | 52044000 | Loss Price Differences - Material Ledger (LKW) |
|  |  |  |  |  |  | 52045000 | Loss Price Differences Own Products (PRK) |
|  |  |  |  |  |  | 52046000 | Loss Price Diff Fm Lower Lev.Own Mats ML (PRC) |
|  |  |  |  |  |  | 52501000 | Gain Inventory Variance (Raw & Trade) |
|  |  |  |  |  |  | 52503000 | Gain Inventory Variance (Sf & Finish Goods) |
|  |  |  |  |  |  | 52511000 | Gain Inventory Transfer (Raw & Trade) |
|  |  |  |  |  |  | 52513000 | Gain Inventory Transfer (SF & Finish Goods) |
|  |  |  |  |  |  | 52532000 | Gain from Valuation Own Products |
|  |  |  |  |  |  | 52542000 | Gain Price Differences (PRV) |
|  |  |  |  |  |  | 52543000 | Gain Price Differences (PRY) |
|  |  |  |  |  |  | 52544000 | Gain Price Differences - Material Ledger (LKW) |
|  |  |  |  |  |  | 52545000 | Posterior Real Rate Activity Allocation (AUI) |
|  |  |  |  |  |  | 54011000 | Inventory Change - Purch.Offset.Acct (Raw) |
|  |  |  |  |  |  | 54013000 | Inventory Change - Purch.Offset.Acct (SF & F.Good) |
|  |  |  | 1700_CE |  | Administration |  |  |
|  |  |  |  |  |  | 64032000 | Depr Expense (Bk < Tax) - Exceptional Depr (FR) |
|  |  |  |  |  |  | 64031000 | Depr Expense (Bk Less than Tax) - Exceptional Depr (FR) |
|  |  |  |  |  |  | 65301000 | Marketing Expenses |
|  |  |  |  |  |  | 65900000 | Loss in The Event of Damage |
|  |  |  |  |  |  | 63007000 | Fax and Internet |
|  |  |  |  |  |  | 65004000 | Donations |
|  |  |  |  |  |  | 65003000 | Vehicle Costs |
|  |  |  |  |  |  | 64021000 | Depreciation Expense - Intangible Assets |
|  |  |  |  |  |  | 63006000 | Telephone and Other Communication |
|  |  |  |  |  |  | 63004000 | Insurance |
|  |  |  |  |  |  | 64060000 | Accrued Interest (CO) |
|  |  |  |  |  |  | 64043000 | Amortization Expense - Goodwill |
|  |  |  |  |  |  | 65300000 | Legal and Audit Services |
|  |  |  |  |  |  | 63005000 | Office/Building Rent |
|  |  |  |  |  |  | 62000000 | Bad Debt Expense |
|  |  |  |  |  |  | 66000000 | Other Operating Expenses |
|  |  |  |  |  |  | 65200000 | Other Supplies |
|  |  |  |  |  |  | 65150000 | Computer Supplies |
|  |  |  |  |  |  | 65100000 | Office Supplies |
|  |  |  |  |  |  | 65002000 | Advertising and Sales Costs |
|  |  |  |  |  |  | 65000000 | Postage and Shipping |
|  |  |  | 1710_CE |  | Depreciation |  |  |
|  |  |  |  |  |  | 64050000 | Estimated Depreciation (CO) |
|  |  |  |  |  |  | 64040000 | Scheduled Deprec Fixed Assets Below Asset Value |
|  |  |  |  |  |  | 64030000 | Unplanned Depreciation Expense |
|  |  |  |  |  |  | 64020000 | Depreciation Expense - Low Value Assets |
|  |  |  |  |  |  | 64008000 | Depreciation Expense - Computer Software |
|  |  |  |  |  |  | 64007000 | Depreciation Expense - Computer Hardware |
|  |  |  |  |  |  | 64006000 | Depreciation Expense - Furniture |
|  |  |  |  |  |  | 64004000 | Depreciation Expense - Motor Vehicles |
|  |  |  |  |  |  | 64003000 | Depreciation Expense - Building Improvement |
|  |  |  |  |  |  | 64002000 | Depreciation Expense - Machinery & Equipment |
|  |  |  |  |  |  | 64001000 | Depreciation Expense - Buildings |
|  |  |  |  |  |  | 64005000 | Depreciation Expense - Office Equipment |
|  |  |  | 1800_CE |  | Buildings and Maintenance |  |  |
|  |  |  |  |  |  | 63000000 | Machine and Equipment Periodic Service |
|  |  |  |  |  |  | 63003000 | Other Periodic Service |
|  |  |  |  |  |  | 65009000 | Other Activity Costs |
|  |  |  |  |  |  | 63008000 | Building Periodic Service |
|  |  |  | 1900_CE |  | Travel Costs |  |  |
|  |  |  |  |  |  | 61003000 | Travel Expenses - Hotel and Accommodation |
|  |  |  |  |  |  | 61004000 | Travel Expenses - Meals |
|  |  |  |  |  |  | 61006000 | Travel Expenses - Entertainment |
|  |  |  |  |  |  | 61007000 | Travel Expenses - Airfare, Rail, Mileage |
|  |  |  |  |  |  | 61008000 | Travel Expenses - Miscellaneous |
|  |  |  |  |  |  | 61005000 | Travel Expenses - Ground Transportation |
|  |  |  |  |  |  | 65008400 | Purchased Services - Accommodation |
|  |  |  |  |  |  | 65008410 | Purchased Services - Airfair |
|  |  |  |  |  |  | 65008420 | Purchased Services - Ground Transportation |
|  |  |  |  |  |  | 65008430 | Purchased Services - Travel Miscellaneous |
|  |  |  | 2000_CE |  | Taxes |  |  |
|  |  |  |  |  |  | 75001000 | Excise Taxes |
|  |  |  |  |  |  | 75004000 | Other Taxes on Income |
|  |  |  |  |  |  | 75005000 | Input Tax Non Deductable (NAV) |
|  |  |  |  |  |  | 75007000 | Property Taxes |
|  |  |  |  |  |  | 75002000 | Corporate Income Tax Expense |
|  |  |  |  |  |  | 75008020 | Tax Fringe Benefits Tax (AU) |
|  |  |  |  |  |  | 75008050 | Export Taxes (FR) (AU) |
|  |  |  | 2100_CE |  | Sales Revenues/Deductions (Type 1) |  |  |
|  |  |  |  |  |  | 70100000 | Interest Income |
|  |  |  |  |  |  | 70300000 | Interest Income - Subsidiaries |
|  |  |  |  |  |  | 70500000 | Consumption of Provisions |
|  |  |  |  |  |  | 70800000 | Other Extraordinary Income |
|  |  |  |  |  |  | 44000000 | Over/Underpayments and Unallowed Deductions |
|  |  |  | 3000_CE |  | Other Income / Expense |  |  |
|  |  |  |  |  |  | 70015000 | Settlement of Asset U. Construction to CO Object |
|  |  |  |  |  |  | 71800000 | Other Extraordinary Expenses |
|  |  |  |  |  |  | 65001000 | Purchased Services |
|  |  |  |  |  |  | 71100000 | Interest Expense |
|  |  |  |  |  |  | 71300000 | Interest Expense - Subsidiaries |
|  |  |  |  |  |  | 72010000 | Loss from Exchange Rate Differences |
|  |  |  |  |  |  | 72020000 | Loss from Rounding Dif. Foreign Currency (MM) |
|  |  |  |  |  |  | 72040000 | Loss from Currency Valuation |
|  |  |  |  |  |  | 72510000 | Gain from Exchange Rate Differences |
|  |  |  |  |  |  | 72520000 | Gain from Rounding Dif. Foreign Currency (MM) |
|  |  |  |  |  |  | 72540000 | Gain from Currency Valuation |
|  |  |  |  |  |  | 71000000 | Bank Charges |
|  |  |  |  |  |  | 41090000 | Other Operating Revenue |
|  |  |  |  |  |  | 62010000 | Individual Value Adjustments |
|  |  |  |  |  |  | 62020000 | Flat-Rate Value Adjustments |
|  |  |  |  |  |  | 63009000 | Leasing Expense |
|  |  |  |  |  |  | 66000600 | Other Gains |
|  |  |  |  |  |  | 70300100 | Gain from Long Term Investment |
|  |  |  |  |  |  | 66010000 | Expense of Discounting (ZKB) |
|  |  |  |  |  |  | 66019900 | Addition to Provisions (ZKK) |
|  |  |  |  |  |  | 71050000 | Cash Discounts Expense |
|  |  |  |  |  |  | 71015000 | Offsetting Account Revaluation Ord. Depreciation |
|  |  | 200_CE | Secondary Costs |  |  |  |  |
|  |  |  | 4100_CE |  | Order Settlement |  |  |
|  |  |  |  |  |  | 93111100 | Result Analysis Primary Costs |
|  |  |  |  |  |  | 92101800 | Settlement R&D |
|  |  |  |  |  |  | 92105100 | Personnel Costs |
|  |  |  |  |  |  | 92105200 | Spare/Service/Ext Material Con |
|  |  |  |  |  |  | 92105300 | Other Costs |
|  |  |  |  |  |  | 92105400 | Secondary Costs |
|  |  |  |  |  |  | 92101500 | Settl. Rework |
|  |  |  | 4200_CE |  | Result Analysis |  |  |
|  |  |  |  |  |  | 93100000 | Result Analysis Technical |
|  |  |  |  |  |  | 93112000 | Result Analysis COP Reserv. |
|  |  |  |  |  |  | 93113000 | Result Analysis SEC Costs |
|  |  |  |  |  |  | 93114000 | Result Analysis COS Reserv. |
|  |  |  |  |  |  | 93115000 | Result Analysis OVH Costs |
|  |  |  |  |  |  | 93116000 | Result Analysis OVH Reserv. |
|  |  |  | 4300_CE |  | Overhead rate |  |  |
|  |  |  |  |  |  | 94113000 | Overhead Administration |
|  |  |  |  |  |  | 94114000 | Overhead Sales |
|  |  |  |  |  |  | 94111000 | Overhead Material |
|  |  |  |  |  |  | 94112000 | Overhead Production |
|  |  |  | 4400_CE |  | Assessments |  |  |
|  |  |  |  |  |  | 94201000 | Buildings & Periodic Service |
|  |  |  |  |  |  | 94222000 | COPA - Marketing |
|  |  |  |  |  |  | 94224000 | COPA - Admin. Overhead |
|  |  |  |  |  |  | 94225000 | COPA - Sales. Overhead |
|  |  |  |  |  |  | 94226000 | COPA - Non-Operating Expense |
|  |  |  |  |  |  | 94227000 | COPA - Non-Operating Income |
|  |  |  |  |  |  | 94228000 | COPA - Taxes |
|  |  |  |  |  |  | 94229000 | COPA - Cash Discount |
|  |  |  |  |  |  | 94202000 | Assessment Quality Costs |
|  |  |  | 4500_CE |  | Activity allocation |  |  |
|  |  |  |  |  |  | 94308000 | Consulting |
|  |  |  |  |  |  | 94311000 | Personnel Hours |
|  |  |  |  |  |  | 94304000 | Water |
|  |  |  |  |  |  | 94305000 | Industry Effluent |
|  |  |  |  |  |  | 94306000 | Environmental |
|  |  |  |  |  |  | 94307000 | Internal Transport |
|  |  |  |  |  |  | 94309000 | Development |
|  |  |  |  |  |  | 94308100 | Service Time |
|  |  |  |  |  |  | 97777700 | ICO Margin |
|  |  |  |  |  |  | 94308500 | Activity Unit Based Billing |
|  |  |  |  |  |  | 94301000 | Machine Hours 1 |
|  |  |  |  |  |  | 94302000 | Machine Hours 2 |
|  |  |  |  |  |  | 94303000 | Setup Production |
|  |  |  |  |  |  | 94310000 | Qm Control |
|  | 20_CE | Revenues and Sales Deductions (Type 11, 12) |  |  |  |  |  |
|  |  |  | 5100_CE |  | Revenues (type 11) |  |  |
|  |  |  |  |  |  | 41000000 | Revenue Domestic - Product |
|  |  |  |  |  |  | 41001500 | Revenue Affiliate - Product |
|  |  |  |  |  |  | 41000400 | Sales Revenue w/ Cost Element |
|  |  |  |  |  |  | 41001000 | Revenue Foreign - Product |
|  |  |  |  |  |  | 66000500 | Income - Reduction in Provisions |
|  |  |  |  |  |  | 41910000 | Billed Revenue Domestic |
|  |  |  |  |  |  | 41940000 | Billed Revenue Foreign |
|  |  |  |  |  |  | 41970000 | Billed Revenue Affiliated |
|  |  |  |  |  |  | 41007100 | On-Account Issued (Service Provider) |
|  |  |  |  |  |  | 41007200 | On-Account Utilized (Service Provider) |
|  |  |  | 5200_CE |  | Sales Deductions (type 12) |  |  |
|  |  |  |  |  |  | 61500000 | Sales Commissions |
|  |  |  |  |  |  | 72530000 | Gain from Rebates Differences |
|  |  |  |  |  |  | 44001000 | Sales Rebates |
|  |  |  |  |  |  | 44002000 | Sales Discounts - Domestic |
|  |  |  |  |  |  | 44005000 | Free Goods and Discount in Kind |
|  |  |  |  |  |  | 44002100 | Sales Discounts - Foreign |
|  |  |  |  |  |  | 44003000 | Customer Sales Deduction - Domestic |
|  |  |  |  |  |  | 44003100 | Customer Sales Deduction - Foreign |
|  |  |  |  |  |  | 44004000 | Sales Deduction - Material |
|  |  |  |  |  |  | 44006000 | Sales Deduction - Menge |
|  |  |  |  |  |  | 44003200 | Customer Sales Deduction - Affiliated |
|  |  |  |  |  |  | 44002200 | Sales Discounts - Affiliated |
|  |  |  |  |  |  | 44910000 | Sales Deduction Domestic |
|  |  |  |  |  |  | 44940000 | Sales Deduction Foreign |
|  |  |  |  |  |  | 44970000 | Sales Deduction Affiliated |
|  | 30_CE | Other costs |  |  |  |  |  |
|  |  |  | 6100_CE |  | Non operating revenues | Cost elements not assigned for US |  |
|  |  |  | 6200_CE |  | Non operating expenses | Cost elements not assigned for US |  |
|  |  |  | 6300_CE |  | Corporate Taxes | Cost elements not assigned for US |  |
|  |  |  |  |  |  | 75002100 | Capital Gains Tax |
|  |  |  |  |  |  | 75003000 | Deferred Tax |
|  |  |  |  |  |  | 75002200 | Solidary Surcharge on Corporate Income Tax |
|  |  |  |  |  |  | 75002300 | Solidary Surcharge for Interest Income Tax |
|  |  |  |  |  |  | 75008000 | Trade Tax |
|  |  |  |  |  |  | 75009000 | Export Duty |
|  |  |  |  |  |  | 75009900 | Other Company Taxes |
|  | 90_CE | Statistical Accounts |  |  |  |  |  |
|  |  |  | 9100_CE |  | Asset Accounting Accounts (CE-category 90) |  |  |
|  |  |  |  |  |  | 16000000 | Land & Land Improvements |
|  |  |  |  |  |  | 16001000 | Buildings |
|  |  |  |  |  |  | 16003000 | Building Improvements |
|  |  |  |  |  |  | 16002000 | Machinery & Equipment |
|  |  |  |  |  |  | 16005000 | Office Equipment |
|  |  |  |  |  |  | 16006000 | Furniture and Fixtures |
|  |  |  |  |  |  | 16007000 | Computer Hardware and Equipment |
|  |  |  |  |  |  | 16008000 | Computer Software |
|  |  |  |  |  |  | 16009000 | Assets Under Construction |
|  |  |  |  |  |  | 16020000 | Low Value Assets |
|  |  |  |  |  |  | 19310000 | Internal Development |
|  |  |  |  |  |  | 19320000 | Intangible Assets |
|  |  |  |  |  |  | 19330000 | Goodwill |
| YB_ALL | All cost elements |  |  |  |  |  |  |
|  |  |  | automatically |  |  | all cost elements are included |  |
| YBMF_001 | Personal related costs |  |  |  |  |  |  |
|  |  |  | 1100_CE |  | Personnel expenses |  |  |
| YBMF_002 | Raw-/service material consumption costs |  |  |  |  |  |  |
|  |  |  | 1200_CE |  | Material costs |  |  |
|  |  |  | 1300_CE |  | Utility Costs |  |  |
|  |  |  | 1400_CE |  | Subcontracting/Third Party |  |  |
|  |  |  | 1500_CE |  | Changes Inventories |  |  |
|  |  |  | 1600_CE |  | Purchasing/Inventory Differences |  |  |
| YBMF_003 | Other Costs |  |  |  |  |  |  |
|  |  |  | 1700_CE |  | Administration |  |  |
|  |  |  | 1800_CE |  | Buildings and Maintenance |  |  |
|  |  |  | 1900_CE |  | Travel Costs |  |  |
|  |  |  | 2000_CE |  | Taxes |  |  |
|  |  |  | 3000_CE |  | Other Income / Expense |  |  |
| YBMF_004 | Other Secondary Costs |  |  |  |  |  |  |
|  |  |  | 4100_CE |  | Order Settlement |  |  |
|  |  |  | 4300_CE |  | Overhead rate |  |  |
|  |  |  | 4400_CE |  | Assessments |  |  |
|  |  |  | 4500_CE |  | Activity allocation |  |  |

### Sheet: Statistical Key Figures

| Key | Name | Unit | Type | Country |
| --- | --- | --- | --- | --- |
| EE_ADM | Non-project relevant working times | H | #1 | XX |
| 1001 | Number of employees | PC | #1 | XX |
| 1002 | Area in square meter | M2 | #1 | XX |

## Suspected conflicts

> [!warning] Conflict
> Flagged while digesting this document, not verified: Cost centers 17101101 etc. appear twice in the Cost Centers sheet with different names and functional areas (e.g. Financials (US) YB40 vs 1000; 17101601 Marketing vs Transportation), so the same ID has two definitions.

> [!warning] Conflict
> Flagged while digesting this document, not verified: Secondary cost element 63009000 'Leasing Expense' and 64000000 are listed alongside a different ID range for the same account types, and cost element category values '#1' and '#01' are both used.

## Connections
- part-of :: [[_cluster]]
- related-to :: [[06-management-accounting/2608-master-data-fi-en-xx-119]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/General/2608_Master_Data_CO_EN_XX.xlsx` — full document · extracted with `xlsx2md` · 168,591 chars in the whole document
