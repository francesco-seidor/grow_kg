---
id: 12-production-and-manufacturing/standardarbeitsplan-anlegen-sds-ble-574
title: Standardarbeitsplan anlegen – SDS (BLE) (BLE_S4CLD2608_Master_Data_DE_XX)
description: "German SAP S/4HANA Cloud master data script (BLE): create a standard routing (reference operation set) with CA11, including prerequisites and test steps."
cluster: 12-production-and-manufacturing
tags: [kb/production-and-manufacturing, topic/routings-and-reference-operation-sets]
aliases: [BLE_S4CLD2608_Master_Data_DE_XX]
keywords: [Routings and Reference Operation Sets, standard routing, routing master data, control keys, work center, plant dependency, bill of materials, business roles, work center usage, BLE]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/BLE_S4CLD2608_Master_Data_DE_XX.docx]
confidence: high
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-574
topic: 12-production-and-manufacturing/routings-and-reference-operation-sets
language: DE
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Standardarbeitsplan anlegen – SDS (BLE) (BLE_S4CLD2608_Master_Data_DE_XX)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/BLE_S4CLD2608_Master_Data_DE_XX.docx`, extracted with `mammoth`. Grouped under **Routings and Reference Operation Sets** in Production and Manufacturing. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

| <!-- image omitted: unnamed --> | StammdatenskriptSAP S/4HANA Cloud Public Edition - 02-07-26 |
| --- | --- |
|  | Standardarbeitsplan anlegen – SDS (BLE) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Inhaltsverzeichnis

[1 Zweck 2](#_Toc233889907)

[2 Voraussetzungen 3](#_Toc233889908)

[2.1 Systemzugriff 3](#_Toc233889909)

[2.2 Rollen 3](#_Toc233889910)

[2.3 Erforderliche Organisationseinheiten 3](#_Toc233889911)

[2.4 Obligatorische und optionale Stammdaten 4](#_Toc233889912)

[2.5 Wesentliche Parameter für die Datenerstellung 4](#_Toc233889913)

[2.5.1 Nutzung 4](#_Toc233889914)

[3 Übersichtstabelle 6](#_Toc233889915)

[4 Testverfahren 7](#_Toc233889916)

[4.1 Standardarbeitsplan anlegen 7](#_Toc233889917)

## Zweck

Dieser Prozess beschreibt, wie Sie einen Standardarbeitsplan anlegen.

Ein Standardarbeitsplan hat die gleiche Struktur wie ein Arbeitsplan. Einem Standardarbeitsplan kann kein zu produzierendes Material zugeordnet werden und es dürfen weder parallele noch alternative Folgen vorhanden sein.

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
| Alle Daten | Werk |  | Alle Daten für einen Standardarbeitsplan sind abhängig vom Werk. | Werk:__________ |

### Obligatorische und optionale Stammdaten

Referenz-Arbeitsplandatensätze können auf andere Stammdaten verweisen. Die folgende Tabelle stellt eine Übersicht optionaler und obligatorischer Stammdatenobjekte für die Verwendung in einem Referenzarbeitsplan bereit.

| Stammdatenobjekt | Verwendet im Datensegment | Obligatorisch / optional | Kommentare |
| --- | --- | --- | --- |
| Material |  | obligatorisch | Führen Sie das folgende Testskript als eine Voraussetzung vor der Ausführung der Prozessschritte aus:Produktstamm vom Typ „Rohstoff“ anlegen – SDS (BNR)Produktstamm vom Typ „Halbfabrikat“ anlegen – SDS (BNS)Produktstamm vom Typ „Fertigerzeugnis“ anlegen – SDS (BNT) |
| Arbeitsplatz | Wählen Sie im Bild Standardarbeitsplan anlegen: Vorgangsübersicht einen Arbeitsplatz für einen internen Vorgang aus. | Obligatorisch, (Optional) | Für einen internen Vorgang ist der Arbeitsplatz kein obligatorisches Eingabefeld.Sofern erforderlich, führen Sie das Testskript Standardarbeitsplan anlegen – SDS (BLE) aus. |
| Stückliste |  | Optional | Führen Sie das Testskript Materialstückliste für Produktion und Vertrieb anlegen – SDS (BNK) aus. |
| Einkaufsinfosatz |  | (Obligatorisch) | Für einen externen Vorgang können Sie einen Einkaufsinfosatz verwenden, um alle bezugsrelevanten Daten zu erfassen. |

### Wesentliche Parameter für die Datenerstellung

In diesem Abschnitt werden einige Basisparameter erläutert, die das Verhalten eines Stammsatzes beeinflussen und zum Anlegen eines Referenzarbeitsplans immer erforderlich sind:

#### Nutzung

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
| [Standardarbeitsplan anlegen](#unique_10) [Seite ] 7 | Produktionsingenieur – diskrete Fertigung | Arbeitsplanreferenz anlegen(CA11) |  |

## Testverfahren

In diesem Abschnitt werden die Testverfahren für den jeweiligen Prozessschritt beschrieben, der zum betreffenden Umfangsbestandteil gehört.

### Standardarbeitsplan anlegen

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
| 1 | Anmelden | Melden Sie sich am SAP Fiori Launchpad als Produktionsingenieur – diskrete Fertigung an. | Das SAP Fiori Launchpad wird angezeigt. |  |
| 2 | SAP-Fiori-App aufrufen | Öffnen Sie Arbeitsplanreferenz anlegen(CA11). | Das Bild Standardarbeitsplan anlegen: Einstieg wird angezeigt. |  |
| 3 | Bild "Standardarbeitsplan anlegen: Einstieg" einrichten | Geben Sie Daten auf dem Standardarbeitsplan anlegen – Einstiegsbild ein.Wählen Sie Enter. | Das Bild Standardarbeitsplan anlegen: Kopfdetails wird angezeigt. |  |
| 4 | Bild "Standardarbeitsplan anlegen: Kopfdetails" einrichten | Geben Sie in der Sicht Standardarbeitsplan anlegen: Kopfdetails folgende Daten ein:Plangruppenzähler: <1>Werk: <Ihr Werk>Verwendung: <1 für Produktion>Status: <4 Freigegeben allgemein>Losgröße von – Losgröße bis: <Geben Sie ein Losgrößenintervall und eine Mengeneinheit ein.> |  |  |
| 5 | "Standardarbeitsplan anlegen: Vorgangsübersicht" einrichten | Wählen Sie Vorgang, woraufhin das Bild Standardarbeitsplan anlegen: Vorgangsübersicht angezeigt wird.Geben Sie im Bild Standardarbeitsplan anlegen: Vorgangsübersicht die folgenden Daten ein.Arbeitsplatz: erforderlich für interne Vorgänge, (leer) für externe VorgängeSteuerschlüssel: <YBP1/YBP2/YBP3/YBP5/YBRW>YBP1 für internen Vorgang ohne automatischen WareneingangYBP2 für externen Vorgang (PP-Lohnbearbeitung)YBP3 für internen Vorgang mit automatischem WareneingangYBP5 für ProzessfertigungsmeilensteinBeschreibung: <Beschreibung für den Vorgang eingeben>Doppelklicken Sie anschließend auf den eingegebenen Vorgang. |  |  |
| 6 | Vorgang für den Vorgabewertabschnitt einrichten | Geben Sie im Bild Standardarbeitsplan anlegen: Vorgangsdetails die folgenden Daten ein.Rüsten: <Rüstzeit>Maschine: <Maschinenbedienungszeit>Personal: <Personalzeit> |  |  |
| 7 | Weitere Vorgänge hinzufügen | Wiederholen Sie die vorherigen Schritte für jeden Vorgang. |  |  |
| 8 | Daten speichern | Sichern Sie Ihre Eingaben. | Ein Standardarbeitsplan wird angelegt. |  |

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
- related-to :: [[12-production-and-manufacturing/master-data-script-create-reference-operation-set-mds-ble-575]]
- related-to :: [[12-production-and-manufacturing/mds-ble-577]]
- related-to :: [[12-production-and-manufacturing/mds-ble-579]]
- related-to :: [[12-production-and-manufacturing/script-de-dados-mestre-criar-conjunto-de-operacoes-de-referencia-mds-b]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/BLE_S4CLD2608_Master_Data_DE_XX.docx` — full document · extracted with `mammoth` · 10,603 chars in the whole document
