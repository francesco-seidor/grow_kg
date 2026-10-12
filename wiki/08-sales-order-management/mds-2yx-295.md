---
id: 08-sales-order-management/mds-2yx-295
title: 得意先/品目情報レコード登録 - MDS (2YX) (2YX_S4CLD2608_Master_Data_JA_XX)
description: "SAP S/4HANA Cloud Public Edition 2608 マスタデータスクリプト (2YX): 得意先品目管理 (F2499) で得意先/品目情報レコードを登録する手順 (日本語)。"
cluster: 08-sales-order-management
tags: [kb/sales-order-management, topic/customer-material-info-records]
aliases: [2YX_S4CLD2608_Master_Data_JA_XX]
keywords: [Customer-Material Info Records, customer material info records, master data scripts, sales units of measure, sales organization, distribution channel, business roles, 2YX]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/2YX_S4CLD2608_Master_Data_JA_XX.docx]
confidence: high
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-295
topic: 08-sales-order-management/customer-material-info-records
language: JA
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# 得意先/品目情報レコード登録 - MDS (2YX) (2YX_S4CLD2608_Master_Data_JA_XX)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/2YX_S4CLD2608_Master_Data_JA_XX.docx`, extracted with `mammoth`. Grouped under **Customer-Material Info Records** in Sales Order Management. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

| <!-- image omitted: unnamed --> | マスタデータスクリプトSAP S/4HANA Cloud Public Edition - 02-07-26 |
| --- | --- |
|  | 得意先/品目情報レコード登録 - MDS (2YX) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

目次

[1 目的 2](#_Toc233891529)

[2 前提条件 3](#_Toc233891530)

[2.1 システムアクセス 3](#_Toc233891531)

[2.2 ロール 3](#_Toc233891532)

[2.3 必須マスタデータおよび任意マスタデータ 3](#_Toc233891533)

[2.4 必須マスタデータおよび任意マスタデータ 4](#_Toc233891534)

[3 概要テーブル 5](#_Toc233891535)

[4 テスト手順 6](#_Toc233891536)

[4.1 得意先品目情報の登録 6](#_Toc233891537)

## 目的

この文書では、SAP S/4HANA Cloud Public Editionシステムに得意先/品目情報を登録する方法について説明します。説明には、SAP S/4HANA Cloud Public Editionアプライアンスに関連するデータセグメントも含まれます。SAP S/4HANA Cloud Public Editionコンテンツの範囲に関連しない項目については、この文書では説明していません。

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
| 社内営業業務担当 | SAP_BR_INTERNAL_SALES_REP | 内部販売/得意先販売/請求 | SAP_BR_INTERNAL_SALES_REP / SAP_SD_SPT_RETURNS_INT_SALES_PC / SAP_SD_SPT_BILLING_INT_SALES_PC |  |

### 必須マスタデータおよび任意マスタデータ

| マスタデータオブジェクト | データセグメントでの使用 | 必須/任意 | コメント |
| --- | --- | --- | --- |
| 得意先 | 第一画面 | 必須 |  |
| 販売組織 | 第一画面 | 必須 |  |
| 流通チャネル | 第一画面 | 必須 |  |
| 品目 | 第一画面 | 任意 |  |

### 必須マスタデータおよび任意マスタデータ

このセクションでは、マスタレコードの動作に影響し、価格設定条件の登録に必ず必要となる基本パラメータの一部を確認することができます。

販売組織: <販売組織>

流通チャネル: <流通チャネル>

得意先: <得意先>

品目: <品目コード>

## 概要テーブル

このスコープアイテムは、以下の表に示されている複数のプロセスステップで構成されます。

|  |
| --- |
| 注記 システム管理者が SAP Fiori ラウンチパッドでスペースおよびページを有効化している場合、ホームページには、ビジネスロールの一般的なタスクを実行するために必要なアプリのみが含まれます。ホームページに含まれていないその他すべての (検索可能な) アプリは、検索バーを使用して見つけることができます ([2434549](https://me.sap.com/notes/2434549))。ホームページをパーソナライズして非表示のアプリを含める場合は、ユーザプロファイルにナビゲートし、アプリファインダを選択します。 |

| プロセスステップ | ビジネスロール | SAP Fiori アプリ/トランザクション | 予想される結果 |
| --- | --- | --- | --- |
| [得意先品目情報の登録](#unique_8) [ ページ] 6 | 社内営業業務担当 | 得意先品目管理 (F2499) | 得意先/品目情報レコードが登録されます。 |

## テスト手順

このセクションでは、このスコープアイテムに属する各プロセスステップのテスト手順について説明します。

### 得意先品目情報の登録

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
| 1 | ログオン | SAP Fiori ラウンチパッドに社内営業業務担当としてログオンします。 | SAP Fiori ラウンチパッドが表示されます。 |  |
| 2 | SAP Fiori アプリにアクセスする | 得意先品目管理 (F2499)を開きます。 | アプリが開きます。 |  |
| 3 | 得意先品目登録にアクセスする | 登録を選択します。 | 得意先品目画面が表示されます。 |  |
| 4 | 基本得意先品目情報を入力する | 以下のエントリを入力します。得意先: <得意先>製品: <品目コード>販売組織: <販売組織>流通チャネル: <流通チャネル>得意先品目テキスト: 得意先と品目に関するテキストを入力します。 | 基本得意先品目情報が更新されます。 |  |
| 5 | 販売単位を入力する | 単位変換セクションで、以下のエントリを入力します。1 PAL (得意先単位): 2 個 (基本単位) | 得意先/品目の組合せの販売単位が更新されます。注記この画面で販売単位および変換を更新するには、数量単位と変換の品目マスタデータを更新する必要があります。ほかのマスタデータスクリプト (商品の"商品" タイプの製品マスタの登録 - MDS - BNFなど) を参照できます。この画面で販売単位が更新されたら、それが販売伝票に表示されます。 |  |
| 6 | 登録を選択する | 登録を選択します。 | 得意先品目が正常に登録されます。 |  |

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
- related-to :: [[08-sales-order-management/crear-registro-info-para-cliente-y-material-mds-2yx-294]]
- related-to :: [[08-sales-order-management/create-customer-material-info-record-mds-2yx-293]]
- related-to :: [[08-sales-order-management/criar-registro-info-de-material-do-cliente-mds-2yx-296]]
- related-to :: [[08-sales-order-management/kundenmaterial-infosatz-anlegen-sds-2yx-292]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/2YX_S4CLD2608_Master_Data_JA_XX.docx` — full document · extracted with `mammoth` · 6,097 chars in the whole document
