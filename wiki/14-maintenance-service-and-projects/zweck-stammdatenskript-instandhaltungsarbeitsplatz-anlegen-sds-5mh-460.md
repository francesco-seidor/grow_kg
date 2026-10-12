---
id: 14-maintenance-service-and-projects/zweck-stammdatenskript-instandhaltungsarbeitsplatz-anlegen-sds-5mh-460
title: "Zweck (Stammdatenskript: Instandhaltungsarbeitsplatz anlegen – SDS 5MH) (5MH_S4CLD2608_Master_Data_DE_XX)"
description: German master data script (5MH) for creating a maintenance work center (type 0005) with app CR01 in SAP S/4HANA Cloud Public Edition 2608.
cluster: 14-maintenance-service-and-projects
tags: [kb/maintenance-service-and-projects, topic/maintenance-work-centers]
aliases: [5MH_S4CLD2608_Master_Data_DE_XX]
keywords: [Maintenance Work Centers, maintenance work center, work center type, standard value key, work center capacity, business roles, master data scripts, plant organizational unit, 5MH]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/5MH_S4CLD2608_Master_Data_DE_XX.docx]
confidence: high
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-460
topic: 14-maintenance-service-and-projects/maintenance-work-centers
language: DE
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Zweck (Stammdatenskript: Instandhaltungsarbeitsplatz anlegen – SDS 5MH) (5MH_S4CLD2608_Master_Data_DE_XX)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/5MH_S4CLD2608_Master_Data_DE_XX.docx`, extracted with `mammoth`. Grouped under **Maintenance Work Centers** in Maintenance, Service and Projects. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

| <!-- image omitted: unnamed --> | StammdatenskriptSAP S/4HANA Cloud Public Edition - 02-07-26 |
| --- | --- |
|  | Instandhaltungsarbeitsplatz anlegen – SDS (5MH) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Inhaltsverzeichnis

[1 Zweck 2](#_Toc233889795)

[2 Voraussetzungen 3](#_Toc233889796)

[2.1 Systemzugriff 3](#_Toc233889797)

[2.2 Rollen 3](#_Toc233889798)

[2.3 Erforderliche Organisationseinheiten 3](#_Toc233889799)

[2.4 Obligatorische und optionale Stammdaten 4](#_Toc233889800)

[2.5 Wesentliche Parameter für die Datenerstellung 4](#_Toc233889801)

[2.5.1 Arbeitsplatzart 4](#_Toc233889802)

[3 Übersichtstabelle 5](#_Toc233889803)

[4 Vorgehensweise 6](#_Toc233889804)

[4.1 Instandhaltungsarbeitsplatz anlegen 6](#_Toc233889805)

## Zweck

Dieses Dokument beschreibt, wie Sie einen Instandhaltungsarbeitsplatz-Stammdatensatz für Ihr S/4HANA-System anlegen. Die Beschreibung umfasst die Datensegmente, die für die Stammdaten zum Arbeiten in einer üblichen Systemumgebung relevant sind. Der Leser lernt hauptsächlich, welche Datensegmente und -felder hauptsächlich mit Eingabewerten gefüllt werden müssen. Felder, die für den durch von SAP Best Practices bereitgestellten Umfang der Kontentauslieferung in S/4HANA nicht relevant sind, werden in diesem Dokument nicht behandelt, obwohl sie möglicherweise in der Benutzeroberfläche (UI) angezeigt werden.

Ein gemäß dieser Beschreibung angelegter Arbeitsplatz-Stammdatensatz kann für den Instandhaltungsprozesse verwendet werden.

## Voraussetzungen

Dieser Abschnitt fasst alle Voraussetzungen zum Anlegen eines Arbeitsplatzes zusammen.

### Systemzugriff

Der Test sollte mit dem folgenden System durchgeführt werden:

Tabelle 1:

| System | Details |
| --- | --- |
| System | Zugriff über das SAP Fiori Launchpad möglich. Ihr Systemadministrator stellt Ihnen die URL für den Zugriff auf die verschiedenen Apps zur Verfügung, die Ihrer Rolle zugeordnet sind. |

### Rollen

Legen Sie Benutzerrollen mit den folgenden von SAP ausgelieferten Benutzerrollenvorlagen an, und ordnen Sie sie Ihren einzelnen Testbenutzern zu.

Alternativ können Sie, falls verfügbar, die folgenden von SAP ausgelieferten Bereiche verwenden. Legen Sie einen Bereich mit Seiten an, die vordefinierte grundlegende Apps enthalten, und ordnen Sie sie der Benutzerrolle zu. Anschließend ordnen Sie diese Benutzerrolle Ihren einzelnen Benutzern zu.

Weitere Informationen finden Sie unter Anwendungsrolle aus einer Vorlage anlegen in der [Product Assistance](https://help.sap.com/docs/SAP_S4HANA_CLOUD/53e36b5493804bcdb3f6f14de8b487dd/ec310a8b669a45ca898dc4dd91d97de2.html) für SAP S/4HANA Cloud Public Edition.

| Name (Rollenvorlage) | ID (Rollenvorlage) | Name (Bereich) | ID (Bereich) |
| --- | --- | --- | --- |
| Produktionsingenieur – diskrete Fertigung | SAP_BR_PRODN_ENG_DISC | Fertigungstechnik - diskrete Fertigung | SAP_BR_PRODN_ENG_DISC |

### Erforderliche Organisationseinheiten

Einige Segmente von Stammdaten hängen von den Organisationseinheiten des Unternehmens ab. Allgemeine (zentrale) Daten hängen nicht von einer Organisationseinheit oder dem Buchungskreis ab. Die folgende Tabelle stellt eine Übersicht dieser verschiedenen Datensegmente und ihrer relevanten Organisationseinheiten bereit:

| Datensegment | Hängt ab von | Feldbeispiele | Kommentare | Zu verwendende Organisationseinheit |
| --- | --- | --- | --- | --- |
| Alle Daten | Werk |  | Alle Daten für den Arbeitsplatz hängen vom Werk ab. | Werk: –––––-- |

### Obligatorische und optionale Stammdaten

Arbeitsplatzstammsätze können auf andere Stammdaten verweisen. Die folgende Tabelle stellt eine Übersicht optionaler und obligatorischer Stammdatenobjekte für die Verwendung in einem Arbeitsplatz bereit.

| Stammdatenobjekt | Verwendet im Datensegment | Obligatorisch / optional | Kommentare |
| --- | --- | --- | --- |
| Vorgabewertschlüssel | Auf dem Bild "Arbeitsplatz", Registerkarte Grunddaten finden Sie im Abschnitt "Vorgabewertbehandlung" den Eintrag "Vorgabewertschlüssel". | obligatorisch | Das System verwendet Vorgabewerte als Parameter mit ursprünglichem Vorgabewert in Formeln für die Berechnung von Zeit, Kapazitätsanforderungen und Kosten. Sie verwenden den Vorgabewerteschlüssel, um den Vorgabewerten eine Parameter-ID zuzuordnen. Die Parameter-ID identifiziert den Vorgabewert in einer Formel. Mit der Parameter-ID können Sie das Schlüsselwort für einen Standardwert festlegen, z.B. Einrichtung, Maschine oder Arbeit. |

### Wesentliche Parameter für die Datenerstellung

In diesem Abschnitt werden einige Basisparameter erläutert, die das Verhalten eines Stammsatzes beeinflussen und zum Anlegen eines Instandhaltungsarbeitsplatzes immer erforderlich sind:

#### Arbeitsplatzart

Die Arbeitsplatzart bestimmt, welche Daten im Stammsatz für den Arbeitsplatz gepflegt werden können. Die Arbeitsplätze können nach ihrer Art unterschieden werden (z.B. Produktionsarbeitsplatz, Instandhaltungsarbeitsplatz, Servicearbeitsplatz usw.)

Tabelle 2:

| Arbeitsplatzart | Beschreibung |
| --- | --- |
| 0005 | Instandhaltung |

## Übersichtstabelle

Dieser Umfangsbestandteil umfasst die verschiedenen Prozessschritte in der Tabelle.

|  |
| --- |
| Hinweis Wenn Ihr Systemadministrator Bereiche und Seiten auf dem SAP Fiori Launchpad aktiviert hat, enthält die Startseite nur die wesentlichen Apps, mit denen die typischen Aufgaben einer Benutzerrolle ausgeführt werden können.Alle anderen (suchbaren) Apps, die nicht auf der Startseite enthalten sind, finden Sie über die Suchleiste ([2434549](https://me.sap.com/notes/2434549)).Wenn Sie die Startseite personalisieren und versteckte Apps hinzufügen möchten, wechseln Sie in Ihr Benutzerprofil und wählen Sie App Finder. |

| Prozessschritt | Benutzerrolle | App/Transaktion | Erwartete Ergebnisse |
| --- | --- | --- | --- |
| [Instandhaltungsarbeitsplatz anlegen](#unique_10) [Seite ] 6 | SAP_BR_PRODN_ENG_DISC | Arbeitsplatz anlegen(CR01) | Der Arbeitsplatz wird angelegt. |

## Vorgehensweise

In diesem Abschnitt werden die Abläufe für jeden Prozessschritt beschrieben, der zu diesem Umfangsbestandteil gehört. Sie können diese Abläufe auch zum Testen der Stammdatenerzeugung verwenden.

### Instandhaltungsarbeitsplatz anlegen

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
| 1 | Anmelden | Melden Sie sich im SAP Fiori Launchpad als SAP_BR_PRODN_ENG_DISC an. | Das SAP Fiori Launchpad wird angezeigt. |  |
| 2 | SAP-Fiori-App aufrufen | Öffnen Sie Arbeitsplatz anlegen(CR01). | Ein neues Fenster Arbeitsplatz anlegen: Einstieg wird geöffnet. |  |
| 3 | Werkscode eingeben | Geben Sie den Werkscode ein: <1010> | Das Bild Organisation anlegen wird angezeigt. |  |
| 4 | Arbeitsplatz-ID eingeben | Geben Sie die Arbeitsplatz-ID ein: <RES-0100>Hinweis Die Arbeitsplatz-ID muss kürzer sein als 8 Zeichen. |  |  |
| 5 | Arbeitsplatzart | Wählen Sie die Arbeitsplatzart aus: <0005 > Instandhaltung |  |  |
| 6 | Grunddaten auswählen | Wählen Sie Grunddaten in der oberen linken Ecke des Bildschirms. | Das Bild "Arbeitsplatz anlegen: Grunddaten" wird angezeigt. |  |
| 7 | Arbeitsplatzbeschreibung eingeben, Verantwortlichen auswählen, Verwendung und Vorgabewertschlüssel | Geben Sie auf der Registerkarte Grunddaten die folgenden Daten ein:Beschreibung: z.B. RES-0100Verantwortlicher: z.B. <YMM> Mechanischer Verantwortlicher für InstandhaltungVerwendung: z.B. <004> Nur InstandhaltungsarbeitspläneVorgabewertschlüssel: z.B. <SAP0> Keine Vorgabewerte |  |  |
| 8 | Bestätigungssteuerschlüssel eingeben | Geben Sie auf der Registerkarte Vorschlagswerte folgende Daten ein:Steuerschlüssel: z.B. <YBM1> Instandhaltung-Intern. |  |  |
| 9 | Kapazität und andere Formeln definieren | Geben Sie auf der Registerkarte Kapazitäten die folgenden Daten ein:Kapazitätsart: z.B. <002> PersonAndere Formel: z.B. <YBPM01> Proj:RqmtsNetwkMai | Wählen Sie "Enter". Das Bild "Arbeitsplatzkapazität erstellen: Kopf" wird angezeigt. |  |
| 10 | Arbeitsplatzkapazität festlegen | Geben Sie im Bereich "Arbeitsplatzkapazität": "Kopf" die folgenden Daten ein:Beschreibung Kapazitätskategorie: z.B. MechanikkapazitätKapazität – Verantwortlicher: z.B. <A> Planergruppe AFabrikkalender: Fabrikkalender-ID Kalender für Ihr Land, z.B. <01> Deutschland (Standard)Basis-ME Kapazität: z.B. <H> StundeStartzeit: z.B. <06:00:00>Endzeit: z.B. <14:30:00>Pausendauer: z.B. <00:30:00>Kapazitätsauslastung: z.B. <100>Anzahl Einzelkapaz.: z.B. <10>Langfristplanung <X> | Wählen Sie "Enter". Sie kehren zur Kapazitätsübersicht zurück. |  |
| 11 | Terminierungsdaten eingeben | Geben Sie auf der Registerkarte Terminierung die folgenden Daten ein:Kapazitätsart: z.B. <002> Person |  |  |
| 12 | Kalkulationsdaten eingeben | Geben Sie auf der Registerkarte Kalkulation die folgenden Daten ein:Startdatum: z.B. <01.01.2015>Kostenstelle: z.B. < 10101701> Werk und Instandh. (DE)Leistungsart Eigenbearbeitung: z.B. <11> PersonalstundenFormelschlüssel Kalkulation: z.B. <YBPM01> Proj:RqmtsNetwkMaint |  |  |
| 13 | Daten sichern | Sichern Sie Ihre Eingaben. | Die Eingaben werden gesichert. |  |

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
- related-to :: [[14-maintenance-service-and-projects/create-maintenance-work-center-mds-5mh-461]]
- related-to :: [[14-maintenance-service-and-projects/criar-centro-de-trabalho-de-manutencao-mds-5mh-464]]
- related-to :: [[14-maintenance-service-and-projects/mds-5mh-463]]
- related-to :: [[14-maintenance-service-and-projects/mds-5mh-465]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/5MH_S4CLD2608_Master_Data_DE_XX.docx` — full document · extracted with `mammoth` · 12,102 chars in the whole document
