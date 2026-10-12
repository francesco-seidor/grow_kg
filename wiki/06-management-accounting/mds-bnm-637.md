---
id: 06-management-accounting/mds-bnm-637
title: 原価センタおよび原価センタグループの登録 - MDS (BNM) (BNM_S4CLD2608_Master_Data_JA_XX)
description: "Japanese master data script (BNM) for SAP S/4HANA Cloud Public Edition 2608: creating cost centers and cost center groups, and where-used analysis."
cluster: 06-management-accounting
tags: [kb/management-accounting, topic/cost-centers-and-groups]
aliases: [BNM_S4CLD2608_Master_Data_JA_XX]
keywords: [Cost Centers and Cost Center Groups, cost center master data, cost center groups, standard hierarchy, global hierarchy management, where-used analysis, business roles, master data integration, master data scripts, BNM]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/BNM_S4CLD2608_Master_Data_JA_XX.docx]
confidence: high
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-637
topic: 06-management-accounting/cost-centers-and-groups
language: JA
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# 原価センタおよび原価センタグループの登録 - MDS (BNM) (BNM_S4CLD2608_Master_Data_JA_XX)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/BNM_S4CLD2608_Master_Data_JA_XX.docx`, extracted with `mammoth`. Grouped under **Cost Centers and Cost Center Groups** in Management Accounting. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

| <!-- image omitted: unnamed --> | マスタデータスクリプトSAP S/4HANA Cloud Public Edition - 02-07-26 |
| --- | --- |
|  | 原価センタおよび原価センタグループの登録 - MDS (BNM) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

目次

[1 目的 2](#_Toc233891984)

[2 前提条件 3](#_Toc233891985)

[2.1 システムアクセス 3](#_Toc233891986)

[2.2 ロール 3](#_Toc233891987)

[2.3 必須の組織ユニット 3](#_Toc233891988)

[2.4 必須マスタデータおよび任意マスタデータ 4](#_Toc233891989)

[2.5 データ登録の主要パラメータ 4](#_Toc233891990)

[3 概要テーブル 5](#_Toc233891991)

[4 テスト手順 6](#_Toc233891992)

[4.1 原価センタマスタデータの登録 6](#_Toc233891993)

[4.2 原価センタグループマスタデータの登録 8](#_Toc233891994)

[4.3 分析 11](#_Toc233891995)

[4.3.1 使用先一覧 - 原価センタ実績 11](#_Toc233891996)

[5 付録 13](#_Toc233891997)

[5.1 SAP S/4HANA Cloud Public Editionから SAP Master Data Integration への原価センタ複製 (オプション) 13](#_Toc233891998)

## 目的

原価センタは、財務原価を割り当てることができる組織ユニットの責任領域です。組織を原価センタに分割することにより、いくつかの目標を達成することができます。

原価を原価センタに割り当てることにより、組織内での原価の発生場所を決定することができます。

原価を原価センタレベルで計画する場合、原価の発生ポイントで原価を効率的にチェックすることができます。

間接費を個別の製品、サービスまたは市場セグメントに正確に割り当てるには、製品またはサービスの生産に直接関与した原価センタに原価を配分する必要もあります。これらの原価センタから、異なる方法を使用し、活動および原価を関連する製品、サービスおよび市場セグメントに割り当てることができます。

これにより、半製品および最終製品を製品原価管理 (CO-PC) で評価し、貢献利益を収益性分析 (CO-PA) で計算することができるようになります。

原価センタグループは、標準階層として知られる原価センタの階層構造を示します。登録された各原価センタを、標準階層のグループに割り当てる必要があります。これにより、標準階層には管理会計グループの原価センタがすべて含まれることになります。標準階層の分析時には、SAP システムにすべての原価センタが自動的に含まれます。

原価センタは、任意の数の代替グループに割り当てることができることに注意してください。ただし、標準階層の更新時には代替グループを登録できません。

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
| 管理会計担当者 - 間接費 | SAP_BR_OVERHEAD_ACCOUNTANT | 間接費会計 | SAP_BR_OVERHEAD_ACCOUNTANT |  |

### 必須の組織ユニット

会社の組織構造およびマスタデータは導入時に ERP システムに登録されました。組織構造は会社の実際の組織構造が反映されています。マスタデータは、会社の重点業務に応じて原価センタおよび原価センタグループを表します。

| データオブジェクト | データセグメントでの使用 | 必須/任意 | コメント |
| --- | --- | --- | --- |
| 管理領域 | 一般データ | 必須 |  |
| 会社コード | 組織ユニット | 必須 |  |

### 必須マスタデータおよび任意マスタデータ

原価センタと原価センタグループのマスタデータレコードは、他のマスタデータを参照していることがあります。以下の表は、原価センタデータレコードで使用される任意および必須のマスタデータオブジェクトの概要を示しています。

| マスタデータオブジェクト | データセグメントでの使用 | 必須/任意 | コメント |
| --- | --- | --- | --- |
| 階層領域 | 組織ユニット | 必須 |  |
| 事業領域 | 組織ユニット | 任意 |  |
| 機能領域 | 組織ユニット | 任意 |  |
| 利益センタ | 組織ユニット | 必須 |  |

### データ登録の主要パラメータ

このスコープアイテムに、ビジネス条件はありません。

## 概要テーブル

このスコープアイテムは、以下の表に示されている複数のプロセスステップで構成されます。

|  |
| --- |
| 注記 システム管理者が SAP Fiori ラウンチパッドでスペースおよびページを有効化している場合、ホームページには、ビジネスロールの一般的なタスクを実行するために必要なアプリのみが含まれます。ホームページに含まれていないその他すべての (検索可能な) アプリは、検索バーを使用して見つけることができます ([2434549](https://me.sap.com/notes/2434549))。ホームページをパーソナライズして非表示のアプリを含める場合は、ユーザプロファイルにナビゲートし、アプリファインダを選択します。 |

| プロセスステップ | ビジネスロール | トランザクション/アプリ | 予想される結果 |
| --- | --- | --- | --- |
| [原価センタマスタデータの登録](#unique_9) [ ページ] 6 | 管理会計担当者 - 間接費 | 原価センタ管理 - 旧バージョン(F1443A) | 新規ビジネス要件に従って原価センタを登録できます。 |
| [原価センタグループマスタデータの登録](#unique_10) [ ページ] 8 | 管理会計担当者 - 間接費 | グローバル階層管理 (F2918)または原価センタグループ管理(F1024) | 新規ビジネス要件に従って原価センタグループを登録できます。 |
| [使用先一覧 - 原価センタ実績](#unique_11) [ ページ] 11 | 管理会計担当者 - 間接費 | 原価センタ管理 - 旧バージョン(F1443A) |  |

## テスト手順

このセクションでは、このスコープアイテムに属する各プロセスステップの手順について説明します。これらの手順は、マスタデータ登録のテストでも使用できます。

### 原価センタマスタデータの登録

テスト管理

カスタマプロジェクト: プロジェクト固有部分への入力

|  |  |  |  |
| --- | --- | --- | --- |
| テストケース ID | <X.XX> | テスト実施日: |  |
| テスト実施者名: |  | 期間: |  |
| ビジネスロール: |  | 責任者: | <都道府県/州、サービスプロバイダ、カスタマ/共同サービスプロバイダ、およびカスタマ> |

|  |
| --- |
| 注記 標準階層ノード 1~2502 エディション以降、新規得意先のインストールでは、値 1~ のグローバル階層機能を使用して標準階層が提供されます。以前の得意先は、セットベースの標準階層値 0001 を引き続き使用することができます。本稼動システムで最初の原価センタを登録する場合は、標準階層ノード項目の検索ドロップダウンリストで値1~を選択する必要があります。これにより、標準階層内で最上位ノード 1~ が構築されます。システムに最初の原価センタが登録されると、標準階層ノード 1~ も自動的に登録されます。2502 エディション以降、SAP S/4HANA Cloud Public Edition Public Edition のデフォルトコンテンツは常に標準階層 1~ で出荷され、最上位レベルとして使用される必要があります。 |

手順

| テストステップ番号 | テストステップ名 | 指示 | 予想される結果 | コメント |
| --- | --- | --- | --- | --- |
| 1 | ログオンする | SAP Fiori ラウンチパッドに管理会計担当者 - 間接費としてログオンします。 | SAP Fiori ラウンチパッドが表示されます。 |  |
| 2 | SAP Fiori アプリにアクセスする | 原価センタ管理 - 旧バージョン(F1443A)を開きます。 | アプリが開きます。 |  |
| 3 | 新規原価センタを登録する | 登録を選択して、新規原価センタを登録します。 |  |  |
| 4 | 新規原価センタを入力する | 一般情報タブで、以下のように入力します。原価センタ: <テキスト>名称: <テキスト>テキスト: <テキスト>責任者: <責任者>有効開始日付: <2017/01/01>有効終了日付: <9999/12/31>原価センタカテゴリ: <原価センタカテゴリ>:あるいは、有効な日付のデフォルト値を変更して、既存の原価センタマスタデータからの参照を選択できます。 | 新しいセクションが開いて、一般情報が表示されます。 |  |
| 5 | 原価センタ組織データを入力する | 原価センタ画面の組織ユニットセクションで、以下のエントリを入力します。標準階層ノード: <1~>会社コード: <会社コード>機能領域: <機能領域>利益センタ: <利益センタ>PSM のみ:注記 公共セクター管理 (PSM)がインストールされている場合、PSM 会社コードの選択後に、これらの項目が入力可能になります。ファンド: <ファンド>ファンド固定割当: <はい/いいえ>補助金: <補助金>補助金固定割当: <はい/いいえ>機能領域固定割当: <はい/いいえ>注記 機能領域、ファンド、および補助金の固定割当チェックボックスは、各マスタデータを入力した後にのみ表示されます。予算持越原価センタ: <原価センタ>予算利用可能管理プロファイル: <プロファイル>予算の利用可能管理有効: <はい/いいえ> | 選択をスクロールすると、組織データが表示されます。 |  |
| 6 | 登録 | 登録を選択します。 | 原価センタが登録されます。 |  |

### 原価センタグループマスタデータの登録

テスト管理

カスタマプロジェクト: プロジェクト固有部分への入力

|  |  |  |  |
| --- | --- | --- | --- |
| テストケース ID | <X.XX> | テスト実施日: |  |
| テスト実施者名: |  | 期間: |  |
| ビジネスロール: |  | 責任者: | <都道府県/州、サービスプロバイダ、カスタマ/共同サービスプロバイダ、およびカスタマ> |

前提条件

この章では、品目の基本データが、次の章の説明に従ってすでに入力されている必要があります。[原価センタマスタデータの登録](#unique_9) [ ページ] 6。前の章でマスタデータエントリを保存したら、この手順を開始してください。

|  |
| --- |
| 注記 グローバル階層管理 (F2918)または原価センタグループ管理(F1024)のいずれかを代替階層の登録時に使用できますが、1 つの方法 (グローバル階層グループまたはセットベースグループ) のみを選択する必要があります。両方の方法について以下のステップで説明します。既存の得意先は、次のパスから BPC エキスパートロールを使用して、完全に移行し、移行ステータスを完了としてマークするまで、セットベースグループ関連アプリ原価センタグループ管理(F1024)を引き続き使用することができます。ビジネスプロセス設定 > 会計管理 > 一般設定: グローバル階層へのセットベースグループの移行 (F6228)。SAP 提供の原価センタグループデモマスタデータも、セットベースグループを使用して登録され、変換することもできます。原価センタグループのグローバル階層への変換の詳細については、次を参照してください。[https://help.sap.com/docs/SAP_S4HANA_CLOUD/c56f622a2edf491b9f1b596b55587009/635e615de9a848eb9129edb0da88cbcc.html?state=DRAFT](https://help.sap.com/docs/SAP_S4HANA_CLOUD/c56f622a2edf491b9f1b596b55587009/635e615de9a848eb9129edb0da88cbcc.html?state=DRAFT)。 |

手順: オプション 1 - グローバル階層グループ

| テストステップ番号 | テストステップ名 | 指示 | 予想される結果 | コメント |
| --- | --- | --- | --- | --- |
| 1 | ログオン | SAP Fiori ラウンチパッドに管理会計担当者 - 間接費としてログオンします。 | SAP Fiori ラウンチパッドが表示されます。 |  |
| 2 | SAP Fiori アプリにアクセスする | グローバル階層管理 (F2918)を開きます。 | アプリが開きます。 |  |
| 3 | 登録を選択する | 階層一覧セクションで、登録を選択します。 | 新規階層画面が表示されます。 |  |
| 4 | 新規原価センタ階層を入力する | 新規階層画面で、以下のエントリを入力して登録を選択します。タイプ: 原価センタ階層:階層 ID: <10 文字までの任意の ID>警告 階層 ID およびノード ID の合計長は 14 文字を超えることはできません。管理領域: A000階層テキスト: <任意のテキスト>有効開始: <現在の日付> |  |  |
| 5 | 新規原価階層を編集する | 階層一覧画面で、詳細アイコン>を選択し、新規登録した原価センタ階層に対して編集を選択します。新たに登録した原価センタ階層を選択し、画面の右側にある追加を選択し、簡易入力を選択します。簡易入力画面で、原価センタを選択し、以下のエントリを入力します。ID: <検索機能を使用して追加する原価センタを選択>終了したらOKを選択し、保存を選択します。原価センタ階層画面に戻り、有効化を選択します。 | 新規登録された原価センタ階層が有効化されます。 |  |

手順: オプション 2 - セットベースグループ

| テストステップ番号 | テストステップ名 | 指示 | 予想される結果 | コメント |
| --- | --- | --- | --- | --- |
| 1 | ログオン | SAP Fiori ラウンチパッドに管理会計担当者 - 間接費としてログオンします。 | SAP Fiori ラウンチパッドが表示されます。 |  |
| 2 | SAP Fiori アプリにアクセスする | 原価センタグループ管理(F1024)を開きます。 | アプリが開きます。 |  |
| 3 | 新規原価センタグループを登録する | 結果一覧: 原価センタグループセクションで、新規を選択します。 |  |  |
| 4 | 新規原価センタグループを入力する | 原価センタグループ: 新規画面で、以下のエントリを入力します。管理領域: <A000>原価センタグループ: <原価センタグループ>続行を選択し、以下のエントリを入力します。名称: <名称>保存を選択します。あるいは、既存の原価センタグループからの参照を選択できます。 | 原価センタグループ: 新規画面が表示されます。 |  |
| 5 | 原価センタ組織データを入力する | 原価センタグループ: 新規画面で、以下のエントリを入力します。最上位レベルでは、新規を選択して新規マスタデータを登録することができます。新規子グループ: <原価センタグループ>下位レベルでは、新規を選択して追加することができます。新規子グループ: <原価センタグループ>新規兄弟グループ: <原価センタグループ>最上位レベルでは、追加を選択して既存のマスタデータを追加することができます。子グループ追加: <原価センタグループ>原価センタ追加: <原価センタ>原価センタグループ追加: <原価センタ>下位レベルでは、新規を選択して追加することができます。新規子グループ: <原価センタグループ>新規兄弟グループ: <原価センタグループ>原価センタ追加: <原価センタ>原価センタグループ追加: <原価センタ> | 新しいマスタデータが原価センタグループ: 新規画面が表示されます。 |  |
| 6 | データを保存する | 保存を選択します。 | 原価センタグループが登録されて保存されます。 |  |

### 分析

#### 使用先一覧 - 原価センタ実績

テスト管理

カスタマプロジェクト: プロジェクト固有部分への入力

|  |  |  |  |
| --- | --- | --- | --- |
| テストケース ID | <X.XX> | テスト実施日: |  |
| テスト実施者名: |  | 期間: |  |
| ビジネスロール: |  | 責任者: | <都道府県/州、サービスプロバイダ、カスタマ/共同サービスプロバイダ、およびカスタマ> |

目的

このアクティビティでは、活動タイプ、利益センタ、実績原価配分など、他のマスタデータのどこで原価センタが使用されたかを確認できます。

手順

| テストステップ番号 | テストステップ名 | 指示 | 予想される結果 | 合格/不合格/コメント |
| --- | --- | --- | --- | --- |
| 1. | ログオンする | SAP Fiori ラウンチパッドに管理会計担当者 - 間接費としてログオンします。 |  |  |
| 2 | SAP Fiori アプリにアクセスする | 原価センタ管理 - 新規バージョン(F1443B)を開きます。 | 原価センタ管理画面が表示されます。 |  |
| 3 | 選択基準を入力する | 以下のエントリを入力してGoを選択します。原価センタ: <原価センタ> |  |  |
| 4 | 使用先 | 目的の原価センタを選択し、使用先を選択します。ドロップダウンリストからオプションを 1 つ選択します。たとえば、すべてのオブジェクトなどです。 | 現在原価センタが使用されている場所を表示するレポートが表示されます。詳細については、マスタデータオブジェクトタイプを選択して確認してください。 |  |

|  |
| --- |
| 注記 使用先一覧 - 原価センタ (F3549) アプリは、現在原価センタが使用されている場所を決定するためにも使用することができます。 |

## 付録

### SAP S/4HANA Cloud Public Editionから SAP Master Data Integration への原価センタ複製 (オプション)

SAP Master Data Integration を介した他のクラウドアプリケーション (SAP SuccessFactorsなど) へのSAP S/4HANA Cloud Public Edition原価センタマスタデータの複製については、このリンク[https://help.sap.com/viewer/6b39bd1d0e5e4099a5b65d835c29c696/LATEST/en-US/decbb94c95fa421ead9101e4c43683f7.html](https://help.sap.com/viewer/6b39bd1d0e5e4099a5b65d835c29c696/LATEST/en-US/decbb94c95fa421ead9101e4c43683f7.html)で説明されています。

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
- related-to :: [[06-management-accounting/create-cost-center-and-cost-center-group-mds-bnm-635]]
- related-to :: [[06-management-accounting/mds-bnm-639]]
- related-to :: [[06-management-accounting/script-de-dados-mestre-criar-centro-de-custo-e-grupo-de-centros-de-cus]]
- related-to :: [[06-management-accounting/script-de-datos-maestros-crear-centro-de-coste-y-grupo-de-centros-de-c]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/BNM_S4CLD2608_Master_Data_JA_XX.docx` — full document · extracted with `mammoth` · 12,017 chars in the whole document
