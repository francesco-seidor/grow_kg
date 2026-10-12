---
id: 02-business-partner-and-product-master-data/stammdatenskript-produktstamm-fur-materialart-nichtlagermaterial-anleg
title: "Stammdatenskript: Produktstamm für Materialart \"Nichtlagermaterial\" anlegen – MDS (31Y) (31Y_S4CLD2608_Master_Data_DE_XX)"
description: "German SAP S/4HANA Cloud Public Edition 2608 master data script (31Y): creating a non-stock material (NLAG) via MM01 or F1602, covering basic, sales, purchasing and accounting data."
cluster: 02-business-partner-and-product-master-data
tags: [kb/business-partner-and-product-master-data, topic/product-master-non-stock-and-service]
aliases: [31Y_S4CLD2608_Master_Data_DE_XX]
keywords: ["Product Master: Non-Stock Materials and Service Products", non-stock material, product master data, basic data, sales data, purchasing data, accounting data, number ranges, organizational units, user roles]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/31Y_S4CLD2608_Master_Data_DE_XX.docx]
confidence: high
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-310
topic: 02-business-partner-and-product-master-data/product-master-non-stock-and-service
language: DE
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Stammdatenskript: Produktstamm für Materialart "Nichtlagermaterial" anlegen – MDS (31Y) (31Y_S4CLD2608_Master_Data_DE_XX)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/31Y_S4CLD2608_Master_Data_DE_XX.docx`, extracted with `mammoth`. Grouped under **Product Master: Non-Stock Materials and Service Products** in Business Partner and Product Master Data. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

| <!-- image omitted: unnamed --> | StammdatenskriptSAP S/4HANA Cloud Public Edition - 02-07-26 |
| --- | --- |
|  | Produktstamm für Materialart "Nichtlagermaterial" anlegen – MDS (31Y) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Inhaltsverzeichnis

[1 Verwendungszweck 2](#_Toc233889618)

[2 Voraussetzungen 3](#_Toc233889619)

[2.1 Systemzugriff 3](#_Toc233889620)

[2.2 Rollen 3](#_Toc233889621)

[2.3 Erforderliche Organisationseinheiten 3](#_Toc233889622)

[2.4 Obligatorische und operative Stammdaten 4](#_Toc233889623)

[2.5 Wesentliche Parameter für die Datenerstellung 5](#_Toc233889624)

[2.5.1 Materialart und Nummernkreise 5](#_Toc233889625)

[2.5.2 Branche 5](#_Toc233889626)

[3 Übersichtstabelle 6](#_Toc233889627)

[4 Testverfahren 7](#_Toc233889628)

[4.1 Materialstammdaten (Nichtlagermaterial) anlegen – Grunddaten 7](#_Toc233889629)

[4.2 Materialstammdaten (Nichtlagermaterial) anlegen – Verkaufsdaten (Umsatzsteuerdaten) 9](#_Toc233889630)

[4.3 Materialstammdaten (Nichtlagermaterial) anlegen – Einkaufsdaten 13](#_Toc233889631)

[4.4 Materialstammdaten (Nichtlagermaterial) anlegen – Buchhaltungsdaten (Bewertungsbereichsdaten) 15](#_Toc233889632)

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

| Name (Rollenvorlage) | ID (Rollenvorlage) | Name (Launchpad-Bereich) | ID (Launchpad-Bereich) | Anmeldung |
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

In diesem Abschnitt geben Sie eine Liste mit Schritten an, die ein Benutzer beim Anlegen eines Datensatzes durchführt. Jedes logische, aussagekräftige Segment eines Stammdatenobjekts sollte zu einem separaten Schritt führen (z.B. organisationseinheitsabhängige Datensegmente usw.).

Dieser Umfangsbestandteil umfasst die verschiedenen Schritte in der folgenden Tabelle:

|  |
| --- |
| Hinweis Wenn Ihr Systemadministrator Bereiche und Seiten auf dem SAP Fiori Launchpad aktiviert hat, enthält die Startseite nur die wesentlichen Apps, mit denen die typischen Aufgaben einer Benutzerrolle ausgeführt werden können.Alle anderen (suchbaren) Apps, die nicht auf der Startseite enthalten sind, finden Sie über die Suchleiste ([2434549](https://me.sap.com/notes/2434549)).Wenn Sie die Startseite personalisieren und versteckte Apps hinzufügen möchten, wechseln Sie in Ihr Benutzerprofil und wählen Sie App Finder. |

| Prozessschritt | Benutzerrolle | Vorgang/App | Erwartete Ergebnisse |
| --- | --- | --- | --- |
| [Materialstammdaten (Nichtlagermaterial) anlegen – Grunddaten](#unique_11) [Seite ] 7 | Stammdatenexperte – Produktdaten | Material anlegen(MM01)/Produktstammdaten verwalten(F1602) | Materialstammdaten - Grunddaten werden angelegt. |
| [Materialstammdaten (Nichtlagermaterial) anlegen – Verkaufsdaten (Umsatzsteuerdaten)](#unique_12) [Seite ] 9 | Stammdatenexperte – Produktdaten | Material anlegen(MM01)/Produktstammdaten verwalten(F1602) | Materialstammdaten - Verkaufsdaten werden angelegt.. |
| [Materialstammdaten (Nichtlagermaterial) anlegen – Einkaufsdaten](#unique_13) [Seite ] 13 | Stammdatenexperte – Produktdaten | Material anlegen(MM01)/Produktstammdaten verwalten(F1602) | Materialstammdaten - Einkaufsdaten werden angelegt. |
| [Materialstammdaten (Nichtlagermaterial) anlegen – Buchhaltungsdaten (Bewertungsbereichsdaten)](#unique_14) [Seite ] 15 | Stammdatenexperte – Produktdaten | Material anlegen(MM01)/Produktstammdaten verwalten(F1602) | Materialstammdaten - Buchhaltungsdaten (Bewertungsbereichsdaten) werden angelegt. |

## Testverfahren

In diesem Abschnitt werden die Testverfahren für den jeweiligen Prozessschritt beschrieben, der zum betreffenden Umfangsbestandteil gehört.

### Materialstammdaten (Nichtlagermaterial) anlegen – Grunddaten

Testverwaltung

Kundenprojekt: Füllen Sie die projektbezogenen Teile aus.

|  |  |  |  |
| --- | --- | --- | --- |
| Testfall-ID | <X.XX> | Testdatum: |  |
| Testername: |  | Dauer: |  |
| Benutzerrolle(n): |  | Zuständigkeit: | <Geben Sie den Serviceanbieter, einen Kunden oder einen Serviceanbieter zusammen mit einem Kunden an.> |

Zweck

Das Verfahren in diesem Abschnitt enthält eine Anleitung zum Anlegen von Materialstammdaten (Produktstammdaten). Die zur Verfügung stehenden Apps hängen von der Ihnen zugeordneten Rolle ab. Aus diesem Grund sind zwei Optionen verfügbar.

Vorgehensweise: Option 1 – Material anlegen

Gehen Sie folgendermaßen vor, wenn Sie aufgrund Ihrer Benutzerrolle auf die App Material anlegen(MM01) zugreifen können.

| Testschrittnummer | Bezeichnung des Testschritts | Anweisung | Erwartetes Ergebnis | Kommentare |
| --- | --- | --- | --- | --- |
| 1 | Anmelden | Melden Sie sich am SAP Fiori Launchpad als Stammdatenexperte – Produktdaten an. | Das SAP Fiori Launchpad wird angezeigt. |  |
| 2 | SAP-Fiori-App aufrufen | Wählen Sie Material anlegen(MM01). | Das Bild Material anlegen(MM01) wird angezeigt. |  |
| 3 | Materialgrunddaten eingeben | Geben Sie in Material anlegen (Einstieg) folgendes ein:Material: MaterialnummerBranche: MHinweis Ist das Eingabefeld Branche ausgeblendet, ist keine Eingabe erforderlich. Wird die Branche nicht zur Eingabe angeboten, wird nicht bekannt im Feld eingetragen.Materialart: NichtlagermaterialWählen Sie Sichtenauswahl. | In einem neuen Fenster wird das Bild Sichtenauswahl angezeigt. |  |
| 4 | Sichten wählen | Wählen Sie in der Sichtenauswahl die Sicht Grunddaten 1 aus, und wählen Sie Weiter. | Das Bild Material ... anlegen (Nichtlagermaterial) wird geöffnet. |  |
| 5 | Grunddaten eingeben | Geben Sie auf dem Bild Material ... (Nichtlagermaterial) auf der Registerkarte Grunddaten 1 eine Materialbeschreibung (Kurztext) ein. |  |  |
| 6 | Grunddaten eingeben | Geben Sie auf der Registerkarte Grunddaten 1 im Abschnitt Allgemeine Daten Beschreibungen für die folgenden Einträge ein:BasismengeneinheitMaterialgruppeAllg. PosTypGrp |  |  |
| 7 | Daten sichern | Wählen Sie unten rechts im Bild Sichern, um Ihre Daten zu sichern. | Das Bild Material anlegen (Einstieg) wird geöffnet.Die Grunddaten werden erzeugt und gesichert. |  |

Vorgehensweise: Option 2 – Produktstammdaten verwalten

Gehen Sie folgendermaßen vor, wenn Sie aufgrund Ihrer Benutzerrolle auf die App Produktstammdaten verwalten(F1602) zugreifen können.

| Testschrittnummer | Bezeichnung des Testschritts | Anweisung | Erwartetes Ergebnis | Kommentare |
| --- | --- | --- | --- | --- |
| 1 | Anmelden | Melden Sie sich am SAP Fiori Launchpad als Stammdatenexperte – Produktdaten an. | Das SAP Fiori Launchpad wird angezeigt. |  |
| 2 | SAP-Fiori-App aufrufen | Öffnen Sie Produktstammdaten verwalten(F1602). |  |  |
| 3 | "Neuen Produktstamm anlegen" auswählen | Wählen Sie Anlegen. | Das Bild Stammdatensatz anlegen wird angezeigt. |  |
| 4 | Daten in Pflichtfelder eingeben | Nehmen Sie auf dem Einstiegsbild Stammdatensatz anlegen die folgenden Einträge vor:Produktnummer: z.B. Z …Geben Sie entweder eine externe alphanumerische ID ein, die mit einem alphanumerischen Zeichen beginnen muss, oder lassen Sie das Feld frei; in diesem Fall weist das System automatisch eine numerische ID zu.Weitere Informationen zur Produktnummer finden Sie im vorangehenden Abschnitt Materialart und Nummernkreise.Produktart: NLAGProduktgruppe: z.B. YBPM01Basis-ME: z.B. StückBeschreibung: beliebige Beschreibung |  |  |
| 5 | Wählen Sie OK. | Wählen Sie in der Sicht Produktstamm verwalten OK. | Die Sicht Produktstamm verwalten wird angezeigt. |  |
| 6 | Grunddaten eingeben | Geben Sie in der Sicht Produktstamm verwalten > GRUNDDATEN > Grunddaten die folgenden Daten ein:Sparte: z.B. 00 |  |  |
| 7 | Hinzufügen (+) wählen | In der Sicht Produktstamm verwalten > GRUNDDATEN > Bezeichnungen wählen Sie + (Hinzufügen). | Die Sicht Bezeichnung Produktstamm wird angezeigt.Einige Dateien sind bereits aus dem vorherigen Schritt mit Daten gefüllt. |  |
| 8 | Beschreibungsdaten eingeben | Geben Sie in der Sicht Beschreibungen folgende Daten ein:Sprache: z.B. Deutsch.Produktbezeichnung: <Ihre Beschreibung> |  |  |
| 9 | Daten sichern | Wählen Sie Sichern. | Eine Systemmeldung bestätigt, dass das Objekt gesichert wurde. |  |

### Materialstammdaten (Nichtlagermaterial) anlegen – Verkaufsdaten (Umsatzsteuerdaten)

Testverwaltung

Kundenprojekt: Füllen Sie die projektbezogenen Teile aus.

|  |  |  |  |
| --- | --- | --- | --- |
| Testfall-ID | <X.XX> | Testdatum: |  |
| Testername: |  | Dauer: |  |
| Benutzerrolle(n): |  | Zuständigkeit: | <Geben Sie den Serviceanbieter, einen Kunden oder einen Serviceanbieter zusammen mit einem Kunden an.> |

Zweck

Das Verfahren in diesem Abschnitt enthält eine Anleitung zum Anlegen von Materialstammdaten (Nichtlagermaterial). Die zur Verfügung stehenden Apps hängen von der Ihnen zugeordneten Rolle ab. Aus diesem Grund sind zwei Optionen verfügbar.

Voraussetzung

Sie müssen den vorherigen Abschnitt Materialstammdaten (Nichtlagermaterial) anlegen - Grunddaten erst abschließen, bevor Sie mit diesem Abschnitt fortfahren können.

Beginnen Sie mit dieser Vorgehensweise, nachdem Sie die eingegebenen Grunddaten gesichert haben, wie bei der vorherigen Vorgehensweise erläutert.

Vorgehensweise: Option 1 – Material anlegen

Gehen Sie folgendermaßen vor, wenn Sie aufgrund Ihrer Benutzerrolle auf die App Material anlegen(MM01) zugreifen können.

| Testschrittnummer | Bezeichnung des Testschritts | Anweisung | Erwartetes Ergebnis | Kommentare |
| --- | --- | --- | --- | --- |
| 1 | Anmelden | Melden Sie sich am SAP Fiori Launchpad als Stammdatenexperte – Produktdaten an. | Das SAP Fiori Launchpad wird angezeigt. |  |
| 2 | SAP-Fiori-App aufrufen | Öffnen Sie Material anlegen(MM01). | Die Sicht Material anlegen(MM01) wird angezeigt. |  |
| 3 | Materialgrunddaten eingeben | Nehmen Sie auf Material anlegen (Einstieg), die folgenden Einträge vor:Material: MaterialnummerBranche: MHinweis Ist das Eingabefeld Branche ausgeblendet, ist keine Eingabe erforderlich. Wird die Branche nicht zur Eingabe angeboten, wird nicht bekannt im Feld eingetragen.Materialart: NLAG NichtlagermaterialWählen Sie Sichtenauswahl. | Nachdem Sie die Einträge vorgenommen haben, wird ein neues Fenster Sichtenauswahl geöffnet. |  |
| 4 | Sichten wählen | Wählen Sie im Fenster Sichtenauswahl die Sichten Vertrieb: VerkaufsorgDaten 1, Vertrieb: VerkaufsorgDaten 2 und Vertrieb: Allg./Werksdaten aus, und wählen Sie dann Weiter.Hinweis Nur für Polen: Wählen Sie außerdem Außenhandel - Exportdaten, um die PKWiU-Klassifikationsnummer einzugeben. | Ein Fenster mit Organisationsebenen wird angezeigt. |  |
| 5 | Organisationsebenendaten eingeben | Geben Sie im Bild Organisationsebenen im Abschnitt Organisationsebene Beschreibungen für folgende Einträge ein:WerkVerkaufsorg.Vertriebs- KanalWählen Sie Weiter.Hinweis Im unteren Bildbereich wird folgende Information angezeigt: Das Material existiert bereits und wird erweitert. | Die Sicht Material ... anlegen (Nichtlagermaterial) wird angezeigt. |  |
| 6 | Verkaufsdaten eingeben | Nehmen Sie auf dem Bild Material ... (Nichtlagermaterial) auf der Registerkarte Vertrieb: Verkaufsorganisation 1 im Bereich Allgemeine Daten folgenden Eintrag vor:BasismengeneinheitAuslieferungswerk |  |  |
| 7 | Verkaufsdaten eingeben | Nehmen Sie auf dem Bild Material ... (Nichtlagermaterial) auf der Registerkarte Vertrieb: Verkaufsorganisation 1 im Bereich Steuerdaten folgende Einträge vor:Steuerklassifikation: 1Hinweis Der eingegebene Wert zeigt an, dass das Material (für gewöhnlich) voll steuerpflichtig ist.Nur für Brasilien: Geben Sie unter Steuerdaten folgende Daten ein:Land: BRSteuerkategorie: IBRXSteuerklassifizierung: Entweder 1 für Material oder 2 für Dienstleistungen | Verkauf: Verkaufsorganisation 2 wird angezeigt. |  |
| 8 | Verkaufsdaten eingeben | Nehmen Sie auf der Registerkarte Vertrieb: Verkaufsorganisation 2 im Abschnitt Gruppierungsbegriffe den folgenden Eintrag vor:allg.Pos.typenGruppePositionstypengruppeKontierungsgr. Mat. | Die nächste Registerkarte Vertrieb: Allg./Werk wird angezeigt. |  |
| 9 | Verkaufsdaten eingeben | Nehmen Sie auf der Registerkarte Vertrieb: Allg./Werk im Abschnitt Versanddaten folgende Einträge vor:Ladegruppe |  |  |
| 10 | Verkaufsdaten eingeben | Nehmen Sie auf der Registerkarte Vertrieb: Allg./Werk im Abschnitt Allgemeine Werksparameter folgende Einträge vor:Profitcenter |  |  |
| Nur für Polen: | Verkaufsdaten eingeben | Geben Sie im Abschnitt International Trade: Export die folgenden Daten ein:Steuerungscode: z.B. 26.70.13.0 | Der PKWiU-Code für Polen ist gepflegt. |  |
| 11 | Daten sichern | Wählen Sie im unteren Bildbereich Sichern. | Ihre Daten werden gesichert. |  |

Vorgehensweise: Option 2 – Produktstammdaten verwalten

Gehen Sie folgendermaßen vor, wenn Sie aufgrund Ihrer Benutzerrolle auf die App Produktstammdaten verwalten(F1602) zugreifen können.

| Testschrittnummer | Bezeichnung des Testschritts | Anweisung | Erwartetes Ergebnis | Kommentare |
| --- | --- | --- | --- | --- |
| 1 | Anmelden | Melden Sie sich am SAP Fiori Launchpad als Stammdatenexperte – Produktdaten an. | Das SAP Fiori Launchpad wird angezeigt. |  |
| 2 | SAP-Fiori-App aufrufen | Öffnen Sie Produktstammdaten verwalten(F1602). | Das Bild Produktstammdaten verwalten(F1602) wird angezeigt. |  |
| 3 | Produkt suchen und zur Bearbeitung öffnen | Suchen Sie nach dem zuvor angelegten Produkt, indem Sie Produktnummer im Suchfeld Produkt eingeben.Wählen Sie das Produkt aus der Liste aus. Sie gelangen daraufhin zur Sicht Produkt.Wählen Sie Bearbeiten. | Das Produkt wird im Bearbeitungsmodus angezeigt (die Felder sind eingabebereit). |  |
| 4 | Vertriebslinien auswählen | Wählen Sie in der Sicht Produkt die Registerkarte Vertriebslinien. | Die Registerkarte Vertriebslinien wird angezeigt. |  |
| 5 | Hinzufügen (+) wählen | Wählen Sie auf der Registerkarte Vertriebslinien die Option + (Hinzufügen). | Das Bild Vertriebslinien wird im Änderungsmodus geöffnet. |  |
| Nicht relevant für Brasilien | Vertriebsliniendaten eingeben | Geben Sie in Vertriebslinien folgende Daten ein:Im Abschnitt ALLGEMEINE DATEN - Allgemeine Informationen:Verkaufsorganisation: VerkaufsorganisationsnummerHinweis Der Organisationseinheitswert richtet sich nach den Optionen in der Wertehilfe.Vertriebsweg: z.B. 10Lieferwerk: WerksnummerIm Abschnitt GRUPPIERUNGSBEGRIFFE:Positionstypengruppe: z.B. NLAGIm Bildbereich UMSATZSTEUER:Land: LändercodeSteuerkategorie: z.B. TTX1Steuerklassifikation: z.B. entweder 1 für Material oder 2 für Dienstleistungen. Beispiel Steuerklassifikation: 1 volle Steuer, wenn Sie die Steuerkondition UTXJ für die USA verwenden.Hinweis Die Steuerklassifikation hängt von den spezifischen Anforderungen des jeweiligen Landes bzw. der Region ab. Die Steuerklassifizierung in den Materialstamm- und Kundenstammtabellen bestimmt die Eingaben der Prozenteingaben. |  |  |
| 6 | Zur Hauptsicht zurückkehren | Wählen Sie Übernehmen, um zur Sicht Produkt zurückzukehren. | Die Sicht Produkt wird angezeigt. |  |
| 7 | Daten sichern | Wählen Sie Sichern. | Eine Systemmeldung bestätigt, dass das Objekt gesichert wurde. |  |

### Materialstammdaten (Nichtlagermaterial) anlegen – Einkaufsdaten

Testverwaltung

Kundenprojekt: Füllen Sie die projektbezogenen Teile aus.

|  |  |  |  |
| --- | --- | --- | --- |
| Testfall-ID | <X.XX> | Testdatum: |  |
| Testername: |  | Dauer: |  |
| Benutzerrolle(n): |  | Zuständigkeit: | <Geben Sie den Serviceanbieter, einen Kunden oder einen Serviceanbieter zusammen mit einem Kunden an.> |

Zweck

Das Verfahren in diesem Abschnitt enthält eine Anleitung zum Anlegen von Materialstammdaten (Nichtlagermaterial). Die zur Verfügung stehenden Apps hängen von der Ihnen zugeordneten Rolle ab. Aus diesem Grund sind zwei Optionen verfügbar.

Voraussetzung

Sie müssen die vorherige Vorgehensweise Materialstammdaten (Nichtlagermaterial) anlegen – Grunddaten erst abschließen, bevor Sie mit diesem Abschnitt fortfahren können.

Beginnen Sie mit dieser Vorgehensweise, nachdem Sie die eingegebenen Grunddaten gesichert haben, wie bei der vorherigen Vorgehensweise erläutert.

Vorgehensweise: Option 1 – Material anlegen

Gehen Sie folgendermaßen vor, wenn Sie aufgrund Ihrer Benutzerrolle auf die App Material anlegen(MM01) zugreifen können.

| Testschrittnummer | Bezeichnung des Testschritts | Anweisung | Erwartetes Ergebnis | Kommentare |
| --- | --- | --- | --- | --- |
| 1 | Anmelden | Melden Sie sich am SAP Fiori Launchpad als Stammdatenexperte – Produktdaten an. | Das SAP Fiori Launchpad wird angezeigt. |  |
| 2 | SAP-Fiori-App aufrufen | Öffnen Sie Material anlegen(MM01). | Die App wird geöffnet. |  |
| 3 | Materialgrunddaten eingeben | Nehmen Sie auf dem Bild Material anlegen (Einstieg), die folgenden Einträge vor:Material: MaterialnummerBranche: MHinweis Ist das Eingabefeld Branche ausgeblendet, ist keine Eingabe erforderlich. Wird die Branche nicht zur Eingabe angeboten, wird nicht bekannt im Feld eingetragen.Materialart: NLAG NichtlagermaterialWählen Sie Sichtenauswahl. | Das Bild Sichtenauswahl wird angezeigt. |  |
| 4 | Sichten wählen | Wählen Sie auf dem Bild Sichtenauswahl die Sicht Einkauf aus, und wählen Sie Weiter. | Das Bild Organisationsebenen wird angezeigt. |  |
| 5 | Organisationsebenendaten eingeben | Nehmen Sie auf dem Bild Organisationsebenen im Bereich Organisationsebene den folgenden Eintrag vor:Werk: WerksnummerWählen Sie Weiter.Hinweis Im unteren Bildbereich wird folgende Meldung angezeigt: Das Material existiert bereits und wird erweitert. | Das Bild Material ... anlegen (Nichtlagermaterial) wird angezeigt. |  |
| 6 | Einkaufsdaten eingeben | Nehmen Sie auf dem Bild Material ... (Nichtlagermaterial) auf der Registerkarte Einkauf im Abschnitt Allgemeine Daten folgende Einträge vor:Basismengeneinheit: z.B. HMaterialgruppe: z.B. YBPM02Einkäufergruppe: z.B. 001Steuerind. Material: z.B. 1 |  |  |
| Nicht relevant für Brasilien | Einkaufsdaten eingeben | Nehmen Sie auf dem Bild Material ... (Nichtlagermaterial) auf der Registerkarte Einkauf im Abschnitt Sonstige Daten / Herstellerdaten den folgenden Eintrag vor:WE-Bearbeitungszeit: z.B. 1 |  |  |
| 7 | Daten sichern | Wählen Sie im unteren Bildbereich Sichern. | Ihre Daten werden gesichert. |  |

Vorgehensweise: Option 2 – Produktstammdaten verwalten

Gehen Sie folgendermaßen vor, wenn Sie aufgrund Ihrer Benutzerrolle auf die App Produktstammdaten verwalten(F1602) zugreifen können.

| Testschrittnummer | Bezeichnung des Testschritts | Anweisung | Erwartetes Ergebnis | Kommentare |
| --- | --- | --- | --- | --- |
| 1 | Anmelden | Melden Sie sich am SAP Fiori Launchpad als Stammdatenexperte – Produktdaten an. | Das SAP Fiori Launchpad wird angezeigt. |  |
| 2 | SAP-Fiori-App aufrufen | Öffnen Sie Produktstammdaten verwalten(F1602). | Die App wird geöffnet. |  |
| 3 | Produkt suchen und zur Bearbeitung öffnen | Suchen Sie nach dem zuvor angelegten Produkt, indem Sie die Produktnummer in das Suchfeld Produkt eingeben.Wählen Sie das Produkt aus der Liste aus. Sie gelangen daraufhin zur Sicht Produkt.Wählen Sie Bearbeiten. | Das Produkt wird im Bearbeitungsmodus angezeigt (die Felder sind eingabebereit). |  |
| 4 | "Kopf bearbeiten" wählen | Wählen Sie in der Sicht Kopf bearbeiten die Option Produktgruppe pflegen.Wählen Sie OK. |  |  |
| 5 | Einkaufsdaten eingeben | Nehmen Sie in der Sicht Einkauf folgenden Eintrag vor:Einkaufswerteschlüssel: z.B. 1 |  |  |
| 6 | Daten sichern | Wählen Sie Sichern. | Eine Systemmeldung bestätigt, dass das Objekt gesichert wurde. |  |

### Materialstammdaten (Nichtlagermaterial) anlegen – Buchhaltungsdaten (Bewertungsbereichsdaten)

Testverwaltung

Kundenprojekt: Füllen Sie die projektbezogenen Teile aus.

|  |  |  |  |
| --- | --- | --- | --- |
| Testfall-ID | <X.XX> | Testdatum: |  |
| Testername: |  | Dauer: |  |
| Benutzerrolle(n): |  | Zuständigkeit: | <Geben Sie den Serviceanbieter, einen Kunden oder einen Serviceanbieter zusammen mit einem Kunden an.> |

Verwendungszweck

Das Verfahren in diesem Abschnitt enthält eine Anleitung zum Anlegen von Materialstammdaten (Nichtlagermaterial). Die zur Verfügung stehenden Apps hängen von der Ihnen zugeordneten Rolle ab. Aus diesem Grund sind zwei Optionen verfügbar.

Voraussetzung

Sie müssen die vorherige Vorgehensweise Materialstammdaten (Nichtlagermaterial) anlegen – Grunddaten erst abschließen, bevor Sie mit diesem Abschnitt fortfahren können.

Beginnen Sie mit dieser Vorgehensweise, nachdem Sie die eingegebenen Grunddaten gesichert haben, wie bei der vorherigen Vorgehensweise erläutert.

Vorgehensweise: Option 1 – Material anlegen

Gehen Sie folgendermaßen vor, wenn Sie aufgrund Ihrer Benutzerrolle auf die App Material anlegen(MM01) zugreifen können.

| Testschrittnummer | Bezeichnung des Testschritts | Anweisung | Erwartetes Ergebnis | Kommentare |
| --- | --- | --- | --- | --- |
| 1 | Anmelden | Melden Sie sich am SAP Fiori Launchpad als Stammdatenexperte – Produktdaten an. | Das SAP Fiori Launchpad wird angezeigt. |  |
| 2 | SAP-Fiori-App aufrufen | Öffnen Sie Material anlegen(MM01). | Die Sicht Material anlegen(MM01) wird angezeigt. |  |
| 3 | Materialgrunddaten eingeben | Nehmen Sie auf dem Bild Material anlegen (Einstieg), die folgenden Einträge vor:Material: MaterialnummerBranche: MHinweis Ist das Eingabefeld Branche ausgeblendet, ist keine Eingabe erforderlich. Wird die Branche nicht zur Eingabe angeboten, wird nicht bekannt im Feld eingetragen.Materialart: NLAG NichtlagermaterialWählen Sie Sichtenauswahl. | Die Sichtenauswahl wird geöffnet. |  |
| 4 | Sichten wählen | Wählen Sie im Fenster Sichtenauswahl die folgenden Sichten aus:Buchhaltung 1Buchhaltung 2Wählen Sie Weiter. | Das Bild Organisationsebenen wird angezeigt. |  |
| 5 | Organisationsebenendaten eingeben | Nehmen Sie auf dem Bild Organisationsebenen im Abschnitt Organisationsebene die folgenden Einträge vor:WerkHinweis Im unteren Teil des Bildes wird folgende Information angezeigt: Das Material existiert bereits und wird erweitert. | Das Bild Material ... anlegen (Nichtlagermaterial) wird geöffnet. |  |
| 6 | Buchhaltungsdaten eingeben | Nehmen Sie auf dem Bild Material ... anlegen (Nichtlagermaterial) auf der Registerkarte Buchhaltung 1 im Abschnitt Aktuelle Bewertungsdaten den folgenden Eintrag vor:Bewertungsklasse: z.B. YB01Preissteuerung: z.B. SGleitender Preis: z.B. 1Preiseinheit: z.B. 1 |  |  |
| Nicht relevant für Brasilien | Eingaben bestätigen | Auf der Registerkarte Buchhaltung 2 sind keine Eingaben erforderlich. |  |  |
| 7 | Daten sichern | Wählen Sie im unteren Bildbereich Sichern. | Das Fenster Stammdaten - Produkt wird angezeigt.Ihre Daten werden gesichert. |  |

Vorgehensweise: Option 2 – Produktstammdaten verwalten

Gehen Sie folgendermaßen vor, wenn Sie aufgrund Ihrer Benutzerrolle auf die App Produktstammdaten verwalten(F1602) zugreifen können.

| Testschrittnummer | Bezeichnung des Testschritts | Anweisung | Erwartetes Ergebnis | Kommentare |
| --- | --- | --- | --- | --- |
| 1 | Anmelden | Melden Sie sich am SAP Fiori Launchpad als Stammdatenexperte – Produktdaten an. | Das SAP Fiori Launchpad wird angezeigt. |  |
| 2 | SAP-Fiori-App aufrufen | Öffnen Sie Produktstammdaten verwalten(F1602). | Das Bild Produktstammdaten verwalten(F1602) wird angezeigt. |  |
| 3 | Produkt suchen und zur Bearbeitung öffnen | Suchen Sie nach dem zuvor angelegten Produkt, indem Sie Produktnummer im Suchfeld Produkt eingeben.Wählen Sie das Produkt aus der Liste aus. Sie gelangen daraufhin zur Sicht Produkt.Wählen Sie Bearbeiten. | Das Produkt wird im Bearbeitungsmodus angezeigt (die Felder sind eingabebereit). |  |
| 4 | Bewertungskreisdaten auswählen | Wählen Sie in der Sicht Produkt die Registerkarte Bewertungskreise. | Die Registerkarte Bewertungskreise wird angezeigt. |  |
| 5 | Hinzufügen (+) wählen | Wählen Sie im Abschnitt Bewertungskreise die Option + (Hinzufügen). | Bewertung wird im Bearbeitungsmodus geöffnet. |  |
| 6 | Bewertungskreisdaten eingeben | Geben Sie in der Sicht Bewertung folgende Daten ein:Bewertungskreis: BewertungskreisnummerBewertungsklasse: z.B. YB01 |  |  |
| Nicht relevant für Brasilien | Aktuelle Bewertungskreisdaten eingeben | Geben Sie unter BEWERTUNGSKREISEBewertung > Laufende Periode die folgenden Daten ein:BestandspreisPreissteuerung: z.B. S |  |  |
| 7 | Zum Hauptbild zurückkehren | Wählen Sie Übernehmen, um zur Sicht Produkt zurückzukehren. | Die Sicht Produktstamm verwalten wird angezeigt. |  |
| 8 | Daten sichern | Wählen Sie Sichern. | Eine Systemmeldung bestätigt, dass das Objekt gesichert wurde. |  |

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
- related-to :: [[02-business-partner-and-product-master-data/master-data-script-create-product-master-of-type-non-stock-material-md]]
- related-to :: [[02-business-partner-and-product-master-data/master-data-script-creating-non-stock-material-product-master-data-31y]]
- related-to :: [[02-business-partner-and-product-master-data/mds-31y-313]]
- related-to :: [[02-business-partner-and-product-master-data/script-de-dados-mestre-criar-mestre-de-produtos-do-tipo-material-nao-e]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/31Y_S4CLD2608_Master_Data_DE_XX.docx` — full document · extracted with `mammoth` · 33,103 chars in the whole document
