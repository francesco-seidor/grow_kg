---
id: 08-sales-order-management/kundenmaterial-infosatz-anlegen-sds-2yx-292
title: Kundenmaterial-Infosatz anlegen – SDS (2YX) (2YX_S4CLD2608_Master_Data_DE_XX)
description: "German SAP master data script (2YX, 2608): create a customer-material info record in app F2499 as internal sales representative, incl. sales unit conversion."
cluster: 08-sales-order-management
tags: [kb/sales-order-management, topic/customer-material-info-records]
aliases: [2YX_S4CLD2608_Master_Data_DE_XX]
keywords: [Customer-Material Info Records, customer material info, sales unit conversion, business roles, sales organization, distribution channel, master data scripts, fiori launchpad access, test procedures, 2YX]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/2YX_S4CLD2608_Master_Data_DE_XX.docx]
confidence: high
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-292
topic: 08-sales-order-management/customer-material-info-records
language: DE
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Kundenmaterial-Infosatz anlegen – SDS (2YX) (2YX_S4CLD2608_Master_Data_DE_XX)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/2YX_S4CLD2608_Master_Data_DE_XX.docx`, extracted with `mammoth`. Grouped under **Customer-Material Info Records** in Sales Order Management. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

| <!-- image omitted: unnamed --> | StammdatenskriptSAP S/4HANA Cloud Public Edition - 02-07-26 |
| --- | --- |
|  | Kundenmaterial-Infosatz anlegen – SDS (2YX) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Inhaltsverzeichnis

[1 Zweck 2](#_Toc233889598)

[2 Voraussetzungen 3](#_Toc233889599)

[2.1 Systemzugriff 3](#_Toc233889600)

[2.2 Rollen 3](#_Toc233889601)

[2.3 Obligatorische und optionale Stammdaten 3](#_Toc233889602)

[2.4 Obligatorische und optionale Stammdaten 4](#_Toc233889603)

[3 Übersichtstabelle 5](#_Toc233889604)

[4 Testverfahren 6](#_Toc233889605)

[4.1 Kunden-Material-Informationen anlegen 6](#_Toc233889606)

## Zweck

Dieses Dokument beschreibt, wie Sie eine Kunden-Material-Info für Ihr SAP S/4HANA Cloud Public Edition-System anlegen. Die Beschreibung umfasst die Datensegmente, die für die SAP S/4HANA Cloud Public Edition-Appliance relevant sind. Felder, die für den Umfang der SAP S/4HANA Cloud Public Edition-Inhalte nicht relevant sind, werden in diesem Dokument nicht behandelt.

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
| Vertriebsmitarbeiter im Innendienst | SAP_BR_INTERNAL_SALES_REP | Interner Vertrieb / Kundenretouren / Abrechnung | SAP_BR_INTERNAL_SALES_REP / SAP_SD_SPT_RETURNS_INT_SALES_PC / SAP_SD_SPT_BILLING_INT_SALES_PC |  |

### Obligatorische und optionale Stammdaten

| Stammdatenobjekt | Verwendet im Datensegment | Obligatorisch / optional | Kommentare |
| --- | --- | --- | --- |
| Kunde | Einstiegsbild | obligatorisch |  |
| Verkaufsorganisation | Einstiegsbild | obligatorisch |  |
| Vertriebsweg | Einstiegsbild | obligatorisch |  |
| Material | Einstiegsbild | optional |  |

### Obligatorische und optionale Stammdaten

In diesem Abschnitt erhalten Sie einige grundlegende Parameter, die das Verhalten eines Stammsatzes beeinflussen und zum Anlegen einer Preiskondition immer erforderlich sind:

Verkaufsorganisation: <Verkaufsorganisation>

Vertriebsweg: <Vertriebsweg>

Kunde: <Kunde>

Material: <Materialnummer>

## Übersichtstabelle

Dieser Umfangsbestandteil umfasst die verschiedenen Schritte in der folgenden Tabelle:

|  |
| --- |
| Hinweis Wenn Ihr Systemadministrator Bereiche und Seiten auf dem SAP Fiori Launchpad aktiviert hat, enthält die Startseite nur die wesentlichen Apps, mit denen die typischen Aufgaben einer Benutzerrolle ausgeführt werden können.Alle anderen (suchbaren) Apps, die nicht auf der Startseite enthalten sind, finden Sie über die Suchleiste ([2434549](https://me.sap.com/notes/2434549)).Wenn Sie die Startseite personalisieren und versteckte Apps hinzufügen möchten, wechseln Sie in Ihr Benutzerprofil und wählen Sie App Finder. |

| Prozessschritt | Benutzerrolle | SAP-Fiori-App / Transaktion | Erwartete Ergebnisse |
| --- | --- | --- | --- |
| [Kunden-Material-Informationen anlegen](#unique_8) [Seite ] 6 | Vertriebsmitarbeiter im Innendienst | Kundenmaterialien verwalten(F2499) | Der Kundenmaterial-Infosatz wird angelegt. |

## Testverfahren

In diesem Abschnitt werden die Testverfahren für den jeweiligen Prozessschritt beschrieben, der zum betreffenden Umfangsbestandteil gehört.

### Kunden-Material-Informationen anlegen

Testverwaltung

Kundenprojekt: Füllen Sie die projektbezogenen Teile aus.

|  |  |  |  |
| --- | --- | --- | --- |
| Testfall-ID | <X.XX> | Testdatum: |  |
| Testername: |  | Dauer: |  |
| Benutzerrolle(n): |  | Zuständigkeit: | <Geben Sie den Serviceanbieter, einen Kunden oder einen Serviceanbieter zusammen mit einem Kunden an.> |

Vorgehensweise

| Testschritt | Bezeichnung des Testschritts | Anweisungen | Erwartetes Ergebnis | Kommentare |
| --- | --- | --- | --- | --- |
| 1 | Anmelden | Melden Sie sich am SAP Fiori Launchpad als Vertriebsmitarbeiter im Innendienst an. | Das SAP Fiori Launchpad wird angezeigt. |  |
| 2 | SAP-Fiori-App aufrufen | Öffnen Sie Kundenmaterialien verwalten(F2499). | Die App wird geöffnet. |  |
| 3 | Bild zum Anlegen von Kundenmaterial aufrufen | Wählen Sie Anlegen. | Das Bild Kundenmaterial wird angezeigt. |  |
| 4 | Grundlegende Informationen zum Kundenmaterial eingeben | Tragen Sie Folgendes ein:Debitor: <Kunde>Produkt: <Materialnummer>Verkaufsorganisation: <Verkaufsorganisation>Vertriebsweg: <Vertriebsweg>Kundenmaterialbeschreibung: Geben Sie eine Beschreibung für den Kunden und das Material ein. | Die grundlegenden Informationen zu Kunde und Material sind gepflegt. |  |
| 5 | Verkaufsmengeneinheit eingeben | Geben Sie im Abschnitt Einheitenumrechnung die folgenden Daten ein:1 PAL (Kundeneinheit): 2 ST (Basiseinheit) | Die Verkaufsmengeneinheit für die Kunden-Material-Kombination wird gepflegt.HinweisUm die Verkaufsmengeneinheit und die Umrechnung auf diesem Bild zu pflegen, müssen die Materialstammdaten der Mengeneinheit und die Umrechnung gepflegt werden. Weitere Informationen können Sie in anderen Stammdatenskripts erhalten, z.B. Produktstamm vom Typ „Handelsware“ anlegen – SDS - BNF für Handelsware.Sobald die Verkaufsmengeneinheit auf diesem Bild eingegeben wurde, wird sie im Verkaufsbeleg angezeigt. |  |
| 6 | "Anlegen" wählen | Wählen Sie Anlegen. | Das Kundenmaterial wurde erfolgreich angelegt. |  |

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
- related-to :: [[08-sales-order-management/crear-registro-info-para-cliente-y-material-mds-2yx-294]]
- related-to :: [[08-sales-order-management/create-customer-material-info-record-mds-2yx-293]]
- related-to :: [[08-sales-order-management/criar-registro-info-de-material-do-cliente-mds-2yx-296]]
- related-to :: [[08-sales-order-management/mds-2yx-295]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/2YX_S4CLD2608_Master_Data_DE_XX.docx` — full document · extracted with `mammoth` · 8,976 chars in the whole document
