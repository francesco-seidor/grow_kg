---
id: 06-management-accounting/mds-bnp-649
title: 原価要素グループの登録 - MDS (BNP) (BNP_S4CLD2608_Master_Data_JA_XX)
description: "SAP S/4HANA Cloud Public Edition 2608 マスタデータスクリプト (BNP): 管理会計担当者が原価要素グループ管理 (F5373) で原価要素グループを登録する手順 (日本語)。"
cluster: 06-management-accounting
tags: [kb/management-accounting, topic/cost-element-groups]
aliases: [BNP_S4CLD2608_Master_Data_JA_XX]
keywords: [Cost Element Groups, master data scripts, reporting row structures, business roles, fiori launchpad access, controlling area, chart of accounts, BNP]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/BNP_S4CLD2608_Master_Data_JA_XX.docx]
confidence: high
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-649
topic: 06-management-accounting/cost-element-groups
language: JA
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# 原価要素グループの登録 - MDS (BNP) (BNP_S4CLD2608_Master_Data_JA_XX)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/BNP_S4CLD2608_Master_Data_JA_XX.docx`, extracted with `mammoth`. Grouped under **Cost Element Groups** in Management Accounting. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

| <!-- image omitted: unnamed --> | マスタデータスクリプトSAP S/4HANA Cloud Public Edition - 02-07-26 |
| --- | --- |
|  | 原価要素グループの登録 - MDS (BNP) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

目次

[1 目的 2](#_Toc233891961)

[2 前提条件 3](#_Toc233891962)

[2.1 システムアクセス 3](#_Toc233891963)

[2.2 ロール 3](#_Toc233891964)

[2.3 必須の組織ユニット 3](#_Toc233891965)

[2.4 必須マスタデータおよび任意マスタデータ 4](#_Toc233891966)

[2.5 データ登録の主要パラメータ 4](#_Toc233891967)

[3 概要テーブル 5](#_Toc233891968)

[4 テスト手順 6](#_Toc233891969)

[4.1 原価要素グループマスタデータの登録 6](#_Toc233891970)

## 目的

ビジネスコンテキスト

原価要素グループは、主にレポート目的で特性が類似する原価要素を収集するために使用されます。原価要素グループは、情報システムなどで使用できます。原価要素グループ構造を使用して、レポートの行構造を定義することができます。合計は、各ノードのレポートで計算されます。

複数の原価要素を 1 つのトランザクションで処理する場合にも、原価要素グループを使用できます。たとえば、原価センタ計画、付替、配賦などで使用できます。

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
| 管理会計担当者 - 間接費 | SAP_BR_OVERHEAD_ACCOUNTANT | 間接費会計 | SAP_BR_OVERHEAD_ACCOUNTANT |  |

### 必須の組織ユニット

会社の組織構造およびマスタデータは導入時に ERP システムに登録されました。組織構造には会社の実際の組織構造が反映されています。マスタデータは、会社の重点業務に応じて原価要素グループを表します。

| データオブジェクト | データセグメントでの使用 | 必須/任意 | コメント |
| --- | --- | --- | --- |
| 管理領域 | 一般データ | 必須 |  |

### 必須マスタデータおよび任意マスタデータ

原価要素グループのマスタデータレコードは、他のマスタデータを参照している場合があります。以下の表は、原価要素グループのデータレコードで使用される任意および必須のマスタデータオブジェクトの概要です。

| マスタデータオブジェクト | データセグメントでの使用 | 必須/任意 | コメント |
| --- | --- | --- | --- |
| 勘定コード表 | 組織ユニット | 任意 |  |

### データ登録の主要パラメータ

このスコープアイテムに、ビジネス条件はありません。

## 概要テーブル

このスコープアイテムは、以下の表に示されている複数のプロセスステップで構成されます。

|  |
| --- |
| 注記 システム管理者が SAP Fiori ラウンチパッドでスペースおよびページを有効化している場合、ホームページには、ビジネスロールの一般的なタスクを実行するために必要なアプリのみが含まれます。ホームページに含まれていないその他すべての (検索可能な) アプリは、検索バーを使用して見つけることができます ([2434549](https://me.sap.com/notes/2434549))。ホームページをパーソナライズして非表示のアプリを含める場合は、ユーザプロファイルにナビゲートし、アプリファインダを選択します。 |

| プロセスステップ | ビジネスロール | トランザクション/アプリ | 予想される結果 |
| --- | --- | --- | --- |
| [原価要素グループマスタデータの登録](#unique_9) [ ページ] 6 | 管理会計担当者 - 間接費 | 原価要素グループ管理 (F5373) | 原価要素グループを新たなビジネス要件に従って登録できます。 |

## テスト手順

このセクションでは、このスコープアイテムに属する各プロセスステップのテスト手順について説明します。

### 原価要素グループマスタデータの登録

テスト管理

カスタマプロジェクト: プロジェクト固有部分への入力

|  |  |  |  |
| --- | --- | --- | --- |
| テストケース ID | <X.XX> | テスト実施日: |  |
| テスト実施者名: |  | 期間: |  |
| ビジネスロール: |  | 責任者: | <都道府県/州、サービスプロバイダ、カスタマ/共同サービスプロバイダ、およびカスタマ> |

前提条件

品目の基本データを入力および保存しておきます。

手順

| テストステップ番号 | テストステップ名 | 指示 | 予想される結果 | コメント |
| --- | --- | --- | --- | --- |
| 1 | ログオンする | SAP Fiori ラウンチパッドに管理会計担当者 - 間接費としてログオンします。 | SAP Fiori ラウンチパッドが表示されます。 |  |
| 2 | SAP Fiori アプリにアクセスする | 原価要素グループ管理 (F5373)を開きます。 | アプリが開きます。 |  |
| 3 | 新規原価要素グループを入力する | 原価要素グループ管理画面で、登録を選択します。原価要素グループ: 第一画面で、以下のエントリを入力します。原価要素グループ: <原価要素グループ>Enterを押します。あるいは、既存の原価センタグループからの参照を選択できます。 | 原価要素グループ登録: 構造画面が表示されます。 |  |
| 4 | 原価要素または原価要素グループ (もしくはその両方) を入力する | 新しいマスタデータが原価要素グループ: 構造画面に表示されます。以下のエントリを入力します。テキスト: <テキスト>さらに、選択対象にカーソルを合わせて、以下のナビゲーションボタンを利用することで、以下のエントリを入力できます。下位レベル: <下位レベルの原価要素グループを挿入>原価要素: <(挿入オプション) - 原価要素または要素範囲追加>同レベル: <同じ下位レベルに追加原価要素グループを挿入> | 新しいマスタデータが原価要素グループ: 構造画面に表示されます。 |  |
| 5 | データを保存する | 保存を選択します。 | 原価要素グループが登録されて保存されます。 |  |

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
- related-to :: [[06-management-accounting/create-cost-element-group-mds-bnp-647]]
- related-to :: [[06-management-accounting/criar-grupo-de-classes-de-custo-mds-bnp-650]]
- related-to :: [[06-management-accounting/kostenartengruppe-anlegen-sds-bnp-646]]
- related-to :: [[06-management-accounting/mds-bnp-651]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/BNP_S4CLD2608_Master_Data_JA_XX.docx` — full document · extracted with `mammoth` · 6,297 chars in the whole document
