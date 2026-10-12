---
id: 09-subscription-billing-and-contract-accounting/sap-s-4hana-cloud-public-edition-mds-5bd-427
title: マスタデータスクリプト SAP S/4HANA Cloud Public Edition - サブスクリプション製品販売請求の登録 - MDS (5BD) (5BD_S4CLD2608_Master_Data_JA_XX)
description: "Japanese master data script (5BD) for creating subscription products in SAP Subscription Billing, Price Calculation lookup tables, and extending SBPD/SBRE products in S/4HANA."
cluster: 09-subscription-billing-and-contract-accounting
tags: [kb/subscription-billing-and-contract-accounting, topic/subscription-product-master-data]
aliases: [5BD_S4CLD2608_Master_Data_JA_XX]
keywords: [Subscription Products and Rate Plans, subscription products, rate elements, rate plan templates, pricing schemes, price lookup tables, product master data, subscription billing, sbpd product type, sbre product type]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/5BD_S4CLD2608_Master_Data_JA_XX.docx]
confidence: low
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-427
topic: 09-subscription-billing-and-contract-accounting/subscription-product-master-data
language: JA
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# マスタデータスクリプト SAP S/4HANA Cloud Public Edition - サブスクリプション製品販売請求の登録 - MDS (5BD) (5BD_S4CLD2608_Master_Data_JA_XX)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/5BD_S4CLD2608_Master_Data_JA_XX.docx`, extracted with `mammoth`. Grouped under **Subscription Products and Rate Plans** in Subscription Billing and Contract Accounting. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

| <!-- image omitted: unnamed --> | マスタデータスクリプトSAP S/4HANA Cloud Public Edition - 02-07-26 |
| --- | --- |
|  | サブスクリプション製品販売請求の登録 - MDS (5BD) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

目次

[1 目的 2](#_Toc233891701)

[2 前提条件 3](#_Toc233891702)

[2.1 システムアクセス 3](#_Toc233891703)

[2.2 ロール 3](#_Toc233891704)

[2.3 必要な組織ユニット (SAP S/4HANA) 3](#_Toc233891705)

[3 概要テーブル 5](#_Toc233891706)

[4 手順 6](#_Toc233891707)

[4.1 サブスクリプション製品の登録 (SAP Subscription Billing) 6](#_Toc233891708)

[4.1.1 料金要素の登録 6](#_Toc233891709)

[4.1.2 料金プランテンプレートの登録 8](#_Toc233891710)

[4.1.3 製品の登録 9](#_Toc233891711)

[4.1.4 価格設定スキームを使用した製品の登録 11](#_Toc233891712)

[4.1.5 価格決定用ルックアップテーブルのアップロード 14](#_Toc233891713)

[4.2 サブスクリプション製品の拡張 (SAP S/4HANA) 19](#_Toc233891714)

[4.2.1 タイプ SBPD のサブスクリプション請求製品の拡張 19](#_Toc233891715)

[4.2.2 タイプ SBRE のサブスクリプション請求製品の拡張 20](#_Toc233891716)

## 目的

この文書では、サブスクリプション製品マスタデータの登録方法について説明します。この説明には、"標準的" なシステム環境で処理するマスタデータに関連するデータセグメントが含まれています。読者は、入力値を入力する必要があるデータセグメントおよび項目について主に学習します。この範囲に該当しない項目は、UI に表示される場合でもこの文書では説明していません。

この説明どおりに登録されるサブスクリプションマスタレコードは、サブスクリプション請求で使用することができます。

| サブスクリプション製品 ID | 説明 | 用途 |
| --- | --- | --- |
| P-CLOUD_STORAGE | サブスクリプション製品 | サブスクリプション請求製品を表します。 |
| P-CLD_STORAGE_PCS | 価格計算サービス製品 | 価格計算製品を表します。 |

## 前提条件

### システムアクセス

| システム | 詳細 |
| --- | --- |
| SAP S/4HANA システム | SAP Fiori ラウンチパッドからアクセスすることができます。各自のロールに割り当てられている各種アプリにアクセスするための URL がシステム管理者から提供されます。 |
| SAP Subscription Billing | URL を使用してアクセスすることができます。このアプリケーションにアクセスするための URL は、システム管理者から提供されます。 |
| 価格計算サービス | SAP Fiori ラウンチパッドからアクセスすることができます。各自のロールに割り当てられている各種アプリにアクセスするための URL がシステム管理者から提供されます。 |

### ロール

SAP から提供される以下のビジネスロールテンプレートを使用して、ビジネスロールを登録し、それらを個別のテストユーザに割り当てます。

SAP S/4HANA

| 名称 | ID |
| --- | --- |
| マスタデータスペシャリスト - 製品データ | SAP_BR_PRODMASTER_SPECIALIST |

SAP Subscription Billing

権限設定については、システム管理者に連絡してください。

### 必要な組織ユニット (SAP S/4HANA)

マスタデータの一部のセグメントは会社の組織ユニットに依存し、一般 (共通) データは組織ユニットまたは会社コードに依存しません。以下の表は、さまざまなデータセグメントおよび関連する組織ユニットの概要を示しています。

| データセグメント | 依存対象 | 使用される組織ユニット | 使用される組織ユニット |
| --- | --- | --- | --- |
| マスタデータレコードの登録 | 販売組織 | 1710 (国内販売組織 US) | ドイツの場合は 1010 (国内販売組織 DE) を使用 |
| マスタデータレコードの登録 | 流通チャネル | 10 (直販) | 10 (直販) |

## 概要テーブル

このマスタレコードは、以下の表に示されている複数のセグメントで構成されます。

| セグメント | ビジネスロール | アプリ/トランザクション | 予想される結果 |
| --- | --- | --- | --- |
| サブスクリプション製品の登録 (SAP Subscription Billing) | 該当なし | 該当なし | サブスクリプション製品が登録されます。 |
| サブスクリプション製品の登録 (SAP S/4HANA) | SAP_BR_PRODMASTER_SPECIALIST | 製品マスタデータ管理 | サブスクリプション製品が登録されます。 |

## 手順

このセクションには、このマスタレコードに含まれる各セグメントまたはプロセスステップの手順が記載されています。

### サブスクリプション製品の登録 (SAP Subscription Billing)

#### 料金要素の登録

目的

このアクティビティでは、SAP Subscription Billing の料金要素を登録します。これらの料金 ID は、タイプ SBRE の関連 S/4HANA 製品に対応している必要があります。

| 料金 ID | 料金タイプ | 内容説明 |
| --- | --- | --- |
| R-ONETIME | ワンタイム | ワンタイム有効化手数料 |
| R-SEATS | 繰返 | シート基準の月額料金 |
| R-TRAFFIC | 使用量ベース | 通信量基準の使用料 |

手順

| テストステップ番号 | テストステップ名 | 指示 | 予想される結果 | コメント |
| --- | --- | --- | --- | --- |
| 1 | ログオンする | SAP Subscription Billing ラウンチパッドにログオンします。 | ホームページが表示されます。 |  |
| 2 | 料金要素にナビゲートする | マスタデータおよび設定でビジネスコンフィグレーション管理 > 料金要素を選択します。 | 料金要素ビューが表示されます。 |  |
| 3 | 料金要素を登録するR-ONETIME | 登録 > ワンタイムを選択し、以下のデータを更新します。ID: R-ONETIME単位: 各 (EA)ラベル: ワンタイム有効化手数料データソース: なしワンタイムタイプ: 初回料手数料請求タイプ: 請求テキスト: テキスト (例:ワンタイム有効化手数料) を更新します。有効: 選択保存を選択します。 | R-ONETIME 料金要素が登録されます。 |  |
| 4 | 料金要素を登録するR-SEATS | 登録を選択し、以下のデータを更新します。タイプ: 繰返ID: R-SEATS単位: 各 (EA)ラベル: シート基準の月額料金データソース: サブスクリプション請求タイプ: 請求テキスト: テキスト (例: シート基準の月額料金) を更新します。有効: 選択保存を選択します。 | R-SEATS 料金要素が登録されます。 |  |
| 5 | 料金要素を登録するR-TRAFFIC | 登録を選択し、以下のデータを更新します。タイプ: 使用量ベースID: R-TRAFFIC単位: 個 (EA)ラベル: 通信量基準の使用料データソース: 使用量請求タイプ: 請求料金サブ要素の使用: 選択(PCS 製品の場合のみ)使用量料金設定バリアント: 集約済技術リソース ID のタイプ: クラウドストレージ領域 IDテキスト: テキストを更新 (例: アップロード/ダウンロード通信量)有効: 選択保存を選択します。 | R-TRAFFIC 料金要素が登録されます。 |  |

|  |
| --- |
| 注記 技術リソースにより、技術システムでのサブスクライバおよびサブスクライブされたサービスが識別されます。これらは、サービスの使用量に基づいて顧客に課金する場合に必要です。たとえば、電力消費量の計測の場合、ここでは技術リソース ID のタイプ:を '電力メータ ID' として定義することができます。これは、使用量が転記される対象の一意の ID (EM392734-A など) です。走行距離が測定されるシナリオでは、技術リソース ID のタイプ:を '車両ライセンス番号' として定義することができます。これは、ユーザ入力項目であり、サービス/シナリオに従って定義されます。 |

#### 料金プランテンプレートの登録

目的

このアクティビティでは、SAP Subscription Billing の料金プランテンプレートを登録します。

手順

| テストステップ番号 | テストステップ名 | 指示 | 予想される結果 | コメント |
| --- | --- | --- | --- | --- |
| 1 | ログオンする | SAP Subscription Billing にログオンします。 | ホームページが表示されます。 |  |
| 2 | 料金プランテンプレートにナビゲートする | 価格設定で、料金プランテンプレート管理アプリを選択します。 | 利用可能な料金プランテンプレートが表示されます。 |  |
| 3 | 料金プランテンプレートを登録する | 登録 > 価格スキーマなしを選択し、一般情報で以下のデータを更新します。テキスト: シート基準のプランテンプレート請求サイクル: 毎月 (月の初日)通貨: 値 - USD (国別バージョン US の場合) | 料金プランテンプレート画面が表示されます。 |  |
| 4 | 料金要素の請求額/クレジットを更新する | 請求額/クレジットセクションで、請求額/クレジットを選択し、追加を選択して、ワンタイムを選択します。次に、以下のデータを更新します。料金要素: R-ONETIME価格: 100 USD請求額/クレジットの場合は、登録を選択し、繰返を選択してから、パーセント価格決定手数料を選択します。次に、以下のデータを更新します。料金要素: R-SEATS次のサイクルで変更を適用: 選択事前請求: 選択初回サイクル比例配分: 選択単価: 10 USD比率: 100請求額/クレジットの場合、追加を選択し、使用量のブロック価格設定を選択します。次に、以下のデータを更新します。料金要素: R-TRAFFIC料金サブ要素: 料金サブ要素の更新[料金要素の登録](#unique_7) [ ページ] 6ステップで料金サブ要素の使用オプションが有効になっている場合。注記 料金サブ要素の使用オプションがステップで有効化されている場合、料金サブ要素は必須項目です。次のサイクルで変更を適用: 未選択含まれる数量: 値 - 1:ブロックサイズ: 値 - 1:ブロック別価格: 値 – 1 USD (国別バージョン US の場合)登録を選択します。次に、公開を選択します。 | 請求額/クレジットが登録されます。 |  |

#### 製品の登録

目的

このアクティビティでは、SAP Subscription Billing の製品 P-CLOUD_STORAGE を登録します。SAP Subscription Billing の製品 ID は、SAP S/4HANA の関連製品 ID に対応している必要があります。

手順

| テストステップ番号 | テストステップ名 | 指示 | 予想される結果 | コメント |
| --- | --- | --- | --- | --- |
| 1 | ログオンする | SAP Subscription Billing にログオンします。 | ホームページが表示されます。 |  |
| 2 | 製品にナビゲートする | マスタデータおよび設定で、製品管理アプリを開きます。 | 利用可能な製品が表示されます。 |  |
| 3 | 一般製品情報を更新する | 登録を選択し、一般情報領域で以下のデータを更新します。製品名: クラウドストレージ製品 ID: P-CLOUD_STORAGEサブスクリプションタイプ: 商用保留としてサブスクリプションを登録: 選択解除済サブスクリプションプロファイル: S/4 統合 | 一般情報が更新されました。 |  |
| 4 | 製品の料金プランを更新する | 料金プランで、登録 > 価格設定スキームなしを選択し、以下のデータを更新します。注記 価格設定スキームを必要とする製品を使用している場合は、価格設定スキームありを選択する必要があります。価格設定スキームあり/なしの価格設定の概要については、SAP Subscription Billing 文書の[価格設定](https://help.sap.com/docs/subscription-billing/feature-overview/pricing)を参照してください。マーケット: 米国東部 (国別バージョン US の場合)料金プランテンプレート: シート基準のプランテンプレートテキスト: 繰返料金プラン (シート基準)請求サイクル: 毎月 (月の初日)登録を選択します。 | その製品の料金プランが更新されました。 |  |
| 5 | サブスクリプション期間を更新する | サブスクリプション期間で、以下を更新します。予測期間: 12 など最短期間: 12更新期間: 12引出期間: 14 | サブスクリプション期間が更新されます。 |  |
| 6 | 製品を登録する | 製品全体に対して、登録を選択します。次に、公開を選択します。 | P-CLOUD_STORAGE 製品が登録されます。 |  |

#### 価格設定スキームを使用した製品の登録

サンプル使用ケースを利用して実行する場合は、サンプル値を使用してデータを最初から登録するか、すべての新規テナントで提供される事前定義設定を使用することができます。価格設定スキームありで製品を登録する前に、価格計算サービスで以下のステップを実行する必要があります。

価格設定スキームを使用した価格設定の設定方法 (例を使用) の詳細については、[価格設定スキームを使用した価格設定設定ガイド](https://help.sap.com/docs/subscription-billing/pricing-configuration/pricing-with-pricing-schemes-configuration-guide)を参照してください。

手順

1.フィールドカタログ管理

サンプルデータを使用する場合、フィールドカタログ管理アプリでは事前定義済のフィールドカタログが使用されます。そのため、ここで追加設定を行う必要はありません。フィールドカタログ管理アプリでは、後で価格要素指定のルックアップテーブルおよび入力プロパティを定義するために使用されるフィールドを登録することができます。

2.ルックアップテーブルを登録する

ルックアップテーブル管理アプリで、入力フィールドのセットを出力フィールドのセットにマッピングすることで、ルックアップテーブルを登録することができます。登録したルックアップテーブルは、後のステップで価格要素指定を登録するために使用されます。このステップの目的は、ワンタイム料金、繰返料金、および使用量に対する料金のルックアップテーブルを登録することです。

- OneTimePrice
- RecurringPrice
- UsagePrice
- Discount1

これらのテーブルは事前定義済コンテンツに含まれています。そのため、このステップで追加の設定を行う必要はありません。

3.価格要素指定

価格要素指定の管理アプリで、価格要素指定を登録して価格設定を定義します。これには、価格設定ロジックおよび上書き可能フィールドの設定が含まれています。

- OneTimePrice
- RecurringPrice
- UsagePrice
- Discount1

|  |
| --- |
| 注記 上記の要素の価格要素指定が更新されていない場合は、個別の要素 (上書き可能フィールド > 追加/登録 > 価格/割引 > 保存) を選択して価格要素指定の管理で更新する必要があります。 |

4.価格設定スキーム

価格設定スキーム管理アプリで、価格設定スキームを登録および更新します。価格設定スキームは、特定の価格設定対象文書の価格要素指定についての用途と関係を定義する手順です。また、価格設定済文書で総額を生成するために、これらの指定を実行する順序も決定されます。

価格設定スキームの '初期値' は、事前定義済コンテンツに含まれています。そのため、このステップで追加の設定を行う必要はありません。

5.料金プランテンプレートを登録する

| テストステップ番号 | テストステップ名 | 指示 | 予想される結果 | コメント |
| --- | --- | --- | --- | --- |
| 1 | ログオンする | SAP Subscription Billing にログオンします。 | ホームページが表示されます。 |  |
| 2 | 料金プランテンプレートアプリにナビゲートする | 価格設定 > 料金プランテンプレート管理に移動します。 | 料金プランテンプレートが表示されます。 |  |
| 3 | 登録を選択する | 登録 > 価格設定スキームありを選択し、一般情報で以下のデータを更新します。テキスト: 価格計算用料金プランテンプレートタグ: PCS (オプション)価格設定スキーム: 初期値請求サイクル: 毎月 (月の初日)課金管理プロファイル: 初期設定通貨: USD | 一般情報が更新されています。 |  |
| 4 | 料金要素の課金/クレジットを更新する | ワンタイムの場合、課金/クレジット > 登録 > ワンタイムを選択し、料金要素にR-ONETIMEを入力します。上書き可能フィールド詳細 > 登録 > 割引 1を選択し、ワンタイム価格を選択します。適用を選択します。繰返の場合、課金/クレジット > 登録 > 繰返を選択し、料金要素にR-SEATSを入力します。上書き可能フィールド詳細 > 登録 > 割引 1を選択し、繰返価格を選択します。適用を選択します。使用料の場合、課金/クレジット > 登録 > 使用量のブロック価格設定を選択し、料金要素にR-TRAFFICと料金サブ要素を入力します。注記 料金サブ要素の使用オプションが[料金要素の登録](#unique_7) [ ページ] 6ステップで有効化されている場合、料金サブ要素は必須項目です。上書き可能フィールド詳細 > 登録 > 割引 1を選択し、使用量に対する価格を選択します。適用を選択します。登録を選択し、公開を選択します。 |  |  |

6.製品を登録する

SAP Subscription Billing で製品P-CLOUD_STORAGE_PCを登録します。SAP Subscription Billing の製品 ID は、SAP S/4HANA の関連製品 ID に対応している必要があります。以下の手順を使用できます。

| テストステップ番号 | テストステップ名 | 指示 | 予想される結果 | コメント |
| --- | --- | --- | --- | --- |
| 1 | ログオンする | SAP Subscription Billing にログオンします。 | ホームページが表示されます。 |  |
| 2 | 製品にナビゲートする | マスタデータおよび設定で、製品管理アプリを開きます。 | 利用可能な製品が表示されます。 |  |
| 3 | 一般製品情報を更新する | 登録を選択し、一般情報領域で以下のデータを更新します。製品名: クラウドストレージ価格計算製品 ID: P-CLOUD_STORAGE_PCサブスクリプションタイプ: 商用サブスクリプションを保留として作成: 選択解除 | 一般情報が更新されました。 |  |
| 4 | 製品の料金プランを更新する | 料金プランタブで、登録 - > 価格設定スキームなしを選択します。テンプレート登録にナビゲートし、以下のデータを更新します。マーケット: 米国東部 (国別バージョン US の場合)料金プランテンプレート: 価格計算用料金プランテンプレートテキスト: 価格計算用料金プランテンプレート請求サイクル: 毎月 (月の初日)登録を選択します。 | その製品の料金プランが更新されました。 |  |
| 5 | サブスクリプション期間を更新する | サブスクリプションパラメータの、サブスクリプション期間領域で、以下のデータを更新します。予測期間: 12 など最小期間: 12更新期間: 12取り消し期間: 14 | サブスクリプション期間が更新されます。 |  |
| 6 | 製品を登録する | 製品ビューで登録を選択します。公開を選択します。 | 製品P-CLOUD_STORAGE_PCが登録されます。 |  |

7.価格決定用のルックアップテーブルをアップロードする

ルックアップテーブルのアップロードの詳細については、[価格決定用ルックアップテーブルのアップロード](#unique_11) [ ページ] 14を参照してください。

#### 価格決定用ルックアップテーブルのアップロード

以下の手順を使用して、ワンタイム料金、繰返料金、使用量に対する料金、および割引のルックアップテーブルをアップロードすることができます。レーティングプロセスの一環として価格を決定する際には、結果テーブルのデータを使用して関連する価格を特定します。

表 1: ワンタイムテーブルのアップロード

| テストステップ番号 | テストステップ名 | 指示 | 予想される結果 | コメント |
| --- | --- | --- | --- | --- |
| 1 | ログオンする | SAP Price Calculation にログオンします。 | ホームページが表示されます。 |  |
| 2 | 料金プランテンプレートにナビゲートする | マスタデータ管理で、ルックアップテーブルデータ管理アプリを開きます。 | ルックアップテーブルが表示されます。 |  |
| 3 | OneTimePriceを選択する | ルックアップテーブルOneTimePriceを選択します。空のテーブルをダウンロードし、CSV ファイルとしてローカルに保存します。ヒント ダウンロードしたファイルの書式が列区切りでない場合は、スプレッドシートの書式を米国の書式に変更する必要があります。 |  |  |
| 4 | ダウンロードファイルを更新する | 以下の値を入力し、ファイルを保存します。productCode: P-CLOUD_STORAGE_PCmarketId: A1rateElement: R-ONETIMEprice: Singleprice (Price Type): Fixedprice (Value): 5000price (Value Currency): USD |  |  |
| 5 | CSV ファイルをアップロードする | ルックアップテーブルOneTimePriceを選択し、インポート > ブラウズに移動して、前のステップで保存したファイルをアップロードします。注記 インポートには 2 つのタイプがあります。既存のデータをそのまま維持するには、マージを選択します。インポートをクリックします。 | ルックアップテーブルOneTimePriceが更新されます。 |  |

表 2: 繰返テーブルのアップロード

| テストステップ番号 | テストステップ名 | 指示 | 予想される結果 | コメント |
| --- | --- | --- | --- | --- |
| 1 | ログオンする | SAP Price Calculation にログオンします。 | ホームページが表示されます。 |  |
| 2 | 料金プランテンプレートにナビゲートする | マスタデータ管理で、ルックアップテーブルデータ管理アプリを開きます。 | ルックアップテーブルが表示されます。 |  |
| 3 | RecurringPriceを選択する | ルックアップテーブルRecurringPriceを選択します。空のテーブルをダウンロードし、CSV ファイルとしてローカルに保存します。ヒント ダウンロードしたファイルの書式が列区切りでない場合は、スプレッドシートの書式を米国の書式に変更する必要があります。 |  |  |
| 4 | ダウンロードファイルを更新する | 以下の値を入力し、ファイルを保存します。productCode: P-CLOUD_STORAGE_PCmarketId: A1rateElement: R-SEATSprice: Singleprice (Price Type): Linearprice (Value): 50price (Value Currency): USDprice (Quantity Value): 1price (Quantity Unit): EA |  |  |
| 5 | CSV ファイルをアップロードする | ルックアップテーブルRecurringPriceを選択し、インポート > ブラウズに移動して、前のステップで保存したファイルをアップロードします。注記 インポートには 2 つのタイプがあります。既存のデータをそのまま維持するには、マージを選択します。インポートをクリックします。 | ルックアップテーブルRecurringPriceが更新されます。 |  |

表 3: 使用量テーブルのアップロード

| テストステップ番号 | テストステップ名 | 指示 | 予想される結果 | コメント |
| --- | --- | --- | --- | --- |
| 1 | ログオンする | SAP Price Calculation にログオンします。 | ホームページが表示されます。 |  |
| 2 | 料金プランテンプレートにナビゲートする | マスタデータ管理で、ルックアップテーブルデータ管理アプリを開きます。 | ルックアップテーブルが表示されます。 |  |
| 3 | UsagePriceを選択する | ルックアップテーブルUsagePriceを選択します。空のテーブルをダウンロードし、CSV ファイルとしてローカルに保存します。ヒント ダウンロードしたファイルの書式が列区切りでない場合は、スプレッドシートの書式を米国の書式に変更する必要があります。 |  |  |
| 4 | ダウンロードファイルを更新する | 以下の値を入力し、ファイルを保存します。productCode: P-CLOUD_STORAGE_PCmarketId: A1rateElement: R-TRAFFICprice: Volumeprice (Price Type): Linear高料金のサブ要素に対し、階層ごとに以下の特定の値を使用することができます。rateSubElement: 高price (Range): 500price (Range Unit): EAprice (Value): 30price (Value Currency): USDprice (Quantity Value): 1price (Quantity Unit): EA階層ごとに以下の特定の値を使用することができます。rateSubElement: 高price (Range): 1000price (Range Unit): EAprice (Value): 25price (Value Currency): USDprice (Quantity Value): 1price (Quantity Unit): EA階層ごとに以下の特定の値を使用することができます。rateSubElement: 高price (Range):price (Range Unit): EAprice (Value): 20price (Value Currency): USDprice (Quantity Value): 1price (Quantity Unit): EA低料金のサブ要素に対し、階層ごとに以下の特定の値を使用することができます。rateSubElement: 低price (Range): 500price (Range Unit): EAprice (Value): 15price (Value Currency): USDprice (Quantity Value): 1price (Quantity Unit): EA低料金のサブ要素に対し、階層ごとに以下の特定の値を使用することができます。rateSubElement: 低price (Range): 1000price (Range Unit): EAprice (Value): 10price (Value Currency): USDprice (Quantity Value): 1price (Quantity Unit): EA低料金のサブ要素に対し、階層ごとに以下の特定の値を使用することができます。rateSubElement: 低price (Range):price (Range Unit): EAprice (Value): 5price (Value Currency): USDprice (Quantity Value): 1price (Quantity Unit): EA |  |  |
| 5 | CSV ファイルをアップロードする | ルックアップテーブルUsagePriceを選択し、インポート > ブラウズに移動して、前のステップで保存したファイルをアップロードします。注記 インポートには以下の 2 つのタイプがあります。既存のデータをそのまま維持するには、マージを選択します。インポートをクリックします。 | ルックアップテーブルUsagePriceが更新されます。 |  |

表 4: 割引テーブルのアップロード

| テストステップ番号 | テストステップ名 | 指示 | 予想される結果 | コメント |
| --- | --- | --- | --- | --- |
| 1 | ログオンする | SAP Price Calculation にログオンします。 | ホームページが表示されます。 |  |
| 2 | 料金プランテンプレートにナビゲートする | マスタデータ管理で、ルックアップテーブルデータ管理アプリを開きます。 | ルックアップテーブルが表示されます。 |  |
| 3 | Discount1を選択する | ルックアップテーブルDiscount1を選択します。空のテーブルをダウンロードし、CSV ファイルとしてローカルに保存します。ヒント ダウンロードしたファイルの書式が列区切りでない場合は、スプレッドシートの書式を米国の書式に変更する必要があります。 |  |  |
| 4 | ダウンロードファイルを更新する | 以下の値を入力し、ファイルを保存します。marketId: A1discount: Singlediscount (Price Type): Percentagediscount (value): 0.1 |  |  |
| 5 | CSV ファイルをアップロードする | ルックアップテーブルDiscount1を選択し、インポート > ブラウズに移動して、前のステップで保存したファイルをアップロードします。注記 インポートには 2 つのタイプがあります。既存のデータをそのまま維持するには、マージを選択します。インポートをクリックします。 | ルックアップテーブルDiscount1が更新されます。 |  |

### サブスクリプション製品の拡張 (SAP S/4HANA)

#### タイプ SBPD のサブスクリプション請求製品の拡張

目的

このアクティビティでは、SAP S/4HANA でサブスクリプション請求製品 P-CLOUD_STORAGE を拡張します。この製品は、サブスクリプション課金管理で登録され、SAP S/4HANA に複製され、スコープアイテム 57Z の一部として製品の複製が設定されると使用可能になります。製品の複製の詳細については、[製品および料金要素を複製する iFlow パッケージの設定](https://help.sap.com/docs/CLOUD_TO_CASH_OD/a78a4be305be4dbc903bd826a1aba456/93e79ab9ec8e4dc49bc1710e396608ed.html)を参照してください。

|  |
| --- |
| 注記 ブラジル固有の項目では、適切な税計算が必要です。この詳細については、品目マスタデータ > マスタデータの BR 固有項目の定義 > ブラジルのマスタデータ登録 (JD0_BR) を参照してください。 |

手順

| テストステップ番号 | テストステップ名 | 指示 | 予想される結果 | コメント |
| --- | --- | --- | --- | --- |
| 1 | ログオンする | SAP Fiori ラウンチパッドにマスタデータスペシャリスト - 製品データとしてログオンします。 | ホームページが表示されます。 |  |
| 2 | SAP Fiori アプリにアクセスする | 製品マスタデータ管理タイルを選択します。 | 製品マスタデータ管理アプリが表示されます。 |  |
| 3 | 製品を検索する | 上部の検索領域で、製品: P-CLOUD_ STORAGEおよびP-CLOUD_ STORAGE_PCを入力します。Goを選択します。 | 製品がレポート一覧に表示されます。 |  |
| 4 | 製品を開き、流通チェーン: 一般情報を更新する | レポート一覧から製品を選択します。製品番号: P-CLOUD_STORAGE基本単位: EA製品タイプ: SBPD (サブスクリプション請求製品)テキスト: クラウドストレージOKを選択します。注記 テキストで、特定の地域の言語および製品の詳細を入力します。たとえば、言語: 英語および製品: サブスクリプション請求製品。 | 製品が開き、一般情報が更新されます。 |  |
| 5 | 流通チェーン更新: 一般情報 | 製品ビューの流通チェーン領域で登録を選択し、以下のデータを更新します。販売組織: 1710 (国内販売組織 US)流通チャネル: 10 (直販)注記 MDI を使用している場合は、SBPD製品タイプに流通チェーンは必要ありません。これらは、Cloud Integration を使用している場合にのみ必要です。 |  | ドイツ国別バージョンの場合は、1710 ではなく以下の値を更新します。販売組織: 1010 (国内販売組織 DE)その他のエントリは両方の国で同じです。 |
| 6 | 流通チェーン更新: グループ化条件を更新する | グループ化条件領域にナビゲートし、以下のデータを更新します。明細カテゴリグループ: SBPD (サブスクリプション請求製品)勘定設定グループ: X9 (定期サービス)税分類: 1 (全課税)次に、適用 > 登録を選択します。注記 MDI を使用している場合は、SBPD製品タイプに明細カテゴリグループは必要ありません。これは、Cloud Integration を使用している場合にのみ必要です。 | グループ化条件が更新され、製品が保存されます。 | ドイツ国別バージョンの場合は、1 (全課税) ではなく以下の値を更新します。税分類: 6 (全課税 (サービス))その他のエントリは両方の国で同じです。 |
| 7 | プラントを更新する | プラント > 登録にナビゲートし、以下のデータを更新します。プラント: 1710 (プラント US)適用 > 保存を選択します。 | プラントデータが更新されます。 |  |

#### タイプ SBRE のサブスクリプション請求製品の拡張

目的

このアクティビティでは、SAP Subscription Billing の料金要素に対応する以下の SAP S/4HANA のサブスクリプション製品を拡張します。製品は Subscription Billing で登録され、SAP S/4HANA に複製されます。57Z スコープアイテムの設定ガイドに記載されているように製品の複製が設定されるか、[製品および料金要素複製](https://help.sap.com/docs/CLOUD_TO_CASH_OD/a78a4be305be4dbc903bd826a1aba456/9dbec8b5ce1841a6a39f0af5571ed63b.html?version=latest)を参照すると、料金要素が使用可能になります。

|  |
| --- |
| 注記 ブラジル固有の項目では、適切な税計算が必要です。この詳細については、品目マスタデータ > マスタデータの BR 固有項目の定義 > ブラジルのマスタデータ登録 (JD0_BR) のチェックを参照してください。 |

| 製品 ID | 製品タイプ | 説明 |
| --- | --- | --- |
| R-ONETIME | SBRE | ワンタイム有効化手数料 |
| R-SEATS | SBRE | シート基準の月額料金 |
| R-TRAFFIC | SBRE | 通信量基準の使用料 |

手順

製品: R-ONETIME

| テストステップ番号 | テストステップ名 | 指示 | 予想される結果 | コメント |
| --- | --- | --- | --- | --- |
| 1 | ログオンする | SAP Fiori ラウンチパッドにマスタデータスペシャリスト - 製品データとしてログオンします。 | ホームページが表示されます。 |  |
| 2 | SAP Fiori アプリにアクセスする | 製品マスタデータ管理タイルを選択します。 | 製品マスタデータ管理アプリが表示されます。 |  |
| 3 | 製品を検索する | 上部の検索領域で、製品: R-ONETIMEを入力します。Goを選択します。 | 製品がレポート一覧に表示されます。 |  |
| 4 | 製品を開き、流通チェーン: 一般情報を更新する | 製品ビューの流通チェーン領域で登録を選択し、以下のデータを更新します。販売組織: 1710 (国内販売組織 US)流通チャネル: 10 (直販)注記 テキストで、特定の地域の言語および製品の詳細を入力します。たとえば、言語: 英語および製品: サブスクリプション請求製品。 | 製品が開き、一般情報が更新されます。 | ドイツ国別バージョンの場合は、1710 ではなく以下の値を更新します。販売組織: 1010 (国内販売組織 DE)その他のエントリは両方の国で同じです。 |
| 5 | 流通チェーン更新: グループ化条件を更新する | グループ化条件領域にナビゲートし、以下のデータを更新します。勘定設定グループ: X9 (定期サービス)税分類: 1 (全課税)次に、適用、登録の順に選択します。注記 MDI を使用している場合は、製品タイプSBREに明細カテゴリグループは必要ありません。 | グループ化条件が更新され、製品が保存されます。 | ドイツ国別バージョンの場合は、1 (全課税) ではなく以下の値を更新します。税分類: 6 (全課税 (サービス))その他のエントリは両方のバージョンで同じです。 |
| 6 | プラントを更新する | プラント領域にナビゲートし、登録を選択して以下のデータを更新します。プラント: 1710 (プラント US)適用および保存を選択します。 | プラントデータが更新されます。 | ドイツ国別バージョンの場合は、以下の値を更新します。プラント: プラント 10101 (プラント DE) |

製品: R-SEATS

| テストステップ番号 | テストステップ名 | 指示 | 予想される結果 | コメント |
| --- | --- | --- | --- | --- |
| 1 | ログオンする | SAP Fiori ラウンチパッドにマスタデータスペシャリスト - 製品データとしてログオンします。 | ホームページが表示されます。 |  |
| 2 | SAP Fiori アプリにアクセスする | 製品マスタデータ管理タイルを選択します。 | 製品マスタデータ管理アプリが表示されます。 |  |
| 3 | 製品を検索する | 上部の検索領域で、次のように入力します。製品: R-SEATSGo ボタンを押します。 | 製品がレポート一覧に表示されます。 |  |
| 4 | 製品を開き、流通チェーン: 一般情報を更新する | 製品ビューの流通チェーン領域で登録を選択し、以下のデータを更新します。販売組織: 1710 (国内販売組織 US)流通チャネル: 10 (直販)注記 テキストで、特定の地域の言語および製品の詳細を入力します。たとえば、言語: 英語および製品: サブスクリプション請求製品。 | 製品が開き、一般情報が更新されます。 | ドイツ国別バージョンの場合は、1710 ではなく以下の値を更新します。販売組織: 1010 (国内販売組織 DE)その他のエントリは両方の国で同じです。 |
| 5 | 流通チェーン更新: グループ化条件を更新する | グループ化条件領域にナビゲートし、以下のデータを更新します。勘定設定グループ: X9 (定期サービス)税分類: 1 (全課税)適用を選択します。 | グループ化条件が更新され、製品が保存されます。 | ドイツ国別バージョンの場合は、1 (全課税) ではなく以下の値を更新します。税分類: 6 (全課税 (サービス))その他のエントリは両方のバージョンで同じです。 |
| 6 | プラントを更新する | プラント領域にナビゲートし、登録を選択して以下のデータを更新します。プラント: 1710 (プラント US)適用および保存を選択します。 | プラントデータが更新されます。 | ドイツ国別バージョンの場合は、以下の値を更新します。プラント: プラント 1010 (プラント DE) |

製品: R-TRAFFIC

| テストステップ番号 | テストステップ名 | 指示 | 予想される結果 | コメント |
| --- | --- | --- | --- | --- |
| 1 | ログオンする | SAP Fiori ラウンチパッドにマスタデータスペシャリスト - 製品データとしてログオンします。 | ホームページが表示されます。 |  |
| 2 | SAP Fiori アプリにアクセスする | 製品マスタデータ管理タイルを選択します。 | 製品マスタデータ管理アプリが表示されます。 |  |
| 3 | 製品を検索する | 上部の検索領域で、次のように入力します。製品: R-TrafficGo ボタンを押します。 | 製品がレポート一覧に表示されます。 |  |
| 4 | 製品を開き、流通チェーン: 一般情報を更新する | 製品ビューの流通チェーン領域で登録を選択し、以下のデータを更新します。販売組織: 1710 (国内販売組織 US)流通チャネル: 10 (直販)注記 テキストで、特定の地域の言語および製品の詳細を入力します。たとえば、言語: 英語および製品: サブスクリプション請求製品。 | 製品が開き、一般情報が更新されます。 | ドイツ国別バージョンの場合は、1710 ではなく以下の値を更新します。販売組織: 1010 (国内販売組織 DE)その他のエントリは両方の国で同じです。 |
| 5 | 流通チェーン更新: グループ化条件を更新する | グループ化条件領域にナビゲートし、以下のデータを更新します。明細カテゴリグループ: SBRE (サブスクリプション請求料金要素)勘定設定グループ: X9 (定期サービス)税分類: 1 (全課税)適用を選択してから保存を選択します。注記 MDI を使用している場合は、製品SBREに明細カテゴリグループは必要ありません。 | 製品が保存されます。 | ドイツローカルバージョンの場合は、1 (全課税) ではなく以下の値を更新します。税分類: 6 (全課税 (サービス))その他のエントリは両方のバージョンで同じです。 |
| 6 | プラントを更新する | プラント領域にナビゲートし、登録を選択して以下のデータを更新します。プラント: 1710 (プラント US)適用を選択してから保存を選択します。 | プラントデータが更新されます。 | ドイツ国別バージョンの場合は、以下の値を更新します。プラント: プラント 10101 (プラント DE) |

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
> Flagged while digesting this document, not verified: Plant for R-SEATS in Germany given as 1010 while R-ONETIME and R-TRAFFIC use 10101; possible inconsistency within the document

> [!warning] Conflict
> Flagged while digesting this document, not verified: Product ID for the pricing-scheme product appears as P-CLD_STORAGE_PCS in the overview table but P-CLOUD_STORAGE_PC in the procedures

## Connections
- part-of :: [[_cluster]]
- related-to :: [[09-subscription-billing-and-contract-accounting/master-data-script-create-subscription-product-sales-billing-mds-5bd-4]]
- related-to :: [[09-subscription-billing-and-contract-accounting/mds-5bd-429]]
- related-to :: [[09-subscription-billing-and-contract-accounting/script-de-dados-mestre-criar-faturamento-de-vendas-de-produto-de-assin]]
- related-to :: [[09-subscription-billing-and-contract-accounting/script-de-datos-maestros-crear-facturacion-de-ventas-de-productos-de-s]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/5BD_S4CLD2608_Master_Data_JA_XX.docx` — full document · extracted with `mammoth` · 22,160 chars in the whole document
