---
id: 04-tax-and-statutory-reporting/mds-2sw-277
title: 税条件の登録 - MDS (2SW) (2SW_S4CLD2608_Master_Data_JA_XX)
description: Japanese SAP S/4HANA Cloud Public Edition 2608 master data script for maintaining tax condition records (MEK2) and purchasing price conditions PPR0 (MEK1/MEK2).
cluster: 04-tax-and-statutory-reporting
tags: [kb/tax-and-statutory-reporting, topic/purchasing-tax-condition-records]
aliases: [2SW_S4CLD2608_Master_Data_JA_XX]
keywords: [Tax Condition Records and Purchasing Price Conditions, tax conditions, purchasing price conditions, price condition changes, tax codes, business roles, master data scripts, 2SW]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/2SW_S4CLD2608_Master_Data_JA_XX.docx]
confidence: high
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-277
topic: 04-tax-and-statutory-reporting/purchasing-tax-condition-records
language: JA
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# 税条件の登録 - MDS (2SW) (2SW_S4CLD2608_Master_Data_JA_XX)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/2SW_S4CLD2608_Master_Data_JA_XX.docx`, extracted with `mammoth`. Grouped under **Tax Condition Records and Purchasing Price Conditions** in Tax and Statutory Reporting. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

| <!-- image omitted: unnamed --> | マスタデータスクリプトSAP S/4HANA Cloud Public Edition - 02-07-26 |
| --- | --- |
|  | 税条件の登録 - MDS (2SW) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

目次

[1 目的 2](#_Toc233891511)

[2 前提条件 3](#_Toc233891512)

[2.1 システムアクセス 3](#_Toc233891513)

[2.2 ロール 3](#_Toc233891514)

[2.3 必須マスタデータおよび任意マスタデータ 3](#_Toc233891515)

[3 概要テーブル 5](#_Toc233891516)

[4 テスト手順 6](#_Toc233891517)

[4.1 税条件レコードの登録 6](#_Toc233891518)

[4.2 価格条件の登録 8](#_Toc233891519)

[4.3 価格条件の変更 9](#_Toc233891520)

## 目的

税条件レコードには、1 つの国/地域固有の情報と、品目の税区分/プラントの税区分/輸入の税区分の異なる組合せに対する異なる税コードが含まれています。

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
| 税務スペシャリスト | SAP_BR_TAX_SPECIALIST | 税率 | SAP_BR_TAX_SPECIALIST |  |
| 購買担当者 | SAP_BR_PURCHASER | 購買管理/ソーシングおよび契約 | SAP_MM_SPT_PURCHASING_PC / SAP_MM_SPT_SOURCING_PC |  |

### 必須マスタデータおよび任意マスタデータ

品目マスタデータレコードは、他のマスタデータを参照する場合があります。以下の表は、品目マスタデータレコードで使用される、任意および必須のマスタデータオブジェクトの概要を示しています。

このセクションでは、マスタレコードの動作に影響し、価格設定条件の登録に必ず必要となる基本パラメータの一部について説明します。

仕向国: DE など

| マスタデータオブジェクト | データセグメントでの使用 | 必須/任意 | コメント |
| --- | --- | --- | --- |
| 仕向国 | 第一画面を定義する | 必須 |  |

## 概要テーブル

このスコープアイテムは、以下の表に示す複数のプロセスステップで構成されます。

|  |
| --- |
| 注記 システム管理者が SAP Fiori ラウンチパッドでスペースおよびページを有効化している場合、ホームページには、ビジネスロールの一般的なタスクを実行するために必要なアプリのみが含まれます。ホームページに含まれていないその他すべての (検索可能な) アプリは、検索バーを使用して見つけることができます ([2434549](https://me.sap.com/notes/2434549))。ホームページをパーソナライズして非表示のアプリを含める場合は、ユーザプロファイルにナビゲートし、アプリファインダを選択します。 |

| プロセスステップ | ビジネスロール | SAP Fiori アプリ/トランザクション | 予想される結果 |
| --- | --- | --- | --- |
| [税条件レコードの登録](#unique_7) [ ページ] 6 | 税務スペシャリスト | 税率設定 - 購買管理(MEK2) | 税条件が設定されます。 |
| [価格条件の登録](#unique_8) [ ページ] 8 | 購買担当者 | 価格条件登録 - 購買管理(MEK1) | 価格設定条件が登録されます。 |
| [価格条件の変更](#unique_9) [ ページ] 9 | 購買担当者 | 価格条件変更 - 購買管理(MEK2) | 価格設定条件が変更されます。 |

## テスト手順

このセクションでは、このスコープアイテムに属する各プロセスステップのテスト手順について説明します。

### 税条件レコードの登録

テスト管理

カスタマプロジェクト: プロジェクト固有部分への入力

|  |  |  |  |
| --- | --- | --- | --- |
| テストケース ID | <X.XX> | テスト実施日: |  |
| テスト実施者名: |  | 期間: |  |
| ビジネスロール: |  | 責任者: | <都道府県/州、サービスプロバイダ、カスタマ/共同サービスプロバイダ、およびカスタマ> |

手順

| テストステップ | テストステップ名 | 指示 | 予想される結果 | コメント |
| --- | --- | --- | --- | --- |
| 1 | ログオンする | SAP Fiori ラウンチパッドに税務スペシャリストとしてログオンします。 | SAP Fiori ラウンチパッドが表示されます。 |  |
| 2 | SAP Fiori アプリにアクセスする | 税率設定 - 購買管理(MEK2)を開きます。 | アプリが開きます。 |  |
| 3 | 価格設定条件タイプ | 条件レコード変更画面で、以下のエントリを入力し、Enterを選択します。条件タイプ: TTX1など | キー組合せ画面が表示されます。 |  |
| 4 | キー組合せ | キー組合せ画面で、税: 品目/プラント/原産地チェックボックスを選択し、選択を選択します。 | 非控除税額変更 T(TTX1): 選択画面が表示されます。 |  |
| 5 | 仕向国 | 非控除税額変更 T(TTX1): 選択画面で以下のエントリを入力し、実行を選択します。仕向国: <国/地域コード> | 非控除税額の税条件変更 (TTX1): 概要画面が表示されます。 |  |
| 6 | 税条件を変更する | 非控除税額の税条件変更 (TTX1): 概要画面で、以下のエントリを入力します。品目の税区分: <品目の税区分>税区分Plnt: <税区分: プラント>輸入: <輸入>有効開始日: <有効開始日>有効終了日: <有効終了日>税コード: <税コード> | 税条件レコードが更新されます。 |  |
| 7 | 保存する | 保存を選択します。 | 税条件レコードが保存されます。 |  |
| 8 | 前画面を選択する | 前画面を 2 回選択します。 |  |  |
| 9 | 価格設定条件タイプ | 条件レコード変更画面で、以下のエントリを入力し、Enterを選択します。条件タイプ: TTX1など | キー組合せダイアログボックスが表示されます。 |  |
| 10 | キー組合せ | キー組合せダイアログボックスで、税: プラント/勘定設定/原産地/地域チェックボックスを選択し、選択を選択します。 | 非控除税額変更 T(TTX1): 選択画面が表示されます。 |  |
| 11 | 仕向国 | 非控除税額変更 T(TTX1): 選択画面で以下のエントリを入力し、実行を選択します。仕向国: <国/地域コード> | 非控除税額の税条件変更 (TTX1): 概要画面が表示されます。 |  |
| 12 | 税条件を変更する | 非控除税額の税条件変更 (TTX1): 概要画面で、以下のエントリを入力します。税区分Plnt: <税区分: プラント>税区分: 勘定設定: <勘定設定の税区分>輸入: <輸入>税区分地域: <地域>有効開始日: <有効開始日>有効終了: <有効終了日>税コード: <税コード> | 税条件レコードが更新されます。 |  |
| 13 | 保存する | 保存を選択します。 | 税条件レコードが保存されます。 |  |

### 価格条件の登録

テスト管理

カスタマプロジェクト: プロジェクト固有部分への入力

|  |  |  |  |
| --- | --- | --- | --- |
| テストケース ID | <X.XX> | テスト実施日: |  |
| テスト実施者名: |  | 期間: |  |
| ビジネスロール: |  | 責任者: | <都道府県/州、サービスプロバイダ、カスタマ/共同サービスプロバイダ、およびカスタマ> |

手順

| テストステップ | テストステップ名 | 指示 | 予想される結果 | コメント |
| --- | --- | --- | --- | --- |
| 1 | ログオンする | SAP Fiori ラウンチパッドに購買担当者としてログオンします。 | SAP Fiori ラウンチパッドが表示されます。 |  |
| 2 | SAP Fiori アプリにアクセスする | 価格条件登録 - 購買管理(MEK1)を開きます。 | アプリが開きます。 |  |
| 3 | 価格設定条件タイプ | 以下のエントリを入力してEnterを押します。条件タイプ: PPR0など | キー組合せダイアログボックスが表示されます。 |  |
| 4 | キー組合せ | キー組合せ画面で、品目購買情報 (プラント別)チェックボックスを選択し、選択を選択します。 | 登録 デフォルト総額 条件 (PPR0): 簡易入力画面が表示されます。 |  |
| 5 | デフォルト総額条件を登録する | 登録 デフォルト総額 条件 (PPR0): 簡易入力画面で、以下のエントリを入力します。サプライヤ: <サプライヤ>品目: <品目>購買組織: <購買組織>プラント: プラント:インフォタイプ: 0 標準など金額: <金額>単位: <価格単位>単位: <数量あたり>UoM: <単位>有効開始日: <有効開始日>有効終了日: <有効終了日> | デフォルト総額条件レコードが更新されます。 |  |
| 6 | 保存する | 保存を選択します。 | 条件レコードが保存されます。 |  |

### 価格条件の変更

テスト管理

カスタマプロジェクト: プロジェクト固有部分への入力

|  |  |  |  |
| --- | --- | --- | --- |
| テストケース ID | <X.XX> | テスト実施日: |  |
| テスト実施者名: |  | 期間: |  |
| ビジネスロール: |  | 責任者: | <都道府県/州、サービスプロバイダ、カスタマ/共同サービスプロバイダ、およびカスタマ> |

手順

| テストステップ | テストステップ名 | 指示 | 予想される結果 | コメント |
| --- | --- | --- | --- | --- |
| 1 | ログオン | SAP Fiori ラウンチパッドに購買担当者としてログオンします。 | SAP Fiori ラウンチパッドが表示されます。 |  |
| 2 | SAP Fiori アプリにアクセスする | 価格条件変更 - 購買管理(MEK2)を開きます。 | アプリが開きます。 |  |
| 3 | 価格設定条件タイプ | 以下のエントリを入力してEnterを押します。条件タイプ: PPR0など | キー組合せ画面が表示されます。 |  |
| 4 | キー組合せ | キー組合せ画面で、品目購買情報 (プラント別)チェックボックスを選択し、選択を選択します。 | 登録 デフォルト総額 条件 (PPR0): 簡易入力画面が表示されます。 |  |
| 5 | デフォルト総額条件を変更する | 変更 デフォルト総額 条件 (PPR0): 簡易入力画面で、以下のエントリを入力します。サプライヤ: <サプライヤ>品目: <品目>購買組織: <購買組織>プラント: <プラント>インフォタイプ: 0 標準など実行を選択します。以下のエントリを入力します。金額: <金額> | デフォルト総額条件レコードが変更されます。 |  |
| 6 | 保存する | 保存を選択します。 | 条件レコードが保存されます。 |  |

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
- related-to :: [[04-tax-and-statutory-reporting/crear-condicion-para-determinacion-de-impuestos-mds-2sw-276]]
- related-to :: [[04-tax-and-statutory-reporting/master-data-script-create-tax-condition-2sw-275]]
- related-to :: [[04-tax-and-statutory-reporting/mds-2sw-279]]
- related-to :: [[04-tax-and-statutory-reporting/objetivo-script-de-dados-mestre-criar-condicao-de-imposto-mds-2sw-port]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/2SW_S4CLD2608_Master_Data_JA_XX.docx` — full document · extracted with `mammoth` · 8,491 chars in the whole document
