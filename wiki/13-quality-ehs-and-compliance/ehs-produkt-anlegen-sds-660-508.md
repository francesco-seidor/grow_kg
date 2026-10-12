---
id: 13-quality-ehs-and-compliance/ehs-produkt-anlegen-sds-660-508
title: EHS-Produkt anlegen – SDS (660) (660_S4CLD2608_Master_Data_DE_XX)
description: "German master data script 660: create an EHS product master record via Manage Product Master Data (F1602) in SAP S/4HANA Cloud Public Edition 2608, for waste management."
cluster: 13-quality-ehs-and-compliance
tags: [kb/quality-ehs-and-compliance, topic/ehs-waste-management-products]
aliases: [660_S4CLD2608_Master_Data_DE_XX]
keywords: [EHS Products and Chemical Compliance Materials for Waste, ehs product, product master data, waste management, business roles, test scripts, 660]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/660_S4CLD2608_Master_Data_DE_XX.docx]
confidence: low
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-508
topic: 13-quality-ehs-and-compliance/ehs-waste-management-products
language: DE
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# EHS-Produkt anlegen – SDS (660) (660_S4CLD2608_Master_Data_DE_XX)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/660_S4CLD2608_Master_Data_DE_XX.docx`, extracted with `mammoth`. Grouped under **EHS Products and Chemical Compliance Materials for Waste** in Quality, EHS and Compliance. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

| <!-- image omitted: unnamed --> | StammdatenskriptSAP S/4HANA Cloud Public Edition - 02-07-26 |
| --- | --- |
|  | EHS-Produkt anlegen – SDS (660) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Inhaltsverzeichnis

[1 Zweck 2](#_Toc233889861)

[2 Voraussetzungen 3](#_Toc233889862)

[2.1 Systemzugriff 3](#_Toc233889863)

[2.2 Rollen 3](#_Toc233889864)

[3 Übersichtstabelle 4](#_Toc233889865)

[4 Vorgehensweisen 5](#_Toc233889866)

[4.1 EHS-Lokationsstammdaten anlegen - Allgemeine Daten 5](#_Toc233889867)

## Zweck

Dieses Dokument beschreibt, wie Sie einen Stammdatensatz für ein EHS-Produkt für Ihr S/4HANA-System anlegen. Die Beschreibung enthält die Datensegmente, die relevant sind, damit die Stammdaten in einer "normalen" Systemumgebung funktionieren. Sie erfahren in erster Linie, welche Datensegmente und -felder mit Eingabewerten gefüllt werden müssen. Felder, die für den durch von SAP Best Practices bereitgestellten Umfang der Content-Auslieferung in S/4HANA nicht relevant sind, werden in diesem Dokument nicht behandelt, obwohl sie möglicherweise auf der Benutzeroberfläche angezeigt werden.

Ein EHS-Produktstammsatz, der wie hier beschrieben angelegt wird, kann später in Prozessen des Abfallmanagements verwendet werden.

Dieses Dokument enthält eine detaillierte Ablaufbeschreibung, anhand deren der Umfangsbestandteil nach der Lösungsaktivierung getestet werden kann; außerdem bildet es den vordefinierten Umfang der Lösung ab. Jeder Prozessschritt, Report oder Bestandteil wird in einem eigenen Abschnitt beschrieben, in dem die Interaktionen im System (Testschritte) tabellarisch dargestellt sind. Schritte, die nicht im Prozessumfang enthalten sind, aber zu Testzwecken benötigt werden, sind entsprechend gekennzeichnet. Projektspezifische Schritte sind zu ergänzen.

|  |
| --- |
| Hinweis Die Werte in diesem Testskript (Dezimalschreibweise, Datumsformate usw.) werden in US-amerikanischer Standardschreibweise dargestellt. Wenn Ihr Testsystem so eingerichtet ist, dass es eine andere Schreibweise verwendet, geben Sie die entsprechenden Werte ein. |

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

| Name | ID |
| --- | --- |
| Stammdatenexperte – Produktdaten | SAP_BR_PRODMASTER_SPECIALIST |

## Übersichtstabelle

Dieser Stammdatensatz umfasst mehrere Segmente, die in der nachfolgenden Tabelle genannt sind.

| Segment | Anwendungsrolle | App/Transaktion | Erwartete Ergebnisse |
| --- | --- | --- | --- |
| [EHS-Lokationsstammdaten anlegen - Allgemeine Daten](#unique_6) [Seite ] 5 | Stammdatenexperte – Produktdaten | Produktstammdaten verwalten (F1602) | Ein EHS-Produkt wird angelegt. |

## Vorgehensweisen

Dieser Abschnitt beschreibt die Vorgehensweisen für die einzelnen Segmente oder Prozessschritte, die Teil dieses Stammsatzes ist.

### EHS-Lokationsstammdaten anlegen - Allgemeine Daten

Zweck

Die folgende Vorgehensweise enthält Anweisungen zum Anlegen eines EHS-Produkts, das später für EHS-Abfallmanagement-Prozesse verwendet werden kann.

Vorgehensweise (mit SAP Fiori Launchpad)

| Testschrittnummer | Bezeichnung des Testschritts | Anweisung | Erwartetes Ergebnis | Kommentare |
| --- | --- | --- | --- | --- |
| 1 | Anmelden | Melden Sie sich am SAP Fiori Launchpad mit Ihren Benutzeranmeldeinformationen an. | Die Startseite wird angezeigt. |  |
| 2 | Zu den Produktstammdaten navigieren | Öffnen Sie die App Produktstammdaten verwalten (F1602). | Die App Produktstammdaten verwalten wird geöffnet und es wird ein List-Report angezeigt. |  |
| 3 | Ein Produkt anlegen | Wählen Sie im Dialogfenster Anlegen die Option Produkt. | Das Bild Stammdatensatz anlegen eines Produkts wird angezeigt. |  |
| 4 | Stammdatensätze eines Produkts auswählen | Geben Sie auf demselben Bildim Feld Produktnummer eine <Produktnummer> ein.Wählen Sie im Feld Produktart eine <Produktart>.Wählen Sie im Feld Produktgruppe eine <Produktgruppe>.Geben Sie in das Feld Beschreibung eine <Beschreibung> ein.Wählen Sie eine Basismengeneinheit über die Wertehilfe für das Feld <Basismengeneinheit>.Wählen Sie OK. | Das Produkt enthält Informationen zum Stammdatensatz. |  |
| 5 | Informationen sichern | Wählen Sie Sichern. | Das Produkt wird angelegt. |  |

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
> Flagged while digesting this document, not verified: Section 4.1 heading says 'EHS-Lokationsstammdaten anlegen' (EHS location) while content creates an EHS product; may differ from other language versions of script 660

## Connections
- part-of :: [[_cluster]]
- related-to :: [[13-quality-ehs-and-compliance/crear-un-producto-ehs-mds-660-510]]
- related-to :: [[13-quality-ehs-and-compliance/criar-um-produto-ehs-mds-660-512]]
- related-to :: [[13-quality-ehs-and-compliance/ehs-mds-660-511]]
- related-to :: [[13-quality-ehs-and-compliance/ehs-mds-660-chinese-513]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/660_S4CLD2608_Master_Data_DE_XX.docx` — full document · extracted with `mammoth` · 7,903 chars in the whole document
