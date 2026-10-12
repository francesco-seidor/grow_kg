---
id: 03-financial-accounting-and-close/stammdatenskript-sap-s-4hana-cloud-public-edition-anlage-anlegen-sds-b
title: Stammdatenskript SAP S/4HANA Cloud Public Edition - Anlage anlegen – SDS (BNI) (BNI_S4CLD2608_Master_Data_DE_XX)
description: "German master data script for asset master records (Anlagenstamm) in SAP S/4HANA Cloud Public Edition 2608: prerequisites, asset classes, number ranges, test procedures."
cluster: 03-financial-accounting-and-close
tags: [kb/financial-accounting-and-close, topic/fixed-asset-master-data]
aliases: [BNI_S4CLD2608_Master_Data_DE_XX]
keywords: [Fixed Asset Master Records, asset master data, asset classes, number ranges, legacy asset takeover, balance carryforward, asset creation, asset change, asset blocking, asset deletion]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/BNI_S4CLD2608_Master_Data_DE_XX.docx]
confidence: high
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-610
topic: 03-financial-accounting-and-close/fixed-asset-master-data
language: DE
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Stammdatenskript SAP S/4HANA Cloud Public Edition - Anlage anlegen – SDS (BNI) (BNI_S4CLD2608_Master_Data_DE_XX)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/BNI_S4CLD2608_Master_Data_DE_XX.docx`, extracted with `mammoth`. Grouped under **Fixed Asset Master Records** in Financial Accounting and Close. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

| <!-- image omitted: unnamed --> | StammdatenskriptSAP S/4HANA Cloud Public Edition - 02-07-26 |
| --- | --- |
|  | Anlage anlegen – SDS (BNI) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Inhaltsverzeichnis

[1 Verwendungszweck 2](#_Toc233889960)

[2 Voraussetzungen 3](#_Toc233889961)

[2.1 Systemzugriff 3](#_Toc233889962)

[2.2 Rollen 3](#_Toc233889963)

[2.3 Erforderliche Organisationseinheiten 3](#_Toc233889964)

[2.4 Obligatorische und optionale Stammdaten 4](#_Toc233889965)

[2.5 Wesentliche Parameter für die Datenerstellung 4](#_Toc233889966)

[2.5.1 Anlagenklassen und Nummernkreise 4](#_Toc233889967)

[2.6 Vorbereitende Schritte 6](#_Toc233889968)

[2.6.1 Bereitschaft des Anlagenbuchhaltungssystems überprüfen 6](#_Toc233889969)

[2.6.1.1 Informationen zum Übernahmedatum bestätigen 6](#_Toc233889970)

[2.6.1.2 Ausführung des Saldovortrags für aktuelles Geschäftsjahr bestätigen 8](#_Toc233889971)

[3 Übersichtstabelle 10](#_Toc233889972)

[4 Testverfahren 12](#_Toc233889973)

[4.1 Anlage anlegen 12](#_Toc233889974)

[4.2 Anlage ändern 14](#_Toc233889975)

[4.3 Anlage anzeigen 15](#_Toc233889976)

[4.4 Anlagen sperren 16](#_Toc233889977)

[4.5 Anlage löschen 17](#_Toc233889978)

[4.6 Unteranlage einer Anlage anlegen 18](#_Toc233889979)

[4.7 Änderungsbelege für Anlagenstammsatz 20](#_Toc233889980)

[4.8 Abschreibungsschlüssel: Details anzeigen 20](#_Toc233889981)

## Verwendungszweck

Eine Anlage ist ein Objekt, ein Recht oder ein anderes Element, das einem Unternehmen gehört und das für die langfristige Verwendung vorgesehen ist und in der Bilanz einzeln aufgeführt werden kann. Die Pflege von Anlagen beinhaltet das Anlegen, Ändern und Anzeigen von Anlagenstammsätzen.

Die verschiedenen Informationselemente sind nach Verwendungsbereich und Funktionen im System strukturiert, um Benutzern das Anlegen, Pflegen und Evaluieren von Stammdaten zu erleichtern.

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
| Anlagenbuchhalter | SAP_BR_AA_ACCOUNTANT | Anlagen | SAP_BR_AA_ACCOUNTANT |  |
| Hauptbuchhalter | SAP_BR_GL_ACCOUNTANT | Hauptbuch | SAP_BR_GL_ACCOUNTANT |  |

### Erforderliche Organisationseinheiten

Anlagenstammdaten hängen von der Organisationseinheit des Unternehmens ab.

Die folgende Tabelle bietet eine Übersicht über diese Organisationseinheit.

| Datensegment | Hängt ab von | Feldbeispiele | Kommentare | Zu verwendende Organisationseinheit |
| --- | --- | --- | --- | --- |
| Buchungskreisdaten | Buchungskreis | ID, Beschreibung, Kostenstelle usw. | Buchungskreisdaten können für jede Buchungskreis-ID Ihrer Unternehmensstruktur vorhanden sein, für die der Anlagenstammsatz verwendet wird. | <Ihr Buchungskreis> |

### Obligatorische und optionale Stammdaten

Anlagenstammdatensätze können auf andere Stammdaten verweisen. Die folgende Tabelle bietet eine Übersicht über die optionalen und obligatorischen Stammdatenobjekte, die in einem Anlagenstammdatensatz verwendet werden müssen.

| Stammdatenobjekt | Verwendet im Datensegment | Obligatorisch / optional | Kommentare |
| --- | --- | --- | --- |
| Kostenstelle | Im Anlagenstamm finden Sie den Eintrag zur Kostenstelle auf der Registerkarte Zeitabhängig. | Obligatorisch | Um die Anlagenkostenstelle eingeben zu können, müssen Sie die Kostenstelle zuvor angelegt haben. In den Anlagenstammsätzen können Sie dann die Ist-Kostenstelle eingeben. |

### Wesentliche Parameter für die Datenerstellung

In diesem Abschnitt werden einige Basisparameter erläutert, die das Verhalten eines Stammsatzes beeinflussen und zum Anlegen eines Anlagenstammdatensatzes immer erforderlich sind:

#### Anlagenklassen und Nummernkreise

Anlagenklassen bestimmen die Nummernkreise für die Anlagenstammsatz-IDs. Sie können die Zuordnung oder IDs nachträglich nicht ändern, sondern sie lediglich zu einem für eine andere Anlagenklasse angelegten Anlagenstammsatz übertragen. Wenn eine Anlagenklasse einem internen Nummernkreis zugeordnet ist, können Sie die Anlagenstammsatz-ID nicht manuell eingeben. Lassen Sie das Feld in diesem Fall leer, da das System automatisch eine Nummer aus dem zugeordneten numerischen Nummernkreis wählt.

Die folgenden Anlagenklassen und entsprechenden Nummernkreise wurden für Anlagen im Buchungskreis 1010 definiert:

| Anlagenklasse | Nummernkreis / Anlagenstammsatz-ID | Kommentare |
| --- | --- | --- |
| 1000 | Interner numerischer Nummernkreis:10000000 – 19999999 | Grundstücke und ähnliche Rechte |
| 1100 | Interner numerischer Nummernkreis:10000000 – 19999999 | Gebäude |
| 1200Nicht für alle Länder/Regionen relevant | Interner numerischer Nummernkreis:10000000 – 19999999 | Gelände |
| 1500Nicht für alle Länder/Regionen relevant | Interner numerischer Nummernkreis:10000000 – 19999999 | Verbesserungen von gemieteten oder gepachteten Objekten |
| 2000 | Interner numerischer Nummernkreis:20000000 – 29999999 | Technische Anlagen und Maschinen |
| 3000 | Interner numerischer Nummernkreis:30000000 – 39999999 | Betriebs- und Geschäftsausstattung |
| 3100 | Interner numerischer Nummernkreis:50000000 – 59999999 | Fahrzeuge |
| 3200 | Interner numerischer Nummernkreis:60000000 – 69999999 | EDV-Hardware |
| 3210 | Interner numerischer Nummernkreis:60000000 – 69999999 | EDV-Software |
| 3300 | Interner numerischer Nummernkreis:30000000 – 39999999 | Büroausstattung |
| 4000 | Interner numerischer Nummernkreis:40000000 – 49999999 | Anlage im Bau (materiell) |
| 4010 | Interner numerischer Nummernkreis:40000000 – 49999999 | Anlage im Bau (immateriell) |
| 4001 | Interner numerischer Nummernkreis:40000000 – 49999999 | AIB als Investitionsmaßnahme (materiell) |
| 4011 | Interner numerischer Nummernkreis:40000000 – 49999999 | AIB als Investitionsmaßnahme (immateriell) |
| 5000 | Interner numerischer Nummernkreis:80000000 – 89999999 | Geringwertige Anlagen |
| 8200 | Interner numerischer Nummernkreis:90000000 – 99999999 | Kulanz |
| 8300 | Interner numerischer Nummernkreis:80000000 - 89999999 | Sonstiges immaterielles Vermögen |
| 9000 | Interner numerischer Nummernkreis:90000000 - 99999999 | Steuervermögen |

### Vorbereitende Schritte

#### Bereitschaft des Anlagenbuchhaltungssystems überprüfen

##### Informationen zum Übernahmedatum bestätigen

Testverwaltung

Kundenprojekt: Füllen Sie die projektbezogenen Teile aus.

|  |  |  |  |
| --- | --- | --- | --- |
| Testfall-ID | <X.XX> | Testdatum: |  |
| Testername: |  | Dauer: |  |
| Benutzerrolle(n): |  | Zuständigkeit: | <Geben Sie den Serviceanbieter, einen Kunden oder einen Serviceanbieter zusammen mit einem Kunden an.> |

Zweck

In dieser Aktivität bestätigen Sie die Datenwerte für Übernahmedatum, Status und Belegart für die Erfassung von Altanlagen.

|  |
| --- |
| Hinweis Nach dem Abschluss der erstmaligen Content-Aktivierung, müssen Sie ein Übernahmedatum festlegen. Dieses bestimmt das aktuelle Geschäftsjahr und das letzte abgeschlossene Geschäftsjahr in der Anlagenbuchhaltung. Das Übernahmedatum ist für die Systemverarbeitung besonders wichtig, da hiermit der Zeitpunkt festgelegt wird, zu dem Werte von Altanlagen geladen werden. Bei SAP S/4HANA Cloud Public Edition-Systemen ist das in der Regel der letzte Tag des Vorjahres. Wenn das System beispielsweise im Geschäftsjahr 2020 ist und für das Unternehmen ein Standardkalenderjahr als Geschäftsjahr gilt, ist das Übernahmedatum der 31.12.2020. |

|  |
| --- |
| Achtung Das bedeutet, dass Altanlagen zum Jahresabschluss 2020 geladen werden. |

Vorgehensweise

| Prozessschritt | Bezeichnung des Testschritts | Anweisung | Erwartetes Ergebnis | Bestanden/Nicht bestanden/Anmerkung |
| --- | --- | --- | --- | --- |
| 1 | Anmelden | Melden Sie sich am SAP Fiori Launchpad als Anlagenbuchhalter an. | Das SAP Fiori Launchpad wird angezeigt. |  |
| 2 | SAP-Fiori-App aufrufen | Öffnen Sie Buchungskreiseinstellungen vornehmen - Anlagenbuchhaltungsspezifisch(F7312). | Das Bild Einstellungen für BuchKreis in Anlagenbuchhaltung anzeigen wird angezeigt.Um zwischen Änderungs- und Anzeigemodus zu wechseln, wählen Sie Ändern/Anzeigen. |  |
| 3 | Buchungskreis auswählen | Wählen Sie im linken Bildbereich den Buchungskreis aus, und wählen Sie Buchungskreis auswählen. |  |  |
| 4 | Allgemeine Einstellungen | Wählen Sie die Registerkarte Allgemeine Einstellungen. |  |  |
| 5 | Allgemeine Einstellungen prüfen | Prüfen Sie de Status für Ihr Unternehmen. | Auf der Registerkarte Allgemeine Informationen werden die Einstellungen Ihres Buchungskreises angezeigt. Der Buchungskreisstatus sollte Zum Testen lauten. |  |
| 6 | Parameter für Altdatenübernahme pflegen | Prüfen oder ändern Sie im Abschnitt Altdatenübernahme die folgenden Einträge:Hinweis Falls erforderlich, legen Sie zunächst ein neues Segment für die Altdatenübernahme an, indem Sie Altdatenübernahmesegment anlegen auswählen.Übernahmedatum: Setzen Sie zu Testzwecken dieses Datum auf den LETZTEN TAG des VORJAHRESULTIMO.Status der Altdatenübernahme: Setzen Sie diesen Status zu Testzwecken auf IN DURCHFÜHRUNG (andere Buchungen zulässig).Belegart: Setzen Sie diese Option zu Testzwecken auf AA.Hinweis Der Wert für das Übernahmedatum ist in der Regel das Enddatum des Vorjahres. Wenn Sie angewiesen sind, ein unterjähriges Datum zu verwenden, wäre es ein Monatsenddatum. Das Datum sollte immer vorwärts verschoben werden (nie rückwärts).Hinweis Für den Wert Status der Altdatenübernahme haben Sie vier Optionen:In Vorbereitung: Das System lässt unvollständige Customizing-Einstellungen für die Altdatenübernahme zu (in dieser Phase sind keine Belegbuchungen zulässig).In Durchführung: Nur Buchungen der Altdatenübernahme sind zulässig (andere Arten von Buchungen, Zu- und Abgänge sind nicht erlaubt).In Durchführung (andere Buchungen zulässig): Nicht nur Buchungen der Altdatenübernahme, sondern auch andere Buchungen sind zulässig. Dieser Status ist sinnvoll, wenn Sie in einem bereits produktiven Buchungskreis weitere Altdatenübernahmen durchführen.Abgeschlossen: Die Altdatenübernahme ist abgeschlossen. Buchungen der Altdatenübernahme sind nicht zulässig, und Sie dürfen keine Altanlagen anlegen. |  |  |
| 7 | Änderungen sichern | Wählen Sie Menü > Allgemein > Sichern. |  |  |

##### Ausführung des Saldovortrags für aktuelles Geschäftsjahr bestätigen

Testverwaltung

Kundenprojekt: Füllen Sie die projektbezogenen Teile aus.

|  |  |  |  |
| --- | --- | --- | --- |
| Testfall-ID | <X.XX> | Testdatum: |  |
| Testername: |  | Dauer: |  |
| Benutzerrolle(n): |  | Zuständigkeit: | <Geben Sie den Serviceanbieter, einen Kunden oder einen Serviceanbieter zusammen mit einem Kunden an.> |

Zweck

In dieser Aktivität bestätigen Sie, dass der Saldovortrag für das aktuelle Geschäftsjahr ausgeführt wurde.

|  |
| --- |
| Hinweis Wenn in Ihrer Implementierung kein spezifischer Ledger verwendet wird, vernachlässigen Sie diesen Ledger. |

Vorgehensweise

| Testschrittnummer | Bezeichnung des Testschritts | Anweisungen | Erwartetes Ergebnis | Bestanden/Nicht bestanden/Anmerkung |
| --- | --- | --- | --- | --- |
| 1 | Anmelden | Melden Sie sich am SAP Fiori Launchpad als Hauptbuchhalter an. |  |  |
| 2 | SAP-Fiori-App aufrufen | Öffnen Sie Hauptbuchjobs einplanen(F1927). |  |  |
| 3 | Anlegen | Wählen Sie Anlegen. |  |  |
| 4 | Details eingeben | Nehmen Sie die folgenden Einträge vor, und wählen Sie Schritt 2:Jobvorlage: SaldovortragJobname: Saldovortrag |  |  |
| 5 | Details eingeben | Nehmen Sie die folgenden Einträge vor, und wählen Sie Schritt 3:Sofort starten: <markiert>. |  |  |
| 6 | Details eingeben | Geben Sie Folgendes ein, und wählen Sie Einplanen:Ledger: <Ledger>: z.B. 0LBuchungskreis: <Buchungskreis>Vortrag auf Geschäftsjahr: <Geschäftsjahr>Testlauf: Markiert. | Sie haben den Joblauf als Testlauf eingeplant. |  |
| 7 | Ergebnisse prüfen | Um die Ergebnisse Ihres Testlaufs zu überprüfen, suchen Sie Ihren Lauf im Bereich Jobs, und wählen Sie die Pfeiltaste rechts neben seiner Zeile. |  |  |
| 8 | Laufdetails | Wählen Sie die Registerkarte Laufdetails. Prüfen Sie den Status des Protokolls. |  |  |
| 9 | Produktivlauf | Um einen Produktivlauf durchzuführen, wiederholen Sie diesen Vorgang, und entmarkieren Sie Testlauf. | Sie haben den Joblauf als Produktivlauf eingeplant. |  |

## Übersichtstabelle

Dieser Umfangsbestandteil umfasst die Prozessschritte in der folgenden Tabelle:

|  |
| --- |
| Hinweis Wenn Ihr Systemadministrator Bereiche und Seiten auf dem SAP Fiori Launchpad aktiviert hat, enthält die Startseite nur die wesentlichen Apps, mit denen die typischen Aufgaben einer Benutzerrolle ausgeführt werden können.Alle anderen (suchbaren) Apps, die nicht auf der Startseite enthalten sind, finden Sie über die Suchleiste ([2434549](https://me.sap.com/notes/2434549)).Wenn Sie die Startseite personalisieren und versteckte Apps hinzufügen möchten, wechseln Sie in Ihr Benutzerprofil und wählen Sie App Finder. |

| Prozessschritt | Anwendungsrolle | Vorgang/App | Erwartete Ergebnisse |
| --- | --- | --- | --- |
| [Anlage anlegen](#unique_12) [Seite ] 12 | Anlagenbuchhalter | Öffnen Sie Anlagen verwalten(F3425A). | Anlagenstamm wird auf Buchungskreisebene (Bewertungsplanebene) angelegt |
| [Anlage ändern](#unique_13) [Seite ] 14 | Anlagenbuchhalter | Öffnen Sie Anlagen verwalten(F3425A). | Anlagenstamm wird aktualisiert. |
| [Anlage anzeigen](#unique_14) [Seite ] 15 | Anlagenbuchhalter | Öffnen Sie Anlagen verwalten(F3425A). | Anlagenstamm wird angezeigt. |
| [Anlagen sperren](#unique_15) [Seite ] 16 | Anlagenbuchhalter | Öffnen Sie Anlagen verwalten(F3425A). | Anlage wird gesperrt. |
| [Anlage löschen](#unique_16) [Seite ] 17 | Anlagenbuchhalter | Öffnen Sie Anlagen verwalten(F3425A). | Anlagenstamm wird gelöscht. |
| [Unteranlage einer Anlage anlegen](#unique_17) [Seite ] 18 | Anlagenbuchhalter | Öffnen Sie Anlagen verwalten(F3425A). | Eine Unteranlage wurde angelegt. |
| [Änderungsbelege für Anlagenstammsatz](#unique_18) [Seite ] 20 | Anlagenbuchhalter | Öffnen Sie Anlagen verwalten(F3425A). | Alle vorherigen Änderungen eines vorhandenen Anlagenstammsatzes (Haupt- oder Unteranlage) werden angezeigt. |
| [Abschreibungsschlüssel: Details anzeigen](#unique_19) [Seite ] 20 | Anlagenbuchhalter | Abschreibungsschlüssel: Details anzeigen(FAA_DEPRKEY_SHOW)Hinweis Wenn Sie den Funktionsschalter für das neue Design aktiviert haben, gilt die App Abschreibungsschlüssel: Details anzeigen(FAA_DEPRKEY_SHOW) nicht. | Mit dieser App werden die Informationen zu den Einstellungen hinter vom Standardinhalt gelieferten Abschreibungsschlüsseln bereitgestellt. |

## Testverfahren

In diesem Abschnitt werden die Testverfahren für den jeweiligen Prozessschritt beschrieben, der zum betreffenden Umfangsbestandteil gehört.

### Anlage anlegen

Testverwaltung

Kundenprojekt: Füllen Sie die projektbezogenen Teile aus.

|  |  |  |  |
| --- | --- | --- | --- |
| Testfall-ID | <X.XX> | Testdatum: |  |
| Testername: |  | Dauer: |  |
| Benutzerrolle(n): |  | Zuständigkeit: | <Geben Sie den Serviceanbieter, einen Kunden oder einen Serviceanbieter zusammen mit einem Kunden an.> |

Zweck

In dieser Aktivität können Sie einen neuen Anlagen-Hauptdatensatz im Rahmen Ihrer täglichen Arbeit anlegen.

Vorgehensweise

| Testschrittnummer | Bezeichnung des Testschritts | Anweisungen | Erwartetes Ergebnis | Bestanden/Nicht bestanden/Anmerkung |
| --- | --- | --- | --- | --- |
| 1 | Anmelden | Melden Sie sich am SAP Fiori Launchpad als Anlagenbuchhalter an. | Das SAP Fiori Launchpad wird angezeigt. |  |
| 2 | SAP-Fiori-App aufrufen | Öffnen Sie Anlagen verwalten(F3425A). | Das Bild Anlagen verwalten wird angezeigt. |  |
| 3 | Anlagenstammdetails eingeben | Wählen Sie Anlegen > Hauptnummer anlegen.Tragen Sie Folgendes ein:Buchungskreis: <Ihr Buchungskreis>Anlagenklasse: <Anlagenklasse, für die Sie eine neue Anlage anlegen möchten>Nachaktivierung: Nur erforderlich, wenn Sie diesen Stammsatz zum Buchen einer Nachaktivierung verwenden möchtenReferenzanlagenstammdaten können verwendet werden. Wenn dies erforderlich ist, sollte die Anlage, die als Referenz verwendet werden soll, im Abschnitt Referenz im Feld Anlagenhauptnummer eingegeben werden.Wählen Sie OK. | Das Bild Hauptnummer anlegen wird angezeigt. |  |
| 4 | Anlagenbeschreibung und Basismengeneinheit eingeben | Tragen Sie Folgendes ein:Beschreibung: <Die Beschreibung Ihrer Anlage>Basismengeneinheit: <Geben Sie die erforderliche Mengeneinheit ein> |  |  |
| 5 | Registerkarte "Zeitabhängige Daten" wählen | Wählen Sie die Registerkarte Zeitabhängige Daten. | Die Registerkarte Zeitabhängige Daten wird angezeigt. |  |
| 6 | Kostenstelle eingeben | Tragen Sie Folgendes ein:Kostenstelle: <Ihre Kostenstelle>PSP_ELEMENT: <Ihr PSP_Element>Hinweis Als Kostensammler für die Abschreibung können die Kostenstelle und/oder ein PSP-Element eingegeben werden. |  |  |
| 7 | Aktivierungsdatum eingeben | Sie müssen das Datum Aktiviert am nur eingeben, wenn die Anlage mit dem Flag Nachaktivierung angelegt wurde.Aktiviert am: <Ihr Aktivierungsdatum> |  |  |
| 8 | Andere Registerkarten prüfen | Wechseln Sie auf die anderen Registerkarten, und erfassen bzw. ändern Sie bei Bedarf weitere Eingaben. |  |  |
| 9 | Bewertungsparameter erfassen, prüfen oder ändern | Nehmen Sie die folgenden Einträge für alle verfügbaren Bewertungsbereiche vor:AfaSchl: <Ihr Abschreibungsschlüssel>Hinweis Wenn Sie den Funktionsschalter für das neue Design aktiviert haben, verwenden Sie anstelle des Abschreibungsschlüssels das Abschreibungsprofil.Nutz.dauer: <Nutzungsdauer in Jahren>Per: Nutzungsdauer in Perioden: | Alle erforderlichen Bewertungsparameter wurden korrekt bearbeitet. |  |
| 10 | Neuen Anlagenstamm sichern | Wählen Sie Anlegen, um Ihre Einträge zu sichern. | Der Anlagenstammsatz wird angelegt. Eine Systemmeldung bestätigt den Anlegevorgang und zeigt die Nummer der neuen Anlage an. |  |

### Anlage ändern

Testverwaltung

Kundenprojekt: Füllen Sie die projektbezogenen Teile aus.

|  |  |  |  |
| --- | --- | --- | --- |
| Testfall-ID | <X.XX> | Testdatum: |  |
| Testername: |  | Dauer: |  |
| Benutzerrolle(n): |  | Zuständigkeit: | <Geben Sie den Serviceanbieter, einen Kunden oder einen Serviceanbieter zusammen mit einem Kunden an.> |

Zweck

In dieser Aktivität können Sie vorhandene Anlagenstammsätze (Haupt- oder Unternummer) im Rahmen Ihrer täglichen Arbeit ändern.

|  |
| --- |
| Hinweis Die Anlagenklassen können Sie nur ändern, indem Sie die Daten unternehmensintern in einen neuen Anlagenstammsatz übertragen, der in der neuen Anlagenklasse angelegt wird. |

Vorgehensweise

| Testschrittnummer | Bezeichnung des Testschritts | Anweisungen | Erwartetes Ergebnis | Bestanden/Nicht bestanden/Anmerkung |
| --- | --- | --- | --- | --- |
| 1 | Anmelden | Melden Sie sich am SAP Fiori Launchpad als Anlagenbuchhalter an. | Das SAP Fiori Launchpad wird angezeigt. |  |
| 2 | SAP-Fiori-App aufrufen | Öffnen Sie Anlagen verwalten(F3425A). | Das Bild Anlagen verwalten wird angezeigt. |  |
| 3 | Anlageninformationen eingeben | Tragen Sie Folgendes ein:Buchungskreis: <Ihr Buchungskreis>Anlage: <Nummer Ihrer Anlage>Wählen Sie Start.Wählen Sie Ihre Anlagennummer aus der Tabelle über den Link mit der Anlagennummer.Wählen Sie auf dem nächsten Bild Bearbeiten. | Das Bild Anlagen verwalten wird angezeigt.Hinweis Das Anzeigen, Ändern und Löschen von Funktionen ist möglich durch die Auswahl der Anlage und der Aktion, die im Dialogfenster angezeigt werden soll. Danach wird die Aktion erneut ausgewählt. |  |
| 4 | Anlagenstamm ändern | Nehmen Sie die erforderlichen Änderungen an den Anlagenstammdaten vor. | Die erforderlichen Änderungen werden vorgenommen. |  |
| 5 | Geänderten Anlagenstamm sichern | Wählen Sie Anlegen, um Ihre Einträge zu sichern.Hinweis Das System zeigt die Meldung Erfolg an. Sie müssen Ihre Änderungen verifizieren. | Die Änderungen am Anlagenstamm werden gesichert.Die durchgeführten Änderungen werden auf der Registerkarte Änderungsbeleg angezeigt. |  |

### Anlage anzeigen

Testverwaltung

Kundenprojekt: Füllen Sie die projektbezogenen Teile aus.

|  |  |  |  |
| --- | --- | --- | --- |
| Testfall-ID | <X.XX> | Testdatum: |  |
| Testername: |  | Dauer: |  |
| Benutzerrolle(n): |  | Zuständigkeit: | <Geben Sie den Serviceanbieter, einen Kunden oder einen Serviceanbieter zusammen mit einem Kunden an.> |

Zweck

In dieser Aktivität können Sie vorhandene Anlagendatensätze (Haupt- oder Unternummer) im Rahmen Ihrer täglichen Arbeit anzeigen.

Vorgehensweise

| Testschrittnummer | Bezeichnung des Testschritts | Anweisungen | Erwartetes Ergebnis | Bestanden/Nicht bestanden/Anmerkung |
| --- | --- | --- | --- | --- |
| 1 | Anmelden | Melden Sie sich am SAP Fiori Launchpad als Anlagenbuchhalter an. | Das SAP Fiori Launchpad wird angezeigt. |  |
| 2 | SAP-Fiori-App aufrufen | Öffnen Sie Anlagen verwalten(F3425A). | Das Bild Anlagen verwalten wird angezeigt. |  |
| 3 | Anlageninformationen eingeben | Tragen Sie Folgendes ein:Buchungskreis: <Ihr Buchungskreis>Anlage: <Nummer Ihrer Anlage>Unternummer: <Ihre betreffende Anlagenunternummer>Wählen Sie Start.Wählen Sie Ihre Anlagennummer aus der Tabelle über den Link mit der Anlagennummer.Überprüfen Sie Ihren Anlagenstammsatz durch Auswählen aller Registerkarten. |  |  |

### Anlagen sperren

Testverwaltung

Kundenprojekt: Füllen Sie die projektbezogenen Teile aus.

|  |  |  |  |
| --- | --- | --- | --- |
| Testfall-ID | <X.XX> | Testdatum: |  |
| Testername: |  | Dauer: |  |
| Benutzerrolle(n): |  | Zuständigkeit: | <Geben Sie den Serviceanbieter, einen Kunden oder einen Serviceanbieter zusammen mit einem Kunden an.> |

Zweck

In dieser Aktivität können Sie vorhandene Anlagenstammsätze (Haupt- oder Unternummer) vor weiteren Zugängen sperren.

Vorgehensweise

| Testschrittnummer | Bezeichnung des Testschritts | Anweisungen | Erwartetes Ergebnis | Bestanden/Nicht bestanden/Anmerkung |
| --- | --- | --- | --- | --- |
| 1 | Anmelden | Melden Sie sich am SAP Fiori Launchpad als Anlagenbuchhalter an. | Das SAP Fiori Launchpad wird angezeigt. |  |
| 2 | SAP-Fiori-App aufrufen | Öffnen Sie Anlagen verwalten(F3425A). | Das Bild Anlagen verwalten wird angezeigt. |  |
| 3 | Anlageninformationen eingeben | Geben Sie Folgendes ein, und wählen Sie Start:Buchungskreis: <Ihr Buchungskreis>Anlage: <Nummer Ihrer Anlage> | Das Bild Anlagen verwalten wird angezeigt. |  |
| 4 | Sperrkennzeichen setzen | Wählen Sie in der Tabelle Ihre Anlagennummer aus.Wählen Sie auf dem neuen Bild die Option Sperren.Hinweis Die Meldung Anlage <Anlagennummer> gesperrt wird angezeigt. | Das Sperrkennzeichen wurde gesetzt.Die Anlage ist für weitere Zugänge gesperrt.Die durchgeführten Änderungen werden auf der Registerkarte Änderungsbeleg angezeigt. |  |

### Anlage löschen

Testverwaltung

Kundenprojekt: Füllen Sie die projektbezogenen Teile aus.

|  |  |  |  |
| --- | --- | --- | --- |
| Testfall-ID | <X.XX> | Testdatum: |  |
| Testername: |  | Dauer: |  |
| Benutzerrolle(n): |  | Zuständigkeit: | <Geben Sie den Serviceanbieter, einen Kunden oder einen Serviceanbieter zusammen mit einem Kunden an.> |

Zweck

In dieser Aktivität können Sie vorhandene Anlagenstammsätze (Haupt- oder Unternummer) löschen.

|  |
| --- |
| Hinweis Sie können ausschließlich Anlagen ohne Aktivierungsdatum und ohne Werte direkt löschen. |

Vorgehensweise

| Testschrittnummer | Bezeichnung des Testschritts | Anweisungen | Erwartetes Ergebnis | Bestanden/Nicht bestanden/Anmerkung |
| --- | --- | --- | --- | --- |
| 1 | Anmelden | Melden Sie sich am SAP Fiori Launchpad als Anlagenbuchhalter an. | Das SAP Fiori Launchpad wird angezeigt. |  |
| 2 | SAP-Fiori-App aufrufen | Öffnen Sie Anlagen verwalten(F3425A). | Das Bild Anlagen verwalten wird angezeigt. |  |
| 3 | Anlageninformationen eingeben | Geben Sie Folgendes ein, und wählen Sie Start:Buchungskreis: <Ihr Buchungskreis>Anlage: <Nummer Ihrer Anlage> |  |  |
| 4 | Löschkennzeichen setzen | Wählen Sie Ihre Anlagennummer, und wählen Sie auf dem neuen Bild Löschen. | Das Kennzeichen wurde gesetzt. |  |
| 5 | Bestätigen | Die Meldung Objekt löschen? wird auf dem Bild angezeigt. Wählen Sie Löschen, um zu bestätigen. |  |  |

### Unteranlage einer Anlage anlegen

Testverwaltung

Kundenprojekt: Füllen Sie die projektbezogenen Teile aus.

|  |  |  |  |
| --- | --- | --- | --- |
| Testfall-ID | <X.XX> | Testdatum: |  |
| Testername: |  | Dauer: |  |
| Benutzerrolle(n): |  | Zuständigkeit: | <Geben Sie den Serviceanbieter, einen Kunden oder einen Serviceanbieter zusammen mit einem Kunden an.> |

Zweck

In dieser Aktivität können Sie im Rahmen Ihrer täglichen Arbeit einen neuen Datensatz für die Unteranlage einer Anlage anlegen.

Vorgehensweise

| Testschrittnummer | Bezeichnung des Testschritts | Anweisungen | Erwartetes Ergebnis | Bestanden/Nicht bestanden/Anmerkung |
| --- | --- | --- | --- | --- |
| 1 | Anmelden | Melden Sie sich am SAP Fiori Launchpad als Anlagenbuchhalter an. | Das SAP Fiori Launchpad wird angezeigt. |  |
| 2 | SAP-Fiori-App aufrufen | Öffnen Sie Anlagen verwalten(F3425A). | Das Bild Anlagen verwalten wird angezeigt. |  |
| 3 | Hauptanlagen-Referenz eingeben | Wählen Sie auf dem Bild Anlagen verwalten die Option Anlage anlegen > Unteranlage einer Anlage anlegen.Nehmen Sie folgende Einträge vor, und wählen Sie Enter:Buchungskreis: <Ihr Buchungskreis>Anlage: <Anlagenhauptnummer, für die Sie eine Unteranlage anlegen möchten>Nachaktivierung: Nur erforderlich, wenn Sie diesen Stammsatz zum Buchen einer Nachaktivierung verwenden möchten | Das Bild Unternummer anlegen wird angezeigt.Die Registerkarte Allgemein wird angezeigt. |  |
| 4 | Allgemeine Daten eingeben | Geben Sie auf der Registerkarte Allgemein folgende Daten ein:Anlagenbezeichnung: <Die Bezeichnung Ihrer Anlage>Mengeneinheit: <Mengeneinheit>Aktiviert am: <Ihr Datum |  |  |
| 5 | Zeitabhängige Daten | Wählen Sie die Registerkarte Zeitabhängige Daten. |  |  |
| 6 | Kostenstelle oder PSP_Element | Erfassen, prüfen oder ändern Sie folgende Daten:Kostenstelle: <Ihre Kostenstelle>oder PSP_Element: <Ihr PSP_Element> |  |  |
| 7 | Andere Registerkarten prüfen | Wechseln Sie auf die anderen Registerkarten, und erfassen bzw. ändern Sie bei Bedarf weitere Eingaben. | Alle erforderlichen Stammdatenfelder enthalten Werte. |  |
| 8 | Bewertungsparameter erfassen, prüfen oder ändern | Erfassen oder bearbeiten Sie folgende Daten für alle verfügbaren Bewertungsbereiche, sofern erforderlich:AfaSchl: <Ihr Abschreibungsschlüssel>Hinweis Wenn Sie den Funktionsschalter für das neue Design aktiviert haben, verwenden Sie anstelle des Abschreibungsschlüssels das Abschreibungsprofil.Nutz.dauer: <Ihre Nutzungsdauer in Jahren>Per: <Ihre Nutzungsdauer in Perioden> | Alle erforderlichen Bewertungsparameter wurden korrekt bearbeitet. |  |
| 9 | Neue Unteranlage einer Anlage sichern | Sichern Sie Ihre Eingaben. | Die Unteranlage eines Anlagenstamms wird angelegt.Unteranlagen beginnen mit 1, z. B. xxxxx-1. |  |

### Änderungsbelege für Anlagenstammsatz

Testverwaltung

Kundenprojekt: Füllen Sie die projektbezogenen Teile aus.

|  |  |  |  |
| --- | --- | --- | --- |
| Testfall-ID | <X.XX> | Testdatum: |  |
| Testername: |  | Dauer: |  |
| Benutzerrolle(n): |  | Zuständigkeit: | <Geben Sie den Serviceanbieter, einen Kunden oder einen Serviceanbieter zusammen mit einem Kunden an.> |

Zweck

In dieser Aktivität können Sie in der Vergangenheit vorgenommene Änderungen an vorhandenen Anlagenstammsätzen (Haupt- oder Unternummer) anzeigen.

Vorgehensweise

| Testschrittnummer | Bezeichnung des Testschritts | Anweisungen | Erwartetes Ergebnis | Bestanden/Nicht bestanden/Anmerkung |
| --- | --- | --- | --- | --- |
| 1 | Anmelden | Melden Sie sich am SAP Fiori Launchpad als Anlagenbuchhalter an. | Das SAP Fiori Launchpad wird angezeigt. |  |
| 2 | SAP-Fiori-App aufrufen | Öffnen Sie Anlagen verwalten(F3425A). | Das Bild Anlagen verwalten wird angezeigt. |  |
| 3 | Anlageninformationen eingeben | Geben Sie Folgendes ein, und wählen Sie Start:Buchungskreis: <Ihr Buchungskreis>Anlagennummer: <Nummer Ihrer Anlage>Anlagenunternummer: <Ihre Anlagenunternummer> | Das Bild Änderungen der Anlagenstammsätze wird geöffnet. |  |

### Abschreibungsschlüssel: Details anzeigen

Testverwaltung

Kundenprojekt: Füllen Sie die projektbezogenen Teile aus.

|  |  |  |  |
| --- | --- | --- | --- |
| Testfall-ID | <X.XX> | Testdatum: |  |
| Testername: |  | Dauer: |  |
| Benutzerrolle(n): |  | Zuständigkeit: | <Geben Sie den Serviceanbieter, einen Kunden oder einen Serviceanbieter zusammen mit einem Kunden an.> |

Zweck

In dieser Aktivität können Sie alle vorherigen Änderungen eines vorhandenen Anlagenstammsatzes (Haupt- oder Unteranlage) anzeigen.

|  |
| --- |
| Hinweis Wenn Sie den Funktionsschalter für das neue Design aktiviert haben, gilt die App Abschreibungsschlüssel: Details anzeigen(FAA_DEPRKEY_SHOW) nicht. |

Vorgehensweise

| Testschrittnummer | Bezeichnung des Testschritts | Anweisungen | Erwartetes Ergebnis | Bestanden/Nicht bestanden/Anmerkung |
| --- | --- | --- | --- | --- |
| 1 | Anmelden | Melden Sie sich am SAP Fiori Launchpad als Anlagenbuchhalter an. | Das SAP Fiori Launchpad wird angezeigt. |  |
| 2 | SAP-Fiori-App aufrufen | Öffnen Sie Abschreibungsschlüssel: Details anzeigen(FAA_DEPRKEY_SHOW). | Die App wird geöffnet. |  |
| 3 | Anlageninformationen eingeben | Geben Sie Folgendes ein, und wählen Sie Ausführen:Bewertungsplan: <Bewertungsplan>Abschreibungsschlüssel: <Abschreibungsschlüssel> | Das Bild Abschreibungsschlüssel <XXXX> im Bewertungsplan <XXXX> wird angezeigt.Die Einstellungen hinter dem ausgewählten Abschreibungsschlüssel werden angezeigt. |  |

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
- related-to :: [[03-financial-accounting-and-close/master-data-script-create-asset-bni-sap-s-4hana-cloud-public-edition-6]]
- related-to :: [[03-financial-accounting-and-close/mds-bni-613]]
- related-to :: [[03-financial-accounting-and-close/sap-s-4hana-cloud-public-edition-mds-bni-615]]
- related-to :: [[03-financial-accounting-and-close/script-de-dados-mestre-criar-imobilizado-mds-bni-614]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/BNI_S4CLD2608_Master_Data_DE_XX.docx` — full document · extracted with `mammoth` · 33,308 chars in the whole document
