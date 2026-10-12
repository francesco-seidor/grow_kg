---
id: 14-maintenance-service-and-projects/stammdatenskript-konfigurierbares-serviceprodukt-anlegen-sds-5be-430
title: "Stammdatenskript: Konfigurierbares Serviceprodukt anlegen – SDS (5BE) (5BE_S4CLD2608_Master_Data_DE_XX)"
description: "German SAP S/4HANA Cloud Public Edition 2608 master data script (5BE): create configurable service products for service contracts/orders, variant classes, profiles, prices."
cluster: 14-maintenance-service-and-projects
tags: [kb/maintenance-service-and-projects, topic/configurable-service-products]
aliases: [5BE_S4CLD2608_Master_Data_DE_XX]
keywords: [Configurable Service Products and Advanced Variant…, configurable service product, service contracts, service orders, characteristics and classes, configuration profile, variant pricing, material variant, variant configuration, user roles]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/5BE_S4CLD2608_Master_Data_DE_XX.docx]
confidence: high
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-430
topic: 14-maintenance-service-and-projects/configurable-service-products
language: DE
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Stammdatenskript: Konfigurierbares Serviceprodukt anlegen – SDS (5BE) (5BE_S4CLD2608_Master_Data_DE_XX)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/5BE_S4CLD2608_Master_Data_DE_XX.docx`, extracted with `mammoth`. Grouped under **Configurable Service Products and Advanced Variant Configuration** in Maintenance, Service and Projects. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

| <!-- image omitted: unnamed --> | StammdatenskriptSAP S/4HANA Cloud Public Edition - 02-07-26 |
| --- | --- |
|  | Konfigurierbares Serviceprodukt anlegen – SDS (5BE) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Inhaltsverzeichnis

[1 Zweck 3](#_Toc233889745)

[2 Voraussetzungen 4](#_Toc233889746)

[2.1 Systemzugriff 4](#_Toc233889747)

[2.2 Rollen 4](#_Toc233889748)

[2.3 Erforderliche Organisationseinheiten 4](#_Toc233889749)

[2.4 Obligatorische und operative Stammdaten 5](#_Toc233889750)

[2.5 Vorbereitende Schritte (obligatorisch) 5](#_Toc233889751)

[3 Übersichtstabelle 7](#_Toc233889752)

[4 Vorgehensweisen 8](#_Toc233889753)

[4.1 Konfigurierbares Serviceprodukt für Serviceverträge anlegen 8](#_Toc233889754)

[4.1.1 Merkmale anlegen 8](#_Toc233889755)

[4.1.2 Klasse anlegen 10](#_Toc233889756)

[4.1.3 Konfigurierbares Serviceprodukt für Verträge anlegen 11](#_Toc233889757)

[4.1.4 Konfigurationsprofil anlegen 14](#_Toc233889758)

[4.1.5 Preise bestimmen 15](#_Toc233889759)

[4.2 Konfigurierbares Serviceprodukt für Serviceaufträge anlegen 17](#_Toc233889760)

[4.2.1 Merkmale anlegen 17](#_Toc233889761)

[4.2.2 Klasse anlegen 21](#_Toc233889762)

[4.2.3 Konfigurierbares Serviceprodukt für Serviceaufträge anlegen 22](#_Toc233889763)

[4.2.4 Konfigurationsprofil anlegen 24](#_Toc233889764)

[4.2.5 Preise bestimmen 25](#_Toc233889765)

[4.3 Materialvariante für ein Serviceprodukt anlegen 28](#_Toc233889766)

[4.3.1 Preise für Materialvariante festlegen 30](#_Toc233889767)

## Zweck

In diesem Dokument wird beschrieben, wie Sie ein konfigurierbares Serviceprodukt für Serviceverträge und Serviceaufträge sowie die zugehörigen Preise anlegen. Die Beschreibung umfasst die Datensegmente, die für die Stammdaten für die Arbeit in einer üblichen Systemumgebung relevant sind. Der Leser lernt hauptsächlich, welche Datensegmente und -felder hauptsächlich mit Eingabewerten gefüllt werden müssen. Felder, die für den durch von SAP Best Practices bereitgestellten Umfang der Content-Auslieferung in S/4HANA nicht relevant sind, werden in diesem Dokument nicht behandelt, obwohl sie möglicherweise in der Benutzeroberfläche angezeigt werden.

Konfigurierbare Serviceprodukte, das wie hier beschrieben angelegt wurden, können für die Servicevertrags- und Serviceauftragsbearbeitung verwendet werden. Informationen zur Verwendung des konfigurierbaren Serviceprodukts finden Sie im Umfangsbestandteil Servicemanagement mit erweiterter Variantenkonfiguration (6GS) oder Servicevertragsmanagement mit erweiterter Variantenkonfiguration (6GU).

Die Funktionalität der Produktkonfiguration, die in Serviceverträgen und Serviceaufträgen verwendet werden kann, entspricht der Beschreibung im Umfangsbestandteil 22T – Konfigurierbares Modell mithilfe der Variantenkonfiguration einrichten.

## Voraussetzungen

### Systemzugriff

| System | Details |
| --- | --- |
| System | Erreichbar über SAP Fiori Launchpad. Ihr Systemadministrator stellt Ihnen die URL für den Zugriff auf die verschiedenen Apps zur Verfügung, die Ihrer Rolle zugeordnet sind. |

### Rollen

Legen Sie Benutzerrollen mit den folgenden von SAP ausgelieferten Benutzerrollenvorlagen an, und ordnen Sie sie Ihren einzelnen Testbenutzern zu.

| Name | ID |
| --- | --- |
| Produktkonfigurationsmodellierer | SAP_BR_PRODUCT_CONFIG_MODELER |
| Stammdatenexperte – Produktdaten | SAP_BR_PRODMASTER_SPECIALIST |
| Preisfindungssachbearbeiter | SAP_BR_PRICING_SPECIALIST |

Darüber hinaus ist die folgende Rolle für den Konfigurationsbenutzer relevant, der sich um die obligatorischen vorbereitenden Schritte kümmert, die unten beschrieben werden:

| Name | ID |
| --- | --- |
| Konfigurationsexperte – Geschäftsprozesskonfiguration | SAP_BR_BPC_EXPERT |

### Erforderliche Organisationseinheiten

Einige Segmente von Stammdaten hängen von den Organisationseinheiten des Unternehmens ab. Allgemeine (zentrale) Daten hängen nicht von einer Organisationseinheit oder dem Buchungskreis ab. Die folgende Tabelle stellt eine Übersicht dieser verschiedenen Datensegmente und ihrer relevanten Organisationseinheiten bereit:

| Datensegment | Hängt ab von | Zu verwendende Organisationseinheit | Kommentare |
| --- | --- | --- | --- |
| Material anlegen | Werk | 1710 (Werk 1 USA) | Für Deutschland, 1010 verwenden (Werk 1 DE) |
| Material anlegen | Verkaufsorganisation | 1710 (Inländ. Verkaufsorganisation USA) | Für Deutschland, 1010 verwenden (Inländ. Verkaufsorganisation DE) |
| Material anlegen | Vertriebsweg | 10 (Direktverkauf) | Für Deutschland, 10 verwenden (Direktverkauf) |

### Obligatorische und operative Stammdaten

Materialstammdatensätze können auf andere Stammdaten verweisen. Die folgende Tabelle bietet eine Übersicht über die optionalen und obligatorischen Stammdatenobjekte, die in einem Materialstammdatensatz verwendet werden müssen.

|  |
| --- |
| Hinweis Für eine ordnungsgemäße Steuerberechnung sind brasilienspezifische Felder erforderlich.Prüfen Sie Nota Fiscal – Brasilien - JD0 im Kapitel BR-spezifische Felder für Stammdaten definieren für Materialstammdaten. |

| Stammdatenobjekt | Verwendet im Datensegment | Obligatorisch / optional | Kommentare |
| --- | --- | --- | --- |
| Profitcenter |  | obligatorisch | Für einwandfreie Bewertungsprozesse ist die Zuweisung eines Profitcenters zu einem Material- oder Produktstamm erforderlich. |

### Vorbereitende Schritte (obligatorisch)

Verwendung

Bevor Sie das konfigurierbare Serviceprodukt wie in der folgenden Vorgehensweise beschrieben anlegen, müssen Sie die vorhandene Materialart SERV (Services) für die Verwendung von Klassifizierungsdaten aktivieren.

Vorgehensweise

| Testschrittnummer | Bezeichnung des Testschritts | Anweisung | Erwartetes Ergebnis | Kommentare |
| --- | --- | --- | --- | --- |
| 1 | Anmelden | Melden Sie sich am SAP Fiori Launchpad als Konfigurationsexperte – Geschäftsprozesskonfiguration an. | Das SAP Fiori Launchpad wird angezeigt. |  |
| 2 | App aufrufen | Öffnen Sie die App Lösung verwalten. | Die App Lösung verwalten wird angezeigt. |  |
| 3 | Lösung konfigurieren | Wählen Sie auf dem Bild Lösung verwalten die Option Lösung konfigurieren. | Das Bild Lösung konfigurieren: Realisierungsphase wird angezeigt. |  |
| 4 | Produktposition für Konfiguration öffnen | Geben Sie in den Suchfiltern folgende Daten ein:Anwendungsbereich: <Database and Data Management>Subanwendungsbereich: ProduktWählen Sie in den Suchergebnissen den Datensatz Produkt. | Das Bild Lösung konfigurieren - Produkt wird angezeigt. |  |
| 5 | Lösung konfigurieren - Produkt | Wählen Sie im Abschnitt Konfigurationsschritte für Eigenschaften der Materialarten festlegen die Option Konfigurieren. | Das Bild Eigenschaften der Materialarten festlegen: Ändern wird angezeigt. |  |
| 6 | "Attribute der Materialart SERV" öffnen | Doppelklicken Sie auf den Eintrag SERV – Serviceprodukt. | Das Bild Eigenschaften der Materialarten festlegen: Ändern: Details wird angezeigt. |  |
| 7 | Klassifizierung aktivieren | Wählen Sie in der Liste Fachbereiche die Option Klassifizierung.Achtung Bevor Sie die Änderungen in der Konfiguration sichern, stellen Sie sicher, dass die bereits vorhandenen Selektionen in der Liste Fachbereiche ebenfalls ausgewählt sind. |  |  |
| 8 | Daten sichern | Wählen Sie Sichern. |  |  |

Ergebnis

Beim Anlegen von Produkten der Art SERV – Serviceprodukt ist die Registerkarte Klassifizierung aktiviert.

## Übersichtstabelle

Dieser Stammdatensatz umfasst mehrere Segmente, die in der nachfolgenden Tabelle genannt sind.

| Segment | Anwendungsrolle | App/Transaktion | Erwartete Ergebnisse |
| --- | --- | --- | --- |
| [Merkmale anlegen](#unique_8) [Seite ] 8 | SAP_BR_PRODUCT_CONFIG_MODELER | Merkmale verwalten | Merkmale für die Servicevertragsklasse werden angelegt. |
| [Klasse anlegen](#unique_9) [Seite ] 10 | SAP_BR_PRODUCT_CONFIG_MODELER | Klassen verwalten | Eine Klasse wird angelegt. |
| [Konfigurierbares Serviceprodukt für Verträge anlegen](#unique_10) [Seite ] 11 | SAP_BR_PRODMASTER_SPECIALIST | Material anlegen | Das Serviceprodukt für Serviceverträge wird angelegt. |
| [Konfigurationsprofil anlegen](#unique_11) [Seite ] 14 | SAP_BR_PRODUCT_CONFIG_MODELER | VC-Modellierungsumgebung | Das Konfigurationsprofil wird angelegt. |
| [Preise bestimmen](#unique_12) [Seite ] 15 | SAP_BR_PRICING_SPECIALIST | Materialpreise festlegen. | Die Preise werden definiert. |
| [Merkmale anlegen](#unique_13) [Seite ] 17 | SAP_BR_PRODUCT_CONFIG_MODELER | Merkmale verwalten | Merkmale für die Servicevertragsklasse werden angelegt. |
| [Klasse anlegen](#unique_14) [Seite ] 21 | SAP_BR_PRODUCT_CONFIG_MODELER | Klassen verwalten | Eine Klasse wird angelegt. |
| [Konfigurierbares Serviceprodukt für Serviceaufträge anlegen](#unique_15) [Seite ] 22 | SAP_BR_PRODMASTER_SPECIALIST | Material anlegen | Das Serviceprodukt für den Serviceauftrag wird angelegt. |
| [Konfigurationsprofil anlegen](#unique_16) [Seite ] 24 | SAP_BR_PRODUCT_CONFIG_MODELER | VC-Modellierungsumgebung | Das Konfigurationsprofil wird angelegt. |
| [Preise bestimmen](#unique_17) [Seite ] 25 | SAP_BR_PRICING_SPECIALIST | Materialpreise festlegen. | Preise für Serviceprodukte werden definiert. |
| [Materialvariante für ein Serviceprodukt anlegen](#unique_18) [Seite ] 28 | SAP_BR_PRODMASTER_SPECIALIST | Material anlegen | Eine Materialvariante für ein konfigurierbares Serviceprodukt wird angelegt. |
| [Preise für Materialvariante festlegen](#unique_19) [Seite ] 30 | SAP_BR_PRICING_SPECIALIST | Materialpreise festlegen. | Der Preis für eine Materialvariante wird definiert. |

## Vorgehensweisen

Dieser Abschnitt beschreibt die Vorgehensweisen für die einzelnen Segmente oder Prozessschritte, die Teil dieses Stammsatzes ist.

### Konfigurierbares Serviceprodukt für Serviceverträge anlegen

#### Merkmale anlegen

Zweck

In dieser Aktivität legen Sie Merkmale an, die im konfigurierbaren Serviceprodukt zur Auswahl stehen sollen und für die Sie individuelle Variantenpreise pflegen können.

Vorgehensweise

Merkmal VARKOND (Variantenkonditionsschlüssel)

| Testschrittnummer | Bezeichnung des Testschritts | Anweisung | Erwartetes Ergebnis | Kommentare |
| --- | --- | --- | --- | --- |
| 1 | Anmelden | Melden Sie sich am SAP Fiori Launchpad als Produktkonfigurationsmodellierer an. | Die Startseite wird angezeigt. |  |
| 2 | App aufrufen | Öffnen Sie Merkmale verwalten.Pflegen Sie auf dem Bild Merkmale die Option Merkmal: VARKONDWählen Sie anschließend Anlegen. | Es werden zusätzliche Bildbereiche angezeigt. |  |
| 3 | Grunddaten eingeben | Geben Sie im Bereich Grunddaten folgende Daten ein:Beschreibung: VariantenkonditionsschlüsselStatus: FreigegebenDatentyp: ZeichenformatAnzahl Stellen: 26Groß-/Kleinschreibung beachten: markiertMehrere Werte: markiert |  |  |
| 4 | Beschreibung eingeben | Pflegen Sie optional zusätzliche Sprachen auf der Registerkarte Beschreibung eingeben. |  |  |
| 5 | Zusatzdaten erfassen | Navigieren Sie zur Registerkarte Zusätzliche Daten, und nehmen Sie die folgenden Einträge vor:Tabellenname: SDCOMFeldname: VKONDnicht eingabebereit: markiertKeine Anzeige: markiert |  |  |
| 6 | Merkmal sichern | Wählen Sie Sichern. | Das neue Merkmal wird angelegt. |  |

Merkmal SERVICE_CHANNEL (Servicekanal)

| Testschrittnummer | Bezeichnung des Testschritts | Anweisung | Erwartetes Ergebnis | Kommentare |
| --- | --- | --- | --- | --- |
| 1 | Anmelden | Melden Sie sich am SAP Fiori Launchpad als Produktkonfigurationsmodellierer an. | Die Startseite wird angezeigt. |  |
| 2 | App aufrufen | Öffnen Sie Merkmale verwalten.Pflegen Sie auf dem Bild Merkmale die Option Merkmal: SERVICE_CHANNELWählen Sie anschließend Anlegen. | Es werden zusätzliche Bildbereiche angezeigt. |  |
| 3 | Grunddaten eingeben | Geben Sie im Bereich Grunddaten folgende Daten ein:Beschreibung: ServicekanalStatus: FreigegebenDatentyp: ZeichenformatAnzahl Stellen: 20Mehrere Werte: markiertEintrag erforderlich: markiert |  |  |
| 4 | Beschreibung eingeben | Pflegen Sie optional zusätzliche Sprachen auf der Registerkarte Beschreibung eingeben. |  |  |
| 5 | Werte eingeben | Wechseln Sie auf die Registerkarte Werte, und geben Sie folgende Daten ein:Merkmalswert / Beschreibung: EMAIL/E-Mail-SupportMerkm. Wert / Beschreibung: TELEPHONE / Telefonsupport |  |  |
| 6 | Merkmal sichern | Wählen Sie Sichern. | Das neue Merkmal wird angelegt. |  |

Merkmal PREVENTIVE_MAINTENANCE (Planmäßige Instandhaltung)

| Testschrittnummer | Bezeichnung des Testschritts | Anweisung | Erwartetes Ergebnis | Kommentare |
| --- | --- | --- | --- | --- |
| 1 | Anmelden | Melden Sie sich am SAP Fiori Launchpad als Produktkonfigurationsmodellierer an. | Die Startseite wird angezeigt. |  |
| 2 | App aufrufen | Öffnen Sie Merkmale verwalten.Pflegen Sie auf dem Bild Merkmale die Option Merkmal: PREVENTIVE_MAINTENANCEWählen Sie anschließend Anlegen. | Es werden zusätzliche Bildbereiche angezeigt. |  |
| 3 | Grunddaten eingeben | Geben Sie im Bereich Grunddaten folgende Daten ein:Beschreibung: Vorbeugende InstandhaltungStatus: FreigegebenDatentyp: ZeichenformatAnzahl Stellen: 20Mehrere Werte: markiertEintrag erforderlich: markiert |  |  |
| 4 | Beschreibung eingeben | Pflegen Sie optional zusätzliche Sprachen auf der Registerkarte Beschreibung eingeben. |  |  |
| 5 | Werte eingeben | Wechseln Sie auf die Registerkarte Werte, und geben Sie folgende Daten ein:Merkmalswert / Beschreibung: YEARLY / JährlichMerkmalswert / Beschreibung: HALFYEARLY / HalbjährlichMerkmalswert / Beschreibung: QUARTERLY / vierteljährlich |  |  |
| 6 | Merkmal sichern | Wählen Sie Sichern. | Das neue Merkmal wird angelegt. |  |

#### Klasse anlegen

Zweck

In dieser Aktivität legen Sie eine Klasse an, der Sie die Merkmale aus dem vorherigen Kapitel zuordnen.

Vorgehensweise

| Testschrittnummer | Bezeichnung des Testschritts | Anweisung | Erwartetes Ergebnis | Kommentare |
| --- | --- | --- | --- | --- |
| 1 | Anmelden | Melden Sie sich am SAP Fiori Launchpad als Produktkonfigurationsmodellierer an. | Die Startseite wird angezeigt. |  |
| 2 | App aufrufen | Öffnen Sie Klassen verwalten.Geben Sie auf dem Bild Klasse folgende Daten ein:Klasse: SERVICE_CONTRACT_CKlassenart: 300 (Varianten)Wählen Sie anschließend Anlegen. | Es werden zusätzliche Bildbereiche angezeigt. |  |
| 3 | Grunddaten eingeben | Geben Sie im Bereich Grunddaten folgende Daten ein:Beschreibung: ServicevertragsklasseStatus: FreigegebenNicht prüfen: markiert |  |  |
| 4 | Merkmale eingeben | Wechseln Sie auf die Registerkarte Merkmal, und geben Sie folgende Daten ein:VARKONDSERVICE_CHANNELPREVENTIVE_MAINTENANCE | Die relevanten Merkmale werden der Klasse zugeordnet. |  |
| 5 | Klasse sichern | Wählen Sie Sichern. | Die neue Klasse wird angelegt. |  |

#### Konfigurierbares Serviceprodukt für Verträge anlegen

Zweck

In dieser Aktivität pflegen Sie ein konfigurierbares Serviceprodukt, das Sie in Serviceverträgen verwenden können.

|  |
| --- |
| Hinweis Für eine ordnungsgemäße Steuerberechnung sind spezifische Felder für Brasilien erforderlich. Prüfen Sie "Stammdaten für Brasilien anlegen" (JD0_BR) im Kapitel "BR-spezifische Felder für Stammdaten definieren" für Materialstammdaten. |

Vorgehensweise

| Testschrittnummer | Bezeichnung des Testschritts | Anweisung | Erwartetes Ergebnis | Kommentare |
| --- | --- | --- | --- | --- |
| 1 | Anmelden | Melden Sie sich im SAP Fiori Launchpad als Stammdatenexperte – Produktdaten an. | Die Startseite wird angezeigt. |  |
| 2 | App aufrufen | Wählen Sie unter der Kachel Produktstammdaten verwalten den Link Material anlegen. | Das Bild Material anlegen (Einstieg) wird angezeigt. |  |
| 3 | Material-ID und Art eingeben | Nehmen Sie auf dem Bild Material anlegen (Einstieg) die folgenden Einträge vor:Material: SRV_CONTR_CONFIGBranche: MWenn das Eingabefeld Branche ausgeblendet ist, ist keine Eingabe erforderlich.Materialart: ServiceproduktWählen Sie anschließend Weiter (Enter). |  |  |
| 4 | Sicht "Grunddaten" auswählen | Wählen Sie im Dialogfenster Sichtenauswahl die Sicht Grunddaten 1, und wählen Sie Weiter (Enter).Geben Sie im Dialogfenster Organisationsebenen die folgenden Daten ein:Werk: 1710Verkaufsorganisation: 1710Vertriebsweg: 10Hinweis Geben Sie für DE als Werk/Verkaufsorganisation/Vertriebsweg 1010/1010/10 ein. | Die Sicht Material SRV_CONTR anlegen wird angezeigt. |  |
| 5 | Grunddaten eingeben | Pflegen Sie in der Sicht Grunddaten 1 die folgenden Werte:Beschreib.: Konfigurierbarer ServicevertragBasismengeneinheit: LE (Leistungseinheit)Materialgruppe: P001 (Services)GenItemGroup: SCNP (Service vertragsprod.)Material ist konfigurierbar: AusgewähltNavigieren Sie zur Registerkarte Zusätzliche Daten, und bearbeiten Sie folgende Daten:Sprache: DEMaterialbeschreibung: Konfigurierbarer ServicevertragWählen Sie anschließend Sichern. | Das Produkt wird angelegt, und die Sicht Material anlegen (Einstieg) wird angezeigt. |  |
| 6 | Verkaufssichten auswählen | Pflegen Sie in der Sicht Material anlegen (Einstieg) das Material SRV_CONTR_CONFIG, und wählen Sie Weiter (Enter).Wählen Sie im Fenster Sichtenauswahl die folgende Sicht aus:Verkauf: VerkaufsorgDaten 1Verkauf: VerkaufsorgDaten 2Verkauf: All./WerksdatenWählen Sie anschließend Weiter (Enter). | Das Dialogfenster Organisationsebenen wird angezeigt. |  |
| 7 | Organisationsebenen wählen | Geben Sie im Dialogfenster Organisationsebenen die folgenden Werte ein:Werk: 1710 (Werk 1 USA)Verkaufsorg.: 1710 (Inländ. Verkaufsorganisation USA)Vertriebsweg: 10 (Direktverkauf)Hinweis Hinweis: Geben Sie für DE jeweils 1010/1010/10 ein.Wählen Sie anschließend Weiter (Enter). | Die Sicht Verkauf: VerkOrg 1 wird angezeigt. |  |
| 8 | Verkaufsorganisationsdaten eingeben (1) | Geben Sie in der Sicht Verkauf: VerkOrg 1 die folgenden Werte ein:Allgemeine Daten• Skonto: X <ausgewählt>Steuerdaten•Steuerklassifikation: 1 (volle Steuer)Wählen Sie anschließend Enter. | Die Sicht Verkauf: VerkOrg 2 wird angezeigt. |  |
| 9 | Verkaufsorganisationsdaten eingeben (2) | Geben Sie in der Sicht Verkauf: VerkOrg 2 die folgenden Daten ein:Positionstypengruppe: SCNP (Service vertragsprod.)Wählen Sie anschließend Enter. | Die Sicht Verkauf: Allg./Werk wird angezeigt. |  |
| 10 | Allgemeine Verkaufsdaten eingeben | Geben Sie in der Sicht Verkauf: Allg./Werk die folgenden Werte ein:Basismengeneinheit: LE (Leistungseinheit)Arbeitsdauer: 1 Std.Wählen Sie anschließend Sichern.Nur für Polen: Drücken Sie Enter, statt Sichern zu wählen. | Die Sicht Material anlegen (Einstieg) wird angezeigt. |  |
| Nur für Polen: | Verkaufsdaten eingeben | Geben Sie im Abschnitt International Trade: Export die folgenden Daten ein:Steuerungscode: z.B. 41.00.30.0Wählen Sie anschließend Sichern. | Die Sicht Material anlegen (Einstieg) wird angezeigt. |  |
| 11 | Sicht "Klassifizierung" auswählen | Pflegen Sie in der Sicht Material anlegen (Einstieg) das Material SRV_CONTR_CONFIG, und wählen Sie Weiter (Enter).Wählen Sie im Fenster Sichtenauswahl die folgende Sicht aus:KlassifizierungWählen Sie anschließend Weiter (Enter). | Die Sicht Klassifizierung wird angezeigt. |  |
| 12 | Klassifizierung eingeben | Markieren Sie im Dialogfenster Klassenartden Eintrag Varianten (300), und wählen Sie Kopieren.Geben Sie in der Sicht Klassifizierung folgende Daten ein:Klasse: SERVICE_CONTRACT_CWählen Sie Enter, um die Merkmale anzuzeigen, die der Klasse zugeordnet sind.Öffnen Sie im Bildbereich Werte für Klasse SERVICE_CONTRACT_C für jedes Merkmal die Wertehilfe, und wählen Sie alle verfügbaren Werte aus.Wählen Sie anschließend Sichern. | Die Sicht Material anlegen (Einstieg) wird angezeigt. |  |

#### Konfigurationsprofil anlegen

Zweck

In dieser Aktivität legen Sie ein Konfigurationsprofil im Variantenkonfigurationsmodellierer an.

Vorgehensweise

| Testschrittnummer | Bezeichnung des Testschritts | Anweisung | Erwartetes Ergebnis | Kommentare |
| --- | --- | --- | --- | --- |
| 1 | Anmelden | Melden Sie sich am SAP Fiori Launchpad als Produktkonfigurationsmodellierer an. | Die Startseite wird angezeigt. |  |
| 2 | App aufrufen | Öffnen Sie VC-Modellierungsumgebung.Geben Sie auf dem Bild Einstieg in Modellierungsumgebung der Variantenkonfiguration die folgenden Daten ein:Material: SRV_CONTR_CONFIGKlassenart: 300 (Varianten)Wählen Sie anschließend Modell eingeben. | Das Bild Konfiguration für SRV_CONTR_CONFIG wird angezeigt. |  |
| 3 | Konfigurationsprofil anlegen | Klicken Sie in der Spalte Objekt mit der rechten Maustaste auf SRV_CONTR_CONFIG, und wählen Sie Konfigurationsprofil anlegen.Geben Sie im Dialogfenster Konfigurationsprofil anlegen folgende Daten ein:Konfigurationsprofil: SRV_CONTR_CONFOhne Änderungsnummer: markiertWählen Sie anschließend Weiter (Enter).Doppelklicken Sie im Bereich Objekt auf das Material SRV_CONTR_CONFIG.Öffnen Sie die Registerkarte Variantenpreisfindung, wählen Sie Ändern und anschließend Liste aufklappen.Pflegen Sie alle Merkmale, die Ihrem konfigurierbaren Produkt zugeordnet sind, mit Ausnahme des Merkmals VARKOND. Stellen Sie außerdem sicher, dass Sie für alle eine Variantenkondition und eine Beschreibung pflegen. Die Variantenkondition wird in der Preiskonditionspflege verwendet.Pflegen Sie z.B. für Merkmal/Merkmalswert/ Variantenkondition/ Variantenkonditionsbeschreibung: folgende Werte:SERVICE_CHANNEL / EMAIL / EMAIL / E-Mail-SupportSERVICE_CHANNEL / TELEPHONE / TELEPHONE / TelefonsupportPREVENTIVE_MAINTENANCE / YEARLY / YEARLY / JährlichPREVENTIVE_MAINTENANCE / HALFYEARLY / HALFYEARLY / HalbjährlichPREVENTIVE_MAINTENANCE / QUARTERLY / QUARTERLY / VierteljährlichWählen Sie anschließend Sichern. | Das Bild Konfiguration für SRV_CONTR_CONFIG wird angezeigt. |  |

#### Preise bestimmen

Zweck

In dieser Aktivität pflegen Sie einen Standardpreis-Konditionssatz für das konfigurierbare Serviceprodukt sowie Variantenpreissätze für die konfigurierbaren Varianten.

Vorgehensweise

Konditionsart: PSI1 (Preis für Servicevertragsposition)

| Testschrittnummer | Bezeichnung des Testschritts | Anweisung | Erwartetes Ergebnis | Kommentare |
| --- | --- | --- | --- | --- |
| 1 | Anmelden | Melden Sie sich am SAP Fiori Launchpad als Preisfindungssachbearbeiter an. | Die Startseite wird angezeigt. |  |
| 2 | App aufrufen | Öffnen Sie Materialpreise festlegen. | Die Sicht Konditionssätze ändern wird angezeigt. |  |
| 3 | Konditionsart eingeben | Pflegen Sie in der Sicht Konditionssätze ändern die Konditionsart: PSI1 (Preis f. SrvVertr), und wählen Sie Enter. | Die Sicht Schlüsselkombination wird angezeigt. |  |
| 4 | Schlüsselkombination auswählen | Wählen Sie in der Sicht Schlüsselkombination die Option Material.Wählen Sie anschließend Enter. | Die Sicht Preis ändern (PSI1): Auswahl wird angezeigt. |  |
| 5 | Auswählen | Geben Sie in der Sicht Preis ändern (PSI1): Auswahl die folgenden Informationen ein:Verkaufsorg.: 1710 (Inländ. Verkaufsorganisation USA)Vertriebsweg: 10 (Direktverkauf)Material:SRV_CONTRACT (Servicevertragsprodukt)Gültig am: <Datum>, z.B. das aktuelle DatumWählen Sie anschließend Ausführen. | Die Sicht Preiskondition ändern (PPSI): Übersicht wird angezeigt. |  |
| 6 | Preiskondition eingeben | Geben Sie in der Sicht Preiskondition ändern (PSI1): Übersicht die folgenden Daten ein:Material: SRV_CONTR_CONFIG (Konfigurierbarer Servicevertrag)Betrag: z.B. 200,00Einheit: z.B. USDGültig ab: <Datum>, z.B. das aktuelle DatumWählen Sie Enter.Wählen Sie anschließend Sichern. | Ein Standardpreis für das Serviceprodukt SRV_CONTR_CONFIG wurde gepflegt. |  |

Konditionsart: VASE (Variantenpreis)

| Testschrittnummer | Bezeichnung des Testschritts | Anweisung | Erwartetes Ergebnis | Kommentare |
| --- | --- | --- | --- | --- |
| 1 | Anmelden | Melden Sie sich am SAP Fiori Launchpad als Preisfindungssachbearbeiter an. | Die Startseite wird angezeigt. |  |
| 2 | App aufrufen | Öffnen Sie Materialpreise festlegen. | Die Sicht Konditionssätze ändern wird angezeigt. |  |
| 3 | Konditionsart eingeben | Pflegen Sie in der Sicht Konditionssätze ändern die Konditionsart: VASE (Variantenpreis), und wählen Sie Enter. | Die Sicht Variantenpreis ändern wird angezeigt. |  |
| 4 | Verkaufsdaten eingeben | Geben Sie im Bild Variantenpreis ändern (VASE): Auswahl die folgenden Informationen ein:Verkaufsorg.: 1710 (Inländ. Verkaufsorganisation USA)Vertriebsweg: 10 (Direktverkauf)Material: SRV_CONTR_CONFIG (Konfigurierbarer Servicevertrag)Gültig am: <Datum>, z.B. das aktuelle DatumWählen Sie anschließend Ausführen. | Die Sicht Variantenpreiskondition ändern (VASE): Übersicht wird angezeigt. |  |
| 5 | Variantenkonditionen eingeben | Geben Sie in der Sicht Variantenpreiskondition ändern (VASE): Übersicht Preise für alle Variantenkonditionen ein, die Sie im vorherigen Kapitel gepflegt haben, z.B.:Variante / Betrag / Einheit:EMAIL / 30 USDTELEPHONE/ 50 USDYEARLY / 250 USDHALFYEARLY / 135 USDQUARTERLY / 90 USDWählen Sie Enter, und überprüfen Sie Ihre Einträge.Wählen Sie anschließend Sichern. | Die Variantenpreiskonditionen wurden gepflegt. |  |

### Konfigurierbares Serviceprodukt für Serviceaufträge anlegen

#### Merkmale anlegen

Zweck

In dieser Aktivität legen Sie Merkmale an, die im konfigurierbaren Serviceprodukt zur Auswahl stehen sollen und für die Sie individuelle Variantenpreise pflegen können.

Vorgehensweise

Merkmal VARKOND (Variantenkonditionsschlüssel)

| Testschrittnummer | Bezeichnung des Testschritts | Anweisung | Erwartetes Ergebnis | Kommentare |
| --- | --- | --- | --- | --- |
| 1 | Anmelden | Melden Sie sich am SAP Fiori Launchpad als Produktkonfigurationsmodellierer an. | Die Startseite wird angezeigt. |  |
| 2 | App aufrufen | Öffnen Sie Merkmale verwalten.Geben Sie im Bild Merkmale im Feld Merkmal den Wert VARKOND ein.Wählen Sie anschließend Anlegen. | Es werden zusätzliche Bildbereiche angezeigt. |  |
| 3 | Grunddaten eingeben | Geben Sie im Bereich Grunddaten folgende Daten ein:Beschreibung: VariantenkonditionsschlüsselStatus: FreigegebenTerminart: ZeichenformatAnzahl Stellen: 26Groß-/Kleinschreibung beachten: markiertMehrere Werte: markiert |  |  |
| 4 | Beschreibung eingeben | Sie können optional zusätzliche Sprachen auf der Registerkarte Beschreibungen pflegen eingeben. |  |  |
| 5 | Zusatzdaten erfassen | Navigieren Sie zur Registerkarte Zusätzliche Daten, und geben Sie die folgenden Daten ein:Tabellenname: SDCOMFeldname: VKONDnicht eingabebereit: markiertKeine Anzeige: markiert |  |  |
| 6 | Merkmal sichern | Wählen Sie Sichern. | Der neue Variantenkonditionsschlüssel wird angelegt. |  |

Merkmal CAR_WASH_TYPE (Art der Autowaschanlage)

| Testschrittnummer | Bezeichnung des Testschritts | Anweisung | Erwartetes Ergebnis | Kommentare |
| --- | --- | --- | --- | --- |
| 1 | Anmelden | Melden Sie sich am SAP Fiori Launchpad als Produktkonfigurationsmodellierer an. | Die Startseite wird angezeigt. |  |
| 2 | App aufrufen | Öffnen Sie Merkmale verwalten.Geben Sie im Bild Merkmale im Feld Merkmal den Wert CAR_WASH_TYPE ein.Wählen Sie anschließend Anlegen. | Es werden zusätzliche Bildbereiche angezeigt. |  |
| 3 | Grunddaten eingeben | Geben Sie im Bereich Grunddaten folgende Daten ein:Beschreibung: Art der AutowaschanlageStatus: FreigegebenTerminart: ZeichenformatAnzahl Stellen: 20Einzelwerte: markiertEintrag erforderlich: markiert |  |  |
| 4 | Beschreibung eingeben | Sie können optional zusätzliche Sprachen auf der Registerkarte Beschreibungen pflegen eingeben. |  |  |
| 5 | Werte eingeben | Wechseln Sie auf die Registerkarte Werte, und geben Sie folgende Daten ein:Merkmalswert / Beschreibung: BASIC/Basis-WäscheMerkmalswert / Beschreibung: STANDARD/Standard-WäscheMerkmalswert / Beschreibung: PREMIUM/Premium-Wäsche |  |  |
| 6 | Merkmal sichern | Wählen Sie Sichern. | Das neue Merkmal wird angelegt. |  |

Merkmal CAR_SIZE (Fahrzeuggröße)

| Testschrittnummer | Bezeichnung des Testschritts | Anweisung | Erwartetes Ergebnis | Kommentare |
| --- | --- | --- | --- | --- |
| 1 | Anmelden | Melden Sie sich am SAP Fiori Launchpad als Produktkonfigurationsmodellierer an. | Die Startseite wird angezeigt. |  |
| 2 | App aufrufen | Öffnen Sie Merkmale verwalten.Geben Sie im Bild Merkmale im Feld Merkmal den Wert CAR_SIZE ein.Wählen Sie anschließend Anlegen. | Es werden zusätzliche Bildbereiche angezeigt. |  |
| 3 | Grunddaten eingeben | Geben Sie im Bereich Grunddaten folgende Daten ein:Beschreibung: FahrzeuggrößeStatus : FreigegebenTerminart: ZeichenformatAnzahl Stellen: 20Einzelwerte: markiertEintrag erforderlich: markiert |  |  |
| 4 | Beschreibung eingeben | Sie können optional zusätzliche Sprachen auf der Registerkarte Beschreibungen pflegen eingeben. |  |  |
| 5 | Werte eingeben | Wechseln Sie auf die Registerkarte Werte, und geben Sie folgende Daten ein:Merkmalswert / Beschreibung: S / KleinMerkmalswert / Beschreibung: M / MittelMerkmalswert / Beschreibung: L / Groß |  |  |
| 6 | Merkmal sichern | Wählen Sie Sichern. | Das neue Merkmal wird angelegt. |  |

Merkmal EXTRA_POLISH (Zusätzliche Politur)

| Testschrittnummer | Bezeichnung des Testschritts | Anweisung | Erwartetes Ergebnis | Kommentare |
| --- | --- | --- | --- | --- |
| 1 | Anmelden | Melden Sie sich am SAP Fiori Launchpad als Produktkonfigurationsmodellierer an. | Die Startseite wird angezeigt. |  |
| 2 | App aufrufen | Öffnen Sie Merkmale verwalten.Geben Sie im Bild Merkmale im Feld Merkmal den Wert EXTRA_POLISH ein.Wählen Sie anschließend Anlegen. | Es werden zusätzliche Bildbereiche angezeigt. |  |
| 3 | Grunddaten eingeben | Geben Sie im Bereich Grunddaten folgende Daten ein:Beschreibung: Zusätzliche PoliturStatus : FreigegebenTerminart: ZeichenformatAnzahl Stellen: 10Einzelwert: markiertEintrag erforderlich: markiert |  |  |
| 4 | Beschreibung eingeben | Sie können optional zusätzliche Sprachen auf der Registerkarte Beschreibungen pflegen eingeben. |  |  |
| 5 | Werte eingeben | Wechseln Sie auf die Registerkarte Werte, und geben Sie folgende Daten ein:Merkmalswert / Beschreibung: YES / JaMerkmalswert / Beschreibung: NO / Nein |  |  |
| 6 | Merkmal sichern | Wählen Sie Sichern. | Das neue Merkmal wird angelegt. |  |

#### Klasse anlegen

Zweck

In dieser Aktivität legen Sie eine Klasse an, der Sie die Merkmale aus dem vorherigen Kapitel zuordnen.

Vorgehensweise

| Testschrittnummer | Bezeichnung des Testschritts | Anweisung | Erwartetes Ergebnis | Kommentare |
| --- | --- | --- | --- | --- |
| 1 | Anmelden | Melden Sie sich am SAP Fiori Launchpad als Produktkonfigurationsmodellierer an. | Die Startseite wird angezeigt. |  |
| 2 | App aufrufen | Öffnen Sie Klassen verwalten.Geben Sie auf dem Bild Klasse folgende Daten ein:Klasse: CAR_WASHKlassenart: 300 (Varianten)Wählen Sie anschließend Anlegen. | Es werden zusätzliche Bildbereiche angezeigt. |  |
| 3 | Klassenname eingeben | Geben Sie auf dem Bild Klasse folgende Daten ein:Klasse: CAR_WASHKlassenart: 300 (Varianten)Wählen Sie anschließend Anlegen. |  |  |
| 4 | Grunddaten eingeben | Geben Sie im Bereich Grunddaten folgende Daten ein:Beschreibung: AutowaschanlageStatus: FreigegebenNicht prüfen: markiert |  |  |
| 5 | Merkmale eingeben | Wechseln Sie auf die Registerkarte Merkmal, und geben Sie folgende Daten ein:VARKONDCAR_WASH_TYPECAR_SIZEEXTRA_POLISH | Die relevanten Merkmale werden der Klasse zugeordnet. |  |
| 6 | Klasse sichern | Wählen Sie Sichern. | Die neue Klasse wird angelegt. |  |

#### Konfigurierbares Serviceprodukt für Serviceaufträge anlegen

Zweck

In dieser Aktivität pflegen Sie ein konfigurierbares Serviceprodukt, das Sie in Serviceaufträgen verwenden können.

Vorgehensweise

| Testschrittnummer | Bezeichnung des Testschritts | Anweisung | Erwartetes Ergebnis | Kommentare |
| --- | --- | --- | --- | --- |
| 1 | Anmelden | Melden Sie sich am SAP Fiori Launchpad an als Stammdatenexperte – Produktdaten | Die Startseite wird angezeigt. |  |
| 2 | App aufrufen | Wählen Sie die App Material anlegen. | Das Bild Material anlegen (Einstieg) wird angezeigt. |  |
| 3 | Material-ID und Art eingeben | Geben Sie auf dem Bild Material anlegen (Einstieg) folgende Daten ein:Material: CAR-WASH_CONFWenn das Eingabefeld Branche ausgeblendet ist, ist keine Eingabe erforderlich.Materialart: SERV ServiceproduktWählen Sie anschließend Weiter (Enter). |  |  |
| 4 | Sicht "Grunddaten" auswählen | Geben Sie im Dialogfenster Organisationsebenen die folgenden Daten ein:Werk: 1710 (Werk 1 USA)Verkaufsorg.: 1710 (Inländ. Verkaufsorganisation USA)Vertriebsweg: 10 (Direktverkauf)Hinweis: Geben Sie für DE jeweils 1010/1010/10 ein.Wählen Sie anschließend Weiter (Enter). | Die Sicht Material anlegen CAR-WASH _CONF wird angezeigt. |  |
| 5 | Grunddaten eingeben | Geben Sie auf der Registerkarte Grunddaten 1 die folgenden Daten ein:Beschreib.: Waschanlage konfigurierbarBasismengeneinheit: LE (Leistungseinheit)Warengruppe: P001 (Services)Allg. PosTypGrp: SRVP (Serviceprodukt)Material ist konfigurierbar: AusgewähltNavigieren Sie zur Registerkarte Zusätzliche Daten, und bearbeiten Sie folgende Daten:Sprache: DEMaterialbeschreibung: Konfigurierbare AutowäscheWählen Sie anschließend Sichern. | Das Produkt wird angelegt, und die Sicht Material anlegen (Einstieg) wird angezeigt. |  |
| 6 | Verkaufssichten auswählen | Geben Sie in der Sicht Material anlegen (Einstieg) im Feld Material den Wert CAR-WASH_CONF ein, und wählen Sie Weiter (Enter).Wählen Sie im Dialogfenster Sichtenauswahl die folgenden Sichten aus:Vertrieb: VerkaufsorgDaten 1Vertrieb: VerkaufsorgDaten 2Vertrieb: All./WerksdatenWählen Sie anschließend Weiter (Enter). | Das Dialogfenster Organisationsebenen wird angezeigt. |  |
| 7 | Organisationsebenen wählen | Geben Sie im Dialogfenster Organisationsebenen die folgenden Daten ein:Werk: 1710 (Werk 1 USA)Verkaufsorg.: 1710 (Inländ. Verkaufsorganisation USA)Vertriebsweg: 10 (Direktverkauf)Hinweis: Geben Sie für DE jeweils 1010/1010/10 ein.Wählen Sie anschließend Weiter (Enter). | Die Sicht Vertrieb: VerkOrg 1 wird angezeigt. |  |
| 8 | Verkaufsorganisationsdaten eingeben (1) | Geben Sie in der Sicht Verkauf: VerkOrg 1 die folgenden Daten ein:Allgemeine Daten• Skonto: X <ausgewählt>Steuerdaten•Steuerklassifikation: 1 (volle Steuer)Wählen Sie anschließend Enter. | Die Sicht Verkauf: VerkOrg 2 wird angezeigt. |  |
| 9 | Verkaufsorganisationsdaten eingeben (2) | Geben Sie in der Sicht Verkauf: VerkOrg 2 die folgenden Daten ein:Positionstypengruppe: SRVP (Serviceprodukt)Wählen Sie anschließend Enter. | Die Sicht Verkauf: Allg./Werk wird angezeigt. |  |
| 10 | Allgemeine Verkaufsdaten eingeben | Geben Sie in der Sicht Verkauf: Allg./Werk die folgenden Daten ein:Basismengeneinheit: LE (Leistungseinheit)Arbeitsdauer: 1 Std.Wählen Sie anschließend Sichern.Nur für Polen: Drücken Sie Enter, statt Sichern zu wählen. | Die Sicht Material anlegen (Einstieg) wird angezeigt. |  |
| Nur für Polen: | Verkaufsdaten eingeben | Geben Sie auf der Registerkarte International Trade: Export im Bereich Außenhandelsdaten die folgenden Daten ein:Steuerungscode: z.B. 41.00,30,0Wählen Sie anschließend Sichern. |  |  |
| 11 | Sicht "Klassifizierung" auswählen | Geben Sie in der Sicht Material anlegen (Einstieg) im Feld Material den Wert CAR_WASH_CONF ein, und wählen Sie Weiter (Enter).Wählen Sie im Dialogfenster Sichtenauswahl die folgende Sicht aus:KlassifizierungWählen Sie anschließend Weiter (Enter). | Die Sicht Klassifizierung wird angezeigt. |  |
| 12 | Klassifizierung eingeben | Markieren Sie im Dialogfenster Klassenart den Eintrag Varianten (300), und wählen Sie Kopieren.Geben Sie in der Sicht Klassifizierung die folgenden Daten ein:Klasse: CAR_WASHWählen Sie Enter, um die Merkmale anzuzeigen, die der Klasse zugeordnet sind.Öffnen Sie im Bildbereich Werte für Klasse CAR_WASH für jedes Merkmal die Wertehilfe, und wählen Sie alle verfügbaren Werte aus.Wählen Sie anschließend Sichern. | Die Merkmale werden dem Material zugeordnet. |  |

#### Konfigurationsprofil anlegen

Zweck

In dieser Aktivität legen Sie ein Konfigurationsprofil im Variantenkonfigurationsmodellierer an.

Vorgehensweise

| Testschrittnummer | Bezeichnung des Testschritts | Anweisung | Erwartetes Ergebnis | Kommentare |
| --- | --- | --- | --- | --- |
| 1 | Anmelden | Melden Sie sich am SAP Fiori Launchpad als Produktkonfigurationsmodellierer an. | Die Startseite wird angezeigt. |  |
| 2 | App aufrufen | Öffnen Sie VC-Modellierungsumgebung.Geben Sie auf dem Bild Einstieg in Modellierungsumgebung der Variantenkonfiguration die folgenden Daten ein:Material: CAR-WASH_CONFKlassenart: 300 (Varianten)Wählen Sie anschließend Modell eingeben. | Das Bild Konfiguration für CAR_WASH_CONF wird angezeigt. |  |
| 3 | Konfigurationsprofil anlegen | Klicken Sie in der Spalte Objekt mit der rechten Maustaste auf CAR_WASH_CONF, und wählen Sie Konfigurationsprofil anlegen.Geben Sie im Dialogfenster Konfigurationsprofil anlegen folgende Daten ein:Konfigurationsprofil: CAR-WASH_CONFOhne Änderungsnummer: markiertWählen Sie anschließend Weiter (Enter).Doppelklicken Sie in der Spalte Objekt auf den Eintrag CAR-WASH_CONF. Öffnen Sie die Registerkarte Variantenpreisfindung, und wählen Sie Ändern. Wählen Sie dann Liste expandieren.Geben Sie alle Merkmale ein, die Ihrem konfigurierbaren Produkt zugeordnet sind, mit Ausnahme des Merkmals VARKOND. Stellen Sie außerdem sicher, dass Sie für alle eine Variantenkondition und eine Beschreibung eingeben. Die Variantenkondition wird in der Preiskonditionspflege verwendet.Pflegen Sie z.B. für Merkmal/Merkmalswert/ Variantenkondition/Variantenkonditionsbeschreibung: Folgendes:CAR_WASH_TYPE/BASIC/C_W_T_B/BasisCAR_WASH_TYPE/STANDARD/C_W_T_S/StandardCAR_WASH_TYPE/PREMIUM/C_W_T_P/PremiumCAR_SIZE/S/C_S_S/KleinCAR_SIZE/M/C_S_M/MittelCAR_SIZE/L/C_S_L/GroßEXTRA_POLISH/YES/E_P_Y/JaEXTRA_POLISH/NO/E_P_N/NeinWählen Sie anschließend Sichern. | Variantenkonditionen werden für alle Merkmale angelegt. |  |

#### Preise bestimmen

Zweck

In dieser Aktivität pflegen Sie einen Standardpreis-Konditionssatz für das konfigurierbare Serviceprodukt sowie Variantenpreissätze für die konfigurierbaren Varianten.

Vorgehensweise

Konditionsart: PPR0 (Preis)

| Testschrittnummer | Bezeichnung des Testschritts | Anweisung | Erwartetes Ergebnis | Kommentare |
| --- | --- | --- | --- | --- |
| 1 | Anmelden | Melden Sie sich am SAP Fiori Launchpad als Preisfindungssachbearbeiter an. | Die Startseite wird angezeigt. |  |
| 2 | App aufrufen | Öffnen Sie Materialpreise festlegen. | Die Sicht Konditionssätze ändern wird angezeigt. |  |
| 3 | Konditionsart eingeben | Geben Sie in der Sicht Konditionssätze ändern im Feld Konditionsart den Wert PPR0 (Preis) ein, und wählen Sie Enter. | Die Sicht Schlüsselkombination wird angezeigt. |  |
| 4 | Schlüsselkombination auswählen | Wählen Sie in der Sicht Schlüsselkombination die Option Material.Wählen Sie anschließend Enter. | Die Sicht Preis ändern (PPR0): Auswahl wird angezeigt. |  |
| 5 | Auswählen | Geben Sie im Bild Preis ändern (PPR0): Auswahl die folgenden Daten ein:Verkaufsorg.: 1710 (Inländ. Verkaufsorganisation USA)Vertriebsweg: 10 (Direktverkauf)Material: CAR-WASH_CONF (Waschanlage konfigurierbar)Gültig am: <Datum>, z.B. das aktuelle DatumWählen Sie anschließend Ausführen. | Die Sicht Preiskondition ändern (PPR0): Übersicht wird angezeigt. |  |
| 6 | Preiskondition eingeben | Geben Sie in der Sicht Preiskondition ändern (PPR0): Übersicht die folgenden Daten ein:Material: CAR-WASH_CONF (Waschanlage konfigurierbar)Betrag: z.B. 10,00Einheit: z.B. USDGültig ab: <Datum>, z.B. das aktuelle DatumWählen Sie Enter.Wählen Sie anschließend Sichern. | Ein Standardpreis für das Serviceprodukt wird angelegt. |  |

Konditionsart: PVA0 (Variantenpreis)

| Testschrittnummer | Bezeichnung des Testschritts | Anweisung | Erwartetes Ergebnis | Kommentare |
| --- | --- | --- | --- | --- |
| 1 | Anmelden | Melden Sie sich am SAP Fiori Launchpad als Preisfindungssachbearbeiter an. | Die Startseite wird angezeigt. |  |
| 2 | App aufrufen | Öffnen Sie Materialpreise festlegen. | Die Sicht Konditionssätze ändern wird angezeigt. |  |
| 3 | Konditionsart eingeben | Pflegen Sie in der Sicht Konditionssätze ändern die Konditionsart: PVA0 (Variantenpreis), und wählen Sie Enter. | Die Sicht Variantenpreis ändern wird angezeigt. |  |
| 4 | Verkaufsdaten eingeben | Geben Sie im Bild Variantenpreis ändern (PVA0): Auswahl die folgenden Informationen ein:Verkaufsorg.: 1710 (Inländ. Verkaufsorganisation USA)Vertriebsweg: 10 (Direktverkauf)Material: CAR-WASH_CONF (Konfigurierbarer Servicevertrag)Gültig am: <Datum>, z.B. das aktuelle DatumWählen Sie anschließend Ausführen. | Die Sicht Variantenpreiskondition ändern (PVA0): Übersicht wird angezeigt. |  |
| 5 | Variantenkonditionen eingeben | Geben Sie in der Sicht Variantenpreiskondition anlegen (PVA0): Übersicht Preise für alle Variantenkonditionen ein, die Sie im vorherigen Kapitel angelegt haben, z.B.:Variante / Betrag / Einheit:C_W_T_B / 5 USDC_W_T_S / 8 USDC_W_T_P / 12 USDC_S_S / 2 USDC_S_M / 4 USDC_S_L / 10 USDWählen Sie Enter, und überprüfen Sie Ihre Einträge.Wählen Sie anschließend Sichern. | Die Variantenpreiskonditionen werden angelegt. |  |

PVA1 (Variantenpreis %)

| Testschrittnummer | Bezeichnung des Testschritts | Anweisung | Erwartetes Ergebnis | Kommentare |
| --- | --- | --- | --- | --- |
| 1 | Anmelden | Melden Sie sich am SAP Fiori Launchpad als Preisfindungssachbearbeiter an. | Die Startseite wird angezeigt. |  |
| 2 | App aufrufen | Öffnen Sie Materialpreise festlegen. | Die Sicht Konditionssätze ändern wird angezeigt. |  |
| 3 | Konditionsart eingeben | Geben Sie in der Sicht Konditionssätze ändern im Feld Konditionsart den Wert PVA1 Variantenpreis (%) ein, und wählen Sie Enter. | Die Sicht Variantenpreis ändern (% PVA1) wird angezeigt. |  |
| 4 | Verkaufsdaten eingeben | Geben Sie in der Sicht Variantenpreis ändern (PVA1): Auswahl die folgenden Daten ein:Verkaufsorg.: 1710 (Inländ. Verkaufsorganisation USA)Vertriebsweg: 10 (Direktverkauf)Material: CAR-WASH_CONFGültig am: <Datum>, z.B. das aktuelle DatumWählen Sie anschließend Ausführen. | Die Sicht Variantenpreis (%) (PVA1) ändern:: Übersicht wird angezeigt. |  |
| 5 | Variantenkonditionen eingeben | Geben Sie in der Sicht Variantenpreis (%) (PVA1) ändern: Schnellerfassung Konditionssätze für alle relevanten Variantenkonditionen ein, z.B.Variante / Betrag / Einheit:E_P_Y / 20%E_P_N / -10%Wählen Sie Enter, und überprüfen Sie Ihre Einträge.Wählen Sie anschließend Sichern. | Die Variantenpreiskonditionen werden angelegt. |  |

### Materialvariante für ein Serviceprodukt anlegen

Zweck

In dieser Aktivität legen Sie eine Materialvariante mit einer vordefinierten Konfiguration an, die in einem Serviceauftrag verwendet werden kann. Der Stammsatz der Variante ist mit einem konfigurierbaren Produkt verknüpft und verwendet dessen Merkmale.

Vorgehensweise

| Testschrittnummer | Bezeichnung des Testschritts | Anweisung | Erwartetes Ergebnis | Kommentare |
| --- | --- | --- | --- | --- |
| 1 | Anmelden | Melden Sie sich am SAP Fiori Launchpad an als Stammdatenexperte – Produktdaten | Die Startseite wird angezeigt. |  |
| 2 | App aufrufen | Wählen Sie unter der Kachel Produktstammdaten verwalten den Link Material anlegen. | Das Bild Material anlegen (Einstieg) wird angezeigt. |  |
| 3 | Material-ID und Art eingeben | Geben Sie auf dem Bild Material anlegen (Einstieg) folgende Daten ein:Material: CAR-WASH-VARBranche: MaschinenbauWenn das Eingabefeld Branche ausgeblendet ist, ist keine Eingabe erforderlich.Materialart: SERV ServiceproduktWählen Sie anschließend Weiter (Enter).Wählen Sie im Dialogfenster Sichtenauswahl die Option Grunddaten 1.Wählen Sie Orgebenen. |  |  |
| 4 | Organisationsebenen auswählen | Geben Sie im Dialogfenster Organisationsebenen die folgenden Daten ein:Werk: 1710 (Werk 1 USA)Verkaufsorganisation: 1710 (Inländ. Verkaufsorganisation USA)Vertriebsweg: 10 (Direktverkauf)Hinweis Geben Sie für DE jeweils 1010/1010/10 ein.Wählen Sie anschließend Weiter (Enter). | Die Sicht Material CAR-WASH-VAR anlegen wird angezeigt. |  |
| 5 | Grunddaten eingeben | Geben Sie auf der Registerkarte Grunddaten 1 die folgenden Daten ein:Beschreib.: Variante für WaschanlageBasismengeneinheit: LE (Leistungseinheit)Warengruppe: P001 (Services)GenItemGroup: SRVP (Serviceprodukt)Material ist konfigurierbar: entmarkiertWerksübergreifendes CM:CAR-WASH_CONFWählen Sie Variante konfigurieren.In der Sicht VariantenkonfigurationWählen Sie die folgenden Merkmale aus:Fahrzeuggröße: KleinZusätzliche Politur: JaArt der Autowaschanlage: Standard-WäscheWählen Sie Fertig.Wählen Sie anschließend Sichern. | Das Produkt wird angelegt, und die Sicht Material anlegen (Einstieg) wird angezeigt. |  |
| 6 | Verkaufssichten auswählen | Geben Sie in der Sicht Material anlegen (Einstieg) im Feld Material den Wert CAR-WASH_VAR ein, und wählen Sie Weiter (Enter).Wählen Sie im Dialogfenster Sichtenauswahl die folgenden Sichten aus:Verkauf: VerkaufsorgDaten 1Verkauf: VerkaufsorgDaten 2Verkauf: All./WerksdatenWählen Sie anschließend Weiter (Enter). | Das Dialogfenster Organisationsebenen wird angezeigt. |  |
| 7 | Organisationsebenen wählen | Geben Sie im Dialogfenster Organisationsebenen die folgenden Daten ein:Werk: 1710 (Werk 1 USA)Verkaufsorg.: 1710 (Inländ. Verkaufsorganisation USA)Vertriebsweg: 10 (Direktverkauf)Hinweis Geben Sie für DE jeweils 1010/1010/10 ein.Wählen Sie anschließend Weiter (Enter). | Die Sicht Verkauf: VerkOrg 1 wird angezeigt. |  |
| 8 | Verkaufsorganisationsdaten eingeben (1) | Geben Sie in der Sicht Verkauf: VerkOrg 1 die folgenden Daten ein:Allgemeine Daten• Skonto: X <ausgewählt>• Steuerdaten• Steuerklassifikation: 1 (volle Steuer)Wählen Sie anschließend Enter. | Die Sicht Verkauf: VerkOrg 2 wird angezeigt. |  |
| 9 | Verkaufsorganisationsdaten eingeben (2) | Geben Sie in der Sicht Verkauf: VerkOrg 2 die folgenden Daten ein:Positionstypengruppe: SRVP (Serviceprodukt)Wählen Sie anschließend Enter. | Die Sicht Verkauf: Allg./Werk wird angezeigt. |  |
| 10 | Allgemeine Verkaufsdaten eingeben | Geben Sie in der Sicht Verkauf: Allg./Werk die folgenden Daten ein:Basismengeneinheit: LE (Leistungseinheit)Arbeitsdauer: 1 Std.Wählen Sie anschließend Sichern. | Die Sicht Material anlegen (Einstieg) wird angezeigt. |  |

#### Preise für Materialvariante festlegen

Zweck

In dieser Aktivität pflegen Sie einen Standardpreiskonditionssatz für die Variante.

Vorgehensweise

Konditionsart: PPR0 (Preis)

| Testschrittnummer | Bezeichnung des Testschritts | Anweisung | Erwartetes Ergebnis | Kommentare |
| --- | --- | --- | --- | --- |
| 1 | Anmelden | Melden Sie sich am SAP Fiori Launchpad als Preisfindungssachbearbeiter an. | Die Startseite wird angezeigt. |  |
| 2 | App aufrufen | Öffnen Sie Materialpreise festlegen. | Die Sicht Konditionssätze ändern wird angezeigt. |  |
| 3 | Konditionsart eingeben | Geben Sie in der Sicht Konditionssätze ändern im Feld Konditionsart den Wert PPR0 (Preis) ein, und wählen Sie Enter. | Die Sicht Schlüsselkombination wird angezeigt. |  |
| 4 | Schlüsselkombination auswählen | Wählen Sie in der Sicht Schlüsselkombination die Option Material mit Freigabestatus.Wählen Sie anschließend Enter. | Die Sicht Preis ändern (PPR0): Auswahl wird angezeigt. |  |
| 5 | Auswahl | Geben Sie im Bild Preis ändern (PPR0): Auswahl die folgenden Daten ein:Verkaufsorg.: 1710 (Inländ. Verkaufsorganisation USA)Vertriebsweg: 10 (Direktverkauf)Material: CAR-WASH-VAR (Variante der Waschanlage)Gültig am: <Datum>, z.B. das aktuelle DatumWählen Sie anschließend Ausführen. | Die Sicht Preiskondition ändern (PPR0): Übersicht wird angezeigt. |  |
| 6 | Preiskondition eingeben | Geben Sie in der Sicht Preiskondition ändern (PPR0): Übersicht die folgenden Daten ein:Material: CAR-WASH-VAR (Variante der Waschanlage)Betrag: z.B. 20,00Einheit: z.B. USDGültig ab: <Datum>, z.B. das aktuelle DatumWählen Sie Enter.Wählen Sie anschließend Sichern. | Ein Standardpreis für die Variante wird angelegt. |  |

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
- related-to :: [[14-maintenance-service-and-projects/criar-produto-de-servico-configuravel-mds-5be-script-de-dados-mestre-s]]
- related-to :: [[14-maintenance-service-and-projects/master-data-script-create-configurable-service-product-mds-5be-431]]
- related-to :: [[14-maintenance-service-and-projects/mds-5be-master-data-script-create-configurable-service-products-435]]
- related-to :: [[14-maintenance-service-and-projects/sap-s-4hana-cloud-public-edition-mds-5be-433]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/5BE_S4CLD2608_Master_Data_DE_XX.docx` — full document · extracted with `mammoth` · 50,322 chars in the whole document
