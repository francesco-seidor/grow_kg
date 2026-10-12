---
id: 14-maintenance-service-and-projects/mds-5to-487
title: プロジェクトのサービス製品の登録 - MDS (5TO) (5TO_S4CLD2608_Master_Data_JA_XX)
description: Japanese master data test script (MDS 5TO) for creating the service product PROJECT with sales org data via MM01 in SAP S/4HANA Cloud Public Edition 2608.
cluster: 14-maintenance-service-and-projects
tags: [kb/maintenance-service-and-projects, topic/solution-orders-and-cpq]
aliases: [5TO_S4CLD2608_Master_Data_JA_XX]
keywords: [Solution Orders and SAP CPQ Quotations, service product, master data script, product master, sales organization data, profit center, business roles, brazil tax fields, 5TO]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/5TO_S4CLD2608_Master_Data_JA_XX.docx]
confidence: high
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-487
topic: 14-maintenance-service-and-projects/solution-orders-and-cpq
language: JA
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# プロジェクトのサービス製品の登録 - MDS (5TO) (5TO_S4CLD2608_Master_Data_JA_XX)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/5TO_S4CLD2608_Master_Data_JA_XX.docx`, extracted with `mammoth`. Grouped under **Solution Orders and SAP CPQ Quotations** in Maintenance, Service and Projects. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

| <!-- image omitted: unnamed --> | マスタデータスクリプトSAP S/4HANA Cloud Public Edition - 02-07-26 |
| --- | --- |
|  | プロジェクトのサービス製品の登録 - MDS (5TO) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

目次

[1 目的 2](#_Toc233891748)

[2 前提条件 3](#_Toc233891749)

[2.1 システムアクセス 3](#_Toc233891750)

[2.2 ロール 3](#_Toc233891751)

[2.3 必須の組織ユニット 3](#_Toc233891752)

[2.4 必須のマスタデータおよび操作可能なマスタデータ 4](#_Toc233891753)

[3 概要テーブル 5](#_Toc233891754)

[4 テスト手順 6](#_Toc233891755)

[4.1 サービス製品の登録 - PROJECT 6](#_Toc233891756)

## 目的

この文書では、価格を含むサービス製品マスタデータレコードの登録方法について説明します。この説明には、"標準的" なシステム環境で処理するマスタデータに関連するデータセグメントが含まれています。読者は、通常、入力値を入力する必要があるデータセグメントおよび項目について主に学習します。この範囲に該当しない項目は、UI に表示される場合でもこの文書では説明していません。

この説明に従って登録されるサービス製品マスタレコードは、ソリューションオーダで使用することができます。

| サービス製品 ID | 説明 | 用途 |
| --- | --- | --- |
| プロジェクト | プロジェクト | プロジェクトを表します。 |

## 前提条件

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
| マスタデータスペシャリスト - 製品データ | SAP_BR_PRODMASTER_SPECIALIST | マスタデータ - 製品 | SAP_CMD_SP_PR_MAINT |

### 必須の組織ユニット

マスタデータの一部のセグメントは会社の組織ユニットに依存し、一般 (共通) データは組織ユニットまたは会社コードに依存しません。以下の表は、さまざまなデータセグメントおよび関連する組織ユニットの概要を示しています。

| データセグメント | 依存対象 | US に使用される組織ユニット | DE に使用される組織ユニット |
| --- | --- | --- | --- |
| 品目の登録 | 販売組織 | 1710 (国内販売組織 US) | 1010 (国内販売組織 DE) |
| 品目の登録 | 流通チャネル | 10 (直販) | 10 (直販) |

### 必須のマスタデータおよび操作可能なマスタデータ

品目マスタデータレコードは、他のマスタデータを参照する場合があります。以下の表は、品目マスタデータレコードで使用される、任意および必須のマスタデータオブジェクトの概要を示しています。

|  |
| --- |
| 注記 適切な税計算を取得するには、ブラジル固有の項目が必要です。チェックNota Fiscal (ブラジル) - JD0品目マスタデータの BR 固有項目の定義の章を参照してください。 |

| マスタデータオブジェクト | データセグメントでの使用 | 必須/任意 | コメント |
| --- | --- | --- | --- |
| 利益センタ |  | 必須 | 正しい評価プロセスのためには、品目 (製品) マスタへの利益センタの割当が必要です。 |

## 概要テーブル

このマスタレコードは、以下の表に示されている複数のセグメントで構成されます。

システム管理者が SAP Fiori ラウンチパッドでスペースおよびページを有効化している場合、ホームページには、ビジネスロールの一般的なタスクを実行するために必要なアプリのみが含まれます。

ホームページに含まれていないその他すべてのアプリは、検索バーを使用して見つけることができます。

ホームページをパーソナライズして非表示のアプリを含める場合は、ユーザプロファイルにナビゲートし、設定 > アプリファインダを選択します。

| ID (ロールテンプレート) | ビジネスロール | アプリ/トランザクション | 予想される結果 |
| --- | --- | --- | --- |
| サービス製品の登録 | SAP_BR_PRODMASTER_SPECIALIST | 品目登録(MM01) | サービス製品が登録されます。 |

## テスト手順

このセクションには、このマスタレコードに含まれる各セグメントまたはプロセスステップの手順が記載されています。

### サービス製品の登録 - PROJECT

目的

| テストステップ番号 | テストステップ名 | 指示 | 予想される結果 | コメント |
| --- | --- | --- | --- | --- |
| 1 | ログオンする | SAP Fiori ラウンチパッドに マスタデータスペシャリスト - 製品データ (MDG)としてログオンします。 |  |  |
| 2 | SAP Fiori アプリにアクセスする | 品目登録(MM01) タイルを選択します。 | 品目登録 (第一画面) が表示されます。 |  |
| 3 | 品目基本データを更新する (サービス製品用) | 品目登録 (第一画面)で、以下のエントリを入力します。品目: PROJECT品目タイプ: サービス製品次に続行 (Enter) を選択します。 | 新規サービス製品の基本情報を更新しました。ビュー選択ダイアログウィンドウが表示されます。 |  |
| 4 | ビューを選択する | ビュー選択: 基本データ 1 ビューを選択し、次に続行 (Enter) を選択します。 | 品目 PROJECT 登録ビューが表示されます。 |  |
| 5 | 基本データを更新する | 基本データ 1 ビューで、以下の値を更新します。テキスト: プロジェクト明細基本数量単位: AU (活動単位)品目グループ: P001 (サービス)GenItemGroup: SPRJ (プロジェクト)次に、保存を選択します。 | 基本データが更新され、サービス製品が保存されます。保存後、品目登録 (第一画面) ビューが表示されます。会社で使用する異なる各言語に対して、対応する製品テキストを言語コードごとに更新する必要があります。 |  |
| 6 | 製品の詳細を拡張する | 品目登録 (第一画面) ビューで、品目 PROJECT を入力し、次に続行 (Enter) を選択します。 | ビュー選択ダイアログウィンドウが表示されます。 |  |
| 7 | ビューを選択する | ビュー選択ダイアログウィンドウで、以下のビューを選択します。販売: 販売組織データ 1販売: 販売組織データ 2次に続行 (Enter) を選択します。 | 組織レベルダイアログウィンドウが表示されます。 |  |
| 8 | 組織レベルを選択する | 組織レベルウィンドウで、以下の値を更新します。販売組織:1710 (国内販売組織 US)流通チャネル: 10 (直販)次に続行 (Enter) を選択します。 | 組織データが選択されました。品目 PROJECT 登録ビューが表示されます。 |  |
| 9 | 販売組織データを更新する (1) | 販売: 販売組織1 ビューで、以下の値を更新します。一般データ現金割引: X <選択済>税データ税分類:1 (全課税)次に Enter を選択します。 | 販売組織データが更新されます。販売: 販売組織2 タブページが表示されます。 |  |
| 10 | 販売組織データを更新する (2) | 販売: 販売組織2 ビューで、以下のエントリを更新します。明細カテゴリグループ: SPRJ (プロジェクト)次にEnterを選択します。次に、保存を選択します。 | 販売組織データが更新されます。販売: 一般/プラントタブページが表示されます。 |  |

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
- related-to :: [[14-maintenance-service-and-projects/creacion-de-producto-de-servicio-para-proyecto-mds-5to-486]]
- related-to :: [[14-maintenance-service-and-projects/criar-produto-de-servico-para-projeto-mds-5to-488]]
- related-to :: [[14-maintenance-service-and-projects/master-data-script-create-service-product-for-project-5to-485]]
- related-to :: [[14-maintenance-service-and-projects/mds-5to-489]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/5TO_S4CLD2608_Master_Data_JA_XX.docx` — full document · extracted with `mammoth` · 6,781 chars in the whole document
