---
id: 10-procurement/einkaufsinfosatz-anlegen-sds-bhd-stammdatenskript-562
title: Einkaufsinfosatz anlegen – SDS (BHD) Stammdatenskript (BHD_S4CLD2608_Master_Data_DE_XX)
description: "German SAP S/4HANA Cloud master data script for creating purchasing info records (standard, consignment, subcontracting, pipeline) and mass changes."
cluster: 10-procurement
tags: [kb/procurement, topic/purchasing-info-records]
aliases: [BHD_S4CLD2608_Master_Data_DE_XX]
keywords: [Purchasing Info Records, consignment info record, subcontracting info record, pipeline info record, mass changes, price mass changes, master data scripts, number ranges, business roles, tax code]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/BHD_S4CLD2608_Master_Data_DE_XX.docx]
confidence: high
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-562
topic: 10-procurement/purchasing-info-records
language: DE
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Einkaufsinfosatz anlegen – SDS (BHD) Stammdatenskript (BHD_S4CLD2608_Master_Data_DE_XX)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/BHD_S4CLD2608_Master_Data_DE_XX.docx`, extracted with `mammoth`. Grouped under **Purchasing Info Records** in Procurement. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

| <!-- image omitted: unnamed --> | StammdatenskriptSAP S/4HANA Cloud Public Edition - 02-07-26 |
| --- | --- |
|  | Einkaufsinfosatz anlegen – SDS (BHD) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Inhaltsverzeichnis

[1 Verwendungszweck 2](#_Toc233889913)

[2 Voraussetzungen 3](#_Toc233889914)

[2.1 Systemzugriff 3](#_Toc233889915)

[2.2 Rollen 3](#_Toc233889916)

[2.3 Erforderliche Organisationseinheiten 3](#_Toc233889917)

[2.4 Obligatorische und optionale Stammdaten 4](#_Toc233889918)

[2.5 Wesentliche Parameter für die Datenerstellung 4](#_Toc233889919)

[2.5.1 Nummernkreise 4](#_Toc233889920)

[3 Übersichtstabelle 5](#_Toc233889921)

[4 Testverfahren 6](#_Toc233889922)

[4.1 Einkaufsinfosatz anlegen 6](#_Toc233889923)

[4.2 Einkaufsinfosatz für Konsignation anlegen 8](#_Toc233889924)

[4.3 Einkaufsinfosatz für Lohnbearbeitung anlegen 10](#_Toc233889925)

[4.4 Einkaufsinfosatz für Pipeline anlegen 12](#_Toc233889926)

[4.5 Massenänderungen an Einkaufsinfosatz 15](#_Toc233889927)

[4.6 Massenänderungen von Preisen an Einkaufsinfosatz 16](#_Toc233889928)

[5 Anhang 18](#_Toc233889929)

[5.1 Relevante Funktionen 18](#_Toc233889930)

## Verwendungszweck

Ein Einkaufsinfosatz enthält Informationen zu einem bestimmten Material und zu dem das Material bereitstellenden Lieferanten.

Er enthält Informationen wie z.B. den Preis des Lieferanten, die Normalbestellmenge sowie Toleranzen für Über- und Unterlieferung. Er wird in der Bestelltransaktion verwendet.

Die Informationen beziehen sich auf eine bestimmte Einkaufsabteilung (bekannt als Einkaufsorganisation) und eine bestimmte Produktionsstätte (bekannt als Werk) Ihres Unternehmens.

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
| Einkäufer | SAP_BR_PURCHASER | Einkauf / Ausschreibungen und Kontrakte | SAP_MM_SPT_PURCHASING_PC / SAP_MM_SPT_SOURCING_PC |  |

### Erforderliche Organisationseinheiten

Die Organisationsstruktur und die Stammdaten Ihres Unternehmens wurden bei der Implementierung in Ihrem ERP-System angelegt. Die Organisationsstruktur gibt den Aufbau Ihres Unternehmens wieder. Die folgende Tabelle stellt eine Übersicht dieser verschiedenen Datensegmente und ihrer relevanten Organisationseinheiten bereit:

| Datensegment | Hängt ab von | Feldbeispiele | Kommentare | Zu verwendende Organisationseinheit |
| --- | --- | --- | --- | --- |
| Einkaufsdaten | Einkaufsorganisation | Einkäufergruppe, Materialgruppe, WE-Bearbeitungszeit usw. | Einkaufsdaten können für jede Einkaufsorganisation existieren, für die das Material in den Einkaufsvorgängen verwendet wird. | Einkaufsorganisation:__________ |

### Obligatorische und optionale Stammdaten

Einkaufsinfosätze können auf andere Stammdaten verweisen. Die folgende Tabelle bietet eine Übersicht über die optionalen und obligatorischen Stammdatenobjekte, die in einem Einkaufsinfosatz verwendet werden müssen.

| Stammdatenobjekt | Verwendet im Datensegment | Obligatorisch / optional | Kommentare |
| --- | --- | --- | --- |
| Material |  | Obligatorisch | Um das Material einzugeben, legen Sie zuerst Materialstammdaten an. |
| Lieferant |  | Obligatorisch | Um den Lieferanten einzugeben, legen Sie zuerst Lieferantenstammdaten an. |

### Wesentliche Parameter für die Datenerstellung

Dieser Abschnitt bietet eine Beschreibung der Basisparameter, die das Verhalten eines Einkaufsinfosatzes beeinflussen und bei jedem Anlegen eines Einkaufsinfosatzes erforderlich sind.

#### Nummernkreise

Die folgenden Nummernkreise sind für Einkaufsinfosätze definiert:

| Nummernkreis | Bereich / Geschäftspartner-ID | Kommentare |
| --- | --- | --- |
| Intern numerisch | Interner nummerischer Nummernkreis für Standardverwendung:5300000000 – 5399999999 | Dieser Nummernkreis wird verwendet, wenn das System einem Material automatisch eine numerische Nummer zuordnet. |
| Externer numerischer Nummernkreis | Externer numerischer Nummernkreis (hoch):5400000000 – 5499999999 | Dieser Nummernkreis ist für die externe numerische Nummernvergabe reserviert. |

## Übersichtstabelle

|  |
| --- |
| Hinweis Wenn Ihr Systemadministrator Bereiche und Seiten auf dem SAP Fiori Launchpad aktiviert hat, enthält die Startseite nur die wesentlichen Apps, mit denen die typischen Aufgaben einer Benutzerrolle ausgeführt werden können.Alle anderen (suchbaren) Apps, die nicht auf der Startseite enthalten sind, finden Sie über die Suchleiste ([2434549](https://me.sap.com/notes/2434549)).Wenn Sie die Startseite personalisieren und versteckte Apps hinzufügen möchten, wechseln Sie in Ihr Benutzerprofil und wählen Sie App Finder. |

| Prozessschritt | Benutzerrolle | App/Transaktion | Erwartete Ergebnisse |
| --- | --- | --- | --- |
| [Einkaufsinfosatz anlegen](#unique_10) [Seite ] 6 | Einkäufer | Einkaufsinfosätze verwalten(F1982) | Die Einkaufsinfosätze werden angelegt. |
| [Einkaufsinfosatz für Konsignation anlegen](#unique_11) [Seite ] 8 | Einkäufer | Einkaufsinfosätze verwalten(F1982) | Der Einkaufsinfosatz für die Konsignation wird angelegt. |
| [Einkaufsinfosatz für Lohnbearbeitung anlegen](#unique_12) [Seite ] 10 | Einkäufer | Einkaufsinfosätze verwalten(F1982) | Der Einkaufsinfosatz für die Lohnbearbeitung wird angelegt. |
| [Einkaufsinfosatz für Pipeline anlegen](#unique_13) [Seite ] 12 | Einkäufer | Einkaufsinfosätze verwalten(F1982) | Der Einkaufsinfosatz für die Pipeline wird angelegt. |
| [Massenänderungen an Einkaufsinfosatz](#unique_14) [Seite ] 15 | Einkäufer | Massenänderungen an Einkaufsinfosätzen(F2667) | Massenänderungen am Einkaufsinfosatz kommen zur Anwendung. |
| [Massenänderungen von Preisen an Einkaufsinfosatz](#unique_15) [Seite ] 16 | Einkäufer | Preisänderungen: Infosätze | Massenpreisänderungen am Einkaufsinfosatz werden angewendet. |

## Testverfahren

In diesem Abschnitt werden die Testverfahren für den jeweiligen Prozessschritt beschrieben, der zum betreffenden Umfangsbestandteil gehört.

### Einkaufsinfosatz anlegen

Testverwaltung

Kundenprojekt: Füllen Sie die projektbezogenen Teile aus.

|  |  |  |  |
| --- | --- | --- | --- |
| Testfall-ID | <X.XX> | Testdatum: |  |
| Testername: |  | Dauer: |  |
| Benutzerrolle(n): |  | Zuständigkeit: | <Geben Sie den Serviceanbieter, einen Kunden oder einen Serviceanbieter zusammen mit einem Kunden an.> |

Vorgehensweise

| Testschrittnummer | Bezeichnung des Testschritts | Anweisung | Erwartetes Ergebnis | Kommentare |
| --- | --- | --- | --- | --- |
| 1 | Anmelden | Melden Sie sich am SAP Fiori Launchpad als Einkäufer an. | Das SAP Fiori Launchpad wird angezeigt. |  |
| 2 | SAP-Fiori-App aufrufen | Öffnen Sie Einkaufsinfosätze verwalten(F1982). | Das Bild Einkaufsinfosätze verwalten(F1982) wird angezeigt. |  |
| 3 | Neuen Einkaufsinfosatz öffnen | Wählen Sie Anlegen. | Das Bild Einkaufsinfosatz wird angezeigt. |  |
| 4 | Kopfdaten eingeben | Machen Sie folgende Eingaben:Typ des Einkaufsinfosatzes: <Standard>Einkaufsorganisation: <Einkaufsorganisation>Lieferant: <Lieferant>Material: <Material>Werk: <Werk>Einkäufergruppe: <Einkäufergruppe> | Die Kopfdaten werden hinzugefügt. |  |
| 5 | Allgemeine Informationen eingeben | Nehmen Sie folgende Einträge vor:Verfügbar ab: MM/TT/JJJJVerfügbar bis: MM/TT/JJJJ | Allgemeine Informationen werden hinzugefügt. |  |
| 6 | Einkaufsdaten eingeben | Geben Sie folgende Daten ein:Incoterm: <Incoterm>Incoterm-Ort 1: <Incoterm-Standort1> | Einkaufsdaten werden hinzugefügt. |  |
| 7 | Liefer- und Mengendaten eingeben | Nehmen Sie folgende Eingaben vor:Lieferzeit in Tagen: <XX Tage>Unterlieferungstoleranz in %: <XX>Überlieferungstoleranz in %: <XX>Steuerkennzeichen: <Steuerkennzeichen>Hinweis Wenn die zeitabhängige Steuer über den Konfigurationsschritt 101016 (Umsatzsteuerkennzeichen definieren) für das Land des Buchungskreises aktiviert wird und das Steuerkennzeichen angegeben wird, ist das Feld "Steuersatz gültig ab" obligatorisch. Sie können das aktuelle Datum eingeben, das an den Gültigkeitsbeginn des Steuerkennzeichens gemäß der Einstellung in dem Konfigurationsschritt angepasst wird.Wenn die URA (Umsatzsteuerliche Registrierung im Ausland) aktiviert ist, das Steuerregistrierungsland für den Buchungskreis im Konfigurationsschritt 103464 (URA aktivieren und Steuerregistrierungsländer pflegen) und das Steuerkennzeichen angegeben ist, ist das Feld "Steuerland", in dem die Länder-ID des Buchungskreises als Standardwert angegeben ist, obligatorisch. Sie können jedoch zu der gültigen Länder-ID wechseln, die entsprechend in dem Konfigurationsschritt gepflegt ist.Hinweis Abhängig von Ihrer Konfigurationsumgebung können Sie auf die Konfigurationsschritte unter Lösung konfigurieren im SAP Fiori Launchpad oder in der App Business Processes Configuration in der Projekterfahrung von SAP Central Business Configuration zugreifen.Bestellmengeneinheit: Bestellmengeneinheit:Normalbestellmenge: <Normalbestellmenge>Wählen Sie bei Bedarf folgende Einträge:Unbegrenzte LieferungWareneingangsbezogene RechnungsprüfungKeine automatische WareneingangsabrechnungAuftragsbestätigungspflichtBestätigungssteuerung | Liefer- und Mengendaten werden hinzugefügt. |  |
| 8 | Konditionsdaten eingeben | Wählen Sie im Abschnitt Konditionen das Symbol Anlegen. Geben Sie folgende Daten ein:Gültig ab: <Gültigkeitsbeginn>Betrag: <Betrag>Preiseinheit: <Preiseinheit>Gültig bis: <Gültigkeitsende>Währung: <Währung>Wählen Sie Übernehmen. | Die Konditionsdaten werden hinzugefügt. |  |
| 9 | Referenzdaten eingeben (optional) | Sie haben die Möglichkeit, Referenzdaten einzugeben. | Die Referenzdaten werden hinzugefügt. |  |
| 10 | Daten sichern | Wählen Sie Anlegen. | Es wird ein Einkaufsinfosatz gesichert. |  |

### Einkaufsinfosatz für Konsignation anlegen

Testverwaltung

Kundenprojekt: Füllen Sie die projektbezogenen Teile aus.

|  |  |  |  |
| --- | --- | --- | --- |
| Testfall-ID | <X.XX> | Testdatum: |  |
| Testername: |  | Dauer: |  |
| Benutzerrolle(n): |  | Zuständigkeit: | <Geben Sie den Serviceanbieter, einen Kunden oder einen Serviceanbieter zusammen mit einem Kunden an.> |

Vorgehensweise

| Testschrittnummer | Bezeichnung des Testschritts | Anweisung | Erwartetes Ergebnis | Kommentare |
| --- | --- | --- | --- | --- |
| 1 | Anmelden | Melden Sie sich am SAP Fiori Launchpad als Einkäufer an. | Das SAP Fiori Launchpad wird angezeigt. |  |
| 2 | SAP-Fiori-App aufrufen | Öffnen Sie Einkaufsinfosätze verwalten(F1982). | Das Bild "Einkaufsinfosätze verwalten" wird angezeigt. |  |
| 3 | Neuen Einkaufsinfosatz öffnen | Wählen Sie Anlegen. | Das Bild "Einkaufsinfosatz" wird angezeigt |  |
| 4 | Kopfdaten eingeben | Machen Sie folgende Eingaben:Typ des Einkaufsinfosatzes: <Konsignation>Einkaufsorganisation: <Einkaufsorganisation>Lieferant: <Lieferant>Material: <Material>Werk: <Werk>:Einkäufergruppe: <Einkäufergruppe> | Die Kopfdaten werden hinzugefügt. |  |
| 5 | Allgemeine Informationen eingeben | Nehmen Sie folgende Einträge vor:Verfügbar ab: MM/TT/JJJJVerfügbar bis: MM/TT/JJJJ | Die Allgemeinen Informationen werden hinzugefügt. |  |
| 6 | Einkaufsdaten eingeben | Nehmen Sie folgende Einträge vor:Incoterm: <Incoterm>Incoterm Standort 1: <Incoterm-Standort1> | Die Einkaufsdaten werden hinzugefügt. |  |
| 7 | Liefer- und Mengendaten eingeben | Geben Sie folgende Daten ein:Lieferzeit in Tagen: <XX Tage>Unterlieferungstoleranz in %: <XX>Überlieferungstoleranz in %: <XX>Steuerkennzeichen: <Steuerkennzeichen>Hinweis Wenn die zeitabhängige Steuer über den Konfigurationsschritt 101016 (Umsatzsteuerkennzeichen definieren) für das Land des Buchungskreises aktiviert wird und das Steuerkennzeichen angegeben wird, ist das Feld "Steuersatz gültig ab" obligatorisch. Sie können das aktuelle Datum eingeben, das an den Gültigkeitsbeginn des Steuerkennzeichens gemäß der Einstellung in dem Konfigurationsschritt angepasst wird.Wenn URA (Umsatzsteuerliche Registrierung im Ausland) aktiviert ist, das Steuerregistrierungsland für den Buchungskreis im Konfigurationsschritt 103464 (URA aktivieren und Steuerregistrierungsländer pflegen) angegeben ist und das Steuerkennzeichen ebenfalls, ist das Feld "Steuerland" obligatorisch, in dem die Länder-ID des Buchungskreises als Standardwert angegeben ist. Sie können jedoch in die gültige Länder-ID wechseln, die in dem Konfigurationsschritt entsprechend gepflegt ist.Hinweis Abhängig von Ihrer Konfigurationsumgebung können Sie auf die Konfigurationsschritte unter Lösung konfigurieren im SAP Fiori Launchpad oder in der App Business Processes Configuration in der Projekterfahrung von SAP Central Business Configuration zugreifen.Bestellmengeneinheit: Bestellmengeneinheit:Normalbestellmenge: <Normalbestellmenge> | Liefer- und Mengendaten werden hinzugefügt. |  |
| 8 | Konditionsdaten eingeben | Wählen Sie im Abschnitt Konditionen das Symbol Anlegen. Geben Sie folgende Daten ein:Gültig ab: <Gültigkeitsbeginn>Betrag: <Betrag>Preiseinheit: <Preiseinheit>Gültig bis: <Gültigkeitsende>:Währung: <Währung>Wählen Sie Übernehmen. | Die Konditionsdaten werden hinzugefügt. |  |
| 9 | Referenzdaten eingeben (optional) | Sie haben die Möglichkeit, Referenzdaten einzugeben. | Die Referenzdaten werden hinzugefügt. |  |
| 10 | Daten sichern | Wählen Sie Anlegen. | Es wird ein Einkaufsinfosatz gesichert. |  |

### Einkaufsinfosatz für Lohnbearbeitung anlegen

Testverwaltung

Kundenprojekt: Füllen Sie die projektbezogenen Teile aus.

|  |  |  |  |
| --- | --- | --- | --- |
| Testfall-ID | <X.XX> | Testdatum: |  |
| Testername: |  | Dauer: |  |
| Benutzerrolle(n): |  | Zuständigkeit: | <Geben Sie den Serviceanbieter, einen Kunden oder einen Serviceanbieter zusammen mit einem Kunden an.> |

Vorgehensweise

| Testschrittnummer | Bezeichnung des Testschritts | Anweisung | Erwartetes Ergebnis | Kommentare |
| --- | --- | --- | --- | --- |
| 1 | Anmelden | Melden Sie sich am SAP Fiori Launchpad als Einkäufer an. | Das SAP Fiori Launchpad wird angezeigt. |  |
| 2 | SAP-Fiori-App aufrufen | Öffnen Sie Einkaufsinfosätze verwalten(F1982). | Das Bild "Einkaufsinfosätze verwalten" (F1982) wird angezeigt |  |
| 3 | Neuen Einkaufsinfosatz öffnen | Wählen Sie Anlegen. | Das Bild "Einkaufsinfosatz" wird angezeigt |  |
| 4 | Kopfdaten eingeben | Machen Sie folgende Eingaben:Typ des Einkaufsinfosatzes: <Lohnbearbeitung>Einkaufsorganisation: <Einkaufsorganisation>Lieferant: <Lieferant>Material: <Material>Werk: <Werk>:Einkäufergruppe: <Einkäufergruppe> | Die Kopfdaten werden hinzugefügt. |  |
| 5 | Allgemeine Informationen eingeben | Nehmen Sie folgende Einträge vor:Verfügbar ab: MM/TT/JJJJVerfügbar bis: MM/TT/JJJJ | Die Allgemeinen Informationen werden hinzugefügt. |  |
| 6 | Liefer- und Mengendaten eingeben | Geben Sie folgende Daten ein:Lieferzeit in Tagen: <XX Tage>Unterlieferungstoleranz in %: <XX>Überlieferungstoleranz in %: <XX>Steuerkennzeichen: <Steuerkennzeichen>Hinweis Wenn die zeitabhängige Steuer über den Konfigurationsschritt 101016 (Umsatzsteuerkennzeichen definieren) für das Land des Buchungskreises aktiviert wird und das Steuerkennzeichen angegeben wird, ist das Feld "Steuersatz gültig ab" obligatorisch. Sie können das aktuelle Datum eingeben, das an den Gültigkeitsbeginn des Steuerkennzeichens gemäß der Einstellung in dem Konfigurationsschritt angepasst wird.Wenn die URA (Umsatzsteuerliche Registrierung im Ausland) aktiviert ist, das Steuerregistrierungsland für den Buchungskreis im Konfigurationsschritt 103464 (URA aktivieren und Steuerregistrierungsländer pflegen) und das Steuerkennzeichen angegeben ist, ist das Feld "Steuerland", in dem die Länder-ID des Buchungskreises als Standardwert angegeben ist, obligatorisch. Sie können jedoch zu der gültigen Länder-ID wechseln, die entsprechend in dem Konfigurationsschritt gepflegt ist.Hinweis Abhängig von Ihrer Konfigurationsumgebung können Sie auf die Konfigurationsschritte unter Lösung konfigurieren im SAP Fiori Launchpad oder in der App Business Processes Configuration in der Projekterfahrung von SAP Central Business Configuration zugreifen.Bestellmengeneinheit: Bestellmengeneinheit:Normalbestellmenge: <Normalbestellmenge> | Liefer- und Mengendaten werden hinzugefügt. |  |
| 7 | Konditionsdaten eingeben | Wählen Sie im Abschnitt Konditionen das Symbol Anlegen. Geben Sie folgende Daten ein:Gültig ab: <Gültigkeitsbeginn>Betrag: <Betrag>Preiseinheit: <Preiseinheit>Gültig bis: <Gültigkeitsende>:Währung: <Währung>:Wählen Sie Übernehmen. | Konditionsdaten werden hinzugefügt. |  |
| 8 | Referenzdaten eingeben (optional) | Sie haben die Möglichkeit, Referenzdaten einzugeben. | Die Referenzdaten werden hinzugefügt. |  |
| 9 | Daten sichern | Wählen Sie Anlegen. | Es wird ein Einkaufsinfosatz gesichert. |  |

### Einkaufsinfosatz für Pipeline anlegen

Testverwaltung

Kundenprojekt: Füllen Sie die projektbezogenen Teile aus.

|  |  |  |  |
| --- | --- | --- | --- |
| Testfall-ID | <X.XX> | Testdatum: |  |
| Testername: |  | Dauer: |  |
| Benutzerrolle(n): |  | Zuständigkeit: | <Geben Sie den Serviceanbieter, einen Kunden oder einen Serviceanbieter zusammen mit einem Kunden an.> |

Vorgehensweise

| Testschrittnummer | Bezeichnung des Testschritts | Anweisung | Erwartetes Ergebnis | Kommentare |
| --- | --- | --- | --- | --- |
| 1 | Anmelden | Melden Sie sich am SAP Fiori Launchpad als Einkäufer an. | Das SAP Fiori Launchpad wird angezeigt. |  |
| 2 | SAP-Fiori-App aufrufen | Öffnen Sie Einkaufsinfosätze verwalten(F1982). | Die App wird geöffnet. |  |
| 3 | Neuen Einkaufsinfosatz öffnen | Wählen Sie Anlegen. | Das Bild Einkaufsinfosatz wird angezeigt. |  |
| 4 | Kopfdaten eingeben | Machen Sie folgende Eingaben:Typ des Einkaufsinfosatzes: <Pipeline>Einkaufsorganisation: <Einkaufsorganisation>Lieferant: <Lieferant>Material: <Pipelinematerial>Werk: <Werk>Einkäufergruppe: <Einkäufergruppe>Warengruppe: <Warengruppe> | Die Kopfdaten werden hinzugefügt. |  |
| 5 | Allgemeine Informationen eingeben | Geben Sie Folgendes ein:Verfügbar ab: MM/TT/JJJJVerfügbar bis: MM/TT/JJJJ | Die allgemeinen Informationen werden hinzugefügt. |  |
| 6 | Einkaufsdaten eingeben | Geben Sie folgende Daten ein:Incoterm: <Incoterm>Incoterm-Ort 1: <Incoterm-Ort 1> | Die Einkaufsdaten werden hinzugefügt. |  |
| 7 | Liefer- und Mengendaten eingeben | Nehmen Sie folgende Eingaben vor:Lieferzeit in Tagen: <XX Tage>Unterlieferungstoleranz in %: <XX>Überlieferungstoleranz in %: <XX>Steuerkennzeichen: <Steuerkennzeichen>Hinweis Wenn die zeitabhängige Steuer über den Konfigurationsschritt 101016 (Umsatzsteuerkennzeichen definieren) für das Land des Buchungskreises aktiviert wird und das Steuerkennzeichen angegeben wird, ist das Feld "Steuersatz gültig ab" obligatorisch. Sie können das aktuelle Datum eingeben, das an den Gültigkeitsbeginn des Steuerkennzeichens gemäß der Einstellung in dem Konfigurationsschritt angepasst wird.Wenn die URA (Umsatzsteuerliche Registrierung im Ausland) aktiviert ist, das Steuerregistrierungsland für den Buchungskreis im Konfigurationsschritt 103464 (URA aktivieren und Steuerregistrierungsländer pflegen) und das Steuerkennzeichen angegeben ist, ist das Feld "Steuerland", in dem die Länder-ID des Buchungskreises als Standardwert angegeben ist, obligatorisch. Sie können jedoch zu der gültigen Länder-ID wechseln, die entsprechend in dem Konfigurationsschritt gepflegt ist.Hinweis Abhängig von Ihrer Konfigurationsumgebung können Sie auf die Konfigurationsschritte unter Lösung konfigurieren im SAP Fiori Launchpad oder in der App Business Processes Configuration in der Projekterfahrung von SAP Central Business Configuration zugreifen.Bestellmengeneinheit: <Bestellmengeneinheit>Normalbestellmenge: <Normalbestellmenge>Wählen Sie bei Bedarf folgende Einträge:Unbegrenzte LieferungWareneingangsbezogene RechnungsprüfungKeine automatische WareneingangsabrechnungAuftragsbestätigungspflichtBestätigungssteuerung | Liefer- und Mengendaten werden hinzugefügt. |  |
| 8 | Konditionsdaten eingeben | Wählen Sie im Abschnitt Kondition die Option Anlegen. Geben Sie folgende Daten ein:Gültig ab: <gültig ab Datum>Betrag: <Betrag>Preiseinheit: <Preiseinheit>Gültig bis: <Gültig-bis-Datum>Währung: <Währung>Wählen Sie Übernehmen. | Konditionsdaten werden hinzugefügt. |  |
| 9 | Referenzdaten eingeben (optional) | Sie haben die Möglichkeit, Referenzdaten einzugeben. | Die Referenzdaten werden hinzugefügt. |  |
| 10 | Daten sichern | Wählen Sie Anlegen. | Es wird ein Einkaufsinfosatz gesichert. |  |

### Massenänderungen an Einkaufsinfosatz

Testverwaltung

Kundenprojekt: Füllen Sie die projektbezogenen Teile aus.

|  |  |  |  |
| --- | --- | --- | --- |
| Testfall-ID | <X.XX> | Testdatum: |  |
| Testername: |  | Dauer: |  |
| Benutzerrolle(n): |  | Zuständigkeit: | <Geben Sie den Serviceanbieter, einen Kunden oder einen Serviceanbieter zusammen mit einem Kunden an.> |

Zweck

In diesem Verfahren übernehmen Sie Änderungen für mehrere ausgewählte Einkaufsinfosätze in einem Schritt.

Vorgehensweise

| Testschrittnummer | Bezeichnung des Testschritts | Anweisung | Erwartetes Ergebnis | Bestanden/Nicht bestanden/Anmerkung |
| --- | --- | --- | --- | --- |
| 1. | Anmelden | Melden Sie sich am SAP Fiori Launchpad als Einkäufer an. | Das SAP Fiori Launchpad wird angezeigt. |  |
| 2 | SAP-Fiori-App aufrufen | Öffnen Sie Massenänderungen an Einkaufsinfosätzen(F2667). | Die App wird geöffnet. |  |
| 3 | Einkaufsinfosätze suchen | Geben Sie für die Suche nach Einkaufsinfosätzen die folgenden Werte zum Filtern ein:Lieferant: <Lieferanten-ID>Einkäufergruppe: z.B. 001Werk: <Werks-ID>Wählen Sie Start. | In den Suchergebnissen werden die Details der entsprechenden Filterkriterien angezeigt.Für Massenänderungsvorgänge werden standardmäßig alle Einkaufsinfosätze ausgewählt. |  |
| 4 | Einkaufsinfosätze auswählen | Wählen Sie das Ankreuzfeld Einkaufsinfosätze auf der Registerkarte Einkaufsinfosätze und Einkaufsorganisation.Wählen Sie Massenbearbeitung. |  |  |
| 5 | Neue Werte festlegen | Geben Sie neue Werte für Folgendes ein:Im Bereich Allgemeine Daten:LieferantenmaterialnummerWarengruppe LieferantIm Abschnitt Einkaufsorganisationsdaten :EinkäufergruppeMindestauftragsmengeWählen Sie Massenänderungen übernehmen.Es wird ein Dialogfenster zur Bestätigung der Massenänderungen angezeigt.Auf dem Bild Massenänderungen übernehmen wählen Sie Übernehmen.Es wird ein Dialogfenster mit der Job-ID angezeigt.Wählen Sie Jobliste anzeigen. | Die neuen Werte werden auf die ausgewählten Einkaufsinfosätze angewendet. |  |
| 6 | Anwendungsjobs prüfen | Geben Sie die Suchkriterien ein, und wählen Sie "Start".Das Bild Anwendungsjobs wird mit der Liste der Job-IDs für alle Einkaufsinfosätze angezeigt.Wählen Sie Protokoll, um zu prüfen, ob Ihre ausgewählten Einkaufsinfosätze erfolgreich waren. |  |  |

### Massenänderungen von Preisen an Einkaufsinfosatz

Testverwaltung

Kundenprojekt: Füllen Sie die projektbezogenen Teile aus.

|  |  |  |  |
| --- | --- | --- | --- |
| Testfall-ID | <X.XX> | Testdatum: |  |
| Testername: |  | Dauer: |  |
| Benutzerrolle(n): |  | Zuständigkeit: | <Geben Sie den Serviceanbieter, einen Kunden oder einen Serviceanbieter zusammen mit einem Kunden an.> |

Zweck

In dieser Vorgehensweise wird die App Preisänderung: Infosätze(MEKP) verwendet, um eine Massenaktualisierung der Preise für Infosätze vorzunehmen.

Vorgehensweise

| Testschrittnummer | Bezeichnung des Testschritts | Anweisung | Erwartetes Ergebnis | Bestanden/Nicht bestanden/Anmerkung |
| --- | --- | --- | --- | --- |
| 1 | Anmelden | Melden Sie sich am SAP Fiori Launchpad als Einkäufer an. | Das SAP Fiori Launchpad wird angezeigt. |  |
| 2 | SAP-Fiori-App aufrufen | Öffnen Sie Preisänderung: Infosätze(MEKP). | Die App wird geöffnet. |  |
| 3 | Ausgangsdaten eingeben | Geben Sie Folgendes ein, und wählen Sie Ausführen:Einkaufsorganisation: <Einkaufsorganisation-ID>Lieferant: <Lieferanten-ID>Material: Material-ID:Infosätze ohne Material: <leer>Testlauf: <leer>Navigieren Sie zum Abschnitt Konditionsart oder Bruttopreis ändern, und geben Sie folgende Daten ein:Konditionsart: <Konditionsart-ID> z.B. PPR0Absolutbetrag: <Absolutbetrag> z.B. 10Vorzeichen: <Vorzeichen> beispielsweise +Bruttopreis: <leer>Staffelzeilen: <X>Navigieren Sie zum Abschnitt Konditionen gültig, und geben Sie folgende Daten ein:Am: <Aktuelles Datum>oder Von <leer> Bis <leer> | Die neuen Werte werden für die Einkaufsinfosätze gepflegt. |  |
| 4 | Änderungen an Einkaufsinfosätzen prüfen | Prüfen Sie auf dem Bild Preisänderung für Infosätze des Lieferanten <XXXX> die alten und neuen Sätze, und bestätigen Sie die Änderungen. | Die Preisänderungen an den Einkaufsinfosätzen werden gesichert. |  |
| 5 | Beenden | Wählen Sie Beenden. |  |  |

## Anhang

### Relevante Funktionen

Hier sind einige wichtige Anwendungsfunktionen für den Einkaufsinfosatz aufgelistet, die in den oben genannten Testverfahren nicht abgedeckt sind.

| Funktionsbereich | Funktion | Detailinformationen | Anmerkung |
| --- | --- | --- | --- |
| Einkaufsinfosätze | Infosatzbezogene Apps | WebGUI: Einkaufsinfosatz löschen (ME15)WebGUI: Einkaufsinfosatz nach Lieferant anzeigen (ME1L)WebGUI: Massenänderungen an Einkaufsinfosätzen (ME14)WebGUI: Einkaufskonditionen pflegen (MEKA)WebGUI: Rundungsprofil pflegen (OWD1) |  |

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
- related-to :: [[10-procurement/create-purchasing-info-record-mds-bhd-master-data-script-563]]
- related-to :: [[10-procurement/criar-registro-info-para-compras-mds-bhd-566]]
- related-to :: [[10-procurement/mds-bhd-565]]
- related-to :: [[10-procurement/mds-bhd-567]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/BHD_S4CLD2608_Master_Data_DE_XX.docx` — full document · extracted with `mammoth` · 28,920 chars in the whole document
