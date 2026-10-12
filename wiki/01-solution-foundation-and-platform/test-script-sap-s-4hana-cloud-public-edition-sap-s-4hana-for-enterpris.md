---
id: 01-solution-foundation-and-platform/test-script-sap-s-4hana-cloud-public-edition-sap-s-4hana-for-enterpris
title: "Test Script - SAP S/4HANA Cloud Public Edition: SAP S/4HANA for Enterprise Contract Management (1XV) (1XV_S4CLD2608_BPD_EN_XX)"
description: "SAP S/4HANA Cloud Public Edition 2608 test script for scope item 1XV Enterprise Contract Management: roles, configuration UIs and 9 test procedures."
cluster: 01-solution-foundation-and-platform
tags: [kb/solution-foundation-and-platform, topic/enterprise-contract-assembly]
aliases: [1XV_S4CLD2608_BPD_EN_XX]
keywords: [Enterprise Contract Assembly Integration, enterprise contract management, test scripts, self-service configuration, legal contexts, legal transactions, contract requests, electronic signature, envelope status update, legal documents]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/1XV_S4CLD2608_BPD_EN_XX.docx]
confidence: low
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-783
topic: 01-solution-foundation-and-platform/enterprise-contract-assembly
language: EN
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Test Script - SAP S/4HANA Cloud Public Edition: SAP S/4HANA for Enterprise Contract Management (1XV) (1XV_S4CLD2608_BPD_EN_XX)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/1XV_S4CLD2608_BPD_EN_XX.docx`, extracted with `mammoth`. Grouped under **Enterprise Contract Assembly Integration** in Solution Foundation and Platform. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

| <!-- image omitted: unnamed --> | Test ScriptSAP S/4HANA Cloud Public Edition - 19-06-26 |
| --- | --- |
|  | SAP S/4HANA for Enterprise Contract Management (1XV) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Table of Contents

[1 Purpose 2](#_Toc232850555)

[2 Prerequisites 3](#_Toc232850556)

[2.1 System Access 3](#_Toc232850557)

[2.2 Roles 3](#_Toc232850558)

[2.3 Additional Manual Configuration 4](#_Toc232850559)

[2.4 Business Conditions 4](#_Toc232850560)

[2.5 Preliminary Steps 5](#_Toc232850561)

[2.5.1 Manage Situation Types 5](#_Toc232850562)

[2.5.2 Create Categories 6](#_Toc232850563)

[2.5.3 Configure Self-Service Configuration UIs/ Configuration Activities 9](#_Toc232850564)

[3 Overview Table 35](#_Toc232850565)

[4 Test Procedures 36](#_Toc232850566)

[4.1 Manage Context 36](#_Toc232850567)

[4.2 Request Legal Contract 42](#_Toc232850568)

[4.3 Manage Legal Transactions 43](#_Toc232850569)

[4.4 Approve Legal Transactions (Optional) 48](#_Toc232850570)

[4.5 Send Legal Document for Signature 49](#_Toc232850571)

[4.6 Envelope Status Update (Optional) 51](#_Toc232850572)

[4.7 Manage Legal Documents 52](#_Toc232850573)

[4.8 Manage Legal Tasks 54](#_Toc232850574)

[4.9 Check Enterprise Contract Management Overview 55](#_Toc232850575)

## Purpose

Overview

SAP S/4HANA Cloud Public Edition, enterprise contract management connects processes, content, technology, and people in legal departments. It provides a central layer for legal content and an integrated platform for legal technology.

The solution provides the following capabilities:

- End-to-end digitization of legal processes
- Create and manage context for legal transactions
- Create and manage legal transactions
- Easily detect at-risk legal transactions
- Provide extensibility to allow customer to add the fields based on their business needs

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
| Configuration Expert - Business Process Configuration | SAP_BR_BPC_EXPERT | Business Process Configuration / Business Process Configuration - Finance / Business Process Configuration - Procurement / Manage your Solution / Business Process Configuration - Workflow / Business Configuration - Feature Management / Business Process Configuration - Extensibility Explorer / Business Configuration - Transportation | SAP_BR_BPC_EXPERT / SAP_FIN_SPT_BPC_EXPERT_PC / SAP_MM_SPT_BIZ_PROC_CONFIGN_PC / SAP_CA_SPT_IC_LND_BASE_PC / SAP_CA_SPT_BPC_WORKFLOW_PC / SAP_CA_SPT_BPC_FM_PC / SAP_EI_SPT_BPC_EXT_PC / SAP_TM_SPT_TRANSPCFG_PC | Suggested sample User: <user>, representing the business role Configuration Expert - Business Process ConfigurationPassword: <password> |
| Administrator - Enterprise Contract Management | SAP_BR_ADMINISTRATOR_LCM | Administration - Enterprise Contract Management | SAP_BR_ADMINISTRATOR_LCM | Suggested sample User: <user>, representing the business role Administrator-Legal Content ManagementPassword: <password> |
| Legal Counsel | SAP_BR_LEGAL_COUNSEL | Legal Counsel - Enterprise Contract Management | SAP_BR_LEGAL_COUNSEL | Suggested sample User: <user>, representing the business role Legal CounselPassword: <password> |
| Employee - Enterprise Contract Management | SAP_BR_EMPLOYEE_LEGAL_CONTENT | Self-Services - Enterprise Contract Management | SAP_LCM_SPT_EMPLOYEE_LGL_CNTNT_PC | Suggested sample User: <user>, representing the business role Employee - Legal Content ManagementPassword: <password> |
| Business Process Specialist | SAP_BR_BUSINESS_PROCESS_SPEC | Business Process Management / Business Process Management | SAP_BR_BUSINESS_PROCESS_SPEC / SAP_CA_SPT_BPS_PC |  |

### Additional Manual Configuration

Before you can test this scope item, you must have completed the additional configuration steps that are described in the Set-Up Instructions for this scope item. These configuration steps are specific for your implementation and include mandatory settings that are not delivered by SAP and must be created by you. For more information, follow the link to the document:

[Link to Set-Up Instructions](https://help.sap.com/docs/SAP_S4HANA_BEST_PRACTICES/55e8dc0b813411102623e7ac5efbcc4e)

### Business Conditions

Before this scope item can be tested, the following business conditions must be met.

| Scope Item ID | Business Condition |
| --- | --- |
| 31N – Situation Handling | If you want to create your own situation type for phases of legal transaction as described in [Preliminary Steps](#unique_7) [page ] 5, scope item 31N - Situation Handling must be activated. |

### Preliminary Steps

#### Manage Situation Types

Purpose

You can refer to the standard delivered template, create your own situation type for phases of legal transaction. With the configured situation, a notification is sent to the predefined recipients when the status of the phase is changed from Completed to Completed (Revision Needed).

|  |
| --- |
| Note If you want to execute this step, please make sure scope item 31N - Situation Handling is activated. |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log onto Fiori Launchpad | Log onto the SAP Fiori launchpad as a Business Process Specialist. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the App | Open Manage Situation Types (F2947). | The Manage Situation Types screen is displayed. |  |
| 3 | Select the template to copy | Choose Situation Template and choose Go to search the Situation Templates:You may choose one situation template or more than one templates at a time. The available situation templates are as follows:LCM_PHASE_STATUS_CHANGELCM_RELATIONSHIP_HEALTH_FAILURELCM_RELATIONSHIP_HEALTH_TRIGGERLCM_DOC_CNTNT_CPY_FAILEDLCM_DOC_CNTNT_CPY_PENDINGChoose Copy. | The New Situation Type screen will display when one template is copied.The Situation Types tab will display when multiple templates are copied at the same time. |  |
| 4 | Create Custom Situation Type | Go to the New Situation Type screen. If you chose more than one template, choose any copied situation type in the step above to go to the New Situation Type screen. Under the Admin Information tab, make the following entries and choose Create:ID: Z_LCM_PHASE_STATUS_CHANGEName: Status of Completed Phase ChangedOn the Conditions tab, the field Process Order 1 and filters Governing Law and Profile are predefined.Note The condition in this template defines that a situation is created with status Open when the status of one or more phases have been changed to Completed (Revision Needed), and a notification is sent. Filter parameters such as governing law and profile are also predefined in the situation template. You can use these filters, for example, if you want situations to be triggered for a specific team of experts with the specified governing law and profile.On the Batch Job Scheduling tab, make the following entries:Time Zone: for example, UTC+1Start Batch Job At: for example, 22:00On the Recipients tab and in the Responsibility by Teams section, the following entries are predefined:Team Category: LCM CategoryFilter by Responsibility Definition: Profile, Governing Law IDFilter by Member Function: BlankNote The predefined settings in this template determine that the notification addresses only members of the LCM Category team category. You can also use the predefined filters Governing Law and Profile to narrow down the recipients. For example, if the legal transaction is available for Governing Law IN and Profile GENERIC, only team members assigned with these attributes will be notified. | The situation type is created. |  |
| 5 | Enable situation type | Choose Yes when dialog box Enable Situation Type is displayed. |  |  |

#### Create Categories

Purpose

Setting up Categories is required to classify a transaction in the most exact way and to identify the templates and text blocks, which fit to a transaction by comparing the categories between those objects. In the following test script, you are creating an example of procurement for setting up Categories.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori launchpad as an Administrator - Enterprise Contract Management. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the appropriate Fiori app | Open the Categories - for Legal Contract (F2710) app under Administration. | The Categories screen is displayed. |  |
| 3 | Categories | In the Categories page, choose Create to create an object. | The Category screen is displayed. |  |
| 4 | New Object Header | Enter a Name, for example, Procurement.Choose the Purpose from dropdown list as your requirement, for example, Legal Transaction Category or Legal Document Category. |  |  |
| 5 | General Information | In the General Information section, make the following entries:Multi-Selectable Values: Select the checkbox. |  |  |
| 6 | Create | Choose Create to create the object. | The values Type Root and Category Level 0 are added automatically. The value for Obsolete is by default No.It then navigates to the Categories table where Root Procurement is created. |  |
| 7 | Find Your Category | Choose the category created in the previous steps. | The Procurement category is displayed. |  |
| 8 | Object Page | Then go to the Children subsection.Choose Create .Note For an existing root category, it is possible to generate dynamic child categories using the Generate Categories from Table option. Some default options are delivered by SAP, and new option could also be customized via the SSCUI/ Configuration Activities - Define Category Models as mentioned in section [Configure Self-Service Configuration UIs/ Configuration Activities](#unique_10) [page ] 9 below. | The Category screen is displayed. |  |
| 9 | New Object | In the Header section:For Name, enter IT Hardware for example.In the General Information section:Selectable: Select the checkbox.Choose Create. | The Procurement category is displayed. In the Children section, a new category is available.Category: IT HardwareType: LeafLevel: 1 |  |
| 10 | Repeat | Repeat steps 8 and 9 for creation of one more Children. For example, Name: Stationery | The Procurement category is displayed. In the Children section, a new category is available:Category: StationeryType: LeafLevel: 1 |  |
| 11 | In section Children | Under Category, choose IT Hardware. | It navigates to the IT Hardware object page |  |
| 12 | Object page | Choose Create to add two Children to IT Hardware, for example PCs and Mobile Phones. | Finally, under IT Hardware category, you should have two Children as follows:Category: PCsType: LeafLevel: 2Category: Mobile PhonesType: LeafLevel: 2When you go to the Procurement category, you will see the following under the Children section:Category: IT HardwareType: NodeLevel: 1 |  |
| 13 | Categories | Go back to the Categories screen. | The table should have the following entries:ProcurementType: RootIT HardwareType: NodePCsType: LeafMobile PhonesType: Leaf |  |

#### Configure Self-Service Configuration UIs/ Configuration Activities

Depending on your configuration environment for SAP S/4HANA Cloud Public Edition, choose one of the following options:

Configure Your Solution:

Purpose

You can use self-service configuration UIs to tailor the pre-configured processes to your business requirements. Proceed with the configuration in the suggested sequence.

List of the available self-service configuration UIs for SAP S/4HANA Cloud Public Edition, enterprise contract management:

| Sequence | Configuration UI | Description |
| --- | --- | --- |
| 1 | Define Reminder Type | Define types of reminders and corresponding template ID for each reminder. It is used for determining the template for emails which will be sent for the user in case a reminder was added in the Legal Transaction app. |
| 2 | Define Date Types | Define types of dates (periods). It is used in Context/Legal Transaction apps for determining kinds of necessary/important dates. |
| 3 | Define Internal Contacts | Define types of users/business partners which are used in Context/Legal Transaction apps as internal contacts. |
| 4 | Define External Contacts | Define types of users/business partners which are used in Context/Legal Transaction apps as external contacts. |
| 5 | Define Entity Types | Define types of entities in Context/Legal Transaction apps. These can be customer, supplier, sales org and so on. |
| 6 | Define Linked Object Types | Define types of objects which are used in Context/Legal Transaction apps as links(for navigation). |
| 7 | Define Access Level | Define the access level that influences the accessibility of the legal transactions. |
| 8 | Define Relationship Types, Relationships, and Use Cases | Define relationships, relationship types and use cases for defined relations for legal contexts and legal transactions. |
| 9 | Define Renewal or Termination Clauses | Define renewal or termination clauses for legal contexts and legal transactions. |
| 10 | Define Technical Types for Linked Object Types | Define the technical types for the linked objects that are used for legal transactions. |
| 11 | Define Phase Types | Define different types of phases of a legal transaction. These phases define the various stages in the life cycle of a legal transaction. |
| 12 | Define Content Types | Define types of content which are used in Documents app. |
| 13 | Define Document Amendment Types | Maintain the amendment types for the contracts. Once these types are defined, the users can select the type of amendment the contracts as per the business needs. |
| 14 | Define Document Stamps | Define types of stamps which can be created for the document in Documents app. |
| 15 | Define Obligation Types | Define the obligation types. This configuration enables the legal counsel to maintain and track the fulfillment of a legal obligation. |
| 16 | Define Profiles | Define profiles for Context/Legal Transaction apps for restriction visibility of data sets (internal/external contacts, entities, linked objects…) |
| 17 | Define Category Qualifier and Property | Define the category qualifiers and scope of the category required to generate dynamic categories using the generate categories from table option in the app categories. |
| 18 | Define Category Models | Define the category models required to generate dynamic categories using the Generate Categories from table option in the app Categories. |
| 19 | Define Filters for Custom Step | Define the filters for a business case that can be used within a workflow that contains a custom step task. |
| 20 | Enable Switch for Business Object Integration | Enable the switch to activate the business object integration. |
| 21 | Define Integration Variants | Define the attributes required for business object integration |
| 22 | Maintain System Type | Maintain the system type for multi-source integration of Enterprise Contract Management. |
| 23 | Enable Switch for Collaboration with Microsoft Teams | Enable the switch to activate integration with Microsoft Teams. |
| 24 | Maintain Retention Period for Collaboration Platforms | Maintain the retention period in days for the collaboration application. |
| 25 | Define Default Values for Legal Contracts | Define default values for legal contracts, based on your business needs. |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori launchpad as a Configuration Expert. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the app | Open Manage Your Solution. | The Manage Your Solution screen is displayed. |  |
| 3 | Filter the Configuration UIs of LCM | On the Manage Your Solution screen, choose Configure Your Solution.On the Configure Your Solution screen, set the filters in the search bar:Application Area: Application Platform and InfrastructureSub Application Area: Enterprise Contract Management and AssemblyChoose one of the entries and the configuration UIs are displayed. | The list of Self-Service Configuration UIs are displayed. |  |
| 4 | Define Reminder Types (Optional) | On the Configure Your Solution screen, choose the item name Legal Transaction. The configuration UIs for Legal Transaction are displayed.Navigate to the step name Define Reminder Types on the right part of the screen and choose Configure.On the Define Reminder Types: Change screen, choose New Entries and make the following entries:Reminder Type: <enter a reminder type ID>Long Text: <enter a reminder type name>Email Template ID: <choose an email template ID>Rem. Rel.: <choose a reminder relationship>Choose Save. | Reminder Types are defined. |  |
| 5 | Define Date Types (Recommended) | On the Configure Your Solution screen, choose the item name Legal Transaction and the configuration UIs for Legal Transaction are displayed.Navigate to the step name Define Date Types on the right part of the screen. Choose Configure.On the Define Date Types: Change screen, choose New Entries and make the following entries:Date Type: <enter a date type ID>Data Type Name: <enter a date type name>TURE: <mark the checkbox if the date type denotes a period, or don’t mark if it is a single date>Choose Save. | Date Types are defined. |  |
| 6 | Define Internal Contacts (Recommended) | On the Configure Your Solution screen, choose the item name Legal Transaction and the configuration UIs for Legal Transaction are displayed.Navigate to the step name Define Internal Contacts on the right part of the screen. Choose Configure.On the Define Internal Contacts: Change screen, choose New Entries and make the following entries:Contact Type: <enter a contact ID>Long Text: <enter a contact name>Function: <define the functions in responsibility management, and maintain the mapping relationship here>Choose Save. | Internal Contacts are defined. |  |
| 7 | Define External Contacts (Recommended) | On the Configure Your Solution screen, choose the item name Legal Transaction and the configuration UIs for Legal Transaction are displayed.Navigate to the step name Define External Contacts on the right part of the screen. Choose Configure.On the Define External Contacts: Change screen, choose New Entries and make the following entries:Contact Type: <enter a contact ID>Long Text: <enter a contact name>Choose Save. | External Contacts are defined. |  |
| 8 | Define Entity Types (Recommended) | On the Configure Your Solution screen, choose the item name Legal Transaction and the configuration UIs for Legal Transaction are displayed.Navigate to the step name Define Entity Types on the right part of the screen. Choose Configure.On the Define Entity Types: Change screen, choose New Entries and make the following entries:Entity Type: <enter an entity type ID>Long Text: <enter an entity type name>Entity TTp: <choose a technical entity type>Note If the entity type is defined as business partner, the following activity is also required to define a BP role, otherwise this entity type will not work properly in the business process.Choose the defined entity type, double-click on the acivity Define Business Partner Role on the left.On the Change View “Define Business Partner Role”: Overview screen, choose New Entries and make the following entries:BP Role: <enter a valid BP role>Choose Save. | Entity Types are defined. |  |
| 9 | Define Linked Object Types (Optional) | On the Configure Your Solution screen, choose the item name Legal Transaction and the configuration UIs for Legal Transaction are displayed.Navigate to the step name Define Linked Object Types on the right of the screen. Choose Configure.On the Define Linked Object Types: Change screen, choose New Entries and make the following entries:LnkObj. Ty: <enter a linked object type ID>Long Text: <enter a linked object type name>LnkObj. TTp: <enter a linked object technical type>Integr.Lnk(optional): <choose a integrated document type>Choose Save. | Linked Object Types are defined. |  |
| 10 | Define Access Level (Recommended) | On the Configure Your Solution screen, choose the item name Legal Transaction and the configuration UIs for Legal Transaction are displayed.Navigate to the step name Define Access Level on the right part of the screen. Choose Configure.On the Define Access Level: Change screen, choose New Entries and make the following entries:Acs. Lvl.Long TextCONFConfidentialPRIVPrivatePUBLPublicChoose Save.Note Access level is not predefined by SAP. | Access Levels are defined. |  |
| 11 | Define Relationship Types, Relationships, and Use Cases (Recommended) | On the Configure Your Solution screen, choose the item name Legal Transaction and the configuration UIs for Legal Transaction are displayed.Navigate to the step name Define Relationship Types, Relationships, and Use Cases on the right part of the screen. Choose Configure.On the Define Relationship Types, Relationships, a..: Change screen, choose New Entries and make the following entries:Rel. TypeRel. Drtn.Relationship Type NameCASCNeutralAssociated toCDCCWeakAmendment toCDCPStrongAmended ByCHLDWeakChild ofPARNStrongParent ofChoose Define Relationships on the left.Choose New Entries and make the following entries:Rel. NameForward Rel. Typ.Reverse Rel. Typ .Rel. Desc.CASCCASCCASCAssociated to-Associated toCDOCCDCPCDCCDoc Link Parent ChildPACHPARNCHLDParent of - Child ofChoose the entry of CASC and choose Define Use Cases for Relationships on the left. Choose New Entries and make the following entries:Rel. Name: CASCRel. Use Case: SSTSGo back to Define Relationships, choose the entry of CDOC and choose Define Use Cases for Relationships on the left.Choose New Entries and make the following entries:Rel. NameRel. Use CaseCDOCSDCCCDOCSDCPGo back to Define Relationships, choose the entry of PACH and choose Define Use Cases for Relationships on the left.Choose New Entries and make the following entries:Rel. Name: PACHRel. Use Case: SSTSChoose Save.Note Relationship types, relationships, and use cases are not predefined by SAP. | Relationship Types, Relationships, and Use Cases are defined. |  |
| 12 | Define Renewal or Termination Clauses (Recommended) | On the Configure Your Solution screen, choose the item name Legal Transaction and the configuration UIs for Legal Transaction are displayed.Navigate to the step name Define Renewal or Termination Clauses on the right part of the screen. Choose Configure.On the Define Renewal or Termination Clauses: Change screen, choose New Entries and make the following entries:Clause Typ: <choose a clause type>Time in Ad: <enter a number of the period>Unit: <choose a period unit>Clause Ref: <choose a clause reference>Obsolete: <mark the checkbox if the caluse is obsolete>Long Text: <enter a description>Choose Save. | Renewal or termination clauses are defined. |  |
| 13 | Define Technical Types for Linked Object Types (Optional) | On the Configure Your Solution screen, choose the item name Legal Transaction and the configuration UIs for legal transaction are displayed.Navigate to the step name Define Technical Types for Linked Object Types on the right part of the screen. Choose Configure.On the Define Technical Types for Linked Object Ty..: Change screen, choose New Entries and make the following entries:Lnk. Obj. Tech. Typ.: <enter a linked object technical name>Lnk. Obj. Tech. Cat.: <choose a linked object technical category>If the linked object techincial type is Internal SAP, continue to make the following entries:Business Entity: <enter a business entity>Semantic Object: <enter a semantic object>Semantic Object Attr.: <enter a semantic object attribute>Intent Action: <enter an intent action>Text Field: <enter the text field which is exposed in the CDS/Business Entity maintained above, it could be chosen using F4 key/value help>Note For example, if you want to integrate with WBS Elements as internal linked object type, please refer to the following picture to fill in the parameters.<!-- image omitted: unnamed -->If the linked object technical type is External, continue to make the following entries:Comm. Arr. Name: <enter a communication arrangement name>Choose Save. | Technical Types for Linked Object Types are defined. |  |
| 14 | Define Phase Types (Optional) | On the Configure Your Solution screen, choose the item name Legal Transaction. The configuration UIs for Legal Transaction are displayed.Navigate to the step name Define Phase Types on the right side of the screen and choose Configure.On the Define Phase Types: Change screen, choose New Entries and make the following entries:Phase TypeDescription of Phase Type1Review2NegotiationChoose Save.Note Phase Type is not predefined by SAP. | Phase Types are defined. |  |
| 15 | Define Content Types (Recommended) | On the Configure Your Solution screen, choose the item name Legal Documents and the configuration UIs for legal documents are displayed.Navigate to the step name Define Content Types on the right of the screen. Choose Configure.On the Define Content Types: Change screen, choose New Entries and make the following entries:Cont. Type: <enter a content type ID>Long Text: <enter a content type name>Choose Save. | Content types are defined. |  |
| 16 | Define Document Amendment Types (Optional) | On the Configure Your Solution screen, choose the item name Legal Documents. The configuration UIs for legal documents are displayed.Navigate to the item name Define Document Amendment Types on the right side of the screen. Choose Configure.On the Define Document Document Amendment Types: Change screen, choose New Entries and make the following entries:Amnt. Type: <enter an amendment type ID>Amendment Type Name: <enter an amendment type name>Choose Save. | Amendment types are defined. |  |
| 17 | Define Document Stamps (Optional) | On the Configure Your Solution screen, choose the item name Legal Documents and the configuration UIs for legal documents are displayed.Navigate to the step name Define Document Stamps on the right of the screen. Choose Configure.On the Define Document Stamps: Change screen, choose New Entries and make the following entries:Stamp Name: <enter a stamp ID>Long Text: <enter a stamp name>Choose Save. | Document stamps are defined. |  |
| 18 | Define Obligation Types (Optional) | On the Configure Your Solution screen, choose the item name Legal Documents. The configuration UIs for legal documents are displayed.Navigate to the step name Define Obligation Types on the right side of the screen, choose Configure.On the Define Obligation Types: Change screen, choose New Entries and make the following entries:Obligation TypeDescription of Obligation TypeCANCCancellation PolicyDDPDelivery MethodPYTMPayment TermChoose Save.Note Obligation type is not predefined by SAP. | Obligation Types are defined. |  |
| 19 | Define Profiles (Optional) | On the Configure Your Solution screen, choose the item name Legal Profiles and the configuration UIs for Legal Profiles are displayed.Navigate to the step name Define Profileson the right part of the screen. Choose Configure.On the Define Profiles: Changescreen, choose New Entries and make the following entries:Prf. Set: <enter a set ID>Set Type: <choose a set type>Long Text: <enter a set name>Repeat the step above for all sets and add your newly created elements (internal contacts, external contacts, dates, linked objects, reminders and document contents).Note Define sets should be maintained to associated sets.For example: entity should be defined under entities structure. The same rule applies for all the sets.Choose Define Profiles on the left, and make the following entries:Profile: <enter a profile name>Long Text: <enter a description>Entity Set: <enter the defined entity set>InCnt. Set: <enter the defined internal contact set>ExCnt. Set: <enter the defined external contact set>Date Set: <enter the defined date set>LObj. Set: <enter the defined linked object set>Rmndr. Set: <enter the defined reminder set>Doc.Cn.Set: <enter the defined document content set>Choose Save. | Profiles are defined. |  |
| 20 | Define Category Qualifier and Property (Optional) | On the Configure Your Solution screen, choose the item name Legal Categories, the configuration UIs for Legal Categories are displayed.Navigate to the step name Define Category Qualifier and Property on the right of the screen, choose Configure.On the Define Category Qualifier and Property: Change screen, choose New Entries and make the following entries:Category Qualifier: <enter the category qualifier ID>Category Qualifier Name: <enter the category qualifier name>Choose Define Qualifier Hierarchies screen, select New Entries and make the following entries:Category Qualifier: <enter a valid category qualifier ID>Parent Category Qualifier: <enter a valid category qualifier ID as parent>Description: <enter the description of this qualifier hierarchy>IsMultiSel: <check if required>Is Select: <check if required>Obsolete: <check if it is obsolete>Choose Define Property for Automatic Classification, select New Entries and make the following entries:Prprt. ID: <enter the proerty ID>Prprt. Type: <select the property type from the dropdown list>Prpt. Value: <enter a valid value of the category scope>Dim. Value Text: <enter the property value text>Parent Category Qualifier: <enter a valid category qualifier ID which is defined as parent category qualifier>Category Qualifier: <enter a valid category qualifier ID>Choose Save.NoteYou cannot delete a category qualifier once it is used in the activity Define Qualifier Hierarchies.Only root category qualifiers can be marked as IsMultiSel.Only parent or node category qualifiers can be marked as Is Select.Changes after execution of synchronization report can be raised due to inconsistency data in the system. If the category qualifiers are deleted or marked as obsolete, then after execution of the synchronization report then all node elements and this element will be marked as obsolete in dictionary of categories.The category qualifier hierarchies cannot be deleted when in use in the activity Define Property for Automatic Classification.For property types Content Type and Integration Variable, the value of the field Property Value must be filled. For property type All documents the field can be left empty without a value.In the field Category Qualifier, you can enter only the category qualifiers from the activity Define Qualifier Hierarchies, and which have the indicator Is Select. Providing the category qualifiers without this flag are not restricted. | Category Qualifier and Property are defined. |  |
| 21 | Define Category Models (Optional) | On the Configure Your Solution screen, choose the item name Legal Categories, the configuration UIs for Legal Categories are displayed.Navigate to the step name Define Category Models on the right of the screen, choose Configure.On the Define Category Models: Change screen, choose New Entries and make the following entries:DDL Source Name: <enter athe CDS view name>Model: Key Field Name: <enter the key field name>Model: Descr. Field Name: <enter the description field name>Long Text: <enter a the long text if required>Choose Save. | Category models are defined. |  |
| 22 | Define Filters for Custom Step (Optional) | On the Configure Your Solution screen, choose the item name Legal Workflow, the configuration UIs for legal workflow are displayed.Navigate to the step name Define Filters for Custom Step on the right of the screen, choose Configure.On the Define Filters for Custom Step: Change screen, choose New Entries and make the following entries:CustStFID: <enter the ID>Long Text: <enter the long text>Choose Save. | Filters for custom step are defined. |  |
| 23 | Enable Switch for Business Object Integration (Optional) | On the Configure Your Solution screen, choose the item name Integration with Business Objects, the configuration UIs for Integration with business objects are displayed.Navigate to the step name Enable Switch for Business Object Integration on the right of the screen, choose Configure.On the Enable Switch for Business Object Integration: Change screen, choose New Entries and make the following entries:Business Feature ID: for example, LCM_BOINTEGRATIONFtr State: for example, ActiveChoose Save.Note This step is only for the business object integration. For example, the scope item 4RD - Direct Material Sourcing is a best practice delivered since 2108 which enables the real use case of integration between ECM and souring project. The business feature LCM_BOINTEGRATION must be active during the integration setup. | The Business Feature of Business Object Integation is defined. |  |
| 24 | Define Integration Variants (Opitonal) | Note Same as above, this step is only for the business object integration.On the Configure Your Solution screen, choose the item name Integration with Business Objects, the configuration UIs for integration with business objects are displayed.Navigate to the step name Define Integration Variants on the right of the screen, choose Configure.On the Define Integration Variants: Change screen, choose New Entries and make the following entries:Identifying Attributes: <enter the identifying attribute ID>Description: <enter the description of the identifying attribute>CDS View Source: <enter a valid CDS view source to fetch the identifying attribute values>Technical Field Name: <enter a technical name from the CDS view to map the identifying attribute>Text of Technical Field Name: <enter the technical type text name from the CDS view if available>Choose Define Integration Variant, select New Entries and make the following entries:Int. Var.: <enter the integration variant ID>Description: <enter the description of the integration variant>Integr.Lnk: <select the integration link which is a predefined set of values>Main Org: <choose a main org type from the dropdown list>Profile: <select the Profile against which the context can be created>Active: <check the active flag if the integration variant adheres to all the rules defined>Choose the defined integration variant, double-click on the activity Map Integration Variant to Identifying Attributes.Choose New Entries and make the following entries:Identifying Attributes: <enter the existing identifying attribute ID>Choose Enter.Doule-click on the activity Map Variants to Integration Variant .Choose New Entries and make the following entries:Note If a mapping variable is maintained for the selected integration variant in the system table as delivered by SAP, then the same has to be imported into the custom configuration using the Import System Fields button during creation of new entries. The description, set type and the technical type of the system mapping variables are not editable.Integration Mapping Variable: <enter the integration mapping variable ID>Description: <enter the description of the integration mapping variable>Set Type: <select the set type from the dropdown list>Technical Type of Set: <enter a valid technical type>Value of Set Type: <enter a valid value of set type>NoteValue of Set Type and Technical Type of Set is not mandatory during save but mandatory during the activation of the integration variant.Choose Save. | Integraton Variants are defined. |  |
| 25 | Maintain System Type (Optional) | On the Configure Your Solution screen, choose the item name Basic Settings for Multisource Integration, the configuration UIs for basic settings for multisource integration are displayed.Navigate to the step name Maintain System Types on the right of the screen, choose Configure.On the Change View "Maintain System Type": Overview screen, choose New Entries and in the field System Type, select the required system type Unclassified, Hub, or Connected.Note The step is only for the multi-source integration of Enterprise Contract Management.The default value of system type is Unclassified. More information about the integration please refer to the related sections of setup instructions. | System type is maintained. |  |
| 26 | Enable Switch for Collaboration with Microsoft Teams (Optional) | On the Configure Your Solution screen, choose the item name Integration with Collaboration Platforms, the configuration UIs for integration with collaboration platforms are displayed.Navigate to the step name Enable Switch for Collaboration with Microsoft Teams on the right of the screen, and choose Configure.On the Display/Change State of Business Function screen, choose Change State to switch the state of the business function.Note The step is only for Microsoft Teams integration. For more information about integration, please refer to related sections of set-up instructions. The business function is in Off state by default. | The integration switch is activated. |  |
| 27 | Maintain Retention Period for Collaboration Platforms (Optional) | On the Configure Your Solution screen, choose the item name Integration with Collaboration Platforms, the configuration UIs for integration with collaboration platforms are displayed.Navigate to the step name Maintain Retention Period for Collaboration Platforms on the right of the screen, choose Configure.On the Change View “Maintain Retention Period for Collaboration..”: Overview screen, choose New Entries and make the following entries:Platform: Microsoft TeamsRtntn Days: for example, 90Choose Save.Note The step is only for collaboration application integration, for example, Microsoft Teams inegration. | The retention period is maintained. |  |
| 28 | Define Default Values for Legal Contracts (Optional) | On the Configure Your Solution screen, choose the item name Legal Transactions, the configuration UIs for integration with collaboration platforms are displayed.Navigate to the step name Define Default Values for Legal Contracts on the right of the screen, choose Configure.On the Define Default Values for Legal Contracts: Change screen, choose New Entries and make the following entries:Sign Pref: for example, SR Signature RelevantLong Text: for example, Signature RelevantChoose Save. | The default values for legal contracts are maintained. |  |

SAP Central Business Configuration

Purpose

You can use these configuration activities to tailor the pre-configured processes to your business requirements. Proceed with the configuration in the suggested sequence.

List of the available configuration activities:

Log on to the project experience in SAP Central Business Configuration.

Go to the Configuration app. Search for the following configuration activities and choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration.

| Sequence | Configuration UI | Description |
| --- | --- | --- |
| 1 | Define Reminder Type | Define types of reminders and corresponding template ID for each reminder. It is used for determining the template for emails which will be sent for the user in case a reminder was added in the Legal Transaction app. |
| 2 | Define Date Types | Define types of dates (periods). It is used in Context/Legal Transaction apps for determining kinds of necessary/important dates. |
| 3 | Define Internal Contacts | Define types of users/business partners which are used in Context/Legal Transaction apps as internal contacts. |
| 4 | Define External Contacts | Define types of users/business partners which are used in Context/Legal Transaction apps as external contacts. |
| 5 | Define Entity Types | Define types of entities in Context/Legal Transaction apps. These can be customer, supplier, sales org and so on. |
| 6 | Define Linked Object Types | Define types of objects which are used in Context/Legal Transaction apps as links(for navigation). |
| 7 | Define Access Level | Define the access level that influences the accessibility of the legal transactions. |
| 8 | Define Relationship Types, Relationships, and Use Cases | Define relationships, relationship types and use cases for defined relations for legal contexts and legal transactions. |
| 9 | Define Renewal or Termination Clauses | Define renewal or termination clauses for legal contexts and legal transactions. |
| 10 | Define Technical Types for Linked Object Types | Define the technical types for the linked objects that are used for legal transactions. |
| 11 | Define Phase Types | Define different types of phases of a legal transaction. These phases define the various stages in the life cycle of a legal transaction. |
| 12 | Define Content Types | Define types of content which are used in Documents app. |
| 13 | Define Document Amendment Types | Maintain the amendment types for the contracts. Once these types are defined, the users can select the type of amendment the contracts as per the business needs. |
| 14 | Define Document Stamps | Define types of stamps which can be created for the document in Documents app. |
| 15 | Define Obligation Types | Define the obligation types. This configuration enables the legal counsel to maintain and track the fulfillment of a legal obligation. |
| 16 | Define Profiles | Define profiles for Context/Legal Transaction apps for restriction visibility of data sets (internal/external contacts, entities, linked objects…) |
| 17 | Define Category Qualifier and Property | Define the category qualifiers and scope of the category required to generate dynamic categories using the generate categories from table option in the app categories. |
| 18 | Define Category Models | Define the category models required to generate dynamic categories using the Generate Categories from table option in the app Categories. |
| 19 | Define Filters for Custom Step | Define the filters for a business case that can be used within a workflow that contains a custom step task. |
| 20 | Enable Switch for Business Object Integration | Enable the switch to activate the business object integration. |
| 21 | Define Integration Variants | Define the attributes required for business object integration |
| 22 | Maintain System Type | Maintain the system type for multi-source integration of Enterprise Contract Management. |
| 23 | Enable Switch for Collaboration with Microsoft Teams | Enable the switch to activate integration with Microsoft Teams. |
| 24 | Maintain Retention Period for Collaboration Platforms | Maintain the retention period in days for the collaboration application. |

| Test Step # | Configuratiion Activity Steps | Instruction | Expected Result | Comment |
| --- | --- | --- | --- | --- |
| 1 | Define Reminder Types (Optional) | On the Define Reminder Types: Change screen, choose New Entries and make the following entries:Reminder Type: <enter a reminder type ID>Long Text: <enter a reminder type name>Email Template ID: <choose an email template ID>Rem. Rel.: <choose a reminder relationship>Choose Save. | Reminder Types are defined. |  |
| 2 | Define Date Types (Recommended) | On the Define Date Types: Change screen, choose New Entries and make the following entries:Date Type: <enter a date type ID>Long Text: <enter a date type name>TURE: <mark the checkbox if the date type denotes a period, or don’t mark if it is a single date>Choose Save. | Date Types are defined. |  |
| 3 | Define Internal Contacts (Recommended) | On the Define Internal Contacts: Change screen, choose New Entries and make the following entries:Cntct Type: <enter a contact ID>Long Text: <enter a contact name>Function: <define the functions in Responsibility Management, and maintain the mapping relationship here>Choose Save. | Internal Contacts are defined. |  |
| 4 | Define External Contacts (Recommended) | On the Define External Contacts: Change screen, choose New Entries and make the following entries:External Contact Type: <enter a contact ID>Long Text: <enter a contact name>Choose Save. | External Contacts are defined. |  |
| 5 | Define Entity Types (Recommended) | On the Define Entity Types: Change screen, choose New Entries and make the following entries:Entity Type: <enter an entity type ID>Long Text: <enter an entity type name>Entity Techn Type: <choose a technical entity type>Note If the entity type is defined as business partner, the following activity is also required to define a BP role, otherwise this entity type will not work properly in the business process.Choose the defined entity type, double-click on the acivity Define Business Partner Role.Choose New Entries and make the following entry:BP Role: <enter a valid BP role>Choose Save. | Entity Types are defined. |  |
| 6 | Define Linked Object Types (Optional) | On the Define Linked Object Types: Change screen, choose New Entries and make the following entries:Linkec Object Type: <enter a linked object type ID>Long Text: <enter a linked object type name>LnkObj. TTp: <enter a linked object technical type>Integr.Lnk(optional): <choose a integrated document type>Choose Save. | Linked Object Types are defined. |  |
| 7 | Define Access Level (Recommended) | On the Define Access Level: Change screen, choose New Entries and make the following entries:Acs. Lvl.Long TextCONFConfidentialPRIVPrivatePUBLPublicChoose Save.Note Access level is not predefined by SAP. | Access Levels are defined. |  |
| 8 | Define Relationship Types, Relationships, and Use Cases (Recommended) | On the Define Relationship Types, Relationships, a..: Change screen, choose New Entries and make the following entries:Rel. TypeRel. Drtn.Relationship Type NameCASCNeutralAssociated toCDCCWeakAmendment toCDCPStrongAmended ByCHLDWeakChild ofPARNStrongParent ofChoose Define Relationships on the left.Choose New Entries and make the following entries:Rel. NameForward Rel. Typ.Reverse Rel. Typ .Rel. Desc.CASCCASCCASCAssociated to-Associated toCDOCCDCPCDCCDoc Link Parent ChildPACHPARNCHLDParent of - Child ofChoose the entry of CASC and choose Define Use Cases for Relationships. Choose New Entries and make the following entries:Rel. Name: CASCRel. Use Case: SSTSGo back to Define Relationships, choose the entry of CDOC and choose Define Use Cases for Relationships on the left.Choose New Entries and make the following entries:Rel. NameRel. Use CaseCDOCSDCCCDOCSDCPGo back to Define Relationships, choose the entry of PACH and choose Define Use Cases for Relationships on the left.Choose New Entries and make the following entries:Rel. Name: PACHRel. Use Case: SSTSChoose Save.Note Relationship types, relationships, and use cases are not predefined by SAP. | Relationship Types, Relationships, and Use Cases are defined. |  |
| 9 | Define Renewal or Termination Clauses (Recommended) | On the Define Renewal or Termination Clauses: Change screen, choose New Entries and make the following entries:Clause Typ: <choose a clause type>Time in Ad: <enter a number of the period>Unit: <choose a period unit>Clause Ref: <choose a clause reference>Obsolete: <mark the checkbox if the caluse is obsolete>Long Text: <enter a description>Choose Save. | Renewal or Termination Clauses are defined. |  |
| 10 | Define Technical Types for Linked Object Types (Optional) | On the Define Technical Types for Linked Object Ty..: Change screen, choose New Entries and make the following entries:Lnk. Obj. Tech. Typ.: <enter a linked object technical name>Lnk. Obj. Tech. Cat.: <choose a linked object technical category>If the linked object techincial type is Internal SAP, continue to make the following entries:Business Entity: <enter a business entity>Semantic Object: <enter a semantic object>Semantic Object Attr.: <enter a semantic object attribute>Intent Action: <enter an intent action>Text Field: <enter the text field which is exposed in the CDS/Business Entity maintained above, it could be chosen using F4 key/value help>Note For example, if you want to integrate with WBS Elements as internal linked object type, please refer to the following picture to fill in the parameters.<!-- image omitted: unnamed -->If the linked object technical type is External, continue to make the following entries:Comm. Arr. Name: <enter a communication arrangement name>Choose Save. | Technical Types for Linked Object Types are defined. |  |
| 11 | Define Phase Types (Optional) | On the Define Phase Types: Change screen, choose New Entries and make the following entries:TypeDescription of Phase Type1Review2NegotiationChoose Save.Note Phase type is not predefined by SAP. | Phase Types are defined. |  |
| 12 | Define Content Types (Recommended) | On the Define Content Types: Change screen, choose New Entries and make the following entries:Content Type: <enter a content type ID>Long Text: <enter a content type name>Choose Save. | Content Types are defined. |  |
| 13 | Define Document Amendment Types (Optional) | On the Define Document Document Amendment Types: Change screen, choose New Entries and make the following entries:Amnt. Type: <enter an amendment type ID>Amendment Type Name: <enter an amendment type name>Choose Save. | Amendment types are defined. |  |
| 14 | Define Document Stamps (Optional) | On the Define Document Stamps: Change screen, choose New Entries and make the following entries:Stamp Name: <enter a stamp ID>Long Text: <enter a stamp name>Choose Save. | Document Stamps are defined. |  |
| 15 | Define Obligation Types (Optional) | On the Define Obligation Types: Change screen, choose New Entries and make the following entries:Obligation TypeDescription of Obligation TypeCANCCancellation PolicyDDPDelivery MethodPYTMPayment TermChoose Save.Note Obligation type is not predefined by SAP. | Obligation Types are defined. |  |
| 16 | Define Profiles (Optional) | On the Define Profiles: Change screen, choose New Entries and make the following entries:Prf. Set: <enter a set ID>Set Type: <choose a set type>Long Text: <enter a set name>Repeat the step above for all sets and add your newly created elements (internal contacts, external contacts, dates, linked objects, reminders and document contents).Note Define sets should be maintained to associated sets.For example: Entity should be defined under Entities structure. The same rule applies for all the sets.Choose Define Profiles, select New Entries and make the following entries:Profile: <enter a profile name>Long Text: <enter a description>Entity Set: <enter the defined entity set>InCnt. Set: <enter the defined internal contact set>ExCnt. Set: <enter the defined external contact set>Date Set: <enter the defined date set>LObj. Set: <enter the defined linked object set>Rmndr. Set: <enter the defined reminder set>Doc.Cn.Set: <enter the defined document content set>Choose Save. | Profiles are defined. |  |
| 17 | Define Category Qualifier and Property (Optional) | On the Configure Your Solution screen, choose the item name Legal Categories, the configuration UIs for Legal Categories are displayed.Navigate to the step name Define Category Qualifier and Property on the right of the screen, choose Configure.On the Define Category Qualifier and Property: Change screen, choose New Entries and make the following entries:Category Qualifier: <enter the category qualifier ID>Category Qualifier Name: <enter the category qualifier name>Choose Define Qualifier Hierarchies, select New Entries and make the following entries:Category Qualifier: <enter a valid category qualifier ID>Parent Category Qualifier: <enter a valid category qualifier ID as parent>Description: <enter the description of this qualifier hierarchy>IsMultiSel: <check if required>Is Select: <check if required>Obsolete: <check if it is obsolete>Choose Define Property for Automatic Classification, select New Entries and make the following entries:Prprt. ID: <enter the proerty ID>Prprt. Type: <select the property type from the dropdown list>Prpt. Value: <enter a valid value of the category scope>Dim. Value Text: <enter the property value text>Parent Category Qualifier: <enter a valid category qualifier ID which is defined as parent category qualifier>Category Qualifier: <enter a valid category qualifier ID>Choose Save.NoteYou cannot delete a category qualifier once it is used in the activity Define Qualifier Hierarchies.Only root category qualifiers can be marked as IsMultiSel.Only parent or node category qualifiers can be marked as Is Select.Changes after execution of synchronization report can be raised due to inconsistency data in the system. If the category qualifiers are deleted or marked as obsolete, then after execution of the synchronization report then all node elements and this element will be marked as obsolete in dictionary of categories.The category qualifier hierarchies cannot be deleted when in use in the activity Define Property for Automatic Classification.For property types Content Type and Integration Variable, the value of the field Property Value must be filled. For property type All documents the field can be left empty without a value.In the field Category Qualifier, you can enter only the category qualifiers from the activity Define Qualifier Hierarchies, and which have the indicator Is Select. Providing the category qualifiers without this flag are not restricted. | Category Qualifier and Property are defined. |  |
| 18 | Define Category Models (Optional) | On the Define Category Models: Change screen, choose New Entries and make the following entries:DDL Source Name: <enter athe CDS view name>Model: Key Field Name: <enter the key field name>Model: Descr. Field Name: <enter the description field name>Long Text: <enter a the long text if required>Choose Save. | Category models are defined. |  |
| 19 | Define Filters for Custom Step (Optional) | On the Define Filters for Custom Step: Change screen, choose New Entries and make the following entries:CustStFID: <enter the ID>Long Text: <enter the long text>Choose Save. | Filters for custom step are defined. |  |
| 20 | Enable Switch for Business Object Integration (Optional) | On the Enable Switch for Business Object Integration: Change screen, choose New Entries and make the following entries:Business Feature ID: for example, LCM_BOINTEGRATIONFtr State: for example, ActiveChoose Save.Note This step is only applicable for the business object integration. For example, the scope item 4RD - Direct Material Sourcing is a Best Practice delivered since 2108 which enables the real use case of integration between ECM and Souring Project. The business feature LCM_BOINTEGRATION must be active during the integration setup. | The Business Feature of Business Object Integation is defined. |  |
| 21 | Define Integration Variants (Opitonal) | Note Same as above, this step is only for the business object integration.On the Define Integration Variants: Change screen, choose New Entries and make the following entries:Identifying Attributes: <enter the identifying attribute ID>Description: <enter the description of the identifying attribute>CDS View Source: <enter a valid CDS view source to fetch the identifying attribute values>Technical Field Name: <enter a technical name from the CDS view to map the identifying attribute>Text of Technical Field Name: <enter the technical type text name from the CDS view if available>Choose Define Integration Variant, select New Entries and make the following entries:Int. Var.: <enter the integration variant ID>Description: <enter the description of the integration variant>Integr.Lnk: <select the integration link which is a predefined set of values>Main Org: <choose a main org type from the dropdown list>Profile: <select the Profile against which the context can be created>Active: <check the active flag if the integration variant adheres to all the rules defined>Choose the defined integration variant, double-click on the activity Map Integration Variant to Identifying Attributes.Choose New Entries and make the following entries:Identifying Attributes: <enter the existing identifying attribute ID>Choose Enter.Doule-click on the activity Map Variants to Integration Variant .Choose New Entries and make the following entries:Note If a mapping variable is maintained for the selected integration variant in the system table as delivered by SAP, then the same has to be imported into the custom configuration using the Import System Fields button during creation of new entries. The description, set type and the technical type of the system mapping variables are not editable.Integration Mapping Variable.: <enter the integration mapping variable ID>Description.: <enter the description of the integration mapping variable>Set Type.: <select the set type from the dropdown list>Technical Type of Set.: <enter a valid technical type>Value of Set Type.: <enter a valid value of set type>NoteValue of Set Type and Technical Type of Set is not mandatory during save but mandatory during the activation of the integration variant.Choose Save. | Integraton Variants are defined. |  |
| 22 | Maintain System Type (Optional) | On the Change View "Maintain System Type": Overview screen, choose New Entries and in the field System Type, select the required system type - Unclassified, Hub, or Connected.Note The step is only for the multi-source integration of Enterprise Contract Management.The default value of system type is Unclassified. More information about the integration please refer to the related sections of setup instructions. | System type is maintained. |  |
| 23 | Enable Switch for Collaboration with Microsoft Teams (Optional) | On the Display/Change State of Business Function screen, choose Change State to switch the state of the business function.Note The step is only for Microsoft Teams integration. For more information about integration, please refer to related sections of setup instructions. The business function is in Off state by default. | The integration switch is activated. |  |
| 24 | Maintain Retention Period for Collaboration Platforms (Optional) | On the Change View “Maintain Retention Period for Collaboration..”: Overview screen, choose New Entries and make the following entries:Platform: Microsoft TeamsRtntn Days: for example, 90Choose Save.Note The step is only for collaboration application integration, for example, Microsoft Teams inegration. | The retention period is maintained. |  |
| 25 | Define Default Values for Legal Contracts (Optional) | On the Configure Your Solution screen, choose the item name Legal Transactions, the configuration UIs for integration with collaboration platforms are displayed.Navigate to the step name Define Default Values for Legal Contracts on the right of the screen, choose Configure.On the Define Default Values for Legal Contracts: Change screen, choose New Entries and make the following entries:Sign Pref: for example, SR Signature RelevantLong Text: for example, Signature RelevantChoose Save. | The default values for legal contracts are maintained. |  |

## Overview Table

This scope item consists of several process steps provided in the table below.

|  |
| --- |
| Note If your system administrator has enabled spaces and pages on the SAP Fiori launchpad, the homepage will only contain the essential apps for performing the typical tasks of a business role.You can find all other (searchable) apps not included on the homepage using the search bar ([2434549](https://me.sap.com/notes/2434549)).If you want to personalize the homepage and include the hidden apps, navigate to your user profile and choose App Finder. |

| Process Step, Report, or Item | Business Role | App/Transaction | Expected Results |
| --- | --- | --- | --- |
| [Manage Context](#unique_12) [page ] 36 | Legal Counsel | Manage Contexts - for Legal Contract (F2346) | User is able to view context. |
| [Request Legal Contract](#unique_13) [page ] 42 | Employee - Enterprise Contract Management | Request Legal Contract (F2403) | User is able to view legal transactions. |
| [Manage Legal Transactions](#unique_14) [page ] 43 | Legal Counsel | Manage Legal Transactions (F2310) | User is able to edit the details. |
| [Approve Legal Transactions (Optional)](#unique_15) [page ] 48 | Employee - Enterprise Contract Management | My Inbox - All Items (F5331) | User is able to approve the transactions. |
| [Send Legal Document for Signature](#unique_16) [page ] 49 | Legal Counsel | Manage Legal Transactions (F2310) | Users can send legal documents that meet the criteria for signature. |
| [Envelope Status Update (Optional)](#unique_17) [page ] 51 | Administrator - Enterprise Contract Management | Schedule Envelope Status Updates (F4344) |  |
| [Manage Legal Documents](#unique_18) [page ] 52 | Legal Counsel | Manage Legal Documents (F2453) | User is able to edit the legal documents. |
| [Manage Legal Tasks](#unique_19) [page ] 54 | Legal Counsel | Manage Legal Tasks (F2304) | User is able to edit the legal tasks. |
| [Check Enterprise Contract Management Overview](#unique_20) [page ] 55 | Legal Counsel | Enterprise Contract Management Overview (F2933) | User is able to see the overview of all legal contexts, legal transactions, legal documents and other CM objects. |

## Test Procedures

This section describes test procedures for each process step that belongs to this scope item.

### Manage Context

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you can create your own context. A context describes a particular scenario or circumstance within which legal transactions are processed in a similar pattern. Within a context, you can predefine settings for transactions, which support a more standardized processing for them. While assigning a context to a transaction, these preconfigured settings get inherited to the item during creation.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori launchpad using business role Legal Counsel. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the appropriate Fiori app | Open Manage Contexts - for Legal Contract (F2346). | The Manage Context screen is displayed. |  |
| 3 | Manage Context | In the Manage Context page, choose Create to create an object. In the Profile dialog box, select Generic Profile. | The New Object screen is displayed. |  |
| 4 | New Object Page Header | Name: Enter for example, Purchasing PCs Germany.Version: Set to 1 as default.Status: Select Active from the drop down list.Language(Optional): Select the language.Governing Law(Optional): Select the referring governing law.Note Governing Law is mandatory if the integration with Enterprise Contract Assembly is enabled, otherwise the virtual document cannot be created for this legal transaction. |  |  |
| 5 | General Information | In the General Information section, make the following entries:Access Level(Optional): The values can be defined via SSCUI/ Configuration Activities - Define Access Level. You can refer to the chapter [Configure Self-Service Configuration UIs/ Configuration Activities](#unique_10) [page ] 9.Owner: Set to default.Main Organization Type(Optional): Select the main organization type, for example,Purchase Organization.Main Organization(Optional): Select the main organization, for example, Purch.Org.1010.Valid From: Add an appropriate start date.Valid To: Add an appropriate end date.Description (Optional): Enter the description if required. |  |  |
| 6 | Categories | Enter Group Name: Enter for example, Contract Details.Path: Select an appropriate value from value help, for example, IT Hardware.Category: Select an appropriate value from value help. For example, PCs.You can also add one more category by following the above steps. | Under Categories, you see one path - Procurement/IT Hardware. |  |
| 7 | Parties | In the Parties section:Add a new Entity by choosing Create.Make the following entries:Rank: Set to default.Entity Type: Select an appropriate entity type from the dropdown list, for example, Supplier.Name(Optional): Choose the value help in the dialog box that opens, and choose GO. Then select the required value.Required: Checked by default.Main Entity: Checked by default.Note All the other steps below are optional in Manage Contexts. You can enter the data if required or execute the step 13 directly.Add an Internal Contact by choosing Create.Rank: Set to default.Contact Type: Select an appropriate value from the dropdown list, for example, Purchaser.Name(Optional): Choose the value help in the dialog box that opens, and choose GO. Then select the required value.Required(Optional): Select the checkbox.To add External Contacts, choose Create.Rank: Set to default.Contact Type: Select an appropriate value from the dropdown list, for example, Signer.Name(Optional): Choose the value help in the dialog box that opens, and choose GO. Then select the required value.Required(Optional): Select the checkbox. | Under Entities, now you see Entity Type Supplier and also Purchase Organization, where Supplier is the main entity.Under Internal Contacts, now you see the Contact Type Purchaser.Under External Contacts, now you see the Contact Type Signer. |  |
| 8 | Relationships(Optional) | In the Legal Transactions section, choose Create and make the following entries:Relationship Type: <defined via SSCUI Define Relationship Types, Relationships, and Use Cases>Legal Transaction(Optional): <add the related legal transaction>Required(Optional): <check if the relationship is mandatory>In the Linked Objects section, choose Create and make the following entries:Object Type: Select an appropriate value from the dropdown list, for example, Purchase Order.Required (optional): Select the checkbox.NoteLinked object type and corresponding technical type can be defined via Self-Service Configuration UI/ Configuration Activities Define Linked Object Types and Define Technical Types for Linked Object Types. You can refer to the chapter [Configure Self-Service Configuration UIs/ Configuration Activities](#unique_10) [page ] 9.With External Linked Objects Integration (SAP_COM_0521), the external linked object type and corresponding technical type can be maintained here. |  |  |
| 9 | Life Cycle(Optional) | In the Renewal and Termination section, make the following combination of entries:Renewal Type: Active RenewalRenewal Reminder Recipient(Optional): for example, Administrator_LcmSend Renewal Reminder(Optional): for example, 30Renewal Period(Optional): for example, 6 MonthsRenewal Clause(Optional): for example, 3 months to contract EndTermination Reminder Recipient(Optional): for example, Administrator_LcmSend Termination Reminder(Optional): for example, 30Termination Clause(Optional): for example, 1 month to quarter EndOr make the following combination of entries:Renewal Type: Auto RenewalRenewal Period(Optional): for example, 6 MonthsTermination Reminder Recipient(Optional): for example, Administrator_LcmSend Termination Reminder(Optional): for example, 30Next Termination Clause(Optional): for example, 1 month to quarter EndTermination Clause(Optional): for example, 1 month to quarter EndIn the All Dates section, Start Date and End date are added by default and marked with Required. Choose Add and make the following entries:Date Type: Select an appropriate value from the dropdown list, for example, Start Date or Renewal Date.Note Renewal/termination clauses and date types can be defined via Self-Service Configuration UI/ Configuration Activities Define Renewal or Termination Clauses and Define Date Types. You can refer to the chapter [Configure Self-Service Configuration UIs/ Configuration Activities](#unique_10) [page ] 9. |  |  |
| 10 | Documents(Optional) | In the Documents section, choose Create to create a new document and make the following entries:Content Type: for example, Master ContractLanguage: for example, EnglishRequired (optional): Select the checkbox.Note Document content types can be defined via Self-Service Configuration UI/ Configuration Activities Define Content Types. You can refer to the chapter [Configure Self-Service Configuration UIs/ Configuration Activities](#unique_10) [page ] 9. |  |  |
| 11 | Phases(Optional) | In the Phases section, choose Create to create a new phase.On the Phase screen and in the General Information section, make the following entries:Type: for example, NegotiationStarting Condition: for example, ParallelAuto Start: <mark the checkbox if you want the phase start automatically after the legal transaction is created from this context.>In the Completion Criteria section, choose Create and make the following entries:Content Type: for example, Master ContractAction: for example, Content ExistsStamp: for example, ReviewedChoose Apply.NotePhase types can be defined via Self-Service Configuration UI/ Configuration Activities Define Phase Types. You can refer to the chapter [Configure Self-Service Configuration UIs/ Configuration Activities](#unique_10) [page ] 9.The sequence number of phases determines the phases that should be processed in order.The phase can only be created when the document is defined in the previous step, otherwise the content type is empty and cannot be saved. |  |  |
| 12 | Tasks(Optional) | In Steps section, choose Add to create a new step.Note Alternatively, you can also choose the workflow template by choosing the arrow beside Add and selecting Add Template in the dropdown list. You need to create the template using the Manage Workflow Templates app first.In Header section, make the following entries:Name(Optional): Enter an appropriate value, for example ApprovalType: select the appropriate value from the drop-down list, for example ApprovalIn Step Properties section, make the following entries:Stamp Name (optional): select the appropriate value from the drop-down list, for example Approved.Filter for Custom Step (optional): it can be defined via Self-Service Configuration UI Define Filters for Custom Step.NoteThe Stamp Name is the document stamp which can be defined via Self-Service Configuration UI/ Configuration Activities Define Document Stamps. You can refer to the chapter [Configure Self-Service Configuration UIs/ Configuration Activities](#unique_10) [page ] 9.The Filter for Custom Step is used within a workflow that contains a custom step task. During the definition of a Workflow Template (Task Group) you must set an appropriate filter ID for your custom step task. This filter will be exposed to the Business Add-In Define Custom Step (LCM_LT_WF_CUSTOM_STEP).In Recipients Section, make the following entriesAssignment by: Select User from the drop-down list(or Team defined via app Manage Teams and Responsibilities)User: Select the appropriate value from the value help, for example John legal_counselStep to be completed by: select One of the recipients or All of the recipientsSubject for Recipients(Optional): Enter an appropriate value, for example Please approve the Legal transactionIn Step Conditions section, make the following entries(Optional):Only start the step if the following preconditions are met: select an appropriate value from the dropdown list, for example, Contains Category.Enter the category name in the dialog box on the right.Choose Add another condition if more conditions are required.Choose Add alternative conditions to define another condition as an alternative.In Deadlines section (optional), choose Create to create a deadline and make the following entries:If step is not completed by: enter the number and select the unit from dropdownlistExecute the following action: Mark step as overdueChoose Apply.In Exception Handling section, the Rejected entry is displayed by default if the Type is Approval in Header section. Make the following entries:Required Action: select the appropriate value from the dropdown list, for example, ReviseYou could also maintain the recipients and deadlines for the revise option optionally.Action Result: select the appropriate value from the dropdown list, for example, Repeat Step |  |  |
| 13 | Create | Once you maintain all the required information, choose Create. | Then you can find your Context in the Manage Context app. |  |

### Request Legal Contract

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

It is a wizard that guides through the process of creating a legal Transaction. The number of steps that the wizard uses depends on the items and settings maintained in the context created using the Manage Context app.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori launchpad using business role Employee - Enterprise Contract Management. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the appropriate Fiori app | Open Request Legal Contract (F2403). | The Request Legal Contract screen is displayed. |  |
| 3 | Step 1 - Basic Data | In the Basic Data section, make the following entries:Title: Enter an appropriate title, for example, PCs Germany.Context: Select an appropriate value from value help, for example, Purchasing PCs Germany.Additional Information(Optional): add the Description, select the Language, Access Level, Governing Law and Main Organization Type and following Main Organization if required.Then choose Step 2.NoteAccess Level is optional, and it can be defined via SSCUI/ Configuration Activities - Define Access Level. You can refer to the chapter [Configure Self-Service Configuration UIs/ Configuration Activities](#unique_10) [page ] 9.Main organization type and main organization is optional, but it is critical for finalization of the legal content. | The Step 2 screen is displayed. | To select the one that you have created, Status should be Active. |
| 4 | Step 2 - Categories | In the Categories section, make sure that you verify categories. Choose Create Category to add new entry if required. Then choose Step 3. | Step 3 screen is displayed. |  |
| 5 | Step 3 - Parties | In the Parties section, make sure that you verify Entities, Internal Contacts, and External Contacts. Choose Create Object to add new entry if required. Then choose Step 4. | Step 4 screen is displayed. | For Internal Contacts, Requester is the default value. |
| 6 | Step 4 - Relationships (if available) | In the Relationships section, make sure that you verify the information. Choose Create Object to add new entry if required. Then choose Step 5. |  |  |
| 7 | Step 5 - Dates | In the Dates section, make sure that you verify the information. Choose Create to add new entry if required. | Step 5 screen is displayed. | Start Date or Renewal Date should be marked as Required by choosing Yes. |
| 8 | Step 6 - Documents (if applicable) | In the Documents section, the documents created in Context are displayed. You can upload the files if required. Choose Review. | The Review screen is displayed. |  |
| 9 | Submit | Choose Submit. | The Manage Legal Transaction page is displayed. |  |

### Manage Legal Transactions

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

A legal transaction is an object to group legal contents, which have to be processed in a specific way. It provides different user roles with access to relevant information about the legal content. This includes status, categories, parties, dates, tasks, linked objects, documents and so on.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori launchpad using business role Legal Counsel. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the appropriate Fiori app | Open Manage Legal Transactions (F2310). | The Manage Legal Transaction screen is displayed. |  |
| 3 | Manage Legal Transactions | Choose the relevant Legal Transaction from the table below it. | You are in the Legal Transaction page now. To edit legal transaction, choose Edit on the top right.Note You can also use the enterprise search function to search your legal transaction:Choose Search in the upper right area of the launchpadIn the dropdown list choose Legal Transactions and input Transaction Number from previous section.Now you are able to see the details of the legal transaction. |  |
| 4 | Relationships(Optional) | In the Legal Transaction section, check or maintain the entries inherited from the con-text if exists. You can also choose Create to add a new relationship.In the Linked Objects section, if there is an entry inherited from the context, make the following entries:Object Type: <Inherited from the context>Linked Object ID: <Enter a document number or search from F4 help>You can also choose Create to add a new relationship.Note 1. (Unchanged) You can only maintain the Linked Object ID when you have the corresponding authorization. For example, the role SAP_BR_PURCHASER is required for Purchase Order and Purchase Contract, and the role SAP_BR_RECM_SPECIALIST is required for Request for Quotation (RFQ).2. (New) For the predelivered linked object types, some of them can be navigated to the management application. For example, if a Purchase Contract, Request for Quotation, Real Estate Contract (additional license is required), Central Purchase Contract (additional license is required) or Sales Contract is maintained as linked object, the hyperlink of the document number can navigate to the corresponding app, e.g. Manage Purchase Contract. | The relationships are defined. |  |
| 5 | Reminders(Optional) | In the Reminders section, make the following entries:To add reminders, choose Create.Reminder Type: Select an appropriate value from the dropdown list, for example Reminder.Subject: Enter an appropriate value, for example Reminder to get signature.Start Date: Enter an appropriate date, for example, <today>.Reminder Cycle: Enter the condition, for example, to resend the reminder every week, enter Recur in 7 days.End Date: Enter an appropriate date, for example, <today + 30 days>.Assignment Type: select the recipient type from the dropdown list, for example, User.Recipient: Select an appropriate value from value help, for example John employeelegalcontent.Note Reminder type can be defined via Self-Service Configuration UI/ Configuration Activities Define Reminder Types. You can refer to the chapter [Configure Self-Service Configuration UIs/ Configuration Activities](#unique_10) [page ] 9. | The reminders are defined. |  |
| 6 | Task Group Templates(Optional) | In the Tasks section, choose the Task Group Templates section, choose Create and make the following entries:Task Group: for example, Task Group 1Choose the task group item. The Task Groups screen is displayed.Choose Workflow section and then choose Create.In Header section, make the following entries:Name(Optional): Enter an appropriate value, for example ApprovalType: select the appropriate value from the drop-down list, for example ApprovalOn the Recipients tab, make the following entries:Assignment By: Select User from the drop-down list(or Role)User: Select the appropriate value from the value help, for example John employeelegalcontentStep to be completed by: Select One of the recipients or All of the recipientsSubject for Recipients(Optional): Enter an appropriate value, for example Please approve the Legal transactionChoose Add to save the step.Repeat the steps above to add more steps.Choose Apply to save the task group. | The tasks are defined. |  |
| 7 | Tasks - Task Groups in Progress(Optional) | In the Tasks sections, choose Task Groups in Progresstab, choose Start Default Workflow.The Start Task Group screen is displayed. The existing legal document can be attached to the task if required.Choose Start to save the task.Note The task is mandatory for tasks mentioned in this section below if you want to manage the workflow in ECM. | The tasks defined in the context are displayed.The tasks defined in groups will also be listed here. |  |
| 8 | Documents(Optional) | There are two options avaliable after you choose Create in the Documents section:Create documentUpload fileCreate DocumentIf you only want to create legal documents with basic structures and limited information, choose Create Document, and make the following entries:Content Type: select an appropriate value from the dropdown list, for example, Master Contract.Language: select an appropriate value from the dropdown list, for example, English.Choose Create.Upload DocumentIf you want to upload files directly from your local computer, make the following entries:To add documents, choose Upload File. The Upload File screen will be displayed.Make the following entries:Content Type: Select an appropriate value from the dropdown list, for example Master Contract.Access Level (optional): for example, PrivateLanguage: Select an appropriate value from the dropdown list, for example English.Governing Law: <read-only and inherited from the legal transaction>File: Choose Browse to upload the file from your computerChoose Upload.NoteLegal document is mandatory for steps mentioned in this section below if you want to manage legal document in ECM. | The document is attached to the legal transaction. |  |
| 9 | Collaboration(Optional) | In the Collaborations section, choose Create and Internal Collaboration or External Collaboration to create a new collaboration object, choose View or Edit from the dropdown list and choose Next.On the New collaboration screen and in the General Information section, make the following entries:Collaboration Name: Enter the name.Team Name: Keep the default valueDescription (optional): Enter the descriptionIn the Documents section, choose Add to add the documents.On the Document List screen, choose the document from the list and choose Add.In the Members section, choose Add and Internal Contact or External Contact to add the members.On the Member List screen, choose the name from the list and choose Add.Choose Submit.NoteWith collaboration platfroms integration, for example, Microsoft Teams Integration (SAP_COM_0823/SAP_COM_0824), the collaboration objects can be maintained here.The integration swtich must be activated first via self-service configuration UI/ configuration activities Enable Switch for Collaboration with Microsoft Teams. You can refer to the chapter [Configure Self-Service Configuration UIs/ Configuration Activities](#unique_10) [page ] 9.The retention period can also be defined via self-service configuration UI/ configuration activities Maintain Retention Period for Collaboration Platforms. You can refer to the chapter [Configure Self-Service Configuration UIs/ Configuration Activities](#unique_10) [page ] 9.The collaboration documents can also be involed in workflow and e-signature business processes addtionally. |  |  |
| 10 | Phases (Optional) | Review the obligations maintained for legal transaction if available.Choose Start to start the phase with not completed status.Note 1. The phase with auto-start function enabled will start automatically once the legal transaction is created, and the status will change to In Progress.2. For the phases are defined with Starting Condition: Parallel, it does not have any impact if not all phases are completed finally. But for the phases are defined with Starting Condition: Sequential, they must be completed one by one, the next one can not be started if the previous one is not completed.3. With the pre-delivered situation type, a notification is sent to the predefined recipients when the status of the phase is changed from Completed to Completed (Revision Needed). | The phases are reviewed or started. |  |
| 11 | Obligations (Optional) | Review the obligations maintained for legal document if available. | The obligations are reviewed. |  |
| 12 | e-Signature Envelops (Optional) | Review the e-Signature envelops for legal document if available, and the open ones can be cancelled here before completed. | The e-Signature envelops are reviewed. |  |
| 13 | Notes (Optional) | Any note, comment or additional information can be added here. | The notes are added. |  |
| 14 | Save | Once you maintain all the information, choose Save. |  |  |

### Approve Legal Transactions (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

It is a wizard that guides you through the process of approving a legal transaction with the business workflow.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori launchpad using business role Employee - Enterprise Contract Management. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the App | Open My Inbox - All Items (F0862) | The My Inbox screen is displayed. |  |
| 3 | Open Notification | On My Inbox screen, choose the appropriate notification. For example, the subject is Process Legal Transaction 100000XXXX <subject of the legal transaction>. | The detailed info of notification is displayed. |  |
| 4 | Approve Legal Transaction | Choose Complete on the lower right corner of the screen. Enter the note if required, then choose Submit. | The legal transaction is approved. |  |

### Send Legal Document for Signature

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you can send the legal document that meets the criteria for signature.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori launchpad with business role Legal Counsel. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the App | Open Manage Legal Transactions (F2310). | The Manage Legal Transactions screen is displayed. |  |
| 3 | Manage Legal Transactions | Choose the legal transaction with status On Track or Open Issues. | You are directed to the Legal Transaction page.You can also use the enterprise search functionality to search your legal transaction by following the steps below:Choose Search in the upper right area.In the dropdown list, choose Legal Transactions and enter Transaction Number from previous section.The details of legal transaction will be displayed. |  |
| 4 | Send for E-Signature (Optional) | Note The integration scenario SAP_COM_0518 must be configured according to the setup instructions of scope item 1XV before the signature process for legal documents can start.If your legal document does not have a valid document, then the button Start Manual Signature will not work, and a piece of error message “Document cannot be sent for manual signature” will be displayed.In Documents section, choose the legal document with a valid document and choose Signature > Send for e-Signature .On the Select Template screen, choose a valid DocuSign template, and choose Next.Select the valid recipient and choose Send. The Signature Status of the legal document will change to Sent for e-Signature.New entry will be automatically generated in the e-Signature Envelopes section. Click the hyperlink of the Envelope ID and log in with DocuSign tenant.Choose SIGN for the envelope, review the document and choose CONTINUE, click on the Sign button on the document. Choose FINISH.After the envelope status is updated, the value of Signature Status field of legal document will change to e-Signed and the Status will change to Accepted. | The legal document is signed with DocuSign e-Signature and is accepted. |  |
| 5 | Start Manual Signature (Optional) | Note The integration scenario SAP_COM_0518 must be configured according to the setup instructions of scope item 1XV before the signature process for legal documents can start.If your legal document does not have a valid document, then the button Start Manual Signature will not work, and a piece of error message “Document cannot be sent for manual signature” will be displayed.In Documents section, choose the legal document with a valid document and choose Signature > Start Manual Signature . The signature status of legal document will change to Sent for Manual Signature.After your downloaded file is signed manually, choose Upload Signed File to upload the signed document from local address. For the legal document, the following status will change:Signiture Status: Manually SignedStatus: Accepted | The legal document is manually signed and accepted. |  |

### Envelope Status Update (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you update the envelope status by running the application job. This step is only required for e-Signature integrated with DocuSign.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori launchpad with a user with business role template Administrator - Enterprise Contract Management | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Schedule Envelope Status Updates (F4344) | The Schedule Envelope Status Updates screen is displayed. |  |
| 3 | Schedule Envelope Status Updates | On the Schedule Envelope Status Updates screen, choose Create.On the New Job: Get DocuSign Envelope Status and Update screen, make the following entries:Job Template: Get DocuSign Envelope Status and UpdateJob Name: Get DocuSign Envelope Status and UpdateChoose Step 2.Keep the default values or you could also choose Define Recurrence Pattern to schedule the regular job.Choose Step 3.Choose the Envelope IDs you want to update the status, or choose all entries.Choose Schedule.Go back to the Schedule Envelope Status Updates screen, choose Go to refresh the job status until it’s finished. | The application job is scheduled and the envelope status will be updated after the job is finished. |  |
| 4 | Access the App | Open Manage Legal Transactions (F2310). | The Manage Legal Transactions screen is displayed. |  |
| 5 | Manage Legal Transactions | Choose the legal transaction whose document you have sent for e-Signature in previous steps. | You are in the Legal Transaction page now. |  |
| 6 | Verify the Signature Status | In e-Signature Envelopes section, the Status of the envelope is Completed (02).In Documents section, the legal document sent for e-Signature will get the Signature Status e-Signed and Status will change to Accepted.Meanwhile, a new document with the name Certificate for Envelope xxxxxx will be created automatically. Its status will become Accepted. You could download the file to check the certificate created by DocuSign. | The signature status is verified. |  |

### Manage Legal Documents

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

A legal document is an object that contains the legal contracts or other documents. The Manage Documents app can manage the legal documents centrally.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori launchpad using business role Legal Counsel. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the App | Open Manage Legal Documents (F2453) | The Manage Legal Documents screen is displayed. |  |
| 3 | Manage Legal Documents | Choose relevant Legal Document from below table | Now you are inside Legal Document. To edit Legal Document, choose Edit on top right corner.Note You can also use the Enterprise Search functionality to search your Legal document:Choose Search in the upper right area of the launchpad.In the dropdown list choose: Legal Documents and input Document Number from previous section.Now you are able to see the details of the Legal document. |  |
| 4 | Stamps | In Stamps Section, make entries and choose Add.Stamp Name: select appropriate from drop down, for example Accepted.Date, Time: Set to defaultAdded By: Set to defaultChoose Save | Then it navigates to Legal Document. |  |
| 5 | Create Amendment for Main Contract (Optional) | If Main Document is the Document Kid of your legal document, you can choose to create amendments for main contract.Choose Create, and then choose Amendment. Two options are avaliable: Upload a File and Create Document.If you choose the option Upload a File, your new amendment will inherit information of parent document, content type, language and governing law from the main document. These pieces of information can not be changed.If you choose the option Create Document, your new amendment will inherit information of parent document, content type and language from the main document. These pieces of information can not be changed. You can also copy header or obligation information by selecting the Header or/and Obligations attributes or facets. | A new amendment is created for your main document. |  |
| 6 | Edit the Document(Optional) | Choose Edit on the upper right corner to change the content of the document.Choose Check Out to lock the attached document.Download the file and edit the file offline.Choose Check In and upload the modified file to release the new version.Choose one of the following options in the Check In dialog box when uploading the file:Confirm check-in and create a new versionConfirm check-in and replace current version | The legal document is modified.Note If you choose the option Confirm check-in and create a new version, the old version of the legal document will be created as version 1 in Version History and the new version will be version 2. |  |
| 7 | Save | Once you maintain this information, choose Save |  |  |

### Manage Legal Tasks

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

With the Manage Documents app, you can manage tasks that are linked to different legal transactions, forward tasks to other agents, and notify agents about pending tasks. You can see all the tasks grouped under the legal transaction from where these workflow tasks were triggered. You can filter the tasks based on task types and agent roles, in addition to all the other common filter types.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori launchpad using business role Legal Counsel. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the App | Open Manage Legal Tasks (F2304). | The Manage Legal Task screen is displayed. |  |
| 3 | Manage Legal Tasks | Choose relevant legal task from the table below with the status Ready, Waiting or Accepted. | Now you are inside Task. |  |
| 4 | Forward the Task | Choose Forward on the upper right corner. The Forward screen is displayed.Make the following entries:To: <Enter the recipient or search from F4 help>Note: <Enter a note for the forwarding>Choose OK. | The legal task is forwarded, and the recipient will replace all users in the Agents section on the Task screen. |  |
| 5 | Check the Forwarded Task in My Inbox app (Optional) | Log on to the SAP Fiori launchpad with the user of the recipient and open My Inbox - All ItemsOn My Inbox screen, choose the appropriate task. | The detailed info of task is displayed, and the following-up action can be taken. |  |
| 6 | Send the Notification | Choose Notify on the upper right corner. The Notify screen is displayed.Make the following entries:To: <The recipient will be displayed by default>Note: <Enter the content of the notification>Choose OK. The message Notification has been sent is displayed. | The notification is sent to the recipients of the Agents. |  |
| 7 | Check the Notification in My Inbox app (Optional) | Log on to the SAP Fiori launchpad with the user of the recipient and open My Inbox - All Items.On My Inbox screen, choose the appropriate task.On Comments tab, the notification is displayed. | The detailed info of notification is displayed, and the following-up action can be taken. |  |

### Check Enterprise Contract Management Overview

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

- You can view the overall status of all CM objects including contexts, documents and legal transactions.
- You can filter the context or main entity to view the status of the corresponding context, document and legal transaction.
- With the tiles of this app, you can view the context expiring soon, legal transactions at risk, total document status, total document stamps, total legal transactions health, total context status, upcoming dates, upcoming reminders, open documents, signed and accepted documents.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori launchpad using business role Legal Counsel. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access Appropriate Fiori App | Open Enterprise Contract Management Overview (F2933) | The Enterprise Contract Management Overview screen is displayed. |  |
| 3 | Total Legal Transaction Status | Choose Total Legal Transaction Status to display all legal transactions, or choose the status category in the chart below to display the legal transactions with different status. | The Manage Legal Transactions screen is displayed. |  |
| 4 | Context Status | Choose Context Status to display all contexts, or choose the status category in the chart below to display the contexts with different status. | The Manage Contexts screen is displayed. |  |
| 5 | Context Expired Soon | Choose Context Expired Soon to display all contexts, or choose the item in the list below to display the individual context which will be expired soon. | The Manage Contexts screen is displayed. |  |
| 6 | Legal Transactions with Open Issues | Choose Legal Transactions with Open Issues to display all legal transactions or choose the item in the list below to display the individual legal transaction which has some open issues. | The Manage Legal Transactions screen is displayed. |  |
| 7 | Document Stamps | Choose Document Stamps to display all legal documents or choose the stamp category in the chart below to display the legal documents with different stamp. | The Manage Legal Documents screen is displayed. |  |
| 8 | Document Status | Choose Document Status to display all legal documents or choose the status category in the chart below to display the legal documents with different status. | The Manage Legal Documents screen is displayed. |  |
| 9 | Average Document Creation Time | Choose Documents to display all legal transactions or choose the dot in the chart below to display the legal transactions created this year. | The Manage Legal Transactions screen is displayed. |  |
| 10 | Average Documents Finalization Time | Choose Documents to display all legal transactions or choose the dot in the chart below to display the legal transactions finalized this year. | The Manage Legal Transactions screen is displayed. |  |
| 11 | Upcoming Dates | Choose Upcoming Dates to display all legal transactions or choose the item in the list below to display the individual legal transaction with the earliest termination date. | The Manage Legal Transactions screen is displayed. |  |
| 12 | Upcoming Reminders | Choose Legal Transactions to display all legal transactions or choose the item in the list below to display the individual legal transaction with the earliest reminder.The dropdown list can be used to filter the reminder type. | The Manage Legal Transactions screen is displayed. |  |
| 13 | Open Documents | Choose Open Documents or View All to display all open documents or choose the <number>of <number> button on the right to get the list of open documents. | The Manage Legal Documents screen is displayed. |  |
| 14 | Signed and Accepted Documents | Choose Signed and Accepted Documents to display all signed and accepted documents or choose the item in the list below to display the individual document which is signed or accepted. | The Manage Legal Documents screen is displayed. |  |
| 15 | Average Task Processing Time | Choose Average Task Processing Time to display all legal documents or choose the dot in the chart below to display the legal tasks with Completed status this year. | The Manage Legal Tasks screen is displayed. |  |
| 16 | Pending Tasks of My Legal Transactions | Choose Pending Tasks of My Transactions to display all legal documents or choose the dot in the chart below to display the legal tasks with Ready or Waiting status. | The Manage Legal Tasks screen is displayed. |  |
| 17 | Task Completion | Choose Task Completion to display all legal documents or choose the dot in the chart below to display the legal tasks with Completed status this year. | The Manage Legal Tasks screen is displayed. |  |

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
> Flagged while digesting this document, not verified: The same app, My Inbox - All Items, is given as F5331 in the Overview Table but as F0862 in the Approve Legal Transactions procedure.

## Connections
- part-of :: [[_cluster]]
- related-to :: [[01-solution-foundation-and-platform/test-script-integration-to-icertis-for-contract-assembly-6v2-sap-s-4ha]]
- related-to :: [[01-solution-foundation-and-platform/test-script-integration-to-sap-enterprise-contract-assembly-2oq-846]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/1XV_S4CLD2608_BPD_EN_XX.docx` — full document · extracted with `mammoth` · 107,449 chars in the whole document
