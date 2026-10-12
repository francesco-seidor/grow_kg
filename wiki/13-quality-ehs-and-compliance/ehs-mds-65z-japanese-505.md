---
id: 13-quality-ehs-and-compliance/ehs-mds-65z-japanese-505
title: EHS 化学物質コンプライアンス情報品目の登録 - MDS (65Z) (Japanese) (65Z_S4CLD2608_Master_Data_JA_XX)
description: Japanese master data script for creating an EHS Chemical Compliance Information (CCI) item in SAP S/4HANA Cloud Public Edition via app F4864.
cluster: 13-quality-ehs-and-compliance
tags: [kb/quality-ehs-and-compliance, topic/ehs-waste-management-products]
aliases: [65Z_S4CLD2608_Master_Data_JA_XX]
keywords: [EHS Products and Chemical Compliance Materials for Waste, master data scripts, ehs cci items, ehs waste management, business roles, 65Z]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/65Z_S4CLD2608_Master_Data_JA_XX.docx]
confidence: high
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-505
topic: 13-quality-ehs-and-compliance/ehs-waste-management-products
language: JA
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# EHS 化学物質コンプライアンス情報品目の登録 - MDS (65Z) (Japanese) (65Z_S4CLD2608_Master_Data_JA_XX)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/65Z_S4CLD2608_Master_Data_JA_XX.docx`, extracted with `mammoth`. Grouped under **EHS Products and Chemical Compliance Materials for Waste** in Quality, EHS and Compliance. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

| <!-- image omitted: unnamed --> | マスタデータスクリプトSAP S/4HANA Cloud Public Edition - 02-07-26 |
| --- | --- |
|  | EHS 化学物質コンプライアンス情報品目の登録 - MDS (65Z) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

目次

[1 目的 2](#_Toc233891766)

[2 前提条件 3](#_Toc233891767)

[2.1 システムアクセス 3](#_Toc233891768)

[2.2 ロール 3](#_Toc233891769)

[3 概要テーブル 4](#_Toc233891770)

[4 手順 5](#_Toc233891771)

[4.1 EHS 化学物質コンプライアンス情報品目マスタデータの登録 - 一般データ 5](#_Toc233891772)

## 目的

この文書では、S/4 HANA システムで EHS 化学物質コンプライアンス情報品目マスタデータレコードを登録する方法について説明します。この説明には、"標準的" なシステム環境で処理するマスタデータに関連するデータセグメントが含まれています。読者は、一般に入力値を入力する必要があるデータセグメントおよび項目について主に学習します。SAP Best Practices による S/4 HANA コンテンツ配信の範囲に関連しない項目については、UI に表示される場合もありますが、この文書では説明されていません。

ここでの説明に従って登録される EHS 化学物質コンプライアンス情報品目マスタレコードは、後で廃棄物管理プロセスで使用することができます。

## 前提条件

このセクションでは、システム、ユーザ、マスタデータ、組織データ、その他テストデータ、およびビジネス条件に関するテストを実施するためのすべての前提条件がまとめられています。

### システムアクセス

| システム | 詳細 |
| --- | --- |
| システム | SAP Fiori ラウンチパッドからアクセスすることができます。各自のロールに割り当てられている各種アプリにアクセスするための URL がシステム管理者から提供されます。 |

### ロール

SAP から提供される以下のビジネスロールテンプレートを使用して、ビジネスロールを登録し、それらを個別のテストユーザに割り当てます。

または、利用可能な場合は、SAP から提供される以下のスペースを使用することができます。スペーステンプレートを使用して、必要な事前定義済アプリを含むページのあるスペースを登録し、それをビジネスロールに割り当てます。その後、このビジネスロールを個別のユーザに割り当てます。

詳細については、SAP S/4HANA Cloud Public Editionの[Product Assistance](https://help.sap.com/docs/SAP_S4HANA_CLOUD/53e36b5493804bcdb3f6f14de8b487dd/ec310a8b669a45ca898dc4dd91d97de2.html)でテンプレートからのビジネスロールの作成方法を参照してください。

| 名称 (ロールテンプレート) | ID (ロールテンプレート) |
| --- | --- |
| 環境管理者 | SAP_BR_EHS_ENV_MGMT |

## 概要テーブル

このマスタレコードは、以下の表に示されている複数のセグメントで構成されます。

| セグメント | ビジネスロール | アプリ/トランザクション | 予想される結果 |
| --- | --- | --- | --- |
| [EHS 化学物質コンプライアンス情報品目マスタデータの登録 - 一般データ](#unique_6) [ ページ] 5 | 環境管理者 | 品目データ管理(F4864) | EHS 化学物質コンプライアンス情報 (CCI) 品目が登録されます。 |

## 手順

このセクションには、このマスタレコードに含まれる各セグメントまたはプロセスステップの手順が記載されています。

### EHS 化学物質コンプライアンス情報品目マスタデータの登録 - 一般データ

目的

以下の手順により、後で EHS 廃棄物管理プロセスで使用できる EHS 化学物質コンプライアンス情報品目の登録に関する指示が提供されます。

手順 (Fiori ラウンチパッドを使用)

| テストステップ番号 | テストステップ名 | 指示 | 予想される結果 | コメント |
| --- | --- | --- | --- | --- |
| 1 | ログオンする | 自分のユーザ認証情報を使用して SAP Fiori ラウンチパッドにログオンします。 | 開始ページが表示されます。 |  |
| 2 | 得意先マスタデータ管理を開く | 品目データ管理アプリ (F4864) を開きます。 | 品目データ管理アプリが開き、一覧レポートが表示されます。 |  |
| 3 | 新規品目を登録する | 登録を選択します。画面で:内部名項目に<名称>を入力します。ロジティクスロールドロップダウンリストから<ロジスティクスロール>を選択します。保存を選択します。 | 新規品目タブが表示され、新規品目が登録されます。 |  |
| 4 | 製品を追加する | 編集を選択します。製品セクションで、追加を選択し、製品を 1 つ選択します。保存を選択します。注記: 品目には、1 つの製品のみを割り当てることができます。 | 製品が品目に追加され、その情報が保存されます。 |  |

Typographic Conventions

| Type Style | Description |
| --- | --- |
| Example | Words or characters quoted from the screen. These include field names, screen titles, pushbuttons labels, menu names, menu paths, and menu options.Textual cross-references to other documents. |
| Example | Emphasized words or expressions. |
| EXAMPLE | Technical names of system objects. These include report names, program names, transaction codes, table names, and key concepts of a programming language when they are surrounded by body text, for example, SELECT and INCLUDE. |
| Example | Output on the screen. This includes file and directory names and their paths, messages, names of variables and parameters, source text, and names of installation, upgrade and database tools. |
| Example | Exact user entry. These are words or characters that you enter in the system exactly as they appear in the documentation. |
| <Example> | Variable user entry. Angle brackets indicate that you replace these words and characters with appropriate entries to make entries in the system. |
| EXAMPLE | Keys on the keyboard, for example, F2 or ENTER. |

|  |
| --- |
|  |
| www.sap.com/contactsap |
| © 2026 SAP SE or an SAP affiliate company. All rights reserved.No part of this publication may be reproduced or transmitted in any form or for any purpose without the express permission of SAP SE or an SAP affiliate company. The information contained herein may be changed without prior notice. Some software products marketed by SAP SE and its distributors contain proprietary software components of other software vendors. National product specifications may vary.These materials are provided by SAP SE or an SAP affiliate company for informational purposes only, without representation or warranty of any kind, and SAP or its affiliated companies shall not be liable for errors or omissions with respect to the materials. The only warranties for SAP or SAP affiliate company products and services are those that are set forth in the express warranty statements accompanying such products and services, if any. Nothing herein should be construed as constituting an additional warranty. SAP and other SAP products and services mentioned herein as well as their respective logos are trademarks or registered trademarks of SAP SE (or an SAP affiliate company) in Germany and other countries. All other product and service names mentioned are the trademarks of their respective companies. See [www.sap.com/copyright](http://www.sap.com/copyright) for additional trademark information and notices. |

<!-- image omitted: SAP Logo -->

## Connections
- part-of :: [[_cluster]]
- related-to :: [[13-quality-ehs-and-compliance/crear-un-material-de-informacion-de-conformidad-de-producto-quimico-eh]]
- related-to :: [[13-quality-ehs-and-compliance/create-an-ehs-chemical-compliance-information-material-mds-65z-503]]
- related-to :: [[13-quality-ehs-and-compliance/criar-um-material-de-informacoes-de-conformidade-quimica-ehs-mds-65z-5]]
- related-to :: [[13-quality-ehs-and-compliance/ehs-mds-65z-chinese-507]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/65Z_S4CLD2608_Master_Data_JA_XX.docx` — full document · extracted with `mammoth` · 5,073 chars in the whole document
