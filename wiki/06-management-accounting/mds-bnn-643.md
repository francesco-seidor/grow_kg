---
id: 06-management-accounting/mds-bnn-643
title: 活動タイプおよび活動タイプ階層の登録 - MDS (BNN) (BNN_S4CLD2608_Master_Data_JA_XX)
description: "Japanese SAP master data script BNN for creating activity types and activity type hierarchies, with change log and where-used test steps."
cluster: 06-management-accounting
tags: [kb/management-accounting, topic/activity-types]
aliases: [BNN_S4CLD2608_Master_Data_JA_XX]
keywords: [Activity Types and Activity Type Hierarchies, activity types, activity type hierarchy, controlling area settings, secondary cost elements, change log, where-used analysis, master data scripts, BNN]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/BNN_S4CLD2608_Master_Data_JA_XX.docx]
confidence: high
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-643
topic: 06-management-accounting/activity-types
language: JA
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# 活動タイプおよび活動タイプ階層の登録 - MDS (BNN) (BNN_S4CLD2608_Master_Data_JA_XX)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/BNN_S4CLD2608_Master_Data_JA_XX.docx`, extracted with `mammoth`. Grouped under **Activity Types and Activity Type Hierarchies** in Management Accounting. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

| <!-- image omitted: unnamed --> | マスタデータスクリプトSAP S/4HANA Cloud Public Edition - 02-07-26 |
| --- | --- |
|  | 活動タイプおよび活動タイプ階層の登録 - MDS (BNN) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

目次

[1 目的 2](#_Toc233891973)

[2 前提条件 3](#_Toc233891974)

[2.1 システムアクセス 3](#_Toc233891975)

[2.2 ロール 3](#_Toc233891976)

[2.3 必須の組織ユニット 3](#_Toc233891977)

[2.4 必須マスタデータおよび任意マスタデータ 4](#_Toc233891978)

[2.5 データ登録の主要パラメータ 4](#_Toc233891979)

[2.6 予備ステップ 4](#_Toc233891980)

[2.6.1 ユーザ設定 - 管理領域設定 4](#_Toc233891981)

[3 概要テーブル 6](#_Toc233891982)

[4 テスト手順 7](#_Toc233891983)

[4.1 活動タイプマスタデータの登録 7](#_Toc233891984)

[4.2 活動タイプ階層マスタデータの登録 8](#_Toc233891985)

[4.3 分析 9](#_Toc233891986)

[4.3.1 活動タイプの変更ログ 9](#_Toc233891987)

[4.3.2 使用先一覧 - 活動タイプ 10](#_Toc233891988)

## 目的

活動タイプは、管理領域内において原価センタで生産された活動を示します。活動タイプは、活動単位で記録および評価された活動の計画と配分に使用されます。活動数量は、原価センタで更新される活動価格を使用して評価されます。

活動タイプは、以下の目的で使用されます。

原価センタの数量基準アウトプットの決定。生産原価センタおよび補助部門原価センタの計画活動数量を、ロジスティクスの基準生産計画と照合する必要があります。これにより、必要な計画活動数量と、計画キャパシティが決定されます。

原価センタにおける活動数量の管理。これにより、原価センタの操業度および能力利用率が評価されます。

活動数量のマニュアル計画に加えて、間接活動配分を使用し、活動数量を自動で計画することもできます。

活動タイプ階層は、計画でも有用です。活動タイプに利用できる複数選択ツールがないため、活動を活動タイプ階層に集約し、複数の活動タイプの計画を同時に実行できるようにすることができます。

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

会社の組織構造およびマスタデータは導入時に ERP システムに登録されました。組織構造には、会社の構造が反映されます。マスタデータは会社の重点業務に応じて、活動タイプおよび活動タイプ階層を表します。

| データオブジェクト | データセグメントでの使用 | 必須/任意 | コメント |
| --- | --- | --- | --- |
| 管理領域 | 一般データ | 必須 |  |

### 必須マスタデータおよび任意マスタデータ

デフォルト値

会社の組織構造およびマスタデータは導入時に ERP システムに登録されました。組織構造には、会社の構造が反映されます。マスタデータは会社の業務目的に応じて異なります。

ビジネスプロセスは、この組織別マスタデータで有効になります。次のセクションに例を示します。

活動タイプおよび活動タイプ階層レコードは、他のマスタデータを参照していることがあります。以下の表は、活動タイプデータレコードで使用される任意および必須のマスタデータオブジェクトの概要を示しています。

| マスタデータオブジェクト | データセグメントでの使用 | 必須/任意 | コメント |
| --- | --- | --- | --- |
| 原価要素 | 一般データ | 必須 | 二次原価要素 (原価要素タイプ ‘43’) |
| G/L 勘定 |  | 必須 | 二次原価要素 (原価要素タイプ ‘43’) 用 |

### データ登録の主要パラメータ

このスコープアイテムに、ビジネス条件はありません。

### 予備ステップ

#### ユーザ設定 - 管理領域設定

| ステップ番号 | ステップ名 | 指示 | 予想される結果 | 合格/不合格/コメント |
| --- | --- | --- | --- | --- |
| 1 | SAP Fiori ラウンチパッドにログオンする | SAP Fiori ラウンチパッドに 管理会計担当者 - 間接費 としてログオンします。 | SAP Fiori ラウンチパッドが表示されます。 |  |
| 2 | 設定を選択する | ユーザコンテキストメニューから設定を選択します。 | ユーザ設定ウィンドウが表示されます。 |  |
| 3 | デフォルト値を選択する | ウィンドウでデフォルト値を選択します。 | デフォルト値ウィンドウが表示されます。 |  |
| 4 | データを入力する | CO 領域項目に <CO 領域値> を入力してから保存を選択します。 | 該当するユーザに管理領域、たとえば A000 が設定されます。 |  |

## 概要テーブル

このスコープアイテムは、以下の表に示されている複数のプロセスステップで構成されます。

|  |
| --- |
| 注記 システム管理者が SAP Fiori ラウンチパッドでスペースおよびページを有効化している場合、ホームページには、ビジネスロールの一般的なタスクを実行するために必要なアプリのみが含まれます。ホームページに含まれていないその他すべての (検索可能な) アプリは、検索バーを使用して見つけることができます ([2434549](https://me.sap.com/notes/2434549))。ホームページをパーソナライズして非表示のアプリを含める場合は、ユーザプロファイルにナビゲートし、アプリファインダを選択します。 |

| プロセスステップ | ビジネスロール | トランザクション | 予想される結果 |
| --- | --- | --- | --- |
| [活動タイプマスタデータの登録](#unique_10) [ ページ] 7 | 管理会計担当者 - 間接費 | 活動タイプ管理 (F1605A) | 新規ビジネス要件に従って活動タイプを登録できます。 |
| [活動タイプ階層マスタデータの登録](#unique_11) [ ページ] 8 | 管理会計担当者 - 間接費 | グローバル階層管理 (F2918) | 新規ビジネス要件に従って活動タイプ階層を登録できます。 |
| [活動タイプの変更ログ](#unique_12) [ ページ] 9 | 管理会計担当者 - 間接費 | 変更ログ - 活動タイプ (F3866) |  |
| [使用先一覧 - 活動タイプ](#unique_13) [ ページ] 10 | 管理会計担当者 - 間接費 | 活動タイプ管理 (バージョン 2) (F1605A) |  |

## テスト手順

このセクションでは、このスコープアイテムに属する各プロセスステップの手順について説明します。これらの手順は、マスタデータ登録のテストでも使用できます。

### 活動タイプマスタデータの登録

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
| 1 | ログオンする | SAP Fiori ラウンチパッドに管理会計担当者 - 間接費としてログオンします。 | SAP Fiori ラウンチパッドが表示されます。 |  |
| 2 | SAP Fiori アプリにアクセスする | 活動タイプ管理 (F1605A)を開きます。 | アプリが開きます。 |  |
| 3 | 登録を選択する | 登録を選択します。 |  |  |
| 4 | 活動タイプデータを入力する | 新規活動タイプ: 新規画面の一般データタブで、以下のエントリを入力します。活動タイプを入力する: 内容説明テキスト活動単位: <活動単位>名称: <名称>活動タイプ内容説明: <内容説明を入力する>有効開始: <現在日付>有効終了: <年度末日>原価センタカテゴリ: <原価センタカテゴリ>:活動タイプカテゴリ: <活動タイプカテゴリ>配分原価要素: 94304000など価格フラグ: <価格フラグ> | 一般データセクションとさまざまなタブが表示されます。注記 SAP S/4HANA Cloud Public Editionの SAP 推奨値を以下に示します (その他は表示されていてもサポートされていない場合があるためです)。活動タイプカテゴリ: 1 (マニュアル入力およびマニュアル割当) のみがサポートされます。価格フラグ: 3 (価格はマニュアルで設定します) のみがサポートされます。実績活動タイプカテゴリ: 空白にする必要があります。実績価格区分: デフォルトでは空白にする必要があります。スコープアイテム33Q-実際原価計算を有効化した場合にのみ、5 または7 を使用する必要があります (これら 2 つの値の詳細については、33Qのテストスクリプトのセクションを参照してください)。 |  |
| 5 | データを保存する | 登録を選択します。 | 活動タイプが登録されて保存されます。 |  |

### 活動タイプ階層マスタデータの登録

テスト管理

カスタマプロジェクト: プロジェクト固有部分への入力

|  |  |  |  |
| --- | --- | --- | --- |
| テストケース ID | <X.XX> | テスト実施日: |  |
| テスト実施者名: |  | 期間: |  |
| ビジネスロール: |  | 責任者: | <都道府県/州、サービスプロバイダ、カスタマ/共同サービスプロバイダ、およびカスタマ> |

前提条件

[活動タイプマスタデータの登録](#unique_10) [ ページ] 7の説明に従って、品目の基本データを入力および保存しておきます。

手順

| テストステップ番号 | テストステップ名 | 指示 | 予想される結果 | コメント |
| --- | --- | --- | --- | --- |
| 1 | ログオンする | SAP Fiori ラウンチパッドに管理会計担当者 - 間接費としてログオンします。 | SAP Fiori ラウンチパッドが表示されます。 |  |
| 2 | SAP Fiori アプリにアクセスする | グローバル階層管理 (F2918)を開きます。 | アプリが開きます。 |  |
| 3 | 登録を選択する | 階層一覧セクションで、登録を選択します。 | 新規階層画面が表示されます。 |  |
| 4 | 新規活動タイプ階層を入力する | 新規階層画面で、以下のエントリを入力して登録を選択します。タイプ: 活動タイプ階層階層 ID: <10 文字までの任意の ID>警告 階層 ID およびノード ID の合計長は 14 文字を超えることはできません。管理領域: A000階層テキスト: <任意のテキスト> |  |  |
| 5 | 新規活動タイプ階層を編集する | 階層一覧画面で、詳細アイコン>を選択し、新規登録した活動タイプ階層に対して編集を選択します。新たに登録した活動タイプ階層を選択し、画面の右側にある追加を選択し、簡易入力を選択します。簡易入力画面で、活動タイプを選択し、以下のエントリを入力します。ID: <検索機能を使用して追加する活動タイプを選択>終了したらOKを選択し、保存を選択します。活動タイプ階層画面に戻り、有効化を選択します。 | 新規登録された活動タイプ階層が有効化されます。 |  |

### 分析

#### 活動タイプの変更ログ

テスト管理

カスタマプロジェクト: プロジェクト固有部分への入力

|  |  |  |  |
| --- | --- | --- | --- |
| テストケース ID | <X.XX> | テスト実施日: |  |
| テスト実施者名: |  | 期間: |  |
| ビジネスロール: |  | 責任者: | <都道府県/州、サービスプロバイダ、カスタマ/共同サービスプロバイダ、およびカスタマ> |

目的

このアクティビティでは、活動タイプの変更ログを実行します。

手順

| テストステップ番号 | テストステップ名 | 指示 | 予想される結果 | コメント |
| --- | --- | --- | --- | --- |
| 1 | ログオンする | SAP Fiori ラウンチパッドに管理会計担当者 - 間接費としてログオンします。 | SAP Fiori ラウンチパッドが表示されます。 |  |
| 2 | SAP Fiori アプリにアクセスする | 変更ログ - 活動タイプ (F3866)を開きます。 | 変更ログ - 活動タイプダイアログボックスが表示されます。 |  |
| 3 | 選択基準を入力する | 以下のエントリを入力します。活動タイプ: <任意の活動タイプ> |  |  |
| 4 | 選択する | Goを選択します。 | 変更詳細履歴を示すレポートが表示されます。 |  |

#### 使用先一覧 - 活動タイプ

テスト管理

カスタマプロジェクト: プロジェクト固有部分への入力

|  |  |  |  |
| --- | --- | --- | --- |
| テストケース ID | <X.XX> | テスト実施日: |  |
| テスト実施者名: |  | 期間: |  |
| ビジネスロール: |  | 責任者: | <都道府県/州、サービスプロバイダ、カスタマ/共同サービスプロバイダ、およびカスタマ> |

目的

このアクティビティでは、利益センタ、実績原価配分など、他のマスタデータのどこで活動タイプが使用されたかを確認できます。

手順

| テストステップ番号 | テストステップ名 | 指示 | 予想される結果 | コメント |
| --- | --- | --- | --- | --- |
| 1 | ログオンする | SAP Fiori ラウンチパッドに管理会計担当者 - 間接費としてログオンします。 | SAP Fiori ラウンチパッドが表示されます。 |  |
| 2 | SAP Fiori アプリにアクセスする | 活動タイプ管理 (バージョン 2) (F1605A)を開きます。 | アプリが開きます。 |  |
| 3 | 選択基準を入力する | 以下のエントリを入力します。活動タイプ: <任意の活動タイプ> |  |  |
| 4 | 使用先 | 目的の原価センタを選択し、使用先 - 活動タイプを選択します。 | 現在活動タイプが使用されている場所を示すレポートが表示されます。詳細については、マスタデータオブジェクトタイプを選択し、さらにドリルダウンすることができます。 |  |

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
- related-to :: [[06-management-accounting/criar-tipo-de-atividade-e-hierarquia-de-tipo-de-atividade-mds-bnn-644]]
- related-to :: [[06-management-accounting/leistungsart-und-leistungsartenhierarchie-anlegen-sds-bnn-640]]
- related-to :: [[06-management-accounting/master-data-script-create-activity-type-and-activity-type-hierarchy-bn]]
- related-to :: [[06-management-accounting/mds-bnn-645]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/BNN_S4CLD2608_Master_Data_JA_XX.docx` — full document · extracted with `mammoth` · 10,200 chars in the whole document
