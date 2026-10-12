---
id: 13-quality-ehs-and-compliance/stammdatenskript-qualitatsmanagementattribute-fur-material-produktstam
title: "Stammdatenskript: Qualitätsmanagementattribute für Material-/Produktstamm anlegen – SDS (BNY) (BNY_S4CLD2608_Master_Data_DE_XX)"
description: German SAP S/4HANA Cloud 2608 master data script (BNY) for creating quality management view data on a material master via MM01 as product data specialist.
cluster: 13-quality-ehs-and-compliance
tags: [kb/quality-ehs-and-compliance, topic/qm-material-master-attributes]
aliases: [BNY_S4CLD2608_Master_Data_DE_XX]
keywords: [Quality Management View of the Material Master, quality management data, material master, inspection types, automatic usage decision, quality info record, business roles, required organizational units, master data scripts, BNY]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/BNY_S4CLD2608_Master_Data_DE_XX.docx]
confidence: high
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-688
topic: 13-quality-ehs-and-compliance/qm-material-master-attributes
language: DE
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Stammdatenskript: Qualitätsmanagementattribute für Material-/Produktstamm anlegen – SDS (BNY) (BNY_S4CLD2608_Master_Data_DE_XX)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/BNY_S4CLD2608_Master_Data_DE_XX.docx`, extracted with `mammoth`. Grouped under **Quality Management View of the Material Master** in Quality, EHS and Compliance. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

| <!-- image omitted: unnamed --> | StammdatenskriptSAP S/4HANA Cloud Public Edition - 02-07-26 |
| --- | --- |
|  | Qualitätsmanagementattribute für Material-/Produktstamm anlegen – SDS (BNY) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Inhaltsverzeichnis

[1 Verwendungszweck 2](#_Toc233890067)

[2 Voraussetzungen 3](#_Toc233890068)

[2.1 Systemzugriff 3](#_Toc233890069)

[2.2 Rollen 3](#_Toc233890070)

[2.3 Erforderliche Organisationseinheiten 3](#_Toc233890071)

[3 Übersichtstabelle 5](#_Toc233890072)

[4 Testverfahren 6](#_Toc233890073)

[4.1 Qualitätsmanagement-Attribute für Material 6](#_Toc233890074)

## Verwendungszweck

Wenn die Materialqualität überprüft werden soll, setzt dies voraus, dass die Qualitätsmanagement-Sicht für den Materialstamm für dieses Werk gepflegt ist.

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
| Stammdatenexperte – Produktdaten | SAP_BR_PRODMASTER_SPECIALIST | Stammdaten – Produkte / Produkt-Governance | SAP_BR_PRODMASTER_SPECIALIST / SAP_CMD_SPT_PR_GOV_PC |  |

### Erforderliche Organisationseinheiten

In diesem Abschnitt beschreiben und erläutern Sie alle Organisationseinheiten, die für das Anlegen der Stammdatensätze relevant sind

Einige Segmente von Debitorenstammdaten hängen von den Organisationseinheiten des Unternehmens ab. Allgemeine (zentrale) Daten hängen nicht von einer Organisationseinheit oder dem Buchungskreis ab. Die folgende Tabelle stellt eine Übersicht dieser verschiedenen Datensegmente und ihrer relevanten Organisationseinheiten bereit:

| Datensegment | Hängt ab von | Feldbeispiele | Kommentare | Zu verwendende Organisationseinheit |
| --- | --- | --- | --- | --- |
| Qualitätsmanagement | Werk |  | Werksdaten können für jede Werks-ID Ihrer Unternehmensstruktur existieren, für die der Materialstammsatz verwendet wird. | Werk: |

## Übersichtstabelle

Dieser Umfangsbestandteil umfasst die verschiedenen Prozessschritte in der folgenden Tabelle:

|  |
| --- |
| Hinweis Wenn Ihr Systemadministrator Bereiche und Seiten auf dem SAP Fiori Launchpad aktiviert hat, enthält die Startseite nur die wesentlichen Apps, mit denen die typischen Aufgaben einer Benutzerrolle ausgeführt werden können.Alle anderen (suchbaren) Apps, die nicht auf der Startseite enthalten sind, finden Sie über die Suchleiste ([2434549](https://me.sap.com/notes/2434549)).Wenn Sie die Startseite personalisieren und versteckte Apps hinzufügen möchten, wechseln Sie in Ihr Benutzerprofil und wählen Sie App Finder. |

| Prozessschritt | Benutzerrolle | Vorgang/App | Erwartete Ergebnisse |
| --- | --- | --- | --- |
| [Qualitätsmanagement-Attribute für Material](#unique_7) [Seite ] 6 | Stammdatenexperte – Produktdaten | Material anlegen(MM01) | Materialstammdaten – Qualitätsmanagementdaten werden erstellt |

## Testverfahren

In diesem Abschnitt werden die Testverfahren für den jeweiligen Prozessschritt beschrieben, der zum betreffenden Umfangsbestandteil gehört.

### Qualitätsmanagement-Attribute für Material

Testverwaltung

Kundenprojekt: Füllen Sie die projektbezogenen Teile aus.

|  |  |  |  |
| --- | --- | --- | --- |
| Testfall-ID | <X.XX> | Testdatum: |  |
| Testername: |  | Dauer: |  |
| Benutzerrolle(n): |  | Zuständigkeit: | <Geben Sie den Serviceanbieter, einen Kunden oder einen Serviceanbieter zusammen mit einem Kunden an.> |

Vorgehensweise

| Testschrittnummer | Bezeichnung des Testschritts | Anweisung | Erwartetes Ergebnis | Kommentare |
| --- | --- | --- | --- | --- |
| 1 | Anmelden | Melden Sie sich am SAP Fiori Launchpad als Stammdatenexperte – Produktdaten an. | Das SAP Fiori Launchpad wird angezeigt. |  |
| 2 | SAP-Fiori-App aufrufen | Öffnen Sie Material anlegen(MM01). | Die App wird geöffnet. |  |
| 3 | Materialdaten eingeben | Nehmen Sie auf dem Bild Material anlegen (Einstieg) die folgenden Einträge vor:Material: <Materialnummer>Materialart: HandelswareWählen Sie Enter. | Das Bild Sichtenauswahl wird angezeigt. |  |
| 4 | Sicht "Qualitätsmanagement" wählen | Wählen Sie auf dem Bild Sichtenauswahl die Sicht Qualitätsmanagement und dann Organisationsebenen. | Ein neues Bild für die Eingabe von Organisationsdaten wird angezeigt. |  |
| 5 | Organisationsebenendaten eingeben | Nehmen Sie auf dem Bild Organisationsebenen im Abschnitt Organisationsebenen den folgenden Eintrag vor und wählen Sie Weiter:Werk: <Nummer des Werks> | Das Bild Material anlegen (Handelsware) wird angezeigt. |  |
| 6 | Qualitätsmanagementdaten eingeben | Geben Sie auf dem Bild Material <XXX> anlegen (Handelsware) auf der Registerkarte Qualitätsmanagement die Beschreibung für das Material ein:Beschreib.: <Geben Sie die Beschreibung ein.>Geben Sie auf der Registerkarte Qualitätsmanagement im Abschnitt Allgemeine Daten folgende Daten ein:Basismengeneinheit: <Mengeneinheit>Wählen Sie Prüfeinstellung. Wählen Sie im angezeigten Dialogfenster die Option Prüfarten anlegen, und geben Sie folgende Daten ein:Prüfart: z.B. 01Bevorzugte Prüf Typ: XAktiv: XWählen Sie Detail zur Prüfart, um die Details anzuzeigen.Stellen Sie sicher, dass die folgenden Felder mit X markiert sind:In den Qualitätsprüfbestand buchenPrüfung mit ArbeitsplanAutomatische ZuordnungMerkmale prüfenWählen Sie Weiter. |  |  |
| 7 | Automatischen Verwendungsentscheid aktivieren/deaktivieren (optional) | Markieren Sie Auto-VE oder heben Sie die Markierung auf, um den automatischen Verwendungsentscheid für diese Kombination aus Material und Prüfart zu aktivieren bzw. zu deaktivieren.Hinweis Ein automatischer Verwendungsentscheid nach der Ergebniserfassung kann für Prüflose mit positiven Prüfergebnissen vorgenommen werden. Um dies zu ermöglichen, muss Ihr System in der App Lösung verwalten(F1241) entsprechend eingerichtet werden. Weitere technische Informationen und Voraussetzungen finden Sie auf [SAP Help](https://help.sap.com/viewer/DRAFT/84dbf30eedb4450983dc3d1c81b71996/1811.500/en-US/746b66d98e504e238eca043bae05ecb8.html). |  |  |
| 8 | Beschaffungsdaten eingeben (optional) | Wenn Sie optional einen Qualitätsinformationssatz für Material verwenden möchten, geben Sie auf der Registerkarte Qualitätsmanagement im Abschnitt Beschaffungsdaten die folgenden Daten ein:QM-Beschaffung aktiv: XQM-Steuerschlüssel: z.B. 0001 |  |  |
| 9 | Daten sichern | Wählen Sie Sichern. | Ihre Daten werden gesichert. |  |

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
- related-to :: [[13-quality-ehs-and-compliance/create-quality-management-attributes-for-material-product-master-mds-b]]
- related-to :: [[13-quality-ehs-and-compliance/criar-atributos-de-administracao-de-qualidade-para-mestre-de-materiais]]
- related-to :: [[13-quality-ehs-and-compliance/mds-bny-691]]
- related-to :: [[13-quality-ehs-and-compliance/mds-bny-693]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/BNY_S4CLD2608_Master_Data_DE_XX.docx` — full document · extracted with `mammoth` · 10,137 chars in the whole document
