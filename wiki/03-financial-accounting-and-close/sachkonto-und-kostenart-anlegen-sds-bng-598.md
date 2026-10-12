---
id: 03-financial-accounting-and-close/sachkonto-und-kostenart-anlegen-sds-bng-598
title: Sachkonto und Kostenart anlegen – SDS (BNG) (BNG_S4CLD2608_Master_Data_DE_XX)
description: "German master data script BNG for SAP S/4HANA Cloud Public Edition: creating a G/L account and cost element by copying an existing account via Configure Your Solution or SAP Central Business…"
cluster: 03-financial-accounting-and-close
tags: [kb/financial-accounting-and-close, topic/chart-of-accounts-and-gl-accounts]
aliases: [BNG_S4CLD2608_Master_Data_DE_XX]
keywords: [Chart of Accounts YCOA and G/L Account Creation, g/l account master data, cost element, chart of accounts, account types, account groups, company code assignment, business process configuration, sap central business configuration, open item management]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/BNG_S4CLD2608_Master_Data_DE_XX.docx]
confidence: high
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-598
topic: 03-financial-accounting-and-close/chart-of-accounts-and-gl-accounts
language: DE
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Sachkonto und Kostenart anlegen – SDS (BNG) (BNG_S4CLD2608_Master_Data_DE_XX)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/BNG_S4CLD2608_Master_Data_DE_XX.docx`, extracted with `mammoth`. Grouped under **Chart of Accounts YCOA and G/L Account Creation** in Financial Accounting and Close. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

| <!-- image omitted: unnamed --> | StammdatenskriptSAP S/4HANA Cloud Public Edition - 02-07-26 |
| --- | --- |
|  | Sachkonto und Kostenart anlegen – SDS (BNG) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Inhaltsverzeichnis

[1 Verwendungszweck 2](#_Toc233889955)

[2 Voraussetzungen 3](#_Toc233889956)

[2.1 Systemzugriff 3](#_Toc233889957)

[2.2 Rollen 3](#_Toc233889958)

[2.3 Erforderliche Organisationseinheiten 3](#_Toc233889959)

[2.4 Obligatorische und optionale Stammdaten 4](#_Toc233889960)

[2.5 Wesentliche Parameter für die Datenerstellung 6](#_Toc233889961)

[3 Übersichtstabelle 7](#_Toc233889962)

[4 Testverfahren 8](#_Toc233889963)

[4.1 Sachkonto anlegen 8](#_Toc233889964)

## Verwendungszweck

Ein Sachkontenstammsatz enthält Informationen über das Konto, die steuern, wie Geschäftsvorfälle gebucht und verwaltet werden.

Das Hauptbuch in SAP bietet eine umfassende und vollständig aktuelle Sicht aller Anlagen-, Verbindlichkeits- und Forderungskonten und ist vollständig in die anderen SAP-Module integriert.

Da alle SAP-Module integriert sind, werden einige Sachkontenbuchungen automatisch vom System im Hintergrund erzeugt, z.B. Buchung des WE/RE-Kontos (Wareneingang/Rechnungseingang) und Sachkontenbuchungen von Bestandsbewegungen.

Einige Konten sind „mit Offene-Posten-Verwaltung geführt“. Sie dienen als Verrechnungskonto, so dass einzelne Positionen ausgeglichen werden können, wenn z.B. Ein-/Ausgangszahlungen und Materialien verarbeitet werden.

Andere Konten, z.B. Debitoren- und Kreditorenabstimmkonten können nicht direkt bebucht werden, da es sich lediglich um eine Widerspiegelung der Geschäftspartner in den Nebenbüchern handelt.

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
| Konfigurationsexperte – Geschäftsprozesskonfiguration | SAP_BR_BPC_EXPERT | Geschäftsprozesskonfiguration / Geschäftsprozesskonfiguration - Finance / Geschäftsprozesskonfiguration - Beschaffung / Lösung verwalten / Geschäftsprozesskonfiguration - Workflow / Geschäftskonfiguration - Feature Management / Geschäftsprozesskonfiguration - Extensibility Explorer / Business Configuration - Transportation Management | SAP_BR_BPC_EXPERT / SAP_FIN_SPT_BPC_EXPERT_PC / SAP_MM_SPT_BIZ_PROC_CONFIGN_PC / SAP_CA_SPT_IC_LND_BASE_PC / SAP_CA_SPT_BPC_WORKFLOW_PC / SAP_CA_SPT_BPC_FM_PC / SAP_EI_SPT_BPC_EXT_PC / SAP_TM_SPT_TRANSPCFG_PC |  |

### Erforderliche Organisationseinheiten

Einige Segmente von Debitorenstammdaten hängen von den Organisationseinheiten des Unternehmens ab. Allgemeine (zentrale) Daten hängen nicht von einer Organisationseinheit oder dem Buchungskreis ab. Die folgende Tabelle stellt eine Übersicht dieser verschiedenen Datensegmente und ihrer relevanten Organisationseinheiten bereit:

| Datensegment | Hängt ab von | Feldbeispiele | Kommentare | Zu verwendende Organisationseinheit |
| --- | --- | --- | --- | --- |
| Sachkonto | BuchungskreisKontenplanKostenrechnungskreis | Siehe [Obligatorische und optionale Stammdaten](#unique_6) [Seite ] 4 | Buchungskreisdaten können für jede Buchungskreis-ID Ihrer Unternehmensstruktur vorhanden sein, für die das Sachkonto und der Kostenarten-Stammsatz verwendet werden. | Buchungskreis:____________Kontenplan____________Kostenrechnungskreis____________ |

### Obligatorische und optionale Stammdaten

Debitorenstammdatensätze können auf andere Stammdaten verweisen. Die folgende Tabelle bietet eine Übersicht über die optionalen und obligatorischen Stammdatenobjekte, die in einem Debitorenstammdatensatz enthalten sein müssen.

| Stammdatenobjekt | Verwendet im Datensegment | Obligatorisch / optional | Kommentare |
| --- | --- | --- | --- |
| Kontenplan | Auf dem Sachkonto-UI finden Sie den Eintrag auf der Registerkarte Allgemein im Abschnitt Steuerung. | Obligatorisch |  |
| Sachkonto | Auf dem Sachkonto-UI finden Sie den Eintrag auf dem Bild Konto kopieren. | Obligatorisch |  |
| Beschreibung | Auf dem Sachkonto-UI finden Sie den Eintrag auf dem Bild Konto kopieren. | Obligatorisch |  |
| Kontoart | Auf dem Sachkonto-UI finden Sie den Eintrag auf der Registerkarte Allgemein im Abschnitt Steuerung. | Obligatorisch |  |
| Kontengruppe | Auf dem Sachkonto-UI finden Sie den Eintrag auf der Registerkarte Allgemein im Abschnitt Steuerung. | Obligatorisch |  |
| Funktionsbereich | Auf dem Sachkonto-UI finden Sie den Eintrag auf der Registerkarte Allgemein im Abschnitt Steuerung. | Optional | Verwenden Sie es für GuV-Konten. |
| Sachkontenlangtext | Auf dem Sachkonto-UI finden Sie den Eintrag auf der Registerkarte Allgemein im Abschnitt Beschreibung. | Optional |  |
| Ankreuzfeld "Buchungskreis" | Auf dem Sachkonto-UI finden Sie den Eintrag auf der Registerkarte Allgemein im Abschnitt Definition in Buchungskreis. | Obligatorisch | Ordnen Sie es einem oder mehreren Buchungskreisen zu. |
| Gesperrt zum Anlegen | Auf dem Sachkonto-UI finden Sie den Eintrag auf der Registerkarte Allgemein im Abschnitt Administration. | Optional |  |
| Gesperrt zum Buchen | Auf dem Sachkonto-UI finden Sie den Eintrag auf der Registerkarte Allgemein im Abschnitt Administration. | Optional |  |
| Gesperrt zum Planen | Auf dem Sachkonto-UI finden Sie den Eintrag auf der Registerkarte Allgemein im Abschnitt Administration. | Optional |  |
| Zum Löschen vorgemerkt | Auf dem Sachkonto-UI finden Sie den Eintrag auf der Registerkarte Allgemein im Abschnitt Administration. | Optional |  |
| Kontowährung | Nachdem Sie ein neues Sachkonto angelegt haben, finden Sie die Details des Buchungskreises im Abschnitt Steuerungsdaten > Kontosteuerung. |  |  |
| Nur Saldo in Hauswährung | Nachdem Sie ein neues Sachkonto angelegt haben, finden Sie die Details des Buchungskreises im Abschnitt Steuerungsdaten > Kontosteuerung. | Optional |  |
| Steuerkategorie | Nachdem Sie ein neues Sachkonto angelegt haben, finden Sie die Details des Buchungskreises im Abschnitt Steuerungsdaten > Kontosteuerung. | Optional |  |
| Buchung ohne Steuer erlaubt | Nachdem Sie ein neues Sachkonto angelegt haben, finden Sie die Details des Buchungskreises im Abschnitt Steuerungsdaten > Kontosteuerung. | Optional |  |
| Alternative Kontonummer | Nachdem Sie ein neues Sachkonto angelegt haben, finden Sie die Details des Buchungskreises im Abschnitt Steuerungsdaten > Kontosteuerung. | Optional |  |
| Sortierschlüssel | Nachdem Sie ein neues Sachkonto angelegt haben, finden Sie die Details des Buchungskreises im Abschnitt Steuerungsdaten > Kontoverwaltung. | Optional |  |
| Kostenrechnungskreis | Nachdem Sie ein neues Sachkonto angelegt haben, finden Sie die Details des Buchungskreises im Abschnitt Buchhaltungseinstellungen für Kostenrechnungskreis. | Obligatorisch | Optional für Kontoart Bestandskonto |
| Kostenartentyp | Nachdem Sie ein neues Sachkonto angelegt haben, finden Sie die Details des Buchungskreises im Abschnitt Steuerungsdaten > Buchhaltungseinstellungen für Kostenrechnungskreis. | Obligatorisch | Optional für Kontoart Bestandskonto |
| Datensatzmenge | Nachdem Sie ein neues Sachkonto angelegt haben, finden Sie die Details des Buchungskreises im Abschnitt Steuerungsdaten > Buchhaltungseinstellungen für Kostenrechnungskreis. | Optional |  |
| Feldstatusgruppe | Nachdem Sie ein neues Sachkonto angelegt haben, finden Sie die Details des Buchungskreises im Abschnitt Anlegen/Bank/Zinsen > Steuerung der Belegerstellung. | Optional |  |
| Nur automatisch buchen | Nachdem Sie ein neues Sachkonto angelegt haben, finden Sie die Details des Buchungskreises im Abschnitt Anlegen/Bank/Zinsen > Steuerung der Belegerstellung. | Optional |  |
| Automatische Buchungen nachkontieren | Nachdem Sie ein neues Sachkonto angelegt haben, finden Sie die Details des Buchungskreises im Abschnitt Anlegen/Bank/Zinsen > Steuerung der Belegerstellung. | Optional |  |
| Planungsebene | Nachdem Sie ein neues Sachkonto angelegt haben, finden Sie die Details des Buchungskreises im Abschnitt Anlegen/Bank/Zinsen > Bank-/Finanzangaben. | Optional |  |
| Geldbewegungsrelevant | Nachdem Sie ein neues Sachkonto angelegt haben, finden Sie die Details des Buchungskreises im Abschnitt Anlegen/Bank/Zinsen > Bank-/Finanzangaben. | Optional |  |
| Gesperrt zum Buchen | Nachdem Sie ein neues Sachkonto angelegt haben, finden Sie die Details des Buchungskreises in der Administration. | Optional |  |
| Zum Löschen vorgemerkt | Nachdem Sie ein neues Sachkonto angelegt haben, finden Sie die Details des Buchungskreises in der Administration. | Optional |  |
| Übersetzungstext | Auf dem Sachkonto-UI finden Sie den Eintrag auf der Registerkarte Übersetzung im Abschnitt Sprachenschlüssel. | Optional | Übersetzen Sie die Beschreibungen in die erforderlichen Sprachen. |

### Wesentliche Parameter für die Datenerstellung

In diesem Abschnitt werden einige Basisparameter erläutert, die das Verhalten eines Stammsatzes beeinflussen und zum Anlegen eines Debitorenstammdatensatzes immer erforderlich sind:

Kontoart

- Bestandskonten
- Nicht betriebliche Aufwendungen oder Erträge
- Primäre Kosten oder Umsätze
- Sekundäre Kosten

Kontengruppen

- Abstimmkonto eingabebereit
- Konten des Anlagevermögens
- Erfolgskonten
- Konten für flüssige Mittel
- Konten der Materialwirtschaft
- Sachkonten allgemein

## Übersichtstabelle

Dieser Umfangsbestandteil umfasst die Prozessschritte, die in der folgenden Tabelle aufgeführt werden:

|  |
| --- |
| Hinweis Wenn Ihr Systemadministrator Bereiche und Seiten auf dem SAP Fiori Launchpad aktiviert hat, enthält die Startseite nur die wesentlichen Apps, mit denen die typischen Aufgaben einer Benutzerrolle ausgeführt werden können.Alle anderen (suchbaren) Apps, die nicht auf der Startseite enthalten sind, finden Sie über die Suchleiste ([2434549](https://me.sap.com/notes/2434549)).Wenn Sie die Startseite personalisieren und versteckte Apps hinzufügen möchten, wechseln Sie in Ihr Benutzerprofil und wählen Sie App Finder. |

| Prozessschritt | Benutzerrolle | Vorgang/App | Erwartete Ergebnisse |
| --- | --- | --- | --- |
| [Sachkonto anlegen](#unique_9) [Seite ] 8 | Konfigurationsexperte – Geschäftsprozesskonfiguration | Lösung verwalten(F1241) |  |

## Testverfahren

In diesem Abschnitt werden die Testverfahren für den jeweiligen Prozessschritt beschrieben, der zum betreffenden Umfangsbestandteil gehört.

### Sachkonto anlegen

Testverwaltung

Kundenprojekt: Füllen Sie die projektbezogenen Teile aus.

|  |  |  |  |
| --- | --- | --- | --- |
| Testfall-ID | <X.XX> | Testdatum: |  |
| Testername: |  | Dauer: |  |
| Benutzerrolle(n): |  | Zuständigkeit: | <Geben Sie den Serviceanbieter, einen Kunden oder einen Serviceanbieter zusammen mit einem Kunden an.> |

Zweck

Beim Anlegen neuer Sachkonten ist es ratsam, einen bestehenden Nummernkreis als Referenz für neue Sachkonten zu verwenden.

Vorgehensweise

Wählen Sie abhängig von Ihrer Konfigurationsumgebung für SAP S/4HANA Cloud Public Edition eine der folgenden Optionen:

Lösung konfigurieren:

| Testschrittnummer | Bezeichnung des Testschritts | Anweisung | Erwartetes Ergebnis | Kommentare |
| --- | --- | --- | --- | --- |
| 1 | Anmelden | Melden Sie sich am SAP Fiori Launchpad als Konfigurationsexperte – Geschäftsprozesskonfiguration an. | Das SAP Fiori Launchpad wird angezeigt. |  |
| 2 | SAP-Fiori-App aufrufen | Öffnen Sie Lösung verwalten(F1241). |  |  |
| 3 | Konfiguration aufrufen | Öffnen Sie die App Lösung konfigurieren. | Das Bild Lösung konfigurieren: Realisierungsphase wird angezeigt. |  |
| 4 | Konfiguration aufrufen | Geben Sie Folgendes ein:Anwendungsbereich: FinanzwesenSubanwendungsbereich: General Ledger |  |  |
| 5 | Öffnen | Wählen Sie den Pfeil rechts neben der Spalte mit dem Kontenplan. |  |  |
| 6 | Konfigurationsschritte auswählen | Wählen Sie für den Schritt Sachkontenstammdaten verwalten die Option Konfigurieren. |  |  |
| 7 | Nach Ihrem Konto suchen | Geben Sie Folgendes ein, und wählen Sie Start:Sicht: KontenplansichtKontenplan: YCOA | Das System zeigt eine Liste übereinstimmender Sachkonten an. |  |
| 8 | Sachkonto wählen | Wählen Sie das Sachkonto im Suchergebnis aus.Hinweis Klicken Sie auf den blauen Kontonummernlink. | Das Bild Sachkontenstammdaten wird angezeigt. |  |
| 9 | Konto kopieren | Wählen Sie Kopieren. | Das Bild Kopie von <Sachkontonummer> wird angezeigt. |  |
| 10 | Konto anlegen | Geben Sie folgende Daten ein, und wählen Sie OK:Kontonummer: <Kontonummer>Bezeichnung in Pflegesprache (DE): <Beschreibung>Konzernkontonummer: <Kontonummer>Hinweis Die Feld ist nur sichtbar, wenn Konsolidierung im Umfang enthalten ist. | Die auf dem Bild Sachkontenstammdaten erfassten Daten werden angezeigt. |  |
| 11 | Beschreibung hinzufügen | Geben Sie im Bereich Basisinformationen folgende Daten ein:Kontenplan: YCOASachkontenlangtext: <Beschreibung> |  |  |
| 12 | Buchungskreis zuordnen | Wählen Sie im Abschnitt Buchungskreiszuordnung einen Buchungskreis, der dem Konto zugeordnet werden soll. |  |  |
| 13 | Übersetzungen hinzufügen | Geben Sie im Abschnitt Übersetzung die Kurz- und Langtexte in allen erforderlichen Sprachen ein. |  |  |
| 14 | Daten sichern | Wählen Sie Sichern. | Das System bestätigt, dass das Konto erfolgreich gesichert wurde. |  |

SAP Central Business Configuration:

| Testschrittnummer | Bezeichnung des Testschritts | Anweisung | Erwartetes Ergebnis | Kommentare |
| --- | --- | --- | --- | --- |
| 1 | Anmelden | Melden Sie sich an der Projekterfahrung in SAP Central Business Configuration an. | "Flexiblen Workflow aktivieren" öffnen |  |
| 2 | SAP-Fiori-App aufrufen | Rufen Sie die App Business Processes Configuration auf, und suchen Sie nach der folgenden Aktivität: Manage G/L Account Master Data.Wählen Sie die Position im Suchergebnis, um weitere Details zu dieser Konfigurationsaktivität anzuzeigen.Wählen Sie die Drucktaste Zur Aktivität, um direkt zum SAP S/4HANA Cloud Public Edition-System zu navigieren. Melden Sie sich am SAP Fiori Launchpad als Konfigurationsexperte – Geschäftsprozesskonfiguration an. |  |  |
| 3 | Nach Ihrem Konto suchen | Geben Sie Folgendes ein, und wählen Sie Start:Sicht: KontenplansichtKontenplan: YCOA | Das System zeigt eine Liste übereinstimmender Sachkonten an. |  |
| 4 | Sachkonto wählen | Wählen Sie das Sachkonto im Suchergebnis aus.Hinweis Klicken Sie auf den blauen Kontonummernlink. | Das Bild Sachkontenstammdaten wird angezeigt. |  |
| 5 | Konto kopieren | Wählen Sie Kopieren. | Das Bild Kopie von <Sachkontonummer> wird angezeigt. |  |
| 6 | Konto anlegen | Geben Sie folgende Daten ein, und wählen Sie OK:Kontonummer: <Kontonummer>Bezeichnung in Pflegesprache (DE): <Beschreibung>Konzernkontonummer: <Kontonummer>Hinweis Die Feld ist nur sichtbar, wenn Konsolidierung im Umfang enthalten ist. | Die auf dem Bild Sachkontenstammdaten erfassten Daten werden angezeigt. |  |
| 7 | Beschreibung hinzufügen | Geben Sie im Bereich Basisinformationen folgende Daten ein:Kontenplan: YCOASachkontenlangtext: <Beschreibung> |  |  |
| 8 | Buchungskreis zuordnen | Wählen Sie im Abschnitt Buchungskreiszuordnung einen Buchungskreis, der dem Konto zugeordnet werden soll. |  |  |
| 9 | Übersetzungen hinzufügen | Geben Sie im Abschnitt Übersetzung die Kurz- und Langtexte in allen erforderlichen Sprachen ein. |  |  |
| 10 | Daten sichern | Wählen Sie Sichern. | Das System bestätigt, dass das Konto erfolgreich gesichert wurde. |  |

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
- related-to :: [[03-financial-accounting-and-close/criar-conta-do-razao-e-classe-de-custo-mds-bng-602]]
- related-to :: [[03-financial-accounting-and-close/g-l-mds-bng-601]]
- related-to :: [[03-financial-accounting-and-close/master-data-script-create-g-l-account-and-cost-element-mds-bng-599]]
- related-to :: [[03-financial-accounting-and-close/mds-bng-603]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/BNG_S4CLD2608_Master_Data_DE_XX.docx` — full document · extracted with `mammoth` · 19,104 chars in the whole document
