---
id: 12-production-and-manufacturing/mds-ble-577
title: 参照作業セットの登録 - MDS (BLE) (BLE_S4CLD2608_Master_Data_JA_XX)
description: "Japanese master data test script (MDS BLE) for creating a reference operation set in SAP S/4HANA Cloud Public Edition 2608 via CA11, Production Engineer role."
cluster: 12-production-and-manufacturing
tags: [kb/production-and-manufacturing, topic/routings-and-reference-operation-sets]
aliases: [BLE_S4CLD2608_Master_Data_JA_XX]
keywords: [Routings and Reference Operation Sets, reference operation set, master data script, routing master data, work center, business roles, control keys, plant organizational data, BLE]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/BLE_S4CLD2608_Master_Data_JA_XX.docx]
confidence: low
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-577
topic: 12-production-and-manufacturing/routings-and-reference-operation-sets
language: JA
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# 参照作業セットの登録 - MDS (BLE) (BLE_S4CLD2608_Master_Data_JA_XX)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/BLE_S4CLD2608_Master_Data_JA_XX.docx`, extracted with `mammoth`. Grouped under **Routings and Reference Operation Sets** in Production and Manufacturing. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

| <!-- image omitted: unnamed --> | マスタデータスクリプトSAP S/4HANA Cloud Public Edition - 02-07-26 |
| --- | --- |
|  | 参照作業セットの登録 - MDS (BLE) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

目次

[1 目的 2](#_Toc233891858)

[2 前提条件 3](#_Toc233891859)

[2.1 システムアクセス 3](#_Toc233891860)

[2.2 ロール 3](#_Toc233891861)

[2.3 必須の組織ユニット 3](#_Toc233891862)

[2.4 必須マスタデータおよび任意マスタデータ 4](#_Toc233891863)

[2.5 データ登録の主要パラメータ 4](#_Toc233891864)

[2.5.1 用途 4](#_Toc233891865)

[3 概要テーブル 5](#_Toc233891866)

[4 テスト手順 6](#_Toc233891867)

[4.1 参照作業手順の登録 6](#_Toc233891868)

## 目的

このプロセスでは、参照作業セットの登録方法について説明します。

参照作業セットの構造は、作業手順と同じ構造です。参照作業セットに製造される品目を割り当てることはできません。並行順序と代替順序のいずれも設定することはできません。

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
| すべてのデータ | プラント |  | 参照作業セットのすべてのデータはプラントによって異なります。 | プラント:__________ |

### 必須マスタデータおよび任意マスタデータ

参照作業手順データレコードは、他のマスタデータを参照する場合があります。以下の表は、参照作業手順で使用される、任意および必須のマスタデータオブジェクトの概要を示しています。

| マスタデータオブジェクト | データセグメントでの使用 | 必須/任意 | コメント |
| --- | --- | --- | --- |
| 品目 |  | 必須 | プロセスステップを実行する前の前提条件として、以下のテストスクリプトを完了します。"原材料" タイプの製品マスタの登録 - MDS (BNR)"半製品" タイプの製品マスタの登録 - MDS (BNS)"最終製品" タイプの製品マスタの登録 - MDS (BNT) |
| 作業区 | 参照作業登録: 作業概要画面で、内部作業の作業区を選択します。 | 必須、(任意) | 外注作業では、作業区は必須の入力項目ではありません。必要な場合は、参照作業セットの登録 - MDS (BLE) テストスクリプトを実行します。 |
| 部品表/配合表 |  | 任意 | 製造および販売向けの品目 BOM の登録 - MDS (BNK) テストスクリプトを実行します。 |
| 購買情報 |  | (必須) | 外注作業では、購買情報を使用して供給に関連するすべてのデータを記録できます。 |

### データ登録の主要パラメータ

このセクションでは、マスタレコードの動作に影響し、参照作業手順の登録に常に必要となる基本パラメータの一部について説明します。

#### 用途

| 作業区カテゴリ | 内容説明 |
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
| [参照作業手順の登録](#unique_10) [ ページ] 6 | 生産エンジニア - ディスクリート製造 | 参照作業手順の登録 (CA11) |  |

## テスト手順

このセクションでは、このスコープアイテムに属する各プロセスステップのテスト手順について説明します。

### 参照作業手順の登録

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
| 1 | ログオンする | SAP Fiori ラウンチパッドに 生産エンジニア - ディスクリート製造 としてログオンします。 | SAP Fiori ラウンチパッドが表示されます。 |  |
| 2 | SAP Fiori アプリにアクセスする | 参照作業手順の登録 (CA11) を開きます。 | 参照作業セット登録: 第一画面が照会されます。 |  |
| 3 | 参照作業セット登録第一画面を設定する | 参照作業セット登録第一画面で、データを入力します。Enter を選択します。 | 参照作業セット登録ヘッダ詳細が表示されます。 |  |
| 4 | 参照作業セット登録ヘッダ詳細画面を設定する | 以下のデータを参照作業セット登録: ヘッダ詳細ビューに入力します。グループカウンタ: <1>プラント: <自分のプラント>用途: <生産の場合は 1>ステータス: <4 リリース済 - 一般>最小ロットサイズ - 最大ロットサイズ: <ロットサイズ間隔と数量単位を入力します> |  |  |
| 5 | 参照作業セット登録: 作業概要を設定する | 作業を選択すると、参照作業セット登録: 作業概要画面が表示されます。以下のデータを参照作業セット登録作業概要画面に入力します。作業区: 内部作業に必要、外注作業の場合は (空白)管理キー: <YBP1/YBP2/YBP3/YBP5/YBRW>YBP1 は自動入庫なしの内部作業YBP2 は外注作業 (PP 外注)YBP1 は自動入庫ありの内部作業YBP5 は製造マイルストーン処理テキスト: <作業の内容説明を入力する>入力した作業をダブルクリックします。 |  |  |
| 6 | 標準値セクションの作業を設定する | 参照作業セット登録: 作業詳細画面で、以下のデータを入力します。段取: <段取時間>機械: <機械作業時間>労力: <労働時間> |  |  |
| 7 | 追加作業を追加する | 作業ごとに前のステップを繰り返します。 |  |  |
| 8 | データを保存する | エントリを保存します。 | 参照作業セットが登録されます。 |  |

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
> Flagged while digesting this document, not verified: Control key description lists YBP1 twice (with and without automatic goods receipt); YBP3 not explained

## Connections
- part-of :: [[_cluster]]
- related-to :: [[12-production-and-manufacturing/master-data-script-create-reference-operation-set-mds-ble-575]]
- related-to :: [[12-production-and-manufacturing/mds-ble-579]]
- related-to :: [[12-production-and-manufacturing/script-de-dados-mestre-criar-conjunto-de-operacoes-de-referencia-mds-b]]
- related-to :: [[12-production-and-manufacturing/script-de-datos-maestros-crear-hoja-de-ruta-estandar-mds-ble-576]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/BLE_S4CLD2608_Master_Data_JA_XX.docx` — full document · extracted with `mammoth` · 6,845 chars in the whole document
