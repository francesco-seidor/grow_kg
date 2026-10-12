---
id: 10-procurement/mds-bhd-565
title: 購買情報の登録 - MDS (BHD) (BHD_S4CLD2608_Master_Data_JA_XX)
description: "Japanese master data script (BHD) for creating and mass-changing purchasing info records (standard, consignment, subcontracting, pipeline) in SAP S/4HANA Cloud Public Edition."
cluster: 10-procurement
tags: [kb/procurement, topic/purchasing-info-records]
aliases: [BHD_S4CLD2608_Master_Data_JA_XX]
keywords: [Purchasing Info Records, standard info record, consignment info record, subcontracting info record, pipeline info record, mass change info records, mass price change, number ranges, business roles, related functions]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/BHD_S4CLD2608_Master_Data_JA_XX.docx]
confidence: high
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-565
topic: 10-procurement/purchasing-info-records
language: JA
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# 購買情報の登録 - MDS (BHD) (BHD_S4CLD2608_Master_Data_JA_XX)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/BHD_S4CLD2608_Master_Data_JA_XX.docx`, extracted with `mammoth`. Grouped under **Purchasing Info Records** in Procurement. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

| <!-- image omitted: unnamed --> | マスタデータスクリプトSAP S/4HANA Cloud Public Edition - 02-07-26 |
| --- | --- |
|  | 購買情報の登録 - MDS (BHD) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

目次

[1 目的 2](#_Toc233891894)

[2 前提条件 3](#_Toc233891895)

[2.1 システムアクセス 3](#_Toc233891896)

[2.2 ロール 3](#_Toc233891897)

[2.3 必須の組織ユニット 3](#_Toc233891898)

[2.4 必須マスタデータおよび任意マスタデータ 4](#_Toc233891899)

[2.5 データ登録の主要パラメータ 4](#_Toc233891900)

[2.5.1 番号範囲 4](#_Toc233891901)

[3 概要テーブル 5](#_Toc233891902)

[4 テスト手順 6](#_Toc233891903)

[4.1 購買情報登録 6](#_Toc233891904)

[4.2 受託品/預託品の購買情報の登録 8](#_Toc233891905)

[4.3 外注の購買情報登録 10](#_Toc233891906)

[4.4 パイプラインの購買情報の登録 13](#_Toc233891907)

[4.5 購買情報への一括変更 15](#_Toc233891908)

[4.6 購買情報の一括価格変更 17](#_Toc233891909)

[5 付録 19](#_Toc233891910)

[5.1 関連機能 19](#_Toc233891911)

## 目的

購買情報レコードには、品目とその品目を提供するサプライヤに固有の情報が含まれています。

それらの情報には、サプライヤによって請求される価格、標準発注数量、過剰納入と不足納入の場合の許容範囲などがあります。このレコードは、購買発注トランザクションで使用されます。

この情報は、特定の購買ユニット (購買組織) と組織内の特定のサイト (プラント) に固有です。

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
| 購買担当者 | SAP_BR_PURCHASER | 購買管理/ソーシングおよび契約 | SAP_MM_SPT_PURCHASING_PC / SAP_MM_SPT_SOURCING_PC |  |

### 必須の組織ユニット

会社の組織構造とマスタデータは、導入時に ERP システムへ登録されます。組織構造は会社の実際の組織構造が反映されています。以下の表は、さまざまなデータセグメントおよび関連する組織ユニットの概要を示しています。

| データセグメント | 依存対象 | 項目例 | コメント | 使用される組織ユニット |
| --- | --- | --- | --- | --- |
| 購買データ | 購買組織 | 購買グループ、品目グループ、GR 処理時間など | 購買データは、品目が購買管理で使用されるすべての購買組織に対して存在可能です。 | 購買組織:__________ |

### 必須マスタデータおよび任意マスタデータ

購買情報レコードは、他のマスタデータを参照する場合があります。以下の表は、購買情報で使用される任意および必須のマスタデータオブジェクトの概要を示しています。

| マスタデータオブジェクト | データセグメントでの使用 | 必須/任意 | コメント |
| --- | --- | --- | --- |
| 品目 |  | 必須 | 品目を入力するには、はじめに品目マスタデータを登録します。 |
| サプライヤ |  | 必須 | 仕入先を入力するには、はじめに仕入先マスタデータを登録します。 |

### データ登録の主要パラメータ

このセクションでは、購買情報のビヘイビアに影響する基本パラメータと、常に購買情報を登録する必要がある基本パラメータについて説明します。

#### 番号範囲

購買情報では、以下の番号範囲が定義されています。

| 番号範囲 | 範囲/ビジネスパートナ ID | コメント |
| --- | --- | --- |
| 内部数値 | 内部数値番号範囲 (基本用途)5300000000 から 5399999999 | この番号範囲は、システムが品目に数値番号を自動的に割り当てるときに使用されます。 |
| 外部数値 | 外部数値番号範囲 (高)5400000000 から 5499999999 | この番号範囲は外部数値番号割当として予約されています。 |

## 概要テーブル

|  |
| --- |
| 注記 システム管理者が SAP Fiori ラウンチパッドでスペースおよびページを有効化している場合、ホームページには、ビジネスロールの一般的なタスクを実行するために必要なアプリのみが含まれます。ホームページに含まれていないその他すべての (検索可能な) アプリは、検索バーを使用して見つけることができます ([2434549](https://me.sap.com/notes/2434549))。ホームページをパーソナライズして非表示のアプリを含める場合は、ユーザプロファイルにナビゲートし、アプリファインダを選択します。 |

| プロセスステップ | ビジネスロール | アプリ/トランザクション | 予想される結果 |
| --- | --- | --- | --- |
| [購買情報登録](#unique_10) [ ページ] 6 | 購買担当者 | 購買情報管理 (F1982) | 購買情報が登録されます。 |
| [受託品/預託品の購買情報の登録](#unique_11) [ ページ] 8 | 購買担当者 | 購買情報管理 (F1982) | 受託の購買情報が登録されます。 |
| [外注の購買情報登録](#unique_12) [ ページ] 10 | 購買担当者 | 購買情報管理 (F1982) | 外注の購買情報が登録されます。 |
| [パイプラインの購買情報の登録](#unique_13) [ ページ] 13 | 購買担当者 | 購買情報管理 (F1982) | パイプラインの購買情報が登録されます。 |
| [購買情報への一括変更](#unique_14) [ ページ] 15 | 購買担当者 | 購買情報の一括変更 (F2667) | 購買情報の一括変更が適用されます。 |
| [購買情報の一括価格変更](#unique_15) [ ページ] 17 | 購買担当者 | 価格変更: 購買情報 | 購買情報の一括価格変更が適用されます。 |

## テスト手順

このセクションでは、このスコープアイテムに属する各プロセスステップのテスト手順について説明します。

### 購買情報登録

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
| 1 | ログオンする | SAP Fiori ラウンチパッドに購買担当者としてログオンします。 | SAP Fiori ラウンチパッドが表示されます。 |  |
| 2 | SAP Fiori アプリにアクセスする | 購買情報管理 (F1982)を開きます。 | 購買情報管理 (F1982)画面が表示されます。 |  |
| 3 | 新規購買情報を開く | 登録を選択します。 | 購買情報画面が表示されます。 |  |
| 4 | ヘッダデータを入力する | 以下のエントリを入力します。購買情報カテゴリ: <標準>購買組織: <購買組織>サプライヤ: <サプライヤ>商品: <品目>サイト: <サイト>購買グループ: <購買グループ> | ヘッダデータが追加されます。 |  |
| 5 | 一般情報を入力する | 以下のエントリを入力します。利用可能開始: YYYY/MM/DD利用可能終了: YYYY/MM/DD | 一般情報が追加されます。 |  |
| 6 | 購買データを入力する | 以下のエントリを入力します。インコタームズ: インコタームズインコタームズロケーション 1: <インコタームズロケーション 1> | 購買データが追加されます。 |  |
| 7 | 納入および数量データを入力する | 以下のエントリを入力します。納入時間 (日数): <XX 日>不足納入許容範囲 (%): <XX>過剰納入許容範囲 (%): <XX>税コード: <税コード>注記 会社コードの国に対して TDT (時間依存の税) が設定ステップ 101016 (定義: 消費税コード) を介して有効化されており、税コードが指定されている場合、税率有効開始項目は必須です。現在の日付を入力することができます。この日付は、設定ステップの設定に従って税コードの有効開始日付に調整されます。RITA (国外の間接課税登録) が有効化されており、設定ステップ 103464 (RITA の有効化および税登録国の更新) で税登録国が会社コードに対して更新され、税コードが指定されている場合、課税国項目は必須です。この項目では、会社コードの国 ID がデフォルト値として指定されますが、設定ステップで更新される有効な国 ID に適宜変更することができます。注記 ご使用の設定環境に応じて、設定ステップには SAP Fiori ラウンチパッドのソリューション設定から、または SAP Central Business Configuration のプロジェクトエクスペリエンスでBusiness Processes Configurationアプリからアクセスできます。発注単位: <発注単位>標準発注数量: <標準発注数量>必要に応じて以下のエントリを選択します。納入無制限入庫基準請求書照合ERS (入庫/請求自動決済) なし購買発注請書依頼確認管理 | 納入および数量データが追加されます。 |  |
| 8 | 条件データを入力する | 条件セクションで、登録アイコンを選択します。以下のデータを入力します。有効開始: <有効開始日付>金額: <金額>価格単位: <価格単位>有効終了: <有効終了日付>通貨: <通貨>適用を選択します。 | 条件データが追加されます。 |  |
| 9 | 参照データを入力する (オプション) | オプションで、参照データを入力できます。 | 参照データが追加されます。 |  |
| 10 | データを保存する | 登録を選択します。 | 購買情報が保存されます。 |  |

### 受託品/預託品の購買情報の登録

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
| 1 | ログオンする | SAP Fiori ラウンチパッドに 購買担当者 としてログオンします。 | SAP Fiori ラウンチパッドが表示されます。 |  |
| 2 | SAP Fiori アプリにアクセスする | 購買情報管理 (F1982) を開きます。 | 購買情報管理画面が表示されます。 |  |
| 3 | 新規購買情報を開く | 登録を選択します。 | 購買情報画面が表示されます。 |  |
| 4 | ヘッダデータを入力する | 以下のエントリを入力します。購買情報カテゴリ:<受託品/預託品>購買組織: <購買組織>サプライヤ: <サプライヤ>品目: <品目>プラント: <プラント>購買グループ: <購買グループ> | ヘッダデータが追加されます。 |  |
| 5 | 一般情報を入力する | 以下のエントリを入力します。利用可能開始: <MM/DD/YYYY>利用可能終了: <MM/DD/YYYY> | 一般情報が追加されます。 |  |
| 6 | 購買データを入力する | 以下のエントリを入力します。インコタームズ: インコタームズインコタームズロケーション 1: <インコタームズロケーション 1> | 購買データが追加されます。 |  |
| 7 | 納入および数量データを入力する | 以下のエントリを入力します。納入時間 (日数): <XX 日>不足納入許容範囲 (%): <XX>過剰納入許容範囲 (%): <XX>税コード: <税コード>注記 会社コードの国に対して TDT (時間依存の税) が設定ステップ 101016 (定義: 消費税コード) を介して有効化されており、税コードが指定されている場合、税率有効開始項目は必須です。現在の日付を入力することができます。この日付は、設定ステップの設定に従って税コードの有効開始日付に調整されます。RITA (国外の間接課税登録) が有効化されており、設定ステップ 103464 (RITA の有効化および税登録国の更新) で税登録国が会社コードに対して更新され、税コードが指定されている場合、課税国項目は必須です。この項目では、会社コードの国 ID がデフォルト値として指定されますが、設定ステップで更新される有効な国 ID に適宜変更することができます。注記 ご使用の設定環境に応じて、設定ステップには SAP Fiori ラウンチパッドのソリューション設定から、または SAP Central Business Configuration のプロジェクトエクスペリエンスでBusiness Processes Configurationアプリからアクセスできます。発注単位: <発注単位>標準発注数量: <標準発注数量> | 納入および数量データが追加されます。 |  |
| 8 | 条件データを入力する | 条件セクションで、登録アイコンを選択します。以下のデータを入力します。有効開始: <有効開始日付>金額: <金額>価格単位: <価格単位>有効終了: <有効終了日付>通貨:<通貨>適用を選択します。 | 条件データが追加されます。 |  |
| 9 | 参照データを入力する (オプション) | オプションで、参照データを入力できます。 | 参照データが追加されます。 |  |
| 10 | データを保存する | 登録を選択します。 | 購買情報が保存されます。 |  |

### 外注の購買情報登録

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
| 1 | ログオンする | SAP Fiori ラウンチパッドに 購買担当者 としてログオンします。 | SAP Fiori ラウンチパッドが表示されます。 |  |
| 2 | SAP Fiori アプリにアクセスする | 購買情報管理 (F1982) を開きます。 | 購買情報管理 (F1982) 画面が表示されます。 |  |
| 3 | 新規購買情報を開く | 登録を選択します。 | 購買情報画面が表示されます。 |  |
| 4 | ヘッダデータを入力する | 以下のエントリを入力します。購買情報カテゴリ:<外注>購買組織: <購買組織>サプライヤ: <サプライヤ>品目: <品目>プラント: <プラント>購買グループ: <購買グループ> | ヘッダデータが追加されます。 |  |
| 5 | 一般情報を入力する | 以下のエントリを入力します。利用可能開始: <MM/DD/YYYY>利用可能終了: <MM/DD/YYYY> | 一般情報が追加されます。 |  |
| 6 | 納入および数量データを入力する | 以下のエントリを入力します。納入時間 (日数): <XX 日>不足納入許容範囲 (%): <XX>過剰納入許容範囲 (%): <XX>税コード: <税コード>注記 会社コードの国に対して TDT (時間依存の税) が設定ステップ 101016 (定義: 消費税コード) を介して有効化されており、税コードが指定されている場合、税率有効開始項目は必須です。現在の日付を入力することができます。この日付は、設定ステップの設定に従って税コードの有効開始日付に調整されます。RITA (国外の間接課税登録) が有効化されており、設定ステップ 103464 (RITA の有効化および税登録国の更新) で税登録国が会社コードに対して更新され、税コードが指定されている場合、課税国項目は必須です。この項目では、会社コードの国 ID がデフォルト値として指定されますが、設定ステップで更新される有効な国 ID に適宜変更することができます。注記 ご使用の設定環境に応じて、設定ステップには SAP Fiori ラウンチパッドのソリューション設定から、または SAP Central Business Configuration のプロジェクトエクスペリエンスでBusiness Processes Configurationアプリからアクセスできます。発注単位: <発注単位>標準発注数量: <標準発注数量> | 納入および数量データが追加されます。 |  |
| 7 | 条件データを入力する | 条件セクションで、登録アイコンを選択します。以下のデータを入力します。有効開始: <有効開始日付>金額: <金額>価格単位: <価格単位>有効終了: <有効終了日付>通貨: <通貨>適用を選択します。 | 条件データが追加されます。 |  |
| 8 | 参照データを入力する (オプション) | オプションで、参照データを入力できます。 | 参照データが追加されます。 |  |
| 9 | データを保存する | 登録を選択します。 | 購買情報が保存されます。 |  |

### パイプラインの購買情報の登録

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
| 1 | ログオンする | SAP Fiori ラウンチパッドに購買担当者としてログオンします。 | SAP Fiori ラウンチパッドが表示されます。 |  |
| 2 | SAP Fiori アプリにアクセスする | 購買情報管理 (F1982)を開きます。 | アプリが開きます。 |  |
| 3 | 新規購買情報を開く | 登録を選択します。 | 購買情報画面が表示されます。 |  |
| 4 | ヘッダデータを入力する | 以下のエントリを入力します。購買情報カテゴリ: <パイプライン>購買組織: <購買組織>サプライヤ: <サプライヤ>品目: <パイプライン品目>プラント: プラント:購買グループ: <購買グループ>品目グループ: <品目グループ>: | ヘッダデータが追加されます。 |  |
| 5 | 一般情報を入力する | 以下のエントリを入力します。利用可能開始: YYYY/MM/DD利用可能終了: YYYY/MM/DD | 一般情報が追加されます。 |  |
| 6 | 購買データを入力する | 以下のエントリを入力します。インコタームズ: インコタームズインコタームズロケーション 1: <インコタームズロケーション 1> | 購買データが追加されます。 |  |
| 7 | 納入および数量データを入力する | 以下のエントリを入力します。納入時間 (日数): <XX 日>不足納入許容範囲 (%): <XX>過剰納入許容範囲 (%): <XX>税コード: <税コード>注記 会社コードの国に対して TDT (時間依存の税) が設定ステップ 101016 (定義: 消費税コード) を介して有効化されており、税コードが指定されている場合、税率有効開始項目は必須です。現在の日付を入力することができます。この日付は、設定ステップの設定に従って税コードの有効開始日付に調整されます。RITA (国外の間接課税登録) が有効化されており、設定ステップ 103464 (RITA の有効化および税登録国の更新) で税登録国が会社コードに対して更新され、税コードが指定されている場合、課税国項目は必須です。この項目では、会社コードの国 ID がデフォルト値として指定されますが、設定ステップで更新される有効な国 ID に適宜変更することができます。注記 ご使用の設定環境に応じて、設定ステップには SAP Fiori ラウンチパッドのソリューション設定から、または SAP Central Business Configuration のプロジェクトエクスペリエンスでBusiness Processes Configurationアプリからアクセスできます。発注単位: <発注単位>標準発注数量: <標準発注数量>必要に応じて以下のエントリを選択します。納入無制限入庫基準請求書照合ERS (入庫/請求自動決済) なし購買発注請書依頼確認管理 | 納入および数量データが追加されます。 |  |
| 8 | 条件データを入力する | 条件セクションで、登録を選択します。以下のデータを入力します。有効開始日: <有効開始日付>金額: <金額>価格単位: <価格単位>有効終了日付: <有効終了日付>通貨: <通貨>適用を選択します。 | 条件データが追加されます。 |  |
| 9 | 参照データを入力する (オプション) | オプションで、参照データを入力できます。 | 参照データが追加されます。 |  |
| 10 | データを保存する | 登録を選択します。 | 購買情報が保存されます。 |  |

### 購買情報への一括変更

テスト管理

カスタマプロジェクト: プロジェクト固有部分への入力

|  |  |  |  |
| --- | --- | --- | --- |
| テストケース ID | <X.XX> | テスト実施日: |  |
| テスト実施者名: |  | 期間: |  |
| ビジネスロール: |  | 責任者: | <都道府県/州、サービスプロバイダ、カスタマ/共同サービスプロバイダ、およびカスタマ> |

目的

この手順では、複数選択した購買情報に一括で変更を適用します。

手順

| テストステップ番号 | テストステップ名 | 指示 | 予想される結果 | 合格/不合格/コメント |
| --- | --- | --- | --- | --- |
| 1. | ログオンする | SAP Fiori ラウンチパッドに購買担当者としてログオンします。 | SAP Fiori ラウンチパッドが表示されます。 |  |
| 2 | SAP Fiori アプリにアクセスする | 購買情報の一括変更 (F2667)を開きます。 | アプリが開きます。 |  |
| 3 | 購買情報を検索する | 購買情報を検索するには、以下の値をフィルタに入力します。サプライヤ: <仕入先 ID>購買グループ: 001 などプラント: <プラント 1 ID>Goを選択します。 | 検索結果に、それぞれのフィルタ基準の詳細が表示されます。デフォルトでは、一括変更操作ではすべての購買情報が選択されています。 |  |
| 4 | 購買情報を選択する | 購買情報および購買組織タブで購買情報チェックボックスを選択します。一括編集を選択します。 |  |  |
| 5 | 新しい値を設定する | 以下のエントリに新規値を入力します。一般データセクション:サプライヤ品目コードサプライヤ品目グループ購買組織データ セクション:購買グループ最小指図数量一括変更適用を選択します。一括変更を確認するダイアログボックスが表示されます。一括変更適用画面で、適用を選択します。ジョブ IDを含むダイアログボックスが表示されます。ジョブ一覧表示を選択します。 | 選択した購買情報に新規値が適用されます。 |  |
| 6 | アプリケーションジョブをチェックする | 検索基準を入力して Go を選択します。すべての購買情報のジョブ ID 一覧を含むアプリケーションジョブ画面が表示されます。ログを選択し、選択した購買情報の成功を確認します。 |  |  |

### 購買情報の一括価格変更

テスト管理

カスタマプロジェクト: プロジェクト固有部分への入力

|  |  |  |  |
| --- | --- | --- | --- |
| テストケース ID | <X.XX> | テスト実施日: |  |
| テスト実施者名: |  | 期間: |  |
| ビジネスロール: |  | 責任者: | <都道府県/州、サービスプロバイダ、カスタマ/共同サービスプロバイダ、およびカスタマ> |

目的

この手順では、価格変更: 購買情報(MEKP)アプリを使用して、購買情報の価格を一括更新します。

手順

| テストステップ番号 | テストステップ名 | 指示 | 予想される結果 | 合格/不合格/コメント |
| --- | --- | --- | --- | --- |
| 1 | ログオンする | SAP Fiori ラウンチパッドに購買担当者としてログオンします。 | SAP Fiori ラウンチパッドが表示されます。 |  |
| 2 | SAP Fiori アプリにアクセスする | 価格変更: 購買情報(MEKP)を開きます。 | アプリが開きます。 |  |
| 3 | 初期データを入力する | 以下のエントリを入力し、実行を選択します。購買組織: <購買組織 ID>サプライヤ: <サプライヤ ID>品目: <品目 ID>購買情報 (品目なし): <空白>テスト実行: <空白>条件タイプまたは基準額変更セクションに移動し、以下のエントリを入力します。条件タイプ: <条件タイプ ID>、PPR0 など絶対額: <絶対額>、10 など符号: <符号>、+ など総額: <空白>スケール行: <X>条件有効セクションに移動し、以下のエントリを入力します。日付: <現在の日付>または開始: <空白>、終了: <空白> | 購買情報が新規の値で更新されます。 |  |
| 4 | 購買情報の変更を確認する | サプライヤ XXXX の購買情報に対する価格変更画面で、古い購買情報と新規購買情報をチェックして変更を確認します。 | 購買情報の価格変更が保存されます。 |  |
| 5 | 終了する | 終了を選択します。 |  |  |

## 付録

### 関連機能

以下は、上記のテスト手順の対象ではない、購買情報に関連する重要なアプリケーション機能の一覧です。

| 機能領域 | 機能 | 詳細情報 | コメント |
| --- | --- | --- | --- |
| 購買情報 | 購買情報関連アプリ | WebGUI: 購買情報削除 (ME15)WebGUI: サプライヤ別購買情報照会 (ME1L)WebGUI: 購買情報の変更の更新 (ME14)WebGUI: 購買条件の更新 (MEKA)WebGUI: 丸めプロファイル更新 (OWD1) |  |

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
- related-to :: [[10-procurement/create-purchasing-info-record-mds-bhd-master-data-script-563]]
- related-to :: [[10-procurement/criar-registro-info-para-compras-mds-bhd-566]]
- related-to :: [[10-procurement/einkaufsinfosatz-anlegen-sds-bhd-stammdatenskript-562]]
- related-to :: [[10-procurement/mds-bhd-567]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/BHD_S4CLD2608_Master_Data_JA_XX.docx` — full document · extracted with `mammoth` · 15,690 chars in the whole document
