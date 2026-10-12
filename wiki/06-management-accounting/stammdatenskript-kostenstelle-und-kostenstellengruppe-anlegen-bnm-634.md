---
id: 06-management-accounting/stammdatenskript-kostenstelle-und-kostenstellengruppe-anlegen-bnm-634
title: "Stammdatenskript: Kostenstelle und Kostenstellengruppe anlegen (BNM) (BNM_S4CLD2608_Master_Data_DE_XX)"
description: "German SAP S/4HANA Cloud Public Edition master data script (BNM) for creating cost centers and cost center groups, with test steps and where-used analysis; dated 02-07-26."
cluster: 06-management-accounting
tags: [kb/management-accounting, topic/cost-centers-and-groups]
aliases: [BNM_S4CLD2608_Master_Data_DE_XX]
keywords: [Cost Centers and Cost Center Groups, cost centers, cost center groups, standard hierarchy, global hierarchies, where-used analysis, master data scripts, business roles, master data replication, overhead cost accounting]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/BNM_S4CLD2608_Master_Data_DE_XX.docx]
confidence: high
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-634
topic: 06-management-accounting/cost-centers-and-groups
language: DE
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Stammdatenskript: Kostenstelle und Kostenstellengruppe anlegen (BNM) (BNM_S4CLD2608_Master_Data_DE_XX)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/BNM_S4CLD2608_Master_Data_DE_XX.docx`, extracted with `mammoth`. Grouped under **Cost Centers and Cost Center Groups** in Management Accounting. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

| <!-- image omitted: unnamed --> | StammdatenskriptSAP S/4HANA Cloud Public Edition - 02-07-26 |
| --- | --- |
|  | Kostenstelle und Kostenstellengruppe anlegen – SDS (BNM) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Inhaltsverzeichnis

[1 Verwendungszweck 2](#_Toc233889992)

[2 Voraussetzungen 3](#_Toc233889993)

[2.1 Systemzugriff 3](#_Toc233889994)

[2.2 Rollen 3](#_Toc233889995)

[2.3 Erforderliche Organisationseinheiten 3](#_Toc233889996)

[2.4 Obligatorische und optionale Stammdaten 4](#_Toc233889997)

[2.5 Wesentliche Parameter für die Datenerstellung 4](#_Toc233889998)

[3 Übersichtstabelle 5](#_Toc233889999)

[4 Testverfahren 6](#_Toc233890000)

[4.1 Kostenstellenstammdaten anlegen 6](#_Toc233890001)

[4.2 Kostenstellengruppen-Stammdatensatz anlegen 8](#_Toc233890002)

[4.3 Analysen 10](#_Toc233890003)

[4.3.1 Verwendungsnachweis - Kostenstellen Ist 10](#_Toc233890004)

[5 Anhang 12](#_Toc233890005)

[5.1 Kostenstellenreplikation aus SAP S/4HANA Cloud Public Edition nach SAP Master Data Integration (optional) 12](#_Toc233890006)

## Verwendungszweck

Kostenstellen stellen Verantwortungsbereiche/Organisationseinheiten dar, denen Kosten zugeordnet werden können. Die Unterteilung einer Organisation in Kostenstellen dient mehreren Zielen.

Durch die Zuordnung der Kosten zu Kostenstellen kann untersucht werden, wo im Unternehmen welche Kosten angefallen sind.

Werden die Kosten auf der Ebene von Kostenstellen geplant, ist eine Kontrolle der Wirtschaftlichkeit am Ort der Kostenentstehung möglich.

Sollen die Gemeinkosten möglichst genau den einzelnen Produkten, Dienstleistungen oder Marktsegmenten zugeordnet werden, erfolgt die Weiterverrechnung der Kosten an diejenigen Kostenstellen, die unmittelbar an der Erstellung der Produkte bzw. Dienstleistungen mitwirken. Von diesen Kostenstellen können Leistungen und Kosten dann mittels verschiedener Verfahren den jeweiligen Produkten, Dienstleistungen und Marktsegmenten direkt zugerechnet werden.

So lassen sich Halb- und Fertigerzeugnisse im Produktkosten-Controlling (CO-PC) bewerten und die Deckungsbeiträge der Marktsegmente in der Ergebnisrechnung (CO-PA) ermitteln.

Kostenstellengruppen stellen eine hierarchische Struktur von Kostenstellen dar, die als Standardhierarchie bezeichnet wird. Jede angelegte Kostenstelle muss einer Gruppe in der Standardhierarchie zugeordnet werden. Dadurch wird sichergestellt, dass die Standardhierarchie alle Kostenstellen des Kostenrechnungskreises enthält. Bei Auswertungen innerhalb der Standardhierarchie erfasst das SAP-System so alle Kostenstellen.

Beachten Sie, dass Kostenstellen beliebig vielen alternativen Gruppen zugeordnet werden können. Allerdings können bei der Pflege der Standardhierarchie keine alternativen Gruppen erstellt werden.

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

### Erforderliche Organisationseinheiten

Die Organisationsstruktur und die Stammdaten Ihres Unternehmens wurden bei der Implementierung in Ihrem ERP-System angelegt. Die Organisationsstruktur gibt den Aufbau Ihres Unternehmens wieder. Die Stammdaten stehen für Kostenstellen und Kostenstellengruppen, je nach betrieblichem Schwerpunkt Ihres Unternehmens.

| Datenobjekt | Verwendet im Datensegment | Obligatorisch / optional | Kommentare |
| --- | --- | --- | --- |
| Kostenrechnungskreis | Allgemeine Daten | Obligatorisch |  |
| Buchungskreis | Organisationseinheiten | Obligatorisch |  |

### Obligatorische und optionale Stammdaten

Kostenstellen- und Kostenstellengruppen-Stammdatensätze können auf andere Stammdaten verweisen. Die folgende Tabelle bietet eine Übersicht über die optionalen und obligatorischen Stammdatenobjekte, die in einem Kostenstellenstammdatensatz enthalten sein müssen.

| Stammdatenobjekt | Verwendet im Datensegment | Obligatorisch / optional | Kommentare |
| --- | --- | --- | --- |
| Hierarchiebereich | Organisationseinheiten | obligatorisch |  |
| Geschäftsbereich | Organisationseinheiten | optional |  |
| Funktionsbereich | Organisationseinheiten | optional |  |
| Profitcenter | Organisationseinheiten | obligatorisch |  |

### Wesentliche Parameter für die Datenerstellung

Dieser Umfangsbestandteil hat keine Voraussetzungen.

## Übersichtstabelle

Dieser Umfangsbestandteil umfasst mehrere Prozessschritte, die in der folgenden Tabelle aufgelistet sind:

|  |
| --- |
| Hinweis Wenn Ihr Systemadministrator Bereiche und Seiten auf dem SAP Fiori Launchpad aktiviert hat, enthält die Startseite nur die wesentlichen Apps, mit denen die typischen Aufgaben einer Benutzerrolle ausgeführt werden können.Alle anderen (suchbaren) Apps, die nicht auf der Startseite enthalten sind, finden Sie über die Suchleiste ([2434549](https://me.sap.com/notes/2434549)).Wenn Sie die Startseite personalisieren und versteckte Apps hinzufügen möchten, wechseln Sie in Ihr Benutzerprofil und wählen Sie App Finder. |

| Prozessschritt | Anwendungsrolle | Vorgang/App | Erwartete Ergebnisse |
| --- | --- | --- | --- |
| [Kostenstellenstammdaten anlegen](#unique_9) [Seite ] 6 | Gemeinkostencontroller | Kostenstellen verwalten - Alte Version(F1443A) | Kostenstellen können gemäß neuen geschäftlichen Anforderungen angelegt werden. |
| [Kostenstellengruppen-Stammdatensatz anlegen](#unique_10) [Seite ] 8 | Gemeinkostencontroller | Globale Hierarchien verwalten(F2918) oder Kostenstellengruppen verwalten(F1024) | Kostenstellengruppen können gemäß neuen geschäftlichen Anforderungen angelegt werden. |
| [Verwendungsnachweis - Kostenstellen Ist](#unique_11) [Seite ] 10 | Gemeinkostencontroller | Kostenstellen verwalten - Alte Version(F1443A) |  |

## Testverfahren

In diesem Abschnitt werden die Abläufe für jeden Prozessschritt beschrieben, der zu diesem Umfangsbestandteil gehört. Sie können diese Abläufe auch zum Testen der Stammdatenerzeugung verwenden.

### Kostenstellenstammdaten anlegen

Testverwaltung

Kundenprojekt: Füllen Sie die projektbezogenen Teile aus.

|  |  |  |  |
| --- | --- | --- | --- |
| Testfall-ID | <X.XX> | Testdatum: |  |
| Testername: |  | Dauer: |  |
| Benutzerrolle(n): |  | Zuständigkeit: | <Geben Sie den Serviceanbieter, einen Kunden oder einen Serviceanbieter zusammen mit einem Kunden an.> |

|  |
| --- |
| Hinweis Standardhierarchieknoten 1~Ab der Edition 2502 wird für neue Kundeninstallationen die Standardhierarchie mit der Funktion für die globale Hierarchie mit dem Wert 1~ ausgeliefert. Frühere Kunden können weiterhin den setbasierten Standardhierarchiewert 0001 verwenden.Wenn Sie die erste Kostenstelle im Produktivsystem anlegen, müssen Sie im Feld Standardhierarchieknoten im Dropdown-Menü der Suche den Wert 1~ eingeben. Dadurch wird der oberste Knoten 1~ in der Standardhierarchie festgelegt. Sobald die erste Kostenstelle im System angelegt wurde, wird automatisch auch der Standardhierarchieknoten 1~ angelegt. Ab 2502 Edition, SAP S/4HANA Cloud Public Edition Public Edition wird Standard-Content immer mit der Standardhierarchie 1~ ausgeliefert und muss als oberste Ebene verwendet werden. |

Vorgehensweise

| Testschrittnummer | Bezeichnung des Testschritts | Anweisung | Erwartetes Ergebnis | Kommentare |
| --- | --- | --- | --- | --- |
| 1 | Anmelden | Melden Sie sich am SAP Fiori Launchpad als Gemeinkostencontroller an. | Das SAP Fiori Launchpad wird angezeigt. |  |
| 2 | SAP-Fiori-App aufrufen | Öffnen Sie Kostenstellen verwalten - Alte Version(F1443A). | Die App wird geöffnet. |  |
| 3 | Neue Kostenstelle anlegen | Wählen Sie Anlegen, um eine neue Kostenstelle anzulegen. |  |  |
| 4 | Neue Kostenstelle eingeben | Geben Sie auf der Registerkarte Allgemeine Informationen die folgenden Daten ein:Kostenstelle: <Text>Name: <Text>Beschreibung: <Text>Verantwortlicher: <verantwortliche Person>Gültig ab: <01.01.2017>Gültig bis: <31.12.9999>Kostenstellenart: <Kostenstellenart>Optional können Sie die Vorschlagswerte für die Gültigkeitsdatumsangaben ändern und eine Referenz aus vorhandenen Kostenstellenstammdaten auswählen. | Ein neuer Bereich wird geöffnet, der Allgemeine Informationen anzeigt. |  |
| 5 | Kostenstellenorganisationsdaten eingeben | Nehmen Sie im Abschnitt Organisationseinheiten auf dem Bild Kostenstelle folgende Einträge vor:Standardhierarchieknoten: <1~>.Buchungskreis: <Buchungskreis>Funktionsbereich: <Funktionsbereich>Profitcenter: <Profitcenter>Nur für PSM:Hinweis Wenn Sie das Public Sector Management (PSM) installiert haben, sind diese Felder für die Eingabe verfügbar, nachdem der PSM-Buchungskreis ausgewählt wurde.Fonds: <Fonds>:Fonds fest zugeordnet: <Ja/Nein>Förderung: <Förderung>Förderung fest zugeordnet: <Ja/Nein>Funktionsbereich fest zugeordnet: <Ja/Nein>Hinweis Das Ankreuzfeld Feste Zuordnung für Funktionsbereich, Fonds und Förderung wird erst nach Eingabe der entsprechenden Stammdaten angezeigt.Budgettragende Kostenstelle: <Kostenstelle>Profil für Budgetverfügbarkeitskontrolle: <Profil>Budgetverfügbarkeitskontrolle ist aktiv: <Ja/Nein> | Die Auswahl wird durchlaufen, und die Organisationsdaten werden angezeigt. |  |
| 6 | Anlegen | Wählen Sie Anlegen. | Die Kostenstelle wird angelegt. |  |

### Kostenstellengruppen-Stammdatensatz anlegen

Testverwaltung

Kundenprojekt: Füllen Sie die projektbezogenen Teile aus.

|  |  |  |  |
| --- | --- | --- | --- |
| Testfall-ID | <X.XX> | Testdatum: |  |
| Testername: |  | Dauer: |  |
| Benutzerrolle(n): |  | Zuständigkeit: | <Geben Sie den Serviceanbieter, einen Kunden oder einen Serviceanbieter zusammen mit einem Kunden an.> |

Voraussetzung

Für dieses Kapitel müssen die Grunddaten für das Material bereits wie in Kapitel beschrieben ausgefüllt sein. [Kostenstellenstammdaten anlegen](#unique_9) [Seite ] 6. Starten Sie diesen Vorgang, nachdem Sie die Einträge für die Stammdaten im vorherigen Thema gesichert haben.

|  |
| --- |
| Hinweis Beim Anlegen alternativer Hierarchien kann entweder Globale Hierarchien verwalten(F2918) oder Kostenstellengruppen verwalten(F1024) verwendet werden, aber es sollte nur eine Methode (Globale Hierarchiegruppen oder Setbasierte Gruppen) ausgewählt werden. Beide Möglichkeiten werden in den folgenden Schritten beschrieben.Bestandskunden dürfen weiterhin die auf setbasierte Gruppen bezogene App Kostenstellengruppen verwalten(F1024) verwenden, bis sie den Migrationsstatus mithilfe der BPC-Expertenrolle über den folgenden Pfad vollständig migrieren und als abgeschlossen kennzeichnen: Geschäftsprozesskonfiguration > Buchhaltung > Allgemeine Einstellungen: Setbasierte Gruppen in globale Hierarchien migrieren (F6228)Die von SAP ausgelieferten Demo-Stammdaten für Kostenstellengruppen werden auch über setbasierte Gruppen angelegt und können auch konvertiert werden.Weitere Informationen zur Konvertierung der Kostenstellengruppe in die globale Hierarchie finden Sie unter: [https://help.sap.com/docs/SAP_S4HANA_CLOUD/c56f622a2edf491b9f1b596b55587009/635e615de9a848eb9129edb0da88cbcc.html?state=DRAFT](https://help.sap.com/docs/SAP_S4HANA_CLOUD/c56f622a2edf491b9f1b596b55587009/635e615de9a848eb9129edb0da88cbcc.html?state=DRAFT). |

Vorgehensweise: Option 1 – Globale Hierarchiegruppen

| Testschrittnummer | Bezeichnung des Testschritts | Anweisungen | Erwartetes Ergebnis | Kommentare |
| --- | --- | --- | --- | --- |
| 1 | Anmelden | Melden Sie sich am SAP Fiori Launchpad als Gemeinkostencontroller an. | Das SAP Fiori Launchpad wird angezeigt. |  |
| 2 | SAP-Fiori-App aufrufen | Öffnen Sie Globale Hierarchien verwalten(F2918). | Die App wird geöffnet. |  |
| 3 | "Anlegen" wählen | Wählen Sie im Abschnitt Hierarchieliste die Option Anlegen. | Das Bild Neue Hierarchie wird angezeigt. |  |
| 4 | Neue Kostenstellenhierarchie eingeben | Geben Sie auf dem Bild Neue Hierarchie folgende Daten ein, und wählen Sie Anlegen:Typ: Kostenstellenhierarchie:Hierarchie-ID: <beliebige ID mit bis zu 10 Zeichen>Achtung Die Gesamtlänge von Hierarchie-ID und Knoten-ID darf 14 Zeichen nicht überschreiten.Kostenrechnungskreis: A000Hierarchiebeschreibung: <beliebige Beschreibung>Gültig ab: <Aktuelles Datum> |  |  |
| 5 | Neue Kostenhierarchie bearbeiten | Wählen Sie auf dem Bild Hierarchieliste das Detailsymbol >, und wählen Sie für die neu angelegte Kostenstellenhierarchie die Option Bearbeiten.Markieren Sie die neu angelegte Kostenstellenhierarchie, wählen Sie das Symbol Mehr auf der rechten Seite des Bildes, und wählen Sie Schnellerfassung.Wählen Sie auf dem Bild Schnellerfassung die Option Kostenstelle, und geben Sie folgende Daten ein:ID: <Wählen Sie die Kostenstelle(n) aus, die Sie über die Suchfunktion hinzufügen möchten.>Wählen Sie OK, wenn Sie fertig sind, und wählen Sie Sichern.Kehren Sie zum Bild Kostenstellenhierarchie zurück, und wählen Sie Aktivieren. | Die neu angelegte Kostenstellenhierarchie ist nun aktiviert. |  |

Vorgehensweise: Option 2 – Setbasierte Gruppen

| Testschrittnummer | Bezeichnung des Testschritts | Anweisungen | Erwartetes Ergebnis | Kommentare |
| --- | --- | --- | --- | --- |
| 1 | Anmelden | Melden Sie sich am SAP Fiori Launchpad als Gemeinkostencontroller an. | Das SAP Fiori Launchpad wird angezeigt. |  |
| 2 | SAP-Fiori-App aufrufen | Öffnen Sie Kostenstellengruppen verwalten(F1024). | Die App wird geöffnet. |  |
| 3 | Neue Kostenstellengruppe anlegen | Wählen Sie im Bereich Ergebnisliste: Kostenstellengruppe die Option Neu. |  |  |
| 4 | Neue Kostenstellengruppe eingeben | Nehmen Sie im Bild Kostenstellengruppe: Neu folgende Einträge vor:Kostenrechnungskreis: <A000>Kostenstellengruppe: <Kostenstellengruppe>Wählen Sie Weiter, und nehmen Sie die folgenden Einträge vor:Name: <Name>Wählen Sie Sichern.Optional können Sie eine Referenz aus vorhandenen Kostenstellengruppen verwenden. | Das Bild Kostenstellengruppen: Neu wird angezeigt. |  |
| 5 | Kostenstellenorganisationsdaten eingeben | Nehmen Sie im Bild Kostenstellengruppen: Neu folgende Einträge vor:Auf der obersten Ebene können Sie über Neu neue Stammdaten anlegen:Neue untergeordnete Gruppe: <Kostenstellengruppe>Auf den unteren Ebenen können Sie über Neu Folgendes hinzufügen:Neue untergeordnete Gruppe: <Kostenstellengruppe>Neue gleichgeordnete Gruppe: <Kostenstellengruppe>Auf der obersten Ebene können Sie über Hinzufügen vorhandene Stammdaten hinzufügen:Untergeordnete Gruppe hinzufügen: <Kostenstellengruppe>Kostenstelle hinzufügen: <Kostenstelle>Kostenstellenbereich hinzufügen: <Kostenstelle(n)>Auf den unteren Ebenen können Sie über Neu Folgendes hinzufügen:Neue untergeordnete Gruppe: <Kostenstellengruppe>Neue gleichgeordnete Gruppe: <Kostenstellengruppe>Kostenstelle hinzufügen: <Kostenstelle>Kostenstellenbereich hinzufügen: <Kostenstelle(n)> | Die neuen Stammdaten werden im Bild Kostenstellengruppen: Neu angezeigt. |  |
| 6 | Daten sichern | Wählen Sie Sichern. | Die Kostenstellengruppe wird angelegt und gesichert. |  |

### Analysen

#### Verwendungsnachweis - Kostenstellen Ist

Testverwaltung

Kundenprojekt: Füllen Sie die projektbezogenen Teile aus.

|  |  |  |  |
| --- | --- | --- | --- |
| Testfall-ID | <X.XX> | Testdatum: |  |
| Testername: |  | Dauer: |  |
| Benutzerrolle(n): |  | Zuständigkeit: | <Geben Sie den Serviceanbieter, einen Kunden oder einen Serviceanbieter zusammen mit einem Kunden an.> |

Zweck

In dieser Aktivität können Sie sehen, wo die Kostenstellen in anderen Stammdaten, wie z.B. Aktivitätsart, Profitcenter und Istkostenverteilung verwendet werden.

Vorgehensweise

| Testschrittnummer | Bezeichnung des Testschritts | Anweisung | Erwartetes Ergebnis | Bestanden/Nicht bestanden/Anmerkung |
| --- | --- | --- | --- | --- |
| 1. | Anmelden | Melden Sie sich am SAP Fiori Launchpad als Gemeinkostencontroller an. |  |  |
| 2 | SAP-Fiori-App aufrufen | Öffnen Sie Kostenstellen verwalten - Neue Version(F1443B). | Das Bild Kostenstellen verwalten wird angezeigt. |  |
| 3 | Selektionskriterien | Geben Sie Folgendes ein, und wählen Sie Start:Kostenstelle: <Ihre Kostenstelle> |  |  |
| 4 | Verwendungsnachweis | Markieren Sie die gewünschte Kostenstelle, und wählen Sie VerwNachweis.Wählen Sie eine Option aus der Auswahlliste aus. Beispiel: In allen Objekten. | Ein Bericht wird angezeigt, dem zu entnehmen ist, wo die Kostenstellen gegenwärtig verwendet werden. Für Details können Sie den Stammdaten-Objekttyp auswählen und weitere Informationen anzeigen. |  |

|  |
| --- |
| Hinweis Die App Verwendungsnachweis - Kostenstellen(F3549) kann auch verwendet werden, um zu ermitteln, wo die Kostenstellen derzeit verwendet werden. |

## Anhang

### Kostenstellenreplikation aus SAP S/4HANA Cloud Public Edition nach SAP Master Data Integration (optional)

Der Link beschreibt die Replikation von Stammdaten von Kostenstellen in SAP S/4HANA Cloud Public Edition an andere Cloud-Apps wie SAP SuccessFactors über SAP Master Data Integration: [https://help.sap.com/viewer/6b39bd1d0e5e4099a5b65d835c29c696/LATEST/en-US/decbb94c95fa421ead9101e4c43683f7.html](https://help.sap.com/viewer/6b39bd1d0e5e4099a5b65d835c29c696/LATEST/en-US/decbb94c95fa421ead9101e4c43683f7.html).

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
- related-to :: [[06-management-accounting/create-cost-center-and-cost-center-group-mds-bnm-635]]
- related-to :: [[06-management-accounting/mds-bnm-637]]
- related-to :: [[06-management-accounting/mds-bnm-639]]
- related-to :: [[06-management-accounting/script-de-dados-mestre-criar-centro-de-custo-e-grupo-de-centros-de-cus]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/BNM_S4CLD2608_Master_Data_DE_XX.docx` — full document · extracted with `mammoth` · 20,862 chars in the whole document
