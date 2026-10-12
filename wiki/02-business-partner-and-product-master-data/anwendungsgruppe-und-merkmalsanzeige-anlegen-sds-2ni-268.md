---
id: 02-business-partner-and-product-master-data/anwendungsgruppe-und-merkmalsanzeige-anlegen-sds-2ni-268
title: Anwendungsgruppe und Merkmalsanzeige anlegen – SDS (2NI) (2NI_S4CLD2608_Master_Data_DE_XX)
description: "German master data script (2NI) for SAP S/4HANA Cloud Public Edition: creating an application group and a characteristic display with characteristic assignment (CU_CHAR_DISPLAY)."
cluster: 02-business-partner-and-product-master-data
tags: [kb/business-partner-and-product-master-data, topic/variant-configuration-master-data]
aliases: [2NI_S4CLD2608_Master_Data_DE_XX]
keywords: [Configurable Materials and Characteristic Display, characteristic display, application group, characteristic assignment, variant configuration, business roles, transaction types, master data scripts, test procedures, 2NI]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/2NI_S4CLD2608_Master_Data_DE_XX.docx]
confidence: low
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-268
topic: 02-business-partner-and-product-master-data/variant-configuration-master-data
language: DE
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Anwendungsgruppe und Merkmalsanzeige anlegen – SDS (2NI) (2NI_S4CLD2608_Master_Data_DE_XX)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/2NI_S4CLD2608_Master_Data_DE_XX.docx`, extracted with `mammoth`. Grouped under **Configurable Materials and Characteristic Display** in Business Partner and Product Master Data. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

| <!-- image omitted: unnamed --> | StammdatenskriptSAP S/4HANA Cloud Public Edition - 02-07-26 |
| --- | --- |
|  | Anwendungsgruppe und Merkmalsanzeige anlegen – SDS (2NI) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Inhaltsverzeichnis

[1 Zweck 2](#_Toc233889552)

[2 Voraussetzungen 3](#_Toc233889553)

[2.1 Systemzugriff 3](#_Toc233889554)

[2.2 Rollen 3](#_Toc233889555)

[2.3 Obligatorische und operative Stammdaten 3](#_Toc233889556)

[2.4 Wesentliche Parameter für die Datenerstellung 4](#_Toc233889557)

[2.4.1 Transaktion 4](#_Toc233889558)

[3 Übersichtstabelle 5](#_Toc233889559)

[4 Testverfahren 6](#_Toc233889560)

[4.1 Anwendungsgruppe anlegen 6](#_Toc233889561)

[4.2 Merkmalsanzeige erstellen 7](#_Toc233889562)

## Zweck

Dieses Dokument beschreibt, wie Sie eine Merkmalsanzeige für Ihr SAP S/4HANA Cloud Public Edition-System anlegen. Die Beschreibung enthält Daten, die für die SAP S/4HANA Cloud Public Edition-Appliance relevant sind, z.B. Anwendungsgruppe, Merkmalsanzeige und Merkmalszuordnung. Felder, die für den Umfang der SAP S/4HANA Cloud Public Edition-Inhalte nicht relevant sind, werden in diesem Dokument nicht behandelt.

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
| Produktkonfigurationsmodellierer | SAP_BR_PRODUCT_CONFIG_MODELER | Variantenkonfiguration | SAP_BR_PRODUCT_CONFIG_MODELER |  |

### Obligatorische und operative Stammdaten

Merkmalsanzeige-Datensätze können auf andere Stammdaten verweisen. Die folgende Tabelle bietet eine Übersicht über die optionalen und obligatorischen Stammdatenobjekte, die in einem Materialstammdatensatz verwendet werden müssen.

| Stammdatenobjekt | Verwendet im Datensegment | Obligatorisch / optional | Kommentare |
| --- | --- | --- | --- |
| Merkmale |  | obligatorisch | Eigenschaften sind einem Merkmalsanzeige-Datensatz zuzuordnen. |

### Wesentliche Parameter für die Datenerstellung

In diesem Abschnitt werden einige Basisparameter erläutert, die das Verhalten eines Stammsatzes beeinflussen und zum Anlegen einer Merkmalsanzeige immer erforderlich sind:

#### Transaktion

Mithilfe der Transaktion bestimmt das System, in welcher Transaktion die Merkmalsanzeige verfügbar sein soll.

In der Edition 1711 wird nur der Vertriebsbeleg unterstützt.

| Transaktion | Anmerkung |
| --- | --- |
| Vertriebsbeleg | In der Edition 1711 wird nur der Vertriebsbeleg für die Merkmalsanzeige unterstützt. |
| Fertigungsauftrag |  |
| Trading-Kontrakt |  |
| Bestellung |  |
| Wareneingang |  |
| Auftragsrückmeldung |  |

## Übersichtstabelle

In diesem Abschnitt wird eine Liste mit Schritten angegeben, die ein Benutzer beim Anlegen eines Datensatzes durchführt. Jedes logische, aussagekräftige Segment eines Stammdatenobjekts sollte zu einem separaten Schritt führen (z.B. organisationseinheitsabhängige Datensegmente usw.).

Der Umfangsbestandteil Anwendungsgruppe und Merkmalsanzeige anlegen – SDS umfasst die verschiedenen Schritte in den folgenden Tabellen:

|  |
| --- |
| Hinweis Wenn Ihr Systemadministrator Bereiche und Seiten auf dem SAP Fiori Launchpad aktiviert hat, enthält die Startseite nur die wesentlichen Apps, mit denen die typischen Aufgaben einer Benutzerrolle ausgeführt werden können.Alle anderen (suchbaren) Apps, die nicht auf der Startseite enthalten sind, finden Sie über die Suchleiste ([2434549](https://me.sap.com/notes/2434549)).Wenn Sie die Startseite personalisieren und versteckte Apps hinzufügen möchten, wechseln Sie in Ihr Benutzerprofil und wählen Sie App Finder. |

| Prozessschritt, Report oder Bestandteil | Benutzerrolle | Vorgang/App | Erwartete Ergebnisse |
| --- | --- | --- | --- |
| [Anwendungsgruppe anlegen](#unique_9) [Seite ] 6 | Produktkonfigurationsmodellierer | Merkmal pflegen Zur Konfiguration anzeigen(CU_CHAR_DISPLAY) | Die Anwendungsgruppe wird angelegt. |
| [Merkmalsanzeige erstellen](#unique_10) [Seite ] 7 | Produktkonfigurationsmodellierer | Merkmal pflegen Zur Konfiguration anzeigen(CU_CHAR_DISPLAY) | Die Anwendungsgruppe wird angelegt. |

## Testverfahren

In diesem Abschnitt werden die Abläufe für jeden Prozessschritt beschrieben, der zu diesem Umfangsbestandteil gehört. Sie können diese Abläufe auch zum Testen der Stammdatenerzeugung verwenden.

### Anwendungsgruppe anlegen

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
| 1 | Anmelden | Melden Sie sich am SAP Fiori Launchpad als Produktkonfigurationsmodellierer an. | Das SAP Fiori Launchpad wird angezeigt. |  |
| 2 | SAP-Fiori-App aufrufen | Öffnen Sie Merkmal pflegen Zur Konfiguration anzeigen(CU_CHAR_DISPLAY). | Im Bild Sicht "Anwendungsgruppe" ändern: Übersicht wird angezeigt. |  |
| 3 | Anwendungsgruppe eingeben | Im Bild Sicht "Anwendungsgruppe" ändern: Übersicht wählen Sie Neuer Eintrag. Geben Sie folgende Daten ein:Transakt. : <Aus der Auswahlliste wählen>Anwendungsgruppe: <beliebiger Code> | Das Bild Neue Einträge: Übersicht Hinzugefügte wird angezeigt. |  |
| 4 | Daten sichern | Wählen Sie Sichern. |  |  |

### Merkmalsanzeige erstellen

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
| 1 | Anmelden | Melden Sie sich am SAP Fiori Launchpad als Produktkonfigurationsmodellierer an. | Das SAP Fiori Launchpad wird angezeigt. |  |
| 2 | SAP-Fiori-App aufrufen | Wählen Sie Merkmal pflegen Zur Konfiguration anzeigen(CU_CHAR_DISPLAY). | Im Bild Sicht "Anwendungsgruppe" ändern: Übersicht wird angezeigt. |  |
| 3 | Anwendungsgruppe eingeben | Im Bild Sicht "Anwendungsgruppe" ändern: Übersicht wählen Sie Merkmalsanzeige.Wählen Sie Neuer Eintrag. Geben Sie folgende Daten ein, und wählen Sie Enter:Merkm. Anzeige: <beliebiger Code>Beschreibung: <Geben Sie eine Beschreibung für die Merkmalsanzeige ein>.Anwd Gruppe: <Wählen Sie F4, um die Hilfe aufzurufen>. | Das Bild Ansicht "Merkmalsanzeige" ändern: Übersicht wird angezeigt. |  |
| 4 | Merkmal zuordnen | Wählen Sie die im vorhergehenden Schritt erzeugte Merkmalsanzeige, und wählen Sie Merkmalszuordnung.Nehmen Sie folgende Einträge vor:Seq.: <Geben Sie eine Folgenummer zur Festlegung der Merkmalsreihenfolge ein>.Merkmalname: <Suchen Sie nach einem Merkmal, indem Sie die Hilfe über F4 aufrufen>.Sp.: <Geben Sie eine geeignete Spaltenbreite ein, um Merkmalsbezeichnung und -wert anzuzeigen>. | Das Bild Ansicht "Merkmalszuordnung" ändern: Übersicht wird angezeigt. |  |
| 5 | Daten sichern | Wählen Sie Sichern. |  |  |

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
> Flagged while digesting this document, not verified: The overview table gives the same expected result (Anwendungsgruppe wird angelegt) for both steps, and the text cites edition 1711 although the document is release 2608; possibly outdated wording.

## Connections
- part-of :: [[_cluster]]
- related-to :: [[02-business-partner-and-product-master-data/crear-grupo-de-aplicaciones-y-visualizacion-de-caracteristicas-mds-2ni]]
- related-to :: [[02-business-partner-and-product-master-data/create-application-group-and-characteristic-display-mds-2ni-269]]
- related-to :: [[02-business-partner-and-product-master-data/mds-2ni-271]]
- related-to :: [[02-business-partner-and-product-master-data/mds-2ni-273]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/2NI_S4CLD2608_Master_Data_DE_XX.docx` — full document · extracted with `mammoth` · 11,088 chars in the whole document
