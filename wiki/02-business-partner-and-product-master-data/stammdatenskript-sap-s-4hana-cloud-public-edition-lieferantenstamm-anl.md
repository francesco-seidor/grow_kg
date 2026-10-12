---
id: 02-business-partner-and-product-master-data/stammdatenskript-sap-s-4hana-cloud-public-edition-lieferantenstamm-anl
title: Stammdatenskript SAP S/4HANA Cloud Public Edition - Lieferantenstamm anlegen – SDS (BNE) (BNE_S4CLD2608_Master_Data_DE_XX)
description: "German master data script (SAP S/4HANA Cloud Public Edition 2608) with test steps to create supplier master data: general, company code and purchasing org data."
cluster: 02-business-partner-and-product-master-data
tags: [kb/business-partner-and-product-master-data, topic/supplier-master]
aliases: [BNE_S4CLD2608_Master_Data_DE_XX]
keywords: [Supplier Master Data, general supplier data, company code data, purchasing organization data, business partner grouping, business partner roles, number ranges, account group, user roles, withholding tax]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/BNE_S4CLD2608_Master_Data_DE_XX.docx]
confidence: low
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-586
topic: 02-business-partner-and-product-master-data/supplier-master
language: DE
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Stammdatenskript SAP S/4HANA Cloud Public Edition - Lieferantenstamm anlegen – SDS (BNE) (BNE_S4CLD2608_Master_Data_DE_XX)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/BNE_S4CLD2608_Master_Data_DE_XX.docx`, extracted with `mammoth`. Grouped under **Supplier Master Data** in Business Partner and Product Master Data. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

| <!-- image omitted: unnamed --> | StammdatenskriptSAP S/4HANA Cloud Public Edition - 02-07-26 |
| --- | --- |
|  | Lieferantenstamm anlegen – SDS (BNE) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Inhaltsverzeichnis

[1 Verwendungszweck 2](#_Toc233889942)

[2 Voraussetzungen 3](#_Toc233889943)

[2.1 Systemzugriff 3](#_Toc233889944)

[2.2 Rollen 3](#_Toc233889945)

[2.3 Vorbereitende Schritte 3](#_Toc233889946)

[2.4 Erforderliche Organisationseinheiten 4](#_Toc233889947)

[2.5 Obligatorische und optionale Stammdaten 5](#_Toc233889948)

[2.6 Wesentliche Parameter für die Datenerstellung 5](#_Toc233889949)

[2.6.1 Geschäftspartnergruppierung und Nummernkreise 5](#_Toc233889950)

[2.6.2 Geschäftspartner-ID: 6](#_Toc233889951)

[2.6.3 Geschäftspartner - Rolle 6](#_Toc233889952)

[2.6.4 Kontengruppe 7](#_Toc233889953)

[3 Übersichtstabelle 8](#_Toc233889954)

[4 Testverfahren 9](#_Toc233889955)

[4.1 Lieferantenstammdaten anlegen - Allgemeine Daten 9](#_Toc233889956)

[4.2 Lieferantenstammdaten anlegen - Buchungskreisdaten 15](#_Toc233889957)

[4.3 Lieferantenstammdaten anlegen - Einkaufsorganisationsdaten 22](#_Toc233889958)

## Verwendungszweck

Geschäftskontext

Ein Lieferant ist ein Geschäftspartner, der Ihrer Organisation Waren verkauft und Services erbringt. Ein Geschäftspartner kann gleichzeitig Lieferant und Kunde sein, z.B. wenn Ihr Lieferant auch Waren bei Ihnen kauft.

Ein Lieferantenstamm enthält Informationen zu dem Lieferanten, z.B. den Namen, die Adresse, die Bankverbindung, Steuerdetails und Rechnungspräferenzen. Diese Lieferanteninformationen werden bei Transaktionen wie Bestellungen, Wareneingängen und Lieferantenrechnungen verwendet und gespeichert.

Einige Lieferanteninformationen sind für ein bestimmtes Unternehmen (Buchungskreis) oder eine bestimmte Einkaufsabteilung (Einkaufsorganisation) in Ihrer Organisation spezifisch.

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
| Stammdatenexperte – Geschäftspartnerdaten | SAP_BR_BUPA_MASTER_SPECIALIST | Stammdaten – Geschäftspartner / Geschäftspartner-Governance / Geschäftspartner-Governance / Geschäftspartner-Governance | SAP_BR_BUPA_MASTER_SPECIALIST / SAP_CA_SPT_MDG_BP_GOV_PC / SAP_CMD_SPT_BP_GOV_PC / SAP_CA_SPT_MDG_BP_WFUSR_PC |  |

### Vorbereitende Schritte

Kontext

In diesem Schritt ordnen Sie dem Testbenutzer die Rollen aus dem Kapitel "Rollen" zu, die für die Datenreplikation erforderlich sind. Stellen Sie vor Ausführung dieses Schritts sicher, dass Sie die erforderlichen Rollen für das spezifische Objekt zur Datenreplikation angelegt und hinzugefügt haben.

| Testschrittnummer | Bezeichnung des Testschritts | Anweisung | Erwartetes Ergebnis | Bestanden/Nicht bestanden/Anmerkung |
| --- | --- | --- | --- | --- |
| 1 | Anmelden | Melden Sie sich am SAP Fiori Launchpad mit Ihren Anmeldeinformationen an. | Die Startseite wird angezeigt. |  |
| 2 | SAP-Fiori-App aufrufen | Wählen Sie Anwendungsbenutzer pflegen. |  |  |
| 3 | Benutzernamen eingeben | Geben Sie den Benutzernamen ein, den Sie von Ihrem Systemadministrator erhalten haben, und wählen Sie Start. |  |  |
| 4 | Benutzer auswählen | Wählen Sie den Benutzer in der Liste aus. |  |  |
| 5 | Bearbeiten | Wählen Sie Bearbeiten. |  |  |
| 6 | Benutzerrollen hinzufügen | Wählen Sie Benutzerrollen hinzufügen, geben Sie im Feld Suchen die betreffende Benutzerrolle ein, und wählen Sie Enter. |  |  |
| 7 | Benutzerrollen auswählen | Wählen Sie die erforderlichen Benutzerrollen aus, und wählen Sie OK. |  |  |
| 8 | Sichern | Wählen Sie Sichern. | Die Benutzerrollen werden gesichert. |  |
| 9 | Startseite | Kehren Sie zur SAP-Startseite zurück. | Die Startseite wird angezeigt. |  |

### Erforderliche Organisationseinheiten

Einige Segmente von Lieferantenstammdaten hängen von den Organisationseinheiten des Unternehmens ab. Allgemeine (zentrale) Daten hängen nicht von einer Organisationseinheit oder dem Buchungskreis ab. Die folgende Tabelle stellt eine Übersicht dieser verschiedenen Datensegmente und ihrer relevanten Organisationseinheiten bereit:

| Datensegment | Hängt ab von | Feldbeispiele | Kommentare | Zu verwendende Organisationseinheit |
| --- | --- | --- | --- | --- |
| Allgemeine / zentrale Daten | Unabhängig von Organisationseinheiten | ID, Name, Adresse, Bankkonto, Steuernummer usw. | Zentrale Daten existieren für einen Lieferantenstammdatensatz nur einmal. | – |
| Buchungskreisdaten | Buchungskreis | Abstimmkonto, Zahlungsbedingungen, zuständiger Sachbearbeiter usw. | Buchungskreisdaten können für jede Buchungskreis-ID Ihrer Unternehmensstruktur vorhanden sein, für die der Lieferantenstammdatensatz verwendet wird. | Buchungskreis:____________ |
| Einkaufsdaten | Einkaufsorganisation | Auftragswährung, Zahlungsbedingungen, Einkäufergruppe, Versandbedingungen | Einkaufsdaten können für jede Einkaufsorganisation vorhanden sein, für die der Lieferantenstammdatensatz verwendet wird. | Einkaufsorganisation:__________ |

### Obligatorische und optionale Stammdaten

Lieferantenstammdatensätze können auf andere Stammdaten verweisen. Die folgende Tabelle bietet eine Übersicht über die optionalen und obligatorischen Stammdatenobjekte, die in einem Lieferantenstammdatensatz verwendet werden müssen.

|  |
| --- |
| Hinweis Prüfen Sie Nota Fiscal – Brasilien - JD0 im Kapitel BR-spezifische Felder für Stammdaten definieren für Lieferantenstammdaten. |

| Stammdatenobjekt | Verwendet im Datensegment | Obligatorisch / optional | Kommentare |
| --- | --- | --- | --- |
| Bankstamm | Auf dem Geschäftspartner-UI finden Sie die Eingabe der Bankkontodaten im Abschnitt Zahlungsverkehr. | Optional | Wenn Sie die Bankkonten des Lieferanten pflegen möchten, müssen Sie den Bankenstamm der entsprechenden Bank angelegt haben. In den Kundenstammsätzen können Sie dann die Ist-Kontonummer gemeinsam mit den Bankstammdaten eingeben. |
| Abstimmkonto | Auf dem Geschäftspartner-UI finden Sie den Eintrag der Abstimmkontodaten unter Buchungskreis > Lieferantenkontenverwaltung | Obligatorisch | Für das Abstimmkonto geben Sie die Sachkontonummer aus dem Debitorennebenbuch ein.Bevor Sie das Sachkonto im Lieferantenstammsatz verwenden können, müssen Sie es zuvor angelegt haben. |

### Wesentliche Parameter für die Datenerstellung

In diesem Abschnitt werden einige Basisparameter erläutert, die das Verhalten eines Stammsatzes beeinflussen und zum Anlegen eines Lieferantenstammdatensatzes immer erforderlich sind:

#### Geschäftspartnergruppierung und Nummernkreise

Geschäftspartnergruppierungen legen die Nummernkreise für die Geschäftspartner-IDs fest. Sie können anschließend die Zuordnung oder die IDs nicht mehr ändern. Wenn eine Geschäftsgruppierung einem internen Nummernkreis zugeordnet ist, können Sie die Geschäftspartner-ID nicht manuell eingeben. Lassen Sie das Feld in diesem Fall leer, da das System automatisch eine Nummer aus dem zugeordneten numerischen Nummernkreis wählt.

Die folgenden Geschäftspartnergruppierungen und entsprechenden Nummernkreise sind für Geschäftspartner (Kunden, Lieferanten, Ansprechpartner, Mitarbeiter etc.) definiert:

| Geschäftspartnergruppierung | Bereich / Geschäftspartner-ID | Kommentare |
| --- | --- | --- |
| BP01 | Externer numerischer Nummernkreis (niedrig):1 – 999999 | Verwenden Sie diese Gruppierung, um z.B. numerische Stammdatensätze zu migrieren. |
| BP02 | Interner nummerischer Nummernkreis für Standardverwendung:1000000 – 9999999 | Wird keine Geschäftspartnergruppe eingegeben, wird dieser Nummernkreis standardmäßig verwendet |
| BP03 | Externer numerischer Nummernkreis (hoch):10000000 – 999999999 | Für SAP-Musterstammdatenobjekte reserviert. |
| BPAB | Externer alphanumerischer Nummernkreis:A – ZZZZZZZZZZ | Dieser Bereich muss mit einem Buchstaben beginnen. |
| BPEE | Interner numerischer Nummernkreis:9980000000 – 9999999999 | Für Geschäftspartner reserviert, die als Mitarbeiter verwendet werden. |

#### Geschäftspartner-ID:

Geschäftspartner-ID:

Es sind die folgenden Optionen zum Zuordnen der Geschäftspartnerkennung (ID) verfügbar:

- Geben Sie eine ID zusammen mit der Geschäftspartnergruppierung für externe Nummerierung ein. Beispiel:

| Geschäftspartnergruppierung | Eingabemöglichkeiten für die Geschäftspartner-ID |
| --- | --- |
| BP01 | Beliebige Nummer im entsprechenden Intervall 1 – 999999 |
| BPAB | Beliebige alphanumerische Kombination mit bis zu 10 Zeichen, sofern diese mit einem Buchstaben beginnt, zum Beispiel Z-TEST01 |

Haben Sie keine Geschäftspartnergruppierung angegeben und lassen die Geschäftspartner-ID leer, nimmt das System die nächste freie Nummer aus der Geschäftspartnergruppierung BP02. Diese Gruppierung wird als Standardgruppierung für interne numerische Geschäftspartner-IDs definiert.

#### Geschäftspartner - Rolle

Geschäftspartner - Rolle

Die Partnerrolle legt die Rechte und Zuständigkeiten jedes Partners in einem Geschäftsvorgang fest.

Beispiele für Partnerrollen im Einkauf sind: Kreditor, Rechnungssteller, Warenlieferant usw.

#### Kontengruppe

Kontengruppen sind führende Steuerungsparameter zum Anlegen der ERP-Datensegmente eines Lieferantenstammsatzes. Derzeit ist SUPL die einzige unterstützte Kontengruppe für Lieferantenstammdaten.

## Übersichtstabelle

Dieser Umfangsbestandteil umfasst mehrere Prozessschritte, die in der folgenden Tabelle aufgelistet sind:

|  |
| --- |
| Hinweis Wenn Ihr Systemadministrator Bereiche und Seiten auf dem SAP Fiori Launchpad aktiviert hat, enthält die Startseite nur die wesentlichen Apps, mit denen die typischen Aufgaben einer Benutzerrolle ausgeführt werden können.Alle anderen (suchbaren) Apps, die nicht auf der Startseite enthalten sind, finden Sie über die Suchleiste ([2434549](https://me.sap.com/notes/2434549)).Wenn Sie die Startseite personalisieren und versteckte Apps hinzufügen möchten, wechseln Sie in Ihr Benutzerprofil und wählen Sie App Finder. |

| Prozessschritt | Anwendungsrolle | App/Vorgang | Erwartete Ergebnisse |
| --- | --- | --- | --- |
| [Lieferantenstammdaten anlegen - Allgemeine Daten](#unique_14) [Seite ] 9 | Stammdatenexperte – Geschäftspartnerdaten | Geschäftspartner pflegen(BP) oder Lieferantenstammdaten verwalten(F1053A) | Lieferantenstamm - Allgemeine Daten werden erzeugt |
| [Lieferantenstammdaten anlegen - Buchungskreisdaten](#unique_15) [Seite ] 15 | Stammdatenexperte – Geschäftspartnerdaten | Geschäftspartner pflegen(BP) oder Lieferantenstammdaten verwalten(F1053A) | Lieferantenstamm - Buchungskreisdaten werden erzeugt |
| [Lieferantenstammdaten anlegen - Einkaufsorganisationsdaten](#unique_16) [Seite ] 22 | Stammdatenexperte – Geschäftspartnerdaten | Geschäftspartner pflegen(BP) oder Lieferantenstammdaten verwalten(F1053A) | Lieferantenstamm - Einkaufsdaten werden erzeugt |

## Testverfahren

In diesem Abschnitt werden die Testverfahren für den jeweiligen Prozessschritt beschrieben, der zum betreffenden Umfangsbestandteil gehört.

### Lieferantenstammdaten anlegen - Allgemeine Daten

Testverwaltung

Kundenprojekt: Füllen Sie die projektbezogenen Teile aus.

|  |  |  |  |
| --- | --- | --- | --- |
| Testfall-ID | <X.XX> | Testdatum: |  |
| Testername: |  | Dauer: |  |
| Benutzerrolle(n): |  | Zuständigkeit: | <Geben Sie den Serviceanbieter, einen Kunden oder einen Serviceanbieter zusammen mit einem Kunden an.> |

Zweck

In diesem Verfahren erhalten Sie eine Anleitung zum Anlegen von Lieferantenstammdaten. Die zur Verfügung stehenden Apps hängen von der Ihnen zugeordneten Rolle ab. Daher werden zwei Optionen bereitgestellt.

Vorgehensweise: Option 1 – Geschäftspartner bearbeiten

Folgen Sie dieser Vorgehensweise, wenn Sie mit Ihrer Benutzerrolle auf die App Geschäftspartner pflegen(BP) zugreifen können.

| Testschrittnummer | Bezeichnung des Testschritts | Anweisungen | Erwartetes Ergebnis | Kommentare |
| --- | --- | --- | --- | --- |
| 1 | Anmelden | Melden Sie sich am SAP Fiori Launchpad als Stammdatenexperte – Geschäftspartnerdaten an. | Das SAP Fiori Launchpad wird angezeigt. |  |
| 2 | SAP-Fiori-App aufrufen | Öffnen Sie Geschäftspartner pflegen(BP). | Die App wird geöffnet. |  |
| 3 | Geschäftspartnerorganisation anlegen | Wählen Sie Organisation. | Das Bild Organisation anlegen wird angezeigt. |  |
| 4 | Allgemeine Daten eingeben | Geben Sie Folgendes ein, und wählen Sie OK.Geschäftspartner: <Geben Sie eine mit einem Buchstaben beginnende Geschäftspartner-ID ein.>Gruppierung: Wählen Sie z.B. Externe alphanumerische Nummerierung.Das Feld Anlegen in GP-Rolle wird vom System mit der Rolle GPartner allgemein ausgefüllt. Behalten Sie diese Einstellung bei.Hinweis Weitere Informationen finden Sie im vorherigen Kapitel [Geschäftspartnergruppierung und Nummernkreise](#unique_9) [Seite ] 5. |  |  |
| 5 | Adressdaten eingeben | Geben Sie auf der Registerkarte Adresse im Abschnitt Name die folgenden Daten ein:Titel: <Unternehmen>Name: <Name> |  |  |
| 6 | Suchbegriff eingeben | Geben Sie auf der Registerkarte Adresse im Abschnitt Suchbegriff einen oder mehrere Suchbegriffe für den Lieferanten ein. |  |  |
| 7 | Adressdaten eingeben | Geben Sie im Abschnitt Standardadresse im Unterabschnitt Straßenadresse die Adresse ein. |  |  |
| 8 | Zeit- und Transportzone eingeben | Wählen Sie im Abschnitt Straßenadresse die Option Weitere Felder. Geben Sie folgende Daten ein:Zeitzone: <Zeitzone>Transportzone <Transportzone> |  |  |
| Nur für Thailand | Adressdaten eingeben (nur für Thailand) | Wählen Sie im Abschnitt Straßenadresse die Option Mehr, und geben Sie folgende Daten ein:Gebäudekürzel: <Gebäude>Raum: <Raumnummer>Etage: <Etagennummer>Straße 2: <Moo>Straße 3: <SOI/Lane>Straße: <Straße>Hausnummer: <Nr.>Anderer Ort: <Unterbezirk>Ortsteil: <Ortsteil/Abschnitt>Ort: <Provinz>Postleitzahl: <Postleitzahl> |  |  |
| 9 | Kommunikationsdaten eingeben | Geben Sie auf der Registerkarte Adresse im Abschnitt Kommunikation die folgenden Daten ein:Sprache: <Wählen Sie die bevorzugte Sprache des Lieferanten aus.>Telefon: <Telefonnummer>E-Mail: <E-Mail-Adresse> |  |  |
| 10 | Identifikationsdaten eingeben | Geben Sie auf der Registerkarte Identifikation im Abschnitt Organisationsdaten die folgenden Daten zum Lieferanten ein:Rechtsform: <Rechtsform> |  |  |
| Nur für Japan | Branchendaten eingeben (nur für Japan) | Wählen Sie auf der Registerkarte Identifikation im Abschnitt Branchen die Option Alle Branchensysteme. Geben Sie folgende Daten ein:Branchensystem: Wählen Sie Bank of Japan.Branche: <Wählen Sie eine Branchennummer aus.>Standardbranche: <nicht markiert> |  |  |
| Nur für Japan | Steuernnummerdaten eingeben (nur für Japan) | Bestätigen Sie mit Enter.Achtung Wenn Sie die falsche Einstellung wählen, können Sie die Daten für Japan: Meine Nummer nicht pflegen. |  |  |
| Nur für Japan | Daten für Steuernummer lang eingeben (nur für Japan) | Geben Sie auf der Registerkarte Identifikation im Abschnitt Steuernummer lang die folgenden Daten ein:Kategorie: JP4 Japan UmsatzsteueridentifikationsnummerSteuernummer lang: <Unternehmensnummer des Geschäftspartners> |  |  |
| 11 | Bankkonten eingeben | Geben Sie auf der Registerkarte Zahlungsverkehr im Abschnitt Bankverbindung die folgenden Daten zum Lieferanten ein:Land/Region: <Land/Region>Bankschlüssel: <Bankschlüssel>Bankkonto: <Bankkonto>Achtung Bankschlüssel müssen zuvor definiert werden. Weitere Informationen zu zulässigen Einträgen in diesem Feld finden Sie in der Eingabehilfe. |  |  |
| 12 | Daten sichern | Sichern Sie Ihre Eingaben. |  |  |

Vorgehensweise: Option 2 – Lieferantenstammdaten verwalten

Folgen Sie dieser Vorgehensweise, wenn Sie mit Ihrer Benutzerrolle auf die App Lieferantenstammdaten verwalten(F1053A) zugreifen können.

| Testschrittnummer | Bezeichnung des Testschritts | Anweisungen | Erwartetes Ergebnis | Kommentare |
| --- | --- | --- | --- | --- |
| 1 | Anmelden | Melden Sie sich am SAP Fiori Launchpad als Stammdatenexperte – Geschäftspartnerdaten an. | Das SAP Fiori Launchpad wird angezeigt. |  |
| 2 | SAP-Fiori-App aufrufen | Öffnen Sie Lieferantenstammdaten verwalten(F1053A). | Die App wird geöffnet. |  |
| 3 | "Anlegen" wählen | Wählen Sie im Abschnitt Lieferanten die Option Anlegen > Organisation. | Das Bild Organisation anlegen wird angezeigt. |  |
| 4 | Allgemeine Daten eingeben | Geben Sie im Abschnitt Allgemeine Daten die folgenden Daten ein, und wählen Sie OK:Geschäftspartner: z.B. Z …, d.h. eine beliebige externe alphanumerische ID, die mit einem Buchstaben beginnen mussGruppierung: z.B. <Externe alphanumerische Nummerierung>.Titel: z.B. Unternehmen (0003)Name 1: <Geben Sie einen Namen ein.> | Das Bild Neuer Lieferant wird angezeigt. |  |
| 5 | Grunddaten eingeben | Geben Sie auf dem Bild Neuer Lieferant auf der Registerkarte Grunddaten folgende Daten ein:Geben Sie im Abschnitt Lieferanteninformationen die folgenden Daten ein:Referenzkontengruppe, Lieferantenberechtigungsgruppe usw.: Wählen Sie einen Wert aus der Wertehilfe aus.Geben Sie im Abschnitt Organisationsdaten die folgenden Daten ein:Umsatzsteuerpflicht, Steuerteilung, Zahlsperre usw.: Wählen Sie den relevanten Indikator aus.Hinweis Weitere Informationen zu GP-Gruppierungen und deren Bezug zur ID-Nummerierung finden Sie im vorherigen Kapitel [Geschäftspartnergruppierung und Nummernkreise](#unique_9) [Seite ] 5.Geben Sie im Abschnitt Zusatzinformationen die folgenden Daten ein:Funktion sperren: Wählen Sie einen Wert aus der Wertehilfe aus.Werk: Wählen Sie einen Wert aus der Wertehilfe aus.Weisungsschlüssel: Wählen Sie einen Wert aus der Wertehilfe aus. |  |  |
| 6 | Rollen auswählen | Wählen Sie auf dem Bild Neuer Lieferant die Registerkarte Rollen. | Sie gelangen zum Abschnitt Rollen. |  |
| 7 | "Anlegen" wählen | Wählen Sie im Abschnitt Rollen die Option Anlegen, und wählen Sie eine Rolle aus der Wertehilfe aus:Geschäftspartnerrolle: z.B. FLVN01.Ein Lieferantenstamm muss entweder mit der Geschäftspartnerrolle FLVN00 (Kreditor) oder mit der Geschäftspartnerrolle FLVN01 (Lieferant mit Einkaufsdaten) oder mit beiden Rollen angelegt werden. Die Geschäftspartnerrolle FLVN00 (FI Kreditor) wird in der Finanzbuchhaltung verwendet, und die Geschäftspartnerrolle FLVN01 (Lieferant mit Einkaufsdaten) wird im Verkauf verwendet.Hinweis Stellen Sie sicher, dass die Meldung Entwurf gesichert im unteren Bildbereich angezeigt wird, bevor Sie zum Hauptbild zurückkehren. | Die Rolle wird hinzugefügt. |  |
| 8 | Zusätzliche Rollen eingeben (optional) | Wiederholen Sie die Schritte 6 und 7, um eine zusätzliche Rolle hinzuzufügen.Geschäftspartnerrolle: z.B. FLVN00. | Nachdem Sie alle Geschäftspartnerrollen eingegeben haben, werden diese auf dem Bild Rollen im Abschnitt Neuer Stamm angezeigt. |  |
| 9 | Standardadresse auswählen | Wählen Sie auf dem Bild Lieferantenstamm - Neuer Lieferant die Registerkarte Adresse, und wechseln Sie zum Abschnitt Standardadresse. | Sie gelangen zum Bildbereich Standardadresse. |  |
| 10 | Adressdaten eingeben | Nehmen Sie im Abschnitt Adresse - Standardadresse Einträge für alle relevanten Felder gemäß Ihren Anforderungen vor. Beispiel:Straße: <Straßenname>Hausnummer: <Nummer für die Adresse>Postleitzahl: <Postleitzahl für die Adresse>Ort: <Ort>Land/Region: <Länder-/Regionscode>Hinweis (Gilt nur für die USA) Wenn Sie einen Geschäftspartner mit Sitz in den USA anlegen, wird der Steuerstandortcode automatisch ermittelt. Wenn der Steuerstandort dagegen aus Ihren Eingaben für Land (USA), Bundesstaat und Postleitzahl abgeleitet wird, müssen Sie die korrekte und vollständige Adresse eingeben.Geben Sie im Bereich Adresse - Standardkommunikation folgende Daten ein:Sprache: <Sprache>Telefon: <Geben Sie die erforderlichen Daten in das Feld ein>E-Mail: z.B. contact@Z.comWählen Sie Anlegen.Wählen Sie im Abschnitt Adresse - Adressdetails den Adresseintrag aus.Prüfen Sie auf dem Bild Neue Adresse auf der Registerkarte Adressverwendungen, ob die folgenden Informationen angezeigt werden:Adresstyp: XXDEFAULT |  |  |
| 11 | Zum Hauptbild zurückkehren | Wählen Sie Übernehmen.Hinweis Stellen Sie sicher, dass die Meldung Entwurf gesichert im unteren Bildbereich angezeigt wird, bevor Sie zum Hauptbild zurückkehren. |  |  |
| 12 | Bankkonten wählen | Wählen Sie auf dem Bild Lieferantenstamm – Neuer Lieferant … die Registerkarte Bankkonten. | Sie gelangen zum Bereich Bankkonten. |  |
| 13 | "Anlegen" wählen | Wählen Sie auf dem Bild Kundenstamm - Bankkonten … die Drucktaste Anlegen. | Ein neues Bankkonto wird hinzugefügt. |  |
| 14 | Bankdaten erfassen | Geben Sie folgende Daten für das neue Bankkonto ein:ID: z.B. BNK1.Bankland/-region: <Länder-/Regionscode>Bankschlüssel: <Bankschlüssel>Kontonummer: <Kontonummer>Füllen Sie alle anderen Felder gemäß Ihren Anforderungen aus. |  |  |
| 15 | Zum Hauptbild zurückkehren | Wählen Sie Übernehmen.Hinweis Stellen Sie sicher, dass die Meldung Entwurf gesichert im unteren Bildbereich angezeigt wird, bevor Sie zum Hauptbild zurückkehren. |  |  |
| 16 | Steuernummer wählen (optional) | Wählen Sie auf dem Bild Lieferantenstamm - Neuer Lieferant auf der Registerkarte Identifikation die Option STEUERNUMMERN. | Sie gelangen zum Bildbereich STEUERNUMMERN. |  |
| 17 | "Anlegen" wählen (optional) | Wählen Sie auf dem Bild Lieferantenstamm - Neuer Lieferantenstamm - STEUERNUMMER ... die Option Anlegen. |  |  |
| 18 | Steuernummerdaten eingeben (optional) | Nehmen Sie im Abschnitt Steuernummern folgende Einträge vor:Steuerkategorie: <Steuerkennzeichen>Steuernummer: <Steuernummer>Hinweis Die Eingabe der Steuernummern ist von länder-/regionsspezifischen Anforderungen abhängig.Wählen Sie die richtige Kategorie für das Land/die Region des Kunden aus. Sie pflegen zum Beispiel für einen deutschen Geschäftspartner einen Wert für die Kategorie DE1, die für die häufig verwendete Umsatzsteuernummer (Umsatzsteuer-Identifikationsnummer) steht.Nehmen Sie nur Einträge für die Felder aus, die Sie benötigen. Anderenfalls wählen Sie Löschen, um den (leeren) Datensatz zu entfernen. |  |  |
| 19 | Zum Hauptbild zurückkehren | Wählen Sie den Pfeil "Zurück".Hinweis Stellen Sie sicher, dass die Meldung Entwurf gesichert im unteren Bildbereich angezeigt wird, bevor Sie zum Hauptbild zurückkehren. |  |  |
| 20 | "Anlegen" wählen | Wählen Sie im Abschnitt Lieferantenstamm - Neuer Lieferant - Steuerkategorien die Option Anlegen. | Das Bild Steuerkategorien wird angezeigt. |  |
| 21 | Steuerkategoriedaten eingeben (optional) | Nehmen Sie folgende Einträge vor:Tax Code: z.B. EWB Erwerb USt.Einzugsermächtigung ab: <Datum>Einzugsermächtigung bis: <Datum> |  |  |
| 22 | Texte eingeben (optional) | Geben Sie auf dem Bild Texte folgende Daten ein:Sprache: z.B. DEID: z.B. 01Langtext: <Geben Sie einen Langtext ein> |  |  |
| 23 | Zusätzliche Lieferdaten eingeben (optional) | Wechseln Sie zu Grunddaten > Zusätzliche Lieferdaten, und wählen Sie Anlegen.Geben Sie wie in den vorangehenden Schritten beschrieben die erforderlichen Daten ein.Hinweis Dieses Szenario dient zu Mehrfachzuordnungen von Lieferanten zu den gleichen Geschäftspartnern, und somit gelten die gleichen Stammdaten, wie in den vorangehenden Schritten beschrieben.Wenn zusätzliche Informationen, wie Verkaufsdaten und Buchungskreis, benötigt werden, finden Sie diese in den vorangehenden Abschnitten. |  |  |
| 24 | Daten sichern | Wählen Sie Anlegen. | Eine Systemmeldung bestätigt, dass das Objekt gesichert wurde. |  |

### Lieferantenstammdaten anlegen - Buchungskreisdaten

Testverwaltung

Kundenprojekt: Füllen Sie die projektbezogenen Teile aus.

|  |  |  |  |
| --- | --- | --- | --- |
| Testfall-ID | <X.XX> | Testdatum: |  |
| Testername: |  | Dauer: |  |
| Benutzerrolle(n): |  | Zuständigkeit: | <Geben Sie den Serviceanbieter, einen Kunden oder einen Serviceanbieter zusammen mit einem Kunden an.> |

Zweck

In diesem Verfahren erhalten Sie eine Anleitung zum Anlegen von Lieferantenstammdaten. Die zur Verfügung stehenden Apps hängen von der Ihnen zugeordneten Rolle ab. Daher werden zwei Optionen bereitgestellt.

Voraussetzung

Sie müssen die vorherige Vorgehensweise ([Lieferantenstammdaten anlegen - Allgemeine Daten](#unique_14) [Seite ] 9) abschließen, bevor Sie mit diesem Abschnitt fortfahren können.

Folgen Sie dieser Vorgehensweise, nachdem Sie die Eingaben zu den allgemeinen Daten, wie im vorherigen Kapitel erläutert, auf dem Bild Organisation anzeigen: <Lieferantenname> vorgenommen und gesichert haben.

Vorgehensweise: Option 1 – Geschäftspartner bearbeiten

Folgen Sie dieser Vorgehensweise, wenn Sie mit Ihrer Benutzerrolle auf die App Geschäftspartner pflegen(BP) zugreifen können.

| Testschrittnummer | Bezeichnung des Testschritts | Anweisungen | Erwartetes Ergebnis | Bestanden/Nicht bestanden/Anmerkung |
| --- | --- | --- | --- | --- |
| 1 | Anmelden | Melden Sie sich am SAP Fiori Launchpad als Stammdatenexperte – Geschäftspartnerdaten an. | Das SAP Fiori Launchpad wird angezeigt. |  |
| 2 | SAP-Fiori-App aufrufen | Öffnen Sie Geschäftspartner pflegen(BP). | Die App wird geöffnet. |  |
| 3 | In den Änderungsmodus wechseln | Wählen Sie Umschalten zwischen Anzeigen und Ändern (F6), um in den Änderungsmodus zu wechseln. |  |  |
| 4 | Geschäftspartnerrolle ändern | Wählen Sie im Feld Ändern in GP-Rolle den folgenden Wert:Lieferant (Finanzbuchhaltung)Hinweis Der technische Schlüssel dieser Geschäftspartnerrolle ist FLVN00. |  |  |
| 5 | Buchungskreisdaten öffnen | Wählen Sie auf dem Bild Buchungskreis. | Das Bild Buchungskreis wird angezeigt. |  |
| 6 | Buchungskreis eingeben | Geben Sie den Buchungskreis ein. z.B. 1010 |  |  |
| Nur für Russland | Kreditorenbuchhaltungsdaten eingeben - Zentrale (nur für Russland) | Wählen Sie auf der Registerkarte Kreditor: Kontoführung im Abschnitt Kontoverwaltung eine der folgenden Optionen ein:163107701 als Zentrale für MwSt-GP 163117701163107701 als Zentrale für MwSt-GP 163117701163107701 als Zentrale für Grundsteuer-GP 163127701163107702 als Zentrale für Grundsteuer-GP 163127702 |  |  |
| 7 | Kreditorenbuchhaltungsdaten eingeben | Geben Sie auf der Registerkarte Kreditor: Kontoführung im Abschnitt Kontoverwaltung die folgenden Daten ein:Abstimmkonto: <21100000> (Verbindlichkeiten Inland)Sortierschlüssel: <Sortierschlüssel>Minderheitenkennzeichen: <Minderheitenkennzeichen> (Die Werte der Minderheitenkennzeichen werden über den Konfigurationsschritt: "Minderheitenkennzeichen definieren" definiert.)Hinweis Es sind unter Umständen weitere Hauptbuch-Abstimmkonten für ausländische Lieferanten oder verbundene Unternehmen vorhanden. |  |  |
| Nur für Japan | Kreditorenbuchhaltungsdaten eingeben - Quellensteuer (nur für Japan) | Wählen Sie auf der Registerkarte Kreditor: Kontoführung im Abschnitt Quellensteuer folgende Daten ein, wenn dieser Lieferant für die Quellensteuer relevant ist:QST-L/R-Schl.: <JP> (Japan) |  |  |
| Nur für Polen | Kreditor erfassen: Quellensteuer (nur für Polen) | Wählen Sie auf der Registerkarte Kreditor: Quellensteuer im Abschnitt Quellensteuertypen Folgendes ein:Ordnen Sie dem Geschäftspartner die Informationen Quellensteuertyp und Quellensteuercode zu.Geben Sie den Befreiungsgrund (DT), den Befreiungsprozentsatz (z.B. 100%), die Befreiungsnummer und den Gültigkeitsbereich für die Quellensteuercodes ein, die für den Doppelbesteuerungsvertrag/die Doppelbesteuerungsvereinbarung relevant sind. |  |  |
| 8 | Kreditorenzahlungsdaten eingeben | Geben Sie auf der Registerkarte Kreditor: Zahlungsverkehr im Abschnitt Zahlungsdaten Folgendes ein:Zahlungsbedingungen: <Zahlungsbedingungen>Hinweis Die in diesem Schritt definierten Zahlungsbedingungen können von den auf Einkaufsebene definierten Zahlungsbedingungen übersteuert werden. |  |  |
| 9 | Kreditorenzahlungsdaten eingeben | Geben Sie auf der Registerkarte Kreditor: Zahlungsverkehr im Abschnitt Automatischer Zahlungsverkehr die folgenden Daten ein:Zahlwege: <Zahlwege>Hausbank: <Hausbank>Hinweis Wählen Sie F4, um die Auswahl im Feld "Zahlwege" zu öffnen. |  |  |
| 10 | Kreditorenkorrespondenzdaten eingeben | Geben Sie auf der Registerkarte Kreditor: Korrespondenz im Abschnitt Korrespondenz die folgenden Daten ein:Konto beim Lieferanten: <Konto beim Kreditor> |  |  |
| Nur für Japan | Quellensteuer (nur für Japan) | Geben Sie auf der Registerkarte Quellensteuer folgende Daten ein, wenn dieser Lieferant für die Quellensteuer relevant ist:Quellensteuerart: <Quellensteuertyp>Quellensteuerkennzeichen: <Quellensteuerkennzeichen>Pflicht: <markiert> |  |  |
| Nur für Japan | Japan: Meine Nummer (nur für Japan) | Wählen Sie Allgemeine Daten. Geben Sie auf der Registerkarte Länderspezif. Erw. folgende Daten ein, wenn der Geschäftspartner keine natürliche Person ist:Unternehmensnummer: <Unternehmensnummer>Geben Sie auf der Registerkarte Länderspezif. Erw. folgende Daten ein, wenn der Lieferant eine natürliche Person ist:Wählen Sie Gültig ab und Gültig bis und dann Anzeigen.Status: <Status>Nachweis f. Identität: <Nachweis f. Identität>Nachweis für Nummer <Nachweis für Nummer>Einbehalt bis: <Einbehalt bis>Wählen Sie Unmaskiert anzeigen, um die Personennummer einzugeben. |  |  |
| Nur für Thailand | Filialcode (nur für Thailand) | Öffnen Sie die allgemeinen Daten, und geben Sie auf der Registerkarte Länderspezif. Erw. die Daten für den Filialschlüssel sowie die Adresse und den Standardfilialschlüssel für diesen Geschäftspartner ein.Für die Adresse des Filialschlüssels wählen Sie Adresse, und geben Sie folgende Daten ein:Name (erste zwei Zeilen): <Name des Steuerzahlers>Land: THGebäudekürzel: <Gebäudename/Dorf>Raum: <Raumnummer>Etage: <Etage>Straße 2: <Moo>Straße 3: <Trok/Soi>Straße: <Straße>Hausnummer: <Nr.>Anderer Ort: <Tumbol/Unterabschnitt>Ortsteil: <Ortsteil/Abschnitt>Ort: <Provinz>Postleitzahl: <Postleitzahl>Telefon: <Telefonnummer>Hinweis Wenn für einen Geschäftspartner mehrere Filialschlüssel vorhanden sind, sollten Sie jeden einzelnen Filialschlüssel zusammen mit der jeweiligen Adresse pflegen. Sie sollten außerdem einen Filialschlüssel, der vom Geschäftspartner allgemein verwendet wird, als Standard festlegen. |  |  |
| Nur für Russland | Steuerzahlungsattribute (nur für Russland) | Geben Sie auf der Registerkarte Länderspezif. Erw. die folgenden Daten für den Geschäftspartner ein.Geben Sie für die Grundsteuer-GP 163107701 und 163107702 die folgenden Werte ein:Zahlungsart: Zahlungen an BudgetStatus des Zahlenden: 01Budget Code: 182 1 06 02010 02 1000 110Geben Sie für den Personalabrechnungs-GP 163107703 den folgenden Wert ein:Zahlungsart: Zahlungen an BudgetGeben Sie für die MwSt-GP 163117701 und 163117702 die folgenden Werte ein:Zahlungsart: Zahlungen an BudgetStatus des Zahlenden: 01Budget Code: 18210301000011000110Geben Sie für die Grundsteuer-GP 163127701 und 163127702 die folgenden Werte ein:Zahlungsart: Zahlungen an BudgetStatus des Zahlenden: 01Budget Code: 18210602010021000110 |  |  |
| Nur für Saudi-Arabien | Kreditor: Länderspez. Erw. (nur für Saudi-Arabien) | Wählen Sie auf der Registerkarte Kreditor: Länderspezif. Erw. die Option Zeile einfügen, um die Lieferantenzertifikate hinzuzufügen. |  |  |
| 11 | Daten sichern | Sichern Sie Ihre Eingaben. | Der Eintrag im Feld Ändern in GP-Rolle ändert sich von Kreditor (Neu) in Kreditor (gepflegt). |  |

Quellensteuerinformationen (nur Brasilien)

Verwenden Sie die folgende Tabelle, um nur für Brasilien die Quellensteuereinträge im vorigen Schritt zu ermitteln.

Für Unternehmensorganisation:

| QuSteuArt | QuSteuKennz. | Thema | Kommentare |
| --- | --- | --- | --- |
| GA | GA | X | für 4,65 % |
| PA | PA | X | nur für PIS |
| CA | CA | X | nur für COFINS |
| SA | SA | X | nur für CSSL |
| EE | EE | X | nur für IRPJ (über TAXBRA) |
| IR | R1 bis R3 | X | nur für IRPJ (über FI) |
| IW | IW | X | für ISS |
| IJ | I1 bis I2 | X | für INSS PJ |

Für natürliche Person:

| QuSteuArt | QuSteuKennz. | Thema | Kommentare |
| --- | --- | --- | --- |
| ID | R0 bis R5 | X | für INSS PF |
| IN | N1 | X | Für INSS PR |

Vorgehensweise: Option 2 – Lieferantenstammdaten verwalten

Folgen Sie dieser Vorgehensweise, wenn Sie mit Ihrer Benutzerrolle auf die App Lieferantenstammdaten verwalten(F1053A) zugreifen können.

| Testschrittnummer | Bezeichnung des Testschritts | Anweisungen | Erwartetes Ergebnis | Kommentare |
| --- | --- | --- | --- | --- |
| 1 | Anmelden | Melden Sie sich am SAP Fiori Launchpad als Stammdatenexperte – Geschäftspartnerdaten an. | Das SAP Fiori Launchpad wird angezeigt. |  |
| 2 | SAP-Fiori-App aufrufen | Öffnen Sie Lieferantenstammdaten verwalten(F1053A). | Die App wird geöffnet. |  |
| 3 | Lieferantendetails eingeben | Wählen Sie aus der Wertehilfe Geschäftspartner aus. Darüber hinaus können Sie weitere Details wie Straßeauswählen.Wählen Sie Start. |  |  |
| 4 | Lieferant auswählen | Wählen Sie einen Lieferanten aus der Ergebnisliste aus. | Das Bild Lieferant wird angezeigt. |  |
| 5 | "Bearbeiten" wählen | Wählen Sie Bearbeiten.Hinweis Dieser Schritt setzt voraus, dass Sie den vorangehenden Schritt ausgeführt haben und bereits zum Bereich Stammdaten - Lieferantenstamm > Lieferantenstamm verwalten navigiert sind. Nachdem Sie Ihre allgemeinen Daten aus dem vorherigen Abschnitt gesichert haben, befindet sich das System im Anzeigemodus. Um fortzufahren, müssen Sie im Bearbeitungsmodus sein. | Das Bild Lieferantenstamm verwalten wird im Bearbeitungsmodus angezeigt (Sie können Daten in die Felder eingeben). |  |
| 6 | Buchungskreise auswählen | Wählen Sie auf dem Bild Lieferanten verwalten die Option Buchungskreise. |  |  |
| 7 | "Anlegen" wählen | Wählen Sie im Bildbereich Buchungskreise die Option Anlegen. | Eine Detailansicht wird im Bearbeitungsmodus angezeigt. |  |
| 8 | Buchungskreisdaten eingeben | Wählen Sie im Abschnitt Buchungskreise einen Eintrag aus, um eine Detailsicht zu öffnen. Tragen Sie Folgendes ein:Auf der Registerkarte Allgemeine Daten:Buchungskreis: Geben Sie den Buchungskreis ein, z.B. 1710.Auf der Registerkarte Korrespondenz:Sachbearbeiter: Beispiel: 01 Frau Schmidt.Konto beim Lieferanten: <Konto beim Lieferanten>Auf der Registerkarte Finanzen :FinanzbuchhaltungAbstimmkonto: z.B. 21100000 – Verbindlichkeiten InlandSortierschlüssel: z.B. 009 Externe Belegnummer.Minderheitengruppe: <Minderheitengruppe> (gilt nur für die Rolle FLVN00 - Lieferant (Finanzbuchhaltung). Die Werte für die Minderheitengruppe werden über den Konfigurationsschritt: Minderheiten-Kennzeichen definieren definiert.)Finanzen - ZahlungsdatenZahlungsbedingungen: z.B. 0001Finanzen – Automatischer ZahlungsverkehrZahlwege: z. B. E LastschriftverfahrenAuf der Registerkarte Mahndaten:Mahnverfahren, Mahnsperre, Mahnempfänger, Mahnsachbearbeiter: Wählen Sie einen Wert aus der Wertehilfe.Mahnstufe: z.B. 0Letzte Mahnung: z.B. 10.02.2020Gerichtliches Mahnverfahren von: z.B. 11.02.2020Auf der Registerkarte Texte:Wählen Sie im Abschnitt Texte die Option Anlegen, und geben Sie folgende Daten ein:Sprache: z.B. DEID: z.B. 01Langtext: <Geben Sie einen Langtext ein> |  |  |
| 9 | Zum Hauptbild zurückkehren | Wählen Sie Anlegen und anschließend Übernehmen.Hinweis Stellen Sie sicher, dass die Meldung Entwurf gesichert im unteren Bildbereich angezeigt wird, bevor Sie zum Hauptbild zurückkehren. |  |  |
| 10 | Daten sichern | Wählen Sie Sichern. | Eine Systemmeldung bestätigt, dass das Objekt gesichert wurde. |  |

### Lieferantenstammdaten anlegen - Einkaufsorganisationsdaten

Testverwaltung

Kundenprojekt: Füllen Sie die projektbezogenen Teile aus.

|  |  |  |  |
| --- | --- | --- | --- |
| Testfall-ID | <X.XX> | Testdatum: |  |
| Testername: |  | Dauer: |  |
| Benutzerrolle(n): |  | Zuständigkeit: | <Geben Sie den Serviceanbieter, einen Kunden oder einen Serviceanbieter zusammen mit einem Kunden an.> |

Zweck

In diesem Verfahren erhalten Sie eine Anleitung zum Anlegen von Lieferantenstammdaten. Die zur Verfügung stehenden Apps hängen von der Ihnen zugeordneten Rolle ab. Daher werden zwei Optionen bereitgestellt.

Voraussetzung

Sie müssen die vorherige Vorgehensweise ([Lieferantenstammdaten anlegen - Allgemeine Daten](#unique_14) [Seite ] 9) abschließen, bevor Sie mit diesem Abschnitt fortfahren können.

Folgen Sie dieser Vorgehensweise, nachdem Sie die Eingaben zu den allgemeinen Daten, wie im vorherigen Kapitel erläutert, auf dem Bild Organisation anzeigen: <Lieferantenname> vorgenommen und gesichert haben.

Vorgehensweise: Option 1 – Geschäftspartner bearbeiten

Folgen Sie dieser Vorgehensweise, wenn Sie mit Ihrer Benutzerrolle auf die App Geschäftspartner pflegen(BP) zugreifen können.

| Testschrittnummer | Bezeichnung des Testschritts | Anweisungen | Erwartetes Ergebnis | Kommentare |
| --- | --- | --- | --- | --- |
| 1 | Anmelden | Melden Sie sich am SAP Fiori Launchpad als Stammdatenexperte – Geschäftspartnerdaten an. | Das SAP Fiori Launchpad wird angezeigt. |  |
| 2 | SAP-Fiori-App aufrufen | Öffnen Sie Geschäftspartner pflegen(BP). | Die App wird geöffnet. |  |
| 3 | In den Änderungsmodus wechseln | Wählen Sie Umschalten zwischen Anzeigen und Ändern (F6), um in den Änderungsmodus zu wechseln. |  |  |
| 4 | Geschäftspartnerrolle ändern | Wählen Sie im Feld Ändern in GP-Rolle den folgenden Wert:LieferantHinweis Der technische Schlüssel dieser Geschäftspartnerrolle ist FLVN01. |  |  |
| 5 | Einkaufsorganisationsdaten öffnen | Wählen Sie Einkauf auf dem Bild. | Das Bild Einkaufsorganisation wird angezeigt. |  |
| 6 | Einkaufsdaten eingeben | Geben Sie folgende Daten ein, und drücken Sie die Eingabetaste:Einkaufsorganisation: <Einkaufsorganisation> |  |  |
| 7 | Einkaufsdaten eingeben | Geben Sie auf der Registerkarte Einkaufsdaten im Abschnitt Konditionen folgende Daten ein:Bestellwährung: <Bestellwährung>Zahlungsbedingungen: <Zahlungsbedingungen> |  |  |
| 8 | Einkaufsdaten eingeben | Geben Sie auf der Registerkarte Einkaufsdaten im Abschnitt Steuerungsdaten die folgenden Daten ein:Versandbedingungen: <Versandbedingungen>Wareneingangsbezogene Rechnungsprüfung: <WE-basierte Rechnungsprüfung> |  |  |
| 9 | Einkaufsdaten eingeben | Geben Sie auf der Registerkarte Einkaufsdaten im Abschnitt Vorschlagswerte Material die folgenden Daten ein:Einkäufergruppe: <Einkäufergruppe>Planlieferzeit: <Planlieferzeit> |  |  |
| 10 | Partnerfunktionsdaten | Prüfen Sie auf der Registerkarte Partnerrollen im Abschnitt Partnerrollen, ob der Eintrag LF (VN bei Anmeldesprache EN) vorhanden ist. |  |  |
| 11 | Daten sichern | Sichern Sie Ihre Eingaben. |  |  |

Vorgehensweise: Option 2 – Lieferantenstamm

Folgen Sie dieser Vorgehensweise, wenn Sie mit Ihrer Benutzerrolle auf die App Lieferantenstammdaten verwalten(F1053A) zugreifen können.

| Testschrittnummer | Bezeichnung des Testschritts | Anweisungen | Erwartetes Ergebnis | Kommentare |
| --- | --- | --- | --- | --- |
| 1 | Anmelden | Melden Sie sich am SAP Fiori Launchpad als Stammdatenexperte – Geschäftspartnerdaten an. | Das SAP Fiori Launchpad wird angezeigt. |  |
| 2 | SAP-Fiori-App aufrufen | Öffnen Sie Lieferantenstammdaten verwalten(F1053A). | Die App wird geöffnet. |  |
| 3 | "Bearbeiten" wählen | Wählen Sie Bearbeiten.Hinweis Dieser Schritt setzt voraus, dass Sie den vorangehenden Schritt ausgeführt haben und bereits zum Bereich Stammdaten – Lieferantenstamm > Lieferantenstamm navigiert sind. Nachdem Sie Ihre Daten aus dem vorherigen Abschnitt gesichert haben, befindet sich das System im Anzeigemodus. Um fortzufahren, müssen Sie im Bearbeitungsmodus sein. | Das Bild Lieferantenstamm wird im Bearbeitungsmodus angezeigt (Sie können Daten in die Felder eingeben). |  |
| 4 | Einkaufsorganisationen auswählen | Wählen Sie im Standardbild Lieferantenstamm … die Option EINKAUFSORGANISATIONEN. | Der Abschnitt Lieferantenstamm - EINKAUF wird angezeigt. |  |
| 5 | "Anlegen" wählen | Wählen Sie im Abschnitt Lieferantenstamm - EINKAUF die Option Anlegen. | Das Bild Neue Einkaufsorganisation … wird im Bearbeitungsmodus angezeigt. |  |
| 6 | Einkaufsorganisationsdaten eingeben | Geben Sie auf dem Bild Neue Einkaufsorganisation folgende Daten ein:Auf der Registerkarte Allgemeine Daten:Einkaufsorganisation: <Code der Einkaufsorganisation>Einkäufergruppe: z.B. 001Auf der Registerkarte EINKAUF:Für die Spalte Bedingungen:Bestellwährung: <Währungscode>Mindestbestellwert: <Mindestbestellwert>Zahlungsbedingungen: z.B. 0001Preisdatumssteuerung: z.B. <aktuelles Datum>Für die Spalte Steuerungsdaten:Versandbedingungen: z.B. 01Automatische Bestellung: <Automatische Bestellung>Wareneingangsbezogene Rechnungsprüfung (Ankreuzfeld) |  |  |
| 7 | Partnerfunktionsdaten | Hinweis Einige Partnerrollen sind gemäß der Anpassung für ausgewählte Kontengruppen und Einkaufsorganisationen vordefiniert.Um weitere Partnerrollen hinzuzufügen, wählen Sie auf der Registerkarte Partnerrollen die Option Anlegen. Folgende Funktionen stehen Ihnen zur Verfügung:VN - LieferantGS - RechnungsstellerMN - Herstellerwerk |  |  |
| 8 | Einkaufsorganisationsdetails eingeben | Wählen Sie auf der Registerkarte Text die Option Anlegen, und geben Sie die Details der Einkaufsorganisation ein. |  |  |
| 9 | Zum Hauptbild zurückkehren | Wählen Sie Übernehmen.Hinweis Stellen Sie sicher, dass die Meldung Entwurf gesichert im unteren Bildbereich angezeigt wird, bevor Sie zum Hauptbild zurückkehren. |  |  |
| 10 | Daten sichern | Wählen Sie Sichern. | Eine Systemmeldung bestätigt, dass das Objekt gesichert wurde. |  |

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
> Flagged while digesting this document, not verified: Text says FLVN01 (supplier with purchasing data) is used in 'Verkauf' (sales), which seems inconsistent with its purchasing use elsewhere in the document.

> [!warning] Conflict
> Flagged while digesting this document, not verified: Reconciliation account is described as a G/L account from the 'Debitorennebenbuch' (customer subledger) although it is for suppliers (21100000 Verbindlichkeiten Inland).

## Connections
- part-of :: [[_cluster]]
- related-to :: [[02-business-partner-and-product-master-data/master-data-script-create-supplier-master-mds-bne-sap-s-4hana-cloud-pu]]
- related-to :: [[02-business-partner-and-product-master-data/mds-bne-591]]
- related-to :: [[02-business-partner-and-product-master-data/sap-s-4hana-cloud-public-edition-mds-bne-589]]
- related-to :: [[02-business-partner-and-product-master-data/script-de-dados-mestre-criar-mestre-de-fornecedores-mds-bne-590]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/BNE_S4CLD2608_Master_Data_DE_XX.docx` — full document · extracted with `mammoth` · 44,959 chars in the whole document
