---
id: 12-production-and-manufacturing/bom-mds-bnk-625
title: "マスタデータスクリプト: 製造および販売向けの品目 BOM の登録 - MDS (BNK) (BNK_S4CLD2608_Master_Data_JA_XX)"
description: "Japanese SAP S/4HANA Cloud 2608 master data script (BNK) for creating change numbers, production BOMs and sales BOMs (F1813A, F1813, CC01)."
cluster: 12-production-and-manufacturing
tags: [kb/production-and-manufacturing, topic/material-boms]
aliases: [BNK_S4CLD2608_Master_Data_JA_XX]
keywords: [Material BOMs for Production and Sales, material bom, production bom, sales bom, change numbers, bom usage, item categories, business roles, master data scripts, routing]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/BNK_S4CLD2608_Master_Data_JA_XX.docx]
confidence: high
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-625
topic: 12-production-and-manufacturing/material-boms
language: JA
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# マスタデータスクリプト: 製造および販売向けの品目 BOM の登録 - MDS (BNK) (BNK_S4CLD2608_Master_Data_JA_XX)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/BNK_S4CLD2608_Master_Data_JA_XX.docx`, extracted with `mammoth`. Grouped under **Material BOMs for Production and Sales** in Production and Manufacturing. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

| <!-- image omitted: unnamed --> | マスタデータスクリプトSAP S/4HANA Cloud Public Edition - 02-07-26 |
| --- | --- |
|  | 製造および販売向けの品目 BOM の登録 - MDS (BNK) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

目次

[1 目的 2](#_Toc233891953)

[2 前提条件 3](#_Toc233891954)

[2.1 システムアクセス 3](#_Toc233891955)

[2.2 ロール 3](#_Toc233891956)

[2.3 必須の組織ユニット 3](#_Toc233891957)

[2.4 必須マスタデータおよび任意マスタデータ 4](#_Toc233891958)

[2.5 データ登録の主要パラメータ 4](#_Toc233891959)

[2.5.1 BOM 用途 4](#_Toc233891960)

[3 概要テーブル 5](#_Toc233891961)

[4 テスト手順 6](#_Toc233891962)

[4.1 変更番号の登録 6](#_Toc233891963)

[4.2 生産 BOM の登録 7](#_Toc233891964)

[4.3 販売 BOM の登録 9](#_Toc233891965)

[5 付録 11](#_Toc233891966)

[5.1 後続処理: 作業手順の登録 11](#_Toc233891967)

## 目的

生産 BOM は、製品または組立品目 (製品の一部) を構成する構成品目の正式に構造化された一覧です。この一覧には、各構成品目のオブジェクト番号が、数量および数量単位とともに含まれます。構成品目は、原材料または組立部品を表す半製品品目の場合があります。

構成品目は、MRP 実行で資材所要量を計画するため、および製造指図などのトランザクションで使用されます。情報は生産サイト (プラントと呼ばれます) に固有です。

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

| 名称 (ロールテンプレート) | ID (ロールテンプレート) | 名称 (ラウンチパッド領域) | ID (ラウンチパッド領域) | ログオンする |
| --- | --- | --- | --- | --- |
| 生産エンジニア - ディスクリート製造 | SAP_BR_PRODN_ENG_DISC | 生産エンジニアリング - ディスクリート製造 | SAP_BR_PRODN_ENG_DISC |  |
| BOM 設計者 | SAP_BR_BOM_ENGINEER | 部品表/配合表 | SAP_BR_BOM_ENGINEER |  |

### 必須の組織ユニット

会社の組織構造およびマスタデータが有効化時にシステムに登録されています。組織構造には、会社の構造が反映されます。マスタデータは、会社の重点業務に応じて、品目、得意先、および仕入先などを表します。

独自のマスタデータまたは以下のサンプルデータを使用して、テスト手順を実行します。

### 必須マスタデータおよび任意マスタデータ

BOM データレコードは、他のマスタデータを参照する場合があります。以下の表は、BOM で使用される、任意および必須のマスタデータオブジェクトの概要を示しています。

| マスタデータオブジェクト | データセグメントでの使用 | 必須/任意 | コメント |
| --- | --- | --- | --- |
| 品目 | 品目 BOM 登録: 第一画面および品目 BOM 登録: 一般明細ビューで、品目および構成品目に品目コードを入力します。 | 必須 | プロセスステップを開始する前の前提条件として、以下のマスタデータスクリプトを完了します。"原材料" タイプの製品マスタの登録 - MDS (BNR)"半製品" タイプの製品マスタの登録 - MDS (BNS)"最終製品" タイプの製品マスタの登録 - MDS (BNT)"商品" タイプの製品マスタの登録 - MDS (BNF) |

### データ登録の主要パラメータ

このセクションでは、マスタレコードの動作に影響し、部品表/配合表の登録に常に必要となる基本パラメータの一部について説明します。

#### BOM 用途

部品表/配合表 (BOM) 用途では、品目 BOM を使用できる領域 (販売、生産など) が定義されます。

| BOM 用途 | 説明 |
| --- | --- |
| 1 | 本稼働 |
| 5 | 販売管理 |

## 概要テーブル

このスコープアイテムは、以下の表に示されている複数のプロセスステップで構成されます。

|  |
| --- |
| 注記 システム管理者が SAP Fiori ラウンチパッドでスペースおよびページを有効化している場合、ホームページには、ビジネスロールの一般的なタスクを実行するために必要なアプリのみが含まれます。ホームページに含まれていないその他すべての (検索可能な) アプリは、検索バーを使用して見つけることができます ([2434549](https://me.sap.com/notes/2434549))。ホームページをパーソナライズして非表示のアプリを含める場合は、ユーザプロファイルにナビゲートし、アプリファインダを選択します。 |

| プロセスステップ | ビジネスロール | トランザクション | 予想される結果 |
| --- | --- | --- | --- |
| [変更番号の登録](#unique_10) [ ページ] 6 | BOM 設計者 | 変更マスタ登録 (CC01) |  |
| [生産 BOM の登録](#unique_11) [ ページ] 7 | 生産エンジニア - ディスクリート製造 | 部品表/配合表の更新 (バージョン 2) - BOM の登録、変更、照会(F1813A) |  |
| [販売 BOM の登録](#unique_12) [ ページ] 9 | 生産エンジニア - ディスクリート製造 | 部品表/配合表の更新 - BOM の登録、変更、照会(F1813) |  |

## テスト手順

このセクションでは、このスコープアイテムに属する各プロセスステップのテスト手順について説明します。

### 変更番号の登録

テスト管理

カスタマプロジェクト: プロジェクト固有部分への入力

|  |  |  |  |
| --- | --- | --- | --- |
| テストケース ID | <X.XX> | テスト実施日: |  |
| テスト実施者名: |  | 期間: |  |
| ビジネスロール: |  | 責任者: | <都道府県/州、サービスプロバイダ、カスタマ/共同サービスプロバイダ、およびカスタマ> |

目的

次の生産および部品表/配合表の登録ステップで部品表/配合表の登録に使用する変更マスタを登録します。

手順

| テストステップ番号 | テストステップ名 | 指示 | 予想される結果 | 合格/不合格/コメント |
| --- | --- | --- | --- | --- |
| 1. | ログオンする | SAP Fiori ラウンチパッドにBOM 設計者としてログオンします。 |  |  |
| 2 | SAP Fiori アプリにアクセスする | 変更マスタ登録 (CC01)を開きます。 |  |  |
| 3 | 変更番号を入力する | 変更マスタの登録: 第一画面で、次のデータを入力してEnterキーを押します。変更番号: <変更番号を入力 (例: CN001)>他の項目はデフォルト値のままにします。 |  |  |
| 4 | 変更マスタデータを入力する | 変更マスタの登録: ヘッダ変更画面で、以下の例に示すデータを入力し、Enter キーを押します。変更番号の横の項目: MBOM の変更マスタ有効開始: 本日変更番号ステータス: 01 - 有効 |  |  |
| 5 | 部品表/配合表のチェックボックスを選択する | 変更マスタの登録: オブジェクトタイプ画面のオブジェクトタイプテーブルの部品表/配合表行で、以下のチェックボックスを選択します。有効オブジェクト管理レコード |  |  |
| 6 | 保存を選択する | 保存を選択します。 | 変更マスタが登録されます。 |  |

### 生産 BOM の登録

テスト管理

カスタマプロジェクト: プロジェクト固有部分への入力

|  |  |  |  |
| --- | --- | --- | --- |
| テストケース ID | <X.XX> | テスト実施日: |  |
| テスト実施者名: |  | 期間: |  |
| ビジネスロール: |  | 責任者: | <都道府県/州、サービスプロバイダ、カスタマ/共同サービスプロバイダ、およびカスタマ> |

手順

| テストステップ番号 | テストステップ名 | 指示 | 予想される結果 | コメント |
| --- | --- | --- | --- | --- |
| 1 | ログオンする | SAP Fiori ラウンチパッドに生産エンジニア - ディスクリート製造としてログオンします。 | SAP Fiori ラウンチパッドが表示されます。 |  |
| 2 | SAP Fiori アプリにアクセスする | 部品表/配合表の更新 (バージョン 2) - BOM の登録、変更、照会(F1813A)を開きます。 |  |  |
| 3 | BOM を登録する | BOM 登録を選択します。BOM 登録画面で、以下のデータを入力して OK を選択します。品目: <最終品目/半製品品目の品目コード>変更番号: <前のステップで登録した変更番号>プラント: <自分のプラント>BOM 用途: 1 (生産のみ) |  |  |
| 4 | 構成品目データを追加する | 構成品目セクションで、追加アイコンを選択して構成品目を 1 つ以上追加します。明細カテゴリ ICt: <在庫品目の場合は L>構成品目: <品目コード、原材料/半製品>数量: <数量>構成品目数量単位: 個 | 構成品目データが追加されます。 |  |
| 5 | BOM 明細カテゴリ非在庫 ('N') を入力する | 構成品目セクションで、追加アイコンを選択して構成品目を 1 つ以上追加します。明細カテゴリ ICt: <N (非在庫品目)>構成品目: <品目コード、原材料/半製品>構成品目数量: <数量>構成品目数量単位: 個Enter キーを押して構成品目および構成品目数量項目を有効化します。注記 この明細カテゴリは、在庫に保管されていない構成品目で使用され、非在庫品目はマスタレコードの有無にかかわらず BOM に入力できます。 | 非在庫品目の構成品目データが追加されます。 |  |
| 6 | BOM 明細カテゴリ可変サイズ ('R') を入力する | 構成品目セクションで、追加アイコンを選択して構成品目を 1 つ以上追加します。明細カテゴリ ICt: <R (可変サイズ品目)>構成品目: <品目コード、原材料/半製品>矢印を選択して詳細ページを開きます。可変サイズ品目データで必要なエントリを入力します。サイズ 1: <可変サイズ品目の寸法を入力>サイズ 2: <可変サイズ品目の寸法を入力>Size3: <可変サイズ品目の寸法を入力>サイズ単位: <可変サイズ品目の数量単位を入力>数式キー: <可変サイズ品目を計算する計算式を入力>可変サイズ品目数: <数量>可変サイズ品目数量: <計算された可変サイズ品目の数量>適用を選択します。注記 この明細カテゴリを使用すると、1 つの品目でセクションごとにサイズが異なる構成品目のサイズ (板張りの修復に必要な 1 枚の鋼板のサイズなど) を指定することができます。 | 可変品目の構成品目データが追加または計算されます。 |  |
| 7 | BOM 明細カテゴリのテキスト明細を入力する (‘T’) | 新規 BOM 明細番号行で、以下の例のようなエントリを入力します。品目カテゴリ: テキスト明細BOM 明細番号行で、矢印を選択して詳細ページを開きます。部品表/配合表更新 - 基本詳細画面で、構成品目数量: 1構成品目数量単位: 個ステータス/テキスト (長) タブを選択し、明細テキストを表示します。明細テキスト: 文書 | テキスト明細のテキスト文書データが追加されます。 |  |
| 8 | ヘッダを確認する | ヘッダ属性セクションでデータを確認し、必要に応じて変更できます。 |  |  |
| 9 | データを保存する | エントリを保存します。 | 品目 BOM が保存されましたというメッセージが表示されます。 |  |

### 販売 BOM の登録

テスト管理

カスタマプロジェクト: プロジェクト固有部分への入力

|  |  |  |  |
| --- | --- | --- | --- |
| テストケース ID | <X.XX> | テスト実施日: |  |
| テスト実施者名: |  | 期間: |  |
| ビジネスロール: |  | 責任者: | <都道府県/州、サービスプロバイダ、カスタマ/共同サービスプロバイダ、およびカスタマ> |

手順

| テストステップ番号 | テストステップ名 | 指示 | 予想される結果 | コメント |
| --- | --- | --- | --- | --- |
| 1 | ログオン | SAP Fiori ラウンチパッドに生産エンジニア - ディスクリート製造としてログオンします。 | SAP Fiori ラウンチパッドが表示されます。 |  |
| 2 | SAP Fiori アプリにアクセスする | 部品表/配合表の更新 - BOM の登録、変更、照会(F1813)を選択します。 |  |  |
| 3 | BOM を登録する | BOM 登録を選択します。BOM 登録画面で、以下のデータを入力して OK を選択します。品目: <BOM ヘッダ品目コード>、SDBOMERLAHD、または SDBOMLUMFHD などプラント: <該当するプラントを入力>変更番号: <前のステップで登録した変更番号>BOM 用途: 5 |  |  |
| 4 | 構成品目データを追加する | 構成品目セクションで、追加アイコンを選択して構成品目を 1 つ以上追加します。明細カテゴリ ICt: <在庫品目の場合は L>構成品目: <品目コード、商品>数量: <数量> | 構成品目データが追加されます。 |  |
| 5 | ヘッダを確認する | ヘッダ属性セクションでデータを確認し、必要に応じて変更できます。 |  |  |
| 6 | データを保存する | エントリを保存します。 | 品目 BOM が保存されましたというメッセージが表示されます。 |  |

## 付録

### 後続処理: 作業手順の登録

| マスタデータオブジェクト | データセグメントでの使用 | 必須/任意 | コメント |
| --- | --- | --- | --- |
| 作業手順 |  |  | このアクティビティを実行するには、作業手順の登録 - MDS (BNL) テストスクリプトを完了します。 |

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
- related-to :: [[12-production-and-manufacturing/crear-lista-de-materiales-para-material-para-produccion-y-ventas-mds-b]]
- related-to :: [[12-production-and-manufacturing/create-material-bom-for-production-and-sales-mds-bnk-623]]
- related-to :: [[12-production-and-manufacturing/mds-bnk-627]]
- related-to :: [[12-production-and-manufacturing/script-de-dados-mestre-criar-lista-tecnica-de-materiais-para-producao]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/BNK_S4CLD2608_Master_Data_JA_XX.docx` — full document · extracted with `mammoth` · 9,819 chars in the whole document
