---
id: 12-production-and-manufacturing/mds-bld-571
title: 製造バージョンの登録 - MDS (BLD) (BLD_S4CLD2608_Master_Data_JA_XX)
description: Japanese SAP S/4HANA Cloud Public Edition master data script (BLD) for creating and editing production versions via F6400 or F2568.
cluster: 12-production-and-manufacturing
tags: [kb/production-and-manufacturing, topic/production-versions]
aliases: [BLD_S4CLD2608_Master_Data_JA_XX]
keywords: [Production Versions, production version editing, production version proposals, bill of materials, task lists, business roles, master data scripts, BLD]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/BLD_S4CLD2608_Master_Data_JA_XX.docx]
confidence: high
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-571
topic: 12-production-and-manufacturing/production-versions
language: JA
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# 製造バージョンの登録 - MDS (BLD) (BLD_S4CLD2608_Master_Data_JA_XX)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/BLD_S4CLD2608_Master_Data_JA_XX.docx`, extracted with `mammoth`. Grouped under **Production Versions** in Production and Manufacturing. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

| <!-- image omitted: unnamed --> | マスタデータスクリプトSAP S/4HANA Cloud Public Edition - 02-07-26 |
| --- | --- |
|  | 製造バージョンの登録 - MDS (BLD) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

目次

[1 目的 2](#_Toc233891889)

[2 前提条件 3](#_Toc233891890)

[2.1 システムアクセス 3](#_Toc233891891)

[2.2 ロール 3](#_Toc233891892)

[2.3 必須の組織ユニット 3](#_Toc233891893)

[2.4 必須マスタデータおよび任意マスタデータ 4](#_Toc233891894)

[3 概要テーブル 5](#_Toc233891895)

[4 テスト手順 6](#_Toc233891896)

[4.1 製品バージョン登録 6](#_Toc233891897)

[4.2 製造バージョンの編集 (オプション) 9](#_Toc233891898)

## 目的

製造バージョンの登録

この文書では、SAP S/4HANA Cloud Public Editionシステムに製造バージョンを登録する方法について説明します。説明には、SAP S/4HANA Cloud Public Editionアプライアンスに関連するデータセグメントも含まれます。SAP S/4HANA Cloud Public Editionの範囲に関連しない項目については、この文書では説明していません。

この説明に従って登録される製造バージョンを製造プロセスの処理で使用できます。

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
| 生産エンジニア - プロセス生産 | SAP_BR_PRODN_ENG_PROC | 生産エンジニアリング - プロセス生産 | SAP_BR_PRODN_ENG_PROC |  |

### 必須の組織ユニット

| データセグメント | 依存対象 | 項目例 | コメント | 使用される組織ユニット |
| --- | --- | --- | --- | --- |
| すべてのデータ | プラント |  | 製造バージョンのすべてのデータはプラントによって異なります。 | プラント:__________ |

### 必須マスタデータおよび任意マスタデータ

製造バージョンデータレコードは他のマスタデータを参照することがあります。以下の表は、製造バージョンで使用される任意および必須のマスタデータオブジェクトの概要を示しています。

| マスタデータオブジェクト | データセグメントでの使用 | 必須/任意 | コメント |
| --- | --- | --- | --- |
| 品目 | 製造バージョンは品目およびプラントごとに登録されます。 | 必須 | 製造バージョン: 一括処理画面で、品目を入力します。品目登録の場合は、マスタデータスクリプト"原材料" タイプの製品マスタの登録 - MDS - BNR、"半製品" タイプの製品マスタの登録 - MDS - BNS、または "最終製品" タイプの製品マスタの登録 - MDS - BNTのステップに従うことができます。 |
| 部品表/配合表 | 品目の BOM マスタデータは製造バージョンで割り当てられます。 | 必須 | 製造バージョン: 一括処理画面で、代替 BOMおよびBOM 用途を入力します。BOM 登録の場合は、マスタデータスクリプト製造および販売向けの品目 BOM の登録 - MDS - BNKのステップに従うことができます。 |
| タスクリスト | 品目のタスクリストは製造バージョンで割り当てられます。 | 必須 | 製造バージョン: 一括処理画面で、タスクリストタイプ、グループおよびグループカウンタを入力します。タスクリストの登録については、マスタデータスクリプト作業手順の登録 - MDS - BNL、またはマスタレシピの登録 - MDS - 3X9のステップに従うことができます。 |

## 概要テーブル

このスコープアイテムは、以下の表に示されている複数のプロセスステップで構成されます。

|  |
| --- |
| 注記 システム管理者が SAP Fiori ラウンチパッドでスペースおよびページを有効化している場合、ホームページには、ビジネスロールの一般的なタスクを実行するために必要なアプリのみが含まれます。ホームページに含まれていないその他すべての (検索可能な) アプリは、検索バーを使用して見つけることができます ([2434549](https://me.sap.com/notes/2434549))。ホームページをパーソナライズして非表示のアプリを含める場合は、ユーザプロファイルにナビゲートし、アプリファインダを選択します。 |

| プロセスステップ | ビジネスロール | トランザクション | 予想される結果 |
| --- | --- | --- | --- |
| [製品バージョン登録](#unique_8) [ ページ] 6 | 生産エンジニア - ディスクリート製造 または 生産エンジニア - プロセス生産 | 製造バージョン処理(F6400) または 製造バージョン管理(F2568) |  |
| [製造バージョンの編集 (オプション)](#unique_9) [ ページ] 9 | 生産エンジニア - ディスクリート製造 または 生産エンジニア - プロセス生産 | 製造バージョン処理(F6400) |  |

## テスト手順

このセクションでは、このスコープアイテムに属する各プロセスステップのテスト手順について説明します。

### 製品バージョン登録

テスト管理

カスタマプロジェクト: プロジェクト固有部分への入力

|  |  |  |  |
| --- | --- | --- | --- |
| テストケース ID | <X.XX> | テスト実施日: |  |
| テスト実施者名: |  | 期間: |  |
| ビジネスロール: |  | 責任者: | <都道府県/州、サービスプロバイダ、カスタマ/共同サービスプロバイダ、およびカスタマ> |

手順

このステップは、さまざまな SAP Fiori アプリで実行することができます。3 つのオプションを使用することができます。いずれかを選択することができます。

オプション 1

| テストステップ番号 | テストステップ名 | 指示 | 予想される結果 | コメント |
| --- | --- | --- | --- | --- |
| 1 | ログオンする | SAP Fiori ラウンチパッドに生産エンジニア - ディスクリート製造または生産エンジニア - プロセス生産としてログオンします。 | 開始ビューが表示されます。 |  |
| 2 | SAP Fiori アプリにアクセスする | 製造バージョン処理(F6400)を開きます。 | アプリが開きます。 |  |
| 3 | 選択項目を入力する | 以下のエントリを入力してGoを選択します。品目: <品目コードを入力します>プラント: <プラントを入力> |  |  |
| 4 | 製造バージョン提案をチェックする | 製造バージョン提案タブでは、対応する BOM/タスクリストの組合せがまだ存在しない場合に、新規製造バージョンを登録するための提案を見つけることができます。提案を選択して提案の詳細を確認し、可能な変更を行うことができます。 | 注記 製造バージョン提案のルールを設定するために、ステップ (ID: 105965) が導入されました。 |  |
| 5 | 提案を受け入る | 製造バージョン提案を選択し、提案の受入を選択します。 |  |  |
| 6 | 確認する | 確認ダイアログボックスで、OKを選択します。 | 提案されたパラメータに基づいて、新規製造バージョンが登録されます。これは、既存の製造バージョンタブにあります。 |  |

オプション 2

| テストステップ番号 | テストステップ名 | 指示 | 予想される結果 | コメント |
| --- | --- | --- | --- | --- |
| 1 | ログオンする | SAP Fiori ラウンチパッドに生産エンジニア - ディスクリート製造または生産エンジニア - プロセス生産としてログオンします。 | 開始ビューが表示されます。 |  |
| 2 | SAP Fiori アプリにアクセスする | 製造バージョン処理(F6400)を開きます。 | アプリが開きます。 |  |
| 3 | 選択項目を入力する | 以下のエントリを入力してGoを選択します。品目: <品目コードを入力します>プラント: <プラントを入力> |  |  |
| 4 | タブを選択する | 既存の製造バージョンタブを選択します。 |  |  |
| 5 | 登録 | 登録を選択します。製造バージョン登録ダイアログボックスで、以下のエントリを入力し、登録を選択します。品目: <品目コードを入力します>プラント: <プラントを入力>製造バージョン: <4 桁の数字>製造バージョンテキスト: <テキスト> |  |  |
| 6 | パラメータを入力する | 必要なパラメータを入力し、登録を選択します。有効開始日付: <本日>有効終了日付: <9999/12/31>最小ロットサイズ: <1>最大ロットサイズ: <999999999>タスクリストセクション:タスクリストタイプ: <品目のタスクリストタイプを選択>タスクリストグループ: <品目のグループを選択>タスクリストカウンタ: <品目のグループカウンタを選択>部品表/配合表画面:代替 BOM: <品目の代替 BOM を選択>BOM 用途: <品目の BOM マスタの BOM 用途を選択> | 製造バージョンが登録されます。 |  |

オプション 3

| テストステップ番号 | テストステップ名 | 指示 | 予想される結果 | コメント |
| --- | --- | --- | --- | --- |
| 1 | ログオンする | SAP Fiori ラウンチパッドに生産エンジニア - ディスクリート製造または生産エンジニア - プロセス生産としてログオンします。 | 開始ビューが表示されます。 |  |
| 2 | SAP Fiori アプリにアクセスする | 製造バージョン管理(F2568)を開きます。 | 製造バージョン: 一括処理ビューが表示されます。 |  |
| 3 | プラントコードを入力する | プラントコードを入力します。 |  |  |
| 4 | 品目を入力する | 品目を入力します。Enter を押します。 |  |  |
| 5 | 製造バージョン | 製造バージョンの明細を入力して、Enter を押します。品目: <品目コードを入力します>製造バージョン: <4 桁の数字>有効開始日: <本日>有効終了日: <9999/12/31>開始ロットサイズ: <1>終了ロットサイズ: <999999999>代替 BOM: F4 を押して品目の代替 BOM を選択します。BOM 用途: F4 を押して品目の BOM マスタの BOM 用途を選択します。グループ: <品目のグループを入力します>グループカウンタ: <品目のグループカウンタを入力します>タイプ: <品目のタスクリストタイプを選択> |  |  |
| 6 | データを保存する | 保存を選択します。 | 製造バージョンが登録されます。 |  |

### 製造バージョンの編集 (オプション)

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
| 1 | ログオンする | SAP Fiori ラウンチパッドに生産エンジニア - ディスクリート製造または生産エンジニア - プロセス生産としてログオンします。 | SAP Fiori ラウンチパッドが表示されます。 |  |
| 2 | SAP Fiori アプリにアクセスする | 製造バージョン処理(F6400)を開きます。 | アプリが開きます。 |  |
| 3 | 選択項目を入力する | 以下のエントリを入力してGoを選択します。品目: <品目コードを入力します>プラント: <プラントを入力> |  |  |
| 4 | 既存の製造バージョンタブにナビゲートする | 既存の製造バージョンタブに移動します。 |  |  |
| 5 | 製造バージョンを編集する | 変更する製造バージョンを選択し、製造バージョン画面で編集を選択します。必要に応じて、項目を変更します。注記 複数の製造バージョンに同様の変更を行う場合は、既存の製造バージョンタブで複数選択を行い、一括編集を選択することができます。一括編集ダイアログボックスで、一覧表示された項目に必要な変更を行うことができます。 |  |  |
| 6 | 保存する | 保存を選択します。 | 製造バージョンが正常に更新されます。 |  |

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
- related-to :: [[12-production-and-manufacturing/fertigungsversion-anlegen-sds-bld-568]]
- related-to :: [[12-production-and-manufacturing/master-data-script-create-production-version-mds-bld-569]]
- related-to :: [[12-production-and-manufacturing/mds-bld-573]]
- related-to :: [[12-production-and-manufacturing/script-de-dados-mestre-criar-versao-de-producao-mds-bld-572]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/BLD_S4CLD2608_Master_Data_JA_XX.docx` — full document · extracted with `mammoth` · 9,343 chars in the whole document
