---
id: 02-business-partner-and-product-master-data/stammdatenskript-produktstamm-vom-typ-ersatzteile-anlegen-sds-2j7-262
title: "Stammdatenskript: Produktstamm vom Typ „Ersatzteile“ anlegen – SDS (2J7) (2J7_S4CLD2608_Master_Data_DE_XX)"
description: "German SAP S/4HANA Cloud Public Edition 2608 master data script (2J7): test steps to create a spare-parts (ERSA) material master via MM01, plus optional document linking."
cluster: 02-business-partner-and-product-master-data
tags: [kb/business-partner-and-product-master-data, topic/product-master-spare-parts]
aliases: [2J7_S4CLD2608_Master_Data_DE_XX]
keywords: ["Product Master: Spare Parts", spare parts material master, material master creation, purchasing data, mrp planning data, storage location data, accounting valuation data, document info record, document linking to material, user roles]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/2J7_S4CLD2608_Master_Data_DE_XX.docx]
confidence: high
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-262
topic: 02-business-partner-and-product-master-data/product-master-spare-parts
language: DE
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Stammdatenskript: Produktstamm vom Typ „Ersatzteile“ anlegen – SDS (2J7) (2J7_S4CLD2608_Master_Data_DE_XX)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/2J7_S4CLD2608_Master_Data_DE_XX.docx`, extracted with `mammoth`. Grouped under **Product Master: Spare Parts** in Business Partner and Product Master Data. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

| <!-- image omitted: unnamed --> | StammdatenskriptSAP S/4HANA Cloud Public Edition - 02-07-26 |
| --- | --- |
|  | Produktstamm vom Typ „Ersatzteile“ anlegen – SDS (2J7) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Inhaltsverzeichnis

[1 Zweck 2](#_Toc233889554)

[2 Voraussetzungen 3](#_Toc233889555)

[2.1 Rollen 3](#_Toc233889556)

[2.2 Erforderliche Organisationseinheiten 3](#_Toc233889557)

[2.3 Obligatorische und optionale Stammdaten 4](#_Toc233889558)

[2.4 Wesentliche Parameter für die Datenerstellung 4](#_Toc233889559)

[2.4.1 Materialart und Nummernkreise 5](#_Toc233889560)

[2.4.2 Branche 5](#_Toc233889561)

[3 Übersichtstabelle 6](#_Toc233889562)

[4 Testverfahren 7](#_Toc233889563)

[4.1 Materialstammdaten anlegen - Grunddaten 7](#_Toc233889564)

[4.2 Materialstammdaten anlegen – Einkaufsdaten 8](#_Toc233889565)

[4.3 Materialstammdaten anlegen - Dispositions-/Planungsdaten (Werksdaten) 10](#_Toc233889566)

[4.4 Materialstammdaten anlegen - Lagerortdaten 12](#_Toc233889567)

[4.5 Materialstammdaten anlegen – Buchhaltungsdaten (Bewertungsbereichsdaten) 14](#_Toc233889568)

[4.6 Dokument anlegen (optional) 16](#_Toc233889569)

[4.7 Materialstammdaten ändern – Dokument mit Materialstammdaten verknüpfen (optional) 17](#_Toc233889570)

## Zweck

Dieser Baustein legt einen Produktstammsatz für Ersatzteile an.

## Voraussetzungen

In diesem Abschnitt sind alle Voraussetzungen für den Test hinsichtlich System, Benutzer, Stammdaten, Organisationsdaten, sonstige Testdaten und Voraussetzungen zusammengefasst.

### Rollen

Legen Sie Benutzerrollen mit den folgenden von SAP ausgelieferten Benutzerrollenvorlagen an, und ordnen Sie sie Ihren einzelnen Testbenutzern zu.

Alternativ können Sie, falls verfügbar, die folgenden von SAP ausgelieferten Bereiche verwenden. Legen Sie einen Bereich mit Seiten an, die vordefinierte grundlegende Apps enthalten, und ordnen Sie sie der Benutzerrolle zu. Anschließend ordnen Sie diese Benutzerrolle Ihren einzelnen Benutzern zu.

Weitere Informationen finden Sie unter Anwendungsrolle aus einer Vorlage anlegen in der [Product Assistance](https://help.sap.com/docs/SAP_S4HANA_CLOUD/53e36b5493804bcdb3f6f14de8b487dd/ec310a8b669a45ca898dc4dd91d97de2.html) für SAP S/4HANA Cloud Public Edition.

| Name (Rollenvorlage) | ID (Rollenvorlage) | Name (Launchpad-Bereich) | ID (Launchpad-Bereich) | Anmelden |
| --- | --- | --- | --- | --- |
| Stammdatenexperte – Produktdaten | SAP_BR_PRODMASTER_SPECIALIST | Stammdaten – Produkte / Produkt-Governance | SAP_BR_PRODMASTER_SPECIALIST / SAP_CMD_SPT_PR_GOV_PC |  |
| Konstrukteur | SAP_BR_DESIGN_ENGINEER | Dokumentenverwaltung | SAP_BR_DESIGN_ENGINEER |  |

### Erforderliche Organisationseinheiten

Einige Segmente von Materialstammdaten hängen von den Organisationseinheiten des Unternehmens ab. Allgemeine (zentrale) Daten hängen nicht von einer Organisationseinheit oder dem Buchungskreis ab. Die folgende Tabelle stellt eine Übersicht dieser verschiedenen Datensegmente und ihrer relevanten Organisationseinheiten bereit:

| Datensegment | Hängt ab von | Feldbeispiele | Kommentare | Zu verwendende Organisationseinheit |
| --- | --- | --- | --- | --- |
| Grunddaten | Unabhängig von Organisationeinheiten | Materialbeschreibung (Kurztext), Materialnummer, Materialgruppe, Basismengeneinheit usw. | Gunddaten existieren für einen Materialstammsatz nur einmal. | Nicht zutreffend |
| Einkaufsdaten | Werk | Einkäufergruppe, Materialgruppe, WE-Bearbeitungszeit usw. | Einkaufsdaten können für jede Einkaufsorganisation existieren, für die das Material in Einkaufsvorgängen verwendet werden soll. | Werk:__________ |
| Dispositions-/Planungsdaten | Werk, Lagerort | Dispositionsmerkmal, Disponent, Losgröße, Planlieferzeit usw. | Werksdaten können für jede Werks-ID Ihrer Unternehmensstruktur existieren, für die der Materialstammsatz verwendet wird.Lagerortdaten (Planungskontext) sind optional, abhängig von der Notwendigkeit, eine lagerortspezifische Planung durchzuführen. | Werk:____________Lagerort:__________ |
| Lagerortdaten | Werk, Lagerort | Anzahl WE-Scheine, Max. Lagerungszeit, Mindestlaufzeit usw. |  | Werk:____________Lagerort:__________ |
| Buchhaltungsdaten | Bewertungsbereich (= Werk), Bewertungsart | Bewertungsklasse, Per. VPreis, Preissteuerung usw. | Daten zum Bewertungsbereich können für jede Werks-ID Ihrer Unternehmensstruktur existieren, für die der Materialstammsatz verwendet wird. Jedes Werk stellt einen Bewertungsbereich dar (z.B. unterschiedliche Bewertungspreise eines Materials in verschiedenen Werken) | Werk:____________Bewertungsart:__________ |

### Obligatorische und optionale Stammdaten

Materialstammdatensätze können auf andere Stammdaten verweisen. Die folgende Tabelle bietet eine Übersicht über die optionalen und obligatorischen Stammdatenobjekte, die in einem Materialstammdatensatz verwendet werden müssen.

|  |
| --- |
| Hinweis Für eine ordnungsgemäße Steuerberechnung sind brasilienspezifische Felder erforderlich.Prüfen Sie Nota Fiscal – Brasilien - JD0 im Kapitel BR-spezifische Felder für Stammdaten definieren für Materialstammdaten. |

| Stammdatenobjekt | Verwendet im Datensegment | Obligatorisch / optional | Kommentare |
| --- | --- | --- | --- |
|  |  | optional |  |
|  |  | Obligatorisch |  |

### Wesentliche Parameter für die Datenerstellung

In den nachfolgenden Themenbereichen in diesem Abschnitt werden einige Basisparameter erläutert, die das Verhalten eines Stammsatzes beeinflussen und zum Anlegen eines Materialstammdatensatzes immer erforderlich sind.

#### Materialart und Nummernkreise

Anhand von Materialarten ermittelt das System welche Datensegmente (Sichten) bearbeitet werden können oder es ermittelt welche Felder Kann- oder Mussfelder sind. Basierend auf den Materialarten ermittelt das System außerdem die Nummernkreise für Materialien. Im SAP-Standardinhalt verwenden alle Materialarten die gleiche Nummernkreisdefinition.

| Nummernkreis | Bereich/Geschäftspartner-ID | Kommentare |
| --- | --- | --- |
| Extern alphanumerisch | A – ZZZZZZZZ | Dieser Bereich muss mit einem Buchstaben beginnen. Insgesamt darf die Kennung nicht länger als 8 Zeichen sein. |
| Intern numerisch | 1–99999999 | Dieser Bereich wird verwendet, wenn das System einem Material automatisch eine numerische Nummer zuordnen soll. |

#### Branche

Der Standardinhalt stellt lediglich eine Branche M bereit.

|  |
| --- |
| Hinweis Diese ist zurzeit nur auf dem SAP-GUI sichtbar. |

## Übersichtstabelle

Dieser Umfangsbestandteil umfasst die verschiedenen Prozessschritte in der folgenden Tabelle:

|  |
| --- |
| Hinweis Wenn Ihr Systemadministrator Bereiche und Seiten auf dem SAP Fiori Launchpad aktiviert hat, enthält die Startseite nur die wesentlichen Apps, mit denen die typischen Aufgaben einer Benutzerrolle ausgeführt werden können.Alle anderen (suchbaren) Apps, die nicht auf der Startseite enthalten sind, finden Sie über die Suchleiste ([2434549](https://me.sap.com/notes/2434549)).Wenn Sie die Startseite personalisieren und versteckte Apps hinzufügen möchten, wechseln Sie in Ihr Benutzerprofil und wählen Sie App Finder. |

| Prozessschritt | Anwendungsrolle | Vorgang/App | Erwartete Ergebnisse |
| --- | --- | --- | --- |
| [Materialstammdaten anlegen - Grunddaten](#unique_10) [Seite ] 7 | Stammdatenexperte – Produktdaten | Material anlegen(MM01) | "Grunddaten für Materialstammdaten" wird angelegt. |
| [Materialstammdaten anlegen – Einkaufsdaten](#unique_11) [Seite ] 8 | Stammdatenexperte – Produktdaten | Material anlegen(MM01) | "Einkaufsstammdaten" wird angelegt. |
| [Materialstammdaten anlegen - Dispositions-/Planungsdaten (Werksdaten)](#unique_12) [Seite ] 10 | Stammdatenexperte – Produktdaten | Material anlegen(MM01) | "Dispositionsstammdaten" wird angelegt. |
| [Materialstammdaten anlegen - Lagerortdaten](#unique_13) [Seite ] 12 | Stammdatenexperte – Produktdaten | Material anlegen(MM01) | "Lagerort - Stammdaten" wird angelegt. |
| [Materialstammdaten anlegen – Buchhaltungsdaten (Bewertungsbereichsdaten)](#unique_14) [Seite ] 14 | Stammdatenexperte – Produktdaten | Material anlegen(MM01) | "Buchhaltung - Stammdaten" wird angelegt. |
| [Dokument anlegen (optional)](#unique_15) [Seite ] 16 | Konstrukteur | Belege verwalten(F2733) | Ein neuer Dokumentinfosatz wird angelegt und die Metadaten werden hinzugefügt. Dem Dokument werden Anlagen hinzugefügt. |
| [Materialstammdaten ändern – Dokument mit Materialstammdaten verknüpfen (optional)](#unique_16) [Seite ] 17 | Stammdatenexperte – Produktdaten | Material ändern(MM02) | Das im vorherigen Schritt angelegte Dokument wird mit den Materialstammdaten verknüpft. |

## Testverfahren

In diesem Abschnitt werden die Testverfahren für den jeweiligen Prozessschritt beschrieben, der zum betreffenden Umfangsbestandteil gehört.

### Materialstammdaten anlegen - Grunddaten

Testverwaltung

Kundenprojekt: Füllen Sie die projektbezogenen Teile aus.

|  |  |  |  |
| --- | --- | --- | --- |
| Testfall-ID | <X.XX> | Testdatum: |  |
| Testername: |  | Dauer: |  |
| Benutzerrolle(n): |  | Zuständigkeit: | <Geben Sie den Serviceanbieter, einen Kunden oder einen Serviceanbieter zusammen mit einem Kunden an.> |

Zweck

Das Verfahren in diesem Abschnitt enthält eine Anleitung zum Anlegen von Materialstammdaten.

Vorgehensweise

| Testschrittnummer | Bezeichnung des Testschritts | Anweisung | Erwartetes Ergebnis | Bestanden/Nicht bestanden/Anmerkung |
| --- | --- | --- | --- | --- |
| 1 | Anmelden | Melden Sie sich am SAP Fiori Launchpad als Stammdatenexperte – Produktdaten an. | Die Startseite wird angezeigt.Hinweis Die Anmeldung über das SAP Fiori Launchpad ist nur bei der Verwendung des Web-GUI relevant. |  |
| 2 | SAP-Fiori-App aufrufen | Öffnen Sie Material anlegen(MM01). | Das Bild Material anlegen (Einstieg) wird angezeigt. |  |
| 3 | Materialgrunddaten eingeben | Nehmen Sie auf dem Bild Material anlegen (Einstieg), die folgenden Einträge vor:Material: <Materialnummer>Branche: MHinweis Ist das Eingabefeld Branche ausgeblendet, ist keine Eingabe erforderlich. Wird die Branche nicht zur Eingabe angeboten, wird nicht bekannt im Feld eingetragen.Materialart: z.B. Ersatzteile ERSA | Das Bild Sichtenauswahl wird angezeigt. |  |
| 4 | Sichten wählen | Wählen Sie auf dem Bild Sichten auswählen die Sichten Grunddaten 1 und Grunddaten 2 aus, und wählen Sie Weiter. | Die Sicht Material anlegen (Ersatzteile) wird angezeigt. |  |
| 5 | Grunddaten eingeben | Geben Sie in der Sicht Material anlegen (Ersatzteile) auf der Registerkarte Grunddaten 1 die Beschreibung (Kurztext) ein. |  |  |
| 6 | Grunddaten eingeben | Nehmen Sie auf der Registerkarte Grunddaten 1 im Abschnitt Allgemeine Daten die folgenden Einträge vor:Basismengeneinheit: z.B. StückMaterialgruppe: z.B. YBPM01 |  |  |
| 7 | Daten sichern | Wählen Sie Sichern. | Die Materialnummer wird angelegt. |  |

### Materialstammdaten anlegen – Einkaufsdaten

Testverwaltung

Kundenprojekt: Füllen Sie die projektbezogenen Teile aus.

|  |  |  |  |
| --- | --- | --- | --- |
| Testfall-ID | <X.XX> | Testdatum: |  |
| Testername: |  | Dauer: |  |
| Benutzerrolle(n): |  | Zuständigkeit: | <Geben Sie den Serviceanbieter, einen Kunden oder einen Serviceanbieter zusammen mit einem Kunden an.> |

Zweck

Das Verfahren in diesem Abschnitt enthält eine Anleitung zum Anlegen von Materialstammdaten.

Voraussetzung

Sie haben die Grunddaten wie im vorherigen Abschnitt Materialstammdaten anlegen – Grunddaten beschrieben eingegeben und gesichert.

Vorgehensweise

| Testschrittnummer | Bezeichnung des Testschritts | Anweisung | Erwartetes Ergebnis | Bestanden/Nicht bestanden/Anmerkung |
| --- | --- | --- | --- | --- |
| 1 | Anmelden | Melden Sie sich am SAP Fiori Launchpad als Stammdatenexperte – Produktdaten an. | Die Startseite wird angezeigt.Hinweis Die Anmeldung über das SAP Fiori Launchpad ist nur bei der Verwendung des Web-GUI relevant. |  |
| 2 | Kachel "Material anlegen" öffnen | Wählen Sie auf dem Bild Produktstamm die App Material anlegen(MM01). | Das Bild Material anlegen (Einstieg) wird angezeigt. |  |
| 3 | Materialgrunddaten eingeben | Nehmen Sie auf dem Bild Material anlegen (Einstieg), die folgenden Einträge vor:Material: Nummer des im vorherigen Schritt angelegten MaterialsBranche: MHinweis Ist das Eingabefeld Branche ausgeblendet, ist keine Eingabe erforderlich. Wird die Branche nicht zur Eingabe angeboten, wird nicht bekannt im Feld eingetragen.Materialart: z.B. Ersatzteile ERSA | Das Bild Sichtenauswahl wird angezeigt. |  |
| 4 | Sichten wählen | Wählen Sie auf dem Bild Sichtenauswahl die Sicht Einkauf aus, und wählen Sie Weiter.Hinweis Nur für Polen: Um den PKWiU-Code eingeben zu können, müssen Sie auch International Trade: Import auswählen. | Das Bild Organisationsebenen wird angezeigt. |  |
| 5 | Organisationsebenendaten eingeben | Nehmen Sie auf dem Bild Organisationsebenen im Bereich Organisationsebenen die folgenden Einträge vor:Werk: <Nummer des Werks>Wählen Sie Weiter. | Das Bild Material anlegen (Ersatzteile) wird angezeigt.Hinweis Die folgende Systemmeldung wird unten im Bild angezeigt: Das Material existiert bereits und wird erweitert. |  |
| 6 | Einkaufsdaten eingeben | Nehmen Sie auf dem Bild Material anlegen (Ersatzteile) auf der Registerkarte Einkauf im Bereich Allgemeine Daten die folgenden Einträge vor:Einkäufergruppe: Einkäufergruppennummer |  |  |
| 7 | Einkaufsdaten eingeben | Nehmen Sie im Bereich Sonstige Daten / Herstellerdaten den folgenden Eintrag vor:WE-Bearbeitungszeit z.B. 1 |  |  |
| Nur für Polen | Verkaufsdaten eingeben | Geben Sie im Abschnitt International Trade: Export die folgenden Daten ein:Steuerungscode: z.B. 41.00.30.0Wählen Sie anschließend Sichern. | Der PKWiU-Code für Polen ist gepflegt. |  |
| 8 | Daten sichern | Wählen Sie Sichern. | Die Materialnummer wird angelegt. |  |

### Materialstammdaten anlegen - Dispositions-/Planungsdaten (Werksdaten)

Testverwaltung

Kundenprojekt: Füllen Sie die projektbezogenen Teile aus.

|  |  |  |  |
| --- | --- | --- | --- |
| Testfall-ID | <X.XX> | Testdatum: |  |
| Testername: |  | Dauer: |  |
| Benutzerrolle(n): |  | Zuständigkeit: | <Geben Sie den Serviceanbieter, einen Kunden oder einen Serviceanbieter zusammen mit einem Kunden an.> |

Zweck

Das Verfahren in diesem Abschnitt enthält eine Anleitung zum Anlegen von Materialstammdaten.

Voraussetzung

Sie haben den vorherigen Abschnitt Materialstammdaten anlegen – Grunddaten abgeschlossen und die Einkaufsstammdaten gesichert.

Vorgehensweise

| Testschrittnummer | Bezeichnung des Testschritts | Anweisung | Erwartetes Ergebnis | Bestanden/Nicht bestanden/Anmerkung |
| --- | --- | --- | --- | --- |
| 1 | Anmelden | Melden Sie sich am SAP Fiori Launchpad als Stammdatenexperte – Produktdaten an. | Die Startseite wird angezeigt.Hinweis Die Anmeldung über das SAP Fiori Launchpad ist nur bei der Verwendung des Web-GUI relevant. |  |
| 2 | SAP-Fiori-App aufrufen | Öffnen Sie Material anlegen(MM01). | Die neue Sicht Material anlegen (Einstieg) wird angezeigt. |  |
| 3 | Materialgrunddaten eingeben | Nehmen Sie in der Sicht Material anlegen (Einstiegssicht) die folgenden Einträge vor:Material: Nummer des im vorherigen Schritt angelegten MaterialsBranche: MHinweis Ist das Eingabefeld Branche ausgeblendet, ist keine Eingabe erforderlich. Wird die Branche nicht zur Eingabe angeboten, wird nicht bekannt im Feld eingetragen.Materialart: z.B. Ersatzteile ERSA | Die Sicht Sichtenauswahl wird angezeigt. |  |
| 4 | Sichten wählen | Wählen Sie in der Sicht Sichtenauswahl die Sichten MRP1, Materialbedarfsplanung 2, MRP3 und MRP4 aus und wählen Sie Weiter. | Die Sicht Organisationsebenen wird angezeigt. |  |
| 5 | Organisationsebenendaten eingeben | Nehmen Sie in der Sicht Organisationsebenen im Abschnitt Organisationsebenen die folgenden Einträge vor:Werk: <Werksnummer>Lagerort: <Lagerort> | Die Sicht Material anlegen (Ersatzteile) wird angezeigt. |  |
| 6 | Dispositions-/Planungsdaten eingeben | Nehmen Sie in der Sicht Material anlegen (Ersatzteile) auf der Registerkarte Disposition 1 im Bereich Dispositionsverfahren die folgenden Einträge vor:Dispositionsmerkmal: z.B. PDDisponent: z.B. 001 | Im unteren Sichtbereich wird die folgende Systemmeldung angezeigt: Das Material existiert bereits und wird erweitert. |  |
| 7 | Dispositions-/Planungsdaten eingeben | Nehmen Sie im Bereich Losgrößendaten den folgenden Eintrag vor:Losgrößenverfahren: z.B. EX | Sie werden zur nächsten Registerkarte Disposition 2 weitergeleitet. |  |
| 8 | Dispositions-/Planungsdaten eingeben | Nehmen Sie in der Sicht Material anlegen (Ersatzteile) auf der Registerkarte Disposition 2 im Bereich Beschaffung die folgenden Einträge vor:Beschaffungsart: z.B. FProduktions lager ort: <Standort>Lagerort für EP <Standort> |  |  |
| 9 | Dispositions-/Planungsdaten eingeben | Nehmen Sie im Bereich Terminierung die folgenden Einträge vor:Planlieferzeit: z.B. 3WE-Bearbeitungszeit z.B. 1Horizontschlüssel: z.B. 000 | Sie werden zur nächsten Registerkarte Disposition 3 weitergeleitet. |  |
| 10 | Dispositions-/Planungsdaten eingeben | Nehmen Sie in der Sicht Material anlegen (Ersatzteile) auf der Registerkarte Disposition 3 im Bereich Verfügbarkeitsprüfung die folgenden Einträge vor:Verfügbarkeitsprüfung: z.B. SPGesamtwieder- beschaffungszeit z.B. 3 | Sie werden zur nächsten Registerkarte Disposition 4 weitergeleitet. |  |
| 11 | Dispositions-/Planungsdaten eingeben | Nehmen Sie in der Sicht Material anlegen (Ersatzteile) auf der Registerkarte Disposition 4 im Bereich Stücklistenauflösung/Sekundärbedarfe die folgenden Einträge vor:Einzel/Sammel: 2 |  |  |
| 12 | Daten sichern | Wählen Sie Sichern. | Die Materialnummer wird angelegt. |  |

### Materialstammdaten anlegen - Lagerortdaten

Testverwaltung

Kundenprojekt: Füllen Sie die projektbezogenen Teile aus.

|  |  |  |  |
| --- | --- | --- | --- |
| Testfall-ID | <X.XX> | Testdatum: |  |
| Testername: |  | Dauer: |  |
| Benutzerrolle(n): |  | Zuständigkeit: | <Geben Sie den Serviceanbieter, einen Kunden oder einen Serviceanbieter zusammen mit einem Kunden an.> |

Zweck

Das Verfahren in diesem Abschnitt enthält eine Anleitung zum Anlegen von Materialstammdaten.

Voraussetzung

Sie haben die Daten für das Material ausgefüllt, wie im vorherigen Verfahren Materialstammdaten anlegen -–Grunddaten erläutert, und die MRP- und Planungsdaten eingegeben und gesichert.

Vorgehensweise

| Testschrittnummer | Bezeichnung des Testschritts | Anweisung | Erwartetes Ergebnis | Bestanden/Nicht bestanden/Anmerkung |
| --- | --- | --- | --- | --- |
| 1 | Anmelden | Melden Sie sich am SAP Fiori Launchpad als Stammdatenexperte – Produktdaten an. | Die Startseite wird angezeigt.Hinweis Die Anmeldung über das SAP Fiori Launchpad ist nur bei der Verwendung des Web-GUI relevant. |  |
| 2 | SAP-Fiori-App aufrufen | Öffnen Sie Material anlegen(MM01). | Die Sicht Material anlegen (Einstiegssicht) wird angezeigt. |  |
| 3 | Materialgrunddaten eingeben | Nehmen Sie in der Sicht Material anlegen (Einstiegssicht) die folgenden Einträge vor:Material: Nummer des im vorherigen Schritt angelegten MaterialsBranche: MHinweis Ist das Eingabefeld Branche ausgeblendet, ist keine Eingabe erforderlich. Wird die Branche nicht zur Eingabe angeboten, wird nicht bekannt im Feld eingetragen.Materialart: z.B. Ersatzteile ERSA | Die Sicht Sichtenauswahl wird angezeigt. |  |
| 4 | Sichten wählen | Wählen Sie in der Sicht Sichtenauswahl die folgenden Sichten aus, und wählen Sie Weiter:Allg. Werksdaten / Lagerung 1Allg. Werksdaten / Lagerung 2 | Die Sicht Organisationsebenen wird angezeigt. |  |
| 5 | Organisationsebenendaten eingeben | Nehmen Sie in der Sicht Organisationsebenen im Abschnitt Organisationsebenen die folgenden Einträge vor:Werk: <Nummer des Werks>Lagerort: <Lagerortnummer> | Die Sicht Material anlegen (Ersatzteile) wird angezeigt.Hinweis Die folgende Systemmeldung wird unten in der Sicht angezeigt: Das Material existiert bereits und wird erweitert. |  |
| 6 | Lagerortdaten eingeben | Nehmen Sie in der Sicht Material anlegen (Ersatzteile) auf der Registerkarte Werksdaten/Lagerung 1 im Bereich Allgemeine Daten folgende Einträge vor:Anzahl WE-Scheine: z.B. 1 | Sie werden zur nächsten Registerkarte Werksdaten/Lagerung2 weitergeleitet. |  |
| 7 | Eingaben bestätigen | Nehmen Sie auf der Registerkarte Werksdaten/Lagerung 2 im Bereich Allgemeine Werksparameter folgende Einträge vor:Profitcenter |  |  |
| 8 | Daten sichern | Wählen Sie Sichern. | Die Materialnummer wird angelegt. |  |

### Materialstammdaten anlegen – Buchhaltungsdaten (Bewertungsbereichsdaten)

Testverwaltung

Kundenprojekt: Füllen Sie die projektbezogenen Teile aus.

|  |  |  |  |
| --- | --- | --- | --- |
| Testfall-ID | <X.XX> | Testdatum: |  |
| Testername: |  | Dauer: |  |
| Benutzerrolle(n): |  | Zuständigkeit: | <Geben Sie den Serviceanbieter, einen Kunden oder einen Serviceanbieter zusammen mit einem Kunden an.> |

Zweck

Das Verfahren in diesem Abschnitt enthält eine Anleitung zum Anlegen von Materialstammdaten.

Voraussetzung

Sie haben die Daten für das Material angelegt, wie im vorherigen Verfahren Materialstammdaten anlegen – Grunddaten erläutert, und die Lagerortdaten abgeschlossen und gesichert.

Vorgehensweise

| Testschrittnummer | Bezeichnung des Testschritts | Anweisung | Erwartetes Ergebnis | Bestanden/Nicht bestanden/Anmerkung |
| --- | --- | --- | --- | --- |
| 1 | Anmelden | Melden Sie sich am SAP Fiori Launchpad als Stammdatenexperte – Produktdaten an. | Die Startseite wird angezeigt.Hinweis Die Anmeldung über das SAP Fiori Launchpad ist nur bei der Verwendung des Web-GUI relevant. |  |
| 2 | SAP-Fiori-App aufrufen | Öffnen Sie Material anlegen(MM01). | Das Bild Material anlegen (Einstieg) wird geöffnet. |  |
| 3 | Materialgrunddaten eingeben | Nehmen Sie auf dem Bild Material anlegen (Einstieg), die folgenden Einträge vor:Material: <Nummer des im vorherigen Schritt angelegten Materials>Branche: MHinweis Ist das Eingabefeld Branche ausgeblendet, ist keine Eingabe erforderlich. Wird die Branche nicht zur Eingabe angeboten, wird nicht bekannt im Feld eingetragen.Materialart: z.B. Ersatzteile ERSA | Die Sicht Sichtenauswahl wird angezeigt. |  |
| 4 | Sichten wählen | Wählen Sie in der Sichtenauswahl Folgendes aus, und wählen Sie Weiter:Buchhaltung 1Buchhaltung 2 | Die Sicht Organisationsebenen wird angezeigt. |  |
| 5 | Organisationsebenendaten eingeben | Nehmen Sie in der Sicht Organisationsebenen im Bereich Organisationsebenen die folgenden Einträge vor:Werk | Die Sicht Material anlegen (Ersatzteile) wird angezeigt.Die folgende Systemmeldung wird angezeigt: Das Material existiert bereits und wird erweitert. |  |
| 6 | Buchhaltungsdaten eingeben | Nehmen Sie in der Sicht Material anlegen (Ersatzteile) auf der Registerkarte Buchhaltung 1 im Bereich Allgemeine Bewertungsdaten den folgenden Eintrag vor:Bewertungsklasse: 3040 |  |  |
| 7 | Buchhaltungsdaten eingeben | Nehmen Sie im Bereich Preise und Werte die folgenden Einträge vor:Standardpreis: z.B. 100Preiseinheit: 1Preis- strg: Behalten Sie den Standard bei. | Die nächste Registerkarte Buchhaltung 2 wird geöffnet. |  |
| 8 | Eingaben bestätigen | Auf der Registerkarte Buchhaltung 2 nehmen Sie keine Einträge vor. |  |  |
| 9 | Daten sichern | Wählen Sie Sichern. | Die Materialnummer wird angelegt. |  |

### Dokument anlegen (optional)

Testverwaltung

Kundenprojekt: Füllen Sie die projektbezogenen Teile aus.

|  |  |  |  |
| --- | --- | --- | --- |
| Testfall-ID | <X.XX> | Testdatum: |  |
| Testername: |  | Dauer: |  |
| Benutzerrolle(n): |  | Zuständigkeit: | <Geben Sie den Serviceanbieter, einen Kunden oder einen Serviceanbieter zusammen mit einem Kunden an.> |

Zweck

Dieses Verfahren enthält eine Anleitung zum Anlegen eines Dokuments.

Vorgehensweise

| Testschrittnummer | Bezeichnung des Testschritts | Anweisung | Erwartetes Ergebnis | Bestanden/Nicht bestanden/Anmerkung |
| --- | --- | --- | --- | --- |
| 1 | Anmelden | Melden Sie sich mit Ihren Benutzeranmeldeinformationen Konstrukteur am SAP Fiori Launchpad an. | Die Startseite wird angezeigt. |  |
| 2 | SAP-Fiori-App aufrufen | Öffnen Sie Belege verwalten(F2733). | Das Bild Belege verwalten(F2733) wird angezeigt. |  |
| 3 | Neues Dokument anlegen | Wählen Sie in der Sicht Dokument verwalten die Option Anlegen, um ein neues Dokument anzulegen. | Die Sicht Dokument wird angezeigt. |  |
| 4 | Metadaten eingeben | Geben Sie in der Sicht Dokument auf der Registerkarte Allgemeine Informationen folgende Daten ein:Belegart: z.B. YBOTeildokument: z.B. 000Geben Sie auf dem Bild Dokument auf der Registerkarte Dokumentdaten folgende Daten ein:Beschreibung: z. B. <SparePartsDoc001> | Die Metadaten in der Sicht Dokument werden mit Standardwerten vorbelegt. |  |
| 5 | Anlagen in das Dokument hochladen | Wechseln Sie in der Sicht Dokument zur Registerkarte Originale, und wählen Sie die Option Hochladen, um die entsprechenden Dokumente zu durchsuchen und hochzuladen.Dateiname: z. B. <test001.jpg> | Die Dokumentenanlagen werden als abgelegt angezeigt. |  |
| 6 | Dokument sichern | Wählen Sie Anlegen, um das Dokument zu sichern. | Ein neues Dokument vom Typ "YBO" wird angelegt und gesichert.Notieren Sie sich die Dokumentnummer. |  |
| 7 | Status ändern | Wählen Sie in der Sicht Dokument die Option Bearbeiten. Setzen Sie im Bereich Dokumentdaten den Dokumentstatus auf FR (Freigegeben). |  |  |
| 8 | Dokument sichern | Wählen Sie Sichern, um das Dokument zu sichern. |  |  |

### Materialstammdaten ändern – Dokument mit Materialstammdaten verknüpfen (optional)

Testverwaltung

Kundenprojekt: Füllen Sie die projektbezogenen Teile aus.

|  |  |  |  |
| --- | --- | --- | --- |
| Testfall-ID | <X.XX> | Testdatum: |  |
| Testername: |  | Dauer: |  |
| Benutzerrolle(n): |  | Zuständigkeit: | <Geben Sie den Serviceanbieter, einen Kunden oder einen Serviceanbieter zusammen mit einem Kunden an.> |

Zweck

Das Verfahren in diesem Abschnitt enthält eine Anleitung zum Verknüpfen eines Dokuments mit den Materialstammdaten.

Voraussetzung

Sie haben die Daten für das Material angelegt, wie im vorherigen Verfahren Materialstammdaten anlegen – Grunddaten erläutert, und das optionale Verfahren Dokument anlegen abgeschlossen.

Vorgehensweise

| Testschrittnummer | Bezeichnung des Testschritts | Anweisung | Erwartetes Ergebnis | Bestanden/Nicht bestanden/Anmerkung |
| --- | --- | --- | --- | --- |
| 1 | Anmelden | Melden Sie sich am SAP Fiori Launchpad als Stammdatenexperte – Produktdaten an. | Das SAP Fiori Launchpad wird angezeigt. |  |
| 2 | SAP-Fiori-App aufrufen | Öffnen Sie Material ändern(MM02). | Es öffnet sich ein neues Fenster, das Material ändern (Einstieg) anzeigt. |  |
| 3 | Materialgrunddaten eingeben | Nehmen Sie auf dem Bild Material ändern (Einstieg), die folgenden Einträge vor:Material: <Nummer des im vorherigen Schritt angelegten Materials>Branche: MHinweis Ist das Eingabefeld Branche ausgeblendet, ist keine Eingabe erforderlich. Wird die Branche nicht zur Eingabe angeboten, wird nicht bekannt im Feld eingetragen. |  |  |
| 4 | Sichten wählen | Wählen Sie in der Sicht Material ändern (Einstieg) den Menüpunkt Sichtenauswahl in der oberen Navigationsleiste. | Die Sicht Sichtenauswahl wird angezeigt. |  |
| 5 | Sichten wählen | Wählen Sie im Fenster Sichtenauswahl die folgenden Sichten aus und wählen Sie Weiter:Grunddaten 1 | Ein neues Fenster mit der Sicht Material ändern (Ersatzteile) wird angezeigt. |  |
| 6 | Zusatzdaten öffnen | Wählen Sie in der Sicht Material ändern (Ersatzteile) die Option Zusatzdaten in der oberen Navigationsleiste. |  |  |
| 7 | Belegdaten eingeben | Wechseln Sie zur Registerkarte Dokumentdaten, und wählen Sie unter Verknüpfte Dokumente die Option Alle Versionen. Wählen Sie +, um eine neue Zeile einzufügen. Suchen Sie das Dokument, das Sie im vorherigen Schritt angelegt haben. |  |  |
| 8 | Dokumentdaten kopieren | Markieren Sie das im vorherigen Schritt angelegte Dokument, und wählen Sie Kopieren, um das Dokument in die Zeile einzufügen. |  |  |
| 9 | Daten sichern | Wählen Sie Sichern. | Die Materialnummer wird geändert. |  |

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
- related-to :: [[02-business-partner-and-product-master-data/master-data-script-create-product-master-of-type-spare-parts-mds-2j7-2]]
- related-to :: [[02-business-partner-and-product-master-data/mds-2j7-265]]
- related-to :: [[02-business-partner-and-product-master-data/mds-2j7-267]]
- related-to :: [[02-business-partner-and-product-master-data/script-de-dados-mestre-criar-mestre-de-produtos-do-tipo-pecas-de-repos]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/2J7_S4CLD2608_Master_Data_DE_XX.docx` — full document · extracted with `mammoth` · 30,667 chars in the whole document
