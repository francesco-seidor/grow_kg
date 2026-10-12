---
id: 06-management-accounting/kostenartengruppe-anlegen-sds-bnp-646
title: Kostenartengruppe anlegen - SDS (BNP) (BNP_S4CLD2608_Master_Data_DE_XX)
description: German master data script for creating a cost element group in SAP S/4HANA Cloud Public Edition via Kostenartengruppen verwalten (F5373).
cluster: 06-management-accounting
tags: [kb/management-accounting, topic/cost-element-groups]
aliases: [BNP_S4CLD2608_Master_Data_DE_XX]
keywords: [Cost Element Groups, master data scripts, business roles, controlling area, chart of accounts, overhead cost reporting, BNP]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/BNP_S4CLD2608_Master_Data_DE_XX.docx]
confidence: low
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-646
topic: 06-management-accounting/cost-element-groups
language: DE
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Kostenartengruppe anlegen - SDS (BNP) (BNP_S4CLD2608_Master_Data_DE_XX)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/BNP_S4CLD2608_Master_Data_DE_XX.docx`, extracted with `mammoth`. Grouped under **Cost Element Groups** in Management Accounting. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

| <!-- image omitted: unnamed --> | StammdatenskriptSAP S/4HANA Cloud Public Edition - 02-07-26 |
| --- | --- |
|  | Kostenartengruppe anlegen – SDS (BNP) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Inhaltsverzeichnis

[1 Verwendungszweck 2](#_Toc233889996)

[2 Voraussetzungen 3](#_Toc233889997)

[2.1 Systemzugriff 3](#_Toc233889998)

[2.2 Rollen 3](#_Toc233889999)

[2.3 Erforderliche Organisationseinheiten 3](#_Toc233890000)

[2.4 Obligatorische und optionale Stammdaten 4](#_Toc233890001)

[2.5 Wesentliche Parameter für die Datenerstellung 4](#_Toc233890002)

[3 Übersichtstabelle 5](#_Toc233890003)

[4 Testverfahren 6](#_Toc233890004)

[4.1 Kostenartengruppen-Stammdatensatz anlegen 6](#_Toc233890005)

## Verwendungszweck

Geschäftskontext

Kostenartengruppen werden üblicherweise verwendet, um Kostenelemente mit gleichartigen Merkmalen für Berichtszwecke zu erfassen. Kostenartengruppen können beispielsweise im Informationssystem verwendet werden. Sie können die Struktur der Kostenartengruppen verwenden, um die Zeilenstruktur Ihrer Berichte zu definieren. Die Summenbildung im Bericht erfolgt pro Knoten.

Sie können Kostenartengruppen auch immer dann einsetzen, wenn Sie mehrere Kostenarten in einem Vorgang verarbeiten möchten. Z.B. in der Kostenstellenplanung, Verteilung oder Umlage.

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

| Name (Rollenvorlage) | ID (Rollenvorlage) | Name (Launchpad-Bereich) | ID (Launchpad-Bereich) | Anmeldung |
| --- | --- | --- | --- | --- |
| Gemeinkostencontroller | SAP_BR_OVERHEAD_ACCOUNTANT | Gemeinkostenrechnung | SAP_BR_OVERHEAD_ACCOUNTANT |  |

### Erforderliche Organisationseinheiten

Die Organisationsstruktur und die Stammdaten Ihres Unternehmens wurden bei der Implementierung in Ihrem ERP-System angelegt. Die Organisationsstruktur gibt den Aufbau Ihres Unternehmens wieder. Die Stammdaten stehen für Kostenartengruppen, je nach betrieblichem Schwerpunkt Ihres Unternehmens.

| Datenobjekt | Verwendet im Datensegment | Obligatorisch / optional | Kommentare |
| --- | --- | --- | --- |
| Kostenrechnungskreis | Allgemeine Daten | Obligatorisch |  |

### Obligatorische und optionale Stammdaten

Kostenartengruppen-Stammdatensätze können auf andere Stammdaten verweisen. Die folgende Tabelle bietet eine Übersicht über die optionalen und obligatorischen Stammdatenobjekte, die in einem Kostenartengruppen-Stammdatensatz enthalten sein müssen.

| Stammdatenobjekt | Verwendet im Datensegment | Obligatorisch / optional | Kommentare |
| --- | --- | --- | --- |
| Kontenplan | Organisationseinheiten | Optional |  |

### Wesentliche Parameter für die Datenerstellung

Dieser Umfangsbestandteil hat keine Voraussetzungen.

## Übersichtstabelle

Dieser Umfangsbestandteil umfasst die Prozessschritte, die in der folgenden Tabelle aufgeführt werden:

|  |
| --- |
| Hinweis Wenn Ihr Systemadministrator Bereiche und Seiten auf dem SAP Fiori Launchpad aktiviert hat, enthält die Startseite nur die wesentlichen Apps, mit denen die typischen Aufgaben einer Benutzerrolle ausgeführt werden können.Alle anderen (suchbaren) Apps, die nicht auf der Startseite enthalten sind, finden Sie über die Suchleiste ([2434549](https://me.sap.com/notes/2434549)).Wenn Sie die Startseite personalisieren und versteckte Apps hinzufügen möchten, wechseln Sie in Ihr Benutzerprofil und wählen Sie App Finder. |

| Prozessschritt | Benutzerrolle | Vorgang/App | Erwartete Ergebnisse |
| --- | --- | --- | --- |
| [Kostenartengruppen-Stammdatensatz anlegen](#unique_9) [Seite ] 6 | Gemeinkostencontroller | Kostenartengruppen verwalten(F5373) | Sie können weitere Kostenartengruppen anlegen, wenn neue geschäftliche Anforderungen auftreten. |

## Testverfahren

In diesem Abschnitt werden die Testverfahren für den jeweiligen Prozessschritt beschrieben, der zum betreffenden Umfangsbestandteil gehört.

### Kostenartengruppen-Stammdatensatz anlegen

Testverwaltung

Kundenprojekt: Füllen Sie die projektbezogenen Teile aus.

|  |  |  |  |
| --- | --- | --- | --- |
| Testfall-ID | <X.XX> | Testdatum: |  |
| Testername: |  | Dauer: |  |
| Benutzerrolle(n): |  | Zuständigkeit: | <Geben Sie den Serviceanbieter, einen Kunden oder einen Serviceanbieter zusammen mit einem Kunden an.> |

Voraussetzung

Sie haben die Grunddaten für das Material eingegeben und gesichert.

Vorgehensweise

| Testschrittnummer | Bezeichnung des Testschritts | Anweisung | Erwartetes Ergebnis | Kommentare |
| --- | --- | --- | --- | --- |
| 1 | Anmelden | Melden Sie sich am SAP Fiori Launchpad als Gemeinkostencontroller an. | Das SAP Fiori Launchpad wird angezeigt. |  |
| 2 | SAP-Fiori-App aufrufen | Öffnen Sie Kostenartengruppen verwalten(F5373). | Die App wird geöffnet. |  |
| 3 | Neue Kostenartengruppe eingeben | Wählen Sie auf dem Bild Kostenartengruppen verwalten die Option Anlegen. Geben Sie auf dem Bild Kostenartengruppe anlegen: Einstieg die folgenden Einträge vor:Kostenartengruppe: <Kostenartengruppe>Wählen Sie Enter.Optional können Sie eine Referenz aus vorhandenen Kostenstellengruppen verwenden. | Das Bild Kostenartengruppe anlegen: Struktur wird angezeigt. |  |
| 4 | Kostenart und/oder Kostenartengruppe eingeben | Die neuen Stammdaten werden auf dem Bild Kostenartengruppe: Struktur angezeigt. Geben Sie Folgendes ein:Beschreibung: <Beschreibung>Außerdem können Sie folgende Einträge vornehmen, indem Sie den Cursor auf Ihre Auswahl positionieren und die folgenden Navigationsdrucktasten verwenden:Untere Stufe: <Fügen Sie eine Kostenartengruppe auf der unteren Stufe ein.>Kostenart: <(Einfügeoption) - Fügen Sie Kostenarten oder Artenbereiche hinzu.>Selbe Ebene: <Fügen Sie auf der gleichen unteren Stufe zusätzliche Kostenartengruppen ein.> | Die neuen Stammdaten werden auf dem Bild Kostenartengruppe: Struktur angezeigt. |  |
| 5 | Daten sichern | Wählen Sie Sichern. | Die Kostenartengruppe wird angelegt und gesichert. |  |

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
> Flagged while digesting this document, not verified: Prerequisite text refers to entering basic material data, which seems inconsistent with a cost element group procedure

## Connections
- part-of :: [[_cluster]]
- related-to :: [[06-management-accounting/create-cost-element-group-mds-bnp-647]]
- related-to :: [[06-management-accounting/criar-grupo-de-classes-de-custo-mds-bnp-650]]
- related-to :: [[06-management-accounting/mds-bnp-649]]
- related-to :: [[06-management-accounting/mds-bnp-651]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/BNP_S4CLD2608_Master_Data_DE_XX.docx` — full document · extracted with `mammoth` · 9,594 chars in the whole document
