---
id: 06-management-accounting/stammdaten-fur-universelle-verrechnung-anlegen-sds-2us-286
title: Stammdaten für universelle Verrechnung anlegen – SDS (2US) (2US_S4CLD2608_Master_Data_DE_XX)
description: "German SAP S/4HANA Cloud Public Edition 2608 master data script: test steps for plan/actual allocation and profit center distribution cycles in app Verrechnungen verwalten (F3338A)."
cluster: 06-management-accounting
tags: [kb/management-accounting, topic/universal-allocation]
aliases: [2US_S4CLD2608_Master_Data_DE_XX]
keywords: [Universal Allocation Cycles, universal allocation, plan allocation cycles, actual allocation cycles, profit center distribution, actual profit center distribution, allocation cycle upload, overhead cost controlling, user roles, master data prerequisites]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/2US_S4CLD2608_Master_Data_DE_XX.docx]
confidence: high
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-286
topic: 06-management-accounting/universal-allocation
language: DE
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Stammdaten für universelle Verrechnung anlegen – SDS (2US) (2US_S4CLD2608_Master_Data_DE_XX)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/2US_S4CLD2608_Master_Data_DE_XX.docx`, extracted with `mammoth`. Grouped under **Universal Allocation Cycles** in Management Accounting. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

| <!-- image omitted: unnamed --> | StammdatenskriptSAP S/4HANA Cloud Public Edition - 02-07-26 |
| --- | --- |
|  | Stammdaten für universelle Verrechnung anlegen – SDS (2US) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Inhaltsverzeichnis

[1 Einsatzmöglichkeiten 2](#_Toc233889576)

[2 Voraussetzungen 3](#_Toc233889577)

[2.1 Systemzugriff 3](#_Toc233889578)

[2.2 Rollen 3](#_Toc233889579)

[2.3 Erforderliche Organisationseinheiten 3](#_Toc233889580)

[2.4 Obligatorische und optionale Stammdaten 4](#_Toc233889581)

[3 Übersichtstabelle 5](#_Toc233889582)

[4 Testverfahren 6](#_Toc233889583)

[4.1 Planverrechnungen 6](#_Toc233889584)

[4.1.1 Planumlagezyklen verwalten 6](#_Toc233889585)

[4.1.2 Planumlagezyklen bearbeiten 8](#_Toc233889586)

[4.2 Istverrechnungen 10](#_Toc233889587)

[4.2.1 Istumlagezyklen verwalten 10](#_Toc233889588)

[4.2.2 Istumlagezyklen bearbeiten 12](#_Toc233889589)

[4.3 Plan-Profitcenter-Verrechnung 14](#_Toc233889590)

[4.3.1 Plan-Profitcenter-Verteilungszyklen verwalten 14](#_Toc233889591)

[4.4 Ist-Profitcenter-Verrechnung 16](#_Toc233889592)

[4.4.1 Ist-Profitcenter-Verteilungszyklen verwalten 16](#_Toc233889593)

## Einsatzmöglichkeiten

Die Universelle Verrechnung umfasst Plan- und Istumlage/-verteilung von Profitcentern im Rahmen des Gemeinkosten-Controllings. Sie verwendet verschiedene Sender/Empfänger-Kombinationen für Beträge, Prozentsätze und Portionen. Diese Stammdaten unterstützen die jährliche Planung durch Neuverteilung der Kosten durch vordefinierte Zuordnungs- und Verteilungszyklen innerhalb eines bestimmten Buchungskreises. Durch die Zuordnung der Kostenelemente zu Kostenstellen im Gemeinkosten-Controlling können Sie Ihre Kosten überwachen und Plan- mit Istkosten vergleichen. Außerdem wird Plan- und Istumlage/-verteilung von Profitcentern von Profitcentern ebenfalls unterstützt.

Dieses Skript enthält einige allgemeine Beispiele für das Anlegen von Stammdaten mit der universellen Verrechnung, aber es kann auch mithilfe verschiedener Sender/Empfänger-Kombinationen für Beträge, Prozentsätze und Portionen an Ihre spezifischen Geschäftsanforderungen angepasst werden.

Dieses Dokument enthält eine detaillierte Ablaufbeschreibung, anhand deren der Umfangsbestandteil nach der Lösungsaktivierung getestet werden kann; außerdem bildet es den vordefinierten Umfang der Lösung ab. Jeder Prozessschritt, Report oder Bestandteil wird in einem eigenen Abschnitt beschrieben, in dem die Interaktionen im System (Testschritte) tabellarisch dargestellt sind. Schritte, die nicht im Prozessumfang enthalten sind, aber zu Testzwecken benötigt werden, sind entsprechend gekennzeichnet. Projektspezifische Schritte sind zu ergänzen.

|  |
| --- |
| Hinweis Die Werte in diesem Testskript (Dezimalschreibweise, Datumsformate usw.) werden in US-amerikanischer Standardschreibweise dargestellt. Wenn Ihr Testsystem so eingerichtet ist, dass es eine andere Schreibweise verwendet, geben Sie die entsprechenden Werte ein. |

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
| Gemeinkostencontroller | SAP_BR_OVERHEAD_ACCOUNTANT | Gemeinkostenrechnung | SAP_BR_OVERHEAD_ACCOUNTANT |  |
| Spartenbuchhalter | SAP_BR_DIVISION_ACCOUNTANT |  |  |  |

### Erforderliche Organisationseinheiten

Die Organisationsstruktur und die Stammdaten Ihres Unternehmens wurden bei der Implementierung in Ihrem ERP-System angelegt. Die Organisationsstruktur gibt den Aufbau Ihres Unternehmens wieder. Die Stammdaten stehen für Kostenstellen und Kostenstellengruppen, je nach betrieblichem Schwerpunkt Ihres Unternehmens.

| Datenobjekt | Verwendet im Datensegment | Obligatorisch / optional | Kommentare |
| --- | --- | --- | --- |
| Kostenrechnungskreis | Allgemeine Daten | obligatorisch |  |
| Buchungskreis | Organisationseinheiten | obligatorisch |  |

### Obligatorische und optionale Stammdaten

Kostenstellen- und Kostenstellengruppen-Stammdatensätze können auf andere Stammdaten verweisen. Die folgende Tabelle stellt eine Übersicht optionaler und obligatorischer Stammdatenobjekte für die Verwendung in der Allokation bereit.

| Stammdatenobjekt | Obligatorisch / optional | Kommentare |
| --- | --- | --- |
| Kostenstelle | obligatorisch |  |
| Kostenart | obligatorisch |  |
| Statistische Kennzahl | Optional |  |
| Profitcenter | obligatorisch |  |

## Übersichtstabelle

Dieser Umfangsbestandteil umfasst verschiedene Prozessschritte, die in der folgenden Tabelle aufgeführt werden:

|  |
| --- |
| Hinweis Wenn Ihr Systemadministrator Bereiche und Seiten auf dem SAP Fiori Launchpad aktiviert hat, enthält die Startseite nur die wesentlichen Apps, mit denen die typischen Aufgaben einer Benutzerrolle ausgeführt werden können.Alle anderen (suchbaren) Apps, die nicht auf der Startseite enthalten sind, finden Sie über die Suchleiste ([2434549](https://me.sap.com/notes/2434549)).Wenn Sie die Startseite personalisieren und versteckte Apps hinzufügen möchten, wechseln Sie in Ihr Benutzerprofil und wählen Sie App Finder. |

Planverrechnungen

| Prozessschritt | Anwendungsrolle | Vorgang/App | Erwartete Ergebnisse |
| --- | --- | --- | --- |
| [Planumlagezyklen verwalten](#unique_8) [Seite ] 6 | Gemeinkostencontroller | Verrechnungen verwalten(F3338A) | Die Kosten werden Kostenstellengruppen, Kostenstellen oder Bereichen zugewiesen. |
| [Planumlagezyklen bearbeiten](#unique_9) [Seite ] 8 | Gemeinkostencontroller | Verrechnungen verwalten(F3338A) | Die Planumlagezyklen werden bearbeitet. |

Istverrechnungen

| Prozessschritt | Anwendungsrolle | Vorgang/App | Erwartete Ergebnisse |
| --- | --- | --- | --- |
| [Istumlagezyklen verwalten](#unique_10) [Seite ] 10 | Gemeinkostencontroller | Verrechnungen verwalten(F3338A) | Die Kosten werden Kostenstellengruppen, Kostenstellen oder Bereichen zugewiesen. |
| [Istumlagezyklen bearbeiten](#unique_11) [Seite ] 12 | Gemeinkostencontroller | Verrechnungen verwalten(F3338A) | Istumlagezyklen werden bearbeitet. |

Plan-Profitcenter-Verrechnung

| Prozessschritt | Anwendungsrolle | Vorgang/App | Erwartete Ergebnisse |
| --- | --- | --- | --- |
| [Plan-Profitcenter-Verteilungszyklen verwalten](#unique_12) [Seite ] 14 | Spartenbuchhalter | Verrechnungen verwalten(F3338A) | Die Plan-Profitcenter-Verteilung wird angelegt. |

Ist-Profitcenter-Verrechnung

| Prozessschritt | Anwendungsrolle | Vorgang/App | Erwartete Ergebnisse |
| --- | --- | --- | --- |
| [Ist-Profitcenter-Verteilungszyklen verwalten](#unique_13) [Seite ] 16 | Spartenbuchhalter | Verrechnungen verwalten(F3338A) | Die Profitcenter-Verteilung wird angelegt. |

## Testverfahren

### Planverrechnungen

#### Planumlagezyklen verwalten

Testverwaltung

Kundenprojekt: Füllen Sie die projektbezogenen Teile aus.

|  |  |  |  |
| --- | --- | --- | --- |
| Testfall-ID | <X.XX> | Testdatum: |  |
| Testername: |  | Dauer: |  |
| Benutzerrolle(n): |  | Zuständigkeit: | <Geben Sie den Serviceanbieter, einen Kunden oder einen Serviceanbieter zusammen mit einem Kunden an.> |

Kontext

In diesem Beispiel verwendet der Planumlagezyklus Sekundärkostenarten, um Kosten einer Kostenstelle oder einer Gruppe von Kostenstellen mit einer anderen Kostenstelle oder Gruppe von Kostenstellen innerhalb eines Buchungskreises zu einem festen Prozentsatz zu verrechnen.

Vorgehensweise

| Testschrittnummer | Bezeichnung des Testschritts | Anweisungen | Erwartetes Ergebnis | Kommentare |
| --- | --- | --- | --- | --- |
| 1 | Anmelden | Melden Sie sich am SAP Fiori Launchpad als Gemeinkostencontroller an. | Das SAP Fiori Launchpad wird angezeigt. |  |
| 2 | SAP-Fiori-App aufrufen | Öffnen Sie Verrechnungen verwalten(F3338A). | Die Sicht Verrechnungen verwalten wird angezeigt. |  |
| 3 | Zykluskopf anlegen | Wählen Sie die Drucktaste Anlegen und dann Neuen Zyklus anlegen. | Das Dialogfenster Neuen Zyklus anlegen wird angezeigt.Hinweis Der Massen-Upload von Allokationszyklen ist für das Anlegen neuer Allokationen und/oder neuer Segmente über die App Verrechnungen verwalten über die Drucktaste Vorlage hochladen/herunterladen möglich. Sie können entweder eine leere Vorlage herunterladen oder einen vorhandenen Allokationszyklus auswählen, der als Vorlage heruntergeladen werden soll. |  |
| 4 | Wert eingeben | Geben Sie folgende Daten ein, und wählen Sie Anlegen:Verrechnungszyklus: <Geben Sie eine Zyklus-ID ein, die mit Z beginnt.>Verrechnungskontext: <Kostenstellen>Allokationsart:UmlageverrechnungLedger: 0LGültig bis: 31.12.2030Zyklusbeschreibung: <Geben Sie eine Zyklusbeschreibung ein>Buchungskreis: 1010Ist/Plan: PlanPlankategorie: PLN | Die Sicht <neuer Zyklus> wird angezeigt. |  |
| 5 | Segmentdaten eingeben | Wählen Sie im unteren Abschnitt der Sicht Neuer Verrechnungszyklus unter dem Abschnitt Segmente die Drucktaste Anlegen, geben Sie im Fenster Neues Segment anlegen die folgenden Daten ein, und wählen Sie die Drucktaste Anlegen:Segmentname: <Geben Sie ein Segment ein, das mit Z beginnt.>Segmentbeschreibung: <Geben Sie eine Beschreibung ein.> | Die Sicht <neues Segment> wird angezeigt. |  |
| 6 | Regeln eingeben | Wählen Sie das neue Segment, und wählen Sie den Pfeil auf der rechten Seite.Geben Sie auf der Registerkarte Regeln die folgenden Daten ein:Umlagekonto: 94201000Senderregel: BuchungsbeträgeEmpfängerregel: Feste ProzentsätzeAnteil in %: 100Währung: <Geben Sie Ihre lokale Währung ein.> |  |  |
| 7 | Senderdetails eingeben | Geben Sie auf der Registerkarte Sender Folgendes ein:Kontonummer:Ändern Sie den Wert in der Spalte Werttyp zu Gruppe.Verwenden Sie in der Spalte Gruppe die Auswahlliste, um 10_CE in der folgenden Sicht Auswählen: Kontonummer auszuwählen.Kostenstelle: 10101101 |  |  |
| 8 | Empfängerdetails eingeben | Wählen Sie auf der Registerkarte Empfänger die Option Hinzufügen. Wählen Sie in der Sicht Empfänger hinzufügen die Option Kostenstelle, und wählen Sie Hinzufügen. Tragen Sie Folgendes ein:KostenstelleÄndern Sie den Wert in der Spalte Eingabe Format zu Gruppe.Verwenden Sie die Dropdown-Liste der Spalte Gruppe, um 1010300 auszuwählen, in der folgenden Sicht Auswählen: Kostenstelle auszuwählen. |  |  |
| 9 | Empfängerbasis | Wählen Sie auf der Registerkarte Empfängerbasis die Drucktaste … (Zusätzliche Optionen), und wählen Sie Gleichmäßig verteilen. | Sie können erkennen, dass die Beträge gleichmäßig verteilt werden. |  |
| 10 | Sichern | Wählen Sie die Drucktaste Sichern. | Ihre Daten werden gesichert. |  |

#### Planumlagezyklen bearbeiten

Testverwaltung

Kundenprojekt: Füllen Sie die projektbezogenen Teile aus.

|  |  |  |  |
| --- | --- | --- | --- |
| Testfall-ID | <X.XX> | Testdatum: |  |
| Testername: |  | Dauer: |  |
| Benutzerrolle(n): |  | Zuständigkeit: | <Geben Sie den Serviceanbieter, einen Kunden oder einen Serviceanbieter zusammen mit einem Kunden an.> |

Kontext

Diese Aktivität zeigt, wie Sie mithilfe von Vorlagen mit Verrechnungen arbeiten können, die große Datenmengen aufweisen.

Vorgehensweise

| Testschrittnummer | Bezeichnung des Testschritts | Anweisung | Erwartetes Ergebnis | Kommentare |
| --- | --- | --- | --- | --- |
| 1 | Anmelden | Melden Sie sich am SAP Fiori Launchpad als Gemeinkostencontroller an. | Das SAP Fiori Launchpad wird angezeigt. |  |
| 2 | SAP-Fiori-App aufrufen | Öffnen Sie Verrechnungen verwalten(F3338A). | Die Sicht Verrechnungen verwalten wird angezeigt. |  |
| 3 | Werte eingeben | Geben Sie folgende Daten ein, und wählen Sie Start:Verrechnungskontext: <Kostenstellen>Buchungskreis: 1010Ledger: 0LVerrechnungszyklus: <Der eben von Ihnen angelegte Zyklus> | Die Sicht Verrechnungszyklen wird angezeigt. |  |
| 4 | Details zum Verrechnungszyklus | Wählen Sie Ihren Verrechnungszyklus, und wählen Sie den Pfeil auf der rechten Seite, um die Details anzuzeigen. Wählen Sie die Drucktaste Bearbeiten. | Die Sicht Verrechnungen verwalten wird angezeigt. |  |
| 5 | Abschnitt "Segmente" | Blättern Sie nach unten zum Abschnitt Segmente, markieren Sie Ihr Segment, und wählen Sie > (Details) auf der rechten Seite. |  |  |
| 6 | Empfängerbasis | Wählen Sie auf der Registerkarte Empfängerbasis die Option Werte hochladen/herunterladen. | Die Sicht Empfängerwerte hochladen wird angezeigt. |  |
| 7 | Empfängerwerte hochladen | Wählen Sie Vorlage mit Werten herunterladen. Laden Sie die Datei herunter, und sichern Sie sie. |  |  |
| 8 | Prozentsätze aktualisieren | Aktualisieren Sie in der Datei die Prozentsatzspalte mit den folgenden Werten:KostenstelleProzentsatz001010110150010101201500101012025001010130150010101302150010101401150010101501150010101601150010101602001010170120 | Die Prozentsätze werden aktualisiert. |  |
| 9 | Empfängerbasis | Kehren Sie zur Registerkarte Empfängerbasis zurück, und gehen Sie wie folgt vor:Wählen Sie Werte hochladen/herunterladen.Wählen Sie in der Sicht Empfängerwerte hochladen die Option Durchsuchen. Wählen Sie Ihre gesicherte Datei. Es wird angezeigt, ob die Werte hochgeladen werden können oder ob Korrekturen erforderlich sind. Wählen Sie Quittieren.Wählen Sie Sichern, um den Verrechnungszyklus zu sichern. | Sie sehen, dass die Daten per CSV-Datei-Upload aktualisiert wurden. |  |

### Istverrechnungen

#### Istumlagezyklen verwalten

Testverwaltung

Kundenprojekt: Füllen Sie die projektbezogenen Teile aus.

|  |  |  |  |
| --- | --- | --- | --- |
| Testfall-ID | <X.XX> | Testdatum: |  |
| Testername: |  | Dauer: |  |
| Benutzerrolle(n): |  | Zuständigkeit: | <Geben Sie den Serviceanbieter, einen Kunden oder einen Serviceanbieter zusammen mit einem Kunden an.> |

Kontext

In diesem Beispiel verwendet der Istumlagezyklus Sekundärkostenarten, um Kosten einer Kostenstelle oder einer Gruppe von Kostenstellen mit einer anderen Kostenstelle oder Gruppe von Kostenstellen innerhalb eines Buchungskreises zu einem festen Prozentsatz zu verrechnen.

Vorgehensweise

| Testschrittnummer | Bezeichnung des Testschritts | Anweisungen | Erwartetes Ergebnis | Kommentare |
| --- | --- | --- | --- | --- |
| 1 | Anmelden | Melden Sie sich am SAP Fiori Launchpad als Gemeinkostencontroller an. | Das SAP Fiori Launchpad wird angezeigt. |  |
| 2 | SAP-Fiori-App aufrufen | Öffnen Sie Verrechnungen verwalten(F3338A). | Die Sicht Verrechnungen verwalten wird angezeigt. |  |
| 3 | Zykluskopf anlegen | Wählen Sie die Drucktaste Anlegen und dann Neuen Zyklus anlegen. | Das Dialogfenster Neuen Zyklus anlegen wird angezeigt. |  |
| 4 | Wert eingeben | Geben Sie folgende Daten ein, und wählen Sie Anlegen:Verrechnungszyklus: <Geben Sie eine Zyklus-ID ein, die mit Z beginnt.>Verrechnungskontext: <Kostenstellen>Buchungskreis: 1010Allokationsart:UmlageverrechnungLedger: 0LGültig bis: 31.12.2030Zyklusbeschreibung: <Geben Sie eine Zyklusbeschreibung ein>Buchungskreis: 1010Ist/Plan: Ist | Das Bild Verrechnung: Plan-Umlagezyklus anlegen: Kopfdaten wird angezeigt. |  |
| 5 | Segmentdaten eingeben | Wählen Sie im unteren Abschnitt der Sicht Neuer Verrechnungszyklus unter dem Abschnitt Segmente die Drucktaste Hinzufügen, und geben Sie die folgenden Daten im Fenster Neues Segment anlegen ein:Segmentname: <Geben Sie ein Segment ein, das mit Z beginnt.>Segmentbeschreibung: <Geben Sie eine Beschreibung ein.> | Die Sicht Einen neuen Zyklus anlegen wird angezeigt. |  |
| 6 | Regeln eingeben | Wählen Sie das neue Segment, und wählen Sie den Pfeil auf der rechten Seite.Geben Sie auf der Registerkarte Regeln die folgenden Daten ein:Umlage- konto: 94201000Senderregel: BuchungsbeträgeEmpfängerregel: Feste Prozentsätze |  |  |
| 7 | Senderdetails eingeben | Geben Sie auf der Registerkarte Sender Folgendes ein:Kontonummer:Ändern Sie den Wert in der Spalte Werttyp zu Gruppe.Verwenden Sie die Dropdown-Liste der Spalte Gruppe, um 10_CE zu suchen und auszuwählen, in der folgenden Sicht Auswählen: Kontonummer auszuwählen.Kostenstelle: 10101101Hinweis Zusätzlich zu Standardkostenstellen und Sachkonten können Sie nun bestimmte Buchungsbelegattribute wie Währung, Funktionsbereich, Profitcenter und Segment verwenden, um eine detailliertere Verrechnungsselektion innerhalb der Senderregel zu ermöglichen. Wählen Sie dazu die Drucktaste Hinzufügen, und wählen Sie dann die gewünschten Optionen aus. |  |  |
| 8 | Empfängerdetails eingeben | Wählen Sie auf der Registerkarte Empfänger die Drucktaste + (Hinzufügen).Markieren Sie Kostenstelle, und wählen Sie die Drucktaste Hinzufügen.Nehmen Sie den folgenden Eintrag vor:KostenstelleÄndern Sie den Wert in der Spalte Eingabe Format zu Gruppe.Verwenden Sie die Dropdown-Liste der Spalte Gruppe, um 1010300 zu suchen und auszuwählen, in der folgenden Sicht Auswählen: Kostenstelle auszuwählen. |  |  |
| 9 | Empfängerbasis | Wählen Sie auf der Registerkarte Empfängerbasis die Drucktaste … (Zusätzliche Optionen), und wählen Sie Gleichmäßig verteilen. | Sie können erkennen, dass die Beträge gleichmäßig verteilt werden. |  |
| 10 | Sichern | Wählen Sie die Drucktaste Sichern. | Ihre Daten werden gesichert. |  |

#### Istumlagezyklen bearbeiten

Testverwaltung

Kundenprojekt: Füllen Sie die projektbezogenen Teile aus.

|  |  |  |  |
| --- | --- | --- | --- |
| Testfall-ID | <X.XX> | Testdatum: |  |
| Testername: |  | Dauer: |  |
| Benutzerrolle(n): |  | Zuständigkeit: | <Geben Sie den Serviceanbieter, einen Kunden oder einen Serviceanbieter zusammen mit einem Kunden an.> |

Kontext

Diese Aktivität zeigt, wie Sie mithilfe von Vorlagen mit Verrechnungen arbeiten können, die große Datenmengen aufweisen.

Vorgehensweise

| Testschrittnummer | Bezeichnung des Testschritts | Anweisung | Erwartetes Ergebnis | Kommentare |
| --- | --- | --- | --- | --- |
| 1 | Anmelden | Melden Sie sich am SAP Fiori Launchpad als Gemeinkostencontroller an. | Das SAP Fiori Launchpad wird angezeigt. |  |
| 2 | SAP-Fiori-App aufrufen | Öffnen Sie Verrechnungen verwalten(F3338A). | Die Sicht Verrechnungen verwalten wird angezeigt. |  |
| 3 | Werte eingeben | Geben Sie folgende Daten ein, und wählen Sie Start:Verrechnungskontext: <Kostenstellen>Buchungskreis: 1010Ledger: 0LVerrechnungszyklus: <Der eben von Ihnen angelegte Zyklus> | Die Sicht Verrechnungszyklen wird angezeigt. |  |
| 4 | Details zum Verrechnungszyklus | Wählen Sie Ihren Verrechnungszyklus, und wählen Sie den Pfeil auf der rechten Seite, um die Details anzuzeigen. | Die Sicht Verrechnungen verwalten wird angezeigt. |  |
| 5 | Abschnitt "Segmente" | Blättern Sie nach unten zum Abschnitt Segmente, markieren Sie Ihr Segment, und wählen Sie > (Details) auf der rechten Seite. |  |  |
| 6 | Empfängerbasis | Wählen Sie auf der Registerkarte Empfängerbasis die Option Werte hochladen/herunterladen. | Die Sicht Empfängerwerte hochladen wird angezeigt. |  |
| 7 | Empfängerwerte hochladen | Wählen Sie Vorlage mit Werten herunterladen. Laden Sie die Datei herunter, und sichern Sie sie. |  |  |
| 8 | Prozentsätze aktualisieren | Aktualisieren Sie in der Datei die Prozentsatzspalte mit den folgenden Werten:KostenstelleProzentsatz001010110150010101201500101012025001010130150010101302150010101401150010101501150010101601150010101602001010170120 | Die Prozentsätze werden aktualisiert. |  |
| 9 | Empfängerbasis | Kehren Sie zur Registerkarte Empfängerbasis zurück, und gehen Sie wie folgt vor:Wählen Sie Werte hochladen/herunterladen.Wählen Sie in der Sicht Empfängerwerte hochladen die Option Durchsuchen. Wählen Sie Ihre gesicherte Datei. Es wird angezeigt, ob die Werte hochgeladen werden können oder ob Korrekturen erforderlich sind. Wählen Sie Quittieren.Wählen Sie Sichern, um den Verrechnungszyklus zu sichern. | Sie sehen, dass die Daten per CSV-Datei-Upload aktualisiert wurden. |  |

### Plan-Profitcenter-Verrechnung

#### Plan-Profitcenter-Verteilungszyklen verwalten

Testverwaltung

Kundenprojekt: Füllen Sie die projektbezogenen Teile aus.

|  |  |  |  |
| --- | --- | --- | --- |
| Testfall-ID | <X.XX> | Testdatum: |  |
| Testername: |  | Dauer: |  |
| Benutzerrolle(n): |  | Zuständigkeit: | <Geben Sie den Serviceanbieter, einen Kunden oder einen Serviceanbieter zusammen mit einem Kunden an.> |

Kontext

Dieses Beispiel zeigt die Planverteilung von Bestandskontosalden zu und von verschiedenen Profitcentern.

Voraussetzungen

Es muss ein Sachkonto zur Ausgleichsverrechnung verfügbar sein. Legen Sie das Sachkonto "29500000 CO-Ausgleichsverrechnung" mit dem Sachkonto 29500100 als Bezug an. Weitere Informationen über das Anlegen eines Sachkontos finden Sie in Sachkonto und Kostenart anlegen – SDS (BNG).

Vorgehensweise

| Testschrittnummer | Bezeichnung des Testschritts | Anweisung | Erwartetes Ergebnis | Kommentare |
| --- | --- | --- | --- | --- |
| 1 | Anmelden | Melden Sie sich am SAP Fiori Launchpad als Spartenbuchhalter an. | Das SAP Fiori Launchpad wird angezeigt. |  |
| 2 | SAP-Fiori-App aufrufen | Öffnen Sie Verrechnungen verwalten(F3338A). | Die Sicht Verrechnungen verwalten wird angezeigt. |  |
| 3 | Zykluskopf anlegen | Wählen Sie die Drucktaste Anlegen und dann Neuen Zyklus anlegen. | Das Dialogfenster Neuen Zyklus anlegen wird angezeigt. |  |
| 4 | Werte eingeben | Geben Sie folgende Daten ein, und wählen Sie Anlegen:Verrechnungszyklus: <Geben Sie eine Zyklus-ID ein, die mit Z beginnt>Verrechnungskontext: <Profitcenter>Buchungskreis: 1010Allokationsart:VerteilungLedger: 0LGültig bis: 31.12.2030Zyklusbeschreibung: <Geben Sie eine Zyklusbeschreibung ein>Buchungskreis: 1010Ist/Plan: PlanPlankategorie: PLN | Die Sicht Verrechnungen verwalten wird angezeigt. |  |
| 5 | Segmentdaten eingeben | Wählen Sie im unteren Abschnitt der Sicht Verrechnungen verwalten unter dem Abschnitt Segmente die Drucktaste Anlegen, und geben Sie im Fenster Neues Segment anlegen die folgenden Daten ein:Segmentname: <Geben Sie einen anderen Segmentnamen ein, der mit ZD beginnt.>Segmentbeschreibung: <Geben Sie eine Beschreibung ein.>Wählen Sie OK. |  |  |
| 6 | Regeln eingeben | Geben Sie auf der Registerkarte Regeln die folgenden Daten ein:Währung:<Geben Sie Ihre lokale Währung ein.>Senderregel:Feste BeträgeAnteil in %: 100Empfängerregel: Feste ProzentsätzeWählen Sie die Registerkarte Sender. |  |  |
| 7 | Senderdetails eingeben | Geben Sie auf der Registerkarte Sender Folgendes ein:Kontonummer: 29500000Profitcenter: YB600Wählen Sie die Registerkarte Senderbasis. |  |  |
| 8 | Senderbasis | Geben Sie folgende Daten ein:Betrag: 100000Wählen Sie die Registerkarte Empfänger. |  |  |
| 9 | Empfängerdetails eingeben | Wählen Sie im Abschnitt Empfänger die Option + (Hinzufügen). Wählen Sie in der Sicht Empfänger hinzufügen die Option Profitcenter. Wählen Sie Hinzufügen, und geben Sie Folgendes ein:Werttyp: IntervallEinzeleintrag/Von: YB700Bis-Wert: YB800Wählen Sie die Registerkarte Empfängerbasis. |  |  |
| 10 | Empfängerbasis | Wählen Sie auf der Registerkarte Empfängerbasis die Drucktaste … (Zusätzliche Optionen), und wählen Sie Gleichmäßig verteilen. | Sie können erkennen, dass die Beträge gleichmäßig verteilt werden. |  |
| 11 | Sichern | Wählen Sie die Schaltfläche Sichern. | Die Plan-Profitcenter-Verteilung wird angelegt. |  |

### Ist-Profitcenter-Verrechnung

#### Ist-Profitcenter-Verteilungszyklen verwalten

Testverwaltung

Kundenprojekt: Füllen Sie die projektbezogenen Teile aus.

|  |  |  |  |
| --- | --- | --- | --- |
| Testfall-ID | <X.XX> | Testdatum: |  |
| Testername: |  | Dauer: |  |
| Benutzerrolle(n): |  | Zuständigkeit: | <Geben Sie den Serviceanbieter, einen Kunden oder einen Serviceanbieter zusammen mit einem Kunden an.> |

Kontext

Dieses Beispiel zeigt die Istverteilung von Bestandskontosalden zu und von verschiedenen Profitcentern.

Voraussetzungen

Es muss ein Sachkonto zur Ausgleichsverrechnung verfügbar sein. Legen Sie das Sachkonto "29500000 CO-Ausgleichsverrechnung" mit dem Sachkonto 29500100 als Bezug an. Weitere Informationen über das Anlegen eines Sachkontos finden Sie in Sachkonto und Kostenart anlegen – SDS (BNG).

Vorgehensweise

| Testschrittnummer | Bezeichnung des Testschritts | Anweisung | Erwartetes Ergebnis | Kommentare |
| --- | --- | --- | --- | --- |
| 1 | Anmelden | Melden Sie sich am SAP Fiori Launchpad als Spartenbuchhalter an. | Das SAP Fiori Launchpad wird angezeigt. |  |
| 2 | SAP-Fiori-App aufrufen | Öffnen Sie Verrechnungen verwalten(F3338A). | Die Sicht Verrechnungen verwalten wird angezeigt. |  |
| 3 | Zykluskopf anlegen | Wählen Sie die Drucktaste Anlegen und dann Neuen Zyklus anlegen. | Das Dialogfenster Neuen Zyklus anlegen wird angezeigt. |  |
| 4 | Werte eingeben | Geben Sie folgende Daten ein, und wählen Sie Anlegen:Verrechnungszyklus: <Geben Sie eine Zyklus-ID ein, die mit Z beginnt>Verrechnungskontext: <Profitcenter>Buchungskreis: 1010Allokationsart:VerteilungLedger: 0LGültig bis: 31.12.2030Zyklusbeschreibung: <Geben Sie eine Zyklusbeschreibung ein>Buchungskreis: 1010Ist/Plan: Ist | Das Bild Verrechnung: Plan-Verteilungszyklus anlegen: Kopfdaten wird angezeigt. |  |
| 5 | Segmentdaten eingeben | Wählen Sie im unteren Abschnitt der Sicht Verrechnungen verwalten unter dem Abschnitt Segmente die Drucktaste Hinzufügen, und geben Sie die folgenden Daten im Fenster Neues Segment anlegen ein:Segmentname: <Geben Sie einen anderen Segmentnamen ein, der mit ZD beginnt.>Segmentbeschreibung: <Geben Sie eine Beschreibung ein.> | Die Sicht Verrechnung: Plan-Verteilungszyklus anlegen: Kopfdaten wird angezeigt. |  |
| 6 | Regeln eingeben | Wählen Sie das neu angelegte Segment, und wählen Sie das Symbol > auf der rechten Seite. Geben Sie auf der Registerkarte Regeln die folgenden Daten ein:Währung:<Geben Sie Ihre lokale Währung ein.>Senderregel: Feste BeträgeAnteil in %: 100Empfängerregel: Feste ProzentsätzeWählen Sie die Registerkarte Sender. |  |  |
| 7 | Senderdetails eingeben | Geben Sie auf der Registerkarte Sender Folgendes ein:Kontonummer: 29500000Profitcenter: YB600Wählen Sie die Registerkarte Senderbasis. |  |  |
| 8 | Senderbasis | Geben Sie folgende Daten ein:Betrag: 100000Wählen Sie die Registerkarte Empfänger. |  |  |
| 9 | Empfängerdetails eingeben | Wählen Sie im Abschnitt Empfänger die Option + (Hinzufügen). Wählen Sie in der Sicht Empfänger hinzufügen die Option Profitcenter. Wählen Sie Hinzufügen, und geben Sie Folgendes ein:Werttyp: IntervallEinzeleintrag/Von: YB700Bis-Wert: YB800Wählen Sie die Registerkarte Empfängerbasis. |  |  |
| 10 | Empfängerbasis | Wählen Sie auf der Registerkarte Empfängerbasis die Drucktaste … (Zusätzliche Optionen), und wählen Sie Gleichmäßig verteilen. | Sie können erkennen, dass die Beträge gleichmäßig verteilt werden. |  |
| 11 | Sichern | Wählen Sie die Schaltfläche Sichern. | Die Profitcenter-Verteilung wird angelegt. |  |

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
- related-to :: [[06-management-accounting/create-universal-allocation-master-data-mds-2us-287]]
- related-to :: [[06-management-accounting/mds-2us-289]]
- related-to :: [[06-management-accounting/mds-2us-291]]
- related-to :: [[06-management-accounting/script-de-dados-mestre-criar-dados-mestre-de-alocacao-universal-mds-2u]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/2US_S4CLD2608_Master_Data_DE_XX.docx` — full document · extracted with `mammoth` · 30,235 chars in the whole document
