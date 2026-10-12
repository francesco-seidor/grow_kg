---
id: 10-procurement/mds-bf6-559
title: "マスタデータスクリプト: 分納契約の登録 - MDS (BF6) (BF6_S4CLD2608_Master_Data_JA_XX)"
description: "Japanese master data/test script (BF6) for creating scheduling agreements (分納契約) in SAP S/4HANA Cloud Public Edition 2608 via app F2179: standard, consignment, subcontracting."
cluster: 10-procurement
tags: [kb/procurement, topic/scheduling-agreements]
aliases: [BF6_S4CLD2608_Master_Data_JA_XX]
keywords: [Purchase Scheduling Agreements, scheduling agreements, standard procurement, consignment procurement, subcontracting procurement, number ranges, business roles, master data prerequisites, test procedures, tax registration country]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/BF6_S4CLD2608_Master_Data_JA_XX.docx]
confidence: high
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-559
topic: 10-procurement/scheduling-agreements
language: JA
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# マスタデータスクリプト: 分納契約の登録 - MDS (BF6) (BF6_S4CLD2608_Master_Data_JA_XX)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/BF6_S4CLD2608_Master_Data_JA_XX.docx`, extracted with `mammoth`. Grouped under **Purchase Scheduling Agreements** in Procurement. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

| <!-- image omitted: unnamed --> | マスタデータスクリプトSAP S/4HANA Cloud Public Edition - 02-07-26 |
| --- | --- |
|  | 分納契約の登録 - MDS (BF6) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

目次

[1 目的 2](#_Toc233891838)

[2 前提条件 3](#_Toc233891839)

[2.1 システムアクセス 3](#_Toc233891840)

[2.2 ロール 3](#_Toc233891841)

[2.3 必須の組織ユニット 3](#_Toc233891842)

[2.4 必須マスタデータおよび任意マスタデータ 4](#_Toc233891843)

[2.5 データ登録の主要パラメータ 4](#_Toc233891844)

[2.5.1 番号範囲 4](#_Toc233891845)

[3 概要テーブル 5](#_Toc233891846)

[4 テスト手順 6](#_Toc233891847)

[4.1 標準調達の分納契約登録 6](#_Toc233891848)

[4.1.1 分納契約 (リリース伝票あり) の登録 - 標準 6](#_Toc233891849)

[4.1.2 分納契約 (リリース伝票なし) の登録 - 標準 8](#_Toc233891850)

[4.2 受託品調達の分納契約登録 10](#_Toc233891851)

[4.3 外注調達の分納契約登録 12](#_Toc233891852)

## 目的

この文書では、SAP S/4HANA Cloud Public Editionシステムに分納契約を登録する方法について説明します。説明には、購買データ、品目データ、およびサプライヤデータなど、SAP S/4HANA Cloud Public Editionアプライアンスに関連するデータセグメントも含まれます。SAP Best Practicesによって提供されるSAP S/4HANA Cloud Public Editionの範囲に関連しない項目については、この文書では説明していません。

分納契約は、事前定義済の条件による品目の供給に対応する仕入先との長期契約です。条件は、事前定義済の期間と事前定義済の合計数量に対して有効です。

分納契約の主な利点は次のとおりです。

- 多額の購買発注または契約リリースを分納契約に置き換えることができます。
- 分納契約は長期契約であり、仕入先との有利な価格交渉を可能にします。

以下の明細カテゴリがあります。

- 標準調達
- 受託品調達
- 外注調達

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

分納契約は、他のマスタデータを参照する場合があります。以下の表は、分納契約で使用される任意および必須のマスタデータオブジェクトの概要を示しています。

| マスタデータオブジェクト | データセグメントでの使用 | 必須/任意 | コメント |
| --- | --- | --- | --- |
| 品目 |  | 必須 | 品目を入力するには、はじめに品目マスタデータを登録します。 |
| サプライヤ |  | 必須 | 仕入先を入力するには、はじめに仕入先マスタデータを登録します。 |

### データ登録の主要パラメータ

このセクションでは、分納契約の動作に影響する基本パラメータと、常に分納契約を登録する必要がある基本パラメータについて説明します。

#### 番号範囲

分納契約では、以下の番号範囲が定義されています。

| 番号範囲 | 範囲/ビジネスパートナ ID | コメント |
| --- | --- | --- |
| 内部数値 | 内部数値番号範囲 (基本用途)5500000000 から 5599999999 | この番号範囲は、システムが分納契約に数値番号を自動的に割り当てるときに使用されます。 |
| 外部数値 | 外部数値番号範囲:5600000000 から 5699999999 | この番号範囲は外部数値番号割当として予約されています。 |

## 概要テーブル

|  |
| --- |
| 注記 システム管理者が SAP Fiori ラウンチパッドでスペースおよびページを有効化している場合、ホームページには、ビジネスロールの一般的なタスクを実行するために必要なアプリのみが含まれます。ホームページに含まれていないその他すべての (検索可能な) アプリは、検索バーを使用して見つけることができます ([2434549](https://me.sap.com/notes/2434549))。ホームページをパーソナライズして非表示のアプリを含める場合は、ユーザプロファイルにナビゲートし、アプリファインダを選択します。 |

| プロセスステップ | ビジネスロール | アプリ/トランザクション | 予想される結果 |
| --- | --- | --- | --- |
|  |  |  |  |
| [分納契約 (リリース伝票あり) の登録 - 標準](#unique_10) [ ページ] 6 | 購買担当者 | 購買分納契約の管理 (F2179) | 分納契約 (リリース伝票あり) - 標準 |
| [分納契約 (リリース伝票なし) の登録 - 標準](#unique_11) [ ページ] 8 | 購買担当者 | 購買分納契約の管理 (F2179) | 分納契約 (リリース伝票なし) - 標準 |
| [受託品調達の分納契約登録](#unique_12) [ ページ] 10 | 購買担当者 | 購買分納契約の管理 (F2179) | 受託品調達の分納契約が登録されます。 |
| [外注調達の分納契約登録](#unique_13) [ ページ] 12 | 購買担当者 | 購買分納契約の管理 (F2179) | 外注調達の分納契約が登録されます。 |

## テスト手順

このセクションでは、このスコープアイテムに属する各プロセスステップのテスト手順について説明します。

### 標準調達の分納契約登録

#### 分納契約 (リリース伝票あり) の登録 - 標準

テスト管理

カスタマプロジェクト: プロジェクト固有部分への入力

|  |  |  |  |
| --- | --- | --- | --- |
| テストケース ID | <X.XX> | テスト実施日: |  |
| テスト実施者名: |  | 期間: |  |
| ビジネスロール: |  | 責任者: | <都道府県/州、サービスプロバイダ、カスタマ/共同サービスプロバイダ、およびカスタマ> |

目的

標準調達の分納契約を登録します。

手順

| テストステップ番号 | テストステップ名 | 指示 | 予想される結果 | 合格/不合格/コメント |
| --- | --- | --- | --- | --- |
| 1. | ログオンする | SAP Fiori ラウンチパッドに購買担当者としてログオンします。 | SAP Fiori ラウンチパッドが表示されます。 |  |
| 2 | SAP Fiori アプリにアクセスする | 購買分納契約の管理 (F2179)を開きます。 | アプリが開きます。 |  |
| 3 | 分納契約を登録する | 登録を選択して新しい分納契約を登録します。 | 新規購買分納契約画面が表示されます。 |  |
| 4 | ヘッダデータを入力する | 以下のデータで新規分納契約を登録します。サプライヤ: <サプライヤ>契約タイプ: LPA (分納契約 (リリース伝票あり))有効期間開始: <YYYY/MM/DD>有効終了: <YYYY/MM/DD>会社コード: <会社コード>購買組織: <購買組織>購買グループ: <購買グループ>目標額: <目標額> |  |  |
| 5 | ヘッダノートを入力する | ノートセクションに移動し、以下のヘッダノートの一部を入力します。ヘッダテキストヘッダノート価格設定タイプ期限納入条件出荷指示支払条件保証契約不履行時のペナルティ製品保証契約付加条項資産その他契約規定入荷伝票仕入先メモ (一般)仕入先メモ (購買組織) |  |  |
| 6 | 分納契約に明細を追加する | 新規購買分納契約画面で、明細ファセットを選択し、登録を選択します。 | 購買分納契約明細画面が表示されます。 |  |
| 7 | 明細データを入力する | 明細ファセット画面で、以下のエントリを入力します。プラント: <プラント>品目: <品目>目標数量: <目標数量>正味発注価格: <正味発注価格>税コード: <XX (購買情報からのデフォルト値)>税日付: <本日の日付をデフォルト値として使用>出力管理セクションで、以下のエントリを入力します。登録プロファイル: <登録プロファイル>画面下部の適用を選択します。 |  |  |
| 8 | 登録する | 新規購買分納契約画面に戻って、画面の下部にある登録を選択します。分納契約番号を書き留めます。 | 分納契約が登録されます。 |  |

#### 分納契約 (リリース伝票なし) の登録 - 標準

テスト管理

カスタマプロジェクト: プロジェクト固有部分への入力

|  |  |  |  |
| --- | --- | --- | --- |
| テストケース ID | <X.XX> | テスト実施日: |  |
| テスト実施者名: |  | 期間: |  |
| ビジネスロール: |  | 責任者: | <都道府県/州、サービスプロバイダ、カスタマ/共同サービスプロバイダ、およびカスタマ> |

目的

標準調達の分納契約を登録します。

手順

| テストステップ番号 | テストステップ名 | 指示 | 予想される結果 | 合格/不合格/コメント |
| --- | --- | --- | --- | --- |
| 1. | ログオンする | SAP Fiori ラウンチパッドに購買担当者としてログオンします。 | SAP Fiori ラウンチパッドが表示されます。 |  |
| 2 | SAP Fiori アプリにアクセスする | 購買分納契約の管理 (F2179)を開きます。 | 購買分納契約の管理 (F2179)一覧ページが表示されます。 |  |
| 3 | 分納契約を登録する | 登録を選択して新しい分納契約を登録します。 | 新規購買分納契約ヘッダビューが表示されます。 |  |
| 4 | ヘッダデータを入力する | 以下のデータで新規分納契約を登録します。サプライヤ: <サプライヤ>契約タイプ: LP (分納契約)有効期間開始: <YYYY/MM/DD>有効終了: <YYYY/MM/DD>会社コード: <会社コード>購買組織: <購買組織>購買グループ: <購買グループ>目標額: <目標額> |  |  |
| 5 | ヘッダノートを入力する | ノートセクションにナビゲートし、以下のヘッダノートの一部を入力します。ヘッダテキストヘッダノート価格設定タイプ期限納入条件出荷指示支払条件保証契約不履行時のペナルティ製品保証契約付加条項資産その他契約規定入荷伝票仕入先メモ (一般)仕入先メモ (購買組織) |  |  |
| 6 | 分納契約に明細を追加する | 新規購買分納契約ビューで、明細ファセットを選択し、登録を選択します。 | 購買分納契約明細ビューが表示されます。 |  |
| 7 | 明細データを入力する | 明細ファセット画面で、以下のエントリを入力します。プラント: <プラント>品目: <品目>目標数量: <目標数量>正味発注価格: <正味発注価格>税コード: <XX (購買情報からのデフォルト値)>税日付: <本日の日付をデフォルト値として使用>画面下部の適用を選択します。 |  |  |
| 8 | 登録する | 新規購買分納契約ヘッダビューに戻って、ビューの下部にある登録を選択します。分納契約番号を書き留めます。 | 分納契約が登録されます。 |  |

### 受託品調達の分納契約登録

テスト管理

カスタマプロジェクト: プロジェクト固有部分への入力

|  |  |  |  |
| --- | --- | --- | --- |
| テストケース ID | <X.XX> | テスト実施日: |  |
| テスト実施者名: |  | 期間: |  |
| ビジネスロール: |  | 責任者: | <都道府県/州、サービスプロバイダ、カスタマ/共同サービスプロバイダ、およびカスタマ> |

目的

受託品調達の分納契約を登録します。

手順

| テストステップ番号 | テストステップ名 | 指示 | 予想される結果 | 合格/不合格/コメント |
| --- | --- | --- | --- | --- |
| 1 | ログオンする | SAP Fiori ラウンチパッドに 購買担当者 としてログオンします。 | SAP Fiori ラウンチパッドが表示されます。 |  |
| 2 | SAP Fiori アプリにアクセスする | 購買分納契約の管理 (F2179)を開きます。 | 分納契約管理一覧ページが表示されます。 |  |
| 3 | 分納契約を登録する | 登録を選択して新しい分納契約を登録します。 | 新規分納契約ヘッダビューが表示されます。 |  |
| 4 | ヘッダデータを入力する | 以下のデータで新規分納契約を登録します。購買契約タイプ: LP (分納契約)サプライヤ: <サプライヤ>有効期間開始: デフォルトの本日有効期間終了: YYYY/MM/DD (本日 + 720 日など)購買グループ: <購買グループ>購買組織: <購買組織>会社コード: <会社コード>目標額: 例: XXXXX EUR |  |  |
| 5 | 分納契約に明細を追加する | 新規購買分納契約ビューで、明細ファセットを選択し、登録を選択します。 | 新規分納契約明細ビューが表示されます。 |  |
| 6 | 明細データを入力する | 明細ファセットビューで、以下のエントリを入力します。明細カテゴリ: K (受託品/預託品)プラント: プラント:品目: <品目>目標数量: <目標数量>税コード: XX (購買情報からのデフォルト値)税日付: デフォルトの本日注記 RITA が有効化されており、財務の設定ステップ 103464 (RITA の有効化および税登録国の更新) で税登録国が会社コードに対して更新されている場合、課税国を取得することができます。また、一覧から異なる課税国の値を選択することもできます。注記 ご使用の設定環境に応じて、設定ステップには SAP Fiori ラウンチパッドのソリューション設定から、または SAP Central Business Configuration のプロジェクトエクスペリエンスでBusiness Processes Configurationアプリからアクセスできます。ビューの下部にある適用を選択します。 |  |  |
| 7 | 登録する | 新規購買分納契約ビューに戻って、ビューの下部にある登録を選択します。分納契約番号を書き留めます。 | 分納契約が登録されます。 |  |

### 外注調達の分納契約登録

テスト管理

カスタマプロジェクト: プロジェクト固有部分への入力

|  |  |  |  |
| --- | --- | --- | --- |
| テストケース ID | <X.XX> | テスト実施日: |  |
| テスト実施者名: |  | 期間: |  |
| ビジネスロール: |  | 責任者: | <都道府県/州、サービスプロバイダ、カスタマ/共同サービスプロバイダ、およびカスタマ> |

目的

外注調達の分納契約を登録します。

手順

| テストステップ番号 | テストステップ名 | 指示 | 予想される結果 | 合格/不合格/コメント |
| --- | --- | --- | --- | --- |
| 1 | ログオンする | SAP Fiori ラウンチパッドに 購買担当者 としてログオンします。 | SAP Fiori ラウンチパッドが表示されます。 |  |
| 2 | SAP Fiori アプリにアクセスする | 購買分納契約の管理 (F2179)を開きます。 | 分納契約管理一覧ページが表示されます。 |  |
| 3 | 分納契約を登録する | 登録を選択して新しい分納契約を登録します。 | 新規分納契約ヘッダビューが表示されます。 |  |
| 4 | ヘッダデータを入力する | 以下のデータで新規分納契約を登録します。購買契約タイプ: LP (分納契約)サプライヤ: <サプライヤ>有効期間開始: デフォルトの本日有効期間終了: YYYY/MM/DD (本日 + 720 日など)購買グループ: <購買グループ>購買組織: <購買組織>会社コード: <会社コード>目標額: 例: XXXXX EUR |  |  |
| 5 | 分納契約に明細を追加する | 新規購買分納契約ビューで、明細ファセットを選択し、登録を選択します。 | 新規分納契約明細ビューが表示されます。 |  |
| 6 | 明細データを入力する | 明細ファセットビューで、以下のエントリを入力します。明細カテゴリ: L (外注)プラント: プラント:保管場所: <保管場所>品目: <品目>正味発注価格: 購買情報からのデフォルト値目標数量: <目標数量>税コード: XX (購買情報からのデフォルト値)税日付: デフォルトの本日注記 RITA が有効化されており、財務の設定ステップ 103464 (RITA の有効化および税登録国の更新) で税登録国が会社コードに対して更新されている場合、課税国を取得することができます。また、一覧から異なる課税国の値を選択することもできます。注記 ご使用の設定環境に応じて、設定ステップには SAP Fiori ラウンチパッドのソリューション設定から、または SAP Central Business Configuration のプロジェクトエクスペリエンスでBusiness Processes Configurationアプリからアクセスできます。ビューの下部にある適用を選択します。 |  |  |
| 7 | 登録する | 新規購買分納契約ビューに戻って、ビューの下部にある登録を選択します。分納契約番号を書き留めます。 | 分納契約が登録されます。 |  |

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
- related-to :: [[10-procurement/master-data-script-create-scheduling-agreement-mds-bf6-557]]
- related-to :: [[10-procurement/mds-bf6-561]]
- related-to :: [[10-procurement/script-de-dados-mestre-criar-programa-de-remessas-mds-bf6-560]]
- related-to :: [[10-procurement/script-de-datos-maestros-creacion-de-plan-de-entregas-mds-bf6-558]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/BF6_S4CLD2608_Master_Data_JA_XX.docx` — full document · extracted with `mammoth` · 11,717 chars in the whole document
