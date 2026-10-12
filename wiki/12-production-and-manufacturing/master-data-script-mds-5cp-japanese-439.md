---
id: 12-production-and-manufacturing/master-data-script-mds-5cp-japanese-439
title: "目的 (Master Data Script: 生産資源/治工具の登録 - MDS 5CP, Japanese) (5CP_S4CLD2608_Master_Data_JA_XX)"
description: "Japanese master data script (5CP) for SAP S/4HANA Cloud 2608: creating production resources/tools (PRT) as material, other, document and equipment PRTs and assigning them to routings and orders."
cluster: 12-production-and-manufacturing
tags: [kb/production-and-manufacturing, topic/production-resources-tools]
aliases: [5CP_S4CLD2608_Master_Data_JA_XX]
keywords: [Production Resources/Tools (PRTs), production resources and tools, prt master data, prt status, prt control key, routing prt assignment, production order prt assignment, document prt, equipment prt, business roles]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/5CP_S4CLD2608_Master_Data_JA_XX.docx]
confidence: low
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-439
topic: 12-production-and-manufacturing/production-resources-tools
language: JA
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# 目的 (Master Data Script: 生産資源/治工具の登録 - MDS 5CP, Japanese) (5CP_S4CLD2608_Master_Data_JA_XX)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/5CP_S4CLD2608_Master_Data_JA_XX.docx`, extracted with `mammoth`. Grouped under **Production Resources/Tools (PRTs)** in Production and Manufacturing. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

| <!-- image omitted: unnamed --> | マスタデータスクリプトSAP S/4HANA Cloud Public Edition - 02-07-26 |
| --- | --- |
|  | 生産資源/治工具の登録 - MDS (5CP) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

目次

[1 目的 2](#_Toc233891741)

[2 前提条件 3](#_Toc233891742)

[2.1 システムアクセス 3](#_Toc233891743)

[2.2 ロール 3](#_Toc233891744)

[2.3 必須の組織ユニット 4](#_Toc233891745)

[2.4 必須マスタデータおよび任意マスタデータ 4](#_Toc233891746)

[2.5 データ登録の主要パラメータ 4](#_Toc233891747)

[2.5.1 PRT ステータス 4](#_Toc233891748)

[2.5.2 PRT 管理キー 5](#_Toc233891749)

[3 概要テーブル 6](#_Toc233891750)

[4 手順 7](#_Toc233891751)

[4.1 生産資源/治工具の登録 7](#_Toc233891752)

[4.1.1 品目 PRT の登録 7](#_Toc233891753)

[4.1.2 その他 PRT の登録 8](#_Toc233891754)

[4.1.3 文書 PRT の登録 10](#_Toc233891755)

[4.1.4 設備 PRT の登録 11](#_Toc233891756)

[4.2 作業手順での PRT の割当 (オプション) 12](#_Toc233891757)

[4.3 製造指図での PRT の割当 (オプション) 14](#_Toc233891758)

[5 付録 17](#_Toc233891759)

## 目的

この文書では、SAP S/4HANA Cloud Private Editionシステムで生産資源/治工具マスタデータレコードを登録する方法について説明します。機械や固定資産とは異なり、PRT (生産資源/治工具) は、活動の実行に必要であり、繰り返し使用できる動産 (不動ではない) 作業資源です。

生産資源/治工具には、いくつかのカテゴリがあります。カテゴリによって、PRT で使用できる特性およびビジネス機能が決まります。

このマスタデータスクリプトの指示で、独自の PRT を登録することができます。

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

| 名称 (ロールテンプレート) | ID (ロールテンプレート) | 名称 (ラウンチパッド領域) | ID (ラウンチパッド領域) | ログオンする |
| --- | --- | --- | --- | --- |
| 生産エンジニア - ディスクリート製造 | SAP_BR_PRODN_ENG_DISC | 生産エンジニアリング - ディスクリート製造 | SAP_BR_PRODN_ENG_DISC |  |
| 製造責任者 - ディスクリート製造 | SAP_BR_PRODN_SUPERVISOR_DISC | 生産管理 - ディスクリート製造 | SAP_BR_PRODN_SUPERVISOR_DISC |  |
| マスタデータスペシャリスト - 製品データ | SAP_BR_PRODMASTER_SPECIALIST | マスタデータ - 製品/製品ガバナンス | SAP_BR_PRODMASTER_SPECIALIST / SAP_CMD_SPT_PR_GOV_PC |  |
| デザインエンジニア | SAP_BR_DESIGN_ENGINEER | 文書管理 | SAP_BR_DESIGN_ENGINEER |  |
| 保全計画者 | SAP_BR_MAINTENANCE_PLANNER | 保全計画 | SAP_BR_MAINTENANCE_PLANNER |  |

### 必須の組織ユニット

品目マスタデータの一部のセグメントは会社の組織ユニットに依存し、一般 (共通) データは組織ユニットまたは会社コードに依存しません。以下の表は、さまざまなデータセグメントおよび関連する組織ユニットの概要を示しています。

| データセグメント | 依存対象 | 項目例 | コメント | 使用される組織ユニット |
| --- | --- | --- | --- | --- |
| 全データ | プラント |  | すべてのデータはプラントによって異なります。 | プラント:____________ |

### 必須マスタデータおよび任意マスタデータ

参照作業手順データレコードは、他のマスタデータを参照する場合があります。以下の表は、参照作業手順で使用される、任意および必須のマスタデータオブジェクトの概要を示しています。

| マスタデータオブジェクト | データセグメントでの使用 | 必須/任意 | コメント |
| --- | --- | --- | --- |
| 作業手順 | 作業手順での PRT の割当 | 任意 | 作業手順があり、その作業手順に PRT を割り当てると仮定します。 |

### データ登録の主要パラメータ

このセクションでは、マスタレコードの動作に影響し、PRT マスタデータレコードの登録に常に必要となる基本パラメータの一部について説明します。

#### PRT ステータス

PRT ステータスによって、生産資源/治工具の用途が管理されます。PRT ステータスに応じて、生産資源/治工具を PRT 更新の各種タスクに対して承認することができます。

| PRT ステータス | 内容説明 |
| --- | --- |
| 01 | 登録日付 |
| 02 | 生産資源/治工具用途計画に承認済 |
| 03 | 生産に承認済 |

#### PRT 管理キー

PRT 管理キーにより、PRT をタスクリストに割り当てるか、指図を以下のビジネス機能に含めるかが決定されます。

| PRT 管理プロファイル | 内容説明 |
| --- | --- |
| 1 | 全機能 |
| 2 | 印刷する |

## 概要テーブル

このスコープアイテムは、以下の表に示されている複数のプロセスステップで構成されます。

|  |
| --- |
| 注記 システム管理者が SAP Fiori ラウンチパッドでスペースおよびページを有効化している場合、ホームページには、ビジネスロールの一般的なタスクを実行するために必要なアプリのみが含まれます。ホームページに含まれていないその他すべての (検索可能な) アプリは、検索バーを使用して見つけることができます ([2434549](https://me.sap.com/notes/2434549))。ホームページをパーソナライズして非表示のアプリを含める場合は、ユーザプロファイルにナビゲートし、アプリファインダを選択します。 |

| プロセスステップ | ビジネスロール | トランザクション/アプリ | 予想される結果 |
| --- | --- | --- | --- |
| [品目 PRT の登録](#unique_11) [ ページ] 7 | マスタデータスペシャリスト - 製品データ | 品目登録(MM01) |  |
| [その他 PRT の登録](#unique_12) [ ページ] 8 | 生産エンジニア - ディスクリート製造 | 生産資源および治工具の管理(F7653) |  |
| [文書 PRT の登録](#unique_13) [ ページ] 10 | デザインエンジニア | 伝票管理 (F2733) |  |
| [設備 PRT の登録](#unique_14) [ ページ] 11 | 保全計画者 | 技術対象登録(W0029) |  |
| [作業手順での PRT の割当 (オプション)](#unique_15) [ ページ] 12 | 生産エンジニア - ディスクリート製造 | 作業手順変更(CA02) |  |
| [製造指図での PRT の割当 (オプション)](#unique_16) [ ページ] 14 | 製造責任者 - ディスクリート製造 | 製造指図の変更(CO02) |  |

## 手順

このセクションには、このマスタレコードに含まれる各セグメントまたはプロセスステップの手順が記載されています。

### 生産資源/治工具の登録

#### 品目 PRT の登録

テスト管理

カスタマプロジェクト: プロジェクト固有部分への入力

|  |  |  |  |
| --- | --- | --- | --- |
| テストケース ID | <X.XX> | テスト実施日: |  |
| テスト実施者名: |  | 期間: |  |
| ビジネスロール: |  | 責任者: | <都道府県/州、サービスプロバイダ、カスタマ/共同サービスプロバイダ、およびカスタマ> |

目的

この章では、品目 PRT の登録方法を示します。

手順

| テストステップ番号 | テストステップ名 | 指示 | 予想される結果 | コメント |
| --- | --- | --- | --- | --- |
| 1 | ログオンする | SAP Fiori ラウンチパッドにマスタデータスペシャリスト - 製品データとしてログオンします。 | 開始ページが表示されます。 |  |
| 2 | SAP Fiori アプリを開く | 品目登録(MM01) を開きます。 | 新しいウィンドウが開き、品目登録 (第一画面)が表示されます。 |  |
| 3 | 品目基本データを入力する | 品目登録 (第一画面) で、以下のエントリを入力します。品目: <品目コード> PRT_01など品目タイプ: 生産資源/治工具ビュー選択を選択します。 | ビュー選択ビューが表示されます。 |  |
| 4 | ビューを選択する | ビュー選択画面で、以下のビューを選択します。基本ビュー生産資源/治工具その他の必要なビュー続行を選択します。 |  |  |
| 5 | 組織レベルデータを入力する | 組織レベルビューの組織レベルセクションで、以下のエントリを入力します。プラント: <プラントコード> 1010などEnterを押します。 |  |  |
| 6 | 基本ビューデータを入力する | 基本データ 1タブで、以下のデータを入力します。テキスト: <最終組立の生産資源/治工具>基本数量単位: <EA>生産資源/治工具タブを選択します。 | 基本データが保存されます。 |  |
| 7 | 生産資源/治工具データを入力する | 生産資源/治工具タブで、以下のデータを入力します。PRT 用途: <009>PRT 管理プロファイル: <1>保存を選択します。 | 画面が第一画面に戻ります。品目 PRT_01 が登録されます。 |  |

#### その他 PRT の登録

テスト管理

カスタマプロジェクト: プロジェクト固有部分への入力

|  |  |  |  |
| --- | --- | --- | --- |
| テストケース ID | <X.XX> | テスト実施日: |  |
| テスト実施者名: |  | 期間: |  |
| ビジネスロール: |  | 責任者: | <都道府県/州、サービスプロバイダ、カスタマ/共同サービスプロバイダ、およびカスタマ> |

目的

この章では、その他 PRT を登録する方法を示します。

手順

| テストステップ番号 | テストステップ名 | 指示 | 予想される結果 | コメント |
| --- | --- | --- | --- | --- |
| 1 | ログオンする | SAP Fiori ラウンチパッドに生産エンジニア - ディスクリート製造としてログオンします。 | SAP Fiori ラウンチパッドが表示されます。 |  |
| 2 | SAP Fiori アプリにアクセスする | 生産資源および治工具の管理(F7653)を開きます。 | アプリが開きます。 |  |
| 3 | 登録を選択する | 登録を選択します。 | 新しいウィンドウが開き、PPT 登録画面が表示されます。 |  |
| 4 | 名称を入力する | 以下のエントリを入力します。生産資源/治工具: <名称> (PRT_02など)基本データを選択します。 | 生産資源/治工具登録: 基本データ画面が表示されます。 |  |
| 5 | 基本データを入力する | 登録した生産資源/治工具のテキストを入力します。生産資源/治工具のテキストツールチップを検索し、以下を入力します。<その他 PRT 02>基本データセクションで、以下のエントリを入力します。ステータス: <03>PRT 用途: <009>基本数量単位: <EA>保存を選択します。 | 画面が第一画面に戻ります。生産資源/治工具が登録されます。 |  |

#### 文書 PRT の登録

テスト管理

カスタマプロジェクト: プロジェクト固有部分への入力

|  |  |  |  |
| --- | --- | --- | --- |
| テストケース ID | <X.XX> | テスト実施日: |  |
| テスト実施者名: |  | 期間: |  |
| ビジネスロール: |  | 責任者: | <都道府県/州、サービスプロバイダ、カスタマ/共同サービスプロバイダ、およびカスタマ> |

目的

この章では、文書 PRT の登録方法を示します。

手順

| テストステップ番号 | テストステップ名 | 指示 | 予想される結果 | コメント |
| --- | --- | --- | --- | --- |
| 1 | ログオンする | SAP Fiori ラウンチパッドにデザインエンジニアとしてログオンします。 | 開始ページが表示されます。 |  |
| 2 | SAP Fiori アプリを開く | 伝票管理 (F2733)を開きます。 | 新しいウィンドウが開き、文書管理が表示されます。 |  |
| 3 | 文書を登録する | 登録を選択します。文書画面で、以下のエントリを入力します。文書タイプ: <SPP>文書テキスト: <PRT_03>登録を選択します。 | 文書が登録されます。文書番号を書き留めておきます。 |  |
| 4 | 文書を編集する | 右上隅の編集を選択します。文書データセクションで、文書ステータスを作業中に変更します。オリジナルセクションで、アップロードを選択し、PC から PRT 文書を添付します。保存を選択します。 | 文書が保存されます。 |  |
| 5 | 文書をリリースする | 右上隅の編集を選択します。文書データセクションで、文書ステータスをリリース済に変更します。保存を選択します。 | 文書が保存されます。 |  |

#### 設備 PRT の登録

テスト管理

カスタマプロジェクト: プロジェクト固有部分への入力

|  |  |  |  |
| --- | --- | --- | --- |
| テストケース ID | <X.XX> | テスト実施日: |  |
| テスト実施者名: |  | 期間: |  |
| ビジネスロール: |  | 責任者: | <都道府県/州、サービスプロバイダ、カスタマ/共同サービスプロバイダ、およびカスタマ> |

目的

この章では、設備 PRT を登録する方法を示します。

手順

| テストステップ番号 | テストステップ名 | 指示 | 予想される結果 | 合格/不合格/コメント |
| --- | --- | --- | --- | --- |
| 1. | ログオンする | SAP Fiori ラウンチパッドに保全計画者としてログオンします。 | SAP Fiori ラウンチパッドが表示されます。 |  |
| 2 | SAP Fiori アプリにアクセスする | 技術対象登録(W0029)を開きます。 | アプリが開きます。 |  |
| 3 | 設備を登録する | 技術対象登録画面で、技術対象タイプ: 設備を選択します。次の画面で、以下のように入力します。技術対象タイプ: 設備技術対象: 空白のまま有効開始日付: 本日の日付技術対象カテゴリ: P (生産資源/治工具続行を選択します。 |  |  |
| 4 | 一般データを更新する | 技術対象登録: <設備 ID>画面の一般データセクションで、以下を入力します。内容説明: <PRT 設備など>オプションで、その他の一般データを更新してから、PRT データセクションにナビゲートします。 | 技術対象登録: 一般データ画面が表示されます。 |  |
| 5 | PRT データを更新する | PRT データセクションで、以下を入力します。タスクリスト用途: 009 (全タスクリストタイプ)管理キー: 1 (全機能)オプションで、追加詳細を更新します。たとえば、いくつかの特性とともに割り当てられた計測点を登録した後に、項目計測点に計測点を添付し、項目負荷レコードのチェックボックスを選択することができます。 | 技術対象登録: 場所データ画面が表示されます。 |  |
| 6 | 設備を保存する | オプションで、他のセクションの追加情報を更新することができます。保存を選択します。 | 設備が登録されます。設備番号を書き留めます。 |  |

### 作業手順での PRT の割当 (オプション)

テスト管理

カスタマプロジェクト: プロジェクト固有部分への入力

|  |  |  |  |
| --- | --- | --- | --- |
| テストケース ID | <X.XX> | テスト実施日: |  |
| テスト実施者名: |  | 期間: |  |
| ビジネスロール: |  | 責任者: | <都道府県/州、サービスプロバイダ、カスタマ/共同サービスプロバイダ、およびカスタマ> |

目的

この章では、作業手順で品目 PRT、その他 PRT、文書 PRT、または設備 PRT を割り当てる方法を示します。生産資源/治工具を必要とするタスクリストおよび製造指図に、さまざまなタイプの生産資源/治工具を割り当てることができます。タスクリストに割り当てられた PRT は、製造指図に自動的にコピーされます。

手順

| テストステップ番号 | テストステップ名 | 指示 | 予想される結果 | コメント |
| --- | --- | --- | --- | --- |
| 1 | ログオンする | SAP Fiori ラウンチパッドに生産エンジニア - ディスクリート製造としてログオンします。 | 開始ページが表示されます。 |  |
| 2 | SAP Fiori アプリを開く | 作業手順変更(CA02)を開きます。 | 新しいウィンドウが開き、作業手順変更: 第一画面が表示されます。 |  |
| 3 | 品目を入力する | 以下のエントリを入力し、続行を選択します。品目: <品目コード>プラント: <プラントコード> 1010など | 作業手順変更: 作業概要画面が表示されます。 |  |
| 4 | 作業を選択する | 明細を選択し、作業を選択します。PRT を割り当てる作業を選択します。次に、生産資源/治工具を選択します。 | 作業手順変更: PRT 概要画面が表示されます。 |  |
| 5 | 品目 PRT を割り当てる | 作業に PRT が存在していない場合は、ダイアログ作業手順変更: 新規生産資源/冶工具で以下のエントリを入力します。すでに存在している場合は、品目を選択し、以下のエントリを入力して緑のチェックマークを押します。PRT 明細番号: <0010>品目: <品目コード> PRT_01などプラント: <プラントコード> 1010など | 品目 PRT が作業に割り当てられます。 |  |
| 6 | その他 PRT を割り当てる | その他を選択し、以下のエントリを入力して緑のチェックマークを押します。PRT 明細番号: <0020>生産資源/治工具: <名称> (PRT_02など) | その他 PRT が作業に割り当てられます。 |  |
| 7 | 文書 PRT を割り当てる | 文書を選択し、以下のエントリを入力して緑のチェックマークを押します。PRT 明細番号: <0030>文書: <前のステップで登録した文書番号>文書タイプ: <SPP>文書パート: <000>文書バージョン: <00>数量: <1 EA>管理 Prof.: <1> | 文書 PRT が作業に割り当てられます。 |  |
| 8 | 設備 PRT を割り当てる | 設備を選択し、以下のエントリを入力して緑のチェックマークを選択します。設備: <前のステップで登録した設備番号> |  |  |
| 9 | 変更内容を保存する | 保存を選択します。 | 作業手順が保存されます。 |  |

### 製造指図での PRT の割当 (オプション)

テスト管理

カスタマプロジェクト: プロジェクト固有部分への入力

|  |  |  |  |
| --- | --- | --- | --- |
| テストケース ID | <X.XX> | テスト実施日: |  |
| テスト実施者名: |  | 期間: |  |
| ビジネスロール: |  | 責任者: | <都道府県/州、サービスプロバイダ、カスタマ/共同サービスプロバイダ、およびカスタマ> |

目的

この章では、製造指図の作業に対して品目 PRT、その他 PRT、文書 PRT、または設備 PRT を割り当てる方法を示します。製造指図が事前に登録されていることを確認します。指図の登録時に、作業概要タブで PRT を割り当てることもできます。

手順

| テストステップ番号 | テストステップ名 | 指示 | 予想される結果 | コメント |
| --- | --- | --- | --- | --- |
| 1 | ログオンする | SAP Fiori ラウンチパッドに製造責任者 - ディスクリート製造としてログオンします。 | 開始ページが表示されます。 |  |
| 2 | SAP Fiori アプリにアクセスする | 製造指図の変更(CO02)を開きます。 | 新しいウィンドウが開き、製造指図変更: 第一画面が表示されます。 |  |
| 3 | 指図情報を入力する | 以下のエントリを入力して続行を選択します。指図: <指図番号> | 製造指図登録: 変更画面が表示されます。 |  |
| 4 | 作業を選択する | 作業を選択します。作業概要テーブルで、1 つの作業 (作業 0010など) のチェックボックスを選択し、PRTを選択します。 | 作業に PRT が存在していない場合は、新しいダイアログ製造指図変更: PRT 新規エントリが表示されます。すでに存在している場合は、生産資源/治工具概要テーブルが表示されます。 |  |
| 5 | 品目 PRT を割り当てる | 作業に PRT が存在していない場合は、ダイアログ製造指図変更: PRT 新規エントリで以下のエントリを入力します。すでに存在している場合は、生産資源/治工具概要の下部にある+を選択し、以下のエントリを入力します。明細番号: 0010など品目: PRT_01などプラント: 1010 など緑のチェックマークを選択します。 | 品目 PRT が作業に割り当てられます。 |  |
| 6 | その他 PRT を割り当てる | 生産資源/治工具概要の下部にある+を選択し、その他を選択します。以下のエントリを入力します。明細番号: 0020など生産資源/治工具: PRT_02など緑のチェックマークを選択します。 | その他 PRT が作業に割り当てられます。 |  |
| 7 | 文書 PRT を割り当てる | 生産資源/治工具概要の下部にある+を選択し、文書を選択します。以下のエントリを入力します。明細番号: <0030>文書: <前のステップで登録した文書番号>文書タイプ: <SPP>文書パート: <000>文書バージョン: <00>数量: <1 EA>管理キー: <1>緑のチェックマークを選択します。 | 文書 PRT が作業に割り当てられます。 |  |
| 8 | 設備 PRT を割り当てる | 生産資源/治工具概要の下部にある+を選択し、設備を選択します。以下のエントリを入力します。設備: <前のステップで登録した設備番号>管理プロファイル: 1 (すべての機能)緑のチェックマークを選択します。 |  |  |

## 付録

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

## Suspected conflicts

> [!warning] Conflict
> Flagged while digesting this document, not verified: The purpose text says the script covers 'SAP S/4HANA Cloud Private Edition' while the title and cover say Public Edition.

## Connections
- part-of :: [[_cluster]]
- related-to :: [[12-production-and-manufacturing/master-data-script-create-production-resources-tools-mds-5cp-437]]
- related-to :: [[12-production-and-manufacturing/mds-5cp-441]]
- related-to :: [[12-production-and-manufacturing/script-de-dados-mestre-criar-meio-auxiliar-de-producao-mds-5cp-440]]
- related-to :: [[12-production-and-manufacturing/script-de-datos-maestros-creacion-de-medios-auxiliares-de-fabricacion]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/5CP_S4CLD2608_Master_Data_JA_XX.docx` — full document · extracted with `mammoth` · 13,825 chars in the whole document
