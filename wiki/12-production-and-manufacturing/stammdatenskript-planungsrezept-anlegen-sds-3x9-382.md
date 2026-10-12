---
id: 12-production-and-manufacturing/stammdatenskript-planungsrezept-anlegen-sds-3x9-382
title: "Stammdatenskript - Planungsrezept anlegen (SDS, 3X9) (3X9_S4CLD2608_Master_Data_DE_XX)"
description: "German master data script (scope 3X9) for creating a planning recipe in process industry in SAP S/4HANA Cloud Public Edition, with prerequisites and 18 test steps."
cluster: 12-production-and-manufacturing
tags: [kb/production-and-manufacturing, topic/process-resources-and-master-recipes]
aliases: [3X9_S4CLD2608_Master_Data_DE_XX]
keywords: [Process Manufacturing Resources and Master Recipes, planning recipe, process manufacturing, recipe operations and phases, production versions, plan usage, change management, mandatory master data, master data scripts, 3X9]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/3X9_S4CLD2608_Master_Data_DE_XX.docx]
confidence: high
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-382
topic: 12-production-and-manufacturing/process-resources-and-master-recipes
language: DE
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Stammdatenskript - Planungsrezept anlegen (SDS, 3X9) (3X9_S4CLD2608_Master_Data_DE_XX)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/3X9_S4CLD2608_Master_Data_DE_XX.docx`, extracted with `mammoth`. Grouped under **Process Manufacturing Resources and Master Recipes** in Production and Manufacturing. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

| <!-- image omitted: unnamed --> | StammdatenskriptSAP S/4HANA Cloud Public Edition - 02-07-26 |
| --- | --- |
|  | Planungsrezept anlegen – SDS (3X9) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Inhaltsverzeichnis

[1 Verwendungszweck 2](#_Toc233889727)

[2 Voraussetzungen 3](#_Toc233889728)

[2.1 Systemzugriff 3](#_Toc233889729)

[2.2 Rollen 3](#_Toc233889730)

[2.3 Erforderliche Organisationseinheiten 3](#_Toc233889731)

[2.4 Obligatorische und optionale Stammdaten 4](#_Toc233889732)

[2.5 Wesentliche Parameter für die Datenerstellung 4](#_Toc233889733)

[2.5.1 Nutzung 4](#_Toc233889734)

[3 Übersichtstabelle 6](#_Toc233889735)

[4 Testverfahren 7](#_Toc233889736)

[4.1 Planungsrezept anlegen 7](#_Toc233889737)

[5 Anhang 10](#_Toc233889738)

[5.1 Planungsrezept mit dem Änderungsmanagement-Prozess bearbeiten 10](#_Toc233889739)

## Verwendungszweck

Mit einem Planungsrezept können Sie ein unternehmensspezifisches Verfahren in der Prozessindustrie ohne Bezug zu einem bestimmten Auftrag beschreiben.

Planungsrezepte dienen in erster Linie dazu, die Herstellung von Produkten zu planen. Sie können aber auch dazu verwendet werden, die Reinigung oder Umstellung einer Fertigungslinie zu beschreiben.

Planungsrezepte dienen als Referenz für Prozessaufträge sowie als Grundlage für die Erzeugniskalkulation.

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
| Produktionsingenieur – Prozessfertigung | SAP_BR_PRODN_ENG_PROC | Fertigungstechnik - Prozessfertigung | SAP_BR_PRODN_ENG_PROC |  |

### Erforderliche Organisationseinheiten

| Datensegment | Hängt ab von | Feldbeispiele | Kommentare | Zu verwendende Organisationseinheit |
| --- | --- | --- | --- | --- |
| Alle Daten | Werk |  | Alle Daten für ein Planungsrezept hängen vom Werk ab. | Werk:__________ |

### Obligatorische und optionale Stammdaten

Planungsrezeptdatensätze können auf andere Stammdaten verweisen. Die folgende Tabelle stellt eine Übersicht optionaler und obligatorischer Stammdatenobjekte für die Verwendung in einem Planungsrezept bereit.

| Stammdatenobjekt | Verwendet im Datensegment | Obligatorisch / optional | Kommentare |
| --- | --- | --- | --- |
| Material |  | obligatorisch | Führen Sie das folgende Testskript als eine Voraussetzung vor der Ausführung der Prozessschritte aus:Produktstamm vom Typ „Rohstoff“ anlegen – SDSProduktstamm vom Typ „Halbfabrikat“ anlegen – SDSProduktstamm vom Typ „Fertigerzeugnis“ anlegen – SDS |
| Ressource | Wählen Sie in Planungsrezept anlegen: Vorgangsübersicht einen Arbeitsplatz für einen internen Vorgang aus. | Obligatorisch, (Optional) | Für einen internen Vorgang ist der Arbeitsplatz kein obligatorisches Eingabefeld.Sofern erforderlich, führen Sie das Testskript Ressource anlegen – SDS aus. |
| Stückliste |  | optional | Führen Sie das Testskript Materialstückliste für Produktion und Vertrieb anlegen – SDS aus. |
| Einkaufsinfosatz |  | (Obligatorisch) | Für einen externen Vorgang können Sie einen Einkaufsinfosatz verwenden, um alle bezugsrelevanten Daten zu erfassen. |
| Materialgruppe |  |  |  |
| Kostenart |  |  |  |

### Wesentliche Parameter für die Datenerstellung

In diesem Abschnitt werden einige grundlegende Parameter erläutert, die das Verhalten eines Stammsatzes beeinflussen und zum Anlegen eines Planungsrezepts immer erforderlich sind.

#### Nutzung

| Schlüssel der Planverwendung | Beschreibung |
| --- | --- |
| 1 | Fertigung |
| 2 | Konstruktion |
| 3 | Universal |

## Übersichtstabelle

Dieser Umfangsbestandteil umfasst den Prozessschritt in der folgenden Tabelle:

|  |
| --- |
| Hinweis Wenn Ihr Systemadministrator Bereiche und Seiten auf dem SAP Fiori Launchpad aktiviert hat, enthält die Startseite nur die wesentlichen Apps, mit denen die typischen Aufgaben einer Benutzerrolle ausgeführt werden können.Alle anderen (suchbaren) Apps, die nicht auf der Startseite enthalten sind, finden Sie über die Suchleiste ([2434549](https://me.sap.com/notes/2434549)).Wenn Sie die Startseite personalisieren und versteckte Apps hinzufügen möchten, wechseln Sie in Ihr Benutzerprofil und wählen Sie App Finder. |

| Prozessschritt | Benutzerrolle | Transaktion | Erwartete Ergebnisse |
| --- | --- | --- | --- |
| [Planungsrezept anlegen](#unique_10) [Seite ] 7 | Produktionsingenieur – Prozessfertigung | Planungsrezepte verwalten(F5426) |  |

## Testverfahren

In diesem Abschnitt werden die Testverfahren für den jeweiligen Prozessschritt beschrieben, der zum betreffenden Umfangsbestandteil gehört.

### Planungsrezept anlegen

Testverwaltung

Kundenprojekt: Füllen Sie die projektbezogenen Teile aus.

|  |  |  |  |
| --- | --- | --- | --- |
| Testfall-ID | <X.XX> | Testdatum: |  |
| Testername: |  | Dauer: |  |
| Benutzerrolle(n): |  | Zuständigkeit: | <Geben Sie den Serviceanbieter, einen Kunden oder einen Serviceanbieter zusammen mit einem Kunden an.> |

Vorgehensweise

| Testschrittnummer | Bezeichnung des Testschritts | Anweisung | Erwartetes Ergebnis | Bestanden/Nicht bestanden/Anmerkung |
| --- | --- | --- | --- | --- |
| 1 | Anmelden | Melden Sie sich am SAP Fiori Launchpad als Produktionsingenieur – Prozessfertigung an. | Das SAP Fiori Launchpad wird angezeigt. |  |
| 2 | SAP-Fiori-App aufrufen | Öffnen Sie Planungsrezepte verwalten(F5426). |  |  |
| 3 | "Anlegen" wählen | Wählen Sie Anlegen. | Das Bild Planungsrezept anlegen: Einstieg wird angezeigt. |  |
| 4 | Bild "Planungsrezept anlegen: Einstieg" einrichten | Auf dem Bild Planungsrezept anlegen: Einstieg geben Sie die folgenden Daten ein:Material: <Materialnummer des Halbfabrikats/Fertigerzeugnisses>Werk: <Ihre Werksnummer>Profil: <YPI1>Wählen Sie Enter. | Das Bild Planungsrezept anlegen: Kopfdetails wird angezeigt. |  |
| 5 | Unterregisterkarte "Planungsrezept anlegen: Kopf" einrichten | Geben Sie auf dem Bild Planungsrezept anlegen: Rezept auf der Unterregisterkarte Rezeptkopf folgende Daten ein:Verwendung: <1 für Produktion>Status: <4 Freigegeben allgemein>Planergruppe: <1>Drücken Sie Enter. |  |  |
| 6 | Vorgang hinzufügen | Geben Sie auf der Unterregisterkarte Vorgänge folgende Daten ein:Ressource: <Ressource>Steuerschlüssel: <YBP4>Beschreibung: <Beschreibung für den Vorgang eingeben>Wählen Sie Enter. |  |  |
| 7 | Phase hinzufügen | Beginnen Sie mit einer neuen Zeile.Geben Sie auf der Unterregisterkarte Vorgänge folgende Daten ein:Phasenkennzeichen: <X>Hauptvorgang: <Vorgangs-ID, z.B. 0010>Ressource: <Ressource>Steuerschlüssel: <YBP4>Beschreibung: <Beschreibung für den Vorgang eingeben>Wählen Sie per Doppelklick die von Ihnen angelegte Phase aus. | Das Bild Planungsrezept anlegen: Vorgang wird angezeigt. |  |
| 8 | Abschnitt "Vorgabewerte" für Phase einrichten | Geben Sie auf der Unterregisterkarte Vorgabewerte folgende Daten ein, und kehren Sie dann zurück:Maschine: <Maschinenbedienungszeit>Personal: <Personalzeit> |  |  |
| 9 | Weitere Vorgänge bzw. Phasen hinzufügen | Wiederholen Sie die vorherigen Schritte für jeden Vorgang bzw. jede Phase.Wenn Sie zu diesem Zeitpunkt Komponenten zuordnen möchten, sollten Sie die folgenden Schritte durchführen. Andernfalls können Sie Ihre Eingaben sichern und die Konfiguration beenden. |  |  |
| 10 | Material auswählen | Wählen Sie in der Sicht Planungsrezept anlegen: Rezept die Unterregisterkarte Materialien. | Das Dialogfenster Fertigungsversion einfügen wird angezeigt. |  |
| 11 | Fertigungsversion einfügen | Nehmen Sie im Dialogfenster Fertigungsversion einfügen folgende Einträge vor:Fertigungsversion: <neue Fertigungsversion>Stücklistendaten - Stücklistenalternative: <Ihre Stücklistenalternative>Stücklistendaten - Stücklistenverwendung: <Verwendung>Wählen Sie Prüfen. Wählen Sie "Prüfen", überprüfen Sie die relevanten Informationen, und stellen Sie sicher, dass kein Fehler vorliegt. Wählen Sie dann Schließen. | Das Prüfkennzeichen für den Abschnitt Stücklistendaten wird grün angezeigt. |  |
| 12 | Bild schließen und Änderungen übernehmen | Wählen Sie im Dialogfenster Fertigungsversion einfügen die Option Bild schließen und Änderungen übernehmen. | Die Materialliste wird auf der Unterregisterkarte Materialien unter Materialkomponentenzuordnungen angezeigt. |  |
| 13 | Neue Zuordnung anlegen | Wählen Sie Neue Zuordnung. | Das Dialogfenster Neue Zuordnung wird angezeigt. |  |
| 14 | Zu Vorgang zuordnen Liste | Wählen Sie Vorgangs liste. |  |  |
| 15 | Vorgang wählen | Wählen Sie einen Vorgang aus, und wählen Sie dann Enter. |  |  |
| 16 | Weitere Komponenten zuordnen | Wiederholen Sie die vorherigen Schritte für weitere Komponenten. |  |  |
| 17 | Daten sichern | Sichern Sie Ihre Eingaben. | Das Planungsrezept ist angelegt. |  |
| 18 | Drucken (optional) | Suchen Sie in der App Planungsrezepte verwalten(F5426) nach dem Planungsrezept, dass Sie gerade angelegt haben, und wählen Sie es aus.Wählen Sie auf dem Bild Planungsrezept anlegen: Rezept den Pfad Mehr > Zusätze > Planungsrezept drucken. | Eine PDF-Datei mit Planungsrezeptdetails wird heruntergeladen. |  |

## Anhang

### Planungsrezept mit dem Änderungsmanagement-Prozess bearbeiten

Wenn Sie ein Planungsrezept verwenden, das genehmigt werden muss, können Sie das Testskript des Umfangsbestandteils 5QC - Produktänderungsmanagement mit Änderungsmappen – Prozessindustrie verwenden und bei jeder Änderung dem Kapitel Planungsrezept ändern folgen.

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
- related-to :: [[12-production-and-manufacturing/create-master-recipe-mds-3x9-383]]
- related-to :: [[12-production-and-manufacturing/criar-receita-mestre-mds-3x9-386]]
- related-to :: [[12-production-and-manufacturing/mds-3x9-385]]
- related-to :: [[12-production-and-manufacturing/mds-3x9-387]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/3X9_S4CLD2608_Master_Data_DE_XX.docx` — full document · extracted with `mammoth` · 13,129 chars in the whole document
