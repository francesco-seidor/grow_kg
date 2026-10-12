---
id: 01-solution-foundation-and-platform/test-script-key-risk-indicator-monitoring-with-sap-risk-management-2u2
title: "Test Script: Key Risk Indicator Monitoring with SAP Risk Management (2U2) (2U2_S4CLD2608_BPD_EN_XX)"
description: "SAP S/4HANA Cloud Public Edition test script for 2U2: creating KRI templates, implementations and risks in on-premise SAP Risk Management and checking threshold violations."
cluster: 01-solution-foundation-and-platform
tags: [kb/solution-foundation-and-platform, topic/governance-risk-and-control-monitoring]
aliases: [2U2_S4CLD2608_BPD_EN_XX]
keywords: ["Risk, Control and Privacy Monitoring (SAP Risk and…", key risk indicators, sap risk management, kri templates, kri implementation, risks and opportunities, kri monitoring job, threshold violation, business roles, business conditions]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/2U2_S4CLD2608_BPD_EN_XX.docx]
confidence: high
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-867
topic: 01-solution-foundation-and-platform/governance-risk-and-control-monitoring
language: EN
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Test Script: Key Risk Indicator Monitoring with SAP Risk Management (2U2) (2U2_S4CLD2608_BPD_EN_XX)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/2U2_S4CLD2608_BPD_EN_XX.docx`, extracted with `mammoth`. Grouped under **Risk, Control and Privacy Monitoring (SAP Risk and Assurance Management)** in Solution Foundation and Platform. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

| <!-- image omitted: unnamed --> | Test ScriptSAP S/4HANA Cloud Public Edition - 19-06-26 |
| --- | --- |
|  | Key Risk Indicator Monitoring with SAP Risk Management (2U2) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Table of Contents

[1 Purpose 2](#_Toc232840313)

[2 Prerequisites 3](#_Toc232840314)

[2.1 Additional Manual Configuration 3](#_Toc232840315)

[2.2 System Access 3](#_Toc232840316)

[2.3 Roles 3](#_Toc232840317)

[2.4 Business Conditions 4](#_Toc232840318)

[3 Overview Table 5](#_Toc232840319)

[4 Test Procedures 6](#_Toc232840320)

[4.1 Create KRI Templates 6](#_Toc232840321)

[4.2 Create KRI Implementation 7](#_Toc232840322)

[4.2.1 Option One: Create KRI Implementation with Scripts for SAP Table 7](#_Toc232840323)

[4.2.2 Option Two: Create KRI Implementation with Scripts for OData Service 8](#_Toc232840324)

[4.3 Create Risk and Opportunities 10](#_Toc232840325)

[4.4 Trigger KRI Monitoring Job 12](#_Toc232840326)

[4.5 Check Threshold Violation 13](#_Toc232840327)

## Purpose

Overview

You can integrate SAP Risk Management on premise with SAP S/4HANA Cloud Public Edition to support a unified view of risk across the enterprise. This scope item enables communication between the applications so that SAP Risk Management can monitor risk indicators in SAP S/4HANA Cloud Public Edition.

This document provides a detailed procedure for testing this scope item after solution activation, reflecting the predefined scope of the solution. Each process step, report, or item is covered in its own section, providing the system interactions (test steps) in a table view. Steps that are not in scope of the process but are needed for testing are marked accordingly. Project-specific steps must be added.

|  |
| --- |
| Note Values in this test script (decimal notation, date formats, and so on) are presented in U.S. standard notation. If your test system is set up to use a different notation, enter values as appropriate. |

## Prerequisites

This section summarizes all the prerequisites for conducting the test in terms of systems, users, master data, organizational data, other test data and business conditions.

### Additional Manual Configuration

Before you can test this scope item, you must have completed the additional configuration steps that are described in the Set-Up Instructions for this scope item. These configuration steps are specific for your implementation and include mandatory settings that are not delivered by SAP and must be created by you. For more information, follow the link to the document:

[Link to Set-Up Instructions](https://help.sap.com/docs/SAP_S4HANA_BEST_PRACTICES/f3e62d02c8d80776c789b4c9f065428d)

### System Access

The test should be conducted with the following system:

| System | Details |
| --- | --- |
| SAP S/4HANA Cloud Public Edition System | Accessible via SAP Fiori launchpad. Your system administrator provides you with the URL to access the various apps assigned to your role. |
| SAP Risk Management System | Your system administrator provides you the logon information to access the system. |

### Roles

Create business roles using the following business role templates delivered by SAP and assign them to your individual test users.

Alternatively, if available, you can use the following spaces delivered by SAP. You create a space with pages containing predefined essential apps and assign it to the business role. You then assign this business role to your individual users.

For more information, refer to How to Create a Business Role from a Template in the [product assistance](https://help.sap.com/docs/SAP_S4HANA_CLOUD/53e36b5493804bcdb3f6f14de8b487dd/ec310a8b669a45ca898dc4dd91d97de2.html) for SAP S/4HANA Cloud Public Edition.

For more information on Roles in SAP Process Control, please refer to Security Guide in product page for [SAP Risk Management](https://help.sap.com/docs/SAP_RISK_MANAGEMENT?locale=en-US).

| Name (Role Template) | ID (Role Template) | Name (Launchpad Space) | ID (Launchpad Space) | Log On |
| --- | --- | --- | --- | --- |
| Central Risk Manager | SAP_GRC_RM_API_CENTRAL_RM | N/A | N/A | Please ask your system administrator to assign to the tester in SAP Risk Management. |
| Unit Risk Manager | SAP_GRC_RM_API_RISK_MANAGER | N/A | N/A | Please ask your system administrator to assign to the tester in SAP Risk Management. |
| Administrator | N/A | N/A | N/A | Pre-delivered role or role template is not provided. Please ask your system administrator to create corresponding role in SAP Risk Management. The role should have access to transaction SE38 and be assigned to the tester. |

### Business Conditions

Before this scope item can be tested, the following business conditions must be met.

| Scope Item | Business Condition |
| --- | --- |
| BD6 - Basic Credit Management | Make sure BD6 is activated before performing test procedures described in this test script, because customizing enabling Credit Limit contained in BD6 is required for successful execution of this test script. |

## Overview Table

This scope item consists of several process steps provided in the table below.

| Process Name | Business Role | System | App/Transaction | Expected Result |
| --- | --- | --- | --- | --- |
| [Create KRI Templates](#unique_8) [page ] 6 | Unit Risk Manager | On-premise SAP Risk Management System | /nnwbc | KRI Template is created. |
| [Option One: Create KRI Implementation with Scripts for SAP Table](#unique_9) [page ] 7 | Unit Risk Manager | On-premise SAP Risk Management System | /nnwbc | KRI Implementation is created. |
| [Option Two: Create KRI Implementation with Scripts for OData Service](#unique_10) [page ] 8 | Unit Risk Manager | On-premise SAP Risk Management System | /nnwbc | KRI Implementation is created. |
| [Create Risk and Opportunities](#unique_11) [page ] 10 | Central Risk Manager | On-premise SAP Risk Management System | /nnwbc | Risk is created. |
| [Trigger KRI Monitoring Job](#unique_12) [page ] 12 | System Administrator | On-premise SAP Risk Management System | /nse38 | KRI monitoring job is triggered. |
| [Check Threshold Violation](#unique_13) [page ] 13 | Central Risk Manager | On-premise SAP Risk Management System | /nnwbc | Threshold violation is reported and observed. |

## Test Procedures

This section describes test procedures for each process step that belongs to this scope item.

### Create KRI Templates

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

Predefined key risk indicators can be set up by creating KRI templates.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to a supported Web browser (such as Internet Explorer) with the following URL:http(s)://<ServerName>:<Port Number>/nwbc | The NetWeaver Business Client screen for SAP Risk Management is displayed. |  |
| 2 | Rule Setup | Choose the Rule Setup tab. |  |  |
| 3 | KRI Templates | In the Key Risk Indicators section, choose KRI Templates. | The KRI Template Catalog view is displayed. |  |
| 4 | KRI Templates | Choose Create. | A dialog box displays. |  |
| 5 | Enter Template Details | Make the following entries and choose Save:General tab:KRI Template Name: <For example, KRI Template Name>Description: <description>Value Type: Number | The KRI template is saved. |  |

### Create KRI Implementation

#### Option One: Create KRI Implementation with Scripts for SAP Table

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you create the actual application of a KRI template.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to a supported Web browser (such as Internet Explorer) with the following URL:http(s)://<ServerName>:<Port Number>/nwbc | The NetWeaver Business Client screen for SAP Risk Management is displayed. |  |
| 2 | Rule Setup | Choose the Rule Setup tab. |  |  |
| 3 | Navigate to KRI Implementation | In the Key Risk Indicators section, choose KRI Implementation. | The KRI Implementation Catalog dialog box is displayed. |  |
| 4 | Create | Choose Create. | A dialog box displays. |  |
| 5 | Create KRI Implementation | Make the following entries:General tab:KRI Implementation Name: <For example, Define Amount Limit>KRI Template: <For example, Define Amount Limit>Description: <For example, KRI Implementation for Define Amount Limit>Connector Type: SAP S/4 TableConnector: <For example, the ID of SAP S/4HANA Cloud Public Edition system>Note The Connector mentioned above is the one which is created after following the Set-up Instruction Guide of 2U2.Script: <Enter the script ID created after following through the Set-up Instruction Guide of 2U2>Note You can choose the Test Connector and Test Script buttons to verify whether the entered Connector and Script are working. |  |  |
| 6 | Implementation Detail | Choose the Implementation Detail tab. |  |  |
| 7 | Enter Data | Make the following entries and choose Save:Value Column: Credit Limit [CREDIT LIMIT]Aggregation Function: <For example, Maximum> | The KRI Implementation is saved. |  |

#### Option Two: Create KRI Implementation with Scripts for OData Service

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log onto On-Premise SAP Risk Management | Log on to a supported Web browser (such as Internet Explorer) with the following URL:http(s)://<ServerName>:<Port Number>/nwbc | The NetWeaver Business Client screen for SAP Risk Management is displayed. |  |
| 2 | Rule Setup | Choose the Rule Setup tab. |  |  |
| 3 | KRI Implementation | In the Key Risk Indicators section, choose KRI Implementation. | The Implementation Catalog view is displayed. |  |
| 4 | Navigate to KRI Implementation | Choose Create. | A dialog box displays. |  |
| 5 | Create KRI Implementation | Make the following entries:General tab:KRI Implementation Name: <For example, Purchase Requisition AmountKRI Template: <For example, Purchase Requisition AmountDescription: <For example, KRI Implementation for Purchase Requisition Amount>Connector Type: S/4 ODataConnector: <For example, the ID of SAP S/4HANA Cloud Public Edition system>Note The Connector mentioned above is the one that you created in the set-up instruction guide for 2U2 - Key Risk Indicator Monitoring with SAP Risk Management.Script: <script ID from the set-up instruction guide of 2U2>Note To verify that the connector and script are working, you can choose the Test Connector and Test Script buttons.Implementation Detail tab:Value Column: <Select the fields you want to monitor, for example, ItemNetAmount>Note When you connect the hierarchical CDS View OData Service script, all the fields in the hierarchical view are displayed in a flat list.Aggregation Function: <For example, Maximum>Note If OData Services with Input Parameters are used, maintain the Input Parameter section.Choose Save to save this KRI Implementation. |  |  |

### Create Risk and Opportunities

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you create a risk and a key risk indicator instance (with the created KRI implementation).

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to a supported Web browser (for example, Internet Explorer) with the following URL:http(s)://<ServerName>:<Port Number>/nwbc | The NetWeaver Business Client view for SAP Risk Management is displayed. |  |
| 2 | Assessments | Choose the Assessments tab. |  |  |
| 3 | Risk and Opportunities | In the Risk Assessments section, choose Risk and Opportunities. | The Risk Management and Opportunity Management view is displayed. |  |
| 4 | Operational Risk | Choose Create > Operational Risk . | A dialog box displays. |  |
| 5 | Create Risk | Make the following entries:General tab:Name: For example, Define Amount LimitOrganization Unit: <organizational unit>Risk Category: <risk category> |  |  |
| 6 | Key Risk Indicators | Choose the Key Risk Indicators tab. |  |  |
| 7 | Create Standard KRI | Choose Create > Standard KRI Instance . | A dialog box displays. |  |
| 8 | Enter Details | Make the following entries:KRI Instance Name: For example, Define Amount Limit KRIKRI Implementation: <KRI implementation (see Note below)>Note For the KRI Implementation field, if you performed [Option One: Create KRI Implementation with Scripts for SAP Table](#unique_9) [page ] 7, choose Define Amount Limit. If you performed [Option Two: Create KRI Implementation with Scripts for OData Service](#unique_10) [page ] 8, choose KRI Implementation for Purchase Requisition Amount.Description: <For example, KRI Instance for Defining Amount Limit>Monitor Frequency: <For example, Daily>Next Execution Date: <Adjust to current date>Data Time Frame: <For example, Year / [Current Year]>Note To verify the validity of your KRI instance, you can choose the Test Instance button.Note If you use OData Services with Input Parameters, maintain the Input Parameter section accordingly.Choose Activate to save this KRI instance. The dialog box closes automatically.Choose Submit to save this risk. | The Create Risk screen is displayed. |  |
| 9 | Key Risk Indicators | Open the created risk and choose the Key Risk Indicators tab. |  |  |
| 10 | Threshold Violation | Select the role representing the KRI instance created in the prior step and choose the button under the Threshold Violation column. | A dialog box displays. |  |
| 11 | Maintain KRI Value Thresholds | Make the following entries and choose Submit:Favorable Value Range: <For example, High Values>Value To: 1 (on the row for the Yellow threshold)Flag Risk: Selected (on the row for Red threshold) | Changes made to the Risk are saved. |  |

### Trigger KRI Monitoring Job

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you manually trigger the threshold violation monitoring job.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the on-premise SAP Risk Management system as a System Administrator. |  |  |
| 2 | Access Transaction | In the Command field, enter SE38 and press Enter. |  |  |
| 3 | Trigger Threshold Violation Monitoring Job | Make the following entries and choose Execute:Program: GRRM_KRI_RUNTIME | The program completed successfully without any error message. |  |

|  |
| --- |
| Note You can then assign created Business Rules to Controls and schedule the monitoring rule. |

### Check Threshold Violation

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you check and verify that the threshold violation is captured.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to a supported Web browser (such as Internet Explorer) with the following URL:http(s)://<ServerName>:<Port Number>/nwbc | The NetWeaver Business Client screen for SAP Risk Management is displayed. |  |
| 2 | Check Threshold Violation | Open the risk created in [Create Risk and Opportunities](#unique_11) [page ] 10, and choose the Key Risk Indicators tab. | A red light is shown under column Threshold Violation for the KRI instance defined in [Create Risk and Opportunities](#unique_11) [page ] 10. |  |

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
- related-to :: [[01-solution-foundation-and-platform/test-script-continuous-control-monitoring-with-sap-process-control-2oh]]
- related-to :: [[01-solution-foundation-and-platform/test-script-control-monitoring-with-sap-risk-and-assurance-management]]
- related-to :: [[01-solution-foundation-and-platform/test-script-privacy-risk-detection-with-sap-risk-and-assurance-managem]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/2U2_S4CLD2608_BPD_EN_XX.docx` — full document · extracted with `mammoth` · 19,822 chars in the whole document
