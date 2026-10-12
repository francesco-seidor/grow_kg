---
id: 11-inventory-warehouse-and-transportation/neue-offene-mm-buchungsperiode-anlegen-sds-bnz-694
title: Neue offene MM-Buchungsperiode anlegen – SDS (BNZ) (BNZ_S4CLD2608_Master_Data_DE_XX)
description: "German SAP master data script (BNZ, 2608): close the MM period and open a new posting period with Perioden abschließen (MMPV) as Stammdatenexperte – Produktdaten."
cluster: 11-inventory-warehouse-and-transportation
tags: [kb/inventory-warehouse-and-transportation, topic/mm-posting-periods]
aliases: [BNZ_S4CLD2608_Master_Data_DE_XX]
keywords: [MM Posting Periods, mm posting period, period closing, material valuation, business roles, fiori launchpad access, master data scripts, test procedures, BNZ]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/BNZ_S4CLD2608_Master_Data_DE_XX.docx]
confidence: high
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-694
topic: 11-inventory-warehouse-and-transportation/mm-posting-periods
language: DE
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Neue offene MM-Buchungsperiode anlegen – SDS (BNZ) (BNZ_S4CLD2608_Master_Data_DE_XX)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/BNZ_S4CLD2608_Master_Data_DE_XX.docx`, extracted with `mammoth`. Grouped under **MM Posting Periods** in Inventory, Warehouse and Transportation. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

| <!-- image omitted: unnamed --> | StammdatenskriptSAP S/4HANA Cloud Public Edition - 02-07-26 |
| --- | --- |
|  | Neue offene MM-Buchungsperiode anlegen – SDS (BNZ) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Inhaltsverzeichnis

[1 Zweck 2](#_Toc233890064)

[2 Voraussetzungen 3](#_Toc233890065)

[2.1 Systemzugriff 3](#_Toc233890066)

[2.2 Rollen 3](#_Toc233890067)

[3 Übersichtstabelle 4](#_Toc233890068)

[4 Testverfahren 5](#_Toc233890069)

[4.1 MM-Periode schließen und neue Buchungsperiode öffnen 5](#_Toc233890070)

## Zweck

Informationen zum Materialbestand sowie bestimmte Bewertungsdaten wie Gesamtbestandswert, Gesamtbestand, Bewertungselementklasse, Preissteuerungskennzeichen und Preiseinheit enthält die Finanzbuchungsperiode. Die Periode muss am Anfang jeder neuen Buchungsperiode eingerichtet werden, um sicherzustellen, dass Werte und Warenbewegungen in die korrekte Periode gebucht werden. Normalerweise ist nur die aktuelle Buchungsperiode für Buchungen geöffnet. Alle anderen Buchungsperioden sind geschlossen.

Eine Rückbuchung in eine vorherige Periode ist nur möglich, wenn das entsprechende Kennzeichen im Verwaltungssatz gesetzt ist. Dieses Kennzeichen wird automatisch bei der Initialisierung und nach jeder Periodenänderung gesetzt. In bestimmten Fällen kann es jedoch notwendig sein, das Kennzeichen manuell zu setzen.

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
| Stammdatenexperte – Produktdaten | SAP_BR_PRODMASTER_SPECIALIST | Stammdaten – Produkte / Produkt-Governance | SAP_BR_PRODMASTER_SPECIALIST / SAP_CMD_SPT_PR_GOV_PC |  |

## Übersichtstabelle

Dieser Umfangsbestandteil umfasst die verschiedenen Prozessschritte in der folgenden Tabelle:

|  |
| --- |
| Hinweis Wenn Ihr Systemadministrator Bereiche und Seiten auf dem SAP Fiori Launchpad aktiviert hat, enthält die Startseite nur die wesentlichen Apps, mit denen die typischen Aufgaben einer Benutzerrolle ausgeführt werden können.Alle anderen (suchbaren) Apps, die nicht auf der Startseite enthalten sind, finden Sie über die Suchleiste ([2434549](https://me.sap.com/notes/2434549)).Wenn Sie die Startseite personalisieren und versteckte Apps hinzufügen möchten, wechseln Sie in Ihr Benutzerprofil und wählen Sie App Finder. |

| Prozessschritt | Anwendungsrolle | Vorgang/App | Erwartete Ergebnisse |
| --- | --- | --- | --- |
| [MM-Periode schließen und neue Buchungsperiode öffnen](#unique_6) [Seite ] 5 | Stammdatenexperte – Produktdaten | Perioden abschließen(MMPV) | Die Buchungsperiode ist aktuell. |

## Testverfahren

In diesem Abschnitt werden die Testverfahren für den jeweiligen Prozessschritt beschrieben, der zum betreffenden Umfangsbestandteil gehört.

### MM-Periode schließen und neue Buchungsperiode öffnen

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
| 1. | Anmelden | Melden Sie sich am SAP Fiori Launchpad als Stammdatenexperte – Produktdaten an. | Das SAP Fiori Launchpad wird angezeigt. |  |
| 2 | SAP-Fiori-App aufrufen | Öffnen Sie Perioden abschließen(MMPV).Hinweis Wenn die Kachel Perioden verschieben nicht sichtbar ist, wählen Sie Kachelkatalog in der Dropdown-Liste rechts oben auf dem Fiori-Launchpad. Wählen Sie in der Gruppe Stammdaten - Verwaltung die Kachel Perioden verschieben aus und fügen Sie sie der Gruppe Meine Startseite hinzu. | Die App wird geöffnet. |  |
| 3 | Selektionsdaten eingeben | Geben Sie auf dem Bild Periodenverschiebung Materialstamm die folgenden Daten ein:Buchungskreis von: <Ihr Buchungskreis>Buchungskreis bis: <Ihr Buchungskreis>Zeitraum: <zu öffnende Periode>Geschäftsjahr: <laufendes Geschäftsjahr>Prüfen und verschieben: markiertHinweis Geben Sie im Feld Periode zwei Ziffern für den Monat ein. Beispiel: Januar ist gleich 01, Oktober ist gleich 10 usw.Wenn Sie also die laufende Periode öffnen möchten, geben Sie in den nächsten Perioden den aktuellen Monat ein. |  |  |
| 4 | "Ausführen" wählen | Wählen Sie auf dem Bild Periodenverschiebung Materialstamm die Option Ausführen. |  |  |
| 5 | Ergebnis prüfen | Wenn ein Protokoll die Meldung Der Verwaltungssatz hat als aktuelle Periode (Monat/Jahr): <Ihre Eingaben zu Periode/Jahr> anzeigt, ist der Vorgang abgeschlossen.Hinweis Falls die Buchungsperiode noch in der Vergangenheit liegt, wiederholen Sie die oben genannten Schritte periodenweise, bis Sie zur richtigen (aktuellen) Periode gelangen. Wenn die angezeigte Periode 04 2014 ist und Sie die Periode 12 2015 öffnen möchten, ist dies nicht auf direktem Wege möglich. Sie müssen zunächst Periode 05 2014, dann 06 2014 usw. aufrufen, bis Sie die aktuelle Periode erreicht haben. Wenn Sie die Bestandsperioden aus dem vergangenen Jahr verschieben möchten, wird unter Umständen in Schritt 3 eine Systemmeldung angezeigt, die besagt, dass Sie eine Periode aus dem vergangenen Jahr öffnen/schließen. Sie müssen diese Meldung bestätigen. | Die Buchungsperiode ist aktuell. |  |

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
- related-to :: [[11-inventory-warehouse-and-transportation/crear-nuevo-periodo-contable-mm-abierto-mds-bnz-696]]
- related-to :: [[11-inventory-warehouse-and-transportation/create-new-open-mm-posting-period-mds-bnz-695]]
- related-to :: [[11-inventory-warehouse-and-transportation/criar-periodo-contabil-mm-aberto-mds-bnz-698]]
- related-to :: [[11-inventory-warehouse-and-transportation/mds-bnz-699]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/BNZ_S4CLD2608_Master_Data_DE_XX.docx` — full document · extracted with `mammoth` · 9,181 chars in the whole document
