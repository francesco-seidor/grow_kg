---
id: 06-management-accounting/stammdatenskript-materialstamm-fur-universelle-erlosrealisierung-anleg
title: "Stammdatenskript: Materialstamm für universelle Erlösrealisierung anlegen (7R8) (7R8_S4CLD2608_Master_Data_DE_XX)"
description: "German SAP S/4HANA Cloud Public Edition 2608 master data script (7R8): create UER test materials and sales prices for stock sales, fixed-price project and service contract."
cluster: 06-management-accounting
tags: [kb/management-accounting, topic/event-based-revenue-recognition-sell-from-stock]
aliases: [7R8_S4CLD2608_Master_Data_DE_XX]
keywords: [Event-Based Revenue Recognition for Sell from Stock, material master, universal revenue recognition, trading goods material, service product material, fixed-price project material, service contract material, material pricing, condition records, user roles]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/7R8_S4CLD2608_Master_Data_DE_XX.docx]
confidence: low
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-532
topic: 06-management-accounting/event-based-revenue-recognition-sell-from-stock
language: DE
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Stammdatenskript: Materialstamm für universelle Erlösrealisierung anlegen (7R8) (7R8_S4CLD2608_Master_Data_DE_XX)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/7R8_S4CLD2608_Master_Data_DE_XX.docx`, extracted with `mammoth`. Grouped under **Event-Based Revenue Recognition for Sell from Stock** in Management Accounting. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

| <!-- image omitted: unnamed --> | StammdatenskriptSAP S/4HANA Cloud Public Edition - 02-07-26 |
| --- | --- |
|  | Materialstamm für universelle Erlösrealisierung anlegen (7R8) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Inhaltsverzeichnis

[1 Zweck 2](#_Toc233889881)

[2 Voraussetzungen 3](#_Toc233889882)

[2.1 Systemzugriff 3](#_Toc233889883)

[2.2 Rollen 3](#_Toc233889884)

[2.3 Erforderliche Organisationseinheiten 3](#_Toc233889885)

[3 Übersichtstabelle 5](#_Toc233889886)

[4 Materialstammdaten für Integrationsszenario für den Verkauf ab Lager (SFS) anlegen 6](#_Toc233889887)

[4.1 Handelswaren: URR_MAT1_NORM 6](#_Toc233889888)

[4.2 Serviceprodukt für einmaligen Service: URR_MAT1_SERV 9](#_Toc233889889)

[5 Materialstammdaten für Integrationsszenario für Festpreiskundenprojekt anlegen 11](#_Toc233889890)

[5.1 URR_FPPRJ_1 11](#_Toc233889891)

[6 Materialstammdaten für Integrationsszenario für Servicevertrag anlegen 14](#_Toc233889892)

[6.1 URR_SRVCONT1 14](#_Toc233889893)

[7 Preise für Materialien festlegen 16](#_Toc233889894)

[7.1 Preis für Handelsware für SFS: URR_MAT1_NORM 16](#_Toc233889895)

[7.2 Preis für Serviceprodukt für einmaligen Service: URR_MAT1_SERV 18](#_Toc233889896)

[7.3 Preis für Servicevertragsmaterial: URR_SRVCONT1 20](#_Toc233889897)

## Zweck

Dieses Dokument enthält einen Leitfaden zum Anlegen von Materialstammdatensätzen einschließlich Preisen für verschiedene Integrationsszenarios für die universellen Erlösrealisierung (UER): UER integriert mit Verkauf ab Lager, UER integriert mit Kundenserviceprojekten und UER integriert mit Servicevertrag.

Der Leitfaden enthält die Beschreibung von Datensegmenten, die für die Stammdaten relevant sind, um in einem UER-Prozess zu arbeiten, und Felder, die mit Eingabewerten in den Datensegmenten gefüllt werden müssen. Datensegmente und Felder, die nicht für den Umfang relevant sind, werden in diesem Dokument nicht behandelt, obwohl sie möglicherweise auf der Benutzungsoberfläche angezeigt werden.

Materialstammdaten, die gemäß dieser Beschreibung angelegte werden, können für die UER-Prozesse verwendet werden:

| Materialstamm-ID | Beschreibung | Verwendung |
| --- | --- | --- |
| URR_MAT1_NORM | UER-Testmaterial 1 NORM | Dieses Material wird im Integrationsszenario für den UER-Verkauf ab Lager verwendet. |
| URR_MAT2_NORM | UER-Testmaterial 2 NORM | Dieses Material wird im Integrationsszenario für den UER-Verkauf ab Lager verwendet. |
| URR_MAT1_SERV | UER-Testmaterial1 TAD | Dieses Material wird im Integrationsszenario für den UER-Verkauf ab Lager verwendet. |
| URR_FPPRJ_1 | UER-Testmaterial Festpreis Kundenprojekt | Dieses Material wird im Integrationsszenario für UER-Kundenprojekte verwendet. |
| URR_SRVCONT1 | UER-Testmaterial Servicevertrag | Dieses Material wird im Integrationsszenario für UER-Serviceverträge verwendet. |

## Voraussetzungen

### Systemzugriff

| System | Details |
| --- | --- |
| System | Erreichbar über SAP Fiori Launchpad. Ihr Systemadministrator stellt Ihnen die URL für den Zugriff auf die verschiedenen Apps zur Verfügung, die Ihrer Rolle zugeordnet sind. |

### Rollen

Legen Sie Benutzerrollen mit den folgenden von SAP ausgelieferten Benutzerrollenvorlagen an, und ordnen Sie sie Ihren einzelnen Testbenutzern zu.

Alternativ können Sie, falls verfügbar, die folgenden von SAP ausgelieferten Bereiche verwenden. Legen Sie einen Bereich mit Seiten an, die vordefinierte grundlegende Apps enthalten, und ordnen Sie sie der Benutzerrolle zu. Anschließend ordnen Sie diese Benutzerrolle Ihren einzelnen Benutzern zu.

Weitere Informationen finden Sie unter Anwendungsrolle aus einer Vorlage anlegen in der [Product Assistance](https://help.sap.com/docs/SAP_S4HANA_CLOUD/53e36b5493804bcdb3f6f14de8b487dd/ec310a8b669a45ca898dc4dd91d97de2.html) für SAP S/4HANA Cloud Public Edition.

| Name (Rollenvorlage) | ID (Rollenvorlage) | Name (Launchpad-Bereich) | ID (Launchpad-Bereich) | Anmelden |
| --- | --- | --- | --- | --- |
| Stammdatenexperte – Produktdaten | SAP_BR_PRODMASTER_SPECIALIST | Stammdaten – Produkte / Produkt-Governance | SAP_BR_PRODMASTER_SPECIALIST / SAP_CMD_SPT_PR_GOV_PC |  |
| Preisfindungssachbearbeiter | SAP_BR_PRICING_SPECIALIST | Preisverwaltung | SAP_BR_PRICING_SPECIALIST |  |

### Erforderliche Organisationseinheiten

Einige Segmente von Stammdaten hängen von den Organisationseinheiten des Unternehmens ab. Allgemeine (zentrale) Daten hängen nicht von einer Organisationseinheit oder dem Buchungskreis ab. Die folgende Tabelle stellt eine Übersicht dieser verschiedenen Datensegmente und ihrer relevanten Organisationseinheiten bereit:

| Datensegment | Hängt ab von | Für DE zu verwendende Organisationseinheit | Für die USA zu verwendende Organisationseinheit |
| --- | --- | --- | --- |
| Material anlegen | Werk | 1010 (Werk 1 DE) | 1710 (Werk 1 USA) |
| Material anlegen | Verkaufsorganisation | 1010 (Inländ. Verkaufsorganisation DE) | 1710 (Inländ. Verkaufsorganisation USA) |
| Material anlegen | Vertriebsweg | 10 (Direktverkauf) | 10 (Direktverkauf) |

## Übersichtstabelle

Dieser Stammdatensatz umfasst mehrere Segmente, die in der nachfolgenden Tabelle genannt sind.

|  |
| --- |
| Hinweis Wenn Ihr Systemadministrator Bereiche und Seiten auf dem SAP Fiori Launchpad aktiviert hat, enthält die Startseite nur die wesentlichen Apps, mit denen die typischen Aufgaben einer Benutzerrolle ausgeführt werden können.Alle anderen (suchbaren) Apps, die nicht auf der Startseite enthalten sind, finden Sie über die Suchleiste ([2434549](https://me.sap.com/notes/2434549)).Wenn Sie die Startseite personalisieren und versteckte Apps hinzufügen möchten, wechseln Sie in Ihr Benutzerprofil und wählen Sie App Finder. |

Tabelle 1: Materialstammdaten für Integrationsszenario für den Verkauf ab Lager (SFS) anlegen

| Prozessschritt | Anwendungsrolle | App/Transaktion | Erwartete Ergebnisse |
| --- | --- | --- | --- |
| [Handelswaren: URR_MAT1_NORM](#unique_6) [Seite ] 6 | Stammdatenexperte – Produktdaten | Material anlegen |  |
| [Serviceprodukt für einmaligen Service: URR_MAT1_SERV](#unique_7) [Seite ] 9 | Stammdatenexperte – Produktdaten | Material anlegen |  |

Tabelle 2: Materialstammdaten für Integrationsszenario für Festpreiskundenprojekt anlegen

| Prozessschritt | Anwendungsrolle | App/Transaktion | Erwartete Ergebnisse |
| --- | --- | --- | --- |
| [URR_FPPRJ_1](#unique_8) [Seite ] 11 | Stammdatenexperte – Produktdaten | Material anlegen |  |

Tabelle 3: Materialstammdaten für Integrationsszenario für Servicevertrag anlegen

| Prozessschritt | Anwendungsrolle | App/Transaktion | Erwartete Ergebnisse |
| --- | --- | --- | --- |
| [URR_SRVCONT1](#unique_9) [Seite ] 14 | Stammdatenexperte – Produktdaten | Material anlegen |  |

Tabelle 4: Materialstammdaten für Integrationsszenario für Servicevertrag anlegen

| Prozessschritt | Anwendungsrolle | App/Transaktion | Erwartete Ergebnisse |
| --- | --- | --- | --- |
| [Preis für Handelsware für SFS: URR_MAT1_NORM](#unique_10) [Seite ] 16 | Preisfindungssachbearbeiter | Materialpreise festlegen. |  |
| [Preis für Serviceprodukt für einmaligen Service: URR_MAT1_SERV](#unique_11) [Seite ] 18 | Preisfindungssachbearbeiter | Materialpreise festlegen. |  |
| [Preis für Servicevertragsmaterial: URR_SRVCONT1](#unique_12) [Seite ] 20 | Preisfindungssachbearbeiter | Materialpreise festlegen. |  |

## Materialstammdaten für Integrationsszenario für den Verkauf ab Lager (SFS) anlegen

### Handelswaren: URR_MAT1_NORM

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
| 1 | Anmelden | Melden Sie sich am SAP Fiori Launchpad als Stammdatenexperte – Produktdaten an. | Die Startseite wird angezeigt. |  |
| 2 | SAP-Fiori-App aufrufen | Wählen Sie die App Material anlegen(wenn die App auf dem Bild nicht verfügbar ist, können Sie versuchen, die App "Material anlegen" zu suchen). | Das Bild "Material anlegen" (Einstieg) wird angezeigt. |  |
| 3 | Materialnummer und Materialart eingeben | Nehmen Sie auf dem Bild "Material anlegen" (Einstieg), die folgenden Einträge vor:Produktnummer: URR_MAT1_NORMMaterialart: HandelswareWählen Sie anschließend "Weiter" (Enter). | Sie haben die Materialnummer und die Materialart für die neuen Materialstammdaten eingegeben.Das Dialogfenster "Sichtenauswahl" wird angezeigt. |  |
| 4 | Sichten wählen | Wählen Sie im Dialogfenster "Sichtenauswahl" die folgenden Sichten aus:Grunddaten 1Verkauf: VerkaufsorgDaten 1Vertrieb: VerkaufsorgDaten 2Vertrieb: All./WerksdatenBuchhaltung1Wählen Sie anschließend "Weiter" (Enter). | Das Dialogfenster "Organisationsebenen" wird angezeigt. |  |
| 5 | Organisationsebenen wählen | Geben Sie im Dialogfenster "Organisationsebenen" die folgenden Werte ein:Werk: 1010 (Werk 1 DE)Verkaufsorganisation: 1010 (Inländ. Verkaufsorganisation DE)Vertriebsweg: 10 (Direktverkauf)Wählen Sie anschließend "Weiter" (Enter). | Es wurden Organisationsdaten ausgewählt.Die Sicht "Grunddaten 1" wird angezeigt. |  |
| 6 | Sicht pflegen: Grunddaten 1 | Pflegen Sie in der Sicht "Grunddaten 1" die folgenden Werte:Beschreib.: UER-Testmaterial1 NORMBasismengeneinheit: ST (Stück)Materialgruppe: L001 (Handelswaren)AllgPosGrp: NORM (Normalposition)Bruttogewicht: 1Nettogewicht: 1Gewichtseinheit: KGVolumen: 1Volumeneinheit: M3Drücken Sie die Eingabetaste. | Die Grunddaten werden gepflegt.Nachdem Sie die Eingabetaste gedrückt haben, wird das Bild Verkauf: Verkaufsorganisation 1" wird angezeigt. |  |
| 7 | Sicht pflegen: Vertrieb: Verkaufsorganisation 1 | Geben Sie auf dem Bild "Vertrieb: Verkaufsorganisation "1 die folgenden Werte ein:Allgemeine DatenSkonto: X <ausgewählt>SteuerdatenSteuerklassifikation: 0Wählen Sie anschließend die Eingabetaste. | Die Verkaufsorganisationsdaten 1 wurden gepflegt. Die Registerkarte "Vertrieb: Verkaufsorganisation 2" wird angezeigt. |  |
| 8 | Sicht pflegen: Vertrieb: Verkaufsorganisation 2 | Geben Sie unter "Vertrieb: Verkaufsorganisation 2" den folgenden Eintrag vor:Allg. PosTypengruppe: NORM (Normalposition)Positionstypengruppe: NORM (Normalposition)Wählen Sie anschließend die Eingabetaste. | Die Verkaufsorganisationsdaten 2 wurden gepflegt. Die Registerkarte "Vertrieb: Allg./Werk" wird angezeigt. |  |
| 9 | Sicht pflegen: Vertrieb: Allg./Werk | Geben Sie unter "Vertrieb: Allg./Werk" die folgenden Werte ein:Basismengeneinheit: ST (Stück)Bruttogewicht: 1KGNettogewicht: 1Verfügbarkeitsprüfung: NCTransportgruppe: 0001Ladegruppe: 0001Profitcenter: Y1041Wählen Sie anschließend die Eingabetaste. | Allgemeine Verkaufsdaten wurden erfasst. Die Sicht "Buchhaltung 1 wird angezeigt. |  |
| 10 | Sicht pflegen: Buchhaltung 1 | Nehmen Sie in der Sicht "Buchhaltung 1" im Abschnitt "Aktuelle Periode" folgenden Eintrag vor:Basismengeneinheit: PCBewertungsklasse: 3100Standardpreis: 16Per. VPreis: 16Preiseinheit: 1Preissteuerung: VZukünftiger Preis: leerWählen Sie anschließend "Sichern". | Die Buchhaltungsdaten werden gepflegt.Die Materialstammdaten werden gesichert. |  |
| 11 | Bei Bedarf weitere Materialstammdaten zum Testen anlegen | Legen Sie weitere Materialstämme gemäß der Namenskonvention URR_MAT*_NORM (z.B. URR_MAT2_NORM, URR_MAT3_NORM usw.) mit unterschiedlichem Standardpreis an. | Weitere Test-Materialstammdaten werden angelegt. | Für CE 2502 werden URR_MAT1_NORM und URR_MAT2_NORM als Demodaten ausgeliefert, sodass der Benutzer sie nicht manuell anlegen muss.Wenn für den Test des Integrationsszenarios "Verkauf ab Lager" weitere Materialstammdaten erforderlich sind, führen Sie die Schritte in diesem Abschnitt aus, um weitere Materialien anzulegen. |

### Serviceprodukt für einmaligen Service: URR_MAT1_SERV

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
| 1 | Anmelden | Melden Sie sich am SAP Fiori Launchpad als Stammdatenexperte – Produktdaten an. | Die Startseite wird angezeigt. |  |
| 2 | SAP-Fiori-App aufrufen | Wählen Sie die App "Material anlegen" (wenn die App auf dem Bild nicht verfügbar ist, können Sie versuchen, die App "Material anlegen" zu suchen). | Das Bild "Material anlegen" (Einstieg) wird angezeigt. |  |
| 3 | Materialnummer und Materialart eingeben | Nehmen Sie auf dem Bild "Material anlegen" (Einstieg), die folgenden Einträge vor:Produktnummer: URR_MAT1_SERVMaterialart: ServiceproduktWählen Sie anschließend "Weiter" (Enter). | Sie haben die Materialnummer und die Materialart für die neuen Materialstammdaten eingegeben.Das Dialogfenster "Sichtenauswahl" wird angezeigt. |  |
| 4 | Sichten wählen | Wählen Sie im Dialogfenster "Sichtenauswahl" die folgenden Sichten aus:Grunddaten 1Verkauf: VerkaufsorgDaten 1Vertrieb: VerkaufsorgDaten 2Vertrieb: All./WerksdatenBuchhaltung1Wählen Sie anschließend "Weiter" (Enter). | Das Dialogfenster "Organisationsebenen" wird angezeigt. |  |
| 5 | Organisationsebenen wählen | Geben Sie im Dialogfenster "Organisationsebenen" die folgenden Werte ein:Werk: 1010 (Werk 1 DE)Verkaufsorganisation: 1010 (Inländ. Verkaufsorganisation DE)Vertriebsweg: 10 (Direktverkauf)Wählen Sie anschließend "Weiter" (Enter). | Es wurden Organisationsdaten ausgewählt.Die Sicht "Grunddaten 1" wird angezeigt. |  |
| 6 | Sicht pflegen: Grunddaten 1 | Pflegen Sie in der Sicht "Grunddaten 1" die folgenden Werte:Beschreib.: UER-Testmaterial1 SERVBasismengeneinheit: h (Stunden)Materialgruppe: YBMM01 (Nichtlagermaterial mit ID)AllgPosGrp: SERV (Services)Drücken Sie die Eingabetaste. | Die Grunddaten werden gepflegt.Nachdem Sie die Eingabetaste gedrückt haben, wird das Bild Verkauf: Verkaufsorganisation 1" wird angezeigt. |  |
| 7 | Sicht pflegen: Vertrieb: Verkaufsorganisation 1 | Geben Sie auf dem Bild "Vertrieb: Verkaufsorganisation "1 die folgenden Werte ein:Allgemeine DatenAuslieferungswerk: 1010Skonto: X <ausgewählt>SteuerdatenSteuerklassifikation: 0Wählen Sie anschließend die Eingabetaste. | Die Verkaufsorganisationsdaten 1 wurden gepflegt. Die Registerkarte "Vertrieb: Verkaufsorganisation 2" wird angezeigt. |  |
| 8 | Sicht pflegen: Vertrieb: Verkaufsorganisation 2 | Nehmen Sie unter "Vertrieb: Verkaufsorganisation 2" den folgenden Eintrag vor:Allg. PosTypengruppe: SERV (Services)Positionstypengruppe: SERV (Services)Wählen Sie anschließend die Eingabetaste. | Die Verkaufsorganisationsdaten 2 wurden gepflegt. Die Registerkarte "Vertrieb: Allg./Werk" wird angezeigt. |  |
| 9 | Sicht pflegen: Vertrieb: Allg./Werk | Geben Sie unter "Vertrieb: Allg./Werk" die folgenden Werte ein:Profitcenter: YB600Wählen Sie anschließend die Eingabetaste. | Allgemeine Verkaufsdaten wurden erfasst. Die Sicht "Buchhaltung 1 wird angezeigt. |  |
| 10 | Sicht pflegen: Buchhaltung 1 | Nehmen Sie in der Sicht "Buchhaltung 1" im Abschnitt "Aktuelle Periode" folgenden Eintrag vor:Bewertungsklasse: 3300Standardpreis: 20Preiseinheit: 1Wählen Sie anschließend "Sichern". | Die Buchhaltungsdaten werden gepflegt.Die Materialstammdaten werden gesichert. |  |

## Materialstammdaten für Integrationsszenario für Festpreiskundenprojekt anlegen

### URR_FPPRJ_1

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
| 1 | Anmelden | Melden Sie sich am SAP Fiori Launchpad als Stammdatenexperte – Produktdaten an. | Die Startseite wird angezeigt. |  |
| 2 | SAP-Fiori-App aufrufen | Wählen Sie die App "Material anlegen" (wenn die App auf dem Bild nicht verfügbar ist, können Sie versuchen, die App "Material anlegen" zu suchen). | Das Bild "Material anlegen" (Einstieg) wird angezeigt. |  |
| 3 | Materialnummer und Materialart eingeben | Nehmen Sie auf dem Bild "Material anlegen" (Einstieg), die folgenden Einträge vor:Produktnummer: URR_FPPRJ_1Materialart: ServiceproduktWählen Sie anschließend "Weiter" (Enter). | Sie haben die Materialnummer und die Materialart für die neuen Materialstammdaten eingegeben.Das Dialogfenster "Sichtenauswahl" wird angezeigt. |  |
| 4 | Sichten wählen | Wählen Sie im Dialogfenster "Sichtenauswahl" die folgenden Sichten aus:Grunddaten 1Verkauf: VerkaufsorgDaten 1Vertrieb: VerkaufsorgDaten 2Vertrieb: All./WerksdatenBuchhaltung1Wählen Sie anschließend "Weiter" (Enter). | Das Dialogfenster "Organisationsebenen" wird angezeigt. |  |
| 5 | Organisationsebenen wählen | Geben Sie im Dialogfenster "Organisationsebenen" die folgenden Werte ein:Werk: 1010 (Werk 1 DE)Verkaufsorganisation: 1010 (Inländ. Verkaufsorganisation DE)Vertriebsweg: 10 (Direktverkauf)Wählen Sie anschließend "Weiter" (Enter). | Es wurden Organisationsdaten ausgewählt.Die Sicht "Grunddaten 1" wird angezeigt. |  |
| 6 | Sicht pflegen: Grunddaten 1 | Pflegen Sie in der Sicht "Grunddaten 1" die folgenden Werte:Beschreib.: UER-Testmaterial1 SERVBasismengeneinheit: LE (Leistungseinheit)Materialgruppe: P000 (Vertragsart)AllgPosGrp: PSFP (Festpreisposition)Drücken Sie die Eingabetaste. | Die Grunddaten werden gepflegt.Nachdem Sie die Eingabetaste gedrückt haben, wird das Bild "Vertrieb: Verkaufsorganisation" angezeigt. |  |
| 7 | Sicht pflegen: Vertrieb: Verkaufsorganisation 1 | Geben Sie auf dem Bild "Vertrieb: Verkaufsorganisation 1" die folgenden Werte ein:Allgemeine DatenAuslieferungswerk: 1010Skonto: X <ausgewählt>SteuerdatenSteuerklassifikation: 0Wählen Sie anschließend die Eingabetaste. | Die Verkaufsorganisationsdaten 1 wurden gepflegt. Die Registerkarte "Vertrieb: Verkaufsorganisation 2" wird angezeigt. |  |
| 8 | Sicht pflegen: Vertrieb: Verkaufsorganisation 2 | Geben Sie unter "Vertrieb: Verkaufsorganisation 2" den folgenden Eintrag vor:Allg. PosTypengruppe: PSFP (Festpreisposition)Kontierungsgr. Mat.: Y1 (Festpreis)Positionstypengruppe: PSFP (Festpreisposition)Wählen Sie anschließend die Eingabetaste. | Die Verkaufsorganisationsdaten 2 wurden gepflegt. Die Registerkarte "Vertrieb: Allg./Werk" wird angezeigt. |  |
| 9 | Sicht pflegen: Vertrieb: Allg./Werk | Geben Sie unter "Vertrieb: Allg./Werk" die folgenden Werte ein:Profitcenter: YB101Wählen Sie anschließend die Eingabetaste. | Allgemeine Verkaufsdaten wurden erfasst. Die Sicht "Buchhaltung 1 wird angezeigt. |  |
| 10 | Sicht pflegen: Buchhaltung 1 | Nehmen Sie in der Sicht "Buchhaltung 1" im Abschnitt "Aktuelle Periode" folgenden Eintrag vor:Bewertungsklasse: 3300Standardpreis: 30Preiseinheit: 1Wählen Sie anschließend "Sichern". | Die Buchhaltungsdaten werden gepflegt.Die Materialstammdaten werden gesichert. |  |
| 11 | Bei Bedarf weitere Materialstammdaten zum Testen anlegen | Legen Sie einen weiteren Materialstamm mit der Namenskonvention URR_FPPRJ* (z.B.: URR_FPPRJ3, URR_FPPRJ4 usw.) mit unterschiedlichem Standardpreis, falls erforderlich an. | Weitere Test-Materialstammdaten werden angelegt. |  |

## Materialstammdaten für Integrationsszenario für Servicevertrag anlegen

### URR_SRVCONT1

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
| 1 | Anmelden | Melden Sie sich am SAP Fiori Launchpad als Stammdatenexperte – Produktdaten an. | Die Startseite wird angezeigt. |  |
| 2 | SAP-Fiori-App aufrufen | Wählen Sie die App "Material anlegen" (wenn die App auf dem Bild nicht verfügbar ist, können Sie versuchen, die App "Material anlegen" zu suchen). | Das Bild "Material anlegen" (Einstieg) wird angezeigt. |  |
| 3 | Materialnummer und Materialart eingeben | Nehmen Sie auf dem Bild "Material anlegen" (Einstieg), die folgenden Einträge vor:Produktnummer: UER_SRVCON1Materialart: ServiceproduktWählen Sie anschließend "Weiter" (Enter). | Sie haben die Materialnummer und die Materialart für die neuen Materialstammdaten eingegeben.Das Dialogfenster "Sichtenauswahl" wird angezeigt. |  |
| 4 | Sichten wählen | Wählen Sie im Dialogfenster "Sichtenauswahl" die folgenden Sichten aus:Grunddaten 1Verkauf: VerkaufsorgDaten 1Vertrieb: VerkaufsorgDaten 2Vertrieb: All./WerksdatenEinkaufWählen Sie anschließend "Weiter" (Enter). | Das Dialogfenster "Organisationsebenen" wird angezeigt. |  |
| 5 | Organisationsebenen wählen | Geben Sie im Dialogfenster "Organisationsebenen" die folgenden Werte ein:Werk: 1010 (Werk 1 DE)Verkaufsorganisation: 1010 (Inländ. Verkaufsorganisation DE)Vertriebsweg: 10 (Direktverkauf)Wählen Sie anschließend "Weiter" (Enter). | Es wurden Organisationsdaten ausgewählt.Die Sicht "Grunddaten 1" wird angezeigt. |  |
| 6 | Sicht pflegen: Grunddaten 1 | Pflegen Sie in der Sicht "Grunddaten 1" die folgenden Werte:Beschreib.: UER-Testmaterial 1 ServicevertragBasismengeneinheit: LE (Leistungseinheit)Materialgruppe: P001 (Services)AllgPosGrp: SCNP (Servicevertragsprod.)Drücken Sie die Eingabetaste. | Die Grunddaten werden gepflegt.Nachdem Sie die Eingabetaste gedrückt haben, wird das Bild Verkauf: Verkaufsorganisation 1" wird angezeigt. |  |
| 7 | Sicht pflegen: Vertrieb: Verkaufsorganisation 1 | Geben Sie auf dem Bild "Vertrieb: Verkaufsorganisation "1 die folgenden Werte ein:Allgemeine DatenBasismengeneinheit: LE (Leistungseinheit)Materialgruppe: P001 (Services)Wählen Sie anschließend die Eingabetaste. | Die Verkaufsorganisationsdaten 1 wurden gepflegt. Die Registerkarte "Vertrieb: Verkaufsorganisation 2" wird angezeigt. |  |
| 8 | Sicht pflegen: Vertrieb: Verkaufsorganisation 2 | Geben Sie unter "Vertrieb: Verkaufsorganisation 2" den folgenden Eintrag vor:Allg. PosTypengruppe SCNP (Servicevertragsprod.)Wählen Sie anschließend die Eingabetaste. | Die Verkaufsorganisationsdaten 2 wurden gepflegt. Die Registerkarte "Vertrieb: Allg./Werk" wird angezeigt. |  |
| 9 | Sicht pflegen: Vertrieb: Allg./Werk | Geben Sie unter "Vertrieb: Allg./Werk" die folgenden Werte ein:Basismengeneinheit: LE (Leistungseinheit)Wählen Sie anschließend die Eingabetaste. | Allgemeine Verkaufsdaten wurden erfasst. Die Sicht "Buchhaltung 1 wird angezeigt. |  |
| 10 | Sicht pflegen: Einkauf | Geben Sie in der Einkaufssicht folgende Daten ein:Basismengeneinheit: LE (Leistungseinheit)Materialgruppe: P001 (Services)Wählen Sie anschließend "Sichern". | Die Buchhaltungsdaten werden gepflegt.Die Materialstammdaten werden gesichert. |  |

## Preise für Materialien festlegen

### Preis für Handelsware für SFS: URR_MAT1_NORM

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
| 1 | Anmelden | Melden Sie sich am SAP Fiori Launchpad als Preisfindungssachbearbeiter an. | Das SAP Fiori Launchpad wird geöffnet. |  |
| 2 | SAP-Fiori-App aufrufen | Wählen Sie Materialpreise festlegen – Verkauf(VK12). | Die Sicht "Konditionssätze ändern" wird angezeigt. |  |
| 3 | Preiskonditionsart | Geben Sie in der Sicht Konditionssätze ändern die folgenden Informationen ein:Konditionsart: PPR0Wählen Sie anschließend Enter. | Die Sicht "Schlüsselkombination" wird angezeigt. |  |
| 4 | Schlüsselkombination | Wählen Sie in der Sicht Schlüsselkombination die Option Material mit Freigabestatus.Wählen Sie anschließend Auswählen. | Das Bild "Preis ändern (PPR0): Auswahl" wird angezeigt. |  |
| 5 | Auswählen | Geben Sie auf dem Bild Preis ändern (PPR0): Auswahl die folgenden Informationen ein:Verkaufsorganisation: 1010 (Inländ. Verkaufsorganisation DE)Vertriebsweg: 10 (Direktverkauf)Material: URR_MAT1_NORMGültig am: <Datum> z.B. das aktuelle DatumWählen Sie anschließend Ausführen. | Die Sicht "Preiskondition ändern (PPR0): Übersicht" wird angezeigt. |  |
| 6 | Preiskonditionen ändern | Geben Sie in der Sicht Preiskondition ändern (PPR0): Übersicht folgende Daten für das Material:Material: URR_MAT1_NORMBetrag: z.B. 25,00Einheit: EURGültig ab: <Datum> z.B. das aktuelle DatumWählen Sie Enter. | Die Preiskonditionen wurden gepflegt. |  |
| 7 | Sichern | Wählen Sie Sichern. | Die Preise wurden definiert. |  |
| 8 | Zurück und App erneut aufrufen | Geben Sie in der Sicht Konditionssätze ändern die folgenden Informationen ein:Konditionsart: PSAMDrücken Sie anschließend ENTER. | Die Sicht "Schlüsselkombination" wird angezeigt. |  |
| 9 | Schlüsselkombination | Wählen Sie in der Sicht Schlüsselkombination die Option "Material mit Freigabestatus".Drücken Sie anschließend ENTER. | Das Bild "Preis ändern (PPR0): Auswahl" wird angezeigt. |  |
| 10 | Auswählen | Das Bild "Preis ändern (PSAM): Auswahl" die folgenden Informationen ein:Verkaufsorganisation: 1010 (Inländ. Verkaufsorganisation DE)Vertriebsweg: 10 (Direktverkauf)Material: URR_MAT1_NORMGültig am: <Datum> z.B. das aktuelle DatumWählen Sie anschließend Ausführen. | Die Sicht "Preiskondition ändern (PSAM): Übersicht" wird angezeigt. |  |
| 11 | Preiskonditionen ändern | Geben Sie auf der Sicht Preiskondition ändern (PSAM): Übersicht folgende Daten für das Material:Material: URR_MAT1_NORMBetrag: z.B. 35,00Einheit: EURGültig ab: <Datum> z.B. das aktuelle DatumWählen Sie Enter. | Die Preiskonditionen wurden gepflegt. |  |
| 12 | Sichern | Wählen Sie Sichern. | Der Preis wurde definiert. |  |

### Preis für Serviceprodukt für einmaligen Service: URR_MAT1_SERV

Testverwaltung

Kundenprojekt: Füllen Sie die projektbezogenen Teile aus.

|  |  |  |  |
| --- | --- | --- | --- |
| Testfall-ID | <X.XX> | Testdatum: |  |
| Testername: |  | Dauer: |  |
| Benutzerrolle(n): |  | Zuständigkeit: | <Geben Sie den Serviceanbieter, einen Kunden oder einen Serviceanbieter zusammen mit einem Kunden an.> |

Verfahren

| Testschrittnummer | Bezeichnung des Testschritts | Anweisungen | Erwartetes Ergebnis | Kommentare |
| --- | --- | --- | --- | --- |
| 1 | Anmelden | Melden Sie sich am SAP Fiori Launchpad als Preisfindungssachbearbeiter an. | Das SAP Fiori Launchpad wird geöffnet. |  |
| 2 | SAP-Fiori-App aufrufen | Wählen Sie Materialpreise festlegen – Verkauf(VK12). | Die Sicht "Konditionssätze ändern" wird angezeigt. |  |
| 3 | Preiskonditionsart | Geben Sie auf der Sicht "Konditionssätze ändern" die folgenden Informationen ein:Konditionsart: PPR0Drücken Sie anschließend ENTER. | Die Sicht "Schlüsselkombination" wird angezeigt. |  |
| 4 | Schlüsselkombination | Wählen Sie in der Sicht "Schlüsselkombination" die Option "Material" mit Freigabestatus.Wählen Sie anschließend "Auswählen" (Enter). | Das Bild "Preis ändern (PPR0): Auswahl" wird angezeigt. |  |
| 5 | Auswählen | Geben Sie auf der Sicht "Preis ändern (PPR0): Auswahl" die folgenden Informationen ein:Verkaufsorganisation: 1010 (Inländ. Verkaufsorganisation DE)Vertriebsweg: 10 (Direktverkauf)Material: URR_MAT1_SERVGültig am: <Datum> z.B. das aktuelle DatumWählen Sie anschließend Ausführen. | Die Sicht "Preiskondition ändern (PPR0): Übersicht" wird angezeigt. |  |
| 6 | Preiskondition ändern | Geben Sie in der Sicht Preiskondition ändern (PPR0): Übersicht folgende Daten für das Material:Material: URR_MAT1_SERVBetrag: z.B. 25,00Einheit: EURGültig ab: <Datum> z.B. das aktuelle DatumWählen Sie Enter. | Die Preiskonditionen für die Serviceprodukte SRV_01 wurden gepflegt. |  |
| 7 | Sichern | Wählen Sie Sichern. | Die Preise für die Serviceprodukte wurden definiert. |  |
| 8 | Zurück und App erneut aufrufen | Geben Sie in der Sicht Konditionssätze ändern die folgenden Informationen ein:Konditionsart: PSAMDrücken Sie anschließend ENTER. |  |  |
| 9 | Schlüsselkombination | Wählen Sie in der Sicht Schlüsselkombination die Option "Material mit Freigabestatus".Drücken Sie anschließend ENTER. | Das Bild "Preis ändern (PPR0): Auswahl" wird angezeigt. |  |
| 10 | Auswählen | Das Bild "Preis ändern (PSAM): Auswahl" die folgenden Informationen ein:Verkaufsorganisation: 1010 (Inländ. Verkaufsorganisation DE)Vertriebsweg: 10 (Direktverkauf)Material: URR_MAT1_SERVGültig am: <Datum> z.B. das aktuelle DatumWählen Sie anschließend Ausführen. | Die Sicht "Preiskondition ändern (PSAM): Übersicht" wird angezeigt. |  |
| 11 | Preiskondition ändern | Geben Sie auf der Sicht Preiskondition ändern (PSAM): Übersicht folgende Daten für das Material:Material: URR_MAT1_SERVBetrag: z.B. 35,00Einheit: EURGültig ab: <Datum> z.B. das aktuelle DatumWählen Sie Enter. | Die Preiskonditionen für die Serviceprodukte SRV_01 wurden gepflegt. |  |
| 12 | Sichern | Wählen Sie Sichern. | Der Preis wurde definiert. |  |

### Preis für Servicevertragsmaterial: URR_SRVCONT1

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
| 1 | Anmelden | Melden Sie sich am SAP Fiori Launchpad als Preisfindungssachbearbeiter an. | Das SAP Fiori Launchpad wird geöffnet. |  |
| 2 | SAP-Fiori-App aufrufen | Wählen Sie Materialpreise festlegen – Verkauf(VK12). | Die Sicht "Konditionssätze ändern" wird angezeigt. |  |
| 3 | Preiskonditionsart | Geben Sie in der Sicht Konditionssätze ändern die folgenden Informationen ein:Konditionsart: PSI1Drücken Sie anschließend ENTER. | Die Sicht "Schlüsselkombination" wird angezeigt. |  |
| 4 | Schlüsselkombination | Wählen Sie in der Sicht Schlüsselkombination die Option "Material".Drücken Sie anschließend ENTER. | Die Sicht "Preis ändern (PSI1): Auswahl" wird angezeigt. |  |
| 5 | Auswählen | Geben Sie auf dem Bild Preis ändern (PSI1): Auswahl die folgenden Informationen ein:Verkaufsorganisation: 1010 (Inländ. Verkaufsorganisation DE)Vertriebsweg: 10 (Direktverkauf)Material: URR_SRVCONT1Gültig am: <Datum> z.B. das aktuelle DatumWählen Sie anschließend Ausführen. | Die Sicht "Preiskondition ändern (PSI1): Übersicht" wird angezeigt. |  |
| 6 | Preiskondition ändern | Geben Sie auf der Sicht Preiskondition ändern (PSI1): Übersicht die folgenden Daten ein:Material: URR_SRVCONT1Betrag: z.B. 90,00Einheit: z.B. EURGültig ab: <Datum> z.B. das aktuelle DatumWählen Sie Enter. | Die Preiskonditionen sind gepflegt. |  |
| 7 | Sichern | Wählen Sie Sichern. | Der Preis wurde definiert. |  |

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
> Flagged while digesting this document, not verified: Step 3 of the URR_SRVCONT1 section uses product number UER_SRVCON1, whereas the rest of the document uses URR_SRVCONT1.

> [!warning] Conflict
> Flagged while digesting this document, not verified: URR_MAT1_SERV is listed in the purpose table as used in the stock sales scenario, while its section is titled one-time service product; URR_FPPRJ_1 step 6 gives description 'UER-Testmaterial1 SERV' instead of a fixed-price description.

## Connections
- part-of :: [[_cluster]]
- related-to :: [[06-management-accounting/7r8-537]]
- related-to :: [[06-management-accounting/master-data-script-create-material-master-for-universal-revenue-recogn]]
- related-to :: [[06-management-accounting/master-data-script-item-master-for-universal-revenue-recognition-7r8-j]]
- related-to :: [[06-management-accounting/script-de-dados-mestre-criar-mestre-de-materiais-para-realizacao-de-re]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/7R8_S4CLD2608_Master_Data_DE_XX.docx` — full document · extracted with `mammoth` · 34,284 chars in the whole document
