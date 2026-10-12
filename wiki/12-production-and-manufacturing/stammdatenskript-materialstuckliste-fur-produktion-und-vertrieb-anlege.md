---
id: 12-production-and-manufacturing/stammdatenskript-materialstuckliste-fur-produktion-und-vertrieb-anlege
title: "Stammdatenskript - Materialstückliste für Produktion und Vertrieb anlegen (BNK), DE (BNK_S4CLD2608_Master_Data_DE_XX)"
description: "German SAP S/4HANA Cloud Public Edition 2608 master data script (BNK): create material BOMs for production and sales, with test steps."
cluster: 12-production-and-manufacturing
tags: [kb/production-and-manufacturing, topic/material-boms]
aliases: [BNK_S4CLD2608_Master_Data_DE_XX]
keywords: [Material BOMs for Production and Sales, bill of materials, production bom, sales bom, change number, business roles, bom usage, bom item categories, master data scripts, routing]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/BNK_S4CLD2608_Master_Data_DE_XX.docx]
confidence: high
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-622
topic: 12-production-and-manufacturing/material-boms
language: DE
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Stammdatenskript - Materialstückliste für Produktion und Vertrieb anlegen (BNK), DE (BNK_S4CLD2608_Master_Data_DE_XX)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/BNK_S4CLD2608_Master_Data_DE_XX.docx`, extracted with `mammoth`. Grouped under **Material BOMs for Production and Sales** in Production and Manufacturing. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

| <!-- image omitted: unnamed --> | StammdatenskriptSAP S/4HANA Cloud Public Edition - 02-07-26 |
| --- | --- |
|  | Materialstückliste für Produktion und Vertrieb anlegen – SDS (BNK) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Inhaltsverzeichnis

[1 Zweck 2](#_Toc233889980)

[2 Voraussetzungen 3](#_Toc233889981)

[2.1 Systemzugriff 3](#_Toc233889982)

[2.2 Rollen 3](#_Toc233889983)

[2.3 Erforderliche Organisationseinheiten 3](#_Toc233889984)

[2.4 Obligatorische und optionale Stammdaten 4](#_Toc233889985)

[2.5 Wesentliche Parameter für die Datenerstellung 4](#_Toc233889986)

[2.5.1 STL-Verwendung 4](#_Toc233889987)

[3 Übersichtstabelle 5](#_Toc233889988)

[4 Testverfahren 6](#_Toc233889989)

[4.1 Änderungsnummer anlegen 6](#_Toc233889990)

[4.2 Produktionsstückliste anlegen 7](#_Toc233889991)

[4.3 Verkaufsstückliste anlegen 9](#_Toc233889992)

[5 Anhang 11](#_Toc233889993)

[5.1 Folgeprozesse Arbeitsplan anlegen 11](#_Toc233889994)

## Zweck

Eine Produktionsstückliste ist eine formal strukturierte Liste der Komponenten, aus denen ein Produkt oder eine Baugruppe (ein Teil eines Produkts) besteht. Die Liste enthält die Objektnummer einer jeden Komponente, zusammen mit der Menge und der Mengeneinheit. Eine Komponente kann ein Rohstoff oder ein Halbfabrikat sein, das eine Baugruppe repräsentiert.

Sie wird in einer Materialbedarfsplanung verwendet, um den Materialbedarf zu berechnen, und in Transaktionen, wie zum Beispiel einem Fertigungsauftrag. Die Informationen sind spezifisch für eine Produktionsstätte (Werk).

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
| Stücklistenbearbeiter | SAP_BR_BOM_ENGINEER | Stücklisten | SAP_BR_BOM_ENGINEER |  |

### Erforderliche Organisationseinheiten

Die Organisationsstruktur und die Stammdaten Ihres Unternehmens wurden bei der Aktivierung in Ihrem System erzeugt. Die Organisationsstruktur gibt den Aufbau Ihres Unternehmens wieder. Die Stammdaten stehen beispielsweise für Materialien, Kunden und Lieferanten, je nach betrieblichem Schwerpunkt Ihres Unternehmens.

Verwenden Sie beim Durchführen des Tests eigene Stammdaten oder die folgenden Beispieldaten.

### Obligatorische und optionale Stammdaten

Stücklistendatensätze können auf andere Stammdaten verweisen. Die folgende Tabelle stellt eine Übersicht optionaler und obligatorischer Stammdatenobjekte für die Verwendung in einer Stückliste bereit.

| Stammdatenobjekt | Verwendet im Datensegment | Obligatorisch / optional | Kommentare |
| --- | --- | --- | --- |
| Material | Geben Sie in den Bildern Anlegen Materialstückliste: Einstieg und Anlegen Materialstückliste: Positionsübersicht Allgemeines die <Materialnummer> in das Feld Material und Komponente ein. | obligatorisch | Führen Sie folgende Stammdatenskripte als Voraussetzung für den Beginn der Prozessschritte aus:Produktstamm vom Typ „Rohstoff“ anlegen – SDS (BNR)Produktstamm vom Typ „Halbfabrikat“ anlegen – SDS (BNS)Produktstamm vom Typ „Fertigerzeugnis“ anlegen – SDS (BNT)Produktstamm vom Typ „Handelsware“ anlegen – SDS (BNF) |

### Wesentliche Parameter für die Datenerstellung

In diesem Abschnitt werden einige Basisparameter erläutert, die das Verhalten eines Stammsatzes beeinflussen und zum Anlegen einer Stückliste immer erforderlich sind:

#### STL-Verwendung

Die Stücklistenverwendung legt fest, in welchem Bereich (z.B. Vertrieb oder Fertigung) eine Materialstückliste verwendet werden kann.

| Stücklistenverwendung | Beschreibung |
| --- | --- |
| 1 | Fertigung |
| 5 | Vertrieb |

## Übersichtstabelle

Dieser Umfangsbestandteil umfasst mehrere Prozessschritte, die in der folgenden Tabelle aufgelistet sind:

|  |
| --- |
| Hinweis Wenn Ihr Systemadministrator Bereiche und Seiten auf dem SAP Fiori Launchpad aktiviert hat, enthält die Startseite nur die wesentlichen Apps, mit denen die typischen Aufgaben einer Benutzerrolle ausgeführt werden können.Alle anderen (suchbaren) Apps, die nicht auf der Startseite enthalten sind, finden Sie über die Suchleiste ([2434549](https://me.sap.com/notes/2434549)).Wenn Sie die Startseite personalisieren und versteckte Apps hinzufügen möchten, wechseln Sie in Ihr Benutzerprofil und wählen Sie App Finder. |

| Prozessschritt | Anwendungsrolle | Bewegung | Erwartete Ergebnisse |
| --- | --- | --- | --- |
| [Änderungsnummer anlegen](#unique_10) [Seite ] 6 | Stücklistenbearbeiter | Änderungsstammsatz anlegen(CC01) |  |
| [Produktionsstückliste anlegen](#unique_11) [Seite ] 7 | Produktionsingenieur – diskrete Fertigung | Stückliste pflegen (Version 2) – Stücklisten anlegen, ändern und anzeigen(F1813A) |  |
| [Verkaufsstückliste anlegen](#unique_12) [Seite ] 9 | Produktionsingenieur – diskrete Fertigung | Stückliste pflegen – Stücklisten anlegen, ändern und anzeigen(F1813) |  |

## Testverfahren

In diesem Abschnitt werden die Testverfahren für den jeweiligen Prozessschritt beschrieben, der zum betreffenden Umfangsbestandteil gehört.

### Änderungsnummer anlegen

Testverwaltung

Kundenprojekt: Füllen Sie die projektbezogenen Teile aus.

|  |  |  |  |
| --- | --- | --- | --- |
| Testfall-ID | <X.XX> | Testdatum: |  |
| Testername: |  | Dauer: |  |
| Benutzerrolle(n): |  | Zuständigkeit: | <Geben Sie den Serviceanbieter, einen Kunden oder einen Serviceanbieter zusammen mit einem Kunden an.> |

Zweck

Der Änderungsstamm, der zur Stücklistenerstellung in den nächsten Schritten der Produktionsstückliste und Stückliste verwendet wird, wird angelegt.

Vorgehensweise

| Testschrittnummer | Bezeichnung des Testschritts | Anweisungen | Erwartetes Ergebnis | Bestanden/Nicht bestanden/Anmerkung |
| --- | --- | --- | --- | --- |
| 1 | Anmelden | Melden Sie sich am SAP Fiori Launchpad als Stücklistenbearbeiter an. |  |  |
| 2 | SAP-Fiori-App aufrufen | Öffnen Sie Änderungsstammsatz anlegen(CC01). |  |  |
| 3 | Änderungsnummer erfassen | Geben Sie auf dem Bild Änderungsstamm anlegen: Anforderungsbild folgende Daten ein, und wählen Sie Enter.Änderungsnummer: <Geben Sie Ihre Änderungsnummer ein, z.B. CN001>In den anderen Feldern behalten Sie die Standardwerte bei. |  |  |
| 4 | Änderungsstammdaten erfassen | Geben Sie auf dem Bild Änderungsstamm anlegen: Änderungskopf die im folgenden Beispiel bereitgestellten Daten ein, und drücken Sie Enter:Feld neben Änderungsnummer: Änderungsstamm für MaterialstücklisteGültig ab: <aktuelles Datum>Status Änderungsnr.: 01 Aktiv |  |  |
| 5 | Ankreuzfelder für Stückliste markieren | Auf dem Bild Änderungsstamm anlegen: Objekttypen markieren Sie in der Tabelle Objekttypen in der Zeile Stückliste die folgenden Ankreuzfelder:AktivObjektObjVGen |  |  |
| 6 | "Sichern" wählen | Wählen Sie Sichern. | Der Änderungsstamm wird angelegt. |  |

### Produktionsstückliste anlegen

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
| 2 | SAP-Fiori-App aufrufen | Öffnen Sie Stückliste pflegen (Version 2) – Stücklisten anlegen, ändern und anzeigen(F1813A). |  |  |
| 3 | Stückliste anlegen | Wählen Sie Stückliste anlegen. Geben Sie auf dem Bild Stückliste anlegen die folgenden Daten ein, und wählen Sie OK.Material: <Materialnummer des Halbfabrikats/Fertigerzeugnisses>Änderungsnummer: <Ihre Änderungsnummer, die Sie im vorherigen Schritt angelegt haben>Werk: <Ihr Werk>Stücklistenverwendung: 1 (nur für Fertigung) |  |  |
| 4 | Komponentendaten hinzufügen | Wählen Sie im Abschnitt Komponenten das Symbol Hinzufügen, um eine oder mehrere Komponenten hinzuzufügen.Positionstyp Ptp: <L für Lagerposition>Komponente: <Materialnummer, Rohstoff/Halbfabrikat>Menge: <Menge>KompMengenEinheit: ST | Die Komponentendaten werden hinzugefügt. |  |
| 5 | Nichtlager für Stücklisten-Positionstypen erfassen ('N') | Wählen Sie im Abschnitt Komponenten das Symbol Hinzufügen, um eine oder mehrere Komponenten hinzuzufügen.Positionstyp Ptp: <N für Nichtlagerposition>Komponente: <Materialnummer, Rohstoff/Halbfabrikat>Komponentenmenge: <Menge>KompMengenEinheit: STWählen Sie Enter, um die Felder Komponente und Komponentenmengezu aktivieren.Hinweis Dieser Positionstyp wird für Komponenten verwendet, die nicht auf Lager gehalten werden. Nichtlagerpositionen können mit oder ohne Stammdatensatz in die Stückliste eingegeben werden. | Komponentendaten für Nichtlagerpositionen werden hinzugefügt. |  |
| 6 | Rohmaß für Stücklisten-Positionstypen erfassen ('R') | Wählen Sie im Abschnitt Komponenten das Symbol Hinzufügen, um eine oder mehrere Komponenten hinzuzufügen.Positionstyp Ptp: <R für Rohmaßposition>Komponente: <Materialnummer, Rohstoff/Halbfabrikat>Wählen Sie den Pfeil, um die Seite Details zu öffnen.Nehmen Sie für Rohteildaten die erforderlichen Einträge vor.Rohmaß 1: <Geben Sie die Abmessungen der Rohmaßpositionen ein>Rohmaß 2: <Geben Sie die Abmessungen der Rohmaßpositionen ein>Rohmaß 3: <Geben Sie die Abmessungen der Rohmaßpositionen ein>Rohmaßeinheit: <Geben Sie die Maßeinheit für die Menge einer Rohmaßposition ein>Formelschlüssel: <Geben Sie die Formel zur Berechnung der Rohmaßposition ein>Anzahl der Rohmaßpositionen: <Menge>Rohteilmenge: <Eine für die Rohmaßpositionen berechnete Menge>Wählen Sie Übernehmen.Hinweis Mit diesem Positionstyp können Sie unterschiedlich große Abschnitte einer Komponente mit einem Material festlegen, z.B. die Größe eines Blechs, das für die Reparatur einer Beplankung erforderlich ist. | Die Komponentendaten für Rohmaßpositionen werden hinzugefügt/berechnet. |  |
| 7 | Textposition für Stücklisten-Positionstypen erfassen ('T') | Geben Sie für die neue Zeile der Nummer der Stücklistenposition die folgenden Daten (oder ähnliche Daten) ein:Positionstyp: TextpositionIn der Zeile Nummer der Stücklistenposition gehen Sie folgendermaßen vor.Wählen Sie den Pfeil, um die Seite Details zu öffnen.Auf dem Bild Stückliste pflegen - Basisdetails:Komponentenmenge: 1KompMengenEinheit: STWählen Sie die Registerkarte Status/Langtext zur Anzeige des Positionstext.Positionstext: Dokumentation | Textdokumentdaten für Textpositionen werden hinzugefügt. |  |
| 8 | Kopf prüfen | Im Abschnitt Kopfattribute können Sie die Daten prüfen und bei Bedarf ändern. |  |  |
| 9 | Daten sichern | Sichern Sie Ihre Eingaben. | Die Meldung Materialstückliste wurde gesichert wird angezeigt. |  |

### Verkaufsstückliste anlegen

Testverwaltung

Kundenprojekt: Füllen Sie die projektbezogenen Teile aus.

|  |  |  |  |
| --- | --- | --- | --- |
| Testfall-ID | <X.XX> | Testdatum: |  |
| Testername: |  | Dauer: |  |
| Benutzerrolle(n): |  | Zuständigkeit: | <Geben Sie den Serviceanbieter, einen Kunden oder einen Serviceanbieter zusammen mit einem Kunden an.> |

Vorgehensweise

| Testschrittnummer | Bezeichnung des Testschritts | Anweisungen | Erwartetes Ergebnis | Kommentare |
| --- | --- | --- | --- | --- |
| 1 | Anmelden | Melden Sie sich am SAP Fiori Launchpad als Produktionsingenieur – diskrete Fertigung an. | Das SAP Fiori Launchpad wird angezeigt. |  |
| 2 | SAP-Fiori-App aufrufen | Wählen Sie Stückliste pflegen – Stücklisten anlegen, ändern und anzeigen(F1813). |  |  |
| 3 | Stückliste anlegen | Wählen Sie Stückliste anlegen. Geben Sie auf dem Bild Stückliste anlegen die folgenden Daten ein, und wählen Sie OK.Material: <Stücklisten-Kopfmaterialnummer>, z.B. SDBOMERLAHD oder SDBOMLUMFHDWerk: <Geben Sie Ihr Werk ein.>Änderungsnummer: <Ihre Änderungsnummer, die Sie im vorherigen Schritt angelegt haben>Stücklistenverwendung: 5 |  |  |
| 4 | Komponentendaten hinzufügen | Wählen Sie im Abschnitt Komponenten das Symbol Hinzufügen, um eine oder mehrere Komponenten hinzuzufügen.Positionstyp Ptp: <L für Lagerposition>Komponente: <Materialnummer, Handelsware>Menge: <Menge> | Die Komponentendaten werden hinzugefügt. |  |
| 5 | Kopf prüfen | Im Abschnitt Kopfattribute können Sie die Daten prüfen und bei Bedarf ändern. |  |  |
| 6 | Daten sichern | Sichern Sie Ihre Eingaben. | Die Meldung "Materialstückliste wurde gesichert" wird angezeigt. |  |

## Anhang

### Folgeprozesse Arbeitsplan anlegen

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
- related-to :: [[12-production-and-manufacturing/bom-mds-bnk-625]]
- related-to :: [[12-production-and-manufacturing/crear-lista-de-materiales-para-material-para-produccion-y-ventas-mds-b]]
- related-to :: [[12-production-and-manufacturing/create-material-bom-for-production-and-sales-mds-bnk-623]]
- related-to :: [[12-production-and-manufacturing/mds-bnk-627]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/BNK_S4CLD2608_Master_Data_DE_XX.docx` — full document · extracted with `mammoth` · 16,672 chars in the whole document
