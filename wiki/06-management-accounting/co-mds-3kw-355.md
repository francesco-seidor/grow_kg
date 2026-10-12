---
id: 06-management-accounting/co-mds-3kw-355
title: CO 原価率の登録 - MDS (3KW) (3KW_S4CLD2608_Master_Data_JA_XX)
description: "Japanese master data script (3KW) for maintaining CO cost rates (activity prices) via Manage Cost Rates apps for service, plan and actual, plus ICO account setup and cost rate query."
cluster: 06-management-accounting
tags: [kb/management-accounting, topic/cost-rates]
aliases: [3KW_S4CLD2608_Master_Data_JA_XX]
keywords: ["CO Cost Rates (Service, Plan and Actual)", cost rates, activity prices, service cost rates, plan cost rates, actual cost rates, cost rate query, intercompany reconciliation accounts, intercompany profit accounts, master data script]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/3KW_S4CLD2608_Master_Data_JA_XX.docx]
confidence: high
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-355
topic: 06-management-accounting/cost-rates
language: JA
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# CO 原価率の登録 - MDS (3KW) (3KW_S4CLD2608_Master_Data_JA_XX)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/3KW_S4CLD2608_Master_Data_JA_XX.docx`, extracted with `mammoth`. Grouped under **CO Cost Rates (Service, Plan and Actual)** in Management Accounting. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

| <!-- image omitted: unnamed --> | マスタデータスクリプトSAP S/4HANA Cloud Public Edition - 02-07-26 |
| --- | --- |
|  | CO 原価率の登録 - MDS (3KW) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

目次

[1 目的 2](#_Toc233891605)

[2 前提条件 3](#_Toc233891606)

[2.1 システムアクセス 3](#_Toc233891607)

[2.2 ロール 3](#_Toc233891608)

[2.3 予備ステップ 3](#_Toc233891609)

[2.3.1 オプション: 会社間調整勘定の更新 (会社間転記の場合のみ) 3](#_Toc233891610)

[2.3.2 オプション: 利益勘定の更新 (会社間レートによる会社間転記の場合のみ) 5](#_Toc233891611)

[3 概要テーブル 7](#_Toc233891612)

[4 テスト手順 8](#_Toc233891613)

[4.1 原価率管理 - サービス 8](#_Toc233891614)

[4.2 原価率管理 - 計画 11](#_Toc233891615)

[4.3 原価率管理 - 実績 13](#_Toc233891616)

[5 分析 15](#_Toc233891617)

[5.1 原価率照会 15](#_Toc233891618)

## 目的

原価率 (活動価格) を更新するために、以下のアプリを使用できます。各アプリには、原価率が定義される方法や活動配分を受け取る対象に応じて、さまざまな目的があります。

| アプリ | 影響を受けるスコープアイテム | コメント |
| --- | --- | --- |
| 原価率管理 - サービス(F3161) | タイムレコーディング (1Q4)間接費会計 (J54)タイムレコーディング - プロジェクトベースサービス (J12)サービスオーダー管理および監視 (3D2) | タイムレコーディング |
| 原価率管理 - 計画(F3162) | 標準原価計算 (BEG)期末処理 - プラント (BEI)期末処理 - 保全指図 (BF7) | 製造確認、指図計画および実績確認 |
| 原価率管理 - 実績(F3422) | 実際原価計算 (33Q) | 原価センタ活動の実績の原価率を入力するために使用します。実績の原価率は、得意先が実際原価計算を使用する場合にのみ必要になります。 |

この文書には、ソリューション有効化後にこのスコープアイテムをテストするための詳細な手順が示されています。これには、事前定義されたソリューション範囲が反映されています。各プロセスステップ、レポート、またはアイテムはそれぞれ個別のセクションで取り上げられ、システムインタラクション (テストステップ) がテーブルビューで示されます。プロセスの範囲内には含まれていなくてもテストに必要となるステップには、それに応じてマークが付いています。プロジェクト固有のステップを追加する必要があります。

|  |
| --- |
| 注記 このテストスクリプトの値 (小数点表記、日付書式など) は、米国の標準表記で表示されます。テストシステムが別の表記を使用するように設定されている場合は、適切な値を入力します。 |

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
| 管理会計担当者 - 間接費 | SAP_BR_OVERHEAD_ACCOUNTANT | 間接費会計 | SAP_BR_OVERHEAD_ACCOUNTANT |  |

### 予備ステップ

#### オプション: 会社間調整勘定の更新 (会社間転記の場合のみ)

用途

このアクティビティでは、会社間 (ICO) 転記の消込勘定を登録および更新することができます。ICO 調整勘定は、アクティビティの G/L 勘定から誘導されます。

手順

SAP S/4HANA Cloud Public Editionの設定環境に応じて、以下のいずれかのオプションを選択します。

ソリューション設定:

1. SAP Fiori ラウンチパッドに設定エキスパート - ビジネスプロセス設定としてログオンします。
2. ソリューション管理 (F1241)を開きます。
3. 必要に応じて、ローカルバージョン設定を選択して国を変更します。
4. ソリューション設定を選択します。
5. 設定ステップセクションの名称列の自動勘定設定(100297) 行で設定を選択します。
6. 以下の表の手順を続行します。

SAP Central Business Configuration:

1. SAP Central Business Configuration でプロジェクト経験にログオンします。
2. Business Processes Configurationアプリに移動します。ツリービューでアクティビティを見つけるには、Automatic Account Determinationアクティビティを検索します。
3. 見つかった明細のOpen Documentationを選択して、この設定アクティビティに関する追加の詳細を表示します。
4. リンクを選択して、SAP S/4HANA Cloud Public Editionシステムに直接ナビゲートします。SAP Fiori ラウンチパッドに設定エキスパート - ビジネスプロセス設定としてログオンします。
5. 以下の表の手順を続行します。

| ステップ番号 | ステップ名 | 指示 | 予想される結果 | 合格/不合格/コメント |
| --- | --- | --- | --- | --- |
| 1 | 領域を選択する | 表示された行で以下のエントリを入力し、ステップ 2を選択します。領域: 管理会計サブ領域: 原価センタ会計プロセス: 実績転記の会社間調整勘定の割当 |  |  |
| 2 | パラメータを選択する | 以下のエントリを入力し、ステップ 3を選択します。勘定コード表: YCOA |  |  |
| 3 | 勘定設定を更新する | ICO 調整に関連する勘定を追加します。注記 デフォルトコンテンツは、消込 G/L 勘定 68888800 - ICO 調整勘定 - 旅費、および 99999900 - ICO 調整勘定 - コンサルティングで提供されます。必要に応じて、この参照を使用して独自の勘定を登録することができます (G/L 勘定タイプ N - 営業外費用または収益)。 |  |  |

#### オプション: 利益勘定の更新 (会社間レートによる会社間転記の場合のみ)

用途

このアクティビティでは、会社間 (ICO) 転記の利益勘定を登録および更新することができます。このステップは、ICO レートで更新および転記する場合に必要です。利益 G/L 消込勘定は、活動配分 G/L 勘定に基づいて誘導されます。

手順

SAP S/4HANA Cloud Public Editionの設定環境に応じて、以下のいずれかのオプションを選択します。

ソリューション設定:

1. SAP Fiori ラウンチパッドに設定エキスパート - ビジネスプロセス設定としてログオンします。
2. ソリューション管理 (F1241)を開きます。
3. 必要に応じて、ローカルバージョン設定を選択して国を変更します。
4. ソリューション設定を選択します。
5. 設定ステップセクションの名称列の自動勘定設定(100297) 行で設定を選択します。
6. 以下の表の手順を続行します。

SAP Central Business Configuration:

1. SAP Central Business Configuration でプロジェクト経験にログオンします。
2. ツリービューでアクティビティを見つけるには、Automatic Account Determinationアクティビティを検索します。
3. 見つかったアイテムのOpen Documentationを選択して、この設定アクティビティの詳細を表示します。
4. リンクを選択して、SAP S/4HANA Cloud Public Editionシステムに直接ナビゲートします。SAP Fiori ラウンチパッドに設定エキスパート - ビジネスプロセス設定としてログオンします。
5. 以下の表の手順を続行します。

| ステップ番号 | ステップ名 | 指示 | 予想される結果 | 合格/不合格/コメント |
| --- | --- | --- | --- | --- |
| 1 | 領域を選択する | 表示された行で以下のエントリを入力し、ステップ 2を選択します。領域: 管理会計サブ領域: 原価センタ会計プロセス: 会社間利益勘定の割当 |  |  |
| 2 | パラメータを選択する | 以下のエントリを入力し、ステップ 3を選択します。勘定コード表: YCOA |  |  |
| 3 | 勘定設定を更新する | 活動配分 G/L の ICO 利益に関連する勘定を追加します。注記 デフォルトコンテンツは、利益勘定 97777700 - ICO 利益で提供されます。必要に応じて、これを参照として使用し、独自の利益勘定を登録することができます (G/L 勘定 P - 一次原価および収益)。 |  |  |

## 概要テーブル

このスコープアイテムは、以下の表に示されている複数のプロセスステップで構成されます。

|  |
| --- |
| 注記 システム管理者が SAP Fiori ラウンチパッドでスペースおよびページを有効化している場合、ホームページには、ビジネスロールの一般的なタスクを実行するために必要なアプリのみが含まれます。ホームページに含まれていないその他すべての (検索可能な) アプリは、検索バーを使用して見つけることができます ([2434549](https://me.sap.com/notes/2434549))。ホームページをパーソナライズして非表示のアプリを含める場合は、ユーザプロファイルにナビゲートし、アプリファインダを選択します。 |

| プロセスステップ | ビジネスロール | トランザクション/アプリ | 予想される結果 |
| --- | --- | --- | --- |
| [原価率管理 - サービス](#unique_8) [ ページ] 8 | 管理会計担当者 - 間接費 | 原価率管理 - サービス(F3161) | サービスの原価率が更新されます。 |
| [原価率管理 - 計画](#unique_9) [ ページ] 11 | 管理会計担当者 - 間接費 | 原価率管理 - 計画(F3162) | 計画の原価率が更新されます。 |
| [原価率管理 - 実績](#unique_10) [ ページ] 13 | 管理会計担当者 - 間接費 | 原価率管理 - 実績(F3422) | 実績の原価率が更新されます。 |

## テスト手順

### 原価率管理 - サービス

テスト管理

カスタマプロジェクト: プロジェクト固有部分への入力

|  |  |  |  |
| --- | --- | --- | --- |
| テストケース ID | <X.XX> | テスト実施日: |  |
| テスト実施者名: |  | 期間: |  |
| ビジネスロール: |  | 責任者: | <都道府県/州、サービスプロバイダ、カスタマ/共同サービスプロバイダ、およびカスタマ> |

コンテキスト

このアプリは、さまざまな基準に基づいて原価率を入力するために使用します。原価率は、時間記録または直接活動配分を介して、以下のレシーバオブジェクトに対する活動配分で使用します。

- 原価センタ
- プロジェクト WBS 要素
- サービスオーダー

このアプリでは、サービス原価レベルおよび特定の従業員の原価率を定義できるため、プロフェッショナルサービスプロバイダが使用できます。ただし、サービス原価レベルおよび従業員の原価率が必要な場合は、製造会社も使用できます。

以下の項目は、価格更新に使用することができます。

- 会社コード (提供) は常に入力されているため、アクセス順序に関連しません。
- 請求対象の会社 (受取)
- ICO 価格 (フラグ)
- 原価センタ (提供)
- 活動タイプ (提供)
- サービス原価レベル (提供)
- 従業員番号 (提供)
- ワークアイテム (新規) (受取)
- WBS 要素 (受取)

一覧の順序は、キーを示していて、一覧の最後 (WBS 要素) が最上位優先度のキーです。

価格テーブルを更新するときに、以下のルールが確認されます。

- センダ会社コードが必要です。
- 以下の 1 つまたは複数の項目が入力されている必要があります。活動タイプ、サービス原価レベル、従業員番号 (原価センタのみはサポートされていません)
- 従業員番号項目と原価センタ項目は 1 つの価格のキー項目として互いに排他的です。個人が特定の原価率を持つか、原価センタの平均レートが有効かのどちらかです。
- 従業員番号項目とサービス原価レベル項目は 1 つの価格のキー項目として互いに排他的です。個人が特定の原価率を持つか、サービス原価レベルの平均レートが有効かのどちらかです。
- 原価センタとサービス原価レベルは、可能なキーの組合せです。
- 原価センタと活動タイプの可能な組合せは、活動タイプで定義された原価センタカテゴリで制御されます。
- 社内の原価率を入力する場合は、受取会社は空白のままにする必要があります。
- WBS 固有の原価率は、会社間および社内活動配分で使用できます。受取会社および WBS 要素を入力すると、WBS 要素が受取会社に割り当てられているかがチェックされます (移行された原価率の問題を招く可能性があるため、受取会社は自動的に WBS 要素から抽出されません)。
- 以下の点が確認され、ICO フラグが設定されます。
    - 受取会社コードが空白の場合は、ユーザ入力の ICO フラグが使用されます。
    - 受取会社コードがセンダ会社コードと一致しない場合は、ICO フラグは true に設定されます。
    - それ以外の場合は、ICO フラグは false に設定されます。

| 原価センタ | 活動タイプ | サービス原価レベル | 従業員番号 (従業員) | ワークアイテム (受取) | WBS + 要素 (受取) | 請求対象会社コード (受取) | コメント |
| --- | --- | --- | --- | --- | --- | --- | --- |
| センダ | レシーバ |  |  |  |  |  |  |
|  | X |  |  |  |  |  | 少なくとも 1 つの項目 (活動タイプ、サービス原価レベル、従業員番号) を入力する必要があります。 |
|  |  | X |  |  |  |  |  |
| 入力不可 |  | 入力不可 | X |  |  |  |  |
| 入力不可 | X | 入力不可 | X |  |  |  | 従業員番号。原価センタなし、サービス原価レベルなし |
| X | X |  |  |  |  |  | 原価センタ+ 活動タイプ |
| X |  | X |  |  |  |  | 原価センタ+ サービス原価レベル |
| X | X | X |  |  |  |  | 原価センタ+ 活動タイプ + サービス原価レベル |
|  | X | X |  |  |  |  | 活動タイプ + サービス原価レベル |
|  | X |  |  | (X) | (X) |  | WBS またはワークアイテムを入力できます。 |
|  |  | X |  | (X) | (X) |  |  |
| 入力不可 |  | 入力不可 | X | (X) | (X) |  |  |
| 入力不可 | X | 入力不可 | X | (X) | (X) |  |  |
| X | X |  |  | (X) | (X) |  |  |
| X |  | X |  | (X) | (X) |  |  |
| X | X | X |  | (X) | (X) |  |  |
|  | X | X |  | (X) | (X) |  |  |
|  | X |  |  | (X) | (X) | X | ICO レート |
|  |  | X |  | (X) | (X) | X |  |
| 入力不可 |  | 入力不可 | X | (X) | (X) | X |  |
| 入力不可 | X | 入力不可 | X | (X) | (X) | X |  |
| X | X |  |  | (X) | (X) | X |  |
| X |  | X |  | (X) | (X) | X |  |
| X | X | X |  | (X) | (X) | X |  |
|  | X | X |  | (X) | (X) | X |  |

手順

| テストステップ番号 | テストステップ名 | 指示 | 予想される結果 | 合格/不合格/コメント |
| --- | --- | --- | --- | --- |
| 1 | ログオンする | SAP Fiori ラウンチパッドに 管理会計担当者 - 間接費 としてログオンします。 |  |  |
| 2 | SAP Fiori アプリにアクセスする | 原価率管理 - サービス(F3161) を開きます。 | 原価率管理 - サービス画面が表示されます。 |  |
| 3 | 会社コード | 以下のエントリを入力し、追加を選択します。会社コード: <会社コード> |  |  |
| 4 | サービス原価率を更新する | 以下のエントリを入力し、保存を選択します。受取会社: <空白のまま>注記 この項目は、会社間原価率の場合にのみ使用する必要があり、それ以外の場合は空白のままにします。原価センタ: <原価センタ>活動タイプ: <活動タイプ>WBS 要素: <これはオプション項目です。>開始会計年度: <今年度>開始期間: <現会計期間>レート: 100注記 この比率は、すべての元帳に転記するために使用されます。通貨: <通貨>単位: 1活動単位: H | 原価率が登録されます。 |  |

### 原価率管理 - 計画

テスト管理

カスタマプロジェクト: プロジェクト固有部分への入力

|  |  |  |  |
| --- | --- | --- | --- |
| テストケース ID | <X.XX> | テスト実施日: |  |
| テスト実施者名: |  | 期間: |  |
| ビジネスロール: |  | 責任者: | <都道府県/州、サービスプロバイダ、カスタマ/共同サービスプロバイダ、およびカスタマ> |

コンテキスト

このアクティビティは、生産環境での原価センタ活動の原価率を計画するために使用します。原価率は、以下で使用されます。

- 製造指図および保全指図に対する活動配分
- 品目原価計算

手順

| テストステップ番号 | テストステップ名 | 指示 | 予想される結果 | 合格/不合格/コメント |
| --- | --- | --- | --- | --- |
| 1 | ログオンする | SAP Fiori ラウンチパッドに 管理会計担当者 - 間接費 としてログオンします。 |  |  |
| 2 | SAP Fiori アプリにアクセスする | 原価率管理 - 計画(F3162) を開きます。 | 原価率管理 - 計画画面が表示されます。 |  |
| 3 | 追加する | 追加を選択します。 |  |  |
| 4 | 計画原価率を更新する | 以下のエントリを入力し、保存を選択します。原価センタ: <原価センタ>活動タイプ: <活動タイプ>開始会計年度: <今年度>開始期間: <現会計期間>通貨: <通貨>固定率: <金額>変動率: <金額>注記 この比率は、すべての元帳に転記するために使用されます。 | 計画の原価率が更新されます。 |  |

### 原価率管理 - 実績

テスト管理

カスタマプロジェクト: プロジェクト固有部分への入力

|  |  |  |  |
| --- | --- | --- | --- |
| テストケース ID | <X.XX> | テスト実施日: |  |
| テスト実施者名: |  | 期間: |  |
| ビジネスロール: |  | 責任者: | <都道府県/州、サービスプロバイダ、カスタマ/共同サービスプロバイダ、およびカスタマ> |

コンテキスト

このアクティビティは、実績原価計算で使用される原価センタ活動の実績原価率を入力するために使用します。実績原価率は、元帳で更新することができます。

手順

| テストステップ番号 | テストステップ名 | 指示 | 予想される結果 | 合格/不合格/コメント |
| --- | --- | --- | --- | --- |
| 1 | ログオンする | SAP Fiori ラウンチパッドに 管理会計担当者 - 間接費 としてログオンします。 |  |  |
| 2 | SAP Fiori アプリにアクセスする | 原価率管理 - 実績(F3422) を開きます。 | 原価率管理 - 実績画面が表示されます。 |  |
| 3 | 追加する | 追加を選択します。 |  |  |
| 4 | 実績原価率を更新する | 以下のエントリを入力し、保存を選択します。原価センタ: <原価センタ>活動タイプ: <活動タイプ>元帳: <0L またはリーディング元帳など>注記実績原価率計算を使用する場合は、元帳ごとに実績原価率が計算されます。自動的に計算された原価率を表示または修正する場合は、元帳を入力する必要があります。元帳項目が空白の実績原価率は、すべての元帳への転記に使用されます。元帳固有の実績原価率が存在する場合は、元帳固有の率が使用されます。元帳列を表示するには、原価率一覧で設定を調整し、元帳を選択します。開始会計年度: <今年度>開始期間: <現会計期間>通貨: <通貨>固定率: <金額>変動率: <金額>注記 この比率は、すべての元帳に転記するために使用されます。 | 実績の原価率が更新されます。 |  |

## 分析

### 原価率照会

目的

このレポートでは、さまざまな原価率タイプを選択して表示することができます。

前提条件

原価率がすでに存在している必要があります。

手順

| テストステップ番号 | テストステップ名 | 指示 | 予想される結果 | 合格/不合格/コメント |
| --- | --- | --- | --- | --- |
| 1 | ログオンする | SAP Fiori ラウンチパッドに管理会計担当者 - 間接費としてログオンします。 |  |  |
| 2 | SAP Fiori アプリにアクセスする | 原価率照会 (F5150)を開きます。 | 原価率照会画面が表示されます。 |  |
| 3 | 選択基準を入力する | 以下のエントリを入力し、Goを選択します。元帳: <この項目は空白のまま>注記 選択項目を空白のままにすると、すべての元帳に適用される同じ比率 (計画比率の例) が表示されます。選択時に元帳を指定すると、選択した特定の元帳でのみ更新され、実績率にのみ適用される比率に原価率の表示が制限されます。原価センタ: <10101101 など>活動タイプ: <11 など>開始会計年度期間: <現会計期間>終了会計年度期間: <現会計期間> |  |  |

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
- related-to :: [[06-management-accounting/co-mds-3kw-357]]
- related-to :: [[06-management-accounting/crear-tasas-de-coste-co-mds-3kw-354]]
- related-to :: [[06-management-accounting/master-data-script-create-co-cost-rates-mds-3kw-353]]
- related-to :: [[06-management-accounting/script-de-dados-mestre-criar-taxas-de-custo-co-mds-3kw-356]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/3KW_S4CLD2608_Master_Data_JA_XX.docx` — full document · extracted with `mammoth` · 13,551 chars in the whole document
