---
id: 08-sales-order-management/mds-bet-541
title: 販売価格設定条件の登録 - MDS (BET) (BET_S4CLD2608_Master_Data_JA_XX)
description: マスタデータスクリプト（日本語）：VK12 で販売価格設定条件（PPR0 など）を登録する手順。
cluster: 08-sales-order-management
tags: [kb/sales-order-management, topic/sales-pricing-conditions]
aliases: [BET_S4CLD2608_Master_Data_JA_XX]
keywords: [Sales Price Conditions and Statistical Conditions, sales pricing conditions, condition records, condition type, sample data, business roles, master data scripts, BET]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/BET_S4CLD2608_Master_Data_JA_XX.docx]
confidence: high
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-541
topic: 08-sales-order-management/sales-pricing-conditions
language: JA
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# 販売価格設定条件の登録 - MDS (BET) (BET_S4CLD2608_Master_Data_JA_XX)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/BET_S4CLD2608_Master_Data_JA_XX.docx`, extracted with `mammoth`. Grouped under **Sales Price Conditions and Statistical Conditions** in Sales Order Management. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

| <!-- image omitted: unnamed --> | マスタデータスクリプトSAP S/4HANA Cloud Public Edition - 02-07-26 |
| --- | --- |
|  | 販売価格設定条件の登録 - MDS (BET) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

目次

[1 目的 2](#_Toc233891817)

[2 前提条件 3](#_Toc233891818)

[2.1 システムアクセス 3](#_Toc233891819)

[2.2 ロール 3](#_Toc233891820)

[2.3 必須マスタデータおよび任意マスタデータ 3](#_Toc233891821)

[3 概要テーブル 5](#_Toc233891822)

[4 テスト手順 6](#_Toc233891823)

[4.1 価格設定条件の登録 6](#_Toc233891824)

## 目的

販売価格設定条件は、受注の自動価格設定の実行に必要な情報を格納するために使用されます。条件には、価格、値引、追加料金、税などがあります。これらの条件は、特定の得意先や品目、またはパラメータの組合せに固有の場合があります。

販売価格設定条件には、ある品目の特定の通貨での価格や、パーセントでの得意先固有の割引などの情報が含まれます。この情報は、受注および請求書などの請求伝票で使用され、保管されます。

一般にこの情報は、組織内の特定の販売単位に固有です。

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
| 価格設定スペシャリスト | SAP_BR_PRICING_SPECIALIST | 価格管理 | SAP_BR_PRICING_SPECIALIST |  |

### 必須マスタデータおよび任意マスタデータ

以下の表は、価格設定条件の登録時に使用される任意および必須のマスタデータオブジェクトの概要を示しています。

SAP Best Practices ベースラインパッケージがインストール済の場合は、ベースラインパッケージサンプルデータを使用したり、必要に応じて独自のマスタデータを追加したりすることができます。

| マスタデータオブジェクト | データセグメントでの使用 | 必須/任意 | サンプル値 | コメント |
| --- | --- | --- | --- | --- |
| 販売組織 | 第一画面 | 必須 | <販売組織番号> |  |
| 流通チャネル | 第一画面 | 必須 | <販売チャネル番号> |  |
| 品目 | 第一画面 | 必須 | 例: TG11 |  |

|  |
| --- |
| 注意 マスタデータ値のサンプル値は国/地域依存であり、ベースラインパッケージのサンプルデータはサポートされる国/地域におけるローカライズ値を示します。 |

## 概要テーブル

このスコープアイテムは、以下の表に示されている複数のプロセスステップで構成されます。

|  |
| --- |
| 注記 システム管理者が SAP Fiori ラウンチパッドでスペースおよびページを有効化している場合、ホームページには、ビジネスロールの一般的なタスクを実行するために必要なアプリのみが含まれます。ホームページに含まれていないその他すべての (検索可能な) アプリは、検索バーを使用して見つけることができます ([2434549](https://me.sap.com/notes/2434549))。ホームページをパーソナライズして非表示のアプリを含める場合は、ユーザプロファイルにナビゲートし、アプリファインダを選択します。 |

| プロセスステップ | ビジネスロール | トランザクション/アプリ | 予想される結果 |
| --- | --- | --- | --- |
| [価格設定条件の登録](#unique_7) [ ページ] 6 | 価格設定スペシャリスト | 品目価格設定 - 販売(VK12) | 販売価格設定条件が登録されます。 |

## テスト手順

このセクションでは、このスコープアイテムに属する各プロセスステップのテスト手順について説明します。

### 価格設定条件の登録

テスト管理

カスタマプロジェクト: プロジェクト固有部分への入力

|  |  |  |  |
| --- | --- | --- | --- |
| テストケース ID | <X.XX> | テスト実施日: |  |
| テスト実施者名: |  | 期間: |  |
| ビジネスロール: |  | 責任者: | <都道府県/州、サービスプロバイダ、カスタマ/共同サービスプロバイダ、およびカスタマ> |

目的

この手順では、販売価格設定条件の登録について説明します。

|  |
| --- |
| 注意 マスタデータ値のサンプル値は国/地域依存です。SAP S/4HANA Cloud Public Editionシステムで提供される国/地域依存値を置き換えるか、この目的で登録したマスタデータ値を使用してください。 |

手順

| テストステップ | テストステップ名 | 指示 | 予想される結果 | コメント |
| --- | --- | --- | --- | --- |
| 1 | ログオン | SAP Fiori ラウンチパッドに価格設定スペシャリストとしてログオンします。 | SAP Fiori ラウンチパッドが表示されます。 |  |
| 2 | SAP Fiori アプリにアクセスする | 品目価格設定 - 販売(VK12)を開きます。 | 委任登録: 第一画面が表示されます。 |  |
| 3 | 価格設定条件タイプ | 条件レコード変更ビューで、以下の情報を入力します。条件タイプ: PPR0などEnterを押します。 | キー組み合わせビューが表示されます。 |  |
| 4 | キー組合せ | キー組み合わせビューで、品目 (承認状況あり)を選択し、選択を選択します。 | 価格変更 (PPR0): 選択ビューが表示されます。 |  |
| 5 | 選択する | 価格変更 (PPR0): 選択ビューで、以下の情報を入力します。販売組織: <販売組織>流通チャネル: <流通チャネル>品目: 例: TG11有効開始日: <日付>など実行を選択します。 | 価格条件変更 (PPR0): 概要ビューが表示されます。 |  |
| 6 | 価格条件を変更する | 価格条件変更 (PPR0): 概要ビューで、以下のデータを入力します。品目: 例: TG11金額: $17.55$など有効開始日付: <現在の日付> など有効終了日付: <現在の日付から 1 年後>など | 品目価格設定条件が更新されます。 |  |
| 7 | 保存する | 保存を選択します。 | 価格設定条件が保存されます。 |  |

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
- related-to :: [[08-sales-order-management/create-sales-pricing-condition-mds-bet-539]]
- related-to :: [[08-sales-order-management/mds-bet-543]]
- related-to :: [[08-sales-order-management/script-de-dados-mestre-criar-condicao-de-determinacao-de-preco-de-vend]]
- related-to :: [[08-sales-order-management/script-de-datos-maestros-crear-condicion-de-determinacion-de-precio-de]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/BET_S4CLD2608_Master_Data_JA_XX.docx` — full document · extracted with `mammoth` · 6,309 chars in the whole document
