---
id: 09-subscription-billing-and-contract-accounting/mds-3ja-325
title: 使用量基準料金計算の製品マスタ登録 - MDS (3JA) (3JA_S4CLD2608_Master_Data_JA_XX)
description: "Japanese SAP S/4HANA Cloud Public Edition 2608 master data script (3JA): create configurable product master with characteristics, class, variant pricing for usage-based billing."
cluster: 09-subscription-billing-and-contract-accounting
tags: [kb/subscription-billing-and-contract-accounting, topic/variant-configured-products-in-provider-contracts]
aliases: [3JA_S4CLD2608_Master_Data_JA_XX]
keywords: [Variant-Configured Products in Provider Contracts, product master, configurable material, characteristics, classes, configuration profile, variant pricing, usage-based billing, sales data, business roles]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/3JA_S4CLD2608_Master_Data_JA_XX.docx]
confidence: high
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-325
topic: 09-subscription-billing-and-contract-accounting/variant-configured-products-in-provider-contracts
language: JA
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# 使用量基準料金計算の製品マスタ登録 - MDS (3JA) (3JA_S4CLD2608_Master_Data_JA_XX)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/3JA_S4CLD2608_Master_Data_JA_XX.docx`, extracted with `mammoth`. Grouped under **Variant-Configured Products in Provider Contracts** in Subscription Billing and Contract Accounting. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

| <!-- image omitted: unnamed --> | マスタデータスクリプトSAP S/4HANA Cloud Public Edition - 02-07-26 |
| --- | --- |
|  | 使用量基準料金計算の製品マスタ登録 - MDS (3JA) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

目次

[1 目的 2](#_Toc233891554)

[2 前提条件 3](#_Toc233891555)

[2.1 システムアクセス 3](#_Toc233891556)

[2.2 ロール 3](#_Toc233891557)

[2.3 必須の組織ユニット 3](#_Toc233891558)

[2.4 必須マスタデータおよび任意マスタデータ 4](#_Toc233891559)

[2.5 データ登録の主要パラメータ 4](#_Toc233891560)

[2.5.1 グルーピングおよび番号範囲 4](#_Toc233891561)

[2.5.2 産業コード 5](#_Toc233891562)

[3 概要テーブル 6](#_Toc233891563)

[4 テスト手順 7](#_Toc233891564)

[4.1 選定可能品目マスタ登録 - 基本データ 7](#_Toc233891565)

[4.2 特性の登録 8](#_Toc233891566)

[4.3 クラスの登録 11](#_Toc233891567)

[4.4 選定プロファイルの登録 12](#_Toc233891568)

[4.5 品目マスタの登録 - 分類 13](#_Toc233891569)

[4.6 バリアント価格設定の登録 15](#_Toc233891570)

[4.7 製品マスタデータの登録 - 販売データ/売上税データ 16](#_Toc233891571)

## 目的

この文書では、SAP S/4HANA Cloud Public Editionシステムに品目マスタデータレコードを登録する方法について説明します。この説明には、"標準的" なシステム環境で処理するマスタデータに関連するデータセグメントが含まれています。読者は、入力値を入力する必要があるデータセグメントおよび項目について主に学習します。SAP S/4HANA Cloud Public Editionコンテンツの範囲に関連しない項目については、UI に表示される場合もありますが、この文書では説明されていません。

ここで説明したとおりに登録されるバリアント価格設定を含む製品マスタレコードは、使用量基準料金計算で使用することができます。

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
| 製品選定モデラ | SAP_BR_PRODUCT_CONFIG_MODELER | バリアント選定 | SAP_BR_PRODUCT_CONFIG_MODELER |  |
| マスタデータスペシャリスト - 製品データ | SAP_BR_PRODMASTER_SPECIALIST | マスタデータ - 製品/製品ガバナンス | SAP_BR_PRODMASTER_SPECIALIST / SAP_CMD_SPT_PR_GOV_PC |  |

### 必須の組織ユニット

マスタデータの一部のセグメントは会社の組織ユニットに依存し、一般 (共通) データは組織ユニットまたは会社コードに依存しません。以下の表は、さまざまなデータセグメントおよび関連する組織ユニットの概要を示しています。

| データセグメント | 依存対象 | 項目例 | コメント | 使用される組織ユニット |
| --- | --- | --- | --- | --- |
| 基本データ | 組織ユニットに依存しない | 品目テキスト (短)、品目コード、品目グループ、基本数量単位など | 基本データは、品目マスタデータレコードに対して一度のみ存在します。 | 該当なし |
| 販売データ | プラント、販売組織、流通チャネル | 税データ、明細カテゴリグループなど。 | プラントデータは、品目マスタレコードが使用される企業構造のすべてのプラント ID に対して存在可能です。 | プラント: ____________ 販売組織: __________ 流通チャネル: __________ |

### 必須マスタデータおよび任意マスタデータ

マスタデータレコードは、他のマスタデータを参照する場合があります。以下の表は、マスタデータレコードで使用される、任意および必須のマスタデータオブジェクトの概要を示しています。

|  |
| --- |
| 注記 適切な税計算を取得するには、ブラジル固有の項目が必要です。チェックNota Fiscal (ブラジル) - JD0品目マスタデータの BR 固有項目の定義の章を参照してください。 |

| マスタデータオブジェクト | データセグメントでの使用 | 必須/任意 | コメント |
| --- | --- | --- | --- |
|  |  |  |  |
|  |  |  |  |

### データ登録の主要パラメータ

このセクションでは、マスタレコードの動作に影響し、品目マスタデータレコードの登録に常に必要となる基本パラメータの一部について説明します。

#### グルーピングおよび番号範囲

品目タイプによって、更新できるデータセグメント (ビュー) や、必須またはオプションの項目が決まります。また、品目の番号範囲も品目タイプに基づいて決められます。SAP の標準コンテンツでは、すべての品目タイプで同じ番号範囲定義が使用されます。

#### 産業コード

標準コンテンツでは、1 つの産業コード M のみが提供されます。現在は、産業コードは SAP GUI でのみ表示可能です。

## 概要テーブル

このマスタレコードは、以下の表に示されている複数のセグメントで構成されます。

|  |
| --- |
| 注記 システム管理者が SAP Fiori ラウンチパッドでスペースおよびページを有効化している場合、ホームページには、ビジネスロールの一般的なタスクを実行するために必要なアプリのみが含まれます。ホームページに含まれていないその他すべての (検索可能な) アプリは、検索バーを使用して見つけることができます ([2434549](https://me.sap.com/notes/2434549))。ホームページをパーソナライズして非表示のアプリを含める場合は、ユーザプロファイルにナビゲートし、アプリファインダを選択します。 |

| セグメント | ビジネスロール | アプリ/トランザクション | 予想される結果 |
| --- | --- | --- | --- |
| [選定可能品目マスタ登録 - 基本データ](#unique_11) [ ページ] 7 | マスタデータスペシャリスト - 製品データ | 品目登録(MM01) | 品目マスタデータ - 基本データが登録されます。 |
| [特性の登録](#unique_12) [ ページ] 8 | 製品選定モデラ | 特性管理 (CT04) | 特性が登録されます。 |
| [クラスの登録](#unique_13) [ ページ] 11 | 製品選定モデラ | クラス管理 (CL02) | クラスが登録されます。 |
| [選定プロファイルの登録](#unique_14) [ ページ] 12 | 製品選定モデラ | VC モデリング環境 (PMEVC) | 選定プロファイルが登録されます。 |
| [品目マスタの登録 - 分類](#unique_15) [ ページ] 13 | マスタデータスペシャリスト - 製品データ | 品目登録(MM01) | 品目マスタデータ - 分類が登録されます。 |
| [バリアント価格設定の登録](#unique_16) [ ページ] 15 | 製品選定モデラ | VC モデリング環境 (PMEVC) | バリアント条件が特性値にマッピングされます。 |
| [製品マスタデータの登録 - 販売データ/売上税データ](#unique_17) [ ページ] 16 | マスタデータスペシャリスト - 製品データ | 品目登録(MM01) | 品目マスタデータ - 販売データ (売上税データ) が登録されます。 |

## テスト手順

このセクションには、このマスタレコードに含まれる各セグメントまたはプロセスステップの手順が記載されています。

### 選定可能品目マスタ登録 - 基本データ

テスト管理

カスタマプロジェクト: プロジェクト固有部分への入力

|  |  |  |  |
| --- | --- | --- | --- |
| テストケース ID | <X.XX> | テスト実施日: |  |
| テスト実施者名: |  | 期間: |  |
| ビジネスロール: |  | 責任者: | <都道府県/州、サービスプロバイダ、カスタマ/共同サービスプロバイダ、およびカスタマ> |

目的

このプロセスステップでは、品目マスタの基本データビューを登録します。

手順

| テストステップ番号 | テストステップ名 | 指示 | 予想される結果 | コメント |
| --- | --- | --- | --- | --- |
| 1 | ログオンする | SAP Fiori ラウンチパッドにマスタデータスペシャリスト - 製品データとしてログオンします。 | SAP Fiori ラウンチパッドが表示されます。 |  |
| 2 | SAP Fiori アプリにアクセスする | 品目登録(MM01)を開きます。 | アプリが開きます。 |  |
| 3 | 品目基本データを入力する | 品目登録 (第一画面)画面で、以下のエントリを入力します。品目: <CBPTS001>産業コード: M注記 産業コード入力項目が表示されていない場合、入力は必要ありません。産業コードが入力用に提供されていない場合、その項目は自動的に入力されます。品目タイプ: KMAT - 選定可能品目 | ビュー選択画面が表示されます。 |  |
| 4 | ビューを選択する | ビュー選択画面で、基本データ 1および基本データ 2を選択し、続行を選択します。 | 品目登録 (選定可能品目)画面が表示されます。 |  |
| 5 | 基本データを入力する | 品目登録 CBPTS001 (選定可能品目)画面の基本データ 1タブで、品目テキスト (テキスト (短)) を入力します。たとえば、<消費ベースの電動工具>と入力します。 |  |  |
| 6 | 基本データを入力する | 基本データ 1 タブの一般データセクションで、以下のエントリを入力します。基本数量単位: <個>一般明細CatGrp.: <0003> |  |  |
| 7 | 基本データを入力する | 次元/EANセクションで、以下のエントリを入力します。重量単位: KG基本データ 2タブを選択します。 |  |  |
| 8 | 基本データを入力する | 基本データ 2タブでは、エントリを入力する必要がありません。Enterを押します。 | 最終データビュー到達画面に、終了しようとしています。最初にこの品目のデータを保存しますかというメッセージが表示されます。 |  |
| 9 | データを保存する | 最終データビュー到達画面で、はいを選択します。 | 品目登録 (第一画面)画面が表示されます。基本データが登録および保存されます。 |  |

### 特性の登録

テスト管理

カスタマプロジェクト: プロジェクト固有部分への入力

|  |  |  |  |
| --- | --- | --- | --- |
| テストケース ID | <X.XX> | テスト実施日: |  |
| テスト実施者名: |  | 期間: |  |
| ビジネスロール: |  | 責任者: | <都道府県/州、サービスプロバイダ、カスタマ/共同サービスプロバイダ、およびカスタマ> |

目的

このプロセスステップでは、特性を登録します。

手順

| テストステップ番号 | テストステップ名 | 指示 | 予想される結果 | コメント |
| --- | --- | --- | --- | --- |
| 1 | ログオン | SAP Fiori ラウンチパッドに製品選定モデラとしてログオンします。 | SAP Fiori ラウンチパッドが表示されます。 |  |
| 2 | 得意先マスタデータ管理を開く | 特性管理 (CT04)を開きます。 | アプリが開きます。 | 登録、変更、および照会モード用の共通画面です。 |
| 3 | 特性名を入力する | 以下のエントリを入力して登録を選択します。特性: <カテゴリ> | 特性登録画面が表示されます。 | 有効開始日付項目に値が自動入力されます。特性 <カテゴリ> がすでに存在する場合は、特性 <カテゴリ>_Vnn (nn は連続番号) を登録します。 |
| 4 | 基本データを入力する | 基本データタブで、以下のエントリを入力します。基本データセクション:テキスト: <カテゴリ>:ステータス: リリース済 (デフォルト)書式セクション:データ型: 文字書式文字数: <15>大文字/小文字区別: <選択解除>値割当セクション:単一値ラジオボタンを選択します。制限可能チェックボックスを選択解除します。 |  |  |
| 5 | 値を入力する | 値タブの許容値セクションで、以下のエントリを入力します。特性値:<標準><高性能>テキスト:<標準電動工具><高性能電動工具><標準>値のデフォルト値チェックボックスを選択します。 |  |  |
| 6 | 特性を保存する | 保存を選択します。 | 特性が登録されます。 |  |
| 7 | 別の特性を登録する | 以下のエントリを入力して登録を選択します。特性: <CATEGORY_VARCOND> |  |  |
| 8 | 基本データを入力する | 基本データタブで、以下のエントリを入力します。基本データセクション:テキスト: <バリアント条件キー>ステータス: リリース済 (デフォルト)書式セクション:データ型: 文字書式文字数: <26>大文字/小文字区別: <選択済>値割当セクション:複数値ラジオボタンを選択します。制限可能チェックボックスを選択解除します。 |  |  |
| 9 | 追加データを入力する | 追加データタブで、以下のエントリを入力します。テーブル項目の参照セクション:テーブル名: SDCOM項目名: VKOND値割当の動作セクション:入力不可: <選択解除> |  |  |
| 10 | 特性を保存する | 保存を選択します。 |  |  |

### クラスの登録

テスト管理

カスタマプロジェクト: プロジェクト固有部分への入力

|  |  |  |  |
| --- | --- | --- | --- |
| テストケース ID | <X.XX> | テスト実施日: |  |
| テスト実施者名: |  | 期間: |  |
| ビジネスロール: |  | 責任者: | <都道府県/州、サービスプロバイダ、カスタマ/共同サービスプロバイダ、およびカスタマ> |

目的

このプロセスステップでは、クラスタイプ - 300 のクラスを登録します。

手順

| テストステップ番号 | テストステップ名 | 指示 | 予想される結果 | コメント |
| --- | --- | --- | --- | --- |
| 1 | ログオンする | SAP Fiori ラウンチパッドに製品選定モデラとしてログオンします。 | SAP Fiori ラウンチパッドが表示されます。 |  |
| 2 | SAP Fiori アプリにアクセスする | クラス管理 (CL02)を開きます。 | アプリが開きます。 | 登録、変更、および照会モード用の共通画面です。 |
| 3 | クラス名を入力する | 以下のエントリを入力し、登録を選択します。クラス: <カテゴリ>クラスタイプ: 300 | クラス登録画面が表示されます。 | 有効開始日付項目に値が自動入力されます。クラス <カテゴリ> がすでに存在する場合は、クラス <カテゴリ>_Vnn (nn は連続番号) を登録します。 |
| 4 | 基本データを入力する | 基本データタブで、以下のエントリを入力します。基本データセクション:テキスト: <電動工具のカテゴリ>ステータス: リリース済 (デフォルト)同一分類セクション:確認なしラジオボタン (デフォルト) を選択します。 |  | 同一分類を使用する場合は、確認方法 (警告メッセージ、エラー、なし) を選択することができます。 |
| 5 | 特性を入力する | 特性タブで、以下のエントリを入力します。特性: <カテゴリ>特性: <CATEGORY_VARCOND> |  |  |
| 6 | クラスを保存する | 保存を選択します。 | クラスが登録されます。 |  |

### 選定プロファイルの登録

テスト管理

カスタマプロジェクト: プロジェクト固有部分への入力

|  |  |  |  |
| --- | --- | --- | --- |
| テストケース ID | <X.XX> | テスト実施日: |  |
| テスト実施者名: |  | 期間: |  |
| ビジネスロール: |  | 責任者: | <都道府県/州、サービスプロバイダ、カスタマ/共同サービスプロバイダ、およびカスタマ> |

目的

このプロセスステップでは、選定プロファイルを登録します。

手順

| テストステップ番号 | テストステップ名 | 指示 | 予想される結果 | コメント |
| --- | --- | --- | --- | --- |
| 1 | ログオンする | SAP Fiori ラウンチパッドに製品選定モデラとしてログオンします。 | SAP Fiori ラウンチパッドが表示されます。 |  |
| 2 | SAP Fiori アプリにアクセスする | VC モデリング環境 (PMEVC)を開きます。 | アプリが開きます。 |  |
| 3 | 選定モデルデータを入力する | 第一画面で、以下のエントリを入力し、モデル入力を選択します。品目: <CBPTS001>クラスタイプ: 300 (デフォルト) | 選定画面が表示されます。 |  |
| 4 | 選定プロファイルを登録する | オブジェクト画面で、<CBPTS001>を右クリックし、選定プロファイル登録を選択します。選定プロファイル登録ダイアログボックスで、以下のエントリを入力します。選定プロファイル: <CBPT_CP_V01>続行を選択します。 | 右側のパネルに選定プロファイル画面が表示され、基本データタブが選択されます。 |  |
| 5 | 選定プロファイルを保存する | 保存を選択します。 | 選定プロファイルが登録されます。 |  |

### 品目マスタの登録 - 分類

テスト管理

カスタマプロジェクト: プロジェクト固有部分への入力

|  |  |  |  |
| --- | --- | --- | --- |
| テストケース ID | <X.XX> | テスト実施日: |  |
| テスト実施者名: |  | 期間: |  |
| ビジネスロール: |  | 責任者: | <都道府県/州、サービスプロバイダ、カスタマ/共同サービスプロバイダ、およびカスタマ> |

目的

このプロセスステップでは、品目マスタの分類ビューを登録します。

前提条件

このセクションを開始する前に、前の[選定可能品目マスタ登録 - 基本データ](#unique_11) [ ページ] 7セクションのステップを完了しておく必要があります。前の手順で説明されているとおりに基本データエントリを保存した後で、この手順を開始してください。

手順

| テストステップ番号 | テストステップ名 | 指示 | 予想される結果 | コメント |
| --- | --- | --- | --- | --- |
| 1 | ログオンする | SAP Fiori ラウンチパッドにマスタデータスペシャリスト - 製品データとしてログオンします。 | SAP Fiori ラウンチパッドが表示されます。 |  |
| 2 | SAP Fiori アプリにアクセスする | 品目登録(MM01)を開きます。 | アプリが開きます。 |  |
| 3 | 品目基本データを入力する | 品目登録 (第一画面)で、以下のエントリを入力します。品目: <CBPTS001>産業コード: M注記 産業コード入力項目が表示されていない場合、入力は必要ありません。産業コードが入力用に提供されていない場合、その項目は自動的に入力されます。品目タイプ: KMAT - 選定可能品目 | ビュー選択画面が表示されます。 |  |
| 4 | ビューを選択する | ビュー選択画面で、分類を選択し、続行を選択します。 | クラスタイプ (1)画面が表示されます。 |  |
| 5 | クラスタイプを入力する | 制約レベルセクションで、以下のエントリを入力し、続行を選択します。クラスタイプテキスト: バリアントタイプ: 300 | 分類画面が表示されます。 |  |
| 6 | 分類データを入力する | 分類画面の割当タブで、以下のデータをクラス列に入力し、保存を選択します。<カテゴリ>クラス CATEGORY – オブジェクト <CBPTS001>タブで、以下のデータを値列に入力し、保存を選択します。<標準><高性能> | データが保存されます。 |  |

### バリアント価格設定の登録

テスト管理

カスタマプロジェクト: プロジェクト固有部分への入力

|  |  |  |  |
| --- | --- | --- | --- |
| テストケース ID | <X.XX> | テスト実施日: |  |
| テスト実施者名: |  | 期間: |  |
| ビジネスロール: |  | 責任者: | <都道府県/州、サービスプロバイダ、カスタマ/共同サービスプロバイダ、およびカスタマ> |

目的

バリアント条件が特性値にマッピングされます。

手順

| テストステップ番号 | テストステップ名 | 指示 | 予想される結果 | コメント |
| --- | --- | --- | --- | --- |
| 1 | ログオンする | SAP Fiori ラウンチパッドに製品選定モデラとしてログオンします。 | SAP Fiori ラウンチパッドが表示されます。 |  |
| 2 | SAP Fiori アプリにアクセスする | VC モデリング環境 (PMEVC)を開きます。 | アプリが開きます。 |  |
| 3 | 選定モデルデータを入力する | 第一画面で、以下のエントリを入力し、モデル更新の入力を選択します。品目: <CBPTS001>クラスタイプ: 300 (デフォルト) | 選定画面が表示されます。 |  |
| 4 | バリアント価格設定を登録する | オブジェクトセクションで、<CBPTS001>をダブルクリックして、右側のパネルでバリアント価格設定タブを選択します。変更を選択し、以下のエントリを入力します。特性: <カテゴリ>特性値: <高性能>バリアント条件: <高性能> |  |  |
| 5 | 設定を保存する | 保存を選択します。 | バリアント価格設定が登録されます。 |  |

### 製品マスタデータの登録 - 販売データ/売上税データ

テスト管理

カスタマプロジェクト: プロジェクト固有部分への入力

|  |  |  |  |
| --- | --- | --- | --- |
| テストケース ID | <X.XX> | テスト実施日: |  |
| テスト実施者名: |  | 期間: |  |
| ビジネスロール: |  | 責任者: | <都道府県/州、サービスプロバイダ、カスタマ/共同サービスプロバイダ、およびカスタマ> |

目的

このプロセスステップでは、品目マスタの販売データビューを登録します。

手順

| テストステップ番号 | テストステップ名 | 指示 | 予想される結果 | コメント |
| --- | --- | --- | --- | --- |
| 1 | ログオンする | SAP Fiori ラウンチパッドにマスタデータスペシャリスト - 製品データとしてログオンします。 | SAP Fiori ラウンチパッドが表示されます。 |  |
| 2 | SAP Fiori アプリにアクセスする | 品目登録(MM01)を開きます。 | アプリが開きます。 |  |
| 3 | 品目基本データを入力する | 品目登録 (第一画面)で、以下のエントリを入力します。品目: <CBPTS001>産業コード: M注記 産業コード入力項目が表示されていない場合、入力は必要ありません。産業コードが入力用に提供されていない場合、その項目は自動的に入力されます。品目タイプ: KMAT - 選定可能品目 | ビュー選択画面が表示されます。 |  |
| 4 | ビューを選択する | ビュー選択画面で、販売: 販売組織データ 1、販売: 販売組織データ 2、および販売: 一般/プラントデータを選択し、続行を選択します。 | 組織レベル画面が表示されます。 |  |
| 5 | 組織レベルデータを入力する | 組織レベル画面の組織レベルセクションで、以下のエントリを入力し、続行を選択します。プラント: <1010>など販売組織: <1010 (プラント 1010 の場合)>など流通チャネル: <10>など | 品目登録 (選定可能品目)画面が表示されます。画面下部に、品目は登録されており、拡張されますというシステムメッセージが表示されます。 |  |
| 6 | 販売データを入力する | 品目登録 CBPTS001 (選定可能品目)画面の販売: 販売組織 1タブで、税分類に適切な値を入力します。通常、この値は完全課税対象を表す1です。Enterを押します。 | 販売: 販売組織 2タブが表示されます。この入力値は、品目が (通常は) 完全な課税対象であることを示します。 |  |
| 7 | 販売データを入力する | 販売: 販売組織 2タブのグループ化条件セクションで、以下のエントリを入力し、Enterを押します。明細カテゴリグループ: <0003> | 販売: 一般/プラントタブが表示されます。 |  |
| 8 | 販売データを入力する | 販売: 一般/プラントタブの一般データセクションで、以下のエントリを入力し、Enterを押します。利用可能在庫確認: <NC>など | 最終データビュー到達画面に、終了しようとしています。最初にこの品目のデータを保存しますかというメッセージが表示されます。 |  |
| 9 | データを保存する | 最終データビュー到達画面ではいを選択します。 | マスタデータ - 製品画面が表示されます。データが保存されます。 |  |

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
- related-to :: [[09-subscription-billing-and-contract-accounting/master-data-script-create-product-master-for-consumption-based-billing]]
- related-to :: [[09-subscription-billing-and-contract-accounting/mds-3ja-327]]
- related-to :: [[09-subscription-billing-and-contract-accounting/script-de-dados-mestre-criar-dados-mestre-do-produto-para-faturamento]]
- related-to :: [[09-subscription-billing-and-contract-accounting/script-de-datos-maestros-creacion-de-maestro-de-productos-para-factura]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/3JA_S4CLD2608_Master_Data_JA_XX.docx` — full document · extracted with `mammoth` · 14,998 chars in the whole document
