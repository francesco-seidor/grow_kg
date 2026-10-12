---
id: 02-business-partner-and-product-master-data/stammdatenskript-produktstamm-vom-typ-leihgut-anlegen-sds-65b-496
title: "Stammdatenskript: Produktstamm vom Typ \"Leihgut\" anlegen – SDS (65B) (65B_S4CLD2608_Master_Data_DE_XX)"
description: "German master data script (SAP S/4HANA Cloud Public Edition 2608) for creating a product master of type Leihgut (loaned item, LEIH) via MM01 or F1602, across five data segments."
cluster: 02-business-partner-and-product-master-data
tags: [kb/business-partner-and-product-master-data, topic/product-master-packaging]
aliases: [65B_S4CLD2608_Master_Data_DE_XX]
keywords: ["Product Master: Packaging and Returnable Packaging", product master, loaned item material type, basic data, sales data, mrp planning data, storage location data, accounting data, material number ranges, organizational units]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/65B_S4CLD2608_Master_Data_DE_XX.docx]
confidence: high
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-496
topic: 02-business-partner-and-product-master-data/product-master-packaging
language: DE
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Stammdatenskript: Produktstamm vom Typ "Leihgut" anlegen – SDS (65B) (65B_S4CLD2608_Master_Data_DE_XX)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/65B_S4CLD2608_Master_Data_DE_XX.docx`, extracted with `mammoth`. Grouped under **Product Master: Packaging and Returnable Packaging** in Business Partner and Product Master Data. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

| <!-- image omitted: unnamed --> | StammdatenskriptSAP S/4HANA Cloud Public Edition - 02-07-26 |
| --- | --- |
|  | Produktstamm vom Typ "Leihgut" anlegen – SDS (65B) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Inhaltsverzeichnis

[1 Einsatzmöglichkeiten 2](#_Toc233889837)

[2 Voraussetzungen 3](#_Toc233889838)

[2.1 Systemzugriff 3](#_Toc233889839)

[2.2 Rollen 3](#_Toc233889840)

[2.3 Erforderliche Organisationseinheiten 3](#_Toc233889841)

[2.4 Obligatorische und optionale Stammdaten 4](#_Toc233889842)

[2.5 Wesentliche Parameter für die Datenerstellung 5](#_Toc233889843)

[2.5.1 Materialart und Nummernkreise 5](#_Toc233889844)

[2.5.2 Branche 5](#_Toc233889845)

[3 Übersichtstabelle 6](#_Toc233889846)

[4 Testverfahren 7](#_Toc233889847)

[4.1 Materialstammdaten (Produktstammdaten) anlegen - Grunddaten 7](#_Toc233889848)

[4.2 Materialstammdaten (Produktstammdaten) anlegen – Verkaufsdaten (Umsatzsteuerdaten) 10](#_Toc233889849)

[4.3 Materialstammdaten (Produktstammdaten) anlegen – Dispositions-/Planungsdaten (Werksdaten) 14](#_Toc233889850)

[4.4 Materialstammdaten (Produktstammdaten) anlegen – Lagerortdaten 17](#_Toc233889851)

[4.5 Materialstammdaten (Produktstammdaten) anlegen – Buchhaltungsdaten 19](#_Toc233889852)

## Einsatzmöglichkeiten

Der Material- oder Produktstamm enthält Informationen über alle physischen Materialien, die gelagert und verkauft werden.

Der Materialstamm enthält Informationen wie die eindeutige Materialnummer, Name, Materialart, Mengeneinheit, Beschreibungen, Gewicht und Abmessungen. Diese Materialinformationen werden in Transaktionen wie Kundenaufträgen, Lieferungen und Warenbewegungen verwendet und gespeichert.

Da alle Informationen für ein Material zentral gespeichert werden, sind die Materialstamminformationen in verschiedenen Ansichten organisiert. Hierzu zählen beispielsweise Beispiel Verkauf, Lagerung und Abrechnung.

Einige Informationen zu den einzelnen Materialien sind spezifisch für bestimmte Organisationseinheiten. Eine Verkaufsbeschreibung ist zum Beispiel spezifisch für eine Verkaufseinheit (Verkaufsbereich), ein Disponent ist spezifisch für einen bestimmten Standort (Werk), und einige Informationen können spezifisch für einen Lagerort sein.

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

| Datensegment | Hängt ab von | Feldbeispiele | Kommentare | Zu verwendende Organisationseinheit |
| --- | --- | --- | --- | --- |
| Grunddaten | Unabhängig von Organisationeinheiten | Materialbeschreibung (Kurztext), Materialnummer, Materialgruppe, Basismengeneinheit usw. | Grunddaten sind für einen Materialstammsatz nur einmal vorhanden. | Keine |
| Verkaufsdaten | Werk, Verkaufsorg., Vertriebsweg | Steuerdaten, Positionstypengruppe, TranspGruppe, Ladegruppe usw. | Verkaufsdaten können für jede Verkaufsorganisation Ihrer Unternehmensstruktur vorhanden sein, für die der Materialstammsatz verwendet wird. | Werk:____________Verkaufsorganisation:__________Vertriebsweg:__________ |
| Dispositions-/Planungsdaten | Werk, Lagerort | Dispositionsmerkmal, Disponent, Planlieferzeit usw. | Werksdaten können für jede Werks-ID Ihrer Unternehmensstruktur existieren, für die der Materialstammsatz verwendet wird.Lagerortdaten (Planungskontext) sind optional, abhängig von der Notwendigkeit, eine lagerortspezifische Planung durchzuführen. | Werk:____________Lagerort:__________ |
| Lagerortdaten | Werk, Lagerort | Profitcenter usw. | Werksdaten können für jede Werks-ID Ihrer Unternehmensstruktur existieren, für die der Materialstammsatz verwendet wird.Lagerortdaten (Planungskontext) sind optional, abhängig von der Notwendigkeit, eine lagerortspezifische Planung durchzuführen. | Werk:____________Lagerort:__________ |
| Buchhaltungsdaten | Bewertungsbereich(= Werk) | Per. VPreis, Preissteuerung usw. | Daten zum Bewertungsbereich können für jede Werks-ID Ihrer Unternehmensstruktur existieren, für die der Materialstammsatz verwendet wird. Jedes Werk stellt einen Bewertungsbereich dar (z.B. unterschiedliche Bewertungspreise eines Materials in verschiedenen Werken). | Werk:____________Bewertungsart:__________ |

### Obligatorische und optionale Stammdaten

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
| Intern numerisch | 1–99999999 | Dieser Bereich wird verwendet, wenn das System einem Material automatisch eine numerische Nummer zuordnen soll. |

#### Branche

Der Standard-Content stellt nur die Branche M bereit. Diese ist zurzeit nur in der SAP GUI sichtbar.

## Übersichtstabelle

Dieser Umfangsbestandteil umfasst die verschiedenen Prozessschritte in der folgenden Tabelle:

Wenn Ihr Systemadministrator Bereiche und Seiten auf dem SAP Fiori Launchpad aktiviert hat, enthält die Startseite nur die wesentlichen Apps, mit denen die typischen Aufgaben einer Benutzerrolle ausgeführt werden können.

Alle anderen Apps, die nicht auf der Startseite enthalten sind, finden Sie über die Suchleiste.

Wenn Sie die Startseite personalisieren und versteckte Apps hinzufügen möchten, wechseln Sie in Ihr Benutzerprofil und wählen Sie App Finder.

| Prozessschritt | Benutzerrolle | Transaktion/App | Erwartete Ergebnisse |
| --- | --- | --- | --- |
| [Materialstammdaten (Produktstammdaten) anlegen - Grunddaten](#unique_11) [Seite ] 7 | Stammdatenexperte – Produktdaten | Material anlegen(MM01) / Produktstammdaten verwalten(F1602) | Materialstammdaten - Grunddaten werden angelegt. |
| [Materialstammdaten (Produktstammdaten) anlegen – Verkaufsdaten (Umsatzsteuerdaten)](#unique_12) [Seite ] 10 | Stammdatenexperte – Produktdaten | Material anlegen(MM01) / Produktstammdaten verwalten(F1602) | Materialstammdaten – Verkaufsdaten werden angelegt.. |
| [Materialstammdaten (Produktstammdaten) anlegen – Dispositions-/Planungsdaten (Werksdaten)](#unique_13) [Seite ] 14 | Stammdatenexperte – Produktdaten | Material anlegen(MM01) / Produktstammdaten verwalten(F1602) | Materialstammdaten – Dispositions-/Planungsdaten werden angelegt. |
| [Materialstammdaten (Produktstammdaten) anlegen – Lagerortdaten](#unique_14) [Seite ] 17 | Stammdatenexperte – Produktdaten | Material anlegen(MM01) / Produktstammdaten verwalten(F1602) | Materialstammdaten – Lagerortdaten werden angelegt. |
| [Materialstammdaten (Produktstammdaten) anlegen – Buchhaltungsdaten](#unique_15) [Seite ] 19 | Stammdatenexperte – Produktdaten | Material anlegen(MM01) / Produktstammdaten verwalten(F1602) | Materialstammdaten – Buchhaltungsdaten (Bewertungsbereichsdaten) werden angelegt. |

## Testverfahren

Dieser Abschnitt beschreibt die Vorgehensweisen für die einzelnen Segmente oder Prozessschritte, die Teil dieses Stammsatzes ist.

### Materialstammdaten (Produktstammdaten) anlegen - Grunddaten

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
| 2 | SAP-Fiori-App aufrufen | Öffnen Sie Material anlegen(MM01). | Das Bild Material anlegen (Einstieg) wird angezeigt. |  |
| 3 | Materialgrunddaten eingeben | Geben Sie auf dem Bild Material anlegen (Einstieg) folgende Daten ein:Material: <Materialnummer>Branche: MaschinenbauHinweis Ist das Eingabefeld Branche ausgeblendet, ist keine Eingabe erforderlich. Wird die Branche nicht zur Eingabe angeboten, wird das Feld ausgegraut.Materialart: LeihgutWählen Sie Sichtenauswahl. | Das Bild Sichtenauswahl wird angezeigt. |  |
| 4 | Sichten wählen | Wählen Sie auf dem Bild Sichtenauswahl die folgenden Einträge aus, und wählen Sie Weiter:Grunddaten 1Grunddaten 2 | Das Bild Material anlegen … (Leihgut) wird angezeigt. |  |
| 5 | Grunddaten eingeben | Geben Sie auf der Registerkarte Grunddaten 1 eine Materialbeschreibung (Kurztext) ein. |  |  |
| 6 | Grunddaten eingeben | Geben Sie auf der Registerkarte Grunddaten 1 im Abschnitt Allgemeine Daten Beschreibungen für die folgenden Einträge ein:BasismengeneinheitWarengruppeAllg. PosTypGrp: LEIH |  |  |
| 7 | Grunddaten eingeben | Geben Sie im Abschnitt Dimensionen/EANs Folgendes ein:BruttogewichtGewichtseinheitNettogewichtDrücken Sie Enter. | Die Registerkarte Grunddaten 2 wird angezeigt. |  |
| 8 | Grunddaten vervollständigen | Für die Sicht Grunddaten 2 sind keine Einträge erforderlich. |  |  |
| 9 | Daten sichern | Wählen Sie unten rechts im Bild Sichern, um Ihre Daten zu sichern. | Das Bild Material anlegen (Einstieg) wird geöffnet.Die Grunddaten werden angelegt und gesichert. |  |

Vorgehensweise: Option 2 – Produktstammdaten verwalten

Gehen Sie folgendermaßen vor, wenn Sie aufgrund Ihrer Benutzerrolle auf die App Produktstammdaten verwalten(F1602) zugreifen können.

| Testschrittnummer | Bezeichnung des Testschritts | Anweisung | Erwartetes Ergebnis | Kommentare |
| --- | --- | --- | --- | --- |
| 1 | Anmelden | Melden Sie sich am SAP Fiori Launchpad als Stammdatenexperte – Produktdaten an. | Das SAP Fiori Launchpad wird angezeigt. |  |
| 2 | SAP-Fiori-App aufrufen | Öffnen Sie Produktstammdaten verwalten(F1602). | Das Bild Produktstammdaten verwalten wird angezeigt. |  |
| 3 | "Neuen Produktstamm anlegen" auswählen | Wählen Sie auf dem Bild Produktstammdaten verwalten im Abschnitt Produkte die Option Anlegen. | Das Bild Stammdatensatz anlegen wird angezeigt. |  |
| 4 | Daten in Pflichtfelder eingeben | Nehmen Sie auf dem Bild Stammdatensatz anlegen die folgenden Einträge vor:Produktnummer: z.B. Z …Hinweis Geben Sie entweder eine externe alphanumerische ID ein, die mit einem alphanumerischen Zeichen beginnen muss, oder lassen Sie das Feld frei; in diesem Fall weist das System automatisch eine numerische ID zu.Weitere Informationen zur Produktnummer finden Sie im vorangehenden Abschnitt Materialart und Nummernkreise.Produktart: LEIHProduktgruppe: z.B. L006Basis-ME: z.B. STBeschreibung: <beliebige Beschreibung> |  |  |
| 5 | Wählen Sie OK. | Wählen Sie OK. |  |  |
| 6 | Grunddaten eingeben | Navigieren Sie zu Produktstamm verwalten > Allgemeine Informationen > Grunddaten, und geben Sie folgende Daten ein:Sparte: z.B. 00 |  |  |
| 7 | Hinzufügen (+) wählen | Navigieren Sie zu Produktstamm verwalten > Allgemeine Informationen > Beschreibungen, und wählen Sie Anlegen. | Die Beschreibung in der Standardsprache (z.B. Deutsch) ist bereits eingegeben. |  |
| 8 | Beschreibungsdaten eingeben | Geben Sie in der Sicht Beschreibungen folgende Daten ein:Sprache: z.B. Deutsch.Produktbeschreibung: <Ihre Beschreibung> |  |  |
| 9 | Gewichtsdaten eingeben | Geben Sie im Abschnitt Gewicht (wenn diese Option nicht angezeigt wird, wählen Sie Mehr anzeigen) Folgendes ein:Bruttogewicht: z.B. 2Gewichtseinheit: z.B. KGNettogewicht: z.B. 1Hinweis Wenn der Abschnitt Gewicht nicht angezeigt wird, wählen Sie Mehr anzeigen. Wenn in den Feldern Bruttogewicht, Gewichtseinheit oder Nettogewicht keine Eingaben möglich sind, müssen Sie die Webseite aktualisieren oder neu laden. Nach dem Aktualisieren oder Neuladen können Sie Werte in die Felder eingeben. |  |  |
| 10 | Daten sichern | Wählen Sie Sichern. | Das Objekt wird gesichert. |  |

### Materialstammdaten (Produktstammdaten) anlegen – Verkaufsdaten (Umsatzsteuerdaten)

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

Sie müssen erst den vorherigen Abschnitt, [Materialstammdaten (Produktstammdaten) anlegen - Grunddaten](#unique_11) [Seite ] 7, abschließen, bevor Sie mit diesem Abschnitt fortfahren können.

Beginnen Sie mit dieser Vorgehensweise, nachdem Sie die eingegebenen Grunddaten gesichert haben, wie bei der vorherigen Vorgehensweise erläutert.

Vorgehensweise: Option 1 – Material anlegen

Gehen Sie folgendermaßen vor, wenn Sie aufgrund Ihrer Benutzerrolle auf die App Material anlegen(MM01) zugreifen können.

| Testschrittnummer | Bezeichnung des Testschritts | Anweisung | Erwartetes Ergebnis | Kommentare |
| --- | --- | --- | --- | --- |
| 1 | SAP-Fiori-App aufrufen | Wählen Sie Material anlegen(MM01). | Das Bild Material anlegen (Einstieg) wird angezeigt. |  |
| 2 | Materialgrunddaten eingeben | Nehmen Sie auf dem Bild Material anlegen (Einstieg) die folgenden Einträge vor:Material: <Materialnummer>Branche: MaschinenbauHinweis Ist das Eingabefeld Branche ausgeblendet, ist keine Eingabe erforderlich. Wird die Branche nicht zur Eingabe angeboten, wird das Feld ausgegraut.Materialart: LEIH LeihgutWählen Sie Sichtenauswahl. | Das Bild Sichtenauswahl wird angezeigt. |  |
| 3 | Sichten wählen | Wählen Sie im Bild Sichtenauswahl die Option Vertrieb: VerkaufsorgDaten 1, Vertrieb: VerkaufsorgDaten 2 und Vertrieb: Allg./Werksdaten aus, und wählen Sie dann Weiter. | Das Bild Organisationsebenen wird angezeigt. |  |
| 4 | Organisationsebenendaten eingeben | Geben Sie im Bild Organisationsebenen im Abschnitt Organisationsebenen Beschreibungen für folgende Einträge ein:WerkVerkaufsorg.Vertriebsweg KanalWählen Sie Weiter.Hinweis Im unteren Teil des Bildes wird folgende Information angezeigt: Das Material existiert bereits und wird erweitert. | Das Bild Material anlegen … (Leihgut) wird angezeigt. |  |
| 5 | Verkaufsdaten eingeben | Nehmen Sie im Bild Material anlegen … (Leihgut) auf der Registerkarte Vertrieb: VerkOrg 1 im Bereich Allgemeine Daten folgende Einträge vor:BasismengeneinheitAuslieferungswerk |  |  |
| 6 | Verkaufsdaten eingeben | Nehmen Sie im Bild Material anlegen … (Leihgut) auf der Registerkarte Vertrieb: VerkOrg 1 im Bereich Steuerdaten folgende Einträge vor:Steuerklassifikation: 1Hinweis Der eingegebene Wert zeigt an, dass das Material (für gewöhnlich) voll steuerpflichtig ist.Nur für Brasilien: Geben Sie unter Steuerdaten folgende Daten ein:Land: BRSteuerkategorie: IBRXSteuerklassifikation: 1Drücken Sie Enter. | Die nächste Registerkarte Vertrieb: VerkOrg 2 wird angezeigt. |  |
| 7 | Verkaufsdaten eingeben | Nehmen Sie auf der Registerkarte Vertrieb: VerkOrg 2 im Abschnitt Gruppierungsbegriffe folgende Einträge vor:StatistikGrMaterialPositionstypengruppe: CB02Allg. PosTypengruppe: LEIHKontierungsgr. Mat.: Y2Drücken Sie Enter. | Die nächste Registerkarte Vertrieb: Allg./Werk wird angezeigt. |  |
| 8 | Verkaufsdaten eingeben | Nehmen Sie auf der Registerkarte Vertrieb: Allg./Werk im Abschnitt Allgemeine Daten die folgenden Einträge vor:Verfügbarkeitsprüfung: SR |  |  |
| 9 | Verkaufsdaten eingeben | Nehmen Sie auf der Registerkarte Vertrieb: Allg./Werk im Abschnitt Versanddaten (Zeiten in Tagen) folgende Einträge vor:Trans. gruppe: <0001>Ladegruppe: <0001> |  |  |
| 10 | Verkaufsdaten eingeben | Nehmen Sie auf der Registerkarte Vertrieb: Allg./Werk im Abschnitt Allgemeine Werksparameter folgende Einträge vor:Profitcenter |  |  |
| 11 | Daten sichern | Wählen Sie im unteren Bildbereich Sichern. | Ihre Daten werden gesichert. |  |

Vorgehensweise: Option 2 – Produktstammdaten verwalten

Gehen Sie folgendermaßen vor, wenn Sie aufgrund Ihrer Benutzerrolle auf die App Produktstammdaten verwalten(F1602) zugreifen können.

| Testschrittnummer | Bezeichnung des Testschritts | Anweisung | Erwartetes Ergebnis | Kommentare |
| --- | --- | --- | --- | --- |
| 1 | SAP-Fiori-App aufrufen | Öffnen Sie Produktstammdaten verwalten(F1602). | Die App wird geöffnet, und verschiedene Suchfelder werden angezeigt. |  |
| 2 | Produkt suchen und zur Bearbeitung öffnen | Suchen Sie nach dem zuvor angelegten Produkt, indem Sie die Produktnummer im Suchfeld Produkt eingeben.Wählen Sie das Produkt aus der Liste aus. Sie gelangen daraufhin zum Bild Produkt.Wählen Sie Bearbeiten. | Das Produkt wird im Bearbeitungsmodus angezeigt (die Felder sind eingabebereit). |  |
| 3 | Vertriebslinien auswählen | Wählen Sie auf dem Bild Produkt die Registerkarte Vertriebslinien. | Die Registerkarte Vertriebslinien wird angezeigt. |  |
| 4 | Hinzufügen (+) wählen | Wählen Sie auf der Registerkarte Vertriebslinien die Option Anlegen. | Vertriebslinien wird im Bearbeitungsmodus geöffnet. |  |
| 5 | Vertriebsliniendaten eingeben | Geben Sie auf dem Bild Vertriebslinien folgende Daten ein:Navigieren Sie zu Allgemeine Informationen > Allgemeine Daten:Verkaufsorganisation: <Verkaufsorganisationsnummer>Hinweis Der Organisationseinheitswert richtet sich nach den Optionen in der Wertehilfe.Vertriebsweg: z.B. 10Lieferwerk: <Werksnummer>Im Abschnitt Gruppierungsbegriffe:Positionstypengruppe: z.B. CB02Kontierungsgruppe: z.B. Y2 LeihgutIm Bildbereich Umsatzsteuer:Land: <Ländercode>Steuerkategorie: z.B. TTX1Steuerklassifikation: z.B. entweder 1 für Material oder 2 für Dienstleistungen. Beispiel Steuerklassifikation: 1 volle Steuer, wenn Sie die Steuerkondition UTXJ für die USA verwenden.Hinweis Die Steuerklassifikation hängt von den spezifischen Anforderungen des jeweiligen Landes ab. Die Steuerklassifizierung in den Materialstamm- und Kundenstammtabellen bestimmt die Eingaben der Prozenteingaben.Nur für Brasilien: Nehmen Sie im Abschnitt Steuerklassifikation folgende Einträge vor:Land: BRSteuerkategorie: IBRXSteuerklassifikation: 1 |  |  |
| 6 | Zur Hauptsicht zurückkehren | Wählen Sie Übernehmen, um zum Bild Produkt zurückzukehren. | Das Bild Produkt wird angezeigt. |  |
| 7 | Daten sichern | Wählen Sie Sichern. | Das Objekt wird gesichert. |  |

### Materialstammdaten (Produktstammdaten) anlegen – Dispositions-/Planungsdaten (Werksdaten)

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

Sie müssen erst die vorherige Vorgehensweise, [Materialstammdaten (Produktstammdaten) anlegen - Grunddaten](#unique_11) [Seite ] 7, abschließen, bevor Sie mit diesem Abschnitt fortfahren können.

Beginnen Sie mit dieser Vorgehensweise, nachdem Sie die eingegebenen Grunddaten gesichert haben, wie bei der vorherigen Vorgehensweise erläutert.

Vorgehensweise: Option 1 – Material anlegen

Gehen Sie folgendermaßen vor, wenn Sie aufgrund Ihrer Benutzerrolle auf die App Material anlegen(MM01) zugreifen können.

| Testschrittnummer | Bezeichnung des Testschritts | Anweisung | Erwartetes Ergebnis | Kommentare |
| --- | --- | --- | --- | --- |
| 1 | SAP-Fiori-App aufrufen | Öffnen Sie Material anlegen(MM01). | Das Bild Material anlegen (Einstieg) wird angezeigt. |  |
| 2 | Materialgrunddaten eingeben | Nehmen Sie auf dem Bild Material anlegen (Einstieg) die folgenden Einträge vor:Material: <Materialnummer>Branche: MaschinenbauHinweis Ist das Eingabefeld Branche ausgeblendet, ist keine Eingabe erforderlich. Wird die Branche nicht zur Eingabe angeboten, wird das Feld ausgegraut.Materialart: LeihgutWählen Sie Sichtenauswahl. | Das Bild Sichtenauswahl wird angezeigt. |  |
| 3 | Sichten wählen | Wählen Sie im Bild Sichtenauswahl Disposition 1, Disposition 2, Disposition 3 und Disposition 4, und wählen Sie anschließend Weiter. | Das Bild Organisationsebenen wird angezeigt. |  |
| 4 | Organisationsebenendaten eingeben | Nehmen Sie auf dem Bild Organisationsebenen im Bereich Organisationsebenen die folgenden Einträgen vor:Werk: <Werksnummer>Lagerort: <Lagerortnummer>Wählen Sie Weiter.Hinweis Im unteren Teil des Bildes wird folgende Information angezeigt: Das Material existiert bereits und wird erweitert. | Das Bild Material anlegen … (Leihgut) wird angezeigt. |  |
| 5 | Dispositions-/Planungsdaten eingeben | Nehmen Sie im Bild Material anlegen … Nehmen Sie auf dem Bild (Leihgut) auf der Registerkarte Disposition 1 im Abschnitt Dispositionsverfahren die folgenden Einträge vor:Dispositionsmerkmal: NDDisponent: <001>Drücken Sie Enter. | Die nächste Registerkarte Disposition 2 wird angezeigt. |  |
| 6 | Dispositions-/Planungsdaten eingeben | Nehmen Sie im Bild Material anlegen … Nehmen Sie auf dem Bild (Leihgut) auf der Registerkarte Disposition 2 im Abschnitt Einplanung die folgenden Einträge vor:Planlieferzeit: z.B. 10Geben Sie im Bereich Beschaffung folgende Daten ein:Beschaffungsart: FDrücken Sie Enter. | Die nächste Registerkarte Disposition 3 wird angezeigt. |  |
| 7 | Dispositions-/Planungsdaten eingeben | Nehmen Sie im Bild Material anlegen … Nehmen Sie auf dem Bild (Leihgut) auf der Registerkarte Disposition 3 im Abschnitt Verfügbarkeitsprüfung die folgenden Einträge vor:Verfügbarkeitsprüfung: z.B. SRDrücken Sie Enter. | Die nächste Registerkarte Disposition 4 wird angezeigt. |  |
| 8 | Daten sichern | Wählen Sie im unteren Bildbereich Sichern. | Ihre Daten werden gesichert. |  |

Vorgehensweise: Option 2 – Produktstammdaten verwalten

Gehen Sie folgendermaßen vor, wenn Sie aufgrund Ihrer Benutzerrolle auf die App Produktstammdaten verwalten(F1602) zugreifen können.

| Testschrittnummer | Bezeichnung des Testschritts | Anweisung | Erwartetes Ergebnis | Kommentare |
| --- | --- | --- | --- | --- |
| 1 | SAP-Fiori-App aufrufen | Öffnen Sie Produktstammdaten verwalten(F1602). | Die App wird geöffnet, und verschiedene Suchfelder werden angezeigt. |  |
| 2 | Produkt suchen und zur Bearbeitung öffnen | Suchen Sie nach dem zuvor angelegten Produkt, indem Sie die Produktnummer im Suchfeld Produkt eingeben.Wählen Sie das Produkt aus der Liste aus. Sie gelangen daraufhin zum Bild Produkt.Wählen Sie Bearbeiten. | Das Produkt wird im Bearbeitungsmodus angezeigt (die Felder sind eingabebereit). |  |
| 3 | Werksdaten auswählen | Wählen Sie auf dem Bild Produkt die Registerkarte Werke aus. | Die Registerkarte Werke wird angezeigt. |  |
| 4 | Hinzufügen (+) wählen | Wählen Sie auf der Registerkarte Werke die Option Anlegen. | Das Bild Werk wird im Bearbeitungsmodus angezeigt. |  |
| 5 | "Werke – Allgemeine Daten" eingeben | Navigieren Sie zu Allgemeine Informationen > Allgemeine Daten, und geben Sie folgende Daten ein:Werk: Werksnummer, z.B. 1010Profitcenter: z.B. YB111Geben Sie im Bereich Vertrieb folgende Daten ein:Ladegruppe: z.B. 0001 |  |  |
| 6 | Werke – Dispositionsdaten eingeben | Navigieren Sie zu Dispositionsdaten > Dispositionsdaten, und nehmen Sie die folgenden Einträge vor:Verfügbarkeitsprüfung: z.B. SRDispositionsmerkmal: z.B. NDDisponent: z.B. 001 |  |  |
| 7 | "Werke – Beschaffungsdaten" eingeben | Navigieren Sie zu Dispositionsdaten > Beschaffung, und geben Sie folgende Daten ein:Planlieferzeit: z.B. 10 |  |  |
| 8 | Zur Hauptsicht zurückkehren | Wählen Sie Übernehmen, um zum Bild Produkt zurückzukehren. | Das Bild Produkt wird angezeigt. |  |
| 9 | Daten sichern | Wählen Sie Sichern. | Das Objekt wird gesichert. |  |

### Materialstammdaten (Produktstammdaten) anlegen – Lagerortdaten

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

Sie müssen erst die vorherige Vorgehensweise, [Materialstammdaten (Produktstammdaten) anlegen - Grunddaten](#unique_11) [Seite ] 7, abschließen, bevor Sie mit diesem Abschnitt fortfahren können.

Beginnen Sie mit dieser Vorgehensweise, nachdem Sie die eingegebenen Grunddaten gesichert haben, wie bei der vorherigen Vorgehensweise erläutert.

Vorgehensweise: Option 1 – Material anlegen

Gehen Sie folgendermaßen vor, wenn Sie aufgrund Ihrer Benutzerrolle auf die App Material anlegen(MM01) zugreifen können.

| Testschrittnummer | Bezeichnung des Testschritts | Anweisung | Erwartetes Ergebnis | Kommentare |
| --- | --- | --- | --- | --- |
| 1 | SAP-Fiori-App aufrufen | Öffnen Sie Material anlegen(MM01). | Das Bild Material anlegen (Einstieg) wird angezeigt. |  |
| 2 | Materialgrunddaten eingeben | Nehmen Sie auf dem Bild Material anlegen (Einstieg) die folgenden Einträge vor:Material: <Materialnummer>Branche: MaschinenbauHinweis Ist das Eingabefeld Branche ausgeblendet, ist keine Eingabe erforderlich. Wird die Branche nicht zur Eingabe angeboten, wird das Feld ausgegraut.Materialart: LeihgutWählen Sie Sichtenauswahl. | Das Bild Sichtenauswahl wird angezeigt. |  |
| 3 | Sichten wählen | Wählen Sie im Fenster Sichtenauswahl die folgenden Sichten aus:Allg. Werksdaten / Lagerung 1Allg. Werksdaten / Lagerung 2Wählen Sie Weiter. | Das Bild Organisationsebenen wird angezeigt. |  |
| 4 | Organisationsebenendaten eingeben | Nehmen Sie auf dem Bild Organisationsebenen im Bereich Organisationsebenen die folgenden Einträgen vor:Werk: z.B. <Werksnummer>Lagerort: <Lagerortnummer>Wählen Sie Weiter.Hinweis Im unteren Teil des Bildes wird folgende Information angezeigt: Das Material existiert bereits und wird erweitert. | Das Bild Material anlegen … (Leihgut) wird angezeigt. |  |
| 5 | Lagerortdaten eingeben | Auf der Registerkarte Werksdaten/Lagerung 1 müssen Sie keine Daten eingeben. |  |  |
| 6 | Eingaben bestätigen | Auf der Registerkarte Werksdaten/Lagerung 2 müssen Sie keine Daten eingeben. |  |  |
| 7 | Daten sichern | Wählen Sie im unteren Bildbereich Sichern. | Ihre Daten werden gesichert. |  |

Vorgehensweise: Option 2 – Produktstammdaten verwalten

Gehen Sie folgendermaßen vor, wenn Sie aufgrund Ihrer Benutzerrolle auf die App Produktstammdaten verwalten(F1602) zugreifen können.

| Testschrittnummer | Bezeichnung des Testschritts | Anweisung | Erwartetes Ergebnis | Kommentare |
| --- | --- | --- | --- | --- |
| 1 | SAP-Fiori-App aufrufen | Öffnen Sie Produktstammdaten verwalten(F1602). | Die App wird geöffnet, und verschiedene Suchfelder werden angezeigt. |  |
| 2 | Produkt suchen und zur Bearbeitung öffnen | Suchen Sie nach dem zuvor angelegten Produkt, indem Sie die Produktnummer im Suchfeld Produkt eingeben.Wählen Sie das Produkt aus der Liste aus. Sie gelangen daraufhin zum Bild Produkt.Wählen Sie Bearbeiten. | Das Produkt wird im Bearbeitungsmodus angezeigt (die Felder sind eingabebereit). |  |
| 3 | Werksdaten auswählen | Wählen Sie auf dem Bild Produkt die Registerkarte Werke aus.Hinweis Wenn kein Werksdatensatz vorhanden ist, führen Sie die Schritte aus dem vorherigen Abschnitt, [Materialstammdaten (Produktstammdaten) anlegen – Dispositions-/Planungsdaten (Werksdaten)](#unique_13) [Seite ] 14, aus. | Die Registerkarte Werke wird angezeigt. |  |
| 4 | Werksdaten auswählen | Wählen Sie auf der Registerkarte Werke über das Pfeilsymbol die Werksdaten aus, die Sie im vorhergehenden Schritt angelegt haben. | Das Bild Werk wird angezeigt. |  |
| 5 | Zum Werk: Lagerort | Navigieren Sie auf dem Bild Werk zu Lagerorte > Lagerorte. |  |  |
| 6 | Hinzufügen (+) wählen | Wählen Sie auf der Registerkarte Lagerorte im Abschnitt Lagerorte die Option Anlegen. | Die Sicht Werk – Lagerorte wird angezeigt. |  |
| 7 | "Werk: Lagerort" eingeben | Geben Sie in der Sicht Werk – Lagerort folgende Daten ein:Lagerort: <Lagerortnummer> |  |  |
| 8 | Zum Hauptbild zurückkehren | Wählen Sie zweimal Übernehmen, um zur Sicht Produkt zurückzukehren. | Das Bild Produkt wird angezeigt. |  |
| 9 | Daten sichern | Wählen Sie Sichern. | Das Objekt wird gesichert. |  |

### Materialstammdaten (Produktstammdaten) anlegen – Buchhaltungsdaten

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

Sie müssen erst die vorherige Vorgehensweise, [Materialstammdaten (Produktstammdaten) anlegen - Grunddaten](#unique_11) [Seite ] 7, abschließen, bevor Sie mit diesem Abschnitt fortfahren können.

Beginnen Sie mit dieser Vorgehensweise, nachdem Sie die eingegebenen Grunddaten gesichert haben, wie bei der vorherigen Vorgehensweise erläutert.

Vorgehensweise: Option 1 – Material anlegen

Gehen Sie folgendermaßen vor, wenn Sie aufgrund Ihrer Benutzerrolle auf die App Material anlegen(MM01) zugreifen können.

| Testschrittnummer | Bezeichnung des Testschritts | Anweisung | Erwartetes Ergebnis | Kommentare |
| --- | --- | --- | --- | --- |
| 1 | SAP-Fiori-App aufrufen | Öffnen Sie Material anlegen(MM01). | Das Bild Material anlegen (Einstieg) wird angezeigt. |  |
| 2 | Materialgrunddaten eingeben | Nehmen Sie auf dem Bild Material anlegen (Einstieg) die folgenden Einträge vor:Material: <Materialnummer>Branche: MaschinenbauHinweis Ist das Eingabefeld Branche ausgeblendet, ist keine Eingabe erforderlich. Wird die Branche nicht zur Eingabe angeboten, wird das Feld ausgegraut.Materialart: LeihgutWählen Sie Sichtenauswahl. | Das Bild Sichtenauswahl wird angezeigt. |  |
| 3 | Sichten wählen | Wählen Sie im Fenster Sichtenauswahl die folgenden Sichten aus:Buchhaltung 1Buchhaltung 2Wählen Sie Weiter. | Das Bild Organisationsebenen wird angezeigt. |  |
| 4 | Organisationsebenendaten eingeben | Nehmen Sie auf dem Bild Organisationsebenen im Bereich Organisationsebenen den folgenden Eintrag vor:Werk: <Werksnummer>Wählen Sie Weiter.Hinweis Im unteren Teil des Bildes wird folgende Information angezeigt: Das Material existiert bereits und wird erweitert. | Das Bild Material anlegen … (Leihgut) wird angezeigt. |  |
| 5 | Buchhaltungsdaten eingeben | Nehmen Sie im Bild Material anlegen … Nehmen Sie auf dem Bild (Leihgut) auf der Registerkarte Buchhaltung 1 im Abschnitt Aktuelle Bewertung den folgenden Eintrag vor:Bewertungsklasse: z.B. 3050Gleitender Preis: z.B. 5Preissteuerung: z.B. VDrücken Sie Enter.Hinweis Die Bewertungsklasse ist für die Produktart "LEIH" nicht obligatorisch. Sie können das entsprechende Feld über die App Material ändern(MM02) leer lassen. | Die nächste Registerkarte Buchhaltung 2 wird angezeigt. |  |
| 6 | Eingaben bestätigen | Für die Registerkarte Buchhaltung 2 sind keine Einträge erforderlich. |  |  |
| 7 | Daten sichern | Wählen Sie im unteren Bildbereich Sichern. | Ihre Daten werden gesichert. |  |

Vorgehensweise: Option 2 – Produktstammdaten verwalten

Gehen Sie folgendermaßen vor, wenn Sie aufgrund Ihrer Benutzerrolle auf die App Produktstammdaten verwalten(F1602) zugreifen können.

| Testschrittnummer | Bezeichnung des Testschritts | Anweisung | Erwartetes Ergebnis | Kommentare |
| --- | --- | --- | --- | --- |
| 1 | SAP-Fiori-App aufrufen | Öffnen Sie Produktstammdaten verwalten(F1602). | Die App wird geöffnet, und verschiedene Suchfelder werden angezeigt. |  |
| 2 | Produkt suchen und zur Bearbeitung öffnen | Suchen Sie nach dem zuvor angelegten Produkt, indem Sie die Produktnummer im Suchfeld Produkt eingeben.Wählen Sie das Produkt aus der Liste aus. Sie gelangen daraufhin zum Bild Produkt.Wählen Sie Bearbeiten. | Das Produkt wird im Bearbeitungsmodus angezeigt (die Felder sind eingabebereit). |  |
| 3 | Bewertungskreisdaten auswählen | Wählen Sie auf dem Bild Produkt die Registerkarte Bewertungskreise. | Die Registerkarte Bewertungskreise wird angezeigt. |  |
| 4 | "Anlegen" wählen | Wählen Sie auf der Registerkarte Bewertungskreise im Abschnitt Bewertungskreise die Option Anlegen. | Das Bild Bewertungskreis wird im Bearbeitungsmodus geöffnet. |  |
| 5 | Aktuelle Bewertungskreisdaten eingeben | Geben Sie auf der Registerkarte Allgemeine Informationen im Abschnitt Allgemeine Daten folgende Daten ein:Bewertungsbereich: z.B. 1010Bewertungsklasse: z.B. 3050Geben Sie im Abschnitt Laufende Periode die folgenden Daten ein:Bestandspreis: z.B. 5Preissteuerung: z.B. Gleitender Durchschnittspreis/Periodischer Verrechnungspreis (V) |  |  |
| 6 | Zum Hauptbild zurückkehren | Wählen Sie Übernehmen, um zum Bild Produkt zurückzukehren. | Das Bild Produkt wird angezeigt. |  |
| 7 | Daten sichern | Wählen Sie Sichern. | Das Objekt wird gesichert. |  |

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
- related-to :: [[02-business-partner-and-product-master-data/master-data-script-create-product-master-of-type-returnable-packaging]]
- related-to :: [[02-business-partner-and-product-master-data/mds-65b-499]]
- related-to :: [[02-business-partner-and-product-master-data/mds-65b-501]]
- related-to :: [[02-business-partner-and-product-master-data/script-de-dados-mestre-criar-mestre-de-produtos-do-tipo-embalagem-reto]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/65B_S4CLD2608_Master_Data_DE_XX.docx` — full document · extracted with `mammoth` · 39,257 chars in the whole document
