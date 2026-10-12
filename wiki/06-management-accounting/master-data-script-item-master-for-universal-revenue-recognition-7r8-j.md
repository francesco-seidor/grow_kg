---
id: 06-management-accounting/master-data-script-item-master-for-universal-revenue-recognition-7r8-j
title: "目的 (Master Data Script: Item Master for Universal Revenue Recognition, 7R8, Japanese) (7R8_S4CLD2608_Master_Data_JA_XX)"
description: "Japanese master data script (7R8) for creating URR test product master records and condition-record prices for stock-sales, fixed-price project and service contract scenarios."
cluster: 06-management-accounting
tags: [kb/management-accounting, topic/event-based-revenue-recognition-sell-from-stock]
aliases: [7R8_S4CLD2608_Master_Data_JA_XX]
keywords: [Event-Based Revenue Recognition for Sell from Stock, universal revenue recognition, product master data, item pricing, service contract items, fixed-price project items, sell from stock, organizational units, business roles, master data scripts]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/7R8_S4CLD2608_Master_Data_JA_XX.docx]
confidence: low
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-535
topic: 06-management-accounting/event-based-revenue-recognition-sell-from-stock
language: JA
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# 目的 (Master Data Script: Item Master for Universal Revenue Recognition, 7R8, Japanese) (7R8_S4CLD2608_Master_Data_JA_XX)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/7R8_S4CLD2608_Master_Data_JA_XX.docx`, extracted with `mammoth`. Grouped under **Event-Based Revenue Recognition for Sell from Stock** in Management Accounting. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

| <!-- image omitted: unnamed --> | マスタデータスクリプトSAP S/4HANA Cloud Public Edition - 02-07-26 |
| --- | --- |
|  | ユニバーサル収益認識の品目マスタ登録 (7R8) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

目次

[1 目的 2](#_Toc233891844)

[2 前提条件 3](#_Toc233891845)

[2.1 システムアクセス 3](#_Toc233891846)

[2.2 ロール 3](#_Toc233891847)

[2.3 必須の組織ユニット 3](#_Toc233891848)

[3 概要テーブル 5](#_Toc233891849)

[4 在庫販売統合シナリオ (SFS) の品目マスタデータの登録 6](#_Toc233891850)

[4.1 商品: URR_MAT1_NORM 6](#_Toc233891851)

[4.2 ワンタイムサービスのサービス製品: URR_MAT1_SERV 9](#_Toc233891852)

[5 固定価格得意先プロジェクト統合シナリオの品目マスタデータの登録 12](#_Toc233891853)

[5.1 URR_FPPRJ_1 12](#_Toc233891854)

[6 サービス契約統合シナリオの品目マスタデータの登録 15](#_Toc233891855)

[6.1 URR_SRVCONT1 15](#_Toc233891856)

[7 品目の価格設定 17](#_Toc233891857)

[7.1 SFS の商品の価格: URR_MAT1_NORM 17](#_Toc233891858)

[7.2 ワンタイムサービスのサービス製品の価格: URR_MAT1_SERV 19](#_Toc233891859)

[7.3 サービス契約品目の価格: URR_SRVCONT1 21](#_Toc233891860)

## 目的

この文書では、さまざまなユニバーサル収益認識 (URR) 統合シナリオ (在庫からの販売と統合された URR、得意先サービスプロジェクトと統合された URR、サービス契約と統合された URR) の価格を含む品目マスタデータレコードの登録方法について説明します。

このガイドには、URR プロセスで機能するマスタデータに関連するデータセグメントの説明と、データセグメントの入力値を入力する必要がある項目の説明が含まれています。この範囲に該当しないデータセグメントおよび項目は、UI に表示される場合であっても、この文書では説明していません。

この説明に従って登録される品目マスタデータは、URR プロセスで使用することができます。

| 品目マスタ ID | テキスト | 用途 |
| --- | --- | --- |
| URR_MAT1_NORM | URR テスト品目 1 NORM | この品目は、URR 在庫からの販売統合シナリオで使用されます。 |
| URR_MAT2_NORM | URR テスト品目 2 NORM | この品目は、URR 在庫からの販売統合シナリオで使用されます。 |
| URR_MAT1_SERV | URR テスト品目 1 TAD | この品目は、URR 在庫からの販売統合シナリオで使用されます。 |
| URR_FPPRJ_1 | URR テスト品目固定価格得意先プロジェクト | この品目は、URR 得意先プロジェクト統合シナリオで使用されます。 |
| URR_SRVCONT1 | URR テスト品目サービス契約 | この品目は URR サービス契約統合シナリオで使用されます。 |

## 前提条件

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
| マスタデータスペシャリスト - 製品データ | SAP_BR_PRODMASTER_SPECIALIST | マスタデータ - 製品/製品ガバナンス | SAP_BR_PRODMASTER_SPECIALIST / SAP_CMD_SPT_PR_GOV_PC |  |
| 価格設定スペシャリスト | SAP_BR_PRICING_SPECIALIST | 価格管理 | SAP_BR_PRICING_SPECIALIST |  |

### 必須の組織ユニット

マスタデータの一部のセグメントは会社の組織ユニットに依存し、一般 (共通) データは組織ユニットまたは会社コードに依存しません。以下の表は、さまざまなデータセグメントおよび関連する組織ユニットの概要を示しています。

| データセグメント | 依存対象 | DE に使用される組織ユニット | US に使用される組織ユニット |
| --- | --- | --- | --- |
| 品目の登録 | プラント | 1010 (プラント 1 DE) | 1710 (プラント 1 US) |
| 品目の登録 | 販売組織 | 1010 (国内販売組織 DE) | 1710 (国内販売組織 US) |
| 品目の登録 | 流通チャネル | 10 (直販) | 10 (直販) |

## 概要テーブル

このマスタレコードは、以下の表に示されている複数のセグメントで構成されます。

|  |
| --- |
| 注記 システム管理者が SAP Fiori ラウンチパッドでスペースおよびページを有効化している場合、ホームページには、ビジネスロールの一般的なタスクを実行するために必要なアプリのみが含まれます。ホームページに含まれていないその他すべての (検索可能な) アプリは、検索バーを使用して見つけることができます ([2434549](https://me.sap.com/notes/2434549))。ホームページをパーソナライズして非表示のアプリを含める場合は、ユーザプロファイルにナビゲートし、アプリファインダを選択します。 |

表 1: 在庫販売統合シナリオ (SFS) の品目マスタデータの登録

| プロセスステップ | ビジネスロール | アプリ/トランザクション | 予想される結果 |
| --- | --- | --- | --- |
| [商品: URR_MAT1_NORM](#unique_6) [ ページ] 6 | マスタデータスペシャリスト - 製品データ | 品目登録 |  |
| [ワンタイムサービスのサービス製品: URR_MAT1_SERV](#unique_7) [ ページ] 9 | マスタデータスペシャリスト - 製品データ | 品目登録 |  |

表 2: 固定価格得意先プロジェクト統合シナリオの品目マスタデータの登録

| プロセスステップ | ビジネスロール | アプリ/トランザクション | 予想される結果 |
| --- | --- | --- | --- |
| [URR_FPPRJ_1](#unique_8) [ ページ] 12 | マスタデータスペシャリスト - 製品データ | 品目登録 |  |

表 3: サービス契約統合シナリオの品目マスタデータの登録

| プロセスステップ | ビジネスロール | アプリ/トランザクション | 予想される結果 |
| --- | --- | --- | --- |
| [URR_SRVCONT1](#unique_9) [ ページ] 15 | マスタデータスペシャリスト - 製品データ | 品目登録 |  |

表 4: サービス契約統合シナリオの品目マスタデータの登録

| プロセスステップ | ビジネスロール | アプリ/トランザクション | 予想される結果 |
| --- | --- | --- | --- |
| [SFS の商品の価格: URR_MAT1_NORM](#unique_10) [ ページ] 17 | 価格設定スペシャリスト | 品目価格設定 |  |
| [ワンタイムサービスのサービス製品の価格: URR_MAT1_SERV](#unique_11) [ ページ] 19 | 価格設定スペシャリスト | 品目価格設定 |  |
| [サービス契約品目の価格: URR_SRVCONT1](#unique_12) [ ページ] 21 | 価格設定スペシャリスト | 品目価格設定 |  |

## 在庫販売統合シナリオ (SFS) の品目マスタデータの登録

### 商品: URR_MAT1_NORM

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
| 1 | ログオンする | SAP Fiori ラウンチパッドにマスタデータスペシャリスト - 製品データとしてログオンします。 | ホームページが表示されます。 |  |
| 2 | SAP Fiori アプリにアクセスする | 品目登録アプリを選択します (画面にアプリが表示されない場合は、品目登録アプリを検索してみます)。 | 品目登録 (第一画面) が表示されます。 |  |
| 3 | 品目コードおよび品目タイプを入力する | 品目登録 (第一画面) で、以下のエントリを入力します。製品番号: URR_MAT1_NORM品目タイプ: 商品次に続行 (Enter) を選択します。 | 新規品目マスタデータの品目コードおよび品目タイプが入力されています。ビュー選択ダイアログウィンドウが表示されます。 |  |
| 4 | ビューを選択する | ビュー選択ダイアログウィンドウで、以下のビューを選択します。基本データ 1販売: 販売組織データ 1販売: 販売組織データ 2販売: 一般/プラントデータ会計管理 1次に続行 (Enter) を選択します。 | 組織レベルダイアログウィンドウが表示されます。 |  |
| 5 | 組織レベルを選択する | 組織レベルウィンドウで、以下の値を更新します。プラント: 1010 (プラント 1 DE)販売組織: 1010 (国内販売組織 DE)流通チャネル: 10 (直販)次に続行 (Enter) を選択します。 | 組織データが選択されました。基本データ 1ビューが表示されます。 |  |
| 6 | ビューを更新する: 基本データ 1 | 基本データ 1 ビューで、以下の値を更新します。テキスト: URR テスト品目 1 NORM基本数量単位: PC (個)品目グループ: L001 (取引品目)一般明細グループ: NORM (標準明細)総重量: 1正味重量: 1重量単位: KG容積: 1容積単位: M3Enter キーを押します。 | 基本データが更新されます。Enter を押すと、販売: 販売組織 1 ビューが表示されます。 |  |
| 7 | ビューを更新する: 販売: 販売組織1 | 販売: 販売組織1 ビューで、以下の値を更新します。一般データ現金割引: X <選択>税データ税分類: 0次に Enter を選択します。 | 販売組織データ 1 が更新されます。販売: 販売組織2 ビューが表示されます。 |  |
| 8 | ビューを更新する: 販売: 販売組織2 | 販売: 販売組織2 ビューで、以下のエントリを更新します。一般明細カテゴリグループ: NORM (標準明細)明細カテゴリグループ: NORM (標準明細)次に Enter を選択します。 | 販売組織データ 2 が更新されます。販売:一般/プラントビューが表示されます。 |  |
| 9 | ビューを更新する: 販売: 一般/プラント | 販売: 一般/プラントビューで、以下の値を更新します。基本数量単位: PC (個)総重量: 1KG正味重量: 1利用可能在庫確認: NC取引グループ: 0001積載グループ: 0001利益センタ: Y1041次に Enter を選択します。 | 一般販売データが更新されます。会計管理 1 ビューが表示されます。 |  |
| 10 | ビューを更新する: 会計管理 1 | 会計管理 1 ビューの現会計期間データセクションで、以下のエントリを入力します。基本数量単位: PC評価クラス: 3100標準原価: 16期間単価: 16価格単位: 1原価管理: V将来価格: 空次に、保存を選択します。 | 会計データが更新されます。品目マスタデータが保存されます。 |  |
| 11 | テスト用の追加品目マスタデータを登録する (必要な場合) | 命名規則URR_MAT*_NORM (URR_MAT2_NORM、URR_MAT3_NORM など) に従って、別の標準原価で品目マスタを追加登録します。 | 追加のテスト品目マスタデータが登録されます。 | CE 2502 では、URR_MAT1_NORM および URR_MAT2_NORM がデモデータとして提供されるため、ユーザがマニュアルで登録する必要はありません。在庫販売統合シナリオのテストで追加の品目マスタデータが必要な場合は、このセクションのステップに従って追加の品目を登録してください。 |

### ワンタイムサービスのサービス製品: URR_MAT1_SERV

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
| 1 | ログオンする | SAP Fiori ラウンチパッドにマスタデータスペシャリスト - 製品データとしてログオンします。 | ホームページが表示されます。 |  |
| 2 | SAP Fiori アプリにアクセスする | 品目登録アプリを選択します (画面にアプリが表示されない場合は、品目登録アプリを検索してみます)。 | 品目登録 (第一画面) が表示されます。 |  |
| 3 | 品目コードおよび品目タイプを入力する | 品目登録 (第一画面) で、以下のエントリを入力します。製品番号: URR_MAT1_SERV品目タイプ: サービス製品次に続行 (Enter) を選択します。 | 新規品目マスタデータの品目コードおよび品目タイプが入力されています。ビュー選択ダイアログウィンドウが表示されます。 |  |
| 4 | ビューを選択する | ビュー選択ダイアログウィンドウで、以下のビューを選択します。基本データ 1販売: 販売組織データ 1販売: 販売組織データ 2販売: 一般/プラントデータ会計管理 1次に続行 (Enter) を選択します。 | 組織レベルダイアログウィンドウが表示されます。 |  |
| 5 | 組織レベルを選択する | 組織レベルウィンドウで、以下の値を更新します。プラント: 1010 (プラント 1 DE)販売組織: 1010 (国内販売組織 DE)流通チャネル: 10 (直販)次に続行 (Enter) を選択します。 | 組織データが選択されました。基本データ 1ビューが表示されます。 |  |
| 6 | ビューを更新する: 基本データ 1 | 基本データ 1 ビューで、以下の値を更新します。テキスト: URR テスト品目 1 SERV基本数量単位: H (時間)品目グループ: YBMM01 (ID ありの非在庫品目)一般明細グループ: SERV (サービス)Enter キーを押します。 | 基本データが更新されます。Enter を押すと、販売: 販売組織 1 ビューが表示されます。 |  |
| 7 | ビューを更新する: 販売: 販売組織1 | 販売: 販売組織 1 ビューで、以下の値を更新します。一般データ出荷プラント: 1010現金割引: X <選択>税データ税分類: 0次に Enter を選択します。 | 販売組織データ 1 が更新されます。販売: 販売組織2 ビューが表示されます。 |  |
| 8 | ビューを更新する: 販売: 販売組織2 | 販売: 販売組織2 ビューで、以下のエントリを更新します。一般明細カテゴリグループ: SERV (サービス)明細カテゴリグループ: SERV (サービス)次に Enter を選択します。 | 販売組織データ 2 が更新されます。販売: 一般/プラントビューが表示されます。 |  |
| 9 | ビューを更新する: 販売: 一般/プラント | 販売: 一般/プラントビューで、以下の値を更新します。利益センタ: YB600次に Enter を選択します。 | 一般販売データが更新されます。会計管理 1 ビューが表示されます。 |  |
| 10 | ビューを更新する: 会計管理 1 | 会計管理 1 ビューの現会計期間データセクションで、以下のエントリを入力します。評価クラス: 3300標準原価: 20価格単位: 1次に、保存を選択します。 | 会計データが更新されます。品目マスタデータが保存されます。 |  |

## 固定価格得意先プロジェクト統合シナリオの品目マスタデータの登録

### URR_FPPRJ_1

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
| 1 | ログオンする | SAP Fiori ラウンチパッドにマスタデータスペシャリスト - 製品データとしてログオンします。 | ホームページが表示されます。 |  |
| 2 | SAP Fiori アプリにアクセスする | 品目登録アプリを選択します (画面にアプリが表示されない場合は、品目登録アプリを検索してみます)。 | 品目登録 (第一画面) が表示されます。 |  |
| 3 | 品目コードおよび品目タイプを入力する | 品目登録 (第一画面) で、以下のエントリを入力します。製品番号: URR_FPPRJ_1品目タイプ: サービス製品次に続行 (Enter) を選択します。 | 新規品目マスタデータの品目コードおよび品目タイプが入力されています。ビュー選択ダイアログウィンドウが表示されます。 |  |
| 4 | ビューを選択する | ビュー選択ダイアログウィンドウで、以下のビューを選択します。基本データ 1販売: 販売組織データ 1販売: 販売組織データ 2販売: 一般/プラントデータ会計管理 1次に続行 (Enter) を選択します。 | 組織レベルダイアログウィンドウが表示されます。 |  |
| 5 | 組織レベルを選択する | 組織レベルウィンドウで、以下の値を更新します。プラント: 1010 (プラント 1 DE)販売組織: 1010 (国内販売組織 DE)流通チャネル: 10 (直販)次に続行 (Enter) を選択します。 | 組織データが選択されました。基本データ 1ビューが表示されます。 |  |
| 6 | ビューを更新する: 基本データ 1 | 基本データ 1 ビューで、以下の値を更新します。テキスト: URR テスト品目 1 SERV基本数量単位: AU (活動単位)品目グループ: P000 (契約タイプ)一般明細グループ: PSFP (固定価格明細)Enter キーを押します。 | 基本データが更新されます。Enter を押すと、販売: 販売組織 1 ビューが表示されます。 |  |
| 7 | ビューを更新する: 販売: 販売組織 1 | 販売: 販売組織 1 ビューで、以下の値を更新します。一般データ出荷プラント: 1010現金割引: X <選択>税データ税分類: 0次に Enter を選択します。 | 販売組織データ 1 が更新されます。販売: 販売組織2 ビューが表示されます。 |  |
| 8 | ビューを更新する: 販売: 販売組織 2 | 販売: 販売組織2 ビューで、以下のエントリを更新します。一般明細カテゴリグループ: PSFP (固定価格明細)勘定割当グループ品目Y1 (固定価格)明細カテゴリグループ: PSFP (固定価格明細)次に Enter を選択します。 | 販売組織データ 2 が更新されます。販売:一般/プラントビューが表示されます。 |  |
| 9 | ビューを更新する: 販売: 一般/プラント | 販売:一般/プラントビューで、以下の値を更新します。利益センタ: YB101次に Enter を選択します。 | 一般販売データが更新されます。会計管理 1 ビューが表示されます。 |  |
| 10 | ビューを更新する: 会計管理 1 | 会計管理 1 ビューの現会計期間データセクションで、以下のエントリを入力します。評価クラス: 3300標準原価: 30価格単位: 1次に、保存を選択します。 | 会計データが更新されます。品目マスタデータが保存されます。 |  |
| 11 | テスト用の追加品目マスタデータを登録する (必要な場合) | 必要な場合は、命名規則URR_FPPRJ* (URR_FPPRJ3、URR_FPPRJ4 など) を使用して、別の標準原価で品目を追加登録します。 | 追加のテスト品目マスタデータが登録されます。 |  |

## サービス契約統合シナリオの品目マスタデータの登録

### URR_SRVCONT1

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
| 1 | ログオンする | SAP Fiori ラウンチパッドにマスタデータスペシャリスト - 製品データとしてログオンします。 | ホームページが表示されます。 |  |
| 2 | SAP Fiori アプリにアクセスする | 品目登録アプリを選択します (画面にアプリが表示されない場合は、品目登録アプリを検索してみます)。 | 品目登録 (第一画面) が表示されます。 |  |
| 3 | 品目コードおよび品目タイプを入力する | 品目登録 (第一画面) で、以下のエントリを入力します。製品番号: URR_SRVCON1品目タイプ: サービス製品次に続行 (Enter) を選択します。 | 新規品目マスタデータの品目コードおよび品目タイプが入力されています。ビュー選択ダイアログウィンドウが表示されます。 |  |
| 4 | ビューを選択する | ビュー選択ダイアログウィンドウで、以下のビューを選択します。基本データ 1販売: 販売組織データ 1販売: 販売組織データ 2販売: 一般/プラントデータ購買次に続行 (Enter) を選択します。 | 組織レベルダイアログウィンドウが表示されます。 |  |
| 5 | 組織レベルを選択する | 組織レベルウィンドウで、以下の値を更新します。プラント: 1010 (プラント 1 DE)販売組織: 1010 (国内販売組織 DE)流通チャネル: 10 (直販)次に続行 (Enter) を選択します。 | 組織データが選択されました。基本データ 1ビューが表示されます。 |  |
| 6 | ビューを更新する: 基本データ 1 | 基本データ 1 ビューで、以下の値を更新します。テキスト: URR テスト品目 1 サービス契約基本数量単位: AU (活動単位)品目グループ: P001 (サービス)一般明細グループ: SCNP (サービス契約製品)Enter キーを押します。 | 基本データが更新されます。Enter を押すと、販売: 販売組織 1 ビューが表示されます。 |  |
| 7 | ビューを更新する: 販売: 販売組織1 | 販売: 販売組織1 ビューで、以下の値を更新します。一般データ基本数量単位: AU (活動単位)品目グループ: P001 (サービス)次に Enter を選択します。 | 販売組織データ 1 が更新されます。販売: 販売組織2 ビューが表示されます。 |  |
| 8 | ビューを更新する: 販売: 販売組織2 | 販売: 販売組織2 ビューで、以下のエントリを更新します。一般明細カテゴリグループ SCNP (サービス契約製品)次に Enter を選択します。 | 販売組織データ 2 が更新されます。販売:一般/プラントビューが表示されます。 |  |
| 9 | ビューを更新する: 販売: 一般/プラント | 販売: 一般/プラントビューで、以下の値を更新します。基本数量単位: AU (活動単位)次に Enter を選択します。 | 一般販売データが更新されます。会計管理 1 ビューが表示されます。 |  |
| 10 | ビューを更新する: 購買 | 購買ビューで、以下のエントリを入力します。基本数量単位: AU (活動単位)品目グループ: P001 (サービス)次に、保存を選択します。 | 会計データが更新されます。品目マスタデータが保存されます。 |  |

## 品目の価格設定

### SFS の商品の価格: URR_MAT1_NORM

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
| 1 | ログオンする | SAP Fiori ラウンチパッドに、価格設定スペシャリストとしてログオンします。 | SAP Fiori ラウンチパッドが開きます。 |  |
| 2 | SAP Fiori アプリにアクセスする | 品目価格設定 - 販売(VK12)を選択します。 | 条件レコード変更ビューが表示されます。 |  |
| 3 | 価格設定条件タイプ | 条件レコード変更ビューで、以下の情報を入力します。条件タイプ: PPR0Enterをクリックします。 | キー組合せビューが表示されます。 |  |
| 4 | キー組合せ | キー組合せビューで、リリースステータスの品目オプションを選択します。その後、選択をクリックします。 | 価格変更 (PPR0): 選択ビューが表示されます。 |  |
| 5 | 選択する | 価格変更 (PPR0): 選択ビューで、以下の情報を更新します。販売組織: 1010 (国内販売組織 DE) を使用流通チャネル: 10 (直販)品目: URR_MAT1_NORM有効日付: <日付>、本日の日付など次に、実行を選択します。 | 価格条件変更 (PPR0): 概要ビューが表示されます。 |  |
| 6 | 価格条件を変更する | 価格条件変更 (PPR0): 概要ビューで、品目に関する以下のデータを更新します。品目: URR_MAT1_NORM金額: 25.00 など単位: EUR有効開始: <日付>、本日の日付などEnterをクリックします。 | 価格条件が更新されています。 |  |
| 7 | 保存する | 保存を選択します。 | 価格が定義されています。 |  |
| 8 | 前画面に戻り、アプリに再度アクセスする | 条件レコード変更ビューで、以下の情報を入力します。条件タイプ: PSAM次にEnterを選択します。 | キー組合せビューが表示されます。 |  |
| 9 | キー組合せ | キー組合せビューで、リリースステータスの品目オプションを選択します。次にEnterを選択します。 | 価格変更 (PSAM): 選択ビューが表示されます。 |  |
| 10 | 選択する | 価格変更 (PSAM): 選択ビューで、以下の情報を更新します。販売組織: 1010 (国内販売組織 DE) を使用流通チャネル: 10 (直販)品目: URR_MAT1_NORM有効日付: <日付>、本日の日付など次に、実行を選択します。 | 価格条件変更 (PSAM): 概要ビューが表示されます。 |  |
| 11 | 価格条件を変更する | 価格条件変更 (PSAM): 概要ビューで、品目に関する以下のデータを更新します。品目: URR_MAT1_NORM金額: 35.00 など単位: EUR有効開始: <日付>、本日の日付などEnterを選択します。 | 価格条件が更新されています。 |  |
| 12 | 保存する | 保存を選択します。 | 価格が定義されます。 |  |

### ワンタイムサービスのサービス製品の価格: URR_MAT1_SERV

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
| 1 | ログオンする | SAP Fiori ラウンチパッドに、価格設定スペシャリストとしてログオンします。 | SAP Fiori ラウンチパッドが開きます。 |  |
| 2 | SAP Fiori アプリにアクセスする | 品目価格設定 - 販売(VK12)を選択します。 | 条件レコード変更ビューが表示されます。 |  |
| 3 | 価格設定条件タイプ | 条件レコード変更ビューで、以下の情報を入力します。条件タイプ: PPR0次にEnterを選択します。 | キー組合せビューが表示されます。 |  |
| 4 | キー組合せ | キー組合せビューで、リリースステータスの品目オプションを選択します。その後、選択 (Enter) を選択します。 | 価格変更 (PPR0): 選択ビューが表示されます。 |  |
| 5 | 選択する | 価格変更 (PPR0): 選択ビューで、以下の情報を更新します。販売組織: 1010 (国内販売組織 DE) を使用流通チャネル: 10 (直販)品目: URR_MAT1_SERV有効日付: <日付>、本日の日付など次に、実行を選択します。 | 価格条件変更 (PPR0): 概要ビューが表示されます。 |  |
| 6 | 価格条件を変更する | 価格条件変更 (PPR0): 概要ビューで、品目に関する以下のデータを更新します。品目: URR_MAT1_SERV金額: 25.00 など単位: EUR有効開始: <日付>、本日の日付などEnterを選択します。 | SRV_01 サービス製品に対する価格条件が更新されます。 |  |
| 7 | 保存する | 保存を選択します。 | サービス製品の価格が定義されました。 |  |
| 8 | 前画面に戻り、アプリに再度アクセスする | 条件レコード変更ビューで、以下の情報を入力します。条件タイプ: PSAM次にEnterを選択します。 |  |  |
| 9 | キー組合せ | キー組合せビューで、リリースステータスの品目オプションを選択します。次にEnterを選択します。 | 価格変更 (PSAM): 選択ビューが表示されます。 |  |
| 10 | 選択する | 価格変更 (PSAM): 選択ビューで、以下の情報を更新します。販売組織: 1010 (国内販売組織 DE) を使用流通チャネル: 10 (直販)品目: URR_MAT1_SERV有効日付: <日付>、本日の日付など次に、実行を選択します。 | 価格条件変更 (PSAM): 概要ビューが表示されます。 |  |
| 11 | 価格条件を変更する | 価格条件変更 (PSAM): 概要ビューで、品目に関する以下のデータを更新します。品目: URR_MAT1_SERV金額: 35.00 など単位: EUR有効開始: <日付>、本日の日付などEnterを選択します。 | SRV_01 サービス製品に対する価格条件が更新されます。 |  |
| 12 | 保存する | 保存を選択します。 | 価格が定義されます。 |  |

### サービス契約品目の価格: URR_SRVCONT1

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
| 1 | ログオンする | SAP Fiori ラウンチパッドに、価格設定スペシャリストとしてログオンします。 | SAP Fiori ラウンチパッドが開きます。 |  |
| 2 | SAP Fiori アプリにアクセスする | 品目価格設定 - 販売(VK12)を選択します。 | 条件レコード変更ビューが表示されます。 |  |
| 3 | 価格設定条件タイプ | 条件レコード変更ビューで、以下の情報を入力します。条件タイプ: PSI1次にEnterを選択します。 | キー組合せビューが表示されます。 |  |
| 4 | キー組合せ | キー組合せビューで、品目を選択します。次にEnterを選択します。 | 価格変更 (PSI1): 選択ビューが表示されます。 |  |
| 5 | 選択する | 価格変更 (PSI1): 選択ビューで、以下の情報を更新します。販売組織: 1010 (国内販売組織 DE) を使用流通チャネル: 10 (直販)品目: URR_SRVCONT1有効日付: <日付>、本日の日付など次に、実行を選択します。 | 価格条件変更 (PSI1): 概要ビューが表示されます。 |  |
| 6 | 価格条件を変更する | 価格条件変更 (PSI1): 概要ビューで、以下のデータを更新します。品目: URR_SRVCONT1金額: 90.00 など通貨: EUR など有効開始: <日付>、本日の日付などEnterを選択します。 | 価格条件が更新されます。 |  |
| 7 | 保存する | 保存を選択します。 | 価格が定義されます。 |  |

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
> Flagged while digesting this document, not verified: The doc says item URR_SRVCONT1 but step 3 enters product number URR_SRVCON1; the URR_FPPRJ_1 item text is URR テスト品目 1 SERV, same as URR_MAT1_SERV's text.

## Connections
- part-of :: [[_cluster]]
- related-to :: [[06-management-accounting/7r8-537]]
- related-to :: [[06-management-accounting/master-data-script-create-material-master-for-universal-revenue-recogn]]
- related-to :: [[06-management-accounting/script-de-dados-mestre-criar-mestre-de-materiais-para-realizacao-de-re]]
- related-to :: [[06-management-accounting/script-de-datos-maestros-crear-maestro-de-materiales-para-el-reconocim]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/7R8_S4CLD2608_Master_Data_JA_XX.docx` — full document · extracted with `mammoth` · 18,904 chars in the whole document
