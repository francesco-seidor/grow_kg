---
id: 11-inventory-warehouse-and-transportation/stammdatenskript-spediteurstamm-anlegen-sds-4de-406
title: "Stammdatenskript: Spediteurstamm anlegen – SDS (4DE) (4DE_S4CLD2608_Master_Data_DE_XX)"
description: "German SAP S/4HANA Cloud Public Edition 2608 master data script: creating carrier/forwarder business partners (road, rail, sea, air, forwarder) for invoice verification and ERS."
cluster: 11-inventory-warehouse-and-transportation
tags: [kb/inventory-warehouse-and-transportation, topic/carrier-master-data]
aliases: [4DE_S4CLD2608_Master_Data_DE_XX]
keywords: [Carrier Business Partners, carrier business partner, freight forwarder master data, invoice verification, evaluated receipt settlement, business partner roles, road carrier, rail carrier, ocean carrier, air carrier]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/4DE_S4CLD2608_Master_Data_DE_XX.docx]
confidence: low
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-406
topic: 11-inventory-warehouse-and-transportation/carrier-master-data
language: DE
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Stammdatenskript: Spediteurstamm anlegen – SDS (4DE) (4DE_S4CLD2608_Master_Data_DE_XX)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/4DE_S4CLD2608_Master_Data_DE_XX.docx`, extracted with `mammoth`. Grouped under **Carrier Business Partners** in Inventory, Warehouse and Transportation. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

| <!-- image omitted: unnamed --> | StammdatenskriptSAP S/4HANA Cloud Public Edition - 02-07-26 |
| --- | --- |
|  | Spediteurstamm anlegen – SDS (4DE) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Inhaltsverzeichnis

[1 Zweck 2](#_Toc233889731)

[2 Voraussetzungen 3](#_Toc233889732)

[2.1 Systemzugriff 3](#_Toc233889733)

[2.2 Rollen 3](#_Toc233889734)

[2.3 Erforderliche Organisationseinheiten 3](#_Toc233889735)

[2.4 Wesentliche Parameter für die Datenerstellung 4](#_Toc233889736)

[2.4.1 Gruppierungen 4](#_Toc233889737)

[3 Übersichtstabelle 5](#_Toc233889738)

[4 Vorgehensweise 6](#_Toc233889739)

[4.1 Geschäftspartner Spediteur (Straße) für Rechnungsprüfungsprozess anlegen 6](#_Toc233889740)

[4.2 Geschäftspartner Spediteur (Straße) für die automatische Wareneingangsabrechnung (ERS) anlegen 10](#_Toc233889741)

[4.3 Geschäftspartner Spediteur (Bahn) für Rechnungsprüfungsprozess anlegen 14](#_Toc233889742)

[4.4 Geschäftspartner Spediteur (Bahn) für die automatische Wareneingangsabrechnung (ERS) anlegen 17](#_Toc233889743)

[4.5 Geschäftspartner Spediteur (See) für Rechnungsprüfungsprozess anlegen 21](#_Toc233889744)

[4.6 Geschäftspartner Spediteur (See) für die automatische Wareneingangsabrechnung (ERS) anlegen 25](#_Toc233889745)

[4.7 Geschäftspartner Spediteur für Rechnungsprüfungsprozess anlegen 29](#_Toc233889746)

[4.8 Geschäftspartner (Spediteur) für die automatische Wareneingangsabrechnung (ERS) anlegen 33](#_Toc233889747)

[4.9 Geschäftspartner Spediteur (Luft) für Rechnungsprüfungsprozess anlegen 36](#_Toc233889748)

[4.10 Geschäftspartner Spediteur (Luft) für die automatische Wareneingangsabrechnung (ERS) anlegen 40](#_Toc233889749)

[5 Anhang 45](#_Toc233889750)

## Zweck

Dieses Dokument beschreibt, wie Sie einen Geschäftspartner-Frachtführer für Ihr SAP S/4HANA-System anlegen. Die Beschreibung umfasst die Datensegmente, die für die SAP S/4HANA Appliance relevant sind, z.B. Geschäftspartnerrollen und andere relevante Felder. Felder, die für die von SAP Best Practices bereitgestellten SAP-S/4HANA-Inhalte nicht relevant sind, werden in diesem Dokument nicht behandelt.

Ein Frachtführer ist ein Geschäftspartner, der für den Transport von Waren zuständig ist. Ein Frachtführer kann Verladern oder Spediteuren Services anbieten.

## Voraussetzungen

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
| Stammdatenexperte – Geschäftspartnerdaten | SAP_BR_BUPA_MASTER_SPECIALIST | Stammdaten – Geschäftspartner / Geschäftspartner-Governance / Geschäftspartner-Governance / Geschäftspartner-Governance | SAP_BR_BUPA_MASTER_SPECIALIST / SAP_CA_SPT_MDG_BP_GOV_PC / SAP_CMD_SPT_BP_GOV_PC / SAP_CA_SPT_MDG_BP_WFUSR_PC |

### Erforderliche Organisationseinheiten

Einige Segmente der Stammdaten hängen von den Organisationseinheiten des Unternehmens ab. Allgemeine (zentrale) Daten sind nicht von einer Organisationseinheit oder dem Buchungskreis abhängig. Die folgende Tabelle stellt eine Übersicht dieser verschiedenen Datensegmente und ihrer relevanten Organisationseinheiten bereit:

| Datensegment | Hängt ab von | Feldbeispiele | Kommentare | Zu verwendende Organisationseinheit |
| --- | --- | --- | --- | --- |
| Einkaufsdaten (Materialwirtschaft) | Einkaufsorganisation |  |  |  |
| Buchungskreis | Buchungskreis |  |  |  |

### Wesentliche Parameter für die Datenerstellung

In diesem Abschnitt werden einige Basisparameter erläutert, die das Verhalten eines Stammsatzes beeinflussen und immer für das Anlegen eines Materialstammdatensatzes eines Geschäftspartner-Frachtführers erforderlich sind.

#### Gruppierungen

Für Geschäftspartner-Frachtführer werden folgende Gruppierungen definiert:

| Gruppierung | Bereich/IDs | Kommentare |
| --- | --- | --- |
| Externe numerische Nummerierung (oberer Bereich) | BP03 |  |

## Übersichtstabelle

Dieser Stammdatensatz umfasst mehrere Segmente, die in der nachfolgenden Tabelle genannt sind.

|  |
| --- |
| Hinweis Wenn Ihr Systemadministrator Bereiche und Seiten auf dem SAP Fiori Launchpad aktiviert hat, enthält die Startseite nur die wesentlichen Apps, mit denen die typischen Aufgaben einer Benutzerrolle ausgeführt werden können.Alle anderen (suchbaren) Apps, die nicht auf der Startseite enthalten sind, finden Sie über die Suchleiste ([2434549](https://me.sap.com/notes/2434549)).Wenn Sie die Startseite personalisieren und versteckte Apps hinzufügen möchten, wechseln Sie in Ihr Benutzerprofil und wählen Sie App Finder. |

| Segment | Anwendungsrolle | App/Vorgang | Erwartete Ergebnisse |
| --- | --- | --- | --- |
| [Geschäftspartner Spediteur (Straße) für Rechnungsprüfungsprozess anlegen](#unique_8) [Seite ] 6 | Stammdatenexperte – Geschäftspartnerdaten | Geschäftspartner pflegen(BP) | Der Geschäftspartner-Frachtführer wird angelegt. |

## Vorgehensweise

Dieser Abschnitt beschreibt die Vorgehensweisen für jedes Segment oder Prozessschritt, das bzw. der Teil eines anderen Geschäftsablaufs ist. Rechnungsprüfungsprozess und Gutschriftsverfahren.

### Geschäftspartner Spediteur (Straße) für Rechnungsprüfungsprozess anlegen

Testverwaltung

Kundenprojekt: Füllen Sie die projektbezogenen Teile aus.

|  |  |  |  |
| --- | --- | --- | --- |
| Testfall-ID | <X.XX> | Testdatum: |  |
| Testername: |  | Dauer: |  |
| Benutzerrolle(n): |  | Zuständigkeit: | <Geben Sie den Serviceanbieter, einen Kunden oder einen Serviceanbieter zusammen mit einem Kunden an.> |

Zweck

Legen Sie einen Geschäftspartner-Frachtführer für die Transportausführung an. Der Frachtführer wird einem Transportauftrag (Frachtauftrag) zugeordnet. Dieser Frachtführer wird hauptsächlich im Rechnungsprüfungsprozess verwendet, wenn die Beträge der Spediteurrechnung mit den im Frachtauftrag berechneten erwarteten Transportkosten verglichen werden.

Vorgehensweise

| Testschrittnummer | Bezeichnung des Testschritts | Anweisungen | Erwartetes Ergebnis | Kommentare |
| --- | --- | --- | --- | --- |
| 1 | Anmelden | Melden Sie sich am SAP Fiori Launchpad als Stammdatenexperte – Geschäftspartnerdaten an. | Die Startseite wird angezeigt. |  |
| 2 | SAP-Fiori-App aufrufen | Geschäftspartner pflegen(BP) | Es wird ein neues Fenster mit dem Bild Geschäftspartner bearbeiten geöffnet. |  |
| 3 | GP-Organisation anlegen | Wählen Sie Organisation. | Das Bild Organisation anlegen wird angezeigt. |  |
| 4 | Allgemeine Daten eingeben | Tragen Sie Folgendes ein:Geschäftspartner: <Geben Sie eine mit einem Buchstaben beginnende Geschäftspartner-ID ein.>Gruppierung: <externe alphanumerische Nummerierung>Das Feld Anlegen in GP-Rolle wird vom System mit der Rolle GPartner allgemein ausgefüllt. Behalten Sie diese Einstellung bei. Geben Sie auf der Registerkarte Adresse die folgenden Informationen ein:Name: <Name der Organisation>Suchbegriff: <Suchbegriff für den Geschäftspartner>Hinweis Beispielwerte mit US-Lokalisierung für die oben genannten Felder:Geschäftspartner: <17386001>Gruppierung: <Externe numerische Nummerierung (oberer Bereich) (BP03)>Name: <TM Straßenspediteur US 1>Suchbegriff: <TMSTRASSENSPEDUS> |  |  |
| 5 | Identifikationsdaten eingeben | Geben Sie für die Rolle des Geschäftspartners auf der Registerkarte Identifikation die folgenden Informationen ein:Rechtsform: <Rechtsform der Organisation>Beispielwerte für das obige Feld: Rechtsform: <01 (Körperschaft)>Sichern Sie Ihre Eingaben. |  |  |
| 6 | Neue Rolle "Frachtführer" zuordnen und Adressdaten eingeben | Wählen Sie Umschalten zwischen Anzeigen und Ändern, um sicherzustellen, dass der Änderungsmodus aktiviert ist. Ordnen Sie die neue GP-Rolle Frachtführer (CRM010) zu, indem Sie die Rolle über die Auswahlliste Ändern in GP-Rolle auswählen.Geben Sie auf der Registerkarte Adresse für die GP-Rolle einen Frachtführer mit den folgenden Informationen ein:Straße: <Straßenname>Postleitzahl/Ort: <Postleitzahl des Orts>Ort: <Ortsname>Land: <Ländername>Region (Bundesland, Provinz, Kreis): <Regionsname>Zeitzone: <Zeitzone>Sprache: <Name der Sprache>Telefon (Vorwahl + Anschluss): <Telefonnummer mit Ortsvorwahl>E-Mail: <E-Mail-Adresse>Hinweis Beispielwerte mit US-Lokalisierung für die oben genannten Felder:Straße: <WindgapAve>Postleitzahl/Ort: <95206>Ort: <Pittsburgh>Land: <US>Region (Bundesland, Provinz, Kreis): <PA>Zeitzone: <EST>Sprache: <EN>Telefon (Vorwahl + Anschluss): <412-264-5632>E-Mail: <info@17386001.com> |  |  |
| 7 | Zahlungsverkehrsdaten für Rolle "Frachtführer" eingeben | Geben Sie für die GP-Rolle "Frachtführer" auf der Registerkarte Zahlungsverkehr die folgenden Informationen ein:Land: <Bankschlüssel>Bankschlüssel: <Bankschlüssel>Bankkonto: <Kontonummer>Sichern Sie Ihre Eingaben.Hinweis Beispielwerte mit US-Lokalisierungen für die oben genannten Felder:Land: <US>Bankschlüssel: <150350300>Bankkonto: <790133> |  |  |
| 8 | Neue Rolle "Lieferant" zuordnen und Geschäftspartnerdaten eingeben | Ordnen Sie die neue GP-Rolle Lieferant (FLVN01) zu, indem Sie die Rolle über die Auswahlliste Ändern in GP-Rolle auswählen. Führen Sie dann die folgenden Schritte durch:Wählen Sie Einkauf.Geben Sie den folgenden Wert in das Feld Einkaufsorganisation ein: <Einkaufsorganisation>Bestätigen Sie mit Enter.Machen Sie auf der Registerkarte Einkaufsdaten folgende Angaben:Bestellwährung: <Währungsbezeichnung>Zahlungsbedingungen: <Zahlungsbedingungen>Versandbedingungen: <Name der Versandbedingung>Einkäufergruppe: <Wert der Einkäufergruppe>Schemagr. Lief.: <Wert>Sichern Sie Ihre Eingaben.Hinweis Beispielwerte mit US-Lokalisierung für die oben genannten Felder:Bestellwährung: <USD>Zahlungsbedingungen: <0004>Versandbedingungen: <01>Einkäufergruppe: <005>Schemagr. Lief.: <03> |  |  |
| 9 | Neue Rolle "Kreditor FI" zuordnen und Geschäftspartnerdaten eingeben | Ordnen Sie die neue GP-Rolle Kreditor (Finanzbuchhaltung) (FLVN00) zu, indem Sie die Rolle über folgende Auswahlliste auswählen:Ändern in GP-RolleWählen Sie Buchungskreis.Geben Sie den Buchungskreis ein: <Buchungskreis>:Wählen Sie Enter.Geben Sie auf der entsprechenden Registerkarte die folgenden Informationen ein:Registerkarte Kreditor: Kontoverwaltung.Abstimmkonto: <Kontonummer>Sortierschlüssel: <Wert>Hinweis Beispielwerte mit US-Lokalisierung für die oben genannten Felder:Buchungskreis: <1710>Abstimmkonto: <21100000>Sortierschlüssel: <009> |  |  |
| 10 | Lieferantenkorrespondenzdaten eingeben | Geben Sie auf der Registerkarte Kreditorenkorrespondenz die folgenden Informationen ein:Sachb.-Kürzel: <Wert>Konto beim Lieferanten: <Wert>Hinweis Beispielwerte mit US-Lokalisierung für die oben genannten Felder:Sachb.-Kürzel: <01>Konto beim Lieferanten: <1710-CARR1> |  |  |
| 11 | Daten sichern | Wählen Sie Sichern. | Eine Systemmeldung bestätigt, dass das Objekt gesichert wurde. |  |

### Geschäftspartner Spediteur (Straße) für die automatische Wareneingangsabrechnung (ERS) anlegen

Testverwaltung

Kundenprojekt: Füllen Sie die projektbezogenen Teile aus.

|  |  |  |  |
| --- | --- | --- | --- |
| Testfall-ID | <X.XX> | Testdatum: |  |
| Testername: |  | Dauer: |  |
| Benutzerrolle(n): |  | Zuständigkeit: | <Geben Sie den Serviceanbieter, einen Kunden oder einen Serviceanbieter zusammen mit einem Kunden an.> |

Zweck

Legen Sie einen Geschäftspartner-Frachtführer für die Transportausführung an. Der Frachtführer wird einem Transportauftrag (Frachtauftrag) zugeordnet. Dieser Frachtführer wird vor allem für das Szenario "Automatische Wareneingangsabrechnung (ERS)" verwendet, in dem die automatische Rechnungsabrechnung erfolgt, ohne auf eine Spediteurrechnung zu warten.

Vorgehensweise

| Testschrittnummer | Bezeichnung des Testschritts | Anweisungen | Erwartetes Ergebnis | Kommentare |
| --- | --- | --- | --- | --- |
| 1 | Anmelden | Melden Sie sich am SAP Fiori Launchpad als Stammdatenexperte - Geschäftspartnerdaten an. | Die Startseite wird angezeigt. |  |
| 2 | SAP-Fiori-App aufrufen | Wählen Sie Geschäftspartner pflegen(BP). | Das Bild Geschäftspartner pflegen(BP) wird angezeigt. |  |
| 3 | GP-Organisation anlegen | Wählen Sie Organisation. | Das Bild Organisation anlegen wird angezeigt. |  |
| 4 | Allgemeine Daten eingeben | Tragen Sie Folgendes ein:Geschäftspartner: <Geben Sie eine mit einem Buchstaben beginnende Geschäftspartner-ID ein.>Gruppierung: <externe alphanumerische Nummerierung>Das Feld Anlegen in GP-Rolle wird vom System mit der Rolle GPartner allgemein ausgefüllt. Behalten Sie diese Einstellung bei.Geben Sie auf der Registerkarte Adresse die folgenden Informationen ein:Name: <Name der Organisation>Suchbegriff: <Suchbegriff für den Geschäftspartner>Hinweis Siehe Abschnitt "Stammdaten", "Organisationsdaten" und "Sonstige Daten" für die Auswahl der richtigen Werte im Szenario "3EP – Auftragsbasierte Transportkonsolidierung".Beispielwerte für die zuvor aufgeführten Felder:Geschäftspartner: <17386002>Gruppierung: <Externe numerische Nummerierung (oberer Bereich) (BP03)>Name: <TM Straßenspediteur Gutschriftsverfahren US>Suchbegriff: <TMSTRASSENSPEDGUTUS> |  |  |
| 5 | Identifikationsdaten eingeben | Geben Sie für die Rolle des Geschäftspartners auf der Registerkarte Identifikation die folgenden Informationen ein:Rechtsform: <Rechtsform der Organisation>Beispielwerte für das obige Feld:Rechtsform: <01 (Körperschaft)>Sichern Sie Ihre Eingaben. |  |  |
| 6 | Neue Rolle "Frachtführer" zuordnen und Adressdaten eingeben | Wählen Sie die Drucktaste Umschalten zwischen Anzeigen und Ändern, um sicherzustellen, dass der "Änderungsmodus" aktiviert ist. Ordnen Sie die neue GP-Rolle Frachtführer (CRM010) zu, indem Sie die Rolle über die Auswahlliste "Ändern in GP-Rolle" auswählen.Geben Sie auf der Registerkarte Adresse die folgenden Informationen ein:Straße: <Straßenname>Postleitzahl/Ort: <Postleitzahl/Ort>Ort: <Name des Orts>Land: <Name des Landes>Region (Bundesland, Provinz): <Name der Region>Zeitzone: <Zeitzone>Sprache: <Sprache>Telefon (Vorwahl + Anschluss): <Telefonnummer mit Vorwahl>E-Mail: <E-Mail-Adresse>Hinweis Beispielwerte für die zuvor aufgeführten Felder:Straße: <E Sweet Ave>Postleitzahl/Ort: <58504>Ort: <Bismarck>Land: <US>Region (Bundesland, Provinz): <ND>Zeitzone: <MST>Sprache: <EN>Telefon (Vorwahl + Anschluss): <999 254 3623>E-Mail: <info@17386002.com> | Die Geschäftspartnerrolle "Frachtführer" wird hinzugefügt. |  |
| 7 | Zahlungsverkehrsdaten für Rolle "Frachtführer" eingeben | Geben Sie auf der Registerkarte Zahlungsverkehr die folgenden Informationen ein:Land: <Bankschlüssel>Bankschlüssel: <Bankschlüssel>Bankkonto: <Kontonummer>Sichern Sie Ihre Eingaben.Hinweis Beispielwerte für die zuvor aufgeführten Felder:Land: <US>Bankschlüssel: <150350300>Bankkonto: <102610> |  |  |
| 8 | Neue Rolle "Lieferant" zuordnen und Geschäftspartnerdaten eingeben | Ordnen Sie die neue GP-Rolle Lieferant (FLVN01) zu, indem Sie die Rolle über die Auswahlliste "Ändern in GP-Rolle" auswählen.Wählen Sie Einkauf.Geben Sie den Wert in das Feld Einkaufsorganisation: <Einkaufsorganisation> ein.Wählen Sie Enter.Machen Sie auf der Registerkarte Einkaufsdaten folgende Angaben:Bestellwährung: <Währungsbezeichnung>Zahlungsbedingungen: <Zahlungsbedingungen>Versandbedingungen: <Name der Versandbedingung>Einkäufergruppe: <Wert>Schemagr. Lief.: <Wert>Auto WEAbr Lieferung: <markieren>Sichern Sie Ihre Eingaben.Hinweis Beispielwerte für die zuvor aufgeführten Felder:Einkaufsorganisation: <1710>Bestellwährung: <USD>Zahlungsbedingungen: <0004>Versandbedingungen: <01>Einkäufergruppe: <005>Schemagr. Lief.: <03>Auto WEAbr Lieferung: <markieren> |  |  |
| 9 | Neue Rolle "Lieferant FI" zuordnen und Geschäftspartnerdaten eingeben | Ordnen Sie die neue GP-Rolle Lieferant (Finanzbuchh.) (FLVN00) zu, indem Sie die Rolle über die Auswahlliste "Ändern in GP-Rolle" auswählen.Wählen Sie Buchungskreis.Geben Sie den Buchungskreis ein: <Buchungskreis>:Wählen Sie Enter.Geben Sie die folgenden Informationen auf der Registerkarte Lieferant: Kontoführung ein:Abstimmkonto: <Kontonummer>Sortierschlüssel: <Wert>Hinweis Beispielwerte für die zuvor aufgeführten Felder:Buchungskreis: <1710>Abstimmkonto: <21100000>Sortierschlüssel: <009> |  |  |
| 10 | Lieferantenkorrespondenzdaten eingeben | Geben Sie die folgenden Informationen auf der Registerkarte Lieferant: Korrespondenz ein:Sachb.-Kürzel: <Wert>Konto beim Lieferanten: <Wert>Hinweis Beispielwerte für die zuvor aufgeführten Felder:Sachb.-Kürzel: <01>Konto beim Lieferanten: <1710-CARR2>. |  |  |
| 11 | Daten sichern | Wählen Sie Sichern. | Eine Systemmeldung bestätigt, dass das Objekt gesichert wurde. |  |

### Geschäftspartner Spediteur (Bahn) für Rechnungsprüfungsprozess anlegen

Testverwaltung

Kundenprojekt: Füllen Sie die projektbezogenen Teile aus.

|  |  |  |  |
| --- | --- | --- | --- |
| Testfall-ID | <X.XX> | Testdatum: |  |
| Testername: |  | Dauer: |  |
| Benutzerrolle(n): |  | Zuständigkeit: | <Geben Sie den Serviceanbieter, einen Kunden oder einen Serviceanbieter zusammen mit einem Kunden an.> |

Zweck

Legen Sie einen Geschäftspartner-Frachtführer für die Transportausführung an. Der Frachtführer wird einem Transportauftrag (Frachtauftrag) zugeordnet. Dieser Frachtführer wird hauptsächlich im Rechnungsprüfungsprozess verwendet, wenn die Beträge der Spediteurrechnung mit den im Frachtauftrag berechneten erwarteten Transportkosten verglichen werden.

Vorgehensweise

| Testschrittnummer | Bezeichnung des Testschritts | Anweisung | Erwartetes Ergebnis | Kommentare |
| --- | --- | --- | --- | --- |
| 1 | Anmelden | Melden Sie sich am SAP Fiori Launchpad als Stammdatenexperte – Geschäftspartnerdaten an. | Die Startseite wird angezeigt. |  |
| 2 | SAP-Fiori-App aufrufen | Geschäftspartner pflegen (BP) | Es wird ein neues Fenster mit dem Bild Geschäftspartner pflegen geöffnet. |  |
| 3 | GP-Organisation anlegen | Wählen Sie Organisation. | Das Bild Organisation anlegen wird angezeigt. |  |
| 4 | Allgemeine Daten erfassen | Geben Sie Folgendes ein:Geschäftspartner: <Geben Sie eine mit einem Buchstaben beginnende Geschäftspartner-ID ein.>Gruppierung: <externe alphanumerische Nummerierung>Das Feld Anlegen in GP-Rolle wird vom System mit der Rolle GPartner allgemein ausgefüllt. Behalten Sie diese Einstellung bei. Geben Sie auf der Registerkarte Adresse die folgenden Informationen ein:Name: <Name der Organisation>Suchbegriff: <Suchbegriff für den Geschäftspartner>Beispielwerte mit US-Lokalisierung für die oben genannten Felder:Geschäftspartner: <17386201>Gruppierung: <Externe numerische Nummerierung (oberer Bereich) (BP03)>Name: <TM Bahnspediteur US 1>Suchbegriff:<TMBAHNSPEDUS1> |  |  |
| 5 | Identifikationsdaten eingeben | Geben Sie für die Rolle des Geschäftspartners auf der Registerkarte Identifikation die folgenden Informationen ein:Rechtsform: <Rechtsform der Organisation>Beispielwerte für das obige Feld: Rechtsform: <01 (Körperschaft)>Sichern Sie Ihre Eingaben. |  |  |
| 6 | Neue Rolle "Frachtführer" zuordnen und Adressdaten eingeben | Wählen Sie Umschalten zwischen Anzeigen und Ändern, um sicherzustellen, dass der Änderungsmodus aktiviert ist. Ordnen Sie die neue GP-Rolle Frachtführer (CRM010) zu, indem Sie die Rolle über die Auswahlliste Ändern in GP-Rolle auswählen.Geben Sie auf der Registerkarte Adresse für die GP-Rolle einen Frachtführer mit den folgenden Informationen ein:Straße: <Straßenname>Postleitzahl/Ort: <Postleitzahl des Orts>Ort: <Ortsname>Land: <Ländername>Region (Bundesland, Provinz, Kreis): <Regionsname>Zeitzone: <Zeitzone>Sprache: <Name der Sprache>Telefon (Vorwahl + Anschluss): <Telefonnummer mit Ortsvorwahl>E-Mail: <E-Mail-Adresse>Beispielwerte mit US-Lokalisierung für die oben genannten Felder:Straße: <WindgapAve>Postleitzahl/Ort: <95206>Ort: <Pittsburgh>Land: <US>Region (Bundesland, Provinz, Kreis): <PA>Zeitzone: <EST>Sprache: <EN>Telefon (Vorwahl + Anschluss): <412-264-5632>E-Mail: <info@17386201.com> |  |  |
| 7 | Zahlungsverkehrsdaten für Rolle "Frachtführer" eingeben | Geben Sie für die GP-Rolle "Frachtführer" auf der Registerkarte Zahlungsverkehr die folgenden Informationen ein:Land: <Bankschlüssel>Bankschlüssel: <Bankschlüssel>Bankkonto: <Kontonummer>Sichern Sie Ihre Eingaben.Beispielwerte mit US-Lokalisierungen für die oben genannten Felder:Land: <US>Bankschlüssel: <150350300>Bankkonto: <790133> |  |  |
| 8 | Neue Rolle "Lieferant" zuordnen und Geschäftspartnerdaten eingeben | Ordnen Sie die neue GP-Rolle Lieferant (FLVN01) zu, indem Sie die Rolle über die Auswahlliste Ändern in GP-Rolle auswählen. Führen Sie dann die folgenden Schritte durch:Wählen Sie Einkauf.Geben Sie den folgenden Wert in das Feld Einkaufsorganisation ein: <Einkaufsorganisation>Bestätigen Sie mit Enter.Machen Sie auf der Registerkarte Einkaufsdaten folgende Angaben:Bestellwährung: <Währungsbezeichnung>Zahlungsbedingungen: <Zahlungsbedingungen>Versandbedingungen: <Name der Versandbedingung>Einkäufergruppe: <Wert der Einkäufergruppe>Schemagr. Lief.: <Wert>Sichern Sie Ihre Eingaben.Beispielwerte mit US-Lokalisierung für die oben genannten Felder:Bestellwährung: <USD>Zahlungsbedingungen: <0004>Versandbedingungen: <01>Einkäufergruppe: <005>Schemagr. Lief.: <03> |  |  |
| 9 | Neue Rolle "Kreditor FI" zuordnen und Geschäftspartnerdaten eingeben | Ordnen Sie die neue GP-Rolle Kreditor (Finanzbuchhaltung) (FLVN00) zu, indem Sie die Rolle über folgende Auswahlliste auswählen:Ändern in GP-RolleWählen Sie Buchungskreis.Geben Sie den Buchungskreis ein: <Buchungskreis>Wählen Sie Enter.Geben Sie auf der entsprechenden Registerkarte die folgenden Informationen ein:Registerkarte Kreditor: Kontoverwaltung.Abstimmkonto: <Kontonummer>Sortierschlüssel: <Wert>Beispielwerte mit US-Lokalisierung für die oben genannten Felder:Buchungskreis: <1710>Abstimmkonto: <21100000>Sortierschlüssel: <009> |  |  |
| 10 | Lieferantenkorrespondenzdaten eingeben | Geben Sie auf der Registerkarte Kreditorenkorrespondenz die folgenden Informationen ein:Sachb.-Kürzel: <Wert>Konto beim Lieferanten: <Wert>Beispielwerte mit US-Lokalisierung für die oben genannten Felder:Sachb.-Kürzel: <01>Konto beim Lieferanten: <1710-CARR201> |  |  |
| 11 | Daten sichern | Wählen Sie Sichern. | Eine Systemmeldung bestätigt, dass das Objekt gesichert wurde. |  |

### Geschäftspartner Spediteur (Bahn) für die automatische Wareneingangsabrechnung (ERS) anlegen

Testverwaltung

Kundenprojekt: Füllen Sie die projektbezogenen Teile aus.

|  |  |  |  |
| --- | --- | --- | --- |
| Testfall-ID | <X.XX> | Testdatum: |  |
| Testername: |  | Dauer: |  |
| Benutzerrolle(n): |  | Zuständigkeit: | <Geben Sie den Serviceanbieter, einen Kunden oder einen Serviceanbieter zusammen mit einem Kunden an.> |

Zweck

Legen Sie einen Geschäftspartner-Frachtführer für die Transportausführung an. Der Frachtführer wird einem Transportauftrag (Frachtauftrag) zugeordnet. Dieser Frachtführer wird vor allem für das Szenario "Automatische Wareneingangsabrechnung (ERS)" verwendet, in dem die automatische Rechnungsabrechnung erfolgt, ohne auf eine Spediteurrechnung zu warten.

Vorgehensweise

| Testschrittnummer | Bezeichnung des Testschritts | Anweisung | Erwartetes Ergebnis | Kommentare |
| --- | --- | --- | --- | --- |
| 1 | Anmelden | Melden Sie sich am SAP Fiori Launchpad als Stammdatenexperte - Geschäftspartnerdaten an. | Die Startseite wird angezeigt. |  |
| 2 | SAP-Fiori-App aufrufen | Wählen Sie Geschäftspartner pflegen (BP). | Das Bild Geschäftspartner pflegen (BP) wird angezeigt. |  |
| 3 | GP-Organisation anlegen | Wählen Sie Organisation. | Das Bild Organisation anlegen wird angezeigt. |  |
| 4 | Allgemeine Daten erfassen | Geben Sie Folgendes ein:Geschäftspartner: <Geben Sie eine mit einem Buchstaben beginnende Geschäftspartner-ID ein.>Gruppierung: <externe alphanumerische Nummerierung>Das Feld Anlegen in GP-Rolle wird vom System mit der Rolle GPartner allgemein ausgefüllt. Behalten Sie diese Einstellung bei.Geben Sie auf der Registerkarte Adresse die folgenden Informationen ein:Name: <Name der Organisation>Suchbegriff: <Suchbegriff für den Geschäftspartner>Siehe Abschnitt "Stammdaten", "Organisationsdaten" und "Sonstige Daten" für die Auswahl der richtigen Werte im Szenario "3EP – Auftragsbasierte Transportkonsolidierung".Beispielwerte für die zuvor aufgeführten Felder:Geschäftspartner: <17386202>Gruppierung: <Externe numerische Nummerierung (oberer Bereich) (BP03)>Name: <TM Bahnspediteur Gutschriftsverfahren US>Suchbegriff: <TMBAHNSPEDGUTUS> |  |  |
| 5 | Identifikationsdaten eingeben | Geben Sie für die Rolle des Geschäftspartners auf der Registerkarte Identifikation die folgenden Informationen ein:Rechtsform: <Rechtsform der Organisation>Beispielwerte für das obige Feld:Rechtsform: <01 (Körperschaft)>Sichern Sie Ihre Eingaben. |  |  |
| 6 | Neue Rolle "Frachtführer" zuordnen und Adressdaten eingeben | Wählen Sie die Drucktaste Umschalten zwischen Anzeigen und Ändern, um sicherzustellen, dass der "Änderungsmodus" aktiviert ist. Ordnen Sie die neue GP-Rolle Frachtführer (CRM010) zu, indem Sie die Rolle über die Auswahlliste "Ändern in GP-Rolle" auswählen.Geben Sie auf der Registerkarte Adresse die folgenden Informationen ein:Straße: <Straßenname>Postleitzahl/Ort: <Postleitzahl/Ort>Ort: <Name des Orts>Land: <Name des Landes>Region (Bundesland, Provinz): <Name der Region>Zeitzone: <Zeitzone>Sprache: <Sprache>Telefon (Vorwahl + Anschluss): <Telefonnummer mit Vorwahl>E-Mail: <E-Mail-Adresse>Beispielwerte für die zuvor aufgeführten Felder:Straße: <E Sweet Ave>Postleitzahl/Ort: <58504>Ort: <Bismarck>Land: <US>Region (Bundesland, Provinz): <ND>Zeitzone: <MST>Sprache: <EN>Telefon (Vorwahl + Anschluss): <999 254 3623>E-Mail: <info@17386202.com> | Die Geschäftspartnerrolle "Spediteur" wird hinzugefügt. |  |
| 7 | Zahlungsverkehrsdaten für Rolle "Frachtführer" eingeben | Geben Sie auf der Registerkarte Zahlungsverkehr die folgenden Informationen ein:Land: <Bankschlüssel>Bankschlüssel: <Bankschlüssel>Bankkonto: <Kontonummer>Sichern Sie Ihre Eingaben.Beispielwerte für die zuvor aufgeführten Felder:Land: <US>Bankschlüssel: <150350300>Bankkonto: <102610> |  |  |
| 8 | Neue Rolle "Lieferant" zuordnen und Geschäftspartnerdaten eingeben | Ordnen Sie die neue GP-Rolle Lieferant (FLVN01) zu, indem Sie die Rolle über die Auswahlliste "Ändern in GP-Rolle" auswählen.Wählen Sie Einkauf.Geben Sie den Wert in das Feld Einkaufsorganisation: <Einkaufsorganisation> ein.Wählen Sie Enter.Machen Sie auf der Registerkarte Einkaufsdaten folgende Angaben:Bestellwährung: <Währungsbezeichnung>Zahlungsbedingungen: <Zahlungsbedingungen>Versandbedingungen: <Name der Versandbedingung>Einkäufergruppe: <Wert>Schemagr. Lief.: <Wert>Autom. WEAbr. Lief. bis Auswert. Wareneingangsabrechnung: <markieren>Sichern Sie Ihre Eingaben.Beispielwerte für die zuvor aufgeführten Felder:Einkaufsorganisation: <1710>Bestellwährung: <USD>Zahlungsbedingungen: <0004>Versandbedingungen: <01>Einkäufergruppe: <005>Schemagr. Lief.: <03>Autom. WEAbr. Lief. bis autom. Wareneingangsabrechnung: <markieren> |  |  |
| 9 | Neue Rolle "Lieferant FI" zuordnen und Geschäftspartnerdaten eingeben | Ordnen Sie die neue GP-Rolle Lieferant (Finanzbuchh.) (FLVN00) zu, indem Sie die Rolle über die Auswahlliste "Ändern in GP-Rolle" auswählen.Wählen Sie Buchungskreis.Geben Sie den Buchungskreis ein: <Buchungskreis>Wählen Sie Enter.Geben Sie die folgenden Informationen auf der Registerkarte Lieferant: Kontoführung ein:Abstimmkonto: <Kontonummer>Sortierschlüssel: <Wert>Beispielwerte für die zuvor aufgeführten Felder:Buchungskreis: <1710>Abstimmkonto: <21100000>Sortierschlüssel: <009> |  |  |
| 10 | Lieferantenkorrespondenzdaten eingeben | Geben Sie die folgenden Informationen auf der Registerkarte Lieferant: Korrespondenz ein:Sachb.-Kürzel: <Wert>Konto beim Lieferanten: <Wert>Beispielwerte für die zuvor aufgeführten Felder:Sachb.-Kürzel: <01>Konto beim Lieferanten: 1710-CARR202 verwendet wird. |  |  |
| 11 | Daten sichern | Wählen Sie Sichern. | Eine Systemmeldung bestätigt, dass das Objekt gesichert wurde. |  |

### Geschäftspartner Spediteur (See) für Rechnungsprüfungsprozess anlegen

Testverwaltung

Kundenprojekt: Füllen Sie die projektbezogenen Teile aus.

|  |  |  |  |
| --- | --- | --- | --- |
| Testfall-ID | <X.XX> | Testdatum: |  |
| Testername: |  | Dauer: |  |
| Benutzerrolle(n): |  | Zuständigkeit: | <Geben Sie den Serviceanbieter, einen Kunden oder einen Serviceanbieter zusammen mit einem Kunden an.> |

Zweck

Legen Sie einen Geschäftspartner-Spediteur für die Transportausführung an. Der Spediteur ist einem Transportauftrag (Frachtbuchung) als ausführender/rechnungsstellender Spediteur auf Stufenebene zugeordnet. Dieser Frachtführer wird hauptsächlich im Rechnungsprüfungsprozess verwendet, wenn die Beträge der Spediteurrechnung mit den in der Frachtbuchung berechneten erwarteten Transportkosten verglichen werden.

Vorgehensweise

| Testschrittnummer | Bezeichnung des Testschritts | Anweisung | Erwartetes Ergebnis | Kommentare |
| --- | --- | --- | --- | --- |
| 1 | Anmelden | Melden Sie sich am SAP Fiori Launchpad als Stammdatenexperte – Geschäftspartnerdaten an. | Die Startseite wird angezeigt. |  |
| 2 | SAP-Fiori-App aufrufen | Geschäftspartner pflegen (BP) | Es wird ein neues Fenster mit dem Bild Geschäftspartner pflegen geöffnet. |  |
| 3 | GP-Organisation anlegen | Wählen Sie Organisation. | Das Bild Organisation anlegen wird angezeigt. |  |
| 4 | Allgemeine Daten erfassen | Geben Sie Folgendes ein:Geschäftspartner: <Geben Sie eine mit einem Buchstaben beginnende Geschäftspartner-ID ein.>Gruppierung: <externe alphanumerische Nummerierung>Das Feld Anlegen in GP-Rolle wird vom System mit der Rolle GPartner allgemein ausgefüllt. Behalten Sie diese Einstellung bei. Geben Sie auf der Registerkarte Adresse die folgenden Informationen ein:Name: <Name der Organisation>Suchbegriff: <Suchbegriff für den Geschäftspartner>Beispielwerte mit US-Lokalisierung für die oben genannten Felder:Geschäftspartner: <17386301>Gruppierung: <Externe numerische Nummerierung (oberer Bereich) (BP03)>Name: <TM Seefrachtführer US 1>Suchbegriff:<TMOCEANCARRUS1> |  |  |
| 5 | Identifikationsdaten eingeben | Geben Sie für die Rolle des Geschäftspartners auf der Registerkarte Identifikation die folgenden Informationen ein:Rechtsform: <Rechtsform der Organisation>Beispielwerte für das obige Feld: Rechtsform: <01 (Körperschaft)>Sichern Sie Ihre Eingaben. |  |  |
| 6 | Neue Rolle "Frachtführer" zuordnen und Adressdaten eingeben | Wählen Sie Umschalten zwischen Anzeigen und Ändern, um sicherzustellen, dass der Änderungsmodus aktiviert ist. Ordnen Sie die neue GP-Rolle Frachtführer (CRM010) zu, indem Sie die Rolle über die Auswahlliste Ändern in GP-Rolle auswählen.Geben Sie auf der Registerkarte Adresse für die GP-Rolle einen Frachtführer mit den folgenden Informationen ein:Straße: <Straßenname>Postleitzahl/Ort: <Postleitzahl des Orts>Ort: <Ortsname>Land: <Ländername>Region (Bundesland, Provinz, Kreis): <Regionsname>Zeitzone: <Zeitzone>Sprache: <Name der Sprache>Telefon (Vorwahl + Anschluss): <Telefonnummer mit Ortsvorwahl>E-Mail: <E-Mail-Adresse>Beispielwerte mit US-Lokalisierung für die oben genannten Felder:Straße:<5301 Waterford at Blue Lagoon>Postleitzahl/Ort: <33126>Stadt:<Miami>Land: <US>Region (Bundesland, Provinz):<FL>Zeitzone: <EST>Sprache: <EN>Telefon (Vorwahl + Anschluss): <412-264-5632>E-Mail: <info@17386301.com> |  |  |
| 7 | Zahlungsverkehrsdaten für Rolle "Frachtführer" eingeben | Geben Sie für die GP-Rolle "Frachtführer" auf der Registerkarte Zahlungsverkehr die folgenden Informationen ein:Land: <Bankschlüssel>Bankschlüssel: <Bankschlüssel>Bankkonto: <Kontonummer>Sichern Sie Ihre Eingaben.Beispielwerte mit US-Lokalisierungen für die oben genannten Felder:Land: <US>Bankschlüssel: <150350300>Bankkonto: <790133> |  |  |
| 8 | Neue Rolle "Lieferant" zuordnen und Geschäftspartnerdaten eingeben | Ordnen Sie die neue GP-Rolle Lieferant (FLVN01) zu, indem Sie die Rolle über die Auswahlliste Ändern in GP-Rolle auswählen. Führen Sie dann die folgenden Schritte durch:Wählen Sie Einkauf.Geben Sie den folgenden Wert in das Feld Einkaufsorganisation ein: <Einkaufsorganisation>Bestätigen Sie mit Enter.Machen Sie auf der Registerkarte Einkaufsdaten folgende Angaben:Bestellwährung: <Währungsbezeichnung>Zahlungsbedingungen: <Zahlungsbedingungen>Versandbedingungen: <Name der Versandbedingung>Einkäufergruppe: <Wert der Einkäufergruppe>Schemagr. Lief.: <Wert>Sichern Sie Ihre Eingaben.Beispielwerte mit US-Lokalisierung für die oben genannten Felder:Bestellwährung: <USD>Zahlungsbedingungen: <0004>Versandbedingungen: <01>Einkäufergruppe: <005>Schemagr. Lief.: <03> |  |  |
| 9 | Neue Rolle "Kreditor FI" zuordnen und Geschäftspartnerdaten eingeben | Ordnen Sie die neue GP-Rolle Kreditor (Finanzbuchhaltung) (FLVN00) zu, indem Sie die Rolle über folgende Auswahlliste auswählen:Ändern in GP-RolleWählen Sie Buchungskreis.Geben Sie den Buchungskreis ein: <Buchungskreis>Wählen Sie Enter.Geben Sie auf der entsprechenden Registerkarte die folgenden Informationen ein:Registerkarte Kreditor: Kontoverwaltung.Abstimmkonto: <Kontonummer>Sortierschlüssel: <Wert>Beispielwerte mit US-Lokalisierung für die oben genannten Felder:Buchungskreis: <1710>Abstimmkonto: <21100000>Sortierschlüssel: <009> |  |  |
| 10 | Kreditorenkorrespondenzdaten eingeben | Geben Sie auf der Registerkarte Kreditorenkorrespondenz die folgenden Informationen ein:Sachb.-Kürzel: <Wert>Konto beim Lieferanten: <Wert>Beispielwerte mit US-Lokalisierung für die oben genannten Felder:Sachb.-Kürzel: <01>Konto beim Lieferanten: <1710-CARR301> |  |  |
| 11 | Daten sichern | Wählen Sie Sichern. | Eine Systemmeldung bestätigt, dass das Objekt gesichert wurde. |  |

### Geschäftspartner Spediteur (See) für die automatische Wareneingangsabrechnung (ERS) anlegen

Testverwaltung

Kundenprojekt: Füllen Sie die projektbezogenen Teile aus.

|  |  |  |  |
| --- | --- | --- | --- |
| Testfall-ID | <X.XX> | Testdatum: |  |
| Testername: |  | Dauer: |  |
| Benutzerrolle(n): |  | Zuständigkeit: | <Geben Sie den Serviceanbieter, einen Kunden oder einen Serviceanbieter zusammen mit einem Kunden an.> |

Zweck

Legen Sie einen Geschäftspartner-Spediteur für die Transportausführung an. Der Spediteur ist einem Transportauftrag (Frachtbuchung) als ausführender/rechnungsstellender Spediteur auf Stufenebene zugeordnet. Dieser Frachtführer wird vor allem für das Szenario "Automatische Wareneingangsabrechnung (ERS)" verwendet, in dem die automatische Rechnungsabrechnung erfolgt, ohne auf eine Spediteurrechnung zu warten.

Vorgehensweise

| Testschrittnummer | Bezeichnung des Testschritts | Anweisung | Erwartetes Ergebnis | Kommentare |
| --- | --- | --- | --- | --- |
| 1 | Anmelden | Melden Sie sich am SAP Fiori Launchpad als Stammdatenexperte - Geschäftspartnerdaten an. | Die Startseite wird angezeigt. |  |
| 2 | SAP-Fiori-App aufrufen | Wählen Sie Geschäftspartner pflegen (BP). | Das Bild Geschäftspartner pflegen (BP) wird angezeigt. |  |
| 3 | GP-Organisation anlegen | Wählen Sie Organisation. | Das Bild Organisation anlegen wird angezeigt. |  |
| 4 | Allgemeine Daten erfassen | Geben Sie Folgendes ein:Geschäftspartner: <Geben Sie eine mit einem Buchstaben beginnende Geschäftspartner-ID ein.>Gruppierung: <externe alphanumerische Nummerierung>Das Feld Anlegen in GP-Rolle wird vom System mit der Rolle GPartner allgemein ausgefüllt. Behalten Sie diese Einstellung bei.Geben Sie auf der Registerkarte Adresse die folgenden Informationen ein:Name: <Name der Organisation>Suchbegriff: <Suchbegriff für den Geschäftspartner>Siehe Abschnitt "Stammdaten", "Organisationsdaten" und "Sonstige Daten" für die Auswahl der richtigen Werte im Szenario "3EP – Auftragsbasierte Transportkonsolidierung".Beispielwerte für die zuvor aufgeführten Felder:Geschäftspartner: <17386302>Gruppierung: <Externe numerische Nummerierung (oberer Bereich) (BP03)>Name: <TM Seefrachtführer Gutschriftsverfahren US 2>Suchbegriff: <TMOCEANCARRSBUS2> |  |  |
| 5 | Identifikationsdaten eingeben | Geben Sie für die Rolle des Geschäftspartners auf der Registerkarte Identifikation die folgenden Informationen ein:Rechtsform: <Rechtsform der Organisation>Beispielwerte für das obige Feld:Rechtsform: <01 (Körperschaft)>Sichern Sie Ihre Eingaben. |  |  |
| 6 | Neue Rolle "Frachtführer" zuordnen und Adressdaten eingeben | Wählen Sie die Drucktaste Umschalten zwischen Anzeigen und Ändern, um sicherzustellen, dass der "Änderungsmodus" aktiviert ist. Ordnen Sie die neue GP-Rolle Frachtführer (CRM010) zu, indem Sie die Rolle über die Auswahlliste "Ändern in GP-Rolle" auswählen.Geben Sie auf der Registerkarte Adresse die folgenden Informationen ein:Straße: <Straßenname>Postleitzahl/Ort: <Postleitzahl/Ort>Ort: <Name des Orts>Land: <Name des Landes>Region (Bundesland, Provinz): <Name der Region>Zeitzone: <Zeitzone>Sprache: <Sprache>Telefon (Vorwahl + Anschluss): <Telefonnummer mit Vorwahl>E-Mail: <E-Mail-Adresse>Beispielwerte für die zuvor aufgeführten Felder:Straße: <888 Brannan Street>Postleitzahl/Ort: <94103>Ort: <San Francisco>Land: <US>Region (Bundesland, Provinz): <CA>Zeitzone: <PST>Sprache: <EN>Telefon (Vorwahl + Anschluss): <999 254 3623>E-Mail: <info@17386302.com> | Die Geschäftspartnerrolle "Spediteur" wird hinzugefügt. |  |
| 7 | Zahlungsverkehrsdaten für Rolle "Frachtführer" eingeben | Geben Sie auf der Registerkarte Zahlungsverkehr die folgenden Informationen ein:Land: <Bankschlüssel>Bankschlüssel: <Bankschlüssel>Bankkonto: <Kontonummer>Sichern Sie Ihre Eingaben.Beispielwerte für die zuvor aufgeführten Felder:Land: <US>Bankschlüssel: <150350300>Bankkonto: <102610> |  |  |
| 8 | Neue Rolle "Lieferant" zuordnen und Geschäftspartnerdaten eingeben | Ordnen Sie die neue GP-Rolle Lieferant (FLVN01) zu, indem Sie die Rolle über die Auswahlliste "Ändern in GP-Rolle" auswählen.Wählen Sie Einkauf.Geben Sie den Wert in das Feld Einkaufsorganisation: <Einkaufsorganisation> ein.Wählen Sie Enter.Machen Sie auf der Registerkarte Einkaufsdaten folgende Angaben:Bestellwährung: <Währungsbezeichnung>Zahlungsbedingungen: <Zahlungsbedingungen>Versandbedingungen: <Name der Versandbedingung>Einkäufergruppe: <Wert>Schemagr. Lief.: <Wert>Autom. WEAbr. Lief. bis Auswert. Wareneingangsabrechnung: <markieren>Sichern Sie Ihre Eingaben.Beispielwerte für die zuvor aufgeführten Felder:Einkaufsorganisation: <1710>Bestellwährung: <USD>Zahlungsbedingungen: <0004>Versandbedingungen: <01>Einkäufergruppe: <005>Schemagr. Lief.: <03>Autom. WEAbr. Lief. bis autom. Wareneingangsabrechnung: <markieren> |  |  |
| 9 | Neue Rolle "Lieferant FI" zuordnen und Geschäftspartnerdaten eingeben | Ordnen Sie die neue GP-Rolle Lieferant (Finanzbuchh.) (FLVN00) zu, indem Sie die Rolle über die Auswahlliste "Ändern in GP-Rolle" auswählen.Wählen Sie Buchungskreis.Geben Sie den Buchungskreis ein: <Buchungskreis>Wählen Sie Enter.Geben Sie die folgenden Informationen auf der Registerkarte Lieferant: Kontoführung ein:Abstimmkonto: <Kontonummer>Sortierschlüssel: <Wert>Beispielwerte für die zuvor aufgeführten Felder:Buchungskreis: <1710>Abstimmkonto: <21100000>Sortierschlüssel: <009> |  |  |
| 10 | Lieferantenkorrespondenzdaten eingeben | Geben Sie die folgenden Informationen auf der Registerkarte Lieferant: Registerkarte Korrespondenz:Sachb.-Kürzel: <Wert>Konto beim Lieferanten: <Wert>Beispielwerte für die zuvor aufgeführten Felder:Sachb.-Kürzel: <01>Konto beim Lieferanten: <1710-CARR302>. |  |  |
| 11 | Daten sichern | Wählen Sie Sichern. | Eine Systemmeldung bestätigt, dass das Objekt gesichert wurde. |  |

### Geschäftspartner Spediteur für Rechnungsprüfungsprozess anlegen

Testverwaltung

Kundenprojekt: Füllen Sie die projektbezogenen Teile aus.

|  |  |  |  |
| --- | --- | --- | --- |
| Testfall-ID | <X.XX> | Testdatum: |  |
| Testername: |  | Dauer: |  |
| Benutzerrolle(n): |  | Zuständigkeit: | <Geben Sie den Serviceanbieter, einen Kunden oder einen Serviceanbieter zusammen mit einem Kunden an.> |

Zweck

Legen Sie einen Geschäftspartner (Spediteur) für die Transportausführung an. Der Spediteur wird einem Transportauftrag (Frachtbuchung) zugeordnet. Dieser Spediteur wird hauptsächlich für den Lohnbearbeitungsprozess und die Organisation der Transportausführung verwendet. Der Spediteur wird für seine Dienstleistung bezahlt, den Transport zu organisieren.

Vorgehensweise

| Testschrittnummer | Bezeichnung des Testschritts | Anweisung | Erwartetes Ergebnis | Kommentare |
| --- | --- | --- | --- | --- |
| 1 | Anmelden | Melden Sie sich am SAP Fiori Launchpad als Stammdatenexperte – Geschäftspartnerdaten an. | Die Startseite wird angezeigt. |  |
| 2 | SAP-Fiori-App aufrufen | Geschäftspartner pflegen (BP) | Es wird ein neues Fenster mit dem Bild Geschäftspartner pflegen geöffnet. |  |
| 3 | GP-Organisation anlegen | Wählen Sie Organisation. | Das Bild Organisation anlegen wird angezeigt. |  |
| 4 | Allgemeine Daten erfassen | Geben Sie Folgendes ein:Geschäftspartner: <Geben Sie eine mit einem Buchstaben beginnende Geschäftspartner-ID ein.>Gruppierung: <externe alphanumerische Nummerierung>Das Feld Anlegen in GP-Rolle wird vom System mit der Rolle GPartner allgemein ausgefüllt. Behalten Sie diese Einstellung bei. Geben Sie auf der Registerkarte Adresse die folgenden Informationen ein:Name: <Name der Organisation>Suchbegriff: <Suchbegriff für den Geschäftspartner>Beispielwerte mit US-Lokalisierung für die oben genannten Felder:Geschäftspartner: <17386401>Gruppierung: <Externe numerische Nummerierung (oberer Bereich) (BP03)>Name: <TM Spediteur US>Suchbegriff:<TMOCEANFORWUS1> |  |  |
| 5 | Identifikationsdaten eingeben | Geben Sie für die Rolle des Geschäftspartners auf der Registerkarte Identifikation die folgenden Informationen ein:Rechtsform: <Rechtsform der Organisation>Beispielwerte für das obige Feld: Rechtsform: <01 (Körperschaft)>Sichern Sie Ihre Eingaben. |  |  |
| 6 | Neue Rolle "Frachtführer" zuordnen und Adressdaten eingeben | Wählen Sie Umschalten zwischen Anzeigen und Ändern, um sicherzustellen, dass der Änderungsmodus aktiviert ist. Ordnen Sie die neue GP-Rolle Frachtführer (CRM010) zu, indem Sie die Rolle über die Auswahlliste Ändern in GP-Rolle auswählen.Geben Sie auf der Registerkarte Adresse für die GP-Rolle einen Frachtführer mit den folgenden Informationen ein:Straße: <Straßenname>Postleitzahl/Ort: <Postleitzahl des Orts>Ort: <Ortsname>Land: <Ländername>Region (Bundesland, Provinz, Kreis): <Regionsname>Zeitzone: <Zeitzone>Sprache: <Name der Sprache>Telefon (Vorwahl + Anschluss): <Telefonnummer mit Ortsvorwahl>E-Mail: <E-Mail-Adresse>Beispielwerte mit US-Lokalisierung für die oben genannten Felder:Straße:<131 Aberdeen Dr.>Postleitzahl/Ort: <92007>Ort:<CARDIFF BY THE SEA>Land: <US>Region (Bundesland, Provinz, Kreis): <CA>Zeitzone:<PST>Sprache: <EN>Telefon (Vorwahl + Anschluss): <412-264-5632>E-Mail: <info@17386401.com> |  |  |
| 7 | Zahlungsverkehrsdaten für Rolle "Frachtführer" eingeben | Geben Sie für die GP-Rolle "Frachtführer" auf der Registerkarte Zahlungsverkehr die folgenden Informationen ein:Land: <Bankschlüssel>Bankschlüssel: <Bankschlüssel>Bankkonto: <Kontonummer>Sichern Sie Ihre Eingaben.Beispielwerte mit US-Lokalisierungen für die oben genannten Felder:Land: <US>Bankschlüssel: <150350300>Bankkonto: <790133> |  |  |
| 8 | Neue Rolle "Lieferant" zuordnen und Geschäftspartnerdaten eingeben | Ordnen Sie die neue GP-Rolle Lieferant (FLVN01) zu, indem Sie die Rolle über die Auswahlliste Ändern in GP-Rolle auswählen. Führen Sie dann die folgenden Schritte durch:Wählen Sie Einkauf.Geben Sie den folgenden Wert in das Feld Einkaufsorganisation ein: <Einkaufsorganisation>Bestätigen Sie mit Enter.Machen Sie auf der Registerkarte Einkaufsdaten folgende Angaben:Bestellwährung: <Währungsbezeichnung>Zahlungsbedingungen: <Zahlungsbedingungen>Versandbedingungen: <Name der Versandbedingung>Einkäufergruppe: <Wert der Einkäufergruppe>Schemagr. Lief.: <Wert>Sichern Sie Ihre Eingaben.Beispielwerte mit US-Lokalisierung für die oben genannten Felder:Bestellwährung: <USD>Zahlungsbedingungen: <0004>Versandbedingungen: <01>Einkäufergruppe: <005>Schemagr. Lief.: <03> |  |  |
| 9 | Neue Rolle "Kreditor FI" zuordnen und Geschäftspartnerdaten eingeben | Ordnen Sie die neue GP-Rolle Kreditor (Finanzbuchhaltung) (FLVN00) zu, indem Sie die Rolle über folgende Auswahlliste auswählen:Ändern in GP-RolleWählen Sie Buchungskreis.Geben Sie den Buchungskreis ein: <Buchungskreis>Wählen Sie Enter.Geben Sie auf der entsprechenden Registerkarte die folgenden Informationen ein:Registerkarte Kreditor: Kontoverwaltung.Abstimmkonto: <Kontonummer>Sortierschlüssel: <Wert>Beispielwerte mit US-Lokalisierung für die oben genannten Felder:Buchungskreis: <1710>Abstimmkonto: <21100000>Sortierschlüssel: <009> |  |  |
| 10 | Kreditorenkorrespondenzdaten eingeben | Geben Sie auf der Registerkarte Kreditorenkorrespondenz die folgenden Informationen ein:Sachb.-Kürzel: <Wert>Konto beim Lieferanten: <Wert>Beispielwerte mit US-Lokalisierung für die oben genannten Felder:Sachb.-Kürzel: <01>Konto beim Lieferanten: <1710-CARR401> |  |  |
| 11 | Daten sichern | Wählen Sie Sichern. | Eine Systemmeldung bestätigt, dass das Objekt gesichert wurde. |  |

### Geschäftspartner (Spediteur) für die automatische Wareneingangsabrechnung (ERS) anlegen

Testverwaltung

Kundenprojekt: Füllen Sie die projektbezogenen Teile aus.

|  |  |  |  |
| --- | --- | --- | --- |
| Testfall-ID | <X.XX> | Testdatum: |  |
| Testername: |  | Dauer: |  |
| Benutzerrolle(n): |  | Zuständigkeit: | <Geben Sie den Serviceanbieter, einen Kunden oder einen Serviceanbieter zusammen mit einem Kunden an.> |

Zweck

Legen Sie einen Geschäftspartner (Spediteur) für die Transportausführung an. Der Spediteur wird einem Transportauftrag (Frachtbuchung) zugeordnet. Dieser Spediteur wird hauptsächlich für den Lohnbearbeitungsprozess und die Organisation der Transportausführung verwendet. Der Spediteur wird für seinen Service bezahlt, um den Transport zu organisieren. Dieser Spediteur wird hauptsächlich für das Szenario der automatischen Wareneingangsabrechnung (ERS) verwendet, in dem die automatische Rechnungsabrechnung erfolgt, ohne auf eine Spediteurrechnung zu warten.

Vorgehensweise

| Testschrittnummer | Bezeichnung des Testschritts | Anweisung | Erwartetes Ergebnis | Kommentare |
| --- | --- | --- | --- | --- |
| 1 | Anmelden | Melden Sie sich am SAP Fiori Launchpad als Stammdatenexperte - Geschäftspartnerdaten an. | Die Startseite wird angezeigt. |  |
| 2 | SAP-Fiori-App aufrufen | Wählen Sie Geschäftspartner pflegen (BP). | Das Bild Geschäftspartner pflegen (BP) wird angezeigt. |  |
| 3 | GP-Organisation anlegen | Wählen Sie Organisation. | Das Bild Organisation anlegen wird angezeigt. |  |
| 4 | Allgemeine Daten erfassen | Geben Sie Folgendes ein:Geschäftspartner: <Geben Sie eine mit einem Buchstaben beginnende Geschäftspartner-ID ein.>Gruppierung: <externe alphanumerische Nummerierung>Das Feld Anlegen in GP-Rolle wird vom System mit der Rolle GPartner allgemein ausgefüllt. Behalten Sie diese Einstellung bei.Geben Sie auf der Registerkarte Adresse die folgenden Informationen ein:Name: <Name der Organisation>Suchbegriff: <Suchbegriff für den Geschäftspartner>Siehe Abschnitt "Stammdaten", "Organisationsdaten" und "Sonstige Daten" für die Auswahl der richtigen Werte im Szenario "3EP – Auftragsbasierte Transportkonsolidierung".Beispielwerte für die zuvor aufgeführten Felder:Geschäftspartner: <17386402>Gruppierung: <Externe numerische Nummerierung (oberer Bereich) (BP03)>Name: <TM Spediteur Gutschriftsverfahren US>Suchbegriff: <TMOCEANFORWSBUS1> |  |  |
| 5 | Identifikationsdaten eingeben | Geben Sie für die Rolle des Geschäftspartners auf der Registerkarte Identifikation die folgenden Informationen ein:Rechtsform: <Rechtsform der Organisation>Beispielwerte für das obige Feld:Rechtsform: <01 (Körperschaft)>Sichern Sie Ihre Eingaben. |  |  |
| 6 | Neue Rolle "Frachtführer" zuordnen und Adressdaten eingeben | Wählen Sie die Drucktaste Umschalten zwischen Anzeigen und Ändern, um sicherzustellen, dass der "Änderungsmodus" aktiviert ist. Ordnen Sie die neue GP-Rolle Frachtführer (CRM010) zu, indem Sie die Rolle über die Auswahlliste "Ändern in GP-Rolle" auswählen.Geben Sie auf der Registerkarte Adresse die folgenden Informationen ein:Straße: <Straßenname>Postleitzahl/Ort: <Postleitzahl/Ort>Ort: <Name des Orts>Land: <Name des Landes>Region (Bundesland, Provinz): <Name der Region>Zeitzone: <Zeitzone>Sprache: <Sprache>Telefon (Vorwahl + Anschluss): <Telefonnummer mit Vorwahl>E-Mail: <E-Mail-Adresse>Beispielwerte für die zuvor aufgeführten Felder:Straße: <2601 Westheimer Road>Postleitzahl/Ort: <77098>Ort: <Houston>Land: <US>Region (Bundesland, Provinz): <TX>Zeitzone: <CST>Sprache: <EN>Telefon (Vorwahl + Anschluss): <999 254 3623>E-Mail: <info@17386402.com> | Die Geschäftspartnerrolle "Spediteur" wird hinzugefügt. |  |
| 7 | Zahlungsverkehrsdaten für Rolle "Frachtführer" eingeben | Geben Sie auf der Registerkarte Zahlungsverkehr die folgenden Informationen ein:Land: <Bankschlüssel>Bankschlüssel: <Bankschlüssel>Bankkonto: <Kontonummer>Sichern Sie Ihre Eingaben.Beispielwerte für die zuvor aufgeführten Felder:Land: <US>Bankschlüssel: <150350300>Bankkonto: <102610> |  |  |
| 8 | Neue Rolle "Lieferant" zuordnen und Geschäftspartnerdaten eingeben | Ordnen Sie die neue GP-Rolle Lieferant (FLVN01) zu, indem Sie die Rolle über die Auswahlliste "Ändern in GP-Rolle" auswählen.Wählen Sie Einkauf.Geben Sie den Wert in das Feld Einkaufsorganisation: <Einkaufsorganisation> ein.Wählen Sie Enter.Machen Sie auf der Registerkarte Einkaufsdaten folgende Angaben:Bestellwährung: <Währungsbezeichnung>Zahlungsbedingungen: <Zahlungsbedingungen>Versandbedingungen: <Name der Versandbedingung>Einkäufergruppe: <Wert>Schemagr. Lief.: <Wert>Autom. WEAbr. Lief. bis Auswert. Wareneingangsabrechnung: <markieren>Sichern Sie Ihre Eingaben.Beispielwerte für die zuvor aufgeführten Felder:Einkaufsorganisation: <1710>Bestellwährung: <USD>Zahlungsbedingungen: <0004>Versandbedingungen: <01>Einkäufergruppe: <005>Schemagr. Lief.: <03>Autom. WEAbr. Lief. bis autom. Wareneingangsabrechnung: <markieren> |  |  |
| 9 | Neue Rolle "Lieferant FI" zuordnen und Geschäftspartnerdaten eingeben | Ordnen Sie die neue GP-Rolle Lieferant (Finanzbuchh.) (FLVN00) zu, indem Sie die Rolle über die Auswahlliste "Ändern in GP-Rolle" auswählen.Wählen Sie Buchungskreis.Geben Sie den Buchungskreis ein: <Buchungskreis>Wählen Sie Enter.Geben Sie die folgenden Informationen auf der Registerkarte Lieferant: Kontoführung ein:Abstimmkonto: <Kontonummer>Sortierschlüssel: <Wert>Beispielwerte für die zuvor aufgeführten Felder:Buchungskreis: <1710>Abstimmkonto: <21100000>Sortierschlüssel: <009> |  |  |
| 10 | Lieferantenkorrespondenzdaten eingeben | Geben Sie die folgenden Informationen auf der Registerkarte Lieferant: Registerkarte Korrespondenz:Sachb.-Kürzel: <Wert>Konto beim Lieferanten: <Wert>Beispielwerte für die zuvor aufgeführten Felder:Sachb.-Kürzel: <01>Konto beim Lieferanten: <1710-CARR402>. |  |  |
| 11 | Daten sichern | Wählen Sie Sichern. | Eine Systemmeldung bestätigt, dass das Objekt gesichert wurde. |  |

### Geschäftspartner Spediteur (Luft) für Rechnungsprüfungsprozess anlegen

Testverwaltung

Kundenprojekt: Füllen Sie die projektbezogenen Teile aus.

|  |  |  |  |
| --- | --- | --- | --- |
| Testfall-ID | <X.XX> | Testdatum: |  |
| Testername: |  | Dauer: |  |
| Benutzerrolle(n): |  | Zuständigkeit: | <Geben Sie den Serviceanbieter, einen Kunden oder einen Serviceanbieter zusammen mit einem Kunden an.> |

Zweck

Legen Sie einen Geschäftspartner-Spediteur für die Transportausführung an. Der Spediteur ist einem Transportauftrag (Frachtbuchung) als ausführender/rechnungsstellender Spediteur auf Stufenebene zugeordnet. Dieser Frachtführer wird hauptsächlich im Rechnungsprüfungsprozess verwendet, wenn die Beträge der Spediteurrechnung mit den in der Frachtbuchung berechneten erwarteten Transportkosten verglichen werden.

Vorgehensweise

| Testschrittnummer | Bezeichnung des Testschritts | Anweisung | Erwartetes Ergebnis | Kommentare |
| --- | --- | --- | --- | --- |
| 1 | Anmelden | Melden Sie sich am SAP Fiori Launchpad als Stammdatenexperte – Geschäftspartnerdaten an. | Die Startseite wird angezeigt. |  |
| 2 | SAP-Fiori-App aufrufen | Geschäftspartner pflegen (BP) | Es wird ein neues Fenster mit dem Bild Geschäftspartner pflegen geöffnet. |  |
| 3 | GP-Organisation anlegen | Wählen Sie Organisation. | Das Bild Organisation anlegen wird angezeigt. |  |
| 4 | Allgemeine Daten eingeben | Nehmen Sie folgende Einträge vor:Geschäftspartner: <Geben Sie eine mit einem Buchstaben beginnende Geschäftspartner-ID ein.>Gruppierung: <externe alphanumerische Nummerierung>Das Feld Anlegen in GP-Rolle wird vom System mit der Rolle GPartner allgemein ausgefüllt. Behalten Sie diese Einstellung bei. Geben Sie auf der Registerkarte Adresse die folgenden Informationen ein:Name: <Name der Organisation>Suchbegriff: <Suchbegriff für den Geschäftspartner>Beispielwerte mit US-Lokalisierung für die oben genannten Felder:Geschäftspartner: <17386501>Gruppierung: <Externe numerische Nummerierung (oberer Bereich) (BP03)>Name: <TM Fluggesellschaft US 1>Suchbegriff: <TMAIRLINEUS1> |  |  |
| 5 | Identifikationsdaten eingeben | Geben Sie für die Rolle des Geschäftspartners auf der Registerkarte Identifikation die folgenden Informationen ein:Rechtsform: <Rechtsform der Organisation>Beispielwerte für das obige Feld: Rechtsform: <01 (Körperschaft)>Sichern Sie Ihre Eingaben. |  |  |
| 6 | Neue Rolle "Frachtführer" zuordnen und Adressdaten eingeben | Wählen Sie Umschalten zwischen Anzeigen und Ändern, um sicherzustellen, dass der Änderungsmodus aktiviert ist. Ordnen Sie die neue GP-Rolle Frachtführer (CRM010) zu, indem Sie die Rolle über die Auswahlliste Ändern in GP-Rolle auswählen.Geben Sie auf der Registerkarte Adresse für die GP-Rolle einen Frachtführer mit den folgenden Informationen ein:Straße: <Straßenname>Postleitzahl/Ort: <Postleitzahl des Orts>Ort: <Ortsname>Land: <Ländername>Region (Bundesland, Provinz, Kreis): <Regionsname>Zeitzone: <Zeitzone>Sprache: <Name der Sprache>Telefon (Vorwahl + Anschluss): <Telefonnummer mit Ortsvorwahl>E-Mail: <E-Mail-Adresse>Beispielwerte mit US-Lokalisierung für die oben genannten Felder:Straße: <5301 Waterford at Blue Lagoon>Postleitzahl/Ort: <33126>Stadt:<Miami>Land: <US>Region (Bundesland, Provinz): <FL>Zeitzone: <EST>Sprache: <EN>Telefon (Vorwahl + Anschluss): <412-264-5632>E-Mail: <info@17386501.com> |  |  |
| 7 | Zahlungsverkehrsdaten für Rolle "Frachtführer" eingeben | Geben Sie für die GP-Rolle "Frachtführer" auf der Registerkarte Zahlungsverkehr die folgenden Informationen ein:Land: <Bankschlüssel>Bankschlüssel: <Bankschlüssel>Bankkonto: <Kontonummer>Sichern Sie Ihre Eingaben.Beispielwerte mit US-Lokalisierungen für die oben genannten Felder:Land: <US>Bankschlüssel: <150350300>Bankkonto: <790133> |  |  |
| 8 | Neue Rolle "Lieferant" zuordnen und Geschäftspartnerdaten eingeben | Ordnen Sie die neue GP-Rolle Lieferant (FLVN01) zu, indem Sie die Rolle über die Auswahlliste Ändern in GP-Rolle auswählen. Führen Sie dann die folgenden Schritte durch:Wählen Sie Einkauf.Geben Sie den folgenden Wert in das Feld Einkaufsorganisation ein: <Einkaufsorganisation>Bestätigen Sie mit Enter.Machen Sie auf der Registerkarte Einkaufsdaten folgende Angaben:Bestellwährung: <Währungsbezeichnung>Zahlungsbedingungen: <Zahlungsbedingungen>Versandbedingungen: <Name der Versandbedingung>Einkäufergruppe: <Wert der Einkäufergruppe>Schemagr. Lief.: <Wert>Sichern Sie Ihre Eingaben.Beispielwerte mit US-Lokalisierung für die oben genannten Felder:Bestellwährung: <USD>Zahlungsbedingungen: <0004>Versandbedingungen: <01>Einkäufergruppe: <005>Schemagr. Lief.: <03> |  |  |
| 9 | Neue Rolle "Kreditor FI" zuordnen und Geschäftspartnerdaten eingeben | Ordnen Sie die neue GP-Rolle Kreditor (Finanzbuchhaltung) (FLVN00) zu, indem Sie die Rolle über folgende Auswahlliste auswählen:Ändern in GP-RolleWählen Sie Buchungskreis.Geben Sie den Buchungskreis ein: <Buchungskreis>Wählen Sie Enter.Geben Sie auf der entsprechenden Registerkarte die folgenden Informationen ein:Registerkarte Kreditor: Kontoverwaltung.Abstimmkonto: <Kontonummer>Sortierschlüssel: <Wert>Beispielwerte mit US-Lokalisierung für die oben genannten Felder:Buchungskreis: <1710>Abstimmkonto: <21100000>Sortierschlüssel: <009> |  |  |
| 10 | Kreditorenkorrespondenzdaten eingeben | Geben Sie auf der Registerkarte Kreditorenkorrespondenz die folgenden Informationen ein:Sachb.-Kürzel: <Wert>Konto beim Lieferanten: <Wert>Beispielwerte mit US-Lokalisierung für die oben genannten Felder:Sachb.-Kürzel: <01>Konto beim Lieferanten: <1710-CARR501> |  |  |
| 11 | Daten speichern | Wählen Sie Sichern. | Eine Systemmeldung bestätigt, dass das Objekt gesichert wurde. |  |

### Geschäftspartner Spediteur (Luft) für die automatische Wareneingangsabrechnung (ERS) anlegen

Testverwaltung

Kundenprojekt: Füllen Sie die projektbezogenen Teile aus.

|  |  |  |  |
| --- | --- | --- | --- |
| Testfall-ID | <X.XX> | Testdatum: |  |
| Testername: |  | Dauer: |  |
| Benutzerrolle(n): |  | Zuständigkeit: | <Geben Sie den Serviceanbieter, einen Kunden oder einen Serviceanbieter zusammen mit einem Kunden an.> |

Zweck

Legen Sie einen Geschäftspartner-Spediteur für die Transportausführung an. Der Spediteur ist einem Transportauftrag (Frachtbuchung) als ausführender/rechnungsstellender Spediteur auf Stufenebene zugeordnet. Dieser Frachtführer wird vor allem für das Szenario "Automatische Wareneingangsabrechnung (ERS)" verwendet, in dem die automatische Rechnungsabrechnung erfolgt, ohne auf eine Spediteurrechnung zu warten.

Vorgehensweise

| Testschrittnummer | Bezeichnung des Testschritts | Anweisung | Erwartetes Ergebnis | Kommentare |
| --- | --- | --- | --- | --- |
| 1 | Anmelden | Melden Sie sich am SAP Fiori Launchpad als "Stammdatenexperte - Geschäftspartnerdaten" an. | Die Startseite wird angezeigt. |  |
| 2 | SAP-Fiori-App aufrufen | Wählen Sie Geschäftspartner pflegen (BP). | Das Bild Geschäftspartner pflegen (BP) wird angezeigt. |  |
| 3 | GP-Organisation anlegen | Wählen Sie Organisation. | Das Bild Organisation anlegen wird angezeigt. |  |
| 4 | Allgemeine Daten eingeben | Nehmen Sie folgende Einträge vor:Geschäftspartner: <Geben Sie eine mit einem Buchstaben beginnende Geschäftspartner-ID ein.>Gruppierung: <externe alphanumerische Nummerierung>Das Feld Anlegen in GP-Rolle wird vom System mit der Rolle GPartner allgemein ausgefüllt. Behalten Sie diese Einstellung bei.Geben Sie auf der Registerkarte Adresse die folgenden Informationen ein:Name: <Name der Organisation>Suchbegriff: <Suchbegriff für den Geschäftspartner>Siehe Abschnitt "Stammdaten", "Organisationsdaten" und "Sonstige Daten" für die Auswahl der richtigen Werte im Szenario "3EP – Auftragsbasierte Transportkonsolidierung".Beispielwerte für die zuvor aufgeführten Felder:Geschäftspartner: <17386502>Gruppierung: <Externe numerische Nummerierung (oberer Bereich) (BP03)>Name: <TM Fluggesellschaft Gutschriftsverfahren US 2>Suchbegriff: <TMAIRLINESBUS2> |  |  |
| 5 | Identifikationsdaten eingeben | Geben Sie für die Rolle des Geschäftspartners auf der Registerkarte Identifikation die folgenden Informationen ein:Rechtsform: <Rechtsform der Organisation>Beispielwerte für das obige Feld:Rechtsform: <01 (Körperschaft)>Sichern Sie Ihre Eingaben. |  |  |
| 6 | Neue Rolle "Frachtführer" zuordnen und Adressdaten eingeben | Wählen Sie die Drucktaste Umschalten zwischen Anzeigen und Ändern, um sicherzustellen, dass der "Änderungsmodus" aktiviert ist. Ordnen Sie die neue GP-Rolle Frachtführer (CRM010) zu, indem Sie die Rolle über die Auswahlliste "Ändern in GP-Rolle" auswählen.Geben Sie auf der Registerkarte Adresse die folgenden Informationen ein:Straße: <Straßenname>Postleitzahl/Ort: <Postleitzahl/Ort>Ort: <Name des Orts>Land: <Name des Landes>Region (Bundesland, Provinz): <Name der Region>Zeitzone: <Zeitzone>Sprache: <Sprache>Telefon (Vorwahl + Anschluss): <Telefonnummer mit Vorwahl>E-Mail: <E-Mail-Adresse>Beispielwerte für die zuvor aufgeführten Felder:Straße: <888 Brannan Street>Postleitzahl/Ort: <94103>Ort: <San Francisco>Land: <US>Region (Bundesland, Provinz): <CA>Zeitzone: <PST>Sprache: <EN>Telefon (Vorwahl + Anschluss): <999 254 3623>E-Mail: <info@17386502.com> | Die Geschäftspartnerrolle "Spediteur" wird hinzugefügt. |  |
| 7 | Zahlungsverkehrsdaten für Rolle "Frachtführer" eingeben | Geben Sie auf der Registerkarte Zahlungsverkehr die folgenden Informationen ein:Land: <Bankschlüssel>Bankschlüssel: <Bankschlüssel>Bankkonto: <Kontonummer>Sichern Sie Ihre Eingaben.Beispielwerte für die zuvor aufgeführten Felder:Land: <US>Bankschlüssel: <150350300>Bankkonto: <102610> |  |  |
| 8 | Neue Rolle "Lieferant" zuordnen und Geschäftspartnerdaten eingeben | Ordnen Sie die neue GP-Rolle Lieferant (FLVN01) zu, indem Sie die Rolle über die Auswahlliste "Ändern in GP-Rolle" auswählen.Wählen Sie Einkauf.Geben Sie den Wert in das Feld Einkaufsorganisation: <Einkaufsorganisation> ein.Wählen Sie Enter.Machen Sie auf der Registerkarte Einkaufsdaten folgende Angaben:Bestellwährung: <Währungsbezeichnung>Zahlungsbedingungen: <Zahlungsbedingungen>Versandbedingungen: <Name der Versandbedingung>Einkäufergruppe: <Wert>Schemagr. Lief.: <Wert>Automatische WE-Abrechn.: <markieren>Sichern Sie die Eingaben.Beispielwerte für die zuvor aufgeführten Felder:Einkaufsorganisation: <1710>Bestellwährung: <USD>Zahlungsbedingungen: <0004>Versandbedingungen: <01>Einkäufergruppe: <005>Schemagr. Lief.: <03>Automatische WE-Abrechn.: <markieren> |  |  |
| 9 | Neue Rolle "Lieferant FI" zuordnen und Geschäftspartnerdaten eingeben | Ordnen Sie die neue GP-Rolle Lieferant (Finanzbuchh.) (FLVN00) zu, indem Sie die Rolle über die Auswahlliste "Ändern in GP-Rolle" auswählen.Wählen Sie Buchungskreis.Geben Sie den Buchungskreis ein: <Buchungskreis>Wählen Sie Enter.Geben Sie die folgenden Informationen auf der Registerkarte Lieferant: Kontoführung ein:Abstimmkonto: <Kontonummer>Sortierschlüssel: <Wert>Beispielwerte für die zuvor aufgeführten Felder:Buchungskreis: <1710>Abstimmkonto: <21100000>Sortierschlüssel: <009> |  |  |
| 10 | Lieferantenkorrespondenzdaten eingeben | Geben Sie die folgenden Informationen auf der Registerkarte Lieferant: Korrespondenz ein:Sachb.-Kürzel: <Wert>Konto beim Lieferanten: <Wert>Beispielwerte für die zuvor aufgeführten Felder:Sachb.-Kürzel: <01>Konto beim Lieferanten: <1710-CARR502>. |  |  |
| 11 | Daten speichern | Wählen Sie Sichern. | Eine Systemmeldung bestätigt, dass das Objekt gesichert wurde. |  |

## Anhang

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

## Suspected conflicts

> [!warning] Conflict
> Flagged while digesting this document, not verified: Step 4 of the road invoice-verification script says grouping 'externe alphanumerische Nummerierung' but samples use BP03 (external numeric).

> [!warning] Conflict
> Flagged while digesting this document, not verified: Step 6 expected-result wording is inconsistent: ERS scripts say Rolle 'Spediteur' wird hinzugefügt vs 'Frachtführer' in the road ERS script; the ERS checkbox label also varies across scripts.

> [!warning] Conflict
> Flagged while digesting this document, not verified: Overview table lists only the road invoice-verification segment although 10 segments are described; Zweck mentions only Frachtführer.

> [!warning] Conflict
> Flagged while digesting this document, not verified: Document title 'Zweck' in the extraction is a heading, not the real title; also the German text mentions a 'Materialstammdatensatz' for a business partner.

## Connections
- part-of :: [[_cluster]]
- related-to :: [[11-inventory-warehouse-and-transportation/master-data-script-create-carrier-master-mds-4de-407]]
- related-to :: [[11-inventory-warehouse-and-transportation/mds-4de-411]]
- related-to :: [[11-inventory-warehouse-and-transportation/mds-4de-master-data-script-create-carrier-master-409]]
- related-to :: [[11-inventory-warehouse-and-transportation/script-de-dados-mestre-criar-mestre-de-transportadoras-mds-4de-410]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/4DE_S4CLD2608_Master_Data_DE_XX.docx` — full document · extracted with `mammoth` · 65,908 chars in the whole document
