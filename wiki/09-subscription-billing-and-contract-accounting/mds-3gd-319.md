---
id: 09-subscription-billing-and-contract-accounting/mds-3gd-319
title: サービスタイプに基づく価格設定条件の登録 - MDS (3GD) (3GD_S4CLD2608_Master_Data_JA_XX)
description: "Japanese master data script 3GD: maintaining service-type based pricing conditions PST0, PST1, PST2 via app VK12 for consolidated billing in S/4HANA Cloud Public Edition 2608."
cluster: 09-subscription-billing-and-contract-accounting
tags: [kb/subscription-billing-and-contract-accounting, topic/consumption-items-and-rating]
aliases: [3GD_S4CLD2608_Master_Data_JA_XX]
keywords: [Consumption Items and Service-Type-Based Rating, service pricing conditions, condition type pst0, condition type pst1, condition type pst2, consolidated billing, business roles, sales organization, 3GD]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/3GD_S4CLD2608_Master_Data_JA_XX.docx]
confidence: high
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-319
topic: 09-subscription-billing-and-contract-accounting/consumption-items-and-rating
language: JA
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# サービスタイプに基づく価格設定条件の登録 - MDS (3GD) (3GD_S4CLD2608_Master_Data_JA_XX)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/3GD_S4CLD2608_Master_Data_JA_XX.docx`, extracted with `mammoth`. Grouped under **Consumption Items and Service-Type-Based Rating** in Subscription Billing and Contract Accounting. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

| <!-- image omitted: unnamed --> | マスタデータスクリプトSAP S/4HANA Cloud Public Edition - 02-07-26 |
| --- | --- |
|  | サービスタイプに基づく価格設定条件の登録 - MDS (3GD) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

目次

[1 目的 2](#_Toc233891561)

[2 前提条件 3](#_Toc233891562)

[2.1 システムアクセス 3](#_Toc233891563)

[2.2 ロール 3](#_Toc233891564)

[2.3 必須マスタデータおよび任意マスタデータ 3](#_Toc233891565)

[3 概要テーブル 5](#_Toc233891566)

[4 テスト手順 6](#_Toc233891567)

[4.1 PST0 の価格設定条件の登録 6](#_Toc233891568)

[4.2 PST1 の価格設定条件の登録 7](#_Toc233891569)

[4.3 PST2 の価格設定条件の登録 8](#_Toc233891570)

## 目的

サービス価格設定条件は、統合請求で自動価格設定を実行するために必要な情報を保存するために使用されます。これには、異なるバリアントに基づく価格と追加料金が含まれます。これらの条件は、特定の得意先や品目、またはパラメータの組合せに固有の場合があります。サービスに基づく価格設定条件には、品目に対する特定の通貨の価格などの情報が含まれています。この情報は、料金計算可能明細、料金計算計画明細、料金計算伝票、および請求伝票で使用および保存されます。

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

| 名称 (ロールテンプレート) | ID (ロールテンプレート) | 名称 (ラウンチパッド領域) | ID (ラウンチパッド領域) |
| --- | --- | --- | --- |
| 価格設定スペシャリスト | SAP_BR_PRICING_SPECIALIST | 価格管理 | SAP_BR_PRICING_SPECIALIST |

### 必須マスタデータおよび任意マスタデータ

マスタデータレコードは、他のマスタデータを参照する場合があります。以下の表は、マスタデータレコードで使用される、任意および必須のマスタデータオブジェクトの概要を示しています。

| マスタデータオブジェクト | データセグメントでの使用 | 必須/任意 | コメント |
| --- | --- | --- | --- |
| 販売組織 | 第一画面 | 必須 | <販売組織番号> |
| 流通チャネル | 第一画面 | 必須 | <販売チャネル番号> |

## 概要テーブル

このマスタレコードは、以下の表に示されている複数のセグメントで構成されます。

|  |
| --- |
| 注記 システム管理者が SAP Fiori ラウンチパッドでスペースおよびページを有効化している場合、ホームページには、ビジネスロールの一般的なタスクを実行するために必要なアプリのみが含まれます。ホームページに含まれていないその他すべての (検索可能な) アプリは、検索バーを使用して見つけることができます ([2434549](https://me.sap.com/notes/2434549))。ホームページをパーソナライズして非表示のアプリを含める場合は、ユーザプロファイルにナビゲートし、アプリファインダを選択します。 |

| セグメント | ビジネスロール | アプリ/トランザクション | 予想される結果 |
| --- | --- | --- | --- |
| [PST0 の価格設定条件の登録](#unique_7) [ ページ] 6 | 価格設定スペシャリスト | 品目価格設定 - 販売(VK12) | 品目価格設定条件が更新されます。 |
| [PST1 の価格設定条件の登録](#unique_8) [ ページ] 7 | 価格設定スペシャリスト | 品目価格設定 - 販売(VK12) | 品目価格設定条件が更新されます。 |
| [PST2 の価格設定条件の登録](#unique_9) [ ページ] 8 | 価格設定スペシャリスト | 品目価格設定 - 販売(VK12) | 品目価格設定条件が更新されます。 |

## テスト手順

このセクションには、このマスタレコードに含まれる各セグメントまたはプロセスステップの手順が記載されています。

### PST0 の価格設定条件の登録

テスト管理

カスタマプロジェクト: プロジェクト固有部分への入力

|  |  |  |  |
| --- | --- | --- | --- |
| テストケース ID | <X.XX> | テスト実施日: |  |
| テスト実施者名: |  | 期間: |  |
| ビジネスロール: |  | 責任者: | <都道府県/州、サービスプロバイダ、カスタマ/共同サービスプロバイダ、およびカスタマ> |

目的

この手順では、販売価格設定条件の登録について説明します。PST0

手順

| テストステップ番号 | テストステップ名 | 指示 | 予想される結果 | コメント |
| --- | --- | --- | --- | --- |
| 1 | ログオン | SAP Fiori ラウンチパッドに価格設定スペシャリストとしてログオンします。 | 開始ページが表示されます。 |  |
| 2 | SAP Fiori アプリにアクセスする | 品目価格設定 - 販売(VK12)を開きます。 | 条件レコード変更画面が表示されます。 |  |
| 3 | 価格設定条件タイプ | 条件レコード変更ビューで以下のエントリを入力し、Enterを選択します。条件タイプ: PST0 |  |  |
| 4 | 選択する | サービスタイプベース価格設定条件変更 (PST0): 選択ビューで以下のエントリを入力し、実行を選択します。販売組織: <販売組織>流通チャネル: <流通チャネル> |  |  |
| 5 | 価格条件を変更する | サービスタイプベース価格設定条件変更 (PST0): 概要ビューで、以下のエントリを入力して、保存を押します。品目: CBPTS002金額: <金額>UoM: <個>有効開始: <現在の日付>有効終了日付: <現在の日付から 1 年後>など | 品目価格設定条件が更新されます。 |  |

### PST1 の価格設定条件の登録

テスト管理

カスタマプロジェクト: プロジェクト固有部分への入力

|  |  |  |  |
| --- | --- | --- | --- |
| テストケース ID | <X.XX> | テスト実施日: |  |
| テスト実施者名: |  | 期間: |  |
| ビジネスロール: |  | 責任者: | <都道府県/州、サービスプロバイダ、カスタマ/共同サービスプロバイダ、およびカスタマ> |

目的

この手順では、販売価格設定条件の登録について説明します。PST1

手順

| テストステップ番号 | テストステップ名 | 指示 | 予想される結果 | コメント |
| --- | --- | --- | --- | --- |
| 1 | ログオン | SAP Fiori ラウンチパッドに価格設定スペシャリストとしてログオンします。 | 開始ページが表示されます。 |  |
| 2 | SAP Fiori アプリにアクセスする | 品目価格設定 - 販売(VK12)を開きます。 | 条件レコード変更画面が表示されます。 |  |
| 3 | 価格設定条件タイプ | 条件レコード変更ビューで、以下のエントリを入力し、Enterを選択します。条件タイプ: PST1 |  |  |
| 4 | 選択する | サービスタイプベース可変価格設定変更 (PST1): 選択ビューで以下のエントリを入力し、実行を選択します。販売組織: 販売組織流通チャネル: 流通チャネル |  |  |
| 5 | 価格条件を変更する | サービスタイプベース可変価格設定変更 (PST1): 概要ビューで、以下のエントリを入力して、保存を押します。品目: CBPTS001バリアント: 高性能金額: <金額>UoM: PC有効開始: <現在の日付>有効終了日付: <現在の日付から 1 年後>など | 品目価格設定条件が更新されます。 |  |

### PST2 の価格設定条件の登録

テスト管理

カスタマプロジェクト: プロジェクト固有部分への入力

|  |  |  |  |
| --- | --- | --- | --- |
| テストケース ID | <X.XX> | テスト実施日: |  |
| テスト実施者名: |  | 期間: |  |
| ビジネスロール: |  | 責任者: | <都道府県/州、サービスプロバイダ、カスタマ/共同サービスプロバイダ、およびカスタマ> |

目的

この手順では、販売価格設定条件の登録について説明します。PST2

手順

| テストステップ番号 | テストステップ名 | 指示 | 予想される結果 | コメント |
| --- | --- | --- | --- | --- |
| 1 | ログオン | SAP Fiori ラウンチパッドに価格設定スペシャリストとしてログオンします。 | 開始ページが表示されます。 |  |
| 2 | SAP Fiori アプリにアクセスする | 品目価格設定 - 販売(VK12)を開きます。 | 条件レコード変更画面が表示されます。 |  |
| 3 | 価格設定条件タイプ | 条件レコード変更ビューで、以下のエントリを入力し、Enterを選択します。条件タイプ: PST2 |  |  |
| 4 | 選択する | サービスタイプベース可変 % (PST2): 選択ビューで以下のエントリを入力し、実行を選択します。販売組織: 販売組織流通チャネル: 流通チャネル |  |  |
| 5 | 価格条件を変更する | サービスタイプベース可変 % 変更 (PST2): 概要ビューで、以下のエントリを入力して、保存を押します。品目: CBPTS001バリアント: 高性能金額: <金額>有効開始: <現在の日付>有効終了日付: <現在の日付から 1 年後>など | 品目価格設定条件が更新されます。 |  |

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
- related-to :: [[09-subscription-billing-and-contract-accounting/criar-condicao-de-determinacao-de-precos-baseada-em-tipo-de-servico-md]]
- related-to :: [[09-subscription-billing-and-contract-accounting/master-data-script-create-service-type-based-pricing-condition-mds-3gd]]
- related-to :: [[09-subscription-billing-and-contract-accounting/mds-3gd-321]]
- related-to :: [[09-subscription-billing-and-contract-accounting/script-de-datos-maestros-crear-condicion-de-determinacion-de-precios-b]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/3GD_S4CLD2608_Master_Data_JA_XX.docx` — full document · extracted with `mammoth` · 7,778 chars in the whole document
