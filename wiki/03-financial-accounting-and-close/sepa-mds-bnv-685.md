---
id: 03-financial-accounting-and-close/sepa-mds-bnv-685
title: SEPA 委任の登録 - MDS (BNV) (BNV_S4CLD2608_Master_Data_JA_XX)
description: "Japanese master data script for registering, displaying, listing and managing SEPA mandates in SAP S/4HANA Cloud Public Edition (scope item BNV)."
cluster: 03-financial-accounting-and-close
tags: [kb/financial-accounting-and-close, topic/direct-debit-and-sepa-mandates]
aliases: [BNV_S4CLD2608_Master_Data_JA_XX]
keywords: [Direct Debit and SEPA Mandates, sepa mandates, mandate registration, mandate management, business roles, customer master data, direct debit, BNV]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/BNV_S4CLD2608_Master_Data_JA_XX.docx]
confidence: high
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-685
topic: 03-financial-accounting-and-close/direct-debit-and-sepa-mandates
language: JA
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# SEPA 委任の登録 - MDS (BNV) (BNV_S4CLD2608_Master_Data_JA_XX)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/BNV_S4CLD2608_Master_Data_JA_XX.docx`, extracted with `mammoth`. Grouped under **Direct Debit and SEPA Mandates** in Financial Accounting and Close. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

| <!-- image omitted: unnamed --> | マスタデータスクリプトSAP S/4HANA Cloud Public Edition - 02-07-26 |
| --- | --- |
|  | SEPA 委任の登録 - MDS (BNV) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

目次

[1 目的 2](#_Toc233892011)

[2 前提条件 3](#_Toc233892012)

[2.1 システムアクセス 3](#_Toc233892013)

[2.2 ロール 3](#_Toc233892014)

[2.3 必須の組織ユニット 3](#_Toc233892015)

[2.4 必須マスタデータおよび任意マスタデータ 4](#_Toc233892016)

[2.5 データ登録の主要パラメータ 4](#_Toc233892017)

[3 概要テーブル 5](#_Toc233892018)

[4 テスト手順 6](#_Toc233892019)

[4.1 SEPA 委任の登録 6](#_Toc233892020)

[4.2 SEPA 委任の照会 7](#_Toc233892021)

[4.3 SEPA 委任一覧照会 8](#_Toc233892022)

[4.4 SEPA 委任管理 9](#_Toc233892023)

## 目的

この文書では、SAP S/4HANA Cloud Public Editionシステムで単一ユーロ支払地域 (SEPA) 委任を登録する方法について説明します。説明には、SAP S/4HANA Cloud Public Editionアプライアンスに関連するデータセグメントも含まれます。SAP Best Practicesによって提供されるSAP S/4HANA Cloud Public Editionの範囲に関連しない項目については、この文書では説明していません。

債務者 (商品またはサービスを購入する得意先) は、債権者 (小売業者またはサービスプロバイダ) が SEPA 口座振替で支払を回収することを許可するために、SEPA 委任を入力します。同時に、SEPA 委任には、これらの回収に対して債務者の銀行が支払うことの許可が含まれます。

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
| 債権担当者 | SAP_BR_AR_ACCOUNTANT | 債権管理 | SAP_BR_AR_ACCOUNTANT |  |

### 必須の組織ユニット

得意先マスタデータの一部のセグメントは会社の組織ユニットに依存し、一般 (共通) データは組織ユニットまたは会社コードに依存しません。以下の表は、さまざまなデータセグメントおよび関連する組織ユニットの概要を示しています。

| データセグメント | 依存対象 | 項目例 | コメント | 使用される組織ユニット |
| --- | --- | --- | --- | --- |
| 委任 | ビジネスパートナ | 得意先コード、IBAN および SWIFT/BIC | SEPA 口座振替の欧州の得意先のみに有効です。 | 得意先コード<自社コード |
| 委任 | 会社コード | 会社コード | 会社コードデータは、SEPA 委任が使用される企業構造のすべての会社コード ID に対して存在する可能性があります。 | 会社コード: 自社コード |

### 必須マスタデータおよび任意マスタデータ

以下の表は、利益センタマスタデータレコードで使用される任意および必須のマスタデータオブジェクトの概要を示しています。

| マスタデータオブジェクト | データセグメントでの使用 | 必須/任意 | コメント |
| --- | --- | --- | --- |
| 得意先コード | 第一画面 | 必須 |  |
| 会社コード | 第一画面 | 必須 |  |

### データ登録の主要パラメータ

このセクションでは、マスタレコードの動作に影響し、SEPA 委任の登録に必ず必要となる基本パラメータの一部について説明します。

会社コード:

たとえば、XX10などです。

ビジネスパートナ - 得意先

たとえば、得意先コードXX100003などです。

## 概要テーブル

このスコープアイテムは、以下の表に示されている複数のプロセスステップで構成されます。

|  |
| --- |
| 注記 システム管理者が SAP Fiori ラウンチパッドでスペースおよびページを有効化している場合、ホームページには、ビジネスロールの一般的なタスクを実行するために必要なアプリのみが含まれます。ホームページに含まれていないその他すべての (検索可能な) アプリは、検索バーを使用して見つけることができます ([2434549](https://me.sap.com/notes/2434549))。ホームページをパーソナライズして非表示のアプリを含める場合は、ユーザプロファイルにナビゲートし、アプリファインダを選択します。 |

| プロセスステップ | ビジネスロール | SAP Fiori アプリ/トランザクション | 予想される結果 |
| --- | --- | --- | --- |
| [SEPA 委任の登録](#unique_9) [ ページ] 6 | 債権担当者 | SEPA 委任登録 (FSEPA_M1) | SEPA 委任が登録されます。 |
| [SEPA 委任の照会](#unique_10) [ ページ] 7 | 債権担当者 | SEPA 委任照会(FSEPA_M3) | SEPA 委任が表示されます。 |
| [SEPA 委任一覧照会](#unique_11) [ ページ] 8 | 債権担当者 | SEPA 委任一覧照会 (FSEPA_M4) | SEPA 委任一覧が表示されます。 |
| [SEPA 委任管理](#unique_12) [ ページ] 9 | 債権担当者 | SEPA 委任管理 (F5158) | SEPA 委任が表示されます。 |

## テスト手順

このセクションでは、このスコープアイテムに属する各プロセスステップのテスト手順について説明します。

### SEPA 委任の登録

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
| 1 | ログオンする | SAP Fiori ラウンチパッドに債権担当者としてログオンします。 | SAP Fiori ラウンチパッドが表示されます。 |  |
| 2 | SAP Fiori アプリにアクセスする | SEPA 委任登録 (FSEPA_M1)を開きます。 | アプリが開きます。 |  |
| 3 | アプリケーションを切り替える | 委任登録: 第一画面画面で、アプリケーションスイッチを選択します。アプリケーション選択ダイアログボックスで財務会計を選択し、続行を選択します。 |  |  |
| 4 | 支払人 ID | 得意先項目にXX100003と入力します。 |  |  |
| 5 | 受取人 ID | 支払会社コード項目にXX10と入力し、Enterを押して続行します。注記 ステータスが有効化された委任の画面が表示された場合は、それらの委任がすでに登録されていることを意味します。委任を選択し、続行を選択して委任をチェックおよび変更します。 | 委任登録: 詳細画面が表示されます。 |  |
| 6 | 補足データ | 補足データを選択します。 | 項目にデータが自動入力されます。 |  |
| 7 | 基本データ | 基本データタブで、以下のエントリを入力します。ステータス: 入力済B2B 委任チェックボックス: 選択署名の場所: <場所>署名日付: <日付> |  |  |
| 8 | 支払人 | 支払人タブの支払人の銀行データセクションで、IBAN項目とSWIFT/BIC項目に入力されていることを確認します。注記 このデータは得意先マスタデータの一部であり、すでに登録されていて利用可能である必要があります。 |  |  |
| 9 | 支払先 | 受取人タブで、以下のエントリを入力します。債権者 ID: <債権者 ID>: |  |  |
| 10 | データを保存する | エントリを保存します。 | 委任 0000000000## は登録済ですというメッセージが表示されます。 |  |

### SEPA 委任の照会

テスト管理

カスタマプロジェクト: プロジェクト固有部分への入力

|  |  |  |  |
| --- | --- | --- | --- |
| テストケース ID | <X.XX> | テスト実施日: |  |
| テスト実施者名: |  | 期間: |  |
| ビジネスロール: |  | 責任者: | <都道府県/州、サービスプロバイダ、カスタマ/共同サービスプロバイダ、およびカスタマ> |

前提条件

委任がすでに存在しています。

手順

| テストステップ番号 | テストステップ名 | 指示 | 予想される結果 | コメント |
| --- | --- | --- | --- | --- |
| 1 | ログオンする | SAP Fiori ラウンチパッドに債権担当者としてログオンします。 | SAP Fiori ラウンチパッドが表示されます。 |  |
| 2 | SAP Fiori アプリにアクセスする | SEPA 委任照会(FSEPA_M3)を開きます。 | アプリが開きます。 |  |
| 3 | 支払人 ID | 得意先項目にXX100003と入力します。 |  |  |
| 4 | 受取人 ID | 支払会社コード項目にXX10と入力し、Enterを押して続行します。 | 委任表示: 詳細画面が表示されます。 |  |
| 5 | ナビゲートする | 以下のタブを選択します。基本データ、支払人、および/または受取人 | 情報が表示されます。 |  |
| 6 | 戻る | 終了を選択します。 |  |  |

### SEPA 委任一覧照会

テスト管理

カスタマプロジェクト: プロジェクト固有部分への入力

|  |  |  |  |
| --- | --- | --- | --- |
| テストケース ID | <X.XX> | テスト実施日: |  |
| テスト実施者名: |  | 期間: |  |
| ビジネスロール: |  | 責任者: | <都道府県/州、サービスプロバイダ、カスタマ/共同サービスプロバイダ、およびカスタマ> |

前提条件

委任がすでに存在しています。

手順

| テストステップ番号 | テストステップ名 | 指示 | 予想される結果 | コメント |
| --- | --- | --- | --- | --- |
| 1 | ログオン | SAP Fiori ラウンチパッドに債権担当者としてログオンします。 | SAP Fiori ラウンチパッドが表示されます。 |  |
| 2 | SAP Fiori アプリにアクセスする | SEPA 委任一覧照会 (FSEPA_M4)を開きます。 | アプリが開きます。 |  |
| 3 | 実行を選択する | ダイアログボックスが表示された場合は、アプリケーション選択ダイアログボックスで財務会計を選択し、続行を選択します。ダイアログボックスが表示されない場合は、技術選択タブをチェックし、アプリケーション項目が財務会計に設定されていることを確認します。実行を選択します。 | 委任画面が開いて、既存の委任の一覧が表示されます |  |
| 4 | 委任を選択する | 委任参照番号を選択します。 | 委任変更画面が開いて、選択した委任の詳細が一覧表示されます。 |  |
| 5 | レビューする | 必要に応じて、委任データを変更することができますが、データは変更せずに、委任データをレビューするだけにしてください。 |  |  |
| 6 | 終了する | 続行を 2 回選択するか、または中止を選択して終了します。 |  |  |

### SEPA 委任管理

テスト管理

カスタマプロジェクト: プロジェクト固有部分への入力

|  |  |  |  |
| --- | --- | --- | --- |
| テストケース ID | <X.XX> | テスト実施日: |  |
| テスト実施者名: |  | 期間: |  |
| ビジネスロール: |  | 責任者: | <都道府県/州、サービスプロバイダ、カスタマ/共同サービスプロバイダ、およびカスタマ> |

前提条件

委任がすでに存在しています。

手順

| テストステップ番号 | テストステップ名 | 指示 | 予想される結果 | コメント |
| --- | --- | --- | --- | --- |
| 1 | ログオンする | SAP Fiori ラウンチパッドに債権担当者としてログオンします。 | SAP Fiori ラウンチパッドが表示されます。 |  |
| 2 | SAP Fiori アプリにアクセスする | SEPA 委任管理 (F5158)を開きます。 | アプリが開きます。 |  |
| 3 | 委任を選択する | アプリケーション項目で、財務会計を選択します。 |  |  |
| 4 | 委任を選択する | 支払会社コード項目に、XX10と入力します。Goを選択します。編集対象の行を選択し、編集を選択します。 | 委任変更: 詳細画面が表示されます。 |  |
| 5 | レビューおよび編集する | 以下のタブの利用可能な項目をレビューおよび編集します。基本データ支払人支払先 |  |  |
| 6 | エントリを保存する | 保存を選択してエントリを保存します。 |  |  |

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
- related-to :: [[03-financial-accounting-and-close/crear-mandato-sepa-mds-bnv-684]]
- related-to :: [[03-financial-accounting-and-close/create-sepa-mandate-mds-bnv-683]]
- related-to :: [[03-financial-accounting-and-close/criar-mandato-sepa-mds-bnv-686]]
- related-to :: [[03-financial-accounting-and-close/sepa-mandat-anlegen-sds-bnv-682]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/BNV_S4CLD2608_Master_Data_JA_XX.docx` — full document · extracted with `mammoth` · 9,509 chars in the whole document
