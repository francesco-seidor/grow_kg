---
id: 03-financial-accounting-and-close/g-l-mds-bng-601
title: "マスタデータスクリプト: G/L 勘定および原価要素の登録 - MDS (BNG) (BNG_S4CLD2608_Master_Data_JA_XX)"
description: "Japanese master data test script (BNG): create G/L accounts and cost elements by copying, via Solution Settings or Central Business Configuration."
cluster: 03-financial-accounting-and-close
tags: [kb/financial-accounting-and-close, topic/chart-of-accounts-and-gl-accounts]
aliases: [BNG_S4CLD2608_Master_Data_JA_XX]
keywords: [Chart of Accounts YCOA and G/L Account Creation, g/l account master data, cost elements, master data scripts, chart of accounts, account types and groups, mandatory master data, business roles, solution settings, central business configuration]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/BNG_S4CLD2608_Master_Data_JA_XX.docx]
confidence: high
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-601
topic: 03-financial-accounting-and-close/chart-of-accounts-and-gl-accounts
language: JA
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# マスタデータスクリプト: G/L 勘定および原価要素の登録 - MDS (BNG) (BNG_S4CLD2608_Master_Data_JA_XX)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/BNG_S4CLD2608_Master_Data_JA_XX.docx`, extracted with `mammoth`. Grouped under **Chart of Accounts YCOA and G/L Account Creation** in Financial Accounting and Close. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

| <!-- image omitted: unnamed --> | マスタデータスクリプトSAP S/4HANA Cloud Public Edition - 02-07-26 |
| --- | --- |
|  | G/L 勘定および原価要素の登録 - MDS (BNG) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

目次

[1 目的 2](#_Toc233891942)

[2 前提条件 3](#_Toc233891943)

[2.1 システムアクセス 3](#_Toc233891944)

[2.2 ロール 3](#_Toc233891945)

[2.3 必須の組織ユニット 4](#_Toc233891946)

[2.4 必須マスタデータおよび任意マスタデータ 4](#_Toc233891947)

[2.5 データ登録の主要パラメータ 6](#_Toc233891948)

[3 概要テーブル 7](#_Toc233891949)

[4 テスト手順 8](#_Toc233891950)

[4.1 G/L 勘定を登録する 8](#_Toc233891951)

## 目的

G/L 勘定マスタレコードには、会計トランザクションの転記および管理方法を制御する、勘定に関する情報が含まれています。

SAP の総勘定元帳は、すべての資産、債務および債権勘定の包括的な最新のビューを提供し、他の SAP モジュールと完全に統合されています。

すべての SAP モジュールが統合されているため、一部の GL 転記はシステムにおいて自動でバックグラウンド生成されます。これには、GR/IR 勘定転記 (入庫/請求書受領) や在庫移動 GL 転記などが含まれます。

一部の勘定は、'明細消込管理' の対象です。これらの勘定は消込勘定として使用されるため、入金時、支払時、品目処理時などに個別の明細を消し込むことができます。

得意先および仕入先統制勘定などのその他の勘定は、補助元帳のビジネスパートナが反映されているにすぎないため、直接転記することはできません。

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
| 設定エキスパート - ビジネスプロセス設定 | SAP_BR_BPC_EXPERT | ビジネスプロセス設定/ビジネスプロセス設定 - ファイナンス/ビジネスプロセス設定 - 調達/ソリューション管理/ビジネスプロセス設定 - ワークフロー/ビジネスコンフィグレーション - 機能管理/ビジネスプロセス設定 - Extensibility Explorer/ビジネス設定 - 輸送 | SAP_BR_BPC_EXPERT / SAP_FIN_SPT_BPC_EXPERT_PC / SAP_MM_SPT_BIZ_PROC_CONFIGN_PC / SAP_CA_SPT_IC_LND_BASE_PC / SAP_CA_SPT_BPC_WORKFLOW_PC / SAP_CA_SPT_BPC_FM_PC / SAP_EI_SPT_BPC_EXT_PC / SAP_TM_SPT_TRANSPCFG_PC |  |

### 必須の組織ユニット

得意先マスタデータの一部のセグメントは会社の組織ユニットに依存し、一般 (共通) データは組織ユニットまたは会社コードに依存しません。以下の表は、さまざまなデータセグメントおよび関連する組織ユニットの概要を示しています。

| データセグメント | 依存対象 | 項目例 | コメント | 使用される組織ユニット |
| --- | --- | --- | --- | --- |
| G/L 勘定 | 会社コード勘定コード表管理領域 | [必須マスタデータおよび任意マスタデータ](#unique_6) [ ページ] 4 を参照してください。 | 会社コードデータは、GL 勘定および原価要素マスタレコードが使用される企業構造のすべての会社コード ID に対して存在する可能性があります。 | 会社コード:____________勘定コード表____________管理領域____________ |

### 必須マスタデータおよび任意マスタデータ

得意先マスタデータレコードは、他のマスタデータを参照することがあります。以下の表は、得意先マスタデータレコードで使用される任意および必須のマスタデータオブジェクトの概要を示しています。

| マスタデータオブジェクト | データセグメントでの使用 | 必須/任意 | コメント |
| --- | --- | --- | --- |
| 勘定コード表 | G/L 勘定 UI の一般タブの管理セクションにエントリが表示されます。 | 必須 |  |
| G/L 勘定 | G/L 勘定 UI の勘定コピー画面にエントリが表示されます。 | 必須 |  |
| 説明 | G/L 勘定 UI の勘定コピー画面にエントリが表示されます。 | 必須 |  |
| 勘定タイプ | G/L 勘定 UI の一般タブの管理セクションにエントリが表示されます。 | 必須 |  |
| 勘定グループ | G/L 勘定 UI の一般タブの管理セクションにエントリが表示されます。 | 必須 |  |
| 機能領域 | G/L 勘定 UI の一般タブの管理セクションにエントリが表示されます。 | 任意 | P&amp;L 勘定に使用します。 |
| G/L 勘定テキスト (長) | G/L 勘定 UI の一般タブのテキストセクションにエントリが表示されます。 | 任意 |  |
| 会社コードチェックボックス | G/L 勘定 UI の一般タブの会社コードでの定義セクションにエントリが表示されます。 | 必須 | 1 つまたは複数の会社コードに割り当てます。 |
| 登録ブロック | G/L 勘定 UI の一般タブの管理セクションにエントリが表示されます。 | 任意 |  |
| 転記ブロック | G/L 勘定 UI の一般タブの管理セクションにエントリが表示されます。 | 任意 |  |
| 計画ブロック | G/L 勘定 UI の一般タブの管理セクションにエントリが表示されます。 | 任意 |  |
| 削除フラグ設定済 | G/L 勘定 UI の一般タブの管理セクションにエントリが表示されます。 | 任意 |  |
| 勘定通貨 | 新規 G/L 勘定を登録すると、制御データ > 勘定管理セクションに会社コードの詳細が表示されます。 |  |  |
| 国内通貨の残高のみ | 新規 G/L 勘定を登録すると、制御データ > 勘定管理セクションに会社コードの詳細が表示されます。 | 任意 |  |
| 税カテゴリ | 新規 G/L 勘定を登録すると、制御データ > 勘定管理セクションに会社コードの詳細が表示されます。 | 任意 |  |
| 税なしの転記可能 | 新規 G/L 勘定を登録すると、制御データ > 勘定管理セクションに会社コードの詳細が表示されます。 | 任意 |  |
| 代替勘定コード | 新規 G/L 勘定を登録すると、制御データ > 勘定管理セクションに会社コードの詳細が表示されます。 | 任意 |  |
| ソートキー | 新規 G/L 勘定を登録すると、制御データ > 勘定コード管理セクションに会社コードの詳細が表示されます。 | 任意 |  |
| 管理領域 | 新規 G/L 勘定を登録すると、制御データ > 管理領域の会計管理設定セクションに会社コードの詳細が表示されます。 | 必須 | 勘定タイプ貸借対照表勘定のオプション |
| 原価要素タイプ | 新規 G/L 勘定を登録すると、制御データ > 管理領域の会計管理設定セクションに会社コードの詳細が表示されます。 | 必須 | 勘定タイプ貸借対照表勘定のオプション |
| レコード数量 | 新規 G/L 勘定を登録すると、制御データ > 管理領域の会計管理設定セクションに会社コードの詳細が表示されます。 | 任意 |  |
| 項目ステータスグループ | 新規 G/L 勘定を登録すると、登録/銀行/金利 > 伝票登録の制御セクションに会社コードの詳細が表示されます。 | 任意 |  |
| 自動転記のみ | 新規 G/L 勘定を登録すると、登録/銀行/金利 > 伝票登録の制御セクションに会社コードの詳細が表示されます。 | 任意 |  |
| 補足自動転記 | 新規 G/L 勘定を登録すると、登録/銀行/金利 > 伝票登録の制御セクションに会社コードの詳細が表示されます。 | 任意 |  |
| 計画レベル | 新規 G/L 勘定を登録すると、登録/銀行/金利 > 銀行/財務詳細セクションに会社コードの詳細が表示されます。 | 任意 |  |
| キャッシュフロー関連 | 新規 G/L 勘定を登録すると、登録/銀行/金利 > 銀行/財務詳細セクションに会社コードの詳細が表示されます。 | 任意 |  |
| 転記ブロック | 新規 G/L 勘定を登録すると、管理に会社コードの詳細が表示されます。 | 任意 |  |
| 削除フラグ設定済 | 新規 G/L 勘定を登録すると、管理に会社コードの詳細が表示されます。 | 任意 |  |
| 翻訳テキスト | G/L 勘定 UI の翻訳タブの言語キーセクションにエントリが表示されます。 | 任意 | 必要な言語にテキストを翻訳します。 |

### データ登録の主要パラメータ

このセクションでは、マスタレコードの動作に影響し、得意先マスタデータレコードの登録に常に必要となる基本パラメータの一部について説明します。

勘定タイプ

- 貸借対照表勘定
- 営業外費用または営業外利益
- 一次原価または一次収益
- 二次原価

勘定グループ

- 統制勘定入力可能
- 固定資産勘定
- 損益計算書勘定
- 流動資金勘定
- 在庫/購買管理勘定
- G/L 勘定 (一般)

## 概要テーブル

このスコープアイテムは、以下の表に示されている複数のプロセスステップで構成されます。

|  |
| --- |
| 注記 システム管理者が SAP Fiori ラウンチパッドでスペースおよびページを有効化している場合、ホームページには、ビジネスロールの一般的なタスクを実行するために必要なアプリのみが含まれます。ホームページに含まれていないその他すべての (検索可能な) アプリは、検索バーを使用して見つけることができます ([2434549](https://me.sap.com/notes/2434549))。ホームページをパーソナライズして非表示のアプリを含める場合は、ユーザプロファイルにナビゲートし、アプリファインダを選択します。 |

| プロセスステップ | ビジネスロール | トランザクション/アプリ | 予想される結果 |
| --- | --- | --- | --- |
| [G/L 勘定を登録する](#unique_9) [ ページ] 8 | 設定エキスパート - ビジネスプロセス設定 | ソリューション管理 (F1241) |  |

## テスト手順

このセクションでは、このスコープアイテムに属する各プロセスステップのテスト手順について説明します。

### G/L 勘定を登録する

テスト管理

カスタマプロジェクト: プロジェクト固有部分への入力

|  |  |  |  |
| --- | --- | --- | --- |
| テストケース ID | <X.XX> | テスト実施日: |  |
| テスト実施者名: |  | 期間: |  |
| ビジネスロール: |  | 責任者: | <都道府県/州、サービスプロバイダ、カスタマ/共同サービスプロバイダ、およびカスタマ> |

目的

新規 G/L 勘定を登録する際に、既存の番号範囲を新規 G/L 勘定の参照として使用することをお奨めします。

手順

SAP S/4HANA Cloud Public Editionの設定環境に応じて、以下のいずれかのオプションを選択します。

ソリューション設定:

| テストステップ番号 | テストステップ名 | 指示 | 予想される結果 | コメント |
| --- | --- | --- | --- | --- |
| 1 | ログオンする | SAP Fiori ラウンチパッドに設定エキスパート - ビジネスプロセス設定としてログオンします。 | SAP Fiori ラウンチパッドが表示されます。 |  |
| 2 | SAP Fiori アプリにアクセスする | ソリューション管理 (F1241)を開きます。 |  |  |
| 3 | 設定にアクセスする | ソリューション設定を開きます。 | ソリューション設定: 実現化フェーズ画面が表示されます。 |  |
| 4 | 設定にアクセスする | 以下のエントリを入力します。アプリケーションエリア: 財務サブアプリケーションエリア: 総勘定元帳 |  |  |
| 5 | 開く | 勘定コード表明細で、列の右側にある矢印を選択します。 |  |  |
| 6 | 設定ステップを選択する | G/L 勘定マスタデータ管理ステップで設定を選択します。 |  |  |
| 7 | 勘定を検索する | 以下のエントリを入力してGoを選択します。ビュー: 勘定コード表ビュー勘定コード表: YCOA | 一致する G/L 勘定の一覧が表示されます。 |  |
| 8 | G/L 勘定を選択する | 検索結果から G/L 勘定を選択します。注記 青い勘定コードリンクをクリックします。 | G/L 勘定マスタデータ画面が表示されます。 |  |
| 9 | 勘定をコピーする | コピーを選択します。 | <G/L 勘定コード> のコピー画面が表示されます。 |  |
| 10 | アカウントを作成する | 以下のエントリを入力してOKを選択します。勘定コード: <勘定コード>更新言語 (EN) のテキスト: <内容説明>グループ勘定コード: <勘定コード>注記 この項目は、連結が範囲内にある場合にのみ表示されます。 | 画面 G/L 勘定マスタデータで入力されたデータが表示されます。 |  |
| 11 | テキストを追加する | 基本情報セクションで、以下のエントリを入力します。勘定コード表: YCOAG/L 勘定テキスト (長): <テキスト> |  |  |
| 12 | 会社コードを割り当てる | 会社コード割当セクションで、会社コードを選択して勘定に割り当てます。 |  |  |
| 13 | 翻訳を追加する | 翻訳セクションで、すべての必要な言語で短いテキストと長いテキストを入力します。 |  |  |
| 14 | データを保存する | 保存を選択します。 | 勘定が正常に保存されたことが確認されます。 |  |

SAP Central Business Configuration:

| テストステップ番号 | テストステップ名 | 指示 | 予想される結果 | コメント |
| --- | --- | --- | --- | --- |
| 1 | ログオンする | SAP Central Business Configuration でプロジェクト経験にログオンします。 | 有効なフレキシブルワークフローが開きます。 |  |
| 2 | SAP Fiori アプリにアクセスする | Business Processes Configurationアプリに移動し、以下のアクティビティを検索します。Manage G/L Account Master Data検索結果でその明細を選択し、この設定アクティビティに関する追加の詳細を表示します。Go to Activityボタンを選択して、SAP S/4HANA Cloud Public Editionシステムに直接ナビゲートします。SAP Fiori ラウンチパッドに設定エキスパート - ビジネスプロセス設定としてログオンします。 |  |  |
| 3 | 勘定を検索する | 以下のエントリを入力してGoを選択します。ビュー: 勘定コード表ビュー勘定コード表: YCOA | 一致する G/L 勘定の一覧が表示されます。 |  |
| 4 | G/L 勘定を選択する | 検索結果から G/L 勘定を選択します。注記 青い勘定コードリンクをクリックします。 | G/L 勘定マスタデータ画面が表示されます。 |  |
| 5 | 勘定をコピーする | コピーを選択します。 | <G/L 勘定コード> のコピー画面が表示されます。 |  |
| 6 | アカウントを作成する | 以下のエントリを入力してOKを選択します。勘定コード: <勘定コード>更新言語 (EN) のテキスト: <内容説明>グループ勘定コード: <勘定コード>注記 この項目は、連結が範囲内にある場合にのみ表示されます。 | 画面 G/L 勘定マスタデータで入力されたデータが表示されます。 |  |
| 7 | テキストを追加する | 基本情報セクションで、以下のエントリを入力します。勘定コード表: YCOAG/L 勘定テキスト (長): <テキスト> |  |  |
| 8 | 会社コードを割り当てる | 会社コード割当セクションで、会社コードを選択して勘定に割り当てます。 |  |  |
| 9 | 翻訳を追加する | 翻訳セクションで、すべての必要な言語で短いテキストと長いテキストを入力します。 |  |  |
| 10 | データを保存する | 保存を選択します。 | 勘定が正常に保存されたことが確認されます。 |  |

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
- related-to :: [[03-financial-accounting-and-close/criar-conta-do-razao-e-classe-de-custo-mds-bng-602]]
- related-to :: [[03-financial-accounting-and-close/master-data-script-create-g-l-account-and-cost-element-mds-bng-599]]
- related-to :: [[03-financial-accounting-and-close/mds-bng-603]]
- related-to :: [[03-financial-accounting-and-close/sachkonto-und-kostenart-anlegen-sds-bng-598]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/BNG_S4CLD2608_Master_Data_JA_XX.docx` — full document · extracted with `mammoth` · 10,862 chars in the whole document
