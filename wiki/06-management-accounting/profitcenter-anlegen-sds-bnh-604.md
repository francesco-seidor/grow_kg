---
id: 06-management-accounting/profitcenter-anlegen-sds-bnh-604
title: Profitcenter anlegen – SDS (BNH) (BNH_S4CLD2608_Master_Data_DE_XX)
description: "German SAP S/4HANA Cloud master data script (BNH) for creating profit center master data with app F3516 as Divisional Accountant, incl. validity periods."
cluster: 06-management-accounting
tags: [kb/management-accounting, topic/profit-centers]
aliases: [BNH_S4CLD2608_Master_Data_DE_XX]
keywords: [Profit Centers and Profit Center Reorganization, profit center master data, profit center creation, validity periods, master data scripts, controlling area, profit center groups, company code assignment, segment reporting, business roles]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/BNH_S4CLD2608_Master_Data_DE_XX.docx]
confidence: high
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-604
topic: 06-management-accounting/profit-centers
language: DE
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Profitcenter anlegen – SDS (BNH) (BNH_S4CLD2608_Master_Data_DE_XX)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/BNH_S4CLD2608_Master_Data_DE_XX.docx`, extracted with `mammoth`. Grouped under **Profit Centers and Profit Center Reorganization** in Management Accounting. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

| <!-- image omitted: unnamed --> | StammdatenskriptSAP S/4HANA Cloud Public Edition - 02-07-26 |
| --- | --- |
|  | Profitcenter anlegen – SDS (BNH) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Inhaltsverzeichnis

[1 Verwendungszweck 2](#_Toc233889962)

[2 Voraussetzungen 3](#_Toc233889963)

[2.1 Systemzugriff und Rollen 3](#_Toc233889964)

[2.2 Erforderliche Organisationseinheiten 3](#_Toc233889965)

[2.3 Obligatorische und optionale Stammdaten 4](#_Toc233889966)

[2.4 Wesentliche Parameter für die Datenerstellung 5](#_Toc233889967)

[3 Übersichtstabelle 6](#_Toc233889968)

[4 Testverfahren 7](#_Toc233889969)

[4.1 Profitcenterstammdaten anlegen 7](#_Toc233889970)

## Verwendungszweck

Organisatorische Einheit des Rechnungswesens, die das Unternehmen managementorientiert, d.h. zum Zwecke der internen Steuerung, gliedert. Die Einteilung Ihres Unternehmens in Profitcenter ermöglicht es Ihnen, den Gewinn interner Verantwortungsbereiche zu analysieren und Verantwortung an dezentrale Einheiten zu delegieren.

Die Stammdaten zu einem Profitcenter enthalten neben dem Namen des Profitcenters, der Zuordnung zu einem Kostenrechnungskreis und der Gültigkeitsdauer auch Informationen über den Profitcenter-Verantwortlichen, die Zuordnung zu einem Hierarchiebereich der Standardhierarchie, sowie Adress- und Kommunikationsdaten usw.

## Voraussetzungen

In diesem Abschnitt sind alle Voraussetzungen für den Test hinsichtlich System, Benutzer, Stammdaten, Organisationsdaten, sonstige Testdaten und Voraussetzungen zusammengefasst.

### Systemzugriff und Rollen

Führen Sie den Test in folgenden Systemen aus:

| System | Details |
| --- | --- |
| SAP S/4HANA Cloud Public Edition | System-ID: Nr.Client: Nr. |

Legen Sie Benutzerrollen mit den folgenden von SAP ausgelieferten Benutzerrollenvorlagen an, und ordnen Sie sie Ihren einzelnen Testbenutzern zu.

Alternativ können Sie, falls verfügbar, die folgenden von SAP ausgelieferten Bereiche verwenden. Legen Sie einen Bereich mit Seiten an, die vordefinierte grundlegende Apps enthalten, und ordnen Sie sie der Benutzerrolle zu. Anschließend ordnen Sie diese Benutzerrolle Ihren einzelnen Benutzern zu.

Weitere Informationen finden Sie unter Anwendungsrolle aus einer Vorlage anlegen in der [Product Assistance](https://help.sap.com/docs/SAP_S4HANA_CLOUD/53e36b5493804bcdb3f6f14de8b487dd/ec310a8b669a45ca898dc4dd91d97de2.html) für SAP S/4HANA Cloud Public Edition.

| Name (Rollenvorlage) | ID (Rollenvorlage) | Name (Launchpad-Bereich) | ID (Launchpad-Bereich) | Anmelden |
| --- | --- | --- | --- | --- |
| Divisionaler Buchhalter | SAP_BR_DIVISION_ACCOUNTANT | Spartenbuchhaltung | SAP_BR_DIVISION_ACCOUNTANT |  |

### Erforderliche Organisationseinheiten

Einige Segmente von Debitorenstammdaten hängen von den Organisationseinheiten des Unternehmens ab. Allgemeine (zentrale) Daten hängen nicht von einer Organisationseinheit oder dem Buchungskreis ab. Die folgende Tabelle stellt eine Übersicht dieser verschiedenen Datensegmente und ihrer relevanten Organisationseinheiten bereit:

| Datensegment | Hängt ab von | Feldbeispiele | Kommentare | Zu verwendende Organisationseinheit |
| --- | --- | --- | --- | --- |
| Profitcenter-Grunddaten | KostenrechnungskreisProfitcentergruppeSegment | Name, Langtext, Gültigkeitszeitraum, verantwortlicher Benutzer, Verantwortlicher | Profitcentergruppen ermöglichen dem Controller, Profitcenter gruppenweise anzusprechen, indem er, z.B. im Customizing oder Reporting, anstelle der einzelnen Profitcenternamen den Gruppennamen bereitstellt. Im Reporting ermöglicht dies eine Analyse von Kennzahlen für das Controlling auf einer Aggregatsebene.Ein Segment wird für gewöhnlich nicht explizit gebucht. Daten werden aus Kontierungsobjekten wie Profitcentern abgeleitet. Das Proficenter wiederum wird für gewöhnlich nicht explizit gebucht. Daten werden aus Primärkontierungsobjekten wie Kostenstellen, internen Aufträgen usw. abgeleitet. | Kostenrechnungskreis:____________Profitcentergruppe:____________Segment:____________ |
| Profitcenter-Buchungskreis-Zuordnung | Buchungskreis | Buchungskreis | Buchungskreisdaten können für jede Buchungskreis-ID Ihrer Unternehmensstruktur vorhanden sein, für die der Profitcenterstammsatz verwendet wird. | Buchungskreis:____________ |

### Obligatorische und optionale Stammdaten

Die folgende Tabelle bietet eine Übersicht über die optionalen und obligatorischen Stammdatenobjekte, die in einem Profitcenterstammdatensatz verwendet werden müssen.

| Stammdatenobjekt | Verwendet im Datensegment | Obligatorisch / optional | Kommentare |
| --- | --- | --- | --- |
| Kostenrechnungskreis | Profitcenter-Grunddaten | Obligatorisch | Zum Anlegen eines neuen Profitcenters kann ein Referenzkostenrechnungskreis verwendet werden. |
| Profitcenter | Profitcenter-Grunddaten | Obligatorisch | Zum Anlegen eines neuen Profitcenters kann ein Referenzprofitcenter verwendet werden. |
| Gültig ab | Profitcenter-Grunddaten | Obligatorisch |  |
| Gültig bis | Profitcenter-Grunddaten | Obligatorisch |  |
| Name | Profitcenter-Grunddaten | Obligatorisch |  |
| Langtext | Profitcenter-Grunddaten | Optional |  |
| Verantwortlicher Benutzer | Profitcenter-Grunddaten | Optional |  |
| Verantwortlicher | Profitcenter-Grunddaten | Obligatorisch |  |
| Profitcentergruppe | Profitcenter-Grunddaten | Obligatorisch |  |
| Abteilung | Profitcenter-Grunddaten | Optional |  |
| Segment | Profitcenter-Grunddaten | Optional | Wenn ein Profitcenter für ein US-Unternehmen gültig ist, wird empfohlen, das Segmentfeld zu belegen. Auf diese Weise kann ein Segment-Reporting erfolgen. |
| Planungsvorlage | Profitcenter-Grunddaten | Optional |  |
| Adress- und Kommunikationsfelder | Adress- und Kommunikationsdaten für Profitcenter | Alle sind optional |  |

### Wesentliche Parameter für die Datenerstellung

In diesem Abschnitt werden einige Basisparameter erläutert, die das Verhalten eines Stammsatzes beeinflussen und zum Anlegen eines Profitcenterstammdatensatzes immer erforderlich sind:

Kostenrechnungskreis: A000

## Übersichtstabelle

Dieser Umfangsbestandteil umfasst die Prozessschritte, die in der folgenden Tabelle aufgeführt werden:

|  |
| --- |
| Hinweis Wenn Ihr Systemadministrator Bereiche und Seiten auf dem SAP Fiori Launchpad aktiviert hat, enthält die Startseite nur die wesentlichen Apps, mit denen die typischen Aufgaben einer Benutzerrolle ausgeführt werden können.Alle anderen (suchbaren) Apps, die nicht auf der Startseite enthalten sind, finden Sie über die Suchleiste ([2434549](https://me.sap.com/notes/2434549)).Wenn Sie die Startseite personalisieren und versteckte Apps hinzufügen möchten, wechseln Sie in Ihr Benutzerprofil und wählen Sie App Finder. |

| Prozessschritt | Benutzerrolle | Vorgang/App | Erwartete Ergebnisse |
| --- | --- | --- | --- |
| [Profitcenterstammdaten anlegen](#unique_8) [Seite ] 7 | Divisionaler Buchhalter | Profitcenter verwalten - Alte Version(F3516) | Das Bild Stammdaten für Profitcenter wird in einem neuen Fenster anzeigt. |

## Testverfahren

In diesem Abschnitt werden die Testverfahren für den jeweiligen Prozessschritt beschrieben, der zum betreffenden Umfangsbestandteil gehört.

### Profitcenterstammdaten anlegen

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
| 1 | Anmelden | Melden Sie sich am SAP Fiori Launchpad als Divisionaler Buchhalter an. | Das SAP Fiori Launchpad wird angezeigt. |  |
| 2 | SAP-Fiori-App aufrufen | Öffnen Sie Profitcenter verwalten - Alte Version(F3516). | Das Bild Stammdaten für Profitcenter wird angezeigt. |  |
| 3 | Profitcenter suchen | Suchen Sie nach dem Profitcenter.Wählen Sie Start. | Eine Liste der Profitcenter wird auf dem Bild angezeigt. |  |
| 4 | Profitcenter hinzufügen | Wählen Sie Anlegen. | Das Bild Profitcenter: Neu wird angezeigt. |  |
| 5 | Profitcenterdaten eingeben | Geben Sie im Abschnitt Neues Profitcenter die folgenden Daten ein:Profitcenter: <Name>, z.B. YBXXXHinweis Die Höchstlänge beträgt 10 Zeichen. Verwenden Sie keine Sonderzeichen wie %, !, $, &, @ usw. Sie verursachen einen App-Absturz und können nicht gelöscht werden.Gültig ab: <gültig ab Datum>Gültig bis: <Gültig-bis-Datum>Name: <beliebige Beschreibung>Verantwortlicher: <Name der verantwortlichen Person> |  |  |
| 6 | Grunddaten eingeben | Geben Sie auf der Registerkarte Organisationseinheit folgende Daten ein:Standardhierarchieknoten: <Profitcentergruppe>:Segment: <Segment> |  |  |
| 7 | Buchungskreiszuordnung | Markieren oder entmarkieren Sie das Ankreuzfeld, um dem neuen Profitcenter Buchungskreise zuzuordnen. |  |  |
| 8 | Daten sichern | Sichern Sie Ihre Eingaben. |  |  |
| 9 | Neuen Gültigkeitszeitraum festlegen (optional) | Wählen Sie Bearbeiten.Im Profitcenter, das Sie angelegt haben, wählen Sie Gültigkeitszeitraum > Neuer Gültigkeitszeitraum.Nehmen Sie Eingaben in den Feldern Gültig ab und Gültig bis vor, und wählen Sie einen Quelldatenzeitraum aus.Wählen Sie Anlegen.Hinweis Wenn sich der neue Gültigkeitszeitraum mit dem bestehenden überschneidet, wird der sich überschneidende Zeitraum aus der aktuellen Zeitraum ausgeschlossen.Wenn es eine Lücke zwischen dem neuen Gültigkeitszeitraum und anderen Zeiträumen gibt, verhindert das System diese Aktion. |  |  |
| 10 | Zeitabhängige Felder ändern (optional) | Sie können die folgenden zeitabhängigen Felder im neu angelegten Gültigkeitszeitraum ändern.AbteilungVerantwortlicher PCVerantwortlicher BenutzerTitelNameName 2Name 3Name 4SperrkennzeichenWählen Sie Sichern.Hinweis Wenn Sie Felder ändern, die nicht zeitabhängig sind, werden die Änderungen über alle Gültigkeitszeiträume hinweg angewendet.Wenn es keinen Unterschied zwischen dem neuen Zeitraum und dem vorherigen oder dem folgenden Zeitraum gibt, wird der neue Zeitraum mit dem vorhandenen Zeitraum zusammengeführt. | Ein neuer Gültigkeitszeitraum wird angelegt.Die Änderungssätze werden im Abschnitt Änderungsprotokoll angezeigt. |  |

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
- related-to :: [[06-management-accounting/create-profit-center-mds-bnh-605]]
- related-to :: [[06-management-accounting/mds-bnh-607]]
- related-to :: [[06-management-accounting/mds-bnh-609]]
- related-to :: [[06-management-accounting/script-de-dados-mestre-criar-centro-de-lucro-mds-bnh-608]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/BNH_S4CLD2608_Master_Data_DE_XX.docx` — full document · extracted with `mammoth` · 12,932 chars in the whole document
