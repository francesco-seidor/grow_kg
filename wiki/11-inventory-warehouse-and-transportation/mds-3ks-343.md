---
id: 11-inventory-warehouse-and-transportation/mds-3ks-343
title: 生産供給場所の更新 - MDS (3KS) (3KS_S4CLD2608_Master_Data_JA_XX)
description: Japanese master data script (3KS) for optionally assigning storage bins to production supply areas (PSA) in warehouse-production integration.
cluster: 11-inventory-warehouse-and-transportation
tags: [kb/inventory-warehouse-and-transportation, topic/ewm-production-integration]
aliases: [3KS_S4CLD2608_Master_Data_JA_XX]
keywords: [EWM Production Supply and Receipt, production supply areas, storage bin assignment, warehouse production integration, kanban, business partners, business conditions, business roles, 3KS]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/3KS_S4CLD2608_Master_Data_JA_XX.docx]
confidence: high
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-343
topic: 11-inventory-warehouse-and-transportation/ewm-production-integration
language: JA
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# 生産供給場所の更新 - MDS (3KS) (3KS_S4CLD2608_Master_Data_JA_XX)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/3KS_S4CLD2608_Master_Data_JA_XX.docx`, extracted with `mammoth`. Grouped under **EWM Production Supply and Receipt** in Inventory, Warehouse and Transportation. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

| <!-- image omitted: unnamed --> | マスタデータスクリプトSAP S/4HANA Cloud Public Edition - 02-07-26 |
| --- | --- |
|  | 生産供給場所の更新 - MDS (3KS) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

目次

[1 目的 2](#_Toc233891574)

[2 前提条件 3](#_Toc233891575)

[2.1 システムアクセス 3](#_Toc233891576)

[2.2 ロール 3](#_Toc233891577)

[2.3 必須の組織ユニット 3](#_Toc233891578)

[2.4 必須マスタデータおよび任意マスタデータ 4](#_Toc233891579)

[2.5 ビジネス条件 4](#_Toc233891580)

[3 概要テーブル 5](#_Toc233891581)

[4 テスト手順 6](#_Toc233891582)

[4.1 (オプション) PSA への棚番割当 - 倉庫 6](#_Toc233891583)

[4.2 (オプション) PSA への棚番割当 7](#_Toc233891584)

## 目的

この文書では、生産供給の倉庫マスタデータを登録するために、以下のアクティビティを実行する方法について学習します。

- [(オプション) PSA への棚番割当 - 倉庫](#unique_2) [ ページ] 6
- [(オプション) PSA への棚番割当](#unique_3) [ ページ] 7

供給場所登録および複製と PSA への棚番割当は、ビジネス条件の章に記載されているマスタデータスクリプトまたはテストスクリプト文書の関連ステップの実行によって行われることになっています。このマスタデータスクリプトは、関連設定をチェックし、ビジネス条件が満たされていない場合は設定をマニュアル登録するカスタマのみを対象としています。

テキストには、標準的なシステム環境で処理するマスタデータに関連するデータセグメントが含まれています。主に、入力値を入力する必要があるデータセグメントおよび項目について学習します。SAP Best Practices による SAP S/4HANA コンテンツ提供の範囲に関連しない項目については、UI に表示される場合でもこの文書では説明していません。

このマスタデータは、倉庫管理の生産統合ビジネスプロセスに使用します。

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
| 倉庫担当者 (EWM) | SAP_BR_WAREHOUSE_CLERK_EWM | 倉庫オフィス | SAP_BR_WAREHOUSE_CLERK_EWM |

### 必須の組織ユニット

マスタデータの一部のセグメントは、会社の組織ユニットによって異なります。一般 (共通) データは組織ユニットまたは会社コードに依存しません。以下の表は、さまざまなデータセグメントおよび関連する組織ユニットの概要を示しています。

| データセグメント | 依存対象 | 項目例 | コメント | 使用される組織ユニット |
| --- | --- | --- | --- | --- |
| すべて | 倉庫番号 |  |  |  |

### 必須マスタデータおよび任意マスタデータ

マスタデータレコードは、他のマスタデータを参照する場合があります。以下の表は、PSA マスタデータレコードに棚番割当を登録する際に使用される、任意および必須のマスタデータオブジェクトの概要を示しています。

| マスタデータオブジェクト | データセグメントでの使用 | 必須/任意 | コメント |
| --- | --- | --- | --- |
| ビジネスパートナ | PSA への棚番割当 - 倉庫 | 必須 | 倉庫の処分対象当事者としてのビジネスパートナ。 |
| 供給場所 | PSA への棚番割当 - 倉庫 | 必須 | SAP S/4HANA に登録される供給場所。ビジネス条件の章を参照してください。 |
| 製品 | PSA への棚番割当 - 倉庫 | 必須 |  |
| 棚番 | PSA への棚番割当 - 倉庫 | 必須 |  |

### ビジネス条件

このスコープアイテムをテストする前に、以下のビジネス条件を満たしておく必要があります。

| スコープアイテム ID | ビジネス条件 |
| --- | --- |
| 40D - 供給場所の登録 - MDS | このマスタデータスクリプトは、この文書の前提条件です。供給場所 (PSA) の登録時に、Cloud WM 保管場所 (105Wなど) を使用します。このマスタデータスクリプトを実行した後、以下の設定を登録しておきます。供給場所が SAP S/4HANA に登録されます。関連する供給場所が SAP S/4HANA から Cloud Warehouse に自動的に複製されます。 |
| 3DV - 倉庫生産統合 | この文書の前提条件は、3DV テストスクリプトの予備ステップの章の管理周期登録ステップです。管理周期登録ステップを実行した後、以下の設定を登録しておきます。関連する供給場所が SAP S/4HANA から Cloud Warehouse に自動的に複製されます。棚番が PSA に割り当てられます。 |
| 3VT - かんばん生産管理方式による生産供給の在庫 | この文書の前提条件は、3VT テストスクリプトの予備ステップの章の "かんばんの管理周期: 在庫転送" ステップです。"かんばんの管理周期: 在庫転送" ステップを実行した後、以下の設定を登録しておきます。関連する供給場所が SAP S/4HANA から Cloud Warehouse に自動的に複製されます。棚番が PSA に割り当てられます。 |

## 概要テーブル

このマスタレコードは、以下の表に示されている複数のセグメントで構成されます。

|  |
| --- |
| 注記 システム管理者が SAP Fiori ラウンチパッドでスペースおよびページを有効化している場合、ホームページには、ビジネスロールの一般的なタスクを実行するために必要なアプリのみが含まれます。ホームページに含まれていないその他すべての (検索可能な) アプリは、検索バーを使用して見つけることができます ([2434549](https://me.sap.com/notes/2434549))。ホームページをパーソナライズして非表示のアプリを含める場合は、ユーザプロファイルにナビゲートし、アプリファインダを選択します。 |

| セグメント | ビジネスロール | アプリ/トランザクション | 予想される結果 |
| --- | --- | --- | --- |
| [(オプション) PSA への棚番割当 - 倉庫](#unique_2) [ ページ] 6 | 倉庫担当者 (EWM) | PSA への棚番割当 - 倉庫(/SCWM/PSASTAGE) | PSA への棚番の割当が登録されます。 |
| [(オプション) PSA への棚番割当](#unique_3) [ ページ] 7 | 倉庫担当者 (EWM) | PSA への棚番割当 (/SCWM/PSASTAGE2) | PSA への棚番の割当が登録されます。 |

## テスト手順

このセクションには、このマスタレコードに含まれる各セグメントまたはプロセスステップの手順が記載されています。

### (オプション) PSA への棚番割当 - 倉庫

目的

このセクションでは、SAP Fiori ラウンチパッドを使用し、SAP S/4HANA における倉庫番号の全供給場所の棚番割当を管理します。

このステップはオプションであり、棚番が想定どおりに PSA に割り当てられている場合はスキップすることができます。このステップは、管理周期登録ステップ時に PSA の棚番割当がまだ実行されていない場合にのみ必要です。ビジネス条件の章の管理周期登録ステップを参照してください。

手順

| テストステップ番号 | テストステップ名 | 指示 | 予想される結果 | コメント |
| --- | --- | --- | --- | --- |
| 1 | ログオン | SAP Fiori ラウンチパッドに倉庫担当者 (EWM)としてログオンします。 |  |  |
| 2 | アプリにアクセスする | PSA への棚番割当 - 倉庫(/SCWM/PSASTAGE)を開きます。 |  |  |
| 3 | 新規エントリを登録する | ビュー "PSA への棚番割当" 変更: 概要画面で、新規エントリを選択します。 |  |  |
| 4 | 割当値を入力する | 新規エントリ: 追加エントリ詳細画面で、以下のデータを入力します。処分: <処分対象当事者のビジネスパートナ ID>供給場所: <供給場所>製品: <製品 ID>棚番: <棚番 ID> |  |  |
| 5 | データを保存する | 保存を選択します。 | システムメッセージによって、PSA への棚番の割当が保存されたことが通知されます。 |  |

### (オプション) PSA への棚番割当

目的

このセクションでは、SAP Fiori ラウンチパッドを使用し、SAP S/4HANA における特定の供給場所内の棚番割当すべてを管理します。

このステップはオプションであり、棚番が想定どおりに PSA に割り当てられている場合はスキップすることができます。このステップは、管理周期登録ステップ時に PSA の棚番割当がまだ実行されていない場合にのみ必要です。ビジネス条件の章の管理周期登録ステップを参照してください。

手順

| テストステップ番号 | テストステップ名 | 指示 | 予想される結果 | コメント |
| --- | --- | --- | --- | --- |
| 1 | ログオン | SAP Fiori ラウンチパッドに倉庫担当者 (EWM)としてログオンします。 |  |  |
| 2 | アプリにアクセスする | PSA への棚番割当 (/SCWM/PSASTAGE2)を開きます。 |  |  |
| 3 | 作業領域を設定する | 作業領域決定エントリダイアログボックスで、以下のデータを入力します。処分対象当事者: <処分対象当事者のビジネスパートナ ID>供給場所: <供給場所>続行を選択します。 |  |  |
| 4 | 新規エントリを登録する | ビュー "PSA への棚番割当" 変更: 概要画面で、新規エントリを選択します。 |  |  |
| 5 | 割当値を入力する | 新規エントリ: 追加エントリ詳細画面で、以下のデータを入力します。製品: <製品 ID>棚番: <棚番 ID> |  |  |
| 6 | データを保存する | 保存を選択します。 | システムメッセージによって、PSA への棚番の割当が保存されたことが通知されます。 |  |

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
- related-to :: [[11-inventory-warehouse-and-transportation/atualizar-area-de-abastecimento-da-producao-mds-3ks-344]]
- related-to :: [[11-inventory-warehouse-and-transportation/maintain-production-supply-area-mds-3ks-341]]
- related-to :: [[11-inventory-warehouse-and-transportation/mds-3ks-345]]
- related-to :: [[11-inventory-warehouse-and-transportation/produktionsversorgungsbereich-pflegen-sds-3ks-340]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/3KS_S4CLD2608_Master_Data_JA_XX.docx` — full document · extracted with `mammoth` · 7,994 chars in the whole document
