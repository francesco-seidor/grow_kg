---
id: 12-production-and-manufacturing/mds-bnl-631
title: "マスタデータスクリプト: 作業手順の登録 - MDS (BNL) (BNL_S4CLD2608_Master_Data_JA_XX)"
description: "Japanese master data script (MDS BNL) for creating production routings in SAP S/4HANA Cloud Public Edition 2608 via Fiori app F5425, with prerequisites and test steps."
cluster: 12-production-and-manufacturing
tags: [kb/production-and-manufacturing, topic/routings-and-reference-operation-sets]
aliases: [BNL_S4CLD2608_Master_Data_JA_XX]
keywords: [Routings and Reference Operation Sets, production routing, routing master data, master data scripts, business roles, work centers, control keys, external processing, bill of materials, plant data]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/BNL_S4CLD2608_Master_Data_JA_XX.docx]
confidence: low
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-631
topic: 12-production-and-manufacturing/routings-and-reference-operation-sets
language: JA
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# マスタデータスクリプト: 作業手順の登録 - MDS (BNL) (BNL_S4CLD2608_Master_Data_JA_XX)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/BNL_S4CLD2608_Master_Data_JA_XX.docx`, extracted with `mammoth`. Grouped under **Routings and Reference Operation Sets** in Production and Manufacturing. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

| <!-- image omitted: unnamed --> | マスタデータスクリプトSAP S/4HANA Cloud Public Edition - 02-07-26 |
| --- | --- |
|  | 作業手順の登録 - MDS (BNL) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

目次

[1 目的 2](#_Toc233891943)

[2 前提条件 3](#_Toc233891944)

[2.1 システムアクセス 3](#_Toc233891945)

[2.2 ロール 3](#_Toc233891946)

[2.3 必須の組織ユニット 3](#_Toc233891947)

[2.4 必須マスタデータおよび任意マスタデータ 4](#_Toc233891948)

[2.5 データ登録の主要パラメータ 4](#_Toc233891949)

[2.5.1 用途 4](#_Toc233891950)

[3 概要テーブル 6](#_Toc233891951)

[4 テスト手順 7](#_Toc233891952)

[4.1 作業手順登録 7](#_Toc233891953)

## 目的

生産作業手順によって、品目の生産プロセスが定義されます。生産作業手順には、生産時に実行される作業または作業ステップが含まれています。生産作業手順によって、品目および作業の使用が定義されます。生産作業手順は製造指図のテンプレートを作成し、原価積上の基礎となります。

作業手順は、最終製品または半製品に対して定義され、生産サイト (プラントとして知られる) に固有です。作業手順は特定のロットサイズに適用され、それぞれが作業区に割り当てられている複数の作業で構成されます。

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
| 生産エンジニア - ディスクリート製造 | SAP_BR_PRODN_ENG_DISC | 生産エンジニアリング - ディスクリート製造 | SAP_BR_PRODN_ENG_DISC |  |

### 必須の組織ユニット

| データセグメント | 依存対象 | 項目例 | コメント | 使用される組織ユニット |
| --- | --- | --- | --- | --- |
| すべてのデータ | プラント |  | 作業手順のすべてのデータはプラントによって異なります。 | プラント:__________ |

### 必須マスタデータおよび任意マスタデータ

作業手順データレコードは、他のマスタデータを参照する場合があります。以下の表は、作業手順で使用される、任意および必須のマスタデータオブジェクトの概要を示しています。

| マスタデータオブジェクト | データセグメントでの使用 | 必須/任意 | コメント |
| --- | --- | --- | --- |
| 品目 |  | 必須 | プロセスステップを実行する前の前提条件として、以下のテストスクリプトを完了します。"原材料" タイプの製品マスタの登録 - MDS (BNR)"半製品" タイプの製品マスタの登録 - MDS (BNS)"最終製品" タイプの製品マスタの登録 - MDS (BNT) |
| 作業区 | 作業手順登録: 作業概要画面で、内部作業のワークセンタを選択します。 | 必須、(任意) | 外注作業では、ワークセンタは必須の入力項目ではありません。必要な場合は、作業手順の登録 - MDS (BNL) テストスクリプトを実行します。 |
| 部品表/配合表 |  | 任意 | 製造および販売向けの品目 BOM の登録 - MDS (BNK) テストスクリプトを実行します。 |
| 購買情報 |  | (必須) | 外注作業では、購買情報を使用して供給に関連するすべてのデータを記録できます。 |
| 品目グループ |  |  |  |
| 原価要素 |  |  |  |

### データ登録の主要パラメータ

このセクションでは、マスタレコードの動作に影響し、作業手順の登録に常に必要となる基本パラメータの一部について説明します。

#### 用途

| 作業区カテゴリ | 説明 |
| --- | --- |
| 1 | 生産 |
| 2 | 設計/デザイン |
| 3 | 汎用 |

## 概要テーブル

このスコープアイテムは、以下のテーブルに示されているプロセスステップで構成されます。

|  |
| --- |
| 注記 システム管理者が SAP Fiori ラウンチパッドでスペースおよびページを有効化している場合、ホームページには、ビジネスロールの一般的なタスクを実行するために必要なアプリのみが含まれます。ホームページに含まれていないその他すべての (検索可能な) アプリは、検索バーを使用して見つけることができます ([2434549](https://me.sap.com/notes/2434549))。ホームページをパーソナライズして非表示のアプリを含める場合は、ユーザプロファイルにナビゲートし、アプリファインダを選択します。 |

| プロセスステップ | ビジネスロール | トランザクション | 予想される結果 |
| --- | --- | --- | --- |
| [作業手順登録](#unique_10) [ ページ] 7 | 生産エンジニア - ディスクリート製造 | 作業手順管理(F5425) |  |

## テスト手順

このセクションでは、このスコープアイテムに属する各プロセスステップのテスト手順について説明します。

### 作業手順登録

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
| 1 | ログオン | SAP Fiori ラウンチパッドに生産エンジニア - ディスクリート製造としてログオンします。 | SAP Fiori ラウンチパッドが表示されます。 |  |
| 2 | SAP Fiori アプリにアクセスする | 作業手順管理(F5425)を開きます。 | アプリが開きます。 |  |
| 3 | 登録を選択する | 登録を選択します。 | 新しいウィンドウが開いて、作業手順登録画面が表示されます。 |  |
| 4 | 作業手順登録画面を設定する | 作業手順登録画面で、以下のデータを入力します。品目: <最終品目/半製品品目の品目コード>プラント: <プラント番号>続行を選択します。 | 作業手順登録: ヘッダ詳細画面が表示されます。 |  |
| 5 | 作業手順登録を設定する: ヘッダ詳細画面 | 以下のデータを作業手順登録: ヘッダ詳細画面で入力します。用途: <生産の場合は 1>ステータス: <4 リリース済 - 一般>最小ロットサイズ - 最大ロットサイズ: <ロットサイズ間隔と数量単位を入力します> |  |  |
| 6 | 作業手順登録を設定する: 作業概要画面 | 作業ボタンを選択します。作業手順: 作業概要画面が表示されます。以下のデータを作業手順登録: 作業概要画面で入力します。作業区: 内部作業に必要、(空白) 外注作業に必要管理キー: <YBP1/YBP2/YBP3/YBP5>YBP1 は自動入庫なしの内部作業YBP2 は外注作業 (PP 外注)YBP1 は自動入庫ありの内部作業YBP4 は製造マイルストーン処理内容説明: <作業のテキストを入力>入力した作業をダブルクリックします。 |  |  |
| 7 | 外部処理セクション向けに外注作業を設定する | 以下のデータを作業手順登録: 作業詳細画面に入力します。購買情報: 内部作業に必要、(空白) 外注作業に必要品目グループ: L002/L003原価要素: <国に関連する原価要素>購買組織: <購買組織> |  |  |
| 8 | 標準値セクションの内部作業を設定する | 作業手順登録: 作業詳細画面で、以下のデータを入力します。段取: <段取時間>機械: <機械作業時間>労力: <労働時間> |  |  |
| 9 | 追加作業を追加する | 作業ごとに前のステップを繰り返します。 |  |  |
| 10 | 構成品目を選択する | ビューの上部で構成品目割当を選択し、構成品目を選択します。 | 構成品目概要ビューが表示されます。 |  |
| 11 | 新規割当を登録する | 新規割当を選択します。 | 新規割当ダイアログボックスが表示されます。 |  |
| 12 | 作業/活動に割り当てる一覧 | 作業/活動一覧を選択します。 |  |  |
| 13 | 作業を選択する | 作業を選択して Enter キーを押します。 |  |  |
| 14 | その他の構成品目を割り当てる | その他の構成品目について前ステップを繰り返します。 |  |  |
| 15 | データを保存する | エントリを保存します。 | 作業手順が登録されます。 |  |

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
> Flagged while digesting this document, not verified: Control key list in step 6 assigns YBP1 to both internal operation without and with auto goods receipt (YBP3 not described), internally inconsistent

## Connections
- part-of :: [[_cluster]]
- related-to :: [[12-production-and-manufacturing/arbeitsplan-anlegen-sds-bnl-628]]
- related-to :: [[12-production-and-manufacturing/creacion-de-hoja-de-ruta-mds-bnl-630]]
- related-to :: [[12-production-and-manufacturing/criar-roteiro-mds-bnl-632]]
- related-to :: [[12-production-and-manufacturing/master-data-script-create-routing-mds-bnl-629]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/BNL_S4CLD2608_Master_Data_JA_XX.docx` — full document · extracted with `mammoth` · 7,426 chars in the whole document
