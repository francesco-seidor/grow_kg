---
id: 08-sales-order-management/objekt-und-wertermittlung-anlegen-sds-5nh-478
title: Objekt- und Wertermittlung anlegen – SDS (5NH) (5NH_S4CLD2608_Master_Data_DE_XX)
description: "German master data script 5NH: test steps to create characteristic combinations and access sequences for substitution (product/plant/storage location) in S/4HANA Cloud Public Edition 2608."
cluster: 08-sales-order-management
tags: [kb/sales-order-management, topic/product-and-location-substitution]
aliases: [5NH_S4CLD2608_Master_Data_DE_XX]
keywords: ["Product, Plant and Storage Location Substitution", characteristic combinations, substitution access sequences, substitution controls, plant substitution, storage location substitution, product substitution, advanced atp, business roles, master data scripts]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/5NH_S4CLD2608_Master_Data_DE_XX.docx]
confidence: high
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-478
topic: 08-sales-order-management/product-and-location-substitution
language: DE
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Objekt- und Wertermittlung anlegen – SDS (5NH) (5NH_S4CLD2608_Master_Data_DE_XX)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/5NH_S4CLD2608_Master_Data_DE_XX.docx`, extracted with `mammoth`. Grouped under **Product, Plant and Storage Location Substitution** in Sales Order Management. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

| <!-- image omitted: unnamed --> | StammdatenskriptSAP S/4HANA Cloud Public Edition - 02-07-26 |
| --- | --- |
|  | Objekt- und Wertermittlung anlegen – SDS (5NH) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Inhaltsverzeichnis

[1 Zweck 2](#_Toc233889816)

[2 Voraussetzungen 3](#_Toc233889817)

[2.1 Systemzugriff 3](#_Toc233889818)

[2.2 Rollen 3](#_Toc233889819)

[2.3 Erforderliche Organisationseinheiten 3](#_Toc233889820)

[2.4 Obligatorische Stammdaten 4](#_Toc233889821)

[2.5 Vorbereitende Schritte 4](#_Toc233889822)

[2.5.1 Steuerung für Produktersetzung anlegen (optional) 4](#_Toc233889823)

[2.5.2 Steuerung für Werksersetzung anlegen (optional) 6](#_Toc233889824)

[2.5.3 Steuerung für Lagerortersetzung anlegen (optional) 7](#_Toc233889825)

[3 Übersichtstabelle 10](#_Toc233889826)

[4 Testverfahren 11](#_Toc233889827)

[4.1 Merkmalskombination anlegen 11](#_Toc233889828)

[4.2 Zugriff anlegen 12](#_Toc233889829)

## Zweck

In diesem Dokument erfahren Sie, wie Sie eine Kombination und den Zugriff mit Merkmalswerten für die Kombinationsstammdaten für Ihr SAP S/4HANA Cloud Public Edition-System anlegen.

Die Objekt- und Wertfestlegung ermöglicht es einem Benutzer, die Merkmale zu konfigurieren, um eine Steuerung zu bestimmen, die während der Verfügbarkeitsprüfung zum Ersetzen eines Produkts/Werks/Lagerorts im Kundenauftrag verwendet wird.

Dies ermöglicht die Integration der Stammdatenersetzung mit der alternativen-basierten Bestätigung (ABC) der AATP-Funktion.

## Voraussetzungen

In diesem Abschnitt sind alle Voraussetzungen für den Test hinsichtlich System, Benutzer, Stammdaten, Organisationsdaten, sonstige Testdaten und Voraussetzungen zusammengefasst.

### Systemzugriff

| System | Details |
| --- | --- |
| System | Zugriff möglich über SAP Fiori Launchpad. Ihr Systemadministrator stellt Ihnen die URL für den Zugriff auf die verschiedenen Apps zur Verfügung, die Ihrer Rolle zugeordnet sind. |

### Rollen

| Name (Rollenvorlage) | ID (Rollenvorlage) | Name (Launchpad-Bereich) | ID (Launchpad-Bereich) | Anmelden |
| --- | --- | --- | --- | --- |
| Experte für die Auftragserfüllung | SAP_BR_ORDER_FULFILLMNT_MNGR | Auftragserfüllungsverwaltung | SAP_BR_ORDER_FULFILLMNT_MNGR |  |
| Stammdatenexperte – Produktdaten | SAP_BR_PRODMASTER_SPECIALIST | Stammdaten – Produkte / Produkt-Governance | SAP_BR_PRODMASTER_SPECIALIST / SAP_CMD_SPT_PR_GOV_PC |  |

### Erforderliche Organisationseinheiten

Es sind keine spezifischen Organisationsdaten erforderlich.

| Datensegment | Hängt ab von | Feldbeispiele | Kommentare | Zu verwendende Organisationseinheit |
| --- | --- | --- | --- | --- |
|  |  |  |  |  |

### Obligatorische Stammdaten

Keine spezifischen Stammdaten erforderlich.

| Stammdatenobjekt | Verwendet im Datensegment | Obligatorisch / optional | Kommentare |
| --- | --- | --- | --- |
|  |  |  |  |

Weitere Informationen zum Anlegen dieser Stammdatenobjekte finden Sie in:Tabelle 1: Verweis auf Stammdatenskript:

| SDS | Beschreibung |
| --- | --- |
|  |  |

### Vorbereitende Schritte

#### Steuerung für Produktersetzung anlegen (optional)

Testverwaltung

Kundenprojekt: Füllen Sie die projektbezogenen Teile aus.

|  |  |  |  |
| --- | --- | --- | --- |
| Testfall-ID | <X.XX> | Testdatum: |  |
| Testername: |  | Dauer: |  |
| Benutzerrolle(n): |  | Zuständigkeit: | <Geben Sie den Serviceanbieter, einen Kunden oder einen Serviceanbieter zusammen mit einem Kunden an.> |

Zweck

Die folgende Vorgehensweise stellt Anweisungen zum Anlegen einer Steuerung für die Ersetzung oder den Ausschluss von Produkten bereit. Die zur Verfügung stehenden Apps hängen von der Ihnen zugeordneten Rolle ab.

Vorgehensweise

| Testschrittnummer | Bezeichnung des Testschritts | Anweisung | Erwartetes Ergebnis | Kommentare |
| --- | --- | --- | --- | --- |
| 1 | Anmelden | Melden Sie sich am SAP Fiori Launchpad als Stammdatenexperte – Produktdaten an. | Das SAP Fiori Launchpad wird angezeigt. |  |
| 2 | SAP-Fiori-App aufrufen | Öffnen Sie Ersetzungssteuerungen verwalten - Produkte(F4787). | Die App wird geöffnet. |  |
| 3 | "Anlegen" wählen | Wählen Sie auf dem Bild Ersetzungssteuerungen verwalten - Produkte die Option Anlegen. | Das Bild Ersetzungssteuerung verwalten - Produkte - Anlegen wird angezeigt. |  |
| 4 | Steuerung eingeben | Geben Sie im Bereich Kopf Folgendes ein:Steuerung: <Geben Sie die neue Steuerung für die Ersetzung ein, z.B. "VERKAUF".> |  |  |
| 5 | "Anlegen" wählen | Wählen Sie Anlegen. | Die Systemmeldung Steuerung angelegt wird angezeigt. |  |
| 6 | Beschreibung anlegen | Wählen Sie im Abschnitt Beschreibung die Option Anlegen. | Das Bild Steuerungsbeschreibung anlegen wird angezeigt. |  |
| 7 | Beschreibungsdaten eingeben | Nehmen Sie im Abschnitt Beschreibung die folgenden Einträge vor:Sprachenschlüssel: <Geben Sie die für die Steuerung geltende Sprache ein, z.B. EN für Englisch.>Steuerungsbeschreibung: <Geben Sie einen Text ein, um die Steuerung zu beschreiben, z.B. "für Verkauf"> |  |  |
| 8 | "Anlegen" wählen | Wählen Sie Anlegen. | Die Systemmeldung Steuerungsbeschreibung angelegt wird angezeigt. |  |
| 9 | "Zurück" wählen | Wählen Sie im Abschnitt Titel die Option < (Zurück). | Das Bild Ersetzungssteuerung verwalten - Produkte wird angezeigt. |  |
| 10 | Gruppen zuordnen | Wählen Sie im Abschnitt Gruppen zuordnen die Option Zuordnen. | Das Dialogfenster Gruppen zur Steuerung zuordnen wird angezeigt. |  |
| 11 | "Gruppe" wählen | Suchen und wählen Sie im Dialogfenster Gruppen zur Steuerung zuordnen die Option Gruppe.Wählen Sie beispielsweise die Gruppe STANDARD_DISPLAY.Hinweis Wenn keine vorhandene Gruppe angezeigt wird, können Sie zunächst den Prozessschritt Gruppe für Ersetzung anlegen (optional) im Stammdatenskript Produktsubstitution anlegen – SDS - 4VO ausführen.Wählen Sie Zuordnen. | Die Systemmeldung Das Objekt wurde zugeordnet. wird angezeigt. |  |

#### Steuerung für Werksersetzung anlegen (optional)

Testverwaltung

Kundenprojekt: Füllen Sie die projektbezogenen Teile aus.

|  |  |  |  |
| --- | --- | --- | --- |
| Testfall-ID | <X.XX> | Testdatum: |  |
| Testername: |  | Dauer: |  |
| Benutzerrolle(n): |  | Zuständigkeit: | <Geben Sie den Serviceanbieter, einen Kunden oder einen Serviceanbieter zusammen mit einem Kunden an.> |

Zweck

Die folgende Vorgehensweise stellt Anweisungen zum Anlegen einer Steuerung für die Ersetzung oder den Ausschluss von Produkten bereit. Die zur Verfügung stehenden Apps hängen von der Ihnen zugeordneten Rolle ab.

Vorgehensweise

| Testschrittnummer | Bezeichnung des Testschritts | Anweisung | Erwartetes Ergebnis | Kommentare |
| --- | --- | --- | --- | --- |
| 1 | Anmelden | Melden Sie sich als Experte für die Auftragserfüllung am SAP Fiori Launchpad an. | Das SAP Fiori Launchpad wird angezeigt. |  |
| 2 | SAP-Fiori-App aufrufen | Öffnen Sie Ersetzungssteuerungen verwalten - Lokationen(F5312). | Die App wird geöffnet. |  |
| 3 | "Anlegen" wählen | Wählen Sie auf dem Bild Ersetzungssteuerungen verwalten - Lokationen die Option Anlegen. | Das Bild Ersetzungssteuerungen verwalten - Lokationen anlegen wird angezeigt. |  |
| 4 | Steuerung eingeben | Geben Sie im Bereich Kopf Folgendes ein:Lokationstyp: <Werk>Steuerung: <Geben Sie die neue Steuerung für die Ersetzung ein, z.B. REGION>. |  |  |
| 5 | Daten sichern | Wählen Sie Sichern. | Die Systemmeldung Steuerung angelegt wird angezeigt. |  |
| 6 | "Anlegen" wählen | Wählen Sie im Abschnitt Beschreibung die Option Anlegen. | Das Bild Steuerungsbeschreibung anlegen wird angezeigt. |  |
| 7 | Beschreibungsdaten eingeben | Nehmen Sie im Abschnitt Beschreibung die folgenden Einträge vor:Sprachenschlüssel: <Geben Sie den für die Steuerung geltenden Sprachenschlüssel ein, z.B. EN für Englisch.>Steuerungsbeschreibung: <Geben Sie einen Text ein, um die Steuerung zu beschreiben, z.B. Steuerung für eine Region> |  |  |
| 8 | Daten sichern | Wählen Sie Anlegen. | Die Systemmeldung Steuerungsbeschreibung angelegt wird angezeigt. |  |
| 9 | "Zurück" wählen | Wählen Sie im Abschnitt Titel die Option < (Zurück). | Das Bild Ersetzungssteuerungen verwalten - Lokationen wird angezeigt. |  |
| 10 | Gruppen zuordnen | Wählen Sie im Abschnitt Gruppen zuordnen die Option Zuordnen. | Das Dialogfenster Gruppen zur Steuerung zuordnen wird angezeigt. |  |
| 11 | "Gruppe" wählen | Suchen und wählen Sie im Dialogfenster Gruppen zur Steuerung zuordnen die Option Gruppe.Wählen Sie beispielsweise die Gruppe <SOUTH_REGION>.Hinweis Wenn keine vorhandene Gruppe angezeigt wird, können Sie zunächst den Prozessschritt Gruppe für Werksersetzung anlegen (optional) im Stammdatenskript Lokationsersetzung und -ausschluss anlegen – SDS - 5NG ausführen.Wählen Sie Zuordnen. | Die Systemmeldung Gruppe(n) wurde(n) zugeordnet wird angezeigt. |  |

#### Steuerung für Lagerortersetzung anlegen (optional)

Testverwaltung

Kundenprojekt: Füllen Sie die projektbezogenen Teile aus.

|  |  |  |  |
| --- | --- | --- | --- |
| Testfall-ID | <X.XX> | Testdatum: |  |
| Testername: |  | Dauer: |  |
| Benutzerrolle(n): |  | Zuständigkeit: | <Geben Sie den Serviceanbieter, einen Kunden oder einen Serviceanbieter zusammen mit einem Kunden an.> |

Zweck

Die folgende Vorgehensweise stellt Anweisungen zum Anlegen einer Steuerung für die Ersetzung oder den Ausschluss von Lagerorten bereit. Verfügbare Apps sind von Ihrer Rolle abhängig.

Vorgehensweise

| Testschrittnummer | Bezeichnung des Testschritts | Anweisung | Erwartetes Ergebnis | Kommentare |
| --- | --- | --- | --- | --- |
| 1 | Anmelden | Melden Sie sich am SAP Fiori Launchpad als Experte für die Auftragserfüllung an. | Das SAP Fiori Launchpad wird angezeigt. |  |
| 2 | SAP-Fiori-App aufrufen | Öffnen Sie Ersetzungssteuerungen verwalten - Lokationen(F5312). | Die App wird geöffnet. |  |
| 3 | "Anlegen" wählen | Wählen Sie auf dem Bild Ersetzungssteuerungen verwalten - Lokationen die Option Anlegen. | Das Bild Ersetzungssteuerungen verwalten - Lokationen anlegen wird angezeigt. |  |
| 4 | Steuerung eingeben | Geben Sie im Bereich Kopf Folgendes ein:Lokationstyp: <Lagerort>Steuerung: <Geben Sie die neue Steuerung für die Ersetzung ein, z.B. STORAGE_TYPE>. |  |  |
| 5 | "Anlegen" wählen | Wählen Sie Anlegen. | Die Systemmeldung Steuerung angelegt wird angezeigt. |  |
| 6 | "Anlegen" wählen | Wählen Sie im Abschnitt Beschreibung die Option Anlegen. | Das Bild Steuerungsbeschreibung anlegen wird angezeigt. |  |
| 7 | Beschreibungsdaten eingeben | Nehmen Sie im Abschnitt Beschreibung die folgenden Einträge vor:Sprachenschlüssel: <Geben Sie den für die Steuerung geltenden Sprachenschlüssel ein, z.B. EN für Englisch.>Steuerungsbeschreibung: <Geben Sie einen Text ein, um die Steuerung zu beschreiben, z.B. Steuerung für Lagertyp> |  |  |
| 8 | Daten sichern | Wählen Sie Anlegen. | Die Systemmeldung Steuerungsbeschreibung angelegt wird angezeigt. |  |
| 9 | "Zurück" wählen | Wählen Sie im Abschnitt Titel die Option < (Zurück). | Das Bild Ersetzungssteuerungen verwalten - Lokationen wird angezeigt. |  |
| 10 | Gruppen zuordnen | Wählen Sie im Abschnitt Gruppen zuordnen die Option Zuordnen. | Das Dialogfenster Gruppen zur Steuerung zuordnen wird angezeigt. |  |
| 11 | "Gruppe" wählen | Suchen und wählen Sie im Dialogfenster Gruppen zur Steuerung zuordnen die Option Gruppe.Wählen Sie beispielsweise die Gruppe <COLD_STORAGE>.Hinweis Wenn keine vorhandene Gruppe angezeigt wird, können Sie zunächst den Prozessschritt Gruppe für Lagerortersetzung anlegen (optional) im Stammdatenskript Lokationsersetzung und -ausschluss anlegen – SDS - 5NG ausführen.Wählen Sie Zuordnen. | Die Systemmeldung Gruppe(n) wurde(n) zugeordnet wird angezeigt. |  |

## Übersichtstabelle

Dieser Umfangsbestandteil umfasst die Segmente in der folgenden Tabelle:

|  |
| --- |
| Hinweis Wenn Ihr Systemadministrator Bereiche und Seiten auf dem SAP Fiori Launchpad aktiviert hat, enthält die Startseite nur die wesentlichen Apps, mit denen die typischen Aufgaben einer Benutzerrolle ausgeführt werden können.Alle anderen (suchbaren) Apps, die nicht auf der Startseite enthalten sind, finden Sie über die Suchleiste ([2434549](https://me.sap.com/notes/2434549)).Wenn Sie die Startseite personalisieren und versteckte Apps hinzufügen möchten, wechseln Sie in Ihr Benutzerprofil und wählen Sie App Finder. |

| Segment | Anwendungsrolle | App/Transaktion | Erwartete Ergebnisse |
| --- | --- | --- | --- |
| [Merkmalskombination anlegen](#unique_11) [Seite ] 11 | Experte für die Auftragserfüllung | Merkmalskombinationen verwalten(F5303). | Die Merkmalskombination wird angelegt. |
| [Zugriff anlegen](#unique_12) [Seite ] 12 | Experte für die Auftragserfüllung | Zugriffsfolgen verwalten – Ersetzungen(F5302) | Der Zugriff wird für die Kombination angelegt, die in den oben genannten Segmenten angelegt wurde, und die Merkmalswerte werden für die Zugriffe definiert. |

## Testverfahren

In diesem Abschnitt werden die Testverfahren für den jeweiligen Prozessschritt beschrieben, der zum betreffenden Umfangsbestandteil gehört.

### Merkmalskombination anlegen

Testverwaltung

Kundenprojekt: Füllen Sie die projektbezogenen Teile aus.

|  |  |  |  |
| --- | --- | --- | --- |
| Testfall-ID | <X.XX> | Testdatum: |  |
| Testername: |  | Dauer: |  |
| Benutzerrolle(n): |  | Zuständigkeit: | <Geben Sie den Serviceanbieter, einen Kunden oder einen Serviceanbieter zusammen mit einem Kunden an.> |

Zweck

Die folgende Vorgehensweise enthält eine Anleitung zum Anlegen einer Merkmalskombination. Die zur Verfügung stehenden Apps hängen von der Ihnen zugeordneten Rolle ab.

Vorgehensweise

| Testschrittnummer | Bezeichnung des Testschritts | Anweisung | Erwartetes Ergebnis | Kommentare |
| --- | --- | --- | --- | --- |
| 1 | Anmelden | Melden Sie sich am SAP Fiori Launchpad als Experte für die Auftragserfüllung an. | Das SAP Fiori Launchpad wird angezeigt. |  |
| 2 | SAP-Fiori-App aufrufen | Öffnen Sie Merkmalskombinationen verwalten(F5303). | Die App wird geöffnet. |  |
| 3 | "Anlegen" wählen | Wählen Sie auf dem Bild Merkmalskombinationen verwalten die Option Anlegen. | Das Bild Merkmalskombinationen verwalten - Anlegen wird angezeigt. |  |
| 4 | Kopfdaten eingeben | Geben Sie im Bereich Kopf folgende Daten ein:Kombination: <Kombinationsnamen eingeben>Kombinationsbeschreibung: <Beschreibung der Kombination eingeben>Verwendung: <Ersetzung>Katalogart: <Basis (Verkaufsbeleg) mit Verwendung SUBSTN>Kombination, Verwendung und Katalogart sind obligatorisch, um eine Ersetzung anzulegen. |  |  |
| 5 | Merkmale zuordnen | Geben Sie im Abschnitt Merkmale Folgendes ein, um die Merkmale zuzuordnen:Wählen Sie Zuordnen.Wählen Sie die Merkmale auf dem Bild.Wählen Sie Zuordnen auf dem Bild.Legen Sie die Reihenfolge der Merkmale fest, indem Sie die Pfeiltaste Nach oben oder Nach unten verwenden. |  |  |
| 6 | "Anlegen" wählen | Wählen Sie Anlegen. | Die Systemmeldung Die Kombination wurde angelegt wird angezeigt. |  |

### Zugriff anlegen

Testverwaltung

Kundenprojekt: Füllen Sie die projektbezogenen Teile aus.

|  |  |  |  |
| --- | --- | --- | --- |
| Testfall-ID | <X.XX> | Testdatum: |  |
| Testername: |  | Dauer: |  |
| Benutzerrolle(n): |  | Zuständigkeit: | <Geben Sie den Serviceanbieter, einen Kunden oder einen Serviceanbieter zusammen mit einem Kunden an.> |

Zweck

Die folgende Vorgehensweise enthält Anweisungen zum Anlegen des Zugriffs für die Kombination und zum Definieren der MWK-Werte für den Zugriff. Verfügbare Apps sind von Ihrer Rolle abhängig.

Vorgehensweise

| Testschrittnummer | Bezeichnung des Testschritts | Anweisung | Erwartetes Ergebnis | Kommentare |
| --- | --- | --- | --- | --- |
| 1 | Anmelden | Melden Sie sich als Experte für die Auftragserfüllung am SAP Fiori Launchpad an. | Das SAP Fiori Launchpad wird angezeigt. |  |
| 2 | Die SAP-Fiori-App aufrufen | Öffnen Sie Zugriffsfolgen verwalten – Ersetzungen(F5302). | Das Bild Zugriffsfolgen verwalten - Ersetzungen wird angezeigt. |  |
| 3 | "Anlegen" wählen | Wählen Sie in der Sicht Zugriffsfolgen verwalten - Ersetzungen auf der Registerkarte Produkte die Option Anlegen (drei Registerkarten Produkte, Werk und Lagerort sind verfügbar). | Das Bild Zugriffsfolgen verwalten - Substitution "Anlegen" wird angezeigt. |  |
| 4 | Details eingeben | Nehmen Sie in dem Dialogfenster folgende Einträge vor:Kombination: <Kombination über die Wertehilfe auswählen>Status : <Erforderlichen Status aus der Auswahlliste auswählen> Das Feld "Status" wird mit dem Status Inaktiv vorbelegt.Wählen Sie Anlegen.Zum Anlegen eines Zugriffs ist eine Kombination obligatorisch. | Eine Systemmeldung zeigt an, dass der Zugriff angelegt wurde. |  |
| 5 | Details der zugeordneten Steuerungen eingeben | Fügen Sie im Abschnitt Zugeordnete Steuerungen die Merkmale und die Steuerungsdetails hinzu:Wählen Sie Hinzufügen.Merkmale: <Merkmalswerte eingeben oder aus der Wertehilfe auswählen>Status: <Status ist standardmäßig "Aktiv">Ersetzung ausführen: <Standardmäßig aktiviert>Steuerung: <Optional - Produktersetzungssteuerung eingeben>Fügen Sie nach Bedarf mehrere Werte hinzu. | Die im Abschnitt Zugeordnete Steuerungen angezeigten Merkmalsspalten sind diejenigen, die der beim Anlegen des Zugriffs ausgewählten Kombination zugeordnet sind. |  |
| 6 | Zugriff anlegen | Wählen Sie Anlegen. | Die Systemmeldung Zugriff angelegt wird angezeigt. |  |

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
- related-to :: [[08-sales-order-management/5nh-483]]
- related-to :: [[08-sales-order-management/crear-determinacion-de-objeto-y-valor-mds-5nh-480]]
- related-to :: [[08-sales-order-management/create-object-and-value-determination-mds-5nh-479]]
- related-to :: [[08-sales-order-management/criar-determinacao-de-objeto-e-valor-mds-5nh-482]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/5NH_S4CLD2608_Master_Data_DE_XX.docx` — full document · extracted with `mammoth` · 19,888 chars in the whole document
