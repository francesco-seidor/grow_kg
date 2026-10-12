---
id: 13-quality-ehs-and-compliance/ehs-lokation-anlegen-sds-3sr-358
title: EHS-Lokation anlegen – SDS (3SR) (3SR_S4CLD2608_Master_Data_DE_XX)
description: "German SAP S/4HANA Cloud master data script (3SR): create an EHS location in the location structure using Manage Locations (EHFND_UI_LOC_ENTRY)."
cluster: 13-quality-ehs-and-compliance
tags: [kb/quality-ehs-and-compliance, topic/ehs-locations]
aliases: [3SR_S4CLD2608_Master_Data_DE_XX]
keywords: [EHS Locations, ehs location, location structure, environment health and safety, business roles, responsible persons, location activation, 3SR]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/3SR_S4CLD2608_Master_Data_DE_XX.docx]
confidence: high
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-358
topic: 13-quality-ehs-and-compliance/ehs-locations
language: DE
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# EHS-Lokation anlegen – SDS (3SR) (3SR_S4CLD2608_Master_Data_DE_XX)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/3SR_S4CLD2608_Master_Data_DE_XX.docx`, extracted with `mammoth`. Grouped under **EHS Locations** in Quality, EHS and Compliance. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

| <!-- image omitted: unnamed --> | StammdatenskriptSAP S/4HANA Cloud Public Edition - 02-07-26 |
| --- | --- |
|  | EHS-Lokation anlegen – SDS (3SR) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Inhaltsverzeichnis

[1 Verwendungszweck 2](#_Toc233889663)

[2 Voraussetzungen 3](#_Toc233889664)

[2.1 Systemzugriff 3](#_Toc233889665)

[2.2 Rollen 3](#_Toc233889666)

[3 Übersichtstabelle 4](#_Toc233889667)

[4 Vorgehensweisen 5](#_Toc233889668)

[4.1 EHS-Lokationsstammdaten anlegen - Allgemeine Daten 5](#_Toc233889669)

## Verwendungszweck

Mit diesem Dokument können Sie eine EHS-Lokation in der Lokationsstruktur anlegen. Die EHS-Lokation ist ein zentrales Stammdatenobjekt, das in Environment, Health, and Safety verwendet wird. Das Anlegen von EHS-Lokationen, die in einer Lokationsstruktur organisiert sind, ist Teil der Erstkonfiguration der Lösung, und Standorte werden in weiteren Prozessen verwendet, die Teil der Lösung sind.

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
| Fachkraft für Arbeitssicherheit (Unfallmanager) | SAP_BR_INDUSTRIAL_HYGIENIST | Arbeitssicherheit | SAP_BR_INDUSTRIAL_HYGIENIST |  |
| Umweltschutzbeauftragter | SAP_BR_EHS_ENV_MGMT | Umweltmanagement | SAP_BR_EHS_ENV_MGMT |  |
| Änderungsmanagement-Koordinator | SAP_BR_CHG_MGMT_COORDINATOR | Management of Change | SAP_BR_CHG_MGMT_COORDINATOR |  |

## Übersichtstabelle

Dieser Stammdatensatz umfasst mehrere Segmente, die in der nachfolgenden Tabelle genannt sind.

|  |
| --- |
| Hinweis Wenn Ihr Systemadministrator Bereiche und Seiten auf dem SAP Fiori Launchpad aktiviert hat, enthält die Startseite nur die wesentlichen Apps, mit denen die typischen Aufgaben einer Benutzerrolle ausgeführt werden können.Alle anderen (suchbaren) Apps, die nicht auf der Startseite enthalten sind, finden Sie über die Suchleiste ([2434549](https://me.sap.com/notes/2434549)).Wenn Sie die Startseite personalisieren und versteckte Apps hinzufügen möchten, wechseln Sie in Ihr Benutzerprofil und wählen Sie App Finder. |

| Segment | Anwendungsrolle | Transaktion/App | Erwartete Ergebnisse |
| --- | --- | --- | --- |
| [EHS-Lokationsstammdaten anlegen - Allgemeine Daten](#unique_6) [Seite ] 5 | Fachkraft für ArbeitssicherheitUmweltschutzbeauftragterÄnderungsmanagement-Koordinator | Lokationen verwalten(EHFND_UI_LOC_ENTRY) | Eine EHS-Lokation wird angelegt und der EHS-Lokationsstruktur zugeordnet. |

## Vorgehensweisen

In diesem Abschnitt werden die Testverfahren für den jeweiligen Prozessschritt beschrieben, der zum betreffenden Umfangsbestandteil gehört.

### EHS-Lokationsstammdaten anlegen - Allgemeine Daten

Zweck

In diesem Verfahren wird erläutert, wie Sie eine EHS-Lokation anlegen und einer EHS-Lokationsstruktur zuordnen.

Vorgehensweise

| Testschrittnummer | Bezeichnung des Testschritts | Anweisungen | Erwartetes Ergebnis | Bestanden/Nicht bestanden/Anmerkung |
| --- | --- | --- | --- | --- |
| 1 | Anmelden | Melden Sie sich mit einer der folgenden Rollen am SAP Fiori Launchpad an:Fachkraft für ArbeitssicherheitUmweltschutzbeauftragterÄnderungsmanagement-Koordinator | Das SAP Fiori Launchpad wird mit den Abschnitten und Kacheln für die jeweilige Rolle angezeigt. |  |
| 2 | Zur Lokationsstruktur navigieren | Öffnen Sie Lokationen verwalten(EHFND_UI_LOC_ENTRY). | Das Bild Lokationen wird angezeigt. In der Lokationsstruktur sind anfangs Alle Lokationsstrukturen auf oberster Ebene angeordnet. |  |
| 3 | Lokation anlegen | Wählen Sie Lokationsstruktur bearbeiten.Auf dem Bild Lokationsstruktur:Wählen Sie die Zeile Alle Lokationen.Wählen Sie Neu.Auf dem Bild Lokation anlegen:Geben Sie in dem Feld Lokation einen <Lokationsnamen> ein.Wählen Sie für das Feld Lokationstyp über die Wertehilfe einen <Lokationstyp> aus.Geben Sie als Revisionsbeginndatum das Datum 01.01.2000 ein.Wählen Sie Sichern.Wählen Sie Zur Lokationsstruktur zurückkehren.Auf dem Bild Lokationsstruktur:Sichern Sie Ihre Eingaben. | Die Lokation mit dem Namen <Lokationsname> wird angelegt und in der Lokationsstruktur gespeichert. |  |
| 4 | Lokation bearbeiten | Auf dem Bild Lokationsstruktur:Wählen Sie in der Spalte Name die Verknüpfung <Lokationsname>. | Die App Lokation bearbeiten wird angezeigt. |  |
| 5 | Grundlegende Informationen hinzufügen | Auf dem Bild Lokation: <Lokationsname> auf der Registerkarte Grundlegende Informationen:Fügen Sie im Feld Beschreibung den Text <Lokationsbeschreibung> hinzu.Wählen Sie neben dem Feld Lokation die Option Übersetzungen. Fügen Sie übersetzten Text für verschiedene Sprachen hinzu.Wählen Sie Übersetzungen neben dem Feld Beschreibung. Fügen Sie übersetzten Text für verschiedene Sprachen hinzu.Wählen Sie Bild hochladen, um ein Bild für die Lokation hinzuzufügen.Sichern Sie Ihre Eingaben. | Die Daten der Lokation werden gesichert. |  |
| 6 | Eine Adresse hinzufügen | Auf dem Bild Lokation: <Lokationsname> auf der Registerkarte Adresse:Geben Sie im Feld Name Zeile 1 <Name Zeile 1> ein.Geben Sie in das Feld Name Zeile 2 <Name Zeile 2> ein.Geben Sie im Feld Straße den <Straßennamen> ein.Geben Sie im Feld Postleitzahl die <Postleitzahl> ein.Geben Sie im Feld Stadt <Name der Stadt> ein.Wählen Sie im Feld Land/Region über die Wertehilfe <das Land bzw. die Region> aus.Geben Sie im Feld Region über die Wertehilfe die <Region> ein.Im Feld Zeitzone behalten Sie den UTC-Standardwert bei.Geben Sie zusätzliche Daten in die Felder Telefonnummer, Faxnummer, Breitengrad, Längengrad und Höhe ein.Sichern Sie Ihre Eingaben. | Die Daten der Lokation werden gesichert. |  |
| 7 | Verantwortlichen hinzufügen | Dieser Schritt ist nur für die folgenden Rollen relevant:SAP_BR_INDUSTRIAL_HYGIENIST (Fachkraft für Arbeitssicherheit)SAP_BR_EHS_ENV_MGMT (Umweltschutzbeauftragter)Auf dem Bild Lokation: <Lokationsname> auf der Registerkarte Verantwortliche Personen:Geben Sie in der Tabelle Verantwortliche nach Rollen in der Spalte Name über die Wertehilfe Ihren <Benutzernamen> ein.Wählen Sie in der Spalte Rolle die Option Unfallmanager oder Umweltschutzbeauftragter aus der Dropdown-Liste aus.Sichern Sie Ihre Eingaben. | Die Daten der Lokation werden gesichert. |  |
| 8 | Dokumente hinzufügen | Auf dem Bild Lokation: <Lokationsname> auf der Registerkarte Dokumente:Wählen Sie in der Tabelle Dokumente und Links die Option Datei hinzufügen, um ein Dokument für den Standort hinzuzufügen.Sichern Sie Ihre Eingaben. | Das ausgewählte Dokument wird der Tabelle hinzugefügt.Die Daten der Lokation werden gesichert. |  |
|  | Lokation aktivieren | Auf dem Bild Lokation: <Lokationsname>:Wählen Sie Status setzen im Seitenkopf.Wählen Sie Aktiv. | Die Lokation wird aktiviert.Das Feld Status im Seitenkopf wird auf Aktiv gesetzt.Die Daten der Lokation werden gesichert. |  |

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
- related-to :: [[13-quality-ehs-and-compliance/create-ehs-location-mds-3sr-359]]
- related-to :: [[13-quality-ehs-and-compliance/ehs-mds-3sr-361]]
- related-to :: [[13-quality-ehs-and-compliance/ehs-mds-3sr-363]]
- related-to :: [[13-quality-ehs-and-compliance/script-de-dados-mestre-criar-local-ehs-mds-3sr-362]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/3SR_S4CLD2608_Master_Data_DE_XX.docx` — full document · extracted with `mammoth` · 10,557 chars in the whole document
