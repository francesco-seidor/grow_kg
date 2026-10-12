---
id: 06-management-accounting/leistungsart-und-leistungsartenhierarchie-anlegen-sds-bnn-640
title: Leistungsart und Leistungsartenhierarchie anlegen – SDS (BNN) (BNN_S4CLD2608_Master_Data_DE_XX)
description: "German SAP S/4HANA Cloud 2608 master data script (BNN): activity types and activity type hierarchies, change log and where-used analyses. Gemeinkostencontroller."
cluster: 06-management-accounting
tags: [kb/management-accounting, topic/activity-types]
aliases: [BNN_S4CLD2608_Master_Data_DE_XX]
keywords: [Activity Types and Activity Type Hierarchies, activity types, activity type hierarchies, master data scripts, activity type change log, where-used analysis, controlling area, secondary cost elements, cost center planning, BNN]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/BNN_S4CLD2608_Master_Data_DE_XX.docx]
confidence: high
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-640
topic: 06-management-accounting/activity-types
language: DE
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Leistungsart und Leistungsartenhierarchie anlegen – SDS (BNN) (BNN_S4CLD2608_Master_Data_DE_XX)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/BNN_S4CLD2608_Master_Data_DE_XX.docx`, extracted with `mammoth`. Grouped under **Activity Types and Activity Type Hierarchies** in Management Accounting. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

| <!-- image omitted: unnamed --> | StammdatenskriptSAP S/4HANA Cloud Public Edition - 02-07-26 |
| --- | --- |
|  | Leistungsart und Leistungsartenhierarchie anlegen – SDS (BNN) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Inhaltsverzeichnis

[1 Verwendungszweck 2](#_Toc233890000)

[2 Voraussetzungen 3](#_Toc233890001)

[2.1 Systemzugriff 3](#_Toc233890002)

[2.2 Rollen 3](#_Toc233890003)

[2.3 Erforderliche Organisationseinheiten 3](#_Toc233890004)

[2.4 Obligatorische und optionale Stammdaten 4](#_Toc233890005)

[2.5 Wesentliche Parameter für die Datenerstellung 4](#_Toc233890006)

[2.6 Vorbereitende Schritte 4](#_Toc233890007)

[2.6.1 Benutzereinstellungen – Kostenrechnungskreis setzen 4](#_Toc233890008)

[3 Übersichtstabelle 6](#_Toc233890009)

[4 Testverfahren 7](#_Toc233890010)

[4.1 Leistungsartenstammdaten anlegen 7](#_Toc233890011)

[4.2 Leistungsartenhierarchie-Stammdaten anlegen 8](#_Toc233890012)

[4.3 Analysen 9](#_Toc233890013)

[4.3.1 Leistungsarten-Änderungsprotokoll 9](#_Toc233890014)

[4.3.2 Verwendungsnachweis – Leistungsarten 10](#_Toc233890015)

## Verwendungszweck

Leistungsarten repräsentieren die erstellten Leistungen einer Kostenstelle innerhalb eines Kostenrechnungskreises. Leistungsarten werden verwendet, um Leistungen zu planen und zuzuweisen, die in Leistungseinheiten erfasst wurden. Die Bewertung der Leistungsmenge erfolgt mit einem Tarif, der in der Kostenstelle hinterlegt ist.

Leistungsarten werden folgendermaßen verwendet:

Zur Bestimmung des mengenmäßigen Outputs einer Kostenstelle. Die Planleistungsmengen von Fertigungs- und Hilfskostenstellen müssen abgestimmt werden, insbesondere mit dem Masterproduktionsplan der Logistik. Damit wird die erforderliche Planleistungsmenge sowie die geplante Kapazität bestimmt.

Zur Kontrolle der Leistungsmengen in den Kostenstellen. Dies ermöglicht die Messung des Beschäftigungs- oder Nutzungsgrads einer Kostenstelle.

Neben der manuellen Planung von Leistungsmengen steht Ihnen die indirekte Leistungsverrechnung für die automatische Planung von Leistungsmengen zur Verfügung.

Leistungsartenhierarchien sind auch bei der Planung hilfreich. Da es kein Tool für die Mehrfachselektion von Leistungsarten gibt, können Leistungen in Leistungsartenhierarchien gesammelt werden, um die Planung mehrerer Leistungsarten in einem Schritt zu ermöglichen.

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
| Gemeinkostencontroller | SAP_BR_OVERHEAD_ACCOUNTANT | Gemeinkostenrechnung | SAP_BR_OVERHEAD_ACCOUNTANT |  |

### Erforderliche Organisationseinheiten

Die Organisationsstruktur und die Stammdaten Ihres Unternehmens wurden bei der Implementierung in Ihrem ERP-System angelegt. Die Organisationsstruktur gibt den Aufbau Ihres Unternehmens wieder. Die Stammdaten stehen für Leistungsarten und Leistungsartenhierarchien, je nach betrieblichem Schwerpunkt Ihres Unternehmens.

| Datenobjekt | Verwendet im Datensegment | Obligatorisch / optional | Kommentare |
| --- | --- | --- | --- |
| Kostenrechnungskreis | Allgemeine Daten | Obligatorisch |  |

### Obligatorische und optionale Stammdaten

Vorschlagswerte

Die Organisationsstruktur und die Stammdaten Ihres Unternehmens wurden bei der Implementierung in Ihrem ERP-System angelegt. Die Organisationsstruktur gibt den Aufbau Ihres Unternehmens wieder. Die Stammdaten hängen vom betrieblichen Schwerpunkt Ihres Unternehmens ab.

Der Geschäftsprozess wird mit diesen organisationsspezifischen Stammdaten aktiviert. Der nächste Abschnitt enthält Beispiele hierzu.

Leistungsarten- und Leistungsartenhierarchiesätze verweisen unter Umständen auf andere Stammdaten. Die folgende Tabelle bietet eine Übersicht über die optionalen und obligatorischen Stammdatenobjekte, die in einem Leistungsartendatensatz enthalten sein müssen.

| Stammdatenobjekt | Verwendet im Datensegment | Obligatorisch / optional | Kommentare |
| --- | --- | --- | --- |
| Kostenart | Allgemeine Daten | obligatorisch | Sekundärkostenart (Kostenartentyp '43') |
| Sachkonto |  | Obligatorisch | Für Sekundärkostenart (Kostenartentyp '43') |

### Wesentliche Parameter für die Datenerstellung

Dieser Umfangsbestandteil hat keine Voraussetzungen.

### Vorbereitende Schritte

#### Benutzereinstellungen – Kostenrechnungskreis setzen

| Schrittnummer | Schrittname | Anweisungen | Erwartetes Ergebnis | Bestanden/Nicht bestanden/Anmerkung |
| --- | --- | --- | --- | --- |
| 1 | Am SAP Fiori Launchpad anmelden | Melden Sie sich am SAP Fiori Launchpad als Gemeinkostencontroller an. | Das SAP Fiori Launchpad wird angezeigt. |  |
| 2 | Einstellungen wählen | Wählen Sie im Kontextmenü den Eintrag Einstellungen. | Das Dialogfenster Benutzereinstellungen wird angezeigt. |  |
| 3 | Standardwerte wählen | Wählen Sie im Dialogfenster Vorschlagswerte aus. | Das Fenster Vorschlagswerte wird geöffnet. |  |
| 4 | Daten eingeben | Geben Sie im Feld Kostenrechnungskreis <Kostenrechnungskreiswert> ein, und wählen Sie Sichern. | Für Ihren Benutzer wird z. B. der Kostenrechnungskreis A000 gesetzt. |  |

## Übersichtstabelle

Dieser Umfangsbestandteil umfasst die verschiedenen Prozessschritte in der folgenden Tabelle:

|  |
| --- |
| Hinweis Wenn Ihr Systemadministrator Bereiche und Seiten auf dem SAP Fiori Launchpad aktiviert hat, enthält die Startseite nur die wesentlichen Apps, mit denen die typischen Aufgaben einer Benutzerrolle ausgeführt werden können.Alle anderen (suchbaren) Apps, die nicht auf der Startseite enthalten sind, finden Sie über die Suchleiste ([2434549](https://me.sap.com/notes/2434549)).Wenn Sie die Startseite personalisieren und versteckte Apps hinzufügen möchten, wechseln Sie in Ihr Benutzerprofil und wählen Sie App Finder. |

| Prozessschritt | Anwendungsrolle | Transaktion | Erwartete Ergebnisse |
| --- | --- | --- | --- |
| [Leistungsartenstammdaten anlegen](#unique_10) [Seite ] 7 | Gemeinkostencontroller | Leistungsarten verwalten(F1605A) | Leistungsarten können gemäß neuen geschäftlichen Anforderungen angelegt werden. |
| [Leistungsartenhierarchie-Stammdaten anlegen](#unique_11) [Seite ] 8 | Gemeinkostencontroller | Globale Hierarchien verwalten(F2918) | Leistungsartenhierarchien können gemäß neuen geschäftlichen Anforderungen angelegt werden. |
| [Leistungsarten-Änderungsprotokoll](#unique_12) [Seite ] 9 | Gemeinkostencontroller | Änderungsprotokoll - Leistungsarten(F3866) |  |
| [Verwendungsnachweis – Leistungsarten](#unique_13) [Seite ] 10 | Gemeinkostencontroller | Leistungsarten verwalten (Version 2)(F1605A) |  |

## Testverfahren

In diesem Abschnitt werden die Abläufe für jeden Prozessschritt beschrieben, der zu diesem Umfangsbestandteil gehört. Sie können diese Abläufe auch zum Testen der Stammdatenerzeugung verwenden.

### Leistungsartenstammdaten anlegen

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
| 1 | Anmelden | Melden Sie sich am SAP Fiori Launchpad als Gemeinkostencontroller an. | Das SAP Fiori Launchpad wird angezeigt. |  |
| 2 | SAP-Fiori-App aufrufen | Öffnen Sie Leistungsarten verwalten(F1605A). | Die App wird geöffnet. |  |
| 3 | "Anlegen" wählen | Wählen Sie Anlegen. |  |  |
| 4 | Daten der Leistungsart eingeben | Geben Sie auf dem Bild Neue Leistungsart: Neu auf der Registerkarte Allgemeine Daten folgende Daten ein:Geben Sie eine Leistungsart ein: BeschreibungstextLeistungseinheit: <Leistungseinheit>Name: <Name>Beschreibung Leistungsart: <Geben Sie eine Beschreibung ein.>Gültig ab: <aktuelles Datum>Gültig bis: <Jahresenddatum>Kostenstellenart: <Kostenstellenart>Leistungsartentyp: <Leistungsartentyp>Verrechnungskostenart: z.B. 94304000Preiskennzeichen: <Preiskennzeichen>: | Der Abschnitt Allgemeine Daten und verschiedene Registerkarten werden angezeigt.Hinweis Im Folgenden finden Sie die von SAP empfohlenen Werte für SAP S/4HANA Cloud Public Edition (da andere, obwohl sichtbar, möglicherweise nicht unterstützt werden):Leistungsartentyp: Nur 1 (manueller Eintrag und manuelle Zuordnung) wird unterstützt.Tarifkennzeichen: Nur 3 (manuell festgelegter Preis) wird unterstützt.Leistungsartentyp Ist: sollte leer sein.Tarifkennzeichen Ist: sollte standardmäßig leer sein. Nur wenn Sie den Umfangsbestandteil 33Q – Istkalkulation aktiviert haben, sollten Sie 5 oder 7 verwenden (Details zu diesen beiden Werten finden Sie im Abschnitt im Testskript von 33Q). |  |
| 5 | Daten sichern | Wählen Sie Anlegen. | Die Leistungsart wird angelegt und gesichert. |  |

### Leistungsartenhierarchie-Stammdaten anlegen

Testverwaltung

Kundenprojekt: Füllen Sie die projektbezogenen Teile aus.

|  |  |  |  |
| --- | --- | --- | --- |
| Testfall-ID | <X.XX> | Testdatum: |  |
| Testername: |  | Dauer: |  |
| Benutzerrolle(n): |  | Zuständigkeit: | <Geben Sie den Serviceanbieter, einen Kunden oder einen Serviceanbieter zusammen mit einem Kunden an.> |

Voraussetzung

Sie haben die Grunddaten für das Material, wie in [Leistungsartenstammdaten anlegen](#unique_10) [Seite ] 7 beschrieben, eingetragen und gesichert.

Vorgehensweise

| Testschrittnummer | Bezeichnung des Testschritts | Anweisung | Erwartetes Ergebnis | Kommentare |
| --- | --- | --- | --- | --- |
| 1 | Anmelden | Melden Sie sich am SAP Fiori Launchpad als Gemeinkostencontroller an. | Das SAP Fiori Launchpad wird angezeigt. |  |
| 2 | SAP-Fiori-App aufrufen | Öffnen Sie Globale Hierarchien verwalten(F2918). | Die App wird geöffnet. |  |
| 3 | "Anlegen" wählen | Wählen Sie im Abschnitt Hierarchieliste die Option Anlegen. | Das Bild Neue Hierarchie wird angezeigt. |  |
| 4 | Neue Leistungsartenhierarchie eingeben | Geben Sie auf dem Bild Neue Hierarchie folgende Daten ein, und wählen Sie Anlegen:Typ: LeistungsartenhierarchieHierarchie-ID: <beliebige ID mit bis zu 10 Zeichen>Achtung Die Gesamtlänge von Hierarchie-ID und Knoten-ID darf 14 Zeichen nicht überschreiten.Kostenrechnungskreis: A000Hierarchiebeschreibung: <beliebige Beschreibung> |  |  |
| 5 | Neue Leistungsartenhierarchie bearbeiten | Wählen Sie auf dem Bild Hierarchieliste das Detailsymbol >, und wählen Sie für die neu angelegte Leistungsartenhierarchie Bearbeiten.Markieren Sie die neu angelegte Leistungsartenhierarchie, wählen Sie das Symbol Mehr auf der rechten Seite des Bildes, und wählen Sie Schnellerfassung.Wählen Sie auf dem Bild Schnellerfassung die Option Leistungsart, und geben Sie folgende Daten ein:ID: <Wählen Sie die Leistungsart(en) aus, die Sie über die Suchfunktion hinzufügen möchten.>Wählen Sie OK, wenn Sie fertig sind, und wählen Sie Sichern.Kehren Sie zum Bild Leistungsartenhierarchie zurück, und wählen Sie Aktivieren. | Die neu angelegte Leistungsartenhierarchie ist nun aktiviert. |  |

### Analysen

#### Leistungsarten-Änderungsprotokoll

Testverwaltung

Kundenprojekt: Füllen Sie die projektbezogenen Teile aus.

|  |  |  |  |
| --- | --- | --- | --- |
| Testfall-ID | <X.XX> | Testdatum: |  |
| Testername: |  | Dauer: |  |
| Benutzerrolle(n): |  | Zuständigkeit: | <Geben Sie den Serviceanbieter, einen Kunden oder einen Serviceanbieter zusammen mit einem Kunden an.> |

Zweck

In dieser Aktivität führen Sie das Änderungsprotokoll für Leistungsarten aus.

Vorgehensweise

| Testschrittnummer | Bezeichnung des Testschritts | Anweisung | Erwartetes Ergebnis | Kommentare |
| --- | --- | --- | --- | --- |
| 1 | Anmelden | Melden Sie sich am SAP Fiori Launchpad als Gemeinkostencontroller an. | Das SAP Fiori Launchpad wird angezeigt. |  |
| 2 | SAP-Fiori-App aufrufen | Öffnen Sie Änderungsprotokoll - Leistungsarten(F3866). | Das Dialogfenster Änderungsprotokoll – Leistungsarten wird angezeigt. |  |
| 3 | Selektionskriterien | Nehmen Sie folgende Einträge vor:Leistungsart: <jegliche Leistungsart> |  |  |
| 4 | Auswählen | Wählen Sie Start. | Ein Bericht mit der Änderungsdetailhistorie wird angezeigt. |  |

#### Verwendungsnachweis – Leistungsarten

Testverwaltung

Kundenprojekt: Füllen Sie die projektbezogenen Teile aus.

|  |  |  |  |
| --- | --- | --- | --- |
| Testfall-ID | <X.XX> | Testdatum: |  |
| Testername: |  | Dauer: |  |
| Benutzerrolle(n): |  | Zuständigkeit: | <Geben Sie den Serviceanbieter, einen Kunden oder einen Serviceanbieter zusammen mit einem Kunden an.> |

Zweck

In dieser Aktivität können Sie sehen, wo die Leistungsarten in anderen Stammdaten wie Profitcenter und Istkostenverteilung verwendet werden.

Vorgehensweise

| Testschrittnummer | Bezeichnung des Testschritts | Anweisung | Erwartetes Ergebnis | Kommentare |
| --- | --- | --- | --- | --- |
| 1 | Anmelden | Melden Sie sich am SAP Fiori Launchpad als Gemeinkostencontroller an. | Das SAP Fiori Launchpad wird angezeigt. |  |
| 2 | SAP-Fiori-App aufrufen | Öffnen Sie Leistungsarten verwalten (Version 2)(F1605A). | Die App wird geöffnet. |  |
| 3 | Selektionskriterien | Nehmen Sie folgende Einträge vor:Leistungsart: <jegliche Leistungsart> |  |  |
| 4 | Verwendungsnachweis | Markieren Sie die gewünschte Kostenstelle, und wählen Sie VerwNachweis – Leistungsart. | Ein Bericht wird angezeigt, dem zu entnehmen ist, wo gegenwärtig Leistungsarten verwendet werden. Für Details können Sie den Stammdaten-Objekttyp auswählen und weitere Informationen anzeigen. |  |

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
- related-to :: [[06-management-accounting/criar-tipo-de-atividade-e-hierarquia-de-tipo-de-atividade-mds-bnn-644]]
- related-to :: [[06-management-accounting/master-data-script-create-activity-type-and-activity-type-hierarchy-bn]]
- related-to :: [[06-management-accounting/mds-bnn-643]]
- related-to :: [[06-management-accounting/mds-bnn-645]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/BNN_S4CLD2608_Master_Data_DE_XX.docx` — full document · extracted with `mammoth` · 17,333 chars in the whole document
