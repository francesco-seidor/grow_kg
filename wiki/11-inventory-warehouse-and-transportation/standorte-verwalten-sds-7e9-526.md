---
id: 11-inventory-warehouse-and-transportation/standorte-verwalten-sds-7e9-526
title: Standorte verwalten - SDS (7E9) (7E9_S4CLD2608_Master_Data_DE_XX)
description: SAP S/4HANA Cloud 2608 master data script (DE) for creating locations via Manage Locations (F6225) as transportation management master data expert.
cluster: 11-inventory-warehouse-and-transportation
tags: [kb/inventory-warehouse-and-transportation, topic/transportation-locations]
aliases: [7E9_S4CLD2608_Master_Data_DE_XX]
keywords: [Transportation Locations, locations, master data script, location types, un/locode, airport codes, transportation management, 7E9]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/7E9_S4CLD2608_Master_Data_DE_XX.docx]
confidence: high
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-526
topic: 11-inventory-warehouse-and-transportation/transportation-locations
language: DE
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Standorte verwalten - SDS (7E9) (7E9_S4CLD2608_Master_Data_DE_XX)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/7E9_S4CLD2608_Master_Data_DE_XX.docx`, extracted with `mammoth`. Grouped under **Transportation Locations** in Inventory, Warehouse and Transportation. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

| <!-- image omitted: unnamed --> | StammdatenskriptSAP S/4HANA Cloud Public Edition - 02-07-26 |
| --- | --- |
|  | Standorte verwalten – SDS (7E9) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Inhaltsverzeichnis

[1 Zweck 2](#_Toc233889876)

[2 Voraussetzungen 3](#_Toc233889877)

[2.1 Systemzugriff 3](#_Toc233889878)

[2.2 Rollen 3](#_Toc233889879)

[2.3 Wesentliche Parameter für die Datenerstellung 3](#_Toc233889880)

[2.3.1 Lokationstypen 3](#_Toc233889881)

[2.3.2 UN/LOCODE definieren 4](#_Toc233889882)

[2.3.3 Flughafencodes definieren 4](#_Toc233889883)

[3 Übersichtstabelle 5](#_Toc233889884)

[4 Testverfahren 6](#_Toc233889885)

[4.1 Lokationen verwalten 6](#_Toc233889886)

## Zweck

Dieses Dokument beschreibt, wie Sie einen Lokationsstammdatensatz für Ihr SAP S/4HANA Cloud Public Edition-System anlegen. Die Beschreibung umfasst die Datensegmente, die für die Stammdaten für die Arbeit in einer üblichen Systemumgebung relevant sind. Sie lernen hauptsächlich, welche Datensegmente und -felder üblicherweise mit Eingabewerten gefüllt werden müssen. Felder, die für den durch von SAP Best Practices bereitgestellten Umfang der Content-Auslieferung in SAP S/4HANA Cloud Public Edition nicht relevant sind, werden in diesem Dokument nicht behandelt, obwohl sie möglicherweise auf der Benutzeroberfläche angezeigt werden.

## Voraussetzungen

### Systemzugriff

| System | Details |
| --- | --- |
| System | Zugriff möglich über das SAP Fiori Launchpad. Ihr Systemadministrator stellt Ihnen die URL für den Zugriff auf die verschiedenen Apps zur Verfügung, die Ihrer Rolle zugeordnet sind. |

### Rollen

Legen Sie Benutzerrollen mit den folgenden von SAP ausgelieferten Benutzerrollenvorlagen an, und ordnen Sie sie Ihren einzelnen Testbenutzern zu.

Alternativ können Sie, falls verfügbar, die folgenden von SAP ausgelieferten Bereiche verwenden. Legen Sie einen Bereich mit Seiten an, die vordefinierte grundlegende Apps enthalten, und ordnen Sie sie der Benutzerrolle zu. Anschließend ordnen Sie diese Benutzerrolle Ihren einzelnen Benutzern zu.

Weitere Informationen finden Sie unter Anwendungsrolle aus einer Vorlage anlegen in der [Product Assistance](https://help.sap.com/docs/SAP_S4HANA_CLOUD/53e36b5493804bcdb3f6f14de8b487dd/ec310a8b669a45ca898dc4dd91d97de2.html) für SAP S/4HANA Cloud Public Edition.

| Name (Rollenvorlage) | ID (Rollenvorlage) | Name (Launchpad-Bereich) | ID (Launchpad-Bereich) |
| --- | --- | --- | --- |
| Stammdatenexperte – Transportation Management | SAP_BR_TRANSP_MDSPEC | Transportstammdaten | SAP_BR_TRANSP_MDSPEC |

### Wesentliche Parameter für die Datenerstellung

In diesem Abschnitt werden einige Basisparameter beschrieben, die das Verhalten eines Stammsatzes beeinflussen und zum Anlegen eines <Typ>-Stammdatensatzes immer erforderlich sind.

#### Lokationstypen

Für die Zuordnung der Lokationstypen stehen Ihnen folgende Möglichkeiten zur Verfügung:

| Name | ID |
| --- | --- |
| Port | 1100 |
| Flughafen | 1110 |
| Bahnhof | 1120 |
| Eisenbahnknoten | 1190 |
| Ladestelle | 1200 |

#### UN/LOCODE definieren

Sie können "United Nations Codes for Trade and Transport Locations" (UN/LOCODES) definieren.

Verwenden Sie die Suchfunktion in Ihrer Konfigurationsumgebung, um die folgende Aktivität zu finden: Weitere Informationen finden Sie unter [Konfigurationsumgebung von SAP S/4HANA Cloud Public Edition](https://help.sap.com/docs/SAP_S4HANA_CLOUD/b249d650b15e4b3d9fc2077ee921abd0/0b3f87579f345c08e10000000a441470.html).

#### Flughafencodes definieren

Sie können Flughafencodes definieren.

Verwenden Sie die Suchfunktion in Ihrer Konfigurationsumgebung, um die folgende Aktivität zu finden: Weitere Informationen finden Sie unter [Konfigurationsumgebung von SAP S/4HANA Cloud Public Edition](https://help.sap.com/docs/SAP_S4HANA_CLOUD/61e246f4b34c4e1790d8b7651c0b40a8/0b3f87579f345c08e10000000a441470.html?state=DRAFT).

## Übersichtstabelle

Dieser Stammdatensatz umfasst mehrere Segmente, die in der nachfolgenden Tabelle genannt sind.

| Segment | Anwendungsrolle | App/Vorgang | Erwartete Ergebnisse |
| --- | --- | --- | --- |
| [Lokationen verwalten](#unique_10) [Seite ] 6 | Stammdatenexperte – Transportation Management | Lokationen verwalten(F6225) |  |

## Testverfahren

Dieser Abschnitt beschreibt die Vorgehensweisen für die einzelnen Segmente oder Prozessschritte, die Teil dieses Stammsatzes ist.

### Lokationen verwalten

Zweck

Die folgenden Schritte zeigen Ihnen, wie Sie Lokationen anlegen.

Vorgehensweise

| Testschrittnummer | Bezeichnung des Testschritts | Anweisungen | Erwartetes Ergebnis | Kommentare |
| --- | --- | --- | --- | --- |
| 1 | Anmelden | Melden Sie sich im SAP Fiori Launchpad als Stammdatenexperte – Transportation Management an. | Das SAP Fiori Launchpad wird angezeigt. |  |
| 2 | App aufrufen | Öffnen Sie Lokationen verwalten(F6225). | Das Bild Lokationsstamm verwalten(F6225) wird angezeigt. |  |
| 3 | "Anlegen" wählen | Wählen Sie Anlegen. | Das Dialogfenster Anlegen wird angezeigt. |  |
| 4 | Details eingeben | Geben Sie im Dialogfenster Anlegen Folgendes ein:Lokation:<Ihre Lokation>Lokationstyp:<Ihr Lokationstyp> |  |  |
| 5 | "Weiter" wählen | Wählen Sie Weiter. | Das Bild Lokation wird angezeigt. |  |
| 6 | Allgemeine Informationen eingeben | Geben Sie auf der Registerkarte Allgemeine Informationen Folgendes ein:Lok. beschreibung:<Ihre Lokationsbeschreibung> |  |  |
| 7 | Adressdaten eingeben | Geben Sie auf der Registerkarte Adresse Folgendes ein:Straße:<Straße>Postleitzahl: <Postleitzahl>Land/Region: <Land/Region>House Number: <Hausnummer>City: <Ort>Region: <Region>Zeitzone: <Zeitzone>Suchbegriff 1: <Suchbegriff> |  |  |
| 8 | Identifikationsdaten eingeben | Geben Sie auf der Registerkarte Identifikation Folgendes ein:UN/LOCODE: <UN/LOCODE>Flughafencode: <Flughafencode> |  |  |
| 9 | "Geokoordinaten berechnen" wählen | Wählen Sie Geokoordinaten berechnen. | Die Geokoordinaten wurden automatisch ermittelt und auf der Registerkarte Geokoordinaten eingetragen. |  |
| 10 | "Anlegen" wählen | Wählen Sie Anlegen. | Die folgende Systemmeldung wird angezeigt:Lokation <Ihre Lokation> erfolgreich angelegt |  |

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
- related-to :: [[11-inventory-warehouse-and-transportation/administrar-localizacoes-mds-7e9-530]]
- related-to :: [[11-inventory-warehouse-and-transportation/gestion-de-ubicaciones-mds-7e9-528]]
- related-to :: [[11-inventory-warehouse-and-transportation/manage-locations-mds-7e9-527]]
- related-to :: [[11-inventory-warehouse-and-transportation/mds-7e9-529]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/7E9_S4CLD2608_Master_Data_DE_XX.docx` — full document · extracted with `mammoth` · 8,751 chars in the whole document
