---
id: 14-maintenance-service-and-projects/stammdatenskript-sap-s-4hana-cloud-public-edition-serviceprodukt-fur-s
title: Stammdatenskript SAP S/4HANA Cloud Public Edition – Serviceprodukt für Servicevorgänge anlegen – SDS (3KV) (3KV_S4CLD2608_Master_Data_DE_XX)
description: "German master data script (3KV): step-by-step creation of service product materials (SRV_*, EXP_FSM_*) and their sales prices/conditions in S/4HANA Cloud Public Edition 2608."
cluster: 14-maintenance-service-and-projects
tags: [kb/maintenance-service-and-projects, topic/service-products-for-service-processes]
aliases: [3KV_S4CLD2608_Master_Data_DE_XX]
keywords: [Service Products and Service Prices, service product master data, material creation, service product prices, overtime pricing, calculation motive conditions, service contract products, field service management expenses, spare parts, service bundles]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/3KV_S4CLD2608_Master_Data_DE_XX.docx]
confidence: low
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-346
topic: 14-maintenance-service-and-projects/service-products-for-service-processes
language: DE
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Stammdatenskript SAP S/4HANA Cloud Public Edition – Serviceprodukt für Servicevorgänge anlegen – SDS (3KV) (3KV_S4CLD2608_Master_Data_DE_XX)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/3KV_S4CLD2608_Master_Data_DE_XX.docx`, extracted with `mammoth`. Grouped under **Service Products and Service Prices** in Maintenance, Service and Projects. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

| <!-- image omitted: unnamed --> | StammdatenskriptSAP S/4HANA Cloud Public Edition - 02-07-26 |
| --- | --- |
|  | Serviceprodukt für Servicevorgänge anlegen – SDS (3KV) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Inhaltsverzeichnis

[1 Zweck 3](#_Toc233889667)

[2 Voraussetzungen 4](#_Toc233889668)

[2.1 Systemzugriff 4](#_Toc233889669)

[2.2 Rollen 4](#_Toc233889670)

[2.3 Erforderliche Organisationseinheiten 4](#_Toc233889671)

[3 Übersichtstabelle 5](#_Toc233889672)

[4 Vorgehensweisen 6](#_Toc233889673)

[4.1 Serviceprodukte anlegen 6](#_Toc233889674)

[4.1.1 SRV_01 6](#_Toc233889675)

[4.1.2 SRV_CONTRACT 8](#_Toc233889676)

[4.1.3 SRV_CTR_RENEWAL 10](#_Toc233889677)

[4.1.4 SRV_02 12](#_Toc233889678)

[4.1.5 Field Service Management – Aufwandsposition 13](#_Toc233889679)

[4.1.6 SRV_03 15](#_Toc233889680)

[4.1.7 SRV_04 17](#_Toc233889681)

[4.1.8 SRV_BUNDLE_01 19](#_Toc233889682)

[4.1.9 SRV_BUNDLE_02 21](#_Toc233889683)

[4.1.10 SRV_05 23](#_Toc233889684)

[4.1.10.1 Grunddaten anlegen 23](#_Toc233889685)

[4.1.10.2 Verkaufsdaten anlegen 24](#_Toc233889686)

[4.1.10.3 Einkaufsdaten anlegen 26](#_Toc233889687)

[4.1.10.4 Dispositions-/Planungsdaten eingeben 27](#_Toc233889688)

[4.1.10.5 Lagerortdaten anlegen 29](#_Toc233889689)

[4.1.10.6 Buchhaltungsdaten anlegen 31](#_Toc233889690)

[4.2 Preise für Materialien festlegen 32](#_Toc233889691)

[4.2.1 Preis für SRV_01 32](#_Toc233889692)

[4.2.2 Preis für SRV_CONTRACT 33](#_Toc233889693)

[4.2.3 Preis für SRV_CTR_RENEWAL 34](#_Toc233889694)

[4.2.4 Preis für SRV_02 35](#_Toc233889695)

[4.2.5 Preis für SRV_04 36](#_Toc233889696)

[4.2.6 Preis für SRV_BUNDLE_01 37](#_Toc233889697)

[4.2.7 Preis für SRV_05 38](#_Toc233889698)

[4.2.8 Preis für FSM – Aufwand EXP_FSM_MILEAGE 39](#_Toc233889699)

[4.3 Preise für Mehrarbeit festlegen 41](#_Toc233889700)

[4.4 Konditionssatz für Berechnungsmotiv anlegen 42](#_Toc233889701)

## Zweck

Dieses Dokument beschreibt, wie Sie Stammdatensätze für das Serviceprodukt einschließlich Preise anlegen. Die Beschreibung umfasst die Datensegmente, die für die Stammdaten für die Arbeit in einer üblichen Systemumgebung relevant sind. Der Leser lernt hauptsächlich, welche Datensegmente und -felder hauptsächlich mit Eingabewerten gefüllt werden müssen. Felder, die nicht für den Umfang relevant sind, werden in diesem Dokument nicht behandelt, obwohl sie möglicherweise auf der Benutzungsoberfläche angezeigt werden.

Ein Serviceproduktstammsatz, der wie hier beschrieben angelegt wird, kann für die Abwicklung von Serviceaufträgen und Servicerückmeldungen verwendet werden.

| Serviceproduktnummer | Beschreibung | Verwendung |
| --- | --- | --- |
| SRV_01 | Service | stellt den Service selbst dar, z.B. Installation, Reparatur oder Instandhaltung |
| SRV_CONTRACT | Vertragsprodukt | stellt den Service innerhalb des Vertrags dar |
| SRV_CTR_RENEWAL | Servicevertragsverlängerungs-Produkt | stellt das Servicevertragsprodukt innerhalb des Vertrags mit voreingestellten Werten für die automatische Verlängerung dar |
| SRV_02 | Serviceaufwand | spiegelt den Aufwand wider, der mit dem Service verbunden ist, z.B. Reisekosten, Kraftstoff |
| SRV_03 | Ersatzteil (nicht definiert) | spiegelt ein für den Service benötigtes Material wider und ermöglicht die Eingabe einer FreitextbeschreibungDieses Nichtlagermaterial kann nur beschafft werden. |
| SRV_04 | Ersatzteil (definiert) | steht für Nichtlagermaterial mit minimaler bzw. ohne LogistikintegrationDieses Nichtlagermaterial kann nur beschafft werden. |
| SRV_05 | Lagerersatzteil | steht für ein Material an, das aus dem Bestand entnommen wird (Auslagerungsszenario) |
| SRV_06 | Lagerersatzteil mit Serialnummernprofil | bildet ein Material mit einem zugeordneten Serialnummernprofil ab, das aus dem Bestand entnommen wird (Auslagerungsszenario) |
| SRV_BUNDLE_01 | Servicepaket 01 | stellt einen komplexen Service als Paket mit Unterpositionen dar |
| SRV_BUNDLE_02 | Servicepaket 02 | stellt einen komplexen Service als Bündel mit Unterpositionen dar (Serviceposition und Festpreispositionen) |
| EXP_FSM_TRAVELEXP_FSM_MEALSEXP_FSM_OTHEREXP_FSM_MILEAGE | Serviceaufwand | spiegelt den Aufwand, z.B. Reisekosten oder Verpflegung, bei der Integration mit SAP Field Service Management wider |

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
| Stammdatenexperte – Produktdaten | SAP_BR_PRODMASTER_SPECIALIST | Stammdaten – Produkte / Produkt-Governance | SAP_BR_PRODMASTER_SPECIALIST / SAP_CMD_SPT_PR_GOV_PC |
| Preisfindungssachbearbeiter | SAP_BR_PRICING_SPECIALIST | Preisverwaltung | SAP_BR_PRICING_SPECIALIST |

### Erforderliche Organisationseinheiten

Einige Segmente von Stammdaten hängen von den Organisationseinheiten des Unternehmens ab. Allgemeine (zentrale) Daten hängen nicht von einer Organisationseinheit oder dem Buchungskreis ab. Die folgende Tabelle stellt eine Übersicht dieser verschiedenen Datensegmente und ihrer relevanten Organisationseinheiten bereit:

| Datensegment | Hängt ab von | Für die USA zu verwendende Organisationseinheit | Für DE zu verwendende Organisationseinheit |
| --- | --- | --- | --- |
| Material anlegen | Werk | 1710 (Werk 1 USA) | 1010 (Werk 1 DE) |
| Material anlegen | Verkaufsorganisation | 1710 (Inländ. Verkaufsorganisation USA) | 1010 (Inländ. Verkaufsorganisation DE) |
| Material anlegen | Vertriebsweg | 10 (Direktverkauf) | 10 (Direktverkauf) |

## Übersichtstabelle

Dieser Stammdatensatz umfasst mehrere Segmente, die in der nachfolgenden Tabelle genannt sind.

|  |
| --- |
| Hinweis Wenn Ihr Systemadministrator Bereiche und Seiten auf dem SAP Fiori Launchpad aktiviert hat, enthält die Startseite nur die wesentlichen Apps, mit denen die typischen Aufgaben einer Benutzerrolle ausgeführt werden können.Alle anderen (suchbaren) Apps, die nicht auf der Startseite enthalten sind, finden Sie über die Suchleiste ([2434549](https://me.sap.com/notes/2434549)).Wenn Sie die Startseite personalisieren und versteckte Apps hinzufügen möchten, wechseln Sie in Ihr Benutzerprofil und wählen Sie App Finder. |

| Segment | Anwendungsrolle | App/Vorgang | Erwartete Ergebnisse |
| --- | --- | --- | --- |
| Serviceprodukte anlegen | SAP_BR_PRODMASTER_SPECIALIST | Material anlegen(MM01) | Serviceprodukte werden angelegt. |
| Preise für Materialien festlegen (Konditionssätze anlegen) | SAP_BR_PRICING_SPECIALIST | Materialpreise festlegen – Verkauf(VK12) | Preise für Serviceprodukte werden definiert. |
| Preise für Mehrarbeit festlegen (Konditionssätze anlegen) | SAP_BR_PRICING_SPECIALIST | Materialpreise festlegen – Verkauf(VK12) | Preis für Mehrarbeit wurde definiert. |

## Vorgehensweisen

Dieser Abschnitt beschreibt die Vorgehensweisen für jedes Segment oder Prozessschritt, das bzw. der Teil dieses Stammsatzes ist.

### Serviceprodukte anlegen

#### SRV_01

Zweck

Dieses Material ist nur für die Cloud Edition relevant.

| Testschrittnummer | Bezeichnung des Testschritts | Anweisung | Erwartetes Ergebnis | Kommentare |
| --- | --- | --- | --- | --- |
| 1 | Anmelden | Melden Sie sich am SAP Fiori Launchpad als Stammdatenexperte – Produktdaten (MDG) an. | Die Startseite wird angezeigt. |  |
| 2 | SAP-Fiori-App aufrufen | Wählen Sie die App Material anlegen. | Das Bild Material anlegen wird angezeigt. |  |
| 3 | Materialgrunddaten (für das Serviceprodukt "Service") pflegen | Nehmen Sie auf dem Bild Material anlegen (Einstieg), die folgenden Einträge vor: Wählen Sie im Dialogfenster Folgendes:Material: SRV_01BrancheMWenn das Eingabefeld Branche ausgeblendet ist, ist keine Eingabe erforderlich. Wenn die Branche nicht zur Eingabe angeboten wird, wird "nicht bekannt" im Feld eingetragen. Derzeit ist nur ein Eintrag für die Branche vorhanden (M = Maschinenbau).Materialart: ServiceproduktWählen Sie anschließend Weiter (Enter). | Sie haben die grundlegenden Informationen für das neue Serviceprodukt erfasst.Das Dialogfenster Sichtenauswahl wird angezeigt. |  |
| 4 | Sichten wählen | Wählen Sie im Dialogfenster Sichtenauswahl die folgenden Sichten aus:Grunddaten 1Verkauf: VerkaufsorgDaten 1Verkauf: VerkaufsorgDaten 2Verkauf: All./WerksdatenEinkaufBuchhaltung 1Wählen Sie anschließend Weiter (Enter). | Das Bild Organisationsebene wird angezeigt. |  |
| 5 | Organisationsebenen wählen | Geben Sie im Dialogfenster Organisationsebenen die folgenden Werte ein:Werk: 1710 (Werk 1 USA)Verkaufsorganisation: 1710 (Inländ. Verkaufsorganisation USA)Vertriebsweg: 10 (Direktverkauf)Wählen Sie anschließend Weiter (Enter). | Es wurden Organisationsdaten ausgewählt.Die Sicht Material anlegen SRV_01 (Services) wird angezeigt. |  |
| 6 | Grunddaten pflegen | Pflegen Sie in der Sicht Grunddaten 1 die folgenden Werte:Beschreib.: ServiceBasismengeneinheit: h (Stunden)Materialgruppe: P001 (Services)GenItemGroup:SRVP (Serviceprodukt)Wählen Sie anschließend Weiter (Enter). | Die Grunddaten werden gepflegt, und die Registerkarte Vertrieb: VerkOrg 1 wird angezeigt.Hinweis Wenn Sie verschiedene Sprachen in Ihrem Unternehmen verwenden, müssen Sie für jeden relevanten Sprachencode die entsprechende Beschreibung für das Produkt pflegen. |  |
| 7 | Verkaufsorganisationsdaten (1) pflegen | Geben Sie in der Sicht Verkauf: VerkOrg 1 die folgenden Werte ein:Allgemeine DatenSkonto: X <markiert>SteuerdatenSteuerklassifikation: 1 (volle Steuer)Wählen Sie anschließend Enter. | Die Verkaufsorganisationsdaten sind gepflegt. Die Registerkarte Verkauf: VerkOrg 2 wird angezeigt. |  |
| 8 | Verkaufsorganisationsdaten (2) pflegen | Geben Sie in der Sicht Verkauf: VerkOrg 2 die folgenden Daten ein:Positionstypengruppe: SRVP (Serviceprodukt)Wählen Sie anschließend Enter. | Die Verkaufsorganisationsdaten sind gepflegt. Die Registerkarte Verkauf: Allg./Werk wird angezeigt. |  |
| 9 | Allgemeine Verkaufsdaten pflegen | Geben Sie in der Sicht Verkauf: Allg./Werk die folgenden Werte ein:Basismengeneinheit: h (Stunden)Arbeitsdauer: 1 hServiceprofil: 5x10 (Mo-Fr: 7-17h)Reaktionsschema: Erst. (Antwortzeit der ersten Ebene)Wählen Sie anschließend Enter. | Allgemeine Verkaufsdaten werden erfasst. |  |
| 10 | Einkaufsdaten bearbeiten | Nehmen Sie in der Sicht Einkauf im Abschnitt "Allgemeine Daten" folgende Einträge vor:Basismengeneinheit: z.B. Std.Materialgruppe: z.B. P001Einkäufergruppe z.B. 001Steuerind. Material: z.B. 1Wählen Sie anschließend Weiter (Enter). | Die Einkaufsdaten werden gepflegt. |  |
| 11 | Buchhaltungsdaten bearbeiten | Nehmen Sie in der Sicht Buchhaltung 1 im Abschnitt Aktuelle Bewertungsdaten folgenden Eintrag vor:Basismengeneinheit: z.B. Std.Bewertungsklasse: z.B. 3200Wählen Sie anschließend Sichern. | Die Buchhaltungsdaten werden gepflegt.Das Serviceprodukt wird gesichert. Das System zeigt die Sicht Material anlegen (Einstieg). |  |

#### SRV_CONTRACT

Zweck

Dieses Material ist für die Cloud- und die On-Premise-Edition relevant.

| Testschrittnummer | Bezeichnung des Testschritts | Anweisung | Erwartetes Ergebnis | Kommentare |
| --- | --- | --- | --- | --- |
| 1 | Anmelden | Melden Sie sich am SAP Fiori Launchpad als Stammdatenexperte – Produktdaten (MDG) an. | Die Startseite wird angezeigt. |  |
| 2 | SAP-Fiori-App aufrufen | Wählen Sie die App Material anlegen. | Das Bild Material anlegen (Einstieg) wird angezeigt. |  |
| 3 | Materialgrunddaten (für das Serviceprodukt "Service") pflegen | Nehmen Sie auf dem Bild Material anlegen (Einstieg) die folgenden Einträge vor:● Material: SRV_CONTRACTBranche: MWenn das Eingabefeld Branche ausgeblendet ist, ist keine Eingabe erforderlich. Wenn die Branche nicht zur Eingabe angeboten wird, wird "nicht bekannt" im Feld eingetragen. Derzeit ist nur ein Eintrag für die Branche vorhanden (M = Maschinenbau).● Materialart: ServiceproduktWählen Sie anschließend Weiter (Enter). | Sie haben die grundlegenden Informationen für das neue Serviceprodukt erfasst.Das Dialogfenster Sichtenauswahl wird angezeigt. |  |
| 4 | Sichten wählen | Wählen Sie im Dialogfenster Sichtenauswahl die folgenden Sichten aus:Grunddaten 1Vertrieb: VerkaufsorgDaten 1Vertrieb: VerkaufsorgDaten 2Vertrieb: All./WerksdatenWählen Sie anschließend Weiter (Enter). | Das Bild Organisationsebenen wird angezeigt. |  |
| 5 | Organisationsebenen wählen | Geben Sie im Dialogfenster Organisationsebenen die folgenden Werte ein:• Werk: 1710 (Werk 1 USA)• Verkaufsorg.: 1710 (Inländ. Verkaufsorganisation USA)• Vertriebsweg kanal: 10 (Direktverkauf)Wählen Sie anschließend Weiter (Enter). | Es wurden Organisationsdaten ausgewählt.Die Sicht Material anlegen SRV_CONTRACT (Serviceprodukt) wird angezeigt. |  |
| 6 | Grunddaten pflegen | Pflegen Sie in der Sicht Grunddaten 1 die folgenden Werte:• Beschr.: Servicevertragsprodukt• Basismengeneinheit: LE (Leistungseinheit)• Materialgruppe: P001 (Services)• GenItemGroup: SCNP-Serv. VertragsproduktWählen Sie anschließend Weiter (Enter). | Die Grunddaten werden gepflegt, und die Registerkarte Vertrieb: VerkOrg 1 wird angezeigt. |  |
| 7 | Verkaufsorganisationsdaten (1) pflegen | Geben Sie in der Sicht Verkauf: VerkOrg 1 die folgenden Werte ein:Allgemeine Daten• Skonto: X <ausgewählt>Steuerdaten•Steuerklassifikation: 1 (volle Steuer)Wählen Sie anschließend Weiter (Enter). | Die Verkaufsorganisationsdaten sind gepflegt. Die Registerkarte Verkauf: VerkOrg 2 wird angezeigt. |  |
| 8 | Verkaufsorganisationsdaten (2) pflegen | Geben Sie in der Sicht Verkauf: VerkOrg 2 die folgenden Daten ein:Positionstypengruppe: SNCP - Serv. VertragsproduktWählen Sie anschließend Weiter (Enter). | Die Verkaufsorganisationsdaten sind gepflegt. Die Registerkarte Verkauf: Allg./Werk wird angezeigt. |  |
| 9 | Allgemeine Verkaufsdaten pflegen | Geben Sie in der Sicht Verkauf: Allg./Werk die folgenden Werte ein:• Basismengeneinheit: LE (Leistungseinheit)• Arbeitsdauer: 1 Tag (Tage)• Serviceprofil: 5 x 10 (Mo-Fr: 7-17 Uhr)• Reaktionsschema.: FIRST (First-Level-Reaktionszeit)Wählen Sie anschließend Sichern. | Allgemeine Verkaufsdaten werden erfasst. |  |

#### SRV_CTR_RENEWAL

Zweck

Dieses Material ist für die Cloud- und die On-Premise-Edition relevant.

Für dieses Material werden Werte der automatischen Verlängerung vorgeschlagen.

| Testschrittnummer | Bezeichnung des Testschritts | Anweisung | Erwartetes Ergebnis | Kommentare |
| --- | --- | --- | --- | --- |
| 1 | Anmelden | Melden Sie sich am SAP Fiori Launchpad als Stammdatenexperte – Produktdaten (MDG) an. | Die Startseite wird angezeigt. |  |
| 2 | SAP-Fiori-App aufrufen | Wählen Sie die App Material anlegen. | Das Bild Material anlegen (Einstieg) wird angezeigt. |  |
| 3 | Materialgrunddaten (für das Serviceprodukt "Service") pflegen | Nehmen Sie auf dem Bild Material anlegen (Einstieg) die folgenden Einträge vor:● Material: SRV_CTR_RENEWAL● Branche: MWenn das Eingabefeld Branche ausgeblendet ist, ist keine Eingabe erforderlich. Wenn die Branche nicht zur Eingabe angeboten wird, wird "nicht bekannt" im Feld eingetragen. Derzeit ist nur ein Eintrag für die Branche vorhanden (M = Maschinenbau).● Materialart: ServiceproduktWählen Sie anschließend Weiter (Enter). | Sie haben die grundlegenden Informationen für das neue Serviceprodukt erfasst.Sie haben die grundlegenden Informationen für das neue Serviceprodukt erfasst. |  |
| 4 | Sichten wählen | Wählen Sie im Dialogfenster Sichtenauswahl die folgenden Sichten aus:Grunddaten 1Vertrieb: VerkaufsorgDaten 1Vertrieb: VerkaufsorgDaten 2Vertrieb: All./WerksdatenWählen Sie anschließend Weiter (Enter). | Das Bild Organisationsebenen wird angezeigt. |  |
| 5 | Organisationsebenen wählen | Geben Sie im Dialogfenster Organisationsebenen die folgenden Werte ein:• Werk: 1710 (Werk 1 USA)• Verkaufsorg.: 1710 (Inländ. Verkaufsorganisation USA)• Vertriebsweg kanal: 10 (Direktverkauf)Wählen Sie anschließend Weiter (Enter). | Es wurden Organisationsdaten ausgewählt.Die Sicht Material SRV_CTR_RENEWAL (Serviceprodukt) anlegen wird angezeigt. |  |
| 6 | Grunddaten pflegen | Pflegen Sie in der Sicht Grunddaten 1 die folgenden Werte:• Beschr.: Servicevertragsverlängerungs-Produkt• Basismengeneinheit: LE (Leistungseinheit)• Materialgruppe: P001 (Services)• GenItemGroup: SCNP-Serv. Vertragsprodukt• Kennzeichen für automatische Vertragsverlängerung: 1Wählen Sie anschließend Weiter (Enter). | Die Grunddaten werden gepflegt, und die Registerkarte Vertrieb: VerkOrg 1 wird angezeigt. |  |
| 7 | Verkaufsorganisationsdaten (1) pflegen | Geben Sie in der Sicht Verkauf: VerkOrg 1 die folgenden Werte ein:Allgemeine Daten• Skonto: X <ausgewählt>Steuerdaten•Steuerklassifikation: 1 (volle Steuer)Wählen Sie anschließend Weiter (Enter). | Die Verkaufsorganisationsdaten sind gepflegt. Die Registerkarte Verkauf: VerkOrg 2 wird angezeigt. |  |
| 8 | Verkaufsorganisationsdaten (2) pflegen | Geben Sie in der Sicht Verkauf: VerkOrg 2 die folgenden Daten ein:Gruppierungsbegriffe• Positionstypengruppe: SRVP (Serviceprodukt)Automatische Verlängerung des Verlängerungszeitraums• Standardverlängerungszeitraum: 1• Einheit VerlngZeitrm: Jahr Wählen Sie anschließend Weiter (Enter). | Die Verkaufsorganisationsdaten sind gepflegt. Die Registerkarte Verkauf: Allg./Werk wird angezeigt. |  |
| 9 | Allgemeine Verkaufsdaten pflegen | Geben Sie in der Sicht Verkauf: Allg./Werk die folgenden Werte ein:• Basismengeneinheit: LE (Leistungseinheit)• Arbeitsdauer: 1 Tag (Tage)• Serviceprofil: 5 x 10 (Mo-Fr: 7-17 Uhr)• Reaktionsschema.: FIRST (First-Level-Reaktionszeit)Wählen Sie anschließend Sichern. | Allgemeine Verkaufsdaten werden erfasst.Das Serviceprodukt wird gesichert. Das System zeigt die Sicht Material anlegen (Einstieg). |  |

#### SRV_02

Zweck

Dieses Material ist nur für die Cloud Edition relevant.

| Testschrittnummer | Bezeichnung des Testschritts | Anweisung | Erwartetes Ergebnis | Kommentare |
| --- | --- | --- | --- | --- |
| 1 | Anmelden | Melden Sie sich am SAP Fiori Launchpad als Stammdatenexperte – Produktdaten (MDG) an. | Die Startseite wird angezeigt. |  |
| 2 | SAP-Fiori-App aufrufen | Wählen Sie die App Material anlegen. | Das Bild Material anlegen (Einstieg) wird angezeigt. |  |
| 3 | Materialgrunddaten (für das Serviceprodukt "Serviceaufwand") pflegen | Nehmen Sie auf dem Bild Material anlegen (Einstieg), die folgenden Einträge vor:Material: SRV_02Branche MWenn das Eingabefeld Branche ausgeblendet ist, ist keine Eingabe erforderlich. Wenn die Branche nicht zur Eingabe angeboten wird, wird "nicht bekannt" im Feld eingetragen. Derzeit ist nur ein Eintrag für die Branche vorhanden (M = Maschinenbau).Materialart: ServiceproduktWählen Sie anschließend Weiter (Enter). | Sie haben die grundlegenden Informationen für das neue Serviceprodukt erfasst.Das Dialogfenster Sichtenauswahl wird angezeigt. |  |
| 4 | Sichten wählen | Wählen Sie im Dialogfenster Sichtenauswahl die folgenden Sichten aus:Grunddaten 1Vertrieb: VerkaufsorgDaten 1Vertrieb: VerkaufsorgDaten 2Vertrieb: All./WerksdatenInternational Trade: ExportWählen Sie anschließend Weiter (Enter). | Das Bild Organisationsebenen wird angezeigt. |  |
| 5 | Organisationsebenen wählen | Geben Sie im Dialogfenster Organisationsebenen die folgenden Werte ein:Werk: 1710 (Werk 1 USA)Verkaufsorganisation: 1710 (Inländ. Verkaufsorganisation USA)Vertriebsweg: 10 (Direktverkauf)Wählen Sie anschließend Weiter (Enter). | Es wurden Organisationsdaten ausgewählt.Die Sicht Material anlegen SRV_02 (Serviceaufwand) wird angezeigt. |  |
| 6 | Grunddaten pflegen | Pflegen Sie in der Sicht Grunddaten 1 die folgenden Werte:Beschreib.: ServiceaufwandBasismengeneinheit: ST (Stück)Materialgruppe: P002 (Aufwand)GenItemGroup: SRVE (Aufwandsposition)Wählen Sie anschließend Weiter (Enter). | Die Grunddaten wurden gepflegt, und die Registerkarte Vertrieb: VerkOrg 1 wird angezeigt.Hinweis Wenn Sie verschiedene Sprachen in Ihrem Unternehmen verwenden, müssen Sie für jeden relevanten Sprachencode die entsprechende Beschreibung für das Produkt pflegen. |  |
| 7 | Verkaufsorganisationsdaten (1) pflegen | Geben Sie in der Sicht Verkauf: VerkOrg 1 die folgenden Werte ein:Allgemeine DatenSkonto: <markiert>SteuerdatenSteuerklassifikation: 1 (volle Steuer)Wählen Sie anschließend Weiter (Enter). | Die Verkaufsorganisationsdaten sind gepflegt. Die Registerkarte Verkauf: VerkOrg 2 wird angezeigt. |  |
| 8 | Verkaufsorganisationsdaten (2) pflegen | Geben Sie in der Sicht Verkauf: VerkOrg 2 die folgenden Daten ein:Positionstypengruppe: SRVE (Ausgabenposition)Wählen Sie anschließend Weiter (Enter). | Die Verkaufsorganisationsdaten sind gepflegt. Das Serviceprodukt wird gesichert. |  |

#### Field Service Management – Aufwandsposition

Zweck

Dieses Material ist nur für die Cloud Edition relevant.

Servicepositionen in Field Service Management übernehmen (Serviceauftragsabwicklung mit SAP Field Service Management), wie SRV_02, z.B. "Aufwandsposition für Unterkunft".

| Testschrittnummer | Bezeichnung des Testschritts | Anweisung | Erwartetes Ergebnis | Kommentare |
| --- | --- | --- | --- | --- |
| 1 | Anmelden | Melden Sie sich am SAP Fiori Launchpad als Stammdatenexperte – Produktdaten an. | Die Startseite wird angezeigt. |  |
| 2 | SAP-Fiori-App aufrufen | Wählen Sie die App Material anlegen. | Das Bild Material anlegen (Einstieg) wird angezeigt. |  |
| 3 | Materialgrunddaten (für das Serviceprodukt "Serviceaufwand") pflegen | Nehmen Sie auf dem Bild Material anlegen (Einstieg), die folgenden Einträge vor:Material:EXP_FSM_ACCOMBranche MWenn das Eingabefeld Branche ausgeblendet ist, ist keine Eingabe erforderlich. Wenn die Branche nicht zur Eingabe angeboten wird, wird "nicht bekannt" im Feld eingetragen. Derzeit ist nur ein Eintrag für die Branche vorhanden (M = Maschinenbau).Materialart: ServiceproduktWählen Sie anschließend Weiter (Enter). | Sie haben die grundlegenden Informationen für das neue Serviceprodukt erfasst.Sie können als Aufwand auch ein Material anlegen, zum Beispiel:EXP_FSM_MEALSEXP_FSM_OTHEREXP_FSM_TRAVELEXP_FSM_MILEAGEDas Dialogfenster Sichtenauswahl wird angezeigt. |  |
| 4 | Sichten wählen | Wählen Sie im Dialogfenster Sichtenauswahl die folgenden Sichten aus:Grunddaten 1Vertrieb: VerkaufsorgDaten 1Vertrieb: VerkaufsorgDaten 2Vertrieb: All./WerksdatenBuchhaltung 1 (nur für EXP_FSM_MILEAGE)Wählen Sie anschließend Weiter (Enter). | Das Bild Organisationsebenen wird angezeigt. |  |
| 5 | Organisationsebenen wählen | Geben Sie im Dialogfenster Organisationsebenen die folgenden Werte ein:Werk: 1710 (Werk 1 USA)Verkaufsorganisation: 1710 (Inländ. Verkaufsorganisation USA)Vertriebsweg: 10 (Direktverkauf)Wählen Sie anschließend Weiter (Enter). | Es wurden Organisationsdaten ausgewählt.Die Sicht Material anlegen SRV_02 (Serviceaufwand) wird angezeigt. |  |
| 6 | Grunddaten pflegen | Pflegen Sie in der Sicht Grunddaten 1 die folgenden Werte:Beschreibung:ServiceaufwandFür alle Aufwände außer EXP_FSM_MILEAGEBasismengeneinheit: ST (Stück)Für Aufwand EXP_FSM_MILEAGEBasismengeneinheit:KM (Kilometer)Materialgruppe: P002 (Aufwand)GenItemGroup: SRVE (Aufwandsposition)Wählen Sie anschließend Sichern. | Die Grunddaten wurden gepflegt, und die Registerkarte Vertrieb: VerkOrg 1 wird angezeigt. |  |
| 7 | Verkaufsorganisationsdaten (1) pflegen | Geben Sie in der Sicht Verkauf: VerkOrg 1 die folgenden Werte ein:Allgemeine DatenSkonto: <markiert>SteuerdatenSteuerklassifikation: 1 (volle Steuer)Wählen Sie anschließend Sichern. | Die Verkaufsorganisationsdaten sind gepflegt. Die Registerkarte Verkauf: VerkOrg 2 wird angezeigt. |  |
| 8 | Verkaufsorganisationsdaten (2) pflegen | Geben Sie in der Sicht Verkauf: VerkOrg 2 die folgenden Daten ein:Positionstypengruppe: SRVE (Ausgabenposition)Wählen Sie anschließend Sichern.Für Polen oder EXP_FSM_MILEAGE: Drücken Sie Enter, anstatt Sichern zu wählen. | Die Verkaufsorganisationsdaten sind erfasst. Das Aufwandsprodukt wird gesichert. |  |
| 9 | Buchhaltung 1 pflegen(nur für EXP_FSM_MILEAGE) | Pflegen Sie in der Sicht "Buchhaltung 1" die folgenden Werte:Aktuelle Bewertung- Wertklasse: z.B. 3300- Standardpreis: z.B. 1,50Wählen Sie anschließend Sichern. | Die Daten für Buchhaltung 1 werden gepflegt. Das Aufwandsprodukt wird gesichert. |  |

#### SRV_03

Zweck

Dieses Material ist nur für die Cloud Edition relevant.

| Testschrittnummer | Bezeichnung des Testschritts | Anweisung | Erwartetes Ergebnis | Kommentare |
| --- | --- | --- | --- | --- |
| 1 | Anmelden | Melden Sie sich am SAP Fiori Launchpad als Stammdatenexperte – Produktdaten (MDG) an. | Die Startseite wird angezeigt. |  |
| 2 | SAP-Fiori-App aufrufen | Wählen Sie die App Material anlegen. | Das Bild Material anlegen (Einstieg) wird angezeigt. |  |
| 3 | Materialgrunddaten (für das Serviceprodukt "Ersatzteil") pflegen | Nehmen Sie auf dem Bild Material anlegen (Einstieg), die folgenden Einträge vor:Material: SRV_03Branche: MWenn das Eingabefeld Branche ausgeblendet ist, ist keine Eingabe erforderlich. Wenn die Branche nicht zur Eingabe angeboten wird, wird "nicht bekannt" im Feld eingetragen. Derzeit ist nur ein Eintrag für die Branche vorhanden (M = Maschinenbau).Materialart: NichtlagermaterialWählen Sie anschließend Weiter (Enter). | Sie haben die grundlegenden Informationen für das neue Serviceprodukt erfasst.Das Dialogfenster Sichtenauswahl wird angezeigt. |  |
| 4 | Sichten wählen | Wählen Sie im Dialogfenster Sichtenauswahl die folgenden Sichten aus:Grunddaten 1Vertrieb: VerkaufsorgDaten 1Vertrieb: VerkaufsorgDaten 2Vertrieb: All./WerksdatenEinkaufBuchhaltung 1Wählen Sie anschließend Weiter (Enter). | Das Bild Organisationsebenen wird angezeigt. |  |
| 5 | Organisationsebenen wählen | Geben Sie im Dialogfenster Organisationsebenen die folgenden Werte ein:Werk: 1710 (Werk 1 USA)Verkaufsorganisation: 1710 (Inländ. Verkaufsorganisation USA)Vertriebsweg: 10 (Direktverkauf)Wählen Sie anschließend Weiter (Enter). | Es wurden Organisationsdaten ausgewählt.Die Sicht Material anlegen SRV_03 (Ersatzteil) wird angezeigt. |  |
| 6 | Grunddaten pflegen | Pflegen Sie in der Sicht Grunddaten 1 die folgenden Werte:Beschr.: ErsatzteilBasismengeneinheit: ST (Stück)Materialgruppe: YBMM00 (Nichtlagermaterial ohne ID)GenItemGroup: SRVM (Servicematerial)Wählen Sie anschließend Weiter (Enter). | Die Grunddaten werden gepflegt, und die Registerkarte Vertrieb: VerkOrg 1 wird angezeigt.Hinweis Wenn Sie verschiedene Sprachen in Ihrem Unternehmen verwenden, müssen Sie für jeden relevanten Sprachencode die entsprechende Beschreibung für das Produkt pflegen. |  |
| 7 | Verkaufsorganisationsdaten (1) pflegen | Geben Sie in der Sicht Verkauf: VerkOrg 1 die folgenden Werte ein:Allgemeine DatenSkonto: <markiert>SteuerdatenSteuerklassifikation: 1 (volle Steuer)Wählen Sie anschließend Enter. | Die Verkaufsorganisationsdaten sind gepflegt. Die Registerkarte Verkauf: VerkOrg 2 wird angezeigt. |  |
| 8 | Verkaufsorganisationsdaten (2) pflegen | Geben Sie in der Sicht Verkauf: VerkOrg 2 die folgenden Daten ein:Positionstypengruppe: SRVM (Servicematerial) | Die Verkaufsorganisationsdaten werden gepflegt. |  |
| 9 | Einkaufsdaten bearbeiten | Nehmen Sie in der Sicht Einkauf im Abschnitt Allgemeine Daten folgende Einträge vor:Basismengeneinheit: z.B. STMaterialgruppe: z.B. YBM00Einkäufergruppe: z.B. 001Steuerind. Material: z.B. 1Wählen Sie anschließend Weiter (Enter). | Die Einkaufsdaten werden gepflegt. |  |
| 10 | Buchhaltungsdaten bearbeiten | Nehmen Sie in der Sicht Buchhaltung 1 im Abschnitt aktuelle Bewertungsdaten folgenden Eintrag vor:Bewertungsklasse: z.B. YB01Preissteuerung: z.B. SStandardpreis: z.B. 1Preiseinheit: z.B. 1Wählen Sie anschließend Sichern. | Die Buchhaltungsdaten werden gepflegt.Das Serviceprodukt wird gesichert. Das System zeigt die Sicht Material anlegen (Einstieg) an. |  |

#### SRV_04

Zweck

Dieses Material ist nur für die Cloud Edition relevant.

| Testschrittnummer | Bezeichnung des Testschritts | Anweisung | Erwartetes Ergebnis | Kommentare |
| --- | --- | --- | --- | --- |
| 1 | Anmelden | Melden Sie sich am SAP Fiori Launchpad als Stammdatenexperte – Produktdaten (MDG) an. | Die Startseite wird angezeigt. |  |
| 2 | SAP-Fiori-App aufrufen | Wählen Sie die App Material anlegen. | Das Bild Material anlegen (Einstieg) wird angezeigt. |  |
| 3 | Materialgrunddaten (für das Serviceprodukt "Verwaltetes Ersatzteil") pflegen | Nehmen Sie auf dem Bild Material anlegen (Einstieg) die folgenden Einträge vor:● Material: SRV_04● Branche: MIst das Eingabefeld "Branche" ausgeblendet, ist keine Eingabe erforderlich. Wenn die Branche nicht zur Eingabe angeboten wird, wird "nicht bekannt" im Feld eingetragen. Derzeit ist nur ein Eintrag für die Branche vorhanden (M = Maschinenbau).● Materialart: NichtlagermaterialWählen Sie anschließend Weiter (Enter). | Sie haben die grundlegenden Informationen für das neue Serviceprodukt erfasst.Das Dialogfenster Sichtenauswahl wird angezeigt. |  |
| 4 | Sichten wählen | Wählen Sie im Dialogfenster Sichtenauswahl die folgenden Sichten aus:Grunddaten 1Vertrieb: VerkaufsorgDaten 1Vertrieb: VerkaufsorgDaten 2Vertrieb: All./WerksdatenInternational Trade: ExportEinkaufBuchhaltung 1Wählen Sie anschließend Weiter (Enter). | Das Bild Organisationsebenen wird angezeigt. |  |
| 5 | Organisationsebenen wählen | Geben Sie im Dialogfenster Organisationsebenen die folgenden Werte ein:● Werk: 1710 (Werk 1 USA)● Verkaufsorg.: 1710 (Inländ. Verkaufsorganisation USA)● Vertriebs- weg: 10 (Direktverkauf)Wählen Sie anschließend Weiter (Enter). | Die Organisationsdaten sind ausgewählt.Die Sicht Material anlegen SRV_04 (Verwaltetes Ersatzteil (Nichtlager)) wird angezeigt. |  |
| 6 | Grunddaten pflegen | Pflegen Sie in der Sicht "Grunddaten 1" die folgenden Werte:● Beschr.: SRV_04 Verwaltetes Ersatzteil (Nichtlager)● Basismengeneinheit: ST (Stück)● Materialgruppe: YBMM01 (Nichtlagermaterial mit ID)●AllgPosGrp: SRVM (Servicematerial)Wählen Sie anschließend Weiter (Enter). | Die Grunddaten werden gepflegt, und die Registerkarte Vertrieb: VerkOrg 1 wird angezeigt.Hinweis Wenn Sie verschiedene Sprachen in Ihrem Unternehmen verwenden, müssen Sie für jeden relevanten Sprachencode die entsprechende Beschreibung für das Produkt pflegen. |  |
| 7 | Verkaufsorganisationsdaten (1) pflegen | Geben Sie in der Sicht Verkauf: VerkOrg 1 die folgenden Werte ein:Allgemeine Daten• Skonto: <markiert>Steuerdaten• Steuerklassifikation: 1 (volle Steuer)Wählen Sie anschließend Enter. | Die Verkaufsorganisationsdaten sind gepflegt. Die Registerkarte Verkauf: VerkOrg 2 wird angezeigt. |  |
| 8 | Verkaufsorganisationsdaten (2) pflegen | Geben Sie in der Sicht Verkauf: VerkOrg 2 die folgenden Daten ein:Positionstypengruppe: SRVM (Servicematerial)Wählen Sie anschließend Weiter (Enter). | Die Verkaufsorganisationsdaten sind gepflegt. |  |
| 9 | Ersatzteil – Einkaufsdaten bearbeiten | Nehmen Sie in der Sicht Einkauf im Abschnitt Allgemeine Daten folgende Einträge vor:• Basismengeneinheit: z.B. ST• Materialgruppe: z.B. YBMM01Einkäufergruppe: z.B. 001Steuerind. Material: z.B. 1Wählen Sie anschließend Weiter (Enter). | Die Einkaufsdaten werden gepflegt. |  |
| 10 | Buchhaltungsdaten bearbeiten | Nehmen Sie in der Sicht Buchhaltung 1 im Abschnitt Aktuelle Bewertungsdaten folgenden Eintrag vor:Bewertungsklasse: z.B. YB01• Preissteuerung: z.B. S• Standardpreis: z.B. 1• Preiseinheit: z.B. 1Wählen Sie anschließend Sichern. | Die Buchhaltungsdaten werden gepflegt.Das Serviceprodukt wird gesichert.Das System zeigt die Sicht Material anlegen (Einstieg). |  |

#### SRV_BUNDLE_01

Zweck

Dieses Material ist nur für die Cloud Edition relevant.

| Testschrittnummer | Bezeichnung des Testschritts | Anweisung | Erwartetes Ergebnis | Kommentare |
| --- | --- | --- | --- | --- |
| 1 | Anmelden | Melden Sie sich am SAP Fiori Launchpad als Stammdatenexperte – Produktdaten (MDG) an. | Die Startseite wird angezeigt. |  |
| 2 | SAP-Fiori-App aufrufen | Wählen Sie die App Material anlegen. | Das Bild Material anlegen (Einstieg) wird angezeigt. |  |
| 3 | Materialgrunddaten (für das Serviceprodukt "Service") pflegen | Nehmen Sie auf dem Bild Material anlegen (Einstieg), die folgenden Einträge vor:● Material: SRV_BUNDLE_01● Branche: MWenn das Eingabefeld "Branche" ausgeblendet ist, ist keine Eingabe erforderlich. Wenn die Branche nicht zur Eingabe angeboten wird, wird "nicht bekannt" im Feld eingetragen. Derzeit ist nur ein Eintrag für die Branche vorhanden (M = Maschinenbau).● Materialart: ServiceproduktWählen Sie anschließend Weiter (Enter). | Sie haben die grundlegenden Informationen für das neue Serviceprodukt erfasst.Das Dialogfenster Sichtenauswahl wird angezeigt. |  |
| 4 | Sichten wählen | Wählen Sie im Dialogfenster Sichtenauswahl die folgenden Sichten aus:Grunddaten 1Vertrieb: VerkaufsorgDaten 1Vertrieb: VerkaufsorgDaten 2Vertrieb: All./WerksdatenInternational Trade: ExportWählen Sie anschließend Weiter (Enter). | Das Bild Organisationsebenen wird angezeigt. |  |
| 5 | Organisationsebenen wählen | Geben Sie im Dialogfenster Organisationsebenen die folgenden Werte ein:● Werk: 1710 (Werk 1 USA)● Verkaufsorg.: 1710 (Inländ. Verkaufsorganisation USA)● Vertriebs- weg: 10 (Direktverkauf)Wählen Sie anschließend Weiter (Enter). | Die Organisationsdaten sind ausgewählt.Die Sicht Material anlegen SRV_BUNDLE_01 (Services) wird angezeigt. |  |
| 6 | Grunddaten pflegen | Pflegen Sie in der Sicht Grunddaten 1 die folgenden Werte:● Beschr.: Festpreis Servicepaket● Basismengeneinheit: ST (Stück)● Materialgruppe: p001 (Services)●AllgPosGrp: SVBL (Servicepaket FP)Wählen Sie anschließend Weiter (Enter). | Die Grunddaten werden gepflegt, und die Registerkarte Vertrieb: VerkOrg 1 wird angezeigt.Hinweis Wenn Sie verschiedene Sprachen in Ihrem Unternehmen verwenden, müssen Sie für jeden relevanten Sprachencode die entsprechende Beschreibung für das Produkt pflegen. |  |
| 7 | Verkaufsorganisationsdaten (1) pflegen | Geben Sie in der Sicht Verkauf: VerkOrg 1 die folgenden Werte ein:Allgemeine DatenSkonto: X <markiert>Steuerdaten• Steuerklassifikation: 1 (volle Steuer)Wählen Sie anschließend Enter. | Die Verkaufsorganisationsdaten sind gepflegt. Die Registerkarte Verkauf: VerkOrg 2 wird angezeigt. |  |
| 8 | Verkaufsorganisationsdaten (2) pflegen | Geben Sie in der Sicht Verkauf: VerkOrg 2 die folgenden Daten ein:Positionstypengruppe: SVBL (Servicepaket FP)Wählen Sie anschließend Weiter (Enter). | Die Verkaufsorganisationsdaten sind gepflegt. Die Registerkarte Verkauf: Allg./Werk wird angezeigt. |  |
| 9 | Allgemeine Verkaufsdaten pflegen | Geben Sie in der Sicht Verkauf: Allg./Werk die folgenden Werte ein:• Basismengeneinheit: ST (Stück)• Arbeitsdauer: z.B. 2 h (Stunden)Wählen Sie anschließend Weiter (Enter). | Allgemeine Verkaufsdaten werden erfasst. |  |

#### SRV_BUNDLE_02

Zweck

Dieses Material ist nur für die Cloud Edition relevant.

| Testschrittnummer | Bezeichnung des Testschritts | Anweisung | Erwartetes Ergebnis | Kommentare |
| --- | --- | --- | --- | --- |
| 1 | Anmelden | Melden Sie sich am SAP Fiori Launchpad als Stammdatenexperte – Produktdaten an. | Die Startseite wird angezeigt. |  |
| 2 | SAP-Fiori-App aufrufen | Wählen Sie die App Material anlegen. | Das Bild Material anlegen (Einstieg) wird angezeigt. |  |
| 3 | Materialgrunddaten (für das Serviceprodukt "Service") pflegen | Nehmen Sie auf dem Bild Material anlegen (Einstieg), die folgenden Einträge vor:Material: SRV_BUNDLE_02Branche MWenn das Eingabefeld "Branche" ausgeblendet ist, ist keine Eingabe erforderlich. Wenn die Branche nicht zur Eingabe angeboten wird, wird "nicht bekannt" im Feld eingetragen. Derzeit ist nur ein Eintrag für die Branche vorhanden (M = Maschinenbau).Materialart: ServiceproduktWählen Sie anschließend Weiter (Enter). | Sie haben die grundlegenden Informationen für das neue Serviceprodukt erfasst.Das Dialogfenster Sichtenauswahl wird angezeigt. |  |
| 4 | Sichten wählen | Wählen Sie im Dialogfenster Sichtenauswahl die folgenden Sichten aus:Grunddaten 1Vertrieb: VerkaufsorgDaten 1Vertrieb: VerkaufsorgDaten 2Vertrieb: All./WerksdatenWählen Sie anschließend Weiter (Enter). | Das Bild Organisationsebenen wird angezeigt. |  |
| 5 | Organisationsebenen wählen | Geben Sie im Dialogfenster Organisationsebenen die folgenden Werte ein:Werk: 1710 (Werk 1 USA)Verkaufsorg.: 1710 (Inländ. Verkaufsorganisation USA)Vertriebsweg: 10 (Direktverkauf)Wählen Sie anschließend Weiter (Enter). | Die Organisationsdaten sind ausgewählt.Die Sicht Material anlegen SRV_BUNDLE_02 (Services) wird angezeigt. |  |
| 6 | Grunddaten pflegen | Pflegen Sie in der Sicht "Grunddaten 1" die folgenden Werte:Beschreib.: ServicepaketBasismengeneinheit: ST (Stück)Materialgruppe: p001 (Services)GenItemGroup: SVBV (Servicepaket T&M)Wählen Sie anschließend Weiter (Enter). | Die Grunddaten werden gepflegt, und die Registerkarte Vertrieb: VerkOrg 1 wird angezeigt.Hinweis Wenn Sie verschiedene Sprachen in Ihrem Unternehmen verwenden, müssen Sie für jeden relevanten Sprachencode die entsprechende Beschreibung für das Produkt pflegen. |  |
| 7 | Verkaufsorganisationsdaten (1) pflegen | Geben Sie in der Sicht Verkauf: VerkOrg 1 die folgenden Werte ein:Allgemeine DatenSkonto: X <ausgewählt>SteuerdatenSteuerklassifikation: 1 (volle Steuer)Wählen Sie anschließend Enter. | Die Verkaufsorganisationsdaten sind gepflegt. Die Registerkarte Verkauf: VerkOrg 2 wird angezeigt. |  |
| 8 | Verkaufsorganisationsdaten (2) pflegen | Geben Sie in der Sicht Verkauf: VerkOrg 2 die folgenden Daten ein:Positionstypengruppe: SVBV (Servicepaket)Wählen Sie anschließend Weiter (Enter). | Die Verkaufsorganisationsdaten sind gepflegt. Die Registerkarte Verkauf: allg./Werk wird angezeigt. |  |
| 9 | Allgemeine Verkaufsdaten pflegen | Geben Sie in der Sicht Verkauf: Allg./Werk die folgenden Werte ein:Basismengeneinheit: ST (Stück)Arbeitsdauer: z.B. 2 h (Stunden)Wählen Sie anschließend Sichern. | Allgemeine Verkaufsdaten werden erfasst. |  |

#### SRV_05

##### Grunddaten anlegen

Zweck

Dieses Material ist nur für die Cloud Edition relevant.

Vorgehensweise

| Testschrittnummer | Bezeichnung des Testschritts | Anweisung | Erwartetes Ergebnis | Kommentare |
| --- | --- | --- | --- | --- |
| 1 | Anmelden | Melden Sie sich am SAP Fiori Launchpad als Stammdatenexperte – Produktdaten (MDG) an. | Das SAP Fiori Launchpad wird angezeigt. |  |
| 2 | SAP-Fiori-App aufrufen | Wählen Sie die App Material anlegen. | Das Bild Material anlegen (Einstieg) wird geöffnet. |  |
| 3 | Materialgrunddaten eingeben | Geben Sie auf dem Bild Material anlegen (Einstieg) Folgendes ein:Material: SRV_05Branche: MHinweis Ist das Eingabefeld Branche ausgeblendet, ist keine Eingabe erforderlich. Wird die Branche nicht zur Eingabe angeboten, wird "nicht bekannt" im Feld eingetragen.Materialart: HandelswareWählen Sie Sichtenauswahl. | In einem neuen Fenster wird das Bild Sichtenauswahl angezeigt. |  |
| 4 | Sichten wählen | Wählen Sie auf dem Bild Sichtenauswahl die Registerkarte Grunddaten 1, und geben Sie folgende Daten ein: | Das Bild Material SRV_05 (Handelsware) anlegen wird geöffnet. |  |
| 5 | Grunddaten eingeben | Geben Sie Folgendes ein:Beschreibung: LagerersatzteilGeben Sie im Abschnitt Allgemeine Daten die folgenden Daten ein:Basiseinheit: STProduktgruppe: L001Sparte: 00Allg. PosTypGrp: SVST oder NORMGeben Sie im Abschnitt Dimensionen/EANs Folgendes ein:Bruttogewicht: 2Gewichtseinheit: kgNettogewicht: 1 | Hinweis Wenn Sie verschiedene Sprachen in Ihrem Unternehmen verwenden, müssen Sie für jeden relevanten Sprachencode die entsprechende Beschreibung für das Produkt pflegen. |  |
| 6 | Grunddaten abschließen | Auf der Registerkarte Grunddaten 2 müssen Sie keine Einträge vornehmen. |  |  |
| 7 | Daten sichern | Wählen Sie unten rechts im Bild Sichern, um Ihre Daten zu sichern. | Das Bild Material anlegen (Einstieg) wird geöffnet.Die Grunddaten werden erzeugt und gesichert. |  |

##### Verkaufsdaten anlegen

Zweck

Dieses Material ist nur für die Cloud Edition relevant.

Voraussetzung

Sie müssen den vorangehenden Abschnitt "Grunddaten anlegen" erst abschließen, bevor Sie mit diesem Abschnitt fortfahren können.

Vorgehensweise

| Testschrittnummer | Bezeichnung des Testschritts | Anweisung | Erwartetes Ergebnis | Kommentare |
| --- | --- | --- | --- | --- |
| 1 | SAP-Fiori-App aufrufen | Wählen Sie die App Material anlegen. | Das Bild Material anlegen (Einstieg) wird angezeigt. |  |
| 2 | Materialgrunddaten eingeben | Nehmen Sie auf dem Bild Material anlegen die folgenden Einträge vor:Material: SRV_05Materialart: HandelswareWählen Sie Sichtenauswahl. | Nachdem Sie die Einträge vorgenommen haben, wird ein neues Fenster Sichtenauswahl geöffnet. |  |
| 3 | Sichten wählen | Wählen Sie im Fenster Sichtenauswahl die Sichten Vertrieb: VerkaufsorgDaten 1, Vertrieb: VerkaufsorgDaten 2 und Vertrieb: Allg./Werksdaten aus, und wählen Sie dann Weiter. | Ein Fenster mit Organisationsebenen wird angezeigt. |  |
| 4 | Organisationsebenendaten eingeben | Geben Sie im Bild Organisationsebenen im Abschnitt Organisationsebene Beschreibungen für folgende Einträge ein:Werk: 1710Verkaufsorg.: 1710Vertriebsweg: 10Wählen Sie Weiter.Hinweis Im unteren Bildbereich wird folgende Information angezeigt: Das Material existiert bereits und wird erweitert. | Das Bild Material SRV_05 (Handelsware) anlegen wird angezeigt. |  |
| 5 | Verkaufsdaten eingeben | Nehmen Sie auf dem Bild Material SRV_05 (Handelsware) auf der Registerkarte Vertrieb: VerkOrg 1 im Bereich Allgemeine Daten folgenden Eintrag vor:Auslieferungswerk: 1710 |  |  |
| 6 | Verkaufsdaten eingeben | Nehmen Sie auf dem Bild Material SRV_05 (Handelsware) auf der Registerkarte Vertrieb: VerkOrg 1 im Bereich Steuerdaten folgende Einträge vor:Steuerklassifikation: 1Wählen Sie die Registerkarte Vertrieb: Verkaufsorganisation 2. | Die nächste Registerkarte Vertrieb: VerkOrg 2 wird angezeigt.. |  |
| 7 | Verkaufsdaten eingeben | Nehmen Sie auf der Registerkarte Vertrieb: Verkaufsorganisation 2 im Abschnitt Gruppierungsbegriffe den folgenden Eintrag vor:Kontierungsgr. Mat.: 01Positionstypengruppe: SVST oder NORMWählen Sie die Registerkarte Vertrieb: Allg./Werk. | Die nächste Registerkarte Vertrieb: Allg./Werk wird angezeigt. |  |
| 8 | Verkaufsdaten eingeben | Nehmen Sie auf der Registerkarte Vertrieb: Allg./Werk im Abschnitt Allgemeine Daten folgende Einträge vor:Verfügbarkeitsprüfung: SP |  |  |
| 9 | Verkaufsdaten eingeben | Nehmen Sie auf der Registerkarte Vertrieb: Allg./Werk im Abschnitt Versanddaten (Zeiten in Tagen) folgende Einträge vor:TranspGruppe: 0001Ladegruppe: 0001 |  |  |
| 10 | Verkaufsdaten eingeben | Geben Sie im Abschnitt Allgemeine Werksparameter die folgenden Daten einProfitcenter: <YB700> |  |  |
| Nur für Polen: | Verkaufsdaten eingeben | Geben Sie im Abschnitt International Trade: Export die folgenden Daten ein:Steuerungscode: z.B. 41.00,30,0 | Der PKWiU-Code für Polen ist gepflegt. |  |
| 11 | Daten sichern | Wählen Sie im unteren Bildbereich Sichern. | Ihre Daten werden gesichert. |  |

##### Einkaufsdaten anlegen

Zweck

Dieses Material ist nur für die Cloud Edition relevant.

Voraussetzung

Sie müssen erst die vorherige Vorgehensweisen abschließen, bevor Sie mit diesem Abschnitt fortfahren können.

Vorgehensweise

| Testschrittnummer | Bezeichnung des Testschritts | Anweisung | Erwartetes Ergebnis | Kommentare |
| --- | --- | --- | --- | --- |
| 1 | SAP-Fiori-App aufrufen | Wählen Sie die App-Kachel Material anlegen. | Das Bild Material anlegen (Einstieg) wird geöffnet. |  |
| 2 | Materialgrunddaten eingeben | Nehmen Sie auf dem Bild Material anlegen die folgenden Einträge vor:Material: SRV_05Materialart:Handelswaren (HAWA)Wählen Sie Sichtenauswahl. | Das Bild Sichtenauswahl wird angezeigt. |  |
| 3 | Sichten wählen | Wählen Sie im Fenster Sichtenauswahl die Sicht Einkauf, und wählen Sie Weiter. | Das Bild Organisationsebenen wird angezeigt.. |  |
| 4 | Organisationsebenendaten eingeben | Nehmen Sie auf dem Bild Organisationsebenen im Abschnitt Organisationsebene die folgenden Einträge vor:Werk: 1710Wählen Sie Weiter.Hinweis Im unteren Teil des Bildes wird folgende Meldung angezeigt: Das Material existiert bereits und wird erweitert. | Das Bild Material SRV_05 (Handelsware) anlegen wird geöffnet. |  |
| 5 | Einkaufsdaten eingeben | Nehmen Sie auf dem Bild Material SRV_05 (Handelsware) auf der Registerkarte Einkauf im Abschnitt Allgemeine Daten die folgenden Einträge vor:Einkäufergruppe: 001Warengruppe: L001 |  |  |
| 6 | Einkaufsdaten eingeben | Nehmen Sie im Bereich Sonstige Daten / Herstellerdaten den folgenden Eintrag vor:WE-Bearbeitungszeit z.B. 1 |  |  |
| 7 | Daten sichern | Wählen Sie im unteren Bildbereich Sichern. | Ihre Daten werden gesichert. |  |

##### Dispositions-/Planungsdaten eingeben

Zweck

Dieses Material ist nur für die Cloud Edition relevant.

Voraussetzung

Sie müssen erst die vorherige Vorgehensweisen abschließen, bevor Sie mit diesem Abschnitt fortfahren können.

Vorgehensweise

| Testschrittnummer | Bezeichnung des Testschritts | Anweisung | Erwartetes Ergebnis | Kommentare |
| --- | --- | --- | --- | --- |
| 1 | SAP-Fiori-App aufrufen | Wählen Sie die App Material anlegen. | Das Bild Material anlegen (Einstieg) wird geöffnet. |  |
| 2 | Materialgrunddaten eingeben | Nehmen Sie auf dem Bild Material anlegen die folgenden Einträge vor:Material: SRV_05Materialart: HandelswareWählen Sie Sichtenauswahl. | Das Bild Sichtenauswahl wird angezeigt. |  |
| 3 | Sichten wählen | Wählen Sie im Fenster Sichtenauswahl die Sichten Disposition 1, Disposition 2, Disposition 3 und Disposition 4 aus, und wählen Sie Weiter. | Das Bild Organisationsebenen wird angezeigt.. |  |
| 4 | Organisationsebenendaten eingeben | Nehmen Sie auf dem Bild Organisationsebenen im Abschnitt Organisationsebene die folgenden Einträge vor:Werk: 1710Lagerort: 171AHinweis Im unteren Teil des Bildes wird folgende Information angezeigt: Das Material existiert bereits und wird erweitert. | Das Bild Material SRV_05 (Handelsware) anlegen wird geöffnet. |  |
| 5 | Dispositions-/Planungsdaten eingeben | Nehmen Sie auf dem Bild Material SRV_05 (Handelsware) auf der Registerkarte Disposition 1 im Abschnitt Allgemeine Daten die folgenden Einträge vor:Dispositionsmerkmal: NDDisponent: <001> |  |  |
| 6 | Dispositions-/Planungsdaten eingeben | Nehmen Sie im Bereich Losgrößendaten den folgenden Eintrag vor:Losgrößenverfahren: <EX>Wählen Sie die nächste Registerkarte Disposition 2. | Die nächste Registerkarte Disposition 2 wird geöffnet. |  |
| 7 | Dispositions-/Planungsdaten eingeben | Nehmen Sie auf dem Bild Material SRV_05 (Handelsware) anlegen auf der Registerkarte Disposition 2 im Abschnitt Beschaffung die folgenden Einträge vor:Beschaffungsart: XNehmen Sie im Abschnitt Terminierung die folgenden Einträge vor:Planlieferzeit: z.B. 3WE-Bearbeitungszeit: z.B. 1Horizontschlüssel: z.B. 000Wählen Sie die nächste Registerkarte Disposition 3. | Die nächste Registerkarte Disposition 3 wird geöffnet. |  |
| 8 | Dispositions-/Planungsdaten eingeben | Nehmen Sie auf dem Bild Material SRV_05 (Handelsware) anlegen auf der Registerkarte Disposition 3 im Abschnitt Planung die folgenden Einträge vor:Strategiegruppe: z.B. 40 |  |  |
| 9 | Dispositions-/Planungsdaten eingeben | Nehmen Sie im Bereich Verfügbarkeitsprüfung die folgenden Einträge vor:Verfügbarkeitsprüfung: NCGesWiederbeschZeit : z.B. 3Wählen Sie die nächste Registerkarte Disposition 4. | Die nächste Registerkarte Disposition 4 wird geöffnet. |  |
| 10 | Dispositions-/Planungsdaten eingeben | Nehmen Sie auf dem Bild Material SRV_05 (Handelsware) anlegen auf der Registerkarte Disposition 4 im Abschnitt Stücklistenauflösung/Sekundärbedarfe die folgenden Einträge vor:Einzel/Sammel: <leer> |  |  |
| 11 | Daten sichern | Wählen Sie im unteren Bildbereich Sichern. | Ihre Daten werden gesichert. |  |

##### Lagerortdaten anlegen

Zweck

Dieses Material ist nur für die Cloud Edition relevant.

Voraussetzung

Sie müssen erst die vorherige Vorgehensweisen abschließen, bevor Sie mit diesem Abschnitt fortfahren können.

|  |
| --- |
| Hinweis Zuerst legen Sie eine Sicht für den Lagerort 171A an und anschließend eine Sicht für den Lagerort 171B. |

Vorgehensweise

| Testschrittnummer | Bezeichnung des Testschritts | Anweisung | Erwartetes Ergebnis | Kommentare |
| --- | --- | --- | --- | --- |
| 1 | SAP-Fiori-App aufrufen | Wählen Sie die App-Kachel Material anlegen. | Das Bild Material anlegen (Einstieg) wird geöffnet. |  |
| 2 | Materialgrunddaten eingeben | Nehmen Sie auf dem Bild Material anlegen die folgenden Einträge vor:Material: SRV_05Materialart: HandelswareWählen Sie Sichtenauswahl. | Die Sichtenauswahl wird geöffnet. |  |
| 3 | Sichten wählen | Wählen Sie im Fenster Sichtenauswahl die folgenden Sichten aus:Allg. Werksdaten / Lagerung 1Allg. Werksdaten / Lagerung 2Wählen Sie Weiter. | Das Bild Organisationsebenen wird angezeigt. |  |
| 4 | Organisationsebenendaten eingeben | Nehmen Sie auf dem Bild Organisationsebenen im Abschnitt Organisationsebene die folgenden Einträge vor:Werk: 1710Lagerort: 171AHinweis Im unteren Teil des Bildes wird folgende Information angezeigt: Das Material existiert bereits und wird erweitert. | Das Bild Material SRV_05 (Handelsware) anlegen wird geöffnet. |  |
| 5 | Lagerortdaten eingeben | Nehmen Sie auf dem Bild Material SRV_05 (Handelsware) anlegen auf der Registerkarte Werksdaten/Lagerung 1 im Bereich Allgemeine Daten folgenden Eintrag vor:Anzahl WE-Scheine: z.B. 1 | Die nächste Registerkarte Werksdaten/Lagerung2 wird angezeigt. |  |
| 6 | Lagerortdaten eingeben | Nehmen Sie auf dem Bild Material SRV_05 (Handelsware) anlegen auf der Registerkarte Werksdaten/Lagerung 2 im Bereich Allgemeine Daten folgenden Eintrag vor:Profitcenter: YB700 |  |  |
| 7 | Daten sichern | Wählen Sie im unteren Bildbereich Sichern. | Stammdaten - Produkt wird angezeigt.Ihre Daten werden gesichert. |  |

##### Buchhaltungsdaten anlegen

Zweck

Dieses Material ist nur für die Cloud Edition relevant.

Voraussetzung

Sie müssen erst die vorherige Vorgehensweisen abschließen, bevor Sie mit diesem Abschnitt fortfahren können.

Vorgehensweise

| Testschrittnummer | Bezeichnung des Testschritts | Anweisung | Erwartetes Ergebnis | Kommentare |
| --- | --- | --- | --- | --- |
| 1 | SAP-Fiori-App aufrufen | Wählen Sie die App Material anlegen. | In einem neuen Fenster wird das Bild Material anlegen (Einstieg) angezeigt. |  |
| 2 | Materialgrunddaten eingeben | Nehmen Sie auf dem Bild Material anlegen (Einstieg) die folgenden Einträge vor:Material: SRV_05Materialart: HAWA – HandelswareWählen Sie Sichtenauswahl. | Die Sichtenauswahl wird geöffnet. |  |
| 3 | Sichten wählen | Wählen Sie im Fenster Sichtenauswahl die folgenden Sichten aus:Buchhaltung 1Wählen Sie Weiter. | Das Bild Organisationsebenen wird angezeigt. |  |
| 4 | Organisationsebenendaten eingeben | Nehmen Sie auf dem Bild Organisationsebenen im Abschnitt Organisationsebene die folgenden Einträge vor:Werk: 1710Hinweis Im unteren Teil des Bildes wird folgende Information angezeigt: Das Material existiert bereits und wird erweitert. | Das Bild Material SRV_05 (Handelsware) anlegen wird geöffnet. |  |
| 5 | Buchhaltungsdaten eingeben | Nehmen Sie auf dem Bild Material SRV_05 (Handelsware) anlegen auf der Registerkarte Buchhaltung 1 im Abschnitt Allgemeine Bewertungsdaten die folgenden Einträge vor:Bewertungsklasse: 3100Preisermittlung: 2 (vorgangsbezogen) |  |  |
| 6 | Buchhaltungsdaten eingeben | Nehmen Sie im Bereich Preise und Werte die folgenden Einträge vor:Standardpreis: z.B. 13,50Preissteuerung: S |  |  |
| 7 | Daten sichern | Wählen Sie im unteren Bildbereich Sichern. | Das Fenster Stammdaten - Produkt wird angezeigt.Ihre Daten werden gesichert. |  |

### Preise für Materialien festlegen

#### Preis für SRV_01

Zweck

Dieses Material ist nur für die Cloud Edition relevant.

| Testschrittnummer | Bezeichnung des Testschritts | Anweisung | Erwartetes Ergebnis | Kommentare |
| --- | --- | --- | --- | --- |
| 1 | Anmelden | Melden Sie sich am SAP Fiori Launchpad als Preisfindungssachbearbeiter an. | Das SAP Fiori Launchpad wird geöffnet. |  |
| 2 | SAP-Fiori-App aufrufen | Wählen Sie Materialpreise festlegen - Verkauf. | Die Sicht Konditionssätze ändern wird angezeigt. |  |
| 3 | Preiskonditionsart | Geben Sie in der Sicht Konditionssätze ändern die folgenden Informationen ein:Konditionsart: PPR0Wählen Sie anschließend Enter. | Die Sicht Schlüsselkombination wird angezeigt. |  |
| 4 | Schlüsselkombination | Wählen Sie in der Sicht Schlüsselkombination die Option Material mit Freigabestatus.Wählen Sie anschließend Auswählen (Enter). | Die Sicht Preis ändern (PPR0): Auswahl wird angezeigt. |  |
| 5 | Selektion | Geben Sie in der Sicht Preis ändern (PPR0): Auswahl die folgenden Informationen ein:Verkaufsorg.: 1710 (Inländ. Verkaufsorganisation USA)Vertriebsweg: 10 (Direktverkauf)Material:SRV_01 (Serviceprodukt)Gültig am: <Datum>, z.B. das aktuelle DatumWählen Sie anschließend Ausführen. | Die Sicht Preiskondition ändern (PPR0): Übersicht wird angezeigt. |  |
| 6 | Preiskondition ändern | Geben Sie in der Sicht Preiskondition ändern (PPR0): Übersicht folgende Daten für das Material SRV_01 ein:Material: z.B. SRV_01 (Serviceprodukt)Betrag: z.B. 35,00Einheit: USDGültig ab: <Datum>, z.B. das aktuelle DatumWählen Sie Enter. | Die Preiskonditionen für die Serviceprodukte SRV_01 wurden gepflegt. |  |
| 7 | Sichern | Wählen Sie Sichern. | Die Preise für die Serviceprodukte wurden definiert. |  |

#### Preis für SRV_CONTRACT

Zweck

Dieses Material ist für die Cloud- und die On-Premise-Edition relevant.

Vorgehensweise

| Testschrittnummer | Bezeichnung des Testschritts | Anweisung | Erwartetes Ergebnis | Kommentare |
| --- | --- | --- | --- | --- |
| 1 | Anmelden | Melden Sie sich am SAP Fiori Launchpad als Preisfindungssachbearbeiter an. | Das SAP Fiori Launchpad wird geöffnet. |  |
| 2 | SAP-Fiori-App aufrufen | Wählen Sie Materialpreise festlegen - Verkauf. | Die Sicht Konditionssätze ändern wird angezeigt. |  |
| 3 | Preiskonditionsart | Geben Sie in der Sicht Konditionssätze ändern die folgenden Informationen ein:Konditionsart: PSI1Wählen Sie anschließend Enter. | Die Sicht Schlüsselkombination wird angezeigt. |  |
| 4 | Schlüsselkombination | Wählen Sie in der Sicht Schlüsselkombination die Option Material.Wählen Sie anschließend Enter. | Die Sicht Preis ändern (PSI1): Selektion wird angezeigt. |  |
| 5 | Selektion | Geben Sie in der Sicht Preis ändern (PSI1): Auswahl die folgenden Informationen ein:Verkaufsorg.: 1710 (Inländ. Verkaufsorganisation USA)Vertriebsweg: 10 (Direktverkauf)Material:SRV_CONTRACT (Servicevertragsprodukt)Gültig am: <Datum>, z.B. das aktuelle DatumWählen Sie anschließend Ausführen. | Die Sicht Preiskondition ändern (PPSI): Schnellerfassung wird angezeigt. |  |
| 6 | Preiskondition ändern | Geben Sie in der Sicht Preiskondition ändern (PSI1): Übersicht folgende Daten für das Material SRV_CONTRACT ein:Material: z.B. SRV_CONTRACT (Servicevertragsprodukt)Betrag: z.B. 100,00Einheit: z.B. USDGültig ab: <Datum>, z.B. das aktuelle DatumWählen Sie Enter. | Die Preiskonditionen für das Servicevertragsprodukt SRV_CONTRACT wurden gepflegt. |  |
| 7 | Sichern | Wählen Sie Sichern. | Der Preis für das Servicevertragsprodukt wird gesichert. |  |

#### Preis für SRV_CTR_RENEWAL

Zweck

Dieses Material ist für die Cloud- und die On-Premise-Edition relevant.

Vorgehensweise

| Testschrittnummer | Bezeichnung des Testschritts | Anweisung | Erwartetes Ergebnis | Kommentare |
| --- | --- | --- | --- | --- |
| 1 | Anmelden | Melden Sie sich am SAP Fiori Launchpad als Preisfindungssachbearbeiter an. | Das SAP Fiori Launchpad wird geöffnet. |  |
| 2 | SAP-Fiori-App aufrufen | Wählen Sie Materialpreise festlegen - Verkauf. | Die Sicht Konditionssätze ändern wird angezeigt. |  |
| 3 | Preiskonditionsart | Geben Sie in der Sicht Konditionssätze ändern die folgenden Informationen ein:Konditionsart: PSI1Wählen Sie anschließend Enter. | Die Sicht Schlüsselkombination wird angezeigt. |  |
| 4 | Schlüsselkombination | Wählen Sie in der Sicht Schlüsselkombination die Option Material.Wählen Sie anschließend Enter. | Die Sicht Preis ändern (PSI1): Selektion wird angezeigt. |  |
| 5 | Selektion | Geben Sie in der Sicht Preis ändern (PSI1): Auswahl die folgenden Informationen ein:Verkaufsorg.: 1710 (Inländ. Verkaufsorganisation USA)Vertriebsweg: 10 (Direktverkauf)Material:SRV_CTR_RENEWAL (Servicevertragsverlängerungs-Produkt)Gültig am: <Datum>, z.B. das aktuelle DatumWählen Sie anschließend Ausführen. | Die Sicht Preiskondition ändern (PPSI): Schnellerfassung wird angezeigt. |  |
| 6 | Preiskondition ändern | Geben Sie in der Sicht Preiskondition ändern (PSI1): Übersicht folgende Daten für das Material SRV_CTR_RENEWAL ein:Material: z.B. SRV_CTR_RENEWAL (Servicevertragsverlängerungs-Produkt)Betrag: z.B. 90,00Einheit: z.B. USDGültig ab: <Datum>, z.B. das aktuelle DatumWählen Sie Enter. | Die Preiskonditionen für das Servicevertragsprodukt SRV_CTR_RENEWAL wurden gepflegt. |  |
| 7 | Sichern | Wählen Sie Sichern. | Die Preise für die Servicevertragsprodukte wurden definiert. |  |

#### Preis für SRV_02

Zweck

Dieses Material ist für die Cloud- und die On-Premise-Edition relevant.

Vorgehensweise

| Testschrittnummer | Bezeichnung des Testschritts | Anweisung | Erwartetes Ergebnis | Kommentare |
| --- | --- | --- | --- | --- |
| 1 | Anmelden | Melden Sie sich am SAP Fiori Launchpad als Preisfindungssachbearbeiter an. | Das SAP Fiori Launchpad wird geöffnet. |  |
| 2 | SAP-Fiori-App aufrufen | Wählen Sie Materialpreise festlegen - Verkauf. | Die Sicht Konditionssätze ändern wird angezeigt. |  |
| 3 | Preiskonditionsart | Geben Sie in der Sicht Konditionssätze ändern die folgenden Informationen ein:Konditionsart: PPR0Wählen Sie anschließend Enter. | Die Sicht Schlüsselkombination wird angezeigt. |  |
| 4 | Schlüsselkombination | Wählen Sie in der Sicht Schlüsselkombination die Option Material mit Freigabestatus.Wählen Sie anschließend Enter. | Die Sicht Preis ändern (PPR0): Selektion wird angezeigt. |  |
| 5 | Selektion | Geben Sie in der Sicht Preis ändern (PPR0): Auswahl die folgenden Informationen ein:Verkaufsorg.: 1710 (Inländ. Verkaufsorganisation USA)Vertriebsweg: 10 (Direktverkauf)Material:SRV_02 (Serviceaufwand)Gültig am: <Datum>, z.B. das aktuelle DatumWählen Sie anschließend Ausführen. | Das Bild Preiskondition ändern (PPR0): Übersicht wird angezeigt. |  |
| 6 | Preiskondition ändern | Geben Sie in der Sicht Preiskondition ändern (PPR0): Übersicht folgende Daten für das Material SRV_02 ein:Material: z.B. SRV_02 (Services)Betrag: z.B. 15,00Einheit: z.B. USDGültig ab: <Datum>, z.B. das aktuelle DatumWählen Sie Enter. | Die Preiskondition für das Serviceprodukt SRV_02 wurde gepflegt. |  |
| 7 | Sichern | Wählen Sie Sichern. | Die Preise für die Serviceprodukte wurden definiert. |  |

#### Preis für SRV_04

Zweck

Dieses Material ist nur für die Cloud Edition relevant.

| Testschrittnummer | Bezeichnung des Testschritts | Anweisung | Erwartetes Ergebnis | Kommentare |
| --- | --- | --- | --- | --- |
| 1 | Anmelden | Melden Sie sich am SAP Fiori Launchpad als Preisfindungssachbearbeiter an. | Das SAP Fiori Launchpad wird geöffnet. |  |
| 2 | SAP-Fiori-App aufrufen | Wählen Sie Materialpreise festlegen - Verkauf. | Die Sicht Konditionssätze ändern wird angezeigt. |  |
| 3 | Preiskonditionsart | Geben Sie in der Sicht Konditionssätze ändern die folgenden Informationen ein:Konditionsart: PPR0Wählen Sie anschließend Enter. | Die Sicht Schlüsselkombination wird angezeigt. |  |
| 4 | Schlüsselkombination | Wählen Sie in der Sicht Schlüsselkombination die Option Material mit Freigabestatus.Wählen Sie anschließend Enter. | Die Sicht Preis ändern (PPR0): Selektion wird angezeigt. |  |
| 5 | Selektion | Geben Sie in der Sicht Preis ändern (PPR0): Auswahl die folgenden Informationen ein:Verkaufsorg.: 1710 (Inländ. Verkaufsorganisation USA)Vertriebsweg: 10 (Direktverkauf)Material:SRV_04 (Verwaltete Ersatzteile (Nichtlagermaterial))Gültig am: <Datum>, z.B. das aktuelle DatumWählen Sie anschließend Ausführen. | Das Bild Preiskondition ändern (PPR0): Übersicht wird angezeigt. |  |
| 6 | Preiskondition ändern | Geben Sie in der Sicht Preiskondition ändern (PPR0): Übersicht folgende Daten für das Material SRV_04 ein:Material: SRV_04 (Verwaltete Ersatzteile (Nichtlagermaterial))Betrag: z.B. 15,00Einheit: USDGültig ab: <Datum>, z.B. das aktuelle DatumWählen Sie Enter. | Die Preiskondition für das Serviceprodukt SRV_04 wurde gepflegt. |  |
| 7 | Sichern | Wählen Sie Sichern. | Die Preise für die Serviceprodukte wurden definiert. |  |

#### Preis für SRV_BUNDLE_01

Zweck

Dieses Material ist nur für die Cloud Edition relevant.

| Testschrittnummer | Bezeichnung des Testschritts | Anweisung | Erwartetes Ergebnis | Kommentare |
| --- | --- | --- | --- | --- |
| 1 | Anmelden | Melden Sie sich am SAP Fiori Launchpad als Preisfindungssachbearbeiter an. | Das SAP Fiori Launchpad wird geöffnet. |  |
| 2 | SAP-Fiori-App aufrufen | Wählen Sie Materialpreise festlegen - Verkauf. | Die Sicht Konditionssätze ändern wird angezeigt. |  |
| 3 | Preiskonditionsart | Geben Sie in der Sicht Konditionssätze ändern die folgenden Informationen ein:Konditionsart: PPR0Wählen Sie anschließend Enter. | Die Sicht Schlüsselkombination wird angezeigt. |  |
| 4 | Schlüsselkombination | Wählen Sie in der Sicht Schlüsselkombination die Option Material mit Freigabestatus.Wählen Sie anschließend Enter. | Die Sicht Preis ändern (PPR0): Selektion wird angezeigt. |  |
| 5 | Selektion | Geben Sie in der Sicht Preis ändern (PPR0): Auswahl die folgenden Informationen ein:Verkaufsorg.: 1710 (Inländ. Verkaufsorganisation USA)Vertriebsweg: 10 (Direktverkauf)Material:SRV_BUNDLE_01 (Service Bundle 01)Gültig am: <Datum>, z.B. das aktuelle DatumWählen Sie anschließend Ausführen. | Die Sicht Preiskondition ändern (PPR0): Übersicht wird angezeigt. |  |
| 6 | Preiskondition ändern | Geben Sie in der Sicht Preiskondition ändern (PPR0): Übersicht folgende Daten für das Material SRV_01 ein:Material: SRV_BUNDLE_01 (Service Bundle 01)Betrag: z.B. 200,00Einheit: USDGültig ab: <Datum>, z.B. das aktuelle DatumWählen Sie Enter. | Die Preiskondition für das Serviceprodukt SRV_BUNDLE_01 wurde gepflegt. |  |
| 7 | Sichern | Wählen Sie Sichern. | Die Preise für die Serviceprodukte wurden definiert. |  |

#### Preis für SRV_05

Zweck

Dieser Materialpreis ist nur für die Cloud Edition relevant.

Vorgehensweise

| Testschrittnummer | Bezeichnung des Testschritts | Anweisung | Erwartetes Ergebnis | Kommentare |
| --- | --- | --- | --- | --- |
| 1 | Anmelden | Melden Sie sich am SAP Fiori Launchpad als Preisfindungssachbearbeiter an. | Das SAP Fiori Launchpad wird geöffnet. |  |
| 2 | SAP-Fiori-App aufrufen | Wählen Sie Materialpreise festlegen - Verkauf. | Die Sicht Konditionssätze ändern wird angezeigt. |  |
| 3 | Preiskonditionsart | Geben Sie in der Sicht Konditionssätze ändern die folgenden Informationen ein:Konditionsart: PPR0Wählen Sie anschließend Enter. | Die Sicht Schlüsselkombination wird angezeigt. |  |
| 4 | Schlüsselkombination | Wählen Sie in der Sicht Schlüsselkombination die Option Material mit Freigabestatus.Wählen Sie anschließend Auswählen (Enter). | Die Sicht Preis ändern (PPR0): Auswahl wird angezeigt. |  |
| 5 | Selektion | Geben Sie in der Sicht Preis ändern (PPR0): Auswahl die folgenden Informationen ein:Verkaufsorg.: 1710 (Inländ. Verkaufsorganisation USA)Vertriebsweg: 10 (Direktverkauf)Material: SRV_05 (Lagerersatzteil)Gültig am: <Datum>, z.B. das aktuelle DatumWählen Sie anschließend Ausführen. | Die Sicht Preiskondition ändern (PPR0): Übersicht wird angezeigt. |  |
| 6 | Preiskondition ändern | Geben Sie in der Sicht Preiskondition ändern (PPR0): Übersicht folgende Daten für das Material SRV_01 ein:Material: SRV_05 (Lagerersatzteil)Betrag: z.B. 14,50Einheit: USDGültig ab: <Datum>, z.B. das aktuelle DatumWählen Sie Enter. | Die Preiskonditionen für das Serviceprodukt SRV_01 wurde gepflegt. |  |
| 7 | Sichern | Wählen Sie Sichern. | Die Preise für die Serviceprodukte wurden definiert. |  |

#### Preis für FSM – Aufwand EXP_FSM_MILEAGE

Zweck

Dieses Material ist für die Cloud- und die On-Premise-Edition relevant.

Vorgehensweise

| Testschrittnummer | Bezeichnung des Testschritts | Anweisung | Erwartetes Ergebnis | Kommentare |
| --- | --- | --- | --- | --- |
| 1 | Anmelden | Melden Sie sich am SAP Fiori Launchpad als Preisfindungssachbearbeiter an. | Das SAP Fiori Launchpad wird geöffnet. |  |
| 2 | SAP-Fiori-App aufrufen | Öffnen Sie Materialpreise festlegen - Verkauf. | Die Sicht Konditionssätze ändern wird angezeigt. |  |
| 3 | Preiskonditionsart | Geben Sie in der Sicht Konditionssätze ändern die folgenden Informationen ein:Konditionsart: PCO4Wählen Sie anschließend Enter. | Die Sicht Schlüsselkombination wird angezeigt. |  |
| 4 | Schlüsselkombination | Wählen Sie in der Sicht Schlüsselkombination die Option Material mit Freigabestatus.Wählen Sie anschließend Enter. | Das Bild Preis ändern (PCO4): Auswahl wird angezeigt. |  |
| 5 | Selektion | Geben Sie auf dem Bild Preis ändern (PCO4): Auswahl die folgenden Informationen ein:Verkaufsorg.: 1710 (Inländ. Verkaufsorganisation USA)Vertriebsweg: 10 (Direktverkauf)Material:EXP_FSM_MILEAGEGültig am: <Datum>, z.B. das aktuelle DatumWählen Sie anschließend Ausführen. | Das Bild Preiskondition ändern (PCO4): Übersicht wird angezeigt. |  |
| 6 | Preiskondition ändern | Geben Sie in der Sicht Preiskondition ändern (PCO4): Übersicht folgende Daten für das Material EXP_FSM_MILEAGE ein:Material: z.B. EXP_FSM_MILEAGEBetrag: z.B. 1,50 (Preis pro Einheit)Einheit: z.B. USDGültig ab: <Datum>, z.B. das aktuelle DatumWählen Sie Enter. | Die Preiskondition für das Serviceprodukt EXP_FSM_MILEAGE wurde gepflegt. |  |
| 7 | Sichern | Wählen Sie Sichern. | Die Preise für die Serviceprodukte wurden definiert. |  |

### Preise für Mehrarbeit festlegen

Zweck

Dieses Verfahren beschreibt, wie Preise für Mehrarbeit festgelegt werden. Dieses Kapitel ist nur für 3D2 relevant (Cloud Edition).

|  |
| --- |
| Hinweis Bevor Sie die Preise für Mehrarbeit pflegen, müssen Sie zunächst die "Mehrarbeitstypen" anlegen.Die Beschreibung finden Sie im Testskript 3D2, Kapitel "2.5.6 Mehrarbeitskategorie pflegen". |

Vorgehensweise

| Testschrittnummer | Bezeichnung des Testschritts | Anweisung | Erwartetes Ergebnis | Kommentare |
| --- | --- | --- | --- | --- |
| 1 | Anmelden | Melden Sie sich am SAP Fiori Launchpad als Preisfindungssachbearbeiter an. | Das SAP Fiori Launchpad wird geöffnet. |  |
| 2 | SAP-Fiori-App aufrufen | Wählen Sie Materialpreise festlegen - Verkauf. | Die Sicht Konditionssätze ändern wird angezeigt. |  |
| 3 | Preiskonditionsart | Geben Sie in der Sicht Konditionssätze ändern die folgenden Informationen ein:Konditionsart: SOV1 oder SOV2Wählen Sie anschließend Enter. | Das Bild Mehrarbeit ändern (SOV1): Selektion oder Mehrarbeit ändern (SOV 2): Selektion wird geöffnet.Info:Wurde SOV1 als Konditionssatz gepflegt, können Sie einen Absolutwert als Preis pflegen.Wurde SOV2 als Konditionssatz gepflegt, können Sie einen Prozentwert für die Preisberechnung pflegen. |  |
| 4 | Selektion | Geben Sie in der Sicht Mehrarbeit ändern (SOV1): Selektion oder Mehrarbeit ändern (SOV 2): Selektion die folgenden Informationen ein:Verkaufsorganisation: 1710 (Inländ. Verkaufsorganisation USA)Vertriebsweg: 10 (Direktverkauf)Gültig am: <Datum>, z.B. das aktuelle DatumWählen Sie anschließend Ausführen. | Die Sicht Mehrarbeit ändern (SOV1): Übersicht oder Mehrarbeit ändern (SOV 2): Übersicht wird angezeigt. |  |
| 5 | Preiskondition ändern | Pflegen Sie in der Sicht Mehrarbeit ändern (SOV1): Selektion oder Mehrarbeit ändern (SOV 2): Selektion eine oder mehrere Preiskonditionen für Mehrarbeit:Mehrarbeit: z.B. OV01, OV02, OV03Betrag: z.B. 30 oder 50Einheit: z.B. USD oder %ME: z.B. Std.Gültig ab: <Datum>, z.B. das aktuelle DatumDrücken Sie Enter. |  |  |
| 6 | Sichern | Wählen Sie Sichern. | Es wurden Preiskonditionen für die Mehrarbeitsberechnungen angelegt. |  |

### Konditionssatz für Berechnungsmotiv anlegen

Zweck

In diesem Schritt definieren Sie Konditionssätze für Berechnungsmotive. Diese Kondition kann in Serviceaufträgen verwendet werden, um zu Preisfindungs- und Kontrollzwecken zwischen abrechenbaren, nicht abrechenbaren und teilweise abrechenbaren Positionen zu unterscheiden. Zu den nicht abrechenbaren und teilweise abrechenbaren Services gehören z.B. jene, die im Rahmen einer Garantie oder als Kulanz erbracht werden. Der Konditionssatz für das Berechnungsmotiv ist optional und gilt nur für die Cloud-Edition.

Vorgehensweise (mit SAP Fiori Launchpad)

| Testschrittnummer | Bezeichnung des Testschritts | Anweisung | Erwartetes Ergebnis | Kommentare |
| --- | --- | --- | --- | --- |
| 1 | Anmelden | Melden Sie sich am SAP Fiori Launchpad als Preisfindungssachbearbeiter an. | Das SAP Fiori Launchpad wird geöffnet. |  |
| 2 | SAP-Fiori-App aufrufen | Wählen Sie Materialpreise festlegen - Verkauf. | Die Sicht Konditionssätze ändern wird angezeigt. |  |
| 3 | Preiskonditionsart | Geben Sie in der Sicht Konditionssätze ändern die folgenden Informationen ein:Konditionsart: DAI2Wählen Sie anschließend Enter. | Die Sicht Berechnungsmotiv ändern (DAI2): Selektion wird angezeigt. |  |
| 4 | Auswählen | Geben Sie in der Sicht Berechnungsmotiv ändern (DAI2): Auswahl die folgenden Informationen ein:Verkaufsorg. z.B. 1710 (Inländ. Verkaufsorganisation USA)Vertriebsweg: z.B. 10 (Direktverkauf)Gültig am: <Datum> z.B. das aktuelle DatumWählen Sie anschließend Ausführen. | Die Sicht Berechnungsmotiv ändern (%) Bedingung (DAI2): Übersicht wird angezeigt. |  |
| 5 | Konditionssatz anlegen | Legen Sie in der Sicht Berechnungsmotiv ändern (%) Bedingung (DAI2): Übersicht die folgende Bedingung für SRV_01 an:Verkaufsorganisation: z.B. 1710 (Inländ. Verkaufsorganisation USA)Vertriebsweg: z.B. <10> (Direktverkauf)Material: z.B. <SRV_01>BerMotiv: S1Betrag: z.B. <-100>Rechenregel: AGültig von: <Datum> z.B. das aktuelle DatumGültig bis:<Datum> z.B. das aktuelle Datum.Wählen Sie Enter. | Die Preiskondition wurde gepflegt. |  |
| 6 | Sichern | Wählen Sie Sichern. | Die Konditionssätze für das Berechnungsmotiv des Serviceprodukts werden angelegt. |  |

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
> Flagged while digesting this document, not verified: SRV_06 is listed in the overview table but has no creation procedure in the document

> [!warning] Conflict
> Flagged while digesting this document, not verified: Minor internal inconsistencies: SRV_03 purchasing example material group YBM00 vs YBMM00 in basic data; SRV_BUNDLE_01 and SRV_05 price steps mention material SRV_01 in text; SRV_05 price result text mentions SRV_01

> [!warning] Conflict
> Flagged while digesting this document, not verified: Item group field labelled GenItemGroup in some steps and AllgPosGrp in others

## Connections
- part-of :: [[_cluster]]
- related-to :: [[14-maintenance-service-and-projects/master-data-script-create-service-product-for-service-processes-mds-3k]]
- related-to :: [[14-maintenance-service-and-projects/sap-s-4hana-cloud-public-edition-3kv-349]]
- related-to :: [[14-maintenance-service-and-projects/sap-s-4hana-cloud-public-edition-mds-3kv-351]]
- related-to :: [[14-maintenance-service-and-projects/script-de-dados-mestre-criar-produto-de-servicos-para-operacao-de-serv]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/3KV_S4CLD2608_Master_Data_DE_XX.docx` — full document · extracted with `mammoth` · 73,610 chars in the whole document
