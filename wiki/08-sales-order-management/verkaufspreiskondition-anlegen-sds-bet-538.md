---
id: 08-sales-order-management/verkaufspreiskondition-anlegen-sds-bet-538
title: Verkaufspreiskondition anlegen – SDS (BET) (BET_S4CLD2608_Master_Data_DE_XX)
description: "German sales data script BET: create sales price condition (PPR0) for material TG11 via Materialpreise festlegen – Verkauf (VK12) as Preisfindungssachbearbeiter"
cluster: 08-sales-order-management
tags: [kb/sales-order-management, topic/sales-pricing-conditions]
aliases: [BET_S4CLD2608_Master_Data_DE_XX]
keywords: [Sales Price Conditions and Statistical Conditions, sales price conditions, pricing, condition records, pricing master data, business roles, baseline package sample data, test procedures, BET]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/BET_S4CLD2608_Master_Data_DE_XX.docx]
confidence: high
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-538
topic: 08-sales-order-management/sales-pricing-conditions
language: DE
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Verkaufspreiskondition anlegen – SDS (BET) (BET_S4CLD2608_Master_Data_DE_XX)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/BET_S4CLD2608_Master_Data_DE_XX.docx`, extracted with `mammoth`. Grouped under **Sales Price Conditions and Statistical Conditions** in Sales Order Management. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

| <!-- image omitted: unnamed --> | StammdatenskriptSAP S/4HANA Cloud Public Edition - 02-07-26 |
| --- | --- |
|  | Verkaufspreiskondition anlegen – SDS (BET) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Inhaltsverzeichnis

[1 Verwendungszweck 2](#_Toc233889877)

[2 Voraussetzungen 3](#_Toc233889878)

[2.1 Systemzugriff 3](#_Toc233889879)

[2.2 Rollen 3](#_Toc233889880)

[2.3 Obligatorische und optionale Stammdaten 3](#_Toc233889881)

[3 Übersichtstabelle 5](#_Toc233889882)

[4 Testverfahren 6](#_Toc233889883)

[4.1 Preiskondition anlegen 6](#_Toc233889884)

## Verwendungszweck

Verkaufspreiskonditionen dienen zum Hinterlegen der Informationen, die für die automatische Preisfindung in einem Kundenauftrag erforderlich sind. Dazu gehören Preise, Rabatte, Zuschläge und Steuern. Es kann sich dabei um spezifische Konditionen für einen bestimmten Kunden oder ein bestimmtes Material oder eine bestimmte Kombination von Parametern handeln.

Eine Verkaufspreiskondition enthält Informationen wie den Preis für ein Material in einer bestimmten Währung oder einen kundenspezifischen Rabatt in Prozent. Diese Informationen werden im Kundenauftrag und in Fakturabelegen, z.B. Rechnungen, verwendet und hinterlegt.

Es handelt sich dabei im Allgemeinen um spezifische Informationen für eine bestimmte Verkaufsabteilung innerhalb Ihrer Organisation.

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

| Name (Rollenvorlage) | ID (Rollenvorlage) | Name (Launchpad-Bereich) | ID (Launchpad-Bereich) | Anmeldung |
| --- | --- | --- | --- | --- |
| Preisfindungssachbearbeiter | SAP_BR_PRICING_SPECIALIST | Preisverwaltung | SAP_BR_PRICING_SPECIALIST |  |

### Obligatorische und optionale Stammdaten

Die folgende Tabelle stellt eine Übersicht optionaler und obligatorischer Stammdatenobjekte für die Verwendung beim Anlegen von Preiskonditionen bereit.

Wenn Sie ein SAP Best Practices Baseline Package implementiert haben, können Sie die Baseline-Package-Beispieldaten verwenden oder nach Bedarf eigene Stammdaten ergänzen.

| Stammdatenobjekt | Verwendet im Datensegment | Obligatorisch / optional | Beispielwerte | Kommentare |
| --- | --- | --- | --- | --- |
| Verkaufsorganisation | Einstiegsbild | obligatorisch | <Nummer der Verkaufsorganisation> |  |
| Vertriebsweg | Einstiegsbild | obligatorisch | <Nummer des Vertriebswegs> |  |
| Material | Einstiegsbild | obligatorisch | z.B. TG11 |  |

|  |
| --- |
| Nicht vergessen Beispielwerte für Stammdaten sind länder-/regionsspezifisch. Die Baseline-Package-Beispieldaten stellen lokalisierte Werte für die unterstützten Länder/Regionen bereit. |

## Übersichtstabelle

Dieser Umfangsbestandteil umfasst mehrere Prozessschritte, die in der folgenden Tabelle aufgelistet sind:

|  |
| --- |
| Hinweis Wenn Ihr Systemadministrator Bereiche und Seiten auf dem SAP Fiori Launchpad aktiviert hat, enthält die Startseite nur die wesentlichen Apps, mit denen die typischen Aufgaben einer Benutzerrolle ausgeführt werden können.Alle anderen (suchbaren) Apps, die nicht auf der Startseite enthalten sind, finden Sie über die Suchleiste ([2434549](https://me.sap.com/notes/2434549)).Wenn Sie die Startseite personalisieren und versteckte Apps hinzufügen möchten, wechseln Sie in Ihr Benutzerprofil und wählen Sie App Finder. |

| Prozessschritt | Anwendungsrolle | Transaktion/App | Erwartete Ergebnisse |
| --- | --- | --- | --- |
| [Preiskondition anlegen](#unique_7) [Seite ] 6 | Preisfindungssachbearbeiter | Materialpreise festlegen – Verkauf(VK12) | Die Verkaufspreiskonditionen werden angelegt. |

## Testverfahren

In diesem Abschnitt werden die Testverfahren für den jeweiligen Prozessschritt beschrieben, der zum betreffenden Umfangsbestandteil gehört.

### Preiskondition anlegen

Testverwaltung

Kundenprojekt: Füllen Sie die projektbezogenen Teile aus.

|  |  |  |  |
| --- | --- | --- | --- |
| Testfall-ID | <X.XX> | Testdatum: |  |
| Testername: |  | Dauer: |  |
| Benutzerrolle(n): |  | Zuständigkeit: | <Geben Sie den Serviceanbieter, einen Kunden oder einen Serviceanbieter zusammen mit einem Kunden an.> |

Zweck

Diese Vorgehensweise beschreibt das Anlegen von Verkaufspreiskonditionen.

|  |
| --- |
| Nicht vergessen Die Beispielwerte für Stammdatenwerte sind länder-/regionsspezifisch. Ersetzen Sie die vom SAP S/4HANA Cloud Public Edition-System bereitgestellten länder-/regionsspezifischen Werte, oder verwenden Sie die von Ihnen zu diesem Zweck angelegten Stammdatenwerte. |

Vorgehensweise

| Testschritt | Bezeichnung des Testschritts | Anweisungen | Erwartetes Ergebnis | Kommentare |
| --- | --- | --- | --- | --- |
| 1 | Anmelden | Melden Sie sich am SAP Fiori Launchpad als Preisfindungssachbearbeiter an. | Das SAP Fiori Launchpad wird angezeigt. |  |
| 2 | SAP-Fiori-App aufrufen | Öffnen Sie Materialpreise festlegen – Verkauf(VK12). | Das Bild Mandat anlegen: Einstieg wird angezeigt. |  |
| 3 | Preiskonditionsart | Geben Sie in der Sicht Konditionssätze ändern die folgenden Informationen ein:Konditionsart: z.B. PPR0Drücken Sie ENTER. | Die Sicht Schlüsselkombination wird angezeigt. |  |
| 4 | Schlüsselkombination | Wählen Sie in der Sicht Schlüsselkombination die Option Material mit Freigabestatus, und wählen Sie Auswählen. | Die Sicht Preis ändern (PPR0): Auswahl wird angezeigt. |  |
| 5 | Auswahl | Geben Sie in der Sicht Preis ändern (PPR0): Auswahl die folgenden Informationen ein:Verkaufsorganisation: <Verkaufsorganisation>Vertriebsweg: <Vertriebsweg>Material: z.B. TG11Gültig am: z.B. <Datum>Wählen Sie Ausführen. | Die Sicht Preiskondition ändern (PPR0): Übersicht wird angezeigt. |  |
| 6 | Preiskondition ändern | Geben Sie in der Sicht Preiskondition ändern (PPR0): Übersicht die folgenden Daten ein:Material: z.B. TG11Betrag: z.B. 17,55 USDGültig ab: z.B. <aktuelles Datum>Gültig bis: z.B. <aktuelles Datum + 1 Jahr> | Die Materialpreiskondition wird gepflegt. |  |
| 7 | Sichern | Wählen Sie Sichern. | Die Preiskondition wird gesichert. |  |

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
- related-to :: [[08-sales-order-management/create-sales-pricing-condition-mds-bet-539]]
- related-to :: [[08-sales-order-management/mds-bet-541]]
- related-to :: [[08-sales-order-management/mds-bet-543]]
- related-to :: [[08-sales-order-management/script-de-dados-mestre-criar-condicao-de-determinacao-de-preco-de-vend]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/BET_S4CLD2608_Master_Data_DE_XX.docx` — full document · extracted with `mammoth` · 9,666 chars in the whole document
