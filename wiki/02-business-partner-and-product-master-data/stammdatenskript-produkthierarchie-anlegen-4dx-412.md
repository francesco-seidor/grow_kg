---
id: 02-business-partner-and-product-master-data/stammdatenskript-produkthierarchie-anlegen-4dx-412
title: "Stammdatenskript: Produkthierarchie anlegen (4DX) (4DX_S4CLD2608_Master_Data_DE_XX)"
description: "German master data script (4DX) for SAP S/4HANA Cloud Public Edition 2608: configure hierarchy nodes and create/activate a product hierarchy with Manage Product Hierarchies (F4359)."
cluster: 02-business-partner-and-product-master-data
tags: [kb/business-partner-and-product-master-data, topic/product-hierarchy]
aliases: [4DX_S4CLD2608_Master_Data_DE_XX]
keywords: [Product Hierarchies, product hierarchy, product hierarchy nodes, master data scripts, product master data, business roles, organizational units, central business configuration, sales orders, 4DX]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/4DX_S4CLD2608_Master_Data_DE_XX.docx]
confidence: high
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-412
topic: 02-business-partner-and-product-master-data/product-hierarchy
language: DE
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Stammdatenskript: Produkthierarchie anlegen (4DX) (4DX_S4CLD2608_Master_Data_DE_XX)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/4DX_S4CLD2608_Master_Data_DE_XX.docx`, extracted with `mammoth`. Grouped under **Product Hierarchies** in Business Partner and Product Master Data. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

| <!-- image omitted: unnamed --> | StammdatenskriptSAP S/4HANA Cloud Public Edition - 02-07-26 |
| --- | --- |
|  | Produkthierarchie anlegen (4DX) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Inhaltsverzeichnis

[1 Zweck 2](#_Toc233889719)

[2 Voraussetzungen 3](#_Toc233889720)

[2.1 Systemzugriff 3](#_Toc233889721)

[2.2 Rollen 3](#_Toc233889722)

[2.3 Erforderliche Organisationseinheiten 3](#_Toc233889723)

[2.4 Obligatorische und optionale Stammdaten 4](#_Toc233889724)

[2.5 Wesentliche Parameter für die Datenerstellung 4](#_Toc233889725)

[2.5.1 Produkthierarchieknoten 4](#_Toc233889726)

[2.6 Vorbereitende Schritte 5](#_Toc233889727)

[2.6.1 Knoten für Produkthierarchien anlegen 5](#_Toc233889728)

[3 Übersichtstabelle 8](#_Toc233889729)

[4 Testverfahren 9](#_Toc233889730)

[4.1 Produkthierarchie anlegen 9](#_Toc233889731)

## Zweck

Dieses Dokument beschreibt, wie Sie Produkthierarchie-Stammdaten für Ihr SAP S/4HANA Cloud Public Edition-System anlegen. Die Beschreibung umfasst die Datensegmente, die für die Stammdaten für die Arbeit in einer üblichen Systemumgebung relevant sind. Der Leser lernt hauptsächlich, welche Datensegmente und -felder hauptsächlich mit Eingabewerten gefüllt werden müssen. Felder, die für den Umfang in SAP S/4HANA Cloud Public Edition nicht relevant sind, werden in diesem Dokument nicht behandelt, obwohl sie möglicherweise auf dem Bild angezeigt werden.

Über die angelegten Produkthierarchie-Stammdaten können Vertriebslinien einer Produkthierarchie zugeordnet werden, die wiederum in Kundenaufträgen für die weitere Verarbeitung verwendet wird.

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
| Konfigurationsexperte – Geschäftsprozesskonfiguration | SAP_BR_BPC_EXPERT | Geschäftsprozesskonfiguration / Geschäftsprozesskonfiguration - Finance / Geschäftsprozesskonfiguration - Beschaffung / Lösung verwalten / Geschäftsprozesskonfiguration - Workflow / Geschäftskonfiguration - Feature Management / Geschäftsprozesskonfiguration - Extensibility Explorer / Business Configuration - Transportation Management | SAP_BR_BPC_EXPERT / SAP_FIN_SPT_BPC_EXPERT_PC / SAP_MM_SPT_BIZ_PROC_CONFIGN_PC / SAP_CA_SPT_IC_LND_BASE_PC / SAP_CA_SPT_BPC_WORKFLOW_PC / SAP_CA_SPT_BPC_FM_PC / SAP_EI_SPT_BPC_EXT_PC / SAP_TM_SPT_TRANSPCFG_PC |  |
| Stammdatenexperte – Produktdaten | SAP_BR_PRODMASTER_SPECIALIST | Stammdaten – Produkte / Produkt-Governance | SAP_BR_PRODMASTER_SPECIALIST / SAP_CMD_SPT_PR_GOV_PC |  |

### Erforderliche Organisationseinheiten

Einige Segmente der Stammdaten hängen von den Organisationseinheiten des Unternehmens ab. Allgemeine (zentrale) Daten sind nicht von einer Organisationseinheit oder dem Buchungskreis abhängig. Die folgende Tabelle stellt eine Übersicht dieser verschiedenen Datensegmente und ihrer relevanten Organisationseinheiten bereit:

| Datensegment | Hängt ab von | Feldbeispiele | Kommentare | Zu verwendende Organisationseinheit |
| --- | --- | --- | --- | --- |
| Verkaufsdaten | Werk, Verkaufsorganisation, Vertriebsweg | Steuerdaten, Positionstypengruppe, Ladegruppe usw. |  | Werk:____________Verkaufsorganisation:____________Vertriebsweg:______________ |

### Obligatorische und optionale Stammdaten

Stammdatensätze können auf andere Stammdaten verweisen. Die folgende Tabelle bietet eine Übersicht über die optionalen und obligatorischen Stammdatenobjekte, die in einem Produkthierarchie-Stammdatensatz verwendet werden müssen.

| Stammdatenobjekt | Verwendet im Datensegment | Obligatorisch / optional | Kommentare |
| --- | --- | --- | --- |
| Product | In der App Produkthierarchien verwalten wird eine Hierarchie mit mehreren Produkten als Blatt- oder Endknoten zugeordnet. | Obligatorisch | Indem Sie die in der App Produktstammdaten verwalten angelegten Produktdatensätze in der App Produkthierarchien verwalten als Blattknoten zuordnen, verleihen Sie der Hierarchie Vollständigkeit und betriebswirtschaftliche Bedeutung. |

### Wesentliche Parameter für die Datenerstellung

In diesem Abschnitt werden einige Basisparameter erläutert, die das Verhalten eines Stammsatzes beeinflussen und zum Anlegen eines Produkthierarchie-Stammdatensatzes immer erforderlich sind.

#### Produkthierarchieknoten

Zum Auswählen oder Erstellen der Hierarchiestruktur muss die für "Product" verfügbare Self-Service-Konfigurations-UI (Konfigurationsschritt) Knoten für Produkthierarchien konfigurieren, auf die Sie durch Filtern nach dem Anwendungsbereich "Database and Data Management" zugreifen können, gepflegt werden.

Diese Konfiguration bietet die Option zum Anlegen mehrerer Knotenwerte sowie einer Beschreibung für jeden Knoten.

|  |
| --- |
| Hinweis Abhängig von Ihrer Konfigurationsumgebung können Sie auf die Konfigurationsschritte unter Lösung konfigurieren im SAP Fiori Launchpad oder in der App Business Processes Configuration in der Projekterfahrung von SAP Central Business Configuration zugreifen. |

### Vorbereitende Schritte

#### Knoten für Produkthierarchien anlegen

Testverwaltung

Kundenprojekt: Füllen Sie die projektbezogenen Teile aus.

|  |  |  |  |
| --- | --- | --- | --- |
| Testfall-ID | <X.XX> | Testdatum: |  |
| Testername: |  | Dauer: |  |
| Benutzerrolle(n): |  | Zuständigkeit: | <Geben Sie den Serviceanbieter, einen Kunden oder einen Serviceanbieter zusammen mit einem Kunden an.> |

Zweck

Zum Anlegen von Produkthierarchien sind die Einträge aus dem Self-Service-Konfigurationsschritt Konten für Produkthierarchien konfigurieren erforderlich.

|  |
| --- |
| Hinweis Dieser Schritt muss von dem Konfigurationsexperte-Benutzer in einem herkömmlichen Geschäftsszenario ausgeführt werden. |

Vorgehensweise

|  |
| --- |
| Hinweis Abhängig von Ihrer Konfigurationsumgebung können Sie auf die Konfigurationsschritte unter Lösung konfigurieren im SAP Fiori Launchpad oder in der App Business Processes Configuration in der Projekterfahrung von SAP Central Business Configuration zugreifen. |

Lösung konfigurieren:

| Testschrittnummer | Bezeichnung des Testschritts | Anweisung | Erwartetes Ergebnis | Kommentare |
| --- | --- | --- | --- | --- |
| 1 | Anmelden | Melden Sie sich am SAP Fiori Launchpad mit Ihren Benutzeranmeldeinformationen an. | Die Startseite wird angezeigt. |  |
| 2 | SAP-Fiori-App öffnen | Wählen Sie im Implementierungs-Cockpit die App Lösung verwalten(F1241). | Eine neue Seite wird geöffnet, die das Bild Lösung verwalten(F1241) anzeigt.Hinweis Diese Anwendung ist Teil der Rolle Konfigurationsexperte – Geschäftsprozesskonfiguration. |  |
| 3 | "Lösung konfigurieren" wählen | Wählen Sie in der App Lösung verwalten die Option Lösung konfigurieren. | Eine neue Seite mit dem Bild Lösung konfigurieren: Änderungsphase wird geöffnet. |  |
| 4 | Anwendungsbereich auswählen | Wählen Sie in der App Lösung konfigurieren den Filter für den Anwendungsbereich aus, und markieren Sie die Option Database and Data Management. | Die Anzahl der angezeigten Einträge in der Ergebnistabelle wird auf wenige Datensätze reduziert. |  |
| 5 | Subanwendungsbereich auswählen | Wählen Sie in der App Lösung konfigurieren den Filter für den Subanwendungsbereich aus, und markieren Sie die Option Product. | Die Anzahl der angezeigten Datensätze in der Ergebnistabelle wird auf einen reduziert. |  |
| 6 | Produktkonfigurationsschritte | Wählen Sie in der Tabelle den Datensatz mit Produkt als Subanwendungsbereich aus.Wählen Sie anschließend den Abschnitt mit dem Titel Konfigurationsschritte. | Im Abschnitt wird eine Liste verschiedener Produktkonfigurationsschritte angezeigt. |  |
| 7 | Knoten für Produkthierarchie konfigurieren | Wählen Sie im Konfigurationsschritt Knoten für Produkthierarchien konfigurieren die Drucktaste Konfigurieren. | Die Anwendungsseite Produkthierarchie: Unterknoten - ID-Pflege wird geöffnet. |  |
| 8 | Neue Einträge anlegen | Wählen Sie Neue Einträge: | Eine bearbeitbare Seite für die Pflege von neuen Unterknoten mit dem Titel Neue Einträge: . Übersicht Hinzugefügte wird geöffnet |  |
| 9 | Neue Unterknoten eingeben | Geben Sie für die gewünschten Unterknoten in der Zielprodukthierarchie mehrere Einträge ein.Beispielsweise kann die Hierarchie <Getränke> wie folgt aussehen:Die Produkthierarchieknoten könnten <GETRÄNKE_MIT_KOHLENSÄURE>, <GETRÄNKE_OHNE_KOHLENSÄURE> usw. lautenDie Beschreibung der Unterknoten könnte <Getränke mit Kohlensäure>, <Getränke ohne Kohlensäure> usw. lauten. |  |  |
| 10 | Eingaben sichern | Wählen Sie unten auf der Seite Sichern. | Die Anwendungsseite Produkthierarchie: Unterknoten - ID-Pflege wird mit den neuen Einträgen angezeigt. |  |
| 11 | Beenden | Wählen Sie Beenden, und melden Sie sich ab. |  |  |

SAP Central Business Configuration:

| Testschrittnummer | Bezeichnung des Testschritts | Anweisung | Erwartetes Ergebnis | Kommentare |
| --- | --- | --- | --- | --- |
| 1 | Anmelden | Melden Sie sich an der Projekterfahrung in SAP Central Business Configuration an. |  |  |
| 2 | "Flexiblen Workflow aktivieren" öffnen | Wechseln Sie zur App Business Processes Configuration. Um die Aktivität in der Baumsicht zu finden, suchen Sie nach der folgenden Aktivität: Configure Nodes for Product Hierarchies.Wählen Sie Open Documentation für die gefundene Position, um weitere Details zu dieser Konfigurationsaktivität anzuzeigen.Wählen Sie den Link, um direkt zum SAP S/4HANA Cloud Public Edition-System zu navigieren. Melden Sie sich am SAP Fiori Launchpad als Konfigurationsexperte – Geschäftsprozesskonfiguration an. |  |  |
| 3 | Neue Einträge anlegen | Wählen Sie Neue Einträge: | Eine bearbeitbare Seite für die Pflege von neuen Unterknoten mit dem Titel Neue Einträge: . Übersicht Hinzugefügte wird geöffnet |  |
| 4 | Neue Unterknoten eingeben | Geben Sie für die gewünschten Unterknoten in der Zielprodukthierarchie mehrere Einträge ein.Beispielsweise kann die Hierarchie <Getränke> wie folgt aussehen:Die Produkthierarchieknoten könnten <GETRÄNKE_MIT_KOHLENSÄURE>, <GETRÄNKE_OHNE_KOHLENSÄURE> usw. lautenDie Beschreibung der Unterknoten könnte <Getränke mit Kohlensäure>, <Getränke ohne Kohlensäure> usw. lauten. |  |  |
| 5 | Eingaben sichern | Wählen Sie unten auf der Seite Sichern. | Die Anwendungsseite Produkthierarchie: Unterknoten - ID-Pflege wird mit den neuen Einträgen angezeigt. |  |
| 6 | Beenden | Wählen Sie Beenden, und melden Sie sich ab. |  |  |

## Übersichtstabelle

Dieser Stammdatensatz umfasst mehrere Segmente, die in der nachfolgenden Tabelle genannt sind.

|  |
| --- |
| Hinweis Wenn Ihr Systemadministrator Bereiche und Seiten auf dem SAP Fiori Launchpad aktiviert hat, enthält die Startseite nur die wesentlichen Apps, mit denen die typischen Aufgaben einer Benutzerrolle ausgeführt werden können.Alle anderen (suchbaren) Apps, die nicht auf der Startseite enthalten sind, finden Sie über die Suchleiste ([2434549](https://me.sap.com/notes/2434549)).Wenn Sie die Startseite personalisieren und versteckte Apps hinzufügen möchten, wechseln Sie in Ihr Benutzerprofil und wählen Sie App Finder. |

| Segment | Anwendungsrolle | App/Vorgang | Erwartete Ergebnisse |
| --- | --- | --- | --- |
| [Produkthierarchie anlegen](#unique_11) [Seite ] 9 | Stammdatenexperte – Produktdaten | Produkthierarchien verwalten(F4359) | Der Produkthierarchie-Stammdatensatz wird angelegt. |

## Testverfahren

In diesem Abschnitt werden die Testverfahren für den jeweiligen Prozessschritt beschrieben, der zum betreffenden Umfangsbestandteil gehört.

### Produkthierarchie anlegen

Testverwaltung

Kundenprojekt: Füllen Sie die projektbezogenen Teile aus.

|  |  |  |  |
| --- | --- | --- | --- |
| Testfall-ID | <X.XX> | Testdatum: |  |
| Testername: |  | Dauer: |  |
| Benutzerrolle(n): |  | Zuständigkeit: | <Geben Sie den Serviceanbieter, einen Kunden oder einen Serviceanbieter zusammen mit einem Kunden an.> |

Zweck

Die folgende Vorgehensweise enthält Anweisungen zum Anlegen einer Produkthierarchie mit Produkten, die der Hierarchie als Endknoten zugeordnet sind. Nach der Aktivierung der Hierarchie kann diese bei der Erstellung von Kundenaufträgen verwendet werden.

Vorgehensweise

| Testschrittnummer | Bezeichnung des Testschritts | Anweisungen | Erwartetes Ergebnis | Kommentare |
| --- | --- | --- | --- | --- |
| 1 | Anmelden | Melden Sie sich am SAP Fiori Launchpad mit Ihren Benutzeranmeldeinformationen an. | Das SAP Fiori Launchpad wird angezeigt. |  |
| 2 | SAP-Fiori-App aufrufen | Öffnen Sie Produkthierarchien verwalten(F4359). | Die App wird geöffnet. |  |
| 3 | Produkthierarchie anlegen | Wählen Sie auf dem Bild Produkthierarchien verwalten das Symbol + (Neue Hierarchie anlegen). | Das Bild Neue Hierarchie anlegen wird angezeigt. |  |
| 4 | Produkthierarchiedaten eingeben | Geben Sie auf dem Bild Neue Hierarchie anlegen folgende Daten ein:Art: z.B. <Produkthierarchie>Hierarchie-ID: z.B. <GETRÄNKE>Hierarchiebeschreibung: z.B. <Getränkehierarchie>Gültig ab: <Geben Sie ein Datum für den Start des Gültigkeitszeitraums der Hierarchie ein.>Gültig bis: <Ändern Sie das vorgeschlagene Datum, wenn Sie eine zeitabhängige Hierarchie benötigen.> |  |  |
| 5 | "Anlegen" wählen | Wählen Sie auf dem Bild Neue Hierarchie anlegen die Option Anlegen. | Die Hierarchieliste wird gefiltert, um den neu angelegten Produkthierarchieeintrag mit dem Status Entwurfanzuzeigen. |  |
| 6 | Neue Produkthierarchie auswählen | Wählen Sie in der App Produkthierarchien verwalten(F4359) die neu angelegte Produkthierarchie mit dem im Ergebnis aufgeführten Status Entwurf aus. | Die Struktur der Produkthierarchie wird in einem Baumtabellenformat angezeigt. |  |
| 7 | Produkthierarchie bearbeiten | Wählen Sie in der Fußzeile des Bildes die Option Bearbeiten. | Das Bild wird im Bearbeitungsmodus angezeigt. So können Sie Werte ändern oder neue Knoten hinzufügen. |  |
| 8 | Knoten zum Wurzelknoten hinzufügen | Wählen Sie für den ersten Knoten + (Hinzufügen). | Das Bild Knoten hinzufügen wird angezeigt. |  |
| 9 | Unterknoten des Wurzelknotens auswählen | Auf dem Bild Knoten hinzufügen ist standardmäßig der Unterknoten ausgewählt.Geben Sie Daten für das Feld Knoten ein. Die im vorbereitenden Schritt [Knoten für Produkthierarchien anlegen](#unique_9) [Seite ] 5 konfigurierten Werte können hier verwendet werden.Beispiel: <GETRÄNKE_MIT_KOHLENSÄURE>, <GETRÄNKE_OHNE_KOHLENSÄURE> usw.Hinweis Mithilfe der Wertehilfe können Sie mehrere Knoten auswählen und diese dem ausgewählten Hierarchieknoten zuordnen.Wählen Sie OK. | Die ausgewählten Knoten werden in der Baumtabellenstruktur dem Wurzelknoten der Produkthierarchie als untergeordnete Knoten hinzugefügt. |  |
| 10 | Knoten zu Unterknoten hinzufügen | Wählen Sie für den Knoten + (Hinzufügen), um weitere Unterknoten hinzuzufügen.Wählen Sie beispielsweise + (Hinzufügen) für den Knoten <GETRÄNKE_OHNE_KOHLENSÄURE>. | Das Bild Knoten hinzufügen wird angezeigt. |  |
| 11 | Knoten als Unterknoten auswählen | Wählen Sie auf dem Bild Knoten hinzufügen weitere Knoten aus der Wertehilfe aus, um diese beispielsweise dem Knoten <GETRÄNKE_OHNE_KOHLENSÄURE> als Unterknoten hinzuzufügen.Wählen Sie OK. | Die ausgewählten Knoten werden in der Baumtabellenstruktur dem ausgewählten Knoten der Produkthierarchie als untergeordnete Knoten hinzugefügt. |  |
| 12 | Produkte der Hierarchie hinzufügen | Wählen Sie für den jeweiligen Knoten + (Hinzufügen), um der Hierarchie Produkte hinzuzufügen. | Das Bild Knoten hinzufügen wird angezeigt. |  |
| 13 | Produkt wählen | Wählen Sie auf dem Bild Knoten hinzufügen die Option Produkt. | Geben Sie auf dem Bild Knoten hinzufügen Ihre Änderungen für das Feld Produkt ein. |  |
| 14 | Produkte zu Hierarchie zuordnen | Wählen Sie auf dem Bild Knoten hinzufügen die entsprechenden Einträge im Feld Produkt aus, um die erforderlichen Produkte dem Hierarchieknoten zuzuordnen.Hinweis Mithilfe der Wertehilfe können Sie mehrere Produkte auswählen und diese dem ausgewählten Unterknoten der Hierarchie zuordnen. | Die ausgewählten Produkte werden dem erforderlichen Unterknoten der Produkthierarchie zugeordnet. |  |
| 15 | Produkthierarchie sichern | Wählen Sie Sichern. | Die Änderungen werden gesichert. |  |
| 16 | Produkthierarchie aktivieren | Wählen Sie Aktivieren. | Die Produkthierarchie wird aktiviert, und der Status wird von Entwurf in Aktiv geändert. |  |

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
- related-to :: [[02-business-partner-and-product-master-data/4dx-415]]
- related-to :: [[02-business-partner-and-product-master-data/4dx-417]]
- related-to :: [[02-business-partner-and-product-master-data/master-data-script-create-product-hierarchy-4dx-413]]
- related-to :: [[02-business-partner-and-product-master-data/script-de-dados-mestre-criar-hierarquia-de-produtos-4dx-416]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/4DX_S4CLD2608_Master_Data_DE_XX.docx` — full document · extracted with `mammoth` · 20,049 chars in the whole document
