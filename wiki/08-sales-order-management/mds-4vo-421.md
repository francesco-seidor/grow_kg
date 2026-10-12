---
id: 08-sales-order-management/mds-4vo-421
title: 製品代替の登録 - MDS (4VO) (マスタデータスクリプト) (4VO_S4CLD2608_Master_Data_JA_XX)
description: "Japanese master data script (4VO) for SAP S/4HANA Cloud Public Edition: creating product substitutions and product exclusions, with substitution reasons, groups and managements."
cluster: 08-sales-order-management
tags: [kb/sales-order-management, topic/product-and-location-substitution]
aliases: [4VO_S4CLD2608_Master_Data_JA_XX]
keywords: ["Product, Plant and Storage Location Substitution", product substitution, product exclusion, substitution reasons, substitution groups, substitution management, product master data, business roles, master data scripts, test procedures]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/4VO_S4CLD2608_Master_Data_JA_XX.docx]
confidence: high
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-421
topic: 08-sales-order-management/product-and-location-substitution
language: JA
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# 製品代替の登録 - MDS (4VO) (マスタデータスクリプト) (4VO_S4CLD2608_Master_Data_JA_XX)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/4VO_S4CLD2608_Master_Data_JA_XX.docx`, extracted with `mammoth`. Grouped under **Product, Plant and Storage Location Substitution** in Sales Order Management. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

| <!-- image omitted: unnamed --> | マスタデータスクリプトSAP S/4HANA Cloud Public Edition - 02-07-26 |
| --- | --- |
|  | 製品代替の登録 - MDS (4VO) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

目次

[1 目的 2](#_Toc233891717)

[2 前提条件 3](#_Toc233891718)

[2.1 システムアクセス 3](#_Toc233891719)

[2.2 ロール 3](#_Toc233891720)

[2.3 必須の組織ユニット 3](#_Toc233891721)

[2.4 必須のマスタデータ 4](#_Toc233891722)

[2.5 予備ステップ 4](#_Toc233891723)

[2.5.1 製品代替理由の登録 (オプション) 4](#_Toc233891724)

[2.5.2 代替グループの登録 (オプション) 5](#_Toc233891725)

[2.5.3 代替管理の登録 (オプション) 7](#_Toc233891726)

[3 概要テーブル 9](#_Toc233891727)

[4 テスト手順 10](#_Toc233891728)

[4.1 製品代替の登録 10](#_Toc233891729)

[4.2 製品除外の登録 11](#_Toc233891730)

## 目的

この文書では、SAP S/4HANA Cloud Public Editionシステムの製品代替および除外マスタデータを登録する方法について説明します。

製品代替は、ある製品を別の製品に置き換えるために使用される方法です。製品代替は、さまざまな理由で登録できます。以下に例を示します。

- 製品が在庫にない
- 製品は保証外である
- 代替製品の在庫が十分である

製品除外により、得意先は製品を代替とすることから除外できます。たとえば、打切製品に対して除外を登録することができます。

## 前提条件

このセクションでは、システム、ユーザ、マスタデータ、組織データ、その他テストデータ、およびビジネス条件に関するテストを実施するためのすべての前提条件がまとめられています。

### システムアクセス

| システム | 詳細 |
| --- | --- |
| システム | SAP Fiori ラウンチパッドからアクセスすることができます。各自のロールに割り当てられている各種アプリにアクセスするための URL がシステム管理者から提供されます。 |

### ロール

| 名称 (ロールテンプレート) | ID (ロールテンプレート) | 名称 (ラウンチパッド領域) | ID (ラウンチパッド領域) | ログオン |
| --- | --- | --- | --- | --- |
| マスタデータスペシャリスト - 製品データ | SAP_BR_PRODMASTER_SPECIALIST | マスタデータ - 製品/製品ガバナンス | SAP_BR_PRODMASTER_SPECIALIST / SAP_CMD_SPT_PR_GOV_PC |  |

### 必須の組織ユニット

組織構造には、会社の構造が反映されます。製品代替は、会社の組織ユニット (プラント) に依存する場合があります。組織ユニットに依存しない場合もあります。以下のテーブルは、関連する組織ユニットの概要を示しています。

| データセグメント | 依存対象 | 項目例 | コメント | 使用される組織ユニット |
| --- | --- | --- | --- | --- |
| 製品代替および製品除外 | プラント |  | プラントは製品代替/除外では必須ではありません。製品代替/除外はプラント制限なしで行うことができます。 | プラント:____________ |

### 必須のマスタデータ

製品代替データは製品マスタデータを参照します。テストスクリプトの必須マスタデータは、品目/製品を表します。以下のサンプルマスタデータに従って、独自のマスタデータを登録します。

| マスタデータオブジェクト | データセグメントでの使用 | 必須/任意 | コメント |
| --- | --- | --- | --- |
| 品目 | 製品代替の登録製品除外の登録 | 必須 | 製品代替または製品除外を登録するには、少なくとも 2 つの品目/製品マスタデータがシステムに存在する必要があります。 |

マスタデータオブジェクト登録の詳細については、[マスタデータスクリプト (MDS)](https://help.sap.com/docs/s4hana-best-practices/s4cld2608-master-data)を参照してください。

表 1: マスタデータスクリプトリファレンス

| MDS | テキスト |
| --- | --- |
| BNF | "商品" タイプの製品マスタの登録 - MDS |

### 予備ステップ

#### 製品代替理由の登録 (オプション)

テスト管理

カスタマプロジェクト: プロジェクト固有部分への入力

|  |  |  |  |
| --- | --- | --- | --- |
| テストケース ID | <X.XX> | テスト実施日: |  |
| テスト実施者名: |  | 期間: |  |
| ビジネスロール: |  | 責任者: | <都道府県/州、サービスプロバイダ、カスタマ/共同サービスプロバイダ、およびカスタマ> |

目的

以下の手順では、製品代替/除外の理由を登録する方法の指示を提供します。ユーザが使用できるアプリは、割り当てられたロールによって異なります。

手順

| テストステップ番号 | テストステップ名 | 指示 | 予想される結果 | コメント |
| --- | --- | --- | --- | --- |
| 1 | ログオンする | SAP Fiori ラウンチパッドにマスタデータスペシャリスト - 製品データとしてログオンします。 | SAP Fiori ラウンチパッドが表示されます。 |  |
| 2 | SAP Fiori アプリにアクセスする | 代替理由管理 - 製品 (F4789)を開きます。 | 代替理由管理 - 製品画面が表示されます。 |  |
| 3 | 登録を選択する | 代替理由管理 - 製品画面で、登録を選択します。 | 理由画面が表示されます。 |  |
| 4 | 理由を入力する | ヘッダセクションで、以下のエントリを入力します。理由: <新規代替理由コードを入力 (例: アップグレード)> |  |  |
| 5 | データを保存する | 登録を選択します。 | オブジェクトが保存されましたというシステムメッセージが表示されます。 |  |
| 6 | 登録を選択する | テキストセクションで、登録を選択します。 | 理由テキスト画面が表示されます。 |  |
| 7 | テキストデータを入力する | テキストセクションで、以下のエントリを入力します。言語キー: <理由に適用可能な言語キーを入力 (例: 英語の場合は EN)>理由テキスト: <理由について説明するテキストを入力 (例: アップグレード中の製品に適用可能)> |  |  |
| 8 | データを保存する | 登録を選択します。 | テキストが登録されましたというシステムメッセージが表示されます。 |  |

#### 代替グループの登録 (オプション)

テスト管理

カスタマプロジェクト: プロジェクト固有部分への入力

|  |  |  |  |
| --- | --- | --- | --- |
| テストケース ID | <X.XX> | テスト実施日: |  |
| テスト実施者名: |  | 期間: |  |
| ビジネスロール: |  | 責任者: | <都道府県/州、サービスプロバイダ、カスタマ/共同サービスプロバイダ、およびカスタマ> |

目的

以下の手順では、製品代替/除外のグループを登録するための指示を示します。ユーザが使用できるアプリは、割り当てられたロールによって異なります。

手順

| テストステップ番号 | テストステップ名 | 指示 | 予想される結果 | コメント |
| --- | --- | --- | --- | --- |
| 1 | ログオンする | SAP Fiori ラウンチパッドにマスタデータスペシャリスト - 製品データとしてログオンします。 | SAP Fiori ラウンチパッドが表示されます。 |  |
| 2 | SAP Fiori アプリにアクセスする | 代替グループ管理 - 製品 (F4788)を開きます。 | 代替グループ管理 - 製品画面が表示されます。 |  |
| 3 | 登録を選択する | 代替グループ管理 - 製品画面で登録を選択します。 | 代替グループ管理 - 製品登録画面が表示されます。 |  |
| 4 | グループを入力する | ヘッダセクションで、以下のエントリを入力します。グループ: <新規代替グループを入力 (例: STANDARD_DISPLAY)> |  |  |
| 5 | データを保存する | 登録を選択します。 | オブジェクトが保存されましたというシステムメッセージが表示されます。 |  |
| 6 | 登録を選択する | テキストセクションで、登録を選択します。 | グループテキスト登録画面が表示されます。 |  |
| 7 | テキストデータを入力する | テキストセクションで、以下のエントリを入力します。言語キー: <グループに適用可能な言語を入力 (例: EN 英語)>グループテキスト: <グループについて説明するテキストを入力 (例: すべての標準コンピュータディスプレイ)> |  |  |
| 8 | データを保存する | 登録を選択します。 | オブジェクトが保存されましたというシステムメッセージが表示されます。 |  |
| 9 | 前画面を選択する | 表題セクションで、< (前画面) を選択します。 | 代替グループ管理 - 製品画面が表示されます。 |  |
| 10 | グループデータを有効化する | 有効に設定を選択します。 | オブジェクトは有効ですというシステムメッセージが表示されます。 |  |

#### 代替管理の登録 (オプション)

テスト管理

カスタマプロジェクト: プロジェクト固有部分への入力

|  |  |  |  |
| --- | --- | --- | --- |
| テストケース ID | <X.XX> | テスト実施日: |  |
| テスト実施者名: |  | 期間: |  |
| ビジネスロール: |  | 責任者: | <都道府県/州、サービスプロバイダ、カスタマ/共同サービスプロバイダ、およびカスタマ> |

目的

以下の手順では、製品代替/除外グループの管理を登録するための指示を示します。ユーザが使用できるアプリは、割り当てられたロールによって異なります。

手順

| テストステップ番号 | テストステップ名 | 指示 | 予想される結果 | コメント |
| --- | --- | --- | --- | --- |
| 1 | ログオンする | SAP Fiori ラウンチパッドにマスタデータスペシャリスト - 製品データとしてログオンします。 | SAP Fiori ラウンチパッドが表示されます。 |  |
| 2 | SAP Fiori アプリにアクセスする | 代替管理の管理 - 製品 (F4787)を開きます。 | 代替管理の管理 - 製品画面が表示されます。 |  |
| 3 | 登録を選択する | 代替管理の管理 - 製品画面で、登録を選択します。 | 代替管理の管理 - 製品登録画面が表示されます。 |  |
| 4 | 管理を入力する | ヘッダセクションで、以下のエントリを入力します。管理: <新規代替管理を入力 (例: SALE)> |  |  |
| 5 | データを保存する | 登録を選択します。 | オブジェクトが保存されましたというシステムメッセージが表示されます。 |  |
| 6 | 登録を選択する | テキストセクションで、登録を選択します。 | 管理テキスト登録画面が表示されます。 |  |
| 7 | テキストデータを入力する | テキストセクションで、以下のエントリを入力します。言語キー: <管理に適用可能な言語を入力 (例: EN 英語)>管理テキスト: <管理について説明するテキストを入力 (例: 販売)> |  |  |
| 8 | データを保存する | 登録を選択します。 | オブジェクトが保存されましたというシステムメッセージが表示されます。 |  |
| 9 | 前画面を選択する | 表題セクションで、< (前画面) を選択します。 | 代替管理の管理 - 製品画面が表示されます。 |  |
| 10 | グループを割り当てる | 割当済グループセクションで、割当を選択します。 | 管理へのグループ割当ダイアログが表示されます。 |  |
| 11 | グループを選択する | 管理へのグループ割当ダイアログで、グループを検索して選択します。たとえば、グループとして <STANDARD_DISPLAY> を選択します。割当を選択します。 | オブジェクトが割り当てられましたというシステムメッセージが表示されます。 |  |

## 概要テーブル

このスコープアイテムは、以下のテーブルに示されているプロセスセグメントで構成されます。

|  |
| --- |
| 注記 システム管理者が SAP Fiori ラウンチパッドでスペースおよびページを有効化している場合、ホームページには、ビジネスロールの一般的なタスクを実行するために必要なアプリのみが含まれます。ホームページに含まれていないその他すべての (検索可能な) アプリは、検索バーを使用して見つけることができます ([2434549](https://me.sap.com/notes/2434549))。ホームページをパーソナライズして非表示のアプリを含める場合は、ユーザプロファイルにナビゲートし、アプリファインダを選択します。 |

| セグメント | ビジネスロール | アプリ/トランザクション | 予想される結果 |
| --- | --- | --- | --- |
| [製品代替の登録](#unique_11) [ ページ] 10 | マスタデータスペシャリスト - 製品データ | 代替管理 - 製品 (F4785) | 製品代替レコードが登録されます。 |
| [製品除外の登録](#unique_12) [ ページ] 11 | マスタデータスペシャリスト - 製品データ | 除外管理 - 製品 (F4786) | 製品除外レコードが登録されます。 |

## テスト手順

このセクションでは、このスコープアイテムに属する各プロセスステップのテスト手順について説明します。

### 製品代替の登録

テスト管理

カスタマプロジェクト: プロジェクト固有部分への入力

|  |  |  |  |
| --- | --- | --- | --- |
| テストケース ID | <X.XX> | テスト実施日: |  |
| テスト実施者名: |  | 期間: |  |
| ビジネスロール: |  | 責任者: | <都道府県/州、サービスプロバイダ、カスタマ/共同サービスプロバイダ、およびカスタマ> |

目的

以下の手順では、製品代替を登録するための指示を示します。ユーザが使用できるアプリは、割り当てられたロールによって異なります。

手順

| テストステップ番号 | テストステップ名 | 指示 | 予想される結果 | コメント |
| --- | --- | --- | --- | --- |
| 1 | ログオンする | SAP Fiori ラウンチパッドにマスタデータスペシャリスト - 製品データとしてログオンします。 | SAP Fiori ラウンチパッドが表示されます。 |  |
| 2 | SAP Fiori アプリにアクセスする | 代替管理 - 製品 (F4785)を開きます。 | 代替管理 - 製品画面が表示されます。 |  |
| 3 | 登録を選択する | 代替管理 - 製品ビューで、登録を選択します。 | フレキシブルな代替管理 - 製品列レイアウトが登録画面に表示されます。 |  |
| 4 | ヘッダデータを入力する | ヘッダセクションで、以下のエントリを入力します。製品: <代替が必要な製品を入力>代替製品: <代替を入力>プラント: <プラント番号>代替を登録するには、製品と代替製品データが必須です。 |  |  |
| 5 | 一般情報データを入力する | 一般情報セクションで、以下のエントリを入力します。理由: <代替を登録する理由を入力(例:アップグレード)>有効開始日付: <有効期間の開始日時を入力>有効終了日付: <有効期間の終了日時を入力>タイムゾーン: <有効期間に適用可能なタイムゾーンを入力>上記のエントリは任意です。 |  |  |
| 6 | データを保存する | 登録を選択します。 | オブジェクトが保存されましたというシステムメッセージが表示されます。 |  |
| 7 | 製品代替データを有効化する | 有効に設定を選択します。 | オブジェクトは有効ですというシステムメッセージが表示されます。 |  |

### 製品除外の登録

テスト管理

カスタマプロジェクト: プロジェクト固有部分への入力

|  |  |  |  |
| --- | --- | --- | --- |
| テストケース ID | <X.XX> | テスト実施日: |  |
| テスト実施者名: |  | 期間: |  |
| ビジネスロール: |  | 責任者: | <都道府県/州、サービスプロバイダ、カスタマ/共同サービスプロバイダ、およびカスタマ> |

目的

以下の手順では、製品例外を登録するための指示を示します。ユーザが使用できるアプリは、割り当てられたロールによって異なります。

手順

| テストステップ番号 | テストステップ名 | 指示 | 予想される結果 | コメント |
| --- | --- | --- | --- | --- |
| 1 | ログオンする | SAP Fiori ラウンチパッドにマスタデータスペシャリスト - 製品データとしてログオンします。 | SAP Fiori ラウンチパッドが表示されます。 |  |
| 2 | SAP Fiori アプリにアクセスする | 除外管理 - 製品 (F4786)を開きます。 | 除外管理 - 製品画面が表示されます。 |  |
| 3 | 登録を選択する | 除外管理 - 製品ビューで登録を選択します。 | 除外管理 - 製品登録画面が表示されます。 |  |
| 4 | ヘッダデータを入力する | ヘッダセクションで、以下のエントリを入力します。製品: <代替から除外する必要がある製品を入力>プラント: <プラント番号>除外を登録するには、製品が必須です。 |  |  |
| 5 | 一般情報データを入力する | 一般情報セクションで、以下のエントリを入力します。理由: <製品を除外する理由を入力>有効開始日付: <有効期間の開始日時を入力>有効終了日付: <有効期間の終了日時を入力>タイムゾーン: <有効期間に適用可能なタイムゾーンを入力>上記のエントリは任意です。 |  |  |
| 6 | データを保存する | 登録を選択します。 | オブジェクトが保存されましたというシステムメッセージが表示されます。 |  |
| 7 | 製品除外データを有効化する | 有効に設定を選択します。 | オブジェクトは有効ですというシステムメッセージが表示されます。 |  |

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
- related-to :: [[08-sales-order-management/creacion-de-sustitucion-de-producto-mds-4vo-420]]
- related-to :: [[08-sales-order-management/create-product-substitution-mds-4vo-419]]
- related-to :: [[08-sales-order-management/mds-4vo-423]]
- related-to :: [[08-sales-order-management/script-de-dados-mestre-criar-substituicao-de-produto-mds-4vo-422]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/4VO_S4CLD2608_Master_Data_JA_XX.docx` — full document · extracted with `mammoth` · 11,196 chars in the whole document
