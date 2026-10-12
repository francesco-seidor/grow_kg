---
id: 02-business-partner-and-product-master-data/stammdatenskript-produktstamm-vom-typ-verpackung-anlegen-sds-3y1-388
title: "Stammdatenskript: Produktstamm vom Typ \"Verpackung\" anlegen – SDS (3Y1) (3Y1_S4CLD2608_Master_Data_DE_XX)"
description: "German SAP S/4HANA Cloud Public Edition master data script (3Y1) for creating packaging-type product masters: basic, sales and WM views via MM01/MM02/F1602."
cluster: 02-business-partner-and-product-master-data
tags: [kb/business-partner-and-product-master-data, topic/product-master-packaging]
aliases: [3Y1_S4CLD2608_Master_Data_DE_XX]
keywords: ["Product Master: Packaging and Returnable Packaging", packaging master data, material master creation, sales view data, warehouse management view, business roles, material types, number ranges, organizational units, manage product master data]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/3Y1_S4CLD2608_Master_Data_DE_XX.docx]
confidence: high
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-388
topic: 02-business-partner-and-product-master-data/product-master-packaging
language: DE
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Stammdatenskript: Produktstamm vom Typ "Verpackung" anlegen – SDS (3Y1) (3Y1_S4CLD2608_Master_Data_DE_XX)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/3Y1_S4CLD2608_Master_Data_DE_XX.docx`, extracted with `mammoth`. Grouped under **Product Master: Packaging and Returnable Packaging** in Business Partner and Product Master Data. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

| <!-- image omitted: unnamed --> | StammdatenskriptSAP S/4HANA Cloud Public Edition - 02-07-26 |
| --- | --- |
|  | Produktstamm vom Typ "Verpackung" anlegen – SDS (3Y1) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Inhaltsverzeichnis

[1 Zweck 2](#_Toc233889707)

[2 Voraussetzungen 3](#_Toc233889708)

[2.1 Systemzugriff 3](#_Toc233889709)

[2.2 Rollen 3](#_Toc233889710)

[2.3 Erforderliche Organisationseinheiten 3](#_Toc233889711)

[2.4 Obligatorische und optionale Stammdaten 4](#_Toc233889712)

[2.5 Wesentliche Parameter für die Datenerstellung 4](#_Toc233889713)

[2.5.1 Materialart und Nummernkreise 4](#_Toc233889714)

[2.5.2 Branche 5](#_Toc233889715)

[3 Übersichtstabelle 6](#_Toc233889716)

[4 Vorgehensweise 7](#_Toc233889717)

[4.1 Materialstammdaten anlegen - Grundsicht 7](#_Toc233889718)

[4.2 Materialstammdaten anlegen - Vertriebssicht 9](#_Toc233889719)

[4.3 Materialstammdaten aktualisieren - WM-Sicht 12](#_Toc233889720)

[5 Anhang 14](#_Toc233889721)

## Zweck

Dieses Stammdatenskript stellt Vorgehensweisen zum Anlegen von Packmitteln/Produktstammdaten bereit, die von den Umfangsbestandteilen der Lagerverwaltung verwendet werden.

Dieses Dokument enthält eine detaillierte Ablaufbeschreibung, anhand deren der Umfangsbestandteil nach der Lösungsaktivierung getestet werden kann; außerdem bildet es den vordefinierten Umfang der Lösung ab. Jeder Prozessschritt, Report oder Bestandteil wird in einem eigenen Abschnitt beschrieben, in dem die Interaktionen im System (Testschritte) tabellarisch dargestellt sind. Schritte, die nicht im Prozessumfang enthalten sind, aber zu Testzwecken benötigt werden, sind entsprechend gekennzeichnet. Projektspezifische Schritte sind zu ergänzen.

|  |
| --- |
| Hinweis Die Werte in diesem Testskript (Dezimalschreibweise, Datumsformate usw.) werden in US-amerikanischer Standardschreibweise dargestellt. Wenn Ihr Testsystem so eingerichtet ist, dass es eine andere Schreibweise verwendet, geben Sie die entsprechenden Werte ein. |

## Voraussetzungen

### Systemzugriff

| System | Details |
| --- | --- |
| System | Erreichbar über SAP Fiori Launchpad. Ihr Systemadministrator stellt Ihnen die URL für den Zugriff auf die verschiedenen Apps zur Verfügung, die Ihrer Rolle zugeordnet sind. |

### Rollen

Legen Sie Benutzerrollen mit den folgenden von SAP ausgelieferten Benutzerrollenvorlagen an, und ordnen Sie sie Ihren einzelnen Testbenutzern zu.

Alternativ können Sie, falls verfügbar, die folgenden von SAP ausgelieferten Bereiche verwenden. Legen Sie einen Bereich mit Seiten an, die vordefinierte grundlegende Apps enthalten, und ordnen Sie sie der Benutzerrolle zu. Anschließend ordnen Sie diese Benutzerrolle Ihren einzelnen Benutzern zu.

Weitere Informationen finden Sie unter Anwendungsrolle aus einer Vorlage anlegen in der [Product Assistance](https://help.sap.com/docs/SAP_S4HANA_CLOUD/53e36b5493804bcdb3f6f14de8b487dd/ec310a8b669a45ca898dc4dd91d97de2.html) für SAP S/4HANA Cloud Public Edition.

| Name (Rollenvorlage) | ID (Rollenvorlage) | Name (Launchpad-Bereich) | ID (Launchpad-Bereich) |
| --- | --- | --- | --- |
| Stammdatenexperte – Produktdaten | SAP_BR_PRODMASTER_SPECIALIST | Stammdaten – Produkte / Produkt-Governance | SAP_BR_PRODMASTER_SPECIALIST / SAP_CMD_SPT_PR_GOV_PC |

### Erforderliche Organisationseinheiten

Einige Segmente von Stammdaten hängen von den Organisationseinheiten des Unternehmens ab. Allgemeine (zentrale) Daten hängen nicht von einer Organisationseinheit oder dem Buchungskreis ab. Die folgende Tabelle stellt eine Übersicht dieser verschiedenen Datensegmente und ihrer relevanten Organisationseinheiten bereit:

| Datensegment | Hängt ab von | Feldbeispiele | Kommentare | Zu verwendende Organisationseinheit |
| --- | --- | --- | --- | --- |
| Grunddaten | Unabhängig von Organisationeinheiten | BasismengeneinheitWarengruppe und so weiter. |  | – |
| Verkaufsdaten | Unabhängig von Organisationeinheiten | TranspGruppe, Gruppe, Packmittelart,Zulässiges Paketgewicht,Zulässiges Paketvolumen usw. |  | – |
| WM-Daten | Unabhängig von Organisationeinheiten | Handling-Unit-TypAllgemeiner HU-Typ |  | – |

### Obligatorische und optionale Stammdaten

Stammdatensätze können auf andere Stammdaten verweisen. Die folgende Tabelle bietet eine Übersicht über die optionalen und obligatorischen Stammdatenobjekte, die in einem Verpackungsstammdatensatz verwendet werden müssen.

| Stammdatenobjekt | Verwendet im Datensegment | Obligatorisch / optional | Kommentare |
| --- | --- | --- | --- |
| Basismengeneinheit | Grunddaten | Obligatorisch |  |

|  |
| --- |
| Hinweis Für eine ordnungsgemäße Steuerberechnung sind für Brasilien spezifische Felder erforderlich. Weitere Informationen finden Sie im Kapitel BR-spezifische Felder für Stammdaten definieren im Materialstammdaten-Kapitel im Dokument Stammdaten für Brasilien anlegen (JD0_BR). |

### Wesentliche Parameter für die Datenerstellung

In diesem Abschnitt werden einige Basisparameter erläutert, die das Verhalten eines Stammsatzes beeinflussen und zum Anlegen eines Verpackungsstammdatensatzes immer erforderlich sind:

#### Materialart und Nummernkreise

Anhand von Materialarten ermittelt das System welche Datensegmente (Sichten) bearbeitet werden können oder es ermittelt welche Felder Kann- oder Mussfelder sind. Basierend auf den Materialarten ermittelt das System außerdem die Nummernkreise für Materialien. Im SAP-Standardinhalt verwenden alle Materialarten die gleiche Nummernkreisdefinition.

| Nummernkreis | Bereich/Geschäftspartner-ID | Kommentare |
| --- | --- | --- |
| Extern alphanumerisch | A - ZZZZZZZZ | Dieser Bereich muss mit einem Buchstaben beginnen. Insgesamt darf die Kennung nicht länger als 40 Zeichen sein. |
| Intern numerisch | 1-99999999 | Dieser Bereich wird verwendet, wenn das System einem Material automatisch eine numerische Nummer zuordnen soll. |

#### Branche

Der Standardinhalt stellt lediglich eine Branche M bereit.

## Übersichtstabelle

Dieser Stammdatensatz umfasst mehrere Segmente, die in der nachfolgenden Tabelle genannt sind.

|  |
| --- |
| Hinweis Wenn Ihr Systemadministrator Bereiche und Seiten auf dem SAP Fiori Launchpad aktiviert hat, enthält die Startseite nur die wesentlichen Apps, mit denen die typischen Aufgaben einer Benutzerrolle ausgeführt werden können.Alle anderen (suchbaren) Apps, die nicht auf der Startseite enthalten sind, finden Sie über die Suchleiste ([2434549](https://me.sap.com/notes/2434549)).Wenn Sie die Startseite personalisieren und versteckte Apps hinzufügen möchten, wechseln Sie in Ihr Benutzerprofil und wählen Sie App Finder. |

| Prozessschritt | Anwendungsrolle | Transaktion/App | Erwartete Ergebnisse |
| --- | --- | --- | --- |
| Materialstammdaten anlegen - Grundsicht | Stammdatenexperte – Produktdaten | Material anlegen(MM01)/Produktstammdaten verwalten(F1602) | Materialstammdaten - Grunddaten werden angelegt. |
| Materialstammdaten anlegen - Vertriebssicht | Stammdatenexperte – Produktdaten | Material anlegen(MM01)/Produktstammdaten verwalten(F1602) | Materialstammdaten – Verkaufsdaten werden angelegt.. |
| Materialstammdaten aktualisieren – WM-Sicht | Stammdatenexperte – Produktdaten | Material ändern(MM02)/Produktstammdaten verwalten(F1602) | Materialstammdaten - WM-Daten werden angelegt. |

## Vorgehensweise

Dieser Abschnitt beschreibt die Vorgehensweisen für jedes Segment oder jeden Prozessschritt, das bzw. der Teil dieses Stammsatzes ist.

### Materialstammdaten anlegen - Grundsicht

Zweck

Das Verfahren in diesem Abschnitt enthält eine Anleitung zum Anlegen von Materialstammdaten. Die zur Verfügung stehenden Apps hängen von der Ihnen zugeordneten Rolle ab. Aus diesem Grund sind zwei Optionen verfügbar.

Vorgehensweise: Option 1 – Material anlegen

Gehen Sie folgendermaßen vor, wenn Sie aufgrund Ihrer Benutzerrolle auf die App Material anlegen zugreifen können.

| Testschrittnummer | Bezeichnung des Testschritts | Anweisung | Erwartetes Ergebnis | Kommentare |
| --- | --- | --- | --- | --- |
| 1 | Anmelden | Melden Sie sich am SAP Fiori Launchpad als Stammdatenexperte – Produktdaten an. | Das SAP Fiori Launchpad wird angezeigt. |  |
| 2 | SAP-Fiori-App aufrufen | Öffnen Sie Material anlegen(MM01). | Das Bild Material anlegen (Einstieg) wird geöffnet. |  |
| 3 | Materialgrunddaten eingeben | Nehmen Sie auf dem Bild Material anlegen (Einstieg), die folgenden Einträge vor:Material: <Materialnummer>Materialart: Verpackung | Das Bild Sichtenauswahl wird angezeigt. |  |
| 4 | "Sichtenauswahl" wählen | Wählen Sie Sichtenauswahl. | Das Dialogfenster Sichtenauswahl wird angezeigt. |  |
| 5 | Sichten wählen | Im Dialogfenster Sichtenauswahl markieren Sie die Ankreuzfelder Grunddaten 1 und Grunddaten 2. Wählen Sie Weiter (Enter). | Das Bild Material anlegen <Ihre Materialnummer> (Verpackung) wird angezeigt. |  |
| 6 | Grunddaten eingeben | Geben Sie auf dem Bild Material anlegen > Ihre Materialnummer > (Verpackung) folgende Daten ein:Beschr.:<Ihre Materialbeschreibung> |  |  |
| 7 | Grunddaten eingeben | Nehmen Sie auf der Registerkarte Grunddaten 1 im Abschnitt Allgemeine Daten die folgenden Einträge vor:Basismengeneinheit:<UoM> z.B. PCAllg. PosTypGrp: VERP |  |  |
| 7 | Grunddaten eingeben | Nehmen Sie im Bereich Dimensionen/EANs die folgenden Einträge vor:Bruttogewicht: z.B. 20Gewichtseinheit: z.B. kgNettogewicht: z.B. 15Volumen: z.B. 138Volumeneinheit: z.B. CD3Wählen Sie Enter. | Wenn die Eingabe abgeschlossen ist, fahren Sie mit der Registerkarte Grunddaten 2 fort. |  |
| 8 | Grunddaten abschließen | Für die Sicht Grunddaten 2 sind keine Einträge erforderlich. |  |  |
| 9 | Daten sichern | Wählen Sie Sichern. | Die Grunddaten werden angelegt und gesichert. |  |

Vorgehensweise: Option 2 – Produktstammdaten verwalten

| Testschrittnummer | Bezeichnung des Testschritts | Anweisung | Erwartetes Ergebnis | Kommentare |
| --- | --- | --- | --- | --- |
| 1 | Anmelden | Melden Sie sich am SAP Fiori Launchpad als Stammdatenexperte – Produktdaten an. | Das SAP Fiori Launchpad wird angezeigt. |  |
| 2 | SAP-Fiori-App aufrufen | Öffnen Sie Produktstammdaten verwalten(F1602). | Das Bild Produktstammdaten verwalten(F1602) wird angezeigt. |  |
| 3 | "Neuen Produktstamm anlegen" auswählen | Wählen Sie im Bild Produktstammdaten verwalten(F1602) die Option Anlegen und dann Produkt. | Das Bild Stammdatensatz anlegen wird angezeigt. |  |
| 4 | Daten in Pflichtfelder eingeben | Nehmen Sie auf dem Bild Stammdatensatz anlegen die folgenden Einträge vor:Produktnummer: z.B. Z …Sie geben entweder eine externe alphanumerische ID ein, die mit einem alphanumerischen Zeichen beginnen muss. Wenn Sie keinen Eintrag vornehmen, vergibt das System automatisch eine numerische ID.Weitere Informationen zur Produktnummer finden Sie im vorangehenden Abschnitt über Materialart und Nummernkreise.Produktart: VERPBasismengeneinheit: z.B. StückBeschreibung: <beliebige Beschreibung>Wählen Sie OK. |  |  |
| 5 | Grunddaten eingeben | Geben Sie auf der Registerkarte Allgemeine Informationen die folgenden Daten ein:Bereich Grunddaten:Sparte: z.B. 00Wählen Sie Mehr anzeigen, und nehmen Sie folgenden Eintrag vor:Allgemeine Positionstypengruppe: VERP |  |  |
| 6 | Beschreibungsdaten eingeben | Wählen Sie im Bereich Beschreibungen die Option Anlegen, und geben Sie folgende Daten ein:Sprache: z.B. DEProduktbeschreibung: <Ihre Beschreibung> |  |  |
| 7 | Basismengeneinheit auswählen | Wählen Sie im Abschnitt Basismengeneinheit für die Eingabe von Zusatzangaben Mehr anzeigen. |  |  |
| 8 | Weitere Messdaten eingeben | Geben Sie im Abschnitt Gewicht folgende Daten ein:Bruttogewicht: zum Beispiel 20 kg.Nettogewicht: zum Beispiel 15 kg.Geben Sie im Abschnitt Volumen folgende Daten ein:Volumen: z.B. 138 CD3 |  |  |
| 9 | Daten sichern | Wählen Sie Anlegen. | Eine Systemmeldung bestätigt, dass das Objekt gesichert wurde. |  |

### Materialstammdaten anlegen - Vertriebssicht

Zweck

Das Verfahren in diesem Abschnitt enthält eine Anleitung zum Anlegen von Materialstammdaten. Die zur Verfügung stehenden Apps hängen von der Ihnen zugeordneten Rolle ab. Aus diesem Grund sind zwei Optionen verfügbar.

Voraussetzung

Sie müssen den vorangehenden Abschnitt "Materialstammdaten anlegen – Grunddaten" erst abschließen, bevor Sie mit diesem Abschnitt fortfahren können.

Beginnen Sie mit dieser Vorgehensweise, nachdem Sie die eingegebenen Grunddaten gesichert haben, wie bei der vorherigen Vorgehensweise erläutert.

|  |
| --- |
| Hinweis Aufgrund einer Performanceeinschränkung in der App "Produktstammdaten verwalten" können nicht alle Felder angezeigt und bearbeitet werden. Wenn ein Feld fehlt, wählen Sie Option 1, um ein Material anzulegen, oder fügen Sie diese Felder in der App "Produktstammdaten verwalten" über die Richtlinie in Adapting SAP Fiori UIs at Runtime - Key User Adaptation \| SAP Help Portal hinzu. |

Vorgehensweise: Option 1 – Material anlegen

| Testschrittnummer | Bezeichnung des Testschritts | Anweisung | Erwartetes Ergebnis | Kommentare |
| --- | --- | --- | --- | --- |
| 1 | SAP-Fiori-App aufrufen | Wählen Sie Material anlegen(MM01). | Material anlegen (Einstieg) wird angezeigt. |  |
| 2 | Materialgrunddaten eingeben | Nehmen Sie in Material anlegen (Einstiegssicht) die folgenden Einträge vor:Material: <Materialnummer>Branche: MHinweis Ist das Eingabefeld Branche ausgeblendet, ist keine Eingabe erforderlich. Wird die Branche nicht zur Eingabe angeboten, wird nicht bekannt im Feld eingetragen.Materialart: VerpackungWählen Sie Sichtenauswahl. | Nachdem Sie die Einträge vorgenommen haben, wird ein neues Bild Sichtenauswahl geöffnet. |  |
| 3 | Sichten wählen | Wählen Sie im Bild Sichtenauswahl die Option Vertrieb: Allg./Werksdaten aus, und wählen Sie dann Weiter.Hinweis Nur für Polen: Wählen Sie außerdem Außenhandel - Exportdaten, um die PKWiU-Klassifikationsnummer einzugeben. | Ein Bild mit Organisationsebenen wird angezeigt. |  |
| 4 | "Weiter" wählen | Auf dem Bild Organisationsebenen im Abschnitt Organisationsebene geben Sie keine Angaben für Werk, Verkaufsorganisation und Vertriebsweg ein.Wählen Sie Weiter.Im unteren Bildbereich wird folgende Information angezeigt: Das Material existiert bereits und wird erweitert.pNur für Polen: Wenn Sie Außenhandel - Exportdaten ausgewählt haben, wählen Sie Werk. |  |  |
| 5 | Verkaufsdaten eingeben | Nehmen Sie auf der Registerkarte Verkauf: Allg./Werk im Abschnitt Versanddaten (Zeiten in Tagen) folgende Einträge vor:Transp.- gruppe: 0001 |  |  |
| 6 | Packmitteldaten eingeben | Geben Sie im Bereich Packmitteldaten die folgenden Daten ein:PackmittelartZulässiges PaketgewichtÜbergewichtstoleranzZulässiges PaketvolumenÜbervolumentoleranzAbgeschlossen |  |  |
| 7 | Nur für Polen: Verkaufsdaten eingeben | Geben Sie im Abschnitt International Trade: Export die folgenden Daten ein:• Steuerungscode: z.B. 26.40.20.0 | Der PKWiU-Code für Polen ist gepflegt. |  |
| 8 | Daten sichern | Wählen Sie Sichern. | Ihre Daten werden gesichert. |  |

Vorgehensweise: Option 2 – Produktstammdaten verwalten

| Testschrittnummer | Bezeichnung des Testschritts | Anweisung | Erwartetes Ergebnis | Kommentare |
| --- | --- | --- | --- | --- |
| 1 | SAP-Fiori-App aufrufen | Öffnen Sie Produktstammdaten verwalten(F1602). | Die App Produktstammdaten verwalten(F1602) wird geöffnet, und verschiedene Suchfelder werden angezeigt. |  |
| 2 | Produkt suchen und zur Bearbeitung öffnen | Suchen Sie nach dem zuvor angelegten Produkt, indem Sie die Produktnummer im Suchfeld Produkt eingeben.Wählen Sie das Produkt aus der Liste aus. Sie gelangen daraufhin zur Sicht Produkt.Wählen Sie Bearbeiten. | Das Produkt wird im Bearbeitungsmodus angezeigt (die Felder sind eingabebereit). |  |
| 3 | Vertrieb wählen | Wählen Sie auf dem Bild Produkt die Option Vertrieb.geben Sie folgende Daten ein:Transportgruppe: 0001Zulässiges Verpackungsgewicht:Zulässiges Verpackungsvolumen: |  |  |
| 4 | Daten sichern | Wählen Sie Sichern. | Eine Systemmeldung bestätigt, dass das Objekt gesichert wurde. |  |

### Materialstammdaten aktualisieren - WM-Sicht

Zweck

Das Verfahren in diesem Abschnitt enthält eine Anleitung zum Anlegen von Materialstammdaten. Die zur Verfügung stehenden Apps hängen von der Ihnen zugeordneten Rolle ab. Aus diesem Grund sind zwei Optionen verfügbar.

Voraussetzung

Sie müssen die vorherige Vorgehensweise Materialstammdaten (Produktstammdaten) anlegen - Grunddaten erst abschließen, bevor Sie mit diesem Abschnitt fortfahren können.

Beginnen Sie mit dieser Vorgehensweise, nachdem Sie die eingegebenen Grunddaten gesichert haben, wie bei der vorherigen Vorgehensweise erläutert.

Vorgehensweise: Option 1 – Material anlegen

Gehen Sie folgendermaßen vor, wenn Sie aufgrund Ihrer Benutzerrolle auf die App Material ändern(MM02) zugreifen können.

| Testschrittnummer | Bezeichnung des Testschritts | Anweisung | Erwartetes Ergebnis | Kommentare |
| --- | --- | --- | --- | --- |
| 1 | SAP-Fiori-App aufrufen | Öffnen Sie Material ändern(MM02). | Das Bild Material anlegen (Einstieg) wird geöffnet. |  |
| 2 | Materialgrunddaten eingeben | Nehmen Sie auf dem Bild Material ändern (Einstieg) die folgenden Einträge vor:Material: <Materialnummer>Wählen Sie Sichtenauswahl. | Die Sichtenauswahl wird geöffnet. |  |
| 3 | Sichten wählen | Wählen Sie im Fenster Sichtenauswahl die folgenden Sichten aus:WM ExecutionWM PackagingWählen Sie Weiter. |  |  |
| 4 | Angaben für "WM Execution" eingeben | Geben Sie auf der Registerkarte WM Execution folgende Daten ein:Allgemeiner HU-Typ: z.B. SP1. |  |  |
| 5 | Angaben für "WM Packaging" eingeben | Geben Sie auf der Registerkarte WM Packaging folgende Daten ein:Handling-Unit-Typ: z.B. SP1. |  |  |
| 6 | Daten sichern | Wählen Sie Sichern. |  |  |

Vorgehensweise: Option 2 – Produktstammdaten verwalten

| Testschrittnummer | Bezeichnung des Testschritts | Anweisung | Erwartetes Ergebnis | Kommentare |
| --- | --- | --- | --- | --- |
| 1 | SAP-Fiori-App aufrufen | Öffnen Sie Produktstammdaten verwalten(F1602). | Die App Produktstammdaten verwalten(F1602) wird geöffnet, und verschiedene Suchfelder werden angezeigt. |  |
| 2 | Produkt suchen und zur Bearbeitung öffnen | Suchen Sie nach dem zuvor angelegten Produkt, indem Sie die Produktnummer im Suchfeld Produkt eingeben.Wählen Sie das Produkt aus der Liste aus. Sie gelangen daraufhin zur Sicht Produkt.Wählen Sie Bearbeiten. | Das Produkt wird im Bearbeitungsmodus angezeigt (die Felder sind eingabebereit). |  |
| 3 | "Execution" auswählen | Wählen Sie in der Sicht Produkt die Registerkarte Warehouse Management. |  |  |
| 4 | Angaben für "Execution" eingeben | Geben Sie im Bereich Execution folgende Daten ein:Standard-HU-Typ: z.B. SP1. |  |  |
| 5 | Angabe für "Packaging" eingeben | Geben Sie im Bereich Packaging folgende Daten ein:Handling-Unit-Typ: z.B. SP1. |  |  |
| 6 | Daten sichern | Wählen Sie Sichern. | Die Systemmeldung bestätigt, dass das Objekt gesichert wurde. |  |

## Anhang

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
- related-to :: [[02-business-partner-and-product-master-data/create-product-master-of-type-packaging-mds-3y1-389]]
- related-to :: [[02-business-partner-and-product-master-data/criar-mestre-de-produtos-do-tipo-embalagem-mds-3y1-392]]
- related-to :: [[02-business-partner-and-product-master-data/mds-3y1-391]]
- related-to :: [[02-business-partner-and-product-master-data/mds-3y1-393]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/3Y1_S4CLD2608_Master_Data_DE_XX.docx` — full document · extracted with `mammoth` · 21,508 chars in the whole document
