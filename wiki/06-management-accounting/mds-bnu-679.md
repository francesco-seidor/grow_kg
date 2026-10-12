---
id: 06-management-accounting/mds-bnu-679
title: 原価積上実行の登録 - MDS (BNU) (BNU_S4CLD2608_Master_Data_JA_XX)
description: SAP S/4HANA Cloud 2608 master data script (JA) for registering and executing cost estimate runs (product costing) with app F1865 as Inventory Accountant.
cluster: 06-management-accounting
tags: [kb/management-accounting, topic/product-costing-and-standard-cost-updates]
aliases: [BNU_S4CLD2608_Master_Data_JA_XX]
keywords: [Product Costing Runs and Standard Cost Updates, cost estimate runs, product costing, master data script, costing variant, inventory accountant role, organizational units, price update, bill of materials, BNU]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/BNU_S4CLD2608_Master_Data_JA_XX.docx]
confidence: high
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-679
topic: 06-management-accounting/product-costing-and-standard-cost-updates
language: JA
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# 原価積上実行の登録 - MDS (BNU) (BNU_S4CLD2608_Master_Data_JA_XX)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/BNU_S4CLD2608_Master_Data_JA_XX.docx`, extracted with `mammoth`. Grouped under **Product Costing Runs and Standard Cost Updates** in Management Accounting. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

| <!-- image omitted: unnamed --> | マスタデータスクリプトSAP S/4HANA Cloud Public Edition - 02-07-26 |
| --- | --- |
|  | 原価積上実行の登録 - MDS (BNU) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

目次

[1 目的 2](#_Toc233892023)

[2 前提条件 3](#_Toc233892024)

[2.1 システムアクセス 3](#_Toc233892025)

[2.2 ロール 3](#_Toc233892026)

[2.3 必須の組織ユニット 3](#_Toc233892027)

[2.4 必須マスタデータおよび任意マスタデータ 4](#_Toc233892028)

[2.5 データ登録の主要パラメータ 4](#_Toc233892029)

[2.5.1 原価計算バリアント 4](#_Toc233892030)

[3 概要テーブル 6](#_Toc233892031)

[4 テスト手順 7](#_Toc233892032)

[4.1 原価積上実行の登録 7](#_Toc233892033)

[4.2 原価積上実行の実行 8](#_Toc233892034)

## 目的

この文書には、選択したロジスティクスシナリオの標準テストスクリプトの処理を開始する前に前提条件として実行する必要があるプロセスステップが含まれています。

この文書では、会社/プラントで使用される品目の原価積上実行を登録および実行する方法について説明します。目的は、受注を参照しないで品目の原価を計画し、品目およびその他の原価計算対象の価格を設定することです。

製品原価計画を使用して、以下のような会社の製品の原価を分析することができます。

- 半製品
- サービス
- その他の非製造品

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
| 管理会計担当者 - 在庫 | SAP_BR_INVENTORY_ACCOUNTANT | 棚卸資産会計 | SAP_BR_INVENTORY_ACCOUNTANT |  |

### 必須の組織ユニット

原価積上実行を登録するには、管理領域および会社コードを指定する必要があります。

|  |
| --- |
| 注記 使用される組織ユニット列に、システム環境に関連するデータセグメントの値を入力します。たとえば、会社コードとして 10 =ドイツ、17 = 米国のように入力します。 |

| データセグメント | 依存対象 | 項目例 | コメント | 使用される組織ユニット |
| --- | --- | --- | --- | --- |
| 原価計算データ | 管理領域 |  |  | 管理領域:____________ |
|  | 会社コード |  |  | 会社コード:__________ |
| 選択 | プラント |  |  | プラント:__________ |

### 必須マスタデータおよび任意マスタデータ

BOM データレコードは、他のマスタデータを参照する場合があります。以下の表は、BOM で使用される任意および必須のマスタデータオブジェクトの概要を示しています。

| マスタデータオブジェクト | データセグメントでの使用 | 必須/任意 | コメント |
| --- | --- | --- | --- |
| 品目 | 原価見積登録 > フローステップ > 選択 | 必須 | 通常では、原価積上実行によって原価積上が登録される品目を示す品目タイプを指定します。 |
| 生産マスタデータ (BOM、作業手順、作業区など) | 原価見積登録--> フローステップ --> 構造展開 | 任意 (または) 必須 | 生産された製品が原価積上実行に使用される場合は (たとえば、品目タイプ "FERT" (完成品) や "HALB" (半製品) の製品)、原価積上実行で "展開" される部品表/配合表がこれらの製品に含まれます。同時に作業手順が選択されます。事後計算のために、原価率とともに、作業区からの追加データ、割り当てられた原価センタ、および使用された活動タイプが決定されます。 |

### データ登録の主要パラメータ

このセクションでは、マスタレコードの動作に影響し、部品表/配合表の登録に常に必要となる基本パラメータの一部について説明します。

#### 原価計算バリアント

原価計算バリアントは、アプリケーションとカスタマイジングのリンクを定義します。なぜなら、すべての原価見積は原価計算バリアントを参照して実行および保存されるからです。

| 原価計算バリアント | 説明 | コメント |
| --- | --- | --- |
| PYC1 | 原価見積標準 | この原価計算バリアントは、選択した品目の標準製品原価見積を登録するのに使用されます。この結果に基づいて、品目評価データが更新されます。 |

## 概要テーブル

このスコープアイテムは、以下の表に示されている複数のプロセスステップで構成されます。

|  |
| --- |
| 注記 システム管理者が SAP Fiori ラウンチパッドでスペースおよびページを有効化している場合、ホームページには、ビジネスロールの一般的なタスクを実行するために必要なアプリのみが含まれます。ホームページに含まれていないその他すべての (検索可能な) アプリは、検索バーを使用して見つけることができます ([2434549](https://me.sap.com/notes/2434549))。ホームページをパーソナライズして非表示のアプリを含める場合は、ユーザプロファイルにナビゲートし、アプリファインダを選択します。 |

| プロセスステップ | ビジネスロール | トランザクション/アプリ名 | 予想される結果 |
| --- | --- | --- | --- |
| [原価積上実行の登録](#unique_10) [ ページ] 7 | 管理会計担当者 - 在庫 | 原価積上実行管理 - 見積原価 (F1865) | ヘッダデータと原価計算データタブが表示されます。 |
| [原価積上実行の実行](#unique_11) [ ページ] 8 | 管理会計担当者 - 在庫 | 原価積上実行管理 - 見積原価 (F1865) |  |

## テスト手順

このセクションでは、このスコープアイテムに属する各プロセスステップのテスト手順について説明します。

### 原価積上実行の登録

テスト管理

カスタマプロジェクト: プロジェクト固有部分への入力

|  |  |  |  |
| --- | --- | --- | --- |
| テストケース ID | <X.XX> | テスト実施日: |  |
| テスト実施者名: |  | 期間: |  |
| ビジネスロール: |  | 責任者: | <都道府県/州、サービスプロバイダ、カスタマ/共同サービスプロバイダ、およびカスタマ> |

目的

このアクティビティでは、原価積上実行を登録します。

手順

| テストステップ番号 | テストステップ名 | 指示 | 予想される結果 | 合格/不合格/コメント |
| --- | --- | --- | --- | --- |
| 1 | ログオンする | SAP Fiori ラウンチパッドに 管理会計担当者 - 在庫 としてログオンします。 | SAP Fiori ラウンチパッドが表示されます。 |  |
| 2 | SAP Fiori アプリにアクセスする | 原価積上実行管理 - 見積原価 (F1865) を開きます。 | 原価積上実行管理 - 見積原価ビューが表示されます。 |  |
| 3 | 原価積上実行を登録する | 登録を選択します。 | 新規原価積上実行登録ビューが表示されます。 |  |
| 4 | 原価積上実行のパラメータを入力する | 以下のエントリを入力して Enter を押します。原価積上実行: Test1原価積上実行日付: <現在日付を入力>テキスト: 原価積上実行 Test1原価計算バリアント: PYC1原価計算バージョン: 1管理領域: A000会社コード: 1010原価計算開始日: <現在日付>原価計算終了日: デフォルト値を採用数量構成日付: <現在日付>評価日: <現在日付> |  |  |
| 5 | 原価積上実行を保存する | 保存を選択します。 |  |  |

### 原価積上実行の実行

テスト管理

カスタマプロジェクト: プロジェクト固有部分への入力

|  |  |  |  |
| --- | --- | --- | --- |
| テストケース ID | <X.XX> | テスト実施日: |  |
| テスト実施者名: |  | 期間: |  |
| ビジネスロール: |  | 責任者: | <都道府県/州、サービスプロバイダ、カスタマ/共同サービスプロバイダ、およびカスタマ> |

目的

このアクティビティでは、原価積上実行を実行します。選定済品目は含まれません。

手順

| テストステップ番号 | テストステップ名 | 指示 | 予想される結果 | 合格/不合格/コメント |
| --- | --- | --- | --- | --- |
| 1 | ログオンする | SAP Fiori ラウンチパッドに 管理会計担当者 - 在庫 としてログオンします。 | SAP Fiori ラウンチパッドが表示されます。 |  |
| 2 | SAP Fiori アプリにアクセスする | 原価積上実行管理 - 見積原価 (F1865) を開きます。 | 原価積上実行管理 - 見積原価ビューが表示されます。 |  |
| 3 | 原価積上実行を選択する | 前のステップで登録した原価積上実行を検索し、エントリをクリックして編集を選択して、原価積上実行の詳細にアクセスします。 |  |  |
| 4 | 原価積上実行を開く | 以下のエントリを入力します。原価積上実行: 前ステップで登録した原価積上実行を入力して Enter を押します。処理セクションを展開します。 |  |  |
| 5 | 原価見積を登録する | 処理テーブルでは、各行のパラメータ列にパラメータ変更ボタンがあります。選択行でこのボタンを選択し、以下のエントリを入力します。品目タイプ: HALB、ROH、FERTプラント: 1010バックグラウンド処理の選択を解除し、オプション EXPLO を選択します。エントリを保存し、前画面を選択します。実行列に表示される実行を選択します。選択行のステータス信号が緑色に変わります。 | 選択が実行されます。 |  |
| 6 | 原価見積を登録する | 原価積上行で、パラメータ変更ボタンを選択します。原価積上実行: 原価見積 - パラメータ変更で、バックグラウンド処理フラグの設定を解除し、保存を選択します。前画面を選択します。実行列に表示される実行を選択します。原価積上行のステータス信号が緑色に変わります。 | 原価積上実行が実行されます。 |  |
| 7 | 原価見積を登録する | メニューから、編集 > 積上結果 の順に選択します。この行のステータス信号が赤色の場合は、原価積上レベルレポートを確認します。レポートのエラーを修正します。原価積上を再実行するには (必要な場合)、構造展開および原価積上行のステップを繰り返します。 | 原価積上実行が実行されます。 |  |
| 8 | 原価見積を登録する | 分析行で、パラメータ変更ボタンを選択します。パラメータ設定に SAP&11 を選択します。原価積上実行: 分析 - パラメータ変更で、バックグラウンド処理フラグの設定を解除し、保存を選択します。前画面を選択します。実行列に表示される実行を選択します。 | 原価積上実行が実行されます。 |  |
| 9 | 原価見積を登録する | マーク行で、ロックボタンを選択します。価格更新: 組織標準画面で、会社コード: 1010 を選択します。表示されるダイアログボックスで、原価計算バリアントに PYC1 を入力し、原価計算バージョンに 1 を入力して、Enter を押します。行のステータス信号が緑色に変わります。前画面を選択します。パラメータ変更を選択し、バックグラウンド処理の選択を解除します。保存を選択します。前画面を選択し、実行を選択します。 | 原価積上実行が実行されます。 |  |
| 10 | 原価見積を登録する | 承認行で、パラメータ変更を選択し、テスト実行およびバックグラウンド処理の選択を解除します。保存を選択します。前画面を選択し、実行を選択します。 | 現価格が品目マスタデータで更新されます。 |  |

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
- related-to :: [[06-management-accounting/crear-ejecucion-del-calculo-del-coste-mds-bnu-678]]
- related-to :: [[06-management-accounting/criar-execucao-de-calculo-de-custos-mds-bnu-680]]
- related-to :: [[06-management-accounting/kalkulationslauf-anlegen-sds-bnu-676]]
- related-to :: [[06-management-accounting/master-data-script-create-costing-run-mds-bnu-677]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/BNU_S4CLD2608_Master_Data_JA_XX.docx` — full document · extracted with `mammoth` · 8,824 chars in the whole document
