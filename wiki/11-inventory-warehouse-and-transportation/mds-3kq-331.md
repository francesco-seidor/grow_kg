---
id: 11-inventory-warehouse-and-transportation/mds-3kq-331
title: 倉庫製品属性の更新 - MDS (3KQ) (3KQ_S4CLD2608_Master_Data_JA_XX)
description: Japanese master data script (3KQ) for updating warehouse-relevant product attributes via Warehouse Monitor (mass) or Manage Product Master Data (F1602).
cluster: 11-inventory-warehouse-and-transportation
tags: [kb/inventory-warehouse-and-transportation, topic/ewm-warehouse-product-attributes]
aliases: [3KQ_S4CLD2608_Master_Data_JA_XX]
keywords: [EWM Warehouse Product Attributes, warehouse product attributes, warehouse monitor, product master data, mass changes, storage type data, replenishment, business roles, warehouse management, 3KQ]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/3KQ_S4CLD2608_Master_Data_JA_XX.docx]
confidence: high
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-331
topic: 11-inventory-warehouse-and-transportation/ewm-warehouse-product-attributes
language: JA
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# 倉庫製品属性の更新 - MDS (3KQ) (3KQ_S4CLD2608_Master_Data_JA_XX)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/3KQ_S4CLD2608_Master_Data_JA_XX.docx`, extracted with `mammoth`. Grouped under **EWM Warehouse Product Attributes** in Inventory, Warehouse and Transportation. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

| <!-- image omitted: unnamed --> | マスタデータスクリプトSAP S/4HANA Cloud Public Edition - 02-07-26 |
| --- | --- |
|  | 倉庫製品属性の更新 - MDS (3KQ) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

目次

[1 目的 2](#_Toc233891571)

[2 前提条件 3](#_Toc233891572)

[2.1 システムアクセス 3](#_Toc233891573)

[2.2 ロール 3](#_Toc233891574)

[2.3 必須の組織ユニット 3](#_Toc233891575)

[2.4 必須マスタデータおよび任意マスタデータ 4](#_Toc233891576)

[3 概要テーブル 5](#_Toc233891577)

[4 テスト手順 6](#_Toc233891578)

[4.1 倉庫製品属性の更新 - 倉庫モニタ使用 6](#_Toc233891579)

[4.2 倉庫製品属性の更新 7](#_Toc233891580)

## 目的

この文書では、品目/製品マスタの倉庫関連属性の登録方法について学習することができます。倉庫属性を更新する 2 つのオプションがあります。

- 倉庫モニタ(/SCWM/MON) アプリで、倉庫製品属性を更新できます。このアプリは、個別変更および一括変更に使用できます。
- 製品マスタデータ管理(F1602) アプリで、倉庫製品属性を更新できます。このアプリは、個別変更に使用できます。

この文書には、標準的なシステム環境で処理するマスタデータに関連するデータセグメントが含まれています。読者は、一般に入力値を入力する必要があるデータセグメントおよび項目について主に学習します。SAP Best Practices による SAP S/4HANA コンテンツ提供の範囲に関連しない項目については、UI に表示される場合でもこの文書では説明していません。

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
| マスタデータスペシャリスト - 製品データ | SAP_BR_PRODMASTER_SPECIALIST | マスタデータ - 製品/製品ガバナンス | SAP_BR_PRODMASTER_SPECIALIST / SAP_CMD_SPT_PR_GOV_PC |

### 必須の組織ユニット

マスタデータの一部のセグメントは、会社の組織ユニットによって異なります。一般 (共通) データは組織ユニットまたは会社コードに依存しません。以下の表は、さまざまなデータセグメントおよび関連する組織ユニットの概要を示しています。

| データセグメント | 依存対象 | 項目例 | コメント | 使用される組織ユニット |
| --- | --- | --- | --- | --- |
| すべて | 倉庫番号 |  |  |  |

### 必須マスタデータおよび任意マスタデータ

マスタデータレコードは、他のマスタデータを参照する場合があります。以下の表は、<type> マスタデータレコードで使用される、任意および必須のマスタデータオブジェクトの概要を示しています。

| マスタデータオブジェクト | データセグメントでの使用 | 必須/任意 | コメント |
| --- | --- | --- | --- |
| ビジネスパートナ | 倉庫製品属性の更新 | 必須 | 倉庫の処分対象当事者としてのビジネスパートナ |

## 概要テーブル

このマスタレコードは、以下の表に示されている複数のセグメントで構成されます。

|  |
| --- |
| 注記 システム管理者が SAP Fiori ラウンチパッドでスペースおよびページを有効化している場合、ホームページには、ビジネスロールの一般的なタスクを実行するために必要なアプリのみが含まれます。ホームページに含まれていないその他すべての (検索可能な) アプリは、検索バーを使用して見つけることができます ([2434549](https://me.sap.com/notes/2434549))。ホームページをパーソナライズして非表示のアプリを含める場合は、ユーザプロファイルにナビゲートし、アプリファインダを選択します。 |

| セグメント | ビジネスロール | アプリ/トランザクション | 予想される結果 |
| --- | --- | --- | --- |
| [倉庫製品属性の更新 - 倉庫モニタ使用](#unique_7) [ ページ] 6 | 倉庫担当者 (EWM) | 倉庫モニタ(/SCWM/MON) | 倉庫製品の一括変更が実行されます。 |
| [倉庫製品属性の更新](#unique_8) [ ページ] 7 | マスタデータスペシャリスト - 製品データ | 製品マスタデータ管理(F1602) | 品目マスタデータの倉庫属性が登録されます。 |

## テスト手順

このセクションには、このマスタレコードに含まれる各セグメントまたはプロセスステップの手順が記載されています。

### 倉庫製品属性の更新 - 倉庫モニタ使用

目的

このセクションでは、倉庫モニタ(/SCWM/MON) アプリを使用して倉庫製品属性を更新します。このアプリは、個別変更および一括変更に使用できます。

手順

| テストステップ番号 | テストステップ名 | 指示 | 予想される結果 | コメント |
| --- | --- | --- | --- | --- |
| 1 | ログオン | SAP Fiori ラウンチパッドに倉庫担当者 (EWM)としてログオンします。 |  |  |
| 2 | アプリにアクセスする | 倉庫モニタ(/SCWM/MON)を開きます。 | 倉庫管理モニタ SAP - 倉庫番号 XX50画面が表示されます。 |  |
| 3 | メニューを選択する | 左の画面領域にある階層で、製品マスタデータ > 倉庫属性の順に選択します。 |  |  |
| 4 | 製品番号を入力する | /SCWM/SAPLPROD_OVERVIEW ダイアログボックスで、以下のデータを入力します。基本属性セクション:製品番号: <製品番号> から <製品番号>追加オプションセクション:倉庫データのない製品のみ: X実行を選択します。 | 倉庫データでまだ更新されていない製品が、右の画面領域に表示されます。 |  |
| 5 | 製品を選択する | 倉庫属性領域で、製品を選択し、追加メソッド > 一括変更/登録の順に選択します。 |  |  |
| 6 | 製品を選択する | /SCWM/SAPLPROD_OVERVIEWダイアログボックスで、該当する場合は、以下のデータを入力します。倉庫データセクション:在庫受入管理区分在庫払出管理区分平置保管区分循環棚卸区分処理タイプ決定区分実行を選択します。注記 Cloud 倉庫管理では、在庫受入管理区分と在庫払出管理区分は通常、同じ値で更新されます。ただし、倉庫で使用される補充プロセスでは、プロセスを有効にするために、この 2 つの項目は別々に更新される必要があります。 |  |  |
| 7 | データを保存する | ダイアログボックスで、変更を確認します。 | システムメッセージによって、製品が正常に保存されたことが通知されます。 |  |

### 倉庫製品属性の更新

目的

このセクションでは、製品マスタデータ管理(F1602) アプリでの倉庫製品属性の更新方法について説明しています。このアプリは、個別変更に使用できます。

手順

| テストステップ番号 | テストステップ名 | 指示 | 予想される結果 | コメント |
| --- | --- | --- | --- | --- |
| 1 | ログオンする | SAP Fiori ラウンチパッドにマスタデータスペシャリスト - 製品データとしてログオンします。 |  |  |
| 2 | アプリにアクセスする | 製品マスタデータ管理(F1602)を開きます。 |  |  |
| 3 | 品目コードを入力する | 製品マスタデータ管理(F1602) 画面で、次のデータを入力します。製品: <品目コード>Goを選択します。 | 品目マスタデータが製品セクションに表示されます。 |  |
| 4 | 品目を選択する | 品目マスタデータの行を選択します。 |  |  |
| 5 | 倉庫管理を選択する | 製品画面で、倉庫管理タブを選択し、倉庫管理 > 倉庫に移動します。 |  |  |
| 6 | 品目マスタデータを編集する | 製品画面で、編集を選択します。 |  |  |
| 7 | 倉庫データを追加する | 倉庫セクションで、倉庫の倉庫番号を選択します。倉庫番号が存在しない場合は、登録を選択します。 |  |  |
| 8 | 値を入力する | 倉庫画面で、次のデータを入力します。一般情報セクションで、以下の操作を行います。倉庫: <EWM 倉庫番号>処分対象当事者: <処分対象当事者のビジネスパートナ ID>処理タイプ決定区分循環棚卸区分注記 入力が必須なのは、倉庫および処分対象当事者のみです。以下の値はオプションです。在庫受入セクション:在庫受入管理区分在庫払出セクション:在庫払出管理区分注記 Cloud 倉庫管理では、在庫受入管理区分と在庫払出管理区分は同じ値で更新されます。ただし、倉庫で使用される補充プロセスでは、プロセスを有効にするために、この 2 つの項目は別々に更新される必要があります。 |  |  |
|  | 補充保管域タイプデータを登録する | 保管域タイプセクションで、登録を選択します。新規レコード - 保管域タイプ画面で、次のデータを入力します。一般情報セクション:保管域タイプ: <保管域タイプ>棚番の最大数: <棚番数>補充セクション:最小補充数量/表示数量単位: <数量>/<数量単位>最小数量/表示数量単位: <数量>/<数量単位>最大数量/表示数量単位: <数量>/<数量単位> |  |  |
| 9 | データを保存する | 適用を選択します。 | 倉庫データが保存されます。 |  |
| 10 | 製品画面に戻る | 製品画面に戻ります。 |  |  |
| 11 | 倉庫管理を選択する | 製品画面で、プラントタブを選択します。 |  |  |
| 12 | プラントデータを追加する | プラントセクションで、プラントを選択します。プラントが存在しない場合は、登録を選択します。 |  |  |
| 13 | 値を入力する | プラント画面で、一般情報セクションに以下のデータを入力します。シリアル番号プロファイル: <シリアル番号プロファイル> |  |  |
| 14 | データを保存する | 適用を選択します。 | プラントデータが保存されます。 |  |

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
- related-to :: [[11-inventory-warehouse-and-transportation/actualizar-atributos-de-productos-de-almacen-mds-3kq-es-330]]
- related-to :: [[11-inventory-warehouse-and-transportation/attribute-fur-lagerprodukte-pflegen-sds-3kq-328]]
- related-to :: [[11-inventory-warehouse-and-transportation/master-data-script-maintain-warehouse-products-attributes-3kq-329]]
- related-to :: [[11-inventory-warehouse-and-transportation/mds-3kq-333]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/3KQ_S4CLD2608_Master_Data_JA_XX.docx` — full document · extracted with `mammoth` · 8,045 chars in the whole document
