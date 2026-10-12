---
id: 12-production-and-manufacturing/fertigungsversion-anlegen-sds-bld-568
title: Fertigungsversion anlegen – SDS (BLD) (BLD_S4CLD2608_Master_Data_DE_XX)
description: "German master data script (BLD) for SAP S/4HANA Cloud Public Edition: create and edit production versions via Fiori apps F6400 and F2568."
cluster: 12-production-and-manufacturing
tags: [kb/production-and-manufacturing, topic/production-versions]
aliases: [BLD_S4CLD2608_Master_Data_DE_XX]
keywords: [Production Versions, production version editing, master data scripts, bills of material, routings, business roles, production version proposals, mass editing, BLD]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/BLD_S4CLD2608_Master_Data_DE_XX.docx]
confidence: high
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-568
topic: 12-production-and-manufacturing/production-versions
language: DE
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Fertigungsversion anlegen – SDS (BLD) (BLD_S4CLD2608_Master_Data_DE_XX)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/BLD_S4CLD2608_Master_Data_DE_XX.docx`, extracted with `mammoth`. Grouped under **Production Versions** in Production and Manufacturing. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

| <!-- image omitted: unnamed --> | StammdatenskriptSAP S/4HANA Cloud Public Edition - 02-07-26 |
| --- | --- |
|  | Fertigungsversion anlegen – SDS (BLD) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Inhaltsverzeichnis

[1 Zweck 2](#_Toc233889921)

[2 Voraussetzungen 3](#_Toc233889922)

[2.1 Systemzugriff 3](#_Toc233889923)

[2.2 Rollen 3](#_Toc233889924)

[2.3 Erforderliche Organisationseinheiten 3](#_Toc233889925)

[2.4 Obligatorische und optionale Stammdaten 4](#_Toc233889926)

[3 Übersichtstabelle 5](#_Toc233889927)

[4 Testverfahren 6](#_Toc233889928)

[4.1 Fertigungsversion anlegen 6](#_Toc233889929)

[4.2 Fertigungsversion bearbeiten (optional) 9](#_Toc233889930)

## Zweck

Fertigungsversion anlegen

Dieses Dokument beschreibt, wie Sie eine Fertigungsversion für Ihr SAP S/4HANA Cloud Public Edition-System anlegen. Die Beschreibung umfasst die Datensegmente, die für die SAP S/4HANA Cloud Public Edition-Appliance relevant sind. Felder, die für den Umfang der SAP S/4HANA Cloud Public Edition-Inhalte nicht relevant sind, werden in diesem Dokument nicht behandelt.

Eine gemäß dieser Beschreibung angelegte Fertigungsversion kann für den Fertigungsprozess verwendet werden.

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
| Produktionsingenieur – diskrete Fertigung | SAP_BR_PRODN_ENG_DISC | Fertigungstechnik - diskrete Fertigung | SAP_BR_PRODN_ENG_DISC |  |
| Produktionsingenieur – Prozessfertigung | SAP_BR_PRODN_ENG_PROC | Fertigungstechnik - Prozessfertigung | SAP_BR_PRODN_ENG_PROC |  |

### Erforderliche Organisationseinheiten

| Datensegment | Hängt ab von | Feldbeispiele | Kommentare | Zu verwendende Organisationseinheit |
| --- | --- | --- | --- | --- |
| Alle Daten | Werk |  | Alle Daten für die Fertigungsversion hängen vom Werk ab. | Werk:__________ |

### Obligatorische und optionale Stammdaten

Daten von Fertigungsversionen können auf andere Stammdaten verweisen. Die folgende Tabelle stellt eine Übersicht optionaler und obligatorischer Stammdatenobjekte für die Verwendung in einer Fertigungsversion bereit.

| Stammdatenobjekt | Verwendet im Datensegment | Obligatorisch / optional | Kommentare |
| --- | --- | --- | --- |
| Material | Die Fertigungsversion wird pro Material und Werk angelegt. | Obligatorisch | Auf dem Bild Fertigungsversion: Massenverarbeitung muss das Material eingegeben werden.Zum Anlegen von Material können Sie die Schritte im Stammdatenskript ausführen: Produktstamm vom Typ „Rohstoff“ anlegen – SDS - BNR, Produktstamm vom Typ „Halbfabrikat“ anlegen – SDS - BNS oder Produktstamm vom Typ „Fertigerzeugnis“ anlegen – SDS - BNT. |
| Stückliste | In der Fertigungsversion werden die Stücklistendaten dem Material zugeordnet. | Obligatorisch | Auf dem Bild Fertigungsversion: Massenpflege müssen die Stücklistenalternative und die Stücklistenverwendung eingegeben werden.Zum Anlegen von Stücklisten können Sie die Schritte im Stammdatenskript ausführen: Materialstückliste für Produktion und Vertrieb anlegen – SDS – BNK. |
| Aufgabenliste | In der Fertigungsversion wird die Aufgabenliste dem Material zugeordnet. | Obligatorisch | Auf dem Bild Fertigungsversion: Massenpflege müssen der Plantyp, die Gruppe und der Plangruppenzähler eingegeben werden.Zum Anlegen eines Aufgabenplans können Sie die Schritte im Stammdatenskript ausführen: Arbeitsplan anlegen – SDS - BNL oder Planungsrezept anlegen – SDS - 3X9. |

## Übersichtstabelle

Dieser Umfangsbestandteil umfasst die verschiedenen Prozessschritte in der folgenden Tabelle:

|  |
| --- |
| Hinweis Wenn Ihr Systemadministrator Bereiche und Seiten auf dem SAP Fiori Launchpad aktiviert hat, enthält die Startseite nur die wesentlichen Apps, mit denen die typischen Aufgaben einer Benutzerrolle ausgeführt werden können.Alle anderen (suchbaren) Apps, die nicht auf der Startseite enthalten sind, finden Sie über die Suchleiste ([2434549](https://me.sap.com/notes/2434549)).Wenn Sie die Startseite personalisieren und versteckte Apps hinzufügen möchten, wechseln Sie in Ihr Benutzerprofil und wählen Sie App Finder. |

| Prozessschritt | Anwendungsrolle | Transaktion | Erwartete Ergebnisse |
| --- | --- | --- | --- |
| [Fertigungsversion anlegen](#unique_8) [Seite ] 6 | Produktionsingenieur – diskrete Fertigung oder Produktionsingenieur – Prozessfertigung | Fertigungsversionen bearbeiten(F6400) oder Fertigungsversionen bearbeiten(F2568) |  |
| [Fertigungsversion bearbeiten (optional)](#unique_9) [Seite ] 9 | Produktionsingenieur – diskrete Fertigung oder Produktionsingenieur – Prozessfertigung | Fertigungsversionen bearbeiten(F6400) |  |

## Testverfahren

In diesem Abschnitt werden die Testverfahren für den jeweiligen Prozessschritt beschrieben, der zum betreffenden Umfangsbestandteil gehört.

### Fertigungsversion anlegen

Testverwaltung

Kundenprojekt: Füllen Sie die projektbezogenen Teile aus.

|  |  |  |  |
| --- | --- | --- | --- |
| Testfall-ID | <X.XX> | Testdatum: |  |
| Testername: |  | Dauer: |  |
| Benutzerrolle(n): |  | Zuständigkeit: | <Geben Sie den Serviceanbieter, einen Kunden oder einen Serviceanbieter zusammen mit einem Kunden an.> |

Vorgehensweise

Diesen Schritt können Sie mit verschiedenen SAP-Fiori-Apps durchführen. Dafür gibt es drei Optionen. Sie können eine davon auswählen.

Option 1

| Testschrittnummer | Bezeichnung des Testschritts | Anweisung | Erwartetes Ergebnis | Kommentare |
| --- | --- | --- | --- | --- |
| 1 | Anmelden | Melden Sie sich am SAP Fiori Launchpad als Produktionsingenieur – diskrete Fertigung oder als Produktionsingenieur – Prozessfertigung an. | Die Sicht Start wird angezeigt. |  |
| 2 | SAP-Fiori-App aufrufen | Öffnen Sie Fertigungsversionen bearbeiten(F6400). | Die App wird geöffnet. |  |
| 3 | Selektionsfelder eingeben | Geben Sie Folgendes ein, und wählen Sie Start:Material: <Geben Sie die Materialnummer ein>Werk:: Werk eingeben |  |  |
| 4 | Vorschläge für Fertigungsversion prüfen | Auf der Registerkarte Fertigungsversionsvorschläge finden Sie die Vorschläge zum Anlegen einer neuen Fertigungsversion, wenn die entsprechende Stücklisten-/Plankombination noch nicht vorhanden ist.Sie können die Vorschlagsdetails durchgehen, indem Sie den Vorschlag auswählen und mögliche Änderungen vornehmen. | Hinweis Der Konfigurationsschritt (ID: 105965) wurde eingeführt, um die Regeln für den Produktionsversionsvorschlag zu konfigurieren. |  |
| 5 | Vorschlag übernehmen | Markieren Sie den Fertigungsversionsvorschlag, und wählen Sie Vorschlag übernehmen. |  |  |
| 6 | Bestätigung | Wählen Sie im Dialogfenster Bestätigung die Drucktaste OK. | Basierend auf den vorgeschlagenen Parametern wird eine neue Fertigungsversion angelegt. Sie finden sie auf der Registerkarte Vorhandene Fertigungsversionen. |  |

Option 2

| Testschrittnummer | Bezeichnung des Testschritts | Anweisung | Erwartetes Ergebnis | Kommentare |
| --- | --- | --- | --- | --- |
| 1 | Anmelden | Melden Sie sich am SAP Fiori Launchpad als Produktionsingenieur – diskrete Fertigung oder als Produktionsingenieur – Prozessfertigung an. | Die Sicht Start wird angezeigt. |  |
| 2 | SAP-Fiori-App aufrufen | Öffnen Sie Fertigungsversionen bearbeiten(F6400). | Die App wird geöffnet. |  |
| 3 | Selektionsfelder eingeben | Geben Sie Folgendes ein, und wählen Sie Start:Material: <Geben Sie die Materialnummer ein>Werk:: Werk eingeben |  |  |
| 4 | Registerkarte auswählen | Wählen Sie die Registerkarte Vorhandene Fertigungsversionen. |  |  |
| 5 | Anlegen | Wählen Sie Anlegen. Geben Sie im Dialogfenster Fertigungsversion anlegen folgende Daten ein, und wählen Sie Anlegen:Material: <Geben Sie die Materialnummer ein>Werk:: Werk eingebenFertigungsversion: <beliebige Nummer mit 4 Ziffern>Fertigungsversion (Beschreibung): <Beschreibung> |  |  |
| 6 | Eingabeparameter | Geben Sie die erforderlichen Parameter ein, und wählen Sie Anlegen:Gültigkeitsbeginn: <heute>Gültigkeitsende: <31.12.9999>Minimale Losgröße: <1>Maximale Losgröße: <999999999>Abschnitt Aufgabenliste:Plantyp: <Plantyp für das Material auswählen>Plangruppe: Gruppe für das Material auswählen>Planzähler: <Gruppenzähler für das Material auswählen>Abschnitt Stückliste:Stücklistenalternative: <Stücklistenalternative für das Material auswählen>Stücklistenverwendung: <Stücklistenverwendung des Stücklistenstamms für das Material auswählen> | Die Fertigungsversion wird angelegt. |  |

Option 3

| Testschrittnummer | Bezeichnung des Testschritts | Anweisung | Erwartetes Ergebnis | Kommentare |
| --- | --- | --- | --- | --- |
| 1 | Anmelden | Melden Sie sich am SAP Fiori Launchpad als Produktionsingenieur – diskrete Fertigung oder als Produktionsingenieur – Prozessfertigung an. | Die Sicht Start wird angezeigt. |  |
| 2 | SAP-Fiori-App aufrufen | Öffnen Sie Fertigungsversionen bearbeiten(F2568). | Die Sicht Fertigungsversion: Sammelbearbeitung wird angezeigt. |  |
| 3 | Werkscode eingeben | Geben Sie den Werkscode ein. |  |  |
| 4 | Material eingeben | Geben Sie das Material ein.Bestätigen Sie mit Enter. |  |  |
| 5 | Fertigungsversion | Geben Sie die Einzelpositionen der Fertigungsversion ein, und wählen Sie Enter.Material: <Geben Sie die Materialnummer ein>Fertigungsversion: <beliebige Nummer mit 4 Ziffern>Gültig ab: <aktuelles Datum>Gültig bis: <31.12.9999>von Losgröße: <1>bis Losgröße: <999999999>Stücklistenalternative: Drücken Sie F4, und wählen Sie für das Material Stücklistenalternative aus.Stücklistenverwendung: Drücken Sie F4, und wählen Sie für das Material Stücklistenverwendung im Stücklistenstamm aus.Gruppe: <Geben Sie Gruppe für das Material ein>Plangruppenzähler: <Geben Sie den Plangruppenzähler für das Material ein>Typ: <Plantyp für das Material auswählen> |  |  |
| 6 | Daten sichern | Wählen Sie Sichern. | Die Fertigungsversion wird angelegt. |  |

### Fertigungsversion bearbeiten (optional)

Testverwaltung

Kundenprojekt: Füllen Sie die projektbezogenen Teile aus.

|  |  |  |  |
| --- | --- | --- | --- |
| Testfall-ID | <X.XX> | Testdatum: |  |
| Testername: |  | Dauer: |  |
| Benutzerrolle(n): |  | Zuständigkeit: | <Geben Sie den Serviceanbieter, einen Kunden oder einen Serviceanbieter zusammen mit einem Kunden an.> |

Vorgehensweise

| Testschrittnummer | Bezeichnung des Testschritts | Anweisung | Erwartetes Ergebnis | Kommentare |
| --- | --- | --- | --- | --- |
| 1 | Anmelden | Melden Sie sich am SAP Fiori Launchpad als Produktionsingenieur – diskrete Fertigung oder als Produktionsingenieur – Prozessfertigung an. | Das SAP Fiori Launchpad wird angezeigt. |  |
| 2 | SAP-Fiori-App aufrufen | Öffnen Sie Fertigungsversionen bearbeiten(F6400). | Die App wird geöffnet. |  |
| 3 | Selektionsfelder eingeben | Geben Sie Folgendes ein, und wählen Sie Start:Material: <Geben Sie die Materialnummer ein>Werk:: Werk eingeben |  |  |
| 4 | Zur Registerkarte "Vorhandene Fertigungsversionen" navigieren | Wechseln Sie zur Registerkarte Vorhandene Fertigungsversionen. |  |  |
| 5 | Fertigungsversion bearbeiten | Wählen Sie die Fertigungsversion aus, die Sie ändern möchten, und wählen Sie auf dem Bild Fertigungsversion die Option Bearbeiten.Nehmen Sie entsprechend Ihren Anforderungen die erforderlichen Änderungen an den Feldern vor.Hinweis Wenn Sie ähnliche Änderungen an mehreren Fertigungsversionen vornehmen möchten, können Sie auf der Registerkarte Vorhandene Fertigungsversionen eine Mehrfachauswahl vornehmen und Massenbearbeitung wählen.Im Dialogfenster Massenbearbeitung können Sie die erforderlichen Änderungen an den aufgeführten Feldern vornehmen. |  |  |
| 6 | Sichern | Wählen Sie Sichern. | Die Fertigungsversion wurde erfolgreich aktualisiert. |  |

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
- related-to :: [[12-production-and-manufacturing/master-data-script-create-production-version-mds-bld-569]]
- related-to :: [[12-production-and-manufacturing/mds-bld-571]]
- related-to :: [[12-production-and-manufacturing/mds-bld-573]]
- related-to :: [[12-production-and-manufacturing/script-de-dados-mestre-criar-versao-de-producao-mds-bld-572]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/BLD_S4CLD2608_Master_Data_DE_XX.docx` — full document · extracted with `mammoth` · 15,416 chars in the whole document
