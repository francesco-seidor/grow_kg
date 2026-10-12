---
id: 11-inventory-warehouse-and-transportation/produktionsversorgungsbereich-pflegen-sds-3ks-340
title: Produktionsversorgungsbereich pflegen – SDS (3KS) (3KS_S4CLD2608_Master_Data_DE_XX)
description: "German SAP S/4HANA Cloud Public 2608 master data script 3KS: optional assignment of storage bins to production supply areas (PSA/PVB) in cloud warehouse management."
cluster: 11-inventory-warehouse-and-transportation
tags: [kb/inventory-warehouse-and-transportation, topic/ewm-production-integration]
aliases: [3KS_S4CLD2608_Master_Data_DE_XX]
keywords: [EWM Production Supply and Receipt, production supply area, storage bin assignment, warehouse management, production integration, control cycle, kanban supply, business roles, master data prerequisites, 3KS]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/3KS_S4CLD2608_Master_Data_DE_XX.docx]
confidence: high
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-340
topic: 11-inventory-warehouse-and-transportation/ewm-production-integration
language: DE
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Produktionsversorgungsbereich pflegen – SDS (3KS) (3KS_S4CLD2608_Master_Data_DE_XX)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/3KS_S4CLD2608_Master_Data_DE_XX.docx`, extracted with `mammoth`. Grouped under **EWM Production Supply and Receipt** in Inventory, Warehouse and Transportation. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

| <!-- image omitted: unnamed --> | StammdatenskriptSAP S/4HANA Cloud Public Edition - 02-07-26 |
| --- | --- |
|  | Produktionsversorgungsbereich pflegen – SDS (3KS) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Inhaltsverzeichnis

[1 Zweck 2](#_Toc233889645)

[2 Voraussetzungen 3](#_Toc233889646)

[2.1 Systemzugriff 3](#_Toc233889647)

[2.2 Rollen 3](#_Toc233889648)

[2.3 Erforderliche Organisationseinheiten 3](#_Toc233889649)

[2.4 Obligatorische und optionale Stammdaten 4](#_Toc233889650)

[2.5 Voraussetzungen/Situation 4](#_Toc233889651)

[3 Übersichtstabelle 5](#_Toc233889652)

[4 Testverfahren 6](#_Toc233889653)

[4.1 (OPTIONAL) Platz PVB zuordnen - Lager 6](#_Toc233889654)

[4.2 (OPTIONAL) Platz PVB zuordnen 7](#_Toc233889655)

## Zweck

In diesem Dokument lernen Sie, wie Sie die folgenden Aktivitäten zum Anlegen von Lagerstammdaten für die Produktionsversorgung ausführen:

- [(OPTIONAL) Platz PVB zuordnen - Lager](#unique_2) [Seite ] 6
- [(OPTIONAL) Platz PVB zuordnen](#unique_3) [Seite ] 7

Die Erstellung und Replikation des Produktionsversorgungsbereichs sowie die Lagerplatzzuordnung zum PVB sollen durch die Ausführung der jeweiligen Schritte in den im Kapitel Voraussetzungen/Situation erwähnten Stammdatenskript- oder Testskriptdokumenten erfolgen. Dieses Stammdatenskript richtet sich nur an Kunden, die die relevanten Einstellungen prüfen und Einstellungen manuell anlegen möchten, falls die Voraussetzungen nicht erfüllt wurden.

Die Beschreibung umfasst die Datensegmente, die für die Stammdaten für die Arbeit in einer normalen Systemumgebung relevant sind. Sie lernen hauptsächlich, welche Datensegmente und -felder üblicherweise mit Eingabewerten gefüllt werden müssen. Felder, die für den durch von SAP Best Practices bereitgestellten Umfang der Kontentauslieferung in SAP S/4HANA nicht relevant sind, werden in diesem Dokument nicht behandelt, obwohl sie möglicherweise in der Benutzeroberfläche angezeigt werden.

Diese Stammdaten verwenden Sie für die Geschäftsprozesse der Produktionsintegration im Warehouse Management.

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

Stammdatensätze können auf andere Stammdaten verweisen. Die folgende Tabelle bietet eine Übersicht über die optionalen und obligatorischen Stammdatenobjekte, die beim Anlegen einer Lagerplatzzuordnung zum PSA-Stammdatensatz verwendet werden müssen.

| Stammdatenobjekt | Verwendet im Datensegment | Obligatorisch / optional | Kommentare |
| --- | --- | --- | --- |
| Geschäftspartner | Platz PVB zuordnen - Lager | Obligatorisch | Geschäftspartner als Verfügungsberechtigte für das Lager. |
| Produktionsversorgungsbereich | Platz PVB zuordnen - Lager | Obligatorisch | Der Produktionsversorgungsbereich, der im SAP-S/4HANA-System angelegt wird. Siehe Kapitel "Voraussetzungen/Situation". |
| Produkt | Platz PVB zuordnen - Lager | Obligatorisch |  |
| Lagerplatz | Platz PVB zuordnen - Lager | Obligatorisch |  |

### Voraussetzungen/Situation

Bevor dieser Umfangsbestandteil getestet werden kann, müssen die folgenden Voraussetzungen erfüllt sein.

| Umfangsbestandteil-ID | Voraussetzung/Situation |
| --- | --- |
| 40D – Produktionsversorgungsbereich anlegen – SDS | Dieses Stammdatenskript ist die Voraussetzung für diesen Beleg.Verwenden Sie beim Anlegen des Produktionsversorgungsbereichs (PVB) den Cloud-WM-Lagerort, z.B. 105W.Nach der Ausführung dieses Stammdatenskripts haben Sie folgende Einstellungen vorgenommen:Der Produktionsversorgungsbereich wird in SAP S/4HANA angelegt.Der relevante Produktionsversorgungsbereich wird automatisch aus SAP S/4HANA in Cloud Warehouse repliziert. |
| 3DV – Integration von Lager und Produktion | Voraussetzung für diesen Beleg ist der Schritt "Regelkreis anlegen" im Kapitel "Vorbereitende Schritte" des 3DV-Testskripts.Nachdem Sie den Schritt "Regelkreis anlegen" ausgeführt haben, haben Sie folgende Einstellungen vorgenommen:Der relevante Produktionsversorgungsbereich wird automatisch aus SAP S/4HANA in Cloud Warehouse repliziert.Der Lagerplatz wird dem PVB zugeordnet. |
| 3VT – Lager – Kanban-gesteuerte Produktionsversorgung | Voraussetzung für diesen Beleg ist der Schritt "Regelkreis für Kanban: Umlagerung" im Kapitel "Vorbereitende Schritte" des 3VT-Testskripts.Nach der Ausführung des Schrittes "Regelkreis für Kanban: Umlagerung" haben Sie die folgenden Einstellungen vorgenommen:Der relevante Produktionsversorgungsbereich wird automatisch aus SAP S/4HANA in Cloud Warehouse repliziert.Der Lagerplatz wird dem PVB zugeordnet. |

## Übersichtstabelle

Dieser Stammdatensatz umfasst mehrere Segmente, die in der nachfolgenden Tabelle genannt sind.

|  |
| --- |
| Hinweis Wenn Ihr Systemadministrator Bereiche und Seiten auf dem SAP Fiori Launchpad aktiviert hat, enthält die Startseite nur die wesentlichen Apps, mit denen die typischen Aufgaben einer Benutzerrolle ausgeführt werden können.Alle anderen (suchbaren) Apps, die nicht auf der Startseite enthalten sind, finden Sie über die Suchleiste ([2434549](https://me.sap.com/notes/2434549)).Wenn Sie die Startseite personalisieren und versteckte Apps hinzufügen möchten, wechseln Sie in Ihr Benutzerprofil und wählen Sie App Finder. |

| Segment | Anwendungsrolle | App/Vorgang | Erwartete Ergebnisse |
| --- | --- | --- | --- |
| [(OPTIONAL) Platz PVB zuordnen - Lager](#unique_2) [Seite ] 6 | Lagerist (EWM) | Platz PVB zuordnen - Lager(/SCWM/PSASTAGE) | Die Zuordnung des Lagerplatzes zum PVB wird angelegt. |
| [(OPTIONAL) Platz PVB zuordnen](#unique_3) [Seite ] 7 | Lagerist (EWM) | Platz PVB zuordnen(/SCWM/PSASTAGE2) | Die Zuordnung des Lagerplatzes zum PVB wird angelegt. |

## Testverfahren

Dieser Abschnitt beschreibt die Vorgehensweisen für die einzelnen Segmente oder Prozessschritte, die Teil dieses Stammsatzes ist.

### (OPTIONAL) Platz PVB zuordnen - Lager

Zweck

In diesem Abschnitt verwalten Sie die Lagerplatzzuordnungen aller PVBs in der Lagernummer in SAP S/4HANA mithilfe des SAP Fiori Launchpad.

Dieser Schritt ist optional und Sie können ihn überspringen, wenn der Lagerplatz dem PVB wie erwartet zugeordnet wurde. Es ist nur erforderlich, wenn während des Erstellungsschrittes des Regelkreises keine Platzzuordnungen für Ihren PVB vorgenommen wurden. Informationen hierzu finden Sie im Kapitel "Voraussetzungen/Situation" im Schritt "Regelkreis anlegen".

Vorgehensweise

| Testschrittnummer | Bezeichnung des Testschritts | Anweisungen | Erwartetes Ergebnis | Kommentare |
| --- | --- | --- | --- | --- |
| 1 | Anmelden | Melden Sie sich am SAP Fiori Launchpad als Lagerist (EWM) an. |  |  |
| 2 | App aufrufen | Öffnen Sie Platz PVB zuordnen - Lager(/SCWM/PSASTAGE). |  |  |
| 3 | Neuen Eintrag anlegen | Wählen Sie in der Änderungssicht "Platz PVB zuordnen": Übersicht die Option Neue Einträge. |  |  |
| 4 | Zuordnungswerte eingeben | Auf dem Bild Neue Einträge: Details der hinzugefügten Einträge geben Sie folgende Daten ein:Beseitigung: <Geschäftspartner-ID für den Verfügungsberechtigten>Produktionsversorgungsbereich: <Produktionsversorgungsbereich>Produkt: Produkt-IDLagerplatz: <Lagerplatz-ID> |  |  |
| 5 | Daten sichern | Wählen Sie Sichern. | Eine Systemmeldung teilt Ihnen mit, dass die Zuordnung des Lagerplatzes zum PVB gesichert wurde. |  |

### (OPTIONAL) Platz PVB zuordnen

Zweck

In diesem Abschnitt verwalten Sie alle Lagerplatzzuordnungen innerhalb eines bestimmten Produktionsversorgungsbereichs in SAP S/4HANA mithilfe des SAP Fiori Launchpad.

Dieser Schritt ist optional und Sie können ihn überspringen, wenn der Lagerplatz dem PVB wie erwartet zugeordnet wurde. Es ist nur erforderlich, wenn während des Erstellungsschrittes des Regelkreises keine Platzzuordnungen für Ihren PVB vorgenommen wurden. Informationen hierzu finden Sie im Kapitel "Voraussetzungen/Situation" im Schritt "Regelkreis anlegen".

Vorgehensweise

| Testschrittnummer | Bezeichnung des Testschritts | Anweisungen | Erwartetes Ergebnis | Kommentare |
| --- | --- | --- | --- | --- |
| 1 | Anmelden | Melden Sie sich am SAP Fiori Launchpad als Lagerist (EWM) an. |  |  |
| 2 | App aufrufen | Öffnen Sie Platz PVB zuordnen(/SCWM/PSASTAGE2). |  |  |
| 3 | Arbeitsbereich festlegen | Geben Sie auf dem Bild Arbeitsbereich festlegen: Eingabe die folgenden Daten ein:Verfügungsberechtigter: <Geschäftspartner-ID für den Verfügungsberechtigten>Produktionsversorgungsbereich: <Produktionsversorgungsbereich>Wählen Sie Weiter. |  |  |
| 4 | Neuen Eintrag anlegen | Wählen Sie in der Änderungssicht "Platz PVB zuordnen": Übersicht die Option Neue Einträge. |  |  |
| 5 | Zuordnungswerte eingeben | Auf dem Bild Neue Einträge: Details der hinzugefügten Einträge geben Sie folgende Daten ein:Produkt: Produkt-IDLagerplatz: <Lagerplatz-ID> |  |  |
| 6 | Daten sichern | Wählen Sie Sichern. | Eine Systemmeldung teilt Ihnen mit, dass die Zuordnung des Lagerplatzes zum PVB gesichert wurde. |  |

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
- related-to :: [[11-inventory-warehouse-and-transportation/atualizar-area-de-abastecimento-da-producao-mds-3ks-344]]
- related-to :: [[11-inventory-warehouse-and-transportation/maintain-production-supply-area-mds-3ks-341]]
- related-to :: [[11-inventory-warehouse-and-transportation/mds-3ks-343]]
- related-to :: [[11-inventory-warehouse-and-transportation/mds-3ks-345]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/3KS_S4CLD2608_Master_Data_DE_XX.docx` — full document · extracted with `mammoth` · 13,172 chars in the whole document
