---
id: 01-solution-foundation-and-platform/test-script-integration-to-icertis-for-contract-assembly-6v2-sap-s-4ha
title: "Test Script: Integration to Icertis for Contract Assembly (6V2) - SAP S/4HANA Cloud Public Edition (6V2_S4CLD2608_BPD_EN_XX)"
description: "SAP test script for scope item 6V2: Icertis integration with Enterprise Contract Management; prerequisites, configuration, legal document and signature tests."
cluster: 01-solution-foundation-and-platform
tags: [kb/solution-foundation-and-platform, topic/enterprise-contract-assembly]
aliases: [6V2_S4CLD2608_BPD_EN_XX]
keywords: [Enterprise Contract Assembly Integration, icertis integration, enterprise contract management, legal documents, legal document management, e-signature, self-service configuration, business roles, test scripts, business conditions]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/6V2_S4CLD2608_BPD_EN_XX.docx]
confidence: low
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-1191
topic: 01-solution-foundation-and-platform/enterprise-contract-assembly
language: EN
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Test Script: Integration to Icertis for Contract Assembly (6V2) - SAP S/4HANA Cloud Public Edition (6V2_S4CLD2608_BPD_EN_XX)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/6V2_S4CLD2608_BPD_EN_XX.docx`, extracted with `mammoth`. Grouped under **Enterprise Contract Assembly Integration** in Solution Foundation and Platform. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

|  |  |
| --- | --- |
| Integration to Icertis for Contract Assembly (6V2)Introduction PUBLIC 1<!-- image omitted: unnamed --> | Test ScriptSAP S/4HANA Cloud Public Edition - 19-06-26 |
|  | Integration to Icertis for Contract Assembly (6V2) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Table of Contents

[1 Introduction 2](#_Toc232841706)

[2 Purpose 3](#_Toc232841707)

[3 Prerequisites 4](#_Toc232841708)

[3.1 System Access 4](#_Toc232841709)

[3.2 Roles 4](#_Toc232841710)

[3.3 Additional Manual Configuration 5](#_Toc232841711)

[3.4 Business Conditions 5](#_Toc232841712)

[3.5 Preliminary Steps 5](#_Toc232841713)

[3.5.1 Configure Self-Service Configuration UIs/ Configuration Activities 5](#_Toc232841714)

[4 Overview Table 11](#_Toc232841715)

[5 Test Procedure 12](#_Toc232841716)

[5.1 Create Legal Documents 12](#_Toc232841717)

[5.2 Manage Legal Documents 14](#_Toc232841718)

[5.3 Send Legal Document for Signature 17](#_Toc232841719)

## Introduction

SAP S/4HANA for Enterprise Contract Management provides a suite of applications designed for the creation and management of legal contracts in enterprises. SAP partners with Icertis to transform the source-to-contract process. This integration unites best-of-breed technologies, providing businesses with easy access to critical information, and enabling better decisions within the SAP application environment. Icertis brings contract intelligence, a new approach to contract lifecycle management that provides companies the ability to dynamically analyze contracts in the context of the systems and processes that drive the business forward. Integration of SAP S/4HANA for Enterprise Contract Management with Icertis enables intelligent, buy-side, sell-side, and organization-wide contracting.

This integration scenario is supported for SAP S/4HANA and includes the following scope items:

- 1XV - SAP S/4HANA for Enterprise Contract Management: This is the main system of this integration scenario where the Legal Counsel manages the lifecycle of your legal content by maintaining:
    - Business related information (legal entities, internal contacts)
    - Configuration (general configuration, legal context, categories)
    - Operational information (legal content lifecycle, tasks)
- 6V2 - Integration to Icertis for Contract Assembly: This system enables the legal counsel to author and assemble the legal content by using:
    - Templates and text blocks as elements to reuse content
    - Legal documents created from the assembly of a template, based on a specific business context

## Purpose

Overview

With Enterprise Contract Management, you can integrate SAP S/4HANA Cloud Public Edition system with external contract assembly product Icertis Contract Intelligence. This integration enables users to create and manage legal content that is generated out of various business scenarios in a company, such as procurement processes, sales, policies, or intercompany agreements. The users can further collaborate on the document until it's agreed on by all the internal and external stakeholders and ready for execution through signature.

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

### Additional Manual Configuration

Before you can test this scope item, you must have completed the additional configuration steps that are described in the Set-Up Instructions for this scope item. These configuration steps are specific for your implementation and include mandatory settings that are not delivered by SAP and must be created by you. For more information, follow the link to the document:

[Link to Set-Up Instructions](https://help.sap.com/docs/SAP_S4HANA_BEST_PRACTICES/d499f7bf26cbf3377b15177a1001d8c6)

### Business Conditions

Before this test script can be tested, the following business conditions must be met.

| Scope Item | Business Condition |
| --- | --- |
| 1XV - SAP S/4HANA for Enterprise Contract Management | The following steps of 1XV - SAP S/4HANA for Enterprise Contract Management are mandatory for this scope item:Prerequisite SettingsManage ContextsRequest Legal Content |

### Preliminary Steps

#### Configure Self-Service Configuration UIs/ Configuration Activities

Depending on your configuration environment for SAP S/4HANA Cloud Public Edition, choose one of the following options:

Configure Your Solution:

Purpose

You can use self-service configuration UIs to tailor the pre-configured processes to your business requirements. Proceed with the configuration in the suggested sequence.

List of the available self-service configuration UIs for Icertis integation:

| Sequence | Configuration UI | Description |
| --- | --- | --- |
| 1 | Enable Switch for Icertis Contract Intelligence | Activate or deactivate the business function switch for integration with Icertis Contract Intelligence. Once the switch is enabled, we can create an agreement via a legal document. |
| 2 | Maintain Icertis Contract Types | Maintain the Icertis contract types that must be mapped to the content type in the Enterprise Contract Management system. |
| 3 | Define Document Variables | Define the variable mapping, source CDS Views, and aliases for the document variables. |
| 4 | Maintain Agreement Business Statuses | Maintain various business statuses for agreements that are received from the Icertis system. |
| 5 | Maintain Mapping between Contact Types and Icertis Roles | Maintain the mapping between the contact types from Enterprise Contract Management system and roles from the Icertis Intelligence system. With this configuration, you can propagate the details from enterprise contract management to Icertis in the agreement. |
| 6 | Maintain Contract Type Groups for Supporting Documents | Maintain the group name for supporting documents and a name for the associated contract type. |
| 7 | Disable Signature Process | Disable the signature process in the Enterprise Contract Management system. |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori launchpad as a Configuration Expert. | The SAP Fiori Launchpad is displayed. |  |
| 2 | Access the app | Open Manage Your Solution. | The Manage Your Solution screen is displayed. |  |
| 3 | Filter the Configuration UIs of ECMA | On the Manage Your Solution screen, choose Configure Your Solution.On the Configure Your Solution screen, set the filters in the search bar:Application Area: Application Platform and InfrastructureSub Application Area: Enterprise Contract Management and AssemblyChoose one of the entries and the configuration UIs are displayed. | The list of self-service configuration UIs are displayed. |  |
| 4 | Enable Switch for Icertis Contract Intelligence (Recommended) | On the Configure Your Solution screen, choose the item name Integration with Icertis Contract Intelligence. The configuration UIs for Icertis integration are displayed.Navigate to the step name Enable Switch for Icertis Contract Intelligence on the right part of the screen and choose Configure.On the Display/Change State of Business Function screen, choose Change State to activate the integration scenario. | Integration with Icertis Contract Intelligence is enabled. |  |
| 5 | Maintain Icertis Contract Types (Recommended) | Navigate to the step name Maintain Icertis Contract Types on the right part of the screen. Choose Configure.On the Change View "Maintain Icertis Contract Types": Ovewview screen, choose New Entries and make the following entries:Cont. Type: <enter a valid content type ID or choose from the search help>Contract Type: <enter the mapping contract type which is valid in Icertis>Choose Save.Note You could maintain the content type via the self-service configuration UI / Configuration Activities – Define Content Types (ID: 101058) in another item Legal Documents. | The mapping between content types (ECM) and contract types (Icertis) are maintained. |  |
| 6 | Define Document Variables (Optional) | Navigate to the step name Define Document Variables on the right part of the screen. Choose Configure.For details please refer to the Set-Up Instructions for this scope item. | Document variables are defined. |  |
| 7 | Maintain Agreement Business Statuses (Recommended) | Navigate to the step name Maintain Agreement Business Statuses on the right part of the screen. Choose Configure.On the Maintain Agreement Business Statuses: Change screen, choose New Entries and make the following entries:Agreement Business Status: <enter a status ID>Agreement Business Status Text: <enter a description>Choose Save. | Agreement business statuses are maintained. |  |
| 8 | Maintain Mapping between Contact Types and Icertis Roles (Optional) | Navigate to the step name Maintain Mapping between Contact Types and Icertis Roles on the right part of the screen. Choose Configure.On the Maintain Mapping between Contract Types and Icertis Roles: Change screen, choose New Entries and make the following entry:Icertis Team Role: <enter a role ID>Select the new entry and choose Maintainance view for Icrts Roles with Contact Typ on the left, choose New Entries and make the following entries:Ctct Type: <choose the contact type (internal or external) from the dropdown list>Indicator: <enter a valid contract type ID or choose from the search help>Choose Save.Note You could maintain the contact type via the self-service configuration UI / configuration activities – Define External Contacts (ID: 101061) and Define Internal Contacts (ID: 101062) in another item Legal Transactions. | The mapping between contract types and Icertis roles are maintained. |  |
| 9 | Maintain Contract Type Groups for Supporting Documents (Optional) | Navigate to the step name Maintain Contract Type Groups for Supporting Documents on the right part of the screen. Choose Configure.On the Maintain Contract Type Groups for Supporting Documents: Change screen, choose New Entries and make the following entry:Group Name: <empty or supporting documents>Select the new entry and choose Content typs of Supporting Documents on the left, choose New Entries and make the following entry:Cont. Type: <enter a valid content type from the search help>Choose Save.Note You could maintain the content type via the self-service configuration UI Define Content Types (ID: 101058) in another item Legal Documents. | The content type groups for supporting documents are maintained. |  |
| 10 | Disable Signature Process (Optional) | Navigate to the step name Disable Signature Process on the right part of the screen. Choose Configure.On the Disable Signature Process: Change: Details screen, check the flag Disable Signature.Choose Save. | The signature process is disabled in ECM system. |  |

SAP Central Business Configuration

Purpose

You can use these configuration activities to tailor the pre-configured processes to your business requirements. Proceed with the configuration in the suggested sequence.

List of the available configuration activities:

|  |  |  |
| --- | --- | --- |
| Sequence | Configuration Activities in SAP Central Business Configuration | Description |
| 1 | Enable Switch for Icertis Contract Intelligence | Activate or deactivate the business function switch for integration with Icertis Contract Intelligence. Once the switch is enabled, we can create agreements via legal documents. |
| 2 | Maintain Icertis Contract Types | Maintain the Icertis contract types that must be mapped to the content type in the Enterprise Contract Management system. |
| 3 | Define Document Variables | Define the variable mapping, source CDS Views, and aliases for the document variables. |
| 4 | Maintain Agreement Business Statuses | Maintain various business statuses for agreements that are received from the Icertis system. |
| 5 | Maintain Mapping between Contact Types and Icertis Roles | Maintain the mapping between the contact types from Enterprise Contract Management system and roles from the Icertis Intelligence system. With this configuration, you can propagate the details from enterprise contract management to Icertis in the agreement.. |
| 6 | Maintain Contract Type Groups for Supporting Documents | Maintain the group name for the supporting documents and the name of the associated contract type. |
| 7 | Disable Signature Process | Disable the signature process in the Enterprise Contract Management system. |

Log on to the project experience in SAP Central Business Configuration.

Go to the Configuration app. Search for the following configuration activities and choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration.

| Test Step # | Configuratiion Activity Steps | Instruction | Expected Result | Comment |
| --- | --- | --- | --- | --- |
| 1 | Enable Switch for Icertis Contract Intelligence (Recommended) | Search the step Enable Switch for Icertis Contract Intelligence and choose Configure.On the Display/Change State of Business Function screen, choose Change State to activate the integration scenario. | Integration with Icertis Contract Intelligence is enabled. |  |
| 2 | Maintain Icertis Contract Types (Recommended) | Search the step name Maintain Icertis Contract Types s. Choose Configure.On the Change View "Maintain Icertis Contract Types": Ovewview screen, choose New Entries and make the following entries:Cont. Type: <enter a valid content type ID or choose from the search help>Contract Type: <enter the mapping contract type which is valid in Icertis>Choose Save.Note You could maintain the content type via the self-service configuration UI / configuration activities – Define Content Types (ID: 101058) in another item Legal Documents. | The mapping between content types (ECM) and contract types (Icertis) are maintained. |  |
| 3 | Define Document Variables (Optional) | Search the step name Define Document Variables . Choose Configure.For details please refer to the Set-Up Instructions for this scope item. | Document variables are defined. |  |
| 4 | Maintain Agreement Business Statuses (Recommended) | Search the step name Maintain Agreement Business Statuses . Choose Configure.On the Maintain Agreement Business Statuses: Change screen, choose New Entries and make the following entries:Agreement Business Status: <enter a status ID>Agreement Business Status Text: <enter a description>Choose Save. | Agreement business statuses are maintained. |  |
| 5 | Maintain Mapping between Contact Types and Icertis Roles (Optional) | Search the step name Maintain Mapping between Contact Types and Icertis Roles . Choose Configure.On the Maintain Mapping between Contract Types and Icertis Roles: Change screen, choose New Entries and make the following entry:Icertis Team Role: <enter a role ID>Select the new entry and choose Maintainance view for Icrts Roles with Contact Typ on the left, choose New Entries and make the following entries:Ctct Type: <choose the contact type (internal or external) from the dropdown list>Indicator: <enter a valid contract type ID or choose from the search help>Choose Save.Note You could maintain the contact type via the self-service configuration UI / configuration activities – Define External Contacts (ID: 101061) and Define Internal Contacts (ID: 101062) in another item Legal Transactions. | The mapping between contract types and Icertis roles are maintained. |  |
| 6 | Maintain Contract Type Groups for Supporting Documents (Optional) | Search the step name Maintain Contract Type Groups for Supporting Documents . Choose Configure.On the Maintain Contract Type Groups for Supporting Documents: Change screen, choose New Entries and make the following entry:Group Name: <empty or Supporting Documents>Select the new entry and choose Content typs of Supporting Documents on the left, choose New Entries and make the following entry:Cont. Type: <enter a valid content type from the search help>Choose Save.Note You could maintain the content type via the self-service configuration UI / configuration activities – Define Content Types (ID: 101058) in another item Legal Documents. | The content type groups for supporting documents are maintained. |  |
| 7 | Disable Signature Process (Optional) | On the Disable Signature Process: Change: Details screen, choose New Entries and check the flag Disable Signature.Choose Save. | The signature process is disabled in ECM system. |  |

## Overview Table

This scope item consists of several process steps provided in the following table.

|  |
| --- |
| Note If your system administrator has enabled spaces and pages on the SAP Fiori launchpad, the homepage will only contain the essential apps for performing the typical tasks of a business role.You can find all other (searchable) apps not included on the homepage using the search bar ([2434549](https://me.sap.com/notes/2434549)).If you want to personalize the homepage and include the hidden apps, navigate to your user profile and choose App Finder. |

| Process Step, Report, or Item | Business Role | App/Transaction | Expected Results |
| --- | --- | --- | --- |
| [Create Legal Documents](#unique_10) [page ] 12 | Legal Counsel | Manage Legal Transactions (F2310) | User is able to create the legal documents. |
| [Manage Legal Documents](#unique_11) [page ] 14 | Legal Counsel | Manage Legal Documents (F2453) | User is able to manage the legal documents. |

## Test Procedure

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

In this step, you can upload your document as an attachment, or create legal documents from the template for legal transaction based on the integration between SAP S/4HANA for Enterprise Contract Management and Icertis Contract Intelligence.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori launchpad using business role Legal Counsel. | The SAP Fiori Launchpad is displayed. |  |
| 2 | Access the App | Open Manage Legal Transactions (F2310) | The Manage Legal Transactions screen is displayed. |  |
| 3 | Manage Legal Transactions | On the Manage Legal Transactions page, choose a legal transaction from the list. | The Legal Transaction screen is displayed. |  |
| 4 | Create Legal Document for Mandatory Document | In the Documents section, if an entry already exists, it means it is a mandatory document (the Required field is Yes) that is created automatically from the context.To add a new document for the mandatory document, choose Add on the right. The Select Creation Method screen is displayed.On the Select Creation Method screen, two options are both possible:Choose Upload File and then choose Continue, and make the following entries:Content Type: <read-only and inherited from the context>Access Level (optional): for example, PublicDocument Name (optional): for example, Legal document #1 of contractLanguage: for example, English (EN)Governing Law: <read-only and inherited from the legal transaction>Main Linked Object Type Status: <choose the valid linked object type>Language: for example, English (EN)File: choose Browse and upload a file from local (supported file formats: .DOCX, .DOC, .PDF, .PPT, .PPTX)Choose Upload.Choose Create from Template and Continue, and make the following entries:Content Type: <read-only and inherited from the context>Access Level (optional): for example, PrivateDocument Name (optional): for example, Legal document #1 of contractLanguage: for example, English (EN)Governing Law: <read-only and inherited from the legal transaction>Main Linked Object Type (optional): <choose the valid linked object type>Choose Continue.On the Create from Template screen, choose a template from the list, which is replicated from Icertis Contract Intelligence via the integration scenario. | The legal document is created for the legal transaction.The External Contract Status of this document is changed to Creation Initiated, and the Status is changed to New.After the document is successfully created, the External Contract Status will be changed to Draft, and Status will be changed to In Process. |  |
| 5 | Create Legal Document for Non-mandatory Document | In the Documents section, there are two options to create the non-mandatory document, which is upload a file from local, or create from template:Choose Upload File and Continue, and make the following entry:Content Type: for example, Master ContractNote The content type without a mapped contract type in the list cannot be selected, otherwise the error message Select the content type that is mapped to the contract type will be displayed. The mapping relationship can be maintained via Self-Service Configuration UI / Configuration Activity Maintain Icertis Contract Types.Access Level (optional): for example, PublicDocument Name (optional): for example, Legal document #2 of contractLanguage: for example, English(EN)Governing Law: <read-only and inherited from the legal transaction>Main Linked Object Type (optional): <choose the valid linked object type>Language: for example, English(EN)File: choose Browse and upload a file from local computer (supported file formats: .DOCX, .DOC, .PDF, .PPT, .PPTX)Choose Upload.Choose Create from Template and Continue, and make the following entries:Content Type: for example, Master ContractAccess Level (optinal): for example, PrivateDocument Name (optional): for example, Legal document #2 of contractLanguage: for example, English(EN)Governing Law: for example, IndiaMain Linked Object Type (optional): <choose the valid linked object type>Choose Continue.On the next Create from Template screen, choose a template from the list, which is replicated from Icertis Contract Intelligence via the integration scenario. | The legal document is created for the legal transaction.The External Contract Status of this document is changed to Creation Initiated, and the status is changed to New.After the document is successfully created, the External Contract Status will be changed to Draft, and the status will be changed to In Process. |  |
| 6 | Create Basic Structure of Legal Documents (Optional) | If you only want to create legal documents with basic structures and limited information, go to the Document section, choose Create Document, and make the following entries:Content Type: select an appropriate value from the dropdown list, for example, Master Contract.Language: select an appropriate value from the dropdown list, for example, English.Choose Create. | A legal document with basic structure is created. You can add concrete information later by following the steps described above. |  |

### Manage Legal Documents

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you can manage the legal documents with Icertis Contract Intelligence.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori launchpad using business role Legal Counsel. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Legal Documents (F2453) | The Manage Legal Documents screen is displayed. |  |
| 3 | Manage Legal Documents | Choose the legal document with status In Process.To edit legal document, choose Edit on the upper right corner.Note The Add button is visible for a legal document when it is in status New. You can create a legal document by creating from templates or uploading a file.The Edit button will not be visible for a legal document until the document status is changed from New to In process.You can also use the enterprise search functionality to search your legal documents by following the below steps:Choose Search in the upper right area of the launchpad.From the dropdown list, choose: Legal Documents and input Document Number from previous section. | Now you can edit Legal Document.The details of legal documents will be displayed.The details of legal documents will be displayed. |  |
| 4 | Stamps (Optional) | In Stamps section, make the following entries and choose Create.Stamp Name: select the appropriate stamp name from the dropdown list, for example, Approved.Date, Time: Set to defaultAdded By: Set to defaultChoose Save. | The stamps are added.Note Stamps can be added to a legal document in status In process. |  |
| 5 | Edit the Document | To change the attributes of the document, choose Edit on the upper right corner.Update the attributes mentioned above and choose Save.To change the content of the document, click on the hypelink of the file name under field External Contract Name.This action will direct you to the Agreements app in integrated Icertis Contract Intelligence tenant with corresponding authentication method. The content can be updated.Some follow-up actions might be avaliable on Icertis Contract Intelligence for the legal doucment.Download: You can download the file. This function is the same as the function in SAP S/4HANA Cloud Public Edition.Upload Document: You can upload an additional file to this legal document. A version 2 document will be created.Edit: You can edit the attributes of the legal document.Send for Approval: Send the document for approval, then the status will be changed to Waiting For Internal Signature. After it is signed off, the status will be changed to Executed. The same status will also be synchronized to the field External Contract Status of legal documents in SAP S/4HANA Cloud Public Edition.Cancel: You can cancel legal documents. A pop-up message Please Confirm: With this action the agreement would be in Draft state having Cancelled status. Are you sure you want to continue? will be displayed. Click on Yes to confirm.In addition, the Templates app in Icertis Contract Intelligence can define the templates used to create legal document in SAP S/4HANA Cloud Public Edition. The Clauses app can define the clauses of the legal document.Note For more information about Icertis Contract Intelligence, you could click on the Help icon on the upper right corner of this application.Switch back to the Manage Legal Documents app in SAP S/4HANA Cloud Public Edition for the following steps. | The legal document is modified.Note If the content or status of legal documents is changed on Icertis Contract Intelligence, an older version will be created under Versions tab, and be synchronized to Version History of the legal document on SAP S/4HANA Cloud Public Edition. |  |
| 6 | Download the Document | To download the document, choose Download on the upper right corner and then choose Save. | The legal document file is downloaded. |  |
| 7 | Display the Change Log | To display the change log, choose Display Logs on the upper right corner. | The change log is displayed. |  |
| 8 | Create Supporting Document (Optional) | To create the additional supporting document, choose Create, then choose Supporting Document on the upper right corner, fill in the required fields and upload a file from local storage location. | A supporting document is created. |  |
| 9 | Create Amendment for Main Contract (Optional) | If the Document Kind of your legal document is Main Document, you can choose to create amendments for main contract.Choose Create, and then choose Amendment. Two options are avaliable: Upload a File and Create Document.If you choose the option Upload a File, your new amendment will inherit information of parent document, content type, language and governing law from the main document. These pieces of information can not be changed.If you choose the option Create Document, your new amendment will inherit information of parent document, content type and language from the main document. These pieces of information can not be changed. You can also copy header or obligation information by selecting the Header or/and Obligations attributes or facets. | A new amendment is created for your main document. |  |
| 10 | Delete Document (Optional) | To delete the document, choose Discard Content on the upper right corner. Pop-up message Deleting this document will de-lete all the content and its associated data. Are you sure you want to continue? will be displayed. Choose Continue.Note Document deletion will not be possible if the document status is changed to Accepted or To Be Archived. | The legal document is deleted. |  |

### Send Legal Document for Signature

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you can send the legal document that meets signature.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori launchpad with business role Legal Counsel. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the App | Open Manage Legal Transactions (F2310). | The Manage Legal Transactions screen is displayed. |  |
| 3 | Manage Legal Transactions | Choose the legal transaction with status On Track or Open Issues.Note You can disable the signature function in ECM via the SSCUI - Disable Signature Process as introduced in the Preliminary Steps section above. If the signature functionality is disabled, the following steps for signature could be ignored. | You are in the Legal Transaction page now.You can also use the enterprise search function to search your legal transaction by following the steps below:Choose Search in the upper right corner.In the dropdown list, choose Legal Transactions and enter Transaction Number from previous section.The details of legal transaction will be displayed. |  |
| 4 | Send for E-Signature (Optional) | In Documents section, choose the legal document with a valid document and choose Signature > Send for e-Signature .On the Select Template screen, choose a valid DocuSign template, and choose Next.Select the valid recipient and choose Send. The Signature Status of the legal document will change to Sent for e-Signature.New entry will be automatically generated in the e-Signature Envelopes section. Click the hyperlink of the Envelope ID and log in with DocuSign tenant.Choose SIGN for the envelope, review the document and choose CONTINUE, click on the Sign button on the document. Choose FINISH.After the envelope status is updated, the value of Signature Status field of legal document will change to e-Signed and the Status will change to Accepted.Note The integration scenario SAP_COM_0518 must be configured according to the setup instructions of scope item 1XV, then the legal document can be sent for e-Signature.If your legal document does not have a valid document, Send for e-Signature will not work, and the error message "There is no valid document to be sent for e-Sign" will be displayed. | The legal document is signed with DocuSign e-Signature and is accepted. |  |
| 5 | Start Manual Signature | In Documents section, choose the legal document with a valid document and choose Signature > Start Manual Signature . The signature status of legal document will change to Sent for Manual Signature.After your downloaded file is signed manually, choose Upload Signed File to upload the signed document from local address. For the legal document, the following status will change:Signiture Status: Manually SignedStatus: AcceptedNote If your legal document does not have a valid document, then the button Start Manual Signature will not work, and a piece of error message “Document cannot be sent for manual signature” will be displayed. | The legal document is manually signed and accepted. |  |

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

## Suspected conflicts

> [!warning] Conflict
> Flagged while digesting this document, not verified: The Overview Table lists only Create Legal Documents and Manage Legal Documents, while the table of contents and Test Procedure also include a third process step, Send Legal Document for Signature.

## Connections
- part-of :: [[_cluster]]
- related-to :: [[01-solution-foundation-and-platform/test-script-integration-to-sap-enterprise-contract-assembly-2oq-846]]
- related-to :: [[01-solution-foundation-and-platform/test-script-sap-s-4hana-cloud-public-edition-sap-s-4hana-for-enterpris]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/6V2_S4CLD2608_BPD_EN_XX.docx` — full document · extracted with `mammoth` · 37,878 chars in the whole document
