---
id: 09-subscription-billing-and-contract-accounting/serviceartbasierte-preiskondition-anlegen-sds-3gd-316
title: Serviceartbasierte Preiskondition anlegen – SDS (3GD) (3GD_S4CLD2608_Master_Data_DE_XX)
description: "German master data script 3GD: create service-type-based sales price conditions PST0, PST1, PST2 via Set Material Prices - Sales (VK12) for convergent billing rating."
cluster: 09-subscription-billing-and-contract-accounting
tags: [kb/subscription-billing-and-contract-accounting, topic/consumption-items-and-rating]
aliases: [3GD_S4CLD2608_Master_Data_DE_XX]
keywords: [Consumption Items and Service-Type-Based Rating, service type pricing, price conditions, material prices, condition types, convergent billing, sales organization, business roles, 3GD]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/3GD_S4CLD2608_Master_Data_DE_XX.docx]
confidence: high
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-316
topic: 09-subscription-billing-and-contract-accounting/consumption-items-and-rating
language: DE
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Serviceartbasierte Preiskondition anlegen – SDS (3GD) (3GD_S4CLD2608_Master_Data_DE_XX)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/3GD_S4CLD2608_Master_Data_DE_XX.docx`, extracted with `mammoth`. Grouped under **Consumption Items and Service-Type-Based Rating** in Subscription Billing and Contract Accounting. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

| <!-- image omitted: unnamed --> | StammdatenskriptSAP S/4HANA Cloud Public Edition - 02-07-26 |
| --- | --- |
|  | Serviceartbasierte Preiskondition anlegen – SDS (3GD) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Inhaltsverzeichnis

[1 Zweck 2](#_Toc233889627)

[2 Voraussetzungen 3](#_Toc233889628)

[2.1 Systemzugriff 3](#_Toc233889629)

[2.2 Rollen 3](#_Toc233889630)

[2.3 Obligatorische und optionale Stammdaten 3](#_Toc233889631)

[3 Übersichtstabelle 4](#_Toc233889632)

[4 Testverfahren 5](#_Toc233889633)

[4.1 Preiskonditionen für PST0 anlegen 5](#_Toc233889634)

[4.2 Preiskonditionen für PST1 anlegen 6](#_Toc233889635)

[4.3 Preiskonditionen für PST2 anlegen 7](#_Toc233889636)

## Zweck

Mit leistungsbezogenen Preiskonditionen lassen sich Informationen hinterlegen, die erforderlich sind, um eine automatische Preisfindung beim Rating in Zusammenhang mit konvergenter Fakturierung durchzuführen. Sie enthalten Preise und Zuschläge auf Basis verschiedener Varianten. Es kann sich dabei um spezifische Konditionen für einen bestimmten Kunden oder ein bestimmtes Material oder eine bestimmte Kombination von Parametern handeln. Eine leistungsbezogene Preiskondition enthält Daten wie etwa einen Preis in einer bestimmten Währung für ein Material. Diese Daten werden verwendet und in den abrechenbaren Positionen, Abrechnungsplanpositionen, Abrechnungs- sowie Fakturierungsbelegen hinterlegt.

Es handelt sich dabei im Allgemeinen um spezifische Informationen für eine bestimmte Verkaufsabteilung innerhalb Ihrer Organisation.

## Voraussetzungen

In diesem Abschnitt sind alle Voraussetzungen für den Test hinsichtlich System, Benutzer, Stammdaten, Organisationsdaten, sonstige Testdaten und Voraussetzungen zusammengefasst.

### Systemzugriff

| System | Details |
| --- | --- |
| System | Erreichbar über SAP Fiori Launchpad. Ihr Systemadministrator stellt Ihnen die URL für den Zugriff auf die verschiedenen Apps zur Verfügung, die Ihrer Rolle zugeordnet sind. |

### Rollen

Legen Sie Benutzerrollen mit den folgenden von SAP ausgelieferten Benutzerrollenvorlagen an, und ordnen Sie sie Ihren einzelnen Testbenutzern zu.

Alternativ können Sie, falls verfügbar, die folgenden von SAP ausgelieferten Bereiche verwenden. Legen Sie einen Bereich mit Seiten an, die vordefinierte grundlegende Apps enthalten, und ordnen Sie sie der Benutzerrolle zu. Anschließend ordnen Sie diese Benutzerrolle Ihren einzelnen Benutzern zu.

Weitere Informationen finden Sie unter Anwendungsrolle aus einer Vorlage anlegen in der [Product Assistance](https://help.sap.com/docs/SAP_S4HANA_CLOUD/53e36b5493804bcdb3f6f14de8b487dd/ec310a8b669a45ca898dc4dd91d97de2.html) für SAP S/4HANA Cloud Public Edition.

| Name (Rollenvorlage) | ID (Rollenvorlage) | Name (Launchpad-Bereich) | ID (Launchpad-Bereich) |
| --- | --- | --- | --- |
| Preisfindungssachbearbeiter | SAP_BR_PRICING_SPECIALIST | Preisverwaltung | SAP_BR_PRICING_SPECIALIST |

### Obligatorische und optionale Stammdaten

Stammdatensätze können auf andere Stammdaten verweisen. Die folgende Tabelle bietet eine Übersicht über die optionalen und obligatorischen Stammdatenobjekte, die in einem Stammdatensatz verwendet werden müssen.

| Stammdatenobjekt | Verwendet im Datensegment | Obligatorisch / optional | Kommentare |
| --- | --- | --- | --- |
| Verkaufsorganisation | Einstiegsbild | Obligatorisch | <Nummer der Verkaufsorganisation> |
| Vertriebsweg | Einstiegsbild | Obligatorisch | <Nummer des Vertriebswegs> |

## Übersichtstabelle

Dieser Stammdatensatz umfasst mehrere Segmente, die in der nachfolgenden Tabelle genannt sind.

|  |
| --- |
| Hinweis Wenn Ihr Systemadministrator Bereiche und Seiten auf dem SAP Fiori Launchpad aktiviert hat, enthält die Startseite nur die wesentlichen Apps, mit denen die typischen Aufgaben einer Benutzerrolle ausgeführt werden können.Alle anderen (suchbaren) Apps, die nicht auf der Startseite enthalten sind, finden Sie über die Suchleiste ([2434549](https://me.sap.com/notes/2434549)).Wenn Sie die Startseite personalisieren und versteckte Apps hinzufügen möchten, wechseln Sie in Ihr Benutzerprofil und wählen Sie App Finder. |

| Segment | Anwendungsrolle | App/Vorgang | Erwartete Ergebnisse |
| --- | --- | --- | --- |
| [Preiskonditionen für PST0 anlegen](#unique_7) [Seite ] 5 | Preisfindungssachbearbeiter | Materialpreise festlegen – Verkauf(VK12) | Die Materialpreiskondition wird gepflegt. |
| [Preiskonditionen für PST1 anlegen](#unique_8) [Seite ] 6 | Preisfindungssachbearbeiter | Materialpreise festlegen – Verkauf(VK12) | Die Materialpreiskondition wird gepflegt. |
| [Preiskonditionen für PST2 anlegen](#unique_9) [Seite ] 7 | Preisfindungssachbearbeiter | Materialpreise festlegen – Verkauf(VK12) | Die Materialpreiskondition wird gepflegt. |

## Testverfahren

Dieser Abschnitt beschreibt die Vorgehensweisen für jedes Segment oder Prozessschritt, das bzw. der Teil dieses Stammsatzes ist.

### Preiskonditionen für PST0 anlegen

Testverwaltung

Kundenprojekt: Füllen Sie die projektbezogenen Teile aus.

|  |  |  |  |
| --- | --- | --- | --- |
| Testfall-ID | <X.XX> | Testdatum: |  |
| Testername: |  | Dauer: |  |
| Benutzerrolle(n): |  | Zuständigkeit: | <Geben Sie den Serviceanbieter, einen Kunden oder einen Serviceanbieter zusammen mit einem Kunden an.> |

Zweck

Dieses Verfahren beschreibt das Anlegen von Verkaufspreiskonditionen. PST0

Vorgehensweise

| Testschrittnummer | Bezeichnung des Testschritts | Anweisungen | Erwartetes Ergebnis | Kommentare |
| --- | --- | --- | --- | --- |
| 1 | Anmelden | Melden Sie sich am SAP Fiori Launchpad als Preisfindungssachbearbeiter an. | Die Startseite wird angezeigt. |  |
| 2 | SAP-Fiori-App aufrufen | Öffnen Sie Materialpreise festlegen – Verkauf(VK12). | Das Bild Konditionssätze ändern wird angezeigt. |  |
| 3 | Preiskonditionsart | Nehmen Sie in der Sicht Konditionssätze ändern die folgenden Einträge vor, und wählen Sie EingebenKonditionsart: PST0 |  |  |
| 4 | Auswählen | Geben Sie in der Sicht Serviceartbas. Preisfind. DE: Auswahl die folgenden Einträge ein, und wählen Sie Ausführen.Verkaufsorganisation: <Verkaufsorganisation>Vertriebsweg: <Vertriebsweg> |  |  |
| 5 | Preiskonditionen ändern | Geben Sie in der Sicht Serviceartbas. Preisfind. DE: Übersicht Folgendes ein, und drücken Sie Sichern.Material: CBPTS002Betrag: <Betrag>ME: <Stück>Gültig ab: <das aktuelle Datum>Gültig bis: z.B. <aktuelles Datum + 1 Jahr> | Die Materialpreiskondition wird gepflegt. |  |

### Preiskonditionen für PST1 anlegen

Testverwaltung

Kundenprojekt: Füllen Sie die projektbezogenen Teile aus.

|  |  |  |  |
| --- | --- | --- | --- |
| Testfall-ID | <X.XX> | Testdatum: |  |
| Testername: |  | Dauer: |  |
| Benutzerrolle(n): |  | Zuständigkeit: | <Geben Sie den Serviceanbieter, einen Kunden oder einen Serviceanbieter zusammen mit einem Kunden an.> |

Zweck

Dieses Verfahren beschreibt das Anlegen von Verkaufspreiskonditionen. PST1

Vorgehensweise

| Testschrittnummer | Bezeichnung des Testschritts | Anweisungen | Erwartetes Ergebnis | Kommentare |
| --- | --- | --- | --- | --- |
| 1 | Anmelden | Melden Sie sich am SAP Fiori Launchpad als Preisfindungssachbearbeiter an. | Die Startseite wird angezeigt. |  |
| 2 | SAP-Fiori-App aufrufen | Öffnen Sie Materialpreise festlegen – Verkauf(VK12). | Das Bild Konditionssätze ändern wird angezeigt. |  |
| 3 | Preiskonditionsart | Geben Sie auf der Sicht Konditionssatz ändern die folgenden Daten ein, und wählen Sie Enter:Konditionsart: PST1 |  |  |
| 4 | Auswählen | Geben Sie in der Sicht Change SrvcTyp-Bsd VarP (PST1): Auswahl die folgenden Einträge ein, und wählen Sie Ausführen.Verkaufsorganisation: VerkaufsorganisationVertriebsweg: Vertriebsweg |  |  |
| 5 | Preiskonditionen ändern | Geben Sie in der Sicht Change SrvcTyp-Bsd VarP (PST1): Übersicht Folgendes ein, und drücken Sie Sichern.Material: CBPTS001Variante: HIGH_ENDBetrag: <Betrag>ME: STGültig ab: <das aktuelle Datum>Gültig bis: z.B. <aktuelles Datum + 1 Jahr> | Die Materialpreiskondition wird gepflegt. |  |

### Preiskonditionen für PST2 anlegen

Testverwaltung

Kundenprojekt: Füllen Sie die projektbezogenen Teile aus.

|  |  |  |  |
| --- | --- | --- | --- |
| Testfall-ID | <X.XX> | Testdatum: |  |
| Testername: |  | Dauer: |  |
| Benutzerrolle(n): |  | Zuständigkeit: | <Geben Sie den Serviceanbieter, einen Kunden oder einen Serviceanbieter zusammen mit einem Kunden an.> |

Zweck

Dieses Verfahren beschreibt das Anlegen von Verkaufspreiskonditionen. PST2

Vorgehensweise

| Testschrittnummer | Bezeichnung des Testschritts | Anweisungen | Erwartetes Ergebnis | Kommentare |
| --- | --- | --- | --- | --- |
| 1 | Anmelden | Melden Sie sich am SAP Fiori Launchpad als Preisfindungssachbearbeiter an. | Die Startseite wird angezeigt. |  |
| 2 | SAP-Fiori-App aufrufen | Öffnen Sie Materialpreise festlegen – Verkauf(VK12). | Das Bild Konditionssätze ändern wird angezeigt. |  |
| 3 | Preiskonditionsart | Geben Sie auf der Sicht Konditionssatz ändern die folgenden Daten ein, und wählen Sie Enter:Konditionsart: PST2 |  |  |
| 4 | Auswählen | Geben Sie in der Sicht SrvcTyp-Bsd Abw.% (PST2): Auswahl die folgenden Einträge ein, und wählen Sie Ausführen.Verkaufsorganisation: VerkaufsorganisationVertriebsweg: Vertriebsweg |  |  |
| 5 | Preiskonditionen ändern | Geben Sie in der Änderungssicht SrvcTyp-Bsd Abw.% (PST2): Übersicht Folgendes ein, und drücken Sie Sichern.Material: CBPTS001Variante: HIGH_ENDBetrag: <Betrag>Gültig ab: <das aktuelle Datum>Gültig bis: z.B. <aktuelles Datum + 1 Jahr> | Die Materialpreiskondition wird gepflegt. |  |

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
- related-to :: [[09-subscription-billing-and-contract-accounting/criar-condicao-de-determinacao-de-precos-baseada-em-tipo-de-servico-md]]
- related-to :: [[09-subscription-billing-and-contract-accounting/master-data-script-create-service-type-based-pricing-condition-mds-3gd]]
- related-to :: [[09-subscription-billing-and-contract-accounting/mds-3gd-319]]
- related-to :: [[09-subscription-billing-and-contract-accounting/mds-3gd-321]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/3GD_S4CLD2608_Master_Data_DE_XX.docx` — full document · extracted with `mammoth` · 12,161 chars in the whole document
