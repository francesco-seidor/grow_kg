---
id: 12-production-and-manufacturing/arbeitsplan-anlegen-sds-bnl-628
title: Arbeitsplan anlegen – SDS (BNL) (BNL_S4CLD2608_Master_Data_DE_XX)
description: "German master data script BNL for SAP S/4HANA Cloud Public Edition 2608: creating a manufacturing routing (Arbeitsplan) with operations and component allocation in app F5425."
cluster: 12-production-and-manufacturing
tags: [kb/production-and-manufacturing, topic/routings-and-reference-operation-sets]
aliases: [BNL_S4CLD2608_Master_Data_DE_XX]
keywords: [Routings and Reference Operation Sets, routings, routing operations, control keys, component allocation, external processing, business roles, master data prerequisites, master data scripts, BNL]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/BNL_S4CLD2608_Master_Data_DE_XX.docx]
confidence: low
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-628
topic: 12-production-and-manufacturing/routings-and-reference-operation-sets
language: DE
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Arbeitsplan anlegen – SDS (BNL) (BNL_S4CLD2608_Master_Data_DE_XX)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/BNL_S4CLD2608_Master_Data_DE_XX.docx`, extracted with `mammoth`. Grouped under **Routings and Reference Operation Sets** in Production and Manufacturing. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

| <!-- image omitted: unnamed --> | StammdatenskriptSAP S/4HANA Cloud Public Edition - 02-07-26 |
| --- | --- |
|  | Arbeitsplan anlegen – SDS (BNL) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Inhaltsverzeichnis

[1 Verwendungszweck 2](#_Toc233889982)

[2 Voraussetzungen 3](#_Toc233889983)

[2.1 Systemzugriff 3](#_Toc233889984)

[2.2 Rollen 3](#_Toc233889985)

[2.3 Erforderliche Organisationseinheiten 3](#_Toc233889986)

[2.4 Obligatorische und optionale Stammdaten 4](#_Toc233889987)

[2.5 Wesentliche Parameter für die Datenerstellung 4](#_Toc233889988)

[2.5.1 Verwendung 4](#_Toc233889989)

[3 Übersichtstabelle 6](#_Toc233889990)

[4 Testverfahren 7](#_Toc233889991)

[4.1 Arbeitsplan anlegen 7](#_Toc233889992)

## Verwendungszweck

Ein Arbeitsplan für die Fertigung definiert den Fertigungsprozess für ein Material. Er enthält die Vorgänge oder Arbeitsschritte, die während der Produktion auszuführen sind. Er definiert die Verwendung von Materialien und Arbeitsplätzen. Er bildet eine Vorlage für einen Fertigungsauftrag und ist die Basis für die Erzeugniskalkulation.

Ein Arbeitsplan wird für ein Fertigerzeugnis oder Halbfabrikat definiert und ist spezifisch für eine Produktionsstätte (Werk). Er gilt für eine bestimmte Losgröße und besteht aus einer Anzahl von Vorgängen, die jeweils einem Arbeitsplatz zugeordnet sind.

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
| Produktionsingenieur – diskrete Fertigung | SAP_BR_PRODN_ENG_DISC | Fertigungstechnik - diskrete Fertigung | SAP_BR_PRODN_ENG_DISC |  |

### Erforderliche Organisationseinheiten

| Datensegment | Hängt ab von | Feldbeispiele | Kommentare | Zu verwendende Organisationseinheit |
| --- | --- | --- | --- | --- |
| Alle Daten | Werk |  | Alle Daten für den Arbeitsplan hängen vom Werk ab. | Werk:__________ |

### Obligatorische und optionale Stammdaten

Arbeitsplandatensätze können auf andere Stammdaten verweisen. Die folgende Tabelle stellt eine Übersicht optionaler und obligatorischer Stammdatenobjekte für die Verwendung in einem Arbeitsplan bereit.

| Stammdatenobjekt | Verwendet im Datensegment | Obligatorisch / optional | Kommentare |
| --- | --- | --- | --- |
| Material |  | Obligatorisch | Führen Sie das folgende Testskript als eine Voraussetzung vor der Ausführung der Prozessschritte aus:Produktstamm vom Typ „Rohstoff“ anlegen – SDS (BNR)Produktstamm vom Typ „Halbfabrikat“ anlegen – SDS (BNS)Produktstamm vom Typ „Fertigerzeugnis“ anlegen – SDS (BNT) |
| Arbeitsplatz | Wählen Sie auf dem Bild Arbeitsplan anlegen: Vorgangsübersicht einen Arbeitsplatz für einen internen Vorgang aus. | Obligatorisch, (Optional) | Für einen internen Vorgang ist der Arbeitsplatz kein obligatorisches Eingabefeld.Sofern erforderlich, führen Sie das Testskript Arbeitsplan anlegen – SDS (BNL) aus. |
| Stückliste |  | Optional | Führen Sie das Testskript Materialstückliste für Produktion und Vertrieb anlegen – SDS (BNK) aus. |
| Einkaufsinfosatz |  | (Obligatorisch) | Für einen externen Vorgang können Sie einen Einkaufsinfosatz verwenden, um alle bezugsrelevanten Daten zu erfassen. |
| Materialgruppe |  |  |  |
| Kostenart |  |  |  |

### Wesentliche Parameter für die Datenerstellung

In diesem Abschnitt werden einige Basisparameter erläutert, die das Verhalten eines Stammsatzes beeinflussen und zum Anlegen eines Arbeitsplans immer erforderlich sind:

#### Verwendung

| Arbeitsplatzart | Beschreibung |
| --- | --- |
| 1 | Fertigung |
| 2 | Konstruktion |
| 3 | Universal |

## Übersichtstabelle

Dieser Umfangsbestandteil umfasst den Prozessschritt in der folgenden Tabelle:

|  |
| --- |
| Hinweis Wenn Ihr Systemadministrator Bereiche und Seiten auf dem SAP Fiori Launchpad aktiviert hat, enthält die Startseite nur die wesentlichen Apps, mit denen die typischen Aufgaben einer Benutzerrolle ausgeführt werden können.Alle anderen (suchbaren) Apps, die nicht auf der Startseite enthalten sind, finden Sie über die Suchleiste ([2434549](https://me.sap.com/notes/2434549)).Wenn Sie die Startseite personalisieren und versteckte Apps hinzufügen möchten, wechseln Sie in Ihr Benutzerprofil und wählen Sie App Finder. |

| Prozessschritt | Benutzerrolle | Transaktion | Erwartete Ergebnisse |
| --- | --- | --- | --- |
| [Arbeitsplan anlegen](#unique_10) [Seite ] 7 | Produktionsingenieur – diskrete Fertigung | Arbeitspläne verwalten(F5425) |  |

## Testverfahren

In diesem Abschnitt werden die Testverfahren für den jeweiligen Prozessschritt beschrieben, der zum betreffenden Umfangsbestandteil gehört.

### Arbeitsplan anlegen

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
| 1 | Anmelden | Melden Sie sich am SAP Fiori Launchpad als Produktionsingenieur – diskrete Fertigung an. | Das SAP Fiori Launchpad wird angezeigt. |  |
| 2 | SAP-Fiori-App aufrufen | Öffnen Sie Arbeitspläne verwalten(F5425). | Die App wird geöffnet. |  |
| 3 | "Anlegen" wählen | Wählen Sie Anlegen. | Ein neues Fenster mit dem Bild Arbeitsplan anlegen wird angezeigt. |  |
| 4 | Bild "Arbeitsplan anlegen" einrichten | Geben Sie auf dem Bild Arbeitsplan anlegen die folgenden Daten ein:Material: <Materialnummer des Halbfabrikats/Fertigerzeugnisses>Werk: <Ihre Werksnummer>Wählen Sie Weiter. | Das Bild Arbeitsplan anlegen: Kopfdetail wird angezeigt. |  |
| 5 | Bild "Arbeitsplan anlegen: Kopfdetails" einrichten | Geben Sie die folgenden Daten auf dem Bild Arbeitsplan anlegen: Kopfdetail ein.Verwendung: <1 für Produktion>Status: <4 Freigegeben allgemein>Losgröße von – Losgröße bis: <Geben Sie ein Losgrößenintervall und eine Mengeneinheit ein.> |  |  |
| 6 | Bild "Arbeitsplan anlegen: Vorgangsübersicht" einrichten | Wählen Sie Vorgang, woraufhin Arbeitsplan anlegen: Vorgangsübersicht angezeigt wird.Geben Sie die folgenden Daten auf dem Bild Arbeitsplan anlegen: Vorgangsübersicht:Arbeitspl.: erforderlich für interne Vorgänge, (leer) für externe VorgängeSteuerschlüssel: <YBP1/YBP2/YBP3/YBP5>YBP1 für internen Vorgang ohne automatischen WareneingangYBP2 für externen Vorgang (PP-Lohnbearbeitung)YBP3 für internen Vorgang mit automatischem WareneingangYBP4 für ProzessfertigungsmeilensteinBeschreibung: <Beschreibung für den Vorgang eingeben>Doppelklicken Sie anschließend auf den eingegebenen Vorgang. |  |  |
| 7 | Externen Vorgang für Abschnitt " Externe Verarbeitung" einrichten | Geben Sie die folgenden Daten auf dem Bild Arbeitsplan anlegen: Vorgangsdetails ein.Einkaufsinfosatz: erforderlich für interne Vorgänge, (leer) für externe VorgängeMaterialgruppe: L002/L003Kostenart: <relevante Kostenart für Ihr Land>Einkaufsorganisation: <Einkaufsorganisation>. |  |  |
| 8 | Internen Vorgang für den Vorgabewertabschnitt einrichten | Geben Sie auf dem Bild Arbeitsplan anlegen: Vorgangsdetails die folgenden Daten ein.Einrichtung: <Rüstzeit>Maschine: <Maschinenbedienungszeit>Personal: <Personalzeit> |  |  |
| 9 | Weitere Vorgänge hinzufügen | Wiederholen Sie die vorherigen Schritte für jeden Vorgang. |  |  |
| 10 | Komponente wählen | Wählen Sie oben in der Sicht die Option Komponentenallokation, und wählen Sie dann eine Komponente aus. | Die Materialkomponentenübersicht wird angezeigt. |  |
| 11 | Neue Zuordnung anlegen | Wählen Sie Neue Zuordnung. | Das Dialogfenster Neue Zuordnung wird angezeigt. |  |
| 12 | Zu Vorgang zuordnen Liste | Wählen Sie Vorgangs Liste. |  |  |
| 13 | Vorgang wählen | Wählen Sie einen Vorgang aus, und wählen Sie dann Enter. |  |  |
| 14 | Weitere Komponenten zuordnen | Wiederholen Sie die vorherigen Schritte für weitere Komponenten. |  |  |
| 15 | Daten sichern | Sichern Sie Ihre Eingaben. | Der Arbeitsplan wird angelegt. |  |

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
> Flagged while digesting this document, not verified: Control key list in step 6 names YBP5 in the entry options while describing YBP4; internal inconsistency

## Connections
- part-of :: [[_cluster]]
- related-to :: [[12-production-and-manufacturing/creacion-de-hoja-de-ruta-mds-bnl-630]]
- related-to :: [[12-production-and-manufacturing/criar-roteiro-mds-bnl-632]]
- related-to :: [[12-production-and-manufacturing/master-data-script-create-routing-mds-bnl-629]]
- related-to :: [[12-production-and-manufacturing/mds-bnl-631]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/BNL_S4CLD2608_Master_Data_DE_XX.docx` — full document · extracted with `mammoth` · 11,883 chars in the whole document
