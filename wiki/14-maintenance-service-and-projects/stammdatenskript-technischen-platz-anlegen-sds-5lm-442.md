---
id: 14-maintenance-service-and-projects/stammdatenskript-technischen-platz-anlegen-sds-5lm-442
title: Stammdatenskript - Technischen Platz anlegen - SDS (5LM) (5LM_S4CLD2608_Master_Data_DE_XX)
description: "German SAP S/4HANA Cloud Public Edition 2608 master data script (5LM): creating a functional location structure (one parent, two children) for maintenance."
cluster: 14-maintenance-service-and-projects
tags: [kb/maintenance-service-and-projects, topic/functional-locations]
aliases: [5LM_S4CLD2608_Master_Data_DE_XX]
keywords: [Functional Locations, functional location, technical objects, structure indicator, master data scripts, maintenance planning, work center, cost center, business roles, 5LM]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/5LM_S4CLD2608_Master_Data_DE_XX.docx]
confidence: high
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-442
topic: 14-maintenance-service-and-projects/functional-locations
language: DE
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Stammdatenskript - Technischen Platz anlegen - SDS (5LM) (5LM_S4CLD2608_Master_Data_DE_XX)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/5LM_S4CLD2608_Master_Data_DE_XX.docx`, extracted with `mammoth`. Grouped under **Functional Locations** in Maintenance, Service and Projects. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

| <!-- image omitted: unnamed --> | StammdatenskriptSAP S/4HANA Cloud Public Edition - 02-07-26 |
| --- | --- |
|  | Technischen Platz anlegen – SDS (5LM) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Inhaltsverzeichnis

[1 Zweck 2](#_Toc233889777)

[2 Voraussetzungen 3](#_Toc233889778)

[2.1 Systemzugriff 3](#_Toc233889779)

[2.2 Rollen 3](#_Toc233889780)

[2.3 Erforderliche Organisationseinheiten 3](#_Toc233889781)

[2.4 Obligatorische und optionale Stammdaten 4](#_Toc233889782)

[2.5 Wesentliche Parameter für die Datenerstellung 4](#_Toc233889783)

[2.5.1 Strukturkennzeichen 4](#_Toc233889784)

[2.5.2 Typ des technischen Objekts 5](#_Toc233889785)

[3 Übersichtstabelle 6](#_Toc233889786)

[4 Vorgehensweise 7](#_Toc233889787)

[4.1 Technischen Platz anlegen 7](#_Toc233889788)

## Zweck

Dieses Dokument enthält eine detaillierte Vorgehensweise zum Anlegen von Stammdatensätzen zu einem technischen Platz für Ihr S/4HANA-System. Es umfasst Datensegmente, die für die Stammdaten für die Arbeit in einer normalen Systemumgebung relevant sind. Dieses Dokument gibt auch Auskunft darüber, für welche Datensegmente und Felder Eingabewerte erforderlich sind.

Die Felder, die für den von SAP Best Practices bereitgestellten Umfang der Inhaltsauslieferung in S/4HANA nicht relevant sind, werden in diesem Dokument nicht behandelt, obwohl sie möglicherweise in der Benutzeroberfläche (UI) angezeigt werden. Ein gemäß dieser Beschreibung angelegter technischer Platz kann für Instandhaltungsprozesse verwendet werden.

## Voraussetzungen

Dieser Abschnitt fasst alle Voraussetzungen zusammen, die zum Anlegen eines technischen Platzes erforderlich sind.

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
| Alle Daten | Werk |  | Alle Daten für den technischen Platz hängen vom Werk ab. | Werk:__________ |

### Obligatorische und optionale Stammdaten

Datensätze des technischen Platzes können auf andere Stammdaten verweisen. Die folgende Tabelle stellt eine Übersicht optionaler und obligatorischer Stammdatenobjekte für die Verwendung an einem technischen Platz bereit.

| Stammdatenobjekt | Verwendet im Datensegment | Obligatorisch / optional | Kommentare |
| --- | --- | --- | --- |
| Instandhaltungsarbeitsplatz | Auf der Benutzungsoberfläche (UI) des technischen Platzes finden Sie auf der Registerkarte Organisationsdaten im Abschnitt der Zuständigkeiten den Eintrag für den Instandhaltungsarbeitsplatz. | Optional | Das System verwendet den Instandhaltungsarbeitsplatz als Parameter, um einige Werte zu ermitteln, z.B. Rüsten, Maschine oder Arbeit. |
| Kostenstelle | Auf der Benutzungsoberfläche (UI) des technischen Platzes finden Sie auf der Registerkarte Organisationsdaten im Abschnitt der Zuständigkeiten den Eintrag für die Kostenstelle. | Optional | Das System verwendet die Kostenstelle als Parameter für die Kalkulation. |

### Wesentliche Parameter für die Datenerstellung

In diesem Abschnitt werden einige Basisparameter erläutert, die das Verhalten eines Stammsatzes beeinflussen und zum Anlegen eines technischen Platzes immer erforderlich sind:

#### Strukturkennzeichen

Das Strukturkennzeichen eines technischen Platzes bestimmt die Struktur des Bezeichners des technischen Platzes. Es legt den folgenden Faktor fest:

- Anzahl der Hierarchieebenen eines technischen Systems
- Schlüssellänge der Ebenen
- Trennzeichen (Bindestriche)

Tabelle 2:

| Strukturkennzeichen | Beschreibung |
| --- | --- |
| YBPM | Strukturkennzeichen für Best Practice |

#### Typ des technischen Objekts

Schlüssel, der den Typ des technischen Objekts anzeigt.

Tabelle 3:

| Typ des technischen Objekts | Beschreibung |
| --- | --- |
| M | Technisches System – Standard |

## Übersichtstabelle

|  |
| --- |
| Hinweis Wenn Ihr Systemadministrator Bereiche und Seiten auf dem SAP Fiori Launchpad aktiviert hat, enthält die Startseite nur die wesentlichen Apps, mit denen die typischen Aufgaben einer Benutzerrolle ausgeführt werden können.Alle anderen (suchbaren) Apps, die nicht auf der Startseite enthalten sind, finden Sie über die Suchleiste ([2434549](https://me.sap.com/notes/2434549)).Wenn Sie die Startseite personalisieren und versteckte Apps hinzufügen möchten, wechseln Sie in Ihr Benutzerprofil und wählen Sie App Finder. |

| Prozessschritt | Anwendungsrolle | App/Transaktion | Erwartete Ergebnisse |
| --- | --- | --- | --- |
| [Technischen Platz anlegen](#unique_11) [Seite ] 7 | SAP_BR_MD_SPECIALIST_EAM | Technisches Objekt anlegen(EAMS_WDA_TECHOBJ_OIF (EAMS_WDA_TECHOBJ_OIF_CFG_V2)) | Der Technische Platz wird angelegt. |

## Vorgehensweise

### Technischen Platz anlegen

Testverwaltung

Kundenprojekt: Füllen Sie die projektbezogenen Teile aus.

|  |  |  |  |
| --- | --- | --- | --- |
| Testfall-ID | <X.XX> | Testdatum: |  |
| Testername: |  | Dauer: |  |
| Benutzerrolle(n): |  | Zuständigkeit: | <Geben Sie den Serviceanbieter, einen Kunden oder einen Serviceanbieter zusammen mit einem Kunden an.> |

Zweck

In diesem Testschritt pflegen Sie die Struktur eines Technischen Platzes mit einem Technischen Platz der obersten Ebene und zwei untergeordneten Technischen Plätzen.

Vorgehensweise

| Testschrittnummer | Bezeichnung des Testschritts | Anweisung | Erwartetes Ergebnis | Bestanden/Nicht bestanden/Anmerkung |
| --- | --- | --- | --- | --- |
| 1. | Anmelden | Melden Sie sich am SAP Fiori Launchpad als Stammdatenexperte SAP_BR_MD_SPECIALIST_EAM an. | Das SAP Fiori Launchpad wird angezeigt. |  |
| 2 | SAP-Fiori-App aufrufen | Öffnen Sie Technisches Objekt anlegen(EAMS_WDA_TECHOBJ_OIF (EAMS_WDA_TECHOBJ_OIF_CFG_V2)). | In einem neuen Fenster wird das Bild "Technisches Objekt anlegen (Einstieg)" angezeigt. |  |
| 3 | Technischen Platz anlegen | Wählen Sie auf dem Bild Technisches Objekt anlegen die Option "Art des technischen Objekts: Technischer Platz".Geben Sie im nächsten Bild folgende Daten ein:Art des technischen Objekts: Technischer PlatzStrukturkennzeichen: YBPM (Strukturkennzeichen für Best Practice)Technisches Objekt: <Z.B. 1711 >Typ des technischen Objekts: M (Technisches System - Standard)Wählen Sie Weiter. |  |  |
| 4 | Allgemeine Daten bearbeiten | Geben Sie auf dem Bild Technisches Objekt anlegen: 1711 im Abschnitt Allgemeine Daten folgende Daten ein:Beschreibung: <z.B. Luftdruckkompressoranlage 1 >Optional können Sie weitere allgemeine Daten pflegen. Navigieren Sie dann zum Abschnitt Standortdaten. | Das Bild "Technisches Objekt anlegen: allgemeine Daten" wird angezeigt. |  |
| 5 | Standortdaten pflegen | Nehmen Sie im Abschnitt Standortdaten die folgenden Einträge vor:Standortwerk: <z.B. 1710 für US>Hinweis Allen technischen Objekten, die zu einer Struktur gehören, muss dasselbe Werk zugeordnet sein. Alternativ können Sie die Felder für Angaben zum Werk für alle technischen Objekte leer lassen.Optional können Sie weitere Details wie die Adresse pflegen. | Das Bild "Technisches Objekt anlegen: Standortdaten" wird angezeigt. |  |
| 6 | Organisationsdaten bearbeiten | Nehmen Sie im Abschnitt Organisationsdaten die folgenden Einträge vor:Planungswerk: <z.B. 1710 für US>Instandhaltungsarbeitsplatz: <z.B. RES-0100 für US>Kostenstelle: <z.B. 17101701 für US>Optional können Sie im Abschnitt Organisationsdaten zusätzliche Informationen wie Partnerinformationen pflegen. | Das Bild "Technisches Objekt anlegen: Organisationsdaten" wird angezeigt. |  |
| 7 | Technischen Platz sichern | Optional können Sie zusätzliche Informationen für andere Abschnitte pflegen.Wählen Sie Einträge prüfen.Wählen Sie Sichern.Kehren Sie dann auf die Startseite zurück. | Der Technische Platz wird angelegt. |  |
| 8 | Untergeordneten Technischen Platz anlegen | Um die Struktur eines Technischen Platzes zu pflegen, führen Sie die oben genannten Schritte aus und pflegen die folgenden Technischen Plätze:Technisches Objekt: 1711-001Beschreibung: <Zum Beispiel Kompressor = 1 >Nehmen Sie im Abschnitt Standortdaten die folgenden Einträge vor:Lokation: <z.B. YB_1701>Betriebsbereich: YOHGeben Sie im Abschnitt Organisationsdaten folgende Daten ein:Planergruppe: <z.B. 920 für US>Planungswerk: <z.B. 1710 für US>Instandhaltungsarbeitsplatz: <z.B. RES-0100 für US>Werk zum Arbeitsplatz: <z.B. 1710 für US>Berichtsschema: <For example, YB-PM0003 für US>Optional können Sie zusätzliche Informationen in anderen Abschnitten pflegen.Wählen Sie Einträge prüfen.Wählen Sie Sichern.Geben Sie Folgendes ein:Technisches Objekt: 1711-002Beschreibung: <Zum Beispiel Kompressor = 2 >Nehmen Sie im Abschnitt Standortdaten die folgenden Einträge vor:Lokation: <z.B. YB_1702>Betriebsbereich: <YOH>Geben Sie im Abschnitt Organisationsdaten folgende Daten ein:Planergruppe: <z.B. 920 für US>Planungswerk: <z.B. 1710 für US>Instandhaltungsarbeitsplatz:<z.B. RES-0100 für US>Werk zum Arbeitsplatz: <z.B. 1710 für US>Berichtsschema: <z.B. YB-PM0003 für US>Optional können Sie zusätzliche Informationen für andere Abschnitte pflegen.Wählen Sie Einträge prüfen.Wählen Sie Sichern. | Untergeordnete Technische Plätze werden angelegt. |  |
| 9 | Technisches Objekt im Asset Viewer prüfen | Wählen Sie auf der Startseite die Kachel Technisches Objekt anzeigen.Geben Sie auf dem Bild Technisches Objekt anzeigen das relevante Technische Objekt, z.B. 1711, ein, und wählen Sie Weiter.Um die Struktur des Technischen Platzes und die Details für jedes technische Objekt zu prüfen, können Sie auch Technisches Objekt im Asset Viewer anzeigen wählen. |  |  |

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
- related-to :: [[14-maintenance-service-and-projects/creacion-de-ubicacion-tecnica-mds-5lm-es-444]]
- related-to :: [[14-maintenance-service-and-projects/create-functional-location-mds-5lm-443]]
- related-to :: [[14-maintenance-service-and-projects/mds-5lm-445]]
- related-to :: [[14-maintenance-service-and-projects/mds-5lm-447]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/5LM_S4CLD2608_Master_Data_DE_XX.docx` — full document · extracted with `mammoth` · 13,687 chars in the whole document
