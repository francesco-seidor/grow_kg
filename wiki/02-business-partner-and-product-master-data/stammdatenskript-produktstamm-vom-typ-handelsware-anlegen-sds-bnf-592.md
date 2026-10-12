---
id: 02-business-partner-and-product-master-data/stammdatenskript-produktstamm-vom-typ-handelsware-anlegen-sds-bnf-592
title: "Stammdatenskript: Produktstamm vom Typ „Handelsware“ anlegen – SDS (BNF) (BNF_S4CLD2608_Master_Data_DE_XX)"
description: "German SAP S/4HANA Cloud Public Edition 2608 master data test script for creating a trading goods (Handelsware) product master via MM01 or F1602, by data view."
cluster: 02-business-partner-and-product-master-data
tags: [kb/business-partner-and-product-master-data, topic/product-master-trading-goods]
aliases: [BNF_S4CLD2608_Master_Data_DE_XX]
keywords: ["Product Master: Trading Goods", product master, material master creation, sales data, purchasing data, mrp planning data, storage location data, accounting valuation data, configurable products, product attachments]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/BNF_S4CLD2608_Master_Data_DE_XX.docx]
confidence: low
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-592
topic: 02-business-partner-and-product-master-data/product-master-trading-goods
language: DE
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Stammdatenskript: Produktstamm vom Typ „Handelsware“ anlegen – SDS (BNF) (BNF_S4CLD2608_Master_Data_DE_XX)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/BNF_S4CLD2608_Master_Data_DE_XX.docx`, extracted with `mammoth`. Grouped under **Product Master: Trading Goods** in Business Partner and Product Master Data. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

| <!-- image omitted: unnamed --> | StammdatenskriptSAP S/4HANA Cloud Public Edition - 02-07-26 |
| --- | --- |
|  | Produktstamm vom Typ „Handelsware“ anlegen – SDS (BNF) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Inhaltsverzeichnis

[1 Verwendungszweck 2](#_Toc233889933)

[2 Voraussetzungen 3](#_Toc233889934)

[2.1 Systemzugriff 3](#_Toc233889935)

[2.2 Rollen 3](#_Toc233889936)

[2.3 Erforderliche Organisationseinheiten 3](#_Toc233889937)

[2.4 Obligatorische und operative Stammdaten 4](#_Toc233889938)

[2.5 Wesentliche Parameter für die Datenerstellung 5](#_Toc233889939)

[2.5.1 Materialart und Nummernkreise 5](#_Toc233889940)

[2.5.2 Branche 5](#_Toc233889941)

[3 Übersichtstabelle 6](#_Toc233889942)

[4 Testverfahren 7](#_Toc233889943)

[4.1 Materialstammdaten (Produktstammdaten) anlegen - Grunddaten 7](#_Toc233889944)

[4.2 Materialstammdaten (Produktstammdaten) anlegen – Verkaufsdaten (Umsatzsteuerdaten) 10](#_Toc233889945)

[4.3 Materialstammdaten (Produktstammdaten) anlegen – Einkaufsdaten 14](#_Toc233889946)

[4.4 Materialstammdaten (Produktstammdaten) anlegen – Dispositions-/Planungsdaten (Werksdaten) 16](#_Toc233889947)

[4.5 Materialstammdaten (Produktstammdaten) anlegen – Lagerortdaten 19](#_Toc233889948)

[4.6 Materialstammdaten (Produktstammdaten) anlegen – Buchhaltungsdaten (Bewertungsbereichsdaten) 22](#_Toc233889949)

[4.7 Produktstammdaten anlegen – Konfigurierbares Produkt und Varianten 25](#_Toc233889950)

[4.8 Produktstammdaten anlegen – Anlagen sichern 27](#_Toc233889951)

[4.9 Produktstammdaten anlegen – Werksverkauf/Allgemeine Daten 29](#_Toc233889952)

[4.10 Produktstammdaten anlegen – Werk/Serienfertigung 31](#_Toc233889953)

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

| Name (Rollenvorlage) | ID (Rollenvorlage) | Name (Launchpad-Bereich) | ID (Launchpad-Bereich) | Anmeldung |
| --- | --- | --- | --- | --- |
| Stammdatenexperte – Produktdaten | SAP_BR_PRODMASTER_SPECIALIST | Stammdaten – Produkte / Produkt-Governance | SAP_BR_PRODMASTER_SPECIALIST / SAP_CMD_SPT_PR_GOV_PC |  |

### Erforderliche Organisationseinheiten

Einige Segmente von Materialstammdaten hängen von den Organisationseinheiten des Unternehmens ab. Allgemeine (zentrale) Daten hängen nicht von einer Organisationseinheit oder dem Buchungskreis ab. Die folgende Tabelle stellt eine Übersicht dieser verschiedenen Datensegmente und ihrer relevanten Organisationseinheiten bereit:

| Datensegment | Hängt ab von | Feldbeispiele | Kommentare | Zu verwendende Organisationseinheit |
| --- | --- | --- | --- | --- |
| Grunddaten | Unabhängig von Organisationeinheiten | Materialbeschreibung (Kurztext), Materialnummer, Materialgruppe, Basismengeneinheit usw. | Grunddaten sind für einen Materialstammsatz nur einmal vorhanden. | Nicht zutreffend |
| Verkaufsdaten | Werk, Verkaufsorg., Vertriebsweg | Steuerdaten, Positionstypengruppe, TranspGruppe Gruppe, Ladegruppe, Rüstzeit usw. | Verkaufsdaten können für jede Verkaufsorganisation Ihrer Unternehmensstruktur vorhanden sein, für die der Materialstammsatz verwendet wird. | Werk:____________Verkaufsorganisation:__________Vertriebsweg:__________ |
| Einkaufsdaten | Werk | Einkäufergruppe, Materialgruppe, WE-Bearbeitungszeit usw. | Einkaufsdaten können für jede Einkaufsorganisation existieren, für die das Material in Einkaufsvorgängen verwendet werden soll. | Werk:__________ |
| Dispositions-/Planungsdaten | Werk, Lagerort | Dispositionsmerkmal, Disponent, Losgröße, Planlieferzeit usw. | Werksdaten können für jede Werks-ID Ihrer Unternehmensstruktur existieren, für die der Materialstammsatz verwendet wird.Lagerortdaten (Planungskontext) sind optional, abhängig von der Notwendigkeit, eine lagerortspezifische Planung durchzuführen. | Werk:____________Lagerort:__________ |
| Lagerortdaten | Werk, Lagerort | Anzahl WE-Scheine, Max. Lagerungszeit, Mindest- restlaufzeit usw. | Werksdaten können für jede Werks-ID Ihrer Unternehmensstruktur existieren, für die der Materialstammsatz verwendet wird.Lagerortdaten (Planungskontext) sind optional, abhängig von der Notwendigkeit, eine lagerortspezifische Planung durchzuführen. | Werk:____________Lagerort:__________ |
| Buchhaltungsdaten | Bewertungsbereich (= Werk), Bewertungsart | Bewertungsklasse, Per. VPreis, Preissteuerung usw. | Daten zum Bewertungsbereich können für jede Werks-ID Ihrer Unternehmensstruktur existieren, für die der Materialstammsatz verwendet wird. Jedes Werk stellt einen Bewertungsbereich dar (z.B. unterschiedliche Bewertungspreise eines Materials in verschiedenen Werken). | Werk:____________Bewertungsart:__________ |

### Obligatorische und operative Stammdaten

Materialstammdatensätze können auf andere Stammdaten verweisen. Die folgende Tabelle bietet eine Übersicht über die optionalen und obligatorischen Stammdatenobjekte, die in einem Materialstammdatensatz verwendet werden müssen.

|  |
| --- |
| Hinweis Für eine ordnungsgemäße Steuerberechnung sind brasilienspezifische Felder erforderlich.Prüfen Sie Nota Fiscal – Brasilien - JD0 im Kapitel BR-spezifische Felder für Stammdaten definieren für Materialstammdaten. |

| Stammdatenobjekt | Verwendet im Datensegment | Obligatorisch / optional | Kommentare |
| --- | --- | --- | --- |
| Profitcenter |  | obligatorisch | Für einwandfreie Bewertungsprozesse ist die Zuweisung eines Profitcenters zu einem Material- oder Produktstamm erforderlich. |

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

Dieser Umfangsbestandteil umfasst die verschiedenen Schritte in der folgenden Tabelle:

|  |
| --- |
| Hinweis Wenn Ihr Systemadministrator Bereiche und Seiten auf dem SAP Fiori Launchpad aktiviert hat, enthält die Startseite nur die wesentlichen Apps, mit denen die typischen Aufgaben einer Benutzerrolle ausgeführt werden können.Alle anderen (suchbaren) Apps, die nicht auf der Startseite enthalten sind, finden Sie über die Suchleiste ([2434549](https://me.sap.com/notes/2434549)).Wenn Sie die Startseite personalisieren und versteckte Apps hinzufügen möchten, wechseln Sie in Ihr Benutzerprofil und wählen Sie App Finder. |

| Prozessschritt | Benutzerrolle | Vorgang/App | Erwartete Ergebnisse |
| --- | --- | --- | --- |
| [Materialstammdaten (Produktstammdaten) anlegen - Grunddaten](#unique_11) [Seite ] 7 | Stammdatenexperte – Produktdaten | Material anlegen(MM01)/Produktstammdaten verwalten(F1602) | Materialstammdaten - Grunddaten werden angelegt. |
| [Materialstammdaten (Produktstammdaten) anlegen – Verkaufsdaten (Umsatzsteuerdaten)](#unique_12) [Seite ] 10 | Stammdatenexperte – Produktdaten | Material anlegen(MM01)/Produktstammdaten verwalten(F1602) | Materialstammdaten - Verkaufsdaten werden angelegt.. |
| [Materialstammdaten (Produktstammdaten) anlegen – Einkaufsdaten](#unique_13) [Seite ] 14 | Stammdatenexperte – Produktdaten | Material anlegen(MM01)/Produktstammdaten verwalten(F1602) | Materialstammdaten - Einkaufsdaten werden angelegt. |
| [Materialstammdaten (Produktstammdaten) anlegen – Dispositions-/Planungsdaten (Werksdaten)](#unique_14) [Seite ] 16 | Stammdatenexperte – Produktdaten | Material anlegen(MM01)/Produktstammdaten verwalten(F1602) | Materialstammdaten - Dispositions-/Planungsdaten werden angelegt. |
| [Materialstammdaten (Produktstammdaten) anlegen – Lagerortdaten](#unique_15) [Seite ] 19 | Stammdatenexperte – Produktdaten | Material anlegen(MM01)/Produktstammdaten verwalten(F1602) | Materialstammdaten - Lagerortdaten werden angelegt. |
| [Materialstammdaten (Produktstammdaten) anlegen – Buchhaltungsdaten (Bewertungsbereichsdaten)](#unique_16) [Seite ] 22 | Stammdatenexperte – Produktdaten | Material anlegen(MM01)/Produktstammdaten verwalten(F1602) | Materialstammdaten - Buchhaltungsdaten (Bewertungsbereichsdaten) werden angelegt. |
| [Produktstammdaten anlegen – Konfigurierbares Produkt und Varianten](#unique_17) [Seite ] 25 | Stammdatenexperte – Produktdaten | Material anlegen(MM01)/Produktstammdaten verwalten(F1602) | Konfigurierbares Produkt und Varianten anlegen |
| [Produktstammdaten anlegen – Anlagen sichern](#unique_18) [Seite ] 27 | Stammdatenexperte – Produktdaten | Material anlegen(MM01)/Produktstammdaten verwalten(F1602) | Anlagen zum Materialstammsatz sichern |
| [Produktstammdaten anlegen – Werksverkauf/Allgemeine Daten](#unique_19) [Seite ] 29 | Stammdatenexperte – Produktdaten | Material anlegen(MM01)/Produktstammdaten verwalten(F1602) |  |
| [Produktstammdaten anlegen – Werk/Serienfertigung](#unique_20) [Seite ] 31 | Stammdatenexperte – Produktdaten | Material anlegen(MM01)/Produktstammdaten verwalten(F1602) |  |

## Testverfahren

In diesem Abschnitt werden die Testverfahren für den jeweiligen Prozessschritt beschrieben, der zum betreffenden Umfangsbestandteil gehört.

### Materialstammdaten (Produktstammdaten) anlegen - Grunddaten

Testverwaltung

Kundenprojekt: Füllen Sie die projektbezogenen Teile aus.

|  |  |  |  |
| --- | --- | --- | --- |
| Testfall-ID | <X.XX> | Testdatum: |  |
| Testername: |  | Dauer: |  |
| Benutzerrolle(n): |  | Zuständigkeit: | <Geben Sie den Serviceanbieter, einen Kunden oder einen Serviceanbieter zusammen mit einem Kunden an.> |

Zweck

In dieser Vorgehensweise erhalten Sie eine Anleitung zum Anlegen von Stammdaten für Material (Produkt). Die zur Verfügung stehenden Apps hängen von der Ihnen zugeordneten Rolle ab. Aus diesem Grund sind zwei Optionen verfügbar.

Vorgehensweise: Option 1 – Material anlegen

Folgen Sie dieser Vorgehensweise, wenn Sie mit Ihrer Benutzerrolle auf die App Material anlegen(MM01) zugreifen können.

| Testschrittnummer | Bezeichnung des Testschritts | Anweisung | Erwartetes Ergebnis | Kommentare |
| --- | --- | --- | --- | --- |
| 1 | Anmelden | Melden Sie sich am SAP Fiori Launchpad als Stammdatenexperte – Produktdaten an. | Das SAP Fiori Launchpad wird angezeigt. |  |
| 2 | SAP-Fiori-App aufrufen | Öffnen Sie Material anlegen(MM01). | Die App wird geöffnet. |  |
| 3 | Materialgrunddaten eingeben | Nehmen Sie in Material anlegen (Einstiegssicht) die folgenden Einträge vor:Material: <Materialnummer>Branche: MHinweis Ist das Eingabefeld Branche ausgeblendet, ist keine Eingabe erforderlich. Wird die Branche nicht zur Eingabe angeboten, ist das Feld ausgegraut.Materialart: HandelswareWählen Sie Sichtenauswahl. | Das Bild Sichtenauswahl wird angezeigt. |  |
| 4 | Views auswählen | Wählen Sie auf dem Bild Sichtenauswahl die Sichten Grunddaten 1 und Grunddaten 2 aus.Wählen Sie Weiter. | Das Bild Material anlegen (Handelswaren) wird angezeigt. |  |
| 5 | Grunddaten eingeben | Geben Sie auf dem Bild Material ... (Handelswaren) auf der Registerkarte Grunddaten 1 die Materialbeschreibung (Kurztext) ein. |  |  |
| 6 | Grunddaten eingeben | Nehmen Sie auf der Registerkarte Grunddaten 1 im Abschnitt Allgemeine Daten die folgenden Einträge vor:Basismengeneinheit: <Basismengeneinheit>Warengruppe: <Warengruppe>Allg. PosTypGrp: <Allg. PosTypGrp> |  |  |
| 7 | Grunddaten eingeben | Nehmen Sie im Bereich Dimensionen/EANs die folgenden Einträge vor:Bruttogewicht: <Bruttogewicht>Gewichtseinheit: <Gewichtseinheit>Nettogewicht: <Nettogewicht>Drücken Sie Enter. | Die Registerkarte Grunddaten 2 wird angezeigt. |  |
| 8 | Grunddaten vervollständigen | Auf der Registerkarte Grunddaten 2 müssen Sie keine Einträge vornehmen. |  |  |
| 9 | Daten sichern | Wählen Sie Sichern, um Ihre Daten zu sichern. | Das Bild Material anlegen (Einstieg) wird geöffnet.Die Grunddaten werden erzeugt und gesichert. |  |

Vorgehensweise: Option 2 – Produktstammdaten verwalten

Folgen Sie dieser Vorgehensweise, wenn Sie mit Ihrer Benutzerrolle auf die App Produktstammdaten verwalten(F1602) zugreifen können.

| Testschrittnummer | Bezeichnung des Testschritts | Anweisung | Erwartetes Ergebnis | Kommentare |
| --- | --- | --- | --- | --- |
| 1 | Anmelden | Melden Sie sich am SAP Fiori Launchpad als Stammdatenexperte – Produktdaten an. | Das SAP Fiori Launchpad wird angezeigt. |  |
| 2 | SAP-Fiori-App aufrufen | Öffnen Sie Produktstammdaten verwalten(F1602). | Die App wird geöffnet. |  |
| 3 | "Produkt anlegen" wählen | Wählen Sie auf dem Bild Produktstammdaten verwalten die Option Produkt anlegen. | Das Bild Stammdatensatz anlegen wird angezeigt. |  |
| 4 | Daten in Pflichtfelder eingeben | Nehmen Sie auf dem Bild Stammdaten anlegen die folgenden Einträge vor:Produktnummer: z.B. Z … oder eine beliebige externe alphanumerische ID. Sie muss mit einem Zeichen beginnen, oder darf keinen Eintrag enthalten, dann legt das System automatisch eine alphanumerische ID an.Hinweis Weitere Informationen über Produktnummern finden Sie im Kapitel [Materialart und Nummernkreise](#unique_8) [Seite ] 5.Produktart: HandelswareProduktgruppe: z.B. L001Basismengeneinheit: z.B. StückBeschreibung: <beliebige Beschreibung> |  |  |
| 5 | Wählen Sie OK. | Wählen Sie auf dem Bild Produktstamm verwalten die Option OK. | Das Bild Produktstamm verwalten wird angezeigt. |  |
| 6 | Grunddaten eingeben | Navigieren Sie zum Bild Produktstamm verwalten > GRUNDDATEN > Grunddaten, und geben Sie folgende Daten ein:Sparte: z.B. 00 |  |  |
| 7 | "Anlegen" wählen | Navigieren Sie zum Bild Produktstamm verwalten > GRUNDDATEN > Beschreibung, und wählen Sie Anlegen. | Die Beschreibung in der Standardsprache (z.B. Deutsch) wird angezeigt |  |
| 8 | Beschreibungsdaten eingeben | Geben Sie auf dem Bild Beschreibungen folgende Daten ein:Sprache: z.B. DeutschProduktbeschreibung: <Produktbeschreibung> |  |  |
| 9 | Zum Hauptbild zurückkehren | Kehren Sie über das Pfeilsymbol "Zurück" zum Hauptbild zurück. | Das Bild Produktstamm wird angezeigt. |  |
| 10 | Basismengeneinheit auswählen | Navigieren Sie zu Produktstamm verwalten > GRUNDDATEN, und wählen Sie Mengeneinheit. |  |  |
| 11 | Zum Hauptbild zurückkehren | Kehren Sie über das Pfeilsymbol "Zurück" zum Hauptbild zurück. | Das Bild Produktstamm wird angezeigt. |  |
| 12 | Daten sichern | Wählen Sie Sichern. | Eine Systemmeldung bestätigt, dass das Objekt gesichert wurde. |  |

### Materialstammdaten (Produktstammdaten) anlegen – Verkaufsdaten (Umsatzsteuerdaten)

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

Sie müssen die vorherige Vorgehensweise ([Materialstammdaten (Produktstammdaten) anlegen - Grunddaten](#unique_11) [Seite ] 7) abschließen, bevor Sie mit diesem Abschnitt fortfahren können.

Folgen Sie der Vorgehensweise, nachdem Sie die eingegebenen Grunddaten gesichert haben, wie im vorherigen Kapitel erläutert.

Vorgehensweise: Option 1 – Material anlegen

Folgen Sie dieser Vorgehensweise, wenn Sie mit Ihrer Benutzerrolle auf die App Material anlegen(MM01) zugreifen können.

| Testschrittnummer | Bezeichnung des Testschritts | Anweisung | Erwartetes Ergebnis | Kommentare |
| --- | --- | --- | --- | --- |
| 1 | SAP-Fiori-App aufrufen | Öffnen Sie Material anlegen(MM01). | Die App wird geöffnet. |  |
| 2 | Materialgrunddaten eingeben | Nehmen Sie auf dem Bild Material anlegen (Einstieg) die folgenden Einträge vor:Material: <Materialnummer>Branche: MHinweis Ist das Eingabefeld Branche ausgeblendet, ist keine Eingabe erforderlich. Wird die Branche nicht zur Eingabe angeboten, ist das Feld ausgegraut.Materialart: HandelswareWählen Sie Sichtenauswahl. | Das Bild Sichtenauswahl wird angezeigt. |  |
| 3 | Views auswählen | Wählen Sie auf dem Bild Sichtenauswahl die Option Vertrieb: VerkaufsorgDaten 1, Vertrieb: VerkaufsorgDaten 2 und Vertrieb: allg./Werksdaten.Wählen Sie Weiter.Hinweis Nur für Polen: Wählen Sie außerdem Außenhandel - Exportdaten, um die PKWiU-Klassifikationsnummer einzugeben. | Das Bild Organisationsebenen wird angezeigt. |  |
| 4 | Organisationsebenendaten eingeben | Nehmen Sie auf dem Bild Organisationsebenen im Abschnitt Organisationsebenen die folgenden Einträge vor:WerkVerkaufsorg.Vertriebsweg KanalWählen Sie Weiter.Hinweis Die Systemmeldung Das Material existiert bereits und wird erweitert wird angezeigt. | Das Bild Material anlegen (Handelswaren) wird angezeigt. |  |
| 5 | Verkaufsdaten eingeben | Geben Sie auf dem Bild Material...(Handelswaren) auf der Registerkarte Verkauf: VerkOrg 1 im Bereich Allgemeine Daten folgende Einträge vor:BasismengeneinheitAuslieferungswerk |  |  |
| 6 | Verkaufsdaten eingeben | Geben Sie auf dem Bild Material...(Handelswaren) auf der Registerkarte Verkauf: VerkOrg 1 im Abschnitt Steuerdaten Folgendes ein:Steuerklassifikation: 1Hinweis Der eingegebene Wert zeigt an, dass das Material (für gewöhnlich) voll steuerpflichtig ist.Nur für Brasilien:Geben Sie im Abschnitt Steuerdaten Folgendes ein:Land: BRSteuerkategorie: IBRXSteuerklassifizierung: Entweder 1 für Material oder 2 für Dienstleistungen. | Die Registerkarte Verkauf: VerkOrg 2 wird angezeigt. |  |
| 7 | Verkaufsdaten eingeben | Nehmen Sie auf der Registerkarte Verkauf: Verkaufsorganisation 2 im Abschnitt Gruppierungsbegriffe den folgenden Eintrag vor:StatistikGrMaterialPositionstypengruppeKontierungsgr. Mat.: 01 | Die Registerkarte Verkauf: Allg./Werk wird angezeigt. |  |
| 8 | Verkaufsdaten eingeben | Nehmen Sie auf der Registerkarte Verkauf: Allg./Werk im Abschnitt Allgemeine Daten die folgenden Einträge vor:Verfügbarkeitsprüfung: SP |  |  |
| 9 | Verkaufsdaten eingeben | Nehmen Sie auf der Registerkarte Verkauf: Allg./Werk im Abschnitt Versanddaten (Zeiten in Tagen) folgende Einträge vor:Transp.- gruppe: <0001>Ladegruppe: <0001> |  |  |
| 10 | Verkaufsdaten eingeben | Nehmen Sie im Bereich Allgemeine Werksparameter folgende Einträge vor:Profitcenter: <Profitcenter>Hinweis Wählen Sie für Serialnummernprofil ein gültiges Serialnummernprofil aus, das mit dem richtigen Equipmenttyp für Ihr Unternehmen zugeordnet wurde. |  |  |
| Nur für Polen | Verkaufsdaten eingeben | Nur für Polen:Geben Sie im Abschnitt International Trade: Export die folgenden Daten ein:Steuerungscode: z.B. 26.70.13.0 | Der PKWiU-Code für Polen ist gepflegt. |  |
| 11 | Daten sichern | Wählen Sie Sichern. | Ihre Daten werden gesichert. |  |

Vorgehensweise: Option 2 – Produktstammdaten verwalten

Folgen Sie dieser Vorgehensweise, wenn Sie mit Ihrer Benutzerrolle auf die App Produktstammdaten verwalten(F1602) zugreifen können.

| Testschrittnummer | Bezeichnung des Testschritts | Anweisung | Erwartetes Ergebnis | Kommentare |
| --- | --- | --- | --- | --- |
| 1 | SAP-Fiori-App aufrufen | Öffnen Sie Produktstammdaten verwalten(F1602). | Die App wird geöffnet. |  |
| 2 | Produkt suchen und zur Bearbeitung öffnen | Suchen Sie nach dem zuvor angelegten Produkt, indem Sie die Produktnummer im Suchfeld Produkt eingeben.Wählen Sie das Produkt aus der Liste aus. Sie gelangen daraufhin zum Bild Produkt.Wählen Sie Bearbeiten. | Das Produkt wird im Bearbeitungsmodus angezeigt (die Felder sind eingabebereit). |  |
| 3 | Vertriebslinien auswählen | Wählen Sie auf dem Bild Produkt die Registerkarte Vertriebslinien. | Die Registerkarte Vertriebslinien wird angezeigt. |  |
| 4 | "+ (Hinzufügen)" wählen | Wählen Sie auf der Registerkarte Vertriebslinien die Option + (Hinzufügen). | Das Bild VERTRIEBSLINIEN wird im Bearbeitungsmodus geöffnet. |  |
| 5 | Vertriebsliniendaten eingeben | Geben Sie auf dem Bild Vertriebslinien folgende Daten ein:Im Abschnitt ALLGEMEINE DATEN - Allgemeine Informationen:Verkaufsorganisation: <Nummer der Verkaufsorganisation>Hinweis Der Organisationseinheitswert richtet sich nach den Optionen in der Wertehilfe.Vertriebsweg: z.B. 10Lieferwerk: <Werksnummer>Im Abschnitt GRUPPIERUNGSBEGRIFFE:Positionstypengruppe: z.B. NORMKontierungsgruppe: z.B. 01 HandelswarenIm Bildbereich UMSATZSTEUER:Land: <Ländercode>Steuerkategorie: Zum Beispiel TTX1.Steuerklassifikation: z.B. entweder 1 für Material oder 2 für Dienstleistungen.Steuerklassifikation: z.B. 1 volle Steuer, wenn Sie die Steuerkondition UTXJ für die USA verwenden.Hinweis Die Steuerklassifikation hängt von den spezifischen Anforderungen des jeweiligen Landes bzw. der Region ab. Die Steuerklassifikation in den Materialstamm- und Kundestammtabellen bestimmt die Eingaben der Prozentsätze.Nur für Brasilien:Nehmen Sie im Abschnitt Steuerklassifikation folgende Einträge vor:Land: BRSteuerkategorie: IBRXSteuerklassifikation: Entweder 1 für Material oder 2 für Dienstleistungen. |  |  |
| 6 | Zum Hauptbild zurückkehren | Wählen Sie Übernehmen, um zum Bild Produkt zurückzukehren. | Das Bild Produkt wird angezeigt. |  |
| 7 | Daten sichern | Wählen Sie Sichern. | Eine Systemmeldung bestätigt, dass das Objekt gesichert wurde. |  |

### Materialstammdaten (Produktstammdaten) anlegen – Einkaufsdaten

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

Sie müssen die vorherige Vorgehensweise ([Materialstammdaten (Produktstammdaten) anlegen - Grunddaten](#unique_11) [Seite ] 7) abschließen, bevor Sie mit diesem Abschnitt fortfahren können.

Folgen Sie der Vorgehensweise, nachdem Sie die eingegebenen Grunddaten gesichert haben, wie im vorherigen Kapitel erläutert.

Vorgehensweise: Option 1 – Material anlegen

Folgen Sie dieser Vorgehensweise, wenn Sie mit Ihrer Benutzerrolle auf die App Material anlegen(MM01) zugreifen können.

| Testschrittnummer | Bezeichnung des Testschritts | Anweisung | Erwartetes Ergebnis | Kommentare |
| --- | --- | --- | --- | --- |
| 1 | SAP-Fiori-App aufrufen | Öffnen Sie Material anlegen(MM01). | Die App wird geöffnet. |  |
| 2 | Materialgrunddaten eingeben | Nehmen Sie auf dem Bild Material anlegen (Einstieg) die folgenden Einträge vor:Material: <Materialnummer>Branche: MHinweis Ist das Eingabefeld Branche ausgeblendet, ist keine Eingabe erforderlich. Wird die Branche nicht zur Eingabe angeboten, ist das Feld ausgegraut.Materialart: HandelswareWählen Sie Sichtenauswahl. | Das Bild Sichtenauswahl wird angezeigt. |  |
| 3 | Views auswählen | Wählen Sie auf dem Bild Sichtenauswahl die Sicht Einkauf aus, und wählen Sie Weiter. | Das Bild Organisationsebenen wird angezeigt. |  |
| 4 | Organisationsebenendaten eingeben | Nehmen Sie auf dem Bild Organisationsebenen im Bereich Organisationsebene den folgenden Eintrag vor:Werk: <Werksnummer>Wählen Sie Weiter.Hinweis Die Systemmeldung Das Material existiert bereits und wird erweitert wird angezeigt. | Das Bild Material anlegen (Handelswaren) wird angezeigt. |  |
| 5 | Einkaufsdaten eingeben | Nehmen Sie auf dem Bild Material ... anlegen (Handelswaren) auf der Registerkarte Einkauf im Abschnitt Allgemeine Daten die folgenden Einträge vor:Basismengeneinheit: z.B. kgEinkäufergruppe: z.B. 001Warengruppe: z.B. L001 |  |  |
| 6 | Einkaufsdaten eingeben | Nehmen Sie im Bereich Sonstige Daten / Herstellerdaten den folgenden Eintrag vor:WE-Bearbeitungszeit: z.B. 1 |  |  |
| 7 | Daten sichern | Wählen Sie Sichern. | Ihre Daten werden gesichert. |  |

Vorgehensweise: Option 2 – Produktstammdaten verwalten

Folgen Sie dieser Vorgehensweise, wenn Sie mit Ihrer Benutzerrolle auf die App Produktstammdaten verwalten(F1602) zugreifen können.

| Testschrittnummer | Bezeichnung des Testschritts | Anweisung | Erwartetes Ergebnis | Kommentare |
| --- | --- | --- | --- | --- |
| 1 | SAP-Fiori-App aufrufen | Öffnen Sie Produktstammdaten verwalten(F1602). | Die App wird geöffnet. |  |
| 2 | Produkt suchen und zur Bearbeitung öffnen | Suchen Sie nach dem zuvor angelegten Produkt, indem Sie die Produktnummer im Suchfeld Produkt eingeben.Wählen Sie das Produkt aus der Liste aus. Sie gelangen daraufhin zum Bild Produkt.Wählen Sie Bearbeiten. | Das Produkt wird im Bearbeitungsmodus angezeigt (die Felder sind eingabebereit). |  |
| 3 | Einkaufsdaten auswählen | Wählen Sie in der Sicht Produkt die Option Einkauf. | Das Bild Einkaufsorganisation wird angezeigt. |  |
| 4 | Einkaufsdaten eingeben | Geben Sie auf dem Bild Einkauf folgende Daten ein:Einkaufswerteschlüssel: z.B. 1Status d. variablen Bestellmengeneinheit: AktivWählen Sie im Abschnitt der Kopfdaten die Option Kopf bearbeiten, und geben Sie folgende Daten ein:Produktgruppe: z.B. L001 |  |  |
| 5 | Daten sichern | Wählen Sie Sichern. | Eine Systemmeldung bestätigt, dass das Objekt gesichert wurde. |  |

### Materialstammdaten (Produktstammdaten) anlegen – Dispositions-/Planungsdaten (Werksdaten)

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

Sie müssen die vorherige Vorgehensweise ([Materialstammdaten (Produktstammdaten) anlegen - Grunddaten](#unique_11) [Seite ] 7) abschließen, bevor Sie mit diesem Abschnitt fortfahren können.

Folgen Sie der Vorgehensweise, nachdem Sie die eingegebenen Grunddaten gesichert haben, wie im vorherigen Kapitel erläutert.

Vorgehensweise: Option 1 – Material anlegen

Folgen Sie dieser Vorgehensweise, wenn Sie mit Ihrer Benutzerrolle auf die App Material anlegen(MM01) zugreifen können.

| Testschrittnummer | Bezeichnung des Testschritts | Anweisung | Erwartetes Ergebnis | Kommentare |
| --- | --- | --- | --- | --- |
| 1 | SAP-Fiori-App aufrufen | Öffnen Sie Material anlegen(MM01). | Die App wird geöffnet. |  |
| 2 | Materialgrunddaten eingeben | Nehmen Sie auf dem Bild Material anlegen (Einstieg) die folgenden Einträge vor:Material: <Materialnummer>Branche: MHinweis Ist das Eingabefeld Branche ausgeblendet, ist keine Eingabe erforderlich. Wird die Branche nicht zur Eingabe angeboten, ist das Feld ausgegraut.Materialart: HandelswareWählen Sie Sichtenauswahl. | Das Bild Sichtenauswahl wird angezeigt. |  |
| 3 | Views auswählen | Wählen Sie auf dem Bild Sichtenauswahl die Sichten Disposition 1, Disposition 2, Disposition 3 und Disposition 4 aus.Wählen Sie Weiter. | Das Bild Organisationsebenen wird angezeigt. |  |
| 4 | Organisationsebenendaten eingeben | Nehmen Sie auf dem Bild Organisationsebenen im Abschnitt Organisationsebenen die folgenden Einträge vor:Werk: <Werksnummer>Lagerort: <Lagerortnummer> | Das Bild Material anlegen (Handelswaren) wird angezeigt. |  |
| 5 | Dispositions-/Planungsdaten eingeben | Nehmen Sie auf dem Bild Material anlegen... (Handelswaren) auf der Registerkarte Disposition 1 im Abschnitt Allgemeine Daten die folgenden Einträge vor:Dispositionsmerkmal: PDDisponent: <001>Hinweis Die Systemmeldung Das Material existiert bereits und wird erweitert wird angezeigt. |  |  |
| 6 | Dispositions-/Planungsdaten eingeben | Nehmen Sie im Bereich Losgrößendaten den folgenden Eintrag vor:Losgrößenverfahren: <EX> | Die Registerkarte Disposition 2 wird angezeigt. |  |
| 7 | Dispositions-/Planungsdaten eingeben | Nehmen Sie auf dem Bild Material anlegen... (Handelswaren) auf der Registerkarte Disposition 2 im Abschnitt Planung die folgenden Einträge vor:Planlieferzeit: z.B. 3Wareneingang VerarbZeit : z.B. 1Horizontschlüssel: z.B. 000 | Die Registerkarte Disposition 3 wird angezeigt. |  |
| 8 | Dispositions-/Planungsdaten eingeben | Nehmen Sie auf dem Bild Material anlegen... (Handelswaren) auf der Registerkarte Disposition 3 im Abschnitt Planung die folgenden Einträge vor:Strategiegruppe: z.B. 40 |  |  |
| 9 | Dispositions-/Planungsdaten eingeben | Nehmen Sie im Bereich Verfügbarkeitsprüfung die folgenden Einträge vor:Verfügbarkeitsprüfung: z.B. SPGesamtwieder- beschaffungszeit z.B. 3 | Die Registerkarte Disposition 4 wird angezeigt. |  |
| 10 | Dispositions-/Planungsdaten eingeben | Nehmen Sie auf dem Bild Material anlegen... (Handelswaren) auf der Registerkarte Disposition 4 im Abschnitt Stücklistenauflösung/Sekundärbedarfe die folgenden Einträge vor:Einzel-/Sammelbedarf: 1 |  |  |
| 11 | Daten sichern | Wählen Sie Sichern. | Ihre Daten werden gesichert. |  |

Vorgehensweise: Option 2 – Produktstammdaten verwalten

Folgen Sie dieser Vorgehensweise, wenn Sie mit Ihrer Benutzerrolle auf die App Produktstammdaten verwalten(F1602) zugreifen können.

| Testschrittnummer | Bezeichnung des Testschritts | Anweisung | Erwartetes Ergebnis | Kommentare |
| --- | --- | --- | --- | --- |
| 1 | SAP-Fiori-App aufrufen | Öffnen Sie Produktstammdaten verwalten(F1602). | Die App wird geöffnet. |  |
| 2 | Produkt suchen und zur Bearbeitung öffnen | Suchen Sie nach dem zuvor angelegten Produkt, indem Sie die Produktnummer im Suchfeld Produkt eingeben.Wählen Sie das Produkt aus der Liste aus. Sie gelangen daraufhin zum Bild Produkt.Wählen Sie Bearbeiten. | Das Produkt wird im Bearbeitungsmodus angezeigt (die Felder sind eingabebereit). |  |
| 3 | Werksdaten auswählen | Wählen Sie auf dem Bild Produkt die Option Werke. | Die Registerkarte Werke wird angezeigt. |  |
| 4 | "Anlegen" wählen | Wählen Sie auf der Registerkarte Werke die Option Anlegen. | Das Bild Werk wird im Bearbeitungsmodus angezeigt. |  |
| 5 | Allgemeine Daten erfassen | Geben Sie im Abschnitt Allgemeine Daten Folgendes ein:Werk: <Werksnummer>, z.B. 1710,Profitcenter: Zum Beispiel YB700.Ladegruppe: z.B. 0001 |  |  |
| 6 | Dispositionsdaten eingeben | Navigieren Sie zum Abschnitt Dispositionsdaten > Dispositionsdaten, und nehmen Sie die folgenden Einträge vor:Verfügbarkeitsprüfung: z.B. SPDispositionsmerkmal: z.B. PDDisponent: z.B. 001 |  |  |
| 7 | Losgrößendaten erfassen | Geben Sie im Abschnitt Dispositionsdaten > Losgrößendaten folgende Daten ein:Losgrößenverfahren: z.B. EX |  |  |
| 8 | Beschaffungsdaten eingeben | Navigieren Sie zu Dispositionsdaten > Beschaffung, und geben Sie folgende Daten ein:Planlieferzeit: z.B. 3Wareneingangsbearbeitungszeit: z.B. 1 |  |  |
| 9 | Prognosedaten wählen | Wählen Sie auf dem Bild Werk die Registerkarte Prognose aus. | Die Registerkarte Prognose wird angezeigt. |  |
| 10 | Prognosedaten bearbeiten | Geben Sie auf der Registerkarte Prognose folgende Daten ein:Periodenart: z.B. monatlich |  |  |
| 11 | Zum Hauptbild zurückkehren | Wählen Sie Übernehmen, um zum Bild Produkt zurückzukehren. | Das Bild Produkt wird angezeigt. |  |
| 12 | Daten sichern | Wählen Sie Sichern. | Eine Systemmeldung bestätigt, dass das Objekt gesichert wurde. |  |

### Materialstammdaten (Produktstammdaten) anlegen – Lagerortdaten

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

Sie müssen die vorherige Vorgehensweise ([Materialstammdaten (Produktstammdaten) anlegen - Grunddaten](#unique_11) [Seite ] 7) abschließen, bevor Sie mit diesem Abschnitt fortfahren können.

Folgen Sie der Vorgehensweise, nachdem Sie die eingegebenen Grunddaten gesichert haben, wie im vorherigen Kapitel erläutert.

Vorgehensweise: Option 1 – Material anlegen

Folgen Sie dieser Vorgehensweise, wenn Sie mit Ihrer Benutzerrolle auf die App Material anlegen(MM01) zugreifen können.

| Testschrittnummer | Bezeichnung des Testschritts | Anweisung | Erwartetes Ergebnis | Kommentare |
| --- | --- | --- | --- | --- |
| 1 | SAP-Fiori-App aufrufen | Öffnen Sie Material anlegen(MM01). | Die App wird geöffnet. |  |
| 2 | Materialgrunddaten eingeben | Nehmen Sie auf dem Bild Material anlegen (Einstieg) die folgenden Einträge vor:Material: <Materialnummer>Branche: MHinweis Ist das Eingabefeld Branche ausgeblendet, ist keine Eingabe erforderlich. Wird die Branche nicht zur Eingabe angeboten, ist das Feld ausgegraut.Materialart: HandelswareWählen Sie Sichtenauswahl. | Das Bild Sichtenauswahl wird angezeigt. |  |
| 3 | Views auswählen | Wählen Sie im Fenster Sichtenauswahl die folgenden Sichten aus:Allg. Werksdaten / Lagerung 1Allg. Werksdaten / Lagerung 2Wählen Sie Weiter. | Das Bild Organisationsebenen wird angezeigt. |  |
| 4 | Organisationsebenendaten eingeben | Nehmen Sie auf dem Bild Organisationsebenen im Abschnitt Organisationsebene die folgenden Einträge vor:Werk: <Werksnummer>Lagerort: <Lagerortnummer>Hinweis Die Systemmeldung Das Material existiert bereits und wird erweitert wird angezeigt. | Das Bild Material anlegen (Handelswaren) wird angezeigt. |  |
| 5 | Lagerortdaten eingeben | Nehmen Sie auf dem Bild Material anlegen (Handelswaren) auf der Registerkarte Werksdaten/Lagerung 1 im Bereich Allgemeine Daten folgenden Eintrag vor:Anzahl WE-Scheine: z.B. 1 | Die Registerkarte Werksdaten/Lagerung2 wird angezeigt. |  |
| 6 | Eingaben bestätigen | Nehmen Sie auf der Registerkarte Werksdaten/Lagerung 2 keine Einträge vor.Hinweis Wählen Sie für das Feld Serialnummernprofil ein gültiges Serialnummernprofil aus, das mit dem richtigen Equipmenttyp für Ihr Unternehmen zugeordnet wurde. |  |  |
| 7 | Daten sichern | Wählen Sie Sichern. | Das Bild Stammdaten - Produkt wird angezeigt.Ihre Daten werden gesichert. |  |

Vorgehensweise: Option 2 – Produktstammdaten verwalten

Folgen Sie dieser Vorgehensweise, wenn Sie mit Ihrer Benutzerrolle auf die App Produktstammdaten verwalten(F1602) zugreifen können.

| Testschrittnummer | Bezeichnung des Testschritts | Anweisung | Erwartetes Ergebnis | Kommentare |
| --- | --- | --- | --- | --- |
| 1 | SAP-Fiori-App aufrufen | Öffnen Sie Produktstammdaten verwalten(F1602). | Die App wird geöffnet. |  |
| 2 | Produkt suchen und zur Bearbeitung öffnen | Suchen Sie nach dem zuvor angelegten Produkt, indem Sie die Produktnummer im Suchfeld Produkt eingeben.Wählen Sie das Produkt aus der Liste aus. Sie gelangen daraufhin zum Bild Produkt.Wählen Sie Bearbeiten. | Das Produkt wird im Bearbeitungsmodus angezeigt (die Felder sind eingabebereit). |  |
| 3 | Werksdaten auswählen | Wählen Sie auf dem Bild Produkt die Registerkarte Werke aus.Hinweis Wenn kein Werksdatensatz vorhanden ist, führen Sie die Schritte aus dem vorherigen Kapitel [Materialstammdaten (Produktstammdaten) anlegen – Dispositions-/Planungsdaten (Werksdaten)](#unique_14) [Seite ] 16 aus. | Die Registerkarte Werke wird angezeigt. |  |
| 4 | Werksdaten auswählen | Wählen Sie auf der Registerkarte Werke über das Pfeilsymbol die Werksdaten aus, die Sie im vorhergehenden Schritt angelegt haben. | Das Bild Werk wird angezeigt. |  |
| 5 | Zum Werk: Lagerorte | Navigieren Sie auf dem Bild Werk zu Lagerorte > Lagerorte. |  |  |
| 6 | "Anlegen" wählen | Navigieren Sie zu Lagerorte > Lagerorte, und wählen Sie Anlegen. | Das Bild Werk - Lagerort wird im Änderungsmodus geöffnet. |  |
| 7 | Werk eingeben: Lagerort" eingeben | Geben Sie im Bild Lagerort folgende Daten ein:Lagerort: <Lagerortnummer> |  |  |
| 8 | Zum Hauptbild zurückkehren | Wählen Sie zweimal Übernehmen, um zur Sicht Produkt zurückzukehren. | Das Bild Produkt wird angezeigt. |  |
| 9 | Daten sichern | Wählen Sie Sichern. | Eine Systemmeldung bestätigt, dass das Objekt gesichert wurde. |  |

### Materialstammdaten (Produktstammdaten) anlegen – Buchhaltungsdaten (Bewertungsbereichsdaten)

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

Sie müssen die vorherige Vorgehensweise ([Materialstammdaten (Produktstammdaten) anlegen - Grunddaten](#unique_11) [Seite ] 7) abschließen, bevor Sie mit diesem Abschnitt fortfahren können.

Folgen Sie der Vorgehensweise, nachdem Sie die eingegebenen Grunddaten gesichert haben, wie im vorherigen Kapitel erläutert.

Vorgehensweise: Option 1 – Material anlegen

Folgen Sie dieser Vorgehensweise, wenn Sie mit Ihrer Benutzerrolle auf die App Material anlegen(MM01) zugreifen können.

| Testschrittnummer | Bezeichnung des Testschritts | Anweisung | Erwartetes Ergebnis | Kommentare |
| --- | --- | --- | --- | --- |
| 1 | SAP-Fiori-App aufrufen | Öffnen Sie Material anlegen(MM01). | Die App wird geöffnet. |  |
| 2 | Materialgrunddaten eingeben | Nehmen Sie auf dem Bild Material anlegen (Einstieg), die folgenden Einträge vor:Material: <Materialnummer>Branche: MHinweis Ist das Eingabefeld Branche ausgeblendet, ist keine Eingabe erforderlich. Wird die Branche nicht zur Eingabe angeboten, ist das Feld ausgegraut.Materialart: HandelswareWählen Sie Sichtenauswahl. | Das Bild Sichtenauswahl wird angezeigt. |  |
| 3 | Sichten wählen | Wählen Sie im Fenster Sichtenauswahl die folgenden Sichten aus:Buchhaltung 1Buchhaltung 2Wählen Sie Weiter. | Das Bild Organisationsebenen wird angezeigt. |  |
| 4 | Organisationsebenendaten eingeben | Nehmen Sie auf dem Bild Organisationsebenen im Bereich Organisationsebene den folgenden Eintrag vor:Werk: <Werk>Hinweis Im unteren Teil des Bildes wird folgende Information angezeigt: Das Material existiert bereits und wird erweitert. | Das Bild Material anlegen (Handelswaren) wird angezeigt. |  |
| 5 | Buchhaltungsdaten eingeben | Nehmen Sie auf dem Bild Material anlegen (Handelswaren) auf der Registerkarte Buchhaltung 1 im Abschnitt Allgemeine Bewertungsdaten den folgenden Eintrag vor:Bewertungsklasse: <Nummer> |  |  |
| 6 | Daten eingeben | Nehmen Sie im Bereich Preise und Werte die folgenden Einträge vor:Per. VPreis: z.B. 20Preissteuerung: z.B. V | Die Registerkarte Buchhaltung 2 wird angezeigt. |  |
| 7 | Eingaben bestätigen | Auf der Registerkarte Buchhaltung 2 sind keine Eingaben erforderlich. |  |  |
| 8 | Daten sichern | Wählen Sie im unteren Bereich der Sicht die Option Sichern. | Das Bild Stammdaten - Produkt wird angezeigt.Ihre Daten werden gesichert. |  |

Vorgehensweise: Option 2 – Produktstammdaten verwalten

Folgen Sie dieser Vorgehensweise, wenn Sie mit Ihrer Benutzerrolle auf die App Produktstammdaten verwalten(F1602) zugreifen können.

| Testschrittnummer | Bezeichnung des Testschritts | Anweisung | Erwartetes Ergebnis | Kommentare |
| --- | --- | --- | --- | --- |
| 1 | SAP-Fiori-App aufrufen | Wählen Sie Produktstammdaten verwalten(F1602). | Die App wird geöffnet, und verschiedene Suchfelder werden angezeigt. |  |
| 2 | Produkt suchen und zur Bearbeitung öffnen | Suchen Sie nach dem zuvor angelegten Produkt, indem Sie Produktnummer im Suchfeld Produkt eingeben.Wählen Sie das Produkt aus der Liste aus. Sie gelangen daraufhin zur Sicht Produkt.Wählen Sie Bearbeiten. | Das Produkt wird im Bearbeitungsmodus angezeigt (die Felder sind eingabebereit). |  |
| 3 | Bewertungskreisdaten auswählen | Wählen Sie in der Sicht Produkt die Registerkarte Bewertungskreise. | Die Registerkarte Bewertungskreise wird angezeigt. |  |
| 4 | "Anlegen" wählen | Wählen Sie im Abschnitt Bewertungskreise die Option Anlegen. | Bewertung wird im Bearbeitungsmodus geöffnet. |  |
| 5 | Bewertungskreisdaten eingeben | Geben Sie in der Sicht Bewertung folgende Daten ein:Bewertungskreis: <Bewertungskreisnummer>Preissteuerungsfindung: 2Bewertungsklasse: z.B. 3100 |  |  |
| 6 | Aktuelle Bewertungskreisdaten eingeben | Wechseln Sie zum Bild BEWERTUNGSKREISE > Bewertung, und geben Sie die folgenden Daten ein:Bestandspreis: z.B. 20Preissteuerungskennzeichen: z.B. VHinweis Wenn Sie V als Preissteuerungskennzeichen eingeben, wird der unter "Bestandspreis" hinzugefügte Wert der gleitende Durchschnittspreis. Wenn Sie S als Preissteuerungskennzeichen eingeben, wird der unter "Bestandspreis" hinzugefügte Wert der Standardpreis. |  |  |
| 7 | Zum Hauptbild zurückkehren | Wählen Sie Übernehmen, um zur Sicht Produkt zurückzukehren. | Die Sicht Produktstamm verwalten wird angezeigt. |  |
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

In dieser Vorgehensweise erhalten Sie eine Anleitung zum Anlegen von Produktstammdaten. Die zur Verfügung stehenden Apps hängen von der Ihnen zugeordneten Rolle ab. Aus diesem Grund sind zwei Optionen verfügbar.

Voraussetzung

Sie müssen die vorherige Vorgehensweise ([Materialstammdaten (Produktstammdaten) anlegen - Grunddaten](#unique_11) [Seite ] 7) abschließen, bevor Sie mit diesem Abschnitt fortfahren können.

Folgen Sie der Vorgehensweise, nachdem Sie die eingegebenen Grunddaten gesichert haben, wie im vorherigen Kapitel erläutert.

Vorgehensweise: Option 1 – Material anlegen

Folgen Sie dieser Vorgehensweise, wenn Sie mit Ihrer Benutzerrolle auf die App Material anlegen(MM01) zugreifen können.

| Testschrittnummer | Bezeichnung des Testschritts | Anweisung | Erwartetes Ergebnis | Bestanden/Nicht bestanden/Anmerkung |
| --- | --- | --- | --- | --- |
| 1 | SAP-Fiori-App aufrufen | Öffnen Sie Material anlegen(MM01). | Die App wird geöffnet. |  |
| 2 | Materialgrunddaten eingeben | Nehmen Sie auf dem Bild Material anlegen (Einstieg) die folgenden Einträge vor:Material: <Materialnummer>Branche: MHinweis Ist das Eingabefeld Branche ausgeblendet, ist keine Eingabe erforderlich. Wird die Branche nicht zur Eingabe angeboten, ist das Feld ausgegraut.Materialart: HandelswareWählen Sie Sichtenauswahl. | Das Bild Sichtenauswahl wird angezeigt. |  |
| 3 | Views auswählen | Wählen Sie auf dem Bild Sichtenauswahl die folgenden Sichten aus, und wählen Sie Weiter:Grunddaten 1Grunddaten 2Klassifizierung |  |  |
| 4 | Grunddaten eingeben | Geben Sie auf dem Bild Material (Fertigerzeugnis) auf der Registerkarte Grunddaten 1 die Materialbeschreibung (Kurztext) und die Basismengeneinheit ein.Drücken Sie Enter. | Die Registerkarte Grunddaten 2 wird angezeigt. |  |
| 5 | Grunddaten eingeben | Markieren Sie auf der Registerkarte Grunddaten 2 das Ankreuzfeld Material ist konfigurierbar.Drücken Sie Enter. | Die Registerkarte Klassifizierung wird angezeigt, und das Dialogfenster Klassenart wird eingeblendet. |  |
| 6 | Klassenart auswählen | Wählen Sie im Dialogfenster Klassenart die Klassenart 300 (Variante) aus, und wählen Sie Weiter. | Das Bild Klassifizierung wird angezeigt. |  |
| 7 | Klasse zuordnen | Ordnen Sie im Abschnitt Zuordnung eine Klasse zu, und wählen Sie Enter. | Die entsprechenden Merkmale werden unterhalb des Abschnitts Zuordnung angezeigt. |  |
| 8 | Merkmalswerte auswählen | Wählen Sie die gewünschten Werte für die Merkmale aus. |  |  |
| 9 | Daten sichern | Wählen Sie Sichern. | Das konfigurierbare Material wird angelegt. |  |
| 10 | Variante anlegen | Zum Anlegen einer Variante öffnen Sie erneut die Kachel Material anlegen(MM01) und führen die oben beschriebenen Schritte zum Anlegen eines neuen Materials mit Grunddaten 1 und Grunddaten 2 aus. |  |  |
| 11 | Variante anlegen | Wechseln Sie auf der Registerkarte Grunddaten 2 zu Mandantenspezifische Konfiguration, und geben Sie im Feld Werksüberg.konf.Mat. das zuvor angelegte konfigurierbare Material ein. Wählen Sie anschließend Variante einstellen, und wählen Sie den gewünschten Merkmalswert zum Konfigurieren der Varianten aus. | Die Variante wird angelegt. |  |

Vorgehensweise: Option 2 – Produktstammdaten verwalten

Folgen Sie dieser Vorgehensweise, wenn Sie mit Ihrer Benutzerrolle auf die App Produktstammdaten verwalten(F1602) zugreifen können.

| Testschrittnummer | Bezeichnung des Testschritts | Anweisung | Erwartetes Ergebnis | Bestanden/Nicht bestanden/Anmerkung |
| --- | --- | --- | --- | --- |
| 1 | SAP-Fiori-App aufrufen | Öffnen Sie Produktstammdaten verwalten(F1602). | Die App wird geöffnet. |  |
| 2 | Produkt suchen und zur Bearbeitung öffnen | Suchen Sie nach dem zuvor angelegten Produkt, indem Sie die Produktnummer im Suchfeld Produkt eingeben.Wählen Sie das Produkt aus der Liste aus. Sie gelangen daraufhin zum Bild Produkt.Wählen Sie Bearbeiten. | Das Produkt wird im Bearbeitungsmodus angezeigt (die Felder sind eingabebereit). |  |
| 3 | Produkt als konfigurierbar kennzeichnen | Wechseln Sie auf dem Bild Produkt zur Registerkarte Konfiguration, und markieren Sie das Ankreuzfeld Produkt ist konfigurierbar. |  |  |
| 4 | Variantenklasse zuordnen | Wechseln Sie auf dem Bild Produkt zur Registerkarte Klassifizierung, wählen Sie Klicken Sie hier, um eine Klasse zuzuordnen., und wählen Sie anschließend eine Klasse der Klassenart 300 (Variante) aus. | Die Merkmale der zugeordneten Klasse werden angezeigt. |  |
| 5 | "Merkmale" wählen | Wählen Sie für jedes Merkmal die gewünschten Merkmalswerte aus. |  |  |
| 6 | Zur Registerkarte "Varianten" wechseln | Wechseln Sie auf dem Bild Produkt zur Registerkarte Varianten, und wählen Sie Produktvarianten auswählen. | Ein Baum oder eine Tabelle mit den verschiedenen Merkmalen wird angezeigt. |  |
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

Sie müssen die vorherige Vorgehensweise ([Materialstammdaten (Produktstammdaten) anlegen - Grunddaten](#unique_11) [Seite ] 7) abschließen, bevor Sie mit diesem Abschnitt fortfahren können.

Folgen Sie der Vorgehensweise, nachdem Sie die eingegebenen Grunddaten gesichert haben, wie im vorherigen Kapitel erläutert.

Vorgehensweise: Option 1 – Material anlegen

Folgen Sie dieser Vorgehensweise, wenn Sie mit Ihrer Benutzerrolle auf die App Material anlegen(MM01) zugreifen können.

| Testschrittnummer | Bezeichnung des Testschritts | Anweisung | Erwartetes Ergebnis | Bestanden/Nicht bestanden/Anmerkung |
| --- | --- | --- | --- | --- |
| 1 | SAP-Fiori-App aufrufen | Öffnen Sie Material anlegen(MM01). | Die App wird geöffnet. |  |
| 2 | Materialgrunddaten eingeben | Nehmen Sie auf dem Bild Material anlegen (Einstieg) die folgenden Einträge vor:Material: <Materialnummer>Branche: MHinweis Ist das Eingabefeld Branche ausgeblendet, ist keine Eingabe erforderlich. Wird die Branche nicht zur Eingabe angeboten, ist das Feld ausgegraut.Materialart: HandelswareWählen Sie Sichtenauswahl. | Das Bild Sichtenauswahl wird angezeigt. |  |
| 3 | Views auswählen | Wählen Sie auf dem Bild Sichtenauswahl die Sichten Grunddaten 1 und Grunddaten 2 aus.Wählen Sie Weiter. | Das Bild Material anlegen (Fertigerzeugnis) wird angezeigt. |  |
| 4 | Dienste zum Objekt wählen | Navigieren Sie auf Drucktastenleiste zu Dienste zum Objekt > Anlage anlegen. | Das Bild Datei importieren wird angezeigt. |  |
| 5 | "Hochladen" wählen | Wählen Sie auf dem Bild Datei importieren die Option Hochladen. | Ein Bild für den Datei-Upload wird angezeigt. |  |
| 6 | Anlage hochladen | Wählen Sie die Datei aus, und wählen Sie Öffnen. | Die Datei wird hochgeladen. |  |
| 7 | Sichern | Wählen Sie Auswählen und Sichern. | Eine Systemmeldung bestätigt, dass das Objekt gesichert wurde. |  |

Vorgehensweise: Option 2 – Produktstammdaten verwalten

Folgen Sie dieser Vorgehensweise, wenn Sie mit Ihrer Benutzerrolle auf die App Produktstammdaten verwalten(F1602) zugreifen können.

| Testschrittnummer | Bezeichnung des Testschritts | Anweisung | Erwartetes Ergebnis | Bestanden/Nicht bestanden/Anmerkung |
| --- | --- | --- | --- | --- |
| 1 | SAP-Fiori-App aufrufen | Wählen Sie Produktstammdaten verwalten(F1602). | Die App wird geöffnet. |  |
| 2 | Produkt suchen und zur Bearbeitung öffnen | Suchen Sie nach dem zuvor angelegten Produkt, indem Sie die Produktnummer im Suchfeld Produkt eingeben.Wählen Sie das Produkt aus der Liste aus. Sie gelangen daraufhin zum Bild Produkt.Wählen Sie Bearbeiten. | Das Produkt wird im Bearbeitungsmodus angezeigt (die Felder sind eingabebereit). |  |
| 3 | Anlagen wählen | Wählen Sie auf dem Bild Produkt die Registerkarte Anlagen aus. | Die Registerkarte Anlagen wird angezeigt. |  |
| 4 | "Anlegen" wählen | Wählen Sie im Abschnitt Dokumentenverwaltung die Option Anlegen. | Ein Bild für den Datei-Upload wird angezeigt. |  |
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

In dieser Vorgehensweise erhalten Sie eine Anleitung zum Anlegen von Stammdaten für Material (Produkt). Die zur Verfügung stehenden Apps hängen von der Ihnen zugeordneten Rolle ab. Aus diesem Grund sind zwei Optionen verfügbar.

Voraussetzung

Sie müssen die vorherige Vorgehensweise ([Materialstammdaten (Produktstammdaten) anlegen - Grunddaten](#unique_11) [Seite ] 7) abschließen, bevor Sie mit diesem Abschnitt fortfahren können.

Folgen Sie der Vorgehensweise, nachdem Sie die eingegebenen Grunddaten gesichert haben, wie im vorherigen Kapitel erläutert.

Vorgehensweise: Option 1 – Material anlegen

Folgen Sie dieser Vorgehensweise, wenn Sie mit Ihrer Benutzerrolle auf die App Material anlegen(MM01) zugreifen können.

| Testschrittnummer | Bezeichnung des Testschritts | Anweisung | Erwartetes Ergebnis | Kommentare |
| --- | --- | --- | --- | --- |
| 1 | SAP-Fiori-App aufrufen | Öffnen Sie Material anlegen(MM01). | Die App wird geöffnet. |  |
| 2 | Materialgrunddaten eingeben | Nehmen Sie auf dem Bild Material anlegen (Einstieg) die folgenden Einträge vor:Material: <Materialnummer>Branche: MHinweis Ist das Eingabefeld Branche ausgeblendet, ist keine Eingabe erforderlich. Wird die Branche nicht zur Eingabe angeboten, ist das Feld ausgegraut.Materialart: HandelswareWählen Sie Sichtenauswahl. | Das Bild Sichtenauswahl wird angezeigt. |  |
| 3 | Views auswählen | Wählen Sie im Fenster Sichtenauswahl die Option Grunddaten und Verkauf: All./Werksdaten.Wählen Sie Weiter. | Das Bild Organisationsebenen wird angezeigt. |  |
| 4 | Organisationsebenendaten eingeben | Nehmen Sie auf dem Bild Organisationsebenen im Abschnitt Organisationsebenen die folgenden Einträge vor:Werk: <Werksnummer>Lagerort: <Lagerortnummer> | Das Bild Material anlegen (Handelswaren) wird angezeigt. |  |
| 5 | Daten auf Sicht "Grunddaten 1" eingeben | Geben Sie im Bild Grunddaten 1 Folgendes ein, und drücken Sie Enter:Beschreibung: <Beschreibung des Produkts>Basismengeneinheit: Geben Sie die Basiseinheit ST ein, z.B. 1. |  |  |
| 6 | Daten eingeben | Geben Sie im Abschnitt Versanddaten (Zeiten in Tagen) die folgenden Daten ein:Ladegruppe: <Wählen Sie einen beliebigen Wert aus der Wertehilfe aus> |  |  |
| 7 | Daten sichern | Wählen Sie Sichern. | Ihre Daten werden gesichert. |  |

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
| 7 | "Werk – Verkauf" eingeben | Geben Sie im Bereich Vertrieb folgende Daten ein:Ladegruppe: <Wählen Sie einen Wert aus der Wertehilfe> |  |  |
| 8 | Zum Hauptbild zurückkehren | Wählen Sie Übernehmen, um zum Bild Produkt zurückzukehren. | Das Bild Produkt wird angezeigt. |  |
| 9 | Daten sichern | Wählen Sie Sichern. | Eine Systemmeldung bestätigt, dass das Objekt gesichert wurde. |  |

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

Sie müssen die vorherige Vorgehensweise ([Materialstammdaten (Produktstammdaten) anlegen - Grunddaten](#unique_11) [Seite ] 7) abschließen, bevor Sie mit diesem Abschnitt fortfahren können.

Folgen Sie der Vorgehensweise, nachdem Sie die eingegebenen Grunddaten gesichert haben, wie im vorherigen Kapitel erläutert.

Vorgehensweise: Option 1 – Material anlegen

Folgen Sie dieser Vorgehensweise, wenn Sie mit Ihrer Benutzerrolle auf die App Material anlegen(MM01) zugreifen können.

| Testschrittnummer | Bezeichnung des Testschritts | Anweisung | Erwartetes Ergebnis | Kommentare |
| --- | --- | --- | --- | --- |
| 1 | SAP-Fiori-App aufrufen | Öffnen Sie Material anlegen(MM01). | Die App wird geöffnet. |  |
| 2 | Materialgrunddaten eingeben | Nehmen Sie auf dem Bild Material anlegen (Einstieg) die folgenden Einträge vor:Material: <Materialnummer>Branche: MHinweis Ist das Eingabefeld Branche ausgeblendet, ist keine Eingabe erforderlich. Wird die Branche nicht zur Eingabe angeboten, ist das Feld ausgegraut.Materialart: HandelswareWählen Sie Sichtenauswahl. | Das Bild Sichtenauswahl wird angezeigt. |  |
| 3 | Views auswählen | Wählen Sie auf dem Bild Sichtenauswahl die Sichten Grunddaten 1, Disposition 1 und Disposition 4 aus.Wählen Sie Weiter. | Das Bild Organisationsebenen wird angezeigt. |  |
| 4 | Organisationsebenendaten eingeben | Nehmen Sie auf dem Bild Organisationsebenen im Abschnitt Organisationsebenen die folgenden Einträge vor:Werk: <Werksnummer>Lagerort: <Lagerortnummer> | Das Bild Material anlegen (Handelswaren) wird angezeigt. |  |
| 5 | Daten in "Grunddaten 1" eingeben | Geben Sie im Bild Grunddaten 1 Folgendes ein, und drücken Sie Enter:Beschreibung: <Beschreibung des Produkts>Basismengeneinheit: Geben Sie die Basiseinheit ST ein, z.B. 1. |  |  |
| 6 | Daten in Disposition 1 eingeben | Nehmen Sie im Abschnitt Dispositionsverfahren die folgende Eingabe vor:Dispositionsmerkmal: z.B. ND |  |  |
| 7 | Daten in Disposition 4 eingeben | Geben Sie im Abschnitt Serienfertigung/Montage/Deployment-Strategie folgende Daten ein:Serien fertigung: Markieren Sie das Ankreuzfeld.Serienfertigungsprofil: <Wählen Sie einen beliebigen Wert aus der Wertehilfe aus> |  |  |
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
> Flagged while digesting this document, not verified: Section titles say Handelsware but some steps reference Fertigerzeugnis screens (configurable product, attachments); Option 1 sections also use Materialart Handelsware throughout.

> [!warning] Conflict
> Flagged while digesting this document, not verified: Last two sections (Werksverkauf, Serienfertigung) have empty expected results in the overview table.

## Connections
- part-of :: [[_cluster]]
- related-to :: [[02-business-partner-and-product-master-data/master-data-script-create-product-master-of-type-trading-good-mds-bnf]]
- related-to :: [[02-business-partner-and-product-master-data/mds-bnf-597]]
- related-to :: [[02-business-partner-and-product-master-data/sap-s-4hana-cloud-public-edition-bnf-595]]
- related-to :: [[02-business-partner-and-product-master-data/script-de-dados-mestre-criar-mestre-de-produtos-do-tipo-produto-comerc]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/BNF_S4CLD2608_Master_Data_DE_XX.docx` — full document · extracted with `mammoth` · 65,684 chars in the whole document
