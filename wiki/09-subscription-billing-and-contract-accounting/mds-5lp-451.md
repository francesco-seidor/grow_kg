---
id: 09-subscription-billing-and-contract-accounting/mds-5lp-451
title: サブスクリプション製品統合請求の登録 - MDS (5LP) (5LP_S4CLD2608_Master_Data_JA_XX)
description: "Japanese master data script (5LP) for SAP S/4HANA Cloud Public Edition 2608: creating BPs, contract accounts, and subscription products in SAP Subscription Billing and S/4HANA."
cluster: 09-subscription-billing-and-contract-accounting
tags: [kb/subscription-billing-and-contract-accounting, topic/subscription-product-master-data]
aliases: [5LP_S4CLD2608_Master_Data_JA_XX]
keywords: [Subscription Products and Rate Plans, subscription products, subscription billing, master data script, business partner, contract accounts, rate elements, rate plan templates, price calculation, lookup tables]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/5LP_S4CLD2608_Master_Data_JA_XX.docx]
confidence: low
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-451
topic: 09-subscription-billing-and-contract-accounting/subscription-product-master-data
language: JA
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# サブスクリプション製品統合請求の登録 - MDS (5LP) (5LP_S4CLD2608_Master_Data_JA_XX)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/5LP_S4CLD2608_Master_Data_JA_XX.docx`, extracted with `mammoth`. Grouped under **Subscription Products and Rate Plans** in Subscription Billing and Contract Accounting. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

| <!-- image omitted: unnamed --> | マスタデータスクリプトSAP S/4HANA Cloud Public Edition - 02-07-26 |
| --- | --- |
|  | サブスクリプション製品統合請求の登録 - MDS (5LP) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

目次

[1 目的 3](#_Toc233891707)

[2 前提条件 4](#_Toc233891708)

[2.1 システムアクセス 4](#_Toc233891709)

[2.2 ロール 4](#_Toc233891710)

[2.3 必要な組織ユニット (SAP S/4HANA) 4](#_Toc233891711)

[3 概要テーブル 6](#_Toc233891712)

[4 手順 7](#_Toc233891713)

[4.1 ビジネスパートナの登録 7](#_Toc233891714)

[4.1.1 得意先マスタデータの登録 8](#_Toc233891715)

[4.1.2 契約アカウントの登録 10](#_Toc233891716)

[4.2 サブスクリプション製品の登録 (SAP Subscription Billing) 12](#_Toc233891717)

[4.2.1 料金要素の登録 12](#_Toc233891718)

[4.2.2 料金プランテンプレートの登録 14](#_Toc233891719)

[4.2.3 製品の登録 (SAP Subscription Billing) 15](#_Toc233891720)

[4.2.4 価格計算サービスに対する製品の登録 17](#_Toc233891721)

[4.2.5 価格決定用ルックアップテーブルのアップロード 20](#_Toc233891722)

[4.3 サブスクリプション請求製品の拡張 25](#_Toc233891723)

[4.3.1 タイプ SBPD のサブスクリプション製品の登録 25](#_Toc233891724)

[4.3.2 タイプ SBRE のサブスクリプション製品の拡張 27](#_Toc233891725)

[5 付録 32](#_Toc233891726)

## 目的

この文書では、サブスクリプション製品マスタデータの登録方法について説明します。この説明には、"標準的" なシステム環境で処理するマスタデータに関連するデータセグメントが含まれています。ここで読者は、入力値を入力する必要があるデータセグメントおよび項目について主に学習します。この範囲に該当しない項目は、UI に表示される場合でもこの文書では説明していません。

この説明どおりに登録されるサブスクリプションマスタレコードは、サブスクリプション請求で使用することができます。

| サブスクリプション製品 ID | 説明 | 用途 |
| --- | --- | --- |
| P-CLOUD_COMM | サブスクリプション製品 | サブスクリプション製品を表します。 |
| P-CLOUD_SUPPORT | サブスクリプション製品 | サブスクリプション製品を表します。 |

## 前提条件

### システムアクセス

次の表に、システムアクセスの要件を示します。

| システム | 詳細 |
| --- | --- |
| SAP S/4HANA システム | SAP Fiori ラウンチパッドからアクセスすることができます。各自のロールに割り当てられている各種アプリにアクセスするための URL がシステム管理者から提供されます。 |
| SAP Subscription Billing | URL を使用してアクセスすることができます。このアプリケーションにアクセスするための URL は、システム管理者から提供されます。 |

### ロール

SAP から提供される以下のビジネスロールテンプレートを使用して、ビジネスロールを登録し、それらを個別のテストユーザに割り当てることができます。

SAP S/4HANA

| 名称 (ロールテンプレート) | ID (ロールテンプレート) | 名称 (ラウンチパッド領域) | ID (ラウンチパッド領域) | ログオン |
| --- | --- | --- | --- | --- |
| マスタデータスペシャリスト - 製品データ | SAP_BR_PRODMASTER_SPECIALIST | マスタデータスペシャリスト - 製品データ | SAP_BR_PRODMASTER_SPECIALIST |  |
| 未収金/未払金担当者 (FI-CA) | SAP_BR_APR_ACCOUNTANT_FICA | 未収金/未払金担当者 (FI-CA): | SAP_BR_APR_ACCOUNTANT_FICA |  |

SAP Subscription Billing

必要な権限を設定するには、システム管理者に連絡する必要があります。

### 必要な組織ユニット (SAP S/4HANA)

マスタデータの一部のセグメントは会社の組織ユニットに依存する一方で、一般 (共通) データは組織ユニットまたは会社コードに依存しません。以下の表は、さまざまなデータセグメントおよび関連する組織ユニットの概要を示しています。

| データセグメント | 依存対象 | 使用される組織ユニット | コメント |
| --- | --- | --- | --- |
| マスタデータレコードの登録 | 販売組織 | 1710 (国内販売組織 US) | ドイツの場合は 1010 (国内販売組織 DE) |
| マスタデータレコードの登録 | 流通チャネル | 10 (直販) |  |

## 概要テーブル

このマスタレコードは、以下の表に示されている複数のセグメントで構成されます。

| セグメント | ビジネスロール | アプリ/トランザクション | 予想される結果 |
| --- | --- | --- | --- |
| サブスクリプション製品の登録 (SAP Subscription Billing) | 該当なし | 該当なし | サブスクリプション製品が登録されます。 |
| サブスクリプション製品の拡張 (SAP S/4HANA) | SAP_BR_PRODMASTER_SPECIALIST | 製品マスタデータの管理 | サブスクリプション製品が登録されます。 |

## 手順

このセクションには、このマスタレコードに含まれる各セグメントまたはプロセスステップの手順が記載されています。

### ビジネスパートナの登録

コンテキスト

このアクティビティでは、S/4HANA Cloud で新しい FI-CA 得意先のビジネスパートナを登録します。

手順

| テストステップ番号 | テストステップ名 | 指示 | 予想される結果 | 合格/不合格/コメント |
| --- | --- | --- | --- | --- |
| 1. | ログオンする | 未収金/未払金担当者 (FI-CA) として SAP Fiori ラウンチパッドにログオンします。 | SAP Fiori ラウンチパッドが表示されます。 |  |
| 2 | SAP Fiori アプリにアクセスする | ビジネスパートナ更新 (BP) を開きます。 | ビジネスパートナ更新ビューが表示されます。 |  |
| 3 | ビジネスパートナを登録する | 個人を選択するか、その他 > ビジネスパートナ > 登録 > 個人を選択します。 | 個人登録ビューが表示されます。 |  |
| 4 | BP 役割を選択する | 以下のエントリを入力します。BP 役割の登録: 契約パートナ | 他 BP ロールへの変更ビューが登録モードで表示されます。 |  |
| 5 | 登録する | 登録を選択します。 | 個人登録ダイアログボックスで役割契約パートナを選択します。契約パートナ (新規) が BP 役割の登録に対して選択されます。 |  |
| 6 | 基本データを入力する | 以下のエントリを入力します。ビジネスパートナ: <特定の ID を入力> たとえば、BP_US_97グルーピング: 外部英数字採番 |  |  |
| 7 | 住所データを入力する | 住所タブで以下のエントリを入力します。名/姓: John/Miller地名/番地: Hillview Ave/3410郵便番号/市区町村: 94304/PALO ALTO国: US地域: CA税管轄: CA00000000ヒント 税管轄が表示されない場合は、+ をクリックしてオプションを展開します。 |  |  |
| 8 | 支払データを更新する | ビジネスパートナ管理アプリを使用して銀行詳細を追加し、ビジネスパートナマスタデータ管理アプリを使用して支払カードを登録します。支払処理タブで以下のエントリを入力します。銀行詳細セクションで、以下のように入力します。ID: 01国: US銀行コード: 011000390銀行口座: <銀行口座>SWIFT コード (SWIFT/BIC): CITIUS33XXX送信を選択します。 | 照合キーチェックビューがポップアップ表示されます。 |  |
| 9 | 保存する | 保存を選択します。 | 新しいビジネスパートナが登録されます。 |  |

#### 得意先マスタデータの登録

テスト管理

カスタマプロジェクト: プロジェクト固有部分への入力

|  |  |  |  |
| --- | --- | --- | --- |
| テストケース ID | <X.XX> | テスト実施日: |  |
| テスト実施者名: |  | 期間: |  |
| ビジネスロール: |  | 責任者: | <都道府県/州、サービスプロバイダ、カスタマ/共同サービスプロバイダ、およびカスタマ> |

コンテキスト

このアクティビティでは、BP 役割が FLCU01 と MKK の FI-CA ビジネスパートナを、販売エリアマスタデータで拡張します。

手順

| テストステップ番号 | テストステップ名 | 指示 | 予想される結果 | 合格/不合格/コメント |
| --- | --- | --- | --- | --- |
| 1. | ログオンする | ユーザ認証情報を使用して、SAP Fiori ラウンチパッドにログオンします。 SAP_BR_APR_ACCOUNTANT_FICA | SAP Fiori ラウンチパッドが表示されます。 |  |
| 2 | SAP Fiori アプリにアクセスする | ビジネスパートナ更新(BP) を開きます。 | ビジネスパートナ更新画面が表示されます。 |  |
| 3 | ビジネスパートナを選択する | ビジネスパートナ番号を入力します。 |  |  |
| 4 | ビジネスパートナを開く | Enterを選択します。 |  |  |
| 5 | 変更モードに切り替える | 照会と変更の切替を選択します。 |  |  |
| 6 | BP 役割を変更する | BP 役割の変更項目で、以下の値を選択します。得意先この BP 役割の技術キーは FLCU01 です。 |  |  |
| 7 | 住所の情報を入力する | 連絡文書言語: <EN> |  |  |
| 8 | 販売エリアを開く | ビューの最上部にある販売管理を選択します。 | 販売エリアビューが表示されます。 |  |
| 9 | 販売エリアデータを入力する | 以下のデータを入力します。販売組織: 1710流通チャネル: 10製品部門: 00Enterを選択して、保存を選択します。注記 上記の 3 つのエントリが販売エリアを形成します。多くの場合、販売エリアによって、たとえば受注や価格設定における販売処理の目的が設定されます。 | ビジネスパートナに対する変更が保存されます。 |  |
| 10 | 出荷データを入力する | 出荷タブの出荷セクションで、以下のデータを入力します。出荷プラント: 1710 |  |  |
| 11 | 税データを入力する | 請求タブの仮受消費税セクションで、以下のデータを入力します。税分類: <1>たとえば、値 <1> は、この得意先が完全な課税対象であることを意味します。 |  |  |
| 12 | データを保存する | エントリを保存します。 |  |  |
| 13 | BP 役割を変更する | BP 役割の変更項目で、以下の値を選択します。契約パートナこの BP 役割の技術キーは MKK です。 |  |  |
| 14 | 住所の情報を入力する | 連絡文書言語: <EN> |  |  |
| 15 | 出荷データを入力する | 出荷タブページの出荷セクションで、以下のデータを入力します。出荷プラント: 1710 |  |  |
| 16 | 税データを入力する | 請求タブページの仮受消費税セクションで、以下のデータを入力します。税分類: <1>たとえば、値 <1> は、この得意先が完全な課税対象であることを意味します。 |  |  |
| 17 | データを保存する | エントリを保存します。 |  |  |

#### 契約アカウントの登録

コンテキスト

このアクティビティでは、SAP S/4HANA Cloud Public Editionで FI-CA 得意先の契約アカウントマスタデータを登録します。

手順

| テストステップ番号 | テストステップ名 | 指示 | 予想される結果 | 合格/不合格/コメント |
| --- | --- | --- | --- | --- |
| 1 | ログオンする | 未収金/未払金担当者 (FI-CA) ビジネスロールを使用し、ユーザ認証情報を使用して SAP Fiori ラウンチパッドにログオンします。 | SAP Fiori ラウンチパッドが表示されます。 |  |
| 2 | SAP Fiori アプリにアクセスする | 契約アカウント更新(CAA3) を開きます。 | 契約情報照会: 第一画面が表示されます。 |  |
| 3 | 契約アカウントを登録する | 登録を選択するか、その他 > 契約アカウント > 登録を選択します。 | 契約アカウント登録: 第一画面が表示されます。 |  |
| 4 | 基本データを入力する | 以下のエントリを入力します。契約アカウント: <特定の ID を入力> たとえば、CA_US_97ビジネスパートナ: <ビジネスパートナの登録ステップで登録したビジネスパートナ番号を選択>契約アカウントカテゴリ: Y1有効開始: <本日の日付> |  |  |
| 5 | 契約アカウント詳細を更新する | 続行を選択します。 | 契約アカウント登録: 一般データ画面が表示されます。 |  |
| 6 | 一般データを入力する | 一般タブで以下のエントリを入力します。契約アカウント名: <契約アカウント名>アカウント関係: 口座名義人:許容範囲グループ: Y001 許可されない許容範囲計画グループ: 国内得意先支払条件: YN01勘定設定ID: Y1 |  |  |
| 7 | 支払/税データを入力する | 支払/税タブで以下のエントリを入力します。会社コード Group: 1710標準会社コード: 1710 |  |  |
| 8 | 督促処理/連絡文書を入力する | 督促処理/連絡文書タブで以下のエントリを入力します。連絡文書バリアント: <即時印刷のみ> |  |  |
| 9 | 保存する | 保存を選択します。 | 新規契約アカウントが登録されます。 |  |

### サブスクリプション製品の登録 (SAP Subscription Billing)

#### 料金要素の登録

目的

このアクティビティでは、SAP Subscription Billing の料金要素を登録します。これらの料金 ID は、タイプ SBRE の関連 S/4HANA 製品に対応している必要があります。

| 料金 ID | 料金タイプ | 内容説明 |
| --- | --- | --- |
| R-ONETIME | ワンタイム | ワンタイム有効化手数料 |
| R-SEATS | 繰返 | シート基準の月額料金 |
| R-TICKETS | 従量課金 | チケット基準の使用料 |

手順

| テストステップ番号 | テストステップ名 | 指示 | 予想される結果 | コメント |
| --- | --- | --- | --- | --- |
| 1 | ログオンする | SAP Subscription Billing にログオンします。 | ホームページが表示されます。 |  |
| 2 | 料金要素にナビゲートする | マスタデータおよび構成でビジネス設定 > 料金要素を選択します。 | 料金要素ビューが表示されます。 |  |
| 3 | 料金要素を登録するワンタイム | 登録を選択し、以下のデータを更新します。タイプ: ワンタイムID: R-ONETIME単位: 各 (EA)ラベル: ワンタイム有効化手数料データソース: なしワンタイムタイプ: 初回料手数料請求タイプ: 請求テキスト: テキスト (例:ワンタイム有効化手数料) を更新します。有効: 選択保存を選択します。 | R-One-Time 料金要素が登録されます。 |  |
| 4 | 料金要素を登録するR-SEATS | 登録を選択し、以下のデータを更新します。タイプ: 繰返ID: R-SEATS単位: 各 (EA)ラベル: シート基準の月額料金データソース: サブスクリプション請求タイプ: 請求テキスト: テキスト (例: シート基準の月額料金) を更新します。有効: 選択保存を選択します。 | R-SEATS 料金要素が登録されます。 |  |
| 5 | 料金要素を登録するR-TICKETS | 登録を選択し、以下のデータを更新します。タイプ: 使用量ベースID: R-TICKETS単位: ギガバイト (GB)/Each (EA)ラベル: チケット基準の使用料データソース: 使用量請求タイプ: 請求使用量料金設定バリアント: 集約済技術リソース ID のタイプ: クラウドストレージ領域 IDテキスト: テキスト (例: アップロード/ダウンロード通信量 (GB)) を更新します。有効: 選択保存を選択します。 | R-TICKETS 料金要素が登録されます。 |  |

#### 料金プランテンプレートの登録

目的

このアクティビティでは、SAP Subscription Billing の料金プランテンプレートを登録します。

手順

| テストステップ番号 | テストステップ名 | 指示 | 予想される結果 | コメント |
| --- | --- | --- | --- | --- |
| 1 | ログオンする | SAP Subscription Billing にログオンします。 | ホームページが表示されます。 |  |
| 2 | 料金プランテンプレートにナビゲートする | 価格設定で、料金プランテンプレートアプリを開きます。 | 利用可能な料金プランテンプレートが表示されます。 |  |
| 3 | 料金プランテンプレートを登録するSEATS | 登録 > 価格スキーマなしを選択し、一般情報で以下のデータを更新します。テキスト: シート基準のプランテンプレート請求サイクル: 値 - 毎月 (月の初日)通貨: 値 - USD (国別バージョン US の場合)追加を選択します。 | テンプレートの基本データが定義されます。 |  |
| 4 | SEATS の請求額/クレジットを更新する | 課金/クレジットセクションで、追加 > ワンタイムを選択してワンタイム請求を登録します。以下のデータを更新します。料金要素: R-ONETIME価格: 値 – 9.99 USD (国別バージョン US の場合)課金/クレジットセクションで、追加 > 繰返 > 比率価格設定を選択して繰返請求を登録します。以下のデータを更新します。料金要素: R-SEATS次のサイクルで変更を適用: 選択事前請求: 選択初回サイクル比例配分: 選択単価: 1 USD比率: 100課金/クレジットセクションで、追加 > 使用量ベース > ブロック価格設定を選択して使用量ベースの請求を登録します。以下のデータを更新します。料金要素: R-TICKETS次のサイクルで変更を適用: 未選択含まれる数量: 値 - 1:ブロックサイズ: 値 - 1:ブロック別価格: 値 – 1 USD (国別バージョン US の場合)保存、およびパブリッシュを選択します。 | 請求額/クレジットが登録されます。 |  |

#### 製品の登録 (SAP Subscription Billing)

目的

このアクティビティでは、SAP Subscription Billing で製品 P-CLOUD_COMM および P-CLOUD_SUPPORT を登録します。SAP Subscription Billing の製品 ID は、SAP S/4HANA の関連製品 ID に対応している必要があります。

手順

製品: P-CLOUD_COMM

| テストステップ番号 | テストステップ名 | 指示 | 予想される結果 | コメント |
| --- | --- | --- | --- | --- |
| 1 | ログオンする | SAP Subscription Billing にログオンします。 | ホームページが表示されます。 |  |
| 2 | 製品にナビゲートする | マスタデータおよび構成カタログでビジネス設定 > 製品を選択します。 | 利用可能な製品が表示されます。 |  |
| 3 | 一般製品情報を更新する | 登録を選択し、一般情報領域で以下のデータを更新します。製品名: クラウド通信製品 ID: P-CLOUD_COMMサブスクリプションタイプ: 商用保留としてサブスクリプションを登録: 選択解除済電子販売: 選択 | 一般情報が更新されました。 |  |
| 4 | 製品の料金プランを更新する | 料金プラン領域で、テンプレートから料金プラン登録を選択します。料金プラン登録ビューで、以下のデータを更新します。マーケット: 米国東部 (国別バージョン US の場合)料金プランテンプレート: シート基準のプランテンプレートテキスト: 繰返料金プラン (シート基準) | 製品の料金プランが更新されました。 |  |
| 5 | サブスクリプション期間を更新する | 以下のサブスクリプションパラメータ詳細を更新します。予測期間: 12 など最短期間: 12更新期間: 12引出期間: 14 | サブスクリプション期間が更新されます。 |  |
| 6 | 製品を登録する | 料金プラン登録ビューで登録を選択します。製品ビューで保存を選択します。次に、パブリッシュを選択します。 | P-CLOUD_COMM 製品が登録されます。 |  |

製品: P-CLOUD_SUPPORT

| テストステップ番号 | テストステップ名 | 指示 | 予想される結果 | コメント |
| --- | --- | --- | --- | --- |
| 1 | ログオンする | SAP Subscription Billing にログオンします。 | ホームページが表示されます。 |  |
| 2 | 製品にナビゲートする | 左側のナビゲーション領域で、製品を選択します。 | 利用可能な製品が表示されます。 |  |
| 3 | 一般製品情報を更新する | 登録を選択し、一般情報領域で以下のデータを更新します。製品名: クラウドのサポート製品 ID: P-CLOUD_SUPPORT を入力します。サブスクリプションタイプ: 商用保留としてサブスクリプションを登録: 選択解除済電子販売: 選択 | 一般情報が更新されました。 |  |
| 4 | 製品の料金プランを更新する | 料金プラン領域で、テンプレートから料金プラン登録を選択します。料金プラン登録ビューで、以下のデータを更新します。マーケット: 米国東部 (国別バージョン US の場合)料金プランテンプレート: シート基準のプランテンプレートテキスト: 繰返料金プラン (シート基準) | 製品の料金プランが更新されました。 |  |
| 5 | サブスクリプション期間を更新する | サブスクリプションパラメータ詳細を更新します。予測期間: 12 など最短期間: 12更新期間: 12引出期間: 14 | サブスクリプション期間が更新されます。 |  |
| 6 | 製品を登録する | 料金プラン登録ビューで登録を選択します。製品ビューで保存を選択します。次に、パブリッシュを選択します。 | P-CLOUD_SUPPORT 製品が登録されます。 |  |

#### 価格計算サービスに対する製品の登録

サンプル使用ケースを利用して実行する場合は、サンプル値を使用してデータを最初から登録するか、すべての新規テナントで提供される事前定義設定を使用することができます。価格計算サービスに対して製品を登録する前に、価格計算で以下のステップを実行する必要があります。

手順

1.フィールドカタログ管理

サンプルデータを使用する場合、フィールドカタログ管理アプリでは事前定義済のフィールドカタログが使用されます。そのため、ここで追加設定を行う必要はありません。フィールドカタログ管理アプリでは、後で価格要素指定のルックアップテーブルおよび入力プロパティを定義するために使用されるフィールドを登録することができます。

2.ルックアップテーブル登録

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

これらの価格要素指定は、事前定義済コンテンツに含まれています。そのため、このステップで追加の設定を行う必要はありません。

4.価格設定スキーム

価格設定スキーム管理アプリで、価格設定スキームを登録および更新します。価格設定スキームは、特定の価格設定対象文書の価格要素指定についての用途と関係を定義する手順です。また、価格設定済文書で総額を生成するために、これらの指定を実行する順序も決定されます。

価格設定スキームの '初期値' は、事前定義済コンテンツに含まれています。そのため、このステップで追加の設定を行う必要はありません。

5.料金プランテンプレート登録

| テストステップ番号 | テストステップ名 | 指示 | 予想される結果 | コメント |
| --- | --- | --- | --- | --- |
| 1 | ログオンする | SAP Subscription Billing にログオンします。 | ホームページが表示されます。 |  |
| 2 | 料金プランテンプレートアプリにナビゲートする | 価格設定 > 料金プランテンプレートに移動します。 | 料金プランテンプレートが表示されます。 |  |
| 3 | 登録を選択する | 登録 - 価格設定スキームありを選択し、一般情報で以下のデータを更新します。テキスト: 価格計算用料金プランテンプレートタグ: PCS (オプション)価格設定スキーム: 初期値請求サイクル: 毎月 (月の初日)通貨: USD | 一般情報が更新されています。 |  |
| 4 | 料金要素の課金/クレジットを更新する | ワンタイムの場合、課金/クレジット > 追加 > ワンタイムを選択し、料金要素にR-ONETIMEを入力します。繰返の場合、課金/クレジット > 追加 > 繰返を選択し、料金要素にR-SEATSを入力します。使用料の場合、課金/クレジット > 追加 > 使用量のブロック価格設定を選択し、料金要素にR-TRAFFICを入力します。保存、パブリッシュの順に選択します。 |  |  |

6.製品登録

SAP Subscription Billing で製品P-CLOUD_STORAGE_PCを登録します。SAP Subscription Billing の製品 ID は、SAP S/4HANA の関連製品 ID に対応している必要があります。以下の手順を使用できます。

| テストステップ番号 | テストステップ名 | 指示 | 予想される結果 | コメント |
| --- | --- | --- | --- | --- |
| 1 | ログオンする | SAP Subscription Billing にログオンします。 | ホームページが表示されます。 |  |
| 2 | 製品にナビゲートする | マスタデータとコンフィグレーションで、製品アプリを開きます。 | 利用可能な製品が表示されます。 |  |
| 3 | 一般製品情報を更新する | 登録を選択し、一般情報領域で以下のデータを更新します。製品名: クラウドストレージ価格計算製品 ID: P-CLOUD_STORAGE_PCサブスクリプションタイプ: 商用サブスクリプションを保留として作成: 選択解除 | 一般情報が更新されました。 |  |
| 4 | 製品の料金プランを更新する | 料金プランタブで、登録 - 価格設定スキームありを選択します。注記 価格計算製品の詳細については、[SAP Subscription Billing with Pricing Schemes](https://help.sap.com/docs/CLOUD_TO_CASH_OD/3da4082dc5094e3489b7c98e9113cf6c/3542ae740bb046b9bf422e193f3e0526.html)を参照してください。テンプレートからの料金プラン登録 > 価格設定スキームのある料金プランの登録にナビゲートし、以下のデータを更新します。マーケット: 米国東部 (国別バージョン US の場合)料金プランテンプレート: 価格計算用料金プランテンプレートテキスト: 価格計算用料金プランテンプレート請求サイクル: 毎月 (月の初日)登録を選択します。 | その製品の料金プランが更新されました。 |  |
| 5 | サブスクリプション期間を更新する | サブスクリプション期間領域で、以下のデータを更新します。予測期間: 12 など最小期間: 12更新期間: 12取り消し期間: 14 | サブスクリプション期間が更新されます。 |  |
| 6 | 製品を登録する | 料金プラン登録ビューで登録を選択します。製品ビューで保存を選択します。パブリッシュを選択します。 | 製品P-CLOUD_STORAGE_PCが登録されます。 |  |

7.価格決定用ルックアップテーブルアップロード

ルックアップテーブルのアップロードの詳細については、価格決定用ルックアップテーブルのアップロードを参照してください。

価格計算製品の詳細については、[SAP Subscription Billing with Pricing Schemes](https://help.sap.com/docs/CLOUD_TO_CASH_OD/3da4082dc5094e3489b7c98e9113cf6c/3542ae740bb046b9bf422e193f3e0526.html)を参照してください。

#### 価格決定用ルックアップテーブルのアップロード

以下の手順を使用して、ワンタイム料金、繰返料金、使用量に対する料金、および割引のルックアップテーブルをアップロードすることができます。料金設定プロセスの一環として価格を決定する際には、以下の表のデータを使用して関連する価格を特定します。

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
| 3 | UsagePriceを選択する | ルックアップテーブルOneTimePriceを選択します。空のテーブルをダウンロードし、CSV ファイルとしてローカルに保存します。ヒント ダウンロードしたファイルの書式が列区切りでない場合は、スプレッドシートの書式を米国の書式に変更する必要があります。 |  |  |
| 4 | ダウンロードファイルを更新する | 以下の値を入力し、ファイルを保存します。productCode: P-CLOUD_STORAGE_PCmarketId: A1rateElement: R-TRAFFICprice: Volumeprice (Price Type): Linear高料金のサブ要素に対し、階層ごとに以下の特定の値を使用することができます。rateSubElement: 高price (Range): 500price (Range Unit): EAprice (Value): 30price (Value Currency): USDprice (Quantity Value): 1price (Quantity Unit): EA階層ごとに以下の特定の値を使用することができます。rateSubElement: 高price (Range): 1000price (Range Unit): EAprice (Value): 25price (Value Currency): USDprice (Quantity Value): 1price (Quantity Unit): EA階層ごとに以下の特定の値を使用することができます。rateSubElement: 高price (Range):price (Range Unit): EAprice (Value): 20price (Value Currency): USDprice (Quantity Value): 1price (Quantity Unit): EA低料金のサブ要素に対し、階層ごとに以下の特定の値を使用することができます。rateSubElement: 低price (Range): 500price (Range Unit): EAprice (Value): 15price (Value Currency): USDprice (Quantity Value): 1price (Quantity Unit): EA低料金のサブ要素に対し、階層ごとに以下の特定の値を使用することができます。rateSubElement: 低price (Range): 1000price (Range Unit): EAprice (Value): 10price (Value Currency): USDprice (Quantity Value): 1price (Quantity Unit): EA低料金のサブ要素に対し、階層ごとに以下の特定の値を使用することができます。rateSubElement: 低price (Range):price (Range Unit): EAprice (Value): 5price (Value Currency): USDprice (Quantity Value): 1price (Quantity Unit): EA |  |  |
| 5 | CSV ファイルをアップロードする | ルックアップテーブルOneTimePriceを選択し、インポート > ブラウズに移動して、前のステップで保存したファイルをアップロードします。注記 インポートには 2 つのタイプがあります。既存のデータをそのまま維持するには、マージを選択します。インポートをクリックします。. | ルックアップテーブルOneTimePriceが更新されます。 |  |

表 4: 割引テーブルのアップロード

| テストステップ番号 | テストステップ名 | 指示 | 予想される結果 | コメント |
| --- | --- | --- | --- | --- |
| 1 | ログオンする | SAP Price Calculation にログオンします。 | ホームページが表示されます。 |  |
| 2 | 料金プランテンプレートにナビゲートする | マスタデータ管理で、ルックアップテーブルデータ管理アプリを開きます。 | ルックアップテーブルが表示されます。 |  |
| 3 | Discount1を選択する | ルックアップテーブルDiscount1を選択します。空のテーブルをダウンロードし、CSV ファイルとしてローカルに保存します。ヒント ダウンロードしたファイルの書式が列区切りでない場合は、スプレッドシートの書式を米国の書式に変更する必要があります。 |  |  |
| 4 | ダウンロードファイルを更新する | 以下の値を入力し、ファイルを保存します。marketId: A1discount: Singlediscount (Price Type): Percentagediscount (value): 0.1 |  |  |
| 5 | CSV ファイルをアップロードする | ルックアップテーブルDiscount1を選択し、インポート > ブラウズに移動して、前のステップで保存したファイルをアップロードします。注記 インポートには 2 つのタイプがあります。既存のデータをそのまま維持するには、マージを選択します。インポートをクリックします。. | ルックアップテーブルDiscount1が更新されます。 |  |

### サブスクリプション請求製品の拡張

#### タイプ SBPD のサブスクリプション製品の登録

目的

このアクティビティでは、SAP S/4HANA でサブスクリプション製品 P-CLOUD_COMM および P-CLOUD_SUPPORT を拡張します。これらの製品は、SAP Subscription Billing で登録され、SAP S/4HANA に複製されます。

手順

製品: P-CLOUD_COMM

| テストステップ番号 | テストステップ名 | 指示 | 予想される結果 | コメント |
| --- | --- | --- | --- | --- |
| 1 | ログオンする | SAP Fiori ラウンチパッドにマスタデータスペシャリスト - 製品データとしてログオンします。 | ホームページが表示されます。 |  |
| 2 | SAP Fiori アプリにアクセスする | 製品マスタデータ管理タイルを選択します。 | 製品マスタデータ管理アプリが表示されます。 |  |
| 3 | 製品 P-CLOUD_COMM を検索する | 上部の検索領域で、製品: P-CLOUD_COMM を入力します。実行ボタンを押します。 | 製品がレポート一覧に表示されます。 |  |
| 4 | 製品を開き、流通チェーン: 一般情報を更新する | レポート一覧から製品を選択します。製品番号: P-CLOUD_COMM基本単位: EA製品タイプ: SBPD (サブスクリプション請求製品)OK を選択します。注記 テキストで、特定の地域の言語および製品の詳細を入力します。たとえば、言語: 英語および製品: サブスクリプション請求製品。 | 製品が開き、一般情報が更新されます。 |  |
| 5 | 流通チェーン更新: 一般情報 | 製品ビューの流通チェーン領域で登録を選択し、以下のデータを更新します。販売組織: 1710 (国内販売組織 US)流通チャネル: 10 (直販)注記 MDI を使用している場合は、SBPD 製品タイプに流通チェーンは必要ありません。これは、Cloud Integration を使用している場合にのみ必要です。 | グループ化条件が更新され、製品が保存されます。 | ドイツ国別バージョンの場合は、1 (全課税) ではなく以下の値を更新します。税分類: 6 (全課税 (サービス))その他のエントリは両方の国で同じです。 |
| 6 | 流通チェーン更新: グループ化条件を更新する | グループ化条件領域にナビゲートし、以下のデータを更新します。明細カテゴリグループ: SBPD (サブスクリプション請求製品)勘定設定グループ: X9 (定期サービス)税分類: 1 (全課税)次に、適用してから登録を選択します。注記 明細カテゴリグループは、複製に Master Data Integration ではなく Cloud Integration を使用している場合にのみ必要です。 |  |  |
| 7 | プラントを更新する | プラント領域にナビゲートし、登録を選択して以下のデータを更新します。プラント: 1710 (プラント US)次に、適用、保存の順に選択します。 | プラントデータが更新されます。 |  |

製品: P-CLOUD_SUPPORT

| テストステップ番号 | テストステップ名 | 指示 | 予想される結果 | コメント |
| --- | --- | --- | --- | --- |
| 1 | ログオンする | SAP Fiori ラウンチパッドにマスタデータスペシャリスト - 製品データとしてログオンします。 | ホームページが表示されます。 |  |
| 2 | SAP Fiori アプリにアクセスする | 製品マスタデータ管理タイルを選択します。 | 製品マスタデータ管理アプリが表示されます。 |  |
| 3 | 製品 P-CLOUD_SUPPORT を検索する | 上部の検索領域で、製品: P-CLOUD_SUPPORTを入力します。実行ボタンを押します。 | 製品がレポート一覧に表示されます。 |  |
| 4 | 製品を開き、流通チェーン: 一般情報を更新する | レポート一覧から製品を選択します。製品番号: P-CLOUD_COMM基本単位: EA製品タイプ: SBPD (サブスクリプション請求製品)OK を選択します。注記 テキストで、特定の地域の言語および製品の詳細を入力します。たとえば、言語: 英語および製品: サブスクリプション請求製品。 | 製品が開き、一般情報が更新されます。 |  |
| 5 | 流通チェーン更新: 一般情報 | 製品ビューの流通チェーン領域で登録を選択し、以下のデータを更新します。販売組織: 1710 (国内販売組織 US)流通チャネル: 10 (直販)注記 Master Data Integration を使用している場合、SBPD 製品タイプに流通チェーンは必要ありません。これは、Cloud Integration を使用している場合にのみ必要です。 | グループ化条件が更新され、製品が保存されます。 | ドイツ国別バージョンの場合は、1 (全課税) ではなく以下の値を更新します。税分類: 6 (全課税 (サービス))その他のエントリは両方の国で同じです。 |
| 6 | 流通チェーン更新: グループ化条件を更新する | グループ化条件領域にナビゲートし、以下のデータを更新します。明細カテゴリグループ: SBPD (サブスクリプション請求製品)勘定設定グループ: X9 (定期サービス)税分類: 1 (全課税)次に、適用してから登録を選択します。注記 Master Data Integration を使用している場合、SBPD 製品タイプに流通チェーンは必要ありません。これは Cloud Integration を使用している場合にのみ必要です。 |  |  |
| 7 | プラントを更新する | プラント領域にナビゲートし、登録を選択して以下のデータを更新します。プラント: 1710 (プラント US)次に、適用、保存の順に選択します。 | プラントデータが更新されます。 |  |

#### タイプ SBRE のサブスクリプション製品の拡張

目的

このアクティビティでは、SAP S/4HANA で以下のサブスクリプション製品を拡張します。これらの製品は、SAP Subscription Billing で登録され、SAP S/4HANA に複製されます。

| 製品 ID | 製品タイプ | 説明 |
| --- | --- | --- |
| R-ONETIME | SBRE | ワンタイム有効化手数料 |
| R-SEATS | SBRE | シート基準の月額料金 |
| R-TICKETS | SBRE | チケット基準の使用料 |

手順

製品: R_ONETIME

| テストステップ番号 | テストステップ名 | 指示 | 予想される結果 | コメント |
| --- | --- | --- | --- | --- |
| 1 | ログオンする | SAP Fiori ラウンチパッドにマスタデータスペシャリスト - 製品データとしてログオンします。 | ホームページが表示されます。 |  |
| 2 | SAP Fiori アプリにアクセスする | 製品マスタデータ管理タイルを選択します。 | 製品マスタデータ管理アプリが表示されます。 |  |
| 3 | 製品 R_ONETIME を検索する | 検索領域で、製品: R-ONETIME を入力します。Goをクリックします。 | 製品がレポート一覧に表示されます。 |  |
| 4 | 製品を開き、流通チェーン: 一般情報を更新する | 製品ビューの流通チェーン領域で登録を選択し、以下のデータを更新します。販売組織: 1710 (国内販売組織 US)流通チャネル: 10 (直販)現金割引: はい注記 テキストで、特定の地域の言語および製品の詳細を入力します。たとえば、言語: 英語および製品: サブスクリプション請求製品。 | 製品が開き、一般情報が更新されます。 | ドイツ国別バージョンの場合は、1710 ではなく以下の値を更新します。販売組織: 1010 (国内販売組織 DE)その他のエントリは両方の国で同じです。 |
| 5 | 流通チェーン更新: グループ化条件を更新する | グループ化条件領域にナビゲートし、以下のデータを更新します。勘定設定グループ: X9 (定期サービス)税分類: 1 (全課税)適用を選択します。 | グループ化条件が更新され、製品が保存されます。 | ドイツ国別バージョンの場合は、1 (全課税) ではなく以下の値を更新します。税分類: 6 (全課税 (サービス))その他のエントリは両方の国で同じです。 |
| 6 | プラントを更新する | プラント領域にナビゲートし、登録を選択して以下のデータを更新します。プラント: 1710 (プラント US)次に、適用、登録の順に選択します。 | プラントデータが更新されます。 |  |

製品: R_SEATS

| テストステップ番号 | テストステップ名 | 指示 | 予想される結果 | コメント |
| --- | --- | --- | --- | --- |
| 1 | ログオンする | SAP Fiori ラウンチパッドにマスタデータスペシャリスト - 製品データとしてログオンします。 | ホームページが表示されます。 |  |
| 2 | SAP Fiori アプリにアクセスする | 製品マスタデータ管理タイルを選択します。 | 製品マスタデータ管理アプリが表示されます。 |  |
| 3 | 製品 R_SEATS を検索する | 検索領域で、製品: R-SEATS を入力します。Goをクリックします。 | 製品がレポート一覧に表示されます。 |  |
| 4 | 製品を開き、流通チェーン: 一般情報を更新する | レポート一覧から製品を選択します。製品ビューで、編集をクリックします。流通チェーン領域で登録を選択し、以下のデータを更新します。販売組織: 1710 (国内販売組織 US)流通チャネル: 10 (直販)注記 テキストで、特定の地域の言語および製品の詳細を入力します。たとえば、言語: 英語および製品: サブスクリプション請求製品。 | 製品が開き、一般情報が更新されます。 | ドイツ国別バージョンの場合は、1710 ではなく以下の値を更新します。販売組織: 1010 (国内販売組織 DE)その他のエントリは両方の国で同じです。 |
| 5 | 流通チェーン更新: グループ化条件を更新する | グループ化条件領域にナビゲートし、以下のデータを更新します。明細カテゴリグループ: SBRE (サブスクリプション請求料金要素)勘定設定グループ: X9 (定期サービス)税分類: 1 (全課税)適用を選択します。 | グループ化条件が更新され、製品が保存されます。 | ドイツ国別バージョンの場合は、1 (全課税) ではなく以下の値を更新します。税分類: 6 (全課税 (サービス))その他のエントリは両方の国で同じです。 |
| 6 | プラントを更新する | プラント領域にナビゲートし、登録を選択して以下のデータを更新します。プラント: 1710 (プラント US)次に、適用および保存を選択します。 | プラントデータが更新されます。 |  |

製品: R_TICKETS

| テストステップ番号 | テストステップ名 | 指示 | 予想される結果 | コメント |
| --- | --- | --- | --- | --- |
| 1 | ログオンする | SAP Fiori ラウンチパッドにマスタデータスペシャリスト - 製品データとしてログオンします。 | ホームページが表示されます。 |  |
| 2 | SAP Fiori アプリにアクセスする | 製品マスタデータ管理タイルを選択します。 | 製品マスタデータ管理アプリが表示されます。 |  |
| 3 | 製品 R_TICKETS を検索する | 検索領域で、製品: R-TICKETS を入力します。Goをクリックします。 | 製品がレポート一覧に表示されます。 |  |
| 4 | 製品を開き、流通チェーン: 一般情報を更新する | レポート一覧から製品を選択します。製品ビューで、編集をクリックします。流通チェーン領域で登録を選択し、以下のデータを更新します。販売組織: 1710 (国内販売組織 US)流通チャネル: 10 (直販)注記 テキストで、特定の地域の言語および製品の詳細を入力します。たとえば、言語: 英語および製品: サブスクリプション請求製品。 | 製品が開き、一般情報が更新されます。 | ドイツ国別バージョンの場合は、1710 ではなく以下の値を更新します。販売組織: 1010 (国内販売組織 DE)その他のエントリは両方の国で同じです。 |
| 5 | 流通チェーン更新: グループ化条件を更新する | グループ化条件領域にナビゲートし、以下のデータを更新します。勘定設定グループ: X9 (定期サービス)税分類: 1 (全課税)適用を選択します。 | グループ化条件が更新され、製品が保存されます。 | ドイツ国別バージョンの場合は、1 (全課税) ではなく以下の値を更新します。税分類: 6 (全課税 (サービス))その他のエントリは両方の国で同じです。 |
| 6 | プラントを更新する | プラント領域にナビゲートし、登録を選択して以下のデータを更新します。プラント: 1710 (プラント US)次に、適用および保存を選択します。 | プラントデータが更新されます。 |  |

## 付録

表 5: 表記規則

| 書体 | 説明 |
| --- | --- |
| 例 | 画面から引用される単語または文字列。項目名、画面のタイトル、押ボタンのラベル、メニュー名、メニューパス、メニューオプションが含まれます。他の文書へのテキスト相互参照。 |
| 例 | 強調された単語または式。 |
| Example | システムオブジェクトの技術名称。レポート名、プログラム名、トランザクションコード、テーブル名、本文中にある場合のプログラミング言語のキーコンセプト (SELECT や INCLUDE など) が含まれます。 |
| 例 | 画面上の出力。ファイル名やディレクトリ名とそのパス、メッセージ、変数名およびパラメータ名、ソーステキスト、インストール名、アップグレード名、データベースツール名などが含まれます。 |
| 例 | ユーザが実際に入力する項目。これらの単語や文字列は、ユーザが文書の記載どおりに入力します。 |
| <例> | 可変的なユーザ入力項目。山括弧は、括弧内の単語または文字列を適切なエントリに置き換えてからシステムでエントリを作成することを示します。 |
| 例 | F2 や ENTER などの、キーボードのキー。 |

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
> Flagged while digesting this document, not verified: Usage rate element is R-TICKETS in the rate element/template sections but R-TRAFFIC in price calculation rate plan template and UsagePrice upload; product IDs written R-ONETIME vs R_ONETIME in headings.

> [!warning] Conflict
> Flagged while digesting this document, not verified: Table 3 and 'Table 1' UsagePrice/OneTimePrice upload steps reference lookup table OneTimePrice where UsagePrice is intended.

## Connections
- part-of :: [[_cluster]]
- related-to :: [[09-subscription-billing-and-contract-accounting/master-data-script-create-subscription-product-convergent-invoicing-md]]
- related-to :: [[09-subscription-billing-and-contract-accounting/sap-s-4hana-cloud-public-edition-convergent-invoicing-mds-5lp-453]]
- related-to :: [[09-subscription-billing-and-contract-accounting/script-de-dados-mestre-criar-faturamento-convergente-de-produto-de-ass]]
- related-to :: [[09-subscription-billing-and-contract-accounting/script-de-datos-maestros-creacion-de-facturacion-convergente-de-produc]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/5LP_S4CLD2608_Master_Data_JA_XX.docx` — full document · extracted with `mammoth` · 27,322 chars in the whole document
