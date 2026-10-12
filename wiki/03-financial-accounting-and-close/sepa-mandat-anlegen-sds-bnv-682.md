---
id: 03-financial-accounting-and-close/sepa-mandat-anlegen-sds-bnv-682
title: SEPA-Mandat anlegen – SDS (BNV) (BNV_S4CLD2608_Master_Data_DE_XX)
description: "German master data script (BNV) for creating, displaying, listing and managing SEPA mandates in SAP S/4HANA Cloud Public Edition 2608."
cluster: 03-financial-accounting-and-close
tags: [kb/financial-accounting-and-close, topic/direct-debit-and-sepa-mandates]
aliases: [BNV_S4CLD2608_Master_Data_DE_XX]
keywords: [Direct Debit and SEPA Mandates, sepa mandates, sepa direct debit, mandate creation, mandate display, mandate lists, mandate management, business roles, customer master data, BNV]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/BNV_S4CLD2608_Master_Data_DE_XX.docx]
confidence: high
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-682
topic: 03-financial-accounting-and-close/direct-debit-and-sepa-mandates
language: DE
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# SEPA-Mandat anlegen – SDS (BNV) (BNV_S4CLD2608_Master_Data_DE_XX)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/BNV_S4CLD2608_Master_Data_DE_XX.docx`, extracted with `mammoth`. Grouped under **Direct Debit and SEPA Mandates** in Financial Accounting and Close. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

| <!-- image omitted: unnamed --> | StammdatenskriptSAP S/4HANA Cloud Public Edition - 02-07-26 |
| --- | --- |
|  | SEPA-Mandat anlegen – SDS (BNV) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Inhaltsverzeichnis

[1 Zweck 2](#_Toc233890044)

[2 Voraussetzungen 3](#_Toc233890045)

[2.1 Systemzugriff 3](#_Toc233890046)

[2.2 Rollen 3](#_Toc233890047)

[2.3 Erforderliche Organisationseinheiten 3](#_Toc233890048)

[2.4 Obligatorische und optionale Stammdaten 4](#_Toc233890049)

[2.5 Wesentliche Parameter für die Datenerstellung 4](#_Toc233890050)

[3 Übersichtstabelle 5](#_Toc233890051)

[4 Testverfahren 6](#_Toc233890052)

[4.1 SEPA-Mandate anlegen 6](#_Toc233890053)

[4.2 SEPA-Mandate anzeigen 7](#_Toc233890054)

[4.3 SEPA-Mandatslisten anzeigen 8](#_Toc233890055)

[4.4 SEPA-Mandate verwalten 9](#_Toc233890056)

## Zweck

Dieses Dokument beschreibt, wie Sie ein Mandat für den einheitlichen Euro-Zahlungsverkehrsraum (SEPA-Mandat) für Ihr SAP S/4HANA Cloud Public Edition-System anlegen. Die Beschreibung umfasst die Datensegmente, die für die SAP S/4HANA Cloud Public Edition-Appliance relevant sind. Felder, die für die von SAP Best Practices bereitgestellten SAP S/4HANA Cloud Public Edition-Inhalte nicht relevant sind, werden in diesem Dokument nicht behandelt.

Ein SEPA-Mandat wird vom Debitor (einem Kunden, der Waren oder Dienstleistungen bezieht) abgeschlossen, um den Kreditor (einen Händler oder Leistungserbringer) zu ermächtigen, Zahlungen über eine SEPA-Lastschrift einzuziehen. Zeitgleich beinhaltet das SEPA-Mandat die Befugnis der Bank des Debitors, diese Einzüge auszuzahlen.

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
| Debitorenbuchhalter | SAP_BR_AR_ACCOUNTANT | Debitorenbuchhaltung | SAP_BR_AR_ACCOUNTANT |  |

### Erforderliche Organisationseinheiten

Einige Segmente von Debitorenstammdaten hängen von den Organisationseinheiten des Unternehmens ab. Allgemeine (zentrale) Daten hängen nicht von einer Organisationseinheit oder dem Buchungskreis ab. Die folgende Tabelle stellt eine Übersicht dieser verschiedenen Datensegmente und ihrer relevanten Organisationseinheiten bereit:

| Datensegment | Hängt ab von | Feldbeispiele | Kommentare | Zu verwendende Organisationseinheit |
| --- | --- | --- | --- | --- |
| Mandat | Geschäftspartner | Debitorennummer, IBAN und SWIFT/BIC | Nur gültige europäische Debitoren mit SEPA-Lastschrift | Debitorennummer: <Ihre Nummer> |
| Mandat | Buchungskreis | Buchungskreis | Buchungskreisdaten können für jede Buchungskreis-ID Ihrer Unternehmensstruktur vorhanden sein, für die das SEPA-Mandat verwendet wird. | Buchungskreis: Ihr Buchungskreis |

### Obligatorische und optionale Stammdaten

Die folgende Tabelle bietet eine Übersicht über die optionalen und obligatorischen Stammdatenobjekte, die in einem Profitcenterstammdatensatz verwendet werden müssen.

| Stammdatenobjekt | Verwendet im Datensegment | Obligatorisch / optional | Kommentare |
| --- | --- | --- | --- |
| Debitorennummer | Einstiegsbild | Obligatorisch |  |
| Buchungskreis | Einstiegsbild | Obligatorisch |  |

### Wesentliche Parameter für die Datenerstellung

In diesem Abschnitt werden einige Basisparameter erläutert, die das Verhalten eines Stammsatzes beeinflussen und zum Anlegen eines SEPA-Mandats immer erforderlich sind:

Buchungskreis:

Zum Beispiel XX10.

Geschäftspartner – Kunde:

z.B. Kundennummer XX100003.

## Übersichtstabelle

Dieser Umfangsbestandteil umfasst mehrere Prozessschritte, die in der folgenden Tabelle aufgelistet sind:

|  |
| --- |
| Hinweis Wenn Ihr Systemadministrator Bereiche und Seiten auf dem SAP Fiori Launchpad aktiviert hat, enthält die Startseite nur die wesentlichen Apps, mit denen die typischen Aufgaben einer Benutzerrolle ausgeführt werden können.Alle anderen (suchbaren) Apps, die nicht auf der Startseite enthalten sind, finden Sie über die Suchleiste ([2434549](https://me.sap.com/notes/2434549)).Wenn Sie die Startseite personalisieren und versteckte Apps hinzufügen möchten, wechseln Sie in Ihr Benutzerprofil und wählen Sie App Finder. |

| Prozessschritt | Anwendungsrolle | SAP-Fiori-App / Transaktion | Erwartete Ergebnisse |
| --- | --- | --- | --- |
| [SEPA-Mandate anlegen](#unique_9) [Seite ] 6 | Debitorenbuchhalter | SEPA-Mandate anlegen(FSEPA_M1) | SEPA-Mandat wird angelegt. |
| [SEPA-Mandate anzeigen](#unique_10) [Seite ] 7 | Debitorenbuchhalter | SEPA-Mandate anzeigen(FSEPA_M3) | Das SEPA-Mandat wird angezeigt. |
| [SEPA-Mandatslisten anzeigen](#unique_11) [Seite ] 8 | Debitorenbuchhalter | SEPA-Mandatslisten anzeigen(FSEPA_M4) | SEPA-Mandatsliste wird angezeigt. |
| [SEPA-Mandate verwalten](#unique_12) [Seite ] 9 | Debitorenbuchhalter | SEPA-Mandate verwalten(F5158) | Das SEPA-Mandat wird angezeigt. |

## Testverfahren

In diesem Abschnitt werden die Testverfahren für den jeweiligen Prozessschritt beschrieben, der zum betreffenden Umfangsbestandteil gehört.

### SEPA-Mandate anlegen

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
| 1 | Anmelden | Melden Sie sich als Debitorenbuchhalter am SAP Fiori Launchpad an. | Das SAP Fiori Launchpad wird angezeigt. |  |
| 2 | SAP-Fiori-App aufrufen | Öffnen Sie SEPA-Mandate anlegen(FSEPA_M1). | Die App wird geöffnet. |  |
| 3 | Anwendung wechseln | Auf der Sicht Mandat anlegen: Einstieg wählen Sie Anwendung wechseln. Wählen Sie im Dialogfenster Anwendung auswählen die Option Finanzwesen, und wählen Sie Weiter. |  |  |
| 4 | Identifikation des Zahlungspflichtigen | Geben Sie im Feld Debitor den Wert XX100003 ein. |  |  |
| 5 | Identifikation des Zahlungsempfängers | Geben Sie im Feld Zahlender Buchungskreis XX10 ein, und wählen Sie Enter, um fortzufahren.Hinweis Wenn ein Bild mit Mandaten mit aktiviertem Status angezeigt wird, bedeutet dies, dass diese Mandate bereits angelegt wurden. Markieren Sie ein Mandat, und wählen Sie Weiter, um das Mandat zu prüfen und zu ändern. | Das Bild Mandat anlegen: Detailbild wird angezeigt. |  |
| 6 | Daten ergänzen | Wählen Sie Daten ergänzen. | Die Felder werden automatisch mit Werten gefüllt. |  |
| 7 | Grunddaten | Geben Sie auf der Registerkarte Grunddaten folgende Daten ein:Status: ErfasstAnkreuzfeld "B2B-Mandat": auswählenOrt der Unterschrift: <Standort>Datum Unterschrift: <Datum> |  |  |
| 8 | Zahlungspflichtiger | Vergewissern Sie sich auf der Registerkarte Zahlungspflichtiger, Abschnitt Bankdaten des Zahlungspflichtigen, dass die Felder IBAN und SWIFT/BIC ausgefüllt sind.Hinweis Diese Daten gehören zu Ihren Kundenstammdaten und sollten bereits angelegt und verfügbar sein. |  |  |
| 9 | Zahlungsempfänger | Geben Sie auf der Registerkarte Zahlungsempfänger folgende Daten ein:Gläubiger-Identifikationsnummer: <Gläubiger-Identifikationsnummer>: |  |  |
| 10 | Daten sichern | Sichern Sie Ihre Eingaben. | Die Systemmeldung Mandat 0000000000## angelegt wird angezeigt. |  |

### SEPA-Mandate anzeigen

Testverwaltung

Kundenprojekt: Füllen Sie die projektbezogenen Teile aus.

|  |  |  |  |
| --- | --- | --- | --- |
| Testfall-ID | <X.XX> | Testdatum: |  |
| Testername: |  | Dauer: |  |
| Benutzerrolle(n): |  | Zuständigkeit: | <Geben Sie den Serviceanbieter, einen Kunden oder einen Serviceanbieter zusammen mit einem Kunden an.> |

Voraussetzung

Ein Mandat ist bereits vorhanden.

Vorgehensweise

| Testschrittnummer | Bezeichnung des Testschritts | Anweisung | Erwartetes Ergebnis | Kommentare |
| --- | --- | --- | --- | --- |
| 1 | Anmelden | Melden Sie sich als Debitorenbuchhalter am SAP Fiori Launchpad an. | Das SAP Fiori Launchpad wird angezeigt. |  |
| 2 | SAP-Fiori-App aufrufen | Öffnen Sie SEPA-Mandate anzeigen(FSEPA_M3). | Die App wird geöffnet. |  |
| 3 | Identifikation des Zahlungspflichtigen | Geben Sie im Feld Debitor den Wert XX100003 ein. |  |  |
| 4 | Identifikation des Zahlungsempfängers | Geben Sie im Feld Zahlender Buchungskreis XX10 ein, und wählen Sie Enter, um fortzufahren. | Das Bild Mandat anzeigen: Detailbild wird angezeigt. |  |
| 5 | Navigation | Wählen Sie die verschiedenen Registerkarten aus:Grunddaten, Regulierer und/oder Zahlungsempfänger. | Die Informationen werden angezeigt. |  |
| 6 | Zurück | Wählen Sie Beenden. |  |  |

### SEPA-Mandatslisten anzeigen

Testverwaltung

Kundenprojekt: Füllen Sie die projektbezogenen Teile aus.

|  |  |  |  |
| --- | --- | --- | --- |
| Testfall-ID | <X.XX> | Testdatum: |  |
| Testername: |  | Dauer: |  |
| Benutzerrolle(n): |  | Zuständigkeit: | <Geben Sie den Serviceanbieter, einen Kunden oder einen Serviceanbieter zusammen mit einem Kunden an.> |

Voraussetzung

Ein Mandat ist bereits vorhanden.

Vorgehensweise

| Testschrittnummer | Bezeichnung des Testschritts | Anweisungen | Erwartetes Ergebnis | Kommentare |
| --- | --- | --- | --- | --- |
| 1 | Anmelden | Melden Sie sich am SAP Fiori Launchpad als Debitorenbuchhalter an. | Das SAP Fiori Launchpad wird angezeigt. |  |
| 2 | SAP-Fiori-App aufrufen | Öffnen Sie SEPA-Mandatslisten anzeigen(FSEPA_M4). | Die App wird geöffnet. |  |
| 3 | "Ausführen" wählen | Wenn ein Dialogfenster angezeigt wird, wählen Sie Finanzwesen im Dialogfenster Anwendung auswählen aus, und wählen Sie dann Weiter.Wenn kein Dialogfenster angezeigt wird, prüfen Sie die Registerkarte Technische Abgrenzungen, und stellen Sie sicher, dass das Feld Anwendung auf Finanzwesen gesetzt ist.Wählen Sie Ausführen. | Das Bild Mandate öffnet sich und zeigt eine Liste der vorhandenen Mandate an. |  |
| 4 | Mandat auswählen | Wählen Sie die Nummer einer Mandatsreferenz aus. | Das Bild Mandaten ändern wird angezeigt und zeigte eine Liste mit den Details zum ausgewählten Mandat an. |  |
| 5 | Prüfen | Obwohl es möglich ist, Mandatsdaten bei Bedarf zu bearbeiten, ändern Sie keine Daten, sondern überprüfen Sie lediglich die Mandatsdaten. |  |  |
| 6 | Beenden | Wählen Sie zweimal Weiter oder Abbrechen, um das Fenster zu verlassen. |  |  |

### SEPA-Mandate verwalten

Testverwaltung

Kundenprojekt: Füllen Sie die projektbezogenen Teile aus.

|  |  |  |  |
| --- | --- | --- | --- |
| Testfall-ID | <X.XX> | Testdatum: |  |
| Testername: |  | Dauer: |  |
| Benutzerrolle(n): |  | Zuständigkeit: | <Geben Sie den Serviceanbieter, einen Kunden oder einen Serviceanbieter zusammen mit einem Kunden an.> |

Voraussetzung

Ein Mandat ist bereits vorhanden.

Vorgehensweise

| Testschrittnummer | Bezeichnung des Testschritts | Anweisung | Erwartetes Ergebnis | Kommentare |
| --- | --- | --- | --- | --- |
| 1 | Anmelden | Melden Sie sich als Debitorenbuchhalter am SAP Fiori Launchpad an. | Das SAP Fiori Launchpad wird angezeigt. |  |
| 2 | SAP-Fiori-App aufrufen | Öffnen Sie SEPA-Mandate verwalten(F5158). | Die App wird geöffnet. |  |
| 3 | Mandat auswählen | Wählen Sie im Feld Anwendung die Option Finanzwesen. |  |  |
| 4 | Mandat auswählen | Im Feld Zahlender Buchungskreis geben Sie XX10 ein.Wählen Sie Start.Markieren Sie die Zeile, die Sie bearbeiten möchten, und wählen Sie Bearbeiten. | Das Bild Mandat ändern: Detail wird angezeigt. |  |
| 5 | Überprüfen und Bearbeiten | Überprüfen und bearbeiten Sie die verfügbaren Felder der folgenden Registerkarten nach Bedarf:GrunddatenZahlungspflichtigerZahlungsempfänger |  |  |
| 6 | Eingaben sichern | Wählen Sie Sichern, um Ihre Einträge zu sichern. |  |  |

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
- related-to :: [[03-financial-accounting-and-close/crear-mandato-sepa-mds-bnv-684]]
- related-to :: [[03-financial-accounting-and-close/create-sepa-mandate-mds-bnv-683]]
- related-to :: [[03-financial-accounting-and-close/criar-mandato-sepa-mds-bnv-686]]
- related-to :: [[03-financial-accounting-and-close/sepa-mds-bnv-685]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/BNV_S4CLD2608_Master_Data_DE_XX.docx` — full document · extracted with `mammoth` · 15,478 chars in the whole document
