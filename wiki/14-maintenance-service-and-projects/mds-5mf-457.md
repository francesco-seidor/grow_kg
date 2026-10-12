---
id: 14-maintenance-service-and-projects/mds-5mf-457
title: "マスタデータスクリプト: 設備の登録 - MDS (5MF) (5MF_S4CLD2608_Master_Data_JA_XX)"
description: "Japanese master data script (MDS 5MF) for creating equipment master records in SAP S/4HANA Cloud Public Edition 2608 using the Create Technical Object app, incl. installation at a functional location."
cluster: 14-maintenance-service-and-projects
tags: [kb/maintenance-service-and-projects, topic/equipment]
aliases: [5MF_S4CLD2608_Master_Data_JA_XX]
keywords: [Equipment Master Records, equipment master data, technical objects, master data scripts, functional location installation, maintenance planning, business roles, maintenance work centers, cost centers, 5MF]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/5MF_S4CLD2608_Master_Data_JA_XX.docx]
confidence: high
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-457
topic: 14-maintenance-service-and-projects/equipment
language: JA
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# マスタデータスクリプト: 設備の登録 - MDS (5MF) (5MF_S4CLD2608_Master_Data_JA_XX)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/5MF_S4CLD2608_Master_Data_JA_XX.docx`, extracted with `mammoth`. Grouped under **Equipment Master Records** in Maintenance, Service and Projects. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

| <!-- image omitted: unnamed --> | マスタデータスクリプトSAP S/4HANA Cloud Public Edition - 02-07-26 |
| --- | --- |
|  | 設備の登録 - MDS (5MF) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

目次

[1 目的 2](#_Toc233891763)

[2 前提条件 3](#_Toc233891764)

[2.1 システムアクセス 3](#_Toc233891765)

[2.2 ロール 3](#_Toc233891766)

[2.3 必須の組織ユニット 3](#_Toc233891767)

[2.4 必須マスタデータおよび任意マスタデータ 4](#_Toc233891768)

[3 概要テーブル 5](#_Toc233891769)

[4 データ登録の主要パラメータ 6](#_Toc233891770)

[4.1 技術対象カテゴリ 6](#_Toc233891771)

[5 手順 7](#_Toc233891772)

[5.1 設備登録 7](#_Toc233891773)

## 目的

この文書では、S/4HANA システムの設備マスタデータレコードを登録する詳細な手順について説明します。この文書には、標準的なシステム環境で処理するマスタデータに関連するデータセグメントが含まれています。また、この文書には、入力値を必要とするデータセグメントおよび項目に関する情報も記載されています。

SAP Best Practices による S/4 HANA コンテンツ配信の範囲に関連しない項目については、UI に表示される場合もありますが、この文書では説明されていません。

## 前提条件

このセクションでは、設備を登録するためのすべての前提条件の概要を示します。

### システムアクセス

テストは以下のシステムを使用して実施する必要があります。

表 1:

| システム | 詳細 |
| --- | --- |
| システム | SAP Fiori ラウンチパッドからアクセスすることができます。各自のロールに割り当てられている各種アプリにアクセスするための URL がシステム管理者から提供されます。 |

### ロール

SAP から提供される以下のビジネスロールテンプレートを使用して、ビジネスロールを登録し、それらを個別のテストユーザに割り当てます。

または、利用可能な場合は、SAP から提供される以下のスペースを使用することができます。スペーステンプレートを使用して、必要な事前定義済アプリを含むページのあるスペースを登録し、それをビジネスロールに割り当てます。その後、このビジネスロールを個別のユーザに割り当てます。

詳細については、SAP S/4HANA Cloud Public Editionの[Product Assistance](https://help.sap.com/docs/SAP_S4HANA_CLOUD/53e36b5493804bcdb3f6f14de8b487dd/ec310a8b669a45ca898dc4dd91d97de2.html)でテンプレートからのビジネスロールの作成方法を参照してください。

| 名称 (ロールテンプレート) | ID (ロールテンプレート) | 名称 (スペース) | ID (スペース) |
| --- | --- | --- | --- |
| 保全計画者 | SAP_BR_MD_SPECIALIST_EAM | 保全計画者 | SAP_EAM_SPT_MD_SPECIALIST_PC |

### 必須の組織ユニット

マスタデータの一部のセグメントは、会社の組織ユニットによって異なります。一般 (共通) データは組織ユニットまたは会社コードに依存しません。以下の表は、さまざまなデータセグメントおよび関連する組織ユニットの概要を示しています。

| データセグメント | 依存対象 | 項目例 | コメント | 使用される組織ユニット |
| --- | --- | --- | --- | --- |
| すべてのデータ | プラント |  | 設備のすべてのデータはプラントによって異なります。 | プラント:__________ |

### 必須マスタデータおよび任意マスタデータ

設備データレコードは、他のマスタデータを参照する場合があります。以下の表は、設備で使用される任意および必須のマスタデータオブジェクトの概要を示しています。

| マスタデータオブジェクト | データセグメントでの使用 | 必須/任意 | コメント |
| --- | --- | --- | --- |
| 保全作業区 | 設備マスタユーザインタフェース (UI) の組織データタブの責任セクションで、保全作業区のエントリを確認できます。 | 任意 | 保全作業区は、段取、機械、作業などの一部の値を決定するためのパラメータとして使用されます。 |
| 原価センタ | 設備マスタユーザインタフェース (UI) の組織データタブの責任セクションで、原価センタのエントリを確認できます。 | 任意 | 原価センタは、原価計算のパラメータとして使用されます。 |

## 概要テーブル

|  |
| --- |
| 注記 システム管理者が SAP Fiori ラウンチパッドでスペースおよびページを有効化している場合、ホームページには、ビジネスロールの一般的なタスクを実行するために必要なアプリのみが含まれます。ホームページに含まれていないその他すべての (検索可能な) アプリは、検索バーを使用して見つけることができます ([2434549](https://me.sap.com/notes/2434549))。ホームページをパーソナライズして非表示のアプリを含める場合は、ユーザプロファイルにナビゲートし、アプリファインダを選択します。 |

| プロセスステップ | ビジネスロール | アプリ/トランザクション | 予想される結果 |
| --- | --- | --- | --- |
| [設備登録](#unique_8) [ ページ] 7 | SAP_BR_MD_SPECIALIST_EAM | 技術対象登録(EAMS_WDA_TECHOBJ_OIF (EAMS_WDA_TECHOBJ_OIF_CFG_V2)) | 設備が登録されます。 |

## データ登録の主要パラメータ

このセクションでは、マスタレコードの動作に影響し、設備の登録に必ず必要となる基本パラメータの一部について説明します。

### 技術対象カテゴリ

以下のような用途が考えられます。

- 機械
- デバイス
- 生産資源/治工具
- 得意先設備

表 2:

| 技術対象カテゴリ | 説明 |
| --- | --- |
| M | 機械 |

## 手順

### 設備登録

テスト管理

カスタマプロジェクト: プロジェクト固有部分への入力

|  |  |  |  |
| --- | --- | --- | --- |
| テストケース ID | <X.XX> | テスト実施日: |  |
| テスト実施者名: |  | 期間: |  |
| ビジネスロール: |  | 責任者: | <都道府県/州、サービスプロバイダ、カスタマ/共同サービスプロバイダ、およびカスタマ> |

目的

このテストステップでは、機能場所に設置されている設備のレコードを更新します。

手順

| テストステップ番号 | テストステップ名 | 指示 | 予想される結果 | 合格/不合格/コメント |
| --- | --- | --- | --- | --- |
| 1. | ログオンする | SAP Fiori ラウンチパッドにSAP_BR_MD_SPECIALIST_EAMとしてログオンします。 | SAP Fiori ラウンチパッドが表示されます。 |  |
| 2 | SAP Fiori アプリにアクセスする | 技術対象登録(EAMS_WDA_TECHOBJ_OIF (EAMS_WDA_TECHOBJ_OIF_CFG_V2))を開きます。 | 新しいウィンドウが開き、技術対象登録: 第一画面が表示されます。 |  |
| 3 | 設備を登録する | 技術対象登録画面で、技術対象タイプ: 設備を選択します。次の画面で、以下のように入力します。技術対象タイプ: 設備技術対象: 空白のまま有効開始日付: 本日の日付技術対象カテゴリ: M (技術システム - 標準)続行を選択します。 |  |  |
| 4 | 一般データを更新する | 技術対象登録: <設備 ID>画面の一般データセクションで、以下を入力します。内容説明: <手動遮断弁など>対象タイプ: 9400 など>開始日: <本日の日付など>製造国/地域: <米国など>製造月/年: <04/2011 など>製造者製品コード: <HZZ-TD B4 など>製造業者シリアル番号: <HZZ-TD B4/66 など>取得値/通貨: <10,000.00/USD など>取得日: <2011/04/10 など>オプションで、その他の一般データを更新してから、場所データセクションにナビゲートします。 | 技術対象登録: 一般データ画面が表示されます。 |  |
| 5 | 場所データを更新する | 場所データセクションで、以下を入力します。保全プラント: <1710 (米国の場合) など>場所: <YB_1701 (US の場合) など>プラントセクション: <YOH (US の場合) など>注記 同じ構造に属する技術対象にはすべて同じプラントが割り当てられている必要があります。あるいは、すべての技術対象でプラント情報を空白のままにしておくこともできます。オプションで、住所情報などのその他の詳細を更新します。 | 技術対象登録: 場所データ画面が表示されます。 |  |
| 6 | 組織データを更新する | 組織データセクションで、以下を入力します。計画グループ: <920 (米国の場合) など>計画プラント: <1710 (米国の場合) など>保全作業区: <RES-0100 (米国の場合) など>作業区プラント: <1710 (米国の場合) など>原価センタ: <17101701 (米国の場合) など>オプションで、組織データセクションにある取引先情報などの追加情報を更新することもできます。 | 技術対象登録: 組織データ画面が表示されます。 |  |
| 7 | 設備を保存する | オプションで、他のセクションの追加情報を更新することができます。エントリチェックボタンを選択します。保存を選択します。 | 設備が登録されます。 |  |
| 8 | 機能場所に設備を設置する | 技術対象変更: <設備 ID> 画面で、構造セクションにナビゲートします。構造変更: 設置を選択します。設置場所の変更画面で、以下を入力します。上位技術対象: (1710 など)>位置: <空白のまま>設置日時: <システム提案を保持>OKを選択します。保存を選択します。 |  |  |

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
- related-to :: [[14-maintenance-service-and-projects/crear-equipo-mds-5mf-456]]
- related-to :: [[14-maintenance-service-and-projects/create-equipment-mds-5mf-455]]
- related-to :: [[14-maintenance-service-and-projects/criar-equipamento-mds-5mf-458]]
- related-to :: [[14-maintenance-service-and-projects/equipment-anlegen-sds-5mf-454]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/5MF_S4CLD2608_Master_Data_JA_XX.docx` — full document · extracted with `mammoth` · 7,386 chars in the whole document
