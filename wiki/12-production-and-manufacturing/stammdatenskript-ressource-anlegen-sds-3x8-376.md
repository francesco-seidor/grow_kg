---
id: 12-production-and-manufacturing/stammdatenskript-ressource-anlegen-sds-3x8-376
title: "Stammdatenskript: Ressource anlegen - SDS (3X8) (3X8_S4CLD2608_Master_Data_DE_XX)"
description: German master data/test script (3X8) for creating a resource (type 0008 processing unit) with app F6176 in SAP S/4HANA Cloud Public Edition 2608.
cluster: 12-production-and-manufacturing
tags: [kb/production-and-manufacturing, topic/process-resources-and-master-recipes]
aliases: [3X8_S4CLD2608_Master_Data_DE_XX]
keywords: [Process Manufacturing Resources and Master Recipes, resources, resource creation, resource types, capacity planning, default value keys, business roles, master recipes, process manufacturing, 3X8]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/3X8_S4CLD2608_Master_Data_DE_XX.docx]
confidence: high
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-376
topic: 12-production-and-manufacturing/process-resources-and-master-recipes
language: DE
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Stammdatenskript: Ressource anlegen - SDS (3X8) (3X8_S4CLD2608_Master_Data_DE_XX)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/3X8_S4CLD2608_Master_Data_DE_XX.docx`, extracted with `mammoth`. Grouped under **Process Manufacturing Resources and Master Recipes** in Production and Manufacturing. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

| <!-- image omitted: unnamed --> | StammdatenskriptSAP S/4HANA Cloud Public Edition - 02-07-26 |
| --- | --- |
|  | Ressource anlegen – SDS (3X8) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Inhaltsverzeichnis

[1 Verwendungszweck 2](#_Toc233889681)

[2 Voraussetzungen 3](#_Toc233889682)

[2.1 Systemzugriff 3](#_Toc233889683)

[2.2 Rollen 3](#_Toc233889684)

[2.3 Erforderliche Organisationseinheiten 3](#_Toc233889685)

[2.4 Obligatorische und optionale Stammdaten 3](#_Toc233889686)

[2.5 Wesentliche Parameter für die Datenerstellung 4](#_Toc233889687)

[2.5.1 Ressourcenart 4](#_Toc233889688)

[3 Übersichtstabelle 5](#_Toc233889689)

[4 Testverfahren 6](#_Toc233889690)

[4.1 Ressource anlegen 6](#_Toc233889691)

[5 Anhang 9](#_Toc233889692)

[5.1 Planungsrezept anlegen 9](#_Toc233889693)

## Verwendungszweck

Produktionsmittel und Personen, die in einen Produktionsprozess involviert sind und die ihnen zugeordnete Kapazitäten aufweisen. Ressourcen sind in Ressourcenkategorien unterteilt, z.B. Arbeit Fertigungslinie, Lagerung.

Mithilfe von Ressourcen können Sie:

- Eine Ressourcennetzwerkstruktur anlegen, um eine Reihenfolge der verwendeten Ressourcen zu definieren.
- Eine Ressourcenhierarchie definieren, um Ressourcen zur Bewertung zu gruppieren.
- Die Ressourcen klassifizieren, um deren Eignung für einen Grund oder Verwendung in einem Vorgang festzulegen.

## Voraussetzungen

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
| Alle Daten | Werk |  | Alle Daten für die Ressource hängen vom Werk ab. | Werk:__________ |

### Obligatorische und optionale Stammdaten

Ressourcendatensätze können auf andere Stammdaten verweisen. Die folgende Tabelle stellt eine Übersicht optionaler und obligatorischer Stammdatenobjekte für die Verwendung in einer Ressource bereit.

| Stammdatenobjekt | Verwendet im Datensegment | Obligatorisch / optional | Kommentare |
| --- | --- | --- | --- |
| Vorgabewertschlüssel | In der Ressourcen-Benutzungsoberfläche auf der Registerkarte "Grunddaten" finden Sie im Abschnitt Vorgabewertbehandlung den Eintrag Vorgabewertschlüssel. | obligatorisch | Das System verwendet Vorgabewerte als Parameter mit ursprünglichem Vorgabewert in Formeln für die Berechnung von Zeit, Kapazitätsanforderungen und Kosten.Sie verwenden den Vorgabewerteschlüssel, um den Vorgabewerten eine Parameter-ID zuzuordnen. Die Parameter-ID identifiziert den Vorgabewert in einer Formel. Mit der Parameter-ID können Sie das Schlüsselwort für einen Standardwert festlegen, z.B. Einrichtung, Maschine oder Arbeit. |

### Wesentliche Parameter für die Datenerstellung

In diesem Abschnitt werden einige Basisparameter erläutert, die das Verhalten eines Stammsatzes beeinflussen und zum Anlegen einer Ressource immer erforderlich sind:

#### Ressourcenart

Die Ressourcenart bestimmt die Art der Daten, die im Ressourcenstammsatz zu pflegen sind. Sie ist der Schlüssel zur Unterscheidung von Ressourcen nach ihrer Art (z.B. Ressourcennetz, Prozesseinheit).

| Ressourcenart | Beschreibung |
| --- | --- |
| 0008 | Prozesseinheit |

## Übersichtstabelle

Dieser Umfangsbestandteil umfasst die verschiedenen Prozessschritte in der folgenden Tabelle:

|  |
| --- |
| Hinweis Wenn Ihr Systemadministrator Bereiche und Seiten auf dem SAP Fiori Launchpad aktiviert hat, enthält die Startseite nur die wesentlichen Apps, mit denen die typischen Aufgaben einer Benutzerrolle ausgeführt werden können.Alle anderen (suchbaren) Apps, die nicht auf der Startseite enthalten sind, finden Sie über die Suchleiste ([2434549](https://me.sap.com/notes/2434549)).Wenn Sie die Startseite personalisieren und versteckte Apps hinzufügen möchten, wechseln Sie in Ihr Benutzerprofil und wählen Sie App Finder. |

| Prozessschritt | Benutzerrolle | App/Transaktion | Erwartete Ergebnisse |
| --- | --- | --- | --- |
| Ressource anlegen | Produktionsingenieur – Prozessfertigung | Verwaltung von Ressourcen(F6176) |  |

## Testverfahren

In diesem Abschnitt werden die Testverfahren für den jeweiligen Prozessschritt beschrieben, der zum betreffenden Umfangsbestandteil gehört.

### Ressource anlegen

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
| 1 | Anmelden | Melden Sie sich am SAP Fiori Launchpad an als Produktionsingenieur – Prozessfertigung | Die Startseite wird angezeigt. |  |
| 2 | Öffnen Sie die SAP-Fiori-App. | Wählen Sie Verwaltung von Ressourcen(F6176). |  |  |
| 3 | "Anlegen" wählen | Wählen Sie Anlegen. | Ein neues Bild Ressource anlegen: Einstieg wird angezeigt. |  |
| 4 | Werkscode eingeben | Geben Sie den Werkscode ein. | Das Bild Organisation anlegen wird angezeigt. |  |
| 5 | Ressourcen-ID eingeben | Geben Sie die Ressourcen-ID ein.Hinweis Die Ressourcen-ID muss kürzer sein als 8 Zeichen. |  |  |
| 6 | Ressourcenart | Wählen Sie die Ressourcenart:<0008> Verarbeitungseinheit |  |  |
| 7 | Grunddaten auswählen | Wählen Sie die Drucktaste Grunddaten in der oberen linken Ecke des Bildschirms. | Das Bild Ressource anzeigen: Grunddaten wird angezeigt. |  |
| 8 | Daten eingeben | Geben Sie auf der Registerkarte Grunddaten die folgenden Daten ein:Beschreibung: <Beschreibung eingeben>Verantwortlicher: <Verantwortlicher oder zuständige Person für das Werk>Verwendung: <008>Vorgabewertschlüssel: <YBP1> |  |  |
| 9 | Vorschlagswerte eingeben | Geben Sie auf der Registerkarte Vorschlagswerte folgende Daten ein:Steuerschlüssel: <YBP4>Vorgabewerteinheit Maschine: <H>Vorgabewerteinheit Arbeit: <H> |  |  |
| 10 | Kapazitäts- und Verarbeitungsformeln definieren | Geben Sie auf der Registerkarte Kapazitäten die folgenden Daten ein:Kapazitätsart: <001(Maschine)/002(Person)>Formel Rüsten: <YBPI01>Bearbeitungsformel: <YBPI02> | Wählen Sie Enter. Das Bild Ressourcenkapazität anlegen: Kopf wird angezeigt. |  |
| 11 | Ressourcenkapazität einrichten | Geben Sie im Bild Ressourcenkapazität: Kopf die folgenden Daten ein:Beschreibung Kapazitätskategorie: <Fügen Sie eine Beschreibung hinzu>Kapazität – Verantwortlicher: Wählen Sie F4, um nach der für das Werk zuständigen Person zu suchen.Fabrikkalender-ID: <Kalender für Ihr Land>Aktive Version: <1>Basis-ME Kapazität: z.B. DStartzeit:Endzeit:Pausendauer:Betriebsdauer:Nutzungsgrad: <100>Anz. Einzelkap: <10>Relevant für Kapazitätsterminierung: <X>Langfristplanung: <X>Von mehreren Vorgängen belegbar: <X>Wählen Sie Enter. | Wählen Sie Enter. Sie kehren zur Kapazitätsübersicht zurück. |  |
| 12 | Terminierungsdaten eingeben | Geben Sie auf der Registerkarte Terminierung die folgenden Daten ein:Kapazitätsart: <001(Maschine)/002(Person)>Dauer Rüsten: <YBPI01>Bearbeitungsdauer: <YBPI02> |  |  |
| 13 | Kalkulationsdaten eingeben | Geben Sie auf der Registerkarte Kalkulation die folgenden Daten ein:Kostenstelle: <Kostenstelle Fertigung für Ihren Buchungskreis>Leistungsart (Maschine): <3>Formel (Maschine): <YBPI01>Leistungsart (Arbeit): <11>Formel （Arbeit）: <YBPI02>Leistungseinheit: Wählen Sie die erforderliche Mengeneinheit, z.B. H |  |  |
| 14 | Daten sichern | Sichern Sie Ihre Eingaben. |  |  |

## Anhang

### Planungsrezept anlegen

| Stammdatenobjekt | Verwendet im Datensegment | Obligatorisch / optional | Kommentare |
| --- | --- | --- | --- |
| Planungsrezept |  |  | Spielen Sie zur Ausführung dieser Aktivität das Szenario "Planungsrezept anlegen" (3X9) durch. |

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
- related-to :: [[12-production-and-manufacturing/crear-recurso-mds-3x8-378]]
- related-to :: [[12-production-and-manufacturing/master-data-script-create-resource-mds-3x8-377]]
- related-to :: [[12-production-and-manufacturing/mds-3x8-379]]
- related-to :: [[12-production-and-manufacturing/mds-3x8-381]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/3X8_S4CLD2608_Master_Data_DE_XX.docx` — full document · extracted with `mammoth` · 11,656 chars in the whole document
