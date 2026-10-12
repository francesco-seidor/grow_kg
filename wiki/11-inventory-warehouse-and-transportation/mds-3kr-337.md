---
id: 11-inventory-warehouse-and-transportation/mds-3kr-337
title: 棚番および固定保管棚の割当の更新 - MDS (3KR) (3KR_S4CLD2608_Master_Data_JA_XX)
description: "Japanese SAP master data script (3KR, 2608): create, change, display, mass-change storage bins and assign fixed storage bins in EWM as warehouse clerk."
cluster: 11-inventory-warehouse-and-transportation
tags: [kb/inventory-warehouse-and-transportation, topic/ewm-storage-bins]
aliases: [3KR_S4CLD2608_Master_Data_JA_XX]
keywords: [EWM Storage Bins and Fixed Bin Assignments, storage bins, fixed bin assignment, bin mass change, warehouse management, business roles, business partner, master data scripts, test procedures, 3KR]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/3KR_S4CLD2608_Master_Data_JA_XX.docx]
confidence: high
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-337
topic: 11-inventory-warehouse-and-transportation/ewm-storage-bins
language: JA
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# 棚番および固定保管棚の割当の更新 - MDS (3KR) (3KR_S4CLD2608_Master_Data_JA_XX)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/3KR_S4CLD2608_Master_Data_JA_XX.docx`, extracted with `mammoth`. Grouped under **EWM Storage Bins and Fixed Bin Assignments** in Inventory, Warehouse and Transportation. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

| <!-- image omitted: unnamed --> | マスタデータスクリプトSAP S/4HANA Cloud Public Edition - 02-07-26 |
| --- | --- |
|  | 棚番および固定保管棚の割当の更新 - MDS (3KR) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

目次

[1 目的 2](#_Toc233891582)

[2 前提条件 3](#_Toc233891583)

[2.1 システムアクセス 3](#_Toc233891584)

[2.2 ロール 3](#_Toc233891585)

[2.3 必須の組織ユニット 3](#_Toc233891586)

[2.4 必須マスタデータおよび任意マスタデータ 4](#_Toc233891587)

[3 概要テーブル 5](#_Toc233891588)

[4 テスト手順 6](#_Toc233891589)

[4.1 棚番の登録 6](#_Toc233891590)

[4.2 棚番変更 7](#_Toc233891591)

[4.3 棚番照会 8](#_Toc233891592)

[4.4 棚番に対する一括変更の実行 9](#_Toc233891593)

[4.5 固定棚割当 10](#_Toc233891594)

## 目的

この文書では、倉庫棚番および固定棚番割当を登録するために、以下のアクティビティを実行する方法について学習します。

- [棚番の登録](#unique_2) [ ページ] 6
- [棚番変更](#unique_3) [ ページ] 7
- [棚番照会](#unique_4) [ ページ] 8
- [棚番に対する一括変更の実行](#unique_5) [ ページ] 9
- [固定棚割当](#unique_6) [ ページ] 10

テキストには、標準的なシステム環境で処理するマスタデータに関連するデータセグメントが含まれています。主に、入力値を入力する必要があるデータセグメントおよび項目について学習します。SAP Best Practices による SAP S/4HANA コンテンツ提供の範囲に関連しない項目については、画面に表示される場合でもこの文書では説明していません。

このマスタデータは、すべての倉庫管理ビジネスプロセスに使用します。

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

マスタデータレコードは、他のマスタデータを参照する場合があります。以下の表は、<type> マスタデータレコードで使用される、任意および必須のマスタデータオブジェクトの概要を示しています。

| マスタデータオブジェクト | データセグメントでの使用 | 必須/任意 | コメント |
| --- | --- | --- | --- |
| ビジネスパートナ | 固定保管棚割当 | 必須 | 倉庫の処分対象当事者としてのビジネスパートナ |

## 概要テーブル

このマスタレコードは、以下の表に示されている複数のセグメントで構成されます。

|  |
| --- |
| 注記 システム管理者が SAP Fiori ラウンチパッドでスペースおよびページを有効化している場合、ホームページには、ビジネスロールの一般的なタスクを実行するために必要なアプリのみが含まれます。ホームページに含まれていないその他すべての (検索可能な) アプリは、検索バーを使用して見つけることができます ([2434549](https://me.sap.com/notes/2434549))。ホームページをパーソナライズして非表示のアプリを含める場合は、ユーザプロファイルにナビゲートし、アプリファインダを選択します。 |

| セグメント | ビジネスロール | アプリ/トランザクション | 予想される結果 |
| --- | --- | --- | --- |
| [棚番の登録](#unique_2) [ ページ] 6 | 倉庫担当者 (EWM) | 棚番登録 (/SCWM/LS01) | 棚番が登録されます。 |
| [棚番変更](#unique_3) [ ページ] 7 | 倉庫担当者 (EWM) | 棚番編集 (/SCWM/LS02) | 棚番が変更されます。 |
| [棚番照会](#unique_4) [ ページ] 8 | 倉庫担当者 (EWM) | 棚番照会 (/SCWM/LS03) | 棚番が表示されます。 |
| [棚番に対する一括変更の実行](#unique_5) [ ページ] 9 | 倉庫担当者 (EWM) | 棚番一括編集 (/SCWM/LS11) | 棚番の一括変更が行われます。 |
| [固定棚割当](#unique_6) [ ページ] 10 | 倉庫担当者 (EWM) | 固定保管棚割当 (/SCWM/BINMAT) | 固定保管棚割当が登録されます。 |

## テスト手順

このセクションには、このマスタレコードに含まれる各セグメントまたはプロセスステップの手順が記載されています。

### 棚番の登録

目的

このセクションでは、SAP Fiori ラウンチパッドを使用して SAP S/4HANA で棚番を登録する方法について説明されています。

手順

| テストステップ番号 | テストステップ名 | 指示 | 予想される結果 | コメント |
| --- | --- | --- | --- | --- |
| 1 | ログオン | SAP Fiori ラウンチパッドに倉庫担当者 (EWM)としてログオンします。 |  |  |
| 2 | アプリにアクセスする | 棚番登録 (/SCWM/LS01)を開きます。 |  |  |
| 3 | 棚番 ID を入力する | 棚番登録 (/SCWM/LS01)画面で、次のデータを入力します。倉庫番号: <各自の倉庫番号>棚番: <棚番 ID>Enterを選択します。 |  |  |
| 4 | 棚番属性を入力する | 棚番タブで、以下のデータを入力します。保管域タイプ: <保管域タイプ>注記 保管域タイプのみが必須項目です。以下のその他すべての項目はオプションです。最大重量最大容積棚番通路X 座標棚Y 座標棚番レベルZ 座標棚番角度 |  |  |
| 5 | データを保存する | 保存を選択します。 | システムメッセージによって、棚番が保存されたことが通知されます。 |  |

### 棚番変更

目的

このセクションでは、SAP Fiori ラウンチパッドを使用し、SAP S/4HANA で棚番を変更します。

手順

| テストステップ番号 | テストステップ名 | 指示 | 予想される結果 | コメント |
| --- | --- | --- | --- | --- |
| 1 | ログオン | SAP Fiori ラウンチパッドに倉庫担当者 (EWM)としてログオンします。 |  |  |
| 2 | アプリにアクセスする | 棚番編集 (/SCWM/LS02)を開きます。 |  |  |
| 3 | 棚番 ID を入力する | 棚番編集 (/SCWM/LS02)画面で、次のデータを入力します。倉庫番号: <各自の倉庫番号>棚番: <棚番 ID>Enterを選択します。 |  |  |
| 4 | 棚番属性を変更する | 棚番タブで、必要に応じて以下の値を変更します。注記 以下の項目のみを変更することができます。最大重量最大容積棚番通路X 座標棚Y 座標棚番レベルZ 座標棚番角度 |  |  |
| 5 | データを保存する | 保存を選択します。 | システムメッセージによって、棚番が保存されたことが通知されます。 |  |

### 棚番照会

目的

このセクションでは、SAP Fiori ラウンチパッドを使用し、SAP S/4HANA で棚番を照会します。

手順

| テストステップ番号 | テストステップ名 | 指示 | 予想される結果 | コメント |
| --- | --- | --- | --- | --- |
| 1 | ログオン | SAP Fiori ラウンチパッドに倉庫担当者 (EWM)としてログオンします。 |  |  |
| 2 | アプリにアクセスする | 棚番照会 (/SCWM/LS03)を開きます。 |  |  |
| 3 | 棚番 ID を入力する | 棚番照会 (/SCWM/LS03)画面で、次のデータを入力します。倉庫番号: <各自の倉庫番号>棚番: <棚番 ID>Enterを選択します。 | 棚番属性が表示されます。 |  |

### 棚番に対する一括変更の実行

目的

このセクションでは、SAP Fiori ラウンチパッドを使用し、SAP S/4HANA で棚番に対する一括変更を実行します。

手順

| テストステップ番号 | テストステップ名 | 指示 | 予想される結果 | コメント |
| --- | --- | --- | --- | --- |
| 1 | ログオン | SAP Fiori ラウンチパッドに倉庫担当者 (EWM)としてログオンします。 |  |  |
| 2 | アプリにアクセスする | 棚番一括編集 (/SCWM/LS11)を開きます。 |  |  |
| 3 | フィルタ基準を入力する | 倉庫番号 XXXX での棚番の一括変更画面で、以下のデータを入力します。倉庫番号: <各自の倉庫番号>以下の値は選択またはフィルタ基準として入力できます。棚番: <棚番 ID>から<棚番 ID>保管域タイプ: <保管域タイプ ID> から <保管域タイプ ID>ブロック中ステータス:注記 動的選択チェックボックスを選択すると、棚番選択に対して複数のフィルタを選択できます。実行を選択します。 | 選択基準に一致する棚棚の一覧が表示されます。 |  |
| 4 | 棚番を一括変更する | 対応するチェックボックスを選択して、任意のエントリを選択します。削除を選択して、一度に複数の棚番を削除します。または編集を選択して、複数の棚番を同時に変更します。棚番の以下の属性を変更することができます。最大重量最大容積棚番通路棚棚番レベル棚番角度 |  |  |
| 5 | データを保存する | 保存を選択します。 | システムメッセージによって、棚番の変更が保存されたことが通知されます。 |  |

### 固定棚割当

目的

このセクションでは、SAP Fiori ラウンチパッドを使用し、SAP S/4HANA で固定保管棚割当を実行します。

手順

| テストステップ番号 | テストステップ名 | 指示 | 予想される結果 | コメント |
| --- | --- | --- | --- | --- |
| 1 | ログオン | SAP Fiori ラウンチパッドに倉庫担当者 (EWM)としてログオンします。 |  |  |
| 2 | アプリにアクセスする | 固定保管棚割当 (/SCWM/BINMAT)を開きます。 |  |  |
| 3 | フィルタ基準を入力する | 固定保管棚の更新画面で、以下のデータを入力します。倉庫番号: <各自の倉庫番号>製品: <製品 ID>から<製品 ID>処分対象当事者: <ビジネスパートナ> から < ビジネスパートナ ID>注記 処分対象当事者は、倉庫番号で更新されているビジネスパートナです。棚番: <棚番 ID>から<棚番 ID>保管域タイプ: <保管域タイプ ID> から <保管域タイプ ID>実行を選択します。 | 選択基準に一致する割り当てられた固定棚の一覧が表示されます。 |  |
| 4 | 固定棚割当を登録する | 倉庫番号 XXXX: 固定保管棚照会画面で編集を選択します。倉庫番号 XXXX: 固定保管棚の更新画面で登録を選択します。新しく登録された行で、以下の値を入力します。処分: <処分対象当事者のビジネスパートナ ID>棚番: <固定保管棚 ID>タイプ: <固定棚保管タイプ ID>製品: <製品 ID>最大数量: <数量>UoM 照会: <最大数量の数量単位> 個など最小数量: <数量>UoM 照会: <最小数量の数量単位> 個など倉庫製品マスタデータを更新してある場合、以下の項目の値:棚番の最大数最大数量最小数量最大/最小数量の UoM 照会固定棚割当の最大数量および最小数量の値は、倉庫製品マスタデータの最大数量、最小数量、および棚番の最大数の値に基づいて計算されます。UoM 照会も、倉庫製品マスタデータから求められます。 |  |  |
| 5 | データを保存する | 保存を選択します。 | システムメッセージによって、棚番が保存されたことが通知されます。 |  |

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
- related-to :: [[11-inventory-warehouse-and-transportation/maintain-storage-bins-and-fixed-bin-assignments-mds-3kr-335]]
- related-to :: [[11-inventory-warehouse-and-transportation/mds-3kr-339]]
- related-to :: [[11-inventory-warehouse-and-transportation/script-de-dados-mestre-atualizar-posicoes-no-deposito-e-atribuicoes-de]]
- related-to :: [[11-inventory-warehouse-and-transportation/script-de-datos-maestros-actualizar-ubicaciones-y-asignaciones-de-ubic]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/3KR_S4CLD2608_Master_Data_JA_XX.docx` — full document · extracted with `mammoth` · 9,019 chars in the whole document
