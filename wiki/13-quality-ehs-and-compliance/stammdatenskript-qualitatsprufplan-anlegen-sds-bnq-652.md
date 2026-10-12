---
id: 13-quality-ehs-and-compliance/stammdatenskript-qualitatsprufplan-anlegen-sds-bnq-652
title: "Stammdatenskript: Qualitätsprüfplan anlegen – SDS (BNQ) (BNQ_S4CLD2608_Master_Data_DE_XX)"
description: "German SAP S/4HANA Cloud Public Edition 2608 master data script (BNQ): step-by-step creation and maintenance of quality inspection plans and their prerequisite QM master data."
cluster: 13-quality-ehs-and-compliance
tags: [kb/quality-ehs-and-compliance, topic/inspection-plans]
aliases: [BNQ_S4CLD2608_Master_Data_DE_XX]
keywords: [Quality Inspection Plans, inspection plans, inspection plan maintenance, master inspection characteristics, code groups, selected sets, sampling plans, dynamic modification rules, copy inspection plan, class characteristic link]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/BNQ_S4CLD2608_Master_Data_DE_XX.docx]
confidence: low
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-652
topic: 13-quality-ehs-and-compliance/inspection-plans
language: DE
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Stammdatenskript: Qualitätsprüfplan anlegen – SDS (BNQ) (BNQ_S4CLD2608_Master_Data_DE_XX)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/BNQ_S4CLD2608_Master_Data_DE_XX.docx`, extracted with `mammoth`. Grouped under **Quality Inspection Plans** in Quality, EHS and Compliance. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

| <!-- image omitted: unnamed --> | StammdatenskriptSAP S/4HANA Cloud Public Edition - 02-07-26 |
| --- | --- |
|  | Qualitätsprüfplan anlegen – SDS (BNQ) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Inhaltsverzeichnis

[1 Verwendungszweck 3](#_Toc233890018)

[2 Voraussetzungen 4](#_Toc233890019)

[2.1 Systemzugriff 4](#_Toc233890020)

[2.2 Rollen 4](#_Toc233890021)

[2.3 Erforderliche Organisationseinheiten 4](#_Toc233890022)

[2.4 Obligatorische und optionale Stammdaten 5](#_Toc233890023)

[2.5 Voraussetzungen/Situation 6](#_Toc233890024)

[2.6 Wesentliche Parameter für die Datenerstellung 6](#_Toc233890025)

[2.6.1 Nummernkreise 6](#_Toc233890026)

[3 Übersichtstabelle 7](#_Toc233890027)

[4 Testverfahren 8](#_Toc233890028)

[4.1 Merkmalsattribute - Codegruppen für Auswahlmengen bearbeiten 8](#_Toc233890029)

[4.2 Auswahlmengen für Merkmalsattribute bearbeiten 9](#_Toc233890030)

[4.3 Codegruppen aufgrund von Fehlern bearbeiten (optional) 10](#_Toc233890031)

[4.4 Prüfmethode anlegen (optional) 11](#_Toc233890032)

[4.5 Stammprüfmerkmale anlegen (optional) 13](#_Toc233890033)

[4.6 Stammprüfmerkmal mit Verweis auf das Klassenmerkmal anlegen (optional) 17](#_Toc233890034)

[4.7 Stichprobenplan anlegen (optional) 18](#_Toc233890035)

[4.8 Stichprobenverfahren anlegen (optional) 22](#_Toc233890036)

[4.9 Dynamisierungsregel erstellen (optional) 23](#_Toc233890037)

[4.10 Prüfplan anlegen 25](#_Toc233890038)

[4.11 Prüfpläne verwalten 27](#_Toc233890039)

[4.12 Aus bestehenden Prüfplänen kopieren 31](#_Toc233890040)

[4.13 Offene Prüflose anzeigen 33](#_Toc233890041)

## Verwendungszweck

Soll die Materialqualität geprüft werden, ist eine der Voraussetzungen, dass ein Prüfplan verfügbar ist. Beispiel: Möglicherweise muss beim Wareneingang eine Prüfung durch den Lieferanten oder aus dem Fertigungsauftrag erfolgen. Der Prüfplan muss dann Details über die zu prüfenden Merkmale, zur Prüfweise und zur Anzahl der Stichproben enthalten.

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
| Qualitätsplaner | SAP_BR_QUALITY_PLANNER | Qualitätsplanung | SAP_BR_QUALITY_PLANNER |  |
| Qualitätstechniker | SAP_BR_QUALITY_TECHNICIAN | Qualitätsprüfung | SAP_BR_QUALITY_TECHNICIAN |  |

### Erforderliche Organisationseinheiten

Einige Segmente von Stammdaten sind von den Organisationseinheiten des Werks abhängig. Die folgende Tabelle bietet eine Übersicht über diese verschiedenen Datensegmente und ihre entsprechenden Organisationseinheiten:

| Datensegment | Hängt ab von | Feldbeispiele | Kommentare | Zu verwendende Organisationseinheit |
| --- | --- | --- | --- | --- |
| Auswahlmengen von Merkmalsattributen - Auswahlmengen bearbeiten | Werk | Auswahlmenge usw. | Auswahlmengen kombinieren unterschiedliche Codegruppen sowie Codes auf Werksebene, die für bestimmte Anwendungen hilfreich sind. | Werk: |
| Prüfmethode anlegen | Werk | Prüfmethode | Die Prüfmethode kann in einem Prüfplan verwendet werden. |  |
| Prüfplanmerkmale anlegen | Werk | Stammprüfmerkmal, Zuordnung einer Auswahlmenge usw. | Stammprüfmerkmale können in einem Prüfplan verwendet werden. | Werk: |
| Prüfplan anlegen | Werk | Zuordnung zu Materialnummer, Verwendung, Status, Arbeitsplatz usw. | Werksdaten werden für jede Werks-ID Ihrer Unternehmensstruktur für einen Prüfplan zugeordnet. | Werk: |

### Obligatorische und optionale Stammdaten

Die folgende Tabelle bietet eine Übersicht über die optionalen und obligatorischen Stammdatenobjekte, die in einem Qualitätsprüfplan-Datensatz verwendet werden.

| Stammdatenobjekt | Verwendet im Datensegment | Obligatorisch / optional | Kommentare |
| --- | --- | --- | --- |
| Codegruppe/Auswahlmenge – für Merkmalsattribut |  | Obligatorisch | Vor dem Anlegen eines Prüfplans müssen Sie die Codegruppe/Auswahlmenge für das Merkmalsattribut anlegen. |
| Codegruppe - bei Fehlern |  | Optional | "Codegruppe - bei Fehlern" kann vor dem Anlegen eines Prüfplans angelegt werden. |
| Prüfmethoden |  | Optional | Vor dem Anlegen eines Prüfplans können Sie die Prüfmethoden anlegen. |
| Stammprüfmerkmale |  | Optional | Vor dem Anlegen eines Prüfplans können Sie Stammprüfmerkmale anlegen. |
| Stichprobenplan |  | Optional | Der Stichprobenplan definiert eine Sammlung von Stichprobenplänen, die vor dem Anlegen eines Prüfplans angelegt werden können. |
| Stichprobenverfahren |  | Optional | Das Stichprobenverfahren definiert die Regeln dazu, wie das System den Stichprobenumfang berechnet, und das Verfahren kann vor dem Anlegen eines Prüfplans angelegt werden. |
| Dynamisierungsregel |  | Optional | Die Dynamisierungsregel enthält die Definition der Prüfstufen und die Bedingung für einen Stufenwechsel. Eine Dynamisierungsregel kann vor dem Anlegen eines Prüfplans angelegt werden. |

### Voraussetzungen/Situation

Um diesen Umfangsbestandteil testen zu können, müssen die folgenden Voraussetzungen erfüllt sein.

| Umfangsbestandteil | Voraussetzungen/Situation |
| --- | --- |
| BNY - Qualitätsmanagementattribute für Material-/Produktstamm anlegen – SDS | Vor dem Anlegen eines Prüfplans müssen Sie den Materialstamm anlegen. |
| 2ZW – Stammdaten der Chargenverwaltung anlegen – SDS (optional) | Wenn die Prüfergebnisse beim Treffen des Verwendungsentscheids an die Chargenklasse übergeben werden sollen, stellen Sie sicher, dass folgende Voraussetzungen erfüllt sind: Beachten Sie auch, dass ein Klassenmerkmal einem Stammprüfmerkmal zugeordnet sein muss (siehe Abschnitt dieses Dokuments):Das Klassenmerkmal muss vorhanden sein.Die Chargenklasse (Typ 203) muss vorhanden sein.Das Klassenmerkmal muss einer Klasse vom Typ 023 zugeordnet sein.Das Material muss chargenpflichtig sein, und dem Materialstamm wurde in der Klassifizierungssicht eine Chargenklasse zugeordnet.Hinweis Wenn der Verwendungsentscheid und die entsprechende Qualitätskennzahl in die Chargenklassifizierung übertragen werden sollen, muss der Chargenklasse das Klassenmerkmal LOBM_UDCODE bzw. LOBM_QSCORE zugeordnet werden. Beachten Sie, dass es in diesem Fall nicht erforderlich ist, diese Merkmale mit einem Stammprüfmerkmal zu verknüpfen. |

### Wesentliche Parameter für die Datenerstellung

In diesem Abschnitt werden einige Basisparameter erläutert, die das Verhalten eines Stammsatzes beeinflussen und zum Anlegen eines Prüfplans immer erforderlich sind.

#### Nummernkreise

Die folgenden Nummernkreise sind für Inspektionspläne und die zugehörigen abhängigen Funktionen definiert:

| Nummernkreis | Bereich / Geschäftspartner-ID | Kommentare |
| --- | --- | --- |
| Externer numerischer Nummernkreis | 50000000 bis 59999999 | Dieser Bereich ist für den Prüfplan. |

## Übersichtstabelle

Dieser Umfangsbestandteil umfasst die verschiedenen Prozessschritte in der folgenden Tabelle:

|  |
| --- |
| Hinweis Wenn Ihr Systemadministrator Bereiche und Seiten auf dem SAP Fiori Launchpad aktiviert hat, enthält die Startseite nur die wesentlichen Apps, mit denen die typischen Aufgaben einer Benutzerrolle ausgeführt werden können.Alle anderen (suchbaren) Apps, die nicht auf der Startseite enthalten sind, finden Sie über die Suchleiste ([2434549](https://me.sap.com/notes/2434549)).Wenn Sie die Startseite personalisieren und versteckte Apps hinzufügen möchten, wechseln Sie in Ihr Benutzerprofil und wählen Sie App Finder. |

| Prozessschritt | Benutzerrolle | App/Vorgang | Erwartete Ergebnisse |
| --- | --- | --- | --- |
| [Merkmalsattribute - Codegruppen für Auswahlmengen bearbeiten](#unique_11) [Seite ] 8 | Qualitätsplaner | Codegruppen bearbeiten(QS41) | Merkmalsattribute Codegruppen und Codes werden angelegt. |
| [Auswahlmengen für Merkmalsattribute bearbeiten](#unique_12) [Seite ] 9 | Qualitätsplaner | Auswahlmengen bearbeiten(QS51) | Auswahlmenge für Merkmalsattribut wird angelegt. |
| [Codegruppen aufgrund von Fehlern bearbeiten (optional)](#unique_13) [Seite ] 10 | Qualitätsplaner | Codegruppen bearbeiten(QS41) | Codegruppen werden angelegt. |
| [Prüfmethode anlegen (optional)](#unique_14) [Seite ] 11 | Qualitätsplaner | Prüfmethode anlegen(QS31) | Eine Prüfmethode wird angelegt. |
| [Stammprüfmerkmale anlegen (optional)](#unique_15) [Seite ] 13 | Qualitätsplaner | Stammprüfmerkmal anlegen(QS21) | Stammprüfmerkmale werden angelegt. |
| [Stammprüfmerkmal mit Verweis auf das Klassenmerkmal anlegen (optional)](#unique_16) [Seite ] 17 | Qualitätsplaner | Stammprüfmerkmal anlegen(QS21) | Ein quantitatives Stammprüfmerkmal mit Verweis auf das Klassenmerkmal wird angelegt. |
| [Stichprobenplan anlegen (optional)](#unique_17) [Seite ] 18 | Qualitätsplaner | Stichprobenplan anlegen(QDP1) | Stichprobenplan wird angelegt. |
| [Stichprobenverfahren anlegen (optional)](#unique_18) [Seite ] 22 | Qualitätsplaner | Stichprobenverfahren anlegen(QDV1) | Stichprobenverfahren wird angelegt. |
| [Dynamisierungsregel erstellen (optional)](#unique_19) [Seite ] 23 | Qualitätsplaner | Dynamisierungsregel anlegen(QDR1) | Eine Dynamisierungsregel wird angelegt. |
| [Prüfplan anlegen](#unique_20) [Seite ] 25 | Qualitätsplaner | Prüfplan anlegen(QP01) | Prüfplan wird angelegt. |

## Testverfahren

In diesem Abschnitt werden die Testverfahren für den jeweiligen Prozessschritt beschrieben, der zum betreffenden Umfangsbestandteil gehört.

### Merkmalsattribute - Codegruppen für Auswahlmengen bearbeiten

Testverwaltung

Kundenprojekt: Füllen Sie die projektbezogenen Teile aus.

|  |  |  |  |
| --- | --- | --- | --- |
| Testfall-ID | <X.XX> | Testdatum: |  |
| Testername: |  | Dauer: |  |
| Benutzerrolle(n): |  | Zuständigkeit: | <Geben Sie den Serviceanbieter, einen Kunden oder einen Serviceanbieter zusammen mit einem Kunden an.> |

Verwendungszweck

Merkmalsattribute bezieht sich auf einen Standardkatalog für das Qualitätsmanagement (QM), in dem mögliche Zustände der geprüften Attribute definiert werden. Die Codes werden in Codegruppen gruppiert, sodass eine hierarchische Struktur festgelegt wird.

Vorgehensweise

| Testschrittnummer | Bezeichnung des Testschritts | Anweisungen | Erwartetes Ergebnis | Kommentare |
| --- | --- | --- | --- | --- |
| 1 | Anmelden | Melden Sie sich am SAP Fiori Launchpad als Qualitätsplaner an. | Die Startseite wird angezeigt. |  |
| 2 | SAP-Fiori-App aufrufen | Öffnen Sie Codegruppen bearbeiten(QS41). | Das Bild Katalog bearbeiten: Einstieg wird angezeigt. |  |
| 3 | Katalog eingeben | Geben Sie im Bild Katalog bearbeiten: Einstieg die folgenden Daten ein:Katalog: z.B. 1Codegruppe: *Wählen Sie Weiter. | Die Sicht "Codegruppen bearbeiten" ändern: Übersicht wird angezeigt. |  |
| 4 | Codegruppen bearbeiten | Wählen Sie eine Codegruppe aus, z.B. OBERFLÄCHE, und wählen Sie Codes in der Dialogstruktur mit Doppelklick aus. | Die Sicht "Codegruppe" ändern: Übersicht wird angezeigt. |  |
| 5 | Codes anlegen | Wählen Sie in der Sicht Sicht "Codes" ändern: Übersicht die Option Neue Einträge, und geben Sie folgende Daten ein:Code: z.B. 0010, 0020 und so weiterKurztext zum Code: <Beschreibung eingeben> |  |  |
| 6 | Daten sichern | Wählen Sie Sichern. | Ihre Daten werden gesichert. |  |

### Auswahlmengen für Merkmalsattribute bearbeiten

Testverwaltung

Kundenprojekt: Füllen Sie die projektbezogenen Teile aus.

|  |  |  |  |
| --- | --- | --- | --- |
| Testfall-ID | <X.XX> | Testdatum: |  |
| Testername: |  | Dauer: |  |
| Benutzerrolle(n): |  | Zuständigkeit: | <Geben Sie den Serviceanbieter, einen Kunden oder einen Serviceanbieter zusammen mit einem Kunden an.> |

Zweck

Auswahlmengen kombinieren unterschiedliche Codegruppen sowie Codes auf Werksebene. Diese Auswahlmengen sind für bestimmte Szenarios wie das Beschreiben möglicher Analyseergebnisse für ein bestimmtes Produktattribut (z.B. Oberflächeneigenschaften) hilfreich.

Vorgehensweise

| Testschrittnummer | Bezeichnung des Testschritts | Anweisung | Erwartetes Ergebnis | Kommentare |
| --- | --- | --- | --- | --- |
| 1 | Anmelden | Melden Sie sich am SAP Fiori Launchpad als Qualitätsplaner an. | Das SAP Fiori Launchpad wird angezeigt. |  |
| 2 | SAP-Fiori-App aufrufen | Öffnen Sie Auswahlmengen bearbeiten(QS51). | Die App wird geöffnet. |  |
| 3 | Katalog\Werk\Auswahlmenge eingeben | Geben Sie im Bild Auswahlmenge bearbeiten: Einstieg die folgenden Daten ein:Katalog: 1Werk: <Nummer des Werks>Auswahlmenge: *Wählen Sie Enter. | Die Änderungssicht "Auswahlmengen": Übersicht wird angezeigt. |  |
| 4 | Auswahlmengen bearbeiten | Wählen Sie eine Auswahlmenge, z.B. GLATT, und wählen Sie dann per Doppelklick Auswahlmengen-Codes in der Dialogstruktur. | Das Bild Sicht "Auswahlmengencodes" ändern: Übersicht wird angezeigt. |  |
| 5 | Auswahlmengen-Codes anlegen | Wählen Sie im Bild Sicht "Auswahlmengencodes" ändern: Übersicht die Option Neue Einträge, und geben Sie folgende Daten ein:Codegruppe: <Codegruppenwert>Code: <Codewert>Bewertungscode: entweder Annahme (in Ordnung) oder Rückweisung (nicht in Ordnung)Fehlerklasse: Hauptfehler |  |  |
| 6 | Daten sichern | Wählen Sie Sichern. | Ihre Daten werden gesichert. |  |

### Codegruppen aufgrund von Fehlern bearbeiten (optional)

Testverwaltung

Kundenprojekt: Füllen Sie die projektbezogenen Teile aus.

|  |  |  |  |
| --- | --- | --- | --- |
| Testfall-ID | <X.XX> | Testdatum: |  |
| Testername: |  | Dauer: |  |
| Benutzerrolle(n): |  | Zuständigkeit: | <Geben Sie den Serviceanbieter, einen Kunden oder einen Serviceanbieter zusammen mit einem Kunden an.> |

Verwendungszweck

Verwenden Sie Codegruppen, um mögliche qualitätsbezogene Fehler zu kategorisieren oder zu klassifizieren.

Vorgehensweise

| Testschrittnummer | Bezeichnung des Testschritts | Anweisungen | Erwartetes Ergebnis | Kommentare |
| --- | --- | --- | --- | --- |
| 1 | Anmelden | Melden Sie sich am SAP Fiori Launchpad als Qualitätsplaner an. | Die Startseite wird angezeigt. |  |
| 2 | SAP-Fiori-App aufrufen | Öffnen Sie Codegruppen bearbeiten(QS41). | Das Bild Katalog bearbeiten: Einstieg wird angezeigt. |  |
| 3 | Ausgangsdaten eingeben | Nehmen Sie folgende Einträge vor:Katalog: z.B. 9Codegruppe z.B. DEF-SURFWählen Sie Weiter. | Die Sicht "Codegruppen bearbeiten" ändern: Übersicht wird angezeigt. |  |
| 4 | Codegruppen bearbeiten | Nehmen Sie im Bereich Codegruppen bearbeiten folgende Einträge vor:Kurztext: z.B. Oberflächenfehler | Stellen Sie sicher, dass der Codegruppenstatus auf Freigegeben eingestellt ist. |  |
| 5 | Codes von Codegruppen bearbeiten | Wählen Sie im Bereich Codegruppen bearbeiten eine Position aus, die Sie angelegt haben.Navigieren Sie zu Codes, und wählen Sie "Codes" in der Dialogstruktur mit Doppelklick aus. | Die Sicht Sicht "Codes“ ändern: Übersicht wird angezeigt. |  |
| 6 | Codes von Codegruppen bearbeiten | Wählen Sie in der Sicht Sicht "Codes“ ändern: Übersicht Neue Einträge.Machen Sie folgende Eingaben:Code: z.B. 0010Kurztext zum Code: z.B. OberflächenproblemFehlerklasse: z.B. HauptfehlerZum Sichern Ihrer Daten wählen Sie Sichern. | Die Codegruppen wurden bearbeitet. |  |

### Prüfmethode anlegen (optional)

Testverwaltung

Kundenprojekt: Füllen Sie die projektbezogenen Teile aus.

|  |  |  |  |
| --- | --- | --- | --- |
| Testfall-ID | <X.XX> | Testdatum: |  |
| Testername: |  | Dauer: |  |
| Benutzerrolle(n): |  | Zuständigkeit: | <Geben Sie den Serviceanbieter, einen Kunden oder einen Serviceanbieter zusammen mit einem Kunden an.> |

Verwendungszweck

Prüfmethode anlegen.

Vorgehensweise

| Testschrittnummer | Bezeichnung des Testschritts | Anweisungen | Erwartetes Ergebnis | Kommentare |
| --- | --- | --- | --- | --- |
| 1 | Anmelden | Melden Sie sich am SAP Fiori Launchpad als Qualitätsplaner an. | Die Startseite wird angezeigt. |  |
| 2 | SAP-Fiori-App aufrufen | Wählen Sie Prüfmethode anlegen(QS31). | Prüfmethode anlegen: Einstieg wird angezeigt. |  |
| 3 | Ausgangsdaten eingeben | Nehmen Sie folgende Einträge vor:Werk: <Nummer des Werks>Prüf Methode: z.B. OBERFLÄCHEGültig ab: z.B. <aktuelles Datum>.Wählen Sie Prüfmethode. | Prüfmethode anlegen: Allgemeine Daten wird angezeigt. |  |
| 4 | Allgemeine Daten eingeben | Nehmen Sie folgende Einträge vor:Status: FreigegebenKurztext: z.B. OberflächeSuchfeld: z.B. Oberfläche |  |  |
| 5 | Langtext erfassen | Wählen Sie Langtext anlegen neben dem Feld Kurztext und geben Sie einen Beschreibungstext ein, z. B.:Bitte prüfen Sie die Oberfläche sorgfältig, insbesondere auf Unebenheiten und Kratzer oder Kerben.Wählen Sie Zurück. |  |  |
| 6 | Daten sichern | Zum Sichern Ihrer Daten wählen Sie Sichern. |  |  |
| 7 | SAP-Fiori-App aufrufen | Wählen Sie Prüfmethode ändern. | Das Bild Version der Prüfmethode ändern: Einstieg wird angezeigt. |  |
| 8 | Ausgangsdaten eingeben | Nehmen Sie folgende Einträge vor:Werk: <Nummer des Werks>Prüf Methode: z.B. OBERFLÄCHEWählen Sie Prüfmethode. | Die Sicht Version der Prüfmethode ändern: Allgemeine Daten wird angezeigt. |  |
| 9 | Anzuhängendes Dokument auswählen | Wählen Sie Dokumente aus Allgemeine Informationen aus. |  |  |
| 10 | Anlage für Dokument anlegen | Wählen Sie Belege anlegen.Wählen Sie im Dialogfenster Version der Prüfmethode ändern: Allgemeine Daten Weiter/Enter , ohne Daten einzugeben.Bestätigen Sie die Meldung über das Hochladen von Dateien mit OK, und wählen Sie per Doppelklick eine Datei aus Ihrem Dateisystem aus.Wählen Sie Übertragen, um zurück zum Bild Version der Prüfmethode ändern: Allgemeine Daten zu navigieren. |  |  |
| 11 | Daten sichern | Zum Sichern Ihrer Daten wählen Sie Sichern. |  |  |

### Stammprüfmerkmale anlegen (optional)

Testverwaltung

Kundenprojekt: Füllen Sie die projektbezogenen Teile aus.

|  |  |  |  |
| --- | --- | --- | --- |
| Testfall-ID | <X.XX> | Testdatum: |  |
| Testername: |  | Dauer: |  |
| Benutzerrolle(n): |  | Zuständigkeit: | <Geben Sie den Serviceanbieter, einen Kunden oder einen Serviceanbieter zusammen mit einem Kunden an.> |

Vorgehensweise

| Testschrittnummer | Bezeichnung des Testschritts | Anweisungen | Erwartetes Ergebnis | Kommentare |
| --- | --- | --- | --- | --- |
| 1 | Anmelden | Melden Sie sich am SAP Fiori Launchpad als Qualitätsplaner an. | Die Startseite wird angezeigt. |  |
| 2 | SAP-Fiori-App aufrufen | Öffnen Sie Stammprüfmerkmal anlegen(QS21). | Das Bild Stammprüfmerkmal anlegen: Einstieg wird angezeigt. |  |
| 3 | Werksdaten eingeben | Geben Sie im Bild Stammprüfmerkmal anlegen: Einstieg die folgenden Daten ein:Werk: <Nummer des Werks>Stammprüfmerkmal: <Wert>, z.B. YQUALI01Gültig ab: <aktuelles Datum>Wählen Sie Stammprüfmerkmal | Das Bild Stammprüfmerkmal anlegen: Allgemeine Daten wird angezeigt. |  |
| 4 | Allgemeine Daten für qualitative Merkmale eingeben | Geben Sie im Bild Stammprüfmerkmal anlegen: Allgemeine Daten folgende Daten ein:Qualitatives Merkmal: markiertKurztext: z.B. OberflächeSuchfeld: z.B. OberflächeStatus: Wählen SieFreigegeben und Referenzmerkmal.Wählen Sie Enter. | Ein neues Fenster wird angezeigt: Steuerungskennzeichen Merkmal bearbeitenReferenzmerkmalWenn Sie das Stammprüfmerkmal in einem Prüfplan verwenden, wird zuerst ein Verweis auf dieses Merkmal angelegt. Sie können diesen Verweis jedoch zurücknehmen und die Daten – zum Beispiel Toleranzen – einzeln ändern. Optionale Einstellungen sind in den folgenden Schritten enthalten.Vollständige KopiervorlageWenn Sie das Stammprüfmerkmal in einem Prüfplan verwenden, wird der Verweis auf dieses Merkmal zurückgenommen. Sie können die Daten - zum Beispiel Toleranzen - sofort ändern. Nur dann können Sie dieses Stammprüfmerkmal als Kopiervorlage verwenden.Unvollständige KopiervorlageWenn Sie das Stammprüfmerkmal in einem Prüfplan verwenden, kann es nur in einer Kopiervorlage verwendet werden. Diese Art von Stammprüfmerkmal kann nicht in einer Materialspezifikation verwendet werden. |  |
| 5 | Steuerungskennzeichen für qualitative Merkmale bearbeiten | Markieren Sie im Bild Steuerkennzeichen Merkmal bearbeiten die folgenden Optionen:MerkmalsausprägungStichprobenverfahrenSumm. ErfassungMussmerkmalWählen Sie Weiter, um weitere Optionen zu markieren.Umfang festKeine DokumentationWählen Sie Weiter, um die Bearbeitung zu beenden. | Das Bild Steuerkennzeichen Merkmal bearbeiten wird angezeigt. |  |
| 6 | Prüfkataloge zuordnen | Wählen Sie aus dem Dialogfenster Zugeordneter Prüfkatalog einen Wert für das Feld Cgr/Amg, z.B. GLATT.Wählen Sie Weiter. | Kehren Sie zum Bild Stammprüfmerkmal anlegen: Allgemeine Daten zurück.Hinweis Das Werk wird automatisch eingetragen, wenn Sie über die Wertehilfe Glatt wählen. |  |
| 7 | Prüfmethode zuordnen (optional) | Wählen Sie Prüfmethoden, und das Bild Zugeordnete Prüfmethoden wird angezeigt.Geben Sie folgende Daten ein:Methode: OberflächeWerk: <Nummer des Werks>Wählen Sie Weiter. | Kehren Sie zum Bild Stammprüfmerkmal anlegen: Allgemeine Daten zurück. |  |
| 8 | Daten sichern | Wählen Sie Sichern. | Ihre Daten werden gesichert. |  |
| 9 | Ein quantitatives Stammprüfmerkmal erstellen | Öffnen Sie im SAP Fiori Launchpad Stammprüfmerkmal anlegen: Einstiegssicht, und geben Sie folgende Daten ein:Werk: <Nummer des Werks>Stammprüfmerkmal: z.B. YQUANT01Gültig ab: <aktuelles Datum>und wählen Sie Stammprüfmerkmal. | Das Bild Stammprüfmerkmal anlegen: Allgemeine Daten wird angezeigt. |  |
| 10 | Allgemeine Daten für quantitative Prüfmerkmale eingeben | Geben Sie in Stammprüfmerkmal anlegen: Allgemeine Daten folgende Daten ein:Quantitatives Prüfmerkmal: markiertKurztext: z.B. LängeSuchfeld: z.B. LängeStatus: 2 FreigegebenWählen SieFreigegeben und Referenzmerkmal.Wählen Sie Enter. | Das Fenster Steuerkennzeichen Merkmal bearbeiten wird angezeigt.ReferenzmerkmaleWenn Sie das Stammprüfmerkmal in einem Arbeitsplan oder einer Materialspezifikation verwenden, wird zuerst ein Verweis auf dieses Merkmal angelegt. Sie können diesen Verweis jedoch zurücknehmen und die Daten einzeln ändern, zum Beispiel für Toleranzen.Vollständige KopiervorlageWenn Sie das Stammprüfmerkmal in einem Arbeitsplan verwenden, kann es nur in einer Kopiervorlage verwendet werden. Diese Art von Stammprüfmerkmal kann nicht in einer Materialspezifikation verwendet werden.Unvollständige KopiervorlageWenn Sie das Stammprüfmerkmal in einem Arbeitsplan verwenden, kann es nur in einer Kopiervorlage verwendet werden. Diese Art von Stammprüfmerkmal kann nicht in einer Materialspezifikation verwendet werden. |  |
| 11 | Steuerkennzeichen für quantitative Prüfmerkmale bearbeiten | Markieren Sie in Steuerkennzeichen Merkmal bearbeiten die folgenden Optionen:Unterer GrenzwertOberer GrenzwertStichprobenverfahrenSumm. ErfassungMussmerkmalWählen Sie Weiter und markieren Sie diese zusätzlichen Optionen:Umfang festKeine DokumentationMesswerte erfassenÄnder.Beleg EEWählen Sie Weiter. |  |  |
| 12 | Sollwert eingeben | Geben Sie im Bild Toleranzschlüssel folgende Daten ein:Sollwert: z.B. 150Und wählen Sie Weiter. |  |  |
| 13 | Quantitative Daten eingeben | Geben Sie im Bild Quantitative Daten folgende Daten ein:Nachkommastellen: z.B. 2Maßeinh.: z. B. cmUntergrenze: z.B. 100Obergrenze: z.B. 200Wählen Sie Weiter. |  |  |
| 14 | Daten sichern | Wählen Sie Sichern. | Ihre Daten werden gesichert. |  |
| 15 | Fehlererfassung für ein bereits vorhandenes Stammprüfmerkmal aktivieren (optional) | Öffnen Sie die App Stammprüfmerkmal ändern(QS23), und öffnen Sie das Stammprüfmerkmal, das Sie ändern möchten.Wählen Sie Steuerkennzeichen.Aktivieren Sie im Dialogfenster Steuerkennzeichen Merkmal bearbeiten die Option Fehlererfassung im Abschnitt Ergebnisrückmeldung, und wählen Sie Weiter.Wählen Sie erneut Weiter . |  |  |
| 16 | Prüfkataloge zuordnen (optional) | Wählen Sie im Bereich Allgemeine Daten die Drucktaste Kataloge. | Das Dialogfenster Zugeordnete Prüfkataloge wird angezeigt. |  |
| 17 | Fehlercodes für Ablehnung bearbeiten (optional) | Suchen Sie im Dialogfenster Zugeordnete Prüfkataloge unter Fehlercodes für Ablehnung nach einer Codegruppe oder einem Code für einen allgemeinen Verstoß bzw. die Verletzung einer Ober- oder Untergrenze, und tragen Sie diese(n) ein.Wählen Sie Weiter. |  |  |
| 18 | Daten sichern | Wählen Sie Sichern. | Ihre Daten werden gesichert. |  |

### Stammprüfmerkmal mit Verweis auf das Klassenmerkmal anlegen (optional)

Testverwaltung

Kundenprojekt: Füllen Sie die projektbezogenen Teile aus.

|  |  |  |  |
| --- | --- | --- | --- |
| Testfall-ID | <X.XX> | Testdatum: |  |
| Testername: |  | Dauer: |  |
| Benutzerrolle(n): |  | Zuständigkeit: | <Geben Sie den Serviceanbieter, einen Kunden oder einen Serviceanbieter zusammen mit einem Kunden an.> |

Verwendungszweck

Die Verknüpfung zwischen Stammprüfmerkmalen und Klassenmerkmalen ermöglicht die automatische Übergabe der Prüfergebnisse an die Chargenklassifizierung, vorausgesetzt, dass Sie eine Prüfung mit Arbeitsplan durchführen. Die Klassenmerkmale der Chargenklasse werden beim Prüfabschluss auf Grundlage der Prüfergebnisse automatisch bewertet.

Wenn Sie ein Klassenmerkmal eingeben und es mit einem Stammprüfmerkmal verknüpfen, werden bestimmte Steuerkennzeichen und Werte dieses Klassenmerkmals in das Stammprüfmerkmal übertragen.

Durch die Verknüpfung von Stammprüfmerkmalen mit Klassenmerkmalen können Sie die Ergebnisse einer Qualitätsprüfung in die Chargenklassifizierung übertragen.

|  |
| --- |
| Hinweis Es ist immer nur eine 1:1-Beziehung zwischen Klassenmerkmal und Stammprüfmerkmal möglich. (Das heißt, Sie können nicht dasselbe Klassenmerkmal mit mehreren Stammprüfmerkmalen verknüpfen.) Das Klassenmerkmal wird auf Mandantenebene definiert und das Stammprüfmerkmal auf Werksebene. Bei Verwendung der Chargenbewertung für mehrere Werke ist es daher obligatorisch, werksspezifische Klassenmerkmale zu definieren und mit den jeweiligen Stammprüfmerkmalen auf Werksebene zu verknüpfen. |

Voraussetzungen

Die Voraussetzungen für die Verknüpfung von Stammprüfmerkmal und Klassenmerkmal müssen erfüllt sein, siehe Kapitel Voraussetzungen/Situation für 2ZW.

Vorgehensweise

| Testschrittnummer | Bezeichnung des Testschritts | Anweisungen | Erwartetes Ergebnis | Kommentare |
| --- | --- | --- | --- | --- |
| 1 | Anmelden | Melden Sie sich am SAP Fiori Launchpad als Qualitätsplaner an. | Das SAP Fiori Launchpad wird angezeigt. |  |
| 2 | SAP-Fiori-App aufrufen | Öffnen Sie Stammprüfmerkmal anlegen(QS21). | Das Bild Stammprüfmerkmal anlegen: Einstieg wird angezeigt. |  |
| 3 | Werksdaten eingeben | Geben Sie auf dem Bild Stammprüfmerkmal anlegen: Einstieg die folgenden Daten ein:Werk: <Nummer des Werks>Stammprüfmerkmal: <Wert>Gültig ab: <aktuelles Datum>Klassenmerkmal: WertWählen Sie Stammprüfmerkmal. | Das Bild Stammprüfmerkmal anlegen: Allgemeine Daten wird angezeigt. |  |
| 4 | Schritte 10-14 des vorherigen Kapitels ausführen | Hinweis Das Stammprüfmerkmal muss ein Bezugsmerkmal sein.Einige Daten werden aus dem Klassenmerkmal in das Stammprüfmerkmal übernommen. Außerdem können, in Abhängigkeit von den Einstellungen des Klassenmerkmals, einige Steuerkennzeichen des Stammprüfmerkmals nicht geändert werden. | Ein quantitatives Stammprüfmerkmal mit Verweis auf das Klassenmerkmal wird angelegt. |  |
| 5 | Chargenmerkmale nach der Qualitätsprüfung überprüfen (optional) | Legen Sie entweder manuell oder per Warenbewegung ein Prüflos an, führen Sie die Qualitätsprüfung durch, und treffen Sie den Verwendungsentscheid.Um Chargenmerkmale zu überprüfen, melden Sie sich am SAP Fiori Launchpad als Qualitätstechniker an, rufen die SAP-Fiori-App Chargen verwalten(F2462) oder Batch Information Cockpit(BMBC) auf und prüfen unter Klassifizierung die Merkmale. | Die Daten der Qualitätsprüfung wurden an das Chargenmerkmal übergeben. |  |

### Stichprobenplan anlegen (optional)

Testverwaltung

Kundenprojekt: Füllen Sie die projektbezogenen Teile aus.

|  |  |  |  |
| --- | --- | --- | --- |
| Testfall-ID | <X.XX> | Testdatum: |  |
| Testername: |  | Dauer: |  |
| Benutzerrolle(n): |  | Zuständigkeit: | <Geben Sie den Serviceanbieter, einen Kunden oder einen Serviceanbieter zusammen mit einem Kunden an.> |

Verwendungszweck

Sie können optional einen Stichprobenplan anlegen. Ein Stichprobenplan ist eine Sammlung von Stichprobenanweisungen. Eine Stichprobenanweisung definiert die Menge an zu prüfenden Stichproben (Stichprobenumfang) als Funktion des Losumfangs. Darüber hinaus können Kriterien für die Annahme oder Ablehnung einer Stichprobe festgelegt werden (z.B. ausgehend von der aktuellen Prüfschärfe). Die Prüfschärfe legt fest, ob eine normale, reduzierte oder verschärfte Prüfung durchzuführen ist, sodass ein Qualitätsplaner den Prüfaufwand für die aktuell vorliegende Qualität flexibel anpassen kann (z.B. weniger Prüfungen, geringerer Stichprobenumfang oder höhere Annahmekriterien, wenn die aktuelle Qualität gut ist).

Vorgehensweise

| Testschrittnummer | Bezeichnung des Testschritts | Anweisungen | Erwartetes Ergebnis | Kommentare |
| --- | --- | --- | --- | --- |
| 1 | Anmelden | Melden Sie sich am SAP Fiori Launchpad als Qualitätsplaner an. | Die Startseite wird angezeigt. |  |
| 2 | SAP-Fiori-App aufrufen | Wählen Sie Stichprobenplan anlegen(QDP1). | Die Sicht Stichprobenplan anlegen: Einstieg wird angezeigt. |  |
| 3 | Stichprobenbezeichnung für Stichprobenplan eingeben | Geben Sie eine Stichprobenbezeichnung für den Stichprobenplan ein.Stichprobenplan: zum Beispiel QM2Wählen Sie Weiter. | Die Sicht Stichprobenplan anlegen: Kopfdaten wird angezeigt. |  |
| 4 | Kopfdaten eingeben | Geben Sie folgende Daten ein, bzw. wählen Sie eine der Optionen aus:Stichprobenplan: z.B. Stichprobenplan für Schärfe(Attr.)Bewertungsparameter: z.B. AttributprüfungStichprobentabelle für: z.B. PrüfschärfeWählen Sie Weiter. | Die Sicht Stichprobenplan anlegen: Parameter wird angezeigt. |  |
| 5 | Parameter für die Prüfschärfe Parameter | Nehmen Sie im Dialogfenster Stichprobenplan anlegen: Parameter die folgende Suche und die folgenden Eingaben vor:Prüfschärfe: z.B. 002(reduzierte Prüfung)Tipp Die Prüfschärfe legt fest, ob eine normale, reduzierte oder verschärfte Prüfung auszuführen ist. Ein Qualitätsplaner kann so den Prüfaufwand flexibel anpassen, z.B. weniger Prüfungen, geringerer Stichprobenumfang, oder höhere Annahmekriterien, wenn die aktuelle Qualität gut ist.Wählen Sie Auswählen. | Die Sicht Stichprobenplan anlegen: Stichprobentabelle wird angezeigt. |  |
| 6 | Stichprobenanweisungen anlegen | Geben Sie in der Tabelle Stichprobenanweisungen folgende Daten ein:Losumfang: z.B. 10.Stichprobenumfang: z.B. 1.Annahmezahl 1: z.B. 0.Rückweisezahl 1: z.B. 1.Losumfang: z.B. 100.Stichprobenumfang: z.B. 2.Annahmezahl 1: z.B. 0.Rückweisezahl 1: z.B. 1.Losumfang: z.B. 1000.Stichprobenumfang: z.B. 5.Annahmezahl 1: z.B. 0.Rückweisezahl 1: z.B. 1.Losumfang: z.B. 10000000000.Stichprobenumfang: z.B. 50.Annahmezahl 1: z.B. 0.Rückweisezahl 1: z.B. 1. | Eine Stichprobenanweisung wird angelegt.Annahmezahl N: Die maximale Anzahl fehlerhafter Einheiten oder Fehler, die für die Annahme von Los oder Attribut toleriert werden.Rückweisezahl N: Die Mindestanzahl fehlerhafter Einheiten oder Fehler, die zu einer Rückweisung des Loses oder Attributs führen.Nicht vergessen Befindet sich die Anzahl fehlerhafter Einheiten oder Fehler zwischen den Annahme- und Rückweisungsgrenzwerten, ermittelt das System die nächste Strichprobenanweisung. |  |
| 7 | Andere Tabelle anlegen | Wählen Sie in der Sicht Stichprobenplan anlegen: Stichprobentabelle die Option Andere Tabelle (oder Umschalttaste + F5). | Das Dialogfenster Stichprobenplan anlegen: Parameter wird angezeigt. |  |
| 8 | Parameter für die Prüfschärfe Parameter | Geben Sie im Dialogfenster Stichprobenplan anlegen: Parameter die folgenden Werte ein:Prüfschärfe: z.B. 004 (normale Prüfung).Wählen Sie Auswählen. | Die Sicht Stichprobenplan anlegen: Stichprobentabelle wird angezeigt. |  |
| 9 | Stichprobenanweisungen anlegen | Geben Sie in der Tabelle Stichprobenanweisungen folgende Daten ein:Losumfang: z.B. 10.Stichprobenumfang: z.B. 1.Annahmezahl 1: z.B. 0.Rückweisezahl 1: z.B. 1.Losumfang: z.B. 100.Stichprobenumfang: z.B. 5.Annahmezahl 1: z.B. 0.Rückweisezahl 1: z.B. 1.Losumfang: z.B. 1000.Stichprobenumfang: z.B. 10.Annahmezahl 1: z.B. 0.Rückweisezahl 1: z.B. 1.Losumfang: z.B. 10000000000.Stichprobenumfang: z.B. 100.Annahmezahl 1: z.B. 0.Rückweisezahl 1: z.B. 1. | Die nächste Stichprobenanweisung wird angelegt. |  |
| 10 | Andere Tabelle anlegen | Wählen Sie in der Sicht Stichprobenplan anlegen: Stichprobentabelle die Option Andere Tabelle (oder Umschalttaste + F5). | Das Dialogfenster Stichprobenplan anlegen: Parameter wird angezeigt. |  |
| 11 | Parameter für die Prüfschärfe Parameter | Geben Sie im Dialogfenster Stichprobenplan anlegen: Parameter die folgenden Werte ein:Prüfschärfe: z.B. 006 (verschärfte Prüfung).Wählen Sie Auswählen. | Die Sicht Stichprobenplan anlegen: Stichprobentabelle wird angezeigt. |  |
| 12 | Stichprobenanweisungen anlegen | Geben Sie in der Tabelle Stichprobenanweisungen folgende Daten ein:Losumfang: z.B. 10.Stichprobenumfang: z.B. 2.Annahmezahl 1: z.B. 0.Rückweisezahl 1: z.B. 1.Losumfang: z.B. 100.Stichprobenumfang: z.B. 10.Annahmezahl 1: z.B. 0.Rückweisezahl 1: z.B. 1.Losumfang: z.B. 1000.Stichprobenumfang: z.B. 25.Annahmezahl 1: z.B. 0.Rückweisezahl 1: z.B. 1.Losumfang: z.B. 10000000000.Stichprobenumfang: z.B. 200.Annahmezahl 1: z.B. 0.Rückweisezahl 1: z.B. 1. | Die nächste Stichprobenanweisung wird angelegt. |  |
| 13 | Daten sichern | Zum Sichern Ihrer Daten wählen Sie Sichern. | Der Stichprobenplan wird angelegt. |  |

### Stichprobenverfahren anlegen (optional)

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
| 1 | Anmelden | Melden Sie sich am SAP Fiori Launchpad als Qualitätsplaner an. | Die Startseite wird angezeigt. |  |
| 2 | SAP-Fiori-App aufrufen | Wählen Sie Stichprobenverfahren anlegen(QDV1). | Das Bild Stichprobenverfahren anlegen: Einstieg wird angezeigt. |  |
| 3 | Namen des Stichprobenverfahrens eingeben | Geben Sie den Namen eines Stichprobenverfahrens ein, z.B. YPERCIN1.Wählen Sie Weiter. | Ein neues Fenster wird angezeigt. |  |
| 4 | Daten des Stichprobenverfahrens eingeben | Geben Sie Daten für das Stichprobenverfahren ein:Geben Sie eine Beschreibung ein, z. B. 10%-Prüfung ohne PrüfpunkteStichprobenart: z.B. Prozentuale StichprobeBewertungsmodus: z. B. Bewertung mit AusprägungscodePrüfpunkte: z. B. Ohne Prüfpunkte wählenVerwendungskennzeichen: Lassen Sie das Feld Verwendung gesperrt leer.Wählen Sie Weiter. | Die Findungsregel wird definiert.Hinweis Zur Verwendung von Stichprobenplänen müssen Sie im Feld Probenart Stichprobenplan verwenden auswählen. Dann können Sie den Stichprobenplan zuordnen, den Sie im vorherigen Verfahren angelegt haben. |  |
| 5 | Stichprobenanweisung pflegen | Wählen Sie Stichprobe, und geben Sie folgende Daten ein:StichprProzentsatz: z.B. 10Wählen Sie Weiter.Wählen Sie Sichern. | Ihre Daten werden gesichert. |  |

### Dynamisierungsregel erstellen (optional)

Testverwaltung

Kundenprojekt: Füllen Sie die projektbezogenen Teile aus.

|  |  |  |  |
| --- | --- | --- | --- |
| Testfall-ID | <X.XX> | Testdatum: |  |
| Testername: |  | Dauer: |  |
| Benutzerrolle(n): |  | Zuständigkeit: | <Geben Sie den Serviceanbieter, einen Kunden oder einen Serviceanbieter zusammen mit einem Kunden an.> |

Verwendungszweck

Anlegen einer Dynamisierungsregel.

Vorgehensweise

| Testschrittnummer | Bezeichnung des Testschritts | Anweisungen | Erwartetes Ergebnis | Kommentare |
| --- | --- | --- | --- | --- |
| 1 | Anmelden | Melden Sie sich am SAP Fiori Launchpad als Qualitätsplaner an. | Die Startseite wird angezeigt. |  |
| 2 | SAP-Fiori-App aufrufen | Öffnen Sie Dynamisierungsregel anlegen(QDR1). | Das Bild Dynamisierungsregel erstellen: Einstieg wird angezeigt. |  |
| 3 | Dynamisierungsregelnamen eingeben | Geben Sie einen Dynamisierungsregelnamen ein, z.B. QM1. | Das Bild Dynamisierungsregel erstellen: Kopfdaten wird angezeigt. |  |
| 4 | Kopfdaten eingeben | Machen Sie folgende Eingaben:Kurztext: Beispiel: Prüfung/ÜberspringenFür Verwendungsentscheid: markiertReset-Zeitraum in Tagen: z.B. 90Wählen Sie Nächstes Bild. | Das Bild Dynamisierungsregel erstellen: Prüfstufen wird angezeigt. |  |
| 5 | Daten für Prüfstufe 10 eingeben | Geben Sie in der ersten Zeile folgende Daten ein:Stufe: 10Schärfe: 2Schärfe Stufe: markiertKurztext: Erstinspektion |  |  |
| 6 | Daten für Prüfstufe 20 eingeben | Geben Sie in der zweiten Zeile folgende Daten ein:Stufe: 20Schärfe: leer lassenÜberspringen: markiertKurztext: Überspringen |  |  |
| 7 | Daten für Prüfstufe 30 eingeben | Geben Sie in der dritten Zeile folgende Daten ein:Stufe: 30Schärfe: 4Kurztext: Z. B. <Normale Prüfung> |  |  |
| 8 | Stufenwechsel für Prüfstufe 10 pflegen | Klicken Sie auf Prüfstufe 10 und wählen Sie Stufenwechsel.Geben Sie auf dem Bild Stufenwechsel anlegen folgende Daten ein:OKAnzahl Prüfungen: 1Neue Prüf Stufe: 20Nicht OKAbweisungen: 1Neue Prüf Stufe: 30 | Die Einträge sind in der Tabelle angegeben. |  |
| 9 | Stufenwechsel für Prüfstufe 20 pflegen (Skip) | Klicken Sie auf Prüfstufe 20, und wählen Sie Stufenwechsel.Geben Sie auf dem Bild Stufenwechsel anlegen folgende Daten ein:OKAnzahl Skips: 1Maximale Skipdauer: 90Neue Prüf Stufe: 30Nicht OKAbweisungen: 1Neue Prüf stufe: 30 | Die Einträge sind in der Tabelle angegeben. |  |
| 10 | Stufenwechsel für Prüfstufe 30 pflegen | Klicken Sie auf Prüfstufe 30 und wählen Sie Stufenwechsel.Geben Sie auf dem Bild Stufenwechsel anlegen folgende Daten ein:OKAnzahl Prüfungen: 1Neue Prüf Stufe: 20Nicht OKAbweisungen: 1Neue Prüf Stufe: 30 | Die Einträge sind in der Tabelle angegeben. |  |
| 11 | Daten sichern | Sichern Sie Ihre Daten. |  |  |

### Prüfplan anlegen

Testverwaltung

Kundenprojekt: Füllen Sie die projektbezogenen Teile aus.

|  |  |  |  |
| --- | --- | --- | --- |
| Testfall-ID | <X.XX> | Testdatum: |  |
| Testername: |  | Dauer: |  |
| Benutzerrolle(n): |  | Zuständigkeit: | <Geben Sie den Serviceanbieter, einen Kunden oder einen Serviceanbieter zusammen mit einem Kunden an.> |

Vorgehensweise

| Testschrittnummer | Bezeichnung des Testschritts | Anweisungen | Erwartetes Ergebnis | Kommentare |
| --- | --- | --- | --- | --- |
| 1 | Anmelden | Melden Sie sich am SAP Fiori Launchpad als Qualitätsplaner an. | Die Startseite wird angezeigt. |  |
| 2 | SAP-Fiori-App aufrufen | Öffnen Sie die Kachel Prüfplan anlegen(QP01). | Prüfplan anlegen (Einstieg) wird angezeigt. |  |
| 3 | Daten eingeben | Geben Sie auf dem Bild Prüfplan anlegen (Einstieg) die folgenden Daten ein:Material: <Ihre Materialnummer>, z.B. QM001Werk: <Nummer des Werks>Stichtag: z.B. heuteWählen Sie Weiter. | Das Bild Prüfplan anlegen: Kopfdetails wird angezeigt, wenn für die angegebene Material-Werk-Kombination kein Plan verfügbar ist.Hinweis Wenn ein Plan aber verfügbar ist, wählen Sie eine Gruppe aus dem Dialogfenster aus, und Prüfplan anlegen: Planübersicht wird angezeigt. Wählen Sie Neue Einträge, um einen neuen Prüfplan anzulegen. |  |
| 4 | Kopfdaten verwalten | Prüfplan anlegen (Kopfdaten) wird angezeigt. Geben Sie folgende Daten ein:Verwendung: Wählen Sie aus der Wertehilfeliste für den Verwendungszweck z.B. 5 Wareneingang.Status: Wählen Sie aus der Wertehilfeliste z.B. 4 Freigegeben allgemein.Losumfang: Von 1 bis 99.999, z.B. 999 StückDynamisierung Ebene (optional): 1 Dynamisierung auf PartienebeneHinweis Diese Daten sind nur notwendig, wenn Sie Dynamisierungsregeln verwendenDynamisierungsregel (optional): <Ihre Daten>Hinweis Diese Daten sind nur notwendig, wenn Sie Dynamisierungsregeln verwendenDynamisierungskriterium (optional): z. B. Lieferant und HerstellerHinweis Diese Daten sind nur notwendig, wenn Sie Dynamisierungsregeln verwendenWählen Sie Vorgänge. | Prüfplan anlegen: Vorgangsübersicht wird angezeigt. |  |
| 5 | Vorgangsdaten eingeben (Übersicht) | Geben Sie auf dem Bild Prüfplan anlegen: Vorgangsübersicht folgende Daten ein:Vorgangsnummer: z.B. 0010Arbeitsplatz: Wählen Sie einen Arbeitsplatz, z.B. QMLABS.Steuerschlüssel: Wählen Sie einen Steuerschlüssel, z.B. QM01.Beschreibung: Geben Sie eine Beschreibung ein.Markieren Sie Vorgansposition, und wählen Sie dann Vorgang.Hinweis Ist die Drucktaste Vorgang nicht verfügbar, wählen Sie Mehr > Vorgang. | Prüfplan anlegen: Vorgangsdetails wird angezeigt.Hinweis Der Steuerschlüssel wirkt sich auf die Planung und Bearbeitung von Prüfvorgängen aus, beispielsweise ob ein Prüfmerkmal für einen Prüfvorgang bearbeitet werden muss oder nicht. |  |
| 6 | Vorgangsdaten (Details) | Blättern Sie im Bild Prüfplan anlegen: Vorgangsdetails zur Überprüfung von Erfassungssicht: Einzelwerte und zusammengefasstes Ergebnis (Standardsicht).Wählen Sie Zurück, um zum Bild Vorgangsübersicht zurückzukehren. |  |  |
| 7 | Planprüfmerkmale eingeben | Markieren Sie die Vorgangszeile und wählen Sie Planprüfmerkmal.Weisen Sie Stammprüfmerkmale zu, z.B. ein qualitätsbezogenes Stammprüfmerkmal wie YQUALI01 für ein qualitatives Prüfmerkmal oder ein quantitätsbezogenes wie YQUANTI01 für ein quantitatives Prüfmerkmal.Weisen Sie Stichprobenverfahren (optional) zu, um diese in Kombination mit dem zu prüfenden Merkmal zu verwenden.Dynamisierungsregel zuordnen (optional): z. B. QMIHinweis Eine Dynamisierung kann auf Kopfebene oder auf Prüfmerkmalebene zugeordnet werden.Wählen Sie Enter. | Detailinformationen werden angezeigt. |  |
| 8 | Daten sichern | Wählen Sie Sichern. | Ihre Daten werden gesichert. |  |

### Prüfpläne verwalten

Testverwaltung

Kundenprojekt: Füllen Sie die projektbezogenen Teile aus.

|  |  |  |  |
| --- | --- | --- | --- |
| Testfall-ID | <X.XX> | Testdatum: |  |
| Testername: |  | Dauer: |  |
| Benutzerrolle(n): |  | Zuständigkeit: | <Geben Sie den Serviceanbieter, einen Kunden oder einen Serviceanbieter zusammen mit einem Kunden an.> |

Vorgehensweise

| Testschrittnummer | Testschrittnr. Testschrittname | Anweisung | Erwartetes Ergebnis | Kommentare |
| --- | --- | --- | --- | --- |
| 1 | Anmelden | Melden Sie sich am SAP Fiori Launchpad als Qualitätsplaner an. | Das SAP Fiori Launchpad wird angezeigt. |  |
| 2 | SAP-Fiori-App aufrufen | Öffnen Sie Prüfpläne verwalten(F3788). | Die App wird geöffnet. |  |
| 3 | Daten filtern | Geben Sie auf dem Bild Prüfpläne verwalten (Einstieg) die folgenden Daten ein:Material: <Material>, indem Sie die Filter im Abschnitt Prüfplanversion anpassen).Werk: <Nummer des Werks>Status des Plans: <Gesamtstatus>, z.B. 4 Freigegeben (allgemein)Wählen Sie Start. | Es wird eine Liste der Prüfpläne angezeigt, die die Selektionskriterien erfüllen. |  |
| 4 | Prüfplan auswählen | Wählen Sie den entsprechenden Eintrag aus, und navigieren Sie über die die Drucktaste > auf der rechten Seite der markierten Zeile. | Sie gelangen zum relevanten Prüfplan. |  |
| 5 | Stichtag ändern | Wählen Sie in der App Prüfpläne verwalten(F3788) die Option Stichtag ändern. Ein Dialogfenster wird angezeigt, und Sie können den Stichtag pflegen, indem Sie das Datum eingeben, ab dem die Änderung gültig sein soll:Stichtag: <Datum>Hinweis Der Stichtag wird nur für angelegte oder gelöschte Objekte (z.B. Prüfvorgänge) berücksichtigt, wird jedoch bei Änderungen eventuell nicht berücksichtigt. Änderungen im vorhandenen Objekt werden eventuell sofort angezeigt. | Der Stichtag wird geändert. |  |
| 6 | Allgemeine Daten bearbeiten | Das Bild Prüfpläne verwalten wird mit den Feldern Allgemein, Materialzuordnung, Vorgänge, Anlagen und Verwaltungsdaten angezeigt. Geben Sie folgende Daten ein, um die allgemeinen Daten zu pflegen (wählen Sie Bearbeiten, um die Einträge zu ändern):Werk: Wenn noch kein Wert eingefügt wurde, wählen Sie einen Eintrag aus der Wertehilfe aus.Prüfplanbeschreibung: Ändern Sie die Beschreibung.Verwendung: Wählen Sie aus der Wertehilfeliste für den Verwendungszweck z.B. 5 Wareneingang.Gesamtstatus: Wählen Sie aus der Wertehilfeliste z.B. 4 Freigegeben allgemein.Losgröße: Von 1 bis 99.999, z.B. 999 StückPrüfpunkt (optional): Fügen Sie 101 Zeitbezogen ein, wenn Sie Prüfpunkte zeitabhängig anlegen möchten.Hinweis Die folgenden Daten sind nur notwendig, wenn Sie Dynamisierungsregeln verwenden.Dynamisierung Ebene (optional): 1 Dynamisierung auf PartienebeneHinweis Innerhalb von Dynamisierungsregeln kann entschieden werden, auf welcher Ebene eine Dynamisierung relevant ist.Dynamisierungsregel (optional): <Ihre Daten>Hinweis Die folgenden Daten sind nur notwendig, wenn Sie Dynamisierungsregeln verwenden.Dynamisierungskriterien (optional): z. B. Lieferant und Hersteller | Die allgemeinen Daten des Prüfplans sind gepflegt. |  |
| 7 | Materialzuordnung pflegen | Pflegen Sie die Informationen zur Materialzuordnung in Prüfpläne verwalten (wählen Sie Hinzufügen, um Einträge hinzuzufügen):Material: <Material>Werk: <Nummer des Werks>Lieferant (optional): <Lieferantennummer>Kunde (optional): <Kundennummer>Hinweis Weitere Kriterien können über Einstellungenangezeigt werden. | Die Informationen zur Materialzuordnung des Prüfplans sind gepflegt. |  |
| 8 | Vorgänge pflegen | Pflegen Sie die informationen zum Vorgang in Prüfpläne verwalten (wählen Sie Anlegen, um Einträge anzulegen):Beschreibung des Vorgangs: <Beschreibung>Werk: <Nummer des Werks>Basismenge: <Menge>Mengeneinheit: <Einheit>Hinweis Weitere Kriterien können über Einstellungenangezeigt werden.Navigieren Sie zu den Vorgangsdetails, indem Sie auf der rechten Seite der ausgewählten Zeile die Drucktaste > wählen. | Die Informationen zum Prüfplanvorgang sind gepflegt, und Sie gelangen zur Position. |  |
| 9 | Vorgang pflegen (Übersicht) | Pflegen Sie Allgemeine Daten im Bild Vorgang:Vorgangsnummer: <vom System vergebene Nummer>Steuerschlüssel: <vom System vergeben>Werk: <Nummer des Werks>Beschreibung des Vorgangs: <Beschreibung>Arbeitsplatz (optional): Wählen Sie einen Arbeitsplatz, z.B. QMLABS.Basismenge: <Menge>Mengeneinheit: <Einheit>Umrechnung von Mengeneinheiten von Kopf zu Vorgang.Hinweis Weitere Kriterien können über die Einstellungen für den Prüfpunkt angezeigt werden. | Die allgemeinen Daten des Vorgangs sind gepflegt. |  |
| 10 | Vorgang pflegen (Merkmale) | Wechseln Sie im Bild Vorgang zu Merkmale. Wählen Sie Merkmale zuordnen, um Stammprüfmerkmalsinformationen zu kopieren, oder wählen Sie Hinzufügen, um ein neues Merkmal oder Stammprüfmerkmale hinzuzufügen.Hinweis Auch nach der Auswahl von Hinzufügen ist es möglich, nachträglich einen Bezug zu einem Stammprüfmerkmal hinzuzufügen.Geben Sie Folgendes ein:Beschreibung: <Kurzbeschreibung>Stammprüfmerkmale (optional): <Stammprüfmerkmale>Steuerungskennzeichen: <Steuerungskennzeichen>Hinweis Weitere Kriterien können über die Einstellungen für den Prüfpunkt angezeigt werden.Navigieren Sie zu den Merkmalsdetails, indem Sie auf der rechten Seite die Drucktaste > wählen. | Die Vorgangsmerkmalsinformationen sind gepflegt, und Sie gelangen zum Merkmal. |  |
| 11 | Merkmale pflegen | Die Details des Merkmals werden angezeigt und können bearbeitet werden. Für die Pflege sind eventuell folgende Daten relevant:Hinweis Je nach den Einstellungen für Steuerkennzeichen im vorherigen Schritt können unterschiedliche Felder angezeigt werden.Beschreibung: <Kurzbeschreibung>Merkmalsgewichtung (optional): Wählen Sie aus der Wertehilfeliste z.B. <Gewichtung>.Prüfmethode, Version, Werk (optional): Wählen Sie aus der Wertehilfeliste aus, z.B. <Prüfmethode>.Infofelder (optional): <Weitere Informationen>Auswahlmenge, Werk: Wählen Sie aus der Wertehilfeliste aus, z.B. <Auswahlmenge, qualitative Merkmale>.Dynamisierung für Merkmal (optional): Wählen Sie aus der Wertehilfeliste aus, z.B. <Anderes Merkmal>.Dynamisierungsregel (optional): Wählen Sie aus der Wertehilfeliste aus, z.B. <Dynamisierungsregel>.Hinweis Die Dynamisierungsregel wird nur angezeigt, wenn auf Merkmalsebene dynamisiert wird.Weitere Verwaltungsdaten finden Sie im entsprechenden Bereich.Kehren Sie zu Vorgänge zurück. | Die Merkmalsinformationen sind gepflegt, und Sie gelangen zum Bild Vorgänge. |  |
| 12 | Verwaltungsdatenvorgänge prüfen | Das Bild Vorgänge wird angezeigt und kann bearbeitet werden.Weitere Verwaltungsdaten finden Sie im entsprechenden Bereich.Navigieren Sie zurück zum Prüfplan. | Die Verwaltungsdaten sind verfügbar, und Sie gelangen zum Bild Prüfplan. |  |
| 13 | Anlagen zum Prüfplan hinzufügen | Der Prüfplan wird angezeigt, und Anlagen können bearbeitet werden.Wählen Sie Hinzufügen, um eine URL mit der Beschreibung anzulegen.Wählen Sie Hochladen, um ein Dokument aus dem lokalen Dateisystem einzufügen.Weitere Verwaltungsdaten finden Sie im entsprechenden Bereich.Navigieren Sie zurück zum Prüfplan. | Die Verwaltungsdaten sind verfügbar, und Sie gelangen zum Bild Prüfplan. |  |
| 14 | Daten sichern | Wählen Sie Sichern. | Ihre Daten werden gesichert. |  |

### Aus bestehenden Prüfplänen kopieren

Testverwaltung

Kundenprojekt: Füllen Sie die projektbezogenen Teile aus.

|  |  |  |  |
| --- | --- | --- | --- |
| Testfall-ID | <X.XX> | Testdatum: |  |
| Testername: |  | Dauer: |  |
| Benutzerrolle(n): |  | Zuständigkeit: | <Geben Sie den Serviceanbieter, einen Kunden oder einen Serviceanbieter zusammen mit einem Kunden an.> |

Vorgehensweise

| Testschrittnummer | Bezeichnung des Testschritts | Anweisungen | Erwartetes Ergebnis | Kommentare |
| --- | --- | --- | --- | --- |
| 1 | Anmelden | Melden Sie sich als Qualitätsplaner am SAP Fiori Launchpad an. | Die Startseite wird angezeigt. |  |
| 2 | SAP-Fiori-App aufrufen | Öffnen Sie Prüfpläne verwalten(F3788). | Prüfpläne verwalten (Einstieg) wird angezeigt. |  |
| 3 | Daten in Erstansicht filtern | Geben Sie auf dem Bild Prüfpläne verwalten (Einstieg) die folgenden Daten ein:Material: <Material>, indem Sie die Filter im Abschnitt Prüfplanversion anpassen.Werk: <Nummer des Werks>Status des Plans: <Gesamtstatus>, z.B. 4 Freigegeben (allgemein)Wählen Sie Starten. | Es wird eine Liste der Prüfpläne angezeigt, die die Selektionskriterien erfüllen. |  |
| 4 | Prüfplan in der gefilterten Sicht auswählen | Wählen Sie den entsprechenden Eintrag aus, und navigieren Sie über die die Drucktaste ">" auf der rechten Seite der markierten Zeile. | Der relevante Prüfplan wurde eingegeben. |  |
| 5 | Aus bestehendem Plan kopieren (Anfang) | Prüfpläne verwalten wird angezeigt. Wählen Sie Aus bestehenden Plänen kopieren.Fügen Sie im Dialogfenster Aus bestehenden Plänen kopieren eventuell einige Daten ein, oder wählen Sie sofort OK:Werk: <Nummer des Werks>, wählen Sie einen Eintrag aus der Wertehilfe aus.Plangruppe und Plangruppenzähler: <ID des Plans>, wählen Sie einen Eintrag aus der Wertehilfe aus.Gesamtstatus: <Status>, wählen Sie aus der Wertehilfeliste z.B. 4 Freigegeben allgemein.Gültigkeitsbeginn: Wählen Sie einen Eintrag aus der Wertehilfe aus.Hinweis Weitere Kriterien können unter "Filter anpassen" angezeigt werden. | Der Nebenbereich Aus bestehenden Plänen kopieren wird angezeigt. |  |
| 6 | Aus bestehendem Plan kopieren (Kopie) | Im Nebenbereich Aus bestehenden Plänen kopieren werden die Pläne gemäß den zuvor ausgewählten Filtern angezeigt. Über die Drucktaste ">" vor jeder Zeile können die Objekte der Pläne komprimiert werden:Plan > Materialien > VorgängeInnerhalb von Materialien kann ein Material ausgewählt werden, und mit Option Kopieren wird der markierte Eintrag in den aktuellen Prüfplan übernommen.Sie können innerhalb von Vorgängen einen oder mehrere Vorgänge auswählen und mit der Option Kopieren in den Prüfplan übernehmen.Vorgang > MerkmaleInnerhalb von Merkmalen, die einem einzelnen Vorgang zugeordnet sind, können Sie ein oder mehrere Merkmale auswählen und über Kopieren in einen frei verwendbaren Vorgang übernehmen. Es ist auch möglich, einen Vorgang und ein oder mehrere zugehörige Merkmale zu markieren, um den Vorgang einschließlich der markierten Merkmale zu kopieren.Hinweis Das Kopieren aus vorhandenen Plänen ist auch innerhalb der Vorgangs- und Merkmalsübersicht in der App Prüfpläne verwalten möglich. | Der Nebenbereich Aus bestehenden Plänen kopieren wird angezeigt. |  |
| 7 | Daten sichern | Wählen Sie Sichern. | Ihre Daten werden gesichert. |  |

### Offene Prüflose anzeigen

Testverwaltung

Kundenprojekt: Füllen Sie die projektbezogenen Teile aus.

|  |  |  |  |
| --- | --- | --- | --- |
| Testfall-ID | <X.XX> | Testdatum: |  |
| Testername: |  | Dauer: |  |
| Benutzerrolle(n): |  | Zuständigkeit: | <Geben Sie den Serviceanbieter, einen Kunden oder einen Serviceanbieter zusammen mit einem Kunden an.> |

Zweck

Das Prüflos wird für die Erfassung der Ergebnisse des Prüfvorgangs verwendet. In diesem optionalen Schritt werden die Bezüge verifiziert und der für die Qualitätsprüfung verwendete Stichprobenumfang wird überprüft. Die Probeziehanweisung kann gedruckt werden.

Voraussetzungen

Das Prüflos wird angelegt.

Vorgehensweise

| Testschrittnummer | Bezeichnung des Testschritts | Anweisungen | Erwartetes Ergebnis | Bestanden/Nicht bestanden/Anmerkung |
| --- | --- | --- | --- | --- |
| 1 | Anmelden | Melden Sie sich als Qualitätstechniker am SAP Fiori Launchpad an. | Das SAP Fiori Launchpad wird angezeigt |  |
| 2 | SAP-Fiori-App aufrufen | Öffnen Sie Prüflose verwalten(F2343). | Das Bild Prüflose verwalten wird angezeigt. |  |
| 3 | Filterfelder eingeben | Geben Sie Filter ein, und wählen Sie Start. | Wenn relevante Referenzen (z.B. Bestellung oder Produktionsauftrag) nicht in den Filtern angezeigt werden, wählen Sie Filter anpassen. Suchen Sie im Dialogfenster Filter anpassen den Eintrag Beschaffung oder Produktion, und wählen Sie Mehr Filter. Wählen Sie das entsprechende Dokument aus, und wählen Sie OK. Wählen Sie Starten. |  |
| 4 | Prüflos auswählen | Wählen Sie in der Prüflosliste das Prüflos aus, das Sie zuvor angelegt haben. | Das Prüflos wird angezeigt. |  |
| 5 | Probeziehanweisung drucken | Wählen Sie Probeziehanweisung drucken.Wählen Sie ein Ausgabeelement für den Druck aus, duplizieren Sie möglicherweise eins, und wählen Sie Ausgabe senden.Hinweis Wenn der Druck für ein Prüflos bereits erzeugt wurde, zeigt das Dialogfenster Ausgabedetails eine Liste der zuvor gedruckten Ausgabepositionen an. | Das Dialogfenster Ausgabedetails wird geöffnet und zeigt eine Liste der Ausgabepositionen mit den konfigurierten Druck- und E-Mail-Kanälen an. Ein PDF-Dokument mit der Probeziehanweisung wird ausgelöst und an die Anwendung "Druckwarteschlangen pflegen" zum Drucken gesendet. |  |
| 6 | Probeziehanweisung per E-Mail senden | Wählen Sie Probeziehanweisung drucken.Wählen Sie eine Ausgabeposition für E-Mail, und wählen Sie Ausgabe senden. | Eine E-Mail mit der PDF wird an die vorgesehenen Empfänger gesendet. |  |

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
> Flagged while digesting this document, not verified: Source title extracted as 'Verwendungszweck' (first heading) rather than the real title; document is in German.

> [!warning] Conflict
> Flagged while digesting this document, not verified: Unfilled placeholders (<X.XX>, test case fields) are template content, not data.

> [!warning] Conflict
> Flagged while digesting this document, not verified: Description of Vollständige/Unvollständige Kopiervorlage differs between qualitative (step 4) and quantitative (step 10) sections, possibly a template inconsistency.

## Connections
- part-of :: [[_cluster]]
- related-to :: [[13-quality-ehs-and-compliance/master-data-script-create-quality-inspection-plan-mds-bnq-653]]
- related-to :: [[13-quality-ehs-and-compliance/sap-s-4hana-cloud-public-edition-mds-bnq-655]]
- related-to :: [[13-quality-ehs-and-compliance/sap-s-4hana-cloud-public-edition-mds-bnq-657]]
- related-to :: [[13-quality-ehs-and-compliance/script-de-dados-mestre-criar-plano-de-controle-de-qualidade-mds-bnq-65]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/BNQ_S4CLD2608_Master_Data_DE_XX.docx` — full document · extracted with `mammoth` · 58,443 chars in the whole document
