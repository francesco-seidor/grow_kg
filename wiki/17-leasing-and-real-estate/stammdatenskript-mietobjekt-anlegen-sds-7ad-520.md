---
id: 17-leasing-and-real-estate/stammdatenskript-mietobjekt-anlegen-sds-7ad-520
title: "Stammdatenskript: Mietobjekt anlegen – SDS (7AD) (7AD_S4CLD2608_Master_Data_DE_XX)"
description: "German master data script (SAP S/4HANA Cloud Public Edition 2608, scope 7AD): creating generic rental objects (usable/rentable, intercompany) with prerequisites and test steps."
cluster: 17-leasing-and-real-estate
tags: [kb/leasing-and-real-estate, topic/real-estate-contracts-and-leasing]
aliases: [7AD_S4CLD2608_Master_Data_DE_XX]
keywords: [Real Estate Rental Objects and Lease Accounting, generic rental objects, usable objects, rentable objects, intercompany leasing, usage types, number ranges, measurements, real estate architecture objects, master data integration]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/7AD_S4CLD2608_Master_Data_DE_XX.docx]
confidence: high
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-520
topic: 17-leasing-and-real-estate/real-estate-contracts-and-leasing
language: DE
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Stammdatenskript: Mietobjekt anlegen – SDS (7AD) (7AD_S4CLD2608_Master_Data_DE_XX)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/7AD_S4CLD2608_Master_Data_DE_XX.docx`, extracted with `mammoth`. Grouped under **Real Estate Rental Objects and Lease Accounting** in Leasing and Real Estate. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

| <!-- image omitted: unnamed --> | StammdatenskriptSAP S/4HANA Cloud Public Edition - 02-07-26 |
| --- | --- |
|  | Mietobjekt anlegen – SDS (7AD) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Inhaltsverzeichnis

[1 Zweck 3](#_Toc233889851)

[2 Voraussetzungen 4](#_Toc233889852)

[2.1 Systemzugriff 4](#_Toc233889853)

[2.2 Rollen 4](#_Toc233889854)

[2.3 Erforderliche Organisationseinheiten 4](#_Toc233889855)

[2.4 Obligatorische und optionale Stammdaten 5](#_Toc233889856)

[2.5 Wesentliche Parameter für die Datenerstellung 5](#_Toc233889857)

[2.5.1 Nutzungstyp 5](#_Toc233889858)

[2.5.2 Nutzungsarten und Nummernkreise 6](#_Toc233889859)

[2.5.3 Eigentums-ID 7](#_Toc233889860)

[2.5.4 Portfolio-ID 7](#_Toc233889861)

[2.5.5 Messungen 8](#_Toc233889862)

[2.5.6 Objekttyp und Nummernkreis der Immobilienarchitektur 9](#_Toc233889863)

[2.5.7 Hierarchie von Immobilienarchitekturobjekten 9](#_Toc233889864)

[2.6 Vorbereitende Schritte 9](#_Toc233889865)

[2.6.1 MDI-Servicebereitschaft validieren 9](#_Toc233889866)

[3 Übersichtstabelle 10](#_Toc233889867)

[4 Testverfahren 11](#_Toc233889868)

[4.1 Nutzbares Objekt ohne Portfoliostruktur anlegen 11](#_Toc233889869)

[4.2 Nutzbares Objekt mit Portfoliostruktur anlegen 12](#_Toc233889870)

[4.3 Vermietbares Objekt ohne Portfoliostruktur anlegen 14](#_Toc233889871)

[4.4 Vermietbares Objekt mit Portfoliostruktur ändern 15](#_Toc233889872)

[4.5 Buchungskreisübergreifendes vermietbares Objekt mit Portfoliostruktur anlegen 16](#_Toc233889873)

[4.6 Buchungskreisübergreifendes vermietbares Objekt ohne Portfoliostruktur anlegen 17](#_Toc233889874)

[4.7 Buchungskreisübergreifendes nutzbares Objekt mit Portfoliostruktur anlegen 18](#_Toc233889875)

[4.8 Buchungskreisübergreifendes nutzbares Objekt ohne Portfoliostruktur anlegen 20](#_Toc233889876)

## Zweck

Ein generisches Mietobjekt kann entweder ein nutzbares oder ein vermietbares Objekt sein.

Ein nutzbares Objekt ist ein Objekt, das von einem Unternehmen angemietet wird oder im Besitz eines Unternehmens ist und den Umfang für die eigene Nutzung, dem externen oder den buchungskreisübergreifenden Mietvertrag definiert. Das nutzbare Objekt kann Gegenstand eines Immobilienanmietvertrags sein. Das Unternehmen handelt aus Kundensicht.

Ein vermietbares Objekt ist ein Objekt, das von einem Unternehmen an einen externen Mieter oder ein verbundenes Unternehmen vermietet werden kann. Das vermietbare Objekt kann Gegenstand eines Immobilienmietvertrags sein. Das Unternehmen handelt aus Lieferantensicht.

Generische Mietobjekte werden in den unterschiedlichen Szenarios wie folgt verwendet:

a) Externe Anmietobjekte oder eigene Objekte

Sie definieren externe Anmietobjekte oder eigene Objekte als verwendbare Objekte. Dazu können Sie die Nutzungskategorie Nutzbares Objekt mit Portfoliostruktur (UP) oder Nutzbares Objekt ohne Portfoliostruktur (UW) verwenden. Nutzbare Objekte werden für alle Folgeprozesse benötigt.

b) Externe Vermietungsobjekte

Sie definieren externe Vermietungsobjekte als vermietbare Objekte. Dazu können Sie die Nutzungskategorie Vermietbares Objekt mit Portfoliostruktur (RP) oder Vermietbares Objekt ohne Portfoliostruktur (RW) verwenden. Jedes vermietbare Objekt benötigt eine Beziehung zu einem nutzbaren Objekt. Daher müssen Sie zuvor ein nutzbares Objekt angelegt haben (siehe a)).

c) Buchungskreisübergreifende Leasingobjekte

Um einen buchungskreisübergreifenden Leasingprozess einzurichten, sind die folgenden Objekte erforderlich:

1. Nutzbares Objekt (extern angemietet oder Eigentum) (siehe a))
2. Buchungskreisübergreifendes vermietbares Objekt (Nutzungskategorie Buchungskreisübergr. vermietb. Objekt mit Portfoliostruktur (I3) oder Buchungskreisübergr. vermietb. Objekt ohne Portfoliostruktur (I4)) mit einer Beziehung zu einem nutzbaren Objekt (siehe 1.) innerhalb des LeasinggeberBuchungskreises
3. Buchungskreisübergreifendes nutzbares Objekt (Nutzungskategorie Buchungskreisübergreifendes nutzbares Objekt mit Portfoliostruktur (I1) oder Buchungskreisübergreifendes nutzbares Objekt ohne Portfoliostruktur (I2)) innerhalb des Leasingnehmer-Buchungskreises mit einer Beziehung zu einem buchungskreisübergreifenden vermietbaren Objekt innerhalb des Leasinggeber-Buchungskreises (siehe 2.)

Anschließend können Sie mit 2. und 3. fortfahren, um einen zusätzlichen buchungskreisübergreifenden Leasingprozess für einen dritten Buchungskreis einzurichten, oder mit b), um ein externes Vermietungsobjekt anzulegen. Das zusätzliche buchungskreisübergreifende vermietbare Objekt oder externe vermietbare Objekt hat in diesem Fall eine Beziehung zum buchungskreisübergreifenden nutzbaren Objekt.

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
| Sachbearbeiter Immobilien - Standortverwaltung | SAP_BR_RE_SPECIALIST_LOCAT | Standortverwaltung | SAP_FIN_SPT_RE_LOCATION_PC |  |
| Sachbearbeiter Vertrag – Leasing | SAP_BR_RECM_SPECIALIST | Leasingvertragsverwaltung / Leasingvertragsverwaltung - Umsatzmiete | SAP_BR_RECM_SPECIALIST / SAP_BR_RECM_SALES_REPORTER |  |

### Erforderliche Organisationseinheiten

Die Organisationsstruktur und die Stammdaten Ihres Unternehmens wurden bei der Implementierung in Ihrem ERP-System angelegt. Die Organisationsstruktur gibt den Aufbau Ihres Unternehmens wieder. Die Stammdaten stehen für nutzbare Objekte, je nach betrieblichem Schwerpunkt Ihres Unternehmens.

| Datenobjekt | Verwendet im Datensegment | Obligatorisch / optional | Kommentare |
| --- | --- | --- | --- |
| Buchungskreis | Allgemeine Daten | obligatorisch |  |

### Obligatorische und optionale Stammdaten

Stammdatensätze von nutzbaren und vermietbaren Objekten können auf andere Stammdaten verweisen. Die folgende Tabelle bietet eine Übersicht über die optionalen und obligatorischen Stammdatenobjekte, die in einem nutzbaren/vermietbaren Stammdatensatz verwendet werden.

| Stammdatenobjekt | Verwendet im Datensegment | Obligatorisch / optional | Kommentare |
| --- | --- | --- | --- |
| Kostenstelle | Kontierungsobjekt: | Obligatorisch | Entweder Kostenstelle oder PSP-Element |
| PSP-Element | Kontierungsobjekt: | Obligatorisch | Entweder Kostenstelle oder PSP-Element |

### Wesentliche Parameter für die Datenerstellung

In diesem Abschnitt werden einige Basisparameter erläutert, die das Verhalten eines Stammsatzes beeinflussen und zum Anlegen eines generischen Mietobjekts erforderlich sind.

#### Nutzungstyp

Nutzungstypen bestimmen die Art und das Geschäftsverhalten eines generischen Mietobjekts. Die folgenden Nutzungstypen werden unterstützt:

1. Nutzbares Objekt mit Portfoliostruktur (UP) – Für diese nutzbare Objekte muss der Service SAP Master Data Integration auf BTP (MDI) verwendet werden, um die Beziehung zu Immobilienarchitekturobjekten herzustellen, die von einer externen Anwendung bereitgestellt werden.
2. Nutzbares Objekt ohne Portfoliostruktur (UW) – Für diese nutzbaren Objekte ist keine Beziehung zu Immobilienarchitekturobjekten möglich.
3. Vermietbares Objekt mit Portfoliostruktur (RP) – Für diese vermietbaren Objekte muss der Service SAP Master Data Integration auf BTP (MDI) verwendet werden, um die Beziehung zu Immobilienarchitekturobjekten herzustellen, die von einer externen Anwendung bereitgestellt werden.
4. Vermietbares Objekt ohne Portfoliostruktur (RW) – Für diese vermietbaren Objekte ist keine Beziehung zu Immobilienarchitekturobjekten möglich.
5. Buchungskreisübergreifendes vermietbares Objekt mit Portfoliostruktur (I3) – Diese vermietbaren Objekte werden in einem Szenario mit buchungskreisübergreifendem Mietvertrag verwendet und erfordern die Nutzung des Service SAP Master Data Integration auf BTP (MDI), um die Beziehung zu Immobilienarchitekturobjekten herzustellen, die von einer externen Anwendung bereitgestellt werden.
6. Buchungskreisübergreifendes vermietbares Objekt ohne Portfoliostruktur (I4) – Diese vermietbaren Objekte werden in einem Szenario mit buchungskreisübergreifender Vermietung ohne Beziehung zu Immobilienarchitekturobjekten verwendet.
7. Buchungskreisübergreifendes nutzbares Objekt mit Portfoliostruktur (I1) – Diese nutzbaren Objekte werden in einem Szenario mit buchungskreisübergreifender Anmietung verwendet und erfordern eine Beziehung zu einem vermietbaren Objekt des Nutzungstyps "Buchungskreisübergreifendes vermietbares Objekt mit Portfoliostruktur (I3)".
8. Buchungskreisübergreifendes nutzbares Objekt ohne Portfoliostruktur (I2) – Diese nutzbaren Objekte werden in einem Szenario mit buchungskreisübergreifender Anmietung verwendet und erfordern eine Beziehung zu einem vermietbaren Objekt des Nutzungstyps "Buchungskreisübergreifendes vermietbares Objekt ohne Portfoliostruktur (I4)".

#### Nutzungsarten und Nummernkreise

Für jeden Nutzungstyp können verschiedene Nutzungsarten definiert werden, um die Objekte und ihr betriebswirtschaftliches Verhalten innerhalb der des Typs zu unterscheiden. Die Nutzungsarten bestimmen die Nummernkreise für die Objektstammsatz-IDs. Sie können anschließend die Zuordnung oder die IDs nicht mehr ändern. Wenn eine Nutzungsart einem internen Nummernkreis zugeordnet ist, können Sie die Stammsatz-ID nicht manuell eingeben. Lassen Sie das Feld in diesem Fall leer, da das System automatisch eine Nummer aus dem zugeordneten numerischen Nummernkreis wählt.

Die folgenden Nutzungsarten und die entsprechenden Nummernkreise sind vordefiniert:

| Nutzungsart | Nutzungstyp | Nummernkreis | Kommentare |
| --- | --- | --- | --- |
| Computer-Hardware (SU01) | Nutzbares Objekt Objekt ohne Portfoliostruktur (UW) | 010000000 - 019999999 |  |
| Ausstattung (SU02) | Nutzbares Objekt Objekt ohne Portfoliostruktur (UW) | 020000000 - 029999999 |  |
| Maschinen (SU03) | Nutzbares Objekt Objekt ohne Portfoliostruktur (UW) | 030000000 - 039999999 |  |
| Fuhrpark (SU04) | Nutzbares Objekt Objekt ohne Portfoliostruktur (UW) | 040000000 - 049999999 |  |
| Betriebs- und Geschäftsausstattung (SU05) | Nutzbares Objekt Objekt ohne Portfoliostruktur (UW) | 050000000 - 059999999 |  |
| Bürogebäude (SU06) | Nutzbares Objekt mit Portfoliostruktur (UP) | 060000000 - 069999999 | Nur für Demozwecke |
| Einzelhandel (SU07) | Nutzbares Objekt mit Portfoliostruktur (UP) | 070000000 - 079999999 | Nur für Demozwecke |
| Wohnung (SU08) | Nutzbares Objekt mit Portfoliostruktur (UP) | 080000000 - 089999999 | Nur für Demozwecke |
| Büro (SR01) | Vermietbares Objekt mit Portfoliostruktur (RP) | 1000000000 - 1099999999 | Nur für Demozwecke |
| Geschäft (SR02) | Vermietbares Objekt mit Portfoliostruktur (RP) | 1100000000 - 1199999999 | Nur für Demozwecke |
| Wohnung (SR03) | Vermietbares Objekt mit Portfoliostruktur (RP) | 1200000000 - 1299999999 | Nur für Demozwecke |
| Fuhrpark (SR04) | Vermietbares Objekt ohne Portfoliostruktur (RW) | 1300000000 - 1399999999 | Nur für Demozwecke |
| Mietvertrag Büro ICO (SRI1) | Buchungskreisübergreifendes vermietbares Objekt mit Portfoliostruktur (I3) | 3100000000 - 3199999999 | Nur für Demozwecke |
| Anmietvertrag Büro ICO (SUI1) | Buchungskreisübergreifendes nutzbares Objekt mit Portfoliostruktur (I1) | 3000000000 - 3099999999 | Nur für Demozwecke |
| Mietvertrag Büroausstattung ICO (SRI2) | Buchungskreisübergreifendes vermietbares Objekt ohne Portfoliostruktur (I4) | 6100000000 - 6199999999 | Nur für Demozwecke |
| Anmietvertrag Büroausstattung ICO (SUI2) | Buchungskreisübergreifendes nutzbares Objekt ohne Portfoliostruktur (I2) | 6000000000 - 6099999999 | Nur für Demozwecke |

Zum Konfigurieren von Nummernkreisen und Nutzungsarten verwenden Sie folgende SSCUIs:

- Nummernkreise für generische Mietobjekte definieren (ID: 106591)
- Nutzungsarten für generische Mietobjekte definieren (ID: 106592)

#### Eigentums-ID

Nutzbare Objekte können unterschiedlichen gesetzlichen Kontrollen unterliegen. Die Art der gesetzlichen Kontrolle muss über das Attribut der Eigentums-ID gepflegt werden. Die Merkmalswerte der Eigentums-ID können in der Konfiguration definiert werden.

Die folgenden Eigentums-IDs sind vordefiniert:

- Anmietvertrag (S001)
- Im Eigenbestand (S002)

Um Eigentums-IDs zu konfigurieren, verwenden Sie die SSCUI: Eigentums-IDs für nutzbare Objekte definieren (ID: 106593).

#### Portfolio-ID

Nutzbare Objekte des Nutzungstyps "Nutzbares Objekt ohne Portfoliostruktur (UW)" können nach einer Portfolio-ID gruppiert werden. Die Merkmalswerte der Portfolio-ID können in der Konfiguration definiert werden.

Für die Untergruppierung von Betriebs- und Geschäftsausstattung und Fahrzeugen sind folgende Portfolio-IDs für Demozwecke vordefiniert:

- Dieselfahrzeug (S401)
- Benzinfahrzeug (S402)
- Elektrofahrzeug (S403)
- Bürogeräte (S501)
- Büroeinrichtung (S502)
- Montagelösungen (S503)

Um Portfolio-IDs zu konfigurieren, verwenden Sie die SSCUI: Portfolio-IDs für nutzbare Objekte definieren (ID: 106594).

#### Messungen

Nutzbare und/oder vermietbare Objekte können Bemessungen aufweisen. Basierend auf diesen Bemessungen können Konditionsbeträge in Verträgen berechnet werden. Bemessungen unterschiedlicher Art können zu einer Summenbemessung summiert werden.

Die folgenden Bemessungsarten sind für Demozwecke vordefiniert:

| Bemessungsart | Standardeinheit | Flächengröße | Summenbemessung | Kommentare |
| --- | --- | --- | --- | --- |
| Büro (SG11) | Quadratmeter (M2) | X |  | Aufsummiert auf Nutzfläche (ST99) |
| Meetingbereich (SG13) | Quadratmeter (M2) | X |  | Aufsummiert auf Nutzfläche (ST99) |
| Vorratsraum (SF04) | Quadratmeter (M2) | X |  | Aufsummiert auf Nutzfläche (ST99) |
| Toilette (SD01) | Quadratmeter (M2) | X |  | Aufsummiert auf Nutzfläche (ST99) |
| Technikraum (SC04) | Quadratmeter (M2) | X |  | Aufsummiert auf Nutzfläche (ST99) |
| Aufzug (SA02) | Quadratmeter (M2) | X |  | Aufsummiert auf Nutzfläche (ST99) |
| Korridor (SE01) | Quadratmeter (M2) | X |  | Aufsummiert auf Nutzfläche (ST99) |
| Geschäft (SG22) | Quadratmeter (M2) | X |  | Aufsummiert auf Nutzfläche (ST99) |
| Wohnraum (SG41) | Quadratmeter (M2) | X |  | Aufsummiert auf Nutzfläche (ST99) |
| Eingangsbereich (SE02) | Quadratmeter (M2) | X |  | Aufsummiert auf Nutzfläche (ST99) |
| Parkplatz (SK01) | Quadratmeter (M2) | X |  |  |
| Nutzfläche (ST99) | Quadratmeter (M2) | X | X |  |

Um Bemessungsarten und Summenbemessungen zu konfigurieren, verwenden Sie die folgenden SSCUIs:

- Bemessungsarten definieren (ID: 105394)
- • Summenbemessungen definieren (ID: 105395)

#### Objekttyp und Nummernkreis der Immobilienarchitektur

Generische Mietobjekte des Nutzungstyps "Nutzbares Objekt mit Portfoliostruktur (UP)" oder "Vermietbares Objekt mit Portfoliostruktur (RP)" beziehen sich auf Immobilienarchitekturobjekte, die von einer externen Anwendung über den Stammdatenintegrationsservice auf der BTP (MDI) bereitgestellt werden. Für Synchronisierungszwecke müssen Typen für Immobilienarchitekturobjekte konfiguriert werden. Der Typ des Immobilienarchitekturobjekts bestimmt den Architekturobjekttyp und den verwendeten Nummernkreis im System.

Die folgenden Typen von Immobilienarchitekturobjekten und die entsprechenden Nummernkreise sind zu Demonstrationszwecken vordefiniert:

| Architekturobjekttypen | Architekturobjektkategorie | Nummernkreise | Kommentare |
| --- | --- | --- | --- |
| Standort (S1SI) | Standort (1) | 10000000 - 19999999 |  |
| Gebäude (S2BU) | Gebäude (2) | 20000000 - 29999999 |  |
| Grundstück (S2LA) | Grundstück (3) | 30000000 - 39999999 |  |
| Geschoss (S3FL) | Andere (99) | 40000000 - 49999999 |  |
| Raum (S4RO) | Andere (99) | 50000000 - 59999999 |  |

Um Nummernkreise und Objekttypen der Immobilienarchitektur zu konfigurieren, verwenden Sie die folgenden SSCUIs:

- Nummernkreis für Architekturobjekt definieren (ID: 106628)
- Architekturobjekttyp definieren (ID: 106629)

#### Hierarchie von Immobilienarchitekturobjekten

Basierend auf den Architekturobjekttypen kann eine Hierarchie definiert werden. Diese Hierarchie wird im Reporting verwendet.

Um eine Architekturobjekttyp-Hierarchie zu konfigurieren, verwenden Sie die SSCUI: Zulässige übergeordnete Architekturobjekttypen definieren (ID: 106630).

### Vorbereitende Schritte

#### MDI-Servicebereitschaft validieren

Wenn Sie nutzbare/vermietbare Objekte mit Portfoliostruktur (Nutzungstyp UP und RP, oder I1 und I3) anlegen möchten, ist eine Anbindung zu einer externen Anwendung erforderlich, die Immobilienarchitekturobjekte über den Service Master Data Integration auf der BTP (MDI) bereitstellt.

Einrichtungsanweisungen und Voraussetzungen finden Sie im Umfangsbestandteil 77V – Stammdatenintegration für die Vertrags- und Mietverwaltung.

## Übersichtstabelle

Dieser Umfangsbestandteil umfasst die verschiedenen Prozesse in der folgenden Tabelle:

|  |
| --- |
| Hinweis Wenn Ihr Systemadministrator Bereiche und Seiten auf dem SAP Fiori Launchpad aktiviert hat, enthält die Startseite nur die wesentlichen Apps, mit denen die typischen Aufgaben einer Benutzerrolle ausgeführt werden können.Alle anderen (suchbaren) Apps, die nicht auf der Startseite enthalten sind, finden Sie über die Suchleiste ([2434549](https://me.sap.com/notes/2434549)).Wenn Sie die Startseite personalisieren und versteckte Apps hinzufügen möchten, wechseln Sie in Ihr Benutzerprofil und wählen Sie App Finder. |

| Prozessdiagramm | Benutzerrollen | Transaktion/App | Erwartete Ergebnisse |
| --- | --- | --- | --- |
| [Nutzbares Objekt ohne Portfoliostruktur anlegen](#unique_17) [Seite ] 11 | Sachbearbeiter Vertrag – Leasing oder Sachbearbeiter Immobilien - Standortverwaltung | Nutzbare Objekte verwalten |  |
| [Nutzbares Objekt mit Portfoliostruktur anlegen](#unique_18) [Seite ] 12 | Sachbearbeiter Vertrag – Leasing oder Sachbearbeiter Immobilien - Standortverwaltung | Nutzbare Objekte verwalten |  |
| [Vermietbares Objekt ohne Portfoliostruktur anlegen](#unique_19) [Seite ] 14 | Sachbearbeiter Vertrag – Leasing oder Sachbearbeiter Immobilien - Standortverwaltung | Vermietbares Objekt verwalten |  |
| [Vermietbares Objekt mit Portfoliostruktur ändern](#unique_20) [Seite ] 15 | Sachbearbeiter Vertrag – Leasing oder Sachbearbeiter Immobilien - Standortverwaltung | Vermietbares Objekt verwalten |  |
| [Buchungskreisübergreifendes vermietbares Objekt mit Portfoliostruktur anlegen](#unique_21) [Seite ] 16 | Sachbearbeiter Vertrag – Leasing oder Sachbearbeiter Immobilien - Standortverwaltung | Vermietbares Objekt verwalten |  |
| [Buchungskreisübergreifendes vermietbares Objekt ohne Portfoliostruktur anlegen](#unique_22) [Seite ] 17 | Sachbearbeiter Vertrag – Leasing oder Sachbearbeiter Immobilien - Standortverwaltung | Vermietbares Objekt verwalten |  |
| [Buchungskreisübergreifendes nutzbares Objekt mit Portfoliostruktur anlegen](#unique_23) [Seite ] 18 | Sachbearbeiter Vertrag – Leasing oder Sachbearbeiter Immobilien - Standortverwaltung | Nutzbare Objekte verwalten |  |
| [Buchungskreisübergreifendes nutzbares Objekt ohne Portfoliostruktur anlegen](#unique_24) [Seite ] 20 | Sachbearbeiter Vertrag – Leasing oder Sachbearbeiter Immobilien - Standortverwaltung | Nutzbare Objekte verwalten |  |

## Testverfahren

### Nutzbares Objekt ohne Portfoliostruktur anlegen

| Testschrittnummer | Bezeichnung des Testschritts | Anweisung | Erwartetes Ergebnis | Kommentare |
| --- | --- | --- | --- | --- |
| 1 | Anmelden | Melden Sie sich am SAP Fiori Launchpad als Sachbearbeiter Vertrag – Leasing oder Sachbearbeiter Immobilien - Standortverwaltung an. | Die Startseite wird angezeigt. |  |
| 2 | "Nutzbare Objekte verwalten" öffnen | Öffnen Sie Nutzbare Objekte verwalten. | Sie gelangen auf das Bild Nutzbare Objekte verwalten. |  |
| 3 | Nutzbare Objekte anlegen | Wählen Sie Anlegen, und nehmen Sie die folgenden Einträge vor:Im Abschnitt Kopf:Name des nutzbaren Objekts: <Ihr Objektname>Nutzungstyp: Nutzbares Objekt Objekt ohne Portfoliostruktur (UW)Nutzungsart des nutzbaren Objekts: <Wählen Sie eine Nutzungsart aus, z.B. Fahrzeuge (SU04)>Buchungskreis: <Wählen Sie einen Buchungskreis aus, z.B. Buchungskreis (1010)>Nutzbares Objekt: <Ihre Objekt-ID im Falle eines externen Nummernkreises, andernfalls lassen Sie das Feld leer>Im Abschnitt Allgemeine Informationen:Portfolio-ID (optional): <Wählen Sie eine Portfolio-ID aus, z.B. Dieselfahrzeug (S401)>Berechtigungsgruppe (optional): <Wählen Sie eine Berechtigungsgruppe aus (dieses Feld ist nur sichtbar, wenn eine Berechtigungsgruppe konfiguriert ist)>Eigentums-ID: <Wählen Sie eine Eigentums-ID aus, z.B. Anmietvertrag (S001)>Gültigkeitsbeginn: <Datum, ab dem Ihr Objekt gültig ist, z.B. das aktuelle Datum>Gültigkeitsende: <Datum, bis zu dem Ihr Objekt gültig ist>Wählen Sie im Abschnitt Führendes Kontierungsobjekt die Option Anlegen, und geben Sie Folgendes ein.Objekttyp des zugeordneten Objekts: <Wählen Sie einen Objekttyp aus, z.B. Kostenstelle (KS).>Kontierungsobjekt: <Ihr Kontierungsobjekt>Hinweis Für die gesamte Objektgültigkeit muss ein führendes Kontierungsobjekt zugeordnet sein. Das Kontierungsobjekt kann sich während der Gültigkeit des Objekts ändern. Es dürfen jedoch keine Überschneidungen oder Lücken auftreten. Für nutzbare Objekte, die zur selben Portfolio-ID gehören, können dieselben oder verschiedene führende Kontierungsobjekte verwendet werden. Ein führendes Kontierungsobjekt, das für eine Portfolio-ID verwendet wird, kann nicht als führendes Kontierungsobjekt für eine andere Portfolio-ID verwendet werden.Wählen Sie Übernehmen.Optional:Wählen Sie für den Abschnitt Bemessung die Option Anlegen, und geben Sie folgende Daten ein.Bemessungsart: <Wählen Sie eine Bemessungsart aus.>Betrag: <Betrag der Messung>Wählen Sie Übernehmen.Wählen Sie Anlegen. | Das nutzbare Objekt wird angelegt. |  |

### Nutzbares Objekt mit Portfoliostruktur anlegen

| Testschrittnummer | Bezeichnung des Testschritts | Anweisung | Erwartetes Ergebnis | Kommentare |
| --- | --- | --- | --- | --- |
| 1 | Anmelden | Melden Sie sich am SAP Fiori Launchpad als Sachbearbeiter Vertrag – Leasing oder Sachbearbeiter Immobilien - Standortverwaltung an. | Die Startseite wird angezeigt. |  |
| 2 | "Nutzbare Objekte verwalten" öffnen | Öffnen Sie Nutzbare Objekte verwalten. | Sie gelangen auf das Bild Nutzbare Objekte verwalten. |  |
| 3 | Nutzbare Objekte anlegen | Wählen Sie Anlegen, und nehmen Sie die folgenden Einträge vor:Im Abschnitt Kopf:Name des nutzbaren Objekts: <Ihr Objektname>Nutzungstyp: Nutzbares Objekt mit Portfoliostruktur (UP)Nutzungsart des nutzbaren Objekts: <Wählen Sie eine Nutzungsart aus, z.B. Bürogebäude (SU06)>Buchungskreis: <Wählen Sie einen Buchungskreis aus, z.B. Buchungskreis (1010)>Nutzbares Objekt: <Ihre Objekt-ID im Falle eines externen Nummernkreises, andernfalls lassen Sie das Feld leer>Im Abschnitt Allgemeine Informationen:Gebäude-/Grundstücksobjektnummer: <Wählen Sie das Architekturobjekt (Gebäude/Grundstück) aus, auf das sich das nutzbare Objekt bezieht (übergeordnetes Objekt)>Berechtigungsgruppe (optional): <Wählen Sie eine Berechtigungsgruppe aus (dieses Feld ist nur sichtbar, wenn eine Berechtigungsgruppe konfiguriert ist)>Eigentums-ID: <Wählen Sie eine Eigentums-ID aus, z.B. Anmietvertrag (S001)>Gültigkeitsbeginn: <Datum, ab dem Ihr Objekt gültig ist, z.B. das aktuelle Datum>Gültigkeitsende: <Datum, bis zu dem Ihr Objekt gültig ist>Wählen Sie im Abschnitt Führendes Kontierungsobjekt die Option Anlegen, und geben Sie Folgendes ein.Objekttyp des zugeordneten Objekts: <Wählen Sie einen Objekttyp aus, z.B. Kostenstelle (KS).>Kontierungsobjekt: <Ihr Kontierungsobjekt>Hinweis Für die gesamte Objektgültigkeit muss ein führendes Kontierungsobjekt zugeordnet sein. Das Kontierungsobjekt kann sich während der Gültigkeit des Objekts ändern. Es dürfen jedoch keine Überschneidungen oder Lücken auftreten. Für nutzbare Objekte, die zum selben Gebäude oder Grundstück gehören, können dieselben oder verschiedene führende Kontierungsobjekte verwendet werden. Ein führendes Kontierungsobjekt, das für ein Gebäude oder Grundstück verwendet wird, kann nicht als führendes Kontierungsobjekt für ein anderes Gebäude oder Grundstück verwendet werden.Wählen Sie Übernehmen.Wählen Sie im Abschnitt Architekturobjektnutzung die Option Anlegen, und geben Sie Folgendes ein.Hinweis Für nutzbare Objekte muss der Service SAP Master Data Integration auf BTP (MDI) verwendet werden, um die Beziehung zu Immobilienarchitekturobjekten herzustellen, die von einer externen Anwendung bereitgestellt werden.Architekturobjekttyp: <Wählen Sie den Architekturobjekttyp aus, z.B. Gebäude (S2BU)>Architekturobjektnummer: <Wählen Sie das Architekturobjekt aus, das durch das nutzbare Objekt dargestellt wird.>Hinweis Sie können mehrere Immobilienarchitekturobjekte zu einem nutzbaren Objekt zusammenfassen.Optional:Wählen Sie im Abschnitt Systemstatus die Option Für buchungskreisübergreifende Einrichtung sperren, wenn Sie verhindern möchten, dass die aus einer externen Immobilienverwaltungslösung synchronisierten vermietbaren Objekte (RP) automatisch nutzbaren Objekten zugeordnet werden, solange Ihre buchungskreisübergreifende Einrichtung noch nicht abgeschlossen ist.Ihr nutzbares Objekt hat den Status Nur Intercompany Vermietung, der eine externe Vermietung verhindert.Wählen Sie Für buchungskreisübergreifende Einrichtung entsperren, nachdem Sie die buchungskreisübergreifende Einrichtung abgeschlossen haben.Wählen Sie für den Abschnitt Bemessung die Option Anlegen, und geben Sie folgende Daten ein.Bemessungsart: <Wählen Sie eine Bemessungsart aus.>Betrag: <Betrag der Messung>Wählen Sie Übernehmen.Wählen Sie Anlegen. | Das nutzbare Objekt wird angelegt. |  |

### Vermietbares Objekt ohne Portfoliostruktur anlegen

| Testschrittnummer | Bezeichnung des Testschritts | Anweisung | Erwartetes Ergebnis | Kommentare |
| --- | --- | --- | --- | --- |
| 1 | Anmelden | Melden Sie sich am SAP Fiori Launchpad als Sachbearbeiter Vertrag – Leasing oder Sachbearbeiter Immobilien - Standortverwaltung an. | Die Startseite wird angezeigt. |  |
| 2 | "Vermietbares Objekt verwalten" öffnen | Öffnen Sie Vermietbares Objekt verwalten. | Sie gelangen auf das Bild Vermietbare Objekte verwalten. |  |
| 3 | Vermietbare Objekte anlegen | Wählen Sie Anlegen, und nehmen Sie die folgenden Einträge vor:Im Abschnitt Kopf:Name des vermietbaren Objekts: <Ihr Objektname>Nutzungstyp: Vermietbares Objekt ohne Portfoliostruktur (RW)Nutzungsart des vermietbaren Objekts: <Wählen Sie eine Nutzungsart aus, z.B. Fahrzeuge (SR04)>Buchungskreis: <Wählen Sie einen Buchungskreis aus, z.B. Buchungskreis (1010)>Vermietbares Objekt: <Ihre Objekt-ID im Falle eines externen Nummernkreises, andernfalls lassen Sie das Feld leer>Im Abschnitt Allgemeine Informationen:Kategorie des vermietbaren Objekts: <Wählen Sie eine vermietbare Objektkategorie aus, z.B. Extern (E)>Berechtigungsgruppe (optional): <Wählen Sie eine Berechtigungsgruppe aus (dieses Feld ist nur sichtbar, wenn eine Berechtigungsgruppe konfiguriert ist)>Gültigkeitsbeginn: <Datum, ab dem Ihr Objekt gültig ist, z.B. das aktuelle Datum>Gültigkeitsende: <Datum, bis zu dem Ihr Objekt gültig ist>Wählen Sie im Abschnitt Zuordnung des nutzbaren Objekts die Option Anlegen, und geben Sie Folgendes ein.Nutzbares Objekt: <Ordnen Sie das nutzbare Objekt zu, auf das sich das vermietbare Objekt bezieht.>Wählen Sie Übernehmen.Optional:Wählen Sie für den Abschnitt Bemessung die Option Anlegen, und geben Sie folgende Daten ein.Bemessungsart: <Wählen Sie eine Bemessungsart aus.>Betrag: <Betrag der Messung>Wählen Sie Übernehmen.Wählen Sie Anlegen. | Das vermietbare Objekt wird angelegt. |  |

### Vermietbares Objekt mit Portfoliostruktur ändern

| Testschrittnummer | Bezeichnung des Testschritts | Anweisung | Erwartetes Ergebnis | Kommentare |
| --- | --- | --- | --- | --- |
| 1 | Anmelden | Melden Sie sich am SAP Fiori Launchpad als Sachbearbeiter Vertrag – Leasing oder Sachbearbeiter Immobilien - Standortverwaltung an. | Die Startseite wird angezeigt. |  |
| 2 | "Vermietbares Objekt verwalten" öffnen | Öffnen Sie Vermietbares Objekt verwalten. | Sie gelangen auf das Bild Vermietbare Objekte verwalten. |  |
| 3 | Vermietbare Objekte ändern | Suchen Sie das vermietbare Objekt anhand der Objekt-ID.Wählen Sie das vermietbare Objekt aus. Wählen Sie Bearbeiten, und geben Sie Folgendes ein:Im Abschnitt Allgemeine Informationen:Berechtigungsgruppe (optional): <Wählen Sie eine Berechtigungsgruppe aus (dieses Feld ist nur sichtbar, wenn eine Berechtigungsgruppe konfiguriert ist)>Im Abschnitt Zuordnung des nutzbaren Objekts kann der folgende Eintrag angelegt oder gepflegt werden:Nutzbares Objekt: <Ordnen Sie das nutzbare Objekt zu, auf das sich das vermietbare Objekt bezieht.>Hinweis Beachten Sie, dass es hier nur eine Zuordnung geben kann.Wählen Sie Übernehmen.Optional:Im Abschnitt Messung kann der folgende Eintrag angelegt oder gepflegt werden:Bemessungsart: <Wählen Sie eine Bemessungsart aus.>Betrag: <Betrag der Messung>Wählen Sie Übernehmen.Wählen Sie Sichern. | Das vermietbare Objekt wird geändert. |  |

### Buchungskreisübergreifendes vermietbares Objekt mit Portfoliostruktur anlegen

| Testschrittnummer | Bezeichnung des Testschritts | Anweisungen | Erwartetes Ergebnis | Kommentare |
| --- | --- | --- | --- | --- |
| 1 | Anmelden | Melden Sie sich am SAP Fiori Launchpad als Sachbearbeiter Vertrag – Leasing oder Sachbearbeiter Immobilien - Standortverwaltung an. | Die Startseite wird angezeigt. |  |
| 2 | "Vermietbares Objekt verwalten" öffnen | Öffnen Sie Vermietbares Objekt verwalten. | Sie gelangen auf das Bild Vermietbare Objekte verwalten. |  |
| 3 | Vermietbare Objekte anlegen | Wählen Sie Anlegen, und nehmen Sie die folgenden Einträge vor:Im Abschnitt Kopf:Name des vermietbaren Objekts: <Ihr Objektname>Nutzungstyp: Buchungskreisübergreifendes vermietbares Objekt mit Portfoliostruktur (I3)Nutzungsart des vermietbaren Objekts: <Wählen Sie eine Nutzungsart aus, z.B. Mietvertrag Büro ICO (SRI1)>Buchungskreis: <Wählen Sie einen Buchungskreis aus, z.B. Buchungskreis (1010)>Vermietbares Objekt: <Ihre Objekt-ID im Falle eines externen Nummernkreises, andernfalls lassen Sie das Feld leer>Im Abschnitt Allgemeine Informationen:obligatorische Gebäude-/Grundstücksobjektnummer:Gebäude-/Grundstücksobjektnummer: <Wählen Sie das Architekturobjekt (Gebäude/Grundstück) aus, auf das sich das buchungskreisübergreifende vermietbare Objekt bezieht (übergeordnetes Objekt)>Berechtigungsgruppe (optional): <Wählen Sie eine Berechtigungsgruppe aus (dieses Feld ist nur sichtbar, wenn eine Berechtigungsgruppe konfiguriert ist)>Gültigkeitsbeginn: <Datum, ab dem Ihr Objekt gültig ist, z.B. das aktuelle Datum>Gültigkeitsende: <Datum, bis zu dem Ihr Objekt gültig ist>Geben Sie im Abschnitt Zuordnung des nutzbaren Objekts Folgendes ein:Nutzbares Objekt: <Ordnen Sie das nutzbare Objekt einem buchungskreisübergreifenden nutzbaren Objekt (I1) oder einem nicht buchungskreisübergreifenden nutzbaren Objekt (UP) zu, auf das sich das buchungskreisübergreifende vermietbare Objekt bezieht>Wählen Sie Übernehmen.Wählen Sie im Abschnitt Architekturobjektnutzung die Option Anlegen, und geben Sie Folgendes ein.Architekturobjekttyp: <Wählen Sie den Architekturobjekttyp aus, z.B. Raum (S4RO)>Architekturobjektnummer: <Wählen Sie das Architekturobjekt aus, das durch das nutzbare Objekt dargestellt wird.>Bemessungsbasierte Nutzung: <Vorschlagswert, ja>Wählen Sie oben rechts Vollbildmodus aktivieren. Wählen Sie unter Architekturnutzungsbemessung die Option Anlegen, und geben Sie Folgendes ein.Bemessungsart: <Ihre Bemessungsart>, z.B. Büro (SG11)Betrag: <Ihr Betrag>Gültigkeitsbeginn: <Datum, ab dem Ihr Objekt gültig ist>Gültigkeitsende: <Datum, bis zu dem Ihr Objekt gültig ist>Wählen Sie Übernehmen.Wählen Sie Anlegen. | Das vermietbare Objekt wird angelegt. |  |

### Buchungskreisübergreifendes vermietbares Objekt ohne Portfoliostruktur anlegen

| Testschrittnummer | Bezeichnung des Testschritts | Anweisung | Erwartetes Ergebnis | Kommentare |
| --- | --- | --- | --- | --- |
| 1 | Anmelden | Melden Sie sich am SAP Fiori Launchpad als Sachbearbeiter Vertrag – Leasing oder Sachbearbeiter Immobilien - Standortverwaltung an. | Die Startseite wird angezeigt. |  |
| 2 | "Vermietbares Objekt verwalten" öffnen | Öffnen Sie Vermietbares Objekt verwalten. | Sie gelangen auf das Bild Vermietbare Objekte verwalten. |  |
| 3 | Vermietbare Objekte anlegen | Wählen Sie Anlegen, und nehmen Sie die folgenden Einträge vor:Im Abschnitt Kopf:Name des vermietbaren Objekts: <Ihr Objektname>Nutzungstyp: Buchungskreisübergreifendes vermietbares Objekt ohne Portfoliostruktur (I4)Nutzungsart des vermietbaren Objekts: <Wählen Sie eine Nutzungsart aus, z.B. Mietvertrag Büroausstattung ICO (SRI2)>Buchungskreis: <Wählen Sie einen Buchungskreis aus, z.B. Buchungskreis (1010)>Vermietbares Objekt: <Ihre Objekt-ID im Falle eines externen Nummernkreises, andernfalls lassen Sie das Feld leer>Im Abschnitt Allgemeine Informationen:Berechtigungsgruppe (optional): <Wählen Sie eine Berechtigungsgruppe aus (dieses Feld ist nur sichtbar, wenn eine Berechtigungsgruppe konfiguriert ist)>Gültigkeitsbeginn: <Datum, ab dem Ihr Objekt gültig ist, z.B. das aktuelle Datum>Gültigkeitsende: <Datum, bis zu dem Ihr Objekt gültig ist>Wählen Sie im Abschnitt Zuordnung des nutzbaren Objekts die Option Anlegen, und geben Sie Folgendes ein.Nutzbares Objekt: <Ordnen Sie das nutzbare Objekt einem buchungskreisübergreifenden nutzbaren Objekt (I2) oder einem nicht buchungskreisübergreifenden nutzbaren Objekt (UW) zu, auf das sich das buchungskreisübergreifende vermietbare Objekt bezieht>Wählen Sie Übernehmen.Optional:Wählen Sie für den Abschnitt Bemessung die Option Anlegen, und geben Sie folgende Daten ein.Bemessungsart: <Wählen Sie eine Bemessungsart aus.>Betrag: <Betrag der Messung>Wählen Sie Übernehmen.Wählen Sie Anlegen. | Das vermietbare Objekt wird angelegt. |  |

### Buchungskreisübergreifendes nutzbares Objekt mit Portfoliostruktur anlegen

| Testschrittnummer | Bezeichnung des Testschritts | Anweisung | Erwartetes Ergebnis | Kommentare |
| --- | --- | --- | --- | --- |
| 1 | Anmelden | Melden Sie sich am SAP Fiori Launchpad als Sachbearbeiter Vertrag – Leasing oder Sachbearbeiter Immobilien - Standortverwaltung an. | Die Startseite wird angezeigt. |  |
| 2 | "Nutzbare Objekte verwalten" öffnen | Öffnen Sie Nutzbare Objekte verwalten. | Sie gelangen auf das Bild Nutzbare Objekte verwalten. |  |
| 3 | Nutzbare Objekte anlegen | Wählen Sie Anlegen, und nehmen Sie die folgenden Einträge vor:Im Abschnitt Kopf:Name des nutzbaren Objekts: <Ihr Objektname>Nutzungstyp: Buchungskreisübergreifendes nutzbares Objekt mit Portfoliostruktur (I1)Nutzungsart des nutzbaren Objekts: <Wählen Sie eine Nutzungsart aus, z.B. Anmietvertrag Büro ICO (SUI1)>Buchungskreis: <Wählen Sie einen Buchungskreis aus, z.B. Buchungskreis (1020)>Nutzbares Objekt: <Ihre Objekt-ID im Falle eines externen Nummernkreises, andernfalls lassen Sie das Feld leer>Im Abschnitt Allgemeine Informationen:Gebäude-/Grundstücksobjektnummer: <Wählen Sie das Architekturobjekt (Gebäude/Grundstück) aus, auf das sich das buchungskreisübergreifende nutzbare Objekt bezieht (übergeordnetes Objekt).>Berechtigungsgruppe (optional): <Wählen Sie eine Berechtigungsgruppe aus (dieses Feld ist nur sichtbar, wenn eine Berechtigungsgruppe konfiguriert ist)>Hinweis Der Gültigkeitsbeginn und das Gültigkeitsende werden anhand des zugeordneten buchungskreisübergreifenden vermietbaren Objekts ermittelt.Wählen Sie im Abschnitt Führendes Kontierungsobjekt die Option Anlegen, und geben Sie Folgendes ein.Objekttyp des zugeordneten Objekts: <Wählen Sie einen Objekttyp aus, z.B. Kostenstelle (KS).>Kontierungsobjekt: <Ihr Kontierungsobjekt>Hinweis Für die gesamte Objektgültigkeit muss ein führendes Kontierungsobjekt zugeordnet sein. Das Kontierungsobjekt kann sich während der Gültigkeit des Objekts ändern. Es dürfen jedoch keine Überschneidungen oder Lücken auftreten. Für nutzbare Objekte, die zum selben Gebäude oder Grundstück gehören, können dieselben oder verschiedene führende Kontierungsobjekte verwendet werden. Ein führendes Kontierungsobjekt, das für ein Gebäude oder Grundstück verwendet wird, kann nicht als führendes Kontierungsobjekt für ein anderes Gebäude oder Grundstück verwendet werden.Wählen Sie Übernehmen.Wählen Sie im Abschnitt Zuordnung des buchungskreisübergreifenden vermietbaren Objekts die Option Anlegen, und geben Sie Folgendes ein.Buchungskreisübergreifendes vermietbares Objekt: <Ordnen Sie das buchungskreisübergreifende vermietbare Objekt zu, auf das sich das buchungskreisübergreifende nutzbare Objekt bezieht.>Wählen Sie Übernehmen.Hinweis Der Umfang der buchungskreisübergreifenden Anmietung ist auf den Umfang der Vermietung durch das verbundene Unternehmen beschränkt. Es muss ein buchungskreisübergreifendes vermietbares Objekt aus dem Buchungskreis des Vermieters zugeordnet werden.Optional:Wählen Sie im Abschnitt Systemstatus die Option Für buchungskreisübergreifende Einrichtung sperren, wenn Sie verhindern möchten, dass die aus einer externen Immobilienverwaltungslösung synchronisierten vermietbaren Objekte (RP) automatisch nutzbaren Objekten zugeordnet werden, solange Ihre buchungskreisübergreifende Einrichtung noch nicht abgeschlossen ist.Ihr unternehmensübergreifendes nutzbares Objekt hat den Status Nur Intercompany Vermietung, der eine externe Vermietung verhindert.Wählen Sie Für buchungskreisübergreifende Einrichtung entsperren, nachdem Sie die buchungskreisübergreifende Einrichtung abgeschlossen haben.Wählen Sie für den Abschnitt Bemessung die Option Anlegen, und geben Sie folgende Daten ein.Bemessungsart: <Wählen Sie eine Bemessungsart aus.>Betrag: <Betrag der Messung>Wählen Sie Übernehmen.Wählen Sie Anlegen. | Das nutzbare Objekt wird angelegt. |  |

### Buchungskreisübergreifendes nutzbares Objekt ohne Portfoliostruktur anlegen

| Testschrittnummer | Bezeichnung des Testschritts | Anweisung | Erwartetes Ergebnis | Kommentare |
| --- | --- | --- | --- | --- |
| 1 | Anmelden | Melden Sie sich am SAP Fiori Launchpad als Sachbearbeiter Vertrag – Leasing oder Sachbearbeiter Immobilien - Standortverwaltung an. | Die Startseite wird angezeigt. |  |
| 2 | "Nutzbare Objekte verwalten" öffnen | Öffnen Sie Nutzbare Objekte verwalten. | Sie gelangen auf das Bild Nutzbare Objekte verwalten. |  |
| 3 | Nutzbare Objekte anlegen | Wählen Sie Anlegen, und nehmen Sie die folgenden Einträge vor:Im Abschnitt Kopf:Name des nutzbaren Objekts: <Ihr Objektname>Nutzungstyp: Buchungskreisübergreifendes nutzbares Objekt ohne Portfoliostruktur (I2)Nutzungsart des nutzbaren Objekts: <Wählen Sie eine Nutzungsart aus, z.B. Anmietvertrag Büroausstattung ICO (SUI2)>Buchungskreis: <Wählen Sie einen Buchungskreis aus, z.B. Buchungskreis (1020)>Nutzbares Objekt: <Ihre Objekt-ID im Falle eines externen Nummernkreises, andernfalls lassen Sie das Feld leer>Im Abschnitt Allgemeine Informationen:Portfolio-ID (optional): <Wählen Sie eine Portfolio-ID aus, z.B. Bürogeräte (S501)>Berechtigungsgruppe (optional): <Wählen Sie eine Berechtigungsgruppe aus (dieses Feld ist nur sichtbar, wenn eine Berechtigungsgruppe konfiguriert ist)>Hinweis Der Gültigkeitsbeginn und das Gültigkeitsende werden anhand des zugeordneten buchungskreisübergreifenden vermietbaren Objekts ermittelt.Wählen Sie im Abschnitt Führendes Kontierungsobjekt die Option Anlegen, und geben Sie Folgendes ein.Objekttyp des zugeordneten Objekts: <Wählen Sie einen Objekttyp aus, z.B. Kostenstelle (KS).>Kontierungsobjekt: <Ihr Kontierungsobjekt>Hinweis Für die gesamte Objektgültigkeit muss ein führendes Kontierungsobjekt zugeordnet sein. Das Kontierungsobjekt kann sich während der Gültigkeit des Objekts ändern. Es dürfen jedoch keine Überschneidungen oder Lücken auftreten. Für nutzbare Objekte, die zum selben Gebäude oder Grundstück gehören, können dieselben oder verschiedene führende Kontierungsobjekte verwendet werden. Ein führendes Kontierungsobjekt, das für ein Gebäude oder Grundstück verwendet wird, kann nicht als führendes Kontierungsobjekt für ein anderes Gebäude oder Grundstück verwendet werden.Wählen Sie Übernehmen.Wählen Sie im Abschnitt Zuordnung des buchungskreisübergreifenden vermietbaren Objekts die Option Anlegen, und geben Sie Folgendes ein.Buchungskreisübergreifendes vermietbares Objekt: <Ordnen Sie das buchungskreisübergreifende vermietbare Objekt zu, auf das sich das buchungskreisübergreifende nutzbare Objekt bezieht.>Hinweis Der Umfang der buchungskreisübergreifenden Anmietung ist auf den Umfang der Vermietung durch das verbundene Unternehmen beschränkt. Es muss ein buchungskreisübergreifendes vermietbares Objekt aus dem Buchungskreis des Vermieters zugeordnet werden.Wählen Sie Übernehmen.Optional:Wählen Sie für den Abschnitt Bemessung die Option Anlegen, und geben Sie folgende Daten ein.Bemessungsart: <Wählen Sie eine Bemessungsart aus.>Betrag: <Betrag der Messung>Wählen Sie Übernehmen.Wählen Sie Anlegen. | Das nutzbare Objekt wird angelegt. |  |

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
- related-to :: [[17-leasing-and-real-estate/create-rental-object-master-data-script-7ad-521]]
- related-to :: [[17-leasing-and-real-estate/sap-s-4hana-cloud-public-edition-mds-7ad-523]]
- related-to :: [[17-leasing-and-real-estate/sap-s-4hana-cloud-public-edition-mds-7ad-525]]
- related-to :: [[17-leasing-and-real-estate/script-de-dados-mestre-criar-objeto-de-locacao-mds-7ad-524]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/7AD_S4CLD2608_Master_Data_DE_XX.docx` — full document · extracted with `mammoth` · 44,647 chars in the whole document
