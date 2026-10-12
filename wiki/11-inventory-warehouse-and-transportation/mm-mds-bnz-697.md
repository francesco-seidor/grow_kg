---
id: 11-inventory-warehouse-and-transportation/mm-mds-bnz-697
title: オープン MM 転記期間の新規登録 - MDS (BNZ) (BNZ_S4CLD2608_Master_Data_JA_XX)
description: Master data script (Japanese) for opening a new MM posting period in SAP S/4HANA Cloud Public Edition 2608 using the Close Periods app (MMPV).
cluster: 11-inventory-warehouse-and-transportation
tags: [kb/inventory-warehouse-and-transportation, topic/mm-posting-periods]
aliases: [BNZ_S4CLD2608_Master_Data_JA_XX]
keywords: [MM Posting Periods, mm posting period, period closing, material valuation, business roles, master data scripts, BNZ]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/BNZ_S4CLD2608_Master_Data_JA_XX.docx]
confidence: high
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-697
topic: 11-inventory-warehouse-and-transportation/mm-posting-periods
language: JA
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# オープン MM 転記期間の新規登録 - MDS (BNZ) (BNZ_S4CLD2608_Master_Data_JA_XX)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/BNZ_S4CLD2608_Master_Data_JA_XX.docx`, extracted with `mammoth`. Grouped under **MM Posting Periods** in Inventory, Warehouse and Transportation. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

| <!-- image omitted: unnamed --> | マスタデータスクリプトSAP S/4HANA Cloud Public Edition - 02-07-26 |
| --- | --- |
|  | オープン MM 転記期間の新規登録 - MDS (BNZ) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

目次

[1 目的 2](#_Toc233892039)

[2 前提条件 3](#_Toc233892040)

[2.1 システムアクセス 3](#_Toc233892041)

[2.2 ロール 3](#_Toc233892042)

[3 概要テーブル 4](#_Toc233892043)

[4 テスト手順 5](#_Toc233892044)

[4.1 MM 期間の終了および新規会計期間の開始 5](#_Toc233892045)

## 目的

在庫品目に関する情報および特定の評価データ (合計在庫金額、合計在庫、評価要素クラス、原価管理区分、価格単位など) は、財務会計期間別に保持されます。この期間は、金額および在庫移動が適切な期間に転記されるように、各新会計期間の開始時に設定する必要があります。通常、現会計期間のみが転記用にオープンしています。その他すべての会計期間はクローズされています。

前の期間への遡及転記は、対応するフラグが管理レコードに設定されている場合にのみ可能です。このフラグは初期化時および各期間変更後に自動的に設定されます。ただし、フラグをマニュアルで設定する必要がある場合があります。

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
| マスタデータスペシャリスト - 製品データ | SAP_BR_PRODMASTER_SPECIALIST | マスタデータ - 製品/製品ガバナンス | SAP_BR_PRODMASTER_SPECIALIST / SAP_CMD_SPT_PR_GOV_PC |  |

## 概要テーブル

このスコープアイテムは、以下の表に示されている複数のプロセスステップで構成されます。

|  |
| --- |
| 注記 システム管理者が SAP Fiori ラウンチパッドでスペースおよびページを有効化している場合、ホームページには、ビジネスロールの一般的なタスクを実行するために必要なアプリのみが含まれます。ホームページに含まれていないその他すべての (検索可能な) アプリは、検索バーを使用して見つけることができます ([2434549](https://me.sap.com/notes/2434549))。ホームページをパーソナライズして非表示のアプリを含める場合は、ユーザプロファイルにナビゲートし、アプリファインダを選択します。 |

| プロセスステップ | ビジネスロール | トランザクション/アプリ | 予想される結果 |
| --- | --- | --- | --- |
| [MM 期間の終了および新規会計期間の開始](#unique_6) [ ページ] 5 | マスタデータスペシャリスト - 製品データ | 締め処理(MMPV) | 会計期間が最新の状態になっています。 |

## テスト手順

このセクションでは、このスコープアイテムに属する各プロセスステップのテスト手順について説明します。

### MM 期間の終了および新規会計期間の開始

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
| 1. | ログオンする | SAP Fiori ラウンチパッドにマスタデータスペシャリスト - 製品データとしてログオンします。 | SAP Fiori ラウンチパッドが表示されます。 |  |
| 2 | SAP Fiori アプリにアクセスする | 締め処理(MMPV)を開きます。注記 締め処理タイルが表示されない場合は、Fiori ラウンチパッドの右上にあるドロップダウンリストからタイルカタログを選択します。マスタデータ - 管理グループで締め処理タイルにナビゲートしてMy ホームグループに追加します。 | アプリが開きます。 |  |
| 3 | 選択データを入力する | 会計期間締め: 品目マスタレコード画面で以下のように入力します。会社コード 開始: <自社の会社コード>会社コード 終了: <自社の会社コード>期間: オープンする期間会計年度: <現会計年度>期間の確認および締め処理: 選択注記 期間項目に月の 2 桁の数字を入力します。たとえば、1 月は01、10 月は10に対応します。現会計期間をオープンするには、次期間に現在の月を入力します。 |  |  |
| 4 | 実行を選択する | 会計期間締め: 品目マスタレコード画面で実行を選択します。 |  |  |
| 5 | 結果をチェックする | 管理レコードの当期 (月/年) は <入力した期間/年度> ですというログが表示された場合は、ここで停止できます。注記 会計期間がまだ過去になっている場合は、正しい (現) 会計期間に達するまで、上記のステップを期間ごとに繰り返します。たとえば、表示されている期間が04 2014の場合、12 2015の期間をオープンする必要があっても、これを直接行うことはできません。代わりに、期間05 2014をオープンしてから、06 2014オープンするなどして、現会計期間に達するまでこれを繰り返す必要があります。過去の会計年度の実地棚卸期間をクローズする必要がある場合は、ステップ 3 で過去の会計年度の期間をオープン/クローズしていることを示すメッセージが表示されることがあります。このシステムメッセージを確認する必要があります。 | 会計期間が最新の状態になっています。 |  |

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
- related-to :: [[11-inventory-warehouse-and-transportation/crear-nuevo-periodo-contable-mm-abierto-mds-bnz-696]]
- related-to :: [[11-inventory-warehouse-and-transportation/create-new-open-mm-posting-period-mds-bnz-695]]
- related-to :: [[11-inventory-warehouse-and-transportation/criar-periodo-contabil-mm-aberto-mds-bnz-698]]
- related-to :: [[11-inventory-warehouse-and-transportation/mds-bnz-699]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/BNZ_S4CLD2608_Master_Data_JA_XX.docx` — full document · extracted with `mammoth` · 6,081 chars in the whole document
