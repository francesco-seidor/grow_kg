---
id: 05-treasury-and-cash-management/geschaftspartner-fur-treasury-and-risk-management-anlegen-mds-22g-256
title: Geschäftspartner für Treasury and Risk Management anlegen - MDS (22G) (22G_S4CLD2608_Master_Data_DE_XX)
description: "German master data script (22G) for SAP S/4HANA Cloud Public Edition 2608: manual test steps to create business partners for Treasury and Risk Management."
cluster: 05-treasury-and-cash-management
tags: [kb/treasury-and-cash-management, topic/treasury-business-partners]
aliases: [22G_S4CLD2608_Master_Data_DE_XX]
keywords: [Business Partners for Treasury and Risk Management, business partner creation, treasury risk management, payment connections, business partner authorizations, treasury correspondence, business partner profiles, issuer and custodian roles, derived transactions, reporting data]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/22G_S4CLD2608_Master_Data_DE_XX.docx]
confidence: high
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-256
topic: 05-treasury-and-cash-management/treasury-business-partners
language: DE
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Geschäftspartner für Treasury and Risk Management anlegen - MDS (22G) (22G_S4CLD2608_Master_Data_DE_XX)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/22G_S4CLD2608_Master_Data_DE_XX.docx`, extracted with `mammoth`. Grouped under **Business Partners for Treasury and Risk Management** in Treasury and Cash Management. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

| <!-- image omitted: unnamed --> | StammdatenskriptSAP S/4HANA Cloud Public Edition - 02-07-26 |
| --- | --- |
|  | Geschäftspartner für Treasury and Risk Management anlegen - MDS (22G) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Inhaltsverzeichnis

[1 Zweck 2](#_Toc233889557)

[2 Voraussetzungen 3](#_Toc233889558)

[2.1 Systemzugriff 3](#_Toc233889559)

[2.2 Rollen 3](#_Toc233889560)

[2.3 Stammdaten, Organisationsdaten und sonstige Daten 4](#_Toc233889561)

[3 Übersichtstabelle 5](#_Toc233889562)

[4 Testverfahren 7](#_Toc233889563)

[4.1 Allgemeine Daten für Geschäftspartner pflegen 7](#_Toc233889564)

[4.2 Buchungskreisdaten für Geschäftspartner pflegen 9](#_Toc233889565)

[4.2.1 Zahlungsverbindungen für Geschäftspartner pflegen 9](#_Toc233889566)

[4.2.2 Berechtigungen für Geschäftspartner pflegen 12](#_Toc233889567)

[4.2.3 Abgeleitete Bewegungen für Geschäftspartner pflegen (optional) 13](#_Toc233889568)

[4.2.4 Meldedaten im Buchungskreis für Geschäftspartner pflegen 15](#_Toc233889569)

[4.3 Korrespondenzdaten für Geschäftspartner pflegen 17](#_Toc233889570)

[4.3.1 Profil- und GP-Gruppenzuordnungen zu externen Empfängern bearbeiten 17](#_Toc233889571)

[4.3.2 Zuordnung von Profilen und Geschäftspartnergruppen zu internen Empfängern pflegen 21](#_Toc233889572)

[4.4 Geschäftspartnerstammdaten für Wertpapiere pflegen 25](#_Toc233889573)

[4.4.1 Rolle "Emittent" für Geschäftspartner anlegen 25](#_Toc233889574)

[4.4.2 Rolle "Depotbank" für Geschäftspartner anlegen 26](#_Toc233889575)

[4.5 Geschäftspartnerstammdaten für Akkreditiv pflegen 27](#_Toc233889576)

[4.5.1 Bankrolle für Geschäftspartner anlegen 27](#_Toc233889577)

## Zweck

Dieser Building Block umfasst die grundlegenden manuellen Schritte zum Anlegen von Geschäftspartnern für Treasury and Risk Management.

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
| Treasury-Spezialist – Backoffice | SAP_BR_TREASURY_SPECIALIST_BOE | Treasury-Backoffice | SAP_BR_TREASURY_SPECIALIST_BOE |  |
| Stammdatenexperte – Geschäftspartnerdaten | SAP_BR_BUPA_MASTER_SPECIALIST | Stammdaten – Geschäftspartner / Geschäftspartner-Governance / Geschäftspartner-Governance / Geschäftspartner-Governance | SAP_BR_BUPA_MASTER_SPECIALIST / SAP_CA_SPT_MDG_BP_GOV_PC / SAP_CMD_SPT_BP_GOV_PC / SAP_CA_SPT_MDG_BP_WFUSR_PC |  |
| Konfigurationsexperte – Geschäftsprozesskonfiguration | SAP_BR_BPC_EXPERT | Geschäftsprozesskonfiguration / Geschäftsprozesskonfiguration - Finance / Geschäftsprozesskonfiguration - Beschaffung / Lösung verwalten / Geschäftsprozesskonfiguration - Workflow / Geschäftskonfiguration - Feature Management / Geschäftsprozesskonfiguration - Extensibility Explorer / Business Configuration - Transportation Management | SAP_BR_BPC_EXPERT / SAP_FIN_SPT_BPC_EXPERT_PC / SAP_MM_SPT_BIZ_PROC_CONFIGN_PC / SAP_CA_SPT_IC_LND_BASE_PC / SAP_CA_SPT_BPC_WORKFLOW_PC / SAP_CA_SPT_BPC_FM_PC / SAP_EI_SPT_BPC_EXT_PC / SAP_TM_SPT_TRANSPCFG_PC |  |

### Stammdaten, Organisationsdaten und sonstige Daten

Die Organisationsstruktur und die Stammdaten Ihres Unternehmens wurden bei der Aktivierung in Ihrem System angelegt. Die Organisationsstruktur gibt den Aufbau Ihres Unternehmens wieder. Die Stammdaten stehen beispielsweise für Materialien, Kunden und Lieferanten, je nach dem betrieblichen Schwerpunkt Ihres Unternehmens.

Verwenden Sie für die Durchführung des Tests eigene Stammdaten. Wenn Sie ein SAP Best Practices Baseline Package installiert haben, können Sie die folgenden Baseline-Package-Beispieldaten verwenden.

|  |
| --- |
| Achtung Beispielwerte für Stammdaten sind länder-/regionsspezifisch. Die Werte in der folgenden Tabelle gelten für Deutschland. Ersetzen Sie die länder-/regionsspezifischen Werte von SAP Best Practices for SAP S/4HANA Cloud, Public Edition, oder verwenden Sie die von Ihnen zu diesem Zweck angelegten Stammdatenwerte. |

| Daten | Beispielwert | Details | Kommentare |
| --- | --- | --- | --- |
| BUCHUNGSKREIS | z.B. 1010. |  |  |
| WÄHRUNG | z.B. EUR |  |  |
| FREMDWÄHRUNG 1 | z.B. USD |  |  |
| HAUSBANK | z.B. DEBK1 |  |  |
| KONTONUMMER HAUSBANK 1 | z.B. DEAC1 |  |  |
| KONTONUMMER HAUSBANK 2 | z.B. USAC2 |  |  |
| GESCHÄFTSPARTNER | 10537001 |  |  |

## Übersichtstabelle

Geschäftspartner für Treasury and Risk Management anlegen - MDS (22G) umfasst die verschiedenen Schritte in der folgenden Tabelle:

|  |
| --- |
| Hinweis Wenn Ihr Systemadministrator Bereiche und Seiten auf dem SAP Fiori Launchpad aktiviert hat, enthält die Startseite nur die wesentlichen Apps, mit denen die typischen Aufgaben einer Benutzerrolle ausgeführt werden können.Alle anderen (suchbaren) Apps, die nicht auf der Startseite enthalten sind, finden Sie über die Suchleiste ([2434549](https://me.sap.com/notes/2434549)).Wenn Sie die Startseite personalisieren und versteckte Apps hinzufügen möchten, wechseln Sie in Ihr Benutzerprofil und wählen Sie App Finder. |

Tabelle 1: Daten für normale Geschäftspartner pflegen

| Prozessschritt, Report oder Bestandteil | Benutzerrolle | Vorgang/App | Erwartete Ergebnisse |
| --- | --- | --- | --- |
| [Allgemeine Daten für Geschäftspartner pflegen](#unique_7) [Seite ] 7 | Stammdatenexperte – Geschäftspartnerdaten | Geschäftspartner pflegen(BP) | Die allgemeinen Daten für den Geschäftspartner sind gepflegt. |
| Buchungskreisdaten für Geschäftspartner pflegen |  |  |  |
| [Zahlungsverbindungen für Geschäftspartner pflegen](#unique_8) [Seite ] 9 | Stammdatenexperte – Geschäftspartnerdaten | Geschäftspartner pflegen(BP) | Die Zahlungsverbindungsdaten für den Geschäftspartner sind gepflegt. |
| [Berechtigungen für Geschäftspartner pflegen](#unique_9) [Seite ] 12 | Stammdatenexperte – Geschäftspartnerdaten | Geschäftspartner pflegen(BP) | Die Berechtigungsdaten für den Geschäftspartner sind gepflegt. |
| [Abgeleitete Bewegungen für Geschäftspartner pflegen (optional)](#unique_10) [Seite ] 13 | Stammdatenexperte – Geschäftspartnerdaten | Geschäftspartner pflegen(BP) | Die abgeleiteten Bewegungsdaten für den Geschäftspartner sind gepflegt. |
| [Meldedaten im Buchungskreis für Geschäftspartner pflegen](#unique_11) [Seite ] 15 | Stammdatenexperte – Geschäftspartnerdaten | Geschäftspartner pflegen(BP) | Die Meldedaten für den Geschäftspartner sind gepflegt. |
| Korrespondenzdaten für Geschäftspartner pflegen |  |  |  |
| [Profil- und GP-Gruppenzuordnungen zu externen Empfängern bearbeiten](#unique_12) [Seite ] 17 | Stammdatenexperte – Geschäftspartnerdaten | Profil und GP-Gruppe zuordnen - Externe Empfänger(FTR_EXT_ASSIGN) | GP-Profile und GP-Gruppen für den externen Empfänger sind gepflegt. |
| [Zuordnung von Profilen und Geschäftspartnergruppen zu internen Empfängern pflegen](#unique_13) [Seite ] 21 | Stammdatenexperte – Geschäftspartnerdaten | Profil und GP-Gruppe zuordnen - Interne Empfänger(FTR_INT_ASSIGN) | GP-Profile, GP-Gruppen und Benutzer-IDs für den internen Empfänger sind gepflegt. |
| Geschäftspartnerstammdaten für Wertpapiere pflegen |  |  |  |
| [Rolle "Emittent" für Geschäftspartner anlegen](#unique_14) [Seite ] 25 | Stammdatenexperte – Geschäftspartnerdaten | Geschäftspartner pflegen(BP) | Die Rolle "Emittent" wird angelegt. |
| [Rolle "Depotbank" für Geschäftspartner anlegen](#unique_15) [Seite ] 26 | Stammdatenexperte – Geschäftspartnerdaten | Geschäftspartner pflegen(BP) | Die Rolle "Depotbank" wird angelegt. |
| Geschäftspartnerstammdaten für Akkreditiv pflegen |  |  |  |
| [Bankrolle für Geschäftspartner anlegen](#unique_16) [Seite ] 27 | Stammdatenexperte – Geschäftspartnerdaten | Geschäftspartner pflegen(BP) | Die Rolle "Bank" wird angelegt. |

## Testverfahren

In diesem Abschnitt werden die Testverfahren für den jeweiligen Prozessschritt beschrieben, der zum betreffenden Umfangsbestandteil gehört.

### Allgemeine Daten für Geschäftspartner pflegen

Testverwaltung

Kundenprojekt: Füllen Sie die projektbezogenen Teile aus.

|  |  |  |  |
| --- | --- | --- | --- |
| Testfall-ID | <X.XX> | Testdatum: |  |
| Testername: |  | Dauer: |  |
| Benutzerrolle(n): |  | Zuständigkeit: | <Geben Sie den Serviceanbieter, einen Kunden oder einen Serviceanbieter zusammen mit einem Kunden an.> |

Zweck

In diesem Abschnitt werden die Schritte zum Pflegen der allgemeinen Daten für einen Geschäftspartner beschrieben.

|  |
| --- |
| Nicht vergessen Beispielwerte für Stammdaten sind länder-/regionsspezifisch. Die Werte in der folgenden Tabelle gelten für Deutschland. Ersetzen Sie die länder-/regionsspezifischen Werte von SAP Best Practices for SAP S/4HANA Cloud, Public Edition, oder verwenden Sie die von Ihnen zu diesem Zweck angelegten Stammdatenwerte. |

Vorgehensweise

| Testschrittnummer | Bezeichnung des Testschritts | Anweisungen | Erwartetes Ergebnis | Bestanden/Nicht bestanden/Anmerkung |
| --- | --- | --- | --- | --- |
| 1 | Anmelden | Melden Sie sich am SAP Fiori Launchpad als Stammdatenexperte – Geschäftspartnerdaten an. | Das SAP Fiori Launchpad wird angezeigt. |  |
| 2 | SAP-Fiori-App aufrufen | Öffnen Sie Geschäftspartner pflegen(BP). | Die App wird geöffnet. |  |
| 3 | Daten auf dem Einstiegsbild erfassen | Wählen Sie auf dem Bild Geschäftspartner pflegen die Option Organisation. | Das Bild Organisation anlegen wird angezeigt. |  |
| 4 | Adressdaten eingeben | Geben Sie auf dem Bild Organisation anlegen folgende Daten ein:Geschäftspartner: z.B. 10537001Gruppierung: Wählen Sie TR02 Treasury-Partner (extern).Anlegen in GP-Rolle: Wählen Sie 000000 Geschäftspartner (allg.).Titel: Wählen Sie 0003 Unternehmen.Name: z.B. Bank 1 – BEISPIELBANKAnrede: z.B. Bank 1Suchbegriff 1/2: z.B. Bank 1Straße/Hausnummer: <Straßenadresse>Postleitzahl/Ort: <Postleitzahl und Ort>Land/Region: Wählen Sie den <Länder-/Regionscode> ausSprache: Wählen Sie den <Sprachschlüssel> aus.E-Mail: <E-Mail-Adresse>Adresse gültig ab: z.B. <aktuelles Datum im Vorjahr>Adresse gültig bis: z.B. 31.12.9999Wählen Sie Sichern.Hinweis Bleiben Sie für die nachfolgenden Schritte auf dem Bild.Hinweis Wenn Ihnen nur Geschäftspartner (Allg.) ohne den Schlüssel 000000 angezeigt wird, können Sie zu Menü > Einstellungen - Interaktionsdesign > Visualisierung > Dropdown-Liste > Dropdown-Listen mit Schlüsseln anzeigen navigieren und ihn einschalten. | Der Geschäftspartner wird erfolgreich angelegt. |  |
| 5 | In den Änderungsmodus wechseln | Wählen Sie auf dem Bild Organisation anzeigen: 10537001 die Option Umschalten zwischen Anzeigen und Ändern, und geben Sie die folgenden Daten ein:Ändern in GP-Rolle: Wählen Sie TR0151 Kontrahent, | Es werden weitere zum Kontrahenten gehörige Registerkarten angezeigt, z.B. Juristische Daten oder Bewertung. |  |
| 6 | Juristische Daten eingeben | Wählen Sie auf dem Bild Organisation ändern: 10537001, neue Rolle Kontrahent das Navigationsmenü.Hinweis Das Navigationsmenü wird ganz rechts auf dem Bild angezeigt. Es wird rechts neben dem Symbol > als … angezeigt.Wählen Sie in der Dropdown-Liste Juristische Daten, und geben Sie folgende Daten ein:Land/Region: Wählen Sie z.B.: DEWählen Sie Sichern.Hinweis Bleiben Sie für die nachfolgenden Schritte auf dem Bild. | Die juristischen Daten werden erfasst und gesichert.Das Bild Organisation ändern: 10537001, neue Rolle Kontrahent wird angezeigt. |  |
| 7 | Daten zum Zahlungsverkehr eingeben | Wählen Sie auf dem Bild Organisation ändern: 10537001, Rolle Kontrahent das Navigationsmenü.Wählen Sie in der Dropdown-Liste die Option Zahlungsverkehr, und geben Sie folgende Daten für zwei Zeilen ein:Zeile 1:ID: Währungscode + 1, z.B. EUR1L/R: <Länder-/Regionscode>Bankschlüssel: <Bankschlüssel>Bankkonto: <Bankkonto>IBAN: Wählen Sie IBAN, und wählen Sie dann im Dialogfenster IBAN die Option Weiter.Zeile 2:ID: Fremdwährungscode + 1, z.B. USD1L/R: <Länder-/Regionscode>Bankschlüssel: <Bankschlüssel>Bankkonto: <Bankkonto>IBAN: Wählen Sie IBAN, und wählen Sie dann im Dialogfenster IBAN die Option Weiter.Wählen Sie Sichern.Hinweis Wenn beim Auswählen der IBAN das Dialogfenster Informationen angezeigt wird, wählen Sie Weiter.Hinweis Die IBAN wird hauptsächlich in EU-Ländern verwendet. Für die USA überspringen Sie die IBAN-bezogenen Schritte. | Die Daten zum Zahlungsverkehr sind erfasst, und der Geschäftspartner wird gesichert. |  |

### Buchungskreisdaten für Geschäftspartner pflegen

#### Zahlungsverbindungen für Geschäftspartner pflegen

Testverwaltung

Kundenprojekt: Füllen Sie die projektbezogenen Teile aus.

|  |  |  |  |
| --- | --- | --- | --- |
| Testfall-ID | <X.XX> | Testdatum: |  |
| Testername: |  | Dauer: |  |
| Benutzerrolle(n): |  | Zuständigkeit: | <Geben Sie den Serviceanbieter, einen Kunden oder einen Serviceanbieter zusammen mit einem Kunden an.> |

Zweck

In diesem Abschnitt werden die Schritte zum Pflegen der Zahlungsverbindungsdaten für einen Geschäftspartner beschrieben.

|  |
| --- |
| Nicht vergessen Beispielwerte für Stammdaten sind länder-/regionsspezifisch. Die Werte in der folgenden Tabelle gelten für Deutschland. Ersetzen Sie die länder-/regionsspezifischen Werte von SAP Best Practices for SAP S/4HANA Cloud, Public Edition, oder verwenden Sie die von Ihnen zu diesem Zweck angelegten Stammdatenwerte. |

Vorgehensweise

| Testschrittnummer | Bezeichnung des Testschritts | Anweisungen | Erwartetes Ergebnis | Bestanden/Nicht bestanden/Anmerkung |
| --- | --- | --- | --- | --- |
| 1 | Anmelden | Melden Sie sich am SAP Fiori Launchpad als Stammdatenexperte – Geschäftspartnerdaten an. | Das SAP Fiori Launchpad wird angezeigt. |  |
| 2 | SAP-Fiori-App aufrufen | Öffnen Sie Geschäftspartner pflegen(BP). | Das Bild Geschäftspartner pflegen wird angezeigt. |  |
| 3 | In den Änderungsmodus wechseln | Wählen Sie auf dem Bild Geschäftspartner pflegen die Option GP öffnen. Geben Sie im Dialogfenster die folgenden Daten ein:Geschäftspartner: 10537001Drücken Sie ENTER.Wählen Sie Zwischen Anzeige- und Änderungsmodus wechseln, und geben Sie die folgenden Daten ein:Ändern in GP-Rolle: Wählen Sie TR0151 Kontrahent. | Das Bild Organisation ändern: 10537001, Rolle Kontrahent wird angezeigt. |  |
| 4 | Daten zu "SI: Zahlungsverbindungen" eingeben | Wählen Sie auf dem Bild Organisation ändern: 10537001, Rolle Kontrahent wählen Sie Buchungskreis und geben die folgenden Daten ein:Buchungskreis: z.B. 1010Wählen Sie ENTER und dann SI: Zahlungsverbindungen, und geben Sie die folgenden vier Datenzeilen ein:Zeile 1Währung: z.B. EURZahlver-ID: z.B. EURIHausbank: z.B. DEBK1Konto-ID: z.B. DEAC1Regulierer: z.B. leer lassenPartnerbank: z.B. leer lassenZahlungsanforderung: z.B. entmarkierenZahlwege: z.B. leer lassenZeile 2Währung: z.B. EURZahlver-ID: z.B. EUROHausbank: z.B. DEBK1Konto-ID: z.B. DEAC1Regulierer: z.B. 10537001Partnerbank: z.B. EUR1Zahlungsanordnung: z.B. markierenZahlwege: z.B. TZeile 3Währung: z.B. EURZahlver-ID: z.B. USDIHausbank: z.B. DEBK1Konto-ID: z.B. USDACRegulierer: z.B. leer lassenPartnerbank: z.B. leer lassenZahlungsanforderung: z.B. entmarkierenZahlwege: z.B. leer lassenZeile 4Währung: z.B. EURZahlver-ID: z.B. USDOHausbank: z.B. DEBK1Konto-ID: z.B. USDACRegulierer: z.B. 10537001Partnerbank: z.B. USD1Zahlungsanordnung: z.B.: markierenZahlwege: z.B. FHinweis Bleiben Sie für die nachfolgenden Schritte auf diesem Bild.Hinweis Stellen Sie sicher, dass Sie den Zahlweg in das Feld "Zahlwege" anstelle des Felds "Zahlweg" eingeben.Hinweis Wenn ein Fenster mit der Warnmeldung Geschäftspartner als Regulierer vorgeschlagen (bitte Langtext beachten!)Diese Meldung für diesen Geschäftspartner noch einmal anzeigen?Wählen Sie Nein. | Die SI-Zahlungsverbindungsdaten werden erfasst. |  |
| 5 | Zahlungsverbindungen zuordnen | Ordnen Sie die Zahlungsverbindungen aus dem Bild des vorherigen Schritts zu. Wählen Sie beispielsweise für EUR die Zeile EUR EURI.Wählen Sie Zuordnen im Dialogfenster Kontrahentenänderung: Zuordnung Zahlungsverbindungen.Wählen Sie Alle eingehenden markieren. Als Ergebnis wird EURI unter Z-ID eing. angezeigt.Wählen Sie Weiter, um das Dialogfenster zu schließen.Markieren Sie die Zeile EUR EURO.Wählen Sie Zuordnen im Dialogfenster Kontrahentenänderung: Zuordnung Zahlungsverbindungen.Wählen Sie Alle ausgehenden markieren. Als Ergebnis wird EURO unter Z-ID ausg. angezeigt.Wählen Sie Weiter, um das Dialogfenster zu schließen.Wiederholen Sie die Schritte für USD:USDI: Z-ID eing.USDO: Z-ID ausg.Auf dem Bild Organisation ändern: 10537001, Rolle Kontrahent wählen Sie Sichern. | Die Zahlungsverbindungen und Zuordnungen wurden gesichert. |  |

#### Berechtigungen für Geschäftspartner pflegen

Testverwaltung

Kundenprojekt: Füllen Sie die projektbezogenen Teile aus.

|  |  |  |  |
| --- | --- | --- | --- |
| Testfall-ID | <X.XX> | Testdatum: |  |
| Testername: |  | Dauer: |  |
| Benutzerrolle(n): |  | Zuständigkeit: | <Geben Sie den Serviceanbieter, einen Kunden oder einen Serviceanbieter zusammen mit einem Kunden an.> |

Zweck

In diesem Abschnitt werden die Schritte zum Pflegen der Berechtigungsdaten für einen Geschäftspartner in SAP Treasury and Risk Management beschrieben.

|  |
| --- |
| Nicht vergessen Beispielwerte für Stammdaten sind länder-/regionsspezifisch. Die Werte in der folgenden Tabelle gelten für Deutschland. Ersetzen Sie die länder-/regionsspezifischen Werte von SAP Best Practices for SAP S/4HANA Cloud, Public Edition, oder verwenden Sie die von Ihnen zu diesem Zweck angelegten Stammdatenwerte. |

Vorgehensweise

| Testschrittnummer | Bezeichnung des Testschritts | Anweisungen | Erwartetes Ergebnis | Bestanden/Nicht bestanden/Anmerkung |
| --- | --- | --- | --- | --- |
| 1 | Anmelden | Melden Sie sich am SAP Fiori Launchpad als Stammdatenexperte – Geschäftspartnerdaten an. | Das SAP Fiori Launchpad wird angezeigt. |  |
| 2 | SAP-Fiori-App aufrufen | Öffnen Sie Geschäftspartner pflegen(BP). | Das Bild Geschäftspartner pflegen wird angezeigt. |  |
| 3 | In den Änderungsmodus wechseln | Wählen Sie auf dem Bild Geschäftspartner pflegen die Option GP öffnen. Geben Sie im Dialogfenster die folgenden Daten ein:Geschäftspartner: 10537001Drücken Sie ENTER.Wählen Sie Umschalten zwischen Anzeigen und Ändern, und geben Sie folgende Daten ein:Ändern in GP-Rolle: Wählen Sie TR0151 Kontrahent. | Das Bild Organisation ändern: 10537001, Rolle Kontrahent wird angezeigt. |  |
| 4 | Daten zu "SI: Berechtigungen" eingeben | Wählen Sie auf dem Bild Organisation ändern: 10537001, Rolle Kontrahent die Option Buchungskreis und dann SI: Berechtigungen.Markieren Sie das Ankreuzfeld Berecht. für alle Einträge, und wählen Sie Sichern.Hinweis Sie können die Ordner aufklappen, um die Berechtigung für eine bestimmte Produkt- oder Geschäftsart zu erteilen. Zu Testzwecken werden alle Berechtigungen allen Produkt- und Geschäftsarten zugeordnet. | Die Berechtigungsdaten werden gesichert. |  |

#### Abgeleitete Bewegungen für Geschäftspartner pflegen (optional)

Testverwaltung

Kundenprojekt: Füllen Sie die projektbezogenen Teile aus.

|  |  |  |  |
| --- | --- | --- | --- |
| Testfall-ID | <X.XX> | Testdatum: |  |
| Testername: |  | Dauer: |  |
| Benutzerrolle(n): |  | Zuständigkeit: | <Geben Sie den Serviceanbieter, einen Kunden oder einen Serviceanbieter zusammen mit einem Kunden an.> |

Zweck

In diesem Abschnitt werden die Schritte zum Pflegen der abgeleiteten Bewegungsdaten für einen Geschäftspartner beschrieben. In einigen Ländern führt die Deklaration von Zinserträgen zu einer Sondersteuer, die Sie für Ihren Geschäftspartner berücksichtigen müssen. In diesem Verfahren legen Sie eine länder-/regionsspezifische Zinsabschlagsteuer für Produktart und Geschäftsart fest. Dieser Schritt ist optional.

|  |
| --- |
| Nicht vergessen Beispielwerte für Stammdaten sind länder-/regionsspezifisch. Die Werte in der folgenden Tabelle gelten für Deutschland. Ersetzen Sie die länder-/regionsspezifischen Werte von SAP Best Practices for SAP S/4HANA Cloud, Public Edition, oder verwenden Sie die von Ihnen zu diesem Zweck angelegten Stammdatenwerte. |

Vorgehensweise

| Testschrittnummer | Bezeichnung des Testschritts | Anweisungen | Erwartetes Ergebnis | Bestanden/Nicht bestanden/Anmerkung |
| --- | --- | --- | --- | --- |
| 1 | Anmelden | Melden Sie sich am SAP Fiori Launchpad als Stammdatenexperte – Geschäftspartnerdaten an. | Das SAP Fiori Launchpad wird angezeigt. |  |
| 2 | SAP-Fiori-App aufrufen | Öffnen Sie Geschäftspartner pflegen(BP). | Die App wird geöffnet. |  |
| 3 | In den Änderungsmodus wechseln | Wählen Sie auf dem Bild Geschäftspartner pflegen die Option GP öffnen. Geben Sie im Dialogfenster die folgenden Daten ein:Geschäftspartner: 10537001Drücken Sie ENTER.Wählen Sie Umschalten zwischen Anzeigen und Ändern, und geben Sie folgende Daten ein:Ändern in GP-Rolle: Wählen Sie TR0151 Kontrahent, | Das Bild Organisation ändern: 10537001, Rolle Kontrahent wird angezeigt. |  |
| 4 | Daten zu "SI Abgeleitete Bewegungen" eingeben | Wählen Sie auf dem Bild Organisation ändern: 10537001, Rolle Kontrahent die Option Buchungskreis und dann SI: Abgeleitete Bewegungen, und expandieren Sie: Geldhandel > Zinsgeschäft > 51A Festgeldaufnahme > 100 Anlage.Wählen Sie Zeile eing. markieren/entmark..Im Dialogfenster Verfahren zur Erzeugung abgeleiteter Bewegungen 1 - Eintrag wählen Sie INTDE.Wählen Sie OK.Das Ergebnis wird durch INTDE in der Spalte Verfahren angezeigt.Wählen Sie Sichern. | Die abgeleiteten Bewegungsdaten werden erfasst und gesichert. |  |
| 5 | Für zusätzliche Produkt- und Geschäftsarten wiederholen | Wiederholen Sie den vorherigen Schritt für die folgenden Produkt- und Geschäftsarten:Produktart.…..Geschäftsart52B.…..10053A.…..10053A.…..10153A.…..10254A.…..10055A.…..10058A.…..300Tipp Die Produktarten finden Sie wie folgt:52B unter Geldhandel > Kündigungsgeld53A unter Geldhandel > Commercial Paper54A unter Geldhandel > Finanzstrom-Geschäft55A unter Geldhandel > Zinsgeschäft58A unter Geldhandel > Instrument im Kontokorrentstil |  |  |

#### Meldedaten im Buchungskreis für Geschäftspartner pflegen

Testverwaltung

Kundenprojekt: Füllen Sie die projektbezogenen Teile aus.

|  |  |  |  |
| --- | --- | --- | --- |
| Testfall-ID | <X.XX> | Testdatum: |  |
| Testername: |  | Dauer: |  |
| Benutzerrolle(n): |  | Zuständigkeit: | <Geben Sie den Serviceanbieter, einen Kunden oder einen Serviceanbieter zusammen mit einem Kunden an.> |

Zweck

In diesem Abschnitt werden die Schritte zum Pflegen der Unternehmensbeziehungen für einen Geschäftspartner beschrieben.

|  |
| --- |
| Nicht vergessen Beispielwerte für Stammdaten sind länder-/regionsspezifisch. Die Werte in der folgenden Tabelle gelten für Deutschland. Ersetzen Sie die länder-/regionsspezifischen Werte von SAP Best Practices for SAP S/4HANA Cloud, Public Edition, oder verwenden Sie die von Ihnen zu diesem Zweck angelegten Stammdatenwerte. |

Vorgehensweise

| Testschrittnummer | Bezeichnung des Testschritts | Anweisungen | Erwartetes Ergebnis | Bestanden/Nicht bestanden/Anmerkung |
| --- | --- | --- | --- | --- |
| 1 | Anmelden | Melden Sie sich am SAP Fiori Launchpad als Stammdatenexperte – Geschäftspartnerdaten an. | Das SAP Fiori Launchpad wird angezeigt. |  |
| 2 | SAP-Fiori-App aufrufen | Öffnen Sie Geschäftspartner pflegen(BP). | Das Bild Geschäftspartner pflegen wird angezeigt. |  |
| 3 | In den Änderungsmodus wechseln | Wählen Sie auf dem Bild Geschäftspartner pflegen die Option GP öffnen. Geben Sie im Dialogfenster die folgenden Daten ein:Geschäftspartner: 10537001Drücken Sie ENTER.Wählen Sie Zwischen Anzeige- und Änderungsmodus wechseln, und geben Sie die folgenden Daten ein:Ändern in GP-Rolle: Wählen Sie TR0151 Kontrahent. | Die Sicht Organisation ändern: 10537001, Rolle Kontrahent wird angezeigt. |  |
| 4 | Meldedaten im Buchungskreis erfassen | Wählen Sie auf dem Bild Organisation ändern: 10537001, Rolle Kontrahent die Option Buchungskreis und dann Meldedaten im Buchungskreis.Hinweis Wenn Meldedaten im Buchungskreis nicht angezeigt wird, wählen Sie Navigationsmenü, und wählen Sie den entsprechenden Eintrag im Dropdown-Menü aus.Geben Sie die folgenden Daten ein:UBeziehung: z.B. 3 SonstigeWählen Sie Sichern.Hinweis UBeziehung spiegelt Ihre Beziehung zum Kontrahenten wider.1 Verbunden und konsolidiert2 Verbunden, aber nicht konsolidiert3 Nicht verbunden4 Nicht verwendenDiese Werte werden zur Ableitung der korrekten Sachkonten verwendet. | Die Meldedaten werden erfasst und gesichert. |  |

### Korrespondenzdaten für Geschäftspartner pflegen

SAP Treasury and Risk Management stellt die Standardkorrespondenzfunktion bereit. Über die Korrespondenzfunktion sendet das System bei jedem Sichern eines TRM-Geschäfts eine E-Mai an den Geschäftspartner oder druckt automatisch ein Druckformular über den dafür festgelegten Drucker aus.

Um diese Korrespondenzfunktion zu verwenden, müssen dem Geschäftspartner die folgenden Daten zugeordnet sein:

- Geschäftspartnerprofil
- Geschäftspartnergruppe

#### Profil- und GP-Gruppenzuordnungen zu externen Empfängern bearbeiten

Testverwaltung

Kundenprojekt: Füllen Sie die projektbezogenen Teile aus.

|  |  |  |  |
| --- | --- | --- | --- |
| Testfall-ID | <X.XX> | Testdatum: |  |
| Testername: |  | Dauer: |  |
| Benutzerrolle(n): |  | Zuständigkeit: | <Geben Sie den Serviceanbieter, einen Kunden oder einen Serviceanbieter zusammen mit einem Kunden an.> |

Zweck

Dieses Verfahren beschreibt die Zuordnung von Geschäftspartnerprofilen und Geschäftspartnergruppen zu einem externen Geschäftspartner.

Geschäftspartnerprofile und Geschäftspartnergruppen steuern die Korrespondenzaktivitäten in SAP Treasury and Risk Management.

Die folgenden vordefinierten Geschäftspartnerprofile sind verfügbar:

- PR_EMAIL
- PR_PRINT

Diese vordefinierten Geschäftspartnerprofile können Ihren Geschäftspartnern zugeordnet werden. Wenn beispielsweise die Kommunikation mit Ihrem Geschäftspartner über E-Mail erfolgt, ordnen Sie dem Geschäftspartner das Profil PR_EMAIL zu. Wenn Sie zur Kommunikation gedruckte Belege verwenden, ordnen Sie dem Geschäftspartner PR_PRINT zu.

Die folgende Geschäftspartnergruppe ist vordefiniert:

- BPG_DEFAULT

Ordnen Sie diese Geschäftspartnergruppe Ihrem Geschäftspartner zu. Alternativ können Sie auch über die Konfigurationsschritte Geschäftspartnergruppe definieren und Geschäftspartnergruppen Attribute zuordnen verwenden, um Ihre eigene Geschäftspartnergruppe hinzuzufügen und dann Ihren spezifischen Anforderungen entsprechende Attribute zuordnen. Einem Geschäftspartner können unterschiedliche Geschäftspartnerprofile und Geschäftspartnergruppen zugewiesen werden.

|  |
| --- |
| Nicht vergessen Beispielwerte für Stammdaten sind länder-/regionsspezifisch. Die Werte in der folgenden Tabelle gelten für Deutschland. Ersetzen Sie die länder-/regionsspezifischen Werte von SAP Best Practices for SAP S/4HANA Cloud, Public Edition, oder verwenden Sie die von Ihnen zu diesem Zweck angelegten Stammdatenwerte. |

Vorgehensweise

| Testschrittnummer | Bezeichnung des Testschritts | Anweisung | Erwartetes Ergebnis | Bestanden/Nicht bestanden/Anmerkung |
| --- | --- | --- | --- | --- |
| 1. | Anmelden | Melden Sie sich am SAP Fiori Launchpad als Treasury-Spezialist – Backoffice an. | Das SAP Fiori Launchpad wird angezeigt. |  |
| 2 | SAP-Fiori-App aufrufen | Öffnen Sie Profil und GP-Gruppe zuordnen - Externe Empfänger(FTR_EXT_ASSIGN). | Das Bild Zuordnung von Profilen und GP-Gruppen zu externen Empfängern wird angezeigt. |  |
| 3 | Geschäftspartnerdaten eingeben | Wählen Sie links im Bild Zuordnung von Profilen und GP-Gruppen zu externen Empfängern die Option Zeile einfügen, und geben Sie folgende Daten ein:GeschPartner: z.B. 10537001BuKr: z.B. 1010Empf./Senderart:: z.B. Zeile KONTRAHENT markierenWählen Sie Enter. | Die Geschäftspartnerinformationen sind erfasst. |  |
| 4 | Geschäftsprofil und GP-Gruppe zu Geschäftspartner zuordnen | Wählen Sie oben rechts im Bild Zuordnung von Profilen und GP-Gruppen zu externen Empfängern die Option Knoten expandieren, und expandieren Sie Folgendes:GP:0010537001 /BuKr: 1010 / Empfänger-/Senderart: KONTRAHENT > Geldhandel > Zinsgeschäft > 51A Festgeldaufnahme > 100 Anlage.Wählen Sie 10 Vertrag.Wählen Sie unten rechts im Bild Zuordnung von Profilen und GP-Gruppen zu externen Empfängern die Option Zeile einfügen, und fügen Sie ein E-Mail- oder Druckprofil hinzu:Hinweis Normalerweise ist einer Produktart, Geschäftsart bzw. einem Aktivitätstyp nur ein Profil zugeordnet. Wenn Sie ein weiteres Profil zuordnen möchten, wählen Sie erneut Zeile einfügen, um nach dem ersten Profil ein weiteres Profil hinzufügen.Wenn das Profil E-Mail ist:Profil: z.B. PR_EMAILGP-Gruppe: z.B. BPG_DEFAULTWählen Sie Sichern.Wenn das Profil Druck ist:Profil: z.B. PR_PRINTGP-Gruppe: z.B. BPG_DEFAULTWählen Sie Sichern. | Die GP-Profile und GP-Gruppen werden der Produktart, der Geschäftsart und dem Aktivitätstyp zugeordnet. |  |
| 5 | Für zusätzliche Produktarten, Geschäftsarten, Aktivitätstypen wiederholen | Wählen Sie oben links im Bild die Option Zeile ändern, und wiederholen Sie den vorherigen Schritt, um GP-Profile und GP-Gruppen für die folgenden Produktarten und Geschäfte zuzuordnen:ProduktartGeschäftsartAktivitäts- Kategorie51A1001051A2001052B1001052B1001153A1001053A1011053A1021053A2001053A2011053A2021054A1001054A2001055A1001055A2001055A1001155A2001156A1001056A2001058A3001058A3001160A1012060A1022060A1032060A1042060A1052060A1072060B1032060B1035560B1042060B1045560B1052060B1055560B1102060B1105562A3002062A3012062A3022062B3002062B3012062B3022076A1002076A20020 | Die GP-Profile und GP-Gruppen werden allen aufgelisteten Produktarten, Geschäftsarten und Aktivitätstypen zugeordnet. |  |

#### Zuordnung von Profilen und Geschäftspartnergruppen zu internen Empfängern pflegen

Testverwaltung

Kundenprojekt: Füllen Sie die projektbezogenen Teile aus.

|  |  |  |  |
| --- | --- | --- | --- |
| Testfall-ID | <X.XX> | Testdatum: |  |
| Testername: |  | Dauer: |  |
| Benutzerrolle(n): |  | Zuständigkeit: | <Geben Sie den Serviceanbieter, einen Kunden oder einen Serviceanbieter zusammen mit einem Kunden an.> |

Zweck

Die interne Empfänger-ID ist von SAP vordefiniert. Sie kann mit SAP-Benutzer-IDs verknüpft werden. Wenn eine Verknüpfung zu einer SAP-Benutzer-ID besteht, versucht SAP TRM immer dann, wenn ein internes Korrespondenzobjekt generiert wird, Korrespondenzinformationen an die Adresse der SAP-Benutzer-ID zu senden. In Abhängigkeit von den verschiedenen Profilen (PR_EMAIL oder PR_PRINT) kann entweder eine E-Mail an die E-Mail-Adresse des Benutzers gesendet oder ein Formular ausgedruckt werden.

Dieser Schritt beschreibt die Zuordnung von Geschäftspartnerprofilen und Geschäftspartnergruppen zu einem internen Geschäftspartner.

|  |
| --- |
| Nicht vergessen Beispielwerte für Stammdaten sind länder-/regionsspezifisch. Die Werte in der folgenden Tabelle gelten für Deutschland. Ersetzen Sie die länder-/regionsspezifischen Werte von SAP Best Practices for SAP S/4HANA Cloud, Public Edition, oder verwenden Sie die von Ihnen zu diesem Zweck angelegten Stammdatenwerte. |

Vorgehensweise

| Testschrittnummer | Bezeichnung des Testschritts | Anweisung | Erwartetes Ergebnis | Bestanden/Nicht bestanden/Anmerkung |
| --- | --- | --- | --- | --- |
| 1. | Anmelden | Melden Sie sich am SAP Fiori Launchpad als Treasury-Spezialist – Backoffice an. | Das SAP Fiori Launchpad wird angezeigt. |  |
| 2 | SAP-Fiori-App aufrufen | Öffnen Sie Profil und GP-Gruppe zuordnen - Interne Empfänger(FTR_INT_ASSIGN). | Das Bild Zuordnung von Profilen und GP-Gruppen zu internen Empfängern wird angezeigt. |  |
| 3 | Geschäftspartnerdaten eingeben | Wählen Sie links im Bild Zuordnung von Profilen und GP-Gruppen zu internen Empfängern die Option Zeile einfügen, und geben Sie folgende Daten ein:Nicht vergessen Beispielwerte für Stammdaten sind länder-/regionsspezifisch. Die folgenden Beispielwerte gelten für Deutschland. Ersetzen Sie Ihre länder-/regionsspezifischen Werte von SAP Best Practices for SAP S/4HANA Cloud, Public Edition, oder verwenden Sie die von Ihnen zu diesem Zweck angelegten Stammdatenwerte.Int. Empf.: z.B. INT.EMPF.BuKr: z.B. 1010Empf./Senderart:: z.B. Ankreuzfeld INTERN markierenWählen Sie Enter. | Die Geschäftspartnerinformationen sind erfasst. |  |
| 4 | Geschäftsprofil und GP-Gruppe zu Geschäftspartner zuordnen | Expandieren Sie rechts oben im Bild Zuordnung von Profilen und GP-Gruppen zu internen Empfängern folgenden Menüpfad:GP:INT. EMPF. /BuKr: 1010 / Empfänger-/Senderart: INTERN > Geldhandel > Zinsgeschäft > 51A Festgeldaufnahme > 100 Anlage.Wählen Sie 10 Vertrag.Wählen Sie unten rechts im Bild Zuordnung von Profilen und GP-Gruppen zu internen Empfängern die Option Zeile einfügen.Geben Sie die Profilinformationen für E-Mail oder Druck ein:Profil: z. B. PR_EMAIL für E-MailGP-Gruppe: z.B. BPG_DEFAULTBenutzername: Wählen Sie eine <Benutzer-ID>.Wählen Sie Sichern.Wählen Sie erneut Zeile einfügen, und fügen Sie einen weiteren Eintrag für Druck hinzu:Profil: z. B. PR_DRUCK für die DruckoptionGP-Gruppe: z.B. BPG_DEFAULTBenutzername: Wählen Sie eine <Benutzer-ID>.Hinweis Bei der <Benutzer-ID> handelt es sich um eine Backend-Benutzer-ID.Wählen Sie Sichern. | Das GP-Profil, die GP-Gruppe und die Benutzer-ID werden der Produktart, der Geschäftsart und dem Aktivitätstyp zugeordnet. |  |
| 5 | Für zusätzliche Produktarten, Geschäftsarten, Aktivitätstypen wiederholen | Wählen Sie oben links im Bild die Option Zeile ändern, und wiederholen Sie den vorherigen Schritt, um GP-Profile und GP-Gruppen für die folgenden Produktarten und Geschäfte zuzuordnen:ProduktartGeschäftsartAktivitäts- Kategorie51A1001051A2001052B1001052B1001153A1001053A1011053A1021053A2001053A2011053A2021054A1001054A2001055A1001055A2001055A1001155A2001156A1001056A2001058A3001058A3001160A1012060A1015560A1022060A1025560A1032060A1035560A1042060A1045560A1052060A1055560A1072060A1075560B1032060B1035560B1042060B1045560B1052060B1055560B1102060B1105562A3002062A3012062A3022062B3002062B3012062B3022076A1002076A20020 | GP-Profile, GP-Gruppen und Benutzer-IDs werden allen aufgelisteten Produktarten, Geschäftsarten und Aktivitätstypen zugeordnet. |  |

### Geschäftspartnerstammdaten für Wertpapiere pflegen

Zweck

Legen Sie bei wertpapierbezogenen Finanzinstrumenten, z.B. Geldmarktfonds, zur Erfassung der Grunddaten des Emittenten und der Depotbank die folgenden Geschäftspartnerrollen an:

- TR0150 Emittent
- TR0152 Depotbank

#### Rolle "Emittent" für Geschäftspartner anlegen

Testverwaltung

Kundenprojekt: Füllen Sie die projektbezogenen Teile aus.

|  |  |  |  |
| --- | --- | --- | --- |
| Testfall-ID | <X.XX> | Testdatum: |  |
| Testername: |  | Dauer: |  |
| Benutzerrolle(n): |  | Zuständigkeit: | <Geben Sie den Serviceanbieter, einen Kunden oder einen Serviceanbieter zusammen mit einem Kunden an.> |

Zweck

Dieser Schritt beschreibt die Prozesse zum Anlegen der Rolle "Emittent" für einen Geschäftspartner.

|  |
| --- |
| Nicht vergessen Die Beispielwerte für Stammdatenwerte sind länder-/regionsspezifisch. Ersetzen Sie die länder-/regionsspezifischen Werte von SAP Best Practices for SAP S/4HANA Cloud, Public Edition, oder verwenden Sie die von Ihnen zu diesem Zweck angelegten Stammdatenwerte. |

Vorgehensweise

| Testschrittnummer | Bezeichnung des Testschritts | Anweisungen | Erwartetes Ergebnis | Bestanden/Nicht bestanden/Anmerkung |
| --- | --- | --- | --- | --- |
| 1 | Anmelden | Melden Sie sich am SAP Fiori Launchpad als Stammdatenexperte – Geschäftspartnerdaten an. | Das SAP Fiori Launchpad wird angezeigt. |  |
| 2 | App aufrufen | Öffnen Sie Geschäftspartner pflegen(BP). | Das Bild Geschäftspartner pflegen wird angezeigt. |  |
| 3 | Rolle "Emittent" anlegen | Wählen Sie GP öffnen. Geben Sie im Dialogfenster die folgenden Daten ein:Geschäftspartner: 10537001Drücken Sie ENTER.Wählen Sie Zwischen Anzeige- und Änderungsmodus wechseln, und geben Sie die folgenden Daten ein:Ändern in GP-Rolle: Wählen Sie TR0150 Emittent.und wählen Sie Sichern. | Wählen Sie auf dem Bild Organisation ändern: 10537001 Rolle Emittent wird folgende Meldung angezeigt:Die Änderungen wurden gesichert |  |

#### Rolle "Depotbank" für Geschäftspartner anlegen

Testverwaltung

Kundenprojekt: Füllen Sie die projektbezogenen Teile aus.

|  |  |  |  |
| --- | --- | --- | --- |
| Testfall-ID | <X.XX> | Testdatum: |  |
| Testername: |  | Dauer: |  |
| Benutzerrolle(n): |  | Zuständigkeit: | <Geben Sie den Serviceanbieter, einen Kunden oder einen Serviceanbieter zusammen mit einem Kunden an.> |

Zweck

Dieser Schritt beschreibt die Prozesse zum Anlegen der Rolle "Depotbank" für einen Geschäftspartner.

|  |
| --- |
| Nicht vergessen Beispielwerte für Stammdaten sind länder-/regionsspezifisch. Die folgenden Beispielwerte gelten für Deutschland. Ersetzen Sie die länder-/regionsspezifischen Werte von SAP Best Practices for SAP S/4HANA Cloud, Public Edition, oder verwenden Sie die von Ihnen zu diesem Zweck angelegten Stammdatenwerte. |

Vorgehensweise

| Testschrittnummer | Bezeichnung des Testschritts | Anweisungen | Erwartetes Ergebnis | Bestanden/Nicht bestanden/Anmerkung |
| --- | --- | --- | --- | --- |
| 1 | Anmelden | Melden Sie sich am SAP Fiori Launchpad als Stammdatenexperte – Geschäftspartnerdaten an. | Das SAP Fiori Launchpad wird angezeigt. |  |
| 2 | SAP-Fiori-App aufrufen | Öffnen Sie Geschäftspartner pflegen(BP). | Das Bild Geschäftspartner pflegen wird angezeigt. |  |
| 3 | Depotbankrolle anlegen | Wählen Sie GP öffnen. Geben Sie im Dialogfenster die folgenden Daten ein:Geschäftspartner: 10537001Drücken Sie ENTER.Wählen Sie Zwischen Anzeige- und Änderungsmodus wechseln, und geben Sie die folgenden Daten ein:Ändern in GP-Rolle: Wählen Sie TR0152 Depotbank,und wählen Sie Sichern. | Auf dem Bild Organisation ändern: 10537001, Rolle Depotbank wird folgende Meldung angezeigt:Änderungen wurden gesichert. |  |

### Geschäftspartnerstammdaten für Akkreditiv pflegen

#### Bankrolle für Geschäftspartner anlegen

Testverwaltung

Kundenprojekt: Füllen Sie die projektbezogenen Teile aus.

|  |  |  |  |
| --- | --- | --- | --- |
| Testfall-ID | <X.XX> | Testdatum: |  |
| Testername: |  | Dauer: |  |
| Benutzerrolle(n): |  | Zuständigkeit: | <Geben Sie den Serviceanbieter, einen Kunden oder einen Serviceanbieter zusammen mit einem Kunden an.> |

Vorgehensweise

| Testschrittnummer | Bezeichnung des Testschritts | Anweisungen | Erwartetes Ergebnis | Bestanden/Nicht bestanden/Anmerkung |
| --- | --- | --- | --- | --- |
| 1 | Im SAP Fiori Launchpad anmelden | Melden Sie sich am SAP Fiori Launchpad als Stammdatenexperte – Geschäftspartnerdaten an. | Das SAP Fiori Launchpad wird angezeigt. |  |
| 2 | App aufrufen | Öffnen Sie Geschäftspartner pflegen(BP). | Das Bild Geschäftspartner pflegen wird angezeigt. |  |
| 3 | Bankrolle anlegen | Wählen Sie GP öffnen. Geben Sie im Dialogfenster die folgenden Daten ein:Geschäftspartner: 10537001Drücken Sie ENTER.Wählen Sie Zwischen Anzeige- und Änderungsmodus wechseln, und geben Sie die folgenden Daten ein:Ändern in GP-Rolle: Wählen Sie TR0703 Bank aus,und wählen Sie Sichern. | Auf dem Bild Organisation ändern: 10537001, Rolle Bank wird die folgende Benachrichtigung angezeigt:Änderungen wurden gesichert. |  |

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
- related-to :: [[05-treasury-and-cash-management/create-business-partner-for-treasury-and-risk-management-mds-22g-257]]
- related-to :: [[05-treasury-and-cash-management/mds-22g-259]]
- related-to :: [[05-treasury-and-cash-management/mds-22g-261]]
- related-to :: [[05-treasury-and-cash-management/script-de-dados-mestre-criar-parceiro-de-negocios-para-o-treasury-and]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/22G_S4CLD2608_Master_Data_DE_XX.docx` — full document · extracted with `mammoth` · 42,763 chars in the whole document
