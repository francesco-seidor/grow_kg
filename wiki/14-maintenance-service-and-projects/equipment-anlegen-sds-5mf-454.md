---
id: 14-maintenance-service-and-projects/equipment-anlegen-sds-5mf-454
title: Equipment anlegen - SDS (5MF) (5MF_S4CLD2608_Master_Data_DE_XX)
description: "German SAP S/4HANA Cloud master data script (5MF): creating equipment master data with Technisches Objekt anlegen and installing it at a functional location."
cluster: 14-maintenance-service-and-projects
tags: [kb/maintenance-service-and-projects, topic/equipment]
aliases: [5MF_S4CLD2608_Master_Data_DE_XX]
keywords: [Equipment Master Records, equipment master, technical objects, master data scripts, test procedures, plant maintenance, business roles, organizational units, mandatory master data, functional location]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/5MF_S4CLD2608_Master_Data_DE_XX.docx]
confidence: high
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-454
topic: 14-maintenance-service-and-projects/equipment
language: DE
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Equipment anlegen - SDS (5MF) (5MF_S4CLD2608_Master_Data_DE_XX)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/5MF_S4CLD2608_Master_Data_DE_XX.docx`, extracted with `mammoth`. Grouped under **Equipment Master Records** in Maintenance, Service and Projects. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

| <!-- image omitted: unnamed --> | StammdatenskriptSAP S/4HANA Cloud Public Edition - 02-07-26 |
| --- | --- |
|  | Equipment anlegen – SDS (5MF) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Inhaltsverzeichnis

[1 Zweck 2](#_Toc233889802)

[2 Voraussetzungen 3](#_Toc233889803)

[2.1 Systemzugriff 3](#_Toc233889804)

[2.2 Rollen 3](#_Toc233889805)

[2.3 Erforderliche Organisationseinheiten 3](#_Toc233889806)

[2.4 Obligatorische und optionale Stammdaten 4](#_Toc233889807)

[3 Übersichtstabelle 5](#_Toc233889808)

[4 Wesentliche Parameter für die Datenerstellung 6](#_Toc233889809)

[4.1 Typ des technischen Objekts 6](#_Toc233889810)

[5 Vorgehensweise 7](#_Toc233889811)

[5.1 Equipment anlegen 7](#_Toc233889812)

## Zweck

Dieses Dokument enthält eine detaillierte Vorgehensweise zum Anlegen von Equipmentstammdatensätzen für Ihr S/4HANA-System. Es umfasst Datensegmente, die für die Stammdaten für die Arbeit in einer normalen Systemumgebung relevant sind. Dieses Dokument gibt auch Auskunft darüber, für welche Datensegmente und Felder Eingabewerte erforderlich sind.

Die Felder, die für den durch von SAP Best Practices bereitgestellten Umfang der Kontentauslieferung in S/4HANA nicht relevant sind, werden in diesem Dokument nicht behandelt, obwohl sie möglicherweise in der Benutzeroberfläche (UI) angezeigt werden.

## Voraussetzungen

Dieser Abschnitt fasst alle Voraussetzungen zum Anlegen eines Equipments zusammen.

### Systemzugriff

Der Test sollte mit dem folgenden System durchgeführt werden:

Tabelle 1:

| System | Details |
| --- | --- |
| System | Zugriff über das SAP Fiori Launchpad möglich. Ihr Systemadministrator stellt Ihnen die URL für den Zugriff auf die verschiedenen Apps zur Verfügung, die Ihrer Rolle zugeordnet sind. |

### Rollen

Legen Sie Benutzerrollen mit den folgenden von SAP ausgelieferten Benutzerrollenvorlagen an, und ordnen Sie sie Ihren einzelnen Testbenutzern zu.

Alternativ können Sie, falls verfügbar, die folgenden von SAP ausgelieferten Bereiche verwenden. Legen Sie einen Bereich mit Seiten an, die vordefinierte grundlegende Apps enthalten, und ordnen Sie sie der Benutzerrolle zu. Anschließend ordnen Sie diese Benutzerrolle Ihren einzelnen Benutzern zu.

Weitere Informationen finden Sie unter Anwendungsrolle aus einer Vorlage anlegen in der [Product Assistance](https://help.sap.com/docs/SAP_S4HANA_CLOUD/53e36b5493804bcdb3f6f14de8b487dd/ec310a8b669a45ca898dc4dd91d97de2.html) für SAP S/4HANA Cloud Public Edition.

| Name (Rollenvorlage) | ID (Rollenvorlage) | Name (Bereich) | ID (Bereich) |
| --- | --- | --- | --- |
| Instandhaltungsplaner | SAP_BR_MD_SPECIALIST_EAM | Instandhaltungsplaner | SAP_EAM_SPT_MD_SPECIALIST_PC |

### Erforderliche Organisationseinheiten

Einige Segmente der Stammdaten hängen von den Organisationseinheiten des Unternehmens ab. Allgemeine (zentrale) Daten sind nicht von einer Organisationseinheit oder dem Buchungskreis abhängig. Die folgende Tabelle stellt eine Übersicht verschiedener Datensegmente und ihrer relevanten Organisationseinheiten bereit:

| Datensegment | Hängt ab von | Feldbeispiele | Kommentare | Zu verwendende Organisationseinheit |
| --- | --- | --- | --- | --- |
| Alle Daten | Werk |  | Alle Daten für das Equipment hängen vom Werk ab. | Werk:__________ |

### Obligatorische und optionale Stammdaten

Equipmentdatensätze können auf andere Stammdaten verweisen. Die folgende Tabelle stellt eine Übersicht optionaler und obligatorischer Stammdatenobjekte für die Verwendung in einem Equipment bereit.

| Stammdatenobjekt | Verwendet im Datensegment | Obligatorisch / optional | Kommentare |
| --- | --- | --- | --- |
| Instandhaltungsarbeitsplatz | Auf der Benutzungsoberfläche (UI) des Equipmentstamms finden Sie auf der Registerkarte "Organisationsdaten" im Abschnitt der Zuständigkeiten den Eintrag für den Instandhaltungsarbeitsplatz. | optional | Das System verwendet den Instandhaltungsarbeitsplatz als Parameter, um einige Werte zu ermitteln, z.B. Rüsten, Maschine oder Arbeit. |
| Kostenstelle | Auf der Benutzungsoberfläche (UI) des Equipmentstamms finden Sie auf der Registerkarte "Organisationsdaten" im Abschnitt der Zuständigkeiten den Eintrag für die Kostenstelle. | optional | Das System verwendet die Kostenstelle als Parameter für die Kalkulation. |

## Übersichtstabelle

|  |
| --- |
| Hinweis Wenn Ihr Systemadministrator Bereiche und Seiten auf dem SAP Fiori Launchpad aktiviert hat, enthält die Startseite nur die wesentlichen Apps, mit denen die typischen Aufgaben einer Benutzerrolle ausgeführt werden können.Alle anderen (suchbaren) Apps, die nicht auf der Startseite enthalten sind, finden Sie über die Suchleiste ([2434549](https://me.sap.com/notes/2434549)).Wenn Sie die Startseite personalisieren und versteckte Apps hinzufügen möchten, wechseln Sie in Ihr Benutzerprofil und wählen Sie App Finder. |

| Prozessschritt | Anwendungsrolle | App/Transaktion | Erwartete Ergebnisse |
| --- | --- | --- | --- |
| [Equipment anlegen](#unique_8) [Seite ] 7 | SAP_BR_MD_SPECIALIST_EAM | Technisches Objekt anlegen(EAMS_WDA_TECHOBJ_OIF (EAMS_WDA_TECHOBJ_OIF_CFG_V2)) | Das Equipment wird angelegt. |

## Wesentliche Parameter für die Datenerstellung

In diesem Abschnitt werden einige Basisparameter erläutert, die das Verhalten eines Stammsatzes beeinflussen und zum Anlegen eines Equipments immer erforderlich sind.

### Typ des technischen Objekts

Mögliche Verwendungen sind:

- technische Anlagen und Maschinen
- Gerät
- Fertigungshilfmittel
- Kundenequipment

Tabelle 2:

| Typ des technischen Objekts | Beschreibung |
| --- | --- |
| M | Maschinen |

## Vorgehensweise

### Equipment anlegen

Testverwaltung

Kundenprojekt: Füllen Sie die projektbezogenen Teile aus.

|  |  |  |  |
| --- | --- | --- | --- |
| Testfall-ID | <X.XX> | Testdatum: |  |
| Testername: |  | Dauer: |  |
| Benutzerrolle(n): |  | Zuständigkeit: | <Geben Sie den Serviceanbieter, einen Kunden oder einen Serviceanbieter zusammen mit einem Kunden an.> |

Zweck

In diesem Testschritt pflegen Sie einen Datensatz für ein Equipment, das auf einem Technischen Platz eingebaut ist.

Vorgehensweise

| Testschrittnummer | Bezeichnung des Testschritts | Anweisung | Erwartetes Ergebnis | Bestanden/Nicht bestanden/Anmerkung |
| --- | --- | --- | --- | --- |
| 1. | Anmelden | Melden Sie sich am SAP Fiori Launchpad als SAP_BR_MD_SPECIALIST_EAM an. | Das SAP Fiori Launchpad wird angezeigt. |  |
| 2 | SAP-Fiori-App aufrufen | Öffnen Sie Technisches Objekt anlegen(EAMS_WDA_TECHOBJ_OIF (EAMS_WDA_TECHOBJ_OIF_CFG_V2)). | In einem neuen Fenster wird das Bild Technisches Objekt anlegen: Einstieg geöffnet. |  |
| 3 | Equipment anlegen | Wählen Sie auf dem Bild Technisches Objekt anlegen die Option "Art des technischen Objekts: Equipment".Geben Sie im nächsten Bild folgende Daten ein:Art des technischen Objekts: EquipmentTechnisches Objekt: leer lassenGültig ab: aktuelles DatumTyp des technischen Objekts: M (Technisches System - Standard)Wählen Sie Weiter. |  |  |
| 4 | Allgemeine Daten bearbeiten | Geben Sie auf dem Bild Technisches Objekt anlegen: <Equipment-ID> im Abschnitt Allgemeine Daten folgende Daten ein:Beschreibung: z.B. manuelles Absperrventil>Objektart: z.B. 9400Inbetriebnahmedatum: z.B. das aktuelle Datum>Herstellungsland/-region: z.B. US>Baumonat/-jahr: z.B. 04/2011>Herstellerteilenummer: z.B. HZZ-TD B4>Herstellerserialnummer: z.B. HZZ-TD B4/66>Anschaffungswert/-währung: z.B. 10.000,00/ USD >Anschaffungsdatum: z.B. 10.04.2011 >Optional können Sie weitere allgemeine Daten pflegen. Navigieren Sie dann zum Abschnitt Standortdaten. | Das Bild "Technisches Objekt anlegen: allgemeine Daten" wird angezeigt. |  |
| 5 | Standortdaten pflegen | Nehmen Sie im Abschnitt Standortdaten die folgenden Einträge vor:Standortwerk: z.B. 1710 für US>Standort: z.B. YB_1701 für US>Betriebsbereich: z.B. YOH für US>Hinweis Allen technischen Objekten, die zu einer Struktur gehören, muss dasselbe Werk zugeordnet sein. Alternativ können Sie die Felder für Angaben zum Werk für alle technischen Objekte leer lassen.Optional können Sie weitere Details wie die Adresse pflegen. | Das Bild "Technisches Objekt anlegen: Standortdaten" wird angezeigt. |  |
| 6 | Organisationsdaten bearbeiten | Nehmen Sie im Abschnitt Organisationsdaten die folgenden Einträge vor:Planergruppe: z.B. 920 für US>Planungswerk: z.B. 1710 für US>Instandhaltungsarbeitsplatz: z.B. RES-0100 für US>Werk zum Arbeitsplatz: z.B. 1710 für US>Kostenstelle: z.B. 17101701 für US>Optional können Sie im Abschnitt "Organisationsdaten" zusätzliche Informationen wie Partnerinformationen pflegen. | Das Bild "Technisches Objekt anlegen: Organisationsdaten" wird angezeigt. |  |
| 7 | Equipment sichern | Optional können Sie zusätzliche Informationen für andere Abschnitte pflegen.Wählen Sie Einträge prüfen.Wählen Sie Sichern. | Ein Equipment wird angelegt. |  |
| 8 | Equipment auf Technischem Platz einbauen | Navigieren Sie auf dem Bild "Technisches Objekt ändern": <Equipment-ID> zum Abschnitt Struktur.Wählen Sie Struktur ändern: Einbauen.Geben Sie auf dem Bild Einbauort ändern folgende Daten ein:Übergeordnetes technisches Objekt: z.B. <1710>Position: <leer lassen>Einbaudatum/-zeit: <Systemvorschlag beibehalten>Wählen Sie OK.Wählen Sie Sichern. |  |  |

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
- related-to :: [[14-maintenance-service-and-projects/crear-equipo-mds-5mf-456]]
- related-to :: [[14-maintenance-service-and-projects/create-equipment-mds-5mf-455]]
- related-to :: [[14-maintenance-service-and-projects/criar-equipamento-mds-5mf-458]]
- related-to :: [[14-maintenance-service-and-projects/mds-5mf-457]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/5MF_S4CLD2608_Master_Data_DE_XX.docx` — full document · extracted with `mammoth` · 11,850 chars in the whole document
