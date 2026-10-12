---
id: 08-sales-order-management/mds-5nh-481
title: "マスタデータスクリプト: オブジェクトおよび値決定 - MDS (5NH) (5NH_S4CLD2608_Master_Data_JA_XX)"
description: "Japanese master data/test script (5NH) for substitution: characteristic combinations (F5303), searches (F5302) and optional product/plant/storage location controls in S/4HANA Cloud 2608."
cluster: 08-sales-order-management
tags: [kb/sales-order-management, topic/product-and-location-substitution]
aliases: [5NH_S4CLD2608_Master_Data_JA_XX]
keywords: ["Product, Plant and Storage Location Substitution", product substitution, characteristic combinations, substitution searches, substitution controls, advanced atp, plant substitution, storage location substitution, business roles, order fulfillment]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/5NH_S4CLD2608_Master_Data_JA_XX.docx]
confidence: low
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-481
topic: 08-sales-order-management/product-and-location-substitution
language: JA
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# マスタデータスクリプト: オブジェクトおよび値決定 - MDS (5NH) (5NH_S4CLD2608_Master_Data_JA_XX)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/5NH_S4CLD2608_Master_Data_JA_XX.docx`, extracted with `mammoth`. Grouped under **Product, Plant and Storage Location Substitution** in Sales Order Management. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

| <!-- image omitted: unnamed --> | マスタデータスクリプトSAP S/4HANA Cloud Public Edition - 02-07-26 |
| --- | --- |
|  | オブジェクトおよび値決定 - MDS (5NH) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

目次

[1 目的 2](#_Toc233891764)

[2 前提条件 3](#_Toc233891765)

[2.1 システムアクセス 3](#_Toc233891766)

[2.2 ロール 3](#_Toc233891767)

[2.3 必須の組織ユニット 3](#_Toc233891768)

[2.4 必須のマスタデータ 4](#_Toc233891769)

[2.5 予備ステップ 4](#_Toc233891770)

[2.5.1 製品代替管理の登録 (オプション) 4](#_Toc233891771)

[2.5.2 プラント代替管理の登録 (オプション) 6](#_Toc233891772)

[2.5.3 保管場所代替管理の登録 (オプション) 7](#_Toc233891773)

[3 概要テーブル 10](#_Toc233891774)

[4 テスト手順 11](#_Toc233891775)

[4.1 特性組合せ登録 11](#_Toc233891776)

[4.2 検索登録 12](#_Toc233891777)

## 目的

この文書では、SAP S/4HANA Cloud Public Editionシステムに対して組合せと、組合せマスタデータのアクセス (特性値あり) を登録する方法を説明します。

オブジェクトおよび値決定では、特性を設定して、利用可能在庫確認の際に受注の製品/プラント/保管場所を代替するために使用される管理を決定することができます。

これにより、マスタデータ代替と AATP 機能の代替ベース確認 (ABC) の統合が可能となります。

## 前提条件

このセクションでは、システム、ユーザ、マスタデータ、組織データ、その他テストデータ、およびビジネス条件に関するテストを実施するためのすべての前提条件がまとめられています。

### システムアクセス

| システム | 詳細 |
| --- | --- |
| システム | SAP Fiori ラウンチパッドからアクセスすることができます。各自のロールに割り当てられている各種アプリにアクセスするための URL がシステム管理者から提供されます。 |

### ロール

| 名称 (ロールテンプレート) | ID (ロールテンプレート) | 名称 (ラウンチパッド領域) | ID (ラウンチパッド領域) | ログオン |
| --- | --- | --- | --- | --- |
| オーダーフルフィルメントマネージャ | SAP_BR_ORDER_FULFILLMNT_MNGR | オーダーフルフィルメント管理 | SAP_BR_ORDER_FULFILLMNT_MNGR |  |
| マスタデータスペシャリスト - 製品データ | SAP_BR_PRODMASTER_SPECIALIST | マスタデータ - 製品/製品ガバナンス | SAP_BR_PRODMASTER_SPECIALIST / SAP_CMD_SPT_PR_GOV_PC |  |

### 必須の組織ユニット

特定の組織データは必要ありません。

| データセグメント | 依存対象 | 項目例 | コメント | 使用される組織ユニット |
| --- | --- | --- | --- | --- |
|  |  |  |  |  |

### 必須のマスタデータ

特定のマスタデータは必要ありません。

| マスタデータオブジェクト | データセグメントでの使用 | 必須/任意 | コメント |
| --- | --- | --- | --- |
|  |  |  |  |

マスタデータオブジェクト登録の詳細については、表 1: マスタデータスクリプトリファレンスを参照してください。

| MDS | テキスト |
| --- | --- |
|  |  |

### 予備ステップ

#### 製品代替管理の登録 (オプション)

テスト管理

カスタマプロジェクト: プロジェクト固有部分への入力

|  |  |  |  |
| --- | --- | --- | --- |
| テストケース ID | <X.XX> | テスト実施日: |  |
| テスト実施者名: |  | 期間: |  |
| ビジネスロール: |  | 責任者: | <都道府県/州、サービスプロバイダ、カスタマ/共同サービスプロバイダ、およびカスタマ> |

目的

以下の手順では、製品代替/除外グループの管理の登録に関する指示を示します。ユーザが使用できるアプリは、割り当てられたロールによって異なります。

手順

| テストステップ番号 | テストステップ名 | 指示 | 予想される結果 | コメント |
| --- | --- | --- | --- | --- |
| 1 | ログオンする | SAP Fiori ラウンチパッドにマスタデータスペシャリスト - 製品データとしてログオンします。 | SAP Fiori ラウンチパッドが表示されます。 |  |
| 2 | SAP Fiori アプリにアクセスする | 代替管理の管理 - 製品 (F4787)を開きます。 | アプリが開きます。 |  |
| 3 | 登録を選択する | 代替管理の管理 - 製品画面で、登録を選択します。 | 代替管理の管理 - 製品登録画面が表示されます。 |  |
| 4 | 管理を入力する | ヘッダセクションで、以下のエントリを入力します。管理: <新規代替管理を入力 (例: SALE)> |  |  |
| 5 | 登録を選択する | 登録を選択します。 | 管理が登録されましたというシステムメッセージが表示されます。 |  |
| 6 | テキストを登録する | テキストセクションで、登録を選択します。 | 管理テキスト登録画面が表示されます。 |  |
| 7 | テキストデータを入力する | テキストセクションで、以下のエントリを入力します。言語キー: <管理に適用可能な言語を入力 (例: 英語の場合は EN)>管理テキスト: <管理について説明するテキストを入力 (例: 販売)> |  |  |
| 8 | 登録を選択する | 登録を選択します。 | 管理テキストが登録されましたというシステムメッセージが表示されます。 |  |
| 9 | 前画面を選択する | 表題セクションで、< (前画面) を選択します。 | 代替管理の管理 - 製品画面が表示されます。 |  |
| 10 | グループを割り当てる | 割当済グループセクションで、割当を選択します。 | 管理へのグループ割当ダイアログボックスが表示されます。 |  |
| 11 | グループを選択する | 管理へのグループ割当ダイアログボックスで、グループを検索して選択します。たとえば、STANDARD_DISPLAYグループを選択します。注記 利用可能な既存のグループが表示されない場合は、最初にマスタデータスクリプト製品代替の登録 - MDS-4VOのプロセスステップ代替グループの登録 (オプション)を実行することができます。割当を選択します。 | オブジェクトが割り当てられましたというシステムメッセージが表示されます。 |  |

#### プラント代替管理の登録 (オプション)

テスト管理

カスタマプロジェクト: プロジェクト固有部分への入力

|  |  |  |  |
| --- | --- | --- | --- |
| テストケース ID | <X.XX> | テスト実施日: |  |
| テスト実施者名: |  | 期間: |  |
| ビジネスロール: |  | 責任者: | <都道府県/州、サービスプロバイダ、カスタマ/共同サービスプロバイダ、およびカスタマ> |

目的

以下の手順では、保管場所代替/除外管理の管理に関する指示を示します。ユーザが使用できるアプリは、割り当てられたロールによって異なります。

手順

| テストステップ番号 | テストステップ名 | 指示 | 予想される結果 | コメント |
| --- | --- | --- | --- | --- |
| 1 | ログオンする | SAP Fiori ラウンチパッドにオーダーフルフィルメントマネージャとしてログオンします。 | SAP Fiori ラウンチパッドが表示されます。 |  |
| 2 | SAP Fiori アプリにアクセスする | 代替管理の管理 - ロケーション (F5312)を開きます。 | アプリが開きます。 |  |
| 3 | 登録を選択する | 代替管理の管理 - ロケーション画面で、登録を選択します。 | 代替管理の管理 - ロケーション登録画面が表示されます。 |  |
| 4 | 管理を入力する | ヘッダセクションで、以下のエントリを入力します。ロケーションタイプ: <プラント>管理: <新規代替管理を入力 (例: REGION)> |  |  |
| 5 | データを保存する | 保存を選択します。 | 管理が登録されましたというシステムメッセージが表示されます。 |  |
| 6 | 登録を選択する | テキストセクションで、登録を選択します。 | 管理テキスト登録画面が表示されます。 |  |
| 7 | テキストデータを入力する | テキストセクションで、以下のエントリを入力します。言語キー: <管理に適用可能な言語キーを入力 (例: 英語の場合は EN)>管理テキスト: <管理について説明するテキストを入力 (例: 地域の管理)> |  |  |
| 8 | データを保存する | 登録を選択します。 | 管理テキストが登録されましたというシステムメッセージが表示されます。 |  |
| 9 | 前画面を選択する | 表題セクションで、< (前画面) を選択します。 | 代替管理の管理 - ロケーション画面が表示されます。 |  |
| 10 | グループを割り当てる | 割当済グループセクションで、割当を選択します。 | 管理へのグループ割当ダイアログボックスが表示されます。 |  |
| 11 | グループを選択する | 管理へのグループ割当ダイアログボックスで、グループを検索して選択します。たとえば、<SOUTH_REGION>グループを選択します。注記 利用可能な既存のグループが表示されない場合は、最初にマスタデータスクリプトロケーション代替および除外の登録 - MDS-5NGのプロセスステッププラント代替グループの登録 (オプション)を実行することができます。割当を選択します。 | グループが割り当てられましたというシステムメッセージが表示されます。 |  |

#### 保管場所代替管理の登録 (オプション)

テスト管理

カスタマプロジェクト: プロジェクト固有部分への入力

|  |  |  |  |
| --- | --- | --- | --- |
| テストケース ID | <X.XX> | テスト実施日: |  |
| テスト実施者名: |  | 期間: |  |
| ビジネスロール: |  | 責任者: | <都道府県/州、サービスプロバイダ、カスタマ/共同サービスプロバイダ、およびカスタマ> |

目的

以下の手順では、保管場所代替/除外管理の管理に関する指示を示します。ユーザが使用できるアプリは、割り当てられたロールによって異なります。

手順

| テストステップ番号 | テストステップ名 | 指示 | 予想される結果 | コメント |
| --- | --- | --- | --- | --- |
| 1 | ログオンする | SAP Fiori ラウンチパッドにオーダーフルフィルメントマネージャとしてログオンします。 | SAP Fiori ラウンチパッドが表示されます。 |  |
| 2 | SAP Fiori アプリにアクセスする | 代替管理の管理 - ロケーション (F5312)を開きます。 | アプリが開きます。 |  |
| 3 | 登録を選択する | 代替管理の管理 - ロケーション画面で、登録を選択します。 | 代替管理の管理 - ロケーション登録画面が表示されます。 |  |
| 4 | 管理を入力する | ヘッダセクションで、以下のエントリを入力します。ロケーションタイプ: <保管場所>管理: <新規代替管理を入力 (例: STORAGE_TYPE)> |  |  |
| 5 | 登録を選択する | 登録を選択します。 | 管理が登録されましたというシステムメッセージが表示されます。 |  |
| 6 | 登録を選択する | テキストセクションで、登録を選択します。 | 管理テキスト登録画面が表示されます。 |  |
| 7 | テキストデータを入力する | テキストセクションで、以下のエントリを入力します。言語キー: <管理に適用可能な言語キーを入力 (例: 英語の場合は EN)>管理テキスト: <管理について説明するテキストを入力 (例: 保管タイプの管理)> |  |  |
| 8 | データを保存する | 登録を選択します。 | 管理テキストが登録されましたというシステムメッセージが表示されます。 |  |
| 9 | 前画面を選択する | 表題セクションで、< (前画面) を選択します。 | 代替管理の管理 - ロケーション画面が表示されます。 |  |
| 10 | グループを割り当てる | 割当済グループセクションで、割当を選択します。 | 管理へのグループ割当ダイアログボックスが表示されます。 |  |
| 11 | グループを選択する | 管理へのグループ割当ダイアログボックスで、グループを検索して選択します。たとえば、<COLD_STORAGE>グループを選択します。注記 利用可能な既存のグループが表示されない場合は、最初にマスタデータスクリプトロケーション代替および除外の登録 - MDS-5NGのプロセスステップ保管場所代替グループの登録 (オプション)を実行することができます。割当を選択します。 | グループが割り当てられましたというシステムメッセージが表示されます。 |  |

## 概要テーブル

このスコープアイテムは、以下のテーブルに示されているプロセスセグメントで構成されます。

|  |
| --- |
| 注記 システム管理者が SAP Fiori ラウンチパッドでスペースおよびページを有効化している場合、ホームページには、ビジネスロールの一般的なタスクを実行するために必要なアプリのみが含まれます。ホームページに含まれていないその他すべての (検索可能な) アプリは、検索バーを使用して見つけることができます ([2434549](https://me.sap.com/notes/2434549))。ホームページをパーソナライズして非表示のアプリを含める場合は、ユーザプロファイルにナビゲートし、アプリファインダを選択します。 |

| セグメント | ビジネスロール | アプリ/トランザクション | 予想される結果 |
| --- | --- | --- | --- |
| [特性組合せ登録](#unique_11) [ ページ] 11 | オーダーフルフィルメントマネージャ | 特性組合せ管理 (F5303)。 | 特性組合せが登録されます。 |
| [検索登録](#unique_12) [ ページ] 12 | オーダーフルフィルメントマネージャ | 検索順序管理 - 代替 (F5302) | 上記のセグメントで登録された組合せに対してアクセスが登録され、アクセスに対して特性値が定義されます。 |

## テスト手順

このセクションでは、このスコープアイテムに属する各プロセスステップのテスト手順について説明します。

### 特性組合せ登録

テスト管理

カスタマプロジェクト: プロジェクト固有部分への入力

|  |  |  |  |
| --- | --- | --- | --- |
| テストケース ID | <X.XX> | テスト実施日: |  |
| テスト実施者名: |  | 期間: |  |
| ビジネスロール: |  | 責任者: | <都道府県/州、サービスプロバイダ、カスタマ/共同サービスプロバイダ、およびカスタマ> |

目的

以下の手順は、特性組合わせの登録に関する指示です。ユーザが使用できるアプリは、割り当てられたロールによって異なります。

手順

| テストステップ番号 | テストステップ名 | 指示 | 予想される結果 | コメント |
| --- | --- | --- | --- | --- |
| 1 | ログオンする | SAP Fiori ラウンチパッドにオーダーフルフィルメントマネージャとしてログオンします。 | SAP Fiori ラウンチパッドが表示されます。 |  |
| 2 | SAP Fiori アプリにアクセスする | 特性組合せ管理 (F5303)を開きます。 | アプリが開きます。 |  |
| 3 | 登録を選択する | 特性組合せ管理画面で、登録を選択します。 | 特性組合せ管理登録画面が表示されます。 |  |
| 4 | ヘッダデータを入力する | ヘッダセクションで、以下のエントリを入力します。組合せ: <組合せ名を入力>組合せテキスト: <組合せのテキストを入力>用途: 代替カタログタイプ: <用途 SUBSTN の基本 (販売伝票)>代替を登録するには、組合せ、用途、およびカタログタイプは必須です。 |  |  |
| 5 | 特性を割り当てる | 特性セクションで、以下のエントリを入力して特性を割り当てます。割当を選択します。画面で特性を選択します。画面で割当を選択します。上矢印または下矢印を使用して特性の順序を設定します。 |  |  |
| 6 | 登録を選択する | 登録を選択します。 | 組合せが登録されますというシステムメッセージが表示されます。 |  |

### 検索登録

テスト管理

カスタマプロジェクト: プロジェクト固有部分への入力

|  |  |  |  |
| --- | --- | --- | --- |
| テストケース ID | <X.XX> | テスト実施日: |  |
| テスト実施者名: |  | 期間: |  |
| ビジネスロール: |  | 責任者: | <都道府県/州、サービスプロバイダ、カスタマ/共同サービスプロバイダ、およびカスタマ> |

目的

以下の手順は、組合せに対する検索を登録し、その検索に CVC 値を定義する指示です。ユーザが使用できるアプリは、割り当てられたロールによって異なります。

手順

| テストステップ番号 | テストステップ名 | 指示 | 予想される結果 | コメント |
| --- | --- | --- | --- | --- |
| 1 | ログオンする | SAP Fiori ラウンチパッドにオーダーフルフィルメントマネージャとしてログオンします。 | SAP Fiori ラウンチパッドが表示されます。 |  |
| 2 | SAP Fiori アプリにアクセスする | 検索順序管理 - 代替 (F5302)を開きます。 | 検索順序管理 - 代替画面が表示されます。 |  |
| 3 | 登録を選択する | 検索順序管理 - 代替ビューの製品タブで、登録を選択します (3 つのタブ製品、プラント、および保管場所を使用できます)。 | 検索順序管理 - 代替の登録画面が表示されます。 |  |
| 4 | 詳細を入力する | ポップアップウィンドウで、以下のエントリを入力します。組合せ: <入力ヘルプから組合せを選択>ステータス: <ドロップダウンから必要なステータスを選択> ステータス項目はデフォルトで有効ステータスに設定されます。登録を選択します。検索を登録するには、組合せが必須です。 | 検索が登録されたことを示すシステムメッセージが表示されます。 |  |
| 5 | 割当済管理の詳細を入力する | 割当済管理セクションで、特性および管理詳細を追加します。追加を選択します。特性: <特性値を入力するか、入力ヘルプから選択>ステータス: <ステータスはデフォルトで有効>代替実行: <デフォルトで有効>管理: <オプション - 製品代替管理を入力>必要に応じて複数の値を追加します。 | 割当済管理セクションに表示される特性列は、検索の登録時に選択された組合せに割り当てられた列です。 |  |
| 6 | 検索を登録する | 登録を選択します。 | アクセス登録済を示すシステムメッセージが表示されます。 |  |

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

## Suspected conflicts

> [!warning] Conflict
> Flagged while digesting this document, not verified: The plant substitution control section's purpose text refers to storage location substitution/exclusion controls rather than plant, an internal inconsistency.

## Connections
- part-of :: [[_cluster]]
- related-to :: [[08-sales-order-management/5nh-483]]
- related-to :: [[08-sales-order-management/crear-determinacion-de-objeto-y-valor-mds-5nh-480]]
- related-to :: [[08-sales-order-management/create-object-and-value-determination-mds-5nh-479]]
- related-to :: [[08-sales-order-management/criar-determinacao-de-objeto-e-valor-mds-5nh-482]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/5NH_S4CLD2608_Master_Data_JA_XX.docx` — full document · extracted with `mammoth` · 11,582 chars in the whole document
