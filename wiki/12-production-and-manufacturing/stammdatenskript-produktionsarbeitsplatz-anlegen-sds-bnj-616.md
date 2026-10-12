---
id: 12-production-and-manufacturing/stammdatenskript-produktionsarbeitsplatz-anlegen-sds-bnj-616
title: "Stammdatenskript: Produktionsarbeitsplatz anlegen – SDS (BNJ) (BNJ_S4CLD2608_Master_Data_DE_XX)"
description: "German SAP S/4HANA Cloud Public Edition test script (BNJ) for creating a production work center and optionally work center groups; lists roles, parameters and steps."
cluster: 12-production-and-manufacturing
tags: [kb/production-and-manufacturing, topic/production-work-centers]
aliases: [BNJ_S4CLD2608_Master_Data_DE_XX]
keywords: [Production Work Centers and Work Center Groups, work centers, work center groups, work center category, capacity planning, default value keys, business roles, master data scripts, routings, BNJ]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/BNJ_S4CLD2608_Master_Data_DE_XX.docx]
confidence: high
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-616
topic: 12-production-and-manufacturing/production-work-centers
language: DE
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Stammdatenskript: Produktionsarbeitsplatz anlegen – SDS (BNJ) (BNJ_S4CLD2608_Master_Data_DE_XX)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/BNJ_S4CLD2608_Master_Data_DE_XX.docx`, extracted with `mammoth`. Grouped under **Production Work Centers and Work Center Groups** in Production and Manufacturing. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

| <!-- image omitted: unnamed --> | StammdatenskriptSAP S/4HANA Cloud Public Edition - 02-07-26 |
| --- | --- |
|  | Produktionsarbeitsplatz anlegen – SDS (BNJ) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Inhaltsverzeichnis

[1 Verwendungszweck 2](#_Toc233889974)

[2 Voraussetzungen 3](#_Toc233889975)

[2.1 Systemzugriff 3](#_Toc233889976)

[2.2 Rollen 3](#_Toc233889977)

[2.3 Erforderliche Organisationseinheiten 3](#_Toc233889978)

[2.4 Obligatorische und optionale Stammdaten 4](#_Toc233889979)

[2.5 Wesentliche Parameter für die Datenerstellung 4](#_Toc233889980)

[2.5.1 Arbeitsplatzart 4](#_Toc233889981)

[3 Übersichtstabelle 5](#_Toc233889982)

[4 Testverfahren 6](#_Toc233889983)

[4.1 Arbeitsplatz anlegen 6](#_Toc233889984)

[4.2 Arbeitsplatzgruppen verwalten (optional) 8](#_Toc233889985)

[4.2.1 Arbeitsplatzgruppe anlegen (optional) 8](#_Toc233889986)

[4.2.2 Arbeitsplatz zuordnen (optional) 9](#_Toc233889987)

[5 Anhang 11](#_Toc233889988)

[5.1 Arbeitsplan anlegen 11](#_Toc233889989)

## Verwendungszweck

In einem Work Center werden Fertigungsvorgänge ausgeführt. Ein Work Center kann beispielsweise eine Fertigungslinie, eine Maschine, eine Gruppe von Maschinen, einen Mitarbeiter oder einer Gruppe von Mitarbeitern repräsentieren.

Zu einem Arbeitsplatz gehören Informationen zur Kapazitätsplanung (z.B. verfügbare Kapazität), Planung (z.B. Formel für Bearbeitungszeit) und Kostenkalkulation (z.B. Kostenstelle). Diese Informationen werden in Aufgabenlisten und Vorgängen verwendet, z.B. als Fertigungsarbeitsaufträge. Die Informationen sind spezifisch für eine Produktionsstätte (Werk).

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
| Produktionsingenieur – diskrete Fertigung | SAP_BR_PRODN_ENG_DISC | Fertigungstechnik - diskrete Fertigung | SAP_BR_PRODN_ENG_DISC |  |

### Erforderliche Organisationseinheiten

| Datensegment | Hängt ab von | Feldbeispiele | Kommentare | Zu verwendende Organisationseinheit |
| --- | --- | --- | --- | --- |
| Alle Daten | Werk |  | Alle Daten für den Arbeitsplatz hängen vom Werk ab. | Werk:__________ |

### Obligatorische und optionale Stammdaten

Arbeitsplatzstammsätze können auf andere Stammdaten verweisen. Die folgende Tabelle stellt eine Übersicht optionaler und obligatorischer Stammdatenobjekte für die Verwendung in einem Arbeitsplatz bereit.

| Stammdatenobjekt | Verwendet im Datensegment | Obligatorisch / optional | Kommentare |
| --- | --- | --- | --- |
| Vorgabewertschlüssel | In der Arbeitsplatz-Benutzungsoberfläche auf der Registerkarte "Grunddaten" finden Sie im Abschnitt Vorgabewertbehandlung den Eintrag Vorgabewertschlüssel. | Obligatorisch | Das System verwendet Vorgabewerte als Parameter mit ursprünglichem Vorgabewert in Formeln für die Berechnunbg von Zeit, Kapazitätsanforderungen und Kosten.Sie verwenden den Vorgabewerteschlüssel, um den Vorgabewerten eine Parameter-ID zuzuordnen. Die Parameter-ID identifiziert den Vorgabewert in einer Formel. Mit der Parameter-ID können Sie das Schlüsselwort für einen Standardwert festlegen, z.B. Setup, Maschine oder Arbeit. |

### Wesentliche Parameter für die Datenerstellung

In diesem Abschnitt werden einige Basisparameter erläutert, die das Verhalten eines Stammsatzes beeinflussen und zum Anlegen eines Arbeitsplatzes immer erforderlich sind:

#### Arbeitsplatzart

Die Arbeitsplatzart bestimmt, welche Daten im Stammsatz für den Arbeitsplatz gepflegt werden können. Die Arbeitsplätze können nach ihrer Art unterschieden werden (z.B. Produktionsarbeitsplatz, Instandhaltungsarbeitsplatz und Servicearbeitsplatz usw.

| Arbeitsplatzart | Beschreibung |
| --- | --- |
| 0001 | Maschine |
| 0007 | Fertigungslinie |

## Übersichtstabelle

Dieser Umfangsbestandteil umfasst die verschiedenen Prozessschritte in der folgenden Tabelle:

|  |
| --- |
| Hinweis Wenn Ihr Systemadministrator Bereiche und Seiten auf dem SAP Fiori Launchpad aktiviert hat, enthält die Startseite nur die wesentlichen Apps, mit denen die typischen Aufgaben einer Benutzerrolle ausgeführt werden können.Alle anderen (suchbaren) Apps, die nicht auf der Startseite enthalten sind, finden Sie über die Suchleiste ([2434549](https://me.sap.com/notes/2434549)).Wenn Sie die Startseite personalisieren und versteckte Apps hinzufügen möchten, wechseln Sie in Ihr Benutzerprofil und wählen Sie App Finder. |

| Prozessschritt | Benutzerrolle | Transaktion | Erwartete Ergebnisse |
| --- | --- | --- | --- |
| [Arbeitsplatz anlegen](#unique_10) [Seite ] 6 | Produktionsingenieur – diskrete Fertigung | Arbeitsplätze verwalten(F6175) |  |
| [Arbeitsplatzgruppe anlegen (optional)](#unique_11) [Seite ] 8 | Produktionsingenieur – diskrete Fertigung | Arbeitsplatzgruppen verwalten(F4044) |  |
| [Arbeitsplatz zuordnen (optional)](#unique_12) [Seite ] 9 | Produktionsingenieur – diskrete Fertigung | Arbeitsplatzgruppen verwalten(F4044) |  |

## Testverfahren

In diesem Abschnitt werden die Testverfahren für den jeweiligen Prozessschritt beschrieben, der zum betreffenden Umfangsbestandteil gehört.

### Arbeitsplatz anlegen

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
| 1 | Anmelden | Melden Sie sich am SAP Fiori Launchpad als Produktionsingenieur – diskrete Fertigung an. | Das SAP Fiori Launchpad wird angezeigt. |  |
| 2 | SAP-Fiori-App öffnen | Wählen Sie Arbeitsplätze verwalten(F6175). |  |  |
| 3 | "Anlegen" wählen | Wählen Sie Anlegen. | Ein neues Bild Arbeitsplatz anlegen: Einstieg wird geöffnet. |  |
| 4 | Werkscode eingeben | Geben Sie den Werkscode ein. | Das Bild Organisation anlegen wird angezeigt. |  |
| 5 | Arbeitsplatz-ID eingeben | Geben Sie die Arbeitsplatz-ID ein.Hinweis Die Arbeitsplatz-ID muss kürzer sein als 8 Zeichen. |  |  |
| 6 | Arbeitsplatzart | Wählen Sie die Arbeitsplatzart aus:<0001> Maschine<0007> Fertigungslinie |  |  |
| 7 | Grunddaten auswählen | Wählen Sie die Drucktaste Grunddaten in der oberen linken Ecke des Bildschirms. | Das Bild Arbeitsplatz anlegen: Grunddaten wird angezeigt. |  |
| 8 | Daten eingeben | Geben Sie auf der Registerkarte Grunddaten die folgenden Daten ein:Beschreibung: <Beschreibung eingeben>Verantwortlicher: <Verantwortlicher oder zuständige Person für das Werk>Verwendung: <009>Vorgabewertschlüssel: <SAP1> |  |  |
| 9 | Kapazitäts- und Verarbeitungsformeln definieren | Geben Sie auf der Registerkarte Kapazitäten die folgenden Daten ein:Kapazitätsart: <001(Maschine)/002(Person)>Formel Rüsten: <SAP005>Bearbeitungsformel: <SAP006>Drücken Sie Enter. | Das Bild Arbeitsplatzkapazität erstellen: Kopf wird angezeigt. |  |
| 10 | Arbeitsplatzkapazität festlegen | Geben Sie im Bereich Arbeitsplatzkapazität: Kopf die folgenden Daten ein:Beschreibung Kapazitätskategorie: <Fügen Sie eine Beschreibung hinzu>Kapazität – Verantwortlicher: Drücken Sie F4, um nach der für das Werk zuständigen Person zu suchen.Fabrikkalender-ID: <Kalender für Ihr Land>Aktive Version: <1>Basis-ME Kapazität: z.B. DStartzeit: <Startzeit>Endzeit: <Endzeit>Pausendauer: <Pausendauer>Betriebsdauer: <Betriebsdauer>Nutzungsgrad: <100>Anz. Einzelkap: <10>Relevant für Kapazitätsterminierung: <X>Langfristplanung: <X>Von mehreren Vorgängen belegbar: <X>Drücken Sie Enter. | Sie kehren zur Kapazitätsübersicht zurück. |  |
| 11 | Terminierungsdaten eingeben | Geben Sie auf der Registerkarte Terminierung die folgenden Daten ein:Kapazitätsart: <001(Maschine)/002(Person)>Dauer Rüsten: <SAP001>Bearbeitungsdauer: <SAP002> |  |  |
| 12 | Kalkulationsdaten eingeben | Geben Sie auf der Registerkarte Kalkulation die folgenden Daten ein:Kostenstelle: <Kostenstelle für Ihren Buchungskreis>Leistungsart (für Rüsten): <3>Formel (für Rüsten): <SAP005>Leistungsart (Maschine): <1>Formel (Maschine): <SAP006>Leistungsart (Arbeit): <11>Formel （Arbeit）: <SAP007>Leistungseinheit: Wählen Sie die erforderliche Mengeneinheit, z.B. Min. |  |  |
| 13 | Daten sichern | Sichern Sie Ihre Eingaben. |  |  |

### Arbeitsplatzgruppen verwalten (optional)

Zweck

Dieses Kapitel beschreibt, wie Sie Arbeitsplätze bei Bedarf gruppieren können.

#### Arbeitsplatzgruppe anlegen (optional)

Testverwaltung

Kundenprojekt: Füllen Sie die projektbezogenen Teile aus.

|  |  |  |  |
| --- | --- | --- | --- |
| Testfall-ID | <X.XX> | Testdatum: |  |
| Testername: |  | Dauer: |  |
| Benutzerrolle(n): |  | Zuständigkeit: | <Geben Sie den Serviceanbieter, einen Kunden oder einen Serviceanbieter zusammen mit einem Kunden an.> |

Zweck

Dieser Prozessschritt zeigt Ihnen, wie Sie eine Arbeitsplatzgruppe anlegen.

Sie können die Beispiel-Arbeitsplatzgruppen prüfen, die über den Prozessschritt Arbeitsplatzgruppe anlegen und zuordnen im Umfangsbestandteil 31L angelegt wurden.

Vorgehensweise

| Testschrittnummer | Bezeichnung des Testschritts | Anweisung | Erwartetes Ergebnis | Bestanden/Nicht bestanden/Anmerkung |
| --- | --- | --- | --- | --- |
| 1 | Anmelden | Melden Sie sich als Produktionsingenieur – diskrete Fertigung am SAP Fiori Launchpad an. | Das SAP Fiori Launchpad wird angezeigt. |  |
| 2 | App aufrufen | Öffnen Sie Arbeitsplatzgruppen verwalten(F4044). | Die App wird geöffnet. |  |
| 3 | Gruppe anlegen | Wählen Sie über der Tabelle Anlegen.Geben Sie auf dem Bild Gruppe anlegen folgende Daten ein:Gruppe: <Geben Sie den Namen der Gruppe ein.>Werk: 1010Gruppentyp: <ALTERNATIVE> oder <GLEICHE ZEILE> oder <ZUSTÄNDIGKEIT>Beschreibung: <Geben Sie die Beschreibung ein.>Wählen Sie Anlegen. | Die Arbeitsplatzgruppe wird angelegt. |  |

#### Arbeitsplatz zuordnen (optional)

Testverwaltung

Kundenprojekt: Füllen Sie die projektbezogenen Teile aus.

|  |  |  |  |
| --- | --- | --- | --- |
| Testfall-ID | <X.XX> | Testdatum: |  |
| Testername: |  | Dauer: |  |
| Benutzerrolle(n): |  | Zuständigkeit: | <Geben Sie den Serviceanbieter, einen Kunden oder einen Serviceanbieter zusammen mit einem Kunden an.> |

Zweck

Dieser Prozessschritt zeigt Ihnen, wie Sie einer Arbeitsplatzgruppe Arbeitsplätze zuordnen.

Vorgehensweise

| Testschrittnummer | Bezeichnung des Testschritts | Anweisung | Erwartetes Ergebnis | Bestanden/Nicht bestanden/Anmerkung |
| --- | --- | --- | --- | --- |
| 1 | Anmelden | Melden Sie sich am SAP Fiori Launchpad als Produktionsingenieur – diskrete Fertigung an. | Das SAP Fiori Launchpad wird angezeigt. |  |
| 2 | App aufrufen | Öffnen Sie Arbeitsplatzgruppen verwalten(F4044). | Die App wird geöffnet. |  |
| 3 | Gruppe auswählen | Suchen Sie nach der im vorherigen Schritt angelegten Gruppe, und wählen Sie dann das Symbol ">" am Ende der Zeile. | Im rechten Bildbereich wird eine Liste mit detaillierten Informationen angezeigt. |  |
| 4 | Arbeitsplatz zuordnen | Wählen Sie im Abschnitt Komponenten gruppieren die Option Arbeitsplatz zuordnen.Wählen Sie einen oder mehrere Arbeitsplätze aus dem Dialogfenster aus, und wählen Sie OK.Hinweis Wenn ein Arbeitsplatz bereits einer anderen Gruppe zugeordnet ist, wird folgende Fehlermeldung ausgegeben: Arbeitsplatz 'XXX' ist bereits dieser Gruppenart zugeordnet. | Die der Gruppe zugeordneten Arbeitsplätze werden angezeigt.Die Arbeitsplätze werden erfolgreich zugeordnet. |  |

## Anhang

### Arbeitsplan anlegen

| Stammdatenobjekt | Verwendet im Datensegment | Obligatorisch / optional | Kommentare |
| --- | --- | --- | --- |
| Arbeitsplan |  |  | Um diese Aktivität durchführen zu können, führen Sie das Testskript Arbeitsplan anlegen – SDS (BNL) aus. |

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
- related-to :: [[12-production-and-manufacturing/create-production-work-center-mds-bnj-617]]
- related-to :: [[12-production-and-manufacturing/mds-bnj-619]]
- related-to :: [[12-production-and-manufacturing/mds-bnj-621]]
- related-to :: [[12-production-and-manufacturing/script-de-dados-mestre-criar-centro-de-trabalho-da-producao-mds-bnj-62]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/BNJ_S4CLD2608_Master_Data_DE_XX.docx` — full document · extracted with `mammoth` · 15,579 chars in the whole document
