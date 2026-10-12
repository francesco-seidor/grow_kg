---
id: 11-inventory-warehouse-and-transportation/stammdatenskript-lagerplatze-und-fixplatzzuordnungen-pflegen-sds-3kr-3
title: "Stammdatenskript: Lagerplätze und Fixplatzzuordnungen pflegen – SDS (3KR) (3KR_S4CLD2608_Master_Data_DE_XX)"
description: "German master data script (3KR) for SAP S/4HANA Cloud Public Edition: create, change, display, mass-change storage bins and assign fixed bins in EWM."
cluster: 11-inventory-warehouse-and-transportation
tags: [kb/inventory-warehouse-and-transportation, topic/ewm-storage-bins]
aliases: [3KR_S4CLD2608_Master_Data_DE_XX]
keywords: [EWM Storage Bins and Fixed Bin Assignments, storage bins, fixed bin assignment, bin mass change, warehouse master data, extended warehouse management, business partners, warehouse clerk role, master data scripts, 3KR]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/3KR_S4CLD2608_Master_Data_DE_XX.docx]
confidence: high
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-334
topic: 11-inventory-warehouse-and-transportation/ewm-storage-bins
language: DE
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Stammdatenskript: Lagerplätze und Fixplatzzuordnungen pflegen – SDS (3KR) (3KR_S4CLD2608_Master_Data_DE_XX)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/3KR_S4CLD2608_Master_Data_DE_XX.docx`, extracted with `mammoth`. Grouped under **EWM Storage Bins and Fixed Bin Assignments** in Inventory, Warehouse and Transportation. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

| <!-- image omitted: unnamed --> | StammdatenskriptSAP S/4HANA Cloud Public Edition - 02-07-26 |
| --- | --- |
|  | Lagerplätze und Fixplatzzuordnungen pflegen – SDS (3KR) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Inhaltsverzeichnis

[1 Zweck 2](#_Toc233889647)

[2 Voraussetzungen 3](#_Toc233889648)

[2.1 Systemzugriff 3](#_Toc233889649)

[2.2 Rollen 3](#_Toc233889650)

[2.3 Erforderliche Organisationseinheiten 3](#_Toc233889651)

[2.4 Obligatorische und optionale Stammdaten 4](#_Toc233889652)

[3 Übersichtstabelle 5](#_Toc233889653)

[4 Testverfahren 6](#_Toc233889654)

[4.1 Lagerplätze anlegen 6](#_Toc233889655)

[4.2 Lagerplätze ändern 7](#_Toc233889656)

[4.3 Lagerplätze anzeigen 8](#_Toc233889657)

[4.4 Massenänderung an Lagerplätzen durchführen 9](#_Toc233889658)

[4.5 Fixplätze zuordnen 10](#_Toc233889659)

## Zweck

In diesem Dokument lernen Sie, wie Sie die folgenden Aktivitäten zum Anlegen von Lagerplätzen und Fixplatzzuordnungen ausführen:

- [Lagerplätze anlegen](#unique_2) [Seite ] 6
- [Lagerplätze ändern](#unique_3) [Seite ] 7
- [Lagerplätze anzeigen](#unique_4) [Seite ] 8
- [Massenänderung an Lagerplätzen durchführen](#unique_5) [Seite ] 9
- [Fixplätze zuordnen](#unique_6) [Seite ] 10

Die Beschreibung umfasst die Datensegmente, die für die Stammdaten für die Arbeit in einer normalen Systemumgebung relevant sind. Sie lernen hauptsächlich, welche Datensegmente und -felder üblicherweise mit Eingabewerten gefüllt werden müssen. Felder, die für den von SAP Best Practices bereitgestellten Umfang der Content-Auslieferung in SAP S/4HANA nicht relevant sind, werden in diesem Dokument nicht behandelt, obwohl sie möglicherweise auf dem Bild angezeigt werden.

Sie können diese Stammdaten für alle Warehouse-Management-Geschäftsprozesse verwenden.

## Voraussetzungen

### Systemzugriff

| System | Details |
| --- | --- |
| System | Zugriff über das SAP Fiori Launchpad möglich. Ihr Systemadministrator stellt Ihnen die URL für den Zugriff auf die verschiedenen Apps zur Verfügung, die Ihrer Rolle zugeordnet sind. |

### Rollen

Legen Sie Benutzerrollen mit den folgenden von SAP ausgelieferten Benutzerrollenvorlagen an, und ordnen Sie sie Ihren einzelnen Testbenutzern zu.

Alternativ können Sie, falls verfügbar, die folgenden von SAP ausgelieferten Bereiche verwenden. Legen Sie einen Bereich mit Seiten an, die vordefinierte grundlegende Apps enthalten, und ordnen Sie sie der Benutzerrolle zu. Anschließend ordnen Sie diese Benutzerrolle Ihren einzelnen Benutzern zu.

Weitere Informationen finden Sie unter Anwendungsrolle aus einer Vorlage anlegen in der [Product Assistance](https://help.sap.com/docs/SAP_S4HANA_CLOUD/53e36b5493804bcdb3f6f14de8b487dd/ec310a8b669a45ca898dc4dd91d97de2.html) für SAP S/4HANA Cloud Public Edition.

| Name (Rollenvorlage) | ID (Rollenvorlage) | Name (Launchpad-Bereich) | ID (Launchpad-Bereich) |
| --- | --- | --- | --- |
| Lagerist (EWM) | SAP_BR_WAREHOUSE_CLERK_EWM | Lagerbüro | SAP_BR_WAREHOUSE_CLERK_EWM |

### Erforderliche Organisationseinheiten

Einige Segmente der Stammdaten hängen von den Organisationseinheiten des Unternehmens ab. Allgemeine (zentrale) Daten sind nicht von einer Organisationseinheit oder dem Buchungskreis abhängig. Die folgende Tabelle stellt eine Übersicht dieser verschiedenen Datensegmente und ihrer relevanten Organisationseinheiten bereit:

| Datensegment | Hängt ab von | Feldbeispiele | Kommentare | Zu verwendende Organisationseinheit |
| --- | --- | --- | --- | --- |
| Alle | Lagernummer |  |  |  |

### Obligatorische und optionale Stammdaten

Stammdatensätze können auf andere Stammdaten verweisen. Die folgende Tabelle bietet eine Übersicht über die optionalen und obligatorischen Stammdatenobjekte, die in einem <Typ>-Stammdatensatz verwendet werden müssen.

| Stammdatenobjekt | Verwendet im Datensegment | Obligatorisch / optional | Kommentare |
| --- | --- | --- | --- |
| Geschäftspartner | Fixlagerplätze zuordnen | Obligatorisch | Geschäftspartner als Verfügungsberechtigte für das Lager |

## Übersichtstabelle

Dieser Stammdatensatz umfasst mehrere Segmente, die in der nachfolgenden Tabelle genannt sind.

|  |
| --- |
| Hinweis Wenn Ihr Systemadministrator Bereiche und Seiten auf dem SAP Fiori Launchpad aktiviert hat, enthält die Startseite nur die wesentlichen Apps, mit denen die typischen Aufgaben einer Benutzerrolle ausgeführt werden können.Alle anderen (suchbaren) Apps, die nicht auf der Startseite enthalten sind, finden Sie über die Suchleiste ([2434549](https://me.sap.com/notes/2434549)).Wenn Sie die Startseite personalisieren und versteckte Apps hinzufügen möchten, wechseln Sie in Ihr Benutzerprofil und wählen Sie App Finder. |

| Segment | Anwendungsrolle | App/Vorgang | Erwartete Ergebnisse |
| --- | --- | --- | --- |
| [Lagerplätze anlegen](#unique_2) [Seite ] 6 | Lagerist (EWM) | Lagerplätze anlegen(/SCWM/LS01) | Die Lagerplätze werden angelegt. |
| [Lagerplätze ändern](#unique_3) [Seite ] 7 | Lagerist (EWM) | Lagerplätze bearbeiten(/SCWM/LS02) | Die Lagerplätze werden geändert. |
| [Lagerplätze anzeigen](#unique_4) [Seite ] 8 | Lagerist (EWM) | Lagerplätze anzeigen(/SCWM/LS03) | Die Lagerplätze werden angezeigt. |
| [Massenänderung an Lagerplätzen durchführen](#unique_5) [Seite ] 9 | Lagerist (EWM) | Massenbearbeitung Lagerplätze(/SCWM/LS11) | Die Massenänderungen an Lagerplätzen werden vorgenommen. |
| [Fixplätze zuordnen](#unique_6) [Seite ] 10 | Lagerist (EWM) | Fixplätze zuordnen(/SCWM/BINMAT) | Die feste Lagerplatzzuordnung wird angelegt. |

## Testverfahren

Dieser Abschnitt beschreibt die Vorgehensweisen für die einzelnen Segmente oder Prozessschritte, die Teil dieses Stammsatzes ist.

### Lagerplätze anlegen

Zweck

In diesem Abschnitt finden Sie eine Beschreibung, wie Sie Lagerplätze in SAP S/4HANA mithilfe des SAP Fiori Launchpad anlegen.

Vorgehensweise

| Testschrittnummer | Bezeichnung des Testschritts | Anweisungen | Erwartetes Ergebnis | Kommentare |
| --- | --- | --- | --- | --- |
| 1 | Anmelden | Melden Sie sich am SAP Fiori Launchpad als Lagerist (EWM) an. |  |  |
| 2 | App aufrufen | Öffnen Sie Lagerplätze anlegen(/SCWM/LS01). |  |  |
| 3 | Lagerplatz-ID eingeben | Geben Sie auf dem Bild Lagerplätze anlegen(/SCWM/LS01) folgende Daten ein:Lagernummer: <Ihre Lagernummer>Lagerplatz: <Lagerplatz-ID>Wählen Sie Enter. |  |  |
| 4 | Lagerplatzattribute eingeben | Geben Sie auf der Registerkarte Lagerplatz die folgenden Daten ein:Lagertyp: <Lagertyp>Hinweis Nur das Feld Lagertyp ist obligatorisch. Alle anderen im Folgenden aufgeführten Felder sind optional:Maximales GewichtMax. VolumenPlatzgangX-KoordinateStapelY-KoordinatePlatzebeneZ-KoordinateLagerplatzwinkel |  |  |
| 5 | Daten sichern | Wählen Sie Sichern. | Eine Systemmeldung teilt Ihnen mit, dass der Lagerplatz gesichert wurde. |  |

### Lagerplätze ändern

Zweck

In diesem Abschnitt können Sie Lagerplätze in SAP S/4HANA mithilfe des SAP Fiori Launchpad ändern.

Vorgehensweise

| Testschrittnummer | Bezeichnung des Testschritts | Anweisungen | Erwartetes Ergebnis | Kommentare |
| --- | --- | --- | --- | --- |
| 1 | Anmelden | Melden Sie sich am SAP Fiori Launchpad als Lagerist (EWM) an. |  |  |
| 2 | App aufrufen | Öffnen Sie Lagerplätze bearbeiten(/SCWM/LS02). |  |  |
| 3 | Lagerplatz-ID eingeben | Geben Sie auf dem Bild Lagerplätze bearbeiten(/SCWM/LS02) folgende Daten ein:Lagernummer: <Ihre Lagernummer>Lagerplatz: <Lagerplatz-ID>Wählen Sie Enter. |  |  |
| 4 | Lagerplatz-Attribute ändern | Falls erforderlich, ändern Sie die folgenden Werte auf der Registerkarte Lagerplatz.Hinweis Nur die folgenden Felder sind änderbar:Maximales GewichtMax. VolumenPlatzgangX-KoordinateStapelY-KoordinatePlatzebeneZ-KoordinateLagerplatzwinkel |  |  |
| 5 | Daten sichern | Wählen Sie Sichern. | Eine Systemmeldung teilt Ihnen mit, dass der Lagerplatz gesichert wurde. |  |

### Lagerplätze anzeigen

Zweck

In diesem Abschnitt können Sie die Lagerplätze in SAP S/4HANA mithilfe des SAP Fiori Launchpad anzeigen.

Vorgehensweise

| Testschrittnummer | Bezeichnung des Testschritts | Anweisungen | Erwartetes Ergebnis | Kommentare |
| --- | --- | --- | --- | --- |
| 1 | Anmelden | Melden Sie sich am SAP Fiori Launchpad als Lagerist (EWM) an. |  |  |
| 2 | App aufrufen | Öffnen Sie Lagerplätze anzeigen(/SCWM/LS03). |  |  |
| 3 | Lagerplatz-ID eingeben | Geben Sie auf dem Bild Lagerplätze anzeigen(/SCWM/LS03) folgende Daten ein:Lagernummer: <Ihre Lagernummer>Lagerplatz: <Lagerplatz-ID>Wählen Sie Enter. | Die Lagerplatzattribute werden angezeigt. |  |

### Massenänderung an Lagerplätzen durchführen

Zweck

In diesem Abschnitt können Sie eine Massenänderung an Lagerplätzen in SAP S/4HANA mithilfe des SAP Fiori Launchpad durchführen.

Vorgehensweise

| Testschrittnummer | Bezeichnung des Testschritts | Anweisungen | Erwartetes Ergebnis | Kommentare |
| --- | --- | --- | --- | --- |
| 1 | Anmelden | Melden Sie sich am SAP Fiori Launchpad als Lagerist (EWM) an. |  |  |
| 2 | App aufrufen | Öffnen Sie Massenbearbeitung Lagerplätze(/SCWM/LS11). |  |  |
| 3 | Filterkriterien eingeben | Geben Sie auf dem Bild Massenänderung von Lagerplätzen in Lagernummer XXXX folgende Daten ein:Lagernummer: <Ihre Lagernummer>Als Selektions- und Filterkriterien können Sie folgende Werte eingeben:Lagerplatz: <Lagerplatz-ID> bis <Lagerplatz-ID>Lagertyp: <Lagertyp-ID> bis <Lagertyp-ID>SperrstatusHinweis Wenn Sie das Ankreuzfeld freie Abgrenzung markieren, können Sie mehrere Filter für die Lagerplatzauswahl wählen.Wählen Sie Ausführen. | Die Liste der den Selektionskriterien entsprechenden Lagerplätze wird angezeigt. |  |
| 4 | Massenänderung Lagerplätze | Wählen Sie die Einträge Ihrer Wahl aus, indem Sie die entsprechenden Ankreuzfelder markieren.Um mehrere Lagerplätze gleichzeitig zu löschen, wählen Sie Löschen.oderUm mehrere Lagerplätze gleichzeitig zu ändern, wählen Sie Bearbeiten. Sie können dann Änderungen an folgenden Attributen der Lagerplätze durchführen.Maximales GewichtMax. VolumenPlatzgangStapelPlatzebeneLagerplatzwinkel |  |  |
| 5 | Daten sichern | Wählen Sie Sichern. | Eine Systemmeldung teilt Ihnen mit, dass die Änderungen am Lagerplatz gesichert wurden. |  |

### Fixplätze zuordnen

Zweck

In diesem Abschnitt legen Sie eine Fixplatzzuordnung in SAP S/4HANA mithilfe des SAP Fiori Launchpad fest.

Vorgehensweise

| Testschrittnummer | Bezeichnung des Testschritts | Anweisungen | Erwartetes Ergebnis | Kommentare |
| --- | --- | --- | --- | --- |
| 1 | Anmelden | Melden Sie sich am SAP Fiori Launchpad als Lagerist (EWM) an. |  |  |
| 2 | App aufrufen | Öffnen Sie Fixplätze zuordnen(/SCWM/BINMAT). |  |  |
| 3 | Filterkriterien eingeben | Geben Sie auf dem Bild Fixlagerplätze bearbeiten die folgenden Daten ein:Lagernummer: <Ihre Lagernummer>Produkt: <Produkt-ID> bis <Produkt-ID>Verfügungsberechtigter: <Geschäftspartner-ID> bis <Geschäftspartner-ID>Hinweis Der Verfügungsberechtigte ist der für die Lagernummer eingegebene Geschäftspartner.Lagerplatz: <Lagerplatz-ID> bis <Lagerplatz-ID>Lagertyp: <Lagertyp-ID> bis <Lagertyp-ID>Wählen Sie Ausführen. | Die Liste der den Selektionskriterien entsprechenden zugeordneten Fixplätzen wird angezeigt. |  |
| 4 | Festlagerplatz-Zuordnung anlegen | Auf dem Bild Lagernummer XXXX: Fixlagerplatz Bild anzeigen, wählen Sie Bearbeiten.Auf dem Bild Lagernummer XXXX: Fixlagerplatz pflegen, wählen Sie Anlegen.Geben Sie in der neu angelegten Zeile die folgenden Werte ein:VerfügBer.: <Geschäftspartner-ID für den Verfügungsberechtigten>Lagerplatz: <ID des Fixlagerplatzes>Typ: <ID des Fixplatzlagertyps>Produkt: Produkt-IDMax Mng: <Menge>AnzMeh: <ME für Maximalmenge>, z.B. StückMindMenge: <Menge>AnzMeh: <ME für Mindestmenge>, z.B. StückWenn Sie die Werte für folgende Felder in den Lagerproduktstammdaten gepflegt haben:Max. Anz PlätzeMaximalmengeMinimalmengeAnzMeh fir die Maximal-/MindestmengeDie Werte für Max Mng und MindMeng in der Fixplatzzuordnung werden basierend auf den Werten für Maximalmenge, Mindestmenge und Max. Anz Plätze in den Lagerproduktstammdaten berechnet. Die AnzMeh wird ebenfalls aus den Lagerproduktstammdaten gefüllt. |  |  |
| 5 | Daten sichern | Wählen Sie Sichern. | Eine Systemmeldung teilt Ihnen mit, dass die Lagerplätze gesichert wurden. |  |

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
- related-to :: [[11-inventory-warehouse-and-transportation/maintain-storage-bins-and-fixed-bin-assignments-mds-3kr-335]]
- related-to :: [[11-inventory-warehouse-and-transportation/mds-3kr-337]]
- related-to :: [[11-inventory-warehouse-and-transportation/mds-3kr-339]]
- related-to :: [[11-inventory-warehouse-and-transportation/script-de-dados-mestre-atualizar-posicoes-no-deposito-e-atribuicoes-de]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/3KR_S4CLD2608_Master_Data_DE_XX.docx` — full document · extracted with `mammoth` · 14,810 chars in the whole document
