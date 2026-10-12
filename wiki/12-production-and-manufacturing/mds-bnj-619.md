---
id: 12-production-and-manufacturing/mds-bnj-619
title: 製造作業区の登録 - MDS (BNJ) (BNJ_S4CLD2608_Master_Data_JA_XX)
description: Japanese SAP S/4HANA Cloud Public Edition master data script (BNJ) for creating production work centers and work center groups with F6175 and F4044.
cluster: 12-production-and-manufacturing
tags: [kb/production-and-manufacturing, topic/production-work-centers]
aliases: [BNJ_S4CLD2608_Master_Data_JA_XX]
keywords: [Production Work Centers and Work Center Groups, work centers, work center groups, work center categories, capacity planning, scheduling and costing, standard value keys, business roles, master data scripts, routings]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/BNJ_S4CLD2608_Master_Data_JA_XX.docx]
confidence: high
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-619
topic: 12-production-and-manufacturing/production-work-centers
language: JA
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# 製造作業区の登録 - MDS (BNJ) (BNJ_S4CLD2608_Master_Data_JA_XX)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/BNJ_S4CLD2608_Master_Data_JA_XX.docx`, extracted with `mammoth`. Grouped under **Production Work Centers and Work Center Groups** in Production and Manufacturing. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

| <!-- image omitted: unnamed --> | マスタデータスクリプトSAP S/4HANA Cloud Public Edition - 02-07-26 |
| --- | --- |
|  | 製造作業区の登録 - MDS (BNJ) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

目次

[1 目的 2](#_Toc233891962)

[2 前提条件 3](#_Toc233891963)

[2.1 システムアクセス 3](#_Toc233891964)

[2.2 ロール 3](#_Toc233891965)

[2.3 必須の組織ユニット 3](#_Toc233891966)

[2.4 必須マスタデータおよび任意マスタデータ 4](#_Toc233891967)

[2.5 データ登録の主要パラメータ 4](#_Toc233891968)

[2.5.1 作業区カテゴリ 4](#_Toc233891969)

[3 概要テーブル 5](#_Toc233891970)

[4 テスト手順 6](#_Toc233891971)

[4.1 作業区の登録 6](#_Toc233891972)

[4.2 作業区グループの管理 (オプション) 8](#_Toc233891973)

[4.2.1 作業区グループの登録 (オプション) 8](#_Toc233891974)

[4.2.2 作業区の割当 (オプション) 9](#_Toc233891975)

[5 付録 11](#_Toc233891976)

[5.1 作業手順登録 11](#_Toc233891977)

## 目的

作業区は、生産処理が実行される場所です。たとえば、作業区は生産ライン、機械、機械グループ、従業員、または従業員グループを表すことがあります。

作業区では、能力計画 (利用可能能力など)、日程計画 (処理時間の計算式など) および原価計算 (原価センタなど) に使用される情報が保持されます。この情報はタスクリストおよび生産作業指図などのトランザクションで使用されます。情報は生産サイト (プラントと呼ばれます) に固有です。

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
| すべてのデータ | プラント |  | 作業区のすべてのデータはプラントによって異なります。 | プラント:__________ |

### 必須マスタデータおよび任意マスタデータ

作業区マスタデータレコードは他のマスタデータを参照することがあります。以下の表は、作業区で使用される任意および必須のマスタデータオブジェクトの概要を示しています。

| マスタデータオブジェクト | データセグメントでの使用 | 必須/任意 | コメント |
| --- | --- | --- | --- |
| 標準値キー | 作業区 UI では、基本データタブの標準値更新セクションに標準値キーが表示されます。 | 必須 | 実行時間、能力所要量、および原価の計算式では、元の標準値のパラメータとして標準値が使用されます。標準値キーを使用して、パラメータ ID を標準値に割り当てます。このパラメータ ID は、計算式内の標準値を識別します。このパラメータ ID を使用して、段取、マシン、労働など、標準値のキーワードを決定できます。 |

### データ登録の主要パラメータ

このセクションでは、マスタレコードの動作に影響し、作業区の登録に必ず必要となる基本パラメータの一部について説明します。

#### 作業区カテゴリ

作業区カテゴリは、作業区マスタレコード内のどのデータが更新されるのかを示します。作業区をカテゴリで区別できます (たとえば、製造作業区、保全作業区、サービス作業区など)。

| 作業区カテゴリ | 説明 |
| --- | --- |
| 0001 | マシン |
| 0007 | 生産ライン |

## 概要テーブル

このスコープアイテムは、以下の表に示されている複数のプロセスステップで構成されます。

|  |
| --- |
| 注記 システム管理者が SAP Fiori ラウンチパッドでスペースおよびページを有効化している場合、ホームページには、ビジネスロールの一般的なタスクを実行するために必要なアプリのみが含まれます。ホームページに含まれていないその他すべての (検索可能な) アプリは、検索バーを使用して見つけることができます ([2434549](https://me.sap.com/notes/2434549))。ホームページをパーソナライズして非表示のアプリを含める場合は、ユーザプロファイルにナビゲートし、アプリファインダを選択します。 |

| プロセスステップ | ビジネスロール | トランザクション | 予想される結果 |
| --- | --- | --- | --- |
| [作業区の登録](#unique_10) [ ページ] 6 | 生産エンジニア - ディスクリート製造 | ワークセンタの管理(F6175) |  |
| [作業区グループの登録 (オプション)](#unique_11) [ ページ] 8 | 生産エンジニア - ディスクリート製造 | 作業区グループ管理 (F4044) |  |
| [作業区の割当 (オプション)](#unique_12) [ ページ] 9 | 生産エンジニア - ディスクリート製造 | 作業区グループ管理 (F4044) |  |

## テスト手順

このセクションでは、このスコープアイテムに属する各プロセスステップのテスト手順について説明します。

### 作業区の登録

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
| 1 | ログオンする | SAP Fiori ラウンチパッドに 生産エンジニア - ディスクリート製造 としてログオンします。 | SAP Fiori ラウンチパッドが表示されます。 |  |
| 2 | SAP Fiori アプリを開く | ワークセンタの管理(F6175)を選択します。 |  |  |
| 3 | 登録を選択する | 登録を選択します。 | 新しい画面が表示され、作業区登録: 第一画面が表示されます。 |  |
| 4 | プラントコードを入力する | プラントコードを入力します。 | 組織登録画面が表示されます。 |  |
| 5 | 作業区 ID を入力する | 作業区 ID を入力します。注記 作業区 ID の項目長は 8 未満です。 |  |  |
| 6 | 作業区カテゴリ | 作業区カテゴリを選択します。<0001> 機械<0007> 生産ライン |  |  |
| 7 | 基本データを選択する | 画面の左上隅の基本データボタンを選択します。 | 作業区登録: 基本データ画面が表示されます。 |  |
| 8 | データを入力する | 基本データタブで、以下のデータを入力します。テキスト: <テキストを入力>責任者: <責任者またはプラントの責任者>用途: <009>標準値キー: <SAP1> |  |  |
| 9 | 能力および処理計算式を設定する | 能力タブで、以下のデータを入力します。能力カテゴリ: <001 (機械)/002 (個人)>段取計算式: <SAP005>処理計算式: <SAP006>Enterキーを押します。 | 作業区能力登録: ヘッダ画面が表示されます。 |  |
| 10 | 作業区能力を設定する | 作業区能力: ヘッダセクションで、以下のデータを入力します。能力カテゴリテキスト: <内容説明を追加します>能力責任者: F4を押してプラントの責任者を検索します。稼働日カレンダ ID: <国のカレンダ>有効バージョン: <1>能力基本単位: Dなど開始時刻<開始時刻>終了時刻<終了時刻>休憩時間の長さ: <休憩時間の長さ>作業時間: <作業時間>能力利用度: <100>個別能力数: <10>有限計画関連: <X>長期計画: <X>複数作業使用可能: <X>Enterキーを押します。 | 画面は能力概要に戻ります。 |  |
| 11 | 日程計画データを入力する | 日程計画タブで、以下のデータを入力します。能力カテゴリ: <001 (機械)/002 (個人)>段取時間: <SAP001>処理期間: <SAP002> |  |  |
| 12 | 原価計算データを入力する | 原価計算タブページで、以下のデータを入力します。原価センタ: <会社コードの原価センタ>活動タイプ (段取用): <3>計算式 (段取用): <SAP005>活動タイプ (機械): <1>計算式 (機械): <SAP006>活動タイプ (労働): <11>計算式 (労働): <SAP007>活動単位: 必要な UOM を選択 (分など) |  |  |
| 13 | データを保存する | エントリを保存します。 |  |  |

### 作業区グループの管理 (オプション)

目的

この章では、必要に応じて作業区をグループ化する方法について説明します。

#### 作業区グループの登録 (オプション)

テスト管理

カスタマプロジェクト: プロジェクト固有部分への入力

|  |  |  |  |
| --- | --- | --- | --- |
| テストケース ID | <X.XX> | テスト実施日: |  |
| テスト実施者名: |  | 期間: |  |
| ビジネスロール: |  | 責任者: | <都道府県/州、サービスプロバイダ、カスタマ/共同サービスプロバイダ、およびカスタマ> |

目的

このプロセスステップでは、作業区グループの登録方法を示します。

スコープアイテム31Lのプロセスステップ作業区グループの登録および割当で登録されたサンプル作業区グループを確認することができます。

手順

| テストステップ番号 | テストステップ名 | 指示 | 予想される結果 | 合格/不合格/コメント |
| --- | --- | --- | --- | --- |
| 1 | ログオンする | SAP Fiori ラウンチパッドに 生産エンジニア - ディスクリート製造 としてログオンします。 | SAP Fiori ラウンチパッドが表示されます。 |  |
| 2 | アプリにアクセスする | 作業区グループ管理 (F4044) を開きます。 | アプリが開きます。 |  |
| 3 | グループを登録する | テーブルの上の登録を選択します。グループ登録画面で、以下のエントリを入力します。グループ: <グループ名を入力>プラント: 1010グループタイプ: <ALTERNATIV>、<SAME LINE>、または <RSPONSBLTY>テキスト: <テキストを入力>登録を選択します。 | 作業区グループが登録されます。 |  |

#### 作業区の割当 (オプション)

テスト管理

カスタマプロジェクト: プロジェクト固有部分への入力

|  |  |  |  |
| --- | --- | --- | --- |
| テストケース ID | <X.XX> | テスト実施日: |  |
| テスト実施者名: |  | 期間: |  |
| ビジネスロール: |  | 責任者: | <都道府県/州、サービスプロバイダ、カスタマ/共同サービスプロバイダ、およびカスタマ> |

目的

このプロセスステップは、作業区を作業区グループに割り当てる方法を示します。

手順

| テストステップ番号 | テストステップ名 | 指示 | 予想される結果 | 合格/不合格/コメント |
| --- | --- | --- | --- | --- |
| 1 | ログオンする | SAP Fiori ラウンチパッドに 生産エンジニア - ディスクリート製造 としてログオンします。 | SAP Fiori ラウンチパッドが表示されます。 |  |
| 2 | アプリにアクセスする | 作業区グループ管理 (F4044) を開きます。 | アプリが開きます。 |  |
| 3 | グループを選択する | 前のステップで登録されたグループを検索して、行の最後にある > アイコンを選択します。 | 詳細情報一覧が右側パネルに表示されます。 |  |
| 4 | 作業区を割り当てる | グループ構成セクションで、作業区割当を選択します。1 つまたはいくつかの作業区をダイアログボックスから選択し、OKを選択します。注記 作業区がすでに別のグループに割り当てられている場合は、エラーメッセージ: 作業区 "XXX" はすでにこのグループタイプに割り当てられていますが表示されます。 | グループに割り当てられた作業区が表示されます。作業区が正常に割り当てられます。 |  |

## 付録

### 作業手順登録

| マスタデータオブジェクト | データセグメントでの使用 | 必須/任意 | コメント |
| --- | --- | --- | --- |
| 作業手順 |  |  | この活動を実行するには、作業手順の登録 - MDS (BNL) テストスクリプトを実行します。 |

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
- related-to :: [[12-production-and-manufacturing/create-production-work-center-mds-bnj-617]]
- related-to :: [[12-production-and-manufacturing/mds-bnj-621]]
- related-to :: [[12-production-and-manufacturing/script-de-dados-mestre-criar-centro-de-trabalho-da-producao-mds-bnj-62]]
- related-to :: [[12-production-and-manufacturing/script-de-datos-maestros-crear-puesto-de-trabajo-de-produccion-mds-bnj]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/BNJ_S4CLD2608_Master_Data_JA_XX.docx` — full document · extracted with `mammoth` · 9,432 chars in the whole document
