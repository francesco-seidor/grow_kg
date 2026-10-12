---
id: 14-maintenance-service-and-projects/stammdatenskript-messpunkt-anlegen-sds-5mi-466
title: Stammdatenskript - Messpunkt anlegen – SDS (5MI) (5MI_S4CLD2608_Master_Data_DE_XX)
description: "SAP S/4HANA Cloud Public Edition 2608 master data script (German) for creating measuring points and counters in asset management, plus measuring point type configuration."
cluster: 14-maintenance-service-and-projects
tags: [kb/maintenance-service-and-projects, topic/measuring-points-and-counters]
aliases: [5MI_S4CLD2608_Master_Data_DE_XX]
keywords: [Measuring Points and Counters, measuring points, measuring counters, measuring point types, condition-based maintenance, technical objects, characteristics, business roles, solution configuration, master data scripts]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/5MI_S4CLD2608_Master_Data_DE_XX.docx]
confidence: high
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-466
topic: 14-maintenance-service-and-projects/measuring-points-and-counters
language: DE
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Stammdatenskript - Messpunkt anlegen – SDS (5MI) (5MI_S4CLD2608_Master_Data_DE_XX)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/5MI_S4CLD2608_Master_Data_DE_XX.docx`, extracted with `mammoth`. Grouped under **Measuring Points and Counters** in Maintenance, Service and Projects. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

| <!-- image omitted: unnamed --> | StammdatenskriptSAP S/4HANA Cloud Public Edition - 02-07-26 |
| --- | --- |
|  | Messpunkt anlegen – SDS (5MI) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Inhaltsverzeichnis

[1 Zweck 2](#_Toc233889795)

[2 Voraussetzungen 3](#_Toc233889796)

[2.1 Systemzugriff 3](#_Toc233889797)

[2.2 Rollen 3](#_Toc233889798)

[2.3 Erforderliche Organisationseinheiten 3](#_Toc233889799)

[2.4 Obligatorische und optionale Stammdaten 4](#_Toc233889800)

[2.5 Wesentliche Parameter für die Datenerstellung 4](#_Toc233889801)

[2.5.1 Messpunkttyp 4](#_Toc233889802)

[3 Übersichtstabelle 7](#_Toc233889803)

[4 Vorgehensweise 8](#_Toc233889804)

[4.1 Messpunkt anlegen 8](#_Toc233889805)

[4.2 Messzähler anlegen 9](#_Toc233889806)

## Zweck

Dieses Dokument beschreibt, wie Sie einen Messpunkt-Stammdatensatz für Ihr S/4HANA-System anlegen. Die Beschreibung umfasst die Datensegmente, die für die Stammdaten zum Arbeiten in einer üblichen Systemumgebung relevant sind. Der Leser lernt hauptsächlich, welche Datensegmente und -felder hauptsächlich mit Eingabewerten gefüllt werden müssen. Felder, die für den durch von SAP Best Practices bereitgestellten Umfang der Kontentauslieferung in S/4HANA nicht relevant sind, werden in diesem Dokument nicht behandelt, obwohl sie möglicherweise in der Benutzeroberfläche (UI) angezeigt werden.

## Voraussetzungen

Dieser Abschnitt fasst alle Voraussetzungen zum Anlegen eines Messpunktes zusammen.

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
| Stammdatenexperte - Instandhaltungsmanagement | SAP_BR_MD_SPECIALIST_EAM | Stammdaten - Instandhaltungsmanagement | SAP_EAM_SPT_MD_SPECIALIST_PC |

### Erforderliche Organisationseinheiten

Einige Segmente der Stammdaten hängen von den Organisationseinheiten des Unternehmens ab. Allgemeine (zentrale) Daten sind nicht von einer Organisationseinheit oder dem Buchungskreis abhängig. Die folgende Tabelle stellt eine Übersicht verschiedener Datensegmente und ihrer relevanten Organisationseinheiten bereit:

| Datensegment | Hängt ab von | Feldbeispiele | Kommentare | Zu verwendende Organisationseinheit |
| --- | --- | --- | --- | --- |
|  |  |  |  |  |

### Obligatorische und optionale Stammdaten

Messpunktdatensätze können auf andere Stammdaten verweisen. Die folgende Tabelle stellt eine Übersicht optionaler und obligatorischer Stammdatenobjekte für die Verwendung an einem Messpunkt bereit.

| Stammdatenobjekt | Verwendet im Datensegment | Obligatorisch / optional | Kommentare |
| --- | --- | --- | --- |
| Technisches Objekt |  | obligatorisch | Equipment oder Technischer Platz. |
| Merkmal |  | obligatorisch | Merkmale beschreiben die Eigenschaften von Objekten. Die Werte eines Merkmals legen die Eigenschaften fest. |

### Wesentliche Parameter für die Datenerstellung

In diesem Abschnitt werden einige Basisparameter erläutert, die das Verhalten eines Stammsatzes beeinflussen und zum Anlegen eines Messpunktes immer erforderlich sind.

#### Messpunkttyp

Der Messpunkttyp bestimmt, welche Daten im Stammsatz für den Messpunkttyp gepflegt werden können. Messpunkte werden im System durch den Messpunkttyp unterschieden. Jeder Messpunkttyp wird durch einen Schlüssel identifiziert, den Sie zuerst beim Anlegen des Messpunkts im System zuordnen.

Tabelle 2:

| Messpunkttyp | Beschreibung |
| --- | --- |
| M | Messpunkt (allgemein) |

Testverwaltung

Kundenprojekt: Füllen Sie die projektbezogenen Teile aus.

|  |  |  |  |
| --- | --- | --- | --- |
| Testfall-ID | <X.XX> | Testdatum: |  |
| Testername: |  | Dauer: |  |
| Benutzerrolle(n): |  | Zuständigkeit: | <Geben Sie den Serviceanbieter, einen Kunden oder einen Serviceanbieter zusammen mit einem Kunden an.> |

Zweck

Mit dieser Aktivität können Sie den Messpunkttyp konfigurieren.

Vorgehensweise

Wählen Sie abhängig von Ihrer Konfigurationsumgebung für SAP S/4HANA Cloud Public Edition eine der folgenden Optionen:

Lösung konfigurieren:

| Testschrittnummer | Bezeichnung des Testschritts | Anweisung | Erwartetes Ergebnis | Bestanden/Nicht bestanden/Anmerkung |
| --- | --- | --- | --- | --- |
| 1. | Anmelden | Melden Sie sich am SAP Fiori Launchpad als Konfigurationsexperte - Geschäftsprozesskonfiguration an. | Das SAP Fiori Launchpad wird angezeigt. |  |
| 2 | App aufrufen | Öffnen Sie Lösung verwalten (F1214). | Das Bild Lösung verwalten wird angezeigt. |  |
| 3 | "Lösung konfigurieren" öffnen | Wählen Sie Lösung konfigurieren.Hinweis Um länder-/regionsabhängige Einstellungen für die gewünschte lokale Version anzulegen, wählen Sie Lokale Version festlegen.Wählen Sie als Anwendungsbereich Asset Management aus.Wählen Sie für den Subanwendungsbereich die Option Instandhaltungstechnik aus.Markieren Sie die Zeile mit dem Positionsnamen: Stammdaten | Das Bild "Lösung konfigurieren" wird angezeigt. |  |
| 4 | "Messpunkttypen anlegen" öffnen | Wählen Sie unter Konfigurationsschritte den Schrittnamen Meßpunkttypen definieren aus, und wählen Sie Konfigurieren. | Das Bild Messpunkttypen wird angezeigt. |  |
| 5 | Bedingungen für CBM aktivieren (optional) | Wählen Sie den Messpunkttyp "M" aus.Geben Sie im Feld Messbereich den Wert "W" ein.Markieren Sie das Ankreuzfeld für Meldungen anlegen.Wählen Sie Sichern. | Bedingungen für CBM wurden festgelegt. |  |

SAP Central Business Configuration

| Testschrittnummer | Bezeichnung des Testschritts | Anweisung | Erwartetes Ergebnis | Bestanden/Nicht bestanden/Anmerkung |
| --- | --- | --- | --- | --- |
| 1. | Anmelden | Melden Sie sich am SAP Fiori Launchpad als Konfigurationsexperte - Geschäftsprozesskonfiguration an. | Das SAP Fiori Launchpad wird angezeigt. |  |
| 2 | App aufrufen | Öffnen Sie die Implementierungsaktivitäten. | Das Bild Lösung verwalten wird angezeigt. |  |
| 3 | Konfiguration aufrufen | Um die Aktivität in der Baumsicht zu finden, klicken Sie auf das Suchsymbol, und wählen Sie die erweiterte Suchoption.Geben Sie den Knotentext/die Aktivitätsbeschreibung Meßpunkttypen definieren ein, und wählen Sie Weiter. | Die Aktivität wird in der Baumsicht angezeigt. |  |
| 4 | "Messpunkttypen anlegen" öffnen | Wählen Sie unter Konfigurationsschritte den Schrittnamen Meßpunkttypen definieren aus, und wählen Sie Konfigurieren. | Das Bild Messpunkttypen wird angezeigt. |  |
| 5 | Bedingungen für CBM aktivieren (optional) | Wählen Sie den Messpunkttyp "M" aus.Geben Sie im Feld Messbereich den Wert "W" ein.Markieren Sie das Ankreuzfeld für Meldungen anlegen.Wählen Sie Sichern. | Bedingungen für CBM wurden festgelegt. |  |

## Übersichtstabelle

Dieser Umfangsbestandteil umfasst die verschiedenen Prozessschritte in der Tabelle.

|  |
| --- |
| Hinweis Wenn Ihr Systemadministrator Bereiche und Seiten auf dem SAP Fiori Launchpad aktiviert hat, enthält die Startseite nur die wesentlichen Apps, mit denen die typischen Aufgaben einer Benutzerrolle ausgeführt werden können.Alle anderen (suchbaren) Apps, die nicht auf der Startseite enthalten sind, finden Sie über die Suchleiste ([2434549](https://me.sap.com/notes/2434549)).Wenn Sie die Startseite personalisieren und versteckte Apps hinzufügen möchten, wechseln Sie in Ihr Benutzerprofil und wählen Sie App Finder. |

| Prozessschritt | Anwendungsrolle | App/Vorgang | Erwartete Ergebnisse |
| --- | --- | --- | --- |
| [Messpunkt anlegen](#unique_10) [Seite ] 8 | SAP_BR_MD_SPECIALIST_EAM | App Messpunkt anlegen(EAMS_WDA_MP_OIF). | Der Messpunkt wird angelegt. |

## Vorgehensweise

In diesem Abschnitt werden die Abläufe für jeden Prozessschritt beschrieben, der zu diesem Umfangsbestandteil gehört. Sie können diese Abläufe auch zum Testen der Stammdatenerzeugung verwenden.

### Messpunkt anlegen

Testverwaltung

Kundenprojekt: Füllen Sie die projektbezogenen Teile aus.

|  |  |  |  |
| --- | --- | --- | --- |
| Testfall-ID | <X.XX> | Testdatum: |  |
| Testername: |  | Dauer: |  |
| Benutzerrolle(n): |  | Zuständigkeit: | <Geben Sie den Serviceanbieter, einen Kunden oder einen Serviceanbieter zusammen mit einem Kunden an.> |

Vorgehensweise

| Testschrittnummer | Bezeichnung des Testschritts | Anweisungen | Erwartetes Ergebnis | Bestanden/Nicht bestanden/Anmerkung |
| --- | --- | --- | --- | --- |
| 1 | Anmelden | Melden Sie sich am SAP Fiori Launchpad als Stammdatenexperte SAP_BR_MD_SPECIALIST_EAM an. | Das SAP Fiori Launchpad wird angezeigt. |  |
| 2 | SAP-Fiori-App aufrufen | Öffnen Sie die App Messpunkt anlegen(EAMS_WDA_MP_OIF). | Ein neues Fenster wird geöffnet, das das Bild Messpunkt anlegen zeigt. |  |
| 3 | Details erfassen | Geben Sie Folgendes ein:Messpunkt/Zähler: <Messpunkt>:Referenzobjekttyp: <Technisches Objekt> | Sie gelangen auf ein neues Bild, auf dem das Referenzobjekt angezeigt wird. |  |
| 4 | Referenzobjektdetails eingeben | Geben Sie Folgendes ein:Technisches Objekt:<Nr. Equipment/Floc>Wählen Sie Enter oder Weiter. | Messpunkt anlegen |  |
| 5 | Allgemeine Daten | Geben Sie im Abschnitt Allgemeine Daten die folgenden Daten ein:Beschreibung: <Beschreibung des Messpunkts>Merkmal: z.B. BETRIEBSSTUNDE/DRUCKMesspunkttyp: M (Messpunkt allgemein) |  |  |
| 6 | Zielgrenzen und Zählerdaten eingeben | Geben Sie im Abschnitt Zielgrenzen und Zählerdaten Folgendes ein:Zielwert: z.B. 10 PAObere Messbereichsgrenze: z.B. 15 PAUntere Messbereichsgrenze: z.B. 5 PA |  |  |
| 7 | Messtoleranz eingeben (optional) | Geben Sie im Abschnitt Messtoleranz Folgendes ein:Obere Messtoleranz: z.B. 12 PAUntere Messtoleranz: z.B. 7 PA |  |  |
| 8 | Bedingung pflegen (nur bei bedingungsbasierter Pflege) | Im Abschnitt "Bedingung pflegen":Klicken Sie auf das Kontrollkästchen für "Bedingung einschalten", wählen Sie eine beliebige Bedingung aus: z.B. Für Bedingung: MESSWERT > OBERGRENZEGeben Sie folgende Daten ein:Objekttyp (Meldungsart): z.B. "Reaktive Arbeit"Priorität: Wählen Sie die Priorität aus, die für die anzulegende Meldung erforderlich ist, z.B. 1 Sehr hoch.Aktiv: Markieren Sie das Ankreuzfeld, um diese Bedingung zu aktivieren.Langtext: Geben Sie den Langtext für die anzulegende Meldung ein.Beschreibung: Geben Sie die Beschreibung für die anzulegende Meldung ein. |  |  |
| 9 | Einträge prüfen | Wählen Sie Einträge prüfen. | Die Einträge werden geprüft. |  |
| 10 | Daten sichern | Sichern Sie Ihre Eingaben. | Der Messpunkt wird angelegt. |  |

### Messzähler anlegen

Testverwaltung

Kundenprojekt: Füllen Sie die projektbezogenen Teile aus.

|  |  |  |  |
| --- | --- | --- | --- |
| Testfall-ID | <X.XX> | Testdatum: |  |
| Testername: |  | Dauer: |  |
| Benutzerrolle(n): |  | Zuständigkeit: | <Geben Sie den Serviceanbieter, einen Kunden oder einen Serviceanbieter zusammen mit einem Kunden an.> |

Vorgehensweise

| Testschrittnummer | Bezeichnung des Testschritts | Anweisung | Erwartetes Ergebnis | Bestanden/Nicht bestanden/Anmerkung |
| --- | --- | --- | --- | --- |
| 1. | Anmelden | Melden Sie sich am SAP Fiori Launchpad als Stammdatenexperte SAP_BR_MD_SPECIALIST_EAM an. | Das SAP Fiori Launchpad wird angezeigt. |  |
| 2 | SAP-Fiori-App aufrufen | Öffnen Sie die App Messpunkt anlegen (EAMS_WDA_MP_OIF). | Ein neues Fenster wird geöffnet, das das Bild Messpunkt anlegen zeigt. |  |
| 3 | Details erfassen | Geben Sie Folgendes ein:Messpunkt/Zähler: <Zähler>Referenzobjekttyp: <Technisches Objekt> | Sie gelangen auf ein neues Bild, auf dem das Referenzobjekt angezeigt wird. |  |
| 4 | Referenzobjekt eingeben | Geben Sie Folgendes ein:Technisches Objekt: <Nr. Equipment/Floc>Wählen Sie Enter oder Weiter. | Das Bild Messpunkt anlegen (Zähler) wird geöffnet. |  |
| 5 | Allgemeine Daten eingeben | Geben Sie im Abschnitt Allgemeine Daten die folgenden Daten ein:Beschreibung: <Beschreibung des Messzählers>Messpunkttyp: M (Messpunkt allgemein)Merkmal: z.B. BETRIEBSSTUNDE/DRUCK | Allgemeine Daten werden gepflegt. |  |
| 6 | Zielgrenzen und Zählerdaten eingeben | Geben Sie im Abschnitt Zielgrenzen und Zählerdaten Folgendes ein:Zählersprungmarke: <Zählersprungmarke>Geschätzte Jahresleistung: <Geschätzte Jahresleistung von technischem Objekt>Messbereichseinheit | Zielgrenzen werden gepflegt. |  |
| 7 | Einträge prüfen | Wählen Sie Einträge prüfen. | Die Einträge werden geprüft. |  |
| 8 | Daten sichern | Sichern Sie Ihre Eingaben. | Der Messpunkt wird angelegt. |  |

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
- related-to :: [[14-maintenance-service-and-projects/5mi-469]]
- related-to :: [[14-maintenance-service-and-projects/crear-punto-de-medicion-mds-5mi-468]]
- related-to :: [[14-maintenance-service-and-projects/create-measuring-point-mds-5mi-467]]
- related-to :: [[14-maintenance-service-and-projects/criar-ponto-de-medicao-mds-5mi-470]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/5MI_S4CLD2608_Master_Data_DE_XX.docx` — full document · extracted with `mammoth` · 15,872 chars in the whole document
