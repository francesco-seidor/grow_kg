---
id: 16-two-tier-erp-and-central-finance/two-tier-erp-integration-setup-document-230
title: Two-Tier ERP Integration Setup Document (S4CLD2608_2T_Int_Setup_Guide_EN)
description: "Customer guide for configuring integration between SAP ECC / on-premise S/4HANA and S/4HANA Cloud Public Edition via SAP Cloud Integration, inbound and outbound IDoc scenarios."
cluster: 16-two-tier-erp-and-central-finance
tags: [kb/two-tier-erp-and-central-finance, topic/two-tier-integration-setup]
aliases: [S4CLD2608_2T_Int_Setup_Guide_EN]
keywords: [Two-Tier ERP Integration Setup, two-tier erp integration, inbound integration, outbound integration, idoc configuration, sap cloud integration, cloud connector, communication management, certificate trust list, business roles]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/General/Two-Tier_ERP_Assets_User_Guides/Two-Tier_ERP_Assets_User_Guides/Integration/S4CLD2608_2T_Int_Setup_Guide_EN.docx]
confidence: low
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-230
topic: 16-two-tier-erp-and-central-finance/two-tier-integration-setup
language: ""
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Two-Tier ERP Integration Setup Document (S4CLD2608_2T_Int_Setup_Guide_EN)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/General/Two-Tier_ERP_Assets_User_Guides/Two-Tier_ERP_Assets_User_Guides/Integration/S4CLD2608_2T_Int_Setup_Guide_EN.docx`, extracted with `mammoth`. Grouped under **Two-Tier ERP Integration Setup** in Two-Tier ERP and Central Finance. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

|  |  |
| --- | --- |
| SAP Cloud ERP June 2026English |  |
|  | Two-Tier ERP Integration Setup Document |
| SAP SE Dietmar-Hopp-Allee 16 69190 Walldorf Germany | Customer Guide |

Copyright

© 2020 SAP SE or an SAP affiliate company. All rights reserved.

No part of this publication may be reproduced or transmitted in any form or for any purpose without the express permission of SAP SE. The information contained herein may be changed without prior notice.

Some software products marketed by SAP SE and its distributors contain proprietary software components of other software vendors.

National product specifications may vary.

These materials are provided by SAP SE and its affiliated companies ("SAP Group") for informational purposes only, without representation or warranty of any kind, and SAP Group shall not be liable for errors or omissions with respect to the materials. The only warranties for SAP Group products and services are those that are set forth in the express warranty statements accompanying such products and services, if any. Nothing herein should be construed as constituting an additional warranty.

SAP and other SAP products and services mentioned herein as well as their respective logos are trademarks or registered trademarks of SAP SE in Germany and other countries. Please see http://www.sap.com/corporate-en/legal/copyright/index.epx#trademark for additional trademark information and notices.

| Revision | Change Date | Description |
| --- | --- | --- |
| 1 | 29.05.2018 | Detailed steps for Inbound & Outbound scenarios |
| 2 | 31.03.2021 | Final Version |

Icons

| Icon | Meaning |
| --- | --- |
| <!-- image omitted: unnamed --> | Caution |
| <!-- image omitted: unnamed --> | Example |
| <!-- image omitted: unnamed --> | Note |
| <!-- image omitted: unnamed --> | Recommendation |
| <!-- image omitted: unnamed --> | Syntax |

Typographic Conventions

| Type Style | Description |
| --- | --- |
| Example text | Words or characters that appear on the screen. These include field names, screen titles, pushbuttons as well as menu names, paths and options.Cross-references to other documentation. |
| Example text | Emphasized words or phrases in body text, titles of graphics and tables. |
| EXAMPLE TEXT | Names of elements in the system. These include report names, program names, transaction codes, table names, and individual key words of a programming language, when surrounded by body text, for example, SELECT and INCLUDE. |
| Example text | Screen output. This includes file and directory names and their paths, messages, source code, names of variables and parameters as well as names of installation, upgrade and database tools. |
| EXAMPLE TEXT | Keys on the keyboard, for example, function keys (such as F2) or the ENTER key. |
| Example text | Exact user entry. These are words or characters that you enter in the system exactly as they appear in the documentation. |
| <Example text> | Variable user entry. Pointed brackets indicate that you replace these words and characters with appropriate entries. |

Content

[1 Purpose 6](#_Toc515545961)

[2 Business Requirements 6](#_Toc515545962)

[3 Technical Details 6](#_Toc515545963)

[3.1 Configurations for S4HANA Cloud - Inbound Scenarios 6](#_Toc515545964)

[3.2 Configurations for S4HANA Cloud - Outbound Scenarios 11](#_Toc515545965)

[4 Test Script 18](#_Toc515545966)

[4.1 Purpose 18](#_Toc515545967)

[4.2 Prerequisites 18](#_Toc515545968)

[4.3 System Access 18](#_Toc515545969)

[4.4 Roles 18](#_Toc515545970)

[4.5 Master Data, Organizational Data and Other Data 18](#_Toc515545971)

[4.6 Overview Table 18](#_Toc515545972)

[4.7 Test Procedure 19](#_Toc515545973)

## Purpose

This document provides the configuration required for Integrating S4HOn-Premise / ECC with S4H Cloud using SAP Cloud Integration (CI).

## Business Requirements

In a 2-tier model, SAP Cloud ERP and SAP Cloud ERP Private systems can support the organization and subsidiaries to run in an independent yet integrated fashion.

Basic Configuration is required in ECC & S/4HANA Cloud Public Edition for integrating these 2 systems for sending or receiving data

## Technical Details

The main steps in the scenario:

1. Configurations in On-Premise ECC

2. Configuration in S/4 HANA Cloud Public Edition

### Configurations for S/4HANA Cloud - Inbound Scenarios

The following list of prerequisite configurations are to be in place to realize the integration process from SAP ECC (on premise) to S/4HANA Cloud Public Edition using SAP CI (Cloud Integration) as middleware.

***Configuration in SAP Cloud ERP Private/ ECC***

1. Create a RFC Destination in SM59. Provide the Cloud Integration URL and Login details. Import Cloud Integration Certificate using “STRUST” and assign the certificate to RFC destination in “Logon & Security --à Security options” (Figure1)

<!-- image omitted: unnamed -->

Figure.1

1. Assign RFC Destination to Port (WE21) as XML HTTP Port (Figure2)

<!-- image omitted: unnamed -->

Figure.2

1. Create Partner profile in WE20 (Type LS). Assign the outbound message type with receiver port details as shown below in Figure 3

<!-- image omitted: unnamed -->

Figure.3

4.Maintain the Distribution Model in BD64 as shown below Figure 4

<!-- image omitted: unnamed -->

Figure.4

***Configuration in S4 HANA Cloud*:**

The incoming IDOC (SALESORDER_CREATEFROMDAT202 / SALESORDER_CREATEFROMDAT2) needs to be processed and converted to a Sales Order. We need to maintain the following configurations.

1. Maintain Communication User. Communication user defined in the SAP Cloud ERP system is used for inbound communication and processing messages in the system.

Procedure: (Figure 5)
 a) Access the SAP Cloud ERP system and log on as an Administrator.
 b) Choose the Maintain Communication Users tile from Communication Management.
 c) In the next window, choose New.
 d) Enter User Name and Description.
 e) Enter a password & Choose Create.Save the changes

<!-- image omitted: unnamed -->

Figure.5

1. Maintain Communication System.(Figure 6) The Communication system defined in the SAP Cloud ERP system is used as source or target system.

<!-- image omitted: unnamed -->

Figure.6

1. Maintain Communication Arrangements: (Figure 7) The Communication Arrangements defined in the SAP Cloud ERP systems enables key users to create and edit communication arrangements that your company has set up with a communication partner.

Maintain Communication Arrangements for the required Scenario ID

Ex : SAP_COM_0008

<!-- image omitted: unnamed -->

Figure.7

### Configurations for S4HANA Cloud - Outbound Scenarios

The following list of prerequisite configurations are to be in place to realize the outbound integration process from S4HANA Cloud to SAP ECC (on premise) using SAP CI (Cloud Integration) as middleware.

***Configuration in SAP S4HANA Cloud Public Edition***

1. Maintain Certificate Trust List (Figure 8)

The communication between S/4HANA Cloud Public Edition and SAP Cloud Integration requires the CI certificates to be stored in certificate trust list.

Open the Maintain Certificate Trust List App in S/4HANA Cloud Public Edition and maintain.

<!-- image omitted: unnamed -->

Figure.8

1. Open Communication Management Tile à Communication Systems and maintain the System Info and User Credentials as shown in Figure.9

<!-- image omitted: unnamed -->

<!-- image omitted: unnamed -->

Figure.9

1. Open Communication Management Tile à Communication Arrangements (Figure.10)

<!-- image omitted: unnamed -->

Figure.10

1. Search for the Communication scenario ID (Figure.11)

<!-- image omitted: unnamed -->

Figure.11

1. Maintain the outbound service URL path (taken from CI SOAP sender adapter) as shown in Figure.12

<!-- image omitted: unnamed -->

Figure.12

**Note:** The Path should have “*/cxf“* prefixed to the IDoc sender adapter URL (figure. 13)

CI Sender SOAP Adapter:

<!-- image omitted: unnamed -->

1. CI receiver IDoc Adapter setup for On-premise ERP (ECC)

The cloud connector is used for sending IDocs from Cloud Integration to on premise ECC system. The CI IDoc adapter to be maintained with the virtual hostname and port maintained in the Cloud Connector tool. The proxy type should be selected as “On-Premise” as shown in Figure.13

<!-- image omitted: unnamed -->

Figure.13

***Configuration in Cloud Connector:***

Data Transfer from S/4 HANA Cloud Public Edition to On-Premise system requires SAP Cloud Connector. For more details on how to install & setup, please go through the official documentation.

[https://help.sap.com/docs/CP_CONNECTIVITY/cca91383641e40ffbe03bdc78f00f681/e6c7616abb5710148cfcf3e75d96d596.html?version=Cloud&locale=en-US](https://help.sap.com/docs/CP_CONNECTIVITY/cca91383641e40ffbe03bdc78f00f681/e6c7616abb5710148cfcf3e75d96d596.html?version=Cloud&locale=en-US)

Cloud Connector Setup:

The following list of prerequisite configurations are to be in place as shown in Figure.14 & 15.

- Cloud Connector Installation and Sub Account registration
- Setup On premise hostname to Virtual hostname map on the cloud connector

<!-- image omitted: unnamed -->

Figure.14

<!-- image omitted: unnamed -->

Figure.15

- If the internal host has an http redirection in place, maintain the mapping as follows

<!-- image omitted: unnamed -->

Figure.16

***Configuration in SAP ERP (on premise)***

1. Setup/Activate the IDoc service in SICF transaction (Figure.16)

<!-- image omitted: unnamed -->

<!-- image omitted: unnamed -->

<!-- image omitted: unnamed -->

Figure.17

1. Maintain Partner profile entries for IDoc (Figure.18)

<!-- image omitted: unnamed -->

<!-- image omitted: unnamed -->

Figure.18

## Test Script

### Purpose

Not Applicable for System Configuration

### Prerequisites

Not Applicable for System Configuration

### System Access

The test is conducted in the following systems:

| System | Details |
| --- | --- |
| System | Access using the SAP Fiori® Launchpad. Your system administrator provides you with the URL to access the various apps assigned to your role. |

### Roles

Assign the following business roles to your individual test users.

Note The following roles are provided as example roles from SAP. You can use these as templates for your own roles.

| Business Role | Business Role ID as Delivered by SAP | Log On |
| --- | --- | --- |
| Admin | ADMINISTRATOR |  |

### Master Data, Organizational Data and Other Data

Not Applicable for System Configuration

### Overview Table

| Process Step | Business Role | Transaction/App | Expected Results |
| --- | --- | --- | --- |
| Maintain Configurations in SAP ECC | Admin | WE20, WE21,SM59,BD64 | ECC system integrated with Target System |
| Maintain Configurations in S/4 HANA Cloud | administrator | App | S/4 HC connected to ECC. |

### Test Procedure

This section describes test procedures for each process step that belongs to this scope item.

| Test Step # | Test Step Name | Instruction | Expected Result |
| --- | --- | --- | --- |
| 1 | NA |  |  |
| 2 |  |  |  |
| 3 |  |  |  |

## Suspected conflicts

> [!warning] Conflict
> Flagged while digesting this document, not verified: Cover says SAP Cloud ERP June 2026 but the last revision is dated 31.03.2021 and the copyright 2020, so content may be outdated relative to release 2608.

## Connections
- part-of :: [[_cluster]]
- see-also :: [[01-solution-foundation-and-platform/edi-extensibility-customer-guide-229]]
- see-also :: [[16-two-tier-erp-and-central-finance/two-tier-master-data-replication-business-partner-master-customer-233]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/General/Two-Tier_ERP_Assets_User_Guides/Two-Tier_ERP_Assets_User_Guides/Integration/S4CLD2608_2T_Int_Setup_Guide_EN.docx` — full document · extracted with `mammoth` · 11,062 chars in the whole document
