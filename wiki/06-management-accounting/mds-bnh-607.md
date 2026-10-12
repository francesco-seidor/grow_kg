---
id: 06-management-accounting/mds-bnh-607
title: 利益センタの登録 - MDS (BNH) (BNH_S4CLD2608_Master_Data_JA_XX)
description: "Japanese master data script BNH: creating profit center master data via app F3516 (legacy) in S/4HANA Cloud Public Edition 2608, with mandatory fields and validity periods."
cluster: 06-management-accounting
tags: [kb/management-accounting, topic/profit-centers]
aliases: [BNH_S4CLD2608_Master_Data_JA_XX]
keywords: [Profit Centers and Profit Center Reorganization, profit centers, validity periods, controlling area, profit center groups, segment reporting, business roles, company code assignment, BNH]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/BNH_S4CLD2608_Master_Data_JA_XX.docx]
confidence: high
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-607
topic: 06-management-accounting/profit-centers
language: JA
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# 利益センタの登録 - MDS (BNH) (BNH_S4CLD2608_Master_Data_JA_XX)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/BNH_S4CLD2608_Master_Data_JA_XX.docx`, extracted with `mammoth`. Grouped under **Profit Centers and Profit Center Reorganization** in Management Accounting. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

| <!-- image omitted: unnamed --> | マスタデータスクリプトSAP S/4HANA Cloud Public Edition - 02-07-26 |
| --- | --- |
|  | 利益センタの登録 - MDS (BNH) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

目次

[1 目的 2](#_Toc233891932)

[2 前提条件 3](#_Toc233891933)

[2.1 システムアクセスとロール 3](#_Toc233891934)

[2.2 必須の組織ユニット 3](#_Toc233891935)

[2.3 必須マスタデータおよび任意マスタデータ 4](#_Toc233891936)

[2.4 データ登録の主要パラメータ 5](#_Toc233891937)

[3 概要テーブル 6](#_Toc233891938)

[4 テスト手順 7](#_Toc233891939)

[4.1 利益センタマスタデータを登録する 7](#_Toc233891940)

## 目的

利益センタは、内部統制を目的とした組織の管理指向構造が反映される会計管理の組織ユニットです。会社を利益センタに分割することにより、内部責任領域の利益を決定し、責任を分散ユニットに移譲することができます。

利益センタのマスタデータには、利益センタ名、割当先の管理領域、利益センタの有効期間、利益センタの責任者に関する情報、標準階層のノードに対する利益センタの割当、および通信に必要なデータ (アドレス、電話番号など) が含まれます。

## 前提条件

このセクションでは、システム、ユーザ、マスタデータ、組織データ、その他テストデータ、およびビジネス条件に関するテストを実施するためのすべての前提条件がまとめられています。

### システムアクセスとロール

以下のシステムでテストを実施します。

| システム | 詳細 |
| --- | --- |
| SAP S/4HANA Cloud Public Edition | システム ID: ###クライアント: ### |

SAP から提供される以下のビジネスロールテンプレートを使用して、ビジネスロールを登録し、それらを個別のテストユーザに割り当てます。

または、利用可能な場合は、SAP から提供される以下のスペースを使用することができます。スペーステンプレートを使用して、必要な事前定義済アプリを含むページのあるスペースを登録し、それをビジネスロールに割り当てます。その後、このビジネスロールを個別のユーザに割り当てます。

詳細については、SAP S/4HANA Cloud Public Editionの[Product Assistance](https://help.sap.com/docs/SAP_S4HANA_CLOUD/53e36b5493804bcdb3f6f14de8b487dd/ec310a8b669a45ca898dc4dd91d97de2.html)でテンプレートからのビジネスロールの作成方法を参照してください。

| 名称 (ロールテンプレート) | ID (ロールテンプレート) | 名称 (ラウンチパッド領域) | ID (ラウンチパッド領域) | ログオンする |
| --- | --- | --- | --- | --- |
| 部門別担当者 | SAP_BR_DIVISION_ACCOUNTANT | 部門別会計 | SAP_BR_DIVISION_ACCOUNTANT |  |

### 必須の組織ユニット

得意先マスタデータの一部のセグメントは会社の組織ユニットに依存し、一般 (セントラル) データは組織ユニットまたは会社コードに依存しません。以下の表は、さまざまなデータセグメントおよび関連する組織ユニットの概要を示しています。

| データセグメント | 依存対象 | 項目例 | コメント | 使用される組織ユニット |
| --- | --- | --- | --- | --- |
| 利益センタの基本データ | 管理領域利益センタグループセグメント | 名称、テキスト (長)、有効期間、責任ユーザ、責任者 | 利益センタグループを使用することにより、管理者は、カスタマイジングやレポートなどで 1 つの利益センタ名を入力するのではなく、グループ名を入力して、利益センタをグループで指定できます。これにより、レポートの集約レベルで管理会計キー数値を分析できます。セグメントは通常では明示的に転記されることはありません。データは利益センタなど勘定割当対象から誘導されます。一方で、利益センタは通常では明示的に転記されることはありません。データは原価センタや内部指図など一次勘定割当対象から誘導されます。 | 管理領域:____________利益センタグループ:____________セグメント:____________ |
| 利益センタ会社コード割当 | 会社コード | 会社コード | 会社コードデータは、利益センタマスタレコードが使用される企業構造のすべての会社コード ID に対して存在する可能性があります。 | 会社コード:____________ |

### 必須マスタデータおよび任意マスタデータ

以下の表は、利益センタマスタデータレコードで使用される任意および必須のマスタデータオブジェクトの概要を示しています。

| マスタデータオブジェクト | データセグメントでの使用 | 必須/任意 | コメント |
| --- | --- | --- | --- |
| 管理領域 | 利益センタの基本データ | 必須 | 参照管理領域を使用して、新規利益センタを登録できます。 |
| 利益センタ | 利益センタの基本データ | 必須 | 参照利益センタを使用して、新規利益センタを登録できます。 |
| 有効開始 | 利益センタの基本データ | 必須 |  |
| 有効終了 | 利益センタの基本データ | 必須 |  |
| 名称 | 利益センタの基本データ | 必須 |  |
| テキスト (長) | 利益センタの基本データ | 任意 |  |
| 責任ユーザ | 利益センタの基本データ | 任意 |  |
| 責任者 | 利益センタの基本データ | 必須 |  |
| 利益センタグループ | 利益センタの基本データ | 必須 |  |
| 部門 | 利益センタの基本データ | 任意 |  |
| セグメント | 利益センタの基本データ | 任意 | 米国企業の利益センタが有効である場合は、セグメント項目にデータを入力することをお奨めします。これにより、セグメントレポートを実行できます。 |
| 計画テンプレート | 利益センタの基本データ | 任意 |  |
| 住所および通信項目 | 利益センタの住所および通信データ | すべて任意 |  |

### データ登録の主要パラメータ

このセクションでは、マスタレコードの動作に影響し、利益センタマスタデータレコードの登録に常に必要となる基本パラメータの一部について説明します。

管理領域:A000

## 概要テーブル

このスコープアイテムは、以下の表に示されている複数のプロセスステップで構成されます。

|  |
| --- |
| 注記 システム管理者が SAP Fiori ラウンチパッドでスペースおよびページを有効化している場合、ホームページには、ビジネスロールの一般的なタスクを実行するために必要なアプリのみが含まれます。ホームページに含まれていないその他すべての (検索可能な) アプリは、検索バーを使用して見つけることができます ([2434549](https://me.sap.com/notes/2434549))。ホームページをパーソナライズして非表示のアプリを含める場合は、ユーザプロファイルにナビゲートし、アプリファインダを選択します。 |

| プロセスステップ | ビジネスロール | トランザクション/アプリ | 予想される結果 |
| --- | --- | --- | --- |
| [利益センタマスタデータを登録する](#unique_8) [ ページ] 7 | 部門別担当者 | 利益センタ管理 - 旧バージョン(F3516) | 新しいウィンドウが開いて、利益センタのマスタデータ画面が表示されます。 |

## テスト手順

このセクションでは、このスコープアイテムに属する各プロセスステップのテスト手順について説明します。

### 利益センタマスタデータを登録する

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
| 1 | ログオンする | SAP Fiori ラウンチパッドに部門別担当者としてログオンします。 | SAP Fiori ラウンチパッドが表示されます。 |  |
| 2 | SAP Fiori アプリにアクセスする | 利益センタ管理 - 旧バージョン(F3516)を開きます。 | 利益センタのマスタデータ画面が表示されます。 |  |
| 3 | 利益センタを検索する | 利益センタを検索します。Goを選択します。 | 利益センタの一覧が画面に表示されます。 |  |
| 4 | 利益センタを追加する | 登録を選択します。 | 利益センタ: 新規画面が表示されます。 |  |
| 5 | 新規利益センタのデータを入力する | 新規利益センタセクションで、以下のデータを入力します。利益センタ: <名称>、YBXXX など注記 最大長は 10 文字です%、!、$、&、@ などの特殊文字は使用しないでください。これらの文字は、アプリがクラッシュする原因となり、削除することができません。有効開始: <有効開始日付>有効終了: <有効終了日付>名: <任意のテキスト>責任者: <責任者の名前> |  |  |
| 6 | 基本データを入力する | 組織ユニットタブで、以下のデータを入力します。標準階層ノード: <利益センタグループ>セグメント: <セグメント> |  |  |
| 7 | 会社コード割当 | 会社コードを新規利益センタに割り当てるためにこのチェックボックスを選択するか、または選択を解除します。 |  |  |
| 8 | データを保存する | エントリを保存します。 |  |  |
| 9 | 新規有効期間を設定する (オプション) | 編集を選択します。登録した利益センタで、有効期間 > 新規有効期間を選択します。有効開始および有効終了項目にエントリを入力し、ソースデータ期間を選択します。登録を選択します。注記 新規有効期間が既存の有効期間と重複する場合は、重複している期間が既存の期間から除外されます。新規有効期間と他の期間との間にギャップがある場合は、このアクションが回避されます。 |  |  |
| 10 | 時間依存の項目を変更する (オプション) | 新規登録された有効期間では、以下の時間依存項目を変更することができます。部門利益センタ責任者責任ユーザ役職名前名前 2:名前 3名前 4ロックフラグ:保存を選択します。注記 時間依存ではない項目を変更すると、その変更がすべての有効期間にわたって適用されます。新規期間と先行期間または後続期間との間に差異がない場合は、新規期間が既存の期間とマージされます。 | 新規有効期間が登録されます。変更レコードが変更ログセクションに表示されます。 |  |

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
- related-to :: [[06-management-accounting/create-profit-center-mds-bnh-605]]
- related-to :: [[06-management-accounting/mds-bnh-609]]
- related-to :: [[06-management-accounting/profitcenter-anlegen-sds-bnh-604]]
- related-to :: [[06-management-accounting/script-de-dados-mestre-criar-centro-de-lucro-mds-bnh-608]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/BNH_S4CLD2608_Master_Data_JA_XX.docx` — full document · extracted with `mammoth` · 7,751 chars in the whole document
