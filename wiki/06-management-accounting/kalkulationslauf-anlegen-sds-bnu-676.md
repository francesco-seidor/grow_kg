---
id: 06-management-accounting/kalkulationslauf-anlegen-sds-bnu-676
title: Kalkulationslauf anlegen – SDS (BNU) (BNU_S4CLD2608_Master_Data_DE_XX)
description: "German master data test script (BNU) for SAP S/4HANA Cloud Public Edition 2608: creating and executing a product costing run (F1865) as a prerequisite for logistics scenarios."
cluster: 06-management-accounting
tags: [kb/management-accounting, topic/product-costing-and-standard-cost-updates]
aliases: [BNU_S4CLD2608_Master_Data_DE_XX]
keywords: [Product Costing Runs and Standard Cost Updates, costing run, costing run execution, product cost planning, master data scripts, costing variant, business roles, organizational units, material price update, BNU]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/BNU_S4CLD2608_Master_Data_DE_XX.docx]
confidence: high
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-676
topic: 06-management-accounting/product-costing-and-standard-cost-updates
language: DE
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Kalkulationslauf anlegen – SDS (BNU) (BNU_S4CLD2608_Master_Data_DE_XX)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/BNU_S4CLD2608_Master_Data_DE_XX.docx`, extracted with `mammoth`. Grouped under **Product Costing Runs and Standard Cost Updates** in Management Accounting. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

| <!-- image omitted: unnamed --> | StammdatenskriptSAP S/4HANA Cloud Public Edition - 02-07-26 |
| --- | --- |
|  | Kalkulationslauf anlegen – SDS (BNU) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Inhaltsverzeichnis

[1 Verwendungszweck 2](#_Toc233890047)

[2 Voraussetzungen 3](#_Toc233890048)

[2.1 Systemzugriff 3](#_Toc233890049)

[2.2 Rollen 3](#_Toc233890050)

[2.3 Erforderliche Organisationseinheiten 3](#_Toc233890051)

[2.4 Obligatorische und optionale Stammdaten 4](#_Toc233890052)

[2.5 Wesentliche Parameter für die Datenerstellung 4](#_Toc233890053)

[2.5.1 Kalkulationsvariante 4](#_Toc233890054)

[3 Übersichtstabelle 6](#_Toc233890055)

[4 Testverfahren 7](#_Toc233890056)

[4.1 Kalkulationslauf anlegen 7](#_Toc233890057)

[4.2 Kalkulationslauf ausführen 8](#_Toc233890058)

## Verwendungszweck

Dieses Dokument enthält Prozessschritte, die als Voraussetzung ausgeführt werden müssen, bevor Sie mit der Durcharbeitung der Standardtestskripts der ausgewählten Logistikszenarien beginnen können.

In diesem Dokument finden Sie eine Beschreibung zum Anlegen und Ausführen eines Erzeugniskalkulationslaufs für in Ihrem Unternehmen oder Werk verwendeten Materialien. Der Zweck ist das Planen von Kosten für Materialien ohne eine Referenz auf Aufträge und das Festlegen von Preisen für Materialien und andere Kostenrechnungsobjekte.

Sie können die Produktkostenplanung verwenden, um die Kosten Ihrer Unternehmenserzeugnisse zu analysieren, z.B.:

- Gefertigte Materialien
- Services
- Andere immaterielle Güter

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
| Bestandscontroller | SAP_BR_INVENTORY_ACCOUNTANT | Vorratsbuchhaltung | SAP_BR_INVENTORY_ACCOUNTANT |  |

### Erforderliche Organisationseinheiten

Um einen Kalkulationslauf anzulegen, müssen Sie den Kostenrechnungskreis und den Buchungskreis angeben.

|  |
| --- |
| Hinweis Geben Sie in der Spalte Zu verwendende Organisationseinheit Ihren Wert für das Datensegment ein, das für Ihre Systemumgebung relevant ist. Für Buchungskreis: z.B. 10 = Deutschland, 17 = USA |

| Datensegment | Hängt ab von | Feldbeispiele | Kommentare | Zu verwendende Organisationseinheit |
| --- | --- | --- | --- | --- |
| Kalkulationsdaten | Kostenrechnungskreis |  |  | Kostenrechnungskreis:____________ |
|  | Buchungskreis |  |  | Buchungskreis:__________ |
| Auswahl | Werk |  |  | Werk:__________ |

### Obligatorische und optionale Stammdaten

Stücklistendatensätze können auf andere Stammdaten verweisen. Die folgende Tabelle stellt eine Übersicht optionaler und obligatorischer Stammdatenobjekte bereit, die in einer Stückliste verwendet werden müssen.

| Stammdatenobjekt | Verwendet im Datensegment | Obligatorisch / optional | Kommentare |
| --- | --- | --- | --- |
| Materialien | Kalkulation anlegen > Ablaufschritt > Auswahl | Obligatorisch | Für gewöhnlich geben Sie die Materialarten an, um anzuzeigen, für welche Materialien der Kalkulationslauf eine Erzeugniskalkulation erzeugen soll. |
| Fertigungsstammdaten (Stückliste, Arbeitsplan, Arbeitsplatz usw.). | Unter Kalkulation anlegen--> Ablaufschritt --> Strukturauflösung | Optional (oder) obligatorisch | Wenn gefertigte Produkte im Kalkulationslauf verwendet werden (z.B. Produkte mit Materialart "FERT" (Fertigerzeugnisse) oder "HALB" (Halbfabrikate), verfügen diese Produkte über eine Stückliste, die im Kalkulationslauf "aufgelöst" wird.Gleichzeitig werden die Arbeitspläne ausgewählt. Zusatzdaten aus Arbeitsplätzen, zugeordnete Kostenstellen und verwendete Leistungsarten sowie Kostensätze werden ermittelt, um die endgültigen Kalkulationsdaten zu ermitteln. |

### Wesentliche Parameter für die Datenerstellung

In diesem Abschnitt werden einige Basisparameter erläutert, die das Verhalten eines Stammsatzes beeinflussen und zum Anlegen einer Stückliste immer erforderlich sind:

#### Kalkulationsvariante

Eine Kalkulationsvariante definiert eine Verknüpfung zwischen der Anwendung und dem Customizing, da alle Kalkulationen mit einer Referenz auf eine Kalkulationsvariante ausgeführt und gesichert werden.

| Kalkulationsvariante | Beschreibung | Anmerkung |
| --- | --- | --- |
| PYC1 | Kalkulation Standard | Diese Kalkulationsvariante wird verwendet, um für die selektierten Materialien Standard-Erzeugniskalkulationen anzulegen. Auf der Grundlage des Ergebnisses werden die Materialbewertungsdaten aktualisiert. |

## Übersichtstabelle

Dieser Umfangsbestandteil umfasst die Prozessschritte, die in der folgenden Tabelle aufgeführt werden:

|  |
| --- |
| Hinweis Wenn Ihr Systemadministrator Bereiche und Seiten auf dem SAP Fiori Launchpad aktiviert hat, enthält die Startseite nur die wesentlichen Apps, mit denen die typischen Aufgaben einer Benutzerrolle ausgeführt werden können.Alle anderen (suchbaren) Apps, die nicht auf der Startseite enthalten sind, finden Sie über die Suchleiste ([2434549](https://me.sap.com/notes/2434549)).Wenn Sie die Startseite personalisieren und versteckte Apps hinzufügen möchten, wechseln Sie in Ihr Benutzerprofil und wählen Sie App Finder. |

| Prozessschritt | Benutzerrolle | Transaktion/App-Name | Erwartete Ergebnisse |
| --- | --- | --- | --- |
| [Kalkulationslauf anlegen](#unique_10) [Seite ] 7 | Bestandscontroller | Kalkulationsläufe verwalten - Plankosten(F1865) | Kopfdaten mit Registerkarte "Kalkulationsdaten" werden angezeigt. |
| [Kalkulationslauf ausführen](#unique_11) [Seite ] 8 | Bestandscontroller | Kalkulationsläufe verwalten - Plankosten(F1865) |  |

## Testverfahren

In diesem Abschnitt werden die Testverfahren für den jeweiligen Prozessschritt beschrieben, der zum betreffenden Umfangsbestandteil gehört.

### Kalkulationslauf anlegen

Testverwaltung

Kundenprojekt: Füllen Sie die projektbezogenen Teile aus.

|  |  |  |  |
| --- | --- | --- | --- |
| Testfall-ID | <X.XX> | Testdatum: |  |
| Testername: |  | Dauer: |  |
| Benutzerrolle(n): |  | Zuständigkeit: | <Geben Sie den Serviceanbieter, einen Kunden oder einen Serviceanbieter zusammen mit einem Kunden an.> |

Zweck

In dieser Aktivität legen Sie einen Kalkulationslauf an.

Vorgehensweise

| Testschrittnummer | Bezeichnung des Testschritts | Anweisungen | Erwartetes Ergebnis | Bestanden/Nicht bestanden/Anmerkung |
| --- | --- | --- | --- | --- |
| 1 | Anmeldung | Melden Sie sich als Bestandscontroller am SAP Fiori Launchpad an. | Das SAP Fiori Launchpad wird angezeigt. |  |
| 2 | SAP-Fiori-App aufrufen | Öffnen Sie Kalkulationsläufe verwalten - Plankosten(F1865). | Die Sicht Kalkulationsläufe verwalten - Plankosten wird angezeigt. |  |
| 3 | Kalkulationslauf anlegen | Wählen Sie Anlegen. | Die Sicht Neuen Kalkulationslauf anlegen wird angezeigt. |  |
| 4 | Parameter für den Kalkulationslauf erfassen | Geben Sie folgende Daten ein, und wählen Sie Enter:Kalkulationslauf: Test1KalkLaufDatum: <Geben Sie das aktuelle Datum ein.>Beschreibung: Kalkulationslauf Test1Kalkulationsvariante: PYC1Kalkulationsversion: 1Kostenrechnungskreis: A000Buchungskreis: 1010Kalkulationsdatum von: <Aktuelles Datum>Kalkulationsdatum bis: Übernehmen Sie den Vorschlagswert.Auflösungstermin: <Aktuelles Datum>Bewertungsdatum: <Aktuelles Datum> |  |  |
| 5 | Kalkulationslauf sichern | Wählen Sie Sichern. |  |  |

### Kalkulationslauf ausführen

Testverwaltung

Kundenprojekt: Füllen Sie die projektbezogenen Teile aus.

|  |  |  |  |
| --- | --- | --- | --- |
| Testfall-ID | <X.XX> | Testdatum: |  |
| Testername: |  | Dauer: |  |
| Benutzerrolle(n): |  | Zuständigkeit: | <Geben Sie den Serviceanbieter, einen Kunden oder einen Serviceanbieter zusammen mit einem Kunden an.> |

Zweck

In dieser Aktivität führen Sie den Kalkulationslauf aus. Es sind keine konfigurierten Materialien enthalten.

Vorgehensweise

| Testschrittnummer | Bezeichnung des Testschritts | Anweisungen | Erwartetes Ergebnis | Bestanden/Nicht bestanden/Anmerkung |
| --- | --- | --- | --- | --- |
| 1 | Anmeldung | Melden Sie sich am SAP Fiori Launchpad als Bestandscontroller an. | Das SAP Fiori Launchpad wird angezeigt. |  |
| 2 | SAP-Fiori-App aufrufen | Öffnen Sie Kalkulationsläufe verwalten - Plankosten(F1865). | Die Sicht Kalkulationsläufe verwalten - Plankosten wird angezeigt. |  |
| 3 | Kalkulationslauf auswählen | Suchen Sie den im vorigen Schritt angelegten Kalkulationslauf, klicken Sie auf den Eintrag, und wählen Sie Bearbeiten aus, um auf die Detailinformationen des Kalkulationslaufs zuzugreifen. |  |  |
| 4 | Kalkulationslauf öffnen | Geben Sie folgende Daten ein:Kalkulationslauf: Geben Sie den im vorigen Schritt angelegten Kalkulationslauf ein, und wählen Sie Enter.Expandieren Sie den Abschnitt Verarbeitung. |  |  |
| 5 | Kalkulationen anlegen | In der Tabelle Verarbeitung finden Sie in der Spalte Parameter für jede Zeile die Drucktaste Parameter ändern. Wählen Sie den entsprechenden Eintrag in der Selektionszeile, und geben Sie folgende Daten ein:Materialart: HALB, ROH, FERTWerk: 1010Entmarkieren Sie Hintergrundverarbeitung, und wählen Sie die Option EXPLO.Sichern Sie Ihre Einträge, und wählen Sie Zurück.Wählen Sie in der Spalte Ausführen die Funktion Ausführen. Die Statusanzeige für die Zeile "Selektion" wechselt auf Grün. | Die Selektion wird ausgeführt. |  |
| 6 | Kalkulationen anlegen | Wählen Sie in der Zeile Kalkulation die Drucktaste Parameter ändern. Entfernen Sie auf dem Bild Kalkulationslauf: Kalkulation - Parameter ändern das Kennzeichen Hintergrundverarbeitung, und wählen Sie dann Sichern.Wählen Sie Zurück.Wählen Sie in der Spalte Ausführen die Funktion Ausführen. Die Statusanzeige für die Zeile "Kostenkalkulation" wechselt auf Grün. | Der Kalkulationslauf wird ausgeführt. |  |
| 7 | Kalkulationen anlegen | Wählen Sie im Menü die Option Bearbeiten > Kalkulationsergebnisse.Wenn die Statusanzeige für diese Zeile auf Rot steht, prüfen Sie den Report "Kalkulationsstufen". Korrigieren Sie die Fehler im Report. Um den Kalkulationslauf (bei Bedarf) erneut durchzuführen, wiederholen Sie die Schritte für die Struktur auflösung und die Kalkulationszeilen. | Der Kalkulationslauf wird ausgeführt. |  |
| 8 | Kalkulationen anlegen | Wählen Sie in der Zeile Analyse die Drucktaste Parameter ändern. Geben Sie für den Parameter den Wert SAP&11 ein. Entfernen Sie auf dem Bild Kalkulationslauf: Analyse - Parameter ändern das Kennzeichen Hintergrundverarbeitung, und wählen Sie dann Sichern.Wählen Sie Zurück.Wählen Sie in der Spalte Ausführen die Funktion Ausführen. | Der Kalkulationslauf wird ausgeführt. |  |
| 9 | Kalkulationen anlegen | Wählen Sie in der Zeile Marketing die Drucktaste zum Sperren.Wählen Sie im Bild Preisfortschreibung: organisatorische Maßnahme den Buchungskreis: 1010.Geben Sie im angezeigten Dialogfenster die Kalkulationsvariante PYC1 und die Kalkulationsversion 1 ein, und wählen Sie anschließend Enter. Die Statusanzeige für die Zeile wechselt zu Grün.Wählen Sie Zurück.Wählen Sie Parameter ändern, und entmarkieren Sie Hintergrundverarbeitung.Wählen Sie Sichern.Wählen Sie Zurück und anschließend Ausführen. | Der Kalkulationslauf wird ausgeführt. |  |
| 10 | Kalkulationen anlegen | Wählen Sie in der Zeile Freigabe die Option Parameter ändern, und entmarkieren Sie Testlauf und Hintergrundverarbeitung.Wählen Sie Sichern.Wählen Sie Zurück und anschließend Ausführen. | Die aktuellen Preise werden in den Materialstammdaten aktualisiert. |  |

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
- related-to :: [[06-management-accounting/crear-ejecucion-del-calculo-del-coste-mds-bnu-678]]
- related-to :: [[06-management-accounting/criar-execucao-de-calculo-de-custos-mds-bnu-680]]
- related-to :: [[06-management-accounting/master-data-script-create-costing-run-mds-bnu-677]]
- related-to :: [[06-management-accounting/mds-bnu-679]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/BNU_S4CLD2608_Master_Data_DE_XX.docx` — full document · extracted with `mammoth` · 15,122 chars in the whole document
