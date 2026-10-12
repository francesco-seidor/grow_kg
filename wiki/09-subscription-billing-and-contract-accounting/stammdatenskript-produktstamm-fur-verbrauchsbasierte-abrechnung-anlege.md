---
id: 09-subscription-billing-and-contract-accounting/stammdatenskript-produktstamm-fur-verbrauchsbasierte-abrechnung-anlege
title: Stammdatenskript - Produktstamm für verbrauchsbasierte Abrechnung anlegen (3JA) (3JA_S4CLD2608_Master_Data_DE_XX)
description: "German master data script (3JA) for SAP S/4HANA Cloud Public Edition: create configurable material with variant pricing for consumption-based billing."
cluster: 09-subscription-billing-and-contract-accounting
tags: [kb/subscription-billing-and-contract-accounting, topic/variant-configured-products-in-provider-contracts]
aliases: [3JA_S4CLD2608_Master_Data_DE_XX]
keywords: [Variant-Configured Products in Provider Contracts, product master data, consumption-based billing, configurable material, characteristics, classes, configuration profile, material classification, variant pricing, sales data]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/3JA_S4CLD2608_Master_Data_DE_XX.docx]
confidence: high
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-322
topic: 09-subscription-billing-and-contract-accounting/variant-configured-products-in-provider-contracts
language: DE
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Stammdatenskript - Produktstamm für verbrauchsbasierte Abrechnung anlegen (3JA) (3JA_S4CLD2608_Master_Data_DE_XX)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/3JA_S4CLD2608_Master_Data_DE_XX.docx`, extracted with `mammoth`. Grouped under **Variant-Configured Products in Provider Contracts** in Subscription Billing and Contract Accounting. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

| <!-- image omitted: unnamed --> | StammdatenskriptSAP S/4HANA Cloud Public Edition - 02-07-26 |
| --- | --- |
|  | Produktstamm für verbrauchsbasierte Abrechnung anlegen – SDS (3JA) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Inhaltsverzeichnis

[1 Zweck 2](#_Toc233889624)

[2 Voraussetzungen 3](#_Toc233889625)

[2.1 Systemzugriff 3](#_Toc233889626)

[2.2 Rollen 3](#_Toc233889627)

[2.3 Erforderliche Organisationseinheiten 3](#_Toc233889628)

[2.4 Obligatorische und optionale Stammdaten 4](#_Toc233889629)

[2.5 Wesentliche Parameter für die Datenerstellung 4](#_Toc233889630)

[2.5.1 Gruppierungen und Nummernkreise 4](#_Toc233889631)

[2.5.2 Branche 5](#_Toc233889632)

[3 Übersichtstabelle 6](#_Toc233889633)

[4 Testverfahren 7](#_Toc233889634)

[4.1 Konfigurierbaren Materialstamm anlegen – Grunddaten 7](#_Toc233889635)

[4.2 Merkmal anlegen 8](#_Toc233889636)

[4.3 Klasse anlegen 11](#_Toc233889637)

[4.4 Konfigurationsprofil anlegen 12](#_Toc233889638)

[4.5 Materialstamm anlegen – Klassifikation 13](#_Toc233889639)

[4.6 Variantenpreisfindung anlegen 14](#_Toc233889640)

[4.7 Produktstammdaten anlegen – Verkaufsdaten/Umsatzsteuerdaten 15](#_Toc233889641)

## Zweck

Dieses Dokument beschreibt, wie Sie einen Materialstammdatensatz für Ihr SAP S/4HANA Cloud Public Edition-System anlegen. Die Beschreibung umfasst die Datensegmente, die für die Stammdaten für die Arbeit in einer üblichen Systemumgebung relevant sind. Der Leser lernt hauptsächlich, welche Datensegmente und -felder hauptsächlich mit Eingabewerten gefüllt werden müssen. Felder, die für den Umfang in SAP S/4HANA Cloud Public Edition nicht relevant sind, werden in diesem Dokument nicht behandelt, obwohl sie möglicherweise in der Benutzeroberfläche angezeigt werden.

Ein wie hier beschrieben angelegter Produktstammsatz mit Variantenpreisfindung kann für die verbrauchsbasierte Abrechnung verwendet werden.

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
| Produktkonfigurationsmodellierer | SAP_BR_PRODUCT_CONFIG_MODELER | Variantenkonfiguration | SAP_BR_PRODUCT_CONFIG_MODELER |  |
| Stammdatenexperte – Produktdaten | SAP_BR_PRODMASTER_SPECIALIST | Stammdaten – Produkte / Produkt-Governance | SAP_BR_PRODMASTER_SPECIALIST / SAP_CMD_SPT_PR_GOV_PC |  |

### Erforderliche Organisationseinheiten

Einige Segmente von Stammdaten hängen von den Organisationseinheiten des Unternehmens ab. Allgemeine (zentrale) Daten hängen nicht von einer Organisationseinheit oder dem Buchungskreis ab. Die folgende Tabelle stellt eine Übersicht dieser verschiedenen Datensegmente und ihrer relevanten Organisationseinheiten bereit:

| Datensegment | Hängt ab von | Feldbeispiele | Kommentare | Zu verwendende Organisationseinheit |
| --- | --- | --- | --- | --- |
| Grunddaten | Unabhängig von Organisationeinheiten | Materialbeschreibung (Kurztext), Materialnummer, Materialgruppe, Basismengeneinheit usw. | Gunddaten existieren für einen Materialstammsatz nur einmal. | Nicht zutreffend |
| Verkaufsdaten | Werk, Verkaufsorg., Vertriebsweg | Steuerdaten, Positionstypengruppe usw. | Werksdaten können für jede Werks-ID Ihrer Unternehmensstruktur existieren, für die der Materialstammsatz verwendet wird. | Werk: ____________ Verkaufsorganisation: __________ Vertriebsweg: __________ |

### Obligatorische und optionale Stammdaten

Stammdatensätze können auf andere Stammdaten verweisen. Die folgende Tabelle bietet eine Übersicht über die optionalen und obligatorischen Stammdatenobjekte, die in einem Stammdatensatz verwendet werden müssen.

|  |
| --- |
| Hinweis Für eine ordnungsgemäße Steuerberechnung sind spezifische Felder für Brasilien erforderlich.Prüfen Sie Nota Fiscal – Brasilien - JD0 im Kapitel BR-spezifische Felder für Stammdaten definieren für Materialstammdaten. |

| Stammdatenobjekt | Verwendet im Datensegment | Obligatorisch / optional | Kommentare |
| --- | --- | --- | --- |
|  |  |  |  |
|  |  |  |  |

### Wesentliche Parameter für die Datenerstellung

In diesem Abschnitt werden einige Basisparameter erläutert, die das Verhalten eines Stammsatzes beeinflussen und zum Anlegen eines Materialstammdatensatzes immer erforderlich sind:

#### Gruppierungen und Nummernkreise

Anhand von Materialarten ermittelt das System welche Datensegmente (Sichten) bearbeitet werden können oder es ermittelt welche Felder Kann- oder Mussfelder sind. Basierend auf den Materialarten ermittelt das System außerdem die Nummernkreise für Materialien. Im SAP-Standardinhalt verwenden alle Materialarten die gleiche Nummernkreisdefinition.

#### Branche

Der Standard-Content bietet nur die Branche M. Diese ist zurzeit nur in der SAP GUI sichtbar.

## Übersichtstabelle

Dieser Stammdatensatz umfasst mehrere Segmente, die in der nachfolgenden Tabelle genannt sind.

|  |
| --- |
| Hinweis Wenn Ihr Systemadministrator Bereiche und Seiten auf dem SAP Fiori Launchpad aktiviert hat, enthält die Startseite nur die wesentlichen Apps, mit denen die typischen Aufgaben einer Benutzerrolle ausgeführt werden können.Alle anderen (suchbaren) Apps, die nicht auf der Startseite enthalten sind, finden Sie über die Suchleiste ([2434549](https://me.sap.com/notes/2434549)).Wenn Sie die Startseite personalisieren und versteckte Apps hinzufügen möchten, wechseln Sie in Ihr Benutzerprofil und wählen Sie App Finder. |

| Segment | Benutzerrolle | App/Transaktion | Erwartete Ergebnisse |
| --- | --- | --- | --- |
| [Konfigurierbaren Materialstamm anlegen – Grunddaten](#unique_11) [Seite ] 7 | Stammdatenexperte – Produktdaten | Material anlegen(MM01) | Materialstammdaten - Grunddaten werden erzeugt. |
| [Merkmal anlegen](#unique_12) [Seite ] 8 | Produktkonfigurationsmodellierer | Merkmale verwalten(CT04) | Das Merkmal wird angelegt. |
| [Klasse anlegen](#unique_13) [Seite ] 11 | Produktkonfigurationsmodellierer | Klassen verwalten(CL02) | Die Klasse wird angelegt. |
| [Konfigurationsprofil anlegen](#unique_14) [Seite ] 12 | Produktkonfigurationsmodellierer | VC-Modellierungsumgebung(PMEVC) | Das Konfigurationsprofil wird angelegt. |
| [Materialstamm anlegen – Klassifikation](#unique_15) [Seite ] 13 | Stammdatenexperte – Produktdaten | Material anlegen(MM01) | Materialstammdaten – Klassifizierung angelegt. |
| [Variantenpreisfindung anlegen](#unique_16) [Seite ] 14 | Produktkonfigurationsmodellierer | VC-Modellierungsumgebung(PMEVC) | Variantenkondition wird im Merkmalswert abgebildet. |
| [Produktstammdaten anlegen – Verkaufsdaten/Umsatzsteuerdaten](#unique_17) [Seite ] 15 | Stammdatenexperte – Produktdaten | Material anlegen(MM01) | Materialstammdaten - Verkaufsdaten (Umsatzsteuerdaten) werden angelegt. |

## Testverfahren

Dieser Abschnitt beschreibt die Vorgehensweisen für jedes Segment oder Prozessschritt, das bzw. der Teil dieses Stammsatzes ist.

### Konfigurierbaren Materialstamm anlegen – Grunddaten

Testverwaltung

Kundenprojekt: Füllen Sie die projektbezogenen Teile aus.

|  |  |  |  |
| --- | --- | --- | --- |
| Testfall-ID | <X.XX> | Testdatum: |  |
| Testername: |  | Dauer: |  |
| Benutzerrolle(n): |  | Zuständigkeit: | <Geben Sie den Serviceanbieter, einen Kunden oder einen Serviceanbieter zusammen mit einem Kunden an.> |

Zweck

In diesem Prozessschritt legen Sie Grunddatensicht für den Materialstamm an.

Vorgehensweise

| Testschrittnummer | Bezeichnung des Testschritts | Anweisung | Erwartetes Ergebnis | Kommentare |
| --- | --- | --- | --- | --- |
| 1 | Anmelden | Melden Sie sich am SAP Fiori Launchpad als Stammdatenexperte – Produktdaten an. | Das SAP Fiori Launchpad wird angezeigt. |  |
| 2 | SAP-Fiori-App aufrufen | Öffnen Sie Material anlegen(MM01). | Die App wird geöffnet. |  |
| 3 | Materialgrunddaten eingeben | Nehmen Sie auf dem Bild Material anlegen (Einstieg) die folgenden Einträge vor:Material: <CBPTS001>Branche: MHinweis Wenn das Eingabefeld "Branche" ausgeblendet ist, ist keine Eingabe erforderlich. Wird das Feld "Branche" nicht zur Eingabe angeboten, wird "Nicht bekannt" in dem Feld eingetragen.Materialart: KMAT - Konfigurierbare Materialien | Das Bild Sichtenauswahl wird angezeigt. |  |
| 4 | Views auswählen | Wählen Sie im Fenster Sichtenauswahl die Sichten Grunddaten 1 und Grunddaten 2 aus, und wählen Sie Weiter. | Das Bild Material anlegen (Konfigurierbare Materialien) wird angezeigt. |  |
| 5 | Grunddaten eingeben | Geben Sie auf dem Bild Material CBPTS001 anlegen (Konfigurierbare Materialien) auf der Registerkarte Grunddaten 1 die Materialbeschreibung (Kurztext) ein.Geben Sie z.B. <Verbrauchsabhängige Elektrowerkzeuge> ein. |  |  |
| 6 | Grunddaten eingeben | Nehmen Sie auf der Registerkarte Grunddaten 1 im Abschnitt Allgemeine Daten die folgenden Einträge vor:Basismengeneinheit: <Stück>Allg. PosTypGrp: <0003> |  |  |
| 7 | Grunddaten eingeben | Nehmen Sie im Bereich Dimensionen/EANs die folgenden Einträge vor:Gewichtseinheit: kgWählen Sie die Registerkarte Grunddaten 2. |  |  |
| 8 | Grunddaten eingeben | Auf der Registerkarte Grunddaten 2 müssen Sie keine Einträge vornehmen.Wählen Sie Enter. | Das Bild Letzte Datensicht erreicht wird mit der folgenden Meldung angezeigt: Sie beenden die Bearbeitung. Möchten Sie Ihre Daten zunächst sichern? |  |
| 9 | Daten sichern | Wählen Sie im Bild Letzte Datensicht erreicht die Drucktaste Ja. | Das Bild Material anlegen (Einstieg) wird geöffnet.Die Grunddaten werden angelegt und gesichert. |  |

### Merkmal anlegen

Testverwaltung

Kundenprojekt: Füllen Sie die projektbezogenen Teile aus.

|  |  |  |  |
| --- | --- | --- | --- |
| Testfall-ID | <X.XX> | Testdatum: |  |
| Testername: |  | Dauer: |  |
| Benutzerrolle(n): |  | Zuständigkeit: | <Geben Sie den Serviceanbieter, einen Kunden oder einen Serviceanbieter zusammen mit einem Kunden an.> |

Zweck

In diesem Prozessschritt legen Sie ein Merkmal an.

Vorgehensweise

| Testschrittnummer | Bezeichnung des Testschritts | Anweisungen | Erwartetes Ergebnis | Kommentare |
| --- | --- | --- | --- | --- |
| 1 | Anmelden | Melden Sie sich am SAP Fiori Launchpad als Produktkonfigurationsmodellierer an. | Das SAP Fiori Launchpad wird angezeigt. |  |
| 2 | "Kundenstammdaten verwalten" öffnen | Öffnen Sie Merkmale verwalten(CT04). | Die App wird geöffnet. | Gemeinsames Bild für die Modi Anlegen, Ändern und Anzeigen. |
| 3 | Merkmalnamen eingeben | Geben Sie folgende Daten ein, und wählen Sie Anlegen:Merkmal: <Kategorie> | Das Bild Merkmal anlegen wird angezeigt. | Das Feld Gültig ab wird automatisch mit einem Wert befüllt.Wenn das Merkmal <KATEGORIE> bereits vorhanden ist, legen Sie das Merkmal <KATEGORIE>_Vnn an, wobei nn die laufende Nummer darstellt. |
| 4 | Grunddaten eingeben | Geben Sie auf der Registerkarte Grunddaten folgende Daten ein:Im Bereich Grunddaten:Beschreibung: <Kategorie>Status: Freigegeben (Standard)Im Bereich Format:Datentyp: ZeichenformatAnzahl Stellen: <15>Abhängig von Groß-/Kleinschreibung: EntmarkiertIm Abschnitt Bewertung:Markieren Sie den Auswahlknopf Einwertig.Entmarkieren Sie das Ankreuzfeld Einschränkbar. |  |  |
| 5 | Werte eingeben | Geben Sie auf der Registerkarte Werte im Bereich Zulässige Werte folgenden Daten ein:Merkmals- wert:<STANDARD><HIGH-END>Beschreibung:<Standard-Elektrowerkzeuge><High-End-Elektrowerkzeuge>Wählen Sie das Ankreuzfeld Standardwert für den Wert <STANDARD>. |  |  |
| 6 | Merkmal sichern | Wählen Sie Sichern. | Das Merkmal wird angelegt. |  |
| 7 | Weiteres Merkmal anlegen | Geben Sie Folgendes ein, und wählen Sie Anlegen:Merkmal: <CATEGORY_VARCOND> |  |  |
| 8 | Grunddaten eingeben | Geben Sie auf der Registerkarte Grunddaten folgende Daten ein:Im Bereich Grunddaten:Beschreibung: <Variantenkonditionsschlüssel>Status: Freigegeben (Standard)Im Bereich Format:Datentyp: ZeichenformatAnzahl Stellen: <26>Abhängig von Groß-/Kleinschreibung: <markiert>Im Abschnitt Bewertung:Markieren Sie den Auswahlknopf Mehrere Werte.Entmarkieren Sie das Ankreuzfeld Einschränkbar. |  |  |
| 9 | Zusatzdaten eingeben | Geben Sie auf der Registerkarte Zusatzdaten folgende Daten ein.Im Bereich Verweis auf Tabellenfeld:Tabellenname: SDCOMFeldname: VKONDIm Abschnitt Verhalten bei Bewertung:nicht eingabebereit: <nicht markiert> |  |  |
| 10 | Merkmal sichern | Wählen Sie Sichern. |  |  |

### Klasse anlegen

Testverwaltung

Kundenprojekt: Füllen Sie die projektbezogenen Teile aus.

|  |  |  |  |
| --- | --- | --- | --- |
| Testfall-ID | <X.XX> | Testdatum: |  |
| Testername: |  | Dauer: |  |
| Benutzerrolle(n): |  | Zuständigkeit: | <Geben Sie den Serviceanbieter, einen Kunden oder einen Serviceanbieter zusammen mit einem Kunden an.> |

Zweck

In diesem Prozessschritt legen Sie eine Klasse der Klassenart 300 an.

Vorgehensweise

| Testschrittnummer | Bezeichnung des Testschritts | Anweisung | Erwartetes Ergebnis | Kommentare |
| --- | --- | --- | --- | --- |
| 1 | Anmelden | Melden Sie sich am SAP Fiori Launchpad als Produktkonfigurationsmodellierer an. | Das SAP Fiori Launchpad wird angezeigt. |  |
| 2 | SAP-Fiori-App aufrufen | Öffnen Sie Klassen verwalten(CL02). | Die App wird geöffnet. | Gemeinsames Bild für die Modi Anlegen, Ändern und Anzeigen. |
| 3 | Klassennamen eingeben | Geben Sie Folgendes ein, und wählen Sie Anlegen:Klasse: <KATEGORIE>Klassenart: 300 | Das Bild Klasse anlegen wird angezeigt. | Das Feld Gültig ab wird automatisch mit einem Wert befüllt.Wenn die Klasse <KATEGORIE> bereits vorhanden ist, legen Sie die Klasse <KATEGORIE>_Vnn an, wobei nn die laufende Nummer darstellt. |
| 4 | Grunddaten eingeben | Geben Sie auf der Registerkarte Grunddaten folgende Daten ein:Im Bereich Grunddaten:Beschreibung: <Kategorie Elektrowerkzeuge>Status: Freigegeben (Standard)Im Abschnitt Gleiche Klassifizierung:Markieren Sie den Auswahlknopf Nicht prüfen (Standard). |  | Wenn Sie die gleiche Klassifizierung verwenden, können Sie die Prüfungsmethode auswählen (Warnmeldung, Fehler, Nicht prüfen). |
| 5 | Registerkarte "Merkmale" | Geben Sie auf der Registerkarte Merkmal folgende Daten ein:Merkmal: <KATEGORIE>Merkmal: <KATEGORY_VARCOND> |  |  |
| 6 | Klasse sichern | Wählen Sie Sichern. | Die Klasse wird angelegt. |  |

### Konfigurationsprofil anlegen

Testverwaltung

Kundenprojekt: Füllen Sie die projektbezogenen Teile aus.

|  |  |  |  |
| --- | --- | --- | --- |
| Testfall-ID | <X.XX> | Testdatum: |  |
| Testername: |  | Dauer: |  |
| Benutzerrolle(n): |  | Zuständigkeit: | <Geben Sie den Serviceanbieter, einen Kunden oder einen Serviceanbieter zusammen mit einem Kunden an.> |

Zweck

In diesem Prozessschritt legen Sie ein Konfigurationsprofil an.

Vorgehensweise

| Testschrittnummer | Bezeichnung des Testschritts | Anweisung | Erwartetes Ergebnis | Kommentare |
| --- | --- | --- | --- | --- |
| 1 | Anmelden | Melden Sie sich am SAP Fiori Launchpad als Produktkonfigurationsmodellierer an. | Das SAP Fiori Launchpad wird angezeigt. |  |
| 2 | SAP-Fiori-App aufrufen | Öffnen Sie VC-Modellierungsumgebung(PMEVC). | Die App wird geöffnet. |  |
| 3 | Konfigurationsmodelldaten eingeben | Geben Sie auf dem Einstiegsbild folgende Daten ein, und wählen Sie Modell eingeben:Material: <CBPTS001>Klassenart: 300 (Standard) | Das Konfigurationsbild wird angezeigt. |  |
| 4 | Konfigurationsprofil anlegen | Klicken Sie mit der rechten Maustaste im Bereich Objekt auf den Knoten <CBPTS001>, und wählen Sie Konfigurationsprofil anlegen.Geben Sie im Dialogfenster Konfigurationsprofil anlegen folgende Daten ein:Konfigurationsprofil: <CBPT_CP_V01>Wählen Sie Weiter. | Das Bild Konfigurationsprofil anlegen wird im rechten Bereich angezeigt und die Registerkarte Grunddaten ist ausgewählt. |  |
| 5 | Konfigurationsprofil sichern | Wählen Sie Sichern. | Das Konfigurationsprofil wird angelegt. |  |

### Materialstamm anlegen – Klassifikation

Testverwaltung

Kundenprojekt: Füllen Sie die projektbezogenen Teile aus.

|  |  |  |  |
| --- | --- | --- | --- |
| Testfall-ID | <X.XX> | Testdatum: |  |
| Testername: |  | Dauer: |  |
| Benutzerrolle(n): |  | Zuständigkeit: | <Geben Sie den Serviceanbieter, einen Kunden oder einen Serviceanbieter zusammen mit einem Kunden an.> |

Zweck

In diesem Prozessschritt legen Sie eine Klassifikationssicht für den Materialstamm an.

Voraussetzung

Sie müssen erst die Schritte aus dem vorherigen Abschnitt [Konfigurierbaren Materialstamm anlegen – Grunddaten](#unique_11) [Seite ] 7 abschließen, bevor Sie mit diesem Abschnitt fortfahren können. Beginnen Sie mit dieser Vorgehensweise, nachdem Sie die eingegebenen Grunddaten gesichert haben, wie in der vorherigen Vorgehensweise erläutert.

Vorgehensweise

| Testschrittnummer | Bezeichnung des Testschritts | Anweisung | Erwartetes Ergebnis | Kommentare |
| --- | --- | --- | --- | --- |
| 1 | Anmelden | Melden Sie sich am SAP Fiori Launchpad als Stammdatenexperte – Produktdaten an. | Das SAP Fiori Launchpad wird angezeigt. |  |
| 2 | SAP-Fiori-App aufrufen | Öffnen Sie Material anlegen(MM01). | Die App wird geöffnet. |  |
| 3 | Materialgrunddaten eingeben | Nehmen Sie auf dem Bild Material anlegen (Einstieg) die folgenden Einträge vor:Material: <CBPTS001>Branche: MHinweis Wenn das Eingabefeld "Branche" ausgeblendet ist, ist keine Eingabe erforderlich. Wenn die Branche nicht zur Eingabe angeboten wird, wird "nicht bekannt" im Feld eingetragen.Materialart: KMAT - Konfigurierbare Materialien | Das Bild Sichtenauswahl wird angezeigt. |  |
| 4 | Views auswählen | Wählen Sie auf dem Bild Sichtenauswahl die Sicht Klassifikation aus, und wählen Sie Weiter. | Das Bild Klassenart (1) wird angezeigt. |  |
| 5 | Klassenart eingeben | Geben Sie im Abschnitt Restriktionsebene die folgenden Daten ein, und wählen Sie Weiter:Klassenartentext: VariantenTyp: 300 | Das Bild Klassifikation wird angezeigt. |  |
| 6 | Klassifikationsdaten eingeben | Geben Sie auf dem Bild Klassifikation auf der Registerkarte Zuordnungen die folgenden Daten in der Spalte Klasse ein, und wählen Sie Sichern.<Kategorie>Geben Sie auf der Registerkarte Werte der Klasse KATEGORIE – Objekt <CBPTS001> die folgenden Daten in der Spalte Wert ein, und wählen Sie Sichern.<STANDARD><HIGH-END> | Ihre Daten werden gesichert. |  |

### Variantenpreisfindung anlegen

Testverwaltung

Kundenprojekt: Füllen Sie die projektbezogenen Teile aus.

|  |  |  |  |
| --- | --- | --- | --- |
| Testfall-ID | <X.XX> | Testdatum: |  |
| Testername: |  | Dauer: |  |
| Benutzerrolle(n): |  | Zuständigkeit: | <Geben Sie den Serviceanbieter, einen Kunden oder einen Serviceanbieter zusammen mit einem Kunden an.> |

Zweck

Die Variantenkondition wird im Merkmalswert abgebildet.

Vorgehensweise

| Testschrittnummer | Bezeichnung des Testschritts | Anweisung | Erwartetes Ergebnis | Kommentare |
| --- | --- | --- | --- | --- |
| 1 | Anmelden | Melden Sie sich am SAP Fiori Launchpad als Produktkonfigurationsmodellierer an. | Das SAP Fiori Launchpad wird angezeigt. |  |
| 2 | SAP-Fiori-App aufrufen | Öffnen Sie VC-Modellierungsumgebung(PMEVC). | Die App wird geöffnet. |  |
| 3 | Konfigurationsmodelldaten eingeben | Geben Sie auf dem Einstiegsbild folgende Daten ein, und wählen Sie Modellpflege eingeben:Material: <CBPTS001>Klassenart: 300 (Standard) | Das Konfigurationsbild wird angezeigt. |  |
| 4 | Variantenpreisfindung anlegen | Doppelklicken Sie im Abschnitt Objekt auf die Option <CBPTS001>, und wählen Sie im rechten Bereich die Registerkarte Variantenpreisfindung.Wählen Sie Ändern und geben Sie Folgendes ein:Merkmal: <Kategorie>Merkmals- wert: <HIGH-END>Variantenkondition: <HIGH-END> |  |  |
| 5 | Konfiguration sichern | Wählen Sie Sichern. | Die Variantenpreisfindung wird angelegt. |  |

### Produktstammdaten anlegen – Verkaufsdaten/Umsatzsteuerdaten

Testverwaltung

Kundenprojekt: Füllen Sie die projektbezogenen Teile aus.

|  |  |  |  |
| --- | --- | --- | --- |
| Testfall-ID | <X.XX> | Testdatum: |  |
| Testername: |  | Dauer: |  |
| Benutzerrolle(n): |  | Zuständigkeit: | <Geben Sie den Serviceanbieter, einen Kunden oder einen Serviceanbieter zusammen mit einem Kunden an.> |

Zweck

In diesem Prozessschritt legen Sie eine Verkaufsdatensicht für den Materialstamm an.

Vorgehensweise

| Testschrittnummer | Bezeichnung des Testschritts | Anweisung | Erwartetes Ergebnis | Kommentare |
| --- | --- | --- | --- | --- |
| 1 | Anmelden | Melden Sie sich am SAP Fiori Launchpad als Stammdatenexperte – Produktdaten an. | Das SAP Fiori Launchpad wird angezeigt. |  |
| 2 | SAP-Fiori-App aufrufen | Öffnen Sie Material anlegen(MM01). | Die App wird geöffnet. |  |
| 3 | Materialgrunddaten eingeben | Nehmen Sie auf dem Bild Material anlegen (Einstieg) die folgenden Einträge vor:Material: <CBPTS001>Branche: MHinweis Wenn das Eingabefeld "Branche" ausgeblendet ist, ist keine Eingabe erforderlich. Wird das Feld "Branche" nicht zur Eingabe angeboten, wird "Nicht bekannt" in dem Feld eingetragen.Materialart: KMAT - Konfigurierbare Materialien | Das Bild Sichtenauswahl wird angezeigt. |  |
| 4 | Sichten wählen | Wählen Sie im Bild Sichtenauswahl die Option Vertrieb: VerkaufsorgDaten 1, Vertrieb: VerkaufsorgDaten 2 und Vertrieb: Allg./Werksdaten aus, und wählen Sie dann Weiter. | Das Bild Organisationsebenen wird angezeigt. |  |
| 5 | Organisationsebenendaten eingeben | Geben Sie auf dem Bild Organisationsebenen im Abschnitt Organisationsebenen folgende Daten ein, und wählen Sie Weiter:Werk: z.B. <1010>Verkaufsorg.: z.B. <1010 für Werk 1010>Vertriebsweg: z.B. <10> | Das Bild Material anlegen (Konfigurierbare Materialien) wird angezeigt.Im unteren Bildbereich wird die folgende Systemmeldung angezeigt: Das Material existiert bereits und wird erweitert. |  |
| 6 | Verkaufsdaten eingeben | Geben Sie im Bild Material CBPTS001 anlegen (Konfigurierbare Materialien) auf der Registerkarte Vertrieb: VerkOrg 1 einen geeigneten Wert für die Steuerklassifikation ein.In der Regel wird der Wert 1 für voll steuerpflichtig verwendet.Wählen Sie Enter. | Die Sicht Verkauf: VerkOrg 2 wird angezeigt.Der eingegebene Wert zeigt an, dass das Material (für gewöhnlich) voll steuerpflichtig ist. |  |
| 7 | Verkaufsdaten eingeben | Nehmen Sie auf der Registerkarte Vertrieb: VerkOrg 2 im Abschnitt Gruppierungsbegriffe den folgenden Eintrag vor, und wählen Sie ENTER:Positionstypengruppe: <0003> | Die Sicht Verkauf: Allg./Werk wird angezeigt. |  |
| 8 | Verkaufsdaten eingeben | Nehmen Sie auf der Registerkarte Vertrieb: Allg./Werk im Abschnitt Allgemeine Daten die folgenden Einträge vor, und drücken Sie ENTER:Verfügbarkeitsprüfung: z.B. <NC> | Das Bild Letzte Datensicht erreicht wird mit der folgenden Meldung angezeigt: Sie beenden die Bearbeitung. Möchten Sie Ihre Daten zunächst sichern? |  |
| 9 | Daten sichern | Wählen Sie Ja auf dem Bild Letzte Datensicht erreicht. | Das Bild Stammdaten - Produkt wird angezeigt.Ihre Daten werden gesichert. |  |

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
- related-to :: [[09-subscription-billing-and-contract-accounting/master-data-script-create-product-master-for-consumption-based-billing]]
- related-to :: [[09-subscription-billing-and-contract-accounting/mds-3ja-325]]
- related-to :: [[09-subscription-billing-and-contract-accounting/mds-3ja-327]]
- related-to :: [[09-subscription-billing-and-contract-accounting/script-de-dados-mestre-criar-dados-mestre-do-produto-para-faturamento]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/3JA_S4CLD2608_Master_Data_DE_XX.docx` — full document · extracted with `mammoth` · 26,466 chars in the whole document
