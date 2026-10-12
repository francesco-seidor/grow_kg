---
id: 02-business-partner-and-product-master-data/mds-2ni-271
title: "マスタデータスクリプト: アプリケーショングループおよび特性照会の登録 - MDS (2NI) (2NI_S4CLD2608_Master_Data_JA_XX)"
description: Japanese master data script (MDS 2NI) for creating application groups and characteristic inquiries (with characteristic assignment) in SAP S/4HANA Cloud Public Edition 2608.
cluster: 02-business-partner-and-product-master-data
tags: [kb/business-partner-and-product-master-data, topic/variant-configuration-master-data]
aliases: [2NI_S4CLD2608_Master_Data_JA_XX]
keywords: [Configurable Materials and Characteristic Display, characteristic inquiry, application groups, master data scripts, characteristic assignment, variant configuration, business roles, transactions, 2NI]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/2NI_S4CLD2608_Master_Data_JA_XX.docx]
confidence: low
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-271
topic: 02-business-partner-and-product-master-data/variant-configuration-master-data
language: JA
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# マスタデータスクリプト: アプリケーショングループおよび特性照会の登録 - MDS (2NI) (2NI_S4CLD2608_Master_Data_JA_XX)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/2NI_S4CLD2608_Master_Data_JA_XX.docx`, extracted with `mammoth`. Grouped under **Configurable Materials and Characteristic Display** in Business Partner and Product Master Data. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

| <!-- image omitted: unnamed --> | マスタデータスクリプトSAP S/4HANA Cloud Public Edition - 02-07-26 |
| --- | --- |
|  | アプリケーショングループおよび特性照会の登録 - MDS (2NI) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

目次

[1 目的 2](#_Toc233891480)

[2 前提条件 3](#_Toc233891481)

[2.1 システムアクセス 3](#_Toc233891482)

[2.2 ロール 3](#_Toc233891483)

[2.3 必須のマスタデータおよび操作可能なマスタデータ 3](#_Toc233891484)

[2.4 データ登録の主要パラメータ 4](#_Toc233891485)

[2.4.1 トランザクション 4](#_Toc233891486)

[3 概要テーブル 5](#_Toc233891487)

[4 テスト手順 6](#_Toc233891488)

[4.1 アプリケーショングループの登録 6](#_Toc233891489)

[4.2 特性照会の登録 7](#_Toc233891490)

## 目的

この文書では、SAP S/4HANA Cloud Public Editionシステムの特性照会レコードを登録する方法について説明します。この説明には、アプリケーショングループ、特性照会、特性割当など、SAP S/4HANA Cloud Public Editionアプライアンスに関連するデータが含まれます。SAP S/4HANA Cloud Public Editionの範囲に関連しない項目については、この文書では説明していません。

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

| 名称 (ロールテンプレート) | ID (ロールテンプレート) | 名称 (ラウンチパッド領域) | ID (ラウンチパッド領域) | ログオン |
| --- | --- | --- | --- | --- |
| 製品選定モデラ | SAP_BR_PRODUCT_CONFIG_MODELER | バリアント選定 | SAP_BR_PRODUCT_CONFIG_MODELER |  |

### 必須のマスタデータおよび操作可能なマスタデータ

特性照会レコードは、他のマスタデータを参照する場合があります。以下の表は、品目マスタデータレコードで使用される、任意および必須のマスタデータオブジェクトの概要を示しています。

| マスタデータオブジェクト | データセグメントでの使用 | 必須/任意 | コメント |
| --- | --- | --- | --- |
| 特性 |  | 必須 | 特性は特性照会レコードへの割当対象です |

### データ登録の主要パラメータ

このセクションでは、マスタレコードの動作に影響し、特性照会の登録に必ず必要となる基本パラメータの一部について説明します。

#### トランザクション

トランザクションを使用して、特性照会を使用可能にする必要があるトランザクションが決定されます。

1711 エディションでは、販売管理伝票のみがサポートされます。

| トランザクション | コメント |
| --- | --- |
| 販売管理伝票 | 1711 エディションでは、特性照会については、販売管理伝票のみがサポートされます。 |
| 製造指図 |  |
| トレード契約 |  |
| 購買発注 |  |
| 入庫 |  |
| 指図確認 |  |

## 概要テーブル

このセクションでは、マスタデータレコードを登録する際にユーザが実行するステップの一覧が提供されます。マスタデータオブジェクトの論理的かつ有効なすべてのセグメントについては、個別のステップ (組織ユニット依存のデータセグメントなど) に続く必要があります。

スコープアイテム アプリケーショングループおよび特性照会の登録 - MDS は、以下の表に示す複数のプロセスステップで構成されます。

|  |
| --- |
| 注記 システム管理者が SAP Fiori ラウンチパッドでスペースおよびページを有効化している場合、ホームページには、ビジネスロールの一般的なタスクを実行するために必要なアプリのみが含まれます。ホームページに含まれていないその他すべての (検索可能な) アプリは、検索バーを使用して見つけることができます ([2434549](https://me.sap.com/notes/2434549))。ホームページをパーソナライズして非表示のアプリを含める場合は、ユーザプロファイルにナビゲートし、アプリファインダを選択します。 |

| プロセスステップ、レポート、またはアイテム | ビジネスロール | トランザクション/アプリ | 予想される結果 |
| --- | --- | --- | --- |
| [アプリケーショングループの登録](#unique_9) [ ページ] 6 | 製品選定モデラ | 選定の特性照会の更新(CU_CHAR_DISPLAY) | アプリケーショングループが登録されます。 |
| [特性照会の登録](#unique_10) [ ページ] 7 | 製品選定モデラ | 選定の特性照会の更新(CU_CHAR_DISPLAY) | アプリケーショングループが登録されます。 |

## テスト手順

このセクションでは、このスコープアイテムに属する各プロセスステップの手順について説明します。これらの手順は、マスタデータ登録のテストでも使用できます。

### アプリケーショングループの登録

テスト管理

カスタマプロジェクト: プロジェクト固有部分への入力

|  |  |  |  |
| --- | --- | --- | --- |
| テストケース ID | <X.XX> | テスト実施日: |  |
| テスト実施者名: |  | 期間: |  |
| ビジネスロール: |  | 責任者: | <都道府県/州、サービスプロバイダ、カスタマ/共同サービスプロバイダ、およびカスタマ> |

手順

| テストステップ番号 | テストステップ名 | 指示 | 予想される結果 | 合格/不合格/コメント |
| --- | --- | --- | --- | --- |
| 1 | ログオンする | SAP Fiori ラウンチパッドに 製品選定モデラ としてログオンします。 | SAP Fiori ラウンチパッドが表示されます。 |  |
| 2 | SAP Fiori アプリにアクセスする | 選定の特性照会の更新(CU_CHAR_DISPLAY) を開きます。 | ビュー "アプリケーショングループ" 変更: 概要ビューが表示されます。 |  |
| 3 | アプリケーショングループを入力する | ビュー "アプリケーショングループ" 変更: 概要画面で、新規エントリを選択します。以下のエントリを入力します。トランザクション: <ドロップダウンリストから選択>Appl Grp: <任意のコード> | 新規エントリ: 追加エントリ概要画面が表示されます。 |  |
| 4 | データを保存する | 保存を選択します。 |  |  |

### 特性照会の登録

テスト管理

カスタマプロジェクト: プロジェクト固有部分への入力

|  |  |  |  |
| --- | --- | --- | --- |
| テストケース ID | <X.XX> | テスト実施日: |  |
| テスト実施者名: |  | 期間: |  |
| ビジネスロール: |  | 責任者: | <都道府県/州、サービスプロバイダ、カスタマ/共同サービスプロバイダ、およびカスタマ> |

手順

| テストステップ番号 | テストステップ名 | 指示 | 予想される結果 | 合格/不合格/コメント |
| --- | --- | --- | --- | --- |
| 1 | ログオンする | SAP Fiori ラウンチパッドに 製品選定モデラ としてログオンします。 | SAP Fiori ラウンチパッドが表示されます。 |  |
| 2 | SAP Fiori アプリにアクセスする | 選定の特性照会の更新(CU_CHAR_DISPLAY) を選択します。 | ビュー "アプリケーショングループ" 変更: 概要ビューが表示されます。 |  |
| 3 | アプリケーショングループを入力する | ビュー "アプリケーショングループ" 変更: 概要画面で、特性照会を選択します。新規エントリを選択します。以下のエントリを入力して Enter を押します。特性照会: <任意のコード>.テキスト: <特性照会のテキストを入力>.アプリケーショングループ: <ヘルプは F4 を選択> | ビュー ''特性照会'' 変更: 概要画面が表示されます。 |  |
| 4 | 特性を割り当てる | 前のステップで登録した特性照会を選択し、特性割当を選択します。以下のエントリを入力します。順序: <特性表示順を決定する順序番号を入力>特性名: <F4 検索ヘルプを選択して特性を検索>.列: <特性テキストおよび値を表示するための適切な列幅を入力> | ビュー ''特性割当'' 変更: 概要画面が表示されます。 |  |
| 5 | データを保存する | 保存を選択します。 |  |  |

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

## Suspected conflicts

> [!warning] Conflict
> Flagged while digesting this document, not verified: 1711-edition limitation (only sales documents supported) is stated in a 2608 document alongside other transactions; may be outdated

## Connections
- part-of :: [[_cluster]]
- related-to :: [[02-business-partner-and-product-master-data/anwendungsgruppe-und-merkmalsanzeige-anlegen-sds-2ni-268]]
- related-to :: [[02-business-partner-and-product-master-data/crear-grupo-de-aplicaciones-y-visualizacion-de-caracteristicas-mds-2ni]]
- related-to :: [[02-business-partner-and-product-master-data/create-application-group-and-characteristic-display-mds-2ni-269]]
- related-to :: [[02-business-partner-and-product-master-data/mds-2ni-273]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/2NI_S4CLD2608_Master_Data_JA_XX.docx` — full document · extracted with `mammoth` · 7,321 chars in the whole document
