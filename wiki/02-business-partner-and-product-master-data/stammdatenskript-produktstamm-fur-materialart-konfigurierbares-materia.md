---
id: 02-business-partner-and-product-master-data/stammdatenskript-produktstamm-fur-materialart-konfigurierbares-materia
title: "Stammdatenskript: Produktstamm für Materialart \"Konfigurierbares Material\" anlegen – MDS (2T7) (2T7_S4CLD2608_Master_Data_DE_XX)"
description: "German SAP S/4HANA Cloud Public Edition 2608 master data script (2T7): test steps to create a KMAT configurable material master via MM01 or F1602."
cluster: 02-business-partner-and-product-master-data
tags: [kb/business-partner-and-product-master-data, topic/variant-configuration-master-data]
aliases: [2T7_S4CLD2608_Master_Data_DE_XX]
keywords: [Configurable Materials and Characteristic Display, configurable material, product master data, material master basic data, sales and tax data, mrp planning data, valuation accounting data, purchasing data, classification, work scheduling]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/2T7_S4CLD2608_Master_Data_DE_XX.docx]
confidence: low
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-280
topic: 02-business-partner-and-product-master-data/variant-configuration-master-data
language: DE
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Stammdatenskript: Produktstamm für Materialart "Konfigurierbares Material" anlegen – MDS (2T7) (2T7_S4CLD2608_Master_Data_DE_XX)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/2T7_S4CLD2608_Master_Data_DE_XX.docx`, extracted with `mammoth`. Grouped under **Configurable Materials and Characteristic Display** in Business Partner and Product Master Data. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

| <!-- image omitted: unnamed --> | StammdatenskriptSAP S/4HANA Cloud Public Edition - 02-07-26 |
| --- | --- |
|  | Produktstamm für Materialart "Konfigurierbares Material" anlegen – MDS (2T7) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Inhaltsverzeichnis

[1 Zweck 2](#_Toc233889583)

[2 Voraussetzungen 3](#_Toc233889584)

[2.1 Systemzugriff 3](#_Toc233889585)

[2.2 Rollen 3](#_Toc233889586)

[2.3 Voraussetzungen/Situation 3](#_Toc233889587)

[2.4 Erforderliche Organisationseinheiten 4](#_Toc233889588)

[2.5 Obligatorische und optionale Stammdaten 5](#_Toc233889589)

[2.6 Wesentliche Parameter für die Datenerstellung 5](#_Toc233889590)

[2.6.1 Materialart und Nummernkreise 5](#_Toc233889591)

[2.6.2 Branche 6](#_Toc233889592)

[3 Übersichtstabelle 7](#_Toc233889593)

[4 Testverfahren 8](#_Toc233889594)

[4.1 Produktstammdaten anlegen – Grunddaten 8](#_Toc233889595)

[4.2 Produktstammdaten anlegen – Verkaufsdaten / Umsatzsteuerdaten 11](#_Toc233889596)

[4.3 Produktstammdaten anlegen – Einkaufsdaten 14](#_Toc233889597)

[4.4 Produktstammdaten anlegen – Klassifikation 16](#_Toc233889598)

[4.5 Produktstammdaten anlegen - Dispositions-/Planungsdaten/Werksdaten 18](#_Toc233889599)

[4.6 Produktstammdaten anlegen – Arbeitsvorbereitung 22](#_Toc233889600)

[4.7 Produktstammdaten anlegen - Lagerortdaten 24](#_Toc233889601)

[4.8 Produktstammdaten anlegen – Buchhaltungsdaten / Bewertungsbereichsdaten 27](#_Toc233889602)

[4.9 Produktstammdaten anlegen – Kalkulation 30](#_Toc233889603)

## Zweck

Der Material- oder Produktstamm enthält Informationen über alle physischen Materialien, die beschafft, gefertigt, gelagert und verkauft werden. Er wird auch verwendet, um Informationen über Dienstleistungen zu verwalten, zum Beispiel für den Einkauf und Verkauf von Dienstleistungen in Stunden.

Der Materialstamm enthält Informationen wie die eindeutige Materialnummer, Name, Materialart, Mengeneinheit, Beschreibungen, Gewicht und Abmessungen. Diese Materialinformationen werden in Transaktionen wie Kundenaufträgen, Lieferungen, Bestellungen und Warenbewegungen verwendet und gespeichert.

Da alle Informationen für ein Material zentral gespeichert werden, sind die Materialstamminformationen in verschiedenen Ansichten organisiert. z.B. Vertrieb, Lager, Materialbedarfsplanung, Kalkulation und Buchhaltung.

Einige Informationen zu den einzelnen Materialien sind spezifisch für bestimmte Organisationseinheiten. Eine Verkaufskonfiguration z.B. ist verkaufseinheitsspezifisch (sogenannte Vertriebsbereiche), ein Disponent ist produktionsstättenspezifisch (sogenannte Werke) oder andere Informationen sind lagerortspezifisch.

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

### Voraussetzungen/Situation

Um dieses Stammdatenskript testen zu können, muss die folgende Voraussetzung erfüllt sein.

|  |
| --- |
| Hinweis Voraussetzung für dieses Stammdatenskript ist Umfangsbestandteil 22T - Konfigurierbares Modell mithilfe der Variantenkonfiguration einrichten. |

### Erforderliche Organisationseinheiten

Einige Segmente von Materialstammdaten hängen von den Organisationseinheiten des Unternehmens ab. Allgemeine (zentrale) Daten hängen nicht von einer Organisationseinheit oder dem Buchungskreis ab. Die folgende Tabelle stellt eine Übersicht dieser verschiedenen Datensegmente und ihrer relevanten Organisationseinheiten bereit:

| Datensegment | Hängt ab von | Feldbeispiele | Kommentare | Zu verwendende Organisationseinheit |
| --- | --- | --- | --- | --- |
| Grunddaten | Unabhängig von Organisationeinheiten | Materialbeschreibung (Kurztext), Materialnummer, Materialgruppe, Basismengeneinheit usw. | Gunddaten existieren für einen Materialstammsatz nur einmal. | Nicht zutreffend |
| Klassifizierung | Unabhängig von Organisationeinheiten | Klassenart, Klasse und Klassenwerte | Klassifikationsdaten existieren für die Klassenart, für die Klassifizierungsdaten verwendet werden. | Nicht zutreffend |
| Verkaufsdaten | Werk, Verkaufsorg., Vertriebsweg | Steuerdaten, Positionstypengruppe, TranspGruppe Gruppe, Ladegruppe, Rüstzeit usw. | Werksdaten können für jede Werks-ID Ihrer Unternehmensstruktur existieren, für die der Materialstammsatz verwendet wird. | Werk:____________Verkaufsorganisation:__________Vertriebsweg:__________ |
| Einkaufsdaten | Werk | Basismengeneinheit, Materialgruppe | Werksdaten können für jede Werks-ID Ihrer Unternehmensstruktur existieren, für die der Materialstammsatz verwendet wird. | Werk:____________ |
| Dispositionsdaten/Planungsdaten (Werksdaten) | Werk, Lagerort | Dispositionsmerkmal, Disponent, Losgröße, Planlieferzeit usw. | Werksdaten können für jede Werks-ID Ihrer Unternehmensstruktur existieren, für die der Materialstammsatz verwendet wird.Lagerortdaten (Planungskontext) sind optional, abhängig von der Notwendigkeit, eine lagerortspezifische Planung durchzuführen. | Werk:____________Lagerort:__________ |
| Arbeitsvorbereitung | Werk | Fertigungssteuerer und Fertigungssteuerungsprofil | Werksdaten können für jede Unternehmensstruktur existieren, für die der Materialstammsatz verwendet wird. | Werk:_____________ |
| Lagerortdaten | Werk, Lagerort | Anzahl WE-Scheine, Max. Lagerungszeit, Mindestlaufzeit usw. |  | Werk:____________Lagerort:__________ |
| Buchhaltungsdaten (Bewertungsdaten) | Bewertungsbereich (= Werk), Bewertungsart | Bewertungsklasse, Per. VPreis, Preissteuerung usw. | Daten zum Bewertungsbereich können für jede Werks-ID Ihrer Unternehmensstruktur existieren, für die der Materialstammsatz verwendet wird. Jedes Werk stellt einen Bewertungsbereich dar (z.B. unterschiedliche Bewertungspreise eines Materials in verschiedenen Werken) | Werk:____________Bewertungsart:__________ |
| Kalkulation | Werk | Basismengeneinheit, Profitcenter, Kalkulationslosgröße, Bewertungsklasse, Preissteuerung und Preiseinheit. | Daten zum Kalkulationsbereich können für jede Werks-ID Ihrer Unternehmensstruktur existieren, für die der Materialstammsatz verwendet wird. | Werk:____________ |

### Obligatorische und optionale Stammdaten

Materialstammdatensätze können auf andere Stammdaten verweisen. Die folgende Tabelle bietet eine Übersicht über die optionalen und obligatorischen Stammdatenobjekte, die in einem Materialstammdatensatz verwendet werden müssen.

|  |
| --- |
| Hinweis Für eine ordnungsgemäße Steuerberechnung sind spezifische Felder für Brasilien erforderlich.Prüfen Sie Nota Fiscal – Brasilien - JD0 im Kapitel BR-spezifische Felder für Stammdaten definieren für Materialstammdaten. |

| Stammdatenobjekt | Verwendet im Datensegment | Obligatorisch / optional | Kommentare |
| --- | --- | --- | --- |
| Profitcenter |  | obligatorisch | Für einwandfreie Bewertungsprozesse ist die Zuweisung eines Profitcenters zu einem Material- oder Produktstamm erforderlich. |

### Wesentliche Parameter für die Datenerstellung

In diesem Abschnitt werden einige Basisparameter erläutert, die das Verhalten eines Stammsatzes beeinflussen und zum Anlegen eines Materialstammdatensatzes immer erforderlich sind:

#### Materialart und Nummernkreise

Anhand von Materialarten ermittelt das System welche Datensegmente (Sichten) bearbeitet werden können oder es ermittelt welche Felder Kann- oder Mussfelder sind. Basierend auf den Materialarten ermittelt das System außerdem die Nummernkreise für Materialien. Im SAP-Standardinhalt verwenden alle Materialarten die gleiche Nummernkreisdefinition.

| Nummernkreis | Bereich/Geschäftspartner-ID | Kommentare |
| --- | --- | --- |
| Extern alphanumerisch | A – ZZZZZZZZ | Dieser Bereich muss mit einem Buchstaben beginnen. Insgesamt darf die Kennung nicht länger als 8 Zeichen sein. |
| Intern numerisch | 1 – 99999999 | Dieser Bereich wird verwendet, wenn das System einem Material automatisch eine numerische Nummer zuordnen soll. |

#### Branche

Der Standard-Content stellt nur die Branche M bereit. Diese ist zurzeit nur in der SAP GUI sichtbar.

## Übersichtstabelle

Dieser Umfangsbestandteil umfasst die verschiedenen Prozessschritte in der folgenden Tabelle:

|  |
| --- |
| Hinweis Wenn Ihr Systemadministrator Bereiche und Seiten auf dem SAP Fiori Launchpad aktiviert hat, enthält die Startseite nur die wesentlichen Apps, mit denen die typischen Aufgaben einer Benutzerrolle ausgeführt werden können.Alle anderen (suchbaren) Apps, die nicht auf der Startseite enthalten sind, finden Sie über die Suchleiste ([2434549](https://me.sap.com/notes/2434549)).Wenn Sie die Startseite personalisieren und versteckte Apps hinzufügen möchten, wechseln Sie in Ihr Benutzerprofil und wählen Sie App Finder. |

| Prozessschritt | Benutzerrolle | Transaktion/App | Erwartete Ergebnisse |
| --- | --- | --- | --- |
| [Produktstammdaten anlegen – Grunddaten](#unique_12) [Seite ] 8 | Stammdatenexperte – Produktdaten | Material anlegen(MM01) oder Produktstammdaten verwalten(F1602) | Materialstammdaten – Grunddaten werden angelegt. |
| [Produktstammdaten anlegen – Verkaufsdaten / Umsatzsteuerdaten](#unique_13) [Seite ] 11 | Stammdatenexperte – Produktdaten | Material anlegen(MM01) oder Produktstammdaten verwalten(F1602) | Materialstammdaten – Verkaufsdaten (Umsatzsteuerdaten) werden angelegt. |
| [Produktstammdaten anlegen – Einkaufsdaten](#unique_14) [Seite ] 14 | Stammdatenexperte – Produktdaten | Material anlegen(MM01) oder Produktstammdaten verwalten(F1602) | Materialstammdaten – Einkaufsdaten werden angelegt. |
| [Produktstammdaten anlegen – Klassifikation](#unique_15) [Seite ] 16 | Stammdatenexperte – Produktdaten | Material anlegen(MM01) | Materialstammdaten – Klassifizierung werden angelegt. |
| [Produktstammdaten anlegen - Dispositions-/Planungsdaten/Werksdaten](#unique_16) [Seite ] 18 | Stammdatenexperte – Produktdaten | Material anlegen(MM01) oder Produktstammdaten verwalten(F1602) | Materialstammdaten – Dispositions-/Planungsdaten (Werksdaten) werden angelegt. |
| [Produktstammdaten anlegen – Arbeitsvorbereitung](#unique_17) [Seite ] 22 | Stammdatenexperte – Produktdaten | Material anlegen(MM01) | Materialstammdaten – Arbeitsvorbereitung werden angelegt. |
| [Produktstammdaten anlegen - Lagerortdaten](#unique_18) [Seite ] 24 | Stammdatenexperte – Produktdaten | Material anlegen(MM01) oder Produktstammdaten verwalten(F1602) | Materialstammdaten – Lagerortdaten werden angelegt. |
| [Produktstammdaten anlegen – Buchhaltungsdaten / Bewertungsbereichsdaten](#unique_19) [Seite ] 27 | Stammdatenexperte – Produktdaten | Material anlegen(MM01) oder Produktstammdaten verwalten(F1602) | Materialstammdaten – Buchhaltungsdaten (Bewertungsdaten) werden angelegt. |
| [Produktstammdaten anlegen – Kalkulation](#unique_20) [Seite ] 30 | Stammdatenexperte – Produktdaten | Material anlegen(MM01) | Materialstammdaten – Kalkulation werden angelegt. |

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

In diesem Verfahren erhalten Sie eine Anleitung zum Anlegen von Produktstammdaten. Die zur Verfügung stehenden Apps hängen von der Ihnen zugeordneten Rolle ab. Aus diesem Grund sind zwei Optionen verfügbar.

Vorgehensweise: Option 1 – Material anlegen

Gehen Sie folgendermaßen vor, wenn Sie aufgrund Ihrer Benutzerrolle auf die App Material anlegen(MM01) zugreifen können.

| Testschrittnummer | Bezeichnung des Testschritts | Anweisung | Erwartetes Ergebnis | Bestanden/Nicht bestanden/Anmerkung |
| --- | --- | --- | --- | --- |
| 1. | Anmelden | Melden Sie sich am SAP Fiori Launchpad als Stammdatenexperte – Produktdaten an. | Das SAP Fiori Launchpad wird angezeigt. |  |
| 2 | SAP-Fiori-App aufrufen | Öffnen Sie Material anlegen(MM01). | Material anlegen(MM01) wird angezeigt. |  |
| 3 | Materialgrunddaten eingeben | Nehmen Sie in der Sicht Material anlegen (Einstiegssicht) die folgenden Einträge vor:Material: CM-FL-V01Branche: MHinweis Ist das Eingabefeld Branche ausgeblendet, ist keine Eingabe erforderlich. Wird die Branche nicht zur Eingabe angeboten, wird nicht bekannt im Feld eingetragen.Materialart: KMAT - Konfigurierbare Materialien | Die Sicht Sichtenauswahl wird angezeigt. |  |
| 4 | Sichten wählen | Wählen Sie im Fenster Sichtenauswahl die Sichten Grunddaten 1 und Grunddaten 2 aus und wählen Sie Weiter. | Die Sicht Material anlegen (Konfigurierbare Materialien) wird angezeigt. |  |
| 5 | Grunddaten eingeben | Geben Sie in der Sicht Material CM-FL-V01 anlegen (Konfigurierbare Materialien) auf der Registerkarte Grunddaten 1 die Materialbeschreibung (Kurztext) ein.Beispiel: Gabelstapler |  |  |
| 6 | Grunddaten eingeben | Nehmen Sie auf der Registerkarte Grunddaten 1 im Abschnitt Allgemeine Daten die folgenden Einträge vor:Basismengeneinheit: STWarengruppe: L004Allg. PosTypGrp: 0002 |  |  |
| 7 | Grunddaten eingeben | Nehmen Sie im Bereich Dimensionen/EANs die folgenden Einträge vor:Bruttogewicht: 3Gewichtseinheit: kgNettogewicht: 2 | Die Registerkarte Grunddaten 2 wird angezeigt. |  |
| 8 | Grunddaten eingeben | Auf der Registerkarte Grunddaten 2 müssen Sie keine Einträge vornehmen. | Es öffnet sich das neue Fenster Letzte Datensicht erreicht mit der Meldung Sie beenden die Bearbeitung. Möchten Sie Ihre Daten zunächst sichern? |  |
| 9 | Daten sichern | Wählen Sie im Fenster Letzte Datensicht erreicht die Drucktaste Ja. | Die Sicht Material anlegen (Einstieg) wird angezeigt.Die Grunddaten werden erzeugt und gesichert. |  |

Vorgehensweise: Option 2 – Produktstammdaten verwalten

Gehen Sie folgendermaßen vor, wenn Sie aufgrund Ihrer Benutzerrolle auf die App Produktstammdaten verwalten(F1602) zugreifen können.

| Testschrittnummer | Bezeichnung des Testschritts | Anweisung | Erwartetes Ergebnis | Bestanden/Nicht bestanden/Anmerkung |
| --- | --- | --- | --- | --- |
| 1. | Anmelden | Melden Sie sich am SAP Fiori Launchpad als Stammdatenexperte – Produktdaten an. | Das SAP Fiori Launchpad wird angezeigt. |  |
| 2 | SAP-Fiori-App aufrufen | Öffnen Sie Produktstammdaten verwalten(F1602). | Die App wird geöffnet. |  |
| 3 | "Neuen Produktstamm anlegen" auswählen | Wählen Sie in der Sicht Produktstammdaten verwalten die Option Anlegen. | Stammdatensatz anlegen wird angezeigt. |  |
| 4 | Daten in Pflichtfelder eingeben | Geben Sie in der Sicht Stammdatensatz anlegen die folgenden Daten ein:Produktnummer: z.B. CM-FL-V01 …externe alphanumerische Kennung ... (muss mit einem Zeichen beginnen) oder kein Eintrag (in diesem Fall weist das System automatisch eine numerische ID zu)Weitere Informationen zur Produktnummer finden Sie im Abschnitt Materialart und Nummernkreise unter Wesentliche Parameter für die Datenerstellung.Produktart: KMATProduktgruppe: z.B. L004Basismengeneinheit: z.B. StückBeschreibung: Gabelstapler |  |  |
| 5 | Wählen Sie OK. | Die Sicht Stammdatensatz anlegen wird angezeigt. Wählen Sie OK. | Produktsicht wird angezeigt. |  |
| 6 | Grunddaten eingeben | Geben Sie in der Sicht Produkt > Allgemeine Informationen > Grunddaten die folgenden Daten ein:Sparte: z.B. 00 |  |  |
| 7 | Bezeichnungen auswählen | Wechseln Sie zu Produkt > Allgemeine Informationen > Beschreibungen. | Die Sicht Beschreibungen wird angezeigt. |  |
| 8 | Hinzufügen (+) wählen | Wählen Sie in der Sicht Beschreibungen die Option + (Hinzufügen). | Einige Felder sind bereits ausgefüllt. |  |
| 9 | Beschreibungsdaten eingeben | Geben Sie in der Sicht Beschreibungen folgende Daten ein:Sprache: z.B. DeutschProduktbeschreibung: <Ihre Beschreibung> |  |  |
| 10 | Basismengeneinheit auswählen | Wechseln Sie zu Produkt > Allgemeine Informationen > Basismengeneinheit. |  |  |
| 11 | Basismengeneinheit von Messdaten eingeben | Geben Sie in der Sicht Gewicht folgende Daten ein:Gewichtseinheit: z.B. kgBruttogewicht: z.B. 2Nettogewicht: z.B. 1Hinweis Wenn in den Feldern Bruttogewicht, Gewichtseinheit oder Nettogewicht keine Eingaben möglich sind, wählen Sie in der rechten Ecke die Option Mehr anzeigen. |  |  |
| 12 | Daten sichern | Wählen Sie Sichern. | Eine Systemmeldung bestätigt, dass das Objekt gesichert wurde. |  |

### Produktstammdaten anlegen – Verkaufsdaten / Umsatzsteuerdaten

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

Gehen Sie folgendermaßen vor, wenn Sie aufgrund Ihrer Benutzerrolle auf die App Material anlegen zugreifen können.

| Testschrittnummer | Bezeichnung des Testschritts | Anweisung | Erwartetes Ergebnis | Bestanden/Nicht bestanden/Anmerkung |
| --- | --- | --- | --- | --- |
| 1. | Anmelden | Melden Sie sich am SAP Fiori Launchpad als Stammdatenexperte – Produktdaten an. | Das SAP Fiori Launchpad wird angezeigt. |  |
| 2 | SAP-Fiori-App aufrufen | Öffnen Sie Material anlegen(MM01). | Material anlegen(MM01) wird angezeigt. |  |
| 3 | Materialgrunddaten eingeben | Nehmen Sie auf dem Bild Material anlegen (Einstieg), die folgenden Einträge vor:Material: : CM-FL-V01Branche: MHinweis Ist das Eingabefeld Branche ausgeblendet, ist keine Eingabe erforderlich. Wird die Branche nicht zur Eingabe angeboten, wird nicht bekannt im Feld eingetragen.Materialart: : KMAT - Konfigurierbare Materialien | In einem neuen Fenster wird die Sicht Sichtenauswahl angezeigt. |  |
| 4 | Sichten wählen | Wählen Sie im Fenster Sichtenauswahl die Sichten Vertrieb: VerkaufsorgDaten 1, Vertrieb: VerkaufsorgDaten 2 und Vertrieb: Allg./Werksdaten aus, und wählen Sie dann Weiter. | In einem neuen Fenster werden die Organisationsebenen angezeigt. |  |
| 5 | Organisationsebenendaten eingeben | Nehmen Sie in der Sicht Organisationsebenen im Abschnitt Organisationsebene die folgenden Einträge vor und wählen Sie Weiter:Werk: z.B. 1710Verkaufsorg.: z.B. 1710Vertriebsweg: z.B. 10 | In einem neuen Fenster wird die Sicht Material anlegen (Konfigurierbare Materialien) angezeigt.Im unteren Sichtbereich wird die folgende Systemmeldung angezeigt: Das Material existiert bereits und wird erweitert. |  |
| 6 | Verkaufsdaten eingeben | Geben Sie in der Sicht Material CM-FL-V01 anlegen (Konfigurierbare Materialien) auf der Registerkarte Vertrieb: VerkOrg 1 einen geeigneten Wert für die <Steuerklassifikation> ein.In der Regel wird der Wert "1" für voll steuerpflichtig verwendet. | Die Registerkarte Vertrieb: VerkOrg 2 wird angezeigt.Der eingegebene Wert zeigt an, dass das Material (für gewöhnlich) voll steuerpflichtig ist. |  |
| 7 | Verkaufsdaten eingeben | Nehmen Sie auf der Registerkarte Vertrieb: VerkOrg 2 im Abschnitt Gruppierungsbegriffe den folgenden Eintrag vor:Positionstypengruppe: 0002StatistikGrMaterial: 1 | Sie werden zur nächsten Registerkarte Vertrieb: Allg./Werk weitergeleitet. |  |
| 8 | Verkaufsdaten eingeben | Geben Sie auf der Registerkarte Vertrieb: Allg./Werk im Abschnitt Allgemeine Daten die folgenden Daten ein:Verfügbarkeitsprüfung: z.B. SP |  |  |
| 9 | Verkaufsdaten eingeben | Geben Sie im Abschnitt Versanddaten (Zeiten in Tagen) die folgenden Daten ein:TranspGruppe z.B. 0001Ladegruppe: z.B. 0001 |  |  |
| 10 | Verkaufsdaten eingeben | Geben Sie im Abschnitt Allgemeine Werksparameter die folgenden Daten ein:Profitcenter: z.B. YB110 oder YB111 | Sie gelangen auf ein neues Fenster: Die Sicht Letzte Datensicht erreicht wird geöffnet und gibt folgende Meldung aus: Sie beenden die Bearbeitung. Möchten Sie Ihre Daten zunächst sichern? |  |
| 11 | Daten sichern | Wählen Sie im Fenster Letzte Datensicht erreicht die Drucktaste Ja. | Das Fenster Stammdaten - Produkt wird angezeigt.Ihre Daten werden gesichert. |  |

Vorgehensweise: Option 2 – Produktstammdaten verwalten

Gehen Sie folgendermaßen vor, wenn Sie aufgrund Ihrer Benutzerrolle auf die App Produktstammdaten verwalten(F1602) zugreifen können.

| Testschrittnummer | Bezeichnung des Testschritts | Anweisung | Erwartetes Ergebnis | Bestanden/Nicht bestanden/Anmerkung |
| --- | --- | --- | --- | --- |
| 1. | Anmelden | Melden Sie sich am SAP Fiori Launchpad als Stammdatenexperte – Produktdaten an. | Das SAP Fiori Launchpad wird angezeigt. |  |
| 2 | SAP-Fiori-App aufrufen | Öffnen Sie Produktstammdaten verwalten(F1602). |  |  |
| 3 | "Bearbeiten" wählen | Wählen Sie Bearbeiten.Hinweis Dieser Schritt setzt voraus, dass Sie den vorangehenden Schritt zuvor ausgeführt haben und Sie bereits bei der Kachel Produktstammdaten verwalten angemeldet sind. Nachdem Sie Ihre Daten aus dem vorherigen Abschnitt gesichert haben, befindet sich das System im Anzeigemodus. Um fortzufahren, müssen Sie den Bearbeitungsmodus aufrufen. | Bearbeitungsmodus (Sie können Daten in die Felder eingeben). |  |
| 4 | Vertriebslinien auswählen | Wählen Sie in der Sicht Produkt Vertriebslinien. | Die Sicht Vertriebslinien wird angezeigt. |  |
| 5 | Hinzufügen (+) wählen | Wählen Sie in der Sicht Vertriebslinien > Vertriebslinien + (Hinzufügen). | Die Sicht Produktstamm – Vertriebslinien wird im Änderungsmodus geöffnet. |  |
| 6 | Vertriebsliniendaten eingeben | Geben Sie in der Sicht Produktstamm – Vertriebslinien folgende Daten ein:ALLGEMEINE DATEN - Allgemeine InformationenVerkaufsorganisation: <Verkaufsorganisationsnummer> z.B. 1710Vertriebsweg: z.B. 10Lieferwerk: <Werksnummer>, z.B. 1710,GRUPPIERUNGSBEGRIFFEPositionstypengruppe: z.B. 0002Kontierungsgruppe: z.B. 03 FertigerzeugnisseUMSATZSTEUERLand: <Ländercode> z.B. DESteuerkategorie: TTX1Steuerklassifikation: Entweder 1 für Material oder 2 für DienstleistungenSteuerklassifikation: z.B. 1 volle Steuer, wenn Sie die Steuerkondition UTXJ für die USA verwenden.Die Steuerklassifikation ist von länder-/regionsspezifischen Anforderungen abhängig. Die Steuerklassifikation in den Materialstamm- und Kundestammtabellen bestimmt die Eingaben der Steuersätze.Geben Sie im Abschnitt Nur für Brasilien unter Steuerklassifikation folgende Daten ein:Land: BRSteuerkategorie: IBRXSteuerklassifikation: Entweder 1 für Material oder 2 für Dienstleistungen |  |  |
| 7 | Daten sichern | Wählen Sie Sichern. | Eine Systemmeldung bestätigt, dass das Objekt gesichert wurde. |  |

### Produktstammdaten anlegen – Einkaufsdaten

Testverwaltung

Kundenprojekt: Füllen Sie die projektbezogenen Teile aus.

|  |  |  |  |
| --- | --- | --- | --- |
| Testfall-ID | <X.XX> | Testdatum: |  |
| Testername: |  | Dauer: |  |
| Benutzerrolle(n): |  | Zuständigkeit: | <Geben Sie den Serviceanbieter, einen Kunden oder einen Serviceanbieter zusammen mit einem Kunden an.> |

|  |
| --- |
| Hinweis Wenn Sie das KMAT-Material mit einem Streckenprozess ausführen möchten, dann erweitern Sie die Einkaufssicht. |

Vorgehensweise: Option 1 – Material anlegen

Gehen Sie folgendermaßen vor, wenn Sie aufgrund Ihrer Benutzerrolle auf die App Material anlegen(MM01)"Material anlegen" (MM01) zugreifen können.

| Testschrittnummer | Bezeichnung des Testschritts | Anweisung | Erwartetes Ergebnis | Bestanden/Nicht bestanden/Anmerkung |
| --- | --- | --- | --- | --- |
| 1. | Anmelden | Melden Sie sich am SAP Fiori Launchpad als Stammdatenexperte – Produktdaten an. | Das SAP Fiori Launchpad wird angezeigt. |  |
| 2 | SAP-Fiori-App aufrufen | Öffnen Sie Material anlegen(MM01). | Material anlegen(MM01) wird angezeigt. |  |
| 3 | Materialgrunddaten eingeben | Nehmen Sie auf dem Bild Material anlegen (Einstieg), die folgenden Einträge vor:Material: : CM-FL-V01Branche: MMaterialart: : KMAT - Konfigurierbare Materialien | In einem neuen Fenster wird die Sicht Sichtenauswahl angezeigt. |  |
| 4 | Sichten wählen | Wählen Sie im Fenster Sichtenauswahl die Sicht Einkauf aus und wählen Sie Weiter. | In einem neuen Fenster werden die Organisationsebenen angezeigt. |  |
| 5 | Organisationsebenendaten eingeben | Nehmen Sie in der Sicht Organisationsebenen im Abschnitt Organisationsebene die folgenden Einträge vor und wählen Sie Weiter:Werk: z.B. 1010 | In einem neuen Fenster wird die Sicht Material anlegen (Konfigurierbare Materialien) angezeigt.Im unteren Sichtbereich wird die folgende Systemmeldung angezeigt: Das Material existiert bereits und wird erweitert. |  |
| 6 | Einkaufsdaten eingeben | Stellen Sie sicher, dass folgende Einträge verfügbar sind.Basismengeneinheit: STWarengruppe: L004 | Die Registerkarte Einkauf wird angezeigt. |  |
| 7 | Daten sichern | Wählen Sie Sichern. | Ihre Daten werden gesichert. |  |

Vorgehensweise: Option 2 – Produktstammdaten verwalten

Gehen Sie folgendermaßen vor, wenn Sie aufgrund Ihrer Benutzerrolle auf die App Produktstammdaten verwalten(F1602) zugreifen können.

| Testschrittnummer | Bezeichnung des Testschritts | Anweisung | Erwartetes Ergebnis | Bestanden/Nicht bestanden/Anmerkung |
| --- | --- | --- | --- | --- |
| 1. | Anmelden | Melden Sie sich am SAP Fiori Launchpad als Stammdatenexperte – Produktdaten an. | Das SAP Fiori Launchpad wird angezeigt. |  |
| 2 | SAP-Fiori-App aufrufen | Öffnen Sie Produktstammdaten verwalten(F1602). |  |  |
| 3 | "Bearbeiten" wählen | Wählen Sie Bearbeiten. | Bearbeitungsmodus (Sie können Daten in die Felder eingeben). |  |
| 4 | Einkaufssicht wählen | Wählen Sie in der Sicht Produktstamm die Option Einkauf. | Die Sicht Einkauf wird angezeigt. |  |
| 5 | Einkaufsdaten eingeben | Geben Sie in der Sicht Einkauf die folgenden Daten ein, und wählen Sie Sichern.Mengeneinheit der Bestellung ST | Eine Systemmeldung bestätigt, dass das Objekt gesichert wurde. |  |

### Produktstammdaten anlegen – Klassifikation

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

| Testschrittnummer | Bezeichnung des Testschritts | Anweisung | Erwartetes Ergebnis | Bestanden/Nicht bestanden/Anmerkung |
| --- | --- | --- | --- | --- |
| 1 | Anmelden | Melden Sie sich am SAP Fiori Launchpad als Stammdatenexperte – Produktdaten an. | Das SAP Fiori Launchpad wird angezeigt. |  |
| 2 | SAP-Fiori-App aufrufen | Öffnen Sie Material anlegen(MM01). | Material anlegen(MM01) wird angezeigt. |  |
| 3 | Materialgrunddaten eingeben | Nehmen Sie auf dem Bild Material anlegen (Einstieg), die folgenden Einträge vor:Material: CM-FL-V01Branche: MHinweis Ist das Eingabefeld Branche ausgeblendet, ist keine Eingabe erforderlich. Wird die Branche nicht zur Eingabe angeboten, wird nicht bekannt im Feld eingetragen.Materialart: KMAT - Konfigurierbare Materialien | In einem neuen Fenster wird die Sicht Sichtenauswahl angezeigt. |  |
| 4 | Sichten wählen | Wählen Sie im Fenster Sichtenauswahl die Sicht Klassifikation aus, und wählen Sie Weiter. | In einem neuen Fenster wird die Sicht Klassenart (1) angezeigt. |  |
| 5 | Organisationsebenendaten eingeben | Geben Sie im Abschnitt Restriktionsebene die folgenden Daten ein, und wählen Sie Weiter:Klassenartentext: VariantenArt: 300 | In einem neuen Fenster wird die Sicht "Klassifikation" angezeigt. |  |
| 6 | Verkaufsdaten eingeben | Geben Sie in der Sicht Klassifikation unter Zuordnungen die folgende Werte in der Spalte Klasse ein, und wählen Sie Sichern.AVC_CL_ELECADD_V01AVC_CL_REFCSTC_V01AVC_CL_COMMON_V01 | Die Klassifikationssicht wird angezeigt.Ihre Daten werden gesichert. |  |

Vorgehensweise: Option 2 – Produktstammdaten verwalten

|  |
| --- |
| Hinweis Die erforderlichen Felder sind für diese Anwendung momentan nicht verfügbar. Verwenden Sie Option 1 (oben) |

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

Sie müssen das vorherige Verfahren Produktstammdaten anlegen – Grunddaten erst abschließen, bevor Sie mit diesem Abschnitt fortfahren können.

Beginnen Sie mit dieser Vorgehensweise, nachdem Sie die eingegebenen Grunddaten gesichert haben, wie bei der vorherigen Vorgehensweise erläutert.

Vorgehensweise: Option 1 – Material anlegen

Gehen Sie folgendermaßen vor, wenn Sie aufgrund Ihrer Benutzerrolle auf die App Material anlegen(MM01) zugreifen können.

| Testschrittnummer | Bezeichnung des Testschritts | Anweisung | Erwartetes Ergebnis | Bestanden/Nicht bestanden/Anmerkung |
| --- | --- | --- | --- | --- |
| 1. | Anmelden | Melden Sie sich am SAP Fiori Launchpad als Stammdatenexperte – Produktdaten an. | Das SAP Fiori Launchpad wird angezeigt. |  |
| 2 | SAP-Fiori-App aufrufen | Öffnen Sie Material anlegen(MM01). | Material anlegen(MM01) wird angezeigt. |  |
| 3 | Materialgrunddaten eingeben | Nehmen Sie auf dem Bild Material anlegen (Einstieg), die folgenden Einträge vor:Material: CM-FL-V01Branche: MHinweis Ist das Eingabefeld Branche ausgeblendet, ist keine Eingabe erforderlich. Wird die Branche nicht zur Eingabe angeboten, wird nicht bekannt im Feld eingetragen.Materialart: KMAT - Konfigurierbare Materialien | Die Sicht Sichtenauswahl wird angezeigt. |  |
| 4 | Sichten wählen | Wählen Sie im Fenster Sichtenauswahl die Sichten Disposition 1, Disposition 2, Disposition 3 und Disposition 4 aus, und wählen Sie Weiter. | Die Sicht Organisationsebenen wird angezeigt. |  |
| 5 | Organisationsebenendaten eingeben | Nehmen Sie in der Sicht Organisationsebenen im Abschnitt Organisationsebenen die folgenden Einträge vor:Werk: <Nummer des Werks>, z.B. 1710,Lagerort: z.B. 171A | Die Sicht Material anlegen (Konfigurierbare Materialien) wird angezeigt.Im unteren Sichtbereich wird die folgende Systemmeldung angezeigt: Das Material existiert bereits und wird erweitert. |  |
| 6 | Dispositions-/Planungsdaten eingeben | Nehmen Sie in der Sicht Material (Konfigurierbare Materialien) auf der Registerkarte Disposition 1 im Abschnitt Allgemeine Daten den folgenden Eintrag vor:Basismengeneinheit: ST |  |  |
| 7 | Dispositions-/Planungsdaten eingeben | Nehmen Sie im Abschnitt Dispositionsverfahren die folgenden Einträge vor:Dispositionsmerkmal: z.B. PDDisponent: z.B. 001 |  |  |
| 8 | Dispositions-/Planungsdaten eingeben | Nehmen Sie im Bereich Losgrößenverfahren den folgenden Eintrag vor:Losgrößenverfahren: EX | Die nächste Registerkarte Disposition 2 wird angezeigt. |  |
| 9 | Dispositions-/Planungsdaten eingeben | Geben Sie in der Sicht Material CM-FL-V01 anlegen (Konfigurierbare Materialien) auf der Registerkarte Disposition 2 die für Ihren Fall erforderlichen Daten ein, oder erfassen Sie mindestens Werte für die erforderlichen Felder, z.B. "Eigenfertigungszeit in Tagen". | Die nächste Registerkarte Disposition 3 wird angezeigt. |  |
| 10 | Dispositions-/Planungsdaten eingeben | Nehmen Sie in der Sicht Material anlegen (Konfigurierbare Materialien) auf der Registerkarte Disposition 3 im Abschnitt Planung die folgenden Einträge vor:Strategiegruppe: z.B. 25Verrechnungsmodus: z.B. 2 |  |  |
| 11 | Dispositions-/Planungsdaten eingeben | Nehmen Sie im Bereich Verfügbarkeitsprüfung die folgenden Einträge vor:Verfügbarkeitsprüfung: z.B. SPGesamtwieder- beschaffungszeit z.B. 3 | Die nächste Registerkarte Disposition 4 wird angezeigt. |  |
| 12 | Dispositions-/Planungsdaten eingeben | In der Sicht Material CM-FL-V01 anlegen (Konfigurierbare Materialien), auf der Registerkarte Disposition 4, müssen Sie keine Einträge vornehmen. | Es öffnet sich das neue Fenster Letzte Datensicht erreicht mit der Meldung Sie beenden die Bearbeitung. Möchten Sie Ihre Daten zunächst sichern? |  |
| 13 | Sichern | Wählen Sie im Fenster Letzte Datensicht erreicht die Drucktaste Ja. | Die Sicht Stammdaten - Produkt wird angezeigt.Ihre Daten werden gesichert. |  |

Vorgehensweise: Option 2 – Produktstammdaten verwalten

Gehen Sie folgendermaßen vor, wenn Sie aufgrund Ihrer Benutzerrolle auf die App Produktstammdaten verwalten(F1602) zugreifen können.

| Testschrittnummer | Bezeichnung des Testschritts | Anweisung | Erwartetes Ergebnis | Bestanden/Nicht bestanden/Anmerkung |
| --- | --- | --- | --- | --- |
| 1. | Anmelden | Melden Sie sich am SAP Fiori Launchpad als Stammdatenexperte – Produktdaten an. | Das SAP Fiori Launchpad wird angezeigt. |  |
| 2 | SAP-Fiori-App aufrufen | Öffnen Sie Produktstammdaten verwalten(F1602). |  |  |
| 3 | "Bearbeiten" wählen | Wählen Sie Bearbeiten.Hinweis Dieser Schritt setzt voraus, dass Sie den vorangehenden Schritt zuvor ausgeführt haben und Sie bereits bei der Kachel Produktstammdaten verwalten angemeldet sind. Nachdem Sie Ihre Daten aus dem vorherigen Abschnitt gesichert haben, befindet sich das System im Anzeigemodus. Um fortzufahren, müssen Sie den Bearbeitungsmodus aufrufen. | Bearbeitungsmodus (Sie können Daten in die Felder eingeben). |  |
| 4 | Werksdaten auswählen | Wählen Sie in der Sicht Produktstamm die Option Werke. | Die Sicht Werke wird angezeigt. |  |
| 5 | Hinzufügen (+) wählen | Wählen Sie im Sichtabschnitt Werke die Option + (Hinzufügen). | Die Sicht Werk wird im Bearbeitungsmodus geöffnet. |  |
| 6 | "Werke - Allgemeine Daten" eingeben | Nehmen Sie in der Sicht Werk > Allgemeine Informationen folgende Einträge vor:Werk: <Werksnummer>, z.B. 1710,Profitcenter: z.B. YB110 oder YB111Ladegruppe: z.B. 0001 – Gabelstapler |  |  |
| 7 | "Werke – Dispositionsdaten" auswählen | Wählen Sie in der Sicht Werk Dispositionsdaten. | Die Sicht Dispositionsdaten wird angezeigt. |  |
| 8 | "Werke – Dispositionsdaten" eingeben | Wählen Sie in der Sicht Dispositionsdaten Dispositionsdaten aus, und nehmen die folgenden Einträge vor:Verfügbarkeitsprüfung: z.B. SPPlanlieferzeit: z.B. 3Wareneingangsbearbeitungszeit: z.B. 1Dispositionsmerkmal: z.B. PDDisponent: z.B. 001 |  |  |
| 9 | "Werke – Losgrößendaten" auswählen | Wählen Sie in der Sicht Dispositionsdaten Losgrößendaten. | Der Sichtabschnitt Losgrößendaten wird angezeigt. |  |
| 10 | "Werke – Losgrößendaten" eingeben | Nehmen Sie in der Sicht Losgrößendaten den folgenden Eintrag vor:Losgrößenverfahren: z.B. EX |  |  |
| 11 | "Werke – Prognosedaten" auswählen | Wählen Sie in der Sicht Produkt > WERKE PROGNOSE. | PROGNOSE wird angezeigt. |  |
| 12 | Werke – Prognosedaten eingeben | Geben Sie in der Sicht PROGNOSE folgende Daten ein:Periodenart: z.B. F |  |  |
| 13 | Zur Hauptsicht zurückkehren | Wählen Sie die Pfeiltaste "Zurück", um zum Produktstamm zurückzukehren. | Die Sicht Produktstamm wird angezeigt. |  |
| 14 | Daten sichern | Wählen Sie Sichern. | Eine Systemmeldung bestätigt, dass das Objekt gesichert wurde. |  |

### Produktstammdaten anlegen – Arbeitsvorbereitung

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

| Testschrittnummer | Bezeichnung des Testschritts | Anweisung | Erwartetes Ergebnis | Bestanden/Nicht bestanden/Anmerkung |
| --- | --- | --- | --- | --- |
| 1 | Anmelden | Melden Sie sich am SAP Fiori Launchpad als Stammdatenexperte – Produktdaten an. | Das SAP Fiori Launchpad wird angezeigt. |  |
| 2 | SAP-Fiori-App aufrufen | Öffnen Sie Material anlegen(MM01). | Das Bild Material anlegen(MM01) wird angezeigt. |  |
| 3 | Materialgrunddaten eingeben | Nehmen Sie in der Sicht Material anlegen (Einstieg), die folgenden Einträge vor:Material: CM-FL-V01Branche: MHinweis Ist das Eingabefeld Branche ausgeblendet, ist keine Eingabe erforderlich. Wird die Branche nicht zur Eingabe angeboten, wird nicht bekannt im Feld eingetragen.Materialart: KMAT - Konfigurierbare Materialien | Die Sicht Sichtenauswahl wird angezeigt. |  |
| 4 | Sichten wählen | Wählen Sie im Fenster Sichtenauswahl die Sicht Arbeitsvorbereitung aus, und wählen Sie Weiter. | Die Sicht Organisationsebenen wird angezeigt. |  |
| 5 | Organisationsebenendaten eingeben | Geben Sie in der Sicht Organisationsebenen die folgenden Daten ein, und wählen Sie Weiter.Werk: 1710 | Ein neues Fenster Material CM-FL-V01 ändern (Konfigurierbare Materialien) wird geöffnet. |  |
| 6 | Arbeitsvorbereitungsdaten eingeben | Geben Sie im Fenster Material CM-FL-V01 ändern (Konfigurierbare Materialien) unter Allgemeine Daten die folgenden Daten ein, und wählen Sie Sichern.Basismengeneinheit: STFertSteuerer: YB3Fertigungssteuerer Profil: YB0003 | Sie gelangen auf ein neues Fenster: Die Sicht Letzte Datensicht erreicht wird geöffnet und gibt folgende Meldung aus: Sie beenden die Bearbeitung. Möchten Sie Ihre Daten zunächst sichern? |  |
| 7 | Daten sichern | Wählen Sie im Fenster Letzte Datensicht erreicht die Drucktaste Ja. | Das Fenster Stammdaten - Produkt wird angezeigt.Ihre Daten werden gesichert. |  |

Vorgehensweise: Option 2 – Produktstammdaten verwalten

|  |
| --- |
| Hinweis Die erforderlichen Felder sind für diese Anwendung momentan nicht verfügbar. Verwenden Sie die Option 1 (siehe oben), und sichern Sie Ihre Eingaben. |

### Produktstammdaten anlegen - Lagerortdaten

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

Sie müssen das vorherige Verfahren Produktstammdaten anlegen – Grunddaten erst abschließen, bevor Sie mit diesem Abschnitt fortfahren können.

Beginnen Sie mit dieser Vorgehensweise, nachdem Sie die eingegebenen Grunddaten gesichert haben, wie bei der vorherigen Vorgehensweise erläutert.

Vorgehensweise: Option 1 – Material anlegen

Gehen Sie folgendermaßen vor, wenn Sie aufgrund Ihrer Benutzerrolle auf die App Material anlegen(MM01) zugreifen können.

| Testschrittnummer | Bezeichnung des Testschritts | Anweisung | Erwartetes Ergebnis | Bestanden/Nicht bestanden/Anmerkung |
| --- | --- | --- | --- | --- |
| 1. | Anmelden | Melden Sie sich am SAP Fiori Launchpad als Stammdatenexperte – Produktdaten an. | Das SAP Fiori Launchpad wird angezeigt. |  |
| 2 | SAP-Fiori-App aufrufen | Öffnen Sie Material anlegen(MM01). | Material anlegen(MM01) wird angezeigt. |  |
| 3 | Materialgrunddaten eingeben | Nehmen Sie in der Sicht Material anlegen (Einstiegssicht) die folgenden Einträge vor:Material: CM-FL-V01Branche: MHinweis Ist das Eingabefeld Branche ausgeblendet, ist keine Eingabe erforderlich. Wird die Branche nicht zur Eingabe angeboten, wird nicht bekannt im Feld eingetragen.Materialart: KMAT - Konfigurierbare Materialien | Die Sicht Sichtenauswahl wird angezeigt. |  |
| 4 | Sichten wählen | Wählen Sie im Fenster Sichtenauswahl die folgenden Sichten aus und wählen Sie Weiter:Allg. Werksdaten / Lagerung 1Allg. Werksdaten / Lagerung 2 | Die Sicht Organisationsebenen wird angezeigt. |  |
| 5 | Organisationsebenendaten eingeben | Nehmen Sie in der Sicht Organisationsebenen im Abschnitt Organisationsebene die folgenden Einträge vor:Werk: z.B. 1710Lagerort: z.B. 171A | Es öffnet sich ein neues Fenster, das die Sicht Material anlegen (Konfigurierbare Materialien) anzeigt.Im unteren Sichtbereich wird die folgende Systemmeldung angezeigt: Das Material existiert bereits und wird erweitert. |  |
| 6 | Lagerortdaten eingeben | Nehmen Sie in der Sicht Material anlegen (Konfigurierbare Materialien) auf der Registerkarte Werksdaten/Lagerung 1 im Bereich Allgemeine Daten folgenden Eintrag vor:Anzahl WE-Scheine: z.B. 1 | Die nächste Registerkarte Werksdaten/Lagerung2 wird angezeigt. |  |
| 7 | Eingaben bestätigen | Nehmen Sie auf der Registerkarte Werksdaten/Lagerung 2 keine Einträge vor. | Es öffnet sich das neue Fenster Letzte Datensicht erreicht mit der Meldung Sie beenden die Bearbeitung. Möchten Sie Ihre Daten zunächst sichern? |  |
| 8 | Sichern | Wählen Sie im Fenster Letzte Datensicht erreicht die Drucktaste Ja. | Das Fenster Stammdaten - Produkt wird angezeigt.Ihre Daten werden gesichert. |  |

Vorgehensweise: Option 2 – Produktstammdaten verwalten

Gehen Sie folgendermaßen vor, wenn Sie aufgrund Ihrer Benutzerrolle auf die App Produktstammdaten verwalten(F1602) zugreifen können.

| Testschrittnummer | Bezeichnung des Testschritts | Anweisung | Erwartetes Ergebnis | Bestanden/Nicht bestanden/Anmerkung |
| --- | --- | --- | --- | --- |
| 1. | Anmelden | Melden Sie sich am SAP Fiori Launchpad als Stammdatenexperte – Produktdaten an. | Das SAP Fiori Launchpad wird angezeigt. |  |
| 2 | SAP-Fiori-App aufrufen | Öffnen Sie Produktstammdaten verwalten(F1602). |  |  |
| 3 | "Bearbeiten" wählen | Wählen Sie Bearbeiten.Hinweis Dieser Schritt setzt voraus, dass Sie den vorangehenden Schritt zuvor ausgeführt haben und Sie bereits bei der Kachel Produktstammdaten verwalten angemeldet sind. Nachdem Sie Ihre Daten aus dem vorherigen Abschnitt gesichert haben, befindet sich das System im Anzeigemodus. Um fortzufahren, müssen Sie den Bearbeitungsmodus aufrufen. | Bearbeitungsmodus (Sie können Daten in die Felder eingeben). |  |
| 4 | Werksdaten auswählen | Wählen Sie in der Sicht Produkt die Option WERKE.Hinweis Wenn kein Werksdatensatz vorhanden ist, führen Sie die Schritte des vorherigen Abschnitts Produktstammdaten anlegen - Dispositions-/Planungsdaten/Werksdaten durch. | Die Sicht WERKE wird angezeigt. |  |
| 5 | Werksdaten auswählen | Wählen Sie in der Sicht WERKE das Pfeilsymbol, um die Werksdaten auszuwählen, die Sie im vorherigen Schritt angelegt haben. | Die Sicht Produktstamm - Werk wird angezeigt. |  |
| 6 | Zum Werk: Lagerort | Navigieren Sie in der Sicht Produktstamm - Werk zu WERKE > LAGERORTE. | Die Sicht Produktstamm – WERKE wird im Änderungsmodus geöffnet. |  |
| 7 | Hinzufügen (+) wählen | Wählen Sie in der Sicht LAGERORTE > Lagerorte, und wählen Sie + (Hinzufügen). | Die Sicht Werk – Lagerort wird im Änderungsmodus geöffnet. |  |
| 8 | Werk eingeben: Lagerort" eingeben | Geben Sie in der Sicht Lagerorte folgende Daten ein:Lagerort:<Lagerortnummer> z.B. 171A |  |  |
| 9 | Zur Hauptsicht zurückkehren | Wählen Sie zweimal die Pfeiltaste "Zurück", um zum Produktstamm zurückzukehren. | Kehren Sie zur Sicht Produktstamm zurück. |  |
| 10 | Sichern | Wählen Sie Sichern. | Eine Systemmeldung bestätigt, dass das Objekt gesichert wurde. |  |

### Produktstammdaten anlegen – Buchhaltungsdaten / Bewertungsbereichsdaten

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

| Testschrittnummer | Bezeichnung des Testschritts | Anweisung | Erwartetes Ergebnis | Bestanden/Nicht bestanden/Anmerkung |
| --- | --- | --- | --- | --- |
| 1. | Anmelden | Melden Sie sich am SAP Fiori Launchpad als Stammdatenexperte – Produktdaten an. | Das SAP Fiori Launchpad wird angezeigt. |  |
| 2 | SAP-Fiori-App aufrufen | Öffnen Sie Material anlegen(MM01). | Material anlegen(MM01) wird angezeigt. |  |
| 3 | Materialgrunddaten eingeben | Nehmen Sie in der Sicht Material anlegen (Einstiegssicht) die folgenden Einträge vor:Material: CM-FL-V01Branche: MHinweis Ist das Eingabefeld Branche ausgeblendet, ist keine Eingabe erforderlich. Wird die Branche nicht zur Eingabe angeboten, wird nicht bekannt im Feld eingetragen.Materialart: KMAT - Konfigurierbare Materialien | Sichtenauswahl wird angezeigt. |  |
| 4 | Sichten wählen | Wählen Sie im Fenster Sichtenauswahl die folgenden Sichten aus und wählen Sie Weiter:Buchhaltung 1Buchhaltung 2 | Die Sicht Organisationsebenen wird angezeigt. |  |
| 5 | Organisationsebenendaten eingeben | Nehmen Sie in der Sicht Organisationsebenen im Abschnitt "Organisationsebenen" die folgenden Einträge vor:Werk: 1710 | Die Sicht Material anlegen (Konfigurierbare Materialien) wird angezeigt.Im unteren Sichtbereich wird die folgende Information angezeigt: Das Material existiert bereits und wird erweitert. |  |
| 6 | Buchhaltungsdaten eingeben | Nehmen Sie in der Sicht Material anlegen (Konfigurierbare Materialien) auf der Registerkarte Buchhaltung 1 im Abschnitt Allgemeine Bewertungsdaten den folgenden Eintrag vor:Bewertungsklasse: 7920 |  |  |
| 7 | Buchhaltungsdaten eingeben | Nehmen Sie im Bereich Preise und Werte die folgenden Einträge vor:Standardpreis: 1Per. VPreis: 1Preis- strg: S | Sie werden zur nächsten Registerkarte Buchhaltung 2 weitergeleitet. |  |
| 8 | Eingaben bestätigen | Auf der Registerkarte Buchhaltung 2 müssen Sie keine Einträge vornehmen. | Es öffnet sich das neue Fenster Letzte Datensicht erreicht mit der Meldung Sie beenden die Bearbeitung. Möchten Sie Ihre Daten zunächst sichern? |  |
| 9 | Daten sichern | Wählen Sie im Fenster Letzte Datensicht erreicht die Drucktaste Ja. | Das Fenster Stammdaten - Produkt wird angezeigt.Ihre Daten werden gesichert. |  |

Vorgehensweise: Option 2 – Produktstammdaten verwalten

Gehen Sie folgendermaßen vor, wenn Sie aufgrund Ihrer Benutzerrolle auf die App Produktstammdaten verwalten(F1602) zugreifen können.

| Testschrittnummer | Bezeichnung des Testschritts | Anweisung | Erwartetes Ergebnis | Bestanden/Nicht bestanden/Anmerkung |
| --- | --- | --- | --- | --- |
| 1. | Anmelden | Melden Sie sich am SAP Fiori Launchpad als Stammdatenexperte – Produktdaten an. | Das SAP Fiori Launchpad wird angezeigt. |  |
| 2 | SAP-Fiori-App aufrufen | Öffnen Sie Produktstammdaten verwalten(F1602). |  |  |
| 3 | "Bearbeiten" wählen | Wählen Sie Bearbeiten.Hinweis Dieser Schritt setzt voraus, dass Sie den vorangehenden Schritt zuvor ausgeführt haben und Sie bereits bei der Kachel Produktstammdaten verwalten angemeldet sind. Nachdem Sie Ihre Daten aus dem vorherigen Abschnitt gesichert haben, befindet sich das System im Anzeigemodus. Um fortzufahren, müssen Sie den Bearbeitungsmodus aufrufen. | Bearbeitungsmodus (Sie können Daten in die Felder eingeben). |  |
| 4 | Bewertungskreisdaten auswählen | Wählen Sie in der Sicht Produkt die Option BEWERTUNGSKREISE. | Die Sicht BEWERTUNGSKREISE wird angezeigt. |  |
| 5 | Hinzufügen (+) wählen | Wählen Sie in der Sicht BEWERTUNGSKREISE + (Hinzufügen). | Die Sicht BEWERTUNGSKREISE wird im Bearbeitungsmodus geöffnet. |  |
| 6 | Bewertungskreisdaten eingeben | Geben Sie in der Sicht BEWERTUNGSKREISE > Bewertungskreis folgende Daten ein:Bewertungskreis: <Nummer>, z.B. 1710Preissteuerungsfindung:2Bewertungsklasse: z.B. 7920 |  |  |
| 7 | Aktuelle Bewertungskreisdaten eingeben | Wählen Sie in der Sicht Bewertung die Laufende Periode und geben folgende Daten ein:Gleitender Durchschnittspreis: z.B. 20Preissteuerung: z.B. S |  |  |
| 8 | Zur Hauptsicht zurückkehren | Wählen Sie die Pfeiltaste "Zurück", um zum Produktstamm zurückzukehren. | Kehren Sie zur Sicht Produktstamm zurück. |  |
| 9 | Sichern | Wählen Sie Sichern. | Eine Systemmeldung bestätigt, dass das Objekt gesichert wurde. |  |

### Produktstammdaten anlegen – Kalkulation

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

| Testschrittnummer | Bezeichnung des Testschritts | Anweisung | Erwartetes Ergebnis | Bestanden/Nicht bestanden/Anmerkung |
| --- | --- | --- | --- | --- |
| 1 | Anmelden | Melden Sie sich am SAP Fiori Launchpad als Stammdatenexperte – Produktdaten an. | Das SAP Fiori Launchpad wird angezeigt. |  |
| 2 | SAP-Fiori-App aufrufen | Öffnen Sie Material anlegen(MM01). | Material anlegen(MM01) wird angezeigt. |  |
| 3 | Materialgrunddaten eingeben | Nehmen Sie in der Sicht Material anlegen (Einstieg), die folgenden Einträge vor:Material: CM-FL-V01Branche: MHinweis Ist das Eingabefeld Branche ausgeblendet, ist keine Eingabe erforderlich. Wird die Branche nicht zur Eingabe angeboten, wird nicht bekannt im Feld eingetragen.Materialart: KMAT - Konfigurierbare Materialien | Die Sicht Sichtenauswahl wird angezeigt. | Feld ist nicht verfügbar. |
| 4 | Sichten wählen | Wählen Sie im Fenster Sichtenauswahl die Sichten Kalkulation 1 und Kalkulation 2 aus, und wählen Sie Weiter. | Die Sicht Klassenart (1) wird angezeigt. |  |
| 5 | Organisationsebenendaten eingeben | Geben Sie im Abschnitt Organisationsebene die folgenden Daten ein, und wählen Sie Weiter:Werk: 1710 | Die Sicht Kalkulation 1 wird angezeigt. |  |
| 6 | Daten für Kalkulation 1 eingeben | Wählen Sie in der Sicht Kalkulation 1 die folgenden Daten ein, und wählen Sie dann die Registerkarte Kalkulation 2.Basismengeneinheit: STProfitcenter: YB110Kalkulationslosgröße: 100 | Die Sicht Kalkulation 2 wird angezeigt.Ihre Daten werden gesichert. |  |
| 7 | Daten für Kalkulation 2 eingeben | Wählen Sie in der Sicht Kalkulation 2 die folgenden Einträge aus, und wählen Sie dann zum Sichern Weiter:Bewertungsklasse: 7920Preissteuerung: SPreiseinheit: 1 | Ihre Daten werden gesichert. |  |

Vorgehensweise: Option 2 – Produktstammdaten verwalten

|  |
| --- |
| Hinweis Die erforderlichen Felder sind für diese Anwendung momentan nicht verfügbar. Verwenden Sie die Option 1 (siehe oben), und sichern Sie Ihre Eingaben. |

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
> Flagged while digesting this document, not verified: Brazil-specific tax fields are required for correct tax calculation (refers to Nota Fiscal JD0), not detailed here

> [!warning] Conflict
> Flagged while digesting this document, not verified: Sample plant values vary between sections (purchasing uses plant 1010, others 1710), possibly inconsistent example data

## Connections
- part-of :: [[_cluster]]
- related-to :: [[02-business-partner-and-product-master-data/master-data-script-create-product-master-of-type-configurable-material]]
- related-to :: [[02-business-partner-and-product-master-data/mds-2t7-285]]
- related-to :: [[02-business-partner-and-product-master-data/sap-s-4hana-cloud-public-edition-mds-2t7-283]]
- related-to :: [[02-business-partner-and-product-master-data/script-de-dados-mestre-criar-mestre-de-produtos-do-tipo-material-confi]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/2T7_S4CLD2608_Master_Data_DE_XX.docx` — full document · extracted with `mammoth` · 57,553 chars in the whole document
