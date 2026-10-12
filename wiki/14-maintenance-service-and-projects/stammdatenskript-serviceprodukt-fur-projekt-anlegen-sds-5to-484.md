---
id: 14-maintenance-service-and-projects/stammdatenskript-serviceprodukt-fur-projekt-anlegen-sds-5to-484
title: "Stammdatenskript: Serviceprodukt für Projekt anlegen – SDS (5TO) (5TO_S4CLD2608_Master_Data_DE_XX)"
description: "German SAP S/4HANA Cloud master data script 5TO: create service product PROJEKT via MM01 including sales organization data, for use in solution orders."
cluster: 14-maintenance-service-and-projects
tags: [kb/maintenance-service-and-projects, topic/solution-orders-and-cpq]
aliases: [5TO_S4CLD2608_Master_Data_DE_XX]
keywords: [Solution Orders and SAP CPQ Quotations, service product, material master, sales organization data, master data scripts, business roles, organizational units, profit center, brazil tax fields, 5TO]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/5TO_S4CLD2608_Master_Data_DE_XX.docx]
confidence: high
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-484
topic: 14-maintenance-service-and-projects/solution-orders-and-cpq
language: DE
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Stammdatenskript: Serviceprodukt für Projekt anlegen – SDS (5TO) (5TO_S4CLD2608_Master_Data_DE_XX)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/5TO_S4CLD2608_Master_Data_DE_XX.docx`, extracted with `mammoth`. Grouped under **Solution Orders and SAP CPQ Quotations** in Maintenance, Service and Projects. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

| <!-- image omitted: unnamed --> | StammdatenskriptSAP S/4HANA Cloud Public Edition - 02-07-26 |
| --- | --- |
|  | Serviceprodukt für Projekt anlegen – SDS (5TO) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Inhaltsverzeichnis

[1 Zweck 2](#_Toc233889814)

[2 Voraussetzungen 3](#_Toc233889815)

[2.1 Systemzugriff 3](#_Toc233889816)

[2.2 Rollen 3](#_Toc233889817)

[2.3 Erforderliche Organisationseinheiten 3](#_Toc233889818)

[2.4 Obligatorische und operative Stammdaten 4](#_Toc233889819)

[3 Übersichtstabelle 5](#_Toc233889820)

[4 Testverfahren 6](#_Toc233889821)

[4.1 Serviceprodukt anlegen – PROJEKT 6](#_Toc233889822)

## Zweck

Dieses Dokument beschreibt, wie Sie Stammdatensätze für das Serviceprodukt einschließlich Preise anlegen. Die Beschreibung umfasst die Datensegmente, die für die Stammdaten für die Arbeit in einer üblichen Systemumgebung relevant sind. Der Leser lernt hauptsächlich, welche Datensegmente und -felder hauptsächlich mit Eingabewerten gefüllt werden müssen. Felder, die nicht für den Umfang relevant sind, werden in diesem Dokument nicht behandelt, obwohl sie möglicherweise auf der Benutzungsoberfläche angezeigt werden.

Ein wie hier beschrieben angelegter Produktstammsatz kann für den Lösungsauftrag verwendet werden.

| Serviceproduktnummer | Beschreibung | Verwendung |
| --- | --- | --- |
| PROJEKT | Projekt | steht für das Projekt |

## Voraussetzungen

### Systemzugriff

| System | Details |
| --- | --- |
| System | Erreichbar über SAP Fiori Launchpad. Ihr Systemadministrator stellt Ihnen die URL für den Zugriff auf die verschiedenen Apps zur Verfügung, die Ihrer Rolle zugeordnet sind. |

### Rollen

Legen Sie Benutzerrollen mit den folgenden von SAP ausgelieferten Benutzerrollenvorlagen an, und ordnen Sie sie Ihren einzelnen Testbenutzern zu.

Alternativ können Sie, falls verfügbar, die folgenden von SAP ausgelieferten Bereiche verwenden. Legen Sie einen Bereich mit Seiten an, die vordefinierte grundlegende Apps enthalten, und ordnen Sie sie der Benutzerrolle zu. Anschließend ordnen Sie diese Benutzerrolle Ihren einzelnen Benutzern zu.

Weitere Informationen finden Sie unter Anwendungsrolle aus einer Vorlage anlegen in der [Product Assistance](https://help.sap.com/docs/SAP_S4HANA_CLOUD/53e36b5493804bcdb3f6f14de8b487dd/ec310a8b669a45ca898dc4dd91d97de2.html) für SAP S/4HANA Cloud Public Edition.

| Name (Rollenvorlage) | ID (Rollenvorlage) | Name (Launchpad-Bereich) | ID (Launchpad-Bereich) |
| --- | --- | --- | --- |
| Stammdatenexperte – Produktdaten | SAP_BR_PRODMASTER_SPECIALIST | Stammdaten - Produkt | SAP_CMD_SP_PR_MAINT |

### Erforderliche Organisationseinheiten

Einige Segmente von Stammdaten hängen von den Organisationseinheiten des Unternehmens ab. Allgemeine (zentrale) Daten hängen nicht von einer Organisationseinheit oder dem Buchungskreis ab. Die folgende Tabelle stellt eine Übersicht dieser verschiedenen Datensegmente und ihrer relevanten Organisationseinheiten bereit:

| Datensegment | Hängt ab von | Für die USA zu verwendende Organisationseinheit | Für DE zu verwendende Organisationseinheit |
| --- | --- | --- | --- |
| Material anlegen | Verkaufsorganisation | 1710 (Inländ. Verkaufsorganisation USA) | 1010 (Inländ. Verkaufsorganisation DE) |
| Material anlegen | Vertriebsweg | 10 (Direktverkauf) | 10 (Direktverkauf) |

### Obligatorische und operative Stammdaten

Materialstammdatensätze können auf andere Stammdaten verweisen. Die folgende Tabelle bietet eine Übersicht über die optionalen und obligatorischen Stammdatenobjekte, die in einem Materialstammdatensatz verwendet werden müssen.

|  |
| --- |
| Hinweis Für eine ordnungsgemäße Steuerberechnung sind brasilienspezifische Felder erforderlich.Prüfen Sie Nota Fiscal – Brasilien - JD0 im Kapitel BR-spezifische Felder für Stammdaten definieren für Materialstammdaten. |

| Stammdatenobjekt | Verwendet im Datensegment | Obligatorisch / optional | Kommentare |
| --- | --- | --- | --- |
| Profitcenter |  | obligatorisch | Für einwandfreie Bewertungsprozesse ist die Zuweisung eines Profitcenters zu einem Material- oder Produktstamm erforderlich. |

## Übersichtstabelle

Dieser Stammdatensatz umfasst mehrere Segmente, die in der nachfolgenden Tabelle genannt sind.

Wenn Ihr Systemadministrator Bereiche und Seiten auf dem SAP Fiori Launchpad aktiviert hat, enthält die Startseite nur die wesentlichen Apps, mit denen die typischen Aufgaben einer Benutzerrolle ausgeführt werden können.

Alle anderen Apps, die nicht auf der Startseite enthalten sind, finden Sie über die Suchleiste.

Wenn Sie die Startseite personalisieren und versteckte Apps hinzufügen möchten, wechseln Sie in Ihr Benutzerprofil und wählen Sie Einstellungen > App Finder.

| ID (Rollenvorlage) | Benutzerrolle | App/Transaktion | Erwartete Ergebnisse |
| --- | --- | --- | --- |
| Serviceprodukt anlegen | SAP_BR_PRODMASTER_SPECIALIST | Material anlegen (MM01) | Serviceprodukte werden angelegt. |

## Testverfahren

Dieser Abschnitt beschreibt die Vorgehensweisen für jedes Segment oder Prozessschritt, das bzw. der Teil dieses Stammsatzes ist.

### Serviceprodukt anlegen – PROJEKT

Zweck

| Testschrittnummer | Bezeichnung des Testschritts | Anweisung | Erwartetes Ergebnis | Kommentare |
| --- | --- | --- | --- | --- |
| 1 | Anmelden | Melden Sie sich am SAP Fiori Launchpad als Stammdatenexperte – Produktdaten (MDG) an. |  |  |
| 2 | SAP-Fiori-App aufrufen | Wählen Sie die Kachel Material anlegen(MM01). | Das Bild Material anlegen (Einstieg) wird angezeigt. |  |
| 3 | Materialgrunddaten (für Serviceprodukt) pflegen | Nehmen Sie auf dem Bild Material anlegen (Einstieg), die folgenden Einträge vor:Material:PROJEKTMaterialart: ServiceproduktWählen Sie anschließend Weiter (Enter). | Sie haben die grundlegenden Informationen für das neue Serviceprodukt erfasst.Das Dialogfenster Sichtenauswahl wird angezeigt. |  |
| 4 | Sichten wählen | Wählen Sie in der Sicht Sichtenauswahl - Grunddaten 1, und wählen Sie Weiter (Enter). | Die Sicht Material PROJEKT anlegen wird angezeigt. |  |
| 5 | Grunddaten pflegen | Pflegen Sie in der Sicht Grunddaten 1 die folgenden Werte:Beschr.:ProjektpositionBasismengeneinheit:AU (Leistungseinheit)Materialgruppe:P001 (Dienstleistungen)AllgPosGrp:SPRJ (Projekt)Wählen Sie anschließend Sichern. | Die Grunddaten sind gepflegt, und das Serviceprodukt ist gesichert.Nach dem Sichern wird die Sicht Material anlegen (Einstieg) angezeigt.Wenn Sie verschiedene Sprachen in Ihrem Unternehmen verwenden, müssen Sie für jeden relevanten Sprachencode die entsprechende Beschreibung für das Produkt pflegen. |  |
| 6 | Produktdetails erweitern | Geben Sie in der Sicht Material anlegen (Einstieg) das Material PROJEKT ein, und wählen Sie Weiter (Enter). | Das Dialogfenster Sichtenauswahl wird angezeigt. |  |
| 7 | Sichten wählen | Wählen Sie im Fenster Sichtenauswahl die folgenden Sichten aus:Verkauf: VerkaufsorgDaten 1Verkauf: VerkaufsorgDaten 2Wählen Sie anschließend Weiter (Enter). | Das Dialogfenster Organisationsebenen wird angezeigt. |  |
| 8 | Organisationsebenen wählen | Geben Sie im Dialogfenster Organisationsebenen die folgenden Werte ein:Verkaufsorganisation: 1710 (Inländ. Verkaufsorganisation USA)Vertriebsweg: 10 (Direktverkauf)Wählen Sie anschließend Weiter (Enter). | Es wurden Organisationsdaten ausgewählt.Die Sicht Material PROJEKT anlegen wird angezeigt. |  |
| 9 | Verkaufsorganisationsdaten (1) pflegen | Geben Sie in der Sicht Verkauf: VerkOrg 1 die folgenden Werte ein:Allgemeine DatenSkonto: X <markiert>SteuerdatenSteuerklassifikation: 1 (volle Steuer)Wählen Sie anschließend Enter. | Die Verkaufsorganisationsdaten sind erfasst. Die Registerkarte Verkauf: VerkOrg 2 wird angezeigt. |  |
| 10 | Verkaufsorganisationsdaten (2) pflegen | Geben Sie in der Sicht Verkauf: VerkOrg 2 die folgenden Daten ein:Positionstypengruppe:SPRJ (Projekt)Wählen Sie anschließend Enter.Wählen Sie anschließend Sichern. | Die Verkaufsorganisationsdaten sind erfasst. Die Registerkarte Verkauf: Allg./Werk wird angezeigt. |  |

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
- related-to :: [[14-maintenance-service-and-projects/creacion-de-producto-de-servicio-para-proyecto-mds-5to-486]]
- related-to :: [[14-maintenance-service-and-projects/criar-produto-de-servico-para-projeto-mds-5to-488]]
- related-to :: [[14-maintenance-service-and-projects/master-data-script-create-service-product-for-project-5to-485]]
- related-to :: [[14-maintenance-service-and-projects/mds-5to-487]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/5TO_S4CLD2608_Master_Data_DE_XX.docx` — full document · extracted with `mammoth` · 10,609 chars in the whole document
