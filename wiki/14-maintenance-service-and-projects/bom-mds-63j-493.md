---
id: 14-maintenance-service-and-projects/bom-mds-63j-493
title: マスタデータスクリプト - サービスの品目および設備 BOM の登録 - MDS (63J) (63J_S4CLD2608_Master_Data_JA_XX)
description: "Japanese SAP S/4HANA Cloud Public Edition 2608 master data script (63J): creating service products, material BOMs, equipment and equipment BOMs."
cluster: 14-maintenance-service-and-projects
tags: [kb/maintenance-service-and-projects, topic/service-technical-objects-and-boms]
aliases: [63J_S4CLD2608_Master_Data_JA_XX]
keywords: [Technical Objects and BOMs for Service, service products, material bom, equipment bom, equipment master data, master data scripts, product master data, sales organization data, business roles, profit center]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/63J_S4CLD2608_Master_Data_JA_XX.docx]
confidence: low
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-493
topic: 14-maintenance-service-and-projects/service-technical-objects-and-boms
language: JA
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# マスタデータスクリプト - サービスの品目および設備 BOM の登録 - MDS (63J) (63J_S4CLD2608_Master_Data_JA_XX)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/63J_S4CLD2608_Master_Data_JA_XX.docx`, extracted with `mammoth`. Grouped under **Technical Objects and BOMs for Service** in Maintenance, Service and Projects. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

| <!-- image omitted: unnamed --> | マスタデータスクリプトSAP S/4HANA Cloud Public Edition - 02-07-26 |
| --- | --- |
|  | サービスの品目および設備 BOM の登録 - MDS (63ジュール) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

目次

[1 目的 2](#_Toc233891815)

[2 前提条件 3](#_Toc233891816)

[2.1 システムアクセス 3](#_Toc233891817)

[2.2 ロール 3](#_Toc233891818)

[2.3 必須の組織ユニット 3](#_Toc233891819)

[2.4 必須のマスタデータおよび操作可能なマスタデータ 4](#_Toc233891820)

[3 概要テーブル 5](#_Toc233891821)

[4 手順 6](#_Toc233891822)

[4.1 品目 BOM 登録 6](#_Toc233891823)

[4.1.1 サービス製品の登録 6](#_Toc233891824)

[4.1.1.1 サービス製品の登録 - SRV_BOM_01_01 6](#_Toc233891825)

[4.1.1.2 サービス製品の登録 - SRV_BOM_02_01 7](#_Toc233891826)

[4.1.1.3 サービス製品の登録 - SRV_BOM_02_02 9](#_Toc233891827)

[4.1.2 新しい部品表/配合表の登録 10](#_Toc233891828)

[4.2 設備 BOM 登録 12](#_Toc233891829)

[4.2.1 設備登録 12](#_Toc233891830)

[4.2.2 設備 BOM 登録 14](#_Toc233891831)

## 目的

この文書では、サービス製品マスタデータレコードを登録する方法、および登録されたサービス製品での部品表/配合表の登録について説明します。この説明には、"通常の" システム環境で処理するマスタデータに関連するデータセグメントが含まれています。読者は、一般に入力値を入力する必要があるデータセグメントおよび項目について主に学習します。この範囲に該当しない項目は、UI に表示される場合でもこの文書では説明していません。

この説明に従って登録されるサービス製品マスタレコードは、サービス契約で使用することができます。

| 製品タイプ | サービス製品 ID | 説明 |
| --- | --- | --- |
| 品目マスタ | SRV_BOM_01_01 | BOM 01_01 のサービス製品 |
|  | SRV_BOM_02_01 | BOM 02_01 のサービス製品 |
|  | SRV_BOM_02_02 | BOM 02_02 のサービス製品 |
| 品目 BOM | SRV_BOM_01_01 | BOM 01_01 のサービス製品 |
| 設備 | <設備 ID> | 設備登録 |
| 設備 BOM | <設備 BOM> | 設備 BOM |

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
| BOM 設計者 | SAP_BR_BOM_ENGINEER | 部品表/配合表 | SAP_BR_BOM_ENGINEER |
| 保全計画者 | SAP_BR_MAINTENANCE_PLANNER | 保全計画 | SAP_BR_MAINTENANCE_PLANNER |

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
| 品目 BOM 登録 | SAP_BR_PRODMASTER_SPECIALIST | 品目登録(MM01) | サービス製品が登録されます。 |
| SAP_BR_BOM_ENGINEER | 部品表/配合表更新 - BOM の登録、変更、紹介 | 品目 BOM が保存されます。 |  |
| 設備 BOM 登録 | SAP_BR_MAINTENANCE_PLANNER | 技術対象登録 | 設備が登録されます。 |
| 設備 BOM 登録 | 設備 BOM が登録されます。 |  |  |

## 手順

このセクションには、このマスタレコードに含まれる各セグメントまたはプロセスステップの手順が記載されています。

### 品目 BOM 登録

#### サービス製品の登録

##### サービス製品の登録 - SRV_BOM_01_01

目的

この品目はクラウドエディションにのみ関連しています。

| テストステップ番号 | テストステップ名 | 指示 | 予想される結果 | コメント |
| --- | --- | --- | --- | --- |
| 1 | ログオンする | SAP Fiori ラウンチパッドにマスタデータスペシャリスト - 製品データ (MDG) としてログオンします。 | ホームページが表示されます。 |  |
| 2 | SAP Fiori アプリにアクセスする | 品目登録タイルを選択します。 | 品目登録 (第一画面) が表示されます。 |  |
| 3 | 品目基本データを更新する (サービス製品用) | 品目登録 (第一画面)で、以下のエントリを入力します。ダイアログウィンドウで、以下を選択します。品目: SRV_BOM_01_01品目タイプ: サービス製品次に続行 (Enter) を選択します。 | 新規サービス製品の基本情報を更新しました。ビュー選択ダイアログウィンドウが表示されます。 |  |
| 4 | ビューを選択する | ビュー選択ダイアログウィンドウで、以下のビューを選択します。基本データ 1販売: 販売組織データ 1販売: 販売組織データ 2次に続行 (Enter)を選択します。 | 組織レベルダイアログウィンドウが表示されます。 |  |
| 5 | 組織レベルを選択する | 組織レベルウィンドウで、以下の値を更新します。販売組織:1710 (国内販売組織 US)流通チャネル: 10 (直販)次に続行 (Enter) を選択します。 | 組織データが選択されました。品目SRV_BOM_01_01登録ビューが表示されます。 |  |
| 6 | 基本データを更新する | 基本データ 1 ビューで、以下の値を更新します。テキスト: BOM 01_01 のサービス製品基本数量単位: HR (時間)品目グループ: P001 (サービス)一般明細CatGrp.: SRVP (サービス製品)次に、保存を選択します。 | 基本データが更新され、サービス製品が保存されます。保存後、品目登録 (第一画面)ビューが表示されます。会社で使用する異なる各言語に対して、対応する製品テキストを言語コードごとに更新する必要があります。 |  |
| 7 | 販売組織データ (1) を更新する | 販売: 販売組織1 ビューで、以下の値を更新します。一般データ現金割引: X <選択済>税データ税分類: 1 (正規税)次にEnterを選択します。 | 販売組織データが更新されます。販売: 販売組織2タブページが表示されます。 |  |
| 8 | 販売組織データ (2) を更新する | 販売: 販売組織2 ビューで、以下のエントリを更新します。明細カテゴリグループ: SRVP (サービス製品)次に、保存を選択します。 | 販売組織データが更新されます。販売: 一般/プラントタブページが表示されます。 |  |

##### サービス製品の登録 - SRV_BOM_02_01

目的

この品目はクラウドエディションにのみ関連しています。

| テストステップ番号 | テストステップ名 | 指示 | 予想される結果 | コメント |
| --- | --- | --- | --- | --- |
| 1 | ログオンする | SAP Fiori ラウンチパッドにマスタデータスペシャリスト - 製品データ (MDG) としてログオンします。 | ホームページが表示されます。 |  |
| 2 | SAP Fiori アプリにアクセスする | 品目登録タイルを選択します。 | 品目登録 (第一画面) が表示されます。 |  |
| 3 | 品目基本データを更新する (サービス製品用) | 品目登録 (第一画面)で、以下のエントリを入力します。ダイアログウィンドウで、以下を選択します。品目: SRV_BOM_02_01品目タイプ: サービス製品次に続行 (Enter) を選択します。 | 新規サービス製品の基本情報を更新しました。ビュー選択ダイアログウィンドウが表示されます。 |  |
| 4 | ビューを選択する | ビュー選択ダイアログウィンドウで、以下のビューを選択します。基本データ 1販売: 販売組織データ 1販売: 販売組織データ 2次に続行 (Enter)を選択します。 | 組織レベルダイアログウィンドウが表示されます。 |  |
| 5 | 組織レベルを選択する | 組織レベルウィンドウで、以下の値を更新します。販売組織:1710 (国内販売組織 US)流通チャネル: 10 (直販)次に続行 (Enter) を選択します。 | 組織データが選択されました。品目 SRV_BOM_ 02_01 登録ビューが表示されます。 |  |
| 6 | 基本データを更新する | 基本データ 1 ビューで、以下の値を更新します。テキスト: BOM 02_01 のサービス製品基本数量単位: HR (時間)品目グループ: P001 (サービス)一般明細CatGrp.: SRVP (サービス製品)次にEnterを選択します。 | 基本データが更新され、サービス製品が保存されます。保存後、品目登録 (第一画面)ビューが表示されます。会社で使用する異なる各言語に対して、対応する製品テキストを言語コードごとに更新する必要があります。 |  |
| 7 | 販売組織データ (1) を更新する | 販売: 販売組織1 ビューで、以下の値を更新します。一般データ現金割引: X <選択済>税データ税分類: 1 (正規税)次にEnterを選択します。 | 販売組織データが更新されます。販売: 販売組織2タブページが表示されます。 |  |
| 8 | 販売組織データ (2) を更新する | 販売: 販売組織2 ビューで、以下のエントリを更新します。明細カテゴリグループ: SRVP (サービス製品)次に、保存を選択します。 | 販売組織データが更新されます。販売: 一般/プラントタブページが表示されます。 |  |

##### サービス製品の登録 - SRV_BOM_02_02

目的

この品目はクラウドエディションにのみ関連しています。

| テストステップ番号 | テストステップ名 | 指示 | 予想される結果 | コメント |
| --- | --- | --- | --- | --- |
| 1 | ログオンする | SAP Fiori ラウンチパッドにマスタデータスペシャリスト - 製品データ (MDG) としてログオンします。 | ホームページが表示されます。 |  |
| 2 | SAP Fiori アプリにアクセスする | 品目登録タイルを選択します。 | 品目登録 (第一画面) が表示されます。 |  |
| 3 | 品目基本データを更新する (サービス製品用) | 品目登録 (第一画面)で、以下のエントリを入力します。ダイアログウィンドウで、以下を選択します。品目: SRV_BOM_02_02品目タイプ: サービス製品次に続行 (Enter) を選択します。 | 新規サービス製品の基本情報を更新しました。ビュー選択ダイアログウィンドウが表示されます。 |  |
| 4 | ビューを選択する | ビュー選択ダイアログウィンドウで、以下のビューを選択します。基本データ 1販売: 販売組織データ 1販売: 販売組織データ 2次に続行 (Enter)を選択します。 | 組織レベルダイアログウィンドウが表示されます。 |  |
| 5 | 組織レベルを選択する | 組織レベルウィンドウで、以下の値を更新します。販売組織:1710 (国内販売組織 US)流通チャネル: 10 (直販)次に続行 (Enter) を選択します。 | 組織データが選択されました。品目 SRV_BOM_02_02 登録ビューが表示されます。 |  |
| 6 | 基本データを更新する | 基本データ 1 ビューで、以下の値を更新します。テキスト: BOM 02_02 のサービス製品基本数量単位: HR (時間)品目グループ: P001 (サービス)一般明細CatGrp.: SRVP (サービス製品)次にEnterを選択します。 | 基本データが更新され、サービス製品が保存されます。保存後、品目登録 (第一画面)ビューが表示されます。会社で使用する異なる各言語に対して、対応する製品テキストを言語コードごとに更新する必要があります。 |  |
| 7 | 販売組織データ (1) を更新する | 販売: 販売組織1 ビューで、以下の値を更新します。一般データ現金割引: X <選択済>税データ税分類: 1 (正規税)次にEnterを選択します。 | 販売組織データが更新されます。販売: 販売組織2タブページが表示されます。 |  |
| 8 | 販売組織データ (2) を更新する | 販売: 販売組織2 ビューで、以下のエントリを更新します。明細カテゴリグループ: SRVP (プロジェクト)次に、保存を選択します。 | 販売組織データが更新されます。販売: 一般/プラントタブページが表示されます。 |  |

#### 新しい部品表/配合表の登録

目的

この品目はクラウドエディションにのみ関連しています。このステップでは、新しい部品表/配合表を登録することができます。

| テストステップ番号 | テストステップ名 | 指示 | 予想される結果 | コメント |
| --- | --- | --- | --- | --- |
| 1 | ログオンする | SAP Fiori ラウンチパッドに BOM 設計者としてログオンします。 | SAP Fiori ラウンチパッドが表示されます。 |  |
| 2 | SAP Fiori アプリにアクセスする | 部品表/配合表の更新 (バージョン 2) - BOM の登録、変更、照会(F1813A)アプリを開きます。 |  |  |
| 3 | BOM 登録を選択する | 部品表/配合表の更新画面で、BOM 登録を選択します。 | BOM 登録ダイアログボックスが表示されます。 |  |
| 4 | BOM ヘッダデータを更新する | BOM 登録ウィンドウで、以下の例と同様のデータを入力し、OK を選択します。例品目: SRV_BOM_01_01BOM 用途: S (サービス管理)有効開始: 本日 | 部品表/配合表の更新画面が表示され、デフォルトで構成品目タブが開きます。 |  |
| 5 | BOM 構成品目データを更新する | BOM 明細番号 0010 行で、以下の例のようにエントリを入力します。例構成品目: SRV_BOM_02_01構成品目数量: 10(Enter キーを押して構成品目および構成品目数量項目を有効化します)注記 明細カテゴリ値は N (非在庫品目) | テーブルの 1 行目にBOM 明細番号 0010、構成品目、構成品目テキスト、および構成品目数量が表示されます。 |  |
| 6 | 追加の BOM 構成品目データを更新する | 以下のエントリを使用して、BOM 明細番号 0020 に対して上記のステップを繰り返します。構成品目: SRV_BOM_02_02構成品目数量: 20 HR(Enter キーを押して構成品目および構成品目数量項目を有効化します)注記 明細カテゴリ値は N (非在庫品目) | テーブルの行にBOM 明細番号 0020、構成品目、構成品目テキスト、および構成品目数量が表示されます。 |  |
| 8 | 明細詳細にナビゲートする | BOM 明細番号 0010行で、テーブルの右端にある詳細矢印をクリックします。部品表/配合表の更新画面の基本詳細タブで、以下の例のようにエントリを入力します。例構成品目数量: 10構成品目数量単位: HR | 入力した明細の詳細セクションを含む部品表/配合表の更新画面が表示されます。 |  |
| 9 | 明細詳細にナビゲートする | BOM 明細番号 0020行で、テーブルの右端にある詳細矢印をクリックします。部品表/配合表の更新画面の基本詳細タブで、以下の例のようにエントリを入力します。例構成品目数量: 20構成品目数量単位: HR | 入力した明細の詳細セクションを含む部品表/配合表の更新画面が表示されます。 |  |
| 10 | 保存を選択する | 部品表/配合表の更新画面で、登録を選択します。 | 部品表/配合表が保存されます。注記 保存すると、BOM ステータスが自動的に 1 (有効) に設定されます。BOM の BOM ステータスを 2 (無効) にする必要がある場合は、部品表/配合表の更新画面でヘッダ詳細表示を選択して、管理データを選択し、BOM ステータスを適切に設定してからもう一度保存します。変更番号は、時系列タブの下に追加されます。 |  |

### 設備 BOM 登録

#### 設備登録

目的

このテストステップでは、機能場所に設置されている設備のレコードを更新します。

| テストステップ番号 | テストステップ名 | 指示 | 予想される結果 | コメント |
| --- | --- | --- | --- | --- |
| 1 | ログオンする | SAP Fiori ラウンチパッドに保全計画者としてログオンします。 | SAP Fiori ラウンチパッドが表示されます。 |  |
| 3 | SAP Fiori アプリにアクセスする | 技術対象登録を開きます。 | 新しいウィンドウが開き、技術対象登録: 第一画面が表示されます。 |  |
| 4 | 設備を登録する | 技術対象登録画面で、技術対象タイプ: 設備を選択します。次の画面で、以下のように入力します。技術対象タイプ: 設備技術対象: 空白のまま有効開始: 本日の日付技術対象カテゴリ: M (機械)続行 (Enter)を選択します。 |  |  |
| 5 | 一般データを更新する | 技術対象登録: <設備 ID>画面の一般データセクションで、以下を入力します。内容説明: 例: サービスの BOM ヘッダの設備オブジェクトタイプ: 9400 など開始日: 本日の日付など製造国/地域: 米国など製造月/年: 2011/04 など製造者製品コード: HZZ-TD B4 など製造業者シリアル番号: HZZ-TD B4/66 など取得値/通貨: 10,000.00/USD など取得日: 2011/04/10 など注記 オプションで、その他の一般データを更新してから、場所データセクションにナビゲートします。 | 技術対象登録: 一般データ画面が表示されます。 |  |
| 6 | 場所データを更新する | 場所データセクションで、以下を入力します。保全プラント: 1710 (米国の場合) など場所: YB_1701 (US の場合) などプラントセクション: YOH (US の場合) など注記 同じ構造に属する技術対象にはすべて同じプラントが割り当てられている必要があります。あるいは、すべての技術対象でプラント情報を空白のままにしておくこともできます。オプションで、住所情報などのその他の詳細を更新します。 | 技術対象登録: 場所データ画面が表示されます。 |  |
| 8 | 組織データを更新する | 組織データセクションで、以下を入力します。計画グループ: 920 (米国の場合) など計画プラント: 1710 (米国の場合) など保全作業区: RES-0100 (米国の場合) など作業区プラント: 1710 (米国の場合) など原価センタ: 17101701 (米国の場合) などオプションで、組織データセクションにある取引先情報などの追加情報を更新することもできます。 | 技術対象登録: 組織データ画面が表示されます。 |  |
| 9 | 設備を保存する | オプションで、他のセクションの追加情報を更新することができます。エントリチェックボタンを選択します。保存を選択します。 | 設備が登録されます。登録された設備 IDを書き留めます。 |  |

#### 設備 BOM 登録

| テストステップ番号 | テストステップ名 | 指示 | 予想される結果 | コメント |
| --- | --- | --- | --- | --- |
| 1 | ログオンする | SAP Fiori ラウンチパッドに保全計画者としてログオンします。 | SAP Fiori ラウンチパッドが表示されます。 |  |
| 2 | SAP Fiori アプリにアクセスする | 設備 BOM 登録を開きます。 | 新しいウィンドウが開き、品目 BOM 登録: 第一画面が表示されます。 |  |
| 3 | 設備を登録する | 設備 BOM 登録: 第一画面で、以下のデータを入力します。設備: 前の章で生成された設備 IDBOM 用途: S続行を選択します。 |  |  |
| 4 | 品目データを更新する | 設備 BOM 登録: 一般明細概要画面の品目セクションで、以下のデータを入力します。構成品目: 品目 ID (SRV_BOM_02_02 など)明細カテゴリ: N (非在庫品目)数量: 10 など数量単位: HR などEnterを選択します。 | 設備 BOM 登録: 一般明細概要画面が表示されます。 |  |
| 5 | 設備を保存する | 保存を選択します。 | 設備 BOM が登録されます。 |  |

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
> Flagged while digesting this document, not verified: Step 8 for SRV_BOM_02_02 labels item category group SRVP as 'プロジェクト' (project) whereas the other two service products label SRVP as 'サービス製品'.

## Connections
- part-of :: [[_cluster]]
- related-to :: [[14-maintenance-service-and-projects/master-data-script-create-material-and-equipment-bom-for-service-mds-6]]
- related-to :: [[14-maintenance-service-and-projects/material-und-equipmentstuckliste-fur-service-anlegen-sds-63j-490]]
- related-to :: [[14-maintenance-service-and-projects/mds-63j-495]]
- related-to :: [[14-maintenance-service-and-projects/script-de-dados-mestre-criar-lista-tecnica-de-material-e-equipamento-p]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/63J_S4CLD2608_Master_Data_JA_XX.docx` — full document · extracted with `mammoth` · 13,700 chars in the whole document
