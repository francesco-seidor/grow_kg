---
id: 08-sales-order-management/stammdatenskript-kundenhierarchiestammdatenskript-anlegen-6n3-514
title: "Stammdatenskript: Kundenhierarchiestammdatenskript anlegen (6N3) (6N3_S4CLD2608_Master_Data_DE_XX)"
description: "German master data test script (6N3) for SAP S/4HANA Cloud Public Edition 2608: create customer master data (general, company code, sales area) and customer hierarchies."
cluster: 08-sales-order-management
tags: [kb/sales-order-management, topic/customer-hierarchies]
aliases: [6N3_S4CLD2608_Master_Data_DE_XX]
keywords: [Customer Hierarchies, customer master data, company code data, sales area data, business partner roles, partner roles, tax numbers, test procedures, organizational units, country-specific requirements]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/6N3_S4CLD2608_Master_Data_DE_XX.docx]
confidence: high
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-514
topic: 08-sales-order-management/customer-hierarchies
language: DE
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Stammdatenskript: Kundenhierarchiestammdatenskript anlegen (6N3) (6N3_S4CLD2608_Master_Data_DE_XX)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/6N3_S4CLD2608_Master_Data_DE_XX.docx`, extracted with `mammoth`. Grouped under **Customer Hierarchies** in Sales Order Management. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

| <!-- image omitted: unnamed --> | StammdatenskriptSAP S/4HANA Cloud Public Edition - 02-07-26 |
| --- | --- |
|  | Kundenhierarchiestammdatenskript anlegen (6N3) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Inhaltsverzeichnis

[1 Zweck 2](#_Toc233889858)

[2 Voraussetzungen 3](#_Toc233889859)

[2.1 Systemzugriff 3](#_Toc233889860)

[2.2 Rollen 3](#_Toc233889861)

[2.3 Erforderliche Organisationseinheiten 3](#_Toc233889862)

[2.4 Obligatorische und optionale Stammdaten 4](#_Toc233889863)

[3 Übersichtstabelle 5](#_Toc233889864)

[4 Testverfahren 6](#_Toc233889865)

[4.1 Kundenstammdaten anlegen: Allgemeine Daten 6](#_Toc233889866)

[4.2 Kundenstammdaten anlegen - Buchungskreisdaten 13](#_Toc233889867)

[4.3 Kundenstammdaten anlegen - Vertriebsbereichsdaten 18](#_Toc233889868)

[4.4 Kundenhierarchien anlegen 24](#_Toc233889869)

## Zweck

Mit der App Kundenhierarchien verwalten können Sie Kundenhierarchien anlegen, kopieren, bearbeiten und löschen sowie mehrere Ebenen von Hierarchieknoten zuordnen. Sie können auch die Gültigkeitszeiträume der Hierarchien verwalten, und eine Hierarchie wird nur in diesem angegebenen Zeitraum für Prozesse berücksichtigt.

Kundenhierarchie – Analyse: Sie verwenden diese Hierarchieart in Verkaufsanalysen, um Bewegungsdaten zu projizieren und aufschlussreiche Informationen zu erhalten.

Kundenhierarchie - Vertrieb: Sie verwenden diesen Hiearchieart für die Preisfindung in Verkaufsbelegen und Fakturen. Diese Hierarchie enthält Kundeninformationen, die zum selben Vertriebsbereich gehören. Das System ermöglicht es Ihnen, Textknoten hinzuzufügen, die jede Art von Informationen wie Bundesland, Bezirk usw. bezeichnen können, damit Sie die Hierarchie besser organisieren können. Darüber hinaus können diese Textknoten als preisfindungsrelevant gepflegt werden. Die Hierarchie enthält auch Geschäftspartnerknoten, denen ein Kundenvertriebsbereich zugeordnet sein muss.

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
| Stammdatenexperte – Geschäftspartnerdaten | SAP_BR_BUPA_MASTER_SPECIALIST | Stammdaten – Geschäftspartner / Geschäftspartner-Governance / Geschäftspartner-Governance / Geschäftspartner-Governance | SAP_BR_BUPA_MASTER_SPECIALIST / SAP_CA_SPT_MDG_BP_GOV_PC / SAP_CMD_SPT_BP_GOV_PC / SAP_CA_SPT_MDG_BP_WFUSR_PC |  |

### Erforderliche Organisationseinheiten

Die erforderlichen Organisationseinheiten sind im Folgenden aufgeführt:

| Datensegment | Hängt ab von | Feldbeispiele | Kommentare | Zu verwendende Organisationseinheit |
| --- | --- | --- | --- | --- |
| Grunddaten | Unabhängig von Organisationeinheiten | Geschäftspartnerbeschreibung, Kundennummer, Preisfindungsrelevant usw. | Grunddaten sind für einen Materialstammsatz nur einmal vorhanden. | Nicht zutreffend |
| Verkaufsdaten | Verkaufsorganisation, Vertriebsweg und Sparte | Steuerdaten, Preisfindungsrelevant usw. | Verkaufsdaten können für jede Verkaufsorganisation Ihrer Unternehmensstruktur vorhanden sein, für die der Geschäftspartner-Stammdatensatz verwendet wird. | VerkaufsorganisationVertriebswegSparte |

### Obligatorische und optionale Stammdaten

Geschäftspartner-Stammdatensätze können auf andere Stammdaten verweisen. Die folgende Tabelle bietet eine Übersicht über die obligatorischen und optionalen Stammdatenobjekte, die in einem Geschäftspartner-Stammdatensatz verwendet werden müssen.

| Stammdatenobjekt | Verwendet im Datensegment | Obligatorisch / optional | Kommentare |
| --- | --- | --- | --- |
| Vertriebsbereich |  | obligatorisch | Die Zuordnung eines Vertriebsbereichs zu Geschäftspartner-Stammdaten ist für die Kundenhierarchie obligatorisch. |

## Übersichtstabelle

Dieser Umfangsbestandteil umfasst mehrere Prozessschritte, die in der folgenden Tabelle aufgelistet sind:

|  |
| --- |
| Hinweis Wenn Ihr Systemadministrator Bereiche und Seiten auf dem SAP Fiori Launchpad aktiviert hat, enthält die Startseite nur die wesentlichen Apps, mit denen die typischen Aufgaben einer Benutzerrolle ausgeführt werden können.Alle anderen (suchbaren) Apps, die nicht auf der Startseite enthalten sind, finden Sie über die Suchleiste ([2434549](https://me.sap.com/notes/2434549)).Wenn Sie die Startseite personalisieren und versteckte Apps hinzufügen möchten, wechseln Sie in Ihr Benutzerprofil und wählen Sie App Finder. |

| Prozessschritt | Anwendungsrolle | App/Vorgang | Erwartete Ergebnisse |
| --- | --- | --- | --- |
| [Kundenstammdaten anlegen: Allgemeine Daten](#unique_8) [Seite ] 6 | Stammdatenexperte – Geschäftspartnerdaten | Geschäftspartner pflegen(BP) oder Kundenstammdaten verwalten(F0850A) | Kundenstamm – Allgemeine Daten werden angelegt. |
| [Kundenstammdaten anlegen - Buchungskreisdaten](#unique_9) [Seite ] 13 | Stammdatenexperte – Geschäftspartnerdaten | Geschäftspartner pflegen(BP) oder Kundenstammdaten verwalten(F0850A) | Kundenstamm – Buchungskreisdaten werden angelegt. |
| [Kundenstammdaten anlegen - Vertriebsbereichsdaten](#unique_10) [Seite ] 18 | Stammdatenexperte – Geschäftspartnerdaten | Geschäftspartner pflegen(BP) oder Kundenstammdaten verwalten(F0850A) | Kundenstamm – Vertriebsbereichsdaten werden angelegt. |
| [Kundenhierarchien anlegen](#unique_11) [Seite ] 24 | Stammdatenexperte – Geschäftspartnerdaten | Kundenhierarchien verwalten(F5794) | Die Kundenhierarchien werden angelegt. |

## Testverfahren

In diesem Abschnitt werden die Testverfahren für den jeweiligen Prozessschritt beschrieben, der zum betreffenden Umfangsbestandteil gehört.

### Kundenstammdaten anlegen: Allgemeine Daten

Testverwaltung

Kundenprojekt: Füllen Sie die projektbezogenen Teile aus.

|  |  |  |  |
| --- | --- | --- | --- |
| Testfall-ID | <X.XX> | Testdatum: |  |
| Testername: |  | Dauer: |  |
| Benutzerrolle(n): |  | Zuständigkeit: | <Geben Sie den Serviceanbieter, einen Kunden oder einen Serviceanbieter zusammen mit einem Kunden an.> |

Zweck

In diesem Verfahren erhalten Sie eine Anleitung zum Anlegen von Kundenstammdaten. Die zur Verfügung stehenden Apps hängen von der Ihnen zugeordneten Rolle ab. Daher werden zwei Optionen bereitgestellt.

Der folgende Hinweis gilt nur für Saudi-Arabien.

|  |
| --- |
| Hinweis Um die ZATCA-E-Rechnungsvorschriften einzuhalten, stellen Sie sicher, dass alle erforderlichen Felder wie Straße 2, Straße 3, Bezirk usw. korrekt in die Geschäftspartnerformulare eingegeben wurden, bevor Sie E-Belege generieren. Dies ist für die erfolgreiche Prüfung von E-Rechnungen erforderlich, bevor sie an das Portal der Steuerbehörde gesendet werden.Diese Informationen werden verwendet, um je nach Art des E-Belegs die entsprechenden XML-Tags gemäß den Anforderungen von ZATCA zu füllen. Weitere Informationen zu den Richtlinien von ZATCA finden Sie in den XML-Implementierungsstandardrichtlinien für elektronische Rechnungen. |

Vorgehensweise: Option 1 – Geschäftspartner bearbeiten

Folgen Sie dieser Vorgehensweise, wenn Sie mit Ihrer Benutzerrolle auf die App Geschäftspartner pflegen(BP) zugreifen können.

| Testschrittnummer | Bezeichnung des Testschritts | Anweisungen | Erwartetes Ergebnis | Bestanden/Nicht bestanden/Anmerkung |
| --- | --- | --- | --- | --- |
| 1 | Anmelden | Melden Sie sich am SAP Fiori Launchpad als Stammdatenexperte – Geschäftspartnerdaten an. | Das SAP Fiori Launchpad wird angezeigt. |  |
| 2 | SAP-Fiori-App aufrufen | Öffnen Sie Geschäftspartner pflegen(BP). | Die App wird geöffnet. |  |
| 3 | Geschäftspartnerorganisation anlegen | Wählen Sie Organisation. | Das Bild Organisation anlegen wird angezeigt. |  |
| 4 | Allgemeine Daten eingeben | Tragen Sie Folgendes ein:Geschäftspartner: <Geben Sie eine mit einem Buchstaben beginnende Geschäftspartner-ID ein.>Gruppierung: Wählen Sie z.B. Externe alphanumerische Nummerierung.Das Feld Anlegen in GP-Rolle wird vom System mit der Rolle GPartner allgemein ausgefüllt. Behalten Sie diese Einstellung bei.Drücken Sie Enter.Hinweis Weitere Informationen zu den Details allgemeiner Daten finden Sie im Abschnitt [Voraussetzungen](#unique_2) [Seite ] 3. |  |  |
| 5 | Adressdaten eingeben | Geben Sie auf der Registerkarte Adresse im Bereich Name die folgenden Daten ein:Titel: <Wählen Sie einen Titel aus.>Name: <Name> |  |  |
| 6 | Adressdaten eingeben | Geben Sie im Abschnitt Standardadresse die Adresse ein. |  |  |
| 7 | Zeit- und Transportzone eingeben | Wählen Sie im Abschnitt Straßenadresse die Option Weitere Felder. Geben Sie folgende Daten ein:Zeitzone: <Zeitzone>Transportzone <Transportzone> |  |  |
| Nur für Thailand | Zusätzliche Adressdaten eingeben (nur für Thailand) | Wählen Sie im Abschnitt Straßenadresse die Option Mehr, und geben Sie folgende Daten ein:Gebäudekürzel: <Gebäude>Raum: <Raumnummer>Etage: <Etagennummer>Straße 2: <Moo>Straße 3: <SOI/Lane>Straße: <Straße>Hausnummer: <Nr.>Anderer Ort: <Unterbezirk>Ortsteil: <Ortsteil/Abschnitt>Ort: <Provinz>Postleitzahl: <Postleitzahl>Telefon: <Telefonnummer> |  |  |
| 8 | Suchbegriffe eingeben | Geben Sie auf der Registerkarte Adresse im Abschnitt Suchbegriffe einen oder mehrere Suchbegriffe für den Geschäftspartner ein. |  |  |
| 9 | Kommunikationsdaten eingeben | Wählen Sie im Abschnitt Kommunikation im Feld Sprache die bevorzugte Sprache des Geschäftspartners. |  |  |
| Nur für Japan | Branchendaten eingeben (nur für Japan) | Wählen Sie auf der Registerkarte Identifikation im Abschnitt Branchen die Option Alle Branchensysteme. Geben Sie folgende Daten ein:Branchensystem: Wählen Sie Bank of Japan.Branche: <Wählen Sie eine Branchennummer aus.>Standardbranche: <nicht markiert> |  |  |
| 10 | Steuernummern eingeben | Geben Sie auf der Registerkarte Identifikation im Abschnitt Steuernummern die folgenden Daten ein:Kategorie: <Kategorie>Steuernummer: <Steuernummer>Hinweis Wählen Sie die richtige Kategorie für das Land/die Region des Geschäftspartners aus. Pflegen Sie zum Beispiel für einen deutschen Geschäftspartner mindestens einen Wert für die Kategorie DE1, die für die allgemein verwendete Umsatzsteuernummer steht (Umsatzsteuer-Identifikationsnummer). |  |  |
| 11 | Bankkonten eingeben | Geben Sie auf der Registerkarte Zahlungsverkehr im Abschnitt Bankverbindung die folgenden Daten ein:Bankschlüssel: <Bankschlüssel>Bankkonto <Bankkonto>Achtung Bankschlüssel müssen zuvor definiert werden. Weitere Informationen zu zulässigen Einträgen in diesem Feld finden Sie in der Eingabehilfe. |  |  |
| 12 | Daten sichern | Sichern Sie Ihre Eingaben. | Ihre Daten werden gesichert. |  |

Vorgehensweise: Option 2 – Kundenstammdaten verwalten

Folgen Sie dieser Vorgehensweise, wenn Sie mit Ihrer Benutzerrolle auf die App Kundenstammdaten verwalten(F0850A) zugreifen können.

| Testschrittnummer | Bezeichnung des Testschritts | Anweisungen | Erwartetes Ergebnis | Kommentare |
| --- | --- | --- | --- | --- |
| 1 | Anmelden | Melden Sie sich am SAP Fiori Launchpad als Stammdatenexperte – Geschäftspartnerdaten an. | Das SAP Fiori Launchpad wird angezeigt. |  |
| 2 | SAP-Fiori-App aufrufen | Öffnen Sie Kundenstammdaten verwalten(F0850A). | Die App wird geöffnet. |  |
| 3 | Neue Organisation anlegen | Wählen Sie auf dem Bild Kundenstamm die Option Anlegen > Organisation. | Das Bild Organisation anlegen wird im Bearbeitungsmodus geöffnet. |  |
| 4 | Grunddaten eingeben | Geben Sie auf dem Bild Organisation anlegen folgende Daten ein:Allgemeine InformationenGeschäftspartner: z.B. Z …, d.h. eine beliebige externe alphanumerische ID, die mit einem Buchstaben beginnen mussGruppierung: z.B. BPABOrdnen Sie jeden Geschäftspartner einer Gruppierung zu, wenn Sie den Geschäftspartner anlegen. Die Gruppierung bestimmt den Nummernkreis. Sie können anschließend die Zuordnung nicht mehr ändern.Geschäftspartnerrolle: Wählen Sie eine Rolle aus, z.B. FLCU01 - Kunde.Hinweis Ein Kunde muss entweder mit der Geschäftspartnerrolle FLCU00 - Kunde (Finanzbuchhaltung) oder mit der Geschäftspartnerrolle FLCU01 - Kunde oder mit beiden Rollen angelegt werden. Die Geschäftspartnerrolle FLCU00 - Kunde (Finanzbuchhaltung) wird in der Finanzbuchhaltung und die Geschäftspartnerrolle FLCU01 - Kunde im Verkauf verwendet.Anrede Organisation: z.B. Unternehmen (0003)Name 1: <Geben Sie einen Namen ein.>StandardadresseLand/Region: z.B. DESprache: z.B. DE |  |  |
| 5 | Bild "Organisation anlegen" schließen | Wählen Sie auf dem Bild Organisation anlegen die Option OK. | Das Bild Organisation anlegen wird geschlossen. Das Bild Neuer Kunde wird angezeigt. |  |
| 6 | Rollen auswählen | Wählen Sie auf dem Bild Neuer Kunde die Option Rollen. | Sie gelangen zum Abschnitt Rollen. |  |
| 7 | "Anlegen" wählen | Wählen Sie im Abschnitt Rollen die Option Anlegen. |  |  |
| 8 | Weitere Rollendaten eingeben | Wählen Sie im Abschnitt Rollen die Option Anlegen, und geben Sie folgende Daten ein:Geschäftspartnerrolle: Wählen Sie die zusätzliche Rolle aus, z.B. FLCU00 - Kunde (Finanzbuchhaltung).Hinweis Ein Kunde muss entweder mit der Geschäftspartnerrolle FLCU00 - Kunde (Finanzbuchhaltung) oder mit der Geschäftspartnerrolle FLCU01 - Kunde oder mit beiden Rollen angelegt werden. Die Geschäftspartnerrolle FLCU00 - Kunde (Finanzbuchhaltung) wird in der Finanzbuchhaltung und die Geschäftspartnerrolle FLCU01 - Kunde im Verkauf verwendet. | Nachdem Sie die Pflege aller Geschäftspartnerrollen abgeschlossen haben, werden diese auf dem Bild Neuer Kunde im Abschnitt Rollen angezeigt. |  |
| 9 | Grunddaten auswählen | Wählen Sie auf dem Bild Neuer Kunde die Option Grunddaten, und wechseln Sie zum Abschnitt Kundeninformationen. | Sie gelangen zum Abschnitt Kundeninformationen. |  |
| 10 | Kundeninformationen eingeben | Nehmen Sie im Abschnitt Kundeninformationen folgende Einträge vor:Kundenklassifizierung: z.B. A - KundeKundenkontengruppe: <Kundenkontengruppe>Hinweis Wenn bei der Geschäftspartnergruppierung eine flexible Kontengruppenzuordnung möglich ist, können Sie die zu verwendende Kontengruppe auswählen und vom vorgeschlagenen Wert abweichen. Weitere Details zur Geschäftspartnergruppierung und in welcher Beziehung sie zur ID-Nummerierung steht, finden Sie im Abschnitt Geschäftspartnergruppierung und Nummernkreise dieses Dokuments. |  |  |
| 11 | "Zusatzinformationen" wählen | Wählen Sie auf dem Bild Neuer Kunde die Option Grunddaten, und wechseln Sie zum Abschnitt Zusatzinformationen. | Sie gelangen zum Abschnitt Zusatzinformationen. |  |
| 12 | Zusatzinformationen eingeben | Nehmen Sie im Abschnitt Zusatzinformationen folgende Einträge vor:Expressbahnhof: <Name des Expressbahnhofs>Werk: <Wählen Sie ein Werk aus.>Branchencode 1: <Wählen Sie einen Branchencode aus.>Konditionsgruppe 1: <Wählen Sie eine Konditionsgruppe aus> |  |  |
| 13 | Adresse wählen | Wählen Sie auf dem Bild Neuer Kunde die Option Adresse, und wechseln Sie zum Abschnitt Standardadresse. | Sie gelangen zum Bildbereich Standardadresse. |  |
| 14 | Adressdaten eingeben | Nehmen Sie im Abschnitt Standardadresse die folgenden Einträge vor:Straße: z.B. Augusta Ave SEWählen Sie das Land/die Region aus, sofern Sie dies nicht in Schritt 4 getan haben.Hausnummer: z.B. 200Postleitzahl: z.B. 30315-1402Ort: z.B. AtlantaRegion: z.B. GAHinweis Wenn Sie einen Geschäftspartner in den USA anlegen, wird der Steuerstandort automatisch ermittelt. Wenn der Steuerstandort dagegen aus Ihren Eingaben unter Region und Postleitzahl abgeleitet wird, müssen Sie die korrekte und vollständige Adresse eingeben.Standard-KommunikationWählen Sie die Sprache aus, wenn Sie dies nicht in Schritt 4 getan haben.Mobiltelefon: <Mobiltelefonnummer>E-Mail: Geben Sie eine E-Mail-Adresse ein, z.B. contact@Z.com. |  |  |
| 15 | Bankkonten wählen | Wählen Sie im Bildbereich Neuer Kunde die Option Bankkonten. | Sie gelangen zum Bereich Bankkonten. |  |
| 16 | "Anlegen" wählen | Wählen Sie im Abschnitt Bankkonten die Option Anlegen. | Ein Eintrag für das Bankkonto wird im Bearbeitungsmodus angezeigt. |  |
| 17 | Bankdaten erfassen | Geben Sie auf dem Bild Neues Bankkonto folgende Daten ein, und wählen Sie Übernehmen:ID: z.B. BNK1Bankland: z.B. DEBankschlüssel: z.B. 011000390 – Bank 1 BEISPIELBANKKontonummer: z.B. 102030Geben Sie in alle anderen Bankdatenfelder die erforderlichen Daten ein. | Sie gelangen zurück auf das Bild Neuer Kunde. |  |
| 18 | "Identifikationsnummern" auswählen | Wählen Sie auf dem Bild Neuer Kunde die Option Identifikationsnummern, und wechseln Sie zum Abschnitt Steuernummern. | Sie gelangen zum Bildbereich Steuernummern. |  |
| 19 | "Anlegen" wählen | Wählen Sie im Bildbereich Steuernummern die Drucktaste Anlegen. |  |  |
| 20 | Steuernummerndaten eingeben | Nehmen Sie im Abschnitt Steuernummern folgende Einträge vor:Steuerkategorie: <Wählen Sie eine Steuerkategorie aus.>Steuernummer: <Steuernummer>Die Eingabe der Steuernummern ist von länder-/regionsspezifischen Anforderungen abhängig.Hinweis Wählen Sie die richtige Kategorie für das Land/die Region des Kunden aus. Sie pflegen zum Beispiel für einen deutschen Geschäftspartner einen Wert für die Kategorie DE1, die für die häufig verwendete Umsatzsteuernummer (Umsatzsteuer-Identifikationsnummer) steht.Nehmen Sie nur Einträge für die Felder aus, die Sie benötigen. Anderenfalls wählen Sie Löschen, um den (leeren) Datensatz zu entfernen. |  |  |
| 21 | Steuerkategorien auswählen | Wählen Sie auf dem Bild Neuer Kunde die Option Steuerkategorien. | Sie gelangen zum Bildbereich Steuerkategorien. |  |
| 22 | "Anlegen" wählen | Wählen Sie im Abschnitt Steuerkategorien die Option Anlegen. |  |  |
| 23 | Steuerkategoriedaten eingeben (optional) | Nehmen Sie im Abschnitt Steuerkategorien folgende Einträge vor:Steuerkennzeichen: z.B. COC HandelskammerNummer des Befreiungszertifikats: <Nummer des Befreiungszertifikats>Befreiungssatz des Zertifikats: z.B. 800Startdatum Befreiung: <Startdatum der Befreiung>.Enddatum Befreiung: <Enddatum der Befreiung> |  |  |
| 24 | "Texte" wählen | Wählen Sie auf dem Bild Neuer Kunde die Option Texte. | Sie gelangen zum Bildbereich Texte. |  |
| 25 | Texte anlegen | Wählen Sie im Abschnitt Texte die Option Anlegen, und geben Sie folgende Daten ein:Sprache: z.B. DEID: z.B. 01Langtext: <Geben Sie einen Langtext ein> |  |  |
| 26 | Grunddaten auswählen | Wählen Sie Grunddaten > Zusätzliche Kunden. | Sie gelangen zum Abschnitt Zusätzliche Kunden. |  |
| 27 | Zusätzliche Kundendaten hinzufügen | Wählen Sie im Abschnitt Zusätzliche Kunden die Option Anlegen.Geben Sie wie in den vorangehenden Schritten beschrieben die erforderlichen Daten ein.Hinweis Dieses Szenario dient zu Mehrfachzuordnungen von Kunden zu den gleichen Geschäftspartnern, und somit gelten die gleichen Stammdaten, wie in den vorangehenden Schritten beschrieben.Wenn zusätzliche Informationen, wie Verkaufsdaten und Buchungskreis, benötigt werden, lesen Sie in den vorangehenden Abschnitten nach, wie Sie Buchungskreis und Verkaufsdaten eingeben können. |  |  |
| 28 | Daten sichern | Wählen Sie Anlegen. | Das System meldet, dass das Objekt gesichert wurde. |  |

### Kundenstammdaten anlegen - Buchungskreisdaten

Testverwaltung

Kundenprojekt: Füllen Sie die projektbezogenen Teile aus.

|  |  |  |  |
| --- | --- | --- | --- |
| Testfall-ID | <X.XX> | Testdatum: |  |
| Testername: |  | Dauer: |  |
| Benutzerrolle(n): |  | Zuständigkeit: | <Geben Sie den Serviceanbieter, einen Kunden oder einen Serviceanbieter zusammen mit einem Kunden an.> |

Zweck

In diesem Verfahren erhalten Sie eine Anleitung zum Anlegen von Kundenstammdaten. Die zur Verfügung stehenden Apps hängen von der Ihnen zugeordneten Rolle ab. Daher werden zwei Optionen bereitgestellt.

Voraussetzung

Sie müssen die vorherige Vorgehensweise ([Kundenstammdaten anlegen: Allgemeine Daten](#unique_8) [Seite ] 6) abschließen, bevor Sie mit diesem Abschnitt fortfahren können.

Folgen Sie der Vorgehensweise, nachdem Sie die eingegebenen allgemeinen Daten gesichert haben, wie im vorherigen Kapitel erläutert.

Vorgehensweise: Option 1 – Geschäftspartner bearbeiten

Folgen Sie dieser Vorgehensweise, wenn Sie mit Ihrer Benutzerrolle auf die App Geschäftspartner pflegen(BP) zugreifen können.

| Testschrittnummer | Bezeichnung des Testschritts | Anweisungen | Erwartetes Ergebnis | Bestanden/Nicht bestanden/Anmerkungen |
| --- | --- | --- | --- | --- |
| 1 | Anmelden | Melden Sie sich am SAP Fiori Launchpad als Stammdatenexperte – Geschäftspartnerdaten an. | Das SAP Fiori Launchpad wird angezeigt. |  |
| 2 | SAP-Fiori-App aufrufen | Öffnen Sie Geschäftspartner pflegen(BP). | Die App wird geöffnet. |  |
| 3 | Suchen und öffnen | Suchen und öffnen Sie den Geschäftspartner (Kunde), den Sie im vorherigen Kapitel angelegt haben: [Kundenstammdaten anlegen: Allgemeine Daten](#unique_8) [Seite ] 6. | Der Geschäftspartner wird in der Suchliste angezeigt. |  |
| 4 | In den Änderungsmodus wechseln | Wählen Sie Umschalten zwischen Anzeigen und Ändern (F6), um in den Änderungsmodus zu wechseln. |  |  |
| 5 | Geschäftspartnerrolle ändern | Wählen Sie im Feld Ändern in GP-Rolle den folgenden Wert:Debitor (Finanzbuchhaltung)Hinweis Der technische Schlüssel dieser Geschäftspartnerrolle ist FLCU00. |  |  |
| 6 | Buchungskreisdaten öffnen | Wählen Sie Buchungskreis. | Das Bild Buchungskreis wird angezeigt. |  |
| 7 | Buchungskreis eingeben | Geben Sie den Buchungskreis ein. |  |  |
| 8 | Debitorenbuchhaltungsdaten eingeben | Geben Sie auf der Registerkarte Debitor: Geben Sie auf der Registerkarte Kontoführung im Abschnitt Kontoführung Folgendes ein:Abstimmkonto: 140000 (Debitoren – Forderungen Inland)Sortierschlüssel: <Sortierschlüssel> |  |  |
| 9 | Debitorenzahlungsdaten eingeben | Geben Sie auf der Registerkarte Debitor: Geben Sie auf der Registerkarte Debitor: Zahlungsverkehr im Abschnitt Zahlungsdaten Folgendes ein:Zahlungsbedingungen: <Zahlungsbedingungen> |  |  |
| 10 | Debitorenzahlungsdaten eingeben | Geben Sie auf der Registerkarte Debitor: Geben Sie auf der Registerkarte Debitor: Zahlungsverkehr im Abschnitt Automatischer Zahlungsverkehr Folgendes ein:Zahlwege: <Zahlwege>Hausbank: <Hausbank>Hinweis Wählen Sie F4, um die Auswahl im Feld "Zahlwege" zu öffnen. |  |  |
| 11 | Debitorenkorrespondenzdaten eingeben | Geben Sie auf der Registerkarte Debitor: Geben Sie auf der Registerkarte Korrespondenz im Abschnitt Korrespondenz folgende Daten ein:Sachbearbeiter: <Sachbearbeiter>Konto beim Kunden <Konto bei Debitor> |  |  |
| Nur für Thailand | Filialcode (nur für Thailand) | Öffnen Sie die allgemeinen Daten, und geben Sie auf der Registerkarte Länderspezif. Erw. die Daten für den Filialschlüssel zusammen mit der Adresse und dem Standardfilialschlüssel für diesen Geschäftspartner ein.Für die Adresse des Filialschlüssels wählen Sie Adresse, und geben Sie folgende Daten ein:Name (erste zwei Zeilen): <Name des Steuerzahlers>Land: THGebäudekürzel: <Gebäudename/Dorf>Raum: <Raumnummer>Etage: <Etage>Straße 2: <Moo>Straße 3: <Trok/Soi>Straße: <Straße>Hausnummer: <Nr.>Anderer Ort: <Tumbol/Unterabschnitt>Ortsteil: <Ortsteil/Abschnitt>Ort: <Provinz>Postleitzahl: <Postleitzahl>Telefon: <Telefonnummer>Hinweis Wenn für einen Geschäftspartner mehrere Filialschlüssel vorhanden sind, sollten Sie jeden einzelnen Filialschlüssel zusammen mit der jeweiligen Adresse pflegen. Sie sollten außerdem einen Filialschlüssel, der vom Geschäftspartner allgemein verwendet wird, als Standard festlegen. |  |  |
| Nur für Japan | Rechnungszusammenfassung (nur für Japan) | Geben Sie auf der Registerkarte Länderspezif. Erw. folgende Daten Ihren Anforderungen entsprechend ein, wenn dieser Kunde für die Rechnungszusammenfassung relevant ist.Im Abschnitt Japan: Rechnungzusammenfassung - Rolle:IS Role: <IS Role>Im Fall dass IS Role folgendes ist: P: Rechnungszusammenfassung - Zahlender im Abschnitt Japan: Rechnungszusammenfassung - Rechnung:Nummernkreis: MI <Nummernkreis: MI>Berechnungssteuer in MI: <Berechnungssteuer in MI>Fälligkeit verschieben: <Fälligkeit verschieben>Regelzahlungsbedingung: <Regelzahlungsbedingung>Gültig ab: <gültig ab>Zahlungsbedingung: <Zahlungsbedingungen>Im Abschnitt Japan: Rechnungsaufstellung - Zahlung:Nummernkreis: PI: <Nummernkreis: PI>Bankgebühr Zahlungsempfänger: <Bankgebühr Zahlungsempfänger>Bankgebühr Muster-ID <Bankgebühr Muster-ID>Relevant für Sonderfälle: <NICHT auswählen>Bankland: <Bankland>Bankschlüssel: <Bankschlüssel>Virtuelle Kontonummer: <Virtuelle Kontonummer>Laufende Nummer: <Laufende Nummer>Name des abweichenden Zahlungsempfängers: <Name des abweichenden Zahlungsempfängers>Kontrahentbankname: <Kontrahentbankname>Name der Kontrahentbankfiliale: <Name der Kontrahentbankfiliale>Im Fall dass IS Role folgendes ist: M: Monatliche Rechnungsempfänger im Abschnitt Japan: Rechnungzusammenfassung - Rolle:Rechnungszusammenfassung - Zahlender: <Rechnungszusammenfassung - Zahlender>Im Abschnitt Japan: Rechnungszusammenfassung - Rechnung:Nummernkreis: MI <Nummernkreis: MI>Berechnungssteuer in MI: <Berechnungssteuer in MI>Im Fall dass IS Role folgendes ist: C: (Rechnungszusammenfassung) Kunde im Abschnitt Japan: Rechnungzusammenfassung - Rolle:Rechnungszusammenfassung - Empfänger: <Rechnungszusammenfassung - Empfänger> |  |  |
| 12 | Daten sichern | Sichern Sie Ihre Eingaben. | Der Eintrag im Feld Ändern in GP-Rolle ändert sich von Debitor (Neu) in Debitor (gepflegt). |  |

Vorgehensweise: Option 2 – Kundenstammdaten verwalten

Folgen Sie dieser Vorgehensweise, wenn Sie mit Ihrer Benutzerrolle auf die App Kundenstammdaten verwalten(F0850A) zugreifen können.

| Testschrittnummer | Bezeichnung des Testschritts | Anweisungen | Erwartetes Ergebnis | Kommentare |
| --- | --- | --- | --- | --- |
| 1 | Anmelden | Melden Sie sich am SAP Fiori Launchpad als Stammdatenexperte – Geschäftspartnerdaten an. | Das SAP Fiori Launchpad wird angezeigt. |  |
| 2 | SAP-Fiori-App aufrufen | Öffnen Sie Kundenstammdaten verwalten(F0850A). | Die App wird geöffnet. |  |
| 3 | Suchen und öffnen | Suchen und öffnen Sie den Geschäftspartner (Kunde), den Sie im vorherigen Kapitel angelegt haben: [Kundenstammdaten anlegen: Allgemeine Daten](#unique_8) [Seite ] 6. |  |  |
| 4 | "Bearbeiten" wählen | Wählen Sie Bearbeiten. | Das Bild Kundenstamm wird im Bearbeitungsmodus angezeigt (Sie können Daten in die Felder eingeben). |  |
| 5 | Buchungskreis auswählen | Wählen Sie auf dem Bild Kundenstamm die Option Buchungskreise. | Sie gelangen zum Abschnitt Buchungskreise. |  |
| 6 | "Anlegen" wählen | Wählen Sie im Bildbereich Buchungskreise die Option Anlegen. | Das Bild Neuer Buchungskreis wird im Bearbeitungsmodus angezeigt. |  |
| 7 | Buchungskreisdaten eingeben | Geben Sie im Bild Neuer Buchungskreis folgende Daten ein:Buchungskreis: Geben Sie den Buchungskreis ein, z.B. 1710.Auf der Registerkarte Korrespondenz:Sachbearbeiter: Beispiel: 01 Frau Schmidt.Auf der Registerkarte Finanzen :FinanzbuchhaltungAbstimmkonto: z.B. 12100000 – Forderungen AuslandSortierschlüssel: z.B. 009 Externe Belegnummer.Finanzen - ZahlungsdatenZahlungsbedingungen: z.B. 0001Finanzen – Automatischer ZahlungsverkehrZahlwege: z.B. C ("Check" (Scheck), z.B. für die USA)Auf der Registerkarte Mahndaten:Mahnbereich: Organisationseinheit, die Sie zur Bearbeitung des Mahnprogramms verwenden, z.B. nach Abteilung oder Verkaufsorganisation.Mahnverfahren, Mahnsperre, Mahnempfänger, Mahnsachbearbeiter: Wählen Sie einen Wert aus der Wertehilfe.Mahnstufe: z.B. 0Letzte Mahnung: z.B. 10.02.2020Gerichtliches Mahnverfahren von: z.B. 11.02.2020Auf der Registerkarte Texte:Wählen Sie im Abschnitt Texte die Option Anlegen, und geben Sie folgende Daten ein:Sprache: z.B. DEID: z.B. 01Langtext: <Geben Sie einen Langtext ein> |  |  |
| 8 | Zum Hauptbild zurückkehren | Wählen Sie Übernehmen. |  |  |
| 9 | Daten sichern | Wählen Sie Sichern. | Eine Systemmeldung bestätigt, dass das Objekt gesichert wurde. |  |

### Kundenstammdaten anlegen - Vertriebsbereichsdaten

Testverwaltung

Kundenprojekt: Füllen Sie die projektbezogenen Teile aus.

|  |  |  |  |
| --- | --- | --- | --- |
| Testfall-ID | <X.XX> | Testdatum: |  |
| Testername: |  | Dauer: |  |
| Benutzerrolle(n): |  | Zuständigkeit: | <Geben Sie den Serviceanbieter, einen Kunden oder einen Serviceanbieter zusammen mit einem Kunden an.> |

Zweck

In diesem Verfahren erhalten Sie eine Anleitung zum Anlegen von Kundenstammdaten. Die zur Verfügung stehenden Apps hängen von der Ihnen zugeordneten Rolle ab. Daher werden zwei Optionen bereitgestellt.

Voraussetzung

Sie müssen die vorherige Vorgehensweise ([Kundenstammdaten anlegen: Allgemeine Daten](#unique_8) [Seite ] 6) abschließen, bevor Sie mit diesem Abschnitt fortfahren können.

Folgen Sie dieser Vorgehensweise, nachdem Sie die Eingaben zu den allgemeinen Daten, wie im vorherigen Kapitel erläutert, auf dem Bild Organisation anzeigen: Kundenname gesichert haben.

Vorgehensweise: Option 1 – Geschäftspartner bearbeiten

Folgen Sie dieser Vorgehensweise, wenn Sie mit Ihrer Benutzerrolle auf die App Geschäftspartner pflegen(BP) zugreifen können.

| Testschrittnummer | Bezeichnung des Testschritts | Anweisungen | Erwartetes Ergebnis | Bestanden/Nicht bestanden/Anmerkung |
| --- | --- | --- | --- | --- |
| 1 | Anmelden | Melden Sie sich am SAP Fiori Launchpad als Stammdatenexperte – Geschäftspartnerdaten an. | Das SAP Fiori Launchpad wird angezeigt. |  |
| 2 | SAP-Fiori-App aufrufen | Öffnen Sie Geschäftspartner pflegen(BP). | Die App wird geöffnet. |  |
| 3 | In den Änderungsmodus wechseln | Wählen Sie Umschalten zwischen Anzeigen und Ändern (F6), um in den Änderungsmodus zu wechseln. |  |  |
| 4 | Geschäftspartnerrolle ändern | Wählen Sie im Feld Ändern in GP-Rolle den folgenden Wert:DebitorHinweis Der technische Schlüssel dieser Geschäftspartnerrolle ist FLCU01. |  |  |
| 5 | Vertriebsbereich öffnen | Wählen Sie auf dem Bild Vertrieb. | Das Bild Vertriebsbereich wird angezeigt. |  |
| 6 | Vertriebsbereichsdaten eingeben | Tragen Sie Folgendes ein:Verkaufsorg.: <Verkaufsorganisation>Vertriebs- kanal: <Vertriebsweg>Sparte: <Sparte>Hinweis Diese drei Einträge (Verkaufsorganisation, Vertriebsweg und Sparte) bilden den Vertriebsbereich. In vielen Fällen legt der Vertriebsbereich den Zweck der Vertriebsabwicklung fest, z.B. im Kundenauftrag oder innerhalb der Preisfindung. |  |  |
| 7 | Kundenauftragsdaten eingeben | Geben Sie auf der Registerkarte Aufträge im Bereich Auftrag folgende Daten ein:Währung: <Währung> |  |  |
| 8 | Versanddaten eingeben | Geben Sie auf der Registerkarte Versand im Bereich Versand folgende Daten ein:Lieferpriorität: <Lieferpriorität>Auslieferungswerk: <Auslieferungswerk>Versandbedingungen: <Versandbedingungen> |  |  |
| 9 | Fakturadaten eingeben | Geben Sie auf der Registerkarte Faktura im Abschnitt Liefer- und Zahlungsbedingungen die folgenden Daten ein:Incoterms: EXW (Ab Werk)Sie können den Incoterm-Wert pflegen und die zugehörige Beschreibung angeben.Hinweis Die Felder für Incoterms sind voneinander abhängig. Wenn Sie beispielsweise den Wert für das Feld Incoterms pflegen, müssen Sie auch Informationen für den Incoterm-Ort 1 (ID) und Incoterm-Ort 1 angeben.Zahlungsbedingungen: <Wählen Sie die Zahlungsbedingungen aus.>Hinweis Die hier definierten Zahlungsbedingungen werden in einen Kundenauftrag kopiert und anstelle der auf Buchungskreisebene definierten Zahlungsbedingungen verwendet. |  |  |
| 10 | Buchhaltungsdaten eingeben | Geben Sie im Abschnitt Buchhaltung folgende Daten ein:Kontierungsgrp.Kunde: <Wählen Sie die Kontierungsgruppe für den Kunden aus.>Inlandskunden können zum Beispiel der Kontierungsgruppe 01 und Auslandskunden der Kontierungsgruppe 02 zugeordnet werden. Weitere Optionen finden Sie in der Eingabehilfe. |  |  |
| 11 | Steuerdaten erfassen | Wählen Sie im Abschnitt Steuerstandortcode den folgenden Wert für den vorhandenen Eintrag in der Tabelle aus:Steuerklassifikation: <1>Der Wert <1> bedeutet z.B., dass dieser Kunde voll steuerpflichtig ist. |  |  |
| 12 | Partnerrollendaten ändern | Auf der Registerkarte Partnerrollen sind die folgenden vier Standardpartnerrollen für den Kunden verfügbar. Sie können die vier Partnerrollen anlegen:AG - AuftraggeberRE - RechnungsempfängerRG - ReguliererWE - WarenempfängerHinweis Die vier oben aufgeführten Partnerrollen bilden für das Zuordnen zu einem Debitorenstammdatensatz den Mindestumfang an Partnerrollen, um in einem Standard-Vertriebsprozess zu funktionieren. |  |  |
| 13 | Langtext erfassen | Geben Sie im Feld Kundentext die Details der Verkaufsdaten ein. Beachten Sie, dass es sich hierbei um ein schreibgeschütztes Feld handelt. Verwenden Sie die Option Text bearbeiten, um den Langtext zu ändern. |  |  |
| 14 | Allgemeine Daten öffnen | Wählen Sie auf dem Bild Allgemeine Daten. |  |  |
| 15 | Organisationsdaten eingeben | Geben Sie auf der Registerkarte Debitor: Geben Sie auf der Registerkarte Allgemeine Daten im Abschnitt Marketing Folgendes ein:Kundenklassifikation: <Wählen Sie eine Kundenklassifikation aus> |  |  |
| 16 | Daten sichern | Sichern Sie Ihre Eingaben. |  |  |

Vorgehensweise: Option 2 – Kundenstammdaten verwalten

Folgen Sie dieser Vorgehensweise, wenn Sie mit Ihrer Benutzerrolle auf die App Kundenstammdaten verwalten(F0850A) zugreifen können.

| Testschrittnummer | Bezeichnung des Testschritts | Anweisungen | Erwartetes Ergebnis | Kommentare |
| --- | --- | --- | --- | --- |
| 1 | Anmelden | Melden Sie sich am SAP Fiori Launchpad als Stammdatenexperte – Geschäftspartnerdaten an. | Das SAP Fiori Launchpad wird angezeigt. |  |
| 2 | SAP-Fiori-App aufrufen | Öffnen Sie Kundenstammdaten verwalten(F0850A). | Die App wird geöffnet. |  |
| 3 | Suchen und öffnen | Suchen und öffnen Sie den Geschäftspartner (Kunde), den Sie im vorherigen Kapitel angelegt haben: [Kundenstammdaten anlegen: Allgemeine Daten](#unique_8) [Seite ] 6. |  |  |
| 4 | "Bearbeiten" wählen | Wählen Sie Bearbeiten. | Das Bild Kundenstamm wird im Bearbeitungsmodus angezeigt (Sie können Daten in die Felder eingeben). |  |
| 5 | Vertriebsbereich öffnen | Wählen Sie auf dem Bild Kundenstamm die Option Vertriebsbereiche.Hinweis Die Registerkarte "Vertriebsbereiche" ist nur verfügbar, wenn der Geschäftspartner die Rolle FLCU01 (Kunde) hat. | Der Abschnitt Vertriebsbereiche wird angezeigt. |  |
| 6 | "Anlegen" wählen | Wählen Sie im Abschnitt Vertriebsbereiche die Option Anlegen. | Das Bild Neuer Vertriebsbereich wird im Bearbeitungsmodus angezeigt. |  |
| 7 | Vertriebsbereichsdaten eingeben | Geben Sie auf dem Bild Neuer Vertriebsbereich folgende Daten ein:Allgemeine DatenVerkaufsorganisation: z.B. 1710Hinweis Wenn Sie die Verkaufsorganisation aus der Wertehilfe auswählen, werden die folgenden Felder (Vertriebsweg und Sparte) automatisch ausgefüllt.Vertriebsweg: z.B. 10Sparte: z.B. 00VertriebsbereichsdetailsVertriebsbereichsdetails - KundenaufträgeKonto bei Debitor <Geben Sie Ihr Konto beim Kunden ein.>Währung: z.B. EURVertriebsbereichsdetails - Rechnungsstellung:Incoterms: z.B. EXWIncoterms-Ort 1: z.B. Palo Alto.Zahlungsbedingungen: z.B. 0001Vertriebsbereichsdetails - Versand:Lieferpriorität: z.B. NormalLieferwerk: z.B. 1710Versandbedingungen: z.B. Sofort.Vertriebsbereichsdetails - Buchungsdaten:Kontierungsgruppe: z.B. Erlös InlandVertriebsbereichsdetails - Preisfindung und Statistiken:Kundenschema: z.B. Schema 01 |  |  |
| 8 | "Texte" wählen | Wählen Sie auf dem Bild Neuer Vertriebsbereich die Option Texte. |  |  |
| 9 | "Anlegen" wählen | Wählen Sie im Abschnitt Texte die Option Anlegen, und geben Sie folgende Daten ein:Sprache: z.B. DEID: Wählen Sie eine Kennnummer aus oder geben Sie manuell eine Kennnummer ein, z.B. 01.Langtext: <Geben Sie einen Langtext ein> |  |  |
| 10 | Steuern auswählen | Wählen Sie auf dem Bild Neuer Vertriebsbereich die Option Steuern. | Der Bereich Steuern wird angezeigt. |  |
| 11 | Land/Region und Steuertyp auswählen | Wählen Sie im Abschnitt Steuern den Eintrag für ein Land/eine Region, z.B. USA (US).Hinweis Der Eintrag der Steuerkategorie hängt vom Standort des Kunden ab. UTXJ ist z.B. die Steuerkategorie zum Anlegen eines US-Kunden; TTXJ ist die Steuerkategorie zum Anlegen eines DE-Kunden. | Das Bild Vertriebsbereichssteuern wird im Bearbeitungsmodus geöffnet. |  |
| 12 | Steuerklassifikation eingeben | Nehmen Sie auf der Registerkarte Steuer folgende Einträge vor:Steuerklassifikation: Wählen Sie z.B. Steuerpflichtig (1). |  |  |
| 13 | "Übernehmen" wählen | Wählen Sie Übernehmen. | Sie kehren zur Hauptsicht zurück. |  |
| 14 | Partnerrollen auswählen | Wählen Sie auf dem Bild Neuer Vertriebsbereich die Option Partnerrollen. | Der Abschnitt Partnerrollen wird angezeigt. |  |
| 15 | "Anlegen" wählen | Wählen Sie im Abschnitt Partnerrollen die Option Anlegen. | Der Abschnitt Partnerrollen wird im Bearbeitungsmodus angezeigt. |  |
| 16 | Partnerrollendaten eingeben | Wählen Sie eine Partnerrolle aus, z.B. Auftraggeber (AG).Wählen Sie den Eintrag für die Partnerrolle, und wählen Sie auf dem Bild Allgemeine Daten eine Partnernummer aus, und geben Sie eine Partnerbeschreibung ein. |  |  |
| 17 | Zur Hauptsicht zurückkehren | Wählen Sie Übernehmen. | Die hinzugefügte Partnerrolle wird in der Hauptsicht angezeigt. |  |
| 18 | Partnerrollendaten eingeben | Wiederholen Sie die Schritte 15 bis 17 (zum Hinzufügen einer Partnerrolle), um zusätzliche Partnerrollendaten einzuschließen. Fügen Sie die folgenden Partnerrollen hinzu:Hinweis Die zweistelligen Schlüssel für die Partnerrolle sind sprachabhängig. Die hier angegebenen Schlüssel gelten für die Anmeldesprache Englisch.In anderen Sprachen können diese Schlüssel unterschiedlich sein. Die zweistelligen Partnerrollenschlüssel auf Deutsch sind z.B.:AG für AuftraggeberWE für WarenempfängerRE für RechnungsempfängerRG für ReguliererPartnerrolle: Warenempfänger:Partnerrolle: WE WarenempfängerPartnerrolle: Rechnungsempfänger:Partnerrolle: RE RechnungsempfängerPartnerrolle: RG Regulierer:Partnerrolle: RG Regulierer |  |  |
| 19 | Zur Hauptsicht zurückkehren | Wählen Sie Übernehmen.Hinweis Stellen Sie sicher, dass die Meldung Entwurf aktualisiert im unteren Bildbereich angezeigt wird, bevor Sie zum Hauptbild zurückkehren. |  |  |
| 20 | Daten sichern | Wählen Sie Sichern. | Eine Systemmeldung bestätigt, dass das Objekt gesichert wurde. |  |

### Kundenhierarchien anlegen

Testverwaltung

Kundenprojekt: Füllen Sie die projektbezogenen Teile aus.

|  |  |  |  |
| --- | --- | --- | --- |
| Testfall-ID | <X.XX> | Testdatum: |  |
| Testername: |  | Dauer: |  |
| Benutzerrolle(n): |  | Zuständigkeit: | <Geben Sie den Serviceanbieter, einen Kunden oder einen Serviceanbieter zusammen mit einem Kunden an.> |

Zweck

Die folgende Vorgehensweise enthält Anweisungen für Kundenhierarchien vom Typ Verkauf und Analyse mit der App Kundenhierarchien verwalten(F5794).

Voraussetzung

Sie müssen die vorherige Vorgehensweise ([Kundenstammdaten anlegen: Allgemeine Daten](#unique_8) [Seite ] 6) abschließen, bevor Sie mit diesem Abschnitt fortfahren können.

Folgen Sie der Vorgehensweise, nachdem Sie die eingegebenen allgemeinen Daten gesichert haben, wie im vorherigen Kapitel erläutert.

Vorgehensweise

| Testschrittnummer | Bezeichnung des Testschritts | Anweisung | Erwartetes Ergebnis | Kommentare |
| --- | --- | --- | --- | --- |
| 1 | Anmelden | Melden Sie sich am SAP Fiori Launchpad als Stammdatenexperte – Geschäftspartnerdaten an. | Das SAP Fiori Launchpad wird angezeigt. |  |
| 2 | SAP-Fiori-App aufrufen | Öffnen Sie Kundenhierarchien verwalten(F5794). | Die App wird geöffnet. |  |
| 3 | Neue Hierarchie anlegen | Wählen Sie auf dem Bild Kundenhierarchien verwalten die Option Anlegen. |  |  |
| 4 | Hierarchieart auswählen | Wählen Sie die Hierarchieart aus folgenden Optionen aus:Kundenhierarchie - VertriebKundenhierarchie - Analyse |  |  |
| 5 | Hierarchiebezogene Daten eingeben | Geben Sie im Dialogfenster Neue Hierarchie anlegen die Hierarchie-ID an, und geben Sie andere erforderlichen Daten ein. |  |  |
| 6 | Unterknoten bearbeiten | Sobald der übergeordnete Knoten mit der im vorherigen Schritt angegebenen Hierarchie-ID angelegt wurde, fügen Sie diesem übergeordneten Knoten Unterknoten hinzu. Sie können folgende Aktionen ausführen:Den Hierarchienamen ändern.Gültigkeiten und andere Details wie Vertrieb, Sparte usw. ändern.Die Option als Ein/Aus simulieren.Die Unterknoten löschen, die der Hierarchie zugeordnet sind. |  |  |
| 7 | Unterknotenoptionen | Wählen Sie den im vorherigen Schritt definierten übergeordneten Knoten aus.Wählen Sie die Option zum Definieren des Unterknotens. Im Folgenden finden Sie die drei Arten von Unterknoten, die hinzugefügt werden können:Unterknoten: Dies ist ein Textknoten, der Ihren Geschäftsanforderungen entsprechend angepasst werden kann. Er kann mehrere Unterknoten enthalten.Unterknoten – Geschäftspartner: Dies ist ein Geschäftspartnerknoten, der mehrere Unterknoten enthalten kann. Das System prüft automatisch, ob der zur Hierarchie hinzugefügte Geschäftspartner zum selben Vertriebsbereich gehört.Geschäftspartner: Dies ist ein Geschäftspartnerknoten, der jedoch ein Blattknoten ist und keine weiteren Knoten enthalten darf. Das System prüft automatisch, ob der zur Hierarchie hinzugefügte Geschäftspartner zum selben Vertriebsbereich gehört. | Das Bild Stammdaten - Produkt wird angezeigt.Ihre Daten werden gesichert. |  |
| 8 | Unterknoten anlegen | Wählen Sie den übergeordneten Knoten aus.Wählen Sie Bearbeiten. Wählen Sie +, um einen Unterknoten hinzuzufügen.Wählen Sie die relevanten Kundenstammsätze aus, die bereits im System vorhanden sind.Wenn der Hierarchieart Vertrieb ist, wählen Sie aus, ob ein Unterknoten preisfindungsrelevant ist.Hinweis Die Unterknoten können auch im Schnellerfassungsmodus angelegt werden, wodurch mehrere Unterknoten auf einmal angelegt werden können. | Stellen Sie sicher, dass der Unterknoten angelegt und unter dem Wurzelknoten angezeigt wird.Hinweis Wenn die Werte für Vertriebsbereich/Sparte/Verteilung nicht mit dem zuvor hinzugefügten relevanten Kunden übereinstimmen, kann der Unterknoten nicht hinzugefügt werden, und es wird eine Fehlermeldung angezeigt, die besagt, dass der Kunde keine relevanten Vertriebs-/Sparten-/Verteilungsdaten hat. |  |
| 9 | Hierarchie aktivieren | Wählen Sie Aktivieren. | Die Kundenhierarchie ist aktiviert. |  |
| 10 | Hierarchie löschen | Wählen Sie Löschen, wenn Sie eine Hierarchie löschen möchten. |  |  |
| 11 | Export/Import | Wählen Sie Exportieren/Importieren, wenn Sie eine Hierarchie exportieren oder importieren möchten. | Sie können eine Hierarchiestruktur exportieren oder importieren. |  |

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
- related-to :: [[08-sales-order-management/6n3-517]]
- related-to :: [[08-sales-order-management/6n3-519]]
- related-to :: [[08-sales-order-management/create-customer-hierarchy-master-data-script-6n3-515]]
- related-to :: [[08-sales-order-management/script-de-dados-mestre-criar-script-de-dados-mestre-de-hierarquia-de-c]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/6N3_S4CLD2608_Master_Data_DE_XX.docx` — full document · extracted with `mammoth` · 46,087 chars in the whole document
