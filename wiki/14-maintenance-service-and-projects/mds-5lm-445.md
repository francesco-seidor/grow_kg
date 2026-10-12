---
id: 14-maintenance-service-and-projects/mds-5lm-445
title: 機能場所の登録 - MDS (5LM) (5LM_S4CLD2608_Master_Data_JA_XX)
description: "Japanese master data script (5LM) for creating a functional location structure (one parent, two children) for plant maintenance in SAP S/4HANA Cloud Public Edition."
cluster: 14-maintenance-service-and-projects
tags: [kb/maintenance-service-and-projects, topic/functional-locations]
aliases: [5LM_S4CLD2608_Master_Data_JA_XX]
keywords: [Functional Locations, plant maintenance, structure indicator, technical object category, maintenance planner role, cost centers, maintenance work centers, 5LM]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/5LM_S4CLD2608_Master_Data_JA_XX.docx]
confidence: high
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-445
topic: 14-maintenance-service-and-projects/functional-locations
language: JA
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# 機能場所の登録 - MDS (5LM) (5LM_S4CLD2608_Master_Data_JA_XX)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/5LM_S4CLD2608_Master_Data_JA_XX.docx`, extracted with `mammoth`. Grouped under **Functional Locations** in Maintenance, Service and Projects. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

| <!-- image omitted: unnamed --> | マスタデータスクリプトSAP S/4HANA Cloud Public Edition - 02-07-26 |
| --- | --- |
|  | 機能場所の登録 - MDS (5LM) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

目次

[1 目的 2](#_Toc233891722)

[2 前提条件 3](#_Toc233891723)

[2.1 システムアクセス 3](#_Toc233891724)

[2.2 ロール 3](#_Toc233891725)

[2.3 必須の組織ユニット 3](#_Toc233891726)

[2.4 必須マスタデータおよび任意マスタデータ 4](#_Toc233891727)

[2.5 データ登録の主要パラメータ 4](#_Toc233891728)

[2.5.1 構成区分 4](#_Toc233891729)

[2.5.2 技術対象カテゴリ 5](#_Toc233891730)

[3 概要テーブル 6](#_Toc233891731)

[4 手順 7](#_Toc233891732)

[4.1 機能場所の登録 7](#_Toc233891733)

## 目的

この文書では、S/4HANA システムで機能場所マスタデータレコードを登録する詳細な手順について説明します。この文書には、標準的なシステム環境で処理するマスタデータに関連するデータセグメントが含まれています。また、この文書には、入力値を必要とするデータセグメントおよび項目に関する情報も記載されています。

SAP Best Practices による S/4 HANA コンテンツ配信の範囲に関連しない項目については、UI に表示される場合もありますが、この文書では説明されていません。この説明に従って登録される機能場所は、保全処理で使用できます。

## 前提条件

このセクションでは、機能場所の登録に必要なすべての前提条件の概要を示します。

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
| 保全計画者 | SAP_BR_MD_SPECIALIST_EAM | 保全計画者 | SAP_EAM_SPT_MD_SPECIALIST_PC |

### 必須の組織ユニット

マスタデータの一部のセグメントは、会社の組織ユニットによって異なります。一般 (共通) データは組織ユニットまたは会社コードに依存しません。以下の表は、さまざまなデータセグメントおよび関連する組織ユニットの概要を示しています。

| データセグメント | 依存対象 | 項目例 | コメント | 使用される組織ユニット |
| --- | --- | --- | --- | --- |
| すべてのデータ | プラント |  | 機能場所のすべてのデータはプラントによって異なります。 | プラント:__________ |

### 必須マスタデータおよび任意マスタデータ

機能場所データレコードは、他のマスタデータを参照する場合があります。以下の表は、機能場所で使用される任意および必須のマスタデータオブジェクトの概要を示しています。

| マスタデータオブジェクト | データセグメントでの使用 | 必須/任意 | コメント |
| --- | --- | --- | --- |
| 保全作業区 | 機能場所ユーザインタフェース (UI) の組織データタブの責任セクションで、保全作業区のエントリを確認できます。 | 任意 | 保全作業区は、段取、機械、作業などの一部の値を決定するためのパラメータとして使用されます。 |
| 原価センタ | 機能場所ユーザインタフェース (UI) の組織データタブの責任セクションで、原価センタのエントリを確認できます。 | 任意 | 原価センタは、原価計算のパラメータとして使用されます。 |

### データ登録の主要パラメータ

このセクションでは、マスタレコードの動作に影響し、機能場所の登録に常に必要となる基本パラメータの一部について説明します。

#### 構成区分

機能場所の構成区分は、機能場所ラベルの構造を決定します。これにより、以下の要素が確立されます。

- 技術システムの階層レベル数
- レベルのキー長
- 区切記号 (ハイフン)

表 2:

| 構成区分 | 説明 |
| --- | --- |
| YBPM | ベストプラクティスの構成区分 |

#### 技術対象カテゴリ

これは、機能場所カテゴリを示すキーです。

表 3:

| 技術対象カテゴリ | テキスト |
| --- | --- |
| M | 技術システム - 標準 |

## 概要テーブル

|  |
| --- |
| 注記 システム管理者が SAP Fiori ラウンチパッドでスペースおよびページを有効化している場合、ホームページには、ビジネスロールの一般的なタスクを実行するために必要なアプリのみが含まれます。ホームページに含まれていないその他すべての (検索可能な) アプリは、検索バーを使用して見つけることができます ([2434549](https://me.sap.com/notes/2434549))。ホームページをパーソナライズして非表示のアプリを含める場合は、ユーザプロファイルにナビゲートし、アプリファインダを選択します。 |

| プロセスステップ | ビジネスロール | アプリ/トランザクション | 予想される結果 |
| --- | --- | --- | --- |
| [機能場所の登録](#unique_11) [ ページ] 7 | SAP_BR_MD_SPECIALIST_EAM | 技術対象登録(EAMS_WDA_TECHOBJ_OIF (EAMS_WDA_TECHOBJ_OIF_CFG_V2)) | 機能場所が登録されます。 |

## 手順

### 機能場所の登録

テスト管理

カスタマプロジェクト: プロジェクト固有部分への入力

|  |  |  |  |
| --- | --- | --- | --- |
| テストケース ID | <X.XX> | テスト実施日: |  |
| テスト実施者名: |  | 期間: |  |
| ビジネスロール: |  | 責任者: | <都道府県/州、サービスプロバイダ、カスタマ/共同サービスプロバイダ、およびカスタマ> |

目的

このテストステップでは、1 つの最上位の機能場所と 2 つの下位の機能場所で構成される機能場所構造を更新します。

手順

| テストステップ番号 | テストステップ名 | 指示 | 予想される結果 | 合格/不合格/コメント |
| --- | --- | --- | --- | --- |
| 1. | ログオンする | SAP Fiori ラウンチパッドにマスタデータスペシャリストSAP_BR_MD_SPECIALIST_EAMとしてログオンします。 | SAP Fiori ラウンチパッドが表示されます。 |  |
| 2 | SAP Fiori アプリにアクセスする | 技術対象登録(EAMS_WDA_TECHOBJ_OIF (EAMS_WDA_TECHOBJ_OIF_CFG_V2))を開きます。 | 新しいウィンドウが開き、技術対象登録: 第一画面が表示されます。 |  |
| 3 | 機能場所を登録する | 技術対象登録画面で、技術対象タイプ: 機能場所を選択します。次の画面で、以下のように入力します。技術対象タイプ: 機能場所構成区分: YBPM (ベストプラクティスの構成区分)技術対象: <1711 など>技術対象カテゴリ: M (技術システム - 標準)続行を選択します。 |  |  |
| 4 | 一般データを更新する | 技術対象登録: 1711画面の一般データセクションで、以下を入力します。テキスト: <空気圧縮機 1 プラントなど>オプションで、その他の一般データを更新してから、場所データセクションにナビゲートします。 | 技術対象登録: 一般データ画面が表示されます。 |  |
| 5 | 場所データを更新する | 場所データセクションで、以下を入力します。保全プラント: <1710 (米国の場合) など>注記 同じ構造に属する技術対象にはすべて同じプラントが割り当てられている必要があります。あるいは、すべての技術対象でプラント情報を空白のままにしておくこともできます。オプションで、住所情報などのその他の詳細を更新します。 | 技術対象登録: 場所データ画面が表示されます。 |  |
| 6 | 組織データを更新する | 組織データセクションで、以下を入力します。計画プラント: <1710 (米国の場合) など>保全作業区: <RES-0100 (米国の場合) など>原価センタ: <17101701 (米国の場合) など>オプションで、組織データセクションにある取引先情報などの追加情報を更新することもできます。 | 技術対象登録: 組織データ画面が表示されます。 |  |
| 7 | 機能場所を保存する | オプションで、他のセクションの追加情報を更新することもできます。エントリチェックボタンをクリックします。保存を選択します。そうすると、ホーム画面に戻ります。 | 機能場所が登録されます。 |  |
| 8 | 下位の機能場所を登録する | 機能場所構造を更新するには、上記ステップを実行して以下の機能場所を更新します。技術対象: 1711-001テキスト: <圧縮機 # 1 など>場所データセクションで、以下を入力します。場所: <YB_1701 など>プラントセクション: YOH組織データセクションで、以下のエントリを更新します。計画グループ: <920 (米国の場合) など>計画プラント: <1710 (米国の場合) など>保全作業区: <RES-0100 (米国の場合) など>作業区プラント: <1710 (米国の場合) など>カタログプロファイル: <YB-PM0003 (米国の場合) など>オプションで、他のセクションの追加情報を更新することもできます。エントリチェックボタンを選択します。保存を選択します。以下を入力します。技術対象: 1711-002テキスト: <圧縮機 # 2 など>場所データセクションで、以下を入力します。場所: <YB_1702 など>プラントセクション: <YOH>組織データセクションで、以下のエントリを更新します。計画グループ: <920 (米国の場合) など>計画プラント: <1710 (米国の場合) など>保全作業区: <RES-0100 (米国の場合) など>作業区プラント: <1710 (米国の場合) など>カタログプロファイル: <YB-PM0003 (米国の場合) など>オプションで、他のセクションの追加情報を更新することもできます。エントリチェックボタンをクリックします。保存を選択します。 | 下位の機能場所が登録されます。 |  |
| 9 | 設備ビューアで技術対象をレビューする | ホームページで、技術対象照会タイルを選択します。技術対象照会画面で、1711 などの関連する技術対象を更新してから、続行を選択します。技術対象ごとに機能場所構造および詳細をレビューするには、次のことも可能: 設備ビューアでの技術対象照会を選択します。 |  |  |

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
- related-to :: [[14-maintenance-service-and-projects/creacion-de-ubicacion-tecnica-mds-5lm-es-444]]
- related-to :: [[14-maintenance-service-and-projects/create-functional-location-mds-5lm-443]]
- related-to :: [[14-maintenance-service-and-projects/mds-5lm-447]]
- related-to :: [[14-maintenance-service-and-projects/script-de-dados-mestre-criar-local-de-instalacao-mds-5lm-446]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/5LM_S4CLD2608_Master_Data_JA_XX.docx` — full document · extracted with `mammoth` · 8,142 chars in the whole document
