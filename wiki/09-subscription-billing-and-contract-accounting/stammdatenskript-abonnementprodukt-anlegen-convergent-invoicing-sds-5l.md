---
id: 09-subscription-billing-and-contract-accounting/stammdatenskript-abonnementprodukt-anlegen-convergent-invoicing-sds-5l
title: "Stammdatenskript: Abonnementprodukt anlegen (Convergent Invoicing) – SDS (5LP) (5LP_S4CLD2608_Master_Data_DE_XX)"
description: "German SAP S/4HANA Cloud Public Edition 2608 master data script (5LP): create business partner, contract account, Subscription Billing products, rate plans, price lookup tables."
cluster: 09-subscription-billing-and-contract-accounting
tags: [kb/subscription-billing-and-contract-accounting, topic/subscription-product-master-data]
aliases: [5LP_S4CLD2608_Master_Data_DE_XX]
keywords: [Subscription Products and Rate Plans, subscription products, business partner, customer master data, contract account, rate plan elements, rate plan templates, price calculation services, price lookup tables, product master enrichment]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/5LP_S4CLD2608_Master_Data_DE_XX.docx]
confidence: low
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-448
topic: 09-subscription-billing-and-contract-accounting/subscription-product-master-data
language: DE
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Stammdatenskript: Abonnementprodukt anlegen (Convergent Invoicing) – SDS (5LP) (5LP_S4CLD2608_Master_Data_DE_XX)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/5LP_S4CLD2608_Master_Data_DE_XX.docx`, extracted with `mammoth`. Grouped under **Subscription Products and Rate Plans** in Subscription Billing and Contract Accounting. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

| <!-- image omitted: unnamed --> | StammdatenskriptSAP S/4HANA Cloud Public Edition - 02-07-26 |
| --- | --- |
|  | Abonnementprodukt anlegen (Convergent Invoicing) – SDS (5LP) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Inhaltsverzeichnis

[1 Zweck 2](#_Toc233889772)

[2 Voraussetzungen 3](#_Toc233889773)

[2.1 Systemzugriff 3](#_Toc233889774)

[2.2 Rollen 3](#_Toc233889775)

[2.3 Erforderliche Organisationseinheiten (SAP S/4HANA) 3](#_Toc233889776)

[3 Übersichtstabelle 5](#_Toc233889777)

[4 Vorgehensweisen 6](#_Toc233889778)

[4.1 Geschäftspartner anlegen 6](#_Toc233889779)

[4.1.1 Kundenstammdaten anlegen 7](#_Toc233889780)

[4.1.2 Vertragskonto anlegen 9](#_Toc233889781)

[4.2 Abonnementprodukt anlegen (SAP Subscription Billing) 11](#_Toc233889782)

[4.2.1 Tarifelemente anlegen 11](#_Toc233889783)

[4.2.2 Tarifvorlage anlegen 12](#_Toc233889784)

[4.2.3 Produkt anlegen (SAP Subscription Billing) 14](#_Toc233889785)

[4.2.4 Produkt für Price-Calculation-Services anlegen 16](#_Toc233889786)

[4.2.5 Suchtabellen für Preisfindung hochladen 19](#_Toc233889787)

[4.3 Abonnementabrechnungsprodukte anreichern 23](#_Toc233889788)

[4.3.1 Abonnementprodukte vom Typ SBPD erweitern 23](#_Toc233889789)

[4.3.2 Abonnementprodukte vom Typ SBRE erweitern 26](#_Toc233889790)

[5 Anhang 31](#_Toc233889791)

## Zweck

Dieses Dokument beschreibt, wie Sie Stammdaten für das Abonnementprodukt anlegen. Die Beschreibung umfasst die Datensegmente, die für die Stammdaten für die Arbeit in einer üblichen Systemumgebung relevant sind. Der Leser lernt hier hauptsächlich, welche Datensegmente und -felder mit Eingabewerten gefüllt werden müssen. Felder, die nicht für den Umfang relevant sind, werden in diesem Dokument nicht behandelt, obwohl sie möglicherweise auf der Benutzungsoberfläche angezeigt werden.

Ein Abonnementstammsatz, der wie in diesem Dokument beschrieben angelegt wird, kann für die Abonnementabrechnung verwendet werden.

| Abonnementprodukt-ID | Beschreibung | Verwendung |
| --- | --- | --- |
| P-CLOUD_COMM | Abonnementprodukt | stellt das Abonnementabrechnungsprodukt dar |
| P-CLOUD_SUPPORT | Abonnementprodukt | stellt das Abonnementabrechnungsprodukt dar |

## Voraussetzungen

### Systemzugriff

In der folgenden Tabelle werden die Systemzugriffsanforderungen beschrieben.

| System | Details |
| --- | --- |
| SAP-S/4HANA-System | Zugriff möglich über SAP Fiori Launchpad.Ihr Systemadministrator stellt Ihnen die URL für den Zugriff auf die verschiedenen Apps zur Verfügung, die Ihrer Rolle zugeordnet sind. |
| SAP Subscription Billing | Zugriff über URL möglich.Ihr Systemadministrator stellt Ihnen die URL für den Zugriff auf die Anwendung zur Verfügung. |

### Rollen

Sie können Benutzerrollen über die folgenden von SAP ausgelieferten Benutzerrollenvorlagen anlegen und sie Ihren einzelnen Testbenutzern zuordnen.

SAP S/4HANA

| Name (Rollenvorlage) | ID (Rollenvorlage) | Name (Launchpad-Bereich) | ID (Launchpad-Bereich) | Anmelden |
| --- | --- | --- | --- | --- |
| Stammdatenexperte - Produktdaten | SAP_BR_PRODMASTER_SPECIALIST | Stammdatenexperte - Produktdaten | SAP_BR_PRODMASTER_SPECIALIST |  |
| Kreditoren- und Debitorenbuchhalter (FI-CA) | SAP_BR_APR_ACCOUNTANT_FICA | Kreditoren- und Debitorenbuchhalter (FI-CA) | SAP_BR_APR_ACCOUNTANT_FICA |  |

SAP Subscription Billing

Wenden Sie sich an Ihren Systemadministrator, um die erforderlichen Berechtigungen einzurichten.

### Erforderliche Organisationseinheiten (SAP S/4HANA)

Während einige Segmente von Stammdaten von den Organisationseinheiten des Unternehmens abhängen, hängen die allgemeinen (zentralen) Daten weder von einer Organisationseinheit noch vom Buchungskreis ab. Die folgende Tabelle stellt eine Übersicht dieser verschiedenen Datensegmente und ihrer relevanten Organisationseinheiten bereit:

| Datensegment | Hängt ab von | Zu verwendende Organisationseinheit | Anmerkungen |
| --- | --- | --- | --- |
| Stammdatensatz anlegen | Verkaufsorganisation | 1710 (Inländ. Verkaufsorganisation USA) | Für Deutschland, 1010 verwenden (Inländ. Verkaufsorganisation DE) |
| Stammdatensatz anlegen | Vertriebsweg | 10 (Direktverkauf) |  |

## Übersichtstabelle

Dieser Stammdatensatz umfasst mehrere Segmente, die in der nachfolgenden Tabelle genannt sind.

| Segment | Anwendungsrolle | App/Transaktion | Erwartete Ergebnisse |
| --- | --- | --- | --- |
| Abonnementprodukt anlegen (SAP Subscription Billing) | – | – | Abonnementprodukte werden angelegt. |
| Abonnementprodukte anreichern (SAP S/4HANA) | SAP_BR_PRODMASTER_SPECIALIST | Produktstammdaten verwalten | Abonnementprodukte werden angelegt. |

## Vorgehensweisen

Dieser Abschnitt beschreibt die Vorgehensweisen für jedes Segment oder Prozessschritt, das bzw. der Teil dieses Stammsatzes ist.

### Geschäftspartner anlegen

Kontext

In dieser Aktivität legen Sie einen Geschäftspartner für einen neuen Vertragskontokorrent-Kunden in S/4HANA Cloud an.

Vorgehensweise

| Testschrittnummer | Bezeichnung des Testschritts | Anweisung | Erwartetes Ergebnis | Bestanden/Nicht bestanden/Anmerkung |
| --- | --- | --- | --- | --- |
| 1 | Anmelden | Melden Sie sich als Kreditoren- und Debitorenbuchhalter (FI-CA) am SAP Fiori Launchpad an. | Das SAP Fiori Launchpad wird angezeigt. |  |
| 2 | SAP-Fiori-App aufrufen | Öffnen Sie Geschäftspartner pflegen (BP). | Die Sicht Geschäftspartner pflegen wird angezeigt. |  |
| 3 | Geschäftspartner anlegen | Wählen Sie Person, oder wählen Sie Mehr > Geschäftspartner > Anlegen > Person. | Die Sicht Person anlegen wird angezeigt. |  |
| 4 | Wählen Sie die GP-Rolle aus. | Geben Sie Folgendes ein:Anlegen in GP-Rolle: Vertragspartner | Die Sicht Wechsel zu einer anderen GP-Rolle wird im Anlegemodus angezeigt. |  |
| 5 | Anlegen | Wählen Sie Anlegen. | Wählen Sie im Dialogfenster Person anlegen die Rolle Vertragspartner.Vertragspartner (Neu) ist für Anlegen in GP-Rolle ausgewählt. |  |
| 6 | Grunddaten eingeben | Geben Sie Folgendes ein:Geschäftspartner: <Geben Sie eine spezifische ID ein> z.B. BP_US_97Gruppierung: Externe alphanumerische Nummerierung |  |  |
| 7 | Adressdaten eingeben | Geben Sie auf der Registerkarte Adresse folgende Daten ein:Vorname/Nachname: John/MillerStraße/Hausnummer: Hillview Ave/3410Postleitzahl/Ort: 94304/PALO ALTOLand: USRegion: CASteuerstandort: CA00000000Tipp Wenn Steuerstandort nicht sichtbar ist, wählen Sie +, um die Optionen zu erweitern. |  |  |
| 8 | Zahlungsbestand pflegen | Fügen Sie eine Bankverbindung über die App Geschäftspartner verwalten hinzu und registrieren Sie die Zahlungskarte über die App Geschäftspartnerstammdaten verwalten.Geben Sie auf der Registerkarte Zahlungsverkehr die folgenden Daten ein:Erfassen Sie im Abschnitt Bankverbindung Folgendes:ID: 01Land: USBankleitzahl: 011000390Bankkonto: <Bankkonto>SWIFT-Code (SWIFT/BIC): CITIUS33XXXWählen Sie Einreichen. | Die Sicht Prüfung des Abstimmschlüssels wird angezeigt. |  |
| 9 | Sichern | Wählen Sie Sichern. | Ein neuer Geschäftspartner wird angelegt. |  |

#### Kundenstammdaten anlegen

Testverwaltung

Kundenprojekt: Füllen Sie die projektbezogenen Teile aus.

|  |  |  |  |
| --- | --- | --- | --- |
| Testfall-ID | <X.XX> | Testdatum: |  |
| Testername: |  | Dauer: |  |
| Benutzerrolle(n): |  | Zuständigkeit: | <Geben Sie den Serviceanbieter, einen Kunden oder einen Serviceanbieter zusammen mit einem Kunden an.> |

Kontext

In dieser Aktivität erweitern Sie einen FI-CA-Geschäftspartner mit der GP-Rolle FLCU01 und MKK um die Vertriebsbereichsstammdaten.

Vorgehensweise

| Testschrittnummer | Bezeichnung des Testschritts | Anweisung | Erwartetes Ergebnis | Bestanden/Nicht bestanden/Anmerkung |
| --- | --- | --- | --- | --- |
| 1 | Anmelden | Melden Sie sich am SAP Fiori Launchpad mit Ihren Anmeldeinformationen als an. SAP_BR_APR_ACCOUNTANT_FICA | Das SAP Fiori Launchpad wird angezeigt. |  |
| 2 | SAP-Fiori-App aufrufen | Öffnen Sie Geschäftspartner pflegen(BP). | Das Bild Geschäftspartner pflegen wird angezeigt. |  |
| 3 | Geschäftspartner selektieren | Geben Sie die Nummer des Geschäftspartners ein. |  |  |
| 4 | Geschäftspartner öffnen | Wählen Sie Enter. |  |  |
| 5 | In den Änderungsmodus wechseln | Wählen Sie Umschalten zwischen Anzeigen und Ändern. |  |  |
| 6 | Ändern in GP-Rolle | Wählen Sie im Feld Ändern in GP-Rolle den folgenden Wert: KundeDer technische Schlüssel dieser GP-Rolle ist FLCU01. |  |  |
| 7 | Eingabeinformationen für Adresse | Korrespondenzsprache: <EN> |  |  |
| 8 | Vertriebsbereich öffnen | Wählen Sie im oberen Bildbereich die Option Vertrieb. | Die Sicht Vertriebsbereich wird angezeigt. |  |
| 9 | Vertriebsbereichsdaten eingeben | Geben Sie folgende Daten ein:Verkaufsorganisation: 1710Vertriebsweg: 10Sparte: 00Wählen Sie Enter und dann Sichern.Hinweis Die drei oben genannten Einträge bilden den Vertriebsbereich. In vielen Fällen legt der Vertriebsbereich den Zweck der Vertriebsabwicklung fest, z.B. im Kundenauftrag oder innerhalb der Preisfindung. | Die Änderungen für den Geschäftspartner werden gesichert. |  |
| 10 | Versanddaten eingeben | Geben Sie auf der Registerkarte Versand im Abschnitt Versand die folgenden Daten ein:Auslieferungswerk: 1710 |  |  |
| 11 | Steuerdaten erfassen | Geben Sie auf der Registerkarte Faktura im Abschnitt Ausgangssteuer die folgenden Daten ein:Steuerklassifikation: <1>Der Wert <1> bedeutet z.B., dass dieser Kunde voll steuerpflichtig ist. |  |  |
| 12 | Daten sichern | Sichern Sie Ihre Eingaben. |  |  |
| 13 | Ändern in GP-Rolle | Wählen Sie im Feld Ändern in GP-Rolle den folgenden Wert: VertragspartnerDer technische Schlüssel dieser GP-Rolle ist MKK. |  |  |
| 14 | Eingabeinformationen für Adresse | Korrespondenzsprache: <EN> |  |  |
| 15 | Versanddaten eingeben | Geben Sie auf der Registerkarte Versand im Abschnitt Versand die folgenden Daten ein:Auslieferungswerk: 1710 |  |  |
| 16 | Steuerdaten erfassen | Geben Sie auf der Registerkarte Faktura im Abschnitt Ausgangssteuer die folgenden Daten ein:Steuerklassifikation: <1>Der Wert <1> bedeutet z.B., dass dieser Kunde voll steuerpflichtig ist. |  |  |
| 17 | Daten sichern | Sichern Sie Ihre Eingaben. |  |  |

#### Vertragskonto anlegen

Kontext

In dieser Aktivität legen Sie Vertragskonto-Stammdaten für einen Vertragskontokorrent-Kunden in SAP S/4HANA Cloud Public Edition an.

Vorgehensweise

| Testschrittnummer | Bezeichnung des Testschritts | Anweisung | Erwartetes Ergebnis | Bestanden/Nicht bestanden/Anmerkung |
| --- | --- | --- | --- | --- |
| 1 | Anmelden | Melden Sie sich am SAP Fiori Launchpad mit Ihren Anmeldeinformationen über die Benutzerrolle des Kreditoren- und Debitorenbuchhalters (FI-CA) an. | Das SAP Fiori Launchpad wird angezeigt. |  |
| 2 | SAP-Fiori-App aufrufen | Öffnen Sie Vertragskonto pflegen(CAA3). | Das Bild Vertragskontenanzeige: Einstieg wird angezeigt. |  |
| 3 | Vertragskonto anlegen | Wählen Sie Anlegen oder im Menü Mehr > Vertragskonto > Anlegen. | Das Bild Vertragskonto - Anlegen: Einstieg wird angezeigt. |  |
| 4 | Grunddaten eingeben | Geben Sie Folgendes ein:Vertragskonto: <Geben Sie eine spezifische ID ein> z.B. CA_US_97Geschäftspartner: <Wählen Sie die Geschäftspartnernummer aus, die Sie im Schritt "Geschäftspartner anlegen" angelegt haben.>VertragsktoTyp: Y1Gültig ab: <aktuelles Datum> |  |  |
| 5 | Details zum Vertragskonto pflegen | Wählen Sie Weiter. | Das Bild Vertragskonto - Anlegen: Allgemeine Daten wird angezeigt. |  |
| 6 | Allgemeine Daten eingeben | Geben Sie auf der Registerkarte Allgemein folgende Daten ein:Vtrgskontobez: <Vertragskontobezeichnung>Konto beziehung: KontoinhaberToleranzgruppe: Y001 Toleranz nicht erlaubtDispositionsgruppe: Inländischer KundeZahl.Kond.: YN01KontFind ID: Y1 |  |  |
| 7 | Daten zu Zahlungen/Steuern eingeben | Geben Sie auf der Registerkarte Zahlungen/Steuern folgende Daten ein:BuchKreisGruppe: 1710Standardbuchkrs: 1710 |  |  |
| 8 | Mahnen/Korrespondenz eingeben | Geben Sie auf der Registerkarte Mahnen/Korrespondenz folgende Daten ein:Korrespondenztyp Variante: <nur Ausdruck, sofort> |  |  |
| 9 | Sichern | Wählen Sie Sichern. | Ein neues Vertragskonto wird angelegt. |  |

### Abonnementprodukt anlegen (SAP Subscription Billing)

#### Tarifelemente anlegen

Zweck

In dieser Aktivität legen Sie Tarifelemente in SAP Subscription Billing an. Die Tarif-IDs müssen den relevanten S/4HANA-Produkten der Art SBRE entsprechen:

| Tarif-ID | Tarifart | Beschreibung |
| --- | --- | --- |
| R-ONETIME | Einmalig | Einmalige Aktivierungsgebühr |
| R-SEATS | Wiederkehrend | Seat-bezogene monatliche Gebühr |
| R-TICKETS | Nutzungsabhängig | Ticket-bezogene Nutzungsgebühr |

Vorgehensweise

| Testschrittnummer | Bezeichnung des Testschritts | Anweisung | Erwartetes Ergebnis | Kommentare |
| --- | --- | --- | --- | --- |
| 1 | Anmelden | Melden Sie sich an SAP Subscription Billing an. | Die Startseite wird angezeigt. |  |
| 2 | Zu Tarifelementen navigieren | Wählen Sie unter Stammdaten und Konfiguration die Option Business-Konfiguration > Tarifelemente. | Die Sicht Tarifelemente wird angezeigt. |  |
| 3 | Tarifelement anlegen: Einmalig | Wählen Sie Anlegen, und nehmen Sie anschließend folgende Einträge vor:Art: EinmaligID: R-ONETIMEEinheit: Stück (ST)Bezeichnung: Einmalige AktivierungsgebührDatenquelle: KeineArt der einmaligen Gebühr: ErstgebührFakturaart: GebührBeschreibung: Geben Sie eine Beschreibung ein, z.B. Einmalige Aktivierungsgebühr.Aktiv: markiertWählen Sie Sichern. | Das Tarifelement R-ONETIME wird angelegt. |  |
| 4 | Tarifelement anlegen: R-SEATS | Wählen Sie Anlegen, und nehmen Sie anschließend folgende Einträge vor:Art: WiederkehrendID: R-SEATSEinheit: Stück (ST)Bezeichnung: Seat-bezogene monatliche GebührDatenquelle: AbonnementFakturaart: GebührBeschreibung: Geben Sie eine Beschreibung ein, z.B. Seat-bezogene monatliche Gebühr.Aktiv: markiertWählen Sie Sichern. | Das R-SEATS-Tarifelement wird angelegt. |  |
| 5 | Tarifelement anlegen: R-TICKETS | Wählen Sie Anlegen, und nehmen Sie anschließend folgende Einträge vor:Art: NutzungsabhängigID: R-TICKETSEinheit: Gigabyte (GB)/Each (EA)Bezeichnung: Ticket-bezogene NutzungsgebührDatenquelle: NutzungFakturaart: GebührNutzungs-Rating-Variante: AggregiertArt der technischen Ressourcen-ID: Cloud-Speicherplatz-IDBeschreibung: Geben Sie eine Beschreibung ein, z.B. Upload/Download-Traffic in GB.Aktiv: markiertWählen Sie Sichern. | Das R-TICKETS-Tarifelement wird angelegt. |  |

#### Tarifvorlage anlegen

Zweck

In dieser Aktivität legen Sie eine Tarifvorlage in SAP Subscription Billing an.

Vorgehensweise

| Testschrittnummer | Bezeichnung des Testschritts | Anweisung | Erwartetes Ergebnis | Kommentare |
| --- | --- | --- | --- | --- |
| 1 | Anmelden | Melden Sie sich an SAP Subscription Billing an. | Die Startseite wird angezeigt. |  |
| 2 | Zu Tarifvorlagen navigieren | Wählen Sie unter Preisfindung die App Tarifvorlagen. | Die verfügbaren Tarifvorlagen werden angezeigt. |  |
| 3 | Tarifvorlage anlegen: SEATS | Wählen Sie Anlegen > Ohne Gebührenmodell, und pflegen Sie unter Allgemeine Informationen folgende Daten:Beschreibung: Platzbasierte TarifvorlageAbrechnungszyklus: Wert- Monatlich am ersten Tag des MonatsWährung: Wert – USD (für Länderversion US)Wählen Sie Hinzufügen. | Die Grunddaten für die Vorlage sind definiert. |  |
| 4 | Gebühren/Gutschriften für SEATS pflegen | Legen Sie im Abschnitt Gebühren/Gutschriften eine einmalige Gebühr an, indem Sie Hinzufügen > Einmalig wählen. Geben Sie folgende Daten ein:Tarifelement: R-ONETIMEPreis: Wert – 9,99 USD (für Länderversion US)Legen Sie im Abschnitt Gebühren/Gutschriften eine wiederkehrende Gebühr an, indem Sie Hinzufügen > Wiederkehrend > Prozentwertpreisdefinition wählen. Geben Sie folgende Daten ein:Tarifelement: R-SEATSÄnderungen mit dem nächsten Zyklus anwenden: ausgewähltAbrechnung im Voraus: ausgewähltErsten Zyklus anteilig berechnen: ausgewähltPreis pro Einheit: 1 EURVerhältnis: 100Legen Sie im Abschnitt Gebühren/Gutschriften eine Nutzungsgebühr an, indem Sie Hinzufügen > Nutzungsabhängig > Blockpreisdefinition wählen. Geben Sie folgende Daten ein:Tarifelement: R-TICKETSÄnderungen mit dem nächsten Zyklus anwenden: nicht markiertInklusivvolumen: Wert – 1Blockgröße: Wert – 1Preis pro Block: Wert – 1 EUR (für Länderversion DE)Wählen Sie Sichern und Veröffentlichen. | Die Gebühren/Gutschriften werden angelegt. |  |

#### Produkt anlegen (SAP Subscription Billing)

Zweck

In dieser Aktivität legen Sie die Produkte P-CLOUD_COMM und P-CLOUD_SUPPORT in SAP Subscription Billing an. Die ID des Produkts in SAP Subscription Billing muss der zugehörigen Produkt-ID in SAP S/4HANA entsprechen.

Vorgehensweise

Produkt: P-CLOUD_COMM

| Testschrittnummer | Bezeichnung des Testschritts | Anweisung | Erwartetes Ergebnis | Kommentare |
| --- | --- | --- | --- | --- |
| 1 | Anmelden | Melden Sie sich an SAP Subscription Billing an. | Die Startseite wird angezeigt. |  |
| 2 | Zu "Produkte" navigieren | Wählen Sie unter Stammdaten und Konfiguration die Option Business-Konfiguration > Produkte. | Die verfügbaren Produkte werden angezeigt. |  |
| 3 | Allgemeine Produktinformationen pflegen | Wählen Sie Anlegen, und geben Sie im Bereich Allgemeine Informationen die folgenden Daten ein:Produktname: Cloud-KommunikationProdukt-ID: P-CLOUD_COMMAbonnementart: KostenpflichtigAbonnements als vorläufig anlegen: EntmarkiertElektronisch verkauft: markiert | Die allgemeinen Informationen wurden gepflegt. |  |
| 4 | Tarif für Produkt pflegen | Wählen Sie im Bereich Tarifedie Option Tarif aus Vorlage anlegen.Geben Sie in der Sicht Tarif anlegen folgende Daten ein:Markt: US East (für Länderversion US)Tarifvorlage: Platzbasierte TarifvorlageBeschreibung: Wiederkehrender Tarif (platzbasiert) | Der Tarif des Produkts wurde gepflegt. |  |
| 5 | Vertragsmodalitäten pflegen | Pflegen Sie die folgenden Abonnementparameterdetails:Erwartete Laufzeit: z.B. 12Mindestlaufzeit: 12Verlängerungslaufzeit: 12Widerrufsfrist: 14 | Die Vertragsmodalitäten werden gepflegt. |  |
| 6 | Produkt anlegen | Wählen Sie in der Sicht Tarif anlegen die Option Anlegen.Wählen Sie in der Sicht Produkt die Option Sichern.Wählen Sie anschließend Veröffentlichen. | Das Produkt P-CLOUD_COMM wird angelegt. |  |

Produkt: P-CLOUD_SUPPORT

| Testschrittnummer | Bezeichnung des Testschritts | Anweisung | Erwartetes Ergebnis | Kommentare |
| --- | --- | --- | --- | --- |
| 1 | Anmelden | Melden Sie sich an SAP Subscription Billing an. | Die Startseite wird angezeigt. |  |
| 2 | Zu "Produkte" navigieren | Wählen Sie im linken Navigationsbereich Produkte. | Die verfügbaren Produkte werden angezeigt. |  |
| 3 | Allgemeine Produktinformationen pflegen | Wählen Sie Anlegen, und geben Sie im Bereich Allgemeine Informationen die folgenden Daten ein:Produktname: Cloud-SupportProdukt-ID: P-CLOUD_SUPPORTAbonnementart: KostenpflichtigAbonnements als vorläufig anlegen: EntmarkiertElektronisch verkauft: markiert | Die allgemeinen Informationen wurden gepflegt. |  |
| 4 | Tarif für Produkt pflegen | Wählen Sie im Bereich Tarifedie Option Tarif aus Vorlage anlegen.Geben Sie in der Sicht Tarif anlegen folgende Daten ein:Markt: US East (für Länderversion US)Tarifvorlage: Platzbasierte TarifvorlageBeschreibung: Wiederkehrender Tarif (platzbasiert) | Der Tarif des Produkts wurde gepflegt. |  |
| 5 | Vertragsmodalitäten pflegen | Pflegen Sie die Abonnementparameterdetails:Erwartete Laufzeit: z.B. 12Mindestlaufzeit: 12Verlängerungslaufzeit: 12Widerrufsfrist: 14 | Die Vertragsmodalitäten werden gepflegt. |  |
| 6 | Produkt anlegen | Wählen Sie in der Sicht Tarif anlegen die Option Anlegen.Wählen Sie in der Sicht Produkt die Option Sichern.Wählen Sie anschließend Veröffentlichen. | Das Produkt P-CLOUD_SUPPORT wird angelegt. |  |

#### Produkt für Price-Calculation-Services anlegen

Wenn Sie einen Beispielanwendungsfall durchlaufen, können Sie entweder die Beispielwerte verwenden, um Daten von Grund auf neu anzulegen, oder Sie können die vordefinierte Konfiguration verwenden, die mit jedem neuen Tenant ausgeliefert wird. Bevor Sie ein Produkt für PCS anlegen, müssen Sie die folgenden Schritte in der Preisberechnung ausführen.

Vorgehensweise

1. Feldkatalog verwalten

Wenn Sie die Beispieldaten einsetzen, wird in der App Feldkatalog verwalten ein vordefinierter Feldkatalog verwendet. Daher müssen Sie hier keine zusätzlichen Einstellungen vornehmen. Mit der App Feldkatalog verwalten können Sie Felder anlegen, die später zum Definieren der Suchtabellen und Eingabeeigenschaften für Preiselementspezifikationen verwendet werden.

2. Suchtabellen anlegen

In der App Suchtabelle verwalten können Sie Suchtabellen anlegen, indem Sie einen Satz von Eingabefeldern einem Satz von Ausgabefeldern zuordnen. Diese Suchtabellen werden dann in einem späteren Schritt verwendet, um Preiselementspezifikationen anzulegen. Das Ziel dieses Schritts besteht darin, die folgenden Suchtabellen für einmalige, wiederkehrende und Nutzungsgebühren zu erstellen:

- OneTimePrice
- RecurringPrice
- UsagePrice
- Discount1

Diese Tabellen sind Bestandteil des vordefinierten Inhalts. Daher müssen Sie in diesem Schritt keine zusätzlichen Einstellungen vornehmen.

3. Preiselementspezifikationen

In der App Preiselementspezifikationen verwalten definieren Sie Ihre Preisfindungskonfiguration, indem Sie Preiselementspezifikationen anlegen. Dazu gehört das Einrichten der Preisfindungslogik und übersteuerbarer Felder:

- OneTimePrice
- RecurringPrice
- UsagePrice
- Discount1

Diese Preiselementspezifikationen sind Teil des vordefinierten Inhalts. Daher müssen Sie in diesem Schritt keine zusätzlichen Einstellungen vornehmen.

4. Preisschema

In der App Preisschema verwalten legen Sie Preisschemata an und pflegen diese. Ein Preisschema ist ein Verfahren, das die Verwendung und die Beziehung der Preiselementspezifikationen für einen bestimmten bepreisbaren Beleg definiert. Es legt außerdem die Reihenfolge zum Ausführen dieser Spezifikationen zum Generieren eines Gesamtbetrags in einem bepreisten Beleg fest.

Das Preisschema "Initial" ist Teil des vordefinierten Inhalts. Daher müssen Sie in diesem Schritt keine zusätzlichen Einstellungen vornehmen.

5. Tarifvorlage anlegen

| Testschrittnummer | Bezeichnung des Testschritts | Anweisungen | Erwartete Ergebnisse | Kommentare |
| --- | --- | --- | --- | --- |
| 1 | Anmelden | Melden Sie sich an SAP Subscription Billing an. | Die Startseite wird angezeigt. |  |
| 2 | Zur App Tarifvorlagen navigieren | Öffnen Sie Preisfindung > Tarifvorlagen | Die Tarifvorlagen werden angezeigt. |  |
| 3 | Anlegen wählen | Wählen Sie Anlegen - Mit Preisschema, und geben Sie unter Allgemeine Informationen die folgenden Daten ein:Beschreibung: RPT für PreisberechnungTags: PCS (optional)Preisschema: InitialAbrechnungszyklus: Monatlich am ersten Tag des MonatsWährung: EUR | Die allgemeinen Informationen wurden gepflegt. |  |
| 4 | Gebühren/Gutschriften für Tarifelemente pflegen | Bei einmaligen Gebühren/Gutschriften wählen Sie Gebühren/Gutschriften > Hinzufügen > Einmalig, und geben Tarifelement = R-ONETIME ein.Bei wiederkehrenden Gebühren/Gutschriften wählen Sie Gebühren/Gutschriften > Hinzufügen > Wiederkehrend, und geben Tarifelement = R-SEATS ein.Bei Gebühren/Gutschriften mit Blockpreisdefinition wählen Sie Gebühren/Gutschriften > Hinzufügen > Nutzungsgutschrift mit Blockpreisdefinition/Nutzungsgebühr mit Blockpreisdefinition, und geben Tarifelement = R-TRAFFIC ein.Wählen Sie Sichern und dann Veröffentlichen. |  |  |

6. Produkt anlegen

Sie legen ein Produkt P-CLOUD_STORAGE_PC in SAP Subscription Billing an. Die ID des Produkts in SAP Subscription Billing muss der zugehörigen Produkt-ID in SAP S/4HANA entsprechen. Sie können folgende Vorgehensweise verwenden:

| Testschrittnummer | Bezeichnung des Testschritts | Anweisung | Erwartetes Ergebnis | Kommentare |
| --- | --- | --- | --- | --- |
| 1 | Anmelden | Melden Sie sich an SAP Subscription Billing an. | Die Startseite wird angezeigt. |  |
| 2 | Zu Produkte navigieren | Öffnen Sie unter Stammdaten und Konfiguration die App Produkte. | Die verfügbaren Produkte werden angezeigt. |  |
| 3 | Allgemeine Produktinformationen pflegen | Wählen Sie Anlegen, und geben Sie im Bereich Allgemeine Informationen die folgenden Daten ein:Produktname: Preisberechnung für Cloud-SpeicherProdukt-ID: P-CLOUD_STORAGE_PCAbonnementart: KostenpflichtigAbonnements als vorläufig anlegen: Entmarkiert | Die allgemeinen Informationen wurden gepflegt. |  |
| 4 | Tarif für Produkt pflegen | Wählen Sie auf der Registerkarte Tarife die Option Anlegen - Mit Preisschema.Hinweis Weitere Informationen über Preisberechnungsprodukte finden Sie unter [SAP Subscription Billing mit Preisschemata.](https://help.sap.com/docs/CLOUD_TO_CASH_OD/3da4082dc5094e3489b7c98e9113cf6c/3542ae740bb046b9bf422e193f3e0526.html)Navigieren Sie zu Tarif aus Vorlage anlegen > Tarif anlegen - Mit Preisschema, und pflegen Sie die folgenden Daten:Markt: US East (für Länderversion US)Tarifvorlage: RPT für PreisberechnungBeschreibung: RPT für PreisberechnungAbrechnungszyklus: Monatlich am ersten Tag des MonatsWählen Sie Anlegen. | Der Tarif wurde für das Produkt gepflegt. |  |
| 5 | Vertragsmodalitäten pflegen | Pflegen Sie im Bereich Vertragsmodalitäten folgende Daten:Erwartete Laufzeit: z.B. 12Mindestlaufzeit: 12Verlängerungslaufzeit: 12Widerrufsfrist: 14 | Die Vertragsmodalitäten werden gepflegt. |  |
| 6 | Produkt anlegen | Wählen Sie in der Sicht Tarif anlegen die Option Anlegen.Wählen Sie in der Sicht Produkt die Option Sichern.Wählen Sie Veröffentlichen. | Das Produkt P-CLOUD_STORAGE_PC wird angelegt. |  |

7. Suchtabellen für Preisfindung hochladen

Weitere Informationen zum Hochladen von Suchtabellen finden Sie unter Suchtabellen für Preisfindung hochladen.

Weitere Informationen über Preisberechnungsprodukte finden Sie unter [SAP Subscription Billing mit Preisschemata.](https://help.sap.com/docs/CLOUD_TO_CASH_OD/3da4082dc5094e3489b7c98e9113cf6c/3542ae740bb046b9bf422e193f3e0526.html)

#### Suchtabellen für Preisfindung hochladen

Sie können Ihre Suchtabellen für einmalige, wiederkehrende und nutzungsabhängige Gebühren und für den Rabatt hochladen, indem Sie folgende Vorgehensweise nutzen. Die Daten in der folgenden Tabelle werden verwendet, um die relevanten Preise während der Preisfindung im Rahmen des Rating-Prozesses zu finden.

Tabelle 1: Einmalige Tabelle hochladen

| Testschrittnummer | Bezeichnung des Testschritts | Anweisungen | Erwartetes Ergebnis | Kommentare |
| --- | --- | --- | --- | --- |
| 1 | Anmelden | Melden Sie sich bei SAP Price Calculation an. | Die Startseite wird angezeigt. |  |
| 2 | Zu Tarifvorlagen navigieren | Öffnen Sie unter Master Data Managementdie App Suchtabelleninhalt pflegen. | Die Suchtabellen werden angezeigt. |  |
| 3 | OneTimePrice wählen | Wählen Sie die Suchtabelle OneTimePrice aus.Laden Sie die leere Tabelle herunter, und speichern Sie sie lokal als CSV-Datei.Tipp Wenn das Format der heruntergeladenen Datei nicht spaltengetrennt ist, müssen Sie das Format der Tabelle in ein US-Format ändern. |  |  |
| 4 | Heruntergeladene Datei aktualisieren | Geben Sie die folgenden Werte ein, und sichern Sie die Datei:Produktcode: P-CLOUD_STORAGE_PCMarkt-ID: A1Tarifelement: R-ONETIMEPreis: EinzelnPreis (Preisart): FestPreis (Wert) 5000Preis (Wertwährung): USD |  |  |
| 5 | CSV-Datei hochladen | Wählen Sie die Suchtabelle OneTimePrice, und wechseln Sie zu Importieren > Durchsuchen, um die gesicherte Datei aus dem vorherigen Schritt hochzuladen.Hinweis Es gibt zwei Arten von Importen. Wählen Sie Zusammenführen, um die vorhandenen Daten intakt zu halten.Wählen Sie Importieren. | Die Suchtabelle OneTimePrice wird aktualisiert. |  |

Tabelle 2: Wiederkehrende Tabelle hochladen

| Testschrittnummer | Bezeichnung des Testschritts | Anweisungen | Erwartetes Ergebnis | Kommentare |
| --- | --- | --- | --- | --- |
| 1 | Anmelden | Melden Sie sich bei SAP Price Calculation an. | Die Startseite wird angezeigt. |  |
| 2 | Zu Tarifvorlagen navigieren | Öffnen Sie unter Master Data Managementdie App Suchtabelleninhalt pflegen. | Die Suchtabellen werden angezeigt. |  |
| 3 | RecurringPrice wählen | Wählen Sie die Suchtabelle RecurringPrice aus.Laden Sie die leere Tabelle herunter, und speichern Sie sie lokal als CSV-Datei.Tipp Wenn das Format der heruntergeladenen Datei nicht spaltengetrennt ist, müssen Sie das Format der Tabelle in ein US-Format ändern. |  |  |
| 4 | Heruntergeladene Datei aktualisieren | Geben Sie die folgenden Werte ein, und sichern Sie die Datei:Produktcode: P-CLOUD_STORAGE_PCMarkt-ID: A1Tarifelement: R-SEATSPreis: EinzelnPreis (Preisart): LinearPreis (Wert) 50Preis (Wertwährung): USDPreis (Mengenwert): 1Preis (Mengeneinheit): ST |  |  |
| 5 | CSV-Datei hochladen | Wählen Sie die Suchtabelle RecurringPrice, und wechseln Sie zu Importieren > Durchsuchen, um die gesicherte Datei aus dem vorherigen Schritt hochzuladen.Hinweis Es gibt zwei Arten von Importen. Wählen Sie Zusammenführen, um die vorhandenen Daten intakt zu halten.Wählen Sie Importieren. | Die Suchtabelle RecurringPrice wird aktualisiert. |  |

Tabelle 3: Verwendungstabelle hochladen

| Testschrittnummer | Bezeichnung des Testschritts | Anweisungen | Erwartetes Ergebnis | Kommentare |
| --- | --- | --- | --- | --- |
| 1 | Anmelden | Melden Sie sich bei SAP Price Calculation an. | Die Startseite wird angezeigt. |  |
| 2 | Zu Tarifvorlagen navigieren | Öffnen Sie unter Master Data Managementdie App Suchtabelleninhalt pflegen. | Die Suchtabellen werden angezeigt. |  |
| 3 | UsagePrice wählen | Wählen Sie die Suchtabelle OneTimePrice aus.Laden Sie die leere Tabelle herunter, und speichern Sie sie lokal als CSV-Datei.Tipp Wenn das Format der heruntergeladenen Datei nicht spaltengetrennt ist, müssen Sie das Format der Tabelle in ein US-Format ändern. |  |  |
| 4 | Heruntergeladene Datei aktualisieren | Geben Sie die folgenden Werte ein, und sichern Sie die Datei:Produktcode: P-CLOUD_STORAGE_PCMarkt-ID: A1Tarifelement: R-TRAFFICPreis: VolumenPreis (Preisart): LinearDie folgenden spezifischen Werte sind für jede Stufe eines Unterelements mit hohem Tarif verfügbar:Tarifunterelement: HochPreis (Bereich): 500Preis (Bereichseinheit): EAPreis (Wert) 30Preis (Wertwährung): USDPreis (Mengenwert): 1Preis (Mengeneinheit): EADie folgenden spezifischen Werte sind für jede Stufe verfügbar:Tarifunterelement: HochPreis (Bereich): 1000Preis (Bereichseinheit): EAPreis (Wert) 25Preis (Wertwährung): USDPreis (Mengenwert): 1Preis (Mengeneinheit): EADie folgenden spezifischen Werte sind für jede Stufe verfügbar:Tarifunterelement: HochPreis (Bereich):Preis (Bereichseinheit): EAPreis (Wert) 20Preis (Wertwährung): USDPreis (Mengenwert): 1Preis (Mengeneinheit): EADie folgenden spezifischen Werte sind für jede Stufe eines Unterelements mit niedrigem Tarif verfügbar:Tarifunterelement: NiedrigPreis (Bereich): 500Preis (Bereichseinheit): EAPreis (Wert) 15Preis (Wertwährung): USDPreis (Mengenwert): 1Preis (Mengeneinheit): EADie folgenden spezifischen Werte sind für jede Stufe eines Unterelements mit niedrigem Tarif verfügbar:Tarifunterelement: NiedrigPreis (Bereich): 1000Preis (Bereichseinheit): EAPreis (Wert) 10Preis (Wertwährung): USDPreis (Mengenwert): 1Preis (Mengeneinheit): EADie folgenden spezifischen Werte sind für jede Stufe eines Unterelements mit niedrigem Tarif verfügbar:Tarifunterelement: NiedrigPreis (Bereich):Preis (Bereichseinheit): EAPreis (Wert) 5Preis (Wertwährung): USDPreis (Mengenwert): 1Preis (Mengeneinheit): EA |  |  |
| 5 | CSV-Datei hochladen | Wählen Sie die Suchtabelle OneTimePrice, und wechseln Sie zu Importieren > Durchsuchen, um die gesicherte Datei aus dem vorherigen Schritt hochzuladen.Hinweis Es gibt zwei Arten von Importen. Wählen Sie Zusammenführen, um die vorhandenen Daten intakt zu halten.Wählen Sie Importieren.. | Die Suchtabelle OneTimePrice wird aktualisiert. |  |

Tabelle 4: Rabatttabelle hochladen

| Testschrittnummer | Bezeichnung des Testschritts | Anweisungen | Erwartetes Ergebnis | Kommentare |
| --- | --- | --- | --- | --- |
| 1 | Anmelden | Melden Sie sich bei SAP Price Calculation an. | Die Startseite wird angezeigt. |  |
| 2 | Zu Tarifvorlagen navigieren | Öffnen Sie unter Master Data Managementdie App Suchtabelleninhalt pflegen. | Die Suchtabellen werden angezeigt. |  |
| 3 | Discount1 wählen | Wählen Sie die Suchtabelle Discount1 aus.Laden Sie die leere Tabelle herunter, und speichern Sie sie lokal als CSV-Datei.Tipp Wenn das Format der heruntergeladenen Datei nicht spaltengetrennt ist, müssen Sie das Format der Tabelle in ein US-Format ändern. |  |  |
| 4 | Heruntergeladene Datei aktualisieren | Geben Sie die folgenden Werte ein, und sichern Sie die Datei:Markt-ID: A1Rabatt: EinzelnRabatt (Preisart): ProzentsatzRabatt (Wert): 0,1 |  |  |
| 5 | CSV-Datei hochladen | Wählen Sie die Suchtabelle Discount1, und wechseln Sie zu Importieren > Durchsuchen, um die gesicherte Datei aus dem vorherigen Schritt hochzuladen.Hinweis Es gibt zwei Arten von Importen. Wählen Sie Zusammenführen, um die vorhandenen Daten intakt zu halten.Wählen Sie Importieren.. | Die Suchtabelle Discount1 wird aktualisiert. |  |

### Abonnementabrechnungsprodukte anreichern

#### Abonnementprodukte vom Typ SBPD erweitern

Zweck

In dieser Aktivität erweitern Sie die Abonnementprodukte P-CLOUD_COMM und P-CLOUD_SUPPORT in SAP S/4HANA. Diese Produkte werden in SAP Subscription Billing angelegt und nach SAP S/4HANA repliziert.

Vorgehensweise

Produkt: P-CLOUD_COMM

| Testschrittnummer | Bezeichnung des Testschritts | Anweisung | Erwartetes Ergebnis | Kommentare |
| --- | --- | --- | --- | --- |
| 1 | Anmelden | Melden Sie sich am SAP Fiori Launchpad als Stammdatenexperte – Produktdaten an. | Die Startseite wird angezeigt. |  |
| 2 | SAP-Fiori-App aufrufen | Wählen Sie die Kachel Produktstammdaten verwalten. | Die App Produktstammdaten verwalten wird angezeigt. |  |
| 3 | Produkt P-CLOUD_COMM suchen | Geben Sie oben im Suchbereichdas Produkt P-CLOUD_COMM ein.Wählen Sie Starten. | Ihr Produkt wird in der Berichtsliste angezeigt. |  |
| 4 | Produkt öffnen und Vertriebslinien pflegen: Allgemeine Informationen | Wählen Sie das Produkt aus der Berichtsliste aus.Produktnummer: P-CLOUD_COMMBasismengeneinheit: STProduktart: SBPD (Sub.- Billing-Produkt)Wählen Sie anschließend OK.Hinweis Geben Sie unter Beschreibung die Details zu Sprache und Produkt für eine bestimmte Region an, z.B. Sprache: Deutsch und Produkt: Abonnementabrechnungsprodukt. | Das Produkt sollte offen sein, und allgemeine Informationen werden gepflegt. |  |
| 5 | Vertriebslinie pflegen: Allgemeine Informationen | Wählen Sie in der Sicht Produkt im Bereich Vertriebslinien die Option Anlegen,und geben Sie folgende Daten ein:Verkaufsorganisation: 1710 (Inländ. Verkaufsorganisation USA)Vertriebsweg: 10 (Direktverkauf)Hinweis Die Vertriebslinie ist für die Produktart SBPD nicht erforderlich, wenn Sie MDI verwenden. Sie ist nur erforderlich, wenn Sie Cloud Integration verwenden. | Gruppierungsbegriffe werden gepflegt, und das Produkt wird gesichert. | Pflegen Sie für die Länderversion Deutschland statt 1 (Volle Steuer) den folgenden Wert:Steuerklassifikation: 6 (Volle Steuer (Services))Die anderen Einträge sind für beide Länder gleich. |
| 6 | Vertriebslinie pflegen: Gruppierungsbegriffe | Wechseln Sie auf die Registerkarte Gruppierungsbegriffe, und geben Sie folgende Daten ein:Positionstypengruppe: SBPD (Sub.- Billing-Produkt)Kontierungsgruppe: X9 (Periodischer Service)Steuerklassifikation: 1 (volle Steuer)Wählen Sie anschließend Übernehmenund dann Anlegen.Hinweis Die Positionstypengruppe ist nur erforderlich, wenn Sie die Cloud-Integration und nicht die Stammdatenintegration für die Replikation verwenden. |  |  |
| 7 | Werke pflegen | Navigieren Sie in den Bereich Werke, wählen Sie Anlegen, und pflegen Sie die folgenden Daten:Werk: 1710 (Werk USA)Wählen Sie anschließend Übernehmen und dann Sichern. | Die Werksdaten werden gepflegt. |  |

Produkt: P-CLOUD_SUPPORT

| Testschrittnummer | Bezeichnung des Testschritts | Anweisung | Erwartetes Ergebnis | Kommentare |
| --- | --- | --- | --- | --- |
| 1 | Anmelden | Melden Sie sich am SAP Fiori Launchpad als Stammdatenexperte – Produktdaten an. | Die Startseite wird angezeigt. |  |
| 2 | SAP-Fiori-App aufrufen | Wählen Sie die Kachel Produktstammdaten verwalten. | Die App Produktstammdaten verwalten wird angezeigt. |  |
| 3 | Produkt P-CLOUD_SUPPORT suchen | Geben Sie oben im Suchbereichdas Produkt: P-CLOUD_SUPPORT ein.Wählen Sie Starten. | Ihr Produkt wird in der Berichtsliste angezeigt. |  |
| 4 | Produkt öffnen und Vertriebslinien pflegen: Allgemeine Informationen | Wählen Sie das Produkt aus der Berichtsliste aus.Produktnummer: P-CLOUD_COMMBasismengeneinheit: STProduktart: SBPD (Sub.- Billing-Produkt)Wählen Sie anschließend OK.Hinweis Geben Sie unter Beschreibung die Details zu Sprache und Produkt für eine bestimmte Region an, z.B. Sprache: Deutsch und Produkt: Abonnementabrechnungsprodukt. | Das Produkt sollte offen sein, und allgemeine Informationen werden gepflegt. |  |
| 5 | Vertriebslinie pflegen: Allgemeine Informationen | Wählen Sie in der Sicht Produkt im Bereich Vertriebslinien die Option Anlegen,und geben Sie folgende Daten ein:Verkaufsorganisation: 1710 (Inländ. Verkaufsorganisation USA)Vertriebsweg: 10 (Direktverkauf)Hinweis Die Vertriebslinie ist für die Produktart SBPD nicht erforderlich, wenn Sie die Stammdatenintegration verwenden. Sie ist nur erforderlich, wenn Sie Cloud Integration verwenden. | Gruppierungsbegriffe werden gepflegt, und das Produkt wird gesichert. | Pflegen Sie für die Länderversion Deutschland statt 1 (Volle Steuer) den folgenden Wert:Steuerklassifikation: 6 (Volle Steuer (Services))Die anderen Einträge sind für beide Länder gleich. |
| 6 | Vertriebslinie pflegen: Gruppierungsbegriffe | Wechseln Sie auf die Registerkarte Gruppierungsbegriffe, und geben Sie folgende Daten ein:Positionstypengruppe: SBPD (Sub.- Billing-Produkt)Kontierungsgruppe: X9 (Periodischer Service)Steuerklassifikation: 1 (volle Steuer)Wählen Sie anschließend Übernehmenund dann Anlegen.Hinweis Vertriebslinie ist für die Produktart SBPD nicht erforderlich, wenn Sie die Stammdatenintegration verwenden, und nur erforderlich, wenn Sie Cloud Integration verwenden. |  |  |
| 7 | Werke pflegen | Navigieren Sie in den Bereich Werke, wählen Sie Anlegen, und pflegen Sie die folgenden Daten:Werk: 1710 (Werk USA)Wählen Sie anschließend Übernehmen und dann Sichern. | Die Werksdaten werden gepflegt. |  |

#### Abonnementprodukte vom Typ SBRE erweitern

Zweck

In dieser Aktivität erweitern Sie die folgenden Abonnementprodukte in SAP S/4HANA. Diese Produkte werden in SAP Subscription Billing angelegt und nach SAP S/4HANA repliziert.

| Produkt-ID | Produktart | Beschreibung |
| --- | --- | --- |
| R-ONETIME | SBRE | Einmalige Aktivierungsgebühr |
| R-SEATS | SBRE | Seat-bezogene monatliche Gebühr |
| R-TICKETS | SBRE | Ticket-bezogene Nutzungsgebühr |

Vorgehensweise

Produkt: R_ONETIME

| Testschrittnummer | Bezeichnung des Testschritts | Anweisung | Erwartetes Ergebnis | Kommentare |
| --- | --- | --- | --- | --- |
| 1 | Anmelden | Melden Sie sich am SAP Fiori Launchpad als Stammdatenexperte – Produktdaten an. | Die Startseite wird angezeigt. |  |
| 2 | SAP-Fiori-App aufrufen | Wählen Sie die Kachel Produktstammdaten verwalten. | Die App Produktstammdaten verwalten wird angezeigt. |  |
| 3 | Produkt R_ONETIME suchen | Geben Sie im Suchbereich das Produkt: R_ONETIME ein.Wählen Sie Start. | Ihr Produkt wird in der Berichtsliste angezeigt. |  |
| 4 | Produkt öffnen und Vertriebslinien pflegen: Allgemeine Informationen | Wählen Sie in der Sicht Produkt im Bereich Vertriebslinien die Option Anlegen,und geben Sie folgende Daten ein:Verkaufsorganisation: 1710 (Inländ. Verkaufsorganisation USA)Vertriebsweg: 10 (Direktverkauf)Skonto: JaHinweis Geben Sie unter Beschreibung die Details zu Sprache und Produkt für eine bestimmte Region an, z.B. Sprache: Deutsch und Produkt: Abonnementabrechnungsprodukt. | Das Produkt sollte offen sein, und allgemeine Informationen werden gepflegt. | Pflegen Sie für die Länderversion Deutschland statt 1710 den folgenden Wert:Verkaufsorganisation: 1010 (Inländ. Verkaufsorganisation DE)Die anderen Einträge sind für beide Länder gleich. |
| 5 | Vertriebslinie pflegen: Gruppierungsbegriffe | Wechseln Sie auf die Registerkarte Gruppierungsbegriffe, und geben Sie folgende Daten ein:Kontierungsgruppe: X9 (Periodischer Service)Steuerklassifikation: 1 (volle Steuer)Wählen Sie anschließend Übernehmen. | Gruppierungsbegriffe werden gepflegt, und das Produkt wird gesichert. | Pflegen Sie für die Länderversion Deutschland statt 1 (Volle Steuer) den folgenden Wert:Steuerklassifikation: 6 (Volle Steuer (Services))Die anderen Einträge sind für beide Länder gleich. |
| 6 | Werke pflegen | Navigieren Sie in den Bereich Werke, wählen Sie Anlegen, und pflegen Sie die folgenden Daten:Werk: 1710 (Werk USA)Wählen Sie anschließend Übernehmen und dann Anlegen. | Die Werksdaten werden gepflegt. |  |

Produkt: R_SEATS

| Testschrittnummer | Bezeichnung des Testschritts | Anweisung | Erwartetes Ergebnis | Kommentare |
| --- | --- | --- | --- | --- |
| 1 | Anmelden | Melden Sie sich am SAP Fiori Launchpad als Stammdatenexperte – Produktdaten an. | Die Startseite wird angezeigt. |  |
| 2 | SAP-Fiori-App aufrufen | Wählen Sie die Kachel Produktstammdaten verwalten. | Die App Produktstammdaten verwalten wird angezeigt. |  |
| 3 | Produkt R_SEATS suchen | Geben Sie im Suchbereich das Produkt: R_SEATS ein.Wählen Sie Start. | Ihr Produkt wird in der Berichtsliste angezeigt. |  |
| 4 | Produkt öffnen und Vertriebslinien pflegen: Allgemeine Informationen | Wählen Sie das Produkt aus der Berichtsliste aus.Wählen Sie in der Sicht Produkt die Option Bearbeiten.Wählen Sie im Bereich Vertriebslinien die Option Anlegen, und geben Sie folgende Daten ein:Verkaufsorganisation: 1710 (Inländ. Verkaufsorganisation USA)Vertriebsweg: 10 (Direktverkauf)Hinweis Geben Sie unter Beschreibung die Details zu Sprache und Produkt für eine bestimmte Region an, z.B. Sprache: Deutsch und Produkt: Abonnementabrechnungsprodukt. | Das Produkt sollte offen sein, und allgemeine Informationen werden gepflegt. | Pflegen Sie für die Länderversion Deutschland statt 1710 den folgenden Wert:Verkaufsorganisation: 1010 (Inländ. Verkaufsorganisation DE)Die anderen Einträge sind für beide Länder gleich. |
| 5 | Vertriebslinie pflegen: Gruppierungsbegriffe | Wechseln Sie auf die Registerkarte Gruppierungsbegriffe, und geben Sie folgende Daten ein:Positionstypengruppe: SBRE (AbonnAbrech. - Tarifelem.)Kontierungsgruppe: X9 (Periodischer Service)Steuerklassifikation: 1 (volle Steuer)Wählen Sie anschließend Übernehmen. | Gruppierungsbegriffe werden gepflegt, und das Produkt wird gesichert. | Pflegen Sie für die Länderversion Deutschland statt 1 (Volle Steuer) den folgenden Wert:Steuerklassifikation: 6 (Volle Steuer (Services))Die anderen Einträge sind für beide Länder gleich. |
| 6 | Werke pflegen | Navigieren Sie in den Bereich Werke, wählen Sie Anlegen, und pflegen Sie die folgenden Daten:Werk: 1710 (Werk USA)Wählen Sie anschließend Übernehmen und Sichern. | Die Werksdaten werden gepflegt. |  |

Produkt: R_TICKETS

| Testschrittnummer | Bezeichnung des Testschritts | Anweisung | Erwartetes Ergebnis | Kommentare |
| --- | --- | --- | --- | --- |
| 1 | Anmelden | Melden Sie sich am SAP Fiori Launchpad als Stammdatenexperte – Produktdaten an. | Die Startseite wird angezeigt. |  |
| 2 | SAP-Fiori-App aufrufen | Wählen Sie die Kachel Produktstammdaten verwalten. | Die App Produktstammdaten verwalten wird angezeigt. |  |
| 3 | Produkt R_TICKETS suchen | Geben Sie im Suchbereich das Produkt: R_TICKETS ein.Wählen Sie Start. | Ihr Produkt wird in der Berichtsliste angezeigt. |  |
| 4 | Produkt öffnen und Vertriebslinien pflegen: Allgemeine Informationen | Wählen Sie das Produkt aus der Berichtsliste aus.Wählen Sie in der Sicht Produkt die Option Bearbeiten.Wählen Sie im Bereich Vertriebslinien die Option Anlegen, und geben Sie folgende Daten ein:Verkaufsorganisation: 1710 (Inländ. Verkaufsorganisation USA)Vertriebsweg: 10 (Direktverkauf)Hinweis Geben Sie unter Beschreibung die Details zu Sprache und Produkt für eine bestimmte Region an, z.B. Sprache: Deutsch und Produkt: Abonnementabrechnungsprodukt. | Das Produkt sollte offen sein, und allgemeine Informationen werden gepflegt. | Pflegen Sie für die Länderversion Deutschland statt 1710 den folgenden Wert:Verkaufsorganisation: 1010 (Inländ. Verkaufsorganisation DE)Die anderen Einträge sind für beide Länder gleich. |
| 5 | Vertriebslinie pflegen: Gruppierungsbegriffe | Wechseln Sie auf die Registerkarte Gruppierungsbegriffe, und geben Sie folgende Daten ein:Kontierungsgruppe: X9 (Periodischer Service)Steuerklassifikation: 1 (volle Steuer)Wählen Sie anschließend Übernehmen. | Gruppierungsbegriffe werden gepflegt, und das Produkt wird gesichert. | Pflegen Sie für die Länderversion Deutschland statt 1 (Volle Steuer) den folgenden Wert:Steuerklassifikation: 6 (Volle Steuer (Services))Die anderen Einträge sind für beide Länder gleich. |
| 6 | Werke pflegen | Navigieren Sie in den Bereich Werke, wählen Sie Anlegen, und pflegen Sie die folgenden Daten:Werk: 1710 (Werk USA)Wählen Sie anschließend Übernehmen und dann Sichern. | Die Werksdaten werden gepflegt. |  |

## Anhang

Tabelle 5: Typografische Konventionen

| Format | Beschreibung |
| --- | --- |
| Beispiel | Dem Bild entnommene Wörter oder Zeichen.Dazu gehören Feldnamen, Bildtitel, Drucktastenbezeichner, Menünamen, Menüpfade und Menüoptionen.Textuelle Verweise auf andere Dokumente. |
| Beispiel | Hervorgehobene Wörter oder Ausdrücke. |
| Example | Technische Namen von Systemobjekten.Dazu gehören Reportnamen, Programmnamen, Transaktionscodes, Tabellennamen und einzelne Schlüsselbegriffe einer Programmiersprache, die von Fließtext umrahmt sind, wie z.B. SELECT und INCLUDE. |
| Beispiel | Ausgabe auf dem Bild.Dazu gehören Datei- und Verzeichnisnamen und ihre Pfade, Meldungen, Quelltext, Namen von Variablen und Parametern sowie Namen von Installations-, Upgrade- und Datenbankwerkzeugen. |
| Beispiel | Genaue Benutzereingabe.Dabei handelt es sich um Wörter und Zeichen, die Sie im System genau so eingeben, wie sie in der Dokumentation angezeigt werden. |
| <Beispiel> | Variable Benutzereingaben.Die Wörter und Zeichen in spitzen Klammern müssen Sie durch entsprechende Eingaben ersetzen, bevor Sie sie in das System eingeben. |
| Beispiel | Tasten auf der Tastatur, z. B. F2 oder ENTER. |

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
> Flagged while digesting this document, not verified: Product ID spellings differ within the document: R-ONETIME/R-SEATS/R-TICKETS vs R_ONETIME/R_SEATS/R_TICKETS, and R-TRAFFIC used in the PCS rate plan template and usage table where R-TICKETS is defined elsewhere.

> [!warning] Conflict
> Flagged while digesting this document, not verified: P-CLOUD_SUPPORT enrichment steps instruct entering product number P-CLOUD_COMM; and the UsagePrice upload step selects OneTimePrice table instead of UsagePrice.

> [!warning] Conflict
> Flagged while digesting this document, not verified: Rate plan template recurring fee priced in EUR while US country version uses USD elsewhere.

## Connections
- part-of :: [[_cluster]]
- related-to :: [[09-subscription-billing-and-contract-accounting/master-data-script-create-subscription-product-convergent-invoicing-md]]
- related-to :: [[09-subscription-billing-and-contract-accounting/mds-5lp-451]]
- related-to :: [[09-subscription-billing-and-contract-accounting/sap-s-4hana-cloud-public-edition-convergent-invoicing-mds-5lp-453]]
- related-to :: [[09-subscription-billing-and-contract-accounting/script-de-dados-mestre-criar-faturamento-convergente-de-produto-de-ass]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/5LP_S4CLD2608_Master_Data_DE_XX.docx` — full document · extracted with `mammoth` · 49,113 chars in the whole document
