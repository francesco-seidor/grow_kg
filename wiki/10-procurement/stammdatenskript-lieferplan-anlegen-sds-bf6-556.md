---
id: 10-procurement/stammdatenskript-lieferplan-anlegen-sds-bf6-556
title: "Stammdatenskript: Lieferplan anlegen – SDS (BF6) (BF6_S4CLD2608_Master_Data_DE_XX)"
description: "German master data script (BF6) for SAP S/4HANA Cloud Public Edition 2608: creating scheduling agreements (Lieferplan) for standard, consignment and subcontracting procurement."
cluster: 10-procurement
tags: [kb/procurement, topic/scheduling-agreements]
aliases: [BF6_S4CLD2608_Master_Data_DE_XX]
keywords: [Purchase Scheduling Agreements, scheduling agreements, purchasing master data, number ranges, consignment procurement, subcontracting procurement, standard procurement, business roles, organizational units, test procedures]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/BF6_S4CLD2608_Master_Data_DE_XX.docx]
confidence: high
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-556
topic: 10-procurement/scheduling-agreements
language: DE
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Stammdatenskript: Lieferplan anlegen – SDS (BF6) (BF6_S4CLD2608_Master_Data_DE_XX)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/BF6_S4CLD2608_Master_Data_DE_XX.docx`, extracted with `mammoth`. Grouped under **Purchase Scheduling Agreements** in Procurement. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

| <!-- image omitted: unnamed --> | StammdatenskriptSAP S/4HANA Cloud Public Edition - 02-07-26 |
| --- | --- |
|  | Lieferplan anlegen – SDS (BF6) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Inhaltsverzeichnis

[1 Zweck 2](#_Toc233889889)

[2 Voraussetzungen 3](#_Toc233889890)

[2.1 Systemzugriff 3](#_Toc233889891)

[2.2 Rollen 3](#_Toc233889892)

[2.3 Erforderliche Organisationseinheiten 3](#_Toc233889893)

[2.4 Obligatorische und optionale Stammdaten 4](#_Toc233889894)

[2.5 Wesentliche Parameter für die Datenerstellung 4](#_Toc233889895)

[2.5.1 Nummernkreise 4](#_Toc233889896)

[3 Übersichtstabelle 5](#_Toc233889897)

[4 Testverfahren 6](#_Toc233889898)

[4.1 Lieferplan für Standardbeschaffung anlegen 6](#_Toc233889899)

[4.1.1 Anlegen von Lieferplan mit Abrufbeleg – Standard 6](#_Toc233889900)

[4.1.2 Anlegen von Lieferplan ohne Abrufbeleg – Standard 8](#_Toc233889901)

[4.2 Lieferplan für Konsignationsbeschaffung anlegen 10](#_Toc233889902)

[4.3 Lieferplan für Lohnbearbeitungsbeschaffung anlegen 12](#_Toc233889903)

## Zweck

Dieses Dokument beschreibt, wie Sie einen Lieferplan für Ihr SAP S/4HANA Cloud Public Edition-System anlegen. Die Beschreibung umfasst die Datensegmente, die für die SAP S/4HANA Cloud Public Edition-Appliance relevant sind, z.B. Einkaufsdaten, Materialdaten und Lieferantendaten. Felder, die für die von SAP Best Practices bereitgestellten SAP S/4HANA Cloud Public Edition-Inhalte nicht relevant sind, werden in diesem Dokument nicht behandelt.

Ein Lieferplan ist eine langfristige Vereinbarung mit einem Lieferanten zur Versorgung mit Materialien zu vorher vereinbarten Bedingungen. Diese Bedingungen gelten für einen vordefinierten Zeitraum und für eine vordefinierte Gesamtmenge.

Die wichtigsten Vorteile von Lieferplänen sind folgende:

- Ein Lieferplan kann viele Bestellungen bzw. Kontraktabrufe ersetzen.
- Es handelt sich um eine langfristige Vereinbarung, im Rahmen derer Sie bessere Preise mit einem Lieferanten verhandelt können.

Es gibt folgende Positionstypen:

- Standardbeschaffung
- Konsignationsbeschaffung
- Lohnbearbeitungsbeschaffung

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
| Einkäufer | SAP_BR_PURCHASER | Einkauf / Ausschreibungen und Kontrakte | SAP_MM_SPT_PURCHASING_PC / SAP_MM_SPT_SOURCING_PC |  |

### Erforderliche Organisationseinheiten

Die Organisationsstruktur und die Stammdaten Ihres Unternehmens wurden bei der Implementierung in Ihrem ERP-System angelegt. Die Organisationsstruktur gibt den Aufbau Ihres Unternehmens wieder. Die folgende Tabelle stellt eine Übersicht dieser verschiedenen Datensegmente und ihrer relevanten Organisationseinheiten bereit:

| Datensegment | Hängt ab von | Feldbeispiele | Kommentare | Zu verwendende Organisationseinheit |
| --- | --- | --- | --- | --- |
| Einkaufsdaten | Einkaufsorganisation | Einkäufergruppe, Materialgruppe, WE-Bearbeitungszeit usw. | Einkaufsdaten können für jede Einkaufsorganisation existieren, für die das Material in den Einkaufsvorgängen verwendet wird. | Einkaufsorganisation:__________ |

### Obligatorische und optionale Stammdaten

Der Lieferplan kann sich auf weitere Stammdaten beziehen. Die folgende Tabelle stellt eine Übersicht optionaler und obligatorischer Stammdatenobjekte für die Verwendung in einem Lieferplan bereit.

| Stammdatenobjekt | Verwendet im Datensegment | Obligatorisch / optional | Kommentare |
| --- | --- | --- | --- |
| Material |  | Obligatorisch | Um das Material einzugeben, legen Sie zuerst Materialstammdaten an. |
| Lieferant |  | Obligatorisch | Um den Lieferanten einzugeben, legen Sie zuerst Lieferantenstammdaten an. |

### Wesentliche Parameter für die Datenerstellung

Dieser Abschnitt beschreibt die Basisparameter, die das Verhalten eines Lieferplans beeinflussen und bei jedem Anlegen eines Lieferplans erforderlich sind.

#### Nummernkreise

Die folgenden Nummernkreise sind für den Lieferplan definiert:

| Nummernkreis | Bereich / Geschäftspartner-ID | Kommentare |
| --- | --- | --- |
| Intern numerisch | Interner nummerischer Nummernkreis für Standardverwendung:5500000000 – 5599999999 | Dieser Nummernkreis wird verwendet, wenn das System einem Lieferplan automatisch eine numerische Nummer zuordnet. |
| Extern numerisch | Externer numerischer Nummernkreis:5600000000 – 5699999999 | Dieser Nummernkreis ist für die externe numerische Nummernvergabe reserviert. |

## Übersichtstabelle

|  |
| --- |
| Hinweis Wenn Ihr Systemadministrator Bereiche und Seiten auf dem SAP Fiori Launchpad aktiviert hat, enthält die Startseite nur die wesentlichen Apps, mit denen die typischen Aufgaben einer Benutzerrolle ausgeführt werden können.Alle anderen (suchbaren) Apps, die nicht auf der Startseite enthalten sind, finden Sie über die Suchleiste ([2434549](https://me.sap.com/notes/2434549)).Wenn Sie die Startseite personalisieren und versteckte Apps hinzufügen möchten, wechseln Sie in Ihr Benutzerprofil und wählen Sie App Finder. |

| Prozessschritt | Anwendungsrolle | App/Transaktion | Erwartete Ergebnisse |
| --- | --- | --- | --- |
|  |  |  |  |
| [Anlegen von Lieferplan mit Abrufbeleg – Standard](#unique_10) [Seite ] 6 | Einkäufer | Einkaufslieferpläne verwalten(F2179) | Lieferplan mit Abrufbeleg – Standard |
| [Anlegen von Lieferplan ohne Abrufbeleg – Standard](#unique_11) [Seite ] 8 | Einkäufer | Einkaufslieferpläne verwalten(F2179) | Lieferplan ohne Abrufbeleg – Standard |
| [Lieferplan für Konsignationsbeschaffung anlegen](#unique_12) [Seite ] 10 | Einkäufer | Einkaufslieferpläne verwalten(F2179) | Lieferplan für Konsignationsbeschaffung wird angelegt. |
| [Lieferplan für Lohnbearbeitungsbeschaffung anlegen](#unique_13) [Seite ] 12 | Einkäufer | Einkaufslieferpläne verwalten(F2179) | Lieferplan für Lohnbearbeitungsbeschaffung wird angelegt. |

## Testverfahren

In diesem Abschnitt werden die Testverfahren für den jeweiligen Prozessschritt beschrieben, der zum betreffenden Umfangsbestandteil gehört.

### Lieferplan für Standardbeschaffung anlegen

#### Anlegen von Lieferplan mit Abrufbeleg – Standard

Testverwaltung

Kundenprojekt: Füllen Sie die projektbezogenen Teile aus.

|  |  |  |  |
| --- | --- | --- | --- |
| Testfall-ID | <X.XX> | Testdatum: |  |
| Testername: |  | Dauer: |  |
| Benutzerrolle(n): |  | Zuständigkeit: | <Geben Sie den Serviceanbieter, einen Kunden oder einen Serviceanbieter zusammen mit einem Kunden an.> |

Zweck

Anlegen eines Lieferplans für Standardbeschaffung

Vorgehensweise

| Testschrittnummer | Bezeichnung des Testschritts | Anweisungen | Erwartetes Ergebnis | Bestanden/Nicht bestanden/Anmerkung |
| --- | --- | --- | --- | --- |
| 1 | Anmelden | Melden Sie sich am SAP Fiori Launchpad als Einkäufer an. | Das SAP Fiori Launchpad wird angezeigt. |  |
| 2 | SAP-Fiori-App aufrufen | Öffnen Sie Einkaufslieferpläne verwalten(F2179). | Die App wird geöffnet. |  |
| 3 | Lieferplan anlegen | Wählen Sie Anlegen, um einen neuen Lieferplan anzulegen. | Das Bild Neuer Einkaufslieferplan wird angezeigt. |  |
| 4 | Kopfdaten eingeben | Legen Sie einen neuen Lieferplan mit den folgenden Daten an:Lieferant: <Lieferant>Vertragsart: LPA (Lieferplan mit Abrufbeleg)Gültigkeitsbeginn: <MM/TT/JJJJ>.Gültig bis: <MM/TT/JJJJ>Buchungskreis: <Buchungskreis>:Einkaufsorganisation: <Einkaufsorganisation>Einkäufergruppe: <Einkäufergruppe>Zielwert: <Zielwert> |  |  |
| 5 | Kopfnotizen eingeben | Navigieren Sie zum Abschnitt Notizen, und geben Sie einige der folgenden Kopfnotizen ein:KopftextKopfnotizPreisfindungsartFristenLieferbedingungenVersandvorschriftZahlungsbedingungenGewährleistungenStrafe bei VertragsverletzungGarantienZusatzklauseln zu VertragAnlageSonstige vertragliche VereinbarungAnlieferungLieferantennotiz (allgemein)Lieferantennotiz (Ekorg) |  |  |
| 6 | Positionen zum Lieferplan hinzufügen | Wählen Sie auf dem Bild Neuer Einkaufslieferplan die Facetten Positionen, und wählen Sie Anlegen. | Das Bild Einkaufslieferplanposition wird angezeigt. |  |
| 7 | Positionsdaten eingeben | Geben Sie auf dem Facettenbild Positionen Folgendes ein:Werk: <Werk>:Material: <Material>Zielmenge: <Zielmenge>Nettobestellpreis: <Bestellnettopreis>Steuerkennzeichen: <XX (der Vorschlagswert aus Infosatz)>Steuerdatum: <aktuelles Datum als Standardwert verwenden>Geben Sie im Bereich Ausgabesteuerung folgende Daten ein:Erstellungsprofil: <Erstellungsprofil>:Wählen Sie unten auf dem Bild Übernehmen. |  |  |
| 8 | Anlegen | Kehren Sie zum Bild Neuer Einkaufslieferplan zurück, und wählen Sie unten auf dem Bild Anlegen.Notieren Sie die Lieferplannummer. | Ein Lieferplan wird angelegt. |  |

#### Anlegen von Lieferplan ohne Abrufbeleg – Standard

Testverwaltung

Kundenprojekt: Füllen Sie die projektbezogenen Teile aus.

|  |  |  |  |
| --- | --- | --- | --- |
| Testfall-ID | <X.XX> | Testdatum: |  |
| Testername: |  | Dauer: |  |
| Benutzerrolle(n): |  | Zuständigkeit: | <Geben Sie den Serviceanbieter, einen Kunden oder einen Serviceanbieter zusammen mit einem Kunden an.> |

Zweck

Anlegen eines Lieferplans für Standardbeschaffung

Vorgehensweise

| Testschrittnummer | Bezeichnung des Testschritts | Anweisungen | Erwartetes Ergebnis | Bestanden/Nicht bestanden/Anmerkung |
| --- | --- | --- | --- | --- |
| 1 | Anmelden | Melden Sie sich am SAP Fiori Launchpad als Einkäufer an. | Das SAP Fiori Launchpad wird angezeigt. |  |
| 2 | SAP-Fiori-App aufrufen | Öffnen Sie Einkaufslieferpläne verwalten(F2179). | Die Listenseite Einkaufslieferpläne verwalten(F2179) wird angezeigt. |  |
| 3 | Lieferplan anlegen | Wählen Sie Anlegen, um einen neuen Lieferplan anzulegen. | Die Kopfsicht Neuer Einkaufslieferplan wird angezeigt. |  |
| 4 | Kopfdaten eingeben | Legen Sie einen neuen Lieferplan mit den folgenden Daten an:Lieferant: <Lieferant>Vertragsart: LP (Lieferplan)Gültigkeitsbeginn: <MM/TT/JJJJ>.Gültig bis: <MM/TT/JJJJ>Buchungskreis: <Buchungskreis>:Einkaufsorganisation: <Einkaufsorganisation>Einkäufergruppe: <Einkäufergruppe>Zielwert: <Zielwert> |  |  |
| 5 | Kopfnotizen eingeben | Navigieren Sie zum Abschnitt Notizen, und geben Sie einige der folgenden Kopfnotizen ein:KopftextKopfnotizPreisfindungsartFristenLieferbedingungenVersandvorschriftZahlungsbedingungenGewährleistungenStrafe bei VertragsverletzungGarantienZusatzklauseln zu VertragAnlageSonstige vertragliche VereinbarungAnlieferungLieferantennotiz (allgemein)Lieferantennotiz (Ekorg) |  |  |
| 6 | Positionen zum Lieferplan hinzufügen | Wählen Sie in der Sicht Neuer Einkaufslieferplan die Facetten Positionen, und wählen Sie Anlegen. | Die Sicht Einkaufslieferplanposition wird angezeigt. |  |
| 7 | Positionsdaten eingeben | Geben Sie auf dem Facettenbild Positionen Folgendes ein:Werk: <Werk>:Material: <Material>Zielmenge: <Zielmenge>Nettobestellpreis: <Bestellnettopreis>Steuerkennzeichen: <XX (der Vorschlagswert aus Infosatz)>Steuerdatum: <aktuelles Datum als Standardwert verwenden>Wählen Sie unten auf dem Bild Übernehmen. |  |  |
| 8 | Anlegen | Kehren Sie zur Kopfsicht Neuer Einkaufslieferplan zurück, und wählen Sie unten in der Sicht Anlegen.Notieren Sie die Lieferplannummer. | Ein Lieferplan wird angelegt. |  |

### Lieferplan für Konsignationsbeschaffung anlegen

Testverwaltung

Kundenprojekt: Füllen Sie die projektbezogenen Teile aus.

|  |  |  |  |
| --- | --- | --- | --- |
| Testfall-ID | <X.XX> | Testdatum: |  |
| Testername: |  | Dauer: |  |
| Benutzerrolle(n): |  | Zuständigkeit: | <Geben Sie den Serviceanbieter, einen Kunden oder einen Serviceanbieter zusammen mit einem Kunden an.> |

Verwendungszweck

Lieferplan für Konsignationsbeschaffung anlegen

Vorgehensweise

| Testschrittnummer | Bezeichnung des Testschritts | Anweisungen | Erwartetes Ergebnis | Bestanden/Nicht bestanden/Anmerkung |
| --- | --- | --- | --- | --- |
| 1 | Anmelden | Melden Sie sich als Einkäufer am SAP Fiori Launchpad an. | Das SAP Fiori Launchpad wird angezeigt. |  |
| 2 | SAP-Fiori-App aufrufen | Öffnen Sie Einkaufslieferpläne verwalten(F2179). | Die Listenseite Lieferpläne verwalten wird angezeigt. |  |
| 3 | Lieferplan anlegen | Wählen Sie Anlegen, um einen neuen Lieferplan anzulegen. | Der Kopf der Sicht Neuer Lieferplan wird angezeigt. |  |
| 4 | Kopfdaten eingeben | Legen Sie einen neuen Lieferplan mit den folgenden Daten an:Vereinbarungstyp: LP (Lieferplan)Lieferant: <Lieferant>Gültigkeitsbeginn: Standard heuteGültigkeitsende: <MM/TT/JJJJ>, z.B. heute + 720 TageEinkäufergruppe: <Einkäufergruppe>Einkaufsorganisation: <Einkaufsorganisation>Buchungskreis: <Buchungskreis>Zielwert: z.B. XXXXX EUR |  |  |
| 5 | Positionen zum Lieferplan hinzufügen | Wählen Sie in der Sicht Neuer Einkaufslieferplan die Facetten Positionen, und wählen Sie Anlegen. | Die Sicht Neue Lieferplanposition wird angezeigt. |  |
| 6 | Positionsdaten eingeben | Geben Sie in der Facettensicht Positionen folgende Daten ein:Positionstyp: K (Konsignation)Werk: <Werk>Material: <Material>Zielmenge: <Zielmenge>Steuerkennzeichen: XX (Vorschlagswert aus Infosatz)Steuerdatum: Standard heuteHinweis Wenn die URA aktiviert ist und die Steuerregistrierungsländer für den Buchungskreis im Finanzwesen-Konfigurationsschritt 103464 (URA aktivieren und Steuerregistrierungsländer pflegen) gepflegt sind, kann das Steuerland übernommen werden. Sie können aber auch einen anderen Wert für das Steuerland aus der Liste auswählen.Hinweis Abhängig von Ihrer Konfigurationsumgebung können Sie auf die Konfigurationsschritte unter Lösung konfigurieren im SAP Fiori Launchpad oder in der App Business Processes Configuration in der Projekterfahrung von SAP Central Business Configuration zugreifen.Wählen Sie unten in der Sicht Übernehmen. |  |  |
| 7 | Anlegen | Kehren Sie zur Sicht Neuer Einkaufslieferplan zurück, und wählen Sie unten in der Sicht Anlegen.Notieren Sie die Lieferplannummer. | Ein Lieferplan wird angelegt. |  |

### Lieferplan für Lohnbearbeitungsbeschaffung anlegen

Testverwaltung

Kundenprojekt: Füllen Sie die projektbezogenen Teile aus.

|  |  |  |  |
| --- | --- | --- | --- |
| Testfall-ID | <X.XX> | Testdatum: |  |
| Testername: |  | Dauer: |  |
| Benutzerrolle(n): |  | Zuständigkeit: | <Geben Sie den Serviceanbieter, einen Kunden oder einen Serviceanbieter zusammen mit einem Kunden an.> |

Verwendungszweck

Lieferplan für Lohnbearbeitungsbeschaffung anlegen

Vorgehensweise

| Testschrittnummer | Bezeichnung des Testschritts | Anweisungen | Erwartetes Ergebnis | Bestanden/Nicht bestanden/Anmerkung |
| --- | --- | --- | --- | --- |
| 1 | Anmelden | Melden Sie sich am SAP Fiori Launchpad als Einkäufer an. | Das SAP Fiori Launchpad wird angezeigt. |  |
| 2 | SAP-Fiori-App aufrufen | Öffnen Sie Einkaufslieferpläne verwalten(F2179). | Die Listenseite Lieferpläne verwalten wird angezeigt. |  |
| 3 | Lieferplan anlegen | Wählen Sie Anlegen, um einen neuen Lieferplan anzulegen. | Der Kopf der Sicht Neuer Lieferplan wird angezeigt. |  |
| 4 | Kopfdaten eingeben | Legen Sie einen neuen Lieferplan mit den folgenden Daten an:Vereinbarungstyp: LP (Lieferplan)Lieferant: <Lieferant>Gültigkeitsbeginn: Standard heuteGültigkeitsende: <MM/TT/JJJJ>, z.B. heute + 720 TageEinkäufergruppe: <Einkäufergruppe>Einkaufsorganisation: <Einkaufsorganisation>Buchungskreis: <Buchungskreis>Zielwert: z.B. XXXXX EUR |  |  |
| 5 | Positionen zum Lieferplan hinzufügen | Wählen Sie in der Sicht Neuer Einkaufslieferplan die Facetten Positionen, und wählen Sie Anlegen. | Die Sicht Neue Lieferplanposition wird angezeigt. |  |
| 6 | Positionsdaten eingeben | Geben Sie in der Facettensicht Positionen folgende Daten ein:Positionstyp: L (Lohnbearbeitung)Werk: <Werk>Lagerort: <Lagerort>Material: <Material>Nettobestellpreis: Vorschlagswert aus InfosatzZielmenge: <Zielmenge>Steuerkennzeichen: XX (Vorschlagswert aus Infosatz)Steuerdatum: Standard heuteHinweis Wenn die URA aktiviert ist und die Steuerregistrierungsländer für den Buchungskreis im Finanzwesen-Konfigurationsschritt 103464 (URA aktivieren und Steuerregistrierungsländer pflegen) gepflegt sind, kann das Steuerland übernommen werden. Sie können aber auch einen anderen Wert für das Steuerland aus der Liste auswählen.Hinweis Abhängig von Ihrer Konfigurationsumgebung können Sie auf die Konfigurationsschritte unter Lösung konfigurieren im SAP Fiori Launchpad oder in der App Business Processes Configuration in der Projekterfahrung von SAP Central Business Configuration zugreifen.Wählen Sie unten in der Sicht Übernehmen. |  |  |
| 7 | Anlegen | Kehren Sie zur Sicht Neuer Einkaufslieferplan zurück, und wählen Sie unten in der Sicht Anlegen.Notieren Sie die Lieferplannummer. | Ein Lieferplan wird angelegt. |  |

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
- related-to :: [[10-procurement/master-data-script-create-scheduling-agreement-mds-bf6-557]]
- related-to :: [[10-procurement/mds-bf6-559]]
- related-to :: [[10-procurement/mds-bf6-561]]
- related-to :: [[10-procurement/script-de-dados-mestre-criar-programa-de-remessas-mds-bf6-560]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/BF6_S4CLD2608_Master_Data_DE_XX.docx` — full document · extracted with `mammoth` · 20,373 chars in the whole document
