---
id: 01-solution-foundation-and-platform/test-script-sap-enable-now-integration-3n5-962
title: "Test Script: SAP Enable Now Integration (3N5) (3N5_S4CLD2608_BPD_EN_XX)"
description: "SAP S/4HANA Cloud Public Edition test script for SAP Enable Now integration: customizing, adding, publishing and reverting Web Assistant user assistance content."
cluster: 01-solution-foundation-and-platform
tags: [kb/solution-foundation-and-platform, topic/in-app-user-assistance]
aliases: [3N5_S4CLD2608_BPD_EN_XX]
keywords: [In-App User Assistance (SAP Enable Now and WalkMe), sap enable now, web assistant, user assistance content, customizing help content, custom help tiles, reverting customizations, publishing help, enable now author roles, business roles]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/3N5_S4CLD2608_BPD_EN_XX.docx]
confidence: high
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-962
topic: 01-solution-foundation-and-platform/in-app-user-assistance
language: EN
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Test Script: SAP Enable Now Integration (3N5) (3N5_S4CLD2608_BPD_EN_XX)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/3N5_S4CLD2608_BPD_EN_XX.docx`, extracted with `mammoth`. Grouped under **In-App User Assistance (SAP Enable Now and WalkMe)** in Solution Foundation and Platform. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

| <!-- image omitted: unnamed --> | Test ScriptSAP S/4HANA Cloud Public Edition - 19-06-26 |
| --- | --- |
|  | SAP Enable Now Integration (3N5) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Table of Contents

[1 Purpose 2](#_Toc232833319)

[2 Prerequisites 3](#_Toc232833320)

[2.1 System Access 3](#_Toc232833321)

[2.2 Roles 3](#_Toc232833322)

[2.2.1 SAP Enable Now Account 3](#_Toc232833323)

[2.2.2 SAP S/4HANA Cloud Public Edition Roles 4](#_Toc232833324)

[2.3 Additional Manual Configuration 4](#_Toc232833325)

[3 Overview Table 5](#_Toc232833326)

[4 Test Procedures 6](#_Toc232833327)

[4.1 Customize and Add Standard Assistant Content for SAP S/4HANA in Web Assistant 6](#_Toc232833328)

[4.1.1 Customize Standard User Assistant Content 6](#_Toc232833329)

[4.1.2 Add Custom User Assistant Content 12](#_Toc232833330)

[4.2 Test Display of Customized User Assistant Content 14](#_Toc232833331)

[4.3 Revert Customized User Assistant Content to Original 15](#_Toc232833332)

## Purpose

Overview

This scope item allows the integration of the SAP Enable Now product to customize and enrich the Web Assistant – the context sensitive in-app end-user documentation. The integration allows you to customize SAP existing in-app standard content. Additionally, for Apps using the Web Assistant you can create your own guided tours and context help for specific application functions.

In addition, a what’s new mode can inform the user about the latest changes within the product pro-actively. Furthermore, any SAP Enable output – such as interactive simulations, courses, documentation, or videos – can be easily embedded into the Web Assistant.

This document provides a detailed procedure for testing this scope item after solution activation, reflecting the predefined scope of the solution. Each process step, report, or item is covered in its own section, providing the system interactions (test steps) in a table view. Steps that are not in scope of the process but are needed for testing are marked accordingly. Project-specific steps must be added.

|  |
| --- |
| Note Values in this test script (decimal notation, date formats, and so on) are presented in U.S. standard notation. If your test system is set up to use a different notation, enter values as appropriate. |

## Prerequisites

This section summarizes all prerequisites to conducting the test in terms of systems, users, master data, organizational data, other test data and business conditions.

- Access to the SAP S/4HANA Cloud Public Edition system
- The content author user is created with corresponding role and permissions on the Enable Now content server.

### System Access

| System | Details |
| --- | --- |
| System | Accessible via SAP Fiori launchpad. Your system administrator provides you with the URL to access the various apps assigned to your role.https://my301430.s4hana.ondemand.com/ui?edithelp=true#Shell-home.Note This is a sample URL. Use the URL to your Fiori launchpad instead. |
| SAP Enable Now account | Use the SAP Enable Now Manager for storing test content:https://education3.hana.ondemand.com/education3Note This is a sample URL. Link to your own SAP Enable Now Manager instance instead. |

### Roles

#### SAP Enable Now Account

Use

The SAP Enable Now Integration for SAP S/4HANA Cloud Public Edition requires an account on the SAP Enable Now Manager to create, edit, and store SAP Enable Now content.

Procedure

1. Log on to your SAP Enable Now Manager, so that your user account can be created.
2. Afterwards, contact your project manager and ask for your user to be provided with the required Standard Author or Master Author role and with editing permissions for the content work area.

#### SAP S/4HANA Cloud Public Edition Roles

In the context of this test script, the SAP S/4HANA Cloud Public Edition roles are used to access the user assistant content of those SAP Fiori apps for which you want to modify or enhance the documentation with help of the SAP Enable Now Manager.

SAP delivers several business roles as templates, which you can use as a starting point to create your own roles. See also [Maintain Business Roles](https://help.sap.com/viewer/f544846954f24b9183eddadcc41bdc3b/Latest/en-US/8980ad05330b4585ab96a8e09cef4688.html).

Hence, you should select a business role that fits to the application context for which you want to enhance the user documentation.

An example would be the role shown below. Assign this to your individual test user to access the related Fiori app documentation.

| Name (Role Template) | ID (Role Template) | Name (Launchpad Space) | ID (Launchpad Space) | Log On |
| --- | --- | --- | --- | --- |
| Internal Sales Representative | SAP_BR_INTERNAL_SALES_REP | Internal Sales / Customer Returns / Billing | SAP_BR_INTERNAL_SALES_REP / SAP_SD_SPT_RETURNS_INT_SALES_PC / SAP_SD_SPT_BILLING_INT_SALES_PC |  |

### Additional Manual Configuration

Before you can test this scope item, you must have completed the additional configuration steps that are described in the Set-Up Instructions for this scope item. These configuration steps are specific for your implementation and include mandatory settings that are not delivered by SAP and must be created by you. For more information, follow the link to the document:

[Link to Set-Up Instructions](https://help.sap.com/docs/SAP_S4HANA_BEST_PRACTICES/f1764e96e7ada98f9ffaca39450915a6)

## Overview Table

This scope item consists of the following item provided in the table below:

|  |
| --- |
| Note If your system administrator has enabled spaces and pages on the SAP Fiori launchpad, the homepage will only contain the essential apps for performing the typical tasks of a business role.You can find all other (searchable) apps not included on the homepage using the search bar ([2434549](https://me.sap.com/notes/2434549)).If you want to personalize the homepage and include the hidden apps, navigate to your user profile and choose App Finder. |

| Item | Business Role | App/Transaction | Expected Results |
| --- | --- | --- | --- |
| Customize, create, or delete user assistance content for SAP S/4HANA Cloud Public Edition in Web Assistant UI | SAP_BR_INTERNAL_SALES_REPInternal Sales Representative | Launchpad | user assistance content has changed or new content is visible in SAP S/4HANA Cloud Public Edition. |

## Test Procedures

This section describes test procedures for each process step that belongs to this scope item.

### Customize and Add Standard Assistant Content for SAP S/4HANA in Web Assistant

|  |  |  |
| --- | --- | --- |
|  | Test Step | Description |
| 1 | Customize standard user assistant content | Customize standard user assistant content that is provided for SAP S/4HANA. |
| 2 | Add custom user assistant content | Create additional custom user assistant content. |

#### Customize Standard User Assistant Content

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

Customize standard user assistant content that is provided for SAP S/4HANA Cloud Public Edition.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad in author mode:https://my301430.s4hana.ondemand.com/ui?edithelp=true#Shell-homeNote This is a sample URL. Use the URL to your Fiori launchpad instead | The SAP Fiori launchpad is displayed.Open Help button is displayed<!-- image omitted: unnamed --> |  |
| 2 | Open Help | Open the SAP Fiori launchpad and choose Open Help. | The user assistant carousel and help content is displayed.<!-- image omitted: unnamed --> |  |
| 3 | Start Editing Mode | Choose Enter / Leave Edit Mode in the carousel.<!-- image omitted: unnamed --> | The carousel will change into edit mode.The Edit button is shown in green <!-- image omitted: unnamed -->and the Published indicator is shown above the carousel.<!-- image omitted: unnamed --> |  |
| 4 | Assign Hotspot | Select a tile in the carousel. | <!-- image omitted: unnamed -->The edit menu is shown above the tile. |  |
| 5 |  | Choose Assign Hotspot. | The carousel is hidden. A cross cursor is displayed. |  |
| 6 |  | Select a tile on the Launchpad to assign the hotspot. | When the mouse is moved over the screen, green or orange highlights indicate stable or instable elements.<!-- image omitted: unnamed -->With a click of the mouse, the hotspot is displayed at that position and the Edit Content popup opens.The Save Changes and Discard Changes buttons are displayed in the carousel.<!-- image omitted: unnamed --> |  |
| 7 | Change Hotspot | Move the slider to select a different hotspot size. | The size of the hotspot icon on the screen is adjusted to the current selection. |  |
| 8 |  | Choose the Tile tab.<!-- image omitted: unnamed --> | Tile parameters: title, summary and sequence are displayed. |  |
| 9 |  | Enter a different title. | The tile title in the carousel is updated accordingly. |  |
| 10 |  | Choose Apply. | The Edit Content popup is closed.<!-- image omitted: unnamed -->The customized tile is highlighted with a green line along the top of the tile in the carousel. |  |
| 11 | Save | Choose Save Changes.<!-- image omitted: unnamed --> | A Save successful message is shown at the top of the screen.<!-- image omitted: unnamed -->The Save Changes and Discard Changes buttons are no longer displayed in the carousel.The published state icon changes to Not published.<!-- image omitted: unnamed --> |  |
| 12 | Revert Change | In the carousel, select another tile that is not highlighted as customized (that is, has no green border at the top) | The edit menu is shown above the tile. |  |
| 13 |  | Choose Edit. | The Edit Content popup opens. |  |
| 14 |  | Change any parameter, for example, enter a new title on the Tile tab or change Size on the hotspot tab. Choose Apply. | The Save Changes and Discard Changes buttons are displayed in the carousel.The Edit Content popup is closed.The customized tile is highlighted with a green line along the top of the tile in the carousel. |  |
| 15 |  | Select the tile again and choose Revert to Original. | The tile and the hotspot are displayed in their original state.The tile is no longer highlighted as customized - the green border along the top of the tile is removed. |  |
| 16 |  | Choose Save Changes . | A Save successful message is shown at the top of the screen.The Save Changes and Discard Changes buttons are no longer displayed in the carousel. |  |
| 17 | Publish Changes | Choose Show/Hide Options. | The options dropdown is displayed.<!-- image omitted: unnamed --> |  |
| 18 |  | Choose Publish Help. | The Publish Help message box is displayed.<!-- image omitted: unnamed --> |  |
| 19 |  | Choose Yes. | A published successfully message is shown at the top of the screenThe published state icon changes to Published. |  |

#### Add Custom User Assistant Content

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

Create additional custom user assistant content.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Add Help Topic | Choose Add Help Topic (+) | **<!-- image omitted: unnamed -->**The add help topic dropdown is displayed. |  |
| 2 |  | Choose Add Help Tile | The Edit Content popup opens on the Tile tab.The carousel is scrolled and the new tile is added behind the last existing help tile.The Save Changes and Discard Changes buttons are displayed in the carousel. |  |
| 3 | Edit Help Tile Values | Enter a title text | The tile title is updated in the carousel. |  |
| 4 |  | Enter a summary text | The summary text is updated in the carousel. |  |
| 5 | Enter Text | Choose the Text tab<!-- image omitted: unnamed --> | The text tab is displayed with HTML editor. |  |
| 6 |  | Enter text in the editor |  |  |
| 7 | Change Bubble Size | Choose the Bubble tab | The Bubble tab is displayed. |  |
| 8 |  | Move the Size slider control | The bubble size is displayed (value range XS - XL) |  |
| 9 | Apply Changes | Choose Apply | The Edit Content popup is closed.The new tile is shown in the carousel with a green line along the top. |  |
| 10 |  | Choose Save | A message is shown at the top of the screen, telling you the save has been successful.The Save and Discard buttons are no longer displayed in the carousel.The published state icon changes to Not published. |  |
| 11 | Publish Changes | Choose Show/Hide Options | The options dropdown is displayed. |  |
| 12 |  | Choose Publish Help | The Publish Help message box is displayed. |  |
| 13 |  | Choose Yes | A published successfully message is shown at the top of the screenThe published state icon changes to Published. |  |
| 14 | Close Help | Choose Open Help | User assistant help is closed. |  |

### Test Display of Customized User Assistant Content

|  |  |  |
| --- | --- | --- |
|  | Test Step | Description |
| 1 | Test display of customized user assistant content | Open helP from end-user perspective to see that all changes are visible |

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

Open help from end-user perspective to see that all changes are visible.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad in end-user mode (that is, no Edit option):https://my301430.s4hana.ondemand.com/ui#Shell-homeNote This is a sample URL. Use the URL to your Fiori launchpad instead | The SAP Fiori launchpad is displayed.The Open Help button is displayed. |  |
| 2 |  | Choose Open Help. | The user assistant carousel and help content is displayed. |  |
| 3 | Display Customized Help Content | Choose a tile in the carousel that is highlighted as customized (that is, has a green line along the top ofthe tile) | The Help bubble is displayed.The tile is highlighted in the carousel. |  |
| 4 |  | Choose Close. | The Help bubble is closed.The tile is not highlighted in the carousel. |  |

### Revert Customized User Assistant Content to Original

|  |  |  |
| --- | --- | --- |
|  | Test Step | Description |
| 1 | Revert customized user assistant help to original | Revert all customization to display the original user assistant content again. |

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

Revert all customization to display the original user assistant content again.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad in author mode:https://my301430.s4hana.ondemand.com/ui?edithelp=true#Shell-homeNote This is a sample URL. Use the URL to your Fiori launchpad instead | The SAP Fiori launchpad is displayed.The Open Help button is displayed. |  |
| 2 |  | Choose Open Help. | The user assistant carousel and help content are displayed. |  |
| 3 | Start Editing | Choose Enter / Leave Edit Mode in the carousel. |  |  |
| 4 | Revert all to Original | Choose Show/Hide Options . | The carousel will change into edit mode.The Edit button is shown in green , an indicator for the published state is shown above the carousel. |  |
| 5 |  | Choose Revert all to Original. | The user assistant help content and carouselare displayed in their original state. All customization is removed, for example, green highlights along the top of the tiles in the carousel.The published state icon changes to Not published. |  |
| 6 | Publish Help | Choose Show/Hide Options. | The options dropdown is displayed. |  |
| 7 |  | Choose Publish Help. | The Publish Help message box is displayed. |  |
| 8 |  | Choose Yes. | A published successfully message is shown at the top of the screenThe published state icon changes to Published. |  |
| 9 |  | Choose Close. | The Help bubble is closed.The tile is not highlighted in the carousel. |  |
| 10 | Close Help | Choose Open Help. | User assistant help is closed. |  |

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
- related-to :: [[01-solution-foundation-and-platform/walkme-premium-integration-7te-test-script-1226]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/3N5_S4CLD2608_BPD_EN_XX.docx` — full document · extracted with `mammoth` · 19,690 chars in the whole document
