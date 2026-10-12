---
id: 12-production-and-manufacturing/stammdatenskript-fertigungshilfsmittel-anlegen-sds-5cp-436
title: Stammdatenskript - Fertigungshilfsmittel anlegen - SDS (5CP) (5CP_S4CLD2608_Master_Data_DE_XX)
description: "German master data script (5CP) for SAP S/4HANA Cloud 2608: creating production resources/tools (FHM) of four types and assigning them to routings and production orders."
cluster: 12-production-and-manufacturing
tags: [kb/production-and-manufacturing, topic/production-resources-tools]
aliases: [5CP_S4CLD2608_Master_Data_DE_XX]
keywords: [Production Resources/Tools (PRTs), production resources tools, material prt, other prt, document prt, equipment prt, routing assignment, production order assignment, prt status, prt control key]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/5CP_S4CLD2608_Master_Data_DE_XX.docx]
confidence: low
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-436
topic: 12-production-and-manufacturing/production-resources-tools
language: DE
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Stammdatenskript - Fertigungshilfsmittel anlegen - SDS (5CP) (5CP_S4CLD2608_Master_Data_DE_XX)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/5CP_S4CLD2608_Master_Data_DE_XX.docx`, extracted with `mammoth`. Grouped under **Production Resources/Tools (PRTs)** in Production and Manufacturing. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

| <!-- image omitted: unnamed --> | StammdatenskriptSAP S/4HANA Cloud Public Edition - 02-07-26 |
| --- | --- |
|  | Fertigungshilfsmittel anlegen – SDS (5CP) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Inhaltsverzeichnis

[1 Zweck 2](#_Toc233889783)

[2 Voraussetzungen 3](#_Toc233889784)

[2.1 Systemzugriff 3](#_Toc233889785)

[2.2 Rollen 3](#_Toc233889786)

[2.3 Erforderliche Organisationseinheiten 4](#_Toc233889787)

[2.4 Obligatorische und optionale Stammdaten 4](#_Toc233889788)

[2.5 Wesentliche Parameter für die Datenerstellung 4](#_Toc233889789)

[2.5.1 FHM-Status 4](#_Toc233889790)

[2.5.2 FHM-Steuerschlüssel 5](#_Toc233889791)

[3 Übersichtstabelle 6](#_Toc233889792)

[4 Vorgehensweisen 7](#_Toc233889793)

[4.1 Fertigungshilfsmittel anlegen 7](#_Toc233889794)

[4.1.1 Material-FHM anlegen 7](#_Toc233889795)

[4.1.2 Sonstiges FHM anlegen 8](#_Toc233889796)

[4.1.3 Dokument-FHM anlegen 9](#_Toc233889797)

[4.1.4 Equipment-FHM anlegen 10](#_Toc233889798)

[4.2 FHM in Arbeitsplan zuordnen (optional) 12](#_Toc233889799)

[4.3 FHM in Fertigungsauftrag zuordnen (optional) 13](#_Toc233889800)

[5 Anhang 16](#_Toc233889801)

## Zweck

Dieses Dokument beschreibt, wie Sie einen Fertigungshilfsmittel-Stammdatensatz für Ihr SAP S/4HANA Cloud Private Edition-System anlegen. Im Gegensatz zu Maschinen und Anlagen sind FHM (Fertigungshilfsmittel) bewegliche (nicht stationäre) Einsatzmittel, die zur Durchführung einer Aktivität benötigt werden und wiederholt eingesetzt werden können.

Es stehen mehrere Arten von Fertigungshilfsmitteln zur Verfügung. Die Art bestimmt die Merkmale und Business Functions, die ein FHM haben kann.

Sie können Ihr eigenes FHM gemäß der Anweisung dieses Stammdatenskripts anlegen.

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
| Produktionsingenieur – diskrete Fertigung | SAP_BR_PRODN_ENG_DISC | Fertigungstechnik - diskrete Fertigung | SAP_BR_PRODN_ENG_DISC |  |
| Fertigungssteuerer – Diskrete Fertigung | SAP_BR_PRODN_SUPERVISOR_DISC | Produktionsverwaltung - Diskrete Fertigung | SAP_BR_PRODN_SUPERVISOR_DISC |  |
| Stammdatenexperte – Produktdaten | SAP_BR_PRODMASTER_SPECIALIST | Stammdaten – Produkte / Produkt-Governance | SAP_BR_PRODMASTER_SPECIALIST / SAP_CMD_SPT_PR_GOV_PC |  |
| Konstrukteur | SAP_BR_DESIGN_ENGINEER | Dokumentenverwaltung | SAP_BR_DESIGN_ENGINEER |  |
| Instandhaltungsplaner | SAP_BR_MAINTENANCE_PLANNER | Instandhaltungsplanung | SAP_BR_MAINTENANCE_PLANNER |  |

### Erforderliche Organisationseinheiten

Einige Segmente von Materialstammdaten hängen von den Organisationseinheiten des Unternehmens ab. Allgemeine (zentrale) Daten hängen nicht von einer Organisationseinheit oder dem Buchungskreis ab. Die folgende Tabelle stellt eine Übersicht dieser verschiedenen Datensegmente und ihrer relevanten Organisationseinheiten bereit:

| Datensegment | Hängt ab von | Feldbeispiele | Kommentare | Zu verwendende Organisationseinheit |
| --- | --- | --- | --- | --- |
| Alle Daten | Werk |  | Alle Daten hängen vom Werk ab. | Werk:____________ |

### Obligatorische und optionale Stammdaten

Referenz-Arbeitsplandatensätze können auf andere Stammdaten verweisen. Die folgende Tabelle stellt eine Übersicht optionaler und obligatorischer Stammdatenobjekte für die Verwendung in einem Referenzarbeitsplan bereit.

| Stammdatenobjekt | Verwendet im Datensegment | Obligatorisch / optional | Kommentare |
| --- | --- | --- | --- |
| Arbeitsplan | FHM in Arbeitsplan zuordnen | optional | Wir nehmen an, Sie haben einen Arbeitsplan und möchten diesem ein FHM zuordnen. |

### Wesentliche Parameter für die Datenerstellung

In diesem Abschnitt werden einige Basisparameter erläutert, die das Verhalten eines Stammsatzes beeinflussen und zum Anlegen eines Fertigungshilfsmittel-Stammdatensatzes immer erforderlich sind.

#### FHM-Status

Der FHM-Status steuert die Verwendung von Fertigungshilfsmitteln. Je nach Status kann ein Fertigungshilfsmittel in der FHM-Pflege für verschiedene Aufgaben freigegeben werden.

| FHM-Status | Beschreibung |
| --- | --- |
| 01 | Angelegt am |
| 02 | Frei für Einsatzplanung |
| 03 | Frei für Produktion |

#### FHM-Steuerschlüssel

Der FHM-Steuerschlüssel legt fest, ob die Fertigungshilfsmittel einem Plan oder einem Auftrag zugeordnet sind. Sie sind in den folgenden Business Functions enthalten:

| FHM-Steuerungsprofil | Beschreibung |
| --- | --- |
| 1 | Alle Funktionen |
| 2 | Drucken |

## Übersichtstabelle

Dieser Umfangsbestandteil umfasst die verschiedenen Prozessschritte in der folgenden Tabelle:

|  |
| --- |
| Hinweis Wenn Ihr Systemadministrator Bereiche und Seiten auf dem SAP Fiori Launchpad aktiviert hat, enthält die Startseite nur die wesentlichen Apps, mit denen die typischen Aufgaben einer Benutzerrolle ausgeführt werden können.Alle anderen (suchbaren) Apps, die nicht auf der Startseite enthalten sind, finden Sie über die Suchleiste ([2434549](https://me.sap.com/notes/2434549)).Wenn Sie die Startseite personalisieren und versteckte Apps hinzufügen möchten, wechseln Sie in Ihr Benutzerprofil und wählen Sie App Finder. |

| Prozessschritt | Anwendungsrolle | Transaktion/App | Erwartete Ergebnisse |
| --- | --- | --- | --- |
| [Material-FHM anlegen](#unique_11) [Seite ] 7 | Stammdatenexperte – Produktdaten | Material anlegen(MM01) |  |
| [Sonstiges FHM anlegen](#unique_12) [Seite ] 8 | Produktionsingenieur – diskrete Fertigung | Fertigungshilfsmittel verwalten(F7653) |  |
| [Dokument-FHM anlegen](#unique_13) [Seite ] 9 | Konstrukteur | Belege verwalten(F2733) |  |
| [Equipment-FHM anlegen](#unique_14) [Seite ] 10 | Instandhaltungsplaner | Technisches Objekt anlegen(W0029) |  |
| [FHM in Arbeitsplan zuordnen (optional)](#unique_15) [Seite ] 12 | Produktionsingenieur – diskrete Fertigung | Arbeitsplan ändern(CA02) |  |
| [FHM in Fertigungsauftrag zuordnen (optional)](#unique_16) [Seite ] 13 | Fertigungssteuerer – Diskrete Fertigung | Fertigungsauftrag ändern(CO02) |  |

## Vorgehensweisen

Dieser Abschnitt beschreibt die Vorgehensweisen für jedes Segment oder Prozessschritt, das bzw. der Teil dieses Stammsatzes ist.

### Fertigungshilfsmittel anlegen

#### Material-FHM anlegen

Testverwaltung

Kundenprojekt: Füllen Sie die projektbezogenen Teile aus.

|  |  |  |  |
| --- | --- | --- | --- |
| Testfall-ID | <X.XX> | Testdatum: |  |
| Testername: |  | Dauer: |  |
| Benutzerrolle(n): |  | Zuständigkeit: | <Geben Sie den Serviceanbieter, einen Kunden oder einen Serviceanbieter zusammen mit einem Kunden an.> |

Verwendungszweck

In diesem Kapitel erfahren Sie, wie Sie ein Material-FHM anlegen.

Vorgehensweise

| Testschrittnummer | Bezeichnung des Testschritts | Anweisung | Erwartetes Ergebnis | Kommentare |
| --- | --- | --- | --- | --- |
| 1 | Anmeldung | Melden Sie sich als Stammdatenexperte – Produktdaten am SAP Fiori Launchpad an. | Die Startseite wird angezeigt. |  |
| 2 | SAP-Fiori-App öffnen | Öffnen Sie die App Material anlegen(MM01). | Es öffnet sich ein neues Fenster, das Material anlegen (Einstieg) anzeigt. |  |
| 3 | Materialgrunddaten eingeben | Nehmen Sie auf dem Bild Material anlegen (Einstieg), die folgenden Einträge vor:Material: <Materialnummer>, z.B. FHM_01Materialart: FertigungshilfsmittelWählen Sie Sichtenauswahl. | Die Sicht Sichtenauswahl wird angezeigt. |  |
| 4 | Sichten wählen | Wählen Sie im Bild Sichtenauswahl die Sicht:GrundsichtFertigungshilfsmittelWeitere notwendige SichtenWählen Sie Weiter. |  |  |
| 5 | Organisationsebenendaten eingeben | Nehmen Sie in der Sicht Organisationsebenen im Bereich Organisationsebenen die folgenden Einträge vor:Werk: <Nummer des Werks>, z.B. 1010,Drücken Sie die Eingabetaste. |  |  |
| 6 | Daten in Grundsicht eingeben | Geben Sie auf der Registerkarte Grunddaten 1 die folgenden Daten ein:Beschreibung: <Fertige Montage FHM>Basismengeneinheit: <ST>Wählen Sie die Registerkarte Fertigungshilfsmittel. | Die Grunddaten werden gesichert. |  |
| 7 | Daten von Fertigungshilfsmitteln erfassen | Geben Sie auf der Registerkarte Fertigungshilfsmittel folgende Daten ein:FHM-Einsatz: <009>FHM Steuerungsprofil: <1>Wählen Sie Sichern. | Sie kehren zum Einstiegsbild zurück.Die Materialnummer PRT_01 wird angelegt. |  |

#### Sonstiges FHM anlegen

Testverwaltung

Kundenprojekt: Füllen Sie die projektbezogenen Teile aus.

|  |  |  |  |
| --- | --- | --- | --- |
| Testfall-ID | <X.XX> | Testdatum: |  |
| Testername: |  | Dauer: |  |
| Benutzerrolle(n): |  | Zuständigkeit: | <Geben Sie den Serviceanbieter, einen Kunden oder einen Serviceanbieter zusammen mit einem Kunden an.> |

Zweck

In diesem Kapitel erfahren Sie, wie Sie ein sonstiges FHM anlegen.

Vorgehensweise

| Testschrittnummer | Bezeichnung des Testschritts | Anweisung | Erwartetes Ergebnis | Kommentare |
| --- | --- | --- | --- | --- |
| 1 | Anmeldung | Melden Sie sich am SAP Fiori Launchpad als Produktionsingenieur – diskrete Fertigung an. | Das SAP Fiori Launchpad wird angezeigt. |  |
| 2 | SAP-Fiori-App aufrufen | Öffnen Sie Fertigungshilfsmittel verwalten(F7653). | Die App wird geöffnet. |  |
| 3 | "Anlegen" wählen | Wählen Sie Anlegen. | Ein neues Fenster mit dem Bild FHM anlegen wird angezeigt. |  |
| 4 | Namen eingeben | Nehmen Sie folgende Einträge vor:Fertigungshilfsmittel: <Name>, z.B. PRT_02Wählen Sie Grundaten. | Das Bild Fertigungshilfsmittel anlegen: Grunddaten wird angezeigt. |  |
| 5 | Grunddaten eingeben | Geben Sie eine Beschreibung für das von Ihnen angelegte FHM ein:Suchen Sie nach der Quick-Info Bezeichnung des Fertigungshilfsmittels, und geben Sie Folgendes ein: <Sonstiges FHM 02>Geben Sie im Bereich Grunddaten folgende Daten ein:Status: <03>FHM-Einsatz: <009>Basismengeneinheit: <ST>Wählen Sie Sichern. | Sie kehren zum Einstiegsbild zurück.Das Fertigungshilfsmittel wird angelegt. |  |

#### Dokument-FHM anlegen

Testverwaltung

Kundenprojekt: Füllen Sie die projektbezogenen Teile aus.

|  |  |  |  |
| --- | --- | --- | --- |
| Testfall-ID | <X.XX> | Testdatum: |  |
| Testername: |  | Dauer: |  |
| Benutzerrolle(n): |  | Zuständigkeit: | <Geben Sie den Serviceanbieter, einen Kunden oder einen Serviceanbieter zusammen mit einem Kunden an.> |

Verwendungszweck

In diesem Kapitel erfahren Sie, wie Sie ein Dokument-FHM anlegen.

Vorgehensweise

| Testschrittnummer | Bezeichnung des Testschritts | Anweisung | Erwartetes Ergebnis | Kommentare |
| --- | --- | --- | --- | --- |
| 1 | Anmeldung | Melden Sie sich als Konstrukteur am SAP Fiori Launchpad an. | Die Startseite wird angezeigt. |  |
| 2 | SAP-Fiori-App öffnen | Öffnen Sie die App Belege verwalten(F2733). | In einem neuen Fenster wird das Bild Dokumente verwalten angezeigt. |  |
| 3 | Dokument anlegen | Wählen Sie Anlegen.Geben Sie auf dem Bild Dokument folgende Daten ein:Dokumentart: <SPP>Dokumentenbeschreibung: <PRT_03>Wählen Sie Anlegen. | Das Dokument wird angelegt.Notieren Sie die Dokumentnummer. |  |
| 4 | Dokument bearbeiten | Wählen Sie oben rechts die Option Bearbeiten.Setzen Sie auf der Registerkarte Dokumentdaten das Feld Dokumentstatus auf In Arbeit.Wählen Sie im Abschnitt Originale die Option Hochladen, und hängen Sie dann ein FHM-Dokument von Ihrem PC an.Wählen Sie Sichern. | Das Dokument wird gesichert. |  |
| 5 | Dokument freigeben | Wählen Sie oben rechts die Option Bearbeiten.Ändern Sie im Abschnitt Dokumentdaten den Dokumentstatus in Freigegeben.Wählen Sie Sichern. | Das Dokument wird gesichert. |  |

#### Equipment-FHM anlegen

Testverwaltung

Kundenprojekt: Füllen Sie die projektbezogenen Teile aus.

|  |  |  |  |
| --- | --- | --- | --- |
| Testfall-ID | <X.XX> | Testdatum: |  |
| Testername: |  | Dauer: |  |
| Benutzerrolle(n): |  | Zuständigkeit: | <Geben Sie den Serviceanbieter, einen Kunden oder einen Serviceanbieter zusammen mit einem Kunden an.> |

Zweck

In diesem Kapitel erfahren Sie, wie Sie ein Equipment-FHM anlegen.

Vorgehensweise

| Testschrittnummer | Bezeichnung des Testschritts | Anweisung | Erwartetes Ergebnis | Bestanden/Nicht bestanden/Anmerkung |
| --- | --- | --- | --- | --- |
| 1 | Anmelden | Melden Sie sich am SAP Fiori Launchpad als Instandhaltungsplaner an. | Das SAP Fiori Launchpad wird angezeigt. |  |
| 2 | SAP-Fiori-App aufrufen | Öffnen Sie Technisches Objekt anlegen(W0029). | Die App wird geöffnet. |  |
| 3 | Equipment anlegen | Wählen Sie auf dem Bild Technisches Objekt anlegen die Option Art des technischen Objekts: Equipment.Geben Sie im nächsten Bild folgende Daten ein:Art des technischen Objekts: EquipmentTechnisches Objekt: leer lassenGültig ab: aktuelles DatumTyp des technischen Objekts: F (Fertigungshilfsmittel)Wählen Sie Weiter. |  |  |
| 4 | Allgemeine Daten bearbeiten | Geben Sie auf dem Bild Technisches Objekt anlegen: <Equipment-ID> im Abschnitt Allgemeine Daten folgende Daten ein:Beschreibung: <z.B. Materialien, Equipments>Optional können Sie weitere allgemeine Daten pflegen. Navigieren Sie dann zum Abschnitt FHM-Daten. | Das Bild Technisches Objekt anlegen: Allgemeine Daten wird angezeigt. |  |
| 5 | FHM-Daten pflegen | Geben Sie im Abschnitt FHM-Daten folgende Daten ein:Planverwendung: 009 (Alle Plantypen)Steuerschlüssel: 1 (Alle Funktionen)Optional können Sie weitere Details pflegen. Sie können beispielsweise einen Messpunkt anlegen, dem einige Merkmale zugeordnet sind, den Messpunkt dann im Feld Messpunkt anhängen und das Ankreuzfeld für das Feld Bedarfssätze markieren. | Das Bild Technisches Objekt anlegen: Standortdaten wird angezeigt. |  |
| 6 | Equipment sichern | Optional können Sie zusätzliche Informationen für andere Abschnitte pflegen.Wählen Sie Sichern. | Ein Equipment wird angelegt. Notieren Sie sich die Equipmentnummer. |  |

### FHM in Arbeitsplan zuordnen (optional)

Testverwaltung

Kundenprojekt: Füllen Sie die projektbezogenen Teile aus.

|  |  |  |  |
| --- | --- | --- | --- |
| Testfall-ID | <X.XX> | Testdatum: |  |
| Testername: |  | Dauer: |  |
| Benutzerrolle(n): |  | Zuständigkeit: | <Geben Sie den Serviceanbieter, einen Kunden oder einen Serviceanbieter zusammen mit einem Kunden an.> |

Verwendungszweck

In diesem Kapitel erfahren Sie, wie Sie ein Material-FHM, ein sonstiges FHM, ein Dokument-FHM oder ein Equipment-FHM in einem Arbeitsplan zuordnen. Sie können den Plänen und Fertigungsaufträgen, für die sie benötigt werden, verschiedene Arten von Fertigungshilfsmitteln zuordnen. FHMs, die dem Plan zugeordnet sind, werden automatisch in den Fertigungsauftrag kopiert.

Vorgehensweise

| Testschrittnummer | Bezeichnung des Testschritts | Anweisung | Erwartetes Ergebnis | Kommentare |
| --- | --- | --- | --- | --- |
| 1 | Anmeldung | Melden Sie sich als Produktionsingenieur – diskrete Fertigung am SAP Fiori Launchpad an. | Die Startseite wird angezeigt. |  |
| 2 | SAP-Fiori-App öffnen | Öffnen Sie die App Arbeitsplan ändern(CA02). | Es öffnet sich ein neues Fenster, dass das Bild Arbeitsplan ändern: Einstieg anzeigt. |  |
| 3 | Material eingeben | Geben Sie folgende Daten ein, und wählen Sie Weiter:Material: <Materialnummer>Werk: <Nummer des Werks>, z.B. 1010, | Das Bild Arbeitsplan ändern: Vorgangsübersicht wird angezeigt. |  |
| 4 | Vorgang wählen | Markieren Sie eine Position, und wählen Sie dann Vorgänge.Wählen Sie einen Vorgang aus, dem Sie das FHM zuordnen möchten. Wählen Sie anschließend FHM. | Das Bild Arbeitsplan ändern: Das Bild FHM-Übersicht wird angezeigt. |  |
| 5 | Material-FHM zuordnen | Wenn im Vorgang kein FHM vorhanden ist, geben Sie im Dialogfenster folgende Daten ein: Arbeitsplan ändern: Neues FHM.Wenn bereits vorhanden, wählen Sie Material, geben Sie folgende Daten ein, und wählen Sie das grüne Häkchen:FHM-Positionsnummer: <0010>Material: <Materialnummer>, z.B. PRT_01Werk: <Nummer des Werks>, z.B. 1010, | Das Material-FHM ist dem Vorgang zugeordnet. |  |
| 6 | Sonstiges FHM zuordnen | Wählen Sie Sonstiges, geben Sie folgende Daten ein, und wählen Sie das grüne Häkchen:FHM-Positionsnummer: <0020>Fertigungshilfsmittel: <Name>, z.B. FHM_02 | Dem Vorgang ist ein sonstiges FHM zugeordnet. |  |
| 7 | Dokument-FHM zuordnen | Wählen Sie Dokument, geben Sie folgende Daten ein, und wählen Sie das grüne Häkchen:FHM-Positionsnummer: <0030>Dokument: <Im vorherigen Schritt angelegte Belegnummer>Dokumentart: <SPP>Teildokument: <000>Dokumentversion: <00>Menge: <1 ST>SteuProfil: <1> | Das Dokument-FHM ist dem Vorgang zugeordnet. |  |
| 8 | Equipment-FHM zuordnen | Wählen Sie Equipment, geben Sie folgende Daten ein, und wählen Sie das grüne Häkchen:Equipment: <Im vorherigen Schritt angelegte Equipmentnummer> |  |  |
| 9 | Änderungen sichern | Wählen Sie Sichern. | Der Arbeitsplan wird gesichert. |  |

### FHM in Fertigungsauftrag zuordnen (optional)

Testverwaltung

Kundenprojekt: Füllen Sie die projektbezogenen Teile aus.

|  |  |  |  |
| --- | --- | --- | --- |
| Testfall-ID | <X.XX> | Testdatum: |  |
| Testername: |  | Dauer: |  |
| Benutzerrolle(n): |  | Zuständigkeit: | <Geben Sie den Serviceanbieter, einen Kunden oder einen Serviceanbieter zusammen mit einem Kunden an.> |

Verwendungszweck

In diesem Kapitel erfahren Sie, wie Sie einem Vorgang in einem Fertigungsauftrag ein Material-FHM, ein sonstiges FHM, ein Dokument-FHM oder ein Equipment-FHM zuordnen. Stellen Sie sicher, dass zuvor ein Fertigungsauftrag angelegt wurde. Sie können FHMs auch während des Anlegens des Auftrags auf der Registerkarte "Vorgangsübersicht" zuordnen.

Vorgehensweise

| Testschrittnummer | Bezeichnung des Testschritts | Anweisung | Erwartetes Ergebnis | Kommentare |
| --- | --- | --- | --- | --- |
| 1 | Anmeldung | Melden Sie sich als Fertigungssteuerer – Diskrete Fertigung am SAP Fiori Launchpad an. | Die Startseite wird angezeigt. |  |
| 2 | SAP-Fiori-App aufrufen | Öffnen Sie Fertigungsauftrag ändern(CO02) | Ein neues Fenster wird geöffnet, in dem das Bild Fertigungsauftrag ändern: Einstieg angezeigt wird. |  |
| 3 | Auftragsdaten eingeben | Nehmen Sie folgende Einträge vor, und wählen Sie Weiter:Auftrag: <Auftragsnummer> | Das Bild Fertigungsauftrag anlegen: Ändern wird angezeigt. |  |
| 4 | Vorgang auswählen | Wählen Sie Vorgänge.Markieren Sie in der Tabelle Vorgangsübersicht das Ankreuzfeld für einen Vorgang, z.B. Vorgang 0010, und wählen Sie FHM. | Das neue Dialogfenster Fertigungsauftrag ändern: FHM Neue Einträge wird angezeigt, wenn im Vorgang kein FHM vorhanden ist.Falls bereit ein FHM vorhanden ist, wird die Tabelle Fertigungshilfsmittel Übersicht angezeigt. |  |
| 5 | Material-FHM zuordnen | Wenn in dem Vorgang kein FHM vorhanden ist, geben Sie im Dialogfenster Fertigungsauftrag ändern: FHM Neue Einträge folgende Daten ein:Wenn bereits ein FHM vorhanden ist, wählen Sie das Pluszeichen + unten in Fertigungshilfsmittel Übersicht und geben Sie folgende Daten ein:Steuernummer: z.B. 0010Material: z.B. PRT_01Werk: z.B. 1010Wählen Sie das grüne Häkchen. | Das Material-FHM ist dem Vorgang zugeordnet. |  |
| 6 | Sonstiges FHM zuordnen | Wählen Sie das Pluszeichen + unten in Fertigungshilfsmittel Übersicht und wählen Sie Sonstige. Geben Sie dann folgende Daten ein:Steuernummer: z.B. 0020FHM, z.B. FHM_02Wählen Sie das grüne Häkchen. | Dem Vorgang ist ein sonstiges FHM zugeordnet. |  |
| 7 | Dokument-FHM zuordnen | Wählen Sie das Pluszeichen + unten in der Fertigungshilfsmittel Übersicht und wählen Sie Dokument. Geben Sie dann folgende Daten ein:Positionsnummer: <0030>Dokument: <Im vorherigen Schritt angelegte Belegnummer>Dokumentart: <SPP>Teildokument: <000>Dokumentversion: <00>Menge: <1 ST>Steuerschlüssel: <1>Wählen Sie das grüne Häkchen. | Das Dokument-FHM ist dem Vorgang zugeordnet. |  |
| 8 | Equipment-FHM zuordnen | Wählen Sie das Pluszeichen + unten in der Fertigungshilfsmittel Übersicht und wählen Sie Equipment. Geben Sie dann folgende Daten ein:Equipment: <Im vorherigen Schritt angelegte Equipmentnummer>Steuerungsprofil: 1 (Alle Funktionen)Wählen Sie das grüne Häkchen. |  |  |

## Anhang

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
> Flagged while digesting this document, not verified: Purpose section says the system is SAP S/4HANA Cloud Private Edition, while the title/footers and role links refer to Public Edition.

> [!warning] Conflict
> Flagged while digesting this document, not verified: Material FHM example number is FHM_01 but the expected result says material number PRT_01 is created; later steps use PRT_01.

## Connections
- part-of :: [[_cluster]]
- related-to :: [[12-production-and-manufacturing/master-data-script-create-production-resources-tools-mds-5cp-437]]
- related-to :: [[12-production-and-manufacturing/master-data-script-mds-5cp-japanese-439]]
- related-to :: [[12-production-and-manufacturing/mds-5cp-441]]
- related-to :: [[12-production-and-manufacturing/script-de-dados-mestre-criar-meio-auxiliar-de-producao-mds-5cp-440]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/5CP_S4CLD2608_Master_Data_DE_XX.docx` — full document · extracted with `mammoth` · 23,612 chars in the whole document
