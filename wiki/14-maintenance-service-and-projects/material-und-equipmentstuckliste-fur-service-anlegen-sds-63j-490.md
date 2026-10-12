---
id: 14-maintenance-service-and-projects/material-und-equipmentstuckliste-fur-service-anlegen-sds-63j-490
title: Material- und Equipmentstückliste für Service anlegen – SDS (63J) (63J_S4CLD2608_Master_Data_DE_XX)
description: "German SAP S/4HANA Cloud Public Edition master data script 63J: create service products, material BOM and equipment BOM for service contracts, with test steps."
cluster: 14-maintenance-service-and-projects
tags: [kb/maintenance-service-and-projects, topic/service-technical-objects-and-boms]
aliases: [63J_S4CLD2608_Master_Data_DE_XX]
keywords: [Technical Objects and BOMs for Service, service products, material bill of materials, equipment bill of materials, equipment master data, material master, business roles, organizational units, profit center, service contracts]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/63J_S4CLD2608_Master_Data_DE_XX.docx]
confidence: low
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-490
topic: 14-maintenance-service-and-projects/service-technical-objects-and-boms
language: DE
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Material- und Equipmentstückliste für Service anlegen – SDS (63J) (63J_S4CLD2608_Master_Data_DE_XX)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/63J_S4CLD2608_Master_Data_DE_XX.docx`, extracted with `mammoth`. Grouped under **Technical Objects and BOMs for Service** in Maintenance, Service and Projects. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

| <!-- image omitted: unnamed --> | StammdatenskriptSAP S/4HANA Cloud Public Edition - 02-07-26 |
| --- | --- |
|  | Material- und Equipmentstückliste für Service anlegen – SDS (63J) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Inhaltsverzeichnis

[1 Zweck 2](#_Toc233889844)

[2 Voraussetzungen 3](#_Toc233889845)

[2.1 Systemzugriff 3](#_Toc233889846)

[2.2 Rollen 3](#_Toc233889847)

[2.3 Erforderliche Organisationseinheiten 3](#_Toc233889848)

[2.4 Obligatorische und operative Stammdaten 4](#_Toc233889849)

[3 Übersichtstabelle 5](#_Toc233889850)

[4 Vorgehensweise 6](#_Toc233889851)

[4.1 Materialstückliste anlegen 6](#_Toc233889852)

[4.1.1 Serviceprodukte anlegen 6](#_Toc233889853)

[4.1.1.1 Serviceprodukt anlegen – SRV_BOM_01_01 6](#_Toc233889854)

[4.1.1.2 Serviceprodukt anlegen – SRV_BOM_02_01 7](#_Toc233889855)

[4.1.1.3 Serviceprodukt anlegen – SRV_BOM_02_02 9](#_Toc233889856)

[4.1.2 Neue Stückliste anlegen 10](#_Toc233889857)

[4.2 Equipmentstückliste anlegen 13](#_Toc233889858)

[4.2.1 Equipment anlegen 13](#_Toc233889859)

[4.2.2 Equipmentstückliste anlegen 14](#_Toc233889860)

## Zweck

In diesem Dokument wird beschrieben, wie Sie Serviceprodukt-Stammdatensätze anlegen und die Stückliste mit den angelegten Serviceprodukten erzeugen. Die Beschreibung enthält die Datensegmente, die relevant sind, damit die Stammdaten in einer "normalen" Systemumgebung funktionieren. Sie erfahren in erster Linie, welche Datensegmente und -felder mit Eingabewerten gefüllt werden müssen. Felder, die nicht für den Umfang relevant sind, werden in diesem Dokument nicht behandelt, obwohl sie möglicherweise auf der Benutzungsoberfläche angezeigt werden.

Der wie hier beschrieben angelegte Serviceprodukt-Stammsatz kann für Serviceverträge verwendet werden.

| Produktart | Serviceproduktnummer | Beschreibung |
| --- | --- | --- |
| Materialstamm | SRV_BOM_01_01 | Serviceprodukt mit Stückliste 01_01 |
|  | SRV_BOM_02_01 | Serviceprodukt mit Stückliste 02_01 |
|  | SRV_BOM_02_02 | Serviceprodukt mit Stückliste 02_02 |
| Materialstückliste | SRV_BOM_01_01 | Serviceprodukt mit Stückliste 01_01 |
| Equipment | <Equipment-ID> | Equipment anlegen |
| Equipmentstückliste | <Equipmentstückliste> | Equipmentstückliste |

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
| Stammdatenexperte – Produktdaten | SAP_BR_PRODMASTER_SPECIALIST | Stammdaten - Produkt | SAP_CMD_SP_PR_MAINT |
| Stücklistenbearbeiter | SAP_BR_BOM_ENGINEER | Stücklisten | SAP_BR_BOM_ENGINEER |
| Instandhaltungsplaner | SAP_BR_MAINTENANCE_PLANNER | Instandhaltungsplanung | SAP_BR_MAINTENANCE_PLANNER |

### Erforderliche Organisationseinheiten

Einige Segmente von Stammdaten hängen von den Organisationseinheiten des Unternehmens ab. Allgemeine (zentrale) Daten hängen nicht von einer Organisationseinheit oder dem Buchungskreis ab. Die folgende Tabelle stellt eine Übersicht dieser verschiedenen Datensegmente und ihrer relevanten Organisationseinheiten bereit:

| Datensegment | Hängt ab von | Für die USA zu verwendende Organisationseinheit | Für DE zu verwendende Organisationseinheit |
| --- | --- | --- | --- |
| Material anlegen | Verkaufsorganisation | 1710 (Inländ. Verkaufsorganisation USA) | 1010 (Inländ. Verkaufsorganisation DE) |
| Material anlegen | Vertriebsweg | 10 (Direktverkauf) | 10 (Direktverkauf) |

### Obligatorische und operative Stammdaten

Materialstammdatensätze können auf andere Stammdaten verweisen. Die folgende Tabelle bietet eine Übersicht über die optionalen und obligatorischen Stammdatenobjekte, die in einem Materialstammdatensatz verwendet werden müssen.

|  |
| --- |
| Hinweis Für eine ordnungsgemäße Steuerberechnung sind brasilienspezifische Felder erforderlich.Prüfen Sie Nota Fiscal – Brasilien - JD0 im Kapitel BR-spezifische Felder für Stammdaten definieren für Materialstammdaten. |

| Stammdatenobjekt | Verwendet im Datensegment | Obligatorisch / optional | Kommentare |
| --- | --- | --- | --- |
| Profitcenter |  | obligatorisch | Für einwandfreie Bewertungsprozesse ist die Zuweisung eines Profitcenters zu einem Material- oder Produktstamm erforderlich. |

## Übersichtstabelle

Dieser Stammdatensatz umfasst mehrere Segmente, die in der nachfolgenden Tabelle genannt sind.

Wenn Ihr Systemadministrator Bereiche und Seiten auf dem SAP Fiori Launchpad aktiviert hat, enthält die Startseite nur die wesentlichen Apps, mit denen die typischen Aufgaben einer Benutzerrolle ausgeführt werden können.

Alle anderen Apps, die nicht auf der Startseite enthalten sind, finden Sie über die Suchleiste.

Wenn Sie die Startseite personalisieren und versteckte Apps hinzufügen möchten, wechseln Sie in Ihr Benutzerprofil und wählen Sie Einstellungen > App Finder.

| ID (Rollenvorlage) | Anwendungsrolle | App/Transaktion | Erwartete Ergebnisse |
| --- | --- | --- | --- |
| Materialstückliste anlegen | SAP_BR_PRODMASTER_SPECIALIST | Material anlegen (MM01) | Serviceprodukte werden angelegt. |
| SAP_BR_BOM_ENGINEER | Stückliste pflegen - Stücklisten anlegen, ändern und anzeigen | Die Materialstückliste wird angelegt. |  |
| Equipmentstückliste anlegen | SAP_BR_MAINTENANCE_PLANNER | Technisches Objekt anlegen | Das Equipment wird angelegt. |
| Equipmentstückliste anlegen | Die Equipmentstückliste wird angelegt. |  |  |

## Vorgehensweise

Dieser Abschnitt beschreibt die Vorgehensweisen für jedes Segment oder jeden Prozessschritt, das bzw. der Teil dieses Stammsatzes ist.

### Materialstückliste anlegen

#### Serviceprodukte anlegen

##### Serviceprodukt anlegen – SRV_BOM_01_01

Zweck

Dieses Material ist nur für die Cloud Edition relevant.

| Testschrittnummer | Bezeichnung des Testschritts | Anweisung | Erwartetes Ergebnis | Kommentare |
| --- | --- | --- | --- | --- |
| 1 | Anmelden | Melden Sie sich am SAP Fiori Launchpad als Stammdatenexperte – Produktdaten (MDG). | Die Startseite wird angezeigt. |  |
| 2 | SAP-Fiori-App aufrufen | Wählen Sie die Kachel Material anlegen aus. | Das Bild Material anlegen (Einstieg) wird angezeigt. |  |
| 3 | Materialgrunddaten (für Serviceprodukt) pflegen | Nehmen Sie auf dem Bild Material anlegen (Einstieg) folgende Einträge vor: Wählen Sie im Dialogfenster Folgendes:Material: SRV_BOM_01_01Materialart: ServiceproduktWählen Sie anschließend Weiter (Enter). | Sie haben die grundlegenden Informationen für das neue Serviceprodukt erfasst.Das Dialogfenster Sichtenauswahl wird angezeigt. |  |
| 4 | Sichten wählen | Wählen Sie im Dialogfenster Sichtenauswahl die folgenden Sichten aus:Grunddaten 1Verkauf: VerkaufsorgDaten 1Verkauf: VerkaufsorgDaten 2Wählen Sie anschließend Weiter (Enter). | Das Dialogfenster Organisationsebenen wird angezeigt. |  |
| 5 | Organisationsebenen wählen | Geben Sie im Dialogfenster Organisationsebenen die folgenden Werte ein:Verkaufsorganisation: 1710 (Inländ. Verkaufsorganisation USA)Vertriebsweg: 10 (Direktverkauf)Wählen Sie anschließend Weiter (Enter). | Es wurden Organisationsdaten ausgewählt.Die Sicht Material SRV_BOM_01_01 anlegen wird angezeigt. |  |
| 6 | Grunddaten pflegen | Pflegen Sie in der Sicht Grunddaten 1 die folgenden Werte:Beschreibung: Serviceprodukt mit Stückliste 01_01Basismengeneinheit: Std. (Stunden)Materialgruppe: P001 (Services)Allg. PosTypGrp: SRVP (Serviceprodukt)Wählen Sie anschließend Sichern. | Die Grunddaten sind gepflegt, und das Serviceprodukt ist gesichert.Nach dem Sichern wird die Sicht Material anlegen (Einstieg) angezeigt.Wenn Sie verschiedene Sprachen in Ihrem Unternehmen verwenden, müssen Sie für jeden relevanten Sprachencode die entsprechende Beschreibung für das Produkt pflegen. |  |
| 7 | Verkaufsorganisationsdaten (1) pflegen | Geben Sie in der Sicht Verkauf: VerkOrg 1 die folgenden Werte ein:Allgemeine DatenSkonto: X <markiert>SteuerdatenSteuerklassifikation: 1 (volle Steuer)Wählen Sie anschließend Enter. | Die Verkaufsorganisationsdaten sind gepflegt. Die Registerkarte Verkauf: VerkOrg 2 wird angezeigt. |  |
| 8 | Verkaufsorganisationsdaten (2) pflegen | Geben Sie in der Sicht Verkauf: VerkOrg 2 die folgenden Daten ein:Positionstypengruppe: SRVP (Serviceprodukt)Wählen Sie anschließend Sichern. | Die Verkaufsorganisationsdaten sind gepflegt. Die Registerkarte Verkauf: Allg./Werk wird angezeigt. |  |

##### Serviceprodukt anlegen – SRV_BOM_02_01

Zweck

Dieses Material ist nur für die Cloud Edition relevant.

| Testschrittnummer | Bezeichnung des Testschritts | Anweisung | Erwartetes Ergebnis | Kommentare |
| --- | --- | --- | --- | --- |
| 1 | Anmelden | Melden Sie sich am SAP Fiori Launchpad als Stammdatenexperte – Produktdaten (MDG). | Die Startseite wird angezeigt. |  |
| 2 | SAP-Fiori-App aufrufen | Wählen Sie die Kachel Material anlegen aus. | Das Bild Material anlegen (Einstieg) wird angezeigt. |  |
| 3 | Materialgrunddaten (für Serviceprodukt) pflegen | Nehmen Sie auf dem Bild Material anlegen (Einstieg) folgende Einträge vor: Wählen Sie im Dialogfenster Folgendes:Material: SRV_BOM_02_01Materialart: ServiceproduktWählen Sie anschließend Weiter (Enter). | Sie haben die grundlegenden Informationen für das neue Serviceprodukt erfasst.Das Dialogfenster Sichtenauswahl wird angezeigt. |  |
| 4 | Sichten wählen | Wählen Sie im Dialogfenster Sichtenauswahl die folgenden Sichten aus:Grunddaten 1Verkauf: VerkaufsorgDaten 1Verkauf: VerkaufsorgDaten 2Wählen Sie anschließend Weiter (Enter). | Das Dialogfenster Organisationsebenen wird angezeigt. |  |
| 5 | Organisationsebenen wählen | Geben Sie im Dialogfenster Organisationsebenen die folgenden Werte ein:Verkaufsorganisation: 1710 (Inländ. Verkaufsorganisation USA)Vertriebsweg: 10 (Direktverkauf)Wählen Sie anschließend Weiter (Enter). | Es wurden Organisationsdaten ausgewählt.Die Sicht Material SRV_BOM_ 02_01 anlegen wird angezeigt. |  |
| 6 | Grunddaten pflegen | Pflegen Sie in der Sicht Grunddaten 1 die folgenden Werte:Beschreibung: Serviceprodukt mit Stückliste 02_01Basismengeneinheit: Std. (Stunden)Materialgruppe: P001 (Services)Allg. PosTypGrp: SRVP (Serviceprodukt)Wählen Sie anschließend Enter. | Die Grunddaten sind gepflegt, und das Serviceprodukt ist gesichert.Nach dem Sichern wird die Sicht Material anlegen (Einstieg) angezeigt.Wenn Sie verschiedene Sprachen in Ihrem Unternehmen verwenden, müssen Sie für jeden relevanten Sprachencode die entsprechende Beschreibung für das Produkt pflegen. |  |
| 7 | Verkaufsorganisationsdaten (1) pflegen | Geben Sie in der Sicht Verkauf: VerkOrg 1 die folgenden Werte ein:Allgemeine DatenSkonto: X <markiert>SteuerdatenSteuerklassifikation: 1 (volle Steuer)Wählen Sie anschließend Enter. | Die Verkaufsorganisationsdaten sind gepflegt. Die Registerkarte Verkauf: VerkOrg 2 wird angezeigt. |  |
| 8 | Verkaufsorganisationsdaten (2) pflegen | Geben Sie in der Sicht Verkauf: VerkOrg 2 die folgenden Daten ein:Positionstypengruppe: SRVP (Serviceprodukt)Wählen Sie anschließend Sichern. | Die Verkaufsorganisationsdaten sind gepflegt. Die Registerkarte Verkauf: Allg./Werk wird angezeigt. |  |

##### Serviceprodukt anlegen – SRV_BOM_02_02

Zweck

Dieses Material ist nur für die Cloud Edition relevant.

| Testschrittnummer | Bezeichnung des Testschritts | Anweisung | Erwartetes Ergebnis | Kommentare |
| --- | --- | --- | --- | --- |
| 1 | Anmelden | Melden Sie sich am SAP Fiori Launchpad als Stammdatenexperte – Produktdaten (MDG). | Die Startseite wird angezeigt. |  |
| 2 | SAP-Fiori-App aufrufen | Wählen Sie die Kachel Material anlegen aus. | Das Bild Material anlegen (Einstieg) wird angezeigt. |  |
| 3 | Materialgrunddaten (für Serviceprodukt) pflegen | Nehmen Sie auf dem Bild Material anlegen (Einstieg) folgende Einträge vor: Wählen Sie im Dialogfenster Folgendes:Material: SRV_BOM_02_02Materialart: ServiceproduktWählen Sie anschließend Weiter (Enter). | Sie haben die grundlegenden Informationen für das neue Serviceprodukt erfasst.Das Dialogfenster Sichtenauswahl wird angezeigt. |  |
| 4 | Sichten wählen | Wählen Sie im Dialogfenster Sichtenauswahl die folgenden Sichten aus:Grunddaten 1Verkauf: VerkaufsorgDaten 1Verkauf: VerkaufsorgDaten 2Wählen Sie anschließend Weiter (Enter). | Das Dialogfenster Organisationsebenen wird angezeigt. |  |
| 5 | Organisationsebenen wählen | Geben Sie im Dialogfenster Organisationsebenen die folgenden Werte ein:Verkaufsorganisation: 1710 (Inländ. Verkaufsorganisation USA)Vertriebsweg: 10 (Direktverkauf)Wählen Sie anschließend Weiter (Enter). | Es wurden Organisationsdaten ausgewählt.Die Sicht Material SRV_BUNDLE_02 anlegen wird angezeigt. |  |
| 6 | Grunddaten pflegen | Pflegen Sie in der Sicht Grunddaten 1 die folgenden Werte:Beschreibung: Serviceprodukt mit Stückliste 02_02Basismengeneinheit: Std. (Stunden)Materialgruppe: P001 (Services)Allg. PosTypGrp: SRVP (Serviceprodukt)Wählen Sie anschließend Enter. | Die Grunddaten sind gepflegt, und das Serviceprodukt ist gesichert.Nach dem Sichern wird die Sicht Material anlegen (Einstieg) angezeigt.Wenn Sie verschiedene Sprachen in Ihrem Unternehmen verwenden, müssen Sie für jeden relevanten Sprachencode die entsprechende Beschreibung für das Produkt pflegen. |  |
| 7 | Verkaufsorganisationsdaten (1) pflegen | Geben Sie in der Sicht Verkauf: VerkOrg 1 die folgenden Werte ein:Allgemeine DatenSkonto: X <markiert>SteuerdatenSteuerklassifikation: 1 (volle Steuer)Wählen Sie anschließend Enter. | Die Verkaufsorganisationsdaten sind gepflegt. Die Registerkarte Verkauf: VerkOrg 2 wird angezeigt. |  |
| 8 | Verkaufsorganisationsdaten (2) pflegen | Geben Sie in der Sicht Verkauf: VerkOrg 2 die folgenden Daten ein:Positionstypengruppe: SRVP (Projekt)Wählen Sie anschließend Sichern. | Die Verkaufsorganisationsdaten sind gepflegt. Die Registerkarte Verkauf: Allg./Werk wird angezeigt. |  |

#### Neue Stückliste anlegen

Zweck

Dieses Material ist nur für die Cloud Edition relevant. In diesem Schritt können Sie eine neue Stückliste anlegen.

| Testschrittnummer | Bezeichnung des Testschritts | Anweisung | Erwartetes Ergebnis | Kommentare |
| --- | --- | --- | --- | --- |
| 1 | Anmelden | Melden Sie sich am SAP Fiori Launchpad als Stücklistenbearbeiter. | Das SAP Fiori Launchpad wird angezeigt. |  |
| 2 | SAP-Fiori-App aufrufen | Öffnen Sie die App Stückliste pflegen (Version 2) – Stücklisten anlegen, ändern und anzeigen(F1813A). |  |  |
| 3 | "Stückliste anlegen" wählen | Wählen Sie im Bild Stückliste pflegen die Option Stückliste anlegen. | Das Dialogfenster Stückliste anlegen wird angezeigt. |  |
| 4 | Stücklisten-Kopfdaten bearbeiten | Geben Sie im Fenster Stückliste anlegen die folgenden Daten ein, und wählen Sie OK:BeispielMaterial: SRV_BOM_01_01Stücklistenverwendung: S (Servicemanagement)Gültig ab: Heute | Das Bild Stückliste pflegen wird angezeigt, und standardmäßig wird die Registerkarte Komponenten geöffnet. |  |
| 5 | Stücklisten-Komponentendaten bearbeiten | Geben Sie in der Zeile mit der Stücklistenpositionsnummer 0010 die folgenden Daten (oder ähnliche Daten) ein:BeispielKomponente: SRV_BOM_02_01Komponentenmenge:10 Std.Wählen Sie "Enter", um die Felder "Komponente" und "Komponentenmenge" zu aktivieren.Hinweis Der Wert des Positionstyps ist N (Nichtlagerposition). | Die Nummer der Stücklistenposition 0010, Komponente, Komponentenbeschreibung und Komponentenmenge werden in der ersten Tabellenzeile angezeigt. |  |
| 6 | Zusätzliche Stücklisten-Komponentendaten bearbeiten | Wiederholen Sie den beschriebenen Schritt mit folgenden Daten für die Stücklistenpositionsnummer 0020:Komponente: SRV_BOM_02_02Komponentenmenge: 20 Std.Wählen Sie "Enter", um die Felder "Komponente" und "Komponentenmenge" zu aktivieren.Hinweis Der Wert des Positionstyps ist N (Nichtlagerposition). | Die Nummer der Stücklistenposition 0020, Komponente, Komponentenbeschreibung und Komponentenmenge werden in den Tabellenzeilen angezeigt. |  |
| 8 | Zu Positionsdetails navigieren | Klicken Sie auf den Detailpfeil ganz rechts in der Tabelle in der Zeile Nummer der Stücklistenposition 0010.Nehmen Sie im Bild Stückliste pflegen ähnliche Einträge wie im folgenden Beispiel in der Registerkarte Grunddaten vor:BeispielKomponentenmenge: 10KompMengenEinheit: Std. | Das Bild Stückliste pflegen wird mit dem Detailabschnitt für die eingegebene Position angezeigt. |  |
| 9 | Zu Positionsdetails navigieren | Klicken Sie auf den Detailpfeil ganz rechts in der Tabelle in der Zeile Nummer der Stücklistenposition 0020.Nehmen Sie im Bild Stückliste pflegen ähnliche Einträge wie im folgenden Beispiel in der Registerkarte Grunddaten vor:BeispielKomponentenmenge: 20KompMengenEinheit: Std. | Das Bild Stückliste pflegen wird mit dem Detailabschnitt für die eingegebene Position angezeigt. |  |
| 10 | "Sichern" wählen | Wählen Sie im Bild Stückliste pflegen die Option Anlegen. | Die Stückliste wird gesichert.Hinweis Nach dem Sichern wird der Stücklistenstatus automatisch auf 1 (Aktiv) gesetzt.Wenn für die Stückliste der Stücklistenstatus 2 (Inaktiv) auf dem Bild "Stückliste pflegen" erforderlich ist, wählen Sie "Kopfdetails einblenden" und dann "Verwaltungsdaten", und setzen Sie den entsprechenden Stücklistenstatus, bevor Sie erneut "Sichern" wählen.Die Änderungsnummer wird unter der Registerkarte "Zeitleiste" hinzugefügt. |  |

### Equipmentstückliste anlegen

#### Equipment anlegen

Zweck

In diesem Testschritt pflegen Sie einen Datensatz für ein Equipment, das auf einem Technischen Platz eingebaut ist.

| Testschrittnummer | Bezeichnung des Testschritts | Anweisung | Erwartetes Ergebnis | Kommentare |
| --- | --- | --- | --- | --- |
| 1 | Anmelden | Melden Sie sich am SAP Fiori Launchpad als Instandhaltungsplaner an. | Das SAP Fiori Launchpad wird angezeigt. |  |
| 3 | SAP-Fiori-App aufrufen | Öffnen Sie Technisches Objekt anlegen. | In einem neuen Fenster wird das Bild Technisches Objekt anlegen: Einstieg geöffnet. |  |
| 4 | Equipment anlegen | Wählen Sie auf dem Bild Technisches Objekt anlegen die Option "Art des technischen Objekts: Equipment".Geben Sie im nächsten Bild folgende Daten ein:Art des technischen Objekts: EquipmentTechnisches Objekt: leer lassenGültig ab: aktuelles DatumTyp des technischen Objekts: M (Maschinen)Wählen Sie Weiter (Enter). |  |  |
| 5 | Allgemeine Daten bearbeiten | Geben Sie auf dem Bild Technisches Objekt anlegen: <Equipment-ID> im Abschnitt Allgemeine Daten folgende Daten ein:Beschreibung: z.B. Equipment des Stücklistenkopfs für ServiceObjekttyp: z.B. 9400Inbetriebnahmedatum: z.B. das aktuelle DatumHerstellungsland/-region: z.B. USBaumonat/-jahr: z.B. 04/2011Herstellerteilenummer: z.B. HZZ-TD B4Herstellerserialnummer: z.B. HZZ-TD B4/66Anschaffungswert/-währung: z.B. 10.000,00 / USDAnschaffungsdatum: z.B. 10.04.2011Hinweis Optional können Sie weitere allgemeine Daten pflegen. Navigieren Sie dann zum Abschnitt "Standortdaten". | Das Bild Technisches Objekt anlegen: Allgemeine Daten wird angezeigt. |  |
| 6 | Standortdaten pflegen | Nehmen Sie im Abschnitt Standortdaten die folgenden Einträge vor:Standortwerk: z.B. 1710 für USStandort: z.B. YB_1701 für USBetriebsbereich: z.B. YOH für USHinweis Allen technischen Objekten, die zu einer Struktur gehören, muss dasselbe Werk zugeordnet sein. Alternativ können Sie die Felder für Angaben zum Werk für alle technischen Objekte leer lassen.Optional können Sie weitere Details wie die Adresse pflegen. | Das Bild Technisches Objekt anlegen: Standortdaten wird angezeigt. |  |
| 8 | Organisationsdaten bearbeiten | Nehmen Sie im Abschnitt Organisationsdaten die folgenden Einträge vor:Planergruppe: z.B. 920 für USPlanungswerk: z.B. 1710 für USInstandhaltungsarbeitsplatz: z.B. RES-0100 für USWerk zum Arbeitsplatz: z.B. 1710 für USKostenstelle: z.B. 17101701 für USOptional können Sie im Abschnitt "Organisationsdaten" zusätzliche Informationen wie Partnerinformationen pflegen. | Das Bild Technisches Objekt anlegen: Organisationsdaten wird angezeigt. |  |
| 9 | Equipment sichern | Optional können Sie zusätzliche Informationen für andere Abschnitte pflegen.Wählen Sie Einträge prüfen.Wählen Sie Sichern. | Ein Equipment wird angelegt.Notieren Sie die angelegte Equipment-ID. |  |

#### Equipmentstückliste anlegen

| Testschrittnummer | Bezeichnung des Testschritts | Anweisung | Erwartetes Ergebnis | Kommentare |
| --- | --- | --- | --- | --- |
| 1 | Anmelden | Melden Sie sich am SAP Fiori Launchpad als Instandhaltungsplaner an. | Das SAP Fiori Launchpad wird angezeigt. |  |
| 2 | SAP-Fiori-App aufrufen | Öffnen Sie Equipmentstückliste anlegen. | Ein neues Fenster mit dem Bild Stückliste anlegen: Einstieg wird geöffnet. |  |
| 3 | Equipment anlegen | Geben Sie auf dem Bild Equipmentstückliste anlegen: Einstieg die folgenden Daten ein:Equipment: im vorherigen Kapitel generierte Equipment-IDStücklistenverwendung: SWählen Sie Weiter. |  |  |
| 4 | Materialdaten pflegen | Geben Sie auf dem Bild Equipmentstückliste anlegen: Positionsübersicht Allgemein im Abschnitt Material folgende Daten ein:Komponente: Material-ID, z.B. SRV_BOM_02_02Positionstyp: N (Nichtlagerposition)Menge: z.B. 10Mengeneinheit: z.B. Std.Wählen Sie Enter. | Das Bild Equipmentstückliste anlegen: Positionsübersicht Allgemein wird angezeigt. |  |
| 5 | Equipment sichern | Wählen Sie Sichern. | Die Equipmentstückliste wird angelegt. |  |

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
> Flagged while digesting this document, not verified: SRV_BOM_02_02 step 8 sets item category group SRVP as '(Projekt)' whereas the other service products label SRVP '(Serviceprodukt)'; step 5 refers to material SRV_BUNDLE_02 instead of SRV_BOM_02_02

## Connections
- part-of :: [[_cluster]]
- related-to :: [[14-maintenance-service-and-projects/bom-mds-63j-493]]
- related-to :: [[14-maintenance-service-and-projects/master-data-script-create-material-and-equipment-bom-for-service-mds-6]]
- related-to :: [[14-maintenance-service-and-projects/mds-63j-495]]
- related-to :: [[14-maintenance-service-and-projects/script-de-dados-mestre-criar-lista-tecnica-de-material-e-equipamento-p]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/63J_S4CLD2608_Master_Data_DE_XX.docx` — full document · extracted with `mammoth` · 24,741 chars in the whole document
