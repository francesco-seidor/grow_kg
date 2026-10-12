---
id: 02-business-partner-and-product-master-data/stammdatenskript-sap-s-4hana-cloud-public-edition-produktstamm-vom-typ
title: Stammdatenskript SAP S/4HANA Cloud Public Edition – Produktstamm vom Typ „Fertigerzeugnis“ anlegen – SDS (BNT) (BNT_S4CLD2608_Master_Data_DE_XX)
description: "German master data test script (SAP S/4HANA Cloud Public Edition 2608) for creating a finished-product (FERT) material master via MM01 or F1602, step by step per data view."
cluster: 02-business-partner-and-product-master-data
tags: [kb/business-partner-and-product-master-data, topic/product-master-raw-semifinished-finished]
aliases: [BNT_S4CLD2608_Master_Data_DE_XX]
keywords: ["Product Master: Raw Materials, Semi-Finished and Finished…", product master data, finished product creation, basic data, sales data, mrp planning data, storage location data, accounting valuation data, configurable products, product attachments]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/BNT_S4CLD2608_Master_Data_DE_XX.docx]
confidence: low
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-670
topic: 02-business-partner-and-product-master-data/product-master-raw-semifinished-finished
language: DE
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Stammdatenskript SAP S/4HANA Cloud Public Edition – Produktstamm vom Typ „Fertigerzeugnis“ anlegen – SDS (BNT) (BNT_S4CLD2608_Master_Data_DE_XX)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/BNT_S4CLD2608_Master_Data_DE_XX.docx`, extracted with `mammoth`. Grouped under **Product Master: Raw Materials, Semi-Finished and Finished Goods** in Business Partner and Product Master Data. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

| <!-- image omitted: unnamed --> | StammdatenskriptSAP S/4HANA Cloud Public Edition - 02-07-26 |
| --- | --- |
|  | Produktstamm vom Typ „Fertigerzeugnis“ anlegen – SDS (BNT) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Inhaltsverzeichnis

[1 Verwendungszweck 2](#_Toc233890047)

[2 Voraussetzungen 3](#_Toc233890048)

[2.1 Systemzugriff 3](#_Toc233890049)

[2.2 Rollen 3](#_Toc233890050)

[2.3 Erforderliche Organisationseinheiten 3](#_Toc233890051)

[2.4 Obligatorische und optionale Stammdaten 4](#_Toc233890052)

[2.5 Wesentliche Parameter für die Datenerstellung 5](#_Toc233890053)

[2.5.1 Materialart und Nummernkreise 5](#_Toc233890054)

[2.5.2 Branche 5](#_Toc233890055)

[3 Übersichtstabelle 6](#_Toc233890056)

[4 Testverfahren 7](#_Toc233890057)

[4.1 Produktstammdaten anlegen – Grunddaten 7](#_Toc233890058)

[4.2 Produktstammdaten anlegen – Verkaufsdaten / Umsatzsteuerdaten 10](#_Toc233890059)

[4.3 Produktstammdaten anlegen - Dispositions-/Planungsdaten/Werksdaten 14](#_Toc233890060)

[4.4 Produktstammdaten anlegen - Lagerortdaten 18](#_Toc233890061)

[4.5 Produktstammdaten anlegen – Buchhaltungsdaten / Bewertungsbereichsdaten 20](#_Toc233890062)

[4.6 Produktstammdaten anlegen – Konfigurierbares Produkt und Varianten 23](#_Toc233890063)

[4.7 Produktstammdaten anlegen – Anlagen sichern 26](#_Toc233890064)

[4.8 Produktstammdaten anlegen – Werksverkauf/Allgemeine Daten 28](#_Toc233890065)

[4.9 Produktstammdaten anlegen – Werk/Serienfertigung 30](#_Toc233890066)

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
| Grunddaten | Unabhängig von Organisationeinheiten | Materialbeschreibung (Kurztext), Materialnummer, Materialgruppe, Basismengeneinheit usw. | Gunddaten existieren für einen Materialstammsatz nur einmal. | Nicht zutreffend |
| Verkaufsdaten | Werk, Verkaufsorg., Vertriebsweg | Steuerdaten, Positionstypengruppe, TranspGruppe Gruppe, Ladegruppe, Rüstzeit usw. | Verkaufsdaten können für jede Verkaufsorganisation Ihrer Unternehmensstruktur vorhanden sein, für die der Materialstammsatz verwendet wird. | Werk:____________Verkaufsorganisation:__________Vertriebsweg:__________ |
| Dispositionsdaten/Planungsdaten (Werksdaten) | Werk, Lagerort | Dispositionsmerkmal, Disponent, Losgröße, Planlieferzeit usw. | Werksdaten können für jede Werks-ID Ihrer Unternehmensstruktur existieren, für die der Materialstammsatz verwendet wird.Lagerortdaten (Planungskontext) sind optional, abhängig von der Notwendigkeit, eine lagerortspezifische Planung durchzuführen. | Werk:____________Lagerort:__________ |
| Lagerortdaten | Werk, Lagerort | Anzahl WE-Scheine, Max. Lagerungszeit, Mindestrest- laufzeit usw. |  | Werk:____________Lagerort:__________ |
| Buchhaltungsdaten (Bewertungsdaten) | Bewertungsbereich (= Werk), Bewertungsart | Bewertungsklasse, Per. VPreis, Preissteuerung usw. | Daten zum Bewertungsbereich können für jede Werks-ID Ihrer Unternehmensstruktur existieren, für die der Materialstammsatz verwendet wird. Jedes Werk stellt einen Bewertungsbereich dar (z.B. unterschiedliche Bewertungspreise eines Materials in verschiedenen Werken) | Werk:____________Bewertungsart:__________ |

### Obligatorische und optionale Stammdaten

Materialstammdatensätze können auf andere Stammdaten verweisen. Die folgende Tabelle bietet eine Übersicht über die optionalen und obligatorischen Stammdatenobjekte, die in einem Materialstammdatensatz verwendet werden müssen.

|  |
| --- |
| Hinweis Für eine ordnungsgemäße Steuerberechnung sind brasilienspezifische Felder erforderlich.Prüfen Sie Nota Fiscal – Brasilien - JD0 im Kapitel BR-spezifische Felder für Stammdaten definieren für Materialstammdaten. |

| Stammdatenobjekt | Verwendet im Datensegment | Obligatorisch / optional | Kommentare |
| --- | --- | --- | --- |
| Profitcenter |  | Obligatorisch | Für einwandfreie Bewertungsprozesse ist die Zuweisung eines Profitcenters zu einem Material- oder Produktstamm erforderlich. |

### Wesentliche Parameter für die Datenerstellung

In diesem Abschnitt werden einige Basisparameter erläutert, die das Verhalten eines Stammsatzes beeinflussen und zum Anlegen eines Materialstammdatensatzes immer erforderlich sind:

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

| Prozessschritt | Anwendungsrolle | Transaktion/App | Erwartete Ergebnisse |
| --- | --- | --- | --- |
| [Produktstammdaten anlegen – Grunddaten](#unique_11) [Seite ] 7 | Stammdatenexperte – Produktdaten | Material anlegen(MM01)/Produktstammdaten verwalten(F1602) | Materialstammdaten - Grunddaten werden angelegt. |
| [Produktstammdaten anlegen – Verkaufsdaten / Umsatzsteuerdaten](#unique_12) [Seite ] 10 | Stammdatenexperte – Produktdaten | Material anlegen(MM01)/Produktstammdaten verwalten(F1602) | Materialstammdaten - Verkaufsdaten (Umsatzsteuerdaten) werden angelegt. |
| [Produktstammdaten anlegen - Dispositions-/Planungsdaten/Werksdaten](#unique_13) [Seite ] 14 | Stammdatenexperte – Produktdaten | Material anlegen(MM01)/Produktstammdaten verwalten(F1602) | Materialstammdaten - Dispositions-/Planungsdaten (Werksdaten) werden angelegt. |
| [Produktstammdaten anlegen - Lagerortdaten](#unique_14) [Seite ] 18 | Stammdatenexperte – Produktdaten | Material anlegen(MM01)/Produktstammdaten verwalten(F1602) | Materialstammdaten – Lagerortdaten werden angelegt. |
| [Produktstammdaten anlegen – Buchhaltungsdaten / Bewertungsbereichsdaten](#unique_15) [Seite ] 20 | Stammdatenexperte – Produktdaten | Material anlegen(MM01)/Produktstammdaten verwalten(F1602) | Materialstammdaten - Buchhaltungsdaten (Bewertungsdaten) werden angelegt. |
| [Produktstammdaten anlegen – Konfigurierbares Produkt und Varianten](#unique_16) [Seite ] 23 | Stammdatenexperte – Produktdaten | Material anlegen(MM01)/Produktstammdaten verwalten(F1602) | Konfigurierbares Produkt und Varianten anlegen |
| [Produktstammdaten anlegen – Anlagen sichern](#unique_17) [Seite ] 26 | Stammdatenexperte – Produktdaten | Material ändern(MM02)/Produktstammdaten verwalten(F1602) | Anlagen zum Materialstammsatz sichern |
| [Produktstammdaten anlegen – Werksverkauf/Allgemeine Daten](#unique_18) [Seite ] 28 | Stammdatenexperte – Produktdaten | Material anlegen(MM01)/Produktstammdaten verwalten(F1602) |  |
| [Produktstammdaten anlegen – Werk/Serienfertigung](#unique_19) [Seite ] 30 | Stammdatenexperte – Produktdaten | Material anlegen(MM01)/Produktstammdaten verwalten(F1602) |  |

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

| Testschrittnummer | Bezeichnung des Testschritts | Anweisung | Erwartetes Ergebnis | Bestanden/Nicht bestanden/Anmerkung |
| --- | --- | --- | --- | --- |
| 1 | Anmelden | Melden Sie sich am SAP Fiori Launchpad als Stammdatenexperte – Produktdaten an. | Das SAP Fiori Launchpad wird angezeigt. |  |
| 2 | SAP-Fiori-App aufrufen | Öffnen Sie Material anlegen(MM01). | Die App wird geöffnet. |  |
| 3 | Materialgrunddaten eingeben | Geben Sie auf dem Bild Material anlegen (Einstieg) folgende Daten ein, und wählen Sie Sichtenauswahl:Material: <Materialnummer>Branche: MHinweis Ist das Eingabefeld Branche ausgeblendet, ist keine Eingabe erforderlich. Wird die Branche nicht zur Eingabe angeboten, wird nicht bekannt im Feld eingetragen.Materialart: FERT | Die Sicht Sichtenauswahl wird angezeigt. |  |
| 4 | Sichten wählen | Wählen Sie im Fenster Sichtenauswahl die Sichten Grunddaten 1 und Grunddaten 2 aus und wählen Sie dann Weiter. | Die Sicht Material anlegen (Fertigerzeugnis) wird angezeigt. |  |
| 5 | Grunddaten eingeben | Geben Sie in der Sicht Material (Fertigerzeugnis) auf der Registerkarte Grunddaten 1 die Materialbeschreibung (Kurztext) ein. |  |  |
| 6 | Grunddaten eingeben | Nehmen Sie auf der Registerkarte Grunddaten 1 im Abschnitt Allgemeine Daten die folgenden Einträge vor:Basismengeneinheit: <Basismengeneinheit>Warengruppe: <Warengruppe>Allg. PosTypGrp: <Allg. PosTypGrp> |  |  |
| 7 | Grunddaten eingeben | Geben Sie im Abschnitt Dimensionen/EANs folgende Daten ein, und wählen Sie Enter:Bruttogewicht: <Bruttogewicht>Gewichtseinheit: <Gewichtseinheit>Nettogewicht: <Nettogewicht> | Die Registerkarte Grunddaten 2 wird angezeigt. |  |
| 8 | Grunddaten eingeben | Auf der Registerkarte Grunddaten 2 müssen Sie keine Einträge vornehmen. | Es öffnet sich das neue Fenster Letzte Datensicht erreicht mit der Meldung Sie beenden die Bearbeitung. Möchten Sie Ihre Daten zunächst sichern? |  |
| 9 | Daten sichern | Wählen Sie im Fenster Letzte Datensicht erreicht die Drucktaste Ja. | Die Sicht Stammdaten - Produkt wird angezeigt.Die Grunddaten werden angelegt und gesichert. |  |

Vorgehensweise: Option 2 – Produktstammdaten verwalten

Gehen Sie folgendermaßen vor, wenn Sie aufgrund Ihrer Benutzerrolle auf die App Produktstammdaten verwalten(F1602) zugreifen können.

| Testschrittnummer | Bezeichnung des Testschritts | Anweisung | Erwartetes Ergebnis | Bestanden/Nicht bestanden/Anmerkung |
| --- | --- | --- | --- | --- |
| 1 | Anmelden | Melden Sie sich am SAP Fiori Launchpad als Stammdatenexperte – Produktdaten an. | Das SAP Fiori Launchpad wird angezeigt. |  |
| 2 | SAP-Fiori-App aufrufen | Öffnen Sie Produktstammdaten verwalten(F1602). | Die App wird geöffnet. |  |
| 3 | "Neuen Produktstamm anlegen" auswählen | Wählen Sie Produkt anlegen. | Die Sicht Stammdatensatz anlegen wird angezeigt. |  |
| 4 | Daten in Pflichtfelder eingeben | Geben Sie in der Sicht Stammdatensatz anlegen die folgenden Daten ein:Produktnummer: z.B. Z …Hinweis Hier können Sie eine beliebige externe alphanumerische ID eingeben … (diese muss mindestens mit einem Zeichen beginnen). Wenn Sie hier keine Eingabe vornehmen, vergibt das System automatisch eine numerische ID.Weitere Informationen zur Produktnummer finden Sie unter Wesentliche Parameter für die Datenerstellung im Abschnitt Materialart und Nummernkreise.Produktart: FERTProduktgruppe: z.B. L004Basismengeneinheit: z.B. StückBeschreibung: <Beschreibung> |  |  |
| 5 | Wählen Sie OK. | Wählen Sie in der Sicht Produktstamm verwalten OK. | Die Sicht Produktstamm verwalten wird angezeigt. |  |
| 6 | Grunddaten eingeben | Navigieren Sie zu Produktstamm verwalten > GRUNDDATEN > Grunddaten, und geben Sie folgende Daten ein:Sparte: z.B. 00 |  |  |
| 7 | Sicht "Beschreibungen" aufrufen | Wechseln Sie zur Sicht Beschreibungen. | Die Beschreibung in der Standardsprache (z.B. Englisch) ist bereits gefüllt. |  |
| 8 | "Anlegen" wählen | Wählen Sie in der Sicht BESCHREIBUNGEN die Option Anlegen. | Die Sicht Produktstamm - Beschreibung wird angezeigt.Einige Felder sind bereits ausgefüllt. |  |
| 9 | Beschreibungsdaten eingeben | Geben Sie in der Sicht Produktstamm - Beschreibung folgende Daten ein:Sprache: z.B. DeutschProduktbezeichnung: <Produktbeschreibung> | Beschreibungen können in verschiedenen Sprachen gepflegt werden. |  |
| 10 | Zum Produktstamm zurückkehren | Wählen Sie die Pfeiltaste "Zurück", um zur Sicht Produktstamm zurückzukehren. | Die Sicht Produktstamm wird angezeigt. |  |
| 11 | Basismengeneinheit auswählen | Gehen Sie in der Sicht Produktstamm zu GRUNDDATEN, und wählen Sie Basismengeneinheit. | Die Sicht Mengeneinheit wird angezeigt. |  |
| 12 | Basismengeneinheit von Messdaten eingeben | Wählen Sie Mehr anzeigen, und geben Sie folgende Daten für die gewichtsbezogenen Felder ein:Gewichtseinheit: z.B. kgBruttogewicht: z.B. 2Nettogewicht: z.B. 1Hinweis Wenn in den Feldern Bruttogewicht, Gewichtseinheit oder Nettogewicht keine Eingaben möglich sind, müssen Sie die Sicht aktualisieren oder neu laden. Nach dem Aktualisieren oder erneuten Laden sollten Sie in diese Felder Daten eingeben können. |  |  |
| 13 | Zum Hauptbild zurückkehren | Wählen Sie die Pfeiltaste "Zurück", um zur Sicht Produktstamm zurückzukehren. | Die Sicht Produktstamm wird angezeigt. |  |
| 14 | Daten sichern | Wählen Sie Sichern. | Das Objekt wird gesichert. |  |

### Produktstammdaten anlegen – Verkaufsdaten / Umsatzsteuerdaten

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

Sie müssen die vorherige Vorgehensweise ([Produktstammdaten anlegen – Grunddaten](#unique_11) [Seite ] 7) abschließen, bevor Sie mit diesem Abschnitt fortfahren können.

Folgen Sie der Vorgehensweise, nachdem Sie die eingegebenen Grunddaten gesichert haben, wie im vorherigen Kapitel erläutert.

Vorgehensweise: Option 1 – Material anlegen

Folgen Sie dieser Vorgehensweise, wenn Sie mit Ihrer Benutzerrolle auf die App Material anlegen(MM01) zugreifen können.

| Testschrittnummer | Bezeichnung des Testschritts | Anweisung | Erwartetes Ergebnis | Bestanden/Nicht bestanden/Anmerkung |
| --- | --- | --- | --- | --- |
| 1 | SAP-Fiori-App aufrufen | Öffnen Sie Material anlegen(MM01). | Die App wird geöffnet. |  |
| 2 | Materialgrunddaten eingeben | Nehmen Sie in Material anlegen (Einstiegssicht) die folgenden Einträge vor:Material: <Materialnummer>Branche: MHinweis Ist das Eingabefeld Branche ausgeblendet, ist keine Eingabe erforderlich. Wird die Branche nicht zur Eingabe angeboten, ist das Feld ausgegraut.Materialart: FERTWählen Sie Sichtenauswahl. | Das Bild Sichtenauswahl wird angezeigt. |  |
| 3 | Views auswählen | Wählen Sie auf dem Bild Sichtenauswahl die Sichten Vertrieb: VerkaufsorgDaten 1, Vertrieb: VerkaufsorgDaten 2 und Vertrieb: Allg./Werksdaten.Wählen Sie Weiter.Hinweis Nur für Polen: Um die PKWiU-Klassifikationsnummer eingeben zu können, müssen Sie auch International Trade: Export wählen. | Das Bild Organisationsebenen wird angezeigt. |  |
| 4 | Organisationsebenendaten eingeben | Nehmen Sie auf dem Bild Organisationsebenen im Abschnitt Organisationsebene die folgenden Einträge vor, und wählen Sie Weiter:Werk: z.B. 1710.Verkaufsorg.: z.B. 1710.Vertriebsweg: z.B. 10. | Das Bild Material anlegen (Fertigerzeugnis) wird angezeigt.Die Systemmeldung Das Material existiert bereits und wird erweitert wird angezeigt. |  |
| 5 | Verkaufsdaten eingeben | Geben Sie auf dem Bild Material (Fertigerzeugnis) auf der Registerkarte Vertrieb: VerkOrg 1 einen geeigneten Wert für das Feld Steuerklassifikation ein. Zum Beispiel 1 für vollständig steuerpflichtig. | Die Registerkarte Verkauf: VerkOrg 2 wird angezeigt.Der eingegebene Wert zeigt an, dass das Material (für gewöhnlich) voll steuerpflichtig ist. |  |
| 6 | Verkaufsdaten eingeben | Nehmen Sie auf der Registerkarte Vertrieb: VerkOrg 2 im Abschnitt Gruppierungsbegriffe den folgenden Eintrag vor:Positionstypengruppe: <Positionstypengruppe> | Die Registerkarte Verkauf: Allg./Werk wird angezeigt. |  |
| 7 | Verkaufsdaten eingeben | Nehmen Sie auf der Registerkarte Vertrieb: Allg./Werk im Abschnitt Allgemeine Daten die folgenden Einträge vor:Verfügbarkeitsprüfung: z.B. SP |  |  |
| 8 | Verkaufsdaten eingeben | Geben Sie im Abschnitt Versanddaten (Zeiten in Tagen) die folgenden Daten ein:TranspGruppe: z.B. 0001.Ladegruppe: z.B. 0001. |  |  |
| 9 | Verkaufsdaten eingeben | Nehmen Sie im Bereich Allgemeine Werksparameter folgende Einträge vor:Profitcenter: z.B. YB110 oder YB111Serialnummernprofil: Wählen Sie ein gültiges Serialnummernprofil, das mit dem richtigen Equipmenttyp für Ihr Unternehmen zugeordnet wurde. | Das Bild Letzte Datensicht erreicht wird mit der folgenden Meldung angezeigt: Sie beenden die Bearbeitung. Möchten Sie Ihre Daten zunächst sichern? |  |
| Nur für Polen | Verkaufsdaten eingeben - nur für Polen | Geben Sie im Abschnitt International Trade: Export die folgenden Daten ein:Steuerungscode: z.B. 26.70.13.0 | Der PKWiU-Code für Polen ist gepflegt. |  |
| 10 | Daten sichern | Wählen Sie im Bild Letzte Datensicht erreicht die Drucktaste Ja. | Das Bild Stammdaten - Produkt wird angezeigt.Ihre Daten werden gesichert. |  |

Vorgehensweise: Option 2 – Produktstammdaten verwalten

Folgen Sie dieser Vorgehensweise, wenn Sie mit Ihrer Benutzerrolle auf die App Produktstammdaten verwalten(F1602) zugreifen können.

| Testschrittnummer | Bezeichnung des Testschritts | Anweisung | Erwartetes Ergebnis | Bestanden/Nicht bestanden/Anmerkung |
| --- | --- | --- | --- | --- |
| 1 | SAP-Fiori-App aufrufen | Öffnen Sie Produktstammdaten verwalten(F1602). | Die App wird geöffnet. |  |
| 2 | Produkt suchen und zur Bearbeitung öffnen | Suchen Sie nach dem zuvor angelegten Produkt, indem Sie die Produktnummer im Suchfeld Produkt eingeben.Wählen Sie das Produkt aus der Liste aus. Sie gelangen daraufhin zum Bild Produkt.Wählen Sie Bearbeiten. | Das Produkt wird im Bearbeitungsmodus angezeigt (die Felder sind eingabebereit). |  |
| 3 | Vertriebslinien auswählen | Wählen Sie auf dem Bild Produktstamm die Option Vertriebslinien. | Das Bild Vertriebslinien wird angezeigt. |  |
| 4 | "Anlegen" wählen | Navigieren Sie zu VERTRIEBSLINIEN > Vertriebslinien, und wählen Sie Anlegen. | Das Bild VERTRIEBSLINIEN wird im Bearbeitungsmodus geöffnet. |  |
| 5 | Vertriebsliniendaten eingeben | Geben Sie auf dem Bild Vertriebslinien folgende Daten ein:ALLGEMEINE DATEN - Allgemeine InformationenVerkaufsorganisation: <Verkaufsorganisationsnummer> z.B. 1710Vertriebsweg: z.B. 10.Lieferwerk: <Werksnummer>, z.B. 1710,GRUPPIERUNGSBEGRIFFEPositionstypengruppe: z.B. NORMKontierungsgruppe: z.B. 03 FertigerzeugnisseUMSATZSTEUERLand: <Ländercode> z.B. DESteuerkategorie: TTX1Steuerklassifikation: Entweder 1 für Material oder 2 für Dienstleistungen.Steuerklassifikation: z.B. 1 volle Steuer, wenn Sie die Steuerkondition UTXJ für die USA verwenden.Hinweis Die Steuerklassifizierung ist von länder-/regionsspezifischen Anforderungen abhängig. Die Steuerklassifikation in den Materialstamm- und Kundestammtabellen bestimmt die Eingaben der Steuersätze.Nur für Brasilien:Nehmen Sie im Abschnitt Steuerklassifikation folgende Einträge vor:Land: BRSteuerkategorie: IBRXSteuerklassifikation: Entweder 1 für Material oder 2 für Dienstleistungen. |  |  |
| 6 | Daten sichern | Wählen Sie Sichern. | Eine Systemmeldung bestätigt, dass das Objekt gesichert wurde. |  |

### Produktstammdaten anlegen - Dispositions-/Planungsdaten/Werksdaten

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

Sie müssen die vorherige Vorgehensweise ([Produktstammdaten anlegen – Grunddaten](#unique_11) [Seite ] 7) abschließen, bevor Sie mit diesem Abschnitt fortfahren können.

Folgen Sie der Vorgehensweise, nachdem Sie die eingegebenen Grunddaten gesichert haben, wie im vorherigen Kapitel erläutert.

Vorgehensweise: Option 1 – Material anlegen

Folgen Sie dieser Vorgehensweise, wenn Sie mit Ihrer Benutzerrolle auf die App Material anlegen(MM01) zugreifen können.

| Testschrittnummer | Bezeichnung des Testschritts | Anweisung | Erwartetes Ergebnis | Bestanden/Nicht bestanden/Anmerkung |
| --- | --- | --- | --- | --- |
| 1 | SAP-Fiori-App aufrufen | Öffnen Sie Material anlegen(MM01). | Die App wird geöffnet. |  |
| 2 | Materialgrunddaten eingeben | Nehmen Sie in Material anlegen (Einstiegssicht) die folgenden Einträge vor:Material: <Materialnummer>Branche: MHinweis Ist das Eingabefeld Branche ausgeblendet, ist keine Eingabe erforderlich. Wird die Branche nicht zur Eingabe angeboten, ist das Feld ausgegraut.Materialart: FERTWählen Sie Sichtenauswahl. | Das Bild Sichtenauswahl wird angezeigt. |  |
| 3 | Views auswählen | Wählen Sie auf dem Bild Sichtenauswahl die Sichten Disposition 1, Disposition 2, Disposition 3 und Disposition 4 aus.Wählen Sie Weiter. | Das Bild Organisationsebenen wird angezeigt. |  |
| 4 | Organisationsebenendaten eingeben | Nehmen Sie auf dem Bild Organisationsebenen im Abschnitt Organisationsebenen die folgenden Einträge vor:Werk: <Nummer des Werks>, z.B. 1710,Lagerort: z.B. 171A | Das Bild Material anlegen (Fertigerzeugnis) wird angezeigt.Die Systemmeldung Das Material existiert bereits und wird erweitert wird angezeigt. |  |
| 5 | Dispositions-/Planungsdaten eingeben | Nehmen Sie auf dem Bild Material ... anlegen (Fertigerzeugnis) auf der Registerkarte Disposition 1 im Abschnitt Allgemeine Daten den folgenden Eintrag vor:Einkäufergruppe: <Einkäufergruppe> |  |  |
| 6 | Dispositions-/Planungsdaten eingeben | Nehmen Sie im Abschnitt Dispositionsverfahren die folgende Eingabe vor:Dispositionsmerkmal: z.B. PDDisponent: z.B. 001. |  |  |
| 7 | Dispositions-/Planungsdaten eingeben | Nehmen Sie im Bereich Losgrößenverfahren den folgenden Eintrag vor:Losgrößenverfahren: EX | Die Registerkarte Disposition 2 wird angezeigt. |  |
| 8 | Dispositions-/Planungsdaten eingeben | Nehmen Sie auf dem Bild Material anlegen (Fertigerzeugnis) auf der Registerkarte Disposition 2 Einträge gemäß Ihren Anforderungen vor, oder geben Sie mindestens Werte für die Mussfelder ein. Zum Beispiel die Eigenfertigungszeit in Tagen. | Die Registerkarte Disposition 3 wird angezeigt. |  |
| 9 | Dispositions-/Planungsdaten eingeben | Nehmen Sie auf dem Bild Material anlegen (Fertigerzeugnis) auf der Registerkarte Disposition 3 im Abschnitt Planung die folgenden Einträge vor:Strategiegruppe: z.B. 40.Verrechnungsmodus: z.B. 2VerInt Rückwärts: <VerInt Rückwärts>VerInt Vorwärts: <VerInt Vorwärts> |  |  |
| 10 | Dispositions-/Planungsdaten eingeben | Nehmen Sie im Bereich Verfügbarkeitsprüfung die folgenden Einträge vor:Verfügbarkeitsprüfung: z.B. SPGesamtwieder- beschaffungszeit z.B. 3. | Die Registerkarte Disposition 4 wird angezeigt. |  |
| 11 | Dispositions-/Planungsdaten eingeben | Auf dem Bild Material anlegen (Fertigerzeugnis), auf der Registerkarte Disposition 4, müssen Sie keine Einträge vornehmen. | Das Bild Letzte Datensicht erreicht mit der Meldung Sie beenden die Bearbeitung. Möchten Sie Ihre Daten zunächst für dieses Material sichern? wird angezeigt. |  |
| 12 | Sichern | Wählen Sie im Bild Letzte Datensicht erreicht die Drucktaste Ja. | Das Bild Stammdaten - Produkt wird angezeigt.Ihre Daten werden gesichert. |  |

Vorgehensweise: Option 2 – Produktstammdaten verwalten

Folgen Sie dieser Vorgehensweise, wenn Sie mit Ihrer Benutzerrolle auf die App Produktstammdaten verwalten(F1602) zugreifen können.

| Testschrittnummer | Bezeichnung des Testschritts | Anweisung | Erwartetes Ergebnis | Bestanden/Nicht bestanden/Anmerkung |
| --- | --- | --- | --- | --- |
| 1 | SAP-Fiori-App aufrufen | Öffnen Sie Produktstammdaten verwalten(F1602). | Die App wird geöffnet. |  |
| 2 | Produkt suchen und zur Bearbeitung öffnen | Suchen Sie nach dem zuvor angelegten Produkt, indem Sie die Produktnummer im Suchfeld Produkt eingeben.Wählen Sie das Produkt aus der Liste aus. Sie gelangen daraufhin zum Bild Produkt.Wählen Sie Bearbeiten. | Das Produkt wird im Bearbeitungsmodus angezeigt (die Felder sind eingabebereit). |  |
| 3 | Werksdaten auswählen | Wählen Sie auf dem Bild Produktstamm die Option WERKE. | Das Bild WERKE wird angezeigt. |  |
| 4 | "Anlegen" wählen | Wählen Sie im Bild WERKE die Option Anlegen. | Das Bild Werk wird im Bearbeitungsmodus angezeigt. |  |
| 5 | Werke – Allgemeine Daten eingeben | Wechseln Sie zu Werk > ALLGEMEINE INFORMATIONEN, und geben Sie folgende Daten ein:Werk: <Werksnummer>, z.B. 1710,Profitcenter: z.B. YB110 oder YB111 |  |  |
| 6 | Werke – Dispositionsdaten eingeben | Wählen Sie auf dem Bild Produktstamm die Option Dispositionsdaten.Geben Sie im Abschnitt Dispositionsdaten > Dispositionsdaten folgende Daten ein:Verfügbarkeitsprüfung: z.B. SPDispositionsmerkmal: z.B. PDDisponent: z.B. 001. |  |  |
| 7 | Werke – Losgrößendaten eingeben | Wählen Sie auf dem Bild Dispositionsdaten die Option Losgrößendaten.Geben Sie im Bildbereich Losgrößendaten folgende Daten ein:Losgrößenverfahren: z.B. EX |  |  |
| 8 | "Werke – Beschaffungsdaten" eingeben | Navigieren Sie zu Dispositionsdaten > Beschaffung, und geben Sie folgende Daten ein:Planlieferzeit: z.B. 3.Wareneingangsbearbeitungszeit: z.B. 1. |  |  |
| 9 | Werke – Prognosedaten auswählen | Navigieren Sie zu Produktstamm verwalten > WERKE, und wählen Sie PROGNOSE. | Das Bild PROGNOSE wird angezeigt. |  |
| 10 | Werke – Prognosedaten eingeben | Geben Sie auf dem Bild PROGNOSE folgende Daten ein:Periodenart: z.B. M. |  |  |
| 11 | Zum Hauptbild zurückkehren | Wählen Sie Übernehmen, um zum Bild Produkt zurückzukehren. | Das Bild Produktstamm wird angezeigt. |  |
| 12 | Daten sichern | Wählen Sie Sichern. | Das Objekt wird gesichert. |  |

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

Sie müssen die vorherige Vorgehensweise ([Produktstammdaten anlegen – Grunddaten](#unique_11) [Seite ] 7) abschließen, bevor Sie mit diesem Abschnitt fortfahren können.

Folgen Sie der Vorgehensweise, nachdem Sie die eingegebenen Grunddaten gesichert haben, wie im vorherigen Kapitel erläutert.

Vorgehensweise: Option 1 – Material anlegen

Folgen Sie dieser Vorgehensweise, wenn Sie mit Ihrer Benutzerrolle auf die App Material anlegen(MM01) zugreifen können.

| Testschrittnummer | Bezeichnung des Testschritts | Anweisung | Erwartetes Ergebnis | Bestanden/Nicht bestanden/Anmerkung |
| --- | --- | --- | --- | --- |
| 1 | SAP-Fiori-App aufrufen | Öffnen Sie Material anlegen(MM01). | Die App wird geöffnet. |  |
| 2 | Materialgrunddaten eingeben | Nehmen Sie in Material anlegen (Einstiegssicht) die folgenden Einträge vor:Material: <Materialnummer>Branche: MHinweis Ist das Eingabefeld Branche ausgeblendet, ist keine Eingabe erforderlich. Wird die Branche nicht zur Eingabe angeboten, ist das Feld ausgegraut.Materialart: FERTWählen Sie Sichtenauswahl. | Das Bild Sichtenauswahl wird angezeigt. |  |
| 3 | Views auswählen | Wählen Sie auf dem Bild Sichtenauswahl die folgenden Sichten aus, und wählen Sie Weiter:Allg. Werksdaten / Lagerung 1Allg. Werksdaten / Lagerung 2 | Das Bild Organisationsebenen wird angezeigt. |  |
| 4 | Organisationsebenendaten eingeben | Nehmen Sie auf dem Bild Organisationsebenen im Abschnitt Organisationsebenen die folgenden Einträge vor:Werk: z.B. 1710.Lagerort: z.B. 171A | Das Bild Material anlegen (Fertigerzeugnis) wird angezeigt.Die Systemmeldung Das Material existiert bereits und wird erweitert wird angezeigt. |  |
| 5 | Lagerortdaten eingeben | Nehmen Sie auf dem Bild Material anlegen (Fertigerzeugnis) auf der Registerkarte Werksdaten/Lagerung1 im Bereich Allgemeine Daten folgenden Eintrag vor:Anzahl WE-Scheine: z.B. 1. | Die Registerkarte Werksdaten/Lagerung2 wird angezeigt. |  |
| 6 | Eingaben bestätigen | Auf der Registerkarte Werksdaten/Lagerung2 müssen Sie keine Einträge vornehmen.Hinweis Wählen Sie für das Feld Serialnummernprofil ein gültiges Serialnummernprofil aus, das mit dem richtigen Equipmenttyp für Ihr Unternehmen zugeordnet wurde. | Das Bild Letzte Datensicht erreicht wird mit der folgenden Meldung angezeigt: Sie beenden die Bearbeitung. Möchten Sie Ihre Daten zunächst sichern? |  |
| 7 | Sichern | Wählen Sie im Bild Letzte Datensicht erreicht die Drucktaste Ja. | Das Bild Stammdaten - Produkt wird angezeigt.Ihre Daten werden gesichert. |  |

Vorgehensweise: Option 2 – Produktstammdaten verwalten

Folgen Sie dieser Vorgehensweise, wenn Sie mit Ihrer Benutzerrolle auf die App Produktstammdaten verwalten(F1602) zugreifen können.

| Testschrittnummer | Bezeichnung des Testschritts | Anweisung | Erwartetes Ergebnis | Bestanden/Nicht bestanden/Anmerkung |
| --- | --- | --- | --- | --- |
| 1 | SAP-Fiori-App aufrufen | Öffnen Sie Produktstammdaten verwalten(F1602). | Die App wird geöffnet. |  |
| 2 | Produkt suchen und zur Bearbeitung öffnen | Suchen Sie nach dem zuvor angelegten Produkt, indem Sie die Produktnummer im Suchfeld Produkt eingeben.Wählen Sie das Produkt aus der Liste aus. Sie gelangen daraufhin zum Bild Produkt.Wählen Sie Bearbeiten. | Das Produkt wird im Bearbeitungsmodus angezeigt (die Felder sind eingabebereit). |  |
| 3 | Werksdaten auswählen | Wählen Sie auf dem Bild Produktstamm verwalten die Option WERKE.Hinweis Wenn kein Werksdatensatz vorhanden ist, führen Sie die Schritte aus dem vorherigen Kapitel [Produktstammdaten anlegen - Dispositions-/Planungsdaten/Werksdaten](#unique_13) [Seite ] 14 aus. | Das Bild WERKE wird angezeigt. |  |
| 4 | Werksdaten auswählen | Wählen Sie auf dem Bild WERKE über das Pfeilsymbol die Werksdaten aus, die Sie im vorhergehenden Schritt angelegt haben. | Das Bild Produktstamm – Werk wird angezeigt. |  |
| 5 | Zum Werk: Lagerort | Navigieren Sie auf dem Bild Produktstamm – Werk zu WERKE > LAGERORTE. | Das Bild Produktstamm – Werke wird im Änderungsmodus angezeigt. |  |
| 6 | "Anlegen" wählen | Navigieren Sie zu LAGERORTE > Lagerorte, und wählen Sie Anlegen. | Das Bild Werk - Lagerort wird im Änderungsmodus geöffnet. |  |
| 7 | Daten für "Werk: Lagerort" eingeben | Geben Sie auf dem Bild Lagerort folgende Daten ein:Lagerort: <Lagerortnummer>, z.B. 171A |  |  |
| 8 | Zum Hauptbild zurückkehren | Wählen Sie zweimal Übernehmen, um zur Sicht Produkt zurückzukehren. | Das Bild Produktstamm wird angezeigt. |  |
| 9 | Sichern | Wählen Sie Sichern. | Eine Systemmeldung bestätigt, dass das Objekt gesichert wurde. |  |

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

Sie müssen die vorherige Vorgehensweise ([Produktstammdaten anlegen – Grunddaten](#unique_11) [Seite ] 7) abschließen, bevor Sie mit diesem Abschnitt fortfahren können.

Folgen Sie der Vorgehensweise, nachdem Sie die eingegebenen Grunddaten gesichert haben, wie im vorherigen Kapitel erläutert.

Vorgehensweise: Option 1 – Material anlegen

Folgen Sie dieser Vorgehensweise, wenn Sie mit Ihrer Benutzerrolle auf die App Material anlegen(MM01) zugreifen können.

| Testschrittnummer | Bezeichnung des Testschritts | Anweisung | Erwartetes Ergebnis | Bestanden/Nicht bestanden/Anmerkung |
| --- | --- | --- | --- | --- |
| 1 | SAP-Fiori-App aufrufen | Öffnen Sie Material anlegen(MM01). | Die App wird geöffnet. |  |
| 2 | Materialgrunddaten eingeben | Nehmen Sie in Material anlegen (Einstiegssicht) die folgenden Einträge vor:Material: <Materialnummer>Branche: MHinweis Ist das Eingabefeld Branche ausgeblendet, ist keine Eingabe erforderlich. Wird die Branche nicht zur Eingabe angeboten, ist das Feld ausgegraut.Materialart: FERTWählen Sie Sichtenauswahl. | Das Bild Sichtenauswahl wird angezeigt. |  |
| 3 | Views auswählen | Wählen Sie auf dem Bild Sichtenauswahl die folgenden Sichten aus, und wählen Sie Weiter:Buchhaltung 1Buchhaltung 2 | Das Bild Organisationsebenen wird angezeigt. |  |
| 4 | Organisationsebenendaten eingeben | Nehmen Sie auf dem Bild Organisationsebenen im Abschnitt Organisationsebenen die folgenden Einträge vor:Werk: <Nummer des Werks> | Das Bild Material anlegen (Fertigerzeugnis) wird angezeigt.Die Systemmeldung Das Material existiert bereits und wird erweitert wird angezeigt. |  |
| 5 | Buchhaltungsdaten eingeben | Nehmen Sie auf dem Bild Material anlegen (Fertigerzeugnis) auf der Registerkarte Buchhaltung 1 im Abschnitt Allgemeine Bewertungsdaten den folgenden Eintrag vor:Bewertungsklasse: 7920 |  |  |
| 6 | Buchhaltungsdaten eingeben | Nehmen Sie im Bereich Preise und Werte die folgenden Einträge vor:Standardpreis: <Standardpreis>Per. VPreis: z.B. 20Preissteuerung: z.B. S | Die Registerkarte Buchhaltung 2 wird angezeigt. |  |
| 7 | Eingaben bestätigen | Auf der Registerkarte Buchhaltung 2 müssen Sie keine Einträge vornehmen. | Das Bild Letzte Datensicht erreicht wird mit folgender Meldung angezeigt: Sie beenden die Bearbeitung. Möchten Sie Ihre Daten zunächst sichern? |  |
| 8 | Daten sichern | Wählen Sie im Bild Letzte Datensicht erreicht die Drucktaste Ja. | Das Bild Stammdaten - Produkt wird angezeigt.Ihre Daten werden gesichert. |  |

Vorgehensweise: Option 2 – Produktstammdaten verwalten

Folgen Sie dieser Vorgehensweise, wenn Sie mit Ihrer Benutzerrolle auf die App Produktstammdaten verwalten(F1602) zugreifen können.

| Testschrittnummer | Bezeichnung des Testschritts | Anweisung | Erwartetes Ergebnis | Bestanden/Nicht bestanden/Anmerkung |
| --- | --- | --- | --- | --- |
| 1 | SAP-Fiori-App aufrufen | Öffnen Sie Produktstammdaten verwalten(F1602). | Die App wird geöffnet. |  |
| 2 | Produkt suchen und zur Bearbeitung öffnen | Suchen Sie nach dem zuvor angelegten Produkt, indem Sie die Produktnummer im Suchfeld Produkt eingeben.Wählen Sie das Produkt aus der Liste aus. Sie gelangen daraufhin zum Bild Produkt.Wählen Sie Bearbeiten. | Das Produkt wird im Bearbeitungsmodus angezeigt (die Felder sind eingabebereit). |  |
| 3 | Bewertungskreisdaten auswählen | Wählen Sie auf dem Bild Produktstamm verwalten die Option BEWERTUNGSKREISE. | Das Bild BEWERTUNGSKREISE wird angezeigt. |  |
| 4 | "Anlegen" wählen | Wählen Sie auf dem Bild BEWERTUNGSKREISE die Option Anlegen. | Das Bild BEWERTUNGSKREISE wird im Bearbeitungsmodus geöffnet. |  |
| 5 | Bewertungskreisdaten eingeben | Wechseln Sie zum Bild BEWERTUNGSKREISE > Bewertungskreis, und geben Sie die folgenden Daten ein:Bewertungskreis: <Bewertungskreis>: z.B. 1710Preissteuerungsfindung: 2Bewertungsklasse: z.B. 7920 |  |  |
| 6 | Aktuelle Bewertungskreisdaten eingeben | Wählen Sie in der Sicht Bewertung die Laufende Periode, und geben folgende Daten ein:Gleitender Durchschnittspreis: z.B. 20Preissteuerung: z.B. S |  |  |
| 7 | Zum Hauptbild zurückkehren | Wählen Sie Übernehmen, um zum Bild Produkt zurückzukehren. | Das Bild Produktstamm wird angezeigt. |  |
| 8 | Daten sichern | Wählen Sie Sichern. | Eine Systemmeldung bestätigt, dass das Objekt gesichert wurde. |  |

### Produktstammdaten anlegen – Konfigurierbares Produkt und Varianten

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

Sie müssen das vorherige Verfahren Produktstammdaten anlegen – Grunddaten erst abschließen, bevor Sie mit diesem Verfahren fortfahren können.

Beginnen Sie mit dieser Vorgehensweise, nachdem Sie die eingegebenen Grunddaten gesichert haben, wie bei der vorherigen Vorgehensweise erläutert.

Vorgehensweise: Option 1 – Material anlegen

Gehen Sie folgendermaßen vor, wenn Sie aufgrund Ihrer Benutzerrolle auf die App Material anlegen(MM01) zugreifen können.

| Testschrittnummer | Bezeichnung des Testschritts | Anweisungen | Erwartetes Ergebnis | Bestanden/Nicht bestanden/Anmerkung |
| --- | --- | --- | --- | --- |
| 1 | SAP-Fiori-App aufrufen | Öffnen Sie Material anlegen(MM01). | Es öffnet sich ein neues Fenster, das Material anlegen (Einstieg) anzeigt. |  |
| 2 | Materialgrunddaten eingeben | Nehmen Sie auf dem Bild Material anlegen (Einstieg), die folgenden Einträge vor:Material: MaterialnummerBranche: MHinweis Ist das Eingabefeld Branche ausgeblendet, ist keine Eingabe erforderlich. Wird die Branche nicht zur Eingabe angeboten, wird nicht bekannt im Feld eingetragen.Materialart: FERTWählen Sie Sichtenauswahl. | Ein neues Fenster mit der Sicht Sichtenauswahl wird geöffnet. |  |
| 3 | Sichten wählen | Wählen Sie im Fenster Sichtenauswahl die folgenden Sichten aus und wählen Sie Weiter:Grunddaten 1Grunddaten 2Klassifizierung |  |  |
| 4 | Grunddaten eingeben | Geben Sie in der Sicht Material (Fertigerzeugnis) auf der Registerkarte Grunddaten 1 die Materialbeschreibung (Kurztext) und die Basismengeneinheit ein.Wählen Sie Enter. | Die Registerkarte Grunddaten 2 wird angezeigt. |  |
| 5 | Grunddaten eingeben | Markieren Sie auf der Registerkarte Grunddaten 2 das Ankreuzfeld Material ist konfigurierbar.Drücken Sie die Eingabetaste. | Die Registerkarte Klassifizierung wird angezeigt, und das Dialogfenster Klassenart wird geöffnet. |  |
| 6 | Klassenart wählen | Wählen Sie im Dialogfenster Klassenart die Klassenart 300 (Variante) aus, und wählen Sie Weiter. | Die Sicht Klassifizierung wird angezeigt. |  |
| 7 | Klasse zuordnen | Ordnen Sie im Abschnitt Zuordnung eine Klasse zu, und wählen Sie "Enter". | Die entsprechenden Merkmale werden unterhalb des Abschnitts Zuordnung angezeigt. |  |
| 8 | Merkmalswerte auswählen | Wählen Sie die gewünschten Werte der Merkmale aus. |  |  |
| 9 | Daten sichern | Wählen Sie Sichern. | Das konfigurierbare Material wird angelegt. Nun müssen Sie eine Variante anlegen. |  |
| 10 | Variante anlegen | Zum Anlegen der Variante öffnen Sie erneut die Kachel Material anlegen(MM01) und führen die oben beschriebenen Schritte zum Anlegen eines neuen Materials mit Grunddaten 1 und Grunddaten 2 aus. |  |  |
| 11 | Variante anlegen | Wechseln Sie unter Grunddaten 2 zu Mandantenspezifische Konfiguration, und geben Sie unter Werksüberg.konf.Mat. das zuvor angelegte konfigurierbare Material ein. Wählen Sie anschließend Variante einstellen, und wählen Sie den gewünschten Merkmalswert zum Konfigurieren von Varianten aus. | Die Variante wird angelegt. |  |

Vorgehensweise: Option 2 – Produktstammdaten verwalten

Gehen Sie folgendermaßen vor, wenn Sie aufgrund Ihrer Benutzerrolle auf die App Produktstammdaten verwalten(F1602) zugreifen können.

| Testschrittnummer | Bezeichnung des Testschritts | Anweisungen | Erwartetes Ergebnis | Bestanden/Nicht bestanden/Anmerkung |
| --- | --- | --- | --- | --- |
| 1 | SAP-Fiori-App aufrufen | Öffnen Sie Produktstammdaten verwalten(F1602). |  |  |
| 2 | Produkt suchen und zur Bearbeitung öffnen | Suchen Sie nach dem zuvor angelegten Produkt, indem Sie Produktnummer im Suchfeld Produkt eingeben.Wählen Sie das Produkt aus der Liste aus. Sie gelangen daraufhin zur Sicht Produkt.Wählen Sie Bearbeiten. | Das Produkt wird im Bearbeitungsmodus angezeigt (die Felder sind eingabebereit). |  |
| 3 | Produkt als konfigurierbar kennzeichnen | Wechseln Sie in der Sicht Produkt zur Registerkarte Konfiguration, und markieren Sie das Ankreuzfeld Produkt ist konfigurierbar. |  |  |
| 4 | Variantenklasse zuordnen | Wechseln Sie in der Sicht Produkt zur Registerkarte Klassifizierung, wählen Sie Klicken Sie hier, um eine Klasse zuzuordnen., und wählen Sie anschließend eine Klasse der Klassenart 300 (Variante) aus. | Die Merkmale der zugeordneten Klasse werden angezeigt. |  |
| 5 | "Merkmale" wählen | Wählen Sie für jedes Merkmal die gewünschten Merkmalswerte aus. |  |  |
| 6 | Zur Registerkarte "Varianten" wechseln | Wechseln Sie in der Sicht Produkt zur Registerkarte Varianten, und wählen Sie Produktvarianten auswählen. | Es wird ein Baum oder eine Tabelle mit den verschiedenen Merkmalen angezeigt. |  |
| 7 | Merkmale auswählen und Varianten anlegen | Wählen Sie die gewünschte Kombination von Merkmalswerten aus, und wählen Sie Übernehmen. | Die Varianten werden angelegt. |  |
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

Sie müssen die vorherige Vorgehensweise ([Produktstammdaten anlegen – Grunddaten](#unique_11) [Seite ] 7) abschließen, bevor Sie mit diesem Abschnitt fortfahren können.

Folgen Sie der Vorgehensweise, nachdem Sie die eingegebenen Grunddaten gesichert haben, wie im vorherigen Kapitel erläutert.

Vorgehensweise: Option 1 – Material ändern

Folgen Sie dieser Vorgehensweise, wenn Sie mit Ihrer Benutzerrolle auf die App Material ändern(MM02) zugreifen können.

| Testschrittnummer | Bezeichnung des Testschritts | Anweisung | Erwartetes Ergebnis | Bestanden/Nicht bestanden/Anmerkung |
| --- | --- | --- | --- | --- |
| 1 | SAP-Fiori-App aufrufen | Öffnen Sie Material ändern(MM02). | Das Bild Material ändern: Einstieg wird angezeigt. |  |
| 2 | Materialnummer eingeben | Geben Sie folgende Daten ein, und wählen Sie Sichtenauswahl:Materialnummer: <Materialnummer> | Das Bild Sichtenauswahl wird angezeigt. |  |
| 3 | Views auswählen | Wählen Sie auf dem Bild Sichtenauswahl die Sichten Grunddaten 1 und Grunddaten 2 aus.Wählen Sie Weiter. | Das Bild Material ändern (Fertigerzeugnis) wird angezeigt. |  |
| 4 | Dienste zum Objekt wählen | Navigieren Sie auf Drucktastenleiste zu Dienste zum Objekt > Anlage anlegen. | Das Bild Datei importieren wird angezeigt. |  |
| 5 | "Hochladen" wählen | Wählen Sie auf dem Bild Datei importieren die Option Hochladen. | Ein Bild für den Datei-Upload wird angezeigt. |  |
| 6 | Anlage hochladen | Wählen Sie die Datei aus, und wählen Sie Öffnen. | Die Datei wird hochgeladen. |  |
| 7 | Sichern | Wählen Sie Auswählen und dann Sichern. | Eine Systemmeldung bestätigt, dass das Objekt gesichert wurde. |  |

Vorgehensweise: Option 2 – Produktstammdaten verwalten

Folgen Sie dieser Vorgehensweise, wenn Sie mit Ihrer Benutzerrolle auf die App Produktstammdaten verwalten(F1602) zugreifen können.

| Testschrittnummer | Bezeichnung des Testschritts | Anweisung | Erwartetes Ergebnis | Bestanden/Nicht bestanden/Anmerkung |
| --- | --- | --- | --- | --- |
| 1 | SAP-Fiori-App aufrufen | Wählen Sie Produktstammdaten verwalten(F1602). | Die App wird geöffnet. |  |
| 2 | Produkt suchen und zur Bearbeitung öffnen | Suchen Sie nach dem zuvor angelegten Produkt, indem Sie die Produktnummer im Suchfeld Produkt eingeben.Wählen Sie das Produkt aus der Liste aus. Sie gelangen daraufhin zum Bild Produkt.Wählen Sie Bearbeiten. | Das Produkt wird im Bearbeitungsmodus angezeigt (die Felder sind eingabebereit). |  |
| 3 | Anlagen wählen | Wählen Sie auf dem Bild Produkt die Registerkarte Anlagen aus. | Die Registerkarte Anlagen wird angezeigt. |  |
| 4 | "Hochladen" wählen | Wählen Sie im Abschnitt Dokumentenverwaltung die Option Hochladen. | Ein Bild für den Datei-Upload wird angezeigt. |  |
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
| 2 | Materialgrunddaten eingeben | Nehmen Sie auf dem Bild Material anlegen (Einstieg), die folgenden Einträge vor:Material: <Materialnummer>Branche: MHinweis Ist das Eingabefeld Branche ausgeblendet, ist keine Eingabe erforderlich. Wird die Branche nicht zur Eingabe angeboten, wird nicht bekannt im Feld eingetragen.Materialart: FERTWählen Sie Sichtenauswahl. | Das Bild Sichtenauswahl wird angezeigt. |  |
| 3 | Sichten wählen | Wählen Sie im Fenster Sichtenauswahl die Option Grunddaten und Verkauf: Allg./Werksdaten aus, und wählen Sie dann Weiter. | Das Bild Organisationsebenen wird angezeigt. |  |
| 4 | Organisationsebenendaten eingeben | Nehmen Sie auf dem Bild "Organisationsebenen" im Abschnitt "Organisationsebene" die folgenden Einträge vor:Werk: <Werksnummer>Lagerort: <Lagerortnummer> | Das Bild Material... anlegen (Fertigerzeugnis) wird angezeigt. |  |
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
| 5 | "Werke – Allgemeine Daten" eingeben | Geben Sie im Abschnitt "Allgemeine Daten" folgende Daten ein:Werk: Werksnummer, z.B. 1710 |  |  |
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

In dieser Vorgehensweise erhalten Sie eine Anleitung zum Anlegen von Produktstammdaten. Die zur Verfügung stehenden Apps hängen von der Ihnen zugeordneten Rolle ab. Aus diesem Grund sind zwei Optionen verfügbar.

Voraussetzung

Sie müssen die vorherige Vorgehensweise ([Produktstammdaten anlegen – Grunddaten](#unique_11) [Seite ] 7) abschließen, bevor Sie mit diesem Abschnitt fortfahren können.

Folgen Sie der Vorgehensweise, nachdem Sie die eingegebenen Grunddaten gesichert haben, wie im vorherigen Kapitel erläutert.

Vorgehensweise: Option 1 – Material anlegen

Folgen Sie dieser Vorgehensweise, wenn Sie mit Ihrer Benutzerrolle auf die App Material anlegen(MM01) zugreifen können.

| Testschrittnummer | Bezeichnung des Testschritts | Anweisung | Erwartetes Ergebnis | Kommentare |
| --- | --- | --- | --- | --- |
| 1 | SAP-Fiori-App aufrufen | Öffnen Sie Material anlegen(MM01). | Die App wird geöffnet. |  |
| 2 | Materialgrunddaten eingeben | Nehmen Sie in Material anlegen (Einstiegssicht) die folgenden Einträge vor:Material: <Materialnummer>Branche: MHinweis Ist das Eingabefeld Branche ausgeblendet, ist keine Eingabe erforderlich. Wird die Branche nicht zur Eingabe angeboten, ist das Feld ausgegraut.Materialart: FERTWählen Sie Sichtenauswahl. | Das Bild Sichtenauswahl wird angezeigt. |  |
| 3 | Views auswählen | Wählen Sie auf dem Bild Sichtenauswahl die Sichten Grunddaten 1, Disposition 1 und Disposition 4 aus.Wählen Sie Weiter. | Das Bild Organisationsebenen wird angezeigt. |  |
| 4 | Organisationsebenendaten eingeben | Nehmen Sie auf dem Bild Organisationsebenen im Abschnitt Organisationsebenen die folgenden Einträge vor:Werk: <Werksnummer>Lagerort: <Lagerortnummer> | Das Bild Material anlegen (Handelswaren) wird angezeigt. |  |
| 5 | Daten in "Grunddaten 1" eingeben | Geben Sie im Bild Grunddaten 1 Folgendes ein, und drücken Sie Enter:Beschreibung: <Beschreibung des Produkts>Basismengeneinheit: Geben Sie die Basiseinheit ST ein, z.B. 1. |  |  |
| 6 | Daten in Disposition 1 eingeben | Nehmen Sie im Abschnitt Dispositionsverfahren die folgende Eingabe vor:Dispositionsmerkmal: z.B. ND |  |  |
| 7 | Daten in Disposition 4 eingeben | Geben Sie im Abschnitt Serienfertigung/Montage/Deployment-Strategie folgende Daten ein:Serienfertigung: Markieren Sie das Ankreuzfeld.Serienfertigungsprofil: <Wählen Sie einen beliebigen Wert aus der Wertehilfe aus> |  |  |
| 8 | Daten sichern | Wählen Sie Sichern. | Ihre Daten werden gesichert. |  |

Vorgehensweise: Option 2 – Produktstammdaten verwalten

Folgen Sie dieser Vorgehensweise, wenn Sie mit Ihrer Benutzerrolle auf die App Produktstammdaten verwalten(F1602) zugreifen können.

| Testschrittnummer | Bezeichnung des Testschritts | Anweisung | Erwartetes Ergebnis | Kommentare |
| --- | --- | --- | --- | --- |
| 1 | SAP-Fiori-App aufrufen | Wählen Sie Produktstammdaten verwalten(F1602). | Die App wird geöffnet. |  |
| 2 | Produkt suchen und zur Bearbeitung öffnen | Suchen Sie nach dem zuvor angelegten Produkt, indem Sie die Produktnummer im Suchfeld Produkt eingeben.Wählen Sie das Produkt aus der Liste aus. Sie gelangen daraufhin zum Bild Produkt.Wählen Sie Bearbeiten. | Das Produkt wird im Bearbeitungsmodus angezeigt (die Felder sind eingabebereit). |  |
| 3 | Werksdaten auswählen | Wählen Sie auf dem Bild Produkt die Option Werke. | Die Registerkarte Werke wird angezeigt. |  |
| 4 | "Anlegen" wählen | Wählen Sie auf der Registerkarte Werke die Option Anlegen. |  |  |
| 5 | "Werke – Allgemeine Daten" eingeben | Geben Sie im Abschnitt Allgemeine Daten folgende Daten ein:Werk: <Werksnummer>, z.B. 1710, |  |  |
| 6 | Dispositionsdaten eingeben | Nehmen Sie im Abschnitt Disposition die folgende Eingabe vor:Dispositionsmerkmal: z.B. ND |  |  |
| 7 | Serienfertigungsdaten eingeben | Geben Sie im Abschnitt Serienfertigung folgende Daten ein:Serienfertigung aktiviert: Markieren Sie das Ankreuzfeld, um das Feld Serienfertigungsprofil zu aktivieren.Serienfertigungsprofil: <Wählen Sie einen beliebigen Wert aus der Wertehilfe aus> | Wenn Sie das Ankreuzfeld Serienfertigung aktiviert markieren, sollte das Feld Serienfertigungsprofil editierbar sein.Wenn Sie das Ankreuzfeld Serienfertigung aktiviert entmarkieren, sollte das Feld Serienfertigungsprofil schreibgeschützt sein. |  |
| 8 | Zum Hauptbild zurückkehren | Wählen Sie Übernehmen, um zum Bild Produkt zurückzukehren. | Das Bild Produkt wird angezeigt. |  |
| 9 | Daten sichern | Wählen Sie Sichern. | Eine Systemmeldung bestätigt, dass das Objekt gesichert wurde. |  |

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
> Flagged while digesting this document, not verified: Basic data steps contradict slightly on missing industry field handling (one says 'nicht bekannt', others 'ausgegraut')

> [!warning] Conflict
> Flagged while digesting this document, not verified: Last two sections (Werksverkauf, Werk/Serienfertigung) leave expected results empty in the overview table and use 'Handelswaren' screen title despite FERT

> [!warning] Conflict
> Flagged while digesting this document, not verified: Tax classification text for Brazil/US is ambiguous in step listing (Steuerklassifikation listed twice)

## Connections
- part-of :: [[_cluster]]
- related-to :: [[02-business-partner-and-product-master-data/master-data-script-create-product-master-of-type-finished-good-sap-s-4]]
- related-to :: [[02-business-partner-and-product-master-data/sap-s-4hana-cloud-public-edition-bnt-675]]
- related-to :: [[02-business-partner-and-product-master-data/sap-s-4hana-cloud-public-edition-mds-bnt-673]]
- related-to :: [[02-business-partner-and-product-master-data/script-de-dados-mestre-criar-mestre-de-produtos-do-tipo-produto-acabad]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/BNT_S4CLD2608_Master_Data_DE_XX.docx` — full document · extracted with `mammoth` · 61,784 chars in the whole document
