---
id: 02-business-partner-and-product-master-data/stammdatenskript-produktstamm-vom-typ-rohstoff-anlegen-sds-bnr-658
title: "Stammdatenskript: Produktstamm vom Typ „Rohstoff“ anlegen – SDS (BNR) (BNR_S4CLD2608_Master_Data_DE_XX)"
description: "German SAP S/4HANA Cloud Public Edition 2608 master data test script for creating a raw material (ROH) product master via MM01 or F1602, step by step."
cluster: 02-business-partner-and-product-master-data
tags: [kb/business-partner-and-product-master-data, topic/product-master-raw-semifinished-finished]
aliases: [BNR_S4CLD2608_Master_Data_DE_XX]
keywords: ["Product Master: Raw Materials, Semi-Finished and Finished…", material master, basic data, purchasing data, mrp planning data, storage location data, accounting valuation data, configurable products, product attachments, plant sales data]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/BNR_S4CLD2608_Master_Data_DE_XX.docx]
confidence: low
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-658
topic: 02-business-partner-and-product-master-data/product-master-raw-semifinished-finished
language: DE
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Stammdatenskript: Produktstamm vom Typ „Rohstoff“ anlegen – SDS (BNR) (BNR_S4CLD2608_Master_Data_DE_XX)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/BNR_S4CLD2608_Master_Data_DE_XX.docx`, extracted with `mammoth`. Grouped under **Product Master: Raw Materials, Semi-Finished and Finished Goods** in Business Partner and Product Master Data. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

| <!-- image omitted: unnamed --> | StammdatenskriptSAP S/4HANA Cloud Public Edition - 02-07-26 |
| --- | --- |
|  | Produktstamm vom Typ „Rohstoff“ anlegen – SDS (BNR) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Inhaltsverzeichnis

[1 Zweck 2](#_Toc233890025)

[2 Voraussetzungen 3](#_Toc233890026)

[2.1 Systemzugriff 3](#_Toc233890027)

[2.2 Rollen 3](#_Toc233890028)

[2.3 Erforderliche Organisationseinheiten 3](#_Toc233890029)

[2.4 Obligatorische und optionale Stammdaten 4](#_Toc233890030)

[2.5 Wesentliche Parameter für die Datenerstellung 5](#_Toc233890031)

[2.5.1 Materialart und Nummernkreise 5](#_Toc233890032)

[2.5.2 Branche 5](#_Toc233890033)

[3 Übersichtstabelle 6](#_Toc233890034)

[4 Testverfahren 7](#_Toc233890035)

[4.1 Materialstammdaten anlegen - Grunddaten 7](#_Toc233890036)

[4.2 Materialstammdaten anlegen – Einkaufsdaten 10](#_Toc233890037)

[4.3 Materialstammdaten anlegen - Dispositions-/Planungsdaten (Werksdaten) 12](#_Toc233890038)

[4.4 Materialstammdaten anlegen - Lagerortdaten 16](#_Toc233890039)

[4.5 Materialstammdaten anlegen – Buchhaltungsdaten (Bewertungsbereichsdaten) 19](#_Toc233890040)

[4.6 Produktstammdaten anlegen – Konfigurierbares Produkt und Varianten 22](#_Toc233890041)

[4.7 Produktstammdaten anlegen – Anlagen sichern 25](#_Toc233890042)

[4.8 Produktstammdaten anlegen – Werksverkauf/Allgemeine Daten 27](#_Toc233890043)

[4.9 Produktstammdaten anlegen – Werk/Serienfertigung 30](#_Toc233890044)

## Zweck

Der Material- oder Produktstamm enthält Informationen über alle physischen Materialien, die beschafft, gefertigt, gelagert und verkauft werden. Er wird auch verwendet, um Informationen über Dienstleistungen zu verwalten, zum Beispiel für den Einkauf und Verkauf von Dienstleistungen in Stunden.

Der Materialstamm enthält Informationen wie die eindeutige Materialnummer, Name, Materialart, Mengeneinheit, Beschreibungen, Gewicht und Abmessungen. Diese Materialinformationen werden in Transaktionen wie Kundenaufträgen, Lieferungen, Bestellungen und Warenbewegungen verwendet und gespeichert.

Da alle Informationen für ein Material zentral gespeichert werden, sind die Materialstamminformationen in verschiedenen Ansichten organisiert. Zum Beispiel Verkauf, Lagerung, Materialbedarfsplanung, Kalkulation und Abrechnung.

Einige Informationen zu den einzelnen Materialien sind spezifisch für bestimmte Organisationseinheiten. Eine Verkaufsbeschreibung ist zum Beispiel spezifisch für eine Verkaufseinheit (Verkaufsbereich), ein Disponent ist spezifisch für einen spezifischen Standort (Werk) und einige Informationen können spezifisch für einen Lagerort sein.

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
| Stammdatenexperte – Produktdaten | SAP_BR_PRODMASTER_SPECIALIST | Stammdaten – Produkte / Produkt-Governance | SAP_BR_PRODMASTER_SPECIALIST / SAP_CMD_SPT_PR_GOV_PC |  |

### Erforderliche Organisationseinheiten

Einige Segmente von Materialstammdaten hängen von den Organisationseinheiten des Unternehmens ab. Allgemeine (zentrale) Daten hängen nicht von einer Organisationseinheit oder dem Buchungskreis ab. Die folgende Tabelle stellt eine Übersicht dieser verschiedenen Datensegmente und ihrer relevanten Organisationseinheiten bereit:

| Datensegment | Hängt ab von | Feldbeispiele | Kommentare | Zu verwendende Organisationseinheit |
| --- | --- | --- | --- | --- |
| Grunddaten | Unabhängig von Organisationeinheiten | Materialbeschreibung (Kurztext), Materialnummer, Materialgruppe, Basismengeneinheit usw. | Gunddaten existieren für einen Materialstammsatz nur einmal. | Nicht zutreffend |
| Einkaufsdaten | Werk | Einkäufergruppe, Materialgruppe, WE-Bearbeitungszeit usw. | Einkaufsdaten können für jede Einkaufsorganisation existieren, für die das Material in Einkaufsvorgängen verwendet werden soll. | Werk:__________ |
| Dispositions-/Planungsdaten | Werk, Lagerort | Dispositionsmerkmal, Disponent, Losgröße, Planlieferzeit usw. | Werksdaten können für jede Werks-ID Ihrer Unternehmensstruktur existieren, für die der Materialstammsatz verwendet wird.Lagerortdaten (Planungskontext) sind optional, abhängig von der Notwendigkeit, eine lagerortspezifische Planung durchzuführen. | Werk:____________Lagerort:__________ |
| Lagerortdaten | Werk, Lagerort | Anzahl WE-Scheine, Max. Lagerungszeit, Mindestrest- laufzeit usw. | Werksdaten können für jede Werks-ID Ihrer Unternehmensstruktur existieren, für die der Materialstammsatz verwendet wird.Lagerortdaten (Planungskontext) sind optional, abhängig von der Notwendigkeit, eine lagerortspezifische Planung durchzuführen. | Werk:____________Lagerort:__________ |
| Buchhaltungsdaten | Bewertungsbereich (= Werk), Bewertungsart | Bewertungsklasse, Per. VPreis, Preissteuerung usw. | Daten zum Bewertungsbereich können für jede Werks-ID Ihrer Unternehmensstruktur existieren, für die der Materialstammsatz verwendet wird. Jedes Werk stellt einen Bewertungsbereich dar (z.B. unterschiedliche Bewertungspreise eines Materials in verschiedenen Werken) | Werk:____________Bewertungsart:__________ |

### Obligatorische und optionale Stammdaten

Materialstammdatensätze können auf andere Stammdaten verweisen. Die folgende Tabelle bietet eine Übersicht über die optionalen und obligatorischen Stammdatenobjekte, die in einem Materialstammdatensatz verwendet werden müssen.

|  |
| --- |
| Hinweis Für eine ordnungsgemäße Steuerberechnung sind brasilienspezifische Felder erforderlich.Prüfen Sie Nota Fiscal – Brasilien - JD0 im Kapitel BR-spezifische Felder für Stammdaten definieren für Materialstammdaten. |

| Stammdatenobjekt | Verwendet im Datensegment | Obligatorisch / optional | Kommentare |
| --- | --- | --- | --- |
|  |  | Optional |  |
|  |  | Obligatorisch |  |

### Wesentliche Parameter für die Datenerstellung

In diesem Abschnitt werden einige Basisparameter erläutert, die das Verhalten eines Stammsatzes beeinflussen und zum Anlegen eines Materialstammdatensatzes immer erforderlich sind:

#### Materialart und Nummernkreise

Anhand von Materialarten ermittelt das System welche Datensegmente (Sichten) bearbeitet werden können oder es ermittelt welche Felder Kann- oder Mussfelder sind. Basierend auf den Materialarten ermittelt das System außerdem die Nummernkreise für Materialien. Im SAP-Standardinhalt verwenden alle Materialarten die gleiche Nummernkreisdefinition.

| Nummernkreis | Bereich / Geschäftspartner-ID | Kommentare |
| --- | --- | --- |
| Extern alphanumerisch | A – ZZZZZZZZ | Dieser Bereich muss mit einem Buchstaben beginnen. Insgesamt darf die Kennung nicht länger als 40 Zeichen sein. |
| Intern numerisch | 1 - 99999999 | Dieser Bereich wird verwendet, wenn das System einem Material automatisch eine numerische Nummer zuordnen soll. |

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
| [Materialstammdaten anlegen - Grunddaten](#unique_11) [Seite ] 7 | Stammdatenexperte – Produktdaten | Material anlegen(MM01)/Produktstammdaten verwalten(F1602) | "Grunddaten für Materialstammdaten" wird angelegt. |
| [Materialstammdaten anlegen – Einkaufsdaten](#unique_12) [Seite ] 10 | Stammdatenexperte – Produktdaten | Material anlegen(MM01)/Produktstammdaten verwalten(F1602) | "Einkaufsstammdaten" wird angelegt. |
| [Materialstammdaten anlegen - Dispositions-/Planungsdaten (Werksdaten)](#unique_13) [Seite ] 12 | Stammdatenexperte – Produktdaten | Material anlegen(MM01)/Produktstammdaten verwalten(F1602) | "Dispositionsstammdaten" wird angelegt. |
| [Materialstammdaten anlegen - Lagerortdaten](#unique_14) [Seite ] 16 | Stammdatenexperte – Produktdaten | Material anlegen(MM01)/Produktstammdaten verwalten(F1602) | "Lagerort - Stammdaten" wird angelegt. |
| [Materialstammdaten anlegen – Buchhaltungsdaten (Bewertungsbereichsdaten)](#unique_15) [Seite ] 19 | Stammdatenexperte – Produktdaten | Material anlegen(MM01)/Produktstammdaten verwalten(F1602) | "Buchhaltung - Stammdaten" wird angelegt. |
| [Produktstammdaten anlegen – Konfigurierbares Produkt und Varianten](#unique_16) [Seite ] 22 | Stammdatenexperte – Produktdaten | Material anlegen(MM01)/Produktstammdaten verwalten(F1602) oder Material ändern(MM02), falls erforderlich | Ein konfigurierbares Produkt und Varianten werden angelegt. |
| [Produktstammdaten anlegen – Anlagen sichern](#unique_17) [Seite ] 25 | Stammdatenexperte – Produktdaten | Material anlegen(MM01)/Produktstammdaten verwalten(F1602) | Anlagen zum Materialstammsatz sichern |
| [Produktstammdaten anlegen – Werksverkauf/Allgemeine Daten](#unique_18) [Seite ] 27 | Stammdatenexperte – Produktdaten | Material anlegen(MM01)/Produktstammdaten verwalten(F1602) |  |
| [Produktstammdaten anlegen – Werk/Serienfertigung](#unique_19) [Seite ] 30 | Stammdatenexperte – Produktdaten | Material anlegen(MM01)/Produktstammdaten verwalten(F1602) |  |

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

In dieser Vorgehensweise erhalten Sie eine Anleitung zum Anlegen von Materialstammdaten. Die zur Verfügung stehenden Apps hängen von der Ihnen zugeordneten Rolle ab. Aus diesem Grund sind zwei Optionen verfügbar.

Vorgehensweise: Option 1 – Material anlegen

Folgen Sie dieser Vorgehensweise, wenn Sie mit Ihrer Benutzerrolle auf die App Material anlegen(MM01) zugreifen können.

| Testschrittnummer | Bezeichnung des Testschritts | Anweisung | Erwartetes Ergebnis | Bestanden/Nicht bestanden/Anmerkung |
| --- | --- | --- | --- | --- |
| 1 | Anmelden | Melden Sie sich am SAP Fiori Launchpad mit Ihren Benutzeranmeldeinformationen an. | Das SAP Fiori Launchpad wird angezeigt.Hinweis Die Anmeldung über das Launchpad ist nur relevant, wenn das Web GUI verwendet wird. |  |
| 2 | SAP-Fiori-App aufrufen | Öffnen Sie Material anlegen(MM01). | Die App wird geöffnet. |  |
| 3 | Materialgrunddaten eingeben | Nehmen Sie auf dem Bild Material anlegen (Einstieg) die folgenden Einträge vor:Material: <Materialnummer>Branche: MHinweis Ist das Eingabefeld Branche ausgeblendet, ist keine Eingabe erforderlich. Wird die Branche nicht zur Eingabe angeboten, ist das Feld ausgegraut.Materialart: ROH (Rohstoffe)Wählen Sie Sichtenauswahl. | Das Bild Sichtenauswahl wird angezeigt. |  |
| 4 | Views auswählen | Wählen Sie auf dem Bild Sichtenauswahl die Sichten Grunddaten 1 und Grunddaten 2 aus.Wählen Sie Weiter. | Das Bild Material anlegen (Rohstoffe) wird angezeigt. |  |
| 5 | Grunddaten eingeben | Geben Sie auf dem Bild Material…(Rohstoffe) auf der Registerkarte Grunddaten 1 eine Beschreibung im Feld Beschr. ein. |  |  |
| 6 | Grunddaten eingeben | Nehmen Sie auf der Registerkarte Grunddaten 1 im Abschnitt Allgemeine Daten die folgenden Einträge vor:Basismengeneinheit: <Basismengeneinheit>Warengruppe: <Warengruppe>Allg. PosTypGrp: <Allg. PosTypGrp> |  |  |
| 7 | Grunddaten eingeben | Nehmen Sie im Bereich Dimensionen/EANs die folgenden Einträge vor:Bruttogewicht: <Bruttogewicht>Gewichtseinheit: <Gewichtseinheit>Nettogewicht: <Nettogewicht>Drücken Sie Enter. | Die Registerkarte Grunddaten 2 wird angezeigt. |  |
| 8 | Grunddaten eingeben | Auf der Registerkarte Grunddaten 2 müssen Sie keine Einträge vornehmen. | Das Bild Letztes Datenbild erreicht wird mit folgender Meldung angezeigt: Sie beenden die Bearbeitung. Möchten Sie Ihre Daten zunächst sichern? |  |
| 9 | Daten sichern | Wählen Sie auf dem Bild Letztes Datenbild erreicht die Option Ja. | Das Bild Stammdaten - Produkt wird angezeigt.Die Grunddaten werden erzeugt und gesichert. |  |

Vorgehensweise: Option 2 – Produktstammdaten verwalten

Folgen Sie dieser Vorgehensweise, wenn Sie mit Ihrer Benutzerrolle auf die App Produktstammdaten verwalten(F1602) zugreifen können.

| Testschrittnummer | Bezeichnung des Testschritts | Anweisung | Erwartetes Ergebnis | Bestanden/Nicht bestanden/Anmerkung |
| --- | --- | --- | --- | --- |
| 1 | Anmelden | Melden Sie sich am SAP Fiori Launchpad mit Ihren Benutzeranmeldeinformationen an. | Das SAP Fiori Launchpad wird angezeigt. |  |
| 2 | SAP-Fiori-App aufrufen | Wählen Sie im Katalog Produktstamm die Option Produktstammdaten verwalten(F1602). | Die App wird geöffnet. |  |
| 3 | "Anlegen" wählen | Wählen Sie auf dem Bild Produktstammdaten verwalten die Option Anlegen. | Das Bild Stammdatensatz anlegen wird angezeigt. |  |
| 4 | Pflichtfelder eingeben | Nehmen Sie auf dem Bild Stammdatensatz anlegen die folgenden Einträge vor, und wählen Sie OK:Produktnummer: z.B. Z oder eine beliebige externe alphanumerische ID. Sie muss mit einem Zeichen beginnen, oder darf keinen Eintrag enthalten, dann legt das System automatisch eine alphanumerische ID an.Hinweis Weitere Informationen zum Anlegen von Produktnummern finden Sie im vorherigen Kapitel [Materialart und Nummernkreise](#unique_8) [Seite ] 5.Produktart: ROHProduktgruppe: z.B. L002Basismengeneinheit: z.B. StückBeschreibung: <beliebige Beschreibung> |  |  |
| 5 | Zum Hauptbild zurückkehren | Kehren Sie zum Bild Produktstamm verwalten zurück. | Das Bild Produktstamm verwalten wird angezeigt. |  |
| 6 | Grunddaten eingeben | Navigieren Sie zu Produktstamm verwalten > GRUNDDATEN > Grunddaten, und geben Sie folgende Daten ein:Sparte: z.B. 00 |  |  |
| 7 | Eine Beschreibung hinzufügen | Navigieren Sie zu Produktstamm verwalten > GRUNDDATEN > Beschreibung, und wählen Sie Anlegen. | Die Beschreibung in der Standardsprache (z.B. Deutsch) wird angezeigt |  |
| 8 | Beschreibungsdaten eingeben | Geben Sie auf dem Bild Beschreibung folgende Daten ein:Sprache: z.B. DeutschProduktbeschreibung: <Produktbeschreibung> |  |  |
| 9 | Zum Hauptbild zurückkehren | Kehren Sie über das Pfeilsymbol "Zurück" zum Hauptbild zurück. | Das Bild Produktstamm wird angezeigt. |  |
| 10 | Basismengeneinheit auswählen | Navigieren Sie zu Allgemeine Daten > GRUNDDATEN, und wählen Sie Mengeneinheit. | Das Bild Mengeneinheit wird angezeigt. |  |
| 11 | Daten sichern | Wählen Sie Anlegen. | Die Systemmeldung Stammdatensatz angelegt wird angezeigt, die angibt, dass das Objekt gesichert wurde. |  |

### Materialstammdaten anlegen – Einkaufsdaten

Testverwaltung

Kundenprojekt: Füllen Sie die projektbezogenen Teile aus.

|  |  |  |  |
| --- | --- | --- | --- |
| Testfall-ID | <X.XX> | Testdatum: |  |
| Testername: |  | Dauer: |  |
| Benutzerrolle(n): |  | Zuständigkeit: | <Geben Sie den Serviceanbieter, einen Kunden oder einen Serviceanbieter zusammen mit einem Kunden an.> |

Zweck

In dieser Vorgehensweise erhalten Sie eine Anleitung zum Anlegen von Materialstammdaten. Die zur Verfügung stehenden Apps hängen von der Ihnen zugeordneten Rolle ab. Aus diesem Grund sind zwei Optionen verfügbar.

Voraussetzung

Sie haben die Grunddaten wie im vorherigen Abschnitt [Materialstammdaten anlegen - Grunddaten](#unique_11) [Seite ] 7 beschrieben eingegeben und gesichert.

Vorgehensweise: Option 1 – Material anlegen

Folgen Sie dieser Vorgehensweise, wenn Sie mit Ihrer Benutzerrolle auf die App Material anlegen(MM01) zugreifen können.

| Testschrittnummer | Bezeichnung des Testschritts | Anweisung | Erwartetes Ergebnis | Bestanden/Nicht bestanden/Anmerkung |
| --- | --- | --- | --- | --- |
| 1 | SAP-Fiori-App aufrufen | Öffnen Sie Material anlegen(MM01). | Die App wird geöffnet. |  |
| 2 | Materialgrunddaten eingeben | Nehmen Sie auf dem Bild Material anlegen (Einstieg) die folgenden Einträge vor:Material: <Materialnummer>Branche: MHinweis Ist das Eingabefeld Branche ausgeblendet, ist keine Eingabe erforderlich. Wird die Branche nicht zur Eingabe angeboten, ist das Feld ausgegraut.Materialart: ROH (Rohstoffe)Wählen Sie Sichtenauswahl. | Das Bild Sichtenauswahl wird angezeigt. |  |
| 3 | Views auswählen | Wählen Sie auf dem Bild Sichtenauswahl die Sicht Einkauf aus, und wählen Sie Weiter.Hinweis Nur für Polen: Um den PKWiU-Code einzugeben, wählen Sie auch Außenhandel - Importdaten aus, bevor Sie Weiter wählen. | Das Bild Organisationsebenen wird angezeigt. |  |
| 4 | Organisationsebenendaten eingeben | Nehmen Sie auf dem Bild Organisationsebenen im Abschnitt Organisationsebene den folgenden Eintrag vor, und wählen Sie Weiter:Werk: <Nummer des Werks> | Das Bild Material anlegen (Rohstoffe) wird angezeigt.Die Systemmeldung Das Material existiert bereits und wird erweitert wird angezeigt. |  |
| 5 | Einkaufsdaten eingeben | Nehmen Sie auf dem Bild Material ... anlegen (Rohstoffe) auf der Registerkarte Einkauf im Abschnitt Allgemeine Daten die folgenden Einträge vor:Einkäufergruppe: <Einkäufergruppennummer>Materialgruppe: z.B. L002 |  |  |
| 6 | Einkaufsdaten eingeben | Nehmen Sie im Bereich Sonstige Daten / Herstellerdaten den folgenden Eintrag vor:WE-Bearbeitungszeit: z.B. 1 | Das Bild Letztes Datenbild erreicht wird mit folgender Meldung angezeigt: Sie beenden die Bearbeitung. Möchten Sie Ihre Daten zunächst sichern? |  |
| Nur für Polen | "Außenhandel – Importdaten" eingeben | Nur für Polen: Geben Sie im Abschnitt Außenhandelsdaten die PKWiU-Codedaten ein:Steuerungscode: z.B. 24.10.32.0 | Der PKWiU-Code für Polen ist gepflegt. |  |
| 7 | Daten sichern | Wählen Sie auf dem Bild Letztes Datenbild erreicht die Option Ja. | Das Bild Stammdaten - Produkt wird angezeigt.Ihre Daten werden gesichert. |  |

Vorgehensweise: Option 2 – Produktstammdaten verwalten

Folgen Sie dieser Vorgehensweise, wenn Sie mit Ihrer Benutzerrolle auf die App Produktstammdaten verwalten(F1602) zugreifen können.

| Testschrittnummer | Bezeichnung des Testschritts | Anweisung | Erwartetes Ergebnis | Bestanden/Nicht bestanden/Anmerkung |
| --- | --- | --- | --- | --- |
| 1 | SAP-Fiori-App aufrufen | Öffnen Sie Produktstammdaten verwalten(F1602). | Die App wird geöffnet. |  |
| 2 | Produkt suchen und zur Bearbeitung öffnen | Suchen Sie nach dem zuvor angelegten Produkt, indem Sie die Produktnummer im Suchfeld Produkt eingeben.Wählen Sie Produkt (Original) aus der Liste aus. Sie gelangen daraufhin zum Bild Produkt.Wählen Sie Bearbeiten. | Das Produkt wird im Bearbeitungsmodus angezeigt (die Felder sind eingabebereit). |  |
| 3 | Einkaufsdaten auswählen | Wählen Sie auf dem Bild Produktstamm die Option Einkauf. | Das Bild Einkaufsorganisation wird angezeigt. |  |
| 4 | Kopf bearbeiten | Wählen Sie oben links im Bild Kopf bearbeiten, und geben Sie Folgendes ein:Produktgruppe: Zum Beispiel A001. | Das Bild Kopf bearbeiten wird angezeigt. |  |
| 5 | Einkaufsdaten eingeben | Geben Sie auf dem Bild Einkauf Folgendes ein:Einkaufswerteschlüssel: z.B. 1 |  |  |
| 6 | Daten sichern | Wählen Sie Sichern. | Die Systemmeldung bestätigt, dass das Objekt gesichert wurde. |  |

### Materialstammdaten anlegen - Dispositions-/Planungsdaten (Werksdaten)

Testverwaltung

Kundenprojekt: Füllen Sie die projektbezogenen Teile aus.

|  |  |  |  |
| --- | --- | --- | --- |
| Testfall-ID | <X.XX> | Testdatum: |  |
| Testername: |  | Dauer: |  |
| Benutzerrolle(n): |  | Zuständigkeit: | <Geben Sie den Serviceanbieter, einen Kunden oder einen Serviceanbieter zusammen mit einem Kunden an.> |

Zweck

In dieser Vorgehensweise erhalten Sie eine Anleitung zum Anlegen von Materialstammdaten. Die zur Verfügung stehenden Apps hängen von der Ihnen zugeordneten Rolle ab. Aus diesem Grund sind zwei Optionen verfügbar.

Voraussetzung

Sie haben die Daten für das Material wie im vorherigen Abschnitt [Materialstammdaten anlegen - Grunddaten](#unique_11) [Seite ] 7 erläutert eingetragen und die Einkaufsstammdaten gesichert.

Vorgehensweise: Option 1 – Material anlegen

Folgen Sie dieser Vorgehensweise, wenn Sie mit Ihrer Benutzerrolle auf die App Material anlegen(MM01) zugreifen können.

| Testschrittnummer | Bezeichnung des Testschritts | Anweisung | Erwartetes Ergebnis | Bestanden/Nicht bestanden/Anmerkung |
| --- | --- | --- | --- | --- |
| 1 | SAP-Fiori-App aufrufen | Öffnen Sie Material anlegen(MM01). | Die App wird geöffnet. |  |
| 2 | Materialgrunddaten eingeben | Nehmen Sie auf dem Bild Material anlegen (Einstieg) die folgenden Einträge vor:Material: <Materialnummer>Branche: MHinweis Ist das Eingabefeld Branche ausgeblendet, ist keine Eingabe erforderlich. Wird die Branche nicht zur Eingabe angeboten, ist das Feld ausgegraut.Materialart: ROH (Rohstoffe)Wählen Sie Sichtenauswahl. | Das Bild Sichtenauswahl wird angezeigt. |  |
| 3 | Views auswählen | Wählen Sie auf dem Bild Sichtenauswahl die Sichten Disposition 1, Disposition 2, Disposition 3 und Disposition 4 aus.Wählen Sie Weiter. | Das Bild Organisationsebenen wird angezeigt. |  |
| 4 | Organisationsebenendaten eingeben | Nehmen Sie auf dem Bild Organisationsebenen im Abschnitt Organisationsebenen die folgenden Einträge vor:Werk: z.B. 1710Lagerort: Zum Beispiel 171C. | Das Bild Material anlegen (Rohstoffe) wird angezeigt. |  |
| 5 | Dispositions-/Planungsdaten eingeben | Nehmen Sie auf dem Bild Material anlegen (Rohstoffe) auf der Registerkarte Disposition 1 im Abschnitt Dispositionsverfahren die folgenden Einträge vor:Dispositionsmerkmal: z.B. PDDisponent: z.B. 001 | Die Systemmeldung Das Material existiert bereits und wird erweitert wird angezeigt. |  |
| 6 | Dispositions-/Planungsdaten eingeben | Nehmen Sie im Bereich Losgrößendaten den folgenden Eintrag vor:Losgrößenverfahren: z.B. EX | Die Registerkarte Disposition 2 wird angezeigt. |  |
| 7 | Dispositions-/Planungsdaten eingeben | Nehmen Sie auf dem Bild Material anlegen (Rohstoffe) auf der Registerkarte Disposition 2 im Abschnitt Beschaffung die folgenden Einträge vor:Beschaffungsart: z.B. FProduktionslagerortLagerort für Fremdbeschaffung |  |  |
| 8 | Dispositions-/Planungsdaten eingeben | Nehmen Sie im Bereich Terminierung die folgenden Einträge vor:Planlieferzeit: z.B. 3Wareneingang VerarbZeit : z.B. 1Horizontschlüssel: z.B. 000 | Die Registerkarte Disposition 3 wird angezeigt. |  |
| 9 | Dispositions-/Planungsdaten eingeben | Nehmen Sie auf dem Bild Material anlegen (Rohstoffe) auf der Registerkarte Disposition 3 im Abschnitt Verfügbarkeitsprüfung die folgenden Einträge vor:Verfügbarkeitsprüfung: z.B. SPSumme Repl. Vorlaufzeit: z.B. 3 | Die Registerkarte Disposition 4 wird angezeigt. |  |
| 10 | Dispositions-/Planungsdaten eingeben | Nehmen Sie auf dem Bild Material anlegen (Rohstoffe) auf der Registerkarte Disposition 4 im Abschnitt Stücklistenauflösung/Sekundärbedarfe die folgenden Einträge vor:Einzel-/Sammelbedarf: 2 | Das Bild Letztes Datenbild erreicht wird mit folgender Meldung angezeigt: Sie beenden die Bearbeitung. Möchten Sie Ihre Daten zunächst sichern? |  |
| 11 | Daten sichern | Wählen Sie auf dem Bild Letztes Datenbild erreicht die Option Ja. | Das Bild Stammdaten - Produkt wird angezeigt.Ihre Daten werden gesichert. |  |

Vorgehensweise: Option 2 – Produktstammdaten verwalten

Folgen Sie dieser Vorgehensweise, wenn Sie mit Ihrer Benutzerrolle auf die App Produktstammdaten verwalten(F1602) zugreifen können.

| Testschrittnummer | Bezeichnung des Testschritts | Anweisung | Erwartetes Ergebnis | Bestanden/Nicht bestanden/Anmerkung |
| --- | --- | --- | --- | --- |
| 1 | SAP-Fiori-App aufrufen | Öffnen Sie Produktstammdaten verwalten(F1602). | Die App wird geöffnet. |  |
| 2 | Produkt suchen und zur Bearbeitung öffnen | Suchen Sie nach dem zuvor angelegten Produkt, indem Sie die Produktnummer im Suchfeld Produkt eingeben.Wählen Sie das Produkt aus der Liste aus. Sie gelangen daraufhin zum Bild Produkt.Wählen Sie Bearbeiten. | Das Produkt wird im Bearbeitungsmodus angezeigt (die Felder sind eingabebereit). |  |
| 3 | Werke wählen | Wählen Sie auf dem Bild Produktstamm die Option WERKE. | Das Bild WERKE wird angezeigt. |  |
| 4 | "Anlegen" wählen | Wählen Sie im Abschnitt WERKE die Option Anlegen. | Das Bild Werke wird im Bearbeitungsmodus angezeigt. |  |
| 5 | Werke – Allgemeine Daten eingeben | Nehmen Sie auf dem Bild Werk - Allgemeine Informationen folgende Einträge vor:Werk: <Werksnummer>Profitcenter: z.B. YB110 oder YB111Geben Sie im Bereich Verkauf folgende Daten ein:Ladegruppe: z.B. 0001 |  |  |
| 6 | Werke – Dispositionsdaten eingeben | Geben Sie auf dem Bild Dispositionsdaten folgende Daten ein:Verfügbarkeitsprüfung: z.B. SPPlanlieferzeit: z.B. 3Wareneingangsbearbeitungszeit: z.B. 1Dispositionsmerkmal: z.B. PDDisponent: z.B. 001 |  |  |
| 7 | Werke – Losgrößendaten eingeben | Wählen Sie auf dem Bild Dispositionsdaten die Option Losgrößendaten.Geben Sie im Bildbereich Losgrößendaten folgende Daten ein:Losgrößenverfahren: z.B. EX |  |  |
| 8 | "Werke – Beschaffungsdaten" eingeben | Navigieren Sie zu Dispositionsdaten > Beschaffung, und geben Sie folgende Daten ein:Planlieferzeit: z.B. 3Wareneingangsbearbeitungszeit: z.B. 1 |  |  |
| 9 | "Werke – Prognose" auswählen | Wählen Sie auf dem Bild Produktstamm - WERKE PROGNOSE. | Das Bild Werk - PROGNOSE wird angezeigt. |  |
| 10 | Prognosedaten eingeben | Geben Sie auf dem Bild PROGNOSE folgende Daten ein:Periodenart: z.B. M. |  |  |
| 11 | Zum Hauptbild zurückkehren | Wählen Sie Übernehmen. | Das Bild Produktstamm verwalten wird angezeigt. |  |
| 12 | Daten sichern | Wählen Sie Sichern. | Die Systemmeldung bestätigt, dass das Objekt gesichert wurde. |  |

### Materialstammdaten anlegen - Lagerortdaten

Testverwaltung

Kundenprojekt: Füllen Sie die projektbezogenen Teile aus.

|  |  |  |  |
| --- | --- | --- | --- |
| Testfall-ID | <X.XX> | Testdatum: |  |
| Testername: |  | Dauer: |  |
| Benutzerrolle(n): |  | Zuständigkeit: | <Geben Sie den Serviceanbieter, einen Kunden oder einen Serviceanbieter zusammen mit einem Kunden an.> |

Zweck

In dieser Vorgehensweise erhalten Sie eine Anleitung zum Anlegen von Materialstammdaten. Die zur Verfügung stehenden Apps hängen von der Ihnen zugeordneten Rolle ab. Aus diesem Grund sind zwei Optionen verfügbar.

Voraussetzung

Sie haben die Daten für das Material wie im vorherigen Abschnitt [Materialstammdaten anlegen - Grunddaten](#unique_11) [Seite ] 7 erläutert eingetragen und die Dispositions- und Planungsdaten gesichert.

Vorgehensweise: Option 1 – Material anlegen

Folgen Sie dieser Vorgehensweise, wenn Sie mit Ihrer Benutzerrolle auf die App Material anlegen(MM01) zugreifen können.

| Testschrittnummer | Bezeichnung des Testschritts | Anweisung | Erwartetes Ergebnis | Bestanden/Nicht bestanden/Anmerkung |
| --- | --- | --- | --- | --- |
| 1 | SAP-Fiori-App aufrufen | Öffnen Sie Material anlegen(MM01). | Die App wird geöffnet. |  |
| 2 | Materialgrunddaten eingeben | Nehmen Sie auf dem Bild Material anlegen (Einstieg) die folgenden Einträge vor:Material: <Materialnummer>Branche: MHinweis Ist das Eingabefeld Branche ausgeblendet, ist keine Eingabe erforderlich. Wird die Branche nicht zur Eingabe angeboten, ist das Feld ausgegraut.Materialart: ROH (Rohstoffe)Wählen Sie Sichtenauswahl. | Das Bild Sichtenauswahl wird angezeigt. |  |
| 3 | Views auswählen | Wählen Sie auf dem Bild Sichtenauswahl die folgenden Sichten aus, und wählen Sie Weiter:Allg. Werksdaten / Lagerung 1Allg. Werksdaten / Lagerung 2 |  |  |
| 4 | Organisationsebenendaten eingeben | Wählen Sie im oberen Bildbereich die Option Organisationsebenen.Nehmen Sie auf dem Bild Organisationsebenen im Abschnitt Organisationsebenen die folgenden Einträge vor:Werk: <Nummer des Werks>Lagerort: <Lagerortnummer> | Das Bild Material anlegen (Rohstoffe) wird angezeigt.Die Systemmeldung Das Material existiert bereits und wird erweitert wird angezeigt. |  |
| 5 | Lagerortdaten eingeben | Nehmen Sie auf dem Bild Material anlegen (Rohstoffe) auf der Registerkarte Werksdaten/Lagerung 1 im Abschnitt Allgemeine Daten folgenden Eintrag vor:Anzahl WE-Scheine: z.B. 1Drücken Sie auf Enter, um zum nächsten Bild zu wechseln. | Die Registerkarte Werksdaten/Lagerung2 wird angezeigt. |  |
| 6 | Eingaben bestätigen | Nehmen Sie auf der Registerkarte Werksdaten/Lagerung 2 im Bereich Allgemeine Werksparameter folgende Einträge vor:Profitcenter: <Profitcenter>Serialnummernprof.: <Serialnummernprofil>Wählen Sie ein gültiges Serialnummernprofil, das mit dem richtigen Equipmenttyp für Ihr Unternehmen zugeordnet wurde. | Das Letzte erreichte Datenbild wird mit folgender Meldung angezeigt: Sie beenden die Bearbeitung. Möchten Sie Ihre Daten zunächst sichern? |  |
| 7 | Daten sichern | Wählen Sie auf dem Bild Letztes Datenbild erreicht die Option Ja. | Das Bild Stammdaten - Produkt wird angezeigt.Ihre Daten werden gesichert. |  |

Vorgehensweise: Option 2 – Produktstammdaten verwalten

Folgen Sie dieser Vorgehensweise, wenn Sie mit Ihrer Benutzerrolle auf die App Produktstammdaten verwalten(F1602) zugreifen können.

| Testschrittnummer | Bezeichnung des Testschritts | Anweisung | Erwartetes Ergebnis | Bestanden/Nicht bestanden/Anmerkung |
| --- | --- | --- | --- | --- |
| 1 | SAP-Fiori-App aufrufen | Öffnen Sie Produktstammdaten verwalten(F1602). | Die App wird geöffnet. |  |
| 2 | Produkt suchen und zur Bearbeitung öffnen | Suchen Sie nach dem zuvor angelegten Produkt, indem Sie die Produktnummer im Suchfeld Produkt eingeben.Wählen Sie das Produkt aus der Liste aus. Sie gelangen daraufhin zum Bild Produkt.Wählen Sie Bearbeiten. | Das Produkt wird im Bearbeitungsmodus angezeigt (die Felder sind eingabebereit). |  |
| 3 | Werke wählen | Wählen Sie auf dem Bild Produktstamm verwalten die Option WERKE.Hinweis Ein Werksdatensatz muss bereits angelegt worden sein. Wenn kein Werksdatensatz vorhanden ist, führen Sie die Schritte des vorherigen vorherigen Abschnitts [Materialstammdaten anlegen - Dispositions-/Planungsdaten (Werksdaten)](#unique_13) [Seite ] 12 aus. | Das Bild WERKE wird angezeigt. |  |
| 4 | Werksdaten auswählen | Wählen Sie auf dem Bild Produktstamm - WERKE das Pfeilsymbol für die Werksdaten aus, die Sie im vorherigen Abschnitt [Materialstammdaten anlegen - Dispositions-/Planungsdaten (Werksdaten)](#unique_13) [Seite ] 12 angelegt haben. | Das Bild Produktstamm – Werk wird angezeigt. |  |
| 5 | Zum Werk: Lagerort | Navigieren Sie auf dem Bild Produktstamm – WERKE zu WERKE > LAGERORT. | Das Bild Produktstamm – WERKE wird im Änderungsmodus angezeigt. |  |
| 6 | "Anlegen" wählen | Wechseln Sie zu WERKE > LAGERORT > Lagerort, und wählen Sie Anlegen. | Das Bild Werk - Lagerort wird im Änderungsmodus geöffnet. |  |
| 7 | Werk eingeben: Lagerortdaten | Geben Sie auf dem Bild Lagerort Folgendes ein:Lagerort: <Lagerortnummer> | Das Bild Neuer Datensatz - Lagerort wird angezeigt. |  |
| 8 | Zum Hauptbild zurückkehren | Wählen Sie zweimal Übernehmen, um zum Bild Produkt zurückzukehren. | Das Bild Produktstamm verwalten wird angezeigt. |  |
| 9 | Daten sichern | Wählen Sie Sichern. | Die Systemmeldung bestätigt, dass das Objekt gesichert wurde. |  |

### Materialstammdaten anlegen – Buchhaltungsdaten (Bewertungsbereichsdaten)

Testverwaltung

Kundenprojekt: Füllen Sie die projektbezogenen Teile aus.

|  |  |  |  |
| --- | --- | --- | --- |
| Testfall-ID | <X.XX> | Testdatum: |  |
| Testername: |  | Dauer: |  |
| Benutzerrolle(n): |  | Zuständigkeit: | <Geben Sie den Serviceanbieter, einen Kunden oder einen Serviceanbieter zusammen mit einem Kunden an.> |

Zweck

In dieser Vorgehensweise erhalten Sie eine Anleitung zum Anlegen von Materialstammdaten. Die zur Verfügung stehenden Apps hängen von der Ihnen zugeordneten Rolle ab. Aus diesem Grund sind zwei Optionen verfügbar.

Voraussetzung

Sie haben die Daten für das Material wie im vorherigen Abschnitt [Materialstammdaten anlegen - Grunddaten](#unique_11) [Seite ] 7 erläutert eingetragen und die Lagerortdaten gesichert.

Vorgehensweise: Option 1 – Material anlegen

Folgen Sie dieser Vorgehensweise, wenn Sie mit Ihrer Benutzerrolle auf die App Material anlegen(MM01) zugreifen können.

| Testschrittnummer | Bezeichnung des Testschritts | Anweisung | Erwartetes Ergebnis | Bestanden/Nicht bestanden/Anmerkung |
| --- | --- | --- | --- | --- |
| 1 | SAP-Fiori-App aufrufen | Öffnen Sie Material anlegen(MM01). | Die App wird geöffnet. |  |
| 2 | Materialgrunddaten eingeben | Nehmen Sie auf dem Bild Material anlegen (Einstieg) die folgenden Einträge vor:Material: <Materialnummer>Branche: MHinweis Ist das Eingabefeld Branche ausgeblendet, ist keine Eingabe erforderlich. Wird die Branche nicht zur Eingabe angeboten, ist das Feld ausgegraut.Materialart: ROH (Rohstoffe)Wählen Sie Sichtenauswahl. | Das Bild Sichtenauswahl wird angezeigt. |  |
| 3 | Views auswählen | Wählen Sie auf dem Bild Sichtenauswahl die folgenden Sichten aus, und wählen Sie Weiter:Buchhaltung 1Buchhaltung 2 | Das Bild Organisationsebenen wird angezeigt. |  |
| 4 | Organisationsebenendaten eingeben | Nehmen Sie auf dem Bild Organisationsebenen im Bereich Organisationsebene den folgenden Eintrag vor:Werk: <Werk> | Das Bild Material anlegen (Rohstoffe) wird angezeigt.Die Systemmeldung Das Material existiert bereits und wird erweitert wird angezeigt. |  |
| 5 | Buchhaltungsdaten eingeben | Nehmen Sie auf dem Bild Material ... anlegen (Rohstoffe) auf der Registerkarte Buchhaltung 1 im Abschnitt Allgemeine Bewertungsdaten den folgenden Eintrag vor:Bewertungsklasse: 3000 |  |  |
| 6 | Buchhaltungsdaten eingeben | Nehmen Sie im Bereich Preise und Werte die folgenden Einträge vor:Per. VPreis: z.B. 20Preissteuerung: <V> | Die Registerkarte Buchhaltung 2 wird angezeigt. |  |
| 7 | Eingaben bestätigen | Auf der Registerkarte Buchhaltung 2 müssen Sie keine Einträge vornehmen. | Das Bild Letztes Datenbild erreicht wird mit folgender Meldung angezeigt: Sie beenden die Bearbeitung. Möchten Sie Ihre Daten zunächst sichern? |  |
| 8 | Daten sichern | Wählen Sie auf dem Bild Letztes Datenbild erreicht die Option Ja. | Das Bild Stammdaten - Produkt wird angezeigt.Ihre Daten werden gesichert. |  |

Vorgehensweise: Option 2 – Produktstammdaten verwalten

Folgen Sie dieser Vorgehensweise, wenn Sie mit Ihrer Benutzerrolle auf die App Produktstammdaten verwalten(F1602) zugreifen können.

| Testschrittnummer | Bezeichnung des Testschritts | Anweisung | Erwartetes Ergebnis | Bestanden/Nicht bestanden/Anmerkung |
| --- | --- | --- | --- | --- |
| 1 | SAP-Fiori-App aufrufen | Öffnen Sie Produktstammdaten verwalten(F1602). | Die App wird geöffnet. |  |
| 2 | Produkt suchen und zur Bearbeitung öffnen | Suchen Sie nach dem zuvor angelegten Produkt, indem Sie die Produktnummer im Suchfeld Produkt eingeben.Wählen Sie das Produkt aus der Liste aus. Sie gelangen daraufhin zum Bild Produkt.Wählen Sie Bearbeiten. | Das Produkt wird im Bearbeitungsmodus angezeigt (die Felder sind eingabebereit). |  |
| 3 | Bewertungskreise auswählen | Wählen Sie auf dem Bild Produktstamm verwalten die Option BEWERTUNGSKREISE. | Das Bild BEWERTUNGSKREISE wird angezeigt. |  |
| 4 | "Anlegen" wählen | Wählen Sie auf dem Bild BEWERTUNGSKREISE die Option Anlegen. | Das Bild Neuer Datensatz - Bewertungskreis wird im Änderungsmodus angzeigt. |  |
| 5 | Bewertungskreisdaten eingeben | Geben Sie auf dem Bild BEWERTUNGSKREISE Folgendes ein:Bewertungskreis: <Bewertungskreisnummer>Preissteuerungsfindung: 2Hinweis Nur für Brasilien: Preissteuerungsfindung ist 2, wenn Preissteuerung V ist, und ist 3, wenn PreissteuerungS ist, sofern die brasilianischen Kostenrechnungsvorschriften angewandt werden.Bewertungsklasse: <Bewertungsklassennummer> |  |  |
| 6 | Aktuelle Bewertungskreisdaten eingeben | Wechseln Sie auf dem Bild Bewertung zu Bewertung > Laufende Periode, und geben Sie Folgendes ein:Standardpreis: z.B. 20Preissteuerung: z.B. S |  |  |
| 7 | Zum Hauptbild zurückkehren | Wählen Sie Übernehmen, um zum Bild Produktstamm verwalten zurückzukehren. | Das Bild Produktstamm verwalten wird angezeigt. |  |
| 8 | Daten sichern | Wählen Sie Sichern. | Die Systemmeldung bestätigt, dass das Objekt gesichert wurde. |  |

### Produktstammdaten anlegen – Konfigurierbares Produkt und Varianten

Testverwaltung

Kundenprojekt: Füllen Sie die projektbezogenen Teile aus.

|  |  |  |  |
| --- | --- | --- | --- |
| Testfall-ID | <X.XX> | Testdatum: |  |
| Testername: |  | Dauer: |  |
| Benutzerrolle(n): |  | Zuständigkeit: | <Geben Sie den Serviceanbieter, einen Kunden oder einen Serviceanbieter zusammen mit einem Kunden an.> |

Zweck

In dieser Vorgehensweise erhalten Sie eine Anleitung zum Anlegen von Produktstammdaten. Die zur Verfügung stehenden Apps hängen von der Ihnen zugeordneten Rolle ab. Aus diesem Grund sind zwei Optionen verfügbar.

Voraussetzung

Sie müssen die vorherige Vorgehensweise ([Materialstammdaten anlegen - Grunddaten](#unique_11) [Seite ] 7) abschließen, bevor Sie mit diesem Abschnitt fortfahren können.

Folgen Sie der Vorgehensweise, nachdem Sie die eingegebenen Grunddaten gesichert haben, wie im vorherigen Kapitel erläutert.

Vorgehensweise: Option 1 – Material anlegen

Folgen Sie dieser Vorgehensweise, wenn Sie mit Ihrer Benutzerrolle auf die App Material anlegen(MM01) zugreifen können.

| Testschrittnummer | Bezeichnung des Testschritts | Anweisung | Erwartetes Ergebnis | Bestanden/Nicht bestanden/Anmerkung |
| --- | --- | --- | --- | --- |
| 1 | Anmelden | Melden Sie sich am SAP Fiori Launchpad mit Ihren Benutzeranmeldeinformationen an. | Das SAP Fiori Launchpad wird angezeigt.Hinweis Die Anmeldung über das Launchpad ist nur relevant, wenn das Web GUI verwendet wird. |  |
| 2 | SAP-Fiori-App aufrufen | Öffnen Sie Material anlegen(MM01). | Die App wird geöffnet. |  |
| 3 | Materialgrunddaten eingeben | Nehmen Sie auf dem Bild Material anlegen (Einstieg) die folgenden Einträge vor:Material: <Materialnummer>Branche: MHinweis Ist das Eingabefeld Branche ausgeblendet, ist keine Eingabe erforderlich. Wird die Branche nicht zur Eingabe angeboten, ist das Feld ausgegraut.Materialart: ROH (Rohstoffe)Wählen Sie Sichtenauswahl. | Das Bild Sichtenauswahl wird angezeigt. |  |
| 4 | Views auswählen | Hinweis Wenn das Dialogfenster Klassenart angezeigt wird, wenn Sie Schritt 3 ausführen, müssen Sie zuerst die Schritte 7, 8, 9 und 10 vor Schritt 4 ausführen und dann das Material erneut in der App Material ändern(MM02) öffnen, um die Schritte 5 und 6 auszuführen.Wählen Sie auf dem Bild Sichtenauswahl die folgenden Sichten aus, und wählen Sie Weiter:Grunddaten 1Grunddaten 2Klassifizierung |  |  |
| 5 | Grunddaten eingeben | Geben Sie auf dem Bild Material (Rohstoffe) auf der Registerkarte Grunddaten 1 Folgendes ein:Materialbeschreibung (Kurztext): <Materialbeschreibung>Basismengeneinheit: <Basismengeneinheit>Drücken Sie Enter. | Die Registerkarte Grunddaten 2 wird angezeigt. |  |
| 6 | Grunddaten eingeben | Markieren Sie auf der Registerkarte Grunddaten 2 das Ankreuzfeld Konfigurierbares Material.Wählen Sie Enter. | Die Registerkarte Klassifizierung wird angezeigt, und das Dialogfenster Klassenart wird eingeblendet. |  |
| 7 | Klassenart wählen | Wählen Sie im Dialogfenster Klassenart die Klassenart 300 (Variante) aus, und wählen Sie Weiter. | Das Bild Klassifizierung wird angezeigt. |  |
| 8 | Klasse zuordnen | Ordnen Sie im Abschnitt Zuordnung eine Klasse zu, und wählen Sie Enter. | Die entsprechenden Merkmale werden unterhalb des Abschnitts Zuordnung angezeigt. |  |
| 9 | Merkmalswerte auswählen | Wählen Sie die gewünschten Werte der Merkmale aus. |  |  |
| 10 | Daten sichern | Wählen Sie Sichern. | Das konfigurierbare Material wird angelegt. |  |
| 11 | Transaktion CU41 aufrufen | Wechseln Sie zur Transaktion CU41, und geben Sie folgende Daten ein:Profilname: <Profilname>Klassenart: 300 |  |  |
| 12 | Daten sichern | Wählen Sie Sichern. | Das Konfigurationsprofil wird angelegt. |  |
| 13 | Transaktion CU42 aufrufen | Rufen Sie die Transaktion CU42 auf.Wählen Sie per Doppelklick Prof.Name > Konfigurationseinstieg > Verarbeitungsmodus: Erweiterte Variantenkonfiguration aus.Wählen Sie Sichern. | Das Profil wird angelegt. |  |
| 14 | Variante anlegen | Zum Anlegen einer Variante öffnen Sie erneut die Kachel Material anlegen(MM01) und führen die oben beschriebenen Schritte zum Anlegen eines neuen Materials mit Grunddaten 1 und Grunddaten 2 aus. |  |  |
| 15 | Variante anlegen | Wählen Sie unter Grunddaten 2 die Mandantenspezifische Konfiguration, und geben Sie unter Werksüberg.konf.Mat. das zuvor angelegte konfigurierbare Material ein. Wählen Sie Variante einstellen, und wählen Sie anschließend den gewünschten Merkmalswert zum Konfigurieren von Varianten aus. | Die Variante wird angelegt. |  |

Vorgehensweise: Option 2 – Produktstammdaten verwalten

Folgen Sie dieser Vorgehensweise, wenn Sie mit Ihrer Benutzerrolle auf die App Produktstammdaten verwalten(F1602) zugreifen können.

| Testschrittnummer | Bezeichnung des Testschritts | Anweisung | Erwartetes Ergebnis | Bestanden/Nicht bestanden/Anmerkung |
| --- | --- | --- | --- | --- |
| 1 | Anmelden | Melden Sie sich am SAP Fiori Launchpad mit Ihren Benutzeranmeldeinformationen an. | Das SAP Fiori Launchpad wird angezeigt.Hinweis Die Anmeldung über das Launchpad ist nur relevant, wenn das Web GUI verwendet wird. |  |
| 2 | SAP-Fiori-App aufrufen | Öffnen Sie Produktstammdaten verwalten(F1602). | Die App wird geöffnet. |  |
| 3 | Produkt suchen und zur Bearbeitung öffnen | Suchen Sie nach dem zuvor angelegten Produkt, indem Sie die Produktnummer im Suchfeld Produkt eingeben.Wählen Sie das Produkt aus der Liste aus. Sie gelangen daraufhin zum Bild Produkt.Wählen Sie Bearbeiten. | Das Produkt wird im Bearbeitungsmodus angezeigt (die Felder sind eingabebereit). |  |
| 4 | Produkt als konfigurierbar kennzeichnen | Wechseln Sie auf dem Bild Produkt zur Registerkarte Konfiguration, und markieren Sie das Ankreuzfeld Produkt ist konfigurierbar. |  |  |
| 5 | Variantenklasse zuordnen | Wählen Sie auf dem Bild Produkt die Registerkarte Klassifikation und anschließend Hier klicken, um eine Klasse zuzuordnen.Wählen Sie eine Klasse mit der Klassenart 300 (Variante) aus. | Die Merkmale der zugeordneten Klasse werden angezeigt. |  |
| 6 | "Merkmale" wählen | Wählen Sie für jedes Merkmal die gewünschten Merkmalswerte aus. |  |  |
| 7 | Zur Registerkarte "Varianten" wechseln | Wechseln Sie auf dem Bild Produkt zur Registerkarte Varianten, und wählen Sie Produktvarianten auswählen. | Ein Baum oder eine Tabelle mit den verschiedenen Merkmalen wird angezeigt. |  |
| 8 | Merkmale auswählen und Varianten anlegen | Wählen Sie die gewünschte Kombination von Merkmalswerten aus, und wählen Sie Übernehmen. | Die Varianten werden angelegt. |  |
| 9 | Sichern | Wählen Sie Sichern. | Eine Systemmeldung bestätigt, dass das Objekt gesichert wurde. |  |

### Produktstammdaten anlegen – Anlagen sichern

Testverwaltung

Kundenprojekt: Füllen Sie die projektbezogenen Teile aus.

|  |  |  |  |
| --- | --- | --- | --- |
| Testfall-ID | <X.XX> | Testdatum: |  |
| Testername: |  | Dauer: |  |
| Benutzerrolle(n): |  | Zuständigkeit: | <Geben Sie den Serviceanbieter, einen Kunden oder einen Serviceanbieter zusammen mit einem Kunden an.> |

Zweck

In dieser Vorgehensweise erhalten Sie eine Anleitung zum Anlegen von Produktstammdaten. Die zur Verfügung stehenden Apps hängen von der Ihnen zugeordneten Rolle ab. Aus diesem Grund sind zwei Optionen verfügbar.

Voraussetzung

Sie müssen den vorherigen Abschnitt, [Materialstammdaten anlegen - Grunddaten](#unique_11) [Seite ] 7, abschließen, bevor Sie mit dieser Vorgehensweise fortfahren.

Beginnen Sie mit dieser Vorgehensweise, nachdem Sie die eingegebenen Grunddaten gesichert haben, wie im vorherigen Abschnitt erläutert.

Vorgehensweise: Option 1 – Material anlegen

Folgen Sie dieser Vorgehensweise, wenn Sie mit Ihrer Benutzerrolle auf die App Material anlegen(MM01) zugreifen können.

| Testschrittnummer | Bezeichnung des Testschritts | Anweisung | Erwartetes Ergebnis | Bestanden/Nicht bestanden/Anmerkung |
| --- | --- | --- | --- | --- |
| 1 | SAP-Fiori-App aufrufen | Öffnen Sie Material anlegen(MM01). | Die App wird geöffnet. |  |
| 2 | Materialgrunddaten eingeben | Nehmen Sie auf dem Bild Material anlegen (Einstieg) die folgenden Einträge vor:Material: <Materialnummer>Branche: MHinweis Ist das Eingabefeld Branche ausgeblendet, ist keine Eingabe erforderlich. Wird die Branche nicht zur Eingabe angeboten, ist das Feld ausgegraut.Materialart: ROH (Rohstoffe)Wählen Sie Sichtenauswahl. | Das Bild Sichtenauswahl wird angezeigt. |  |
| 3 | Views auswählen | Wählen Sie auf dem Bild Sichtenauswahl die Sichten Grunddaten 1 und Grunddaten 2 aus.Wählen Sie Weiter. | Das Bild Material anlegen (Rohstoffe) wird angezeigt. |  |
| 4 | Dienste zum Objekt wählen | Wählen Sie Dienste zum Objekt > Anlage anlegen. | Das Bild Datei importieren wird angezeigt. |  |
| 5 | "Hochladen" wählen | Wählen Sie auf dem Bild Datei importieren die Option Hochladen. | Ein Bild für den Datei-Upload wird angezeigt. |  |
| 6 | Anlage hochladen | Wählen Sie die Datei aus, und wählen Sie Öffnen. | Die Datei wird hochgeladen. |  |
| 7 | Sichern | Wählen Sie Auswählen und dann Sichern. | Die Systemmeldung bestätigt, dass das Objekt gesichert wurde. |  |

Vorgehensweise: Option 2 – Produktstammdaten verwalten

Folgen Sie dieser Vorgehensweise, wenn Sie mit Ihrer Benutzerrolle auf die App Produktstammdaten verwalten(F1602) zugreifen können.

| Testschrittnummer | Bezeichnung des Testschritts | Anweisung | Erwartetes Ergebnis | Bestanden/Nicht bestanden/Anmerkung |
| --- | --- | --- | --- | --- |
| 1 | SAP-Fiori-App aufrufen | Öffnen Sie Produktstammdaten verwalten(F1602). | Die App wird geöffnet. |  |
| 2 | Produkt suchen und zur Bearbeitung öffnen | Suchen Sie nach dem zuvor angelegten Produkt, indem Sie die Produktnummer im Suchfeld Produkt eingeben.Wählen Sie das Produkt aus der Liste aus. Sie gelangen daraufhin zum Bild Produkt.Wählen Sie Bearbeiten. | Das Produkt wird im Bearbeitungsmodus angezeigt (die Felder sind eingabebereit). |  |
| 3 | Anlagen wählen | Wählen Sie auf dem Bild Produkt die Registerkarte Anlagen aus. | Das Bild Anlagen wird angezeigt. |  |
| 4 | "Hochladen" wählen | Wählen Sie im Abschnitt Dokumentenverwaltung die Option Hochladen. | Ein Bild für den Datei-Upload wird angezeigt. |  |
| 5 | Anlage hochladen | Wählen Sie die Datei aus, und wählen Sie Öffnen. | Die Datei wird hochgeladen. |  |
| 6 | Sichern | Wählen Sie Sichern. | Die Systemmeldung bestätigt, dass das Objekt gesichert wurde. |  |

### Produktstammdaten anlegen – Werksverkauf/Allgemeine Daten

Testverwaltung

Kundenprojekt: Füllen Sie die projektbezogenen Teile aus.

|  |  |  |  |
| --- | --- | --- | --- |
| Testfall-ID | <X.XX> | Testdatum: |  |
| Testername: |  | Dauer: |  |
| Benutzerrolle(n): |  | Zuständigkeit: | <Geben Sie den Serviceanbieter, einen Kunden oder einen Serviceanbieter zusammen mit einem Kunden an.> |

Zweck

In dieser Vorgehensweise erhalten Sie eine Anleitung zum Anlegen von Stammdaten für Material (Produkt). Die zur Verfügung stehenden Apps hängen von der Ihnen zugeordneten Rolle ab. Aus diesem Grund sind zwei Optionen verfügbar.

Voraussetzung

Sie müssen den vorherigen Abschnitt, [Materialstammdaten anlegen - Grunddaten](#unique_11) [Seite ] 7, abschließen, bevor Sie mit dieser Vorgehensweise fortfahren.

Beginnen Sie mit dieser Vorgehensweise, nachdem Sie die eingegebenen Grunddaten gesichert haben, wie im vorherigen Abschnitt erläutert.

Vorgehensweise: Option 1 – Material anlegen

Folgen Sie dieser Vorgehensweise, wenn Sie mit Ihrer Benutzerrolle auf die App Material anlegen(MM01) zugreifen können.

| Testschrittnummer | Bezeichnung des Testschritts | Anweisung | Erwartetes Ergebnis | Kommentare |
| --- | --- | --- | --- | --- |
| 1 | SAP-Fiori-App aufrufen | Öffnen Sie Material anlegen(MM01). | Die App wird geöffnet. |  |
| 2 | Materialgrunddaten eingeben | Nehmen Sie auf dem Bild Material anlegen (Einstieg) die folgenden Einträge vor:Material: <Materialnummer>Branche: MHinweis Ist das Eingabefeld Branche ausgeblendet, ist keine Eingabe erforderlich. Wird die Branche nicht zur Eingabe angeboten, ist das Feld ausgegraut.Materialart: ROH (Rohstoffe)Wählen Sie Sichtenauswahl. | Das Bild Sichtenauswahl wird angezeigt. |  |
| 3 | Views auswählen | Wählen Sie auf dem Bild Sichtenauswahl die Option Grunddaten und Verkauf: allg./Werksdaten.Wählen Sie Weiter. | Das Bild Organisationsebenen wird angezeigt. |  |
| 4 | Organisationsebenendaten eingeben | Nehmen Sie auf dem Bild Organisationsebenen im Abschnitt Organisationsebenen die folgenden Einträge vor:Werk: <Werksnummer>Verkaufsorganisation: <Verkaufsorganisationsnummer>Vertriebs weg: <Vertriebsweg> | Das Bild Material anlegen... (Rohstoffe) wird angezeigt. |  |
| 5 | Daten auf dem Bild "Grunddaten 1" eingeben | Geben Sie auf dem Bild Grunddaten 1 Folgendes ein, und drücken Sie Enter:Beschreibung: Geben Sie eine Beschreibung für das Produkt ein.Basismengeneinheit: Geben Sie die Basiseinheit ST ein, z.B. 1. |  |  |
| 6 | Auf dem Bild "Verkauf: Allgemeine/Werksdaten" Folgendes eingeben | Geben Sie im Abschnitt Versanddaten (Zeiten in Tagen) Folgendes ein:Ladegruppe: <Wählen Sie einen Wert aus der Wertehilfe aus> |  |  |
| 8 | Daten sichern | Wählen Sie Sichern. | Ihre Daten werden gesichert. |  |

Vorgehensweise: Option 2 – Produktstammdaten verwalten

Folgen Sie dieser Vorgehensweise, wenn Sie mit Ihrer Benutzerrolle auf die App Produktstammdaten verwalten(F1602) zugreifen können.

| Testschrittnummer | Bezeichnung des Testschritts | Anweisung | Erwartetes Ergebnis | Kommentare |
| --- | --- | --- | --- | --- |
| 1 | SAP-Fiori-App aufrufen | Öffnen Sie Produktstammdaten verwalten(F1602). | Die App wird geöffnet. |  |
| 2 | Produkt suchen und zur Bearbeitung öffnen | Suchen Sie nach dem zuvor angelegten Produkt, indem Sie die Produktnummer im Suchfeld Produkt eingeben.Wählen Sie das Produkt aus der Liste aus. Sie gelangen daraufhin zum Bild Produkt.Wählen Sie Bearbeiten. | Das Produkt wird im Bearbeitungsmodus angezeigt (die Felder sind eingabebereit). |  |
| 3 | Werksdaten auswählen | Wählen Sie auf dem Bild Produkt die Option Werke. | Die Registerkarte Werke wird angezeigt. |  |
| 4 | "Anlegen" wählen | Wählen Sie auf dem Bild Werke die Option Anlegen. |  |  |
| 5 | "Werke – Allgemeine Daten" eingeben | Geben Sie im Abschnitt Allgemeine Daten folgende Daten ein:Werk: <Werksnummer>, z.B. 1710, |  |  |
| 6 | Dispositionsdaten eingeben | Nehmen Sie im Abschnitt Disposition die folgende Eingabe vor:Dispositionsmerkmal: z.B. ND |  |  |
| 7 | "Werk – Verkauf" eingeben | Geben Sie im Bereich Vertrieb folgende Daten ein:Ladegruppe: <Wählen Sie einen Wert aus der Wertehilfe aus> |  |  |
| 8 | Zum Hauptbild zurückkehren | Wählen Sie Übernehmen, um zum Bild Produkt zurückzukehren. | Das Bild Produkt wird angezeigt. |  |
| 9 | Daten sichern | Wählen Sie Sichern. | Die Systemmeldung bestätigt, dass das Objekt gesichert wurde. |  |

### Produktstammdaten anlegen – Werk/Serienfertigung

Testverwaltung

Kundenprojekt: Füllen Sie die projektbezogenen Teile aus.

|  |  |  |  |
| --- | --- | --- | --- |
| Testfall-ID | <X.XX> | Testdatum: |  |
| Testername: |  | Dauer: |  |
| Benutzerrolle(n): |  | Zuständigkeit: | <Geben Sie den Serviceanbieter, einen Kunden oder einen Serviceanbieter zusammen mit einem Kunden an.> |

Zweck

In dieser Vorgehensweise erhalten Sie eine Anleitung zum Anlegen von Stammdaten für Material (Produkt). Die zur Verfügung stehenden Apps hängen von der Ihnen zugeordneten Rolle ab. Aus diesem Grund sind zwei Optionen verfügbar.

Voraussetzung

Sie müssen den vorherigen Abschnitt, [Materialstammdaten anlegen - Grunddaten](#unique_11) [Seite ] 7, abschließen, bevor Sie mit dieser Vorgehensweise fortfahren.

Beginnen Sie mit dieser Vorgehensweise, nachdem Sie die eingegebenen Grunddaten gesichert haben, wie im vorherigen Abschnitt erläutert.

Vorgehensweise: Option 1 – Material anlegen

Folgen Sie dieser Vorgehensweise, wenn Sie mit Ihrer Benutzerrolle auf die App Material anlegen(MM01) zugreifen können.

| Testschrittnummer | Bezeichnung des Testschritts | Anweisung | Erwartetes Ergebnis | Kommentare |
| --- | --- | --- | --- | --- |
| 1 | SAP-Fiori-App aufrufen | Öffnen Sie Material anlegen(MM01). | Die App wird geöffnet. |  |
| 2 | Materialgrunddaten eingeben | Nehmen Sie auf dem Bild Material anlegen (Einstieg) die folgenden Einträge vor:Material: <Materialnummer>Branche: MHinweis Ist das Eingabefeld Branche ausgeblendet, ist keine Eingabe erforderlich. Wird die Branche nicht zur Eingabe angeboten, ist das Feld ausgegraut.Materialart: ROH (Rohstoffe)Wählen Sie Sichtenauswahl. | Das Bild Sichtenauswahl wird angezeigt. |  |
| 3 | Views auswählen | Wählen Sie auf dem Bild Sichtenauswahl die Sichten Grunddaten 1, Disposition 1 und Disposition 4 aus.Wählen Sie Weiter. | Das Bild Organisationsebenen wird angezeigt. |  |
| 4 | Organisationsebenendaten eingeben | Nehmen Sie auf dem Bild Organisationsebenen im Abschnitt Organisationsebenen die folgenden Einträge vor:Werk: <Werksnummer>Lagerort: <Lagerortnummer> | Das Bild Material anlegen... (Rohstoffe) wird angezeigt. |  |
| 5 | Daten auf dem Bild "Grunddaten 1" eingeben | Geben Sie auf dem Bild Grunddaten 1 Folgendes ein, und drücken Sie Enter:Beschreibung: Geben Sie eine Beschreibung für das Produkt ein.Basismengeneinheit: Geben Sie die Basiseinheit ST ein, z.B. 1. |  |  |
| 6 | Daten auf dem Bild "Disposition 1" eingeben | Nehmen Sie im Abschnitt Dispositionsverfahren die folgende Eingabe vor:Dispositionsmerkmal: z.B. ND |  |  |
| 7 | Daten auf dem Bild "Disposition 4" eingeben | Geben Sie im Abschnitt Serienfertigung/Montage/Deployment-Strategie folgende Daten ein:Serienfertigung: Markieren Sie das Ankreuzfeld.Serienfertigungsprofil: <Wählen Sie einen Wert aus der Wertehilfe aus> |  |  |
| 8 | Daten sichern | Wählen Sie Sichern. | Ihre Daten werden gesichert. |  |

Vorgehensweise: Option 2 – Produktstammdaten verwalten

Folgen Sie dieser Vorgehensweise, wenn Sie mit Ihrer Benutzerrolle auf die App Produktstammdaten verwalten(F1602) zugreifen können.

| Testschrittnummer | Bezeichnung des Testschritts | Anweisung | Erwartetes Ergebnis | Kommentare |
| --- | --- | --- | --- | --- |
| 1 | SAP-Fiori-App aufrufen | Öffnen Sie Produktstammdaten verwalten(F1602). | Die App wird geöffnet. |  |
| 2 | Produkt suchen und zur Bearbeitung öffnen | Suchen Sie nach dem zuvor angelegten Produkt, indem Sie die Produktnummer im Suchfeld Produkt eingeben.Wählen Sie das Produkt aus der Liste aus. Sie gelangen daraufhin zum Bild Produkt.Wählen Sie Bearbeiten. | Das Produkt wird im Bearbeitungsmodus angezeigt (die Felder sind eingabebereit). |  |
| 3 | Werksdaten auswählen | Wählen Sie auf dem Bild Produkt die Option Werke. | Die Registerkarte Werke wird angezeigt. |  |
| 4 | Hinzufügen (+) wählen | Wählen Sie im Bild Werke die Option Hinzufügen (+). |  |  |
| 5 | "Werke – Allgemeine Daten" eingeben | Geben Sie im Abschnitt Allgemeine Daten folgende Daten ein:Werk: <Werksnummer>, z.B. 1710, |  |  |
| 6 | Dispositionsdaten eingeben | Nehmen Sie im Abschnitt Disposition die folgende Eingabe vor:Dispositionsmerkmal: z.B. ND |  |  |
| 7 | Serienfertigungsdaten eingeben | Geben Sie im Abschnitt Serienfertigung Folgendes ein:Serienfertigung aktiviert: Markieren Sie das Ankreuzfeld, um das Feld Serienfertigungsprofil zu aktivieren.Serienfertigungsprofil: <Wählen Sie einen Wert aus der Wertehilfe aus>Hinweis Wenn Sie das Ankreuzfeld Serienfertigung aktiviert markieren, sollte das Feld Serienfertigungsprofil editierbar sein.Wenn Sie das Ankreuzfeld Serienfertigung aktiviert entmarkieren, sollte das Feld Serienfertigungsprofil schreibgeschützt sein. |  |  |
| 8 | Zum Hauptbild zurückkehren | Wählen Sie Übernehmen, um zum Bild Produkt zurückzukehren. | Das Bild Produkt wird angezeigt. |  |
| 9 | Daten sichern | Wählen Sie Sichern. | Die Systemmeldung bestätigt, dass das Objekt gesichert wurde. |  |

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

## Suspected conflicts

> [!warning] Conflict
> Flagged while digesting this document, not verified: Table of mandatory/optional master data objects is empty in extraction; the purchasing data row lists dependency on Werk while the comment mentions purchasing organization; step 7 is missing in the plant-sales Option 1 table (numbering jumps 6 to 8). Likely overlaps with other language versions/variants of the same master data script.

## Connections
- part-of :: [[_cluster]]
- related-to :: [[02-business-partner-and-product-master-data/master-data-script-create-product-master-of-type-raw-material-mds-bnr]]
- related-to :: [[02-business-partner-and-product-master-data/sap-s-4hana-cloud-public-edition-mds-bnr-661]]
- related-to :: [[02-business-partner-and-product-master-data/sap-s-4hana-cloud-public-edition-mds-bnr-663]]
- related-to :: [[02-business-partner-and-product-master-data/script-de-dados-mestre-criar-mestre-de-produtos-do-tipo-materia-prima]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/BNR_S4CLD2608_Master_Data_DE_XX.docx` — full document · extracted with `mammoth` · 60,334 chars in the whole document
