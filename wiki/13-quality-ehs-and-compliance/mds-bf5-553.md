---
id: 13-quality-ehs-and-compliance/mds-bf5-553
title: "マスタデータスクリプト: 品質管理情報の登録 - MDS (BF5) (BF5_S4CLD2608_Master_Data_JA_XX)"
description: "Japanese master data script BF5 for creating quality info records (procurement), QM control key assignment (QI05) and PPAP setup in SAP S/4HANA Cloud Public."
cluster: 13-quality-ehs-and-compliance
tags: [kb/quality-ehs-and-compliance, topic/quality-info-records]
aliases: [BF5_S4CLD2608_Master_Data_JA_XX]
keywords: [Quality Info Records in Procurement, quality info records, qm control key, ppap, first article inspection, supplier release, master data scripts, business roles, BF5]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/BF5_S4CLD2608_Master_Data_JA_XX.docx]
confidence: high
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-553
topic: 13-quality-ehs-and-compliance/quality-info-records
language: JA
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# マスタデータスクリプト: 品質管理情報の登録 - MDS (BF5) (BF5_S4CLD2608_Master_Data_JA_XX)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/BF5_S4CLD2608_Master_Data_JA_XX.docx`, extracted with `mammoth`. Grouped under **Quality Info Records in Procurement** in Quality, EHS and Compliance. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

| <!-- image omitted: unnamed --> | マスタデータスクリプトSAP S/4HANA Cloud Public Edition - 02-07-26 |
| --- | --- |
|  | 品質管理情報の登録 - MDS (BF5) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

目次

[1 目的 2](#_Toc233891868)

[2 前提条件 3](#_Toc233891869)

[2.1 システムアクセス 3](#_Toc233891870)

[2.2 ロール 3](#_Toc233891871)

[2.3 必須の組織ユニット 3](#_Toc233891872)

[2.4 必須マスタデータおよび任意マスタデータ 4](#_Toc233891873)

[3 概要テーブル 5](#_Toc233891874)

[4 テスト手順 6](#_Toc233891875)

[4.1 調達での品質管理情報登録 6](#_Toc233891876)

[4.2 品質管理情報なしの品目の品質管理情報の登録(オプション) 7](#_Toc233891877)

[4.3 調達の QM 管理キー割当 8](#_Toc233891878)

[4.4 PPAP の設定登録 9](#_Toc233891879)

## 目的

品目で品質保証契約または仕入先リリースが必要な場合は、品質計画担当者は品質情報レコード (品質管理情報) を登録する必要があります。品質管理情報では、品目の後続処理を可能にする条件を設定します。

購買発注を登録すると、品目と仕入先の組み合わせで品質管理情報が必要かどうかと利用可能かどうかがチェックされます。

また、見積や購買発注、入庫でその仕入先、および品目と仕入先の組み合わせがブロックされているかリリースされているかもチェックされます。このチェックの実行は、品目マスタの調達管理キーの QM 設定によって決まります。

さらに、QM システムを割り当てて、可能な品質検査を適宜トリガすることができます。また、入庫検査と納入前検査 (あるいはそのいずれか) のトリガを決定することもできます。品質管理情報で第一モデル品質検査 (FAI) を計画できる製造部品承認処理 (PPAP) が必要であることを示すこともできます。ここで、(行った使用決定に基づいて) PPAP ステータスおよび評価コードを更新することで、PPAP を管理することができます。また、PPAP で第一モデル品質検査 (FAI) を実行するために、複数の購買発注/明細を同時に割り当てることもできます。

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
| 品質計画担当者 | SAP_BR_QUALITY_PLANNER | 品質計画 | SAP_BR_QUALITY_PLANNER |  |

ビジネスロールの詳細については、SAP S/4HANA Cloud Public Editionの導入管理ガイドのユーザへのビジネスロールの割当を参照してください。

### 必須の組織ユニット

得意先マスタデータの一部のセグメントは会社の組織ユニットに依存し、一般 (セントラル) データは組織ユニットまたは会社コードに依存しません。以下の表は、さまざまなデータセグメントおよび関連する組織ユニットの概要を示しています。

| データセグメント | 依存対象 | 項目例 | コメント | 使用される組織ユニット |
| --- | --- | --- | --- | --- |
| 品質管理情報 | プラント |  | プラントデータは、品目マスタレコードが使用される企業構造のすべてのプラント ID に対して存在可能です。 | プラント: |

### 必須マスタデータおよび任意マスタデータ

品質管理データレコードは、他のマスタデータを参照する場合があります。以下の表は、品質管理情報で使用される任意および必須のマスタデータオブジェクトの概要を示しています。

| マスタデータオブジェクト | データセグメントでの使用 | 必須/任意 | コメント |
| --- | --- | --- | --- |
| 品目マスタ |  | 必須 | 品質管理ビューで使用します。詳細については、マスタデータスクリプト 品目/製品マスタの品質管理属性の登録 - MDS (BNY) を参照してください。 |
| 仕入先マスタ |  | 必須 |  |

|  |
| --- |
| 注記 品質管理情報は、QM 調達キーに仕入先リリースが必要な場合に必要です。この場合、仕入先/品目の組合せごとに、品質管理情報を登録する必要があります。 |

## 概要テーブル

このスコープアイテムは、以下の表に示されている複数のプロセスステップで構成されます。

|  |
| --- |
| 注記 システム管理者が SAP Fiori ラウンチパッドでスペースおよびページを有効化している場合、ホームページには、ビジネスロールの一般的なタスクを実行するために必要なアプリのみが含まれます。ホームページに含まれていないその他すべての (検索可能な) アプリは、検索バーを使用して見つけることができます ([2434549](https://me.sap.com/notes/2434549))。ホームページをパーソナライズして非表示のアプリを含める場合は、ユーザプロファイルにナビゲートし、アプリファインダを選択します。 |

| プロセスステップ | ビジネスロール | アプリ/トランザクション | 予想される結果 |
| --- | --- | --- | --- |
| [調達での品質管理情報登録](#unique_8) [ ページ] 6 | 品質計画担当者 | 品質管理情報の登録 - 調達 (QI01) | 品質管理情報が登録されます。 |
| [品質管理情報なしの品目の品質管理情報の登録(オプション)](#unique_9) [ ページ] 7 | 品質計画担当者 | 品質管理情報管理(F2256A) | 品質管理情報が登録されます。 |
| [調達の QM 管理キー割当](#unique_10) [ ページ] 8 | 品質計画担当者 | 調達の QM 管理キー割当 - マニュアル処理(QI05) | 品質管理情報が登録されます。 |
| [PPAP の設定登録](#unique_11) [ ページ] 9 | 品質計画担当者 | 品質管理情報管理(F2256A) | 品質管理情報が登録されます。 |

## テスト手順

このセクションでは、このスコープアイテムに属する各プロセスステップのテスト手順について説明します。

### 調達での品質管理情報登録

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
| 1 | ログオンする | SAP Fiori ラウンチパッドに品質計画担当者としてログオンします。 | SAP Fiori ラウンチパッドが表示されます。 |  |
| 2 | SAP Fiori アプリにアクセスする | 品質管理情報の登録 - 調達 (QI01) を開きます。 | 品質管理情報の登録ビューが表示されます。 |  |
| 3 | 一般データを入力する | 以下のエントリを入力します。品目: <品目コード>サプライヤ: <サプライヤコード>プラント: <プラントコード>続行を選択します。 |  |  |
| 4 | リリースデータを入力する | リリースセクションで、以下のデータを入力します。リリース期限: 未来の日付。1 年以内などオプション:リリース数量有効: フラグ設定リリース数量: 15 など |  |  |
| 5 | データを保存する | 保存を選択します。 | データが保存されます。 |  |

|  |
| --- |
| 注記 品質管理情報では、入庫品質検査を無効化するか、入庫品質検査または納入前検査 (もしくはその両方) を実行するかを決定することもできます。このためには、品質検査管理タブを選択し、以下のデータを入力します。入庫品質検査に加えて納入前検査を実行する場合は、納入前検査の品質検査タイプとリードタイム (日数) を入力します。品目マスタの設定でこのような品質検査が指定されていても、入庫品質検査を実行しない場合は、品質検査なし区分を設定します。入庫品質検査ではなく納入前検査を実行する場合は、関連する区分を設定します。この区分を設定すると、納入前検査が実行される場合は、入庫に対して品質検査ロットは登録されません。納入前検査が実行されない場合は、入庫に対して品質検査ロットが生成されます。品質検査管理タブでは、以下を入力することもできます。サプライヤの QM システムサプライヤに QM システムがある場合は、この特定の品目に対してここに QM システムのテキストを保存することができます。部品製造の承認部品製造の承認プロセスが必須であるように指定することができます。この追加設定は、品質管理情報管理(F2256A)アプリで行う必要があります (章[調達の QM 管理キー割当](#unique_10) [ ページ] 8を参照)。 |

### 品質管理情報なしの品目の品質管理情報の登録(オプション)

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
| 1 | ログオンする | SAP Fiori ラウンチパッドに 品質計画担当者 としてログオンします。 | SAP Fiori ラウンチパッドが表示されます。 |  |
| 2 | SAP Fiori アプリにアクセスする | 品質管理情報管理(F2256A) を開きます。 |  |  |
| 3 | 品質管理情報を登録する (オプション) | 結果テーブルの右上隅にある登録を選択し、以下のデータをヘッダレベルで更新します。品目: 品目コードサプライヤ: サプライヤコードプラント: プラントコードリリースセクションについては、前の章のステップ 4 を参照してください。 |  |  |
| 4 | データを保存する | 登録を選択します。 | データが保存され、新しい品質管理情報が登録されました。 |  |

### 調達の QM 管理キー割当

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
| 1 | ログオンする | SAP Fiori ラウンチパッドに品質計画担当者としてログオンします。 | SAP Fiori ラウンチパッドが表示されます。 |  |
| 2 | SAP Fiori アプリにアクセスする | 調達の QM 管理キー割当 - マニュアル処理(QI05)を開きます。 |  |  |
| 3 | QM 管理キーを割り当てる | この選択は、プラントレベルまたは品目レベル (もしくはその両方) で実行することができます。割り当てる QM 管理キーを選択します。品目: 品目コードプラント: プラントコードQM 管理キー: QM 管理キーデータベース変更の導入: 有効 (この区分が設定されていない場合は、テスト実行のみが実行されます)注記 品目マスタデータで調達における QM 有効区分が設定されている品目のみが選択されます。 |  |  |

### PPAP の設定登録

テスト管理

カスタマプロジェクト: プロジェクト固有部分への入力

|  |  |  |  |
| --- | --- | --- | --- |
| テストケース ID | <X.XX> | テスト実施日: |  |
| テスト実施者名: |  | 期間: |  |
| ビジネスロール: |  | 責任者: | <都道府県/州、サービスプロバイダ、カスタマ/共同サービスプロバイダ、およびカスタマ> |

前提条件

第一モデル品質検査は、専用の品質検査計画使用 GR 品質検査モデルを使用して行います。これは、調達において以下の QM の管理キーに割り当てられます。

- 0001 サプライヤリリース
- 9001 サプライヤリリース (エラーメッセージあり)

第一モデル品質検査を実行するには、以下の条件を満たす必要があります。

- 第一モデル品質検査に対して使用 GR 品質検査モデル (51) を使用する品質検査計画が存在しています。
- 上記の QM管理キーの 1 つが品目に割り当てられています。
- この品目には、部品製造の承認の以下の設定で品質管理情報が存在しています。
    - 製造部品の承認が有効化され、PPAP レベルと PPAP ステータスが設定されています。
    - 少なくとも 1 つの購買発注および購買発注明細が入力されています。

購買発注明細の入庫時に、第一モデル品質検査に対して品質検査ロットが登録されます。この品質検査ロットでは、QM 管理キーの FAI 計画使用が取得され、品質検査タイプに対してこの使用が更新されます。

手順

品質管理情報管理(F2256A)アプリで PPAP を有効化します。そこで、品目に対して、1 つまたは複数の購買発注明細の入庫時に第一モデル品質検査が行われるように指定することができます。

手順

| テストステップ番号 | テストステップ名 | 指示 | 予想される結果 | コメント |
| --- | --- | --- | --- | --- |
| 1 | ログオンする | SAP Fiori ラウンチパッドに品質計画担当者としてログオンします。 | SAP Fiori ラウンチパッドが表示されます。 |  |
| 2 | SAP Fiori アプリにアクセスする | 品質管理情報管理(F2256A)を開きます。 |  |  |
| 3 | 品質管理情報を登録する | 結果テーブルの右上隅にある登録を選択し、以下のデータをヘッダレベルで更新します。品目: 品目コードサプライヤ: サプライヤコードプラント: プラントコードリリースセクションについては、前の章のステップ 4 を参照してください。または、PPAP を有効化する既存の品質管理情報を選択します。 |  |  |
| 4 | 部品製造の承認データを入力する | 部品製造の承認セクションに移動します。有効化を選択します。PPAP レベル項目で対応する PPAP レベルを割り当てます。 |  |  |
| 5 | データを保存する | 登録を選択します。 | データが保存され、新しい品質管理情報が登録されました。 |  |

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
- related-to :: [[13-quality-ehs-and-compliance/crear-registro-info-de-calidad-mds-bf5-552]]
- related-to :: [[13-quality-ehs-and-compliance/create-quality-info-record-mds-bf5-551]]
- related-to :: [[13-quality-ehs-and-compliance/criar-registro-info-de-qualidade-mds-bf5-554]]
- related-to :: [[13-quality-ehs-and-compliance/mds-bf5-555]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/BF5_S4CLD2608_Master_Data_JA_XX.docx` — full document · extracted with `mammoth` · 10,277 chars in the whole document
