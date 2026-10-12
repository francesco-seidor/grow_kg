---
id: 08-sales-order-management/lokationsersetzung-und-ausschluss-anlegen-sds-5ng-472
title: Lokationsersetzung und -ausschluss anlegen – SDS (5NG) (5NG_S4CLD2608_Master_Data_DE_XX)
description: "German master data script (5NG) for SAP S/4HANA Cloud Public Edition 2608: creating plant and storage location substitutions and exclusions via Fiori apps F5311-F5315."
cluster: 08-sales-order-management
tags: [kb/sales-order-management, topic/product-and-location-substitution]
aliases: [5NG_S4CLD2608_Master_Data_DE_XX]
keywords: ["Product, Plant and Storage Location Substitution", plant substitution, plant exclusion, storage location substitution, storage location exclusion, substitution reasons, substitution groups, substitution controls, order fulfillment, organizational units]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/5NG_S4CLD2608_Master_Data_DE_XX.docx]
confidence: high
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-472
topic: 08-sales-order-management/product-and-location-substitution
language: DE
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Lokationsersetzung und -ausschluss anlegen – SDS (5NG) (5NG_S4CLD2608_Master_Data_DE_XX)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/5NG_S4CLD2608_Master_Data_DE_XX.docx`, extracted with `mammoth`. Grouped under **Product, Plant and Storage Location Substitution** in Sales Order Management. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

| <!-- image omitted: unnamed --> | StammdatenskriptSAP S/4HANA Cloud Public Edition - 02-07-26 |
| --- | --- |
|  | Lokationsersetzung und -ausschluss anlegen – SDS (5NG) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Inhaltsverzeichnis

[1 Zweck 2](#_Toc233889822)

[2 Voraussetzungen 3](#_Toc233889823)

[2.1 Systemzugriff 3](#_Toc233889824)

[2.2 Rollen 3](#_Toc233889825)

[2.3 Erforderliche Organisationseinheiten 3](#_Toc233889826)

[2.4 Obligatorische Stammdaten 4](#_Toc233889827)

[2.5 Vorbereitende Schritte für Werksersetzung 4](#_Toc233889828)

[2.5.1 Grund für Werksersetzung anlegen (optional) 4](#_Toc233889829)

[2.5.2 Gruppe für Werksersetzung anlegen (optional) 5](#_Toc233889830)

[2.5.3 Steuerung für Werksersetzung anlegen (optional) 7](#_Toc233889831)

[2.6 Vorbereitende Schritte für die Lagerortersetzung 8](#_Toc233889832)

[2.6.1 Grund für Lagerortersetzung anlegen (optional) 8](#_Toc233889833)

[2.6.2 Gruppe für Lagerortersetzung anlegen (optional) 10](#_Toc233889834)

[2.6.3 Steuerung für Lagerortersetzung anlegen (optional) 11](#_Toc233889835)

[3 Übersichtstabelle 13](#_Toc233889836)

[4 Testverfahren 14](#_Toc233889837)

[4.1 Werksersetzung 14](#_Toc233889838)

[4.1.1 Werksersetzung anlegen 14](#_Toc233889839)

[4.1.2 Werksausschluss anlegen 15](#_Toc233889840)

[4.2 Lagerortersetzung 17](#_Toc233889841)

[4.2.1 Lagerortersetzung anlegen 17](#_Toc233889842)

[4.2.2 Lagerortausschluss anlegen 18](#_Toc233889843)

## Zweck

In diesem Dokument erfahren Sie, wie Sie Stammdaten für Lokationsersetzungen und -ausschlüsse für Ihr SAP S/4HANA Cloud Public Edition-System anlegen.

Die Lokationstypen Werk und Lagerort werden für Ersetzung und Ausschluss unterstützt.

Die Werksersetzung ist eine Technik, bei der ein Werk durch ein anderes Werk ersetzt wird. Eine Werksersetzung kann aus verschiedenen Gründen angelegt werden. Beispiel:

- Quellwerk befindet sich in der Instandhaltung
- Quellwerk befindet sich in einer kontaminierten Zone
- Produktbestand ist im Quellwerk nicht verfügbar

Ein Werksausschluss ermöglicht es Kunden, ein Produkt von der Ersetzung auszuschließen. Beispielsweise kann ein Werksausschluss für ein Werk angelegt werden, das vorübergehend stillgelegt wird.

Die Lagerortersetzung ist eine Technik, mit der ein Lagerort durch einen anderen Lagerort innerhalb desselben Werks ersetzt wird. Eine Lagerortersetzung kann aus verschiedenen Gründen angelegt werden. Beispiel:

- Der Quelllagerort ist nicht verfügbar.
- Der Produktbestand ist am Quelllagerort im Werk nicht verfügbar.

Der Lagerortausschluss ermöglicht es Kunden, einen Lagerort vom Ersatz auszuschließen.

## Voraussetzungen

In diesem Abschnitt sind alle Voraussetzungen für den Test hinsichtlich System, Benutzer, Stammdaten, Organisationsdaten, sonstige Testdaten und Voraussetzungen zusammengefasst.

### Systemzugriff

| System | Details |
| --- | --- |
| System | Zugriff möglich über SAP Fiori Launchpad. Ihr Systemadministrator stellt Ihnen die URL für den Zugriff auf die verschiedenen Apps zur Verfügung, die Ihrer Rolle zugeordnet sind. |

### Rollen

| Name (Rollenvorlage) | ID (Rollenvorlage) | Name (Launchpad-Bereich) | ID (Launchpad-Bereich) | Anmelden |
| --- | --- | --- | --- | --- |
| Experte für die Auftragserfüllung | SAP_BR_ORDER_FULFILLMNT_MNGR | Auftragserfüllungsverwaltung | SAP_BR_ORDER_FULFILLMNT_MNGR |  |

### Erforderliche Organisationseinheiten

Die Organisationsstruktur gibt den Aufbau Ihres Unternehmens wieder.

Werksersetzungen können von den Organisationseinheiten (Verkaufsorganisation und Vertriebsweg) des Unternehmens abhängig sein. Sie können auch unabhängig von der Organisationseinheit sein.

Die Lagerortersetzung ist von der Organisationseinheiten (Werk) des Unternehmens abhängig. Sie ist immer abhängig von der Organisationseinheit.

Die folgende Tabelle bietet eine Übersicht über die relevanten Organisationseinheiten.

| Datensegment | Hängt ab von | Feldbeispiele | Kommentare | Zu verwendende Organisationseinheit |
| --- | --- | --- | --- | --- |
| Werksersetzung und Werksausschluss | Verkaufsorganisation |  | Verkaufsorganisation ist in Werksersetzung/-ausschluss nicht obligatorisch. Werksersetzung/-ausschluss kann ohne Verkaufsorganisationseinschränkung erfolgen. | Verkaufsorganisation:____________ |
| Werksersetzung und Werksausschluss | Vertriebsweg |  | Vertriebsweg ist in Werksersetzung/-ausschluss nicht obligatorisch. Werksersetzung/-ausschluss kann ohne Vertriebswegeinschränkung erfolgen. | Vertriebsweg:____________ |
| Lagerortersetzung und Lagerortausschluss | Werk |  | Werk ist in Lagerortersetzung/-ausschluss obligatorisch. Lagerortersetzung/-ausschluss kann nicht ohne Werk erfolgen. | Werk: 1010 |

### Obligatorische Stammdaten

| Stammdatenobjekt | Verwendet im Datensegment | Obligatorisch / optional | Kommentare |
| --- | --- | --- | --- |
| NA | NA | NA | NA |

### Vorbereitende Schritte für Werksersetzung

#### Grund für Werksersetzung anlegen (optional)

Testverwaltung

Kundenprojekt: Füllen Sie die projektbezogenen Teile aus.

|  |  |  |  |
| --- | --- | --- | --- |
| Testfall-ID | <X.XX> | Testdatum: |  |
| Testername: |  | Dauer: |  |
| Benutzerrolle(n): |  | Zuständigkeit: | <Geben Sie den Serviceanbieter, einen Kunden oder einen Serviceanbieter zusammen mit einem Kunden an.> |

Zweck

Die folgende Vorgehensweise stellt Anweisungen zum Anlegen von Gründen für die Ersetzung oder den Ausschluss von Werken bereit. Verfügbare Apps sind von Ihrer Rolle abhängig.

Vorgehensweise

| Testschrittnummer | Bezeichnung des Testschritts | Anweisung | Erwartetes Ergebnis | Kommentare |
| --- | --- | --- | --- | --- |
| 1 | Anmelden | Melden Sie sich als Experte für die Auftragserfüllung am SAP Fiori Launchpad an. | Das SAP Fiori Launchpad wird angezeigt. |  |
| 2 | SAP-Fiori-App aufrufen | Öffnen Sie Ersetzungsgründe verwalten - Lokationen(F5313). | Das Bild Ersetzungsgründe verwalten - Lokationen wird angezeigt. |  |
| 3 | "Anlegen" wählen | Wählen Sie auf dem Bild Ersetzungsgründe verwalten - Lokationen die Drucktaste Anlegen. | Das Bild Ersetzungsgründe verwalten - Lokationen - Anlegen wird angezeigt. |  |
| 4 | Grund eingeben | Geben Sie im Bereich Kopf folgende Daten ein:Lokationsart: <Werk>Grund: <Geben Sie den neuen Ursachencode für die Ersetzung ein, z.B. NEW_PLANT.> |  |  |
| 5 | Daten anlegen | Wählen Sie Anlegen. | Die Systemmeldung Grund wird angelegt wird angezeigt. |  |
| 6 | "Anlegen" wählen | Wählen Sie im Abschnitt Beschreibung die Option Anlegen. | Das Bild Beschreibung Grund Anlegen wird angezeigt. |  |
| 7 | Beschreibungsdaten eingeben | Nehmen Sie im Abschnitt Beschreibung die folgenden Einträge vor:Sprachenschlüssel: <Geben Sie die für den Grund gültige Sprache ein, z.B. DE Deutsch.>Grundbeschreibung: <Geben Sie einen Text ein, um den Grund zu beschreiben, z.B. Neues Werk ist verfügbar> |  |  |
| 8 | Daten anlegen | Wählen Sie Anlegen. | Die Systemmeldung Beschreibung angelegt wird angezeigt. |  |

#### Gruppe für Werksersetzung anlegen (optional)

Testverwaltung

Kundenprojekt: Füllen Sie die projektbezogenen Teile aus.

|  |  |  |  |
| --- | --- | --- | --- |
| Testfall-ID | <X.XX> | Testdatum: |  |
| Testername: |  | Dauer: |  |
| Benutzerrolle(n): |  | Zuständigkeit: | <Geben Sie den Serviceanbieter, einen Kunden oder einen Serviceanbieter zusammen mit einem Kunden an.> |

Zweck

Die folgende Vorgehensweise stellt Anweisungen zum Anlegen von Gruppen für die Ersetzung oder den Ausschluss von Werken bereit. Verfügbare Apps sind von Ihrer Rolle abhängig.

Vorgehensweise

| Testschrittnummer | Bezeichnung des Testschritts | Anweisung | Erwartetes Ergebnis | Kommentare |
| --- | --- | --- | --- | --- |
| 1 | Anmelden | Melden Sie sich als Experte für die Auftragserfüllung am SAP Fiori Launchpad an. | Das SAP Fiori Launchpad wird angezeigt. |  |
| 2 | SAP-Fiori-App aufrufen | Öffnen Sie Ersetzungsgruppen verwalten - Lokationen(F5311). | Das Bild Ersetzungsgruppen verwalten - Lokationen wird angezeigt. |  |
| 3 | "Anlegen" wählen | Wählen Sie auf dem Bild Ersetzungsgruppen verwalten - Lokationen die Option Anlegen. | Das Bild Ersetzungsgruppen verwalten - Lokationen - Anlegen wird angezeigt. |  |
| 4 | Gruppe eingeben | Geben Sie im Bereich Kopf folgende Daten ein:Lokationsart: <Werk>Gruppe: <Geben Sie die neue Gruppe für die Ersetzung ein, z.B. SOUTH_REGION> |  |  |
| 5 | Daten anlegen | Wählen Sie Anlegen. | Die Systemmeldung Gruppe angelegt wird angezeigt. |  |
| 6 | "Anlegen" wählen | Wählen Sie im Abschnitt Beschreibung die Option Anlegen. | Das Bild Beschreibung Gruppe - Anlegen wird angezeigt. |  |
| 7 | Beschreibungsdaten eingeben | Nehmen Sie im Abschnitt Beschreibung die folgenden Einträge vor:Sprachenschlüssel: <Geben Sie die für die Gruppe geltende Sprache ein, z.B. DE Deutsch.>Beschreibung Gruppe: <Geben Sie einen Text ein, um die Gruppe zu beschreiben, z.B. Werke in der Region Süden verfügbar> |  |  |
| 8 | Daten anlegen | Wählen Sie Anlegen. | Die Systemmeldung Gruppenbeschreibung angelegt wird angezeigt. |  |
| 9 | "Zurück" wählen | Wählen Sie im Abschnitt Titel die Option < (Zurück). | Das Bild Ersetzungsgruppen verwalten - Lokationen wird angezeigt. |  |
| 10 | Gruppendaten aktivieren | Wählen Sie Aktiv setzen. | Die Systemmeldung Status geändert wird angezeigt. |  |

#### Steuerung für Werksersetzung anlegen (optional)

Testverwaltung

Kundenprojekt: Füllen Sie die projektbezogenen Teile aus.

|  |  |  |  |
| --- | --- | --- | --- |
| Testfall-ID | <X.XX> | Testdatum: |  |
| Testername: |  | Dauer: |  |
| Benutzerrolle(n): |  | Zuständigkeit: | <Geben Sie den Serviceanbieter, einen Kunden oder einen Serviceanbieter zusammen mit einem Kunden an.> |

Zweck

Die folgende Vorgehensweise stellt Anweisungen zum Anlegen einer Steuerung für die Ersetzung oder den Ausschluss von Produkten bereit. Verfügbare Apps sind von Ihrer Rolle abhängig.

Vorgehensweise

| Testschrittnummer | Bezeichnung des Testschritts | Anweisung | Erwartetes Ergebnis | Kommentare |
| --- | --- | --- | --- | --- |
| 1 | Anmelden | Melden Sie sich als Experte für die Auftragserfüllung am SAP Fiori Launchpad an. | Das SAP Fiori Launchpad wird angezeigt. |  |
| 2 | SAP-Fiori-App aufrufen | Öffnen Sie Ersetzungssteuerungen verwalten - Lokationen(F5312). | Das Bild Ersetzungssteuerungen verwalten - Lokationen wird angezeigt. |  |
| 3 | "Anlegen" wählen | Wählen Sie auf dem Bild Ersetzungssteuerungen verwalten - Lokationen die Option Anlegen. | Das Bild Ersetzungssteuerungen verwalten - Lokationen - Anlegen wird angezeigt. |  |
| 4 | Steuerung eingeben | Geben Sie im Bereich Kopf folgende Daten ein:Lokationsart: <Werk>Steuerung: <Geben Sie die neue Steuerung für die Ersetzung ein, z.B. REGION>. |  |  |
| 5 | Daten anlegen | Wählen Sie Anlegen. | Die Systemmeldung Steuerung angelegt wird angezeigt. |  |
| 6 | "Anlegen" wählen | Wählen Sie im Abschnitt Beschreibung die Option Anlegen. | Das Bild wird angezeigt. |  |
| 7 | Beschreibungsdaten eingeben | Nehmen Sie im Abschnitt Beschreibung die folgenden Einträge vor:Sprachenschlüssel: <Geben Sie die für die Steuerung geltende Sprache ein, z.B. DE Deutsch>.Steuerungsbeschreibung: <Geben Sie einen Text ein, um die Steuerung zu beschreiben, z.B. Steuerung für eine Region> |  |  |
| 8 | Daten anlegen | Wählen Sie Anlegen. | Die Systemmeldung Steuerungsbeschreibung angelegt wird angezeigt. |  |
| 9 | "Zurück" wählen | Wählen Sie im Abschnitt Titel die Option < (Zurück). | Das Bild Ersetzungssteuerungen verwalten - Lokationen wird angezeigt. |  |
| 10 | Gruppen zuordnen | Wählen Sie im Abschnitt Gruppen zuordnen die Option Zuordnen. | Das Dialogfenster Gruppen zur Steuerung zuordnen wird angezeigt. |  |
| 11 | "Gruppe" wählen | Suchen und wählen Sie im Dialogfenster die Option Gruppe.Wählen Sie z.B. Gruppe<SOUTH_REGION>.Wählen Sie Zuordnen. | Die Systemmeldung Gruppe(n) wurde(n) zugeordnet wird angezeigt. |  |

### Vorbereitende Schritte für die Lagerortersetzung

#### Grund für Lagerortersetzung anlegen (optional)

Testverwaltung

Kundenprojekt: Füllen Sie die projektbezogenen Teile aus.

|  |  |  |  |
| --- | --- | --- | --- |
| Testfall-ID | <X.XX> | Testdatum: |  |
| Testername: |  | Dauer: |  |
| Benutzerrolle(n): |  | Zuständigkeit: | <Geben Sie den Serviceanbieter, einen Kunden oder einen Serviceanbieter zusammen mit einem Kunden an.> |

Zweck

Die folgende Vorgehensweise stellt Anweisungen zum Anlegen von Gründen für die Ersetzung oder den Ausschluss von Lagerorten bereit. Die zur Verfügung stehenden Apps hängen von der Ihnen zugeordneten Rolle ab.

Vorgehensweise

| Testschrittnummer | Bezeichnung des Testschritts | Anweisung | Erwartetes Ergebnis | Kommentare |
| --- | --- | --- | --- | --- |
| 1 | Anmelden | Melden Sie sich am SAP Fiori Launchpad als Experte für die Auftragserfüllung an. | Das SAP Fiori Launchpad wird angezeigt. |  |
| 2 | SAP-Fiori-App aufrufen | Öffnen Sie Ersetzungsgründe verwalten - Lokationen(F5313). | Das Bild Ersetzungsgründe verwalten - Lokationen wird angezeigt. |  |
| 3 | "Anlegen" wählen | Wählen Sie auf dem Bild Ersetzungsgründe verwalten - Lokationen die Drucktaste Anlegen. | Das Bild Grund wird angezeigt. |  |
| 4 | Grund eingeben | Geben Sie im Bereich Kopf folgende Daten ein:Lokationsart: <Lagerort>Grund: <Geben Sie den neuen Ursachencode für die Lagerortersetzung ein, z.B. NEW_SLOC.> |  |  |
| 5 | Daten anlegen | Wählen Sie Anlegen. | Die Systemmeldung Grund wird angelegt wird angezeigt. |  |
| 6 | "Anlegen" wählen | Wählen Sie im Abschnitt Beschreibung die Option Anlegen. | Das Bild Beschreibung Grund wird angezeigt. |  |
| 7 | Beschreibungsdaten eingeben | Nehmen Sie im Abschnitt Beschreibung die folgenden Einträge vor:Sprachenschlüssel: <Geben Sie die für den Grund gültige Sprache ein, z.B. DE Deutsch.>Beschreibung Grund: <Geben Sie einen Text ein, um den Grund zu beschreiben, z.B. Neuer Lagerort ist verfügbar> |  |  |
| 8 | Daten anlegen | Wählen Sie Anlegen. | Die Systemmeldung Beschreibung angelegt wird angezeigt. |  |

#### Gruppe für Lagerortersetzung anlegen (optional)

Testverwaltung

Kundenprojekt: Füllen Sie die projektbezogenen Teile aus.

|  |  |  |  |
| --- | --- | --- | --- |
| Testfall-ID | <X.XX> | Testdatum: |  |
| Testername: |  | Dauer: |  |
| Benutzerrolle(n): |  | Zuständigkeit: | <Geben Sie den Serviceanbieter, einen Kunden oder einen Serviceanbieter zusammen mit einem Kunden an.> |

Zweck

In der folgenden Vorgehensweise finden Sie Anweisungen zum Anlegen von Gruppen für die Ersetzung oder den Ausschluss von Lagerorten. Verfügbare Apps sind von Ihrer Rolle abhängig.

Vorgehensweise

| Testschrittnummer | Bezeichnung des Testschritts | Anweisung | Erwartetes Ergebnis | Kommentare |
| --- | --- | --- | --- | --- |
| 1 | Anmelden | Melden Sie sich am SAP Fiori Launchpad als Experte für die Auftragserfüllung an. | Das SAP Fiori Launchpad wird angezeigt. |  |
| 2 | SAP-Fiori-App aufrufen | Öffnen Sie Ersetzungsgruppen verwalten - Lokationen(F5311). | Das Bild Ersetzungsgruppen verwalten - Lokationen wird angezeigt. |  |
| 3 | "Anlegen" wählen | Wählen Sie auf dem Bild Ersetzungsgruppen verwalten - Lokationen die Option Anlegen. | Das Bild Ersetzungsgruppen verwalten - Lokationen - Anlegen wird angezeigt. |  |
| 4 | Gruppe eingeben | Geben Sie im Bereich Kopf folgende Daten ein:Lokationsart: <Lagerort>Gruppe: <Geben Sie die neue Gruppe für die Ersetzung ein, z.B. COLD_STORAGE> |  |  |
| 5 | Daten anlegen | Wählen Sie Anlegen. | Die Systemmeldung Gruppe angelegt wird angezeigt. |  |
| 6 | "Anlegen" wählen | Wählen Sie im Abschnitt Beschreibung die Option Anlegen. | Das Bild Beschreibung Gruppe - Anlegen wird angezeigt. |  |
| 7 | Beschreibungsdaten eingeben | Nehmen Sie im Abschnitt Beschreibung die folgenden Einträge vor:Sprachenschlüssel: <Geben Sie die für die Gruppe geltende Sprache ein, z.B. DE Deutsch.>Beschreibung Gruppe: <Geben Sie einen Text zur Beschreibung der Gruppe ein, z.B. Lagerort für Kühllagerpositionen> |  |  |
| 8 | Daten anlegen | Wählen Sie Anlegen. | Die Systemmeldung Gruppenbeschreibung angelegt wird angezeigt. |  |
| 9 | "Zurück" wählen | Wählen Sie im Abschnitt Titel die Option < (Zurück). | Sie gelangen auf das Bild Ersetzungsgruppen verwalten - Lokationen. |  |
| 10 | Gruppendaten aktivieren | Wählen Sie Aktiv setzen. | Die Systemmeldung Status geändert wird angezeigt. |  |

#### Steuerung für Lagerortersetzung anlegen (optional)

Testverwaltung

Kundenprojekt: Füllen Sie die projektbezogenen Teile aus.

|  |  |  |  |
| --- | --- | --- | --- |
| Testfall-ID | <X.XX> | Testdatum: |  |
| Testername: |  | Dauer: |  |
| Benutzerrolle(n): |  | Zuständigkeit: | <Geben Sie den Serviceanbieter, einen Kunden oder einen Serviceanbieter zusammen mit einem Kunden an.> |

Zweck

Die folgende Vorgehensweise stellt Anweisungen zum Anlegen einer Steuerung für die Ersetzung oder den Ausschluss von Lagerorten bereit. Verfügbare Apps sind von Ihrer Rolle abhängig.

Vorgehensweise

| Testschrittnummer | Bezeichnung des Testschritts | Anweisung | Erwartetes Ergebnis | Kommentare |
| --- | --- | --- | --- | --- |
| 1 | Anmelden | Melden Sie sich als Experte für die Auftragserfüllung am SAP Fiori Launchpad an. | Das SAP Fiori Launchpad wird angezeigt. |  |
| 2 | SAP-Fiori-App aufrufen | Öffnen Sie Ersetzungssteuerungen verwalten - Lokationen(F5312). | Das Bild Ersetzungssteuerungen verwalten - Lokationen wird angezeigt. |  |
| 3 | "Anlegen" wählen | Wählen Sie auf dem Bild Ersetzungssteuerungen verwalten - Lokationen die Option Anlegen. | Das Bild Ersetzungssteuerungen - Lokationen - Anlegen wird angezeigt. |  |
| 4 | Steuerung eingeben | Geben Sie im Bereich Kopf folgende Daten ein:Lokationsart: <Lagerort>Steuerung: <Geben Sie die neue Steuerung für die Ersetzung ein, z.B. STORAGE_TYPE>. |  |  |
| 5 | Daten anlegen | Wählen Sie Anlegen. | Die Systemmeldung Steuerung angelegt wird angezeigt. |  |
| 6 | "Anlegen" wählen | Wählen Sie im Abschnitt Beschreibung die Option Anlegen. | Das Bild wird angezeigt. |  |
| 7 | Beschreibungsdaten eingeben | Nehmen Sie im Abschnitt Beschreibung die folgenden Einträge vor:Sprachenschlüssel: <Geben Sie die für die Steuerung geltende Sprache ein, z.B. DE Deutsch>.Steuerungsbeschreibung: <Geben Sie einen Text ein, um die Steuerung zu beschreiben, z.B. Steuerung für Lagertyp> |  |  |
| 8 | Daten anlegen | Wählen Sie Anlegen. | Die Systemmeldung Steuerungsbeschreibung angelegt wird angezeigt. |  |
| 9 | "Zurück" wählen | Wählen Sie im Abschnitt Titel die Option < (Zurück). | Das Bild Ersetzungssteuerungen - Lokationen wird angezeigt. |  |
| 10 | Gruppen zuordnen | Wählen Sie im Abschnitt Gruppen zuordnen die Option Zuordnen. | Das Dialogfenster Gruppen zur Steuerung zuordnen wird angezeigt. |  |
| 11 | "Gruppe" wählen | Suchen und wählen Sie im Dialogfenster die Option Gruppe.Wählen Sie z.B. Gruppe<COLD_STORAGE>.Wählen Sie Zuordnen. | Die Systemmeldung Gruppe(n) wurde(n) zugeordnet wird angezeigt. |  |

## Übersichtstabelle

Dieser Umfangsbestandteil umfasst die Segmente in der folgenden Tabelle:

|  |
| --- |
| Hinweis Wenn Ihr Systemadministrator Bereiche und Seiten auf dem SAP Fiori Launchpad aktiviert hat, enthält die Startseite nur die wesentlichen Apps, mit denen die typischen Aufgaben einer Benutzerrolle ausgeführt werden können.Alle anderen (suchbaren) Apps, die nicht auf der Startseite enthalten sind, finden Sie über die Suchleiste ([2434549](https://me.sap.com/notes/2434549)).Wenn Sie die Startseite personalisieren und versteckte Apps hinzufügen möchten, wechseln Sie in Ihr Benutzerprofil und wählen Sie App Finder. |

| Segment | Anwendungsrolle | App/Transaktion | Erwartete Ergebnisse |
| --- | --- | --- | --- |
| [Werksersetzung anlegen](#unique_14) [Seite ] 14 | Experte für die Auftragserfüllung | Ersetzungen verwalten - Lokationen(F5314) | Der Datensatz für die Werksersetzung wird angelegt. |
| [Werksausschluss anlegen](#unique_15) [Seite ] 15 | Experte für die Auftragserfüllung | Ausschlüsse verwalten - Lokationen(F5315) | Der Datensatz für den Werksausschluss wird angelegt. |
| [Lagerortersetzung anlegen](#unique_16) [Seite ] 17 | Experte für die Auftragserfüllung | Ersetzungen verwalten - Lokationen(F5314) | Der Datensatz für die Lagerortersetzung wird angelegt. |
| [Lagerortausschluss anlegen](#unique_17) [Seite ] 18 | Experte für die Auftragserfüllung | Ausschlüsse verwalten - Lokationen(F5315) | Der Datensatz für den Lagerortausschluss wird angelegt. |

## Testverfahren

In diesem Abschnitt werden die Testverfahren für den jeweiligen Prozessschritt beschrieben, der zum betreffenden Umfangsbestandteil gehört.

### Werksersetzung

#### Werksersetzung anlegen

Testverwaltung

Kundenprojekt: Füllen Sie die projektbezogenen Teile aus.

|  |  |  |  |
| --- | --- | --- | --- |
| Testfall-ID | <X.XX> | Testdatum: |  |
| Testername: |  | Dauer: |  |
| Benutzerrolle(n): |  | Zuständigkeit: | <Geben Sie den Serviceanbieter, einen Kunden oder einen Serviceanbieter zusammen mit einem Kunden an.> |

Zweck

Dieses Verfahren enthält eine Anleitung zum Anlegen einer Werksersetzung. Verfügbare Apps sind von Ihrer Rolle abhängig.

Vorgehensweise

| Testschrittnummer | Bezeichnung des Testschritts | Anweisung | Erwartetes Ergebnis | Kommentare |
| --- | --- | --- | --- | --- |
| 1 | Anmelden | Melden Sie sich am SAP Fiori Launchpad als Experte für die Auftragserfüllung an. | Das SAP Fiori Launchpad wird angezeigt. |  |
| 2 | SAP-Fiori-App aufrufen | Öffnen Sie Ersetzungen verwalten - Lokationen(F5314). | Das Bild Ersetzungen verwalten - Lokationen wird angezeigt. |  |
| 3 | "Anlegen" wählen | Wählen Sie in der Sicht Ersetzungen verwalten - Lokationen im Abschnitt Werk die Option Anlegen. | Das flexible Spaltenlayout Ersetzungen verwalten - Lokationen mit dem Bild "Anlegen" wird angezeigt. |  |
| 4 | Kopfdaten eingeben | Geben Sie im Bereich Kopf folgende Daten ein:Werk: <Geben Sie das Werk ein, das ersetzt werden soll.>Ersetzungswerk: <Geben Sie das Ersetzungswerk ein.>Verkaufsorganisation: <Nummer der Verkaufsorganisation>Vertriebsweg: <Nummer des Vertriebswegs>Werks- und Ersetzungswerkdaten sind obligatorisch, um eine Ersetzung anzulegen. |  |  |
| 5 | Daten in "Allgemeine Informationen" eingeben | Geben Sie im Bereich Allgemeine Informationen folgende Daten ein:Grund: <Geben Sie den Grund für das Anlegen eines Ersatzprodukts ein, z.B. NEW_PLANT>Gruppe: <Geben Sie die Ersetzungsgruppe ein, z.B. SOUTH_REGION>Gültig ab: <<Geben Sie den Starttermin für die Gültigkeit ein.>Gültig bis: <Geben Sie den Endtermin für die Gültigkeit ein.>Zeitzone: <Geben Sie die für die Gültigkeit geltende Zeitzone ein.>Die vorstehenden Einträge sind optional. |  |  |
| 6 | Daten anlegen | Wählen Sie Anlegen. | Die Systemmeldung Ersetzung angelegt wird angezeigt. |  |
| 7 | Werksersetzungsdaten aktivieren | Wählen Sie Aktiv setzen. | Die Systemmeldung Status geändert wird angezeigt. |  |
| 8 | Grafik anzeigen | Wählen Sie Grafik anzeigen. | Das Bild Netzplangrafik für Werk anzeigen wird angezeigt. |  |

#### Werksausschluss anlegen

Testverwaltung

Kundenprojekt: Füllen Sie die projektbezogenen Teile aus.

|  |  |  |  |
| --- | --- | --- | --- |
| Testfall-ID | <X.XX> | Testdatum: |  |
| Testername: |  | Dauer: |  |
| Benutzerrolle(n): |  | Zuständigkeit: | <Geben Sie den Serviceanbieter, einen Kunden oder einen Serviceanbieter zusammen mit einem Kunden an.> |

Zweck

Dieses Verfahren enthält eine Anleitung zum Anlegen eines Werksausschlusses. Verfügbare Apps sind von Ihrer Rolle abhängig.

Vorgehensweise

| Testschrittnummer | Bezeichnung des Testschritts | Anweisung | Erwartetes Ergebnis | Kommentare |
| --- | --- | --- | --- | --- |
| 1 | Anmelden | Melden Sie sich am SAP Fiori Launchpad als Experte für die Auftragserfüllung an. | Das SAP Fiori Launchpad wird angezeigt. |  |
| 2 | SAP-Fiori-App aufrufen | Öffnen Sie Ausschlüsse verwalten - Lokationen(F5315). | Das Bild Ausschlüsse verwalten - Lokationen wird angezeigt. |  |
| 3 | "Anlegen" wählen | Wählen Sie in der Sicht Ausschlüsse verwalten - Lokationen (Werk) die Option Anlegen. | Das Bild Werksausschluss wird angezeigt. |  |
| 4 | Kopfdaten eingeben | Geben Sie im Bereich Kopf folgende Daten ein:Werk: <Geben Sie das Werk ein, das von der Ersetzung ausgeschlossen werden soll.>Verkaufsorganisation: <Nummer der Verkaufsorganisation>Vertriebsweg: <Nummer des Vertriebswegs>Die Werkseingabe ist obligatorisch, um einen Ausschluss anzulegen. |  |  |
| 5 | Daten in "Allgemeine Informationen" eingeben | Geben Sie im Bereich Allgemeine Informationen folgende Daten ein:Grund: <Geben Sie den Grund für den Ausschluss des Werks ein.>Gruppe: <Geben Sie die Gruppe ein, die für den Werksausschluss gilt.>Gültig ab: <<Geben Sie den Starttermin für die Gültigkeit ein.>Gültig bis: <Geben Sie den Endtermin für die Gültigkeit ein.>Zeitzone: <Geben Sie die für die Gültigkeit geltende Zeitzone ein.>Die vorstehenden Einträge sind optional. |  |  |
| 6 | Daten anlegen | Wählen Sie Anlegen. | Die Systemmeldung Ausschluss angelegt wird angezeigt. |  |
| 7 | Werksausschlussdaten aktivieren | Wählen Sie Aktiv setzen. | Die Systemmeldung Status geändert wird angezeigt. |  |

### Lagerortersetzung

#### Lagerortersetzung anlegen

Testverwaltung

Kundenprojekt: Füllen Sie die projektbezogenen Teile aus.

|  |  |  |  |
| --- | --- | --- | --- |
| Testfall-ID | <X.XX> | Testdatum: |  |
| Testername: |  | Dauer: |  |
| Benutzerrolle(n): |  | Zuständigkeit: | <Geben Sie den Serviceanbieter, einen Kunden oder einen Serviceanbieter zusammen mit einem Kunden an.> |

Zweck

Dieses Verfahren enthält eine Anleitung zum Anlegen einer Lagerortersetzung. Verfügbare Apps sind von Ihrer Rolle abhängig.

Vorgehensweise

| Testschrittnummer | Bezeichnung des Testschritts | Anweisung | Erwartetes Ergebnis | Kommentare |
| --- | --- | --- | --- | --- |
| 1 | Anmelden | Melden Sie sich am SAP Fiori Launchpad als Experte für die Auftragserfüllung an. | Das SAP Fiori Launchpad wird angezeigt. |  |
| 2 | SAP-Fiori-App aufrufen | Öffnen Sie Ersetzungen verwalten - Lokationen(F5314). | Das Bild Ersetzungen verwalten - Lokationen wird angezeigt. |  |
| 3 | Lagerort auswählen | Wählen Sie auf dem Bild Ersetzungen verwalten - Lokationen die Registerkarte Lagerort. | Das Bild Ersetzungen verwalten - Lokationen (Lagerort) wird angezeigt. |  |
| 4 | "Anlegen" wählen | Wählen Sie auf der Registerkarte Lagerort die Option Anlegen. | Das flexible Spaltenlayout Ersetzungen verwalten - Lokationen mit dem Bild "Anlegen" wird angezeigt. |  |
| 5 | Kopfdaten eingeben | Geben Sie im Bereich Kopf folgende Daten ein:Werk: <Werksnummer>Lagerort: <Geben Sie den Lagerort ein, der ersetzt werden soll.>Ersetzungslagerort: <Geben Sie den Ersetzungslagerort ein.>Werks- und Ersetzungslagerortdaten sind obligatorisch, um eine Ersetzung anzulegen, wobei der Lagerort optional ist. "Werk" wird standardmäßig ausgewählt, wenn "Lagerort" ausgewählt ist. |  |  |
| 6 | Daten in "Allgemeine Informationen" eingeben | Geben Sie im Bereich Allgemeine Informationen folgende Daten ein:Grund: <Geben Sie den Grund für das Anlegen eines Ersatzprodukts ein, z.B. NEW_SLOC>Gruppe: <Geben Sie die Ersetzungsgruppe ein, z.B. COLD_STORAGE>Gültig ab: <<Geben Sie den Starttermin für die Gültigkeit ein.>Gültig bis: <Geben Sie den Endtermin für die Gültigkeit ein.>Zeitzone: <Geben Sie die für die Gültigkeit geltende Zeitzone ein.>Die vorstehenden Einträge sind optional. |  |  |
| 7 | Daten anlegen | Wählen Sie Anlegen. | Die Systemmeldung Ersetzung angelegt wird angezeigt. |  |
| 8 | Lagerortersetzungsdaten aktivieren | Wählen Sie Aktiv setzen. | Die Systemmeldung Status geändert wird angezeigt. |  |
| 9 | Grafik anzeigen | Wählen Sie Grafik anzeigen. | Das Bild Netzplangrafik des Lagerorts anzeigen wird angezeigt. |  |

#### Lagerortausschluss anlegen

Testverwaltung

Kundenprojekt: Füllen Sie die projektbezogenen Teile aus.

|  |  |  |  |
| --- | --- | --- | --- |
| Testfall-ID | <X.XX> | Testdatum: |  |
| Testername: |  | Dauer: |  |
| Benutzerrolle(n): |  | Zuständigkeit: | <Geben Sie den Serviceanbieter, einen Kunden oder einen Serviceanbieter zusammen mit einem Kunden an.> |

Zweck

Dieses Verfahren enthält eine Anleitung zum Anlegen eines Lagerortausschlusses. Verfügbare Apps sind von Ihrer Rolle abhängig.

Vorgehensweise

| Testschrittnummer | Bezeichnung des Testschritts | Anweisung | Erwartetes Ergebnis | Kommentare |
| --- | --- | --- | --- | --- |
| 1 | Anmelden | Melden Sie sich am SAP Fiori Launchpad als Experte für die Auftragserfüllung an. | Das SAP Fiori Launchpad wird angezeigt. |  |
| 2 | SAP-Fiori-App aufrufen | Öffnen Sie Ausschlüsse verwalten - Lokationen(F5315). | Das Bild Ausschlüsse verwalten - Lokationen wird angezeigt. |  |
| 3 | Lagerort auswählen | Wählen Sie in der Sicht Ausschlüsse verwalten - Lokationen die Option Lagerort. | Das Bild Ausschlüsse verwalten - Lokationen (Lagerort) wird angezeigt. |  |
| 4 | "Anlegen" wählen | Wählen Sie in der Sicht Ausschlüsse verwalten - Lokationen (Lagerort) die Option Anlegen. | Das Bild Ausschlüsse verwalten - Lokationen - Anlegen wird angezeigt. |  |
| 5 | Kopfdaten eingeben | Geben Sie im Bereich Kopf folgende Daten ein:Werk: <Werksnummer>Lagerort: <Geben Sie den Lagerort ein, der von der Ersetzung ausgeschlossen werden soll.>Sowohl Werk als auch Lagerort müssen ausgeschlossen werden. |  |  |
| 6 | Daten in "Allgemeine Informationen" eingeben | Geben Sie im Bereich Allgemeine Informationen folgende Daten ein:Grund: <Geben Sie den Grund für den Ausschluss des Lagerorts ein.>Gruppe: <Geben Sie die Gruppe ein, die für den Lagerortsausschluss gilt.>Gültig ab: <Geben Sie den Starttermin für die Gültigkeit ein.>Gültig bis: <Geben Sie den Endtermin für die Gültigkeit ein.>Zeitzone: <Geben Sie die für die Gültigkeit geltende Zeitzone ein.>Die vorstehenden Einträge sind optional. |  |  |
| 7 | Daten anlegen | Wählen Sie Anlegen. | Die Systemmeldung Ausschluss angelegt wird angezeigt. |  |
| 8 | Lagerortausschlussdaten aktivieren | Wählen Sie Aktiv setzen. | Die Systemmeldung Status geändert wird angezeigt. |  |

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
- related-to :: [[08-sales-order-management/master-data-script-create-location-substitution-and-exclusion-mds-5ng]]
- related-to :: [[08-sales-order-management/mds-5ng-475]]
- related-to :: [[08-sales-order-management/mds-5ng-477]]
- related-to :: [[08-sales-order-management/script-de-dados-mestre-criar-substituicao-e-exclusao-de-local-mds-5ng]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/5NG_S4CLD2608_Master_Data_DE_XX.docx` — full document · extracted with `mammoth` · 32,620 chars in the whole document
