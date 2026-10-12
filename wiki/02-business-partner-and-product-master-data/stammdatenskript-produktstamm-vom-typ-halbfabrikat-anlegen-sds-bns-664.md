---
id: 02-business-partner-and-product-master-data/stammdatenskript-produktstamm-vom-typ-halbfabrikat-anlegen-sds-bns-664
title: "Stammdatenskript: Produktstamm vom Typ „Halbfabrikat“ anlegen – SDS (BNS) (BNS_S4CLD2608_Master_Data_DE_XX)"
description: "German SAP S/4HANA Cloud Public Edition 2608 master data test script (BNS) for creating a semi-finished (HALB) product master via MM01 or F1602, by data view."
cluster: 02-business-partner-and-product-master-data
tags: [kb/business-partner-and-product-master-data, topic/product-master-raw-semifinished-finished]
aliases: [BNS_S4CLD2608_Master_Data_DE_XX]
keywords: ["Product Master: Raw Materials, Semi-Finished and Finished…", product master, material master data, basic data, purchasing data, mrp planning data, storage location data, accounting valuation data, configurable products, product attachments]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/BNS_S4CLD2608_Master_Data_DE_XX.docx]
confidence: low
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-664
topic: 02-business-partner-and-product-master-data/product-master-raw-semifinished-finished
language: DE
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Stammdatenskript: Produktstamm vom Typ „Halbfabrikat“ anlegen – SDS (BNS) (BNS_S4CLD2608_Master_Data_DE_XX)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/BNS_S4CLD2608_Master_Data_DE_XX.docx`, extracted with `mammoth`. Grouped under **Product Master: Raw Materials, Semi-Finished and Finished Goods** in Business Partner and Product Master Data. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

| <!-- image omitted: unnamed --> | StammdatenskriptSAP S/4HANA Cloud Public Edition - 02-07-26 |
| --- | --- |
|  | Produktstamm vom Typ „Halbfabrikat“ anlegen – SDS (BNS) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Inhaltsverzeichnis

[1 Verwendungszweck 2](#_Toc233890020)

[2 Voraussetzungen 3](#_Toc233890021)

[2.1 Systemzugriff 3](#_Toc233890022)

[2.2 Rollen 3](#_Toc233890023)

[2.3 Erforderliche Organisationseinheiten 3](#_Toc233890024)

[2.4 Obligatorische und optionale Stammdaten 4](#_Toc233890025)

[2.5 Wesentliche Parameter für die Datenerstellung 5](#_Toc233890026)

[2.5.1 Materialart und Nummernkreise 5](#_Toc233890027)

[2.5.2 Branche 5](#_Toc233890028)

[3 Übersichtstabelle 6](#_Toc233890029)

[4 Testverfahren 7](#_Toc233890030)

[4.1 Produktstammdaten anlegen – Grunddaten 7](#_Toc233890031)

[4.2 Produktstammdaten anlegen – Einkaufsdaten 10](#_Toc233890032)

[4.3 Produktstammdaten anlegen - Dispositions-/Planungsdaten/Werksdaten 12](#_Toc233890033)

[4.4 Produktstammdaten anlegen - Lagerortdaten 16](#_Toc233890034)

[4.5 Produktstammdaten anlegen – Buchhaltungsdaten / Bewertungsbereichsdaten 19](#_Toc233890035)

[4.6 Produktstammdaten anlegen – Konfigurierbares Produkt und Varianten 22](#_Toc233890036)

[4.7 Produktstammdaten anlegen – Anlagen sichern 25](#_Toc233890037)

[4.8 Produktstammdaten anlegen – Werksverkauf/Allgemeine Daten 27](#_Toc233890038)

[4.9 Produktstammdaten anlegen – Werk/Serienfertigung 29](#_Toc233890039)

## Verwendungszweck

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

| Name (Rollenvorlage) | ID (Rollenvorlage) | Name (Launchpad-Bereich) | ID (Launchpad-Bereich) | Anmelden |
| --- | --- | --- | --- | --- |
| Stammdatenexperte – Produktdaten | SAP_BR_PRODMASTER_SPECIALIST | Stammdaten – Produkte / Produkt-Governance | SAP_BR_PRODMASTER_SPECIALIST / SAP_CMD_SPT_PR_GOV_PC |  |

### Erforderliche Organisationseinheiten

Einige Segmente von Materialstammdaten hängen von den Organisationseinheiten des Unternehmens ab. Allgemeine (zentrale) Daten hängen nicht von einer Organisationseinheit oder dem Buchungskreis ab. Die folgende Tabelle stellt eine Übersicht dieser verschiedenen Datensegmente und ihrer relevanten Organisationseinheiten bereit:

| Datensegment | Hängt ab von | Feldbeispiele | Kommentare | Zu verwendende Organisationseinheit |
| --- | --- | --- | --- | --- |
| Grunddaten | Unabhängig von Organisationeinheiten | Materialbeschreibung (Kurztext), Materialnummer, Materialgruppe, Basismengeneinheit usw. | Grunddaten sind für einen Materialstammsatz nur einmal vorhanden. | Nicht zutreffend |
| Einkaufsdaten | Werk | Einkäufergruppe, Materialgruppe, WE-Bearbeitungszeit usw. | Einkaufsdaten können für jede Einkaufsorganisation existieren, für die das Material in Einkaufsvorgängen verwendet werden soll. | Werk:__________ |
| Dispositionsdaten/Planungsdaten (Werksdaten) | Werk, Lagerort | Dispositionsmerkmal, Disponent, Losgröße, Planlieferzeit usw. | Werksdaten können für jede Werks-ID Ihrer Unternehmensstruktur existieren, für die der Materialstammsatz verwendet wird.Lagerortdaten (Planungskontext) sind optional, abhängig von der Notwendigkeit, eine lagerortspezifische Planung durchzuführen. | Werk:____________Lagerort:__________ |
| Lagerortdaten | Werk, Lagerort | Anzahl WE-Scheine, Max. Lagerungszeit, Mindestrestlaufzeit usw. | Werksdaten können für jede Werks-ID Ihrer Unternehmensstruktur existieren, für die der Materialstammsatz verwendet wird.Lagerortdaten (Planungskontext) sind optional, abhängig von der Notwendigkeit, eine lagerortspezifische Planung durchzuführen. | Werk:____________Lagerort:__________ |
| Buchhaltungsdaten | Bewertungsbereich (= Werk), Bewertungsart | Bewertungsklasse, Per. VPreis, Preissteuerung usw. | Daten zum Bewertungsbereich können für jede Werks-ID Ihrer Unternehmensstruktur existieren, für die der Materialstammsatz verwendet wird. Jedes Werk stellt einen Bewertungsbereich dar (z.B. unterschiedliche Bewertungspreise eines Materials in verschiedenen Werken) | Werk:____________Bewertungsart:__________ |

### Obligatorische und optionale Stammdaten

Materialstammdatensätze können auf andere Stammdaten verweisen. Die folgende Tabelle bietet eine Übersicht über die optionalen und obligatorischen Stammdatenobjekte, die in einem Materialstammdatensatz verwendet werden müssen.

|  |
| --- |
| Hinweis Für eine ordnungsgemäße Steuerberechnung sind brasilienspezifische Felder erforderlich.Prüfen Sie Nota Fiscal – Brasilien - JD0 im Kapitel BR-spezifische Felder für Stammdaten definieren für Materialstammdaten. |

| Stammdatenobjekt | Verwendet im Datensegment | Obligatorisch / optional | Kommentare |
| --- | --- | --- | --- |
| Profitcenter |  | Obligatorisch | Für einwandfreie Bewertungsprozesse ist die Zuweisung eines Profitcenters zu einem Materialstamm erforderlich. |

### Wesentliche Parameter für die Datenerstellung

In diesem Abschnitt werden einige Basisparameter erläutert, die das Verhalten eines Stammsatzes beeinflussen und zum Anlegen eines Materialstammdatensatzes immer erforderlich sind.

#### Materialart und Nummernkreise

Anhand von Materialarten ermittelt das System welche Datensegmente (Sichten) bearbeitet werden können oder es ermittelt welche Felder Kann- oder Mussfelder sind. Basierend auf den Materialarten ermittelt das System außerdem die Nummernkreise für Materialien. Im SAP-Standardinhalt verwenden alle Materialarten die gleiche Nummernkreisdefinition.

| Nummernkreis | Bereich / Geschäftspartner-ID | Kommentare |
| --- | --- | --- |
| Extern alphanumerisch | A – ZZZZZZZZ | Dieser Bereich muss mit einem Buchstaben beginnen. Insgesamt darf die Kennung nicht länger als 40 Zeichen sein. |
| Intern numerisch | 1 - 99999999 | Dieser Bereich wird verwendet, wenn das System einem Material automatisch eine numerische Nummer zuordnen soll. |

#### Branche

Der Standardinhalt stellt lediglich eine Branche M bereit. Diese ist zurzeit nur auf dem SAP GUI sichtbar.

## Übersichtstabelle

Dieser Umfangsbestandteil umfasst die verschiedenen Prozessschritte in der folgenden Tabelle:

|  |
| --- |
| Hinweis Wenn Ihr Systemadministrator Bereiche und Seiten auf dem SAP Fiori Launchpad aktiviert hat, enthält die Startseite nur die wesentlichen Apps, mit denen die typischen Aufgaben einer Benutzerrolle ausgeführt werden können.Alle anderen (suchbaren) Apps, die nicht auf der Startseite enthalten sind, finden Sie über die Suchleiste ([2434549](https://me.sap.com/notes/2434549)).Wenn Sie die Startseite personalisieren und versteckte Apps hinzufügen möchten, wechseln Sie in Ihr Benutzerprofil und wählen Sie App Finder. |

| Prozessschritt | Benutzerrolle | Transaktion | Erwartete Ergebnisse |
| --- | --- | --- | --- |
| [Produktstammdaten anlegen – Grunddaten](#unique_11) [Seite ] 7 | Stammdatenexperte – Produktdaten | Material anlegen(MM01)/Produktstammdaten verwalten(F1602) | Materialstammdaten - Grunddaten werden angelegt. |
| [Produktstammdaten anlegen – Einkaufsdaten](#unique_12) [Seite ] 10 | Stammdatenexperte – Produktdaten | Material anlegen(MM01)/Produktstammdaten verwalten(F1602) | Materialstammdaten – Einkaufsdaten (Werksdaten) werden angelegt. |
| [Produktstammdaten anlegen - Dispositions-/Planungsdaten/Werksdaten](#unique_13) [Seite ] 12 | Stammdatenexperte – Produktdaten | Material anlegen(MM01)/Produktstammdaten verwalten(F1602) | Materialstammdaten - Dispositions-/Planungsdaten werden angelegt. |
| [Produktstammdaten anlegen - Lagerortdaten](#unique_14) [Seite ] 16 | Stammdatenexperte – Produktdaten | Material anlegen(MM01)/Produktstammdaten verwalten(F1602) | Materialstammdaten - Lagerortdaten werden angelegt. |
| [Produktstammdaten anlegen – Buchhaltungsdaten / Bewertungsbereichsdaten](#unique_15) [Seite ] 19 | Stammdatenexperte – Produktdaten | Material anlegen(MM01)/Produktstammdaten verwalten(F1602) | Materialstammdaten - Buchhaltungsdaten (Bewertungsdaten) werden angelegt. |
| [Produktstammdaten anlegen – Konfigurierbares Produkt und Varianten](#unique_16) [Seite ] 22 | Stammdatenexperte – Produktdaten | Material anlegen(MM01)/Produktstammdaten verwalten(F1602) | Konfigurierbares Produkt und Varianten anlegen |
| [Produktstammdaten anlegen – Anlagen sichern](#unique_17) [Seite ] 25 | Stammdatenexperte – Produktdaten | Material anlegen(MM01)/Produktstammdaten verwalten(F1602) | Anlagen zum Materialstammsatz sichern |
| [Produktstammdaten anlegen – Werksverkauf/Allgemeine Daten](#unique_18) [Seite ] 27 | Stammdatenexperte – Produktdaten | Material anlegen(MM01)/Produktstammdaten verwalten(F1602) |  |
| [Produktstammdaten anlegen – Werk/Serienfertigung](#unique_19) [Seite ] 29 | Stammdatenexperte – Produktdaten | Material anlegen(MM01)/Produktstammdaten verwalten(F1602) |  |

## Testverfahren

In diesem Abschnitt werden die Testverfahren für den jeweiligen Prozessschritt beschrieben, der zum betreffenden Umfangsbestandteil gehört.

### Produktstammdaten anlegen – Grunddaten

Testverwaltung

Kundenprojekt: Füllen Sie die projektbezogenen Teile aus.

|  |  |  |  |
| --- | --- | --- | --- |
| Testfall-ID | <X.XX> | Testdatum: |  |
| Testername: |  | Dauer: |  |
| Benutzerrolle(n): |  | Zuständigkeit: | <Geben Sie den Serviceanbieter, einen Kunden oder einen Serviceanbieter zusammen mit einem Kunden an.> |

Zweck

In dieser Vorgehensweise erhalten Sie eine Anleitung zum Anlegen von Produktstammdaten. Die zur Verfügung stehenden Apps hängen von der Ihnen zugeordneten Rolle ab. Aus diesem Grund sind zwei Optionen verfügbar.

Vorgehensweise: Option 1 – Material anlegen

Gehen Sie folgendermaßen vor, wenn Sie aufgrund Ihrer Benutzerrolle auf die App Material anlegen(MM01) zugreifen können.

| Testschrittnummer | Bezeichnung des Testschritts | Anweisung | Erwartetes Ergebnis | Kommentare |
| --- | --- | --- | --- | --- |
| 1 | Anmelden | Melden Sie sich am SAP Fiori Launchpad als Stammdatenexperte – Produktdaten an. | Das SAP Fiori Launchpad wird angezeigt. |  |
| 2 | SAP-Fiori-App aufrufen | Öffnen Sie Material anlegen(MM01). | Material anlegen(MM01) wird angezeigt. |  |
| 3 | Materialgrunddaten eingeben | Nehmen Sie in der Sicht Material anlegen (Einstiegssicht) die folgenden Einträge vor:Material: MaterialnummerBranche: MHinweis Ist das Eingabefeld Branche ausgeblendet, ist keine Eingabe erforderlich. Wird die Branche nicht zur Eingabe angeboten, wird nicht bekannt im Feld eingetragen.Materialart: HALB (Halbfabrikat)Wählen Sie Sichtenauswahl. | Die Sicht Sichtenauswahl wird angezeigt. |  |
| 4 | Sichten wählen | Wählen Sie im Fenster Sichtenauswahl die Sichten Grunddaten 1 und Grunddaten 2 aus und wählen Sie Weiter. | Die Sicht Material anlegen (Halbfabrikat) wird angezeigt. |  |
| 5 | Grunddaten eingeben | Geben Sie in der Sicht Material... (Halbfabrikat) auf der Registerkarte Grunddaten 1 die Materialbeschreibung (Kurztext) ein. |  |  |
| 6 | Grunddaten eingeben | Nehmen Sie auf der Registerkarte Grunddaten 1 im Abschnitt Allgemeine Daten die folgenden Einträge vor:BasismengeneinheitWarengruppeAllg. PosTypGrp |  |  |
| 7 | Grunddaten eingeben | Nehmen Sie im Abschnitt Dimensionen/EAN die folgenden Einträge vor und bestätigen Sie zweimal mit Enter.BruttogewichtGewichtseinheitNettogewichtWechseln Sie zur Registerkarte Grunddaten 2. | Die Registerkarte Grunddaten 2 wird angezeigt. |  |
| 8 | Grunddaten eingeben | Auf der Registerkarte Grunddaten 2 müssen Sie keine Einträge vornehmen. Mit Enter bestätigen. | Es öffnet sich die neue Sicht Letzte Datensicht erreicht mit der Benachrichtigung Sie beenden die Bearbeitung. Möchten Sie Ihre Daten zunächst sichern? |  |
| 9 | Daten sichern | Wählen Sie in der Sicht Letztes Datenbild erreicht die Drucktaste Ja. | Die Sicht Stammdaten - Produkt wird angezeigt.Die Grunddaten werden angelegt und gesichert. |  |

Vorgehensweise: Option 2 – Produktstammdaten verwalten

Gehen Sie folgendermaßen vor, wenn Sie aufgrund Ihrer Benutzerrolle auf die App Produktstammdaten verwalten(F1602) zugreifen können.

| Testschrittnummer | Bezeichnung des Testschritts | Anweisung | Erwartetes Ergebnis | Kommentare |
| --- | --- | --- | --- | --- |
| 1 | Anmelden | Melden Sie sich am SAP Fiori Launchpad mit Ihren Benutzeranmeldeinformationen an. | Das SAP Fiori Launchpad wird angezeigt. |  |
| 2 | SAP-Fiori-App aufrufen | Öffnen Sie Produktstammdaten verwalten(F1602). | Die Sicht Produktstamm verwalten wird geöffnet. |  |
| 3 | "Neuen Produktstamm anlegen" auswählen | Wählen Sie in der Sicht Produktstamm verwalten die Option Produkt anlegen. | Das Fenster Stammdatensatz anlegen wird angezeigt. |  |
| 4 | Daten in Pflichtfelder eingeben | Geben Sie in der Sicht Stammdatensatz anlegen die folgenden Daten ein:Produktnummer: z.B. Z …externe alphanumerische Kennung ... (muss mit einem Zeichen beginnen) oder kein Eintrag (in diesem Fall weist das System automatisch eine numerische ID zu)Produktart: HALB (Halbfabrikat)Produktgruppe: z.B. L003Basismengeneinheit: z.B. StückBeschreibung: <beliebige Beschreibung> |  |  |
| 5 | Wählen Sie OK. | Wählen Sie in der Sicht Produktstamm verwalten OK. | Die Sicht Produktstamm verwalten wird angezeigt. |  |
| 6 | Grunddaten eingeben | Geben Sie in der Sicht Produktstamm verwalten > GRUNDDATEN > Grunddaten die folgenden Daten ein:Sparte: z.B. 00 |  |  |
| 7 | "Anlegen" wählen | Wechseln Sie in der Sicht Produkt zur Facette GRUNDDATEN > Beschreibungen, und wählen Sie Anlegen. | Die Beschreibung in der Standardsprache (z.B. Deutsch) ist bereits eingegeben. |  |
| 8 | Beschreibungsdaten eingeben | Geben Sie in der Sicht Beschreibungen folgende Daten ein:Sprache: z.B. DeutschProduktbeschreibung: <Ihre Beschreibung> | Beschreibungen können in verschiedenen Sprachen gepflegt werden. |  |
| 9 | Basismengeneinheit auswählen | Wählen Sie in der Sicht Produktstamm verwalten > GRUNDDATEN die Option Mengeneinheit aus. | Die Sicht Mengeneinheit wird angezeigt. |  |
| 10 | Daten sichern | Wählen Sie Sichern. | Eine Systemmeldung bestätigt, dass das Objekt gesichert wurde. |  |

### Produktstammdaten anlegen – Einkaufsdaten

Testverwaltung

Kundenprojekt: Füllen Sie die projektbezogenen Teile aus.

|  |  |  |  |
| --- | --- | --- | --- |
| Testfall-ID | <X.XX> | Testdatum: |  |
| Testername: |  | Dauer: |  |
| Benutzerrolle(n): |  | Zuständigkeit: | <Geben Sie den Serviceanbieter, einen Kunden oder einen Serviceanbieter zusammen mit einem Kunden an.> |

Zweck

In diesem Verfahren erhalten Sie eine Anleitung zum Anlegen von Produktstammdaten. Die zur Verfügung stehenden Apps hängen von der Ihnen zugeordneten Rolle ab. Aus diesem Grund sind zwei Optionen verfügbar.

Voraussetzung

Sie müssen den vorangehenden Abschnitt Produktstammdaten anlegen – Grunddaten erst abschließen, bevor Sie mit diesem Abschnitt fortfahren können.

Beginnen Sie mit dieser Vorgehensweise, nachdem Sie die eingegebenen Grunddaten gesichert haben, wie im vorherigen Abschnitt erläutert.

Vorgehensweise: Option 1 – Material anlegen

Gehen Sie folgendermaßen vor, wenn Sie aufgrund Ihrer Benutzerrolle auf die App Material anlegen(MM01) zugreifen können.

| Testschrittnummer | Bezeichnung des Testschritts | Anweisungen | Erwartetes Ergebnis | Bestanden/Nicht bestanden/Anmerkung |
| --- | --- | --- | --- | --- |
| 1 | SAP-Fiori-App aufrufen | Öffnen Sie Material anlegen(MM01). | Die Sicht Material anlegen (Einstieg) wird angezeigt. |  |
| 2 | Materialgrunddaten eingeben | Nehmen Sie in der Sicht Material anlegen (Einstieg), die folgenden Einträge vor:Material: MaterialnummerBranche:MHinweis Ist das Eingabefeld Branche ausgeblendet, ist keine Eingabe erforderlich. Wird die Branche nicht zur Eingabe angeboten, wird nicht bekannt im Feld eingetragen.Materialart: HALB (Halbfabrikat)Wählen Sie Sichtenauswahl. | Die Sicht Sichtenauswahl wird angezeigt. |  |
| 3 | Sichten wählen | Wählen Sie im Fenster Sichtenauswahl die Sicht Einkauf aus und wählen Sie Weiter.Hinweis Nur Polen: um den PKWiU-Code einzugeben, wählen Sie auch Außenhandel - Importdaten aus, bevor Sie Weiter wählen. | Die Sicht Organisationsebenen wird angezeigt. |  |
| 4 | Organisationsebenendaten eingeben | Nehmen Sie auf in der Sicht Organisationsebenen im Abschnitt Organisationsebenen den folgenden Eintrag vor und wählen Sie Weiter:Werk: <Werksnummer> | Die Sicht Material anlegen (Halbfabrikat) wird angezeigt. |  |
| 5 | Einkaufsdaten eingeben | Nehmen Sie in der Sicht Material (Halbfabrikat) auf der Registerkarte Einkauf im Abschnitt Allgemeine Daten die folgenden Einträge vor:Einkäufergruppe: z.B. 001Materialgruppe: z.B. L003 |  |  |
| 6 | Einkaufsdaten eingeben | Nehmen Sie im Bereich Sonstige Daten / Herstellerdaten den folgenden Eintrag vor:WE-Bearbeitungszeit: z.B. 1 | Es öffnet sich das neue Fenster Letzte Datensicht erreicht mit der Meldung Sie beenden die Bearbeitung. Möchten Sie Ihre Daten zunächst sichern? |  |
| Nur für Polen: | "Außenhandel – Importdaten" eingeben | Geben Sie für Polen im Abschnitt Außenhandelsdaten die PKWiU-Codedaten ein:Steuerungscode: z.B. 24.10.32.0 | Der PKWiU-Code für Polen ist gepflegt. |  |
| 7 | Daten sichern | Wählen Sie im Fenster Letzte Datensicht erreicht die Drucktaste Ja. | Das Fenster Stammdaten - Produkt wird angezeigt.Ihre Daten werden gesichert. |  |

Vorgehensweise: Option 2 – Produktstammdaten verwalten

Gehen Sie folgendermaßen vor, wenn Sie aufgrund Ihrer Benutzerrolle auf die App Produktstammdaten verwalten(F1602) zugreifen können.

| Testschrittnummer | Bezeichnung des Testschritts | Anweisungen | Erwartetes Ergebnis | Bestanden/Nicht bestanden/Anmerkung |
| --- | --- | --- | --- | --- |
| 1 | SAP-Fiori-App aufrufen | Öffnen Sie Produktstammdaten verwalten(F1602). | Die App Produktstammdaten verwalten wird geöffnet, und es werden verschiedene Suchfelder angezeigt. |  |
| 2 | Produkt suchen und zur Bearbeitung öffnen | Suchen Sie nach dem zuvor angelegten Produkt, indem Sie Produktnummer im Suchfeld Produkt eingeben.Wählen Sie das Produkt aus der Liste aus. Sie gelangen daraufhin zur Sicht Produkt.Wählen Sie Bearbeiten. | Das Produkt wird im Bearbeitungsmodus angezeigt (die Felder sind eingabebereit). |  |
| 3 | Einkaufsdaten auswählen | Wählen Sie in der Sicht Produktstamm die Option EINKAUF. | Die EINKAUFSSICHT wird angezeigt. |  |
| 4 | Einkaufsdaten eingeben | Geben Sie in der EINKAUFSSICHT folgende Daten ein:• Einkaufswerteschlüssel: z.B. 1 |  |  |
| 5 | Daten sichern | Wählen Sie Sichern. | Eine Systemmeldung bestätigt, dass das Objekt gesichert wurde. |  |

### Produktstammdaten anlegen - Dispositions-/Planungsdaten/Werksdaten

Testverwaltung

Kundenprojekt: Füllen Sie die projektbezogenen Teile aus.

|  |  |  |  |
| --- | --- | --- | --- |
| Testfall-ID | <X.XX> | Testdatum: |  |
| Testername: |  | Dauer: |  |
| Benutzerrolle(n): |  | Zuständigkeit: | <Geben Sie den Serviceanbieter, einen Kunden oder einen Serviceanbieter zusammen mit einem Kunden an.> |

Zweck

In diesem Verfahren erhalten Sie eine Anleitung zum Anlegen von Produktstammdaten. Die zur Verfügung stehenden Apps hängen von der Ihnen zugeordneten Rolle ab. Aus diesem Grund sind zwei Optionen verfügbar.

Voraussetzung

Sie müssen den vorangehenden Abschnitt Produktstammdaten anlegen – Grunddaten erst abschließen, bevor Sie mit diesem Abschnitt fortfahren können.

Beginnen Sie mit dieser Vorgehensweise, nachdem Sie die eingegebenen Grunddaten gesichert haben, wie bei der vorherigen Vorgehensweise erläutert.

Vorgehensweise: Option 1 – Material anlegen

Gehen Sie folgendermaßen vor, wenn Sie aufgrund Ihrer Benutzerrolle auf die App Material anlegen(MM01) zugreifen können.

| Testschrittnummer | Bezeichnung des Testschritts | Anweisungen | Erwartetes Ergebnis | Bestanden/Nicht bestanden/Anmerkung |
| --- | --- | --- | --- | --- |
| 1 | SAP-Fiori-App aufrufen | Öffnen Sie Material anlegen(MM01). | Die Sicht Material anlegen (Einstiegssicht) wird angezeigt. |  |
| 2 | Materialgrunddaten eingeben | Nehmen Sie in der Sicht Material anlegen (Einstiegssicht) die folgenden Einträge vor:Material: MaterialnummerBranche: MHinweis Ist das Eingabefeld Branche ausgeblendet, ist keine Eingabe erforderlich. Wird die Branche nicht zur Eingabe angeboten, wird nicht bekannt im Feld eingetragen.Materialart: HALB (Halbfabrikat)Wählen Sie Sichtenauswahl. | Die Sicht Sichtenauswahl wird angezeigt. |  |
| 3 | Sichten wählen | Wählen Sie im Fenster Sichtenauswahl die Sichten Disposition 1, Disposition 2, Disposition 3 und Disposition 4 aus, und wählen Sie Weiter. | Die Sicht Organisationsebenen wird angezeigt. |  |
| 4 | Organisationsebenendaten eingeben | Nehmen Sie in der Sicht Organisationsebenen im Abschnitt Organisationsebenen die folgenden Einträge vor:WerkLagerort | Die Sicht Material anlegen (Halbfabrikat) wird angezeigt. |  |
| 5 | Dispositions-/Planungsdaten eingeben | Nehmen Sie auf der Sicht Material anlegen (Halbfabrikat) auf der Registerkarte Disposition 1 im Abschnitt Allgemeine Daten die folgenden Einträge vor:Dispositionsmerkmal: PDFixierungshorizontDisponent: 001 | Im unteren Sichtbereich wird die folgende Systemmeldung angezeigt: Das Material existiert bereits und wird erweitert. | . |
| 6 | Dispositions-/Planungsdaten eingeben | Nehmen Sie im Bereich Losgrößenverfahren den folgenden Eintrag vor:Losgrößenverfahren: EX | Die Sicht Disposition 2 wird angezeigt. |  |
| 7 | Dispositions-/Planungsdaten eingeben | Nehmen Sie auf der Sicht Material anlegen (Halbfabrikat) auf der Registerkarte Disposition 2 im Abschnitt Beschaffung die folgenden Einträge vor:BeschaffungsartProduktionslagerort |  |  |
| 8 | Dispositions-/Planungsdaten eingeben | Nehmen Sie im Bereich Terminierung die folgenden Einträge vor:EigenfertigungPlanlieferzeitWE-BearbeitungszeitHorizontschlüssel | Die Sicht Disposition 3 wird angezeigt. |  |
| 9 | Dispositions-/Planungsdaten eingeben | Nehmen Sie auf der Sicht Material anlegen (Halbfabrikat) auf der Registerkarte Disposition 3 im Abschnitt Planung die folgenden Einträge vor:StrategiegruppeVerrechnungsmodusVerInt RückwärtsVerInt Vorwärts |  |  |
| 10 | Dispositions-/Planungsdaten eingeben | Nehmen Sie im Bereich Verfügbarkeitsprüfung die folgenden Einträge vor:VerfügbarkeitsprüfungGesamtwieder- beschaffungszeit | Die Sicht Disposition 4 wird angezeigt. |  |
| 11 | Dispositions-/Planungsdaten eingeben | Hinweis Für den Umfangsbestandteil Lohnbearbeitung - BMY müssen Sie das Feld Fertigungsversionen pflegen, um die korrekte Funktion sicherzustellen.Nehmen Sie auf der Sicht Material anlegen (Halbfabrikat) auf der Registerkarte Disposition 4 im Abschnitt Stücklistenauflösung/Sekundärbedarfe die folgenden Einträge vor:Einzel/Sammel: | Ein neues Fenster Neue Datensicht erreicht wird mit folgender Meldung geöffnet: Sie beenden die Bearbeitung. Möchten Sie Ihre Daten zunächst sichern? |  |
| 12 | Daten sichern | Wählen Sie im Fenster Letzte Datensicht erreicht die Drucktaste Ja. | Die Sicht Stammdaten - Produkt wird angezeigt.Ihre Daten werden gesichert. |  |

Vorgehensweise: Option 2 – Produktstammdaten verwalten

Gehen Sie folgendermaßen vor, wenn Sie aufgrund Ihrer Benutzerrolle auf die App Produktstammdaten verwalten(F1602) zugreifen können.

| Testschrittnummer | Bezeichnung des Testschritts | Anweisungen | Erwartetes Ergebnis | Bestanden/Nicht bestanden/Anmerkung |
| --- | --- | --- | --- | --- |
| 1 | SAP-Fiori-App aufrufen | Öffnen Sie Produktstammdaten verwalten(F1602). | Die App Produktstammdaten verwalten wird geöffnet, und es werden verschiedene Suchfelder angezeigt. |  |
| 2 | Produkt suchen und zur Bearbeitung öffnen | Suchen Sie nach dem zuvor angelegten Produkt, indem Sie Produktnummer im Suchfeld Produkt eingeben.Wählen Sie das Produkt aus der Liste aus. Sie gelangen daraufhin zur Sicht Produkt.Wählen Sie Bearbeiten. | Das Produkt wird im Bearbeitungsmodus angezeigt (die Felder sind eingabebereit). |  |
| 3 | Werksdaten auswählen | Wählen Sie in der Sicht Produktstamm die Option WERKE. | Die Sicht WERKE wird angezeigt. |  |
| 4 | "Anlegen" wählen | Wählen Sie in der Sicht WERKE die Option Anlegen. | Die Sicht Werk wird im Bearbeitungsmodus geöffnet. |  |
| 5 | Werke – Allgemeine Daten eingeben | Nehmen Sie in der Sicht Werk > ALLGEMEINE INFORMATIONEN folgende Einträge vor:Werk: <Werksnummer>Profitcenter: z.B. YB110 oder YB111Ladegruppe: z.B. 0001 | Die Sicht Material anlegen (Halbfabrikat) wird angezeigt. |  |
| 6 | Werke – Dispositionsdaten eingeben | Hinweis Für den Umfangsbestandteil Lohnbearbeitung - BMY müssen Sie auch das Feld Strategiegruppe pflegen.Wählen Sie in der Sicht Produktstamm die Option Dispositionsdaten.Wählen Sie auf der Sicht Dispositionsdaten Dispositionsdaten aus, und nehmen die folgenden Einträge vor:Verfügbarkeitsprüfung: z.B. SPPlanlieferzeit: z.B. 3Wareneingangsbearbeitungszeit: z.B. 1Dispositionsmerkmal: z.B. PD DispositionDisponent: z.B. 001 |  |  |
| 7 | Werke – Losgrößendaten eingeben | Wählen Sie in der Sicht "Dispositionsdaten" die Option Losgrößendaten.Geben Sie in der Sicht Losgrößendaten folgende Daten ein:Losgrößenverfahren: z.B. EX |  |  |
| 8 | "Werke – Beschaffungsdaten" eingeben | Geben Sie im Abschnitt Dispositionsdaten > Beschaffung folgende Daten ein:● Planlieferzeit: z.B. 3● Wareneingangsbearbeitungszeit: z.B. 1 |  |  |
| 9 | Werke – Prognosedaten auswählen | Wählen Sie in der Sicht Produktstamm verwalten - WERKE PROGNOSE. | Die Sicht Werk – PROGNOSE wird angezeigt. |  |
| 10 | Werke – Prognosedaten eingeben | Geben Sie in der Sicht PROGNOSE folgende Daten ein:Periodenart: z.B. M |  |  |
| 11 | Zur Hauptsicht zurückkehren | Wählen Sie Übernehmen, um zur Sicht Produkte zurückzukehren. | Kehren Sie zur Sicht Produktstamm zurück. |  |
| 12 | Daten sichern | Wählen Sie Sichern. | Eine Systemmeldung bestätigt, dass das Objekt gesichert wurde. |  |

### Produktstammdaten anlegen - Lagerortdaten

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

Sie müssen den vorangehenden Abschnitt Produktstammdaten anlegen – Grunddaten erst abschließen, bevor Sie mit diesem Abschnitt fortfahren können.

Beginnen Sie mit dieser Vorgehensweise, nachdem Sie die eingegebenen Grunddaten gesichert haben, wie im vorherigen Abschnitt erläutert.

Vorgehensweise: Option 1 – Material anlegen

Gehen Sie folgendermaßen vor, wenn Sie aufgrund Ihrer Benutzerrolle auf die App Material anlegen(MM01) zugreifen können.

| Testschrittnummer | Bezeichnung des Testschritts | Anweisung | Erwartetes Ergebnis | Bestanden/Nicht bestanden/Anmerkung |
| --- | --- | --- | --- | --- |
| 1 | SAP-Fiori-App aufrufen | Öffnen Sie Material anlegen(MM01). | Die Sicht Material anlegen (Einstieg) wird angezeigt. |  |
| 2 | Materialgrunddaten eingeben | Nehmen Sie in der Sicht Material anlegen (Einstieg), die folgenden Einträge vor:Material: MaterialnummerBranche: MHinweis Ist das Eingabefeld Branche ausgeblendet, ist keine Eingabe erforderlich. Wird die Branche nicht zur Eingabe angeboten, wird nicht bekannt im Feld eingetragen.Materialart: HALB (Halbfabrikat)Wählen Sie Sichtenauswahl. | Die Sicht Sichtenauswahl wird angezeigt. |  |
| 3 | Views auswählen | Wählen Sie im Fenster Sichtenauswahl die folgenden Sichten aus und wählen Sie Weiter:Allg. Werksdaten / Lagerung 1Allg. Werksdaten / Lagerung 2 | Die Sicht Organisationsebenen wird angezeigt. |  |
| 4 | Organisationsebenendaten eingeben | Nehmen Sie in der Sicht Organisationsebenen im Abschnitt Organisationsebenen die folgenden Einträge vor:Werk: <Werksnummer>Lagerort: <Lagerortnummer> | Es öffnet sich ein neues Fenster, das die Sicht Material anlegen (Halbfabrikat) anzeigt.Die folgende Systemmeldung wird unten in der Sicht angezeigt: Das Material existiert bereits und wird erweitert. |  |
| 5 | Lagerortdaten eingeben | Nehmen Sie in der Sicht Material anlegen (Halbfabrikat) auf der Registerkarte Werksdaten/Lagerung 1 im Abschnitt Allgemeine Daten den folgenden Eintrag vor und bestätigen Sie mit Enter:Anzahl WE-Scheine: z.B. 1 | Die Registerkarte Werksdaten/Lagerung2 wird angezeigt. |  |
| 6 | Eingaben bestätigen | Nehmen Sie auf der Registerkarte Werksdaten/Lagerung 2 im Bereich Allgemeine Werksparameter folgende Einträge vor:Profitcenter: z.B. YB110 oder YB111SerialnummernprofilWählen Sie ein gültiges Serialnummernprofil, das mit dem richtigen Equipmenttyp für Ihr Unternehmen zugeordnet wurde. | Es öffnet sich das neue Fenster Letzte Datensicht erreicht mit der Meldung Sie beenden die Bearbeitung. Möchten Sie Ihre Daten zunächst sichern? |  |
| 7 | Daten sichern | Wählen Sie im Fenster Letzte Datensicht erreicht die Drucktaste Ja. | Die Sicht Stammdaten - Produkt wird angezeigt.Ihre Daten werden gesichert. |  |

Vorgehensweise: Option 2 – Produktstammdaten verwalten

Gehen Sie folgendermaßen vor, wenn Sie aufgrund Ihrer Benutzerrolle auf die App Produktstammdaten verwalten(F1602) zugreifen können.

| Testschrittnummer | Bezeichnung des Testschritts | Anweisung | Erwartetes Ergebnis | Bestanden/Nicht bestanden/Anmerkung |
| --- | --- | --- | --- | --- |
| 1 | SAP-Fiori-App aufrufen | Öffnen Sie Produktstammdaten verwalten(F1602). | Die App Produktstammdaten verwalten wird geöffnet, und es werden verschiedene Suchfelder angezeigt. |  |
| 2 | Produkt suchen und zur Bearbeitung öffnen | Suchen Sie nach dem zuvor angelegten Produkt, indem Sie die Produktnummer im Suchfeld Produkt eingeben.Wählen Sie das Produkt aus der Liste aus. Sie gelangen daraufhin zur Sicht Produkt.Wählen Sie Bearbeiten. | Das Produkt wird im Bearbeitungsmodus angezeigt (die Felder sind eingabebereit). |  |
| 3 | Werksdaten auswählen | Wählen Sie in der Sicht Produktstamm verwalten WERKE.Hinweis Wenn Sie noch keinen Werksdatensatz hinzugefügt haben, führen Sie die Schritte des vorherigen Verfahrens Produktstammdaten anlegen -– Dispositions-/Planungsdaten/Werksdaten aus. | Die Sicht WERKE wird angezeigt. |  |
| 4 | Werksdaten auswählen | Wählen Sie in der Sicht WERKE den Pfeil nach rechts, um die Werksdaten auszuwählen, die Sie im vorherigen Verfahren angelegt haben. | Die Sicht Produktstamm - Werk wird angezeigt. |  |
| 5 | Zum Werk: Lagerort | Navigieren Sie im Abschnitt WERKE zu WERKE > LAGERORTE. | Die Sicht WERKE wird im Bearbeitungsmodus geöffnet. |  |
| 6 | "Anlegen" wählen | Wählen Sie in der Sicht WERKE > LAGERORTE > Lagerorte die Option Anlegen. | DieSicht Lagerort wird im Änderungsmodus geöffnet. |  |
| 7 | Werk eingeben: Lagerort" eingeben | Geben Sie in der Sicht Lagerort folgende Daten ein:Lagerort: <Lagerortnummer> | Die Sicht Neuer Datensatz - Lagerort wird angezeigt. |  |
| 8 | Zur Hauptsicht zurückkehren | Wählen Sie zweimal die Pfeiltaste "Zurück", um zum Produktstamm zurückzukehren. | Kehren Sie zur Sicht Produktstamm zurück. |  |
| 9 | Daten sichern | Wählen Sie Sichern. | Eine Systemmeldung bestätigt, dass das Objekt gesichert wurde. |  |

### Produktstammdaten anlegen – Buchhaltungsdaten / Bewertungsbereichsdaten

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

Sie müssen den vorangehenden Abschnitt Produktstammdaten anlegen – Grunddaten erst abschließen, bevor Sie mit diesem Abschnitt fortfahren können.

Beginnen Sie mit dieser Vorgehensweise, nachdem Sie die eingegebenen Grunddaten gesichert haben, wie bei der vorherigen Vorgehensweise erläutert.

Vorgehensweise: Option 1 – Material anlegen

Gehen Sie folgendermaßen vor, wenn Sie aufgrund Ihrer Benutzerrolle auf die App Material anlegen(MM01) zugreifen können.

| Testschrittnummer | Bezeichnung des Testschritts | Anweisung | Erwartetes Ergebnis | Bestanden/Nicht bestanden/Anmerkung |
| --- | --- | --- | --- | --- |
| 1 | SAP-Fiori-App aufrufen | Öffnen Sie Material anlegen(MM01). | Die Sicht Material anlegen (Einstieg) wird angezeigt. |  |
| 2 | Materialgrunddaten eingeben | Nehmen Sie in der Sicht Material anlegen (Einstieg), die folgenden Einträge vor:Material: MaterialnummerBranche: MHinweis Ist das Eingabefeld Branche ausgeblendet, ist keine Eingabe erforderlich. Wird die Branche nicht zur Eingabe angeboten, wird nicht bekannt im Feld eingetragen.Materialart: HALB (Halbfabrikat)Wählen Sie Sichtenauswahl. | Die Sicht Sichtenauswahl wird angezeigt. |  |
| 3 | Sichten wählen | Wählen Sie im Fenster Sichtenauswahl die folgenden Sichten aus und wählen Sie Weiter:Buchhaltung 1Buchhaltung 2 | Die Sicht Organisationsebenen wird angezeigt. |  |
| 4 | Organisationsebenendaten eingeben | Nehmen Sie in der Sicht Organisationsebenen im Abschnitt Organisationsebenen die folgenden Einträge vor:Werk | Ein neues Fenster wird geöffnet, das die Sicht Material anlegen (Halbfabrikat) anzeigt.Die folgende Systemmeldung wird unten in der Sicht angezeigt: Das Material existiert bereits und wird erweitert. | . |
| 5 | Buchhaltungsdaten eingeben | Nehmen Sie in der Sicht Material anlegen (Halbfabrikat) auf der Registerkarte Buchhaltung 1 im Abschnitt Allgemeine Bewertungsdaten den folgenden Eintrag vor:Bewertungsklasse: z.B. 7900 |  |  |
| 6 | Buchhaltungsdaten eingeben | Nehmen Sie im Bereich Preise und Werte die folgenden Einträge vor:StandardpreisPer. VPreis: z.B. 20Preis- strg: z.B. SBestätigen Sie Ihre Einträge, indem Sie zweimal Enter drücken. | Die Registerkarte Buchhaltung 2 wird angezeigt. |  |
| 7 | Eingaben bestätigen | Auf der Registerkarte Buchhaltung 2 müssen Sie keine Einträge vornehmen. | Es öffnet sich das neue Fenster Letzte Datensicht erreicht mit der Meldung Sie beenden die Bearbeitung. Möchten Sie Ihre Daten zunächst sichern? |  |
| 8 | Daten sichern | Wählen Sie im Fenster Letzte Datensicht erreicht die Drucktaste Ja. | Das Fenster Stammdaten - Produkt wird angezeigt.Ihre Daten werden gesichert. |  |

Vorgehensweise: Option 2 – Produktstammdaten verwalten

Gehen Sie folgendermaßen vor, wenn Sie aufgrund Ihrer Benutzerrolle auf die App Produktstammdaten verwalten(F1602) zugreifen können.

| Testschrittnummer | Bezeichnung des Testschritts | Anweisung | Erwartetes Ergebnis | Bestanden/Nicht bestanden/Anmerkung |
| --- | --- | --- | --- | --- |
| 1 | SAP-Fiori-App aufrufen | Öffnen Sie Produktstammdaten verwalten(F1602). | Die App Produktstammdaten verwalten wird geöffnet, und es werden verschiedene Suchfelder angezeigt. |  |
| 2 | Produkt suchen und zur Bearbeitung öffnen | Suchen Sie nach dem zuvor angelegten Produkt, indem Sie die Produktnummer im Suchfeld Produkt eingeben.Wählen Sie das Produkt aus der Liste aus. Sie gelangen daraufhin zur Sicht Produkt.Wählen Sie Bearbeiten. | Das Produkt wird im Bearbeitungsmodus angezeigt (die Felder sind eingabebereit). |  |
| 3 | Bewertungskreisdaten auswählen | Wählen Sie in der Sicht Produktstamm die Option BEWERTUNGSKREISE. | Der Anzeigebereich BEWERTUNGSKREIS wird angezeigt. |  |
| 4 | "Anlegen" wählen | Wählen Sie in der Sicht Neuer Produktstamm - BEWERTUNGSKREIS die Option Anlegen. | Die Sicht Produktstamm – Bewertung wird im Änderungsmodus geöffnet. |  |
| 5 | Bewertungskreisdaten eingeben | Geben Sie in der Sicht "Neuer Produktstamm – Bewertung" folgende Daten ein:Bewertungskreis: <Nummer>Preissteuerungsfindung: z.B. 2Hinweis Nur für Brasilien: Die Preisfindung für Brasilien muss 3 für brasilianische Kostenrechnungsvorschriften sein.Bewertungsklasse: <Nummer>, z. B. 3100 |  |  |
| 6 | Aktuelle Bewertungskreisdaten eingeben | Wählen Sie in der Sicht BEWERTUNGSKREISE > BEWERTUNG die Laufende Periode... und geben folgende Daten ein:Gleitender Durchschnittspreis: z.B. 20Preissteuerungskennzeichen: z.B. S |  |  |
| 7 | Zur Hauptsicht zurückkehren | Wählen Sie Übernehmen, um zur Sicht Produkte zurückzukehren. | Kehren Sie zur Hauptsicht Produktstamm zurück. |  |
| 8 | Daten sichern | Wählen Sie Sichern. | Eine Systemmeldung bestätigt, dass das Objekt gesichert wurde. |  |

### Produktstammdaten anlegen – Konfigurierbares Produkt und Varianten

Testverwaltung

Kundenprojekt: Füllen Sie die projektbezogenen Teile aus.

|  |  |  |  |
| --- | --- | --- | --- |
| Testfall-ID | <X.XX> | Testdatum: |  |
| Testername: |  | Dauer: |  |
| Benutzerrolle(n): |  | Zuständigkeit: | <Geben Sie den Serviceanbieter, einen Kunden oder einen Serviceanbieter zusammen mit einem Kunden an.> |

Verwendungszweck

In diesem Verfahren erhalten Sie eine Anleitung zum Anlegen von Produktstammdaten. Die zur Verfügung stehenden Apps hängen von der Ihnen zugeordneten Rolle ab. Aus diesem Grund sind zwei Optionen verfügbar.

Voraussetzung

Sie müssen das vorherige Verfahren Produktstammdaten anlegen – Grunddaten erst abschließen, bevor Sie mit diesem Verfahren fortfahren können.

Beginnen Sie mit dieser Vorgehensweise, nachdem Sie die eingegebenen Grunddaten gesichert haben, wie bei der vorherigen Vorgehensweise erläutert.

Vorgehensweise: Option 1 – Material anlegen

Gehen Sie folgendermaßen vor, wenn Sie aufgrund Ihrer Benutzerrolle auf die App Material anlegen(MM01) zugreifen können.

| Testschrittnummer | Bezeichnung des Testschritts | Anweisungen | Erwartetes Ergebnis | Bestanden/Nicht bestanden/Anmerkung |
| --- | --- | --- | --- | --- |
| 1 | SAP-Fiori-App aufrufen | Öffnen Sie Material anlegen(MM01). | Es öffnet sich ein neues Fenster, das Material anlegen (Einstieg) anzeigt. |  |
| 2 | Materialgrunddaten eingeben | Nehmen Sie auf dem Bild Material anlegen (Einstieg), die folgenden Einträge vor:Material: <Materialnummer>Branche: MHinweis Ist das Eingabefeld Branche ausgeblendet, ist keine Eingabe erforderlich. Wird die Branche nicht zur Eingabe angeboten, wird nicht bekannt im Feld eingetragen.Materialart: HALB (Halbfabrikat)Wählen Sie Sichtenauswahl. | Ein neues Fenster mit der Sicht Sichtenauswahl wird geöffnet. |  |
| 3 | Sichten wählen | Wählen Sie im Fenster Sichtenauswahl die folgenden Sichten aus und wählen Sie Weiter:Grunddaten 1Grunddaten 2Klassifizierung |  |  |
| 4 | Grunddaten eingeben | Geben Sie in der Sicht Material (Fertigerzeugnis) auf der Registerkarte Grunddaten 1 die Materialbeschreibung (Kurztext) und die Basismengeneinheit ein.Drücken Sie die Eingabetaste. | Die Registerkarte Grunddaten 2 wird angezeigt. |  |
| 5 | Grunddaten eingeben | Markieren Sie auf der Registerkarte Grunddaten 2 das Ankreuzfeld Material ist konfigurierbar.Wählen Sie Enter. | Die Registerkarte Klassifizierung wird angezeigt, und das Dialogfenster Klassenart wird geöffnet. |  |
| 6 | Klassenart wählen | Wählen Sie im Dialogfenster Klassenart die Klassenart 300 (Variante) aus, und wählen Sie Weiter. | Die Sicht Klassifikation wird angezeigt. |  |
| 7 | Klasse zuordnen | Ordnen Sie im Abschnitt Zuordnung eine Klasse zu, und wählen Sie Enter. | Die entsprechenden Merkmale werden unterhalb des Abschnitts Zuordnung angezeigt. |  |
| 8 | Merkmalswerte auswählen | Wählen Sie die gewünschten Werte der Merkmale aus. |  |  |
| 9 | Daten sichern | Wählen Sie Sichern. | Das konfigurierbare Material wird angelegt. Nun müssen Sie eine Variante anlegen. |  |
| 10 | Variante anlegen | Zum Anlegen der Variante öffnen Sie erneut die Kachel Material anlegen, und führen Sie die oben beschriebenen Schritte zum Anlegen eines neuen Materials mit Grunddaten 1 und Grunddaten 2 aus. |  |  |
| 11 | Variante anlegen | Wählen Sie unter Grunddaten 2 die Mandantenspezifische Konfiguration, und geben Sie unter Werksüberg.konf.Mat. das zuvor angelegte konfigurierbare Material ein. Wählen Sie Variante einstellen, und wählen Sie anschließend den gewünschten Merkmalswert zum Konfigurieren von Varianten aus. | Die Variante wird angelegt. |  |

Vorgehensweise: Option 2 – Produktstammdaten verwalten

Gehen Sie folgendermaßen vor, wenn Sie aufgrund Ihrer Benutzerrolle auf die App Produktstammdaten verwalten(F1602) zugreifen können.

| Testschrittnummer | Bezeichnung des Testschritts | Anweisungen | Erwartetes Ergebnis | Bestanden/Nicht bestanden/Anmerkung |
| --- | --- | --- | --- | --- |
| 1 | SAP-Fiori-App aufrufen | Öffnen Sie Produktstammdaten verwalten(F1602). | Die App Produktstammdaten verwalten wird geöffnet, und es werden verschiedene Suchfelder angezeigt. |  |
| 2 | Produkt suchen und zur Bearbeitung öffnen | Suchen Sie nach dem zuvor angelegten Produkt, indem Sie Produktnummer im Suchfeld Produkt eingeben.Wählen Sie das Produkt aus der Liste aus. Sie gelangen daraufhin zur Sicht Produkt.Wählen Sie Bearbeiten. | Das Produkt wird im Bearbeitungsmodus angezeigt (die Felder sind eingabebereit). |  |
| 3 | Produkt als konfigurierbar kennzeichnen | Wechseln Sie in der Sicht Produkt zur Registerkarte Konfiguration, und markieren Sie das Ankreuzfeld Produkt ist konfigurierbar. |  |  |
| 4 | Variantenklasse zuordnen | Wählen Sie in der Sicht Produkt die Registerkarte Klassifikation und anschließend Hier klicken, um eine Klasse zuzuordnen. Wählen Sie dann eine Klasse mit der Klassenart 300 (Variante) aus. | Die Merkmale der zugeordneten Klasse werden angezeigt. |  |
| 5 | "Merkmale" wählen | Wählen Sie für jedes Merkmal die gewünschten Merkmalswerte aus. |  |  |
| 6 | Zur Registerkarte "Varianten" wechseln | Wechseln Sie in der Sicht Produkt zur Registerkarte Varianten, und wählen Sie Produktvarianten auswählen. | Ein Baum oder eine Tabelle mit den verschiedenen Merkmalen wird angezeigt. |  |
| 7 | Merkmale auswählen und Varianten anlegen | Wählen Sie die gewünschte Kombination von Merkmalswerten aus, und wählen Sie Übernehmen. | Varianten werden angelegt. |  |
| 8 | Sichern | Wählen Sie Sichern. | Eine Systemmeldung bestätigt, dass das Objekt gesichert wurde. |  |

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

Sie müssen das vorherige Verfahren Produktstammdaten anlegen – Grunddaten erst abschließen, bevor Sie mit diesem Verfahren fortfahren können.

Beginnen Sie mit dieser Vorgehensweise, nachdem Sie die eingegebenen Grunddaten gesichert haben, wie bei der vorherigen Vorgehensweise erläutert.

Vorgehensweise: Option 1 – Material anlegen

Gehen Sie folgendermaßen vor, wenn Sie aufgrund Ihrer Benutzerrolle auf die App Material anlegen(MM01) zugreifen können.

| Testschrittnummer | Bezeichnung des Testschritts | Anweisung | Erwartetes Ergebnis | Bestanden/Nicht bestanden/Anmerkung |
| --- | --- | --- | --- | --- |
| 1 | SAP-Fiori-App aufrufen | Öffnen Sie Material anlegen(MM01). | Es öffnet sich ein neues Fenster, das Material anlegen (Einstieg) anzeigt. |  |
| 2 | Materialgrunddaten eingeben | Wählen Sie auf dem Bild Material anlegen (Einstieg) im Menü Mehr den Pfad Material > Ändern > Sofort, und geben Sie folgende Daten ein:Material: MaterialnummerBranche: MHinweis Ist das Eingabefeld Branche ausgeblendet, ist keine Eingabe erforderlich. Wird die Branche nicht zur Eingabe angeboten, wird "nicht bekannt" im Feld eingetragen.Materialart: HALB (Halbfabrikat)Wählen Sie Sichtenauswahl. | Ein neues Fenster mit der Sicht Sichtenauswahl wird geöffnet. |  |
| 3 | Sichten wählen | Wählen Sie im Fenster Sichtenauswahl die Sichten Grunddaten 1 und Grunddaten 2 aus und wählen Sie Weiter. | Die Sicht Material anlegen (Fertigerzeugnis) wird angezeigt. |  |
| 4 | Dienste zum Objekt wählen | Wählen Sie auf der Drucktastenleiste Dienste zum Objekt > Anlage anlegen. | Das Fenster Datei importieren wird geöffnet. |  |
| 5 | "Hochladen" wählen | Wählen Sie im Fenster Datei importieren die Drucktaste Hochladen. | Ein Fenster zum Hochladen von Dateien wird geöffnet. |  |
| 6 | Anlage hochladen | Wählen Sie die Datei aus, und wählen Sie Öffnen. | Die Datei wird hochgeladen. |  |
| 7 | Sichern | Wählen Sie Auswählen und Sichern. | Eine Systemmeldung bestätigt, dass das Objekt gesichert wurde. |  |

Vorgehensweise: Option 2 – Produktstammdaten verwalten

Gehen Sie folgendermaßen vor, wenn Sie aufgrund Ihrer Benutzerrolle auf die App Produktstammdaten verwalten(F1602) zugreifen können.

| Testschrittnummer | Bezeichnung des Testschritts | Anweisung | Erwartetes Ergebnis | Bestanden/Nicht bestanden/Anmerkung |
| --- | --- | --- | --- | --- |
| 1 | SAP-Fiori-App aufrufen | Öffnen Sie Produktstammdaten verwalten(F1602). | Die App Produktstammdaten verwalten wird geöffnet, und es werden verschiedene Suchfelder angezeigt. |  |
| 2 | Produkt suchen und zur Bearbeitung öffnen | Suchen Sie nach dem zuvor angelegten Produkt, indem Sie die Produktnummer im Suchfeld Produkt eingeben.Wählen Sie das Produkt aus der Liste aus. Sie gelangen daraufhin zur Sicht Produkt.Wählen Sie Bearbeiten. | Das Produkt wird im Bearbeitungsmodus angezeigt (die Felder sind eingabebereit). |  |
| 3 | Anlagen wählen | Wechseln Sie in der Sicht Produkt zur Registerkarte Anlagen. | Die Sicht "Anlagen" wird angezeigt. |  |
| 4 | "Anlegen" wählen | Wählen Sie im Abschnitt Dokumentenverwaltung die Option Anlegen. | Ein Fenster zum Hochladen von Dateien wird geöffnet. |  |
| 5 | Anlage hochladen | Wählen Sie die Datei aus, und wählen Sie Öffnen. | Die Datei wird hochgeladen. |  |
| 6 | Sichern | Wählen Sie Sichern. | Eine Systemmeldung bestätigt, dass das Objekt gesichert wurde. |  |

### Produktstammdaten anlegen – Werksverkauf/Allgemeine Daten

Testverwaltung

Kundenprojekt: Füllen Sie die projektbezogenen Teile aus.

|  |  |  |  |
| --- | --- | --- | --- |
| Testfall-ID | <X.XX> | Testdatum: |  |
| Testername: |  | Dauer: |  |
| Benutzerrolle(n): |  | Zuständigkeit: | <Geben Sie den Serviceanbieter, einen Kunden oder einen Serviceanbieter zusammen mit einem Kunden an.> |

Zweck

Das Verfahren in diesem Abschnitt enthält eine Anleitung zum Anlegen von Materialstammdaten (Produktstammdaten). Die zur Verfügung stehenden Apps hängen von der Ihnen zugeordneten Rolle ab. Aus diesem Grund sind zwei Optionen verfügbar.

Voraussetzung

Sie müssen die vorherige Vorgehensweise Materialstammdaten (Produktstammdaten) anlegen - Grunddaten erst abschließen, bevor Sie mit diesem Abschnitt fortfahren können.

Beginnen Sie mit dieser Vorgehensweise, nachdem Sie die eingegebenen Grunddaten gesichert haben, wie bei der vorherigen Vorgehensweise erläutert.

Vorgehensweise: Option 1 – Material anlegen

Gehen Sie folgendermaßen vor, wenn Sie aufgrund Ihrer Benutzerrolle auf die App Material anlegen(MM01) zugreifen können.

| Testschrittnummer | Bezeichnung des Testschritts | Anweisung | Erwartetes Ergebnis | Kommentare |
| --- | --- | --- | --- | --- |
| 1 | SAP-Fiori-App aufrufen | Öffnen Sie Material anlegen(MM01). | Das Bild Material anlegen (Einstieg) wird geöffnet. |  |
| 2 | Materialgrunddaten eingeben | Nehmen Sie auf dem Bild Material anlegen (Einstieg), die folgenden Einträge vor:Material: <Materialnummer>Branche: MHinweis Ist das Eingabefeld Branche ausgeblendet, ist keine Eingabe erforderlich. Wird die Branche nicht zur Eingabe angeboten, wird "nicht bekannt" im Feld eingetragen.Materialart: HALBWählen Sie Sichtenauswahl. | Das Bild Sichtenauswahl wird angezeigt. |  |
| 3 | Sichten wählen | Wählen Sie im Fenster Sichtenauswahl die Option Grunddaten und Verkauf: Allg./Werksdaten aus, und wählen Sie dann Weiter. | Das Bild Organisationsebenen wird angezeigt. |  |
| 4 | Organisationsebenendaten eingeben | Nehmen Sie auf dem Bild Organisationsebenen im Abschnitt Organisationsebene die folgenden Einträge vor:Werk: <Werksnummer>Lagerort: <Lagerortnummer> | Das Bild Material anlegen ... (Handelswaren) wird geöffnet. |  |
| 5 | Daten in "Grunddaten 1" eingeben | Geben Sie in der Sicht "Grunddaten 1" die folgenden Daten ein, und wählen Sie Enter:Beschreibung: Geben Sie eine Beschreibung für das Produkt ein.Basismengeneinheit: Geben Sie die Basiseinheit "ST" ein, z.B. 1. |  |  |
| 6 | Daten in "Vertrieb: Allgemein/Werk" eingeben | Geben Sie im Abschnitt Versanddaten (Zeiten in Tagen) die folgenden Daten ein:Ladegruppe: Wählen Sie einen beliebigen Wert aus der Wertehilfe aus. |  |  |
| 7 | Daten sichern | Wählen Sie im unteren Bildbereich Sichern. | Ihre Daten werden gesichert. |  |

Vorgehensweise: Option 2 – Produktstammdaten verwalten

Gehen Sie folgendermaßen vor, wenn Sie aufgrund Ihrer Benutzerrolle auf die App Produktstammdaten verwalten(F1602) zugreifen können.

| Testschrittnummer | Bezeichnung des Testschritts | Anweisung | Erwartetes Ergebnis | Kommentare |
| --- | --- | --- | --- | --- |
| 1 | SAP-Fiori-App aufrufen | Wählen Sie Produktstammdaten verwalten(F1602). | Die App Produktstammdaten verwalten (F1602) wird geöffnet, und es werden verschiedene Suchfelder angezeigt. |  |
| 2 | Produkt suchen und zur Bearbeitung öffnen | Suchen Sie nach dem zuvor angelegten Produkt, indem Sie die Produktnummer im Suchfeld Produkt eingeben.Wählen Sie das Produkt aus der Liste aus. Sie gelangen daraufhin zur Sicht Produkt.Wählen Sie Bearbeiten. | Das Produkt wird im Bearbeitungsmodus angezeigt (die Felder sind eingabebereit). |  |
| 3 | Werksdaten auswählen | Wählen Sie in der Sicht Produkt die Option Werke. | Die Registerkarte Werke wird angezeigt. |  |
| 4 | "Anlegen" wählen | Wählen Sie in der Sicht Werke die Option Anlegen. |  |  |
| 5 | "Werke – Allgemeine Daten" eingeben | Geben Sie im Abschnitt Allgemeine Daten folgende Daten ein:Werk: Werksnummer, z.B. 1710 |  |  |
| 6 | Dispositionsdaten eingeben | Nehmen Sie im Abschnitt MRP folgende Einträge vor:Dispositionsmerkmal: z.B. ND |  |  |
| 7 | "Werk – Verkauf" eingeben | Geben Sie im Abschnitt Verkauf folgende Daten ein:Ladegruppe: Wählen Sie einen Wert aus der Wertehilfe. |  |  |
| 8 | Zum Hauptbild zurückkehren | Wählen Sie Übernehmen, um zur Sicht Produkt zurückzukehren. | Die Sicht Produkt wird angezeigt. |  |
| 9 | Daten sichern | Wählen Sie Sichern. | Eine Systemmeldung zeigt an: Das Objekt wurde gesichert. |  |

### Produktstammdaten anlegen – Werk/Serienfertigung

Testverwaltung

Kundenprojekt: Füllen Sie die projektbezogenen Teile aus.

|  |  |  |  |
| --- | --- | --- | --- |
| Testfall-ID | <X.XX> | Testdatum: |  |
| Testername: |  | Dauer: |  |
| Benutzerrolle(n): |  | Zuständigkeit: | <Geben Sie den Serviceanbieter, einen Kunden oder einen Serviceanbieter zusammen mit einem Kunden an.> |

Zweck

Das Verfahren in diesem Abschnitt enthält eine Anleitung zum Anlegen von Materialstammdaten (Produktstammdaten). Die zur Verfügung stehenden Apps hängen von der Ihnen zugeordneten Rolle ab. Aus diesem Grund sind zwei Optionen verfügbar.

Voraussetzung

Sie müssen die vorherige Vorgehensweise Materialstammdaten (Produktstammdaten) anlegen - Grunddaten erst abschließen, bevor Sie mit diesem Abschnitt fortfahren können.

Beginnen Sie mit dieser Vorgehensweise, nachdem Sie die eingegebenen Grunddaten gesichert haben, wie bei der vorherigen Vorgehensweise erläutert.

Vorgehensweise: Option 1 – Material anlegen

Gehen Sie folgendermaßen vor, wenn Sie aufgrund Ihrer Benutzerrolle auf die App Material anlegen(MM01) zugreifen können.

| Testschrittnummer | Bezeichnung des Testschritts | Anweisung | Erwartetes Ergebnis | Kommentare |
| --- | --- | --- | --- | --- |
| 1 | SAP-Fiori-App aufrufen | Öffnen Sie Material anlegen(MM01). | Das Bild Material anlegen (Einstieg) wird geöffnet. |  |
| 2 | Materialgrunddaten eingeben | Nehmen Sie auf dem Bild Material anlegen (Einstieg), die folgenden Einträge vor:Material: <Materialnummer>Branche: MHinweis Ist das Eingabefeld Branche ausgeblendet, ist keine Eingabe erforderlich. Wird die Branche nicht zur Eingabe angeboten, wird "nicht bekannt" im Feld eingetragen.Materialart: HALBWählen Sie Sichtenauswahl. | Das Bild Sichtenauswahl wird angezeigt. |  |
| 3 | Sichten wählen | Wählen Sie im Fenster Sichtenauswahl die Sichten Grunddaten 1, Disposition 1 und Disposition 4aus, und wählen Sie Weiter. | Das Bild Organisationsebenen wird angezeigt. |  |
| 4 | Organisationsebenendaten eingeben | Nehmen Sie auf dem Bild Organisationsebenen im Abschnitt Organisationsebene die folgenden Einträge vor:Werk: <Werksnummer>Lagerort: <Lagerortnummer> | Das Bild Material anlegen ... (Handelswaren) wird geöffnet. |  |
| 5 | Daten in "Grunddaten 1" eingeben | Geben Sie in der Sicht "Grunddaten 1" die folgenden Daten ein, und wählen Sie Enter:Beschreibung: Geben Sie eine Beschreibung für das Produkt ein.Basismengeneinheit: Geben Sie die Basiseinheit "ST" ein, z.B. 1. |  |  |
| 6 | Daten in Disposition 1 eingeben | Nehmen Sie im Abschnitt Dispositionsverfahren die folgende Eingabe vor:Dispositionsmerkmal: Pflegen Sie z.B. das Dispositionsmerkmal "ND". |  |  |
| 7 | Daten in Disposition 4 eingeben | Geben Sie im Abschnitt Serienfertigung/Montage/Deployment-Strategie folgende Daten ein:Serienfertigung: Markieren Sie das Ankreuzfeld.Serienfertigungsprofil: Wählen Sie einen beliebigen Wert aus der Wertehilfe aus. |  |  |
| 8 | Daten sichern | Wählen Sie im unteren Bildbereich Sichern. | Ihre Daten werden gesichert. |  |

Vorgehensweise: Option 2 – Produktstammdaten verwalten

Gehen Sie folgendermaßen vor, wenn Sie aufgrund Ihrer Benutzerrolle auf die App Produktstammdaten verwalten(F1602) zugreifen können.

| Testschrittnummer | Bezeichnung des Testschritts | Anweisung | Erwartetes Ergebnis | Kommentare |
| --- | --- | --- | --- | --- |
| 1 | SAP-Fiori-App aufrufen | Wählen Sie Produktstammdaten verwalten(F1602). | Die App Produktstammdaten verwalten (F1602) wird geöffnet, und es werden verschiedene Suchfelder angezeigt. |  |
| 2 | Produkt suchen und zur Bearbeitung öffnen | Suchen Sie nach dem zuvor angelegten Produkt, indem Sie die Produktnummer im Suchfeld Produkt eingeben.Wählen Sie das Produkt aus der Liste aus. Sie gelangen daraufhin zur Sicht Produkt.Wählen Sie Bearbeiten. | Das Produkt wird im Bearbeitungsmodus angezeigt (die Felder sind eingabebereit). |  |
| 3 | Werksdaten auswählen | Wählen Sie in der Sicht Produkt die Option Werke. | Die Registerkarte Werke wird angezeigt. |  |
| 4 | "Anlegen" wählen | Wählen Sie in der Sicht Werke die Option Anlegen. |  |  |
| 5 | "Werke – Allgemeine Daten" eingeben | Geben Sie im Abschnitt Allgemeine Daten folgende Daten ein:Werk: Werksnummer, z.B. 1710 |  |  |
| 6 | Dispositionsdaten eingeben | Nehmen Sie im Abschnitt MRP folgende Einträge vor:Dispositionsmerkmal: z.B. ND |  |  |
| 7 | Serienfertigungsdaten eingeben | Geben Sie im Abschnitt Serienfertigung folgende Daten ein:Serienfertigung aktiviert: Markieren Sie das Ankreuzfeld, um das Feld "Serienfertigungsprofil" zu aktivieren.Serienfertigungsprofil: Wählen Sie einen beliebigen Wert aus der Wertehilfe aus. | Wenn Sie das Ankreuzfeld Serienfertigung aktiviert markieren, sollte das Feld Serienfertigungsprofil editierbar sein.Wenn Sie das Ankreuzfeld Serienfertigung aktiviert entmarkieren, sollte das Feld "Serienfertigungsprofil" schreibgeschützt sein. |  |
| 8 | Zum Hauptbild zurückkehren | Wählen Sie Übernehmen, um zur Sicht Produkt zurückzukehren. | Die Sicht Produkt wird angezeigt. |  |
| 9 | Daten sichern | Wählen Sie Sichern. | Eine Systemmeldung zeigt an: Das Objekt wurde gesichert. |  |

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
> Flagged while digesting this document, not verified: Section titles for plant sales and repetitive manufacturing steps mention material types Handelswaren/Fertigerzeugnis in screen names although material type HALB is used; the Werksverkauf and Serienfertigung overview rows have empty expected results.

## Connections
- part-of :: [[_cluster]]
- related-to :: [[02-business-partner-and-product-master-data/master-data-script-create-product-master-of-type-semi-finished-good-md]]
- related-to :: [[02-business-partner-and-product-master-data/mds-bns-669]]
- related-to :: [[02-business-partner-and-product-master-data/mds-bns-sap-s-4hana-cloud-public-edition-2608-japanese-667]]
- related-to :: [[02-business-partner-and-product-master-data/script-de-dados-mestre-criar-mestre-de-produtos-do-tipo-produto-semiac]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/BNS_S4CLD2608_Master_Data_DE_XX.docx` — full document · extracted with `mammoth` · 60,740 chars in the whole document
