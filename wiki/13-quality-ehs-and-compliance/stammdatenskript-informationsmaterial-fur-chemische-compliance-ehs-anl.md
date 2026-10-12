---
id: 13-quality-ehs-and-compliance/stammdatenskript-informationsmaterial-fur-chemische-compliance-ehs-anl
title: "Stammdatenskript: Informationsmaterial für chemische Compliance (EHS) anlegen - SDS (65Z) (65Z_S4CLD2608_Master_Data_DE_XX)"
description: German master data script (65Z) for creating a material master for EHS chemical compliance information in SAP S/4HANA Cloud Public Edition 2608 via Fiori app F4864.
cluster: 13-quality-ehs-and-compliance
tags: [kb/quality-ehs-and-compliance, topic/ehs-waste-management-products]
aliases: [65Z_S4CLD2608_Master_Data_DE_XX]
keywords: [EHS Products and Chemical Compliance Materials for Waste, ehs chemical compliance, material master, master data scripts, waste management, business roles, 65Z]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/65Z_S4CLD2608_Master_Data_DE_XX.docx]
confidence: high
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-502
topic: 13-quality-ehs-and-compliance/ehs-waste-management-products
language: DE
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Stammdatenskript: Informationsmaterial für chemische Compliance (EHS) anlegen - SDS (65Z) (65Z_S4CLD2608_Master_Data_DE_XX)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/65Z_S4CLD2608_Master_Data_DE_XX.docx`, extracted with `mammoth`. Grouped under **EHS Products and Chemical Compliance Materials for Waste** in Quality, EHS and Compliance. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

| <!-- image omitted: unnamed --> | StammdatenskriptSAP S/4HANA Cloud Public Edition - 02-07-26 |
| --- | --- |
|  | Informationsmaterial für chemische Compliance (EHS) anlegen – SDS (65Z) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Inhaltsverzeichnis

[1 Zweck 2](#_Toc233889830)

[2 Voraussetzungen 3](#_Toc233889831)

[2.1 Systemzugriff 3](#_Toc233889832)

[2.2 Rollen 3](#_Toc233889833)

[3 Übersichtstabelle 4](#_Toc233889834)

[4 Vorgehensweisen 5](#_Toc233889835)

[4.1 Einen einen Materialstammsatz für Informationen zur chemischen EHS-Compliance - Allgemeine Daten anlegen 5](#_Toc233889836)

## Zweck

Dieses Dokument beschreibt, wie Sie einen Materialstammsatz für Informationen zur chemischen EHS-Compliance für Ihr S/4HANA-System anlegen. Die Beschreibung enthält die Datensegmente, die relevant sind, damit die Stammdaten in einer "normalen" Systemumgebung funktionieren. Sie erfahren in erster Linie, welche Datensegmente und -felder mit Eingabewerten gefüllt werden müssen. Felder, die für den durch von SAP Best Practices bereitgestellten Umfang der Content-Auslieferung in S/4HANA nicht relevant sind, werden in diesem Dokument nicht behandelt, obwohl sie möglicherweise auf der Benutzeroberfläche angezeigt werden.

Ein Materialstammsatz für Informationen zur chemischen EHS-Compliance , der wie hier beschrieben angelegt wird, kann später in Prozessen des Abfallmanagements verwendet werden.

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

| Name (Rollenvorlage) | ID (Rollenvorlage) |
| --- | --- |
| Umweltschutzbeauftragter | SAP_BR_EHS_ENV_MGMT |

## Übersichtstabelle

Dieser Stammdatensatz umfasst mehrere Segmente, die in der nachfolgenden Tabelle genannt sind.

| Segment | Anwendungsrolle | App/Transaktion | Erwartete Ergebnisse |
| --- | --- | --- | --- |
| [Einen einen Materialstammsatz für Informationen zur chemischen EHS-Compliance - Allgemeine Daten anlegen](#unique_6) [Seite ] 5 | Umweltschutzbeauftragter | Materialdaten verwalten (F4864) | Ein Material für Informationen zur chemischen Compliance (CCI) von EHS wird angelegt. |

## Vorgehensweisen

Dieser Abschnitt beschreibt die Vorgehensweisen für die einzelnen Segmente oder Prozessschritte, die Teil dieses Stammsatzes ist.

### Einen einen Materialstammsatz für Informationen zur chemischen EHS-Compliance - Allgemeine Daten anlegen

Zweck

Die folgende Vorgehensweise enthält Anweisungen zum Anlegen eines Materialstammsatzes für Informationen zur chemischen EHS-Compliance, der später für EHS-Abfallmanagement-Prozesse verwendet werden kann.

Vorgehensweise (mit SAP Fiori Launchpad)

| Testschrittnummer | Bezeichnung des Testschritts | Anweisung | Erwartetes Ergebnis | Kommentare |
| --- | --- | --- | --- | --- |
| 1 | Anmelden | Melden Sie sich am SAP Fiori Launchpad mit Ihren Benutzeranmeldeinformationen an. | Die Startseite wird angezeigt. |  |
| 2 | "Kundenstammdaten verwalten" öffnen | Öffnen Sie die App Materialdaten verwalten (F4864). | Die App Materialdaten verwalten wird geöffnet, und es wird ein Listen-Report angezeigt. |  |
| 3 | Ein neues Material anlegen | Wählen Sie Anlegen.Auf dem Bild:Geben Sie im Feld <Name> einen Internen Namen ein.Wählen Sie eine <Logistikrolle> aus der Dropdown-Liste Rolle in der Logistik aus.Wählen Sie Sichern. | Die Registerkarte Neues Material wird angezeigt, und ein neues Material wird angelegt. |  |
| 4 | Produkt hinzufügen | Wählen Sie Bearbeiten.Wählen Sie im Abschnitt Produkt die Option Hinzufügen, und wählen Sie ein Produkt aus.Wählen Sie Sichern.Hinweis: Einem Material darf nur ein Produkt zugeordnet werden. | Es wird ein Produkt zum Material hinzugefügt, und die Informationen werden gesichert. |  |

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
- related-to :: [[13-quality-ehs-and-compliance/crear-un-material-de-informacion-de-conformidad-de-producto-quimico-eh]]
- related-to :: [[13-quality-ehs-and-compliance/create-an-ehs-chemical-compliance-information-material-mds-65z-503]]
- related-to :: [[13-quality-ehs-and-compliance/criar-um-material-de-informacoes-de-conformidade-quimica-ehs-mds-65z-5]]
- related-to :: [[13-quality-ehs-and-compliance/ehs-mds-65z-chinese-507]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/65Z_S4CLD2608_Master_Data_DE_XX.docx` — full document · extracted with `mammoth` · 7,388 chars in the whole document
