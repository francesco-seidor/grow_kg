---
id: 14-maintenance-service-and-projects/mds-5mh-463
title: 保全作業区の登録 - MDS (5MH) (5MH_S4CLD2608_Master_Data_JA_XX)
description: "Japanese SAP S/4HANA Cloud 2608 master data script 5MH: create a plant maintenance work center with app CR01 as production engineer, including capacity and costing data."
cluster: 14-maintenance-service-and-projects
tags: [kb/maintenance-service-and-projects, topic/maintenance-work-centers]
aliases: [5MH_S4CLD2608_Master_Data_JA_XX]
keywords: [Maintenance Work Centers, work center, plant maintenance, master data scripts, work center category, standard value key, work center capacity, business roles, 5MH]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/5MH_S4CLD2608_Master_Data_JA_XX.docx]
confidence: high
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-463
topic: 14-maintenance-service-and-projects/maintenance-work-centers
language: JA
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# 保全作業区の登録 - MDS (5MH) (5MH_S4CLD2608_Master_Data_JA_XX)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/5MH_S4CLD2608_Master_Data_JA_XX.docx`, extracted with `mammoth`. Grouped under **Maintenance Work Centers** in Maintenance, Service and Projects. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

| <!-- image omitted: unnamed --> | マスタデータスクリプトSAP S/4HANA Cloud Public Edition - 02-07-26 |
| --- | --- |
|  | 保全作業区の登録 - MDS (5MH) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

目次

[1 目的 2](#_Toc233891741)

[2 前提条件 3](#_Toc233891742)

[2.1 システムアクセス 3](#_Toc233891743)

[2.2 ロール 3](#_Toc233891744)

[2.3 必須の組織ユニット 3](#_Toc233891745)

[2.4 必須マスタデータおよび任意マスタデータ 4](#_Toc233891746)

[2.5 データ登録の主要パラメータ 4](#_Toc233891747)

[2.5.1 作業区カテゴリ 4](#_Toc233891748)

[3 概要テーブル 5](#_Toc233891749)

[4 手順 6](#_Toc233891750)

[4.1 保全作業区の登録 6](#_Toc233891751)

## 目的

この文書では、S/4HANA システムで保全作業区マスタデータレコードを登録する方法について説明します。この説明には、"標準的" なシステム環境で処理するマスタデータに関連するデータセグメントが含まれています。読者は、通常、入力値を入力する必要があるデータセグメントおよび項目について主に学習します。SAP Best Practices による S/4HANA コンテンツ配信の範囲に関連しない項目については、ユーザインタフェース (UI) に表示される場合もありますが、この文書では説明されていません。

この説明に従って登録される保全作業区は、保全処理で使用することができます。

## 前提条件

このセクションでは、作業区を登録するためのすべての前提条件の概要を示します。

### システムアクセス

テストは以下のシステムを使用して実施する必要があります。

表 1:

| システム | 詳細 |
| --- | --- |
| システム | SAP Fiori ラウンチパッドからアクセスすることができます。各自のロールに割り当てられている各種アプリにアクセスするための URL がシステム管理者から提供されます。 |

### ロール

SAP から提供される以下のビジネスロールテンプレートを使用して、ビジネスロールを登録し、それらを個別のテストユーザに割り当てます。

または、利用可能な場合は、SAP から提供される以下のスペースを使用することができます。スペーステンプレートを使用して、必要な事前定義済アプリを含むページのあるスペースを登録し、それをビジネスロールに割り当てます。その後、このビジネスロールを個別のユーザに割り当てます。

詳細については、SAP S/4HANA Cloud Public Editionの[Product Assistance](https://help.sap.com/docs/SAP_S4HANA_CLOUD/53e36b5493804bcdb3f6f14de8b487dd/ec310a8b669a45ca898dc4dd91d97de2.html)でテンプレートからのビジネスロールの作成方法を参照してください。

| 名称 (ロールテンプレート) | ID (ロールテンプレート) | 名称 (スペース) | ID (スペース) |
| --- | --- | --- | --- |
| 生産エンジニア - ディスクリート製造 | SAP_BR_PRODN_ENG_DISC | 生産エンジニアリング - ディスクリート製造 | SAP_BR_PRODN_ENG_DISC |

### 必須の組織ユニット

マスタデータの一部のセグメントは会社の組織ユニットに依存し、一般 (共通) データは組織ユニットまたは会社コードに依存しません。以下の表は、さまざまなデータセグメントおよび関連する組織ユニットの概要を示しています。

| データセグメント | 依存対象 | 項目例 | コメント | 使用される組織ユニット |
| --- | --- | --- | --- | --- |
| すべてのデータ | プラント |  | 作業区のすべてのデータはプラントによって異なります。 | プラント: –––––-- |

### 必須マスタデータおよび任意マスタデータ

作業区データレコードは、他のマスタデータを参照する場合があります。以下の表は、作業区で使用される任意および必須のマスタデータオブジェクトの概要を示しています。

| マスタデータオブジェクト | データセグメントでの使用 | 必須/任意 | コメント |
| --- | --- | --- | --- |
| 標準値キー | 作業区画面の基本データタブ標準値更新セクションで、標準値キーのエントリを確認できます。 | 必須 | 実行時間、能力所要量、および原価の計算式では、元の標準値のパラメータとして標準値が使用されます。標準値キーを使用して、パラメータ ID を標準値に割り当てます。このパラメータ ID は、計算式内の標準値を識別します。このパラメータ ID を使用して、段取、マシン、労働など、標準値のキーワードを決定できます。 |

### データ登録の主要パラメータ

このセクションでは、マスタレコードの動作に影響し、保全作業区の登録に必ず必要となる基本パラメータの一部について説明します。

#### 作業区カテゴリ

作業区カテゴリは、作業区マスタレコード内のどのデータが更新されるのかを示します。作業区をカテゴリで区別できます (たとえば、製造作業区、保全作業区、サービス作業区など)。

表 2:

| 作業区カテゴリ | 説明 |
| --- | --- |
| 0005 | プラント保全 |

## 概要テーブル

このスコープアイテムは、表に示されている複数のプロセスステップで構成されます。

|  |
| --- |
| 注記 システム管理者が SAP Fiori ラウンチパッドでスペースおよびページを有効化している場合、ホームページには、ビジネスロールの一般的なタスクを実行するために必要なアプリのみが含まれます。ホームページに含まれていないその他すべての (検索可能な) アプリは、検索バーを使用して見つけることができます ([2434549](https://me.sap.com/notes/2434549))。ホームページをパーソナライズして非表示のアプリを含める場合は、ユーザプロファイルにナビゲートし、アプリファインダを選択します。 |

| プロセスステップ | ビジネスロール | アプリ/トランザクション | 予想される結果 |
| --- | --- | --- | --- |
| [保全作業区の登録](#unique_10) [ ページ] 6 | SAP_BR_PRODN_ENG_DISC | 作業区登録 (CR01) | 作業区が登録されます。 |

## 手順

このセクションでは、このスコープアイテムに属する各プロセスステップの手順について説明します。これらの手順は、マスタデータ登録のテストでも使用できます。

### 保全作業区の登録

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
| 1. | ログオンする | SAP Fiori ラウンチパッドにSAP_BR_PRODN_ENG_DISCとしてログオンします。 | SAP Fiori ラウンチパッドが表示されます。 |  |
| 2 | SAP Fiori アプリにアクセスする | 作業区登録 (CR01)を開きます。 | 新しいウィンドウが開き、作業区登録: 第一画面が表示されます。 |  |
| 3 | プラントコードを入力する | プラントコードを入力します。 <1010> | 組織登録画面が表示されます。 |  |
| 4 | 作業区 ID を入力する | 作業区 ID: <RES-0100>を入力します。注記 作業区 ID の項目長は 8 未満です。 |  |  |
| 5 | 作業区カテゴリを選択する | 作業区カテゴリ: <0005> プラント保全を選択します。 |  |  |
| 6 | 基本データを選択する | 画面の左上隅の基本データボタンを選択します。 | 作業区登録: 基本データ画面が表示されます。 |  |
| 7 | 作業区テキストを入力し、責任者、用途、および標準値キーを選択する | 基本データタブで、以下のデータを入力します。テキスト: RES-0100など責任者: <YMM> プラント保全機械責任者など用途: <004> 保全タスクリストのみなど標準値キー: <SAP0> 非標準値など |  |  |
| 8 | 管理キーを入力する | 初期値タブを選択し、以下のデータを入力します。管理キー: <YBM1> プラント保全 - 内部など |  |  |
| 9 | 能力および他の計算式を設定する | 能力タブで、以下のデータを入力します。能力カテゴリ: <002> 作業者など他の計算式: <YBPM01> Proj:RqmtsNetwkMaiなど | Enter を選択します。作業区能力登録: ヘッダ画面が表示されます。 |  |
| 10 | 作業区能力を設定する | 作業区能力: ヘッダセクションで、以下のデータを入力します。能力カテゴリテキスト: 整備士能力など能力責任者: <A> 計画グループ Aなど稼働日カレンダ: 自国のカレンダ、<01> ドイツ (標準)など能力基本単位: <H> 時間など開始時刻: <06:00:00>など終了時刻: <14:30:00>など休憩時間: <00:30:00>など能力利用度: <100>など個別能力数: <10>など長期計画: <X> | Enter を選択します。画面が能力概要に戻ります。 |  |
| 11 | 日程計画データを入力する | 日程計画タブで、以下のデータを入力します。能力カテゴリ: <002> 作業者など |  |  |
| 12 | 原価計算データを入力する | 原価計算タブページで、以下のデータを入力します。開始日付: <2015/01/01> など原価センタ: <10101701> プラントおよび保全 (DE)など活動タイプ内部工程: <11> 従業員時間など原価計算の計算式キー: <YBPM01> Proj:RqmtsNetwkMaintなど |  |  |
| 13 | データを保存する | 入力内容を保存します。 | エントリが保存されます。 |  |

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
- related-to :: [[14-maintenance-service-and-projects/create-maintenance-work-center-mds-5mh-461]]
- related-to :: [[14-maintenance-service-and-projects/criar-centro-de-trabalho-de-manutencao-mds-5mh-464]]
- related-to :: [[14-maintenance-service-and-projects/mds-5mh-465]]
- related-to :: [[14-maintenance-service-and-projects/script-de-datos-maestros-crear-puesto-de-trabajo-de-mantenimiento-mds]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/5MH_S4CLD2608_Master_Data_JA_XX.docx` — full document · extracted with `mammoth` · 7,472 chars in the whole document
