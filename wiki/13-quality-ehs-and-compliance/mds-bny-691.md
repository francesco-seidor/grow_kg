---
id: 13-quality-ehs-and-compliance/mds-bny-691
title: 品目/製品マスタの品質管理属性の登録 - MDS (BNY) (BNY_S4CLD2608_Master_Data_JA_XX)
description: マスタデータスクリプト（日本語）：MM01 で品目マスタの品質管理ビュー（検査タイプ等）をプラント別に登録する手順。
cluster: 13-quality-ehs-and-compliance
tags: [kb/quality-ehs-and-compliance, topic/qm-material-master-attributes]
aliases: [BNY_S4CLD2608_Master_Data_JA_XX]
keywords: [Quality Management View of the Material Master, quality management view, inspection type, material master, automatic usage decision, quality info record, business roles, master data scripts, BNY]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/BNY_S4CLD2608_Master_Data_JA_XX.docx]
confidence: high
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-691
topic: 13-quality-ehs-and-compliance/qm-material-master-attributes
language: JA
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# 品目/製品マスタの品質管理属性の登録 - MDS (BNY) (BNY_S4CLD2608_Master_Data_JA_XX)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/BNY_S4CLD2608_Master_Data_JA_XX.docx`, extracted with `mammoth`. Grouped under **Quality Management View of the Material Master** in Quality, EHS and Compliance. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

| <!-- image omitted: unnamed --> | マスタデータスクリプトSAP S/4HANA Cloud Public Edition - 02-07-26 |
| --- | --- |
|  | 品目/製品マスタの品質管理属性の登録 - MDS (BNY) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

目次

[1 目的 2](#_Toc233892065)

[2 前提条件 3](#_Toc233892066)

[2.1 システムアクセス 3](#_Toc233892067)

[2.2 ロール 3](#_Toc233892068)

[2.3 必須の組織ユニット 3](#_Toc233892069)

[3 概要テーブル 5](#_Toc233892070)

[4 テスト手順 6](#_Toc233892071)

[4.1 品目の品質管理属性 6](#_Toc233892072)

## 目的

品目の品質が検査されることになっている場合、品目マスタでそれぞれのプラントに対して品質管理ビューが更新されていることが前提条件です。

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

### 必須の組織ユニット

このセクションでは、マスタデータレコードの登録に関連するすべての組織ユニットについて説明します。

得意先マスタデータの一部のセグメントは会社の組織ユニットに依存し、一般 (セントラル) データは組織ユニットまたは会社コードに依存しません。以下の表は、さまざまなデータセグメントおよび関連する組織ユニットの概要を示しています。

| データセグメント | 依存対象 | 項目例 | コメント | 使用される組織ユニット |
| --- | --- | --- | --- | --- |
| 品質管理 | プラント |  | プラントデータは、品目マスタレコードが使用される企業構造のすべてのプラント ID に対して存在可能です。 | プラント: |

## 概要テーブル

このスコープアイテムは、以下の表に示されている複数のプロセスステップで構成されます。

|  |
| --- |
| 注記 システム管理者が SAP Fiori ラウンチパッドでスペースおよびページを有効化している場合、ホームページには、ビジネスロールの一般的なタスクを実行するために必要なアプリのみが含まれます。ホームページに含まれていないその他すべての (検索可能な) アプリは、検索バーを使用して見つけることができます ([2434549](https://me.sap.com/notes/2434549))。ホームページをパーソナライズして非表示のアプリを含める場合は、ユーザプロファイルにナビゲートし、アプリファインダを選択します。 |

| プロセスステップ | ビジネスロール | トランザクション/アプリ | 予想される結果 |
| --- | --- | --- | --- |
| [品目の品質管理属性](#unique_7) [ ページ] 6 | マスタデータスペシャリスト - 製品データ | 品目登録(MM01) | 品目マスタデータ - 品質管理データが登録されます。 |

## テスト手順

このセクションでは、このスコープアイテムに属する各プロセスステップのテスト手順について説明します。

### 品目の品質管理属性

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
| 1 | ログオンする | SAP Fiori ラウンチパッドにマスタデータスペシャリスト - 製品データとしてログオンします。 | SAP Fiori ラウンチパッドが表示されます。 |  |
| 2 | SAP Fiori アプリにアクセスする | 品目登録(MM01)を開きます。 | アプリが開きます。 |  |
| 3 | 品目データを入力する | 品目登録 (第一画面)画面で、以下のエントリを入力します。品目: <品目コード>品目タイプ: 商品Enterを押します。 | ビュー選択画面が表示されます。 |  |
| 4 | 品質管理ビューを選択する | ビュー選択画面で、品質管理ビューを選択し、組織レベルを選択します。 | 組織データ入力用の新しい画面が表示されます。 |  |
| 5 | 組織レベルデータを入力する | 組織レベル画面の組織レベルセクションで、以下のエントリを入力し、続行を選択します。プラント: <プラントコード> | 品目登録...(商品)画面が表示されます。 |  |
| 6 | 品質管理データを入力する | 品目 XXX 登録 (商品)画面の品質管理タブで品目のテキストを入力します。テキスト: <テキストを入力>品質管理タブの一般データセクションで、以下のエントリを入力します。基本数量単位: <数量単位>品質検査設定を選択します。表示されたダイアログボックスで品質検査タイプ登録を選択して、以下のエントリを入力します。品質検査タイプ: 01など優先品質検査タイプ: X有効: X検査タイプ詳細を選択して詳細を確認します。以下の項目に対してXのフラグが設定されていることを確認します。検査在庫への転記タスクリスト使用検査自動割当品質検査特性続行を選択します。 |  |  |
| 7 | 自動使用決定を有効化/無効化する (オプション) | 自動使用決定を選択または選択解除し、品目と品質検査タイプのこの組合せに対し、自動使用決定を有効化または無効化します。注記 結果記録後の自動使用決定は、品質検査結果が良い品質検査ロットに対して実行できます。このプロセスを有効化するには、システムがソリューション管理 (F1241)アプリで適切に設定されている必要があります。追加の技術情報および前提条件については、[SAP ヘルプ](https://help.sap.com/viewer/DRAFT/84dbf30eedb4450983dc3d1c81b71996/1811.500/en-US/746b66d98e504e238eca043bae05ecb8.html)を参照してください。 |  |  |
| 8 | 調達データを入力する (オプション) | 品目の品質情報レコードを任意で使用するには、品質管理タブの調達データセクションで、以下のエントリを入力します。調達における QM 有効: XQM 管理キー: 0001など |  |  |
| 9 | データを保存する | 保存を選択します。 | データが保存されます。 |  |

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
- related-to :: [[13-quality-ehs-and-compliance/create-quality-management-attributes-for-material-product-master-mds-b]]
- related-to :: [[13-quality-ehs-and-compliance/criar-atributos-de-administracao-de-qualidade-para-mestre-de-materiais]]
- related-to :: [[13-quality-ehs-and-compliance/mds-bny-693]]
- related-to :: [[13-quality-ehs-and-compliance/script-de-datos-maestros-crear-atributos-de-gestion-de-calidad-para-ma]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/BNY_S4CLD2608_Master_Data_JA_XX.docx` — full document · extracted with `mammoth` · 6,541 chars in the whole document
