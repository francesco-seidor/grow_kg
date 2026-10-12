---
id: 02-business-partner-and-product-master-data/stammdatenskript-produktstamm-vom-typ-serviceprodukt-anlegen-sds-31x-3
title: "Stammdatenskript: Produktstamm vom Typ „Serviceprodukt“ anlegen – SDS (31X) (31X_S4CLD2608_Master_Data_DE_XX)"
description: "German SAP S/4HANA Cloud Public Edition master data script (31X): create a service product master (basic, sales/tax, purchasing, accounting data) via MM01 or F1602."
cluster: 02-business-partner-and-product-master-data
tags: [kb/business-partner-and-product-master-data, topic/product-master-non-stock-and-service]
aliases: [31X_S4CLD2608_Master_Data_DE_XX]
keywords: ["Product Master: Non-Stock Materials and Service Products", service product master, material master data, basic data, sales data, purchasing data, accounting data, material types, number ranges, organizational units]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/31X_S4CLD2608_Master_Data_DE_XX.docx]
confidence: high
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-304
topic: 02-business-partner-and-product-master-data/product-master-non-stock-and-service
language: DE
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Stammdatenskript: Produktstamm vom Typ „Serviceprodukt“ anlegen – SDS (31X) (31X_S4CLD2608_Master_Data_DE_XX)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/31X_S4CLD2608_Master_Data_DE_XX.docx`, extracted with `mammoth`. Grouped under **Product Master: Non-Stock Materials and Service Products** in Business Partner and Product Master Data. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

| <!-- image omitted: unnamed --> | StammdatenskriptSAP S/4HANA Cloud Public Edition - 02-07-26 |
| --- | --- |
|  | Produktstamm vom Typ „Serviceprodukt“ anlegen – SDS (31X) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Inhaltsverzeichnis

[1 Verwendungszweck 2](#_Toc233889601)

[2 Voraussetzungen 3](#_Toc233889602)

[2.1 Systemzugriff 3](#_Toc233889603)

[2.2 Rollen 3](#_Toc233889604)

[2.3 Erforderliche Organisationseinheiten 3](#_Toc233889605)

[2.4 Obligatorische und operative Stammdaten 4](#_Toc233889606)

[2.5 Wesentliche Parameter für die Datenerstellung 5](#_Toc233889607)

[2.5.1 Materialart und Nummernkreise 5](#_Toc233889608)

[2.5.2 Branche 5](#_Toc233889609)

[3 Übersichtstabelle 6](#_Toc233889610)

[4 Testverfahren 7](#_Toc233889611)

[4.1 Materialstammdaten (Serviceprodukt) anlegen - Grunddaten 7](#_Toc233889612)

[4.2 Materialstammdaten (Serviceprodukt) anlegen – Verkaufsdaten (Umsatzsteuerdaten) 9](#_Toc233889613)

[4.3 Materialstammdaten (Serviceproduktstammdaten) anlegen – Einkaufsdaten 13](#_Toc233889614)

[4.4 Materialstammdaten (Serviceproduktstammdaten) anlegen – Buchhaltungsdaten (Bewertungsbereichsdaten) 15](#_Toc233889615)

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
| System | Erreichbar über SAP Fiori Launchpad. Ihr Systemadministrator stellt Ihnen die URL für den Zugriff auf die verschiedenen Apps zur Verfügung, die Ihrer Rolle zugeordnet sind. |

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
| Einkaufsdaten | Werk | Einkäufergruppe, Materialgruppe, WE-Bearbeitungszeit usw. | Einkaufsdaten können für jede Einkaufsorganisation existieren, für die das Material in Einkaufsvorgängen verwendet werden soll. | Werk:__________ |
| Buchhaltungsdaten | Bewertungsbereich (= Werk), Bewertungsart | Bewertungsklasse, Per. VPreis, Preissteuerung usw. | Daten zum Bewertungsbereich können für jede Werks-ID Ihrer Unternehmensstruktur existieren, für die der Materialstammsatz verwendet wird. Jedes Werk stellt einen Bewertungsbereich dar (z.B. unterschiedliche Bewertungspreise eines Materials in verschiedenen Werken) | Werk:____________Bewertungsart:__________ |

### Obligatorische und operative Stammdaten

Materialstammdatensätze können auf andere Stammdaten verweisen. Die folgende Tabelle bietet eine Übersicht über die optionalen und obligatorischen Stammdatenobjekte, die in einem Materialstammdatensatz verwendet werden müssen.

|  |
| --- |
| Hinweis Für eine ordnungsgemäße Steuerberechnung sind brasilienspezifische Felder erforderlich.Prüfen Sie Nota Fiscal – Brasilien - JD0 im Kapitel BR-spezifische Felder für Stammdaten definieren für Materialstammdaten. |

| Stammdatenobjekt | Verwendet im Datensegment | Obligatorisch / optional | Kommentare |
| --- | --- | --- | --- |
| Profitcenter |  | Obligatorisch | Für einwandfreie Bewertungsprozesse ist die Zuweisung eines Profitcenters zu einem Material- oder Produktstamm erforderlich. |

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

| Prozessschritt | Benutzerrolle | Vorgang/App | Erwartete Ergebnisse |
| --- | --- | --- | --- |
| [Materialstammdaten (Serviceprodukt) anlegen - Grunddaten](#unique_11) [Seite ] 7 | Stammdatenexperte – Produktdaten | Material anlegen(MM01)/Produktstammdaten verwalten(F1602) | Materialstammdaten - Grunddaten werden angelegt. |
| [Materialstammdaten (Serviceprodukt) anlegen – Verkaufsdaten (Umsatzsteuerdaten)](#unique_12) [Seite ] 9 | Stammdatenexperte – Produktdaten | Material anlegen(MM01)/Produktstammdaten verwalten(F1602) | Materialstammdaten - Verkaufsdaten werden angelegt. |
| [Materialstammdaten (Serviceproduktstammdaten) anlegen – Einkaufsdaten](#unique_13) [Seite ] 13 | Stammdatenexperte – Produktdaten | Material anlegen(MM01)/Produktstammdaten verwalten(F1602) | Materialstammdaten - Einkaufsdaten werden angelegt. |
| [Materialstammdaten (Serviceproduktstammdaten) anlegen – Buchhaltungsdaten (Bewertungsbereichsdaten)](#unique_14) [Seite ] 15 | Stammdatenexperte – Produktdaten | Material anlegen(MM01)/Produktstammdaten verwalten(F1602) | Materialstammdaten – Buchhaltungsdaten (Bewertungsbereichsdaten) werden angelegt. |

## Testverfahren

In diesem Abschnitt werden die Testverfahren für den jeweiligen Prozessschritt beschrieben, der zum betreffenden Umfangsbestandteil gehört.

### Materialstammdaten (Serviceprodukt) anlegen - Grunddaten

Testverwaltung

Kundenprojekt: Füllen Sie die projektbezogenen Teile aus.

|  |  |  |  |
| --- | --- | --- | --- |
| Testfall-ID | <X.XX> | Testdatum: |  |
| Testername: |  | Dauer: |  |
| Benutzerrolle(n): |  | Zuständigkeit: | <Geben Sie den Serviceanbieter, einen Kunden oder einen Serviceanbieter zusammen mit einem Kunden an.> |

Verwendungszweck

Das Verfahren in diesem Abschnitt enthält eine Anleitung zum Anlegen von Materialstammdaten (Produktstammdaten). Die zur Verfügung stehenden Apps hängen von der Ihnen zugeordneten Rolle ab. Aus diesem Grund sind zwei Optionen verfügbar.

Vorgehensweise: Option 1 – Material anlegen

Gehen Sie folgendermaßen vor, wenn Sie aufgrund Ihrer Benutzerrolle auf die App Material anlegen(MM01) zugreifen können.

| Testschrittnummer | Bezeichnung des Testschritts | Anweisungen | Erwartetes Ergebnis | Kommentare |
| --- | --- | --- | --- | --- |
| 1 | Anmelden | Melden Sie sich am SAP Fiori Launchpad als Stammdatenexperte – Produktdaten an. | Das SAP Fiori Launchpad wird angezeigt. |  |
| 2 | SAP-Fiori-App aufrufen | Öffnen Sie Material anlegen(MM01). | Die Sicht Material anlegen(MM01) wird angezeigt. |  |
| 3 | Materialgrunddaten eingeben | Geben Sie in Material anlegen (Einstieg) folgendes ein:Material: MaterialnummerBranche: MHinweis Ist das Eingabefeld Branche ausgeblendet, ist keine Eingabe erforderlich. Wird die Branche nicht zur Eingabe angeboten, wird nicht bekannt im Feld eingetragen.Materialart: ServiceproduktWählen Sie Sichtenauswahl. | In einem neuen Fenster wird das Bild Sichtenauswahl angezeigt. |  |
| 4 | Sichten wählen | Wählen Sie in der Sichtenauswahl die Sicht Grunddaten 1 aus, und wählen Sie Weiter. | Die Sicht Material anlegen ... (Serviceprodukt) wird geöffnet. |  |
| 5 | Grunddaten eingeben | Geben Sie in der Sicht Material ... (Serviceprodukt) auf der Registerkarte Grunddaten 1 eine Materialbeschreibung (Kurztext) ein. |  |  |
| 6 | Grunddaten eingeben | Geben Sie auf der Registerkarte Grunddaten 1 im Abschnitt Allgemeine Daten Beschreibungen für die folgenden Einträge ein:BasismengeneinheitMaterialgruppeAllg. PosTypGrp |  |  |
| 7 | Daten sichern | Wählen Sie unten rechts im Bild Sichern, um Ihre Daten zu sichern. | Das Bild Material anlegen (Einstieg) wird geöffnet.Die Grunddaten werden erzeugt und gesichert. |  |

Vorgehensweise: Option 2 – Produktstammdaten verwalten

Gehen Sie folgendermaßen vor, wenn Sie aufgrund Ihrer Benutzerrolle auf die App Produktstammdaten verwalten(F1602) zugreifen können.

| Testschrittnummer | Bezeichnung des Testschritts | Anweisungen | Erwartetes Ergebnis | Kommentare |
| --- | --- | --- | --- | --- |
| 1 | Anmelden | Melden Sie sich am SAP Fiori Launchpad als Stammdatenexperte – Produktdaten an. | Das SAP Fiori Launchpad wird angezeigt. |  |
| 2 | SAP-Fiori-App aufrufen | Öffnen Sie Produktstammdaten verwalten(F1602). | Das Bild Produktstammdaten verwalten(F1602) wird angezeigt. |  |
| 3 | "Neuen Produktstamm anlegen" auswählen | Wählen Sie in der Sicht Produktstammdaten verwalten die Option Anlegen. | Das Bild Stammdatensatz anlegen wird angezeigt. |  |
| 4 | Daten in Pflichtfelder eingeben | Nehmen Sie auf dem Einstiegsbild Stammdatensatz anlegen die folgenden Einträge vor:Produktnummer: z.B. Z …Geben Sie entweder eine externe alphanumerische ID ein, die mit einem alphanumerischen Zeichen beginnen muss, oder lassen Sie das Feld frei; in diesem Fall weist das System automatisch eine numerische ID zu.Weitere Informationen zur Produktnummer finden Sie im vorangehenden Abschnitt Materialart und Nummernkreise.Produktart: SERVProduktgruppe: z.B. L002Basis-ME: z.B. HBeschreibung: beliebige Beschreibung |  |  |
| 5 | Wählen Sie OK. | Wählen Sie in der Sicht Produktstamm verwalten OK. | Die Sicht Produktstamm verwalten wird angezeigt. |  |
| 6 | Grunddaten eingeben | Geben Sie unter Produkt > Allgemeine Informationen > Grunddaten die folgenden Daten ein:Sparte: z.B. 00 |  |  |
| 7 | Hinzufügen (+) wählen | Wählen Sie unter Produkt > Allgemeine Informationen > Bezeichnungen die Option + (Hinzufügen). | Die Sicht Bezeichnung Produktstamm wird angezeigt.Einige Dateien sind bereits aus dem vorherigen Schritt mit Daten gefüllt. |  |
| 8 | Beschreibungsdaten eingeben | Geben Sie in der Sicht Beschreibungen folgende Daten ein:Sprache: z.B. Deutsch.Produkt: <Ihre Beschreibung> |  |  |
| 9 | Daten sichern | Wählen Sie Sichern. | Eine Systemmeldung bestätigt, dass das Objekt gesichert wurde. |  |

### Materialstammdaten (Serviceprodukt) anlegen – Verkaufsdaten (Umsatzsteuerdaten)

Testverwaltung

Kundenprojekt: Füllen Sie die projektbezogenen Teile aus.

|  |  |  |  |
| --- | --- | --- | --- |
| Testfall-ID | <X.XX> | Testdatum: |  |
| Testername: |  | Dauer: |  |
| Benutzerrolle(n): |  | Zuständigkeit: | <Geben Sie den Serviceanbieter, einen Kunden oder einen Serviceanbieter zusammen mit einem Kunden an.> |

Zweck

Das Verfahren in diesem Abschnitt enthält eine Anleitung zum Anlegen von Materialstammdaten (Dienstleistungsstammdaten). Die zur Verfügung stehenden Apps hängen von der Ihnen zugeordneten Rolle ab. Aus diesem Grund sind zwei Optionen verfügbar.

Voraussetzung

Sie müssen den vorherigen Abschnitt Materialstammdaten (Serviceprodukt) anlegen - Grunddaten erst abschließen, bevor Sie mit diesem Abschnitt fortfahren können.

Beginnen Sie mit dieser Vorgehensweise, nachdem Sie die eingegebenen Grunddaten gesichert haben, wie bei der vorherigen Vorgehensweise erläutert.

Vorgehensweise: Option 1 – Material anlegen

Gehen Sie folgendermaßen vor, wenn Sie aufgrund Ihrer Benutzerrolle auf die App Material anlegen(MM01) zugreifen können.

| Testschrittnummer | Bezeichnung des Testschritts | Anweisungen | Erwartetes Ergebnis | Kommentare |
| --- | --- | --- | --- | --- |
| 1 | Anmelden | Melden Sie sich am SAP Fiori Launchpad als Stammdatenexperte – Produktdaten an. | Das SAP Fiori Launchpad wird angezeigt. |  |
| 2 | SAP-Fiori-App aufrufen | Öffnen Sie Material anlegen(MM01). | Die Sicht Material anlegen(MM01) wird angezeigt. |  |
| 3 | Materialgrunddaten eingeben | Nehmen Sie auf Material anlegen (Einstieg), die folgenden Einträge vor:Material: MaterialnummerBranche: MHinweis Hinweis: Ist das Eingabefeld Branche ausgeblendet, ist keine Eingabe erforderlich. Wird die Branche nicht zur Eingabe angeboten, wird nicht bekannt im Feld eingetragen.Materialart: SERV ServiceproduktWählen Sie Sichtenauswahl. | Nachdem Sie die Einträge vorgenommen haben, wird ein neues Fenster Sichtenauswahl geöffnet. |  |
| 4 | Sichten wählen | Wählen Sie im Fenster Sichtenauswahl die Sichten Vertrieb: VerkaufsorgDaten 1, Vertrieb: VerkaufsorgDaten 2 und Vertrieb: Allg./Werksdaten aus, und wählen Sie dann Weiter.Hinweis Nur für Polen: Wählen Sie außerdem Außenhandel - Exportdaten, um die PKWiU-Klassifikationsnummer einzugeben. | Ein Fenster mit Organisationsebenen wird angezeigt. |  |
| 5 | Organisationsebenendaten eingeben | Geben Sie im Bild Organisationsebenen im Abschnitt Organisationsebene Beschreibungen für folgende Einträge ein:WerkVerkaufsorg.Vertriebs- KanalWählen Sie Weiter.Hinweis Im unteren Bildbereich wird folgende Information angezeigt: Das Material existiert bereits und wird erweitert. | Die Sicht Material anlegen ... (Dienstleistungen) wird angezeigt. |  |
| 6 | Verkaufsdaten eingeben | Nehmen Sie auf dem Bild Material ... (Serviceprodukt) auf der Registerkarte Verkaufsorganisation 1 im Bereich Allgemeine Daten folgenden Eintrag vor:BasismengeneinheitAuslieferungswerk |  |  |
| 7 | Verkaufsdaten eingeben | Nehmen Sie auf dem Bild Material ... (Serviceprodukt) auf der Registerkarte Vertrieb: Verkaufsorganisation 1 im Bereich Steuerdaten folgende Einträge vor:Steuerklassifikation: 1Hinweis Der eingegebene Wert zeigt an, dass das Material (für gewöhnlich) voll steuerpflichtig ist.Nur für Brasilien:Nehmen Sie im Bereich Steuerdaten folgende Einträge vor:Land: BRSteuerkategorie: IBRXSteuerklassifizierung: Entweder 1 für Material oder 2 für Dienstleistungen | Verkauf: Verkaufsorganisation 2 wird angezeigt. |  |
| 8 | Verkaufsdaten eingeben | Nehmen Sie auf der Registerkarte Vertrieb: Verkaufsorganisation 2 im Abschnitt Gruppierungsbegriffe den folgenden Eintrag vor:allg.Pos.typenGruppePositionstypengruppe | Die nächste Registerkarte Vertrieb: Allg./Werk wird angezeigt. |  |
| 9 | Verkaufsdaten eingeben | Nehmen Sie auf der Registerkarte Vertrieb: Allg./Werk im Abschnitt Allgemeine Werksparameter folgende Einträge vor:Profitcenter |  |  |
| Nur für Polen: | Verkaufsdaten eingeben | Geben Sie im Abschnitt International Trade: Export die folgenden Daten ein:Steuerungscode: z.B. 41.00.30.0 | Der PKWiU-Code für Polen ist gepflegt. |  |
| 10 | Daten sichern | Wählen Sie im unteren Bildbereich Sichern. | Ihre Daten werden gesichert. |  |

Vorgehensweise: Option 2 – Produktstammdaten verwalten

Gehen Sie folgendermaßen vor, wenn Sie aufgrund Ihrer Benutzerrolle auf die App Produktstammdaten verwalten(F1602) zugreifen können.

| Testschrittnummer | Bezeichnung des Testschritts | Anweisungen | Erwartetes Ergebnis | Kommentare |
| --- | --- | --- | --- | --- |
| 1 | Anmelden | Melden Sie sich am SAP Fiori Launchpad als Stammdatenexperte – Produktdaten an. | Das SAP Fiori Launchpad wird angezeigt. |  |
| 2 | SAP-Fiori-App aufrufen | Öffnen Sie Produktstammdaten verwalten(F1602). | Die App Produktstammdaten verwalten(F1602) wird geöffnet, und verschiedene Suchfelder werden angezeigt. |  |
| 3 | Produkt suchen und zur Bearbeitung öffnen | Suchen Sie nach dem zuvor angelegten Produkt, indem Sie Produktnummer im Suchfeld Produkt eingeben.Wählen Sie das Produkt aus der Liste aus. Sie gelangen daraufhin zur Sicht Produkt.Wählen Sie Bearbeiten. | Das Produkt wird im Bearbeitungsmodus angezeigt (die Felder sind eingabebereit). |  |
| 4 | Vertriebslinien auswählen | Wählen Sie in der Sicht Produkt die Registerkarte Vertriebslinien. | Die Registerkarte Vertriebslinien wird angezeigt. |  |
| 5 | Hinzufügen (+) wählen | Wählen Sie auf der Registerkarte Vertriebslinien die Option + (Hinzufügen). | Das Bild Vertriebslinien wird im Änderungsmodus geöffnet. |  |
| Nicht relevant für Brasilien | Vertriebsliniendaten eingeben | Geben Sie in Vertriebslinien folgende Daten ein:Im Abschnitt ALLGEMEINE DATEN - Allgemeine Informationen:Verkaufsorganisation: VerkaufsorganisationsnummerHinweis Der Organisationseinheitswert richtet sich nach den Optionen in der Wertehilfe.Vertriebsweg: z.B. 10Lieferwerk: WerksnummerIm Abschnitt GRUPPIERUNGSBEGRIFFE:Positionstypengruppe: z.B. SERVIm Bildbereich UMSATZSTEUER:Land: LändercodeSteuerkategorie: z.B. TTX1Steuerklassifikation: z.B. entweder 1 für Material oder 2 für Dienstleistungen. Beispiel Steuerklassifikation: 1 volle Steuer, wenn Sie die Steuerkondition UTXJ für die USA verwenden.Hinweis Die Steuerklassifikation hängt von den spezifischen Anforderungen des jeweiligen Landes bzw. der Region ab. Die Steuerklassifizierung in den Materialstamm- und Kundenstammtabellen bestimmt die Eingaben der Prozenteingaben. |  |  |
| 6 | Zur Hauptsicht zurückkehren | Wählen Sie Übernehmen, um zur Sicht Produkte zurückzukehren. | Die Sicht Produkt wird angezeigt. |  |
| 7 | Daten sichern | Wählen Sie Sichern. | Eine Systemmeldung bestätigt, dass das Objekt gesichert wurde. |  |

### Materialstammdaten (Serviceproduktstammdaten) anlegen – Einkaufsdaten

Testverwaltung

Kundenprojekt: Füllen Sie die projektbezogenen Teile aus.

|  |  |  |  |
| --- | --- | --- | --- |
| Testfall-ID | <X.XX> | Testdatum: |  |
| Testername: |  | Dauer: |  |
| Benutzerrolle(n): |  | Zuständigkeit: | <Geben Sie den Serviceanbieter, einen Kunden oder einen Serviceanbieter zusammen mit einem Kunden an.> |

Zweck

Das Verfahren in diesem Abschnitt enthält eine Anleitung zum Anlegen von Materialstammdaten (Dienstleistungsstammdaten). Die zur Verfügung stehenden Apps hängen von der Ihnen zugeordneten Rolle ab. Aus diesem Grund sind zwei Optionen verfügbar.

Voraussetzung

Sie müssen die vorherige Vorgehensweise Materialstammdaten (Serviceproduktstammdaten) anlegen - Grunddaten erst abschließen, bevor Sie mit diesem Abschnitt fortfahren können.

Beginnen Sie mit dieser Vorgehensweise, nachdem Sie die eingegebenen Grunddaten gesichert haben, wie bei der vorherigen Vorgehensweise erläutert.

Vorgehensweise: Option 1 – Material anlegen

Gehen Sie folgendermaßen vor, wenn Sie aufgrund Ihrer Benutzerrolle auf die App Material anlegen(MM01) zugreifen können.

| Testschrittnummer | Bezeichnung des Testschritts | Anweisungen | Erwartetes Ergebnis | Kommentare |
| --- | --- | --- | --- | --- |
| 1 | Anmelden | Melden Sie sich am SAP Fiori Launchpad als Stammdatenexperte – Produktdaten an. | Das SAP Fiori Launchpad wird angezeigt. |  |
| 2 | SAP-Fiori-App aufrufen | Öffnen Sie Material anlegen(MM01). | Die Sicht Material anlegen(MM01) wird angezeigt. |  |
| 3 | Materialgrunddaten eingeben | Nehmen Sie auf dem Bild Material anlegen (Einstieg), die folgenden Einträge vor:Material: MaterialnummerBranche: MHinweis Ist das Eingabefeld Branche ausgeblendet, ist keine Eingabe erforderlich. Wird die Branche nicht zur Eingabe angeboten, wird nicht bekannt im Feld eingetragen.Materialart: SERV ServiceproduktWählen Sie Sichtenauswahl. | Das Bild Sichtenauswahl wird angezeigt. |  |
| 4 | Sichten wählen | Wählen Sie im Fenster Sichtenauswahl die Sicht Einkauf aus und wählen Sie Weiter. | Das Bild Organisationsebenen wird angezeigt. |  |
| 5 | Organisationsebenendaten eingeben | Nehmen Sie auf dem Bild Organisationsebenen im Abschnitt Organisationsebene die folgenden Einträge vor:Werk: WerksnummerWählen Sie Weiter.Hinweis Im unteren Teil des Bildes wird folgende Meldung angezeigt: Das Material existiert bereits und wird erweitert. | Die Sicht Material anlegen ... (Dienstleistungen) wird geöffnet. |  |
| Nicht relevant für Brasilien | Einkaufsdaten eingeben | Nehmen Sie auf dem Bild Material (Serviceprodukt) auf der Registerkarte Einkauf im Abschnitt Allgemeine Daten die folgenden Einträge vor:Basismengeneinheit: z.B. HMaterialgruppe: z.B. YBPM02 |  |  |
| 6 | Daten sichern | Wählen Sie im unteren Bildbereich Sichern. | Ihre Daten werden gesichert. |  |

Vorgehensweise: Option 2 – Produktstammdaten verwalten

Gehen Sie folgendermaßen vor, wenn Sie aufgrund Ihrer Benutzerrolle auf die App Produktstammdaten verwalten(F1602) zugreifen können.

| Testschrittnummer | Bezeichnung des Testschritts | Anweisungen | Erwartetes Ergebnis | Kommentare |
| --- | --- | --- | --- | --- |
| 1 | Anmelden | Melden Sie sich am SAP Fiori Launchpad als Stammdatenexperte – Produktdaten an. | Das SAP Fiori Launchpad wird angezeigt. |  |
| 2 | SAP-Fiori-App aufrufen | Öffnen Sie Produktstammdaten verwalten(F1602). | Die App Produktstammdaten verwalten(F1602) wird geöffnet, und verschiedene Suchfelder werden angezeigt. |  |
| 3 | Produkt suchen und zur Bearbeitung öffnen | Suchen Sie nach dem zuvor angelegten Produkt, indem Sie Produktnummer im Suchfeld Produkt eingeben.Wählen Sie das Produkt aus der Liste aus. Sie gelangen daraufhin zur Sicht Produkt.Wählen Sie Bearbeiten. | Das Produkt wird im Bearbeitungsmodus angezeigt (die Felder sind eingabebereit). |  |
| 4 | Einkaufsdaten auswählen | Wählen Sie in der Sicht Produkt die Option Einkauf. | Die Sicht Einkauf wird angezeigt. |  |
| 5 | Einkaufsdaten eingeben | Geben Sie in der Sicht Einkauf folgende Daten ein:Einkaufswerteschlüssel: z.B. 1 |  |  |
| 6 | Daten sichern | Wählen Sie Sichern. | Eine Systemmeldung bestätigt, dass das Objekt gesichert wurde. |  |

### Materialstammdaten (Serviceproduktstammdaten) anlegen – Buchhaltungsdaten (Bewertungsbereichsdaten)

Testverwaltung

Kundenprojekt: Füllen Sie die projektbezogenen Teile aus.

|  |  |  |  |
| --- | --- | --- | --- |
| Testfall-ID | <X.XX> | Testdatum: |  |
| Testername: |  | Dauer: |  |
| Benutzerrolle(n): |  | Zuständigkeit: | <Geben Sie den Serviceanbieter, einen Kunden oder einen Serviceanbieter zusammen mit einem Kunden an.> |

Zweck

Das Verfahren in diesem Abschnitt enthält eine Anleitung zum Anlegen von Materialstammdaten (Serviceproduktstammdaten). Die zur Verfügung stehenden Apps hängen von der Ihnen zugeordneten Rolle ab. Aus diesem Grund sind zwei Optionen verfügbar.

Voraussetzung

Sie müssen die vorherige Vorgehensweise Materialstammdaten (Serviceproduktsmmdaten) anlegen - Grunddaten erst abschließen, bevor Sie mit diesem Abschnitt fortfahren können.

Beginnen Sie mit dieser Vorgehensweise, nachdem Sie die eingegebenen Grunddaten gesichert haben, wie bei der vorherigen Vorgehensweise erläutert.

Vorgehensweise: Option 1 – Material anlegen

Gehen Sie folgendermaßen vor, wenn Sie aufgrund Ihrer Benutzerrolle auf die App Material anlegen(MM01) zugreifen können.

| Testschrittnummer | Bezeichnung des Testschritts | Anweisungen | Erwartetes Ergebnis | Kommentare |
| --- | --- | --- | --- | --- |
| 1 | Anmelden | Melden Sie sich am SAP Fiori Launchpad als Stammdatenexperte – Produktdaten an. | Das SAP Fiori Launchpad wird angezeigt. |  |
| 2 | SAP-Fiori-App aufrufen | Öffnen Sie Material anlegen(MM01). | Die Sicht Material anlegen(MM01) wird angezeigt. |  |
| 3 | Materialgrunddaten eingeben | Nehmen Sie auf dem Bild Material anlegen (Einstieg), die folgenden Einträge vor:Material: MaterialnummerBranche: MHinweis Ist das Eingabefeld Branche ausgeblendet, ist keine Eingabe erforderlich. Wird die Branche nicht zur Eingabe angeboten, wird nicht bekannt im Feld eingetragen.Materialart: SERV ServiceproduktWählen Sie Sichtenauswahl. | Die Sichtenauswahl wird geöffnet. |  |
| 4 | Sichten wählen | Wählen Sie im Fenster Sichtenauswahl die folgenden Sichten aus:Buchhaltung 1Wählen Sie Weiter. | Das Bild Organisationsebenen wird angezeigt. |  |
| 5 | Organisationsebenendaten eingeben | Nehmen Sie auf dem Bild Organisationsebenen im Abschnitt Organisationsebene die folgenden Einträge vor:WerkHinweis Im unteren Teil des Bildes wird folgende Information angezeigt: Das Material existiert bereits und wird erweitert. | Die Sicht Material anlegen ... (Dienstleistungen) wird geöffnet. |  |
| 6 | Buchhaltungsdaten eingeben | Nehmen Sie auf dem Bild Material anlegen ... (Serviceprodukt) auf der Registerkarte Buchhaltung 1 im Abschnitt Aktuelle Bewertung den folgenden Eintrag vor:Bewertungsklasse: Nummer |  |  |
| 7 | Buchhaltungsdaten eingeben | Nehmen Sie im Bereich Preise und Werte die folgenden Einträge vor:Per. Stückpreis: z.B. 1 |  |  |
| 8 | Eingaben bestätigen (für alle Länder/Regionen außer Brasilien) | Auf der Registerkarte Buchhaltung 2 sind keine Eingaben erforderlich. |  |  |
| 9 | Daten sichern | Wählen Sie im unteren Bildbereich Sichern. | Das Fenster Stammdaten - Produkt wird angezeigt.Ihre Daten werden gesichert. |  |

Vorgehensweise: Option 2 – Produktstammdaten verwalten

Gehen Sie folgendermaßen vor, wenn Sie aufgrund Ihrer Benutzerrolle auf die App Produktstammdaten verwalten(F1602) zugreifen können.

| Testschrittnummer | Bezeichnung des Testschritts | Anweisungen | Erwartetes Ergebnis | Kommentare |
| --- | --- | --- | --- | --- |
| 1 | Anmelden | Melden Sie sich am SAP Fiori Launchpad als Stammdatenexperte – Produktdaten an. | Das SAP Fiori Launchpad wird angezeigt. |  |
| 2 | SAP-Fiori-App aufrufen | Öffnen Sie Produktstammdaten verwalten(F1602). | Die App Produktstammdaten verwalten(F1602) wird geöffnet, und verschiedene Suchfelder werden angezeigt. |  |
| 3 | Produkt suchen und zur Bearbeitung öffnen | Suchen Sie nach dem zuvor angelegten Produkt, indem Sie Produktnummer im Suchfeld Produkt eingeben.Wählen Sie das Produkt aus der Liste aus. Sie gelangen daraufhin zur Sicht Produkt.Wählen Sie Bearbeiten. | Das Produkt wird im Bearbeitungsmodus angezeigt (die Felder sind eingabebereit). |  |
| 4 | Bewertungskreisdaten auswählen | Wählen Sie in der Sicht Produkt die Registerkarte Bewertungskreise. | Die Registerkarte Bewertungskreise wird angezeigt. |  |
| 5 | Hinzufügen (+) wählen | Wählen Sie im Abschnitt Bewertungskreise die Option + (Hinzufügen). | Bewertung wird im Bearbeitungsmodus geöffnet. |  |
| Nicht relevant für Brasilien | Bewertungskreisdaten eingeben | Geben Sie in der Sicht Bewertung folgende Daten ein:Bewertungskreis: BewertungskreisnummerBewertungsklasse: z.B. 3200 |  |  |
| 6 | Zum Hauptbild zurückkehren | Wählen Sie Übernehmen, um zur Sicht Produkt zurückzukehren. | Die Sicht Produktstamm verwalten wird angezeigt. |  |
| 7 | Daten sichern | Wählen Sie Sichern. | Eine Systemmeldung bestätigt, dass das Objekt gesichert wurde. |  |

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
- related-to :: [[02-business-partner-and-product-master-data/master-data-script-create-product-master-of-type-service-product-mds-3]]
- related-to :: [[02-business-partner-and-product-master-data/mds-31x-307]]
- related-to :: [[02-business-partner-and-product-master-data/mds-31x-309]]
- related-to :: [[02-business-partner-and-product-master-data/script-de-dados-mestre-criar-mestre-de-produtos-do-tipo-produto-de-ser]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/31X_S4CLD2608_Master_Data_DE_XX.docx` — full document · extracted with `mammoth` · 32,539 chars in the whole document
