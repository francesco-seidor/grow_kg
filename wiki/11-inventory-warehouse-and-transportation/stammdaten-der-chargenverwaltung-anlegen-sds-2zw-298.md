---
id: 11-inventory-warehouse-and-transportation/stammdaten-der-chargenverwaltung-anlegen-sds-2zw-298
title: Stammdaten der Chargenverwaltung anlegen – SDS (2ZW) (2ZW_S4CLD2608_Master_Data_DE_XX)
description: "German SAP S/4HANA Cloud master data script (2ZW): create batch management master data - characteristics, classes, sort orders, search and derivation strategies."
cluster: 11-inventory-warehouse-and-transportation
tags: [kb/inventory-warehouse-and-transportation, topic/batch-management-master-data]
aliases: [2ZW_S4CLD2608_Master_Data_DE_XX]
keywords: [Batch Management Master Data, batch characteristics, batch classes, sort sequences, batch search strategies, batch determination, batch derivation strategies, classification system, business roles, master data scripts]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/2ZW_S4CLD2608_Master_Data_DE_XX.docx]
confidence: high
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-298
topic: 11-inventory-warehouse-and-transportation/batch-management-master-data
language: DE
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Stammdaten der Chargenverwaltung anlegen – SDS (2ZW) (2ZW_S4CLD2608_Master_Data_DE_XX)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/2ZW_S4CLD2608_Master_Data_DE_XX.docx`, extracted with `mammoth`. Grouped under **Batch Management Master Data** in Inventory, Warehouse and Transportation. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

| <!-- image omitted: unnamed --> | StammdatenskriptSAP S/4HANA Cloud Public Edition - 02-07-26 |
| --- | --- |
|  | Stammdaten der Chargenverwaltung anlegen – SDS (2ZW) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Inhaltsverzeichnis

[1 Verwendungszweck 2](#_Toc233889607)

[2 Voraussetzungen 3](#_Toc233889608)

[2.1 Systemzugriff 3](#_Toc233889609)

[2.2 Rollen 3](#_Toc233889610)

[3 Übersichtstabelle 4](#_Toc233889611)

[4 Testverfahren 5](#_Toc233889612)

[4.1 Merkmal anlegen 5](#_Toc233889613)

[4.2 Klasse anlegen 6](#_Toc233889614)

[4.3 Sortierreihenfolge anlegen 7](#_Toc233889615)

[4.4 Chargensuchstrategiesatz für Bestandsführung anlegen 8](#_Toc233889616)

[4.5 Chargensuchstrategiesätze für die Produktion anlegen 10](#_Toc233889617)

[4.6 Chargensuchstrategiesätze für Vertrieb anlegen 12](#_Toc233889618)

[4.7 Ableitungsstrategie für Sendermaterial anlegen 14](#_Toc233889619)

[4.8 Ableitungsstrategie für Empfängermaterial anlegen 15](#_Toc233889620)

## Verwendungszweck

Zu den Chargenverwaltungsstammdaten gehören Chargenspezifikationen, Sortierreihenfolgen (Sortierregeln) und Chargensuchstrategiesätze in der Chargenfindung.

Chargenspezifikationen beschreiben die technischen, physikalischen und chemischen Eigenschaften einer Charge. Chargenspezifikationen, wie z.B. der Chargenstatus oder der Wirkstoffgehalt, werden im Klassifizierungssystem als Merkmale gesichert.

Über das Klassifizierungssystem können Sie die Materialspezifikationen dem Material einer Charge zuordnen. Diese Materialspezifikationen werden derselben Klasse zugeordnet wie die Chargen des Materials. So können Sie die Zielwerte einer Charge zusammen mit dem entsprechenden Toleranzbereich ablegen. Diese Zielwerte werden z.B. bei der Qualitätsprüfung oder während des Wareneingangs verwendet, wenn es erforderlich ist, eine Charge sofort zu klassifizieren. Die Werte werden auch bei der Verwendbarkeitsprüfung verwendet.

Im Material legen Sie die Zielbereiche für alle Merkmale ab. Da die Charge zu derselben Klasse gehört wie das Material, erhält die Charge automatisch die Merkmale des Materials. Geben Sie für jede einzelne Charge die exakten Istwerte ein.

Die Chargenfindung in verschiedenen Prozessen (Bestandsführung, Produktion, Vertrieb) hat unterschiedliche Kriterien. Zur Pflege der Kriterien werden Sortierreihenfolgen und Chargensuchstrategiesätze benötigt.

Die Sortierreihenfolge gibt an, ob Chargen im Suchergebnis der Chargenfindung nach Merkmalswerten aufsteigend oder absteigend sortiert werden.

In einer Chargensuchstrategie für die Chargenfindung können Sie festlegen, nach welchen Werten das System Chargen finden soll, einschließlich der Attribute für den Prozess (z.B. Bewegungsart, Auftragsart oder Werk) und die Materialnummer. Erst wenn die Konditionssätze erfüllt sind, können diese Chargen anhand von Sortierreihenfolgen und Chargenspezifikationen weiter sortiert und gefunden werden.

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
| Stücklistenbearbeiter | SAP_BR_BOM_ENGINEER | Stücklisten | SAP_BR_BOM_ENGINEER |  |
| Stammdatenexperte – Chargendaten | SAP_BR_BATCH_MASTER_SPCLST | Stammdaten - Charge | SAP_BR_BATCH_MASTER_SPCLST |  |

## Übersichtstabelle

Dieser Umfangsbestandteil umfasst mehrere Prozessschritte, die in der folgenden Tabelle aufgelistet sind:

|  |
| --- |
| Hinweis Wenn Ihr Systemadministrator Bereiche und Seiten auf dem SAP Fiori Launchpad aktiviert hat, enthält die Startseite nur die wesentlichen Apps, mit denen die typischen Aufgaben einer Benutzerrolle ausgeführt werden können.Alle anderen (suchbaren) Apps, die nicht auf der Startseite enthalten sind, finden Sie über die Suchleiste ([2434549](https://me.sap.com/notes/2434549)).Wenn Sie die Startseite personalisieren und versteckte Apps hinzufügen möchten, wechseln Sie in Ihr Benutzerprofil und wählen Sie App Finder. |

| Prozessschritt | Anwendungsrolle | Bewegung | Erwartete Ergebnisse |
| --- | --- | --- | --- |
| [Merkmal anlegen](#unique_6) [Seite ] 5 | Stücklistenbearbeiter | Merkmale verwalten(CT04) | Das Merkmal wird angelegt. |
| [Klasse anlegen](#unique_7) [Seite ] 6 | Stücklistenbearbeiter | Klassen verwalten(CL02) | Die Klasse wird angelegt. |
| [Sortierreihenfolge anlegen](#unique_8) [Seite ] 7 | Stammdatenexperte – Chargendaten | Sortierreihenfolgen anlegen(CU70) | Die Sortierreihenfolge wird angelegt. |
| [Chargensuchstrategiesatz für Bestandsführung anlegen](#unique_9) [Seite ] 8 | Stammdatenexperte – Chargendaten | Suchstrategien verwalten - Bestandsführung(MBC2) | Chargensuchstrategiesätze werden angelegt. |
| [Chargensuchstrategiesätze für die Produktion anlegen](#unique_10) [Seite ] 10 | Stammdatenexperte – Chargendaten | Suchstrategien verwalten - Produktion(COB2) | Chargensuchstrategiesätze werden angelegt. |
| [Chargensuchstrategiesätze für Vertrieb anlegen](#unique_11) [Seite ] 12 | Stammdatenexperte – Chargendaten | Suchstrategien verwalten - Vertrieb(VCH2) | Chargensuchstrategiesätze werden angelegt. |
| [Ableitungsstrategie für Sendermaterial anlegen](#unique_12) [Seite ] 14 | Stammdatenexperte – Chargendaten | Ableitungsstrategien verwalten - Absender(DVS2) | Die Ableitungsstrategie für das Sendermaterial wird angelegt. |
| [Ableitungsstrategie für Empfängermaterial anlegen](#unique_13) [Seite ] 15 | Stammdatenexperte – Chargendaten | Ableitungsstrategien verwalten - Empfänger(DVR2) | Die Ableitungsstrategie für das Empfängermaterial wird angelegt. |

## Testverfahren

In diesem Abschnitt werden die Testverfahren für den jeweiligen Prozessschritt beschrieben, der zum betreffenden Umfangsbestandteil gehört.

### Merkmal anlegen

Testverwaltung

Kundenprojekt: Füllen Sie die projektbezogenen Teile aus.

|  |  |  |  |
| --- | --- | --- | --- |
| Testfall-ID | <X.XX> | Testdatum: |  |
| Testername: |  | Dauer: |  |
| Benutzerrolle(n): |  | Zuständigkeit: | <Geben Sie den Serviceanbieter, einen Kunden oder einen Serviceanbieter zusammen mit einem Kunden an.> |

Zweck

Dieses Verfahren enthält eine Anleitung zum Anlegen eines Merkmals.

Vorgehensweise

Gehen Sie folgendermaßen vor, wenn Sie mit Ihrer Benutzerrolle auf die App Merkmale verwalten(CT04) zugreifen können.

| Testschrittnummer | Bezeichnung des Testschritts | Anweisungen | Erwartetes Ergebnis | Kommentare |
| --- | --- | --- | --- | --- |
| 1 | Anmelden | Melden Sie sich als Stücklistenbearbeiter am SAP Fiori Launchpad an. | Das SAP Fiori Launchpad wird angezeigt. |  |
| 2 | SAP-Fiori-App aufrufen | Öffnen Sie Merkmale verwalten(CT04). | Das Bild Merkmale wird angezeigt.Hinweis Gemeinsames Bild für die Modi Anlegen, Ändern und Anzeigen. |  |
| 3 | Merkmalsnamen eingeben | Geben Sie Folgendes ein, und wählen Sie Anlegen:Merkmal: <Ihr Merkmalsname> | Das Optionen des Bildes Grunddaten werden angezeigt.Hinweis Das Feld Gültig ab wird automatisch mit einem Wert befüllt. |  |
| 4 | Grunddaten eingeben | Geben Sie Folgendes ein, und wählen Sie Sichern.Bereich Grunddaten:Beschreibung: <Beschreibung eingeben>Status: Freigegeben (Standard)Bereich Format:Datentyp: <Format wählen>Bereich Bewertung:Markieren Sie den Auswahlknopf Einwertig. | Hinweis Im Abschnitt Format sind weitere Eingaben zum ausgewählten Format erforderlich. Geben Sie die entsprechenden Daten ein. |  |
| 5 | Werte für Prüfung eingeben | Auf der Registerkarte Werte geben Sie im Bereich Zulässige Werte die zulässigen Werte für dieses Merkmal ein. |  |  |
| 6 | Merkmal sichern | Wählen Sie Sichern. | Das Merkmal wird angelegt. |  |

### Klasse anlegen

Testverwaltung

Kundenprojekt: Füllen Sie die projektbezogenen Teile aus.

|  |  |  |  |
| --- | --- | --- | --- |
| Testfall-ID | <X.XX> | Testdatum: |  |
| Testername: |  | Dauer: |  |
| Benutzerrolle(n): |  | Zuständigkeit: | <Geben Sie den Serviceanbieter, einen Kunden oder einen Serviceanbieter zusammen mit einem Kunden an.> |

Zweck

Dieses Verfahren enthält eine Anleitung zum Anlegen einer Klasse.

Voraussetzung

Sie müssen erst den vorherigen Abschnitt, [Merkmal anlegen](#unique_6) [Seite ] 5, abschließen, bevor Sie mit diesem Abschnitt fortfahren können.

Vorgehensweise

Gehen Sie folgendermaßen vor, wenn Sie aufgrund Ihrer Benutzerrolle auf die App Klassen verwalten(CL02) zugreifen können.

| Testschrittnummer | Bezeichnung des Testschritts | Anweisung | Erwartetes Ergebnis | Kommentare |
| --- | --- | --- | --- | --- |
| 1 | Anmelden | Melden Sie sich am SAP Fiori Launchpad als Stücklistenbearbeiter an. | Das SAP Fiori Launchpad wird angezeigt. |  |
| 2 | SAP-Fiori-App aufrufen | Öffnen Sie Klassen verwalten(CL02). | Das Bild Klasse wird angezeigt.Hinweis Es handelt sich um ein allgemeines Bild für Anlege-, Änderungs- und Anzeigemodi. |  |
| 3 | Klassennamen eingeben | Nehmen Sie folgende Einträge vor, und wählen Sie Anlegen:Klasse: <Klassenname>Klassenart: 023 | Das Bild Klasse anlegen wird angezeigt.Hinweis Das Feld Gültig ab wird automatisch mit einem Wert gefüllt. |  |
| 4 | Grunddaten eingeben | Geben Sie auf der Registerkarte Grunddaten folgende Daten ein:Im Bereich Grunddaten:Beschreibung: <Beschreibung der Klasse>Status: Freigegeben |  |  |
| 5 | Registerkarte "Merkmale" Registerkarte | Wählen Sie die Registerkarte Merkmale, und geben Sie Folgendes ein, um die von Ihnen angelegten Merkmale dieser Klasse zuzuordnen. Wählen Sie anschließend Enter:In der Spalte Merkmal:Merkmal: <Merkmalsname> | Die Felder Beschreibung und Datentyp von Merkmalen werden automatisch mit Werten gefüllt. |  |

### Sortierreihenfolge anlegen

Testverwaltung

Kundenprojekt: Füllen Sie die projektbezogenen Teile aus.

|  |  |  |  |
| --- | --- | --- | --- |
| Testfall-ID | <X.XX> | Testdatum: |  |
| Testername: |  | Dauer: |  |
| Benutzerrolle(n): |  | Zuständigkeit: | <Geben Sie den Serviceanbieter, einen Kunden oder einen Serviceanbieter zusammen mit einem Kunden an.> |

Zweck

Dieses Verfahren enthält eine Anleitung zum Anlegen von Sortierfolgen.

Voraussetzung

Sie müssen den Abschnitt Merkmal anlegen erst abschließen, bevor Sie mit diesem Abschnitt fortfahren können.

Vorgehensweise

Gehen Sie folgendermaßen vor, wenn Sie aufgrund Ihrer Benutzerrolle auf die App Sortierreihenfolgen anlegen(CU70) zugreifen können.

| Testschrittnummer | Bezeichnung des Testschritts | Anweisungen | Erwartetes Ergebnis | Kommentare |
| --- | --- | --- | --- | --- |
| 1 | Anmelden | Melden Sie sich am SAP Fiori Launchpad als Stammdatenexperte – Chargendaten an. | Das SAP Fiori Launchpad wird angezeigt. |  |
| 2 | SAP-Fiori-App aufrufen | Öffnen Sie Sortierreihenfolgen anlegen(CU70). | Das Bild Sortierreihenfolge anlegen wird angezeigt. |  |
| 3 | Name der Sortierreihenfolge eingeben | Geben Sie folgende Daten ein, und wählen Sie Anlegen.Sortierreihenfolge: <Name der Sortierreihenfolge> | Das Bild Sortierreihenfolgen anlegen: Grunddaten wird angezeigt. |  |
| 4 | Grunddaten eingeben | Geben Sie die Beschreibung neben dem Namen der Sortierreihenfolge ein, und wählen Sie Merkmale.Beschreibung: <Beschreibung der Sortierreihenfolge> | Das Bild Sortierreihenfolgen anlegen: Merkmale wird angezeigt. |  |
| 5 | Details zur Sortierreihenfolge eingeben | Wählen Sie Neue Einträge, pflegen Sie folgende Spalten, und wählen Sie Sichern:Merkmal: <Merkmalsname>Aufsteigend: XAbsteigend: ‘ ’ | Die Sortierreihenfolgen wird angelegt.Hinweis Sie können zwischen aufsteigender und absteigender Sortierung wählen. |  |

### Chargensuchstrategiesatz für Bestandsführung anlegen

Testverwaltung

Kundenprojekt: Füllen Sie die projektbezogenen Teile aus.

|  |  |  |  |
| --- | --- | --- | --- |
| Testfall-ID | <X.XX> | Testdatum: |  |
| Testername: |  | Dauer: |  |
| Benutzerrolle(n): |  | Zuständigkeit: | <Geben Sie den Serviceanbieter, einen Kunden oder einen Serviceanbieter zusammen mit einem Kunden an.> |

Verwendungszweck

Die folgende Vorgehensweise bietet eine Anleitung zum Anlegen von Suchstrategien für die Chargenfindung.

Vorgehensweise

| Testschrittnummer | Bezeichnung des Testschritts | Anweisungen | Erwartetes Ergebnis | Kommentare |
| --- | --- | --- | --- | --- |
| 1 | Anmeldung | Melden Sie sich als Stammdatenexperte – Chargendaten am SAP Fiori Launchpad an. | Das SAP Fiori Launchpad wird angezeigt. |  |
| 2 | Das SAP Fiori Launchpad wird angezeigt. | Öffnen Sie Suchstrategien verwalten - Bestandsführung(MBC2). | Das Bild Chargensuchstrategie ändern: Einstieg wird angezeigt. |  |
| 3 | Strategieart eingeben | Geben Sie folgende Daten ein, und wählen Sie Ändern:Strategieart: <Strategieart, z.B. YB11>Hinweis Die Strategieart ist über die Self-Service-Konfigurations-UI konfigurierbar. | Das Dialogfenster Schlüsselkombination wird angezeigt. |  |
| 4 | Schlüsselkombination auswählen | Wählen Sie im Dialogfenster Schlüsselkombination eine der folgenden Optionen aus, und wählen Sie Auswählen:Bewegungsart/Werk/MaterialWerk/MaterialBewegungsart/MaterialBewegungsart/WerkBewegungsart | Das Bild BP ändern: Chargennummer (YB11): Selektion wird angezeigt. | Die Schlüsselkombinationen hängen von der ausgewählten Strategieart ab. Wenn in Ihrer ausgewählten Strategie nur eine Schlüsselkombination vorhanden ist, wird das Dialogfenster nicht angezeigt. |
| 5 | Auswahl eingeben | Um Ihre Datensätze anzugeben, geben Sie die folgenden Attribute ein, die basierend auf der ausgewählten Schlüsselkombination angezeigt werden, und wählen Sie Ausführen:Warenbewegungsart: <Warenbewegungsart>Werk: <Werk>Material: <Materialnummer> | Das Bild BP ändern: Chargennummer (YB11): Schnellerfassung wird angezeigt. |  |
| 6 | Strategiesatz im Detail eingeben | Um einen neuen Datensatz anzulegen, geben Sie folgende Daten ein, und wählen Sie Sichern:Material: <Materialnummer>Falls erforderlich, können Sie auch die folgenden Attribute für jeden Datensatz angeben:Anz. ChargensplitsÄndern erlaubtDialog ChargenfindungAnzeige-MEMengenvorschlagÜberlieferg. erlaubtSelektionsart |  |  |
| 7 | Selektionskriterien pflegen (optional) | Um die Selektionskriterien für den Chargenmerkmalswert des Materials in einem Datensatz zu pflegen, markieren Sie den Datensatz, und wählen Sie Selektionskriterien. | Das Bild BP ändern: Klassifizierung wird angezeigt. |  |
| 8 | Sortierfolge pflegen (optional) | Um die Sortierfolge für bestimmte Datensätze zu pflegen, markieren Sie den Datensatz, und wählen Sie Sortieren. | Das Bild BP ändern: Chargennummer (YB11): Sortierregel wird angezeigt. |  |

### Chargensuchstrategiesätze für die Produktion anlegen

Testverwaltung

Kundenprojekt: Füllen Sie die projektbezogenen Teile aus.

|  |  |  |  |
| --- | --- | --- | --- |
| Testfall-ID | <X.XX> | Testdatum: |  |
| Testername: |  | Dauer: |  |
| Benutzerrolle(n): |  | Zuständigkeit: | <Geben Sie den Serviceanbieter, einen Kunden oder einen Serviceanbieter zusammen mit einem Kunden an.> |

Zweck

Die folgende Vorgehensweise bietet eine Anleitung zum Anlegen von Suchstrategien für die Chargenfindung.

Vorgehensweise

| Testschrittnummer | Bezeichnung des Testschritts | Anweisungen | Erwartetes Ergebnis | Kommentare |
| --- | --- | --- | --- | --- |
| 1 | Anmeldung | Melden Sie sich als Stammdatenexperte – Chargendaten am SAP Fiori Launchpad an. | Das SAP Fiori Launchpad wird angezeigt. |  |
| 2 | SAP-Fiori-App aufrufen | Öffnen Sie Suchstrategien verwalten - Produktion(COB2). | Das Bild Chargensuchstrategie ändern: Einstieg wird angezeigt. |  |
| 3 | Strategieart eingeben | Geben Sie folgende Daten ein, und wählen Sie "Ändern":Strategieart: <Strategieart, z.B. YB11>Hinweis Die Strategieart kann über die Self-Service-Konfigurations-UI konfiguriert werden. | Das Bild GP ändern: Chargennummer (YB11): Selektion wird angezeigt.Hinweis Die Schlüsselkombination wird nicht angezeigt, da in der Produktion nur eine Schlüsselkombination für YB11 konfiguriert ist |  |
| 4 | Auswahl eingeben | Um Ihre Datensätze anzugeben, geben Sie die folgenden Attribute ein, die basierend auf der ausgewählten Schlüsselkombination angezeigt werden, und wählen Sie Ausführen:Auftragsart: <Auftragsart>Werk: <Werk>Material: <Materialnummer> | Das Bild GP ändern: Chargennummer (YB11): Schnellerfassung wird angezeigt. | Die Schlüsselkombinationen hängen von der ausgewählten Strategieart ab. Wenn in Ihrer ausgewählten Strategie nur eine Schlüsselkombination vorhanden ist, wird das Dialogfenster nicht angezeigt. |
| 5 | Strategiesatz im Detail eingeben | Um einen neuen Datensatz anzulegen, geben Sie folgende Daten ein, und wählen Sie Sichern:Material: <Materialnummer>Falls erforderlich, können Sie auch die folgenden Attribute für jeden Datensatz angeben:Anz. ChargensplitsÄndern erlaubtDialog ChargenfindungAnzeige-MEMengenvorschlagÜberlieferg. erlaubtSelektionsart |  |  |
| 6 | Selektionskriterien pflegen (optional) | Um die Selektionskriterien für den Chargenmerkmalswert des Materials in einem Datensatz zu pflegen, markieren Sie den Datensatz, und wählen Sie Selektionskriterien. | Das Bild GP ändern: Klassifizierung wird angezeigt. |  |
| 7 | Sortierfolge pflegen (optional) | Um die Sortierfolge für bestimmte Datensätze zu pflegen, markieren Sie den Datensatz, und wählen Sie Sortieren. | Das Bild GP ändern: Chargennummer (YB11): Sortierregel wird angezeigt. |  |

### Chargensuchstrategiesätze für Vertrieb anlegen

Testverwaltung

Kundenprojekt: Füllen Sie die projektbezogenen Teile aus.

|  |  |  |  |
| --- | --- | --- | --- |
| Testfall-ID | <X.XX> | Testdatum: |  |
| Testername: |  | Dauer: |  |
| Benutzerrolle(n): |  | Zuständigkeit: | <Geben Sie den Serviceanbieter, einen Kunden oder einen Serviceanbieter zusammen mit einem Kunden an.> |

Zweck

Die folgende Vorgehensweise stellt eine Anleitung zum Anlegen von Suchstrategien für die Chargenfindung zur Verfügung.

Vorgehensweise

| Testschrittnummer | Bezeichnung des Testschritts | Anweisungen | Erwartetes Ergebnis | Kommentare |
| --- | --- | --- | --- | --- |
| 1 | Anmeldung | Melden Sie sich als Stammdatenexperte – Chargendaten am SAP Fiori Launchpad an. | Das SAP Fiori Launchpad wird angezeigt. |  |
| 2 | SAP-Fiori-App aufrufen | Öffnen Sie Suchstrategien verwalten - Vertrieb(VCH2). | Das Bild "Chargensuchstrategie ändern: Einstieg" wird angezeigt. |  |
| 3 | Strategieart eingeben | Geben Sie folgende Daten ein, und wählen Sie "Ändern:"Strategieart: <Strategieart, z.B. YB11>Hinweis Die Strategieart ist über die Self-Service-Konfigurations-UI konfigurierbar. | Das Dialogfenster Schlüsselkombination wird angezeigt. |  |
| 4 | Schlüsselkombination auswählen | Wählen Sie im Dialogfenster Schlüsselkombination eine der folgenden Optionen aus, und wählen Sie Auswählen:Kunde/MaterialMaterial | Das Bild GP ändern: Chargennummer (YB11): Selektion wird angezeigt. | Die Schlüsselkombinationen hängen von der ausgewählten Strategieart ab. Wenn in Ihrer ausgewählten Strategie nur eine Schlüsselkombination vorhanden ist, wird das Dialogfenster nicht angezeigt. |
| 5 | Auswahl eingeben | Um Ihre Datensätze anzugeben, geben Sie die folgenden Attribute ein, die basierend auf der ausgewählten Schlüsselkombination angezeigt werden, und wählen Sie Ausführen:Kunde: <Kunden-ID>Material: <Materialnummer> | Das Bild GP ändern: Chargennummer (YB11): Schnellerfassung wird angezeigt. |  |
| 6 | Strategiesatz im Detail eingeben | Um einen neuen Datensatz anzulegen, geben Sie folgende Daten ein, und wählen Sie Sichern:Material: <Materialnummer>Falls erforderlich, können Sie auch die folgenden Attribute für jeden Datensatz angeben:Anz. ChargensplitsÄndern erlaubtDialog ChargenfindungAnzeige-MEMengenvorschlagÜberlieferg. erlaubtSelektionsart |  |  |
| 7 | Selektionskriterien pflegen (optional) | Um die Selektionskriterien für den Chargenmerkmalswert des Materials in einem Datensatz zu pflegen, markieren Sie den Datensatz, und wählen Sie Selektionskriterien. | Das Bild GP ändern: Klassifizierung wird angezeigt. |  |
| 8 | Sortierreihenfolge pflegen (optional) | Um die Sortierreihenfolge für bestimmte Datensätze zu pflegen, markieren Sie den Datensatz, und wählen Sie Sortieren. | Das Bild GP ändern: Chargennummer (YB11): Sortierregel wird angezeigt. |  |

### Ableitungsstrategie für Sendermaterial anlegen

Testverwaltung

Kundenprojekt: Füllen Sie die projektbezogenen Teile aus.

|  |  |  |  |
| --- | --- | --- | --- |
| Testfall-ID | <X.XX> | Testdatum: |  |
| Testername: |  | Dauer: |  |
| Benutzerrolle(n): |  | Zuständigkeit: | <Geben Sie den Serviceanbieter, einen Kunden oder einen Serviceanbieter zusammen mit einem Kunden an.> |

Zweck

Die folgende Vorgehensweise enthält Anweisungen zum Anlegen von Strategiesätzen, die verwendet werden, um Attribute für das Sendermaterial während der Chargenableitung zu ermitteln.

Vorgehensweise

| Testschrittnummer | Bezeichnung des Testschritts | Anweisung | Erwartetes Ergebnis | Kommentare |
| --- | --- | --- | --- | --- |
| 1 | Anmelden | Melden Sie sich am SAP Fiori Launchpad als Stammdatenexperte – Chargendaten an. | Das SAP Fiori Launchpad wird angezeigt. |  |
| 2 | SAP-Fiori-App aufrufen | Öffnen Sie Ableitungsstrategien verwalten - Absender(DVS2). | Das Bild Ableitung - Suchstrategie ändern: Einstieg wird angezeigt. |  |
| 3 | Strategieart eingeben | Geben Sie folgende Daten ein, und wählen Sie Ändern:Strategieart: <Strategieart> | Das Dialogfenster Schlüsselkombination wird angezeigt. | Vor diesem Schritt müssen Sie die folgenden Konfigurationsschritte Ihren Anforderungen entsprechend abschließen:Nummernkreise für die Ableitung von ChargenSendende Chargen in der Chargenableitung ermitteln |
| 4 | Schlüsselkombination auswählen | Wählen Sie im Dialogfenster Schlüsselkombination eine der folgenden Optionen aus, und wählen Sie Auswählen:<Schlüsselkombination 1><Schlüsselkombination 2>… | Das Bild <Strategieart> ändern: Selektion wird angezeigt. | Die Schlüsselkombinationen hängen von der ausgewählten Strategieart ab. |
| 5 | Auswahl eingeben | Um Ihre Datensätze anzugeben, geben Sie die folgenden Attribute ein, die basierend auf der ausgewählten Schlüsselkombination angezeigt werden, und wählen Sie Ausführen:Sendermaterial:<ID des Sendermaterials><Schlüsselfeld>: <Schlüsselwert>… | Das Bild <Strategieart> ändern: Schnellerfassung wird angezeigt. |  |
| 6 | Strategiesatz eingeben | Um einen neuen Datensatz anzulegen, geben Sie folgende Daten ein, und wählen Sie Sichern:Sendermaterial: <ID des Sendermaterials>Um die Details für das Sendermaterial weiter zu pflegen, markieren Sie einen Datensatz, und wählen Sie Details. | Das Bild <Strategieart> ändern: Details wird angezeigt. |  |
| 7 | Details zum Strategiesatz pflegen | Geben Sie im Abschnitt Gesendete Attribute (Felder/Merkmale) folgende Daten ein, und wählen Sie Sichern:Attribut: <ID des Sendermaterials>Feld: <Standardmäßig ausgewählt>Merkmal: <Standardmäßig nicht ausgewählt> |  |  |

### Ableitungsstrategie für Empfängermaterial anlegen

Testverwaltung

Kundenprojekt: Füllen Sie die projektbezogenen Teile aus.

|  |  |  |  |
| --- | --- | --- | --- |
| Testfall-ID | <X.XX> | Testdatum: |  |
| Testername: |  | Dauer: |  |
| Benutzerrolle(n): |  | Zuständigkeit: | <Geben Sie den Serviceanbieter, einen Kunden oder einen Serviceanbieter zusammen mit einem Kunden an.> |

Zweck

Die folgende Vorgehensweise enthält Anweisungen zum Anlegen von Strategiesätzen, die zur Ermittlung von Attributen für das Empfängermaterial während der Chargenableitung verwendet werden.

Vorgehensweise

| Testschrittnummer | Bezeichnung des Testschritts | Anweisung | Erwartetes Ergebnis | Kommentare |
| --- | --- | --- | --- | --- |
| 1 | Anmelden | Melden Sie sich am SAP Fiori Launchpad als Stammdatenexperte – Chargendaten an. | Das SAP Fiori Launchpad wird angezeigt. |  |
| 2 | SAP-Fiori-App aufrufen | Öffnen Sie Ableitungsstrategien verwalten - Empfänger(DVR2). | Das Bild Ableitung - Suchstrategie ändern: Einstieg wird angezeigt. |  |
| 3 | Strategieart eingeben | Geben Sie folgende Daten ein, und wählen Sie Ändern:Strategieart: <Strategieart>: | Das Dialogfenster Schlüsselkombination wird angezeigt. | Vor diesem Schritt müssen Sie die folgenden Konfigurationsschritte Ihren Anforderungen entsprechend abschließen:Nummernkreise für die Ableitung von ChargenEmpfangende Chargen in der Chargenableitung ermitteln |
| 4 | Schlüsselkombination auswählen | Wählen Sie im Dialogfenster Schlüsselkombination eine der folgenden Optionen aus, und wählen Sie Auswählen:<Schlüsselkombination 1><Schlüsselkombination 2>… | Das Bild <Strategieart> ändern: Selektion wird angezeigt. | Die Schlüsselkombinationen hängen von der ausgewählten Strategieart ab. |
| 5 | Auswahl eingeben | Um Ihre Datensätze anzugeben, geben Sie die folgenden Attribute ein, die basierend auf der ausgewählten Schlüsselkombination angezeigt werden, und wählen Sie Ausführen:Empfängermaterial: <ID des Empfängermaterials><Schlüsselfeld>: <Schlüsselwert>… | Das Bild <Strategieart> ändern: Schnellerfassung wird angezeigt. |  |
| 6 | Strategiesatz eingeben | Um einen neuen Datensatz anzulegen, geben Sie folgende Daten ein, und wählen Sie Sichern:Empfängermaterial: <ID des Empfängermaterials>Um die Details für das Empfängermaterial weiter zu pflegen, markieren Sie einen Datensatz, und wählen Sie Details. | Das Bild <Strategieart> ändern: Details wird angezeigt. |  |
| 7 | Details zum Strategiesatz pflegen | Geben Sie auf der Registerkarte Attribute im Abschnitt Empfangene Attribute (Felder/Merkmale) die folgenden Daten ein, und wählen Sie Sichern:Attribut: <ID des Empfängermaterials>Feld: <Standardmäßig ausgewählt>Merkmal: <Standardmäßig nicht ausgewählt>Um die Regeln für jedes Attribut zu pflegen, wählen Sie ein Attribut aus, und wählen Sie die Registerkarte Regeln. Anschließend können Sie die folgenden Regeln pflegen:Regeln zur Steuerung der AbleitungSenderfeld leerEmpf. überschreib.Stufen im ChargenverwendungsnachweisEmpfänger sendet nichtRegeln zur Wertauswahl bei mehreren SendernVergleichendBooleschMehrwertige Merkmale |  |  |

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
- related-to :: [[11-inventory-warehouse-and-transportation/master-data-script-create-batch-management-master-data-mds-2zw-299]]
- related-to :: [[11-inventory-warehouse-and-transportation/mds-2zw-301]]
- related-to :: [[11-inventory-warehouse-and-transportation/mds-2zw-303]]
- related-to :: [[11-inventory-warehouse-and-transportation/script-de-dados-mestre-criar-dados-mestre-de-administracao-de-lotes-2z]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/2ZW_S4CLD2608_Master_Data_DE_XX.docx` — full document · extracted with `mammoth` · 29,623 chars in the whole document
