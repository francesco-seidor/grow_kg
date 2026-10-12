---
id: 06-management-accounting/stammdatenskript-leistungstarife-anlegen-sds-3kw-352
title: "Stammdatenskript: Leistungstarife anlegen – SDS (3KW) (3KW_S4CLD2608_Master_Data_DE_XX)"
description: "German master data/test script (3KW) for SAP S/4HANA Cloud Public Edition: maintaining activity-type rates (Leistungstarife) via Services, Plan and Actual apps, plus display report."
cluster: 06-management-accounting
tags: [kb/management-accounting, topic/cost-rates]
aliases: [3KW_S4CLD2608_Master_Data_DE_XX]
keywords: ["CO Cost Rates (Service, Plan and Actual)", activity rates, service rates, plan rates, actual rates, intercompany postings, margin accounts, automatic account determination, rate display report, business roles]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/3KW_S4CLD2608_Master_Data_DE_XX.docx]
confidence: high
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-352
topic: 06-management-accounting/cost-rates
language: DE
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Stammdatenskript: Leistungstarife anlegen – SDS (3KW) (3KW_S4CLD2608_Master_Data_DE_XX)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/3KW_S4CLD2608_Master_Data_DE_XX.docx`, extracted with `mammoth`. Grouped under **CO Cost Rates (Service, Plan and Actual)** in Management Accounting. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

| <!-- image omitted: unnamed --> | StammdatenskriptSAP S/4HANA Cloud Public Edition - 02-07-26 |
| --- | --- |
|  | Leistungstarife anlegen – SDS (3KW) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Inhaltsverzeichnis

[1 Zweck 2](#_Toc233889669)

[2 Voraussetzungen 3](#_Toc233889670)

[2.1 Systemzugriff 3](#_Toc233889671)

[2.2 Rollen 3](#_Toc233889672)

[2.3 Vorbereitende Schritte 3](#_Toc233889673)

[2.3.1 Optional: Buchungskreisverrechnungskonten pflegen (nur für buchungskreisübergreifende Buchungen) 3](#_Toc233889674)

[2.3.2 Optional: Margin-Konten pflegen (nur für buchungskreisübergreifende Buchungen mit buchungskreisübergreifenden Tarifen) 5](#_Toc233889675)

[3 Übersichtstabelle 7](#_Toc233889676)

[4 Testverfahren 8](#_Toc233889677)

[4.1 Leistungstarife verwalten - Services 8](#_Toc233889678)

[4.2 Leistungstarife verwalten – Plan 11](#_Toc233889679)

[4.3 Leistungstarife verwalten – Ist 12](#_Toc233889680)

[5 Analysen 14](#_Toc233889681)

[5.1 Leistungstarife anzeigen 14](#_Toc233889682)

## Zweck

Es stehen die folgenden Apps zur Verfügung, um Kostensätze (Tarife) zu pflegen. Jede App erfüllt einen anderen Zweck, der davon abhängt, wie die Sätze definiert werden und welche Objekte Leistungsverrechnungen empfangen können.

| App | Betroffene Umfangsbestandteile | Kommentare |
| --- | --- | --- |
| Leistungstarife verwalten - Services(F3161) | Zeiterfassung (1Q4)Gemeinkostenrechnung (J54)Zeiterfassung – Projektbezogene Dienstleistungen (J12)Serviceauftragsabwicklung und -überwachung (3D2) | Zeiterfassung |
| Leistungstarife verwalten - Plan(F3162) | Standardkostenberechnung (BEG)Periodenabschluss – Werk (BEI)Periodenabschluss – Instandhaltungsaufträge (BF7) | Fertigungs-, Auftragsplan- und Istrückmeldungen |
| Leistungstarife verwalten - Ist(F3422) | Istkalkulation (33Q) | Wird verwendet, um Istkostensätze für Leistungen von Kostenstellen zu erfassen.Istkostensätze sind nur erforderlich, wenn ein Kunde die Istkalkulation verwenden möchte. |

Dieses Dokument enthält eine detaillierte Ablaufbeschreibung, anhand deren der Umfangsbestandteil nach der Lösungsaktivierung getestet werden kann; außerdem bildet es den vordefinierten Umfang der Lösung ab. Jeder Prozessschritt, Report oder Bestandteil wird in einem eigenen Abschnitt beschrieben, in dem die Interaktionen im System (Testschritte) tabellarisch dargestellt sind. Schritte, die nicht im Prozessumfang enthalten sind, aber zu Testzwecken benötigt werden, sind entsprechend gekennzeichnet. Projektspezifische Schritte sind zu ergänzen.

|  |
| --- |
| Hinweis Die Werte in diesem Testskript (Dezimalschreibweise, Datumsformate usw.) werden in US-amerikanischer Standardschreibweise dargestellt. Wenn Ihr Testsystem so eingerichtet ist, dass es eine andere Schreibweise verwendet, geben Sie die entsprechenden Werte ein. |

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

| Name (Rollenvorlage) | ID (Rollenvorlage) | Name (Launchpad-Bereich) | ID (Launchpad-Bereich) | Anmeldung |
| --- | --- | --- | --- | --- |
| Gemeinkostencontroller | SAP_BR_OVERHEAD_ACCOUNTANT | Gemeinkostenrechnung | SAP_BR_OVERHEAD_ACCOUNTANT |  |

### Vorbereitende Schritte

#### Optional: Buchungskreisverrechnungskonten pflegen (nur für buchungskreisübergreifende Buchungen)

Verwendung

Mit dieser Aktivität können Sie Verrechnungskonten für buchungskreisübergreifende Buchungen (ICO-Buchungen) anlegen und aktualisieren. Die ICO-Verrechnungskonten werden aus dem Sachkonto des Vorgangs abgeleitet.

Vorgehensweise

Wählen Sie abhängig von Ihrer Konfigurationsumgebung für SAP S/4HANA Cloud Public Edition eine der folgenden Optionen:

Lösung konfigurieren:

1. Melden Sie sich am SAP Fiori Launchpad als Konfigurationsexperte – Geschäftsprozesskonfiguration an.
2. Öffnen Sie Lösung verwalten(F1241).
3. Wählen Sie bei Bedarf Lokale Version festlegen, um das Land zu ändern.
4. Öffnen Sie Lösung konfigurieren.
5. Wählen Sie im Abschnitt Konfigurationsschritte in der Spalte Name für die Zeile Automatische Kontenfindung (100297) die Option Konfigurieren.
6. Fahren Sie mit der Vorgehensweise in der folgenden Tabelle fort.

SAP Central Business Configuration:

1. Melden Sie sich an der Projekterfahrung in SAP Central Business Configuration an.
2. Wechseln Sie zur App Business Processes Configuration. Um die Aktivität in der Baumsicht zu finden, suchen Sie nach der Aktivität Automatic Account Determination.
3. Wählen Sie Open Documentation für die gefundene Position, um weitere Details zu dieser Konfigurationsaktivität anzuzeigen.
4. Wählen Sie den Link, um direkt zum SAP S/4HANA Cloud Public Edition-System zu navigieren. Melden Sie sich am SAP Fiori Launchpad als Konfigurationsexperte – Geschäftsprozesskonfiguration an.
5. Fahren Sie mit der Vorgehensweise in der folgenden Tabelle fort.

| Schrittnummer | Schrittname | Anweisung | Erwartetes Ergebnis | Bestanden/Nicht bestanden/Anmerkung |
| --- | --- | --- | --- | --- |
| 1 | Bereich auswählen | Nehmen Sie für die angezeigte Zeile folgende Einträge vor, und wählen Sie Schritt 2:Bereich: ControllingUnterbereich: KostenstellenrechnungProzess: Buchungskreisverrechnungskonten für Istbuchungen zuordnen |  |  |
| 2 | Parameter auswählen | Nehmen Sie die folgenden Einträge vor, und wählen Sie Schritt 3:Kontenplan: YCOA |  |  |
| 3 | Kontenfindung pflegen | Fügen Sie ein Konto hinzu, das für den ICO-Ausgleich relevant ist.Hinweis Der Standardinhalt wird mit dem Verrechnungskonto 68888800 - Unternehmensübergreif. Verrechnungskonto - Reise und 99999900 - Unternehmensübergr. Verrechnungskonto - Beratung ausgeliefert. Sie können dies als Referenz verwenden, um bei Bedarf Ihre eigenen Konten anzulegen (mit Sachkonto Typ N: Nicht operatives Aufwands-/Ertragskonto). |  |  |

#### Optional: Margin-Konten pflegen (nur für buchungskreisübergreifende Buchungen mit buchungskreisübergreifenden Tarifen)

Verwendung

Mit dieser Aktivität können Sie Margin-Konten für buchungskreisübergreifende Buchungen (ICO-Buchungen) anlegen und aktualisieren. Dieser Schritt ist erforderlich, wenn Sie ICO-Tarife pflegen und buchen. Die Margin-Verrechnungssachkonten werden auf Basis des Leistungsverrechnungssachkontos abgeleitet.

Vorgehensweise

Wählen Sie abhängig von Ihrer Konfigurationsumgebung für SAP S/4HANA Cloud Public Edition eine der folgenden Optionen:

Lösung konfigurieren:

1. Melden Sie sich am SAP Fiori Launchpad als Konfigurationsexperte – Geschäftsprozesskonfiguration an.
2. Öffnen Sie Lösung verwalten(F1241).
3. Wählen Sie bei Bedarf Lokale Version festlegen, um das Land zu ändern.
4. Öffnen Sie Lösung konfigurieren.
5. Wählen Sie im Abschnitt Konfigurationsschritte in der Spalte Name für die Zeile Automatische Kontenfindung (100297) die Option Konfigurieren.
6. Fahren Sie mit der Vorgehensweise in der folgenden Tabelle fort.

SAP Central Business Configuration:

1. Melden Sie sich an der Projekterfahrung in SAP Central Business Configuration an.
2. Um die Aktivität in der Baumsicht zu finden, suchen Sie nach der Aktivität Automatic Account Determination.
3. Wählen Sie Open Documentation für die gefundene Position, um weitere Details zu dieser Konfigurationsaktivität anzuzeigen.
4. Wählen Sie den Link, um direkt zum SAP S/4HANA Cloud Public Edition-System zu navigieren. Melden Sie sich am SAP Fiori Launchpad als Konfigurationsexperte – Geschäftsprozesskonfiguration an.
5. Fahren Sie mit der Vorgehensweise in der folgenden Tabelle fort.

| Schrittnummer | Schrittname | Anweisung | Erwartetes Ergebnis | Bestanden/Nicht bestanden/Anmerkung |
| --- | --- | --- | --- | --- |
| 1 | Bereich auswählen | Nehmen Sie für die angezeigte Zeile folgende Einträge vor, und wählen Sie Schritt 2:Bereich: ControllingUnterbereich: KostenstellenrechnungProzess: Unternehmensübergreifende Margin-Konten zuordnen |  |  |
| 2 | Parameter auswählen | Nehmen Sie die folgenden Einträge vor, und wählen Sie Schritt 3:Kontenplan: YCOA |  |  |
| 3 | Kontenfindung pflegen | Fügen Sie ein Konto hinzu, das für die unternehmensübergreifende Marge für das Sachkonto Leistungsverrechnung relevant ist.Hinweis Der Standardinhalt wird mit dem Margin-Konto "97777700 - Unternehmensübergreifende Marge" übertragen. Sie können dies als Referenz verwenden, um bei Bedarf Ihr eigenes Margin-Konto anzulegen (mit Sachkonto P: Primärkosten und Erlös). |  |  |

## Übersichtstabelle

Dieser Umfangsbestandteil setzt sich aus mehreren Prozessschritten zusammen, die in der folgenden Tabelle aufgelistet sind:

|  |
| --- |
| Hinweis Wenn Ihr Systemadministrator Bereiche und Seiten auf dem SAP Fiori Launchpad aktiviert hat, enthält die Startseite nur die wesentlichen Apps, mit denen die typischen Aufgaben einer Benutzerrolle ausgeführt werden können.Alle anderen (suchbaren) Apps, die nicht auf der Startseite enthalten sind, finden Sie über die Suchleiste ([2434549](https://me.sap.com/notes/2434549)).Wenn Sie die Startseite personalisieren und versteckte Apps hinzufügen möchten, wechseln Sie in Ihr Benutzerprofil und wählen Sie App Finder. |

| Prozessschritt | Benutzerrolle | Vorgang/App | Erwartete Ergebnisse |
| --- | --- | --- | --- |
| [Leistungstarife verwalten - Services](#unique_8) [Seite ] 8 | Gemeinkostencontroller | Leistungstarife verwalten - Services(F3161) | Die Services-Kostensätze werden gepflegt. |
| [Leistungstarife verwalten – Plan](#unique_9) [Seite ] 11 | Gemeinkostencontroller | Leistungstarife verwalten - Plan(F3162) | Die Plankostensätze werden gepflegt. |
| [Leistungstarife verwalten – Ist](#unique_10) [Seite ] 12 | Gemeinkostencontroller | Leistungstarife verwalten - Ist(F3422) | Die Istkostensätze werden gepflegt. |

## Testverfahren

### Leistungstarife verwalten - Services

Testverwaltung

Kundenprojekt: Füllen Sie die projektbezogenen Teile aus.

|  |  |  |  |
| --- | --- | --- | --- |
| Testfall-ID | <X.XX> | Testdatum: |  |
| Testername: |  | Dauer: |  |
| Benutzerrolle(n): |  | Zuständigkeit: | <Geben Sie den Serviceanbieter, einen Kunden oder einen Serviceanbieter zusammen mit einem Kunden an.> |

Kontext

Mithilfe dieser App erfassen Sie Leistungstarife anhand verschiedener Kriterien. Die Leistungstarife werden in der Leistungsverrechnung mit den folgenden Empfängerkontierungen über Zeiterfassung oder direkte Leistungsverrechnung verwendet:

- Kostenstellen
- Projekt-PSP-Elemente
- Serviceaufträge

Mit dieser App können Sie Leistungstarife für Servicekostenstufen und einzelne Mitarbeiter definieren, sodass diese von Professional-Services-Anbietern verwendet werden können. Sie kann allerdings auch von produzierenden Unternehmen verwendet werden, wenn diese Leistungstarife für Servicekostenstufen und Mitarbeiter brauchen.

Für die Preispflege stehen Ihnen folgende Felder zur Verfügung:

- Buchungskreis (Bereitstellung) – immer gefüllt, daher nicht relevant für die Zugriffsfolge
- Zu fakturierender Buchungskreis (Empfang)
- ICO-Preis (Kennzeichen)
- Kostenstelle (Bereitstellung)
- Leistungsart (Bereitstellung)
- Servicekostenstufen (Bereitstellung)
- Personalnummer (Bereitstellung)
- Workitem (neu) (Empfang)
- PSP-Element (Empfang)

Die Sortierung der Liste gibt die Schlüssel mit der höchsten Priorität am Ende der Liste aus (PSP-Element).

Beim Aktualisieren der Preistabelle werden die folgenden Regeln überprüft.

- Senderbuchungskreis ist erforderlich
- Eins oder mehrere der folgenden Felder müssen gefüllt werden: Leistungsart, Servicekostenstufe oder Personalnummer (nur die Kostenstelle wird nicht unterstützt)
- Die Felder Personalnummer und Kostenstelle schließen einander als Schlüsselfelder für einen Tarif aus. Entweder verfügt die Person über einen bestimmten Leistungstarif, oder es gilt der durchschnittliche Tarif der Kostenstelle.
- Die Felder Personalnummer und Servicekostenstufe schließen einander als Schlüsselfelder für einen Tarif aus. Entweder verfügt die Person über einen bestimmten Leistungstarif, oder es gilt der durchschnittliche Tarif der Servicekostenstufe.
- Kostenstelle und Servicekostenstufe sind eine zulässige Schlüsselkombination
- Kostenstellenarten, die in der Leistungsart definiert sind, steuern die zulässigen Kombinationen aus Kostenstelle und Leistungsart.
- Wenn ein buchungskreisinterner Leistungstarif eingegeben wird, bleibt das empfangende Unternehmen leer
- Für unternehmensinterne und buchungskreisübergreifende Leistungsverrechnungen können PSP-spezifische Leistungstarife verwendet werden. Wenn ein empfangendes Unternehmen und ein PSP-Element eingegeben werden, prüft das System, ob das PSP-Element dem empfangenden Unternehmen zugeordnet ist (das System leitet das empfangende Unternehmen nicht automatisch aus dem PSP-Element ab, da dies zu Problemen mit migrierten Leistungstarifen führen kann).
- Prüfen und ICO-Kennzeichen setzen
    - Wenn der empfangende Buchungskreis leer ist, verwenden Sie das ICO-Kennzeichen aus den Benutzereingaben
    - Wenn der empfangende Buchungskreis nicht mit dem Senderbuchungskreis übereinstimmt, setzen Sie das ICO-Kennzeichen auf wahr
    - Ist das nicht der Fall, setzen Sie das ICO-Kennzeichen auf falsch

| Kostenstelle | Aktivitätsart | Servicekostenstufe | Personalnummer (Mitarbeiter) | Workitem (Empfang) | PSP-Element (Empfang) | Zu fakturierender Buchungskreis (Empfang) | Anmerkung |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Sender | Empfänger |  |  |  |  |  |  |
|  | X |  |  |  |  |  | Mindestens ein Feld muss gefüllt werden (Leistungsart, Servicekostenstufe, Personalnummer) |
|  |  | X |  |  |  |  |  |
| NIE |  | NIE | X |  |  |  |  |
| NIE | X | NIE | X |  |  |  | Personalnummer ohne Kostenstelle, ohne Servicekostenstufe |
| X | X |  |  |  |  |  | KSt. + Kontotyp |
| X |  | X |  |  |  |  | KSt. + Servicekostenstufe |
| X | X | X |  |  |  |  | KSt. + Kontotyp + Servicekostenstufe |
|  | X | X |  |  |  |  | Kontotyp + Servicekostenstufe |
|  | X |  |  | (X) | (X) |  | PSP oder Workitem kann gefüllt sein |
|  |  | X |  | (X) | (X) |  |  |
| NIE |  | NIE | X | (X) | (X) |  |  |
| NIE | X | NIE | X | (X) | (X) |  |  |
| X | X |  |  | (X) | (X) |  |  |
| X |  | X |  | (X) | (X) |  |  |
| X | X | X |  | (X) | (X) |  |  |
|  | X | X |  | (X) | (X) |  |  |
|  | X |  |  | (X) | (X) | X | ICO-Sätze |
|  |  | X |  | (X) | (X) | X |  |
| NIE |  | NIE | X | (X) | (X) | X |  |
| NIE | X | NIE | X | (X) | (X) | X |  |
| X | X |  |  | (X) | (X) | X |  |
| X |  | X |  | (X) | (X) | X |  |
| X | X | X |  | (X) | (X) | X |  |
|  | X | X |  | (X) | (X) | X |  |

Vorgehensweise

| Testschrittnummer | Bezeichnung des Testschritts | Anweisungen | Erwartetes Ergebnis | Bestanden/Nicht bestanden/Anmerkung |
| --- | --- | --- | --- | --- |
| 1 | Anmelden | Melden Sie sich am SAP Fiori Launchpad als Gemeinkostencontroller an. |  |  |
| 2 | SAP-Fiori-App aufrufen | Öffnen Sie Leistungstarife verwalten - Services(F3161). | Das Bild Leistungstarife verwalten - Services wird angezeigt. |  |
| 3 | Buchungskreis | Geben Sie folgende Daten ein, und wählen Sie Hinzufügen:Buchungskreis: <Buchungskreis> |  |  |
| 4 | Servicekostensätze pflegen | Geben Sie folgende Daten ein, und wählen Sie Sichern:Empfangendes Unternehmen: <leer lassen>Hinweis Dieses Feld sollte nur bei buchungskreisübergreifenden Leistungstarifen verwendet werden. Andernfalls lassen Sie dieses Feld leer.Kostenstelle: <Kostenstelle>Leistungsart: <Leistungsart>PSP-Element: <dies ist ein optionales Feld>Von Geschäftsjahr: <aktuelles Jahr>Von-Periode: <laufende Periode>Kurs: 100Hinweis Dieser Kurs wird für Buchungen in alle Ledger verwendet.Währung: <Währung>Per: 1Leistungseinheit: H | Die Leistungstarife werden angelegt. |  |

### Leistungstarife verwalten – Plan

Testverwaltung

Kundenprojekt: Füllen Sie die projektbezogenen Teile aus.

|  |  |  |  |
| --- | --- | --- | --- |
| Testfall-ID | <X.XX> | Testdatum: |  |
| Testername: |  | Dauer: |  |
| Benutzerrolle(n): |  | Zuständigkeit: | <Geben Sie den Serviceanbieter, einen Kunden oder einen Serviceanbieter zusammen mit einem Kunden an.> |

Kontext

Mit dieser Aktivität planen Sie Leistungstarife für Kostenstellenaktivitäten in einer Fertigungsumgebung. Die Tarife werden für folgende Zwecke verwendet:

- Leistungsverrechnungen auf Fertigungsaufträge und Instandhaltungsaufträge
- Materialkostenkalkulation

Vorgehensweise

| Testschrittnummer | Bezeichnung des Testschritts | Anweisungen | Erwartetes Ergebnis | Bestanden/Nicht bestanden/Anmerkung |
| --- | --- | --- | --- | --- |
| 1 | Anmelden | Melden Sie sich am SAP Fiori Launchpad als Gemeinkostencontroller an. |  |  |
| 2 | SAP-Fiori-App aufrufen | Öffnen Sie Leistungstarife verwalten - Plan(F3162). | Das Bild Leistungstarife verwalten - Plan wird angezeigt. |  |
| 3 | Hinzufügen | Wählen Sie Hinzufügen. |  |  |
| 4 | Planleistungstarife pflegen | Geben Sie folgende Daten ein, und wählen Sie Sichern:Kostenstelle: <Kostenstelle>Leistungsart: <Leistungsart>Von Geschäftsjahr: <aktuelles Jahr>Von-Periode: <laufende Periode>Währung: <Währung>Festbetrag: <Betrag>Variable Rate: <Betrag>Hinweis Dieser Kurs wird für Buchungen in alle Ledger verwendet. | Die Plankostensätze werden gepflegt. |  |

### Leistungstarife verwalten – Ist

Testverwaltung

Kundenprojekt: Füllen Sie die projektbezogenen Teile aus.

|  |  |  |  |
| --- | --- | --- | --- |
| Testfall-ID | <X.XX> | Testdatum: |  |
| Testername: |  | Dauer: |  |
| Benutzerrolle(n): |  | Zuständigkeit: | <Geben Sie den Serviceanbieter, einen Kunden oder einen Serviceanbieter zusammen mit einem Kunden an.> |

Kontext

Diese Aktivität dient zum Erfassen von Istkostensätzen für Leistungen von Kostenstellen, die in der Istkalkulation verwendet werden. Istleistungstarife können nach Ledger gepflegt werden.

Vorgehensweise

| Testschrittnummer | Bezeichnung des Testschritts | Anweisungen | Erwartetes Ergebnis | Bestanden/Nicht bestanden/Anmerkung |
| --- | --- | --- | --- | --- |
| 1 | Anmelden | Melden Sie sich am SAP Fiori Launchpad als Gemeinkostencontroller an. |  |  |
| 2 | SAP-Fiori-App aufrufen | Öffnen Sie Leistungstarife verwalten - Ist(F3422). | Das Bild Leistungstarife verwalten - Ist wird angezeigt. |  |
| 3 | Hinzufügen | Wählen Sie Hinzufügen. |  |  |
| 4 | Istleistungstarife pflegen | Geben Sie folgende Daten ein, und wählen Sie Sichern:Kostenstelle: <Kostenstelle>Leistungsart: <Leistungsart>Ledger: <z.B. 0L oder Ihr führendes Ledger>HinweisWenn Sie die Berechnung des Istleistungstarifs verwenden, berechnet das System die Istleistungstarife pro Ledger. Wenn Sie automatisch berechnete Leistungstarife anzeigen oder korrigieren möchten, müssen Sie ein Ledger eingeben. Istleistungstarife mit leerem Ledger-Feld werden für Buchungen in alle Ledger verwendet. Wenn ledgerspezifische Istleistungstarife vorhanden sind, verwendet das System die ledgerspezifischen Tarife.Um die Ledger-Spalte anzuzeigen, passen Sie die Einstellungen in der Leistungstarifliste an, und wählen Sie das Ledger aus.Von Geschäftsjahr: <aktuelles Jahr>Von-Periode: <laufende Periode>Währung: <Währung>Festbetrag: <Betrag>Variable Rate: <Betrag>Hinweis Dieser Tarif wird für Buchungen in alle Ledger verwendet. | Die Istkostensätze werden gepflegt. |  |

## Analysen

### Leistungstarife anzeigen

Zweck

Mit diesem Bericht können Sie die verschiedenen Leistungstarifarten auswählen und anzeigen.

Voraussetzungen

Leistungstarife müssen bereits vorhanden sein.

Vorgehensweise

| Testschrittnummer | Bezeichnung des Testschritts | Anweisung | Erwartetes Ergebnis | Bestanden/Nicht bestanden/Anmerkung |
| --- | --- | --- | --- | --- |
| 1 | Anmelden | Melden Sie sich als Gemeinkostencontroller am SAP Fiori Launchpad an. |  |  |
| 2 | SAP-Fiori-App aufrufen | Öffnen Sie Leistungstarife anzeigen(F5150). | Das Bild Leistungstarife anzeigen wird angezeigt. |  |
| 3 | Selektionskriterien | Geben Sie folgende Daten ein, und wählen Sie Start.Ledger: <Lassen Sie das Feld leer.>Hinweis Wenn Sie das Selektionsfeld leer lassen, werden Tarife angezeigt, die identisch sind und für alle Ledger gelten (z.B. Plantarif). Die Angabe eines Ledgers in der Selektion schränkt die Anzeige der Leistungstarife auf die Tarife ein, die für die ausgewählten Ledger gepflegt wurden und auf Isttarife anwendbar sind.Kostenstelle: <z.B. 10101101>Leistungsart: <z.B. 11>Von Geschäftsjahresperiode: <laufende Periode>Bis Geschäftsjahresperiode: <laufende Periode> |  |  |

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
- related-to :: [[06-management-accounting/co-mds-3kw-355]]
- related-to :: [[06-management-accounting/co-mds-3kw-357]]
- related-to :: [[06-management-accounting/crear-tasas-de-coste-co-mds-3kw-354]]
- related-to :: [[06-management-accounting/master-data-script-create-co-cost-rates-mds-3kw-353]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/3KW_S4CLD2608_Master_Data_DE_XX.docx` — full document · extracted with `mammoth` · 23,965 chars in the whole document
