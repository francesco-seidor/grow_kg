---
id: 14-maintenance-service-and-projects/instandhaltungs-stammdaten-fur-service-anlegen-sds-3u3-370
title: Instandhaltungs-Stammdaten für Service anlegen – SDS (3U3) (3U3_S4CLD2608_Master_Data_DE_XX)
description: "German master data script (3U3) for SAP S/4HANA Cloud Public Edition: creating functional location and equipment master data for service orders, confirmations and contracts."
cluster: 14-maintenance-service-and-projects
tags: [kb/maintenance-service-and-projects, topic/service-technical-objects-and-boms]
aliases: [3U3_S4CLD2608_Master_Data_DE_XX]
keywords: [Technical Objects and BOMs for Service, functional locations, equipment master data, service master data, equipment installation, warranty, business roles, master data scripts, technical objects, 3U3]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/3U3_S4CLD2608_Master_Data_DE_XX.docx]
confidence: high
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-370
topic: 14-maintenance-service-and-projects/service-technical-objects-and-boms
language: DE
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Instandhaltungs-Stammdaten für Service anlegen – SDS (3U3) (3U3_S4CLD2608_Master_Data_DE_XX)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/3U3_S4CLD2608_Master_Data_DE_XX.docx`, extracted with `mammoth`. Grouped under **Technical Objects and BOMs for Service** in Maintenance, Service and Projects. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

| <!-- image omitted: unnamed --> | StammdatenskriptSAP S/4HANA Cloud Public Edition - 02-07-26 |
| --- | --- |
|  | Instandhaltungs-Stammdaten für Service anlegen – SDS (3U3) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Inhaltsverzeichnis

[1 Einsatzmöglichkeiten 2](#_Toc233889686)

[2 Voraussetzungen 3](#_Toc233889687)

[2.1 Systemzugriff 3](#_Toc233889688)

[2.2 Rollen 3](#_Toc233889689)

[3 Vorgehensweisen 4](#_Toc233889690)

[3.1 Anlegen von Stammdaten zum Technischen Platz 4](#_Toc233889691)

[3.2 Anlegen von Equipmentstammdaten 5](#_Toc233889692)

## Einsatzmöglichkeiten

Dieses Dokument beschreibt, wie Sie einen Stammdatensatz für den Technischen Platz und das Equipment für Ihr S/4HANA-System anlegen. Die Beschreibung umfasst die Datensegmente, die für die Stammdaten für die Arbeit in einer üblichen Systemumgebung relevant sind. Der Leser lernt hauptsächlich, welche Datensegmente und -felder hauptsächlich mit Eingabewerten gefüllt werden müssen. Felder, die für den durch von SAP Best Practices bereitgestellten Umfang der Content-Auslieferung in S/4HANA nicht relevant sind, werden in diesem Dokument nicht behandelt, obwohl sie möglicherweise in der Benutzeroberfläche angezeigt werden.

Stammdatensätze für den Technischen Platz und das Equipment, die wie hier beschrieben angelegt werden, können in Serviceaufträgen, Servicerückmeldungen und Serviceverträgen verwendet werden.

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
| Instandhaltungsplaner | SAP_BR_MAINTENANCE_PLANNER | Instandhaltungsplanung | SAP_BR_MAINTENANCE_PLANNER |

## Vorgehensweisen

### Anlegen von Stammdaten zum Technischen Platz

Einsatzmöglichkeiten

In diesem Testschritt pflegen Sie die Struktur eines Technischen Platzes mit einem Technischen Platz der obersten Ebene und zwei untergeordneten Technischen Plätzen.

Vorgehensweise

| Testschrittnummer | Bezeichnung des Testschritts | Anweisung | Erwartetes Ergebnis | Kommentare |
| --- | --- | --- | --- | --- |
| 1 | Anmelden | Melden Sie sich am SAP Fiori Launchpad als Instandhaltungsplaner an. |  |  |
| 2 | App öffnen | Wählen Sie im Abschnitt Technisches Objekt die Kachel Technisches Objekt anlegen. |  |  |
| 3 | Technischen Platz anlegen | Wählen Sie auf dem Bild Technisches Objekt anlegen die Option Art des technischen Objekts: Technischer Platz.Geben Sie auf dem nächsten Bild folgende Daten ein:Art des technischen Objekts: Technischer PlatzStrukturkennzeichen: YBPM (Strukturkennzeichen für Best Practice)Technisches Objekt: <Geben Sie einen Identifikator ein, z.B.> ZZ01Typ des technischen Objekts: S (Kundenlokation)Wählen Sie Weiter. |  |  |
| 4 | Allgemeine Daten pflegen | Geben Sie auf dem Bild Technisches Objekt anlegen: ZZ01 im Abschnitt Allgemeine Daten folgende Daten ein:Beschreibung: <z.B. Gebäude A>Optional können Sie weitere allgemeine Daten pflegen. Navigieren Sie dann zum Abschnitt Standortdaten. |  |  |
| 5 | Standortdaten pflegen | Geben Sie im Abschnitt Standortdaten folgende Daten ein:Standortwerk: <Geben Sie ein relevantes Werk ein, z.B. 1710 für die USA>Hinweis Allen technischen Objekten, die zu einer Struktur gehören, muss dasselbe Werk zugeordnet sein. Alternativ können Sie die Felder für Angaben zum Werk für alle technischen Objekte leer lassen.Optional können Sie weitere Details wie die Adresse pflegen. |  |  |
| 6 | Technischen Platz sichern | Optional können Sie im Abschnitt Organisationsdaten zusätzliche Informationen wie Partnerinformationen pflegen.Wählen Sie "Sichern".Kehren Sie dann auf die Startseite zurück. |  |  |
| 7 | Untergeordneten Technischen Platz anlegen | Um die Struktur eines Technischen Platzes zu pflegen, führen Sie die oben genannten Schritte aus und pflegen die folgenden Technischen Plätze:Technisches Objekt: ZZ01-001Beschreibung: Erster StockTechnisches Objekt: ZZ01-002Beschreibung: Zweiter Stock |  |  |
| 8 | Technisches Objekt im Asset Viewer prüfen | Wählen Sie auf der Startseite die Kachel Technisches Objekt anzeigen.Geben Sie auf dem Bild Technisches Objekt anzeigen das relevante Technische Objekt, z.B. ZZ01, ein, und wählen Sie Weiter.Um die Struktur des Technischen Platzes und die Details für jedes technische Objekt zu prüfen, können Sie auch Technisches Objekt im Asset Viewer anzeigen wählen. |  |  |

### Anlegen von Equipmentstammdaten

Zweck

In diesem Testschritt pflegen Sie einen Datensatz für ein Equipment, das auf einem Technischen Platz eingebaut ist.

Vorgehensweise

| Testschrittnummer | Bezeichnung des Testschritts | Anweisung | Erwartetes Ergebnis | Kommentare |
| --- | --- | --- | --- | --- |
| 1 | Anmelden | Melden Sie sich am SAP Fiori Launchpad als Instandhaltungsplaner an. |  |  |
| 2 | App öffnen | Öffnen Sie Technisches Objekt anlegen. |  |  |
| 3 | Equipment anlegen | Wählen Sie auf dem Bild Technisches Objekt anlegen die Option Art des technischen Objekts: Equipment.Geben Sie auf dem nächsten Bild folgende Daten ein:Technischer Objekttyp: EquipmentTechnisches Objekt: <leer>Gültig ab: <aktuelles Datum>Typ des technischen Objekts: S (Kundenequipment)Wählen Sie Weiter. |  |  |
| 4 | Allgemeine Daten pflegen | Geben Sie auf dem Bild Technisches Objekt anlegen: <Equipment-ID> im Abschnitt Allgemeine Daten folgende Daten ein:Beschreibung: <z.B. Drucker A1>(Optional) Kundengarantie: Garantiebeginn/-ende(Optional) Lieferantengarantie: Garantiebeginn/-endeHinweis Der Werkstattreparaturprozess (Umfangsbestandteil 3XK) unterstützt und integriert Garantien, die auf Terminen basieren (Garantiezeitraum). Bei der Werkstattreparatur können Sie die Garantiearten "Kundengarantie" und "Lieferantengarantie" verwenden.Sie müssen das Garantiebeginndatum und das Garantieenddatum in den Equipmentstammdaten eingeben. Wenn Sie das Enddatum für die Kunden- und/oder Lieferantengarantie eines Equipments eingegeben haben, prüft das System, ob das Garantieenddatum vor dem Anlegedatum der Werkstattreparatur liegt.Ein Symbol zeigt an, ob das Anlegedatum der Werkstattreparatur innerhalb des Garantiezeitraums liegt.Optional können Sie weitere allgemeine Daten wie Informationen zum Hersteller und die Modellnummer pflegen. Navigieren Sie dann zum Abschnitt Standortdaten. |  |  |
| 5 | Material- und Serialnummer zuordnen | Wählen Sie Zusätzliche Funktionen > Serialnummerndaten anzeigen.Geben Sie folgende Daten ein, und wählen Sie Enter:Material: TG20 |  |  |
| 6 | Standortdaten pflegen | Geben Sie im Abschnitt Standortdaten folgende Daten ein:Standortwerk: <Geben Sie ein relevantes Werk ein, z.B. 1710 für die USA.>Hinweis Allen technischen Objekten, die zu einer Struktur gehören, muss dasselbe Werk zugeordnet sein. Alternativ können Sie die Felder für Werksdaten für alle technischen Objekte leer lassen.Optional können Sie weitere Details wie die Adresse oder Informationen zum Raum pflegen. |  |  |
| 7 | Equipment sichern | Optional können Sie im Abschnitt Organisationsdaten zusätzliche Informationen wie Partnerinformationen pflegen.Wählen Sie "Sichern". |  |  |
| 8 | Equipment auf Technischem Platz einbauen | Navigieren Sie auf dem Bild Technisches Objekt ändern: <Equipment-ID> zum Abschnitt Struktur.Wählen Sie Struktur ändern: Einbauen.Geben Sie im Dialogfenster Einbauort ändern folgende Daten ein:Übergeordnetes technisches Objekt: ZZ01-001Position: <leer lassen>Einbaudatum/-zeit: <Systemvorschlag beibehalten>Wählen Sie OK.Wählen Sie Sichern. |  |  |

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
- related-to :: [[14-maintenance-service-and-projects/master-data-script-create-plant-maintenance-master-data-for-service-md]]
- related-to :: [[14-maintenance-service-and-projects/mds-3u3-373]]
- related-to :: [[14-maintenance-service-and-projects/mds-3u3-375]]
- related-to :: [[14-maintenance-service-and-projects/script-de-dados-mestre-criar-dados-mestre-de-manutencao-de-centro-para]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/3U3_S4CLD2608_Master_Data_DE_XX.docx` — full document · extracted with `mammoth` · 11,018 chars in the whole document
