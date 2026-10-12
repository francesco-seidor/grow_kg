---
id: 11-inventory-warehouse-and-transportation/attribute-fur-lagerprodukte-pflegen-sds-3kq-328
title: Attribute für Lagerprodukte pflegen – SDS (3KQ) (3KQ_S4CLD2608_Master_Data_DE_XX)
description: "German SAP S/4HANA Cloud Public 2608 master data script 3KQ: maintaining warehouse product attributes via Warehouse Monitor (mass) or Manage Product Master Data (F1602)."
cluster: 11-inventory-warehouse-and-transportation
tags: [kb/inventory-warehouse-and-transportation, topic/ewm-warehouse-product-attributes]
aliases: [3KQ_S4CLD2608_Master_Data_DE_XX]
keywords: [EWM Warehouse Product Attributes, warehouse product attributes, warehouse monitor, product master data, mass change products, putaway and removal control, replenishment, storage type data, business roles, 3KQ]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/3KQ_S4CLD2608_Master_Data_DE_XX.docx]
confidence: high
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-328
topic: 11-inventory-warehouse-and-transportation/ewm-warehouse-product-attributes
language: DE
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Attribute für Lagerprodukte pflegen – SDS (3KQ) (3KQ_S4CLD2608_Master_Data_DE_XX)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/3KQ_S4CLD2608_Master_Data_DE_XX.docx`, extracted with `mammoth`. Grouped under **EWM Warehouse Product Attributes** in Inventory, Warehouse and Transportation. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

| <!-- image omitted: unnamed --> | StammdatenskriptSAP S/4HANA Cloud Public Edition - 02-07-26 |
| --- | --- |
|  | Attribute für Lagerprodukte pflegen – SDS (3KQ) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Inhaltsverzeichnis

[1 Zweck 2](#_Toc233889637)

[2 Voraussetzungen 3](#_Toc233889638)

[2.1 Systemzugriff 3](#_Toc233889639)

[2.2 Rollen 3](#_Toc233889640)

[2.3 Erforderliche Organisationseinheiten 3](#_Toc233889641)

[2.4 Obligatorische und optionale Stammdaten 4](#_Toc233889642)

[3 Übersichtstabelle 5](#_Toc233889643)

[4 Testverfahren 6](#_Toc233889644)

[4.1 Attribute für Lagerprodukte pflegen – mit Lagermonitor 6](#_Toc233889645)

[4.2 Attribute für Lagerprodukte pflegen 7](#_Toc233889646)

## Zweck

In diesem Dokument lernen Sie, wie Sie lagerrelevante Attribute für Ihr Material/Ihren Produktstamm anlegen. Es gibt zwei Optionen zur Pflege der Lagerattribute:

- Sie können Lagerproduktattribute mit der App Lagermonitor(/SCWM/MON) pflegen. Diese App kann für die Einzel- und Massenänderung verwendet werden.
- Sie können Lagerproduktattribute mit der App Produktstammdaten verwalten(F1602) pflegen. Diese App kann für die Einzeländerung verwendet werden.

Dieses Dokument umfasst die Datensegmente, die für die Stammdaten für die Arbeit in einer normalen Systemumgebung relevant sind. Der Leser lernt hauptsächlich, welche Datensegmente und -felder hauptsächlich mit Eingabewerten gefüllt werden müssen. Felder, die für den von SAP Best Practices bereitgestellten Umfang der Content-Auslieferung in SAP S/4HANA nicht relevant sind, werden in diesem Dokument nicht behandelt, obwohl sie möglicherweise auf der Benutzeroberfläche angezeigt werden.

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
| Stammdatenexperte – Produktdaten | SAP_BR_PRODMASTER_SPECIALIST | Stammdaten – Produkte / Produkt-Governance | SAP_BR_PRODMASTER_SPECIALIST / SAP_CMD_SPT_PR_GOV_PC |

### Erforderliche Organisationseinheiten

Einige Segmente der Stammdaten hängen von den Organisationseinheiten des Unternehmens ab. Allgemeine (zentrale) Daten sind nicht von einer Organisationseinheit oder dem Buchungskreis abhängig. Die folgende Tabelle stellt eine Übersicht dieser verschiedenen Datensegmente und ihrer relevanten Organisationseinheiten bereit:

| Datensegment | Hängt ab von | Feldbeispiele | Kommentare | Zu verwendende Organisationseinheit |
| --- | --- | --- | --- | --- |
| Alle | Lagernummer |  |  |  |

### Obligatorische und optionale Stammdaten

Stammdatensätze können auf andere Stammdaten verweisen. Die folgende Tabelle bietet eine Übersicht über die optionalen und obligatorischen Stammdatenobjekte, die in einem <Typ>-Stammdatensatz verwendet werden müssen.

| Stammdatenobjekt | Verwendet im Datensegment | Obligatorisch / optional | Kommentare |
| --- | --- | --- | --- |
| Geschäftspartner | Attribute für Lagerprodukte pflegen | Obligatorisch | Geschäftspartner als Verfügungsberechtigte für das Lager |

## Übersichtstabelle

Dieser Stammdatensatz umfasst mehrere Segmente, die in der nachfolgenden Tabelle genannt sind.

|  |
| --- |
| Hinweis Wenn Ihr Systemadministrator Bereiche und Seiten auf dem SAP Fiori Launchpad aktiviert hat, enthält die Startseite nur die wesentlichen Apps, mit denen die typischen Aufgaben einer Benutzerrolle ausgeführt werden können.Alle anderen (suchbaren) Apps, die nicht auf der Startseite enthalten sind, finden Sie über die Suchleiste ([2434549](https://me.sap.com/notes/2434549)).Wenn Sie die Startseite personalisieren und versteckte Apps hinzufügen möchten, wechseln Sie in Ihr Benutzerprofil und wählen Sie App Finder. |

| Segment | Anwendungsrolle | App/Vorgang | Erwartete Ergebnisse |
| --- | --- | --- | --- |
| [Attribute für Lagerprodukte pflegen – mit Lagermonitor](#unique_7) [Seite ] 6 | Lagerist (EWM) | Lagermonitor(/SCWM/MON) | Eine Massenänderung von Lagerprodukten wird durchgeführt. |
| [Attribute für Lagerprodukte pflegen](#unique_8) [Seite ] 7 | Stammdatenexperte – Produktdaten | Produktstammdaten verwalten(F1602) | Lagerattribute werden für die Materialstammdaten angelegt. |

## Testverfahren

Dieser Abschnitt beschreibt die Vorgehensweisen für die einzelnen Segmente oder Prozessschritte, die Teil dieses Stammsatzes ist.

### Attribute für Lagerprodukte pflegen – mit Lagermonitor

Zweck

In diesem Abschnitt pflegen Sie Lagerproduktattribute mit der App Lagermonitor(/SCWM/MON). Diese App kann für die Einzel- und Massenänderung verwendet werden.

Vorgehensweise

| Testschrittnummer | Bezeichnung des Testschritts | Anweisungen | Erwartetes Ergebnis | Kommentare |
| --- | --- | --- | --- | --- |
| 1 | Anmelden | Melden Sie sich am SAP Fiori Launchpad als Lagerist (EWM) an. |  |  |
| 2 | App aufrufen | Öffnen Sie Lagermonitor(/SCWM/MON). | Das Bild Lagerverwaltungsmonitor SAP - Lagernummer XX50 wird angezeigt. |  |
| 3 | Menü wählen | In der Hierarchie im linken Bildbereich wählen Sie Produktstammdaten > Lagerattribut. |  |  |
| 4 | Produktnummer eingeben | Geben Sie im Dialogfenster /SCWM/SAPLPROD_OVERVIEW folgende Daten ein:Abschnitt Basisattribute:Produktnummer: <Produktnummer> zu <Produktnummer>Abschnitt Zusatzoptionen:Nur Produkte ohne Lagerdaten: XWählen Sie Ausführen. | Im rechten Bildbereich zeigt das System die Produkte an, für die noch keine Lagerdaten gepflegt wurden. |  |
| 5 | Produkte auswählen | Im Bereich Lagerattribute wählen Sie die Produkte aus, und wählen Sie dann Weitere Methoden > Massenänderung/-erstellung. |  |  |
| 6 | Produkte auswählen | Geben Sie in das Dialogfenster /SCWM/SAPLPROD_OVERVIEW ggf. folgende Daten ein.Im Abschnitt Lagerdaten:EinlagerSteuerkz.AuslagerSteuerkz.Blocklagerkennz.Cycle-Counting-KennzeichenProzessartFindKnWählen Sie Ausführen.Hinweis Im Cloud-Warehouse-Management werden das Einlagerungssteuerkennzeichen und das Auslagerungssteuerkennzeichen in der Regel mit dem gleichen Wert angegeben. Im Nachschubprozess im Lager müssen diese beiden Felder jedoch mit verschiedenen Werte gepflegt werden, um den Prozess zu ermöglichen. |  |  |
| 7 | Daten sichern | Bestätigen Sie die Änderungen im Dialogfenster. | Eine Systemmeldung teilt Ihnen mit, dass die Produkte erfolgreich gesichert wurden. |  |

### Attribute für Lagerprodukte pflegen

Zweck

In diesem Abschnitt finden Sie eine Beschreibung, wie Sie mit der App Produktstammdaten verwalten(F1602) Lagerproduktattribute pflegen. Diese App kann für die Einzeländerung verwendet werden.

Vorgehensweise

| Testschrittnummer | Bezeichnung des Testschritts | Anweisung | Erwartetes Ergebnis | Kommentare |
| --- | --- | --- | --- | --- |
| 1 | Anmelden | Melden Sie sich am SAP Fiori Launchpad als Stammdatenexperte – Produktdaten an. |  |  |
| 2 | App aufrufen | Öffnen Sie Produktstammdaten verwalten(F1602)． |  |  |
| 3 | Materialnummer eingeben | Geben Sie auf dem Bild Produktstammdaten verwalten(F1602) folgende Daten ein:Produkt: <Materialnummer>Wählen Sie Start. | Die Materialstammdaten werden im Abschnitt Produkt angezeigt. |  |
| 4 | Material auswählen | Markieren Sie die Zeile mit den Materialstammdaten. |  |  |
| 5 | Lagerverwaltung wählen | Wählen Sie auf dem Bild Produkt die Registerkarte Lagerverwaltung, und wechseln Sie zu Lagerverwaltung > Lager. |  |  |
| 6 | Materialstammdaten ändern | Wählen Sie auf dem Bild Produkt die Option Bearbeiten. |  |  |
| 7 | Lagerdaten hinzufügen | Wählen Sie im Abschnitt Lager die Lagernummer für Ihr Lager aus.Wenn Ihre Lagernummer nicht vorhanden ist, wählen Sie Anlegen. |  |  |
| 8 | Werte eingeben | Geben Sie auf dem Bild Lager folgende Daten ein:Im Abschnitt Allgemeine Informationen:Lager: <EWM-Lagernummer>Verfügungsberechtigter: <Geschäftspartner-ID für den Verfügungsberechtigten>Kennzeichen für ProzessartfindungCycle-Counting-KennzeichenHinweis Nur die Eingabe in den Feldern Lager und Verfügungsberechtigter ist obligatorisch. Die folgenden Werte sind optional.Im Abschnitt Einlagerung:EinlagerungssteuerkennzeichenIm Abschnitt Auslagerung:AuslagerungssteuerkennzeichenHinweis Im Cloud-Warehouse-Management werden das Einlagerungssteuerkennzeichen und das Auslagerungssteuerkennzeichen mit dem gleichen Wert angegeben. Im Nachschubprozess im Lager müssen diese beiden Felder jedoch mit verschiedenen Werte gepflegt werden, um den Prozess zu ermöglichen. |  |  |
|  | Lagertypdaten für Nachschub anlegen | Im Abschnitt Lagertypen wählen Sie anlegen.Geben Sie auf dem Bild Neuer Datensatz - Lagertyp die folgenden Daten ein:Im Abschnitt Allgemeine Informationen:Lagertyp: <Lagertyp>Maximale Anzahl Plätze: <Anzahl der Lagerplätze>:Im Abschnitt Nachschub:Mindestnachschubmenge/AnzMeh: <Menge>/<ME>Mindestmenge/AnzMeh: <Menge>/<ME>Maximale Menge/AnzMeh: <Menge>/<ME> |  |  |
| 9 | Daten sichern | Wählen Sie Übernehmen. | Die Lagerdaten werden gesichert. |  |
| 10 | Zurück zum Bild "Produkt" gehen | Navigieren Sie zum Bild Produkt zurück. |  |  |
| 11 | "Lagerverwaltung" wählen | Wählen Sie auf dem Bild Produkt die Registerkarte Werke aus. |  |  |
| 12 | Werksdaten hinzufügen | Wählen Sie im Abschnitt Werke das Werk aus.Wenn Ihr Werk nicht vorhanden ist, wählen Sie Anlegen. |  |  |
| 13 | Werte eingeben | Geben Sie auf dem Bild Werk im Abschnitt "Allgemeine Informationen" folgende Daten ein:Serialnummernprofil: <Serialnummernprofil> |  |  |
| 14 | Daten sichern | Wählen Sie Übernehmen. | Die Werksdaten werden gesichert. |  |

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
- related-to :: [[11-inventory-warehouse-and-transportation/actualizar-atributos-de-productos-de-almacen-mds-3kq-es-330]]
- related-to :: [[11-inventory-warehouse-and-transportation/master-data-script-maintain-warehouse-products-attributes-3kq-329]]
- related-to :: [[11-inventory-warehouse-and-transportation/mds-3kq-331]]
- related-to :: [[11-inventory-warehouse-and-transportation/mds-3kq-333]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/3KQ_S4CLD2608_Master_Data_DE_XX.docx` — full document · extracted with `mammoth` · 13,169 chars in the whole document
