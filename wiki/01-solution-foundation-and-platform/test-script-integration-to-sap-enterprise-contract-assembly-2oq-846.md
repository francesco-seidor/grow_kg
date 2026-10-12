---
id: 01-solution-foundation-and-platform/test-script-integration-to-sap-enterprise-contract-assembly-2oq-846
title: "Test Script: Integration to SAP Enterprise Contract Assembly (2OQ) (2OQ_S4CLD2608_BPD_EN_XX)"
description: "SAP S/4HANA Cloud Public Edition test script for scope item 2OQ: ECA integration setup (areas, document variables) and creating/managing legal documents."
cluster: 01-solution-foundation-and-platform
tags: [kb/solution-foundation-and-platform, topic/enterprise-contract-assembly]
aliases: [2OQ_S4CLD2608_BPD_EN_XX]
keywords: [Enterprise Contract Assembly Integration, enterprise contract assembly, enterprise contract management, test script, define areas, document variables, create legal documents, manage legal documents, business roles, business conditions]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/2OQ_S4CLD2608_BPD_EN_XX.docx]
confidence: high
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-846
topic: 01-solution-foundation-and-platform/enterprise-contract-assembly
language: EN
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Test Script: Integration to SAP Enterprise Contract Assembly (2OQ) (2OQ_S4CLD2608_BPD_EN_XX)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/2OQ_S4CLD2608_BPD_EN_XX.docx`, extracted with `mammoth`. Grouped under **Enterprise Contract Assembly Integration** in Solution Foundation and Platform. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

| <!-- image omitted: unnamed --> | Test ScriptSAP S/4HANA Cloud Public Edition - 19-06-26 |
| --- | --- |
|  | Integration to SAP Enterprise Contract Assembly (2OQ) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Table of Contents

[1 Introduction 2](#_Toc232847991)

[2 Purpose 3](#_Toc232847992)

[3 Prerequisites 4](#_Toc232847993)

[3.1 System Access 4](#_Toc232847994)

[3.2 Roles 4](#_Toc232847995)

[3.3 Business Conditions 5](#_Toc232847996)

[3.4 Additional Manual Configuration 5](#_Toc232847997)

[3.5 Preliminary Steps 5](#_Toc232847998)

[3.5.1 Define Areas 5](#_Toc232847999)

[3.5.2 Define Document Variables (Optional) 7](#_Toc232848000)

[4 Overview Table 13](#_Toc232848001)

[5 Test Procedures 14](#_Toc232848002)

[5.1 Create Legal Documents 14](#_Toc232848003)

[5.2 Manage Legal Documents 15](#_Toc232848004)

## Introduction

Integration of SAP S/4HANA for Enterprise Contract Assembly with SAP S/4HANA for Enterprise Contract Management enables you to integrate into all core business processes, assemble all types of documents based on templates, text blocks, rules and simultaneously store all documents in a central online repository.

This integration scenario is supported for SAP S/4HANA and includes the following scope items:

- 1XV - SAP S/4HANA for Enterprise Contract Management: This is the main system of this integration scenario where the Legal Counsel manages the lifecycle of your legal content by maintaining:
    - Business related information (legal entities, internal contacts)
    - Configuration (general configuration, legal context, categories)
    - Operational information (legal content lifecycle, tasks)
- 2OQ - Integration to SAP Enterprise Contract Assembly: This system enables the legal counsel to author and assemble the legal content by using:
    - Templates and text blocks as elements to reuse content
    - Virtual documents created from the assembly of a template, based on a specific business context

## Purpose

Overview

The SAP S/4HANA Cloud Public Edition, enterprise contract management solution enables digitization of legal transactions within an organization. This application facilitates creation and management of legal content in enterprises in alignment with core business processes and provides an integrated platform to run enterprise-wide legal process more efficiently.

SAP Enterprise Contract Assembly is an SAP BTP application that enables the authoring and assembly of the following legal content:

- Templates and text blocks as elements to reuse content
- Virtual documents as a result of the assembly of a template based on and specific business context

The integration of SAP Enterprise Contract Assembly with SAP S/4HANA Cloud Public Edition, enterprise contract management enables enterprises to integrate with all core business processes, assemble all types of documents based on templates, text blocks, rules, and simultaneously store all documents in a central online repository.

This document provides a detailed procedure for testing this scope item after solution activation, reflecting the predefined scope of the solution. Each process step, report, or item is covered in its own section, providing the system interactions (test steps) in a table view. Steps that are not in scope of the process but are needed for testing are marked accordingly. Project-specific steps must be added.

|  |
| --- |
| Note Values in this test script (decimal notation, date formats, and so on) are presented in U.S. standard notation. If your test system is set up to use a different notation, enter values as appropriate. |

## Prerequisites

This section summarizes all the prerequisites for conducting the test in terms of systems, users, master data, organizational data, other test data and business conditions.

### System Access

| System | Details |
| --- | --- |
| System | Accessible via SAP Fiori launchpad. Your system administrator provides you with the URL to access the various apps assigned to your role. |

### Roles

Create business roles using the following business role templates delivered by SAP and assign them to your individual test users.

Alternatively, if available, you can use the following spaces delivered by SAP. You create a space with pages containing predefined essential apps and assign it to the business role. You then assign this business role to your individual users.

For more information, refer to How to Create a Business Role from a Template in the [product assistance](https://help.sap.com/docs/SAP_S4HANA_CLOUD/53e36b5493804bcdb3f6f14de8b487dd/ec310a8b669a45ca898dc4dd91d97de2.html) for SAP S/4HANA Cloud Public Edition.

| Name (Role Template) | ID (Role Template) | Name (Launchpad Space) | ID (Launchpad Space) | Log On |
| --- | --- | --- | --- | --- |
| Configuration Expert - Business Process Configuration | SAP_BR_BPC_EXPERT | Business Process Configuration / Business Process Configuration - Finance / Business Process Configuration - Procurement / Manage your Solution / Business Process Configuration - Workflow / Business Configuration - Feature Management / Business Process Configuration - Extensibility Explorer / Business Configuration - Transportation | SAP_BR_BPC_EXPERT / SAP_FIN_SPT_BPC_EXPERT_PC / SAP_MM_SPT_BIZ_PROC_CONFIGN_PC / SAP_CA_SPT_IC_LND_BASE_PC / SAP_CA_SPT_BPC_WORKFLOW_PC / SAP_CA_SPT_BPC_FM_PC / SAP_EI_SPT_BPC_EXT_PC / SAP_TM_SPT_TRANSPCFG_PC | Suggested sample User: <user>, representing the business role Configuration Expert - Business Process Configuration.Password: <password> |
| Legal Counsel | SAP_BR_LEGAL_COUNSEL | Legal Counsel - Enterprise Contract Management | SAP_BR_LEGAL_COUNSEL | Suggested sample User: <user>, representing the business role: Legal CounselPassword: <password> |

### Business Conditions

Before this test script can be tested, the following business conditions must be met.

| Scope Item | Business Condition |
| --- | --- |
| 1XV - SAP S/4HANA for Enterprise Contract Management | The following steps of 1XV - SAP S/4HANA for Enterprise Contract Management are mandatory for this scope item:4.4 Prerequisite Settings5.1 Manage Contexts5.2 Request Legal Content |

### Additional Manual Configuration

Before you can test this scope item, you must have completed the additional configuration steps that are described in the Set-Up Instructions for this scope item. These configuration steps are specific for your implementation and include mandatory settings that are not delivered by SAP and must be created by you. For more information, follow the link to the document:

[Link to Set-Up Instructions](https://help.sap.com/docs/SAP_S4HANA_BEST_PRACTICES/a729753e61748c34871d0907fa3e123a)

### Preliminary Steps

#### Define Areas

Purpose

This topic guides you to define areas. The areas can create the mapping relationship between the entities in SAP S/4HANA Cloud Public Edition, enterprise contract management and areas in SAP Enterprise Contract Assembly, private edition to authorize the document creation.

Procedure

Depending on your configuration environment for SAP S/4HANA Cloud Public Edition, choose one of the following options:

Configure Your Solution:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori launchpad using business role Configuration Expert - Business Process Configuration. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the appropriate Fiori app | Open Manage Your Solution (F1241). | The Manage Your Solution screen is displayed. |  |
| 3 | Open Configure Your Solution | Choose Configure Your Solution.Note To create country or region dependent settings for the intended local version, choose Set Local Version. | The Configure Your Solution: Realize Phase screen is displayed. |  |
| 4 | Open Define Areas | On the Configure Your Solution: Realize Phases screen, search Legal Transaction Assembly Integration, then choose Search.Select the line of the item and go to the next screen.On the Configure Your Solution - Legal Transaction Assembly Integration screen, choose Configure on the line of configuration step with the name Define Areas. | The Change View "LCA Area": Details screen is displayed. |  |
| 5 | Save | On the Define Areas: Change screen, choose New Entries, then make the following entries:Area ID: for example, GEN01Profle: GENERICEntity Technical Type: Purchase OrgnizationEntity Minimum: for example, 1000Entity Maximum (optinal): for example, 2000Choose Save.NoteThe area IDs come from the table LCM_LCA_AREA, the data is replicated from ECA tenant on SAP BTP via the background job which will be scheduled after scope item 2OQ is activated.As mentioned in the section [Additional Manual Configuration](#unique_7) [page ] 5, the Entity Technical Type is the organization type and should be configured as a prerequisite, otherwise it does not make sense to maintain the areas here.The combination of Entity Technical Type, Entity Minimum and Entity Maximum maintained in the area should cover the data you have entered in the Context, otherwise the legal document created from the template will fail. | Area is created. |  |

SAP Central Business Configuration:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the project experience in SAP Central Business Configuration. |  |  |
| 2 | Open Define Document Variables | Go to the Configuration app and search for the following activity: Define Areas.Choose Open Documentation for the line item to see more details about this configuration activity.Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. | The Change View "LCA Area": Overview screen displays. |  |
| 3 | Save | On the Define Areas: Change screen, choose New Entries, then make the following entries:Area ID: for example, GEN01Profle: GENERICEntity Technical Type: Purchase OrgnizationEntity Minimum: for example, 1000Entity Maximum (optinal): for example, 2000Choose Save.NoteThe area IDs come from the table LCM_LCA_AREA, the data is replicated from ECA tenant on SAP BTP via the background job which will be scheduled after scope item 2OQ is activated.As mentioned in the section [Additional Manual Configuration](#unique_7) [page ] 5, the Entity Technical Type is the organization type and should be configured as a prerequisite, otherwise it does not make sense to maintain the areas here.The combination of Entity Technical Type, Entity Minimum and Entity Maximum maintained in the area should cover the data you have entered in the Context, otherwise the legal document created from the template will fail. | Area is created. |  |

#### Define Document Variables (Optional)

Purpose

It is a Self-Service Configuration UI to guide you to define the document variables using the Manage Your Solution app, which defines the variable mapping, source CDS Views, and aliases for the document variables. For more details, please refer to the setup instruction of scope item 2OQ.

Procedure

Depending on your configuration environment for SAP S/4HANA Cloud Public Edition, choose one of the following options:

Configure Your Solution:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori launchpad using business role Configuration Expert - Business Process Configuration. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the Fiori app | Open Manage Your Solution. | The Manage Your Solution screen is displayed. |  |
| 3 | Open Configure Your Solution | Choose Configure Your Solution.Note To create country-/region-dependent settings for the intended local version, choose Set Local Version. | The Configure Your Solution: Realize Phase screen is displayed. |  |
| 4 | Open Define Document Variables | On the Configure Your Solution: Realize Phases screen, search Legal Transaction Assembly Integration, then choose Search.Select the line of the item and go to the next screen.On the Configure Your Solution - Legal Transaction Assembly Integration screen, choose Configure. On the line of configuration step with name Define Document Variables. | The Change View "Maintain Variable/Association Source CDS Mapping": Ovewview screen is displayed. |  |
| 5 | Option 1: Create New Variable If Not Exist in System Table | On the Change View "Maintain Variable/Association Source CDS Mapping": Ovewview screen, choose New Entries and make the following entries:Variable: enter the variable name, for example: ZAbcCDS View Name: enter the CDS View, for example I_ABCChoose Save.Choose the view Maintain Variable Source Field Alias on the left. On the Change View "Maintain Variable Source Field Alias": Ovewview screen, choose New Entries and make the following entries:Variable: enter the variable name, for example: ZAddressTechnical Field Name: select the data element for the variable, for example CITYNAMETechnical Field Alias/Association Name: maintain the Alias or Association name as interpreted by ECA. For example: CityNameCardinality: maintain the cardinality if the data element is not maintainedRef.Curr/Quan Alias Field: enter the Reference field if the variable is Currency/Quantity, for example: DocumentCurrencyNote When you select the Technical Field Name, the fields Tech. Field Data Type, Length, and Decimals are auto populated.Mandatory: select the check box of a variable if it must be used for further association with another variableTech.Field Long Text: enter the long text for the variableChoose Save.Choose the view Maintain Entity Mapping for Document Variables on the left. On the Change View "Maintain Entity Mapping for Document Variables": Ovewview screen, choose New Entries and make the following entries:Seq. ID: enter the sequence number, for example, 5001Variable: enter a variable name, for example, ZAbcClass/Interface: enter a class name for calculation, for example, ZCL_CLASS_NAMEChoose Save. | The document variables are maintained with option 1. |  |
| 6 | Option 2: Maintain Variable and Alias If Variable Exists in System Table | Choose the view Maintain Variable Source Field Alias on the left. On the Change View "Maintain Variable Source Field Alias": Ovewview screen, choose New Entries and make the following entries:Variable: enter a variable name which already exists in the system table, for example, AddressTechnical Field Name: select the data element for the variable, for example CITYNAMETechnical Field Alias/Association Name: maintain the Alias or Association name as interpreted by ECA. For example: CityNameCardinality: maintain the cardinality if the data element is not maintainedRef.Curr/Quan Alias Field: enter the Reference field if the variable is Currency/Quantity, for example: DocumentCurrencyMandatory: select the check box of a variable if it must be used for further association with another variableTech.Field Long Text: enter the long text for the variableChoose Save.Choose the view Maintain Entity Mapping for Document Variables on the left. On the Change View "Maintain Entity Mapping for Document Variables": Ovewview screen, choose New Entries and make the following entries:Seq. ID: enter the sequence number, for example, 5001Variable: enter a variable name, for example, ZAbcClass/Interface: enter a class name for calculation, for example, ZCL_CLASS_NAMEChoose Save. | The document variables are maintained with option 2. |  |
| 7 | Option 3: Maintain Variable and Alias by Import Variable Fields | Choose the view Maintain Variable Source Field Alias on the left. On the Change View "Maintain Variable Source Field Alias": Ovewview screen, choose New Entries and choose Import Variable Fields, make the following entries:Variable: enter a variable name which already exists in the system table, for example, AddressTechnical Field Name: select all the fields by selecting the checkbox on the leftChoose Copy.Choose Save. | The document variables are maintained with option 3. |  |

SAP Central Business Configuration:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the project experience in SAP Central Business Configuration. |  |  |
| 2 | Open Define Document Variables | Go to the Configuration app and search for the following activity: Define Document Variables.Choose Open Documentation for the line item to see more details about this configuration activity.Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. | The Change View "Maintain Variable/Association Source": Overview screen displays. |  |
| 3 | Option 1: Create New Variable If Not Exist in System Table | On the Change View "Maintain Variable/Association Source": Overview screen, choose New Entries and make the following entries:Variable: enter the variable name, for example: ZAbcCDS View Name: enter the CDS View, for example I_ABCChoose Save.Choose the view Maintain Variable Source Field Alias on the left. On the Change View "Maintain Variable Source Field Alias": Ovewview screen, choose New Entries and make the following entries:Variable: enter the variable name, for example: ZAddressTechnical Field Name: select the data element for the variable, for example CITYNAMETechnical Field Alias/Association Name: maintain the Alias or Association name as interpreted by ECA. For example: CityNameCardinality: maintain the cardinality if the data element is not maintainedRef.Curr/Quan Alias Field: enter the Reference field if the variable is Currency/Quantity, for example: DocumentCurrencyNote When you select the Technical Field Name, the fields Tech. Field Data Type, Length, and Decimals are auto populated.Mandatory: select the check box of a variable if it must be used for further association with another variableTech.Field Long Text: enter the long text for the variableChoose Save.Choose the view Maintain Entity Mapping for Document Variables on the left. On the Change View "Maintain Entity Mapping for Document Variables": Ovewview screen, choose New Entries and make the following entries:Seq. ID: enter the sequence number, for example, 5001Variable: enter a variable name, for example, ZAbcClass/Interface: enter a class name for calculation, for example, ZCL_CLASS_NAMEChoose Save. | The document variables are maintained with option 1. |  |
| 4 | Option 2: Maintain Variable and Alias If Variable Exists in System Table | Choose the view Maintain Variable Source Field Alias on the left. On the Change View "Maintain Variable Source Field Alias": Ovewview screen, choose New Entries and make the following entries:Variable: enter a variable name which already exists in the system table, for example, AddressTechnical Field Name: select the data element for the variable, for example CITYNAMETechnical Field Alias/Association Name: maintain the Alias or Association name as interpreted by ECA. For example: CityNameCardinality: maintain the cardinality if the data element is not maintainedRef.Curr/Quan Alias Field: enter the Reference field if the variable is Currency/Quantity, for example: DocumentCurrencyMandatory: select the check box of a variable if it must be used for further association with another variableTech.Field Long Text: enter the long text for the variableChoose Save.Choose the view Maintain Entity Mapping for Document Variables on the left. On the Change View "Maintain Entity Mapping for Document Variables": Ovewview screen, choose New Entries and make the following entries:Seq. ID: enter the sequence number, for example, 5001Variable: enter a variable name, for example, ZAbcClass/Interface: enter a class name for calculation, for example, ZCL_CLASS_NAMEChoose Save. | The document variables are maintained with option 2. |  |
| 5 | Option 3: Maintain Variable and Alias by Import Variable Fields | Choose the view Maintain Variable Source Field Alias on the left. On the Change View "Maintain Variable Source Field Alias": Ovewview screen, choose New Entries and choose Import Variable Fields, make the following entries:Variable: enter a variable name which already exists in the system table, for example, AddressTechnical Field Name: select all the fields by selecting the checkbox on the leftChoose Copy.Choose Save. | The document variables are maintained with option 3. |  |

## Overview Table

This scope item consists of several process steps provided in the following table.

|  |
| --- |
| Note If your system administrator has enabled spaces and pages on the SAP Fiori launchpad, the homepage will only contain the essential apps for performing the typical tasks of a business role.You can find all other (searchable) apps not included on the homepage using the search bar ([2434549](https://me.sap.com/notes/2434549)).If you want to personalize the homepage and include the hidden apps, navigate to your user profile and choose App Finder. |

| Process Step, Report, or Item | Business Role | App/Transaction | Expected Results |
| --- | --- | --- | --- |
| [Create Legal Documents](#unique_12) [page ] 14 | Legal Counsel | Manage Legal Transactions (F2310) | User is able to edit the details. |
| [Manage Legal Documents](#unique_13) [page ] 15 | Legal Counsel | Manage Legal Documents (F2453) | User is able to edit the legal documents. |

## Test Procedures

This section describes test procedures for each process step that belongs to this scope item.

### Create Legal Documents

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you can not only upload the document as an attachment, but also create the virtual document from the template for a Legal Transaction based on the integration between SAP S/4HANA for Enterprise Contract Management and SAP S/4HANA for Enterprise Contract Assembly.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori launchpad using business role Legal Counsel. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the app | Open Manage Legal Transactions (F2310) | The Manage Legal Transactions screen is displayed. |  |
| 3 | Manage Legal Transactions | On the Manage Legal Transactions page, choose a legal transaction in the list. | The Legal Transaction screen is displayed. |  |
| 4 | Create Virtual Document for the mandatory document | In the Documents section, if an entry is already existing, it is a mandatory document which is created automatically from the Context.To add virtual document for the mandatory document, choose Create under the document name. The Select Creation Method screen is displayed.On the Select Creation Method screen, choose Create from Template and make the following entries:Content Type: <fixed and inherited from the Context>Acess Level (optional): for example, PrivateDocument Name (optional): for example, Virtual Document of ContractLanguage: for example, EnglishGoverning Law: <read-only and inherited from the legal transaction>for example, IndiaChoose Continue.On the Select: Template screen, choose a template (click on the first column of the entry) from the list, which is replicated from Legal Content Assembly via the integration scenario. | The Virtual Document is created for the legal transac-tion.The Status of this document is New, and the Assembly Status is Assembly in progress.The Status of this document will be changed to In process, and the Assembly Status is Final, Peng-ding or Error after the synchronization to ECA is done.Note The current version of the legal document is 1. |  |
| 5 | Create Virtual Document for the non-mandatory document | In the Documents section, choose Create from Template on the right near the search bar. The Create from Template screen is displayed.On the Create from Template screen, make the following entries:Content Type: for example, Master ContractAcess Level (optinal): for example, PrivateDocument Name (optional): for example, Virtual Document of ContractLanguage : for example, EnglishGoverning Law: for example, IndiaChoose Continue .On the Select: Template screen, choose a template (click on the first column of the entry) from the list, which is replicated from Legal Content Assembly via the integration scenario. | The Virtual Document is created for the legal transaction.The Status of this document is New, and the Assembly Status is Assembly in progress.The Status of this document will be changed to In process, and the Assembly Status is Final, Pengding or Error after the synchronization to ECA is done.Note The current version of the legal document is 1. |  |

### Manage Legal Documents

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you can manage the legal documents including the virtual documents.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori launchpad using business role Legal Counsel. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the App | Open Manage Legal Documents (F2453) | The Manage Legal Documents screen is displayed. |  |
| 3 | Manage Legal Documents | Choose the Legal Document with status In Process.To edit Legal Document, choose Edit on the upper right corner. | Now you are inside Legal Document.Note The Create button is visible for a Virtual Document when the status is still New. You can create a file from template or upload a file.Edit button is not visible for a Virtual Document until the status is changed from New to In process.You can also use the Enterprise Search functionality to search your Legal docuement:Choose Search in the upper right area of the launchpad.In the dropdown list choose: Legal Documents and input Document Number from previous section.Now you are able to see the details of the Legal document. |  |
| 4 | Stamps (Optional) | In Stamps Section, make the following entries and choose Create.Stamp Name: select the appropriate one from the dropdown list, for example ApprovedDate, Time: Set to defaultAdded By: Set to defaultChoose Save | Then it navigates to Legal Document.Note Stamps can be added to a virtual document only after the Assembly Status is changed from In process to Final. |  |
| 5 | Edit the document (For the virtual document) | To change the attributes of the document, choose Edit on the upper right corner.Update the attributes and choose Save.To change the content of the document, choose More and then choose Edit Content on the upper right corner.This action will access the Manage Document app in integrated ECA tenant with corresponding authentication method. The content can be updated.Note For the details of ECA apps on BTP, please refer to the[User Guide for SAP Enterprise Contract Assembly](https://help.sap.com/viewer/37ab28cfdf2a4f32b7585eaf8b43d514/SHIP/en-US). | The virtual document is modified.Note If the virtual document is edited on SAP BTP, the old version will be created in Version History. |  |
| 6 | Generate word file (For the virtual document) | To generate the word file of the document, choose More and then choose Generate Word File on the upper right corner.If the warning By generating a word file, you can no longer edit the virtual document. Are you sure you want to continue? appears, choose Continue. | The word file of the legal document is generated.Note The old version will be created in Version History. |  |
| 7 | Upload signed document (For the virtual document) | Choose Download on the upper right corner and save the file to your local folder.After the file is signed off CM application, choose Check In and upload the modified file to release the new version. | The signed document is uploaded.Note The old version will be created in Version History. |  |
| 8 | Update document status | After the document is completed, choose Set the Set to Accepted on the upper right corner to set the document status to Accepted. | Health Status of the legal document is updated to On Track after all the documents have the status Accepted.Note The Health Status will remain Pending if a virtual document is created in the Legal Transaction. |  |
| 9 | Archive the document (Optional) | To archive the document, choose To Be Archived on the upper right corner. | The Status and Assembly Status of the document is changed to To Be Archived. |  |
| 10 | Reopen the document (Optional) | To reopen the document with status To Be Archived, choose Reopen on the upper right corner. | The Status of the document is changed to In Process, and the Assembly Status is changed to Assembly In Process. |  |
| 11 | Delete the document (Optional) | To delete the document, choose Delete on the upper right corner. | The legal document is deleted. |  |

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
- related-to :: [[01-solution-foundation-and-platform/test-script-integration-to-icertis-for-contract-assembly-6v2-sap-s-4ha]]
- related-to :: [[01-solution-foundation-and-platform/test-script-sap-s-4hana-cloud-public-edition-sap-s-4hana-for-enterpris]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/2OQ_S4CLD2608_BPD_EN_XX.docx` — full document · extracted with `mammoth` · 32,237 chars in the whole document
