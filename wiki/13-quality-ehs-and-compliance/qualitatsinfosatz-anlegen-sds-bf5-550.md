---
id: 13-quality-ehs-and-compliance/qualitatsinfosatz-anlegen-sds-bf5-550
title: Qualitätsinfosatz anlegen – SDS (BF5) (BF5_S4CLD2608_Master_Data_DE_XX)
description: "German master data script (BF5) for SAP S/4HANA Cloud Public Edition 2608: creating quality info records, QM control keys and PPAP settings in procurement."
cluster: 13-quality-ehs-and-compliance
tags: [kb/quality-ehs-and-compliance, topic/quality-info-records]
aliases: [BF5_S4CLD2608_Master_Data_DE_XX]
keywords: [Quality Info Records in Procurement, quality info record, qm control key, ppap, first article inspection, supplier release, goods receipt inspection, quality planner role, master data scripts, BF5]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/BF5_S4CLD2608_Master_Data_DE_XX.docx]
confidence: high
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-550
topic: 13-quality-ehs-and-compliance/quality-info-records
language: DE
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Qualitätsinfosatz anlegen – SDS (BF5) (BF5_S4CLD2608_Master_Data_DE_XX)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/BF5_S4CLD2608_Master_Data_DE_XX.docx`, extracted with `mammoth`. Grouped under **Quality Info Records in Procurement** in Quality, EHS and Compliance. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

| <!-- image omitted: unnamed --> | StammdatenskriptSAP S/4HANA Cloud Public Edition - 02-07-26 |
| --- | --- |
|  | Qualitätsinfosatz anlegen – SDS (BF5) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Inhaltsverzeichnis

[1 Zweck 2](#_Toc233889902)

[2 Voraussetzungen 3](#_Toc233889903)

[2.1 Systemzugriff 3](#_Toc233889904)

[2.2 Rollen 3](#_Toc233889905)

[2.3 Erforderliche Organisationseinheiten 3](#_Toc233889906)

[2.4 Obligatorische und optionale Stammdaten 4](#_Toc233889907)

[3 Übersichtstabelle 5](#_Toc233889908)

[4 Testverfahren 6](#_Toc233889909)

[4.1 Qualitätsinfosatz in Beschaffung anlegen 6](#_Toc233889910)

[4.2 Qualitätsinfosatz für Materialien ohne Qualitätsinfosatz anlegen (optional) 7](#_Toc233889911)

[4.3 QM-Steuerschlüssel für Beschaffung zuordnen 8](#_Toc233889912)

[4.4 Einstellungen für PPAP anlegen 9](#_Toc233889913)

## Zweck

Falls für ein Material eine Qualitätssicherungsvereinbarung oder eine Lieferantenfreigabe erforderlich ist, muss ein Qualitätsplaner einen Qualitätsinfosatz anlegen. Der Qualitätsinfosatz bestimmt, wie das Material weiter verarbeitet werden kann.

Wenn eine Bestellung angelegt wird, prüft das System, ob ein Qualitätsinfosatz erforderlich und für die Kombination aus Material und Lieferant verfügbar ist.

Das System prüft weiterhin, ob der Lieferant und die Kombination aus Material und Lieferant gesperrt oder für Angebote, Bestellungen und/oder Wareneingang freigegeben sind. Die Ausführung dieser Prüfung hängt von den Einstellungen des Steuerschlüssels QM in der Beschaffung im Materialstamm ab.

Darüber hinaus können Sie QM-Systeme zuordnen und entsprechend eine mögliche Prüfung anstoßen. Es kann auch festgelegt werden, ob eine Wareneingangsprüfung und/oder eine Abnahmeprüfung angestoßen wird. Sie können festlegen, dass ein Produktionsteil-Freigabeverfahren (PPAP) erforderlich ist, für das Sie im Qualitätsinfosatz Erstmusterprüfungen (FAI) planen können. Sie können PPAP hier verwalten, indem Sie den PPAP-Status und den Bewertungscode aktualisieren (basierend auf dem getroffenen Verwendungsentscheid). Sie können für PPAP auch mehrere Bestellungen/Positionen gleichzeitig zuordnen, um die Erstmusterprüfung durchzuführen.

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
| Qualitätsplaner | SAP_BR_QUALITY_PLANNER | Qualitätsplanung | SAP_BR_QUALITY_PLANNER |  |

Weitere Informationen zu Benutzerrollen finden Sie unter "Benutzern Benutzerrollen zuordnen" im Administrationsleitfaden für die Implementierung von SAP S/4HANA Cloud Public Edition.

### Erforderliche Organisationseinheiten

Einige Segmente von Debitorenstammdaten hängen von den Organisationseinheiten des Unternehmens ab. Allgemeine (zentrale) Daten hängen nicht von einer Organisationseinheit oder dem Buchungskreis ab. Die folgende Tabelle stellt eine Übersicht dieser verschiedenen Datensegmente und ihrer relevanten Organisationseinheiten bereit:

| Datensegment | Hängt ab von | Feldbeispiele | Kommentare | Zu verwendende Organisationseinheit |
| --- | --- | --- | --- | --- |
| Qualitätsinfosatz | Werk |  | Werksdaten können für jede Werks-ID Ihrer Unternehmensstruktur existieren, für die der Materialstammsatz verwendet wird. | Werk: |

### Obligatorische und optionale Stammdaten

Qualitätsmanagement-Stammdatensätze können auf andere Stammdaten verweisen. Die folgende Tabelle bietet eine Übersicht über die optionalen und obligatorischen Stammdatenobjekte, die in einem Qualitätsinfosatz verwendet werden müssen.

| Stammdatenobjekt | Verwendet im Datensegment | Obligatorisch / optional | Kommentare |
| --- | --- | --- | --- |
| Materialstamm |  | Obligatorisch | Mit Qualitätsmanagement-Sicht. Weitere Informationen finden Sie im Stammdatenskript Qualitätsmanagementattribute für Material-/Produktstamm anlegen – SDS (BNY). |
| Lieferantenstamm |  | Obligatorisch |  |

|  |
| --- |
| Hinweis Ein Qualitätsinfosatz ist zwingend notwendig, wenn der QM-Beschaffungsschlüssel eine Lieferantenfreigabe erfordert. In diesem Fall muss für jede Kombination aus Lieferant/Material ein Qualitätsinfosatz angelegt werden. |

## Übersichtstabelle

Dieser Umfangsbestandteil umfasst die verschiedenen Prozessschritte in der folgenden Tabelle:

|  |
| --- |
| Hinweis Wenn Ihr Systemadministrator Bereiche und Seiten auf dem SAP Fiori Launchpad aktiviert hat, enthält die Startseite nur die wesentlichen Apps, mit denen die typischen Aufgaben einer Benutzerrolle ausgeführt werden können.Alle anderen (suchbaren) Apps, die nicht auf der Startseite enthalten sind, finden Sie über die Suchleiste ([2434549](https://me.sap.com/notes/2434549)).Wenn Sie die Startseite personalisieren und versteckte Apps hinzufügen möchten, wechseln Sie in Ihr Benutzerprofil und wählen Sie App Finder. |

| Prozessschritt | Benutzerrolle | App/Vorgang | Erwartete Ergebnisse |
| --- | --- | --- | --- |
| [Qualitätsinfosatz in Beschaffung anlegen](#unique_8) [Seite ] 6 | Qualitätsplaner | Q-Infosatz anlegen - Beschaffung(QI01) | Ein Qualitätsinfosatz wird angelegt. |
| [Qualitätsinfosatz für Materialien ohne Qualitätsinfosatz anlegen (optional)](#unique_9) [Seite ] 7 | Qualitätsplaner | Q-Infosätze verwalten(F2256A) | Ein Qualitätsinfosatz wird angelegt. |
| [QM-Steuerschlüssel für Beschaffung zuordnen](#unique_10) [Seite ] 8 | Qualitätsplaner | QM-Steuerschlüssel für Beschaffung zuordnen – Manuell bearbeiten(QI05) | Ein Qualitätsinfosatz wird angelegt. |
| [Einstellungen für PPAP anlegen](#unique_11) [Seite ] 9 | Qualitätsplaner | Q-Infosätze verwalten(F2256A) | Ein Qualitätsinfosatz wird angelegt. |

## Testverfahren

In diesem Abschnitt werden die Testverfahren für den jeweiligen Prozessschritt beschrieben, der zum betreffenden Umfangsbestandteil gehört.

### Qualitätsinfosatz in Beschaffung anlegen

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
| 1 | Anmelden | Melden Sie sich am SAP Fiori Launchpad als Qualitätsplaner an. | Das SAP Fiori Launchpad wird angezeigt. |  |
| 2 | SAP-Fiori-App aufrufen | Öffnen Sie Q-Infosatz anlegen - Beschaffung(QI01). | Die Sicht Qualitätsinfosatz anlegen wird angezeigt |  |
| 3 | Allgemeine Daten eingeben | Nehmen Sie folgende Einträge vor:Material: <Materialnummer>Lieferant: <Lieferantennummer>Werk: <Nummer des Werks>Wählen Sie Weiter. |  |  |
| 4 | Freigabedaten eingeben | Geben Sie im Abschnitt Freigabe die folgenden Daten ein:Freigabe bis: Datum in der Zukunft, z.B. in einem JahrOptional:Freigabemenge aktiv: vorgemerktAbrufmengen: z.B. 15 |  |  |
| 5 | Daten sichern | Wählen Sie Sichern. | Ihre Daten werden gesichert. |  |

|  |
| --- |
| Hinweis Im Qualitätsinfosatz können Sie außerdem festlegen, ob Sie die Wareneingangsprüfung deaktivieren wollen oder eine Wareneingangsprüfung und/oder Abnahmeprüfung durchführen wollen. Wählen Sie dazu die Registerkarte Prüfsteuerung, und geben Sie die folgenden Daten ein:Wenn Sie zusätzlich zur Wareneingangsprüfung eine Abnahmeprüfung durchführen wollen, geben Sie eine Prüfart für die Abnahmeprüfung und eine Vorlaufzeit in Tagen an.Wenn Sie keine Wareneingangsprüfung durchführen wollen, obwohl die Einstellungen im Materialstammsatz diese vorsehen, setzen Sie das Kennzeichen Keine Prüfung.Wenn Sie eine Abnahmeprüfung anstelle einer Wareneingangsprüfung durchführen wollen, setzen Sie das entsprechende Kennzeichen.Wenn dieses Kennzeichen gesetzt ist, wird im Falle einer Abnahmeprüfung kein Prüflos für einen Wareneingang erzeugt. Wird keine Abnahmeprüfung durchgeführt, wird ein Prüflos für den Wareneingang erzeugt.Auf der Registerkarte Prüfsteuerung können Sie außerdem Folgendes erfassen:QM-System des LieferantenFalls der Lieferant ein QM-System unterhält, können Sie hier die Beschreibung dieses QM-Systems für dieses bestimmte Material hinterlegen.Produktionsteil-FreigabeSie können festlegen, dass ein Produktionsteil-Freigabeverfahren erforderlich ist. Hierfür müssen Sie weitere Einstellungen in der App Q-Infosätze verwalten(F2256A) vornehmen (siehe Kapitel [QM-Steuerschlüssel für Beschaffung zuordnen](#unique_10) [Seite ] 8). |

### Qualitätsinfosatz für Materialien ohne Qualitätsinfosatz anlegen (optional)

Testverwaltung

Kundenprojekt: Füllen Sie die projektbezogenen Teile aus.

|  |  |  |  |
| --- | --- | --- | --- |
| Testfall-ID | <X.XX> | Testdatum: |  |
| Testername: |  | Dauer: |  |
| Benutzerrolle(n): |  | Zuständigkeit: | <Geben Sie den Serviceanbieter, einen Kunden oder einen Serviceanbieter zusammen mit einem Kunden an.> |

Vorgehensweise

| Testschrittnummer | Bezeichnung des Testschritts | Anweisungen | Erwartetes Ergebnis | Kommentare |
| --- | --- | --- | --- | --- |
| 1 | Anmelden | Melden Sie sich am SAP Fiori Launchpad als Qualitätsplaner an. | Das SAP Fiori Launchpad wird angezeigt. |  |
| 2 | SAP-Fiori-App aufrufen | Öffnen Sie Q-Infosätze verwalten(F2256A). |  |  |
| 3 | Qualitätsinfosatz anlegen (optional) | Wählen Sie in der oberen rechten Ecke der Ergebnistabelle Anlegen, und geben Sie auf Kopfebene die folgenden Daten ein:Material: MaterialnummerLieferant: LieferantennummerWerk: Nummer des WerksInformationen zum Abschnitt Freigabe finden Sie im vorherigen Kapitel, Schritt 4. |  |  |
| 4 | Daten sichern | Wählen Sie Anlegen. | Ihre Daten werden gesichert, und ein neuer Qualitätsinfosatz wird angelegt. |  |

### QM-Steuerschlüssel für Beschaffung zuordnen

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
| 1 | Anmelden | Melden Sie sich am SAP Fiori Launchpad als Qualitätsplaner an. | Das SAP Fiori Launchpad wird angezeigt. |  |
| 2 | SAP-Fiori-App aufrufen | Öffnen Sie QM-Steuerschlüssel für Beschaffung zuordnen – Manuell bearbeiten(QI05).. |  |  |
| 3 | QM-Steuerschlüssel zuordnen | Sie können diese Auswahl auf Werks- und/oder Materialebene ausführen. Wählen Sie den zuzuordnenden QM-Steuerschlüssel aus.Material: MaterialnummerWerk: Nummer des WerksQM-Steuerschlüssel: QM-SteuerschlüsselDatenbankänderung durchführen: aktiv (wenn dieses Kennzeichen nicht gesetzt ist, wird nur ein Testlauf ausgeführt)Hinweis Es werden nur die Materialien, bei denen in den Materialstammdaten das Kennzeichen QM in Besch. aktiv gesetzt ist, ausgewählt. |  |  |

### Einstellungen für PPAP anlegen

Testverwaltung

Kundenprojekt: Füllen Sie die projektbezogenen Teile aus.

|  |  |  |  |
| --- | --- | --- | --- |
| Testfall-ID | <X.XX> | Testdatum: |  |
| Testername: |  | Dauer: |  |
| Benutzerrolle(n): |  | Zuständigkeit: | <Geben Sie den Serviceanbieter, einen Kunden oder einen Serviceanbieter zusammen mit einem Kunden an.> |

Voraussetzung

Eine Erstmusterprüfung wird durch die Nutzung einer dedizierten Prüfplanverwendung "WE Erstmusterprüfung" erreicht, die folgenden Steuerschlüsseln für das QM in der Beschaffung zugeordnet ist:

- 0001 Lieferantenfreigabe
- 9001 Lieferantenfreigabe (mit Fehlermeldung)

Im Einzelnen müssen folgende Voraussetzungen erfüllt sein, damit eine Erstmusterprüfung durchgeführt werden kann:

- Ein Prüfplan mit Verwendung "WE Erstmusterprüfung" (51) existiert für die Erstmusterprüfung
- Einer der oben aufgeführten QM-Steuerschlüssel ist dem Material zugeordnet.
- Für dieses Material ist unter Produktionsteil-Freigabe ein Qualitätsinfosatz mit den folgenden Einstellungen vorhanden:
    - Produktionsteil-Freigabe ist aktiviert, und der PPAP-Level und PPAP-Status sind gesetzt.
    - Mindestens eine Bestellung und Bestellposition sind erfasst.

Beim Wareneingang für die Bestellposition wird ein Prüflos für die Erstmusterprüfung erzeugt. Für dieses Prüflos wird die "Planverwendung Erstmusterprüfung" des QM-Steuerschlüssels übernommen und die Verwendung, die für die Prüfart hinterlegt ist.

Vorgehensweise

Sie aktivieren PPAP in der App Q-Infosätze verwalten(F2256A). Dort können Sie für ein Material festlegen, dass für eine oder mehrere Bestellpositionen eine Erstmusterprüfung beim Wareneingang erfolgen soll.

Vorgehensweise

| Testschrittnummer | Bezeichnung des Testschritts | Anweisung | Erwartetes Ergebnis | Kommentare |
| --- | --- | --- | --- | --- |
| 1 | Anmelden | Melden Sie sich am SAP Fiori Launchpad als Qualitätsplaner an. | Das SAP Fiori Launchpad wird angezeigt. |  |
| 2 | SAP-Fiori-App aufrufen | Öffnen Sie Q-Infosätze verwalten(F2256A). |  |  |
| 3 | Qualitätsinfosatz anlegen | Wählen Sie in der oberen rechten Ecke der Ergebnistabelle Anlegen, und geben Sie auf Kopfebene die folgenden Daten ein:Material: MaterialnummerLieferant: LieferantennummerWerk: Nummer des WerksInformationen zum Abschnitt Freigabe finden Sie im vorherigen Kapitel, Schritt 4.Alternativ können Sie einen vorhandenen Qualitätsinfosatz auswählen, für den Sie das PPAP aktivieren möchten. |  |  |
| 4 | Daten für die Produktionsteil-Freigabe eingeben | Wechseln Sie zum Abschnitt Produktionsteil-Freigabe. Wählen Sie Aktivieren.Ordnen Sie im Feld PPAP-Level den entsprechenden PPAP-Level zu. |  |  |
| 5 | Daten sichern | Wählen Sie Anlegen. | Ihre Daten werden gesichert, und ein neuer Qualitätsinfosatz wird angelegt. |  |

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
- related-to :: [[13-quality-ehs-and-compliance/crear-registro-info-de-calidad-mds-bf5-552]]
- related-to :: [[13-quality-ehs-and-compliance/create-quality-info-record-mds-bf5-551]]
- related-to :: [[13-quality-ehs-and-compliance/criar-registro-info-de-qualidade-mds-bf5-554]]
- related-to :: [[13-quality-ehs-and-compliance/mds-bf5-553]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/BF5_S4CLD2608_Master_Data_DE_XX.docx` — full document · extracted with `mammoth` · 17,614 chars in the whole document
