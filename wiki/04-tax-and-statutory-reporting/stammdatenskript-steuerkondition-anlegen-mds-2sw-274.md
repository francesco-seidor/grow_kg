---
id: 04-tax-and-statutory-reporting/stammdatenskript-steuerkondition-anlegen-mds-2sw-274
title: Stammdatenskript - Steuerkondition anlegen – MDS (2SW) (2SW_S4CLD2608_Master_Data_DE_XX)
description: "German master data script (2SW) for SAP S/4HANA Cloud Public Edition: creating tax condition records (MEK2) and creating/changing purchasing price conditions (MEK1/MEK2)."
cluster: 04-tax-and-statutory-reporting
tags: [kb/tax-and-statutory-reporting, topic/purchasing-tax-condition-records]
aliases: [2SW_S4CLD2608_Master_Data_DE_XX]
keywords: [Tax Condition Records and Purchasing Price Conditions, tax conditions, purchasing price conditions, condition records, master data scripts, tax codes, business roles, price condition changes, 2SW]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/2SW_S4CLD2608_Master_Data_DE_XX.docx]
confidence: high
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-274
topic: 04-tax-and-statutory-reporting/purchasing-tax-condition-records
language: DE
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Stammdatenskript - Steuerkondition anlegen – MDS (2SW) (2SW_S4CLD2608_Master_Data_DE_XX)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/2SW_S4CLD2608_Master_Data_DE_XX.docx`, extracted with `mammoth`. Grouped under **Tax Condition Records and Purchasing Price Conditions** in Tax and Statutory Reporting. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

| <!-- image omitted: unnamed --> | StammdatenskriptSAP S/4HANA Cloud Public Edition - 02-07-26 |
| --- | --- |
|  | Steuerkondition anlegen – MDS (2SW) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Inhaltsverzeichnis

[1 Zweck 2](#_Toc233889580)

[2 Voraussetzungen 3](#_Toc233889581)

[2.1 Systemzugriff 3](#_Toc233889582)

[2.2 Rollen 3](#_Toc233889583)

[2.3 Obligatorische und optionale Stammdaten 3](#_Toc233889584)

[3 Übersichtstabelle 5](#_Toc233889585)

[4 Testverfahren 6](#_Toc233889586)

[4.1 Steuerkonditionssätze anlegen 6](#_Toc233889587)

[4.2 Preiskonditionen anlegen 7](#_Toc233889588)

[4.3 Preiskonditionen ändern 9](#_Toc233889589)

## Zweck

Ein Steuerkonditionssatz enthält spezifische Informationen zu einem Land/einer Region und diverse Steuerkennzeichen für verschiedene Kombinationen von Steuerindikatoren für Material, Werk und Import.

## Voraussetzungen

In diesem Abschnitt sind alle Voraussetzungen für den Test hinsichtlich System, Benutzer, Stammdaten, Organisationsdaten, sonstige Testdaten und Voraussetzungen zusammengefasst.

### Systemzugriff

| System | Details |
| --- | --- |
| System | Zugriff möglich über SAP Fiori Launchpad. Ihr Systemadministrator stellt Ihnen die URL für den Zugriff auf die verschiedenen Apps zur Verfügung, die Ihrer Rolle zugeordnet sind. |

### Rollen

Legen Sie Benutzerrollen mit den folgenden von SAP ausgelieferten Benutzerrollenvorlagen an, und ordnen Sie sie Ihren einzelnen Testbenutzern zu.

Alternativ können Sie, falls verfügbar, die folgenden von SAP ausgelieferten Bereiche verwenden. Legen Sie einen Bereich mit Seiten an, die vordefinierte grundlegende Apps enthalten, und ordnen Sie sie der Benutzerrolle zu. Anschließend ordnen Sie diese Benutzerrolle Ihren einzelnen Benutzern zu.

Weitere Informationen finden Sie unter Anwendungsrolle aus einer Vorlage anlegen in der [Product Assistance](https://help.sap.com/docs/SAP_S4HANA_CLOUD/53e36b5493804bcdb3f6f14de8b487dd/ec310a8b669a45ca898dc4dd91d97de2.html) für SAP S/4HANA Cloud Public Edition.

| Name (Rollenvorlage) | ID (Rollenvorlage) | Name (Launchpad-Bereich) | ID (Launchpad-Bereich) | Anmelden |
| --- | --- | --- | --- | --- |
| Steuerspezialist | SAP_BR_TAX_SPECIALIST | Steuerprozentsätze | SAP_BR_TAX_SPECIALIST |  |
| Einkäufer | SAP_BR_PURCHASER | Einkauf / Ausschreibungen und Kontrakte | SAP_MM_SPT_PURCHASING_PC / SAP_MM_SPT_SOURCING_PC |  |

### Obligatorische und optionale Stammdaten

Materialstammdatensätze können auf andere Stammdaten verweisen. Die folgende Tabelle bietet eine Übersicht über die optionalen und obligatorischen Stammdatenobjekte, die in einem Materialstammdatensatz verwendet werden müssen.

In diesem Abschnitt werden einige grundlegende Parameter erläutert, die das Verhalten eines Stammsatzes beeinflussen und zum Anlegen einer Preiskondition immer erforderlich sind:

Empfangsland: z.B. DE

| Stammdatenobjekt | Verwendet im Datensegment | Obligatorisch / optional | Kommentare |
| --- | --- | --- | --- |
| Empfangsland | Einstiegsbild | obligatorisch |  |

## Übersichtstabelle

Dieser Umfangsbestandteil umfasst die verschiedenen Schritte in der folgenden Tabelle:

|  |
| --- |
| Hinweis Wenn Ihr Systemadministrator Bereiche und Seiten auf dem SAP Fiori Launchpad aktiviert hat, enthält die Startseite nur die wesentlichen Apps, mit denen die typischen Aufgaben einer Benutzerrolle ausgeführt werden können.Alle anderen (suchbaren) Apps, die nicht auf der Startseite enthalten sind, finden Sie über die Suchleiste ([2434549](https://me.sap.com/notes/2434549)).Wenn Sie die Startseite personalisieren und versteckte Apps hinzufügen möchten, wechseln Sie in Ihr Benutzerprofil und wählen Sie App Finder. |

| Prozessschritt | Anwendungsrolle | SAP-Fiori-App / Transaktion | Erwartete Ergebnisse |
| --- | --- | --- | --- |
| [Steuerkonditionssätze anlegen](#unique_7) [Seite ] 6 | Steuerspezialist | Steuersätze festlegen - Einkauf(MEK2) | Die Steuerkondition ist eingerichtet. |
| [Preiskonditionen anlegen](#unique_8) [Seite ] 7 | Einkäufer | Preiskonditionen anlegen Einkauf(MEK1) | Die Preiskonditionen werden angelegt. |
| [Preiskonditionen ändern](#unique_9) [Seite ] 9 | Einkäufer | Preiskonditionen ändern - Einkauf(MEK2) | Die Preiskonditionen werden geändert. |

## Testverfahren

In diesem Abschnitt werden die Testverfahren für den jeweiligen Prozessschritt beschrieben, der zum betreffenden Umfangsbestandteil gehört.

### Steuerkonditionssätze anlegen

Testverwaltung

Kundenprojekt: Füllen Sie die projektbezogenen Teile aus.

|  |  |  |  |
| --- | --- | --- | --- |
| Testfall-ID | <X.XX> | Testdatum: |  |
| Testername: |  | Dauer: |  |
| Benutzerrolle(n): |  | Zuständigkeit: | <Geben Sie den Serviceanbieter, einen Kunden oder einen Serviceanbieter zusammen mit einem Kunden an.> |

Vorgehensweise

| Testschritt | Bezeichnung des Testschritts | Anweisung | Erwartetes Ergebnis | Kommentare |
| --- | --- | --- | --- | --- |
| 1 | Anmelden | Melden Sie sich am SAP Fiori Launchpad als Steuerspezialist an. | Das SAP Fiori Launchpad wird angezeigt. |  |
| 2 | SAP-Fiori-App aufrufen | Öffnen Sie Steuersätze festlegen - Einkauf(MEK2). | Die App wird geöffnet. |  |
| 3 | Preiskonditionsart | Geben Sie auf dem Bild Konditionssatz ändern die folgenden Daten ein, und wählen Sie Enter:Konditionsart: z.B. TTX1 | Das Bild Schlüsselkombination wird angezeigt. |  |
| 4 | Schlüsselkombination | Wählen Sie auf dem Bild Schlüsselkombination die Registerkarte Steuern: Material, Werk und Herkunft, und wählen Sie Auswählen. | Das Bild Nicht abzugsf. S (TTX1) ändern: Auswahl wird angezeigt. |  |
| 5 | Empfangsland | Geben Sie im Bild Nicht abzugsf. S (TTX1) ändern: Auswahl folgende Einträge vor, und wählen Sie Ausführen:Empfangsland: <Länder-/Regionscode> | Das Bild Nicht abzugsf. St. (TTX1) ändern: Übersicht wird angezeigt. |  |
| 6 | Steuerkondition ändern | Geben Sie auf dem Bild Nicht abzugsf. St. (TTX1) ändern: Übersicht folgende Daten ein:Steuerind. Material: <Steuerindikator für Material>StIndWerk: <Steuerindikator: Werk>Importieren: <Importieren>Gültig ab: <gültig ab>Gültig bis: <gültig bis>Steuerkennzeichen: <Steuerkennzeichen> | Der Steuerkonditionssatz wird gepflegt. |  |
| 7 | Sichern | Wählen Sie Sichern. | Der Steuerkonditionssatz wird gesichert. |  |
| 8 | "Zurück" wählen | Wählen Sie zweimal Zurück. |  |  |
| 9 | Preiskonditionsart | Geben Sie auf dem Bild Konditionssatz ändern die folgenden Daten ein, und wählen Sie Enter:Konditionsart: z.B. TTX1 | Das Dialogfenster Schlüsselkombination wird angezeigt. |  |
| 10 | Schlüsselkombination | Wählen Sie im Dialogfenster Schlüsselkombination das Ankreuzfeld Steuer: Werk, Kontierung, Herkunft und Region, und wählen Sie Auswählen. | Das Bild Nicht abzugsf. S (TTX1) ändern: Auswahl wird angezeigt. |  |
| 11 | Empfangsland | Geben Sie im Bild Nicht abzugsf. S (TTX1) ändern: Auswahl folgende Einträge vor, und wählen Sie Ausführen:Empfangsland: <Länder-/Regionscode> | Das Bild Nicht abzugsf. St. (TTX1) ändern: Übersicht wird angezeigt. |  |
| 12 | Steuerkondition ändern | Geben Sie auf dem Bild Nicht abzugsf. St. (TTX1) ändern: Übersicht folgende Daten ein:StIndWerk: <Steuerindikator: Werk>Steuerind. Kont.: <Steuerindikatorkontierung>Importieren: <Importieren>Steuerind. Region: <Region>Gültig ab: <gültig ab>Gültig bis: <gültig bis>Steuerkennzeichen: <Steuerkennzeichen> | Der Steuerkonditionssatz wird gepflegt. |  |
| 13 | Sichern | Wählen Sie Sichern. | Der Steuerkonditionssatz wird gesichert. |  |

### Preiskonditionen anlegen

Testverwaltung

Kundenprojekt: Füllen Sie die projektbezogenen Teile aus.

|  |  |  |  |
| --- | --- | --- | --- |
| Testfall-ID | <X.XX> | Testdatum: |  |
| Testername: |  | Dauer: |  |
| Benutzerrolle(n): |  | Zuständigkeit: | <Geben Sie den Serviceanbieter, einen Kunden oder einen Serviceanbieter zusammen mit einem Kunden an.> |

Vorgehensweise

| Testschritt | Bezeichnung des Testschritts | Anweisung | Erwartetes Ergebnis | Kommentare |
| --- | --- | --- | --- | --- |
| 1 | Anmelden | Melden Sie sich am SAP Fiori Launchpad als Einkäufer an. | Das SAP Fiori Launchpad wird angezeigt. |  |
| 2 | SAP-Fiori-App aufrufen | Öffnen Sie Preiskonditionen anlegen Einkauf(MEK1). | Die App wird geöffnet. |  |
| 3 | Preiskonditionsart | Nehmen Sie folgende Einträge vor, und drücken Sie Enter:Konditionsart: z.B. PPR0. | Das Dialogfenster Schlüsselkombination wird angezeigt. |  |
| 4 | Schlüsselkombination | Wählen Sie in der Schlüsselkombination das Ankreuzfeld Materialinfosatz (werksspezifisch), und wählen Sie Auswählen. | Das Bild Standard-Bruttopreiskondition (PPR0) anlegen: Schnellerfassung wird angezeigt. |  |
| 5 | Standard-Bruttokondition anlegen | Nehmen Sie im Bild Standard-Bruttopreiskondition (PPR0) anlegen: Schnellerfassung die folgenden Eingaben vor:Lieferant: <Lieferant>Material: <Material>Einkaufsorganisation: <Einkaufsorganisation>Werk: <Werk>Infotyp: z.B. 0 StandardBetrag: <Betrag>Einheit: <Preiseinheit>Pro: <pro Menge>ME: <Einheit>Gültig ab: <gültig ab>Gültig bis: <gültig bis> | Der Standard-Bruttokonditionssatz wird gepflegt. |  |
| 6 | Sichern | Wählen Sie Sichern. | Der Konditionssatz wird gesichert. |  |

### Preiskonditionen ändern

Testverwaltung

Kundenprojekt: Füllen Sie die projektbezogenen Teile aus.

|  |  |  |  |
| --- | --- | --- | --- |
| Testfall-ID | <X.XX> | Testdatum: |  |
| Testername: |  | Dauer: |  |
| Benutzerrolle(n): |  | Zuständigkeit: | <Geben Sie den Serviceanbieter, einen Kunden oder einen Serviceanbieter zusammen mit einem Kunden an.> |

Vorgehensweise

| Testschritt | Bezeichnung des Testschritts | Anweisungen | Erwartetes Ergebnis | Kommentare |
| --- | --- | --- | --- | --- |
| 1 | Anmelden | Melden Sie sich am SAP Fiori Launchpad als Einkäufer an. | Das SAP Fiori Launchpad wird angezeigt. |  |
| 2 | SAP-Fiori-App aufrufen | Öffnen Sie Preiskonditionen ändern - Einkauf(MEK2). | Die App wird geöffnet. |  |
| 3 | Preiskonditionsart | Nehmen Sie folgenden Eintrag vor, und drücken Sie ENTER:Konditionsart: z.B. PPR0 | Das Bild Schlüsselkombination wird angezeigt. |  |
| 4 | Schlüsselkombination | Wählen Sie in der Schlüsselkombination das Ankreuzfeld Materialinfosatz (werksspezifisch), und wählen Sie Auswählen. | Das Bild Standard-Bruttopreiskondition (PPR0) anlegen: Schnellerfassung wird angezeigt. |  |
| 5 | Standard-Bruttokondition ändern | Nehmen Sie auf dem Bild Standard-Bruttopreiskondition (PPR0) ändern: Schnellerfassung die folgenden Daten ein:Lieferant: <Lieferant>Material: <Material>Einkaufsorganisation: <Einkaufsorganisation>Werk: <Werk>:Infotyp: z.B. 0 StandardWählen Sie Ausführen.Geben Sie Folgendes ein:Betrag: <Betrag> | Der Standard-Bruttokonditionssatz wird geändert. |  |
| 6 | Sichern | Wählen Sie Sichern. | Der Konditionssatz wird gesichert. |  |

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
- related-to :: [[04-tax-and-statutory-reporting/crear-condicion-para-determinacion-de-impuestos-mds-2sw-276]]
- related-to :: [[04-tax-and-statutory-reporting/master-data-script-create-tax-condition-2sw-275]]
- related-to :: [[04-tax-and-statutory-reporting/mds-2sw-277]]
- related-to :: [[04-tax-and-statutory-reporting/mds-2sw-279]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/2SW_S4CLD2608_Master_Data_DE_XX.docx` — full document · extracted with `mammoth` · 13,376 chars in the whole document
