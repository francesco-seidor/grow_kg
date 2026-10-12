---
id: 12-production-and-manufacturing/stammdatenskript-produktionsversorgungsbereich-anlegen-sds-40d-400
title: "Stammdatenskript: Produktionsversorgungsbereich anlegen – SDS (40D) (40D_S4CLD2608_Master_Data_DE_XX)"
description: German master data script (40D) for creating a production supply area (PVB) in SAP S/4HANA Cloud Public Edition via Fiori apps PK05S or F6935.
cluster: 12-production-and-manufacturing
tags: [kb/production-and-manufacturing, topic/production-supply-areas]
aliases: [40D_S4CLD2608_Master_Data_DE_XX]
keywords: [Production Supply Areas, production supply area, master data script, test procedure, lean manufacturing, user roles, organizational units, fiori launchpad, 40D]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/40D_S4CLD2608_Master_Data_DE_XX.docx]
confidence: high
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-400
topic: 12-production-and-manufacturing/production-supply-areas
language: DE
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Stammdatenskript: Produktionsversorgungsbereich anlegen – SDS (40D) (40D_S4CLD2608_Master_Data_DE_XX)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/40D_S4CLD2608_Master_Data_DE_XX.docx`, extracted with `mammoth`. Grouped under **Production Supply Areas** in Production and Manufacturing. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

| <!-- image omitted: unnamed --> | StammdatenskriptSAP S/4HANA Cloud Public Edition - 02-07-26 |
| --- | --- |
|  | Produktionsversorgungsbereich anlegen – SDS (40D) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Inhaltsverzeichnis

[1 Zweck 2](#_Toc233889744)

[2 Voraussetzungen 3](#_Toc233889745)

[2.1 Systemzugriff 3](#_Toc233889746)

[2.2 Rollen 3](#_Toc233889747)

[2.3 Erforderliche Organisationseinheiten 3](#_Toc233889748)

[2.4 Obligatorische und optionale Parameter für die Datenerstellung 4](#_Toc233889749)

[3 Übersichtstabelle 5](#_Toc233889750)

[4 Testverfahren 6](#_Toc233889751)

[4.1 Produktionsversorgungsbereich anlegen 6](#_Toc233889752)

## Zweck

Dieses Dokument beschreibt, wie Sie einen Produktionsversorgungsbereich für Ihr SAP S/4HANA Cloud Public Edition-System anlegen. Die Beschreibung umfasst die Datensegmente, die für die SAP S/4HANA Cloud Public Edition-Appliance relevant sind. Felder, die für den Umfang der SAP S/4HANA Cloud Public Edition-Inhalte nicht relevant sind, werden in diesem Dokument nicht behandelt.

Ein gemäß dieser Beschreibung angelegter Produktionsversorgungsbereich kann für Fertigungsprozesse verwendet werden.

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
| Produktionsplaner – Lean Manufacturing | SAP_BR_PRODN_PLNR_LEAN_MFG | Produktionsplanung - Lean Manufacturing | SAP_BR_PRODN_PLNR_LEAN_MFG |  |

### Erforderliche Organisationseinheiten

| Datensegment | Hängt ab von | Feldbeispiele | Kommentare | Zu verwendende Organisationseinheit |
| --- | --- | --- | --- | --- |
| Alle Daten | Werk |  | Alle Daten für den Produktionsversorgungsbereich hängen vom Werk ab. | Werk:__________ |
| Alle Daten | Lagerort |  | Alle Daten für den Produktionsversorgungsbereich hängen vom Lagerort ab. | Lagerort:__________ |

### Obligatorische und optionale Parameter für die Datenerstellung

Datensätze des Produktionsversorgungsbereichs können auf anderen Eingabeparameter verweisen. Die folgende Tabelle bietet eine Übersicht über die optionalen und obligatorischen Eingabeparameter zum Anlegen eines Produktionsversorgungsbereichs.

| Datenobjekt | Obligatorisch / optional | Kommentare |
| --- | --- | --- |
| Verantwortlicher / Disponent | optional | Verantwortlicher für einen oder mehrere PVBs |

## Übersichtstabelle

Dieser Umfangsbestandteil umfasst den Prozessschritt in der folgenden Tabelle:

|  |
| --- |
| Hinweis Wenn Ihr Systemadministrator Bereiche und Seiten auf dem SAP Fiori Launchpad aktiviert hat, enthält die Startseite nur die wesentlichen Apps, mit denen die typischen Aufgaben einer Benutzerrolle ausgeführt werden können.Alle anderen (suchbaren) Apps, die nicht auf der Startseite enthalten sind, finden Sie über die Suchleiste ([2434549](https://me.sap.com/notes/2434549)).Wenn Sie die Startseite personalisieren und versteckte Apps hinzufügen möchten, wechseln Sie in Ihr Benutzerprofil und wählen Sie App Finder. |

| Prozessschritt | Anwendungsrolle | Bewegung | Erwartete Ergebnisse |
| --- | --- | --- | --- |
| [Produktionsversorgungsbereich anlegen](#unique_8) [Seite ] 6 | Produktionsplaner – Lean Manufacturing | Produktionsversorgungsbereich - Schnellerfassung(PK05S) oder Produktionsversorgungsbereiche verwalten(F6935) | Der Produktionsversorgungsbereich wird erstellt. |

## Testverfahren

In diesem Abschnitt werden die Testverfahren für den jeweiligen Prozessschritt beschrieben, der zum betreffenden Umfangsbestandteil gehört.

### Produktionsversorgungsbereich anlegen

Testverwaltung

Kundenprojekt: Füllen Sie die projektbezogenen Teile aus.

|  |  |  |  |
| --- | --- | --- | --- |
| Testfall-ID | <X.XX> | Testdatum: |  |
| Testername: |  | Dauer: |  |
| Benutzerrolle(n): |  | Zuständigkeit: | <Geben Sie den Serviceanbieter, einen Kunden oder einen Serviceanbieter zusammen mit einem Kunden an.> |

Vorgehensweise

Option 1:

| Testschrittnummer | Bezeichnung des Testschritts | Anweisungen | Erwartetes Ergebnis | Bestanden/Nicht bestanden/Anmerkung |
| --- | --- | --- | --- | --- |
| 1 | Anmelden | Melden Sie sich am SAP Fiori Launchpad als Produktionsplaner – Lean Manufacturing an. | Das SAP Fiori Launchpad wird angezeigt. |  |
| 2 | SAP-Fiori-App aufrufen | Öffnen Sie Produktionsversorgungsbereich - Schnellerfassung(PK05S). | Das Bild Tabellensichten bearbeiten: Einstiegsbild wird angezeigt. |  |
| 3 | Werkscode eingeben | Geben Sie auf dem Teilbild Arbeitsbereich festlegen: Einstieg den Werkscode ein, und wählen Sie Weiter. |  |  |
| 4 | Zum Bild "Versorgungsbereich anlegen" navigieren | Wählen Sie Neue Einträge. |  |  |
| 5 | Versorgungsbereich | Geben Sie die Details für den Produktionsversorgungsbereich ein, und wählen Sie dann Enter.Produktionsversorgungsbereich: <Versorgungsbereich>Lagerort: <Lagerort>Res: <Ein Disponent>Abladestelle: <"Abladestelle A">Name des Produktionsversorgungsbereichs: <Bezeichnung des Produktionsversorgungsbereichs> |  |  |
| 6 | Daten sichern | Wählen Sie Sichern. |  |  |
| 7 | Weitere Parameter bearbeiten (optional) | Sie können je nach Bedarf weitere erforderliche Parameter eingeben. Zum Beispiel:Bearbeiten Sie die Adresse des Produktionsversorgungsbereichs über Mehr > Springen > Adresse.Sichern Sie die Änderungen. |  |  |

Option 2:

| Testschrittnummer | Bezeichnung des Testschritts | Anweisungen | Erwartetes Ergebnis | Bestanden/Nicht bestanden/Anmerkung |
| --- | --- | --- | --- | --- |
| 1 | Anmelden | Melden Sie sich am SAP Fiori Launchpad als Produktionsplaner – Lean Manufacturing an. | Das SAP Fiori Launchpad wird angezeigt. |  |
| 2 | SAP-Fiori-App aufrufen | Öffnen Sie Produktionsversorgungsbereiche verwalten(F6935). | Die App wird geöffnet. |  |
| 3 | Anlegen | Wählen Sie im Bildbereich Produktionsversorgungsbereiche die Option Anlegen. |  |  |
| 4 | Daten eingeben | Geben Sie im Dialogfenster folgende Daten ein, und wählen Sie Weiter:Produktionsversorgungsbereich: <Versorgungsbereich>Werk: <Werk>:Lagerort: <Lagerort> |  |  |
| 5 | Grunddaten eingeben | Geben Sie im Bereich Grunddaten folgende Daten ein:Verantwortlicher: <Ein Disponent>Abladestelle: <"Abladestelle A"> |  |  |
| 6 | Beschreibung eingeben | Geben Sie im Abschnitt Sprachabhängige Bezeichnung folgende Daten ein:Sprache: <Wählen Sie einen Sprachcode, z.B. EN für Englisch>Beschreibung: <Bezeichnung des Produktionsversorgungsbereichs> |  |  |
| 7 | Daten sichern | Wählen Sie Anlegen. |  |  |
| 8 | Weitere Parameter bearbeiten (optional) | Sie können je nach Bedarf weitere erforderliche Parameter eingeben. Zum Beispiel:Bearbeiten Sie die Adresse des Produktionsversorgungsbereichs über Adresse anlegen.Sichern Sie die Änderungen. |  |  |

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
- related-to :: [[12-production-and-manufacturing/creacion-de-area-de-suministro-de-produccion-mds-40d-402]]
- related-to :: [[12-production-and-manufacturing/create-production-supply-area-mds-40d-401]]
- related-to :: [[12-production-and-manufacturing/criar-area-de-abastecimento-da-producao-mds-40d-404]]
- related-to :: [[12-production-and-manufacturing/mds-40d-403]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/40D_S4CLD2608_Master_Data_DE_XX.docx` — full document · extracted with `mammoth` · 10,465 chars in the whole document
