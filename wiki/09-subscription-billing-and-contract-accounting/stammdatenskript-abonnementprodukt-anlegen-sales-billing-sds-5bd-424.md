---
id: 09-subscription-billing-and-contract-accounting/stammdatenskript-abonnementprodukt-anlegen-sales-billing-sds-5bd-424
title: "Stammdatenskript: Abonnementprodukt anlegen (Sales Billing) – SDS (5BD) (5BD_S4CLD2608_Master_Data_DE_XX)"
description: "German master data script (5BD) for creating subscription products in SAP Subscription Billing, Price Calculation Service and S/4HANA Cloud Public Edition 2608, US and DE variants."
cluster: 09-subscription-billing-and-contract-accounting
tags: [kb/subscription-billing-and-contract-accounting, topic/subscription-product-master-data]
aliases: [5BD_S4CLD2608_Master_Data_DE_XX]
keywords: [Subscription Products and Rate Plans, subscription products, rate elements, rate plan templates, pricing schemes, lookup tables, product master enrichment, sbpd products, sbre products, price calculation service]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/5BD_S4CLD2608_Master_Data_DE_XX.docx]
confidence: low
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-424
topic: 09-subscription-billing-and-contract-accounting/subscription-product-master-data
language: DE
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Stammdatenskript: Abonnementprodukt anlegen (Sales Billing) – SDS (5BD) (5BD_S4CLD2608_Master_Data_DE_XX)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/5BD_S4CLD2608_Master_Data_DE_XX.docx`, extracted with `mammoth`. Grouped under **Subscription Products and Rate Plans** in Subscription Billing and Contract Accounting. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

| <!-- image omitted: unnamed --> | StammdatenskriptSAP S/4HANA Cloud Public Edition - 02-07-26 |
| --- | --- |
|  | Abonnementprodukt anlegen (Sales Billing) – SDS (5BD) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Inhaltsverzeichnis

[1 Zweck 2](#_Toc233889757)

[2 Voraussetzungen 3](#_Toc233889758)

[2.1 Systemzugriff 3](#_Toc233889759)

[2.2 Rollen 3](#_Toc233889760)

[2.3 Erforderliche Organisationseinheiten (SAP S/4HANA) 3](#_Toc233889761)

[3 Übersichtstabelle 4](#_Toc233889762)

[4 Vorgehensweisen 5](#_Toc233889763)

[4.1 Abonnementprodukt anlegen (SAP Subscription Billing) 5](#_Toc233889764)

[4.1.1 Tarifelemente anlegen 5](#_Toc233889765)

[4.1.2 Tarifvorlage anlegen 7](#_Toc233889766)

[4.1.3 Ein Produkt anlegen 8](#_Toc233889767)

[4.1.4 Produkt mit einem Preisschema anlegen 9](#_Toc233889768)

[4.1.5 Suchtabellen für Preisfindung hochladen 13](#_Toc233889769)

[4.2 Abonnementprodukte anreichern (SAP S/4HANA) 17](#_Toc233889770)

[4.2.1 Subscription-Billing-Produkte vom Typ SBPD erweitern 17](#_Toc233889771)

[4.2.2 Abonnementabrechnungsprodukte vom Typ SBRE erweitern 19](#_Toc233889772)

## Zweck

Dieses Dokument beschreibt, wie Sie Stammdaten für das Abonnementprodukt anlegen. Die Beschreibung umfasst die Datensegmente, die für die Stammdaten für die Arbeit in einer üblichen Systemumgebung relevant sind. Der Leser lernt hauptsächlich, welche Datensegmente und -felder hauptsächlich mit Eingabewerten gefüllt werden müssen. Felder, die nicht für den Umfang relevant sind, werden in diesem Dokument nicht behandelt, obwohl sie möglicherweise auf der Benutzungsoberfläche angezeigt werden.

Ein wie hier beschrieben angelegter Abonnementstammsatz kann für die Abonnementabrechnung verwendet werden.

| Abonnementprodukt-ID | Beschreibung | Verwendung |
| --- | --- | --- |
| P-CLOUD_STORAGE | Abonnementprodukt | stellt das Abonnementabrechnungsprodukt dar |
| P-CLD_STORAGE_PCS | Produkt für Price Calculation Services | stellt das Preisberechnungsprodukt dar |

## Voraussetzungen

### Systemzugriff

| System | Details |
| --- | --- |
| SAP-S/4HANA-System | Zugriff möglich über SAP Fiori Launchpad. Ihr Systemadministrator stellt Ihnen die URL für den Zugriff auf die verschiedenen Apps zur Verfügung, die Ihrer Rolle zugeordnet sind. |
| SAP Subscription Billing | Zugriff über URL möglich. Ihr Systemadministrator stellt Ihnen die URL für den Zugriff auf die Anwendung zur Verfügung. |
| Price Calculation Service | Zugriff möglich über SAP Fiori Launchpad. Ihr Systemadministrator stellt Ihnen die URL für den Zugriff auf die verschiedenen Apps zur Verfügung, die Ihrer Rolle zugeordnet sind. |

### Rollen

Legen Sie Benutzerrollen mit den folgenden von SAP ausgelieferten Benutzerrollenvorlagen an, und ordnen Sie sie Ihren einzelnen Testbenutzern zu.

SAP S/4HANA

| Name | ID |
| --- | --- |
| Stammdatenexperte – Produktdaten | SAP_BR_PRODMASTER_SPECIALIST |

SAP Subscription Billing

Wenden Sie sich an Ihren Systemadministrator, um die Berechtigungseinstellungen zu erhalten.

### Erforderliche Organisationseinheiten (SAP S/4HANA)

Einige Segmente von Stammdaten hängen von den Organisationseinheiten des Unternehmens ab. Allgemeine (zentrale) Daten hängen nicht von einer Organisationseinheit oder dem Buchungskreis ab. Die folgende Tabelle stellt eine Übersicht dieser verschiedenen Datensegmente und ihrer relevanten Organisationseinheiten bereit:

| Datensegment | Hängt ab von | Zu verwendende Organisationseinheit | Zu verwendende Organisationseinheit |
| --- | --- | --- | --- |
| Stammdatensatz anlegen | Verkaufsorganisation | 1710 (Inländ. Verkaufsorganisation USA) | Für Deutschland, 1010 verwenden (Inländ. Verkaufsorganisation DE) |
| Stammdatensatz anlegen | Vertriebsweg | 10 (Direktverkauf) | 10 (Direktverkauf) |

## Übersichtstabelle

Dieser Stammdatensatz umfasst mehrere Segmente, die in der nachfolgenden Tabelle genannt sind.

| Segment | Anwendungsrolle | App/Transaktion | Erwartete Ergebnisse |
| --- | --- | --- | --- |
| Abonnementprodukt anlegen (SAP Subscription Billing) | Keine | Keine | Abonnementprodukte werden angelegt. |
| Abonnementprodukte anlegen (SAP S/4HANA) | SAP_BR_PRODMASTER_SPECIALIST | Produktstammdaten verwalten | Abonnementprodukte werden angelegt. |

## Vorgehensweisen

Dieser Abschnitt beschreibt die Vorgehensweisen für die einzelnen Segmente oder Prozessschritte, die Teil dieses Stammsatzes ist.

### Abonnementprodukt anlegen (SAP Subscription Billing)

#### Tarifelemente anlegen

Zweck

In dieser Aktivität legen Sie Tarifelemente in SAP Subscription Billing an. Die Tarif-IDs müssen den relevanten S/4HANA-Produkten der Art SBRE entsprechen:

| Tarif-ID | Tarifart | Beschreibung |
| --- | --- | --- |
| R-ONETIME | Einmalig | Einmalige Aktivierungsgebühr |
| R-SEATS | Wiederkehrend | Seat-bezogene monatliche Gebühr |
| R-TRAFFIC | Nutzungsabhängig | Traffic-bezogene Nutzungsgebühr |

Vorgehensweise

| Testschrittnummer | Bezeichnung des Testschritts | Anweisung | Erwartetes Ergebnis | Kommentare |
| --- | --- | --- | --- | --- |
| 1 | Anmelden | Melden Sie sich am SAP Subscription Billing Launchpad an. | Die Startseite wird angezeigt. |  |
| 2 | Zu Tarifelementen navigieren | Wählen Sie unter Stammdaten und Konfiguration die Option Business-Konfiguration verwalten > Tarifelemente. | Die Sicht Tarifelemente wird angezeigt. |  |
| 3 | Tarifelement anlegen: R-ONETIME | Wählen Sie Anlegen > Einmalig, und nehmen Sie anschließend folgende Einträge vor:ID: R-ONETIMEEinheit: Stück (ST)Bezeichnung: Einmalige AktivierungsgebührDatenquelle: KeineArt der einmaligen Gebühr: ErstgebührFakturaart: GebührBeschreibung: Geben Sie eine Beschreibung ein, z.B. Einmalige Aktivierungsgebühr.Aktiv: markiertWählen Sie Sichern. | Das Tarifelement R-ONETIME wird angelegt. |  |
| 4 | Tarifelement anlegen: R-SEATS | Wählen Sie Anlegen, und nehmen Sie anschließend folgende Einträge vor:Art: WiederkehrendID: R-SEATSEinheit: Stück (ST)Bezeichnung: Seat-bezogene monatliche GebührDatenquelle: AbonnementFakturaart: GebührBeschreibung: Geben Sie eine Beschreibung ein, z.B. Seat-bezogene monatliche Gebühr.Aktiv: markiertWählen Sie Sichern. | Das R-SEATS-Tarifelement wird angelegt. |  |
| 5 | Tarifelement anlegen: R-TRAFFIC | Wählen Sie Anlegen, und nehmen Sie anschließend folgende Einträge vor:Art: NutzungsabhängigID: R-TRAFFICEinheit: STÜCK (ST)Bezeichnung: Traffic-bezogene NutzungsgebührDatenquelle: NutzungFakturaart: GebührTarifunterelemente verwenden: markiert (nur für PCS-Produkte)Nutzungs-Rating-Variante: AggregiertArt der technischen Ressourcen-ID: Cloud-Speicherplatz-IDBeschreibung: Geben Sie eine Beschreibung ein, z.B. Upload/Download-Traffic.Aktiv: markiertWählen Sie Sichern. | Das R-TRAFFIC-Tarifelement wird angelegt. |  |

|  |
| --- |
| Hinweis Technische Ressourcen identifizieren den Abonnenten und den abonnierten Service in einem technischen System. Sie werden benötigt, wenn Sie Ihre Kunden basierend auf der Nutzung Ihres Service abrechnen. Beispiel: Messung des Stromverbrauchs; hier könnte die Art der technischen Ressourcen-ID als "Stromzähler-ID" definiert werden. Hierbei handelt es sich um die eindeutige ID (z.B. EM392734-A), gegen die der Verbrauch gebucht wird. In einem Szenario, in dem der Verbrauch gemessen wird, könnte die Art der technischen Ressourcen-ID als "Kfz-Zulassungsnummer" definiert werden.Hierbei handelt es sich um ein Benutzereingabefeld, das je nach Service/Szenario definiert wird. |

#### Tarifvorlage anlegen

Zweck

In dieser Aktivität legen Sie eine Tarifvorlage in SAP Subscription Billing an.

Vorgehensweise

| Testschrittnummer | Bezeichnung des Testschritts | Anweisung | Erwartetes Ergebnis | Kommentare |
| --- | --- | --- | --- | --- |
| 1 | Anmelden | Melden Sie sich an SAP Subscription Billing an. | Die Startseite wird angezeigt. |  |
| 2 | Zu Tarifvorlagen navigieren | Wählen Sie unter Preisfindung die App Tarifplanvorlagen verwalten. | Die verfügbaren Tarifvorlagen werden angezeigt. |  |
| 3 | Tarifvorlage anlegen: | Wählen Sie Anlegen > Ohne Gebührenmodell, und pflegen Sie unter Allgemeine Informationen folgende Daten:Beschreibung: Platzbasierte TarifvorlageAbrechnungszyklus: Monatlich am ersten Tag des MonatsWährung: Wert – USD (für Länderversion US) | Das Bild Tarifvorlage wird angezeigt. |  |
| 4 | Gebühren/Gutschriften für Tarifelemente pflegen | Wählen Sie im Abschnitt für Gebühren/Gutschriften die Option Gebühren/Gutschriften, wählen Sie Hinzufügen und dann Einmalig.Pflegen Sie nun folgende Daten:Tarifelement: R-ONETIMEPreiswert 100 EURWählen Sie für Gebühren/Gutschriften die Option Anlegen, wählen Sie Wiederkehrend und anschließend Gebühr mit Prozentwertpreisdefinition.Pflegen Sie nun folgende Daten:Tarifelement: R-SEATSÄnderungen mit dem nächsten Zyklus anwenden: markiertAbrechnung im Voraus: markiertErsten Zyklus anteilig berechnen: markiertPreis pro Einheit: 10 EURVerhältnis: 100Wählen Sie für Gebühren/Gutschriften die Option Hinzufügen und dann NutzungBlockpreisdefinition.Pflegen Sie nun folgende Daten:Tarifelement: R-TRAFFICTarifunterelement: Pflegen Sie das Tarifunterelement,wenn die Option Tarifunterelemente verwenden im Schritt [Tarifelemente anlegen](#unique_7) [Seite ] 5 aktiviert ist.Hinweis Tarifunterelemente sind Pflichtfelder, wenn die Option Tarifunterelemente verwenden aktiviert ist.Änderungen mit dem nächsten Zyklus anwenden: nicht markiertInklusivvolumen: Wert – 1Blockgröße: Wert – 1Preis pro Block: Wert – 1 EUR (für Länderversion DE)Wählen Sie Anlegen.Wählen Sie anschließend Veröffentlichen. | Die Gebühren/Gutschriften werden angelegt. |  |

#### Ein Produkt anlegen

Zweck

In dieser Aktivität legen Sie das Produkt P-CLOUD_STORAGE in SAP Subscription Billing an. Die ID des Produkts in SAP Subscription Billing muss der zugehörigen Produkt-ID in SAP S/4HANA entsprechen.

Vorgehensweise

| Testschrittnummer | Bezeichnung des Testschritts | Anweisung | Erwartetes Ergebnis | Kommentare |
| --- | --- | --- | --- | --- |
| 1 | Anmelden | Melden Sie sich an SAP Subscription Billing an. | Die Startseite wird angezeigt. |  |
| 2 | Zu "Produkte" navigieren | Öffnen Sie unter Stammdaten und Konfiguration die App Produkte verwalten. | Die verfügbaren Produkte werden angezeigt. |  |
| 3 | Allgemeine Produktinformationen pflegen | Wählen Sie Anlegen, und geben Sie im Bereich Allgemeine Informationen die folgenden Daten ein:Produktname: Cloud StorageProdukt-ID: P-CLOUD_STORAGEAbonnementart: KostenpflichtigAbonnements als vorläufig anlegen: EntmarkiertAbonnementprofil S/4-Integration | Die allgemeinen Informationen wurden gepflegt. |  |
| 4 | Tarif für Produkt pflegen | Wählen Sie unter Tarife den Pfad Anlegen > Ohne Preisschema, und pflegen Sie die folgenden Daten.Hinweis Wenn Sie Produkte verwenden, für die ein Preisschema erforderlich ist, müssen Sie Mit Preisschema wählen. Eine Übersicht über die Preisdefinition mit und ohne Preisschemata finden Sie in der Dokumentation zu SAP Subscription Billing unter [Preisdefinition](https://help.sap.com/docs/subscription-billing/feature-overview/pricing).Markt: US East (für Länderversion US)Tarifvorlage: Platzbasierte TarifvorlageBeschreibung: Wiederkehrender Tarif (platzbasiert)Abrechnungszyklus: Monatlich am ersten Tag des MonatsWählen Sie Anlegen. | Der Tarif wurde für das Produkt gepflegt. |  |
| 5 | Vertragsmodalitäten pflegen | Geben Sie unter Vertragsmodalitäten Folgendes ein:Erwartete Laufzeit: z.B. 12Mindestlaufzeit: 12Verlängerungslaufzeit: 12Widerrufsfrist: 14 | Die Vertragsmodalitäten werden gepflegt. |  |
| 6 | Produkt anlegen | Wählen Sie für das gesamte Produkt Anlegen.Wählen Sie anschließend Freigeben. | Das Produkt P-CLOUD_STORAGE wird angelegt. |  |

#### Produkt mit einem Preisschema anlegen

Wenn Sie einen Beispielanwendungsfall durchlaufen, können Sie entweder die Beispielwerte verwenden, um Daten von Grund auf neu anzulegen, oder Sie können die vordefinierte Konfiguration verwenden, die mit jedem neuen Tenant ausgeliefert wird. Bevor Sie ein Produkt mit einem Gebührenmodell anlegen, müssen Sie die folgenden Schritte im Price-Calculation-Service ausführen.

Eine detaillierte Beschreibung der Einrichtung der Preisdefinition mit Preisschemata (Verwendung eines Beispiels) finden Sie im [Pricing with Pricing Schemes: Configuration Guide](https://help.sap.com/docs/subscription-billing/pricing-configuration/pricing-with-pricing-schemes-configuration-guide).

Vorgehensweise

1 Feldkatalog verwalten

Wenn Sie die Beispieldaten einsetzen, wird in der App Feldkatalog verwalten ein vordefinierter Feldkatalog verwendet. Daher müssen Sie hier keine zusätzlichen Einstellungen vornehmen. Mit der App Feldkatalog verwalten können Sie Felder anlegen, die später zum Definieren der Suchtabellen und Eingabeeigenschaften für Preiselementspezifikationen verwendet werden.

2 Suchtabellen anlegen

In der App Suchtabelle verwalten können Sie Suchtabellen anlegen, indem Sie einen Satz von Eingabefeldern einem Satz von Ausgabefeldern zuordnen. Diese Suchtabellen werden dann in einem späteren Schritt verwendet, um Preiselementspezifikationen anzulegen. Das Ziel dieses Schritts besteht darin, die folgenden Suchtabellen für einmalige, wiederkehrende und Nutzungsgebühren zu erstellen:

- OneTimePrice
- RecurringPrice
- UsagePrice
- Discount1

Diese Tabellen sind Bestandteil des vordefinierten Inhalts. Daher müssen Sie in diesem Schritt keine zusätzlichen Einstellungen vornehmen.

3 Preiselementspezifikationen

In der App Preiselementspezifikationen verwalten definieren Sie Ihre Preisfindungskonfiguration, indem Sie Preiselementspezifikationen anlegen. Dazu gehört das Einrichten der Preisfindungslogik und übersteuerbarer Felder:

- OneTimePrice
- RecurringPrice
- UsagePrice
- Discount1

|  |
| --- |
| Hinweis Wenn die Preiselementspezifikationen für die oben genannten Elemente nicht gepflegt werden, müssen Sie diese in der App Preiselementspezifikationen verwalten pflegen, indem Sie die einzelnen Elemente wählen (Übersteuerbare Felder > Hinzufügen/Anlegen > Preis/Rabatt > Sichern). |

4 Preisschema

In der App Preisschema verwalten legen Sie Preisschemata an und pflegen diese. Ein Preisschema ist ein Verfahren, das die Verwendung und die Beziehung der Preiselementspezifikationen für einen bestimmten bepreisbaren Beleg definiert. Es legt außerdem die Reihenfolge zum Ausführen dieser Spezifikationen zum Generieren eines Gesamtbetrags in einem bepreisten Beleg fest.

Das Preisschema "Initial" ist Teil des vordefinierten Inhalts. Daher müssen Sie in diesem Schritt keine zusätzlichen Einstellungen vornehmen.

5 Tarifvorlage anlegen

| Testschrittnummer | Bezeichnung des Testschritts | Anweisungen | Erwartete Ergebnisse | Kommentare |
| --- | --- | --- | --- | --- |
| 1 | Anmelden | Melden Sie sich an SAP Subscription Billing an. | Die Startseite wird angezeigt. |  |
| 2 | Zur App Tarifvorlagen navigieren | Öffnen Sie Preisfindung > Tarifvorlagen verwalten | Die Tarifvorlagen werden angezeigt. |  |
| 3 | Anlegen wählen | Wählen Sie Anlegen > Mit Preisschema, und geben Sie unter Allgemeine Informationen die folgenden Daten ein:Beschreibung: RPT für PreisberechnungTags: PCS (optional)Preisschema: InitialAbrechnungszyklus: Monatlich am ersten Tag des MonatsAbrechnungsprofil: Initiale EinstellungenWährung: EUR | Die allgemeinen Informationen wurden gepflegt. |  |
| 4 | Gebühren/Gutschriften für Tarifelemente pflegen | Bei einmaligen Gebühren/Gutschriften wählen Sie Gebühren/Gutschriften > Anlegen > Einmalig und geben Tarifelement = R-ONETIME ein.Wählen Sie Details der übersteuerbaren Felder > Anlegen > Rabatt 1, und geben Sie Einmaliger Preis = markieren ein. Wählen Sie Übernehmen.Bei wiederkehrenden Gebühren/Gutschriften wählen Sie Gebühren/Gutschriften > Anlegen > Wiederkehrend und geben Tarifelement = R-SEATS ein.Wählen Sie Details der übersteuerbaren Felder > Anlegen > Rabatt 1, und geben Sie Wiederkehrender Preis = markieren ein. Wählen Sie Übernehmen.Bei Gebühren/Gutschriften mit Blockpreisdefinition wählen Sie Gebühren/Gutschriften > Anlegen > Nutzungsgutschrift mit Blockpreisdefinition/Nutzungsgebühr mit Blockpreisdefinition und geben Tarifelement = R-TRAFFIC und Tarifunterelement ein.Hinweis Tarifunterelemente sind Pflichtfelder, wenn im Schritt [Tarifelemente anlegen](#unique_7) [Seite ] 5 die Option Tarifunterelemente verwenden aktiviert ist.Wählen Sie Details der übersteuerbaren Felder > Anlegen > Rabatt 1, und geben Sie Verbrauchsbas. Preis = markieren ein. Wählen Sie Übernehmen.Wählen Sie Anlegen und dann Veröffentlichen. |  |  |

6 Produkt anlegen

Sie legen ein Produkt P-CLOUD_STORAGE_PC in SAP Subscription Billing an. Die ID des Produkts in SAP Subscription Billing muss der zugehörigen Produkt-ID in SAP S/4HANA entsprechen. Sie können folgende Vorgehensweise verwenden:

| Testschrittnummer | Bezeichnung des Testschritts | Anweisung | Erwartetes Ergebnis | Kommentare |
| --- | --- | --- | --- | --- |
| 1 | Anmelden | Melden Sie sich an SAP Subscription Billing an. | Die Startseite wird angezeigt. |  |
| 2 | Zu Produkte navigieren | Öffnen Sie unter Stammdaten und Konfiguration die App Produkte verwalten. | Die verfügbaren Produkte werden angezeigt. |  |
| 3 | Allgemeine Produktinformationen pflegen | Wählen Sie Anlegen, und geben Sie im Bereich Allgemeine Informationen die folgenden Daten ein:Produktname: Preisberechnung für Cloud-SpeicherProdukt-ID: P-CLOUD_STORAGE_PCAbonnementart: KostenpflichtigAbonnements als vorläufig anlegen: Entmarkiert | Die allgemeinen Informationen wurden gepflegt. |  |
| 4 | Tarif für Produkt pflegen | Wählen Sie auf der Registerkarte Tarife die Option Anlegen - > Mit Preisschema. Navigieren Sie zu Vorlage anlegen, und pflegen Sie die folgenden Daten:Markt: US East (für Länderversion US)Tarifvorlage: RPT für PreisberechnungBeschreibung: RPT für PreisberechnungAbrechnungszyklus: Monatlich am ersten Tag des MonatsWählen Sie Anlegen. | Der Tarif wurde für das Produkt gepflegt. |  |
| 5 | Vertragsmodalitäten pflegen | Pflegen Sie unter Abonnementparameter im Bereich Vertragsmodalitäten folgende Daten:Erwartete Laufzeit: z.B. 12Mindestlaufzeit: 12Verlängerungslaufzeit: 12Widerrufsfrist: 14 | Die Vertragsmodalitäten werden gepflegt. |  |
| 6 | Produkt anlegen | Wählen Sie in der Sicht Produkt die Option Anlegen.Wählen Sie Veröffentlichen. | Das Produkt P-CLOUD_STORAGE_PC wird angelegt. |  |

7 Suchtabellen für Preisfindung hochladen

Weitere Informationen zum Hochladen von Suchtabellen finden Sie unter [Suchtabellen für Preisfindung hochladen](#unique_11) [Seite ] 13.

#### Suchtabellen für Preisfindung hochladen

Sie können Ihre Suchtabellen für einmalige, wiederkehrende und nutzungsabhängige Gebühren und für den Rabatt hochladen, indem Sie folgende Vorgehensweise nutzen. Die Daten in der resultierenden Tabelle werden verwendet, um die relevanten Preise während der Preisfindung im Rahmen des Rating-Prozesses zu finden.

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
| 3 | UsagePrice wählen | Wählen Sie die Suchtabelle UsagePrice aus.Laden Sie die leere Tabelle herunter, und speichern Sie sie lokal als CSV-Datei.Tipp Wenn das Format der heruntergeladenen Datei nicht spaltengetrennt ist, müssen Sie das Format der Tabelle in ein US-Format ändern. |  |  |
| 4 | Heruntergeladene Datei aktualisieren | Geben Sie die folgenden Werte ein, und sichern Sie die Datei:Produktcode: P-CLOUD_STORAGE_PCMarkt-ID: A1Tarifelement: R-TRAFFICPreis: VolumenPreis (Preisart): LinearDie folgenden spezifischen Werte sind für jede Stufe eines Unterelements mit hohem Tarif verfügbar:Tarifunterelement: HochPreis (Bereich): 500Preis (Bereichseinheit): EAPreis (Wert) 30Preis (Wertwährung): USDPreis (Mengenwert): 1Preis (Mengeneinheit): EADie folgenden spezifischen Werte sind für jede Stufe verfügbar:Tarifunterelement: HochPreis (Bereich): 1000Preis (Bereichseinheit): EAPreis (Wert) 25Preis (Wertwährung): USDPreis (Mengenwert): 1Preis (Mengeneinheit): EADie folgenden spezifischen Werte sind für jede Stufe verfügbar:Tarifunterelement: HochPreis (Bereich):Preis (Bereichseinheit): EAPreis (Wert) 20Preis (Wertwährung): USDPreis (Mengenwert): 1Preis (Mengeneinheit): EADie folgenden spezifischen Werte sind für jede Stufe eines Unterelements mit niedrigem Tarif verfügbar:Tarifunterelement: NiedrigPreis (Bereich): 500Preis (Bereichseinheit): EAPreis (Wert) 15Preis (Wertwährung): USDPreis (Mengenwert): 1Preis (Mengeneinheit): EADie folgenden spezifischen Werte sind für jede Stufe eines Unterelements mit niedrigem Tarif verfügbar:Tarifunterelement: NiedrigPreis (Bereich): 1000Preis (Bereichseinheit): EAPreis (Wert) 10Preis (Wertwährung): USDPreis (Mengenwert): 1Preis (Mengeneinheit): EADie folgenden spezifischen Werte sind für jede Stufe eines Unterelements mit niedrigem Tarif verfügbar:Tarifunterelement: NiedrigPreis (Bereich):Preis (Bereichseinheit): EAPreis (Wert) 5Preis (Wertwährung): USDPreis (Mengenwert): 1Preis (Mengeneinheit): EA |  |  |
| 5 | CSV-Datei hochladen | Wählen Sie die Suchtabelle UsagePrice, und wechseln Sie zu Importieren > Durchsuchen, um die gesicherte Datei aus dem vorherigen Schritt hochzuladen.Hinweis Es gibt zwei Arten von Importen. Wählen Sie Zusammenführen, um die vorhandenen Daten intakt zu halten.Wählen Sie Importieren. | Die Suchtabelle UsagePrice wird aktualisiert. |  |

Tabelle 4: Rabatttabelle hochladen

| Testschrittnummer | Bezeichnung des Testschritts | Anweisungen | Erwartetes Ergebnis | Kommentare |
| --- | --- | --- | --- | --- |
| 1 | Anmelden | Melden Sie sich bei SAP Price Calculation an. | Die Startseite wird angezeigt. |  |
| 2 | Zu Tarifvorlagen navigieren | Öffnen Sie unter Master Data Managementdie App Suchtabelleninhalt pflegen. | Die Suchtabellen werden angezeigt. |  |
| 3 | Discount1 wählen | Wählen Sie die Suchtabelle Discount1 aus.Laden Sie die leere Tabelle herunter, und speichern Sie sie lokal als CSV-Datei.Tipp Wenn das Format der heruntergeladenen Datei nicht spaltengetrennt ist, müssen Sie das Format der Tabelle in ein US-Format ändern. |  |  |
| 4 | Heruntergeladene Datei aktualisieren | Geben Sie die folgenden Werte ein, und sichern Sie die Datei:Markt-ID: A1Rabatt: EinzelnRabatt (Preisart): ProzentsatzRabatt (Wert): 0,1 |  |  |
| 5 | CSV-Datei hochladen | Wählen Sie die Suchtabelle Discount1, und wechseln Sie zu Importieren > Durchsuchen, um die gesicherte Datei aus dem vorherigen Schritt hochzuladen.Hinweis Es gibt zwei Arten von Importen. Wählen Sie Zusammenführen, um die vorhandenen Daten intakt zu halten.Wählen Sie Importieren. | Die Suchtabelle Discount1 wird aktualisiert. |  |

### Abonnementprodukte anreichern (SAP S/4HANA)

#### Subscription-Billing-Produkte vom Typ SBPD erweitern

Zweck

In dieser Aktivität erweitern Sie das Subscription-Billing-Produkt P-CLOUD_STORAGE in SAP S/4HANA. Dieses Produkt wird in Subscription Billing angelegt, nach SAP S/4HANA repliziert und steht zur Verfügung, sobald die Replikation von Produkten im Rahmen des Umfangsbestandteils 57Z eingerichtet ist. Weitere Informationen zur Replikation von Produkten erhalten Sie unter [iFlow-Paket für Replikation von Produkten und Tarifelementen konfigurieren](https://help.sap.com/docs/CLOUD_TO_CASH_OD/a78a4be305be4dbc903bd826a1aba456/93e79ab9ec8e4dc49bc1710e396608ed.html).

|  |
| --- |
| Hinweis Für eine ordnungsgemäße Steuerberechnung sind für Brasilien spezifische Felder erforderlich. Weitere Informationen hierzu finden Sie unter Materialstammdaten > BR-spezifische Felder für Stammdaten definieren > Stammdaten für Brasilien anlegen (JD0_BR). |

Vorgehensweise

| Testschrittnummer | Bezeichnung des Testschritts | Anweisung | Erwartetes Ergebnis | Kommentare |
| --- | --- | --- | --- | --- |
| 1 | Anmelden | Melden Sie sich am SAP Fiori Launchpad als Stammdatenexperte – Produktdaten an. | Die Startseite wird angezeigt. |  |
| 2 | SAP-Fiori-App aufrufen | Wählen Sie die Kachel Produktstammdaten verwalten. | Die App Produktstammdaten verwalten wird angezeigt. |  |
| 3 | Produkt suchen | Geben Sie oben im Suchbereich das Produkt P-CLOUD_ STORAGE und P-CLOUD_ STORAGE_PC ein.Wählen Sie Start. | Ihr Produkt wird in der Berichtsliste angezeigt. |  |
| 4 | Produkt öffnen und Vertriebslinien pflegen: Allgemeine Informationen | Wählen Sie das Produkt aus der Berichtsliste aus.Produktnummer: P-CLOUD_STORAGEBasismengeneinheit: STProduktart: SBPD (Sub.- Billing-Produkt)Beschreibung: Cloud StorageWählen Sie anschließend OK.Hinweis Geben Sie unter Beschreibung die Details zu Sprache und Produkt für eine bestimmte Region an, z.B. Sprache: Deutsch und Produkt: Abonnementabrechnungsprodukt. | Das Produkt sollte offen sein, und allgemeine Informationen werden gepflegt. |  |
| 5 | Vertriebslinie pflegen: Allgemeine Informationen | Wählen Sie in der Sicht Produkt im Bereich Vertriebslinien die Option Anlegen, und geben Sie folgende Daten ein:Verkaufsorganisation: 1710 (Inländ. Verkaufsorganisation USA)Vertriebsweg: 10 (Direktverkauf)Hinweis Die Vertriebslinie ist für die Produktart SBPD nicht erforderlich, wenn Sie MDI verwenden. Sie ist nur erforderlich, wenn Sie Cloud Integration verwenden. |  | Pflegen Sie für die Länderversion Deutschland statt 1710 den folgenden Wert:Verkaufsorganisation: 1010 (Inländ. Verkaufsorganisation DE)Die anderen Einträge sind für beide Länder gleich. |
| 6 | Vertriebslinie pflegen: Gruppierungsbegriffe | Wechseln Sie auf die Registerkarte Gruppierungsbegriffe, und geben Sie folgende Daten ein:Positionstypengruppe: SBPD (Sub.- Billing-Produkt)Kontierungsgruppe: X9 (Periodischer Service)Steuerklassifikation: 1 (volle Steuer)Wählen Sie anschließend Übernehmen > Anlegen.Hinweis Die Positionstypengruppe ist für die Produktart SBPD nicht erforderlich, wenn Sie MDI verwenden. Sie ist nur erforderlich, wenn Sie Cloud Integration verwenden. | Gruppierungsbegriffe werden gepflegt, und das Produkt wird gesichert. | Pflegen Sie für die Länderversion Deutschland statt 1 (Volle Steuer) den folgenden Wert:Steuerklassifikation: 6 (Volle Steuer (Services))Die anderen Einträge sind für beide Länder gleich. |
| 7 | Werke pflegen | Navigieren Sie zu Werke > Anlegen, und pflegen Sie die folgenden Daten:Werk: 1710 (Werk USA)Wählen Sie Übernehmen > Sichern. | Die Werksdaten werden gepflegt. |  |

#### Abonnementabrechnungsprodukte vom Typ SBRE erweitern

Zweck

In dieser Aktivität erweitern Sie die folgenden Subskriptionsprodukte in SAP S/4HANA, die Tarifelementen in SAP Subscription Billing entsprechen: Die Produkte werden in SAP Subscription Billing angelegt und nach SAP S/4HANA repliziert. Die Tarifelemente sind verfügbar, sobald die Replikation von Produkten wie im Einrichtungsleitfaden des Umfangsbestandteils 57Z oder unter [Replikation von Produkten und Tarifelementen](https://help.sap.com/docs/CLOUD_TO_CASH_OD/a78a4be305be4dbc903bd826a1aba456/9dbec8b5ce1841a6a39f0af5571ed63b.html?version=latest) beschrieben eingerichtet ist.

|  |
| --- |
| Hinweis Für eine ordnungsgemäße Steuerberechnung sind für Brasilien spezifische Felder erforderlich. Weitere Informationen hierzu finden Sie unter Materialstammdaten > BR-spezifische Felder für Stammdaten definieren > Stammdaten für Brasilien anlegen (JD0_BR). |

| Produkt-ID | Produktart | Beschreibung |
| --- | --- | --- |
| R-ONETIME | SBRE | Einmalige Aktivierungsgebühr |
| R-SEATS | SBRE | Seat-bezogene monatliche Gebühr |
| R-TRAFFIC | SBRE | Traffic-bezogene Nutzungsgebühr |

Vorgehensweise

Produkt: R-ONETIME

| Testschrittnummer | Bezeichnung des Testschritts | Anweisung | Erwartetes Ergebnis | Kommentare |
| --- | --- | --- | --- | --- |
| 1 | Anmelden | Melden Sie sich am SAP Fiori Launchpad als Stammdatenexperte – Produktdaten an. | Die Startseite wird angezeigt. |  |
| 2 | SAP-Fiori-App aufrufen | Wählen Sie die Kachel Produktstammdaten verwalten. | Die App Produktstammdaten verwalten wird angezeigt. |  |
| 3 | Produkt suchen | Geben Sie oben im Suchbereich das folgende Produkt ein: R-ONETIME.Wählen Sie Start. | Ihr Produkt wird in der Berichtsliste angezeigt. |  |
| 4 | Produkt öffnen und Vertriebslinien pflegen: Allgemeine Informationen | Wählen Sie in der Sicht Produkt im Bereich Vertriebslinien die Option Anlegen, und geben Sie folgende Daten ein:Verkaufsorganisation: 1710 (Inländ. Verkaufsorganisation USA)Vertriebsweg: 10 (Direktverkauf)Hinweis Geben Sie unter Beschreibung die Details zu Sprache und Produkt für eine bestimmte Region an, z.B. Sprache: Deutsch und Produkt: Abonnementabrechnungsprodukt. | Das Produkt sollte offen sein, und allgemeine Informationen werden gepflegt. | Pflegen Sie für die Länderversion Deutschland statt 1710 den folgenden Wert:Verkaufsorganisation: 1010 (Inländ. Verkaufsorganisation DE)Die anderen Einträge sind für beide Länder gleich. |
| 5 | Vertriebslinie pflegen: Gruppierungsbegriffe | Wechseln Sie auf die Registerkarte Gruppierungsbegriffe, und geben Sie folgende Daten ein:Kontierungsgruppe: X9 (Periodischer Service)Steuerklassifikation: 1 (volle Steuer)Wählen Sie anschließend Übernehmen und dann Anlegen.Hinweis Die Positionstypengruppe ist für die Produktart SBRE nicht erforderlich, wenn Sie MDI verwenden. | Gruppierungsbegriffe werden gepflegt, und das Produkt wird gesichert. | Pflegen Sie für die Länderversion Deutschland statt 1 (Volle Steuer) den folgenden Wert:Steuerklassifikation: 6 (Volle Steuer (Services))Die anderen Einträge sind für beide Versionen gleich. |
| 6 | Werke pflegen | Navigieren Sie in den Bereich Werke, wählen Sie Anlegen, und pflegen Sie die folgenden Daten:Werk: 1710 (Werk USA)Wählen Sie Übernehmen und Sichern. | Die Werksdaten werden gepflegt. | Pflegen Sie für die Länderversion Deutschland den folgenden Wert:Werk: Werk 10101 (Werk DE) |

Produkt: R-SEATS

| Testschrittnummer | Bezeichnung des Testschritts | Anweisung | Erwartetes Ergebnis | Kommentare |
| --- | --- | --- | --- | --- |
| 1 | Anmelden | Melden Sie sich am SAP Fiori Launchpad als Stammdatenexperte – Produktdaten an. | Die Startseite wird angezeigt. |  |
| 2 | SAP-Fiori-App aufrufen | Wählen Sie die Kachel Produktstammdaten verwalten. | Die App Produktstammdaten verwalten wird angezeigt. |  |
| 3 | Produkt suchen | Geben Sie oben im Suchbereichfolgendes Produkt ein: R-SEATSWählen Sie Starten. | Ihr Produkt wird in der Berichtsliste angezeigt. |  |
| 4 | Produkt öffnen und Vertriebslinien pflegen: Allgemeine Informationen | Wählen Sie in der Sicht Produkt im Bereich Vertriebslinien die Option Anlegen, und geben Sie folgende Daten ein:Verkaufsorganisation: 1710 (Inländ. Verkaufsorganisation USA)Vertriebsweg: 10 (Direktverkauf)Hinweis Geben Sie unter Beschreibung die Details zu Sprache und Produkt für eine bestimmte Region an, z.B. Sprache: Deutsch und Produkt: Abonnementabrechnungsprodukt. | Das Produkt sollte offen sein, und allgemeine Informationen werden gepflegt. | Pflegen Sie für die Länderversion Deutschland statt 1710 den folgenden Wert:Verkaufsorganisation: 1010 (Inländ. Verkaufsorganisation DE)Die anderen Einträge sind für beide Länder gleich. |
| 5 | Vertriebslinie pflegen: Gruppierungsbegriffe | Wechseln Sie auf die Registerkarte Gruppierungsbegriffe, und geben Sie folgende Daten ein:Kontierungsgruppe: X9 (Periodischer Service)Steuerklassifikation: 1 (volle Steuer)Wählen Sie anschließend Übernehmen. | Gruppierungsbegriffe werden gepflegt, und das Produkt wird gesichert. | Pflegen Sie für die Länderversion Deutschland statt 1 (Volle Steuer) den folgenden Wert:Steuerklassifikation: 6 (Volle Steuer (Services))Die anderen Einträge sind für beide Versionen gleich. |
| 6 | Werke pflegen | Navigieren Sie in den Bereich Werke, wählen Sie Anlegen, und pflegen Sie die folgenden Daten:Werk: 1710 (Werk USA)Wählen Sie Übernehmen und Sichern. | Die Werksdaten werden gepflegt. | Pflegen Sie für die Länderversion Deutschland den folgenden Wert:Werk: Werk 1010 (Werk DE) |

Produkt: R-TRAFFIC

| Testschrittnummer | Bezeichnung des Testschritts | Anweisung | Erwartetes Ergebnis | Kommentare |
| --- | --- | --- | --- | --- |
| 1 | Anmelden | Melden Sie sich am SAP Fiori Launchpad als Stammdatenexperte – Produktdaten an. | Die Startseite wird angezeigt. |  |
| 2 | SAP-Fiori-App aufrufen | Wählen Sie die Kachel Produktstammdaten verwalten. | Die App Produktstammdaten verwalten wird angezeigt. |  |
| 3 | Produkt suchen | Geben Sie oben im Suchbereichfolgendes Produkt ein: R-TRAFFICWählen Sie Starten. | Ihr Produkt wird in der Berichtsliste angezeigt. |  |
| 4 | Produkt öffnen und Vertriebslinien pflegen: Allgemeine Informationen | Wählen Sie in der Sicht Produkt im Bereich Vertriebslinien die Option Anlegen, und geben Sie folgende Daten ein:Verkaufsorganisation: 1710 (Inländ. Verkaufsorganisation USA)Vertriebsweg: 10 (Direktverkauf)Hinweis Geben Sie unter Beschreibung die Details zu Sprache und Produkt für eine bestimmte Region an, z.B. Sprache: Deutsch und Produkt: Abonnementabrechnungsprodukt. | Das Produkt sollte offen sein, und allgemeine Informationen werden gepflegt. | Pflegen Sie für die Länderversion Deutschland statt 1710 den folgenden Wert:Verkaufsorganisation: 1010 (Inländ. Verkaufsorganisation DE)Die anderen Einträge sind für beide Länder gleich. |
| 5 | Vertriebslinie pflegen: Gruppierungsbegriffe | Wechseln Sie auf die Registerkarte Gruppierungsbegriffe, und geben Sie folgende Daten ein:Positionstypengruppe: SBRE (AbonnAbrech. - Tarifelem.)Kontierungsgruppe: X9 (Periodischer Service)Steuerklassifikation: 1 (volle Steuer)Wählen Sie Übernehmen und anschließend Sichern.Hinweis Die Positionstypengruppe ist für das Produkt SBRE nicht erforderlich, wenn Sie MDI verwenden. | Das Produkt wird gesichert. | Pflegen Sie für die lokale Version Deutschland statt 1 (Volle Steuer) folgenden Wert:Steuerklassifikation: 6 (Volle Steuer (Services))Die anderen Einträge sind für beide Versionen gleich. |
| 6 | Werke pflegen | Navigieren Sie in den Bereich Werke, wählen Sie Anlegen, und pflegen Sie die folgenden Daten:Werk: 1710 (Werk USA)Wählen Sie Übernehmen und anschließend Sichern. | Die Werksdaten werden gepflegt. | Pflegen Sie für die Länderversion Deutschland den folgenden Wert: Werk: Werk 10101 (Werk DE) |

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
> Flagged while digesting this document, not verified: DE plant for R-ONETIME and R-TRAFFIC is given as 10101, but for R-SEATS as 1010; the document is internally inconsistent.

> [!warning] Conflict
> Flagged while digesting this document, not verified: Intro table lists price calculation product P-CLD_STORAGE_PCS, but procedures create P-CLOUD_STORAGE_PC.

> [!warning] Conflict
> Flagged while digesting this document, not verified: Rate plan template uses USD currency for the US version while the price for R-ONETIME is stated as 100 EUR.

## Connections
- part-of :: [[_cluster]]
- related-to :: [[09-subscription-billing-and-contract-accounting/master-data-script-create-subscription-product-sales-billing-mds-5bd-4]]
- related-to :: [[09-subscription-billing-and-contract-accounting/mds-5bd-429]]
- related-to :: [[09-subscription-billing-and-contract-accounting/sap-s-4hana-cloud-public-edition-mds-5bd-427]]
- related-to :: [[09-subscription-billing-and-contract-accounting/script-de-dados-mestre-criar-faturamento-de-vendas-de-produto-de-assin]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/5BD_S4CLD2608_Master_Data_DE_XX.docx` — full document · extracted with `mammoth` · 39,757 chars in the whole document
