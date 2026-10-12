---
id: 13-quality-ehs-and-compliance/ehs-mds-3sr-361
title: EHS ロケーション登録 - MDS (3SR) (3SR_S4CLD2608_Master_Data_JA_XX)
description: Japanese master data script (MDS 3SR) for creating EHS locations in a location structure via EHFND_UI_LOC_ENTRY in SAP S/4HANA Cloud Public Edition 2608.
cluster: 13-quality-ehs-and-compliance
tags: [kb/quality-ehs-and-compliance, topic/ehs-locations]
aliases: [3SR_S4CLD2608_Master_Data_JA_XX]
keywords: [EHS Locations, ehs location, location structure, master data script, business roles, location responsibles, location activation, 3SR]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/3SR_S4CLD2608_Master_Data_JA_XX.docx]
confidence: high
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-361
topic: 13-quality-ehs-and-compliance/ehs-locations
language: JA
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# EHS ロケーション登録 - MDS (3SR) (3SR_S4CLD2608_Master_Data_JA_XX)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/3SR_S4CLD2608_Master_Data_JA_XX.docx`, extracted with `mammoth`. Grouped under **EHS Locations** in Quality, EHS and Compliance. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

| <!-- image omitted: unnamed --> | マスタデータスクリプトSAP S/4HANA Cloud Public Edition - 02-07-26 |
| --- | --- |
|  | EHS ロケーション登録 - MDS (3SR) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

目次

[1 目的 2](#_Toc233891592)

[2 前提条件 3](#_Toc233891593)

[2.1 システムアクセス 3](#_Toc233891594)

[2.2 ロール 3](#_Toc233891595)

[3 概要テーブル 4](#_Toc233891596)

[4 手順 5](#_Toc233891597)

[4.1 EHS ロケーションマスタデータの登録 - 一般データ 5](#_Toc233891598)

## 目的

この文書は、ロケーション構造内に EHS ロケーションを登録するのに役立ちます。EHS ロケーションは、環境、安全、衛生で使用される共通マスタデータオブジェクトです。ロケーション構造に編成された EHS ロケーションの登録はソリューションの初期設定の一部であり、ロケーションはソリューションの一部である後続の処理で使用されます。

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
| 産業衛生士 (インシデント管理者) | SAP_BR_INDUSTRIAL_HYGIENIST | 職場安全 | SAP_BR_INDUSTRIAL_HYGIENIST |  |
| 環境管理者 | SAP_BR_EHS_ENV_MGMT | 環境管理 | SAP_BR_EHS_ENV_MGMT |  |
| 変更管理コーディネータ | SAP_BR_CHG_MGMT_COORDINATOR | 変更の管理 | SAP_BR_CHG_MGMT_COORDINATOR |  |

## 概要テーブル

このマスタレコードは、以下の表に示されている複数のセグメントで構成されます。

|  |
| --- |
| 注記 システム管理者が SAP Fiori ラウンチパッドでスペースおよびページを有効化している場合、ホームページには、ビジネスロールの一般的なタスクを実行するために必要なアプリのみが含まれます。ホームページに含まれていないその他すべての (検索可能な) アプリは、検索バーを使用して見つけることができます ([2434549](https://me.sap.com/notes/2434549))。ホームページをパーソナライズして非表示のアプリを含める場合は、ユーザプロファイルにナビゲートし、アプリファインダを選択します。 |

| セグメント | ビジネスロール | トランザクション/アプリ | 予想される結果 |
| --- | --- | --- | --- |
| [EHS ロケーションマスタデータの登録 - 一般データ](#unique_6) [ ページ] 5 | 産業衛生士環境管理者変更管理コーディネータ | ロケーション管理(EHFND_UI_LOC_ENTRY) | EHS ロケーションが登録され、EHS ロケーション構造に割り当てられます。 |

## 手順

このセクションでは、このスコープアイテムに属する各プロセスステップのテスト手順について説明します。

### EHS ロケーションマスタデータの登録 - 一般データ

目的

以下の手順は、EHS ロケーションを登録して EHS ロケーション構造に割り当てる処理に関する指示です。

手順

| テストステップ番号 | テストステップ名 | 指示 | 予想される結果 | 合格/不合格/コメント |
| --- | --- | --- | --- | --- |
| 1. | ログオンする | 以下のいずれかのロールを使用して、SAP Fiori ラウンチパッドにログオンします。産業衛生士環境管理者変更管理コーディネータ | 各ロールのセクションおよびタイルが含まれる SAP Fiori ラウンチパッドが表示されます。 |  |
| 2 | ロケーション構造にナビゲートする | ロケーション管理(EHFND_UI_LOC_ENTRY)を開きます。 | ロケーション画面が表示されます。ロケーション構造は、最上位レベルとしてすべてのロケーションが初期設定されています。 |  |
| 3 | ロケーションを登録する | ロケーション構造の編集を選択します。ロケーション構造画面:すべてのロケーションの行を選択します。新規を選択します。ロケーション登録画面:ロケーション項目に <ロケーション名> を入力します。ロケーションタイプ項目の入力ヘルプを使用して、<ロケーションタイプ> を選択します。改訂開始日付項目に日付2000/01/01を入力します。保存を選択します。ロケーション構造に戻るを選択します。ロケーション構造画面:エントリを保存します。 | 名称<ロケーション名>のロケーションが登録され、ロケーション構造に保存されます。 |  |
| 4 | ロケーションを編集する | ロケーション構造画面:名称列で、<ロケーション名> リンクを選択します。 | ロケーションの編集アプリが表示されます。 |  |
| 5 | 基本情報を追加する | ロケーション: <ロケーション名>画面で、基本情報タブ内:テキスト項目に <ロケーションテキスト> を追加します。ロケーション項目の横にある翻訳を選択します。別の言語の翻訳済テキストを追加します。テキスト項目の横にある翻訳を選択します。別の言語の翻訳済テキストを追加します。ロケーションの画像を追加する場合は、イメージアップロードを選択します。エントリを保存します。 | ロケーションのデータが保存されます。 |  |
| 6 | 住所を追加する | ロケーション: <ロケーション名>画面で、住所タブ内:名称行 1項目に<名称行 1>を入力します。名称行 2項目に<名称行 2>を入力します。地名項目に <地名> を入力します。郵便番号項目に <郵便番号> を入力します。市区町村項目に <市区町村名> を入力します。入力ヘルプを使用して国/地域項目で <国/地域> を選択します。入力ヘルプを使用して地域項目で <地域> を選択します。タイムゾーン項目はデフォルトのUTC値のままにしておきます。電話番号、FAX 番号、緯度、経度、および立面図の各項目に追加データを入力します。エントリを保存します。 | ロケーションのデータが保存されます。 |  |
| 7 | 責任者を追加する | このステップは、以下のロールのみに関連します。SAP_BR_INDUSTRIAL_HYGIENIST (産業衛生士)SAP_BR_EHS_ENV_MGMT (環境管理者)ロケーション: <ロケーション名> 画面で、責任者タブ内:ロール別責任者テーブルで、入力ヘルプを使用して名前列で <ユーザ名> を選択します。ロール列で、ドロップダウンリストからインシデント管理者または環境管理者を選択します。エントリを保存します。 | ロケーションのデータが保存されます。 |  |
| 8 | 文書を追加する | ロケーション: <ロケーション名> 画面で、文書タブ内:文書およびリンクテーブルで、ファイル追加を選択してロケーションの文書を追加します。エントリを保存します。 | 選択した文書がテーブルに追加されます。ロケーションのデータが保存されます。 |  |
|  | ロケーションを有効化する | ロケーション: <ロケーション名> 画面:ページヘッダでステータス設定を選択します。有効オプションを選択します。 | ロケーションが有効化されます。ページヘッダのステータス項目が有効に設定されます。ロケーションのデータが保存されます。 |  |

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
- related-to :: [[13-quality-ehs-and-compliance/create-ehs-location-mds-3sr-359]]
- related-to :: [[13-quality-ehs-and-compliance/ehs-lokation-anlegen-sds-3sr-358]]
- related-to :: [[13-quality-ehs-and-compliance/ehs-mds-3sr-363]]
- related-to :: [[13-quality-ehs-and-compliance/script-de-dados-mestre-criar-local-ehs-mds-3sr-362]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/3SR_S4CLD2608_Master_Data_JA_XX.docx` — full document · extracted with `mammoth` · 6,715 chars in the whole document
