---
id: 05-treasury-and-cash-management/test-script-treasury-trading-via-trading-platforms-2f5-sap-s-4hana-clo-part-02
title: "Test Script: Treasury Trading via Trading Platforms (2F5) - SAP S/4HANA Cloud Public Edition (2F5_S4CLD2608_BPD_EN_XX) — part 2 of 2"
description: "S/4HANA Cloud 2608 test script (2F5): treasury trading via external platforms - MM/MMF steps, optional trade tasks, mapping and business-rule examples."
cluster: 05-treasury-and-cash-management
tags: [kb/treasury-and-cash-management, topic/treasury-trading-platforms-and-swift]
aliases: []
keywords: [Treasury Trading Platforms and SWIFT Correspondence, money market fund trades, mmf without clearing house, mmf clearing house scenario, trading platform integration, trade request processing, trade editing and reprocessing, counterparty limits, field mappings, business rules]
sources: ["raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/2F5_S4CLD2608_BPD_EN_XX.docx#lines-3619-4517"]
confidence: low
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-821
topic: 05-treasury-and-cash-management/treasury-trading-platforms-and-swift
language: EN
part: 2/2
created: 2026-10-12
updated: 2026-10-12
---

# Test Script: Treasury Trading via Trading Platforms (2F5) - SAP S/4HANA Cloud Public Edition (2F5_S4CLD2608_BPD_EN_XX) — part 2 of 2

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/2F5_S4CLD2608_BPD_EN_XX.docx`, part 2 of 2 (lines 3619–4517 of the extracted text), extracted with `mammoth`. Grouped under **Treasury Trading Platforms and SWIFT Correspondence** in Treasury and Cash Management. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

| 2 | Display the External Trade Request(s) | On the Manage Intercompany Trade Requests screen, enter following data and choose Go:Trade Request ID (Back End): for example, <Trade Request ID (backend) – Trading via Trading Platform MM 1> | The following trade requests is displayed:Trade Request ID (backend) – Trading via Trading Platform MM 1Go to the detailed page of the trade requests and note down the trade request IDs: XXX-XXXXXXXXXXXXXXXXXXXXXXXXXX |  |
| 3 | Send Trade Request | Select the checkbox(es) of all the external trade request(s) under the same Back End Trade Request ID, and choose Send.Select the trading platform in the Select Trading Platform Profile dialog box and choose OK to confirm. | The intercompany trade request has been sent to external Trading platform:Trade Request ID (backend) – Trading via Trading Platform FX Forward 1 |  |
| 4 | Reload Page | Reload the page, and confirm the status of the trade request is Sent to Trading Platform. | The status of the trade request(s) is now Sent to Trading Platform. |  |

##### Review Intercompany MM Trade Request Status in External Trading Platform

Purpose

In this step, you may review the trade requests in the external trading platform.

Prerequisite

You’ve sent intercompany trade requests to the external trading platform.

Procedure

This step is performed in the external trading platform.

You may use the trade request IDs you’ve noted down in previous step to search for your trade requests in the external trading platforms.

##### Create Intercompany MM Trades in External Trading Platform

Purpose

In this step, you create intercompany money market trades for the intercompany trade requests you’ve reviewed in previous step in the external trading platforms.

Procedure

This step is performed outside of your SAP S/4HANA Cloud Public Edition system. You need to do this step in External Trading Platforms.

Note down the IDs of the FX trades you created in the external trading platform. This ID will be filled in the External reference field in the Manage Intercompany Trades app in SAP trading platform integration.

Make sure you have created intercompany trades for following intercompany trade request:

- Trade Request ID (backend) – Trading via Trading Platform MM 1

##### Generate Intercompany MM Trades in SAP Trading Platform Integration

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The intercompany MM trades created in the external trading platform will be automatically imported into SAP trading platform integration. Follow the steps below to review the intercompany MM trades in SAP trading platform integration.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Open the Manage Intercompany Trades app in SAP trading platform integration. | A list of all intercompany MM trades imported from external trading platforms is displayed. |  |
| 2 | Enter Filter | Choose Adapt Filters, enter the following data and choose Go:External reference: <Reference IDs noted from the previous step> | The intercompany MM trades you created in external trading platforms in the previous step are displayed in SAP trading platform integration.The status of the FX trades should be Successful.Note Note down the Financial transaction in the detailed page: XXXX/XXXXXXXXXXXXX Note The first 4 chars XXXX is the company code in SAP S/4HANA Cloud Public Edition. The last 13 chars XXXXXXXXXXXXX is the transaction number. |  |

##### Create Intercompany Money Market Transactions in SAP S/4HANA Cloud Public Edition

Purpose

This is an automatic step. The MM transactions are automatically created in the SAP S/4HANA Cloud Public Edition system. In this step, you check the MM transaction information in the SAP S/4HANA Cloud Public Edition system.

Procedure

Please follow the following section of this test script to check the MM transactions in SAP S/4HANA Cloud Public Edition.

- Treasury Trading via Trading Platforms - MM Inbound
    - [Create Money Market Transaction in SAP S/4HANA Cloud Public Edition](#unique_70) [page ] 101

### Treasury Management Integration for Trading Platform - MMF

The Money Market fund external scenario handles trades with external counterparties. In current release, this only includes the following process:

Create MMF trades with external counterparties in the external trading platform and import them into SAP trading platform integration and SAP S/4HANA Cloud Public Edition.

Main steps in the process include:

- [Create Money Market Fund Trade in External Trading Platform](#unique_89) [page ] 135
- [Generate Money Market Fund Trade in SAP Trading Platform Integration](#unique_90) [page ] 136
- [Create Money Market Fund Transactions in SAP S/4HANA Cloud Public Edition](#unique_91) [page ] 137

#### Analyze Liquidity Forecast in S/4HANA Cloud

Purpose

In this step, you review the liquidity forecast and make decisions for financial transactions, such as money market, foreign exchange, or money market fund.

Procedure

Perform the following steps in the Debt and Investment Management (1WV) test script:

- Analyze Liquidity Forecast

#### Create Money Market Fund Trade in External Trading Platform

Purpose

In this step, you create a money market fund trade in the external trading platform. Money market fund trades created with or without Clearing House are supported.

Procedure

This step is performed outside of your SAP S/4HANA Cloud Public Edition system or SAP trading platform integration. You need to do this step in the external trading platforms (i.e. ICD Portal).

|  |
| --- |
| Note You may note down the Trade ID and name it as Trade ID - external trading platform. |

#### Treasury Management Integration for Trading Platform – MMF w/o Clearing House Scenario

In current release, MMF w/o clearing house scenario includes the following process:

Create MMF trades with known quantity and price in the external trading platform and import them into SAP trading platform integration and SAP S/4HANA Cloud Public Edition.

Main steps in the process include:

- [Generate Money Market Fund Trade in SAP Trading Platform Integration](#unique_90) [page ] 136
- [Create Money Market Fund Transactions in SAP S/4HANA Cloud Public Edition](#unique_91) [page ] 137

##### Generate Money Market Fund Trade in SAP Trading Platform Integration

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This is an automatic step. Once a money market fund trade is closed in the external trading platforms, SAP trading platform integration will automatically receive and submit the money market fund trade to SAP S/4HANA Cloud Public Edition. If you want to check the money market fund trade data in SAP trading platform integration, you can follow the following procedures to check.

Prerequisite

You've created a money market fund trade with known quantity and price in non-clearing house scenario in the previous step.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Open the Manage Trades app in SAP trading platform integration. |  |  |
| 2 | Enter Filters | Choose Adapt Filters, enter the following data and choose Go:External Trade ID: <Trade ID - external trading platform > | The money market fund trade you created in external trading platforms in the previous step is displayed in SAP trading platform integration.The status of the money market trade is Successful. |  |
| 3 | Go to Detailed Page | Choose Details (arrow > ) to go to the detail page. | The detailed trade information is displayed.Note down the Financial transaction:XXXX/XXXXXXXXXXXXXThe first four characters XXXX is the company code in SAP S/4HANA Cloud Public Edition.The last 13 characters XXXXXXXXXXXXX is the transaction number. |  |

##### Create Money Market Fund Transactions in SAP S/4HANA Cloud Public Edition

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This is an automatic step. The money market fund transactions are automatically created in the SAP S/4HANA Cloud Public Edition system. In this step, you check the money market fund transaction data in the SAP S/4HANA Cloud Public Edition system using the following Fiori app:

- Process Securities Transactions - Collective Processing (TS00)

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as Treasury Specialist - Front Office | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the SAP Fiori App | Open Process Securities Transactions - Collective Processing (TS00). | The Securities: Collective Processing screen is displayed. |  |
| 3 | Enter Selection Criteria and Execute | Enter the following data and choose Execute：Company Code: <The first four character of the Financial Transaction Reference ID you noted down in previous step>Transaction: <The last 13 characters of the Financial Transaction you noted down in previous step> |  |  |
| 4 | Display the Money Market Fund Transaction Details | Select the checkbox at the beginning of the money market fund transaction and choose Display.You can now compare the money market fund transaction data on the external trading platform with that in the SAP S/4HANA Cloud Public Edition system. | The money market fund transaction data should be consistent with that in the external trading platform. |  |

#### Treasury Management Integration for Trading Platform – MMF Clearing House Scenario

In current release, MMF clearing house scenario includes the following process:

Create MMF trades w/o known quantity and price in the external trading platform and import them into SAP trading platform integration and SAP S/4HANA Cloud Public Edition. Once the quantity and price of the MMF trades are known in the external trading platforms, then update MMF trades with quantity and price information in external trading platforms and import them into SAP trading platform integration and SAP S/4HANA Cloud Public Edition

Main steps in the process include:

[Generate Money Market Fund Trade w/o Known Quantity and Price in SAP Trading Platform Integration](#unique_92) [page ] 138

[Create Money Market Fund Transactions w/o Known Quantity and Price in SAP S/4HANA Cloud Public Edition](#unique_93) [page ] 140

[Update Money Market Fund Trade with Quantity and Price Information in External Trading Platform](#unique_94) [page ] 141

[Update Money Market Fund Trade with Quantity and Price Information in SAP Trading Platform Integration](#unique_95) [page ] 141

[Update Money Market Fund Transactions with Quantity and Price Information in SAP S/4HANA Cloud Public Edition](#unique_96) [page ] 142

##### Generate Money Market Fund Trade w/o Known Quantity and Price in SAP Trading Platform Integration

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This is an automatic step. Once a money market fund trade is closed in the external trading platforms, SAP trading platform integration will automatically receive and submit the money market fund trade to SAP S/4HANA Cloud Public Edition. If you want to check the money market fund trade data in SAP trading platform integration, you can follow the following procedures to check.

Prerequisite

You've created a money market fund trade with the quantity and price unknown in a clearing house scenario in the external trading platform.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Open the Manage Trades app in SAP trading platform integration. |  |  |
| 2 | Enter Filters | Choose Adapt Filters, enter the following data and choose Go:External Trade ID: <Trade ID - external trading platform > | The money market fund trade you created in external trading platforms in the previous step is displayed in SAP trading platform integration.The status of the money market trade is Successful. |  |
| 3 | Go to Detailed Page | Choose Details (arrow > ) to go to the detail page. | The detailed trade information is displayed.Note down the Financial transaction:XXXX/XXXXXXXXXXXXXThe first four characters XXXX is the company code in SAP S/4HANA Cloud Public Edition.The last 13 characters XXXXXXXXXXXXX is the transaction number. |  |

##### Create Money Market Fund Transactions w/o Known Quantity and Price in SAP S/4HANA Cloud Public Edition

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This is an automatic step. The money market fund transactions are automatically created in the SAP S/4HANA Cloud Public Edition system. In this step, you check the money market fund transaction data in the SAP S/4HANA Cloud Public Edition system using the following Fiori app:

- Process Securities Transactions - Collective Processing (TS00)

|  |
| --- |
| Note You may follow following section of Money Market Mutual Fund Management(2UN) to further process the money market fund transaction in SAP S/4HANA Cloud Public Edition system:Set Settlement StatusPayment for Purchase |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as Treasury Specialist - Front Office | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the SAP Fiori App | Open Process Securities Transactions - Collective Processing (TS00). | The Securities: Collective Processing screen is displayed. |  |
| 3 | Enter Selection Criteria and Execute | Enter the following data and choose Execute：Company Code: <The first four character of the Financial Transaction Reference ID you noted down in previous step>Transaction: <The last 13 characters of the Financial Transaction you noted down in previous step> |  |  |
| 4 | Display the Money Market Fund Transaction Details | Select the checkbox at the beginning of the money market fund transaction and choose Display.You can now compare the money market fund transaction data on the external trading platform with that in the SAP S/4HANA Cloud Public Edition system. | The money market fund transaction data should be consistent with that in the external trading platform. |  |

##### Update Money Market Fund Trade with Quantity and Price Information in External Trading Platform

Purpose

In this step, you receive a money market fund trade (quantity and price not known) in the external trading platform (for example, in ICD portal) with the quantity and price information.

Prerequisite

A Money Market Fund Trade (quantity and price not known) has been created in external trading platforms and transferred into SAP trading platform integration and SAP S/4HANA Cloud Public Edition system.

Procedure

This step is performed outside of your SAP S/4HANA Cloud Public Edition system or SAP trading platform integration. You need to do this step in the external trading platforms.

##### Update Money Market Fund Trade with Quantity and Price Information in SAP Trading Platform Integration

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This is an automatic step. Once a money market fund trade is updated with quantity and price information in the external trading platforms, SAP trading platform integration will automatically receive and submit the updated money market fund trade to SAP S/4HANA Cloud Public Edition. If you want to check the money market fund trade data in SAP trading platform integration, you can follow the following procedures to check.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Open the Manage Trades app in SAP trading platform integration. |  |  |
| 2 | Enter Filters | Choose Adapt Filters, enter the following data and choose Go:External Trade ID: <Trade ID - external trading platform > | The money market fund trade you created in external trading platforms in the previous step is displayed in SAP trading platform integration.The status of the money market trade is Successful. |  |
| 3 | Go to Detailed Page | Choose Details (arrow > ) to go to the detail page. | The detailed trade information is displayed.Note down the Financial transaction:XXXX/XXXXXXXXXXXXXThe first four characters XXXX is the company code in SAP S/4HANA Cloud Public Edition.The last 13 characters XXXXXXXXXXXXX is the transaction number. |  |

##### Update Money Market Fund Transactions with Quantity and Price Information in SAP S/4HANA Cloud Public Edition

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This is an automatic step. The money market fund transactions are automatically updated in the SAP S/4HANA Cloud Public Edition system. In this step, you check the money market fund transaction data in the SAP S/4HANA Cloud Public Edition system using the following Fiori app:

- Process Securities Transactions - Collective Processing (TS00)

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as Treasury Specialist - Front Office | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the SAP Fiori App | Open Process Securities Transactions - Collective Processing (TS00). | The Securities: Collective Processing screen is displayed. |  |
| 3 | Enter Selection Criteria and Execute | Enter the following data and choose Execute：Company Code: <The first four character of the Financial Transaction Reference ID you noted down in previous step>Transaction: <The last 13 characters of the Financial Transaction you noted down in previous step> |  |  |
| 4 | Display the Money Market Fund Transaction Details | Select the checkbox at the beginning of the money market fund transaction and choose Display.You can now compare the money market fund transaction data on the external trading platform with that in the SAP S/4HANA Cloud Public Edition system. | The money market fund transaction data should be consistent with that in the external trading platform. |  |

## Appendix

### Set Trade Requests to Completed (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you set a trade request to the completed status manually. For example, you've already fulfilled the trade requests, you may set it to the completed status manually.

Once the status of the trade request is set to completed, the trade request can no longer be further processed.

Procedure

Table 10: Set a Trade Request to Completed status

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Open the Manage Trade Requests app in SAP trading platform integration. | A list of trade requests is displayed. |  |
| 2 | Set a Trade Request to Completed status | On the Manage Trade Requests screen, select the checkbox before the trade request you want to set the completed status.Choose Details (arrow >).On the Trade Request screen, choose Set to Completed.Choose OK in the subsequent Warning dialog box. | The following message is displayed:Trade request was set to completed. |  |

### Edit Trades (Optional）

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

Normally, after you create an FX transaction in the external trading platform (for example, 360T or FXall), the deal will be imported into trading platform integration application on SAP BTP immediately. Then the trading platform integration application will transfer the FX transaction details to SAP S/4HANA Cloud Public Edition in which an FX transaction will be created.

In some cases, this inbound process might fail due to technical issues or mapping issues. In such case, you may edit the FX transaction details and then reprocess it to finish this process successfully.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Open the Manage Trades app in SAP trading platform integration. |  |  |
| 2 | Set filter to select Trades with Mapping error and Technical Error | On the Manage Trades screen, in the filter area in the upper side of the screen, select Mapping error and Technical Error in the Status field and then choose Go. | A list of Trades with mapping error and technical error is displayed. |  |
| 3 | Navigate to the trade’s detailed screen | On the Manage Trades screen, select a trade with mapping error or technical error, and choose Details (i.e. at the end of the row). | The detailed screen of the trade is displayed. |  |
| 4 | Check the error message | On the trade’s detailed screen, click on Message, | The screen scroll to the error messages section and the error details are displayed. |  |
| 5 | Edit the trade | On the top of the screen, choose Edit. Maintain the fields you want to edit and choose Save.Note:You may choose Save and Reprocess to save and reprocess immediately. | The trade is saved. |  |
| 6 | Reprocess the trade | On the top of the screen, choose Reprocess. A Confirmation dialog box is displayed. Choose OK to continue.Reload the page and you can see the status of the trade is updated. | The status of the trade is updated. |  |

### Assign and Unassign Processor of Trade Requests (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you assign yourself as the processor to a trade request. Once a trade request is assigned to a processor, it can only be further processed by the processor. You may also unassign the processor from a trade request.

Procedure

Table 11: 1. Assign a processor to a trade request

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Open the Manage Trade Requests app in SAP trading platform integration and choose Go. | A list of trade requests is displayed. |  |
| 2 | Assign a processor to a trade request | On the Manage Trade Requests screen, select the checkbox before the trade request you want to assign to a processor.Choose Assign Processor, and the Assign Processor dialog box is displayed. Choose Assign to confirm the assignment | The following message is displayed:A processor is being assigned to the trade requests. |  |

Table 12: 2. Unassign a processor from a trade request

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Open the Manage Trade Requests app in SAP trading platform integration and choose Go. | A list of trade requests is displayed. |  |
| 2 | Assign a processor to a trade request | On the Manage Trade Requests screen, select the checkbox before a trade request for which you are the processor.Choose Unassign Processor, and the Unassign Processor dialog box is displayed . Choose Unassign to confirm and close the dialog box. | The following message is displayed:The processor is being unassigned to the trade requests. |  |

### Partial Decline for a Trade Request (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In cases where you've split a trade request into several small ones, you can decline some of these split requests. In this step, you decline a split trade request. Once it is declined, you cannot further process the trade request.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Open the Manage Trade Requests app in SAP trading platform integration and choose Go. | A list of trade requests is displayed. |  |
| 2 | Assign a processor to a trade request | On the Manage Trade Requests screen, select the checkbox before the split trade request.Choose Decline, and the Reason for Declining dialog box is displayed. Choose a reason and close the dialog box. | The following message is displayed:Trade Requests are being declined. |  |

|  |
| --- |
| Note Once all the split trade requests are processed (declined or sent to external trading platform), the status of the trade request in SAP S/4HANA Cloud Public Edition will also be updated. You may refer to the following section of the Foreign Currency Risk Management(1X1) test script to check its status:Check Trade Request Status |

### Check Counterparty Limit in SAP Trading Platform Integration

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you can synchronize the counterparty limit status from the SAP S/4HANA Cloud Public Edition system to SAP trading platform integration and review the counterparty limit in SAP trading platform integration.

Prerequisite

- Setup configurations for backend connection
- Setup configurations for mappings

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP trading platform integration | The SAP trading platform integration apps are displayed in theSAP trading platform integration home page. |  |
| 2 | Access the SAP Fiori App | Open the Counterparty Limit Utilization app and choose Go. | The Counterparty Limit Utilization screen is displayed. |  |
| 3 | Synchronize Counterparty Limit | On the Counterparty Limit Utilization screen, choose Get. | A window of Success is displayed with following message:Data for counterparty limit utilization was retrieved. |  |
| 4 | Review Counterparty Limit | Choose OK to close the window of Success.Choose Adapt Filters and enter following data:Limit Type: for example, Y03Choose the Table View button on the right side of the screen and choose Go.Note You may use the Review Limit Utilizations app in SAP S/4HANA Cloud Public Edition to check the counterparty limit and the counterparty limit amount in SAP trading platform integration should be the same with that in SAP S/4HANA Cloud Public Edition. | A list of the counterparty limit is displayed. |  |

### Field Mapping Settings Example

Purpose

A full field mapping example is listed as below for your reference. You may adjust the mappings according to your business requirement.

#### Configure Mappings - Trading Platform Format

|  |
| --- |
| Remember The sample value provided below are for DE. Substitute the country/region-specific values provided by Best Practices for SAP S/4HANA or use master data values you have created for this purpose. |

360T-Inbound

| Field | Mapping Type | Source Field | Source Value | Target Value | Constant |
| --- | --- | --- | --- | --- | --- |
| COMPANY_ID | Copy and Reference Table | PARTICIPANT_COMPANY_REQUEST | SAP SE | 1710 |  |
|  |  |  | Default Target Value | 1010 |  |
| COUNTERPARTY_ID | Copy and Reference Table | PARTICIPANT_COMPANY_COUNTERPARTY | CITI BANK | 10537001 |  |
|  |  |  | Default Target Value | 10537001 |  |
| CONTACT_PERSON | Constant |  |  |  | Test Trader |
| CURRENCY1 | Copy and Reference Table | CURRENCY_CODE1 |  |  |  |
| CURRENCY2 | Copy and Reference Table | CURRENCY_CODE2 |  |  |  |
| EXPIRY_DATE | Copy | MATURITY_DATE |  |  |  |
| EXPIRY_LOCATION | Copy and Reference Table | EXPIRY_TIME | Default Target ValueNew York 10:00Frankfurt 15:00 | DEFRUSNYDEFR |  |
| EXPIRY_TIME | Copy and Reference Table | EXPIRY_TIME | Default Target ValueNew York 10:00Frankfurt 15:00 | 15:00:0010:00:0015:00:00 |  |
| FIXING_REFERENCE_ID | Copy and Reference Table | FIXING_REFERENCE | Default Target Value | ECB37 EUR/USD |  |
| FIXING_REFERENCE_PRE_AGREED_INDICATOR | Copy and Reference Table | FIXING_REFERENCE | Default Target Value | FALSE |  |
| OPPOSITE_CURRENCY | Copy and Reference Table | DERIVED_OPPOSITE_CURRENCY_CODE |  |  |  |
| PREMIUM_CURRENCY | Copy and Reference Table | PREMIUM_CURRENCY_CODE |  |  |  |
| TRADED_CURRENCY | Copy and Reference Table | NOTIONAL_CURRENCY_CODE |  |  |  |
| TRADER | Copy and Reference Table | PARTICIPANT_INDIVIDUAL_REQUESTOR |  |  |  |

360T-outbound

| Field | Mapping Type | Source Field | Source Value | Target Value | Constant |
| --- | --- | --- | --- | --- | --- |
| INDIVIDUAL | Copy and Reference Table | DERIVED_LOGON_USER |  | <Your 360T user> |  |
| LEGAL_ENTITY | Copy and Reference Table | COMPANY_ID | 1010 | <Your Company's account in 360T> |  |
| CURRENCY_CODE | Copy and Reference Table | CURRENCY_CODE |  |  |  |
| EXPIRY_TIME_LOCATION_PART | Copy and reference Table | EXPIRY_LOCATION | USNYDEFRDefault Target Value | New YorkFrankfurtFrankfurt |  |

Generic Format-Inbound

| Field | Mapping Type | Source Field | Source Value | Target Value | Constant |
| --- | --- | --- | --- | --- | --- |
| COMPANY_ID | Copy and Reference Table | LEGAL_ENTITY | SAP SE | 1710 |  |
|  |  |  | Default Target Value | 1010 |  |
| COUNTERPARTY_ID | Copy and Reference Table | COUNTER_PARTY | CITI BANK | 10537001 |  |
|  |  |  | Default Target Value | 10537001 |  |
| CONTACT_PERSON | Constant |  |  |  | Test Trader |
| CURRENCY1 | Copy and Reference Table | CURRENCY_CODE1 |  |  |  |
| CURRENCY2 | Copy and Reference Table | CURRENCY_CODE2 |  |  |  |
| EXPIRY_DATE | Copy | EXPIRY_DATE |  |  |  |
| EXPIRY_LOCATION | Copy and Reference Table | EXPIRY_LOCATION | Default Target ValueUSNYDEFR | DEFRUSNYDEFR |  |
| EXPIRY_TIME | Copy and Reference Table | EXPIRY_TIME | Default Target Value10:00:0015:00:00 | 15:0010:0015:00 |  |
| OPPOSITE_CURRENCY | Copy and Reference Table | DERIVED_OPPOSITE_CURRENCY_CODE |  |  |  |
| PREMIUM_CURRENCY | Copy and Reference Table | PREMIUM_CURRENCY_CODE |  |  |  |
| SETTLEMENT_CURRENCY | Copy and Reference Table | SETTLEMENT_CURRENCY_CODE |  |  |  |
| TRADED_CURRENCY | Copy and Reference Table | TRADED_CURRENCY_CODE |  |  |  |
| TRADER | Copy and Reference Table | PARTICIPANT_INDIVIDUAL_REQUESTOR |  |  |  |
| SECURI-TIES_ACCOUNT_ID | Copy or Reference Table | SECURI-TIES_ACCOUNT_ID |  |  |  |
| SECURI-TIES_ACCOUNT_NAME | Copy and Reference Table | SECURI-TIES_ACCOUNT_NAME |  |  |  |
| SECURI-TIES_ID_TYPE | Copy and Reference Table | SECURI-TIES_ID_TYPE |  |  |  |
| SECURITIES_ID_VALUE | SECURITIES_ID_VALUE | SECURITIES_ID_VALUE | SECURITIES_ID_VALUE | SECURITIES_ID_VALUE |  |
|  | SECURITIES_ID_VALUE | SECURITIES_ID_VALUE | SECURITIES_ID_VALUE | MMF_DE1 |  |
| SECURITIES_NAME | Copy and Reference Table | SECURI-TIES_NAME |  |  |  |

Generic Format-Outbound

| Field | Mapping Type | Source Field | Source Value | Target Value | Constant |
| --- | --- | --- | --- | --- | --- |
| TRADER | Copy | DERIVED_LOGON_USER |  |  |  |
| LEGAL_ENTITY | Constant |  |  |  | TEST |

#### Configure Mappings - Back-End Format

|  |
| --- |
| Remember The sample value provided below are for DE. Substitute the country/region-specific values provided by Best Practices for SAP S/4HANA or use master data values you have created for this purpose. |

Inbound

| Field | Mapping Type | Source Field | Source Value | Target Value | Constant |
| --- | --- | --- | --- | --- | --- |
| COMPANY_CODE | Copy and Reference Table | COMPANY_ID | Default Target Value | 1010 |  |
| FLOW_TYPE | Copy and Reference Table | DERIVED_INSTRUMENT_CATEGORY | Default Target Value | 1300 |  |
| PARTNER | Copy | COUNTERPARTY_ID |  |  |  |
| PRODUCT_TYPE | Copy and Reference Table | DERIVED_INSTRUMENT_CATEGORY | FX_COLLAR_BUY | 76A |  |
|  | Copy and Reference Table | DERIVED_INSTRUMENT_CATEGORY | FX_COLLAR_SELL | 76A |  |
|  | Copy and Reference Table | DERIVED_INSTRUMENT_CATEGORY | FX_FORWARD | 60A |  |
|  | Copy and Reference Table | DERIVED_INSTRUMENT_CATEGORY | FX_NDF | 60B |  |
|  | Copy and Reference Table | DERIVED_INSTRUMENT_CATEGORY | FX_SPOT | 60A |  |
|  | Copy and Reference Table | DERIVED_INSTRUMENT_CATEGORY | FX_OPTION_BUY | 76A |  |
|  | Copy and Reference Table | DERIVED_INSTRUMENT_CATEGORY | FX_OPTION_SELL | 76A |  |
|  | Copy and Reference Table | DERIVED_INSTRUMENT_CATEGORY | FX_SWAP_SPOT | 60A |  |
|  | Copy and Reference Table | DERIVED_INSTRUMENT_CATEGORY | FX_SWAP_FORWARD | 60A |  |
|  | Copy and Reference Table | DERIVED_INSTRUMENT_CATEGORY | FX_NDS_NDF | 60B |  |
|  | Copy and Reference Table | DERIVED_INSTRUMENT_CATEGORY | MM_DEALFT_INVEST | 55A |  |
|  | Copy and Reference Table | DERIVED_INSTRUMENT_CATEGORY | MM_DEALFT_BORROW | 55A |  |
|  | Copy and Reference Table | DERIVED_INSTRUMENT_CATEGORY | Default Target Value | 60A |  |
| TRANSACTION_TYPE | Copy and Reference Table | DERIVED_INSTRUMENT_CATEGORY | FX_FORWARD | 102 |  |
|  | Copy and Reference Table | DERIVED_INSTRUMENT_CATEGORY | FX_SPOT | 101 |  |
|  | Copy and Reference Table | DERIVED_INSTRUMENT_CATEGORY | FX_NDF | 110 |  |
|  | Copy and Reference Table | DERIVED_INSTRUMENT_CATEGORY | FX_NDS_NDF | 110 |  |
|  | Copy and Reference Table | DERIVED_INSTRUMENT_CATEGORY | FX_SWAP_SPOT | 101 |  |
|  | Copy and Reference Table | DERIVED_INSTRUMENT_CATEGORY | FX_SWAP_FORWARD | 102 |  |
|  | Copy and Reference Table | DERIVED_INSTRUMENT_CATEGORY | FX_OPTION_BUY | 100 |  |
|  | Copy and Reference Table | DERIVED_INSTRUMENT_CATEGORY | FX_OPTION_SELL | 200 |  |
|  | Copy and Reference Table | DERIVED_INSTRUMENT_CATEGORY | FX_COLLAR_BUY | 100 |  |
|  | Copy and Reference Table | DERIVED_INSTRUMENT_CATEGORY | FX_COLLAR_SELL | 200 |  |
|  | Copy and Reference Table | DERIVED_INSTRUMENT_CATEGORY | FX_NDS_NDF | 110 |  |
|  | Copy and Reference Table | DERIVED_INSTRUMENT_CATEGORY | MM_DEALFT_INVEST | 100 |  |
|  | Copy and Reference Table | DERIVED_INSTRUMENT_CATEGORY | MM_DEALFT_BORROW | 200 |  |
|  | Copy and Reference Table | DERIVED_INSTRUMENT_CATEGORY | SEC_MMF_ORDER_VERIFIED_PURCHASE | 101 |  |
|  | Copy and Reference Table | DERIVED_INSTRUMENT_CATEGORY | SEC_MMF_TRANS_PRICED_PURCHASE | 101 |  |
|  | Copy and Reference Table | DERIVED_INSTRUMENT_CATEGORY | SEC_MMF_DIV_REINVESTED_PURCHASE | 500 |  |
|  | Copy and Reference Table | DERIVED_INSTRUMENT_CATEGORY | SEC_MMF_REB_REINVESTED_PURCHASE | 300 |  |
|  | Copy and Reference Table | DERIVED_INSTRUMENT_CATEGORY | SEC_MMF_ORDER_VERIFIED_SALE | 201 |  |
|  | Copy and Reference Table | DERIVED_INSTRUMENT_CATEGORY | SEC_MMF_TRANS_PRICED_SALE | 201 |  |
|  | Copy and Reference Table | DERIVED_INSTRUMENT_CATEGORY | SEC_MMF_DIV_REINVESTED_SALE | 600 |  |
|  | Copy and Reference Table | DERIVED_INSTRUMENT_CATEGORY | SEC_MMF_REB_REINVESTED_SALE | 400 |  |
|  | Copy and Reference Table | DERIVED_INSTRUMENT_CATEGORY | Default Target Value | 102 |  |
| SECURITIES_ACCOUNT | Copy and Reference Table | SECURITIES_ACCOUNT_ID | BLOOMBERG |  |  |
|  | Copy and Reference Table | SECURITIES_ACCOUNT_ID | Default Target Value |  |  |
| SECURITIES_INTERNAL_ID | Copy and Reference Table | DERIVED_SECURITIES_ID_VALUE | BLOOMBERG_BL1010 |  |  |
|  |  | DERIVED_SECURITIES_ID_VALUE | Default Target Value |  |  |
| SECURITIES_ALTERNATIVE_ID_VALUE | Copy and Reference Table | DERIVED_SECURITIES_ID_VALUEDERIVED_SECURITIES_ID_VALUE | BLOOMBERG_BL1010 |  |  |
|  | Copy and Reference Table | DERIVED_SECURITIES_ID_VALUEDERIVED_SECURITIES_ID_VALUE | Default Target Value |  |  |

Outbound

| Field | Mapping Type | Source Field | Source Value | Target Value | Constant |
| --- | --- | --- | --- | --- | --- |
| CHANGE_ALLOWED_INDICATOR | Constant |  |  |  | TRUE |
| COMPANY_ID | Copy | COMPANY_CODE |  |  |  |
| EXECUTION_TYPE | Constant |  |  |  | RFQ |
| EXERCISE_TYPE | Copy | EXERCISE_TYPE |  |  |  |
| EXPIRY_LOCATION | Constant |  |  |  | NWYK |
| EXPIRY_TIME | Constant |  |  |  | 15:00:00 |
| PREMIUM_CURRENCY | Copy | PREMIUM_CURRENCY_ISO |  |  |  |

#### Configure Mappings - Back-End Format (Intercompany)

|  |
| --- |
| Remember The sample value provided below are for DE. Substitute the country/region-specific values provided by Best Practices for SAP S/4HANA or use master data values you have created for this purpose. |

Inbound

| Field | Mapping Type | Source Field | Source Value | Target Value | Constant |
| --- | --- | --- | --- | --- | --- |
| COMPANY_CODE | Copy | COMPANY_ID |  |  |  |
| FLOW_TYPE | Constant |  |  |  | 1300 |
| PARTNER | Copy and Reference Table | COUNTERPARTY_COMPANY_ID | 1010 | 10401010 |  |
| 1710 | 17401710 |  |  |  |  |
| PRODUCT_TYPE | Copy and Reference Table | DERIVED_INSTRUMENT_CATEGORY | FX_COLLAR_BUY | 76A |  |
| FX_COLLAR_SELL | 76A |  |  |  |  |
| FX_FORWARD | 60A |  |  |  |  |
| FX_NDF | 60B |  |  |  |  |
| FX_SPOT | 60A |  |  |  |  |
| FX_OPTION_BUY | 76A |  |  |  |  |
| FX_OPTION_SELL | 76A |  |  |  |  |
| FX_SWAP_SPOT | 60A |  |  |  |  |
| FX_SWAP_FORWARD | 60A |  |  |  |  |
| FX_NDS_FX_NDF | 60B |  |  |  |  |
| MM_DEALFT_INVEST | 55A |  |  |  |  |
| MM_DEALFT_BORROW | 55A |  |  |  |  |
| Default Target Value | 60A |  |  |  |  |
| TRANSACTION_TYPE | Copy and Reference Table | DERIVED_INSTRUMENT_CATEGORY | FX_FORWARD | 102 |  |
| FX_SPOT | 101 |  |  |  |  |
| FX_NDF | 110 |  |  |  |  |
| FX_NDS_NDF | 102 |  |  |  |  |
| FX_SWAP_SPOT | 101 |  |  |  |  |
| FX_SWAP_FORWARD | 102 |  |  |  |  |
| FX_OPTION_BUY | 100 |  |  |  |  |
| FX_OPTION_SELL | 200 |  |  |  |  |
| FX_COLLAR_BUY | 100 |  |  |  |  |
| FX_COLLAR_SELL | 200 |  |  |  |  |
| FX_NDS_FX_NDF | 110 |  |  |  |  |
| MM_DEALFT_INVEST | 100 |  |  |  |  |
| MM_DEALFT_BORROW | 200 |  |  |  |  |
| Default Target Value | 102 |  |  |  |  |
| CONTACT_PERSON | Copy | CONTACT_PERSON |  |  |  |
| EXPIRY_LOCATION | Copy | EXPIRY_LOCATION |  |  |  |

Outbound

| Field | Mapping Type | Source Field | Source Value | Target Value | Constant |
| --- | --- | --- | --- | --- | --- |
| CHANGE_ALLOWED_INDICATOR | Constant |  |  |  | TRUE |
| COMPANY_ID | Copy | COMPANY_CODE |  |  |  |
| EXECUTION_TYPE | Constant |  |  |  | RFQ |
| EXERCISE_TYPE | Copy | EXERCISE_TYPE |  |  |  |
| EXPIRY_LOCATION | Copy and Reference Table | EXPIRY_LOCATION |  |  |  |
| EXPIRY_TIME | Copy | EXPIRY_TIME |  |  |  |
| PREMIUM_CURRENCY | Copy | PREMIUM_CURRENCY_ISO |  |  |  |

### Business Rules Settings Example

A full business rule example is listed as below for your reference. You may adjust the mappings according to your business requirement.

#### Configure Business Rules

|  |
| --- |
| Remember The sample value provided below are for DE. Substitute the country/region-specific values provided by Best Practices for SAP S/4HANA or use master data values you have created for this purpose. |

##### Counterparty

Table 13: Derivation of Authorized Instrument Categories

| If | Then Counterparty Authorization Instrument Category |
| --- | --- |
| Input for Authorized Instruments Derivation.Product Type = '60A' | 'FX_SPOT' |
| Input for Authorized Instruments Derivation.Product Type = '60A' | 'FX_FORWARD' |
| Input for Authorized Instruments Derivation.Product Type = '60A' | 'FX_SWAP' |
| Input for Authorized Instruments Derivation.Product Type = '60B' | 'FX_NDF' |
| Input for Authorized Instruments Derivation.Product Type = '60B' | 'FX_NDS' |
| Input for Authorized Instruments Derivation.Product Type = '76A' | 'FX_OPTION' |
| Input for Authorized Instruments Derivation.Product Type = '76A' | 'FX_COLLAR' |

Table 14: Derivation of Counterparty Role

| If | Then Counterparty Role |
| --- | --- |
| TRUE | 'TR0151' |

Table 15: Derivation of Preferred Counterparties

| If | Then Preferred Counterparty |
| --- | --- |
| Input for Preferred Counterparties Derivation.Instrument Category = 'FX_FORWARD' | '17537001' |
| TRUE | '17537001' |

##### Counterparty Limit

Table 16: Derivation of Counterparty Limit Types

| If | Then Limit Type |
| --- | --- |
| TRUE | 'Y07' |
| TRUE | 'Y13' |
| TRUE | 'Y26' |

Table 17: Derivation of FX Instrument Limit Check Parameters

| If | Then Transaction Type | Product Type |
| --- | --- | --- |
| Input for FX Instrument Limit Check.Instrument Category = 'FX_FORWARD' | '102' | '60A' |
| Input for FX Instrument Limit Check.Instrument Category = 'FX_NDF' | '110' | '60B' |
| Input for FX Instrument Limit Check.Instrument Category = 'FX_SWAP' AND Input for FX Instrument Limit Check.Leg Type = 'NEAR_LEG' | '101' | '60A' |
| Input for FX Instrument Limit Check.Instrument Category = 'FX_SWAP' AND Input for FX Instrument Limit Check.Leg Type = 'FAR_LEG' | '102' | '60A' |
| Input for FX Instrument Limit Check.Instrument Category = 'FX_OPTION' AND Input for FX Instrument Limit Check.Activity Type = 'BUY' | '100' | '76A' |
| Input for FX Instrument Limit Check.Instrument Category = 'FX_OPTION' AND Input for FX Instrument Limit Check.Activity Type = 'SELL' | '200' | '76A' |
| Input for FX Instrument Limit Check.Instrument Category = 'FX_COLLAR' AND Input for FX Instrument Limit Check.Activity Type = 'BUY' | '100' | '76A' |
| Input for FX Instrument Limit Check.Instrument Category = 'FX_COLLAR' AND Input for FX Instrument Limit Check.Activity Type = 'SELL' | '200' | '76A' |

Table 18: Derivation of ICO Counterparty Limit Types

| If | Then Limit Type | Limit Type Default | Limit Type ID |
| --- | --- | --- | --- |
|  |  |  |  |

Table 19: Derivation of MM Instrument Limit Check Parameters

| If | Then Transaction Type | Product Type |
| --- | --- | --- |
|  |  |  |

Table 20: Settings for Counterparty Limit Check

| If | Then Limit Type ID | Limit Type |
| --- | --- | --- |
| Input for Settings for Counterparty Limit Check.Instrument Group = 'FX' | 'FX' | 'Y07' |
| Input for Settings for Counterparty Limit Check.Instrument Group = 'FX' | 'FX' | 'Y13' |
| Input for Settings for Counterparty Limit Check.Instrument Group = 'FX' | 'FX' | 'Y26' |

##### External Trading

Table 21: Decision for Foreign Exchange Instrument Category

| If | Then Instrument Category |
| --- | --- |
| Input for FX Instrument Category Decision.Instrument Category = 'FX_UNDEF' | 'FX_FORWARD' |

Table 22: Decision for Money Market Instrument Category

| If | Then Instrument Category | Interest Rate Category |
| --- | --- | --- |
| TRUE | 'MM_DEALFT' | 'FIXED' |

Table 23: Decision for Trading Scenario

| If | Then Scenar-io |
| --- | --- |
| Input for Trading Scenario Decision.On Behalf Of Company = '1710' | '5' |

##### Intercompany Trading

Table 24: Decision for Creating Intercompany Trades

| If | Create for Subsidiary | Create for Subsidiary |
| --- | --- | --- |
| Input for Intercompany Trades Creation Decision.Subsidiary Company ID = '1710' | TRUE | TRUE |

Table 25: Decision for Foreign Exchange Instrument Category

| If | Instrument Category |
| --- | --- |
| Input for FX Instrument Category Deci-sion.Instrument Category = 'FX_UNDEF' | 'FX_FORWARD' |

Table 26: Decision for Intercompany Trading Scenario

| If | Then Scenario |
| --- | --- |
| Input for Intercompany Trading Scenario Decision.Company ID = '1710' AND Input for Intercompany Trading Scenario Decision.Assignment = 'B2B_TRADING_SB' | '1' |
| Input for Intercompany Trading Scenario Decision.Company ID = '1710' AND Input for Intercompany Trading Scenario Decision.Assignment = 'MANUAL_TRADING' | '2' |
| Input for Intercompany Trading Scenario Decision.Company ID = '1710' AND Input for Intercompany Trading Scenario Decision.Assignment = 'AUTO_TRADING' | '3' |
| Input for Intercompany Trading Scenario Decision.Company ID = '1710' AND Input for Intercompany Trading Scenario Decision.Assignment = 'TRADING_VIA_TP' | '4' |
| Input for Intercompany Trading Scenario Decision.Company ID = '1710' ANDInput for Intercompany Trading Scenario Decision.Instrument Category = 'MM_DEALFT'AND Input for Intercompany Trading Scenario Decision.Nominal Amount Currency = 'EUR' | '1' |
| Input for Intercompany Trading Scenario Decision.Company ID = '1710' ANDInput for Intercompany Trading Scenario Decision.Instrument Category = 'MM_DEALFT'AND Input for Intercompany Trading Scenario Decision.Nominal Amount Currency = 'USD' | '2' |
| Input for Intercompany Trading Scenario Decision.Company ID = '1710' ANDInput for Intercompany Trading Scenario Decision.Instrument Category = 'MM_DEALFT'AND Input for Intercompany Trading Scenario Decision.Nominal Amount Currency = 'JPY' | '4' |
| TRUE | '1' |

Table 27: Decision for Money Market Instrument Category

| If | Then Instrument Category | Interest Rate Category |
| --- | --- | --- |
| TRUE | 'MM_DEALFT' | 'FIXED' |

Table 28: Decision for Trade Request Routing Category

| If | Then Trade Request Routing Category |
| --- | --- |
| Input for Trade Request Routing Category Decision.Leg 1 On Behalf Of Company = '1710' | 'EXTERNAL' |
| Input for Trade Request Routing Category Decision.Company Code = '1710' | 'INTERNAL' |
| TRUE | 'EXTERNAL' |

Table 29: Derivation of Values for Trade Request

| If | Then Company ID | Heding Area |
| --- | --- | --- |
| Input for Derivation of Trade Request Values.Company ID = '1710' | '1010' | Input for Derivation of Trade Request Values.Hedging Area |

Table 30: Derivation of Values for Trade Request V2

| If | Leg 2 On Behalf Of Company | Leg 1 On Behalf Of Company |
| --- | --- | --- |
| TRUE | Input for Derivation of Trade Request Values V2.Leg 2 On Behalf Of Company | Input for Derivation of Trade Request Values V2.Leg 1 On Behalf Of Company |

Table 31: Derive which trading partners to use

| If | Then Treasury Center Company ID | Subsidiary Company ID |
| --- | --- | --- |
| Input for Intercompany Trading Partners Derivation.Company ID EXISTSIN [ '1710' ] | '1010' | Input for Intercompany Trading Partners Derivation.Company ID |

##### Market Data Adapter

Table 32: Decision for MM Markup or Markdown

| If | Value |
| --- | --- |
| Input for MM Markup Markdown Value Derivation.Company ID = '1010' | 0.01 |

| If | Then Format | Value |
| --- | --- | --- |
| Markup or Markdown Decision Input.Subsidiary Company ID = '1710' AND Markup or Markdown Decision Input.Instrument Category = 'FX_FORWARD' | 'PERCENTAGE' | 1 |
| Markup or Markdown Decision Input.Subsidiary Company ID = '1710' AND Markup or Markdown Decision Input.Instrument Category = 'FX_OPTION' | 'BASIC' | 0.1 |
| TRUE | 'BASIC' | 0.2 |

Table 33: Decision for Quotation Source

| If | Then Exchange Rate Type | Quotation Source Type |
| --- | --- | --- |
| Quotation Source Decision Input.Subsidiary Company ID = '1710' | 'M' | 'SAP_S4' |

Table 34: Decision for Retrieving Rate for Manual Trading

| If | ThenRetrieve Rate Enabled |
| --- | --- |
| Retrieve Rate Decision Input.Instrument Category = 'FX_NDF' | true |
| Retrieve Rate Decision Input.Instrument Category = 'FX_SPOT' | true |
| Retrieve Rate Decision Input.Instrument Category = 'FX_FORWARD' | true |

Table 35: Derivation of Allowed Reference Interest Rates

| If | Default Interest Calculation Method | Default Interest Calculation Method |
| --- | --- | --- |
| Input for Reference Interest Rates Derivation.Nominal Amount Currency = 'EUR' | 'EURM01EUR' | 'ACT/360' |
| Input for Reference Interest Rates Derivation.Nominal Amount Currency = 'EUR' | 'EURM03EUR' | 'ACT/360' |

##### Counterparty Mapping

Please use the app Manage Counterparties to create following counterparties.

Table 36:

| Counterparty | Trading Platform Configuration | Counterparty ID (Trading Platform) | Back-End Configuration | Business Partner | Allocated Company ID |
| --- | --- | --- | --- | --- | --- |
| 10537001 | 360T | CITI BANK | <Your S/4HANACloud> | 10537001 |  |
| 10401010 |  |  | <Your S/4HANACloud> | 10401010 | 10401010 |
| 17401710 |  |  | <Your S/4HANACloud> | 17401710 | 17401710 |

### Useful Resources

Useful Resources

Please refer to below resources for further details.

| Item | Link |
| --- | --- |
| Treasury Management Integration for Trading Platforms | https://help.sap.com/viewer/product/TRADING_PLATFORM_INTEGRATION |

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
> Flagged while digesting this document, not verified: In the Back-End Format (Intercompany) inbound mapping, TRANSACTION_TYPE for FX_NDS_NDF is 102, while the same key maps to 110 in the external Back-End Format inbound mapping, and FX_NDS_FX_NDF maps to 110 within the intercompany table itself.

## Connections
- part-of :: [[_cluster]]
- related-to :: [[05-treasury-and-cash-management/test-script-treasury-trading-via-trading-platforms-2f5-sap-s-4hana-clo-part-01]]
- related-to :: [[05-treasury-and-cash-management/treasury-correspondence-integration-with-swift-network-3qm-test-script]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/2F5_S4CLD2608_BPD_EN_XX.docx` — lines 3619–4517 of the extracted text · extracted with `mammoth` · 302,966 chars in the whole document
