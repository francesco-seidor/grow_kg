---
id: 08-sales-order-management/stammdatenskript-produktsubstitution-anlegen-sds-4vo-418
title: "Stammdatenskript: Produktsubstitution anlegen – SDS (4VO) (4VO_S4CLD2608_Master_Data_DE_XX)"
description: "German SAP S/4HANA Cloud Public Edition master data script (4VO) for creating product substitutions and exclusions via Fiori apps, with optional reason/group/control setup."
cluster: 08-sales-order-management
tags: [kb/sales-order-management, topic/product-and-location-substitution]
aliases: [4VO_S4CLD2608_Master_Data_DE_XX]
keywords: ["Product, Plant and Storage Location Substitution", product substitution, product exclusion, substitution reasons, substitution groups, substitution controls, product master data, business roles, master data scripts, plant]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/4VO_S4CLD2608_Master_Data_DE_XX.docx]
confidence: high
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-418
topic: 08-sales-order-management/product-and-location-substitution
language: DE
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Stammdatenskript: Produktsubstitution anlegen – SDS (4VO) (4VO_S4CLD2608_Master_Data_DE_XX)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/4VO_S4CLD2608_Master_Data_DE_XX.docx`, extracted with `mammoth`. Grouped under **Product, Plant and Storage Location Substitution** in Sales Order Management. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

| <!-- image omitted: unnamed --> | StammdatenskriptSAP S/4HANA Cloud Public Edition - 02-07-26 |
| --- | --- |
|  | Produktsubstitution anlegen – SDS (4VO) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Inhaltsverzeichnis

[1 Zweck 2](#_Toc233889763)

[2 Voraussetzungen 3](#_Toc233889764)

[2.1 Systemzugriff 3](#_Toc233889765)

[2.2 Rollen 3](#_Toc233889766)

[2.3 Erforderliche Organisationseinheiten 3](#_Toc233889767)

[2.4 Obligatorische Stammdaten 4](#_Toc233889768)

[2.5 Vorbereitende Schritte 4](#_Toc233889769)

[2.5.1 Grund für Produktersetzung anlegen (optional) 4](#_Toc233889770)

[2.5.2 Gruppe für Ersetzung anlegen (optional) 5](#_Toc233889771)

[2.5.3 Ersetzungssteuerungen anlegen (optional) 7](#_Toc233889772)

[3 Übersichtstabelle 9](#_Toc233889773)

[4 Testverfahren 10](#_Toc233889774)

[4.1 Produktersetzung anlegen 10](#_Toc233889775)

[4.2 Produktausschluss anlegen 11](#_Toc233889776)

## Zweck

In diesem Dokument erfahren Sie, wie Sie Stammdaten für Produktersetzungen und -ausschlüsse für Ihr SAP S/4HANA Cloud Public Edition-System anlegen.

Die Produktersetzung ist eine Technik, bei der ein Produkt durch ein anderes Produkt ersetzt wird. Eine Produktersetzung kann aus verschiedenen Gründen angelegt werden. Beispiel:

- Das Produkt ist nicht mehr vorrätig
- Das Produkt hat keine Garantie mehr
- Das Ersatzprodukt ist übermäßig vorrätig

Ein Produktausschluss ermöglicht es Kunden ein Produkt von der Ersetzung ausschließen. Beispielsweise kann ein Ausschluss für ein ausgelaufenes Produkt angelegt werden.

## Voraussetzungen

In diesem Abschnitt sind alle Voraussetzungen für den Test hinsichtlich System, Benutzer, Stammdaten, Organisationsdaten, sonstige Testdaten und Voraussetzungen zusammengefasst.

### Systemzugriff

| System | Details |
| --- | --- |
| System | Zugriff möglich über SAP Fiori Launchpad. Ihr Systemadministrator stellt Ihnen die URL für den Zugriff auf die verschiedenen Apps zur Verfügung, die Ihrer Rolle zugeordnet sind. |

### Rollen

| Name (Rollenvorlage) | ID (Rollenvorlage) | Name (Launchpad-Bereich) | ID (Launchpad-Bereich) | Anmeldung |
| --- | --- | --- | --- | --- |
| Stammdatenexperte – Produktdaten | SAP_BR_PRODMASTER_SPECIALIST | Stammdaten – Produkte / Produkt-Governance | SAP_BR_PRODMASTER_SPECIALIST / SAP_CMD_SPT_PR_GOV_PC |  |

### Erforderliche Organisationseinheiten

Die Organisationsstruktur gibt den Aufbau Ihres Unternehmens wieder. Produktersetzungen können von den Organisationseinheiten (Werk) des Unternehmens abhängig sein. Eine Produktersetzung kann auch unabhängig von der Organisationseinheit sein. Die folgende Tabelle bietet eine Übersicht über die relevanten Organisationseinheiten.

| Datensegment | Hängt ab von | Feldbeispiele | Kommentare | Zu verwendende Organisationseinheit |
| --- | --- | --- | --- | --- |
| Produktersetzung und Produktausschluss | Werk |  | Werk ist für die Produktersetzung bzw. den -ausschluss nicht obligatorisch. Produktersetzung/-ausschluss kann ohne Werkseinschränkung erfolgen. | Werk:____________ |

### Obligatorische Stammdaten

Produktersetzungsdaten beziehen sich auf Produktstammdaten. Die obligatorischen Stammdaten für das Testskript stellen Materialien/Produkte dar. Legen Sie Ihre eigenen Stammdaten an, indem Sie den unten angegebenen Beispielstammdaten folgen.

| Stammdatenobjekt | Verwendet im Datensegment | Obligatorisch / optional | Kommentare |
| --- | --- | --- | --- |
| Material | Produktersetzung anlegenProduktausschluss anlegen | obligatorisch | Um eine Produktersetzung oder einen Produktausschluss anzulegen, müssen mindestens zwei Material-/Produktstammdaten in Ihrem System vorhanden sein. |

Weitere Informationen zum Anlegen dieser Stammdatenobjekte finden Sie unter [Stammdatenskripten](https://help.sap.com/docs/s4hana-best-practices/s4cld2608-master-data):

Tabelle 1: Verweis auf Stammdatenskripte

| MDS | Beschreibung |
| --- | --- |
| BNF | Produktstamm vom Typ „Handelsware“ anlegen – SDS |

### Vorbereitende Schritte

#### Grund für Produktersetzung anlegen (optional)

Testverwaltung

Kundenprojekt: Füllen Sie die projektbezogenen Teile aus.

|  |  |  |  |
| --- | --- | --- | --- |
| Testfall-ID | <X.XX> | Testdatum: |  |
| Testername: |  | Dauer: |  |
| Benutzerrolle(n): |  | Zuständigkeit: | <Geben Sie den Serviceanbieter, einen Kunden oder einen Serviceanbieter zusammen mit einem Kunden an.> |

Zweck

Die folgende Vorgehensweise stellt Anweisungen zum Anlegen von Gründen für die Ersetzung oder den Ausschluss von Produkten bereit. Verfügbare Apps sind von Ihrer Rolle abhängig.

Vorgehensweise

| Testschrittnummer | Bezeichnung des Testschritts | Anweisung | Erwartetes Ergebnis | Kommentare |
| --- | --- | --- | --- | --- |
| 1 | Anmelden | Melden Sie sich am SAP Fiori Launchpad als Stammdatenexperte – Produktdaten an. | Das SAP Fiori Launchpad wird angezeigt. |  |
| 2 | SAP-Fiori-App aufrufen | Öffnen Sie Ersetzungsgründe verwalten - Produkte(F4789). | Das Bild Ersetzungsgründe verwalten - Produkte wird angezeigt. |  |
| 3 | "Anlegen" wählen | Wählen Sie auf dem Bild Ersetzungsgründe verwalten - Produkte die Option Anlegen. | Das Bild Grund wird angezeigt. |  |
| 4 | Grund eingeben | Geben Sie im Bereich Kopf Folgendes ein:Grund: <Geben Sie den neuen Ursachencode für die Ersetzung ein, z.B. Upgrade.> |  |  |
| 5 | Daten sichern | Wählen Sie Anlegen. | Die Systemmeldung Objekt ist gesichert wird angezeigt. |  |
| 6 | "Anlegen" wählen | Wählen Sie im Abschnitt Beschreibung die Option Anlegen. | Das Bild Beschreibung des Grunds wird angezeigt. |  |
| 7 | Beschreibungsdaten eingeben | Nehmen Sie im Abschnitt Beschreibung die folgenden Einträge vor:Sprachenschlüssel: <Geben Sie den für den Grund geltenden Sprachenschlüssel ein, z.B. EN für Englisch.>Beschreibung Grund: <Geben Sie einen Text ein, um den Grund zu beschreiben, z.B. Anwendbar für Produkte, die ein Upgrade durchlaufen.> |  |  |
| 8 | Daten sichern | Wählen Sie Anlegen. | Die Systemmeldung Beschreibung angelegt wird angezeigt. |  |

#### Gruppe für Ersetzung anlegen (optional)

Testverwaltung

Kundenprojekt: Füllen Sie die projektbezogenen Teile aus.

|  |  |  |  |
| --- | --- | --- | --- |
| Testfall-ID | <X.XX> | Testdatum: |  |
| Testername: |  | Dauer: |  |
| Benutzerrolle(n): |  | Zuständigkeit: | <Geben Sie den Serviceanbieter, einen Kunden oder einen Serviceanbieter zusammen mit einem Kunden an.> |

Zweck

In der folgenden Vorgehensweise finden Sie Anweisungen zum Anlegen von Gruppen für die Produktersetzung bzw. -ausschluss. Verfügbare Apps sind von Ihrer Rolle abhängig.

Vorgehensweise

| Testschrittnummer | Bezeichnung des Testschritts | Anweisungen | Erwartetes Ergebnis | Kommentare |
| --- | --- | --- | --- | --- |
| 1 | Anmelden | Melden Sie sich am SAP Fiori Launchpad als Stammdatenexperte – Produktdaten an. | Das SAP Fiori Launchpad wird angezeigt. |  |
| 2 | SAP-Fiori-App aufrufen | Öffnen Sie Ersetzungsgruppen verwalten - Produkte(F4788). | Das Bild Ersetzungsgruppen verwalten - Produkte wird angezeigt. |  |
| 3 | "Anlegen" wählen | Wählen Sie auf dem Bild Ersetzungsgruppen verwalten - Produkte die Option Anlegen. | Das Bild Ersetzungsgruppen verwalten - Produkte -Anlegen wird angezeigt. |  |
| 4 | Gruppe eingeben | Geben Sie im Bereich Kopf folgende Daten ein:Gruppe: <Geben Sie die neue Gruppe für die Ersetzung ein, z.B. "STANDARD_DISPLAY"> |  |  |
| 5 | Daten speichern | Wählen Sie Anlegen. | Eine Systemmeldung bestätigt Das Objekt wurde gesichert. |  |
| 6 | "Anlegen" wählen | Wählen Sie im Abschnitt Beschreibung die Option Anlegen. | Das Bild Beschreibung Gruppe - Anlegen wird angezeigt. |  |
| 7 | Beschreibungsdaten eingeben | Nehmen Sie im Abschnitt Beschreibung die folgenden Einträge vor:Sprachenschlüssel: <Geben Sie die für die Gruppe geltende Sprache ein, z.B. DE Deutsch.>Beschreibung Gruppe: <Geben Sie einen Text ein, um die Gruppe zu beschreiben, z.B. "Alle Standardrechner anzeigen".> |  |  |
| 8 | Daten speichern | Wählen Sie Anlegen. | Eine Systemmeldung bestätigt Das Objekt wurde gesichert. |  |
| 9 | "Zurück" wählen | Wählen Sie im Abschnitt Titel die Option < (Zurück). | Das Bild Ersetzungsgruppen verwalten - Produkte wird angezeigt. |  |
| 10 | Gruppendaten aktivieren | Wählen Sie Aktiv setzen. | Eine Systemmeldung bestätigt Das Objekt ist aktiv. |  |

#### Ersetzungssteuerungen anlegen (optional)

Testverwaltung

Kundenprojekt: Füllen Sie die projektbezogenen Teile aus.

|  |  |  |  |
| --- | --- | --- | --- |
| Testfall-ID | <X.XX> | Testdatum: |  |
| Testername: |  | Dauer: |  |
| Benutzerrolle(n): |  | Zuständigkeit: | <Geben Sie den Serviceanbieter, einen Kunden oder einen Serviceanbieter zusammen mit einem Kunden an.> |

Zweck

Die folgende Vorgehensweise stellt Anweisungen zum Anlegen einer Steuerung für die Ersetzung oder den Ausschluss von Produkten bereit. Verfügbare Apps sind von Ihrer Rolle abhängig.

Vorgehensweise

| Testschrittnummer | Bezeichnung des Testschritts | Anweisungen | Erwartetes Ergebnis | Kommentare |
| --- | --- | --- | --- | --- |
| 1 | Anmelden | Melden Sie sich am SAP Fiori Launchpad als Stammdatenexperte – Produktdaten an. | Das SAP Fiori Launchpad wird angezeigt. |  |
| 2 | SAP-Fiori-App aufrufen | Öffnen Sie Ersetzungssteuerungen verwalten - Produkte(F4787). | Sie gelangen auf das Bild Ersetzungssteuerungen verwalten - Produkte. |  |
| 3 | "Anlegen" wählen | Wählen Sie auf dem Bild Ersetzungssteuerungen - Produkte die Drucktaste Anlegen. | Das Bild Ersetzungssteuerung - Produkte - Anlegen wird angezeigt. |  |
| 4 | Steuerung eingeben | Geben Sie im Bereich Kopf folgende Daten ein:Steuerung: <Geben Sie die neue Steuerung für die Ersetzung ein, z.B. "VERKAUF">. |  |  |
| 5 | Daten speichern | Wählen Sie Anlegen. | Eine Systemmeldung bestätigt Das Objekt wurde gesichert. |  |
| 6 | "Anlegen" wählen | Wählen Sie im Abschnitt Beschreibung die Option Anlegen. | Das Bild wird angezeigt. |  |
| 7 | Beschreibungsdaten eingeben | Nehmen Sie im Abschnitt Beschreibung die folgenden Einträge vor:Sprachenschlüssel: <Geben Sie die für die Steuerung geltende Sprache ein, z.B. DE Deutsch>.Steuerungsbeschreibung: <Geben Sie einen Text ein, um die Steuerung zu beschreiben, z.B. "für Verkauf"> |  |  |
| 8 | Daten speichern | Wählen Sie Anlegen. | Eine Systemmeldung bestätigt Das Objekt wurde gesichert. |  |
| 9 | "Zurück" wählen | Wählen Sie im Abschnitt Titel die Option < (Zurück). | Sie gelangen auf das Bild Ersetzungssteuerung verwalten - Produkte. |  |
| 10 | Gruppen zuordnen | Wählen Sie im Abschnitt Gruppen zuordnen die Option Zuordnen. | Das Dialogfenster Gruppen zur Steuerung zuordnen wird angezeigt. |  |
| 11 | "Gruppe" wählen | Suchen und wählen Sie im Dialogfenster die Option Gruppe.Wählen Sie z.B. Gruppe<STANDARD_DISPLAY>.Wählen Sie Zuordnen. | Eine Systemmeldung bestätigt Das Objekt wurde zugeordnet. |  |

## Übersichtstabelle

Dieser Umfangsbestandteil umfasst die Segmente in der folgenden Tabelle:

|  |
| --- |
| Hinweis Wenn Ihr Systemadministrator Bereiche und Seiten auf dem SAP Fiori Launchpad aktiviert hat, enthält die Startseite nur die wesentlichen Apps, mit denen die typischen Aufgaben einer Benutzerrolle ausgeführt werden können.Alle anderen (suchbaren) Apps, die nicht auf der Startseite enthalten sind, finden Sie über die Suchleiste ([2434549](https://me.sap.com/notes/2434549)).Wenn Sie die Startseite personalisieren und versteckte Apps hinzufügen möchten, wechseln Sie in Ihr Benutzerprofil und wählen Sie App Finder. |

| Segment | Anwendungsrolle | App/Transaktion | Erwartete Ergebnisse |
| --- | --- | --- | --- |
| [Produktersetzung anlegen](#unique_11) [Seite ] 10 | Stammdatenexperte – Produktdaten | Ersetzungen verwalten - Produkte(F4785) | Der Datensatz für die Produktersetzung wird angelegt. |
| [Produktausschluss anlegen](#unique_12) [Seite ] 11 | Stammdatenexperte – Produktdaten | Ausschlüsse verwalten - Produkte(F4786) | Der Datensatz für den Produktausschluss wird angelegt. |

## Testverfahren

In diesem Abschnitt werden die Testverfahren für den jeweiligen Prozessschritt beschrieben, der zum betreffenden Umfangsbestandteil gehört.

### Produktersetzung anlegen

Testverwaltung

Kundenprojekt: Füllen Sie die projektbezogenen Teile aus.

|  |  |  |  |
| --- | --- | --- | --- |
| Testfall-ID | <X.XX> | Testdatum: |  |
| Testername: |  | Dauer: |  |
| Benutzerrolle(n): |  | Zuständigkeit: | <Geben Sie den Serviceanbieter, einen Kunden oder einen Serviceanbieter zusammen mit einem Kunden an.> |

Zweck

Dieses Verfahren enthält eine Anleitung zum Anlegen einer Produktersetzung. Verfügbare Apps sind von Ihrer Rolle abhängig.

Vorgehensweise

| Testschrittnummer | Bezeichnung des Testschritts | Anweisungen | Erwartetes Ergebnis | Kommentare |
| --- | --- | --- | --- | --- |
| 1 | Anmelden | Melden Sie sich am SAP Fiori Launchpad als Stammdatenexperte – Produktdaten an. | Das SAP Fiori Launchpad wird angezeigt. |  |
| 2 | SAP-Fiori-App aufrufen | Öffnen Sie Ersetzungen verwalten - Produkte(F4785). | Das Bild Ersetzungen verwalten - Produkte wird angezeigt. |  |
| 3 | "Anlegen" wählen | Wählen Sie in der Sicht Ersetzungen verwalten - Produkte die Option Anlegen. | Das flexible Spaltenlayout Ersetzungen verwalten - Produkte mit dem Bild "Anlegen" wird angezeigt. |  |
| 4 | Kopfdaten eingeben | Geben Sie im Bereich Kopf folgende Daten ein:Produkt: <Geben Sie das Produkt ein, das ersetzt werden soll.>Ersatzprodukt: <Geben Sie das Ersatzprodukt ein.>Werk: <Werksnummer>Produkt- und Ersatzproduktdaten sind obligatorisch, um eine Ersetzung anzulegen. |  |  |
| 5 | Allgemeine Daten eingeben | Geben Sie im Bereich Allgemeine Informationen folgende Daten ein:Grund: <Geben Sie den Grund für das Anlegen eines Ersatzprodukts ein, z.B. Upgrade>Gültig ab: <<Geben Sie den Starttermin für die Gültigkeit ein.>Gültig bis: <Geben Sie den Endtermin für die Gültigkeit ein.>Zeitzone: <Geben Sie die für die Gültigkeit geltende Zeitzone ein.>Die vorstehenden Einträge sind optional. |  |  |
| 6 | Daten speichern | Wählen Sie Anlegen. | Die Systemmeldung Objekt ist gesichert wird angezeigt. |  |
| 7 | Produktersetzungsdaten aktivieren | Wählen Sie Aktiv setzen. | Die Systemmeldung Objekt ist aktiv wird angezeigt. |  |

### Produktausschluss anlegen

Testverwaltung

Kundenprojekt: Füllen Sie die projektbezogenen Teile aus.

|  |  |  |  |
| --- | --- | --- | --- |
| Testfall-ID | <X.XX> | Testdatum: |  |
| Testername: |  | Dauer: |  |
| Benutzerrolle(n): |  | Zuständigkeit: | <Geben Sie den Serviceanbieter, einen Kunden oder einen Serviceanbieter zusammen mit einem Kunden an.> |

Zweck

Dieses Verfahren enthält eine Anleitung zum Anlegen eines Produktausschlusses. Verfügbare Apps sind von Ihrer Rolle abhängig.

Vorgehensweise

| Testschrittnummer | Bezeichnung des Testschritts | Anweisungen | Erwartetes Ergebnis | Kommentare |
| --- | --- | --- | --- | --- |
| 1 | Anmelden | Melden Sie sich am SAP Fiori Launchpad als Stammdatenexperte – Produktdaten an. | Das SAP Fiori Launchpad wird angezeigt. |  |
| 2 | SAP-Fiori-App aufrufen | Öffnen Sie Ausschlüsse verwalten - Produkte(F4786). | Das Bild Ausschlüsse verwalten - Produkte wird angezeigt. |  |
| 3 | "Anlegen" wählen | Wählen Sie in der Sicht Ausschlüsse verwalten - Produkte die Option Anlegen. | Das Bild Ausschlüsse verwalten - Produkte - Anlegen wird angezeigt. |  |
| 4 | Kopfdaten eingeben | Geben Sie im Bereich Kopf folgende Daten ein:Produkt: <Geben Sie das Produkt ein, das von der Ersetzung ausgeschlossen werden soll.>Werk: <Werksnummer>Die Produkteingabe ist obligatorisch, um einen Ausschluss anzulegen. |  |  |
| 5 | Daten in "Allgemeine Informationen" eingeben | Geben Sie im Bereich Allgemeine Informationen folgende Daten ein:Grund: <Geben Sie den Grund für den Ausschluss des Produkts ein.>Gültig ab: <<Geben Sie den Starttermin für die Gültigkeit ein.>Gültig bis: <Geben Sie den Endtermin für die Gültigkeit ein.>Zeitzone: <Geben Sie die für die Gültigkeit geltende Zeitzone ein.>Die vorstehenden Einträge sind optional. |  |  |
| 6 | Daten speichern | Wählen Sie Anlegen. | Die Systemmeldung Objekt ist gesichert wird angezeigt. |  |
| 7 | Produktausschlussdaten aktivieren | Wählen Sie Aktiv setzen. | Die Systemmeldung Objekt ist aktiv wird angezeigt. |  |

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
- related-to :: [[08-sales-order-management/creacion-de-sustitucion-de-producto-mds-4vo-420]]
- related-to :: [[08-sales-order-management/create-product-substitution-mds-4vo-419]]
- related-to :: [[08-sales-order-management/mds-4vo-421]]
- related-to :: [[08-sales-order-management/mds-4vo-423]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/4VO_S4CLD2608_Master_Data_DE_XX.docx` — full document · extracted with `mammoth` · 18,825 chars in the whole document
