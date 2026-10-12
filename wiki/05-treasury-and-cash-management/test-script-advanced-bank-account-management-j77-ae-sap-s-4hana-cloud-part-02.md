---
id: 05-treasury-and-cash-management/test-script-advanced-bank-account-management-j77-ae-sap-s-4hana-cloud-part-02
title: "Test Script: Advanced Bank Account Management (J77_AE), SAP S/4HANA Cloud Public Edition (J77_S4CLD2608_BPD_EN_AE) — part 2 of 2"
description: "J77 Advanced Bank Account Management test script, part 2: two-person and workflow bank account lifecycles, payment approvers, powers of attorney, reviews."
cluster: 05-treasury-and-cash-management
tags: [kb/treasury-and-cash-management, topic/bank-account-management]
aliases: []
keywords: [Bank Account Management, two-person verification, workflow revision activation, bank account creation, bank account closing, payment approvers, powers of attorney, bank account reviews, bank account hierarchies, in-house bank accounts]
sources: ["raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/J77_S4CLD2608_BPD_EN_AE.docx#lines-2889-5542"]
confidence: low
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-1308
topic: 05-treasury-and-cash-management/bank-account-management
language: EN
part: 2/2
created: 2026-10-12
updated: 2026-10-12
---

# Test Script: Advanced Bank Account Management (J77_AE), SAP S/4HANA Cloud Public Edition (J77_S4CLD2608_BPD_EN_AE) — part 2 of 2

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/J77_S4CLD2608_BPD_EN_AE.docx`, part 2 of 2 (lines 2889–5542 of the extracted text), extracted with `mammoth`. Grouped under **Bank Account Management** in Treasury and Cash Management. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

| 13 | Return to Active | Choose Return to Preceding Status.Refer to Activate the Bank Account Request via Dual Control step to activate the change request. | A bank account change request has been created. Follow the steps in Activate the Bank Account Request via Dual Control to activate this request. Once completed, the bank account status will be updated to Active. |  |

##### Maintain Payment Approver for Multiple Bank Accounts (Dual Control Revision Activate)

Prerequisites

Approval patterns and and payment approve group have to be defined and assigned to company code before you start following procedures. Make sure you have finished the prerequisite step of Payment Approval Customizing before you start to maintain payment approver. SAP has predelivered the sequential pattern P001 with payment approver group G001 and G002, and the nonsequential pattern s001 with payment approver group SG01 and SG02 as Demo data in Start system.

Use

This step describes how to maintain Payment Approver for multiple bank accounts with Full Cash Management and Dual Control Revision Activate.

|  |
| --- |
| Note SAP supports sequential and nonsequential payment approval process.Sequential Payment Approver: The payment approval should obey the approver sequence. For example, if the Accounts Payable Manager is set as the first approver, the Cash Manager is set as the second approver. The Cash Manager cannot approve the payment before the Accounts Payable Manager in sequential Payment Approver case.Nonsequential Payment Approver: No sequence exists for the approvers. The Approver Group field decides the Payment Approver case you can choose. |

|  |
| --- |
| Caution The following procedure assumes that you are only Maintaining Payment Approver for Multiple Accounts with Full Cash Procedures Management Using Dual Control Revision Activate procedure. If you are implementing and testing additional Full Cash Management options, especially in a single environment, you cannot use the same Master Data values for more than one procedure type. You must create additional Master Data values, for example G/L Accounts, and then use these different values in each procedure type. |

###### Add Payment Approver for Multiple Bank Accounts

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you can trigger the mass maintenance of Payment Approver for multiple bank accounts. And one individual approve and confirm process is required for change Payment Approver requests to one Payment Approver group.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Cash Management Specialist. |  |  |
| 2 | Open SAP Fiori App | Open Maintain Payment Approver (WDA_FCLM_BAM_ADAPT_SIGN (APP_CFG_FCLM_BAM_ADAPT_SIGN)). |  |  |
| 3 | Select Company Code | Select company code in the filter header:Company Code: For example, 3310 and then choose Go to filter the results list. | Multiple bank accounts of the company code display in the Results List. |  |
| 4 | Select Bank Accounts | Select Bank Accounts rows in Results List:For example, bank account 0000000693123456 of bank key 18121976and bank account 0000000693123456 of bank key 18121986.Choose Add Payment Approver. | The Add Payment Approver screen displays. |  |
| 5 | Add Payment Approver to Payment Approver Group G001 | On the Add Payment Approver screen, make the following entries:New Approver: For example, <the user ID (CB*) has business role Accounts Payable Manager assigned>Valid From: For example, <current date>.Valid To: For example, 31.12.9999Payment Approver Group: G001Note The value above is used for sequential Payment Approver. If you want to use nonsequential Payment Approver, use SG01.Max. Amount for Payment: For example, 100,000.000Max. Amount for Batch: For example, 1,000,000.000Note The check box of Unlimited Approval is used for grant the authorization of approving unlimited amount. When you select this check box, the value of Maximum Amount for Payment and Maximum Amount for Batch will be invalid, the Payment Approver can approve an unlimited amount.Currency: AEDTitle: For example, Add Payment ApproverNote: Enter an explanatory noteChoose OK. | Change Payment Approver request to Payment Approver Group G001 has been created. |  |
| 6 | Add Payment Approver to Payment Approver Group G002 | Once Change Payment Approver request to Payment Approver Group G001 has been activated by the Cash Manager as described in the Activate the Bank Account after Payment Approver Maintenance procedure, repeat steps 2-4.On the Add Payment Approver screen, make the following entries:New Approver: For example, the user ID (CB*) of business user Cash Manager has business role Cash Manager assignedValid From: For example, <current date>Valid To: For example, 31.12.9999Payment Approver Group: For example, G002Note The value above is used for sequential Payment Approver. If you want to use nonsequential Payment Approver, use SG02.Max. Amount for Payment: For example, 100,000.000Max. Amount for Batch: For example, 1,000,000.000Currency: AEDTitle: For example, Add Payment ApproverNote: <Enter a note>Choose OK. | The bank account is changed (To be Active). |  |

###### Change Payment Approver for Multiple Bank Accounts

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you can make mass maintenance of Payment Approver in multiple bank accounts.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Cash Management Specialist. | The SAP Fiori launchpad is displayed. |  |
| 2 | Open SAP Fiori App | Open Maintain Payment Approver (WDA_FCLM_BAM_ADAPT_SIGN (APP_CFG_FCLM_BAM_ADAPT_SIGN)). | The Maintain Payment Approver - For Multiple Bank Accounts screen is displayed. |  |
| 3 | Select Company Code | Select company code in the filter header:Company Code: For example, 3310, and then choose Go to filter the results list. | Multiple bank accounts of the company code are displayed in the Results List. |  |
| 4 | Select Bank Accounts | Select Bank Accounts rows in Results List:For example, bank account 0000000693123456 of bank key 18121976and bank account 0000000693123456 of bank key 18121986.Choose Change Payment Approver. | Change Payment Approver screen is displayed. |  |
| 5 | Change Payment Approver | On the Change Payment Approver screen, make the following entries:New Payment Approver: For example, the user ID (CB*) has business role Cash Manager Specialist assignedValid From: For example, current date.Valid To: For example, 31.12.9999(New Payment Approver Section)Note Keep the Valid To date in Old Payment Approver section as current date.Choose OK. | The Payment Approver is changed for the bank account. |  |

##### Upload Attachments for Bank Account

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

You can upload attachments for the bank account.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Cash Management Specialist. |  |  |
| 2 | Access the SAP Fiori App | Open Manage Bank Accounts (F1366A). | The Manage Bank Accounts view displays. |  |
| 3 | Binding Cash Pools as Leading Account | Make the following entries and choose Go:Account Number: An active account. For example, 1133698 | Note If the basic setting is Direct Revision Activate, the bank account is activated. |  |
| 4 | Bank Account View | In the data table, choose the arrow icon at the right of the row for the account. | The Bank Account view displays. |  |
| 5 | Edit | Choose Edit. |  |  |
| 6 | Upload Attachments | Navigate to Attachments tabSelect Doc.Type to Upload: AttachmentsChoose Upload.Select a document to upload.Choose Submit for Activation. |  |  |

##### Activate the Bank Account via Dual Control

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, a second operator can approve the changes that are made in previous steps.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Cash Manager. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the SAP Fiori App | Open Manage Bank Accounts (F1366A). | The Manage Bank Accounts view displays. |  |
| 3 | Select a Bank Account Number | Enter the following data:Account Number: <bank account number created in the previous procedure>and choose Go. | The Bank Accounts table displays the bank account. |  |
| 4 | Choose the Bank Account | Select the bank account. | The bank account details view displays. |  |
| 5 | Activate | Choose Confirm Revision. | The Revision List displays. |  |
| 6 | Select Revision 1 and Activate | Select Revision 1.Choose Details to display bank account master data in revision 1.Choose Review and Confirm.Choose Confirm.An email is automatically sent to the relevant person, when the email address parameters are correctly maintained. For more information, see the Define Output Parameter Determination procedure in the Prerequisites section.To verify that an email was sent, From the Manage Bank Accounts view, select the bank account to open the details view. Review the log entry created in the Bank Correspondence tab.Remember The sender email address maintained in Output Parameter Determination takes priority when valid. If the sender email address is invalid in Output Parameter Determination, the email address is defaulted to the company code’s email address. The receiver email address is that of the Bank Contact Person. If Bank Contact Person is not maintained, the receiver email is the Bank Relationship Manager. If Bank Relationship Manager is not maintained, the receiver is the email address maintained in the Bank. | Revision Status is changed to Activated. |  |

#### Using Two-Person Verification Revision Activation

##### Create Bank Account

###### Open Bank Account

Purpose

The bank accountant (Cash Management Specialist) goes to the bank and opens a new bank account at that bank. This step does not occur in the system.

###### Create Bank Master Data

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you can create standard banks and internal banks master data with general information. For physical banks you should create it as standard banks, and for others you should create it as internal banks.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori launchpad as a Cash Management Specialist. |  |  |
| 2 | Access the SAP Fiori App | Open Manage Banks - Master Data (F6437). |  |  |
| 3 | Choose Create Bank | Choose Go for the banks to display in a list and choose Create Bank. | The Create Bank view displays. |  |
| 4 | Enter Criteria | Make the following entries:Bank Country/Region: AEBank Key: 88800011Choose Create Bank. |  |  |
| 5 | Enter General Data | Make the following entries:Bank Name: AE Standard Bank for Advanced Bank Account Management Two-Person ModeChoose Create. | The standard bank is created. |  |
| 6 | Create Internal Banks | Go to the initial page of app Manage Banks - Master Data (F6437).Choose the triangle button beside the Create.Choose Create Internal Bank. |  |  |
| 7 | Enter Control Data | Make the following entries:Bank Country/Region: AEBank Key: 88888889Internal Bank Category: Payment Service ProviderChoose Create Internal Bank.Note If the bank key created is used for an internal virtual bank, for example, PayPal,which is used as House Bank, please select Internal - Payment Service Provider.which is used to enable the maintenance of the business partner bank details with alias, please select the Payment system. For more details, please refer to SSCUIs 105361 - Define Alias Types and 105362 - Define Payment Systems. |  |  |
| 8 | Enter General Data | Make the following entries:Bank Name: AE Internal Bank for Advanced Bank Account Management Two-Person ModeChoose Create. | The Internal bank is created. |  |

###### Edit Bank Master Data

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The purpose of this step is to edit bank and input more bank information in production system.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Cash Management Specialist. |  |  |
| 2 | Access the SAP Fiori App | Open Manage Banks - Master Data (F6437). |  |  |
| 3 | Filter the Bank | Make the following entry in the filter and choose Go.Bank Key: 88800011 |  |  |
| 4 | Choose the Bank | Choose the Bank in the list. |  |  |
| 5 | Edit Bank | Choose Edit.Make the following entries:SWIFT/BIC: DEUTDEFFXX1City: for example, 60040 Frankfurt, Main |  |  |
| 5 | Save Your Entries | Choose Save. |  |  |

###### Create Bank G/L Account

Purpose

The G/L accountant may create the G/L accounts for a new bank account.

|  |
| --- |
| Note In cash management in this package, you can use the same G/L accounts (bank main account and bank subaccount) for different bank accounts if they use the same currency key. The balance of each bank account can be displayed in the Cash management app, instead of checking balances of the relevant G/L account. Using this approach keeps the chart of accounts smaller. |

|  |
| --- |
| Note If you want to create a G/L account for a new bank account, execute the following steps. Create G/L accounts in production system, development system, and consolidation test system. |

|  |
| --- |
| Note This procedure is mentioned in the Accounting and Financial Close (([J58](https://me.sap.com/processnavigator/SolS/SolS-013/2608/SolP/J58))) test script. Refer to the step Manage G/L Account Master Data and copy an existing G/L Account to a new one, for example, copy 11001000 to 11003000. |

###### Manage Banks Cash Management Data

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you can input banks data that is used for cash management.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori launchpad as a Cash Management Specialist. |  |  |
| 2 | Access the SAP Fiori App | Open Manage Banks - Cash Management (F1574A). |  |  |
| 3 | Enter Search Criteria | Make the following entries:Bank Country/Region: AEBank Key: 88800011If the Bank Key field is not visible, choose Filters to unhide it.Choose Go.Go into the detail of the bank. | The Display Bank view appears. |  |
| 4 | Enter Risk Business Partner | Choose Edit.Make the following entry:Risk Business Partner: for example, 55555 | The Manage Banks view displays. |  |
| 5 | Enter House Bank Data | Go to House Banks tab and choose Create.Make the following entries:Company Code: 3310House Bank: AEBK3Choose Continue.Choose Apply. |  |  |
| 6 | Enter Netting Business Partner | Go to Netting Business Partner tab.Make the following entries:Valid From: <Current Date>.Valid To: <Futrue Date>.Business Partner: <Choose one by using search help>. |  |  |
| 7 | Save Bank | Choose Save. | New house bank is saved successfully. |  |

###### Create Bank Account

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you create a bank account.

|  |
| --- |
| Note Since bank accounts are not transportable to the production system, they must be maintained manually there. |

|  |
| --- |
| Remember The [Define Basic Settings](#unique_9) [page ] 12 topic in the Prerequisites section must be reviewed following any system upgrade or improvement before continuing any business operations in the system. When differences are found from previous activations, you must correct the setting through the following IMG path: IMG > Financial Supply Chain Management > Cash and Liquidity Management > General Settings > Define Basic Settings via the user who has sufficient authorization to do the customizing. In this setting, set the Cash Scope field to Full Scope and the Bank Account Control Mode field to Two-Person Verification. |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Cash Management Specialist. |  |  |
| 2 | Access the SAP Fiori App | Open Manage Bank Accounts (F1366A). |  |  |
| 3 | Create Bank Account | Choose Create to add a new bank account.Make the following entries.Company Code: 3310Account Type: 01 | The Bank Account screen displays. |  |
| 4 | Enter Header Data | Make the following entries:Account Number: 0000000033108888Account Description: AEBank Account for Advanced Bank Account Management Two-Person ModeBank Country/Region: AEBank Key: 88800011Currency: AED |  |  |
| 5 | Enter General Data | Change the following entries:Opening Date: for example, <current date>Account Holder: Company Code3310 (company code name is usually defaulted by system)Bank Control Key: for example, PNote Only perform this step if the country is using Bank Control Key; if you do not use Bank Control Key in your process, just skip this step.IBAN: <Generate IBAN>Note Only perform this step if the country is using IBAN; if you do not use IBAN in your process, just skip this step. |  |  |
| 6 | Bank Relationship Data | Pmnt Tran Type Group: CAMT053Note The field Transaction Type is not available for on premise. To assign the Transaction Type to your Bank Account use the IMG Menu Path: Financial Accounting > Bank Accounting > Business Transactions > Payment Transactions > Electronic Bank Statement > Make Global Settings for Electronic Bank StatementsNote If you are going to upload camt.054 format bank statement for supplier financing, which is described in test script 1EG, the field Pmnt Tran Type Group has to be maintained as camt053, otherwise camt054 bank statement can't be uploaded. |  |  |
| 7 | Maintain Internal Bank Account Contact | In the Contact Persons area (in the Bank Relationship section), enter a system user ID, for example, the ID assigned with the business role of Cash Management Specialist.Enter the ID in the Internal Bank Account Contact field. |  |  |
| 8 | Maintain Internal Bank Account | In the Contact Persons area, enter a system user ID, for example, the ID assigned with the business role of Cash ManagerEnter the user ID in the Internal Bank Account Supervisor field. |  |  |
| 9 | Choose Bank Relationship Tab | In the Bank Statement Data area, make the following entries:Processing status: SelectedInterval: for example, 01Interval Unit: for example, MonthsFactory Calendar ID: for example, 01Note Processing status: Indicates whether to monitor this bank account at the end of the day in Bank Statement Monitor.Interval: Specifies how often the bank statements for a bank account are imported to your system.Interval Unit: Specifies the unit of measurement for an interval.Factory Calendar ID: Distinguishes between working days and non-working days. |  |  |
| 10 | Choose House Bank Account Connectivity | Choose the House Bank Account Connectivity tab. | The House Bank Account Connectivity tab displays. | House Bank Account Connectivity allows you to associate a bank account with its house bank account in the central system where SAP S/4HANA Cloud Public Edition Finance for Cash Management is installed. It also enables connections to accounts in remote SAP or third-party systems. For additional information, please refer to the online help [Define House Bank Account Connectivity](https://help.sap.com/docs/SAP_S4HANA_CLOUD/186460fdc35a4b64a713da9bb00deb1e/2abbcf54a14a713be10000000a44176d.html?version=LATEST&locale=en-US). |
| 11 | Enter House Bank Account Connectivity | Choose Create.Make the following entries:ID Category: for example, Central System: House Bank AccountRemote System: Leave blankNote If you have enabled the Convert Remote House Bank Accounts functionality in the configuration activity Define System Groups (107199), please ensure that all necessary attributes for the remote house bank accounts to be replicated are properly maintained prior to their conversion to the ID category Central System: House Bank Account. These accounts are then replicated back to the originating target system. Incorrect or missing attributes may result in validation errors in the target systems. For further information, please refer to the online help [Define House Bank Account Connectivity](https://help.sap.com/docs/SAP_S4HANA_CLOUD/186460fdc35a4b64a713da9bb00deb1e/2abbcf54a14a713be10000000a44176d.html?version=LATEST&locale=en-US) and [Outbound Integration](https://help.sap.com/docs/SAP_S4HANA_CLOUD/186460fdc35a4b64a713da9bb00deb1e/9b57a8997a02462989f2d0b168dac811.html?version=LATEST&locale=en-US).Company Code: 3310House Bank: AEBK3House Bank Acct ID: AEAC3G/L Account: 11001000Control Key: PUse in Cash Pooling: DeselectedNote The Use in Cash Pooling field determines if the house bank account is used for cash pooling. If the checkbox is selected, this house bank account can be used for cash pooling. If there are multiple house bank accounts for one bank account, only one house bank account can be used for cash pooling. |  |  |
| 12 | Choose Payment Approvers tab | Choose the Payment Approvers tab. |  |  |
| 13 | Maintain Payment Approver for Payment Approver Group G001 | Make the following entries:Note Make sure you have finished the prerequisite step of Payment Approval Customizing, before you start maintain approver.Payment Approver Group: for example, G001 (the first step of two-step approval)Payment Approver: for example, the user ID assigned with the Accounts Payable Manager business roleCurrency: AEDMax. Amount for Payment: for example, 10,000,000.00Max. Amount for Batch Payment: for example, 50,000,000.00Note If the Unlimited Approval check box is selected, the payment approver can approve unlimited amount.Valid From: for example, <current date>.Valid To: for example, 31.12.9999 | The Payment Approver Group G001 is maintained. |  |
| 14 | Maintain Payment Approver for Payment Approver Group G002 | Repeat the previous step to create a User ID to Payment Approver group G002 (The second step for two-step approval).Use the same values in previous step, except that Payment Approver Group is (G002).For Payment Approver, enter the user ID assigned with the Cash Manager business role. The user ID assigned MUST be different from the user ID assigned to G001. | The Payment Approver Group G002 is maintained. |  |
| 15 | Check Approval Information | Choose Show Approval Step.You can find the detail information about approval sequence, approval amount for each approver. |  |  |
| 16 | Overdraft Limits | Make the following entries:Overdraft Type: SO01Overdraft Type Description: Overnight OverdraftOverdraft Category: Overnight OverdraftAmount: 10000 AEDValid From: Current DateValid To: 12/31/9999Note The valid period for the same overdraft type cannot overlap. You can maintain Overdraft Type in SSCUI 107092 Define Bank Account Overdraft Limit Types. |  | Overdraft Limit Type is controlled by Customer Control Feature Toggle FTGL_BAM_BKACCT_OVERDRAFT_TYPE, the feature toggle is deactivated by default. You can activate the feature toggle in SSCUI 106573 Activate Features. If the feature toggle is not activated, fields Overdraft Type, Overdraft Type Description and Overdraft Category will be hidden, SSCUI 107092 Define Bank Account Overdraft Limit Types will also be invisible. |
| 17 | Save and Activate Bank Account for Origination Process Enabled Scenario | Note This step can be executed if Bank Account Origiantion Process has been enabled, otherwise skip this step.Ensure all necessary data have been entered and choose Save.You can choose edit and enrich the data if necessary, then choose Start Opening.Choose Confirm Opening at Bank.Note The step of choosing Start Opening and choosing Confirm Opening at Bank is depending on the Preliminary step Enable Bank Account Origination Process setting. Only if the status 24 Pre-Opening Preparation has been configured and its enable status check box has been selected, you can execute the step Send Open Request to Bank. And only if the status 26 In Opening Process has been configured and its enable status check box has been selected, you can execute the step Confirm Opening at Bank. |  |  |
| 18 | Save as Inactive and Submit for Activation | Ensure all necessary data have been entered and choose Save as Inactive.Choose Submit for Verification.Enter Note: Please verify the bank account.Choose Submit for Verification.Note After you submit for verification, you can withdraw your application by choosing the Withdraw button on the upright of the screen. You can’t modify the bank account during the verification process. |  |  |

###### Export Bank Account

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The bank account modification in the production system is completed in the previous step. Because some system configuration is based on house bank and house bank account, after a bank account’s attribute is changed, you may need to update the configuration in the development system. If so, export the bank accounts from the production system, and then import them into the development and consolidation test systems.

Prerequisites

Use Microsoft Office 2010 or higher that includes Microsoft Excel.

You must enable the Developer tab in Microsoft Excel.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log onto the SAP Fiori launchpad as a Cash Management Specialist. |  |  |
| 2 | Access the SAP Fiori app | Open Manage Bank Accounts (F1366A). |  |  |
| 3 | Upload/download Account | Choose Import and Export Bank Accounts. | The Import and Export Bank Accounts screen displays. |  |
| 4 | Export Bank Master Data XML file | In the Bank Accounts Export section, choose Export Bank Accounts to an XML File.In the File Download dialog box, choose Save As.In the Save As dialog box, identify a location to save the XML file.Choose Save.Note Download processing steps varies on different browser, above steps apply to IE. If you are using Chrome, the file will be directly saved in C:\Users\[your user ID]\Downloads | The file is saved at the location you indicated. |  |
| 5 | Download XML Spreadsheet Template | In the Bank Accounts Export section, choose Download XML Spreadsheet Template.In the Save As dialog box, identify a location to save the XML spreadsheet template.Choose Save.Note Download processing steps varies on different browser, above steps apply to IE. If you are using Chrome, the file will be directly saved in C:\Users\[your user ID]\Downloads | The XML_Spreadsheet_Template.xml file is saved at the location you indicated. |  |
| 6 | Open XML Spreadsheet Template and Import Bank Account Master Data | Using Microsoft Excel to open XML_Spreadsheet_Template.xml.On the Microsoft Excel Developer tab, choose Import.Choose the Bank_Accounts.xml file in the Import XML dialog box.Choose Import. | Bank accounts master data have been imported into the XML spreadsheet template.If the system displays the message XML import error-Failed schema validation, but data have been imported from Bank_Accounts.xml, ignore this message and choose OK. |  |
| 7 | Export Data to a New XML File | On the Developer tab in Microsoft Excel, choose Export.Enter the file name Bank_Accounts_Export.xml and then choose Export. | Bank accounts master data is saved in Bank_Accounts_Export.xml. |  |

###### Import Bank Accounts

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

Import the exported bank accounts into the development system and consolidation test system.

|  |
| --- |
| Note You may only have one client for testing. You can test the function Export and Import the bank accounts with the same client. |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log onto the SAP Fiori launchpad as a Cash Management Specialist. |  |  |
| 2 | Access the SAP Fiori app | Open Manage Bank Accounts (F1366A). |  |  |
| 3 | Import and Export Accounts | Choose Import and Export Bank Accounts. | The Import and Export Bank Accounts screen displays. |  |
| 4 | Identify the Import Path | Choose Select File.In the Open dialog box, identify the XML (Bank_Accounts_Export.xml) to be uploaded.Choose Open. |  |  |
| 5 | Import with Test Run | Choose Import with Test Run and check the validation results.If the message Bank Account "1XXXXXXXXX" is already in approval process displays, we recommend that you import bank accounts next time, since some bank accounts are still in process workflow.When the message displays, only execute a test run, or complete the workflow before the production run.When the status of all validation results is OK, you can import bank accounts into production system. |  |  |
| 6 | Import XML File with Production Run | Choose Select File again.In the Open dialog box, identify the XML (Bank_Accounts.xml) to be uploaded.Choose Open.Choose Import and check the validation results. | Bank accounts are successfully imported into development system. |  |
| 7 | Import to Test System | Repeat the preceding steps to import bank accounts into consolidation test system. |  |  |

###### Approve Bank Account Request for Two-Person Verification

###### Option 1: Approve Bank Account Request by Using Manage Bank Account

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

A second operator can approve the new bank account.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori launchpad as a Cash Manager. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori app | Open Manage Bank Accounts (F1366A). |  |  |
| 3 | Select a Bank Account Number | Make the following entry and choose Go:Account Number: <Bank account number from prior procedure> | The bank account is listed. |  |
| 4 | Choose the Bank Account | Choose the arrow button to the right of the row of the bank account. |  |  |
| 5 | Approve | Choose Verify Changes.Choose Approve.Enter a Note: Approve the Bank Account.Choose Approve. |  |  |

###### Option 2: Approve Bank Account Request by Using Approve Bank Account Changes

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

A second operator can approve the new bank account.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori launchpad as a Cash Manager. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori app | Open Approve Bank Account Changes - Two-Person Verification (F6264). |  |  |
| 3 | Select a Request | Select the request which is created in the previous step. | Right panel displays the request detailed page.Approve and Reject buttons are enabled. |  |
| 4 | Approve | Choose Approve.Enter a Note: Approve the Bank Account.Choose Approve. |  |  |

##### Change Bank Account

###### Notify Bank to Change

Purpose

The bank accountant (Cash Management Specialist) goes to the bank and asks the bank employee to change the attributes of this bank account. This step does not occur in the system.

|  |
| --- |
| Note Bank account master data modification does not always result in a notification to the bank (for example, the modification of payment signatories). |

###### Change Bank Account

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This step describes how to change a bank account by bank accountant (Cash Management Specialist).

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori launchpad as a Cash Management Specialist. |  |  |
| 2 | Access the SAP Fiori app | Open Manage Bank Accounts (F1366A). |  |  |
| 3 | Choose the Bank Account to Change | Choose the bank account to be changed from the account list view.For example, account 0000000033108888 in AEBK3.Enter the filter and choose Go. | A new window displays. |  |
| 4 | Start to Edit | Choose Edit. Modify fields according to your requirements. |  |  |
| 5 | Save Your Changes | Choose Submit for Verification.Enter a Note: Changed a sensitive field house bank account ID.Choose Save.Note Only sensitive field updates will be submitted to another person to verify the changes. For non-sensitive fields, the bank account modification will be saved directly. | The bank account is changed (Inactive). |  |

|  |
| --- |
| Remember [Define Basic Settings](#unique_9) [page ] 12 must be reviewed following any system upgrade or improvement before continuing any business operation in the system. When differences are found from previous activations, you must correct the setting through the following IMG path: IMG > Financial Supply Chain Management > Cash and Liquidity Management > General Settings > Define Basic Settings via the user who has sufficient authorization to do the customizing. |

###### Withdraw Bank Account Request (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

Follow steps below to withdraw the bank account changes.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori launchpad as a Cash Management Specialist. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori app | Open Manage Bank Accounts (F1366A). |  |  |
| 3 | Select a Bank Account Number | Make the following entry and choose Go:Account Number: <Bank account number from prior procedure> | The bank account is listed. |  |
| 4 | Choose the Bank Account | Choose the arrow button to the right of the row of the bank account. |  |  |
| 5 | Withdraw Bank Account Changes | Choose Cancel Changes.Enter a Note: Cancel the Bank Account changes.Choose Cancel Changes.Note Only sensitive field being changed can trigger the withdraw bank account process. If the change is not related to sensitive field, the bank account will be saved directly. |  |  |

###### Update Bank G/L Account

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The key user updates the G/L account of the bank only when required. For example, if the currency key of the bank account is changed, the user updates the currency of G/L account. However, not all bank account modifications result in a G/L account modification.

|  |
| --- |
| Note Update the G/L accounts in the production, development, and consolidation test systems. |

Procedure

Depending on your configuration environment for SAP S/4HANA Cloud Public Edition, choose one of the following options:

Configure Your Solution:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. |  |  |
| 2 | Access the SAP Fiori app | Open Manage Your Solution (F1241). |  |  |
| 3 | Search Configuration | Open Configure Your Solution. | The Configure Your Solution: Realize Phase screen displays. |  |
| 4 | Access Configuration | Make the following entries and choose Go:Application Area: FinanceSub Application Area: General Ledger |  |  |
| 5 | Choose the G/L Account to Update | Choose the G/L account link. |  |  |
| 6 | Open | Choose the arrow at the right of the column with the Chart of Accounts item. |  |  |
| 7 | Select Configuration Step | For the Manage G/L Account Master Data SSCUI 150001 step, choose Configure. |  |  |
| 8 | Edit the Account | Choose Edit. |  |  |
| 9 | Choose Company Code | If prompted, choose the company code 3310 in which to change the G/L account. | The Manage G/L Account Master Data screen displays.Note You can also complete the test by logging on as General Ledger Accountant and use Manage G/L Account Master Data (F0731A). |  |
| 10 | Search for Your Account | Make the following entries and choose Go:Chart of Accounts: YCOAG/L Account: For example, 11001000View: Chart of Accounts View | Relevant bank subaccounts are updated. |  |
| 11 | Choose the G/L Account | Choose the triangle button on the right of the target G/L Account. |  |  |
| 12 | Edit the Account | Choose Edit. |  |  |
| 13 | Choose Company Code | Choose the company code 3310 in which to change the G/L account. | A screen showing the account parameters at the company code level displays. |  |
| 14 | Maintain the attributes of the G/L account at Company Code Level | Update the attributes of the account.For example, change Account Currency to a different currency from the one you used when creating a bank account in the previous step Create Bank Account Change Request, and deselect the checkbox of Only Balance in Local Currency. |  |  |
| 15 | Save the G/L Account | Choose Save. | The G/L account is updated successfully. |  |
| 16 | Update Bank Subaccount | Repeat the preceding steps to change bank subaccounts.For example, from 11001010 to 11001099. | Relevant bank subaccounts are updated. |  |

SAP Central Business Configuration:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the project experience in SAP Central Business Configuration. |  |  |
| 2 | Open Manage G/L Account Master Data | Go to the Business Processes Configuration app. To locate the activity in the tree view, search for the following activity: Manage G/L Account Master Data.Choose Open Documentation for the found line item to see more details about this configuration activity.Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. | The Manage G/L Account Master Data screen displays. |  |
| 3 | Edit the Account | Choose Edit. |  |  |
| 4 | Choose Company Code | If prompted, choose the company code 3310 in which to change the G/L account. | The Manage G/L Account Master Data screen displays.Note You can also complete the test by logging on as General Ledger Accountant and use Manage G/L Account Master Data (F0731A). |  |
| 5 | Search for Your Account | Make the following entries and choose Go:Chart of Accounts: YCOAG/L Account: For example, 11001000View: Chart of Accounts View | Relevant bank subaccounts are updated. |  |
| 6 | Choose the G/L Account | Choose the triangle button on the right of the target G/L Account. |  |  |
| 7 | Edit the Account | Choose Edit. |  |  |
| 8 | Choose Company Code | Choose the company code 3310 in which to change the G/L account. | A screen showing the account parameters at the company code level displays. |  |
| 9 | Maintain the attributes of the G/L account at Company Code Level | Update the attributes of the account.For example, change Account Currency to a different currency from the one you used when creating a bank account in the previous step Create Bank Account Change Request, and deselect the checkbox of Only Balance in Local Currency. |  |  |
| 10 | Save the G/L Account | Choose Save. | The G/L account is updated successfully. |  |
| 11 | Update Bank Subaccount | Repeat the preceding steps to change bank subaccounts.For example, from 11001010 to 11001099. | Relevant bank subaccounts are updated. |  |

|  |
| --- |
| Note Changing the currency is not possible when there is an existing balance for the G/L account. |

##### Repair Bank Accounts

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

You can change back the bank accounts to preceding status or preceding versions with following steps.

Prerequisite

You have finished the Define Repair Action for Bank Accounts configuration.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori launchpad as a Cash Management Specialist. |  |  |
| 2 | Access the SAP Fiori App | Open Manage Bank Accounts (F1366A). |  |  |
| 3 | Choose the Bank Account to Repair | Choose the bank account to be repaired from the account list view.For example, account 0000000033108888 in AEBK3.Enter the filter and choose Go. | A new window displays. |  |
| 4 | Start to Repairing | Choose Return to Preceding Status or Restore Predecessor Version.Note The button appear as Return to Preceding Status or Restore Predecessor Version are depend on the settings of preliminary step [Define Repair Action for Bank Accounts](#unique_32) [page ] 50. |  |  |
| 5 | Save | Make a note and Choose Return to Preceding Status or Restore Predecessor Version. |  |  |

##### Close Bank Account and Cancel Closing

###### Notify Bank to Close Account

Purpose

The bank accountant (Cash Management Specialist) goes to the bank and asks the bank employee to close the bank account. This step does not occur in the system.

###### Close Bank Account and Cancel Closing

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This step describes how to close an obsolete bank account by bank accountant (Cash Management Specialist) and the process of cancel the closing if you want to reactivate it.

Prerequisite

There are five indicators to display the status of a bank account.

| Status | Comment |
| --- | --- |
| Active | This status indicates bank account is successfully created in sap system and can be normally used. |
| Inactive | This status displayed in full cash management, it indicates bank account is initially created without being approved. |
| Closing Request Sent to Bank | This status indicates you have planned and informed the bank to close the bank account in a future date. After initial closing button is triggered and approved, the bank account status will be display as To be Closed. The function of bank account in status To be Closed is the same with bank account status active, for example, you can still normally use it as review bank account, make bank transfer, run payment, posting etc. |
| Closed at Bank | This status indicates the bank account has been closed by the bank. You can’t make bank transfer, run payment, review bank account, maintain payment approver, import signatory cards, monitor intraday/end of day bank statement and being displayed in bank relationship overview in this status. If you set a posting block date for a bank reconciliation account in Start to Confirm Closing at Bank step, no posting is allowed after that specific date. However, you can still make postings for other G/L accounts, unless the G/L accounts has been blocked from General Ledger Accounting side. |
| Closed | This status indicates the bank account is completely closed in sap system, no posting is allowed for bank reconciliation accounts, you can find bank reconciliation accounts details in online help: [Define G/L Accounts for Payment Processes](https://help.sap.com/docs/SAP_S4HANA_CLOUD/0fa84c9d9c634132b7c4abb9ffdd8f06/781544a06fc6476fa99755b96a3006be.html?locale=en-US). However, you can still make postings for other G/L accounts. Unless the G/L account has been blocked from General Ledger Accounting side, you can refer to online help: [Mark G/L Accounts as Not Used](https://help.sap.com/docs/SAP_S4HANA_CLOUD/0fa84c9d9c634132b7c4abb9ffdd8f06/2052bdb5d8fc4b6d9d787ea991e3613d.html?locale=en-US) and [G/L Accounts Blocked in P System Until Transport of Changes](https://help.sap.com/docs/SAP_S4HANA_CLOUD/0fa84c9d9c634132b7c4abb9ffdd8f06/e392432f0b2041528a118f8373f2269d.html?locale=en-US). |

|  |
| --- |
| Caution Do not close sample bank accounts that are connected to house bank AEBK1/AEAC1 and AEBK2/AEAC2 in the Connectivity Path tab for the bank master data (bank account 0000000693123456 of bank key 18121976, and bank account 0000000693123456 of bank key 18121986). The sample bank accounts are used when testing other scope items, for example, Accounts Payable (J60) and Advanced Cash Operations (J78). |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori launchpad as a Cash Management Specialist. |  |  |
| 2 | Access the SAP Fiori app | Open Manage Bank Accounts (F1366A). |  |  |
| 3 | Choose the Bank Account to Close | Choose the triangle button of the bank account to be closed.For example, account 0000000033108888 in AEBK3. |  |  |
| 4 | Mark for Closing | Choose Mark for Closing.Make the following entry in the dialog box and choose Mark for Closing.Planned Closing Date: for example, <current date + 2 days>Choose OK in the success dialog box. |  |  |
| 5 | Send Closing Request to Bank | Choose Send Closing Request to Bank. | The Send Closing Request to Bank dialog box is displayed. |  |
| 6 | Start to Initial Closing | Make the following entries in the dialog box and choose Send Closing Request to Bank:Planned Closing Date: for example, <current date + 2 days>Choose OK in the success dialog box.Refer to Approve Bank Account Request via Two-Person Verification step to activate the change request. | Bank account change request is created, and you have to refer to Activate Bank Account Closing Request step to activate the change request. After which the bank account’s status is changed to To Be Closed.If the email address is properly maintained, an e-mail is sent out to the relevant person in charge automatically.For more information on maintaining the e-mail address, see the Advanced Bank Account Management (J77) test script, Prerequisites > Preliminary Steps > Define Output Parameter Determination.The e-mail address maintained here takes precedence as the sender if it is valid. If it is not valid, the sender's e-mail address defaults to the company code's email address.In the Manage Bank Accounts (F1366A) app, find the 0000000033108888 bank account. Choose the account to access its master data page. A log entry is created in Bank Correspondence tab.The receiver is the Bank Contact Person. If Bank Contact Person is not maintained, the receiver is Bank Relationship Manager. If Bank Relationship Manager is not maintained, the receiver is the e-mail address maintained in the Bank. |  |
| 7 | Confirm Closing at Bank | Choose Confirm Closing at Bank. | The Confirm Closing at Bank dialog box is displayed. |  |
| 8 | Start to Confirm Closing at Bank | Make the following entries in the dialog box and choose Confirm Closing at Bank:Closing Date: for example, <current date>Note If Bank Reconciliation Account is set in House Bank Account Connectivity, you can input a posting blocking date. You use posting block date to set a final date for marking financial postings to this bank account. After the specified posting block date, posting is no longer allowed for this bank account. This date allows you to add an additional check for financial postings and help you maintain correct data for Advanced Valuation in Financial Accounting. You set the posting block date when you change the bank account status to Closed at Bank. You can update the posting block date as needed before the bank account is set to the Close status.Refer to Approve Bank Account Request via Two-Person Verification step to activate the change request. | A bank account change request has been created. Follow the steps in Approve Bank Account Request via Two-Person Verification to activate this request. Once completed, the bank account status will be updated to Closed at Bank. | You can choose confirm closing at bank without bank account initial closing. If you bypassing the initial closing procedure and choose confirm closing at bank, the bank account status will be changed to Closed at Bank directly. Output correspondence will be triggered, an e-mail is sent out to the relevant person in charge automatically, If the email address is properly maintained. |
| 9 | Complete Closing | Choose Complete Closing. |  | The actual balance of the bank account will be checked. The checking logic is defined in step Basic Settings. You can go to step Basic Settings to configure the Balance Check for Closing Process field as following:Blank: Balance Check Method (Deprecated)With this option set, you use the deprecated balance check method controlled via the configuration activity Change Message Control for Bank Account Management.10: No validation and close immediately.You set this option if you don't want to perform any bank account balance check when bank accounts are closed.20: Validate against aggregated actuals for amount in bank account currency in One Exposure.With this option set, the system checks the aggregated actuals of a bank account in One Exposure before the account is closed.Users can view the aggregated actuals for your bank account in the Bank Account Balance Reconciliation with Drill Down (FCLM_BANK_RECONCIL) app. To do so, in this app, do the following:In the Account Dimension field, select Bank Account (House Bank/House Bank Account).Set the reconciliation date as your current local date.In the Data Source Selection field, select Acnt Bal in Cash Pos (Tran Dt).Run the report. The Acnt Bal in Cash Position (Tran. Dt) field to show the aggregated actuals for bank accounts.To adjust the aggregated actuals for your bank account to produce zero, users can create a memo record to offset the current amount. To do so, in the Manage Memo Records 2.0 (F2986A) app, create a memo record with the memo record category Actual Cash Memo. Please note that the value date of the memo record must not be later than the bank account closing date. After the bank account balance is adjusted to zero, the bank account will no longer be visible in the report above.30: Validate against ledger balance (from bank statement).With this option set, the system checks the ledger balance of a bank account in the Manage Bank Account Balances (F5175) app before the account is closed. Only bank accounts for which the ledger balance is zero or has never been updated before can be closed.When the balance check error is shown, users need to ensure the ledger balance reflects the real balance of the bank account. They can import the latest bank statement that confirms the ledger balance is zero, or enter a ledger balance for this bank account in the Manage Bank Statements (F1564) app.To use option 30: Validate against ledger balance (from bank statement), make sure that all of your bank accounts are not set with the transfer mode No Update for Cash Management for end-of-day bank statements as the method requires that balance data is saved for cash management. |
| 10 | Start to Confirm Closing at Bank | Choose Complete Closing in the Complete Closing dialog box.Refer to Approve Bank Account Request via Two-Person Verification step to activate the change request. | A bank account change request has been created. Follow the steps in Approve Bank Account Request via Two-Person Verification to activate this request. Once completed, the bank account status will be updated to Closed. |  |
| 11 | Return to Closed at Bank | Choose Return to Preceding Status.Refer to Approve Bank Account Request via Two-Person Verification step to activate the change request. | A bank account change request has been created. Follow the steps in Approve Bank Account Request via Two-Person Verification to activate this request. Once completed, the bank account status will be updated to Closed at Bank. |  |
| 12 | Return to Closing Request Sent to Bank | Choose Return to Preceding Status.Refer to Approve Bank Account Request via Two-Person Verification step to activate the change request. | A bank account change request has been created. Follow the steps in Approve Bank Account Request via Two-Person Verification to activate this request. Once completed, the bank account status will be updated to Closing Request Sent to Bank. |  |
| 13 | Return to Active | Choose Return to Preceding Status.Refer to Approve Bank Account Request via Two-Person Verification step to activate the change request. | A bank account change request has been created. Follow the steps in Approve Bank Account Request via Two-Person Verification to activate this request. Once completed, the bank account status will be updated to Active. |  |

##### Maintain Payment Approver for Multiple Bank Accounts (Two-Person Verification Revision Activate)

Prerequisites

Approval patterns and payment approve group have to be defined and assigned to company code before you start following procedures. Make sure you have finished the prerequisite step of Payment Approval Customizing before you start to maintain payment approver. SAP has predelivered the sequential pattern P001 with payment approver group G001 and G002, and the non-sequential pattern s001 with payment approver group SG01 and SG02 as Demo data in Start system.

Use

This step describes how to maintain Payment Approver for multiple bank accounts with Full Cash Management and Two-Person Verification Revision Activate.

SAP supports sequential and non-sequential payment approval process.

- Sequential Payment Approver: The payment approval should obey the approver sequence. For example, if the Accounts Payable Manager is set as the first approver, the Cash Manager is set as the second approver. The Cash Manager cannot approve the payment before the Accounts Payable Manager in sequential Payment Approver case.
- Non-sequential Payment Approver: No sequence exists for the approvers. The Approver Group field decides the Payment Approver case you can choose.

|  |
| --- |
| Caution The following procedure assumes that you are only Maintaining Payment Approver for Multiple Accounts with Full Cash Procedures Management Using Two-Person Verification Revision Activate procedure. If you are implementing and testing additional Full Cash Management options, especially in a single environment, you cannot use the same Master Data values for more than one procedure type. You must create additional Master Data values, for example G/L Accounts, and then use these different values in each procedure type. |

###### Add Payment Approver for Multiple Bank Accounts

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you can trigger the mass maintenance of Payment Approver for multiple bank accounts. And one individual approve and confirm process is required for change Payment Approver requests to one Payment Approver group.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Cash Management Specialist. |  |  |
| 2 | Open SAP Fiori App | Open Maintain Payment Approver (WDA_FCLM_BAM_ADAPT_SIGN (APP_CFG_FCLM_BAM_ADAPT_SIGN)). |  |  |
| 3 | Select Company Code | Select company code in the filter header:Company Code: For example, 3310 and then choose Go to filter the results list. | Multiple bank accounts of the company code display in the Results List. |  |
| 4 | Select Bank Accounts | Select Bank Accounts rows in Results List:For example, bank account 0000000693123456 of bank key 18121976and bank account 0000000693123456 of bank key 18121986.Choose Add Payment Approver. | The Add Payment Approver screen displays. |  |
| 5 | Add Payment Approver to Payment Approver Group G001 | On the Add Payment Approver screen, make the following entries:New Approver: For example, <the user ID (CB*) has business role Accounts Payable Manager assigned>Valid From: For example, <current date>.Valid To: For example, 31.12.9999Payment Approver Group: G001Note The value above is used for sequential Payment Approver. If you want to use non-sequential Payment Approver, use SG01.Max. Amount for Payment: For example, 100,000.000Max. Amount for Batch: For example, 1,000,000.000The check box of Unlimited Approval is used for grant the authorization of approving unlimited amount. When you select this check box, the value of Maximum Amount for Payment and Maximum Amount for Batch will be invalid, the Payment Approver can approve an unlimited amount.Currency: AEDTitle: For example, Add Payment ApproverNote: Enter an explanatory noteChoose OK. | Change Payment Approver request to Payment Approver Group G001 has been created. |  |
| 6 | Add Payment Approver to Payment Approver Group G002 | Once Change Payment Approver request to Payment Approver Group G001 has been activated by the Cash Manager as described in the Activate the Bank Account after Payment Approver Maintenance procedure, repeat steps 2-4.On the Add Payment Approver screen, make the following entries:New Approver: For example, the user ID (CB*) of business user Cash Manager has business role Cash Manager assignedValid From: For example, <current date>Valid To: For example, 31.12.9999Payment Approver Group: For example, G002Note The value above is used for sequential Payment Approver. If you want to use nonsequential Payment Approver, use SG02.Max. Amount for Payment: For example, 100,000.000Max. Amount for Batch: For example, 1,000,000.000Currency: AEDTitle: For example, Add Payment ApproverNote: <Enter a note>Choose OK. | The bank account is changed (To be Active). |  |

###### Change Payment Approver for Multiple Bank Accounts

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you can make mass maintenance of Payment Approver in multiple bank accounts.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Cash Management Specialist. | The SAP Fiori launchpad is displayed. |  |
| 2 | Open SAP Fiori App | Open Maintain Payment Approver (WDA_FCLM_BAM_ADAPT_SIGN (APP_CFG_FCLM_BAM_ADAPT_SIGN)). | The Maintain Payment Approver - For Multiple Bank Accounts screen is displayed. |  |
| 3 | Select Company Code | Select company code in the filter header:Company Code: For example, 3310, and then choose Go to filter the results list. | Multiple bank accounts of the company code are displayed in the Results List. |  |
| 4 | Select Bank Accounts | Select Bank Accounts rows in Results List:For example, bank account 0000000693123456 of bank key 18121976and bank account 0000000693123456 of bank key 18121986.Choose Change Payment Approver. | Change Payment Approver screen is displayed. |  |
| 5 | Change Payment Approver | On the Change Payment Approver screen, make the following entries:New Payment Approver: For example, the user ID (CB*) has business role Cash Manager Specialist assignedValid From: For example, current date.Valid To: For example, 31.12.9999(New Payment Approver Section)Note Keep the Valid To date in Old Payment Approver section as current date.Choose OK. | The Payment Approver is changed for the bank account. |  |

###### Verify the Bank Account after Payment Approver Maintenance

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

A second operator can approve the newly changed bank account.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori launchpad as a Cash Manager. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori app | Open Manage Bank Accounts (F1366A). |  |  |
| 3 | Select a Bank Account Number | Make the following entries and choose Go:Account Number: <bank account number created in prior step> | The bank account is listed. |  |
| 4 | Choose the Bank Account | Select the bank account. | The Bank Account screen displays. |  |
| 5 | Verify Bank Account Changes | Choose Verify Changes.Choose Approve.Enter a Note: Approve the bank account.Choose Approve. |  |  |

##### Upload Attachments for Bank Account

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

You can upload attachments for the bank account.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Cash Management Specialist. |  |  |
| 2 | Access the SAP Fiori App | Open Manage Bank Accounts (F1366A). | The Manage Bank Accounts view displays. |  |
| 3 | Binding Cash Pools as Leading Account | Make the following entries and choose Go:Account Number: An active account. For example, 1133698 | Note If the basic setting is Direct Revision Activate, the bank account is activated. |  |
| 4 | Bank Account View | In the data table, choose the arrow icon at the right of the row for the account. | The Bank Account view displays. |  |
| 5 | Edit | Choose Edit. |  |  |
| 6 | Upload Attachments | Navigate to Attachments tabSelect Doc.Type to Upload: AttachmentsChoose Upload.Select a document to upload.Choose Submit for Activation. |  |  |

##### Approve Bank Account Request via Two-Person Verification

###### Check Bank Account Change Request

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

Cash Specialsit or Cash Manager can go to app Bank Account Change Request to check change request’s status

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori launchpad as a Cash Management Specialist or Cash Manager. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori app | Open Bank Account Change Requests - Two-Person Verification (F6265). |  |  |
| 3 | Filter the Request | Make the following entries and choose Go:Account Number: <bank account number from prior procedure> | The change request are listed. |  |
| 4 | Choose the Change Request | Choose the triangle button of the Change Reqeust. | Detailed information of the request dispalys. |  |

###### Option 1: Approve Bank Account Request by Using Manage Bank Account

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, a second operator can approve the changes that are made in previous steps.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori launchpad as a Cash Manager. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori app | Open Manage Bank Accounts (F1366A). |  |  |
| 3 | Select a Bank Account Number | Make the following entry and choose Go:Account Number: <Bank account number from prior procedure> | The bank account is listed. |  |
| 4 | Choose the Bank Account | Choose the triangle button of the bank account. |  |  |
| 5 | Approve | Choose Approve.Enter a Note: Approve the Bank Account.Choose Approve. |  |  |

###### Option 2: Approve Bank Account Request by Using Approve Bank Account Changes App

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, a second operator can approve the changes that are made in previous steps.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori launchpad as a Cash Manager. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori app | Open Approve Bank Account Changes - Two-Person Verification (F6264). |  |  |
| 3 | Select a Bank Account Num-ber | Select the request which is created in the previous step. | Right panel displays the request detailed page.Approve and Reject buttons are enabled. |  |
| 4 | Approve | Choose Approve.Enter a Note: Approve the Bank Account.Choose Approve. |  |  |

##### Bank Account Change Request Overview – Two-Person Verification

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

With this steps, you can get an overview of all the bank account change requests that were triggered in the two-person verification mode. You can also check the details of each bank account change request to see what is to be changed or has been changed.

Prerequisites

You have finished step [Define Basic Settings](#unique_9) [page ] 12 to set the Cash Scope as Full Scope and Bank Acc Revision as Activate Via Two-Person Verification.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori launchpad as a Cash Management Specialist. |  |  |
| 2 | Access the SAP Fiori app | Open Bank Account Change Requests - Two-Person Verification (F6265). |  |  |
| 3 | Enter Search Criteria | Make the following entries and choose Go:Bank Country/Region: AECompany Code: 3310 | Bank Account Change Requests displays. |  |
| 4 | Go into Detail Information | Choose the triangle button for a change request. | Detail information displays. |  |

#### Using Workflow Revision Activation

Purpose

The steps in this section describe the workflow process for bank account creation, update and close.

Prerequisites

You have finished step [Define Basic Settings](#unique_9) [page ] 12 to set the Cash Scope as Full Scope and Bank Acc Revision as Activation Via Workflow. Finish [Manage Workflows](#unique_12) [page ] 19 to set the workflow preconditions and the workflow type.

Only sensitive data can trigger workflow process. Make sure you have finished the [Configure Sensitive Fields (Optional)](#unique_15) [page ] 24 step before you start this section.

##### Create Bank Account

Purpose

The steps in this section describe the workflow for bank account creation.

|  |
| --- |
| Remember The [Define Basic Settings](#unique_9) [page ] 12 procedure must be reviewed following any system upgrade or improvement before continuing any business operation in the system. When differences are found from previous activations, you have to correct in the SSCUI Define Basic Settings |

Prerequisites

Before you execute this process, ensure that the basic Customizing for workflow is completed.

The customization is automatically completed in the SAP S/4HANA Enterprise Management Cloud system.

###### Open Bank Account

Purpose

The bank accountant (Cash Management Specialist) goes to the bank and opens a new bank account in this bank. This step does not occur in the system.

###### Create Bank Master Data

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you can create standard banks and internal banks master data with general information. For physical banks you should create it as standard banks, and for others you should create it as internal banks.

|  |
| --- |
| Note The app Manage Banks and Manage Banks Basic will be replaced by app Manage Banks - Master Data (F6437) and Manage Banks - Cash Management (F1574A) on SAP S/4HANA Cloud Public Edition2308. |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori launchpad as a Cash Management Specialist. |  |  |
| 2 | Access the SAP Fiori App | Open Manage Banks - Master Data (F6437). |  |  |
| 3 | Choose Create Bank | Choose Go for the banks to display in a list and choose Create Bank. | The Create Bank view displays. |  |
| 4 | Enter Criteria | Make the following entries:Bank Country/Region: AEBank Key: 88800011Choose Create Bank. |  |  |
| 5 | Enter General Data | Make the following entries:Bank Name: AEStandard Bank for Advanced Bank Account Management Workflow ModeChoose Create. | The standard bank is created. |  |
| 6 | Create Internal Banks | Go to the initial page of app Manage Banks - Master Data (F6437).Choose the triangle button beside the Create.Choose Create Internal Bank. |  |  |
| 7 | Enter Control Data | Make the following entries:Bank Country/Region: AEBank Key: 88888889Internal Bank Category: Payment Service ProviderChoose Create Internal Bank.Note If the bank key created is used for an internal virtual bank, for example, PayPal,which is used as House Bank, please select Internal - Payment Service Provider.which is used to enable the maintenance of the business partner bank details with alias, please select the Payment system. For more details, please refer to SSCUIs 105361 - Define Alias Types and 105362 - Define Payment Systems. |  |  |
| 8 | Enter General Data | Make the following entries:Bank Name: Internal Bank 3Choose Create. | The Internal bank is created. |  |

###### Edit Bank Master Data

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The purpose of this step is to edit bank and input more bank information in production system.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Cash Management Specialist. |  |  |
| 2 | Access the SAP Fiori App | Open Manage Banks - Master Data (F6437). |  |  |
| 3 | Filter the Bank | Make the following entry in the filter and choose Go.Bank Key: 88800011 |  |  |
| 4 | Choose the Bank | Choose the Bank in the list. |  |  |
| 5 | Edit Bank | Choose Edit.Make the following entries:SWIFT/BIC: DEUTDEFFXX1City: for example, 60040 Frankfurt, Main |  |  |
| 5 | Save Your Entries | Choose Save. |  |  |

###### Create Bank G/L Accounts

Purpose

The General Ledger Accountant may create the G/L accounts for the new bank account.

|  |
| --- |
| Note In cash management in this package, you can use the same G/L accounts (bank main account and bank subaccount) for different bank accounts when they use the same currency key. The balance of each bank account can be displayed in the cash management SAP Fiori apps, instead of checking the relevant G/L account balances. Using this approach keeps the chart of accounts smaller. |

|  |
| --- |
| Note If you want to create a new G/L account for a new bank account, execute the following steps. Create G/L accounts in production system, development system, and consolidation test system. |

|  |
| --- |
| Note This procedure is mentioned in the Accounting and Financial Close (J58) test script. See the Manage G/L Account Master Data step and copy an existing G/L Account to a new one, for example, copy 11001000 to 11003000. |

###### Manage Banks Cash Management Data

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you can input banks data that is used for cash management.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori launchpad as a Cash Management Specialist. |  |  |
| 2 | Access the SAP Fiori App | Open Manage Banks - Cash Management (F1574A). |  |  |
| 3 | Enter Search Criteria | Make the following entries:Bank Country/Region: AEBank Key: 88800011If the Bank Key field is not visible, choose Filters to unhide it.Choose Go.Go into the detail of the bank. | The Display Bank view appears. |  |
| 4 | Enter Risk Business Partner | Choose Edit.Make the following entry:Risk Business Partner: for example, 55555 | The Manage Banks view displays. |  |
| 5 | Enter House Bank Data | Go to House Banks tab and choose Create.Make the following entries:Company Code: 3310House Bank: AEBK3Choose Continue.Choose Apply. |  |  |
| 6 | Enter Netting Business Partner | Go to Netting Business Partner tab.Make the following entries:Valid From: <Current Date>.Valid To: <Futrue Date>.Business Partner: <Choose one by using search help> |  |  |
| 7 | Save Bank | Choose Save. | New house bank is saved successfully. |  |

###### Create Bank Account Request

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This step describes how to create a new bank account request by a bank accountant (Cash Management Specialist). The request is then sent to Cash Manager's inbox (My Inbox).

|  |
| --- |
| Note Since bank accounts are not transportable to the production system, they must be maintained manually there. |

|  |
| --- |
| Remember The [Define Basic Settings](#unique_9) [page ] 12 topic in the Prerequisites section must be reviewed following any system upgrade or improvement before continuing any business operations in the system. When differences are found from previous activations, you have to correct in the SSCUI 101025 Define Basic Settings. In this setting, set the Cash Scope field to Full Scope and the Bank Account Control Mode field to Workflow. |

Prerequisite

You have completed the steps in Manage Workflows topics.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Cash Management Specialist. |  |  |
| 2 | Access the SAP Fiori App | Open Manage Bank Accounts (F1366A). |  |  |
| 3 | Create a New Bank Account | Choose Create to add a new bank account.Make the following entries.Company Code: 3310Account Type: 01 | The Bank Account view displays. |  |
| 4 | Maintain Header Data of New Bank Account | Choose the Header tab and enter the following values.Currency: for example, AEDAccount Description: AEBank Account for Advanced Bank Account Management Workflow ModeBank Country/Region: AEBank Key: 88800011Account Number: 0000000033108888 |  |  |
| 5 | Enter General Data | Make the following entries:Company Code: 3310Account Holder: Company Code3310 (company code name is usually defaulted by system)Account Type: for example, 01 Current AccountIBAN: <Generate IBAN>Note Only perform this step if the country is using IBAN; if you do not use IBAN in your process, just skip this step.Bank Control Key: for example, PNote Bank Control Key is only used in some countries like France, Spain, Italy. If you don't use Bank Control Key, you should leave this field blank. |  |  |
| 6 | Bank Relationship Data | Pmnt Tran Type Group: CAMT053Note The field Transaction Type is not available for on premise. To assign the Transaction Type to your Bank Account use the IMG Menu Path: Financial Accounting > Bank Accounting > Business Transactions > Payment Transactions > Electronic Bank Statement > Make Global Settings for Electronic Bank StatementsNote If you are going to upload camt.054 format bank statement for supplier financing, which is described in test script 1EG, the field Pmnt Tran Type Group has to be maintained as camt053, otherwise camt054 bank statement can't be uploaded. |  |  |
| 7 | Maintain Contact Persons | Choose the Bank Relationship tab.In the Contact Persons area, make the following entries:Internal Bank Account Contact: <ID assigned to the Cash Management Specialistrole>Internal Bank Account Supervisor: <ID assigned to the Cash Managerrole> |  |  |
| 8 | Choose Bank Relationship Tab | In the Bank Statement Data area, make the following entries:Planning Level: <Select a planning level>Processing Status: <selected>Interval: for example, 01Interval Unit: for example, MonthsFactory Calendar ID: for example, 01Note Processing Status: Indicates if you should monitor this bank account at the end of the day using the Bank Status MonitorInterval: Specifies how often the bank statements for a bank account are imported to your system.Interval Unit: Specifies the unit of measurement for an interval.Factory Calendar ID: Distinguishes between working days and non-working days. |  |  |
| 9 | Choose House Bank Account Connectivity | Choose the House Bank Account Connectivity tab. | The House Bank Account Connectivity tab appears. | House Bank Account Connectivity allows you to associate a bank account with its house bank account in the central system where SAP S/4HANA Cloud Public Edition Finance for Cash Management is installed. It also enables connections to accounts in remote SAP or third-party systems. For additional information, please refer to the online help [Define House Bank Account Connectivity](https://help.sap.com/docs/SAP_S4HANA_CLOUD/186460fdc35a4b64a713da9bb00deb1e/2abbcf54a14a713be10000000a44176d.html?version=LATEST&locale=en-US). |
| 10 | Maintain House Bank Account Connectivity | Choose Create and make the following entries:ID Category: Indicates whether; for example, Central System: House Bank AccountRemote System: <Leave blank>If the house bank account only exist in the local system you can specify the ID Category as Central System: House Bank Account; If the house bank account exist in remote system, and need to be migrated to local system, you can specify the ID Category to Remote System: House Bank AccountNote If you have enabled the Convert Remote House Bank Accounts functionality in the configuration activity Define System Groups (107199), please ensure that all necessary attributes for the remote house bank accounts to be replicated are properly maintained prior to their conversion to the ID category Central System: House Bank Account. These accounts are then replicated back to the originating target system. Incorrect or missing attributes may result in validation errors in the target systems. For further information, please refer to the online help [Define House Bank Account Connectivity](https://help.sap.com/docs/SAP_S4HANA_CLOUD/186460fdc35a4b64a713da9bb00deb1e/2abbcf54a14a713be10000000a44176d.html?version=LATEST&locale=en-US) and [Outbound Integration](https://help.sap.com/docs/SAP_S4HANA_CLOUD/186460fdc35a4b64a713da9bb00deb1e/9b57a8997a02462989f2d0b168dac811.html?version=LATEST&locale=en-US).Company Code: 3310House Bank: AEBK3Valid From: for example, If the house bank account only exist in the local system you can<current date>Valid To: for example, 31.12.9999House Bank Acct ID: AEAC3Use in Cash Pooling: DeselectedNote The Use in Cash Pooling field determines if the house bank account is used for cash pooling. If the checkbox is selected, this house bank account can be used for cash pooling. If there are multiple house bank accounts for one bank account, only one house bank account can be used for cash pooling. |  |  |
| 11 | Maintain House Bank Account Data | Maintain the following entries in the House Bank Account Data tab:G/L Account: 11001000Choose Apply.Note If the account does not exist in your system, add the account by following the steps in the Create G/L Account and Cost Element - MDS (BNG) master data script. | The house bank account ID maintained here is called by other applications (for example, payment program, and bank statement). |  |
| 12 | Choose Payment Approvers tab | Choose the Payment Approvers tab. |  |  |
| 13 | Maintain Payment Approver for Payment Approver Group G001 | Make the following entries:Note Make sure you have finished the prerequisite step of Payment Approval Customizing, before you start maintain approver.Payment Approver Group: for example, G001 (the first step of two-step approval)Payment Approver: for example, the user ID assigned with the Accounts Payable Manager business roleCurrency: AEDMax. Amount for Payment: for example, 10,000,000.00Max. Amount for Batch Payment: for example, 50,000,000.00Note If the Unlimited Approval check box is selected, the payment approver can approve unlimited amount.Valid From: for example, <current date>.Valid To: for example, 31.12.9999 | The Payment Approver Group G001 is maintained. |  |
| 14 | Maintain Payment Approver for Payment Approver Group G002 | Repeat the previous step to create a User ID to Payment Approver group G002 (The second step for two-step approval).Use the same values in previous step, except that Payment Approver Group is (G002).For Payment Approver, enter the user ID assigned with the Cash Manager business role. The user ID assigned MUST be different from the user ID assigned to G001. | The Payment Approver Group G002 is maintained. |  |
| 15 | Check Approval Information | Choose Show Approval Step.You can find the detail information about approval sequence, approval amount for each approver. |  |  |
| 16 | Overdraft Limits | Make the following entries:Overdraft Type: SO01Overdraft Type Description: Overnight OverdraftOverdraft Category: Overnight OverdraftAmount: 10000 AEDValid From: Current DateValid To: 12/31/9999Note The valid period for the same overdraft type cannot overlap. You can maintain Overdraft Type in SSCUI 107092 Define Bank Account Overdraft Limit Types. |  | Overdraft Limit Type is controlled by Customer Control Feature Toggle FTGL_BAM_BKACCT_OVERDRAFT_TYPE, the feature toggle is deactivated by default. You can activate the feature toggle in SSCUI 106573 Activate Features. If the feature toggle is not activated, fields Overdraft Type, Overdraft Type Description and Overdraft Category will be hidden, SSCUI 107092 Define Bank Account Overdraft Limit Types will also be invisible. |
| 17 | Save and Activate Bank Account for Origination Process Enabled Scenario | Note This step can be executed if Bank Account Origiantion Process has been enabled, otherwise skip this step.Ensure all necessary data have been entered and choose Save.You can choose edit and enrich the data if necessary, then choose Start Opening.Choose Confirm Opening at Bank.Note The step of choosing Start Opening and choosing Confirm Opening at Bank is depending on the Prelimi-nary step Enable Bank Account Origination Process setting. Only if the status 24 Pre-Opening Preparation has been configured and its enable status check box has been selected, you can execute the step Send Open Request to Bank. And only if the status 24 In Opening Process has been configured and its enable status check box has been selected, you can execute the step Confirm Opening at Bank. |  |  |
| 18 | Save Your Changes | Ensure all necessary data have been entered and choose Save as Inactive.Choose Submit for Approval. | The change request is created. |  |

###### Export Bank Accounts

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The bank account modification in the production system is completed in the previous step. Because some system configuration is based on house bank and house bank account, after a bank account’s attribute is changed, you may need to update the configuration in the development system or consolidation test system. You can use Export/Import Bank Accounts functionality to faciliate your bank accounts' update.

Prerequisites

- You use Microsoft Office 2010 or higher that contains Microsoft Excel
- The Developer tab in Microsoft Excel is enabled.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log onto the SAP Fiori launchpad as a Cash Management Specialist. |  |  |
| 2 | Access the SAP Fiori app | Open Manage Bank Accounts (F1366A). |  |  |
| 3 | Upload/download Account | Choose Import and Export Bank Accounts. | The Import and Export Bank Accounts screen displays. |  |
| 4 | Export Bank Master Data XML file | In the Bank Accounts Export section, enter company code and choose Go. Select the check box of the bank accounts, and choose Export Bank Accounts to an XML File.In the File Download dialog box, choose Save As.In the Save As dialog box, identify a location to save the XML file.Choose Save.Note Download processing steps varies on different browser, above steps apply to IE. If you are using Chrome, the file will be directly saved in C:\Users\[your user ID]\Downloads | The file is saved at the location you indicated. |  |
| 5 | Download XML Spreadsheet template | In the Bank Accounts Export section, choose Download XML Spreadsheet Template.In the Save As dialog box, identify a location to save the XML spreadsheet template.Choose Save.Note Download processing steps varies on different browser, above steps apply to IE. If you are using Chrome, the file will be directly saved in C:\Users\[your user ID]\Downloads | The XML_Spreadsheet_Template.xml file is saved at the location you indicated. |  |
| 6 | Open XML Spreadsheet Template and Import Bank Account Master Data | Using Microsoft Excel to open XML_Spreadsheet_Template.xml.In the Microsoft Excel Developer tab, choose Import.Choose the Bank_Accounts.xml file in the Import XML dialog box.Choose Import. | Bank accounts master data have been imported into the XML spreadsheet template.If the system displays the message XML import error-Failed schema validation displays, but data have been imported from Bank_Accounts.xml, ignore this message and choose OK. |  |
| 7 | Export Data to a New XML File | In the Developer tab in Microsoft Excel, choose Export.Enter the file name Bank_Accounts_Export.xml and then choose Export. | Bank accounts master data is saved in Bank_Accounts_Export.xml. |  |

###### Import Bank Accounts

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This instruction guides you how to import the bank accounts into the target system, if you use Solution Builder environment with 2 system landscape, or use SAP Central Business Configuration with 2 system landscape, you may use this functinality to update your test system. If you use On-Premise system or use SAP Central Business Configuration with 3 system landscape, the development system can also be updated besides the test system.

|  |
| --- |
| Note You may only have one client for testing. You can test the function Export and Import the bank accounts in the same client. |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log onto the SAP Fiori launchpad as a Cash Management Specialist. |  |  |
| 2 | Access the SAP Fiori app | Open Manage Bank Accounts (F1366A). |  |  |
| 3 | Import and Export Accounts | Choose Import and Export Bank Accounts. | The Import and Export Bank Accounts screen displays. |  |
| 4 | Identify the Import Path | Choose Select File.In the Open dialog box, identify the XML (Bank_Accounts_Export.xml) to be uploaded.Choose Open. |  |  |
| 5 | Import with Test Run | Choose Import with Test Run and check the validation results.Note If the message Bank Account "1XXXXXXXXX" is already in approval process displays, we recommend that you import bank accounts next time, since some bank accounts are still in process workflow.When the message displays, only execute a test run, or complete the workflow before the production run.When the status of all validation results is OK, you can import bank accounts into production system. |  |  |
| 6 | Import XML file with Production Run | Choose Select File again.In the Open dialog box, identify the XML (Bank_Accounts.xml) to be uploaded.Choose Open.Choose Import and check the validation results. | Bank accounts are successfully imported into development system.Note If you import full tabs bank account to a target system with hide tabs bank account, the bank account information in the hide tabs will not be imported. |  |
| 7 | Import to Test System | Repeat the preceding steps to import bank accounts into consolidation test system. |  |  |

###### Change Bank Account During Workflow (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Prerequisite

This function only applies to extensive system.

Purpose

The new bank account request is sent to the bank account worklist (inbox) for the Cash Manager. The Cash Manager can change the bank account before finally approve it.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori launchpad as a Cash Manager. |  |  |
| 2 | Access the SAP Fiori app | Open My Inbox - For Bank Accounts (F2797). | The Work Items for Bank Accounts displays. |  |
| 3 | Locate the open bank account Request | Choose a request for the change from the left pane. | The detailed information of bank account requests displays. |  |
| 4 | Edit the Request | Choose the link of bank account technical ID. | Navigate to revision detail page.Edit button is enabled. |  |
| 5 | Start to Edit | Choose Edit.Modify fields to your requirements.Choose Submit for Approval | The revision detail page is updated and waiting for approval. |  |

##### Change Bank Account

Context

This step describes how to change an existing bank account and workflow of bank account change management.

|  |
| --- |
| Caution Do not change sample bank accounts that are connected to house bank AEBK1 and AEBK2 in the Connectivity Path tab for the bank master data (bank account 0000000693123456 of bank key 18121976, and bank account 0000000693123456 of bank key 18121986). The sample accounts are also used for testing other scope items, for example, Accounts Payable (J60) and Advanced Cash Operations (J78). |

###### Receive Change Request from Requester

Purpose

The bank accountant (Cash Management Specialist) receives a change request from other colleagues; for example, another colleague request to change the currency key for a bank account.

###### Create Bank Account Change Request

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This step describes how to create a bank account change request by bank accountant (Cash Management Specialist). The request is then sent to the Cash Manager's inbox (My Inbox).

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log onto the SAP Fiori launchpad as a Cash Management Specialist. |  |  |
| 2 | Access the SAP Fiori app | Open Manage Bank Accounts (F1366A). | The Bank Hierarchy: Active Accounts screen displays. |  |
| 3 | Enter Selection Criteria | On the current screen, make the following entries:Company Code: 3310Choose Go. |  |  |
| 4 | Choose the Bank Account to Change | Choose the bank account to be changed from the account list view.For example, account 0000000033108888 | A new window displays. |  |
| 5 | Start to Edit | Choose Edit.Modify fields to your requirements. |  |  |
| 6 | Choose Payment Approvers tab | Choose Payment Approvers. |  |  |
| 7 | Edit Payment Approvers | Make the following changes for both lines of group G001 and G002:Currency: the changed currency valueNote If the Unlimited Approval check box is selected, the payment approver can approve unlimited amount. |  |  |
| 8 | Choose Overdraft Limits tab | Choose the Overdraft Limits tab. |  |  |
| 9 | Edit Overdraft Limits | Make the following changes for each line.Currency: <the changed currency value> |  |  |
| 10 | Save Your Changes | Choose Submit for Approval. | Change request XXXXXXXXXXXX is created. |  |

|  |
| --- |
| Remember The [Define Basic Settings](#unique_9) [page ] 12 procedure must be reviewed following any system upgrade or improvement before continuing any business operation in the system. When differences are found from previous activations, you have to correct in the SSCUI Define Basic Settings. |

|  |
| --- |
| Note When you change the value of any of the following sensitive fields, the workflow can be triggered. You must complete the workflow process. Otherwise, changing one of the other values of the bank account does not trigger the workflow process, and the bank account must be changed and activated directly.IBAN (International Bank Account Number)Overdraft Limit AmountOverdraft Limit Amount Currency KeyMaximum Amount for Payment BatchPayment SignatoryMaximum Amount for PaymentSignatory: Valid ToCash Pool (Header Account)Cash Pool (Subaccount)Cash Pool Minimum Transfer AmountCash Pool Maximum Transfer AmountCash Pool Target BalanceCash Pool Payment methodReconciliation Intraday Memo RecordsTolerance Group for ReconciliationRule for Intraday StatementsUpload of Intraday Statements |

###### Change Bank Account During Workflow (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Prerequisite

This function only applies to extensive system.

Purpose

The new bank account request is sent to the bank account worklist (inbox) for the Cash Manager. The Cash Manager can change the bank account before finally approve it.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori launchpad as a Cash Manager. |  |  |
| 2 | Access the SAP Fiori app | Open My Inbox - For Bank Accounts (F2797). | The Work Items for Bank Accounts displays. |  |
| 3 | Locate the open bank account Request | Choose a request for the change from the left pane. | The detailed information of bank account requests displays. |  |
| 4 | Edit the Request | Choose the link of bank account technical ID. | Navigate to revision detail page.Edit button is enabled. |  |
| 5 | Start to Edit | Choose Edit.Modify fields to your requirements.Choose Submit for Approval | The revision detail page is updated and waiting for approval. |  |

###### Notify Bank to Change

Purpose

The bank accountant (Cash Management Specialist) goes to the bank and asks the bank employee to change the attributes of this bank account. This step does not occur in the system.

|  |
| --- |
| Note Bank account master data modification does not always result in a notification to the bank (for example, the modification of payment signatories). |

###### Update Bank G/L Account

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The key user updates the G/L account of bank only when updating is required. For example, if the currency key of bank account is changed, the user updates the currency of G/L account. However, not all bank account modifications result in a G/L account modification.

|  |
| --- |
| Note Update the G/L accounts in the production, development, and consolidation test systems. |

Procedure

Depending on your configuration environment for SAP S/4HANA Cloud Public Edition, choose one of the following options:

Configure Your Solution:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. |  |  |
| 2 | Access the SAP Fiori app | Open Manage Your Solution (F1241). |  |  |
| 3 | Search Configuration | Open Configure Your Solution. | The Configure Your Solution: Realize Phase screen displays. |  |
| 4 | Access Configuration | Make the following entries and choose Go:Application Area: FinanceSub Application Area: General Ledger |  |  |
| 5 | Choose the G/L Account to Update | Choose the G/L account link. |  |  |
| 6 | Open | Choose the arrow at the right of the column with the Chart of Accounts item. |  |  |
| 7 | Select Configuration Step | For the Manage G/L Account Master Data SSCUI 150001 step, choose Configure. |  |  |
| 8 | Edit the Account | Choose Edit. |  |  |
| 9 | Choose Company Code | If prompted, choose the company code 3310 in which to change the G/L account. | The Manage G/L Account Master Data screen displays.Note You can also complete the test by logging on as General Ledger Accountant and use Manage G/L Account Master Data (F0731A). |  |
| 10 | Search for Your Account | Make the following entries and choose Go:Chart of Accounts: YCOAG/L Account: For example, 11001000View: Chart of Accounts View | Relevant bank subaccounts are updated. |  |
| 11 | Choose the G/L Account | Choose the triangle button on the right of the target G/L Account. |  |  |
| 12 | Edit the Account | Choose Edit. |  |  |
| 13 | Choose Company Code | Choose the company code 3310 in which to change the G/L account. | A screen showing the account parameters at the company code level displays. |  |
| 14 | Maintain the attributes of the G/L account at Company Code Level | Update the attributes of the account.For example, change Account Currency to a different currency from the one you used when creating a bank account in the previous step Create Bank Account Change Request, and deselect the checkbox of Only Balance in Local Currency. |  |  |
| 15 | Save the G/L Account | Choose Save. | The G/L account is updated successfully. |  |
| 16 | Update Bank Subaccount | Repeat the preceding steps to change bank subaccounts.For example, from 11001010 to 11001099. | Relevant bank subaccounts are updated. |  |

SAP Central Business Configuration:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the project experience in SAP Central Business Configuration. |  |  |
| 2 | Open Manage G/L Account Master Data | Go to the Business Processes Configuration app. To locate the activity in the tree view, search for the following activity: Manage G/L Account Master Data.Choose Open Documentation for the found line item to see more details about this configuration activity.Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. | The Manage G/L Account Master Data screen displays. |  |
| 3 | Edit the Account | Choose Edit. |  |  |
| 4 | Choose Company Code | If prompted, choose the company code 3310 in which to change the G/L account. | The Manage G/L Account Master Data screen displays.Note You can also complete the test by logging on as General Ledger Accountant and use Manage G/L Account Master Data (F0731A). |  |
| 5 | Search for Your Account | Make the following entries and choose Go:Chart of Accounts: YCOAG/L Account: For example, 11001000View: Chart of Accounts View | Relevant bank subaccounts are updated. |  |
| 6 | Choose the G/L Account | Choose the triangle button on the right of the target G/L Account. |  |  |
| 7 | Edit the Account | Choose Edit. |  |  |
| 8 | Choose Company Code | Choose the company code 3310 in which to change the G/L account. | A screen showing the account parameters at the company code level displays. |  |
| 9 | Maintain the attributes of the G/L account at Company Code Level | Update the attributes of the account.For example, change Account Currency to a different currency from the one you used when creating a bank account in the previous step Create Bank Account Change Request, and deselect the checkbox of Only Balance in Local Currency. |  |  |
| 10 | Save the G/L Account | Choose Save. | The G/L account is updated successfully. |  |
| 11 | Update Bank Subaccount | Repeat the preceding steps to change bank subaccounts.For example, from 11001010 to 11001099. | Relevant bank subaccounts are updated. |  |

|  |
| --- |
| Note Changing the currency is not possible when there is an existing balance for the G/L account. |

##### Repair Bank Accounts

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

You can change back the bank accounts to preceding status or preceding versions with following steps.

Prerequisite

You have finished the Define Repair Action for Bank Accounts configuration.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori launchpad as a Cash Management Specialist. |  |  |
| 2 | Access the SAP Fiori App | Open Manage Bank Accounts (F1366A). |  |  |
| 3 | Choose the Bank Account to Repair | Choose the bank account to be repaired from the account list view.For example, account 0000000033108888 in AEBK3.Enter the filter and choose Go. | A new window displays. |  |
| 4 | Start to Repairing | Choose Return to Preceding Status or Restore Predecessor Version.Note The button appear as Return to Preceding Status or Restore Predecessor Version are depend on the settings of preliminary step [Define Repair Action for Bank Accounts](#unique_32) [page ] 50. |  |  |
| 5 | Save | Make a note and Choose Return to Preceding Status or Restore Predecessor Version. |  |  |

##### Close Bank Account and Cancel Closing

Context

This step describes how to close an obsolete bank account and workflow of bank account closing.

|  |
| --- |
| Caution Do not close sample bank accounts that are connected to house bank AEBK1 and AEBK2 in the Connectivity Path tab for the bank master data (bank account 0000000693123456 of bank key 18121976, and bank account 0000000693123456 of bank key 18121986). The sample bank accounts are used when testing other scope items, for example, Accounts Payable (J60) and Advanced Cash Operations (J78). |

###### Receive Bank Account Closing Request from Requester

Purpose

The bank accountant (Cash Management Specialist) receives a request to close an existing bank account from other colleagues. For example, the company no longer needs this bank account.

###### Notify Bank to Close Account

Purpose

The bank accountant (Cash Management Specialist) goes to the bank and asks the bank employee to close the bank account. This step does not occur in the system.

###### Close Bank Account and Cancel Closing

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This step describes how to close an obsolete bank account by bank accountant (Cash Management Specialist) and the process of cancel the closing if you want to reactivate it.

Prerequisite

There are five indicators to display the status of a bank account.

| Status | Comment |
| --- | --- |
| Active | This status indicates bank account is successfully created in sap system and can be normally used. |
| Inactive | This status displayed in full cash management, it indicates bank account is initially created without being approved. |
| Closing Request Sent to Bank | This status indicates you have planned and informed the bank to close the bank account in a future date. After initial closing button is triggered and approved, the bank account status will be display as Closing Request Sent to Bank. The function of bank account in status Closing Request Sent to Bank is the same with bank account status active, for example, you can still normally use it as review bank account, make bank transfer, run payment, posting etc. |
| Closed at Bank | This status indicates the bank account has been closed by the bank. You can’t make bank transfer, run payment, review bank account, maintain payment approver, import signatory cards, monitor intraday/end of day bank statement and being displayed in bank relationship overview in this status. If you set a posting block date for a bank reconciliation account in Start to Confirm Closing at Bank step, no posting is allowed after that specific date. However, you can still make postings for other G/L accounts, unless the G/L accounts has been blocked from General Ledger Accounting side. |
| Closed | This status indicates the bank account is completely closed in sap system, no posting is allowed for bank reconciliation accounts, you can find bank reconciliation accounts details in online help: [Define G/L Accounts for Payment Processes](https://help.sap.com/docs/SAP_S4HANA_CLOUD/0fa84c9d9c634132b7c4abb9ffdd8f06/781544a06fc6476fa99755b96a3006be.html?locale=en-US). However, you can still make postings for other G/L accounts. Unless the G/L account has been blocked from General Ledger Accounting side, you can refer to online help: [Mark G/L Accounts as Not Used](https://help.sap.com/docs/SAP_S4HANA_CLOUD/0fa84c9d9c634132b7c4abb9ffdd8f06/2052bdb5d8fc4b6d9d787ea991e3613d.html?locale=en-US) and [G/L Accounts Blocked in P System Until Transport of Changes](https://help.sap.com/docs/SAP_S4HANA_CLOUD/0fa84c9d9c634132b7c4abb9ffdd8f06/e392432f0b2041528a118f8373f2269d.html?locale=en-US). |

|  |
| --- |
| Caution Do not close sample bank accounts that are connected to house bank AEBK1/AEAC1 and AEBK2/AEAC2 in the Connectivity Path tab for the bank master data (bank account 0000000693123456 of bank key 18121976, and bank account 0000000693123456 of bank key 18121986). The sample bank accounts are used when testing other scope items, for example, Accounts Payable (J60) and Advanced Cash Operations (J78). |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori launchpad as a Cash Management Specialist. |  |  |
| 2 | Access the SAP Fiori app | Open Manage Bank Accounts (F1366A). |  |  |
| 3 | Choose the Bank Account to Close | Choose the triangle button of the bank account to be closedFor example, account 0000000033108888 in BANK3. |  |  |
| 4 | Mark for Closing | Choose Mark for Closing.Make the following entry in the dialog box and choose Mark for Closing.Planned Closing Date: for example, <current date + 2 days>Choose OK in the success dialog box. |  |  |
| 5 | Send Closing Request to Bank | Choose Send Closing Request to Bank. | The Send Closing Request to Bank dialog box is displayed. |  |
| 6 | Start to Initial Closing | Make the following entries in the dialog box and choose Send Closing Request to Bank:Planned Closing Date: for example, <current date + 2 days>Choose OK in the success dialog box.Refer to Approve Bank Account Request via Workflow step to activate the change request. | Bank account change request is created, and you have to refer to Approve Bank Account Closing Request step to activate the change request. After which the bank account’s status is changed to Closing Request Sent to Bank.If the email address is properly maintained, an e-mail is sent out to the relevant person in charge automatically.For more information on maintaining the e-mail address, see the Advanced Bank Account Management (J77) test script, Prerequisites > Preliminary Steps > Define Output Parameter Determination .The e-mail address maintained here takes precedence as the sender if it is valid. If it is not valid, the sender's e-mail address defaults to the company code's email address.In the Manage Bank Accounts (F1366A) app, find the 0000000033108888 bank account . Choose the account to access its master data page. A log entry is created in Bank Correspondence tab.Note The receiver is the Bank Contact Person. If Bank Contact Person is not maintained, the receiver is Bank Relationship Manager. If Bank Relationship Manager is not maintained, the receiver is the e-mail address maintained in the Bank. |  |
| 7 | Confirm Closing at Bank | Choose Confirm Closing at Bank. | The Confirm Closing at Bank dialog box is displayed. |  |
| 8 | Start to Confirm Closing at Bank | Make the following entries in the dialog box and choose Confirm Closing at Bank:Closing Date: for example, <current date>Note If Bank Reconciliation Account is set in House Bank Account Connectivity, you can input a posting blocking date. You use posting block date to set a final date for marking financial postings to this bank account. After the specified posting block date, posting is no longer allowed for this bank account. This date allows you to add an additional check for financial postings and help you maintain correct data for Advanced Valuation in Financial Accounting. You set the posting block date when you change the bank account status to Closed at Bank. You can update the posting block date as needed before the bank account is set to the Close status.Refer to Approve Bank Account Request via Workflow step to activate the change request. | A bank account change request has been created. Follow the steps in Approve Bank Account Request via Workflow to activate this request. Once completed, the bank account status will be updated to Closed at Bank. | You can choose confirm closing at bank without bank account initial closing. If you bypassing the initial closing procedure and choose confirm closing at bank, the bank account status will be changed to Closed at Bank directly. Output correspondence will be triggered, an e-mail is sent out to the relevant person in charge automatically, If the email address is properly maintained. |
| 9 | Complete Closing | Choose Complete Closing. |  | The actual balance of the bank account will be checked. The checking logic is defined in step Basic Settings. You can go to step Basic Settings to configure the Balance Check for Closing Process field as following:Blank: Balance Check Method (Deprecated)With this option set, you use the deprecated balance check method controlled via the configuration activity Change Message Control for Bank Account Management.10: No validation and close immediately.You set this option if you don't want to perform any bank account balance check when bank accounts are closed.20: Validate against aggregated actuals for amount in bank account currency in One Exposure.With this option set, the system checks the aggregated actuals of a bank account in One Exposure before the account is closed.Users can view the aggregated actuals for your bank account in the Bank Account Balance Reconciliation with Drill Down (FCLM_BANK_RECONCIL) app. To do so, in this app, do the following:In the Account Dimension field, select Bank Account (House Bank/House Bank Account).Set the reconciliation date as your current local date.In the Data Source Selection field, select Acnt Bal in Cash Pos (Tran Dt).Run the report. The Acnt Bal in Cash Position (Tran. Dt) field to show the aggregated actuals for bank accounts.To adjust the aggregated actuals for your bank account to produce zero, users can create a memo record to offset the current amount. To do so, in the Manage Memo Records 2.0 (F2986A) app, create a memo record with the memo record category Actual Cash Memo. Please note that the value date of the memo record must not be later than the bank account closing date. After the bank account balance is adjusted to zero, the bank account will no longer be visible in the report above.30: Validate against ledger balance (from bank statement).With this option set, the system checks the ledger balance of a bank account in the Manage Bank Account Balances (F5175) app before the account is closed. Only bank accounts for which the ledger balance is zero or has never been updated before can be closed.When the balance check error is shown, users need to ensure the ledger balance reflects the real balance of the bank account. They can import the latest bank statement that confirms the ledger balance is zero, or enter a ledger balance for this bank account in the Manage Bank Statements (F1564) app.To use option 30: Validate against ledger balance (from bank statement), make sure that all of your bank accounts are not set with the transfer mode No Update for Cash Management for end-of-day bank statements as the method requires that balance data is saved for cash management. |
| 10 | Start to Confirm Closing at Bank | Choose Close in the Complete Closing dialog box.Refer to Approve Bank Account Request via Workflow step to activate the change request. | A bank account change request has been created. Follow the steps in Approve Bank Account Request via Workflow to activate this request. Once completed, the bank account status will be updated to Closed. |  |
| 11 | Return to Closed at Bank | Choose Return to Preceding Status.Refer to Approve Bank Account Request via Workflow step to activate the change request. | A bank account change request has been created. Follow the steps in Approve Bank Account Request via Workflow to activate this request. Once completed, the bank account status will be updated to Closed at Bank. |  |
| 12 | Return to Closing Request Sent to Bank | Choose Return to Preceding Status.Refer to Approve Bank Account Request via Workflow step to activate the change request. | A bank account change request has been created. Follow the steps in Approve Bank Account Request via Workflow to activate this request. Once completed, the bank account status will be updated to Closing Request Sent to Bank. |  |
| 13 | Return to Active | Choose Return to Preceding Status.Refer to Approve Bank Account Request via Workflow step to activate the change request. | A bank account change request has been created. Follow the steps in Approve Bank Account Request via Workflow to activate this request. Once completed, the bank account status will be updated to Active. |  |

###### Change Bank Account During Workflow (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Prerequisite

This function only applies to extensive system.

Purpose

The new bank account request is sent to the bank account worklist (inbox) for the Cash Manager. The Cash Manager can change the bank account before finally approve it.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori launchpad as a Cash Manager. |  |  |
| 2 | Access the SAP Fiori app | Open My Inbox - For Bank Accounts (F2797). | The Work Items for Bank Accounts displays. |  |
| 3 | Locate the open bank account Request | Choose a request for the change from the left pane. | The detailed information of bank account requests displays. |  |
| 4 | Edit the Request | Choose the link of bank account technical ID. | Navigate to revision detail page.Edit button is enabled. |  |
| 5 | Start to Edit | Choose Edit.Modify fields to your requirements.Choose Submit for Approval | The revision detail page is updated and waiting for approval. |  |

##### Maintain Payment Approver in Multiple Bank Accounts (Workflow Revision Activate)

Prerequisites

Approval patterns and and payment approve group have to be defined and assigned to company code before you start following procedures. Make sure you have finished the prerequisite step of Payment Approval Customizing before you start to maintain payment approver. SAP has predelivered the sequential pattern P001 with payment approver group G001 and G002, and the nonsequential pattern s001 with payment approver group SG01 and SG02 as Demo data in Start system.

Purpose

This step describes how to maintain Payment Approver in multiple bank accounts with Full Cash Management and Workflow Revision Activate.

SAP supports sequential and nonsequential signatories for payment approval.

This step describes how to maintain Payment Approver in multiple bank accounts with Full Cash Management and Workflow Revision Activate.

|  |
| --- |
| Note SAP supports sequential and nonsequential signatories for payment approval.Sequential Payment Approver: The payment approval should obey the approver sequence. For example, if the Accounts Payable Manager is set as the first approver, the Cash Manager is set as the second approver. The Cash Manager cannot approve the payment before the Accounts Payable Manager in sequential Payment Approver case.Nonsequential Payment Approver: No sequence exists for the approvers. The Payment Approver Group field decides the Payment Approver case you can choose. |

|  |
| --- |
| Caution The following procedure assumes that you are only maintaining Payment Approver for multiple accounts with Full Cash Procedures Management Using Workflow Revision Activate procedure. If you are implementing and testing additional Full Cash Management options, especially in a single environment, you cannot use the same Master Data values for more than one procedure type. You must create additional Master Data values, for example G/L Accounts, and then use these different values in each procedure type. |

|  |
| --- |
| Note If you maintained the Payment Approver for multiple bank accounts, corresponding requests are grouped to sent to the approval user. To set the requests grouping rule:Depending on your configuration environment for SAP S/4HANA Cloud Public Edition, choose one of the following options:Configure Your Solution:Log on as a Configuration Expert - Business Process Configuration.Open Manage Your Solution (F1241).Choose Configure Your Solution.Search for the Define Basic Settings (SSCUI ID 101025) SSCUI. Once you find it, choose Configure.Review the Request Grouping field value per the following table:Request Grouping Field ValueExplanationGroup into a Single Change RequestAll bank account change requests you did in one multiple change are grouped together to be sent to the corresponding approval user.Group by Company CodeThe bank account change requests you did in one multiple change are grouped by the company code and sent to the corresponding approval user.Group by Account TypeThe bank account change requests you did in one multiple change are grouped by the Account Type and sent to the corresponding approval userGroup by Company Code and Account TypeThe bank account change requests you did in one multiple change are grouped by the Company Code and Account Type and sent to the corresponding approval user.SAP Central Business Configuration:Log on to the project experience in SAP Central Business Configuration.Go to the Business Processes Configuration app. You can search forDefine Basic Settings and navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori Launchpad as a Configuration Expert - Business Process Configuration (SAP_BR_BPC_EXPERT).Review the Request Grouping field value per the following table:Request Grouping Field ValueExplanationGroup into a Single Change RequestAll bank account change requests you did in one multiple change are grouped together to be sent to the corresponding approval user.Group by Company CodeThe bank account change requests you did in one multiple change are grouped by the company code and sent to the corresponding approval user.Group by Account TypeThe bank account change requests you did in one multiple change are grouped by the Account Type and sent to the corresponding approval userGroup by Company Code and Account TypeThe bank account change requests you did in one multiple change are grouped by the Company Code and Account Type and sent to the corresponding approval user. |

###### Add Payment Approver for Multiple Accounts

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The Bank Accountant (Cash Management Specialist) triggers to maintain Payment Approver for multiple bank accounts collectively, instead of individually. And one individual approve and confirm process is required for change Payment Approver requests to one Payment Approver group.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log onto the SAP Fiori launchpad as a Cash Management Specialist. | The SAP Fiori launchpad displays. |  |
| 2 | Open SAP Fiori App | Open Maintain Payment Approver (WDA_FCLM_BAM_ADAPT_SIGN (APP_CFG_FCLM_BAM_ADAPT_SIGN)). | The Maintain Payment Approver- For Multiple Bank Accounts screen displays. |  |
| 3 | Select Company Code | Select company code in the filter header.Company Code: For example, 3310 and then choose Go to filter the results list. | Results List. |  |
| 4 | Select Bank Accounts | Select Bank Accounts rows in Results List. Multiple bank accounts of the company code display.For example, bank account 0000000693123456 Multiple bank accounts of the company code display in the of bank key 18121976and bank account 0000000693123456 of bank key 18121986.Choose Add Payment Approver.Caution Only the entry of bank accounts in which the field Editable Account is ticked can be maintained. | Add Payment Approver screen displays. |  |
| 5 | Add Payment Approver to Payment Approver Group G001 | On the Add Payment Approver screen, make the following entries:New Payment Approver: For example, <the user ID (CB*)has business role Accounts Payable Manager assigned>Valid From: For example, <current date>.Valid To: For example, 31.12.9999Payment Approver Group: G001Note Payment Approver group G001 is used for sequential Payment Approver. To use nonsequential Payment Approver, use SG01.Max. Amount for Payment: For example, 100,000.000Max. Amount for Batch: For example, 1,000,000.000Note The check box of Unlimited Approval is used for grant the authorization of approving unlimited amount. When you select this check box, the value of Maximum Amount for Payment and Maximum Amount for Batch will be invalid, the Payment Approver can approve an unlimited amount.Currency: AEDChoose OK. | Change Payment Approver request to Payment Approver Group G001 has been created. |  |
| 6 | Add Payment Approver to Payment Approver Group G002 | Once Change Payment Approver request to Payment Approver Group G001 has been approved by the Accounts Payable Manager as described in the Approve Payment Approver Maintenance Change Request procedure and confirmed by the Cash Manager in the Approve Payment Approver Maintenance Change procedure, repeat steps 2-4.On the Add Payment Approver screen, make the following entries:New Approver: For example, <the user ID (CB*) of business user Cash Manager has business role Cash Manager assigned>Valid From: For example, <current date>Valid To: For example, 31.12.9999Payment Approver Group: For example, G002Note Payment Approver group G002 is used for sequential Payment Approver. To use nonsequential Payment Approver, use SG02.Max. Amount for Payment: For example, 100,000.000Max. Amount for Batch: For example, 1,000,000.000Currency: AEDChoose OK. | Change Payment Approver request to Payment Approver Group G002 has been created. |  |

###### Change Payment Approver in Multiple Bank Accounts

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you as Bank Accountant (Cash Management Specialist) can make mass maintenance of Payment Approver for multiple bank accounts.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Cash Management Specialist. |  |  |
| 2 | Open SAP Fiori App | Open Maintain Payment Approver (WDA_FCLM_BAM_ADAPT_SIGN (APP_CFG_FCLM_BAM_ADAPT_SIGN)). | The Maintain Payment Approver - For Multiple Bank Accounts screen is displayed. |  |
| 3 | Select Company Code | Select company code in the filter header:Company Code: For example, 3310, and then choose Go to filter the results list. | Multiple bank accounts of the company code are displayed in the Results List. |  |
| 4 | Select Bank Accounts | Select Bank Accounts rows in Results List:For example, bank account 0000000693123456 of bank key 18121976and bank account 0000000693123456 of bank key 18121986.Choose Change Payment Approver. | Change Payment Approver screen is displayed. |  |
| 5 | Change Payment Approver | On the Change Payment Approver screen, make the following entries:New Payment Approver: For example, <the user ID (CB*) has business role Cash Manager Specialist assigned>Valid From: For example, current date.Valid To: For example, 31.12.9999(New Payment Approver Section)Note Keep the Valid To date in Old Payment Approver section as current date.Choose OK. | The Payment Approver is changed for the bank account. |  |

##### Upload Attachments for Bank Account

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

You can upload attachments for the bank account.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Cash Management Specialist. |  |  |
| 2 | Access the SAP Fiori App | Open Manage Bank Accounts (F1366A). | The Manage Bank Accounts view displays. |  |
| 3 | Binding Cash Pools as Leading Account | Make the following entries and choose Go:Account Number: An active account. For example, 1133698 | Note If the basic setting is Direct Revision Activate, the bank account is activated. |  |
| 4 | Bank Account View | In the data table, choose the arrow icon at the right of the row for the account. | The Bank Account view displays. |  |
| 5 | Edit | Choose Edit. |  |  |
| 6 | Upload Attachments | Navigate to Attachments tabSelect Doc.Type to Upload: AttachmentsChoose Upload.Select a document to upload.Choose Submit for Activation. |  |  |

##### Cancel Bank Accounts Requests

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

If the signatory of accounts have been created, edited or changed, in this activity, the requests creator can cancel the requests before approval.

Prerequisite

Ensure the basic setting is the Activate Via Workflow mode before using this functionality.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Cash Management Specialist. |  |  |
| 2 | Access the SAP Fiori app | Open My Sent Requests - For Bank Accounts (F1371A). | The My Sent Requests (Version 2) view displays. |  |
| 3 | Select Request | Select the check box of the request to cancel. |  |  |
| 4 | Cancel Request | Choose Cancel Requests and them choose Close. | Change request was canceled. |  |

##### Approve Bank Account Request via Workflow

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

If changes are made in previous steps, the change request wil be send to the Cash Manager’s inbox (My Inbox). This activity guides Cash Manager to approve or reject the request.

Prerequisite

Assign the logon user to the correct rule for corresponding actions from the previous Manage Workflows procedure.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Cash Manager .If you completed the Manage Workflows preliminary steps, log on to the SAP Fiori launchpad as a Business Partner you maintained in Responsibility Management (1NJ) test script.You can only choose one of these two approaches as the prerequisite, due to their incompatibility in some way for the bank account management workflow process. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open My Inbox - For Bank Accounts (F2797).Note You can also access to this app by clicking the notification on the upright of the screen, please make sure the role SAP_BR_MANAGER is assigned to the user if you want to access the approval page from this method. | The worklist displays. |  |
| 3 | Check Requests for Approval | Choose Requests for Approval. | The list of bank account requests for approval displays. |  |
| 5 | Approve the Request | Choose Approve. | The Submit Decision screen displays. |  |
| 6 | Enter and Approve | In the dialog box, enter a note and choose Submit. | The closing request is approved.An Email is sent out to the relevant person in charge automatically if the sender’s Email address has been correctly maintained in Define Output Parameter Determination step (please refer to Test Script J77 > Prerequisite > Define Output Parameter Determination ). Find bank account 8765432188 in the Manage Bank Account app. Click this account to it’s master data page. An log entry is created in the Bank Correspondence tab.The Email address maintained in Output Parameter Determination takes the first priority as the sender if it is valid. Please refer to Preliminary Steps > Define Output Parameter Determination in test script J77.If the email address is invalid in Output Parameter Determination, Sender’s email address will be defaulted as company code’s email address.The receiver is the Bank Contact Person. If Bank Contact Person is not maintained, the receiver is Bank Relationship Manager. If Bank Relationship Manager is not maintained, the receiver is the Email address maintained in the Bank. |  |

##### Create Bank Account with Bank Correspondence

Purpose

This step describes how to create a In-House Bank Account by bank accountant (Cash Management Specialist).

Prerequisite

1. Create a company code, a bank key as in-house bank center and extend a business partner as IHB account holder. Please refer to step Manage Banks and House Banks, Extend Business Partners as IHB Account Holder and Inhouse Bank Area Owner in In-House Banking ([6BP](https://me.sap.com/processnavigator/SolP/O60)) test script for detail.
2. Perform step Enable Bank Account Contract Type.
3. Perform step Configure Origination Process and Manual Creation to enable the Origiantion process, and enter the following data:

Contract Type: <Current Account>

Company Code: 3340

Enable Origination Process: <Select>

Disable Manual Creation: <Deselect>

1. Perform step Configure Status and Bank Account Control Modes to configure process to next status, and enter the following data:

Contract Type: In-House Bank

Status: 28 Opened at Bank

Enable Status: <Select>

Control Mode to Next Status: Direct Change

Control Mode to Preceding Status: Direct Change

### Create In-House Bank Account via eBAM

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This step describes how to create a In-House Bank Account via eBAM by a bank accountant (Cash Management Specialist).

Prerequisites

1. Go to the Define Basic Settings step to select the Enable Bank Account Contract Types checkbox in Configuration Activity 101025 Define Basic Settings.
2. Go to the Configure Origination Process and Manual Creation step to create an entry with parameter Contract Type as 06 In-House Bank Account, CoCd as blank and select the Enable Origination Process checkbox.
3. Scope item In-House Banking ([6BP](https://me.sap.com/processnavigator/SolP/O60)) should be implemented and complete the Manage Banks and House Banks step in In-House Banking ([6BP](https://me.sap.com/processnavigator/SolP/O60)) test script.
4. Assign both Payment Specialist - In-House Banking role and Cash Management Specialist role to your user.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Cash Management Specialist. |  |  |
| 2 | Access the SAP Fiori App | Open Manage Bank Accounts (F1366A). |  |  |
| 3 | Create Bank Account | Choose Create.Enter the following data and choose Continue.Company Code: 3340Account Type: 88Note Please go to step Define Account Type and Contract Type to configure the Contract Type to 06 for the Account Type 88. | The Bank Account screen displays. |  |
| 4 | Enter Header Data | Enter the following data:Account Number: 104001Account Description: IHB Account for eBAMBank Country/Region: AEBank Key: #600310101Account Currency: AEDIn-House Bank Servicer: 33403310 |  |  |
| 5 | Enter General Data | Enter the following data:Opening Date: for example, <current date>Account Holder: Company Code IHB 3340 (company code name is uasually defaulted by system)Bank Control Key: for example, PNote Bank Control Key is only used in some countries like France, Spain, Italy. If you don't use Bank Control Key, you should leave this field blank.IBAN: <Generate IBAN>Note Only perform this step if your country is using IBAN. If not, just skip this step. |  |  |
| 6 | Bank Relationship Data | Payment Transaction Type Group: C053IHBNote The field Transaction Type is not available for on premise. To assign the Transaction Type to your Bank Account use the IMG Menu Path: Financial Accounting > Bank Accounting > Business Transactions > Payment Transactions > Electronic Bank Statement > Make Global Settings for Electronic Bank StatementsNote If you are going to upload camt.054 format bank statement for supplier financing, which is described in test script 1EG, the field Pmnt Tran Type Group has to be maintained as camt053, otherwise camt054 bank statement can't be uploaded. |  |  |
| 7 | Maintain Internal Contact Persons | In the Bank Relationship pane, in the Internal Contact Persons area, enter the following data:Internal Bank Account Contact: <ID assigned to the Cash Management Specialist role>Bank Account Supervisor: ID assigned to the Cash Manager role |  |  |
| 8 | Choose Bank Relationship Tab | In the Bank Relationship pane, in the Bank Statement Data area, enter the following data:Processing Status: <selected>Interval: for example, 01Interval Unit: for example, MonthsFactory Calendar ID: for example, 01Note The Processing Status field indicates whether to monitor this bank account at the end of the day in the Bank Statement Monitor. You can specify the import frequency with the Interval and Interval Unit fields. The Factory Calendar ID field distinguishes between working days and non-working days. |  |  |
| 9 | Choose House Bank Account Connectivity | Choose House Bank Account Connectivity. |  |  |
| 10 | Enter House Bank Account Connectivity | Choose Create. Enter the following data:ID Category: for example, Central System: House Bank AccountNote If the house bank account only exists in the local system, you can specify the ID Category as Central System: House Bank Account; If the house bank account exists in remote system, and need to be migrated to local system, you can specify the ID Category to Remote System: House Bank Account.Remote System: <Leave blank>Company Code: 3340House Bank: AEBK4Note If the bank account does not exist, please refer to Manage Banks and House Banks step in In-House Banking ([6BP](https://me.sap.com/processnavigator/SolP/O60)) test script to create one.House Bank Acct ID: AEAC4G/L Account: 11001000Choose Apply.Choose Save. | Account status is equal to Pre-Opening Preparation. |  |
| 11 | Start Opening | Choose Start Opening. | Status change to In Opening Process. |  |
| 12 | Create Correspondence Container | Choose Edit.Choose tab Bank Correspondence.Choose Create.Enter the following data and choose Save.Correspondence Type: <Select a bank correspondence type that is configured in SSCUI 106791: Define Bank Correspondence Types>NoteGo to configuration activity 106793 Define Number Ranges for Bank Correspondence Folders and configuration activity 106794 Define Number Ranges for Bank Correspondence Objects to configure the number range setting if number range hasn't been configured yet.Go to configuration activity 106792 Define Authorization Groups for Bank Correspondence to create a Bank Correspondence Authorization Group.Go to configuration activity 106791 Define Bank Correspondence Types to create the Bank Correspondence Types.Folder Description: Account OpeningChoose Save. |  | By default, you can bypass this step, as Bank Correspondence folder will be automatically created for In-House Bank Account with status 26 In Opening Process, you can go to SSCUI 106884 Define Basic Accounts for Automatic Creation of Correspondence Folder to adjust the automation settings. |
| 13 | Send Account Opening Request | Select the Correspondence Container you previously created.Choose Send Account Opening Request.Note If error message pop up that customer number hasn't been maintained, please go to the Manage Banks Cash Management Data step to fill a customer number in object page of the House Bank tab. | Correspondence status is changed from created to in communication eBAM message is collected automatically. | This step can also be bypassed, as Bank Correspondence folder will be automatically created for In-House Bank Account with status 26 In Opening Process, you can go to SSCUI 106884 Define Basic Accounts for Automatic Creation of Correspondence Folder to adjust the automation settings. |
| 14 | Check Correspondence Container | Choose the triangle button on the right to go into the detail of the correspondence folder.Check if the Outbound Message ACMT.007.001.04 (Account Opening Request) has been created.If In-House Bank account has been created in bank side, an Account Request Acknowledgement message with message type ACMT.010.001.03, and an Account Report message with message type ACMT.014.001.04 will be routed via MBC into Bank Relationship Management. |  |  |
| 15 | Update Account with Respondence | In the Correspondence Container Object screen, choose Update Account with Response.Compare the Request and Response.Choose Update.Choose Finalize.Enter a date on the pop up dialog and choose Finalize. |  |  |
| 16 | Confirm Opening at Bank | Go back to the bank account screen.Choose Confirm Opening at Bank. |  |  |
| 17 | Save Bank Account | Choose Save and follow the control mode you configured in step Configure Status and Bank Account Control Modes to activate the bank account. |  |  |

### Powers of Attorney

Purpose

Powers of attorney represent the legal Powers of attorney that a company has granted to one or more persons to carry out banking transactions on behalf of the company. This section described the steps of processing a Powers of Attorney.

#### Manage Payment Approval Rules

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you can manage payment approval rules. Using the payment approval rule, you define how authorized representatives are allowed to approve payments. This is achieved by defining payment approval rules as an approval pattern for approver groups. In detail, you define in the payment approval rule how many people (1 or 2) from which approver groups can approve which payment amount. To use the payment approval rules, you must then assign a payment approval rule in the [Manage Powers of Attorney for Banking Transactions](https://help.sap.com/docs/SAP_S4HANA_CLOUD/186460fdc35a4b64a713da9bb00deb1e/ca1969a9c4884842a2499141767f9bbc.html?state=DRAFT) app and assign an approver group to each authorized representative.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori launchpad as a Cash Management Specialist. |  |  |
| 2 | Access the SAP Fiori app | Open Manage Payment Approval Rules (F6959). |  |  |
| 3 | Create Payment Approval Rules | Choose Create.Make the following entries:Rule ID: ZR01Default Limit Currency: EURChoose Create. | Payment Rule Object Page Opening |  |
| 4 | Enter Header Data | Make the following entries:Rule Description: Payment Approval Rule for POA Testing |  |  |
| 5 | Create Approval Rule Details | Choose Create.Enter the following entry:Approval Rule Item: ZRI01Choose Create. | The approval rule item object page opening |  |
| 6 | Header Data for Rule Item | Enter the following entries:Approval Category: Two Persons TogetherDefault Limit Amount: 1000000 EUR |  |  |
| 7 | Payment Approval Groups | Enter the following entries:Approval Group: AApproval Group: B |  |  |
| 8 | Limits | Choose CreateMake the following entry:Limit Currency: USDNote The limit Currency should be different frome the Defalt Limit Currency.Choose Continue.Limit Amount: 500000 USDChoose Apply.Choose Create. | Payment Approval Rule Created. |  |
| 9 | Submit for Approval | Choose Submit. |  |  |
| 10 | Approve the Rule | Log on to the SAP Fiori launchpad as a Cash Manager . Open Manage Payment Approval Rules (F6959).Go into the detail of Rule ZR01.Choose Approve. | Payment Approval Rule Approved. |  |

#### Create Powers of Attorney

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you can represent and manage the Powers of attorney for banking transactions for your company codes. A Powers of attorney for banking transactions represents the legal Powers of attorney that a company has granted to one or more persons to carry out banking transactions on behalf of the company. In the Powers of attorney, you assign the principals, the authorized representatives, the payment approval rule, the bank accounts, and the permitted activities.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori launchpad as a Cash Management Specialist. |  |  |
| 2 | Access the SAP Fiori app | Open Manage Powers of Attorney for Banking Transactions (F5742). |  |  |
| 3 | Create Powers of Attorney | Choose Create. | The Powers of Attorney for Banking Transactions displays. |  |
| 4 | Enter Header Data | Make the following entries:Powers of Attorney ID: Z_POA_01POA Description: Powers of Attorney for TestingAuthorization Group: Z_TSPOA Type: SGBMValid From: Current DateValid To: At the end of this MonthBA Assignment Type: Via Selections, Existing and Future Bank AccountsPayment Approval Rule: ZR01 |  |  |
| 5 | Add Principals | Choose Add.Enter the following entry:Company Code: 3310 |  |  |
| 6 | Add Bank Accounts | Choose Add.Enter the following entries:Selection Field: CurrencySelect Option: Equal toValue: AED |  |  |
| 7 | Assign Bank Accounts | Choose Retrieve Bank Accounts button on the upright of the screen. | Bank Accounts meet the selection criteria are listed. |  |
| 8 | Add Authorization Representatives Details | Choose Add.Make the following entry:Business Partner: Select a Business PartnerApprover Group: ABusiness Partner: Select another Business PartnerApprover Group: BNote You can only add Business Partner that have the Business Partner Role Authorized Representative (TR1000) assigned to them. If you try to enter invalid Business Partner you will get an error message when clicking Save.To create Business Partner, please refer to test script [BFA](https://me.sap.com/processnavigator/SolP/BFA) preliminary step Create Bank Business Partner. |  |  |
| 9 | Add Activity | Choose Add.Make the following entry:Activity: SPAYChoose Create. | The Powers of attorney is created. |  |
| 10 | Add Predecessor | Choose Add, and make the following entry:Predecessor ID: Choose an Active Powers of Attorney IDNote You can only assign predecessors with the same POA type or predecessors had no POA type at all. If there is no Predecess or POA ID from the search help, you can skip this step.Choose Create. |  |  |
| 11 | Upload Attachment | Choose Edit.Select Doc.Type to Upload: POA AttachmentsChoose: UploadSelect a document to upload.Choose Save. |  |  |
| 12 | Submit for Approval | Choose Submit.Note You can choose the withdraw button on the up-right of the screen, if you want to withdraw your application. | Powers of attorney is submitted for approval. |  |

#### Approve Powers of Attorney

In this step, you can approve powers of attorney via Dual Control or Workflow. You can go to SSCUI 101025: Define Basic Setitngs to configure the field Power of Attorney Approval Mode to control its approving mode.

##### Approve Powers of Attorney via Dual Control

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The Powers of Attorney request is sent to the Cash Manager who can approve or reject the request.

Prerequisite

Go to SSCUI 101025: Define Basic Setitngs to configure the field Power of Attorney Approval Mode as Dual Control.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log onto the SAP Fiori launchpad as a Cash Manager. |  |  |
| 2 | Access the SAP Fiori app | Open Manage Powers of Attorney for Banking Transactions (F5742). |  |  |
| 3 | Select Powers of Attorney | Enter Powers of Attorney Name you created in the last step in the search bar.Choose the triangle button of the Powers of Attorney.Choose Approve. | The Powers of Attorney for Banking Transactions displays. |  |
| 4 | Approve Powers of Attorney | Choose Approve. | The Powers of attorney is approved. |  |

##### Approve Powers of Attorney via Workflow

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

If you created a new powers of attorney, the request will be sent to the Cash Manager’s inbox (My Inbox). This activity guides Cash Manager to approve or reject the request.

Prerequisite

Preliminary step Manage Workflows for Powers of Attorney and Email Notification should be performed, and go to SSCUI 101025 Define Basic Setting to configure the field Power of Attorney Approval Mode as Workflow.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Cash Manager .If you completed the Manage Workflows preliminary steps, log on to the SAP Fiori launchpad as a Business Partner you maintained in Responsibility Management (1NJ) test script.You can only choose one of these two approaches as the prerequisite, due to their incompatibility in some way for the bank account management workflow process. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open My Inbox - All Items (F0862). | The worklist displays. |  |
| 3 | Check Requests for Approval | Choose Requests for Approval. |  |  |
| 4 | Approve the Request | Choose Approve. | The Submit Decision screen displays. |  |
| 5 | Enter and Approve | In the dialog box, enter a note and choose Submit.Note Please go to the Workflow tab to check if additional workflow steps exist. If yes, you can log on with the additional workflow step approver user, and repeat the test step 1-6 to approve the additional workflow steps. |  |  |

##### Approve Powers of Attorney with Basic Bank Account Management User (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

If you have already implemented advanced bank account management for certain users and now wish to approve the powers of attorney via workflow for other users who only have basic bank account management privileges, this step outlines the operational procedure.

Prerequisite

Preliminary step manage workflows for powers of attorney should be performed and you need to go to Configuration Activity 101025 Define Basic Setitngs to configure the field Power of Attorney Approval Mode as Workflow.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as Administrator. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Maintain Business Roles (F1492).Choose New.Make the following entries:Role Type: Business UserBusiness Role ID: POA_BASIC_BAMBusiness Role Description: Business Role for POA Basic BAMChoose Create.Go to the Business Catalogs tab, choose Add.Search for the Business Catalog: SAP_FIN_BC_CM_POA_APPROVE_PCSelect the check box and choose OK.Choose OK.Choose Save. |  |  |
| 3 | Assign Business Role to User | Open Maintain Business Users (F1303).In the filter, search for your business user and Choose Go.Go into the details of the business user.Go to the assigned business roles tab.Choose Add.In the filter, enter the Business Role ID: POA_BASIC_BAM.Select the check box and choose OK.On the Assigned Business Roles tab, choose Add again.In the filter, enter the Business Role ID: SAP_BR_EMPLOYEE.Select the check box and choose OK.Choose Create. |  |  |
| 4 | Add User to Team Member | Go to step [Manage Workflow for Powers of Attorney and Email Notification](#unique_14) [page ] 22 to add the newly created user as team member for team type SFCLM_POA. |  |  |
| 5 | Create Powers of Attorney | Go to step [Create Powers of Attorney](#unique_129) [page ] 233 to create and submit a new Power of Attorney. |  |  |
| 6 | Approve Powers of Attorney | Log on with the user with the role POA_BASIC_BAM and SAP_BR_EMPLOYEE. |  |  |
| 7 | Approve the Powers of Attorney | Open My Inbox - All Items (F0862).You can approve or reject the workitem. |  |  |

#### Create PDF for Powers of Attorney

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you can create PDF as attachment for the Powers of Attorney with the customized form template.

Prerequisites

Perform the step [Assign Form Templates to Powers of Attorney Types](#unique_28) [page ] 45. The PDF created in this step is based on the content form

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log onto the SAP Fiori launchpad as a Cash Management Specialist. |  |  |
| 2 | Access the SAP Fiori app | Open Manage Powers of Attorney for Banking Transactions (F5742). |  |  |
| 3 | Select Powers of Attorney | Enter the Powers of Attorney Name you created in the previous step in the search bar.Choose the triangle button of the Powers of Attorney. |  |  |
| 4 | Edit Powers of Attorney | Choose Edit. |  |  |
| 5 | Create PDF | Choose Create PDF. |  |  |

#### Revoke Powers of Attorney

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

If the Powers of Attorney no longer used, you can revoke it through below steps.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log onto the SAP Fiori launchpad as a Cash Management Specialist. |  |  |
| 2 | Access the SAP Fiori app | Open Manage Powers of Attorney for Banking Transactions (F5742). |  |  |
| 3 | Select Powers of Attorney | Enter Powers of Attorney Name you created in the last step in the search bar.Choose the triangle button of the Powers of Attorney.Choose Approve. | The Powers of Attorney for Banking Transactions displays. |  |
| 4 | Revoke Powers of Attorney | Choose Revoke. | The Powers of attorney is revoked. |  |

#### Implement Powers of Attorney

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you can monitor the implementation process of powers of attorney for the different channels. To do this, you create exactly one implementation for a powers of attorney for banking transactions. Within the implementation, you assign the channels for which you want to implement the powers of attorney. For each channel, you create correspondence objects representing the correspondence that you have sent to or received from your banks.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori launchpad as a Cash Management Specialist. |  |  |
| 2 | Access the SAP Fiori App | Open Implement Powers of Attorney for Banking Transactions (F6374). |  |  |
| 3 | Create Powers of Attorney Implementation | Choose Create. |  |  |
| 4 | Enter Header Data | Make the following entries:Implementation ID: Z_IMPOA_01Description: Implement Powers of Attorney for Testing |  |  |
| 5 | Add Powers of Attorney | Choose Add.Make the following entry and press Enter:Powers of Attorney ID: Z_POA_01 |  |  |
| 6 | Add Channels | Choose Add.Make the following entry and press Enter:Channel ID: Online Banking (Administrated by Bank)(SOBB) |  |  |
| 7 | Create Outgoing Correspondence | Choose Create Outgoing Correspondence.Enter the following entries:Correspondence Object ID: ZOUT01Correspondence Object Description: Outgoing CorrespondenceSent On: <Current Date> |  |  |
| 8 | Remove a Bank | Go to Banks tab.Select the check box of one bank and choose Remove.Choose Apply.Choose Create. |  |  |
| 9 | Set to Sent for Outgoing Correspondence | Go into the detail of the Channel.Select the checkbox of Correspondence Object ZOUT01.Choose Set to Sent.Choose OK. |  |  |
| 10 | Create Incoming Correspondence Object | Choose Edit.Choose Create Incoming on Correspondence Object ID ZOUT01 item.Make the following entries:Correspondence Object ID: ZIN01Correspondence Object Description: Incoming CorrespondenceConfirmation Date: Current DateChoose Apply.Select the check box of outgoing correspondence object.Choose Apply.Choose Apply.Choose Create. |  |  |
| 11 | Revoke Outgoing Correspondence (Optional) | Go into the detail of the Implementation Z_IMPOA_01.Choose EditGo into the detail of the Channel.Choose Create Outgoing Correspondence.Enter the following entries:Correspondence Object ID: ZOUT02Correspondence Object Description: Second Outgoing CorrespondenceSent On: <Current Date>Select the check box of RevokationGo to the Replaced Outgoing Correspondence Objects tab.Choose Add.Input the Correspondence ID you want to revoked. For example ZOUT01.Choose Apply. |  |  |
| 12 | Create Incoming Correspondence Object | Choose Edit.Choose Create Incoming on Correspondence Object ID ZOUT02 item.Make the following entries:Correspondence Object ID: ZIN02Correspondence Object Description: Incoming CorrespondenceConfirmation Date: Current DateChoose Apply.Select the check box of outgoing correspondence object.Choose Apply.Choose Apply.Choose Save. |  |  |
| 13 | Submit for Approval | Choose Submit.Note You can choose the withdraw button on the up-right of the screen, if you want to withdraw your application. | Powers of attorney is submitted for approval. |  |

#### Compare Powers of Attorney

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you can compare the powers of attorney with its predecessor and others.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori launchpad as a Cash Management Specialist. |  |  |
| 2 | Access the SAP Fiori app | Open Manage Powers of Attorney for Banking Transactions (F5742). |  |  |
| 3 | Select Powers of Attorney | Enter Powers of Attorney Name you created in the last step in the search bar.Choose the triangle button of the Powers of Attorney. |  |  |
| 4 | Compare with Predicessor | Choose Compare with Predecessor.Note If the predecessor Powers of Attorney is not assigned, button Compare with Predecessor won’t appear. You can skip this step and go to step Comapare with Other. | You should see the comparison page containing the header data in basic info section and the child entity in the remaining section. The default page hided the identical items. You can choose the Show Identical Items button to display the uncanged items and choose Hide Identical Items to hide them. |  |
| 5 | Compare with Other POA | Choose Compare with Other POA. | You should see the comparison page containing the header data in basic info section and the child entity in the remaining section. The default page hided the identical items. You can choose the Show Identical Items button to display the uncanged items and choose Hide Identical Items to hide them. |  |

#### Start Data Collection

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you can collect the data of powers of attorney.

Prerequiste

Preliminary Steps Profile Creation for Powers of Attorney and Define Purpose for Powers of Attorney should be performed.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log onto the SAP Fiori launchpad as a DATA_PRIVACY_SPECIALIST. |  |  |
| 2 | Access the SAP Fiori app | Open Start Data Collection (DTINF_START_COLL). |  |  |
| 3 | Fetching Purpose | Choose Refresh Purposes.Choose Continue. | Information message “Fetching Purpose. This may take a while!” displays.Purpose relevant for your ILM Object should appear in the F4 help of the Purpose field. |  |
| 4 | Start Collection | Make the following entries:Data Subject ID Type: Business PartnerData Subject ID: The business partner ID assigned in Powers of Attorney.Language: for example, EnglishPurpose: for example, Z_POA_PURPOSEChoose Execute. | Data collection triggered successfully. |  |

#### Process Data Collection

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you can process the collected data of powers of attorney.

Prerequiste

Preliminary Steps Profile Creation for Powers of Attorney and Define Purpose for Powers of Attorney should be performed.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log onto the SAP Fiori launchpad as a DATA_PRIVACY_SPECIALIST. |  |  |
| 2 | Access the SAP Fiori app | Open Process Data Collection Results (DTINF_PROC_COLL). | A list of all data collection requests is displayed. |  |
| 3 | Check Data Collection | Double-click the data collection performed in the previous step.Make the following entry:Purpose: Select Purpose for POAChoose Go. | If the collection has completed the status should be green.The results are displayed hierarchically on the left-hand side of the sub-screen. |  |

#### Destruct and Block Powers of Attorney

##### Destruct Powers of Attorney

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

You can destruct POAs that are in the status Obsolete and for which the Residence Period has passed, the related POAIs and Correspondence Objects will also be destructed.

Prerequisite

Before you start the following steps, please follow the Information Lifecycle Management ([1KA](https://me.sap.com/processnavigator/SolP/O60)) test script to maintain the Audit Area as Demo in Maintain Audit Area step. Input the parameter Policy Category as Retention Rules, Audit Area as Demo, assign ILM Object FCLM_POA to Audit Area Demo and set the status to Active in the Assign ILM Object to Audit Area step. Input the parameter Policy Category as Retention Rules, Audit Area as Demo, ILM Object as FCLM_POA in configuration activity 106666 Maintain ILM Policies and Rules, and follow the Maintain ILM Policies and Rules step of Information Lifecycle Management ([1KA](https://me.sap.com/processnavigator/SolP/O60)) to create Policies and Rules.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Data Privacy Specialist. |  |  |
| 2 | Access the SAP Fiori App | Note Before you start the following steps, please follow the Maintain ILM Policies and Rules step described in Information Lifecycle Management ([1KA](https://me.sap.com/processnavigator/SolP/O60)) test script to check if the Live status policy in Policy Category is Retention Period, ILM Area is DEMO, and ILM Object is FCLM_POA.Open ILM Data Destruction (F2662). |  |  |
| 3 | Search Destruction Object | Select the Data Destruction Object and choose Not Scheduled category.Search for the destruction object FCLM_POA_DESTRUCTION. | The destruction objects that are currently not scheduled for a destruction run are listed. | Depending on the frequency maintained in the Cloud System, it takes several days or one week until a run is executed. |
| 4 | Schedule Destruction | Select the checkbox of object FCLM_POA_DESTRUCTION.Choose Schedule.On the pop up, choose Delete. | POAs that are in the status Obsolete and for which the Retention Period has passed, the related POAIs and Correspondence Objects will also be deleted. |  |

##### Block Powers of Attorney

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

POAs that are in the status Obsolete and for which the Residence Period has passed should be marked as blocked and only be accessible via a dedicated audit user.

Also related POAIs and Correspondence Objects that are related to a blocked POA will be logically blocked.

Prerequisite

Before you start the following steps, please follow the Information Lifecycle Management ([1KA](https://me.sap.com/processnavigator/SolP/O60)) test script to check if Blocking exists in Audit Area of the Maintain Audit Area step. In case that Blocking does not exist, you can create one with Y or Z customer namespace. Assign ILM Object FCLM_POA to Audit Area Blocking and set the status to Active in the Assign ILM Object to Audit Area step. Input the parameter Policy Category as Residence Rules, Audit Area as Blocking, ILM Object as FCLM_POA in comfiguration activity 106666 Maintain ILM Policies and Rules and follow the Maintain ILM Policies and Rules step of Information Lifecycle Management ([1KA](https://me.sap.com/processnavigator/SolP/O60)) to create Policies and Rules.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Data Privacy Specialist. |  |  |
| 2 | Access the SAP Fiori App | Note Before you start the following steps, please follow the Maintain ILM Policies and Rules step described in Information Lifecycle Management ([1KA](https://me.sap.com/processnavigator/SolP/O60)) test script to check if the Live status policy in Policy Category is Residence Rules, ILM Area is Blocking, and ILM Object is FCLM_POA.Open ILM Data Destruction (F2662). |  |  |
| 3 | Search Destruction Object | Select the Data Destruction Object and choose Not Scheduled category.Search for the destruction object FCLM_POA_DESTRUCTION. | The destruction objects that are currently not scheduled for a destruction run are listed. | Depending on the frequency maintained in the Cloud System, it takes several days or one week until a run is executed. |
| 4 | Schedule Destruction | Select the checkbox of object FCLM_POA_DESTRUCTION.Choose Schedule.On the pop up, choose Delete. | POAs that are in the status Obsolete and for which the Residence Period has passed, the related POAIs and Correspondence Objects will also be blocked. |  |

### Manage Bank Account Hierarchies

Purpose

The Manage Bank Account Hierarchies app is used to rebuild previous bank account hierarchy. Use this app to create many kinds of groups according your chosen group type. This section guides you through bank account group creation.

#### Create Bank Account Group

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you can create a bank account group which contains the candidate bank accounts.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log onto the SAP Fiori launchpad as a Cash Management Specialist. |  |  |
| 2 | Access the SAP Fiori app | Open Manage Bank Account Hierarchies (F4973). |  |  |
| 3 | Create New Hierarchy | Choose Create. | The New Hierarchy dialog box displays. |  |
| 4 | Enter Hierarchy Data | Make the following entries and choose Create:Type: Bank Account GroupHierarchy ID: GROUP_01Hierarchy Description: Test Group 01Valid From: <Input current date> | The maintenance UI displays your new nodes. |  |
| 5 | Add Bank Account to the Hierarchy | Choose the arrow icon at the end of the row for the hierarchy you created.In the right pane, expand the node where you want to add a bank account. |  |  |
| 6 | Edit | Choose Edit. |  |  |
| 7 | Add | In the row of the node you chose above, at the right side of the row, choose + (Add). |  |  |
| 8 | Add Subnode Details | Make the following entries and choose OK:Subnode: SelectedID: SUBNODE_01Description: Subnode 01 for group testing |  |  |
| 9 | Add Account to Node | On the subnode, choose + (Add).Make the following entries and choose OK:Bank Account: SelectedID: <Select an ID> | The bank account is added to the group.Note You can drag and drop nodes and accounts in the hierarchy to change their order. |  |
| 10 | Save | Choose Save. |  |  |
| 11 | Activate | Choose Activate. |  |  |

#### Edit Bank Account Group

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you can create a bank account group that contains the candidate bank accounts.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log onto the SAP Fiori launchpad as a Cash Management Specialist. |  |  |
| 2 | Access the SAP Fiori app | Open Manage Bank Account Hierarchies (F4973). |  |  |
| 3 | Deactivate Bank Account Group | In the row for the bank account hierarchy, choose the arrow icon to the right side of the row. |  |  |
| 4 | Deactivate | Choose Deactivate. |  |  |
| 5 | Edit Bank Account Group | Choose Edit. |  |  |
| 6 | Enter Data | Make the following entries and choose Save:Hierarchy Description: Change for testing |  |  |
| 7 | Activate | Choose Activate. | You have activated the change. |  |

#### Delete Bank Account Group

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you can delete a bank account group.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log onto the SAP Fiori launchpad as a Cash Management Specialist. |  |  |
| 2 | Access the SAP Fiori app | Open Manage Bank Account Hierarchies (F4973). |  |  |
| 3 | Deactivate Bank Account Group | In the row for the bank account hierarchy, choose the arrow icon to the right side of the row. |  |  |
| 4 | Deactivate | Choose Deactivate.Note If the bank account group's status is already inactive, you can skip this step. |  |  |
| 5 | Delete Bank Account Group | Choose Delete. |  |  |

### Review Bank Account and Destruct Bank Account Reviews (Workflow Mode)

#### Initiate Review Bank Account

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The step describes how to review bank account via workflow, cash specialist will start the review process and designate reviewers to review the bank account.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Cash Management Specialist. |  |  |
| 2 | Access the SAP Fiori App | Open Manage Bank Account Reviews (F7510). |  |  |
| 3 | Create Bank Account Review | Choose Create.Enter the following data and choose Create:Review ID: Review_01Reference Date: <Current Date>Review Description: Review Bank AccountsReview Area ID: RA01Review Area Description: Review Area for Bank Accounts |  |  |
| 4 | Enter Review Bank Accounts Parameters | Choose Edit.Choose the triangle button on the right of the review area to go to the detail page.Enter the following data in Bank Account Selections tab:Selection Field: Company CodeSelection Option: equal toValue: 3310Enter the following data in Reviewer tab:Review Step: 1Reviewer (User ID): select Cash ManagerNote If you add more than one step, the bank account review process can be completed after all the reviewers have finished the review process. The maximum steps are 5 by default, if you want to add more steps, please refer to Set Up More Review Steps (Optional).Choose Apply.Choose Save. |  |  |
| 5 | Take Snapshot | Choose the triangle button on the right of the Review Area ID to go to the detail page.Choose Take Snapshot. | The bank accounts to be reviewed are listed in the Bank Account Snapshot tab. |  |
| 6 | Start Review | Choose Start Review. |  |  |

#### Review Bank Accounts (Workflow)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, the designated reviewers in previous step will review the bank accounts in app My Inbox - All Items (F0862).

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Cash Manager. |  |  |
| 2 | Access the SAP Fiori App | Open My Inbox - All Items (F0862).Choose the bank account review task you triggered in previous step.Check if the snapshot is shown.Choose Approve.Choose Submit.Note You can forward the tasks to assign them to other users for processing. The steps are as follows:Choose the Forward button.In the Search field of the Forward dialog, enter the user ID of the target user manually, and choose search.(Optional) Add a note in the field with label Forward Note to the recipient of the task.Choose Forward. | The review status in Manage Bank Account Reviews (F7510) is In Process and the Review Area Status changed to Passed Review. |  |
| 3 | Complete Review | Log on to the SAP Fiori launchpad as a Cash Management Specialist.Open Manage Bank Account Reviews (F7510).Select the Review Area RA01 checkbox.Choose Set to Complete.Choose OK. | The Review Status changes to Completed. |  |

#### Destruction of Bank Account Reviews

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you can use the data destruction object FCLM_BAR_DESTRUCTION to destruct the whole entity of bank account reviews after the retention period.

Prerequisite

Before you start the following steps, please follow the Information Lifecycle Management ([1KA](https://me.sap.com/processnavigator/SolP/O60)) test script to check if Demo Exists in Audit Area of the Maintain Audit Area step. In case that Demo does not exist, you can create one with Y or Z customer namespace. Input the parameter Policy Category as Retention Rules, Audit Area as Demo, Assign ILM Object FCLM_POA to Audit Area Demo and set the status to Active in the Assign ILM Object to Audit Area step. Input the parameter Policy Category as Retention Rules, Audit Area as Demo, ILM Object as FCLM_POA in configuration activity 106666 Maintain ILM Policies and Rules, and follow the Maintain ILM Policies and Rules step of Information Lifecycle Management ([1KA](https://me.sap.com/processnavigator/SolP/O60)) to create Policies and Rules.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Data Privacy Specialist. |  |  |
| 2 | Access the SAP Fiori App | Note Before you start the following steps, please follow the Maintain ILM Policies step described in Information Lifecycle Management ([1KA](https://me.sap.com/processnavigator/SolP/O60)) test script to check if the Live status policy in Policy Category is Retention Rules, ILM Area is DEMO, and ILM Object is FCLM_BAR_DESTRUCTION.Open ILM Data Destruction (F2662). |  |  |
| 3 | Search Destruction Object | Select the Data Destruction Object and choose the Not Scheduled category.Search for the destruction object FCLM_BAR_DESTRUCTION. | The destruction objects that are currently not scheduled for a destruction run are listed. |  |
| 4 | Schedule Destruction | Select the checkbox of object FCLM_BAR_DESTRUCTION.Choose Schedule.On the pop up, choose Delete. |  |  |

#### Set Up Email Notifications

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This steps describe how to set up email notifications for bank account review.The predefined workflow for bank account review does not support email notifications. It is possible to enable email notifications to be sent to the reviewers and initiator during the review process of a review area by defining custom email templates (based on the email templates delivered by SAP) and assigning them to the bank account review workflow steps in a new bank account review workflow.

The following email notification templates are available:

- Bank Account Review Workflow Step Deadline (FCLM_BAR_DEADLINE)

The email template is used to inform the next reviewer that the bank account review needs to be performed now. The first reviewer gets this mail, when the review is started in the Manage Bank Account Reviews (F7510) app. The follow-on reviewers get a mail as soon as their predecessor approved the correctness of the snapshot data in the workflow task. If substitutes have been defined in the My Inbox - All Items (F0862) app, they will also receive these email notifications. If a reviewer forwards the review task to another user, this user will not receive an email notification.

- Bank Account Review Approved (FCLM_BAR_RESULT_APPROVED)

The email template is used to inform the initiator about the review result once a reviewer has approved the correctness of the snapshot data in the workflow task.

- Bank Account Review Rejected (FCLM_BAR_RESULT_REJECTED)

The email template is used to inform the initiator about the review result once a reviewer has rejected the correctness of the snapshot data in the workflow task.

Prerequisite

It requires the extensibility system to perform this function.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Extensibility Specialist. |  |  |
| 2 | Access the SAP Fiori App | Open Maintain Email Templates (F1306A). |  |  |
| 3 | Copy Predefined Template | Choose the Predelivered tab.Search for the object FCLM_BAR_DEADLINE.Select the radio button and choose Copy.Enter the following data and choose Copy:Email Template: Z_FCLM_BAR_DEADLINERepeat the above step to copy object FCLM_BAR_RESULT_APPROVED and FCLM_BAR_RESULT_REJECTED. |  |  |
| 4 | Log On | Log on to the SAP Fiori launchpad as a Cash Management Specialist. |  |  |
| 5 | Create Workflow with Email Notification | Open Manage Workflows - For Bank Accounts (F2796).Select Bank Account Review on the upper left corner dropdown list.Choose Create.Note Alternatively, you can just use an existing workflow that already has email notifications configured. Make sure that only the desired workflow with notifications is active.Enter the following data:Workflow Name: Email notification for bank account reviewIn the Step tab, choose Create.Go to the Deadlines tab and choose Create.Enter the following data:If step is not completed by: Step Started, 0, Hour(s)Execute the following action: Send mail notificationE-mail Template: Bank Account Review WorkflowIn the Recipients tab, enter the following data:Role: Processors of Task |  |  |

#### Set Up More Review Steps (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The delivered standard workflow supports up to 5 review steps per review area. It is possible to enhance the delivered workflow so that more than 5 review steps can be defined per review area.

Prerequisite

It requires extensibility system to perform this function.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Extensibility Specialist. |  |  |
| 2 | Access the SAP Fiori App | Open Custom Logic (F6957). |  |  |
| 3 | Define Implementations | Choose Create.Search Extension Point RSM_BADI_RESPONSIBILITY_RULE on the filter.Select the radio button for Extension Point RSM_BADI_RESPONSIBILITY_RULE.Choose Step 2.On the Implementation Attributes tab, choose Add.On the pop up window, choose Add.Enter the following data and choose Save:Filter Name: STATIC_RULE_FILTERComparator: =Value: The BAdI Filter Value you noted down in previous step, for example, YY1_FCLM_BAR_REVChoose Step 3.Enter the following data:Implementation Description: Bank Account Review ImplementationsImplementation ID: YY1_BANKACCOUNTREVIEWIMPLEMENTChoose Review.Choose Create.Choose Publish. |  |  |
| 4 | Access the SAP Fiori App | Open Manage Responsibility Rules (F4637). |  |  |
| 5 | Copy Predefined Responsibility Rules | Choose the Standerd tab.Enter the following data and choose Go:ID: FCLM_BAR_REVSelect the radio button and choose Copy.Enter the following data:ID: YY1_FCLM_BAR_REVDescription: Bank Account ReviewerOn the Parameters tab, enter the following data:Name: Leading_ObjectDescription: Leading_ObjectType: StructureCDS View: I_BKACCOUNTREVIEWAREAWORKFLOWName: REVIEWSTEPDescription: Review StepsType: ElementCDS View: I_BANKACCOUNTREVIEWERCDS Field: BANKACCOUNTREVIEWSTEPChoose Create. |  |  |
| 6 | Access the SAP Fiori App | Open Manage Responsibility Contexts (F4636). |  |  |
| 7 | Define Additional Agent Rules | Enter WS48000097 in the ID filter.Choose Go.Select the radio button of WS48000097 and choose Extend.Note If the responsibility contexts ID WS48000097 has already been extended, the Extend button will be grayed out. In this case, you can skip this step.Choose Create.Enter the following data and choose Go:ID: YY1_WS48000097Choose the triangle button on the right to go into the detail of YY1_WS48000097.Choose Edit.On the Agent Rule tab, choose Create.Enter the following data and choose Save:ID: YY1_REVIEWER_01Description: Bank Account Review Area Reviewer 01Responsibility Rule ID: YY1_BAR_REV |  |  |
| 8 | Create Workflow for More Review Steps | Log on to the SAP Fiori launchpad as a Cash Manager.Open Manage Workflows - For Bank Accounts (F2796).Select Bank Account Review on the upper left corner dropdown list.Choose Create. |  |  |
| 9 | Create Reviewer Step | On the Steps tab, choose Create.On the recipients tab, make the following entries:Role: Bank Account Review Area Reviewer 1Select the radio button for One of the recipients.Choose Create. |  |  |
| 10 | Create Reviewer Steps | Repeat Test Step 9 to create Roles:Bank Account Review Area Reviewer 2Bank Account Review Area Reviewer 3Bank Account Review Area Reviewer 4Bank Account Review Area Reviewer 5Bank Account Review Area Reviewer 6 |  |  |
| 11 | Save and Activate Workflow | Choose Save.Choose Active.Choose Define Order to rank the newly created workflow on first priority. |  |  |

### Assign Rating Procedures and Ratings to Business Partner

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you can assign rating procedures and ratings to business partners, and the bank associated with the business partner will then be marked with these ratings. If you want to use your own rating procedures and ratings, you can proceed to the Set Rating Procedures and Ratings step to configure them. Otherwise, you can skip the configuration step and use SAP's pre-delivered rating procedures and ratings.

Prerequisite

A Business Partner with the role TR0703 should be created. You can refer to the step Create Business Partners for Bank Account Management in scope item BFA, Basic Bank Account Management, to create one. Be sure to note down the bank keys that are associated with the business partner.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Master Data Specialist - Business Partner Data. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Maintain Business Partner (BP). |  |  |
| 3 | Maintain Business Partner | Make the following entry and choose Start:Business Partner: <Enter the business partner number that you created by following the step Create Business Partners for Bank Account Management in scope item BFA, Basic Bank Account Management>Double-click the business partner line item to view its details.Choose Switch Between Display and Change.Make the following entry and choose Enter:Display in BP Role: TR0703 Bank |  |  |
| 4 | Enter Rating Data | Choose the Ratings tab.Make the following entries:Rat.Proc.: for example, 1_FitchRating: for example, 1_AAAChoose Enter.Choose Save. | Log on to the SAP Fiori launchpad as a Cash Management Specialist. Open the Manage Banks - Cash Management (F1574A) app. Enter the bank key you noted in the prerequisite step, which is associated with the business partner—into the filter. Open the details, and on the Ratings tab, you can find information about the rating procedures and ratings. |  |

### Bank Account Report and Fact Sheet

#### Foreign Bank Account Report

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This report displays the bank accounts that are opened in foreign countries.

Prerequisite

Foreign bank accounts exist in the system.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Cash Manager. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Foreign Bank Account Report (F1575). |  |  |
| 3 | Enter Selection Criteria | Make the following entries and choose Go:Home Country: <For example, US, PR.>Note In the Home Country/Region field, you specify countries and regions that are considered as territories of the State where your company is created and organized. Bank accounts maintained with banks located outside of the specified countries and regions are regarded as foreign bank accounts in calculation. In above example, you specify US and PR as territories of the State where your company is created and organized. Bank accounts outside US and PR are regarded as foreign bank accounts and will be listed.Time Range: For example, 01/01/2020 – 12/31/2020Note If a selection field is not shown, choose Adapt Filters to select and display the missing criteria. | The foreign bank accounts are displayed in the table view. |  |
| 4 | Review Result List | Choose Go. | The foreign bank accounts are displayed in a form view in the Result List area. |  |
| 5 | Review Employee | Choose the Employee tab. | The system displays a list of signatories for foreign bank accounts, which are authorized representatives maintained in the Manage Powers of Attorney for Banking Transactions (F5742) app. |  |
| 6 | Review Company Code | Choose Company Code tab | You can review the foreign bank account at company code level. |  |

#### Bank (Fact Sheet)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This fact sheet displays the banks that are opened in the system.

Prerequisites

Bank master data exists in the system.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Cash Manager. |  |  |
| 2 | Search | Choose the Search button (magnifying glass icon) in the top header. | The search box displays. |  |
| 3 | Enter Selection Information | Make the following entries and press Enter:Dropdown: BanksSearch field: 18121976 | The bank matching that bank number is displayed. |  |
| 4 | Review Bank Information | To expand or hide the bank details, choose the arrow button on the bottom right of the bank details. |  |  |

#### House Bank (Fact Sheet)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This fact sheet displays the house banks that are defined in the system.

Prerequisites

House banks exist in the system.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Cash Manager. |  |  |
| 2 | Search | Choose the Search button (magnifying glass icon) in the top header. | The search box displays. |  |
| 3 | Enter Selection Information | Make the following entries and press Enter:Dropdown: House BanksSearch field: AEBK1 | The selected house bank is displayed. |  |
| 4 | Review Bank Information | Choose the arrow icon to expand or hide the details. |  |  |

#### House Bank Account (Fact Sheet)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This fact sheet displays the house bank accounts that are created in the system.

Prerequisites

House bank accounts exist in the system.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Cash Manager. |  |  |
| 2 | Search | Choose the Search button (magnifying glass icon) in the top header. | The search box displays. |  |
| 3 | Enter Selection Information | Make the following entries and press Enter:Dropdown: House Bank AccountsSearch field: AEAC1 | The selected house bank account is displayed. |  |
| 4 | Review Bank Information | Choose the arrow icon to expand or hide the details. |  |  |

## Appendix

### Split Technical Bank Accounts (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

For historical reason, there might be some technique bank account with multiple bank account connectivity path exist in the system. But according to the latest bank account management logic, the technique bank account only support one bank account connectivity path. This app provide a tool to split the existing technique bank account with multiple bank account connectivity path.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log onto the SAP Fiori launchpad as a Cash Management Specialist. |  |  |
| 2 | Access the SAP Fiori app | Open Split Technical Bank Accounts. |  |  |
| 3 | Split Technique Bank Account | Select the technique bank account with status Red.Choose Split. | A new bank account is created based on the splited technique bank account. You can go to app Application Log Message to check the split log, and go to app Manage Bank Account to check the newly created bank account. |  |

### Migrate Bank Control Keys (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

Field Bank Control Key exist both in bank account master data and bank account connectivity path. Since the field of bank control key in bank account connectivity path is obsolete, it is hiddened in the application of the connectivity path but still exist in the table. For the existing bank accounts that still have bank control key in the table of connectivity path, you can use this migration functionality to synchronize the bank control key in bank account master data and bank account connectivity path.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log onto the SAP Fiori launchpad as a Cash Management Specialist. |  |  |
| 2 | Access the SAP Fiori app | Open Migrate Bank Control Keys (FCLM_BKONT_MIGRATION). |  |  |
| 3 | Migrate Bank Control Key | Select the to be migrated item.Choose Migrate.Input the following entry:Bank Control Key: 03Choose Continue. | The bank control key in the bank account connectivity path is cleared, the value in the bank account master data is updated. |  |

### Import Existing Bank Account Group (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you can import the bank account groups that are created in the Manage Bank Accounts (WDA_FCLM_BAM_HIERARCHY) app. The app Manage Bank Accounts (WDA_FCLM_BAM_HIERARCHY) is obsolete, it has been replaced by app Manage Global Hierarchies (F2918). The bank account group creation function has been dismantled from app Manage Bank Accounts (WDA_FCLM_BAM_HIERARCHY), it only has functions to display the existing bank account group.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log onto the SAP Fiori launchpad as a Cash Management Specialist. |  |  |
| 2 | Access the SAP Fiori app | Open Manage Global Hierarchies (F2918). |  |  |
| 3 | Import Whole Old Bank Account Group | Choose Import Hierarchy. |  |  |
| 4 | Import Hierarchy | Make the following entries and choose OK:Source: Bank Account GroupBank Account Group ID: <bank account group ID> |  |  |
| 5 | Enter Data | Make the following entries and choose Create:Hierarchy ID: H001Hierarchy Description: Hierarchy H001Valid From: <current date> |  |  |
| 6 | Import Subnode of Old Bank Account Group | In the row for the bank account group, choose the arrow icon to the right of the row. |  |  |
| 7 | Edit | Choose Edit. |  |  |
| 8 | Select Subnode | Select the subnode's checkbox, then choose the More button. |  |  |
| 9 | Import Subnode | Choose Import Nodes. |  |  |
| 10 | Import Subnode | Make the following entries and choose OK:Source: Bank Account Group NodeBank Account Group ID: <bank account group node> |  |  |
| 11 | Save | Choose Save. |  |  |
| 12 | Activate | Choose Activate. | Your nodes are activated. |  |

### Bank Relationship Overview

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you can access key information about bank relationship management and gain insights into current trends. Its functionality provides a central source of information for recent payments, bank profiles, bank fees and bank account statuses.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log onto the SAP Fiori launchpad as a Cash Management Specialist. |  |  |
| 2 | Access the SAP Fiori app | Open Bank Relationship Overview (F3775). |  |  |
| 3 | Enter Selection Criteria | Make the following entries:Display Currency: USDExchange Rate Date: <Current Date>Exchange Rate Type: <M>Press ENTER. |  |  |

### Succeeding Processes

After completing the activities in this test case, you can continue testing the following business processes:

| Process | Business Condition |
| --- | --- |
| J78 | The bank accounts created in Advanced Cash Operations (J78) can be used for further processing. For example, importing bank statement, making bank transfer, and so on. This processing is optional. |

### Configuration

After the bank account is created, changed, or closed, the following configuration must be completed.

- Bank Determination

When a new bank account (including house bank and house bank account ID) is created, maintain the corresponding bank subaccount (clearing account) for payment program for vendors (or customers). Afterward, the payment program for vendors (or customers) can find the bank subaccount for financial posting purposes. When a bank account is changed or closed, the bank subaccount (clearing account) determination of the payment program may also require update.

Because this is a configuration step, in the SAP S/4HANA Enterprise Management Cloud system, use the Bank Determination self-service configuration UI to complete the configuration. In SAP S/4HANA system, use IMG activity Financial Accounting (New) > Accounts Receivable and Accounts Payable > Business Transactions > Outgoing Payments > Automatic Outgoing Payments > Payment Method/Bank Selection for Payment Program > Set Up Bank Determination for Payment Transactions. For more information, see the External Financial Basics (J16) guide. Perform this step in the development system; contact your system administrator to transport it to the production system.

- Clearing Account for Paying & Receiving Bank Accounts

If a new bank account is used as a paying/receiving bank account in bank transfer (from one bank account to another bank account), you must configure the bank subaccount (clearing account) determination for paying and receiving bank accounts in bank transfer. Once done, you can create the financial posting of bank transfer. When a bank account is changed or closed, the bank subaccount determination for bank transfer may also require update.

Because this is a configuration step, in SAP S/4HANA Enterprise Management Cloud system, use the Define Account Determination for Bank Clearing Accounts and Define Clearing Accts for Receiving Bank for Acct. Transfer self-service configuration UIs to complete the configuration. In the SAP S/4HANA system, use IMG activity Financial Accounting (New) > Bank Accounting > Business Transactions > Payment Transactions > Payment Request > Define Clearing Accts for Receiving Bank for Acct. Transfer and IMG activity Financial Accounting (New) > Bank Accounting > Business Transactions > Payment Handling > Bank Clearing Account Determination > Define Account Determination for Bank Clearing Accounts. . For more information, see the Cash Daily Operation – Delta for Extended Version (BFP and 2N5) configuration guides. Perform this step in the development system; contact your system administrator to transport it to the production system.

- Define Default Liquidity Items for G/L Accounts

If you created G/L accounts of bank subaccounts (for example, 11003010–11003080), define a default liquidity item for each G/L account. When a bank account is changed or closed, and bank subaccounts are possibly updated or deleted consequently, you must also update the Define Liquidity Items for G/L Accounts configuration.

Because this is a configuration step, in the SAP S/4HANA Enterprise Management Cloud system, use the SAP Fiori app Define Default Liquidity Items (Deprecated) - For G/L Accounts (FLQINFACC) to complete the configuration. In the SAP S/4HANA system, use IMG activity Financial Supply Chain Management > Cash and Liquidity Management > Cash Management > Liquidity Items > Derivation Rules for Liquidity Items > Define Default Liquidity Items for G/L Accounts . The configuration in this customizing activity cannot be transported to other clients. You must perform this configuration in the production, development system, and consolidation test systems. With SAP S/4HANA, aside from G/L Accounts, Cloud customers can define liquidity item derivation rules based on more information, via Define Derivation Rules in SAP Fiori app Liquidity Item Hierarchy (WDA_FCLM_LQH). To get more information and guide, please further check SAP note[2530814](https://me.sap.com/notes/%202530814) - Enable Liquidity Item Derivation via BRF+.

You may refer to the following rule for new bank subaccounts:

| Account from | Account to | Incl/excl | Default Value (of Liquidity Item) | Name (of Liquidity Item) |
| --- | --- | --- | --- | --- |
| 11003010 | 11003010 | Inclusive of defined values/range | BNK_0002 | Cash Payment |
| 11003020 | 11003020 | Inclusive of defined values/range | BNK_0003 | Bank Transfer |
| 11003030 | 11003030 | Inclusive of defined values/range | BNK_0009 | Other Interim Transfers |
| 11003040 | 11003040 | Inclusive of defined values/range | BNK_0005 | Direct Debit Out |
| 11003050 | 11002050 | Inclusive of defined values/range | BNK_0007 | Checks Out |
| 11003060 | 11003060 | Inclusive of defined values/range | BNK_0006 | Checks In |
| 11003070 | 11003070 | Inclusive of defined values/range | BNK_0006 | Checks In |
| 11003080 | 11003080 | Inclusive of defined values/range | BNK_0001 | Cash Receipt |

- Other Configurations

Besides the configurations mentioned above, there are additional configurations required for bank-related G/L accounts: Classify G/L Accounts for Document Splitting in Financial Accounting – General Ledger Accounting. Add these new G/L accounts in to the Financial Statement Version.

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
> Flagged while digesting this document, not verified: In the Two-Person Verification closing path the status after initial closing is called 'To Be Closed' (and the status table description mentions it), whereas the Workflow closing path calls the same state 'Closing Request Sent to Bank'; the status names for the same step differ within the document.

## Connections
- part-of :: [[_cluster]]
- related-to :: [[05-treasury-and-cash-management/test-script-advanced-bank-account-management-j77-ae-sap-s-4hana-cloud-part-01]]
- related-to :: [[05-treasury-and-cash-management/test-script-basic-bank-account-management-bfa-ae-sap-s-4hana-cloud-pub]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/J77_S4CLD2608_BPD_EN_AE.docx` — lines 2889–5542 of the extracted text · extracted with `mammoth` · 466,078 chars in the whole document
